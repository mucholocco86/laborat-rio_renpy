init:
    $ v_ep03_01_05_shopping_with_Ariel = 0
    $ v_ep03_01_06_ariel_kiss = False
    $ v_ep03_01_06_continue_talking_with_Vivian = False
    $ v_ep03_ariel_fantasy_counter = 0
    $ v_ep03_01_06_vivian_knock_door = False



label lb_ep03_01_06_Vivian_waits_for_the_MC_in_her_room:
    scene black
    with dissolve
    pause 1.0
    centered "Later that night...{w=2.0}{nw}" with dissolve
    show text "Later that night..."
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/02/Sibling Dispute1.mp3" loop fadein 1.0
    #show the MC walking upstairs on his way to his bedroom
    scene sc vivinvitesmc d001
    with dissolve
    pause 2.0
    show sc vivinvitesmc d002
    with dissolve
    pause 2.0
    #he sees Ariel coming out of the bathroom
    show sc vivinvitesmc d003
    mc"Hey [a_name]."
    show sc vivinvitesmc d004
    a"Hey..."
    show sc vivinvitesmc d005
    a"Were you about to go to bed?"
    show sc vivinvitesmc d006
    mc"Yeah, I was."
    show sc vivinvitesmc d007
    mc"Say, where’s [b_name]?"
    show sc vivinvitesmc d008
    a"She’s already called it a night."
    show sc vivinvitesmc d009
    a"She tried to talk with [mc_v_address] but she wouldn’t come to the door."
    show sc vivinvitesmc d010
    mc"Maybe she’s gone to bed already?"
    show sc vivinvitesmc d011
    a"I guess."
    show sc vivinvitesmc d012
    a"I hope she’s okay."
    show sc vivinvitesmc d013
    a"Will you talk to her if you get the chance?"
    show sc vivinvitesmc d014
    mc"It doesn’t seem like she wants to talk to anybody at the moment, [a_name]."
    show sc vivinvitesmc d015
    mc"But I’ll see how she is in the morning."
    show sc vivinvitesmc d016
    a"Yeah, good idea."
    show sc vivinvitesmc d017
    a"Okay, well... I’m going to bed."
    show sc vivinvitesmc d018
    a"I’m pretty tired and I’d rather not be awake when [mc_vic_address] comes back."
    show sc vivinvitesmc d019
    mc"I can totally understand that."
    #[Hug her / Kiss her / Say Goodnight]
    menu:
        "Hug her"(wt="Bonus Image"):
            #the MC hugs Ariel
            show sc vivinvitesmc d020
            with dissolve
            pause 1.0
            show sc vivinvitesmc d021
            with dissolve
            a"Mmm..."
            $ rewards_unlock ("ariel",11)
            show sc vivinvitesmc d022
            a"I just wish things could be easier, and we could all lead a normal life one day, you know?"
            #They speak to each other while hugging
            show sc vivinvitesmc d023
            mc"Yeah, I feel the same."
            #the break the hug
            show sc vivinvitesmc d024
            mc"And who knows? Maybe one day if we’re lucky, we’ll get there."
            show sc vivinvitesmc d025
            a"I hope so."
            #she doesn’t seem so sure
            show sc vivinvitesmc d026
            mc"Goodnight, [a_name]."
            show sc vivinvitesmc d027
            a"Night, [y_name]."
            #she smiles
            #the MC watches her walk to her bedroom door - show a behind shot of Ariel
            #then disappearing into her room
            show sc vivinvitesmc d028
            with dissolve
            pause 1.5
        "Kiss her"(wt="Best option"):
            show screen scr_secret_icon("v_secrets_ep03_01_06_1") onlayer ontop
            with { "ontop": dissolve}
            show sc vivinvitesmc d022
            a"I just wish things could be easier, and we could all lead a normal life one day, you know?"
            show sc vivinvitesmc d023
            mc"Yeah, I feel the same."
            $ v_ep01_ariel_respect_counter += 1
            #the break the hug
            show sc vivinvitesmc d024
            show screen scr_secret_hotspot ("sc vivinvitesmc d024","1110, 956, 112, 115","v_secrets_ep03_01_06_1")
            mc"And who knows? Maybe one day if we’re lucky, we’ll get there."
            hide screen scr_secret_hotspot
            show sc vivinvitesmc d025
            a"I hope so."
            #she doesn’t seem so sure
            show sc vivinvitesmc d026
            mc"Goodnight, [a_name]."
            if ariel_love_level >= 2:
                #If the player has 2 or more Ariel Hearts
                play sound "sound effects/01/kiss_and_moan_sound_effect01.mp3" noloop
                show sc vivinvitesmc d030
                with dissolve
                pause 2.0
                a"Mmm..."
                stop sound fadeout 1.0
                #The MC kisses Ariel on the lips, they close their eyes as they embrace
                show sc vivinvitesmc d027
                a"Night, [y_name]."
                $ v_ep03_01_06_ariel_kiss = True
                $ v_ep03_01_05_shopping_with_Ariel +=1
                #the MC watches her walk to her bedroom door - show a behind shot of Ariel
                #then disappearing into her room
                show sc vivinvitesmc d028
                with dissolve
                pause 0.5
            else:
                #SOUND EFFECT
                play sound "sound effects/01/Male_kissing_girl_on_the_cheek.mp3" noloop
                show sc vivinvitesmc d029
                mc"Mwah!"
                #Ariel smiles The MC kisses her on the cheek
                show sc vivinvitesmc d027
                a"Night, [y_name]."
                $ v_ep03_01_05_shopping_with_Ariel +=1
                #the MC watches her walk to her bedroom door - show a behind shot of Ariel
                #then disappearing into her room
                show sc vivinvitesmc d028
                with dissolve
                pause 0.5
            hide screen scr_secret_icon onlayer ontop
            with { "ontop": dissolve}
        "Say goodnight":
            show sc vivinvitesmc d026
            mc"Goodnight, [a_name]."
            show sc vivinvitesmc d027
            a"Night, [y_name]."
            #she smiles
            #the MC watches her walk to her bedroom door - show a behind shot of Ariel
            show sc vivinvitesmc d028
            with dissolve
            pause 0.5
    show sc vivinvitesmc d028a
    with dissolve
    pause 1.0
    play sound "sound effects/01/door_close_soft.mp3" noloop
    show sc vivinvitesmc d028b
    with dissolve
    pause 1.0
    #then disappearing into her room
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    if persistent.v_secrets_enabled and persistent.v_secrets_ep03_01_06_1:
        jump lb_ep03_01_06_ariel_masturbating
    else:
        jump lb_ep03_01_06_vivian_door


label lb_ep03_01_06_ariel_masturbating:
    if not _in_replay:
        scene img_secret_scene_overlay onlayer anim_layer
        with { "anim_layer": dissolve}
    else:
        show screen scr_end_replay
    ##NOTE: The trigger for this scene should be placed in the “Kiss her" option (ABOVE)
    #### ARIEL NON-CANON SCENE
    $ v_ep03_ariel_fantasy_counter += 1
    #Ariel is standing in her room, standing, thinking about the kiss - still wearing the same clothes as she did in the previous scene
    play music "sound effects/01/Whispers of Love.mp3" loop fadein 2.0
    show sc arielbednc a00
    with dissolve
    pause 2.0
    show sc arielbednc a00a
    with dissolve
    pause 2.0
    #Show a flashback to Ariel and the MC kissing
    #flash returns to back in her room
    #she slides down her pink shorts so we see her in her white underwear - https://pixhost.to/show/748/529248070_prev1.jpg
    show sc arielbednc a01
    with dissolve
    a"Mmm..."
    show sc arielbednc a02
    with dissolve
    a"([y_name] ... the things you do to me.)"
    #https://pixhost.to/show/748/529248079_prev2.jpg
    a"(I need to find some kind of release.)"
    #Ariel wanders over to her bed
    #she sits on her bed, then spreads her legs
    #she rubs herself over the top of her panties
    show sc arielbednc a03
    a"Ohh..."
    #show a close-up of this
    #Ariel then rests her hand on her lower stomach, just above her panty-line
    #she then slides her hand inside underwear - https://pixhost.to/show/748/529248087_prev4.jpg
    show sc arielbednc a01
    a"NGHH!"
    #ANIMATED SCENE - Ariel touching herself
    #show an expanded shot - https://pixhost.to/show/748/529248082_prev3.jpg
    show sc arielbednc a02
    a"Oooh..."
    #show this angle - https://pixhost.to/show/748/529248089_prev5.jpg
    #she stops masturbating - show Ariel’s face
    show sc arielbednc a04
    a"(Why doesn’t this feel as good as it normally does?)"
    show sc arielbednc a04a
    a"Hmm..."
    pause 0.5
    #Ariel looks up slightly, thinking back
    #screen flashes
    stop music fadeout 1.0
    #she has a flashback to Bella being in her room, giving her a special gift on her 18th birthday.
    #they sit on Ariel’s bed, next to each other
    play music "sound effects/01/Frayed_Relations2.mp3" loop fadein 3.0
    show sc arielbednc a05
    with flash(0.50, 0, 0.75, "#fff")
    b"So I have one last birthday gift for you, [a_name]."
    show sc arielbednc a05a
    b"I just couldn’t give it to you earlier, not in front of the [private_group]."
    show sc arielbednc a06
    b"Here..."
    #Bella hands her a box, that has a sex toy inside.
    show sc arielbednc a07
    a"What is it?"
    show sc arielbednc a08
    b"If I were to tell you, then that would spoil the surprise, silly."
    show sc arielbednc a14
    b"Go on, open it."
    show sc arielbednc a09
    a"Oh, is this what I think it is?"
    show sc arielbednc a11
    b"I certainly hope so!"
    show sc arielbednc a12
    a"But why would I need something like this?"
    show sc arielbednc a15
    b"Let’s just say that it will come in handy for those special moments, especially when you need some extra \"inspiration\"."
    show sc arielbednc a10
    a"I don’t know, [b_name]."
    show sc arielbednc a12
    a"I mean, I appreciate the gift and all, but I can’t see myself ever using it."
    show sc arielbednc a13
    b"You say that now, [a_name]."
    show sc arielbednc a14
    b"But trust me, you’ll be thanking me for this soon enough."
    stop sound fadeout 1.0
    #Ariel gives Bella an unsure look
    show sc arielbednc a15
    with dissolve
    pause 1.5
    #She then looks down at the sex toy (vibrator)
    show sc arielbednc a16
    with flash(0.50, 0, 0.75, "#fff")
    pause 0.5
    #screen flashes
    #we return to the present day with Ariel still looking at the same sex toy Bella gave her
    play music "sound effects/01/Seducing the Officer.mp3" loop fadein 1.0
    show sc arielbednc a17
    with dissolve
    pause 1.5
    #She lays back, pulls down her underwear
    #Ariel spreads her legs apart
    show sc arielbednc a18
    with dissolve
    pause 2.0
    #she rubs the tip of the dildo against her pussy
    show sc arielbednc a19
    with dissolve
    a"Nnn..."
    #She softly moans and has her eyes closed
    #show a close-up of the dildo rubbing up and down between her pussy lips
    #show Ariel’s face, biting her bottom lip
    #She then directs the tip at her opening
    #she slowly slides it into her pussy
    show sc arielbednc a20
    with dissolve
    a"OHH!"
    show sc arielbednc a21
    with dissolve
    pause 1.5
    #and quickly withdraws (because she’s a virgin)
    show sc arielbednc a22
    with dissolve
    pause 1.5
    show sc arielbednc a23
    with dissolve
    pause 1.5
    show sc arielbednc a25
    with dissolve
    pause 1.5
    #Ariel is unsure and frustrated.
    show sc arielbednc a26
    with dissolve
    a"(Sigh... No, I can’t lose my virginity like this.)"
    show sc arielbednc a27
    with dissolve
    a"(Hmm... I wonder what this button does.)"
    #She then looks at the dildo closer and sees a flick button at the opposite end of the toy
    play sound "sound effects/01/sex/Buzzing_noise_Sound_FX.ogg" loop fadein 0.5
    show sc arielbednc a28
    with dissolve
    pause 1.5
    #She turns it on and it starts buzzing
    show sc arielbednc a29
    with dissolve
    pause 1.5
    #SOUND EFFECT - for the buzzing noise
    #Ariel lays back, pulls her top up so we see the bottom of her breasts
    #Ariel carefully lays the vibrator against her pussy lips and gets a short little shock
    show sc arielbednc a30
    with dissolve
    pause 1.0
    a"(Oh my God!)"
    show sc arielbednc a31
    with dissolve
    a"(Haha... It kind of tickles.)"
    #She does it again and gets used to it, is happy, and starts moaning a little louder
    show sc arielbednc a32
    with dissolve
    a"Oh... my..."
    show sc arielbednc a33
    with dissolve
    a"(This is different... Definitely, different.)"
    #Ariel rubs her nipple through her top
    #show a shot of Ariel lying on the bed - show from the ceiling looking directly down at her
    show sc arielbednc a34
    with dissolve
    a"([b_name] was right...)"
    #Once she focuses the toy on her clit, she moans really loudly
    show sc arielbednc a35
    with dissolve
    a"(Oh geez...)"
    show sc arielbednc a23
    a"(I think I’m gonna lose it!)"
    show sc arielbednc a19
    with dissolve
    a"NGHH!!"
    #Ariel closes her eyes shut as she continues to pleasure herself
    show sc arielbednc a20
    with dissolve
    pause 1.0
    #screen flashes
    show sc arielbednc a37
    with dissolve
    pause 1.0
    #show the MC on top of her (Ariel’s POV view), insinuating that he is inside of her - but don’t show that, just his face and upper body, and don’t show the sex toy
    show sc arielbednc a38
    mc"Enjoying yourself, [a_name]?"
    #A second flash - shows Ariel climaxing
    show sc arielbednc a39
    with flash(0.15, 0, 0.75, "#fff")
    a"OHHH!!!"
    #screen flashes
    show sc arielbednc a39
    with flash(0.15, 0, 0.75, "#fff")
    a"Ohhh!"
    #Ariel then quickly covers her mouth
    show sc arielbednc a40
    a"(Oh no!)"
    stop sound fadeout 1.0
    show sc arielbednc a41
    a"(I hope nobody heard me.)"
    # maybe have bella knock on her door before the scene ends?
    show sc arielbednc a42
    with dissolve
    a"Mmm..."
    show sc arielbednc a43
    with dissolve
    a"(So worth it though...)"
    stop music fadeout 2.0
    #Show Ariel lying back on the bed with a satisfied look on her face, and her eyes closed
    #final shot - show a close-up of her pussy glistening from her juices
    #screen goes blank
    scene onlayer anim_layer
    with { "anim_layer": dissolve}
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ persistent.replay_ep03_ariel_bed_fantasy = False
    $ renpy.end_replay()
    jump lb_ep03_01_06_vivian_door


label lb_ep03_01_06_vivian_door:
    #scene continues with the MC coming out of the bathroom, wearing just his boxer shorts
    #he starts walking towards his room and then sees Vivian’s bedroom door.
    play music "sound effects/02/Counting Sheep.mp3" loop fadein 1.0
    show sc vivinvitesmc d031
    with dissolve
    mc"Hmm..."
    #[Go to bed / See if Vivian is awake]
    menu:
        "Go to bed":
            #the MC decides to go to his room to bed
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_02_01_Training_in_The_Park_with_Zora
        "See if [v_name] is awake"(wt="Best option"):
            $ v_ep03_01_06_vivian_knock_door = True
            #the MC knocks on her door
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3" noloop
            show sc vivinvitesmc d032
            with faster_dissolve
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock)"
                pause 2.0
            else:
                scene sc vivinvitesmc d032
                pause 2.0
            show sc vivinvitesmc d033
            with dissolve
            mc"..."
            show sc vivinvitesmc d034
            mc"[mc_v_address!c]?"
            show sc vivinvitesmc d035
            mc"Are you awake?"
            show sc vivinvitesmc d036
            v"Yes, I'm awake, but I don’t want to talk right now."
            #[Leave / Insist]
            menu:
                "Leave":
                    show sc vivinvitesmc d037
                    mc"Okay, I won’t disturb you."
                    show sc vivinvitesmc d038
                    mc"Goodnight, [mc_v_address!c]..."
                    #the MC walks away from her door and back to his room
                    #he looks downhearted
                    stop music fadeout 1.0
                    #SCENE ENDS
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    jump lb_ep03_02_01_Training_in_The_Park_with_Zora
                "Insist"(wt="Best option"):
                    show sc vivinvitesmc d039
                    mc"You can’t just shut us out, [mc_v_address]."
                    show sc vivinvitesmc d040
                    mc"We’re only doing this because we care."
                    show sc vivinvitesmc d041
                    mc"Because I care..."
                    show sc vivinvitesmc d042
                    mc"..."
                    mc"... ..."
                    show sc vivinvitesmc d042a
                    v"Okay, just give me a second."
                    pause 2.0
                    #Vivian opens the door
                    play sound "sound effects/01/Door_Opening.mp3" noloop
                    pause 1.0
                    show sc vivinvitesmc d043
                    with dissolve
                    mc"(Woah...)"
                    $ v_ep03_01_05_checking_on_Vivian_counter += 1
    #she’s wearing a nightwear slip - https://m.media-amazon.com/images/I/71si7x5tKoL._AC_UY1000_.jpg
    show sc vivinvitesmc d044a
    v"Hey, sweetheart."
    #She looks a little tipsy, after drinking some more wine
    show sc vivinvitesmc d048
    v"I thought for sure that you’d be asleep by now."
    show sc vivinvitesmc d046
    mc"I was just about to go to bed."
    show sc vivinvitesmc d047
    mc"I just needed to know that you were okay first."
    mc"The girls were really concerned about you, as was I."
    show sc vivinvitesmc d049
    v"I know, I heard them knock on my door earlier."
    show sc vivinvitesmc d048
    v"I didn’t want them to see me like this."
    show sc vivinvitesmc d046
    mc"Do you mean, really upset?"
    show sc vivinvitesmc d049
    v"Yeah..."
    show sc vivinvitesmc d056
    v"But I’m much better now, I promise."
    show sc vivinvitesmc d054
    mc"Good to hear."
    #[Say goodnight / Continue talking]
    menu:
        "Say goodnight":
            show sc vivinvitesmc d055
            mc"Anyway...I should get some rest as I have to be up in time to go with [a_name] to find some clothes at [b_name]’s store."
            show sc vivinvitesmc d048
            v"Of course."
            show sc vivinvitesmc d047
            mc"Are you sure you’re going to be all right?"
            show sc vivinvitesmc d049
            v"Honestly, you don’t have to keep asking me, [y_name]."
            show sc vivinvitesmc d046
            mc"Yeah, but what about [mc_vic_address]?"
            show sc vivinvitesmc d048
            v"I can handle him. Don’t worry so much about it."
            show sc vivinvitesmc d043
            mc"If you say so."
            show sc vivinvitesmc d047
            mc"Goodnight, [mc_v_address!c]."
            show sc vivinvitesmc d051
            mc"And thanks again for dinner."
            show sc vivinvitesmc d050
            mc"It was wonderful."
            show sc vivinvitesmc d050a
            v"You’re welcome, sweetheart."
            show sc vivinvitesmc d045
            v"Night..."
            stop music fadeout 1.0
            #Final shot of Vivian smiling as the MC exits her room
            #SCENE ENDS
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_02_01_Training_in_The_Park_with_Zora
        "Continue talking"(wt="Best option"):
            $ v_ep03_01_06_continue_talking_with_Vivian = True
            show sc vivinvitesmc d048
            v"Um... Do you think I could have a moment of your time?"
            show sc vivinvitesmc d049
            v"There’s something I’d like to show you."
            show sc vivinvitesmc d050
            mc"What is it?"
            #He looks at her suspiciously
            show sc vivinvitesmc d052
            v"That would spoil the surprise if I were to tell you."
            show sc vivinvitesmc d049
            v"It will only take a few minutes."
            show sc vivinvitesmc d054
            mc"Well..."
            #He deliberates
            show sc vivinvitesmc d045
            v"Please, honey."
            show sc vivinvitesmc d052a
            v"I would really like you to see it."
            show sc vivinvitesmc d055
            mc"Okay, sure."
            $ v_ep01_vivian_respect_counter += 1
            show sc vivinvitesmc d050a
            v"Great!"
            show sc vivinvitesmc d056
            v"Follow me."
            show sc vivinvitesmc d059
            with dissolve
            pause 1.5
            $ v_ep03_01_05_checking_on_Vivian_counter += 1
            #she turns around and the MC follows her into the main bedroom
            play sound "sound effects/01/door_close_soft.mp3" noloop
            show sc vivinvitesmc d060
            with dissolve
            pause 1.5
            #Vivian opens the door and allows the MC to enter first, and then she closes the bedroom door behind them
            #screen goes blank"
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_01_07_Evening_scene_in_Vivians_bedroom

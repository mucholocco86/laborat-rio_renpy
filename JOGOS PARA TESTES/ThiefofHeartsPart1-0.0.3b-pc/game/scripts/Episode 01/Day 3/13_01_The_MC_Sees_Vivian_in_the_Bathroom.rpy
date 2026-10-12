init:
    $ v_ep01_task08_art_gallery_with_vivian_counter = 0

    screen scr_ep01_13_01_Vivian_in_the_bathroom_Choices:
        default tt = Tooltip("Where will you hide?")
        zorder 10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc vivshower v20a"

        imagebutton:
            focus_mask True
            hovered tt.Action("Under the bed" + If(persistent.v_walkthrough_enabled == True,"{color=#33ff33} (Better option){/color}",""))
            idle "images/Episode 01/Day 03/13-Evening/13-01 Vivian Shower/sc vivshower v20a_bed_idle.png"
            hover "images/Episode 01/Day 03/13-Evening/13-01 Vivian Shower/sc vivshower v20a_bed_hover.png"
            action [Hide("scr_ep01_13_01_Vivian_in_the_bathroom_Choices"),Jump("lb_ep01_The_MC_sees_Vivian_in_the_bathroom1")]

        imagebutton:
            focus_mask True
            hovered tt.Action("In the closet" + If(persistent.v_walkthrough_enabled == True,"{color=#33ff33} (Funnier option){/color}",""))
            idle "images/Episode 01/Day 03/13-Evening/13-01 Vivian Shower/sc vivshower v20a_dresser_idle.png"
            hover "images/Episode 01/Day 03/13-Evening/13-01 Vivian Shower/sc vivshower v20a_dresser_hover.png"
            action [Hide("scr_ep01_13_01_Vivian_in_the_bathroom_Choices"),Jump("lb_ep01_The_MC_sees_Vivian_in_the_bathroom2")]

        frame:
            xfill True
            xalign 0.5
            yalign 0.0
            vbox:
                xalign 0.5
                yalign 0.5
                text tt.value

    image sc vivian shower massage1:
        "sc vivshower v88" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v88a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v88b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v88a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat


    image sc vivian shower massage2:
        "sc vivshower v83" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v83a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v83b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v83a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc vivian shower massage3:
        "sc vivshower v92" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v92a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v92b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v92a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc vivian shower massage4:
        "sc vivshower v85" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v85a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v85b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc vivshower v85a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat


label lb_ep01_The_MC_sees_Vivian_in_the_bathroom:
    #evening scene - the MC is at home
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    scene sc vivshower v01
    with dissolve
    mc"(All right, I have just under half an hour before Megan's car shows up.)"
    show sc vivshower v02
    mc"(This woman knows more about me than she's letting on.)"
    show sc vivshower v03
    mc"(But how?)"
    mc"(And what if I'm heading into some kind of trap?)"
    show sc vivshower v02
    mc"(Hmm... I should at least tell someone where I'm going, in case something goes wrong...)"

    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the MC stands outside Vivian's bedroom door
    show sc vivshower v04
    with dissolve
    mc"(She's the only person I can speak to who won't say anything to [mc_vic_address].)"
    mc"(So I better talk to her now while my [mc_a_b_rel]s are occupied.)"
    #The MC knocks on her door
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc vivshower v05
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    show sc vivshower v08
    with dissolve
    mc"Hello?"
    stop sound fadeout 1.0
    show sc vivshower v04
    mc"[mc_v_address]? Are you in there?"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc vivshower v05
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    show sc vivshower v07
    with dissolve
    mc"(It doesn't seem like it.)"
    stop sound fadeout 1.0
    show sc vivshower v08
    mc"(She has to be in there because she's not anywhere else.)"
    #the MC tries the door knob and lets himself in
    show sc vivshower v07
    mc"(I'm feeling a strange case of deja vu.)"
    show sc vivshower v08
    mc"(The only difference is, [mc_vic_address] isn't here or in the house.)"
    #shower sound effect
    $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
    play sound "sound effects/01/Door_Opening.mp3"
    play ambient "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
    show sc vivshower v06
    with dissolve
    mc"(Sounds like she's having a shower.)"
    #The MC notices that the door to the bathroom is open - and the light inside is on
    stop sound fadeout 1.0
    show sc vivshower v09
    mc"(Oh...)"
    mc"(The door isn't closed this time.)"

    #[Wait for her to finish / Take a quick look]
    menu:
        "Wait for her to finish":
            show sc vivshower v20
            mc"(No, I'm not going to do it.)"
            show sc vivshower v21
            mc"(I'll wait out here until she's finished...)"
            $ v_ep01_vivian_respect_counter += 1
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

    #GO DOWN TO > (scene continues)

        "Take a quick look"(wt="Best option"):
            mc"(I'm already here, and the door is open.)"
            #The MC approaches the door to the bathroom
            #show the MC looking in first before showing Vivian showering
            $ renpy.music.set_volume(1., 0.4, channel="ambient")
            #louder shower sound effect
            show sc vivshower v10
            with vpunch
            mc"(Oh good God...)"
            #SLOW ROLLING SCREEN FROM THE FLOOR UP, SHOWING VIVIAN SHOWERING
            #steam up the shower so Vivian's naked body is like a silhouette
            menu:
                "Get the hell out of there!":
                    show sc vivshower v13
                    mc"(I better go before she sees me!)"
                    stop sound fadeout 1.0
                "Risk being caught"(wt="Best option"):
                    show sc vivshower v13
                    mc"(I know I should turn around and leave, but I simply can't.)"
                    mc"(At least until some of the steam clears so I can get a better look.)"
                    $ v_ep01_vivian_cocky_counter += 1
                    #The steam cleans around her top half - show Vivian cupping her breasts, washing and covering them with her hands, but not unveiling them (possible animation here?)
                    show sc vivshower v15
                    mc"(Good lord...)"
                    mc"(Why can't I resist her?)"
                    show sc vivshower v14
                    mc"(Is it because [mc_vic_address] isn't here, and I know that I'll get away with it?)"
                    show sc vivshower v13
                    mc"(Yep, I definitely made the right choice.)"
                    #shower sound effect ends
                    stop ambient fadeout 1.0
                    play sound "sound effects/01/turn_shower_off.ogg"
                    show sc vivshower v16
                    mc"(Oh crap!! She turned the shower off!)"
                    show sc vivshower v10
                    mc"(I better get out of here!)"
                    stop sound fadeout 1.0
            show sc vivshower v49
            with dissolve
            v"(Mmm... I sure needed that.)"
            #Only show Vivian's face or from the neck up, to tease the player
            show sc vivshower v16
            v"(Where's my towel?)"
            #Vivian sees her towel on the bathroom sink bench
            show sc vivshower v17
            v"(Oh, there it is.)"
            #scene moves to the MC looking around in the bedroom
            show sc vivshower v20
            mc"(Shit, shit, shit!)"
            show sc vivshower v18
            mc"(If she finds me in here, she's going to know I was spying on her.)"
            show sc vivshower v21
            mc"(And she might hear me open the bedroom door if I try to leave.)"
            show sc vivshower v19
            mc"(I could hide under the bed, but it might be a little risky.)"
            #The MC looks at the base of the bed
            show sc vivshower v22
            mc"(There's also the closet.)"
            #The MC sees the closet
            show sc vivshower v20
            mc"(Fuck, what am I going to do??)"
            show sc vivshower v20a
            call screen scr_ep01_13_01_Vivian_in_the_bathroom_Choices with Dissolve(0.2) onlayer master

            #Under the bed / In the closet
            label lb_ep01_The_MC_sees_Vivian_in_the_bathroom1:
                scene black
                with dissolve
                show sc vivshower v112
                with dissolve
                mc"(I hope I can fit under here.)"
                #The MC hides under the bed
                #Vivian enters the bedroom in just a towel - hair still wet
                show sc vivshower v24
                v"Mmm..."
                #Vivian sits on the bed shows slight anguish - she clutches at her neck
                show sc vivshower v25
                v"(My neck is so sore.)"
                v"(I'd ask [vic_name] to rub it but he's not here right now.)"
                show sc vivshower v26
                v"(Not that he would, even if I asked him to.)"
                #Vivian looks dismayed
                show sc vivshower v111
                mc"(I may have to wait under here until she leaves the bedroom.)"
                #show the MC under the bed, he can see her feet
                show sc vivshower v113
                with dissolve
                mc"(I just have to remain perfectly still.)"
                #Vivian stands up in her towel and moves away from the bed so the MC can see her from under the bed
                show sc vivshower v114
                mc"(What is she...)"
                #show Vivian getting ready to undo her towel
                #next render, show Vivian's towel at her feet, facing the closet where the MC is
                show sc vivshower v28
                with vpunch
                mc"(Oh... my... God...)"
                #the MC looks stunned
                mc"(She's showing everything!)"
                $ rewards_unlock ("vivian",7)
                #show Vivian put her fingers through her hair, eyes closed, showing her breasts for the first time
                show sc vivshower v30
                with dissolve
                pause 1.0
                #show a gobsmacked MC
                #Vivian removes her hand from the top of her head - and realises her hair is still wet
                show sc vivshower v31
                with dissolve
                v"(Ah, geez... My hair is still soaking wet.)"
                show sc vivshower v30
                v"(I better go back into the bathroom and run the hairdryer over it.)"
                #A slight bump from under the bed - sound effect
                play sound "sound effects/01/cat_hiss.ogg"
                if persistent.v_sounds_text_on == True:
                    "Hisssssssss!"
                else:
                    pause 1.0
                show sc vivshower v32
                v"(What was that?)"
                stop sound fadeout 1.0
                show sc vivshower v115
                mc"(Huh?)"
                #MC looks around and sees the cat
                show sc vivshower v117
                if v_ep01_01_bella_room or v_ep01_01_ariel_room:
                    mc"(Seriously kitty! Do you have it out for me?)"
                else:
                    mc"(kitty? What the hell is she doing in here??)"
                show sc vivshower v32
                v"(I think it came from under the bed.)"
                #Vivian approaches the bed and the MC watches and panics
                show sc vivshower v116
                mc"(Oh shit... She's going to find me.)"
                #The MC cups his mouth while the cat sits next to him
                show sc vivshower v118
                mc"(I sure hope this works.)"
                #The MC grabs the cat and pushes it out from under the bed
                #note if possible - find an annoyed/angry cat meow sound effect
                play sound "sound effects/01/cat_meow_sound_effect.mp3"
                show sc vivshower v40
                if persistent.v_sounds_text_on == True:
                    "Meow!!"
                else:
                    pause 2.0
                #Vivian is about to look under the bed until the cat moves out from under it
                show sc vivshower v39
                v"Huh?"
                #Vivian stands back and is shocked to see the cat
                stop sound fadeout 1.0
                show sc vivshower v41
                v"Oh! Hey kitty, it's just you."
                v"I had no idea that you were even in here."
                show sc vivshower v113
                mc"(That little bastard... Neither did I!)"
                show sc vivshower v110
                v"Oh, you want out."
                #The cat stands by the bedroom door
                show sc vivshower v43
                v"Okay, I can help you with that."
                #Vivian goes over to the bedroom door
                show sc vivshower v115
                mc"(Finally that damm cat was useful for a change!)"
                show sc vivshower v113
                mc"(She certainly saved my bacon.)"
                show sc vivshower v44
                v"Out you go."
                #Vivian opens the door and lets the cat out
                #Vivian turns and thinks
                show sc vivshower v46
                v"(Now I can dry my hair.)"
                #show Vivian heading towards the bathroom door
                show sc vivshower v113
                mc"(She's going back into the bathroom.)"
                #sound effect - hair dryer from the bathroom
                mc"(Now's my chance to escape!)"
                #the MC moves out from under the bed while Vivian remains in the bathroom
                jump lb_ep01_The_MC_sees_Vivian_in_the_bathroom3

            label lb_ep01_The_MC_sees_Vivian_in_the_bathroom2:
                play sound "sound effects/01/closet_close.ogg"
                scene black
                with dissolve
                show sc vivshower v23
                with dissolve
                mc"(Oh geez... That was close.)"
                #Vivian enters the bedroom in just a towel - hair still wet
                show sc vivshower v24
                v"Mmm..."
                stop sound fadeout 1.0
                show sc vivshower v34
                mc"(I don't think she saw me.)"
                #Vivian sits on the bed shows slight anguish - she clutches at her neck
                show sc vivshower v25
                v"(My neck is so sore.)"
                v"(I'd ask [vic_name] to rub it but he's not here right now.)"
                show sc vivshower v26
                v"(Not that he would, even if I asked him to.)"
                #Vivian looks dismayed
                show sc vivshower v34
                mc"(I may have to wait in here until she leaves the bedroom.)"
                #show the MC inside the closet
                mc"(I just have to remain perfectly still.)"
                #Vivian stands up in her towel
                show sc vivshower v35
                mc"(Wait...)"
                show sc vivshower v27
                mc"(What is she...)"
                #show Vivian getting ready to undo her towel
                show sc vivshower v28
                pause 1.5
                #next render, show Vivian's towel at her feet, facing the closet where the MC is
                show sc vivshower v33
                with vpunch
                mc"(Oh... my... God...)"
                #the MC looks stunned
                show sc vivshower v29
                mc"(She's showing everything!)"
                #show Vivian put her fingers through her hair, eyes closed, showing her breasts for the first time
                show sc vivshower v30
                mc"(...)"
                #show a gobsmacked MC
                #Vivian removes her hand from the top of her head - and realises her hair is still wet
                show sc vivshower v31
                v"(Ah, geez... My hair is still soaking wet.)"
                show sc vivshower v30
                v"(I better go back into the bathroom and run the hairdryer over it.)"
                #A slight bump from the closet - sound effect
                play sound "sound effects/01/closet_creek.ogg"
                if persistent.v_sounds_text_on == True:
                    "(Creek.)"
                else:
                    pause 1.0
                show sc vivshower v32
                v"(What was that?)"
                stop sound fadeout 1.0
                show sc vivshower v35
                mc"(Huh?)"
                #MC looks down and sees his erection in his pants pressed up against the inside of the closet door
                show sc vivshower v36
                mc"(Oh goddamnit!)"
                show sc vivshower v37
                mc"(Not now!)"
                show sc vivshower v32
                v"(I think it came from the closet.)"
                #Vivian approaches the closet and the MC watches her
                show sc vivshower v38
                mc"(Oh shit... She's going to find me in here.)"
                #The MC cups his mouth
                show sc vivshower v29
                mc"(I need a miracle.)"
                #Vivian is about to open the closet door when the cat moves out from under the bed
                play sound "sound effects/01/cat_meow_sound_effect.mp3"
                show sc vivshower v38
                if persistent.v_sounds_text_on == True:
                    "Meow!!"
                else:
                    pause 2.0
                show sc vivshower v39
                v"Huh?"
                #Vivian takes her hand away from the closet door and sees the cat behind her, under the bed
                stop sound fadeout 1.0
                show sc vivshower v40
                v"Oh! Hey kitty, it's just you."
                show sc vivshower v41
                v"I had no idea that you were even in here."
                show sc vivshower v33
                mc"(Son of a bitch... Neither did I!)"
                show sc vivshower v110
                v"Oh, you want out."
                #The cat stands by the bedroom door
                show sc vivshower v45
                v"Okay, I can help you with that."
                #Vivian goes over to the bedroom door
                show sc vivshower v35
                mc"(Finally that damm cat was useful for a change!)"
                show sc vivshower v43
                mc"(She certainly saved my bacon.)"
                show sc vivshower v44
                v"Out you go."
                #Vivian opens the door and lets the cat out
                #Vivian turns and thinks
                show sc vivshower v46
                v"(Now I can dry my hair.)"

                #show Vivian heading towards the bathroom door
                show sc vivshower v35
                mc"(She's going back into the bathroom.)"
                #sound effect - hair dryer from the bathroom
                show sc vivshower v34
                mc"(Now's my chance to escape!)"
                #the MC exits the closet while Vivian remains in the bathroom

            label lb_ep01_The_MC_sees_Vivian_in_the_bathroom3:
                scene black
                with dissolve
                show sc vivshower v47
                with dissolve
                mc"(My talk with her will just have to wait until she's finished...)"
                #show the MC sitting on the bed
                #screen goes blank
                scene black
                with dissolve
                scene black
                with Pause (2)

    #GO DOWN TO > (scene continues)

    #scene continues

    #Vivian comes out of the bathroom wearing just a towel and with wet hair - https://m.media-amazon.com/images/M/MV5BODA5NDZlNWMtZjAxMS00ZTEyLTkyYWUtZDU5ODUyNmNjOTUwXkEyXkFqcGdeQXVyNzQ1NjgzOTA@._V1_.jpg
    #She sees the MC sitting on the bed and gets a fright
    centered "A few minutes later...{w=2.0}{nw}" with dissolve
    show text "A few minutes later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    show sc vivshower v51
    with dissolve
    with hpunch
    v"[y_name]!!"
    v"What are you doing in here??"
    show sc vivshower v52
    mc"I needed to speak to you. It's pretty important."
    mc"So I thought I'd wait until you were done drying your hair."
    mc"Plus your door was unlocked so I let myself in."
    show sc vivshower v101
    v"(Hmm... Did he see me showering?)"
    show sc vivshower v102
    v"(No, he's a good boy. Surely he wouldn't spy on me.)"
    show sc vivshower v53
    v"What did you want to talk about?"
    #Vivian looks for clothes as they talk
    show sc vivshower v52
    mc"I have to head out to see someone."
    v"Let me take a seat."
    play music "sound effects/01/Ease My Mind2.mp3" loop fadein 1.0
    show sc vivshower v54
    with dissolve
    v"So who is this person you're going to see?"
    show sc vivshower v60
    v"A girl, perhaps?"
    show sc vivshower v67
    mc"As much as I'd like to say that I am, no, I'm not seeing a girl."
    show sc vivshower v55
    mc"It's someone who apparently has found my bike."
    show sc vivshower v59
    v"Oh, that's great news, sweetheart!"
    show sc vivshower v62
    mc"So anyway, I'll be back soon but I thought I'd let you know in case you were wondering where I was."
    show sc vivshower v57
    v"Just make sure you return home before curfew."
    show sc vivshower v56
    v"You don't want to anger [vic_name] any more than you already have."
    show sc vivshower v55
    mc"Yeah, I know."
    mc"Don't worry, I'll be back in time."
    show sc vivshower v103
    mc"(I know I planned to tell her exactly where I was going and I would tell her about Megan...)"
    show sc vivshower v104
    mc"(But what she doesn't know can't worry her.)"
    show sc vivshower v105
    mc"(Besides, I'm old enough to take care of myself.)"
    #Show Vivian with a towel around her
    show sc vivshower v106
    mc"(Damn, I can't think straight when she's wearing just a towel and she's sitting so close.)"
    show sc vivshower v63
    mc"Did you speak to [vic_name] when he was home earlier?"
    show sc vivshower v67
    mc"Did you tell him about what we did today?"
    show sc vivshower v61
    v"I um... I didn't get a chance to."
    show sc vivshower v58
    v"He didn't seem all that interested in hearing what I had to say and just came in here to get a few things."
    show sc vivshower v56
    v"And then he left again. Maybe I'll tell him tomorrow."
    show sc vivshower v67
    mc"Yeah, you should."
    show sc vivshower v107
    v"Speaking of tomorrow, [vic_name] has asked me to check out the local art gallery in the morning."
    show sc vivshower v60
    v"He wants me to check out the setup, take note of the number of guards, placement of cameras and whatnot."
    show sc vivshower v59
    v"Would you maybe want to join me for that?"
    show sc vivshower v54
    v"I don't have to work at the restaurant until later in the afternoon so we could go in the morning when the gallery opens at ten."
    show sc vivshower v109
    mc"(Despite not everything going to plan at the theatre, it was fun spending time with her.)"
    show sc vivshower v68
    mc"Sure, count me in."
    $ task_addnew("Visit the Art Gallery with "+v_name+" ",8)

    #[Leave / Hang around]
    menu:
        "Leave":
            show sc vivshower v55
            mc"Anyway, I should probably head out so I'm back before curfew."
            show sc vivshower v69
            v"Sure, sweetheart."
            v"Let me walk you out."
            #The MC goes to leave
            #screen goes blank
            scene black
            with dissolve
            show sc vivshower v73
            with dissolve
            v"[y_name]? One more thing before you go."
            show sc vivshower v75
            mc"What is it [mc_v_address]?"
            show sc vivshower v72
            v"I just wanted to say thanks again for today."
            show sc vivshower v71
            v"It meant so much to have you there with me."
            show sc vivshower v70
            v"I enjoyed it."
            show sc vivshower v74
            mc"So did I."
            show sc vivshower v75
            mc"If we don't talk again when I get back, have a good night."
            show sc vivshower v71
            v"Yeah, you too."
            #Vivian smiles and the MC leaves
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_gets_his_bike_back

        "Hang around"(wt="Task Point"):
            show sc vivshower v57
            v"Was there anything else?"
            show sc vivshower v62
            mc"Uh, no, that was it."
            show sc vivshower v64
            mc"I guess I should get going then."
            #Vivian clutches at her shoulder and is in some discomfort
            show sc vivshower v76
            v"Mmm..."
            mc"Are you all right?"
            $ v_ep01_task08_art_gallery_with_vivian_counter += 1
            show sc vivshower v77
            v"Yeah, it's just my shoulder. It feels incredibly tense."
            show sc vivshower v99
            v"I thought taking a shower might help, but it's still sore."

            #Say nothing / Offer to help
            menu:
                "Say nothing":
                    show sc vivshower v77
                    v"Do you mind?"
                    show sc vivshower v64
                    mc"Do I mind what?"
                    show sc vivshower v60
                    v"Would you be able to rub some soothing lotion in there before you go?"
                    show sc vivshower v57
                    v"That is if you have a few minutes."
                    show sc vivshower v65
                    mc"Are you sure?"
                    $ v_ep01_vivian_respect_counter += 1
                    show sc vivshower v59
                    v"Yeah, of course."
                    show sc vivshower v60
                    v"I mean after all that working out that you do, I'd imagine you're pretty good with your hands, right?"
                    show sc vivshower v99
                    v"I'd do it myself but it's a little difficult to reach back there."
                    show sc vivshower v67
                    mc"Oh, okay. I should be able to help you with that."
                    show sc vivshower v69
                    mc"(The car will be here soon, so I better do this quickly.)"
                    show sc vivshower v80
                    v"Give me a moment while I go get some massage lotion that you can use on me..."
                    stop music fadeout 1.0
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                "Offer to help"(wt="Task Point"):
                    show sc vivshower v67
                    mc"Let me help you with that."
                    show sc vivshower v57
                    v"How do you mean?"
                    show sc vivshower v68
                    mc"I'll give you a quick rubdown. So you're nice and relaxed before this trip to the art gallery in the morning."
                    $ v_ep01_task08_art_gallery_with_vivian_counter += 1
                    show sc vivshower v61
                    v"Oh, that's nice of you to offer, but you don't have to do that, sweetheart."
                    show sc vivshower v100
                    mc"Nonsense! Besides, I guarantee that you'll notice the difference once my hands have given your shoulders a thorough treatment!"
                    show sc vivshower v57
                    v"Are you sure? Do you have time? You're going out soon, aren't you?"
                    show sc vivshower v79
                    mc"Yeah, we have time."
                    mc"Besides, you're more important. It can wait."
                    show sc vivshower v107
                    with dissolve
                    pause 2.0
                    #Vivian smiles
                    show sc vivshower v62
                    with dissolve
                    mc"Do you have any soothing oil that I could use?"
                    show sc vivshower v59
                    v"Yeah, of course."
                    show sc vivshower v80
                    v"Give me a moment while I go get some massage lotion that you can use on me..."
                    $ rewards_unlock ("vivian",8)
                    mc"(The car will be here soon, so I better do this quickly.)"
                    stop music fadeout 1.0
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                "A good idea":
                    show sc vivshower v67
                    mc"Maybe you could get [mc_vic_address] to give you a rubdown when he gets home?"
                    $ v_ep01_vivian_arrogant_counter += 1
                    show sc vivshower v61
                    v"Oh, yeah, I guess I could ask him."
                    show sc vivshower v56
                    v"(Though I would've preferred someone else do it.)"
                    show sc vivshower v55
                    mc"Anyway, I should probably head out so I'm back before curfew."
                    show sc vivshower v69
                    v"Sure, sweetheart."
                    v"Let me walk you out."
                    #The MC goes to leave
                    #screen goes blank
                    scene black
                    with dissolve
                    show sc vivshower v73
                    with dissolve
                    v"[y_name]? One more thing before you go."
                    show sc vivshower v75
                    mc"What is it [mc_v_address]?"
                    show sc vivshower v72
                    v"I just wanted to say thanks again for today."
                    show sc vivshower v71
                    v"It meant so much to have you there with me."
                    show sc vivshower v70
                    v"I enjoyed it."
                    show sc vivshower v74
                    mc"So did I."
                    show sc vivshower v75
                    mc"If we don't speak again when I get back, have a good night."
                    show sc vivshower v71
                    v"Yeah, you too."
                    stop music fadeout 1.0
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    jump lb_ep01_The_MC_gets_his_bike_back

            #show a close-up of Vivian's face to start with - https://pixhost.to/show/1027/447363733_screenshot-2024-02-20-at-1-12-09-am.jpg
            show sc vivshower v81
            with dissolve
            v"I found some."
            show sc vivshower v74
            mc"Great!"
            show sc vivshower v101
            mc"Uh... How should we do this?"
            show sc vivshower v53
            v"How about I lay down on the bed?"
            show sc vivshower v75
            mc"O-kay..."
            scene black
            with dissolve
            pause 1.0
            play music "sound effects/01/Touch_and_Tension.mp3" loop fadein 1.0
            show sc vivshower v83
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage2
            else:
                show sc vivshower v83
            v"Ohhh..."
            v"Yeah, that feels good."
            show sc vivshower v85
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage4
            else:
                show sc vivshower v85
            v"Can you feel how tight it is?"
            #show the MC's face
            show sc vivshower v86
            mc"Uh, yeah... I sure can..."
            show sc vivshower v87
            v"Oh wow..."
            #Show a front shot of her with the MC's hands on her shoulders
            show sc vivshower v87
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage2
            else:
                show sc vivshower v83
            v"I never realised just how good you were at this."
            show sc vivshower v86
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage4
            else:
                show sc vivshower v85
            mc"Are you feeling any tension?"
            v"Not as much as before. I feel nice and relaxed now."
            mc"(I bet you do.)"
            show sc vivshower v93
            mc"How about you turn over for me so I can do your front now?"
            show sc vivshower v84
            v"Oooh... I can't wait to see what else you have in store for me..."
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            show sc vivshower v89
            with dissolve
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage3
            else:
                show sc vivshower v92
            v"Mmm..."
            show sc vivshower v94
            mc"How's the pressure?"
            show sc vivshower v96
            v"Yeah, it's perfect."
            show sc vivshower v97
            with faster_dissolve
            v"Where did you learn to give massages like this?"
            show sc vivshower v94
            mc"Oh, you know... Online courses, picking up tips here and there."
            show sc vivshower v93
            mc"Plus you regularly learn all about the human anatomy from working in a gym."
            show sc vivshower v98
            v"Why do you think I have this tension in my neck and shoulders?"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage3
            else:
                show sc vivshower v92
            mc"It could be a variety of things..."
            mc"They could feel tight or stiff due to stress or overuse."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage1
            else:
                show sc vivshower v88
            mc"Or that soreness you're feeling may be caused by sitting for a long time or incorrect sleeping positions."
            v"Well, I have had some restless nights lately."
            show sc vivshower v91
            mc"(At a guess, I'd say it's due to the extra stress and anxiety that [mc_vic_address] causes her on a daily basis.)"
            show sc vivshower v95
            mc"(Not that I can tell her that.)"
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage3
            else:
                show sc vivshower v92
            mc"(He never seems to be around when she really needs him.)"
            mc"(Even though he should be here, I'm kind of glad he's not.)"
            show sc vivshower v89
            mc"(I like doing this for her, and I think she's enjoying it too.)"
            show sc vivshower v95
            v"Mmm..."
            show sc vivshower v97
            v"You're insanely good with your hands, [y_name]."
            show sc vivshower v93
            mc"Guilty as charged."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc vivian shower massage1
            else:
                show sc vivshower v88
            mc"(I really want to work on the rest of her body, but that car could be here any second now.)"
            mc"(Maybe next time.)"
            v"I never want this massage to end, but..."
            show sc vivshower v98
            with faster_dissolve
            v"I think that should do it for now."
            show sc vivshower v94
            mc"Um, sure. No problem..."
            stop music fadeout 1.0
            scene black
            with dissolve
            pause 1.0

            play music "sound effects/01/Ease My Mind1.mp3" loop fadein 1.0
            show sc vivshower v78
            with dissolve
            v"Wow! My shoulders feel a lot less tense now."
            v"Thank you."
            #Vivian turns around so she's unknowingly looking up at the MC between his legs
            show sc vivshower v68
            mc"You're welcome."
            show sc vivshower v69
            v"So um, I'm going to get changed now."
            show sc vivshower v62
            mc"Sure. I should probably get going."
            show sc vivshower v69
            v"Sure, sweetheart."
            v"Let me walk you out."
            scene black
            with dissolve
            show sc vivshower v73
            with dissolve
            v"[y_name]? One more thing before you go."
            show sc vivshower v75
            mc"Yes?"
            show sc vivshower v72
            v"Thanks again for today."
            show sc vivshower v71
            v"It meant so much to have you there with me."
            show sc vivshower v70
            v"I enjoyed it."
            show sc vivshower v75
            mc"Yeah, so did I."
            show sc vivshower v72
            v"I'll see you in the morning before our trip to the art gallery."
            show sc vivshower v74
            mc"Sounds good."
            show sc vivshower v71
            v"It's a date."
            #Vivian is surprised by what she just said
            show sc vivshower v73
            v"Um... You know what I mean."
            #Vivian looks away from the MC
            show sc vivshower v75
            mc"Right..."
            show sc vivshower v108
            mc"Anyway, if we don't talk by the time I get back, have a good night."
            show sc vivshower v70
            v"Yeah, you too."
            show sc vivshower v71
            v"And be safe."
            #Vivian smiles and the MC leaves
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_gets_his_bike_back

init:
    $ v_ep03_02_03_trying_on_clothes_with_Bella = 0

label lb_ep03_02_03_At_Bellas_clothing_store:
    #The scene begins with just Bella and the MC
    #The MC in the changing room again, getting changed into something similar to the suit he had on with Ariel
    #The difference is, he’s wearing a white jacket and a bow tie - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlP6-1R7zaJfwJyTPrjt7yxsW4AE3wPdEPqg&s
    play music "sound effects/03/changing_room.mp3" loop fadein 2.0
    scene sc ep3bellatask m001
    with dissolve
    pause 1.0
    #he looks at himself in the mirror
    show sc ep3bellatask m002
    with dissolve
    pause 1.0
    show sc ep3bellatask m003
    with dissolve
    pause 1.0
    show sc ep3bellatask m005
    with dissolve
    mc"Okay, I’m ready [b_name]."
    #he calls out to her from inside the dressing room
    pause 2.0
    mc"Are you out there?"
    show sc ep3bellatask m006
    with dissolve
    pause 1.0
    #the MC looks confused as he exits the changing room
    show sc ep3bellatask m007
    with dissolve
    pause 1.0
    #then he walks around the store and notices the “Back in 15 minutes“ sign
    #He continues to look around
    show sc ep3bellatask m009
    with dissolve
    mc"[b_name]?"
    show sc ep3bellatask m008
    with dissolve
    b"I’m just out the back. Give me a few minutes."
    #The MC looks intrigued
    #[See what she’s doing / Wait for her]
    menu:
        "See what she’s doing"(wt="Best option"):
            #the MC walks around the counter and to the back room
            show sc ep3bellatask m020
            with dissolve
            pause 1.5
            show sc ep3bellatask m012
            with dissolve
            pause 1.5
            #the MC sees Bella out there, still dressed
            show sc ep3bellatask m013
            with dissolve
            pause 1.5
            $ v_ep03_02_03_trying_on_clothes_with_Bella +=1
            #He’s about to say something but stops as she starts to take her work dress off

            #the MC’s mouth opens as he sees Bella strip down to her bra and panties
            #[Go and wait for her / Keep watching]
            menu:
                "Go and wait for her"(wt="Bonus Image"):
                    show sc ep3bellatask m013
                    with dissolve
                    #screen goes blank
                    $ rewards_unlock ("bella",17)
                    $ v_ep01_bella_respect_counter += 1
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #Go Down to > scene continues
                    jump lb_ep03_02_03_Bella_returns_from_the_back_room

                "Keep watching"(wt="Best option"):
                    show sc ep3bellatask m015
                    with dissolve
                    pause 1.5
                    show sc ep3bellatask m016
                    with dissolve
                    pause 1.5
                    #Bella turns her back to him so we see her ass in thong panties
                    show sc ep3bellatask m017
                    with dissolve
                    pause 1.5
                    $ v_ep01_bella_cocky_counter += 1
                    #she undoes her bra but we don’t see her breasts as she is still facing away from the MC
                    #the MC continues to look shocked
                    show sc ep3bellatask m018
                    with dissolve
                    pause 1.5
                    $ v_ep03_02_03_trying_on_clothes_with_Bella +=1
                    #Bella bends forward to pick up a dress from the floor, so we can see her ass bent over

                    #[Go and wait for her / Don’t move]
                    menu:
                        "Go and wait for her":
                            show sc ep3bellatask m013
                            with dissolve
                            pause 1.0
                            $ v_ep01_bella_respect_counter += 1
                            #screen goes blank
                            stop music fadeout 1.0
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            #Go Down to > scene continues
                            jump lb_ep03_02_03_Bella_returns_from_the_back_room

                        "Don’t move"(wt="Best option"):
                            pause 1.0
                            show sc ep3bellatask m018a
                            with dissolve
                            pause 1.5
                            #Bella turns around and faces the MC, showing her naked breasts to the MC
                            $ v_ep01_bella_arrogant_counter += 1
                            #she doesn’t notice him watching her
                            show sc ep3bellatask m014
                            with dissolve
                            pause 1.5
                            #the MC continues to look shocked
                            show sc ep3bellatask m019
                            with dissolve
                            pause 1.5
                            #the MC grabs his crotch
                            $ v_ep03_02_03_trying_on_clothes_with_Bella +=1
                            stop music fadeout 1.0
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            #the MC leaves
                            jump lb_ep03_02_03_Bella_returns_from_the_back_room

        "Wait for her"(wt="Bonus Image"):
            show sc ep3bellatask m023
            with dissolve
            pause 1.0
            $ rewards_unlock ("bella",16)
            $ v_ep01_bella_respect_counter += 1
            stop music fadeout 2.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_02_03_Bella_returns_from_the_back_room

label lb_ep03_02_03_Bella_returns_from_the_back_room:
    # scene continues
    #scene returns with the MC waiting patiently out near the front counter
    play music "sound effects/02/Sibling_Blues.mp3" loop fadein 1.0
    show sc ep3bellatask m021
    with dissolve
    b"Okay, I’m on my way out now, [y_name]."
    #She calls out from the back room
    show sc ep3bellatask m022
    mc"What were you doing out there anyway?"
    show sc ep3bellatask m023
    b"You’re about to see."
    #Bella appears, all dressed up
    show sc ep3bellatask m025
    mc"Oh..."
    #POSSIBLE ANIMATION - BELLA WALKING AROUND TOWARDS THE MC FROM THE BACK ROOM
    show sc ep3bellatask m106
    with dissolve
    pause 1.0
    show sc ep3bellatask m107
    with dissolve
    pause 1.0
    show sc ep3bellatask m108
    with dissolve
    pause 1.0
    show sc ep3bellatask m109
    with dissolve
    pause 1.0
    show sc ep3bellatask m112
    with dissolve
    pause 1.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc ep3bellatask m111 at tt_top
        with dissolve
        pause 6.0
    elif True:
        scene sc ep3bellatask m113
        with dissolve
        pause 2.0
    scene sc ep3bellatask m110
    with dissolve
    b"So, what do you think?"

    #[Perfect / Overdressed / Other]
    menu:
        "Incredible"(wt="Best option"):
            show sc ep3bellatask m027
            mc"I hate to say it, but you look incredible, [b_name]."
            $ v_ep01_bella_respect_counter += 1
            show sc ep3bellatask m028
            b"I know."
            show sc ep3bellatask m029
            b"And thanks."
            $ v_ep03_02_03_trying_on_clothes_with_Bella +=1
        "Overdressed"(wt="Bonus Image"):
            show sc ep3bellatask m030
            mc"You’re a little overdressed for work, don’t you think?"
            $ rewards_unlock ("bella",18)
            show sc ep3bellatask m031
            b"It’s not for work, dummy."
            $ v_ep01_bella_arrogant_counter += 1

        "Other":
            show sc ep3bellatask m035
            mc"Um... I’m not sure."
            #Bella looks bemused
    show sc ep3bellatask m036
    mc"So what are we all dressed up for?"
    show sc ep3bellatask m032
    b"It’s for the afternoon function at the art gallery."
    show sc ep3bellatask m034
    b"[mc_vic_address!c] wants us to be there as two of the invited guests."
    show sc ep3bellatask m033
    b"So we both need to be dressed up for the occasion."
    show sc ep3bellatask m038
    mc"And to also help [mc_v_address!c] in case something goes wrong, yeah?"
    show sc ep3bellatask m037
    b"That’s part of the plan. [mc_vic_address!c] will explain our part in more detail soon."
    #Bella looks the MC over
    show sc ep3bellatask m114
    with dissolve
    b"It looks like I got your sizing right."
    #the MC and Bella are dressed similarly to this - https://i.pinimg.com/originals/40/68/d0/4068d070df9acf425a40bbb565757222.jpg
    show sc ep3bellatask m115
    with dissolve
    b"Yes, this worked out better than I thought it would."
    show sc ep3bellatask m116
    with dissolve
    pause 1.0
    #though the MC has a white suit on instead - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlP6-1R7zaJfwJyTPrjt7yxsW4AE3wPdEPqg&s
    #[Suggest something / Suggest nothing]
    menu:
        "Suggest something"(wt="Bonus Image"):
            show sc ep3bellatask m035
            mc"Hey, why don’t we take some photos together so we can show [mc_vic_address]?"
            show sc ep3bellatask m036
            mc"That way, he can confirm that what we’re wearing will be appropriate for this function."
            show sc ep3bellatask m037
            b"That’s just what I was going to recommend."
            $ rewards_unlock ("bella",19)
            show sc ep3bellatask m038
            mc"Great minds and all that, right?"
            show sc ep3bellatask m029
            b"Yeah, I suppose so."
            $ v_ep01_bella_respect_counter += 1


        "Suggest nothing":
            show sc ep3bellatask m040
            b"So as you know, I’ve closed the store."
            show sc ep3bellatask m034
            b"We have around five minutes before I need to open up again."
            show sc ep3bellatask m032
            b"So I think we should take some photos together so we can show [mc_vic_address] to see if what we’re wearing will be appropriate for this function."
            show sc ep3bellatask m036
            mc"That’s a good idea."
    #scene continues
    show sc ep3bellatask m034
    b"Okay, give me a moment to set up my phone camera so we can have these shots together."
    #show Bella setting it up on the counter
    show sc ep3bellatask m041
    with dissolve
    pause 2.0
    #show Bella standing next to the MC, readying themselves for the photo to be taken
    show sc ep3bellatask m042
    with dissolve
    b"All right, the camera will take a picture in about ten seconds."
    #She rushes to stand next to the MC and poses
    b"Get ready."

    #[Stand still / Put your arm around her]
    menu:
        "Stand still"(wt="Bonus Image"):
            show sc ep3bellatask m056
            with dissolve
            pause 2.0
            play sound "sound effects/01/camera_phone_photo.mp3"
            show sc ep3bellatask m056
            with flash(0.25, 0, 0.75, "#fff")
            pause 1.0
            #Bella places her hand on the MC’s shoulder and poses
            #ADD a FLASH
            #The phone takes a photo - camera flash sound effect
            show sc ep3bellatask m057
            with dissolve
            b"Sweet."
            $ rewards_unlock ("bella",20)
            $ v_ep01_bella_respect_counter += 1
            #Bella is happy and then checks her phone
            show sc ep3bellatask m058
            with dissolve
            mc"How did the photo turn out?"

        "Put your arm around her"(wt="Best option"):
            #The MC puts his arm around her
            show sc ep3bellatask m043
            with dissolve
            pause 1.0
            play sound "sound effects/01/camera_phone_photo.mp3"
            show sc ep3bellatask m043
            with flash(0.25, 0, 0.75, "#fff")
            pause 1.0
            #The phone takes a photo - camera flash sound effect
            #ADD a FLASH
            #Bella gives an awkward look while the MC has a cheeky grin
            show sc ep3bellatask m044
            with dissolve
            b"Hey!"
            show sc ep3bellatask m045
            b"Why did you put your arm around me?"
            show sc ep3bellatask m048
            mc"Well, I wanted the picture to look more natural."
            show sc ep3bellatask m046
            mc"Besides, if we’re going to this function together, people are going to assume we’re a couple, right?"
            show sc ep3bellatask m055
            mc"So I figure we could at least start acting like it."
            show sc ep3bellatask m052
            b"Hmm..."
            b"(I hate it when he’s right.)"
            show sc ep3bellatask m053
            b"Fine, but don’t think I’m gonna hold your hand all night."
            show sc ep3bellatask m055
            mc"No, of course not."
            $ v_ep01_bella_cocky_counter += 1
            show sc ep3bellatask m058
            with dissolve
            mc"Anyway, how did the photo turn out?"
            $ v_ep03_02_03_trying_on_clothes_with_Bella +=1


    #She looks over the photo on her phone
    show sc ep3bellatask m059
    b"Perfect."
    show sc ep3bellatask m060
    b"All right, that should just about do it."
    show sc ep3bellatask m061
    mc"Can I change now?"
    show sc ep3bellatask m062
    b"Sure, go for it."
    #the MC goes to leave but Bella stops him
    show sc ep3bellatask m063
    with dissolve
    b"And one more thing, [y_name]..."
    stop music fadeout 2.0
    play music2 "sound effects/01/Temptation2.mp3" loop fadein 1.0
    show sc ep3bellatask m065
    with dissolve
    b"When we go to this function together, just remember that I’m in charge."
    show sc ep3bellatask m078
    b"And don’t even think about chatting to any other girls while we’re there."
    show sc ep3bellatask m066
    mc"Oh, really [b_name]?"
    show sc ep3bellatask m067
    mc"What do you take me for?"
    show sc ep3bellatask m068
    b"All I’m saying is that make sure to keep your eyes on the prize."
    show sc ep3bellatask m069
    mc"I will."
    show sc ep3bellatask m070
    mc"But why are you in charge?"
    show sc ep3bellatask m071
    mc"Did [mc_vic_address] confirm this?"
    show sc ep3bellatask m072
    b"No, but it’s pretty obvious that he’ll ask me to be the one running things once we’re inside."
    show sc ep3bellatask m073
    mc"Yeah, we’ll see."
    show sc ep3bellatask m074
    b"What’s that supposed to mean?"
    show sc ep3bellatask m075
    mc"Come on, [b_name]."
    show sc ep3bellatask m076
    mc"You can drop the tough act."
    show sc ep3bellatask m077
    mc"We both know that [mc_vic_address] will put me in charge."
    show sc ep3bellatask m078
    b"There’s no way that will happen, I guarantee it."
    if v_ep03_02_03_trying_on_clothes_with_Bella >= 4:
        $ bella_love_level +=1


    #Add these lines and this scene if the player has less than TWO BELLA HEARTS
    if bella_love_level <= 1:
        #they both stare at each other, hands on hips, like angry siblings
        stop music2 fadeout 1.0
        show sc ep3bellatask m079
        with dissolve
        woman"Ahem!" with hpunch
        #A random upset woman who is still in the store interrupts

    #Add these lines and this scene if the player has TWO BELLA HEARTS
    if bella_love_level >= 2:
        stop music2 fadeout 3.0
        play music "sound effects/01/Blues_Fight.mp3" loop fadein 3.0
        show sc ep3bellatask m081
        mc"You’re still pissed off about the other night, aren’t you?"
        show sc ep3bellatask m082
        b"I don’t know what you’re talking about."
        #she looks away from him
        show sc ep3bellatask m083
        mc"Come on, admit it, [b_name]. You liked me kissing you."
        show sc ep3bellatask m085
        mc"I don’t know whether it’s because you’ve been deprived of any kind of intimacy from a guy, or if it’s something else, but deep down, you know you enjoyed it."
        show sc ep3bellatask m086
        b"No, it’s not true."
        ##Bella doesn’t look the MC in the face
        show sc ep3bellatask m081
        mc"And just now you said you don’t want me to talk to any other girls at the party."
        show sc ep3bellatask m085
        mc"Why?"
        show sc ep3bellatask m088
        b"I um, no reason..."
        #Bella continues to not look the MC in the face
        show sc ep3bellatask m119
        mc"Look me in the eye and tell me you didn’t enjoy it."
        #she looks up at him
        show sc ep3bellatask m090
        with dissolve
        pause 2.0
        show sc ep3bellatask m091
        b"Fine, I..."
        show sc ep3bellatask m092
        with dissolve
        pause 1.0
        #she looks at the MC with a defiant look and hesitates
        show sc ep3bellatask m120
        with dissolve
        pause 1.0
        #show the MC and Bella staring at each other here
        #in slow motion, the MC leans forward and kisses her closed mouth
        play sound "sound effects/01/kiss_and_moan_sound_effect02.mp3" loop fadein 2.0
        show sc ep3bellatask m121
        with dissolve
        pause 1.0
        b"Mmm..."
        show sc ep3bellatask m094
        with dissolve
        pause 1.5
        #a close-up of them kissing
        show sc ep3bellatask m122
        with dissolve
        pause 1.0
        show sc ep3bellatask m095
        with dissolve
        pause 1.5
        #expand the shot so we see them standing in their attire and kissing
        show sc ep3bellatask m123
        with dissolve
        pause 1.0
        show sc ep3bellatask m096
        with dissolve
        pause 1.5
        b"(Oh God... Why is he so damn good at this?)"
        #they continue to kiss and the MC pulls her in close to him
        show sc ep3bellatask m097
        with dissolve
        pause 1.5
        stop music fadeout 1.0
        #Her breasts press against his chest
        stop sound fadeout 1.0
        show sc ep3bellatask m098
        woman"Ahem!" with hpunch
        #A random upset woman is still in the store
    #scene continues
    show sc ep3bellatask m099
    woman"Excuse me?"
    play music "sound effects/01/School Hallways1.mp3" loop fadein 1.0
    woman"If you two don’t mind, I’d like to buy something."
    show sc ep3bellatask m124
    woman"It’s the least you can do after locking me in the store for the past fifteen minutes!"
    #the woman has her hands on her hips
    show sc ep3bellatask m101
    b"(Oh my God!! I had no idea she was still in here!)"
    show sc ep3bellatask m102
    mc"Well, I don’t work here. But she does."
    #The MC points to Bella
    show sc ep3bellatask m117
    mc"I’ll be getting changed now, miss."
    show sc ep3bellatask m118
    with dissolve
    pause 1.0
    #the MC cheekily addresses Bella like he doesn’t know her
    if bella_love_level >= 2:
        show sc ep3bellatask m103
        with dissolve
        b"(Damn him... He got me again!!)"
    #Bella looks at the MC angrily as he walks away
    show sc ep3bellatask m104
    woman"Miss?"
    show sc ep3bellatask m105
    woman"Miss??"
    #Bella remains angry while the customer stands behind Bella, looking angrily at her, her mouth open and Bella’s closed.
    #(screen goes blank)"
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_02_04_The_MC_talks_with_Victor_at_the_house


label lb_ep03_04_04_The_Art_Gallery_Heist_Part_3:
    #SCENE BEGINS

    #Bella communicates with Victor who is in the truck with Ariel - still standing next to her
    #she’s currently on foot, staying out of plain sight, hiding from security and police
    play music "sound effects/01/Griphop.mp3" loop fadein 2.0
    scene sc ep3heistpart3 j001
    with dissolve
    b"[mc_vic_address]?"
    show sc ep3heistpart3 j002
    b"Are you here?"
    #Bella looks in the ruck and finds Ariel
    show sc ep3heistpart3 j003
    a"He’s gone."
    show sc ep3heistpart3 j004
    a"He went into the gallery looking for you and [y_name]."
    show sc ep3heistpart3 j005
    a"Where is he?"
    show sc ep3heistpart3 j006
    b"[y_name] is still inside."
    show sc ep3heistpart3 j007
    b"Are you able to contact either of them?"
    show sc ep3heistpart3 j008
    a"I lost contact with [y_name] about ten minutes ago, and [mc_vic_address] is not responding."
    #Ariel sits down in front of her computer screen
    show sc ep3heistpart3 j009
    a"What should we do? Did [y_name] say anything to you?"
    show sc ep3heistpart3 j010
    b"[y_name] told me that if he’s not here in five minutes, then we should leave."
    show sc ep3heistpart3 j013
    a"Do you think we should?"
    show sc ep3heistpart3 j011
    b"If we don’t want to get caught, then it’s probably a smart idea."
    show sc ep3heistpart3 j012
    b"I’m sure [mc_vic_address] would have planned for this, and will get [y_name] out of there safely."
    show sc ep3heistpart3 j010
    b"If they’re not back in time, then we’ll meet up with [mc_v_address]."
    show sc ep3heistpart3 j011
    b"She’s parked three streets over in the getaway car."
    show sc ep3heistpart3 j013
    a"Okay, we’ll wait a few minutes to see if they return..."
    #the final shot here is Bella and Ariel waiting in the truck, they both look concerned
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The scene returns with the MC still in the basement
    #the alarm continues to siren
    show sc ep3heistpart3 j014
    mc"[mc_vic_address]?"
    show sc ep3heistpart3 j015
    mc"[mc_vic_address], do you copy?"
    show sc ep3heistpart3 j016
    mc"[a_name]? [b_name]?"
    show sc ep3heistpart3 j017
    mc"..."
    play music "sound effects/02/Mission Unseen.mp3" loop fadein 1.0
    mc"(Shit, I’ve lost the signal again.)"
    #he looks at his phone
    show sc ep3heistpart3 j018
    with dissolve
    pause 1.5
    #the MC locates another way out of there. He walks up some wooden stairs.
    show sc ep3heistpart3 j019
    with dissolve
    mc"(There has to be another way out of here...)"
    #https://remodelagain.com/wp-content/uploads/2024/02/20230720_145642469_iOS-scaled.jpg
    show sc ep3heistpart3 j020
    with dissolve
    pause 1.5
    #he opens the door at the top of the stairs, and it takes him out to this part of the gallery
    show sc ep3heistpart3 j021
    with dissolve
    pause 1.5
    #here - https://pixhost.to/show/461/524525616_sc-artgallery-a016.jpg
    show sc ep3heistpart3 j022
    with dissolve
    pause 1.5
    #make sure this entire room is darkened, as it’s well after closing time.
    show sc ep3heistpart3 j024
    with dissolve
    pause 1.5
    #the MC carefully walks alongside the walls
    show sc ep3heistpart3 j025
    with dissolve
    pause 1.5
    #he sees a security camera and makes sure to stay out of its line of sight
    show sc ep3heistpart3 j023
    with dissolve
    pause 1.5
    #See this video to get an idea: https://www.youtube.com/watch?v=B0KpMLGC70Q&ab_channel=maestropaolo
    show sc ep3heistpart3 j027
    with dissolve
    pause 1.5
    show sc ep3heistpart3 j026
    with dissolve
    pause 1.5
    #https://pixhost.to/show/461/524528725_screenshot-2024-10-22-at-12-48-28-pm.jpg
    stop music fadeout 1.0
    play sound "sound effects/03/glass_breaking_sound_effect.mp3" noloop
    if persistent.v_sounds_text_on == True:
        with vpunch
        "(SMASH!!)"
    else:
        scene sc ep3heistpart3 j029
        with dissolve
        pause 1.0
    scene sc ep3heistpart3 j029
    mc"(Oh shit!)"
    #when the camera is pointing the other way, the MC keeps moving through the gallery
    show sc ep3heistpart3 j030
    with dissolve
    mc"(Where did that sound come from?)"
    #The MC hears the sound of broken glass
    #sound effect of broken glass
    #he looks concerned and then carefully moves forward
    #as he gets closer towards the front of the gallery, Victor appears
    show sc ep3heistpart3 j032
    with dissolve
    mc"[mc_vic_address]??"
    show sc ep3heistpart3 j035
    with dissolve
    vic"[y_name]!"
    #Victor arrives and he’s out the front of the gallery, near the front entrance
    show sc ep3heistpart3 j033
    mc"What are you doing here?"
    show sc ep3heistpart3 j034
    vic"I’m saving you and [b_name]’s ass, that’s what!"
    show sc ep3heistpart3 j035
    vic"Where’s the painting?"
    show sc ep3heistpart3 j036
    mc"We had to leave it."
    show sc ep3heistpart3 j037
    vic"FUCK!!"
    show sc ep3heistpart3 j034
    vic"What about [b_name]? Is she okay?"
    show sc ep3heistpart3 j038
    mc"I helped her to get out. She’s safe."
    show sc ep3heistpart3 j039
    mc"She should be back at the truck by now."
    show sc ep3heistpart3 j040
    vic"Hmm... So it’s just you in here, right?"
    show sc ep3heistpart3 j036
    mc"Yeah, that's right."
    show sc ep3heistpart3 j041
    vic"..."
    #Victor is deep in thought, like he’s concocting a devilish, sinister plan
    show sc ep3heistpart3 j042
    with dissolve
    pause 1.3
    show sc ep3heistpart3 j043
    mc"[mc_vic_address]?"
    pause 1.5
    show sc ep3heistpart3 j083
    mc"Hey, [mc_vic_address]!?"
    show sc ep3heistpart3 j044
    vic"Huh?"
    show sc ep3heistpart3 j045
    mc"We need to get out of here, the police could arrive any second now!"
    show sc ep3heistpart3 j046
    vic"Okay, follow me."
    #The MC follows Victor
    play music "sound effects/02/Heist of the Night.mp3" loop fadein 1.0
    show sc ep3heistpart3 j047
    with dissolve
    pause 2.0
    #The MC sees the smashed window entrance Victor made for himself
    show sc ep3heistpart3 j048
    with dissolve
    pause 2.0
    #the MC looks optimistic
    show sc ep3heistpart3 j049
    with dissolve
    pause 2.0
    #Victor stops
    show sc ep3heistpart3 j061
    pause 2.0
    show sc ep3heistpart3 j050
    mc"Why are you stopping?"
    show sc ep3heistpart3 j051
    vic"That’s far enough, [y_name]."
    #Victor turns to face the MC
    show sc ep3heistpart3 j052
    mc"Huh? What’s going on?"
    #Victor pulls a gun out of his pocket

    #show a close-up of Victor reaching for the back of his trousers, reaching for his gun
    show sc ep3heistpart3 j084
    with dissolve
    pause 1.3
    show sc ep3heistpart3 j085
    with dissolve
    pause 1.3
    show sc ep3heistpart3 j057
    with dissolve
    vic"Back away, kid."
    show sc ep3heistpart3 j059
    vic"Only one of us is getting out of here, and it’s not going to be you."
    show sc ep3heistpart3 j055
    mc"You son of a bitch!"
    mc"You're going to just leave me here. But why?"
    #The MC realises what Victor is doing - trapping him inside the gallery
    show sc ep3heistpart3 j053
    vic"Because this has been a long time coming, [y_name]."
    show sc ep3heistpart3 j054
    vic"And it’s your punishment for fucking up this heist among other things."
    play sound "sound effects/03/hand_gun_cocking_effect.mp3" noloop
    if persistent.v_sounds_text_on == True:
        scene sc ep3heistpart3 j058
        "(Gun clicks)"
    else:
        scene sc ep3heistpart3 j058
        pause 2.0
    #Victor clicks the gun - sound effect - he prepares to shoot
    show sc ep3heistpart3 j055
    mc"You'll pay for this, [mc_vic_address]!"
    show sc ep3heistpart3 j059
    vic"Uh-uh... That's far enough, [y_name]."
    show sc ep3heistpart3 j060
    vic"You’re a loose end, kid."
    vic"And loose ends need to be taken care of."
    show sc ep3heistpart3 j062
    vic"Or in your case, they need to take the fall."
    #Victor raises his gun, readying himself to shoot
    show sc ep3heistpart3 j063
    vic"I may not have that painting, but at least you won't be able to tell [v_name] anything about my late-night outings."
    show sc ep3heistpart3 j064
    mc"And what's stopping me from ratting you out?"
    show sc ep3heistpart3 j065
    vic"You could try."
    show sc ep3heistpart3 j059
    vic"But if you were to do that, you'd also be putting [v_name], [b_name] and [a_name] behind bars."
    show sc ep3heistpart3 j054
    vic"And I'm sure you won't, knowing how much you care about them and their well-being."
    show sc ep3heistpart3 j053
    vic"Plus they would hate you forever for it."
    show sc ep3heistpart3 j056
    #The MC looks downhearted
    vic"Anyway, enough talk."
    show sc ep3heistpart3 j059
    vic"Don’t try and follow me, otherwise..."
    #Vic steps back towards the broken window, but still facing the MC
    show sc ep3heistpart3 j060
    vic"Lead poisoning."
    #Show the barrel/end of the gun
    show sc ep3heistpart3 j064
    mc"You won’t get away with this!"
    #MC snaps back, angry at Victor
    show sc ep3heistpart3 j065
    vic"Oh, but I will."
    #Victor responds confidently

    #Victor gives the MC a cocky smirk, and then before he turns to leave

    #THERE’S A HUGE FLASH OF LIGHT THAT SHINES INTO THE GALLERY AS THE POLICE ARRIVE
    stop music fadeout 1.0
    #the Police sirens sound close - sound effect
    play sound "sound effects/03/police_siren_short_effect.mp3" noloop
    pause 2.0
    play sound "sound effects/03/police_speaker01.mp3" noloop
    show sc ep3heistpart3 j067
    police"THIS IS THE POLICE!"
    pause 1.0
    play sound "sound effects/03/police_speaker02.mp3" noloop
    show sc ep3heistpart3 j068
    police"PUT THE WEAPON DOWN, TURN AROUND SLOWLY, WITH YOUR HANDS UP!"
    #Victor lowers the gun
    pause 1.0
    #IMPORTANT: the MC isn’t seen by the police, only Victor. Victor is blocking the policeman's view of the MC, so they only think that VICTOR is at the scene of a possible crime
    play music "sound effects/03/the_police_arrive.mp3" loop fadein 1.0
    #The MC looks genuinely worried here, that Victor has been caught
    #Victor doesn’t turn around - he faces the MC with a stern look on his face through the window of the front of the gallery
    show sc ep3heistpart3 j069
    vic"(...)"
    #Victor looks angry
    play sound "sound effects/03/police_speaker03.mp3" noloop
    show sc ep3heistpart3 j067
    police"TURN AROUND, NOW!"
    pause 1.5
    #Victor has his hands up and looks at the MC
    show sc ep3heistpart3 j070
    vic"I guess I’ll be seeing you in the slammer, kid."
    show sc ep3heistpart3 j071
    mc"(Not if I can help it...)"
    #the MC looks somewhat confident, but unsure. He turns and runs through the gallery while avoiding the security cameras.
    show sc ep3heistpart3 j072
    with dissolve
    pause 1.3
    show sc ep3heistpart3 j073
    with dissolve
    pause 1.3
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #scene returns with the MC walking through the art gallery back dock/storage area
    #The storage area has plenty of wooden crates that are ready to be opened or shipped
    #show him calmly walking through the back dock area
    #https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKTtjfXxL9674xACCwC78pmPVlsZ5lQDrCFA&s
    show sc ep3heistpart3 j074
    with dissolve
    mc"(This looks like it could be a way out of here.)"
    $ image_sequence("sc ep3heistpart3", ["j075", "j076", "j077"], 1.7)
    with dissolve

    # show sc ep3heistpart3 j076
    # with dissolve
    # pause 1.5
    # #the MC sees a roller door that leads out of the gallery - https://integritydoors.com.au/wp-content/uploads/2013/12/Integrity-Doors-and-Engineering-Adelaide-Industrial-Commercial-Roller-Doors-Door-Shutters-Loading-Dock-Doors-Adelaide-24-hour-Roller-Door-Repairs-Adelaide-50.png
    # show sc ep3heistpart3 j077
    # with dissolve
    # pause 1.5
    #he stands by the roller door, and then lifts it up -
    #https://i0.wp.com/www.thompsonsroller.com.au/wp-content/uploads/2011/08/Loading-Docks-1.jpg?fit=900%2C600&ssl=1
    play sound "sound effects/03/rolling_door_sound_effect.mp3" noloop
    show sc ep3heistpart3 j078
    with dissolve
    pause 0.5
    #https://image.made-in-china.com/2f0j00cYTqSUHKsWzu/Industrial-Auto-Roller-Door-with-Dock-Leveler.jpg
    show sc ep3heistpart3 j079
    with dissolve
    pause 1.5
    #https://pixhost.to/show/461/524530686_screenshot-2024-10-22-at-11-47-48-am.jpg

    #show the MC’s look of glee as the roller door starts to open

    #he pushes the roller door up to the top - LOUDER
    show sc ep3heistpart3 j080
    with dissolve
    police"FREEZE!"
    mc"(Oh, crap.)"
    #his look of glee turns into one of horror as he is caught by the police
    police"Keep your hands up where I can see them!"
    #we don’t see their face
    #the MC puts his hands up
    play music "sound effects/01/Episode1_final_scene.mp3" fadein 2.5
    show sc ep3heistpart3 j081
    with dissolve
    pause 3.0
    show sc ep3heistpart3 j082
    with dissolve
    pause 3.0
    with slow_dissolve
    stop music fadeout 10.0
    scene black
    with Pause (10)
    with slow_dissolve
    jump lb_chapter_end_03


    jump start_pick_menu
    #The final shot we see from the officer’s POV. We see the MC in full, caught before he can escape with his hands up

label lb_review_end_03:
    $ count_points("ariel")
    $ count_points("bella")
    $ count_points("vivian")
    $ count_points("megan")
    $ count_points("juliet")
    $ count_points("zora")
    $ v_review_episode = 3
    call screen toh_final_review_screen
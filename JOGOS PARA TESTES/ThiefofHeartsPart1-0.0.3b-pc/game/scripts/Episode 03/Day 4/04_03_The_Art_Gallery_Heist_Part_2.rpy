init:
    $ v_ep03_04_03_maze_minigame = False
    $ v_ep03_04_03_levers_minigame = False

label lb_ep03_04_03_The_Art_Gallery_Heist_Part_2:
    #SCENE BEGINS

    centered "Later that night...{w=2.0}{nw}" with dissolve
    show text "Later that night..."
    scene bg black with Dissolve(1)
    pause 1.0

    #Victor is in the van with Ariel, while the MC and Bella are dressed in dark disguises, ready to rob the gallery
    #this is how they’re dressed:
    #MC - https://pixhost.to/show/446/524192104_mc_disguise.jpg
    #Make sure he has gloves on and not showing his fingerprints.
    #And cover his hair with a beanie
    #Bella - https://pixhost.to/show/446/524192101_bella_disguise.jpg (She’s also still wearing the pendant she had on during the previous scene
    #Ariel - https://pixhost.to/show/446/524192098_ariel01_out06-logo.png
    #Victor - he has changed out of his limousine driver’s outfit and has his earpiece in
    #IMPORTANT - make sure they’re both wearing gloves, so as to not leave their fingerprints on anything

    #evening setting, after sunset
    #The MC, Victor, Bella and Ariel sit inside the van
    play music "sound effects/01/Covert Affair.mp3" loop fadein 1.0
    scene sc ep3heistpart2 j001
    with dissolve
    vic"Okay, is everybody ready?"
    show sc ep3heistpart2 j002
    mc"Yeah, we’re all set."
    show sc ep3heistpart2 j005
    vic"Here, don’t forget this, [b_name]."
    #Victor hands Bella a pole-shaped container that has the forged painting inside of it - https://www.slimlinewarehouse.com.au/static/products/1561/large_592b308f-58a8-4242-a03b-fbbd47d294d3.webp
    #IMPORTANT: Victor isn’t wearing gloves, therefore, his fingerprints are on it. This will be important later when the police ask him questions.
    show sc ep3heistpart2 j005a
    with dissolve
    pause 1.0
    show sc ep3heistpart2 j004
    with dissolve
    b"Oh, right. Thanks."
    show sc ep3heistpart2 j005b
    vic"All right, get going you two."
    vic"The clock is ticking..."
    show sc ep3heistpart2 j006
    with dissolve
    pause 1.0
    show sc ep3heistpart2 j007
    with dissolve
    pause 1.0
    #show the MC and Bella exiting the van which is parked in a dark area across from the art gallery carpark
    #screen fades and returns shortly after

    #show the MC and Bella in their changed outfits, walking along the outside of the gallery, a darkened area
    show sc ep3heistpart2 j008
    with dissolve
    a"Where exactly are you right now, guys?"
    #Ariel speaks from the truck
    show sc ep3heistpart2 j009
    mc"We’re approaching the entrance. The one that I disabled this afternoon."
    #The MC and Bella approach the side of the gallery
    #show her carrying a pole-shaped container that has the forged painting inside of it - https://www.slimlinewarehouse.com.au/static/products/1561/large_592b308f-58a8-4242-a03b-fbbd47d294d3.webp
    #you’ll have to show her carrying it the entire time
    #Victor speaks to everyone else from the van now.
    show sc ep3heistpart2 j010
    vic"Good."
    show sc ep3heistpart2 j011
    vic"And we’ve still got eyes thanks to your pendant, [b_name]."

    #show Bella still wearing her pendant
    show sc ep3heistpart2 j012
    vic"Once the two of you are inside, you’ll probably lose radio contact with us again."
    #show the MC and Bella listening to Victor as he speaks
    show sc ep3heistpart2 j013
    with dissolve
    vic"Do you have the underground plans I forwarded to you from the flash drive, [y_name]?"
    show sc ep3heistpart2 j014
    mc"Yeah, I have it."
    #The MC has the underground map of the gallery on his phone
    show sc ep3heistpart2 j015
    b"What do we need it for? Can’t we just go back in the same way we found this emergency exit?"
    show sc ep3heistpart2 j016
    vic"No... Now that the gallery is closed, it will have a lot more security measures in place this time of night."
    show sc ep3heistpart2 j017
    vic"However, if you follow those plans, there’s a couple of ways through the underground tunnel that you can take
    to shortcut your way straight into the gala room where the painting is."
    vic"Plus there are no security cameras in that part of the underground."
    #Show the MC and Bella listening while Victor speaks
    show sc ep3heistpart2 j018
    vic"Make sure to take a good look around when you’re inside and get familiar with your surroundings."

    vic"You’ll need to do this for when you have the painting during your escape."
    show sc ep3heistpart2 j019
    mc"Will do."
    show sc ep3heistpart2 j020
    mc"[a_name]... Are there any of their security doing their rounds outside of the gallery at the moment?"
    show sc ep3heistpart2 j021
    a"I can see one guy, but he’s on the other side of the venue."
    show sc ep3heistpart2 j008
    a"So you should have enough time to get inside without being noticed if you move quickly."
    show sc ep3heistpart2 j022
    mc"All right, let’s go now, [b_name]..."
    #The MC opens the door to the underground of the gallery, letting Bella in first, and he follows her in.
    #screen fades and then shows Bella and the MC inside the underground agai
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    play sound "sound effects/03/cave_sound_effect.mp3" loop fadein 1.0
    show sc ep3heistpart2 j023
    with dissolve
    pause 2.0
    show sc ep3heistpart2 j027
    with dissolve
    b"Okay, now that we’re here, which way do we go?"

    # their options are to go left or right
    show sc ep3heistpart2 j025
    mc"Well..."
    #The MC looks at his phone, which is tilts into landscape mode
    show sc ep3heistpart2 j026
    mc"According to these underground plans, we could go in either direction to get to that room."
    show sc ep3heistpart2 j027
    b"So should we go left, or right?"
    #[Left / Right]
    menu:
        "Left"(wt="Short way, leads to Laser Beam mini-game + 3 x Task points"):
            show sc ep3heistpart2 j028
            mc"Let’s go this way..."
            #show the MC and Bella walking off in this direction to the left of where they began
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            stop sound fadeout 1.0
            #the MC and Bella enter through a door that places them down the opposite end of the room to where the painting is
            #this room is not lit up, as we need to show the slightly visible laser beams between the MC/Bella and the painting
            play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
            show sc ep3heistpart2 j029
            with dissolve
            pause 2.0
            show sc ep3heistpart2 j030
            with dissolve
            b"Here we are."
            show sc ep3heistpart2 j031
            mc"Can you see us, [a_name]?"
            show sc ep3heistpart2 j021
            a"Yeah, we’ve got you."
            #Victor stands beside Ariel while in the truck - he doesn’t speak, he just listens in
            show sc ep3heistpart2 j033
            a"I’ve also altered the images on the cameras in that room to make it look like no one is there."
            #show an image from the security office where the screens show an empty room. The guy in that room sees nothing unusual
            show sc ep3heistpart2 j034
            mc"Perfect."
            show sc ep3heistpart2 j127
            b"All right, let’s go get that painting!"
            #Bella is about to head towards the painting and the MC stops her, putting his hand across the top of her chest
            show sc ep3heistpart2 j036
            mc"Wait!"
            show sc ep3heistpart2 j037
            b"What’s wrong?"
            show sc ep3heistpart2 j038
            mc"Look."
            #The MC points out the sets of lasers across the floor and at various heights - https://media.istockphoto.com/id/1202920845/vector/museum-laser-beam-security-system-realistic-vector.jpg?s=170667a&w=0&k=20&c=FqFY8rLttnI61OElw0c35sNchaJRYbT9fYdVU5x2d5Q=
            #Preferably have the beams run across the room horizontally
            show sc ep3heistpart2 j039
            mc"They have laser beams across this room."
            show sc ep3heistpart2 j040
            b"Shit!"
            show sc ep3heistpart2 j128
            b"I nearly ran straight into one of them."
            show sc ep3heistpart2 j041
            b"What are we going to do?"
            show sc ep3heistpart2 j042
            mc"[a_name], we have a problem."
            #the MC tries to communicate with her via his earpiece
            show sc ep3heistpart2 j043
            mc"This gala room has laser beams between us and the painting."
            show sc ep3heistpart2 j128
            mc"We could try and wiggle and move our way past them, but one slip up and we’ll trigger the alarm."
            show sc ep3heistpart2 j044
            a"I had a feeling that this might happen."
            show sc ep3heistpart2 j045
            a"According to the gallery layout, there should be a control room close by where you can turn those beams off."
            show sc ep3heistpart2 j046
            a"Can you see it?"
            #The MC and Bella look around
            #Bella notices a small single door
            show sc ep3heistpart2 j047
            b"Maybe that’s it. That door over there."
            #Bella points at it
            show sc ep3heistpart2 j048
            mc"Let’s check it out..."
            stop music fadeout 2.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #the scene returns with the MC and Bella inside the control room
            #There are sets of levers against a wall
            play music "sound effects/03/Gallery Heist.mp3" loop fadein 1.0
            show sc ep3heistpart2 j049
            with dissolve
            pause 2.0
            show sc ep3heistpart2 j050
            with dissolve
            mc"Okay, we’re in the control room."
            show sc ep3heistpart2 j052
            mc"What are we looking for?"
            show sc ep3heistpart2 j008
            a"There will be a set of levers or maybe a set of buttons that will turn the beams off."
            show sc ep3heistpart2 j021
            a"You'll have to work out how to do that."
            show sc ep3heistpart2 j051
            mc"Hmm..."
            mc"It's a panel with buttons."
            show sc ep3heistpart2 j052
            mc"[b_name], I’m going to have to try some combinations with these levers."
            show sc ep3heistpart2 j053
            mc"Poke your head outside the room and let me know if I’ve switched them all off."
            #The MC addresses Bella with this line above
            show sc ep3heistpart2 j054
            b"Okay."
            show sc ep3heistpart2 j052
            mc"All right, let’s see here..."
            call screen scr_ep03_levers_screen
            #the MC looks at the levers
            $ v_ep03_04_03_levers_minigame = True
            jump lb_ep3_levers_minigame
            #LASER BEAM MINI-GAME BEGINS HERE
            #Give the players instructions on the screen for how the Mini-Game Maze works.
            #Place these lines below on the screen:
            #You need to figure out the correct lever combination in order to turn all the laser beams off.
            #[b_name] will let you know if you have turned them all off or not.
            #Make sure to take note of which options you have chosen in case you make a mistake.
            #Once you have the correct combination, the laser beams will be switched off and you can get to the painting.

            #IF THE PLAYER CHOOSES THE WRONG COMBINATION



        "Right"(wt="Long way, leads to the maze mini-game + 3 x Task points"):

            show sc ep3heistpart2 j064
            mc"Let’s go this way..."
            stop sound fadeout 1.0
            #show the MC and Bella walking off in this direction to the right of where they began
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            play music "sound effects/03/Gallery Heist.mp3" loop fadein 1.0
            call screen scr_ep03_maze_screen
            $ v_ep03_04_03_maze_minigame = True
            jump lb_ep03_04_03_Maze_Minigame
            #MINI-GAME MAZE BEGINS HERE
            #Give the players instructions on the screen for how the Mini-Game Maze works
            #Place these lines below on the screen:
            #Once you begin, on the screen will be two or more arrows to choose from.
            #Click the arrow you think is the correct option each time.
            #If you reach a dead end, then you have gone the wrong way
            #Make sure to take note of which options you have chosen
            #Once you have made all the correct choices, it will lead you into the Gala Room where the painting is

            #AFTER THE PLAYER FINDS THE GALA ROOM
            #the MC and Bella enter through a door that places them at the end of the room where the painting is
            #this room is not lit up, as we need to show the laser beams in the room
            #They both look up at the painting



label lb_ep03_04_03_The_Art_Gallery_Heist_Part_2_continues:
    if v_ep03_04_03_maze_minigame:

        stop music fadeout 2.0
        scene black
        with dissolve
        scene black
        with Pause (2)

        play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
        show sc ep3heistpart2 j063
        b"There it is."
        show sc ep3heistpart2 j076
        mc"Can you see us, [a_name]?"
        show sc ep3heistpart2 j021
        a"Yeah, we’ve got you."
        #Victor stands beside Ariel while in the truck - he doesn’t speak, he just listens in
        show sc ep3heistpart2 j033
        a"I’ve also altered the images on the cameras in that room to make it look like no one is in there."
        #show an image from the security office where the screens show an empty room. the guy in that room sees nothing unusual
        show sc ep3heistpart2 j066
        mc"Perfect."
        $ v_ep03_task_14_helping_the_team += 3

        #they look up and the painting is on the wall in front of them.

        #"Hmm... There are laser beams behind us."
        #The looks behind him

        #"It’s a bit lucky that we entered the room this way."

        #"Yeah, they would’ve been a bitch to try and get through."
        #show sc ep3heistpart2 j065
        #mc"Anyway..."

    else:

        show sc ep3heistpart2 j058
        # random choice:
        $ choice = renpy.random.choice(["Is that it?", "How’s that?", "How about now?"])
        mc"[choice]"
        play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
        show sc ep3heistpart2 j059
        b"Yeah, you got it!"
        show sc ep3heistpart2 j060
        mc"Awesome!"
        $ v_ep03_task_14_helping_the_team += 3
        show sc ep3heistpart2 j061
        mc"Now it should be safe to move across the floor."
        show sc ep3heistpart2 j062
        with dissolve
        pause 1.5
        #show the MC and Bella safely walking across the floor
        #screen fades as the MC and Bella stand before the painting in the gala room
        show sc ep3heistpart2 j063
        with dissolve
        b"There it is."
        #they look up and the painting is on the wall in front of them.

        #Go down to > scene continues

    #scene continues
    show sc ep3heistpart2 j066
    mc"Let’s get it out of the frame."
    show sc ep3heistpart2 j068
    mc"Make sure the forged painting is ready for the swap-over, [b_name]."
    show sc ep3heistpart2 j069
    b"I’m on it."

    #she kneels and takes this sling off her shoulder - https://www.slimlinewarehouse.com.au/static/products/1561/large_592b308f-58a8-4242-a03b-fbbd47d294d3.webp

    #the MC surveys the painting and starts to remove it from the frame
    show sc ep3heistpart2 j070
    mc"Okay, steady as she goes."

    #Bella watches on as the MC carefully tries to open up the frame to slide the painting off
    show sc ep3heistpart2 j071
    b"Careful now."
    #as soon as he’s about to, a loud security alarm goes off
    show sc ep3heistpart2 j073
    mc"Not to worry. This is like taking candy from a baby."
    stop music fadeout 1.0
    #SECURITY ALARM SOUND EFFECT
    #the MC’s expression goes from cocky to stunned
    play sound "sound effects/03/security_alarm_sound_effect.mp3" loop fadein 0.5
    show sc ep3heistpart2 j130
    mc"Uh-oh."
    show sc ep3heistpart2 j074
    b"What the hell?"
    show sc ep3heistpart2 j075
    a"What happened?"
    show sc ep3heistpart2 j076
    mc"Something set the alarm off!"
    show sc ep3heistpart2 j077
    mc"There must be a trigger on the painting that we didn’t account for."
    show sc ep3heistpart2 j078
    vic"ABORT! ABORT!"
    #Victor stands beside Ariel while in the truck - he yells this line below and above
    show sc ep3heistpart2 j079
    vic"Get the hell out of there, as fast as you can!"

    #the MC and Bella try to exit through one of the doors they entered through."
    #It won’t open - SOUND EFFECT trying to open the door
    show sc ep3heistpart2 j080
    with dissolve
    pause 1.5
    show sc ep3heistpart2 j081
    mc"Shit!"
    show sc ep3heistpart2 j082
    mc"The door... It’s locked! We can’t get out!"

    #Bella tries one of the other doors on the opposite side of the room the MC has checked
    #make sure she doesn’t check a door that could be in line with where the laser beams are (for the "Right" option)"
    show sc ep3heistpart2 j083
    b"So is this one."
    show sc ep3heistpart2 j078
    vic"FUCK!!"
    show sc ep3heistpart2 j079
    vic"The gallery could be on a full lockdown."
    stop sound fadeout 1.0
    show sc ep3heistpart2 j084
    a"Okay, I've managed to access their security room to turn the alarm off, but the police are now on their way there."
    show sc ep3heistpart2 j081
    mc"We need another way out, [a_name], and fast!"
    show sc ep3heistpart2 j084
    a"All right, listen carefully."
    show sc ep3heistpart2 j075
    a"There should be a door panel on the floor in one of the corners of the room."
    show sc ep3heistpart2 j085
    a"Can you see it?"
    #the MC and Bella look at the floor
    show sc ep3heistpart2 j086
    with dissolve
    pause 1.5
    show sc ep3heistpart2 j087
    b"Yeah, we see it."
    show sc ep3heistpart2 j044
    a"Open it up."
    show sc ep3heistpart2 j045
    a"It should lead to a basement room."
    show sc ep3heistpart2 j088
    b"{i}(*Whispering*){/i}\nWhat about the painting?"
    #She whispers so Victor can’t hear their conversation
    show sc ep3heistpart2 j089
    mc"{i}(*Whispering*){/i}\nForget about it, [b_name]!"
    show sc ep3heistpart2 j090
    mc"{i}(*Whispering*){/i}\nIf either of us get caught we’re all done for!"
    show sc ep3heistpart2 j091
    mc"{i}(*Whispering*){/i}\nAnd leave the forgery. We can’t afford to be carrying any extra weight."
    #Bella leaves the pole-shaped container on the floor (important that you show this)
    show sc ep3heistpart2 j092
    vic"I just intercepted a police radio frequency!"
    show sc ep3heistpart2 j093
    vic"You have about three minutes at most before they arrive!"

    #show the MC climbing into the open floor panel - Bella has already gone in there ahead of him
    show sc ep3heistpart2 j090
    mc"Roger that!"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #scene returns with the MC and Bella in the basement room - https://i.pinimg.com/736x/c8/ab/16/c8ab161f0fac748f7654adc16de93697.jpg

    #make sure it doesn’t have anything the MC or Bella can stand on to allow him to get out of there
    #there needs to be a window panel up high that Bella can be lifted by the MC to help push her up to allow her to escape
    #example - https://i.pinimg.com/736x/fa/d2/89/fad289ace4a99541d3dfb7feff2b07fb.jpg
    #the idea is the MC will be stuck in there
    play music "sound effects/01/On The Ground.mp3" loop fadein 1.0
    show sc ep3heistpart2 j094
    b"Now what do we do?"
    menu:
        "Take time to think":
            #the MC and Bella look around
            show sc ep3heistpart2 j102
            b"What about up there!"
            show sc ep3heistpart2 j096
            with dissolve
            pause 1.5
            #The MC points to a window near the top of the ceiling that leads outside
            show sc ep3heistpart2 j097
            b"Could that be a way out?"
            show sc ep3heistpart2 j100
            mc"It looks like it."
            show sc ep3heistpart2 j099
            b"But how are we going to get up there?"

        "Find a way out"(wt="Task point"):
            #the MC and Bella look around
            show sc ep3heistpart2 j095
            mc"Look! Up there!"
            show sc ep3heistpart2 j096
            with dissolve
            pause 1.5
            #The MC points to a window near the top of the ceiling that leads outside
            show sc ep3heistpart2 j097
            b"Is that the way out?"
            show sc ep3heistpart2 j100
            mc"It’s {b}our{/b} way out."
            $ v_ep03_task_14_helping_the_team += 1
            show sc ep3heistpart2 j099
            b"How are we going to get up there?"

    show sc ep3heistpart2 j102
    b"There’s nothing in here that we can stand on and no ladders either."
    show sc ep3heistpart2 j098
    mc"I’ll boost you up."
    show sc ep3heistpart2 j103
    mc"Come on, we don't have much time."
    #screen dissolves and returns with the MC helping to lift Bella up
    show sc ep3heistpart2 j104
    with dissolve
    mc"See if you can push the window open."

    #The MC lifts up Bella all the way
    show sc ep3heistpart2 j105
    with dissolve
    pause 1.5
    #show different angles in her skin-tight outfit
    show sc ep3heistpart2 j106
    with dissolve
    pause 1.5
    #show a POV angle for the MC
    show sc ep3heistpart2 j107
    with dissolve
    pause 1.5

    #Show Bella eye-level with the window
    show sc ep3heistpart2 j108
    with dissolve
    pause 1.5
    play sound "sound effects/03/opening_window_sound_effect.mp3" noloop
    show sc ep3heistpart2 j109
    with dissolve
    pause 1.0
    #she pushes it forward
    show sc ep3heistpart2 j110
    b"It opens!"
    show sc ep3heistpart2 j111
    mc"All right, push yourself through."
    #The MC pushes her up and Bella slides through and out of the window
    show sc ep3heistpart2 j112
    with dissolve
    pause 1.5
    #show the first half of her body, so we see her ass and legs in between the window
    show sc ep3heistpart2 j113
    with dissolve
    pause 1.5
    #and then she’s all the way out
    show sc ep3heistpart2 j114
    with dissolve
    mc"Okay, now get back to the truck."
    #she spins around to face him
    show sc ep3heistpart2 j115
    b"But what about you?"
    show sc ep3heistpart2 j116
    b"I can’t just leave you in there, [y_name]."
    #she looks worried
    show sc ep3heistpart2 j117
    mc"Don’t worry about me, just go!"
    show sc ep3heistpart2 j118
    b"But [y_name]..."
    show sc ep3heistpart2 j119
    mc"[b_name]! Listen to me!"
    #The MC yells at her
    show sc ep3heistpart2 j120
    mc"Go back to the truck and wait."
    if v_ep03_task_14_helping_the_team == 5:
        $ task_completed(14,"aa")
        $ v_ep03_othergirls_aa_tasks_counter +=1
    if v_ep03_task_14_helping_the_team == 4:
        $ task_completed(14,"a")
    if v_ep03_task_14_helping_the_team == 3:
        $ task_completed(14,"b")
    if v_ep03_task_14_helping_the_team <= 2:
        $ task_completed(14,"c")
    if v_ep03_task_14_helping_the_team <= 1:
        $ task_completed(14,"d")
    show sc ep3heistpart2 j121
    mc"If I’m not there in five minutes, then leave without me."
    show sc ep3heistpart2 j122
    mc"Is that understood?"
    #He has a look of seriousness on his face
    show sc ep3heistpart2 j123
    b"Okay, okay. I’m going."
    #she backs off
    show sc ep3heistpart2 j124
    b"I’ll see if I can get [mc_vic_address] to help..."
    #Bella leaves
    show sc ep3heistpart2 j125
    with dissolve
    pause 1.5
    # The final shot here is of the MC still in the basement
    #screen goes blank
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_04_04_The_Art_Gallery_Heist_Part_3

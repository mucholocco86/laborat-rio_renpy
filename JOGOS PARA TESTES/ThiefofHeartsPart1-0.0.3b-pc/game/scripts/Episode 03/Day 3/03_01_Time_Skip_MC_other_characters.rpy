

label lb_ep03_03_01_Time_Skip_Montage_MC_other_characters:

    #Time Skip - Fitness sessions with Zora and Juliet, 
    #Victor planning out the art gallery heist, MC spending time with each LI

    centered "Over the next week...{w=2.0}{nw}" with dissolve
    show text "Over the next week..."
    scene bg black with Dissolve(1)
    pause 1.0
    #play music "sound effects/03/team_america_montage.mp3" noloop
    #MONTAGE MUSIC REQUIRED HERE - The Week’s Rollercoaster
    play music "sound effects/03/The Weeks Rollercoaster1.mp3" loop fadein 1.0
    $ image_sequence("sc ep3timeskip", ["m001", "m002", "m003", "m004", "m005", "m006", "m007","m008","m009", "m010"], 2.0)
    #show a montage of the MC training with Zora
    # show sc ep3timeskip m001
    # with dissolve
    # pause 2.0
    # #she copies his moves 
    # show sc ep3timeskip m002
    # with dissolve
    # pause 2.0
    # #he helps her to do sit-ups 
    # show sc ep3timeskip m003
    # with dissolve
    # pause 2.0
    # #they do pushups together, lift dumbbells 
    # show sc ep3timeskip m004
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m005
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m006
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m007
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m008
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m009
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m010
    # with dissolve
    # pause 2.0
    #Add this image if the MC slept with Zora
    if v_ep3_sex_with_Zora == True:
        show sc ep3timeskip m010a
        with dissolve
        pause 2.0
    #Show the MC and Zora making out on the padded mat in one of the closed-off rooms - the same one he uses to fight with Juliet
    with slow_dissolve
    show sc ep3timeskip m011
    with dissolve
    pause 2.0
    # #Victor maps out the art gallery heist 
    # #It has the caption “THE GERMAN ARTIST” written on it
    # with slow_dissolve
    # #Vivian is in the kitchen and prepares dinner, daydreaming, depressed 
    with slow_dissolve
    show sc ep3timeskip m012
    with dissolve
    pause 2.0
    with slow_dissolve
    # with slow_dissolve
    # #The MC comes in and gives her a hug from behind which makes her smile 
    show sc ep3timeskip m013
    with dissolve
    pause 2.0
    with slow_dissolve
   
    #Add these images if the player has TWO Vivian hearts or more 
    if vivian_love_level >= 2:
        show sc ep3timeskip m013c
        with dissolve
        pause 2.0
        show sc ep3timeskip m013b
        with dissolve
        pause 2.0
        show sc ep3timeskip m013a
        with dissolve
        pause 2.0
        show sc ep3timeskip m013d
        with dissolve
        pause 2.0

        #She turns around and then they make it to the kitchen
        
        #The MC slides up the side of her dress and rests his hand on her outer thigh
        
        #she stops him with her hand and places the other hand on his chest
        
        #he smiles
        
        #they kiss again
    with slow_dissolve
    show sc ep3timeskip m014
    #ith dissolve
    pause 3.0
    with slow_dissolve
    show sc ep3timeskip m015
    #ith dissolve
    pause 3.0
    with slow_dissolve
    $ image_sequence("sc ep3timeskip", ["m016a", "m016b", "m016c", "m016d", "m016e"], 2.2)
    # #The MC leaves and Vivian looks like she’s having a naughty thought
    with slow_dissolve
    $ image_sequence("sc ep3timeskip", ["m017", "m018", "m019", "m019a", "m019b", "m019c"], 2.2)
    # show sc ep3timeskip m015
    # with dissolve
    # pause 2.0
    # with slow_dissolve
    # #Bella tries on some costumes in preparation for intercepting the German woman
    # show sc ep3timeskip m016
    # with dissolve
    # pause 2.0
    # #The MC comes into her room dressed up as well - a complete look
    # show sc ep3timeskip m016a
    # with dissolve
    # pause 2.0
    # #Show Bella helping him put his tie on
    # show sc ep3timeskip m016b
    # with dissolve
    # pause 2.0
    # #Add this image if the player has ONE Bella heart or more 
    # show sc ep3timeskip m016c
    # with dissolve
    # pause 2.0
    # #Show the MC looking down at her cleavage while she adjusts his tie
    # show sc ep3timeskip m016d
    # with dissolve
    # pause 2.0
    # #then show Bella catching the MC doing that
    # #Finally, show Bella chasing the MC out of her room
    # #He has a laughing look on his face while she looks pissed off
    # show sc ep3timeskip m016e
    # with dissolve
    # pause 2.0
    # #the MC and Juliet jog alongside each other on a treadmill, sweating it up 
    # with slow_dissolve
    # show sc ep3timeskip m017
    # with dissolve
    # pause 2.0
    # #then show them in the same room they were in when they wrestled - sparring together 
    # with slow_dissolve
    # show sc ep3timeskip m018
    # with dissolve
    # pause 2.0
    # with slow_dissolve
    # show sc ep3timeskip m019
    # with dissolve
    # pause 2.0
    # #but they have more fun this time - both smiling as they wrestle on the floor
    # show sc ep3timeskip m019a
    # with dissolve
    # pause 2.0
    # #show the MC and Ariel at an ice cream parlour, sitting opposite each other, talking
    # show sc ep3timeskip m019b
    # with dissolve
    # pause 2.0
    # show sc ep3timeskip m019c
    # with dissolve
    # pause 2.0
    #This image if you have less than TWO Ariel Hearts
    with slow_dissolve
    if ariel_love_level <= 1:
        show sc ep3timeskip m020
        with dissolve
        pause 2.0
        with slow_dissolve
    #Add this image if the player has TWO Ariel hearts or more 
    if ariel_love_level >= 2:
        show sc ep3timeskip m021
        with dissolve
        pause 3.0
        show sc ep3timeskip m021a
        with dissolve
        pause 3.0
        with slow_dissolve
    #The MC and Ariel share an ice cream sundae like this - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeeuS8YbU_B6wWol6u4tHOrLqpol3NCb5Tow&s
    
    #They both then sit on the same side of the booth, with the MC’s arm around Ariel
    
    #She looks up at him
    
    #And then they share a short kiss
    show sc ep3timeskip m023
    with dissolve
    pause 3.0
    #then a final shot of the MC and the family/team sitting in the living room on the sofa.
    #They listen to Victor who stands before them, as he unveils his plan on a whiteboard for intercepting the German artist 
    #the whiteboard has the details of her arrival at the airport
    with slow_dissolve
    show sc ep3timeskip m022
    with dissolve
    pause 2.0

    scene black
    with Dissolve(5.0)
   
    #then the screen slowly fades to black
    #screen goes blank
    stop music fadeout 7.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_03_02_Intercepting_the_German_artist



    # centered "Over the next week...{w=2.0}{nw}" with dissolve
    # show text "Over the next week..."
    # scene bg black with Dissolve(1)
    # pause 1.0
    # play music "sound effects/03/team_america_montage.mp3" noloop
    # show sc ep3timeskip m001
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m003
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m017
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m015
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m016a
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m012
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m013
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m021
    # with dissolve
    # pause 2.2
    # show sc ep3timeskip m021a
    # with dissolve
    # pause 1.7

    # with slow_dissolve
    # show sc ep3timeskip m011
    # with dissolve
    # pause 1.7
    # with slow_dissolve
    
    # show sc ep3timeskip m013c
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m013d
    # with dissolve
    # pause 1.7
    # with slow_dissolve
    # show sc ep3timeskip m018
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m019
    # with dissolve
    # pause 1.7
    
    # show sc ep3timeskip m019a
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m019b
    # with dissolve
    # pause 1.7
    # with slow_dissolve

    # show sc ep3timeskip m016b
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m016c
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m016d
    # with dissolve
    # pause 1.7

    # show sc ep3timeskip m007
    # with dissolve
    # pause 1.9
    # show sc ep3timeskip m009
    # with dissolve
    # pause 1.7
    # show sc ep3timeskip m010a
    # with dissolve
    # pause 1.7
    # with slow_dissolve
    # show sc ep3timeskip m023
    # with dissolve
    # pause 2.5
    # #then a final shot of the MC and the family/team sitting in the living room on the sofa.
    # #They listen to Victor who stands before them, as he unveils his plan on a whiteboard for intercepting the German artist 
    # #the whiteboard has the details of her arrival at the airport
    # with slow_dissolve
    # show sc ep3timeskip m022
    # with dissolve
    # pause 3.0

    # scene black
    # with Dissolve(5.0)
   
    
    # #then the screen slowly fades to black
    # #screen goes blank
    # stop music fadeout 8.0
    # scene black
    # with dissolve
    # scene black
    # with Pause (2)
    # jump lb_ep03_03_02_Intercepting_the_German_artist



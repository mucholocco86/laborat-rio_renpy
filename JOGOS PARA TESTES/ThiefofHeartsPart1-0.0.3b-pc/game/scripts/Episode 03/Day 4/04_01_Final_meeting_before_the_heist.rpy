

label lb_ep03_04_01_Final_meeting_before_the_heist:
    #SCENE BEGINS

    centered "The Morning of the Art Gallery Heist...{w=2.0}{nw}" with dissolve
    show text "The Morning of the Art Gallery Heist..."
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/03/montage_music_pre_gallery_heist.mp3" loop fadein 1.0
    scene sc finalmeeting i001
    with dissolve
    pause 2.0
    #show the team sitting at the breakfast table on the morning of the heist
    $ task_addfuturetask("",4)
    $ task_addnew("Try to help the group on the next major heist",14)
    #Victor has a whiteboard with the underground layout of the Art Gallery on it
    show sc finalmeeting i002
    with dissolve
    vic"So let me go over the plan one last time."
    show sc finalmeeting i003
    b"Do we have to?"
    #Bella reacts to this. She’s tired of hearing it over and over again
    show sc finalmeeting i004
    b"I feel like you’ve explained it to us a hundred times already."
    show sc finalmeeting i005
    vic"This is the biggest job any of us have ever attempted."
    show sc finalmeeting i006
    vic"So we have to be flawless, as one slip-up could bring the entire plan crashing down."
    show sc finalmeeting i007
    vic"Now let me start again from the beginning."

    #VICTOR NARRATES HERE WHILE WE SHOW IMAGES OF WHAT THE TEAM ARE DOING AT THE TIME
    show sc finalmeeting i008
    with dissolve
    vic"{i}We’ll all leave here at one-thirty.{/i}"
    #show Bella getting changed into her dress/gown for the function in her room
    #IMPORTANT - MAKE SURE SHE’S WEARING A NECKLACE WITH PENDANT.
    #IT’S SO ARIEL CAN STORE A HIDDEN CAMERA IN IT
    show sc finalmeeting i009
    with dissolve
    vic"{i}The function begins at two o’clock so that should be enough time to get everything ready to go.{/i}"
    #show Vivian getting changed into her dress/gown for the function in her room
    show sc finalmeeting i010
    with dissolve
    vic"{i}[a_name] will fit you all with a spy camera so that she can see everything you see from the van.{/i}"
    #show Ariel placing the spy camera into the MC’s bow tie
    show sc finalmeeting i011
    with dissolve
    vic"{i}We’ll have to do one final check after she’s mic’d the three of you up, just to make sure we can hear you clearly.{/i}"
    #Show Bella wearing an earpiece
    show sc finalmeeting i012
    with dissolve
    vic"{i}Girls, be sure to leave yourselves enough time to get changed and to do your hair and makeup, so we arrive at the function just before it begins.{/i}"
    #show Bella and Vivian in the bathroom changed into their clothing for the heist
    show sc finalmeeting i013
    with dissolve
    vic"{i}[y_name], you’ll have to do likewise.{/i}"
    #show the MC getting ready in his room, changed into his suit - white jacket, black pants and bow tie
    show sc finalmeeting i014
    with dissolve
    vic"{i}The commute time from here to the art gallery is approximately twenty minutes.{/i}"
    #show Bella, the MC and Vivian standing outside the front of the house, changed into their disguises/clothes for the function
    show sc finalmeeting i015
    with dissolve
    vic"{i}I’ll be driving the limo that escorts [v_name], aka... The German artist, to the party.{/i}"
    #Show Vivian getting into the back of Victor’s limo. Victor dressed as he does for work as a limo driver
    show sc finalmeeting i016
    with dissolve
    vic"{i}[y_name] and [b_name], you’ll need to drop [a_name] off outside the back of the gallery first.{/i}"
    #show the MC driving a car from the house with Bella in the passenger seat, and Ariel sitting in the back seat.
    show sc finalmeeting i017
    with dissolve
    vic"{i}That’s where our communication truck will be parked.{/i}"
    #show the limo on a main road, Victor driving with Vivian in the backseat, and the MC, Bella and Ariel in the car behind them
    show sc finalmeeting i018
    with dissolve
    vic"{i}I’ll join [a_name] after I've dropped [v_name] off out the front.{/i}"
    #show the limo Victor is driving pulling up outside the art gallery
    #show Vivian getting out and being greeted by a member of the art gallery
    show sc finalmeeting i019
    with dissolve
    vic"{i}There will be a lot of attention on [v_name] once she arrives, so [y_name] and [b_name], you’ll have to make sure you’re close by when that happens.{/i}"
    #show Vivian walking towards the entrance of the gallery
    show sc finalmeeting i020
    with dissolve
    pause 2.0
    #USE THIS SETTING: https://pixhost.to/show/399/523639538_sc-artgallery-a015.jpg - https://pixhost.to/show/399/523639551_sc-artgallery-a015a.jpg
    #ADD A RED CARPET AND VELVET ROPE CONNECTED TO POLES ON THE WALK INTO THE GALLERY
    show sc finalmeeting i021
    with dissolve
    mc"{i}What about the invitations?{/i}"
    #show the MC and Bella walking up to the entrance of the art gallery behind Vivian
    #the scene cuts back to the team meeting
    show sc finalmeeting i022
    with dissolve
    b"I found an invite that the German artist had on her. I created a copy of it for us and also for [mc_v_address]."
    #show Bella addressing the MC at the breakfast table
    show sc finalmeeting i023
    a"And I was able to hack into the gallery’s computer system so that you and [b_name] are on the guest list."
    #Show Ariel addressing the MC at the breakfast table
    show sc finalmeeting i024
    with dissolve
    mc"{i}What will our names be?{/i}"
    #scene cuts back to the MC and Bella walking up to the art gallery entrance, where they are stopped by a member of security on the door
    #They hand their invites to the man on the door who looks over his checklist
    #then he looks them over and speaks to the MC
    show sc finalmeeting i025
    with dissolve
    pause 1.0
    show sc finalmeeting i026
    with dissolve
    "Thank you, Mister Cohen."
    show sc finalmeeting i027
    mc"Please, call me Dean."
    #he then looks over Bella
    show sc finalmeeting i028
    "So you must be..."
    show sc finalmeeting i029
    b"Lauren Winchester."
    show sc finalmeeting i025
    with dissolve
    pause 1.0
    show sc finalmeeting i030
    with dissolve
    "Of course."
    show sc finalmeeting i031
    "Have fun, folks."
    #The guy on the door steps aside and the MC addresses Victor and Ariel (in the truck) just before they enter the gallery
    show sc finalmeeting i033
    mc"{i}(*Whispering*){/i}\nAll right, we’re heading in..."
    $ image_sequence("sc finalmeeting", ["i032", "i034"], 1.7)
    # show sc finalmeeting i032
    # with dissolve
    # pause 2.0
    # show sc finalmeeting i034
    # with dissolve
    # pause 2.0
    #When he speaks, we can see the earpiece he’s wearing
    #final shot here of the MC and Bella walking into the front entrance of the gallery - show this shot from behind them
    stop music fadeout 2.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_04_02_The_Art_Gallery_Heist_Part_1
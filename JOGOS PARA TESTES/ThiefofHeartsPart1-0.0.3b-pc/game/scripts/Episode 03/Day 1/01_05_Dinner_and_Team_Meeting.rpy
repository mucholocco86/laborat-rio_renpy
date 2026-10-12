init:
    $ v_ep03_01_05_checking_on_Vivian_counter = 0


label lb_ep03_01_05_Dinner_and_Team_Meeting:
    #start with the chat during dinner about their days
    centered "Later that evening...{w=2.0}{nw}" with dissolve
    show text "Later that evening..."
    scene bg black with Dissolve(1)
    pause 1.0
    scene black
    with dissolve
    play music "sound effects/03/family_feast_fiasco.mp3" loop fadein 1.0
    scene sc ep3teammeeting e001
    with dissolve
    v"Dinner everyone!"
    #she calls out to everyone upstairs from the kitchen area - a close-up of her face
    show sc ep3teammeeting e002
    with dissolve
    pause 2.0
    #the MC and the girls come down the stairs
    #coming down the stairs sound effect
    show sc ep3teammeeting e003
    with dissolve
    pause 2.0
    #expand the shot so we see Vivian in the kitchen, cooking - she’s wearing a motherly dress, but also all dressed up to impress Victor
    #https://img.freepik.com/premium-photo/beautiful-young-woman-cooking-kitchen-healthy-food-concept_21255-819.jpg?w=360
    show sc ep3teammeeting e004
    with dissolve
    a"Woah..."
    show sc ep3teammeeting e005
    with dissolve
    b"What’s all this for?"
    #the MC and the girls stand and look at the dinner that Vivian has prepared for everyone
    #she has made a small banquet - https://www.ikea.com/images/a-buffet-table-with-food-and-drink-in-various-bowls-dishes-a-026f0392372976ec801892eeb4dce1d6.jpg?f=s
    show sc ep3teammeeting e006
    pause 2.0
    show sc ep3teammeeting e007
    with dissolve
    v"Well, it’s a very special night."
    show sc ep3teammeeting e008
    v"It’s me and [vic_name]’s wedding anniversary."
    show sc ep3teammeeting e009
    a"Oh! How wonderful!"
    show sc ep3teammeeting e010
    mc"How could you afford all of this, [mc_v_address]?"
    #The MC refers to the food on the table
    show sc ep3teammeeting e016
    v"Oh, I didn’t get it all today, sweetheart."
    v"That would have been far too expensive."
    show sc ep3teammeeting e008
    v"I just kept my eye out for sales over the past few weeks."
    v"That way we can afford to have this wonderful meal tonight."
    show sc ep3teammeeting e012
    b"This looks incredible, [mc_v_address]."
    show sc ep3teammeeting e013
    a"It does, but you still should’ve let us help you."
    show sc ep3teammeeting e014
    v"Honestly, it’s fine dear. Besides, I enjoy doing this."
    show sc ep3teammeeting e015
    a"Is [mc_vic_address] here?"
    show sc ep3teammeeting e011
    v"He should be home any minute now."
    show sc ep3teammeeting e017
    v"I had to put dinner out now before it gets cold."
    v"But I’ve kept his dinner warm for him."
    show sc ep3teammeeting e018
    a"I’m sure he’s going to really appreciate all the trouble you went to for this."
    show sc ep3teammeeting e007
    v"Go ahead, take a seat guys."
    #the MC and the girls sit at the dinner table
    show sc ep3teammeeting e019
    with dissolve
    pause 2.0
    show sc ep3teammeeting e020
    a"How old were you when you got married? I’ve forgotten."
    #Ariel looks up at Vivian from a seated position as she puts another bowl of food on the table
    show sc ep3teammeeting e021
    v"I was eighteen, and your father was twenty-one. Nearly twenty-two."
    show sc ep3teammeeting e022
    b"So I was born not long after, right?"
    show sc ep3teammeeting e023
    v"That’s correct."
    show sc ep3teammeeting e024
    a"You never told us... Why did you decide to get married so young?"
    show sc ep3teammeeting e025
    v"It’s a long story."
    show sc ep3teammeeting e026
    v"But the main thing is, our story is still going."
    show sc ep3teammeeting e023
    v"Now come on, eat up. Enjoy yourselves."
    show sc ep3teammeeting e027
    mc"(She’s in a very good mood tonight.)"
    #Vivian heads back into the kitchen while the other three talk
    show sc ep3teammeeting e028
    mc"(Hopefully, [mc_vic_address] doesn’t do anything to spoil it.)"
    #show the MC looking at his food
    show sc ep3teammeeting e029
    mc"Are you working at the clothing store tomorrow, [b_name]?"
    show sc ep3teammeeting e030
    b"Yeah, I’m there from open until close."
    show sc ep3teammeeting e031
    b"Why?"
    show sc ep3teammeeting e032
    mc"I’m going to need some specific clothing for this job [mc_vic_address] has for us."
    show sc ep3teammeeting e033
    b"All right, I’ll make sure I have plenty of options for you to look over when you get there."
    show sc ep3teammeeting e032
    mc"Are you working in the morning, [a_name]?"
    show sc ep3teammeeting e035
    a"I don’t start work until after lunch. I’m just doing a half-day at the shop."
    show sc ep3teammeeting e036
    mc"Do you want to come with me to [b_name]’s store?"
    mc"You can look at some clothing as well."
    show sc ep3teammeeting e034
    a"Sure, count me in!"
    #NEW TASK ADDED - GO WITH ARIEL TO FIND CLOTHES AT BELLA’S STORE
    show sc ep3teammeeting e029
    mc"Do you think we can take clothes from your store so that your boss doesn’t know they’re missing, even for a couple of nights?"
    show sc ep3teammeeting e033
    b"Yeah, I’ll make some adjustments to our inventory and then change it back the following day."
    show sc ep3teammeeting e037
    b"Once we know what's needed, I’ll bring them home the day before we intercept this German artist."
    $ task_addfuturetask("",5)
    $ task_addnew("Intercept the German Artist at the Airport",13)
    play sound "sound effects/01/Door_Opening.mp3" noloop
    show sc ep3teammeeting e038
    with dissolve
    pause 1.3
    #the front door opens and Vivian looks in that direction - SOUND EFFECT door opening
    show sc ep3teammeeting e039
    with dissolve
    v"That will be your father now."
    #Vivian calls from the kitchen to the kids
    show sc ep3teammeeting e040
    with dissolve
    pause 2.0
    #Victor enters the room
    play sound "sound effects/01/door_close_soft.mp3" noloop
    show sc ep3teammeeting e041
    with dissolve
    vic"Evening all."
    show sc ep3teammeeting e042
    v"Hi honey."
    show sc ep3teammeeting e043
    v"Great timing. We were just about to start eating."
    #Victor looks at the MC, Ariel and Bella sitting at the dinner table
    #He’s completely oblivious to all the food Vivian has made
    show sc ep3teammeeting e044
    v"Would you like to join us?"
    show sc ep3teammeeting e045
    vic"No, I’m just making a pitstop. I’ll be heading back out again shortly. I need to get something from upstairs."
    show sc ep3teammeeting e046a
    v"Huh? Why?"
    #Vivian looks concerned
    show sc ep3teammeeting e047
    vic"I have another damn client to pick up from the airport and take them to their hotel."
    #he looks disgruntled
    show sc ep3teammeeting e047a
    vic"I'll be back later."
    show sc ep3teammeeting e048
    v"Oh..."
    #Victor goes upstairs
    show sc ep3teammeeting e049
    a"[mc_v_address!c]? Are you okay?"
    show sc ep3teammeeting e050
    v"I’m okay dear. It’s fine."

    #[Say something / Leave it]
    menu:
        "Say something"(wt="Best option"):
            show sc ep3teammeeting e053
            mc"I can go up and say something to him if you want."
            mc"Tell him to take the night off  and spend it with us instead."
            show sc ep3teammeeting e052
            v"No, you don’t need to, sweetheart."
            show sc ep3teammeeting e051
            mc"Huh? Why not?"
            show sc ep3teammeeting e054
            mc"You went to a lot of trouble for this asshole and he didn’t even have the decency to thank you for preparing dinner."
            show sc ep3teammeeting e053
            mc"And how the hell could he forget your anniversary??"
            v"..."
            $ v_ep01_ariel_respect_counter += 1
            show sc ep3teammeeting e055
            b"[y_name] is right, [mc_v_address]."
            $ v_ep01_bella_respect_counter += 1
            show sc ep3teammeeting e056
            v"I appreciate your concern, but please, don't worry about it guys."
            pause 1.5
            $ v_ep03_01_05_checking_on_Vivian_counter += 1

        "Leave it":
            show sc ep3teammeeting e057
            b"I can go upstairs and say something to that asshole before he leaves."
            show sc ep3teammeeting e058
            v"No, you don’t need to, sweetheart."
            show sc ep3teammeeting e059
            b"Why not?"
            #Bella angry
            show sc ep3teammeeting e060
            b"You went to a lot of trouble for tonight and he didn’t even have the decency to thank you for preparing dinner."
            show sc ep3teammeeting e057
            b"And how could he forget your anniversary??"
            show sc ep3teammeeting e054
            v"..."
            show sc ep3teammeeting e061
            mc"[b_name]’s right, [mc_v_address]."
            show sc ep3teammeeting e062
            v"I appreciate your concern, but please, don't worry about it guys."
            pause 1.5

    #Victor returns from upstairs
    show sc ep3teammeeting e063
    with dissolve
    vic"All right, I’ll be going now."
    show sc ep3teammeeting e064
    vic"I’ll be back soon, so don’t stay up too late."
    show sc ep3teammeeting e065
    vic"Tomorrow is another important day."
    show sc ep3teammeeting e066
    v"(As was tonight, for some...)"
    show sc ep3teammeeting e067
    vic"Bye..."
    #Vivian still looks depressed after Victor leaves the room
    show sc ep3teammeeting e068
    with dissolve
    pause 2.0
    #sound effect of the door slamming shut, Victor leaves the house
    show sc ep3teammeeting e070
    mc"And off he goes again."
    show sc ep3teammeeting e069
    b"[mc_v_address!c]?"
    #the three of them all look at Vivian. They all look concerned for her. Bella’s mouth is open to speak
    #MC is not happy about this
    show sc ep3teammeeting e071
    v"I um... I’m gonna go upstairs. I just need to be alone right now."
    #show Vivian looking despairingly
    show sc ep3teammeeting e072
    v"Enjoy your dinner, guys."
    show sc ep3teammeeting e073a
    with dissolve
    pause 1.5
    #Vivian leaves, she takes the bottle of wine and the glass she was drinking from with her
    #show Vivian leaving, about to go up the stairs
    show sc ep3teammeeting e073
    with dissolve
    a"Poor, [mc_v_address]."
    show sc ep3teammeeting e074
    b"I know, I feel so sorry for her."
    show sc ep3teammeeting e075
    a"Perhaps one of us should go and talk to her."
    show sc ep3teammeeting e076
    b"But she said she wants to be alone."
    show sc ep3teammeeting e077
    mc"We should give her some time, and some space. Respect her wishes."
    show sc ep3teammeeting e078
    mc"When the time is right, I’m sure she’ll talk to us."
    mc"Still, [mc_vic_address] is such an inconsiderate prick for ignoring her like that."
    show sc ep3teammeeting e079
    b"Finally, something we can agree on."
    show sc ep3teammeeting e078
    mc"Yeah..."
    mc"For now, the best way we can show [mc_v_address] our appreciation is to enjoy this meal she prepared."
    #show the food in front of them
    show sc ep3teammeeting e080
    a"And afterwards, we’ll clean everything up and put it all away so she doesn’t have to."
    show sc ep3teammeeting e081
    mc"Yeah, good idea."
    show sc ep3teammeeting e082
    mc"A toast guys. To [mc_v_address], and the incredible woman that she is."
    show sc ep3teammeeting e083
    b"Cheers!"
    #Sound Effect - chinking glasses
    play sound "sound effects/03/clinking_glasses_sound_effect.mp3" noloop
    show sc ep3teammeeting e084
    pause 2.0
    #the three of them raise their glasses and chink them together
    #(screen goes blank)"
    #END SCENE
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_01_06_Vivian_waits_for_the_MC_in_her_room

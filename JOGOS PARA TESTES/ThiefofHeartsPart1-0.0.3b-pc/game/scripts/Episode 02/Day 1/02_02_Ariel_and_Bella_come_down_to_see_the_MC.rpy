label lb_ep02_02_02_Ariel_and_Bella_come_down_to_see_the_MC:
    #SCENE BEGINS

    #The scene returns with Ariel and Bella coming down the stairs in their nightwear
    #Bella's is a little sexy, silky, whereas Ariel's is sexy but more casual 
    play music "sound effects/01/Imaginary_Heroes2.mp3" loop fadein 1.0
    show sc girlscomedowng 001
    with dissolve
    b"What's going on down here?" 
    #Bella says this as she and Ariel are coming down the stairs

    show sc girlscomedowng 002
    with dissolve
    a"[y_name]! You're back!"
    #Ariel is surprised when she sees the MC with Vivian when the girls get to the bottom of the stairs

    show sc girlscomedowng 003
    with dissolve
    a"And you're safe."

    show sc girlscomedowng 004
    mc"Just as I said I would be."
    #he places his hands on her shoulders to reassure her

    show sc girlscomedowng 005
    b"Where the hell were you?" 
    #she has her hands on her hips
    show sc girlscomedowng 006
    b"Do you realise how much trouble you've caused us?"
    #Bella not impressed 

    if v_ep01_day3_vivian_dress == "black":
        show sc girlscomedowng 007
        v"Easy now, [b_name]." 
        #Vivian breaks up the situation 

        show sc girlscomedowng 008
        with dissolve
        v"[y_name] has his reasons." 
        #She looks at the MC when she says this

        show sc girlscomedowng 010
        v"Also... Look at what he has." 
        #we see the flash drive in his hands

        show sc girlscomedowng 011
        a"You got it!" 
        #Ariel is happy and surprised 

        show sc girlscomedowng 012
        mc"Yeah, and not a moment too soon!"
        #Ariel closed mouth

        show sc girlscomedowng 013
        b"Good. Now [mc_vic_address] might finally get off our cases." 
        #Bella is also relieved 

        show sc girlscomedowng 014
        b"Actually, where is he?"
        #Bella looks around

        show sc girlscomedowng 015a
        v"He um... He went out."
        #Vivian makes up an excuse

        show sc girlscomedowng 016
        v"He said that he had to clear his head." 
        #a slightly different expression to the previous line

        show sc girlscomedowng 026
        with dissolve
        mc"(The less the girls know about the arguments between [mc_v_address!c] and [mc_vic_address] the better.)"
        #We see the three girls while the MC is thinking
        show sc girlscomedowng 003
        a"How long have you been home?" 
        #reuse a render from above 
        show sc girlscomedowng 012
        mc"Only about five or so minutes." 
        #reuse a render from above 
        show sc girlscomedowng 006
        b"And what were the two of you discussing before we came down?"
        #Bella looks sceptical
        show sc girlscomedowng 018a
        with dissolve
        mc"Not much."
        #reuse a render from above
        show sc girlscomedowng 019
        mc"[mc_v_address!c] just told me that I had to get the drive back the morning." 
        #we see three girls as mc points to her #don't worry, it will be mc pov 

        show sc girlscomedowng 020
        v"And you know what that means?" 
        #Vivian looks at the girls

        show sc girlscomedowng 021
        a"We'll be having another [private_group] meeting?"
        #Ariel addresses Vivian
        show sc girlscomedowng 022a
        v"That's right." 
        #reuse a render from above
        v"So we should all head back upstairs and get a good night's rest." 
        #a slightly different render to the one above

        show sc girlscomedowng 023
        b"Fine..." 
        #rolling eyes

        show sc girlscomedowng 024
        b"Though it might be hard to get back to sleep now." 
        #same expression as above, different pose
        show sc girlscomedowng 022a
        v"Off you go girls. [y_name] and I will be up shortly."
        show sc girlscomedowng 025
        a"Night guys."
        #Show Bella heading up the stairs as Ariel (at the base of the stairs) turns to Viv and the MC to speak 

        show sc girlscomedowng 026
        with dissolve
        mc"I'm gonna take a shower before I call it a night if that's okay?" 
        #just the MC and Vivian again now - Vivian stares at him while he speaks

        show sc girlscomedowng 027
        v"Of course you can."
        #Vivian smiles and responds  

        show sc girlscomedowng 028
        v"But just remember..." 
        #a different render to above, Vivian looks cautious

        show sc girlscomedowng 029
        mc"I know, I know. Don't use too much water." 
        #reuse a render above
        mc"Goodnight, [mc_v_address!c]." 
        #Vivian has a slight smile

        show sc girlscomedowng 027
        v"Night, sweetheart."
        #The MC heads up the stairs while Vivian watches him in the background 

        show sc girlscomedowng 030
        with dissolve
        mc"(It's nice to come home and not get yelled at for a change.)"
        #the MC smirks

        show sc girlscomedowng 032
        with dissolve
        mc"(However, I could still be waking up to that in the morning..)"
        #the MC looks concerned 
        #(screen goes blank)"
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_03_The_late_chat_with_Bella

    
    if v_ep01_day3_vivian_dress == "red":
        show sc girlscomedowng 007a
        v"Easy now, [b_name]." 
        #Vivian breaks up the situation 

        show sc girlscomedowng 015c
        with dissolve
        v"[y_name] has his reasons." 
        #She looks at the MC when she says this

        show sc girlscomedowng 010a
        v"Also... Look at what he has." 
        #we see the flash drive in his hands

        show sc girlscomedowng 011
        a"You got it!" 
        #Ariel is happy and surprised 

        show sc girlscomedowng 012
        mc"Yeah, and not a moment too soon!"
        #Ariel closed mouth

        show sc girlscomedowng 013
        b"Good. Now [mc_vic_address] might finally get off our cases." 
        #Bella is also relieved 

        show sc girlscomedowng 014
        b"Actually, where is he?"
        #Bella looks around

        show sc girlscomedowng 015c
        v"He um... He went out."
        #Vivian makes up an excuse

        show sc girlscomedowng 016a
        v"He said that he had to clear his head." 
        #a slightly different expression to the previous line

        show sc girlscomedowng 026a
        with dissolve
        mc"(The less the girls know about the arguments between [mc_v_address!c] and [mc_vic_address] the better.)"
        #We see the three girls while the MC is thinking
        show sc girlscomedowng 003
        a"How long have you been home?" 
        #reuse a render from above 
        show sc girlscomedowng 012
        mc"Only about five or so minutes." 
        #reuse a render from above 
        show sc girlscomedowng 006
        b"And what were the two of you discussing before we came down?"
        #Bella looks sceptical
        show sc girlscomedowng 018a
        with dissolve
        mc"Not much."
        #reuse a render from above
        show sc girlscomedowng 019a
        mc"[mc_v_address!c] just told me that I had to get the drive back by the morning." 
        #we see three girls as mc points to her #don't worry, it will be mc pov 

        show sc girlscomedowng 020a
        v"And you know what that means?" 
        #Vivian looks at the girls

        show sc girlscomedowng 021a
        a"We'll be having another [private_group] meeting?"
        #Ariel addresses Vivian
        show sc girlscomedowng 020a
        v"That's right." 
        #reuse a render from above
        v"So we should all head back upstairs and get a good night's rest." 
        #a slightly different render to the one above

        show sc girlscomedowng 023a
        b"Fine..." 
        #rolling eyes

        show sc girlscomedowng 024a
        b"Though it might be hard to get back to sleep now." 
        #same expression as above, different pose
        show sc girlscomedowng 020a
        v"Off you go girls. [y_name] and I will be up shortly."
        show sc girlscomedowng 025
        a"Night guys."
        #Show Bella heading up the stairs as Ariel (at the base of the stairs) turns to Viv and the MC to speak 

        show sc girlscomedowng 026a
        with dissolve
        mc"I'm gonna take a shower before I call it a night if that's okay?" 
        #just the MC and Vivian again now - Vivian stares at him while he speaks

        show sc girlscomedowng 027a
        v"Of course you can."
        #Vivian smiles and responds  

        show sc girlscomedowng 028a
        v"But just remember..." 
        #a different render to above, Vivian looks cautious

        show sc girlscomedowng 029a
        mc"I know, I know. Don't use too much water." 
        #reuse a render above
        mc"Goodnight, [mc_v_address!c]." 
        #Vivian has a slight smile

        show sc girlscomedowng 027a
        v"Night, sweetheart."
        #The MC heads up the stairs while Vivian watches him in the background 

        show sc girlscomedowng 030a
        with dissolve
        mc"(It's nice to come home and not get yelled at for a change.)"
        #the MC smirks

        show sc girlscomedowng 032
        with dissolve
        mc"(However, I could still be waking up to that in the morning..)"
        #the MC looks concerned 
        #(screen goes blank)"
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_03_The_late_chat_with_Bella

    
    if v_ep01_day3_vivian_dress == "golden":
        show sc girlscomedowng 015b
        v"Easy now, [b_name]." 
        #Vivian breaks up the situation 

        show sc girlscomedowng 007b
        with dissolve
        v"[y_name] has his reasons." 
        #She looks at the MC when she says this

        show sc girlscomedowng 010b
        v"Also... Look at what he has." 
        #we see the flash drive in his hands

        show sc girlscomedowng 011
        a"You got it!" 
        #Ariel is happy and surprised 

        show sc girlscomedowng 012
        mc"Yeah, and not a moment too soon!"
        #Ariel closed mouth

        show sc girlscomedowng 013
        b"Good. Now [mc_vic_address] might finally get off our cases." 
        #Bella is also relieved 

        show sc girlscomedowng 014
        b"Actually, where is he?"
        #Bella looks around

        show sc girlscomedowng 015d
        v"He um... He went out."
        #Vivian makes up an excuse

        show sc girlscomedowng 016b
        v"He said that he had to clear his head." 
        #a slightly different expression to the previous line

        show sc girlscomedowng 026b
        with dissolve
        mc"(The less the girls know about the arguments between [mc_v_address!c] and [mc_vic_address] the better.)"
        #We see the three girls while the MC is thinking
        show sc girlscomedowng 003
        a"How long have you been home?" 
        #reuse a render from above 
        show sc girlscomedowng 012
        mc"Only about five or so minutes." 
        #reuse a render from above 
        show sc girlscomedowng 006
        b"And what were the two of you discussing before we came down?"
        #Bella looks sceptical
        show sc girlscomedowng 018a
        with dissolve
        mc"Not much."
        #reuse a render from above
        show sc girlscomedowng 019b
        mc"[mc_v_address!c] just told me that I had to get the drive back by the morning." 
        #we see three girls as mc points to her #don't worry, it will be mc pov 

        show sc girlscomedowng 020b
        v"And you know what that means?" 
        #Vivian looks at the girls

        show sc girlscomedowng 021b
        a"We'll be having another [private_group] meeting?"
        #Ariel addresses Vivian
        show sc girlscomedowng 020b
        v"That's right." 
        #reuse a render from above
        v"So we should all head back upstairs and get a good night's rest." 
        #a slightly different render to the one above

        show sc girlscomedowng 023b
        b"Fine..." 
        #rolling eyes

        show sc girlscomedowng 024b
        b"Though it might be hard to get back to sleep now." 
        #same expression as above, different pose
        show sc girlscomedowng 020b
        v"Off you go girls. [y_name] and I will be up shortly."
        show sc girlscomedowng 025
        a"Night guys."
        #Show Bella heading up the stairs as Ariel (at the base of the stairs) turns to Viv and the MC to speak 

        show sc girlscomedowng 026b
        with dissolve
        mc"I'm gonna take a shower before I call it a night if that's okay?" 
        #just the MC and Vivian again now - Vivian stares at him while he speaks

        show sc girlscomedowng 027b
        v"Of course you can."
        #Vivian smiles and responds  

        show sc girlscomedowng 028b
        v"But just remember..." 
        #a different render to above, Vivian looks cautious

        show sc girlscomedowng 029b
        mc"I know, I know. Don't use too much water." 
        #reuse a render above
        mc"Goodnight, [mc_v_address!c]." 
        #Vivian has a slight smile

        show sc girlscomedowng 027b
        v"Night, sweetheart."
        #The MC heads up the stairs while Vivian watches him in the background 

        show sc girlscomedowng 030b
        with dissolve
        mc"(It's nice to come home and not get yelled at for a change.)"
        #the MC smirks

        show sc girlscomedowng 032
        with dissolve
        mc"(However, I could still be waking up to that in the morning..)"
        #the MC looks concerned 
        #(screen goes blank)"
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_02_03_The_late_chat_with_Bella
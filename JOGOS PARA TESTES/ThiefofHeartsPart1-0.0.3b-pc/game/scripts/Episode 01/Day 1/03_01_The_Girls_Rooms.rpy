init:
    $ v_ep01_01_bella_room = False
    $ v_ep01_01_ariel_room = False
    $ v_ep01_01_vivian_room = False

label lb_ep01_girls_rooms:
    $ quick_menu = True
    show screen toh_main_game_screen
    #scene continues with the MC in his room after taking a shower, and getting changed
    scene sc girlsrooms g01
    with dissolve
    mc"(What I'd give to have a shower that lasts longer than a few minutes.)"
    show sc girlsrooms g02
    mc"(But those are the rules,  \"conserve the water\".)"
    mc"(Hmm... What's going on in there?)"
    #the MC walks past Victor and Vivian's bedroom and overhears them talking"
    play music "sound effects/01/Hidden Conversations1.mp3" loop fadein 1.0
    show sc girlsrooms g03
    vic"I think I’ve made a grave error in judgment."
    #Vivian sits on the bed while Victor speaks and has his back turned away from her and with a glass of scotch in hand"
    show sc girlsrooms g04
    v"What do you mean?"
    show sc girlsrooms g05
    vic"[y_name] wasn't ready to lead a mission."
    show sc girlsrooms g06
    vic"That much is obvious."
    show sc girlsrooms g07
    vic"And I'm starting to believe that he never will be."
    show sc girlsrooms g08
    vic"He has the wrong attitude."
    #Victor drinks from his glass of scotch - make sure there's less in the glass after he has"
    show sc girlsrooms g09
    v"You're too harsh on him, [vic_name]."
    v"Clearly, he didn't make those mistakes on purpose."
    show sc girlsrooms g12
    vic"You know what your problem is, [v_name]?"
    show sc girlsrooms g13
    vic"You're too soft. On all three of them."
    vic"And you make me look weak."
    show sc girlsrooms g11
    v"That was never my intention."
    show sc girlsrooms g14
    vic"I'm trying to set us all up for that big payday and you constantly undermine my authority."
    show sc girlsrooms g13
    vic"You need to be a lot stricter. Otherwise, they're never going to learn and we're never going to get anywhere."
    show sc girlsrooms g12
    vic"And these kinds of errors like the ones [y_name] caused today, along with you over-coddling him, is what will eventually see all of us in the slammer."
    show sc girlsrooms g10
    vic"I honestly don't get you sometimes."
    show sc girlsrooms g14
    vic"You all don't respect me enough or appreciate what I've done for this [private_group]."
    #Vivian has her head down, copping the criticism"
    show sc girlsrooms g15
    v"I'll try harder, [vic_name]. And I'll make sure that the three of them do likewise."
    #victor finishes his glass of scotch and starts to make his way out the door"
    show sc girlsrooms g16
    v"Where are you going?"
    show sc girlsrooms g17
    vic"Downstairs to get some more scotch. And to watch some TV."
    show sc girlsrooms g08
    vic"I'm too agitated to sleep. Not that you can do anything to help me with that."
    #the MC still stands outside the door - Victor walks down the stairs and doesn't see him, heading in the opposite direction to where the MC is standing"
    #(Door closes sound effect)
    play sound "sound effects/01/Door Slam - sound effect.mp3"
    show sc girlsrooms g18
    mc"(He didn't see me, luckily.)"
    stop sound fadeout 1.0
    show sc girlsrooms g05
    mc"(Poor [mc_v_address]. She doesn't deserve that kind of treatment.)"
    show sc girlsrooms g19
    mc"(She deserves a hell of a lot better than him.)"
    show sc girlsrooms g07
    mc"(She's one of the most caring people that you're ever likely to meet.)"
    play sound "sound effects/01/door_creaking_open.mp3"
    show sc girlsrooms g25
    mc"(Hmm... Looks like the catch on that door is still broken.)"
    stop sound fadeout 1.0
    mc"(I don't get why [mc_vic_address] treats her like this, or acts like she's invisible.)"
    show sc girlsrooms g25b
    mc"(I mean, she's still pretty stunning for a woman her age.)"
    mc"(A goddess, some might say.)"
    mc"(If only she believed it.)"
    show sc girlsrooms g06
    mc"(I guess it doesn't help that she's with someone who isn't in any way supportive of her wants and needs, especially emotionally.)"
    show sc girlsrooms g05
    mc"(I can't help but feel responsible that [mc_vic_address] took his anger and frustrations out on her.)"
    show sc girlsrooms g07
    mc"(And this isn't the first time he's done it.)"
    show sc girlsrooms g04
    mc"(Life would be so much easier if he wasn't around.)"
    #the MC goes to the top of the stairwell and can see Victor on the sofa"
    show sc girlsrooms g05
    mc"(But it's not like he's just going to suddenly \"up and leave\".)"
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    #show Victor sitting in the living room watching TV in the dark with a glass of scotch in hand"
    show sc girlsrooms g20
    with dissolve
    "{i}To breaking news now...{/i}"
    show sc girlsrooms g26
    "{i}A man was discovered locked in an abandoned basement and was rescued by police after an anonymous tip.{/i}"
    "{i}But in a bizarre turn of events, shortly after being treated by ambulance staff, the man escaped from police custody.{/i}"
    "{i}We've been informed that he stole a car from a little old lady and he's likely to have fled the city.{/i}"
    show sc girlsrooms g27
    "{i}So far they have no leads to his exact whereabouts, but they believe that he has no fixed abode.{/i}"
    show sc girlsrooms g29
    "{i}He is a white Caucasion male in his mid to late 20s, around six feet tall, was last seen wearing a plain, grey t-shirt and is considered to be a person of interest.{/i}"
    show sc girlsrooms g26
    "{i}Please call crime stoppers if you have any information.{/i}"
    show sc girlsrooms g28
    vic"It sounds like this little asshole is just asking for trouble."
    vic"I wonder if {i}Kings County Nine-Nine{/i} is on?"
    show sc girlsrooms g20
    mc"(Well he won't be going to bed any time soon.)"
    show sc girlsrooms g21
    mc"(If I'm going to have a discussion with the girls about this new mission, I better do it now.)"
    mc"([a_name] would surely know something, given that she put that encrypted code on the drive.)"
    mc"(I'll find out what she knows...)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #show a hallway with three bedroom doors - Bella's (OS) room, Ariel's (YS) room and Vivian's room (main bedroom)
    #IMPORTANT: Make it possible to click on each of these girls' doors - the player can choose them in any order - All doors are closed"
    label lb_ep01_girls_rooms_01:
        scene sc girlsrooms g22
        with dissolve
        if v_ep01_01_ariel_room == False and v_ep01_01_bella_room == False and v_ep01_01_vivian_room == False:
            mc"(Who should I talk to first?)"

        if v_ep01_01_ariel_room == True and v_ep01_01_bella_room == True and v_ep01_01_vivian_room == True:
            show sc girlsrooms g22
            mc"(There's not much else I can do so it's time for me to call it a night...)"
            #screen goes blank"
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MCs_Room_1
        else:
            menu:
                "[a_name]" if v_ep01_01_ariel_room == False:
                    $ v_ep01_01_ariel_room = True
                    jump lb_ep01_Ariel_Room_1
                "[b_name]" if v_ep01_01_bella_room == False:
                    $ v_ep01_01_bella_room = True
                    jump lb_ep01_03_02_Bella_Room_1
                "[v_name]" if v_ep01_01_vivian_room == False:
                    $ v_ep01_01_vivian_room = True
                    jump lb_ep01_vivians_room_3


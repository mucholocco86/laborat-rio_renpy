label lb_ep01_The_MC_Investigates_the_gang:
    #The Scene begins with the MC sitting downstairs looking at the clock
    play ambient "sound effects/01/Alleyway_Ambience.ogg" loop fadein 1.0
    scene sc mcinvest i001
    with dissolve
    mc"(It's almost sundown, and Megan has sent me the location she wants me to check out.)"
    show sc mcinvest i002
    mc"(There's a lot on riding this.)"
    show sc mcinvest i003
    mc"(If it really is the hideout of the {i}Apex Legion{/i}, and that girl from the party is there, then all will be right in my world again.)"
    show sc mcinvest i004
    mc"(At least I think it will be.)"
    show sc mcinvest i005
    mc"(All right, time to go into town and to find this place...)"

    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The scene returns with the MC in the middle of an alleyway, among some warehouses and factories
    #Setting option - https://www.daz3d.com/the-alley
    scene sc mcinvest i006
    with dissolve
    mc"(Hmm... It's quiet.)"
    show sc mcinvest i007
    with dissolve
    mc"(This area has always been known as a dangerous part of town. Certainly not safe for someone by themselves.)"
    mc"(But I'm sure I'll be fine.)"
    mc"(Then again, I'd be more concerned if Megan wanted me to check this place out late at night.)"
    #The MC looks around
    show sc mcinvest i009
    with dissolve
    mc"(There doesn't seem to be anyone around. But I need to keep looking.)"
    show sc mcinvest i010
    mc"(What if this is a waste of time?)"
    show sc mcinvest i011
    mc"(What the hell am I going to do then?)"
    #The MC turns the corner
    show sc mcinvest i012
    mc"(Hang on a second...)"
    #The MC sees the back of the mystery girl, exactly like in this image but she'll be alone in an alley - she has a tattoo on her back - https://pixhost.to/show/173/451123815_image.png
    show sc mcinvest i014b
    mc"(Who is that?)"
    #Show a close-up of the tattoo
    show sc mcinvest i014
    with dissolve
    mc"(Oh shit! That's the same tattoo the girl at the party had!)"
    #The MC gets a bit closer
    show sc mcinvest i015
    mc"(I'm pretty sure it's her, but I need to know for sure.)"
    #The MC stands right behind her
    show sc mcinvest i014
    menu:
        "Approach her":
            show sc mcinvest i016
            with dissolve
    pause 1.0
    show sc mcinvest i017
    with dissolve
    pause 1.0
    show sc mcinvest i018
    with dissolve
    pause 1.0
    mc"Hey, you..."
    #Show someone's hand on the MC's shoulder
    show sc mcinvest i015a
    mc"I've been looking everywhere for you."
    show sc mcinvest i028
    "And so were we..."
    show sc mcinvest i019
    mc"(Huh?)"
    #The MC turns around and is knocked out by a guy who is part of the gang
    #screen shakes
    show sc mcinvest i027
    mc"(Oh shit!)"
    play sound "sound effects/01/Punch_Sound_Effect.mp3"
    show sc mcinvest i020
    with vpunch
    pause 1.0
    scene black
    with fast_dissolve
    play sound2 "sound effects/01/Falling Over Sound Effect.mp3"
    scene sc mcinvest i022
    with dissolve
    pause 1.0
    #The MC hits the ground and is out cold
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc mcinvest i021
    with dissolve
    guy"Take that, motherfucker!"
    #show a shot of the MC on the ground and the female's high heels standing next to his unconscious body
    show sc mcinvest i023
    with dissolve
    guy"What should we do with him?"
    #The woman replies but we never see her face
    show sc mcinvest i024
    woman"Take him inside, before someone sees him like this."
    woman"And do it quickly..."
    show sc mcinvest i025
    with dissolve
    pause 0.4
    show sc mcinvest i026
    with dissolve
    pause 0.4
    stop ambient fadeout 1.0
    #The final shot here is of the MC's face - eyes closed and unconscious
    #the screen slowly fades to black
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_review_end_01
    #END OF THE EPISODE 1




label lb_review_end_01:
    $ count_points("ariel")
    $ count_points("bella")
    $ count_points("vivian")
    $ count_points("megan")



    if v_ep01_ariel_aa_tasks_counter > 1:
        $ ariel_love_level +=2
    if v_ep01_ariel_aa_tasks_counter == 1:
        $ ariel_love_level +=1
    else:
        $ ariel_love_level +=0


    if v_ep01_bella_aa_tasks_counter > 1:
        $ bella_love_level +=2
    if v_ep01_bella_aa_tasks_counter == 1:
        $ bella_love_level +=1
    else:
        $ bella_love_level +=0

    if v_ep01_vivian_aa_tasks_counter > 1:
        $ vivian_love_level +=2
    if v_ep01_vivian_aa_tasks_counter == 1:
        $ vivian_love_level +=1
    else:
        $ vivian_love_level +=0



    if v_ep01_megan_aa_tasks_counter > 1:
        $ megan_love_level +=2
    if v_ep01_megan_aa_tasks_counter == 1:
        $ megan_love_level +=1
    else:
        $ megan_love_level +=0
    call screen toh_final_review_screen

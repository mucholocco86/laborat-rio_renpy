init:
    $ v_ep01_work_visit_options_1 = ""
    $ v_ep01_work_visit_options_2 = ""
    $ v_ep01_work_visit_options_3 = ""
    $ v_ep01_task02_girls_tattoo_counter = 0
    $ v_ep01_ariel_aa_tasks_counter = 0
    $ v_ep01_bella_aa_tasks_counter = 0
    $ v_ep01_vivian_aa_tasks_counter = 0
    $ v_ep01_megan_aa_tasks_counter = 0

    image sc mcroom wake up:
        "sc mcroom m01" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcroom m02" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcroom m01" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc mcroom m02" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc mcroom m01" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc mcroom m02" with Dissolve(0.2, alpha=True)

label lb_ep01_The_MCs_Room_1:
    #scene continues with the MC waking up the next day"
    scene black
    with dissolve
    pause 0.5
    "The next morning... {w=2.0}{nw}" with dissolve
    scene black
    play music "sound effects/01/Morning Light.mp3" loop fadein 1.0
    if persistent.v_anim_enabled:
        scene sc mcroom wake up
        with dissolve
        mc"Mmm..."
        mc"Huh?"
    else:
        scene sc mcroom m01
        with dissolve
        mc"Mmm..."
        show sc mcroom m01
        mc"Huh?"
    show sc mcroom m03
    mc"(What time is it?)"
    #the MC looks at his clock - it shows 09:00 am"
    show sc mcroom m04
    mc"(What the hell??)"
    mc"(I slept in!)"
    show sc mcroom m03
    mc"(Stupid alarm clock is broken again. It should have gone off two hours ago!)"
    play sound "sound effects/01/alarm_clock_button_press.ogg"
    #the MC gets up and sits on the side of the bed"
    show sc mcroom m05
    stop sound fadeout 1.0
    mc"(Dammit... Everyone has probably left and gone to work by now.)"
    mc"(I really need to speak to the girls before I start my shift later today.)"
    mc"(Especially [a_name], to see if she's found any handy information yet on that girl.)"
    $ task_addnew("Go and see "+a_name+" at her place of work",3)
    show sc mcroom m06
    mc"(The quicker I can find that girl from the party, the better my chances are of getting that flash drive back.)"
    mc"(First things first... I’ll have some breakfast, get changed and then head into town...)"
    stop music fadeout 1.0
    #screen goes blank"
    show black
    with dissolve
    pause 1.0
    centered "A little later on...{w=2.0}{nw}" with dissolve
    show text "A little later on..."
    scene bg black with Dissolve(1)
    pause 1.0
    #show the MC standing in the middle of town, in the main shopping district"
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    show sc mctown m01
    with dissolve
    mc"(The girls will all be at work, but seeing as it’s still early, they might not be too busy.)"
    show sc mctown m02
    mc"(So I should be able to at least have a short conversation with them.)"

    #IMPORTANT: Make it possible to click on either the RESTAURANT, the CLOTHING STORE and the COMPUTER SHOP"

    #NOTE: The player can choose any order for the three LI’s. The first two they choose will give them the chance to find the bonus scene.
    #They will need to come back to this point (before choosing any of them) to get the third

    #there’s a fancy restaurant, clothing shop and a computer shop all within close proximity of each other"

    mc"(Hmm... I have a few options here.)"
    show sc mctown m03
    mc"(I could visit [mc_v_address] at the restaurant. It wont be busy yet, so that should give us time to talk.)"
    show sc mctown m02
    mc"([b_name] is at the clothing store just down the road, but she could be busy.)"
    mc"(Or I could go and see [a_name] at the computer shop where she works.)"

    #TEMP MENU UNTIL INTERACTABLE MENU MADE
    menu:
        "Clothing Store ([b_name])"(wt="CHOOSE LAST"):
            #"If the player clicks on the CLOTHING STORE (scene with BELLA)"
            #mc"(I’ll go and visit [b_name] in the clothing store...)"
            $ v_ep01_work_visit_options_1 = "[b_name]"
            stop ambient fadeout 1.0
            scene black
            with dissolve
            pause 2.0
            jump lb_ep01_04_01_Bella_Work_1

        "Computer Shop ([a_name])"(wt="CHOOSE FIRST - The best order for these choices"):
            #"If the player clicks on the COMPUTER SHOP (scene with ARIEL)"
            #mc"(Now would be a good time to see [a_name] at the computer shop...)"
            $ v_ep01_work_visit_options_1 = "[a_name]"
            #the screen will go blank and take the player to the computer shop
            stop ambient fadeout 1.0
            scene black
            with dissolve
            pause 2.0
            jump lb_ep01_05_01_Ariel_Work_1

        "Restaurant ([v_name])"(wt="CHOOSE SECOND"):
            #"If the player clicks on the RESTAURANT (scene with Vivian)"
            #mc"(I’ll pop in to the restaurant to see if [v_name] is free to chat...)"
            $ v_ep01_work_visit_options_1 = "[v_name]"
            #the screen will go blank and take the player to the restaurant"
            stop ambient fadeout 1.0
            scene black
            with dissolve
            pause 2.0
            jump lb_ep01_06_01_Vivian_Work_1

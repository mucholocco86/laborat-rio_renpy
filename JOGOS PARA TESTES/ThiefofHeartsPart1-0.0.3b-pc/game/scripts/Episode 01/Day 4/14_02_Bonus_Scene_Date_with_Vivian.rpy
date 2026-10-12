default v_ep01_vivian_dates_counter = 0

label lb_ep01_Bonus_Scene_Date_with_Vivian1:
    #THIS SCENE WILL ONLY TRIGGER IF THE PLAYER CHOOSES "AGREE" DURING SCENE 06-01
    #scene begins back at the house, the MC in the hallway
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/01/Living Room Love1.mp3" loop fadein 1.0
    scene sc datewv v002
    with dissolve
    mc"(It's quiet...)"
    show sc datewv v003
    mc"(Hmm... Where is everybody?)"
    #The MC heads down the stairs and he sees Vivian in the living room sitting on the sofa
    show sc datewv v004
    mc"(Oh, [mc_v_address]'s here.)"
    mc"Hey..."
    show sc datewv v006
    v"Oh, you're still here."
    show sc datewv v005
    mc"Yeah."
    show sc datewv v007
    mc"Is anyone else around? Where's [mc_vic_address]?"
    #The MC is in the living room now
    show sc datewv v008
    v"He's at work."
    show sc datewv v009
    v"[b_name] will be back soon and then I think she said she's going out for a jog."
    show sc datewv v010
    v"[a_name] is doing the morning shift at the computer shop."
    v"So it's just you and me."
    show sc datewv v011
    v"What are your plans today?"
    show sc datewv v006
    mc"Oh, nothing much on until later."
    show sc datewv v010
    v"Do you have a lead on that flash drive?"
    show sc datewv v016
    mc"Yeah, I think so. I'm following up on it."
    show sc datewv v015
    v"That's great, sweetheart."
    show sc datewv v016
    v"Come, take a seat with me."
    show sc datewv v010
    v"Let's talk while we have this time together."
    #The MC sits next to Vivian
    show sc datewv v017
    with dissolve
    v"How are you feeling?"
    show sc datewv v026
    mc"What do you mean?"
    show sc datewv v019
    v"I'd imagine that you must have a lot going on in that head of yours lately."
    show sc datewv v020
    v"The crimes, working a job at the gym, trying to please [vic_name], helping me out with these tasks..."
    show sc datewv v021
    v"And also girls..."
    show sc datewv v022
    v"It must be rather frustrating for you, huh?"
    show sc datewv v018
    mc"Yeah, you don't know the half of it."
    show sc datewv v024
    v"Well, I want you to know that I'm here for you whenever you need to talk or for anything else."
    show sc datewv v025
    v"I'll always make time for you."
    show sc datewv v027
    mc"Thanks."
    #The MC places a hand on her thigh
    show sc datewv v028
    mc"What about you?"
    #Vivian smiles
    show sc datewv v029
    mc"How are you handling everything that's been going on?"
    show sc datewv v030
    v"I'm just taking things day by day."
    show sc datewv v031
    v"[b_name] and [a_name] barely have any time for me because they have to work."
    show sc datewv v025
    v"And whenever they're home, they just want to do their own thing."
    show sc datewv v024
    v"Which is why I'm so grateful that we've been able to spend some time together these past few days."
    #or v"Which is why I'm so thankful for the time we spent together these past few days."
    show sc datewv v021
    v"It means a lot to me."
    #Vivian looks at the MC in a loving way
    show sc datewv v040
    mc"Yeah, me too."

    #[Check out her chest / Look at her face / Look down]
    menu:
        "Check out her chest":
            show sc datewv v035
            mc"(Hmm... I think how she's dressed matches her mood.)"
            show sc datewv v033
            mc"(Happy and more \"free\" than usual.)"
            show sc datewv v034
            mc"(I'm certainly not against it.)"

        "Look at her face":
            show sc datewv v035
            mc"(It's always nice seeing her smile.)"
            show sc datewv v036
            mc"(I must have really made a good impression on her of late.)"

        "Look down"(wt="Best option"):
            show sc datewv v037
            mc"(Hmm... She doesn't normally wear these kinds of clothes around me.)"
            show sc datewv v038
            mc"(Or around the house.)"
            show sc datewv v039
            mc"(But I'm certainly not against it either.)"
            $ rewards_unlock ("vivian",10)

    #scene continues

    mc"So um..."
    show sc datewv v040
    mc"How are things between you and [mc_vic_address]?"
    show sc datewv v022
    v"Oh... You know what he can be like."
    show sc datewv v021
    v"He's been very busy, working long hours, sometimes all through the night."
    show sc datewv v020
    v"Lately there have been nights where I've gone to bed alone and found the spot next to me is empty when I wake up."
    show sc datewv v044
    mc"Oh, I'm sorry, [mc_v_address]."
    show sc datewv v027
    mc"I had no idea."
    show sc datewv v108
    v"It's okay, [y_name]. You weren't to know."
    show sc datewv v109
    v"As long as I have you here, that's enough for me."
    #Vivian hugs the MC
    show sc datewv v048
    v"Mmm..."
    v"My big, strong boy."
    show sc datewv v051
    v"You've grown up so quickly, where has the time gone?"
    #show Vivian's pressed up against the MC's chest
    show sc datewv v049
    mc"I have no idea."
    v"It's so nice to hug you like this. We don't do it nearly enough."
    show sc datewv v050
    mc"I'm also here for you whenever you need me."
    #they hug, look at each other
    show sc datewv v051
    v"Thank you, [y_name]."
    #the MC gives Vivian a closed-mouth kiss and still has a hand on her thigh
    #They break the hug and she looks down to see the MC has a reaction
    show sc datewv v110
    with vpunch
    v"(Oh my!)"
    #Vivian's eyes expand
    v"(He's hard!)"
    show sc datewv v054
    with dissolve
    v"(Surely that isn't because of me... Is it?)"
    #Vivian has some concern on her face
    mc"Are you okay?"
    #Vivian is still looking down
    show sc datewv v056
    v"Huh?"
    show sc datewv v057
    #And then she looks up at the MC, still a concerned look
    v"Oh, yeah, I'm fine."
    show sc datewv v058
    v"So um... I can make you some lunch. What would you like?"
    show sc datewv v059
    mc"You don't need to do that."
    show sc datewv v060
    mc"Besides, when we have lunch we're all meant to eat together, so we don't waste food, right?"
    show sc datewv v061
    v"I know, but you've earned this. And it can be our little secret."
    #She smiles
    show sc datewv v062
    v"Let me make you some warm apple pie."
    #Vivian stands up
    show sc datewv v063
    v"Wait right here while I get you some."
    #Vivian leaves and the MC watches her from behind
    show sc datewv v064
    mc"(Hmm... She's acting kind of strange.)"
    #The MC looks confused
    show sc datewv v065
    mc"(And I have no idea why-)"
    #The MC looks down at his crotch and sees that he's hard
    show sc datewv v066
    pause 1.0
    show sc datewv v067
    with vpunch
    mc"(Oh, shit!)"
    show sc datewv v068
    mc"(Could that be the reason?)"
    show sc datewv v069
    mc"(Is that why she suddenly left to make me something to eat?)"
    show sc datewv v070
    mc"(Dammit, I didn't even notice.)"
    show sc datewv v071
    mc"(When she comes back, it's best that I don't say anything about it, unless she says something first...)"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #the scene returns with Vivian holding a plate with a small warm apple pie
    play music "sound effects/01/Living Room Love2.mp3" loop fadein 1.0
    show sc datewv v072
    with dissolve
    pause 1.5
    show sc datewv v073
    with dissolve
    v"Here you are, my [mc_v_rel]."
    mc"Oh... This looks good, but I don't know if I should."
    show sc datewv v075
    v"You're right."
    #Vivian dips her finger into the pie and puts her index finger into her mouth
    show sc datewv v076
    v"It does look good."
    show sc datewv v077a
    v"Mmm..."
    #A close-up of Vivian's finger between her lips
    show sc datewv v077c
    mc"(Damn...)"
    mc"(She's really selling it.)"
    show sc datewv v076
    v"And it tastes even better."
    #Vivian holds it out for the MC
    show sc datewv v077
    v"Go on, try it."
    mc"Well... Okay."
    #The MC takes Vivian's finger in her mouth
    show sc datewv v111
    v"Mmm..."
    #The MC takes her finger out
    show sc datewv v075
    mc"(She's right, it smells great!)"
    #The MC looks at Vivian
    mc"(Same with the pie.)"
    show sc datewv v082
    v"So?"
    show sc datewv v081
    mc"I have to admit, it's really good."
    show sc datewv v084
    v"I told you."
    show sc datewv v085
    v"Now you stay right here while I go get a knife so I can cut you a slice."
    #Vivian stands up to leave
    show sc datewv v082
    v"After that, I'm going to do some laundry and then change the bedsheets before [a_name] and [b_name] get home."
    show sc datewv v078
    mc"Sure thing. And thanks again for the pie, [mc_v_address]."
    show sc datewv v063
    v"You're welcome, sweetheart."
    play sound "sound effects/01/mwah_short_kissing_sound_effect4.mp3"
    show sc datewv v092
    v"Mmm..."
    if v_ep01_06_01_Vivian_Work_Date == True:
        show sc datewv v112
        with dissolve
        pause 2.0
    show sc datewv v092
    with dissolve
    pause 0.1
    stop sound fadeout 1.0
    show sc datewv v093
    pause 1.0
    show sc datewv v094
    pause 1.0
    show sc datewv v095
    pause 1.0
    v"(Oh my! [y_name] and I just did {b}that{/b}!)"
    show sc datewv v058
    mc"(Oh! She just brushed her lips against mine.)"
    mc"(And I think she used a little bit of tongue!)"
    show sc datewv v061
    mc"(Did she do it on purpose, or was it purely an accident?)"
    show sc datewv v086
    with dissolve
    v"I look forward to spending more time together like this."
    #Vivian smiles
    show sc datewv v088
    mc"Yeah, so do I."
    show sc datewv v089
    v"Enjoy, sweetheart."
    mc"(If that was an accident, she's certainly not acting like it.)"
    show sc datewv v091
    with dissolve
    pause 1.5
    #Vivian leaves
    #screen goes blank
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ v_ep01_vivian_dates_counter += 1
    if v_ep01_04_01_Bella_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Bella1
    if v_ep01_05_01_Ariels_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Ariel1
    else:
        jump lb_ep01_The_MC_Investigates_the_gang

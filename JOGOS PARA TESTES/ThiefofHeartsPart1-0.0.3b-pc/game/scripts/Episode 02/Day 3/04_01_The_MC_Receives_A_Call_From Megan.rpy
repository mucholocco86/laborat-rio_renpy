init:
    $ v_ep02_04_01_megan_work_with_her = False


label lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan:
    #SCENE BEGINS
    centered "The next morning...{w=2.0}{nw}" with dissolve
    show text "The next morning..."
    scene bg black with Dissolve(1)
    pause 1.0
    #This comes up on the screen with a black background

    scene sc cliffhangerm 001
    with dissolve
    pause 2.0

    #Sound Effect - Eggs and Bacon cooking - optional
    #scene begins with the MC in the kitchen, making himself some breakfast

    #show the MC sipping some coffee while the TV is on in the background - sound effects for this
    #When she calls, the MC's reaction is all about the facial expressions
    show sc cliffhangerm 002
    with dissolve
    pause 1.0
    play sound "sound effects/01/Cell_Phone_Ring_Sound_Effect_-_reduced.mp3" loop
    if persistent.v_sounds_text_on == True:
        "(Phone ringing)"
    else:
        scene sc cliffhangerm 002
        pause 1.0

    show sc cliffhangerm 003
    with dissolve
    pause 1.0
    #the MC is startled by his phone ringing. It sits on the kitchen counter

    show sc cliffhangerm 005
    with dissolve
    pause 1.0
    stop sound fadeout 1.0

    show sc cliffhangerm 006
    with dissolve
    #He has a calm look on his face
    mc"Hello?"

    show sc cliffhangerm 007
    megan"Good morning, [y_name]."
    #Show Megan in her house, wearing casual attire - she's not in her bikini yet

    show sc cliffhangerm 008
    megan"How are you?"
    show sc cliffhangerm 009
    mc"I'm fine. You?"
    #the MC gives a half-hearted response

    show sc cliffhangerm 010
    megan"I'm terrific!"

    show sc cliffhangerm 012
    with dissolve
    megan"Sorry I haven't been in touch. I had a few things to take care of."
    megan"But otherwise, everything is just fine."

    show sc cliffhangerm 013
    mc"And what about the other night? You're pretending like nothing happened!"
    #Show Megan with her mouth closed, surprised by the MCs tone

    show sc cliffhangerm 013
    mc"With your so called 'ears to the ground' and all that?"

    show sc cliffhangerm 014
    mc"You're aware of what happened, aren't you?"

    show sc cliffhangerm 015
    megan"Oh..."
    #she looks down, open mouth, concerned

    show sc cliffhangerm 016
    mc"Is that it?"

    show sc cliffhangerm 017
    mc"I had my lights punched out and all you can say is, \"Oh\"??"

    show sc cliffhangerm 018
    megan"Look, I'm sorry, I didn't mean for that to happen."
    #she's more stern with her reply

    show sc cliffhangerm 019
    megan"But if you just let me explain then I-"

    show sc cliffhangerm 020
    mc"No Megan, I'm done talking."

    show sc cliffhangerm 021
    mc"I barely got out alive and the only reason I was there in the first place is because I listened to you!"

    show sc cliffhangerm 022
    mc"So I'm hanging up this phone. We are {b}done{/b}."
    #the MC prepares to hang up on her

    show sc cliffhangerm 023
    megan"Did you get your flash drive back?"

    show sc cliffhangerm 024
    mc"Well, yeah, I did."
    #His expression changes

    show sc cliffhangerm 025
    mc"But that's beside the point!"
    #he goes back to being angry with her

    show sc cliffhangerm 026
    megan"True, but without me, you wouldn't have it back, right?"

    show sc cliffhangerm 027
    mc"That's true, I guess."

    show sc cliffhangerm 028
    megan"Look [y_name], can we please talk about this in person?"

    show sc cliffhangerm 029
    megan"I'd much rather apologise to you face to face and also because I..."

    show sc cliffhangerm 030
    megan"I need your help."

    megan"It's one of my reasons for calling you."

    show sc cliffhangerm 031
    mc"My help? My help with what?"

    show sc cliffhangerm 032
    #far-shot
    megan"Again, it would be best if you could come and see me."
    show sc cliffhangerm 042
    #close-shot
    megan"Are you able to visit my house this morning?"

    #[Rudely response / Agree]
    menu:
        "Rude response":
            show sc cliffhangerm 031
            mc"Well, it's my day off."

            show sc cliffhangerm 034
            mc"And quite frankly, there are plenty of better things I would rather be doing on a warm, sunny day."
            show sc cliffhangerm 036
            mc"So no, I'll pass..."

            show sc cliffhangerm 037
            megan"I suggest you come and see me young man, as it's vitally important."
            #Megan shows an authoritative face

            show sc cliffhangerm 038
            megan"Otherwise, I'll have to send two of my guys to come pick you up, and drag you over here if they have to."
            #or
            #megan"Otherwise, I'll send two of my guys to drag you back here.  Kicking and screaming if needed."

            show sc cliffhangerm 038
            megan"And honestly, I'd rather not do that."

            show sc cliffhangerm 039
            mc"(Shit. This does sound serious.)"

            show sc cliffhangerm 040
            mc"All right, fine."
            #the MC is not happy

            show sc cliffhangerm 041
            mc"I'll be there in half an hour."

            show sc cliffhangerm 042
            megan"I shall see you then."
            show sc cliffhangerm 043
            megan"Bye..."
            #the call ends
            #the MC sips his coffee and he looks like he's in a bad mood
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #Go Down to scene continues

        "Agree"(wt="Best option"):
            show sc cliffhangerm 016
            mc"Well, it {b}is{/b} my day off, but fine. I'll come see you."
            show sc cliffhangerm 017
            mc"I'll be there in half an hour."
            show sc cliffhangerm 042
            megan"I shall see you then."
            show sc cliffhangerm 043
            megan"Bye..."
            #the call ends
            #the MC sips his coffee and looks conflicted about his choice
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)


    #scene continues
    play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
    show sc cliffhangerm 046
    with dissolve
    pause 1.5
    #Show the MC riding his bike heading towards the front of Megan's house

    show sc cliffhangerm 047
    with dissolve
    pause 1.5
    #show the MC pulling up near the front and getting off his bike

    show sc cliffhangerm 048
    with dissolve
    pause 1.5
    #show the MC with the two bodyguards at the front of Megan's house
    mc"Okay, okay..."

    show sc cliffhangerm 049
    mc"I have nothing to hide, guys."

    show sc cliffhangerm 050
    security"Just standard pro-"

    show sc cliffhangerm 051
    mc"Standard procedure. I know, I know."
    pause 1.5
    #the security pats him down

    show sc cliffhangerm 052
    with dissolve
    security"He's clean."

    show sc cliffhangerm 053
    mc"So, can I see Megan now?"

    show sc cliffhangerm 054
    security"Yes, but not through here."
    show sc cliffhangerm 055
    security"Go around the side of the house to the back and head towards the pool area."
    #or
    # security"Go around back to the pool."

    show sc cliffhangerm 056
    security"Miss Megan is expecting you."

    show sc cliffhangerm 057
    with dissolve
    pause 1.0
    mc"Sure..."
    show sc cliffhangerm 058
    with dissolve
    pause 1.0
    show sc cliffhangerm 059
    with dissolve
    pause 1.0
    #the MC starts walking around the house. Show 2-3 images of him until he gets to the back of the house

    show sc cliffhangerm 060
    with dissolve
    pause 1.0
    #he will see the pool area at the back of the house and some deck chairs, and umbrellas - https://staticg.sportskeeda.com/editor/2023/01/69e55-16742251976622-1920.jpg

    #SETTING - https://www.daz3d.com/luxury-pool-house-and-garden

    show sc cliffhangerm 061
    with dissolve
    mc"Woah..."

    show sc cliffhangerm 062
    mc"{i}(*Whispering*){/i}\nThis pool is incredible."

    show sc cliffhangerm 063
    mc"{i}(*Whispering*){/i}\nIf only I brought my swimming trunks with me."

    show sc cliffhangerm 064
    niles"Something to drink, Sir?"
    #Niles pops up behind the MC, surprising him, just like this scene -
    #https://pixhost.to/show/255/499926354_screenshot-2024-08-01-at-11-13-06-pm.jpg - https://pixhost.to/show/255/499926356_screenshot-2024-08-01-at-11-13-11-pm.jpg

    #screen shakes
    show sc cliffhangerm 065
    with vpunch
    pause 1.0

    show sc cliffhangerm 066
    mc"What the shit!?"
    #the MC puts a hand to his chest as he turns around and sees Littamen, Megan's butler behind him

    show sc cliffhangerm 067
    mc"Dude, you gotta stop doing that!"

    show sc cliffhangerm 068
    with dissolve
    niles"My apologies, young Sir."
    #or
    #niles"My apologies, young sir."

    show sc cliffhangerm 069
    niles"Sometimes I find ways to amuse myself."
    #Niles has a funny smirk on his face

    show sc cliffhangerm 070
    mc"Yeah, I'll bet."

    show sc cliffhangerm 071
    mc"Is Megan around?"

    show sc cliffhangerm 072
    niles"Miss Megan will be with you shortly."

    show sc cliffhangerm 073
    niles"She's currently attending to some important business."

    show sc cliffhangerm 074
    niles"Can I interest you in a light refreshment?"

    show sc cliffhangerm 075
    mc"Nah, I'm good."

    show sc cliffhangerm 076
    niles"In that case, please take a seat."

    show sc cliffhangerm 077
    mc"Can do..."
    #Niles walks away while the MC sits on one of the deck chairs
    show sc cliffhangerm 078
    with dissolve
    pause 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    centered "Moments later...{w=2.0}{nw}" with dissolve
    show text "Moments later..."
    scene bg black with Dissolve(1)
    pause 1.0
    #This comes up on the screen with a black background

    show sc cliffhangerm 079
    with dissolve
    megan"Well, hello there, [y_name]."
    #megan calls the MC while he's daydreaming

    show sc cliffhangerm 080
    mc"{i}(*Whispering*){/i}\nOh damn..."
    #the MC turns to see Megan in a bikini
    #examples - https://i.redd.it/vkzkv4h5rb481.gif - https://images.squarespace-cdn.com/content/v1/5d436dd21aad2f0001e00fc4/1585042933643-GY9UN2JEG2EQIIJ5XCF7/201+KC+marg.gif?format=1500w

    #ROLLING IMAGE OF MEGAN IN HER BIKINI AND HEELS
    #IMPORTANT - make sure to change Megan's poses during her conversation with the MC here
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc cliffhangerm 081 at tt_top
        pause
    elif True:
        scene sc cliffhangerm 082

    scene sc cliffhangerm 082
    with dissolve
    megan"Sorry for making you wait. I had something that urgently required my attention."

    scene sc cliffhangerm 083
    megan"But I'm all yours now."

    show sc cliffhangerm 084
    megan"Thank you for coming."

    show sc cliffhangerm 086
    with dissolve
    mc"Well, you did leave me with very little choice."
    #Show two of Megan's security guys loitering in the background
    show sc cliffhangerm 087
    mc"And your guys in those candy-ass monkey suits back there have been eye-balling me like a fat guy at the buffet."

    show sc cliffhangerm 091
    with dissolve
    megan"They take their jobs very seriously. Sorry if you feel uncomfortable."
    show sc cliffhangerm 094
    mc"Nah, it's cool."
    show sc cliffhangerm 086
    mc"I'm curious though. What was so urgent that you needed me to come all the way to your house."
    show sc cliffhangerm 096
    megan"Well, I'll get right to the point."
    show sc cliffhangerm 088
    megan"Does this mean anything to you?"
    #Megan shows the MC her phone
    #Alternate idea, Hyper: Megan is being blackmailed and MC and needs someone "outside" her surroundings
    #who she can trust to investigate further. Let me know if we should go with this idea instead.
    show sc cliffhangerm 089
    mc"{i}You'll get yours bitch. You better watch your back{/i}."
    #he takes it from her and reads it
    show sc cliffhangerm 090
    mc"Hmm... No, I can't say that it does."
    #He hands her phone back to her

    show sc cliffhangerm 088
    with dissolve
    megan"Have you told anyone about our relationship?"

    show sc cliffhangerm 092
    mc"Our relationship?"
    #the MC looks confused

    show sc cliffhangerm 091
    megan"Yes, our work relationship. How we know each other."

    show sc cliffhangerm 094
    mc"No, not a soul."

    show sc cliffhangerm 095
    mc"Sorry, but what does this message have to do with me."

    show sc cliffhangerm 096
    megan"Someone is trying to bring me and my business down."

    show sc cliffhangerm 097
    megan"I'm almost certain of that."

    show sc cliffhangerm 098
    megan"At first, I thought it was something you told the gang who captured you the other day."

    show sc cliffhangerm 099
    megan"I can't trust anyone, and I'm starting to think even some of my own people are conspiring against me."

    show sc cliffhangerm 100
    megan"Which is why I need you."

    show sc cliffhangerm 101
    mc"What do you need me for?"

    show sc cliffhangerm 102
    megan"You're someone I can trust. Someone who I can rely on."
    #or
    #megan"I see you as someone I can trust and rely on."

    show sc cliffhangerm 103
    megan"A person who I can confide in."

    show sc cliffhangerm 104
    mc"Why would you trust me? We hardly know each other."

    show sc cliffhangerm 105
    megan"True... But despite what happened the other night, you never gave up my name when you were captured and interrogated."

    show sc cliffhangerm 106
    megan"Even to the girl who you stole your flash drive back from."

    show sc cliffhangerm 107
    megan"Or, I assume, even anyone in your own [private_group]."
    show sc cliffhangerm 108
    megan"Am I right?"

    show sc cliffhangerm 109
    mc"No, I haven't."

    show sc cliffhangerm 110
    megan"You know, you and I aren't so different, [y_name]."

    show sc cliffhangerm 111
    megan"We're both striving for something bigger, better.  We're also focused and always watching our backs."

    megan"We're looking out for number one, first and foremost."

    show sc cliffhangerm 112
    megan"You remind me a lot of myself when I was younger."

    show sc cliffhangerm 113
    megan"Ambitious... determined... wanting to be the best at what you do."
    #She gives him a sexy seductive look

    show sc cliffhangerm 114
    mc"Yes, that's all very true."

    show sc cliffhangerm 115
    megan"So... [y_name]."
    show sc cliffhangerm 105
    megan"Can I trust you?"

    show sc cliffhangerm 117
    megan"And will you help me to figure out who is trying to destroy me and my business?"
    show sc cliffhangerm 105
    #[Refuse / Agree]

    menu:
        "Refuse":
            show sc cliffhangerm 118
            mc"I'm sorry, Megan."

            show sc cliffhangerm 119
            mc"I'm sure you mean well, but your enemies and your business dealings are none of my concern."

            show sc cliffhangerm 120
            mc"After what happened the other night, I really don't have any interest in being your gopher again."

            show sc cliffhangerm 122
            mc"So if there's nothing else, then I'll be on my way."
            #the MC turns to leave

            show sc cliffhangerm 123
            mc"Goodbye, and good luck."
            pause 1.0
            #Megan looks has a smirk on her face

            show sc cliffhangerm 137
            with dissolve
            mc"Uh-oh..."

            show sc cliffhangerm 125
            with dissolve
            megan"I think you'll find that refusal to comply is not an option."

            #The MC turns to find two of her security guys blocking his leave
            stop ambient fadeout 1.0
            stop sound fadeout 1.0
            play music "sound effects/01/Episode1_final_scene.mp3" fadein 2.5
            show sc cliffhangerm 126
            mc"Oh, shit..."
            pause 3.0
            #Show the MC looking up at the two security guys with Megan in the background.
            show sc cliffhangerm 127
            with dissolve
            pause 4.0
            #Her arms are folded and she has a devilish smile on her face
            pause 2.0
            with slow_dissolve
            stop music fadeout 10.0
            scene black
            with Pause (10)
            with slow_dissolve
            jump lb_review_end_02
            #This comes up on the screen
            #Exit music to start playing here
            #END OF UPDATE



        "Agree"(wt="Best option"):
            $ v_ep02_04_01_megan_work_with_her = True
            show sc cliffhangerm 128
            mc"Fine, I'll work with you on this."

            show sc cliffhangerm 129
            mc"But I'm not real sure where to start."

            show sc cliffhangerm 130
            megan"You can start by using your own contacts I know you have."

            show sc cliffhangerm 131
            megan"And I'd recommend talking to the people you work with."

            show sc cliffhangerm 132
            megan"You're a smart boy. I'm sure you'll figure something out."

            show sc cliffhangerm 133
            mc"(Hmm... I could ask [a_name] for help. Maybe she can figure out who Megan's possible enemies are.)"

            show sc cliffhangerm 134
            mc"I'll see what I can do."

            show sc cliffhangerm 135
            megan"Now that's what I like to hear."
            #She smiles
            show sc cliffhangerm 136
            megan"Guys, can you leave us to talk in private, please?"
            #Megan addresses her two security guys

            show sc cliffhangerm 137
            security"Yes, ma'am."

            show sc cliffhangerm 138
            megan"Thank you..."
            #The security guys leave

            show sc cliffhangerm 131
            with dissolve
            megan"Now finally, we are alone."

            show sc cliffhangerm 139
            megan"I want to properly apologise for what happened the other night."

            #Megan sits on a deck chair opposite the MC and crosses her legs
            #ROLLING IMAGE OF MEGAN IN HER BIKINI AND HEELS
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                scene sc cliffhangerm 085a at tt_top
                pause
            elif True:
                scene sc cliffhangerm 085
                with dissolve
                pause 1.0

            scene sc cliffhangerm 140
            megan"I pride myself on taking {b}very{/b} good care of my assets."
            #she smiles as she moves towards him

            show sc cliffhangerm 141
            megan"Especially young men like yourself."

            show sc cliffhangerm 142
            mc"Oh yeah... And what does that normally include?"
            mc"This... \"apology\" of yours?"

            show sc cliffhangerm 143
            with dissolve
            megan"If you stick around long enough, you might just find out."
            pause 1.5
            #she presses the palm of her hand against his chest
            stop ambient fadeout 1.0
            play music "sound effects/01/Episode1_final_scene.mp3" fadein 2.5
            show sc cliffhangerm 144
            with dissolve
            pause 2.0
            #Megan presses her body against the MC and slides her hand down towards his crotch
            show sc cliffhangerm 145
            with dissolve
            mc"(OH!!)"
            pause 2.0
            with slow_dissolve
            stop music fadeout 10.0
            scene black
            with Pause (10)
            with slow_dissolve
            jump lb_review_end_02
            #This comes up on the screen
            #Exit music to start playing here
            #END OF UPDATE



label lb_review_end_02:
    $ count_points("ariel")
    $ count_points("bella")
    $ count_points("vivian")
    $ count_points("megan")
    $ count_points("juliet")
    $ count_points("zora")
    $ v_review_episode = 2
    call screen toh_final_review_screen

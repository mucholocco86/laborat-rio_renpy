init:
    image anim_ep02_juliet_nc_boobs_close1 = Movie(channel="anim_ep02_juliet_nc_boobs_close1", play="images/extras/Episode 02/anim_ep02_juliet_nc_boobs_close1.webm")
    image anim_ep02_juliet_nc_boobs1 = Movie(channel="anim_ep02_juliet_nc_boobs1", play="images/extras/Episode 02/anim_ep02_juliet_nc_boobs1.webm")
    image anim_ep02_juliet_nc_jerkoff_close1 = Movie(channel="anim_ep02_juliet_nc_jerkoff_close1", play="images/extras/Episode 02/anim_ep02_juliet_nc_jerkoff_close1.webm")
    image anim_ep02_juliet_nc_jerkoff1 = Movie(channel="anim_ep02_juliet_nc_jerkoff", play="images/extras/Episode 02/anim_ep02_juliet_nc_jerkoff1.webm")
    image anim_ep02_juliet_nc_masturbating_close1 = Movie(channel="anim_ep02_juliet_nc_masturbating_close1", play="images/extras/Episode 02/anim_ep02_juliet_nc_masturbating_close1.webm")
    image anim_ep02_juliet_nc_masturbating1 = Movie(channel="anim_ep02_juliet_nc_masturbating1", play="images/extras/Episode 02/anim_ep02_juliet_nc_masturbating1.webm")

    $ v_ep02_03_08_fitness_session_with_juliet_counter = 0
    $ v_ep01_juliet_respect_counter = 0
    $ v_ep01_juliet_cocky_counter = 0
    $ v_ep01_juliet_arrogant_counter = 0
    $ v_ep02_03_08_fitness_session_with_juliet_fight = False
    $ v_ep02_03_08_fitness_session_with_juliet_fight_win = False
    $ v_ep02_juliet_fantasy_counter = 0
    $ v_ep02_task11_juliet_fitness_session = 0
    $ v_ep02_ariel_aa_tasks_counter = 0
    $ v_ep02_juliet_aa_tasks_counter = 0

label lb_ep02_03_08_The_MCs_private_session_with_Juliet:

    #Images sc julietgym j008 to sc julietgym j019 here
    play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
    show sc julietgym j011
    with dissolve
    ju"[y_name]?"
    $ task_addnew("Fitness session with Juliet",11)
    #Juliet calls the MC who turns his gaze towards her - https://pixhost.to/show/146/498732419_screenshot-2024-07-28-at-10-47-58-am.jpg
    show sc julietgym j010
    mc"Oh, hello again."
    $ task_addfuturetask("",2,notify=False)
    $ juliet_known = True
    $ persistent.juliet_gallery_unlocked = True
    #ROLLING WIP OF JULIET
    #Options here for the MC to react to Juliet's choice of attire - still make sure her back is mostly covered

    #[Compliment her / Get on with the session]
    menu:
        "Compliment her":
            show sc julietgym j012
            mc"Sweet outfit if you don't mind me saying."
            $ v_ep01_juliet_arrogant_counter += 1
            show sc julietgym j014
            ju"I know."
            show sc julietgym j015
            ju"But enough of the chit-chat."
            ju"Let's get down to business."
            show sc julietgym j016
            mc"Works for me."

        "Get on with the session"(wt="Best option"):
            show sc julietgym j012
            mc"All right, let's get down to business."
            $ v_ep01_juliet_respect_counter += 1
            show sc julietgym j015
            ju"Works for me."
            $ v_ep02_03_08_fitness_session_with_juliet_counter += 1
            #+1 JULIET POINT


    #scene continues
    show sc julietgym j014
    ju"Hey... Did you get in a fight recently?"
    show sc julietgym j016
    mc"Um... No, why do you ask?"
    show sc julietgym j015
    ju"Your right cheek looks a little redder than the last time we spoke."
    show sc julietgym j016
    mc"Goddamnit, is it still that obvious?"
    show sc julietgym j015
    ju"What happened?"

    #[Make up and excuse / Exaggerate / Say very little]
    menu:
        "Make up an excuse":
            show sc julietgym j016
            mc"I slipped in the shower and bumped it against the glass."
            show sc julietgym j019
            mc"It's fine."
            #The MC looks away from Juliet when he replies
            show sc julietgym j014
            ju"Okay, now that's a lie."
            show sc julietgym j016
            mc"What do you mean?"
            $ v_ep01_juliet_arrogant_counter += 1
            show sc julietgym j015
            ju"You looked away when you responded."
            show sc julietgym j014
            ju"So you can tell me the truth, or don't tell me."
            ju"Either way, I'll know if you're lying or not."

        "Exaggerate"(wt="Best option + Task Point"):
            show sc julietgym j016
            mc"I went to watch an ice hockey match last night and rather than a fight taking place on the ice, it took place in the stands."
            show sc julietgym j015
            ju"Seriously?"
            #She looks at him sceptically
            show sc julietgym j013
            mc"Yeah, the guy caught me a good one during the first period, I'm not gonna lie."
            $ v_ep02_task11_juliet_fitness_session += 1
            show sc julietgym j017
            mc"But by the end of the game he had as many teeth as a duck!"
            $ v_ep01_juliet_cocky_counter += 1
            show sc julietgym j018
            ju"Haha! If you say so."
            $ v_ep02_03_08_fitness_session_with_juliet_counter += 1
            #she laughs
            #+1 JULIET POINT

        "Say very little":
            show sc julietgym j019
            mc"It's nothing."
            show sc julietgym j015
            ju"Fine, don't tell me."
            show sc julietgym j014
            ju"We all have our secrets, I guess this is one of yours."

    #scene continues
    show sc julietgym j019
    mc"Uh, let's move on..."
    show sc julietgym j016
    mc"We'll start with some stretches, just to limber up before we get into the hard stuff."
    show sc julietgym j013
    mc"Just follow my lead."
    show sc julietgym j014
    ju"Actually, I know how I want to warm up."
    show sc julietgym j015
    ju"Feel free to join me or just watch. I don't care either way."
    #Juliet reacts, doesn't need his advice or for him to lead, and shows her experience and authority
    show sc julietgym j016
    mc"Err... Okay."
    #a montage of images of Juliet and the MC doing the same stretches alongside each other
    #Images sc julietgym j020 to sc julietgym j029 here

    #Image #1 - https://s3.amazonaws.com/prod.skimble/assets/34401/skimble-workout-trainer-exercise-windmills-1_iphone.jpg
    #Image #2 - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpumyPIZmhFtPf-6YhX0xsLmGjG1zDhzoIDqXAT1TV-ekVuppy8ITcq3nY6rfG1vlzBB8&usqp=CAU
    #Image #3 - https://img.freepik.com/premium-photo/fitness-team-stretching-arms-workout-exercise-training-together-with-smile-gym-active-people-sports-class-warm-up-stretch-arm-body-balance-healthy-wellness_590464-106600.jpg
    #Image #4 - https://media.istockphoto.com/id/1214302429/photo/sporty-couple-doing-stretching-exercises-at-gym.jpg?s=612x612&w=is&k=20&c=wPU2aK4_oI4Pd_-Pf-4jVpZ5zba-tKSD_hLWMmFq9JU=
    #Image #5 - https://us.123rf.com/450wm/georgerudy/georgerudy1705/georgerudy170500086/77194196-beautiful-young-sports-couple-is-stretching-after-workout-in-gym.jpg
    #Image #6 - https://pixhost.to/show/124/498391687_screenshot-2024-07-27-at-12-05-05-pm.jpg
    play music "sound effects/02/Stretch and Move2.mp3" loop fadein 1.0
    show sc julietgym j020
    with dissolve
    pause 1.5
    show sc julietgym j021
    with dissolve
    pause 1.5
    show sc julietgym j022
    with dissolve
    pause 1.5
    show sc julietgym j023
    with dissolve
    pause 1.5
    show sc julietgym j024
    with dissolve
    pause 1.5
    show sc julietgym j025
    with dissolve
    pause 1.5
    show sc julietgym j026
    with dissolve
    pause 1.5
    show sc julietgym j027
    with dissolve
    pause 1.5
    show sc julietgym j028
    with dissolve
    pause 1.5
    show sc julietgym j029
    with dissolve
    pause 1.5
    scene black
    with dissolve
    scene black
    with Pause (2)

    show sc julietgym j011
    with dissolve
    ju"All right, that's enough warming up."
    show sc julietgym j012
    mc"So what are you doing first?"
    #Juliet chooses first
    show sc julietgym j011
    ju"I'm gonna start off by using the butterfly machine."
    show sc julietgym j010
    mc"Alrighty then..."
    #the MC looks confused, as he's not sure what he's meant to do
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #scene returns with Juliet using the butterfly machine - https://pixhost.to/show/157/498847362_001.png -
    #https://www.youtube.com/watch?v=WpVu2duHnQE




    #Images sc julietgym j040 to sc julietgym j046 here
    #show 2-3 different angles and views of Juliet using the butterfly machine
    show sc julietgym j040
    with dissolve
    pause 1.5
    show sc julietgym j041
    with dissolve
    pause 1.5
    show sc julietgym j042
    with dissolve
    pause 1.5
    show sc julietgym j040
    with dissolve
    pause 1.5
    show sc julietgym j041
    with dissolve
    pause 1.5
    show sc julietgym j042
    with dissolve
    pause 1.5

    show sc julietgym j044
    with dissolve
    mc"Someone looks determined."
    mc"If you pull any harder you could strain something."
    #the MC looks concerned
    show sc julietgym j043
    ju"I'm sure you would know all about that, huh?"
    #Juliet gives the MC a devilish smirk back
    show sc julietgym j045
    mc"Oooh... That was below the belt. Try to keep the gloves up."
    #Juliet smirks at the MC's light banter
    #show 2 more different angles and views of Juliet lifting weights for the player to click through
    show sc julietgym j042
    with dissolve
    pause 1.0
    show sc julietgym j041
    with dissolve
    pause 1.0
    #screen goes blank
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    show sc julietgym j013
    with dissolve
    mc"Okay, so what are you going to do now?"
    show sc julietgym j014
    ju"How about you decide for me this time?"
    show sc julietgym j017
    mc"Really?"
    mc"Um... Okay."


    #[Weights / Leg press]
    #NOTE: The player can only choose one of these options
    menu:
        "Weights"(wt="Bonus image"):
            show sc julietgym j013
            mc"I'll get you to work with some weights next."
            show sc julietgym j014
            ju"Sounds fine by me..."
            #she looks unfazed
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #Images sc julietgym j030 to sc julietgym j035 here
            #Juliet lifting weights like this - https://pixhost.to/show/123/498385157_010.png

            #show 2-3 different angles and views of Juliet lifting weights for the player to click through

            #if you're going to show the MC, then try not to show his face
            #example - if he's standing behind her, then show up until his neck
            play music "sound effects/02/Stretch and Move1.mp3" loop fadein 1.0
            show sc julietgym j030
            with dissolve
            pause 1.5
            show sc julietgym j031
            with dissolve
            pause 1.5
            show sc julietgym j032
            with dissolve
            pause 1.5
            show sc julietgym j033
            with dissolve
            mc"That's it. Keep your back straight."
            $ rewards_unlock ("juliet",1)
            show sc julietgym j035
            mc"Engage your core and stick your chest out slightly."
            show sc julietgym j034
            ju"How about you let me just do my workout and you stick to being my spotter?"
            #Juliet sticks out her chest and shows the MC some extra cleavage
            show sc julietgym j033
            mc"Uh... Okay.."

            #show 2 more different angles and views of Juliet lifting weights for the player to click through
            show sc julietgym j030
            with dissolve
            pause 1.5
            show sc julietgym j031
            with dissolve
            pause 1.5
            show sc julietgym j032
            with dissolve
            pause 1.5
            show sc julietgym j030
            with dissolve
            pause 1.5
            show sc julietgym j031
            with dissolve
            pause 1.5
            show sc julietgym j032
            with dissolve
            pause 1.5


            #once the five views are shown, the remaining option will come up here
            show sc julietgym j034
            with dissolve
            ju"Okay, I think I'm done here..."
            #screen goes blank
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            #Go Down To > #scene continues



        "Leg press"(wt="Bonus image + Task Point"):
            show sc julietgym j013
            mc"I'll get you to work on the leg press machine."
            show sc julietgym j014
            ju"Sounds fine by me..."
            #she looks unfazed
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            #scene returns with Juliet using the leg press -
            #https://media.post.rvohealth.io/wp-content/uploads/sites/2/2022/04/GRT-01.01.HorizontalSeatedLegPress.gif
            #Images sc julietgym j036 to sc julietgym j039, and #Images sc julietgym j049 to sc julietgym j052 here

            #show 2-3 different angles and views of Juliet pushing weights with her feet for the player to click through
            play music "sound effects/02/Stretch and Move1.mp3" loop fadein 1.0
            show sc julietgym j036
            with dissolve
            pause 1.5
            show sc julietgym j037
            with dissolve
            pause 1.5
            show sc julietgym j038
            with dissolve
            pause 1.5
            show sc julietgym j037
            with dissolve
            mc"That's it. Quick on the push, and ease on down when bending your knees."
            mc"And don't forget to take deep breaths."
            $ rewards_unlock ("juliet",2)
            show sc julietgym j039
            ju"How about you let me just do my workout and you stick to being my spotter?"
            #Juliet sticks out her chest and shows the MC some extra cleavage
            show sc julietgym j036
            mc"Uh... Okay.."
            #show 2 more different angles and views of Juliet pushing weights with her feet for the player to click through

            show sc julietgym j036
            with dissolve
            pause 1.5
            show sc julietgym j037
            with dissolve
            pause 1.5
            show sc julietgym j038
            with dissolve
            pause 1.5
            show sc julietgym j037
            with dissolve
            pause 1.5
            #once the five views are shown, the remaining option will come up here
            show sc julietgym j050
            with dissolve
            ju"Okay, I think I'm done here..."
            $ v_ep02_task11_juliet_fitness_session += 1
            #screen goes blank
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            #Go Down To > #scene continues

    #scene continues

    #Images sc julietgym j053 to sc julietgym j059 here
    show sc julietgym j053
    with dissolve
    mc"Nice form, Juliet."
    show sc julietgym j054
    mc"Are you sure you even need my help?"
    mc"Most exercises like the ones you have done since you got here don't even need a spotter."
    show sc julietgym j055
    with dissolve
    ju"Is it not your job to help and watch over your clients?"
    #Juliet continues to exercise without looking at the MC
    show sc julietgym j054
    with dissolve
    mc"Well yeah, it is my job, but it looks like you could teach yourself."
    show sc julietgym j061
    with dissolve
    ju"I bet I could teach you a thing or two."
    #Juliet gets cocky
    show sc julietgym j056
    mc"Seeing as you're such an expert, do you have anything special in mind?"
    #MC shoots back at her
    show sc julietgym j059
    ju"I'm sure I have moves that you've never seen before."
    show sc julietgym j056
    mc"Yeah, I can't wait to see those."
    #the MC replies in a sarcastic, disrespectful way
    #Juliet shoots the MC a snide look
    show sc julietgym j062
    with dissolve
    ju"You know, you're not as tough as you seem."
    show sc julietgym j062a
    mc"Oh yeah? Well, you're not as badass as you think you are!"
    show sc julietgym j063
    ju"Is that right?"
    #She stands up and looks at her hands
    show sc julietgym j066
    ju"Are you willing to back up that mouth of yours?"
    #then looks up at him
    show sc julietgym j062b
    mc"What are you suggesting?"
    show sc julietgym j067
    ju"You, and me... We duke it out."
    show sc julietgym j072
    mc"What? Right here in the gym?"
    show sc julietgym j064
    ju"Do you have somewhere else we can do this, away from all these people?"
    show sc julietgym j072
    mc"Sure, but, what are we doing exactly?"
    show sc julietgym j063
    ju"Take me to a quieter place in this gym and then we can discuss all that."
    show sc julietgym j070
    ju"Unless of course, you're chicken?"
    show sc julietgym j071
    mc"By the time I'm through with you, you'll be the one laying eggs."
    show sc julietgym j069
    with dissolve
    mc"Follow me..."
    stop ambient fadeout 1.0
    #the MC walks away with a cocky smile on his face while Juliet watches him, pissed off
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the scene continues with the MC and Juliet in a quiet room within the gym
    #It has soft padded mats on the floor like for what wrestlers use - https://www.daz3d.com/fm-home-wrestling
    show sc julietwrestling j001
    with dissolve
    show screen scr_secret_icon("v_secrets_ep02_03_08_1") onlayer ontop
    with { "ontop": dissolve}
    mc"All right, we're here where no one will bother us."
    show sc julietwrestling j002
    mc"So how are we going to settle this?"
    show sc julietwrestling j003
    ju"Get on the mat first, and then I'll explain."
    show sc julietwrestling j004
    mc"UGHH... Fine."
    #the MC is getting frustrated with her
    #the MC and Juliet stand on the mat
    show sc julietwrestling j005
    with dissolve
    show screen scr_secret_hotspot ("sc julietwrestling j005","932,11,129,268","v_secrets_ep02_03_08_1")
    show sc julietwrestling j005
    ju"So... Do you know how to wrestle?"
    hide screen scr_secret_hotspot
    show sc julietwrestling j007
    mc"So that's it?"
    show sc julietwrestling j008
    mc"We wrestle each other and the first one to tap out loses?"
    show sc julietwrestling j009
    ju"That's one part of it."
    show sc julietwrestling j010
    ju"But mix that with any form of fighting, and then we have our challenge."
    show sc julietwrestling j011
    ju"So what do you say?"
    show sc julietwrestling j012
    ju"Are you in, or are you out?"
    show sc julietwrestling j013
    mc"You want to fight and wrestle me at the same time?"
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    #[Leave / Agree]
    menu:
        "Leave":
            show sc julietwrestling j014
            mc"No, this is pointless."
            show sc julietwrestling j015
            mc"If we get caught doing this, then I could lose my job."
            show sc julietwrestling j024
            mc"But any other time or place, and I'm in."
            $ v_ep01_juliet_respect_counter += 1
            show sc julietwrestling j017
            ju"Yeah, we'll see about that."
            show sc julietwrestling j018
            ju"Fine, if your job means that much to you, then we won't fight... today."
            show sc julietwrestling j019
            ju"I'm going to finish off the session, alone."
            show sc julietwrestling j017
            ju"I'll see you before I leave."
            #Juliet leaves the room
            #the MC looks confused, scratches his head
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            #Go To FINAL SCENE
            jump lb_ep02_03_08_The_MCs_private_session_with_Juliet_final

        "Agree"(wt="Best option + 2 Task Points"):
            #Video examples of what I'd like to see here: https://mega.nz/folder/EdtSVTSQ#oZVIxuo1QX11grbOHFL6Cg
            show sc julietwrestling j009
            mc"(Time to put this cocky bitch back in her place.)"
            show sc julietwrestling j013
            mc"Okay, I'm in."
            $ v_ep02_03_08_fitness_session_with_juliet_fight = True
            $ v_ep01_juliet_cocky_counter += 1
            show sc julietwrestling j025
            ju"Excellent..."
            $ v_ep02_03_08_fitness_session_with_juliet_counter += 2
            #+2 JULIET POINT
            $ v_ep02_task11_juliet_fitness_session += 2
            show sc julietwrestling j026
            mc"So when do we start?"
            show sc julietwrestling j027
            ju"We can start...right..."
            play music "sound effects/02/The Final Round.mp3" loop fadein 0.1
            play sound "sound effects/02/punch_and_miss1.mp3" noloop
            show sc julietwrestling j028
            with vpunch
            ju"Now!"
            show sc julietwrestling j029
            with faster_dissolve
            pause 1.0
            #Juliet takes a swing at the MC which he evades
            play sound "sound effects/02/punch_and_miss2.mp3" noloop
            show sc julietwrestling j030
            with faster_dissolve
            mc"(Woah!)"
            show sc julietwrestling j031
            with faster_dissolve
            pause 1.0
            #Juliet takes a second swing at the MC with her other hand and he also evades it to you
            play sound "sound effects/02/punch_to_the_gut.mp3" noloop
            show sc julietwrestling j032
            with vpunch
            mc"Geezus!"
            #Juliet takes a third swing at the MC and she hits him in the gut with vpunch
            show sc julietwrestling j033
            with vpunch
            mc"UHH!"
            #he bends over after taking the hit
            show sc julietwrestling j034
            with faster_dissolve
            mc"Haha... You hit like a girl."
            #the MC looks up at her and laughs while he is hunched over
            show sc julietwrestling j035
            ju"Oh, no you didn't!"
            ju"Hi-ya!"
            show sc julietwrestling j036
            with fast_dissolve
            #Juliet swings her knee at his head
            play sound "sound effects/02/blocking_a_punch.mp3" noloop
            show sc julietwrestling j037
            with vpunch
            pause 0.5
            ju"NGHH!"
            #As his head is lowered, he blocks her knee
            show sc julietwrestling j038
            with faster_dissolve
            mc"So much aggression."
            #he's still calm and composed, cocky with his words
            show sc julietwrestling j039
            with faster_dissolve
            pause 0.6
            show sc julietwrestling j039a
            with faster_dissolve
            pause 0.6
            play sound "sound effects/02/falling_over.mp3" noloop
            show sc julietwrestling j040
            with vpunch
            ju"Oh!!"
            #The MC grabs her knees and pushes Juliet to the mat
            show sc julietwrestling j041
            with faster_dissolve
            pause 0.6
            play sound "sound effects/02/punch_and_miss3.mp3" noloop
            show sc julietwrestling j042
            with faster_dissolve
            with fast_dissolve
            play sound "sound effects/02/blocking_a_punch1.mp3" noloop
            show sc julietwrestling j043
            with faster_dissolve
            mc"But for what purpose?"
            #Juliet gets back up and continues to attack the MC but he calmly blocks everything she throws at him
            play sound "sound effects/02/kicking_out.mp3" noloop
            show sc julietwrestling j044
            with fast_dissolve
            with vpunch
            ju"Huff!"
            #she takes a swing and misses
            show sc julietwrestling j045
            with faster_dissolve
            mc"You're fast, but not fast enough."
            #The MC has a cocky grin
            play sound "sound effects/02/punch_and_miss3.mp3" noloop
            show sc julietwrestling j046
            with faster_dissolve
            ju"Grr!"
            show sc julietwrestling j046a
            with faster_dissolve
            pause 0.6
            show sc julietwrestling j046b
            with faster_dissolve
            pause 0.6
            play sound "sound effects/02/blocking_a_punch1.mp3" noloop
            show sc julietwrestling j047
            with vpunch
            pause 0.6
            show sc julietwrestling j047a
            with faster_dissolve
            pause 0.6
            #Juliet looks up at the MC from the canvas, with an angry face
            #a series of right and left punches thrown by Juliet that the MC blocks
            #Sound effects for each block
            #Right-Left-Right-Left-Right - make them run one after the other without the need for clicking
            #when Juliet throws her final right punch, the MC grabs it and throws her past him
            #She stays on her feet, but their positions have changed on the mat
            show sc julietwrestling j048
            with faster_dissolve
            pause 0.6
            show sc julietwrestling j049
            with faster_dissolve
            mc"You caught me with a lucky shot, but no more, Juliet."
            show sc julietwrestling j050
            mc"There's no shame in conceding defeat."
            #She runs at the MC to attack him, and her combination punches begin again
            #a series of right and left punches and kicks by Juliet attack the MC which he blocks
            #Sound effects for each block
            show sc julietwrestling j051
            ju"NEVER!!"
            play sound "sound effects/02/punch_and_miss1.mp3" noloop
            show sc julietwrestling j052
            with faster_dissolve
            pause 0.8
            play sound "sound effects/02/blocking_a_punch1.mp3" noloop
            show sc julietwrestling j053
            with faster_dissolve
            with vpunch
            pause 0.8
            play sound "sound effects/02/blocking_a_punch1.mp3" noloop
            show sc julietwrestling j054
            with faster_dissolve
            with vpunch
            pause 0.8
            play sound "sound effects/02/blocking_a_punch1.mp3" noloop
            show sc julietwrestling j055a
            with vpunch
            pause 0.5
            mc"All right, it's time to end this."
            show sc julietwrestling j056
            with faster_dissolve
            pause 0.8
            show sc julietwrestling j056a
            with faster_dissolve
            pause 0.8
            show sc julietwrestling j057
            with faster_dissolve
            pause 0.8
            play sound "sound effects/02/flip_and_land.mp3" noloop
            show sc julietwrestling j058
            with vpunch
            pause 0.8
            show sc julietwrestling j107
            with faster_dissolve
            pause 0.8
            #The MC anticipates her punch, grabs her arm and turns her around, holding Juliet in a bear hug
            #He pulls her to the ground. The MC kneels behind her, holding her arms so she can't move
            #She sits in front of him on the mat, a pained expression on her face
            show sc julietwrestling j059
            with faster_dissolve
            pause 0.8
            mc"Besides, it looks like you've had enough."
            #The MC holds her tightly, thinking he has control over the situation
            show sc julietwrestling j060
            ju"Not a chance in hell!"
            #she angrily replies
            show sc julietwrestling j061
            with faster_dissolve
            mc"Well, from where I'm positioned right now, you don't have any options left."
            show sc julietwrestling j062
            with faster_dissolve
            mc"So I suggest that you stop resisting and tap out already."


            #[Look at her chest / Look at her thighs / Stay focused]
            menu:
                "Look at her chest"(wt="Best option + Task Point"):
                    show sc julietwrestling j063
                    with faster_dissolve
                    mc"{i}(*Whispering*){/i}\nVery nice..."
                    show sc julietwrestling j064
                    with faster_dissolve
                    pause 1.0
                    show sc julietwrestling j065
                    with faster_dissolve
                    pause 1.0
                    $ rewards_unlock ("juliet",3)
                    #The MC stares at Juliet's chest
                    #show 2-3 other angles of Juliet's cleavage for the player to click through
                    show sc julietwrestling j066
                    with faster_dissolve
                    mc"You might be really strong, know your way around gym equipment and have a fit as fuck body..."
                    show sc julietwrestling j067
                    mc"But you're simply no match for-"
                    #show these next images one after the other as Juliet gains control when the MC lets his guard down
                    show sc julietwrestling j068
                    with faster_dissolve
                    pause 1.0
                    #First image - show Juliet moving her arms back and wrapping them around the MC's head and/or shoulders
                    show sc julietwrestling j069
                    with faster_dissolve
                    pause 1.0
                    #Second image of Juliet flipping the MC upside down and over her head
                    play sound "sound effects/02/flip_and_land.mp3" noloop
                    show sc julietwrestling j070
                    with vpunch
                    mc"What the-?"
                    #Final image - The MC lands on his back and onto the soft mat.
                    #screen shakes
                    #Juliet wraps her thighs around the MC - like this scene from Lethal Weapon - https://youtu.be/Jg-kfatZAOE?si=wGYntgH2lD2pYjOa&t=199
                    show sc julietwrestling j072
                    with faster_dissolve
                    mc"(Oh crap!)"
                    show sc julietwrestling j073
                    ju"Now I've got you right where I want you, [y_name]."
                    #expand the shot of Juliet's thighs/legs wrapped around the MC who looks like he's struggling
                    show sc julietwrestling j074
                    mc"Mfmfmfmf!!"
                    #the MC is struggling for air
                    show sc julietwrestling j075
                    with faster_dissolve
                    mc"I uh... uh... ..."
                    #the MC passes out and the screen fades to black
                    #screen goes blank
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    centered "Several minutes later...{w=2.0}{nw}" with dissolve
                    show text "Several minutes later..."
                    scene bg black with Dissolve(1)
                    pause 0.6
                    #start with these words on a black screen
                    #Juliet calls out to the MC
                    show sc julietwrestling j076
                    with dissolve
                    ju"[y_name]??"
                    show sc julietwrestling j077
                    with dissolve
                    ju"[y_name]? Are you okay?"
                    show sc julietwrestling j078
                    mc"{i}(*Murmurs*){/i}\nOh yeah, you're French, aren't you...? Just like that."
                    show sc julietwrestling j080
                    with dissolve
                    pause 0.6
                    mc"Um... Was I just talking in my sleep?"
                    show sc julietwrestling j077
                    ju"Yeah, you were."
                    show sc julietwrestling j081
                    mc"What the hell happened?"
                    show sc julietwrestling j079
                    ju"You passed out."
                    show sc julietwrestling j080
                    mc"I did?"
                    show sc julietwrestling j081
                    mc"But how?"
                    show sc julietwrestling j082
                    ju"I had you in a strangle hold."
                    #the MC looks confused
                    show sc julietwrestling j084
                    ju"You passed out within a few seconds. Sorry."
                    show sc julietwrestling j085
                    ju"I've also taken a few judo classes."
                    show sc julietwrestling j086
                    mc"Of course you have."
                    #The MC seems unsurprised by that
                    show sc julietwrestling j087
                    ju"Here, you need to get back up on your feet."
                    #Juliet helps the MC to his feet
                    show sc julietwrestling j088
                    with dissolve
                    ju"Are you all right?"
                    show sc julietwrestling j089
                    with dissolve
                    mc"Yeah, I'm fine."
                    show sc julietwrestling j090
                    ju"You know, after what I did to that asshole who you kicked out of your gym last week, I expected you to think more of me."
                    show sc julietwrestling j091
                    mc"Well, if I didn't before, I do now."
                    show sc julietwrestling j092
                    ju"Don't doubt me ever again..."
                    #Juliet leans in close like she's going to kiss the MC
                    #+1 JULIET POINT
                    $ v_ep02_03_08_fitness_session_with_juliet_counter += 1
                    show sc julietwrestling j093
                    ju"Otherwise, I'm going to have to show you some of the many other skills I've learned."
                    show sc julietwrestling j094
                    ju"And it will be a far more bruising experience for you next time."
                    #she backs off
                    show sc julietwrestling j095
                    mc"I know not to ever take you lightly in the future."
                    show sc julietwrestling j096
                    mc"So I guess you win then."
                    show sc julietwrestling j097
                    ju"Yeah, I suppose I did."
                    show sc julietwrestling j095
                    mc"But you know that I'll want a re-match soon though, yeah?"
                    show sc julietwrestling j099
                    ju"I look forward to having my way with you again. Haha!"
                    $ v_ep02_task11_juliet_fitness_session += 1
                    #She smiles
                    show sc julietwrestling j100
                    ju"Anyway, I'm going to cool down with some light stretches while I give you some time to recover."
                    show sc julietwrestling j101
                    mc"I'll speak with you when you're finished..."
                    #Juliet leaves the room

                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #GO DOWN TO > FINAL SCENE

                "Look at her thighs"(wt="Best option + Task Point"):
                    show sc julietwrestling j102
                    with dissolve
                    pause 1.0
                    mc"{i}(*Whispering*){/i}\nVery nice..."
                    #The MC stares at Juliet's stomach and between her legs
                    #show 2-3 other angles of Juliet's thighs and stomach for the player to click through
                    show sc julietwrestling j103
                    with dissolve
                    pause 1.0
                    show sc julietwrestling j104
                    with dissolve
                    pause 1.0
                    show sc julietwrestling j105
                    with dissolve
                    pause 1.0
                    show sc julietwrestling j106
                    with dissolve
                    mc"You might be really strong, know your way around gym equipment and have a fit as fuck body..."
                    show sc julietwrestling j067
                    mc"But you're simply no match for-"
                    #show these next images one after the other as Juliet gains control when the MC lets his guard down
                    show sc julietwrestling j068
                    with dissolve
                    pause 0.6
                    #First image - show Juliet moving her arms back and wrapping them around the MC's head and/or shoulders
                    show sc julietwrestling j069
                    with dissolve
                    pause 0.6
                    #Second image of Juliet flipping the MC upside down and over her head
                    play sound "sound effects/02/flip_and_land.mp3" noloop
                    show sc julietwrestling j070
                    with vpunch
                    mc"Oh shit!!"
                    #Final image - The MC lands on his back and onto the soft mat.
                    #screen shakes
                    #Juliet wraps her thighs around the MC - like this scene from Lethal Weapon - https://youtu.be/Jg-kfatZAOE?si=wGYntgH2lD2pYjOa&t=199
                    show sc julietwrestling j072
                    with dissolve
                    mc"(Oh crap!)"
                    show sc julietwrestling j073
                    ju"Now I got you right where I want you, [y_name]."
                    #expand the shot of Juliet's thighs/legs wrapped around the MC who looks like he's struggling
                    show sc julietwrestling j074
                    mc"Mfmfmfmf!!"
                    #the MC is struggling for air
                    show sc julietwrestling j075
                    with dissolve
                    mc"I uh... uh... ..."
                    stop music fadeout 1.0
                    #the MC passes out and the screen fades to black
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    centered "Several minutes later...{w=2.0}{nw}" with dissolve
                    show text "Several minutes later..."
                    scene bg black with Dissolve(1)
                    pause 0.6
                    #start with these words on a black screen
                    #Juliet calls out to the MC
                    show sc julietwrestling j076
                    with dissolve
                    ju"[y_name]??"
                    show sc julietwrestling j077
                    with dissolve
                    ju"[y_name]? Are you okay?"
                    #the MC's eyes flutter open and he sees Juliet looking down at him
                    show sc julietwrestling j078
                    mc"{i}(*Murmurs*){/i}\nOh yeah, you're French, aren't you...? Just like that."
                    show sc julietwrestling j080
                    with dissolve
                    pause 0.6
                    mc"Um... Was I just talking in my sleep?"
                    show sc julietwrestling j077
                    ju"Yeah, you were."
                    show sc julietwrestling j081
                    mc"What the hell happened?"
                    show sc julietwrestling j079
                    ju"You passed out."
                    show sc julietwrestling j080
                    mc"I did?"
                    show sc julietwrestling j081
                    mc"But how?"
                    show sc julietwrestling j082
                    ju"I had you in a strangle hold."
                    #the MC looks confused
                    show sc julietwrestling j084
                    ju"You passed out within a few seconds. Sorry."
                    show sc julietwrestling j085
                    ju"I've also taken a few judo classes."
                    show sc julietwrestling j086
                    mc"Of course you have."
                    #The MC seems unsurprised by that
                    show sc julietwrestling j087
                    ju"Here, you need to get back up on your feet."
                    #Juliet helps the MC to his feet
                    show sc julietwrestling j088
                    with dissolve
                    ju"Are you all right?"
                    show sc julietwrestling j089
                    with dissolve
                    mc"Yeah, I'm fine."
                    show sc julietwrestling j090
                    ju"You know, after what I did to that asshole who you kicked out of your gym last week, I expected you to think more of me."
                    show sc julietwrestling j091
                    mc"Well, if I didn't before, I do now."
                    show sc julietwrestling j092
                    ju"Don't doubt me ever again..."
                    #Juliet leans in close like she's going to kiss the MC
                    #+1 JULIET POINT
                    $ v_ep02_03_08_fitness_session_with_juliet_counter += 1
                    show sc julietwrestling j093
                    ju"Otherwise, I'm going to have to show you some of the many other skills I've learned."
                    show sc julietwrestling j094
                    ju"And it will be a far more bruising experience for you next time."
                    #she backs off
                    show sc julietwrestling j095
                    mc"I know not to ever take you lightly in the future."
                    show sc julietwrestling j096
                    mc"So I guess you win then."
                    show sc julietwrestling j097
                    ju"Yeah, I suppose I did."
                    show sc julietwrestling j095
                    mc"But you know that I'll want a re-match soon though, yeah?"
                    show sc julietwrestling j099
                    ju"I look forward to having my way with you again. Haha!"
                    $ v_ep02_task11_juliet_fitness_session += 1
                    #She smiles
                    show sc julietwrestling j100
                    ju"Anyway, I'm going to cool down with some light stretches while I give you some time to recover."
                    show sc julietwrestling j101
                    mc"I'll speak with you at the end of your session..."
                    #Juliet leaves the room

                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #GO DOWN TO > FINAL SCENE

                "Stay focused"(wt="Bonus Image"):
                    $ v_ep02_03_08_fitness_session_with_juliet_fight_win = True
                    #The MC continues to hold her tightly
                    show sc julietwrestling j107
                    with dissolve
                    ju"UGHH!"
                    show sc julietwrestling j108
                    ju"All right. You win."
                    show sc julietwrestling j109
                    mc"Make it official."
                    $ rewards_unlock ("juliet",4)
                    #Juliet reluctantly taps the mat on the floor
                    play sound "sound effects/02/tapping_out.mp3" noloop
                    if persistent.v_sounds_text_on == True:
                        "(Tap, tap!)"
                    else:
                        show sc julietwrestling j063b
                        pause 0.1
                        show sc julietwrestling j063a
                        pause 0.1
                        show sc julietwrestling j063b
                        pause 0.1
                        show sc julietwrestling j063a
                        pause 0.1
                        show sc julietwrestling j063b
                        pause 0.5
                    #Tapping sound
                    #The MC lets her go
                    show sc julietwrestling j110
                    with dissolve
                    ju"Uhh!"
                    stop music fadeout 3.0
                    #she takes a gasp of air
                    show sc julietwrestling j111
                    mc"Are you good?"
                    #The MC stands up and looks down at her
                    show sc julietwrestling j112
                    ju"Yeah, I'm fine."
                    show sc julietwrestling j113
                    mc"There's no shame in finishing second, Juliet."
                    show sc julietwrestling j114a
                    mc"I'd imagine that's quite rare for you."
                    #The MC is being cheeky here which doesn't impress her
                    show sc julietwrestling j115
                    ju"Yeah, yeah. You just got lucky."
                    show sc julietwrestling j116
                    mc"Or perhaps, experience simply won out in the end."
                    show sc julietwrestling j117
                    ju"Care for a re-match sometime soon?"
                    show sc julietwrestling j118
                    mc"Sure, why not."
                    show sc julietwrestling j119
                    mc"Here, let me help you up."
                    #the MC helps Juliet to his feet
                    show sc julietwrestling j120
                    with dissolve
                    ju"So I'm gonna go and cool down with some light stretches if you don't mind."
                    show sc julietwrestling j121
                    mc"Sure thing."
                    show sc julietwrestling j122
                    mc"I'll speak with you at the end of your session..."
                    #Juliet leaves the room

                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)


    #FINAL SCENE

    # show sc julietwrestling j123
    # with dissolve
    # mc"So um, it looks like our time is up."
    # #the MC and Juliet are back on the mat again
    # show sc julietwrestling j124
    # mc"How would you rate our session together?"
    # show sc julietwrestling j125
    # ju"It was okay. I've had better."
    # show sc julietwrestling j126
    # ju"But seeing as this was our first time, I'd be willing to have another one with you at the very least."
    # show sc julietwrestling j127
    # mc"Cool..."
    # show sc julietwrestling j127a
    # mc"Perhaps we can work on some other things next time."
    # show sc julietwrestling j128
    # ju"Sure."
    # if v_ep02_03_08_fitness_session_with_juliet_counter == 5:
    #     $ juliet_love_level +=1
    # show sc julietwrestling j129
    # ju"Anyway, I'm just going to get changed and then I'll be out of your hair."
    # show sc julietwrestling j130
    # mc"No problem."
    # show sc julietwrestling j130a
    # mc"You'll need to sign out before you leave."
    # show sc julietwrestling j020
    # ju"I know the drill."
    # show sc julietwrestling j021
    # ju"See you shortly."
    # show sc julietwrestling j022
    # mc"(Damn...)"
    # #screen goes blank
    # scene black
    # with dissolve
    # scene black
    # with Pause (2)

    # #scene returns with the MC looking at Juliet while she prepares to leave
    # play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    # show sc julietwrestling j132
    # with dissolve
    # ju"Okay, I'm all signed out."
    # show sc julietwrestling j133
    # mc"Thanks."
    # show sc julietwrestling j134
    # mc"Shall I book you in for another session?"
    # show sc julietwrestling j135
    # ju"I'll call you."
    # show sc julietwrestling j136
    # ju"There's a few things I need to take care of first. Finding a job for starters."
    # show sc julietwrestling j137
    # mc"I'd be happy to help you out with that."
    # show sc julietwrestling j138
    # ju"Thanks, but I've got this."
    # show sc julietwrestling j139
    # ju"However, having a gym to call home is definitely a priority. So I'll be in touch."
    # show sc julietwrestling j140
    # ju"Thanks for your time today."
    # show sc julietwrestling j132
    # mc"It was my pleasure."
    # show sc julietwrestling j142
    # ju"Bye, [y_name]..."
    # stop ambient fadeout 1.0
    # #final shot of Juliet leaving the gym
    # #screen goes blank
    # scene black
    # with dissolve
    # scene black
    # with Pause (2)

    # #GO TO > #"Zora" (if the player has not had a session with Zora yet - continue with ZORA SECOND lines)
    # #or
    # #"The MC finishes his shift" (if the player has done sessions with both girls)
    # #GO TO > Ep 2 Scene 03-07
    # #screen goes blank
    # scene black
    # with dissolve
    # scene black
    # with Pause (2)


    show sc julietwrestling j123
    with dissolve
    mc"So it looks like our time is up."
    #the MC and Juliet are back on the mat again
    show sc julietwrestling j124
    mc"How would you rate our session together?"
    show sc julietwrestling j125
    ju"I must admit, it was pretty good for our first time."
    show sc julietwrestling j126
    ju"I'd certainly be willing to have another session with you. Maybe more."
    #Juliet smiles without seeming overly excited
    if v_ep02_03_08_fitness_session_with_juliet_counter >= 4:
        $ juliet_love_level +=1
        show sc julietwrestling j127
        mc"Sweet!"
        show sc julietwrestling j127a
        mc"Perhaps we can work on some other things next time."
        show sc julietwrestling j144
        ju"I'm looking forward to what you come up with."
        show sc julietwrestling j129
        ju"Anyway, I'm just going to get changed and then I'll be out of your hair."
        show sc julietwrestling j130
        mc"No problem."
        show sc julietwrestling j130a
        mc"You'll need to sign out before you leave."
        show sc julietwrestling j145
        ju"I know the drill."
        #Juliet gives the MC a sexy look before she walks away
        show sc julietwrestling j143
        ju"See you shortly, [y_name]."
        #The MC watches Juliet walk away and toward the changing room
        #When she gets to the women's changing room, she looks at the MC, gives a smile and then disappears in there.
    else:
        show sc julietwrestling j128
        ju"Sure."
        show sc julietwrestling j129
        ju"Anyway, I'm just going to get changed and then I'll be out of your hair."
        show sc julietwrestling j130
        mc"No problem."
        show sc julietwrestling j130a
        mc"You'll need to sign out before you leave."
        show sc julietwrestling j020
        ju"I know the drill."
        show sc julietwrestling j021
        ju"See you shortly."
        show sc julietwrestling j022
        mc"(Damn...)"
    show sc julietwrestling j146
    with dissolve
    pause 1.0
    if persistent.v_secrets_enabled and persistent.v_secrets_ep02_03_08_1:
        menu:
            "Follow her"(wt="Best option"):
                jump lb_ep02_03_08_The_MCs_private_session_with_Juliet_fantasy
            "Don't follow her":
                pause 0.01
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_08_The_MCs_private_session_with_Juliet_final

label lb_ep02_03_08_The_MCs_private_session_with_Juliet_fantasy:
    ###START OF THE NON-CANON SCENE
    if not _in_replay:
        scene img_secret_scene_overlay onlayer anim_layer
        with { "anim_layer": dissolve}
    else:
        show screen scr_end_replay
    #the MC stands just inside the women's changing room
    #the MC looks around the corner
    play music "sound effects/01/Temptation1.mp3" loop fadein 1.0
    show sc julietwrestling j147
    with flash(0.25, 0, 0.75, "#fff")
    with dissolve
    pause 2.0
    show sc julietwrestling j148
    with dissolve
    pause 2.0
    show sc zoragym z181
    with vpunch
    mc"(Oh!!)"
    show sc julietwrestling j148b
    with dissolve
    pause 0.6
    show sc julietwrestling j149
    with dissolve
    pause 0.6
    #ROLLING SCREEN OF JULIET IN HER UNDERWEAR
    show sc julietwrestling j150
    with dissolve
    pause 1.0
    show sc julietwrestling j151
    with dissolve
    pause 1.0
    show sc julietwrestling j152
    with dissolve
    pause 1.0

    #he sees her just as Juliet starts changing - she shows her front
    #show images of Juliet changing out of her clothes, and bending over, almost like she's posing for the MC
    #she never makes eye contact with him
    #do not show her from behind
    #ROLLING SCREEN OF JULIET FROM HER FRONT WITH HER UNDERWEAR ON AND TOPLESS

    #IMAGE - when she removes her underwear, she turns to her side so we can't see her pussy
    show sc julietwrestling j153
    with dissolve
    mc"{i}(*Whispering*){/i}\nOh God..."
    #IMAGE - Juliet raises her hands above her head and has her eyes closed - we still can't see her pussy
    show sc julietwrestling j154
    with dissolve
    mc"(I better get out of here.)"
    show sc julietwrestling j156
    with dissolve
    pause 1.0
    show sc julietwrestling j155
    with dissolve
    pause 1.0
    #the MC turns to leave, and Juliet calls out to him
    show sc julietwrestling j165
    with dissolve
    ju"Leaving so soon?"
    show sc julietwrestling j168
    with dissolve
    mc"(Oh fuck! She knows that I was spying on her!!)"
    #the MC looks stunned, and then turns back to face her
    show sc julietwrestling j166
    with dissolve
    ju"You know... I couldn't help but get a bit excited by the way we fought and tangled our bodies together."
    #Juliet speaks to the MC by looking at his reflection in the mirror
    show sc julietwrestling j167
    with dissolve
    ju"It got me all nice and hot, especially when you grabbed me from behind."
    #She still faces away from him, and we see her hand between her legs
    show sc julietwrestling j169
    mc"R-really?"
    #show a full shot of Juliet naked from behind
    show sc julietwrestling j170
    ju"Oh yeah..."
    #she still looks at him in the mirror
    show sc julietwrestling j171
    with dissolve
    ju"See for yourself."
    #A slightly different expression
    #Juliet turns around and faces the MC, stretching her arms above her head
    show sc julietwrestling j172
    with dissolve
    mc"{i}(*Whispering*){/i}\nHoly shit-balls..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_boobs_close1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j178a
    ju"Mmm..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_boobs1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j178b
    mc"(This was the last thing I expected from her.)"
    show sc julietwrestling j178
    with dissolve
    ju"Why don't you come a little closer..."
    show sc julietwrestling j179
    ju"We can wrestle again if you want to?"
    #Juliet moves closer to him
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_masturbating1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j173
    mc"I uh..."

    ju"NGHH..."
    show sc julietwrestling j180
    ju"What's the matter?"
    show sc julietwrestling j186
    ju"Cat got your tongue?"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_masturbating_close1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j186a
    mc"It's not that, it's just..."
    show sc julietwrestling j184
    ju"Go ahead... Touch me, [y_name]."
    show sc julietwrestling j185
    ju"I don't bite... much."

    menu:
        "Pussy":
            show sc julietwrestling j199
            with dissolve
            pause 1.0
            show sc julietwrestling j200
            with dissolve
            pause 1.0
            show sc julietwrestling j204
            with dissolve
            ju"Mmm..."
            ju"How does my pussy feel?"
            show sc julietwrestling j205
            ju"Hot and wet, right?"
            mc"Y-yeah..."


        "Breasts":
            #the MC reaches out to cup one of her breasts
            show sc julietwrestling j199
            with dissolve
            pause 1.0
            show sc julietwrestling j200
            with dissolve
            pause 1.0
            show sc julietwrestling j201
            with dissolve
            pause 1.0
            ju"Mmm..."
            show sc julietwrestling j202
            with dissolve
            ju"How do they feel?"
            show sc julietwrestling j203
            ju"Nice and supple, yeah?"
            mc"Oh yeah..."

    show sc julietwrestling j195
    mc"You know, I really shouldn't be doing this."
    #the MC takes his hand away from her breast
    show sc julietwrestling j195
    mc"If I get caught in here, then I could lose my job."
    show sc julietwrestling j194
    ju"Come on, [y_name]. We both know why we're here."
    show sc julietwrestling j189
    ju"At least allow me to give you something extra to thank you for today's session."
    show sc julietwrestling j188
    mc"Oh yeah, like what?"
    show sc julietwrestling j192
    ju"You seem very tense for someone so confident."
    ju"I can help you with that."
    show sc julietwrestling j194
    ju"Allow me to help you relieve some of the obvious tension between us."
    show sc julietwrestling j193
    with dissolve
    pause 1.0
    show sc julietwrestling j187a
    with dissolve
    pause 1.0
    show sc julietwrestling j196
    with dissolve
    pause 1.0
    mc"Mmm..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_jerkoff_close1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j187
    ju"So nice and firm."
    ju"You've been aching for a real woman's touch, haven't you?"
    show sc julietwrestling j194
    with dissolve
    ju"Do you like that, [y_name]?"
    show sc julietwrestling j195
    mc"Uh... Yeah, it feels great, Juliet."
    show sc julietwrestling j187
    ju"You're not the only one who is good with their hands."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_jerkoff1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j187a
    mc"NGHH!"
    ju"Are you gonna cum for me?"
    show sc julietwrestling j196
    mc"Y-yeah... Any second now."
    show sc julietwrestling j189
    ju"Where are you going to do it?"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_jerkoff_close1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j187
    ju"In my hand? On my breasts?"
    ju"Maybe I could get down on my knees so you can shower your load all over my face."
    ju"Or if you're quick enough, I could let you cream inside my tight, warm... pussy..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene anim_ep02_juliet_nc_jerkoff1:
            size (config.screen_width, config.screen_height)
    elif True:
        show sc julietwrestling j187a
    mc"Oh shit!"
    play sound "sound effects/01/sex/MC_climax_from_BJ_on_face.mp3" noloop
    show sc julietwrestling j191
    with vpunch
    mc"UNGHH!!!"
    show sc julietwrestling j197
    with vpunch
    mc"UHHH!!"
    show sc julietwrestling j196
    mc"Oh fuck!!"
    show sc julietwrestling j189
    ju"In my hand it is."
    stop sound fadeout 1.0
    show sc julietwrestling j194
    ju"Until our next seession. [y_name]."
    play sound "sound effects/01/couple_kissing_sound_effect.mp3" fadein 1.0
    show sc julietwrestling j198
    with dissolve
    ju"Mmm..."
    pause 1.0
    stop sound fadeout 1.0
    stop music fadeout 1.0
    #the MC leaves the women's changing room
    scene black
    with dissolve
    scene black
    with Pause (2)
    scene onlayer anim_layer
    $ v_ep02_juliet_fantasy_counter += 1
    $ persistent.replay_ep02_juliet_changing_room_fantasy = False
    $ renpy.end_replay()
    jump lb_ep02_03_08_The_MCs_private_session_with_Juliet_final

label lb_ep02_03_08_The_MCs_private_session_with_Juliet_final:

    #scene returns with the MC looking at Juliet while she prepares to leave
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    show sc julietwrestling j132
    with dissolve
    ju"Okay, I'm all signed out."
    show sc julietwrestling j133
    mc"Thanks."
    if v_ep02_task11_juliet_fitness_session == 5:
        $ task_completed(11,"aa")
        $ v_ep02_juliet_aa_tasks_counter +=1
    if v_ep02_task11_juliet_fitness_session == 4:
        $ task_completed(11,"a")
    if v_ep02_task11_juliet_fitness_session == 3:
        $ task_completed(11,"b")
    if v_ep02_task11_juliet_fitness_session == 2:
        $ task_completed(11,"c")
    if v_ep02_task11_juliet_fitness_session <= 1:
        $ task_completed(11,"d")
    show sc julietwrestling j134
    mc"Shall I book you in for another session?"
    show sc julietwrestling j135
    ju"I'll call you."
    show sc julietwrestling j136
    ju"There's a few things I need to take care of first. Finding a job for starters."
    show sc julietwrestling j139
    ju"But having a gym to call home is a big priority. But I'll definitely be in touch."
    show sc julietwrestling j140
    ju"Thanks for your time today."
    show sc julietwrestling j132
    mc"It was my pleasure."
    #show Juliet making a sexy hot remark to the MC to rock his world before she leaves
    show sc julietwrestling j158
    ju"I'm sure we'll be seeing plenty of each other in the near future."
    ju"See you soon, [y_name]."
    show sc julietwrestling j157
    mc"I look forward to it..."
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    if v_ep02_day2_gym_session_girls == "Zora":
        jump lb_ep02_03_08_The_MC_finishes_his_shift_at_the_gym
    else:
        #START WITH THESE LINES IF THE PLAYER CHOOSES ZORA SECOND
        centered "A little while later...{w=2.0}{nw}" with dissolve
        show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
        scene bg black with Dissolve(1)
        pause 1.0
        play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
        show sc zoragym z009
        zora"Hello?"
        #The MC looks up and sees that Zora has entered the gym
        show sc zoragym z008
        mc"Oh, hey Zora."
        show sc zoragym z012
        zora"I'm not late, am I?"
        show sc zoragym z010
        mc"No no, you're right on time!"
        show sc zoragym z014
        mc"It's great to see you again."
        show sc zoragym z013
        zora"Yeah, you too."
        show sc zoragym z015
        mc"So anyway, head on over there to the changing rooms and when you're ready, I'll meet you by the exercise machines."
        show sc zoragym z009
        zora"All right, I'll see you soon..."
        #Zora smiles and then leaves
        #screen goes blank
        stop ambient fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep02_03_07_Zora_arrives_at_the_gym_1


label lb_ep02_03_08_The_MC_finishes_his_shift_at_the_gym:

    #Harry stands behind the counter and the MC has changed clothes and is set to leave
    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    show sc julietwrestling j159
    with dissolve
    mc"All right, Harry. I'm done for the day."
    show sc julietwrestling j160
    ha"Adios, bro!"
    #they fist bump
    show sc julietwrestling j161
    ha"Make sure to fetch the gym some more honey's before your next shift."
    show sc julietwrestling j162
    mc"Haha! Sure, no problems."
    #the MC responds sarcastically
    show sc julietwrestling j163
    mc"See ya!"
    stop ambient fadeout 1.0
    #the MC leave the gym
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_09_The_MC_sees_the_tattoo_girl_from_the_parlour
    #END SCENE



    # ################################################################################

    # #NEXT SCENE: ToH's Ep2 Scene 03-09 - The MC encounters the tattoo girl from the parlour (???)

    # #SCENE NOTES:

    # #START OF THE JULIET NON-CANON SCENE
    # #the screen fizzles out and back in again to show that the MC is dreaming

    # mc"Oh, no you don't!"
    # #the MC slips his head out from Juliet's grip

    # ju"Huh?!"

    # ju"UHH!"
    # #the MC pins Juliet down. He sits on her stomach and presses his hands over her wrists so she can't move

    # ju"Get off of me!!"

    # mc"Say the word and I'll let you go."

    # ju"Fuck you!"

    # mc"Oh yeah..."
    # #the MC looks at Juliet's chest

    # mc"Time to have some fun!"
    # #the MC puts his hands on her chest

    # ju"Ohh!!"
    # ju"What are you doing??"

    # mc"Oh, come on."
    # mc"Don't pretend like you're not enjoying this."

    # mc"You love it when a guy like me takes control.."
    # mc"I can already feel how hard your nipples are under there."

    # #ANIMATION OF THE MC FONDLING HER CHEST

    # ju"Oh God..."
    # #The MC tears her top off so we see her breasts

    # ju"UHH!!"

    # ju"You asshole!!"
    # #she looks angry

    # ju"You.. You..."
    # #And then she eyes his erection in his pants

    # ju"Oh, screw it!!"
    # #Juliet grabs the back of his neck and pulls him down to kiss her

    # ju"Mmm..."
    # #show a close-up of them kissing

    # ju"Oh yes..."
    # #she has her eyes closed as the MC kisses her neck

    # ju"Lower..."
    # ju"NGHH!!"
    # #The MC cups one breast and licks/sucks on the other

    # ju"Oh fuck..."

    # mc"Damn, you have one incredibly, fuckable body."

    # ju"Uhhh.... [y_name]..."
    # #Show the MC's kissing her stomach and his hands on her gym pants

    # mc"Jackpot!"
    # #the MC stares at her crotch and then removes her shorts

    # mc"Oh yeah, that's what I'm talking about."

    # ju"Now the question is, what are you going to do about it?"
    # mc"I can think of a few things."

    # mc"Like this, for instance."
    # #show Juliet and the MC from a side angle, he slides her panties off

    # mc"Time to take you to pleasure town."

    # ju"Oh, [y_name]?"
    # #she calmly calls from between her legs just before he's about to eat her out

    # mc"Yeah?"
    # #The MC looks up from between her legs

    # ju"You didn't really expect me to be that easy, did you?"

    # mc"Huh?"
    # #Juliet closes her legs around his head

    # mc"Mfmfmfmf!!"
    # #the MC is struggling for air

    # mc"I uh... Oh..."
    # #the MC passes out and the screen fades to black

    # #screen goes blank
    # scene black
    # with dissolve
    # scene black
    # with Pause (2)

    # #END OF THE JULIET NON-CANON SCENE


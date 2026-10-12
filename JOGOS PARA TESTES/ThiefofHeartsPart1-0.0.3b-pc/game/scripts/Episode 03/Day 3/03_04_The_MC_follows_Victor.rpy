init:
    $ v_ep03_othergirls_fantasy_counter = 0
    $ v_ep03_03_04_lucy_kiss = False
    $ v_ep03_othergirls_dates_counter = 0




label lb_ep03_03_04_The_MC_follows_Victor:

    #SCENE BEGINS
    play music "sound effects/03/following_you2.mp3" loop fadein 1.0
    show sc mcfollowsvictor q001
    with dissolve
    pause 1.8
    $ image_sequence("sc mcfollowsvictor", ["q002", "q003", "q004","q005", "q006"], 1.8)
    # scene sc mcfollowsvictor q001
    # #The scene begins with Victor driving down a busy road - an evening scene
    # show sc mcfollowsvictor q002
    # with dissolve
    # pause 1.5
    # #The MC follows him on his bike
    # show sc mcfollowsvictor q003
    # with dissolve
    # pause 1.5
    # #Victor pulls up outside a local bar/club
    # show sc mcfollowsvictor q004
    # with dissolve
    # pause 1.5
    # #the MC finds somewhere to stop without Victor seeing him. He watches for a distance
    # #Victor gets out of his car and walks into a bar/club on the street
    # show sc mcfollowsvictor q005
    # with dissolve
    # pause 1.5
    # #the MC follows him and enters shortly after
    # show sc mcfollowsvictor q006
    # with dissolve
    # pause 1.5
    #screen goes blank
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    #Show the MC inside the bar/club, which is pretty busy - bar ambience
    play music "sound effects/03/nightclub_music_slow1.mp3" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party1.ogg" loop fadein 1.0
    show sc mcfollowsvictor q007
    with dissolve
    pause 1.5
    #He looks around for Victor
    show sc mcfollowsvictor q008
    with dissolve
    pause 1.5
    show sc mcfollowsvictor q009
    with dissolve
    mc"(Where did he go?)"
    $ image_sequence("sc mcfollowsvictor", ["q010", "q011", "q012", "q013","q014", "q015", "q016", "q017", "q018", "q019"], 1.5)
    # show sc mcfollowsvictor q010
    # with dissolve
    # pause 1.5
    # #The MC sees him at the bar by himself
    # show sc mcfollowsvictor q011
    # with dissolve
    # pause 1.5
    # #Victor orders a drink from the bartender
    # show sc mcfollowsvictor q012
    # with dissolve
    # pause 1.5
    # #MC has a thinking face
    # show sc mcfollowsvictor q013
    # with dissolve
    # pause 1.5
    # #The MC is about to turn and leave
    # show sc mcfollowsvictor q014
    # with dissolve
    # pause 1.5
    # #Then he notices an attractive woman in her mid-30s come up to Victor at the bar
    # show sc mcfollowsvictor q015
    # with dissolve
    # pause 1.5
    # #They hug and then Victor makes out with her at the bar
    # show sc mcfollowsvictor q016
    # with dissolve
    # pause 1.5
    # #The MC looks stunned
    # show sc mcfollowsvictor q017
    # with dissolve
    # pause 1.5
    # #They continue to kiss
    # show sc mcfollowsvictor q018
    # with dissolve
    # pause 1.5
    # #The MC pulls his phone out
    # show sc mcfollowsvictor q019
    # with dissolve
    # pause 1.5
    # #He takes a couple of quick photos
    # show sc mcfollowsvictor q020
    # with dissolve
    # pause 1.5
    #show the stills on his phone
    show sc mcfollowsvictor q021
    with dissolve
    mc"(Got you, you son of a bitch!)"
    #[Leave / Confront him]
    menu:
        "Leave":
            show sc mcfollowsvictor q022
            with dissolve
            pause 1.5
            #The MC turns before Victor sees him
            show sc mcfollowsvictor q023
            with dissolve
            pause 1.5
            stop music fadeout 1.5
            stop ambient fadeout 1.0
            #The MC leaves the bar with a mischievous look on his face
            #Go down to > #scene continues

        "Confront him"(wt="Best option"):
            #The MC notices the woman leave Victor’s side
            stop music fadeout 1.0
            show sc mcfollowsvictor q024
            with dissolve
            pause 1.5
            #Victor can’t take his eyes off her as she leaves for the bathroom
            show sc mcfollowsvictor q025
            with dissolve
            pause 1.5
            #The MC starts to walk up to Victor, a determined look on his face
            show sc mcfollowsvictor q026
            with dissolve
            pause 1.5
            play music "sound effects/01/Pulse Rock.mp3" loop fadein 1.0
            show sc mcfollowsvictor q027
            vic"[y_name]! What the hell are you doing here?"
            show sc mcfollowsvictor q028
            mc"I could ask you the same thing!"
            show sc mcfollowsvictor q029
            mc"I just saw you with that other woman."
            show sc mcfollowsvictor q030a
            with dissolve
            mc"So that’s why you’ve been staying out late at night."
            show sc mcfollowsvictor q031
            vic"I don’t know what you believe you saw, but it’s not what you think."
            show sc mcfollowsvictor q032
            mc"Really? You’re going to pull that line on me?"
            show sc mcfollowsvictor q033
            mc"I wasn’t born yesterday, [mc_vic_address]."
            show sc mcfollowsvictor q034
            mc"You’re cheating on [mc_v_address]."
            #The MC talks down at Victor who doesn’t even look at the MC
            show sc mcfollowsvictor q035
            mc"After all these years of us listening to your shit, about curfews and making sure we cover our asses..."
            show sc mcfollowsvictor q030a
            mc"I mean, seriously??"
            show sc mcfollowsvictor q044
            mc"When [mc_v_address] and the others find out about this, then they’ll-"
            #Victor cuts the MC off and looks up at him
            show sc mcfollowsvictor q037
            vic"No! You’re not going to do that."
            show sc mcfollowsvictor q038
            mc"Why the fuck wouldn’t I?"
            show sc mcfollowsvictor q029
            mc"They have a right to know that you’re just a lying, cheating scumbag."
            show sc mcfollowsvictor q040
            vic"Say what you want me, [y_name], but I’ll tell you why you won’t say anything."
            show sc mcfollowsvictor q041
            vic"It’s because you still need me to do this art gallery job, and you know it."
            #Vic looks forward again without staring at the MC
            show sc mcfollowsvictor q042
            vic"You all do."
            #Victor takes a sip of his whiskey
            show sc mcfollowsvictor q043
            mc"(Fuck...! He’s right.)"
            show sc mcfollowsvictor q044
            mc"You may be right, but one way or another, I’m going to tell [mc_v_address]."
            show sc mcfollowsvictor q045
            mc"On second thought, you will."
            show sc mcfollowsvictor q031
            vic"What do you mean?"
            show sc mcfollowsvictor q028
            mc"I won’t say anything to her."
            show sc mcfollowsvictor q044
            mc"And we’ll do the job tomorrow night as planned."
            show sc mcfollowsvictor q045
            mc"But once it’s done, and we’re in the clear, either you will come clean with [mc_v_address] about your infidelity, or I'll tell her myself."
            show sc mcfollowsvictor q047
            mc"And that’s non-negotiable."
            show sc mcfollowsvictor q035
            mc"Because the way I see it, you also need me tomorrow."
            #Victor grimaces
            show sc mcfollowsvictor q037
            vic"Fine."
            show sc mcfollowsvictor q040
            vic"I’ll tell her as soon as the job is finished."
            show sc mcfollowsvictor q036
            mc"Good."
            show sc mcfollowsvictor q041
            vic"What makes you so sure she’ll even believe you?"
            show sc mcfollowsvictor q042
            vic"It’s your word against mine."
            show sc mcfollowsvictor q044
            mc"True."
            show sc mcfollowsvictor q048
            mc"That’s why I always carry insurance."
            #The MC lifts his phone to show Victor the image of him kissing the other woman
            show sc mcfollowsvictor q034
            mc"And if [mc_v_address] throws you out, then you’ll leave without a fuss."
            show sc mcfollowsvictor q035
            mc"Comprende?"
            show sc mcfollowsvictor q040
            vic"Once the painting has been sold, I’ll be gone."
            show sc mcfollowsvictor q032
            mc"Smart decision."
            show sc mcfollowsvictor q049
            mc"I’m out of here..."
            #The MC leaves
            show sc mcfollowsvictor q050
            with dissolve
            pause 1.5
            stop music fadeout 1.0
            #Show a shot of Victor watching in the background from the bar as the MC leaves
            #He has a menacing look on his face


    #scene continues
    if v_ep02_01_04_Switch_The_Drives == True:
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        #NOTE: Only add this scene if we have time to make it
        #This scene only happens if the player selected “Switch the drives" in Scene 01-04 in Episode 2 - https://pixhost.to/show/1/531419767_screenshot-2024-11-09-at-11-09-50-pm.jpg
        play music2 "sound effects/01/party_music#5.ogg" loop fadein 1.0
        play ambient2 "sound effects/01/people_talking_at_party2.ogg" loop fadein 1.0
        show sc mcfollowsvictor q051
        with dissolve
        pause 1.0
        #A voice calls out to the MC just as he’s about to exit the club/bar
        "Leaving so soon?"

        #The MC turns around and sees Lucy (in different clothing to their first encounter)
        show sc mcfollowsvictor q052
        with dissolve
        pause 1.5
        show sc mcfollowsvictor q053
        with dissolve
        mc"Lucy?"
        show sc mcfollowsvictor q054
        lucy"I thought that was you."
        show sc mcfollowsvictor q055
        mc"What are you doing here?"
        show sc mcfollowsvictor q056
        lucy"Isn’t it obvious?"
        show sc mcfollowsvictor q057
        lucy"I have a life too.  When I’m not tracking down people that is."
        show sc mcfollowsvictor q058
        lucy" Which isn’t easy when one is trying to keep a low profile."
        show sc mcfollowsvictor q059
        mc"I know how that feels."
        show sc mcfollowsvictor q060
        mc"But what’s the real reason why you’re here?"
        show sc mcfollowsvictor q061
        lucy"I’m meeting someone if you must know. It’s just business."
        show sc mcfollowsvictor q132
        with dissolve
        mc"(She seems a little overdressed for a business meeting.)"
        show sc mcfollowsvictor q062
        lucy"Why so interested?"
        show sc mcfollowsvictor q063
        mc"I’m not. Just making small talk."
        show sc mcfollowsvictor q064
        with dissolve
        pause 1.0
        #Lucy looks across the room and sees a guy staring at her
        #The guy needs to look older but not too old or desperate-looking
        show sc mcfollowsvictor q065
        with dissolve
        lucy"Oh, God."
        #Lucy tries to cover her eyes to not make eye contact with him
        #The MC looks behind him and notices who she is looking at
        show sc mcfollowsvictor q065
        mc"Is that who you’re meeting with?"
        show sc mcfollowsvictor q066
        lucy"No. That’s just some guy who I {i}was{/i} seeing."
        show sc mcfollowsvictor q067
        lucy"Here's a tip: never mix business with pleasure."
        #Lucy looks bothered by this guy being here
        show sc mcfollowsvictor q068
        lucy" Unless you’re willing to suffer the consequences, you know?"
        show sc mcfollowsvictor q069
        mc"I get what you’re saying."
        show sc mcfollowsvictor q070
        mc"So what happened?"
        show sc mcfollowsvictor q075
        lucy"Without going into too much detail, we agreed to work together."
        show sc mcfollowsvictor q072
        lucy"Then, one thing led to another, and after a few meetups, some late-night drinks, it started to become more than that."
        show sc mcfollowsvictor q073
        lucy"And to him, it was even more."
        show sc mcfollowsvictor q074
        lucy"He wouldn’t stop calling even after I told him I didn’t want anything serious."
        show sc mcfollowsvictor q075
        lucy"He just doesn't get the message and he always knows where to find me."
        show sc mcfollowsvictor q076
        lucy"It’s been affecting my work and the control that I've had over my team."
        show sc mcfollowsvictor q077
        mc"So you’re aiming for something more casual then?"
        show sc mcfollowsvictor q069
        lucy"For now, yes."
        show sc mcfollowsvictor q077
        mc"I can respect that. Making others a priority first when you need to."
        #Lucy smiles
        show sc mcfollowsvictor q071
        mc"So why don't you just go over there and tell this guy to fuck off?"
        show sc mcfollowsvictor q073
        lucy"Oh, believe me, I really want to."
        show sc mcfollowsvictor q074
        lucy"But I can't make a scene in here."
        show sc mcfollowsvictor q076
        lucy"I'm trying to keep a low profile, remember?"
        show sc mcfollowsvictor q077
        mc"Yes, of course."

        show sc mcfollowsvictor q078
        with dissolve
        pause 1.5
        #Her mood changes when the guy stands up and looks like he’s approaching them
        show sc mcfollowsvictor q065
        with dissolve
        lucy"Shit..."
        show sc mcfollowsvictor q067
        with dissolve
        lucy"I think he’s coming over here."

        #[Say something / Make out with her]
        menu:
            "Say something to the guy"(wt= "You won’t get another special scene with Lucy"):
                #Variable required here for this choice
                show sc mcfollowsvictor q079
                mc"I’ll handle this."

                #The MC turns and faces the guy
                show sc mcfollowsvictor q081
                mc"Can I help you, buddy?"
                show sc mcfollowsvictor q082
                man"I just wanted to speak with Lucy for a minute, if I may?"
                show sc mcfollowsvictor q083
                mc"Yeah, not a good idea."
                show sc mcfollowsvictor q084
                mc"We’re in the middle of a conversation, so I’d suggest you back off."
                show sc mcfollowsvictor q085
                mc"Lucy doesn’t want to speak with you. So beat it!"
                show sc mcfollowsvictor q086
                man"Really?"
                show sc mcfollowsvictor q087
                man"You’re with this guy?"
                #He addresses Lucy but points at the MC
                show sc mcfollowsvictor q088
                lucy"When are you going to get the message?"
                show sc mcfollowsvictor q089
                lucy"I’m not interested."
                show sc mcfollowsvictor q090
                lucy"I don’t want to do business. Or anything else with you anymore!"
                show sc mcfollowsvictor q091
                lucy"So get the fuck outta here!"
                show sc mcfollowsvictor q092
                man"Ughh, fine."
                show sc mcfollowsvictor q093
                man"You’re nothing but a cheap whore, anyway."
                show sc mcfollowsvictor q094
                man"Good luck with her, kid."
                #the man leaves
                show sc mcfollowsvictor q095
                mc"Now I can see why you broke it off with this idiot. What a dumbass."
                #The MC speaks to Lucy but he’s watching the man leave
                show sc mcfollowsvictor q096
                lucy"Just what the hell do you think you were doing?"
                #Lucy’s tone changes, she has her hands and arms up and looks pissed off at the MC
                show sc mcfollowsvictor q097
                mc"Huh?"
                show sc mcfollowsvictor q098
                mc"What did I do?"
                show sc mcfollowsvictor q099
                lucy"I don’t need someone to stand up for me, [y_name]."
                show sc mcfollowsvictor q100
                lucy"The last thing I want is to be made to look weak, especially in front of that loser."
                show sc mcfollowsvictor q101
                mc"Oh, sorry Lucy."
                show sc mcfollowsvictor q102
                mc"I didn’t mean to-"
                show sc mcfollowsvictor q103
                lucy"Save it! The damage is already done."
                #She folds her arms and rolls her eyes
                show sc mcfollowsvictor q104
                lucy"Anyway, my informant has just arrived."
                #Lucy looks to her right as she sees her informant arrive
                show sc mcfollowsvictor q105
                lucy"I guess I’ll see you around."
                show sc mcfollowsvictor q106
                lucy"Bye..."
                stop music2 fadeout 2.0
                stop ambient2 fadeout 2.0
                #Lucy leaves and greets the informant

                #The MC looks dismayed when he leaves the club

                #screen goes blank

                scene black
                with dissolve
                scene black
                with Pause (2)
                jump lb_ep03_04_01_Final_meeting_before_the_heist

            "Make out with her"(wt= "You will get another special scene with Lucy in the future"):
                show screen scr_secret_icon("v_secrets_ep03_03_04_1") onlayer ontop
                with { "ontop": dissolve}
                $ v_ep03_03_04_lucy_kiss = True
                #Variable required here for this choice
                #the MC thinks for a moment and then pulls Lucy in close
                show sc mcfollowsvictor q109
                with dissolve
                pause 1.0
                show sc mcfollowsvictor q110
                lucy"What are you-"

                #The MC kisses Lucy deeply in front of the guy approaching
                play sound "sound effects/01/kiss_and_moan_sound_effect03.mp3" noloop
                show sc mcfollowsvictor q111
                lucy"Mmm..."

                menu:
                    "Grope her ass":
                        #show the MC grabbing Lucy’s ass with one hand while the other remains on her upper back
                        show sc mcfollowsvictor q112
                        lucy"(OH!)"
                    "French kiss her":
                        #show the MC openly French-kissing Lucy
                        show sc mcfollowsvictor q113
                        lucy"(OH!)"
                        show sc mcfollowsvictor q114
                        with dissolve
                        pause 1.5

                #The man who is approaching looks on awkwardly as the MC kisses Lucy
                show screen scr_secret_hotspot ("sc mcfollowsvictor q115","262, 506, 64, 201","v_secrets_ep03_03_04_1")
                show sc mcfollowsvictor q115
                with dissolve

                pause 1.5
                #He then leaves
                show sc mcfollowsvictor q116
                with dissolve
                pause 1.5
                #After he leaves, the kiss ends
                stop sound fadeout 2.0
                hide screen scr_secret_hotspot
                show sc mcfollowsvictor q118
                with dissolve
                lucy"Um... What was that?"
                show sc mcfollowsvictor q119
                with dissolve
                mc"That was me diffusing the situation."
                show sc mcfollowsvictor q120
                lucy"Yeah, but did you need to kiss me?"
                show sc mcfollowsvictor q121
                mc"I got rid of him, didn’t I?"
                mc"Besides, it seemed like the best thing to do at the time."
                show sc mcfollowsvictor q122
                mc"And I had to make it look convincing."
                show sc mcfollowsvictor q123
                with dissolve
                lucy"I like your assertiveness and quick thinking, so I’ll let it slide."
                show sc mcfollowsvictor q124
                lucy"But don’t think that kissing me means that you can-"
                show sc mcfollowsvictor q125
                mc"I know, I know. You and I are strictly business."
                show sc mcfollowsvictor q126
                mc"However, I enjoyed doing {i}business{/i} with you Lucy, even though it was brief."
                show sc mcfollowsvictor q127
                lucy"Yeah, I guess it wasn't so bad."
                show sc mcfollowsvictor q128
                lucy"Better than having a sharp object jammed against your throat, right?"
                show sc mcfollowsvictor q129
                mc"Haha! Yeah, much better."
                #Lucy gives the MC a cheeky look
                show sc mcfollowsvictor q130
                with dissolve
                pause 1.5
                show sc mcfollowsvictor q131
                with dissolve
                lucy"Anyway, my informant just arrived."
                #Lucy looks to her right as she sees her informant arrive
                show sc mcfollowsvictor q127
                lucy"We’ll be in touch very soon."
                show sc mcfollowsvictor q132
                mc"I look forward to it."
                show sc mcfollowsvictor q131
                lucy"Bye, [y_name]."
                $ image_sequence("sc mcfollowsvictor", ["q133", "q134", "q135", "q137","q138"], 1.5)
                #The MC watches Lucy leave
                # show sc mcfollowsvictor q133
                # with dissolve
                # pause 1.5
                # #He checks out her ass
                # show sc mcfollowsvictor q134
                # with dissolve
                # pause 1.5
                # show sc mcfollowsvictor q135
                # with dissolve
                # pause 1.5
                # #Lucy greets her informant who embraces her, kisses her on the cheek
                # #While he is doing this, she gives the MC one final look and winks at him
                # show sc mcfollowsvictor q137
                # with dissolve
                # pause 1.5
                # #The MC looks happy as he starts walking out of the club
                # show sc mcfollowsvictor q138
                # with dissolve
                # pause 1.5
                stop music2 fadeout 2.0
                stop ambient2 fadeout 2.0
                #screen goes blank
                scene black
                with dissolve
                scene black
                with Pause (2)
                hide screen scr_secret_icon onlayer ontop
                with { "ontop": dissolve}
                if persistent.v_secrets_enabled and persistent.v_secrets_ep03_03_04_1:
                    jump lb_ep03_03_04_Lucy_NC

    #scene continues
    show sc mcfollowsvictor q051
    with dissolve
    pause 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    stop music2 fadeout 2.0
    stop ambient2 fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_04_01_Final_meeting_before_the_heist

label lb_ep03_03_04_Lucy_NC:
    if not _in_replay:
        scene img_secret_scene_overlay onlayer anim_layer
        with { "anim_layer": dissolve}
    else:
        show screen scr_end_replay
    $ v_ep03_othergirls_fantasy_counter += 1
    #THE NC SCENE BEGINS HERE
    #The “NON-CANON BONUS SCENE" writing will be at the top of the screen as soon as the scene finishes above

    #This scene is somewhat a nod to this one from Top Gun - https://www.youtube.com/watch?v=oVqW4GzLILM&ab_channel=puashine
    #show Lucy sitting at a table in the club, talking with the male informant. Show from the MC’s POV
    play music "sound effects/01/party_music#2.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party2.ogg" loop fadein 1.0
    show sc ep3lucync l01
    with dissolve
    pause 1.5
    $ image_sequence("sc ep3lucync", ["l02", "l03", "l04", "l05", "l01","l06"], 1.7)
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #The MC decides not to leave after he said goodbye to Lucy.
    #He watches her from a distance where she can’t see him

    #he waits and watches Lucy talk with her informant, a male

    #after some time, Lucy gets up from her seat and leaves to go to the ladies bathroom

    #the MC follows her

    #the MC enters the women’s bathroom - **Make sure there is a counter that Lucy can sit on

    #e.g. - https://i.pinimg.com/736x/b8/15/07/b815077aa15eb94cf5f7517a11a8aa2a.jpg
    play music "sound effects/03/nightclub_bathroom_ambience.mp3" loop fadein 1.0
    show sc ep3lucync l07
    with dissolve
    pause 1.5
    #Lucy stands and looks at the mirror, fixing her lipstick
    show sc ep3lucync l08
    with dissolve
    lucy"So..."
    show sc ep3lucync l09
    lucy"You just couldn’t stay away, huh?"
    show sc ep3lucync l10
    with dissolve
    pause 1.0
    #Lucy sees the MC, but then turns back to the mirror
    show sc ep3lucync l11
    with dissolve
    mc"It’s hard to do that when you know that somebody might be making a huge mistake."
    show sc ep3lucync l12
    lucy"I presume you’re referring to that guy out there."
    #Lucy turns to look at the MC but doesn’t change her posture
    show sc ep3lucync l13
    lucy"And how do you know it’s not a mistake coming into the ladies bathroom."
    show sc ep3lucync l14
    mc"I know a risk worth taking when I see it."
    show sc ep3lucync l15
    with dissolve
    pause 1.5
    #The MC checks Lucy out as he moves closer to her
    show sc ep3lucync l16
    with dissolve
    pause 1.5
    #Lucy turns around so she’s backed against the bathroom bench and the MC is facing her
    show sc ep3lucync l17
    with dissolve
    lucy"You should quit while you’re behind, [y_name]."
    show sc ep3lucync l19
    lucy"Because I can tell you right now, there’s no way you’d be able to keep up with me."
    show sc ep3lucync l18
    mc"And what if I wasn’t trying to keep up?"
    show sc ep3lucync l18a
    mc"What if I was merely trying to score points with you."
    show sc ep3lucync l19
    lucy"Okay, you have my attention."
    show sc ep3lucync l17
    lucy"You have two minutes before I walk out that door and sit back down with your um... competition."
    show sc ep3lucync l19
    lucy"Wow me."

    lucy"And do it without using your words."
    $ image_sequence("sc ep3lucync", ["l20", "l21"], 1.8)
    #the MC moves in close, preparing to kiss her, but then holds off

    #Instead, he bends slightly and places his hands on her thighs and pushes up her skirt a few centimetres

    #then to Lucy’s surprise, the MC lifts her up onto the bathroom counter
    show sc ep3lucync l22
    with vpunch
    lucy"Woah!"
    #the MC teases her, pulls her legs apart as he kisses her neck
    stop music fadeout 1.0
    play music "sound effects/01/Touch_and_Tension.mp3" loop fadein 1.0
    show sc ep3lucync l23
    lucy"Mmm..."
    show sc ep3lucync l24
    lucy" You’ll need to do better than that, [y_name]."

    show sc ep3lucync l22
    with dissolve
    pause 1.5
    #the MC slides his hand under her skirt, presses his fingers against her underwear
    show sc ep3lucync l18
    with dissolve
    mc"Very well then..."
    show sc ep3lucync l25
    with dissolve
    pause 1.5
    play sound "sound effects/01/female_moaning01.mp3" noloop
    show sc ep3lucync l26
    with dissolve
    lucy"Nnn..."
    show sc ep3lucync l27
    lucy"Are you sure you wanna go there?"
    show sc ep3lucync l28
    mc"Not only am I sure, but I’m deadset on it."

    #the MC takes hold of the side of her panties and tears them off
    show sc ep3lucync l29
    lucy"OH!"
    show sc ep3lucync l30
    lucy"I’m going to make sure you pay for that."
    show sc ep3lucync l30a
    lucy"But not right now, as I want to see what you do next."
    #the MC smiles and then descends so he is face height with her crotch, and swings her legs apart

    #Lucy POV - the MC looks up at her
    show sc ep3lucync l30b
    lucy"Well? What are you waiting for?"
    show sc ep3lucync l32
    lucy"Or are you going to chicken out--"
    show sc ep3lucync l33
    pause 0.5
    #the MC dives between her legs
    play sound "sound effects/03/cunnilingus_sex_sound_effect.mp3" loop fadein 1.0
    show sc ep3lucync l34
    with vpunch
    lucy"HOLY SHIT!!!"
    #Lucy’s eyes roll into the back of her head

    #various renders of the MC’s face between her legs - show different angles

    #close-up, side view, zoomed out, Lucy’s POV
    show sc ep3lucync l35
    lucy"Oh fuck!"
    show sc ep3lucync l36
    lucy"Did you um... lock the door?"
    stop sound fadeout 1.0
    show sc ep3lucync l37
    mc"Uh-huh..."
    #the MC looks up at her to respond
    show sc ep3lucync l38
    lucy" You may continue then."
    $ image_sequence("sc ep3lucync", ["l39", "l40", "l33"], 1.5)
    #The MC resumes eating her out
    play sound "sound effects/03/cunnilingus_sex_sound_effect2.mp3" loop fadein 1.0
    show sc ep3lucync l41
    with dissolve
    lucy"Oh yes... Eat my pussy!"
    show sc ep3lucync l42
    lucy"Lick my clit, just like that."

    #The MC licks her clitoris

    #The MC resumes eating her out
    show sc ep3lucync l43
    lucy"Oh my God!"
    lucy"I think I’m gonna..."
    show sc ep3lucync l41
    lucy"NGHH!!!"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    #screen flashes
    #As she climaxes, her legs cross over the MC’s head and she throws her head back with her mouth open

    #screen flashes again

    #show Lucy sitting at the table with the informant, and she wasn’t paying attention to what he was saying
    play music "sound effects/01/party_music#2.ogg" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party2.ogg" loop fadein 1.0
    show sc ep3lucync l44
    with flash(0.25, 0, 0.75, "#fff")
    pause 1.5
    "Lucy?"
    show sc ep3lucync l45
    "Are you all right?"
    show sc ep3lucync l46
    lucy"Oh, yeah..."
    show sc ep3lucync l47
    lucy" I’m fine."
    show sc ep3lucync l48
    pause 1.5
    #Lucy looks down and realises she has a hand between her legs, rubbing her panty-covered pussy
    show sc ep3lucync l49
    pause 1.5
    #she looks shocked and then returns her attention to the informant
    show sc ep3lucync l50
    lucy"Um... Could you please excuse me for a few minutes?"
    show sc ep3lucync l46
    lucy"I'm just going to use the bathroom..."
    show sc ep3lucync l51
    with dissolve
    pause 2.0
    #Lucy leaves the table with a confused look on her face

    #final shot of her walking towards the bathroom like she did in the early part of this scene

    #screen goes blank
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene onlayer anim_layer
    with { "anim_layer": dissolve}
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ persistent.replay_ep03_lucy_bathroom_fantasy = False
    $ renpy.end_replay()
    jump lb_ep03_04_01_Final_meeting_before_the_heist




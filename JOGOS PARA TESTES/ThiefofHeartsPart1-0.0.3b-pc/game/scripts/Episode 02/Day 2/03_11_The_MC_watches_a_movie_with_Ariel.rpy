init:
    $ v_ep02_ariel_fantasy_counter = 0
    $ ariel_harem_points_counter = 0
    $ bella_harem_points_counter = 0
    $ vivian_harem_points_counter = 0

    image sc movienightariel breast fondle:
        "sc movienightariel l094" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc movienightariel l094a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc movienightariel l094b" with Dissolve(0.2, alpha=True)
        pause 0.8
        repeat

    image sc arieldreamtv breast fondle1:
        "sc arieldreamtv a00b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a00ba" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a00bb" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc arieldreamtv rub1:
        "sc arieldreamtv a00d" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00da" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00db" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc arieldreamtv rub2:
        "sc arieldreamtv a00e" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00ea" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00eb" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc arieldreamtv rub3:
        "sc arieldreamtv a00f" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00fa" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00fb" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc arieldreamtv rub4:
        "sc arieldreamtv a00k" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00ka" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc arieldreamtv a00kb" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc arieldreamtv breast fondle2:
        "sc arieldreamtv a08a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a08" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a08b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a08" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc arieldreamtv pussy rub:
        "sc arieldreamtv a09" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc arieldreamtv a09a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc arieldreamtv grind:
        "sc arieldreamtv a21" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arieldreamtv a21a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arieldreamtv a21b" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc arieldreamtv a21a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

label lb_ep02_03_11_The_MC_watches_a_movie_with_Ariel:
    #SCENE BEGINS
    #USE THIS SETTING - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
    #the MC waits downstairs in front of the TV for Ariel to join him
    #there's a bowl of popcorn on the coffee table
    #Ariel comes down and has removed her glasses and let her hair down
    scene sc movienightariel l001
    with dissolve
    pause 2.0
    show sc movienightariel l002
    with dissolve
    pause 1.0
    scene sc movienightariel l003
    with dissolve
    a"Hey, I'm here."
    show sc movienightariel l004
    with dissolve
    mc"Woah..."
    show sc movienightariel l005
    a"What?"
    show sc movienightariel l006
    mc"You're um... You're not wearing your glasses."
    show sc movienightariel l008
    a"Yeah, I don't need them."
    a"I figured that if we're going to sit back and relax, I may as well let my hair hang down too."
    show sc movienightariel l007
    mc"You look great. You should do it more often."
    show sc movienightariel l010
    a"Oh, well, maybe..."
    #Ariel seems hesitant and then takes a seat on the sofa with the MC
    show sc movienightariel l011
    mc"Did you talk with [b_name] much before she went to bed?"
    show sc movienightariel l012
    a"Not for long."
    show sc movienightariel l013
    a"She was complaining about a tough day at the clothing store."
    show sc movienightariel l013a
    with dissolve
    pause 1.0
    show sc movienightariel l014
    with dissolve
    a"And then she mentioned something about taking a valium before she went to sleep."
    show sc movienightariel l015
    a"So she'll be out like a light until the morning."
    show sc movienightariel l016
    mc"Cool..."
    show sc movienightariel l017
    a"So what are we gonna watch?"
    show sc movienightariel l018
    mc"Well, how about..."

    #[Romance / Horror]
    menu:
        "Romance"(wt="Bonus image"):
            show sc movienightariel l019
            mc"{i}Love is Nice?{/i}"
            show sc movienightariel l020
            a"Oh, what's it about?"
            show sc movienightariel l021b
            mc"Well, it's a romantic comedy, and it's about a guy who ends up getting engaged to two brides at the same time..."
            mc"...and they both show up on the day of the wedding."
            show sc movienightariel l023
            mc"What do you think?"
            show sc movienightariel l024
            a"It sounds a little silly, however, now that you've mentioned the synopsis, I kind of want to see how things turn out."
            show sc movienightariel l025
            mc"All right, I'm happy to suffer. I mean, sit down and watch this with you."
            show sc movienightariel l026
            a"Oh, [y_name]..."
            $ rewards_unlock ("ariel",10)
            play sound "sound effects/01/Ariel_laughing1.mp3" noloop
            show sc movienightariel l027
            a"Haha..."
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)


            centered "A little later on...{w=2.0}{nw}" with dissolve
            show text "A little later on..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
            scene bg black with Dissolve(1)
            pause 1.0
            #this comes up on the screen while Ariel is simply sitting next to the MC on the sofa in a now, dimly lit room
            play music "sound effects/02/The Love We Find.mp3" loop fadein 1.0
            show sc movienightariel l028
            with dissolve
            pause 1.0
            show sc movienightariel l029
            with dissolve
            movie_man"{i}Ladies... stop!{/i}"
            #the man and two women on the screen speak as the MC and Ariel watch
            show sc movienightariel l030
            movie_man"{i}You can both marry me!{/i}"
            movie_woman1"{i}Oh my!{/i}" (multiple=2)
            movie_woman2"{i}Yeah, let's do it!{/i}" (multiple=2)
            pause 1.0

            #[Be critical / Positive feedback]
            menu:
                "Be critical":
                    show sc movienightariel l033
                    mc"Ughh... Really?"
                    #the MC looks pissed off about the film
                    show sc movienightariel l034
                    a"What's wrong?"
                    #Ariel turns to the MC
                    show sc movienightariel l035
                    mc"What's wrong?"
                    show sc movienightariel l035a
                    mc"This whole set-up."
                    show sc movienightariel l036
                    mc"The storyline makes absolutely no sense at all."
                    show sc movienightariel l037
                    a"I know, but it's just a movie."
                    show sc movienightariel l038
                    a"He simply didn't want to choose one girl over the other. He was crazy about both of them."
                    show sc movienightariel l039
                    a"It's kind of romantic in a unique way."
                    show sc movienightariel l040
                    mc"Yeah, but how is it meant to work?"
                    show sc movienightariel l041
                    a"I suppose we're not meant to find out."
                    show sc movienightariel l042
                    mc"I guess."
                    show sc movienightariel l043
                    mc"Still, it's pretty ridculous."
                    $ v_ep01_ariel_arrogant_counter += 1
                    show sc movienightariel l044
                    a"Hmm..."
                    #Ariel looks down
                    stop music fadeout 2.0
                    show sc movienightariel l045
                    a"Anyway, it's getting kind of late, so I think I'm gonna go to bed."
                    #she looks up at him and speaks
                    show sc movienightariel l046
                    mc"But there's still more of the movie to go."
                    show sc movienightariel l047
                    a"I know, but [mc_vic_address] and [mc_v_address ] will be home any minute now."
                    show sc movienightariel l048
                    a"So maybe it's best if we call it a night."
                    show sc movienightariel l049
                    mc"Yeah, that would probably be wise."
                    show sc movienightariel l050
                    with dissolve
                    a"Thanks for inviting me to watch a movie with you, [y_name]."
                    #Ariel stands up
                    show sc movienightariel l051
                    a"And sorry that you didn't enjoy it."
                    show sc movienightariel l077
                    a"Mmm..."
                    show sc movienightariel l078
                    a"Goodnight."
                    show sc movienightariel l053
                    mc"Night, [a_name]..."
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                    #END SCENE

                "Positive feedback"(wt="Best option + 1 [a_name] Harem Point"):
                    show sc movienightariel l054
                    a"So, what do you think so far?"
                    show sc movienightariel l023
                    mc"I'm not really a fan of the genre, but it's been pretty decent."
                    mc"And you?"
                    show sc movienightariel l055
                    a"It's been okay, though I do feel bad for those two girls."
                    show sc movienightariel l018
                    mc"Why?"
                    show sc movienightariel l056
                    a"Well, if he marries both, then they will have to share one guy between them."
                    show sc movienightariel l023
                    mc"Maybe they prefer it that way."
                    show sc movienightariel l020
                    a"Possibly."
                    show sc movienightariel l018
                    mc"How would you feel if there was another woman in love with the same guy that you're in love with?"
                    show sc movienightariel l054
                    a"I never thought of it like that."
                    show sc movienightariel l023
                    mc"Maybe now you might be able to see why the main character found it so difficult to choose one or the other."
                    show sc movienightariel l058
                    a"I can see your point."
                    $ v_ep01_ariel_respect_counter += 1
                    show sc movienightariel l059
                    a"Interesting..."
                    #Ariel in deep thought
                    #+1 HAREM POINT
                    $ ariel_harem_points_counter += 1
                    show sc movienightariel l060
                    with dissolve
                    mc"Anyway, let's get back to the movie, and find out what happens next!"
                    show sc movienightariel l061
                    a"Yeah, good idea..."
                    $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                    #screen goes blank
                    stop music fadeout 1.0
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                    #IMPORTANT - THE HIDDEN ITEM FOR THE NC SCENE NEEDS TO BE HIDDEN BETWEEN HERE AND THE TWO OPTIONS BELOW

                    #the scene returns with Ariel snuggling up against the MC, resting her head on his shoulder
                    play music "sound effects/02/The Love We Find1.mp3" loop fadein 1.0
                    show sc movienightariel l062
                    with dissolve
                    mc"(...)"
                    #show Ariel resting her head on his chest/shoulder
                    show sc movienightariel l063
                    mc"(This movie took a really hot turn.)"
                    show sc movienightariel l064
                    mc"(I've never seen a threesome take place in a romantic comedy before.)"
                    mc"(Well, apart from that movie \"Threesome\"!)"
                    #Tease the player by not showing what is happening on the TV screen

                    #[Continue watching the movie / Put your arm around her]
                    menu:
                        "Continue watching the movie":
                            #show Ariel and the MC watching the film - Ariel bites her bottom lip, to show how intense the scene is that they are watching
                            #screen goes blank
                            stop music fadeout 1.0
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            show sc movienightariel l066
                            a"Well, that was pretty good. Did you like it?"
                            #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                            #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen

                            show sc movienightariel l067
                            mc"Oh yeah, it was very entertaining, for a chick flick."
                            show sc movienightariel l068
                            a"I know, I was pleasantly surprised by some of the um... content."
                            show sc movienightariel l069
                            a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                            show sc movienightariel l070
                            a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                            show sc movienightariel l071
                            a"So maybe you should too."
                            show sc movienightariel l072
                            mc"Yeah, that would probably be wise."
                            show sc movienightariel l067
                            with dissolve
                            a"Thanks for inviting me to watch a movie with you, [y_name]."
                            #Ariel stands up
                            show sc movienightariel l073
                            mc"You're welcome."
                            show sc movienightariel l074
                            with dissolve
                            mc"Perhaps we could do it again sometime?"
                            show sc movienightariel l075
                            a"Sure, that'd be great!"
                            #Ariel hugs the MC
                            show sc movienightariel l077
                            a"Mmm..."
                            show sc movienightariel l078
                            a"Goodnight."
                            #they break the hug
                            show sc movienightariel l053
                            mc"Night, [a_name]..."
                            #The MC watches Ariel head towards the staircase and leave
                            #screen goes blank
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                            #END SCENE

                        "Put your arm around her"(wt="Best option"):
                            #The MC subtly puts an arm around Ariel
                            show sc movienightariel l080
                            with dissolve
                            pause 2.0
                            show sc movienightariel l081
                            with dissolve
                            a"Mmm..."
                            #Ariel smiles and continues to watch the movie
                            #+1 ARIEL POINT
                            $ v_ep02_03_11_movie_date_with_ariel_counter += 1

                            #show Ariel and the MC watching the film - Ariel bites her bottom lip, to show how intense the scene is that they are watching
                            show sc movienightariel l082
                            with dissolve
                            pause 1.0
                            #[Continue watching the movie / Make a move]
                            #NOTE: The “Make a move" option will only be available if the player has at least ONE Ariel HEART by this point
                            menu:
                                "Continue watching the movie":
                                    show sc movienightariel l083
                                    with dissolve
                                    pause 1.0
                                    #show the MC continuing to watch the film with Ariel glancing up at him, which he doesn't notice
                                    #screen goes blank
                                    stop music fadeout 1.0
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)

                                    show sc movienightariel l084
                                    with dissolve
                                    a"Well, that was pretty good. Did you like it?"
                                    #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                                    #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen
                                    show sc movienightariel l085
                                    mc"Oh yeah, it was very entertaining, for a chick flick."
                                    show sc movienightariel l086
                                    a"I know, I was pleasantly surprised by some of the um... content."
                                    show sc movienightariel l087
                                    a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                                    show sc movienightariel l088
                                    a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                                    show sc movienightariel l089
                                    a"So maybe you should too."
                                    show sc movienightariel l090
                                    mc"Yeah, that would probably be wise."
                                    show sc movienightariel l067a
                                    with dissolve
                                    a"Thanks for inviting me to watch a movie with you, [y_name]."
                                    #Ariel stands up
                                    mc"You're welcome."
                                    show sc movienightariel l075
                                    with dissolve
                                    mc"Perhaps we could do it again sometime?"
                                    show sc movienightariel l076
                                    a"Sure, that'd be great!"
                                    show sc movienightariel l077
                                    a"Mmm..."
                                    #Ariel hugs the MC
                                    show sc movienightariel l078
                                    a"Goodnight, [y_name]."
                                    #they break the hug
                                    show sc movienightariel l079
                                    with dissolve
                                    mc"Night, [a_name]..."
                                    #The MC watches Ariel head towards the staircase and leave
                                    #screen goes blank
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)
                                    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                                    #END SCENE

                                "Make a move"(wt="Best option"):
                                    #show consecutive images of the MC's hand moving from its place on Ariel's hip/waist and cupping under her breast
                                    show sc movienightariel l091
                                    with dissolve
                                    pause 1.0
                                    show sc movienightariel l092
                                    with dissolve
                                    a"{i}(*Whispering*){/i}\nOhh..."
                                    #Ariel murmurs but never takes her eyes off the screen
                                    #+1 ARIEL POINT
                                    $ v_ep02_03_11_movie_date_with_ariel_counter += 1

                                    movie_man"That feels amazing, ladies..."
                                    #the guy on the screen speaks

                                    #[Squeeze her breast / Continue watching the film]

                                    menu:
                                        "Squeeze her breast"(wt="Best option"):
                                            #show an animation of the MC fondling her breast
                                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                                show sc movienightariel breast fondle
                                            else:
                                                show sc movienightariel l094
                                            a"(Oh!!)"
                                            show sc movienightariel l095
                                            a"Er... Um..."
                                            #Ariel moves so that the MC's hand slips from her chest
                                            show sc movienightariel l096
                                            mc"Everything okay?"
                                            show sc movienightariel l097
                                            a"Y-yeah.. My leg started to fall asleep and I just had to move to wake it up."
                                            show sc movienightariel l098
                                            mc"Oh, all right."
                                            show sc movienightariel l099
                                            a"I'm fine now. Let's get back to watching the movie."
                                            $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                                            #Ariel rests her head back on the MC's shoulder/chest
                                            #+1 ARIEL POINT
                                            show sc movienightariel l100
                                            with dissolve
                                            pause 1.0
                                            #final shot here of the MC continuing to watch the film with Ariel glancing up at him, smiling
                                            #screen goes blank
                                            stop music fadeout 1.0
                                            scene black
                                            with dissolve
                                            scene black
                                            with Pause (2)
                                            #go down to "scene continues"

                                        "Continue watching the film":
                                            show sc movienightariel l101
                                            with dissolve
                                            pause 1.0
                                            #final shot here of the MC continuing to watch the film with Ariel glancing up at him, smiling
                                            show sc movienightariel l102
                                            a"Um... Let's not take things too far, [y_name]."
                                            #She removes her hand
                                            show sc movienightariel l103
                                            mc"Oh, sure thing, [a_name]."
                                            #Ariel gives the MC an awkward smile
                                            show sc movienightariel l100
                                            with dissolve
                                            pause 1.0
                                            stop music fadeout 1.0
                                            #final shot here of the MC continuing to watch the film with Ariel glancing up at him, smiling
                                            #screen goes blank
                                            scene black
                                            with dissolve
                                            scene black
                                            with Pause (2)
                                            #go down to "scene continues"


                            #scene continues
                            show sc movienightariel l137a
                            a"Well, that was pretty good. Did you like it?"
                            #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                            #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen
                            show sc movienightariel l067a
                            mc"Oh yeah, it was very entertaining, for a chick flick."
                            show sc movienightariel l084
                            a"I know, I was pleasantly surprised by some of the um... content."
                            show sc movienightariel l086
                            a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                            show sc movienightariel l087
                            a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                            show sc movienightariel l088
                            a"So maybe you should too."
                            show sc movienightariel l090
                            mc"Yeah, that would probably be wise."
                            show sc movienightariel l067a
                            with dissolve
                            a"Thanks for inviting me to watch a movie with you, [y_name]."
                            #Ariel stands up
                            if v_ep02_03_11_movie_date_with_ariel_counter >= 4:
                                $ ariel_love_level +=1
                                $ v_ep02_ariel_hearts_counter += 1
                            mc"You're welcome."
                            show sc movienightariel l074
                            with dissolve
                            mc"Perhaps we could do it again sometime?"
                            show sc movienightariel l075
                            a"Sure, that'd be great!"
                            #Ariel hugs the MC
                            show sc movienightariel l077
                            a"Mmm..."
                            show sc movienightariel l078
                            a"Goodnight."
                            #they break the hug

                            #If the player has less than -5 Ariel points for this task
                            #Go Down to “scene continues"

                            #If the player has 5 Ariel points or more for this task
                            #Make sure it's coded to accommodate any extra points that may have been allocated
                            if v_ep02_03_11_movie_date_with_ariel_counter == 5:
                                play sound "sound effects/01/couple_kissing_sound_effect.mp3"
                                show sc movienightariel l104
                                with dissolve
                                pause 1.0
                                a"Mmm..."
                                show sc movienightariel l105
                                with dissolve
                                pause 1.0
                                #The MC and Ariel share a kiss

                                #They retract the kiss, look at each other, then kiss again
                                #ADD A HOT KISS ANIMATION HERE
                                stop sound fadeout 1.0
                                show sc movienightariel l106
                                with dissolve
                                mc"Night, [a_name]."
                                #she smiles after they stop kissing and then says goodnight

                                #Go Down to “scene continues"
                            else:
                                show sc movienightariel l079
                                mc"Night, [a_name]."
                                #scene continues
                                #The MC watches Ariel head towards the staircase and leave, she smiles back at him

                            #screen goes blank
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            #END SCENE



        "Horror":
            show sc movienightariel l107
            mc"{i}The Bloodening?{/i}"
            show sc movienightariel l108
            a"Oh..."
            show sc movienightariel l109
            a"What's it about?"
            show sc movienightariel l021a
            mc"It's about four mysterious blond-haired children with Scottish accents and strange powers, including mind control, telepathy and telekinesis."
            mc"When their powers activate, their eyes glow with a piercing blue color."
            show sc movienightariel l112
            a"Oh... It doesn't sound like my kind of film."
            show sc movienightariel l113
            mc"Nah, I'm sure it will be fine."
            show sc movienightariel l114
            mc"If you were watching it alone, then I'd understand."
            show sc movienightariel l115
            mc"But seeing as I'll be watching it with you, you'll be okay. I promise."
            show sc movienightariel l116
            a"All right, if you say so..."
            #Ariel looks concerned
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            centered "A little later on...{w=2.0}{nw}" with dissolve
            show text "A little later on..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
            scene bg black with Dissolve(1)
            pause 1.0
            #this comes up on the screen while Ariel is simply sitting next to the MC on the sofa in a now, dimly lit room
            play music "sound effects/02/Whispers in the Dark.mp3" loop fadein 1.0
            show sc movienightariel l117
            with dissolve
            pause 2.0
            show sc movienightariel l118
            with dissolve
            movie_kid1"{i}But you're the one who's been doing terrible things.{/i}"
            #the characters on the screen speak as the MC and Ariel watch
            show sc movienightariel l117
            movie_kid1"{i}You've been fooling around with the minister's daughter, haven't you?{/i}"
            show sc movienightariel l118
            movie_man"{i}But, but... How on earth do you know that?{/i}"
            show sc movienightariel l119
            movie_kid1"{i}We know all your secrets.{/i}" (multiple=2)
            movie_kid2"{i}We know all your secrets.{/i}" (multiple=2)
            show sc movienightariel l120
            movie_kid2"{i}And Doctor...{/i}"
            movie_kid2"{i}We know that you've been having it off with the local blacksmith's wife when she comes in for her monthly checkup.{/i}"
            #[Negative feedback / Positive feedback]
            menu:
                "Negative feedback":
                    show sc movienightariel l122
                    with dissolve
                    mc"Aw, really?"
                    #the MC looks pissed off with the film
                    show sc movienightariel l127
                    a"What's wrong?"
                    #Ariel turns to the MC
                    show sc movienightariel l125
                    mc"What's wrong?"
                    show sc movienightariel l126
                    mc"This whole storyline."
                    show sc movienightariel l123
                    mc"It's almost a complete rip-off of another film that I'm sure I've seen recently."
                    show sc movienightariel l033
                    mc"They've copied it almost word for word."
                    show sc movienightariel l024
                    a"I know, but it's just a movie."
                    show sc movienightariel l016
                    a"The kids are a little freaky, but it's not as scary as I thought it would be."
                    show sc movienightariel l128
                    mc"Well, that's a big part of the problem."
                    show sc movienightariel l122
                    mc"It's not scary enough."
                    show sc movienightariel l107
                    mc"It's more of a comedy than a horror. The dialogue is just laughable."
                    show sc movienightariel l114
                    mc"I know nothing about screenplays, but even I could write a better script than this."
                    show sc movienightariel l124
                    a"Hmm..."
                    $ v_ep01_ariel_arrogant_counter += 1
                    #Ariel looks down
                    show sc movienightariel l127
                    a"Anyway, it's getting kind of late, so I think I'm gonna go to bed."
                    stop music fadeout 2.0
                    #she looks up at him and speaks
                    show sc movienightariel l046
                    mc"But there's still more of the movie to go."
                    show sc movienightariel l047
                    a"I know, but [mc_vic_address] and [mc_v_address ] will be home any minute now."
                    show sc movienightariel l048
                    a"So maybe it's best if we call it a night."
                    show sc movienightariel l049
                    mc"Yeah, that would probably be wise."
                    show sc movienightariel l155
                    with dissolve
                    a"Thanks for inviting me to watch a movie with you, [y_name]."
                    #Ariel stands up
                    show sc movienightariel l050
                    a"And sorry that you didn't enjoy it."
                    show sc movienightariel l052
                    a"Goodnight."
                    show sc movienightariel l079
                    with dissolve
                    mc"Night, [a_name]..."
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                    #END SCENE


                "Positive feedback"(wt="Best option"):
                    show sc movienightariel l054
                    a"So, what do you think so far?"
                    show sc movienightariel l122
                    mc"It's been okay. It's not entirely original, and the influences of other films are evident, but it's at the very least watchable."
                    show sc movienightariel l126
                    mc"How about you?"
                    show sc movienightariel l129
                    a"I honestly don't know what I was so worried about."
                    show sc movienightariel l112
                    a"Sure, the kids are a little freaky, but it's not as scary as I thought it would be."
                    show sc movienightariel l021
                    mc"Yeah, it's almost comedic the way they are being portrayed."
                    show sc movienightariel l109
                    a"Yeah, you're right."
                    $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                    show sc movienightariel l110
                    mc"Anyway, let's get back to the movie, and find out what happens next!"
                    $ v_ep01_ariel_respect_counter += 1
                    show sc movienightariel l061
                    a"Yeah, good idea..."
                    stop music fadeout 1.0
                    #screen goes blank
                    scene black
                    with dissolve
                    scene black
                    with Pause (2)

                    #the scene returns with Ariel snuggling up against the MC, resting her head on his shoulder, she's a little freaked out, as is the MC
                    play music "sound effects/02/Whispers in the Dark1.mp3" loop fadein 1.0
                    show sc movienightariel l130
                    with dissolve
                    mc"(...)"

                    #show Ariel resting her head on his chest/shoulder
                    show sc movienightariel l131
                    mc"(This movie took a really fucked-up turn!)"
                    show sc movienightariel l132
                    movie_man"{i}Help me!!{/i}"
                    movie_man"{i}Their eyes... Their eyes are sucking away my will to live!!{/i}"
                    show sc movienightariel l133
                    a"Oh!!"
                    show sc movienightariel l134
                    a"I can't watch!"
                    #Ariel closes her eyes

                    #Tease the player by not showing what is happening on the TV screen
                    #[Continue watching the movie / Put your arm around her]
                    show sc movienightariel l135
                    with dissolve
                    pause 1.0
                    menu:
                        "Continue watching the movie":
                            show sc movienightariel l136
                            with dissolve
                            pause 1.0
                            #show Ariel closing her eyes and hugging the MC tight as he continues watching the film
                            #screen goes blank
                            stop music fadeout 1.0
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)

                            show sc movienightariel l137
                            mc"Well, that was pretty good. Did you like it?"
                            #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                            #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen
                            show sc movienightariel l138a
                            a"No... It scared the shit out of me!"
                            show sc movienightariel l139a
                            mc"Haha! So much for not being as scary as you thought it would be, huh?"
                            #Ariel looks annoyed
                            show sc movienightariel l140a
                            a"Yeah, well... It wasn't that scary."
                            show sc movienightariel l141a
                            a"But did they really need to kill all those people?"
                            show sc movienightariel l142a
                            mc"Maybe not, but it was a horror film, after all."
                            show sc movienightariel l143a
                            a"I suppose..."
                            show sc movienightariel l084
                            a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                            show sc movienightariel l141
                            a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                            show sc movienightariel l143
                            a"So maybe you should too."
                            show sc movienightariel l142
                            mc"Yeah, that would probably be wise."
                            show sc movienightariel l067
                            with dissolve
                            a"Thanks for inviting me to watch a movie with you, [y_name]."
                            #Ariel stands up
                            show sc movienightariel l073
                            mc"You're welcome."
                            show sc movienightariel l074
                            with dissolve
                            mc"Perhaps we could do it again sometime?"
                            show sc movienightariel l155
                            a"Just no more horror films, please."
                            show sc movienightariel l156
                            mc"You got it!"
                            show sc movienightariel l154
                            a"Goodnight, [y_name]."
                            #she gives a half-hearted smile to the MC
                            show sc movienightariel l079
                            mc"Night, [a_name]..."
                            #The MC watches Ariel head towards the staircase and leave
                            #screen goes blank
                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                            #END SCENE


                        "Put your arm around her"(wt="Best option"):
                            #The MC subtly puts an arm around Ariel
                            show sc movienightariel l144
                            mc"Come here..."
                            show sc movienightariel l145
                            a"Mmm..."
                            #Ariel smiles and continues to watch the movie
                            #+1 ARIEL POINT
                            $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                            show sc movienightariel l146
                            mc"This will help."
                            #the MC looks down at Ariel's chest
                            show sc movienightariel l147
                            with dissolve
                            pause 1.0
                            #show Ariel and the MC watching the film - Ariel bites her bottom lip, as she looks down at the MC's bulge in his pants
                            #[Continue watching the movie / Make a move]
                            #NOTE: The “Make a move" option will only be available if the player has at least ONE ARIEL HEART by this point

                            menu:
                                "Continue watching the movie":
                                    show sc movienightariel l083
                                    with dissolve
                                    pause 1.0
                                    #show the MC continuing to watch the film with Ariel glancing up at him, while he looks away, trying to pretend he doesn't have an erection
                                    #screen goes blank
                                    stop music fadeout 1.0
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)

                                    show sc movienightariel l137a
                                    with dissolve
                                    mc"Well, that was pretty good. Did you like it?"
                                    #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                                    #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen
                                    show sc movienightariel l138
                                    a"No... It scared the shit out of me!"
                                    show sc movienightariel l139
                                    mc"Haha! So much for not being as scary as you thought it would be, huh?"
                                    #Ariel looks annoyed
                                    show sc movienightariel l140
                                    a"Yeah, well... It wasn't that scary."
                                    show sc movienightariel l141
                                    a"But did they really need to kill all those people?"
                                    show sc movienightariel l142
                                    mc"Maybe not, but it was a horror film, after all."
                                    show sc movienightariel l143
                                    a"I suppose..."
                                    show sc movienightariel l067a
                                    a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                                    show sc movienightariel l086
                                    a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                                    show sc movienightariel l087
                                    a"So maybe you should too."
                                    show sc movienightariel l090
                                    mc"Yeah, that would probably be wise."
                                    show sc movienightariel l067a
                                    with dissolve
                                    a"Thanks for inviting me to watch a movie with you, [y_name]."
                                    #Ariel stands up
                                    mc"You're welcome."
                                    show sc movienightariel l074
                                    with dissolve
                                    mc"Perhaps we could do it again sometime?"
                                    show sc movienightariel l155
                                    a"Just no more horror films, please."
                                    show sc movienightariel l156
                                    mc"You got it!"
                                    show sc movienightariel l154
                                    a"Goodnight, [y_name]."
                                    #she gives a half-hearted smile to the MC
                                    show sc movienightariel l079
                                    with dissolve
                                    mc"Night, [a_name]..."
                                    #The MC watches Ariel head towards the staircase and leave
                                    #screen goes blank
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)
                                    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
                                    #END SCENE


                                "Make a move"(wt="Best option"):
                                    #show consecutive images of the MC's hand moving from its place on Ariel's hip/waist and cupping under her breast
                                    show sc movienightariel l147a
                                    with dissolve
                                    pause 2.0
                                    $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                                    show sc movienightariel l092
                                    a"{i}(*Whispering*){/i}\nOhh..."
                                    #Ariel murmurs but never takes her eyes off the screen
                                    #+1 ARIEL POINT

                                    #[Squeeze her breast / Continue watching the film]

                                    menu:
                                        "Squeeze her breast"(wt="Best option"):
                                            #show an animation of the MC fondling her breast
                                            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                                                show sc movienightariel breast fondle
                                            else:
                                                show sc movienightariel l094
                                            a"(Oh!!)"
                                            show sc movienightariel l095
                                            a"Er... Um..."
                                            #Ariel moves so that the MC's hand slips from her chest
                                            show sc movienightariel l096
                                            mc"Everything okay?"
                                            show sc movienightariel l097
                                            a"Y-yeah.. My leg started to fall asleep and I just had to move to wake it up."
                                            show sc movienightariel l098
                                            mc"Oh, all right."
                                            show sc movienightariel l099
                                            a"I'm fine now. Let's get back to watching the movie."
                                            #Ariel rests her head back on the MC's shoulder/chest
                                            #+1 ARIEL POINT
                                            $ v_ep02_03_11_movie_date_with_ariel_counter += 1
                                            show sc movienightariel l100
                                            with dissolve
                                            pause 1.0
                                            #final shot here of the MC continuing to watch the film with Ariel glancing up at him, smiling
                                            #screen goes blank
                                            stop music fadeout 1.0
                                            scene black
                                            with dissolve
                                            scene black
                                            with Pause (2)


                                        "Continue watching the film":
                                            show sc movienightariel l101
                                            with dissolve
                                            pause 1.0
                                            #final shot here of the MC continuing to watch the film with Ariel glancing up at him, smiling
                                            show sc movienightariel l102
                                            a"Um... Let's not take things too far, [y_name]."
                                            #She removes her hand
                                            show sc movienightariel l103
                                            mc"Oh, sure thing, [a_name]."
                                            #Ariel gives the MC an awkward smile
                                            show sc movienightariel l100
                                            with dissolve
                                            pause 1.0
                                            stop music fadeout 1.0
                                            scene black
                                            with dissolve
                                            scene black
                                            with Pause (2)



                                    show sc movienightariel l137a
                                    with dissolve
                                    mc"Well, that was pretty good. Did you like it?"
                                    #show this angle - https://pixhost.to/show/206/499488524_screenshot-2024-07-30-at-10-29-32-pm.jpg
                                    #a shot from behind the MC and Ariel looking at the TV, the end credits are on the screen
                                    show sc movienightariel l138
                                    a"No... It scared the shit out of me!"
                                    show sc movienightariel l139
                                    mc"Haha! So much for not being as scary as you thought it would be, huh?"
                                    #Ariel looks annoyed
                                    show sc movienightariel l140
                                    a"Yeah, well... It wasn't that scary."
                                    show sc movienightariel l141
                                    a"But did they really need to kill all those people?"
                                    show sc movienightariel l142
                                    mc"Maybe not, but it was a horror film, after all."
                                    show sc movienightariel l143
                                    a"I suppose..."
                                    show sc movienightariel l067a
                                    a"Anyway, it's pretty late, so I think I'm gonna go to bed."
                                    show sc movienightariel l086
                                    a"Plus [mc_vic_address] and [mc_v_address ] will be home any minute now."
                                    show sc movienightariel l087
                                    a"So maybe you should too."
                                    show sc movienightariel l090
                                    mc"Yeah, that would probably be wise."
                                    show sc movienightariel l067a
                                    with dissolve
                                    a"Thanks for inviting me to watch a movie with you, [y_name]."
                                    if v_ep02_03_11_movie_date_with_ariel_counter >= 4:
                                        $ ariel_love_level +=1
                                        $ v_ep02_ariel_hearts_counter += 1
                                    #Ariel stands up
                                    mc"You're welcome."
                                    show sc movienightariel l074
                                    with dissolve
                                    mc"Perhaps we could do it again sometime?"
                                    show sc movienightariel l155
                                    a"Just no more horror films, please."
                                    show sc movienightariel l156
                                    mc"You got it!"
                                    show sc movienightariel l077
                                    a"Mmm..."
                                    show sc movienightariel l078
                                    a"Goodnight."

                                    #Go Down to “scene continues"
                                    #If the player has 5 Ariel points or more for this task
                                    #Make sure it's coded to accommodate any extra points that may have been allocated
                                    if v_ep02_03_11_movie_date_with_ariel_counter == 5:
                                        play sound "sound effects/01/couple_kissing_sound_effect.mp3"
                                        show sc movienightariel l104
                                        with dissolve
                                        pause 0.5
                                        show sc movienightariel l105
                                        with dissolve
                                        a"Mmm..."
                                        pause 1.5

                                        #The MC and Ariel share a kiss

                                        #They retract the kiss, look at each other, then kiss again
                                        #ADD A HOT KISS ANIMATION HERE
                                        stop sound fadeout 1.0
                                        show sc movienightariel l106
                                        with dissolve
                                        mc"Night, [a_name]."
                                        #she smiles after they stop kissing and then says goodnight
                                    else:
                                        show sc movienightariel l079
                                        with dissolve
                                        mc"Night, [a_name]."
                                        scene black
                                        with dissolve
                                        scene black
                                        with Pause (2)

                                    #scene continues
                                    #The MC watches Ariel head towards the staircase and leave, she smiles back at him
                                    #screen goes blank
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)


    if persistent.v_secrets_enabled and persistent.v_secrets_ep02_03_11_1:
        $ v_ep02_ariel_fantasy_counter += 1
        jump lb_ep02_03_11_The_MC_watches_a_movie_with_Ariel_fantasy
    else:
        jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan

label lb_ep02_03_11_The_MC_watches_a_movie_with_Ariel_fantasy:
    if not _in_replay:
        scene img_secret_scene_overlay onlayer anim_layer
        with { "anim_layer": dissolve}
    else:
        show screen scr_end_replay
    #START OF THE ARIEL NON-CANON SCENE (Bonus Scene)
    #the scene starts with Ariel asleep in her bed. Make sure the lighting is dimmed
    centered "Later that night...{w=2.0}{nw}" with dissolve
    show text "Later that night..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/02/In My Dreams.mp3" loop fadein 1.0
    show sc arieldreamtv a00
    with dissolve
    a"Mmm..."
    #She looks like she's struggling to sleep
    show sc arieldreamtv a00a
    with dissolve
    pause 1.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv breast fondle1
    else:
        show sc arieldreamtv a00b
    with dissolve
    a"Nghh..."
    show sc arieldreamtv a00c
    with dissolve
    show sc arieldreamtv a00c
    with dissolve
    pause 0.8
    show sc arieldreamtv a00ca
    with dissolve
    pause 0.8
    show sc arieldreamtv a00cb
    with dissolve
    pause 0.8
    play sex1 "sound effects/01/sex/ariel_moan_loop2.ogg" loop fadein 1.0
    show sc arieldreamtv a00cc
    with dissolve
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv rub1
    else:
        show sc arieldreamtv a00d
    with dissolve
    pause 2.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv rub2
    else:
        show sc arieldreamtv a00e
    with dissolve
    pause 2.0
    #The screen fizzles as it shows inside Ariel's dream

    #The scene continues with the MC and Ariel back on the sofa again, watching the movie
    #Ariel snuggles up against the MC, resting her head on his shoulder

    #show Ariel resting her head on his chest/shoulder
    stop sex1 fadeout 1.0
    scene black
    with flash(0.50, 0, 0.75, "#fff")
    show sc arieldreamtv a01
    with dissolve
    a"This movie is pretty intense, huh?"
    show sc arieldreamtv a02
    mc"Yeah, it sure is."
    show sc arieldreamtv a03
    a"Do you kiss girls like the guy in the film?"
    show sc arieldreamtv a04
    mc"Nah, he's just an actor."
    mc"The way I do it is more realistic."
    show sc arieldreamtv a06
    a"Show me..."
    show sc arieldreamtv a05
    mc"With pleasure."
    play sound "sound effects/01/couple_kissing_sound_effect.mp3"
    show sc arieldreamtv a07
    a"Mmm..."
    #the MC and Ariel make out on the sofa
    a"(This is so hot!)"
    #the MC and Ariel tongue kiss
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv breast fondle2
    else:
        show sc arieldreamtv a08
    a"Ohh..."
    #The MC kisses Ariel's neck and cups one of her breasts
    stop sound fadeout 1.0
    mc"Do you like that, [a_name]?"
    show sc arieldreamtv a10
    a"Oh yeah..."
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv pussy rub
    else:
        show sc arieldreamtv a09
    mc"And how about this?"
    #the MC rubs Ariel's between her legs, while she still has her underwear on
    a"NGHH!"
    #She bites her bottom lip
    show sc arieldreamtv a03
    with dissolve
    a"Oh [y_name]!"
    show sc arieldreamtv a04
    mc"Do you wanna do some of what they're doing in the film?"
    show sc arieldreamtv a06
    a"Where should we begin?"
    show sc arieldreamtv a05
    mc"Simple."
    mc"Stand in front of me and start taking off your clothes."
    show sc arieldreamtv a06
    a"Okay."
    #Ariel stands before the MC while he sits on the sofa watching her

    #show Ariel sliding off her nightwear shorts

    #show Ariel lifting up her top over her head, and then off her body

    #she now stands in her underwear - bra and panties
    show sc arieldreamtv a11
    with dissolve
    pause 1.5
    show sc arieldreamtv a12
    with dissolve
    pause 1.0
    show sc arieldreamtv a13
    with dissolve
    pause 1.0
    show sc arieldreamtv a14
    with dissolve
    pause 1.0
    show sc arieldreamtv a15
    with dissolve
    pause 1.0
    show sc arieldreamtv a16
    with dissolve
    pause 1.0
    show sc arieldreamtv a17
    with dissolve
    a"Do you like what you see?"

    #ROLLING IMAGE HERE
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene wip_ep02_arieldreamtv_01 at tt_top
        pause 1.0
    elif True:
        show sc arieldreamtv a16
    mc"Oh yeah."
    scene sc arieldreamtv a18
    mc"Damn, [a_name]!"
    #show a shot from behind Ariel so we can see her ass in the shot and the MC staring at her
    show sc arieldreamtv a19
    a"You're sizzling!"
    show sc arieldreamtv a16
    mc"Now come to me. Hop aboard."
    #Ariel climbs on top of the MC - show her sitting in the MC's lap
    play sound "sound effects/01/couple_kissing_sound_effect.mp3"
    show sc arieldreamtv a20
    with dissolve
    a"Mmm..."
    #the MC and Ariel kiss
    #he cups her ass in his hands while they make out
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv grind
    else:
        show sc arieldreamtv a21
    with dissolve
    a"Oh [y_name]..."
    #show Ariel and the MC face-to-face, her mouth open to speak
    show sc arieldreamtv a22
    with dissolve
    pause 1.0
    show sc arieldreamtv a23
    with dissolve
    pause 1.0
    show sc arieldreamtv a28
    with dissolve
    pause 1.0
    stop sound fadeout 1.0
    #show Ariel's panty-clad pussy pressed against the MC's erection
    #ANIMATED SCENE of Ariel grinding on his cock while they continue to make out
    show sc arieldreamtv a24
    with dissolve
    a"I can feel you... down below."
    show sc arieldreamtv a27
    mc"And what do you plan to do about it?"
    #show Ariel's face
    show sc arieldreamtv a25
    a"I want to make it all mine."
    #Ariel cups her hand over his crotch
    show sc arieldreamtv a26
    mc"Then take it out of my pants and slide your virgin pussy down upon it."
    show sc arieldreamtv a22
    with dissolve
    a"Mmm..."
    $ renpy.music.set_volume(0.0, 0.0, channel="sex1")
    play sex1 "sound effects/01/sex/ariel_climax.mp3"
    show sc arieldreamtv a23a
    with dissolve
    pause 1.0
    show sc arieldreamtv a23b
    with dissolve
    pause 1.0
    #the MC and Ariel kiss again
    #A flash on the screen as Ariel wakes up from her dream
    scene black
    with flash(0.25, 0, 0.75, "#fff")
    stop music fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, channel="sex1")
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv rub4
    else:
        show sc arieldreamtv a00k
    pause 2.0
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        show sc arieldreamtv rub3
    else:
        show sc arieldreamtv a00f
    with vpunch
    pause 1.0
    with vpunch
    pause 1.0
    with vpunch
    pause 1.0
    with vpunch
    pause 2.0
    #She rises up
    #stop sex1 fadeout 1.0
    show sc arieldreamtv a00g
    with dissolve
    a"Oh my God!!"
    stop sex1 fadeout 1.0
    #she looks down at her hands - one is cupping her breast, the other is inside her underwear
    show sc arieldreamtv a00h
    with dissolve
    pause 1.0
    #She removes them
    show sc arieldreamtv a00j
    with dissolve
    a"(What on earth was I dreaming about??)"
    #Ariel stares in shock as the screen fades to black
    #screen goes blank
    scene onlayer anim_layer
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ persistent.replay_ep02_ariel_moviedate_fantasy = False
    $ renpy.end_replay()
    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
    #END OF THE ARIEL NON-CANON SCENE

init:
    $ v_ep3_park_with_zora_hername = ""
    $ v_ep3_park_with_zora_thesession = ""
    $ v_ep3_park_with_zora_atthegym = ""
    $ v_ep3_park_with_zora_counter = 0
    $ v_ep03_02_01_standing_up_for_Zora = 0

label lb_ep03_02_01_Training_in_The_Park_with_Zora:
    centered "The next morning...{w=2.0}{nw}" with dissolve
    show text "The next morning..."
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
    #park ambience required here
    scene sc zoratrainingpark g001
    with dissolve
    pause 2.0
    #Start with the MC waiting at the local park in his fitness gear
    #He looks around, hands on his hips

    show sc zoratrainingpark g002
    with dissolve
    pause 2.0
    #Zora arrives in her fitness gear. she’s wearing a new outfit compared to what she wears at the gym
    #https://thumbs.dreamstime.com/b/body-positive-plus-size-plump-woman-athlete-jogging-fitness-outfit-her-trainer-park-body-positive-plus-size-plump-woman-325729867.jpg
    #make sure this time she’s wearing an exercise bra under her top to push her breasts up more
    #so that she’s more eye-catching this time
    zora"Hey [y_name]!"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc zoratrainingpark g003 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc evescenemcviv f006
        with dissolve
        pause 2.0
    scene sc zoratrainingpark g005
    zora"Sorry, I’m late."
    show sc zoratrainingpark g006
    mc"No, no. Your timing is great."
    mc"I was just doing some warm-ups before we get started."
    mc"How was your morning?"
    show sc zoratrainingpark g007
    zora"It was okay. I slept in after studying until late last night but still had some time to get in a quick yoga session before leaving the house."
    show sc zoratrainingpark g008
    zora"How about you?"
    show sc zoratrainingpark g009
    mc"Pretty good. Like yourself, a late night, but the allure of the clean crisp morning air is enough to get me raring to go for a workout in the park."
    show sc zoratrainingpark g010
    mc"So have you been here before?"
    show sc zoratrainingpark g011
    zora"We’ve driven past it a few times, but this is the first time setting foot in here."
    show sc zoratrainingpark g010
    mc"When you say we, do you mean you and your parents?"
    show sc zoratrainingpark g012
    zora"Uh-huh."
    show sc zoratrainingpark g013
    zora"And because this park isn’t close to home, it’s rare for me to be out this way."
    show sc zoratrainingpark g009
    mc"Of course."
    show sc zoratrainingpark g010
    mc"And I see you have a different outfit."
    #Zora looks down at her clothing
    #ROLLING SCREEN OF ZORA IN HER FITNESS CLOTHING
    show sc zoratrainingpark g011
    zora"Oh, right..."
    show sc zoratrainingpark g014
    zora"I had a look online to see what would be more appropriate for me to wear for a jog so I wouldn’t seem out of place."
    mc"You look great. And after our warm-up, you’ll look like you’ve been jogging around here for months!"
    show sc zoratrainingpark g015
    zora"Thanks..."
    show sc zoratrainingpark g015a
    zora"I like what you have on too. Very trendy."
    show sc zoratrainingpark g016
    mc"I try and keep up with what’s in with fashion as well you know."
    show sc zoratrainingpark g017
    zora"Haha, I’m sure."
    show sc zoratrainingpark g018
    mc"Okay, is it safe to presume that you won’t be required to do any stretches after you did some yoga before coming here?"
    show sc zoratrainingpark g019
    zora"Yeah, I’m all set."
    mc"Alrighty then."
    show sc zoratrainingpark g020
    mc"Let’s go for a short jog and then we can talk some more when we take a break..."
    play sound "sound effects/01/jogging_in_the_park.ogg" loop fadein 1.0
    show sc zoratrainingpark g021
    with dissolve
    pause 1.5
    #A montage of the MC and Zora jogging through the park - no dialogue, just images
    show sc zoratrainingpark g022
    with dissolve
    pause 1.5
    #show them jogging side by side along the park trail
    show sc zoratrainingpark g023
    with dissolve
    pause 1.5
    #show the upper half of their bodies - from head to chest areas
    show sc zoratrainingpark g024
    with dissolve
    pause 1.5
    #show the lower half of their bodies - from stomach to knee height
    show sc zoratrainingpark g025
    with dissolve
    pause 1.5
    #show a side shot of them jogging
    show sc zoratrainingpark g026
    with dissolve
    pause 1.5
    #show a behind shot of them jogging - full-body
    #Show a close-up of Zora’s ass in her new fitness clothing
    #show one final shot of them from behind - jogging in the distance on the park trail before the screen fades
    #screen goes blank
    stop sound fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    centered "Fifteen minutes later...{w=2.0}{nw}" with dissolve
    show text "Fifteen minutes later..."
    scene bg black with Dissolve(1)
    pause 1.0
    #they stand by a water fountain, sweating and then talking
    play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
    show sc zoratrainingpark g027
    with dissolve
    zora"Wow-wee..."
    #She places her hand on her chest
    show sc zoratrainingpark g028
    with dissolve
    zora"I can feel my heart racing so fast!"
    show sc zoratrainingpark g029
    mc"Yeah, even a half-tempo jog really gets the blood pumping."
    show sc zoratrainingpark g030
    mc"Now we’re just going to rest and stretch for a little while and then go again."


label lb_ep3_02_01_chat_with_Zora_menu:

    #[Her name / The session / At the gym]
    if v_ep3_park_with_zora_counter < 3:
        menu:
            "Her name"(wt="Bonus Image - Only if you choose this option first") if v_ep3_park_with_zora_hername == "" and v_ep3_park_with_zora_counter == 0:
                jump lb_ep3_02_01_chat_with_Zora_menu_her_name
            "Her name" if v_ep3_park_with_zora_hername == "" and v_ep3_park_with_zora_counter != 0:
                jump lb_ep3_02_01_chat_with_Zora_menu_her_name

                label lb_ep3_02_01_chat_with_Zora_menu_her_name:
                    $ v_ep3_park_with_zora_counter += 1
                    $ v_ep3_park_with_zora_hername = v_ep3_park_with_zora_counter
                    show sc zoratrainingpark g031
                    mc"So I’ve been meaning to ask you about your name."
                    mc"It’s very unusual but incredibly unique."
                    mc"Why did your parents choose Zora?"
                    show sc zoratrainingpark g032
                    zora"Oh, it’s been a very long time since anyone has asked me that."
                    show sc zoratrainingpark g033
                    zora"Well... The truth is, it’s not my birth name."
                    zora"My real name is Brunhilde."
                    show sc zoratrainingpark g034
                    mc"Oh, really?"
                    show sc zoratrainingpark g035
                    zora"Yeah, my family has German roots, you see."
                    show sc zoratrainingpark g036
                    zora"My parents named me after a very well-known legend in Germany."
                    show sc zoratrainingpark g037
                    mc"And who was Brunhilde?"
                    show sc zoratrainingpark g038
                    zora"She was a mighty female warrior and one of the Valkyries."
                    show sc zoratrainingpark g039
                    mc"The Valkyries?"
                    if v_ep3_park_with_zora_hername == 1:
                        $ rewards_unlock ("zora",5)
                    mc"That's the Norse mythology if I’m not mistaken!"
                    show sc zoratrainingpark g040
                    zora"That’s right!"
                    show sc zoratrainingpark g041
                    zora"How did you know?"
                    show sc zoratrainingpark g042
                    mc"I’m pretty sure I studied a bit about it in high school."
                    show sc zoratrainingpark g043
                    zora"Awesome."
                    show sc zoratrainingpark g044
                    zora"Anyway, Brunhilde is a very ancient name and the older I got, the more I grew to dislike it."
                    show sc zoratrainingpark g045
                    zora"Kids would tease me about my name and one girl in particular, who knew all about her story, would call me Rote Zora, which is based on a film figure."
                    show sc zoratrainingpark g046
                    zora"Then other kids would try and harass me with this name."
                    show sc zoratrainingpark g047
                    mc"That doesn’t sound so bad."
                    show sc zoratrainingpark g048
                    zora"And you’d be right."
                    show sc zoratrainingpark g049
                    zora"I grew to like the name after I looked up the story about Rote Zora, also known as, \"Red Zora\"."
                    show sc zoratrainingpark g050
                    mc"What was so special about her?"
                    show sc zoratrainingpark g051
                    zora"It’s a story about a strong girl leading a gang of boys, similar to the story of Robin Hood."
                    show sc zoratrainingpark g052
                    mc"So like stealing from the rich to give to the poor?"
                    show sc zoratrainingpark g053
                    zora"More like, stealing from the rich, to survive and to not starve."
                    show sc zoratrainingpark g054
                    zora"She and her people were being hunted and her main goal was to not get caught, while also trying to live her life."
                    show sc zoratrainingpark g055
                    zora"So because of her story, I always wanted to be like her, and then the nickname Zora just kind of stuck for me."
                    show sc zoratrainingpark g049
                    zora"And the kids at school stopped giving me a hard time."
                    show sc zoratrainingpark g042
                    mc"That’s one hell of a story."
                    mc"You know, you should consider getting it legally changed to Zora."
                    show sc zoratrainingpark g043
                    zora"That’s a great idea!"
                    show sc zoratrainingpark g046
                    zora"Though I’m not sure how my parents would feel about that."
                    #Zors seems unsure
                    show sc zoratrainingpark g047
                    mc"Well, you’re of legal age to make that decision for yourself."
                    mc"You should definitely do it."
                    show sc zoratrainingpark g052
                    mc"And Zora is a much cooler name than Brunhilde!"
                    show sc zoratrainingpark g055
                    zora"Haha, thanks."
                    show sc zoratrainingpark g048
                    zora"I think you’ve convinced me."
                    show sc zoratrainingpark g030
                    mc"Glad I could help."

            "The session" if v_ep3_park_with_zora_thesession ==  "":
                $ v_ep3_park_with_zora_counter += 1
                $ v_ep3_park_with_zora_thesession = v_ep3_park_with_zora_counter
                show sc zoratrainingpark g031
                mc"How are you finding the session so far?"
                show sc zoratrainingpark g033
                zora"It’s been okay."
                show sc zoratrainingpark g045
                zora"It’s been so long since I went jogging or running."
                show sc zoratrainingpark g046
                zora"What seems easy for you is very strenuous for me."
                show sc zoratrainingpark g047
                mc"That’s to be expected."
                mc"But the more you do it, like anything, the easier it gets."
                mc"In saying that, if at any point during our workout, you feel it’s becoming too much, let me know, and we’ll do something else, okay?"
                show sc zoratrainingpark g048
                zora"Sure, that would be great."
                show sc zoratrainingpark g030
                mc"Sweet!"

            "At the gym" if v_ep3_park_with_zora_atthegym ==  "":
                $ v_ep3_park_with_zora_counter += 1
                $ v_ep3_park_with_zora_atthegym = v_ep3_park_with_zora_counter
                show sc zoratrainingpark g050
                mc"How did you feel after our session together at the gym?"
                show sc zoratrainingpark g048
                zora"At first I felt pretty good, but later on that night my arms and legs felt like boulders."
                show sc zoratrainingpark g046
                zora"I found it difficult to move or lift my arms up high."
                show sc zoratrainingpark g047
                mc"That’s a normal reaction after a tough first workout."
                show sc zoratrainingpark g045
                zora"My back was a little sore too. But maybe that’s just my bad posture."
                show sc zoratrainingpark g039
                mc"Again, it’s something we can work on."
                show sc zoratrainingpark g042
                mc"Is your back sore now?"
                show sc zoratrainingpark g033
                zora"I can feel a mild throb in my lower back, but nothing too serious."
                show sc zoratrainingpark g030
                mc"I see."
                #[Offer to check / Go and ahead and check]
                menu:
                    "Offer to check"(wt="Best option"):
                        show sc zoratrainingpark g034
                        mc"Would you like me to check?"
                        show sc zoratrainingpark g046
                        zora"Oh, only if you want to."
                        show sc zoratrainingpark g056
                        mc"Yeah, it’s no problem at all."
                        $ v_ep03_02_01_standing_up_for_Zora +=1
                        $ v_ep01_zora_respect_counter += 1
                        #the MC stands behind her and presses against her lower back

                    "Go ahead and check"(wt="Bonus Image"):
                        show sc zoratrainingpark g042
                        mc"Allow me to check."
                        $ rewards_unlock ("zora",6)
                        show sc zoratrainingpark g046
                        zora"Oh..."
                        $ v_ep01_zora_cocky_counter += 1
                        #the MC stands behind her and presses against her lower back
                        show sc zoratrainingpark g056
                        zora"(I would’ve preferred that he asked me first.)"
                        #Zora looks uncomfortable

                #scene continues
                show sc zoratrainingpark g057
                zora"Oooh..."
                show sc zoratrainingpark g059
                mc"You feeling something there?"
                show sc zoratrainingpark g058
                zora"Yeah, right where you were pressing."
                show sc zoratrainingpark g061
                zora"Why is it still so sore?"
                show sc zoratrainingpark g061a
                mc"It could be a few things."
                mc"Lower back pain is often a result of a strain or injury to muscles or tendons in your back."
                show sc zoratrainingpark g057
                mc"Or it could be other things like arthritis, structural problems or even disk injuries."
                show sc zoratrainingpark g062
                zora"So what should I do to make it go away?"
                show sc zoratrainingpark g059
                mc"The pain often disappears with rest, physical therapy or medication, depending on how bad it is."
                mc"Did you feel this before our session the other day?"
                show sc zoratrainingpark g061
                zora"No, this one is new."
                mc"In that case, it could be your body just getting used to strenuous activity again."
                show sc zoratrainingpark g057
                mc"Don’t worry, in time and with more sessions, that soreness shouldn’t show up again."
                show sc zoratrainingpark g062
                zora"Okay."
                show sc zoratrainingpark g030
                mc"You'll be fine."
                #she responds and smiles
        jump lb_ep3_02_01_chat_with_Zora_menu


#scene continues after all 3 choices have been made
label lb_ep3_02_01_The_session_continues_with_Zora:
    scene black
    with dissolve
    scene black
    with Pause (2)
    show sc zoratrainingpark g063
    with dissolve
    mc"So when you’re ready, we can continue on with our jog."
    show sc zoratrainingpark g064
    zora"Sure. I’m just going to have some water before we go."
    show sc zoratrainingpark g063
    mc"No worries."
    show sc zoratrainingpark g065
    with dissolve
    pause 1.0
    #Zora bends down to use the water fountain and bumps into "Guy", from the Episode 1 park scene with Bella
    show sc zoratrainingpark g066
    with dissolve
    pause 1.3
    show sc zoratrainingpark g067
    "Excuse me, I believe I was here first."
    #Don’t show his face here, just his arms and the front of his body - IMPORTANT
    show sc zoratrainingpark g068a
    zora"Oh, I’m sorry. I didn’t see you there."
    #[Let it go / Say something]
    menu:
        "Let it go":
            show sc zoratrainingpark g069
            with dissolve
            pause 1.5
            $ v_ep01_zora_arrogant_counter += 1
            #the guy uses the drinking fountain while Zora stands and watches him
            show sc zoratrainingpark g061a
            with dissolve
            pause 1.5
            show sc zoratrainingpark g074
            with dissolve
            "It's all yours now."
            if v_ep01_04_01_Bella_Work_Date == True:
                show sc zoratrainingpark g072
                mc"(Oh, fuck... Not this asshole again.)"
                show sc zoratrainingpark g073
                guy"Hang on a second... It’s you!"
                show sc zoratrainingpark g074
                with dissolve
                guy"My mistake then, ladies first."
            else:
                show sc zoratrainingpark g073
                guy"Okay then."
                show sc zoratrainingpark g074
                guy"Ladies first, so be my guest."
        "Say something"(wt="Best option"):
            show sc zoratrainingpark g070
            with dissolve
            mc"Hey, buddy?"
            mc"Haven’t you ever heard of \"ladies first\"?"
            # Show the MC talking to Guy from behind him so he still can’t see his face
            $ v_ep01_zora_respect_counter += 1
            mc"Or are all those extra muscles in your head causing you to lack any manners?"
            $ v_ep03_02_01_standing_up_for_Zora +=1
            #scene continues with "Guy" looking up at the MC - the first time we see his face in this scene
            #This scene and options if the player DID NOT play the Bella \"Bonus Date\" scene in Episode 1 (he has never met Guy before)
            show sc zoratrainingpark g071
            with dissolve
            pause 1.5
            if v_ep01_04_01_Bella_Work_Date == True:
                show sc zoratrainingpark g072
                with dissolve
                mc"(Oh, fuck... Not this asshole again.)"
                show sc zoratrainingpark g073
                guy"Hang on a second... It’s you!"
                show sc zoratrainingpark g074
                with dissolve
                guy"My mistake then. As you said, ladies first."
            else:
                show sc zoratrainingpark g073
                guy"Okay then."
                show sc zoratrainingpark g074
                guy"As you said, ladies first, so be my guest."

    #this scene and options if the player played the Bella \"Bonus Date\" scene in Episode 1 (he’s met Guy before)
    if v_ep01_04_01_Bella_Work_Date == True:
        #he points at the water fountain for the MC
        show sc zoratrainingpark g075
        zora"You know this person?"
        #she addresses the MC
        show sc zoratrainingpark g076
        mc"Yeah, I’ve had the displeasure of meeting Guy here recently."
        #Guy checks out Zora
        show sc zoratrainingpark g061a
        guy"I see you’ve traded blonde bombshell in for 'Chunky Town'."
        show sc zoratrainingpark g078
        guy"You work fast."

        #[Trick him / Explain]
        menu:
            "Trick him"(wt="Best option"):
                show sc zoratrainingpark g102
                guy"You should come to a real gym. My gym."
                show sc zoratrainingpark g103
                guy"I could have you looking as hot as [b_name] in no time!"
                show sc zoratrainingpark g079
                mc"Speak of the devil."
                #the MC steps up to Guy, to intimidate him
                show sc zoratrainingpark g080
                mc"Here’s [b_name] now."
                #He looks past Guy’s shoulder, pretending to see Bella
                show sc zoratrainingpark g081
                guy"Really?"
                #Guy looks over his shoulder
                guy"But I don’t see her anywh-"
                play sound "sound effects/01/kick_to_the_gut.mp3" noloop
                show sc zoratrainingpark g082
                with vpunch
                #the MC moves forward and knees Guy in the nuts and he hits the ground, clutching at them
                play sound "sound effects/01/male_grunt_gut_punch.mp3" noloop
                guy"NGHH!!{w=1.0}{nw}"
                play sound2 "sound effects/01/male_moaning_in_pain1.mp3" noloop
                show sc zoratrainingpark g083
                with vpunch
                pause 0.5
                play sound3 "sound effects/01/Falling Over Sound Effect.mp3" noloop
                show sc zoratrainingpark g084
                with dissolve
                guy"Fuck!!"
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                stop sound3 fadeout 1.0
                mc"Now let’s try that again, and I suggest that you throw in an apology to the lady while you’re at it."
                show sc zoratrainingpark g085
                guy"Uhhh... Fuck you!"
                #he responds while on the ground
                play sound "sound effects/03/cracking_knuckles_effect.mp3" noloop
                show sc zoratrainingpark g086
                pause 1.0
                #the MC grabs on the hand not grabbing his crotch and bends it backwards
                play sound2 "sound effects/01/male_scream_sound_effect1.mp3" noloop
                show sc zoratrainingpark g087
                guy"Ahhh!"
                #he yells in pain
                mc"What was that?"
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                show sc zoratrainingpark g088
                guy"Sorry, I’m sorry miss for the insult and for stepping in front of you."
                show sc zoratrainingpark g089
                guy"It won’t happen again."
                show sc zoratrainingpark g090
                zora"Oh, thank you."
                show sc zoratrainingpark g091
                mc"Best you run along, Guy. That is, if you can."
                show sc zoratrainingpark g092
                guy"You just made yourself an enemy."
                #the MC looks at him menacingly
                show sc zoratrainingpark g093
                mc"Excuse me?"
                show sc zoratrainingpark g094
                guy"I meant, I’ll be going now."
                play sound "sound effects/01/jogging_in_the_park.ogg" fadein 1.0
                show sc zoratrainingpark g170
                with dissolve
                pause 1.5
                #MC turns to Zora
                show sc zoratrainingpark g096
                with dissolve
                mc"Are you okay?"
                stop sound fadeout 1.0
                show sc zoratrainingpark g097
                zora"Yeah, I’m fine."
                show sc zoratrainingpark g098
                zora"Thanks for standing up for me... Again."
                show sc zoratrainingpark g097
                zora"You’re making a habit of that."
                show sc zoratrainingpark g096
                mc"Something I’m more than happy to do, and as often as possible if you need me to."
                $ v_ep03_02_01_standing_up_for_Zora +=1
                #Zora smiles

            "Explain":
                show sc zoratrainingpark g100
                mc"There’s no trade. I’m her trainer, that’s it."
                #the MC steps up to Guy, to intimidate him
                #LAUGHING SOUND EFFECT
                play sound "sound effects/01/Male_Laughing_Sound_Effect.mp3"
                show sc zoratrainingpark g101
                guy"Haha! Really?"
                show sc zoratrainingpark g102
                guy"Girl, if he’s your trainer then you ain’t learning shit!"
                show sc zoratrainingpark g103
                guy"You should come to a real gym. My gym."
                show sc zoratrainingpark g104
                guy"I mean, look at you."
                stop sound fadeout 1.0
                show sc zoratrainingpark g077
                guy"This pipsqueak wouldn’t be able to train a mime artist let alone a girl of your si-"
                #Zora starts getting angry
                show sc zoratrainingpark g106
                zora"Hi-ya!!"
                #She moves towards Guy and kicks him in the nuts and he hits the ground, clutching at them
                play sound "sound effects/01/kick_to_the_gut.mp3" noloop
                show sc zoratrainingpark g105
                with vpunch
                play sound2 "sound effects/01/male_grunt_gut_punch.mp3" noloop
                guy"NGHH!!{w=1.0}{nw}"
                play sound3 "sound effects/01/male_moaning_in_pain1.mp3" noloop
                show sc zoratrainingpark g083
                with vpunch
                guy"Fuck!!"
                play sound "sound effects/01/Falling Over Sound Effect.mp3" noloop
                show sc zoratrainingpark g084
                mc"Woah..."
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                stop sound3 fadeout 1.0
                #the MC stands over him
                show sc zoratrainingpark g106
                zora"Say that again, \"Guy\"?"
                show sc zoratrainingpark g085
                guy"Uhhh... Fuck you!"
                #he responds while on the ground
                #the MC grabs the hand of Guy's that's not holding his crotch and bends it backwards
                play sound "sound effects/03/cracking_knuckles_effect.mp3" noloop
                show sc zoratrainingpark g086
                pause 1.0
                #the MC grabs on the hand not grabbing his crotch and bends it backwards
                play sound2 "sound effects/01/male_scream_sound_effect1.mp3" noloop
                show sc zoratrainingpark g087
                guy"Ahhh!"
                #he yells in pain
                mc"What was that?"
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                show sc zoratrainingpark g088
                guy"Okay, okay..."
                show sc zoratrainingpark g089
                guy"I’m sorry miss for the insult and for stepping in front of you."
                show sc zoratrainingpark g090
                guy"It won’t happen again."
                show sc zoratrainingpark g106
                zora"There, was that so difficult?"
                #Zora has her hands on her hips as she looks down at him
                show sc zoratrainingpark g092
                guy"You just made yourself an enemy."
                #the MC looks at him menacingly
                show sc zoratrainingpark g093
                mc"Excuse me?"
                show sc zoratrainingpark g094
                guy"I meant, I’ll be going now."
                #MC turns to Zora
                play sound "sound effects/01/jogging_in_the_park.ogg" fadein 1.0
                show sc zoratrainingpark g170
                with dissolve
                pause 1.5
                show sc zoratrainingpark g096
                with dissolve
                mc"Are you okay?"
                stop sound fadeout 1.0
                show sc zoratrainingpark g097
                zora"Yeah, I’m fine."
                show sc zoratrainingpark g099
                mc"Where on earth did that come from??"
                show sc zoratrainingpark g108
                zora"I... I don’t know."
                show sc zoratrainingpark g109
                zora"He just made me so mad that I just reacted without thinking."
                show sc zoratrainingpark g110
                zora"I did good though, right?"
                show sc zoratrainingpark g111
                mc"Are you kidding me?"
                show sc zoratrainingpark g112
                mc"That was one of the coolest things that I’ve seen in a while."
                show sc zoratrainingpark g113
                mc"Hey, perhaps you channeled your inner Red Zora?"
                play sound "sound effects/01/female_laughing1.mp3" noloop
                show sc zoratrainingpark g114
                zora"Haha!"
                stop sound fadeout 1.0
                show sc zoratrainingpark g115
                zora"I don’t know, maybe."
                #She gives him a sexy little smile.

    else:
        #he stands up straight and points at the water fountain for the MC
        #Guy checks out Zora
        show sc zoratrainingpark g077
        guy"And then 'Chunky Town can go next."
        #[Trick him / Speak up]
        menu:
            "Trick him"(wt="Best option"):
                show sc zoratrainingpark g071
                mc"(What the fuck?)"
                show sc zoratrainingpark g102
                guy"You should come to my gym."
                show sc zoratrainingpark g079
                mc"Excuse me..."
                #the MC steps up to Guy, to intimidate him
                show sc zoratrainingpark g080
                mc"But I think that hottie wearing skin-tight clothing might want to use the water bubbler next."
                #He looks past Guy’s shoulder, pretending to see Bella
                show sc zoratrainingpark g081
                guy"Really?"
                guy"But I don’t see any hottie-"
                #Guy looks over his shoulder
                play sound "sound effects/01/kick_to_the_gut.mp3" noloop
                show sc zoratrainingpark g082
                with vpunch
                #the MC moves forward and knees Guy in the nuts and he hits the ground, clutching at them
                play sound2 "sound effects/01/male_grunt_gut_punch.mp3" noloop
                guy"NGHH!!{w=1.0}{nw}"
                play sound3 "sound effects/01/male_moaning_in_pain1.mp3" noloop
                show sc zoratrainingpark g083
                with vpunch
                pause 0.5
                play sound "sound effects/01/Falling Over Sound Effect.mp3" noloop
                show sc zoratrainingpark g084
                with dissolve
                guy"Fuck!!"
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                stop sound3 fadeout 1.0
                #the MC stands over him
                show sc zoratrainingpark g085
                mc"Now let’s try that again, and I suggest that you throw in an apology to the lady while you’re at it."
                show sc zoratrainingpark g084
                guy"Uhhh... Fuck you!"
                play sound "sound effects/03/cracking_knuckles_effect.mp3" noloop
                show sc zoratrainingpark g086
                pause 1.0
                #he responds while on the ground
                play sound2 "sound effects/01/male_scream_sound_effect1.mp3" noloop
                #the MC grabs on the hand not grabbing his crotch and bends it backwards
                show sc zoratrainingpark g087
                guy"Ahhh!"
                #he yells in pain
                show sc zoratrainingpark g088
                guy"Okay, okay..."
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                show sc zoratrainingpark g089
                guy"Sorry, I’m sorry miss for the insult and for stepping in front of you."
                guy"It won’t happen again."
                show sc zoratrainingpark g090
                zora"Oh, thank you."
                show sc zoratrainingpark g095
                mc"Best you run along, dude. That is, if you can."
                show sc zoratrainingpark g092
                guy"You just made yourself an enemy."
                #the MC looks at him menacingly
                show sc zoratrainingpark g093
                mc"What was that?"
                show sc zoratrainingpark g095
                guy"I meant, I’ll be going now."
                play sound "sound effects/01/jogging_in_the_park.ogg" fadein 1.0
                show sc zoratrainingpark g170
                with dissolve
                pause 1.5
                #MC turns to Zora
                show sc zoratrainingpark g096
                with dissolve
                mc"Are you okay?"
                stop sound fadeout 1.0
                show sc zoratrainingpark g097
                zora"Yeah, I’m fine."
                show sc zoratrainingpark g098
                zora"Thanks for standing up for me... Again."
                show sc zoratrainingpark g097
                zora"You’re making a habit of that."
                show sc zoratrainingpark g099
                mc"Something I’m more than happy to do, and as often as possible if you need me to."
                $ v_ep03_02_01_standing_up_for_Zora +=1
                #Zora smiles

            "Speak up":
                show sc zoratrainingpark g102
                mc"(Who the fuck does this asshole think he is?)"
                show sc zoratrainingpark g072a
                mc"No need for the cheap insults, dude. I’m her trainer, and we’re trying to work out here."
                #the MC steps up to Guy, to intimidate him
                show sc zoratrainingpark g101
                guy"Haha! Really?"
                show sc zoratrainingpark g102
                guy"Girl, if he’s your trainer then you ain’t learning shit!"
                show sc zoratrainingpark g104
                guy"I mean, look at you."
                show sc zoratrainingpark g103
                guy"You should come to a real gym. My gym."
                show sc zoratrainingpark g077
                guy"This pipsqueak wouldn’t be able to train a mime artist let alone a girl of your si-"
                #Zora starts getting angry
                show sc zoratrainingpark g106
                zora"Hi-ya!!"
                #She moves towards Guy and kicks him in the nuts and he hits the ground, clutching at them
                play sound "sound effects/01/kick_to_the_gut.mp3" noloop
                show sc zoratrainingpark g105
                with vpunch
                pause 0.5
                play sound2 "sound effects/01/male_grunt_gut_punch.mp3" noloop
                guy"NGHH!!{w=1.0}{nw}"
                play sound3 "sound effects/01/male_moaning_in_pain1.mp3" noloop
                show sc zoratrainingpark g083
                with vpunch
                guy"Fuck!!"
                play sound "sound effects/01/Falling Over Sound Effect.mp3" noloop
                show sc zoratrainingpark g084
                mc"Woah..."
                #GUY HITS THE GROUND - SOUND EFFECT
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                stop sound3 fadeout 1.0
                #the MC stands over him
                show sc zoratrainingpark g106
                zora"Say that again, asshole?"
                show sc zoratrainingpark g085
                guy"Uhhh... Fuck you!"
                #he responds while on the ground
                #the MC grabs the hand of Guy's that's not holding his crotch and bends it backwards
                play sound "sound effects/03/cracking_knuckles_effect.mp3" noloop
                show sc zoratrainingpark g086
                pause 1.0
                #the MC grabs on the hand not grabbing his crotch and bends it backwards
                play sound2 "sound effects/01/male_scream_sound_effect1.mp3" noloop
                show sc zoratrainingpark g087
                guy"Ahhh!"
                mc"What was that?"
                #he yells in pain
                stop sound fadeout 1.0
                stop sound2 fadeout 1.0
                show sc zoratrainingpark g088
                guy"Okay, okay..."
                show sc zoratrainingpark g089
                guy"I’m sorry miss for the insult and for stepping in front of you."
                show sc zoratrainingpark g090
                guy"It won’t happen again."
                show sc zoratrainingpark g106
                zora"There, was that so difficult?"
                #Zora has her hands on her hips as she looks down at him
                show sc zoratrainingpark g092
                guy"You just made yourself an enemy."
                #the MC looks at him menacingly
                show sc zoratrainingpark g093
                mc"Excuse me?"
                show sc zoratrainingpark g094
                guy"I meant, I’ll be going now."
                play sound "sound effects/01/jogging_in_the_park.ogg" fadein 1.0
                show sc zoratrainingpark g170
                with dissolve
                pause 1.5
                #MC turns to Zora
                show sc zoratrainingpark g096
                with dissolve
                mc"Are you okay?"
                stop sound fadeout 1.0
                show sc zoratrainingpark g097
                zora"Yeah, I’m fine."
                show sc zoratrainingpark g099
                mc"Where on earth did that come from??"
                show sc zoratrainingpark g108
                zora"I... I don’t know."
                show sc zoratrainingpark g109
                zora"He just made me so mad that I just reacted without thinking."
                show sc zoratrainingpark g110
                zora"I did good though, right?"
                show sc zoratrainingpark g111
                mc"Are you kidding me?"
                show sc zoratrainingpark g112
                mc"That was one of the coolest things that I’ve seen in a while."
                show sc zoratrainingpark g113
                mc"Hey, perhaps you channeled your inner Red Zora?"
                play sound "sound effects/01/female_laughing1.mp3" noloop
                show sc zoratrainingpark g114
                zora"Haha!"
                stop sound fadeout 1.0
                show sc zoratrainingpark g115
                zora"I don’t know, maybe."
                #She gives him a sexy little smile.

    #scene continues
    show sc zoratrainingpark g117
    mc"Come on, let’s continue on with our session."
    show sc zoratrainingpark g118
    zora"Sounds good..."
    play sound "sound effects/01/jogging_in_the_park.ogg" fadein 1.0
    show sc zoratrainingpark g119
    with dissolve
    pause 2.0
    #final shot here of the MC and Zora continuing their jog
    stop ambient fadeout 1.0
    stop sound fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
    #the scene continues with the MC and Zora standing alongside a park bench stretching
    show sc zoratrainingpark g120
    with dissolve
    mc"We’re almost done."
    show sc zoratrainingpark g121
    mc"Now just a simple cool down with some light stretches."
    show sc zoratrainingpark g122
    with dissolve
    mc"Did you have a good time with me this morning?"
    show sc zoratrainingpark g123
    with dissolve
    zora"Yeah, it’s been great."
    #she says this unenthusiastically
    show sc zoratrainingpark g124
    mc"Is there something wrong?"
    show sc zoratrainingpark g125
    mc"The lack of conviction in your voice suggests to me that there is."
    show sc zoratrainingpark g126
    zora"It’s just..."
    show sc zoratrainingpark g127
    zora"I want to ask you something but I don’t know if I should."
    show sc zoratrainingpark g125
    mc"I’m an open book, Zora."
    show sc zoratrainingpark g126
    mc"Ask me anything you want and there’ll be no judgment, I promise."
    show sc zoratrainingpark g127
    zora"Okay, let me take a seat first..."

    if v_ep01_04_01_Bella_Work_Date == True:
        #these lines if the player played the Bella \"Bonus Date\" scene in Episode 1 (he’s met Guy before)
        #Zora now sits on the park bench
        show sc zoratrainingpark g128
        with dissolve
        zora"That guy before, who was at the water fountain."
        show sc zoratrainingpark g129
        zora"He said something before about trading a blonde bombshell in for being with me."
        zora"What did he mean by that?"
        #the MC now sits next to her
        show sc zoratrainingpark g130
        with dissolve
        mc"Oh..."
        mc"Well, do you know how I said that I’d run into him before?"
        show sc zoratrainingpark g131
        zora"Yeah..."
        show sc zoratrainingpark g130
        mc"The day I last spoke with him, I was here with my [b_mc_rel]."
        show sc zoratrainingpark g132
        zora"Oh..."
        show sc zoratrainingpark g134
        zora"So you two are...?"
        show sc zoratrainingpark g130
        mc"Yeah, that’s who he was referring to."
        mc"[b_name] and I live together with a few others and she invited me to go for a run with her that day."
        mc"That’s why I knew about this place."
        show sc zoratrainingpark g136
        zora"That’s great!"
        show sc zoratrainingpark g133
        zora"I thought for a second that she might be your..."
        show sc zoratrainingpark g135
        mc"Oh, no chance!"
        show sc zoratrainingpark g138
        mc"Even if it were possible, [b_name] would be a lot of hard work."

    else:
        #this lines if the player DID NOT play the Bella \"Bonus Date\" scene in Episode 1 (he’s never met Guy before)
        #Zora now sits on the park bench
        show sc zoratrainingpark g128
        zora"That guy before, who was at the water fountain."
        show sc zoratrainingpark g129
        zora"He referred to me as \"Chunky town\"."
        show sc zoratrainingpark g147
        zora"Is that how you see me?"
        #the MC now sits next to her
        show sc zoratrainingpark g149
        mc"No, not at all, Zora."
        mc"Just because one asshole says this about you, it's not how the whole world sees you."
        show sc zoratrainingpark g152
        mc"And as of right now, you’re still figuring things out."
        show sc zoratrainingpark g135
        mc"If you’re not happy with your health or the way you look, then it’s never too late to do something about it."
        mc"And like I said before, you’ve already made the first step."
        show sc zoratrainingpark g138
        mc"And I’ll be right here to help you out, every step of the way."
        show sc zoratrainingpark g137
        zora"Thanks."

    #scene continues

    #[Further comfort her / Leave her be]
    menu:
        "Further comfort her"(wt="Best option"):
            show sc zoratrainingpark g135
            mc"You know, I genuinely like hanging out with you."
            show sc zoratrainingpark g140
            mc"Like, a lot."
            #He places his hand upon hers
            show sc zoratrainingpark g141
            zora"I like hanging out with you too, [y_name]."
            show sc zoratrainingpark g142
            mc"And I’ll do anything to get you where you want to be."
            $ v_ep01_zora_respect_counter += 1
            #they stare at each other
            show sc zoratrainingpark g154
            zora"I’m very happy where I am right now, to be honest."
            show sc zoratrainingpark g152
            mc"Yeah, me too."
            $ v_ep03_02_01_standing_up_for_Zora +=1
            #[Kiss her / Don’t kiss her]
            menu:
                "Kiss her"(wt="Best option"):
                    #The MC slowly leans in, waits to see if she will move her head back, and then kisses her
                    show sc zoratrainingpark g143
                    with dissolve
                    pause 1.0
                    show sc zoratrainingpark g144
                    with dissolve
                    pause 1.0
                    play sound "sound effects/02/new_kissing_sound_FX.mp3" loop fadein 1.0
                    show sc zoratrainingpark g145
                    with dissolve
                    zora"Mmm..."
                    #the MC moves his hand to her waist
                    #they tongue kiss
                    show sc zoratrainingpark g145a
                    with dissolve
                    pause 1.0
                    #Zora is surprised and retracts the kiss
                    stop sound fadeout 1.0
                    show sc zoratrainingpark g146
                    with dissolve
                    zora"Oh, wow..."
                    show sc zoratrainingpark g147
                    zora"I really wasn’t expecting that."
                    show sc zoratrainingpark g148
                    mc"Did you not like it?"
                    show sc zoratrainingpark g150
                    zora"It’s not that, you just took me by surprise is all."
                    #She looks confused
                    show sc zoratrainingpark g151
                    mc"Sorry, I couldn’t help it."
                    mc"It just felt like the right moment, you know?"
                    mc"But we can take things slow if you prefer."
                    $ v_ep01_zora_respect_counter += 1
                    show sc zoratrainingpark g149
                    mc"Or not at all."
                    show sc zoratrainingpark g153
                    zora"No, no... I want to. But going slow would be much better."
                    show sc zoratrainingpark g151
                    mc"Cool. So, would you like to try this again?"
                    show sc zoratrainingpark g154
                    zora"I’d love to."
                    #the MC leans in and kisses her again
                    play sound "sound effects/02/new_kissing_sound_FX1.mp3"
                    show sc zoratrainingpark g145
                    zora"(Oh my... This is so confusing but so amazing at the same time!)"
                    #they tongue kiss
                    zora"Mmm..."
                    stop sound fadeout 1.0
                    $ v_ep03_02_01_standing_up_for_Zora +=1
                    #they break the kiss

                "Don’t kiss her":
                    show sc zoratrainingpark g151
                    pause 1.0
                    #scene continues
        "Leave her be"(wt="Bonus Image"):
            show sc zoratrainingpark g138
            pause 1.0
            $ rewards_unlock ("zora",7)
            #scene continues
    show sc zoratrainingpark g155
    with dissolve
    mc"Would you be interested in hanging out again, with no fitness involved?"
    show sc zoratrainingpark g156
    zora"Do you mean like a date?"
    show sc zoratrainingpark g157
    mc"It can be anything you want it to be."
    show sc zoratrainingpark g158
    zora"Well..."
    show sc zoratrainingpark g159
    zora"Sure, I’d love to."
    show sc zoratrainingpark g161
    mc"How about tonight?"
    show sc zoratrainingpark g157
    zora"Tonight?"
    show sc zoratrainingpark g150
    zora"Oh, um, I’m supposed to go out with my parents this evening."
    show sc zoratrainingpark g152
    zora"But I don’t really want to go as I don’t enjoy eating out in public around other people."
    show sc zoratrainingpark g158
    mc"Well... Maybe you could just ditch them?"
    show sc zoratrainingpark g160
    zora"What do you mean?"
    show sc zoratrainingpark g161
    mc"Tell them that you’re too sick to go out and stay home."
    show sc zoratrainingpark g162
    mc"Do you think you could do that?"
    show sc zoratrainingpark g163
    zora"I feel like I could."
    show sc zoratrainingpark g168
    zora"And then we could do something together."
    show sc zoratrainingpark g160
    zora"Maybe you could come over to my house."
    show sc zoratrainingpark g163
    zora"There won’t be anyone home and my parents will be gone for a few hours."
    show sc zoratrainingpark g164
    zora"I mean, that is if you’re okay coming to my place?"
    show sc zoratrainingpark g165
    mc"Actually, that would be perfect."
    show sc zoratrainingpark g166
    mc"What time should I come over?"
    show sc zoratrainingpark g167
    zora"Well, my parents are leaving at seven-thirty."
    show sc zoratrainingpark g168
    zora"So a little after then. Is that okay?"
    show sc zoratrainingpark g165
    mc"I’ll be there around eight o'clock."
    if v_ep03_02_01_standing_up_for_Zora >= 4:
        $ zora_love_level +=1
        $ v_ep03_zora_fantasy_counter +=1
    show sc zoratrainingpark g169
    mc"Let me walk you back to your car and then I’ll get your address from you."
    stop ambient fadeout 1.0
    #Zora smiles and they start walking out of the park entrance.
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_02_02_Trying_clothes_on_with_Ariel


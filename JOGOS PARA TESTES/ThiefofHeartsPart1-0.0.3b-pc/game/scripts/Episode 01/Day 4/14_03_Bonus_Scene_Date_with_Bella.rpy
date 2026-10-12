init:
    $ v_ep01_defend_bella = False

default v_ep01_bella_dates_counter = 0

label lb_ep01_Bonus_Scene_Date_with_Bella1:
    #THIS SCENE WILL ONLY TRIGGER IF THE PLAYER CHOOSES "OFFER TO HELP" DURING SCENE 04-01

    #scene begins back at the house, the MC in the hallway

    #"After lunch..." #This comes up on the screen
    scene sc bellatalk b00
    with dissolve
    mc"(I think I saw [b_name] go into her room.)"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    #The MC arrives at her bedroom door
    show sc bellapark b156
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    mc"[b_name]?"
    mc"Are you in there?"
    stop sound fadeout 1.0
    #Bella shows up, dressed in fitness attire
    #Options
    #https://www.daz3d.com/fg-workout-outfit-for-genesis-8-and-81-females
    #https://www.daz3d.com/s3d-fitness-clothes-for-genesis-8-females

    #ROLLING SCREEN OF BELLA
    play sound "sound effects/01/Door_Opening.mp3"
    show sc bellapark b158
    with dissolve
    b"Hey, what's up?"
    stop sound fadeout 1.0
    show sc bellapark b159
    mc"(Fuck me...)"
    show sc bellapark b157
    mc"(It kills me every time I see her dressed like this, right before she goes out for her run.)"
    show sc bellapark b161
    mc"I was going to ask you the same thing."
    show sc bellapark b160
    b"Well, I'm about to go out for a jog."
    b"So unless it's important, I'll be going now."
    show sc bellapark b161
    mc"Where are you running today?"
    show sc bellapark b159
    b"Just at the local park. I like to use the exercise circuit they have there."
    show sc bellapark b162
    b"Why, did you want to join me or something?"
    show sc bellapark b163
    b"(There's no way he'll agree to this.)"
    show sc bellapark b165
    mc"You know what?"
    show sc bellapark b166
    mc"Sure, why not!"
    show sc bellapark b164
    b"Oh, but I wasn't being seri-"
    #The MC cuts her off
    show sc bellapark b167
    mc"Give me five minutes to change and I'll be raring to get my sweat on!"
    #The MC takes off into his room and Bella has a devilish look in her eye
    show sc bellapark b168
    b"(Great...)"
    show sc bellapark b169
    b"(He better not hold me up.)"
    show sc bellapark b170
    b"(However, [y_name] has no idea what he's in for...)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The next scene is the MC and Bella jogging in the park
    #Bella is out ahead and the MC is trying to keep up with her
    play ambient "sound effects/01/park_sounds_ambience.ogg" loop fadein 1.0
    play ambient2 "sound effects/01/jogging_in_the_park.ogg" loop fadein 1.0
    $ ui.timer(0.3, Play("ambient3", "sound effects/01/jogging_in_the_park.ogg", loop=True))
    play music "sound effects/01/Running in the Sun1.mp3" loop fadein 1.0
    scene sc bellapark b001
    with dissolve
    scene sc bellapark b002
    b"Come on, [y_name]!"
    show sc bellapark b003
    b"Move your ass!!"
    show sc bellapark b004
    mc"(God damn...)"
    show sc bellapark b005
    mc"(I never realised just how damn fast she is!)"
    show sc bellapark b006
    mc"I'm coming!"
    show sc bellapark b007
    b"I bet you say that a lot after only putting a little effort in!"
    play sound "sound effects/01/female_laughing4.mp3"
    show sc bellapark b008
    b"Hahaha!"
    #Bella laughs and then keeps running so we can see her ass in her tight shorts
    show sc bellapark b009
    mc"(It's just as well I have a great view otherwise I may have been offended by that.)"
    stop sound fadeout 1.0
    stop ambient2 fadeout 1.0
    #Bella stops and waits for the MC to catch up
    show sc bellapark b011
    b"You know, for someone who works in a gym..."
    stop ambient3 fadeout 1.0
    show sc bellapark b012
    b"You don't seem all that fit."
    show sc bellapark b013
    mc"You do realise that some of us focus on resistance training rather than aerobics, right?"
    show sc bellapark b014
    b"Hmm... Touché."
    #The MC watches Bella while she is stretching
    #Pose #1 - https://www.verywellfit.com/thmb/dXsD_BF6jzg2PmzcATxGhvzXCHM=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/QuadStretch_annotated-88a3172391cc4daa85fd643d14f73a15.jpg
    show sc bellapark b015
    mc"(I can't help but notice how many guys have been checking [b_name] out ever since we got here.)"
    mc"(And some girls too!)"
    show sc bellapark b016
    mc"(Even though she's my [b_mc_rel], I must be the envy of every person in the park!)"
    #Pose #2 - https://www.verywellfit.com/thmb/wePFJzNNLnMnQnIjdnAd-9K2OVw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/ITBandStretch_annotated-8a042d90eb534d0b8dc2d38823569a91.jpg
    show sc bellapark b018
    mc"So how often do you go jogging here?"
    show sc bellapark b017
    b"Sometimes three to four times a week."
    #Pose #3 - https://www.verywellfit.com/thmb/yJiZNmaqElRDSE2QYFGLp69n2A0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/ArmsAndAbsStretch_annotated-4ea15ef043a44edb8537e20f6ad9af65.jpg
    show sc bellapark b019
    b"It all depends on how many shifts I have at work."
    show sc bellapark b021
    b"And sometimes I need to get out of the house just for my own sanity."
    show sc bellapark b022
    mc"I totally get it."
    show sc bellapark b023
    mc"Anything to make up for not being able to go out late at night, huh?"
    show sc bellapark b024
    b"Yeah, exactly."
    #A fit muscular Guy comes up to Bella
    show sc bellapark b025
    guy"Hey there, hot stuff!"
    show sc bellapark b026
    guy"I was hoping you would be here today."
    show sc bellapark b027
    guy"You know, you look even hotter when you sweat."
    show sc bellapark b171
    b"Ugh... Hey, Guy."
    show sc bellapark b029
    mc"You two know each other?"
    #Bella very nonchalantly introduces the MC to Guy
    show sc bellapark b172
    b"[y_name], this is Guy, aka, my stalker."
    show sc bellapark b032
    guy"Woah, woah..."
    show sc bellapark b031
    guy"That's a little harsh."
    show sc bellapark b033
    guy"I'm more like a \"keen admirer\"."
    show sc bellapark b034
    b"If you don't mind, we're in the middle of a workout."
    show sc bellapark b035
    guy"From what I could see, it seems like you need a man that's able to keep up with you."
    #Guy gives a cocky grin
    show sc bellapark b036
    guy"And not just on the running circuit, if you know what I mean?"
    #Guy addresses the MC
    show sc bellapark b038
    guy"No offence, dude."
    show sc bellapark b039
    b"Sigh..."

    #[Say something back / Stay out of it]
    menu:
        "Say something back"(wt="Best option"):
            $ v_ep01_defend_bella = True
            #The MC puts his arm on Bella's shoulder
            show sc bellapark b040
            mc"Sorry to deflate your ego, \"Guy\", but [b_name] doesn't need any more running partners today."
            #The MC looks at Bella
            show sc bellapark b041
            mc"Do you, babe?"
            show sc bellapark b042
            b"(Did he just call me babe??)"
            show sc bellapark b043
            guy"Do you mean... You two?"
            show sc bellapark b044
            mc"Yeah..."
            play sound "sound effects/01/Male_Laughing_Sound_Effect.mp3"
            show sc bellapark b045
            guy"Hahaha!"
            show sc bellapark b046
            guy"You must be fucking joking!"
            stop sound fadeout 1.0
            show sc bellapark b047
            guy"Why would she date a guy like-"
            #The screen shakes MC cups Bella's ass
            show sc bellapark b048
            b"Oh!!"
            show sc bellapark b050
            b"(What on earth is he doing?)"
            show sc bellapark b051
            b"(Is he crazy?)"
            show sc bellapark b052
            mc"As you can see, this fine, tight ass is mine."
            show sc bellapark b053
            mc"So I suggest you get lost before you embarrass yourself even more, dude."
            #Guy looks confused and upset
            show sc bellapark b055
            guy"Fine, whatever..."
            #The MC watches Guy as he leaves
            show sc bellapark b035
            guy"Come and find me when you're done playing with Junior."
            show sc bellapark b056
            guy"I'm outta here!"
            show sc bellapark b057
            mc"God, what a douche."
            $ v_ep01_bella_cocky_counter += 1
            #The MC turns to Bella who has her arms folded and is not impressed
            show sc bellapark b059
            b"Just what the hell was that?"
            show sc bellapark b060
            mc"What? The guy was being an asshole."
            show sc bellapark b061
            b"True, but did you really need to grope me?"
            show sc bellapark b062
            mc"I'd hardly call it groping."
            show sc bellapark b062
            mc"More like... firm fondling."
            show sc bellapark b064
            mc"Besides, I got rid of him, didn't I?"
            show sc bellapark b065
            b"Hmm... I guess so."
            show sc bellapark b066
            b"But don't you dare pull that kind of shit again, [y_name]."
            show sc bellapark b067
            mc"Fine... But in future, if you don't speak up when there's a muscle-headed moron about, then I will."
            show sc bellapark b068
            b"(Wow... Was he protecting me because he's my [mc_b_rel] or because he really hated Guy?)"
            show sc bellapark b069
            b"(Maybe I was overreacting. I mean, all he did was put his hand on my ass.)"
            show sc bellapark b070
            b"(I've had a lot worse from guys.)"
            $ rewards_unlock ("bella",10)

        "Stay out of it":
            show sc bellapark b071
            b"How many times do I have to tell you this, Guy."
            show sc bellapark b072
            b"Stay the hell away from me before I tear your nuts off and stuff them down your throat!"
            show sc bellapark b073
            guy"Okay, okay. Message received!"
            #Guy looks at the MC
            show sc bellapark b074
            guy"Good luck with the loose canon, kid."
            show sc bellapark b056
            guy"I'm outta here!"
            #Bella looks angry
            show sc bellapark b075
            mc"(Damn... I've never seen [b_name] this pissed off before.)"
            #Bella turns to the MC, unimpressed
            show sc bellapark b072
            b"Thanks alot for your help there, dipshit."
            show sc bellapark b078
            mc"Did you see the size of that guy?"
            $ v_ep01_bella_arrogant_counter += 1
            show sc bellapark b079
            mc"He might be an asshole but I'm not stupid enough to get in a fight with that nut job!"
            #Bella turns away from the MC with her arms folded
            show sc bellapark b080
            b"Pftt... Typical."

    #scene continues

    #they go for another run
    show sc bellapark b081
    b"Anyway, we're going to run for another ten or fifteen minutes."
    show sc bellapark b082
    b"Try and keep up this time."
    #Bella takes off and the MC watches her

    #"Add these lines if the player chose "Say something back"
    if v_ep01_defend_bella:
        play ambient2 "sound effects/01/park_sounds_ambience.ogg" loop fadein 1.0
        show sc bellapark b083
        mc"(She'll never admit it, but I'm pretty sure [b_name] liked me blatantly caressing her butt.)"
        #Show Bella's ass as she runs ahead
        show sc bellapark b085
        mc"Hmm..."
        show sc bellapark b086
        mc"(And what I fine butt it is...)"
        stop ambient2 fadeout 1.0
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    play ambient "sound effects/01/park_sounds_ambience.ogg" loop fadein 1.0
    play ambient2 "sound effects/01/jogging_in_the_park.ogg" loop fadein 1.0
    $ ui.timer(0.3, Play("ambient3", "sound effects/01/jogging_in_the_park.ogg", loop=True, fadein=1.0))
    play music "sound effects/01/Running in the Sun2.mp3" loop fadein 1.0
    show sc bellapark b088
    with dissolve
    mc"How much further?"
    show sc bellapark b089
    b"Just a little longer!"
    show sc bellapark b090
    b"Race you to that tree ahead, [y_name]."
    show sc bellapark b091
    mc"You're on!!"
    #The MC and Bella run at full pelt, neck and neck
    play ambient2 "sound effects/01/jogging_in_the_park_speed.ogg" loop
    $ ui.timer(0.3, Play("ambient3", "sound effects/01/jogging_in_the_park_speed.ogg", loop=True))
    show sc bellapark b092
    b"Oh no you don't!"
    show sc bellapark b094
    mc"Oh yes I do!!"
    #The MC streaks ahead
    show sc bellapark b095
    mc"(I'm actually going to beat her!)"
    show sc bellapark b096
    mc"Eat my dust [b_name]..."
    stop ambient2 fadeout 1.0
    show sc bellapark b096a
    with hpunch
    # 'thud?'  first impression was Bella ran into a tree
    # more like a 'flop' sound if bella falls over from a cramp
    if persistent.v_sounds_text_on == True:
        "(Thud.)"
    else:
        pause 1.0
    stop ambient3 fadeout 1.0
    show sc bellapark b097
    mc"[b_name]?"
    #The MC turns around and sees Bella on the ground, clutching at her calf
    show sc bellapark b098
    b"(Ow...)"
    #The MC jogs back over to her
    show sc bellapark b099
    mc"What happened?"
    show sc bellapark b100
    mc"Are you all right?"
    show sc bellapark b101
    b"Yeah, I'll be fine."
    show sc bellapark b102
    b"My calf tightened up I think."
    #Bella grabs at it - https://img.livestrong.com/375/clsd/getty/bc468d31f00943e0a5aa790f614058e0.jpg
    show sc bellapark b103
    b"And my quad muscles."
    #Bella grabs at her quads - https://www.performancehealth.com/media/wysiwyg/blog/articles/Hamstring-quadriceps_3.PNG
    show sc bellapark b105
    b"Ow..."
    #Bella limps
    #The MC could offer to help her or not

    #[Offer to help / Walk it off]
    menu:
        "Offer to help"(wt="Best option"):
            show sc bellapark b106
            mc"Want me to take a look at it?"
            show sc bellapark b107
            b"Oh sure."
            b"Are you going to just rub your palms together and fix me, Mr. Miyagi?"
            show sc bellapark b108
            mc"I'm serious, [b_name]."
            mc"I see this kind of thing all the time at the gym."
            show sc bellapark b109
            mc"Let me take a look at it."
            show sc bellapark b110
            mc"Sit down on the ground for me."
            #The MC surveys Bella's cramped muscle in her leg - https://www.sportsinjuryclinic.net/wp-content/uploads/2019/02/tight-calf-muscles800.jpg
            show sc bellapark b111
            b"Fine, you have me where you want me."
            b"What now?"
            show sc bellapark b114
            b"Oooh..."
            show sc bellapark b115
            mc"How does that feel?"
            show sc bellapark b116
            b"Sore..."
            show sc bellapark b117
            b"Like incredibly sore."
            show sc bellapark b118
            mc"Okay."

            #[Stop / Go higher]
            menu:
                "Stop":
                    #Bella looks at the MC
                    show sc bellapark b175
                    mc"I think you just need to put some ice on it and then rest up."
                    show sc bellapark b176
                    mc"And make sure you elevate this leg when we get back."
                    $ v_ep01_bella_respect_counter += 1
                    show sc bellapark b120
                    b"I'll remember to do that."
                    #GO TO > #scene continues

                "Go higher"(wt="Best option"):
                    show sc bellapark b121
                    mc"I'm just going to lightly massage your calf."
                    show sc bellapark b122
                    mc"Let me know how it feels."
                    #The MC squeezes and caresses Bella's calf muscle - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTS-y2IAXLiLpLAOE9KSCacXAy2jbfPcSUKOdBxOkCdi7y7Qja4qn8NQFi0-duy9h0i-Tc&usqp=CAU
                    show sc bellapark b123
                    b"Uhh..."
                    show sc bellapark b124
                    b"Yeah, it feels really tight."
                    show sc bellapark b125
                    b"Like super tight."
                    #Show the MC's POV where we can see between Bella's legs while he attended to her calf.
                    #She's showing some slight cameltoe
                    show sc bellapark b126
                    mc"Um... Okay."
                    show sc bellapark b127
                    mc"(Is she still talking about her calf muscle??)"

                    #[Stop / Keep going]
                    menu:
                        "Stop":
                            #Bella looks at the MC
                            show sc bellapark b175
                            mc"I think you just need to put some ice on it and then rest up."
                            show sc bellapark b176
                            mc"And make sure you elevate this leg when we get back."
                            $ v_ep01_bella_respect_counter += 1
                            show sc bellapark b130
                            b"I'll remember to do that."

                            #GO TO > #scene continues

                        "Keep going"(wt="Best option"):
                            show sc bellapark b131
                            mc"What about here?"
                            #The MC's hands go up to her quad muscles or upper thigh muscles - https://i.pinimg.com/736x/4a/3a/95/4a3a95cf868975aec49a7c1c954da86f.jpg
                            show sc bellapark b132
                            b"UNGH!"
                            show sc bellapark b133
                            b"Oh geez..."
                            show sc bellapark b134
                            b"I don't know how this could happen."
                            show sc bellapark b135
                            mc"It could be several reasons..."
                            show sc bellapark b136
                            # this line needs help
                            mc"Lack of hydration, hard physical activity or overexertion, or even prolonged or repetitive use of your quad muscles without adequate rest can lead to muscle fatigue."
                            mc"Or maybe you didn't stretch long enough before we started our run."
                            show sc bellapark b137
                            b"Yeah, it sounds like it could be that."

                            #[Stop / A little higher]
                            menu:
                                "Stop"(wt="Best option"):
                                    #Bella looks at the MC
                                    show sc bellapark b175
                                    mc"I think you just need to put some ice on it and then rest up."
                                    show sc bellapark b176
                                    mc"And make sure you elevate this leg when we get back."
                                    $ v_ep01_bella_respect_counter += 1
                                    show sc bellapark b130
                                    b"I'll remember to do that."
                                    $ rewards_unlock ("bella",11)

                                    #GO TO > #scene continues

                                "A little higher":
                                    #The MC's hands go up to her inner thigh muscles or groin muscles - https://qph.cf2.quoracdn.net/main-qimg-90056468756583ae031bd69fe31bc473-lq
                                    show sc bellapark b138
                                    mc"And here... Do you feel any tension?"
                                    #This makes Bella uncomfortable
                                    mc"(Her thighs feel so nice and supple, well-rounded...)"
                                    show sc bellapark b139
                                    mc"(...and luxuriant to the touch.)"
                                    show sc bellapark b137
                                    b"Uh... What are you doing?"
                                    show sc bellapark b144
                                    mc"I was just checking your groin muscles."
                                    show sc bellapark b134
                                    b"I don't have any issues there, [y_name]."
                                    show sc bellapark b138
                                    mc"Oh... Well, my mistake."
                                    #Bella gives the MC a sceptical look
                                    show sc bellapark b147
                                    b"(Hmm...)"
                                    show sc bellapark b148
                                    mc"(I wasn't exactly subtle about what I was doing.)"
                                    show sc bellapark b149
                                    mc"(Still... Totally worth it!)"
                                    $ v_ep01_bella_cocky_counter += 1

                                    #GO TO > #scene continues

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        "Walk it off":
            show sc bellapark b106
            mc"You'll be fine. Just walk it off."
            $ v_ep01_bella_arrogant_counter += 1
            #Bella shoots the MC a funny look
            show sc bellapark b109
            b"Yeah... Thanks."


    #scene continues
    show sc bellapark b150
    with dissolve
    mc"So, do you wanna do something else?"
    show sc bellapark b173
    b"Actually, I think I'm done for today."
    show sc bellapark b174
    b"So we can head home."
    show sc bellapark b153
    b"But thanks for joining me."
    show sc bellapark b154
    b"Maybe we could do this again once I've healed up."
    show sc bellapark b155
    mc"Yeah, that'd be great..."
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ v_ep01_bella_dates_counter += 1
    jump lb_ep01_Bonus_Scene_Date_with_Ariel1
    if v_ep01_05_01_Ariels_Work_Date:
        jump lb_ep01_Bonus_Scene_Date_with_Ariel1
    else:
        jump lb_ep01_The_MC_Investigates_the_gang
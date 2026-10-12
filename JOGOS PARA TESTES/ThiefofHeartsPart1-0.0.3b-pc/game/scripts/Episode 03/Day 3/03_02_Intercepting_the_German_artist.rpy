init:
    $ v_ep03_task_13_german_woman_counter = 0
    $ v_ep03_othergirls_aa_tasks_counter = 0
    $ v_ep03_german_woman_real_name_used = False

label lb_ep03_03_02_Intercepting_the_German_artist:

    #SCENE BEGINS

    centered "The German Artist...{w=2.0}{nw}" with dissolve
    show text "The German Artist..."
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/03/airport_ambience.mp3" loop fadein 1.0
    #Start with a shot of Airport arrivals - https://live-production.wcms.abc-cdn.net.au/80bf7cae24e30d09a16cf29c3faadeb1?impolicy=wcms_crop_resize&cropH=1577&cropW=2375&xPos=222&yPos=0&width=862&height=575
    scene sc germanartist o001
    with dissolve
    pause 1.5
    #people start coming through the terminal - https://thumbs.dreamstime.com/b/people-waiting-greeting-friends-relatives-arrival-hall-hong-kong-international-airport-273694120.jpg
    scene sc germanartist o002
    with dissolve
    pause 1.5
    #the MC and Ariel, dressed up a member from the Art Gallery with Ariel as his assistant
    #Ariel will wear the suit she tried on at Bella’s shop (Scene 02-02)
    scene sc germanartist o003
    with dissolve
    pause 1.5
    #She has her hair down and isn’t wearing glasses - so it’s harder for the German woman to recognise her later
    scene sc germanartist o005
    with dissolve
    pause 1.5
    #the MC is dressed professionally as well but has a moustache as well to hide his identity
    #Ariel holds up a sign that says "Miss Helga Veerhaart" written on it - https://www.shutterstock.com/image-vector/people-meeting-someone-airport-arrival-260nw-2256541321.jpg
    show sc germanartist o006
    with dissolve
    a"According to the arrival’s board, she should be here any second now."
    show sc germanartist o007
    mc"Yeah, we’ll have to keep our eyes peeled."
    show sc germanartist o008
    a"By the way, I changed her arrival details with the art gallery."
    show sc germanartist o009
    a"I hacked into their email account so that they think she’s arriving tomorrow morning."
    show sc germanartist o010
    a"I just have to make sure I send a reply to the gallery when we get home, to tell them not to pick her up, and that she’s arrived at the hotel safe and sound."
    show sc germanartist o011
    a"Once we have the German artist, I’ll use her phone so it looks like she’s responding from her email."
    show sc germanartist o012
    mc"I can help you to get it from her."
    show sc germanartist o013
    a"Thanks."
    show sc germanartist o014
    mc"You never cease to amaze me, [a_name]."
    show sc germanartist o015
    mc"You’ve managed to cover all those small details that the rest of us wouldn’t be able to do."
    show sc germanartist o016
    a"It’s no big deal. I just want to do my bit."
    show sc germanartist o017
    a"So do you have any idea what she looks like?"
    #The MC and Ariel have a conversation
    show sc germanartist o018
    mc"Kind of."
    show sc germanartist o019
    mc"When I went to the acting theater with [mc_v_address], she gave me an idea of how this woman would be dressed."

    if v_ep03_01_06_continue_talking_with_Vivian == True:
        #Add these lines if the player selected "Continue talking" during Scene 01-06
        show sc germanartist o020
        mc"And she should be a blonde because that’s the wig [mc_v_address] was wearing the other night when I spoke to her."
        show sc germanartist o021
        a"Well, hopefully she sees this sign, and believes that we’re from the art gallery."
        show sc germanartist o022
        mc"Just let me do most of the talking."

    #the German Artist walks out - she needs to look similar to how Vivian is dressed in the acting theatre scene - the green dress, but a different colour
    #Make sure she’s very attractive, but also a snob
    show sc germanartist o023
    with dissolve
    pause 1.5
    show sc germanartist o024
    with dissolve
    mc"I think that’s her now."
    a"Let's hope that she buys our fake accents and your moustache."
    #She comes up to the MC and Ariel who is holding the sign with her name on it
    show sc germanartist o025
    a"Miss Veerhart?"
    show sc germanartist o026
    mv"Ja, that is me."
    #[Use your real name / Use a fake name]
    menu:
        "Use your real name":
            show sc germanartist o027
            mc"Hi there. I’m [y_name] [lastname] and this is my associate, Violet Periwinkle."
            $ v_ep03_german_woman_real_name_used = True
        "Use a fake name"(wt="Task point"):
            show sc germanartist o027
            mc"Hi there. I’m Gunther Spretzle and this is my associate, Violet Periwinkle."
            $ v_ep03_task_13_german_woman_counter += 1
    show sc germanartist o028
    a"We’re from the art gallery."
    show sc germanartist o029
    mv"You look too young to be from art gallery."
    #She looks at them suspiciously
    show sc germanartist o030
    mv"I not be looked after by kids from nursery!"
    #She’s being a real bitch about the situation
    show sc germanartist o031
    mc"We’re on work experience, and the directors tasked us with making sure you get to your hotel safe and sound."
    show sc germanartist o028
    a"So if you could follow us, please."
    show sc germanartist o032
    a"I’m sure you’re probably tired from your flight and would like to get some rest."
    show sc germanartist o033
    mv"UGHH!"
    show sc germanartist o034
    mv"Das ist Blödsinn..."
    #Suitcase help / Don't help her
    menu:
        "Offer to help her"(wt="Task point"):
            show sc germanartist o035
            mc"Allow me to help you get your suitcase from the baggage claim area, Miss Veerhart."
            $ v_ep03_task_13_german_woman_counter += 1
        "Don't help her":
            show sc germanartist o038a
            mv"Get my things from baggage claim area!"
            show sc germanartist o027
            mc"Sure thing."
            show sc germanartist o034
            mc"(You snotty bitch.)"
    #The MC takes her luggage
    show sc germanartist o036
    a"There’s a car waiting for you outside to take you to your hotel."
    show sc germanartist o037
    mc"We’ll be escorting you there and can discuss tomorrow’s event with you on the way."
    show sc germanartist o038a
    mv"Ja. Fine..."
    show sc germanartist o039
    with dissolve
    pause 2.0
    stop ambient fadeout 2.0
    #The MC and Ariel walk behind Miss Veerhart with her luggage as she walks ahead of them, she’s still an angry woman

    #screen dissolves
    play music "sound effects/02/Airport Lounge.mp3" loop fadein 1.0
    #now show the limo parked outside in Airport arrivals - https://limousinesinparadise.com.au/wp-content/uploads/limo_airport.jpg
    show sc germanartist o040
    with dissolve
    pause 1.5
    #show the limo on the road with Victor standing outside - https://allvalleylimo.com/wp-content/uploads/2019/05/airport-pickup.jpg
    show sc germanartist o041
    with dissolve
    pause 1.5
    #show MV getting into the back seat of the limo
    show sc germanartist o042
    with dissolve
    pause 1.5
    #show the MC putting her luggage in the boot of the car - https://www.driveme2.com.au/wp-content/uploads/2019/11/chauffeur-placing-luggage-in-boot-of-limousine-768x513.jpg
    show sc germanartist o043
    with dissolve
    pause 1.5
    #the car takes off, departing from the airport
    show sc germanartist o044
    with dissolve
    pause 1.5
    #Ariel and the MC watch it leave
    show sc germanartist o045
    with dissolve
    pause 1.5
    show sc germanartist o046
    with dissolve
    mc"Okay, we better get back to the house."
    show sc germanartist o047
    a"[mc_v_address!c] should be here to pick us up shortly..."
    stop music fadeout 2.0
    #Final shot of Ariel and the MC waiting at airport arrivals outside
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    play ambient "sound effects/01/car_interior_ambience.ogg" loop fadein 2.0
    #show the limo driving on the road
    show sc germanartist o048
    with dissolve
    pause 1.5
    #show inside the limo - Victor is driving
    show sc germanartist o049
    with dissolve
    pause 1.5
    #the divider between him and the German woman is open
    show sc germanartist o050
    with dissolve
    pause 1.5
    #she looks confused, wondering where the MC and Ariel are
    show sc germanartist o051
    with dissolve
    mv"Hey, where has young man and young woman from art gallery gone?"
    show sc germanartist o052
    mv"We are meant to be discussing tomorrow’s event."
    show sc germanartist o049
    with dissolve
    pause 1.5
    #Victor says nothing
    show sc germanartist o056
    mv"HEY!"
    show sc germanartist o054
    mv"ANSWER ME!"
    show sc germanartist o055
    mv"I AM SPEAKING TO YOU!"
    #Victor pushes a button so that the window divider in the limo goes up so she can’t speak to him or see him
    #SOUND EFFECT FOR ELECTRONIC WINDOW GOING UP
    play sound "sound effects/03/electric_window_sound_effect.mp3" noloop
    show sc germanartist o057
    with dissolve
    pause 2.0
    show sc germanartist o058
    mv"What are you doing??"
    #It is closed and she is now angry
    show sc germanartist o059
    mv"Open up!"
    #she bangs on the divider - BANGING SOUND EFFECT
    play sound "sound effects/03/pounding_the_wall_effect.mp3" noloop
    show sc germanartist o060
    with dissolve
    pause 2.0
    stop sound fadeout 1.0
    play sound "sound effects/03/gas_leak_sound.mp3" fadein 1.0 noloop
    #some gas starts to enter the back seat of the limo - GAS LEAKING SOUND EFFECT
    show sc germanartist o061
    with dissolve
    mv"Huh?"
    #the gas reaches her face
    show sc germanartist o061
    with dissolve
    pause 0.5
    show sc germanartist o062
    with dissolve
    mv"What is this?"
    show sc germanartist o063
    with dissolve
    pause 1.0
    show sc germanartist o064
    with dissolve
    mv"I..."
    show sc germanartist o065
    with dissolve
    mv"I..."
    show sc germanartist o066
    with dissolve
    pause 1.5
    #her eyes roll in the back of her head and she passes out
    show sc germanartist o067
    with dissolve
    pause 0.5
    stop sound fadeout 1.0
    #she slumps down on the back seat
    #The limo continues to drive
    stop ambient fadeout 2.0
    #screen fades and continues
    play music "sound effects/01/Cool Vibes.mp3" loop fadein 1.0
    show sc germanartist o068
    with Dissolve(2.0)
    pause 2.0
    #Victor carries the German woman into the house and stores her in the basement
    show sc germanartist o069
    with dissolve
    pause 1.5
    #he straps her to a single bed and then blindfolds her
    show sc germanartist o070
    with dissolve
    pause 1.5
    #he ties only her wrists to the bed posts
    show sc germanartist o071
    with dissolve
    pause 1.5
    #show the German woman tied to the bed, unconscious
    show sc germanartist o072
    with dissolve
    pause 1.5
    #Victor goes up the wooden stairs in the basement
    stop music fadeout 2.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    centered "Meanwhile, upstairs...{w=2.0}{nw}" with dissolve
    show text "Meanwhile, upstairs..."
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/03/Montauk Point.mp3" loop fadein 1.0
    show sc germanartist o067
    #show the MC upstairs with Ariel, Bella, and Vivian
    #the MC and Ariel are still dressed in the clothes they wore at the airport
    show sc germanartist o073
    with dissolve
    pause 2.0
    show sc germanartist o074
    with dissolve
    b"So how was it?"
    show sc germanartist o075
    b"Do you think she suspected anything when she spoke to you two?"
    show sc germanartist o076
    a"Unlikely."
    show sc germanartist o077
    mc"I don’t think she’d be able to recognise either of us if she ever saw [a_name] or myself again."
    show sc germanartist o078
    with dissolve
    pause 1.5
    #Victor enters the room after being in the basement
    show sc germanartist o079
    with dissolve
    vic"Okay, she’s restrained."
    show sc germanartist o080
    vic"We’ll have to make sure we feed her before we go to the event tomorrow and also when we return home."
    show sc germanartist o081
    vic"[v_name] will be able to keep an eye on her tomorrow evening for an hour or so while the rest of us are at the gallery."
    show sc germanartist o082
    a"Do you have her phone?"
    show sc germanartist o083
    vic"Oh... shit."
    show sc germanartist o084
    vic"Sorry, I forgot to bring it up with me."
    show sc germanartist o085
    mc"Really? You? Forgetful?"
    show sc germanartist o086
    with dissolve
    mc"That’s so unlike you, [mc_vic_address]."
    #MC asks sarcastic and cocky here
    show sc germanartist o087
    mc"Lately, I’ve learned that it’s best to remember {b}everything{/b}, to take in every single detail."

    mc"Especially the important stuff which at any time could affect people in this [private_group], do you know what I mean?"
    show sc germanartist o080
    vic"Don’t push your luck, [y_name]."
    show sc germanartist o085
    mc"Or you’ll do what, huh?"
    show sc germanartist o089
    b"What on earth are you two arguing about?"
    show sc germanartist o090
    b"We have the German artist now. So why the animosity?"
    show sc germanartist o091
    mc"No reason."
    show sc germanartist o077
    mc"Put it down to it being a really tense week for all of us, where one slip-up could be catastrophic, right [mc_vic_address]?"

    #Victor replies through gritted teeth
    show sc germanartist o092
    vic"Yes, it has been tense."
    show sc germanartist o093
    vic"(The first chance I get, he's going to pay for this.)"
    show sc germanartist o094
    vic"You go and get that woman's phone for [a_name]."
    show sc germanartist o095
    vic"I’m going upstairs to take a shower."
    show sc germanartist o096
    vic"Just make sure you don’t engage in conversation with her if she happens to wake up."
    show sc germanartist o097
    mc"I’ll be sure not to do that."
    show sc germanartist o098
    with dissolve
    pause 1.5
    #Victor leaves the room with an annoyed look on his face

    #the MC moves to the kitchen
    show sc germanartist o099
    with dissolve
    mc"I’m just going to have something to eat as I’m starving, and then I’ll quickly get out of these clothes."
    show sc germanartist o100
    with dissolve
    mc"After I’ve done that, I’ll go and get that phone for you, [a_mc_rel]."
    show sc germanartist o101
    a"Thanks, [y_name]."
    show sc germanartist o102
    a"No rush, take your time..."
    #The final shot is of Ariel smiling at the MC while he is in the kitchen
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    centered "A little later on...{w=2.0}{nw}" with dissolve
    show text "A little later on..."
    scene bg black with Dissolve(1)
    pause 1.0
    show sc germanartist o105
    with dissolve
    pause 2.0
    #show the MC walking down the basement stairs
    play music "sound effects/02/Dances and Dames.mp3" loop fadein 1.0
    #show him on the ground floor in the basement
    show sc germanartist o106
    with dissolve
    pause 1.5
    #The MC looks down at the sleeping woman, while she has her blindfold on and her wrists are strapped.
    show sc germanartist o107
    with dissolve
    pause 1.5
    #the MC kneels at her side and starts to pad her body down, checking her dress, careful where his hands are placed
    show sc germanartist o108
    with dissolve
    mc"(Hmm...)"
    show sc germanartist o108
    mc"(It’s not on her.)"
    #He looks confused
    show sc germanartist o109
    with dissolve
    pause 1.5

    #[Keep searching her  / Look around the room ]
    #"Keep searching her" leads to some lewd sexual content
    menu:
        "Keep searching her"(wt="Task point"):
            #The MC checks out her cleavage
            show sc germanartist o110
            with dissolve
            pause 1.5
            #A smile crosses his face
            show sc germanartist o111
            with dissolve
            pause 1.5
            $ v_ep03_task_13_german_woman_counter += 1
            #check her chest / Look around the room
            menu:
                "Check her chest":
                    #The MC gropes her breasts
                    show sc germanartist o112
                    with dissolve
                    pause 1.5
                    mc"Mmm..."
                    show sc germanartist o113
                    with dissolve
                    pause 1.5

                    #Try somewhere else / Look around the room]
                    menu:
                        "Try somewhere else":
                            #The MC moves further down where he is still kneeling at the side of the bed
                            show sc germanartist o114
                            with dissolve
                            pause 1.5
                            #He is near her hips and thigh area
                            show sc germanartist o115
                            with dissolve
                            pause 1.5
                            #He places his hand on the top of her upper thigh
                            show sc germanartist o116
                            with dissolve
                            mc"(Damn she has nice legs and such a tight figure.)"
                            #He looks cocky here
                            show sc germanartist o117
                            with dissolve
                            mc"(Just a shame about that stick up her ass!)"
                            #His expression changes her
                            #The MC moves her legs apart so he can see her underwear
                            show sc germanartist o118
                            with dissolve
                            pause 1.5
                            #A devilish smile crosses his face
                            show sc germanartist o119
                            with dissolve
                            pause 1.5
                            #He caresses her inner thigh
                            show sc germanartist o120
                            with dissolve
                            pause 1.5
                            show sc germanartist o121
                            with dissolve
                            pause 1.5
                            #He moves his hand closer to her underwear, ready to touch her between her legs
                            show sc germanartist o122
                            with vpunch
                            mv"HEY!"
                            #with vpunch
                            #screen shakes
                            show sc germanartist o123
                            mv"Who's touching me?"
                            show sc germanartist o124
                            mc"(Oh shit!)"
                            show sc germanartist o125
                            mv"Take this blindfold off!"
                            #The German woman is awake, but cannot see due to blindfold
                            show sc germanartist o126
                            pause 1.0
                            #she moves and struggles on the bed, restricted by the ropes tying her to the bedposts
                            show sc germanartist o127
                            mv"Take these things off me or I scream!"

                            menu:
                                "Find a rag to silence her":
                                    #The MC locates a clean rag close by and picks it up
                                    show sc germanartist o128
                                    with dissolve
                                    pause 1.5
                                    show sc germanartist o129
                                    with dissolve
                                    mc"You won’t be doing anything like that, lady..."
                                    #He then stuffs in it the German woman’s mouth to stop her from taking
                                    show sc germanartist o140
                                    with dissolve
                                    pause 1.5
                                    show sc germanartist o141
                                    mv"Mfmfmfmfmfmfmf!"
                                    #She tries to talk but can’t
                                            #scene continues
                                    show sc germanartist o132
                                    with dissolve
                                    pause 1.5
                                    #The MC looks around the room while the German woman is gagged
                                    show sc germanartist o133
                                    with dissolve
                                    pause 1.5
                                    #The MC sees her handbag on the floor against a wall in the basement
                                    show sc germanartist o134
                                    with dissolve
                                    pause 1.5
                                    #He goes over to it and reaches in, pulling out her phone
                                    show sc germanartist o135
                                    with dissolve
                                    pause 1.5
                                    #The MC looks at the phone screen
                                    show sc germanartist o142
                                    with dissolve
                                    pause 1.5
                                    #then takes one last look at the German woman lying on the bed
                                    #NOTE - You’ll need two render versions here for this line - one with the gag in her mouth ("Find a gag"), the other with her panties in her mouth ("Something else")
                                    show sc germanartist o138
                                    with dissolve
                                    pause 1.5
                                    #And then the MC makes his way towards the stairs
                                    if v_ep03_task_13_german_woman_counter == 5:
                                        $ task_completed(13,"aa")
                                        $ v_ep03_othergirls_aa_tasks_counter +=1
                                    if v_ep03_task_13_german_woman_counter == 4:
                                        $ task_completed(13,"a")
                                    if v_ep03_task_13_german_woman_counter == 3:
                                        $ task_completed(13,"b")
                                    if v_ep03_task_13_german_woman_counter <= 2:
                                        $ task_completed(13,"c")
                                    #he walks up the stairs and leaves the basement room
                                    stop music fadeout 2.0
                                    #screen goes blank
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)
                                    jump lb_ep03_03_03_Ariel_speaks_with_the_MC

                                "Mess around with her":

                                    #The MC looks around but can’t find anything to use
                                    show sc germanartist o109
                                    with dissolve
                                    pause 1.5
                                    #He looks down at the German woman again
                                    show sc germanartist o108
                                    with dissolve
                                    pause 1.5
                                    #he has a devilish look on his face again
                                    show sc germanartist o121
                                    with dissolve
                                    pause 1.5
                                    #He kneels down and parts her legs
                                    show sc germanartist o127
                                    with dissolve
                                    mv"What are you doing?!?"

                                    #the MC runs his hands under the side of her outer thighs and under her dress
                                    show sc germanartist o143
                                    mv"Get your hands away from me!"
                                    show sc germanartist o144
                                    with dissolve
                                    pause 1.5
                                    #The MC snaps her panties off
                                    show sc germanartist o145
                                    with dissolve
                                    pause 1.5
                                    show sc germanartist o146
                                    with vpunch
                                    mv"UHHH!!"
                                    show sc germanartist o127
                                    mv"You son of bitch!"

                                    mv"When I get you, I will-"

                                    #She is cut off when the MC stuffs the German woman’s panties in her mouth to stop her from talking
                                    show sc germanartist o147
                                    with vpunch
                                    mc"There, that’s better."
                                    mv"Mfmfmfmfmfmfmf!"
                                    #She tries to talk but can’t

                                    #the MC pushes her legs apart so he can see her pussy

                                    #We see a close-up of her pussy


                                    #scene continues
                                    show sc germanartist o132
                                    with dissolve
                                    pause 1.5
                                    #The MC looks around the room while the German woman is gagged
                                    show sc germanartist o133
                                    with dissolve
                                    pause 1.5
                                    #The MC sees her handbag on the floor against a wall in the basement
                                    show sc germanartist o134
                                    with dissolve
                                    pause 1.5
                                    #He goes over to it and reaches in, pulling out her phone
                                    show sc germanartist o135
                                    with dissolve
                                    pause 1.5
                                    #The MC looks at the phone screen
                                    show sc germanartist o136
                                    with dissolve
                                    pause 1.5
                                    #then takes one last look at the German woman lying on the bed
                                    #NOTE - You’ll need two render versions here for this line - one with the gag in her mouth ("Find a gag"), the other with her panties in her mouth ("Something else")
                                    show sc germanartist o138
                                    with dissolve
                                    pause 1.5
                                    #And then the MC makes his way towards the stairs
                                    if v_ep03_task_13_german_woman_counter == 5:
                                        $ task_completed(13,"aa")
                                        $ v_ep03_othergirls_aa_tasks_counter +=1
                                    if v_ep03_task_13_german_woman_counter == 4:
                                        $ task_completed(13,"a")
                                    if v_ep03_task_13_german_woman_counter == 3:
                                        $ task_completed(13,"b")
                                    if v_ep03_task_13_german_woman_counter <= 2:
                                        $ task_completed(13,"c")
                                    #he walks up the stairs and leaves the basement room
                                    stop music fadeout 2.0
                                    #screen goes blank
                                    scene black
                                    with dissolve
                                    scene black
                                    with Pause (2)
                                    jump lb_ep03_03_03_Ariel_speaks_with_the_MC

                        "Look around the room":

                            #The MC looks around the room while the German woman is gagged
                            show sc germanartist o133
                            with dissolve
                            pause 1.5
                            #The MC sees her handbag on the floor against a wall in the basement
                            show sc germanartist o134
                            with dissolve
                            pause 1.5
                            #He goes over to it and reaches in, pulling out her phone
                            show sc germanartist o135
                            with dissolve
                            pause 1.5
                            $ v_ep03_task_13_german_woman_counter += 1
                            #The MC looks at the phone screen
                            #then takes one last look at the German woman lying on the bed - no gag, she’s still unconscious
                            show sc germanartist o139
                            with dissolve
                            pause 1.5
                            if v_ep03_task_13_german_woman_counter == 5:
                                $ task_completed(13,"aa")
                                $ v_ep03_othergirls_aa_tasks_counter +=1
                            if v_ep03_task_13_german_woman_counter == 4:
                                $ task_completed(13,"a")
                            if v_ep03_task_13_german_woman_counter == 3:
                                $ task_completed(13,"b")
                            if v_ep03_task_13_german_woman_counter <= 2:
                                $ task_completed(13,"c")
                            #he walks up the stairs and leaves the basement room
                            show sc germanartist o138
                            with dissolve
                            pause 1.5
                            #screen goes blank


                            scene black
                            with dissolve
                            scene black
                            with Pause (2)
                            jump lb_ep03_03_03_Ariel_speaks_with_the_MC


                "Look around the room"(wt="Task point"):

                    #The MC looks around the room while the German woman is gagged
                    show sc germanartist o133
                    with dissolve
                    pause 1.5
                    #The MC sees her handbag on the floor against a wall in the basement
                    show sc germanartist o134
                    with dissolve
                    pause 1.5
                    #He goes over to it and reaches in, pulling out her phone
                    show sc germanartist o135
                    with dissolve
                    pause 1.5
                    $ v_ep03_task_13_german_woman_counter += 2
                    #The MC looks at the phone screen
                    #then takes one last look at the German woman lying on the bed - no gag, she’s still unconscious
                    show sc germanartist o139
                    with dissolve
                    pause 1.5
                    if v_ep03_task_13_german_woman_counter == 5:
                        $ task_completed(13,"aa")
                        $ v_ep03_othergirls_aa_tasks_counter +=1
                    if v_ep03_task_13_german_woman_counter == 4:
                        $ task_completed(13,"a")
                    if v_ep03_task_13_german_woman_counter == 3:
                        $ task_completed(13,"b")
                    if v_ep03_task_13_german_woman_counter <= 2:
                        $ task_completed(13,"c")
                    #he walks up the stairs and leaves the basement room
                    show sc germanartist o138
                    with dissolve
                    pause 1.5
                    #screen goes blank


                    scene black
                    with dissolve
                    scene black
                    with Pause (2)
                    jump lb_ep03_03_03_Ariel_speaks_with_the_MC


        "Look around the room":
            #Renders here can be copied from the other “Look around the room” option above
            #The MC looks around the room while the German woman is gagged
            show sc germanartist o133
            with dissolve
            pause 1.5
            #The MC sees her handbag on the floor against a wall in the basement
            show sc germanartist o134
            with dissolve
            pause 1.5
            #He goes over to it and reaches in, pulling out her phone
            show sc germanartist o135
            with dissolve
            pause 1.5
            #The MC looks at the phone screen
            #then takes one last look at the German woman lying on the bed - no gag, she’s still unconscious
            show sc germanartist o139
            with dissolve
            pause 1.5
            if v_ep03_task_13_german_woman_counter == 5:
                $ task_completed(13,"aa")
            if v_ep03_task_13_german_woman_counter == 4:
                $ task_completed(13,"a")
            if v_ep03_task_13_german_woman_counter == 3:
                $ task_completed(13,"b")
            if v_ep03_task_13_german_woman_counter <= 2:
                $ task_completed(13,"c")
            #he walks up the stairs and leaves the basement room
            show sc germanartist o138
            with dissolve
            pause 1.5
            stop music fadeout 2.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep03_03_03_Ariel_speaks_with_the_MC
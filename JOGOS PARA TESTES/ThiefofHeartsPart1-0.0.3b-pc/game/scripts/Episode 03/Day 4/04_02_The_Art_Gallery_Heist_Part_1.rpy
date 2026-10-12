init:
    $ v_ep03_task_14_helping_the_team = 0


label lb_ep03_04_02_The_Art_Gallery_Heist_Part_1:
    #AFTERNOON - THE ART GALLERY FUNCTION
    #The scene begins with the MC and Bella entering the art gallery - there are already several guests in attendance present
    play music "sound effects/03/Shades of Spring.mp3" loop fadein 1.0
    play ambient "sound effects/01/people_talking_at_party.ogg" loop fadein 1.0
    scene sc ep3heistpart1 j001
    b"Okay, we’re inside the gallery and the party has already started."
    b"There's quite a few guests here already."
    show sc ep3heistpart1 j009
    vic"As expected."
    show sc ep3heistpart1 j002
    mc"What’s the visual like on your end, [a_name]?"
    #He grabs his bow tie
    show sc ep3heistpart1 j003
    a"Yeah, it’s very clear from both of you."
    #show Ariel in the truck looking at visuals from the MC’s bow tie and Bella’s pendant
    #the MC and Bella look around
    #Make sure that the MC and Bella are moving in and amongst the gallery guests while they are talking with Ariel

    show sc ep3heistpart1 j004
    mc"We can see six guards who are either manning the doors or patrolling the gallery."
    $ image_sequence("sc ep3heistpart1", ["j005", "j006", "j007"], 1.7)
    # show sc ep3heistpart1 j005
    # with dissolve
    # pause 1.5
    # show sc ep3heistpart1 j006
    # with dissolve
    # pause 1.5
    # show sc ep3heistpart1 j007
    # with dissolve
    # pause 1.5
    #Show the guards manned on doors and/or walking around the room
    show sc ep3heistpart1 j008
    with dissolve
    a"I see them."
    show sc ep3heistpart1 j009
    vic"Very soon all the guests will be escorted into the main room where the painting is."
    show sc ep3heistpart1 j010
    vic"When that happens, you two hang towards the back of the group."
    show sc ep3heistpart1 j011
    b"How come?"
    show sc ep3heistpart1 j012
    a"There will be an access door inside that room."
    a"It should be at the other end of the room to where the painting is that we’re going to steal."
    show sc ep3heistpart1 j013
    a"According to the previous footage I’ve reviewed, there shouldn’t be any members of security guarding that door as you need to have a pass to access it."
    show sc ep3heistpart1 j012
    a"[y_name], do you have the security pass you stole from that guy?"
    #the MC checks his pockets and pulls it out
    show sc ep3heistpart1 j014
    with dissolve
    pause 1.0
    show sc ep3heistpart1 j015
    with dissolve
    mc"Yes, I have it."
    show sc ep3heistpart1 j016
    a"Great."
    show sc ep3heistpart1 j012
    a"At the right time, I’ll temporarily kill the security footage within the gallery so it doesn’t show you guys leaving the gala room."
    show sc ep3heistpart1 j013
    a"So just wait for my signal."
    show sc ep3heistpart1 j017
    mc"Roger that."
    show sc ep3heistpart1 j018
    mc"Everything all right where you are, [mc_v_address]?"
    show sc ep3heistpart1 j019
    v"Yeah, I’m okay for now."
    #show Vivian in her own space, looking over one of the paintings
    show sc ep3heistpart1 j020
    v"They don’t suspect a thing... yet."
    show sc ep3heistpart1 j021
    v"How long will [y_name] and [b_name] need to find this underground emergency access door?"
    show sc ep3heistpart1 j009
    vic"It should take no more than fifteen minutes."
    vic"Keep an eye on the time when you have to speak before all the guests and the gallery directors."
    show sc ep3heistpart1 j010
    vic"Do not finish talking until you see [y_name] and [b_name] rejoin the party."
    show sc ep3heistpart1 j022
    v"I’ll do my best."
    #Vivian looks concerned
    show sc ep3heistpart1 j023
    woman"Excuse me, Miss Geerhart?"
    #An elderly woman and man come up to her
    show sc ep3heistpart1 j024
    v"Ja? What is it that you want?"
    show sc ep3heistpart1 j025
    woman"Oh, it is you!"
    show sc ep3heistpart1 j026
    woman"My husband and I just wanted to say that we are big fans of your work."
    woman"I have your \"Nude Adonis\" painting in a special room in my home."
    show sc ep3heistpart1 j027
    v"Oh, is good, ya?"
    show sc ep3heistpart1 j028
    woman"It is um, how do you say fantastic where you’re from?"
    show sc ep3heistpart1 j029
    v"Fantastisch..."
    show sc ep3heistpart1 j028
    woman"Oh, so not too dissimilar."
    show sc ep3heistpart1 j029
    v"Excuse me, must speak with other people."
    #Vivian looks desperate to leave the conversation
    show sc ep3heistpart1 j026
    woman"Yes, of course, of course."
    stop music fadeout 1.0
    #Vivian looks relieved they didn’t ask her any more questions
    #One of the Art Gallery coordinators speaks on the microphone
    show sc ep3heistpart1 j031
    with dissolve
    play sound2 "sound effects/03/announcement_chime.ogg"
    if persistent.v_sounds_text_on == True:
        "(PA System){w=2.0}{nw}"
    else:
        pause 2.5
    play sound3 "sound effects/03/PA_Announcement1.mp3"
    if persistent.v_sounds_text_on == True:
        "{i}Welcome everyone to this very prestigious event.{/i}{w=4.0}{nw}"
    else:
        pause 4.0
    #The audience hushes, to allow the gallery director to speak
    stop sound3 fadeout 4.0
    play sound2 "sound effects/03/PA_Announcement2.mp3"
    if persistent.v_sounds_text_on == True:
        "{i}We ask that you please make your way through to the gala room, as our main event will begin very shortly.{/i}{w=6.0}{nw}"
    else:
        pause 6.0
    stop sound2 fadeout 4.0
    show sc ep3heistpart1 j032
    with dissolve
    pause 2.0
    #the crowd starts making their way into the gala room - this room: https://pixhost.to/show/422/523899726_sc-artgallery-a120.jpg
    #show Bella and the MC are the last ones to enter the room
    #screen goes blank
    $ renpy.music.set_volume(0.4, 2.0, channel="ambient")
    scene black
    with dissolve
    scene black
    with Pause (2)
    #Sound effect - small chatter by the attendees and guests
    #the MC and Bella enter the gala room, standing towards the back of the attendees present in the room
    play music "sound effects/03/Art Gallery Plans5.mp3" loop fadein 1.0
    show sc ep3heistpart1 j033
    with dissolve
    pause 2.0
    show sc ep3heistpart1 j034
    with dissolve
    mc"You still there, [a_name]?"
    show sc ep3heistpart1 j035
    a"Yeah, I’m here."
    show sc ep3heistpart1 j036
    a"Tell me what you can see."
    show sc ep3heistpart1 j037
    b"There’s just one guard in this room. Another two are outside at the entrance but they can’t see us from where we are currently."
    show sc ep3heistpart1 j038
    b"The guy that we can see is currently doing his rounds and keeping an eye on the attendees."
    #show this member of security moving around the gallery
    show sc ep3heistpart1 j039
    a"They’ll probably have someone in their control room keeping watch through their cameras in that next room."
    show sc ep3heistpart1 j040
    v"I’ll try and attract the security guy’s attention long enough for [b_name] and [y_name] to get through that door."
    show sc ep3heistpart1 j041
    mc"Good luck."
    show sc ep3heistpart1 j042
    v"Excuse me, you, security man."
    #Vivian attracts the security guy’s attention
    show sc ep3heistpart1 j043
    v"Come here."
    show sc ep3heistpart1 j044
    security"No can do, miss."
    show sc ep3heistpart1 j045
    v"Excuse me?"
    #Vivian looks angry
    #a worried art gallery director comes over to Vivian
    show sc ep3heistpart1 j046
    "What seems to be the problem, miss?"
    show sc ep3heistpart1 j047
    v"Your security man will not help me."
    show sc ep3heistpart1 j048
    "One moment madam. I will fix this for you."
    show sc ep3heistpart1 j049
    "Hey, you! What is your name?"
    #a member of the art gallery addresses the member of the security
    show sc ep3heistpart1 j050
    security"It’s Evans, Sir."
    show sc ep3heistpart1 j051
    "Miss Veerhart is our special guest. If she asks you for your services, you will give them to her."
    "Is that understood?"
    #The member from the Art Gallery stands very close to the security guy. He looks sternly at the MC.
    show sc ep3heistpart1 j052
    security"Yes, Sir."
    #The security guy looks worried
    show sc ep3heistpart1 j053
    security"How may I help you, Miss Veerhart?"
    show sc ep3heistpart1 j054
    v"There are too many people trying to make chit-chat with me."
    show sc ep3heistpart1 j055
    v"Can you stand in their way, while I am here at gallery so I not speak to them?"
    show sc ep3heistpart1 j056
    security"Yes, I can do that for you, miss."
    show sc ep3heistpart1 j057
    a"Okay, [mc_v_address] has this guy occupied."
    show sc ep3heistpart1 j058
    a"Carefully make your way towards that access door guys."
    show sc ep3heistpart1 j059
    mc"Roger that."
    show sc ep3heistpart1 j060
    mc"Let’s go [b_name]."
    #The MC and Bella break away from the attendees as one of the art gallery directors speaks to the attendees
    #screen goes blank
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.0, 2.0, channel="ambient")
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ renpy.music.set_volume(0.4, 1.0, channel="ambient")
    show sc ep3heistpart1 j061
    with dissolve
    "May I have your attention again, please."
    stop ambient fadeout 2.0
    #she stands to the side of the painting with a microphone in hand
    #The audience hushes, to allow her to speak - SOUND EFFECT AMBIENCE
    show sc ep3heistpart1 j062
    "Thank you."
    "The gallery has hosted many wonderful events since its inception in 1935."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc ep3heistpart1 j063
    "We’ve had the fortune of hosting functions for some of the greatest artists in the world."
    "And they have also allowed us the chance to showcase their fine work within the walls of our gallery."
    show sc ep3heistpart1 j064
    "Today, we have a very special treat for you all."
    "After years of repeated requests for her to be our guest of honour, earlier this year, she finally responded."
    show sc ep3heistpart1 j065
    "Hailing from Bochum, a city in Western Germany... Would you please give a warm welcome to the incredibly gifted artist..."
    "The one and only, Miss Helga Veerhart."
    play sound "sound effects/01/light_clapping_sound_effect.mp3" fadein 1.0
    show sc ep3heistpart1 j066
    with dissolve
    pause 3.0
    #small room clapping applause - SOUND effect
    #Vivian makes her way to where the Gallery Director is standing, while the security guy escorts her
    #show the MC and Bella are on their way to the security door
    stop sound fadeout 1.0
    play music "sound effects/01/Rollin at 5 - 210 - full.mp3" loop fadein 1.0
    show sc ep3heistpart1 j067
    with dissolve
    a"Okay, I’m going to intercept the security cameras within the gallery."
    show sc ep3heistpart1 j068
    a"They’ll be scrambled for about five to ten seconds."
    show sc ep3heistpart1 j069
    a"In that time, you need to open the door, get through, and close it before their screens come back up."
    show sc ep3heistpart1 j070
    a"Are you ready?"
    show sc ep3heistpart1 j071
    mc"Yeah, let’s do this."
    show sc ep3heistpart1 j057
    a"Okay..."
    show sc ep3heistpart1 j058
    a"Cutting transmission..."
    show sc ep3heistpart1 j072
    a"NOW!"
    #Ariel touches her enter/return button as she says NOW
    #Show the security control room office - the guy looks at all his monitors showing static - https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeSOvMRP00rVqLdW0hhKioFz0uB9tv4_hT7Q&s
    show sc ep3heistpart1 j073
    with vpunch
    "What the hell??"
    #the guy in the control room office looks baffled. He spills his coffee as he sits up
    show sc ep3heistpart1 j075
    "DAMMIT!!"
    #the MC and Bella get to the door
    show sc ep3heistpart1 j076
    with dissolve
    pause 2.0
    #The MC swipes the pass card over the screen. The green light comes up
    #The MC opens the door
    play sound [ "<silence .5>","sound effects/01/card_swipe.ogg"]
    show sc ep3heistpart1 j077
    with dissolve
    pause 2.0
    #Bella and the MC exit, then close the door behind them
    play sound2 [ "<silence .5>","sound effects/01/door_buzz.mp3"]
    play sound3 [ "<silence .5>","sound effects/01/door_bolt_unlocking.mp3"]
    show sc ep3heistpart1 j078
    with dissolve
    mc"We're in."
    show sc ep3heistpart1 j079
    with dissolve
    pause 2.0
    #show the guy in the office where all the vision comes back - https://c8.alamy.com/comp/KBKB9F/rear-view-of-security-system-operator-looking-at-cctv-footage-at-desk-KBKB9F.jpg
    show sc ep3heistpart1 j080
    with dissolve
    pause 2.0
    show sc ep3heistpart1 j081
    "(Phew! That was a scary ten or so seconds...)"
    #the security guy in the office goes back to relaxing in the control room
    #The screen goes blank
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    #show the MC and Bella in a quiet corridor of the art gallery
    #spy music plays here
    play music "sound effects/01/Private Eye.mp3" loop fadein 1.0
    show sc ep3heistpart1 j082
    with dissolve
    pause 2.0
    show sc ep3heistpart1 j083
    with dissolve
    mc"Okay, we’re in some kind of corridor."
    show sc ep3heistpart1 j084
    a"There should be a trap door on the floor ahead of you on the right."
    a"Do you see it?"
    #they see it on the floor - https://i.pinimg.com/736x/ba/53/61/ba53617ae94740613e9bc9e7f03e521e.jpg - https://i.redd.it/w9hv71tjh9m51.jpg
    $ image_sequence("sc ep3heistpart1", ["j197", "j198"], 1.5)
    # show sc ep3heistpart1 j197
    # with dissolve
    # pause 1.5
    # show sc ep3heistpart1 j198
    # with dissolve
    # pause 1.5
    show sc ep3heistpart1 j086
    with dissolve
    b"Yeah, we got it."
    show sc ep3heistpart1 j087
    a"Open it up, and it will take you underneath the gallery."
    show sc ep3heistpart1 j088
    a"It’s a bit of a maze down there but you should see the emergency exit door as soon as you’re in the underground."
    show sc ep3heistpart1 j089
    mc"All right, we’ll let you know shortly."

    #the MC opens the door and finds a metal ladder that takes them into the underground - https://www.jomy.com/Manhole-ladder---Sewer-ladder---Well-ladder---Shaft-ladder-in-aluminium_clg6086.jpg
    #https://www.shutterstock.com/image-photo/old-empty-abandoned-bunker-interior-260nw-614366042.jpg

    #[Go first / Let [b_name] go first]
    menu:
        "Go first"(wt="Task point"):
            show sc ep3heistpart1 j090
            with dissolve
            mc"..."
            $ v_ep01_bella_arrogant_counter += 1
            #the MC goes in first, climbs down the steps
            $ image_sequence("sc ep3heistpart1", ["j091", "j092", "j093", "j094", "j097"], 1.6)
            # show sc ep3heistpart1 j091
            # with dissolve
            # pause 1.3
            # #then Bella follows
            # show sc ep3heistpart1 j092
            # with dissolve
            # pause 1.3
            # #the MC looks up and sees under her dress
            # show sc ep3heistpart1 j093
            # with dissolve
            # pause 1.3
            # #a close-up shot of what he can see
            # show sc ep3heistpart1 j094
            # with dissolve
            # pause 1.3
            $ v_ep03_task_14_helping_the_team += 1
        "Let [b_name] go first":
            show sc ep3heistpart1 j092
            with dissolve
            b"..."
            $ v_ep01_bella_respect_counter += 1
            #Bella goes down the steps first
            $ image_sequence("sc ep3heistpart1", ["j093", "j094", "j091", "j095", "j096", "j097"], 1.6)
            # show sc ep3heistpart1 j093
            # with dissolve
            # pause 1.3
            # #
            # #then the MC follows
            # show sc ep3heistpart1 j094
            # with dissolve
            # pause 1.3
            # #
            # #the MC looks down and he sees her huge cleavage at the top of her dress
            # show sc ep3heistpart1 j091
            # with dissolve
            # pause 1.3
            # #a close-up shot of what he can see
            # show sc ep3heistpart1 j095
            # with dissolve
            # pause 1.3
            # #
            # show sc ep3heistpart1 j096
            # with dissolve
            # pause 1.3

    #scene continues
    #the MC and Bella are in the underground (underneath the art gallery) - https://budacastlebudapest.com/wp-content/uploads/2023/08/Buda-Castle-Cave-Tour-Budapest-Underground-Labyrinth-scaled.jpeg
    stop music fadeout 4.0
    pause 2.0
    play music "sound effects/03/cave_sound_effect.mp3" loop fadein 1.0
    show sc ep3heistpart1 j098
    with dissolve
    mc"Okay, we’re down in the underground section, [a_name]."
    show sc ep3heistpart1 j099
    mc"[a_name]...?"

    "..."
    show sc ep3heistpart1 j100
    mc"Shit, I think we lost her."
    show sc ep3heistpart1 j101
    b"Yeah, I have radio silence from her too."
    #Bella checks her earpiece as she says this
    show sc ep3heistpart1 j102
    mc"Looks like we’re on our own."
    #they look around and see a door with the word Emergency Exit on it
    show sc ep3heistpart1 j103
    mc"That must be the emergency door she mentioned."
    show sc ep3heistpart1 j104
    with dissolve
    pause 2.0
    #they go over to it and stand before the door
    show sc ep3heistpart1 j105
    with dissolve
    b"What are we going to do? We can’t just leave it unlocked from the inside."
    show sc ep3heistpart1 j106
    b"Plus one of the alarms could go off if we try and open it."
    show sc ep3heistpart1 j108
    mc"I was preparing for this to happen."
    #the MC surveys the door frame and sees two wires running across the top-left side of the door frame - https://pixhost.to/show/435/524064422_screenshot-2024-10-21-at-10-43-50-am.jpg
    mc"Give me a second."

    #the MC reaches the inside of his pocket and pulls out some safety pliers - https://cdn.thewirecutter.com/wp-content/media/2022/04/wirecutters-2048px-9011.jpg?auto=webp&quality=75&width=1024
    show sc ep3heistpart1 j109
    with dissolve
    pause 1.5
    show sc ep3heistpart1 j110
    with dissolve
    b"What are you doing?"
    show sc ep3heistpart1 j111
    mc"Watch and learn."
    show sc ep3heistpart1 j112
    with dissolve
    pause 1.0
    show sc ep3heistpart1 j188
    mc"Red wire."
    play sound "sound effects/03/cutting_wire_sound_effect.mp3"
    show sc ep3heistpart1 j189
    pause 1.5
    #the MC cuts the red wire and then the blue wire - https://ktcables.com.au/wp-content/uploads/2018/10/KT3MM30RBE.jpg
    #clipping sound effect
    show sc ep3heistpart1 j112
    mc"Then the blue wire..."
    #clipping sound
    play sound "sound effects/03/cutting_wire_sound_effect.mp3"
    show sc ep3heistpart1 j190
    pause 1.5
    show sc ep3heistpart1 j113
    b"What now?"
    show sc ep3heistpart1 j114
    mc"Now we see if it worked."
    show sc ep3heistpart1 j110
    b"Oh geez..."
    #the MC goes to push the door open
    show sc ep3heistpart1 j115
    with dissolve
    pause 1.3
    #Bella braces herself
    show sc ep3heistpart1 j116
    with dissolve
    pause 1.3
    play sound "sound effects/03/metal_door_opening_effect.mp3"
    #the door opens and no alarm goes off
    #door opening sound effect
    show sc ep3heistpart1 j117
    with dissolve
    mc"A-ha!"
    show sc ep3heistpart1 j118
    mc"Worked like a charm."
    show sc ep3heistpart1 j119
    b"Where did you learn how to do that?"
    show sc ep3heistpart1 j123
    mc"There’s a lot you don’t know about me, [b_name]."
    show sc ep3heistpart1 j121
    mc"I’ve been fracturing an occasional law ever since birth."
    show sc ep3heistpart1 j122
    b"Yeah, yeah..."
    #Bella looks at him bemused
    show sc ep3heistpart1 j123
    mc"Come on, let’s get back to this party before anyone notices that we’re gone..."
    #screen goes blank
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #show the MC and Bella walking calmly through a quiet section of the gallery that is just outside the gala room (NOT the corridor they were in before they found the emergency exit)
    play music "sound effects/03/Shadows of Deception.mp3" loop fadein 1.0
    show sc ep3heistpart1 j124
    with dissolve
    pause 2.0
    show sc ep3heistpart1 j125
    with dissolve
    mc"We’re almost there."
    show sc ep3heistpart1 j126
    mc"Remember, we need to act casually when we get back into this party."
    show sc ep3heistpart1 j127
    b"I know the plan, [y_name]."
    #She looks at him while the MC looks forward
    #the MC looks up ahead and sees a member of security coming the other way who hasn’t seen them yet
    #Bella hasn’t noticed him yet either
    show sc ep3heistpart1 j128
    with dissolve
    pause 1.3
    show sc ep3heistpart1 j129
    mc"(Oh, fuck!)"

    if bella_love_level >= 2:
        #If the player has at least TWO Bella hearts, this scene will play out

        #the MC turns to Bella and grabs her shoulders
        show sc ep3heistpart1 j130
        with dissolve
        pause 1.0
        show sc ep3heistpart1 j131
        b"[y_name], what the hell are you do-"

        #Bella gets cut off when the MC kisses her

        #Bella stops being angry and loses herself in the kiss
        show sc ep3heistpart1 j132
        b"(Why is he...)"
        #she closes her eyes and enjoys the kiss
        play sound "sound effects/01/kiss_and_moan_sound_effect01.mp3" noloop
        show sc ep3heistpart1 j133
        b"Mmm..."
        #she closes her eyes and savours the kiss
        show sc ep3heistpart1 j134
        b"(I know that time is of the essence but this feels pretty nice.)"
        stop sound fadeout 1.0
        show sc ep3heistpart1 j135
        security"Hey! What are you two doing out here??"
        #the security guy shouts at them
        #Bella and the MC stop kissing and turn to see the security guy
        show sc ep3heistpart1 j136
        with dissolve
        mc"Oh, thank God we found you!"
        show sc ep3heistpart1 j137
        mc"My girlfriend and I took a wrong turn and she was starting to panic."
        show sc ep3heistpart1 j138
        with dissolve
        mc"Sorry you had to see that, I was just trying to comfort her."
        show sc ep3heistpart1 j139
        mc"She’s such a worrier."
        show sc ep3heistpart1 j141
        b"(Oh... So that’s why he kissed me.)"
        show sc ep3heistpart1 j142a
        security"Yeah, I’ll bet you were."
        show sc ep3heistpart1 j143
        b"Our apologies, Sir. We didn’t mean to cause any trouble."
        show sc ep3heistpart1 j144
        b"We’re here for the party."
        show sc ep3heistpart1 j145
        b"Would you be so kind as to escort us back, please?"
        #Bella bats her eyelids at him, trying to look innocent
        show sc ep3heistpart1 j142
        security"Well... fine. But only because you asked so nicely."
        show sc ep3heistpart1 j146
        security"Follow me. And don’t touch anything."

        #the security guy turns and the MC and Bella follow

        #they whisper to each other while they follow the security guy
        show sc ep3heistpart1 j147
        b"{i}(*Whispering*){/i}\nPretty smooth move, [y_name]."
        show sc ep3heistpart1 j148
        mc"{i}(*Whispering*){/i}\nHey, it was our best play. And it worked, didn’t it?"
        show sc ep3heistpart1 j149
        b"{i}(*Whispering*){/i}\nYeah, this time..."
        show sc ep3heistpart1 j150
        with dissolve
        pause 2.0
        stop music fadeout 1.0
        #Final shot of them walking behind the security guy, a sexy smirk on Bella’s face
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)

    else:
        #If the player has less than TWO Bella hearts, this scene will play out
        show sc ep3heistpart1 j151
        with dissolve
        security"Hey! What are you two doing out here??"
        #the security guy shouts at them
        show sc ep3heistpart1 j152
        b"Oh, sorry, Sir."
        show sc ep3heistpart1 j153
        b"My guest and I took a wrong turn and he was starting to panic."
        show sc ep3heistpart1 j154
        b"And he badly needed to use the bathroom."
        show sc ep3heistpart1 j155
        b"He drinks like a fish this one."
        #The MC looks at her annoyed
        show sc ep3heistpart1 j157
        security"You two shouldn’t be here. This is a restricted access area."
        show sc ep3heistpart1 j156
        b"We understand. And we didn’t mean to cause any trouble."
        show sc ep3heistpart1 j145
        b"Would you be so kind as to escort us back to the party, please?"
        #Bella bats her eyelids at him, trying to look innocent
        show sc ep3heistpart1 j142
        security"Well... fine. But only because you asked so nicely."
        show sc ep3heistpart1 j146
        security"Follow me. And don’t touch anything."

        #the security guy turns and the MC and Bella follow

        #they whisper to each other while they follow the security guy
        show sc ep3heistpart1 j148
        mc"{i}(*Whispering*){/i}\nMaybe next time, give me a heads-up when you’re going to take the lead like that, [b_name]."
        show sc ep3heistpart1 j159
        b"{i}(*Whispering*){/i}\nI didn’t want you thinking. You’re not very good at that."
        show sc ep3heistpart1 j160
        mc"Pftt!"
        #He scoffs at her reply and tries to think of a reply
        show sc ep3heistpart1 j161
        b"{i}(*Whispering*){/i}\nOh, look at you, searching for a witty comeback."
        show sc ep3heistpart1 j199
        mc"{i}(*Whispering*){/i}\nScrew you."
        show sc ep3heistpart1 j149
        b"{i}(*Whispering*){/i}\nHow very George Orwell of you."
        show sc ep3heistpart1 j150
        with dissolve
        pause 1.5

        #Final shot of them walking behind the security guy, a cocky smirk on Bella’s face
        #screen goes blank
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)

    #the MC and Bella return to the party where Vivian speaks with the guests and answers questions

    show sc ep3heistpart1 j191
    with dissolve
    pause 2.0
    show sc ep3heistpart1 j163
    with dissolve
    woman"So who would say is your greatest inspiration for this specific piece of work, Miss Veerhart?"
    show sc ep3heistpart1 j164
    v"I would say it was my mother."
    show sc ep3heistpart1 j168
    v"She was very troubled woman, quite insecure, even though she had kind nature."
    show sc ep3heistpart1 j169
    v"In my work, I wanted to capture something of her mood, using memories from childhood."
    show sc ep3heistpart1 j167
    woman"What was her reaction when she saw it?"
    show sc ep3heistpart1 j193
    v"She did not. She passed away before she ever got chance."
    show sc ep3heistpart1 j166
    woman"But in your book, it said that she was still alive when you’re painting was first unveiled to the public."
    show sc ep3heistpart1 j168
    v"The book is not always accurate to every event."
    show sc ep3heistpart1 j193
    v"In final years of her life, my mother rarely left house, not even her bedroom, so she couldn’t see painting I made for her."
    show sc ep3heistpart1 j165
    v"Even showing her photos on my phone, she did not believe I painted it. Her mind had already declined so much."
    show sc ep3heistpart1 j166
    woman"Oh, I see..."
    #the guest looks embarrassed by her questions
    show sc ep3heistpart1 j194
    mc"{i}(*Whispering*){/i}\nDamn, she’s good."
    #the MC stands beside Bella, watching on
    show sc ep3heistpart1 j192
    b"{i}(*Whispering*){/i}\nYeah, [mc_v_address] has them all fooled."
    #the art gallery directors address all of the attendees
    show sc ep3heistpart1 j172
    "Okay, I think that should just about do it."
    show sc ep3heistpart1 j173
    "Miss Veerhart will not be answering any more questions."
    show sc ep3heistpart1 j174
    "Can we please give her a round of applause for attending today and sharing her valuable time with us this afternoon?"
    #audience applause
    play sound "sound effects/01/light_clapping_sound_effect.mp3" noloop
    show sc ep3heistpart1 j175
    vic"All right, phase one is just about done."
    #Victor speaks to the group
    show sc ep3heistpart1 j195
    vic"You two should start making your way out of there as soon as you can."
    #show Bella and the MC listening in
    show sc ep3heistpart1 j196
    b"{i}(*Whispering*){/i}\nWhat about [mc_v_address]?"
    show sc ep3heistpart1 j178
    v"{i}(*Whispering*){/i}\nDon’t wait for me, I’ll be right behind you..."
    #Vivian speaks into her earpiece
    #show the MC and Bella leaving the gala room together
    #screen goes blank
    stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    centered "Sometime later...{w=2.0}{nw}" with dissolve
    show text "Sometime later..."
    scene bg black with Dissolve(1)
    pause 1.0
    #show the MC and Bella leaving the art gallery together
    #they hop into their waiting car
    play music "sound effects/01/Cool Vibes.mp3" loop fadein 1.0
    $ image_sequence("sc ep3heistpart1", ["j180", "j181", "j183", "j184", "j185", "j186"], 1.9)
    # show sc ep3heistpart1 j180
    # with dissolve
    # pause 1.5
    # #and drive off together.
    # show sc ep3heistpart1 j181
    # with dissolve
    # pause 1.5
    # #show Vivian being escorted out of the front of the art gallery by the gallery director
    # #he walks her to the limo that is parked out the front, driven by Victor
    # show sc ep3heistpart1 j183
    # with dissolve
    # pause 1.5
    # #Vivian enters the car
    # show sc ep3heistpart1 j184
    # with dissolve
    # pause 1.5
    # #Victor drives the car off and away from the gallery
    # show sc ep3heistpart1 j185
    # with dissolve
    # pause 1.5
    # #
    # show sc ep3heistpart1 j186
    # with dissolve
    # pause 1.5
    #screen goes blank
    stop music fadeout 3.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_04_03_The_Art_Gallery_Heist_Part_2

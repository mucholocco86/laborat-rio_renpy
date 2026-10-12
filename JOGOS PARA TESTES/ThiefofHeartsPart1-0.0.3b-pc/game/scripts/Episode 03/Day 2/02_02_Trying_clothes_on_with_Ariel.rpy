init:
    $ v_ep03_02_02_ariel_suit = ""
    $ v_ep03_ariel_hearts_counter = 0

label lb_ep03_02_02_Trying_clothes_on_with_Ariel:
    #The scene begins with the MC waiting outside Bella’s store for Ariel to arrive
    #Street ambience
    centered "Later that morning...{w=2.0}{nw}" with dissolve
    show text "Later that morning..."
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    scene sc eparieltask n001
    with dissolve
    pause 2.0
    #Ariel arrives, wearing her glasses
    play music "sound effects/01/Whispering Aisles1.mp3" loop fadein 1.0
    show sc eparieltask n002
    with dissolve
    a"Hey..."
    show sc eparieltask n003
    mc"Hey, [a_name]."
    show sc eparieltask n004
    a"Have you been waiting long?"
    show sc eparieltask n005
    mc"Nah, just a few minutes."
    show sc eparieltask n006
    mc"But now that you’re here, we can head in and get what we need."
    show sc eparieltask n007
    a"Sounds good."
    #she smiles
    #Ariel and the MC head into the store
    #The doorbell rings
    #they see Bella serving a female customer
    stop ambient fadeout 1.0
    stop music fadeout 3.0
    play music2 "sound effects/01/Shiny Days.mp3" loop fadein 3.0
    play sound "sound effects/01/convenience_store_ring.mp3" noloop
    show sc eparieltask n008
    with dissolve
    pause 1.5
    show sc eparieltask n009
    with dissolve
    b"Thanks, have a great day."
    #the customer leaves the store after the MC and Ariel enter
    play sound "sound effects/01/convenience_store_ring.mp3" noloop
    show sc eparieltask n010
    with dissolve
    pause 1.0
    show sc eparieltask n011
    with faster_dissolve
    b"That was honestly the most hideous dress that this guy bought for his daughter."
    #She addresses the MC and Ariel
    show sc eparieltask n012
    a"Then why did you sell it to him?"
    show sc eparieltask n013
    b"Because I get a good commission from it."
    show sc eparieltask n014
    b"And he was incredibly pushy and quite arrogant."
    show sc eparieltask n015
    mc"It's great to see you have your priorities in check, [b_name]."
    show sc eparieltask n016
    b"But of course!"
    #she responds cheekily and also sarcastically
    #She moves out from behind the counter
    show sc eparieltask n017
    with dissolve
    b"Now that it’s quiet, we can talk."
    show sc eparieltask n018
    b"The rack over there are your options, and I’ve added some of my own recommendations for both of you."
    show sc eparieltask n019
    a"Why can’t we choose something from the other racks?"
    show sc eparieltask n020
    b"Because they’re higher-priced options and my boss is more likely to notice that they’re missing."
    show sc eparieltask n021
    b"The clothes I’ve picked are either out of season or we have plenty of them in stock."
    show sc eparieltask n022
    b"Try them on until you find something suitable."
    #The doorbell rings as two more people enter the store
    play sound "sound effects/01/convenience_store_ring.mp3" noloop
    show sc eparieltask n023
    with dissolve
    pause 1.0
    show sc eparieltask n024
    with dissolve
    b"I’ll come and see you both when I can."
    #Bella attends to the customers
    show sc eparieltask n025
    with dissolve
    b"Hi there, how can I help you?"
    #Attention returns to the MC and Ariel
    show sc eparieltask n026
    with dissolve
    mc"I guess we should take a look at what clothes she’s selected for us."
    show sc eparieltask n027
    with dissolve
    pause 1.0
    #Ariel and the MC head over to a rack of various clothing that is situated in the middle of the aisle
    show sc eparieltask n028
    with dissolve
    pause 1.0
    #show them going through various pieces
    show sc eparieltask n029
    with dissolve
    pause 1.0
    #holding them up in front of them with different facial expressions
    show sc eparieltask n030
    with dissolve
    pause 1.0
    #the MC holds up a long-sleeved white shirt
    show sc eparieltask n031
    mc"I’m going to try this one on."
    show sc eparieltask n032
    a"Is that what [mc_vic_address] has asked you to wear?"
    show sc eparieltask n033
    mc"It fits the description that he gave me."
    show sc eparieltask n035
    a"I can’t believe we’re doing this."
    #She looks worried
    show sc eparieltask n036
    a"I never thought we’d have to resort to such an act."
    show sc eparieltask n037
    mc"I know, but it’s the only way to make sure this job goes off without a hitch."
    show sc eparieltask n038
    a"(Sigh...)"
    show sc eparieltask n039
    a"Okay, well, I better find some clothes."
    show sc eparieltask n040
    mc"You’ll be with me to greet this woman when she arrives, so there’s no need to worry."
    show sc eparieltask n041
    mc"Try and find something that looks professional, so that she’s convinced that you’re affiliated with the art gallery."
    show sc eparieltask n042
    a"All right, I’ll see what I can find..."
    stop music2 fadeout 2.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The scene returns with the MC in the changing room

    #Make sure that there’s a mirror inside the changing room
    play music "sound effects/01/Painting Dreams1.mp3" loop fadein 2.0
    show sc eparieltask n043
    with dissolve
    mc"..."
    #the MC can see Ariel peering her head into his changing room from the reflection on the mirror
    show sc eparieltask n044
    with dissolve
    pause 1.5
    #[Let her look / Call out to her]
    menu:
        "Let her look"(wt="Best option"):
            #show the MC undoing his shirt
            show sc eparieltask n045
            with dissolve
            pause 1.5
            #Ariel peeks through the changing room door to spy on the MC
            $ v_ep01_ariel_cocky_counter += 1
            #show the MC undoing his pants
            show sc eparieltask n046
            with dissolve
            a"(Oh my!)"
            show sc eparieltask n047
            with dissolve
            pause 1.5
            #show the MC putting on long black trousers
            show sc eparieltask n052
            with dissolve
            a"(I shouldn’t be spying on [y_name], but I can’t help it.)"
            #show the MC putting on a white long-sleeved shirt
            show sc eparieltask n048
            with dissolve
            pause 1.5
            show sc eparieltask n049
            with dissolve
            pause 1.5
            #then his black suit jacket
            show sc eparieltask n050
            with dissolve
            a"(Wow... He looks great.)"
            show sc eparieltask n051
            with dissolve
            a"(He definitely looks convincing.)"
            #then he looks in the mirror to do up his tie

            #he now looks like this - https://www.shutterstock.com/image-photo/portrait-handsome-chauffeur-near-luxury-260nw-1994929418.jpg (but without a hat, sunglasses or gloves - Victor will give him those)
            #ADD ONE ARIEL HEART FOR ONLY THE PLAYERS WHO CURRENTLY HAVE ZERO OR ONE ARIEL POINT AT THIS POINT IN THE GAME
            show sc eparieltask n052
            with dissolve
            pause 1.5
            a"(Oh geez! He’s on his way out!)"
            $ v_ep03_01_05_shopping_with_Ariel +=1
            #the MC exits the changing room and asks Ariel her thoughts
            #screen goes blank
            stop music fadeout 2.0
            scene black
            with dissolve
            scene black
            with Pause (2)

        "Call out to her"(wt="Bonus Image"):
            #he doesn’t turn around while he calls out to her so that she’ll leave and have no idea the MC knows she was watching him change
            show sc eparieltask n053
            mc "Hey, [a_name]? Are you still out there?"
            $ v_ep01_ariel_respect_counter += 1
            #Ariel backs away from the curtain
            show sc eparieltask n052
            a"(Oh God, I better not let him see me.)"
            $ rewards_unlock ("ariel",12)
            show sc eparieltask n052a
            with dissolve
            pause 1.5
            show sc eparieltask n054
            with dissolve
            pause 1.5
            show sc eparieltask n055
            with dissolve
            pause 1.5
            #MC smiles as he sees Ariel leave from the changing room door
            #screen goes blank
            stop music fadeout 2.0
            scene black
            with dissolve
            scene black
            with Pause (2)


    #the MC exits the changing room
    #He looks around and sees Ariel nervously looking over the clothes rack
    play music "sound effects/01/Walking on Sunshine2.mp3" loop fadein 1.0
    show sc eparieltask n056
    mc"So, what do you think?"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n059a at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n059b
        with dissolve
        pause 2.0
    #a render of the MC posing in his outfit
    scene sc eparieltask n060
    with dissolve
    a"Y-yeah… You look great."
    show sc eparieltask n058
    a"It’s just missing something."
    #Ariel thinking
    show sc eparieltask n062
    mc"Hmm… I’m sure I can come up with a way for me to look more like someone who is an official member of the art gallery."

    if bella_love_level >= 1:
        #NOTE: Only add these images/lines if the player has 1 or more Bella Hearts at this point in the game
        #Bella deals with some other customers and momentarily glances over to see the MC dressed up and showing his outfit off to Ariel
        show sc eparieltask n063
        with dissolve
        pause 1.0
        show sc eparieltask n064
        with dissolve
        b"(Well, well.. [y_name] looks pretty neat in those clothes.)"
        #Bella’s attention turns to the MC
        b"(I’m genuinely surprised.)"
        show sc eparieltask n065
        woman"Miss? I asked you a question."
        show sc eparieltask n066a
        b"Huh? Oh, yeah, this will look great on you."
        #Bella looks up and realises the customer is talking to her
        show sc eparieltask n067
        woman"But it’s a size twelve. I asked for a size eight!"
        show sc eparieltask n067a
        woman"Are you suggesting I’m fat?"
        show sc eparieltask n068
        b"Oh, no, not at all."
        #Bella panics and has to apologise
        show sc eparieltask n069
        b"Let me change that for you."
        #The woman has her arms folded, giving Bella an angry stare
        show sc eparieltask n070
        b"(Damn you, [y_name].)"
        #She’s agitated
        b"(Now this woman is pissed at me!)"
    show sc eparieltask n058
    with dissolve
    mc"Anyway, I'm going to change out of these clothes."
    show sc eparieltask n061
    a"Sweet. I'm gonna keep looking and then I'll show you my choices when you're back..."
    #scene returns to the MC and Ariel
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)


    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..."
    scene bg black with Dissolve(1)
    pause 1.0
    play music "sound effects/01/Breathe In Calm.mp3" loop fadein 1.0
    show sc eparieltask n071
    with dissolve
    mc"Are you still looking for clothes, [a_name]?"
    show sc eparieltask n072
    a"Um, yeah... It’s not as easy as I thought it would be."
    show sc eparieltask n073
    a"I have two designs that might be good, but I think I need another one."
    show sc eparieltask n074a
    mc"What about that dress over here?"
    #don’t show it, just make it look like the MC has found one for her
    show sc eparieltask n075
    a"Yeah, that one might do."
    show sc eparieltask n076
    a"All right, give me a few minutes to try each of them on."
    show sc eparieltask n077
    mc"No problems. Make sure to show me how they look on you."
    show sc eparieltask n078
    a"I will, for sure."
    #screen goes blank
    scene black
    with dissolve
    pause 2.0
    #Moments later
    #the MC stands outside the changing room
    show sc eparieltask n079
    with dissolve
    mc"Are you almost done in there?"
    show sc eparieltask n080
    a"Yep, I’m coming out now."
    stop music fadeout 1.0
    play music2 "sound effects/01/Imaginary_Heroes2.mp3" loop fadein 2.0
    show sc eparieltask n098
    with dissolve
    a"Okay, don’t laugh."
    #she peers her head out from behind the changing room curtain
    show sc eparieltask n099
    mc"Haha, I’ll try not to. I’m sure it’s not that bad."
    show sc eparieltask n100
    a"You just did. But all right, here it goes."

    #she’s wearing a suit like this - https://www.istanbulmeetandgreetservice.com/wp-content/uploads/2016/01/ataturk-airport-greeting.jpg.webp
    #You can reuse the same suit the girls wear in Sunshine Love - the red hotel uniforms

    #ROLLING WIP OF ARIEL IN THIS OUTFIT - FRONT SHOT
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n101 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n101a
        with dissolve
        pause 2.0
    #ROLLING WIP OF ARIEL IN THIS OUTFIT - BEHIND SHOT
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n102 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n102a
        with dissolve
        pause 2.0
    scene sc eparieltask n103
    with dissolve
    mc"I don’t see why you were so worried."
    show sc eparieltask n104
    a"I'm just not sure about this one. I look more like someone who works in a hotel resort."
    show sc eparieltask n105
    mc"You’re overthinking things, [a_name]."
    show sc eparieltask n106
    a"Probably."
    show sc eparieltask n107
    a"But do you think I’ll be able to convince this woman that I’m part of the art gallery?"
    show sc eparieltask n105
    mc"Let me see the other options before you make a final decision."
    show sc eparieltask n108
    a"Good idea."
    show sc eparieltask n106
    a"All right, let me try on the next one..."
    #screen goes blank
    scene black
    with dissolve
    pause 2.0
    #A few minutes later
    stop music2 fadeout 2.0
    play music "sound effects/01/Breathe In Calm1.mp3" loop fadein 1.0
    show sc eparieltask n089
    with dissolve
    pause 2.0
    show sc eparieltask n090
    with dissolve
    pause 2.0
    #the MC sits outside on the cushioned sofa waiting for Ariel
    #Ariel calls out from the changing room
    a"How’s this?"

    #she’s wearing a suit like this - https://media.istockphoto.com/id/802691832/vector/group-of-people-meet-someone-in-airport-hall.jpg?s=612x612&w=0&k=20&c=WDrn2Yd93J2f18QY4eheUAMi1WFW-wdAAfGMgsPjmk4=
    #She wears a black outfit to match the MC

    #ROLLING WIP OF ARIEL IN THIS OUTFIT - FRONT SHOT
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n091 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n091a
        with dissolve
        pause 2.0
    #ROLLING WIP OF ARIEL IN THIS OUTFIT - BEHIND SHOT
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n092 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n092a
        with dissolve
        pause 2.0
    scene sc eparieltask n093
    mc"Damn, that’s just as impressive as the first one."
    show sc eparieltask n094
    mc"And wearing glasses makes it even better."
    show sc eparieltask n095
    mc"This is gonna be a tough choice."
    show sc eparieltask n096
    a"While you’re deciding which one you think is better, I’m gonna change into the last option."
    show sc eparieltask n097
    mc"Can’t wait to see it!"
    #screen goes blank
    scene black
    with dissolve
    pause 2.0

    #the MC stands back as Ariel exits the changing room
    #IMPORTANT - Make sure all 3 of these outfits have a zipper in the back of the top

    #she’s wearing a suit like this - https://c8.alamy.com/comp/DBXX22/airport-staff-members-welcoming-passenger-in-airport-lobby-DBXX22.jpg
    #She wears a light grey pinstripe outfit
    show sc eparieltask n090
    with dissolve
    a"So, what do you think?"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n081 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n081b
        with dissolve
        pause 2.0
    #ROLLING WIP OF ARIEL IN THIS OUTFIT - FRONT SHOT

    #ROLLING WIP OF ARIEL IN THIS OUTFIT - BEHIND SHOT
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc eparieltask n082 at tt_top
        with dissolve
        pause 6.0
    elif True:
        show sc eparieltask n082b
        with dissolve
        pause 2.0
    mc"Very nice."
    scene sc eparieltask n083
    mc"You look very professional, [a_name]."
    show sc eparieltask n085
    a"Thanks."
    show sc eparieltask n087
    a"Okay, so which one did you like the most?"
    show sc eparieltask n115
    a"Which outfit do you think is the most believable that I could pass as someone from the art gallery?"
    #[Black / Red / Gray pinstripe]
    menu:
        "Black":
            #Create a variable for this suit for when the MC and Ariel greet the German artist at the airport
            show sc eparieltask n109
            mc"I think the black one suits you best."
            show sc eparieltask n111
            a"Really? How come?"
            show sc eparieltask n110
            mc"I think it will compliment my chosen attire perfectly."
            $ v_ep03_02_02_ariel_suit = "Black"

        "Red"(wt="Bonus Image"):
            #Create a variable for this suit for when the MC and Ariel greet the German artist at the airport
            show sc eparieltask n112
            mc"I know you have your doubts, but I still think the red one is the best choice."
            show sc eparieltask n111
            a"Really? How come?"
            show sc eparieltask n109
            mc"It’s more dynamic than the other two. It stands out more, and the colour red means passion and desire."
            $ rewards_unlock ("ariel",13)
            show sc eparieltask n110
            mc"If you can show your passion and desire for working at an art gallery, then this woman will believe you are representing them. "
            $ v_ep03_02_02_ariel_suit = "Red"

        "Gray pinstripe":
            #Create a variable for this suit for when the MC and Ariel greet the German artist at the airport
            show sc eparieltask n109
            mc"I personally like the gray pinstripe one you have on now."
            show sc eparieltask n110
            mc"It makes you stand out and looks very professional."
            $ v_ep03_02_02_ariel_suit = "Grey"
    show sc eparieltask n085
    a"Do you think this woman will question my age?"
    show sc eparieltask n086
    mc"Maybe, but that outfit should help to allay those concerns."
    show sc eparieltask n113
    a"Okay, I’ll let [b_name] know that I’ve made my choice."
    show sc eparieltask n114
    mc"Awesome!"
    show sc eparieltask n115
    a"I’ll change out of this suit and then we can get out of here."
    show sc eparieltask n116
    mc"No worries. I’ll be here when you’re ready..."
    #Ariel smiles
    #screen goes blank
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    #### THIS SCENE ONLY AVAILABLE IF THE PLAYER HAS 2+ ARIEL HEARTS
    if ariel_love_level >=2:
        centered "Several minutes later...{w=2.0}{nw}" with dissolve
        show text "Several minutes later..."
        scene bg black with Dissolve(1)
        pause 1.0
        #the MC waits on the seat for Ariel
        play music "sound effects/01/Velvet Touch1.mp3" loop fadein 1.0
        show sc eparieltask n117
        with dissolve
        pause 1.5
        play sound "sound effects/03/girl_scream2.mp3" noloop
        a"Aiiii!{w=1.0}{nw}" with hpunch
        show sc eparieltask n118
        with faster_dissolve
        pause 0.6
        a"[y_name]!"
        a"Are you still out there?"
        #She calls from inside the changing room
        show sc eparieltask n119
        mc"Yeah, I'm still here [a_name]? Are you all right?"
        show sc eparieltask n120
        a"I need your help! Can you come in here?"
        show sc eparieltask n119
        mc"I'm coming!"
        show sc eparieltask n122
        with dissolve
        pause 1.0
        #the MC stands up and approaches the changing room
        #he opens the curtain and sees that Ariel is still in her suit/outfit
        show sc eparieltask n123
        with dissolve
        mc"What’s wrong? Why did you scream just now?"
        show sc eparieltask n124
        a"I know this is going to sound crazy, but, I felt something crawling up my back."
        show sc eparieltask n125
        a"I think it might be a spider. Can you check for me?"
        show sc eparieltask n126
        mc"Um, okay."
        show sc eparieltask n201
        mc"But you might need to take your jacket off. We'll see."
        show sc eparieltask n202
        a"Oh... Okay."
        show sc eparieltask n125
        a"Just try and find it as quickly as possible, please."
        #the MC stands behind Ariel and helps with her jacket
        show sc eparieltask n203
        mc"Don't worry, I got this..."
        show sc eparieltask n127
        with dissolve
        mc"Give me a second here."
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene sc eparieltask n127a at tt_bottom
            pause 3.0
        elif True:
            scene sc eparieltask n127a
            pause 1.0
        show sc eparieltask n128
        mc"Okay, there's nothing on the back of your jacket."
        mc"Let's take it off."
        show sc eparieltask n193
        a"Oh... okay."
        scene black
        with dissolve
        pause 0.6
        #The MC removes her jacket
        show sc eparieltask n196
        with dissolve
        pause 1.0
        show sc eparieltask n194
        with dissolve
        mc"Hmm... I can't see anything on your blouse."
        #Show the MC looking at her blouse from behind Ariel
        show sc eparieltask n195
        mc"We should remove that too, just to be sure."
        #The MC pulls off her top without hesitating
        show sc eparieltask n129
        with faster_dissolve
        with vpunch
        pause 1.0
        show sc eparieltask n197
        with faster_dissolve
        pause 0.6
        show sc eparieltask n199
        with faster_dissolve
        with hpunch
        a"OH MY!!"
        #And then she removes her blouse under her jacket
        show sc eparieltask n192
        mc"Hey, why aren't you wearing a bra?"
        #The MC realises she has no bra on
        show sc eparieltask n198
        a"I uh... I took it off because wearing it with the suit and blouse felt uncomfortable."
        show sc eparieltask n132
        mc"Hmm...."
        #Ariel covers her chest so the MC can't see her breasts in the mirror reflection
        show sc eparieltask n133
        mc"Well, I don't see any spider or any creepy crawlies on your back."
        show sc eparieltask n134
        a"Phew... That's a relief."
        show sc eparieltask n209
        a"Maybe I was just imagining things."
        #A slightly different expression from Ariel here
        show sc eparieltask n210
        a"I'm just not used to wearing clothes like this so I probably freaked out for nothing."
        #A slightly different expression again from Ariel here
        show sc eparieltask n199
        a"Thanks, I’ll be able to change now."
        #The MC half-smiles while he speaks
        show sc eparieltask n135
        mc"No problems."

        #[Kiss her / Don’t kiss her]
        menu:
            "Kiss her"(wt="Best option"):
                play sound "sound effects/02/new_kissing_sound_FX.mp3" loop fadein 1.0
                show sc eparieltask n200
                with dissolve
                a"Mmm..."
                #The MC and Ariel kiss
                show sc eparieltask n136
                with dissolve
                pause 2.0
                stop sound fadeout 1.0
                show sc eparieltask n137
                with dissolve
                a"What was that for?"
                show sc eparieltask n138
                mc"I just felt like it."
                show sc eparieltask n139
                mc"Plus I like the idea of us kissing in a place where we could be caught."
                show sc eparieltask n140
                mc"Don’t you?"
                show sc eparieltask n141
                a"Oh... I guess so."
                #Ariel seems more enthusiastic about it
                play sound "sound effects/02/new_kissing_sound_FX1.mp3" loop fadein 1.0
                show sc eparieltask n200
                a"Mmm..."
                #The MC and Ariel kiss again
                #it’s a little awkward as she’s holding her dress up to stop it from falling down
                stop sound fadeout 1.0
                show sc eparieltask n142
                with dissolve
                a"Uh, I should get changed, if you don’t mind?"
                show sc eparieltask n143
                mc"Yes, of course."
                $ v_ep03_01_05_shopping_with_Ariel +=1
                #Scene continues below
            "Don’t kiss her":
                show sc eparieltask n142
                a"Uh, I should get changed, if you don’t mind?"
                show sc eparieltask n143
                mc"Yes, of course."
                #Scene continues below
        show sc eparieltask n129
        mc"I’ll wait outside until you’re done."
        stop music fadeout 1.0
        scene black
        with dissolve
        #the MC attempts to leave
        show sc eparieltask n145
        with dissolve
        pause 1.0
        #he peeks his head out and just outside of the changing room, he overhears Bella talking with a woman who turns out to be her boss
        play music2 "sound effects/01/Touch_and_Tension1.mp3" loop fadein 2.0
        show sc eparieltask n146
        with dissolve
        boss"We need to meet our quota this month, [b_name], otherwise, we could all be out of a job!"
        show sc eparieltask n147
        b"Yes, ma’am."
        show sc eparieltask n148
        mc"Geez...!"
        show sc eparieltask n149
        a"What’s wrong?"
        show sc eparieltask n150
        mc"It’s [b_name]. Her boss is in the store!"
        show sc eparieltask n151
        a"Oh God..."
        show sc eparieltask n152
        mc"It’s fine. Just keep quiet."
        show sc eparieltask n153
        mc"Are you done changing yet?"
        show sc eparieltask n154
        a"Yeah, give me a minute or so."
        show sc eparieltask n131
        a"Whatever you do, don’t turn around."
        show sc eparieltask n148
        mc"Sure..."
        stop music2 fadeout 2.0
        pause 1.0
        #NOTE: Only add these images/lines if the player has 2 or more Ariel Hearts at this point in the game
        #[Peek / Don’t look]
        play music "sound effects/01/Velvet Touch2.mp3" loop fadein 1.0
        menu:
            "Peek"(wt="Best option"):
                #The MC turns around slowly and sees Ariel changing
                show sc eparieltask n155
                with dissolve
                pause 2.0
                show sc eparieltask n156
                with dissolve
                pause 2.0
                $ v_ep01_ariel_cocky_counter += 1
                $ v_ep03_01_05_shopping_with_Ariel +=1
                #she’s removed the suit top and we see her naked back and skirt on
                #[Keep looking / Turn around]
                menu:
                    "Keep looking"(wt="Best option"):
                        show sc eparieltask n157
                        with dissolve
                        pause 2.0
                        $ v_ep01_ariel_cocky_counter += 1
                        $ v_ep03_01_05_shopping_with_Ariel +=1
                        #she’s removed the suit skirt and we see her naked back and Ariel in her underwear
                        #[Continue to look / Turn around
                        menu:
                            "Continue to look"(wt="Bonus Image"):
                                #she puts her original dress back on and turns to her side so the MC can see the side of her naked breast
                                show sc eparieltask n158
                                mc"Woah..."
                                $ rewards_unlock ("ariel",15)
                                #Ariel looks up and sees the MC staring at her
                                show sc eparieltask n159
                                with vpunch
                                a"[y_name!u]!!"
                                a"I told you not to turn around!"
                                #she turns to face him and covers her chest with her forearm
                                show sc eparieltask n160
                                mc"Sorry. I thought you were finished changing."
                                $ v_ep01_ariel_arrogant_counter += 1
                                show sc eparieltask n159
                                a"Well, I’m not."
                                show sc eparieltask n162
                                a"Now don’t turn around until I tell you."
                                show sc eparieltask n163
                                mc"Sorry, [a_name]."
                                #Go down to > #scene continues
                            "Turn around"(wt="Best option"):
                                show sc eparieltask n204
                                mc"(...)"
                                $ v_ep01_ariel_respect_counter += 1
                                $ v_ep03_01_05_shopping_with_Ariel +=1
                                #Go down to > #scene continues
                    "Turn around"(wt="Bonus Image"):
                        show sc eparieltask n204
                        mc"(...)"
                        $ rewards_unlock ("ariel",14)
                        $ v_ep01_ariel_respect_counter += 1
                    #Go down to > #scene continues
            "Don’t look":
                show sc eparieltask n204
                mc"(...)"
                $ v_ep01_ariel_respect_counter += 1
                #Go down to > #scene continues
        stop music fadeout 2.0
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        #scene continues
        #The MC peers out from the changing room
        show sc eparieltask n165
        mc"Okay, looks like [b_name]’s boss is gone. The coast is clear."
        show sc eparieltask n164
        mc"Let’s go, [a_name]."
        show sc eparieltask n166
        with dissolve
        pause 2.0
        if v_ep03_01_05_shopping_with_Ariel >= 5:
            $ ariel_love_level +=1
            $ v_ep03_ariel_hearts_counter +=1
        #Ariel who has changed now, follows the MC out
        play music "sound effects/01/Family Ties.mp3" loop fadein 2.0
        #they run into Bella
        show sc eparieltask n167
        with dissolve
        b"Hey, where did you two go?"
        show sc eparieltask n168
        mc"Oh, we were both in the changing room... Separately of course."
        #Ariel tries not to look guilty
        show sc eparieltask n181
        b"Are you two okay? I thought a scream before."
        show sc eparieltask n168
        mc"A scream?"
        show sc eparieltask n208
        mc"I didn't hear any scream."
        #The MC turns to Ariel
        show sc eparieltask n172
        mc"Did you hear a scream, [a_name]?"
        #Ariel looks at the MC
        show sc eparieltask n173
        a"I have no idea what she's talking about, [y_name]."
        #Bella looks sceptical, mouth closed with hands on her hips
        show sc eparieltask n207
        b"Hmm..."
        show sc eparieltask n171
    else:
        centered "Several minutes later...{w=2.0}{nw}" with dissolve
        show text "Several minutes later..."
        scene bg black with Dissolve(1)
        pause 1.0
        play music2 "sound effects/01/Touch_and_Tension1.mp3" loop fadein 2.0
        show sc eparieltask n145
        with dissolve
        pause 1.0
        #he peeks his head out and just outside of the changing room, he overhears Bella talking with a woman who turns out to be her boss
        show sc eparieltask n146
        with dissolve
        boss"We need to meet our quota this month, [b_name], otherwise, we could all be out of a job!"
        show sc eparieltask n147
        b"Yes, ma’am."
        show sc eparieltask n148
        mc"Geez...!"
        show sc eparieltask n151
        a"What’s wrong?"
        show sc eparieltask n150
        mc"It’s [b_name]. Her boss is in the store!"
        a"Oh God..."
        show sc eparieltask n152
        mc"It’s fine. Just keep quiet."
        show sc eparieltask n153
        mc"Are you done changing yet?"
        show sc eparieltask n131
        a"Yeah, give me a minute or so."
        show sc eparieltask n148
        mc"Sure..."
        stop music2 fadeout 2.0
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        play music "sound effects/01/Family Ties.mp3" loop fadein 2.0
        show sc eparieltask n165
        with dissolve
        mc"Okay, looks like [b_name]’s boss is gone. The coast is clear."
        show sc eparieltask n164
        mc"Let’s go, [a_name]."
        show sc eparieltask n166
        with dissolve
        pause 1.5
        show sc eparieltask n167
        with dissolve
        b"Hey, where did you two go?"
        show sc eparieltask n168
        mc"Oh, we were both using the changing rooms."
        show sc eparieltask n171
    b"So did you two find something you like?"
    show sc eparieltask n170
    a"Yeah, I found a really nice outfit."
    #no need to show it
    show sc eparieltask n169
    b"Ah, nice one."
    show sc eparieltask n180
    b"And you, [y_name]?"
    show sc eparieltask n172
    mc"I think I have what I need, don’t I [a_name]?"
    show sc eparieltask n173
    a"Yeah, he really did look like someone from the art gallery."
    show sc eparieltask n171
    b"Sweet!"
    show sc eparieltask n169
    b"Okay, just leave your clothing choices at the front counter and I’ll take care of the rest."
    show sc eparieltask n175
    a"Guys, I have to go. I have to start work in half an hour."
    show sc eparieltask n176
    a"I don’t want to be late."
    show sc eparieltask n177
    a"So I guess I’ll see you both for dinner."
    show sc eparieltask n178
    a"Bye."
    b"See ya, [a_name]."
    #Ariel waves and exits the store
    play sound "sound effects/01/convenience_store_ring.mp3" noloop
    show sc eparieltask n179
    mc"So what did your boss want?"
    show sc eparieltask n183
    mc"I couldn't help but overhear her conversation with you."
    show sc eparieltask n180
    b"Ughh... She’s been riding me a lot lately."
    show sc eparieltask n181
    b"She questioned my customer service skills and attitude."
    show sc eparieltask n182
    b"The sooner I can get out of this shitty job the better."
    show sc eparieltask n183
    mc"Well hopefully  this job at the art gallery will change things for all of us."
    show sc eparieltask n184
    b"Yeah, I’m counting on it."
    show sc eparieltask n185
    b"Speaking of which, do you have time to hang around for a little while longer?"
    show sc eparieltask n180
    b"I’d like you to try on some clothes that [vic_name] asked me to pick out for you."
    show sc eparieltask n186
    mc"What’s it for?"
    show sc eparieltask n205
    b"I’ll let you know once you’ve changed."
    show sc eparieltask n188
    b"The clothes are hanging up in the changing room over there."
    show sc eparieltask n206
    mc"Fine."
    #The MC seems annoyed
    show sc eparieltask n190
    b"I’ll see you back here shortly..."
    #the MC leaves for the changing room
    show sc eparieltask n191
    with dissolve
    pause 2.0
    stop music fadeout 2.0
    #final shot here of Bella closing the front door to the store.
    #show her turning around a sign that says “Back in 15 minutes"
    #Like this: https://i.etsystatic.com/9877706/r/il/96d09b/5665665615/il_570xN.5665665615_li17.jpg
    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_02_03_At_Bellas_clothing_store

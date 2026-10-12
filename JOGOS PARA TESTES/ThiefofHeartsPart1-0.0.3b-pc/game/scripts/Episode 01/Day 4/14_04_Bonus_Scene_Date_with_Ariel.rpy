init:
    $ v_ep01_14_01_Cafe_Scene_Fix = False

default v_ep01_ariel_dates_counter = 0

label lb_ep01_Bonus_Scene_Date_with_Ariel1:
    #THIS SCENE WILL ONLY TRIGGER IF THE PLAYER CHOSE "WORK WITH HER" DURING SCENE 05-01
    #scene begins back at the house, the MC in the hallway
    play music "sound effects/01/Breathe In Calm1.mp3" loop fadein 1.0
    scene sc cafeariel c001
    mc"(I think [a_name] is still in the house somewhere.)"
    #The MC sees Ariel in her room
    show sc cafeariel c003
    mc"(Ah, there she is.)"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    show sc cafeariel c006
    mc"[a_name]?"
    stop sound fadeout 1.0
    show sc cafeariel c005
    a"Oh, hey [y_name]."
    #She looks at her laptop screen
    show sc cafeariel c006
    a"(Sigh...)"
    show sc cafeariel c007
    mc"Something wrong?"
    show sc cafeariel c008
    a"I've been looking for information on that gang from the tattoo and I can't seem to find anything useful."
    show sc cafeariel c010
    a"Whoever they are, they've made it really hard for anyone to find them."
    a"It's quite frustrating. I almost always find something."
    show sc cafeariel c011
    mc"It sounds like you need a break."
    show sc cafeariel c012
    a"I did that already."
    show sc cafeariel c013
    mc"No, I mean you need to get out of the house."
    show sc cafeariel c009
    mc"I think you could do with some coffee or fresh air."
    show sc cafeariel c014
    a"Why would I do that?"
    show sc cafeariel c012
    a"I could just order coffee online and have it delivered."
    show sc cafeariel c011
    mc"I know, but you probably need a change of scenery."
    #The MC starts to walk out of her room
    show sc cafeariel c015
    mc"Grab your things and let's go."
    show sc cafeariel c016
    a"Where are we going...?"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #The MC and Ariel stand outside the coffee shop
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    show sc cafeariel c022a
    with dissolve
    mc"Here we are."
    #The MC looks at Ariel who looks worried
    show sc cafeariel c018
    mc"[a_name]?"
    show sc cafeariel c019
    a"..."
    #HYPER - maybe don't paint Ariel like she doesn't know the places outside. She has been outside a lot before her recent changes for school and also does she work in a shop - so she might know some spots in this town she lives for her whole life for sure.
    #HPYER - maybe make this coffee shop kind of new opened and Ariel hasn't seen it before nor was she there
    show sc cafeariel c020
    mc"Don't you like the place I chose?"
    show sc cafeariel c021
    a"It's not that, I just, I've never been here before is all."
    show sc cafeariel c022
    mc"Well, that makes sense."
    mc"It only just opened last week."
    show sc cafeariel c023
    mc"I've never been here before either, but I thought we could try it out. I've heard great things about it."
    show sc cafeariel c024
    a"Oh..."
    mc"What is it?"
    show sc cafeariel c026
    a"I um... I have this social phobia whenever I go to places I've never been to before."
    menu:
        "Find out why":
            show sc cafeariel c027
            mc"Since when? I've never known this to be a problem for you before."
            show sc cafeariel c029
            a"It's a more recent thing. It's kinda hard to explain."
            show sc cafeariel c028
            a"And you're right, I never used to be like this."
            show sc cafeariel c024
            mc"When do you think it all started?"
            show sc cafeariel c029
            a"Ever since I finished high school. And because I don't go to college, I don't really interact with anyone except for you guys."
            show sc cafeariel c028
            a"I'm fine at work because I'm usually in the back at my desk and I don't have to interact with anyone."
            show sc cafeariel c026
            a"I mean, there are other places in town I'm okay being at."
            show sc cafeariel c025
            a"You must think I'm crazy, huh?"
            show sc cafeariel c030
            mc"No, not at all."
            show sc cafeariel c024
            mc"We all have our own fears, our own anxieties..."
            mc"We can go somewhere else if you want?"
            show sc cafeariel c032
            a"No, no... I don't want to put you out."
            show sc cafeariel c033
            a"I'm just warning you that I might be awkward once we're in there."
        "Go into the cafe":
            pause 1.5
    show sc cafeariel c029
    mc"In that case, let me order for you and talk to the waiter or waitress."
    show sc cafeariel c034
    mc"Let's talk more when we're inside and at a table."
    #Ariel hesitantly enters the coffee shop with the MC
    show sc cafeariel c035
    mc"(I may have to help [a_name] in public places, so she can get used to being around other people again...)"
    stop ambient fadeout 1.0

    #cross-screen fade

    #the MC and Ariel sit in the diner/cafe - Setting options
    #https://www.daz3d.com/fg-60s-diner
    #https://daz3d.com/fg-cafe
    #https://www.daz3d.com/office-cafeteria
    #https://www.daz3d.com/the-coffee-shop
    #https://www.daz3d.com/fg-modern-coffee

    #The MC and Ariel approach the counter at the coffee shop
    #The cafe is very busy with most tables occupied
    play music "sound effects/01/Silent Dream1.mp3" loop fadein 1.0
    play ambient2 "sound effects/01/cafe_ambience.ogg" loop fadein 1.0
    show sc cafeariel c037
    with dissolve
    pause 1.0
    show sc cafeariel c038
    with dissolve
    barista"Hey guys, what can I get for you?"
    show sc cafeariel c039
    mc"I'll have an espresso with a lemon twist."
    show sc cafeariel c040
    mc"And you, [a_name]?"
    #Ariel looks down and away from the MC and the Barista
    show sc cafeariel c041
    mc"Um... She'll have an Iced Latte?"
    #Ariel nods and smiles
    show sc cafeariel c045
    barista"Very good."
    barista"Take a seat guys, and I'll have someone bring those out to you when they're ready."
    #The MC and Ariel make their way to a table

    #cross-screen fade
    #The MC and Ariel sit down at one of the booths/tables
    show sc cafeariel c046
    with dissolve
    pause 1.0
    show sc cafeariel c047
    with dissolve
    pause 1.0
    show sc cafeariel c048
    a"Thanks for ordering for me."
    show sc cafeariel c049
    a"How did you know that I wanted an Iced Latte?"
    show sc cafeariel c049
    mc"You forget that I can be very observant."
    show sc cafeariel c052
    mc"I've seen you drinking them when you're in the van or in your room."
    #Ariel smiles
    menu:
        "Ask about her fear":
            show sc cafeariel c053
            mc"So while we're waiting for our orders, tell me what worries you the most about being out in public?"
            show sc cafeariel c054
            a"Oh, well... I guess my biggest fear is being judged, or getting embarrassed if I do or say something wrong."
            show sc cafeariel c056
            a"When I'm in front of a computer or I have a set of headphones on, I'm perfectly calm."
            show sc cafeariel c057
            a"It's my safe space."
            show sc cafeariel c152
            mc"But what about when we went to the security warehouse together?"
            show sc cafeariel c053
            mc"You seemed pretty calm that day."
            show sc cafeariel c054
            a"Yeah, I was..."
            show sc cafeariel c048
            a"I think that's because you were there with me and I was more comfortable with those surroundings for the most part."
            show sc cafeariel c049
            a"And I'd prepared pretty well for that."
            show sc cafeariel c052
            mc"So being in here, in a cafe with only a few other people..."
            show sc cafeariel c053
            mc"How does that make you feel?"
            show sc cafeariel c068
            a"Anxious as all hell."
            show sc cafeariel c057
            a"I've never set foot in here before."
            a"You sprung it on me and when that happens, I start to overthink everything."
            show sc cafeariel c052
            mc"Well, just being here is a start."
            show sc cafeariel c053
            mc"Hmm..."
            mc"Okay, I'm going to help you."
            show sc cafeariel c077
            a"What do you mean?"
        "Make a suggestion":
            show sc cafeariel c050
            mc"So I've been thinking it over."
    show sc cafeariel c078
    mc"It seems like a social anxiety disorder. You have a social phobia."
    mc"It's not incurable, you just need to take things one step at a time."
    show sc cafeariel c068
    a"And you're going to help me?"
    show sc cafeariel c053
    mc"Yeah, of course. You have nothing to fear, [a_name]."
    show sc cafeariel c047
    mc"Sure, starting a conversation doesn't come naturally to everyone, especially in a social setting like this one."
    mc"It just takes practice."
    show sc cafeariel c083
    a"You make it sound so easy."
    show sc cafeariel c084
    mc"Anything worth doing isn't always easy."
    #The waitress brings their drinks
    show sc cafeariel c059
    waitress"Hey guys, I'm sorry about the wait."

    #Say something / Say nothing
    menu:
        "Say something"(wt="Best option"):
            show sc cafeariel c066
            mc"(Damn... She probably has no idea what she's showing everyone in this cafe!)"
            show sc cafeariel c068
            mc"(No doubt [a_name] noticed too.)"
            mc"(Well, I don't want her to feel any more uncomfortable than she already is.)"
            show sc cafeariel c060
            mc"Sorry miss... Don't be alarmed, but, you're um... \"showing\"."
            show sc cafeariel c153
            waitress"Oh, I'm so sorry!"
            #the waitress looks down in shock
            show sc cafeariel c154
            waitress"Let me fix this."
            #the waitress looks at the MC as she tries to fix her top
            show sc cafeariel c155
            waitress"This is so embarrassing."
            #the waitress looks away from the table, mouth slightly open
            show sc cafeariel c156
            mc"Don't worry about it."
            #the MC has his hand up, mouth open, unperturbed
            show sc cafeariel c157
            mc"Besides, it looks like that little mishap has been very good for business."
            #the MC looks around at the other people in the cafe
            show sc cafeariel c158
            mc"And more business means more tips for you, yeah?"
            #the MC looks back at the waitress who is now dressed again
            show sc cafeariel c159
            waitress"Yeah, I suppose you're right."
            #The waitress smiles
            show sc cafeariel c074
            waitress"So... Who had the espresso with the lemon twist?"
            show sc cafeariel c065
            mc"That would be me."
            #She puts that in front of the MC

            mc"Thanks."
            show sc cafeariel c074
            waitress"And yours must be the iced Latte."
            #Ariel doesn't make eye contact with her
            show sc cafeariel c075
            a"Yes, thank you."
            #She puts that in front of Ariel
            show sc cafeariel c072
            waitress"Was there anything else I can get either of you?"
            show sc cafeariel c076
            mc"We're good, thanks."
            show sc cafeariel c073
            mc"And I'd also like to add that you've got that perfect blend of efficiency and charm. It's like watching a caffeinated ballet."
            waitress"Oh, wow!"
            #The waitress is surprised and happy
            show sc cafeariel c072
            waitress"That's certainly the loveliest and funniest compliment I've had in a while."
            show sc cafeariel c100
            mc"Hey, you more than earned it."
            #The waitress addresses Ariel
            show sc cafeariel c074
            waitress"Is he always this charming?"
            show sc cafeariel c075
            a"Uh... I guess so."
            show sc cafeariel c076
            waitress"Enjoy your drinks, guys."
            #The waitress leaves
            stop music fadeout 2.0

        "Say nothing":
            show sc cafeariel c060
            mc"It's no problem at all. You look pretty busy."
            show sc cafeariel c062
            waitress"Yeah, we've been pretty swamped today."
            show sc cafeariel c063
            waitress"But getting the orders to our customers as quickly as possible is the most important thing."
            show sc cafeariel c061
            mc"It's very commendable."
            #The waitress smiles
            #She places the drinks in front of them
            show sc cafeariel c064
            waitress"So... Who had the espresso with the lemon twist?"
            show sc cafeariel c065
            mc"That would be me."
            #She puts that in front of the MC
            show sc cafeariel c066
            mc"Thanks."
            show sc cafeariel c067
            waitress"And yours must be the iced Latte."
            #Ariel doesn't make eye contact with her
            show sc cafeariel c068
            a"Yes, thank you."
            #She puts that in front of Ariel
            show sc cafeariel c069
            a"(Does she know that her chest is showing?)"
            show sc cafeariel c091
            a"(Surely, [y_name] has noticed.)"
            show sc cafeariel c095
            a"(So why hasn't he said anything?)"
            show sc cafeariel c086
            a"(Maybe it's best to pretend like I haven't seen anything.)"
            show sc cafeariel c070
            waitress"Was there anything else I can get either of you?"
            show sc cafeariel c071
            mc"No, we're okay, thanks."
            mc"(Maintain eye contact, maintain eye contact!)"
            show sc cafeariel c065
            mc"And I'd also like to add that you've got that perfect blend of efficiency and charm. It's like watching a caffeinated ballet."
            show sc cafeariel c072
            waitress"Oh, wow!"
            #The waitress is surprised and happy
            show sc cafeariel c073
            waitress"That's certainly the loveliest and funniest compliment I've had in a while."
            mc"Hey, you more than earned it."
            #The waitress addresses Ariel
            show sc cafeariel c074
            waitress"Is he always this charming?"
            show sc cafeariel c075
            a"Uh... I guess so."
            show sc cafeariel c076
            waitress"Enjoy your drinks, guys."
            stop music fadeout 2.0
    #The waitress leaves
    show sc cafeariel c077
    a"Okay, how did you do that?"
    play music "sound effects/01/Silent Dream2.mp3" loop fadein 1.0
    show sc cafeariel c078
    mc"Do what?"
    #The MC takes a sip of his expresso while Ariel talks
    show sc cafeariel c079
    a"Talk to the waitress so confidently."
    show sc cafeariel c080
    a"You practically made her melt with your words."
    show sc cafeariel c082
    mc"As I said before, it just takes practice."
    show sc cafeariel c089
    mc"Giving compliments to someone is usually a sure-fire winner, especially when they least expects it."
    mc"I'd imagine working here isn't the greatest job in the world, and she's probably on minimum wage."
    show sc cafeariel c087
    mc"But sometimes just a simple compliment can go a very long way."
    show sc cafeariel c085
    a"I see..."
    show sc cafeariel c087
    mc"How's your latte?"
    show sc cafeariel c090
    a"Oh, I haven't tried it yet..."
    #Ariel takes a sip of her iced latte
    show sc cafeariel c094
    a"Hmm..."
    show sc cafeariel c095
    mc"What is it?"
    show sc cafeariel c089
    a"This isn't what I ordered."
    show sc cafeariel c091
    a"It tastes more like an Iced Mocha than a latte."
    show sc cafeariel c090
    a"I guess it will have to do."

    #[Leave it / Fix it]
    menu:
        "Leave it":
            show sc cafeariel c091
            mc"Yeah, I mean, there's not really much of a difference, right?"
            show sc cafeariel c093
            a"Um... Yeah."
            #Ariel tentatively sips her drink
            show sc cafeariel c094
            mc"(There's not much point making a scene over this.)"
            $ v_ep01_ariel_arrogant_counter += 1
            #The waitress returns
            show sc cafeariel c097
            waitress"Miss, I am so sorry."
            show sc cafeariel c098
            waitress"I think I gave you the wrong order."
            show sc cafeariel c099
            waitress"Did your order happen to be an Iced Mocha?"
            show sc cafeariel c075
            a"Yeah, it is."
            show sc cafeariel c074
            waitress"My apologies."
            show sc cafeariel c100
            mc"Don't sweat it. It's just another stroke in the masterpiece of imperfection, right?"
            show sc cafeariel c076
            waitress"Indeed it is."
            show sc cafeariel c074
            waitress"Let me get that changed for you straight away, miss."
            #The Waitress takes her iced mocha
            show sc cafeariel c103
            a"That was nice of her."
            show sc cafeariel c102
            mc"Yeah, it certainly was..."
        "Fix it"(wt="Best option"):
            #***Choosing this option will give the player another set of options later in the scene
            show sc cafeariel c089
            mc"Okay, here's another tip for you, [a_name]."
            show sc cafeariel c088
            mc"You should never settle for anything less than you deserve, or what you've paid for."
            show sc cafeariel c103
            a"I know, but I don't want to make a scene."
            show sc cafeariel c104
            mc"Alright, let's fix this together."
            $ v_ep01_ariel_respect_counter += 1
            show sc cafeariel c105
            a"What do you mean?"
            show sc cafeariel c093
            mc"Just make sure to speak up when the time calls for it."
            #The MC sees the same waitress pretty close by and calls her back to their table
            show sc cafeariel c105
            mc"Excuse me, miss?"
            show sc cafeariel c114
            waitress"Yes, how can I help you?"
            #The MC looks at Ariel
            show sc cafeariel c068
            mc"[a_name]?"
            show sc cafeariel c108
            a"Hi... Um, I think I got the wrong order."
            show sc cafeariel c109
            a"This is an Iced Mocha. I ordered an Iced Latte."
            show sc cafeariel c110
            waitress"Oh, I am so sorry."
            show sc cafeariel c111
            waitress"My sicnerest apologies."
            show sc cafeariel c112
            a"No sweat."
            show sc cafeariel c114
            mc"It's just another stroke in the masterpiece of imperfection, right?"
            show sc cafeariel c110
            waitress"Indeed it is."
            show sc cafeariel c111
            waitress"Let me get that changed for you straight away, miss."
            #The Waitress takes her iced mocha
            show sc cafeariel c103
            a"That was nice of her."
            show sc cafeariel c102
            mc"Yeah, it certainly was."
            show sc cafeariel c053
            mc"You see how simple that was?"
            mc"You didn't settle for less and you were able to speak to her in a calm, composed tone."
            show sc cafeariel c054
            a"Yeah... I did, didn't I?"
            show sc cafeariel c118
            mc"(It's a breakthrough, even if it's only a minor one...)"
            $ v_ep01_14_01_Cafe_Scene_Fix = True
    #screen goes blank
    stop ambient2 fadeout 1.0
    stop music fadeout 2.0
    scene black
    with dissolve
    pause 1.0
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #scene continues
    play music "sound effects/01/Sunshine Walk1.mp3" loop fadein 1.0
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    #The MC and Ariel walk home together
    show sc cafeariel c119
    with dissolve
    pause 1.0
    show sc cafeariel c120
    mc"So, how do you feel now?"
    show sc cafeariel c121
    a"Okay, I suppose."
    show sc cafeariel c122
    a"I was still a little anxious being in a place full of complete strangers, but overall, it wasn't too bad."
    show sc cafeariel c123
    mc"That's perfectly normal."
    #show Ariel's mouth closed as she walks - show her face looking at the MC
    show sc cafeariel c124
    mc"It takes practice. The more you get out of the house, the quicker that feeling of anxiety will fade."
    mc"I promise you."
    show sc cafeariel c120
    mc"Besides that, did you enjoy hanging out?"
    #show the MC and Ariel walking down the street, MC talking
    show sc cafeariel c122
    a"Yes, I did."
    #Ariel happy and mouth open, talking
    show sc cafeariel c125
    mc"That's great to hear."
    #Ariel looks around and has a concerned look on her face
    show sc cafeariel c127
    with dissolve
    pause 1.0


    #[Keep walking / Hold her hand]
    menu:
        "Keep walking":
            show sc cafeariel c125
            a"I know this is going to seem strange, but can you hold my hand while we walk?"
            show sc cafeariel c126
            mc"(I'm stunned! I can tell that she was nervous to ask me.)"
            show sc cafeariel c133
            mc"Sure, I can do that."
            #The MC holds Ariel's hand
            show sc cafeariel c128
            a"Thanks."
            #Ariel and the MC smile - show them walking down the sidewalk hand in hand looking at each other - https://c8.alamy.com/comp/WP7041/black-couple-holding-hands-while-walking-by-autumn-park-WP7041.jpg
            stop ambient fadeout 1.0
            stop music fadeout 1.0

        "Hold her hand"(wt="Best option"):
            #The MC holds her hand, much to the surprise of Ariel
            show sc cafeariel c126
            mc"(I'm going to need to do something to help speed up this process a bit.)"
            show sc cafeariel c128
            with dissolve
            pause 1.0
            show sc cafeariel c129
            with dissolve
            pause 1.0
            show sc cafeariel c125
            with dissolve
            a"Uh, [y_name]?"
            show sc cafeariel c132
            mc"Yeah?"
            show sc cafeariel c123
            a"You're holding my hand."
            show sc cafeariel c134
            mc"You don't like it?"
            mc"Do you trust me?"
            show sc cafeariel c122
            a"Of course I do."
            show sc cafeariel c133
            mc"Alright, then just go with it."
            #The MC looks into Ariel's eyes
            show sc cafeariel c123
            a"O-okay..."
            #Ariel and the MC smile - show them walking down the sidewalk hand in hand looking at each other - https://c8.alamy.com/comp/WP7041/black-couple-holding-hands-while-walking-by-autumn-park-WP7041.jpg
            show sc cafeariel c148
            a"(Hmm... This kind of feels nice.)"
            $ rewards_unlock ("ariel",6)
            stop ambient fadeout 1.0
            stop music fadeout 1.0

    #scene continues
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)


    #cross-screen fade
    #The MC and Ariel stand outside of the front door
    play music "sound effects/01/Frayed_Relations1.mp3" loop fadein 1.0
    play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
    show sc cafeariel c146
    a"So thanks again for taking me out."
    show sc cafeariel c135
    a"And you were right. I definitely needed that."
    show sc cafeariel c136
    mc"It was my pleasure."


    #***Before they enter the house, Ariel will kiss the MC on the cheek, only IF the player chooses "Fix it"
    if v_ep01_14_01_Cafe_Scene_Fix == True:
        play sound "sound effects/01/mwah_short_kissing_sound_effect3.mp3"
        show sc cafeariel c137
        with dissolve
        a"Mwah!{p=1.0}{nw}"
        show sc cafeariel c147
        with dissolve
        mc"(Oh... This is... unexpected.){p=1.5}{nw}"
        stop sound fadeout 1.0
        show sc cafeariel c141
        with dissolve
        mc"How about we do this again sometime soon?"
        show sc cafeariel c140
        a"I'd like that a lot."
        #Ariel smiles
        show sc cafeariel c142
        a"But do you think can we keep this between us?"
        show sc cafeariel c141
        a"I'd rather [mc_v_address!c] and [b_name], and especially [mc_vic_address], don't know anything about it."
        show sc cafeariel c143
        mc"Sure, I'd prefer it that way."
        show sc cafeariel c150
        a"Yeah, me too."
        show sc cafeariel c149
        mc"And if you ever want to talk about what we said at the cafe, any time, day or night, you know where to find me."
        show sc cafeariel c140
        a"Thanks, [y_name]. I probably will."

    #Ariel smiles
    show sc cafeariel c144
    mc"Come on, let's go and see what everyone else is up to..."
    stop ambient fadeout 1.0
    stop music fadeout 1.0

    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    $ v_ep01_ariel_dates_counter += 1
    jump lb_ep01_The_MC_Investigates_the_gang
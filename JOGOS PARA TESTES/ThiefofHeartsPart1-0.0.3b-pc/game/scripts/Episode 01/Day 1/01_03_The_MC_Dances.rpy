init:
    $ v_ep01_mansionhall_vivian = False

    image sc mansionhall mc fall:
        "sc mansionoutside o35" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mansionoutside o37" with Dissolve(0.2, alpha=True)


label lb_ep01_intro_04_heist_scene:
    #he sees the party continuing, people either talking, drinking or dancing"
    #the MC speaks to the other members of the team"
    play ambient "sound effects/01/people_talking_at_party1.ogg" loop fadein 1.0
    $ renpy.music.set_volume(0.6, 0.0, channel="music")
    play music "sound effects/01/party_music#1.ogg" loop fadein 0.5
    scene sc mansionhall h52
    mc"I'm rejoining the party now."
    mc"I'm going to make a beeline for the nearest exit."
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionkitchen k31
    waitress"No! Don't do that just yet."
    waitress"They have all the exits covered."
    waitress"It's best that you try and leave without anyone noticing you, just to be safe."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party3.ogg" loop
    show sc mansionhall h55
    mc"Where are you? I can't see you anywhere."
    #Show Bella in the kitchen
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionkitchen k35
    waitress"I'm getting a tray of food in the kitchen. I'll be back in the main room shortly."
    #mom talks to the MC, just show her lips here
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party5.ogg" loop
    show sc mansionhall h57
    female_v2"You're going to have to blend in for the next few minutes while we work on a way to get everyone out without drawing any attention."
    show sc mansionhall h60
    mc"Oh hey, good to hear your voice."
    show sc mansionhall h58
    mc"I saw you earlier but it looked like you were busy."
    show sc mansionhall h57
    female_v2"Well, somebody had to calm things down after that stunt you pulled with the head chef."
    female_v2"It sounds like everything went well with the download, yes?"
    show sc mansionhall h55
    mc"Yep, I have the drive on me."
    show sc mansionhall h60
    mc"By the way, thanks for what you did earlier."
    show sc mansionhall h59
    female_v2"You're welcome, sweetheart."
    #party music plays"
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionkitchen k31
    waitress"Guys, I just got word that security is going around and checking everyone's invitations."
    show sc mansionkitchen k33
    mc"How come?"
    show sc mansionkitchen k31
    waitress"One of them was upstairs on a routine check and they found one of the doors unlocked."
    mc"Oh..."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party2.ogg" loop
    show sc mansionhall h57
    mc"(Shit! I forgot to lock the door from the inside on my way out.)"
    $ renpy.music.set_volume(0.1, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o15
    leader"Dammit, [y_name]!"
    leader"How many times have I told you to cover your tracks?"
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    stop music fadeout 4.0
    $ renpy.music.set_volume(1.0, 0.0, channel="music2")
    play music2 "sound effects/01/party_music#2.ogg" loop fadein 4.0
    show sc mansionhall h54
    waitress"Quickly now... Go and talk with someone at the party so you look less suspicious."

    #show the party full of people and have Vivian standing near the dance floor, and the anonymous girl standing by the bar

    #IMPORTANT - make sure the mom is wearing an especially short/revealing dress"
    #She doesn't look like a punk-looking chick (anonymous girl) during the party. She's wearing a formal dress and heels, and a brunette or redhead long hair wig.
    #Just like the MC's mom, she wants to avoid the police or being caught on camera so they don't see her real looks"

    #IMPORTANT: Make it possible to click on each of these girls - the player can only choose one"

    #also use these scenes to show various angles and parts of both women in this scene to show how attractive they are"
    #MD - Make sure you create a variable for both options here as it will be necessary for Scene 02-01
    $ renpy.music.set_volume(1.0, 0.5, channel="music")
    show sc mansionhall h61
    mc"(Hmm... who should I talk to?)"
    menu:
        "The woman on the left"(wt="She's a part of your [private_group]"):
            $ v_ep01_mansionhall_vivian = True
            #$ persistent.v_rewards_bella_1 = False
            $ rewards_unlock ("bella",1)
            show sc mansionhall h60
            mc"Okay, blending in."
            #the MC walks through the crowd of people towards Vivian while the security looks around for him
            show sc mansionhall h62
            mc"Excuse me, miss?"
            show sc mansionhall h64
            mc"Would you care to dance?"
            show sc mansionhall h64b
            milf"Oh, I'd love to, young man."
            #the MC takes her hand and escorts Vivian to the dance floor"
            show sc mansionhall h65
            mc"Perfect."
            #the MC and Vivian dance in amongst the crowd of party-goers"
            #he holds her close and she whispers in his ear"
            show sc mansionhall h68
            mc"(Hopefully, I've drawn attention away from myself.)"
            show sc mansionhall h70
            milf"You know, the next time you're going to ask me to dance, maybe give me a heads-up so I can prepare myself."
            #show the mother with the earpiece in one of her ears, to show she's also part of the team"
            show sc mansionhall h70b
            leader"She's right. Try not to ad-lib like that in future."
            show sc mansionhall h71
            mc"She was the best option. I didn't have time to think."
            show sc mansionhall h65
            milf"Well, I am a little flattered that you asked me to dance instead of one of these much younger hotties."
            #vivian smiles"
            #the MC looks over Vivian's shoulder and sees a member of security looking in his direction"
            show sc mansionhall h72
            mc"(Shit! He's looking over this way.)"
            show sc mansionhall h73
            mc"Changing direction."
            #the MC spins Vivian so she faces in the opposite direction and the MC's back is turned to the security"
            show sc mansionhall h74
            milf"(Woah!)"
            show sc mansionhall h76
            milf"Where did you learn that?"
            show sc mansionhall h77
            mc"Dance Dance Revolution!"
            show sc mansionhall h75
            milf"(Who knew that he could dance like this?)"
            #vivian gives the MC a funny smirk"
            show sc mansionhall h78
            milf"(Certainly not I.)"
            show sc mansionkitchen k39
            waitress"Guys, I have a way to get you both out of there."
            show sc mansionhall h77
            mc"What will be the signal?"
            #We show the older sis leaving one of the fires from the oven on. Then later on during the scene, the alarm sets off.
            #The player will connect the dots.
            #Just like Tyler Mowery says, show don't tell."
            show sc mansionkitchen k40
            waitress"It will be-"
            #older sister is cut off as security taps the MC on the shoulder and asks to check his invitation"
            show sc mansionhall h79
            security"Excuse me, Sir. May I see your invitation?"
            #The Smoke Alarm goes off in the room"
            #sound effect required for this"
            $ ui.timer(0.5, Play("sound", "sound effects/01/business_fire_alarm.ogg", loop=True))
            #the MC turns to face a menacing-looking guy"
            show sc mansionhall h113
            mc"Oh, sure... Let me just get that for you."
            stop music2 fadeout 2.0
            show sc mansionhall h82
            head_chef"Everybody please evacuate! We have a situation in the kitchen!"
            show sc mansionhall h81
            security"What the hell?"
            #a burst of flames can be seen behind the head chef inside the kitchen - https://frinkiac.com/img/S07E21/609992.jpg"
            show sc mansionkitchen k41
            waitress"Guys, I just set the fire alarm off."
            waitress"Get the hell out of there!!"
            show sc mansionhall h83
            mc"Adios amigos!"
            #The MC says to the security and he disappears into the crowd with everyone else"
            show sc mansionhall h84
            security"Hey! Get back here!"
            stop ambient fadeout 1.0
            stop sound fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)


            #the MC is looking back at security as he's exiting the house with everyone else and runs into the anonymous girl"
            play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o33
            with dissolve
            mc"I'm outside the house."
            mc"Looks like I'm going to get away unscathed."
            play sound "sound effects/01/male_hurt.mp3"
            show sc mansionoutside o34
            mc"UHH!{p=0.6}{nw}" with hpunch
            show sc mansionhall mc fall
            pause 0.8
            stop sound fadeout 1.0
            play sound2 "sound effects/01/Falling Over Sound Effect.mp3"
            pretty_g"Oh!!" with vpunch
            mc"Dammit!"
            show sc mansionoutside o40
            mc"(Ugh... What happened?)"
            stop sound2 fadeout 1.0
            show sc mansionoutside o38
            pretty_g"Oh my God, are you okay?"
            show sc mansionoutside o44
            mc"Yeah, I'm fine. Sorry, I didn't see you there."
            #the MC looks up and sees the anonymous girl - POV shot from the floor"
            show sc mansionoutside o40b
            mc"(Woah... Dream weaver...)"
            show sc mansionoutside o39
            pretty_g"It's okay, mistakes happen."
            show sc mansionoutside o45
            pretty_g"Here, let me help you up."
            #anonymous girl helps the MC to his feet"
            play ambient "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o46
            mc"Thanks."
            show sc mansionoutside o47
            pretty_g"Pretty crazy party, huh?"
            show sc mansionoutside o50
            mc"I'll say."
            #victor speaks to the MC via his earpiece"
            show sc mansionoutside o48
            leader"[y_name], seconds count, ditch her."
            mc"(How the hell did I not notice this girl at the party?)"
            mc"By the way, I'm [y_name]."
            show sc mansionoutside o47
            pretty_g"Nice to meet you."
            show sc mansionoutside o49
            pretty_g"Uh, sorry, but I should get going."
            pretty_g"I have to catch up with somebody."
            show sc mansionoutside o51
            pretty_g"Bye."
            #anonymous girl walks away"
            show sc mansionoutside o52
            mc"Dayum..."
            #anonymous girl looks over her shoulder and flashes the MC a brief smile"
            mc"(Who... is that girl?)"
            #show a close-up of her tattoo"
            show sc mansionoutside o53
            mc"Hmm... Interesting."
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            show sc mansionoutside o16
            leader"What the hell happened, [y_name]?"
            play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o58a
            mc"It was nothing, I'm fine."
            show sc mansionoutside o54
            waitress"I think he was a little lovestruck for a moment with that girl."
            #os gives a cheeky smirk"
            show sc mansionoutside o58b
            mc"Jealous much?"
            show sc mansionoutside o55
            waitress"Don't flatter yourself."
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            show sc mansionoutside o15
            leader"You two stop bickering and get out of there before security catches up with either of you."
            play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o58
            mc"Roger that..."
            show sc mansionoutside o55
            waitress"We'll meet you all back at the van."
            show sc mansionoutside o56
            mc"See you there, over!"
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            #(screen goes blank)"
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_intro_05_heist_scene


        "The girl on the right"(wt="She's a Mystery Girl"):
            $ v_ep01_mansionhall_mystery_girl = True
            show sc mansionhall h60
            mc"Okay, blending in."
            #the MC walks through the crowd of people towards the anonymous girl who is holding a glass of champagne while the security looks around for him"
            show sc mansionhall h86
            mc"Excuse me, miss? Would you care to dance?"
            show sc mansionhall h87a
            pretty_g"Oh."
            show sc mansionhall h87b
            pretty_g"Sure. Why not?"
            #she puts down the champagne and the MC takes her hand and escorts the anonymous girl to the dance floor"
            show sc mansionhall h88
            mc"Perfect."
            #the MC and the anonymous girl dance in amongst the crowd of party-goers"
            #he holds her close and she whispers in his ear"
            show sc mansionhall h90
            pretty_g"So, I don't believe we've met before."
            pretty_g"How do you know the birthday boy?"
            show sc mansionhall h89
            mc"We were college roommates during our first year."
            show sc mansionhall h92
            leader"Keep the conversation short. Don't give too much away."
            leader"We're still working on a way to get you out of there."
            show sc mansionhall h90
            pretty_g"Why do I get the feeling you're not telling me the truth?"
            show sc mansionhall h93
            mc"It's because of my nose, isn't it?"
            show sc mansionhall h97
            mc"It may be a little long but looks can be deceiving."
            show sc mansionhall h99
            pretty_g"Haha! I suppose so."
            pretty_g"I actually think it makes you look even more cute."
            show sc mansionhall h98
            mc"Thanks. I guess..."
            show sc mansionhall h88
            mc"And how about you? How do you know him?"
            show sc mansionhall h90
            pretty_g"I'm an old girlfriend of his believe it or not."
            #the MC shoots her a surprised look"
            show sc mansionhall h92
            pretty_g"I know, I know. You're probably thinking, \"Why would I want to attend my ex's party?\""
            show sc mansionhall h93
            mc"I'll bite. How come?"
            show sc mansionhall h90
            pretty_g"I like the chance to be able to dress up."
            pretty_g"And to um... meet new people."
            #Vivian speaks to him via his earpiece"
            show sc mansionhall h88
            female_v2"[y_name]..."
            show sc mansionhall h95
            female_v2"You have one of the guys from security eyeballing you right now."
            #show the mother with the earpiece in one of her ears, to show she's also part of the team"
            show sc mansionhall h72
            leader"You'll have to ditch this girl, [y_name]."
            show sc mansionhall h93
            mc"Anyway, I'm afraid I must get going."
            show sc mansionhall h91
            pretty_g"Yeah, me too."
            #anonymous girl leans in close to his ear, her hands on his chest"
            show sc mansionhall h90
            pretty_g"But thank you for the dance."
            show sc mansionhall h104
            pretty_g"Maybe we'll bump into each other again soon."
            pretty_g"See ya."
            show sc mansionhall h103
            mc"Bye."
            #anonymous girl walks away"
            show sc mansionhall h105
            mc"Woah..."
            #anonymous girl looks over her shoulder and flashes the MC a brief smile as she exits the dance floor"
            mc"(Who... was that girl?)"
            mc"(Damn! I should've at least asked for her name, or given her mine.)"
            show sc mansionhall h106
            #show a close-up of her tattoo"
            mc"Hmm... Interesting."
            show sc mansionkitchen k39
            waitress"Okay, I have a way to get you out of there."
            show sc mansionhall h107
            mc"What will be the signal?"
            show sc mansionkitchen k40
            #We show the older sis leaving one of the fires from the oven on. Then later on during the scene, the alarm sets off. The player will connect the dots. Just like Tyler Mowery says, show don't tell."
            waitress"It will be-"
            #older sister is cut off as security taps the MC on the shoulder and asks to check his invitation"
            show sc mansionhall h108
            security" Excuse me, Sir. May I see your invitation?"
            #the MC turns to face a menacing-looking guy"
            show sc mansionhall h108b
            mc"(Okay, keep your cool, [y_name].)"
            #The Smoke Alarm goes off in the room"
            #sound effect required for this"
            $ ui.timer(0.5, Play("sound", "sound effects/01/business_fire_alarm.ogg", loop=True))
            show sc mansionhall h109
            mc"Oh, sure... Let me get that for you."
            stop music2 fadeout 2.0
            show sc mansionhall h82
            head_chef"Everybody please evacuate! We have a situation in the kitchen!"
            #a burst of flames can be seen behind the head chef inside the kitchen"
            stop music fadeout 1.0
            show sc mansionkitchen k41
            waitress"Guys, I just set the fire alarm off."
            waitress"Get the hell out of there!!"
            show sc mansionhall h83
            mc"Adios amigos!"
            #The MC says to the security and he disappears into the crowd with everyone else"
            show sc mansionhall h84
            security"Hey! Get back here!"
            stop sound fadeout 1.0
            stop ambient fadeout 1.0
            #the MC is looking back at security as he's exiting the house"
            #(screen goes blank)"
            scene black
            with dissolve
            scene black
            with Pause (2)
            play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o33
            mc"Looks like I'm going to get away unscathed."
            show sc mansionoutside o55
            waitress"Great... We'll meet you all back at the van."
            show sc mansionoutside o56
            mc"Cool... See you all shortly."
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            show sc mansionoutside o15
            leader"What the hell happened back there, [y_name]?"
            play ambient"sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o58a
            mc"It was nothing. Forget about it."
            show sc mansionoutside o54
            waitress"I think [y_name] was a little lovestruck for a moment with that girl."
            #os gives a cheeky smirk"
            show sc mansionoutside o58b
            mc"Jealous much?"
            show sc mansionoutside o55
            waitress"Don't flatter yourself."
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            show sc mansionoutside o15
            leader"You two stop bickering and get out of there before security catches up with either of you."
            play ambient "sound effects/01/Birds_in_trees_sounds_effects1.mp3" loop fadein 1.0
            play ambient2 "sound effects/01/People Outside Talking Ambience.ogg" loop fadein 1.0
            show sc mansionoutside o58
            mc"Roger that...."
            stop ambient fadeout 1.0
            stop ambient2 fadeout 1.0
            #(screen goes blank)"
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_intro_05_heist_scene

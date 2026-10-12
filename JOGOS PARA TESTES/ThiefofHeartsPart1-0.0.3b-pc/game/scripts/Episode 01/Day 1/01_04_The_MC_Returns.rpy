init:
    image sc mansionoutside removes disguise:
        "sc mansionoutside o66" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mansionoutside o67" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mansionoutside o68" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mansionoutside o69" with Dissolve(0.2, alpha=True)

    image sc mansionoutside officers running:
        "sc mansionoutside o73" with Dissolve(0.2, alpha=True)
        pause 3.0
        "sc mansionoutside o74" with Dissolve(0.2, alpha=True)

    image sc mansionoutside truck driving away:
        "sc mansionoutside o94" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc mansionoutside o95" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc mansionoutside o96" with Dissolve(0.2, alpha=True)

    image intro_movie:
        "sc mansionoutside o86" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mansionoutside o87" with Dissolve(0.2, alpha=True)
        pause 0.3
        "sc mansionoutside o88" with Dissolve(0.2, alpha=True)
        pause 0.3
        Movie(channel="movies_with_sound", loop=False, fadeout=1.0, play="images/extras/Episode 01/anim_ep01_toh_intro.webm", image=Crop((0,0,1920,1080), "#000"))

    screen scr_ep01_01_04_Intro_Movie:
        #Prevent all these buttons from skipping the intro movie
        key "K_RETURN" action Hide("nonexistent_screen")
        key "K_KP_ENTER" action Hide("nonexistent_screen")
        key "K_SPACE" action Hide("nonexistent_screen")
        key "mousedown_4" action Hide("nonexistent_screen")
        key "K_PAGEUP" action Hide("nonexistent_screen")
        key "mousedown_5" action Hide("nonexistent_screen")
        key "K_PAGEDOWN" action Hide("nonexistent_screen")
        key "mouseup_3" action Hide("nonexistent_screen")
        key "mouseup_1" action Hide("nonexistent_screen")
        key "K_ESCAPE" action Return("smth") # Only allow Escape key to skip the intro movie

    screen scr_ep01_04_04_Set_Names_Choice:
        default tt = Tooltip("Would you like to use the names previously set on your last playthrough for this playthrough?\n\nIf \"YES\", you will skip the naming/introduction scene.\n(These can be changed in the From the Game Tablet later.)")
        zorder 10 # These should look like part of the scene, so they should go under things like the music player if they overlap

        frame:
            xfill True
            xalign 0.5
            yalign 0.0
            vbox:
                xalign 0.5
                yalign 0.5
                text tt.value

label lb_ep01_intro_05_heist_scene:
    #scene continues with the MC walking out the front entrance - the birthday party crowd breaks up"

    #The scene starts with the police arriving at the house and we can see them in the distance discussing with the rich group and security guys."
    #There are also fire-fighters at the scene of the crime
    #We also see a female police officer with the group. She will become a side character in the future. We cannot hear what they're saying"

    #the MC gets separated from everyone else - he talks with the father on his earpiece."
    play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
    scene sc mansionoutside o59
    with dissolve
    mc"Looks like they called the cops. Mrs. Walker is talking with a female officer."
    #this will be the first glimpse of the "Female Officer"."
    show sc mansionoutside o60
    mc"Can anyone hear what they're saying?"
    show sc mansionoutside o61
    leader"No, the girls are already off the premises." # use "we", as b_name is not defined right now
    #show the mom and the older sister together"
    show sc mansionoutside o62
    leader"Just act naturally."
    leader"And try and lose your disguise if you can, [y_name]."
    show sc mansionoutside o63
    mc"Can do."
    #we see the MC removing his glasses, then his wig, and then finally, his fake nose - one frame after another"
    #we see him drop the items in the trash"
    #rolling/swivelling screen so we can see the MC completely in the fresh, so he kind of has a superhero pose"
    show sc mansionoutside removes disguise
    pause 3.4
    mc"That's a relief."
    #the MC sees two police officers coming his way, holding walkie-talkies"
    show sc mansionoutside o70
    mc"(Now to casually walk back to the van.)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    show sc mansionoutside o71a
    with dissolve
    $ ui.timer(0.1, Play("sound", "sound effects/01/two_officers_running_effect.mp3", loop=True, fadein=1.0))
    $ ui.timer(0.5, Play("sound2", "sound effects/01/two_officers_running_effect.mp3", loop=True, fadein=1.0))
    mc"(Well, that went better than expected.)"
    show sc mansionoutside o71b
    mc"(Oh shit.)"
    mc"(They've found me!)"
    show sc mansionoutside o72
    officer"Out of the way, Sir."
    mc"Huh?"
    #they rush past him and towards the house. One of them puts a walkie-talkie to his mouth"
    show sc mansionoutside officers running
    officer"Yeah chief... According to home security, we're looking for a guy with glasses, frizzy hair and a huge fucking nose!"
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    officer"He should be easy to locate, over!"
    #the officers enter the house, and the MC breathes a sigh of relief"
    show sc mansionoutside o75
    mc"Damn... What a rush."
    #he speaks to the father and younger sister"
    mc"I thought for sure that I'd been made."
    stop ambient fadeout 1.0
    show sc mansionoutside o76
    hacker"Get back to the van, [y_name]."
    play ambient2 "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    show sc mansionoutside o79
    with dissolve
    mc"I'm already here."
    #expand the shot so we can see the MC standing outside the back of the van"
    #sound effect for opening the van door
    play sound "sound effects/01/van_back_door_open_effect.mp3"
    show sc mansionoutside o77
    hacker"Huh?"
    #the MC opens the back of the van - https://www.daz3d.com/z-everyday-van"
    #he sees older and younger sis in the back - mom and Viktor sit in the front seats"
    stop sound fadeout 1.0
    show sc mansionoutside o109
    waitress"Quick, get in!"
    stop ambient2 fadeout 1.0
    #the MC hops into the back of the van, closes the doors and the father drives off"
    #SUGGESTION: this could be a short animation
    #show the van leaving the scene of the crime, driving down the street, and police continue talking to guests in and around the premises"
    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    with Pause (2)

    #scene returns with the MC inside the van"
    #sound effect of the van driving away
    #he talks to the player (narrates)"
    play sound "sound effects/01/truck_driving_away_effect.mp3"
    show sc mansionoutside truck driving away
    with dissolve
    pause 1.6
    stop sound fadeout 1.0
    play ambient "sound effects/01/truck_interior_sound_effect.ogg" loop fadein 1.0
    show sc mansionoutside o159
    with dissolve
    mc"Hi there."
    mc"What you just witnessed earlier was how to pull off a heist, or a robbery if you will."
    show sc mansionoutside o158
    mc"Sure, it was nothing major, but we're working towards something even bigger."
    show sc mansionoutside o106
    mc"And who are we?"

    if persistent.v_allow_previous_names == True:
        show sc mansionoutside o103
        show screen scr_ep01_04_04_Set_Names_Choice with Dissolve(0.2)
        menu:
            "YES":
                $ set_persistent_names("restore")
                $ v_allow_redefine = True
                hide screen scr_ep01_04_04_Set_Names_Choice with Dissolve(0.2)
                jump lb_ep01_intro_05_heist_scene_02
            "NO":
                hide screen scr_ep01_04_04_Set_Names_Choice with Dissolve(0.2)
                jump lb_ep01_intro_05_heist_scene_01

label lb_ep01_intro_05_heist_scene_01:
    show sc mansionoutside o159
    mc"Well, let me introduce everybody."
    stop ambient fadeout 1.0
    #show the younger sister who sits in the back of the van with the MC and older sister"
    #show various images of younger sis here while the MC is telling her story - past and present - learning how to be an expert hacker"
    #Note: THIS would be a great time/point to name the characters – until now, they should be called “younger female 1 + 2, older female, older male. Leave the player completely in the open what happens."
    play music "sound effects/01/Rollin at 5 - 210 - full.mp3" loop fadein 1.0
    show sc mansionoutside o81
    with dissolve

    # define Ariel
    ################################################################
    $ choice_done = False
    while not choice_done:
        $ name = renpy.input("Our \"Hacker\" is called... (Enter her name - Default name: [a_name])").strip()
        if not name:
            $ name = a_name
        $ rel = renpy.input("She's your younger... (Enter relationship - Default: [a_mc_rel])").strip() # Strip any leading/trailing whitespace
        if not rel:
            $ rel = a_mc_rel
        # Note: a_mc_rel => that means "Ariel" is "MC's" <whatever>
        $ rel2 = renpy.input("That makes you her older... (Enter relationship - Default: [mc_a_rel])").strip() # Strip any leading/trailing whitespace
        if not rel2:
            $ rel2 = mc_a_rel
            # Note: mc_a_rel => that means "mc" is "Ariel's" <whatever>
        $ address = renpy.input("You will address her as your... (Default example: 'Hi, [a_mc_address]')").strip()
        if not address:
            $ address = a_mc_address
        $ address2 = renpy.input("And she addresses you as her... (Default example: 'Hi, [mc_a_address]')").strip()
        if not address2:
            $ address2 = mc_a_address
        "Her name is [name]. She is your younger [rel], and you are her older [rel2].\n"
        "In short, you call her your [address], and she calls you her [address2]."
        "Is that correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ a_name = name
    $ a_mc_rel = rel
    $ mc_a_rel = rel2
    $ mc_a_address = address
    $ a_mc_address = address2

    ################################################################

    show sc mansionoutside o159
    with dissolve
    mc"As you can probably tell from the job we just did, [a_name] is a whiz when it comes to technology and communications."
    show sc mansionoutside o105
    with dissolve
    mc"She can hack into just about any system or create a fake profile for anyone within a matter of minutes."
    show sc mansionoutside o112
    with dissolve
    mc"We call her 'The Hacker' for obvious reasons."
    #show the younger sister typing on her laptop in her room"
    show sc mansionoutside o110
    with dissolve
    mc"[a_name] once said that she wishes she could be more like me and admires my confidence."
    show sc mansionoutside o111
    with dissolve
    mc"It's fair to say that she looks up to me."
    show sc mansionoutside o113
    with dissolve
    mc"I'm not sure why as I wouldn't exactly consider myself to be the ideal role model."
    mc"I guess it's nice to be thought of like that."
    #have the screen pan from younger sis to older sis"
    #show various images of older sis here while the MC is telling her story - past and present - showing her at college, dressed to the nines when at a function, chatting up more than one guy at a time"
    stop music fadeout 2.0
    scene black
    with Dissolve(1.0)
    pause 0.5
    play music "sound effects/01/Too Cool.mp3" loop fadein 1.0
    show sc mansionoutside o82
    with Dissolve(1.0)

    # define Bella
    ################################################################
    $ choice_done = False
    while not choice_done:
        $ name = renpy.input("Next we have... (Enter her name - Default name: [b_name])").strip()
        if not name:
            $ name = b_name
        $ rel = renpy.input("She's your older... (Enter relationship - Default: [b_mc_rel])").strip()
        if not rel:
            $ rel = b_mc_rel
        $ rel2 = renpy.input("That means you are her younger... (Enter relationship - Default: [mc_b_rel])").strip()
        if not rel2:
            $ rel2 = mc_b_rel
        $ address = renpy.input("You will address her as your... (Default example: 'Hi, [mc_b_address]')").strip()
        if not address:
            $ address = b_mc_address
        $ address2 = renpy.input("And she addresses you as her... (Default example: 'Hi, [b_mc_address]')").strip()
        if not address2:
            $ address2 = mc_b_address
        "Her name is [name]. She is your older [rel], and you are her younger [rel2].\n"
        "In short, you call her your [address], and she calls you her [address2]."
        "Is that correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ b_name = name
    $ b_mc_rel = rel
    $ mc_b_rel = rel2
    $ mc_b_address = address
    $ b_mc_address = address2
    ################################################################

    show sc mansionoutside o104
    with dissolve
    mc"It may not seem like it when looking at her now, but [b_name] was a little pissed at me taking the lead role for today's job."
    mc"She didn't think I was ready and thought that it was too soon to be tasked with such an important job."
    mc"But after today's successful heist, I feel like I'm more than ready to take on bigger tasks."
    with dissolve
    show sc mansionoutside o139
    with dissolve
    mc"She simply didn't want to play the distraction role to all the horny males (young and old) who were ogling her at the party."
    #show older sis' cleavage"
    #older sis shoots the MC a snide look"
    show sc mansionoutside o140
    with dissolve
    mc"It's always been like this between us growing up."
    #show the older sis being chatted up by two guys at the same time - a previous scene"
    show sc mansionoutside o138
    with dissolve
    mc"But admittedly, [b_name] really excels in the department of being a master of disguise and she has a great sense of fashion."
    #show sis putting makeup and a fake nose on the MC - an earlier scene"
    show sc mansionoutside o141
    with dissolve
    mc"She also has an incredible ability to forge documents or create fake items, like paintings or jewelry."
    show sc mansionoutside o115
    with dissolve
    mc"All the clothes, wigs and the fake nose you saw me wearing, was because of her."
    mc"Though I didn't get any say on this ridiculous look, of course."
    mc"But it worked, so I have no complaints."
    show sc mansionoutside o137
    with dissolve
    mc"[b_name] is very much a free spirit and also wants to be seen as an independent woman."
    #have the screen switch from the MC to Vivian", who sits in the passenger seat up front"
    #show various images of Mom here while the MC is telling her story - past and present"
    stop music fadeout 2.0
    #scene black
    #with Dissolve(1.0)
    #pause 0.5
    play music2 "sound effects/01/Vivian_Intro.mp3" loop fadein 2.0
    show sc mansionoutside o84
    with fade

    # define Vivian
    ################################################################
    $ choice_done = False
    while not choice_done:
        $ name = renpy.input("And then there's ... (Enter her name - Default name: [v_name])").strip()
        if not name:
            $ name = v_name
        $ lname = renpy.input("Her surname is...\n (Default: [lastname])").strip() # Strip any leading/trailing whitespace
        if not lname:
            $ lname = lastname
        $ mc_v_address = v_pre_address + " " + lastname # add now defined lastname to addressing
        $ rel = renpy.input("She's my ... (Enter relationship - Default: [v_mc_rel])").strip()
        if not rel:
            $ rel = v_mc_rel
        $ rel2 = renpy.input("So I am her ... (Enter relationship - Default: [mc_v_rel])").strip()
        if not rel2:
            $ rel2 = mc_v_rel
        $ address = renpy.input("Because of our relationship, I address her as... (Default: [mc_v_address])").strip()
        if not address:
            $ address = mc_v_address
        "Your [rel]'s name is [name] [lname]."
        "You are her [rel2] and you will address her as [address], while she will address you by your first name."
        "Is that correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ v_name = name
    $ lastname = lname
    $ v_mc_rel = rel
    $ mc_v_rel = rel2
    $ mc_v_address = address
    ################################################################

    show sc mansionoutside o118
    with dissolve
    mc"We know her as 'The Actress', as that's what she was hoping to become when she was younger."
    show sc mansionoutside o119
    with dissolve
    mc"She's great at putting on different accents, courtesy of being multilingual."
    mc"[mc_v_address] also knows how to pretend to be almost any famous female celebrity you can think of!"
    show sc mansionoutside o120
    with dissolve
    mc"However, once the three of us were part of her life, that squandered any hopes of her having a serious acting career."
    mc"So life didn't quite pan out the way she hoped it would, but being part of a group of thieves allows her to play a different character each time we plan out a robbery."
    #show Vivian impersonating Marilyn Monroe - https://www.hollywoodreporter.com/wp-content/uploads/2011/05/marilyn_monroe_subway_2011_a_p.jpg?w=2000&h=1126&crop=1“

    show sc vivianwork v006
    with dissolve
    mc"During the day and sometimes at night, [mc_v_address] works at a local diner as a waitress."
    mc"It's far from her dream job, but we all know she's doing it for us."
    #show the MC helping Vivian in the kitchen with dinner - a previous scene"
    show sc mansionoutside o121
    with dissolve
    mc"We've always been pretty close, probably because I'm one of the two males in her life."
    mc"I'm not usually one for being sentimental, but deep down I just want her to be proud of me."
    mc"And to help in some way to give her the life that she deserves."
    stop music2 fadeout 2.0
    scene black
    with Dissolve(1.0)
    pause 0.5
    play music "sound effects/01/Private Eye.mp3" loop fadein 1.0
    show sc mansionoutside o83
    with Dissolve(1.0)
    mc"That brings me to the last person that I'll be introducing."

    # Define Victor
    ################################################################
    $ choice_done = False
    $ mc_vic_address = vic_pre_address + " " + lastname # add now defined lastname to addressing
    while not choice_done:
        $ rel = renpy.input("He's my ... (Default: [vic_mc_rel])").strip()
        if not rel:
            $ rel = vic_mc_rel
        $ name = renpy.input("And his name is ... (Default: [vic_name])").strip()
        if not name:
            $ name = vic_name
        $ rel2 = renpy.input("He is my [rel], and I am his ... (Default: [mc_vic_rel])").strip()
        if not rel2:
            $ rel = mc_vic_rel
        $ address = renpy.input("I will address him as ... (Default: [mc_vic_address])").strip()
        if not address:
            $ address = mc_vic_address
        "Your [rel]'s name is [name] [lastname]."
        "You are his [rel2] and you will address him as [address], while he will address you by your first name."
        "Is that correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ vic_name = name
    $ vic_mc_rel = rel
    $ mc_vic_rel = rel2
    $ mc_vic_address = address

    ################################################################
    # define sisters/roommates
    ################################################################
    $ choice_done = False
    while not choice_done:
        $ rel = renpy.input("You call [a_name] and/or [b_name] your ... (Default: [mc_a_b_rel] - use singular)").strip()
        if not rel:
            $ rel = mc_a_b_rel
        $ rel2 = renpy.input("You call [v_name] and/or [vic_name] your ... (Default: [mc_v_vic_rel] - use singular)").strip()
        if not rel2:
            $ rel2 = mc_v_vic_rel
        "The girls are your [rel]s, and the married couple are your [rel2]s."
        "Are all these details correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ mc_a_b_rel = rel
    $ mc_v_vic_rel = rel2
    ################################################################
    ################################################################

    # define Group/Team
    ################################################################
    $ choice_done = False
    while not choice_done:
        $ rel = renpy.input("That's it! Now you know the whole... (Default: [private_group])").strip()
        if not rel:
            $ rel = private_group
        $ rel2 = renpy.input("But the people that have never met us would see us as a... (Default: [public_group])").strip()
        if not rel2:
            $ rel2 = public_group
        "Together, we make up a [rel] of high-quality thieves, but people who do not know us, see us as a [rel2]."
        "Are all these details correct?"
        menu:
            "YES":
                $ choice_done = True
            "NO":
                "Okay, not to worry. Let's try this again."
    $ private_group = rel
    $ public_group = rel2
    ################################################################

    # From now on allow access to redefine Names and relationships in Preferences -> Exta
    $ v_allow_redefine = True

    # Enable the option for future games to use the currently stored values and skipping the naming intro.
    $ persistent.v_allow_previous_names = True

    # Store the set names as psersistant variables to be used by later games
    $ set_persistent_names("set")
    ######################################################################################

    #have the screen switch from Vivian across to Victor", who sits in the passenger seat up front
    #show various images of Mom here while the MC is telling her story - past and present - showing her "
    show sc mansionoutside o80
    with dissolve
    mc"[mc_vic_address]'s been doing this kind of work from a very young age."
    #show Victor as a thief in his younger days - https://frinkiac.com/img/S09E16/575724.jpg"
    mc"Not only is he the leader of our team, but he's also the brains behind each job, robbery or heist that we do."
    #show a previous scene where Victor hosts a meeting with the rest of the team, discussing a heist - e.g. https://m.media-amazon.com/images/M/MV5BNDkwMjc0MzgyMl5BMl5BanBnXkFtZTgwMDQyNzM3MTI@._V1_QL75_UX500_CR0,46,500,281_.jpg"
    show sc mansionoutside o122
    with dissolve
    mc"Like with today's job, [mc_vic_address] lays out the plan for us to all learn and memorize, weeks in advance."
    mc"He explains each of our roles in specific detail and expects us to know everything inside-out."
    show sc mansionoutside o123
    with dissolve
    mc"Away from being a thief, he's a limo driver for the rich folk in town."
    show sc mansionoutside o124
    with dissolve
    mc"He took the gig on to learn more about rich families we could steal from that can ultimately help to provide for all of us."
    show sc mansionoutside o125
    with dissolve
    mc"It's incredibly rare if he does a job by himself nowadays, which is why the rest of us have become so important to him with each mission."
    mc"At least, that's what he told me once."
    stop music fadeout 2.0
    scene black
    with Dissolve(1.0)
    pause 0.5
    play music "sound effects/01/C-Funk.mp3" loop fadein 1.0
    show sc mansionoutside o126
    with Dissolve(1.0)
    #show Victor and the older sis arguing"
    mc"[mc_vic_address] and [b_name] butt heads quite frequently."
    show sc mansionoutside o127
    with dissolve
    mc"It's mainly because of the strict rules that he has set for all of us."
    mc"[b_name] rebels against that which usually leads to heated arguments."
    show sc mansionoutside o128
    with dissolve
    mc"And it's always [mc_v_address] who has to step in to keep the peace."
    show sc mansionoutside o128a
    with dissolve
    mc"And she usually does."
    show sc mansionoutside o128b
    with dissolve
    mc"All of us having a job that brings in money helps to keep us afloat."
    show sc mansionoutside o129
    with dissolve
    mc"That's just one of his rules. Everyone must be working a paid job at all times."
    mc"A nine o'clock curfew, unless we're working, is another."
    #show the MC talking to the player again"
    show sc mansionoutside o107
    with dissolve
    mc"So we're not exactly living below the poverty line, but life could certainly be a hell of a lot better."

    #show Victor at a local bar, drinking scotch"

    show sc mansionoutside o130
    with dissolve
    mc"[mc_vic_address] can often be incredibly selfish, condescending and downright hypocritical."
    mc"He sets rules for the three of us and also [mc_v_address], but doesn't abide by them himself."
    mc"It sucks ass, but I'm in no position to argue with him, nor is anyone else."

    #show the MC talking to the player"
    #IMPORTANT DOTS - The MC is cocky, funny, confident, but also has his heart in the right place - like Wade Wilson

    stop music fadeout 1.0
    show sc mansionoutside o159
    with dissolve
    mc"So that just leaves me."
    show sc mansionoutside o108
    mc"Hmm... Where do I start?"
    play music "sound effects/01/Stronger Together.mp3" loop fadein 1.0

    show sc mansionoutside o131
    with dissolve
    mc"I live with two girls, [b_name] and [a_name], my [v_mc_rel] [v_name] and my [vic_mc_rel] [vic_name]. They got married six months after [b_name] was born."

    #show the MC working behind the counter at a gym"
    mc"I dropped out of high school as soon as I legally could."
    show sc mansionoutside o132
    with dissolve
    mc"During the day and sometimes nights, I work at a local gym."
    mc"It's a decent enough cover, I guess."
    mc"No one would suspect that I'm leading a double life."
    mc"Well, not yet."

    #scene continues

    show sc grouphouse f15
    with dissolve
    mc"This was always [mc_vic_address]'s intention, but not so much [mc_v_address]'s."
    mc"She kind of just went along with it, especially when things got tough financially for the entire [private_group]."

    show sc gymjuliet j06
    with dissolve
    mc"All of us having steady jobs is for the purpose of aiding us in this life of thieving."

    #show the MC lifting weights"
    show sc mansionoutside o133
    with dissolve
    mc"Considering some of the strenuous, physical activities we sometimes have to do for these heists, keeping in tip-top
    shape is incredibly important to me."
    #show the MC checking out hot women in the gym - https://upload.wikimedia.org/wikipedia/it/thumb/5/52/Call_on_Me.png/1200px-Call_on_Me.png“
    show sc mansionoutside o134
    with dissolve
    mc"Plus I like checking out the hot women that sometimes drop in for a workout."
    mc"I guess if I wasn't so great at being a criminal, then I'd love to have my own gym one day."
    #show the MC daydreaming behind the counter at the gym"
    show sc mansionoutside o108
    with dissolve
    mc"But that seems like a pipe dream that will never come true."
    #go back to the MC talking to the player inside the van"
    show sc mansionoutside o161
    with dissolve
    mc"Thanks to years of studying and training in various forms of martial arts, I know how to take care of myself."
    show sc mansionoutside o162
    with dissolve
    pause 1.5
    show sc mansionoutside o163
    with dissolve
    pause 1.5
    scene black
    with dissolve
    pause 1.0

    show sc mansionoutside o159
    with dissolve
    mc"So why do I want to continue being a thief?"
    show sc mansionoutside o158
    mc"Well, it's actually quite simple."
    stop music fadeout 2.0
    scene black
    with dissolve

    play music "sound effects/01/Strength in My Blood.mp3" loop fadein 1.5
    show sc mansionoutside o142
    with dissolve
    mc"I suppose it's because it's all I've ever really known."
    show sc mansionoutside o143
    with dissolve
    mc"I get such an adrenaline rush even at just the idea of committing a crime and then getting away with it."
    #go back to the MC talking to the player inside the van"
    show sc mansionoutside o144
    with dissolve
    mc"My best skills?"
    mc"I'm a team player. I want the best for everyone in our little group."
    show sc mansionoutside o145
    with dissolve
    mc"And I'd do anything for them."
    show sc mansionoutside o146
    with dissolve
    mc"I'm also very good with my hands..."
    show sc mansionoutside o147
    with dissolve
    mc"And not just when I'm working a job."
    #show the MC chatting up a bartender or waitress - https://www.youtube.com/watch?v=RR2AopBfSnE&ab_channel=Mirrorshade%E2%84%A2“
    show sc mansionoutside o135
    with dissolve
    mc"I'm great at making conversation and I love being around highly attractive women."
    mc"Sometimes I just automatically click with them, you know?"
    #show the MC hooking up or making out with the same waitress - maybe base the waitress on Jo, MD - https://upload.wikimedia.org/wikipedia/en/9/95/Joharvelle.JPG“
    show sc mansionoutside o136
    with dissolve
    mc"I suppose it kind of explains why I enjoy being a part of this team."
    scene black
    with Dissolve(1.0)
    pause 0.5
    #show the other three women here"
    show sc mansionoutside o81
    with dissolve
    mc"I know I shouldn't be saying this, but the girls are all pretty damn attractive in their own right."
    show sc mansionoutside o84
    with dissolve
    mc"Which is definitely a huge asset to have when you're in the thieving game."
    show sc mansionoutside o82
    with dissolve
    mc"You'll get to see plenty of these three, and a whole lot more the longer you stick around."
    mc"I promise!"
    stop music fadeout 1.0
    scene black
    with Dissolve(1.0)
    pause 0.5
    play ambient "sound effects/01/truck_interior_sound_effect.ogg" loop fadein 1.0
    show sc mansionoutside o159
    with dissolve
    mc"So that's pretty much it..."
    mc"This is our [private_group]. This is what we do."
    show sc mansionoutside o106
    mc"And we'll be planning and attempting to carry out even bigger jobs in the future."
    show sc mansionoutside o107
    mc"That's about all you need to know about us for now."
    show sc mansionoutside o159
    mc"So strap in for the ride!"
    #MC winks at the player"
    show sc mansionoutside o158
    mc"Anyway, let's get back to the story..."

label lb_ep01_intro_05_heist_scene_02:
    #victor speaks to the MC from the driver's seat"
    show sc mansionoutside o148
    with dissolve
    vic"When we get home, [y_name], I'm going to need you to get rid of the van."
    vic"We have to dispose of any evidence that could connect us to the job, and also just in case someone spotted any of you entering this vehicle."
    #the MC replies from the back of the van"
    show sc mansionoutside o149
    mc"Sure thing, [mc_vic_address]. I'll take care of it."
    ####### ADD THE TABLET ICON
    show screen toh_main_game_screen

    ##########################
    $ v_mm_available = False
    $ v_stats_task_1 = "Steal information from the Walker family residence."
    $ v_stats_task_1_completed = True
    $ v_stats_poi_1 = "The Mystery Girl at the Birthday Party"
    $ v_stats_task_1_rating = "aa"


    #victor goes back to driving and the MC addresses the player one last time"
    show sc mansionoutside o150
    mc"Oh, just a few more things that you need to know..."
    show sc mansionoutside o152a
    mc"In case you didn't see it, there's a new icon in the top left corner of your screen."
    show sc mansionoutside o151
    mc"Clicking on it will take you to a special menu where you will be able to configure or check various things while you are playing the game."
    #the MC points to the top-left corner of the screen
    #OPTIONS - Skip Tutorial/Learn More

    menu:
        "Skip Tutorial":
            show sc mansionoutside o151
            mc"Ah, so you're a know-it-all type, huh?"
            show sc mansionoutside o150
            mc"All right, fair enough."
            $ v_mm_available = True

        "Learn More":
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ quick_menu = False
            play music "sound effects/01/Airport Lounge.mp3" loop fadein 1.0
            stop ambient fadeout 1.0
            jump lb_ep01_intro_tutorial_01
            call screen scr_ep01_intro_tutorial_01
            show sc mansionoutside o159


label lb_ep01_01_04_intro_continue:
    $ v_mm_available = True
    $ quick_menu = True
    show sc mansionoutside o151
    mc"The other thing I want to say is that today was my first major test."
    mc"To see if I could lead and pull off a heist without getting caught."
    show sc mansionoutside o150
    mc"Sure, I made a couple of minor errors. It happens."
    #mc smiles"
    show sc mansionoutside o152
    mc"Other than that, it looks like I passed with flying colors!"
    #the MC checks his inside pocket"
    show sc mansionoutside o153
    mc"Especially after I managed to get out of the house with this."
    stop ambient fadeout 1.0
    play music "sound effects/01/Endless Highway.mp3" loop
    show sc mansionoutside o154
    with vpunch
    mc"(Oh... Crap!)"
    #show the MC with a worried look on his face"
    show sc mansionoutside o155
    with dissolve
    mc"(It's gone...)"
    scene black
    hide screen toh_main_game_screen
    $ quick_menu = False
    show screen scr_ep01_01_04_Intro_Movie
    show intro_movie:
        align(0.5,0.5)
    pause 19
    stop music fadeout 3.0
    hide intro_movie
    hide screen scr_ep01_01_04_Intro_Movie
    #We see the outside of the van driving and then after it drives down the street, the screen scrolls upwards, into the sky and then we see the:
    #"THIEF OF HEARTS" Logo appears on the screen with the blue sky background."
    #stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_group_meeting_home

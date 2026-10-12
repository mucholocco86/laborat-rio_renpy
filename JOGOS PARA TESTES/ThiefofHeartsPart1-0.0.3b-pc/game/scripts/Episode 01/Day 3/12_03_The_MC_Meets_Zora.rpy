label lb_ep01_The_MC_meets_Zora:
    #the MC starts at the same place he has ended in any of the scenes with Vivian, Ariel or Bella
    #He'll be on the street and is about to make a phone call but sees a girl being
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/ghetto_street_ambience.ogg" loop fadein 1.0
    scene sc zoras z001
    with dissolve
    if v_ep01_mc_task_visit_options_2 != "" and not v_ep01_mc_task_visit_options_1 != "":
        mc"(My day's almost over. I'm looking forward to having a nice relaxing night in.)"
    else:
        mc"(I better make a call to see if she's available to do the job.)"
    #The MC sees Zora when he looks up
    show sc zoras z002
    mc"(Hmm... That girls looks lost.)"

    #ROLLING SCREEN OF ZORA WALKING DOWN A DODGY BROKEN-DOWN STREET
    #show sc zoras z003
    #Show her towards the MC looking worried
    #Make sure she's wearing a pretty necklace
    show sc zoras z004
    mc"(I've never seen her before, but she definitely looks like she's not from around here.)"
    show sc zoras z006
    mc"(I should take a closer look as I have bad feeling about this.)"
    #switch to Zora's POV
    show sc zoras z004
    un"(What am I doing here?)"
    show sc zoras z008
    un"(I shouldn't have tried to take that shortcut.)"
    show sc zoras z007
    un"(Maybe I could ask that guy for help.)"
    show sc zoras z012
    un"Excuse me, Sir?"
    show sc zoras z009
    thug"Hey little lady..."
    show sc zoras z010
    thug"You shouldn't be walking around these parts."
    show sc zoras z011
    thug"Are you by yourself?"
    show sc zoras z012
    un"Um... Yeah."
    show sc zoras z013
    un"I'm sorry. I need to get back to the main part of town."
    un"Can you help me?"
    show sc zoras z014
    thug"Sure I can."
    show sc zoras z015
    thug"But it's gonna cost you."
    show sc zoras z016
    un"Oh... How much?"
    show sc zoras z017
    thug"How much you got?"
    show sc zoras z018
    un"I have around thirty dollars on me. That should be enough, right?"
    show sc zoras z019
    thug"Hmm... How about we start with this instead."
    #The thug grabs her necklace and rips it from her neck
    show sc zoras z020
    un"What?!"
    play sound "sound effects/01/snapping_sound.ogg"
    show sc zoras z021
    with hpunch
    un"Ow!"
    thug"This should fetch me a lot more than thirty dollars."
    show sc zoras z022
    un"Please... My grandmother gave me that."
    show sc zoras z023
    thug"And I'll be taking that ring as well."
    show sc zoras z024
    un"No..."
    show sc zoras z025
    thug"Oh yes."
    show sc zoras z025a
    menu:
        "Help her"(wt="Best option"):
            #The MC stands behind the thug
            show sc zoras z026
            mc"Hey asshat!"
        "Wait and watch":
            show sc zoras z019
            thug"I'm sure there's a lot of other things I can take from you."
            mc"(Ah, shit... I better step in before things gets really bad.)"
    show sc zoras z027
    mc"She said no."
    #The thug turns around and sees the MC
    show sc zoras z028
    thug"And what's it to you, asshole?"
    show sc zoras z029
    mc"Now, now... Is that any way to talk in front of a young lady?"
    show sc zoras z030
    thug"You picked the wrong conversation to interrupt."
    #The thug takes a swing at the MC's face and he catches his fist.
    play sound "sound effects/01/punch_to_fist_effect.mp3"
    show sc zoras z031
    with hpunch
    pause 0.5
    show sc zoras z032
    with faster_dissolve
    thug"Huh?"
    stop sound fadeout 1.0
    #The MC twists his arm around so it's pressed up against his back
    play sound2 "sound effects/01/bone_break1.ogg"
    show sc zoras z033
    pause 0.5
    play sound3 "sound effects/01/male_scream_sound_effect1.mp3"
    thug"Ahhh!!!" with hpunch
    show sc zoras z034
    mc"I think I'm definitely a part of this conversation."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    show sc zoras z035
    thug"You son of bitch!"
    show sc zoras z036
    thug"Uhhh!! Fuck!!!"
    thug"You're twisting my arm!"
    show sc zoras z037
    mc"Again with the potty mouth."
    show sc zoras z038
    mc"Tsk, tsk... People just never learn."
    #The MC tightens his grip on the thug so he screams in pain again
    show sc zoras z039
    play sound "sound effects/01/bone_break2.ogg"
    with hpunch
    thug"All right, all right..."
    show sc zoras z040
    thug"I'm sorry."
    stop sound fadeout 1.0
    show sc zoras z041
    mc"I'm sorry, what?"
    show sc zoras z042
    thug"I'm sorry, man."
    show sc zoras z044
    mc"Don't say sorry to me, dumbass."
    mc"Say sorry to..."
    show sc zoras z045
    mc"Sorry, what's your name?"
    show sc zoras z046
    zora"It's Zora."
    show sc zoras z047
    mc"Nice name."
    #The MC gets close to the back of the thug's head
    show sc zoras z048
    mc"Say it."
    show sc zoras z049
    thug"I'm sorry, Zora."
    show sc zoras z050
    mc"Now give the young lady back her necklace and ring."
    #With his spare hand, the thug hands Zora her necklace back and her ring
    show sc zoras z051
    pause 1.5
    show sc zoras z052
    with dissolve
    thug"Okay, I gave them back to her. Will you let me go now?"
    show sc zoras z053
    mc"One more thing..."
    #The MC whispers up close to the thug's ear
    show sc zoras z054
    mc"If you ever come near Zora again..."
    show sc zoras z055
    mc"I'll make my foot a permanent resident of your rear end. Complete with the aroma of shoe polish as a constant reminder."
    mc"Do you hear me?"
    show sc zoras z056
    thug"Yes, yes, I hear ya!"
    show sc zoras z057
    mc"Get the hell out of here!"
    #The MC pushes the thug forward, releasing him, and he scurries off
    show sc zoras z058
    with dissolve
    mc"Good riddance."
    #The MC turns to Zora
    show sc zoras z059
    with dissolve
    mc"Are you okay?"
    show sc zoras z061
    zora"Yeah, I think so."
    show sc zoras z062
    zora"Thank you so much for your help."
    zora"I'm-"
    show sc zoras z063
    mc"Zora... I heard."
    show sc zoras z064
    mc"And I'm [y_name]."
    show sc zoras z065
    zora"Well, thank you, [y_name]."
    show sc zoras z059
    mc"Where were you trying to get to?"
    show sc zoras z067
    zora"I was trying to find the main part of town. Can you help me?"
    show sc zoras z068
    mc"For sure."
    #final shot here is the MC walking with Zora out of the dodgy street
    show sc zoras z063
    mc"Follow me..."
    #screen goes blank
    stop ambient fadeout 1.0
    scene black
    with dissolve
    with Pause (1)
    #Show them walking into town
    play music "sound effects/01/Sunshine Walk1.mp3" loop fadein 1.0
    show sc zoras z069
    with dissolve
    pause 1.5
    show sc zoras z071
    with dissolve
    zora"So you live around here?"
    show sc zoras z073
    mc"Not in the centre of town but pretty close."
    show sc zoras z072
    mc"So where are you from?"
    show sc zoras z075
    zora"Oh... I'm from the other side of the city."
    show sc zoras z077
    zora"Which is kind of why I don't know these streets very well."
    show sc zoras z076
    mc"Were you looking for someone in particular?"
    show sc zoras z079
    zora"Not so much someone. I was looking for a local gym."
    show sc zoras z078
    mc"Really? Don't they have one near where you live?"
    show sc zoras z079
    zora"They do, but-"
    zora"It's a long story."
    show sc zoras z080
    zora"I don't want to bore you with all the details."
    menu:
        "Say something":
            show sc zoras z107
            mc"Thanks..."
            show sc zoras z099
            mc"I mean, tell me all about it."

        "Hear her out"(wt="Best option"):
            show sc zoras z082
            mc"Try me."

    show sc zoras z084
    zora"Okay... Where I'm from, I prefer to remain discreet about working out and getting into shape."
    zora"Everyone knows who I am and also my family."
    show sc zoras z085
    zora"But here, no one knows me."
    show sc zoras z086
    mc"(Zora sounds like she could be someone important.)"
    show sc zoras z087
    mc"(Not like \"royalty\" important, but if she were to go missing, it would be a big deal.)"
    show sc zoras z088
    mc"So you're from the rich part of town then."
    show sc zoras z089
    zora"Yeah..."
    show sc zoras z090
    zora"You probably think I'm a self-absorbed, snobby rich girl, right?"
    menu:
        "Ask her a question":
            show sc zoras z109
            mc"Well, are you?"
            show sc zoras z112
            zora"Excuse me?"
            show sc zoras z108
            mc"I don't mean to be rude, but..."

        "Dismiss her claim"(wt="Best option"):
            show sc zoras z091
            mc"No, not at all."

    show sc zoras z092
    with dissolve
    mc"I guess I'm trying to understand why someone would care so much about what other people think."
    show sc zoras z094
    zora"I just needed to do something for me, you know?"
    show sc zoras z095
    zora"Coming here wasn't easy, and finding a gym is an even bigger step for me to take. I've avoided going to one my whole life."
    show sc zoras z089
    zora"But... I've chosen to finally make this first step, and that's always the hardest part, right?"
    show sc zoras z096
    mc"(Hmm... That's usually what we tell new signups at our gym.)"
    show sc zoras z097
    zora"I would have thought that someone who is in really great shape like yourself would understand."
    show sc zoras z098
    zora"But maybe not."
    show sc zoras z099
    mc"Woah, woah... Let's back up a bit."
    show sc zoras z100
    mc"I completely get where you're coming from."
    show sc zoras z101
    zora"Really? What are you like a personal trainer or something?"
    #The MC stops and gives Zora a knowing look
    show sc zoras z102
    mc"Well..."
    show sc zoras z103
    zora"Oh my God... Seriously??"
    show sc zoras z104
    mc"Yeah, and I work at a local gym in town."
    show sc zoras z105
    zora"I am so sorry."
    show sc zoras z106
    zora"That's typical of me."
    show sc zoras z107
    zora"The one person I'm looking for, and I make a complete fool of myself before I've even started a session."
    menu:
        "It happens"(wt="Best option"):
            show sc zoras z108
            mc"Hey, it happens to the best of us."

        "It's okay":
            show sc zoras z108
            mc"It's okay, you weren't to know."
    show sc zoras z106
    with fast_dissolve
    pause 1.5
    show sc zoras z109
    with fast_dissolve
    mc"So you're searching for a personal trainer then?"
    show sc zoras z110
    zora"Yes, very much so."
    show sc zoras z111
    zora"And I can pay you well in advance for numerous sessions."
    show sc zoras z112
    zora"I just want to do this right."
    show sc zoras z113
    mc"That's good. And I'd be more than happy to help you."
    $ task_addpoi("Zora - Girl who is looking for a personal trainer",6)
    show sc zoras z114
    zora"Can we start today?"
    show sc zoras z115
    mc"Unfortunately no, I have to be somewhere right now."
    show sc zoras z116b
    mc"But here's my card."
    #The MC hands her a business card from the gym
    show sc zoras z116
    zora"Thanks."
    show sc zoras z117
    mc"And if you're going to the gym now, then ask for a guy named Harry."
    mc"Tell him I sent you and that you would like to have a personal session with me next week."
    show sc zoras z119
    zora"What day should I book?"
    show sc zoras z118
    mc"Whatever day suits you."
    show sc zoras z120
    mc"I'll talk to the boss when I go to work tomorrow and make sure he schedule's me for that day."
    show sc zoras z121
    mc"Any other questions?"
    show sc zoras z124
    zora"Yeah..."
    show sc zoras z125
    zora"Where did you learn to take care of yourself like that?"
    show sc zoras z122
    mc"Do you mean with that guy back there?"
    show sc zoras z115
    mc"Oh, well..."
    show sc zoras z121
    mc"I took several martial arts classes throughout my teens."
    show sc zoras z120
    mc"I picked up a thing or two."
    show sc zoras z125
    zora"I don't suppose it will be part of our lesson next week?"
    show sc zoras z128
    mc"It's not part of a normal lesson, but I could show you a few moves, even some that I came up with."
    show sc zoras z126
    zora"I'd like that."
    #The MC points here below
    show sc zoras z123
    mc"Anyway, if you walk down there for a couple of blocks, you'll find the gym."
    show sc zoras z124
    zora"And I'll ask for Harry."
    show sc zoras z120
    mc"That's right."
    show sc zoras z126
    zora"Thank you, [y_name], for coming to my rescue, for walking me into town and um..."
    show sc zoras z127
    zora"For telling me about your gym."
    show sc zoras z114
    zora"I guess I'll see you next week. I'm already looking forward to it."
    $ task_addfuturetask("Beginners workout session with Zora",3)
    show sc zoras z121
    mc"Yeah, me too, Zora."
    show sc zoras z129
    zora"Bye..."
    #Zora walks towards the gym and looks over her shoulder at the MC
    show sc zoras z130
    mc"(And there's my good deed done for the day.)"
    show sc zoras z131
    mc"(Well, at least one of them.)"
    #The MC focuses on the final job
    show sc zoras z132
    mc"(Now to make that phone call so I can do these final tasks I promised to help with...)"
    stop music fadeout 1.0

    #Vivian / Ariel / Bella

    #IMPORTANT - only the choices the player hasn't made yet will be available on the screen here
    menu:
        "[v_name]" if not v_ep01_mc_task_visit_options_1 == "[v_name]":



            #screen goes blank
            scene black
            with dissolve
            jump lb_ep01_12_03_MC_Calls_Vivian



        "[a_name]" if not v_ep01_mc_task_visit_options_1 == "[a_name]":

            #screen goes blank
            scene black
            with dissolve
            jump lb_ep01_12_03_MC_Calls_Ariel



    #SCENE CONTINUES WITH > Scene 12-04 - The MC helps Ariel steal security cards

        "[b_name]" if not v_ep01_mc_task_visit_options_1 == "[b_name]":

            #screen goes blank
            scene black
            with dissolve
            jump lb_ep01_12_03_MC_Calls_Bella





label lb_ep01_12_03_MC_Calls_Ariel:
            show sc zoras z133
            with dissolve
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3"
            show sc zoras z134
            pause 2.0
            #The MC calls Ariel
            stop sound fadeout 1.0
            play music "sound effects/01/Family_Ties2.mp3" loop fadein 1.0
            show sc zoras z142
            with dissolve
            a"Hello?"
            show sc zoras z134
            mc"[a_name]?"
            show sc zoras z143
            a"Oh, hey [y_name]. What's up?"
            show sc zoras z138
            mc"Sorry to bother you, but I was wondering if we could check out that security systems place."
            mc"Preferably now."
            show sc zoras z144
            a"Oh, how come?"
            show sc zoras z139
            mc"I'm free at the moment, and if we don't go soon, then I might not be able to help you later."
            show sc zoras z145
            a"Hmm... It's a little sooner than I was planning to go there, but if I move some things around, then it can work."
            show sc zoras z146
            a"But you're going to need to come home first, I have something that you'll need."
            show sc zoras z134
            mc"Um... Okay."
            show sc zoras z138
            mc"I should be home in about fifteen minutes."
            show sc zoras z147
            a"Sweet, I'll see you shortly..."
            stop music fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #The MC waits patiently in the living room for Ariel
            show sc arielhome a10
            with dissolve
            a"Are you ready to leave, [y_name]?"
            #The MC looks up and Ariel has changed into a security systems outfit - https://pixhost.to/show/1044/447513812_000.jpg
            show sc arielhome a09
            mc"Yeah, I'm all set."
            show sc arielhome a16
            mc"What's that you're wearing?"
            show sc arielhome a11
            a"This is the security staff uniform for the place we'll be going to."
            show sc arielhome a12
            a"I had [mc_v_address] find me a similar dress shirt that matches their uniform."
            show sc arielhome a11
            a"It should help us to blend in."
            show sc arielhome a14
            a"What do you think?"
            #Ariel poses for him
            show sc arielhome a16
            mc"Yeah, you look great."
            show sc arielhome a18
            a"I also made us some fake employee ID cards."
            #She hands the MC a card with the name of the security place and his face on it
            show sc arielhome a17
            mc"Sweet!"
            show sc arielhome a12
            a"I have a shirt for you too."
            #She has him the shirt
            show sc arielhome a13
            a"I left it upstairs in your room though."
            show sc arielhome a11
            a"Once you've put it on, we can get going."
            #Ariel smiles
            show sc arielhome a10
            mc"Sure thing, [a_name]."
            $ v_ep01_mc_task_visit_options_2 = "[a_name]"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_12_04_card_theft1
            #SCENE CONTINUES WITH > Scene 12-04 - The MC helps Ariel steal security cards


label lb_ep01_12_03_MC_Calls_Vivian:
            show sc zoras z133
            with dissolve
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3" fadein 1.0
            show sc zoras z134
            pause 4.0
            stop sound fadeout 1.0
            play music "sound effects/01/Frayed_Relations1.mp3" loop fadein 1.0
            #The MC calls Vivian
            show sc zoras z134
            with dissolve
            mc"[mc_v_address]?"
            show sc zoras z135
            v"What's up, sweetheart?"
            show sc zoras z136
            v"Where are you?"
            show sc zoras z138
            mc"I'm near the centre of town."
            show sc zoras z139
            mc"Is there any chance we could go to the theatre now?"
            show sc zoras z137
            mc"I have a few things I have to do, and if we don't go now, then I can't guarantee that I'll be able to help you later."
            show sc zoras z140
            v"Oh, well in that case, we can go to the theatre right away!"
            show sc zoras z141
            v"I'll pick you up on the way there. Let me know where you are..."
            stop music fadeout 1.0
            $ v_ep01_mc_task_visit_options_2 = "[v_name]"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_and_Vivian_acting_school1

            #SCENE CONTINUES WITH > Scene 12-02- The MC helps Vivian Infiltrate the acting school and steal the wig and dress


label lb_ep01_12_03_MC_Calls_Bella:
            show sc zoras z133
            with dissolve
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3" fadein 1.0
            show sc zoras z134
            pause 2.0
            #The MC calls Bella
            stop sound fadeout 1.0
            play music "sound effects/01/Blues_Fight.mp3" loop fadein 1.0
            show sc zoras z149
            with dissolve
            b"Hello?"
            show sc zoras z134
            mc"[b_name]?"
            show sc zoras z148
            b"Oh, it's you. What do you want?"
            show sc zoras z138
            mc"I know you probably wanted to go to this art school a little later on, but is there any chance we could go sooner, as in, right now?"
            show sc zoras z150
            b"Why?"
            show sc zoras z139
            mc"I have a few things I have to do is all."
            show sc zoras z151
            b"This is not very convenient, [y_name]."
            show sc zoras z153
            b"The school will still be in session so there will be plenty of students and staff on the grounds if we were to go now."
            show sc zoras z152
            b"So it's not a great time."
            show sc zoras z137
            mc"I understand. However, if we don't go now, then I can't guarantee that I'll be able to help you later."
            show sc zoras z151
            b"(Sigh...)"
            show sc zoras z148
            b"All right, fine."
            show sc zoras z153
            b"I'll have to make some adjustments to the plan on the way there."
            show sc zoras z149
            b"Where are you right now?"
            show sc zoras z138
            mc"I'm near the centre of town but I can meet you at the art school."
            show sc zoras z153
            b"Fine, I'll leave here in a few minutes and meet you there..."
            #screen goes blank
            $ v_ep01_mc_task_visit_options_2 = "[b_name]"
            stop music fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_and_Bella_at_the_art_school

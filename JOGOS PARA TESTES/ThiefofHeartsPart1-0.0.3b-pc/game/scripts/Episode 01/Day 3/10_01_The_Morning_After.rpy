init:
    image sc morningafter wake up:
        "sc morningafter m02" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc morningafter m03" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc morningafter m02" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc morningafter m03" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc morningafter m02" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc morningafter m03" with Dissolve(0.2, alpha=True)

label lb_ep01_the_morning_after:
    if v_ep01_09_01_Tasha_Sex_path == True:
        #"This scene if the player chose TASHA"
        #the MC wakes up alone in the bedroom he was in with Tasha
        centered "The next morning...{w=2.0}{nw}" with dissolve
        show text "The next morning..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
        scene bg black with Dissolve(1)
        pause 1.0
        scene sc morningafter m01
        with dissolve
        pause 0.5
        if persistent.v_anim_enabled:
            show sc morningafter wake up
        else:
            show sc morningafter m03
        mc"Mmm..."
        show sc morningafter m04
        pause 1.0
        #His eyes flutter open and he looks around
        show sc morningafter m07
        mc"Tasha?"
        show sc morningafter m08
        mc"(Hmm... She must be having breakfast with Mikayla and Harry.)"
        #The MC sits up and looks around for his clothes
        show sc morningafter m05
        mc"Hmm..."
        show sc morningafter m06
        mc"(Where did I put my clothes?)"
        #The MC looks at the bedside table
        mc"(And my wallet?)"
        mc"(Wait a second...)"
        mc"(I think I've been-)"
        #Harry bursts into the room naked, holding his hands over his crotch
        show sc morningafter m13
        with vpunch
        ha"DUDE!!!"
        show sc morningafter m14
        ha"I've been robbed!!"
        show sc morningafter m09
        mc"You too?"
        show sc morningafter m19
        ha"You were robbed as well?"
        show sc morningafter m11
        mc"Hmm..."
        #The MC realises he's been robbed
        #Flashback scene to the night before when the MC was talking with Mikayla at the club
        show sc harrybar b213
        with flash(0.25, 0, 0.75, "#fff")
        mik"True... The same thing is happening in my hometown."
        mik"And the scary thing about that is that just about anybody could be a thief."
        #The flashback ends and goes back to the MC in the bedroom
        show sc morningafter m09
        with flash(0.25, 0, 0.75, "#fff")
        mc"SON OF A BITCH!!" with vpunch
        show sc morningafter m17
        ha"For fucks sake!! Is everybody in this town a goddamn thief??"
        show sc morningafter m20
        mc"Y-yeah... It sure feels like it."
        show sc morningafter m19
        ha"Should we call hotel reception?"
        show sc morningafter m10
        mc"What good will that do?"
        show sc morningafter m19
        ha"They might have the girl's names on file."
        show sc morningafter m12
        mc"I don't think they'd be stupid enough to use their actual names."
        show sc morningafter m10
        mc"They probably weren't even flight attendants."
        show sc morningafter m19
        ha"How do you know so much about this?"
        show sc morningafter m09
        mc"I um..."
        show sc morningafter m07
        mc"I watch a lot of \"Good Girls\"."
        show sc morningafter m19
        ha"Oh..."
        show sc morningafter m07
        mc"They're probably long gone by now."
        show sc morningafter m10
        mc"But we'll keep our eyes peeled in case we see them again in the future."
        $ task_addpoi("Mikayla & Tasha - Girls at the Eager Beaver club",5)
        show sc morningafter m14
        ha"What the hell are we going to do??"
        show sc morningafter m12
        mc"Well, neither of us can call a cab because we don't have any money."
        show sc morningafter m17
        ha"Yeah, they took my wallet. And also my phone."
        show sc morningafter m07
        mc"Yeah, mine too."
        show sc morningafter m19
        ha"You know, I think there's only one thing we can do."
        show sc morningafter m10
        mc"And what's that?"
        show sc morningafter m14
        ha"We're going to have to make a run for it!"
        show sc morningafter m09
        mc"What? All the way home!?"
        show sc morningafter m19
        ha"Yeah... What other choice do we have?"
        show sc morningafter m21
        mc"Well, the room is probably paid for. So we won't need to check out."
        show sc morningafter m09
        mc"We can leave the room card here."
        #the MC looks at the bedsheets
        show sc morningafter m07
        mc"But maybe we could take the bath towels with us."
        show sc morningafter m08
        mc"We'll have to try and avoid the security cameras on the way out though."
        show sc morningafter m19
        ha"We'll take the stairs down to reception and then dash right out of the front entrance."
        show sc morningafter m09
        mc"Good idea."
        show sc morningafter m10
        mc"So... We're really doing this?"
        show sc morningafter m17
        ha"Yeah... Let's make a run for it!"
        scene black
        with dissolve
        scene black
        with Pause (2)
        #show cross-fade
        #Proceeds to a scene where the MC and Harry are running out of the hotel front entrance
        show sc morningafter m22
        with flash(0.25, 0, 0.25, "#fff")
        play sound "sound effects/01/man_yelling1.mp3" noloop
        $ ui.timer(0.1, Play("sound2", "sound effects/01/man_yelling2.mp3", loop=True))
        play sound3 "sound effects/01/barefoot_running_loop.ogg" loop
        $ ui.timer(0.1, Play("sound4", "sound effects/01/barefoot_running_loop.ogg", loop=True))
        mc"Ahhhh! {w=1.0}{nw}"
        #Show the guys running through reception with the bedsheets around them while the receptionist stares with eyes wide open
        stop sound fadeout 1.0
        show sc morningafter m23
        with flash(0.25, 0, 0.25, "#fff")
        mc"Keep going, Harry!{w=1.0}{nw}" with dissolve
        scene black
        with dissolve
        scene black
        with Pause (2)
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        stop sound4 fadeout 1.0
        with Pause (2)

        #cross screen fade
        #show the MC and Harry running in the early morning past peoples' yards - holding bed sheets around their naked bodies, running all the way home
        #animated montage scene of them running - with the background changing while they run
        play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
        play sound "sound effects/01/barefoot_running_loop.ogg" loop
        $ ui.timer(0.1, Play("sound2", "sound effects/01/barefoot_running_loop.ogg", loop=True))
        show sc morningafter m24
        with dissolve
        ha"This is my street dude!"
        show sc morningafter m25
        ha"Call you later, once I get a new phone!!"
        show sc morningafter m26
        ha"See ya [y_name]!"
        #Harry runs off in a different direction
        show sc morningafter m27
        mc"(I haven't seen a single person since we left the hotel.)"
        show sc morningafter m28
        mc"(Which is pretty lucky.)"
        #The MC turns and sees a middle-aged woman walking a dog, who sees him standing on the sidewalk with the bedsheets around his body. She just stares at him
        show sc morningafter m29
        mc"(Uh-oh! I spoke too soon!)"
        show sc morningafter m30
        "Oh my God!"
        show sc morningafter m31
        mc"What? Haven't you ever seen a guy running near naked in broad daylight before?"
        #The lady gives him a strange look
        show sc morningafter m32
        mc"(I better get home before she calls the cops and I get arrested for indecent exposure!)"
        #Show a behind shot of the MC running a different way and we can see his butt not hidden by the sheets
        #screen goes blank
        stop ambient fadeout 1.0
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        #GO DOWN TO > #scene continues

    if v_ep01_09_01_Mikayla_Sex_path == True:
        #"This scene if the player chose MIKAYLA"
        centered "The next morning...{w=2.0}{nw}" with dissolve
        show text "The next morning..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
        scene bg black with Dissolve(1)
        pause 1.0
        scene sc morningafter wake up
        with dissolve
        mc"Mmm..."
        show sc morningafter m04
        pause 1.0
        #His eyes flutter open and he looks around
        show sc morningafter m07
        mc"Mikayla?"
        show sc morningafter m08
        mc"(Hmm... She must be having breakfast with Tasha and Harry.)"
        #The MC sits up and looks around for his clothes
        show sc morningafter m05
        mc"Hmm..."
        show sc morningafter m11
        mc"(Where did I put my clothes?)"
        #The MC looks at the bedside table
        show sc morningafter m06
        mc"(And my wallet?)"
        show sc morningafter m08
        mc"(Wait a second...)"
        show sc morningafter m09
        mc"(I think I've been-)"
        #Harry bursts into the room naked, holding his hands over his crotch
        show sc morningafter m13
        with vpunch
        ha"DUDE!!!"
        show sc morningafter m14
        ha"I've been robbed!!"
        show sc morningafter m09
        mc"You too?"
        show sc morningafter m19
        ha"You were robbed as well?"
        show sc morningafter m11
        mc"Hmm..."
        #The MC realises he's been robbed
        #Flashback scene to the night before when the MC was talking with Mikayla at the club
        show sc harrybar b213
        with flash(0.25, 0, 0.75, "#fff")
        mik"True... The same thing is happening in my hometown."
        mik"And the scary thing about that is that just about anybody could be a thief."
        #The flashback ends and goes back to the MC in the bedroom
        show sc morningafter m09
        with flash(0.25, 0, 0.75, "#fff")
        mc"SON OF A BITCH!!" with vpunch
        show sc morningafter m17
        ha"For fucks sake!! Is everybody in this town a goddamn thief??"
        show sc morningafter m20
        mc"Y-yeah... It sure feels like it."
        show sc morningafter m19
        ha"Should we call hotel reception?"
        show sc morningafter m10
        mc"What good will that do?"
        show sc morningafter m19
        ha"They might have the girl's names on file."
        show sc morningafter m12
        mc"I don't think they'd be stupid enough to use their actual names."
        show sc morningafter m10
        mc"They probably weren't even flight attendants."
        show sc morningafter m19
        ha"How do you know so much about this?"
        show sc morningafter m07
        mc"I um... I watch a lot of \"Good Girls\"."
        show sc morningafter m19
        ha"Oh..."
        show sc morningafter m07
        mc"They're probably long gone by now."
        show sc morningafter m10
        mc"But we'll keep our eyes peeled in case we see them again in the future."
        $ task_addpoi("Mikayla & Tasha - Girls at the Eager Beaver club",5)
        show sc morningafter m14
        ha"What the hell are we going to do??"
        show sc morningafter m12
        mc"Well, neither of us can call a cab because we don't have any money."
        show sc morningafter m17
        ha"Yeah, they took my wallet. And also my phone."
        show sc morningafter m07
        mc"Yeah, mine too."
        show sc morningafter m19
        ha"You know, I think there's only one thing we can do."
        show sc morningafter m10
        mc"And what's that?"
        show sc morningafter m14
        ha"We're going to have to make a run for it!"
        show sc morningafter m09
        mc"What? All the way home!?"
        show sc morningafter m19
        ha"Yeah... What other choice do we have?"
        show sc morningafter m21
        mc"Well, the room is probably paid for. So we won't need to check out."
        show sc morningafter m09
        mc"We can just leave the room card here."
        #the MC looks at the bedsheets
        show sc morningafter m07
        mc"But maybe we could take the bath towels with us."
        show sc morningafter m08
        mc"We'll just have to avoid the security cameras on the way out though."
        show sc morningafter m19
        ha"We'll take the stairs down to reception and then bolt right out of the front entrance."
        show sc morningafter m09
        mc"Good idea."
        show sc morningafter m10
        mc"So... We're really doing this?"
        show sc morningafter m17
        ha"Yeah... Let's make a run for it!"
        #show cross-fade
        #Proceeds to a scene where the MC and Harry are running out of the hotel front entrance
        show sc morningafter m22
        with flash(0.25, 0, 0.25, "#fff")
        play sound "sound effects/01/man_yelling1.mp3" noloop
        $ ui.timer(0.1, Play("sound2", "sound effects/01/man_yelling2.mp3", loop=True))
        play sound3 "sound effects/01/barefoot_running_loop.ogg" loop
        $ ui.timer(0.1, Play("sound4", "sound effects/01/barefoot_running_loop.ogg", loop=True))
        mc"Ahhhh! {w=1.0}{nw}"
        #Show the guys running through reception with the bedsheets around them while the receptionist stares with eyes wide open
        stop sound fadeout 1.0
        show sc morningafter m23
        with flash(0.25, 0, 0.25, "#fff")
        mc"Keep going, Harry!{w=1.0}{nw}" with dissolve
        scene black
        with dissolve
        scene black
        with Pause (2)
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        stop sound4 fadeout 1.0
        with Pause (2)

        #cross screen fade
        #show the MC and Harry running in the early morning past peoples' yards - holding bed sheets around their naked bodies, running all the way home
        #animated montage scene of them running - with the background changing while they run
        play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
        play sound "sound effects/01/barefoot_running_loop.ogg" loop
        $ ui.timer(0.1, Play("sound2", "sound effects/01/barefoot_running_loop.ogg", loop=True))
        show sc morningafter m24
        with dissolve
        ha"This is my street dude!"
        show sc morningafter m25
        ha"Call you later, once I get a new phone!!"
        show sc morningafter m26
        ha"See ya [y_name]!"
        #Harry runs off in a different direction
        show sc morningafter m27
        mc"(I haven't seen a single person since we left the hotel.)"
        show sc morningafter m28
        mc"(Which is pretty lucky.)"
        #The MC turns sees a middle-aged woman walking a dog, who sees him standing on the sidewalk with the bedsheets around his body. She just stares at him
        show sc morningafter m29
        mc"(Uh-oh! I spoke too soon!)"
        show sc morningafter m30
        "Oh my God!"
        show sc morningafter m31
        mc"What? Haven't you ever seen a guy running near naked in broad daylight before?"
        #The lady gives him a strange look
        show sc morningafter m32
        mc"(I better get home before she calls the cops and I get arrested for indecent exposure!)"
        stop ambient fadeout 1.0
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        #Show a behind shot of the MC running a different way and we can see his butt not hidden by the sheets
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        #GO DOWN TO > #scene continues

    if v_ep01_09_01_Tasha_and_Mikayla_Sex_path == True:
        #"This scene if the player selected CHOOSE BOTH"
        #the MC wakes up alone in the bedroom he was in with Mikayla and Tasha
        centered "The next morning...{w=2.0}{nw}" with dissolve
        show text "The next morning..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
        scene bg black with Dissolve(1)
        pause 1.0
        scene sc morningafter wake up
        with dissolve
        mc"Mmm..."
        show sc morningafter m04
        pause 1.0
        #His eyes flutter open and he looks around
        show sc morningafter m05
        mc"Mikayla?"
        show sc morningafter m08
        mc"Tasha?"
        show sc morningafter m11
        mc"(Hmm... They must be having breakfast.)"
        #The MC sits up and looks around for his clothes
        show sc morningafter m05
        mc"Hmm..."
        show sc morningafter m11
        mc"(Where did I put my clothes?)"
        #The MC looks at the bedside table
        show sc morningafter m06
        mc"(And my wallet?)"
        show sc morningafter m08
        mc"(Wait a second...)"
        show sc morningafter m09
        mc"(I think I've been-)"
        #The MC realises he's been robbed
        #Flashback scene to the night before when the MC was talking with Mikayla at the club
        show sc harrybar b213
        with flash(0.25, 0, 0.75, "#fff")
        mik"True... The same thing is happening in my hometown."
        mik"And the scary thing about that is that just about anybody could be a thief."
        #The flashback ends and goes back to the MC in the bedroom
        show sc morningafter m09
        with flash(0.25, 0, 0.75, "#fff")
        mc"SON OF A BITCH!!" with vpunch
        show sc morningafter m10
        mc"(What the hell am I going to do??)"
        show sc morningafter m11
        mc"(Those girls will be long gone by now.)"
        mc"(I don't think they would have been stupid enough to use their actual names when checking in.)"
        show sc morningafter m08
        mc"(And they probably weren't even flight attendants.)"
        show sc morningafter m07
        mc"(I'll have to keep my eyes peeled in case we see them again in the future.)"
        $ task_addpoi("Mikayla & Tasha - Girls at the Eager Beaver club",5)
        show sc morningafter m11
        mc"(I think there's only one thing I can do.)"
        mc"(I'm going to have to make a run for it.)"
        #the MC looks at the bedsheets
        show sc morningafter m07
        mc"(And I'll take a bath towel with me.)"
        show sc morningafter m11
        mc"(I'll need to take the stairs down to reception and then dash right out of the front entrance.)"
        mc"(While trying to to avoid the security cameras...)"
        #show cross-fade
        #Proceeds to a scene where the MC running out of the hotel front entrance
        show sc morningafter m59
        with flash(0.25, 0, 0.25, "#fff")
        play sound "sound effects/01/man_yelling1.mp3" noloop
        play sound2 "sound effects/01/barefoot_running_loop.ogg" loop
        mc"Ahhhh! {w=1.0}{nw}"
        scene black
        with dissolve
        scene black
        with Pause (2)
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        with Pause (2)
        #Show the MC running through reception with the bedsheets around him while the receptionist stares with eyes wide open
        #cross screen fade
        #show the MC in the early morning running past peoples' yards - holding the bed sheet around his naked body, running all the way home

        #animated montage scene of him running - with the background changing while he runs

        #he stops at a cross street
        play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
        play sound "sound effects/01/barefoot_running_loop.ogg" loop
        show sc morningafter m60
        with dissolve
        mc"(I'm almost there.)"
        show sc morningafter m27
        mc"(I haven't seen a single person since I left the hotel.)"
        show sc morningafter m28
        mc"(Which is pretty lucky.)"
        #The MC turns sees a middle-aged woman walking a dog, who sees him standing on the sidewalk with the bedsheets around his body. She just stares at him
        show sc morningafter m29
        mc"(Uh-oh! I spoke too soon!)"
        show sc morningafter m30
        "Oh my God!"
        show sc morningafter m31
        mc"What? Haven't you ever seen a guy with a towel around his naked body in broad daylight before?"
        #The lady gives him a strange look
        show sc morningafter m32
        mc"(I better get out of here before she calls the cops and I get arrested for indecent exposure!)"
        stop ambient fadeout 1.0
        stop sound fadeout 1.0
        #Show a behind shot of the MC running a different way and we can see his butt not hidden by the sheets
        #screen goes blank
        scene black
        with dissolve
        scene black
        with Pause (2)
        #GO DOWN TO > #scene continues
    #scene continues
    #The MC sneaks in through the front door of the house
    show sc morningafter m34
    with dissolve
    mc"(It's pretty quiet. Everyone must be still asleep.)"
    mc"(Now to carefully sneak upstairs and-)"
    #The MC runs into Vivian
    show sc morningafter m33
    with vpunch
    v"[y_name]!"
    #she looks down at the bedsheet around his body
    show sc morningafter m41
    v"What on earth happened?"
    show sc morningafter m36
    mc"Um... It's kind of a long story."
    #Bella enters the scene and sees the MC with the bedsheet
    play sound "sound effects/01/sexy_female_laugh3.mp3"
    show sc morningafter m42
    b"Hahaha!"
    stop sound fadeout 1.0
    show sc morningafter m61
    b"Who the hell are you meant to be?"
    b"Julius Caesar?"
    show sc morningafter m38
    mc"Fine... Get your jokes in."
    #Bella mocks the MC - https://img.gifglobe.com/grabs/montypython/MontyPythonsLifeOfBrian/gif/5v3ntz1IIGO8.gif
    show sc morningafter m44
    b"Hail, Caesar!"
    #Ariel enters the scene and sees the MC with the bedsheet
    show sc morningafter m62
    a"Oh my God!"
    a"Are you naked under there, [y_name]?"
    show sc morningafter m63
    mc"Can I please just go to my room so I can put some goddamn pants on?!"
    show sc morningafter m45
    v"Girls, please go into the other room."
    v"I need to speak with [y_name]."
    v"And not a word about this to [vic_name]."
    show sc morningafter m47
    b"Aww... But I was just getting warmed up."
    show sc morningafter m46
    v"Now!"
    show sc morningafter m47
    b"Ugh... Fine."
    show sc morningafter m48
    b"Make sure to wash your grapes very thoroughly, [y_name]."
    play sound "sound effects/01/sexy_female_laugh2.mp3"
    b"Haha!"
    menu:
        "Bite back":
            mc"(No, I better not. It won't make this situation any less embarrassing.)"
        "Say nothing":
            pause 1.0
    stop sound fadeout 1.0
    show sc morningafter m49
    mc"(I'm never going to be able to live this one down.)"
    #Bella and Ariel leave the room
    show sc morningafter m54
    mc"Is he here?"
    show sc morningafter m56b
    v"No, you're lucky that he went out this morning for a jog."
    show sc morningafter m52
    v"And don't worry, I'll make sure he doesn't find out about this."
    show sc morningafter m50
    v"But he could be back any minute."
    show sc morningafter m53
    v"However, I want you to explain to me what happened after you've changed."
    show sc morningafter m51
    mc"Sure thing, [mc_v_address]."
    show sc morningafter m56b
    mc"I'm gonna go upstairs now."
    show sc morningafter m55
    mc"Thanks for understanding."
    show sc morningafter m56a
    v"You're welcome..."
    show sc morningafter m57
    v"(What kind of trouble did my [mc_v_rel] get himself into this time??)"
    #Vivian smiles and has her arms folded
    #The MC goes up the stairs and Vivian watches him leave

    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_the_group_meeting1

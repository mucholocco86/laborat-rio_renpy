label lb_ep01_group_meeting_home:
    $ quick_menu = True
    show screen toh_main_game_screen
    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    scene sc grouphouse f01
    with dissolve
    vic"What do you mean you lost it?? How the fuck did you lose it??"
    stop ambient fadeout 1.0
    show sc grouphouse f02
    mc"I honestly have no idea... I put it inside my pocket and then the next thing I knew, it was gone."
    show sc grouphouse f03
    a"Maybe someone stole it from you?"
    show sc grouphouse f15
    v"But who would do that?"
    scene sc grouphouse f07
    mc"Oh shit!"
    #show a flashback from the party scene"

    #"This scene if the player selected to dance with Vivian/mom"
    if v_ep01_mansionhall_vivian:
        show sc mansionoutside o156
        with flash(0.25, 0, 0.75, "#fff")
        pause 0.5
        show sc mansionoutside o157
        pause 1.0
        scene sc mansionoutside o34
        with vpunch
        mc"UHH!"
        #the MC turns and bumps face-to-face into an anonymous girl and the MC hits the floor"
        show sc mansionoutside o38
        pretty_g"Oh my God, are you okay?"
        show sc mansionoutside o44
        mc"Yeah, I'm fine. Sorry, I didn't see you there."
        #the MC looks up and sees the anonymous girl - POV shot from the floor"
        show sc mansionoutside o39
        pretty_g"It's okay, mistakes happen."
        #screen flashes back to the scene at home"
        scene sc grouphouse f08
        with flash(0.25, 0, 0.75, "#fff")
        mc"I think I know who took it."
        show sc grouphouse f06
        mc"The girl at the party."
        mc"The one I ran into after the alarm went off."
    else:
        #"This scene if the player if the player selected to dance with the anonymous girl"
        #anonymous girl leans in close to his ear, her hands on his chest"
        show sc mansionhall h114
        with flash(0.25, 0, 0.75, "#fff")
        pause 0.5
        show sc mansionhall h115
        pause 1.0
        show sc mansionhall h90
        with dissolve
        pretty_g"Thank you for the dance."
        pretty_g"Maybe we'll bump into each other again soon."
        pretty_g"Bye."
        #anonymous girl walks away"
        #screen flashes back to the scene at home"
        scene sc grouphouse f08
        with flash(0.25, 0, 0.75, "#fff")
        mc"I think I know who took it."
        show sc grouphouse f06
        mc"The girl at the party. The one I was dancing with."

    #(scene continues)
    show sc grouphouse f05
    mc"She must have swiped it without me knowing."
    show sc grouphouse f09
    b"Typical..."
    show sc grouphouse f10
    b"This is why you should have let me take the lead on that job."
    #older sis turns to the father as she says this line above
    show sc grouphouse f11
    vic"Quiet [b_name]. I'm trying to think."
    #mother approaches Victor"
    show sc grouphouse f15
    v"How could she have known that [y_name] even had the flash drive?"
    show sc grouphouse f14
    vic"My guess is that she's also a thief. And she knew what we were doing right from the start."
    vic"She must've tracked [y_name] as soon as he entered the house and then waited for the right time to make her move."
    show sc grouphouse f12
    vic"Which suggests that she is very well versed at this."
    show sc grouphouse f13
    #Victor looks at the window, pondering his thoughts"
    vic"Hmm..."
    show sc grouphouse f14
    vic"There's every chance that she was also in disguise, which further complicates things."
    show sc grouphouse f15
    v"Do you think she was working alone?"
    show sc grouphouse f12
    vic"I can't say for certain, yet."
    vic"I'll need to check my sources to see if there's another gang in town who may have been planning to hit that house as well."
    show sc grouphouse f14
    vic"But it's best not to assume anything."
    vic"The smartest thing that you can all do is to keep a low profile for now."
    show sc grouphouse f12
    vic"Stick to doing your day jobs until we find more information on this girl."
    show sc grouphouse f21
    #father turns to the MC with a menacing look on his face"
    vic"As for you, [y_name]."
    vic"What you did today was inexcusable."
    show sc grouphouse f16
    vic"Not only did you disobey some of my orders and forget to lock the office door, but you lost the only thing you needed to protect."
    show sc grouphouse f17
    vic"This job could be as good as dead."
    show sc grouphouse f18
    mc"Wait!"
    mc"I remember something. About the girl at the party..."
    if v_ep01_mansionhall_vivian:
        show sc mansionoutside o53
        with flash(0.25, 0, 0.75, "#fff")
    else:
        show sc mansionhall h106
        with flash(0.25, 0, 0.75, "#fff")
    mc"She had a tattoo on her back. It was very distinct, very unique."
    show sc grouphouse f24
    with flash(0.25, 0, 0.75, "#fff")
    v"Do you think you could describe what it looks like?"
    show sc grouphouse f37
    mc"Yes, certainly!"
    show sc grouphouse f25
    v"Well, if [y_name] can remember the details, then [b_name] might be able to draw and also recognise it."
    v"It is kind of your speciality, right?"
    #older sis has her arms folded and mutters back"
    show sc grouphouse f26
    b"Yeah, I guess."
    #the MC address his father"
    show sc grouphouse f35
    mc"Just give me some time to retrieve the drive."
    $ task_addpoi("Mystery Girl at the Birthday Party",1)
    show sc grouphouse f37
    mc"I know I can get it back and fix this mess I made."
    show sc grouphouse f22
    vic"[a_name], how long do you estimate that this girl will have the flash drive in her possession?"
    show sc grouphouse f28
    a"Well, presuming that she's working alone, and going by the size of the files and information stored on there..."
    a"I'd say anywhere between forty-eight to seventy-two hours."
    show sc grouphouse f39
    mc"What happens after that time is up?"
    show sc grouphouse f03
    a"She'll either be able to crack the encrypted code that I personally stored onto that drive, or, she'll sell it to someone else."
    a"Most likely on the black market."
    show sc grouphouse f28
    a"If this girl is smart, then she stole it with the intention to make money as soon as possible."
    show sc grouphouse f29
    b"So in other words, we're completely fucked then?"
    #Victor addresses the MC"
    show sc grouphouse f16
    vic"You know, I should be kicking you out of the [private_group] right now."
    vic"Or at the very least, standing you down from leading any future heists or scams."
    show sc grouphouse f21
    vic"Especially for this next big job that I have in mind."
    show sc grouphouse f15
    v"[vic_name], please..."
    #the mom pleads with him to reconsider"
    show sc grouphouse f13
    vic"Hmm..."
    vic"(The boy knows too much.)"
    show sc grouphouse f38
    vic"(If I get rid of him entirely, then he could drop us all in it if he wanted to.)"
    vic"(Then again, I could always pin one of our previous robberies on him without [y_name] even knowing.)"
    show sc grouphouse f21
    vic"Okay, I've come to a decision..."
    show sc grouphouse f16
    vic"I'm going to give you seventy-two hours to get that flash drive back."
    #victor addresses the older sister"
    show sc grouphouse f22
    vic"[b_name], once [y_name] draws the image of the tattoo he saw on that girl, I want the two of you to check out all the local tattoo parlours."
    show sc grouphouse f30
    b"We won't be able to do that tonight. There are only three parlours in town and they'd all be closed by now."
    show sc grouphouse f10
    b"We'll have to go tomorrow after they open. But I have to work in the morning."
    #victor addresses the MC and older sister"
    show sc grouphouse f22
    vic"Fine. You two can meet up after you finish and before [y_name] starts his shift at the gym."
    show sc grouphouse f28
    a"I'll monitor all the sites that I can think of, just in case that flash drive pops up for sale."
    show sc grouphouse f24
    v"And I'll talk with Mrs. Walker to see if I can get a copy of the guest list from today's party."
    show sc grouphouse f25
    v"This girl could be on it, or perhaps she was using an alias that we might recognise."
    show sc grouphouse f22
    vic"Very good."
    show sc grouphouse f29
    b"Uhhh! This is a complete waste of time."
    show sc grouphouse f22
    vic"I'll be the judge of that. So enough with the pouting and do what you're told, [b_name]."
    show sc grouphouse f31
    b"Hmphh!"
    show sc grouphouse f12
    vic"Now that you have a new task, I suggest that you all get a good night's rest and wake up fresh tomorrow morning."
    $ task_addnew("Find out more details about the girls tattoo",2)
    show sc grouphouse f15
    v"Of course."
    show sc grouphouse f22
    vic"Girls, I need a moment with [y_name], alone."
    show sc grouphouse f15
    v"Go easy on him, [vic_name]."
    v"We all make mistakes. Even you."
    show sc grouphouse f23
    vic"Hmm..."
    show sc grouphouse f25
    v"Come on..."
    show sc grouphouse f32
    with dissolve
    v"Let's leave them be, girls."
    #mom looks at the MC concerned and then leaves the room"
    #the girls all leave the room
    #victor addresses the MC"
    show sc grouphouse f21
    vic"I'll cut to the chase."
    show sc grouphouse f16
    vic"This is your final chance. Don't make me regret this."
    show sc grouphouse f37
    mc"You won't, [mc_vic_address]."
    show sc grouphouse f21
    vic"Fine... And don't stay up too late."
    show sc grouphouse f37
    mc"What exactly is on that drive, anyway? Why is it so important?"
    show sc grouphouse f21
    vic"It's important because it's a project I've been working on for the past three months."
    vic"The information on there is worth millions."
    show sc grouphouse f38
    mc"(Damn... No wonder he's pissed at me for losing it.)"
    # maybe have MC say this out loud? and then victor reacts accordingly?
    show sc grouphouse f22
    vic"Err, anyway..."
    show sc grouphouse f16
    vic"The contents of the drive is none of your concern, [y_name]."
    show sc grouphouse f35
    mc"Look, I know I royally screwed up... but that doesn't mean that I'm completely ignorant to understand the severity of where this leaves us."
    show sc grouphouse f37
    mc"Not that you haven't done anything wrong before, have you?"
    show sc grouphouse f38
    vic"That's beside the point."
    show sc grouphouse f21
    vic"I've been preparing you for today for several years and you let me down."
    vic"You let everyone down."
    show sc grouphouse f34
    vic"And I don't appreciate the tone."
    show sc grouphouse f21
    vic"You have one job... Get that damn drive back."
    $ task_addfuturetask("Find the flashdrive",1)
    show sc grouphouse f16
    vic"And don't you dare disobey me ever again, otherwise, there will be consequences."
    show sc grouphouse f36
    vic"Do you understand?"
    show sc grouphouse f37
    mc"Yeah..."
    show sc grouphouse f38
    mc"(Whatever...)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    #the MC leaves the room and Victor has an unsure look on his face"

    #(screen goes blank)
    show sc grouphouse f40
    with dissolve
    mc"(Damn... That could have gone so much worse.)"
    mc"(I thought for sure he was going to go a lot more ballistic.)"
    # or  mc"(I thought for sure he was going to tear me a new one.)"
    show sc grouphouse f36
    mc"(I'm just sick and tired of him criticising all of us.)"
    mc"(However, I should also count myself lucky that I still have the opportunity to rectify this situation.)"
    mc"(I know that [mc_v_address] and [a_name] have my back, but [b_name] would love nothing more than to see me fall flat on my face.)"
    show sc grouphouse f38
    mc"(Either way, we have to work together.)"
    show sc grouphouse f40
    mc"(Maybe I can talk with each of them before they go to bed.)"
    mc"(I'll do that after I've had something to eat and had a shower...)"
    $ quick_menu = False
    #screen goes blank
    hide screen toh_main_game_screen
    scene black
    with dissolve
    scene black
    with Pause (2)
    if persistent.v_anim_enabled:
        scene anim_ep01_Cat_tattoo:
            size (config.screen_width, config.screen_height)
        pause 7.0
    else:
        show ep01 cat tattoo
        with dissolve
        pause 3.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_girls_rooms

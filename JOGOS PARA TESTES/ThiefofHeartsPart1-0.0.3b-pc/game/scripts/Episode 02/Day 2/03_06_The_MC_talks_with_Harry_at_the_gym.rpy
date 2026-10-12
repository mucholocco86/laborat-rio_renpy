label lb_ep02_03_06_The_MC_talks_with_Harry_at_the_gym:
    #SCENE BEGINS
    #show the MC back out to the gym. He's looking over the gym equipment while a couple of gym junkies train near them
    #gym ambience
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
    scene sc gymboss g38
    with dissolve
    ha"Hey, dude. How did it go?"
    #Harry acknowledges the MC
    show sc gymboss g39
    mc"Not good..."
    #show Harry with his mouth closed
    mc"The gym was robbed overnight."
    #reuse the same render as above
    show sc gymboss g40
    ha"Yeah, so I heard."
    #reuse the same render as above
    show sc gymboss g38
    ha"So what did he want to speak to you about?"
    #a slightly different expression from Harry here
    show sc gymboss g45
    mc"(I won't tell Harry about having my passkey card stolen. It will just lead to more questions.)"
    #Show Harry staring at MC thinks about his reply
    show sc gymboss g44
    mc"Nothing much. He just wanted to see if I had any information that might be useful."
    #reuse the same render as above
    show sc gymboss g49
    mc"Have you seen the recordings from the security cameras?"
    #reuse the same render as above
    show sc gymboss g38
    ha"No, he wouldn't show it to me."
    #Harry looks disappointed, slightly open mouth
    ha"What was on it?"
    #Same image as above except e raises one hand
    show sc gymboss g52
    mc"Just some footage of the perpetrators taking money from the till."
    #reuse the same render as above
    show sc gymboss g48
    mc"They were in disguise and had masks covering their faces. So they could have been anyone."
    #reuse the same render as above
    show sc gymboss g38
    ha"I see."
    #reuse the same render as above

    #These lines if the player slept with just Mikayla
    if v_ep01_09_01_Mikayla_Sex_path == True:
        show sc gymboss g40
        ha"What a week..."
        #reuse the same render as above
        show sc gymboss g05
        ha"First we get robbed by those two girls and then we come back to work and the gym is robbed!"
        #Harry throws both hands/arms up
        show sc gymboss g07
        ha"Not to mention all the shit that happened to you last week."
        #reuse the same render as above
        show sc gymboss g54
        mc"Yeah, don't remind me."
        #Harry stands there with his hands on his hips and mouth closed
        show sc gymboss g05
        ha"It's a shame we can't do anything about either situation."
        #reuse the same render as above
        show sc gymboss g51
        mc"(Oh, we'll just see about that.)"
        #The MC thinks like he's on a mission
        show sc gymboss g45
        mc"(If they were here last night, then those girls might still be somewhere in town.)"
        #reuse the same render as above

    #These lines if the player slept with just Tasha
    if v_ep01_09_01_Tasha_Sex_path == True:
        show sc gymboss g40
        ha"What a week..."
        #reuse the same render as above
        show sc gymboss g05
        ha"First we get robbed by those two girls and then we come back to work and the gym is robbed!"
        #Harry throws both hands/arms up
        show sc gymboss g07
        ha"Not to mention all the shit that happened to you last week."
        #reuse the same render as above
        show sc gymboss g54
        mc"Yeah, don't remind me."
        #Harry stands there with his hands on his hips and mouth closed
        show sc gymboss g05
        ha"It's a shame we can't do anything about either situation."
        #reuse the same render as above
        show sc gymboss g51
        mc"(Oh, we'll just see about that.)"
        #The MC thinks like he's on a mission
        show sc gymboss g45
        mc"(If they were here last night, then those girls might still be somewhere in town.)"
        #reuse the same render as above

    #These lines if the player slept with both Mikayla and Tasha (threesome path)"
    if v_ep01_09_01_Tasha_and_Mikayla_Sex_path == True:
        show sc gymboss g40
        ha"What a week..."
        #reuse the same render as above
        show sc gymboss g05
        ha"It's a shame we can't do anything about it though."
        #reuse the same render as above
        show sc gymboss g51
        mc"(Oh, we'll just see about that.)"
        #The MC thinks  like he's on a mission
        show sc gymboss g45
        mc"(If they were here last night, then those girls might still be somewhere in town.)"
        #reuse the same render as above
        show sc gymboss g05
        ha"By the way..."
        #reuse the same render as above
        show sc gymboss g07
        ha"What happened the other night?"
        #reuse the same render as above
        show sc gymboss g55
        mc"Um... What do you mean?"
        #reuse the same render as above
        show sc gymboss g38
        ha"I uh... I didn't embarrass myself in front of Mikayla, did I?"
        #Harry looks worried here
        show sc gymboss g56
        mc"No, why would you think that?"
        #reuse the same render as above
        show sc gymboss g05
        ha"I had a lot to drink as you probably noticed..."
        show sc gymboss g07
        ha"...and I'm not even sure how I got home!"
        #reuse the same render as above
        show sc gymboss g52
        mc"I had to put you in a cab, buddy. You were pretty wasted."
        #reuse the same render as above
        show sc gymboss g56
        mc"You could barely stand on your feet. So you left me with no option."
        #reuse the same render as above
        show sc gymboss g05
        ha"Oh... Thanks."
        #reuse the same render as above
        show sc gymboss g40
        ha"I had one nasty hangover the next morning."
        #reuse the same render as above
        show sc gymboss g07
        ha"So what happened after I left?"
        #reuse the same render as above
        show sc gymboss g06
        mc"Oh, not much."
        #reuse the same render as above
        show sc gymboss g05
        ha"Don't hold out on me, [y_name]."
        #Harry looks at him with intent
        show sc gymboss g03
        ha"You had two fine-looking flight attendants all to yourself."
        #reuse the same render as above
        show sc gymboss g07
        ha"Something must have happened."
        #reuse the same render as above
        show sc gymboss g46
        ha"So I want details, I want them... NOW!"
        #Harry looks demanding
        show sc gymboss g47
        mc"(Ah, geez...)"
        #reuse the same render as above
        show sc gymboss g48
        mc"Fine..."
        show sc gymboss g55
        mc"I ended up going with the girls back to their hotel apartment, and we um..."
        show sc gymboss g56
        mc"Well, you know?"
        #reuse the same render as above
        show sc gymboss g38
        ha"No, I don't."
        #Harry looks confused
        show sc gymboss g49
        mc"Do I have to spell it out for you, Harry?"
        show sc gymboss g56
        mc"I had several hours of amazing sex with both Mikayla and Tasha!!"
        #Harry looks at an excited MC, and he's mad at him
        show sc gymboss g05
        ha"Do you really expect me to believe that?"
        #Harry stands there with his hands on his hips
        show sc gymboss g44
        mc"Huh?"
        #the MC looks confused
        show sc gymboss g03
        ha"I know I was drunk the other night and I missed my shot with Mikayla, but there's no need to lie and make fun of me!"
        #Harry is not impressed
        show sc gymboss g02
        mc"But Harry, I-"
        #Harry folds his arms and has his mouth closed
        show sc gymboss g05
        ha"Yeah, yeah... I heard you."
        #he still has his arms folded but glances his eyes to the left when he responds to the MC
        show sc gymboss g07
        ha"You had a threesome with two flight attendants."
        #reuse the same render as above
        show sc gymboss g42
        ha"And last night I got a dual titfuck from Sweeney and Daddario!"
        #reuse the same render as above
        show sc gymboss g35
        ha"And I'm betting that this time you have absolutely no proof."
        #he points at the MC
        show sc gymboss g36
        mc"(Well, I tried to be honest with him.)"
        #the MC sneers and looks away from Harry
        show sc gymboss g52
        mc"All right..."
        #reuse the same render as above
        show sc gymboss g53
        mc"You got me..."
        #the MC holds his hands up like this - https://www.theodysseyonline.com/media-library/breaking-bad-oops-gif.gif?id=23508370&width=764&quality=80
        show sc gymboss g35
        ha"You can't put anything past this guy, [y_name]."
        #Harry points at himself
        show sc gymboss g42
        ha"Threesome... Haha! You almost had me going for a minute there, [y_name]!"

    #scene continues
    show sc gymboss g35
    ha"So what have you got on today?"
    #Harry smiling again as he speaks to the MC
    show sc gymboss g52
    mc"I have a couple of solo sessions booked in, and then we have that yoga workout class coming in later on."
    #reuse the same render as above
    show sc gymboss g05
    ha"Ah, of course."
    #reuse the same render as above
    show sc gymboss g38
    ha"You also sent some stray in to speak with me the other day."
    #Harry looking cocky here
    show sc gymboss g37
    ha"What was her name?"
    #Harry thinking face while speaking
    ha"Cora? Laura?"
    #Harry looks confused, trying to think of her name
    mc"Zora."
    #the answer comes to mind for Harry
    show sc gymboss g35
    ha"That's her!"
    #he looks surprised
    show sc gymboss g45
    ha"Looks like you'll have a mission on your hand whipping her into shape, buddy."
    #reuse the same render as above
    show sc gymboss g49
    mc"That sounds like a challenge."
    #The MC looks confident when speaking
    show sc gymboss g42
    ha"Yeah, good luck with that."
    #reuse the same render as above
    show sc gymboss g52
    mc"Asshole..."
    #the MC shoots Harry and snide look
    show sc gymboss g05
    ha"You also have a session with that girl who was here last week, yeah?"
    #reuse the same render as above
    show sc gymboss g52
    mc"I do, with Juliet."
    #reuse the same render as above
    show sc gymboss g35
    ha"Now that's a girl you should be putting all your time and effort into. Among other things."
    #reuse the same render as above
    show sc gymboss g54
    mc"Just don't make a fool of yourself again when she gets here."
    #reuse the same render as above
    show sc gymboss g38
    ha"What time is your session with her?"
    #reuse the same render as above
    show sc gymboss g48
    mc"I'll have to go double-check our bookings. I know it's soon, but I'm not sure of the exact time."
    #reuse the same render as above
    show sc gymboss g52
    mc"And before I forget, the boss wanted me to tell you that he's made edits to next week's roster."
    #reuse the same render as above
    show sc gymboss g38
    ha"Great..."
    show sc gymboss g35
    ha"Okay, while you're checking out your bookings, I'll be in the bathrooms cleaning out the crappers!"
    #reuse the same render as above
    show sc gymboss g56
    mc"Good luck with that. Happy snorkelling!"
    #reuse the same render as above
    show sc gymboss g35
    ha"Yeah, yeah... Thanks a lot, smartass!"
    #shot of Harry walking away while the MC watches him leave for the bathroom
    #(screen goes blank)
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_07_Zora_arrives_at_the_gym

label lb_ep01_The_MC_gets_his_bike_back:
    #The scene begins with the MC waiting outside his house for the car to arrive - an evening setting
    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    scene sc meganhouse m01
    with dissolve
    mc"(Hmm...)"
    play sound "sound effects/01/car_arriving.ogg"
    $ ui.timer(9.3, Play("sound2", "sound effects/01/car_idle_loop.ogg", loop=True))
    mc"(The car should be here any moment now.)"
    #The limo pulls up - https://www.daz3d.com/royal-luxury-limousine
    show sc meganhouse m02
    mc"(Woah...)"
    #The driver puts his window down - he looks like an older gentleman
    show sc meganhouse m05
    driver"Are you [y_name]?"
    stop sound fadeout 1.0
    show sc meganhouse m03
    mc"Uh, yeah. That would be me."
    show sc meganhouse m06
    driver"Very good."
    niles"I'm Niles, m'ladies head chauffeur."
    show sc meganhouse m07
    niles"Allow me to get the door for you."
    #The driver goes to exit the driver's seat
    show sc meganhouse m04
    mc"No need. I got this, pops."
    #The MC opens the backseat door and lets himself
    show sc meganhouse m09
    niles"Hmm..."
    #Show the MC in the backseat of the limo
    show sc meganhouse m08
    mc"Damn... I'll never get tired of hopping into the backseat of a limo."
    stop ambient fadeout 1.0
    stop sound2 fadeout 1.0
    play music "sound effects/01/Road Trip Dreams.mp3" loop fadein 1.0
    play ambient2 "sound effects/01/car_interior_ambience.ogg" loop fadein 1.0
    show sc meganhouse m07b
    with dissolve
    niles"I imagine this will be a real treat for you."
    #The driver takes off
    show sc meganhouse m20
    mc"It certainly is!"
    show sc meganhouse m18
    mc"So you're Megan's personal driver?"
    show sc meganhouse m10
    niles"I'm one of her personal drivers. She has a few."
    show sc meganhouse m17
    mc"(Damn, who is this woman?)"
    show sc meganhouse m20
    mc"Sorry, I didn't get your name."
    show sc meganhouse m11
    niles"The name is Littamen."
    show sc meganhouse m18
    mc"Pleasure to meet you."
    show sc meganhouse m20
    mc"So what can you tell me about Megan?"
    show sc meganhouse m11
    niles"I'm sure she would prefer you to ask her yourself."
    show sc meganhouse m22
    niles"I recommend you enjoy the ride while it lasts, young man."
    show sc meganhouse m13
    niles"And help yourself to something to eat and drink."
    #the driver puts up the window between them - https://media2.giphy.com/media/l2Je1Ls2AGy3S5CgM/200w.gif?cid=6c09b9522k48gvmy28fpq5sz4miva3ot9sjch48wm85iujws&ep=v1_gifs_search&rid=200w.gif&ct=g
    show sc meganhouse m23
    mc"(Hmm... Not the chatty type then.)"
    show sc meganhouse m17
    mc"(He could be right though.)"
    show sc meganhouse m24
    mc"(Who knows when I'll be in the back of a limo again?)"
    #The MC finds a bottle of liquor and pours himself a drink
    show sc meganhouse m21
    mc"(Ah... Jackpot!)"
    show sc meganhouse m15
    with dissolve
    mc"Mmm..."
    show sc meganhouse m26
    mc"(This is already turning out to be a great night...)"
    stop ambient2 fadeout 1.0
    stop music fadeout 1.0
    #Show an outside shot of the limo driving down a street at night
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #The car drives up towards Megan's mansion - https://www.daz3d.com/antebellum-mansion
    play ambient "sound effects/01/car_interior_ambience.ogg" loop fadein 1.0
    show sc meganhouse m29
    with dissolve
    mc"(Oh my God... This is her house?)"
    show sc meganhouse m28
    mc"(It can't be.)"
    #The limo pulls up at the front of the house and the MC sees his bike parked out the front
    stop ambient fadeout 1.0
    play ambient2 "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    show sc meganhouse m30
    with dissolve
    mc"(What the hell have I walked into?)"
    #The limo driver comes around to open the MC's door. Two security guys stand at her front door
    play sound "sound effects/01/car_door_opening.mp3"
    show sc meganhouse m32
    niles"Welcome to the the residence of Miss Megan."
    stop sound fadeout 1.0
    show sc meganhouse m31
    mc"Thanks, Littamen."
    #security approaches the MC
    show sc meganhouse m33
    security"Please put your arms out, Sir."
    show sc meganhouse m35
    mc"Huh?"
    show sc meganhouse m34
    security"Miss Megan requests all of her guests be screened before entering her home."
    show sc meganhouse m35
    mc"Oh, fair enough."
    show sc meganhouse m36
    mc"Lot of robberies and nut jobs in town, right?"
    #The drive gives the MC a straight-faced look
    show sc meganhouse m37
    niles"..."
    show sc meganhouse m38
    mc"All righty, then."
    menu:
        "Make a joke"(wt="Best option"):
            #The MC stands with his arms spread and the member of security waves a wand over his arms
            mc"(I should try and pick up the mood.)"
            #The security waves his wand between the MC's legs
            show sc meganhouse m39
            mc"Woah... Easy now."
            mc"I can assure you that the crown jewels aren't down there."
            show sc meganhouse m38
            mc"Or maybe they are?"
            #The security smirks at the MC
            show sc meganhouse m40
            security"..."
            mc"(Hmm... If things get any livelier around here a funeral's gonna break out!)"
        "Stay quiet":
            pause 2.0


    show sc meganhouse m41
    with dissolve
    security"You're good to go."
    show sc meganhouse m42
    niles"Please make your way inside. Miss Megan will be in the living room."
    show sc meganhouse m43
    mc"Thanks, pops."
    #The MC walks up to the front door and enters the house
    show sc meganhouse m44
    mc"(Geez... I bet this place is even more incredible on the inside.)"
    pause 1.5
    #The MC sees the living room on his left and then looks at the clothes he's wearing
    stop ambient2 fadeout 1.0
    play sound "sound effects/01/door_close_soft.mp3"
    show sc meganhouse m71
    with dissolve
    mc"Wow..."
    stop sound fadeout 1.0
    show sc meganhouse m72
    mc"(This area alone is bigger than my room!)"
    show sc meganhouse m73
    mc"(You could drive a semi-trailer through here.)"
    mc"(I wonder if this is the living room up here on the left.)"
    play music "sound effects/01/Midday_Mischief_with_Vivian.mp3" loop fadein 1.0
    show sc meganhouse m74
    mc"Hello?"
    #Megan calls out to the MC from behind
    show sc meganhouse m47
    megan"There you are..."
    #He turns around, she looks glamorous, in her night robe, which leaves nothing to the imagination
    #She shows some leg - https://pixhost.to/show/1192/449034373_screenshot-2024-02-26-at-10-00-54-pm.jpg
    #https://pixhost.to/show/1192/449034383_screenshot-2024-02-26-at-10-00-58-pm.jpg
    #https://pixhost.to/show/1192/449034393_screenshot-2024-02-26-at-10-01-02-pm.jpg
    show sc meganhouse m46
    mc"Woah..."
    #ROLLING SCREEN of Megan - https://pixhost.to/show/1191/449032891_megan_out.jpg
    show sc meganhouse m47
    megan"I'm so glad that you could make it, [y_name]."
    show sc meganhouse m46
    megan"And at such short notice."
    mc"Uh... No problem."
    #Megan kisses the MC on the cheek
    play sound "sound effects/01/mwah_short_kissing_sound_effect1.mp3"
    show sc meganhouse m48
    megan"Mwah!"
    #Megan kisses the MC on the other cheek
    play sound2 "sound effects/01/mwah_short_kissing_sound_effect3.mp3"
    show sc meganhouse m49
    megan"Mwah!"
    mc"(Oh! She seems very happy to see me.)"
    #Megan shows the MC where he can sit
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc meganhouse m75
    mc"This is some place you have here, Megan."
    megan"Thanks."
    show sc meganhouse m76
    megan"Please, make yourself comfortable while I fix myself a drink."
    #The driver pops up behind the MC
    show sc meganhouse m77
    niles"Will that be all for tonight, ma'am?"
    #The MC is shocked to see the driver standing right behind
    show sc meganhouse m78
    with hpunch
    mc"Holy crap!"
    show sc meganhouse m79
    mc"Where did you come from??"
    show sc meganhouse m81
    niles"I am very sneaky, Sir."
    show sc meganhouse m80
    mc"Yeah... Like a thief in the night."
    #The MC puts a hand on his chest
    show sc meganhouse m82
    mc"(Damn... Out of me and the old man, I'm the one more likely to have a heart attack!)"
    show sc meganhouse m83
    megan"Thank you, Littamen. That will be all."
    show sc meganhouse m84
    driver"Very good. Have a pleasant evening, ma'am."
    #The driver leaves and Megan stands at a bar pouring a drink
    show sc meganhouse m85
    mc"He seems very attentive."
    show sc meganhouse m86
    megan"He certainly is. And also one of the most reliable chauffeurs I've ever had."
    show sc meganhouse m87
    megan"Something to drink?"
    show sc meganhouse m85
    mc"Nah, I'm good."
    mc"I had one on the drive over, and the last I need is to get picked up for being drunk while riding a bicycle!"
    show sc meganhouse m86
    megan"Yes, of course."
    show sc meganhouse m60
    mc"Speaking of which, I saw my bike parked out the front."
    show sc meganhouse m64
    mc"Thanks again for finding it."
    show sc meganhouse m110
    megan"It was my pleasure."
    #Megan walls back towards where the MC sits
    show sc meganhouse m112
    mc"I have to know... Where did you find it?"
    mc"And how did you manage to recover it so quickly?"
    #She sits on the sofa opposite the MC
    show sc meganhouse m110
    megan"So many questions..."
    show sc meganhouse m56
    megan"Let's just say that I have some friends in very high places."
    show sc meganhouse m53
    megan"They're my eyes and ears, twenty-four hours a day."
    show sc meganhouse m54
    megan"They could pick up a microfilm hidden in a hollowed-out book. They're that thorough."
    megan"But trust me when I say that not knowing every little detail is for the best."
    show sc meganhouse m64
    mc"Well, again, I really appreciate it."
    show sc meganhouse m110
    megan"So I bet you didn't expect to hear from me again so soon after our chance meeting yesterday, huh?"
    show sc meganhouse m113
    mc"No, definitely not."
    show sc meganhouse m110
    megan"But you're glad that you did, right?"
    #Megan crosses her legs after this line above
    show sc meganhouse m113
    mc"Yes... Very much so."

    #[Check out her legs / Smile back / Another option]

    #A bonus render for each option will be added to her gallery - it gives the player a reason to check each option
    menu:
        "Check out her legs"(wt="Better option"):
            #The MC zeros in on her legs
            show sc meganhouse m67
            mc"(Those legs of hers are look like sleek pillars of marble.)"
            show sc meganhouse m69
            mc"(They make me want to tear off her robe and do naughty things to her.)"
            mc"(At least for a few seconds before her goons rush in here and pummel the shit out of me!)"
            $ rewards_unlock ("megan",4)
            show sc meganhouse m52
            megan"(He thinks he's being discreet by checking out my legs.)"
            show sc meganhouse m54
            megan"(I can't say I blame him though, being a young man seeing me dressed like this.)"
            $ v_ep01_megan_cocky_counter += 1

            #ONE BONUS RENDER OF MEGAN (IN HER ROBE) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
        "Smile back":
            #The MC zeros in on her face/smile
            show sc meganhouse m65
            mc"(She has a smile that seems very genuine, and incredibly enchanting.)"
            show sc meganhouse m52
            megan"(It's pretty admirable of him to not take sneaking glances, considering the attire I'm wearing tonight.)"
            $ v_ep01_megan_respect_counter += 1

            #ONE BONUS RENDER OF MEGAN (IN HER ROBE) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
        "Check out her breasts"(wt="Better option"):
            #The MC zeros in on her cleavage
            show sc meganhouse m68
            mc"(That cleavage of hers is incredibly distracting... In the most perfect way.)"
            mc"(However, it's like looking at the sun.)"
            show sc meganhouse m66
            mc"(I shouldn't stare for too long.)"
            mc"(Take a quick glance and then look away!)"
            #The MC looks up at her smiling face
            show sc meganhouse m52
            mc"(They make me want to tear off her robe and do naughty things to her.)"
            mc"(At least for a few seconds before her goons rush in here and beat the shit out of me!)"
            $ rewards_unlock ("megan",4)
            show sc meganhouse m50
            megan"(Could he be more obvious?)"
            show sc meganhouse m55
            megan"(He's been here less than five minutes and he's blatantly staring at my chest.)"
            $ v_ep01_megan_arrogant_counter += 1
            #ONE BONUS RENDER OF MEGAN (IN HER ROBE) ADDED TO THE PHOTO GALLERY FOR HER PROFILE

    #scene continues
    show sc meganhouse m51
    megan"So after I meet people for the first time, if they pique my interest, I take it upon myself to learn more about them."
    show sc meganhouse m56
    megan"Tell me something, [y_name]?"
    show sc meganhouse m55
    megan"Did you find it a little ironic that someone would steal your bicycle?"
    show sc meganhouse m58
    mc"Ironic? How do you mean?"
    show sc meganhouse m111
    megan"Well, you can either tell me more about the real you, or I'll do it for you."
    megan"So what's it gonna be?"
    show sc meganhouse m112
    menu:
        "Play dumb":
            show sc meganhouse m63
            mc"I'm not sure what you want me to say, Megan."
            $ v_ep01_megan_arrogant_counter += 1
            show sc meganhouse m54
            megan"Very well then."
            show sc meganhouse m56
            megan"Have you been to any birthday parties recently?"
            #The MC looks stunned
            show sc meganhouse m60
            with vpunch
            mc"(Oh shit... She knows!)"
            mc"(Have we been compromised?)"
            show sc meganhouse m58
            mc"How do you know about that?"
        "Come clean"(wt="Best option"):
            show sc meganhouse m59
            mc"(This woman isn't stupid.)"
            show sc meganhouse m50
            mc"(If she even suspects that I'm lying to her, then I could end up as the next concrete fashion model at the bottom of the river.)"
            # or  mc"(If she even suspects that I'm lying to her, then I could end up with a pair of concrete overshoes in the river.)"
            mc"(The least I could do is be honest with her after she found my bike and gave me a lift to work yesterday.)"
            $ v_ep01_megan_respect_counter += 1
            show sc meganhouse m60
            mc"What gave me away?"
            $ rewards_unlock ("megan",5)
        "Change the subject":
            show sc meganhouse m64
            mc"Well, we could talk about that, Megan..."
            show sc meganhouse m57
            mc"Or we could talk about why you really invited me here?"
            show sc meganhouse m112
            megan"..."
            mc"(Damn, she's serious.)"
            show sc meganhouse m50
            mc"Or perhaps not."
            $ v_ep01_megan_cocky_counter += 1
            show sc meganhouse m60
            mc"So what gave me away?"


    show sc meganhouse m54
    megan"Like I said... I have eyes and ears everywhere."
    #Megan picks up a folder and reads from it
    show sc meganhouse m51
    megan"You managed to make your way into the Walker Family Residence, in disguise, and to also break into the main office."
    show sc meganhouse m56
    megan"My sources tell me that you were looking for something in particular, a file or evidence perhaps, and you weren't working alone."
    show sc meganhouse m54
    megan"Possibly with the people you live with, right?"
    #The MC looks concerned
    show sc meganhouse m60
    mc"Look, Megan... I can explain."
    play sound "sound effects/01/sexy_female_laugh4.mp3"
    show sc meganhouse m53
    megan"Haha!"
    show sc meganhouse m51
    megan"Don't look so worried, [y_name]. I'm not going to rat you out."
    stop sound fadeout 1.0
    show sc meganhouse m52
    mc"You're not?"
    mc"How come?"
    show sc meganhouse m54
    megan"Well, let's just say that I'm not a snitch, and after this development, I've taken a professional interest in you."
    show sc meganhouse m62
    mc"What exactly do you mean by that?"
    show sc meganhouse m54
    megan"I'd like to help you. From what i've seen and been told, you have a lot of potential."
    megan"And at such a young age, you almost pulled off the perfect crime."
    show sc meganhouse m63
    mc"Uhh, thanks?"
    show sc meganhouse m55
    megan"Don't thank me. And I did say, \"almost\"."
    show sc meganhouse m56
    megan"Tell me... What went wrong?"
    show sc meganhouse m60
    mc"With the heist?"
    show sc meganhouse m62
    mc"Well, quite a few things."
    show sc meganhouse m55
    megan"What is it that you were looking for?"
    show sc meganhouse m59
    mc"Hmm..."
    show sc meganhouse m53
    megan"It's okay. You can trust me."
    show sc meganhouse m54
    megan"I mean, I did find your bicycle, didn't I?"
    show sc meganhouse m104
    megan"And the more you tell me..."
    show sc meganhouse m106
    megan"The more I can do for you..."
    mc"(Geez... She's purposely baiting me here.)"
    show sc meganhouse m105
    mc"(But are her intentions for real?)"
    show sc meganhouse m52
    mc"(If she really has eyes and ears everywhere, then Megan could be the kind of person that could help me find that girl from the party.)"
    show sc meganhouse m68
    mc"(But I get the feeling she will know straight away if I'm deceiving her.)"
    show sc meganhouse m69
    mc"(However, I feel like it's worth the risk.)"
    show sc meganhouse m62
    mc"Well, I downloaded some files from the father's main computer."
    mc"Then put them on a flash drive."
    show sc meganhouse m58
    mc"Everything was going fine and it seemed like we planned it all out perfectly."
    mc"But just as I was about to leave, some girl at the party picked my pocket, and took the drive.  I didn't notice it was missing until later."
    show sc meganhouse m56
    megan"What did she look like?"
    show sc meganhouse m64
    mc"Um, she was five foot three, early to mid-twenties, with dark hair, although she may have been wearing a wig."
    show sc meganhouse m60
    mc"But the main thing I noticed was she had a cat-face tattoo on her back."
    mc"We looked into this and supposedly it's an old tattoo for a gang going by the name, {i}Apex Legion{/i}."
    show sc meganhouse m62
    mc"Have you heard of it?"
    show sc meganhouse m51
    megan"No, it doesn't ring a bell. But I can have my people check it out."
    show sc meganhouse m55
    megan"Anything else?"
    show sc meganhouse m63
    mc"No, except, our [public_group] leader has given me until tomorrow night to find it."
    show sc meganhouse m58
    mc"He's pretty pissed that I lost it."
    show sc meganhouse m56
    megan"Well, mistakes happen. It's how we react to them which is the important thing."
    show sc meganhouse m50
    megan"Hmm..."
    show sc meganhouse m51
    megan"Okay, this is what's going to happen."
    megan"I'll help you find this girl and the flash drive."
    show sc meganhouse m56
    megan"In exchange, I want something from you in return."
    show sc meganhouse m58
    mc"Um... Okay. What exactly do you want?"
    show sc meganhouse m54
    megan"All in good time."
    show sc meganhouse m51
    megan"I'll call you tomorrow morning."
    megan"Make sure to answer, and to keep the afternoon free."
    show sc meganhouse m55
    megan"Can I trust you to do that?"
    show sc meganhouse m64
    mc"Yes, you can."
    show sc meganhouse m53
    megan"Great."
    show sc meganhouse m60
    mc"And what about my bike?"
    show sc meganhouse m53
    megan"It's all yours."
    show sc meganhouse m63
    mc"Really? Just like that?"
    show sc meganhouse m54
    megan"Consider it a peace offering. And also to confirm that my intentions for you are noble."
    show sc meganhouse m51
    megan"You help me get what I want, and I'll do likewise when and where I can."
    show sc meganhouse m54
    megan"Do we have a deal?"
    show sc meganhouse m59
    mc"(She's giving me no reason not to trust her.)"
    show sc meganhouse m113
    mc"(I still need to be careful though.)"
    mc"Agreed."
    show sc meganhouse m110
    megan"Great. You've made the right decision."
    megan"I look forward to working {i}very closely{/i} with you."
    show sc meganhouse m111
    megan"Do you have any other questions?"
    show sc meganhouse m63
    mc"Just one..."
    show sc meganhouse m60
    mc"Why are you helping me? It can't be solely because you think I have potential."
    mc"It's just a little hard for me to believe that anyone would be interested in me for \"almost\" doing a job successfully."
    show sc meganhouse m62
    mc"So what's the real reason?"
    show sc meganhouse m54
    megan"All right, I'll be perfectly frank with you, [y_name]."
    show sc meganhouse m51
    megan"It's because I believe you can be trusted. And because I like you."
    show sc meganhouse m53
    megan"I felt like we made a very strong connection when we met yesterday."
    megan"Wouldn't you agree?"
    #Show the MC looking at her cleavage
    show sc meganhouse m64
    mc"Y-yeah... I suppose we did."
    show sc meganhouse m66
    mc"(I could definitely feel some sexual tension between us.)"
    show sc meganhouse m50
    mc"(But maybe that was just me and a certain part of my anatomy that believes that.)"
    show sc meganhouse m51
    megan"A lot of my success and everything I have achieved, everything you see before you, is because I'm a good judge of character."
    megan"I don't request services from just anybody."
    show sc meganhouse m55
    megan"Does that answer your question?"
    show sc meganhouse m57
    mc"Yes, it does."
    show sc meganhouse m53
    megan"Wonderful!"
    #Megan stands
    show sc meganhouse m55
    megan"Anyway, I don't mean to be rude but I do need my beauty sleep."
    show sc meganhouse m85
    mc"Yeah, I should probably get going."
    show sc meganhouse m88
    megan"Allow me to show you out..."
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #They stand outside the front door of her house with a member of security close by
    #Evening sound effects

    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    show sc meganhouse m89
    with dissolve
    mc"Thanks again for finding my bike."
    show sc meganhouse m90
    megan"You're most welcome."
    show sc meganhouse m91
    megan"But do you think saying thanks is enough?"

    #[Say more / Show more appreciation]
    menu:
        "Say more":
            show sc meganhouse m92
            mc"Oh, um... Thank you very much?"
            mc"And thanks for sending your limo to pick me up."
            mc"I really do appreciate it and I look forward to hearing from you tomorrow."
            #Megan is a little disappointed
            show sc meganhouse m93
            megan"Oh... Sure thing."
            show sc meganhouse m107
            megan"(I didn't take him for the completely ignorant type.)"
            $ v_ep01_megan_arrogant_counter += 1

        "Show your confidence":
            #The MC kisses her on the cheek
            play sound "sound effects/01/Male_kissing_girl_on_the_cheek.mp3"
            show sc meganhouse m94
            mc"Mwah!"
            mc"(Damn, she smells amazing!)"
            stop sound fadeout 1.0
            show sc meganhouse m89
            mc"And there's plenty more where that came from if you play your cards right."
            show sc meganhouse m90
            megan"(He's certainly sure of himself, and doesn't seem too intimidated by me... yet.)"
            show sc meganhouse m95
            megan"(But will his attitude in the future be a hindrance or a help?)"
            $ v_ep01_megan_cocky_counter += 1
            show sc meganhouse m96
            mc"I look forward to hearing from you tomorrow."
        "Show more appreciation"(wt="Best option"):
            #The MC kisses her on the cheek
            play sound "sound effects/01/Male_kissing_girl_on_the_cheek.mp3"
            show sc meganhouse m94
            mc"Mwah!"
            show sc meganhouse m103
            megan"Now there's a good boy."
            $ rewards_unlock ("megan",6)
            stop sound fadeout 1.0
            mc"(Damn, she smells amazing!)"
            show sc meganhouse m96
            mc"I look forward to hearing from you tomorrow."
            $ v_ep01_megan_respect_counter += 1

    #scene continues

    #The MC hops on his bike
    show sc meganhouse m97
    megan"The gate will open automatically on your way out."
    show sc meganhouse m98
    mc"Thanks."
    mc"Goodnight Megan."
    show sc meganhouse m99
    megan"Safe journey home, [y_name]."
    #The MC takes off on his bike and a member of security stands behind her to the side, talking over her shoulder
    show sc meganhouse m100
    security"Do you want me to send someone to follow him, boss?"
    show sc meganhouse m101
    megan"No, let him go."
    megan"I trust him not to say anything."
    show sc meganhouse m102
    megan"I have big plans for this kid which I will discuss with you all in due time..."
    #screen goes blank
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_13_03_MC_Evening_Visit1


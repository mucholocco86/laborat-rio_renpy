init:
    $ bella_heart_ep02_late_night_chat = False
    $ bella_heart_ep02_scene_03_let_her_leave = False
    $ v_ep02_02_03_chat_with_bella_counter = 0
    $ v_ep02_bella_fantasy_counter = 0

    image sc lateevechat nc reach down:
        "sc lateevechat nc b005" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b005a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b005b" with Dissolve(0.2, alpha=True)

    image sc lateevechat nc rub1:
        "sc lateevechat nc b005b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b005c" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc search1:
        "sc lateevechat nc b007" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b008" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b008a" with Dissolve(0.2, alpha=True)

    image sc lateevechat nc search2:
        "sc lateevechat nc b009" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b009a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc mast1:
        "sc lateevechat nc b012b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b012a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b012b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc mast2:
        "sc lateevechat nc b013b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b013a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b013b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc mast3:
        "sc lateevechat nc b014b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b014a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b014b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc mast4:
        "sc lateevechat nc b015b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b015a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b015b" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc mast5:
        "sc lateevechat nc b018" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b018a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b018b" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc lateevechat nc b018a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc lateevechat nc kneeling mast1:
        "sc lateevechat nc b019" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b019a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b019b" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b019a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc lateevechat nc kneeling mast2:
        "sc lateevechat nc b020" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b020a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b020b" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc lateevechat nc b020a" with Dissolve(0.2, alpha=True)
        pause 0.6
        repeat

    image sc lateevechat nc kneeling mast3:
        "sc lateevechat nc b020" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b020a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b020b" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b020a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc lateevechat nc mc lick:
        "sc lateevechat nc b021" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b021a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b021b" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc lateevechat nc b021a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc lateevechat nc kneeling mast4:
        "sc lateevechat nc b019" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc lateevechat nc b019a" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc lateevechat nc b019b" with Dissolve(0.2, alpha=True)
        pause 0.2
        "sc lateevechat nc b019a" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat

label lb_ep02_02_03_The_late_chat_with_Bella:
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #SCENE BEGINS
    #The scene begins with a blank screen - show Bella lying in bed on her back, eyes open
    play music "sound effects/02/Counting Sheep.mp3" loop fadein 1.0
    scene sc lateevechath 001
    with dissolve
    b"Hmph!"
    #Bella looks annoyed
    show sc lateevechath 002
    with dissolve
    b"(Just as predicted, I can't get back to sleep.)"
    #she rolls her eyes
    show sc lateevechath 003
    b"(Damn you, [y_name]!)"
    #she looks pissed off
    show sc lateevechath 004
    with dissolve
    b"(Well, at least he got the drive back and [mc_vic_address] won't be a grumpy prick about it in the morning.)"
    #Bella thinks things over
    show sc lateevechath 005
    b"(Then again, he might find something else to complain about.)"
    #reuse the same render above
    show sc lateevechath 006
    with dissolve
    b"(What is with me tonight?)"
    show screen scr_secret_icon("v_secrets_ep02_02_03_1") onlayer ontop
    with { "ontop": dissolve}
    #She's deep in thought here
    show sc lateevechath 006a
    with dissolve
    b"(I'm feeling more agitated than usual...)"
    #reuse the same render above
    show sc lateevechath 006b
    with dissolve
    b"(These stupid curfews are killing me.)"
    show sc lateevechath 006c
    with dissolve
    b"(Not being able to go out, to have fun, to feel...)"
    #reuse the same render above
    show sc lateevechath 006d
    with dissolve
    b"(Something, with someone...)"
    #show her hand on her stomach, above her underwear
    show sc lateevechath 007
    show screen scr_secret_hotspot ("sc lateevechath 007","700, 700, 200, 60","v_secrets_ep02_02_03_1")
    b"(Hmm... I could always try and pleasure myself to sleep.)"
    hide screen scr_secret_hotspot
    show sc lateevechath 008
    #Bella lays on her side on her bed - show the dildo under her bed in the same shot
    b"(But I don't think everyone is asleep yet.)"
    #show her face, thinking
    show sc lateevechath 009
    with dissolve
    b"(I'm going to see if [y_name] is still awake.)"
    #Bella sits up
    show sc lateevechath 010
    b"(He's the reason I'm wide awake, so I'm gonna go and spoil his night too...)"
    #Bella has a devilish look on her face
    #screen goes blank
    hide screen scr_secret_icon onlayer ontop
    with { "ontop": dissolve}
    scene black
    with dissolve
    scene black
    with Pause (2)
    show sc lateevechath 011
    with dissolve
    pause 1.0
    #Show Bella walking in the hallway towards the MC's room
    show sc lateevechath 012
    with dissolve
    b"(His door is still open, so perhaps he hasn't gone to bed yet.)"
    #the MC's door is open
    show sc lateevechath 013
    with dissolve
    b"[y_name]??"
    #She looks in his empty room
    pause 1.5
    show sc lateevechath 014
    with dissolve
    b"(Where is he?)"
    #she looks around
    b"(Maybe he's downstairs.)"
    #she looks down the stairwell: Ask Dots for this image
    show sc lateevechath 015
    with dissolve
    b"(I won't call out to him because I don't want to wake anyone up.)"
    #reuse the same render above

    if v_ep01_04_01_Bella_Work_Date == True:
        #"This scene if the player got the Special Date scene at the park with Bella in Episode 1"
        show sc lateevechath 016
        b"(Forget this, I need to use the bathroom.)"
        #she rolls her eyes
        stop music fadeout 2.0
        play sound "sound effects/01/Shower_Sound_Effect_In_High_Quality.ogg" loop fadein 1.0
        show sc lateevechath 017
        with dissolve
        pause 1.0
        #without thinking, Bella enters the bathroom where the MC is taking a shower
        #show her pushing the door open
        #shower sound effect
        show sc lateevechath 018
        with vpunch
        b"(Oh my!)"
        #she cups her mouth
        b"(He's taking a shower! How did I not hear that?)"
        show sc lateevechath 019
        b"(Oh...)"
        #Bella zeros on the MC's penis, which hangs down while he showers

        if v_ep01_task06_help_bella_artclass == True:
            #Add these lines if the player selected "Look away" in Episode 1, during the Art School task that leads to the Art Class scene
            show sc lateevechath 020
            b"(God, not again!)"
            #Bella's eyes look up, unhappy with herself
            show sc lateevechath 021
            b"(Why do I get myself into situations where I end up looking at his dick!?)"
            #Bella looks to one side, thinking
            show sc lateevechath 022
            b"(Still, it's pretty impressive.)"
            #she looks back at the MC in the shower, smirks
            show sc lateevechath 023
            b"(UGHH!)"
            #she's angry with herself
            b"(Dammit! I'm thinking dirty thoughts about him again!)"
            #reuse a render from above
            show sc lateevechath 024
            b"(What the fuck is wrong with me?)"
            #Bella angry with herself
            show sc lateevechath 028
            with dissolve
            b"(I need to get out of here before he sees me.)"
            #Bella looks at the bathroom door
            show sc lateevechath 029
            b"(I'll wait for him to finish...)"
            #She turns to leave the bathroom
            #Bella leaves
            show sc lateevechath 030
            with dissolve
            mc"(Hmm... Why do I have this feeling like I'm being watched?)"
            #The MC has a suspicious look on his face
            show sc lateevechath 031
            with dissolve
            mc"(Nah, it's probably just today's events messing with my head...)"
            #He turns to where Bella was standing previously
            #screen goes blank
        else:
            #Add these lines if the player selected "Take a closer look" in Episode 1, during the Art School task that leads to the Girls' locker room scene
            show sc lateevechath 025
            b"(I can't believe I'm thinking this, but I'm very impressed.)"
            #Replicate this image - https://pixhost.to/show/74/490115095_sc-artschool-a207.jpg
            show sc lateevechath 026
            b"(I mean... ew!)"
            #Replicate this image - https://pixhost.to/show/74/490115101_sc-artschool-a208.jpg
            show sc lateevechath 027
            with dissolve
            b"(Dammit, am I really that repressed?)"
            #Bella looks down and is disappointed in herself
            show sc lateevechath 028
            with dissolve
            b"(I need to get out of here before he sees me.)"
            #Bella looks at the bathroom door
            show sc lateevechath 029
            b"(I'll wait for him to finish...)"
            #She turns to leave the bathroom
            #Bella leaves
            show sc lateevechath 030
            with dissolve
            mc"(Hmm... Why do I have this feeling like I'm being watched?)"
            #The MC has a suspicious look on his face
            show sc lateevechath 031
            with dissolve
            mc"(Nah, it's probably just today's events messing with my head...)"
            #He turns to where Bella was standing previously
            #screen goes blank
    else:
        #"This scene if the player DID NOT get the Special Date scene at the park with Bella in Episode 1"
        play sound "sound effects/01/Shower_Sound_Effect_Reduced_Audio.mp3" loop fadein 1.0
        show sc lateevechath 016
        b"(I need to use the bathroom, however...)"
        #She slightly opens the door: the start of the shower sound effect
        #Bella doesn't go in, she stays outside, holding the door handle as the door slightly opens
        show sc lateevechath 033
        b"(Oh, so that's where he is.)"
        #Bella realising face
        #shower effect from outside the door
        b"(I might just wait for him to finish.)"
        #She steps back and closes the door
        show sc lateevechath 034
        b"(Phew! I nearly walked in on [y_name] showering!)"
        #Bella relieved
        show sc lateevechath 035
        b"(That would have been embarrassing.)"
        #She places a hand on her chest
        show sc lateevechath 036
        b"(And I would have seen him naked!)"
        #a slightly different render to the one above
        #Add these lines if the player selected "Look away" in Episode 1, during the Art School task that leads to the Art Class scene
        if v_ep01_task06_help_bella_artclass == True:
            show sc lateevechath 037
            b"(Again...)"
            #Bella hangs her head in shame
            #screen goes blank
    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)


    #the scene returns with the MC wearing just a towel
    #IMPORTANT make sure the side of the MC's face where he got punched at the end of Episode 1 is glowing a little pink colour
    play music "sound effects/02/Sibling Dispute1.mp3" loop fadein 1.0
    show sc lateevechath 038
    with dissolve
    pause 1.0
    #he enters his room where Bella is sitting on his bed
    show sc lateevechath 039
    with dissolve
    mc"[b_name]??"
    show sc lateevechath 040
    mc"What are you doing in my room??"
    #MC looks pissed off
    show sc lateevechath 041
    b"I wanted to talk to you."
    #She sits there, calm and composed. Her mouth open to speak
    menu:
        "Dismiss her":
            show sc lateevechath 042
            mc"Can't it wait? I'd like to change and get some sleep. It's been a long day."
        "Be polite"(wt="Bonus image"):
            show sc lateevechath 042
            mc"Okay, what do you want?"
            $ rewards_unlock ("bella",12)
    #Bella sits on his bed, with her mouth closed
    show sc lateevechath 043
    b"Hey... What happened to your face?"
    #Bella's expression changes where she looks concerned
    mc"What do you mean?"
    #reuse the same render as above
    show sc lateevechath 044
    with dissolve
    b"I can't believe I didn't notice it before. It's like a reddy-pink colour."
    #She stands up and looks at him with intent
    show sc lateevechath 045
    b"Did something happen?"
    #She has a hand on her hip and raises the palm of her other hand
    show sc lateevechath 046
    mc"No..."
    #He looks away from her
    show sc lateevechath 047
    b"It looks like somebody punched you."
    #she stands up close to him, placing a hand under the left side of his cheek, to take a better look
    show sc lateevechath 048
    mc"Well..."
    #The MC looks away, not making eye contact with her - show both of them in the same shot here
    show sc lateevechath 049
    b"Oh my God!"
    #Bella's mouth is wide open, realising what happened
    show sc lateevechath 050
    b"That's what happened, didn't it?"
    #a slightly different render to the line above
    show sc lateevechath 051
    mc"Look, it's not a big deal."
    #Bella looks at the MC with her mouth closed
    show sc lateevechath 050
    b"Who did this to you? I want names!"
    #reuse the same render as above
    show sc lateevechath 051
    mc"Just leave it, [b_name]."
    show sc lateevechath 049
    b"Did you put a cold towel or an ice pack on it?"
    #reuse the same render as above
    show sc lateevechath 052
    mc"I told you, I'm fine."
    #Bella starts heading for the door
    show sc lateevechath 053
    mc"Where are you going now?"
    #the MC watches her leave - show both of them in the same shot, the MC's mouth open to speak
    show sc lateevechath 054
    b"Just wait here. I'll be right back."
    #she leaves the room
    show sc lateevechath 055
    with dissolve
    mc"(Goddamnit... Will this night never end??)"
    stop music fadeout 1.0
    #show his bedroom door open with Bella already gone
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    play music "sound effects/01/Whispers of Love.mp3" loop fadein 1.0
    show sc lateevechath 056
    #scene returns with a shot of the MC's bedroom door from outside his room
    #don't show the MC and Bella here, yet
    with dissolve
    mc"Ow!!"
    b"Hold still! You're swelling up, [y_name]!"
    b"I need to attend to it until it goes down!"
    show sc lateevechath 057
    mc"Dammit, [b_name]!"
    #NOW show Bella holding the MC's face and pressing a cold hand towel against his cheek
    #they both sit on the bed together - Bella sits on his left
    #IMPORTANT - when creating some of these renders below, include some here and there where we see both of them in the same render, sitting on the edge of the bed
    #And if one person is speaking, then the other person's mouth should be closed.
    show sc lateevechath 058
    mc"I told you, I'm fine."
    #The MC's not happy with Bella sitting next to him on the bed
    show sc lateevechath 059
    mc"(Why does she suddenly give a damn about me?)"
    show sc lateevechath 060
    mc"Anyway, I got the drive back, which is the main thing."
    #the MC more calm, straight-faced, Bella sits next to him, listening
    show sc lateevechath 063
    b"So you found that girl from the party then? The one who stole it from you?"
    #Bella takes the towel away from his face and asks him seriously
    show sc lateevechath 062
    mc"Yeah, it was her."
    #Bella looks at the MC while the MC speaks
    show sc lateevechath 063
    b"That's great. How did you manage to track her down?"
    #Bella happy
    show sc lateevechath 064
    mc"I had some help. I spoke with someone who knew of her whereabouts."
    #MC is happy now too while Bella sits next to him smiling
    show sc lateevechath 072
    b"Well, whatever's on that drive must be pretty important."
    #reuse the same render as above
    show sc lateevechath 065
    mc"(She's right... I should see if [a_name] is still awake so we can take a look at the contents on it before I hand it over to [mc_vic_address].)"
    #While the MC thinks about this, show Bella smiling at him
    show sc lateevechath 066
    b"So who was this lead?"
    #Bella questions him, serious face
    show sc lateevechath 067
    mc"It's a long story. It's probably best if I keep that information to myself."
    #Bella's mouth is closed, listening to him speak
    show sc lateevechath 068
    b"Fine, don't tell me."
    #Bella is calm and looks away from the MC while mc pov sees her booba
    show sc lateevechath 069
    b"So how does it feel to get the drive back and prove [mc_vic_address] wrong?"
    #she looks back at the MC and calmly asks
    mc"Oh, it's like the best feeling in the world right now."
    #reuse the same render as above
    show sc lateevechath 070
    mc"But do you know what made it even better?"
    #a slightly different render than above
    show sc lateevechath 071
    mc"Getting the better of that girl who stole the drive from me."
    #the MC has a cocky look on his face

    if v_ep02_01_04_The_Shower == True:
        #"These lines if the player selected THE SHOWER during Scene 01-04"
        show sc lateevechath 072
        b"How did you get it?"
        #Bella asks with a concerned look
        show sc lateevechath 073
        mc"I stole it while she was taking a shower."
        #The MC looks cocky while Bella stares at him sceptically
        show sc lateevechath 074
        b"Did you take a quick peep?"
        $ rewards_unlock ("bella",13)
        #Bella has her arms folded, a cheeky look on her face
        show sc lateevechath 075
        mc"Huh? Why would you ask me that?"
        #the MC was agitated by the question, with Bella sitting next to him looking cheeky
        show sc lateevechath 076
        b"Well, did you?"
        #Bella folds her arms and has a straight face, slightly open mouth
        show sc lateevechath 077
        mc"Well, maybe for a few seconds."
        #the MC looks away at her when he responds
        show sc lateevechath 078
        b"Of course you did."
        #Bella rolls her eyes
        show sc lateevechath 079
        mc"Totally worth it though."
        #the MC smiles as he responds
        #Reuse a render from the GREEN SECTION ABOVE
    else:
        #"These lines if the player selected THE BED during Scene 01-04"
        show sc lateevechath 072
        b"How did you get it?"
        #Reuse a render from the GREEN SECTION ABOVE
        show sc lateevechath 073
        mc"I stole it while she was taking a shower."
        #Reuse a render from the GREEN SECTION ABOVE
        show sc lateevechath 077
        mc"It was incredibly tempting to take a look in the bathroom so I could see this girl in all her glory."
        #Reuse a render from the GREEN SECTION ABOVE
        show sc lateevechath 079
        mc"I can only imagine how hot she would've looked in the buff!"
        #Reuse a render from the GREEN SECTION ABOVE
        show sc lateevechath 066
        b"UGHH..."
        #Reuse a render from the GREEN SECTION ABOVE

    #SCENE CONTINUES
    show sc lateevechath 081
    mc"However, I would've given anything to see the look on her face when she realised I'd done a number on her."
    show sc lateevechath 073
    mc"It would have been glorious..."
    #He's pleased with himself while Bella looks at him unimpressed
    show sc lateevechath 084
    b"Oh my God..."
    #Bella looks at the MC, trying to hold in a laugh
    show sc lateevechath 083
    mc"What? Why are you looking at me like that?"
    #Similar render to the line above but with Bella's mouth closed
    show sc lateevechath 082
    b"It's so obvious..."
    #Bella is surprised
    show sc lateevechath 085
    b"You like this girl!"
    #Bella smiling here while talking
    show sc lateevechath 086
    mc"What???"
    #The MC is shocked while Bella smiles at him
    show sc lateevechath 087
    mc"Are you crazy?"
    #a slightly different look to the one above and Bella still smiles at him
    show sc lateevechath 089
    b"Yeah, I'm the one who's crazy."
    #Bella thinks the MC is nuts
    show sc lateevechath 085
    b"You're into this girl, it's written all over your face. You're glowing."
    #Bella backs up her point
    show sc lateevechath 090
    mc"That's absurd."
    #The MC looks away from Bella but she still looks at him
    show sc lateevechath 075
    mc"And the glow is probably still from that punch to the side of my face."
    #reuse the render above
    show sc lateevechath 087
    mc"Anyway, even if that were true, why do you care so much?"
    #reuse the render above

    if bella_love_level == 0:
        #These lines below if this player has LESS than ONE HEART with BELLA
        show sc lateevechath 091
        b"Never mind."
        #Show Bella unamused
        show sc lateevechath 092
        b"I'm going to bed."
        #A slightly different render to the one above
        show sc lateevechath 093
        b"Goodnight, [y_name]..."
        #Show her exiting his room
        show sc lateevechath 094
        mc"(What the hell was that all about?)"
        #The MC sits on his bed, confused
        show sc lateevechath 095
        mc"(Great!)"
        #The MC is pissed off now
        show sc lateevechath 096
        mc"(I'll never understand her.)"
        #the MC looks confused
        show sc lateevechath 097
        mc"(But was she jealous because of this other girl, or...)"
        #The MC thinks about what Bella could be upset about
        show sc lateevechath 098
        mc"(No, no... Surely it's not what I think it is.)"
        #Then looks away and dismisses that thought
        show sc lateevechath 099
        mc"(Terrific... I won't be able to sleep thinking about this.)"
        #The MC looks bemused
        show sc lateevechath 100
        mc"(Hmm... I'll go and see if [a_name] is still up...)"
        #(screen goes blank)"
    elif bella_love_level >= 1:
        #These lines below if this player already has ONE HEART with BELLA
        show sc lateevechath 102
        b"Uh... No reason."
        #Bella looks away from the MC
        show sc lateevechath 103
        mc"A-ha!"
        #The MC calls Bella out - he points at Bella while she sits on the bed next to him, looking away
        show sc lateevechath 104
        mc"You're jealous, aren't you?"
        #The MC acts cocky here
        show sc lateevechath 105
        b"Um... What are you talking about?"
        #Bella confused
        show sc lateevechath 103
        mc"You can't stand the fact that I \"might\" have something going on with an attractive girl..."
        mc"Even though I don't, and you have nothing or no one."
        #reuse a render from above
        show sc lateevechath 106
        b"No, it's not that at all."
        #Bella is cautious, dismissive, and looks away from him
        show sc lateevechath 107
        mc"Then what is it, [b_name]?"
        #The MC looks like he genuinely wants to know, Bella continues to look away
        show sc lateevechath 108
        b"You know what?"
        #Bella looks back at him - very calm
        show sc lateevechath 109
        b"I don't have to listen to this. I come in here to try and help, and this is the thanks I get."
        #Bella tries to make the MC seem ungrateful
        show sc lateevechath 110
        b"I knew it was a waste of time speaking to you."
        #Bella stands up and faces the palm of her hand at the MC's face "Talk to the hand" pose -
        #she doesn't look at the MC when she leaves his room

        #Let her leave / Stop her
        menu:
            "Let her leave":
                show sc lateevechath 111
                mc"Fine, go..."
                #the MC is pissed off
                #NO BELLA HEARTS AWARDED
                show sc lateevechath 093
                b"Goodnight, [y_name]..."
                #Bella unamused, exits his room
                show sc lateevechath 094
                mc"(What the hell was that all about?)"
                #The MC sits on his bed, confused
                show sc lateevechath 095
                mc"(Great!)"
                #The MC is pissed off now
                show sc lateevechath 096
                mc"(I'll never understand her.)"
                #the MC looks confused
                show sc lateevechath 097
                mc"(But was she jealous because of this other girl, or...)"
                #The MC thinks about what Bella could be upset about
                show sc lateevechath 098
                mc"(No, no... Surely it's not what I think it is.)"
                #Then looks away and dismisses that thought
                show sc lateevechath 099
                mc"(Terrific... I won't be able to sleep thinking about this.)"
                #The MC looks bemused
                show sc lateevechath 100
                mc"(Hmm... I'll go and see if [a_name] is still up.)"
                $ bella_heart_ep02_scene_03_let_her_leave = True
                #(screen goes blank)"
            "Stop her"(wt="Best option"):
                show sc lateevechath 111
                mc"[b_name]?"
                #The MC calls out to her, confused
                show sc lateevechath 112
                b"What do you want now?"
                #Bella stops before she exits his room
                show sc lateevechath 113
                mc"It's not my fault that it wasn't YOU in that shower instead of that girl."
                #the MC is being a smart ass
                show sc lateevechath 120
                mc"Not that I would've minded."
                #the MC smirks and Bella looks at the door
                show sc lateevechath 115
                b"Of course, you wouldn't... you're a perv. We all know that."
                #Bella turns around and faces him
                show sc lateevechath 116
                b"(I would not have minded either, but only so I could tease him.)"
                #Bella thinking
                show sc lateevechath 117
                b"(Fuck! Why do I keep thinking like this??)"
                #Bella angry at herself
                show sc lateevechath 118
                b"I'm going to bed. Good night, [y_name]."
                #Bella walking to the exit
                show sc lateevechath 119
                mc"(She didn't flip out like usual which is new for her.)"
                mc"(It almost feels like she's jealous because of the way I talked about this other girl.)"
                show sc lateevechath 120
                mc"(There's only one way to know for sure.)"
                #The MC thinks about what Bella could think
                show sc lateevechath 093
                mc"[b_name]... wait."
                #MC getting close to her
                show sc lateevechath 112
                with dissolve
                b"Now what, [y_name]?"
                #Bella is now getting frustrated with him
                show sc lateevechath 122
                mc"I just wanted to say thanks for your concern and also for the first aid."
                #The MC is appreciative and genuine
                show sc lateevechath 126
                mc"You know you can be downright nice sometimes when you want to be."
                #MC standing close to her
                show sc lateevechath 124
                b"Oh, thanks."
                $ rewards_unlock ("bella",14)

                if bella_love_level == 1:
                    #Bella is surprised by his compliment
                    show sc lateevechath 124a
                    b"Um, anyway, I should probably get some sleep."
                    show sc lateevechath 054
                    b"Talk to you tomorrow, [y_name]..."
                    #Bella is bemused and then exits his room
                    show sc lateevechath 094
                    with dissolve
                    mc"(That was a little strange.)"
                    #The MC sits on his bed, confused
                    show sc lateevechath 096
                    mc"(I don't think I'll ever understand her.)"
                    #the MC looks confused
                    show sc lateevechath 097
                    mc"(But was she jealous because of this other girl, or...)"
                    #The MC thinks about what Bella could be upset about
                    show sc lateevechath 098
                    mc"(No, no... Surely it's not what I think it is.)"
                    #Then looks away and dismisses that thought
                    $ v_ep02_02_03_chat_with_bella_counter += 1
                    show sc lateevechath 099
                    mc"(Terrific... I won't be able to sleep thinking about this.)"
                    #The MC looks bemused
                    show sc lateevechath 100
                    mc"(Hmm, I'll go and see if [a_name] is still up...)"
                    #(screen goes blank)"
                else:
                    #Bella is surprised by his compliment
                    show sc lateevechath 126
                    mc"I just wish there was some way I could thank you is all."
                    show sc lateevechath 127
                    b"You don't need to do or say anything, [y_name]. I-"
                    show sc lateevechath 128
                    with vpunch
                    pause 1.5
                    #the screen shakes as the MC suddenly kisses Bella on her lips
                    #Bella is taken by surprise – her eyes wide open mouth straight
                    play sound "sound effects/02/new_kissing_sound_FX1.mp3" noloop
                    show sc lateevechath 129
                    with dissolve
                    pause 1.0
                    b"Mmm..."
                    #Bella closes her eyes and gives in to the kiss
                    show sc lateevechath 130
                    with dissolve
                    b"(Wait, what?!)"
                    stop sound fadeout 1.0
                    #Bella comes to her senses, her eyes shoot open, and she breaks the kiss
                    show sc lateevechath 131a
                    with dissolve
                    pause 0.5
                    play sound "sound effects/02/slap_hard_effect.mp3" noloop
                    stop music fadeout 1.0
                    show sc lateevechath 131
                    with vpunch
                    if persistent.v_sounds_text_on == True:
                        "(Slap!)"
                    else:
                        pause 2.0
                        #Bella slaps slapping MC's face on the non-injured side - the left side, using her right hand.
                    show sc lateevechath 132
                    mc"OW!!"
                    #The MC shouts and grabs his left cheek
                    show sc lateevechath 133
                    b"You asshole!!"
                    #Bella angry
                    show sc lateevechath 115
                    b"I'm going to bed!!"
                    #Bella leaves the room angrily
                    show sc lateevechath 055
                    mc"(Wow ... Now that was one sweet kiss.)"
                    mc"(And was that also a flicker of tongue?)"
                    #the MC gives a cocky smirk
                    show sc lateevechath 098
                    with dissolve
                    mc"(Maybe there's more to her jealousy than she was letting on.)"
                    mc"(Who would have thought?)"
                    #Then looks away and dismisses that thought
                    show sc lateevechath 099
                    mc"(Terrific... Now I won't be able to sleep thinking about this.)"
                    #The MC looks bemused
                    show sc lateevechath 100
                    mc"(Hmm., I'll go and see if [a_name] is still up...)"
                    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    stop music fadeout 1.0
    with Pause (2)
    if persistent.v_secrets_enabled and bella_love_level > 0 and persistent.v_secrets_ep02_02_03_1:
        $ v_ep02_bella_fantasy_counter += 1
        jump lb_ep02_02_03_The_late_chat_with_Bella_NC
    else:
        jump lb_ep02_02_04_The_MC_talks_to_Ariel_about_the_flash_drive

label lb_ep02_02_03_The_late_chat_with_Bella_NC:
    if not _in_replay:
        scene img_secret_scene_overlay onlayer anim_layer
        with { "anim_layer": dissolve}
    else:
        show screen scr_end_replay
    #scene starts with bella laying in bed facing to the right.
    scene sc lateevechat nc b001
    with dissolve
    b"(I can't believe [y_name]!)"
    #Bella looks annoyed
    if bella_heart_ep02_scene_03_let_her_leave:
        b"(I try to help him and he acts like a total ass.)"
        b"(The nerve of him to call me jealous and that I have no one.)"
        show sc lateevechat nc b002
        b"(He frustrates me so much at times.)"
        b"(He just has this way about him that seems to push my buttons.)"
        show sc lateevechat nc b003
        with faster_dissolve
        b"(And as much as I hate to admit it, he's right. I don't have anyone right now.)"
        #She turns on her back now.
        show sc lateevechat nc b004
        with faster_dissolve
        b"(It's been such a long time since I've made out with someone, that I've almost forgotten just how good it can feel.)"
        # She holds her fingers up to her lips
        b"(And the thought of that is making me even more frustrated, and even a bit horny.)"
        show sc lateevechat nc reach down
        b"(Sigh, it's been far too long...)"
        # We see her hand reach down to her crotch
    else:
        if bella_love_level == 1:
            b"(It almost seemed like he was purposely teasing me while also acting like a gentleman.)"
            show sc lateevechat nc b002
            b"(He frustrates me so much sometimes.)"
            b"(He just has this way about him that seems to push my buttons.)"
            show sc lateevechat nc b003
            with faster_dissolve
            b"(When he acts that way, it just reminds me of how alone I am.)"
            #She turns on her back now.
            show sc lateevechat nc b004
            with faster_dissolve
            b"(It's been such a long time since I've made out with someone, that I've almost forgotten just how good it can feel.)"
            # She holds her fingers up to her lips
            b"(And the thought of that is making me even more frustrated, and even a bit horny.)"
            show sc lateevechat nc reach down
            b"(Sigh, it's been far too long...)"
            # We see her hand reach down to her crotch
        else:
            b"(The nerve of him to just kiss me like that.)"
            show sc lateevechat nc b002
            b"(He frustrates me so much sometimes.)"
            b"(He just has this way about him that seems to push my buttons.)"
            show sc lateevechat nc b003
            with faster_dissolve
            b"(What's worse is I didn't expect to enjoy it so much.)"
            #She turns on her back now.
            show sc lateevechat nc b004
            with faster_dissolve
            b"(It's been such a long time since I've made out with someone, that I'd almost forgotten just how good it can feel.)"
            # She holds her fingers up to her lips
            b"(I'm even more frustrated now, and even a little horny. Shit!)"
            show sc lateevechat nc reach down
            b"(I wonder what would of happened if I'd not resisted and I let him continue.)"
            # We see her hand reach down to her crotch
    show sc lateevechat nc rub1
    b"Mmm..."
    #she starts to slowly rub
    show sc lateevechat nc b006
    pause 1.0
    show sc lateevechat nc b007
    with faster_dissolve
    b"(Dammit!)"
    # Cuts back to her face with an annoyed look
    show sc lateevechat nc search1
    b"(I need to do something or else I won't be able to fall asleep.)"
    # she turns to her left and starts searching under her bed.
    show sc lateevechat nc search2
    b"(Where is that damn thing??)"
    show sc lateevechat nc b010
    b"(Ah, there you are.)"
    # She holds up the vibrator that was hidden under it
    show sc lateevechat nc b011
    b"(All right, I'll get this done quick so I can hopefully trail off.)"
    play sex1 "sound effects/02/sex/vibrator_soft_loop.ogg" loop fadein 0.5
    show sc lateevechat nc mast1
    b"(...)"
    # She turns it onto a low setting and places it on her crotch
    show sc lateevechat nc mast2
    with faster_dissolve
    b"(...)"
    # We see her trying to get off, but not getting anywhere
    show sc lateevechat nc mast3
    b"(Fuck! Why can't I get [y_name] out of my head?)"
    # Back to an annoyed expression on her face
    if bella_heart_ep02_scene_03_let_her_leave:
        b"(I can't imagine he would say those things to hurt me.)"
        show sc lateevechat nc mast4
        b"(I know that boys will sometimes pick on girls because they actually like them.)"
        b"(But there's no way he could see me as anything but an annoying [b_mc_rel].)"
    else:
        show sc lateevechat nc mast4
        if bella_love_level == 1:
            b"(It did seem like he was trying to be nice to me.)"
            b"(But there's no way he could see me as anything but an annoying [b_mc_rel].)"
        else:
            b"(Why would he kiss me?)"
            b"(Surely there's no way that he would see me as anything other than an annoying [b_mc_rel].)"
    show sc lateevechat nc b016
    b"(Granted I can't deny that he looks after himself, is quite strong and is easy on the eye.)"
    # Expression changes to a subtle smile
    play sex2 "sound effects/01/sex/bella_moan_slow.ogg" loop
    show sc lateevechat nc b017
    with faster_dissolve
    b"(Nghh...)"
    # She starts getting turned on thinking of the MC
    if v_ep01_04_01_Bella_Work_Date == True:
        b"(And the sight of just how big his package was, makes him seem even more impressive.)"
        show sc lateevechat nc mast5
        b"(And he wasn't even fully erect either.)"
    else:
        b"(And I'll bet he has a big package too.)"
        show sc lateevechat nc mast5
        b"(I can't help but notice the size of the bulge in his pants sometimes.)"
    # Cuts back to her crotch, the vibrator moving a little faster
    b"Ohhh yeah..."
    if v_ep01_04_01_Bella_Work_Date == True:
        b"(I wonder what it's like to be fucked by a cock as big as his.)"
    else:
        b"(I wonder what it would be like to be fucked by his huge cock.)"
    show sc lateevechat nc mast5
    with Dissolve(0.2, alpha=True)
    pause 0.4
    stop sex2 fadeout 1.0
    play sex4 "sound effects/01/sex/bella_moan_fast.ogg" loop
    show sc lateevechat nc kneeling mast1
    with Dissolve(0.2, alpha=True)
    b"Mmm, fuck me..."
    # An intense look on her face
    show sc lateevechat nc kneeling mast2
    b"(Oh god... Even having his face buried between my legs right now would be amazing, I bet.)"
    #stop sex1
    #play sex3 "sound effects/02/sex/vibrator_loud_loop.ogg" loop
    show sc lateevechat nc mc lick
    with flash(0.25, 0, 0.75, "#fff")
    b"Oh fuck, that's it [y_name], you're making me so wet."
    # Flashes to a shot of the MC between her legs as she imagins him going down on her
    show sc lateevechat nc kneeling mast3
    with flash(0.25, 0, 0.75, "#fff")
    pause 1.0
    b"(I can imagine him running his tongue all over my wet pussy, exploring my moistened lips until he finds my sensitive clit.)"
    # Back to her face as she is very close to climax
    b"Oh god, right there!"
    # Cuts back to her cotch as she is moving the vibrator even faster now.
    show sc lateevechat nc kneeling mast4
    b"Yes! Make your [b_mc_rel] cum!"
    stop sex4
    play sex3 "sound effects/02/sex/bella_climax.ogg" noloop
    b"NGHH!!" with vpunch
    # Cuts to her face as she climaxes
    show sc lateevechat nc b022
    b"Oh fuck!!" with vpunch
    show sc lateevechat nc b023
    with vpunch
    b"UNGHH!!!"
    # This last climax will be a crotch shot with the vibrator still blocking the view, but we see a splash effect from behind it as she cums one last time.
    stop sex4 fadeout 1.0
    stop sex1 fadeout 1.0
    show sc lateevechat nc b024
    with dissolve
    b"Oh, sweet lord..."
    # Back to her face, with an expression of joy on it
    stop sex3 fadeout 1.0
    show sc lateevechat nc b025
    with faster_dissolve
    b"(Damn, I really needed that.)"
    show sc lateevechat nc b026
    with faster_dissolve
    b"(But now I feel so dirty, so guilty...)"
    # Expression changes to confusion
    show sc lateevechat nc b027
    with faster_dissolve
    b"(Why on earth did I have to think about [y_name] to help me get off...?)"
    #(screen goes blank)"
    #NON-CANON BELLA SCENE ENDS
    $ persistent.replay_ep02_bella_solo_fantasy = False
    $ v_ep01_bella_fantasy_counter += 1
    scene onlayer anim_layer
    scene black
    with dissolve
    scene black
    stop music fadeout 1.0
    with Pause (2)
    $ renpy.end_replay()
    jump lb_ep02_02_04_The_MC_talks_to_Ariel_about_the_flash_drive


label lb_ep03_01_02_the_MC_speaks_with_Victor:
    scene sc mcvictalks b001
    with dissolve
    pause 2.0
    if v_ep03_01_01_megan_beating_guy == True:
        #These lines if the player played the scene where the #ADD A VARIABLE HERE FOR THIS PART OF THE SCENE begins in Scene 01-01
        #the MC is in deep thought
        mc"(Surely that didn’t happen.)" 
        #show sc mcvictalks b002
        show sc mcvictalks b002
        mc"(Megan had one of her men brutally beating that guy.)" 
        #show sc mcvictalks b003
        show sc mcvictalks b003
        mc"(What have I just agreed to?)" 
        #show sc mcvictalks b004
        show sc mcvictalks b004
        mc"(Who the hell is this woman?)" 
    #scene continues
    #show sc mcvictalks b005
    #Victor enters the room, dressed as a limo driver
    play music "sound effects/03/fathers_and_sons.mp3" loop fadein 1.0
    show sc mcvictalks b006
    with dissolve
    vic"[y_name]."
    show sc mcvictalks b007
    vic"Where have you been this morning?"
    show sc mcvictalks b008
    mc"I had a few things to take care of regarding the upcoming heist."
    show sc mcvictalks b009
    vic"Is that right?" 
    show sc mcvictalks b010
    vic"I have to talk with you about that, but not right now."
    show sc mcvictalks b011
    mc"Heading out again?" 
    show sc mcvictalks b007
    vic"Shortly."
    show sc mcvictalks b012
    vic"But something I want you to do is to look for any other opportunities where we could make some money."
    show sc mcvictalks b013
    mc"How do you mean?" 
    show sc mcvictalks b014
    vic"Opportunities that we can take advantage of."
    show sc mcvictalks b015
    vic"Other places or people we could hit which are preferably low-risk." 
    show sc mcvictalks b024
    vic"The art gallery heist is still several days away, but we could do with some other options for after this job is done." 
    show sc mcvictalks b017
    vic"What I’m saying is, let’s not put all of our eggs in one basket."
    vic"This [private_group] won't stop just because we've stolen a painting."
    show sc mcvictalks b018
    mc"Well, there might be one option for us."
    show sc mcvictalks b019
    vic"All right, I’m listening." 
    show sc mcvictalks b020
    mc"I met this girl who just started doing training sessions at our gym." 
    show sc mcvictalks b021
    mc"Her name’s Zora."
    show sc mcvictalks b012
    vic"And?"
    show sc mcvictalks b022
    mc"Her father is the main branch manager at Edge City Bank." 
    show sc mcvictalks b014
    vic"No, no banks. This is not a low-risk option, [y_name]."
    show sc mcvictalks b015
    vic"We don’t have enough time to prepare for it."
    show sc mcvictalks b023
    vic"You’ll have to come up with something else. "
    show sc mcvictalks b024
    vic"What about this girl?"
    show sc mcvictalks b025
    vic"What else do you know about her?"
    show sc mcvictalks b026
    mc"Not much."
    show sc mcvictalks b027
    mc"She’s an only child, studying to be a vet, and works in a small cafe."
    show sc mcvictalks b028
    mc"And her parents own a place on Main Street."
    show sc mcvictalks b029
    vic"Main Street?" 
    show sc mcvictalks b015
    vic"Do you mean in the ritzy side of town? That Main Street?"
    show sc mcvictalks b030
    mc"Yeah, that’s what she told me."
    show sc mcvictalks b031
    vic"Well that will be the mark then."
    show sc mcvictalks b032
    mc"The mark? Do you mean Zora?"
    show sc mcvictalks b033
    vic"Yeah, your next target."
    show sc mcvictalks b034
    vic"I want you to get close to this girl, learn more about her and get her to invite you over to her place."
    show sc mcvictalks b035
    mc"How the hell am I going to do that?"
    show sc mcvictalks b045
    mc"We only just met recently. I hardly know her."
    show sc mcvictalks b036
    vic"I’m sure it won’t be a problem for you, seeing as you like being around the ladies." 
    show sc mcvictalks b023
    vic"You’ll figure something out."
    show sc mcvictalks b037
    vic"Besides, this is your job, [y_name]."
    show sc mcvictalks b017
    vic"And what do I always say when it comes to our heists?"
    show sc mcvictalks b054
    mc"No job is impossible, nor do we let obstacles stand in our way."
    #the MC rolls his eyes as he speaks
    show sc mcvictalks b034
    vic"Exactly."
    show sc mcvictalks b039
    vic"I have no doubt this girl’s father will have a safe in his office or somewhere else."
    show sc mcvictalks b040
    vic"That’s what the end goal will be."
    show sc mcvictalks b041
    vic"What else can you tell me about her?"
    show sc mcvictalks b042
    vic"Does she have a boyfriend? Any siblings? Does she have any martial arts training?"
    show sc mcvictalks b043
    mc"Nope, she has none of those things."
    show sc mcvictalks b044
    vic"So she’s not a threat then?" 
    show sc mcvictalks b045
    mc"Are you kidding me?"
    show sc mcvictalks b046
    mc"She’s one of the most pleasant girls I’ve ever met. She’s harmless."
    show sc mcvictalks b047
    vic"All right, so when are you seeing her again?"
    show sc mcvictalks b048
    mc"I don’t have another session with her until next week."
    show sc mcvictalks b049
    vic"That’s not soon enough."
    show sc mcvictalks b050
    vic"Call her now, get her to meet with you. Do whatever is necessary."
    show sc mcvictalks b051
    mc"But [mc_vic_address]..."
    show sc mcvictalks b052
    vic"No buts, [y_name]. She’s your focus right now, nothing else."
    show sc mcvictalks b053
    vic"If you want to remain on this team, sometimes you’ll need to do things you don’t want to."
    show sc mcvictalks b054
    #The MC turns away from Victor and mumbles under his breath
    mc"(Murmurs) Yeah, because that’s worked out so well for you."
    show sc mcvictalks b055
    vic"Sorry, what was that?"
    show sc mcvictalks b056
    mc"Nothing."
    show sc mcvictalks b057
    mc"Fine, I’ll give her a call after I’ve had something to eat."
    #NEW TASK ADDED - Get Invited to Zora’s House
    $ task_addnew("Get Zora to invite you over to her place",12)
    show sc mcvictalks b058
    vic"Very good."
    show sc mcvictalks b059
    vic"I have a client to pick up shortly. I’m expected to drive them around all afternoon, so I’ll be back around dinner time."
    show sc mcvictalks b060
    vic"I hope you will have some good news regarding this Zora girl when I return..."
    #Victor leaves
    #show sc mcvictalks b061
    #The MC looks dismayed at what he’s just agreed to.
    #(screen goes blank)"
    #END SCENE
    stop music fadeout 2.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_01_03_Officer_Justice_finds_a_clue

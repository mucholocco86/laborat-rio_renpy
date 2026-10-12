label lb_ep01_The_MC_arrives_at_work1:
    #scene begins with the MC entering the gym holding the clothing bag Luke gave him.
    # And then he sees Harry behind the counter
    play ambient "sound effects/01/gymnasium_ambience1.ogg" loop fadein 1.0
    scene sc gymintro g01
    with dissolve
    mc"(I’m finally here.)"
    mc"(And there’s Harry.)"
    #harry stands behind the front counter
    show sc gymintro g03
    ha"Where the hell have you been, [y_name]?"
    show sc gymintro g02
    ha"How long does it take to pick up a package?"
    show sc gymintro g18c
    mc"Look, I have a legit reason for being late."
    show sc gymintro g14
    ha"Yeah, I’m sure you do. What’s your excuse this time?"
    ha"Were you abducted by aliens and anally probed in the past half hour and they dropped you off outside the gym without your bike?"
    show sc gymintro g09
    ha"Wait... Where’s your bike?"
    show sc gymintro g18d
    mc"That’s what I've been trying to tell you."
    show sc gymintro g18c
    mc"When I went to pick up the clothes at your brother’s store, some asshole stole it while I was inside."
    show sc gymintro g12
    ha"Geez, dude."
    ha"The amount of crime going on of late. You can’t trust anyone in this town."
    menu:
        "Agree with him":
            show sc gymintro g25
            mc"Uh, yeah... Tell me about it."
        "Disagree with him":
            show sc gymintro g18e
            mc"It's not as bad as it seems."
    show sc gymintro g09
    ha"So how did you manage to get here?"
    show sc gymintro g18f
    mc"You’re not going to believe this, but, I met this woman..."
    show sc gymintro g27
    mc"And once she realised that my bike had been stolen, she offered to give me a lift here."
    show sc gymintro g14
    ha"Out of the kindness of her heart?"
    show sc gymintro g15
    ha"That’s a rarity around here."
    show sc gymintro g05
    ha"So who is this mystery woman?"
    show sc gymintro g27
    mc"Her name’s Megan. She’s a real stunner too."
    show sc gymintro g18f
    mc"A great body, long blonde hair... A bonafide MILF!"
    show sc gymintro g28
    mc"And get this! She has her own driver and brought me here in a limo!"
    show sc gymintro g09
    ha"You’re so full of shit!"
    show sc gymintro g10
    ha"She’s probably some freak with three tits or something like that."
    show sc gymintro g13
    mc"Why would I lie to you about that?"
    show sc gymintro g18f
    mc"I mean, how else do you explain how I got here without my bike?"
    show sc gymintro g15
    ha"For all I know you sucked off some truck driver in exchange for a lift."
    show sc gymintro g23
    mc"You douche..."
    show sc gymintro g14
    ha"Well, if you can’t prove it, then it never really happened dude."
    show sc gymintro g18c
    mc"How do you expect me to prove it?"
    show sc gymintro g09
    ha"Did you get her digits? Or a business card? Or did she leave some of her lipstick on your cock??"
    show sc gymintro g05
    ha"Anything??"
    show sc gymintro g25
    mc"Hmm... I got her number, but..."
    show sc gymintro g18d
    mc"She asked me to call her Mrs. X."
    play sound "sound effects/01/Male_Laughing_Sound_Effect.mp3"
    show sc gymintro g14
    ha"Hahaha!"
    ha"That is the dumbest fucking story I’ve ever heard!"
    stop sound fadeout 1.0
    show sc gymintro g15
    ha"What is she like a Bond villain or something?"
    show sc gymintro g12
    ha"You’re unbelievable, dude."
    show sc gymintro g18g
    mc"Well, that’s my story and I’m sticking to it."
    show sc gymintro g09
    ha"I tell you what..."
    show sc gymintro g05
    ha"If you can prove that she’s real before our shift ends, then the first three rounds tonight are on me."
    show sc gymintro g18b
    mc"Hmm..."
    mc"(There has to be some kind of proof that I’m not making it up.)"
    show sc gymintro g19
    mc"Fine, you have a deal."
    #they shake hands
    show sc gymintro g14
    ha"And in case you’re wondering, I’ll have some expensive German beer for my first drink."
    menu:
        "Insult reply #1":
            show sc gymintro g23
            mc"Idiot..."
        "Insult reply #2":
            show sc gymintro g23
            mc"Well I'm gonna piss in your beer before you get it, you bellend..."
        "Insult reply #3":
            show sc gymintro g23
            mc"Whatever you say... you dick!"
    play sound "sound effects/01/Male_Laughing_Sound_Effect.mp3"
    show sc gymintro g14
    ha"Hahaha!"
    show sc gymintro g18c
    mc"You are right though. I should have at least asked her more questions about her personal life."
    stop sound fadeout 1.0
    show sc gymintro g14
    ha"Sounds like this woman is Megan you crazy!"
    ha"Even if she is a figment of your imagination."
    show sc gymintro g19
    mc"I’m not even going to respond to how painfully bad that pun was."
    show sc gymintro g14
    ha"I don’t know why you don’t get yourself a car, dude."
    show sc gymintro g13
    mc"I told you before, I don’t have the money for it... yet."
    show sc gymintro g18f
    mc"Besides, riding a bike is good for fitness."
    show sc gymintro g06
    ha"True... But it’s still pretty messed up that some scumbag took it."
    show sc gymintro g09
    ha"Are you going to report it to the cops?"
    show sc gymintro g13
    mc"What good will that do?"
    show sc gymintro g19
    mc"They couldn’t care less about a bike going missing."
    show sc gymintro g18
    mc"(And I’ve been trying to remain as inconspicuous as possible.)"
    show sc gymintro g12
    ha"Sorry, but I can’t help but be a law-abiding citizen."
    show sc gymintro g10
    ha"However, you make a fair point."
    ha"The police are probably using all their resources on that robbery that happened yesterday."
    show sc gymintro g25
    mc"You heard about that?"
    show sc gymintro g12
    ha"Of course!"
    show sc gymintro g09
    ha"There was also a female inspector in here earlier asking if I happened to have any information about it."
    show sc gymintro g24
    mc"(Shit... This officer has covered a lot of ground today.)"
    show sc gymintro g14
    ha"And unlike your mystery lady, this woman was not only insanely hot, but totally real!"
    show sc gymintro g16
    ha"And I have the security footage to prove it."
    #Harry points to the security camera in the top corner of the ceiling
    show sc gymintro g17
    mc"Smart ass..."
    #Harry grins at the MC
    show sc gymintro g18e
    mc"Anyway, how’s it been here this afternoon?"
    show sc gymintro g06
    ha"We had a bit of a rush of clients after lunch and it only died down about ten minutes ago."
    show sc gymintro g15
    ha"No doubt we’ll be busy again in an hour or so when all the \"business types\" come in for a session."
    show sc gymintro g14
    ha"So go and get changed and store those clothes my brother gave you inside your locker."
    ha"Then when you come back, you can watch the counter while I clean the changing rooms."
    show sc gymintro g27
    mc"Sure thing, Harry."
    show sc gymintro g14
    ha"See you in a bit."
    #the MC goes to leave and is still carrying the clothes from Luke’s store
    show sc gymintro g30
    mc"(How can I prove to Harry that Megan is real?)"
    show sc gymintro g31
    mc"(I better put these clothes away and get ready for work.)"
    #the MC has a look that an idea  has come to mind
    show sc gymintro g32
    mc"(Hmm... I’ve got it!)"
    mc"(I have the proof that I need!!)"
    stop ambient fadeout 1.0
    #the final shot here is the MC looking down at the clothes bag that Luke gave him
    #The clue here is that Luke can vouch for Megan being real and Harry will find out he lost the bet at the start of the next scene
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_meets_Juliet1

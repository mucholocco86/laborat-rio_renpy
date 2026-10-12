init:
    $ v_ep03_task_12_zora_counter = 0


label lb_ep03_02_04_The_MC_talks_with_Victor_at_the_house:
    #The MC enters the house where only Victor is present
    #he’s on the phone and has his back turned to the MC
    #the MC listens in to the conversation
    play music "sound effects/01/Family_Ties1.mp3" loop fadein 1.0
    scene sc mctalksvicabtzora h001
    with dissolve
    vic"Yeah..."
    show sc mctalksvicabtzora h002
    vic"Did you get it?"
    vic"Good."
    show sc mctalksvicabtzora h003
    vic"I have a lot going on today."
    vic"However, I should be able to fulfil that request later on."
    show sc mctalksvicabtzora h004
    vic"All right, I’ll be in touch. Bye."
    show sc mctalksvicabtzora h005
    mc"[mc_vic_address]?"
    #Victor turns around
    show sc mctalksvicabtzora h006
    vic"[y_name]. I didn’t hear you come in."

    #[Ask about the call / Mind your own business]
    menu:
        "Ask about the call":
            show sc mctalksvicabtzora h007
            mc"Who was that on the phone?"
            show sc mctalksvicabtzora h008
            vic"No one important. Just one of the guys at the head office for limo drivers."
            show sc mctalksvicabtzora h009
            vic"They’re asking me why I need the car on my day off."
            show sc mctalksvicabtzora h010
            vic "I’m trying to convince them to let me have it so I can use it for when I pick up this woman at the airport."
            vic"But they’re making things difficult."
            show sc mctalksvicabtzora h014
            mc"So what are we going to do if you can’t borrow it?"
            show sc mctalksvicabtzora h011
            vic"Don’t worry about that, [y_name]."
            show sc mctalksvicabtzora h009
            vic"I’ll figure it out."
            #the MC still looks suspicious of Victor
            show sc mctalksvicabtzora h013
            mc"If you say so, [mc_vic_address]."
            show sc mctalksvicabtzora h014
            mc"So how long are you home for?"

        "Mind your own business":
            show sc mctalksvicabtzora h014
            mc"How long are you home for?"
    #scene continues
    show sc mctalksvicabtzora h015
    vic"I’m just about to head out again."
    show sc mctalksvicabtzora h012
    mc"(Lately, he seems to be out of the house a lot more than he's actually here.)"
    #[Tell him about Zora / Don’t tell him about Zora]

    menu:
        "Tell him about Zora"(wt="Task point"):
            show sc mctalksvicabtzora h019
            mc"Oh, by the way, I spent time with that girl from the gym I told you about."
            show sc mctalksvicabtzora h020
            vic"And?"
            show sc mctalksvicabtzora h018
            mc"I’m seeing her again tonight, actually."
            show sc mctalksvicabtzora h019
            mc"She’s invited me over to her place."
            show sc mctalksvicabtzora h021
            vic"I have to say, good work, [y_name]."
            show sc mctalksvicabtzora h022
            vic"You’ve managed to get yourself over to her place in quick time."
            #Victor seems genuinely impressed
            #FIRST TASK POINT
            $ v_ep03_task_12_zora_counter +=1
        "Don’t tell him about Zora":
            show sc mctalksvicabtzora h022
            vic"But before I do, what happened with that girl from the gym you told me about?"
            show sc mctalksvicabtzora h024
            mc"Oh, well..."
            show sc mctalksvicabtzora h025
            mc"I’m seeing her again tonight, actually."
            show sc mctalksvicabtzora h028
            mc"She’s invited me over to her place."
            show sc mctalksvicabtzora h027
            vic"Is that right?"
            show sc mctalksvicabtzora h026
            vic"And is there any reason why you didn’t tell me sooner?"
            show sc mctalksvicabtzora h029
            mc"Well, I’ve only been home less than five minutes."
            show sc mctalksvicabtzora h031
            mc"And the job isn’t done yet, [mc_vic_address]."
            show sc mctalksvicabtzora h010
            vic"Hmm..."
            show sc mctalksvicabtzora h008
            vic"Very well."

    #scene continues
    show sc mctalksvicabtzora h033
    vic"Just make sure you keep your eye on the prize."
    show sc mctalksvicabtzora h034
    mc"One thing though..."
    show sc mctalksvicabtzora h035
    mc"I can’t guarantee that I’ll be back before curfew."
    show sc mctalksvicabtzora h032
    mc"Will that be a problem?"
    show sc mctalksvicabtzora h022
    vic"I’ll let it slide this time, considering it’s part of an even bigger job that I have in mind."
    show sc mctalksvicabtzora h006
    vic"Your main objective is to stake out the place whenever you can, without her knowing what you’re up to."
    show sc mctalksvicabtzora h009
    vic"Look for anything useful."
    show sc mctalksvicabtzora h011
    vic"Security systems, cameras, safes, anything of value."
    show sc mctalksvicabtzora h015
    vic"And then report everything you find out to me tomorrow."
    show sc mctalksvicabtzora h027
    vic"You got it?"
    show sc mctalksvicabtzora h031
    mc"Yeah, I know the drill."
    show sc mctalksvicabtzora h033
    vic"Anything else?"
    show sc mctalksvicabtzora h030
    mc"There was a cop at my gym yesterday poking around asking questions."
    show sc mctalksvicabtzora h010
    vic"And?"
    show sc mctalksvicabtzora h024
    mc"Um, nothing."
    show sc mctalksvicabtzora h013
    mc"I saw her outside the Walker place shortly after I entered the truck before we left."
    show sc mctalksvicabtzora h014
    mc"She might be on our tail, I’m not sure."
    show sc mctalksvicabtzora h016
    mc"I just thought you should know."
    show sc mctalksvicabtzora h017
    vic"What did she look like?"
    show sc mctalksvicabtzora h019
    mc"Brunette, late-20s, early-30s, five foot seven."
    show sc mctalksvicabtzora h020
    mc"Possible Latino background."
    show sc mctalksvicabtzora h036
    vic"I think I know who you’re referring to."
    show sc mctalksvicabtzora h037
    mc"Really?"
    show sc mctalksvicabtzora h006
    vic"Yeah, it sounds like it could be Officer Justice."
    show sc mctalksvicabtzora h029
    mc"How do you know about her?"
    show sc mctalksvicabtzora h011
    vic"I do my homework on everyone, [y_name]."
    show sc mctalksvicabtzora h039
    mc"So is she a threat?"
    show sc mctalksvicabtzora h036
    vic"No, I don’t believe so."
    show sc mctalksvicabtzora h022
    vic"But that’s not to say you shouldn’t cover your tracks."
    show sc mctalksvicabtzora h015
    vic"Anyway, I have to go now."
    show sc mctalksvicabtzora h040
    vic"No doubt you’ll have some useful information for me the next time we talk."
    show sc mctalksvicabtzora h041
    with dissolve
    pause 2.0
    #The MC watches Victor leave
    show sc mctalksvicabtzora h042
    with dissolve
    pause 2.0
    #the MC looks concerned
    stop music fadeout 2.0
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_02_05_The_MC_goes_over_to_Zoras_place

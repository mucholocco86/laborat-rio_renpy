label lb_ep02_03_03_Victor_makes_the_MC_part_of_the_next_heist:
    #SCENE BEGINS
    #The scene begins with the girls coming down the stairs
    $ renpy.music.set_volume(1.0, 0.0, channel="music")
    play music "sound effects/02/Carpe Diem.mp3" loop fadein 1.0
    scene sc girlscomesdownk 001
    with dissolve
    v"What's going on?"
    #Vivian looks concerned
    show sc girlscomesdownk 002
    b"Are you two arguing again?"
    #Bella has her hands on her hips
    show sc girlscomesdownk 003
    mc"Are we?"
    #the MC looks at Victor with a cocky grin

    show sc girlscomesdownk 018
    vic"No... We're good."
    #Victor concedes and replies through gritted teeth
    show sc girlscomesdownk 003
    mc"[mc_vic_address] was just telling me that now that we have the flash drive back, he's decided to include me on our next heist."
    #The MC turns to the girls
    show sc girlscomesdownk 005
    mc"Isn't that right?"
    #The MC's mouth open and smiling while Victor's is closed and angry

    show sc girlscomesdownk 020
    vic"Yes, that's correct."
    #Victor gives in but doesn't look happy

    show sc girlscomesdownk 007
    a"That's great news!"
    #Ariel happy for the MC

    show sc girlscomesdownk 008
    b"Congratulations, I guess."
    #Bella folds her arms and conceals her happiness for the MC

    show sc girlscomesdownk 009
    v"Thanks for giving  [y_name] another chance, [vic_name]."
    #Vivian stands up for the MC, addressing Victor

    show sc girlscomesdownk 010
    v"He's more than earned it."
    #She looks at the MC

    show sc girlscomesdownk 011
    v"Besides, from everything you've told us, we won't be able to do this job without a fifth person."
    #A slightly different render to the one above

    show sc girlscomesdownk 012
    mc"(I never thought I'd see the day when all three of them would be siding with me.)"
    #Show all three girls in the same shot looking at the MC, smiling

    show sc girlscomesdownk 013
    vic"Okay, enough with this gooey cr-"
    #The girls stare at Victor, unimpressed

    show sc girlscomesdownk 037
    with dissolve
    vic"...creation of emotion."

    show sc girlscomesdownk 015
    vic"With [y_name] now on board for the next heist, this is what's going to happen..."
    #A slightly different render to the one above

    show sc girlscomesdownk 025
    vic"Seeing as you like helping the girls out, there are a few more things that still need to be taken care of."
    #Victor addresses the MC

    show sc girlscomesdownk 017
    vic"I've already told the girls the first part of the plan for the next heist, so you better listen carefully, [y_name], as I will only say this once."

    show sc girlscomesdownk 018
    vic"There will be a guest of honour at the local art gallery for an exhibition of her work."

    show sc girlscomesdownk 048
    vic"She is arriving from Germany next week, and is staying at a major hotel in town, close to the gallery."
    vic"So we need to be well prepared."

    show sc girlscomesdownk 035
    vic"Our understanding is that no one at the gallery has ever met her in person, and she rarely attends public events."

    show sc girlscomesdownk 036
    vic"What we're going to do is intercept her arrival."

    show sc girlscomesdownk 022
    vic"The four of you are going to pose as either staff from the art gallery, the hotel she is staying in, or anyone who helps with her transportation from the airport."

    show sc girlscomesdownk 023
    mc"What does this woman have to do with robbing the art gallery?"

    show sc girlscomesdownk 024
    mc"We're stealing a painting, aren't we?"

    show sc girlscomesdownk 025
    vic"That's right."

    show sc girlscomesdownk 026
    vic"But in order to keep the people and security at the art gallery occupied during the exhibition, we're going to need someone to take her place."
    show sc girlscomesdownk 027
    vic"That's where you come in, [v_name]."
    show sc girlscomesdownk 028
    v"This next part is very important, sweetheart."
    show sc girlscomesdownk 029
    vic"The reason why I asked her to steal the dress and the wig from the acting theatre is that she will impersonate this German artist."
    show sc girlscomesdownk 049
    v"I've also been taking German lessons and listened to numerous audio recordings
    to master her accent."
    show sc girlscomesdownk 031
    vic"For this to work, we need this woman out of the picture so that [v_name] can take her place."
    show sc girlscomesdownk 035
    vic"Any questions so far?"
    show sc girlscomesdownk 033
    mc"What role will myself, [a_name] and [b_name] play?"
    show sc girlscomesdownk 031
    vic"I will give you all your respective tasks ahead of time before we intercept this woman."
    show sc girlscomesdownk 035
    vic"Your main objective is to do whatever you can to stop her from attending that exhibition."
    show sc girlscomesdownk 036
    vic"When she gets to her hotel, the three of you are going to need to steal some items from her hotel room so that the organisers at the art gallery truly believe that [v_name] is this artist."
    ###NEW TASK ADDED - INTERCEPT THE GERMAN ARTIST AT THE AIRPORT
    $ task_addfuturetask("Intercept the German Artist at the Airport",5)
    show sc girlscomesdownk 039
    mc"(Great... I still have more hoops that I have to jump through for him.)"
    #the MC rolls his eyes
    show sc girlscomesdownk 024
    mc"What should we do for the time being?"
    #reuse the same render as above
    show sc girlscomesdownk 027
    vic"I'll speak with you individually to make sure that you fully understand your assignments."
    #reuse the same render as above
    show sc girlscomesdownk 031
    vic"For now, just go about your business as per usual."
    #reuse the same render as above
    show sc girlscomesdownk 040
    mc"(Hmm... He seems to be working late quite a lot recently.)"
    #the MC is thinking and his mouth is closed
    show sc girlscomesdownk 039
    mc"(And even when he's not, he still leaves the house and doesn't come back until after midnight, like last night.)"
    #A slightly different render to the one above
    show sc girlscomesdownk 034
    vic"Make sure that you all get to work on time and remain as inconspicuous as possible."
    #reuse the same render as above
    show sc girlscomesdownk 035
    vic"My informants tell me that they still have police searching for us and also potentially another gang in town."
    #reuse the same render as above
    show sc girlscomesdownk 039
    mc"(Another gang?)"
    #reuse the same render as above
    show sc girlscomesdownk 040
    mc"(Could that be the one that I encountered last night?)"
    #reuse the same render as above
    show sc girlscomesdownk 024a
    mc"Did your informant give you any details about this other gang?"
    #reuse the same render as above
    show sc girlscomesdownk 026
    vic"Nothing useful."
    #reuse the same render as above
    show sc girlscomesdownk 025
    vic"So just keep your eyes peeled and always check to see if you're being followed."
    #reuse the same render as above
    show sc girlscomesdownk 009
    v"Yes, [vic_name]."
    #reuse the same render as above
    show sc girlscomesdownk 041
    v"Would you like me to make you some breakfast?"
    #Vivian looks more hopeful
    show sc girlscomesdownk 042
    vic"No, I'm not hungry."
    #he responds to Vivian
    show sc girlscomesdownk 043
    vic"I'm going out for a run and then I have some clients to pick up at lunchtime."
    #A slightly different render to the one above
    show sc girlscomesdownk 044
    with dissolve
    vic"We'll talk more about this next heist tomorrow. Make sure that you're all available."
    #Victor stands and then leaves the table
    show sc girlscomesdownk 045
    with dissolve
    a"So, you're in!"
    #Ariel happily speaks to the MC

    show sc girlscomesdownk 046
    mc"Yeah... It's a huge relief."
    #he responds to Ariel happily

    show sc girlscomesdownk 047
    mc"Thanks for having my back, ladies."
    #he addresses the girls

    show sc girlscomesdownk 048
    v"You're welcome."
    #show all three girls, but only Vivian has her mouth open

    show sc girlscomesdownk 049
    v"And don't worry about [mc_vic_address]."
    #Vivian addresses the MC

    show sc girlscomesdownk 050
    v"We all know he's very strict and set in his ways, but deep down I'm sure he appreciates all of you and the potential that you are showing."
    #Vivian addresses the girls

    show sc girlscomesdownk 051
    b"Yeah, and monkeys will fly out of my butt!"
    #Bella doesn't look convinced

    show sc girlscomesdownk 052
    mc"Now that would be a sight!"
    #the MC mocks her and smiles
    play sound "sound effects/01/Ariel_laughing3.mp3" noloop
    play sound2 "sound effects/01/sexy_female_laugh1.mp3" noloop
    show sc girlscomesdownk 053
    a"Hahaha!" (multiple=2)
    v"Hahaha!" (multiple=2)
    #Vivian and Ariel laugh - sound effect
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc girlscomesdownk 054
    b"Ah, geez..."
    #She looks embarrassed

    show sc girlscomesdownk 055
    v"Don't go anywhere. I'm gonna make you all something special to eat."
    #Vivian smiles and speaks enthusiastically to them all

    show sc girlscomesdownk 056
    mc"(Things have worked out pretty well. For now.)"
    #show Vivian walking into the kitchen

    show sc girlscomesdownk 057
    mc"([mc_vic_address] didn't punish me for being out after curfew again last night.)"
    show sc girlscomesdownk 058
    mc"(So that's another personal victory.)"
    show sc girlscomesdownk 060
    a"[y_name]."
    #Ariel and Bella sit at the breakfast table - she speaks, Bella's mouth closed
    show sc girlscomesdownk 061
    a"Come, sit with us."
    #Ariel extends her arm and points it at the seat next to her for the MC to sit at
    show sc girlscomesdownk 062
    with dissolve
    mc"(I should enjoy the moment while it's here...)"
    #show all of them in the same shot - Vivian cooking in the kitchen, Ariel and Bella chatting, and the MC smiling - a rare, happy, positive moment for them all
    stop music fadeout 1.0
    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_03_04_The_MC_Returns_To_His_Room


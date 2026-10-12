
label lb_ep03_01_04_The_MC_calls_Zora:
#SCENE BEGINS

    centered "Five minutes later, back in the gym...{w=2.0}{nw}" with dissolve
    show text "Five minutes later, back in the gym..."
    scene bg black with Dissolve(1)
    pause 1.0

    #show the MC in the boss's office, sitting down, looking in a filing cabinet in the office
    #https://media.istockphoto.com/id/870765174/photo/office-clerk-searching-for-files.jpg?s=612x612&w=0&k=20&c=jqW58EHdc6VS1vxSng_FSRA7GhAnO6eVM8-RhaHPKl8=
    scene sc mccallszora d001
    with dissolve
    mc"(...)"
    #He has a puzzled look on his face
    show sc mccallszora d002
    with dissolve
    pause 1.5
    #show a second image of the MC staring at the screen, scrolling through files and folders
    show sc mccallszora d003
    with dissolve
    mc"(A-ha! I got it.)"
    #He looks happy, after finding Zora’s number
    #he takes out his phone to call Zora
    show sc mccallszora d004
    #Dialling Sound Effect
    show sc mccallszora d005
    with dissolve
    "..."
    play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3" loop
    show sc mccallszora d007
    with dissolve
    pause 1.5
    "... ..."
    stop sound fadeout 1.0
    play music "sound effects/01/Whispers of Love.mp3" loop fadein 1.0
    show sc mccallszora d006
    zora"Hello?"
    #a close-up of her face
    show sc mccallszora d015
    mc"Zora, hey. It’s [y_name], from the gym."
    show sc mccallszora d009
    zora"Oh... Hi [y_name]!"
    #still a close-up of her face
    show sc mccallszora d008
    zora"This is a nice surprise."
    #still a close-up of her face
    show sc mccallszora d010
    mc"Where are you now? It sounds kind of \"busy\"."
    show sc mccallszora d011
    zora"I’m just at work. I’m on my break, so your timing is pretty good."
    #expand the shot to show her at the coffee shop she works at and in a cute little uniform
    #example - https://openart.ai/community/Ln3OSeIRNTo1uM4eWX6A
    #she sits out the back on her work break
    show sc mccallszora d012
    mc"At the coffee shop?"
    show sc mccallszora d013
    zora"That’s the one!"
    show sc mccallszora d014
    zora"By the way, how did you get my number?"
    show sc mccallszora d015
    mc"I uh... I had your contact details at the gym, which is where I’m at right now."
    show sc mccallszora d016
    zora"Oh, of course."
    show sc mccallszora d018
    zora"Anyway, I only have a few minutes before I have to go back to work. What can I do for you?"
    show sc mccallszora d019
    zora"We don’t have a session today, do we?"
    show sc mccallszora d020
    mc"No, no. That’s not why I called. But it does have to do with training."
    show sc mccallszora d012
    mc"I don’t know if you’re interested, but there's a park I go to for exercise, and I’m going there for a run."
    mc"And I was wondering if you’d like to join me?"
    show sc mccallszora d023
    zora"Oh... Well..."
    show sc mccallszora d024
    zora"Sure, I’d love to!"
    show sc mccallszora d025
    mc"Great."
    show sc mccallszora d018
    zora"When are you going?"
    show sc mccallszora d022
    mc"How’s tomorrow morning for you? Seven o’clock?"
    show sc mccallszora d013
    zora"Perfect. I have the whole day off so I’m all yours."
    pause 1.0
    show sc mccallszora d024
    with dissolve
    zora"Uh... You know what I mean."
    show sc mccallszora d020
    mc"Excellent."
    show sc mccallszora d019
    zora"And feel free to store my number in your phone."
    show sc mccallszora d025
    mc"I’ll do that shortly."
    mc"And I'll send you the details of the park and where to meet."
    show sc mccallszora d028
    zora"Okay, I really need to go."
    show sc mccallszora d029
    zora"See you in the morning, [y_name]."
    show sc mccallszora d007
    mc"Bye, Zora."
    #The call ends
    show sc mccallszora d030
    mc"(Phase one complete...)"
    stop music fadeout 2.0
    #the MC smiles
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep03_01_05_Dinner_and_Team_Meeting

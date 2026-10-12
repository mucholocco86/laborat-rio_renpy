init:
    image sc mcinalleyc ariel open window:
        "sc mcinalleyc 032" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcinalleyc 032a" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcinalleyc 033" with Dissolve(0.2, alpha=True)

    image sc mcinalleyc ariel fall:
        "sc mcinalleyc 039" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcinalleyc 039a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mcinalleyc 039b" with Dissolve(0.2, alpha=True)

    image sc mcinalleyc ariel riding bike:
        "sc mcinalleyc 048" with Dissolve(1.0, alpha=True)
        pause 1.5
        "sc mcinalleyc 048b" with Dissolve(1.0, alpha=True)

    image sc mcinalleyc ariel sly look:
        "sc mcinalleyc 082" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc mcinalleyc 082a" with Dissolve(0.2, alpha=True)

label lb_ep02_01_03_The_MC_calls_Ariel_and_asks_for_a_favour:
    #SCENE BEGINS
    #The scene begins with the MC back outside in the alleyway
    play ambient "sound effects/01/Alleyway_Ambience.ogg" loop fadein 1.0
    scene sc mcinalleyc 001
    with dissolve
    mc"(Damn, I'm lucky to get out of there fairly unscathed.)"
    show sc mcinalleyc 002
    mc"(And now I have a new task.)"
    #MC's expression is slightly different to the image above - mouth still closed
    show sc mcinalleyc 003
    with dissolve
    mc"(Well, two of them.)"
    #MC's expression is slightly different again to the image above - mouth still closed
    show sc mcinalleyc 004
    mc"(This could be my last shot at getting the drive back.)"
    #reuse the same render above
    show sc mcinalleyc 005
    mc"(However, I better check in with someone at the house.)"
    mc"(I could call [mc_v_address!c], but I won't, just in case [mc_vic_address] is with her right now.)"
    #he looks up from the phone as he's holding it
    show sc mcinalleyc 006
    mc"(No doubt he's angry that I missed tonight's meeting, so I don't want to make things worse for her.)"
    #reuse the same render above
    mc"([b_name] probably won't be able to help me either so I won't call her.)"
    #slightly different render to above
    stop ambient fadeout 1.0
    play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3" loop
    show sc mcinalleyc 007
    mc"(I'll call [a_name].)"
    #the MC puts the phone to his ear
    "..."
    "..."
    stop sound fadeout 1.0
    #dial tone sound effect
    play music "sound effects/02/Empty Streets.mp3" loop fadein 1.0
    show sc mcinalleyc 008
    a"[y_name]??"
    #he calls Ariel, who is in her room
    show sc mcinalleyc 009
    mc"Yeah, it's me."
    #MC speaks while holding the phone to his ear
    show sc mcinalleyc 010
    a"Where are you? I've been worried sick about you!"
    mc"(Aww... It's great that she cares so much.)"
    #show Ariel on her bed, mouth closed
    show sc mcinalleyc 009
    mc"Sorry I didn't check in sooner, I had a few things to take care of."
    #reuse the same render above
    show sc mcinalleyc 010
    a"Did you get the drive back?"
    #reuse the same render above
    show sc mcinalleyc 016
    mc"That's kind of why I'm calling you."
    show sc mcinalleyc 011
    mc"I know where to find the girl who took it, but I'm going to need your help."
    mc"Can you come and meet me right now, and bring with you an identical copy of the USB stick?"
    #reuse the same render above
    show sc mcinalleyc 015
    a"At this late hour? What do you need the stick for?"
    #reuse the same render above
    menu:
        "Don't answer her":
            show sc mcinalleyc 013
            mc"No time for questions, [a_name]. This is important."
            show sc mcinalleyc 014
            a"Oh..."
        "Be insistent"(wt="Task Point"):
            show sc mcinalleyc 013
            mc"No time for questions, [a_name]... I need you to do it NOW!"
            $ v_ep02_task09_find_the_flash_drive += 1
            show sc mcinalleyc 014
            a"Okay, okay..."
    show sc mcinalleyc 018
    a"But what if [mc_vic_address] finds out that I snuck out of the house?"
    #Ariel looks more concerned here
    show sc mcinalleyc 015
    a"He'll lose his mind! He's already in a bad mood as it is."
    #slightly different render to the one above
    show sc mcinalleyc 011
    mc"Don't worry about that. You're the last person he expects to disobey him."
    #MC looks kind of cocky when he says this
    show sc mcinalleyc 017
    mc"Besides, I can't come home as I think someone could be following me."
    #the MC looks around as if someone is following him
    show sc mcinalleyc 018
    a"How am I going to leave the house without [mc_vic_address] noticing?"
    #Ariel lifts a hand when saying this
    show sc mcinalleyc 019
    mc"Go out your bedroom window and then hang off the edge and just drop down."
    show sc mcinalleyc 020
    a"Will that actually work?"
    show sc mcinalleyc 011
    mc"Do you realise how many times I've broken out after curfew before without anyone noticing?"
    mc"And yeah, you'll be fine.."
    show sc mcinalleyc 023
    with dissolve
    mc"The drop to the ground isn't that far."
    #the same render as above but her mouth is closed
    show sc mcinalleyc 024
    mc"And when you get back, there's a ladder around the side of the house."
    show sc mcinalleyc 025
    mc"You can use it to get back up to your room without having to go through the front door."
    show sc mcinalleyc 026
    with dissolve
    a"I don't know, [y_name]..."
    #ariel looks worried
    show sc mcinalleyc 027
    mc"Come on, [a_name], I really need your help here. You can do it."
    #the same render as above but her mouth is closed
    show sc mcinalleyc 028
    a"(Oh geez...)"
    #ariel looks down, worried, mouth closed
    show sc mcinalleyc 029
    a"(This is such a bad idea, but he sounds like he's in serious trouble.)"
    #reuse the same render above - but close-up camera
    show sc mcinalleyc 026
    a"Okay, I'll come and see you."
    #reuse the same render above
    show sc mcinalleyc 016
    mc"That a girl!"
    show sc mcinalleyc 031
    mc"Can you also grab me a shirt and a towel?"
    show sc mcinalleyc 029
    mc"I'm a bit of a mess right now."
    show sc mcinalleyc 026
    a"Um... Okay."
    a"What shirt should I bring you?"
    show sc mcinalleyc 027
    mc"Any will do."
    mc"And don't forget to lock your bedroom door and turn the lights off before you leave."
    #reuse the same render above
    show sc mcinalleyc 026
    a"Sure... So where do you want to meet?"
    #reuse the same render above
    show sc mcinalleyc 028
    mc"I'll send you the address shortly..."
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    play music "sound effects/01/Midnight Heist.mp3" loop fadein 1.0
    show sc mcinalleyc ariel open window
    with dissolve
    pause 1.0
    a"(This is so risky.)"
    #show Ariel lifting her bedroom window #cant make her lift the window since it's part of the wall
    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    #show Ariel sliding through the window and out onto the roof - she wears a hoodie and tight shorts, showing off her legs
    #make sure she goes ass out first.
    show sc mcinalleyc 034
    with dissolve
    pause 1.0
    a"(Okay, I'm up high.)"
    a"(No big deal.)"
    #Ariel looks away from the house, down at the front lawn
    show sc mcinalleyc 035
    with dissolve
    pause 1.0
    a"(I just can't afford to make any big noises.)"
    show sc mcinalleyc 036
    with fast_dissolve
    pause 1.0
    a"(All right, here goes nothing.)"
    show sc mcinalleyc 037
    with fast_dissolve
    pause 1.0
    show sc mcinalleyc 038
    with fast_dissolve
    pause 1.0
    if persistent.v_anim_enabled:
        show sc mcinalleyc ariel fall
    else:
        show sc mcinalleyc 039b
    with faster_dissolve
    with vpunch
    a"(Woah!)"
    show sc mcinalleyc 040
    with dissolve
    pause 1.0
    #create a couple of extra images of Ariel here - this is a good place to show some upskirts of Ariel while she's hanging on the rope and above the ground. And also one above her so we see her worried face not looking down at the ground

    show sc mcinalleyc 041
    with dissolve
    a"(Oh shit, oh shit!)"
    show sc mcinalleyc 042
    a"(Please don't let me break a leg or something bad!!)"
    #show her hands releasing from the rope and she lands on her ass
    show sc mcinalleyc 042a
    with Dissolve(0.2, alpha=True)
    a"OH NO!{w=0.8}{nw}"
    show sc mcinalleyc 043
    with Dissolve(0.2, alpha=True)
    pause 0.6
    show sc mcinalleyc 043b
    with Dissolve(0.2, alpha=True)
    pause 0.6
    #screen shakes
    show sc mcinalleyc 044
    with vpunch
    pause 0.6
    a"(Phew!)"
    show sc mcinalleyc 045
    with faster_dissolve
    a"([y_name] was right. It wasn't that big of a fall.)"
    show sc mcinalleyc 046
    a"(Okay, I just have to get my bike and I'll be on my way.)"
    #Ariel is downstairs on the front lawn
    scene black
    with dissolve
    pause 1.0
    show sc mcinalleyc 047
    with dissolve
    pause 1.0
    show sc mcinalleyc ariel riding bike
    with dissolve
    a"(I'm coming [y_name]!)"
    #Show Ariel riding her bike to find the MC
    #screen goes blank
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)

    play music "sound effects/02/Midnight Rendezvous.mp3" loop fadein 1.0
    show sc mcinalleyc 049
    with dissolve
    pause 1.5
    #the MC waits on a street corner and looks down the street
    show sc mcinalleyc 050
    with dissolve
    mc"(I think that's her now.)"
    show sc mcinalleyc 051
    #Ariel shows up
    a"Hey [y_name]."
    show sc mcinalleyc 052
    mc"Thanks for getting here so quickly, [a_name]."
    #the MC has a thankful look on his face
    show sc mcinalleyc 053
    mc"Do you think [mc_vic_address] knows that you're gone?"
    show sc mcinalleyc 054
    a"I don't think he has any idea, so I should be okay."
    show sc mcinalleyc 057
    mc"Did you bring what I asked?"
    show sc mcinalleyc 054
    a"One second, [y_name]. Let me hop off my bike."
    pause 1.0
    show sc mcinalleyc 074
    with dissolve
    a"Okay, so I packed a clean shirt."
    show sc mcinalleyc 073
    a"There's also a towel in there."
    show sc mcinalleyc 075
    a"And the flash drive is in the front pocket."
    #Ariel takes off her backpack and hands it to him
    show sc mcinalleyc 076
    mc"Thanks, [a_name]."
    show sc mcinalleyc 078
    mc"You're a lifesaver!"
    #He takes the bag from her and looks at it
    show sc mcinalleyc 079
    mc"Do me a favour and keep an eye out while I get changed."
    #The MC puts the bag down and starts to take off his shirt
    show sc mcinalleyc 080
    a"Oh..."
    #Ariel looks surprised
    show sc mcinalleyc 081
    a"You're changing clothes right here?"
    #The MC reaches for his pants
    show sc mcinalleyc ariel sly look
    mc"Naturally."
    #The MC confidently removes his pants so he's standing in only his underwear
    show sc mcinalleyc 083
    a"(Oh my...)"
    #Ariel blushes as she stares at the MC
    show sc mcinalleyc 084
    mc"It's no big deal. This will just take a minute."
    #He starts putting on some clean pants
    show sc mcinalleyc 068
    mc"Besides, I don't really have time to waste."
    #Ariel isn't sure where to look
    show sc mcinalleyc 069
    a"Oh... Okay..."
    #Ariel turns away and we see the MC preparing to put on his shirt
    show sc mcinalleyc 082
    with dissolve
    pause 2.0
    show sc mcinalleyc 086
    with dissolve
    mc"There... Now I'm good as gold!"
    #The MC puts a new shirt on
    show sc mcinalleyc 088
    with dissolve
    mc"It's refreshing to have clean clothes on again."
    #Ariel turns back to see the MC fully clothed again
    show sc mcinalleyc 072
    a"I'll bet."
    show sc mcinalleyc 069
    a"So what on earth happened to you?"
    #ariel looks at the state of the MC
    a"And where have you been all night? Are you okay?"
    show sc mcinalleyc 070
    mc"I'm fine. I just have to follow up this lead and then I'll come straight home."
    #MC looks casual, composed
    show sc mcinalleyc 069
    a"I see..."
    show sc mcinalleyc 088
    mc"Hey..."
    #Ariel looks down, as she's worried about the MC
    show sc mcinalleyc 060
    mc"You have nothing to worry about, [a_name]. I'll be okay."
    #MC puts a hand on her shoulder, to reassure her
    show sc mcinalleyc 061
    a"I wish I could believe you."
    #Ariel hugs the MC
    show sc mcinalleyc 062
    mc"I'll be back before you know it. Trust me."
    #MC smiles and talks to her while they hug
    #Ariel hands an identical flash drive to the MC - red, like the one used in the opening heist
    show sc mcinalleyc 088
    mc"Now get on home, just in case [mc_vic_address] suspects anything."
    #They break their embrace, and he looks her in the eye
    show sc mcinalleyc 054
    a"Please call or message me as soon as you're on your way back."
    #reuse the same render above
    show sc mcinalleyc 057
    mc"I will."
    #reuse the same render above
    show sc mcinalleyc 064b
    a"Bye [y_name]. Be safe."
    #Ariel hops back onto her bike
    show sc mcinalleyc 065
    with dissolve
    mc"Always, {i}Mini Marvel{/i}..."
    #Ariel rides off
    show sc mcinalleyc 086a
    with dissolve
    mc"(Okay, I have the location and everything I need to make things right.)"
    #MC's mouth closed while he is thinking.
    show sc mcinalleyc 088a
    mc"(It's now or never...)"
    #a slightly different image to the one above, more confident
    #(screen goes blank)"
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl
    #END SCENE

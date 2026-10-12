init:
    $ v_ep02_task09_find_the_flash_drive = 0

    image sc mckidnapb shock:
        "sc mckidnapb 004d" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc mckidnapb 006a" with Dissolve(0.2, alpha=True)

label lb_ep02_01_02_The_MC_is_kidnapped_by_the_Apex_Legion:
    #SCENE BEGINS
    #play ambient "sound effects/02/abandoned_warehouse_ambience.ogg" loop fadein 1.0
    play ambient "sound effects/02/factory_water_dripping.ogg" loop fadein 1.0
    show sc mckidnapb 000
    with slow_dissolve
    pause 1.5
    #The scene begins with a blank screen - the MC has his eyes closed
    #His arms are behind his back, tied to the chair so he can't move
    #we hear them talking
    show sc mckidnapb 001
    with Dissolve(1.0)
    guy"Hey! Time to wake up, snowflake."
    show sc mckidnapb 002a
    with faster_dissolve
    pause 0.4
    play sound "sound effects/02/slap_hard_effect.mp3" noloop
    show sc mckidnapb 003
    with hpunch
    with faster_dissolve
    show sc mckidnapb 002
    with faster_dissolve
    pause 0.4
    #the guy slaps him in the face - sound effect for slap
    show sc mckidnapb 004
    with faster_dissolve
    pause 0.5
    show sc mckidnapb 004a
    with faster_dissolve
    pause 0.5
    show sc mckidnapb 004b
    with faster_dissolve
    pause 1.0
    show sc mckidnapb 004c
    with dissolve
    stop sound fadeout 1.0
    mc"Where the hell am I?"
    show sc mckidnapb shock
    with faster_dissolve
    guy"QUIET!" with hpunch
    #he sees the tattoo guy standing next to a tray of sharp tools
    show sc mckidnapb 006a

    #tattoo guy shouts
    show sc mckidnapb 007
    with faster_dissolve
    guy"I will speak and you will listen."
    show sc mckidnapb 009
    #The MC looks at the tattoo guy and recognises him
    mc"Wait a second... You're the guy that was at the nightclub."
    show sc mckidnapb 010
    guy"Yeah, and you're the smartass who's been poking around, asking about a certain tattoo."
    show sc mckidnapb 011
    guy"What the hell are you doing on our turf? Who were you looking for?"
    #Tattoo guy's expression is slightly different to the line before this one
    show sc mckidnapb 012
    mc"No one."
    show sc mckidnapb 013
    guy"Don't lie to me, kid. You don't want to piss me off."
    mc"(I better not give anything away.)"
    $ task_addnew("Find the flashdrive",9)
    menu:
        "Piss him off anyway" (wt="Task Point"):
            show sc mckidnapb 014
            mc"Ah, so you're the big prick that runs the show, huh?"
            #MC gives a cocky look, smiling
            $ v_ep02_task09_find_the_flash_drive += 1
            show sc mckidnapb 011
            guy"You little shit! Maybe that punch that knocked you out wasn't enough."
            show sc mckidnapb 015
            #The guy raises his hand/arm to hit the MC again
        "Back down":
            show sc mckidnapb 013
            pause 0.5
            #scene continues
    show sc mckidnapb 017
    woman"STOP!"
    $ task_addfuturetask("",1,notify=False)
    show sc mckidnapb 018
    with faster_dissolve
    pause 1.0
    show sc mckidnapb 018a
    with faster_dissolve
    pause 1.0
    show sc mckidnapb 018b
    with faster_dissolve
    pause 1.0
    #the guys turn their heads to a voice that calls in the darkened part of the room
    mc"Wait a second..."
    #the MC looks around and sees the girl in the shadows, lighting a smoke
    show sc mckidnapb 020
    #it's a silhouette of the girl in the alleyway
    mc"It's you!"
    show sc mckidnapb 019
    #the MC looks surprised
    mc"Hey! I want what you stole from me!"
    show sc mckidnapb 011
    #then he looks angry
    guy"SHUT UP!"
    show sc mckidnapb 022
    guy"Not unless you want this jammed through your neck!"
    #the guy holds a sharp object up at the MC's face
    show sc mckidnapb 023
    with vpunch
    mc"(Oh, crap...)"
    #MC's mouth closed, he looks worried

    #ANIMATED SCENE? - The woman moves towards him, showing her face and we see she's a different woman than the one at the party - She's Asian.

    show sc mckidnapb 027
    with dissolve
    mc"(Wait a minute... That's not her.)"
    #MC surprised look on his face
    show sc mckidnapb 025
    woman"And what exactly did I steal from you, huh?"
    #woman looks calm and casual
    show sc mckidnapb 027
    mc"Okay... Not what I was expecting."
    #MC looks confused
    mc"I thought you were someone else."
    #show the woman, with her mouth closed, hands on hips
    show sc mckidnapb 028
    woman"I get that a lot."
    #woman gives a slight smile
    show sc mckidnapb 029
    with dissolve
    pause 1.0
    show sc mckidnapb 029a
    with dissolve
    pause 1.0
    show sc mckidnapb 030
    with dissolve
    pause 1.0
    #show the woman taking her wig off and we see her real hair now
    show sc mckidnapb 031
    with dissolve
    mc"Woah..."
    #MC surprised
    show sc mckidnapb 032
    mc"Okay, what the hell is going on here??"
    #MC confused
    show sc mckidnapb 033
    woman"I'll be the one asking the questions."
    #Woman is stern in her response - images will be new now because she's not wearing a wig
    show sc mckidnapb 034
    woman"Why were you looking for us? And what were you doing wandering around outside our hideout?"
    #she crosses her arms as she asks this question
    show sc mckidnapb 032
    mc"Well, I wasn't looking for you specifically."
    #reuse the same render
    show sc mckidnapb 031
    mc"I had an inkling that a woman who I thought was you, could be here."
    show sc mckidnapb 034
    mc"This is just a case of mistaken identity."
    #reuse the same render above
    show sc mckidnapb 036
    guy"So why were you asking about the tattoo the other night?"
    #the tattoo guy addresses the MC
    show sc mckidnapb 037
    mc"Well, the person I'm looking for has the exact same tattoo as hers."
    #the MC points at Lucy
    #The MC refers to Lucy - the Asian girl
    show sc mckidnapb 034
    woman"Who exactly are you looking for?"
    #reuse the same render above
    show sc mckidnapb 022
    mc"There was an attractive girl at a party that I went to a few days ago."
    #reuse the same render above
    show sc mckidnapb 034
    mc"She also has the same cat tattoo that you have on your back."
    #reuse the same render above
    show sc mckidnapb 038
    woman"UGHH!"
    #lucy annoyed face
    show sc mckidnapb 039
    woman"That bitch!"
    #Lucy angry
    mc"You know her?"
    #the MC looks puzzled
    show sc mckidnapb 041
    woman"I guess you could say that."
    show sc mckidnapb 042
    woman"He's looking for you know who."
    #Lucy turns to the tattoo guy
    show sc mckidnapb 043
    guy"Yeah, it seems like it."
    #and he looks at her in his response
    show sc mckidnapb 041
    woman"What do you want with this girl anyway?"
    #the woman looks at the MC
    show sc mckidnapb 032
    mc"She stole something of value to me and I need to get it back."
    #reuse the same render above
    show sc mckidnapb 045
    woman"And what is this valuable item that she took?"
    #she raises her palm, pointing it at him when she responds
    show sc mckidnapb 047
    mc"Um.. It's just a flash drive."
    #the MC said this casually, not making eye contact with her
    show sc mckidnapb 041
    woman"Is that it? All of this trouble over some flash drive?"
    #reuse the same render above
    show sc mckidnapb 031
    mc"I know it doesn't seem like much, but it's very important to me."
    #show Lucy looking at him with her mouth closed
    show sc mckidnapb 049
    guy"This is a waste of time."
    #tattoo guy intervenes
    show sc mckidnapb 048
    guy"I say we knock him out, put him in the back of the van and leave him someplace where no one will find him."
    #tattoo guy looks with the intent on his face
    show sc mckidnapb 050a
    guy"Lights out again for you, buddy boy!"
    show sc mckidnapb 050
    with fast_dissolve
    play sound "sound effects/02/blocking_a_punch1.mp3" noloop
    show sc mckidnapb 051
    with vpunch
    woman"No!"
    #the woman grabs the tattoo guy's arm before he can strike - SOUND EFFECT grabbing his arm
    show sc mckidnapb 052
    with dissolve
    woman"Cut him loose."
    show sc mckidnapb 053
    #she lets his arm go and looks at him as she responds
    guy"What??"
    #tattoo guy looks puzzled
    show sc mckidnapb 054
    guy"Why?"
    #The guy gets angry
    show sc mckidnapb 055
    woman"Because he's not a threat."
    show sc mckidnapb 072
    woman"However... He could be of some use to us."
    show sc mckidnapb 056
    guy"But-"
    #tattoo guy tries to change her mind
    show sc mckidnapb 057
    woman"Just do it."
    #she replies sternly
    show sc mckidnapb 058
    with dissolve
    guy"Fine!"
    show sc mckidnapb 059
    with dissolve
    pause 1.0
    #guy bends down to cut the MC from his restraints
    play sound "sound effects/02/knife_sound_effect.mp3" noloop
    show sc mckidnapb 060
    with dissolve
    guy"I've still got my eyes on you, do you hear me?"
    #guy waves his knife across his face
    show sc mckidnapb 061
    mc"Hey... You don't have to tell me twice."
    #the MC gives a cocky look as he responds
    show sc mckidnapb 062
    mc"(Goddamn... That punch may have realigned my jaw.)"
    #The MC grabs at his jaw
    show sc mckidnapb 063
    guy"Face her, kid."
    #the guy stands behind the MC, watching over him
    show sc mckidnapb 064
    woman"So... What are we going to do with you?"
    show sc mckidnapb 065
    mc"You guys aren't gonna get me to strip all my clothes off and make me run home naked, are you?"
    #the MC looks concerned
    show sc mckidnapb 066
    woman"Huh? Why the hell would we do that?"
    #she looks confused
    show sc mckidnapb 067
    mc"Um... Never mind."
    show sc mckidnapb 068
    mc"So what are you going to do to me?"
    show sc mckidnapb 069
    mc"Torture me until I give up more details?"
    show sc mckidnapb 072
    woman"On the contrary. I have something else in mind."
    #she raises an eyebrow and smiles
    show sc mckidnapb 070
    guy"Wait... Are you going to get him to do the job for us?"
    #the tattoo guy looks at Lucy
    show sc mckidnapb 057
    woman"Precisely!"
    #she seems happier here
    show sc mckidnapb 072
    woman"Now you see why we can't kill him."
    #and then she turns to the guy
    show sc mckidnapb 075
    mc"Well, that's a relief."
    #the MC looks relieved
    show sc mckidnapb 074
    guy"Good thinking, boss. We'll get him to do our dirty work for us."
    #tattoo guy rubs his hands together looking at mc
    show sc mckidnapb 075
    mc"Err... Wait, what job are you talking about?"
    #reuse the same render above
    show sc mckidnapb 077
    woman"The girl that you're looking for, we know where she's hiding."
    #reuse the same render above
    show sc mckidnapb 078
    woman"One of our guys picked up her trail about twenty minutes ago and he's tailing her as we speak."
    #reuse the same render above
    show sc mckidnapb 075
    mc"(So there's more of them in this girl's group. But how many?)"
    #show an image of Lucy staring at him with her mouth closed
    show sc mckidnapb 082
    woman"We want you to go to her hideout and steal something for us."
    #reuse the same render above
    show sc mckidnapb 083
    woman"And while you're at it, maybe you'll find that flash drive you're looking for."
    #reuse the same render above
    show sc mckidnapb 075
    mc"Okay... But I do have one question."
    #show the MC calmly asking her a question
    show sc mckidnapb 069
    mc"If you know where to find her, then why don't you go after her yourself?"
    #reuse the same render above
    show sc mckidnapb 077
    woman"Because she knows us. She knows how we operate."
    show sc mckidnapb 082
    woman"No doubt she's aware we're coming after her because every time we get close, she's off like a flash in the night."
    show sc mckidnapb 078
    woman"You, however, might have better luck."
    #reuse the same render above
    show sc mckidnapb 083
    woman"You might be our best shot at getting back what she took from us."
    show sc mckidnapb 079
    mc"And why the hell would I help you?"
    show sc mckidnapb 063
    woman"Because you have no other choice."
    #Show the tattoo guy holding the knife across his neck
    show sc mckidnapb 064
    woman"Besides... You want something from her, and so do we."
    #reuse the same render above
    show sc mckidnapb 082
    woman"It's win-win. Assuming you succeed with your task, of course."
    show sc mckidnapb 085
    mc"What if I fail though? What happens then?"
    #reuse the same render above
    show sc mckidnapb 077
    woman"That is NOT an option."
    show sc mckidnapb 075
    mc"(Shit... I was afraid she would say that.)"
    show sc mckidnapb 078
    woman"It's [y_name], right?"
    #reuse the same render above
    show sc mckidnapb 080
    mc"Um..."
    #the MC hesitates, doesn't look at her
    show sc mckidnapb 086
    woman"Let me see here."
    show sc mckidnapb 089
    mc"Hey! That's mine!"
    #the woman holds up his phone and starts reading what is on the screen - make sure that it has the girlie phone case - https://pixhost.to/show/830/484338388_sc-arieltalk-a23.jpg
    show sc mckidnapb 087
    woman"You've had a few missed calls and text messages."
    #she speaks to the MC while going through his phone
    show sc mckidnapb 088
    woman"Seems like whoever was trying to get in contact with you is pretty concerned about your well being."
    #she looks at the MC and speaks while holding his phone
    show sc mckidnapb 089
    mc"(It must be [mc_v_address!c].)"
    #Lucy looks at the MC, mouth closed, holding his phone
    mc"(It's probably because I missed the meeting.)"
    mc"(To hell with that, I have bigger problems right now to deal with.)"
    #reuse the same render above
    show sc mckidnapb 090
    woman"Cute phone case, by the way."
    #she holds up his phone, the back cover facing him as she smiles
    show sc mckidnapb 089
    mc"Oh, well I can explain that."
    show sc mckidnapb 092
    woman"Save it."
    #she looks serious again
    show sc mckidnapb 093
    woman"So... Are you in or are you out?"
    show sc mckidnapb 093a
    mc"(I don't really have much choice here.)"
    #The guy leans in again with a sharp object - reuse the same render above
    mc"(It's the only play I have left, even if it means having to steal two items from this girl instead of one.)"
    #reuse the same render above
    show sc mckidnapb 095
    mc"Sure, I'll do it."
    #he confidently replies
    show sc mckidnapb 088
    woman"Smart answer."
    #reuse the same render above
    show sc mckidnapb 087
    woman"Do this job, and you can consider us even for your intrusion on our turf."
    #reuse the same render above
    show sc mckidnapb 089
    mc"You'll let me go, just like that?"
    show sc mckidnapb 098
    mc"How do I know I can trust you?"
    show sc mckidnapb 097
    woman"You don't."
    show sc mckidnapb 088
    woman"However... I like to consider myself a girl who keeps her word, even if you are part of another group or gang."
    show sc mckidnapb 089
    mc"You know so much about me but I don't know anything about you."
    #reuse the same render above
    mc"I mean, what's your name?"
    #reuse the same render above
    show sc mckidnapb 098
    mc"How can I contact you if something goes wrong?"
    #reuse the same render above
    mc"How do I know that there are no further strings attached even if I do this job for you?"
    #reuse the same render above
    show sc mckidnapb 093
    woman"I'll answer your first question, only."
    #reuse the same render above
    show sc mckidnapb 097
    woman"You can call me Lucy.{w=0.6}{nw}"
    lucy"You can call me Lucy." with Dissolve(0.2)
    ###ADD LUCY TO PERSON OF INTEREST - NOTIFICATION
    $ task_addpoi("Lucy - Gang leader of the Apex Legion",7)
    show sc mckidnapb 098
    mc"Is that your real name?"
    #reuse the same render above
    show sc mckidnapb 088
    lucy"You'll never know for sure."
    #reuse the same render above
    show sc mckidnapb 099
    mc"And what about you, tattoo man? What's your real name?"
    #The MC turns to the tattoo guy
    show sc mckidnapb 100
    guy"Grr..."
    #he grits his teeth
    mc"Okay, forget I asked."
    #the MC holds his hands up as he responds
    show sc mckidnapb 077
    lucy"Our guy, Bruno will meet you there."
    #reuse the same render above
    show sc mckidnapb 102
    lucy"He will give you the full details for what you need to steal back from this girl."
    show sc mckidnapb 075
    mc"Sure, sounds gravy."
    mc"Well, I guess I should be on my way then."
    #the MC goes to leave
    show sc mckidnapb 104a
    lucy"One last thing, [y_name]..."
    #she speaks to the MC as he's about to walk away
    show sc mckidnapb 108
    lucy"Don't even think of trying to cut and run from us."
    #the MC turns around and faces Lucy as she talks to him
    show sc mckidnapb 106
    lucy"Because {b}he{/b} will find you, and my guy won't be anywhere near as hospitable as he's been this evening."
    show sc mckidnapb 107
    lucy"And we'll also come after the rest of your [public_group] and anybody you care about."
    show sc mckidnapb 108
    lucy"That's a promise."
    #she looks serious here
    show sc mckidnapb 109
    lucy"Do I make myself clear?"
    #she has her hands on her hips
    show sc mckidnapb 109a
    mc"Yes, ma'am... I mean, Lucy."
    #he hesitantly replies
    show sc mckidnapb 111
    lucy"Don't forget your phone."
    #she hands him his phone
    show sc mckidnapb 109a
    mc"Oh, thanks."
    #MC replies, embarrassed
    show sc mckidnapb 112
    lucy"All right, you better get going."
    #she has her hand on her hips
    show sc mckidnapb 113a
    lucy"The clock's ticking..."
    stop ambient fadeout 1.0
    #a slightly different render to the one above, with a different facial expression
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep02_01_03_The_MC_calls_Ariel_and_asks_for_a_favour
    #END SCENE

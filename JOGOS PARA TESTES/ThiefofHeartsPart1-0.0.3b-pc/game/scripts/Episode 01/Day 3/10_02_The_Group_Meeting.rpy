label lb_ep01_the_group_meeting1:
    centered "A little later...{w=2.0}{nw}" with dissolve
    show text "A little later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #Show this on the screen
    #screen fades
    #the MC is in his room, changed clothing and exits his room to go downstairs
    play music "sound effects/01/Family Shadows1.mp3" loop fadein 1.0
    scene sc meeting m52
    with dissolve
    mc"(Damn... I could do with an oily breakfast to help cure this hangover)."
    #The MC gets to the bottom of the stairs and sees Victor standing in the living room with arms folded, and the girls sitting on the sofas
    show sc meeting m53
    mc"Uh... What's going on here?"
    show sc meeting m01
    vic"[private_group!c] meeting, [y_name]."
    vic"Take a seat."
    show sc meeting m53
    mc"(Ah, shit... That can't be good.)"
    #The MC sits with Bella and Ariel on the sofa
    show sc meeting m06
    vic"Where were you last night?"
    menu:
        "Be honest":
            show sc meeting m05
            mc"(If I try and lie to him, he's going to know.)"
            mc"(Maybe there's a way to tell him the truth without telling him everything.)"
            show sc meeting m41
            mc"So after work, I went to this club in town."
            show sc meeting m32
            vic"What on earth were you doing at a club last night?"
            show sc meeting m03a
            vic"And after curfew??"
            show sc meeting m10
            b"You were following a lead from the tattoo parlour we visited, right [y_name]?"
            show sc meeting m41
            mc"Uh, yeah..."
            show sc meeting m45
            mc"The guy at the tattoo parlour recommended I go and check out."
            mc"It was a lead I felt was worth following up."
        "Act clueless":
            show sc meeting m45
            mc"What do you mean?"
            show sc meeting m32
            vic"Don't play dumb with me."
            vic"You broke curfew."
            show sc meeting m47
            mc"I worked late at the gym."
            show sc meeting m03
            vic"Yeah, and you should have been home by midnight."
            show sc meeting m06
            vic"So I'll ask you again. Where were you?"
            show sc meeting m10
            b"You were following a lead from the tattoo parlour we visited, right [y_name]?"
            show sc meeting m41
            mc"Uh, yeah..."
            show sc meeting m45
            mc"There was this club in town that the guy at the tattoo parlour recommended I go and check out."
    show sc meeting m06
    vic"And what did you find?"
    show sc meeting m49
    mc"Um, nothing... Initially."
    show sc meeting m45
    mc"But a little while after, a girl I spoke to happened to have that exact same tattoo."
    show sc meeting m06
    vic"And?"
    show sc meeting m45
    mc"She told me the name of the gang attached to it."
    mc"It's something called the {i}Apex Legion{/i}."
    # or mc"It's some gang called the {i}Apex Legion{/i}."
    show sc meeting m47
    mc"Have you heard of it?"
    show sc meeting m05
    vic"Hmm..."
    show sc meeting m06
    vic"No, I can't say that I have."
    vic"Did she say anything else?"
    show sc meeting m45
    mc"Yeah... Getting that tattoo was part of a dare that she lost when she used to live here in town."
    show sc meeting m06
    vic"Do you know where she lives now?"
    show sc meeting m49
    mc"I have no idea. Her name is Mikayla."
    show sc meeting m48
    mc"(If that's even her real name.)"
    show sc meeting m45
    mc"But the gang seems like they are definitely based here."
    show sc meeting m06
    vic"So you met some random girl in a club, who you say had the same tattoo as the girl we're looking for."
    vic"You don't know who she is, where she's from or how to get in contact with her."
    show sc meeting m03
    vic"Is that what you're telling me?"
    show sc meeting m45
    mc"Yeah, that's pretty much it."
    show sc meeting m02
    vic"And let me guess, you went back to her place and had some fun even though you should have come straight back here, didn't you?"
    vic"And how come you didn't answer when I tried to call you last night?"
    show sc meeting m49
    mc"I um... I was kind of robbed."
    show sc meeting m03a
    with vpunch
    vic"Are you fucking kidding me??"
    vic"What did they take?"
    show sc meeting m45
    mc"My wallet... My phone."
    show sc meeting m33
    vic"I can't believe this."
    show sc meeting m32
    vic"I can't trust you to do a simple damn thing right."
    show sc meeting m26
    v"[vic_name], that's enough."
    v"[y_name] has another lead. Why don't we focus on that instead?"
    show sc meeting m35a
    a"I could run a check on that name to see if anything comes up."
    show sc meeting m18
    a"And I'll do a trace on his phone, to see if I can find its exact location."
    show sc meeting m41
    mc"What about the contact numbers on it?"
    show sc meeting m35a
    a"I have a system that backs up everyone's contact details daily, even when you're not here."
    a"It allows me to transfer all those numbers to a new phone."
    show sc meeting m35b
    a"As for your bank cards, they were all untraceable and had a minimal debit amount on them."
    a"So I can replace them too."
    #Bella addresses Victor
    show sc meeting m13
    b"And I have plenty of backup phones. [y_name] can have one of them."
    show sc meeting m15
    b"At least until we know if your old one can be recovered."
    #The MC addresses Victor
    show sc meeting m45
    mc"I still have time, [mc_vic_address]. You gave me seventy-two hours, remember?"
    show sc meeting m32
    vic"Yeah, and at this rate and with the amount of time you've already wasted..."
    show sc meeting m03a
    vic"Going out partying with random girls, we're no closer to getting that flash drive back since you first lost it!"
    show sc meeting m50
    v"Just give him some more time, [vic_name]."
    show sc meeting m07
    vic"So you all think that this is still worth pursuing?"
    show sc meeting m08
    vic"Even despite the incredibly weak lead that [y_name] has come back with?"
    show sc meeting m26
    v"Yes, I do."
    #show Bella and Ariel
    show sc meeting m12
    b"And so do we."
    #Victor seems unimpressed but surprised
    show sc meeting m07
    vic"Fine."
    vic"If this is a group decision, then it looks like I'm outnumbered."
    vic"Very well then."
    show sc meeting m08
    vic"If you want to work on this with [y_name], then you better get on it."
    show sc meeting m06
    vic"I won't be here for most of the day as I have to head out again."
    show sc meeting m37
    vic"I have to pick up a client shortly and then I have a function tonight which I have to be at."
    show sc meeting m26a
    v"What time will you be home?"
    show sc meeting m37
    vic"Late. That's all you need to know."
    vic"But that doesn't mean any of you should be out after nine o'clock tonight."
    vic"Capiche?"
    show sc meeting m11
    b"Yes, we all understand."
    show sc meeting m37
    vic"I'm going to go get ready for work."
    show sc meeting m44
    vic"But the next time we have a meeting like this, you better have something more than a gang name."
    #Victor leaves
    show sc meeting m39
    b"What the hell are we going to do?"
    show sc meeting m15
    b"We don't have much to go on.  And we don't even know if that gang name is real or not."
    show sc meeting m23
    v"Real or not, no one gives up on the [private_group] remember?"
    show sc meeting m16
    a"And what if we don't have anything to present to [mc_vic_address] the next time he calls us for one of these meetings?"
    show sc meeting m23
    v"Then we give him something else."
    show sc meeting m31
    v"Don't worry, we'll figure this out. Together."
    #The girls look unsure
    show sc meeting m23
    v"Girls, would you please excuse me and [y_name]?"
    stop music fadeout 2.0
    show sc meeting m13
    b"Sure thing, [mc_v_address]."
    show sc meeting m55
    b"Let's go, [a_name]."
    #The girls leave the main room
    play music "sound effects/01/Family Shadows2.mp3" loop fadein 1.0
    show sc meeting m28
    v"[y_name], I want you to tell me everything that happened last night."
    v"But not now."
    show sc meeting m42
    mc"Okay... When?"
    show sc meeting m28
    v"Once [vic_name] leaves, come to my room."
    v"We can talk in private as I'm sure that you don't want [b_name] and [a_name] eavesdropping on our conversation."
    show sc meeting m30
    mc"Yeah, good idea."
    show sc meeting m31
    v"I'll see you shortly, sweetheart."
    #She kisses him on the forehead
    play sound "sound effects/01/mwah_short_kissing_sound_effect5.mp3"
    show sc meeting m51
    v"Mwah!"
    #The MC watches Vivian leave and go up the stairs
    stop sound fadeout 1.0
    show sc meeting m56
    mc"(Just when I think my life is going to shit, she always seems to have my back...)"
    #screen goes blank
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_talks_with_Vivian1


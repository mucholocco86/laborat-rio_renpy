label scene102_2:
    play music "river.mp3" fadein 1.0 loop
    if maia_pussy_sex > 0:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
    if maia_anal_sex > 0:
        $ maia_anus_virgin = False
        $ maia_virgin = False
    if maia_pregnant:
        $ maia_pussy_virgin = False
        $ maia_virgin = False

    scene 102_s2 with Dissolve(1.5)
    ""
    scene 102_s3 with Dissolve(1.0)
    empathy "Get your shit together. There are people depending on you. You're still alive, so go on, finish the job."
    if maia_anal_sex > 0:
        $ maia_anus_virgin = False
        $ maia_virgin = False
    if maia_pussy_sex > 0:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
    scene 102_s4 with Dissolve(1.3)
    reham "Should we... talk to him?"
    reham "He's been staring blankly for nearly an hour now."
    scene 102_s5 with dissolve
    alex "Yeah. I noticed."
    alex "Something happened out there. I'm sure of it."
    scene 102_s7 with Dissolve(1.0)
    reham "Can you talk to him, Maia? You're the closest to him."
    scene 102_s6 with dissolve
    m "[mc]'s fine."
    scene 102_s7 with dissolve
    alex "Do your eyes work? Because that doesn't look like fine to me."
    scene 102_s8 with dissolve
    m "As if you care, you... you murderer!"
    scene 102_s9 with dissolve
    alex "What did you—!"
    scene 102_s8 with dissolve
    m "That's right, I know what you used to do now."
    scene 102_s9 with dissolve
    if mc_console_maia:
        alex "You're not one to talk. You've killed someone too... or did you already forget that?"
        scene 102_s8 with dissolve
        m "That's different!"
        scene 102_s9 with dissolve
        alex "And what makes you think what I've done isn't different too?"
    else:
        alex "You're not one to talk. You've killed someone too."
        alex "{i}And{/i} it looks like he doesn't care about you either. I've seen how he avoids you."
        scene 102_s8 with dissolve
        m "H-He saved me!"
        scene 102_s9 with dissolve
        alex "So? That doesn't necessarily mean it's love."
    
    reham "Stop fighting you two, I'll go."
    alex "*sigh* I'm coming with you."
    scene 102_s10 with Dissolve(1.0)
    reham "Go inside, Maia."
    m "..."

    scene 102_s11 with Fade(1.3,1.0,1.0)
    if mc_harem_reham:
        reham "Master...?"
    else:
        reham "[mc]...?"
    reham "Is everything alright? I've never seen you this... distant before."

    scene 102_s13 with dissolve
    mc "Hmm? Oh. I'm fine. Sorry if I'm worrying you."
    scene 102_s12 with dissolve
    alex "Come on. What happened out there? We're a team, remember? You can talk to us."
    scene 102_s13 with dissolve
    mc "I appreciate the concern, both of you. Really. But I'm fine. Honest."
    reham "Hmm..."
    mc "But you're right, this isn't like me. Moping around like this is useless, there's lots we need to do."

    if not mc_execute_kat and not mc_life_kat:
        mc "Let's go over our next move. Kat agreed to help me, though... I left rather abruptly."
        mc "Alex, after I'm done with Diana, I need you to check in on her. Make sure she's doing alright. And her friend Ava too."
        scene 102_s12 with dissolve
        alex "Got it."
    else:
        mc "Let's go over our next move. Now that I have a prosthetic, I need to visit Diana. See if she's picked up anything useful from any drunken lords."

    scene 102_s11 with dissolve
    reham "Remind me again—why are we relying on information from a brothel?"
    scene 102_s13 with dissolve
    if mc_agree_alex:
        mc "I need to understand Avery's plans if I'm going to rescue the princess. Right now, I don't see how we pull this off without knowing more."
    else:
        mc "I need intel on Avery's next moves before we commit to anything. It'd be a disaster to learn the princess's execution date is tomorrow when we thought we had weeks."
    scene 102_s15 with Dissolve(1.0)
    reham "And what if Diana knows nothing? You said it's a brothel, not exactly where distinguished people gather."
    scene 102_s14 with dissolve
    mc "That's exactly the point. No honorable lord would visit a place like that. Only the corrupt ones—the ones who talk when their tongues are loose."
    mc "Diana's sharp. I'm willing to bet she's heard a thing or two."
    scene 102_s15 with dissolve
    alex "Makes sense to me. I can take you close to the stables again, same as last time."
    scene 102_s14 with dissolve
    mc "No need. I've got my horse now. Oh, and a sword too."
    scene 102_s16 with vpunch
    alex "A sword?! I can take it, right?"
    scene 102_s17 with dissolve
    reham "*chuckles* Your eyes light up after hearing {i}that?{/i}"
    scene 102_s18 with dissolve
    call screen scene102_choice01 with dissolve

label scene102_choice01_op1:
    mc "Go ahead. I've already got one."
    scene 102_s16 with vpunch
    alex "Ha! Thank you!"
    scene 102_s18 with dissolve
    jump scene102_3

label scene102_choice01_op2:
    $ mc_gave_sword_reham = True
    $ alex_love -= 10
    mc "I'll give it to Reham."
    scene 102_s19 with dissolve
    reham "Wh— Huh? Me? I... Thank you, [mc], but I don't really know how to use a sword..."
    scene 102_s22 with dissolve
    alex "Her?! Seriously? Look at her! She's never held anything longer than a kitchen knife in her life."
    scene 102_s21 with dissolve
    reham "That's... actually true, but you didn't have to sound quite so dismissive about it."
    scene 102_s19 with dissolve
    reham "Still, it would be wasted on me, [mc]. Better in her hands. And honestly? *giggles* Now probably isn't the time for sword lessons."
    scene 102_s23 with dissolve
    mc "Hmm. Fair enough. I guess it's yours, then."
    scene 102_s22 with dissolve
    alex "{i}'Then'?{/i} I'm the second choice here? *scoff*"
    scene 102_s23 with dissolve
    jump scene102_3

label scene102_3:
    scene 102_s26 with Fade(1.3,1.0,1.0)
    play sound "sound_effects/sword/sword_swing1.mp3"
    perception "Her face twists into a menacing grin as she grabs the sword and begins swinging it wildly through the air."
    scene 102_s25 with Dissolve(1.4)
    play sound "sound_effects/unsheathe2.mp3"
    alex "This is incredible! A master craftsman made this, no doubt. The weight, the sharpness..."
    scene 102_s24 with dissolve
    mc "The same one who made my prosthetic, actually."
    scene 102_s25 with dissolve
    alex "Ohh? I can feel it. Don't worry, I'll take good care of it."
    scene 102_s24 with dissolve
    scene 102_s27 with Dissolve(1.4)
    mc "See that you do. I'll find you something too, when I can."
    scene 102_s29 with dissolve
    reham "Ahaha... Let's just... drop the sword idea for me. For now."
    scene 102_s27 with dissolve
    if mc_want_help_serena:
        mc "Oh, and I also promised someone my help. I'll need to do that first before meeting Diana."
        scene 102_s28 with dissolve
        alex "You're piling a lot onto your shoulders lately. Why not let me handle something with you?"

        scene 102_s27 with dissolve
        if not mc_execute_kat and not mc_life_kat:
            mc "No. You've got Kat to deal with."
        else:
            mc "No. I need you here to protect Maia and Reham."
        
        scene 102_s28 with dissolve
        alex "*sigh* ...Fine. You gave me a sword so I can't really complain."
        scene 102_s29 with dissolve
        reham "You don't have to worry about us quite so much, you know. If Alex is needed elsewhere, we can manage."
        scene 102_s28 with dissolve
        alex "At least tell me what you're walking into. If something happens, I need to know where to start looking."
        scene 102_s27 with dissolve
        mc "Breaking into a lord's manor and destroying documents that prove ownership over a bunch of slaves."
        scene 102_s28 with dissolve
        alex "Ah. I see. Very well."
        scene 102_s31 with vpunch
        alex "Is that what you wanted to hear?!"
        scene 102_s30 with dissolve
        mc "What?"
        scene 102_s31 with dissolve
        alex "What do you mean 'what'!? Don't give me that, [mc]! We have much bigger problems than playing vigilante!"
        scene 102_s30 with dissolve
        mc "This is important. I'm making allies. Besides, I'm not about to ignore something like this. It isn't all that different from what's happening to your brother."
        scene 102_s32 with dissolve
        reham "*sigh* This has 'disaster' written all over it."
        scene 102_s30 with dissolve
        mc "The woman I'm helping is strong. She uhh... subdued me without breaking a sweat. If we do her this favor, she'll owe us."
        scene 102_s31 with dissolve
        alex "Ngh... If she's really as strong you say, then maybe it's worth it. But if you're doing this today, then you'd better come back tomorrow. No delays this time."

    scene 102_s30 with dissolve
    mc "Now then... I'll head out."
    scene 102_s33 with dissolve
    reham "But you haven't slept at all!"
    scene 102_s34 with dissolve
    mc "I know. For some reason... *chuckles* I don't feel tired."
        
    scene 102_s33 with dissolve
    if mc_harem_reham:
        reham "Master... you really need to take care of yourself. I appreciate everything you're doing for us, but not at your own expense."
    else:
        reham "[mc]... you really need to take care of yourself. I appreciate everything you're doing for us, but not at your own expense."

    if mc_harem_reham:
        scene 102_s33 with dissolve
        reham "As your servant, I insist you take a break. I'll even pamper you thoroughly if that's what it takes."
        scene 102_s34 with dissolve
        alex "Ugh..."
        mc "*chuckles* I—"

    jump scene103

label scene103:
    stop music fadeout 1.0 
    scene 103_s1 with Dissolve(1.0)
    perception "Heavy footsteps crunch against the grass nearby... someone's coming."
    play music "tense/scary_music.mp3" fadein 1.0 loop
    mc "..."
    alex "[mc]?"
    logic "Two sets of footsteps. One masks the other. More than one person out there."
    scene 103_s2 with dissolve
    mc "Ambush!"
    scene 103_s1 with dissolve
    reham "Huh?! W-Where?"
    scene 103_s2 with dissolve
    mc "Inside the cabin. Now. And stay away from windows."
    scene 103_s1 with dissolve
    reham "On it!"
    scene 103_s2 with dissolve
    mc "Alex—"
    scene 103_s3 with dissolve
    play sound "sound_effects/unsheathe2.mp3"
    alex "I know."
    scene 103_s4 with Dissolve(1.3)
    mc "..."
    alex "..."
    scene 103_s5 with Dissolve(1.0)
    Millicent_ "Impressive. Most people wouldn't have noticed us so quickly. Usually it's too late by then."
    scene 103_s6 with dissolve
    alex "Where are you? Show yourself!"
    scene 103_s8 with dissolve
    mc "There."
    alex "Who the hell are you?!"
    call screen scene103_choice01 with dissolve

label scene103_choice01_op1:
    $ mc_scared_milesent = True
    scene 103_s9 with dissolve
    Millicent_ "I'm your—"
    scene 103_s8 with dissolve
    mc "Get away from that roof! Now!"
    scene 103_s9 with dissolve
    Millicent_ "You're at a disadvantage here. You can't order m—"
    scene 103_s7 with vpunch
    mc "If you so much as touch a single hair on anyone in that cabin, I'll tear your head off!"
    scene 103_s10 with Dissolve(1.0)
    Millicent_ "...Alright, alright. I wasn't planning to hurt anyone anyway. So... calm down."
    scene 103_s11 with Dissolve(1.0)
    play sound "sound_effects/clothing_rustle.mp3"
    scene 103_s11 with vpunch
    Millicent_ "Hoop!"
    scene 103_s12 with Dissolve(1.0)
    alex "Start talking."
    scene 103_s13 with dissolve
    Millicent_ "*ahem* As I was trying to say, before the angry one started threatening me—I'm your savior."
    Millicent_ "You and the girl inside. I dragged you both down that mountain on my sled."
    scene 103_s14 with dissolve
    mc "..."
    scene 103_s13 with dissolve
    Millicent_ "Not even a 'thank you'?"
    jump scene103_2

label scene103_choice01_op2:
    scene 103_s9 with dissolve
    Millicent_ "I'm your savior."
    scene 103_s8 with dissolve
    alex "Savior?"
    scene 103_s9 with dissolve
    Millicent_ "I helped your friend when he was on the brink of death, along with that girl inside."
    scene 103_s8 with dissolve
    mc "..."
    scene 103_s9 with dissolve
    Millicent_ "Don't trust me?"
    scene 103_s8 with dissolve
    alex "Hard to do that when you're not even facing us."
    scene 103_s9 with dissolve
    Millicent_ "Very well."
    scene 103_s11 with Dissolve(1.0)
    play sound "sound_effects/clothing_rustle.mp3"
    scene 103_s11 with vpunch
    Millicent_ "Hoop!"
    scene 103_s12 with Dissolve(1.3)
    jump scene103_2

label scene103_2:
    scene 103_s12 with dissolve
    alex "{size=30}What should we do? She's dangerous, but... I'm not sensing any real malice.{/size}"
    scene 103_s13 with dissolve
    Millicent_ "Would you both relax? I don't even have a weapon on me."
    scene 103_s14 with dissolve
    sensation "You sense an intense magical aura radiating from her, so strong that the hair on your arms stands on end."
    mc "You're a mage."
    scene 103_s13 with dissolve
    Millicent_ "...Heh. I suppose I can't fool someone like you. Either way, I'm not here to fight."
    Millicent_ "To tell you the truth, I'm here to ask for your... assistance, [mc]."
    scene 103_s14 with dissolve
    mc "How do you know my name?"
    scene 103_s15 with Dissolve(1.0)
    play sound "sound_effects/grass.mp3"
    thulkin "I think we're past that now. You're the talk of the city, after all."
    alex "Another one?!"
    mc "(Shit! I Forgot!) Protect my back, Alex."
    scene 103_s16 with Dissolve(1.0)
    thulkin "You've never been one to ask politely, were you, sister?"
    scene 103_s17 with dissolve
    Millicent_ "I wanted to see if they were actually worth asking first. He seems aware enough. Not sure about his strength, though. That's on you."
    scene 103_s16 with dissolve
    thulkin "*laughs* Fair enough."
    thulkin "I don't see you holding a weapon, [mc]. Are you so confident in your strength... or just foolish?"
    scene 103_s17 with dissolve
    mc "Neither. I'm just wondering why two strangers are standing in front our cabin."
    Millicent_ "'Our cabin'? Please."
    scene 103_s18 with Dissolve(1.0)
    thulkin "My sister told you. You'll be helping us... after you spar with me, of course."
    scene 103_s19 with dissolve
    mc "I don't remember agreeing to any of that."
    scene 103_s18 with dissolve
    thulkin "Think of the bigger picture, [mc]! Remember what I told you at the smithy? There's a goblin tribe not too far from here. You're basically in walking distance to them."
    scene 103_s88 with dissolve
    alex "Wait, you know this man?"
    scene 103_s20 with dissolve
    mc "Barely. I met him once."
    scene 103_s18 with dissolve
    thulkin "After doing some forced reconnaissance, it turns out there are way more of them than we thought."
    thulkin "Don't get me wrong—a real challenge only makes my blood boil hotter."
    thulkin "But Millicent pointed out that if we want to wipe them out for good, none can escape and start a new tribe elsewhere. That means we need numbers."
    scene 103_s88 with dissolve
    Millicent "Hey! Don't go throwing my name around like that, you idiot!"
    scene 103_s19 with dissolve
    mc "If you need my help so badly, why the sparring?"
    scene 103_s18 with dissolve
    thulkin "I need to know if you're really as strong as they say. Can't risk you dying out there and leaving your people without you."
    thulkin "I'm not leaving until we fight, [mc]. Simple as that."
    stop music fadeout 1.0 
    scene 103_s21 with Dissolve(1.0)
    play music "angry/hard_advent.mp3" fadein 1.0 loop
    m "Hnng—!"
    mc "Maia?!"
    scene 103_s22 with Dissolve(0.3)
    play sound "sound_effects/woosh1.mp3"
    scene 103_s22 with vpunch
    m "Haaagh!"
    scene 103_s27 with Dissolve(1.0)
    perception "You glance back. Maia stands in the doorway, breathing hard from the effort of throwing you the sword."
    thulkin "*laughs* Amusing! So this is the true love they always talk about in stories!"
    scene 103_s24 with Dissolve(1.0)
    if mc_want_help_serena:
        alex "Hold on, [mc]. Think about this—if we help them, maybe they help us in return. We could use more allies for our cause. You're doing the same for those slaves afterall."
    else:
        alex "Hold on, [mc]. Think about this—if we help them, maybe they help us in return. We could use more allies for our cause."
    Millicent "Your {i}cause?{/i} You should know that you're the one who owes us, not the other way around. Your friend would be dead if I hadn't found him."
    reham "I really don't like this, [mc]. What if you get injured again? I say we don't indulge them."
    scene 103_s23 with dissolve
    thulkin "I'm not leaving without you. There are innocent lives at stake. Trust me, I know. I will not make the same mistake again."
    scene 103_s25 with dissolve
    minthra "Go with them. I will extend my power to you. You can influence the goblin leader, bend them to your will. Killing them would be a waste. Let them ravage the plains in your name instead."
    mc "Hnnn!"
    alex "[mc]?!"
    scene 103_s26 with dissolve
    mc "It's nothing."
    scene 103_s25 with dissolve
    scene 103_s31 with Dissolve(1.0)
    call screen scene103_choice02 with dissolve

label scene103_choice02_op1:
    $ mc_agree_help_thulkin = True
    if mc_asked_maia_opinion:
        mc "I got Maia backing me up, I can't turn you down now."
        scene 103_s31 with Dissolve(1.0)
    else:
        mc "Fine. We'll spar."
    mc "But understand something first. If I'm going to help you, you help me in return."
    Millicent "Did you not hear what I just—"
    scene 103_s32 with dissolve
    thulkin "Very well!"
    scene 103_s31 with dissolve
    Millicent "Thulkin!"
    scene 103_s32 with dissolve
    thulkin "It's only natural for warriors to help each other! You have a deal, my friend. BUT..."
    thulkin "...only if you win."
    scene 103_s31 with dissolve
    mc "Then I'll show you."
    scene 103_s32 with dissolve
    thulkin "*laughs* That's exactly what I wanted to hear!"
    thulkin "Don't worry, this won't take long."
    scene 103_s33 with Dissolve(1.0)
    alex "Hey... Maybe don't sound so confident. You don't know who you're dealing with. I mean... look at him."
    scene 103_s34 with dissolve
    Millicent "Eh. If he loses that easily, he wouldn't have been useful to you anyway."
    scene 103_s35 with dissolve
    alex "Shut up."
    scene 103_s32 with Dissolve(1.0)
    thulkin "Enough talking! Everyone not involved should move out of our way."
    thulkin "And you, [mc]. Fight as if you intend to kill."
    jump scene103_4

label scene103_4:
    scene 103_s36 with Dissolve(1.0)
    perception "He steps forward, his posture loose but balanced like a predator testing the ground. He hefts his axe, rolling his shoulders."
    thulkin "Whenever you're ready."
    scene 103_s37 with Dissolve(1.0)
    play sound "sound_effects/woosh2.mp3"
    mc "HGAHHHH!"
    scene 103_s38 with Dissolve(0.3)
    play sound "sound_effects/sword_clash.mp3"
    scene 103_s38 with vpunch
    perception "You lunge forward. Steel meets steel with a sharp clang that echoes through the clearing."
    thulkin "*laughs* Good! Good!"
    scene 103_s39 with Dissolve(0.3)
    play sound "sound_effects/slash02.mp3"
    scene 103_s39 with vpunch
    thulkin "HANHG!"
    scene 103_s40 with Dissolve(0.8)
    play sound "sound_effects/body/clothes1.mp3"
    sensation "His swing carries the weight of someone who has fought for decades. Your feel your arms stinging from the impact."
    mc "(He's fast but I can... I can read his moves!"
    scene 103_s41 with Dissolve(0.6)
    thulkin "HNGGHHNN!"
    scene 103_s42 with Dissolve(0.3)
    play sound "sound_effects/sword/sword_swing1.mp3"
    scene 103_s42 with vpunch
    perception "You catch an opening—a split second where his weight shifts too far forward. You twist, redirecting his strike past your shoulder."
    scene 103_s43 with Dissolve(1.0)
    thulkin "Whoa! Almost got me there."
    scene 103_s44 with dissolve
    mc "You're not taking me seriously."
    scene 103_s43 with dissolve
    thulkin "What makes you say that?"
    scene 103_s44 with dissolve
    mc "Your axe... You're holding it with one arm."
    scene 103_s45 with dissolve
    thulkin "You're also one-armed, aren't you? In a fight, I don't take advantages I wouldn't want used against me. I fight fair even if it kills me."
    mc "That's... honorable. But you don't have to. This isn't just metal, it's enchanted. I can use it as if it was my real hand."
    thulkin "*chuckles* Would you look at that! Very well then."
    scene 103_s46 with dissolve
    perception "He adjusts his grip, both hands now firmly on the haft. His stance shifts, becoming lower, more solid."
    thulkin "Two hands it is."
    scene 103_s47 with Dissolve(1.0)
    play sound "sound_effects/woosh2.mp3"
    perception "He explodes forward with a speed his hulking frame shouldn't allow. The axe comes down in a devastating arc."
    thulkin "This is how you do a lunging attack!"
    scene 103_s48 with Dissolve(0.3)
    play sound "sound_effects/sword/hard_slash1.mp3"
    scene 103_s48 with vpunch
    sensation "You raise your sword just in time. The impact sends a shockwave through your entire body, rattling your teeth."
    mc "Nghnn!"
    thulkin "*laughs* Impressive! Even a mighty ogre would crumple under this strike!"
    logic "Slide his axe to the side. Use his momentum against him. Surprise him with a punch. The same way Adam did to you back then."
    empathy "But he said he fights fair. He's honoring that so shouldn't you do the same?"
    call screen scene103_choice03 with dissolve

label scene103_choice03_op1:
    scene 103_s49 with Dissolve(0.3)
    play sound "sound_effects/punch3.mp3"
    scene 103_s49 with vpunch
    perception "You twist sharply, sliding his axe. Before he can recover, your fist connects with his cheek."
    scene 103_s50 with Dissolve(0.5)
    thulkin "Nghnn!"
    scene 103_s51 with Dissolve(0.3)
    play sound "sound_effects/bodydrop2.mp3"
    scene 103_s51 with vpunch
    perception "His body flys away hitting a tree. Instead of anger, his face splits into a wide, approving grin."
    Millicent "What in the world?! H-How did you—"
    scene 103_s52 with Dissolve(1.0)
    mc "..."
    alex "[mc]! That was incredible! I knew you were capable but... I didn't think you were {i}this{/i} strong!"
    scene 103_s53 with dissolve
    mc "I... I didn't know either."
    scene 103_s52 with dissolve
    scene 103_s55 with Dissolve(1.0)
    thulkin "HA! You are a fighter! Tricky, but I like it!"
    scene 103_s54 with dissolve
    mc "You said you fight fair. I don't. I do whatever it takes to survive."
    scene 103_s55 with dissolve
    thulkin "I don't expect anyone to follow my rules. All's fair in a real fight, my friend. I'm just glad you didn't knock a tooth out. Or my entire head, for that matter."
    scene 103_s54 with dissolve
    jump scene103_5

label scene103_choice03_op2:
    $ mc_fought_thulkin_fair = True
    mc "..."
    scene 103_s56 with Dissolve(0.3)
    play sound "sound_effects/sword/unsheathe3.mp3"
    scene 103_s56 with Dissolve(0.3)
    mc "NhnnnnAHHHHHHH!"
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if not mc_karma == 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    sensation "A wild surge of fierce and electric power flood your muscles, and you shove back hard, sending Thulkin staggering backward."
    thulkin "Whoa!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 103_s57 with Dissolve(0.3)
    play sound "sound_effects/bodydrop.mp3"
    scene 103_s57 with vpunch
    mc "Don't move."
    scene 103_s89 with dissolve
    thulkin "..."
    scene 103_s58 with dissolve
    thulkin "Well. Damn."
    thulkin "I was hoping for a fight. Instead I got a humiliation."
    scene 103_s89 with dissolve
    Millicent "That shouldn't even be possible! Were you going easy on him?"
    scene 103_s58 with dissolve
    thulkin "Not at all. *chuckles* I'm as surprised as you are."
    scene 103_s89 with dissolve
    scene 103_s61 with Fade(1.3,1.0,1.0)
    stop music fadeout 3.0 
    if mc_agree_help_thulkin:
        thulkin "You have my respect, [mc]. And my axe. It would be a great honor to fight along side you."
    else:
        thulkin "You have my respect, [mc]. A shame you don't want to help us, it would've been a great honor to fight along side you."
    jump scene103_5

label scene103_choice02_op2:
    if mc_asked_maia_opinion:
        scene 103_s27 with dissolve
        mc "Sorry, Maia. But he came here uninvited. And now he's demanding a fight?"
        scene 103_s31 with Dissolve(1.0)
    else:
        mc "You came here uninvited. And now you're demanding a fight?"
    mc "I have more important things to do. Leave."
    scene 103_s32 with dissolve
    thulkin "If you don't fight me, then I'll keep standing here."
    scene 103_s31 with dissolve
    mc "That's it? I can just ignore you."
    scene 103_s32 with dissolve
    thulkin "Hmm. In that case..."
    play sound "sound_effects/body/scream.mp3"
    scene 103_s59 with vpunch
    thulkin "*inhale* AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
    sensation "The sound pierces your ears, loud enough to echo for miles."
    scene 103_s60 with dissolve
    alex "Make him stop! He'll give away our position!"
    scene 103_s59 with dissolve
    mc "Fine! Fine! Just stop!"
    scene 103_s31 with dissolve
    mc "Look, I'll fight you but as I said. I have more urgent things on my mind right now."
    scene 103_s32 with dissolve
    thulkin "...Hmph."
    thulkin "Fair enough."
    scene 103_s31 with dissolve
    Millicent "Wait, that's it? You're just giving up?!"
    scene 103_s32 with dissolve
    thulkin "He made his choice. No point forcing a man who doesn't want to help."
    thulkin "Besides... I can see it in his eyes. He's endured a lot, and time is short for him. I respect that."
    scene 103_s31 with dissolve
    Millicent "*sigh* Fine. But if some runaway goblin ends up slaughtering villagers later, don't say we didn't warn you."
    scene 103_s32 with dissolve
    thulkin "Come, [mc]! Show me what you got!"
    scene 103_s31 with dissolve
    jump scene103_4

label scene103_choice02_op3:
    $ mc_asked_maia_opinion = True
    $ maia_love += 10
    scene 103_s27 with Dissolve(1.0)
    mc "I've heard Alex and Reham. What about you, Maia?"
    scene 103_s28 with dissolve
    m "M-Me? I... I would rather leave this up to you, [mc]..."
    scene 103_s27 with dissolve
    mc "Come on. I want to know what {i}you{/i} think most of all."
    scene 103_s28 with dissolve
    m "What I think?"
    scene 103_s29 with dissolve
    m "...Do it! Show that man who's stronger!"
    if mc_told_maia_ogre:
        m "Beat him up like you beat that ogre!"
    scene 103_s30 with dissolve
    mc "*laughs* There she is."
    call screen scene103_choice02 with dissolve

label scene103_5:
    if mc_agree_help_thulkin:
        if mc_fought_thulkin_fair:
            scene 103_s61 with dissolve
            thulkin "Now then, shall we head out?"
        else:
            scene 103_s61 with Fade(1.0,0.5,0.5)
            thulkin "Hhngg! Now then, shall we head out?"
        scene 103_s72 with Dissolve(1.0)
        play music "river.mp3" fadein 2.0 loop
        alex "Now!?"
        scene 103_s73 with dissolve
        thulkin "Why delay? Best to quench the evil before it festers."
        scene 103_s62 with Dissolve(1.0)
        mc "How far is it? The golbin tribe."
        Millicent "Close to where I found you. The distance isn't the problem, it's the climb... Ugh."
        scene 103_s61 with dissolve
        thulkin "Clearing out the tribe won't take long, not with you both with us."
        scene 103_s74 with Dissolve(1.0)
        alex "Good. I've been itching to use this. I felt like I was getting rusty so this will be good training."
        scene 103_s75 with Dissolve(1.0)
        Millicent "Hmm... That sword of yours. Such elegant craftsmanship."
        scene 103_s76 with dissolve
        alex "You know your weapons well."
        scene 103_s75 with dissolve
        Millicent "Thank you. I'm Millicent, a mercenary mage. In case my brother hasn't already made that known to the entire forest."
        scene 103_s76 with dissolve
        alex "Alex."
        scene 103_s75 with dissolve
        Millicent "That's... all?"
        scene 103_s76 with dissolve
        alex "Yes."
        scene 103_s75 with dissolve
        Millicent "*chuckles* Alright, keep your secrets. Mysterious type, aren't you?"
        scene 103_s77 with Dissolve(1.4)
        reham "Take care of yourselves and don't worry about us, [mc]."
        scene 103_s78 with dissolve
        thulkin "Hehe~"
        scene 103_s79 with Dissolve(1.0)
        mc "Uhh...?"
        scene 103_s80 with dissolve
        thulkin "These people really care for you. I can feel it in my bones."
        if maia_love >= 60:
            thulkin "Especially that freckled one."
        else:
            thulkin "Especially that freckled one... though I sense you don't feel the same way about her."
        scene 103_s79 with dissolve
        mc "You can tell that sort of thing?"
        scene 103_s80 with dissolve
        thulkin "You wound me, [mc]! Just because I look like this doesn't mean I don't have emotions."
        thulkin "Love flows through these muscles just as much as power does!"
        scene 103_s79 with dissolve
        mc "I see..."
        scene 103_s80 with dissolve
        thulkin "Now then! It's time to hit the road."
        scene 103_s79 with dissolve
        call screen scene103_choice05 with dissolve

    else:
        if mc_fought_thulkin_fair:
            scene 103_s61 with dissolve
            thulkin "Regardless. I shall respect your word."
        else:
            scene 103_s61 with Fade(1.0,0.5,0.5)
            thulkin "Hhngg! You fought well. I will respect your word."
        thulkin "It's time to leave, sister. If we want to wipe out that tribe on our own, we simply have to fight harder."
        scene 103_s62 with dissolve
        Millicent "..."
        call screen scene103_choice04 with dissolve

label scene103_choice04_op1:
    $ mc_agree_help_thulkin = True
    mc "Wait. I changed my mind. I'll help you out."
    scene 103_s63 with vpunch
    thulkin "*laughs* Hah! I knew you had a good heart! Your troubles, my troubles... doesn't matter. You'll help anyone who needs it!"
    scene 103_s64 with dissolve
    mc "Thanks."
    scene 103_s63 with dissolve
    thulkin "Shall we head out, then?"
    scene 103_s72 with Dissolve(1.0)
    alex "Now!?"
    scene 103_s73 with dissolve
    thulkin "Why delay? Best to quench the evil before it festers."
    scene 103_s62 with Dissolve(1.0)
    mc "How far is it? The golbin tribe."
    Millicent "Close to where I found you. The distance isn't the problem—it's the climb... Ugh."
    scene 103_s61 with dissolve
    thulkin "Clearing out the tribe won't take long, not with you both with us."
    scene 103_s74 with Dissolve(1.0)
    alex "I've been itching to use this. I felt like I was getting rusty so this will be good training."
    scene 103_s75 with Dissolve(1.0)
    Millicent "Hmm... That sword of yours. Such elegant craftsmanship."
    scene 103_s76 with dissolve
    alex "You know your weapons well."
    scene 103_s75 with dissolve
    Millicent "Thank you. I'm Millicent, a mercenary mage. In case my brother hasn't already made that known to the entire forest."
    scene 103_s76 with dissolve
    alex "Alex."
    scene 103_s75 with dissolve
    Millicent "That's... all?"
    scene 103_s76 with dissolve
    alex "Yes."
    scene 103_s75 with dissolve
    Millicent "*chuckles* Alright, keep your secrets. Mysterious type, aren't you?"
    scene 103_s77 with Dissolve(1.0)
    reham "Take care of yourselves. Don't worry about us, [mc]."
    scene 103_s78 with dissolve
    thulkin "Hehe~"
    scene 103_s79 with Dissolve(1.0)
    mc "Uhh...?"
    scene 103_s80 with dissolve
    thulkin "These people really care for you. I can feel it in my bones."
    if maia_love >= 60:
        thulkin "Especially that freckled one."
    else:
        thulkin "Especially that freckled one... though I sense you don't feel the same way about her."
    scene 103_s79 with dissolve
    mc "You can tell that sort of thing?"
    scene 103_s80 with dissolve
    thulkin "You wound me, [mc]! Just because I look like this doesn't mean I don't have emotions."
    thulkin "Love flows through these muscles just as much as power does!"
    scene 103_s79 with dissolve
    mc "I see..."
    scene 103_s80 with dissolve
    thulkin "Now then! It's time to hit the road."
    scene 103_s79 with dissolve
    call screen scene103_choice05 with dissolve

label scene103_choice04_op2:
    play music "river.mp3" fadein 1.0 loop
    scene 103_s65 with Dissolve(2.0)
    perception "The two of them disappear back into the trees as quietly as they arrived, leaving only the rustle of leaves behind."
    alex "...Well."
    scene 103_s66 with Dissolve(1.3)
    if mc_fought_thulkin_fair:
        m "You were incredible, [mc]! It looked like he had you pinned, but then you just... shoved him off like he was nothing!"
    else:
        m "You were incredible, [mc]! *laughs* You punched him so hard he flew back!"
    scene 103_s67 with dissolve
    mc "Thanks. That was... weird."
    scene 103_s68 with dissolve
    reham "Are you hurt anywhere?"
    scene 103_s67 with dissolve
    mc "I don't think so."
    scene 103_s69 with dissolve
    alex "We could've used them as allies, but I suppose we don't need them if we can count on you doing that more often. Seriously, though—how did you do that?"
    scene 103_s70 with Dissolve(1.3)
    mc "No time to think about that. I need to... need to..."
    scene 103_s71 with dissolve
    reham "Something wrong?"
    mc "(Fuck... I feel so tried all of a sudden.)"
    minthra "The danger is gone, and so your body has returned to its natural state. My power consumes your very essence... Use it wisely, or it will consume you."
    m "[mc]!?"
    scene 103_s70 with dissolve
    mc "*cough* I need to lay down for a bit."
    scene 103_s71 with dissolve
    reham "Looks like you might have caught a cold. Let's get you to bed. Alex, help me out."
    jump scene106

label scene103_choice05_op2:
    mc "Hold on a second."
    scene 103_s81 with Fade(0.5,0.5,0.5)
    mc "Neither of us are here to protect you so don't leave this place. And turn down the fire or at least make it smaller. The smoke could give you away."
    scene 103_s83 with dissolve
    reham "Got it."
    scene 103_s82 with dissolve
    m "[mc]... Thank you for caring about us. We promise we'll be safe!"
    scene 103_s81 with dissolve
    mc "*chuckles* I'll be back in a second!"
    if mc_harem_reham and maia_love >= 60:
        scene 103_s85 with Dissolve(2.0)
        play sound "se_sfx/blowjob/kiss5.mp3" 
        reham "*smooch*"
        m "*mwah*"
        sensation "Warmth blooms on both sides of your face. Two soft kisses, one heart full."
    elif mc_harem_reham:
        scene 103_s87 with Dissolve(2.0)
        play sound "se_sfx/blowjob/kiss1.mp3" 
        reham "*smooch* Come back to us without a missing limb, understand?"
        sensation "Her lips brush softly against your cheek."
    else:
        scene 103_s86 with Dissolve(2.0)
        play sound "se_sfx/blowjob/kiss4.mp3" 
        m "*mwah* Be careful."
        sensation "Her lips press warmly against your cheek."
    jump scene104

label scene103_choice05_op1:
    mc "Let's move. Better to get this over with quickly."
    scene 103_s80 with dissolve
    thulkin "You have quite the loving family here. I understand, we won't keep you long."
    scene 103_s79 with dissolve
    jump scene104

label scene104:
    stop music fadeout 1.0 
    scene 104_s1 with Fade(1.5,1.0,1.5)
    play music "blizzard.mp3" fadein 1.0 loop
    env "The path grows steep as you leave the tree line behind. Cold wind whips across the slope, carrying the scent of pine and distant snow."
    scene 104_s2 with Dissolve(1.5)
    Millicent "I missed this."
    scene 104_s3 with dissolve
    alex "Missed what?"
    scene 104_s2 with dissolve
    Millicent "Going out with a proper party. Slaying beasts. Helping people who can't help themselves."
    scene 104_s3 with dissolve
    alex "You don't do that anymore?"
    scene 104_s2 with dissolve
    Millicent "After a while, you learn that being alone is safer. For everyone. You tend to... hurt others. One way or another."
    Millicent "Seeing your allies cut down in front of you... that stays with you."
    scene 104_s4 with Dissolve(1.0)
    thulkin "What's with this talk?! Enough, you'll ruin our morale."
    scene 104_s5 with dissolve
    Millicent "*chuckles* I suppose. Nowadays I travel with my stupid brother. It's better this way. If something happens to him, I'm the only one who gets hurt. Not some family waiting back home."
    scene 104_s6 with Dissolve(2.0)
    ""
    scene 104_s7 with Fade(1.3,1.0,1.0)
    mc "Say... why did you help us? You could've kept going."
    scene 104_s8 with Dissolve(1.0)
    Millicent "{i}Why?{/i} Would you have not done the same?"
    scene 104_s137 with dissolve
    call screen scene104_choice01 with dissolve

label scene104_choice01_op3:
    $ mc_milesent_trust = True
    scene 104_s9 with dissolve
    mc "Yeah. I would have."
    scene 104_s8 with dissolve
    Millicent "Then you understand. Some things aren't choices."
    jump scene104_2

label scene104_choice01_op2:
    $ mc_milesent_trust = True
    scene 104_s9 with dissolve
    mc "If it were my people? Yes. But strangers? My first priority would be the ones I love."
    scene 104_s8 with dissolve
    Millicent "I used to think that way too. But love has a way of expanding when you're not looking. Suddenly every face you pass could be someone's loved one."
    Millicent "Even the annoying ones."
    jump scene104_2

label scene104_choice01_op1:
    scene 104_s9 with dissolve
    mc "No. My safety comes before anyone else's."
    mc "You could've been a bandit. A murderer on the run. I wouldn't risk myself for that."
    scene 104_s8 with dissolve
    Millicent "Hmm. That might have been the case. But aren't you glad I didn't think like that?"
    scene 104_s9 with dissolve
    mc "Better safe the sorry."
    jump scene104_2

label scene104_2:
    scene 104_s10 with Dissolve(0.8)
    Millicent "It's honestly a miracle I even found you. I felt a strange presence pulling me in your direction... and then I saw this wolf standing over your body."
    Millicent "At first I thought it was going to devour you, but... it just stood there howling, like it was calling me closer."
    scene 104_s11 with vpunch
    thulkin "AGGHHHHH! Enough of the gloomy talk! Tell them about the time you mistook our prince for a butler during his coronation!"
    scene 104_s12 with dissolve
    Millicent "Th-That was a mistake! And I apologized profusely afterwards!"
    scene 104_s13 with Dissolve(1.0)
    alex "How do you even mistake a prince for a butler? Shouldn't the dress give it away?"
    Millicent "I was drunk of my mind, alright?!"
    empathy "As they bicker and trade stories, you notice something. Beneath the teasing, there's a rhythm to them, like people who've only ever had each other. She watches his blind spots. He lightens her darkness."
    scene 104_s14 with Fade(0.5,0.5,0.5)
    thulkin "A landslide is blocking the path ahead. We'll have to climb from here."
    scene 104_s15 with Dissolve(1.0)
    alex "F-F-Fuck! I-I'm fr-frreezing..."
    Millicent "Should've worn something warmer."
    alex "L-Like I had a ch-choice!"
    scene 104_s16 with Fade(0.5,0.5,0.5)
    alex "Nghn! I really am getting rusty."
    mc "Hold tight."
    scene 104_s17 with vpunch
    alex "Oh, fuck!"
    scene 104_s18 with dissolve
    play sound "sound_effects/woosh3.mp3"
    Millicent "Alex!"
    call screen scene104_choice02 with dissolve

label scene104_choice02_op1:
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    
    show screen stat_change with easeinright
    scene 104_s23 with Dissolve(0.3)
    play sound "sound_effects/poof.mp3"
    scene 104_s23 with vpunch
    alex "Ahnhg!"
    scene 104_s25 with Dissolve(1.0)
    alex "Wha...? What happened?"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 104_s24 with dissolve
    mc "I got you."
    scene 104_s25 with dissolve
    alex "*sigh* Thank you! My fingers were so frozen that I could barely latch on."
    scene 104_s24 with dissolve
    mc "(She's really light.)"
    scene 104_s25 with dissolve
    alex "*sigh* Let me try that again."
    scene 104_s24 with dissolve
    mc "..."
    scene 104_s25 with dissolve
    alex "Ummm... Y-You can put me down now."
    scene 104_s24 with dissolve
    mc "Oh, sorry."
    jump scene104_3

label scene104_choice02_op2:
    scene 104_s19 with Dissolve(0.3)
    play sound "sound_effects/bodydrop2.mp3"
    scene 104_s19 with vpunch
    perception "Her butt slams straight into your face, your nose landing right between her cheeks as her full weight brings you both down."
    scene 104_s20 with Dissolve(0.3)
    play sound "sound_effects/bodydrop3.mp3"
    scene 104_s20 with vpunch
    alex "Ahnng!"
    alex "Shit! [mc], I-I'm so sorry!"
    scene 104_s21 with dissolve
    alex "Are you hurt?"
    mc "*sniff* I'm fine... Don't worry about it."
    scene 104_s22 with Dissolve(1.5)
    alex "Phew... That could've been way worse."
    Millicent "Why's he smiling like that?"
    alex "No clue..."
    alex "*sigh* Anyway, let's try that again. Come on, get up."
    jump scene104_3

label scene104_3:
    scene 104_s26 with Fade(1.5,1.0,1.0)
    Millicent "There it is. The bastards have taken over some old ruins."
    alex "Wait... didn't they make a board game out of this? What was it called... umm... Ah! Realms and Runes!"
    if mc_play_bgame:
        scene 104_s28 with Dissolve(1.3)
        mc "You're right! I actually played it once."
        scene 104_s29 with Dissolve(0.8)
        alex "..."
        Millicent "..."
        scene 104_s30 with dissolve
        alex "*laughs* You? Really? I never took you for the type to play silly games like that."
        scene 104_s31 with dissolve
        mc "Come on... it was fun."
        scene 104_s30 with dissolve
        alex "Whatever you say~"
    else:
        scene 104_s28 with Dissolve(1.3)
        mc "Board game? (I remember Rebecca wanting me to play that game with her before...)"
        scene 104_s27 with dissolve
        alex "Mhm, some nerdy thing about exploring ruins. Never played it myself. Didn't think it'd be real, though."
    
    scene 104_s32 with Dissolve(1.0)
    Millicent "Trust me, it's nothing like whatever trash they put in those boxes. I doubt we'll find magical beasts or flying colossal squids in there."
    scene 104_s28 with dissolve
    mc "Wasn't counting on it anyway."
    scene 104_s32 with dissolve
    Millicent "Let's go over the plan—"
    play sound "sound_effects/body/snow_run.mp3"
    scene 104_s33 with vpunch
    thulkin "HYAAAHHHH!"
    Millicent "That idiot!"
    scene 104_s34 with vpunch
    mc "Let's go."
    alex "Right behind you."
    Millicent "Wait! Ughhnnn...!"
    stop sound fadeout 1.0 
    scene 104_s35 with Fade(1.0,0.5,1.0)
    mc "Sheesh. He spared no one."
    alex "Neither should we."
    stop music fadeout 1.0 
    scene 104_s36 with Fade(1.5,1.0,1.5)
    play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    perception "You push deeper into the ruins. The sound of combat echoes ahead mixed with Thulkin's laughter, goblin shrieks and the crashing of stone."
    alex "Where should we go?"
    Millicent "You two go right. I'll take left. We'll corner whatever my brother missed."
    Millicent "Kill anything that moves. No mercy for these parasites."
    call screen scene104_choice03 with dissolve

label scene104_choice03_op1:
    mc "Alex, with me."
    alex "Got it."
    jump scene104_choice03_op1_2

label scene104_choice03_op1_2:
    $ mc_goblins_alex = True
    scene 104_s64 with Fade(1.5,1.0,1.0)
    perception "The left tunnel slopes downward, damp and cold. Water drips from above, each drop echoing in the silence. Faint torchlight flickers, casting dancing shadows on the stone walls."
    scene 104_s65 with Dissolve(2.0)
    alex "Quiet. Too quiet."
    scene 104_s66 with Dissolve(0.8)
    mc "Ambush!"
    scene 104_s67 with dissolve
    alex "Behind too."
    scene 104_s68 with dissolve
    goblin "NGHAAA!"
    scene 104_s69 with dissolve
    alex "Stay focused. Don't let their numbers overwhelm you."
    mc "Right."
    scene 104_s70 with Dissolve(0.3)
    play sound "sound_effects/sword/stab5.mp3"
    scene 104_s70 with vpunch
    perception "You fight back-to-back. Alex's movements are sharp and precise. Each strike flows smoothly into the next like water."
    scene 104_s71 with Dissolve(0.3)
    play sound "sound_effects/sword/stab6.mp3"
    scene 104_s71 with vpunch
    goblin "Aghnmm...?"
    scene 104_s72 with Dissolve(2.0)
    mc "(The way she fights... somehow, it's beautiful.)"
    scene 104_s73 with dissolve
    alex "[mc]!"
    scene 104_s74 with dissolve
    play sound "sound_effects/arrow2.mp3"
    mc "Shit!"
    scene 104_s75 with Dissolve(0.3)
    play sound "sound_effects/poof.mp3"
    scene 104_s75 with vpunch
    ""
    scene 104_s76 with Dissolve(0.3)
    play sound "sound_effects/sword/stab4.mp3"
    scene 104_s76 with vpunch
    perception "She moves in a blur, decapitating the goblin in one clean sweep. Its body crumples inches from you."
    scene 104_s77 with Fade(0.5,0.5,0.5)
    alex "Focus."
    scene 104_s78 with dissolve
    mc "T-Thanks. I owe you one."
    mc "..."
    scene 104_s77 with dissolve
    alex "W-What? Why are you staring?"
    scene 104_s78 with dissolve
    call screen scene104_choice05 with dissolve

label scene104_choice05_op1:
    $ mc_likes_alex_fighting = True
    $ alex_love += 10
    mc "I just... really like watching you fight. It's beautiful."
    scene 104_s79 with dissolve
    alex "The... the way I {i}fight{/i}?"
    scene 104_s80 with dissolve
    mc "Mhm. I've never seen you smile like that before. Genuinely, I mean."
    mc "Would've liked to see it outside of combat, but I guess I can't complain."
    scene 104_s79 with dissolve
    alex "Umm... thanks."
    scene 104_s80 with dissolve
    mc "You should smile more. It's not just your fighting that's beautiful, Alex. It's you."
    scene 104_s81 with dissolve
    empathy "For a moment, the mask slips. The cold assassin vanishes, and someone softer appears."
    scene 104_s82 with dissolve
    alex "We need to keep moving! The others are counting on us!"
    scene 104_s81 with dissolve
    mc "*laughs* You're right."
    jump scene104_4

label scene104_choice05_op2:
    mc "It's nothing. Come on, let's catch up with the others."
    scene 104_s77 with dissolve
    alex "Right."
    scene 104_s78 with dissolve
    jump scene104_4

label scene104_choice03_op2:
    $ alex_love -= 30
    scene 104_s37 with Dissolve(1.0)
    mc "I'll go with you."
    scene 104_s38 with dissolve
    Millicent "Not sticking with your girlfriend?"
    scene 104_s37 with dissolve
    alex "G-Girlfriend?!"
    mc "She's not—never mind. Let's just go."

    if mc_scared_milesent or not mc_milesent_trust:
        $ mc_Millicent_rejected_mc = True
        scene 104_s38 with dissolve
        Millicent "Actually... I'd rather you stayed with her, [mc]."
        scene 104_s37 with dissolve
        mc "Why?"
        scene 104_s38 with dissolve
        Millicent "No offense, but I still don't fully trust you. You're a little... scary."
        Millicent "I appreciate the offer to help, really. But I work better alone anyway."
        scene 104_s37 with dissolve
        mc "Have it your way. Let's go, Alex."
        if mc_gave_sword_reham:
            alex "*scoff* Second choice again... great."
        jump scene104_choice03_op1_2

    else:
        $ mc_goblins_milesent = True
        scene 104_s38 with dissolve
        Millicent "Alright. But be sure to give me space, I don't want to accidentally burn you."
        scene 104_s37 with dissolve

    scene 104_s39 with Fade(1.0,1.0,1.3)
    Millicent "Watch your step. These ruins are old, really old. One wrong move and the whole thing could come down."
    scene 104_s40 with dissolve
    mc "You've been here before?"
    scene 104_s39 with dissolve
    Millicent "Once. A long time ago. With people who didn't make it out."
    scene 104_s40 with dissolve
    mc "I'm sorry."
    scene 104_s39 with dissolve
    Millicent "Wasn't your fault."
    scene 104_s41 with Dissolve(1.7)
    mc "Aren't you scared for your brother?"
    Millicent "Quite the opposite, actually. *chuckles* I'm scared he might bring this whole place down on us."
    scene 104_s42 with Fade(1.0,0.5,0.5)
    perception "Ahead, the tunnel opens into a large chamber. Goblins huddle around a crude fire, staring silently at it."
    Millicent "Four of them. I'll take the ones on the left. You take right. Again, don't let any escape."
    mc "Got it."
    scene 104_s43 with Dissolve(1.0)
    perception "You move in silence. The goblins don't notice until it's too late."
    scene 104_s44 with Dissolve(0.3)
    play sound "sound_effects/sword/stab4.mp3"
    scene 104_s44 with vpunch
    mc "HAHHHG!"
    mc "(It went through them like butter! This sword is insane!)"
    scene 104_s45 with Dissolve(0.3)
    play sound "sound_effects/magic/magic_fire3.mp3"
    scene 104_s45 with vpunch
    Millicent "Die, flith!"
    scene 104_s46 with Dissolve(0.3)
    scene 104_s46 with vpunch
    perception "Millicent unleashes a focused beam of fire from her palm. It rips through the goblins, incinerating their insides in an instant."
    stop sound fadeout 1.0
    scene 104_s47 with Fade(0.5,0.5,0.5)
    mc "Impressive. Definitely don't want to be in the receiving end of that."
    scene 104_s48 with dissolve
    Millicent "You're not bad yourself. A bit rough around the edges, but nothing a little polish can't fix."
    scene 104_s47 with dissolve
    mc "*chuckles* Come on, let's catch u—"
    scene 104_s49 with dissolve
    perception "From the corner of your eyes, you spot a goblin hiding in the shadows aiming a bow."
    scene 104_s50 with dissolve
    mc "Watch out!"
    scene 104_s51 with Dissolve(0.3)
    play sound "sound_effects/magic/magic_fire3.mp3"
    scene 104_s51 with vpunch
    Millicent "Hah!"
    stop sound fadeout 1.0
    scene 104_s52 with dissolve
    Millicent "Oh no—"
    scene 104_s53 with Dissolve(0.3)
    play sound "sound_effects/body/clap.mp3"
    scene 104_s53 with vpunch
    perception "Time slows. You move without thinking, your fingers close around the arrow inches from her face. The shaft vibrates with released tension."
    scene 104_s54 with dissolve
    Millicent "Hahh... uhh..."
    scene 104_s55 with Dissolve(1.0)
    Millicent "Y-You saved me... I was about to—"
    Millicent "I was about to die."
    mc "You're fine."
    scene 104_s56 with Dissolve(1.0)
    Millicent "Thank you... I—"
    Millicent "I can't believe I almost met my end for something so foolish. After everything... after all the battles... a golbin."
    scene 104_s57 with dissolve
    mc "Calm down."
    scene 104_s56 with dissolve
    Millicent "This is how... This is how one of my friends died. Not in battle, just... careless."
    scene 104_s57 with dissolve
    call screen scene104_choice04 with dissolve

label scene104_choice04_op2:
    $ mc_milesent_hug = True
    mc "You couldn't have possibly predicted that. Don't blame yourself."
    scene 104_s56 with dissolve
    Millicent "But I should have!"
    scene 104_s57 with dissolve
    mc "You're still standing. That's what matters."
    scene 104_s56 with dissolve
    Millicent "You don't understand. I've been carrying them for years, every mistake and every death that I couldn't prevent. It's so heavy, [mc]."
    scene 104_s57 with dissolve
    mc "Then put them down."
    scene 104_s60 with dissolve
    Millicent "What?"
    scene 104_s59 with dissolve
    mc "Just for a moment. Let someone else carry the weight. I'd be happy to share it with you."
    Millicent "..."
    scene 104_s61 with Dissolve(1.0)
    Millicent "*sniff* I don't... I don't usually cry in front of people."
    mc "I won't tell anyone."
    Millicent "*hic* You're strange... You don't even know me."
    mc "*chuckles* Do I have to know you to want to make you feel better?"
    scene 104_s62 with Dissolve(2.0)
    play sound "sound_effects/clothing_rustle.mp3"
    perception "She stays still for a long moment. Then, slowly, she turns and pulls you into a tight hug."
    scene 104_s63 with dissolve
    Millicent "Thank you... For saving my life. And for this."
    scene 104_s62 with dissolve
    mc "Anytime."
    Millicent "..."
    mc "Millicent?"
    scene 104_s63 with dissolve
    Millicent "Sorry... Can we stay like this a bit longer? *chuckles* You have no idea how long it's been since I hugged someone."
    scene 104_s62 with dissolve
    jump scene104_4

label scene104_choice04_op1:
    mc "You should have been more careful. You knew the ruins were unstable."
    scene 104_s56 with dissolve
    Millicent "I—you're right. I wasn't paying attention. I was... distracted."
    scene 104_s57 with dissolve
    mc "That distraction almost killed you."
    scene 104_s56 with dissolve
    Millicent "I know."
    scene 104_s57 with dissolve
    mc "..."
    scene 104_s56 with dissolve
    Millicent "*sniff* Let's keep moving. We've wasted enough time."
    scene 104_s58 with Dissolve(1.0)
    perception "She walks past you without another word. The brief moment of connection is gone, buried under stone and silence."
    jump scene104_4
    
label scene104_4:
    scene 104_s83 with Fade(1.5,1.0,1.5)
    perception "You arrive into the deepest chamber. Sunlight streams through a hole in the ceiling, painting yellow streaks across the ancient stone."
    
    if mc_goblins_milesent:
        scene 104_s84 with Dissolve(1.5)
        alex "Oh, thank God! I thought I was lost."
        alex "By the way, did you come across a goblin archer? It ran away from me."
        scene 104_s84 with dissolve
        mc "So that was you?"
        alex "Hmm?"
        Millicent "*sigh* Nevermind. Yes, we got him."
    else:
        scene 104_s86 with Dissolve(1.5)
        Millicent "There you are! This place is a maze."

    scene 104_s87 with Dissolve(1.0)
    mc "I hear Thulkin's screams through that door, we should hurry up."
    alex "I hope he left us something. I barely got to use this sword—"
    play sound "sound_effects/doors/door_kick.mp3"
    scene 104_s88 with vpunch
    stop music fadeout 5.0
    thulkin "NGHNNNN!"
    Millicent "Thulkin!"
    scene 104_s90 with Dissolve(1.0)
    thulkin "Took you... *cough* long enough. Saved all the fun... for you."
    scene 104_s89 with dissolve
    Millicent "You were supposed to wait for the plan, you idiot!"
    alex "Forget the plan—what in the hells did this to you?"
    scene 104_s90 with dissolve
    thulkin "The chieftain's through there. Big one. Really big. Wasn't too happy about me killing his little minions."
    scene 104_s89 with dissolve
    Millicent "*sigh* Stay here and regain your stamina. We'll deal with it."
    play music "angry/grenade.mp3" fadein 4.0 loop
    scene 104_s91 with Fade(0.5,0.5,0.5)
    perception "You step through the doorway into the chieftain's chamber. Smoke hangs thick in the air, stinging your eyes and throat. The aftermath of Thulkin's assault, shattered pillars, deep gouges in the stone floor."
    minthra "He's too strong to face head-on. Break his will first, then you can influence him."
    scene 104_s92 with Dissolve(2.0)
    perception "Through the haze, a massive silhouette emerges. The goblin chieftain steps forward, his enormous club dragging along the ground."
    alex "What is it? An ogre?"
    Millicent "That's just how big their chieftains get. The stronger and meaner you are, the higher your chances of ruling the tribe."
    scene 104_s93 with vpunch
    thulkin "HAAAAA!"
    play sound "sound_effects/sword/shield_hit1.mp3"
    scene 104_s94 with Dissolve(0.3)
    scene 104_s94 with vpunch
    chieftain "Akghnn!"
    perception "The chieftain swipes his club. It connects with Thulkin's side with a shockwave that clears the smoke, sending him flying backward through the same door he entered."
    play sound "sound_effects/doors/door_kick.mp3"
    scene 104_s95 with dissolve
    Millicent "Dammit, Thulkin! I told you to rest!"
    thulkin "I'm... nghn... fine!"
    scene 104_s96 with Dissolve(1.0)
    alex "[mc], I'll target his legs. Keep him off balance. You go for his hands, try to disarm him if you can."
    mc "Got it."
    scene 104_s97 with Dissolve(0.3)
    play sound "sound_effects/sword/stab7.mp3"
    scene 104_s97 with vpunch
    perception "Alex darts forward in a blur. Her blade slices across the chieftain's calf. The giant roars and stomps furiously."
    scene 104_s98 with Dissolve(0.3)
    play sound "sound_effects/sword/stab6.mp3"
    scene 104_s98 with vpunch
    perception "You charge in right after, sword raised. Your blade bites deep into his wrist and blood spurts out."
    chieftain "Grahh!"
    scene 104_s99 with dissolve
    Millicent "Clear off, you two. This is going to hurt {i}a lot{/i}."
    scene 104_s100 with Dissolve(0.3)
    play sound "sound_effects/magic/magic_fire3.mp3"
    scene 104_s100 with vpunch
    chieftain "GRHKHANNN!"
    stop sound fadeout 1.0
    mc "Ouch..."
    scene 104_s101 with dissolve
    alex "Let's end it!"
    play sound "sound_effects/woosh2.mp3"
    scene 104_s102 with dissolve
    perception "Despite the pain, the chieftain suddenly snaps and aims his massive club at Alex, who's caught off-guard."
    Millicent "Back away!"
    scene 104_s138 with Dissolve(1.0)
    minthra "I know what you're trying to do. Don't. You cannot influence the dead. Take the hit, I will shield you."
    call screen scene104_choice06 with dissolve

label scene104_choice06_op1:
    play sound "sound_effects/sword/club_hit.mp3"
    scene 104_s103 with Dissolve(0.3)
    scene 104_s103 with vpunch
    sensation "You jump in front of the chieftain just in time. His club connects with your head and pain explodes behind your eyes. The force is strong enough to send you flying."
    play sound "sound_effects/bodydrop2.mp3"
    scene 104_s104 with Dissolve(0.3)
    scene 104_s104 with vpunch
    Millicent "[mc]!"
    alex "NO!"
    scene 104_s105 with Dissolve(0.3)
    play sound "sound_effects/bodydrop4.mp3"
    scene 104_s105 with vpunch
    mc "..."
    minthra "You're fading."
    sensation "Darkness. Then... invigorating warmth. It spreads through your skull, your spine, your limbs."
    scene 104_s106 with Dissolve(1.0)
    mc "(Hnn... huh? I-I should be dead.)"
    scene 104_s107 with Dissolve(2.0)
    mc "Hhng!"
    alex "How... your head... that should have—"
    scene 104_s108 with Dissolve(1.0)
    perception "You move again. Faster now, stronger."
    scene 104_s109 with Dissolve(0.3)
    play sound "sound_effects/stab3.mp3"
    scene 104_s109 with vpunch
    perception "The chieftain tries to swing, but you're not there. You're behind him, blade plunging deep into his thick skin."
    scene 104_s110 with dissolve
    Millicent "What happened to him? Is this normal?"
    scene 104_s111 with dissolve
    alex "I don't know... but I'm not complaining!"
    scene 104_s112 with Dissolve(0.3)
    play sound "sound_effects/doors/wood_break.mp3"
    scene 104_s112 with vpunch
    pause(0.3)
    stop sound
    thulkin "RAAGH! Missed me?!"
    scene 104_s113 with Dissolve(1.0)
    thulkin "Let's hit him all at once!"
    play sound "sound_effects/punch4.mp3"
    scene 104_s114 with Dissolve(0.3)
    scene 104_s114 with vpunch
    perception "The chieftain falters. His swings grow wild, desperate. Alex takes a leg. Millicent focuses her beam. Thulkin plunges his axe into his arm and tackles him, holding him down with sheer mass."
    thulkin "NOW!"
    scene 104_s115 with Dissolve(1.0)
    empathy "The chieftain looks back to you with hateful, defiant eyes. Yet, there's something underneath all the anger. Fear."
    minthra "I will take it from here."
    call screen scene104_choice07 with dissolve

label scene104_choice07_op1:
    stop music fadeout 2.0 
    play sound "sound_effects/magic/dark_magic2.mp3" fadein 3.0 volume 0.5
    scene 104_s116 with Dissolve(1.0)
    perception "You place your hand on his head. He thrashes, then stills. His eyes go wide, then distant as if looking at something only he can."
    chieftain "..."
    stop sound fadeout 2.0
    Millicent "What are you doing!? Kill him!"
    play sound "sound_effects/bodydrop3.mp3"
    scene 104_s117 with Dissolve(2.0)
    perception "His struggles cease and he kneels to the ground, the hate is gone and replaced by something else. Awe. Fear. Worship."
    call screen scene104_choice08 with dissolve

default mc_influence_cheiftain_bad_counted = False
label scene104_choice08_op1:
    $ mc_influence_cheiftain_bad = True
    chieftain "Yeeessh, Mashter..."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 5
    $ mc_influence_cheiftain_bad_counted = True
    $ karma_less = True
    show screen stat_change with easeinright
    thulkin "T-They talk!?"
    scene 104_s139 with Dissolve(1.0)
    minthra "Well done, my vessel. This will not go unrewarded."
    minthra "Continue proving your worth, and I shall grant you powers and knowledge far beyond your comprehension."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 104_s119 with Dissolve(1.0)
    Millicent "What did you do to him?"
    scene 104_s118 with dissolve
    mc "I gave him a choice."
    scene 104_s120 with dissolve
    alex "What choice? That didn't look like a choice."
    scene 104_s119 with dissolve
    Millicent "[mc]! We can't let him live. He'll regroup, find somewhere else, start this all over again!"
    scene 104_s118 with dissolve
    mc "I said let him."
    thulkin "...If he's under his will, then I assume he won't be hurting anyone anymore. Isn't that right, [mc]?"
    scene 104_s121 with Dissolve(1.5)
    mc "We're done here."
    perception "As you leave the chamber, you glance back once. The chieftain's kneeling form fades into the smoke, still watching you."
    jump scene105

label scene104_choice08_op2:
    $ mc_influence_cheiftain_good = True
    chieftain "Yeeessh, Mashter..."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    thulkin "T-They talk!?"
    scene 104_s139 with Dissolve(1.0)
    minthra "What have you done? This {i}isn't{/i} what I ordered you to do."
    mc "(I will use your power, but not as you intend.)"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 104_s119 with Dissolve(1.0)
    Millicent "What did you do to him?"
    scene 104_s118 with dissolve
    mc "I gave him a choice."
    scene 104_s120 with dissolve
    alex "What choice? That didn't look like a choice."
    scene 104_s119 with dissolve
    Millicent "[mc]! We can't let him live. He'll regroup, find somewhere else, start this all over again!"
    scene 104_s118 with dissolve
    mc "I ordered him to fight for us. Against his kind."
    scene 104_s119 with dissolve
    Millicent "What kind of magic is that? And what if it doesn't hold for long?"
    scene 104_s118 with dissolve
    thulkin "[mc]'s strong. I'm sure it'll hold. If this thing is fighting goblins on our behalf then it's a win-win for us."
    scene 104_s121 with Dissolve(1.5)
    perception "As you leave the chamber, you glance back once. The chieftain's kneeling form fades into the smoke, still watching you."
    jump scene105
    
label scene104_choice07_op2:
    $ mc_killed_cheiftain = True
    scene 104_s122 with dissolve
    mc "It's over."
    chieftain "GRAAHHH—"
    scene 104_s123 with Dissolve(0.3)
    play sound "sound_effects/sword/stab4.mp3"
    scene 104_s123 with vpunch
    ""
    scene 104_s140 with Dissolve(1.0)
    if mc_agree_minthra:
        minthra "Do not grow bold enough to start disobeying me, vessel. Remember, the only reason you still breathe is because my power sustains you."
    else:
        minthra "Twice now you have defied me. I will be lenient this time... but do not mistake my patience for weakness."
    stop music fadeout 2.0 
    scene 104_s124 with Dissolve(1.0)
    thulkin "Hahh, well. That's that."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 104_s125 with dissolve
    Millicent "You alright?"
    scene 104_s124 with dissolve
    if not mc_fought_thulkin_fair:
        thulkin "*laughs* I've been through far worse! The punch from [mc] hurt a lot more."
    else:
        thulkin "*laughs* I've been through far worse!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 104_s126 with dissolve
    alex "Good job, [mc]. Seriously."
    scene 104_s128 with Dissolve(1.0)
    mc "You too. All of you."
    scene 104_s127 with dissolve
    thulkin "You fought well, friend! Even if you did steal my kill."
    scene 104_s128 with dissolve
    Millicent "He didn't steal anything. You got thrown outside of the chamber. {i}Twice.{/i}"
    scene 104_s129 with Dissolve(1.5)
    alex "Come on. Let's get out of here. I need air that doesn't smell like dead goblin."
    thulkin "And ale! Lots of ale!"
    perception "As you leave the chamber, you glance back once. The chieftain's body fades into the smoke."
    desire "You've changed something today. For good."
    jump scene105

label scene104_choice06_op2:
    $ mc_killed_cheiftain = True
    scene 104_s130 with Dissolve(1.0)
    mc "Hngg!"
    scene 104_s131 with Dissolve(0.3)
    play sound "sound_effects/sword/stab4.mp3"
    scene 104_s131 with vpunch
    sensation "You grip your sword, twist, and hurl it like a spear. The blade spins through the air, and sinks into the chieftain's skull with a wet crunch mid-swing."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 104_s132 with Dissolve(1.5)
    stop music fadeout 3.0 
    alex "What—"
    scene 104_s133 with Dissolve(1.0)
    hide screen stat_change with easeoutright
    $ karma_more = False
    if mc_tried_help_alex:
        alex "T-Thank you. You saved me... again."
    else:
        alex "T-Thank you. You saved me."
    if mc_goblins_milesent:
        scene 104_s134 with dissolve
        Millicent "He saved me too."

    scene 104_s135 with dissolve
    mc "I wasn't sure that would work..."
    scene 104_s134 with dissolve
    Millicent "*laughs* showoff."
    scene 104_s133 with dissolve
    alex "Did you learn that from... you know?"
    scene 104_s135 with dissolve
    mc "I just took inspiration."
    scene 104_s141 with dissolve

    if mc_agree_minthra:
        minthra "Do not grow bold enough to start disobeying me, vessel. Remember, the only reason you still breathe is because my power sustains you."
    else:
        minthra "Twice now you have defied me. I will be lenient this time... but do not mistake my patience for weakness."

    scene 104_s135 with dissolve
    mc "..."
    mc "Is your brother still outside?"
    scene 104_s136 with dissolve
    Millicent "Shit! I forgot about that idiot..."
    mc "*chuckles* Let's get out of here."
    scene 104_s129 with Dissolve(1.5)
    alex "*sigh* Mhm. I need air that doesn't smell like dead goblin."
    perception "As you leave the chamber, you glance back once. The chieftain's body fades into the smoke."
    desire "You've changed something tonight. For good."
    jump scene105
    
label scene105:
    scene 105_s1 with Fade(1.5,1.5,1.5)
    play music "night.mp3" fadein 1.0 loop
    ""
    scene 105_s2 with Fade(0.5,0.5,1.0)
    thulkin "It was an honor fighting beside you, [mc]! You can count on our strength whenever you need it."
    scene 105_s5 with Dissolve(1.0)
    mc "I'm counting on you both. Why don't you stay with us for a bit? There's not much here, but it's enough."
    scene 105_s4 with dissolve
    Millicent "No, we've already taken enough of your time."
    scene 105_s3 with dissolve
    thulkin "We'll meet again soon enough anyway."
    scene 105_s4 with dissolve
    Millicent "Good luck out there, [mc]. I'm truly sorry for everything that's happened to you."
    Millicent "We'll be staying in Irda for a while. If you need anything, just send us a letter."
    scene 105_s3 with dissolve
    thulkin "Right. Send it to the Adventurer's Guild as a commission. They're always short on strong hands, and we'll answer the call. Fugitives or not."
    scene 105_s5 with dissolve
    if mc_goblins_milesent and mc_milesent_hug:
        scene 105_s6 with Dissolve(1.0)
        play sound "se_sfx/blowjob/kiss5.mp3" 
        perception "Millicent approaches you slowly and gives you a soft kiss on the cheek."
        scene 105_s7 with Dissolve(0.7)
        Millicent "Um... thank you again for saving me back there."
        mc "Of course. We're even now, right?"
        Millicent "*chuckles* Right."
        call screen scene105_choice01 with dissolve
    else:
        jump scene105_choice01_op1

label scene105_choice01_op2:
    $ mc_kiss_milesent = True
    scene 105_s8 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    sensation "You lean in and capture her lips in a deeper kiss, soft and warm."
    thulkin "*laughs* Ohoho! Well now, what do we have here?"
    scene 105_s10 with dissolve
    Millicent "[mc]?!"
    scene 105_s9 with dissolve
    mc "I just wanted to show you I wasn't lying about sharing the burden with you."
    Millicent "..."
    thulkin "Did I miss something? When did you two get so close?!"
    mc "You can count on me anytime, Millicent. You're incredibly strong... but even the strong need someone to lean on. Besides your burly brother, of course."
    scene 105_s10 with dissolve
    Millicent "T-Thank you... I'll... *ahem* I {i}might{/i} take you up on that offer."
    scene 105_s9 with dissolve
    mc "*chuckles* Don't keep me waiting too long."
    jump scene105_choice01_op1

label scene105_choice01_op1:
    scene 105_s2 with Fade(0.5,0.5,0.5)
    thulkin "Our work is far from over. Farewell."
    if mc_goblins_milesent and (mc_kiss_milesent or mc_milesent_hug):
        scene 105_s11 with Fade(1.0,1.0,1.0)
        alex "..."
        mc "What?"
        scene 105_s12 with dissolve
        alex "Nothing. It's just... girls seem to be attracted to you wherever you go."
        scene 105_s11 with dissolve
        mc "What can I say? My charm and reputation precede me~"
        scene 105_s12 with dissolve
        alex "Heh. Shut up."
        scene 105_s13 with dissolve
    else:
        scene 105_s13 with Fade(1.0,1.0,1.0)
    alex "Wait, dammit!"
    mc "What's wrong?"
    scene 105_s12 with Dissolve(1.0)
    alex "I forgot to ask the girl something. They're siblings, right?"
    scene 105_s11 with dissolve
    mc "You mean the ears?"
    scene 105_s12 with dissolve
    alex "Mhm. It doesn't make sense. If she's an elf, her brother should be an elf too. Elf genes are dominant, if an elf and a human breed, the child is always a half-elf."
    scene 105_s11 with dissolve
    mc "Hmm... We'll have to ask them next time we see them."
    scene 105_s12 with dissolve
    alex "But I want to know now! Ugh... Whatever. Go get some rest. I'll keep watch tonight."
    scene 105_s11 with dissolve
    stop music fadeout 1.0 
    jump scene105_2

label scene105_2:
    scene 105_s14 with Fade(1.0,1.0,1.0)
    play music "fire.mp3" fadein 1.0 volume 0.8 loop
    mc "(This power... it's definitely Minthra's doing.)"
    scene 105_s15 with Dissolve(1.0)
    mc "(I could use it for good. Protect everyone. But... what if she hurts me again? What if she decides that I have done enough and takes control of me when I least expect it?)"
    mc "(I never want to feel that pain again. Never.)"
    if maia_love >= 70:
        scene 105_s16 with Dissolve(1.0)
        mc "Hmm?"
        scene 105_s17 with Dissolve(1.0)
        mc "You two aren't sleepy yet?"
        scene 105_s18 with dissolve
        reham "A lot has been on our minds, perhaps we need a bedtime story first."
        scene 105_s17 with dissolve
        mc "A bedtime story? Seriously?"
        scene 105_s19 with dissolve
        m "Tell us a story about your adventures, [mc]!"
        scene 105_s17 with dissolve
        mc "I don't know..."
        scene 105_s19 with dissolve
        m "Pleeaasseee~!"
        scene 105_s20 with dissolve
        mc "Well..."
        scene 105_s21 with dissolve
        call screen scene105_choice02 with dissolve
        
    elif mc_harem_reham and maia_love <= 70:
        scene 105_s47 with Dissolve(1.0)
        mc "Hmm?"
        scene 105_s49 with Dissolve(1.0)
        reham "You must be exhausted... You look like you've been carrying the whole world on your shoulders."
        scene 105_s48 with dissolve
        mc "Feels that way sometimes."
        scene 105_s49 with dissolve
        reham "Then let me help, even if it's just by sitting here with you."
        scene 105_s48 with dissolve
        mc "You always know what to say."
        scene 105_s24 with Dissolve(1.0)
        reham "You're acting differently, [mc]. Quieter than usual."
        reham "You never told us what happened when you came back this morning..."
        scene 105_s25 with dissolve
        mc "Yeah. I'm back now. That's what matters."
        scene 105_s24 with dissolve
        reham "I won't push you if you don't want to talk about it. But please remember that I'm always here if you need me."
        reham "Unless you'd rather be alone tonight?"
        scene 105_s25 with dissolve
        call screen scene105_choice03 with dissolve

    elif maia_love >= 60:
        scene 105_s46 with Dissolve(1.0)
        mc "Hmm?"
        scene 105_s44 with Dissolve(1.0)
        perception "Maia sits beside you, tucking her legs under herself. The flames dances in her wide eyes as she stares at you."
        scene 105_s43 with dissolve
        mc "I see that look in your eyes. Don't worry about me, Maia. I'm not even hurt, just tired."
        scene 105_s45 with dissolve
        m "That is strange. The others said you fought so hard..."
        scene 105_s43 with dissolve
        mc "Guess I'm tougher than I look."
        scene 105_s45 with dissolve
        m "*giggles* I knew that already. You've always been strong, even when you pretend you're not."
        scene 105_s33 with Dissolve(1.0)
        mc "What about you? How are you holding up?"
        scene 105_s34 with dissolve
        m "I'm always fine whenever you're beside me."
        m "...I-I want to tell you something."
        scene 105_s33 with dissolve
        mc "Tell me what?"
        scene 105_s22 with Dissolve(1.0)
        m "That... you're the only person who ever made me feel safe. Like I matter. Like I'm not just... some girl who was left behind."
        m "I'm so glad I met you, [mc]."
        scene 105_s23 with dissolve
        mc "Ever after all that?"
        scene 105_s22 with dissolve
        m "More so after."
        scene 105_s23 with dissolve
        mc "*chuckles* Thank you."
        m "..."
        scene 105_s22 with dissolve
        m "Can I ask you something?"
        scene 105_s23 with dissolve
        mc "Anything."
        scene 105_s22 with dissolve
        m "When you're out there... when you're gone, do you think about me like I think about you?"
        scene 105_s23 with dissolve
        call screen scene105_choice04 with dissolve

    else:
        mc "*sigh* (Fuck, I'm tired as hell. I need to hit the bed.)"
        jump scene106

label scene105_choice03_op1:
    $ mc_slept_reham_106 = True
    scene 105_s31 with Dissolve(1.0)
    mc "No. I'd love to sleep together tonight. I could really use the comforting touch of a beautiful woman."
    scene 105_s32 with dissolve
    reham "*giggles* Come. I'll make the bed nice and warm for you."
    jump scene106

label scene105_choice03_op2:
    scene 105_s26 with Dissolve(1.0)
    mc "I think I need some time alone tonight, Reham."
    scene 105_s27 with dissolve
    reham "I understand."
    reham "Rest well, okay? I'll be right here if you need anything."
    reham "Goodnight, [mc]. I'm really proud of you."
    jump scene106

label scene105_choice04_op2:
    $ maia_love += 10
    scene 105_s33 with Dissolve(1.0)
    mc "Every second. You never leave my mind. Your smile... your cute face."
    scene 105_s34 with dissolve
    m "R-Really?"
    scene 105_s33 with dissolve
    mc "Really. *laughs* A girl like you? Hard to forget."
    scene 105_s34 with dissolve
    m "That's... that means more than you know."
    m "Thank you. For saving me. For everything."
    scene 105_s23 with dissolve
    reham "It's getting late you two. Leave [mc] alone, Maia. He should rest."
    scene 105_s22 with dissolve
    m "Umm... C-Can we sleep together, [mc]? It's been so long since we shared the same bed."
    scene 105_s23 with dissolve
    call screen scene105_choice05 with dissolve

label scene105_choice04_op1:
    $ maia_love -= 10
    mc "I get what you're saying, Maia. But there's much to think about other than you."
    scene 105_s22 with dissolve
    m "O-Of course. This isn't the time for that... you have a lot depending on you. Right?"
    scene 105_s23 with dissolve
    mc "Right."
    scene 105_s22 with dissolve
    m "Then I shouldn't be sad. You're thinking about all of us. Hehe~"
    scene 105_s23 with dissolve
    reham "It's getting late you two. Leave [mc] alone, Maia. He should rest."
    scene 105_s22 with dissolve
    m "Can we sleep together, [mc]? It's been so long since we shared the same bed."
    scene 105_s23 with dissolve
    call screen scene105_choice05 with dissolve

label scene105_choice05_op1:
    $ mc_slept_maia_106 = True
    scene 105_s33 with Dissolve(1.0)
    mc "Yeah, I want you close tonight."
    scene 105_s34 with dissolve
    m "I missed this... just being near you."
    jump scene106

label scene105_choice05_op2:
    scene 105_s23 with dissolve
    mc "I think I need to be alone tonight, Maia. Just... to think."
    scene 105_s22 with dissolve
    m "A-Alright. I understand."
    m "If you change your mind... Just tell me."
    m "Sleep well, [mc]. I'm glad you're here."
    scene 105_s23 with dissolve
    jump scene106

label scene105_choice02_op1:
    stop music fadeout 1.0 
    scene 105_s20 with dissolve
    mc "How about a scary story?"
    play music "ambiance/witch_swamp.mp3" fadein 4.0 volume 0.5 loop
    scene 105_s19 with dissolve
    m "Ooooh~ I love scary stories!"
    scene 105_s30 with Dissolve(2.5)
    env "Unseen crows scream from the trees. Flies buzz around the damp, rotting earth. And in the middle of it all stands a crooked, ancient house... alive with shadows."
    env "Inside, a lone woman hunches over a heavy tome, her eyes tracing every line with deep concentration. But there's no hunger in her gaze, only worry... and sadness."
    scene 105_s24 with Dissolve(1.0)
    reham "She really chooses to live like that? All alone in that horrible place? I'd lose my mind without anyone to talk to."
    scene 105_s25 with dissolve
    mc "Some people prefer the quiet. The isolation."
    scene 105_s22 with dissolve
    m "*giggles* Still... that place must smell awful. All those flies and damp earth..."
    scene 105_s23 with dissolve
    reham "Spare us the commentary, castle maiden."
    reham "So... what did you do to her?"
    scene 105_s26 with Dissolve(1.0)
    if quest_witch_amelia_dead:
        mc "I..."
        m "..."
        mc "I dealt with her."
        scene 105_s27 with dissolve
        reham "...I see."
        reham "That must have been difficult."
    elif quest_witch_amelia_alive and not quest_witch_amelia_alive_free:
        mc "She was too dangerous to leave free, so I captured her. She should be locked up in one of Irda's dungeons by now."
        scene 105_s26 with dissolve
        reham "Just like that?"
        scene 105_s27 with dissolve
        mc "Just like that."
        scene 105_s27 with dissolve

    else:
        mc "I managed to make her see reason. She won't hurt anyone anymore... and she might even help us in the future."
        scene 105_s27 with dissolve
        reham "You convinced a witch to turn good?! How?!"
        m "[mc] is good at talking!"
        scene 105_s26 with dissolve
        mc "*chuckles* Maybe she wasn't as evil as she seemed. Just... misunderstood."
        scene 105_s27 with dissolve
    stop music fadeout 1.0 
    m "More!"
    play music "fire.mp3" fadein 1.0 loop
    jump scene105_3

label scene105_choice02_op2:
    stop music fadeout 1.0 
    scene 105_s20 with dissolve
    mc "I was sent on an important mission by the Queen. On the way there, we stumbled upon this strange little village hidden in a valley."
    play music "side_event6.mp3" fadein 4.0 loop
    scene 105_s24 with dissolve
    reham "A haunted one?"
    scene 105_s25 with dissolve
    mc "Not quite. Just... really weird."
    scene 105_s29 with Dissolve(2.5)
    env "The village lay quietly in a valley, untouched by any main road. Neat rows of houses with doors left wide open, dark windows, and a single stone well."
    scene 105_s22 with Dissolve(1.0)
    m "Where was everyone?"
    scene 105_s23 with dissolve
    mc "That's exactly what we wondered. Alex and I found a young girl and tried to ask her, but she took one look at us and ran away."
    scene 105_s24 with Dissolve(1.0)
    reham "W-Were they... some kind of cult?"
    scene 105_s25 with dissolve
    mc "*laughs* You got it right. And it turns out they were all gathered in the main building... preparing for some festival."
    m "...That's it?"
    scene 105_s26 with dissolve
    mc "*ahem* Yeah, that's it."
    scene 105_s27 with dissolve
    reham "Oh... how disappointing."
    stop music fadeout 1.0 
    mc "(Yeah... better leave out the part about it being a breeding festival.)"
    play music "fire.mp3" fadein 1.0 loop
    m "More!"
    jump scene105_3

label scene105_choice02_op3:
    $ mc_told_maia_reham_other_world = True
    stop music fadeout 1.0 
    scene 105_s26 with dissolve
    mc "Fine. I'll tell you about where I really came from, but I can't promise it'll be a fun story."
    play music "breakup.mp3" fadein 4.0 loop
    scene 105_s27 with dissolve
    reham "Where you came from? You weren't born in Irda?"
    scene 105_s26 with dissolve
    mc "No. I was born somewhere... very far away."
    scene 105_s27 with dissolve
    m "Another kingdom?"
    scene 105_s26 with dissolve
    mc "Another world."
    scene 105_s27 with dissolve
    scene 105_s28 with Dissolve(2.5)
    env "Raindrops fall on streets lit by every color imaginable. Red, green, blue, yellow. Bright signs glow in the darkness, buzzing softly. People walk beneath umbrellas of all kinds, their footsteps splashing through puddles."
    env "One man holds a small, flat rectangle to his ear and speaks quietly. A voice answers from the device. Both of them laugh."
    env "A metal carriage without horses glides past, its bright lights cutting through the rain."
    scene 105_s22 with Dissolve(1.0)
    reham "What... is a 'phone'?"
    scene 105_s23 with dissolve
    mc "It's a device that lets you speak to someone who's far away. Like magic... but it isn't magic."
    scene 105_s22 with dissolve
    m "And that carriage? How does it move without horses?"
    scene 105_s23 with dissolve
    mc "*laughs* They have machines inside called engines. They burn fuel or use electricity. Honestly, I don't fully understand it myself."
    scene 105_s24 with Dissolve(1.0)
    reham "They sound so practical."
    scene 105_s25 with dissolve
    mc "They are. You can travel for hundreds of miles without needing to stop."
    scene 105_s27 with dissolve
    stop music fadeout 1.0 
    empathy "The fire crackles softly as your voice fades. Their faces shift... doubt, wonder, doubt again."
    play music "fire.mp3" fadein 1.0 loop
    reham "...You're not lying, are you?"
    scene 105_s26 with dissolve
    mc "I'm not."
    scene 105_s27 with dissolve
    m "Then... how did you get here?"
    scene 105_s26 with dissolve
    mc "I don't know. One morning I just woke up in a big grassy field with no memory of how I got there."
    scene 105_s27 with dissolve
    reham "And you never tried to go back? You must miss it terribly."
    scene 105_s26 with dissolve
    mc "A little."
    scene 105_s27 with dissolve
    m "Well... I'm really glad you're here with us, [mc]."
    m "Please tell us more! What else is there? I want to hear about the phones... and the moving carriages... and everything!"
    jump scene105_3

label scene105_3:
    scene 105_s24 with Dissolve(1.0)
    reham "No, that's enough. [mc] must be exhausted after all that."
    if mc_harem_reham and not mc_maia_monogamous_sure:
        reham "Why don't you relax? Let us take care of you for once."
        scene 105_s22 with Dissolve(1.0)
        m "Right! We'll make you feel really good, [mx]."
        scene 105_s31 with Dissolve(1.0)
        mc "You two... what exactly are you getting at?"
        scene 105_s32 with dissolve
        reham "Well, I thought since we both have you now... it might be nice for both of us to... please you. Together."
        scene 105_s33 with dissolve
        mc "You agreed to this?"
        scene 105_s34 with dissolve
        m "Y-Yes. I want you to be happy, even if I have to share."
        scene 105_s32 with dissolve
        reham "She was against it at first, you know. Always wants you for herself."
        reham "But I suppose her love for you made her see things differently. I managed to convince her that sexual relife for warriors before a battle is just as important as training."
        scene 105_s31 with dissolve
        mc "I see..."
        scene 105_s22 with dissolve
        m "I just want to make you feel good, [mc]. Even if I'm not the only one."
        scene 105_s23 with dissolve
        reham "We never did discuss who should go first..."
        scene 105_s36 with Dissolve(0.3)
        scene 105_s36 with hpunch
        m "Me! Obviously!"
        scene 105_s37 with Dissolve(0.3)
        scene 105_s37 with hpunch
        reham "Hold on. Shouldn't we decide this fairly?"
        scene 105_s36 with Dissolve(0.3)
        scene 105_s36 with hpunch
        m "He was mine first!"
        scene 105_s37 with Dissolve(0.3)
        scene 105_s37 with hpunch
        reham "That doesn't mean much when we're both here now."
        scene 105_s36 with Dissolve(0.3)
        scene 105_s36 with hpunch
        m "But—!"
        scene 105_s37 with Dissolve(0.3)
        scene 105_s37 with hpunch
        reham "You're being really selfish right now, Maia. [mc] should be the one to choose."
        scene 105_s36 with Dissolve(0.3)
        scene 105_s36 with hpunch
        m "[mc]! Tell her you want me first!"
        mc "..."
        call screen scene105_choice06 with dissolve
    else:
        $ mc_slept_maia_reham_106_nosex = True
        scene 105_s22 with Dissolve(1.0)
        m "R-Right! Sleep with us, [mx]. We'll make sure you're nice and warm between us~"
        scene 105_s23 with Dissolve(1.0)
        mc "*chuckles* Alright, fine. Feel like I'm about to drop any second now."
        stop music fadeout 1.0
        jump scene106

default s105_maia_first = False
default s105_reham_first = False
label scene105_choice06_op2:
    $ mc_slept_maia_reham_106 = True
    $ s105_reham_first = True
    scene 105_s38 with dissolve
    mc "I don't even know what we're starting, but you go first, Reham."
    scene 105_s39 with dissolve
    reham "Oh? Well then..."
    reham "You don't mind terribly, do you?"
    scene 105_s40 with dissolve
    m "...Fine. But you better not take forever."
    scene 105_s39 with dissolve
    reham "*giggles* I can't promise that. I plan to be {i}very{/i}... thorough~"
    reham "Come, [mc]. I'll show you that choosing me first wasn't a mistake."
    m "Tch!"
    jump scene105_4

label scene105_choice06_op1:
    $ mc_slept_maia_reham_106 = True
    $ s105_maia_first = True
    scene 105_s38 with dissolve
    mc "I don't even know what we're starting, but you go first, Maia."
    scene 105_s41 with dissolve
    m "Heh~ It's clear now who [mc] really prefers."
    scene 105_s42 with dissolve
    reham "{i}Please{/i}. He's just being kind so you don't throw a tantrum."
    scene 105_s41 with dissolve
    m "Keep telling yourself that~"
    jump scene105_4

label scene105_choice06_op3:
    scene 105_s38 with dissolve
    mc "I appreciate you two trying to make me feel better, but I'm honestly too tired for {i}any{/i} of that tonight."
    scene 105_s41 with dissolve
    m "O-Oh... alright."
    scene 105_s42 with dissolve
    reham "Of course. I was just about to suggest that. Better to rest."
    scene 105_s41 with dissolve
    m "Just about to? You were {i}begging{/i} me to share him with you."
    scene 105_s42 with dissolve
    reham "You're imagining things again."
    scene 105_s38 with dissolve
    mc "*sigh* Enough. Leave me alone."
    scene 105_s41 with dissolve
    m "R-Right. I apologize, [mc]."
    scene 105_s14 with Dissolve(2.0)
    sensation "The fire crackles softly. For the first time in what feels like forever, you let yourself simply... rest."
    jump scene106

label scene105_4:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p7_replay:
        $ persistent.scene5_p7_replay = True

    stop music fadeout 1.0 
    scene 106_s1 with Fade(1.0,1.0,1.5)
    ""
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 106_s2 with Dissolve(1.3)
    ""
    scene 106_s3 with Dissolve(1.0)
    m "Please lie down and stay still, [mx]. Just leave it to us~"
    scene 106_s4 with Dissolve(1.0)
    ""
    scene 106_s5 with Dissolve(1.3)
    m "It's... so warm. And hard..."
    scene 106_s6 with dissolve
    reham "Hah~! It's so large up close!"
    scene 106_s7 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    sensation "She leans in, lips brushing the tip, soft and loving. A small kiss, then another, tasting you gently."
    m "Mmm~"

    if persistent.scene7_replay:
        scene 106_s8 with dissolve
        m "You have to kiss it too."
        scene 106_s9 with dissolve
        reham "H-Huh?! I... I don't know."
        scene 106_s8 with dissolve
        m "You have to. [mx] likes it when you kiss his cock because it means you're his woman."
        scene 106_s12 with dissolve
        mc "When did I say that?"
        scene 106_s8 with dissolve
        if maia_anal_sex > 0:
            m "Not to mention that you'll have to learn to swallow his seed... and take it in the butt."
        else:
            m "Not to mention that you'll have to learn to swallow his seed when he asks you to."
        scene 106_s9 with dissolve
        reham "Umm... well..."
        scene 106_s8 with dissolve
        m "Isn't that right, [mx]?"
        scene 106_s12 with dissolve
        call screen scene105_choice07 with dissolve
    
    if s105_reham_first:
        scene 106_s8 with dissolve
        m "Go ahead. [mx] choose you first."
        scene 106_s9 with dissolve
        reham "R-Right! I'll try my best. Tell me if I'm doing it wrong, Master."
    jump scene106_bj

label scene105_choice07_op1:
    mc "That's right. Go on, Reham."
    scene 106_s9 with dissolve
    reham "Y-Yes, Master."
    scene 106_s10 with dissolve
    play sound "se_sfx/blowjob/kiss1.mp3" 
    reham "Mmmn..."
    reham "Rike shis?"
    scene 106_s11 with dissolve
    if s105_maia_first:
        m "Yes. But be more affectionate next time. Show [mx] that you love his cock and only his... Now move, I start first."
        mc "(Sheesh, Maia...)"
    else:
        m "Yes. But be more affectionate next time. Show [mx] that you love his cock and only his... Now start making him feel good. [mx] choose you first."
        mc "(Sheesh, Maia...)"
    jump scene106_bj

label scene105_choice07_op2:
    $ reham_love += 10
    mc "It's fine. She doesn't have to if she's uncomfortable."
    scene 106_s9 with dissolve
    reham "Thank you..."
    scene 106_s8 with dissolve
    m "You're too kind, [mx]~ Be grateful of that, Reham."
    scene 106_s9 with dissolve
    reham "Thank you, Master."
    scene 106_s12 with dissolve
    mc "Please don't give her a wrong idea about me, Maia..."
    jump scene106_bj

image s106_bj1 = Movie(play="images/chapter5/scene106/s106_bj1.webm", loop=True)
image s106_bj2 = Movie(play="images/chapter5/scene106/s106_bj2.webm", loop=True)
image s106_bj3 = Movie(play="images/chapter5/scene106/s106_bj3.webm", loop=True)

image s106_r_vsex1 = Movie(play="images/chapter5/scene106/s106_r_vsex1.webm", loop=True)
image s106_r_vsex2 = Movie(play="images/chapter5/scene106/s106_r_vsex2.webm", loop=True)
image s106_r_asex1 = Movie(play="images/chapter5/scene106/s106_r_asex1.webm", loop=True)
image s106_r_asex2 = Movie(play="images/chapter5/scene106/s106_r_asex2.webm", loop=True)

image s106_r_vsex3 = Movie(play="images/chapter5/scene106/s106_r_vsex3.webm", loop=True)
image s106_r_asex3 = Movie(play="images/chapter5/scene106/s106_r_asex3.webm", loop=True)


image s106_m_vsex1 = Movie(play="images/chapter5/scene106/s106_m_vsex1.webm", loop=True)
image s106_m_vsex2 = Movie(play="images/chapter5/scene106/s106_m_vsex2.webm", loop=True)
image s106_m_asex1 = Movie(play="images/chapter5/scene106/s106_m_asex1.webm", loop=True)
image s106_m_asex2 = Movie(play="images/chapter5/scene106/s106_m_asex2.webm", loop=True)

default s106_bj_maia = False
default s106_bj_reham = False
default s106_bj_share = False

label scene106_bj:
    $ maia_mouth_virgin = False
    $ s106_bj_share = False
    if s105_maia_first:
        $ s106_bj_maia = True
        $ s106_bj_reham = False
        show s106_bj1 with Dissolve(1.0)
        sensation "She starts sucking you passionately, tongue swirling around the head in little circle. Her saliva already coating your entire cock."
        m "Mffhmmm~ Am I... doing it good?"
        mc "Perfect. Keep going."
        m "Mnnnnn..."
        sensation "Your cock collides with the back of her throat as she takes you deeper. She gags, but doesn't pull away."
        m "Mmm... I love how you feel~ how you throb on my tongue~"
        m "*slrup* Mfhnn..."
        reham "Watching you do this... nghnn~ It's making me feel really hot."
    else:
        $ s106_bj_maia = False
        $ s106_bj_reham = True
        show s106_bj2 with Dissolve(1.0)
        perception "She hesitantly takes you in her warm mouth, going no deeper than the head."
        empathy "She looks at you for affirmation, trying to gauge your reaction."
        reham "Mmm... *gag* So... *gag* this is how a cock feels like in your mouth..."
        m "*giggles* You look like a chimpmunk."
        reham "*slrup* Mfhnn..."
        reham "Sorry if I'm... *gag* drooling too much. *slurp*"
        mc "You're doing fine."
    call screen scene106_bj with dissolve

default scene106_bj2_reham = False
default scene106_bj2_maia = False
default scene106_bj_share = False

label scene106_bj_op1:
    $ reham_mouth_virgin = False
    
    $ s106_bj_maia = False
    $ s106_bj_reham = True
    $ scene106_bj2_reham = True
    $ s106_bj_share = False
    mc "Ahhnn... Reham... your turn."
    reham "Yes, Master."
    scene black with Dissolve(1.0)
    show s106_bj2 with Dissolve(1.0)
    m "B-But... I wasn't done!"
    reham "You'll get him again soon. Let me practice, it's my first time afterall."
    if maia_virgin:
        m "Me too!"
        reham "Wait... what?"
        m "[mx] didn't do anything to me all this time."
        reham "I find that very hard to believe."
        m "It's true..."
    else:
        m "R-Really?"
        reham "I might not have the experiance but I can still worship him properly~"
    sensation "She opens wider, her lips stretching around your tip as Maia's wet tongue works your testicles."
    m "*slurp* I think he prefers if you go all the way."
    reham "I can't... *gag* not yet."
    reham "Hnnnm~ This cock... it's more than enough for both of us."
    m "*lick* Don't take too long."
    call screen scene106_bj with dissolve

label scene106_bj_op2:
    $ s106_bj_maia = True
    $ s106_bj_reham = False
    $ scene106_bj2_maia = True
    $ s106_bj_share = False
    mc "Ahnn... Maia, your turn."
    m "A-Alright!"
    scene black with Dissolve(1.0)
    show s106_bj1 with Dissolve(1.0)
    sensation "She slides your cock into her hungry mouth. Her smooth tongue mercilessly teasing your frenulum."
    m "Mmm... please give me your seed, [mx]~"
    reham "She's really into it. I never knew you had this side, Maia."
    m "Mmnnnn~"
    m "Are you ready to release your seed for me, [mx]~?"
    mc "Ahhnn... N-Not yet."
    reham "W-What will you do when he does?"
    m "*slurp* I'll swallow it all~ Every single drop~"
    call screen scene106_bj with dissolve

label scene106_bj_op3:
    $ scene106_bj_share = True
    $ s106_bj_maia = False
    $ s106_bj_reham = False
    reham "Mmm... he's so big... my pu— *ahem* vagina is aching like it's never been before."
    m "You mean your pussy?"
    reham "No need to be vulgar, girl."
    perception "Their tongues flick and tease around your length, swallowing their own spit and your precum in messy, open-mouthed glides."
    m "Mmmfmmn~ you're leaking so much... it's running down my chin."
    reham "It tastes weird... I think he's close. Feel how he's pulsing against our tongues?"
    m "Yes... I can feel it in my mouth... [mx] is going to leak any second~"
    call screen scene106_bj with dissolve


label scene106_bj2_op1:
    $ s106_bj_maia = False
    $ s106_bj_reham = True
    $ s106_bj_share = False
    mc "Hnnng... Reham!"
    reham "Yes, Master. My turn to pleasure you."
    scene black with Dissolve(0.3)
    show s106_bj2 with dissolve
    sensation "You feel her lips brushing agaisnt your glans. For some reason, the way she moans while struggling to go beyond the head makes you shiver. You feel like erupting any second now."
    mc "Ahnngg!"
    reham "Mmm?! Master, your expression... are you actually enjoying my sloppy work?"
    mc "Y-Yes. *chuckles* But not for the reason you think it is."
    reham "*slurp* Mnnn~"
    m "What about me, [mx]?"
    mc "You're doing great. Ahnn... keep those lips around my balls."
    call screen scene106_bj with dissolve

label scene106_bj2_op2:
    $ s106_bj_maia = True
    $ s106_bj_reham = False
    $ s106_bj_share = False
    m "Yes! My turn~"
    scene black with Dissolve(0.3)
    show s106_bj1 with dissolve
    sensation "She sucks hard, cheeks hollowing, tongue flicking the slit in rapid little lashes. Right now, her only purpose is to milk every last drop of your seed."
    m "Mmmph... please... give it to me, [mx]~ Fill my mouth~ I promise to not waste a drop of your delicious seed."
    reham "Y-Yes! Let out all of your semen in {i}her{/i} mouth. I-I don't mind if she takes it."
    m "You're saying that because you don't want him to do it in your mouth, aren't you?"
    reham "What?! No! T-That's not true..."
    m "*slurp* It totally is. [mx], why don't you let her taste it? She'll be addicted to it after the third time."
    reham "Third time?! Surely you're not planning on feeding me your semen every day, right?"
    mc "*chuckles* Who knows... Maybe I'll put you on a special diet."
    reham "Please don't!"
    call screen scene106_bj with dissolve

default s106_bj_share_first = True
label scene106_bj2_op3:
    $ s106_bj_maia = False
    $ s106_bj_reham = False
    $ s106_bj_share = True
    scene 106_s49 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss5.mp3" 
    sensation "Maia leans in from your right, Reham from your left. Their lips meet around the swollen head of your cock in a slow, wet kiss."
    scene black with Dissolve(0.3)
    show s106_bj3 with dissolve
    if s106_bj_share_first:
        $ s106_bj_share_first = False
        reham "Gods... this is more intense than I thought. Makes me clench just thinking about it."
        m "You're so wet too... I can smell it."
        reham "Oh Gods... that's awkward..."
        sensation "Reham's soft, eager tongue laps at the sensitive ridge just under the head while Maia's longer strokes drag along the shaft."
        reham "Let's make him ejaculate together."
        m "Mnnhnnn *slurp*"
        sensation "Their tongues gently slide over you, dripping with saliva. The heat of their mouths mingles, slick and seething."
    else:
        jump scene106_bj_op3
    call screen scene106_bj with dissolve

label scene106_bj_op4:
    call screen scene106_bj_op4 with dissolve

label scene106_bj_cum_m:
    if s106_bj_reham:
        scene black with Dissolve(0.3)
        show s106_bj1 with dissolve
    mc "I'm gonna finish inside you, Maia!"
    m "Mhmmm~ please... inside me... I want to feel you release in my mouth~"
    scene 106_s13 with Dissolve(0.3)
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 106_s13 with vpunch
    sensation "Your cock erupts with thick, powerful spurts that flood deep into her throat. She moans softly, throat spasming rhythmically around you, drawing out every pulse."
    mc "Aghhhn!"
    scene 106_s14 with Dissolve(0.3)
    play sound "se_sfx/blowjob/blowjob_cum2.mp3" 
    scene 106_s14 with vpunch
    m "*gulp* *gulp* Oh Gods... you're filling my belly, [mx]!"
    mc "Hahh..."
    reham "Y-You're still keeping it in your mouth?"
    m "There might be something left in there~"
    scene 106_s15 with Dissolve(1.0)
    play sound "se_sfx/lick/lick1.mp3" 
    m "Ahhhnn... Rook, [mx]. Did I do well?"
    mc "You always do."
    scene 106_s17 with Dissolve(1.0)
    play sound "se_sfx/blowjob/swallow3.mp3" 
    reham "How does it taste?"
    scene 106_s16 with dissolve
    m "*slurp* Shoo good~! *gulp* "
    scene 106_s22 with Fade(1.0,1.0,1.0)
    reham "There. All cleaned up~ I hope I did well to service you, Master. But now, it's time to rest. We'll be with you, of course."
    scene 106_s23 with dissolve
    call screen scene106_choice01 with dissolve

label scene106_bj_cum_r:
    if s106_bj_maia:
        scene black with Dissolve(0.3)
        show s106_bj2 with dissolve
    mc "Reham!"
    reham "M-Me? I... never tasted it before. To swallow a liquid meant to impregnate a woman... The act is so depraved—it makes me shudder."
    mc "A first time for everything."
    reham "...Fine. do it, then. Finish inside my mouth, Master. Spill on your servant's tongue."
    mc "Ahhnn... You want it that deep?!"
    reham "Mhm~ I'll swallow it all if that's your intent."
    scene 106_s18 with Dissolve(0.3)
    play sound "se_sfx/blowjob/blowjob_cum3.mp3" 
    scene 106_s18 with vpunch
    sensation "Your cock erupts with thick streams of cum in her mouth, flooding down into her throat. She moans awkwardly, throat gagging, and tears forming in her eyes."
    mc "Ahhhgn! Keep sucking my balls, Maia!"
    scene 106_s19 with Dissolve(0.3)
    play sound "se_sfx/blowjob/blowjob_cum4.mp3" 
    scene 106_s19 with vpunch
    reham "MFHMMMMM?!"
    mc "R-Reham?"
    scene 106_s21 with Dissolve(1.0)
    reham "*cough* *cough* I apologzie... that was a lot more than I thought. Ugh..."
    scene 106_s20 with dissolve
    m "*laughs* It's in your nose!"
    scene 106_s21 with dissolve
    reham "I know... *achoo*! ...*sniff*."
    reham "Could you please find me a cloth?"
    scene 106_s20 with dissolve
    m "Right away."
    scene 106_s21 with dissolve
    scene 106_s22 with Fade(1.0,1.0,1.0)
    reham "There. All cleaned up~ I hope I did well to service you, Master. But now, it's time to rest. We'll be with you, of course."
    scene 106_s23 with dissolve
    call screen scene106_choice01 with dissolve

label scene106_bj_cum_b:
    mc "I'll cover you both!"
    if s106_bj_maia or s106_bj_reham:
        scene black with Dissolve(0.3)
        show s106_bj3 with dissolve
    m "Yes... please... cover us in your seed, [mx]~ Let us know who we belong to."
    reham "Oh dear, I hope it's ease to clean."
    m "Look at us... waiting for your load... give it to us~!"
    scene 106_s44 with Dissolve(0.3)
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene 106_s44 with vpunch
    if s106_bj_maia:
        perception "Maia pulls your cock from her throat, and it immediatly start spraying them in hot, white ropes."
    elif s106_bj_reham:
        perception "Maia pulls your cock from her throat, and it immediatly start spraying them in hot, white ropes."
    else:
        m "Ahnn~!"
    scene 106_s45 with Dissolve(0.3)
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene 106_s45 with vpunch
    perception "Your warm seed finds Reham's cheek and lips, then Maia's forehead and tongue, then back and forth as they tilt their heads to catch every spurt."
    reham "Mmm... S-So much!"
    scene 106_s47 with Dissolve(1.5)
    m "It's everywhere! I love it~ T-Thank you, [mx]."
    scene 106_s46 with dissolve
    reham "Hahh... it was certainly intense... I need to go wash my face now."
    if not maia_virgin:
        scene 106_s47 with dissolve
        m "Let it stay for a while! You can't treat [mx]'s seed like it's an unpleasant thing. You should be proud of it."
        scene 106_s48 with dissolve
        mc "(Did I do this to her?! When did she get so... smutty?)"
    else:
        scene 106_s48 with dissolve
    scene 106_s22 with Fade(1.5,1.0,1.5)
    reham "There. All cleaned up~ I hope I did well to service you, Master. But now, it's time to rest. We'll be with you, of course."
    scene 106_s23 with dissolve
    call screen scene106_choice01 with dissolve

default scene106_reham_anal = False
default scene106_reham_anal_rejected = False
label scene106_choice01_op1:
    if maia_pussy_sex > 0:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
    if maia_anal_sex > 0:
        $ maia_anus_virgin = False
        $ maia_virgin = False
    if maia_pregnant:
        $ maia_pussy_virgin = False
        $ maia_virgin = False

    mc "That's not happening anytime soon."
    scene 106_s22 with dissolve
    reham "W-What?"
    scene 106_s23 with dissolve
    m "Mmm?"
    mc "Prepare for more. I'm not finished with you yet."
    scene 106_s22 with dissolve
    reham "Are you sure, Master? I-I really must insist that—"
    scene 106_s23 with dissolve
    mc "You really think I can stop now? After you two made such a mess on the floor with your juices like snails?"
    scene 106_s22 with dissolve
    reham "I... Well..."
    scene 106_s23 with dissolve
    mc "*chuckles* Exactly. Look at the state you're in. It would be cruel to stop now."
    mc "Lie down, Reham."
    scene 106_s22 with dissolve
    reham "As you wish, Master. But just know that I'm... still a virgin."
    scene 106_s24 with Dissolve(1.0)
    m "I'll help you!"
    scene 106_s25 with dissolve
    reham "Help me? {i}How{/i}?"
    scene 106_s24 with dissolve
    m "Hehe~"
    play sound "sound_effects/body/clothes1.mp3"
    scene black with vpunch
    reham "Hey!"
    scene 106_s28 with Fade(1.0,1.0,1.0)
    perception "Maia gently takes Reham's ankles, folding her legs back toward her chest."
    scene 106_s26 with dissolve
    m "There you go, [mx]. All open for you."
    scene 106_s28 with dissolve
    mc "Where would I be without you..."
    scene 106_s27 with dissolve
    reham "This is so embarrassing! Please don't look directly at it!"
    scene 106_s26 with dissolve
    m "Too late~ Look how pretty she is down here... shiny~"
    scene 106_s27 with dissolve
    reham "I... I trust you. Just... go slow?"
    $ scene106_reham_anal = True
    scene 106_s28 with dissolve
    call screen scene106_presex with dissolve

default scene106_r_presex_v = True
default scene106_r_presex_a = True
default scene106_r_presex_v_second = True
default scene106_r_presex_a_second = True

default scene106_sex_mis = True
default scene106_sex_doggy = False

default scene106_sex_maia = False
default scene106_sex_reham = False

default scene106_sex_v = False
default scene106_sex_a = False

default scene106_sex_pov = False




label scene106_sex_reham_v:
    $ reham_pussy_virgin = False

    $ scene106_sex_v = True
    $ scene106_sex_a = False

    $ scene106_sex_mis = True
    $ scene106_sex_doggy = False

    $ scene106_sex_maia = False
    $ scene106_sex_reham = True

    if scene106_r_presex_v:
        $ scene106_r_presex_v = False
        scene 106_s29 with Dissolve(1.0)
        play sound "se_sfx/sex/sex4.mp3" 
        sensation "You press the head against her wet enterance. She gasps sharply as you ease in, inch by inch, her walls fluttering around you like they're trying to pull you deeper and push you away at the same time."
        reham "Ahhn~! It's... it's stretching me!"
        m "Breathe, Reham. You're doing so good... look how well you're taking him."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 106_s30 with Dissolve(1.0)
        reham "Uhgnnn!"
        mc "You okay?"
        reham "Y-Yes... you can start moving."

        if scene106_sex_pov:
            scene black with Dissolve(0.3)
            show s106_r_vsex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s106_r_vsex1 with dissolve

        sensation "You start fast with deep thrusts. Her body adjusts quickly, wetness easing the way, walls clenching rhythmically."
        reham "Ahhn! Master! Umnnn~! Aren't you being a little too... Ahhn! ...rough considering this is my first time?"
        mc "Sorry, I already know that I'm going to be addicted to this pussy."
        reham "Fhnhn~! You're bounding it so fast~!"
        m "It's going to feel so good~"
        reham "Don't—don't say that..."
        m "Congratulations on losing your virginity!"
        reham "Ahhhh~! Fhhnnnmm~! I feel you all the way inside my stomach!"
        mc "How does it feel?"
        reham "I'm not sure... I always thought about how I'd eventually get married and children. I never... Ahhn~! ...thought it would be like this!"
    elif scene106_r_presex_v_second:

        if scene106_sex_pov:
            scene black with Dissolve(0.3)
            show s106_r_vsex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s106_r_vsex1 with dissolve

        $ scene106_r_presex_v_second = False
        mc "Your pussy must be cooking by now. I'll give it a good stirring!"
        reham "Ahhn~!"
        sensation "You thrust into her pussy, now slightly more open from earlier pounding. She tries her best to relax and let you in deeper."
        mc "You're dripping everywhere."
        if not reham_anus_virgin:
            reham "Because of you! Unnmgg~! Because you just had my ass... it's making me crazy! To think I lost both my vagina and ass virginity in the same day!"
        else:
            reham "Because of you! Unnmgg~! Your large cock... it's making me crazy! I'm glad I lost my virginity to you, Master!"
        reham "You can go harder... please... I need to feel you claim every part of me, Master. I must get used to this if I'm to service you properly!"
    else:
        if scene106_sex_pov:
            scene black with Dissolve(0.3)
            show s106_r_vsex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s106_r_vsex1 with dissolve

        if not reham_anus_virgin:
            mc "You love being filled everywhere, don't you?"
            reham "Yes~! I love it... I love being your dirty little hole! Don't stop switching... use me like you own me, master!"
        else:
            mc "You love being filled like this, don't you?"
            reham "Yes~! I love it... I love being your dirty little hole! Use me like you own me, master!"
        m "Whoa... She's really lost it."

    call screen scene106_sex with dissolve

label scene106_sex_reham_a:
    $ scene106_sex_v = False
    $ scene106_sex_a = True
    
    $ scene106_sex_mis = True
    $ scene106_sex_doggy = False
    
    $ scene106_sex_maia = False
    $ scene106_sex_reham = True

    if scene106_r_presex_a:
        $ scene106_reham_anal_decide = True
        $ scene106_r_presex_a = False
        mc "I want your ass."
        scene 106_s32 with Dissolve(1.0)
        reham "M-My ass?! But... that's not allowed!"
        scene 106_s31 with dissolve
        mc "Not allowed? By who?"
        scene 106_s32 with dissolve
        reham "It's absolutely forbidden in my culture! I'm sorry, [mc], but... you can't. Not there."
        scene 106_s31 with dissolve
        if mc_harem_reham_dom or mc_harem_reham_dom_dom:
            $ scene106_reham_anal = True
            $ reham_anus_virgin = False
            mc "You're mine, Reham. You know that, don't you?"
            scene 106_s32 with dissolve
            reham "B-But Master... it's forbidden. I've never..."
            scene 106_s31 with dissolve
            mc "I know you're nervous. But I also know how wet you get when I take control."
            scene 106_s32 with dissolve
            reham "Th-That's..."
            scene 106_s31 with dissolve
            mc "You're mine. Every single part of you is mine."
            empathy "She hesitates, her breathing shaky, but after a few seconds she slowly relaxes her anus."
            play sound "se_sfx/sex/touch4.mp3" 
            scene 106_s33 with Dissolve(1.0)
            mc "Good girl."
            mc "I'm not going to hurt you. I'm going to make you feel so good you'll forget every rule you were ever taught."
            reham "Master..."
            m "Breathe. Let him in."
            play sound "se_sfx/sex/touch2.mp3" 
            scene 106_s34 with Dissolve(1.0)
            sensation "Your head goes deeper than the ring, drawing a sharp cry from her. Inch by inch, she opens for you, tight heat gripping like a fist."
            reham "It's... it's too big! I can feel how thick you are just pressing there!"

            if scene106_sex_pov:
                scene black with Dissolve(0.3)
                show s106_r_asex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s106_r_asex1 with dissolve

            mc "Tell me to stop if it's too much."
            reham "Oh Gods! You're going so deep! Ahnn~! Hannhg~! You're treating me like a whore!"
            reham "It's weird... but I want you to own me, Master! Make me scream!"
            mc "Fuck, you're so tight! I'll make this hole remember the shape of my cock!"
            reham "Please do~ Mess up my asshole, Master! Mnnnn~!"
        
        elif scene106_reham_anal:
            $ mc_anal_reham_ready = False
            $ scene106_reham_anal = False
            $ scene106_reham_anal_rejected = True
            mc "Alright... I won't force you. We did agree in the contract not to do any sexual acts in the first place."
            mc "You're already doing more than enough for me."
            scene 106_s32 with dissolve
            reham "Thank you. I'm glad you understand."
            scene 106_s31 with dissolve
            call screen scene106_presex with dissolve

    elif scene106_r_presex_a_second:
        if scene106_sex_pov:
            scene black with Dissolve(0.3)
            show s106_r_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s106_r_asex1 with dissolve

        $ scene106_r_presex_a_second = False
        mc "Back to your ass. I want to feel how much looser you are now."
        reham "Nhhnnn~! Not to fast!"
        sensation "Your cock leaves the tight heat of her pussy and pushes into the even tighter heat of her ass. It's clear she isn't yet accustomed to your size."
        reham "Ohhh Gods! it's easier now... P-Please don't make it a habit of entering my ass!"
        mc "*chuckles* I already told you that you're mine, girl."
        reham "What would my parents say if they heard about me letting a man penetrate my ass? I would be in so much trouble!"
        mc "Then we'll keep it our little secret."
        reham "Ahhhnn~! Hahhnn! You're breaking my tiny hole!"

    else:
        if scene106_sex_pov:
            scene black with Dissolve(0.3)
            show s106_r_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s106_r_asex1 with dissolve
        
        mc "Look how you're clenching... you're going to come just from me moving between your tight holes."
        reham "I feel it coming! I'm so close... please... please..."
    call screen scene106_sex with dissolve

label scene106_sex_pov:
    if scene106_sex_maia:
        if scene106_sex_v:
            if scene106_sex_pov:
                $ scene106_sex_pov = False
                scene black with Dissolve(0.3)
                show s106_m_vsex2 with dissolve
                ""
            else:
                scene black with Dissolve(0.3)
                show s106_m_vsex1 with dissolve
                ""
        else:
            if scene106_sex_pov:
                $ scene106_sex_pov = False
                scene black with Dissolve(0.3)
                show s106_m_asex2 with dissolve
                ""
            else:
                scene black with Dissolve(0.3)
                show s106_m_asex1 with dissolve
                ""
                
    else:
        if scene106_sex_v:
            if scene106_sex_pov:
                $ scene106_sex_pov = False
                scene black with Dissolve(0.3)
                show s106_r_vsex1 with dissolve
                reham "God~ You're touching all my spots~! I might... mnfnnmm~ pass out~!"
            else:
                $ scene106_sex_pov = True
                scene black with Dissolve(0.3)
                show s106_r_vsex2 with dissolve
                reham "Ahnn~! Mfmnnn~ Please mess me up hard, Master."
        else:
            if scene106_sex_pov:
                $ scene106_sex_pov = False
                scene black with Dissolve(0.3)
                show s106_r_asex1 with dissolve
                reham "My mind is going blank! Please... please... Mmmnhhnn~!"
                mc "You want it to deeper?!"
                reham "Yes! Yes! Make me screaaammm!"
            else:
                $ scene106_sex_pov = True
                scene black with Dissolve(0.3)
                show s106_r_asex2 with dissolve
                reham "[mx]~! [mx]~! [mx]~!"
                reham "So... Ahnngnm~! ...Fast! Fast~!"
                m "Does she... enjoy it or not? I can't tell."

    call screen scene106_sex with dissolve

default scene106_sex_maia_first = True

default scene106_sex_maia_v_first = True
default scene106_sex_maia_a_first = True

default scene106_sex_maia_v_second = True
default scene106_sex_maia_a_second = True

label scene106_sex_maia_pre:
    $ scene106_sex_maia_first = False
    mc "Take a rest, Reham."
    reham "Ahh... thank you..."
    m "*giggles* My turn!"
    scene 106_s51 with Fade(1.5,1.0,1.0)
    perception "Maia lies on her back eagerly, legs parting as you kneel between them. You grip her hips possessively, thumbs brushing the sweaty skin just above her hip bones."
    scene 106_s50 with dissolve
    if maia_pussy_sex > maia_anal_sex:
        m "My pussy is already wet from watching you play with Reham, [mx]~"
        m "You can thrust as hard as you want and it wouldn't hurt~!"
        if not maia_pregnant:
            m "And... maybe you can... breed me now, [mx]?"
            scene 106_s51 with dissolve
            mc "You wanna get pregnant?"
            scene 106_s50 with dissolve
            m "Yes! Yes! Yes! Please breed me, [mx]! I want to have a baby with you~"
            scene 106_s51 with dissolve

    elif maia_anal_sex > maia_pussy_sex:
        m "My butt is ready for you, [mx]~"
        scene 106_s51 with dissolve
        reham "You're starting with your ass?"
        scene 106_s50 with dissolve
        if maia_pussy_sex == 0:
            m "Mhm! [mx] likes it only in my butt!"
            scene 106_s51 with dissolve
            reham "{i}Only?{/i} Y-You haven't done it once in your vagina? ...You're saying you're still a virgin?!"
            scene 106_s50 with dissolve
            m "Yes. Only in the butt. Right, [mx]?"
            scene 106_s51 with dissolve
            mc "That's right."
            if reham_pussy_virgin:
                reham "Master, you haven't taken my virginity too... A-Are you also planning to do the same to me?"
                mc "Maybe."
                reham "Gods have mercy! I don't know if I can handle constant pounding this intense to my rear..."
                reham "*sigh* I suppose I'll need to make a habit of loosening my asshole from now on."
                mc "*chuckles* No need. I'll be more than happy to do that for you."
            else:
                reham "I see..."
        else:
            m "Mhm! [mx] prefers to make love to my butt more than my pussy."
            scene 106_s51 with dissolve
            reham "You seem weirdly happy about that..."
    else:
        m "I'm ready for you, [mx]. Please stick your cock inside your wife and make her feel good~"
        scene 106_s51 with dissolve
    call screen scene106_sex_maia_v with dissolve

label scene106_sex_maia_v:
    if scene106_sex_maia_first:
        jump scene106_sex_maia_pre
    
    $ scene106_sex_v = True
    $ scene106_sex_a = False
    
    $ scene106_sex_mis = True
    $ scene106_sex_doggy = False
    
    $ scene106_sex_maia = True
    $ scene106_sex_reham = False

    if scene106_sex_maia_v_first:
        $ scene106_sex_maia_v_first = False
        if maia_pussy_virgin:
            $ maia_pussy_virgin = False
            scene 106_s52 with Dissolve(1.5)
            play sound "se_sfx/sex/touch2.mp3" 
            m "Aghhn~ You're finally doing it, [mx]..."
            mc "Doing what?"
            scene black with Dissolve(0.3)
            show s106_m_vsex1 with dissolve
            m "Fhnngn~! Using my pussy... I-I'm still a virgin, didn't you know?"
            mc "Ah... right. I did keep you waiting, huh?"
            m "For soooo long!"
            reham "You two seriously haven't had sex yet? What kind of relationship did you have..."
            if maia_pussy_sex == 0 and maia_anal_sex > 0:
                m "It's because [mx] only likes to mate with my butt~"
                m "He trained me on only liking it there, and now... I-I'm addicited to the feeling~"
        else:
            scene black with Dissolve(0.3)
            show s106_m_vsex1 with dissolve
            m "Ohhh~... yes!"
            m "Don't be afraid of being rough, [mx]. I was... made for you... only you~"
            sensation "You thrust deep, the force makes her breasts bounce softly. Her wetness coats you completely, slick sounds filling the cabin with every movement."
            m "Yes! R-Right there... you're hitting that spot... please don't stop~"

    elif scene106_sex_maia_v_second:
        $ scene106_sex_maia_v_second = False
        scene black with Dissolve(0.3)
        show s106_m_vsex1 with dissolve
        sensation "She tries her best to keep you buried in, but you manage pull free and thrust deep into her pussy. You can go deeper here without worrying about hurting her."
        m "Ahhnn~ my pussy is slippery~ I'm sorry if it isn't tight for you, [mx]! I-I'm trying."
        mc "Ahhnn... You're doing well."
        m "Will you finish in my butt or pussy, [mx]? I want to know so that I-Ahhnn~! can make it feel tight and ready for you."
        mc "*chuckles* Where would you like it?"
        if maia_anal_sex > maia_pussy_sex:
            m "My butthole! I'm addictied to the feeling of you filling me there~ And how it drips afterwards."
        elif maia_pussy_sex > maia_anal_sex:
            m "My pussy! I want to have all your baby making seed~ Even if I'm pregnant."
        else:
            m "Wherever you wish, [mx]! You own my body and my pleasure holes~"
    else:
        scene black with Dissolve(0.3)
        show s106_m_vsex1 with dissolve
        m "It feels like I'm about to pee everytime you go deep inside~!"
        reham "Don't ruin the sheets please."
    call screen scene106_sex with dissolve

label scene106_sex_maia_a:
    if scene106_sex_maia_first:
        jump scene106_sex_maia_pre

    $ scene106_sex_v = False
    $ scene106_sex_a = True
    
    $ scene106_sex_mis = True
    $ scene106_sex_doggy = False
    
    $ scene106_sex_maia = True
    $ scene106_sex_reham = False

    if scene106_sex_maia_a_first:
        $ scene106_sex_maia_a_first = False
        if maia_anus_virgin:
            $ maia_anus_virgin = False
            scene 106_s53 with Dissolve(1.5)
            play sound "se_sfx/sex/touch3.mp3" 
            m "T-There?"
            mc "This is your first time in the ass, right?"
            m "Mhm~ It's alright, [mx]. I-I don't mind if you were rough like you did with Reham! My body is yours afterall~"
            scene black with Dissolve(0.3)
            show s106_m_asex1 with dissolve
        else:
            mc "I never get tired of this tiny hole."
            m "Yes... please... take it~"
            scene black with Dissolve(0.3)
            show s106_m_asex1 with dissolve
            perception "The head pops past the ring with a soft moan from her. Reham watches attentively, her expression a mix of awe and shock."
            m "Ahhn~! It's... mhnng~! So thick... stretching my ass so wide..."
            reham "H-How can you do that so comfortably?"
            m "[mc] has been... umm... really interested in my butthole ever since he met me. He trained me hard~ Right, [mx]?"
            mc "Mhm. Your asshole knows my cock well at this point."
            sensation "You sink deeper—inch by inch—her heat gripping you like a vice, tighter than her pussy, pulsing with every heartbeat."
            m "Hahhnnn~! I-I love it when you bursh against my belly~!"
            reham "Incredible..."

    elif scene106_sex_maia_a_second:
        $ scene106_sex_maia_a_second = False
        mc "Ready your ass, I'm barging in."
        m "You don't need to tell me, [mx]. It's always ready for you~"
        scene black with Dissolve(0.3)
        show s106_m_asex1 with dissolve
        sensation "As if anticipating your arrival, the walls of her colon relaxe instantly to let you in. She moans loudly as you bottom out, her pussy dripping onto your balls."
        m "Weather I'm-Hnaahh~! Weather I'm awake or asleep... weather I'm working or free. You can use my butt for your relief~"
        mc "Hahnn!"
        m "I love when you switch... feeling you move between my holes like you don't care~"

    else:
        scene black with Dissolve(0.3)
        show s106_m_asex1 with dissolve
        m "Ahhnn~ Hghnn~ Yes, please~"
        reham "She's in a complete trans..."

    call screen scene106_sex with dissolve

label scene106_sex2:
    $ scene106_sex2 = False
    mc "I want to try something."
    scene 106_s56 with Fade(1.3,1.0,1.5)
    perception "Both girls turn around. Their dripping, glistining holes are on full display for you."
    scene 106_s54 with dissolve
    reham "Umm... this looks weird, doesn't it?"
    scene 106_s56 with dissolve
    mc "Not at all, I always wanted to do something like this."
    scene 106_s55 with dissolve
    m "[mx] can pick between four holes for his pleasure, I'm so excited~"
    if mc_harem_reham_dom or mc_harem_reham_dom_dom:
        scene 106_s56 with dissolve
        call screen scene106_sex2 with dissolve
    else:
        scene 106_s54 with dissolve
        reham "Only three! My asshole is off-limits."
        scene 106_s55 with dissolve
        m "You're so boring..."
        scene 106_s56 with dissolve
    call screen scene106_sex2 with dissolve

default scene106_sex2 = True
default scene106_sex_maia_v2 = True
default scene106_sex_maia_a2 = True
default scene106_sex_reham_v2 = True
default scene106_sex_reham_a2 = True

label scene106_sex_maia_v2:
    if scene106_sex2:
        jump scene106_sex2

    $ scene106_sex_v = True
    $ scene106_sex_a = False
    
    $ scene106_sex_mis = False
    $ scene106_sex_doggy = True
    
    $ scene106_sex_maia = True
    $ scene106_sex_reham = False

    if scene106_sex_maia_v2:
        $ scene106_sex_maia_v2 = False
        if maia_pussy_virgin:
            $ maia_pussy_virgin = False
            scene 106_s58 with Dissolve(1.5)
            play sound "se_sfx/sex/touch2.mp3" 
            m "Aghhn~ You're finally doing it, [mx]..."
            mc "Doing what?"
            scene black with Dissolve(0.3)
            show s106_m_vsex2 with dissolve
            m "Fhnngn~! Using my pussy... I-I'm still a virgin, didn't you know?"
            mc "Ah... right. I did keep you waiting, huh?"
            m "For soooo long!"
            reham "You two seriously haven't had sex yet? What kind of relationship did you have..."
            if maia_pussy_sex == 0 and maia_anal_sex > 0:
                m "It's because [mx] only likes to mate with my butt~"
                m "He trained me on only liking it there, and now... I-I'm addicited to the feeling~"
            call screen scene106_sex with dissolve

        scene black with Dissolve(0.3)
        show s106_m_vsex2 with dissolve
        sensation "You line up with Maia's soaked entrance, her pussy is fully swollen now. Your cock sinks deep one thrust while her moist walls flutter and milk you as if she's begging to be inseminated."
        mc "Ahhah... You're soaking the sheets."
        reham "Nhnn... I can feel some of it splashing on me too. It's so warm."
        perception "Your powerful thrusts make Maia's whole body jolt forward. Reham's weight on her back adds pressure, making every movement feel tighter, more intense."
        m "Hannn~ My pussy's being used for [mx]'s pleasure~!"
        reham "Stop saying that word!"
    else:
        scene black with Dissolve(0.3)
        show s106_m_vsex2 with dissolve
        m "Reham's juices are dripping down on me~ She's getting excited from watching you breed me, [mx]~"
        reham "S-Sorry... I don't mean to drench you like this."
    call screen scene106_sex with dissolve

label scene106_sex_reham_v2:
    if scene106_sex2:
        jump scene106_sex2

    $ scene106_sex_v = True
    $ scene106_sex_a = False
    
    $ scene106_sex_mis = False
    $ scene106_sex_doggy = True
    
    $ scene106_sex_maia = False
    $ scene106_sex_reham = True

    if scene106_sex_reham_v2:
        $ scene106_sex_reham_v2 = False
        scene black with Dissolve(0.3)
        show s106_r_vsex3 with dissolve
        sensation "You press into Reham's glistening pussy, her walls are much tighter than Maia's. She moans low as you sink in, squeezing despite the apparent discomfort."
        reham "Mmm~! Master!"
        reham "You'll make me addicted to this feeling!"
        m "Let it happen~ [mx] is more than ready to deliver."
        mc "Hmm? You're starting to clench like you want to keep me in there."
        reham "I am~ I want you stay buried in me."
        perception "Reham's body rocks forward with each thrust. The stacked position makes every movement echo through both girls."
    else:
        scene black with Dissolve(0.3)
        show s106_r_vsex3 with dissolve
        reham "Hahhn~! T-This isn't a safe day, Master. Be careful not to impregnate me."
        reham "I cannot raise a child in these conditions."
    call screen scene106_sex with dissolve

label scene106_sex_maia_a2:
    if scene106_sex2:
        jump scene106_sex2

    $ scene106_sex_v = False
    $ scene106_sex_a = True
    
    $ scene106_sex_mis = False
    $ scene106_sex_doggy = True
    
    $ scene106_sex_maia = True
    $ scene106_sex_reham = False

    if scene106_sex_maia_a2:
        $ scene106_sex_maia_a2 = False
        mc "Maia. Push back for me."
        if maia_anus_virgin:
            $ maia_anus_virgin = False
            scene 106_s57 with Dissolve(1.0)
            m "T-There?"
            mc "This is your first time in the ass, right?"
            m "Mhm~ It's alright, [mx]. I-I don't mind if you were rough like you did with Reham! My body is yours afterall~"
            scene black with Dissolve(0.3)
            show s106_m_asex2 with dissolve
            call screen scene106_sex with dissolve

        scene black with Dissolve(0.3)
        show s106_m_asex2 with dissolve
        sensation "Her hole opens quickly, and she even pushes back to help you enter. Inside, intense heat and grip welcomes you."
        m "Hnnngh~!"
        m "I love it when you ruin my butthole, [mx]~ Because after you're done with it, I can still feel in there throughout the whole day~!"
        reham "She's a completely different person when you penetrate her anus... Just what have you done to this girl?"
        mc "*chuckles* Nothing. She's the one who wants it."
        m "Mhnnmmn~! Yes... my butthole is made for [mx] to ruin and break."
    else:
        scene black with Dissolve(0.3)
        show s106_m_asex2 with dissolve
        m "Y-Yes~! Hahnn~"
        reham "Gods... her expression changes completely when you enter her ass."
    call screen scene106_sex with dissolve

default scene106_reham_anal_decide = False
label scene106_sex_reham_a2:
    if scene106_sex2:
        jump scene106_sex2
    
    if not scene106_reham_anal_decide:
        jump scene106_sex_reham_a

    $ scene106_sex_v = False
    $ scene106_sex_a = True
    
    $ scene106_sex_mis = False
    $ scene106_sex_doggy = True
    
    $ scene106_sex_maia = False
    $ scene106_sex_reham = True

    if scene106_sex_reham_a2:
        $ scene106_sex_reham_a2 = False
        mc "Reham. Ass up a little more."
        scene black with Dissolve(0.3)
        show s106_r_asex3 with dissolve
        sensation "You push in with great resistance, her ring still so tight it can crush your shaft. A loud moan pierces your ears as you push deeper into her colon."
        reham "Fuck! Oh! Execue me..."
        m "*laughs* She swore."
        reham "I'm s-sorry. It's just-ahhnn~! ...this is all new to me!"
        reham "It feels so wrong to be doing this... not to mention you're using us both."
        m "Don't take too long, [mx]. I want it in my butt too!"
        reham "N-Not yet! I want to get used to this... Ughmm~! It's clear that Master has a fetish for anal stuff. I have to be—Ahhn~! ...b-be ready."
    else:
        scene black with Dissolve(0.3)
        show s106_r_asex3 with dissolve
        reham "Not to rough, master! I-I know you own me now, but... please have mercy on your poor servant!"
        m "*giggles* What is she saying?"
    call screen scene106_sex with dissolve

default scene106_cum_inside = False

label scene106_sex_cum:
    call screen scene106_sex_cum with dissolve

default mc_cum_inside_reham_ass = False
default mc_cum_inside_maia_ass = False
default mc_cum_inside_reham_puss = False

label scene106_cum:
    if scene106_cum_inside:
        if scene106_sex_maia:
            if scene106_sex_v:
                $ maia_pussy_sex += 1
                m "I-I can feel it getting bigger! You want to finish inside my pussy, [mx]! Please do it very deep~!"
                if maia_pregnant:
                    reham "What if she wasn't pregnant? Would you have still taken the risk?"
                    m "I don't care! [mx] can breed me whenever he wants!"
                else:
                    reham "Wait! What if she gets pregnant?"
                    m "I don't care! [mx] can breed me whenever he wants!"
                if persistent.xray_mode:
                    scene 106_s65_xray1 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum1.mp3" 
                    scene 106_s65_xray1 with vpunch
                    sensation "Hot spurts of semen inflitrate her womb, flooding her completely. Her body convulses and her walls squeeze harder trying to draw out everything."
                    scene 106_s66_xray2 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum5.mp3" 
                    scene 106_s66_xray2 with vpunch
                else:
                    scene 106_s65 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum1.mp3" 
                    scene 106_s65 with vpunch
                    sensation "Hot spurts of semen inflitrate her womb, flooding her completely. Her body convulses and her walls squeeze harder trying to draw out everything."
                    scene 106_s66 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum5.mp3" 
                    scene 106_s66 with vpunch
                m "Nnnmmmm~!"
                m "Stay inside... just a little longer... let me keep you."
                if not maia_pregnant:
                    call pregnancy_check_maia from _________call_pregnancy_check_maia
                play sound "se_sfx/sex/touch2.mp3" 
                if persistent.xray_mode:
                    scene 106_s67_xray3 with Dissolve(1.0)
                else:
                    scene 106_s67 with Dissolve(1.0)
                mc "Hahh... Ahnn... Fuck. I got it all over your feet too."
            else:
                $ mc_cum_inside_maia_ass = True
                $ maia_anal_sex += 1
                m "Y-You want to mark my special hole~? Please bury it deep and spurt it all out!"
                scene 106_s68 with Dissolve(0.3)
                play sound "se_sfx/sex/sex_cum1.mp3" 
                scene 106_s68 with vpunch
                sensation "Her ass relaxes around you... then suddenly she clenches harder than you ever felt, pushing you over instantly."
                mc "Maia!"
                scene 106_s69 with Dissolve(0.3)
                play sound "se_sfx/sex/sex_cum5.mp3" 
                scene 106_s69 with vpunch
                sensation "You spurt deep inside her colon. She cries out sharply, body shaking, ass spasming rhythmically around you. Your cock feels like melting from the intenstity."
                m "Yes~! Deeper, [mx]! Fill my belly! I-I want to taste it in my mouth!"
                play sound "se_sfx/sex/touch2.mp3" 
                scene 106_s70 with Dissolve(1.0)
                mc "Hahh... ahh..."
                m "It's dripping to my feet, [mx]... I'm sorry that I couldn't hold it in longer, my butthole is just too loose~"
        
        else:
            if scene106_sex_v:
                $ mc_cum_inside_reham_puss = True
                mc "I'm spilling it all inside you, Reham!"
                reham "Wait! What if I get pregnant?!"
                m "Let him breed you, you're his now!"
                if persistent.xray_mode:
                    scene 106_s59_xray1 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum4.mp3" 
                    scene 106_s59_xray1 with vpunch
                    reham "But—!"
                    sensation "Thick spurts of hot cum erupts deep inside her, flooding her deepest parts. She moans, shocked as her pussy instinctively squeezes out your semen and tries to make her a mother."
                    scene 106_s60_xray2 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum9.mp3" 
                    scene 106_s60_xray2 with vpunch
                    reham "HAHHNN! Gods! There's so much!"
                    mc "Get pregnant!"
                    reham "GAHHNN~!"
                else:
                    scene 106_s59 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum4.mp3" 
                    scene 106_s59 with vpunch
                    reham "But—!"
                    sensation "Thick spurts of hot cum erupts deep inside her, flooding her deepest parts. She moans, shocked as her pussy instinctively squeezes out your semen and tries to make her a mother."
                    scene 106_s60 with Dissolve(0.3)
                    play sound "se_sfx/sex/sex_cum9.mp3" 
                    scene 106_s60 with vpunch
                    reham "HAHHNN! Gods! There's so much!"
                    mc "Get pregnant!"
                    reham "GAHHNN~!"

                call pregnancy_check_reham from call_pregnancy_check_reham
                play sound "se_sfx/sex/touch2.mp3" 
                if persistent.xray_mode:
                    scene 106_s61_xray3 with Dissolve(1.0)
                else:
                    scene 106_s61 with Dissolve(1.0)
                mc "Hahhh! Ahnn... Fuck... I might have seriously gotten you pregnant."
            else:
                $ mc_cum_inside_reham_ass = True
                reham "[mc]?! I feel your organ getting bigger... don't tell me you're intending on finishing inside my colon?"
                mc "I am. I'll make your ass as my personal cum chalice!"
                reham "{i}Cum chalice!?{/i} Please don't ever say that again!"
                scene 106_s62 with Dissolve(0.3)
                play sound "se_sfx/sex/sex_cum4.mp3" 
                scene 106_s62 with vpunch
                sensation "Thick ropes erupt deep in her colon, some even spilling out of her anus. She moans loud as the shocking heat fill the hole she never thought would be used like this."
                scene 106_s63 with Dissolve(0.3)
                play sound "se_sfx/sex/sex_cum5.mp3" 
                scene 106_s63 with vpunch
                reham "My ass! It's being filled with my master's seed!"
                mc "You're spasming out. Did you just cum from your ass?"
                play sound "se_sfx/sex/touch2.mp3" 
                scene 106_s64 with Dissolve(1.0)
                m "Oh my..."
                reham "Nghnnn... I'm... spent..."
    else:
        scene 106_s71 with Dissolve(0.3)
        play sound "se_sfx/sex/sex_cum7.mp3" 
        scene 106_s71 with vpunch
        sensation "Powerful spurts of cum shoot across their round asses, splattering over their cheeks and lower back. Their bodies tremble as they feel the hot liquid marking their skin."
        reham "Ahh~! You're doing it all over my ass~! It feels so dirty..."
        scene 106_s72 with Dissolve(0.3)
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 106_s72 with vpunch
        m "You marked me, [mx]... I can feel it sliding down my skin~"
        reham "Mmm... look at the mess you made on us~"

    if scene106_cum_inside:
        if scene106_sex_maia:
            scene 106_s43 with Fade(1.0,1.3,1.5)
        else:
            scene 106_s35 with Fade(1.0,1.3,1.5)
    else:
        scene 106_s36 with Fade(1.0,1.3,1.5)

    perception "They collapse together, Reham trembling, Maia draped over her, both breathing hard. The entire cabin smells like sex now."
    m "Haahh... Ahhnnah... I'm sorry, [mx]... we made a mess."
    mc "The best mess there is."
    scene 106_s37 with Dissolve(1.7)
    m "Reham?"
    reham "..."
    m "She's... she's sleeping!"
    mc "*laughs* I guess it was too much for her first time."
    if scene106_sex_maia:
        if scene106_sex_v:
            m "I want to sleep too, [mc]. My eyelids are getting so heavy after what you did to my pussy~"
        else:
            m "I want to sleep too, [mc]. My eyelids are getting so heavy after what you did to my butthole~"
    else:
        m "I want to sleep too, [mc]. My eyelids are getting so heavy after what you did~"
    mc "Yeah, let's take a rest."

    scene 106_s38 with Fade(1.0,1.0,1.0)
    alex "*yawn* [mc]? Can you take over? I feel like dying over here..."
    scene 106_s39 with Dissolve(1.0)
    alex "(What the—!?)"
    alex "(Did... did he do both of them... at the same time?! ...That's—)"
    alex "(No! Don't think about it... don't you think about it, Alex. Take a breath and walk away...)"
    scene 106_s40 with Dissolve(1.0)
    alex "..."
    if persistent.alex_p:
        scene 106_s41 with vpunch
        alex "(I can't stop thinking about it!)"
    elif persistent.alex_d: 
        scene 106_s42 with vpunch
        alex "(I can't stop thinking about it!)"

    alex "(I need to masturbate now!)"
    $ renpy.end_replay()
    play music "river.mp3" fadein 5.0 loop
    jump scene106
    
label scene106_choice01_op2:
    mc "I think we're done here. Thank you for treating me like this."
    scene 106_s22 with dissolve
    reham "I'm glad to hear that. Now get ready for best night sleep you ever had~"
    scene 106_s23 with dissolve
    $ renpy.end_replay()
    jump scene106

label scene106:
    scene 106_s99 with Fade(1.5,1.0,1.5)
    ""
    if mc_slept_maia_reham_106:
        scene 106_s100 with Dissolve(1.5)
        mc "Huh!? I-I can't breathe!"
        mc "Someone is choking me!"
        scene 106_s101 with dissolve
        mc "*cough* (Ahh, right.)"
        scene 107_s1 with Fade(1.0,1.0,1.0)
        perception "You untangle yourself from their bodies. Reham curls really tight in her sleep. Maia murmurs something unintelligible."
        mc "Sleep tight, you two."
    elif mc_slept_maia_106:
        scene 106_s104 with Dissolve(1.5)
        mc "*yawn*"
        scene 107_s1 with Fade(1.0,1.0,1.0)
        ""
    elif mc_slept_reham_106:
        scene 106_s102 with Dissolve(1.5)
        mc "Huh!? I-I can't breathe!"
        mc "Someone is choking me!"
        scene 106_s103 with dissolve
        mc "*cough* (Ahh, right... Wait, why is she naked?)"
        scene 107_s1 with Fade(1.0,1.0,1.0)
        ""
    else:
        mc "*yawn* Huh?! W-Where am I? (Ah, right... I almost blacked out yesterday.)"
        mc "(I have to use this power sparingly or else I might really get hurt.)"
        scene 107_s1 with Fade(1.0,1.0,1.0)
        ""
    play sound "sound_effects/doors/door_open2.mp3"
    scene 107_s2 with Dissolve(1.0)
    mc "Good morning."
    scene 107_s3 with Dissolve(1.0)
    alex "Morning..."
    scene 107_s4 with dissolve
    mc "I'll be heading out now. Take care of the place while I'm gone."
    scene 107_s3 with dissolve
    alex "Ahuh."
    scene 107_s4 with dissolve
    mc "Something wrong?"
    scene 107_s3 with dissolve
    if mc_gave_sword_reham:
        alex "I just think it's weird that you thought to give the sword to Reham first."
        scene 107_s4 with dissolve
        mc "You're still upset about that?"
        scene 107_s3 with dissolve
        alex "Of course I am. It was a stupid decision. You knew how capable I am, yet you still chose her."
        scene 107_s4 with dissolve
        mc "I had my reasons."
        scene 107_s3 with dissolve
        alex "*scoff* Sure you did."
        if mc_goblins_milesent:
            alex "And what was your reason for going with Millicent instead of me yesterday?"
            scene 107_s4 with dissolve
            mc "What's wrong with you today?"
            scene 107_s3 with dissolve
            alex "I think you're avoiding me, [mc], and it's pissing me off."
            alex "Like it or not, we're stuck together until this situation is over. After that... you can ignore me all you want."
            scene 107_s4 with dissolve
            mc "*sigh* I don't have time for this argument right now. I'm heading out."
            alex "..."
        else:
            scene 107_s4 with dissolve
            mc "*sigh* I don't have time for this, Alex. I'm heading out."
            alex "..."
    elif mc_goblins_milesent:
        alex "I just think it's weird that you chose to go with Millicent yesterday instead of me. You barely even knew her."
        scene 107_s4 with dissolve
        mc "I just wanted to get to know her a bit."
        scene 107_s3 with dissolve
        alex "*scoff* Right. Why actually stick with your teammate when you can go make new friends?"
        scene 107_s4 with dissolve
        mc "What's gotten into you today?"
        scene 107_s3 with dissolve
        alex "You're avoiding me. And it's pissing me off."
        alex "Like it or not, we're a team. You're stuck with me until this is over. After that... you can ignore me all you want."
        scene 107_s4 with dissolve
        mc "*sigh* I don't have time for this argument right now. I'm heading out."
        alex "..."
    else:
        scene 107_s3 with dissolve
        alex "N-No. Everything's fine."
        scene 107_s4 with dissolve
        mc "...If you say so."
        scene 107_s3 with dissolve
        alex "*sigh* Just shout if you need me, alright?"
    jump scene107

label scene107:
    scene 107_s5 with Fade(1.0,1.0,1.0)
    play sound "sound_effects/horse_snort.mp3"
    if mc_want_help_serena:
        mc "(Hopefully no one jumps at me from a tree this time.)"
        stop music fadeout 1.0 
        scene 107_s6 with Fade(2.0,1.0,1.5)
        play music "selene_temp.mp3" fadein 1.0 loop
        mc "Serena?"
        selene "Ah, [mc]!"
        scene 107_s7 with Dissolve(1.7)
        perception "She runs towards you, nearly slipping twice. Her hair is full of straw, her clothes worn and patched, but her smile is bright as the morning sun."
        scene 107_s8 with dissolve
        selene "You came back! I knew you would! I told mother, I said, 'He's gonna come back, just wait!' and she said, 'Don't get your hopes up, dummy,' but look! You're here!"
        scene 107_s9 with Dissolve(1.0)
        play sound "sound_effects/horse1.mp3"
        mc "[horse], please give us a little bit of room..."
        scene 107_s10 with Dissolve(1.0)
        mc "So, how are things?"
        scene 107_s11 with dissolve
        selene "I've been singin' a lot since you said you'd help. Seriously, thank you."
        scene 107_s10 with dissolve
        mc "Don't thank me yet. There's still work to do. Speaking of which—where's your mother?"
        scene 107_s11 with dissolve
        selene "Oh! She went ahead without you."
        scene 107_s10 with dissolve
        mc "But—"
        scene 107_s11 with dissolve
        selene "Don't worry. She's just tryna egg you on but she's doesn't need to, I know you wanna help."
        scene 107_s12 with dissolve
        selene "Anyway. Here! She left you a map with the location circled. I traced it with my finger so many times it almost tore, so... be careful with it, alright?"
        scene 107_s10 with dissolve
        mc "*sigh* Thank you. I just hope she hasn't already done something reckless."
        selene "..."
        mc "Well then, see you."
        scene 107_s15 with Dissolve(1.0)
        perception "She fidgets, then suddenly steps forward and takes your hand."
        scene 107_s13 with dissolve
        selene "Thank you, [mc]. It feels like... like ages since someone cared about me. Really cared, you know? Not because they had to, but because they wanted to."
        scene 107_s14 with dissolve
        mc "Serena..."
        scene 107_s13 with dissolve
        if not update0_3_1_tasks_massage_fin_uncomplete:
            selene "And you even gave my breasts a massage! *giggles* It felt so good that I almost fell asleep once you left."
            scene 107_s14 with dissolve
            mc "Ahaha... it was nothing."
            scene 107_s13 with dissolve
        selene "Umm... after this is all over... you think I can live a normal life again?"
        selene "I still want to work at the stables. Maybe find... someone. Someone nice. And have little ones, and... and grow old with them. Like the normal people do."
        scene 107_s15 with dissolve
        call screen scene107_choice01 with dissolve
    else:
        ""
        jump scene107_2

label scene107_choice01_op1:
    $ mc_kind_serena = True
    scene 107_s14 with dissolve
    mc "Of course you will. You're kind, you work hard, and you care about people. Any man would be lucky to have you."
    scene 107_s13 with dissolve
    selene "You... you really think so?"
    scene 107_s14 with dissolve
    mc "I know so. Just make sure he deserves you, alright?"
    scene 107_s13 with dissolve
    selene "I will! I'll be really picky! Like... he has to like horses! And not mind that I talk a lot and smell like sheep! And— Sorry. I'm doing it again."
    scene 107_s14 with dissolve
    mc "*chuckles* I'll be going now."
    scene 107_s13 with dissolve
    selene "Take care!"
    scene 107_s15 with dissolve
    jump scene107_2

label scene107_choice01_op2:
    $ mc_harem_serena = True
    scene 107_s75 with dissolve
    perception "Without a word, you grip her hand back. She freezes, stiff with surprise."
    scene 107_s17 with dissolve
    selene "...[mc]?"
    scene 107_s16 with dissolve
    mc "You'll have that life, Serena. I'll make sure of it."
    scene 107_s17 with dissolve
    selene "*giggles* I never seen you like this. You're serious."
    scene 107_s16 with dissolve
    mc "I am."
    scene 107_s17 with dissolve
    selene "Ermm... thank you. I will trust your word."
    scene 107_s16 with dissolve
    mc "Feel better now?"
    scene 107_s17 with dissolve
    selene "Mhm. I think I know who that 'someone' is now."
    scene 107_s16 with dissolve
    mc "*chuckles* Good for you. Take care now."
    stop music fadeout 1.0 
    scene 107_s75 with dissolve
    jump scene107_2

label scene107_choice01_op3:
    stop music fadeout 1.0 
    scene 107_s19 with dissolve
    mc "I should be going. Your mother's waiting."
    scene 107_s18 with dissolve
    selene "O-Of course! Right! Go! Save the day! Be heroic!"
    scene 107_s19 with dissolve
    mc "Take care, Serena."
    scene 107_s18 with dissolve
    selene "You too, [mc]. Come back safe, alright?"
    scene 107_s19 with dissolve
    mc "I will."
    scene black with Fade(1.0,1.0,1.0)
    empathy "As you get up on your horse, you hear her start humming again. A little shaky at first, then steadier. Trying to be brave."
    jump scene107_2

label scene107_2:
    stop sound fadeout 1.0
    scene 107_s20 with Fade(2.0,1.0,1.6)
    play music "nature.mp3" fadein 2.0 loop
    mc "(I wonder...)"
    mc "Try not to look suspicious, [horse]."
    scene 107_s21 with Fade(1.0,0.5,1.0)
    perception "You grip the rough stone with both hands and feet and begin to scale it. Your new borrowed strength makes the impossible seem effortless. Handholds you couldn't have gripped before now feel solid."
    scene 107_s22 with Dissolve(1.0)
    mc "Nghnnn! (Almost there!)"
    scene 107_s23 with Fade(0.5,0.5,0.5)
    mc "Hahh... phew. (Now how the hell do I get down?)"
    stop music fadeout 1.0 
    scene 107_s24 with Fade(1.5,1.5,1.5)
    play music "wind.mp3" fadein 1.0 loop
    merchant "Is that all, miss?"
    ml "I hope so. Actually... could you wait a moment? I may have forgotten something."
    scene 107_s25 with Dissolve (1.0)
    mc "Hm? Nadia?"
    call screen scene107_choice02 with dissolve

label scene107_choice02_op1:
    $ mc_talked_nadia_leaving = True
    stop music fadeout 1.0 
    scene 107_s26 with Fade(1.0,0.5,1.0)
    play music "wind.mp3" fadein 1.0 volume 0.5 loop
    mc "Nadia?"
    #play sound "sound_effects/body/scream2.mp3"
    #pause (0.5)
    scene 107_s27 with vpunch
    ml "KYAAHH!"
    scene 107_s29 with Dissolve(1.0)
    mc "Going somewhere?"
    scene 107_s28 with Dissolve(1.0)
    ml "[mc]?"
    empathy "Her eyes travel over you. The new prosthetic. The exhaustion etched into your face. The haunted look behind your eyes."
    ml "Ahh... look what's happened to you."
    scene 107_s31 with dissolve
    mc "I could say the same. You look seriously tired... And what's with the carriage? You're leaving?"
    scene 107_s30 with dissolve
    ml "I-I am. This city... it's all become too much, [mc]."
    if mc_harem_nadia:
        ml "Even after you helped me keep my stall... the market's all but gone now. The blast took everything. Everyone I knew there either fled or..."

    ml "The other markets started charging rent just to sell. Daily rent. And I don't have enough coin to buy my own shop, let alone a spot for my 'stall'. Not anymore."
    scene 107_s31 with dissolve
    mc "Nadia..."
    scene 107_s30 with dissolve
    ml "*scoff* I was lucky, you know. Being a little farther from the blast... the one you and that girl caused."
    ml "This city's becoming so unfamiliar. I don't recognize it anymore. I don't recognize myself in it."
    scene 107_s31 with dissolve
    mc "I can explain it all, Nadia."
    scene 107_s30 with dissolve
    ml "Save it. I have a feeling you didn't mean for any of this to happen. But that doesn't change what {i}did{/i} happen, does it?"

    if mc_harem_nadia:
        scene 107_s32 with Dissolve(1.0)
        mc "...What about us?"
        scene 107_s33 with dissolve
        ml "Us? *laughs* I only see me, [mc]. For the last few weeks, it's been only me wondering if you were dead without a grave somewhere."
        scene 107_s34 with dissolve
        mc "I'm sorry, Nadia. But you have to understand—none of this is within my control."
        scene 107_s33 with dissolve
        ml "I'm trying to understand. I am. But I can't stay here anymore. And you can't call what we had a relationship, can you?"
        scene 107_s76 with dissolve
        mc "..."
        scene 107_s33 with dissolve
        ml "I'm not angry, [mc]. I'm just... tired."
        ml "*sigh* To set your mind at ease. I found a free spot a little ways from the city."
        ml "A place wher I can set up a proper stall, a main road with plenty of travelers. Real customers, not just scraps."
        scene 107_s34 with dissolve
        mc "That sounds... good. Really."
        scene 107_s33 with dissolve
        ml "Mhm. I'll see all sorts of people. Merchants, travelers, adventurers... Maybe even someone I used to know, passing through."
    elif mc_friend_nadia:
        scene 107_s32 with Dissolve(1.0)
        mc "...So this is really goodbye, then?"
        scene 107_s33 with dissolve
        ml "It is, [mc]. This city... it doesn't feel like home anymore. Too many memories. Too much... change."
        scene 107_s34 with dissolve
        mc "I'm sorry. I never meant to drag you into any of this."
        scene 107_s33 with dissolve
        ml "*sigh* Back when we first met, I saw someone who needed a hand. I don't regret helping you."
        ml "On the contrary, I'm glad I met you, [mc]. You made my life a little brighter. You were a good friend to me."
        ml "But alas, I have to take this step if I'm to secure my future. Don't blame yourself for it, please."
        ml "Goodbye, [mc]."
    else:
        scene 107_s33 with Dissolve(1.0)
        ml "*sigh* Goodbye, [mc]. I just hope you don't ruin things any further for others. Even if it was unintentional."
    scene 107_s76 with dissolve
    call screen scene107_choice03 with dissolve

label scene107_choice03_op1:
    $ mc_offer_nadia_coin = True
    if mc_coin >= 100:
        scene 107_s35 with Dissolve(1.0)
        play sound "sound_effects/karma_more.mp3" volume 0.2
        if mc_karma < 10:
            $ mc_karma += 1
        $ karma_more = True
        show screen stat_change with easeinright
        mc "Here. It's not much, but... it might be enough to rent a spot. Just for a start."
        scene 107_s36 with dissolve
        ml "[mc]... why would you do this?"
        hide screen stat_change with easeoutright
        $ karma_more = False
        scene 107_s35 with dissolve
        if mc_harem_nadia:
            call screen scene107_choice04 with dissolve
        else:
            jump scene107_choice04_op2
    else:
        mc "(I don't even have that amount of coin... any less would probably not be enough.)"
        call screen scene107_choice03 with dissolve

label scene107_choice04_op1:
    scene 107_s38 with Dissolve(1.0)
    mc "Because I still want you, Nadia. I know I've been absent, but I don't want to lose you."
    scene 107_s37 with dissolve
    ml "You're not losing me, [mc]. You already did... weeks ago."
    ml "I can't take this, not if it comes with strings."
    scene 107_s38 with dissolve
    mc "There are no strings."
    scene 107_s37 with dissolve
    ml "*sigh* You should leave. The guards patrol these streets now. They won't ask questions before swinging."
    ml "Goodbye."
    scene 107_s39 with Dissolve(1.5)
    impulse "Even after all that... she still walks away? Fine. Let the ungrateful bitch go. She never deserved you anyway, king."
    call screen scene107_choice05 with dissolve

label scene107_choice04_op2:
    scene 107_s38 with Dissolve(1.0)
    mc "I'm just trying to help. I can't watch you struggle and do nothing."
    scene 107_s37 with dissolve
    ml "You always were too kind for your own good."
    scene 107_s38 with dissolve
    mc "Please. No strings. Just... let me do this."
    scene 107_s37 with dissolve
    ml "Thank you, [mc]. But I have to decline. This isn't about the money afterall."
    scene 107_s38 with dissolve
    mc "Nadia—"
    scene 107_s37 with dissolve
    ml "For once in my life... let me think about myself. Let me make my own way."
    scene 107_s38 with dissolve
    mc "..."
    scene 107_s37 with dissolve
    ml "You should leave. The guards patrol these streets now. They won't ask questions before swinging."
    ml "Goodbye."
    scene 107_s39 with Dissolve(1.5)
    if mc_harem_nadia:
        impulse "Even after all that... she still walks away? Fine. Let the ungrateful bitch go. She never deserved you anyway, king."
        call screen scene107_choice05 with dissolve
    else:
        ""
        scene 107_s40 with Dissolve(1.0)
        mc "..."
        jump scene108

label scene107_choice03_op2:
    scene 107_s34 with dissolve
    mc "Nadia, wait. We can find another way. You don't have to leave."
    scene 107_s33 with dissolve
    ml "What way? Tell me. What future is there for me here?"
    scene 107_s34 with dissolve
    mc "I... I don't know yet. But—"
    scene 107_s33 with dissolve
    ml "But nothing. You're chasing ghosts, [mc]. Fighting battles I don't understand. I can't wait around for a maybe."
    ml "Take care of yourself. Please."
    scene 107_s39 with Dissolve(1.5)
    impulse "Even after all that... she still walks away? Fine. Let the ungrateful bitch go. She never deserved you anyway, king."
    call screen scene107_choice05 with dissolve

label scene107_choice03_op3:
    $ mc_convinced_nadia_stay = False
    scene 107_s39 with Dissolve(1.5)
    ""
    scene 107_s40 with Dissolve(1.0)
    if mc_harem_nadia:
        empathy "For a moment, she hesitates... maybe she was waiting for you to say something."
    else:
        mc "..."
    jump scene108

label scene107_choice05_op2:
    $ mc_angry_nadia = True
    mc "Fine... Go. I didn't want you anyway. Good luck survivng out there without me."
    scene 107_s40 with Dissolve(1.0)
    ml "Your true colors are showing. Looks like I made the right choice."
    mc "..."
    jump scene108
    
label scene107_choice05_op1:
    $ mc_convinced_nadia_stay = True
    scene 107_s41 with Dissolve(0.3)
    play sound "sound_effects/doors/door_kick.mp3"
    scene 107_s41 with vpunch
    ml "Huh?!"
    scene 107_s42 with dissolve
    mc "I can't."
    stop music fadeout 1.0 
    scene 107_s43 with dissolve
    ml "C-Can't what?"
    play music "hope/mountain_mist.mp3" fadein 3.0 loop
    scene 107_s42 with dissolve
    mc "Can't let you leave. Not like this."
    ml "..."
    mc "These past few weeks... I've been living in fear. Everything I had was taken from me in a single day. My hand. My position. My purpose."
    mc "At first, it felt easier to just give up. To let the current take me. But I didn't because there are people depending on me now. People who believe in me. And I'll be damned if I let them down."
    scene 107_s43 with dissolve
    ml "What does that have to do with me?"
    scene 107_s44 with dissolve
    mc "Everything. I realized that the life of a noble's lapdog wasn't a life at all. But this... standing here, talking to you, feeling something real..."
    mc "I want you to stay, Nadia. Not because it's the right thing to do, but because I {i}want{/i} you."
    mc "I can't promise I'll be here tomorrow. Or the day after. I'm in the middle of something dangerous, and I won't lie to you about that."
    mc "But I can promise that I'm working my absolute hardest to survive it. And when it's finally over... I'll come back to you."
    scene 107_s45 with dissolve
    ml "*laughs* ...You're an idiot."
    scene 107_s44 with dissolve
    mc "I know."
    scene 107_s45 with dissolve
    ml "A lovable idiot."
    scene 107_s44 with dissolve
    mc "Is that a yes?"
    scene 107_s46 with Dissolve(0.3)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    scene 107_s46 with vpunch
    empathy "She steps forward and cups your face in her hands. She then gives you a deep, desperate kiss, pouring weeks of fear and longing into a single moment."
    scene 107_s47 with Dissolve(1.0)
    ml "Yes."
    scene 107_s48 with dissolve
    mc "Yes?"
    scene 107_s47 with dissolve
    ml "I'll stay."
    scene 107_s48 with dissolve
    mc "Really?"
    scene 107_s47 with dissolve
    ml "But you have to promise me. Even if you're not here... send me letters. Let me know you're alive. Anything."
    scene 107_s48 with dissolve
    mc "I'll write so often you'll get sick of reading them."
    scene 107_s47 with dissolve
    ml "*chuckles* I won't, but you can try."
    scene 107_s48 with dissolve

    if mc_offer_nadia_coin:
        mc "And I'll still give you the hundred coins to rent a shop. Just enough for a while anyway."
        scene 107_s49 with dissolve
        ml "[mc]... that's—"
        scene 107_s50 with dissolve
        mc "I know you already refused, but it's different this time."
        scene 107_s47 with dissolve
        ml "...Fine. But I'm keeping track. You're getting every coin back with interest."
    
    scene 107_s53 with Dissolve(1.0)
    ml "Even when you weren't here... you never left my mind, you know?"
    ml "Someone selfless who helped me even though he knew nothing about me. Who asked for nothing in return. I knew that losing someone like that would hurt. A lot."
    scene 107_s52 with dissolve
    mc "I'm glad you didn't have to find out."
    scene 107_s53 with dissolve
    ml "I'm glad too."
    ml "Are you... busy right now? I could make you a cup of milk-tea. If you have time."

    if mc_lactose_intolerant:
        ml "Ah, right. You said you're lactose intolerant. Just tea, then?"

    scene 107_s77 with dissolve
    call screen scene107_choice06 with dissolve
    
label scene107_choice06_op1:
    scene 107_s52 with dissolve
    mc "That sounds nice."
    scene 107_s51 with Dissolve(0.8)
    ml "On it! Oh... wait. All my teapots and everything else are still on the carriage."
    scene 107_s52 with Dissolve(0.8)
    mc "Let's bring them in then. Make this place feel like home again."
    scene 107_s77 with dissolve
    scene 107_s54 with Fade(0.5,0.5,0.5)
    ml "Sorry, sir! Change of plans! I'm not going anywhere today."
    merchant "Huh?!"
    stop music fadeout 1.0 
    scene 107_s55 with Fade(1.3,1.0,1.3)
    play music "nadia.mp3" fadein 5.0 volume 0.8 loop
    ml "Your hand... How are you moving it like that? It looks so natural."
    scene 107_s78 with dissolve
    call screen scene107_choice07 with dissolve

label scene107_choice07_op1:
    scene 107_s56 with dissolve
    mc "I made a pact with a demon lord and sold my soul for it."
    scene 107_s55 with dissolve
    ml "*laughs* Now wouldn't that be something! Personally, I'd rather stay limbless than burn for eternity in the afterlife."
    jump scene107_3

label scene107_choice07_op2:
    scene 107_s56 with dissolve
    mc "Magic!"
    scene 107_s55 with dissolve
    ml "*laughs* Oh, well that makes perfect sense then!"
    jump scene107_3

label scene107_choice07_op3:
    scene 107_s56 with dissolve
    mc "I'm not sure myself."
    scene 107_s55 with dissolve
    ml "Hmm... Some kind of powerful magic must be involved. If that's true, mages would become richer than surgeons overnight."
    jump scene107_3

label scene107_3:
    ml "Does it feel like a real hand? Can you actually feel things with it?"
    scene 107_s56 with dissolve
    mc "Mostly. It's strange... There's like a thin layer between me and whatever I touch. But it moves just like my own."
    scene 107_s55 with dissolve
    ml "The things people can do when they have to..."
    scene 107_s57 with Dissolve(2.0)
    perception "She pours you another cup, then another."
    scene 107_s58 with dissolve
    ml "You know... I almost joined a proper merchant guild a couple years ago. Real contracts, caravans, the whole thing."
    scene 107_s57 with dissolve
    mc "What happened?"
    scene 107_s58 with dissolve
    ml "*chuckles* I fell in love with this city. The people, the quiet... By the time I came to my senses, the guild had already moved on."
    ml "I don't regret it much anymore. If I had gone... I wouldn't be sitting here with you right now. And I'm rather glad I stayed."
    scene 107_s57 with dissolve
    mc "I'm glad too."
    scene 107_s59 with Dissolve(1.0)
    shiver "A cold shiver runs down your spine as a vision flashes behind your eyes—the city completely empty, streets silent, houses dark. A peace so absolute it feels like death."
    minthra "Forget these feelings of comfort, vessel. Attachment is weakness. Remember that."
    scene 107_s61 with dissolve
    ml "You know what I dream about?"
    scene 107_s60 with dissolve
    mc "What?"
    scene 107_s61 with dissolve
    ml "A little shop. Nothing too fancy... just big enough for me to arrange everything nicely."
    scene 107_s58 with Dissolve(1.0)
    ml "I'd sell fresh milk that still carries the morning chill. Warm bread that steams when you break it open. Things so good that people never forget the taste."
    scene 107_s57 with dissolve
    mc "..."
    scene 107_s58 with dissolve
    ml "Maybe you'll visit me between your adventures. *giggles* Or better yet... work together."
    scene 107_s57 with dissolve
    mc "Maybe."
    mc "Well... I should get going. Thanks for the drink, Nadia. It was really nice seeing you again."
    scene 107_s62 with Dissolve(1.0)
    ml "A-Already? Before you set off on your journey..."
    scene 107_s63 with dissolve
    mc "Hmm?"
    scene 107_s62 with dissolve
    if mc_nadia_pregnant:
        scene 107_s62 with dissolve
        ml "I'm... I'm pregnant, [mc]."
        scene 107_s63 with dissolve
        mc "A-Ah... right."
        scene 107_s62 with dissolve
        ml "You knew that, right? You came inside me last time. It was only natural."
        scene 107_s63 with dissolve
        mc "Yeah... I figured. How far along are you?"
        scene 107_s62 with dissolve
        ml "Not very. It's still really early."
        ml "To be honest... I'm a little scared. Especially because I was planning to leave."
        ml "But knowing you'll be here to support me makes me feel a lot better. And hopefully we can secure a safe future for our child."
        scene 107_s63 with dissolve
        mc "I'll be there for you, Nadia. No matter what. Take good care of yourself while I'm away."
        scene 107_s62 with dissolve
        ml "I will."
    else:
        ml "Perhaps you could come see me first... when you have time."
        scene 107_s63 with dissolve
        mc "*chuckles* I'll see how things turn out."
        scene 107_s62 with dissolve
        ml "I was really hoping we could lay together today, but... Mother Nature had other plans."
        ml "Bad timing, as usual."
        scene 107_s63 with dissolve
        mc "We'll have plenty of time later."
        scene 107_s62 with dissolve
        ml "I know~"
    scene 107_s63 with dissolve
    call screen scene107_choice08 with dissolve

label scene107_choice08_op1:
    mc "Goodbye, Nadia."
    scene 107_s74 with Fade(1.5,1.0,1.5)
    stop music fadeout 2.0 
    ""
    jump scene108

label scene107_choice08_op2:
    scene 107_s64 with Dissolve(1.0)
    stop music fadeout 3.0 
    ml "*giggles* Such a piercing gaze... I wonder what you're staring at~"
    call screen scene107_choice09 with dissolve

label scene107_choice09_op1:
    mc "Your breasts."
    ml "Bold, aren't you~?"
    scene 107_s65 with Fade(0.5,0.5,0.5)
    ""
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 107_s66 with Dissolve(1.5)
    ml "How about you admire them a little closer then, hmm? My treat before you go."
    scene 107_s67 with dissolve
    call screen scene107_choice10 with dissolve

label scene107_choice10_op1:
    $ mc_played_nadia_boobs = True
    call screen scene107_boobs with dissolve

default scene107_boobs_right_b_first = False
default scene107_boobs_left_b_first = False
default scene107_boobs_nipples_first = False

label scene107_boobs_right_b:
    if not scene107_boobs_right_b_first:
        $ scene107_boobs_right_b_first = True
        scene 107_s68 with Dissolve(1.0)
        sensation "You cup her large right breast. Her skin is cool but incredibly smooth."
        scene 107_s69 with Dissolve(1.0)
        mc "God... it's like a soft pillow. I feel like I could sleep on them for months."
        ml "I'm glad you like them. Maybe once you're done... we can make that a reality? Not for months, though~"
    else:
        scene 107_s68 with Dissolve(1.0)
        ml "Ahnnm~"
        scene 107_s69 with Dissolve(1.0)
        mc "Why don't you start a business selling your breast milk?"
        ml "That sounds so stupid I'm not even going to humor you..."
    scene 107_s67 with Dissolve(1.0)
    call screen scene107_boobs with dissolve

label scene107_boobs_left_b:
    if not scene107_boobs_left_b_first:
        $ scene107_boobs_left_b_first = True
        scene 107_s70 with Dissolve(1.0)
        ml "You're not going to use your metallic hand?"
        mc "It might be cold. I didn't want to make you uncomfortable."
        scene 107_s71 with Dissolve(1.0)
        ml "[mc]... you're such a gentleman~"
        ml "Mmmhnn~ Dig deeper please... squeeze them harder~"
    else:
        scene 107_s70 with Dissolve(1.0)
        ml "Are my plumb breasts to your liking, sire?"
        scene 107_s71 with Dissolve(1.0)
        mc "*laughs* Why are you speaking like a noble?"
        ml "I thought you'd like that... having lived in the castle and all."
    scene 107_s67 with Dissolve(1.0)
    call screen scene107_boobs with dissolve

label scene107_boobs_nipples:
    if not scene107_boobs_nipples_first:
        $ scene107_boobs_nipples_first = True
        scene 107_s72 with Dissolve(1.0)
        ml "Uhhnn~!"
        mc "You're making such lewd noises."
        scene 107_s73 with Dissolve(1.0)
        ml "You expect me to stay quiet... nhnn~ ...while you're fondling and teasing my nipples like this?"
        ml "I'm starting to get wet... trust me, you don't want that to happen now~!"
    else:
        if mc_nadia_pregnant:
            scene 107_s72 with Dissolve(1.0)
            ml "Only a couple more months before they start pouring milk~"
            mc "Mmm..."
            scene 107_s73 with Dissolve(1.0)
            ml "*giggles* Why are you licking your lips? That milk is for our little one, not you."
            mc "We can both share from time to time."
        else:
            scene 107_s72 with Dissolve(1.0)
            ml "You're just trying to make me moan louder, aren't you?"
            scene 107_s73 with Dissolve(1.0)
            mc "I am."
            ml "Hnnmmn~!"
    scene 107_s67 with Dissolve(1.0)
    call screen scene107_boobs with dissolve

label scene107_boobs_fin:
    mc "Thank you. Now I won't have to think about them for a while."
    scene 107_s66 with dissolve
    ml "Only a while?"
    scene 107_s67 with dissolve
    mc "Of course not! I'll need to admire them constantly from now on!"
    ml "Mmmm~"
    mc "*sigh* But that will have to wait for another time."
    scene 107_s66 with dissolve
    ml "R-Right!"
    scene 107_s67 with dissolve
    scene 107_s74 with Fade(1.5,1.0,1.5)
    ""
    jump scene108

label scene107_choice10_op2:
    mc "No need. Just looking at you is already enough motivation."
    scene 107_s66 with dissolve
    ml "My, my... Even with such a plump pair of breasts right in front of you, you still have that much self-control? I'm not as worried about you anymore~"
    scene 107_s67 with dissolve
    mc "*chuckles* Goodbye, Nadia."
    scene 107_s74 with Fade(1.5,1.0,1.5)
    ""
    jump scene108
    
label scene107_choice09_op2:
    mc "Ah... nothing."
    ml "If you say so~"
    scene 107_s74 with Fade(1.5,1.0,1.5)
    ""
    jump scene108

label scene107_choice06_op2:
    scene 107_s52 with dissolve
    mc "I'd love to, but... We'll sip tea together later. When this is over."
    scene 107_s53 with dissolve
    ml "You have people depending on you. I know."
    ml "Go. I'll be here when you're done."
    scene 107_s52 with dissolve
    mc "Thank you, Nadia."
    scene 107_s51 with Dissolve(0.8)
    ml "Before you go... Could you at least help me bring my things back inside? My back is sore from all the hauling I did."
    scene 107_s52 with Dissolve(0.8)
    mc "*chuckles* Of course."
    scene 107_s77 with dissolve
    stop music fadeout 1.0 
    scene 107_s74 with Fade(1.3,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    ""
    jump scene108

label scene107_choice02_op2:
    mc "(Whatever's going on with her, it's none of my business.)"
    jump scene108
    
label scene108:
    scene 108_s1 with Fade(1.5,1.0,1.5)
    mc "(No one expects a fugitive to barge into a brothel, right? Fingers crossed.)"
    stop music fadeout 1.0 
    scene 108_s2 with Fade(1.0,1.0,1.0)
    play music "diana.mp3" fadein 3.0 loop
    perception "The familiar scent of perfume, cheap wine, and sweat fills the air."
    scene 108_s3 with Fade(0.5,0.5,0.5)
    di "Welcome, sir. What can I get you?"
    scene 108_s4 with Dissolve(1.0)
    di "S-Sir! You can't be back here!"
    play sound "sound_effects/body/clothes1.mp3"
    scene 108_s5 with Dissolve(1.0)
    di "Sir!? What are you—put me down!"
    scene 108_s6 with Dissolve(1.0)
    vera "Ah, finally! Someone actually asked for you, girl. About time."
    scene 108_s7 with dissolve

    if mc_harem_diana:
        di "But I don't do that kind of work anymore! I already have—I have someone!"
        scene 108_s6 with dissolve
        vera "Oh hush. Be grateful someone noticed you. Now go on, be nice."
        scene 108_s7 with dissolve
        di "Put me down, you brute! When I get my hands on you—"
    else:
        di "I get it, alright? But not like this! At least ask me first, dammit!"
        scene 108_s6 with dissolve
        vera "That's the spirit, girl. Earn your keep."
        scene 108_s7 with dissolve

    stop music fadeout 1.0 
    scene 108_s8 with Fade(1.0,1.0,1.0)
    di "What the hell was that?! Do you think because I work here you can just—"
    scene 108_s9 with dissolve
    di "...[mc]?"
    scene 108_s10 with dissolve
    mc "Hey, Diana."
    scene 108_s9 with dissolve
    di "*sigh* You're alive."
    di "You idiot... I thought you were dead."
    scene 108_s10 with dissolve
    mc "*chuckles* You're taking this surprisingly well."
    mc "Don't you want to know what happened?"
    scene 108_s9 with dissolve
    di "I already know enough. Some of the guards who come here can't keep their mouths shut when they're drunk."
    scene 108_s10 with dissolve
    mc "Are you not angry?"
    play music "diana2.mp3" fadein 3.0 loop
    scene 108_s11 with vpunch
    di "Angry? [mc], this is the most exciting thing that's happened in this city since... ever!"
    di "The Queen is gone. No one knows what's happening with the princess. You're running around causing chaos. It's like a story coming to life!"
    scene 108_s12 with dissolve
    mc "Huh? You think this is fun?"
    scene 108_s11 with dissolve
    di "For me? Stuck in this place, pouring drinks and smiling for men who I'd much rather kick in the eye? Yes."
    di "This is my whole world. But you're out there living the kind of story I used to read about in those cheap fantasy novels. How could I not be excited?"
    scene 108_s12 with dissolve
    mc "..."
    scene 108_s13 with Dissolve(1.0)
    if mc_lied:
        di "Remember the ogre? Sure, you lied about killing that ogre, but you still saved those farmers."
        di "That was a nice little story. But this? This is the type of story where the hero ends up on top."
    else:
        di "Remember the ogre? Sure, you saved those farmers. That was a nice little story. But this? This is the type of story where the hero ends up on top."
    scene 108_s12 with Dissolve(1.0)
    mc "I see... I'm glad you're at least optimistic about it.."
    scene 108_s11 with dissolve
    di "I want in, [mc]. I want to be part of this."
    scene 108_s12 with dissolve
    mc "In?"
    scene 108_s11 with dissolve
    di "When you win... and you {i}will{/i} win. I want to be there. Not stuck here. I want a real position in whatever comes next."
    di "I don't care what it is... maid, cook, even your personal mistress. Just... get me {i}out{/i}."
    scene 108_s12 with dissolve
    impulse "Fuckin' right you will win. This woman knows what she's talking about. You should give her a good pat on the ass for that."
    call screen scene108_choice01 with dissolve

label scene108_choice01_op1:
    mc "Come here."
    scene 108_s31 with Dissolve(0.3)
    play sound "sound_effects/slap07.mp3"
    scene 108_s31 with vpunch
    perception "You reach down and give her ass a firm, playful smack."
    if mc_harem_diana:
        di "Ahh! Hey!"
        scene 108_s22 with Dissolve(1.0)
        di "*laughs* Is this really the time for that, you pervert?"
        scene 108_s21 with dissolve  
        mc "Just rewarding you for the vote of confidence."
        scene 108_s22 with dissolve  
        di "You missed me a lot, hmm~?" 
        di "But... I suppose I don't mind that kind of reward."
        scene 108_s14 with Dissolve(1.0)

    elif mc_friend_diana:
        di "Ah! [mc]!"
        scene 108_s16 with Dissolve(1.0)  
        play sound "sound_effects/karma_less.mp3" volume 0.2
        if mc_karma > 1:
            $ mc_karma -= 1
        $ karma_less = True
        show screen stat_change with easeinright
        di "What the hell was that for, [mc]?!"
        scene 108_s17 with dissolve  
        mc "You sounded so confident. Had to reward good behavior."
        hide screen stat_change with easeoutright
        $ karma_less = False
        scene 108_s16 with dissolve  
        di "Don't do that out of nowhere, idiot... It's embarrassing."
        scene 108_s14 with Dissolve(1.0)
    else:
        di "Ahh!"
        play sound "sound_effects/karma_less.mp3" volume 0.2
        if mc_karma > 1:
            $ mc_karma -= 1
        $ karma_less = True
        show screen stat_change with easeinright
        scene 108_s16 with Dissolve(1.0)  
        di "Excuse me?! What do you think you're doing?!"
        scene 108_s17 with dissolve
        mc "You sounded so confident. Had to reward good behavior."
        hide screen stat_change with easeoutright
        $ karma_less = False
        scene 108_s16 with dissolve
        di "T-Thanks. But that's... highly inappropriate. Please don't do that again."
        scene 108_s17 with dissolve
        mc "Inappropriate? We're in a brothel."
        scene 108_s16 with dissolve
        di "Tch. Forget it."
        scene 108_s14 with Dissolve(1.0)

    di "*sigh* Anyway..."
    if mc_harem_diana:
        di "Since we're lovers... I hoped you might want me there anyway once you come out on top."
    elif mc_friend_diana:
        di "Since we're friends... I hoped you might want me there anyway once you come out on top."
    else:
        di "I know it's a lot to ask. We barely know each other... but I'm good at reading people. And you're going somewhere. I'd rather follow you than stay here."
        scene 108_s15 with dissolve
        mc "You're still on about that? I already told you there's nothing between us, Diana."
        scene 108_s14 with dissolve
        di "I-I know that, but... you can still use me!"
    jump scene108_2

label scene108_choice01_op2:
    scene 108_s14 with Dissolve(1.0)
    if mc_harem_diana:
        di "And since we're lovers... I hoped you might want me there anyway once you come out on top."
    elif mc_friend_diana:
        di "And since we're friends... I hoped you might want me there anyway once you come out on top."
    else:
        di "I know it's a lot to ask. We barely know each other... but I'm good at reading people. And you're going somewhere. I'd rather follow you than stay here."
        scene 108_s15 with dissolve
        mc "You're still on about that? I already told you there's nothing between us, Diana."
        scene 108_s14 with dissolve
        di "I-I know that, but... you can still use me!"
    jump scene108_2

label scene108_2:
    scene 108_s15 with dissolve 
    mc "I get that. But I can't risk your safety, Diana."
    scene 108_s14 with dissolve 
    di "I won't be on the frontlines, obviously. I'd be feeding you information from the shadows."
    di "I hear everything that happens in this place—guards, nobles, merchants. Listening is basically my whole job anyway."
    scene 108_s26 with Dissolve(1.0) 
    mc "What if I fail?"
    scene 108_s25 with dissolve 
    di "You won't."
    scene 108_s26 with dissolve 
    mc "You can't know that."
    scene 108_s25 with dissolve 
    di "I've watched hundreds of men walk through these doors. They all had the same exhausted, defeated look. Like they were just going through the motions."
    di "But you've never had that look. Even the first time you came in here... there was something different about you."
    scene 108_s26 with dissolve 
    mc "Different how?"
    scene 108_s25 with dissolve 
    di "Like you didn't quite belong here. Like you were from somewhere else entirely."
    mc "(She's {i}really{/i} sharp...)"
    scene 108_s14 with Dissolve(1.0) 
    di "I also picked up some valuable news from a noble who has close ties to the castle. He always tries to disguise himself, but that rich-fucker accent is impossible to miss."
    scene 108_s15 with dissolve 
    if mc_harem_diana or mc_friend_diana:
        mc "That's my girl."
        scene 108_s14 with dissolve 
        if mc_friend_diana:
            di "Friends help each other, right?"
        else:
            di "I'm glad you still see me that way."
    else:
        mc "Good job."
        scene 108_s14 with dissolve 
        di "Thank you."

    scene 108_s22 with dissolve 
    di "Actually... I have something you'll really want to know right now."
    scene 108_s21 with dissolve 
    mc "What is it?"
    scene 108_s22 with dissolve 
    di "Well... first... In case you win. W-What would my position be?"
    scene 108_s21 with dissolve 
    mc "Diana..."
    scene 108_s16 with dissolve 
    di "Just humor me, please? It's something to look forward to at least."
    di "I've spent years listening to men talk about their grand plans. Now I'm finally talking to someone who might actually make one of my dreams come true."
    di "Let a girl dream a little."
    scene 108_s17 with dissolve 
    call screen scene108_choice02 with dissolve
    
label scene108_choice02_op1:
    $ mc_promise_diana_queen = True
    mc "You'll be my queen."
    scene 108_s19 with dissolve 
    di "...What?"
    scene 108_s18 with dissolve 
    mc "If I win, I'm not leaving you behind a bar. You'll stand beside me—not as a servant or a mistress, but as my respected queen."
    scene 108_s19 with dissolve 
    di "You... you really mean that?"
    scene 108_s18 with dissolve 
    mc "Every word. You've got the sharpest mind I know. That'll serve me well if I ever sit on a throne."
    scene 108_s19 with dissolve 
    di "A queen... {i}me{/i}? Gods, the other girls would lose their minds! They'd be so jealous!"
    scene 108_s20 with dissolve 
    di "I need to tell them now!"
    scene 108_s18 with Dissolve(1.0) 
    mc "Diana! Focus."
    scene 108_s16 with Dissolve(0.8)  
    di "I'm sorry! *ahem* Alright, my king. Listen close."
    jump scene108_3

label scene108_choice02_op2:
    $ mc_promise_diana_harem = True
    mc "You'd be one of my {i}special{/i} girls. Valued. No more pouring drinks for strangers."
    scene 108_s21 with Dissolve(0.8)  
    mc "You'd be in the room where decisions are made... and you'd have my ear every night."
    scene 108_s22 with dissolve
    di "R-Really? That's... more than I hoped for."
    di "Just know that none of the other girls in your collection will hold a candle to me. I'll make sure of that~"
    scene 108_s21 with dissolve
    mc "Oh?"
    scene 108_s22 with dissolve
    di "Mhm~ Keeping me close will benefit you greatly. I'll keep your bed warm and your nights very... satisfying."
    scene 108_s16 with Dissolve(1.0) 
    stop music fadeout 1.0 
    di "*ahem* Now. Listen carefully."
    jump scene108_3

label scene108_choice02_op3:
    $ mc_promise_diana_maid = True
    mc "You'll be a regular maid."
    scene 108_s22 with dissolve
    di "...A maid? That's what being close to you gets me?"
    scene 108_s21 with dissolve
    mc "You'll be safe. A place to sleep, food in your belly, coin in your pocket. No one would look twice at you."
    mc "You'd be out of here, like you wanted."
    scene 108_s22 with dissolve
    di "I did suggest that, didn't I? *sigh* Can't really complain. It's still better than here. Much better."
    scene 108_s16 with Dissolve(1.0) 
    stop music fadeout 1.0 
    di "Alright, fair enough. Now listen up."
    jump scene108_3

label scene108_choice02_op4:
    $ mc_promise_diana_nothing = True
    mc "You won't have any position. Tell me what you know. Now."
    stop music fadeout 2.0 
    scene 108_s24 with dissolve
    di "...N-Nothing?"
    scene 108_s23 with dissolve
    mc "I can't promise what I don't know I can deliver."
    scene 108_s24 with dissolve
    di "You really mean that..."
    di "Do you... really not see anything in me worth keeping around? Please, [mc]..."
    scene 108_s23 with dissolve
    mc "I don't have time for daydreaming, Diana."
    scene 108_s16 with Dissolve(1.0)
    di "*sigh* Fine."
    di "But don't think I'm doing this out of charity. If you win and you forget about me... I'll remember."
    jump scene108_3

label scene108_3:
    play music "tense/lie.mp3" fadein 2.0 loop
    di "Avery and some important person are meeting today."
    scene 108_s17 with dissolve
    mc "Important person?"
    scene 108_s16 with dissolve
    di "I didn't catch any names or titles, but they were definitely talking about a man."
    scene 108_s17 with dissolve
    mc "(Avery's meeting a man... Hmm.)"
    scene 108_s16 with dissolve
    di "That's not all. They're meeting near the Irdan river in some closed-off mansion. I think the street was called... Eitrean's? Eitrean Lane?"
    di "It should be on the city map if you have one."
    scene 108_s17 with dissolve
    mc "This is really good, Diana. Anything else?"
    scene 108_s22 with dissolve
    di "Actually... I think it's happening right now. Ahaha... I should've said that sooner, shouldn't I?"
    scene 108_s27 with Dissolve(1.0)
    mc "What?! I need to go right now!"
    scene 108_s28 with Dissolve(1.0)
    di "Wait! You're just going to barge in? There are probably at least a dozen guards. Maybe more."
    scene 108_s29 with dissolve
    mc "I'll just listen in. Like you do."

    if mc_harem_diana or mc_friend_diana:
        scene 108_s28 with dissolve
        di "If that's the case... erm, [mc]. What about the brothel? You said you'd help me take it over."
        di "There's so much more I could learn if this place became somewhere important people aren't ashamed to visit. The kind of information that would be priceless."
        scene 108_s29 with dissolve
        if mc_coin >= brothel_coin_new:
            mc "(Huh?! I actually have enough... Where did all this coin come from?)"
            mc "Somehow I have enough to buy you this brothel, Diana. But we'll talk about it later."
        else:
            mc "I've been thinking about it, but... I don't have enough coin right now, Diana."

        if mc_harem_diana:
            mc "But I'll find a way. And if something happens to me... at least you'd still have this place."
            scene 108_s28 with dissolve
            di "Don't say that!"
        else:
            scene 108_s28 with dissolve
            di "*sigh* I see. Later then."

        di "...Next time you come, just knock on the window next to the bar. Three quick taps. I'll make a habit of glancing that way from now on."
        scene 108_s29 with dissolve
        mc "Sounds good. I have to go—I can't miss this."
        scene 108_s28 with dissolve
        di "Good luck."

    stop music fadeout 1.0 
    scene 108_s30 with Fade(0.5,1.0,1.3)
    vera "That quickly?! *scoff* A shame your first real customer was an early finisher..."
    jump scene109

label scene109:
    play music "wind.mp3" fadein 1.0 loop
    scene 109_s1 with Fade(0.5,0.5,1.0)
    mc "(A meeting outside the castle? What is she planning?)"
    scene 109_s2 with Fade(0.5,0.5,0.5)
    sensation "You suddenly feel your lungs expanding, deeper, fuller. Your legs thrum with energy, muscles coiling like springs and the world blurs."
    mc "Hahh... nghnn! Fuck! I-I feel like I'm going to puke."
    scene 109_s3 with Dissolve(1.0)
    guard "Did you see that?! Something just passed by!"
    scene 109_s4 with dissolve
    guard "*yawn* A bird?"
    scene 109_s3 with dissolve
    guard "No bird is that big, idiot!"
    if mc_want_help_serena:
        scene 109_s5 with Fade(0.5,1.0,1.4)
        lena "Ah, there you are. I was beginning to think you chickened ou—"
        scene 109_s6 with dissolve
        mc "Not now!"
        play sound "sound_effects/woosh2.mp3"
        scene 109_s8 with Dissolve(0.3)
        scene 109_s8 with vpunch
        mc "Ahhngg!"
        lena "Holy shit!"

    else:
        scene 109_s7 with Fade(0.5,0.5,1.0)
        mc "Hahh! Ahhn! Fuck, the road ahead is closed!"
        play sound "sound_effects/woosh2.mp3"
        scene 109_s9 with Dissolve(0.3)
        scene 109_s9 with vpunch
        mc "Ahhngg!"
    
    play sound "sound_effects/bodydrop4.mp3"
    scene 109_s10 with Fade(0.5,0.5,1.0)
    mc "Hahhh... ahh... (D-Diana was right! She's actually here... Avery and... Reiner?!)"
    impulse "It's now or never, brother. This is your chance. Catch them off guard and kill them with your bare fists."
    scene 109_s27 with Dissolve(1.0)
    mc "(If I deal with them now... it's over. I can end this today.)"
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
        
    call screen scene109_choice01 with dissolve

label scene109_choice01_op1:
    $ mc_minthra_talk1 = True
    scene 109_s35 with Dissolve(1.0)
    minthra "Halt this madness at once!"
    minthra "Cast aside these foolish thoughts, vessel!"
    minthra "My weakened power grants you strength and endurance far beyond mortal limits... but even I cannot protect you from a hundred arrows piercing your body at once."
    mc "(I know.)"
    minthra "Then why do you still want to step forward? This is not courage. This is suicide."
    empathy "Despite her words, a heavy silence follows. For the first time, Minthra sounds almost... frustrated."
    mc "(...Fine. I won't do it.)"
    jump scene109_choice01_op2

label scene109_choice01_op1_2:
    $ renpy.notify("Check failed!")
    mc "(I-I can't! I'm to scared to die...)"
    logic "Being afraid of death's cold grip isn't something to be ashamed of."
    jump scene109_choice01_op2

label scene109_choice01_op2:
    stop music fadeout 1.0 
    scene 109_s10 with Dissolve(1.0)
    mc "..."
    play music "ambiance/waltz_of_melancholy.mp3" fadein 3.0 loop
    scene 109_s11 with Dissolve(2.0)
    reiner "...the princess's execution will draw them out. Every loyalist, every sympathizer—they'll show themselves like moths to flame."
    reiner "We'll crush them. All of them. One public execution, and the old guard dies with her."
    scene 109_s13 with Dissolve(1.0)
    mc "(She's really going through with it.)"
    reiner "Once the loyalists are eliminated, the city is ours. No more pretending. No more games."
    scene 109_s12 with dissolve
    avery "Ours?"
    scene 109_s17 with Dissolve(1.0)
    reiner "Why of course, my dear. I helped you throughout all of this, didn't I? Where would you be without my counsel? My resources? My... patience?"
    reiner "Don't worry. It's only temporary, the title of queen will still be yours. You'll handle all the... menial tasks that come with it. Ceremonies, audiences and whatnot."
    reiner "But when it comes to matters of consequence... you always consult me first."
    scene 109_s14 with dissolve
    avery "What is the point of any of this if I'm not the one truly in charge?"
    scene 109_s15 with dissolve
    reiner "Because you're unfit to lead yet. You're reckless, emotional and far too young."
    scene 109_s18 with vpunch
    avery "What did you say?!"
    scene 109_s19 with dissolve
    reiner "Our conversations over the past months have made that abundantly clear."
    scene 109_s18 with dissolve
    avery "You think I did all this... for you?"
    scene 109_s15 with Dissolve(1.0)
    reiner "No. You did it because you were angry. Angry at your sister. She overshadowed you afterall."
    scene 109_s16 with dissolve
    avery "...You used me."
    scene 109_s15 with dissolve
    reiner "*scoff* {i}Used you?{/i} You were the one who approached me, dear. If anything, you should have seen this coming. Ah, wait. You're not as smart as her. Never were."
    scene 109_s19 with Dissolve(1.0)
    avery "..."
    reiner "The only question now is whether you'll accept reality gracefully or make this unpleasant for both of us."
    scene 109_s20 with Dissolve(1.0)
    avery "Hnng... Is the princess really necessary for this?"
    scene 109_s21 with dissolve
    reiner "Hmm?"
    scene 109_s20 with dissolve
    avery "Can't we find a lookalike? Someone to parade in chains? No one's seen her up close in a long time."
    avery "She doesn't need to die. She's innocent in all of this."
    scene 109_s21 with dissolve
    reiner "Having second thoughts? How disappointing."
    scene 109_s20 with dissolve
    avery "She's my—"
    scene 109_s23 with Dissolve(1.0)
    reiner "She's a threat and can turn the people against us. The Queen's lineage must perish completely. Every drop of that bloodline that isn't ours needs to be erased."
    scene 109_s22 with dissolve
    avery "Did you forget that I'm also in that lineage?"
    scene 109_s23 with dissolve
    reiner "You're... special. You've proven useful... Loyal. I only need one of your sister's lineage to assume control. One figurehead."
    reiner "That's you, dear. Be grateful."
    scene 109_s22 with dissolve
    avery "But—"
    scene 109_s24 with Dissolve(1.5)
    reiner "Do as you're told, {i}Queen.{/i} You can't turn back time now. The wheels are in motion. They've been in motion since the moment you first came to me."
    avery "..."
    reiner "Understood?"
    scene 109_s25 with dissolve
    avery "...Yes."
    scene 109_s24 with dissolve
    reiner "Good. You should rest. You look... tired."
    scene 109_s26 with Dissolve(1.0)
    perception "Reiner strides out of the courtyard, his guards falling into step behind him. The door closes behind him quietly."
    scene 109_s27 with dissolve
    mc "(Huh? What is she—)"
    scene 109_s28 with dissolve
    avery "AHHHHH!"
    scene 109_s29 with Dissolve(0.3)
    play sound "sound_effects/punch.mp3"
    scene 109_s29 with vpunch
    avery "AHNGG!"
    scene 109_s30 with dissolve
    avery "...Owww! Fuck!"
    scene 109_s31 with Dissolve(1.5)
    avery "Unfit? {i}Unfit{/i}?! I'll show you who's unfit. I'll show {i}all{/i} of you."

    if mc_want_help_serena:
        guard "Your Majesty!"
        scene 109_s33 with vpunch
        avery "WHAT!?"
        scene 109_s32 with dissolve
        guard "I-It's urgent. Mr. Gheris's manor—it's under attack!"
        scene 109_s33 with dissolve
        avery "Under attack? By whom?"
        scene 109_s32 with dissolve
        guard "We're... we're not certain of the full situation yet, Your Majesty. But initial reports suggest... a single woman."
        scene 109_s33 with dissolve
        avery "A single woman."
        scene 109_s32 with dissolve
        guard "Yes, Your Majesty."
        scene 109_s33 with vpunch
        avery "By the hells, then dispose of her! Are you telling me my guards can't handle {i}one woman{/i}?!"
        scene 109_s32 with dissolve
        guard "W-We're trying, Your Majesty! She's... she's unlike anything we've—"
        scene 109_s33 with dissolve
        avery "Can this day get any worse?!"
        scene 109_s32 with dissolve
        guard "I... I don't think so, Your Majesty?"
        scene 109_s33 with vpunch
        avery "That wasn't a question! Find her. Kill her. And if you fail, don't bother coming back!"
        scene 109_s32 with dissolve
    else:
        guard "Your Majesty?"
        scene 109_s33 with vpunch
        avery "WHAT?!"
        scene 109_s32 with dissolve
        guard "W-We need to escort you back to the castle."

    scene 109_s34 with Dissolve(1.5)
    stop music fadeout 4.0 
    mc "..."
    jump scene110

label scene110:
    if mc_tried_help_alex:
        $ mc_save_queen = True

    if mc_save_queen:
        scene 110_s1 with Fade(2.0,1.0,1.5)
        play music "ocean2.mp3" fadein 1.0 loop
        ""
        scene 110_s2 with Dissolve(1.5)
        q "Anything biting?"
        scene 110_s3 with dissolve
        whitlaw "*snore* ...Wh?"
        scene 110_s5 with Dissolve(1.0)
        whitlaw "Your Grace. I was just resting my eyes."
        scene 110_s4 with dissolve
        q "*chuckles* Here I thought you were finally putting food in our bellies."
        scene 110_s5 with dissolve
        whitlaw "The sea has been unkind to me, my queen. Forgive me."
        scene 110_s4 with dissolve
        q "No need for honorifics, old friend. I am queen of nothing right now. *chuckles* I don't even have a fish to my name."
        scene 110_s6 with Dissolve(1.0)
        whitlaw "You will always be my queen. Hollow titles or not."
        whitlaw "I followed your father into battle. I'll not stop using the word just because the world's gone crooked."
        scene 110_s7 with Dissolve(1.0)
        
        if mc_princess_alex:
            q "I feel things getting better soon."
            scene 110_s8 with dissolve
            whitlaw "The fish still aren't biting."
            scene 110_s7 with dissolve
            q "The fish can wait. For the first time in so long, I feel like the tide might actually be turning."
            q "Perhaps I can join you. It's been a while since I picked up a rod."
        else:
            q "*sigh* Something's wrong. I can't put my finger on it, but... it's there."
            scene 110_s8 with dissolve
            whitlaw "A premonition?"
            scene 110_s7 with dissolve
            q "Something more. I can sense when I'm about to make good or bad decisions, it's a magic I learned long ago. It's subtle, but it helps me from time to time."
            q "Perhaps it's time for me to make a move sooner than I expected."
        scene 110_s1 with Dissolve(2.0)
        stop music fadeout 2.0 
        ""
        scene 111_s1 with Fade(1.3,1.0,1.5)
        jump scene111
    else:
        scene 111_s1 with Fade(1.3,1.0,1.5)
        jump scene111

label scene111:
    if mc_want_help_serena:
        play sound "sound_effects/body/landing.mp3"
        scene 111_s1 with vpunch
        mc "Hmph."
        scene 111_s2 with Dissolve(1.2)
        lena "How did you—? No, I saw you. One jump... You cleared the roof in one jump!"
        scene 111_s3 with dissolve
        mc "Fuck. My legs are numb... Anyway. How do we start?"
        scene 111_s2 with dissolve
        lena "Hold on. You're just going to move past that?"
        scene 111_s3 with dissolve
        play music "tense/lie.mp3" fadein 1.0 loop
        mc "Look, the quee—Avery was here. I wanted to check on an old friend."
        scene 111_s5 with Dissolve(1.0)
        lena "Avery?! What's that bitch doing here?"
        scene 111_s4 with dissolve
        mc "To put it bluntly... They're planning to execute the princess and I'm going to put a stop to it."
        lena "..."
        scene 111_s5 with dissolve
        lena "You're not kidding, are you? Oh, fuck me..."
        scene 111_s4 with dissolve
        mc "I need all the help I can get, Lena. It's part of the reason I'm helping you, so you can help me in return."
        scene 111_s6 with Dissolve(1.0)
        lena "I just got back to Serena. It's only been three days ago since I finally held her again..."
        lena "And now you're standing here asking me to stage a rescue that's going to bring every guard in the city down on our heads?"
        scene 111_s7 with dissolve
        if mc_princess_reham:
            mc "I don't plan to rescue the princess here. I'm doing it by asking the king of Nahraya."
        else:
            mc "You don't have to physically be there. I just need help with something. Anything."
        lena "..."
        scene 111_s8 with Dissolve(1.0)
        lena "How about a carriage? You got one wherever you're hiding?"
        if mc_princess_reham:
            lena "You'll need one if you're travelling with a group."
            scene 111_s9 with dissolve
            mc "I don't. A carriage or wagon would be perfect for all of us."
        else:
            lena "I don't assume you'll be sticking around after {i}that{/i}."
            scene 111_s9 with dissolve
            mc "I'm not. A carriage or wagon would be perfect for all of us. Including the princess."
        scene 111_s8 with dissolve
        lena "Then you can count on me. I'll get you one with supplies after I take Serena to sisters of fate temple a little off from the city."
        lena "The sisters there owe me a favor; they'll keep her safe until the heat dies down."
        scene 111_s9 with dissolve
        mc "Thank you. So how do we approach? The garden wall?"
        scene 111_s8 with dissolve
        lena "Exactly. Quiet and clean. We reach his office, force him to burn the deeds—or kill him. Either way works for me."
        scene 111_s9 with dissolve
        mc "I'll follow you."
        scene 111_s8 with dissolve
        lena "Come on. We're basically there already."
        scene 111_s9 with dissolve
        stop music fadeout 1.0 
        jump scene111_2

    else:
        play sound "sound_effects/body/landing.mp3"
        scene 111_s1 with vpunch
        mc "Hmph."
        scene 111_s10 with Dissolve(1.3)
        mc "*sigh* (This is getting to be too much for me.)"
        scene 111_s11 with dissolve
        jenny2 "Help! Please, where have those fucking guards gone?!"
        scene 111_s12 with Dissolve(1.0)
        mc "(Hmm? Is that... Jenna?)"
        scene 111_s13 with vpunch
        jenny2 "You!"
        play music "tense/lie.mp3" fadein 1.0 loop
        mc "(Shit. She saw me.)"
        scene 111_s14 with Dissolve(1.0)
        jenny2 "You look capable enough. P-Please! I can't find anyone—you have to help me!"
        scene 111_s15 with dissolve
        mc "*ahem* Easy. Take a breath. Tell me what's happened first." 
        scene 111_s14 with dissolve
        jenny2 "My father's manor is under attack! Right now! T-This woman, she's killing our personal guards!"
        jenny2 "Please, I'll give you anything. He's wealthy, you'll be swimming in coin, I swear it!"
        scene 111_s15 with dissolve
        mc "...Did you try telling the guards?"
        scene 111_s14 with dissolve
        jenny2 "What does it look like I'm doing, moron?! They've all vanished! Every last one of them!"
        scene 111_s15 with dissolve
        mc "(I guess they're all with Avery now.)"
        scene 111_s16 with dissolve
        jenny2 "Wait a moment... I know you."
        scene 111_s17 with dissolve
        mc "S-Sorry?"
        scene 111_s16 with dissolve
        jenny2 "Don't. You were a judge during the Guild evaluation. I never forget a face. You escaped after you killed Able and blew up the market."
        scene 111_s17 with dissolve
        mc "You're confusing me with someone else."
        scene 111_s16 with dissolve
        jenny2 "Don't play dumb, [mc]. You're a wanted man, and yet here you are, strolling the city like nothing's wrong."
        jenny2 "Fucking guards can't do anything right lately."
        if mc_accept_jenny:
            jenny2 "Look, my father managed to make a deal with the Guild after you let me join. We have connections now."
            jenny2 "You'll have more coin than you'll know what to do with, enough to leave this city, start over anywhere! Just... please. Help us."
        else:
            jenny2 "My father's rich. Stupidly rich. Help me and he'll reward you."
        scene 111_s17 with dissolve
        mc "..."
        scene 111_s16 with dissolve
        jenny2 "*sigh* Not good enough? Well, I won't call the guards on you if you come and help me. Now."
        scene 111_s17 with dissolve
        mc "Jenna, pleas—"
        scene 111_s18 with vpunch
        jenny "It's JENNY! J, e, n, n, y."
        jenny "This is the second time you said my name wrong."
        scene 111_s19 with dissolve
        mc "Sorry. I flubbed it."
        scene 111_s18 with dissolve
        jenny "No way, that was on purpose!"
        scene 111_s19 with dissolve
        call screen scene111_choice01 with dissolve

label scene111_choice01_op1:
    mc "Fine. Show me the way."
    mc "(I have to do this before Avery's guards show up.)"
    scene 111_s16 with dissolve
    jenny "Quickly, follow me."
    scene 111_s17 with dissolve
    stop music fadeout 1.0 
    jump scene111_2

label scene111_choice01_op2:
    mc "I'm not helping you. Go find someone else, Jenny."
    scene 111_s18 with dissolve
    jenny "Oh, sorry. Did you not hear what I said?"
    jenny "You don't have a choice here. Either you help, or I turn you in."
    scene 111_s19 with dissolve
    mc "You—"
    scene 111_s20 with Dissolve(1.0)
    jenny "Help! Help! The fugitive is over here!"
    scene 111_s21 with vpunch
    mc "Shut up! ...Fine. I'll do it."
    mc "*sigh* Lead the way."
    stop music fadeout 1.0 
    jump scene111_2

label scene111_2:
    if mc_want_help_serena:
        scene 111_s22 with Fade(1.5,1.0,1.3)
        play music "nature.mp3" fadein 1.0 loop
        lena "Over there."
        lena "Strange... Usually there's lots of guards circling the place. Gheris doesn't sleep easy without men at his door."
        mc "We're in luck. The attention is all on Avery right now. But we have to be quick. That luck won't hold."
        scene 111_s23 with Dissolve(1.3)
        lena "Right. See that window? That's his office. Gheris is a creature of habit—he'll be at his ledgers this time of day."
        scene 111_s25 with Dissolve(1.0)
        lena "You know how to climb? Or better yet, can you do what you did back then?"
        scene 111_s24 with dissolve
        mc "Ughn... my poor legs. I'll try."
        mc "Umm... how should I carry you?"
        scene 111_s25 with dissolve
        lena "Aww~ Don't be shy, boy. I'm like your mother."
        scene 111_s24 with dissolve
        mc "I'd rather not think of it like that."
        scene 111_s26 with Fade(1.0,0.5,0.7)
        lena "*chuckles* You're pretty strong. No wonder my daughter is head over heels for you."
        lena "Just don't overshoot us into the manor next door. One Gheris is enough for me."
        play sound "sound_effects/woosh2.mp3"
        scene 111_s27 with Dissolve(0.5)
        scene 111_s27 with vpunch
        mc "HNNNGG!"
        lena "Wooohh! This is insane!"
        scene 111_s28 with dissolve
        lena "Uhh... [mc]?!"
        scene 111_s29 with Dissolve(1.2)
        mc "Shit! Shit! Shit!"
        play sound "sound_effects/glass_shatter.mp3"
        scene 111_s30 with Dissolve(0.3)
        stop music
        scene 111_s30 with vpunch
        perception "You smash through the window in a shower of glass. You tumble on top of each other, sending paper everywhere. Lena lands in a tangled heap directly on top of a very startled, very soft man in silk clothing."
        scene 111_s31 with Dissolve(1.0)
        lena "Oww..."
        mc "You good?"
        lena "I'm fine. He broke my fall."
        scene 111_s32 with Dissolve(1.0)
        gheris "What the—!?"
        gheris "Who the hell are you two!? Guards! GUARDS!"
        play music "tense/foreboding.mp3" fadein 2.0 loop
        scene 111_s33 with vpunch
        perception "Lena moves fast. She unsheathes her sword, pressing it flat against his throat. The scream dies in his windpipe."
        scene 111_s34 with dissolve
        lena "Shut your mouth, you pig. You should be grateful my blade isn't slitting your throat this instant."
        lena "Now. I'm going to ask you this once."
        scene 111_s33 with dissolve
        gheris "Wh-What do you want?! Coin? I have coin—"
        scene 111_s34 with dissolve
        lena "The deeds to your slaves. Where are they?"
        scene 111_s33 with dissolve
        gheris "Th-The drawer! Top drawer of the desk! You want them? Take them! Please, please don't hurt me—"
        scene 111_s35 with dissolve
        mc "Avylin... Eida... Ruby..."
        mc "(Wait, Ruby is here? Is this the noble she angered?)"
        scene 111_s36 with dissolve
        mc "Serena! I found it."
        mc "Should I rip it up?"
        scene 111_s37 with Dissolve(1.0)
        lena "No. I want him to do it. Get up."
        lena "You're going to revoke your ownership of that girl. Right now. In writing."
        scene 111_s38 with dissolve
        gheris "C-Certainly. Of course. You could have simply asked..."
        scene 111_s37 with dissolve
        lena "*scoff* Sure."
        scene 111_s39 with Fade(0.5,0.5,0.5)
        perception "Gheris writes his signature with trembling hands, then presses his ring into the wax."
        scene 111_s40 with Dissolve(1.0)
        gheris "There. She is mine no longer."
        scene 111_s41 with dissolve
        lena "All those unpaid wages, give it to the man."
        scene 111_s40 with dissolve
        gheris "Yes, of course. He can take it."
        gheris "A-Anything else... ma'am? And dear sir?"
        scene 111_s90 with dissolve
        $ renpy.notify("You received 2000 coins!")
        play sound "sound_effects/coin_collect.mp3"
        $ mc_coin += 2000
        call screen scene111_choice02 with dissolve

    else:
        jump scene111_4

label scene111_choice02_op1:
    $ mc_freed_ruby = True
    scene 111_s42 with Dissolve(1.0)
    mc "Not just her. All of them. Every name in those papers. Revoke them now."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 111_s43 with dissolve
    gheris "But that's my entire work force! Do you have any idea what they're worth?!"
    scene 111_s42 with dissolve
    mc "Less than your life, I'd wager. Write."
    scene 111_s43 with dissolve
    jump scene111_3

label scene111_choice02_op2:
    $ mc_wants_more_coin_gheris = True
    scene 111_s42 with Dissolve(1.0)
    mc "That's all you have? I don't believe it."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    mc "I want more."
    scene 111_s43 with dissolve
    gheris "There's a pouch filled with coin behind the couch over there. That's all I have that isn't in the bank, I swear."
    $ renpy.notify("You found 500 coins!")
    play sound "sound_effects/coin_collect.mp3"
    $ mc_coin += 500
    jump scene111_3

label scene111_choice02_op3:
    scene 111_s42 with Dissolve(1.0)
    mc "That's good enough."
    mc "We have what we came for, Lena. Let's not give the guards a reason to find this place before we're gone."
    scene 111_s43 with dissolve
    jump scene111_3

label scene111_3:
    scene 111_s44 with Dissolve(1.0)
    lena "I have no use for you now. Time to meet your Gods, human."
    hide screen stat_change with easeoutright
    $ karma_less = False
    $ karma_more = False
    scene 111_s45 with dissolve
    gheris "W-Wait, what?! But I did what you asked! The deed is revoked—you saw me sign it!"
    scene 111_s44 with dissolve
    lena "You did. And I'm grateful for that. Truly..."
    lena "But I'm still not satisfied. I need to make sure you don't refute the documents the moment I turn them in. A dead man can't contest a claim."
    scene 111_s45 with dissolve
    gheris "Please! I don't even own them yet! They're slaves in name only!"
    scene 111_s44 with dissolve
    lena "What are you on about?"
    scene 111_s45 with dissolve
    gheris "I haven't turned the papers of ownership yet! I swear!"
    scene 111_s89 with dissolve
    mc "Think this through, Lena. We can just leave."
    scene 111_s45 with dissolve
    if mc_freed_ruby:
        gheris "Let me go and I promise I'll let that girl go, all of them, every last one. You have my word."
    else:
        gheris "Let me go and I promise I'll let that girl go. You have my word."
    scene 111_s44 with dissolve
    lena "Heh. Your word. Well, that's all the more reason to kill you. No paperwork to clean up. Just one less noble breathing my air."
    scene 111_s45 with dissolve
    gheris "Wait—!"
    play sound "sound_effects/doors/door_kick.mp3"
    scene 111_s46 with vpunch
    jenny "What with all this noise, daddy?! I'm trying to—"
    scene 111_s47 with dissolve
    jenny "Huh? What's happening here?"
    lena "What are you standing for?! Get her!"
    scene 111_s48 with dissolve
    mc "Stop. Stay right where you are. Don't make this worse."
    mc "Go sit next to your father."
    scene 111_s49 with Dissolve(1.6)
    jenny "Daddy, what's happening?! I'm scared!"
    scene 111_s50 with dissolve
    gheris "Calm down, dear. It will be fine. Everything will be fine. Just do as they say."
    scene 111_s51 with Dissolve(1.0)
    mc "Dammit! We could have been gone, Lena. We were done!"
    mc "Why didn't you mention that he had a daughter?!"
    scene 111_s52 with dissolve
    lena "It's fine. What's one more? You're all the same to me. Daughter, father... you bleed the same color."
    scene 111_s53 with dissolve
    gheris "Don't hurt her! Please! It's me you want, isn't it?! I'm the one who wronged you. She has nothing to do with this!"
    scene 111_s52 with dissolve
    lena "Don't blame me, Gheris. This is all your doing. You built this house on the backs of people who hated you. Now it falls on everyone inside it."
    scene 111_s54 with Dissolve(1.0)
    jenny "You! I know you!"
    jenny "[mc]!"
    jenny "I don't know what's going on, or why you're here, but I can help you! My father has money, lots of it! I'll give you coin, more than you've ever seen!"

    if mc_accept_jenny:
        jenny "My father managed to make a deal with the Guild after you let me join. We have connections now."
        jenny "You'll have more coin than you'll know what to do with—enough to leave this city, start over anywhere! Just... please. Help us."
    else:
        jenny "My father's rich. Stupidly rich. Get rid of her and he'll reward you! I swear it!"
        jenny "We'll forget everything here. You walk away a wealthy man and dissapear wherever you want!"

    scene 111_s56 with Dissolve(1.5)
    lena "*laughs* The nerve you have, girl. [mc] is here to help {i}me{/i}. We have an understanding. Now... where were we?"
    perception "Cold air flows through the broken window. Jenny sobs once, stifling it. Gheris squeezes his eyes shut. Lena's hand is steady."
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene111_choice03 with dissolve

label scene111_choice03_op2:
    $ mc_convince_lena = True
    $ mc_helped_lena = True
    scene 111_s57 with Dissolve(1.0)
    mc "Lena. Put the sword down."
    scene 111_s58 with dissolve
    lena "Don't."
    scene 111_s57 with dissolve
    mc "We got what we came for. This isn't justice anymore—it's slaughter."
    mc "I can't let you do this. Not with the girl here."
    scene 111_s58 with dissolve
    lena "You think I care about the girl? She's just another noble brat. Given time, she'll grow up to be exactly like him."
    scene 111_s57 with dissolve
    mc "Maybe. But we're not them."
    mc "You're a mother, Lena. Look at her. She's terrified. She's exactly what Serena was when I met you—caught in a nightmare she didn't make."
    scene 111_s58 with dissolve
    lena "Don't you dare use my daughter against me."
    scene 111_s57 with dissolve
    mc "You risked everything to get Serena back. You didn't do it by becoming the monsters you hate, you did it because you're better than them."
    stop music fadeout 3.0 
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 111_s59 with Dissolve(1.0)
    empathy "Lena stares at Jenny, who meets her eyes with raw terror. Slowly, as if the weight of her own arm becomes unbearable, Lena lowers the blade."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 111_s60 with Dissolve(1.0)
    play music "sad/case_file.mp3" fadein 3.0 loop
    lena "If you ever try to claim her, or send anyone after us... I will come back. And I won't stop to talk."
    scene 111_s61 with dissolve
    gheris "You have my word."
    scene 111_s60 with dissolve
    mc "Let's go. The window. Now."
    scene 111_s62 with Dissolve(1.5)
    lena "..."
    jenny "Thank you, [mc]."
    scene black with Dissolve(1.0)
    jump scene113

default mc_killed_lena_counted = False

label scene111_choice03_op1:
    $ mc_helped_jenny = True
    $ mc_betray_lena = True
    $ mc_killed_lena = True
    $ mc_killed_lena_counted = True

    if mc_karma > 1:
        $ mc_karma -= 4
    if mc_karma <= 0:
        $ mc_karma = 1

    scene 111_s63 with Dissolve(1.0)
    mc "...How much coin are we talking, Jenny?"
    scene 111_s64 with dissolve
    lena "What?! [mc]! You can't be serious!"
    jenny "Twenty gold coins! No, thirty!"
    scene 111_s65 with dissolve
    lena "You'd sell me out? For coin?"
    lena "After everything we— After I trusted you?!"
    scene 111_s66 with dissolve
    mc "I'm sorry, Lena. I have my own war to fight. I need resources, and I'm out of options."
    scene 111_s65 with dissolve
    lena "Then you're out of allies, too."
    scene 111_s69 with dissolve
    perception "She moves without hesitation, just the flash of steel and the sound of displaced air."
    scene 111_s70 with Dissolve(0.3)
    play sound "sound_effects/sword/sword_swing1.mp3"
    scene 111_s70 with vpunch
    perception "Instinct takes over. You twist, the edge slicing air instead of flesh. She fights with the fury of a woman who's lost everything twice."
    scene 111_s71 with dissolve
    perception "She overextends. In less than a second, you catche her wrist."
    lena "GHNN! LET GO!"
    mc "(I'm sorry.)"
    play sound "sound_effects/stab01.mp3"
    scene 111_s72 with vpunch
    lena "Gahn!"
    perception "You twist her hand and drives the blade into her body. A choked gasp escapes her lips. She looks down at the blood blooming across her chest. The fury drains from her face, replaced by surprise and sorrow."
    scene 111_s73 with Dissolve(1.5)
    play sound "sound_effects/bodydrop.mp3"
    lena "Serena..."
    gheris "I-I'll get the gold. Just... please. Don't hurt us."
    mc "..."
    stop music fadeout 1.0 
    scene 111_s81 with Fade(1.0,1.0,1.0)
    jump scene111_5

label scene111_choice03_op3:
    $ mc_helped_lena = True
    $ mc_let_jenny_die = True
    mc "...Do what you have to do. I won't stop you."
    scene 111_s74 with Dissolve(1.0)
    lena "This is for Serena. For all of the people you wronged."
    scene 111_s64 with Dissolve(1.0)
    play sound "sound_effects/sword/stab6.mp3"
    perception "Lena's swings her blade. The sound is wet and brief, swallowed by Jenny's scream. Then the scream cuts short, too, collapsing into a gasp."
    lena "It's done."
    lena "Let's go."
    stop music fadeout 1.0 
    jump scene113

label scene111_4:
    scene 111_s75 with Fade(1.4,1.0,1.3)
    jenny "Here we are! On the third floor!"
    scene 111_s76 with Fade(1.0,1.0,1.0)
    jenny "In this room!"
    mc "Stay outside. I'll take care of it."
    scene 111_s77 with Dissolve(1.0)
    play music "tense/foreboding.mp3" fadein 1.0 loop
    gheris "H-Help! Please, someone!"
    scene 111_s78 with dissolve
    lena "No one's left, pig. They've all fled or fallen. It's time you met them too."
    scene 111_s67 with dissolve
    mc "Stop!"
    scene 111_s68 with dissolve
    lena "Another one? Fine. Come here. I'll make it quick."
    lena "Ah... [mc]."
    scene 111_s65 with dissolve
    lena "So you don't have time to help me—a woman trying to free her daughter from slavery, but you have time to help a {i}noble{/i}?"
    lena "Looks like I was completely wrong about you. And so was my daughter."
    scene 111_s66 with dissolve
    mc "We can still talk about this, Lena. It doesn't have to go this way."
    scene 111_s65 with dissolve
    lena "Talk? You want to talk?"
    lena "I'm not doing shit until this fucker dies. He doesn't get to walk away, not after what he did."
    scene 111_s66 with dissolve
    gheris "I swear to let that girl go free, you have my word!"
    scene 111_s65 with dissolve
    lena "That's not enough."
    scene 111_s66 with dissolve
    jenny "Do something! She's going to hurt him!"
    empathy "Your mind races. You can hear Jenny sobbing and screaming from behind the door."
    call screen scene111_choice04 with dissolve
    
label scene111_choice04_op1:
    $ mc_helped_jenny = True
    $ mc_convince_lena = True
    scene 111_s67 with Dissolve(1.0)
    mc "Lena. Put the blade down. This isn't justice anymore, it's slaughter."
    mc "I can't let you do this. Not with his daughter here crying and begging."
    scene 111_s68 with dissolve
    lena "You think I care about the girl? She's just another noble brat. Given time, she'll grow up to be exactly like him."
    scene 111_s67 with dissolve
    mc "Maybe. But we're not them."
    mc "You're a mother, Lena. His daughter is terrified. She's exactly what Serena was when I met you—caught in a nightmare she didn't make."
    scene 111_s68 with dissolve
    lena "Don't you dare use my daughter against me!"
    scene 111_s67 with dissolve
    mc "You risked everything to get Serena back. You didn't do it by becoming the monsters she hates. You did it because you're better than them."
    scene 111_s68 with dissolve
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    empathy "Lena stares at you for a while. Slowly, as if the weight of her own arm becomes unbearable, Lena lowers the blade."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 111_s78 with Dissolve(1.0)
    lena "If you ever try to claim her again, or send anyone after us... I will come back. And I won't stop until your head isn't attached to your neck. Do you understand me?"
    scene 111_s77 with dissolve
    gheris "Y-You have my word. I'll set her free, I swear it on my life."
    scene 111_s78 with dissolve
    mc "You have to leave. Now. Guards could be here any second."
    lena "..."
    stop music fadeout 1.0 
    scene 111_s81 with Fade(1.0,1.0,1.5)
    jump scene111_5

label scene111_choice04_op2:
    $ mc_killed_lena = True
    $ mc_helped_jenny = True
    scene 111_s67 with dissolve
    mc "You're out of control, Lena. I'm sorry."
    scene 111_s68 with dissolve
    lena "You wanna fight, you? A little cub?"
    lena "I've been cutting throats since before you were in your father's balls. But come. Try your luck."
    scene 111_s69 with Dissolve(1.0)
    jenny "Stop! I didn't want you to fight! You'll... you'll ruin the carpet with your blood!"
    perception "She moves without hesitation, just the flash of steel and the sound of displaced air."
    scene 111_s70 with Dissolve(0.3)
    play sound "sound_effects/sword/sword_swing1.mp3"
    scene 111_s70 with vpunch
    perception "Instinct takes over. You twist, the edge slicing air instead of flesh. She fights with the fury of a woman who's lost everything twice."
    scene 111_s71 with dissolve
    perception "She overextends. Just an inch. You catche her wrist, twist it and drives the blade into her body."
    lena "GHNN! LET GO!"
    mc "(I'm sorry.)"
    play sound "sound_effects/stab01.mp3"
    scene 111_s72 with vpunch
    lena "Gahn!"
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 2
    $ karma_less = True
    $ mc_killed_lena_counted = True
    show screen stat_change with easeinright
    perception "You twist her hand and drives the blade into her body. A choked gasp escapes her lips. She looks down at the blood blooming across her tunic. The fury drains from her face, replaced by surprise and sorrow."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 111_s73 with Dissolve(1.5)
    play sound "sound_effects/bodydrop.mp3"
    lena "Serena..."
    scene 111_s79 with Dissolve(1.0)
    jenny "Dammit... *sigh* I suppose there wasn't any other way."
    stop music fadeout 1.0 
    scene 111_s81 with Fade(1.0,1.0,1.0)
    jump scene111_5

label scene111_5:
    play music "nature.mp3" fadein 1.0 volume 0.5 loop
    jenny "Are you alright, daddy? Were you hurt?"
    gheris "*cough* I'm well, dear. Crazy woman almost killed me!"
    scene 111_s82 with Dissolve(1.0)
    gheris "Thank you for your help. My daughter has always had good instincts about people."
    scene 111_s83 with dissolve
    jenny "I was screaming in the street, but nobody came. The guards—they've all vanished. Every last one."
    jenny "I'm so glad to have come across you. I would be utterly devastated if something happened to my daddy."
    scene 111_s82 with dissolve
    gheris "Me too, little sparrow. Me too. A generous reward is most in order for this young man."
    scene 111_s86 with Dissolve(1.0)
    gheris "Here. This isn't nearly enough, but know that I am forever in your debt. If you ever need shelter, resources, a name to open doors... mine is yours."
    if not mc_helped_jenny:
        if mc_wants_more_coin_gheris:
            gheris "You can keep the wages coin and my secret pouch as well. It's better spent on you than those lazy bastards."
        else:
            gheris "You can keep the wages coin as well. It's better spent on you than those lazy bastards."
    else:
        gheris "I put in a little extra since my daughter managed to secure me a good deal at the guild."
    scene 111_s87 with dissolve
    if mc_accept_jenny:
        $ renpy.notify("You received 3000 coins!")
        play sound "sound_effects/coin_collect.mp3"
        $ mc_coin += 3000
    else:
        $ renpy.notify("You received 3500 coins!")
        play sound "sound_effects/coin_collect.mp3"
        $ mc_coin += 3500
    mc "I'm gonna need a carriage too."
    scene 111_s86 with dissolve
    gheris "A carriage? Of course. You'll have one. I'll also throw in some supplies too in case you're planning on a journey."
    scene 111_s87 with dissolve
    

    if mc_killed_lena:
        scene 111_s84 with Dissolve(1.0)
        jenny "*sniff* *sniff* We're going to need some cleaners...  *gag* Gods, the stench of blood will haunt me forever."
        jenny "I didn't know it would smell like that. Like iron and salt."
        scene 111_s85 with dissolve
        gheris "This is why I told you not to join the Guild, dear. You're soft. Too soft for the ugliness that is out there."
        scene 111_s84 with dissolve
        jenny "Right, right... I was there just to get you the deal anyway."
        scene 111_s83 with dissolve
        jenny "The... the guards could be here any second. Even incompetent, they'll show up eventually."
        jenny "Why don't you come to my room? We can hide there until they leave."
        scene 111_s91 with dissolve
        mc "Your room?"
        scene 111_s83 with dissolve
        jenny "Y-Yes. I'll... I'll give you a reward of my own. A proper one. Not just my father's coin."
        scene 111_s82 with dissolve
        gheris "No one will lay a hand on you as long as you're in my house, brave sir."
        scene 111_s91 with dissolve

    else:
        scene 111_s83 with dissolve
        jenny "The... the guards could be here any second. Even incompetent, they'll show up eventually."
        jenny "Why don't you come to my room? Just until they leave. It's the last place they'd search."
        scene 111_s91 with dissolve
        mc "Your room?"
        scene 111_s83 with dissolve
        jenny "Y-Yes. I'll... I'll give you a reward of my own. A proper one. Not just my father's coin."
        scene 111_s82 with dissolve
        gheris "No one will lay a hand on you as long as you're in my house, brave sir."
        scene 111_s91 with dissolve
    call screen scene111_choice05 with dissolve

label scene111_choice05_op1:
    $ mc_sex_jenny = True
    mc "...Lead the way."
    scene 111_s88 with Dissolve(1.4)
    perception "She gestures for you to follow, leaving Gheris alone with his scattered ledgers and his fragile, borrowed life."
    jump scene112

label scene111_choice05_op2:
    mc "I can't stay. There's somewhere I need to go. But... thank you for the offer. And for keeping my name off the guards' lips."
    scene 111_s83 with dissolve
    jenny "Of course. The mysterious stranger has places to be..."
    jenny "Try not to get yourself killed before I see you again. I... I really want to thank you properly sometime."
    scene 111_s91 with dissolve
    stop music fadeout 1.0
    jump scene113

image s112_bj1 = Movie(play="images/chapter5/scene112/s112_bj1.webm", loop=True)
image s112_bj2 = Movie(play="images/chapter5/scene112/s112_bj2.webm", loop=True)

image s112_vsex1 = Movie(play="images/chapter5/scene112/s112_vsex1.webm", loop=True)
image s112_vsex2 = Movie(play="images/chapter5/scene112/s112_vsex2.webm", loop=True)

image s112_asex1 = Movie(play="images/chapter5/scene112/s112_asex1.webm", loop=True)
image s112_asex2 = Movie(play="images/chapter5/scene112/s112_asex2.webm", loop=True)

label scene112:
    stop music fadeout 1.0 
    scene 112_s1 with Fade(1.0,1.0,1.0)
    perception "You enter her room. It's incredibly neat, polished furniture, various makeup products arranged on the vanity, and several luxurious dresses sticking out of her closet."
    scene 112_s2 with Dissolve(1.0)
    jenny "Welcome~ Very few people ever get the honor of entering my room."
    scene 112_s3 with Dissolve(1.0)
    mc "It's nice. So... are you hiding me in the closet or under the bed?"
    scene 112_s4 with dissolve
    jenny "Hiding? Gods, you're dense."
    jenny "There's no need for any of that. My father will deal with anyone who comes invistigating. As for us..."
    jenny "We're going to have a little fun. Consider it a much better reward than mere coin."
    scene 112_s3 with dissolve
    mc "I see..."
    scene 112_s5 with Dissolve(1.0)
    if mc_accept_jenny:
        jenny "I still remember the taste of your cock from that day at the guild... You came so much in my mouth I didn't even need dinner afterwards."
        scene 112_s6 with dissolve
        mc "*chuckles* You still didn't get enough?"
        scene 112_s5 with dissolve
        jenny "Not even close. I've been thinking about it for so long... how it would feel if you put something so big somewhere else."
    else:
        jenny "You actually rejected my offer back at the guild... No one has ever done that to me before."
        jenny "It made me so frustrated. I spent days thinking about you... imagining what a bold, assertive man like you would do to a girl like me."
    scene 112_s6 with Dissolve(1.0)
    mc "Jenny, are you sure about this? What if someone comes knocking?"
    scene 112_s4 with dissolve
    jenny "Then I'll simply shoo them away. It's {i}my{/i} room."
    scene 112_s3 with dissolve
    mc "..."
    scene 112_s4 with dissolve
    jenny "Ugh, stop acting like girls ask you to fuck them all the time."
    jenny "I want you to take me... Just for a little while. I've been such an impatient girl~"
    scene 112_s3 with dissolve
    call screen scene111_choice06 with dissolve

label scene111_choice06_op1:
    mc "I'll make sure you have enough of me for a while."
    scene 112_s4 with dissolve
    jenny "Finally, some good sense."
    scene 112_s3 with dissolve
    jump scene112_2

label scene112_2:
    scene 112_s9 with Fade(0.5,0.5,0.5)
    jenny "Mmmm~"
    scene 112_s10 with Dissolve(2.5)
    jenny "Aren't I the prettiest girl you've ever seen?"
    scene 112_s11 with dissolve
    call screen scene112_choice01 with dissolve

label scene112_choice01_op1:
    mc "You are."
    mc "You're the most beautiful girl I've ever laid eyes on."
    scene 112_s10 with dissolve
    jenny "I know~"
    jenny "My face could make kings kneel and poets cry. Wars would be waged for this body."
    jenny "But... it's nice to hear you say it~"
    scene 112_s11 with dissolve
    jump scene112_3

label scene112_choice01_op2:
    mc "You're very pretty... but I've seen prettier."
    scene 112_s13 with dissolve
    jenny "Who?!"
    scene 112_s14 with dissolve
    mc "I can think of a few girls."
    scene 112_s13 with dissolve
    jenny "A few?! More than {i}one{/i} girl?"
    jenny "Hmph. Daddy always tells me I'm the prettiest in Irda. Maybe you just need... convincing~"
    scene 112_s14 with dissolve
    jump scene112_3

label scene112_choice01_op3:
    $ mc_jenny_hate = True
    mc "Not even close."
    scene 112_s13 with dissolve
    jenny "Execuse me!?"
    jenny "I am a noble lady! You should be on your knees thanking me for even looking at me!"
    scene 112_s14 with dissolve
    mc "I'm just telling the truth. And that spoiled attitude needs fixing."
    mc "Now, get on your knees and suck me dry."
    jenny "..."
    scene 112_s13 with dissolve
    if mc_accept_jenny:
        jenny "You're lucky that I'm too horny and your dick is the biggest I've seen, asshole..."
    else:
        jenny "You're lucky that I'm too horny to get angry, asshole..."
    scene 112_s14 with dissolve
    jump scene112_3

default scene112_sex_pov = False
default scene112_sex_bj = True
default scene112_sex_sex = False
default scene112_sex_v = True
default scene112_sex_a = False

default scene112_switch_bj_v = False
default scene112_switch_bj_a = False

default scene112_switch_bj_v_first = True
default scene112_switch_bj_a_first = True
default scene112_switch_bj_v_second = False
default scene112_switch_bj_a_second = False

label scene112_3:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_2_replay:
        $ persistent.chapter5_p7_2_replay = True
    scene 112_s15 with Dissolve(2.0)
    perception "Jenny squats down gracefully. She eagerly pulls your pants down."
    jenny "Hahhnn~ Finally... I've been fantasizing about this for so long."
    scene 112_s16 with Dissolve(1.0)
    play sound "se_sfx/lick/lick1.mp3" 
    sensation "She leans in and slowly drags her tongue along your shaft."
    jenny "Mmm... Much bigger than I imagined. How greedy of you to keep this from me for so long."
    scene 112_s17 with Dissolve(1.0)
    play sound "se_sfx/blowjob/blowjob5.mp3" 
    sensation "Her soft lips wrap around your tip as she begins bobbing her head, clearly enjoying herself."
    mc "Aghnn..."
    scene 112_s18 with Dissolve(1.0)
    play sound "se_sfx/blowjob/facial2.mp3" 
    jenny "*slurp* You should feel honored. A noble lady like me is on her knees for you."
    jenny "Don't finish in my mouth. I still want you inside me~"
    if mc_accept_jenny:
        jenny "Go ahead. Don't go easy on me like last time."
        jenny "This time, I want you to fuck my mouth hole like you mean it~"
    else:
        jenny "Go ahead. Don't go easy on me."
        jenny "I want you to fuck my mouth hole like it's my pussy~"
    scene 112_s19 with dissolve
    mc "Are you sure? This might be uncomfortable."
    scene 112_s18 with dissolve
    jenny "Oh, I'm sure~ I can tak—"
    show s112_bj1 with dissolve
    jenny "GUHK! *gag* *cough* I-I didn't mean this rough!"
    $ scene112_sex_bj = True
    call screen scene112_sex with dissolve

label scene112_sex_pov:
    scene black with Dissolve(0.3)
    if scene112_sex_bj:
        $ scene112_sex_bj = True
        $ scene112_sex_sex = False
        $ scene112_sex_v = False
        $ scene112_sex_a = False
        if scene112_sex_pov:
            $ scene112_sex_pov = False
            show s112_bj1 with dissolve
            jenny "Gluk~! Gugh! W-Why do I feel like cumming just from my throat being abused~?"
            mc "You're a natural at this!"
            jenny "*slurp* *gag* You're using my mouth like a whore's!"
        else:
            show s112_bj2 with dissolve
            $ scene112_sex_pov = True
            perception "Looking down, you see the spoiled noble daughter eagerly sucking you off. Her eyes occasionally glance up at you with a mix of lust and arrogance."
            jenny "*lick* *gag* How is it? Is the daughter of a high noble sucking your cock to your satisfaction?"
            mc "Mhnngh... It feels incredible. How the hell are you so good at this?"
            jenny "*slurp* It's not that hard~ I suppose I'm just naturally talented at sucking straws."
    else:
        if scene112_sex_v:
            if scene112_sex_pov:
                $ scene112_sex_pov = False
                show s112_vsex1 with dissolve
            else:
                $ scene112_sex_pov = True
                show s112_vsex2 with dissolve
        else:
            if scene112_sex_pov:
                $ scene112_sex_pov = False
                show s112_asex1 with dissolve
            else:
                $ scene112_sex_pov = True   
                show s112_asex2 with dissolve    
    call screen scene112_sex with dissolve

label scene112_sex_bj:
    $ scene112_sex_bj = True
    $ scene112_sex_sex = False
    if scene112_switch_bj_v:
        if scene112_switch_bj_v_first:
            $ scene112_switch_bj_v = False
            $ scene112_switch_bj_v_first = False
            $ scene112_switch_bj_v_second = True
            jenny "Ahnnm~ You want me to clean my own pussy juice off your cock?"
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            mc "Tell me how you taste."
            jenny "Mmmph~ It's so dirty... I've tasted myself plenty before, but never like this..."
            jenny "See? Even after you fucked me, I'm still cleaning you like a good girl. You should be praising me more, don't you think~?"
            mc "Ahnng... good girl."
            jenny "*giggles* That's more like it."
        elif scene112_switch_bj_v_second:
            $ scene112_switch_bj_v_second = False
            jenny "*giggles* You want me to clean your cock after it's been inside my pussy again?"
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            jenny "Hmph... You're really pushing your luck, you know. A lady shouldn't have to taste herself like this..."
            perception "She pulls back slightly, strings of saliva and her own juices connecting her lips to your cock."
            jenny "Mmmph~ *lick* *gag* It tastes even stronger this time..."
            jenny "See? I'm cleaning you again like an obedient servant. You should be rewarding me for being such a good girl~"
            mc "Ahnhng!"
        else:
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            jenny "Say it! Say I'm a good girl for cleaning you like tihs!"
            mc "*chuckles* You're a good girl."

    elif scene112_switch_bj_a:
        if scene112_switch_bj_a_first:
            $ scene112_switch_bj_a = False
            $ scene112_switch_bj_a_first = False
            $ scene112_switch_bj_a_second = True
            jenny "A-After you've been in my ass?! This... this is really too much, even for me."
            mc "I want to see how well you serve me after taking it in the ass."
            jenny "Hmph. A first for everything, I suppose... Fuck me."
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            perception "Despite her complaint, she leans forward without hesitation and takes your cock back into her mouth, sucking and licking with surprising eagerness."
            jenny "Mmm... I can taste my own ass on you. How humiliating..."
            mc "God, this is hot... you're so good."
            jenny "Only because it's you. Don't think I'd ever do something this dirty for just anyone. You should feel {i}extremely{/i} special right now."
        elif scene112_switch_bj_a_second:
            $ scene112_switch_bj_a_second = False
            jenny "Again?! After you've been fucking my ass nonstop?!"
            perception "She stares at your cock, still slick from the walls of her colon, with clear hesitation."
            jenny "This is so humiliating... Only a pervert would make a noble lady do something like this."
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            sensation "She leans in and starts sucking and licking with shameless enthusiasm, you feel her throat gagging around you."
            jenny "*gag* Disgusting..."
        else:
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_bj2 with dissolve
            else:
                show s112_bj1 with dissolve
            jenny "You're really enjoying making me do this, aren't you? Hmph. Only because it's you... I'd never lower myself like this for anyone else."
            jenny "*slurp* You better remember how much I'm spoiling you right now."

    call screen scene112_sex with dissolve

default scene112_sex_first = True
label scene112_sex:
    $ scene112_sex_bj = False
    $ scene112_sex_sex = True
    if scene112_sex_first:
        $ scene112_sex_v = True
        $ scene112_sex_first = False
        $ scene112_sex_vag_second = True
        scene 112_s19 with Dissolve(1.0)
        mc "Fuck, Jenny... I wanna take you now."
        $ scene112_sex_pov = False
        scene 112_s18 with dissolve
        jenny "Had enough of my mouth~? Fine. My pussy is aching for you~"
        scene 112_s19 with dissolve
        scene 112_s20 with Fade(1.0,1.0,1.0)
        perception "Jenny goes over to her bed. She bends over, presenting her dripping enterance with eagerness."
        jenny "Mess up my insides please~! Hurry!"
        scene 112_s21 with Dissolve(1.0)
        play sound "se_sfx/sex/touch3.mp3" 
        jenny "Aahhn~! Gods... You're stretching me so much..."
        show s112_vsex1 with Dissolve(1.0)
        perception "You start moving your hips, your cock dialting her wide. Her ass bounces with every thrust."
        mc "Ahhnn! You're gripping me so hard!"
        jenny "Mfhmnnn~ I bet my pussy is so much tighter than anyone you've had before."
        jenny "Hahhn~! Aahnn~! Gods, I wanted you to mess up my needy pussy for so damn long~"
        call screen scene112_sex with dissolve
    else:
        if scene112_sex_v:
            $ scene112_sex_v = True
            $ scene112_sex_a = False
            $ scene112_switch_bj_v = True
            $ scene112_switch_bj_a = False
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_vsex2 with Dissolve(1.0)
            else:
                show s112_vsex1 with Dissolve(1.0)
            jenny "Nmmnn~ Ahhnn~ I know you want to, but don't you dare finish inside my pussy... Ahnnmm~"
            jenny "NO WAY I'm raising a peasant's child."
            mc "This peasant is making you drool all over your bed right now."
            jenny "...Mfhmmnn~"
        else:
            $ scene112_sex_a = True
            $ scene112_sex_v = False
            $ scene112_switch_bj_a = True
            $ scene112_switch_bj_v = False
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_asex2 with Dissolve(1.0)
            else:
                show s112_asex1 with Dissolve(1.0)
            jenny "Ahh! Fahnnm~! You better take full responsibility for turning a proper lady into such a lewd girl!"
            jenny "Goddss~! I feel you scrape my pussy walls through my asshole~! I'm... I'm feeling it poke my stomach too! Gahhh~! J-Just how thick is your fucking cock?!"
        call screen scene112_sex with dissolve

default scene112_sex_anal_first = True
default scene112_sex_anal_second = False
label scene112_sex_anal:
    if scene112_sex_anal_first:
        $ scene112_sex_anal_first = False
        $ scene112_sex_anal_second = True
        mc "I wanna feel your ass, Jenny."
        jenny "Hahhn~? But you're already feeling it slapping against your groin every time you move."
        mc "Not that. I meant your asshole. It's been winking and puckering at me nonstop."
        jenny "Wha—?!"
        jenny "Y-You really want to put it in there?! Are you serious right now?!"
        jenny "That place isn't for sex, you moron! Mfhmnn~ A noble lady like myself would never stoop so low... How disgusting of you to even suggest something like that!"
        call screen scene112_choice02 with dissolve
    else:
        $ scene112_sex_a = True
        $ scene112_sex_v = False
        $ scene112_switch_bj_a = True
        $ scene112_switch_bj_v = False
        if scene112_sex_anal_second:
            $ scene112_sex_anal_second = False
            scene 112_s22 with Dissolve(1.0)
            perception "You press the head of your cock against her tight, puckered entrance. Jenny tenses up immediately."
            jenny "A-Ahh! Wait! It's too big...! You pervert... mnnh!"
            scene 112_s23 with Dissolve(1.0)
            play sound "se_sfx/sex/touch4.mp3" 
            perception "Despite her loud complaints, she pushes back slightly, determined to take you."
            jenny "Hahh! It's going in! I can't believe something this thick is inside my asshole!"
            mc "Your pipe is yearning for it. Just let me in."
            jenny "Fughnnn~! M-Move already! I wanna know how this anal thing feels after hearing the brothel whores talking about it!"
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_asex2 with Dissolve(1.0)
            else:
                show s112_asex1 with Dissolve(1.0)
        else:
            scene black with Dissolve(0.3)
            if scene112_sex_pov:
                show s112_asex2 with Dissolve(1.0)
            else:
                show s112_asex1 with Dissolve(1.0)
            jenny "Ahhnnn~! Again!? You went back to my ass already?"
            jenny "Gahhnmm~ You really are a pervert. Using my ass and pussy like it's a toy to relieve yourself... I'm a human too, remember?!"
            perception "As you push back into her tight rear entrance, she lets out a sharp, needy moan."
            jenny "A-Ahhhn~! It still feels so strange! It's like your touching my stomach every time you go deep."
            jenny "Hahh... I can't believe I'm starting to enjoy this... You're corrupting me, you know that? An innocent girl..."
            mc "*chuckles* Innocent?"
            jenny "Why are you laughing?!"
    call screen scene112_sex with dissolve

label scene112_choice02_op1:
    mc "This is my reward, remember?"
    jenny "H-Hmph! I didn't mean {i}there{i}!"
    mc "Please~?"
    jenny "Insufferable... Making a highborn lady do something this filthy..."
    jenny "Ahnnmm~ F-Fine... But only because it's you. And you better be grateful! No one else would ever get this kind of privilege."
    jenny "Just... go slow at first, okay? If it hurts too much, I'll make you stop immediately."
    call screen scene112_sex with dissolve

label scene112_choice02_op2:
    mc "Fine. You don't have to if you don't want to."
    jenny "...Hmph. You're really going to back off just because I complained a little?"
    jenny "Idiot... I didn't say I {i}wouldn't{/i} do it. I just said it was disgusting."
    jenny "...You can try. But only a little. And you have to be gentle! If I don't like it, we stop right away. Understand?"
    call screen scene112_sex with dissolve

default scene112_sex_vag_second = False

label scene112_sex_vag:
    scene black with Dissolve(0.3)
    $ scene112_sex_v = True
    $ scene112_sex_a = False
    $ scene112_switch_bj_v = True
    $ scene112_switch_bj_a = False
    if scene112_sex_vag_second:
        $ scene112_sex_vag_second = False
        if scene112_sex_pov:
            show s112_vsex2 with Dissolve(1.0)
        else:
            show s112_vsex1 with Dissolve(1.0)
        jenny "Hmph. Don't get the wrong idea. I'm only doing this because my ass needs a break... Not because I like feeling you stretch my pussy more."
        mc "Ahnn! I can't get enough of this heat and tightness."
        jenny "Aahn~! Yes... Much better... My pussy feels so full compared to my ass."
        jenny "See? This is what a proper noble lady's holes feels like. You should be thanking me for letting you use all three of my pleasure holes."
    else:
        if scene112_sex_pov:
            show s112_vsex2 with Dissolve(1.0)
        else:
            show s112_vsex1 with Dissolve(1.0)
        jenny "Yes~! Mess up my bitch pussy! Ahhnn~ Mfhnnnn~"
        mc "Your gripping tight! I might not be able to pull out if you keep doing this."
        jenny "Ahhnn~! I don't care at this point~ Breed me~ Make me your sow~"
        jenny "Actually don't! Ahhnnn~ Fuck, I don't know what to think anymore! Damn this fat cock of yours for making me stupid~!"
    call screen scene112_sex with dissolve

label scene112_sex_cum:
    call screen scene112_choice03 with dissolve

label scene112_choice03_op1:
    if scene112_sex_v:
        mc "Jenny... I'm about to cum!"
        jenny "Then do it! Cover my back with your warm seed~"
        mc "No! I wanna finish inside you!"
        jenny "Wait, what!?"
        if persistent.xray_mode:
            scene 112_s28_xray1 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum9.mp3" 
            scene 112_s28_xray1 with vpunch
            sensation "You thrust deep one final time and release, flooding her tight walls with thick, hot spurts of cum."
            jenny "A-Agaahhn! You're impregnating me with your fucking child!"
            scene 112_s29_xray2 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum5.mp3" 
            scene 112_s29_xray2 with vpunch
            sensation "Her body trembles violently as she cums with you, her pussy clenching and milking every drop."
        else:
            scene 112_s28 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum9.mp3" 
            scene 112_s28 with vpunch
            sensation "You thrust deep one final time and release, flooding her tight walls with thick, hot spurts of cum."
            jenny "A-Agaahhn! You're impregnating me with your fucking child!"
            scene 112_s29 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum5.mp3" 
            scene 112_s29 with vpunch
            sensation "Her body trembles violently as she cums with you, her pussy clenching and milking every drop."

        call pregnancy_check_jenny from _pregnancy_check_jenny
        jenny "I can't believe it! Y-You finsihed inside me!"
        play sound "se_sfx/sex/sex4.mp3" 
        if persistent.xray_mode:
            scene 112_s27_xray3 with Dissolve(1.0)
        else:
            scene 112_s27 with Dissolve(1.0)
        mc "Fuck... it felt too good to pull out."
        jenny "Oh, oh no! I... I'll be pregnant!"
        jenny "You! A fugitive {i}and{/i} a peasant! Came so much inside a noble lady!"
        mc "I was buried so deep... and you didn't help either by gripping so hard."
        jenny "Dammit..."
        jenny "*sigh* You better take responsibility if I get pregnant because of this!"
        mc "*chuckles* I will."
    elif scene112_sex_a:
        mc "I'll fill your ass!"
        jenny "Fhnnmgh~! Inside my ass?! You perverted— Ahhn~!"
        jenny "F-Fine! Do it! Fill my ass if you want it so badly!"
        scene 112_s24 with Dissolve(0.3)
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 112_s24 with vpunch
        sensation "You bury yourself to the hilt inside her tight ass and explode, pumping rope after rope of thick cum in the deepest part of her asshole."
        jenny "A-Aaahh~! It's so hot... I can feel you pulsing inside my ass... There's so much!"
        scene 112_s25 with Dissolve(0.3)
        play sound "se_sfx/sex/sex_cum6.mp3" 
        scene 112_s25 with vpunch
        jenny "FAAHHHHNNNN~!"
        perception "She shudders hard, her body twitching as she experiences a powerful anal orgasm."
        play sound "se_sfx/sex/sex4.mp3" 
        scene 112_s26 with Dissolve(1.0)
        jenny "Hahh... You actually came inside... How filthy~"
        mc "*laughs* It looks like you came from your ass. Not so filthy now, is it?"
        jenny "D-Don't you dare tell anyone about this! My reputation would be in the gutters if people knew I orgasmed from having my ass ploughed like some bitch..."
        mc "It will be our filthy secret."
    jump scene112_4

label scene112_choice03_op2:
    mc "I'm gonna mark you as mine!"
    jenny "Then pull out! Finish on me~"
    play sound "se_sfx/sex/touch3.mp3" 
    scene 112_s30 with vpunch
    sensation "You pull out at the last second. Thick ropes of cum shoot across her back and plump ass, painting her smooth skin white."
    jenny "Ahh~! It's so warm... You're making such a mess of me..."
    scene 112_s31 with Dissolve(0.3)
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 112_s31 with vpunch
    perception "She reaches back and spreads her ass slightly, letting some cum drip between her cheeks."
    jenny "Look what you did to a highborn lady... Covered in your seed like a cheap whore. Are you satisfied now?"
    jump scene112_4

label scene112_4:
    scene 112_s32 with Fade(1.3,1.0,1.5)
    play music "nature.mp3" fadein 1.0 volume 0.4 loop
    perception "After catching your breath, you gently go down on her, caressing her face."
    scene 112_s33 with dissolve
    jenny "You were really rough on me~"
    jenny "...But it felt good. Don't let it go to your head though."
    scene 112_s32 with dissolve
    mc "You were amazing."
    scene 112_s33 with dissolve
    jenny "Of course I was... I'm me, after all."
    scene 112_s32 with dissolve
    mc "I should leave now. I have places to be, Jenny."
    scene 112_s33 with dissolve
    jenny "I know. Next time you come... you better stay longer. A noble lady like me deserves proper aftercare, you know."
    scene 112_s32 with dissolve
    mc "*chuckles* I'll keep that in mind."
    scene 112_s33 with dissolve
    jenny "And you can stop playing with my breast, you perv."
    jenny "It feels cold. Are these metal gloves?"
    scene 112_s32 with dissolve
    mc "...Something like that."
    scene black with Dissolve(2.0)
    perception "She blows you a kiss, and you slip out of her room."
    $ renpy.end_replay()
    jump scene113

label scene111_choice06_op2:
    $ mc_sex_jenny = False
    mc "Sorry, but I just remembered something really important... I really need to go."
    scene 112_s7 with dissolve
    if not mc_accept_jenny:
        jenny "Hmph! You're rejcting me again?!"
        jenny "*sigh* You do realize that this will me make me seek you out more, right?"
    else:
        jenny "Hmph! How boring."
        jenny "Fine... b-but you really... I really need you to do me at some point."
    scene 112_s8 with dissolve
    mc "*chuckles* Later, Jenny. Take care of yourself, and your dad."
    jump scene113

label scene113:
    if mc_helped_lena:
        scene 113_s1 with Fade(1.5,1.0,1.3)
        lena "*sigh* I need some time to clear my head, [mc]. Meet you back at the stables, alright? Give me an hour or two."
        scene 113_s2 with Dissolve(1.0)
        mc "Not going together? The streets aren't safe."
        lena "I'm the most dangerous thing in these streets right now."
        lena "Sorry. This was all... too much. I need to process it all before I can be useful to anyone."
        if mc_convince_lena:
            lena "I almost became something I can't come back from. You stopped that. I know I should be grateful, but right now I just feel... raw."
        mc "No pressure. Take the time you need. I might have a few things to do first."
        stop music fadeout 4.0 
    else:
        stop music fadeout 2.0 
        scene 113_s3 with Fade(1.5,1.0,1.3)
        if mc_harem_diana or mc_friend_diana:
            mc "(I might have enough coin to finally buy the brothel from Diana's boss. I can go there before returning to the hideout.)"
        else:
            mc "(I need to head back to the hideout.)"

    scene 113_s4 with Fade(1.5,1.0,1.3)
    ""
    scene 113_s5 with Dissolve(0.3)
    play sound "sound_effects/clothing_rustle.mp3"
    scene 113_s5 with vpunch
    perception "A shadow detaches itself from the alley wall behind you. Light feet. You hear it, but it's too late."
    alice "Ahah! So it {i}was{/i} you!"
    mc "What the—!?"
    play music "tense/alice.mp3" fadein 1.0 loop
    scene 113_s6 with dissolve
    alice "[mc]. Your physique was all too similar. I've got a good eye for those things, even under a hood."
    alice "You can hide your face, but you can't hide the way you carry yourself."
    scene 113_s7 with dissolve
    mc "Look, Alice. Whatever you were instructed to do, you must know that I'm innocent!"
    scene 113_s6 with dissolve
    alice "Innocent? You call what you did at the market {i}innocent{/i}?! I saw the what happened to some of our men, [mc]. I helped carry them out. Men I served with. Men who had families."
    alice "Save your speeches for the court. It's time you finally face justice."
    scene 113_s7 with dissolve
    mc "There is no justice here. Do you not see what Avery is doing? Allowing slavery, the new foreign guards, the princess—"
    mc "There's barely any guards on the street today. Ask yourself why."
    scene 113_s8 with Dissolve(1.0)
    empathy "She flinches. Barely perceptible, but there. Something shifts behind her eyes."
    scene 113_s9 with dissolve
    alice "...I'm not blind. I see what's happening. But this is for the best."
    alice "The city needs stability. Avery provides that. What's happening with the princess is... regrettable, but necessary for conspiring with you."
    scene 113_s8 with dissolve
    mc "Necessary? She had no role in this, Alice. Don't guards swear an oath to protect the innocent?"
    scene 113_s9 with dissolve
    alice "I was demoted, you know? A common soldier, where once I was a respectable lieutenant. My quarters, my rank, my seat at the table... all stripped away."
    alice "Do you know what it's like to salute officers who used to call you equal? To take orders from men you trained?"
    scene 113_s8 with dissolve
    mc "She treated you like this and you still want to serve her?"
    scene 113_s9 with dissolve
    alice "You don't understand. I was... I was simply incompetent by our new majesty's standards."
    alice "That's all it is. A failure of performance, not of loyalty. I need to work harder to prove myself again."
    alice "You're my ticket back. Once I bring you back to her... I will regain my position. Everything goes back to how it was. Everything makes sense again..."
    scene 113_s8 with dissolve
    mc "..."
    scene 113_s6 with dissolve
    alice "Now. You can come with me the easy way... or I'll drag you back in chains. Your choice."
    alice "I remember how terrible you were during training with Adam. All those rumors about you fighting Gaius are just that... {i}rumors{/i}. So I suggest you don't make this difficult."
    scene 113_s7 with dissolve
    impulse "How convenient. It's just the two of you in this dark, empty alley. No one would ever know if you got rid of her right now."
    scene 113_s10 with Dissolve(0.3)
    play sound "sound_effects/body/smack.mp3"
    scene 113_s10 with vpunch
    perception "In a blur, you close the distance, grab her sword arm, and twist it sharply. The blade falls and clatters in the ground."
    scene 113_s11 with dissolve
    alice "Hah—?!"
    mc "Stand down, Alice."
    play sound "sound_effects/punch2.mp3"
    scene 113_s12 with vpunch
    alice "Hng!"
    play sound "sound_effects/punch.mp3"
    scene 113_s13 with Dissolve(0.3)
    scene 113_s13 with vpunch
    alice "AAHH!"
    play sound "sound_effects/punch4.mp3"
    scene 113_s14 with Dissolve(0.5)
    scene 113_s14 with vpunch
    alice "Hng!"
    mc "Gahh fuck! Alright, that's enough! That one actually hurt."
    scene 113_s15 with dissolve
    alice "H-How?! How are you not reacting to my attacks?!"
    scene 113_s16 with dissolve
    perception "She struggles hard at first, trying to break free, but quickly realizes she can't. Her eyes widen in disbelief."
    scene 113_s15 with dissolve
    alice "What the hell...?! Help! I need backup!"
    scene 113_s16 with dissolve
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene113_choice01 with dissolve

label scene113_choice01_op3:
    $ mc_convince_alice = True
    scene 113_s17 with Dissolve(1.0)
    mc "I don't want to hurt you, Alice. I don't want to hurt anyone."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    mc "Avery is using you. Look at yourself right now, is this really the person you want to be?"
    scene 113_s18 with dissolve
    alice "You don't get to lecture me about who I am."
    scene 113_s17 with dissolve
    mc "Not too long ago, I overheard her. Avery's planning to execute the princess. I'm sure you've heard the rumors."
    hide screen stat_change with easeoutright
    $ karma_more = False
    alice "..."
    mc "Is that the kind of ruler you want to serve? Someone who kills her own blood for power?"
    scene 113_s18 with dissolve
    alice "I... I don't know what's right anymore."
    alice "What other choice do I have?!"
    scene 113_s17 with dissolve
    mc "You still have a second choice. Let me go. Pretend you never saw me today. I'm going to fix this. I swear it."
    scene 113_s18 with dissolve
    alice "I don't trust you."
    scene 113_s17 with dissolve
    mc "Do you trust Avery more?"
    scene 113_s18 with dissolve
    alice "...No."
    scene 113_s17 with dissolve
    mc "Then take the better gamble. A lot of people are depending on me, Alice. If I get captured, the princess dies with me."
    scene 113_s19 with Dissolve(1.0)
    alice "Ahh... Dammit! I swear I can't even tell my head from my heart these days..."
    alice "Just... go! And don't let me catch you again."
    mc "Thank you. You did the right thing."
    alice "..."
    scene 113_s25 with Fade(1.0,0.5,0.7)
    jump scene113_2

label scene113_choice01_op2:
    $ mc_scare_alice = True
    mc "Listen very carefully, Alice."
    mc "I'm not the same man you saw training before. Not anymore. If I wanted you dead... you'd already be dead."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    empathy "Her breathing becomes rapid and shallow. Her body starts trembling."
    scene 113_s15 with vpunch
    alice "Let go of me, [mc]! This isn't funny! You're only delaying the inevitable."
    scene 113_s16 with dissolve
    mc "Does it look like I'm joking?"
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 113_s15 with dissolve
    alice "Y-You... you really did fight Gaius, didn't you? No human should be this strong... How are you still alive?!"
    scene 113_s16 with dissolve
    mc "I did. And yet here you are, confronting a dangerous fugitive alone in a dark alley by yourself. How stupid can you be?"
    scene 113_s15 with dissolve
    alice "I... I wasn't alone! There were... There had to be—"
    scene 113_s16 with dissolve
    mc "There's no one here. Just you and me."
    mc "You realize how easy it is to just... get rid of you, right here and now?"
    scene 113_s20 with Dissolve(1.0)
    perception "Her legs shake violently. A moment later, a wet trickle runs down her thigh as she loses control of her bladder."
    alice "...No."
    play sound "sound_effects/body/pee2.mp3" fadein 1.0 fadeout 1.0
    scene 113_s21 with Dissolve(1.0)
    mc "I'll save the princess and this city. Only then you'll get your position back. Not by... this."
    mc "Now go home, Alice. Forget you saw me. Tell no one."
    alice "I... I won't say anything. I swear it. Just... please don't kill me."
    play sound "sound_effects/running_concrete.mp3"
    scene 113_s22 with Dissolve(1.0)
    perception "You slowly release her. She runs out of the alley, legs too weak to hold her up properly."
    stop sound fadeout 0.5
    scene 113_s25 with Fade(1.0,0.5,0.7)
    jump scene113_2
    
default mc_killed_alice_counted = False

label scene113_choice01_op1:
    $ mc_killed_alice_counted = True
    $ mc_killed_alice = True
    if mc_karma > 1:
        $ mc_karma -= 4
    if mc_karma <= 1:
        $ mc_karma = 1
    scene 113_s23 with dissolve
    perception "Your hand snaps forward, grabbing her by the neck and the back of her head."
    alice "Ghng!"
    play sound "sound_effects/body/bonecrack2.mp3"
    scene 113_s24 with vpunch
    perception "With one brutal twist, you snap her neck."
    scene 113_s25 with Dissolve(1.5)
    perception "Her body collapses to the ground like a discarded doll. No struggle. No resistance. She never even had time to scream."
    mc "..."
    jump scene113_2

label scene113_2:
    if diana_pregnant:
        $ mc_harem_diana = True

    stop music fadeout 3.0 
    if mc_convince_alice or mc_scare_alice:
        if mc_princess_alex:
            mc "(I don't know if Alice will keep her word. I must rescue the princess as soon as possible and leave this city.)"
        else:
            mc "(I don't know if Alice will keep her word. I must leave for Nahraya as soon as possible.)"
    else:
        if mc_princess_alex:
            mc "(Someone is bound to know what happened to Alice. A former lieutenant doesn't just get killed without questions being asked. I better rescue the princess as soon as possible and leave this city.)"
        else:
            mc "(Someone is bound to know what happened to Alice. A former lieutenant doesn't just get killed without questions being asked. I better leave this city as soon as possible.)"
            
    if mc_friend_diana or mc_harem_diana:
        if mc_coin >= brothel_coin_new:
            mc "(I also have enough to buy the brothel now. I can return to Diana and give her some good news before I go anywhere else.)"
        else:
            mc "(Dammit! Even after that, I still don't have enough to buy the brothel... Maybe I'll have another chance.)"
    
    call screen scene113_choice02 with dissolve

label scene114:
    if mc_coin < brothel_coin_new:
        mc "(I don't have enough coin to buy the brothel...)"
        call screen scene113_choice02 with dissolve
    else:
        scene 114_s1 with Fade(1.5,1.0,1.3)
        play music "diana.mp3" fadein 1.0 loop
        drunk "Good sirr. Gooood sir. Got a copper for meh? Just one."
        scene 114_s2 with Dissolve(1.0)
        drunk "Ey! I was talking to ya!"
        scene 114_s3 with Fade(0.5,0.5,0.5)
        di "Ohh! H-Hello there, sir! Can I help you this fine morning? A drink, perhaps? A room?"
        di "{size=30}[mc], what are you {i}doing{/i}?! I told you to knock on the window! Not waltz through the front door like you own the—{/size}"
        di "{size=30}Wait. Why are you smiling?{/size}"
        play sound "sound_effects/coin_pouch.mp3"
        scene 114_s4 with dissolve
        stop sound fadeout 0.5
        perception "You reach into your pocket, pull out a heavy leather pouch, then throw it onto the counter. Vera's eyes flick down. Her expression barely changes, but one eyebrow slowly rises."
        mc "I want to buy this establishment."
        di "W-What?"
        scene 114_s5 with Dissolve(1.0)
        vera "Hmm? And who told you it's for sale in the first place, hon?"
        vera "Am I missing something? Because I'm fairly certain I would've remembered deciding to sell my life's work to some stranger."
        scene 114_s6 with dissolve
        di "Five... ten... fifteen... [brothel_coin_new]!"
        scene 114_s7 with dissolve
        di "*ahem* Surely this is more than enough for this gentleman to buy the brothel, miss Vera. Generous, even."
        scene 114_s8 with Dissolve(1.0)
        vera "Hmph. It ain't for sale, honey. Hasn't been for forty years. This was my family's business for Gods know how long"
        vera "My grandmother ran it, her mother before her, and her mother before her, all the way back to when this district was but an empty grassy field."
        vera "I'm not about to sell it to some suspicious guy who finishes too early and calls it a night."
        scene 114_s9 with dissolve
        mc "I don't—"
        scene 114_s8 with dissolve
        vera "You think owning a brothel is all shits and giggles? It ain't. It's work. Hard work."
        vera "What would someone like you possibly know about operating a brothel, hmm?"
        vera "In your expert opinion, what's the most important thing in running a successful, respectable brothel?"
        scene 114_s9 with dissolve
        mc "Well... Let me just gather my thoughts outloud. *ahem* {size=30}Diana...{/size}"
        scene 114_s10 with Dissolve(1.0)
        call screen scene114_choice01 with dissolve
    
default mc_correct_answer_brothel = 0
label scene114_choice01_op1:
    scene 114_s11 with dissolve
    mc "Making sure the girls are extremely attractive is the priority. If they don't catch the eye, customers won't even walk through the door."
    scene 114_s12 with dissolve
    vera "Gods give me patience... You're a proprietor, not a pimp. Wrong."
    scene 114_s12 with dissolve
    jump scene114_2
label scene114_choice01_op2:
    scene 114_s11 with dissolve
    mc "Charging the highest prices possible. Exclusivity brings in the real money."
    scene 114_s12 with dissolve
    vera "That's how you run a scam, not a brothel. High prices without high standards just means you're fleecing fools until word gets around. And word always gets around."
    scene 114_s12 with dissolve
    jump scene114_2
label scene114_choice01_op3:
    $ mc_correct_answer_brothel += 1
    scene 114_s14 with dissolve
    mc "Keeping the girls safe and well taken care of. Happy workers do good work."
    scene 114_s13 with dissolve
    vera "Hmph. I see you did your studies."
    scene 114_s12 with dissolve
    jump scene114_2
label scene114_choice01_op4:
    scene 114_s11 with dissolve
    mc "You need the best alcohol and entertainment. If the drinks are good and the music's lively, they'll spend more and tell their friends."
    scene 114_s12 with dissolve
    vera "This isn't a tavern, boy. If they want ale and a lute, there's a dozen places on this street alone. They come here for something else entirely."
    scene 114_s12 with dissolve
    jump scene114_2
    
label scene114_2:
    vera "Next. It's a busy night. Suddenly, some drunk asshole starts causing a ruckus, shouting slurs, and he's got his hands on one of the girls. She's scared stiff. What do you do?"
    scene 114_s15 with Dissolve(1.0)
    call screen scene114_choice02 with dissolve

label scene114_choice02_op1:
    scene 114_s11 with dissolve
    mc "Call the guards. That's what they're paid for."
    scene 114_s12 with dissolve
    vera "By the time the guards show up, *chuckles* if they show up—the girl's got a black eye and half the brothel is in dissary."
    vera "The guard could barely care about a brothel. You're on your own in here. Always."
    jump scene114_3
label scene114_choice02_op2:
    scene 114_s11 with dissolve
    mc "Let the girl handle it. She'll grow a spine if it happens enough."
    scene 114_s12 with dissolve
    vera "If you think any girl under my roof deserves to handle an assault alone while you sit back counting coin, you can walk out that door right now. Disgusting."
    jump scene114_3
label scene114_choice02_op3:
    scene 114_s11 with dissolve
    mc "Offer him a free drink to calm down, then ask him to leave politely. No need to cause a scene that'll frighten the other customers."
    scene 114_s12 with dissolve
    vera "Reward bad behavior with free alcohol? Next time he'll come back and do it twice as bad, because he knows he'll get a free drink out of it."
    jump scene114_3
label scene114_choice02_op4:
    $ mc_correct_answer_brothel += 1
    scene 114_s14 with dissolve
    mc "Step in myself. Physically remove him from the place, make it clear we don't tolerate that behavior."
    scene 114_s13 with dissolve
    vera "*chuckles* Good. That's how it's done."
    scene 114_s12 with dissolve
    jump scene114_3

label scene114_3:
    vera "Another one, boy. One of your girls comes up to you. She's nervous, twisting her apron in her hands. And then she tells you she's pregnant."
    vera "What do you do with her?"
    scene 114_s16 with Dissolve(1.0)
    call screen scene114_choice03 with dissolve

label scene114_choice03_op1:
    $ mc_correct_answer_brothel += 1
    scene 114_s14 with dissolve
    mc "Support her until the child is born. Then we decide together what's best for her and the baby."
    scene 114_s13 with dissolve
    vera "Hmph. You actually thought about that, didn't you?"
    vera "Most men don't. Most men think a whore's just a body that pays rent. You seem to understand they're people."
    jump scene114_4
label scene114_choice03_op2:
    scene 114_s11 with dissolve
    mc "I'd have to let her go. She can't work in her condition."
    scene 114_s12 with dissolve
    vera "True, but also heartless. You think a pregnant girl with no coin and no references survives long on these streets?"
    jump scene114_4
label scene114_choice03_op3:
    scene 114_s11 with dissolve
    mc "Give her a bonus and wish her luck."
    scene 114_s12 with dissolve
    vera "A bonus and a pat on the back? How generous. Wrong."
    jump scene114_4
label scene114_choice03_op4:
    $ mc_correct_answer_brothel -= 1
    scene 114_s11 with dissolve
    mc "She'd have to keep working. Business is business. She knew the risks when she took the job."
    empathy "She doesn't even dignify that with a response. She just looks at you with disappointment."
    jump scene114_4

label scene114_4:
    if mc_correct_answer_brothel == 3:
        $ mc_bought_brothel = True
        $ mc_coin -= brothel_coin_new
        scene 114_s17 with Dissolve(1.4)
        vera "Well, I'll be damned. You actually know what you're talking about."
        vera "The Slick Worm is yours. Try not to burn it down. And if I hear you've been mistreating the girls, I'll come back and haunt you myself."
        scene 114_s18 with dissolve
        mc "Understood. I won't let you down."
        scene 114_s17 with dissolve
        vera "See that you don't. Now if you'll excuse me, I have a bottle of very old wine I've been saving for a day exactly like this."
        scene 114_s18 with dissolve
        scene 114_s24 with Dissolve(0.3)
        play sound "se_sfx/blowjob/kiss4.mp3" 
        scene 114_s24 with vpunch
        perception "Diana launches herself across the counter and wraps her arms around you in a fierce sloppy kiss. She holds on for exactly three seconds before her brain catches up with her body."
        scene 114_s25 with Dissolve(1.0)
        di "I mean—! Congratulations, sir! A wise investment indeed!"
        if mc_harem_diana:
            di "{size=30}You actually did it. I love you so much, darling.{/size}"
        else:
            di "{size=30}You actually did it.{/size}"
        scene 114_s26 with dissolve
        mc "{size=30}I said I will, didn' I?{/size}"
        scene 114_s25 with dissolve
        di "*giggles* I'll start preparing the ownership papers immediately. Come, let's go to Vera's offi—{i}your{/i} office."
        scene 114_s26 with dissolve
        jump scene114_5
    elif mc_correct_answer_brothel == 2:
        $ mc_bought_brothel = True
        $ mc_coin -= brothel_coin_new
        scene 114_s19 with Dissolve(1.4)
        vera "Hmm... You've got the right instincts, even if your judgment needs seasoning."
        vera "I'm going to do something I don't usually do. I'm going to sell you this establishment on probation."
        vera "You get one year. If, at the end of that year, the girls are happy, the books are balanced, and the place hasn't burned to the ground, it's yours free and clear. If not..."
        scene 114_s17 with Dissolve(1.0)
        vera "Let's just say you don't want to find out what happens if not. The Slick Worm is yours. For now. Don't make me regret this."
        scene 114_s18 with dissolve
        mc "Understood. I won't let you down."
        scene 114_s17 with dissolve
        vera "See that you don't. Now if you'll excuse me, I have a bottle of very old wine I've been saving for a day exactly like this."
        scene 114_s18 with dissolve
        scene 114_s24 with Dissolve(0.3)
        scene 114_s24 with vpunch
        perception "Diana launches herself across the counter and wraps her arms around you in a tight, fierce hug. She takes your lips for exactly three seconds before her brain catches up with her body."
        scene 114_s25 with Dissolve(1.0)
        di "I mean—! Congratulations, sir! A wise investment indeed!"
        di "{size=30}You actually did it. I love you so much, darling.{/size}"
        scene 114_s26 with dissolve
        mc "{size=30}I said I will, didn' I?{/size}"
        scene 114_s25 with dissolve
        di "*giggles* I'll start preparing the ownership papers immediately. Come, let's go to Vera's offi-{i}your{/i} office."
        scene 114_s26 with dissolve
        jump scene114_5
    else:
        $ mc_failed_buy_brothel = True
        scene 114_s20 with Dissolve(1.4)
        vera "You've got the coin, but you don't have the sense. Come back when you've spent a few months working the floor and learning what this life actually requires. Then we'll talk."
        scene 114_s21 with dissolve
        di "That's... that's perfectly fair! A delay, not a refusal! He'll be back! He's a fast learner! R-Right sir?"
        scene 114_s22 with dissolve
        mc "(Dammit... I couldn't buy the brothel. Maybe I'll have a second chance when I return from Nahraya.)"
        mc "Fine then. Next time I'll come back more prepared."
        scene 114_s21 with dissolve
        di "Goodbye, sir..."
        scene 114_s23 with Dissolve(1.5)
        empathy "You hear something in Diana's voice, a crushing sadness, the sound of someone who pinned all her hopes on this moment and watched them slip away."
        call screen scene113_choice02 with dissolve

label scene114_5:
    stop music fadeout 1.0 
    scene 114_s27 with Fade(1.5,1.0,1.3)
    play music "fire.mp3" fadein 1.0 volume 0.2 loop
    di "I'll put in a fake name, something innocuous, easy to forget. The royal court won't look twice at a transaction this clean."
    di "I'll turn in the papers first thing tomorrow morning. Afterwards, this place will be officially and legally yours."
    scene 114_s28 with Dissolve(1.0)
    mc "Good. Now... what's there to do? I've never owned a business before."
    scene 114_s29 with Dissolve(1.0)
    di "Well, I did say I wanted to turn this place into a tavern."
    di "Proper food, good ale, music that doesn't make your ears bleed. Somewhere people come to eat and drink and be merry, not just a place to get shove your cock in others."
    scene 114_s30 with dissolve
    call screen scene114_choice04 with dissolve

default brothel_name = "Slick Worm"

label scene114_choice04_op1:
    $ mc_changed_to_tavern = True
    mc "Sounds good. A tavern feels... honest."
    scene 114_s29 with dissolve
    di "Yes! Oh, this is going to be wonderful! We'll need a new name, though—something that doesn't sound like a... brothel."
    scene 114_s30 with dissolve
    mc "A new name, huh?"
    scene 114_s29 with dissolve
    di "First impressions matter. We need a name that sets the tone. It should be memorable, but not embarrassing. Classy, but not pretentious. Fun, but not silly."
    di "Any ideas?"
    scene 114_s30 with dissolve
    mc "Shit, I was never good with names."
    mc "Let me think."
    call screen scene114_choice05 with dissolve

label scene114_choice05_op1:
    $ brothel_name = "The Drunken Bastard"
    mc "How about 'The Drunken Bastard'?"
    scene 114_s31 with dissolve
    di "The... The Drunken Bastard?"
    di "That's absolutely terrible! The sign painter would charge double just for the embarrassment!"
    di "*sigh* ...I love it. I hate that I love it, but I love it. 'The Drunken Bastard' it is."
    scene 114_s32 with dissolve
    mc "See? Memorable."
    scene 114_s31 with dissolve
    di "That's one word for it."
    jump scene114_6

label scene114_choice05_op2:
    $ brothel_name = "Gronko's Rest"
    mc "How about 'Gronko's Rest'?"
    scene 114_s31 with dissolve
    di "Gronko's Rest? Who the hell is Gronko?"
    scene 114_s32 with dissolve
    mc "My new nickname as the owner. Got a nice ring to it, no?"
    scene 114_s31 with dissolve
    di "...Sure. If that's what you want. It'll definitely turn some heads, I think."
    jump scene114_6
    
default mc_brothel_name_fail = False

label scene114_choice05_op3:
    $ mc_brothel_name_fail = True
    mc "How about 'The New Queen is a Bitch'?"
    scene 114_s32 with dissolve
    di "..."
    perception "Diana stares at you in dead silence for several seconds."
    scene 114_s31 with dissolve
    di "Are you trying to get us executed? Because that is a very fast way to get us executed."
    di "We'd be shut down and hanged before the paint on the sign even dried."
    di "*sigh* Please tell me you have at least one idea that won't get us killed..."
    scene 114_s32 with dissolve
    call screen scene114_choice05 with dissolve

label scene114_choice05_op4:
    $ brothel_name = renpy.input("What should I name the brothel?", length=32)
    $ brothel_name = brothel_name.strip() 
    mc "How about... [brothel_name]?"
    scene 114_s29 with dissolve
    di "Hmm. If that's what you want."
    di "From this day forward, this establishment shall be known as [brothel_name]!"
    jump scene114_6

label scene114_choice04_op2:
    $ mc_remain_brothel = True
    mc "Actually, Diana. I would prefer if this remained a brothel."
    scene 114_s31 with dissolve
    di "Huh? B-But why?"
    scene 114_s32 with dissolve
    mc "Think about it. There are too many taverns around here—every other door on this street serves cheap trash."
    mc "This place stands out because it's the only one of its kind around here. We'd be giving up our only competitive advantage."
    scene 114_s31 with dissolve
    di "I... I get that from a business standpoint. It makes sense. It's just..."
    scene 114_s32 with dissolve
    mc "Trust me. Under my management, we'll be making bank. Quality girls, better food and drinks, a reputation that brings in nobles from the castle district."
    mc "And don't worry. You'll be a manager, not a worker."
    scene 114_s31 with dissolve
    di "On one hand, I like taverns more. They smell better, for one thing. On the other... coin. I do like coin. And Miss Vera always said I had a head for management."
    di "Fine. You're the owner. You get to decide in the end. The Slick Worm remains... well, The Slick Worm."
    di "Unless you have something else in mind?"
    scene 114_s32 with dissolve
    call screen scene114_choice06 with dissolve

label scene114_choice06_op1:
    mc "No need to change the name."
    scene 114_s29 with dissolve
    di "Got it."
    jump scene114_6

label scene114_choice06_op2:
    $ brothel_name = renpy.input("What should I name the brothel?", length=32)
    $ brothel_name = brothel_name.strip() 
    mc "How about... [brothel_name]?"
    scene 114_s29 with dissolve
    di "Hmm. If that's what you want."
    di "From this day forward, this establishment shall be known as [brothel_name]!"
    jump scene114_6

label scene114_6:
    scene 114_s30 with dissolve
    mc "Now that that's settled, let's move to other matters..."
    mc "I always forget to ask, are you the only one working here? I never see other girls around when I visit."
    scene 114_s33 with Dissolve(1.0)
    di "Ah, that's because they work the night shift."
    di "Lynn, Isabel, and Amy. They only come in after sundown. I'm the only girl who handles the day shift."
    scene 114_s34 with dissolve
    mc "Doesn't that sound... tiring? Handling the entire place by yourself?"
    scene 114_s35 with dissolve
    di "*scoff* If only Vera could understand that too. She always says no one comes during the day, so the work must be lighter. 'You've got it easy, girl', she'd tell me."
    di "Between you and me, I think she's just stingy when it comes to spending coin on extra help. She still counts every copper like it's her last."
    play sound "sound_effects/body/wood_slam.mp3"
    scene 114_s36 with vpunch
    di "Oh! How about we hire someone! Right now, before you go back to the life-threatening business you were doing."
    di "I could desperately use the help. Someone to cover the day shift with me."
    di "Don't worry about paying them for now, we'll just say that the first month is training."
    scene 114_s37 with dissolve
    mc "No pay for the first month, huh? Eugh... you're reminding me of things."
    scene 114_s36 with dissolve
    di "What do you think? Want to interview a few candidates? Or... you could leave it up to me if you're in a hurry."
    scene 114_s37 with dissolve
    call screen scene114_choice07 with dissolve

label scene114_choice07_op2:
    $ mc_left_hiring_diana = True
    mc "I'll leave it up to you. You know this place better than I do. And I trust your judgment."
    scene 114_s36 with dissolve
    di "...You do? *ahem* I mean—thank you!"
    scene 114_s37 with dissolve
    mc "I'll be going now, Diana. Take care of the place."
    scene 114_s36 with dissolve
    di "I will not let you down, darling! Come back safe!"
    scene 114_s37 with dissolve
    scene 114_s39 with dissolve
    call screen scene114_choice14 with dissolve

label scene114_choice07_op1:
    mc "Alright. Let's hire someone. I can spare some time for you."
    mc "Show me these candidates of yours."
    scene 114_s36 with dissolve
    di "Give me ten minutes and I'll have a list for you!"
    di "And umm... darling? I know I don't have to say this, but... just in case."
    di "You're the boss now. That means no touching the employees. At all. Understood?"
    scene 114_s37 with dissolve
    mc "Come on, do you really have so little faith in me?"
    scene 114_s36 with dissolve
    di "I'm just being cautious!"
    di "We don't want our new boss getting a reputation on the very first day. Or worse... a scandal before we've even breathed new life into the place."
    scene 114_s37 with dissolve
    scene 114_s38 with Fade(0.5,0.5,0.5)
    ""
    play sound "sound_effects/doors/door_open2.mp3"
    scene 114_s39 with Dissolve(1.0)
    if mc_remain_brothel:
        di "Sorry for the wait! I only managed to find one. It turns out not many girls are willing to work in a brothel after all."
    else:
        di "Sorry for the wait! I only managed to find one. It turns out not many girls are willing to work in a place that used to be a brothel."
        di "We'll have to build some reputation as a tavern before we start getting more candidates."
    scene 114_s40 with dissolve
    mc "No worries. Give it to me."
    if mc_freed_ruby:
        scene 114_s41 with dissolve
        play sound "sound_effects/paperOpen.mp3"
        call screen scene114_choice08 with dissolve
    else:
        scene 114_s41 with Dissolve(1.0)
        play sound "sound_effects/paperOpen.mp3"
        call screen scene114_choice09 with dissolve

label scene114_choice08_op1:
    mc "Sapphire Purple? What kind of name is that?"
    di "And she only wants three copper coins for a month's work. That's not even a wage, that's practically a slave at that point. Must be crazy desperate."
    mc "I'll interview her. Anyone who asks for that amount is either the most honest person in the city or running from something. Either way, I'm curious."
    stop music fadeout 1.0 
    jump scene114_7

label scene114_choice08_op2:
    $ mc_dismiss_ruby = True
    mc "Is this a joke? She put no work whatsoever into her resume. She isn't getting an interview."
    di "Perhaps we could've seen what she was first, but... alright. Sapphire Purple remains a mystery."
    di "I'll go see if there are any others."
    scene 114_s39 with Fade(1.5,1.0,1.3)
    di "[mc]! I found another! This one looks a lot more promising."
    scene 114_s41 with Dissolve(1.0)
    play sound "sound_effects/paperOpen.mp3"
    call screen scene114_choice09 with dissolve

label scene114_7:
    $ mc_interview_ruby = True
    scene 114_s42 with Fade(1.5,1.0,1.3)
    play music "side_event7.mp3" fadein 1.0 loop
    perception "A young woman walks in with confident, almost aggressive strides. Her face is sharp and hardened, like someone who's seen too much too soon."
    scene 114_s43 with Dissolve(1.0)
    mc "Hello. Take a sea—"
    scene 114_s45 with dissolve
    sapphire "Hey."
    scene 114_s44 with dissolve
    mc "Hey... Have I seen you before?"
    if mc_helped_ruby:
        scene 114_s45 with dissolve
        sapphire "We might've crossed paths once or twice."
        scene 114_s44 with dissolve
        mc "Ruby?! W-What are you doing here? {i}How{/i} are you here?"
        scene 114_s45 with dissolve
        sapphire "Apparently the noble I 'offended' had a sudden change of heart. I was released from the dungeon this morning. Lucky me."
        scene 114_s44 with dissolve
        mc "(The noble...? Could it have been Gheris? He said he'd free his slaves. Maybe he pulled strings for her too.)"
        mc "That's... good for you. So why the name change?"
        scene 114_s45 with dissolve
        sapphire "Not just the name. Everything. New face, new name, new life. Just in case that bastard has a second change of heart."
        sapphire "Had a friend who's good with disguises. Cost me my last three silvers, but it's worth it. Ruby's dead. Long live Sapphire."
        scene 114_s44 with dissolve
        mc "I see. And you decide to come here the moment you're released? How long has it been, a couple hours at most?"
        scene 114_s46 with dissolve
        sapphire "I need coin if I'm going to survive out there while looking for my sister."
        sapphire "No more thieving. I'm looking for honest work... Well, as honest as this shithole can offer anyway."
        sapphire "Don't I look professional now? That woman with the dick sucking lips dressed me up in this outfit, and did my hair too."
        scene 114_s44 with dissolve
        if mc_changed_to_tavern:
            mc "Well... actually, we're in the middle of converting this place into a tavern."
            scene 114_s45 with dissolve
            sapphire "Tavern, brothel, doesn't matter to me. I'll work. Job's a job."
            sapphire "And by the way, I only put three coppers on the table to get your attention. I expect to be paid a lot more than that."
            scene 114_s44 with dissolve
            mc "Naturally... Alright, let's start the interview."
        else:
            mc "I see... Anyway, let's start the interview."
    else:
        scene 114_s45 with dissolve
        sapphire "Hey fucker."
        scene 114_s44 with dissolve
        mc "Ruby?! W-What are you doing here? {i}How{/i} are you here?"
        scene 114_s45 with dissolve
        sapphire "Apparently the noble I 'offended' had a sudden change of heart. I was released from the dungeon this morning. Lucky me."
        scene 114_s44 with dissolve
        mc "(The noble...? Could it have been Gheris? He said he'd free his slaves. Maybe he pulled strings for her too.)"
        mc "That's... good for you. So why the name change?"
        scene 114_s45 with dissolve
        sapphire "Not just the name. Everything. New face, new name, new life. Just in case that bastard has a second change of heart."
        scene 114_s44 with dissolve
        mc "I see. And you decide to come here the moment you're released? How long has it been, a couple hours at most?"
        scene 114_s45 with dissolve
        sapphire "I need coin if I'm going to survive out there while looking for my sister. My sister who you refused to help look for."
        scene 114_s44 with dissolve
        mc "Look, Ruby—Sapphire. I simply didn't want to take the risk. I just arrived in this... city. You think I would cause trouble the moment I set foot here??"
        scene 114_s46 with dissolve
        sapphire "Trouble? All I asked was to look for someone. But whatever. That's behind us now."
        sapphire "Besides, you're in the same position as me now. I've seen the posters. Wanted fugitive, huh? The reward for your capture is pretty high."
        sapphire "Oh, how karma comes and fucks you in the ass, huh?"
        scene 114_s47 with dissolve
        mc "*sigh* Let's move on."
        scene 114_s46 with dissolve
        sapphire "*scoff* Gladly. I suppose I need to suck up to you if I'm to work here, so... no more messing with you."
        sapphire "And no more thieving too. I'm looking for honest work... Well, as honest as this shithole can offer anyway."
        if mc_changed_to_tavern:
            scene 114_s44 with dissolve
            mc "Well... actually, we're in the middle of converting this place into a tavern."
            scene 114_s45 with dissolve
            sapphire "Tavern, brothel, doesn't matter to me. I'll work. Job's a job."
            sapphire "And by the way, I only put three coppers o.n the table to get your attention. I expect to be paid a lot more than that."
            scene 114_s44 with dissolve
            mc "Naturally... Alright, let's start the interview"

    call screen scene114_choice10 with dissolve

default ruby_questions = 0
default ruby_q1 = False
default ruby_q2 = False
default ruby_q4 = False
default ruby_q3 = False

default sarah_questions = 0
default sarah_q1 = False
default sarah_q2 = False
default sarah_q4 = False
default sarah_q3 = False

label scene114_choice10_op1:
    $ ruby_q1 = True
    $ ruby_questions += 1
    mc "Tell me about yourself."
    scene 114_s45 with dissolve
    sapphire "Not much to tell. I steal when I have to, I fight when I need to, and I don't take shit from anyone."
    sapphire "I'm not gonna smile and act sweet for the drunkards, but I get things done. Always have."
    scene 114_s44 with dissolve
    mc "You're not making a good first impression."
    scene 114_s45 with dissolve
    sapphire "I don't like to lie. I'm laying myself bare for you."
    scene 114_s44 with dissolve
    call screen scene114_choice10 with dissolve

label scene114_choice10_op2:
    $ ruby_q2 = True
    $ ruby_questions += 1
    mc "How do you think you can contribute to this place?"
    scene 114_s45 with dissolve
    sapphire "I'm good at reading people. I know when someone's about to cause trouble before they do. And if they do... I can handle them."
    sapphire "I don't scare easily, and I don't mind getting my hands dirty."
    scene 114_s44 with dissolve
    mc "Better not to get your hands dirty so soon after being released."
    scene 114_s45 with dissolve
    sapphire "Then I'll pick a mop. Happy?"
    scene 114_s44 with dissolve
    call screen scene114_choice10 with dissolve

label scene114_choice10_op3:
    $ ruby_q3 = True
    $ ruby_questions += 1
    mc "Do you have any past experience working in a place like this?"
    scene 114_s46 with dissolve
    sapphire "*laughs* You kidding? I've spent more nights in taverns and brothels than most girls my age spend in their own beds."
    scene 114_s47 with dissolve
    mc "Oh! So you worked in a place like this before?"
    scene 114_s46 with dissolve
    sapphire "Nah, I just like going there for drinks."
    scene 114_s47 with dissolve
    mc "..."
    call screen scene114_choice10 with dissolve

label scene114_choice10_op4:
    $ ruby_q4 = True
    $ ruby_questions += 1
    mc "Why do you want to work here?"
    scene 114_s45 with dissolve
    sapphire "Cuz' I want coin? What kind of stupid fuckin' question is that?"
    scene 114_s44 with dissolve
    mc "I get it, but you're not supposed to {i}say{/i} that."
    call screen scene114_choice10 with dissolve

label scene114_choice10_op5:
    mc "Alright. I think I've heard enough."
    if ruby_questions == 0:
        scene 114_s45 with dissolve
        sapphire "What? You didn't even ask me a single question?"
        sapphire "Not complaining though."
        scene 114_s44 with dissolve
        mc "I already know who you are."
    elif ruby_questions <= 2:
        scene 114_s45 with dissolve
        sapphire "That quickly?"
        sapphire "Not complaining though."
        scene 114_s44 with dissolve
        mc "I already know who you are."
    stop music fadeout 1.0 
    scene 114_s48 with Dissolve(1.0)
    sapphire "*sigh* Listen, [mc]... I know I'm not doing great right now. I'm not a dumbass."
    play music "fire.mp3" fadein 1.0 volume 0.2 loop
    sapphire "But I really need this job. Like, {i}really{/i} need it. You have no idea how badly I need the coin right now."
    scene 114_s49 with dissolve
    mc "Hmm..."
    scene 114_s48 with dissolve
    sapphire "I'll do anything for it."
    if mc_helped_ruby_after_sex2:
        scene 114_s48 with dissolve
        sapphire "I already tasted your cock once before... and I'll gladly do it again. If that's what it takes."
        scene 114_s49 with dissolve
        mc "..."
    else:
        scene 114_s49 with dissolve
        mc "Anything?"
        scene 114_s48 with dissolve
        sapphire "Anything. I'm not afraid to get my hands dirty... or my upper pussy, in this case."
        scene 114_s49 with dissolve
    call screen scene114_choice11 with dissolve

label scene114_choice11_op1:
    $ mc_hired_ruby = True
    mc "You're hired."
    scene 114_s48 with dissolve
    sapphire "Wait... r-really? You're not fucking with me, are you?"
    scene 114_s49 with dissolve
    mc "I'm not. Welcome to the team, Sapphire."
    scene 114_s50 with dissolve
    sapphire "Great! I didn't even have to get pubes stuck to the back of my throat."
    sapphire "Won't let you down, boss!"
    scene 114_s51 with Fade(1.0,1.0,1.0)
    play sound "sound_effects/doors/door_open2.mp3"
    di "Hmm? Are you already done with the interview? Well, I found another candidate!"
    scene 114_s53 with Dissolve(1.0)
    mc "Let me see."
    scene 114_s41 with Dissolve(1.0)
    play sound "sound_effects/paperOpen.mp3"
    call screen scene114_choice09 with dissolve
    
label scene114_choice11_op2:
    $ mc_dismiss_ruby = True
    mc "I'm sorry, but you're dismissed."
    sapphire "..."
    empathy "Her expression hardens instantly. She stands up, trying to maintain her pride."
    scene 114_s48 with dissolve
    sapphire "Figures. Another disappointment."
    sapphire "Whatever, I get my freedom back. I'm sure I can find something if I looked hard enough..."
    scene 114_s49 with dissolve
    mc "You're not gonna—"
    scene 114_s48 with dissolve
    sapphire "I aint a fucking snitch."
    scene 114_s49 with dissolve
    mc "...Good."
    scene 114_s67 with Dissolve(1.0)
    ""
    scene 114_s51 with Fade(1.0,1.0,1.0)
    play sound "sound_effects/doors/door_open2.mp3"
    di "Hmm? Are you already done with the interview? Well, I found another candidate!"
    scene 114_s53 with Dissolve(1.0)
    mc "Let me see."
    scene 114_s41 with Dissolve(1.0)
    call screen scene114_choice09 with dissolve
    
image s114_r1 = Movie(play="images/chapter5/scene114/s114_r1.webm", loop=True)
image s114_r2 = Movie(play="images/chapter5/scene114/s114_r2.webm", loop=True)
image s114_r3 = Movie(play="images/chapter5/scene114/s114_r3.webm", loop=True)

label scene114_choice11_op3:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_4_replay:
        $ persistent.chapter5_p7_4_replay = True

    $ mc_hired_ruby = True
    $ mc_hired_ruby_after_bj = True
    mc "Get on your knees."
    scene 114_s46 with dissolve
    sapphire "Straight to it, huh?"
    sapphire "Guess my throat is better at sucking cocks than at talking."
    sapphire "Fine. Let me show you how bad you want me here. I'll suck your whistle so good you'll start crying."
    scene 114_s47 with dissolve
    stop music fadeout 3.0 
    scene 114_s74 with Fade(1.0,0.5,1.0)
    perception "She slowly walks behind the desk and kneels in front of you, looking up with a mix of defiance and arousal."
    scene 114_s73 with dissolve
    sapphire "*chuckles* If only things were always this easy."
    sapphire "Well? What are you waiting for? Pull it out already."
    scene 114_s75 with Dissolve(1.0)
    sapphire "You fuckin' bastard! A-Already hard?! Don't tell me this was your intention all along?"
    scene 114_s76 with dissolve
    mc "*chuckes* Maybe."
    scene 114_s75 with dissolve
    sapphire "Degenerate... I can't imagine what you do to the other women here."
    scene 114_s76 with dissolve
    show s114_r1 with Dissolve(1.0)
    sensation "She wraps her chapped lips around the head. A shiver runs down your spine as she starts sucking."
    sapphire "*slurp* Mmm... You're throbbing already. Can't handle my slimy mouth?"
    sensation "She bobs her head steadily, teasing your head, her tongue swirling around your glans."
    sapphire "You like having a girl who just got out of the dungeon on her knees for you?"
    scene 114_s51 with Dissolve(1.0)
    play sound "sound_effects/doors/door_open2.mp3"
    di "Hmm? Are you already done with the interview? Well, I found another candidate!"
    scene 114_s53 with Dissolve(1.0)
    mc "Ahnn... D-Diana?!"
    scene 114_s52 with dissolve
    di "Here. She looks a lot more earnest than the last one... Sapphire, was it? She gave me lots of trouble while dressing her up."
    scene 114_s53 with dissolve
    sensation "Sapphire's eyes narrow at the insult. Without warning, she bites down gently on the head of your cock."
    scene 114_s55 with vpunch
    mc "AHHHH!"
    scene 114_s54 with dissolve
    di "[mc]!? Are you alright?!"
    scene 114_s55 with dissolve
    mc "S-Sorry, nothing! Thank you, Diana. I'll... ah... take a look at her."
    scene 114_s54 with dissolve
    di "Sure... I'll go look for more."
    scene 114_s55 with dissolve
    show s114_r1 with Dissolve(1.0)
    sapphire "{size=30}Earnest? That bitch. I'll show you earnest.{/size}"
    play sound "sound_effects/paperOpen.mp3"
    call screen scene114_choice09 with dissolve


label scene114_choice09_op1:
    mc "She's quite professional. Almost... too professional to want to work in a brothel."
    if mc_hired_ruby_after_bj:
        sapphire "{size=30}*gag* That's kind you want, no? *lick*{/size}"
        mc "{size=30}Fahnn... I guess.{/size}"
        mc "Bring her over, Diana!"
    else:
        di "I'll bring her over."
    stop music fadeout 1.0 
    jump scene114_8

label scene114_choice09_op2:
    if mc_hired_ruby_after_bj:
        mc "Five silver coins a month? Ahnn... Outrageous!"
        sapphire "{size=30}*slurp* That's what I was hoping to be paid.{/size}"
        mc "{size=30}You're special.{/size}"
        sapphire "{size=30}Nice try. *suck* But you're still not getting out of paying me fairly.{/size}"
        di "Umm... should I bring her over, [mc]?"
        mc "Y-Yes! Please do!"
        mc "I-I mean no! Diana, wait!"
        sapphire "*chuckles* Is my throat making your brain numb?"
        sapphire "I don't blame you. Might as well see what that bitch looks like first."
        stop music fadeout 1.0 
        jump scene114_8
    else:
        mc "Five silver coins a month? Outrageous!"
        di "That's the minimum wage here, [mc]..."
        mc "Well... I didn't like her!"
        di "*sigh* Fine. You're the boss."
        stop music fadeout 1.0 
        jump scene114_9

label scene114_8:
    scene 114_s56 with Fade(1.0,1.0,1.0)
    if not mc_hired_ruby_after_bj:
        play music "side_event2.mp3" fadein 1.0 loop
    if mc_interview_ruby:
        perception "Sarah enters the room with much more professionalism than Sapphire. She carries herself gracefully, with a warm and kind expression."
    else:
        perception "Sarah enters the room with a professional demeanor. She carries herself gracefully, with a warm and kind expression."
    scene 114_s57 with Dissolve(1.0)
    sarah "Thank you for seeing me, sir."
    scene 114_s58 with dissolve
    mc "Of course."
    scene 114_s57 with dissolve
    sarah "It's a pleasure to meet you."
    scene 114_s58 with dissolve
    mc "Likewise."
    sarah "..."
    mc "...Right. Please, have a seat."
    if mc_hired_ruby_after_bj:
        scene 114_s59 with Dissolve(1.0)
        pause 0.1
        show s114_r2 with Dissolve(1.0)
        perception "As Sarah sits down, Sapphire doesn't hesitate. Without making a sound, she dives back down, taking you much deeper this time."
        mc "Ahhnnnm!"
        sarah "Something the matter, sir?"
        mc "*chuckles* I'm fine."
        show s114_r3 with Dissolve(1.0)
        sensation "The sudden heat and tightness of her throat makes your hips buck. Sapphire doesn't stop, she pushes until her nose presses against your pelvis, holding you deep in her throat."
        sapphire "*gluck* *slurp*"
        sarah "Do you... hear something strange?"
        scene 114_s62 with Dissolve(1.0)
        mc "Ah! No, no. Must be the... the walls. It's an old building. Let's focus on the interview, shall we?"
        scene 114_s61 with dissolve
        sarah "Of course, sir."
        show s114_r3 with Dissolve(1.0)
    else:
        scene 114_s59 with dissolve
        mc "Let's start, shall we?"
        scene 114_s60 with dissolve
        sarah "Of course! I'm ready."
        scene 114_s59 with dissolve
    call screen scene114_choice12 with dissolve

label scene114_choice12_op1:
    $ sarah_q1 = True
    if mc_hired_ruby_after_bj:
        scene 114_s59 with dissolve
        mc "Ahhn... First question. Do you have past experiance in this role?"
        scene 114_s60 with dissolve
        sarah "I worked as a waitress for three years and as a personal maid for a minor noble house for another two."
        sarah "I'm very comfortable attending to guests and making sure they feel welcome."
        scene 114_s59 with dissolve
        show s114_r1 with Dissolve(1.0)
        sensation "Sapphire suddenly sucks hard on the head of your cock, swirling her tongue aggressively."
        mc "M-Mhm...! Very good! It's so good!"
        sarah "Umm... thank you!"
    else:
        mc "Do you have past experiance in this role?"
        scene 114_s60 with dissolve
        sarah "I worked as a waitress for three years and as a personal maid for a minor noble house for another two."
        sarah "I'm very comfortable attending to guests and making sure they feel welcome."
        scene 114_s59 with dissolve
        mc "That sounds pretty good."
        scene 114_s60 with dissolve
        sarah "Thank you!"
        scene 114_s59 with dissolve
    call screen scene114_choice12 with dissolve

label scene114_choice12_op2:
    $ sarah_q2 = True
    if mc_hired_ruby_after_bj:
        scene 114_s59 with dissolve
        mc "How would you handle a rude customer?"
        scene 114_s60 with dissolve
        sarah "With patience and a smile, sir. I always make sure to de-escalate most situations. I never take things personally."
        scene 114_s59 with dissolve
        show s114_r3 with Dissolve(1.0)
        sensation "Sapphire takes you all the way to the back of her throat, holding you there as it tightens around you."
        mc "A-Ahh...! Excellent answer."
        sarah "...Are you sure you're alright, sir? Your face is quite red. And... you're sweating a lot."
        mc "I assure that I'm perfectly fine."
    else:
        mc "How would you handle a rude customer?"
        scene 114_s60 with dissolve
        sarah "With patience and a smile, sir. I always make sure to de-escalate most situations. I never take insults to heart."
        scene 114_s59 with dissolve
        mc "Excellent answer."
    call screen scene114_choice12 with dissolve

label scene114_choice12_op3:
    $ sarah_q3 = True
    scene 114_s59 with dissolve
    mc "What are your strengths and weaknesses?"
    scene 114_s61 with dissolve
    sarah "My stenghts? Umm... I'm very organized! And attentive to detail, a-and excellent at reading what people need before they ask."
    sarah "As for weaknesses... Errm..."
    sarah "*chuckles* S-Sorry, I was never asked this question before."
    if mc_hired_ruby_after_bj:
        scene 114_s62 with dissolve
        show s114_r2 with Dissolve(1.0)
        sensation "Sapphire begins bobbing her head faster, wet sucking sounds becoming harder to hide."
        mc "F-Fuck! I mean, f-fantastic!"
    else:
        scene 114_s62 with dissolve
        mc "Don't worry about it."
    call screen scene114_choice12 with dissolve

label scene114_choice12_op4:
    $ sarah_q4 = True
    if mc_hired_ruby_after_bj:
        scene 114_s62 with dissolve
        mc "How do you feel about getting a deepthroat?"
        scene 114_s61 with dissolve
        sarah "...Sorry?"
        scene 114_s62 with dissolve
        if mc_remain_brothel:
            mc "Oh! I-I meant how do you feel about working in a brothel?"
            scene 114_s61 with dissolve
            sarah "As long as I'm treated fairly, I'm willing to adapt, sir."
        else:
            mc "Oh! I-I meant how do you feel about working in a tavern that used to be a brothel?"
            mc "Some men will confuse this place for a while. You might get harassed every now and then."
            scene 114_s61 with dissolve
            sarah "I'm sort of used to it. Unfortunetly, some men will harass you regardless of where you work."
        show s114_r3 with Dissolve(1.0)
        sensation "Sapphire pushes herself to the limit, deepthroating you fully while humming softly around your cock."
        show s114_r2 with Dissolve(1.0)
    else:
        if mc_remain_brothel:
            mc "How do you feel about working in a brothel?"
            scene 114_s61 with dissolve
            sarah "As long as I'm treated fairly, I'm willing to adapt, sir."
        else:
            mc "How do you feel about working in a tavern that used to be a brothel?"
            mc "Some men will confuse this place for a while. You might get harassed every now and then."
            scene 114_s61 with dissolve
            sarah "I'm sort of used to it. Unfortunetly, some men will harass you regardless of where you work."
        scene 114_s62 with dissolve
    call screen scene114_choice12 with dissolve
    

label scene114_bj1:
    scene black with Dissolve(0.3)
    show s114_r1 with dissolve
    sensation "She slows down, savoring every moment as she tastes and teases your glans. You feel like letting go every time her tongue glides over your frenulum."
    mc "(Ahhnn... she's gonna make me cum if she keeps this up.)"
    sapphire "{size=30}Mmm~ I love this part. So sensitive.{/size}"
    call screen scene114_choice12 with dissolve

label scene114_bj2:
    scene black with Dissolve(0.3)
    show s114_r2 with dissolve
    sensation "The soft heat of her mouth envelops you completely. Her tongue presses flat against the underside of your cock, stroking every inch as she slides up and down."
    mc "{size=30}Just like that... keep going.{/size}"
    call screen scene114_choice12 with dissolve

label scene114_bj3:
    scene black with Dissolve(0.3)
    show s114_r3 with dissolve
    sensation "Sapphire gags quietly as she pushes herself to the limit, taking you into the deepest part of her steaming hot throat. The pressure is intense."
    sapphire "*glk* Mmmfhnn..."
    mc "(God... she's trying to swallow my whole cock.)"
    call screen scene114_choice12 with dissolve
    
label scene114_choice12_op5:
    if mc_hired_ruby_after_bj:
        mc "Ahhhn!!"
        scene 114_s61 with dissolve
        sarah "Maybe we should conduct this interview another time, sir? You seem... unwell."
        scene 114_s62 with dissolve
        mc "NO! I'm done! I-I'm finished!"
        show s114_r2 with Dissolve(1.0)
        sarah "W-What?"
        mc "I'm finished! It's over!"
        play sound "se_sfx/blowjob/blowjob_cum2.mp3" 
        scene 114_s77 with vpunch
        sensation "You can't hold back any longer. Thick ropes of cum erupt down Sapphire's throat as she tries to swallow the ceaseless stream coming from your urethra."
        mc "Aghnng!"
        play sound "se_sfx/blowjob/blowjob_cum5.mp3" 
        scene 114_s78 with vpunch
        mc "Gahh!"
        sapphire "Mfhnn~!"
        sarah "Sir?!"
        play sound "se_sfx/blowjob/blowjob5.mp3" 
        scene 114_s79 with Dissolve(1.0)
        sapphire "{size=30}Blergh... Disgusting! I couldn't swallow it all so some of it got into my nose...{/size}"
        mc "Hahh..."
        scene 114_s62 with Dissolve(1.0)
        mc "This was easily the most exciting interview I've ever conducted."
        scene 114_s60 with dissolve
        sarah "Oh! Well... thank you!"
        $ renpy.end_replay()
    else:
        mc "I've heard enough."
        if not (sarah_q1 and sarah_q2 and sarah_q3 and sarah_q4):
            scene 114_s61 with dissolve
            sarah "I think there might be a mistake, sir. You didn't even ask me a single question..."
            scene 114_s62 with dissolve
            mc "I can read people by their looks and mannerisms."
            scene 114_s61 with dissolve
            sarah "Got it..."
            scene 114_s60 with dissolve    
            sarah "*ahem* So, what did you think, sir?"
        else:
            scene 114_s60 with dissolve    
            sarah "What did you think, sir?"

    sarah "Can I expect a response sometime this week?"
    scene 114_s59 with dissolve
    mc "Actually... we're a little short on employees."
    mc "You might need to start today."
    scene 114_s62 with dissolve
    sarah "..."
    empathy "Her expression darkens. She knows exactly what that means."
    scene 114_s61 with dissolve
    sarah "I... see."
    scene 114_s62 with dissolve
    call screen scene114_choice13 with dissolve
    
label scene114_choice13_op1:
    $ mc_hired_sarah = True
    mc "You're hired."
    mc "Welcome to the team, Sarah."
    scene 114_s63 with dissolve
    sarah "Thank you so much, sir! I won't let you down."
    if mc_hired_ruby_after_bj:
        scene 114_s64 with Fade(1.3,0.5,0.5)
        perception "As Sarah leaves the room, Sapphire crawls out from under the desk, cleaning her lips."
        sapphire "*cough* You hired the goody-two-shoes? I almost fell asleep listening to her."
        scene 114_s65 with Dissolve(1.0)
        mc "You made my eyes roll back, Sapphire."
        mc "I swear I thought she would notice at times."
        scene 114_s66 with dissolve
        sapphire "*chuckles* Next time you interview someone, I'm sitting on your lap. No more hiding under the desk."
        sapphire "That way, you can make it clear that you're the man in charge here."
        sapphire "And if you ever decide to corrupt that innocent girl by filling her throat too... Make sure to invite me~"
        scene 114_s65 with dissolve
    jump scene114_9

label scene114_choice13_op2:
    mc "I'm sorry, but... you're dismissed."
    scene 114_s61 with dissolve
    sarah "I... I understand. Thank you for your time."
    sarah "May I please know what was the reason for my refusal?"
    scene 114_s62 with dissolve
    mc "Ah... well. You did good, but I'm just not interested."
    scene 114_s61 with dissolve
    sarah "I see..."
    if mc_hired_ruby_after_bj:
        scene 114_s64 with Fade(1.3,0.5,0.5)
        perception "As Sarah leaves the room, Sapphire crawls out from under the desk, licking her lips with a satisfied smirk."
        sapphire "Good choice. I almost fell asleep listening to her."
        scene 114_s66 with Dissolve(1.0)
        sapphire "But next time you interview someone, I'm sitting on your lap. No more hiding under the desk."
        sapphire "That way, you can make it clear that you're the man in charge here."
        scene 114_s65 with dissolve
    else:
        scene 114_s62 with dissolve
    jump scene114_9

label scene114_9:
    stop music fadeout 1.0 
    scene 114_s68 with Fade(1.5,1.0,1.3)
    play music "diana.mp3" fadein 1.0 loop
    ""
    if mc_hired_sarah and mc_hired_ruby:
        scene 114_s69 with Dissolve(1.5)
        di "You hired {i}both{/i} girls?"
        di "Oh, such a relief... Sarah can handle the inventory and tables. She's obviously qualified, maybe overqualified."
        di "Sapphire can handle the troublemakers and the... the troublemakers."
        di "Honestly, no idea what I should assign that girl."
        scene 114_s70 with dissolve
        mc "Go easy on her. She went through a lot."
        scene 114_s69 with dissolve
        di "As you wish."
        scene 114_s70 with dissolve
        mc "Be a good manager, you hear?"
        scene 114_s69 with dissolve
        di "I will. The best manager this establishment has ever seen. Vera who? *giggles* Never heard of her."
        di "Thank you, [mc]. For giving me something to live for. For being there for me."
        scene 114_s70 with dissolve
        mc "*chuckles* No problem. Take care of the place while I'm gone."
        scene 114_s69 with dissolve
        if diana_pregnant:
            di "And you take care of yourself, darling. Our baby will need daddy alive and well."
        else:
            di "And you take care of yourself, darling."
        di "By the time you return, you'll find this place... let's just say, different."
        scene 114_s70 with dissolve
        mc "Should I be concered?"
        scene 114_s69 with dissolve
        di "Not at all! Now go! [brothel_name] will be here when you get back."

    elif mc_hired_ruby:
        scene 114_s69 with Dissolve(1.5)
        di "How did it go?"
        scene 114_s70 with dissolve
        mc "I hired Sapphire. Sarah's too expensive, and honestly... I think this place needs someone who can handle trouble."
        scene 114_s71 with dissolve
        di "{i}Her?!{/i} She looks more like a bodyguard than a maiden, but I'll trust your judgment."
        scene 114_s72 with dissolve
        mc "Then it's settled. I'm trusting you to keep her in line."
        mc "Be a good manager, you hear?"
        scene 114_s69 with dissolve
        di "I will. The best manager this establishment has ever seen. Vera who? *giggles* Never heard of her."
        di "Thank you, [mc]. For giving me something to live for. For being there for me."
        scene 114_s70 with dissolve
        mc "Take care of the place while I'm gone."
        scene 114_s69 with dissolve
        if diana_pregnant:
            di "And you take care of yourself, darling. Our baby will need daddy alive and well."
        else:
            di "And you take care of yourself, darling."
        di "By the time you return, you'll find this place... let's just say, different."
        scene 114_s70 with dissolve
        mc "*chuckles* Sounds good."
        scene 114_s69 with dissolve
        di "Now go! [brothel_name] will be here when you get back."

    elif mc_hired_sarah:
        scene 114_s69 with Dissolve(1.5)
        di "How did it go?"
        scene 114_s70 with dissolve
        mc "I hired Sarah. She's professional, experienced, and she actually knows how to talk."
        scene 114_s69 with dissolve
        di "I agree. She seemed so competent compared to that... 'girl'."
        di "*sigh* Finally, someone to share the burden."
        scene 114_s70 with dissolve
        mc "Be a good manager, you hear?"
        scene 114_s69 with dissolve
        di "I will. The best manager this establishment has ever seen. Vera who? *giggles* Never heard of her."
        di "Thank you, [mc]. For giving me something to live for. For being there for me."
        scene 114_s70 with dissolve
        mc "Take care of the place while I'm gone."
        scene 114_s69 with dissolve
        if diana_pregnant:
            di "And you take care of yourself, darling. Our baby will need daddy alive and well."
        else:
            di "And you take care of yourself, darling."
        di "By the time you return, you'll find this place... let's just say, different."
        scene 114_s70 with dissolve
        mc "*chuckles* Sounds good."
        scene 114_s69 with dissolve
        di "Now go! [brothel_name] will be here when you get back."

    else:
        scene 114_s71 with Dissolve(1.5)
        di "Umm, [mc]? You didn't hire either of them."
        scene 114_s72 with dissolve
        mc "I know. Neither of them stood out to me. Sapphire's too... aggressive, and Sarah's too expensive. We can find better."
        scene 114_s71 with dissolve
        di "I see..."
        scene 114_s72 with dissolve
        mc "I'll have to go now, Diana. I'll trust this place to you. Next time I'm back, I'll have more time to review other candidates."
        scene 114_s71 with dissolve
        di "Would've liked some help with the day shift... but fine. I'll take care of it for now. Maybe I can order the other girls to help me out."
        scene 114_s72 with dissolve
        mc "Be a good manager, you hear?"
        scene 114_s69 with dissolve
        di "I will. The best manager this establishment has ever seen. Vera who? *giggles* Never heard of her."
        di "Thank you, [mc]. For giving me something to live for. For being there for me."
        scene 114_s70 with dissolve
        mc "Take care of the place while I'm gone."
        scene 114_s69 with dissolve
        if diana_pregnant:
            di "And you take care of yourself, darling. Our baby will need daddy alive and well."
        else:
            di "And you take care of yourself, darling."
        di "By the time you return, you'll find this place... let's just say, different."
        scene 114_s70 with dissolve
        mc "*chuckles* Sounds good."
        scene 114_s69 with dissolve
        di "Now go! [brothel_name] will be here when you get back."
    scene 114_s70 with dissolve
    call screen scene114_choice14 with dissolve
    
label scene115_0:
    if mc_bought_brothel:
        if mc_killed_lena:
            mc "(Lena is dead... I can't face Serena after that. Never.)"
        else:
            mc "(I doubt Lena would be happy to see me after going against her.)"
        call screen scene114_choice14 with dissolve
    else:
        if mc_killed_lena:
            mc "(Lena is dead... I can't face Serena after that. Never.)"
        else:
            mc "(I doubt Lena would be happy to see me after going against her.)"
        call screen scene113_choice02 with dissolve

label scene115:
    stop music fadeout 1.0 
    $ mc_went_stables = True
    scene 115_s1 with Fade(1.5,1.0,1.5)
    play music "night.mp3" fadein 1.0 volume 0.5 loop
    ""
    scene 115_s2 with Dissolve(1.3)
    mc "(Where are they?)"
    scene 115_s3 with Dissolve(1.0)
    selene "[mc]! Up here!"
    scene 115_s4 with dissolve
    mc "Uh, Serena. Be careful, you're too close to the edge."
    scene 115_s5 with dissolve
    mc "Holy shit! Serena, w-wait! Not from the top platform!"
    scene 115_s6 with Dissolve(0.3)
    play sound "sound_effects/body/body_falling3.mp3"
    scene 115_s6 with vpunch
    perception "She launches herself from the platform above with reckless abandon like a cannonball. Her full weight crashes into you."
    scene 115_s8 with Dissolve(0.3)
    play sound "sound_effects/body/body_falling_mud.mp3"
    scene 115_s8 with vpunch
    stop sound fadeout 0.5
    mc "Ghng! Serena... h-hey."
    scene 115_s7 with dissolve
    selene "Ya did it! Mom told me everything! Well, not everything everything, but the important parts!"
    scene 115_s8 with dissolve
    mc "I see you're already over the moon about it."
    scene 115_s7 with dissolve
    selene "I can go anywhere now! I can visit the market like I used to, buy those little honey cakes from the stall with the—"
    selene "Ah, wait. Market's no more."
    selene "Well, I can go anywhere! Everywhere that isn't burned down! The whole city is mine!"
    scene 115_s8 with dissolve
    mc "*chuckles* Good for you."
    scene 115_s7 with dissolve
    selene "Mom told me you solved the problem peacefully. Is that right, [mc]? Don't get me wrong... I'm not sayin' I don't trust mother. But..."
    scene 115_s39 with dissolve
    if mc_convince_lena:
        scene 115_s9 with Dissolve(1.0)
        mc "Your mother's right. No one was hurt. Or at least... not too much."
        selene "Phew! My freedom won't mean much if it's covered in blood."
        selene "Anyway. Mom's up there, She's been waiting on ya. Said she wanted to talk to you before you went off."
        jump scene115_2
    else:
        call screen scene115_choice01 with dissolve

label scene115_choice01_op1:
    $ mc_told_serena_truth = True
    scene 115_s10 with Dissolve(1.0)
    mc "Serena... your mother didn't tell you everything."
    scene 115_s11 with dissolve
    selene "What do you mean?"
    scene 115_s10 with dissolve
    mc "The man who owned your deed. Gheris. He's dead. And his daughter too."
    mc "Your mother killed them."
    scene 115_s11 with dissolve
    selene "You're lyin'."
    scene 115_s10 with dissolve
    mc "I'm not. I'm sorry."
    scene 115_s11 with dissolve
    selene "No. No, she wouldn't... she promised me! She promised she'd do it clean! She said no one had to die!"
    selene "Why? Why didn't you stop her?"
    scene 115_s10 with dissolve
    mc "..."
    jump scene115_2

label scene115_choice01_op2:
    scene 115_s9 with Dissolve(1.0)
    mc "Your mother's right. Everything went peacefully. The deed was revoked, and we walked away. No one got hurt."
    selene "*sigh* That's... that's real good. My freedom wouldn't mean much if it's covered in blood."
    selene "Anyway. Mom's up there, She's been waiting on ya. Said she wanted to talk to you before you went off."
    jump scene115_2

label scene115_2:
    if mc_told_serena_truth:
        scene 115_s12 with Fade(1.0,1.0,1.0)
        lena "Serena? What's with that expression?"
        selene "We need to talk! {i}Now{/i}!"
        scene 115_s13 with Dissolve(1.0)
        lena "What's up with you? Shouldn't you be frolicking outside right now, girl? I thought you were too happy to stand still."
        scene 115_s14 with dissolve
        selene "[mc] told me the truth! You... you killed them! The man AND his daughter! You're a murderer! A monster!"
        scene 115_s13 with dissolve
        lena "What?! N-No... I—"
        scene 115_s14 with dissolve
        selene "I don't want to hear it! Go away! I don't want to ever see you again!"
        selene "You promised! You PROMISED you'd do it clean! You're not my mother! My mother wouldn't..."
        scene 115_s15 with Dissolve(1.0)
        lena "Serena!"
        scene 115_s16 with Dissolve(1.0)
        lena "For fuck's sake, [mc]! Why did you tell her?!"
        scene 115_s17 with dissolve
        mc "She deserved to know the truth."
        scene 115_s16 with dissolve
        lena "The truth? You realize just how fragile our relationship is? I've been gone for years! And finally, I get her back and here you come, spouting things about how her mother is a killer?!"
        scene 115_s17 with dissolve
        mc "I—"
        scene 115_s16 with dissolve
        lena "I was about to... never mind."
        lena "*sigh* I guess it's for the best that she forgets me. I never should've come here after I killed them anyway."
        lena "I'll bring her to the temple. The Sisters will take her. They're good people—better than me. And then I... will forget about her too."
        scene 115_s17 with dissolve
        mc "Really? You're leaving her again? After everything you did to get her back?"
        scene 115_s16 with dissolve
        lena "You don't understand. None of this would've happened if I'd been there from the beginning. I deserve it all."
        lena "Goodbye, [mc]. Thank you for helping me. You'll find a carriage at the back of the stables with some supplies already in it. Take it."
        scene 115_s17 with dissolve
        scene 115_s18 with Fade(1.5,1.3,1.3)
        play sound "sound_effects/horse/horse_walk.mp3"
        perception "Serena puts up a fight, but eventually gives in and gets up on her mother's horse. They set off, presumably to that temple Lena talked about."
        mc "(I ought to get back to the hideout.)"
        jump scene116
    else:
        scene 115_s12 with Fade(1.0,1.0,1.0)
        mc "Lena?"
        lena "There you are."
        mc "Something wrong?"
        lena "Not at all. I was hoping you'd come visit before you set off."
        scene 115_s13 with Dissolve(1.0)
        lena "Dear? Would you give us some privacy?"
        scene 115_s14 with dissolve
        selene "Alright. I'll be outside with [mc]'s horse. We haven't talked in a while."
        selene "But don't take too long! It's cold out there."
        scene 115_s19 with Dissolve(1.0)
        lena "That girl and animals. She'd rather talk to a horse than most people. Can't say I blame her."
        lena "Thank you, [mc]. For helping me. I doubt I could've done it without you."
        lena "Well... I could've, but I appreciate it nonetheless."
        if mc_convince_lena:
            scene 115_s16 with dissolve
            lena "And thank you for... stopping me."
            lena "I was so close. So close to becoming exactly what I've spent my whole life hating."
            lena "Who knows what I could've become if you didn't. Not a mother that's for sure. Not someone Serena could look at without fear."
            scene 115_s20 with dissolve
            mc "You would've found your way back. You're stronger than you think."
            scene 115_s19 with dissolve
            lena "Maybe. But I'm glad I didn't have to find out. That's all."
        else:
            scene 115_s16 with dissolve
            lena "Yet I feel a little terrible after what I did. Their scared faces... her face. The girl."
            lena "We live long lives, some would say too long. But I doubt something like that would ever be forgotten with time."
            scene 115_s17 with dissolve
            mc "You did what you had to do."
            scene 115_s16 with dissolve
            lena "Right. It doesn't matter now, what's done is done. I have to live with it weather I like it or not."

        scene 115_s21 with Dissolve(1.0)
        lena "Fuck... I can't get it out of my head. I thought a peaceful walk in the woods would calm me down, but the adrenaline is still pumping hard."
        scene 115_s22 with dissolve
        mc "*chuckles* Maybe you can go for a walk with Serena—"
        scene 115_s23 with dissolve
        lena "Shut up."
        mc "..."
        scene 115_s25 with Dissolve(1.0)
        perception "She turns to you with a fierce, hungry look in her eyes."
        scene 115_s24 with dissolve
        lena "I don't want a walk. I want something that'll tire me out until I can't even stand."
        scene 115_s25 with dissolve
        mc "What exactly are you proposing?"
        scene 115_s24 with dissolve
        lena "I want to ride you like a fucking horse. Right now."
        scene 115_s25 with dissolve
        mc "...S-Sorry?"
        scene 115_s24 with dissolve
        lena "You heard me. Off with your pants, boy."
        scene 115_s25 with dissolve
        mc "Lena, are you sure about this? Serena is just outside..."
        scene 115_s24 with dissolve
        lena "*chuckles* She's got big ears, but when she's focused on something, she's deaf as a temple bell to the blind. We'll be fine."
        lena "You're after my daughter, aren't you? Who could blame you... She inherited these tits from me, after all."
        lena "But before you even think about putting your hands on her... you're going to pass a little test from her mother."
        lena "Let me see if you're really worthy of her."
        scene 115_s25 with dissolve
        call screen scene115_choice02 with dissolve

image s115_tj1 = Movie(play="images/chapter5/scene115/s115_tj1.webm", loop=True)
image s115_tj2 = Movie(play="images/chapter5/scene115/s115_tj2.webm", loop=True)

image s115_vsex1 = Movie(play="images/chapter5/scene115/s115_vsex1.webm", loop=True)
image s115_vsex2 = Movie(play="images/chapter5/scene115/s115_vsex2.webm", loop=True)

image s115_asex1 = Movie(play="images/chapter5/scene115/s115_asex1.webm", loop=True)
image s115_asex2 = Movie(play="images/chapter5/scene115/s115_asex2.webm", loop=True)

default scene115_sex_tj_first = True
default scene115_sex_tj_second = False

default scene115_sex_tj = False
default scene115_sex_cow = False
default scene115_sex_lay = False
label scene115_choice02_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_3_replay:
        $ persistent.chapter5_p7_3_replay = True
    $ mc_sexd_lena = True
    stop music fadeout 1.0 
    perception "You quickly undo your belt and drop your pants. Your cock springs free, already hard from her lewd expression."
    scene 115_s24 with dissolve
    lena "Good boy. That's what I like to see."
    lena "Now lie down on that hay bale. I'll rub some lotion and spit on me so you don't get chafed."
    scene 115_s25 with dissolve
    scene 115_s40 with Fade(1.0,1.0,1.0)
    lena "Mmm... Look at it, soo big and hard."
    scene 115_s41 with dissolve
    mc "I can't look away from your massive breasts. Ever since I saw you, I wanted to know how they felt."
    scene 115_s40 with dissolve
    lena "Who wouldn't? But unlike other losers on the streets who can only look, you're getting a first hand experiance~"
    jump scene115_sex_tj

label scene115_sex_tj:
    $ scene115_sex_tj = True
    $ scene115_sex_lay = False
    $ scene115_sex_cow = False

    if scene115_sex_tj_first:
        $ s115_after_tj = True

        $ scene115_sex_tj_first = False
        $ scene115_sex_tj_second = True
        lena "My tits should be more than enough to make you spill your load. Let's see how long you can last between them."
        play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
        scene 115_s42 with Dissolve(1.0)
        perception "She leans forward and slides your throbbing cock into the warm, soft embrace of her cleavage. The pressure is incredible."
        show s115_tj1 with dissolve
        lena "There we go... Feel that? Nice and snug, isn't it?"
        perception "She begins to move her upper body up and down in a slow, deliberate rhythm, stroking your cock between her massive breasts."
        lena "Mmm~ Look at you... already twitching so much. Does it feel good being smothered by a mother's tits?"
        mc "Ahnn... they're soo smooth. I feel like I'm inside of a pussy."
        lena "Are you really going to cum just from my tits? Tch. Tch. Hold it in, I want it inside me next."
        lena "That's it... fuck my tits. Show me how badly you want to fuck my daughter."
        mc "Fahhnn... S-Stop talking about her..."
        lena "You're getting close already, aren't you? I can feel you pulsing between them..."
        sensation "The fabric of her bra is slightly damp from the lotion, creating a slick, velvety tunnel around your shaft."
        lena "Go ahead, release your filthy seed! Mark my tits!"
        mc "Gahh! I wanna fuck you first!"
        lena "*giggles* Good. That was a test."
        if maia_anal_sex > maia_pussy_sex:
            $ scene115_sex_a = True
            lena "Your face is screaming for my... ass?"
            lena "Why do I get the feeling that you want it in my ass first?"
            mc "Because I do!"
            lena "Fine~ You wanna to fuck my girl, huh? Wanna defile her virgin anus? Then you better learn how to handle a real woman first."
        else:
            lena "Your face is screaming for my cunt."
            $ scene115_sex_v = True
            lena "You wanna to fuck my girl, huh? Wanna put a baby in her virgin womb? Then you better learn how to handle a real woman first."
        jump scene115_sex_cow

    elif scene115_sex_tj_second:
        $ s115_after_tj = True
        $ scene115_sex_tj_second = False
        mc "Lena, I can't stop staring at your breasts..."
        lena "Who told you to stare at my breasts you pervert?!"
        lena "*chuckles* Just kidding. Come here~"
        scene black with Dissolve(0.3)
        show s115_tj2 with dissolve
        lena "Look at the mess you made~ Covered in my juices. How filthy."
        sensation "Your cock is enveloped again in her warm, pillowy flesh. The combination of the lotion and your mixed fluids creates an incredibly slick tunnel."
        mc "The friction is driving me insane..."
        lena "You're lucky, you know that? Not many humans ever get the privilege to mating with an elf."
        mc "W-What about goblins?"
        lena "{i}Goblins?!{/i} What kind of degenerate nonsense are you spouting, boy?"
        lena "A disgusting, filthy goblin would never even dream of touching a human, let alone an elf."
        lena "Enough about goblins. Now focus on my tits~"
    else:
        $ s115_after_tj = True
        scene black with Dissolve(0.3)
        show s115_tj2 with dissolve
        perception "She spits directly onto your cock, using the extra lubrication to glide faster, her breasts jiggling heavily with every stroke."
        lena "Can't get enough of my large, slick tits~?"

    call screen scene115_sex with dissolve

default scene115_sex_cow_v_first = True
default scene115_sex_cow_a_first = True
default s115_after_tj = False

label scene115_sex_cow:
    $ scene115_sex_tj = False
    $ scene115_sex_cow = True
    $ scene115_sex_lay = False
    if scene115_sex_v:
        if scene115_sex_cow_v_first:
            $ lena_only_a = False
            $ scene115_sex_cow_v_first = False
            if s115_after_tj:
                $ s115_after_tj = False
                play sound "se_sfx/masturbate_female/1_masturbate.mp3"
                scene 115_s41 with Dissolve(1.0)
                perception "She releases your cock from her cleavage with a wet pop."
                scene 115_s40 with dissolve
                lena "I'm going to ride you now. And you're going to take every inch like a good boy."
                scene 115_s41 with dissolve
                scene 115_s43 with Fade(1.0,1.0,1.0)
                perception "You lie back on the wooden platform. Lena wastes no time stripping off her bottoms, revealing her glistening pussy."
                play sound "se_sfx/masturbate_female/3_masturbate3.mp3"
                scene 115_s44 with Dissolve(1.5)
                sensation "She reaches down, lines you up with her entrance, already dripping, and sinks down onto you in one smooth motion."
                show s115_vsex1 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s115_vsex1 with dissolve
            mc "Ahhn! Your so warm... and tight!"
            lena "Fuuuck... That's it. Stretch me out, boy."
            sensation "She immediately begins riding you with powerful, rhythmic bounces. Her pussy grips and massages your cock with rhythmic pulses, as if it has a will of its own."
            lena "Mmmh~! Yes~! I'm impressed you didn't let it out the second you entered me. Most humans lose control the moment they feel an elven pussy."
            mc "Ahhnn! Hahhnn!"
            sensation "Her inner walls ripple and squeeze around you in waves, sucking and milking your cock with every rise and fall of her hips."
            lena "That's right... feel how my insides are sucking on you. Elven pussies were made to drain cocks dry."
            lena "Impregnating an elf is hard so our insides evolved to suck out every drop of semen from our partners."
            mc "I can feel it! Ahhn! God!"
            lena "You're throbbing so pathetically inside me already. Drowning in ecstasy? How cute."
            lena "Resist the urge to breed me, little human. You'll never be able to fill an elf's womb if you ejaculate prematurely."
            mc "Ahnn! I'm trying!"
            lena "Now moan for me. Let me hear how much you love my cunt."
        else:
            scene black with Dissolve(0.3)
            show s115_vsex1 with dissolve
            lena "Ahhn~ Hmmmn~ You want me to do all the work~?"
            lena "Fine. I'll milk your cock dry~ You'll be spurting out everything stored up in your testicles once done I'm with you!"
    else:
        if scene115_sex_cow_a_first:
            $ lena_only_v = False
            $ scene115_sex_cow_a_first = False
            if s115_after_tj:
                $ s115_after_tj = False
                play sound "se_sfx/masturbate_female/1_masturbate.mp3"
                scene 115_s41 with Dissolve(1.0)
                perception "She releases your cock from her cleavage with a wet pop."
                scene 115_s40 with dissolve
                lena "I'm going to ride you now. And you're going to take every inch like a good boy."
                scene 115_s41 with dissolve
                scene 115_s43 with Fade(1.0,1.0,1.0)
                perception "You lie back on the wooden platform. Lena wastes no time stripping off her bottoms, revealing her glistening pussy."

            mc "Ahnnnm... I want you to ride me with your ass!"
            lena "You want to shove that big cock into my tight asshole? With pleasure~"
            scene 115_s47 with Dissolve(1.0)
            perception "With surprising eagerness, Lena aligns your cock with her puckered anus."
            mc "You want me to be gentl—?"
            play sound "se_sfx/sex/sex6.mp3" 
            scene 115_s45 with vpunch
            sensation "Without any warning, Lena drops down hard, forcing your entire length deep into her ass in one swift motion."
            show s115_asex1 with dissolve
            lena "Ahhnmmmm~! That's it! Stretch my ass!"
            sensation "She wastes no time, riding you with long, deep strokes, her ass clenching and massaging your cock with incredible control."
            lena "Mmmh~ You like that? You like fucking my asshole?"
            mc "Slow down, Lena! What if you hurt... aghnn... yourself?"
            lena "Hurt myself? Don't speak nonsense, boy, and sit still while I take in your cock~"
            sensation "Her anal walls ripple and pulse around you in ways no human could replicate, hot, silky, and greedily milking your shaft."
            lena "That's it~ Let my superior elven body ruin you for any human woman. You'll never be satisfied with anything less after this."
            mc "Hahhnn... Y-You're trying to make me stay for your daughter, aren't you?"
            lena "Maybe~ After all, you won't settle for less after I'm finished with you."
        else:
            $ s115_after_tj = False
            scene black with Dissolve(0.3)
            show s115_asex1 with dissolve
            lena "Fuaacckk my tight ass! Keep it hard for me~!"
            lena "Mfmmmmnn~ Gods! Tear my ass in half!"
    call screen scene115_sex with dissolve

default scene115_sex_cow_v2_first = True
default scene115_sex_cow_a2_first = True
default scene115_sex_v = False
default scene115_sex_a = False

label scene115_sex_cow_v:
    $ scene115_sex_v = True
    $ scene115_sex_a = False
    $ scene115_sex_tj = False
    scene black with Dissolve(0.3)
    show s115_vsex1 with dissolve

    $ lena_only_a = False
    $ s115_after_tj = False

    if scene115_sex_cow_v2_first: 
        $ scene115_sex_cow_v2_first = False
        $ lena_orgasm_v = True
        lena "GAHHNN~! No...!"
        mc "L-Lena? What's wrong?"
        lena "Impossible... A mere human cock cannot make me— AHHNHH!"
        play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
        scene 115_s48 with vpunch
        perception "She suddenly pulls herself off you. A powerful stream of clear liquid squirts out of her, splashing onto your legs and the wood below."
        scene 115_s49 with dissolve
        mc "*chuckles* Did you just cum?"
        lena "D-Don't be stupid. I just had to piss. Your weak human cock would never be enough to satisfy me..."
        mc "Get back on then. I'll show you~"
        show s115_vsex1 with dissolve
        lena "Ahhnn~"
        lena "Alright, fine! You did make me orgasm... But there's no way you can impregnate me. You'll have to bury yourself as deep as possible inside my womb if you want even a chance."
        mc "Ahhnn! Is that a challenge I hear?"
        lena "Don't get ahead of yourself, boy. An elf's womb is not so easily conquered."
    else: 
        lena "Can you feel it? How my insides are sucking on you?"
        lena "Don't hold back. Fuck me harder. Show me you're worthy of breeding an elf."
    call screen scene115_sex with dissolve
    
label scene115_sex_cow_a:
    $ scene115_sex_v = False
    $ scene115_sex_a = True
    $ scene115_sex_tj = False

    $ lena_only_v = False
    $ s115_after_tj = False
    
    if scene115_sex_cow_a_first:
        mc "Ahnnnm... I wanna fuck your ass!"
        lena "You want to shove that big cock into my tight asshole? With pleasure~"
        scene 115_s47 with Dissolve(1.0)
        perception "With surprising eagerness, Lena lifts herself up, pulls your cock out of her pussy, and aligns it with her puckered anus."
        scene 115_s45 with vpunch
        sensation "Without any warning, Lena drops down hard, forcing your entire length deep into her ass in one swift motion."
        show s115_asex1 with dissolve
        lena "Ahhnmmmm~! That's it! Stretch my fucking ass!"
        sensation "She wastes no time, riding you with long, deep strokes, her ass clenching and massaging your cock with incredible control."
        lena "Mmmh~ You like that? You like fucking my asshole?"
        mc "Slow down, Lena! What if you hurt... aghnn... yourself?"
        lena "Hurt myself? Don't speak nonsense, boy, and sit still while I take in your cock~"
        sensation "Her anal walls ripple and pulse around you in ways no human could replicate, hot, silky, and greedily milking your shaft."
        lena "That's it~ Let my superior elven body ruin you for any human woman. You'll never be satisfied with anything less after this."
        mc "Hahhnn... Y-You're trying to make me stay for your daughter, aren't you?"
        lena "Maybe~ After all, you won't settle for less after I'm finished with you."

    elif scene115_sex_cow_a2_first:
        $ scene115_sex_cow_a2_first = False
        lena "You want back into my ass already? How insatiable."
        scene black with Dissolve(0.3)
        show s115_asex1 with dissolve
        sensation "She forces herself back down hard, taking your entire length into her tight hole."
        mc "You're gripping me like you want me to cum in your ass!"
        lena "*chuckles* That's exactly where your seed belongs. Since you can't possibly impregnate me, you might as well finish somewhere else~"
        mc "Gahhnn... Keep grinding like that and I might just."
        sensation "The heat and clenching sensation is almost overwhelming. You feel your erect cock almost bending at times."
    else:
        scene black with Dissolve(0.3)
        show s115_asex1 with dissolve
        lena "Mhnnm~ Ahnngn~ Do it. Give it all to me, fill my intestines. Let my asshole leak your cum for days~!"
    call screen scene115_sex with dissolve

default scene115_sex_miss_first_v = True
default scene115_sex_miss_first_a = True
default scene115_sex_lay_first = True

label scene115_sex_lay:
    $ scene115_sex_tj = False
    $ scene115_sex_cow = False
    $ scene115_sex_lay = True
    $ s115_after_tj = False

    if scene115_sex_lay_first:
        $ scene115_sex_lay_first = False
        mc "Enough of you doing all the work. I wanna fuck you myself."
        scene 115_s46 with Fade(1.0,1.0,1.0)
        perception "She moves off you and lies down on her side on the hay bale, pressing her legs tightly together. She arches her back slightly, presenting her round ass and glistening holes to you."
        lena "Come here, boy. I want to feel you thrust into me properly."
    if scene115_sex_miss_first_v and scene115_sex_v:
        $ scene115_sex_miss_first_v = False
        $ lena_only_a = False
        play sound "se_sfx/sex/sex2.mp3" 
        scene 115_s60 with dissolve
        lena "Yes~! Show me what that human cock can do. Shove it deep."
        scene black with Dissolve(0.3)
        show s115_vsex2 with Dissolve(1.0)
        mc "Ahhhn... So tight!"
        lena "Ahhnn~! Good boy. That's it..."
        sensation "Her bumpy, slick walls massage and pull you deeper. The way her legs are pressed together makes her feel almost unbearably snug." 
        lena "Harder! Fuck me like you mean it!"
        mc "I am! F-Fahhn... Your pussy is gripping me so hard it's difficult to even pull back."
        lena "*laughs* Yes~! Just like that... Keep pounding my needy hole!"
        lena "Can you feel how my cunt is trying to milk you dry? Elves were made to ruin lesser human like yours."
    elif scene115_sex_miss_first_a and scene115_sex_a:
        $ lena_only_v = False
        $ scene115_sex_miss_first_a = False
        play sound "se_sfx/sex/sex3.mp3" 
        scene 115_s61 with dissolve
        lena "Ooof~! You really show no mercy..."
        scene black with Dissolve(0.3)
        show s115_asex2 with dissolve
        sensation "You press the swollen head of your cock against her tight, puckered entrance. Even after being fucked, her asshole still resists for a moment before slowly yielding."
        lena "Go on. Ruin my asshole."
        lena "*giggles* You're trying so hard to make me moan louder. How cute."
        mc "With how ridiculously tight you are... I thought you'd be screaming by now."
        sensation "You push forward, sinking inch after inch into the scorching heat of her ass. The silky, powerful grip is even stronger than her pussy, almost painfully tight."
        lena "Fghmmmh~! There we go... go deep and kiss my stomach~!"
        mc "Fuck... Lena!"
    else:
        if scene115_sex_v:
            scene black with Dissolve(0.3)
            show s115_vsex2 with dissolve
            lena "Yes~! Yes~! Fuck my tight cunt with your w-weak human cock!"
            mc "Can you really say that when your pussy is making such lewd noises?"
            lena "Mfhmmnn~ Nnmmmh~ S-Shut up!"
        else:
            scene black with Dissolve(0.3)
            show s115_asex2 with dissolve
            lena "You're really intent on my breaking my ass!"
            mc "I love seeing you whimper."
            lena "Hnnn~ Gods~ I can't keep my voice down if you keep thrusting like this~!"
    call screen scene115_sex with dissolve

label scene115_sex_lay_v:
    $ scene115_sex_v = True
    $ scene115_sex_a = False
    $ scene115_sex_tj = False
    scene black with Dissolve(0.3)
    show s115_vsex2 with dissolve

    $ lena_only_a = False
    $ s115_after_tj = False

    if scene115_sex_lay_v_first:
        $ scene115_sex_lay_v_first = False
        mc "Ahhhn—! Fuck...!"
        lena "Fuck, yes! Yes! That's the feeling I wanted."
        lena "My cunt is slowly taking on your shape, it wants you~"
        sensation "A strange fleshy sensation that feel almost intentional massages the underside of your cock with each thrust."
    else:
        lena "Ahhnn~ Yes~ Deeper~! Breed me~"
        mc "I'll do it! I'll make you a mother, Lena!"
        lena "As if! You... Ahnng~ can't~!"
    call screen scene115_sex with dissolve

default scene115_sex_lay_a_first = True
default scene115_sex_lay_v_first = True

label scene115_sex_lay_a:
    $ scene115_sex_v = False
    $ scene115_sex_a = True
    $ scene115_sex_tj = False

    $ lena_only_v = False
    $ s115_after_tj = False

    if scene115_sex_miss_first_a:
        $ scene115_sex_miss_first_a = False
        play sound "se_sfx/sex/sex3.mp3" 
        scene 115_s61 with dissolve
        lena "Ooof~! You really show no mercy..."
        show s115_asex2 with dissolve
        sensation "You press the swollen head of your cock against her tight, puckered entrance. Even after being fucked, her asshole still resists for a moment before slowly yielding."
        lena "Go on. Ruin my asshole."
        lena "*giggles* You're trying so hard to make me moan louder. How cute."
        mc "With how ridiculously tight you are... I thought you'd be screaming by now."
        sensation "You push forward, sinking inch after inch into the scorching heat of her ass. The silky, powerful grip is even stronger than her pussy, almost painfully tight."
        lena "Fghmmmh~! There we go... go deep and kiss my stomach~!"
        mc "Fuck... Lena!"

    elif scene115_sex_lay_a_first:
        scene black with Dissolve(0.3)
        show s115_asex2 with dissolve
        $ scene115_sex_lay_a_first = False
        $ lena_orgasm_a = True
        lena "Go on then. Slide back into my asshole."
        sensation "You shove your cock balls-deep into her incredibly tight ass. Her whole body convulses for a moment."
        mc "*chuckles* Your ass must be really sensitive for you to orgasm from it."
        lena "Ahhnngh~! Don't get bold! Y-You're not... you're not gonna make me orgasm from such a hole..."
    else:
        scene black with Dissolve(0.3)
        show s115_asex2 with dissolve
        lena "Start spilling already~! Pump your human seed deep into my ass. That's all it's good for anyway!"
        mc "Ahn! Fuck! You're crushing my dick!"
    call screen scene115_sex with dissolve

label scene115_sex_cum_0:
    call screen scene115_choice03 with dissolve

label scene115_sex_cum:
    if scene115_sex_v:
        if scene115_sex_cow or scene115_sex_tj:
            scene black with Dissolve(0.3)
            show s115_vsex2 with dissolve
        mc "Lena... I'm going to cum!"
        lena "Then do it! Cum inside me!"
        sensation "You feel her pussy clenching violently around you."
        lena "Yes~! Fill me! Pump your seed deep into my womb!"
        if persistent.xray_mode:
            play sound "se_sfx/sex/sex_cum6.mp3" 
            scene 115_s50_xray1 with vpunch
            mc "GHAHHH!"
            perception "You explode inside her, flooding her with thick, hot spurts of cum."
            scene 115_s51_xray2 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum4.mp3"
            scene 115_s51_xray2 with vpunch
            lena "Fuucckk~! I can feel it... so much warm seed flooding my womb..."
        else:
            play sound "se_sfx/sex/sex_cum6.mp3" 
            scene 115_s50 with vpunch
            mc "GHAHHH!"
            perception "You explode inside her, flooding her with thick, hot spurts of cum."
            scene 115_s51 with Dissolve(0.3)
            play sound "se_sfx/sex/sex_cum4.mp3"
            scene 115_s51 with vpunch
            lena "Fuucckk~! I can feel it... so much warm seed flooding me..."
        call pregnancy_check_lena from call_pregnancy_check_lena
        if lena_pregnant:
            perception "She suddenly freezes, eyes wide with genuine shock as she presses a hand to her lower belly."
            play sound "se_sfx/sex/sex_cum8.mp3" 
            if persistent.xray_mode:
                scene 115_s52_xray3 with Dissolve(1.0)
            else:
                scene 115_s52 with Dissolve(1.0)
            lena "Hahh... Annmmm... Fuck... I can feel it. My body is accepting it. You actually managed to knock me up!"
            lena "Impossible... At my age? After all these years... a {i}human{/i} got me pregnant?!"
            lena "I never thought this would happen again. Not at this stage of my life..."
            scene 115_s56 with Dissolve(1.0)
            lena "You idiot! You... you really put a child in me!"
            scene 115_s57 with dissolve
            mc "Shit... I seem to have a knack for doing that."
            scene 115_s56 with dissolve
            lena "Gugh! This is so fucked up!"
            lena "What the hell do I do now!?"
            $ renpy.end_replay()
            scene 115_s57 with dissolve
            call screen scene115_choice04 with dissolve
        else:
            lena "*giggles* My body is drinking it all in."
            play sound "se_sfx/sex/sex_cum8.mp3" 
            if persistent.xray_mode:
                scene 115_s52_xray3 with Dissolve(1.0)
            else:
                scene 115_s52 with Dissolve(1.0)
            lena "Don't get your hopes up. Impregnating an elf is no easy task. You'll have to fill me many more times before that happens."
            lena "But this was the only chance you'll get with me. Try harder for my daughter's sake."
    else:
        if scene115_sex_cow or scene115_sex_tj:
            scene black with Dissolve(0.3)
            show s115_asex2 with dissolve

        mc "I'm filling your whole colon!"
        lena "Fill my ass like the greedy boy you are!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene 115_s53 with vpunch
        sensation "Her anal walls suddenly clench down hard, squeezing and rippling around you with incredible force as she forces you over the edge."
        mc "GAHHNNN!"
        scene 115_s54 with Dissolve(0.3)
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene 115_s54 with vpunch
        sensation "You thrust up and explode, pumping thick ropes of cum deep into her tight elven ass."
        lena "Ahhnngh~! F-Fuck! I can feel you pulsing inside my asshole... So much hot seed!"
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 115_s55 with Dissolve(1.0)
        lena "Hahh... Good boy. Filling my ass like that... How depraved."
        lena "Mmm... Feel how my body is sucking it all deeper? Nothing is going to waste."

    mc "Hahh... hahhh..."
    scene 115_s58 with Dissolve(1.0)
    lena "Phew... That finally took the edge off."
    lena "Dress yourself, boy. Serena will start wondering why we've been gone so long. If she hasn't started already."
    scene 115_s59 with dissolve
    mc "Don't want a hug first? Or maybe a smoke?"
    scene 115_s58 with dissolve
    lena "You barely made me break a sweat. There's no need for all that."
    scene 115_s59 with dissolve
    mc "That's cheating. Your kind doesn't even sweat..."
    if lena_orgasm_a and lena_orgasm_v:
        mc "Besides, can you really say that after I made you cum with both that tight ass and your dripping pussy?"
        scene 115_s58 with dissolve
        lena "*giggles* What am I supposed to do when you keep switching between my holes like some possessed madman?"
    elif lena_orgasm_a:
        mc "Besides, can you really say that after I made you cum with that tight ass?"
        scene 115_s58 with dissolve
        lena "*giggles* You were lucky you found that spot through there... I'll give you that."
    elif lena_orgasm_v:
        mc "Besides, can you really say that after I made you cum with that dripping pussy?"
        scene 115_s58 with dissolve
        lena "*giggles* Shut up... Like I told you, I just really had to piss."

    if lena_only_a:
        scene 115_s56 with dissolve
        lena "Fuck me... I'm going to need crutches just to walk back to the temple. The sisters are going to stare for days."
        scene 115_s57 with dissolve
        mc "Why's that?"
        scene 115_s56 with dissolve
        lena "You're seriously asking? After the relentless assault you unleashed on my poor ass? You didn't even touch my cunt once!"
        scene 115_s57 with dissolve
        mc "Oh... right. I'm a man of very specific preferences."

        scene 115_s58 with dissolve
        lena "*chuckles* Now put that cock away before it starts twitching for another round. I can already see it stirring and my ass won't handle it this time."
    else:
        scene 115_s58 with dissolve
        lena "*chuckles* Now put that cock away before it starts twitching for another round. I can already see it stirring."

    lena "When you return... Serena will be ready for you. Make her a true woman, you hear me?"
    if mc_harem_serena:
        scene 115_s59 with dissolve
        mc "I will. Whatever that means."
    else:
        scene 115_s59 with dissolve
        mc "Actually... I don't really have those kinds of feelings for her."
        scene 115_s58 with dissolve
        lena "That so? Shame. Though perhaps it's for the best—you might not be able to handle a woman like her anyway."
        scene 115_s59 with dissolve
    $ renpy.end_replay()
    jump scene115_3

label scene115_choice04_op1:
    mc "I'll... I'll take responsibility. If it's really happening."
    scene 115_s56 with dissolve
    lena "Responsibility? And what exactly does that mean to you?"
    scene 115_s57 with dissolve
    mc "I'll take care of you and the child. When the time comes, I'll be there for you."
    lena "..."
    scene 115_s56 with dissolve
    lena "...You better mean that."
    lena "I won't raise a child alone. Not again."
    lena "You can dress up now. Serena will start wondering why we've been gone so long. If she hasn't started already."
    scene 115_s57 with dissolve
    jump scene115_3

label scene115_choice04_op2:
    mc "You should get rid of it."
    scene 115_s56 with dissolve
    lena "...Get rid of {i}it{/i}?"
    lena "You put it in me, and now you want me to deal with it alone? You spineless little shit."
    lena "*sigh* But... I suppose its the only way. I simply {i}cannot{/i} do this now."
    lena "Dress up. We're done here."
    scene 115_s57 with dissolve
    jump scene115_3

label scene115_sex_cum_no:
    if scene115_sex_v:
        mc "I wanna paint your ass!"
        sensation "Her pussy clenches around you with overwhelming strength, far too powerful for you to pull out without hurting yourself."
        mc "L-Lena?! What are you doing?!"
        lena "Inside. You're finishing inside me~"
        mc "Aghnnn!"
        lena "That's right. You don't get to choose where you finish. I do."
        lena "Fill me. Pump every last drop into my womb like a good boy. You're not allowed to waste it."
    else:
        mc "I wanna paint your ass!"
        sensation "Her ass clenches around you with overwhelming strength, far too powerful for you to pull out without hurting yourself."
        mc "L-Lena?! What are you doing?!"
        lena "Inside. You're finishing inside me~"
        mc "Aghnnn!"
        lena "That's right. You don't get to choose where you finish. I do."
        lena "Fill me. Pump every last drop into my colon like a good boy. You're not allowed to waste it."
    jump scene115_sex_cum

label scene115_choice02_op2:
    mc "Lena... we really shouldn't. Not here. Not with Serena right outside."
    scene 115_s26 with dissolve
    lena "Oh? Getting cold feet now?"
    lena "Tch. Fine. Run away then. But just know... if you can't even handle the mother, you sure as hell don't deserve the daughter."
    scene 115_s27 with dissolve
    jump scene115_3
    
label scene115_3:
    scene 115_s28 with Fade(1.3,1.0,1.3)
    ""
    play music "night.mp3" fadein 1.0 volume 0.7 loop
    if mc_sexd_lena:
        perception "You step out of the stables, adjusting your clothes. Serena is already waiting nearby."
        play sound "sound_effects/doors/door_close2.mp3"
        scene 115_s29 with Dissolve(1.0)
        selene "Ah, there you are! You two took quite a while. I heard some loud yelling in there."
        scene 115_s30 with Dissolve(1.0)
        selene "You look... really tired, Mom. Did ya run laps inside the stables or somethin'?"
        scene 115_s31 with dissolve
        lena "Don't worry about it, hon. [mc] was just showing me a few... tricks he learned. Combat techniques for the road."
        lena "He {i}trained{/i} me so hard that I feel sore now."
        scene 115_s30 with dissolve
        selene "Oh! What kind of tricks?"
        scene 115_s31 with dissolve
        lena "*giggles* You'll find out later."
        scene 115_s30 with dissolve
        selene "All right, then. Keep your secrets."
        scene 115_s31 with dissolve
        lena "Anyway, we'll be leaving now, Serena. We're heading to a much safer place."
        scene 115_s30 with dissolve
        selene "What?! B-But I want to stay here! Who's going to feed the pigs and chickens? They all trust me!"
        scene 115_s31 with dissolve
        lena "You don't even work here legally anymore, sweetheart. Besides, I'm sure there will be plenty of little critters to take care of where we're going."
        scene 115_s33 with Dissolve(1.0)
        selene "What about [mc]? Is he coming with us?"
        scene 115_s32 with dissolve
        mc "I'll see you soon, Serena. I won't be gone too long. Just have to take care of a few things first."
        scene 115_s33 with dissolve
        selene "Aww... I wanted to spend more time with you... You're way more fun than Mom."
        scene 115_s35 with dissolve
        lena "Move it, girl. You'll have time later."
        scene 115_s34 with dissolve
        mc "Hmph... Well, thank you, [mc]. I'll never forget this. Ever!"
        if mc_harem_serena:
            scene 115_s34 with vpunch
            selene "And... I-I love you!"
            scene 115_s36 with dissolve
            mc "Oh..."
            scene 115_s35 with dissolve
            lena "Aren't you coming on a bit strong, honey? You're older than [mc]. Start acting like it."
            scene 115_s36 with dissolve
            mc "Wait... what?"
            scene 115_s34 with dissolve
            selene "That doesn't matter! I want to marry [mc] and make lots of children! Lots and lots of them!"
            scene 115_s35 with dissolve
            lena "Straight to it, huh? No courtship, no chaperone, just... children. An entire legion."
            lena "Well, I'm sure he'd love {i}that{/i} part, but now's not the time. We have a long road ahead, and [mc] has even longer ones. Save it to when you two are settled."
            scene 115_s34 with dissolve
            selene "I know... Goodbye, [mc]! Thank you for helping me! And for making Mom sore and tired—she's fat and needed the exercise."
            scene 115_s35 with dissolve
            lena "You little...!"
            scene 115_s34 with dissolve
            selene "Don't forget me, alright?"
            scene 115_s32 with Dissolve(1.0)
            mc "I won't. It's hard to forget a cute elf like you."
            selene "Hehee~"
        else:
            scene 115_s34 with dissolve
            selene "Goodbye, [mc]! Thank you for helping me! And for making Mom sore and tired—she's fat and needed the exercise."
            scene 115_s35 with dissolve
            lena "You little...!"
            scene 115_s32 with Dissolve(1.0)
            mc "*chuckles* Take care, Serena. And you too, Lena."

    else:
        play sound "sound_effects/doors/door_close2.mp3"
        scene 115_s29 with Dissolve(1.0)
        selene "Ah there you were. That wasn't long."
        scene 115_s36 with Dissolve(1.0)
        mc "We just needed to talk for a bit."
        scene 115_s31 with dissolve
        lena "We'll be leaving now, Serena. We're heading to a much safer place."
        scene 115_s30 with dissolve
        selene "What?! B-But I want to stay here! Who's going to feed the pigs and chickens? They all trust me!"
        scene 115_s31 with dissolve
        lena "You don't even work here legally anymore, sweetheart. Besides, I'm sure there will be plenty of little critters to take care of where we're going."
        scene 115_s30 with dissolve
        selene "What about [mc]? Is he coming with us?"
        scene 115_s32 with Dissolve(1.0)
        mc "I'll see you soon, Serena. I won't be gone too long. Just have to take care of a few things first."
        scene 115_s33 with dissolve
        selene "Aww... I wanted to spend more time with you... You're way more fun than Mom."
        scene 115_s35 with dissolve
        lena "Move it, girl. You'll have time later."
        scene 115_s34 with dissolve
        selene "Hmph... Well, thank you, [mc]. I'll never forget this. Ever!"
        if mc_harem_serena:
            scene 115_s34 with vpunch
            selene "And... I-I love you!"
            scene 115_s36 with dissolve
            mc "Oh..."
            scene 115_s35 with dissolve
            lena "Aren't you coming on a bit strong, honey? You're older than [mc]. Start acting like it."
            scene 115_s36 with dissolve
            mc "Wait... what?"
            scene 115_s34 with dissolve
            selene "That doesn't matter! I want to marry [mc] and make lots of children! Lots and lots of them!"
            scene 115_s35 with dissolve
            lena "Straight to it, huh? No courtship, no chaperone, just... children. An entire legion."
            lena "Well, I'm sure he'd love {i}that{/i} part, but now's not the time. We have a long road ahead, and [mc] has even longer ones. Save it to when you two are settled."
            scene 115_s34 with dissolve
            selene "I know... Goodbye, [mc]! Thank you for helping me!"
            selene "Don't forget me, alright?"
            scene 115_s32 with Dissolve(1.0)
            mc "I won't. It's hard to forget a cute elf like you."
            selene "Hehee~"

        else:
            scene 115_s34 with dissolve
            selene "Goodbye, [mc]! Thank you for helping me!"
            scene 115_s32 with dissolve
            mc "*chuckles* Take care, Serena. And you too, Lena."

    if lena_pregnant:
        scene 115_s37 with Dissolve(1.0)
        lena "{size=30}Psst! [mc]... I'll keep the kid, so... be sure to come back, alright?{/size}"
        scene 115_s38 with dissolve
        mc "{size=30}I will.{/size}"
        scene 115_s37 with dissolve
        lena "*chuckles* {size=30}Good. Still can't believe this is actually happening...{/size}"

    scene 115_s18 with Dissolve(2.0)
    play sound "sound_effects/horse/horse_walk.mp3"
    mc "(I ought to return to the hideout.)"
    jump scene116

label scene116:
    if maia_pussy_sex > 0:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
    if maia_anal_sex > 0:
        $ maia_anus_virgin = False
        $ maia_virgin = False
    if maia_pregnant:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
        
    stop music fadeout 1.0 
    scene black with Dissolve(1.0)

    if not mc_went_stables and not mc_helped_jenny:
        perception "Before you return to the hideout, you meet with Lena who gives you a carriage for helping her."
    scene 116_s1 with Fade(1.4,1.0,1.3)
    if mc_princess_alex:
        mc "Hmm? These horses... they must be here."
        if maia_happy:
            scene 116_s2 with Dissolve(2.0)
            m "Welcome back, [mc]! I was starting to worry. Joan and Lewis are here to see you."
            scene 116_s3 with Dissolve(1.0)
        else:
            scene 116_s3 with Dissolve(2.0)

        play music "hope/the_plan.mp3" fadein 1.0 loop
        if mc_name_name:
            lewis "[mc], we need to talk. It's urgent."
        else:
            lewis "Sir, we need to talk. It's urgent."
        scene 116_s5 with dissolve
        mc "What's the news? Good or bad, I'll take either."
        scene 116_s3 with dissolve
        lewis "It's now or never. Tomorrow's night is as perfect as it can be. The coronation preparations have half the garrison running drills in the outer ward."
        lewis "If we're going to move, this is our window. We cannot waste it."
        scene 116_s5 with dissolve
        mc "Then we won't. What do we know?"
        scene 116_s3 with dissolve
        lewis "We learned where they're hiding the princess. She's in a cellar deep beneath the castle, it's an old storage place mainly used to store wine. Only a handful of guards know she's even there."
        scene 116_s5 with dissolve
        mc "A cellar..."
        scene 116_s4 with dissolve
        joan "That's not all. I was finally assigned guard duty specifically for the cellar's door. I've been pushing for it without raising too much suspicion."
        scene 116_s5 with dissolve
        mc "Good. That's good. What else?"
        scene 116_s4 with dissolve
        joan "The cellar is connected to an abandoned sewer system that runs through the entire castle district."
        joan "And we found a manhole south of the castle grounds, it should lead directly to that cellar."
        scene 116_s5 with dissolve
        mc "Good work, both of you. This is exactly what we needed. We can finally—"
        scene 116_s6 with Dissolve(1.0)
        alex "Hold on, [mc]... This is where the good news ends."
        scene 116_s5 with Dissolve(1.0)
        mc "Of course. What is it?"
        scene 116_s3 with dissolve
        lewis "We'll need a lot more help than we originally thought. Joan and I tried to sway some of the other guards. We found only three."
        scene 116_s4 with dissolve
        joan "Avery holds a very tight rope. Most of the castle guards aren't even Irdan anymore. They don't know the girl. They don't care."
        scene 116_s5 with dissolve
        mc "We don't need them. As long as we know where the princess is, we can pull this off. A quick dip in the sewer, in and out before anyone notices. Right?"
        scene 116_s4 with dissolve
        joan "If only..."
        scene 116_s3 with dissolve
        lewis "We... also learned that the sewer system is protected. Not by guards, but with a powerful chemical solution."
        lewis "Apparently, the vapors alone are strong enough to melt bones in minutes."
        scene 116_s5 with dissolve
        alex "*scoff* We're stopped by sewer stink. Apparently."
        scene 116_s4 with dissolve
        joan "We had hoped you might have ideas. Otherwise... Otherwise, it's over before it even started."
        scene 116_s7 with dissolve
        mc "Hmm... A chemical solution... Like a poison?"
        scene 116_s8 with dissolve
        lewis "Sure. Poison is one word for it. Another is 'we're completely fucked'."
        scene 116_s7 with dissolve
        mc "Could a poison resistance spell or potion work?"
        scene 116_s8 with dissolve
        lewis "I doubt there's a potion strong enough to make you immune that doesn't also melt your stomach when you drink it. A spell, however..."
        if mc_name_name:
            joan "Do you have someone who can cast something like that, [mc]? An exceptionally powerful sorcerer, mind you."
        else:
            joan "Do you have someone who can cast something like that, sir? An exceptionally powerful sorcerer, mind you."
        call screen scene116_choice01 with dissolve
    else:
        ""
        scene 116_s7 with Fade(0.5,0.5,0.5)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop        
        mc "Everyone, get ready. We'll be heading out first thing tomorrow morning."
        mc "Back up everything you need. We can't waste any second."
        scene 116_s8 with dissolve
        scene 116_s15 with Dissolve(1.0)
        reham "Yes. We should have already left, but better late than never."
        scene 116_s6 with Dissolve(1.0)
        alex "How will we travel? On horses? What about supplies?"
        scene 116_s16 with dissolve
        if mc_helped_lena:
            mc "Already taken care of. Lena, the woman I helped, promised to give me a wagon, and she's giving us supplies aswell."
        elif mc_helped_jenny:
            mc "Already taken care of. A noble has promised to provide us a wagon, and he's giving up supplies aswell."
        scene 116_s22 with Dissolve(1.0)
        m "The city... I... I'll miss it a lot."
        scene 116_s21 with dissolve
        mc "Everyone should get some rest. We need to be fully focused."
        stop music fadeout 1.0 
        scene 116_s24 with Fade(1.5,1.0,1.3)
        play music "nature.mp3" fadein 1.0 loop
        mc "Time to go."
        m "*yawn* But it's too early..."
        mc "Get up, Maia. There's plenty of time to sleep in the carriage."
        stop music fadeout 1.0 
        jump scene118

label scene116_choice01_op1_0:
    if not quest_witch_amelia_alive_free:
        if quest_witch_amelia_dead:
            mc "(Amelia is dead...)"
        else:
            mc "(Amelia is imprisoned...)"
    else:
        mc "(I haven't visited Amelia in a while. Even if I spend an entire day travelling there, I doubt she would agree to help after ignoring her for so long.)"
    call screen scene116_choice01 with dissolve

label scene116_choice01_op2_0:
    if mc_kill_ava:
        mc "(The elf is dead. I killed her.)"
    else:
        mc "(I left Ava while her house was burning down. Even if she was somehow alive, she wouldn't agree to help me.)"
    call screen scene116_choice01 with dissolve

label scene116_choice01_op1:
    $ mc_princess_amelia = True
    scene 116_s9 with Dissolve(1.0)
    mc "Amelia! I know you're hearing us! I need you!"
    if mc_harem_reham:
        reham "Master? Who are you calling to? There's no one out there."
    else:
        reham "[mc]? Who are you calling to? There's no one out there."
    scene 116_s10 with Dissolve(1.0)
    crow "So you noticed~? Caw~ Caw~ I was wondering how long you'd prattle on before remembering little old me."
    alex "Umm..."
    scene 116_s11 with Dissolve(1.0)
    mc "How long were you in that cup for?"
    mc "You know what? Forget it. I need your help, Amelia."
    scene 116_s12 with dissolve
    crow "And what will I get in return? I'm a busy woman, darling. You can't expect me to drop everything for free."
    scene 116_s11 with dissolve
    mc "You owe me. Remember? You couldn't pull off the spell to bind my arm. You said you'd make it up to me."
    scene 116_s12 with dissolve
    crow "CAW! No need to be so patronizing, darling. Yes, yes, I did promise to help you. But..."
    crow "I'm feeling a little... tired after I pulled off that teleportation spell. You have no idea how draining it is to fold space and time like that. I may need some convincing."
    scene 116_s11 with dissolve
    mc "I'll... I'll let you use me again if you do!"
    scene 116_s12 with dissolve
    crow "You're supposed to negotiate, not offer yourself up on a silver platter, sweatheart."
    scene 116_s11 with dissolve
    mc "Do we have a deal or not?"
    scene 116_s12 with dissolve
    if mc_wants_impregnate_amelia:
        crow "Very well~ I haven't forgotten you saying you want me pregnant. Such a bold request. We need to get on that once you're done playing hero~"
        scene 116_s11 with dissolve
        mc "R-Right... So, will you help us?"
        scene 116_s12 with dissolve
    else:
        crow "Deal! Deal! Caw!"
    crow "Caw! Caw! Caw! I shall follow you to that manhole and cast the spell on you. Don't keep me waiting. CAW!"
    scene 116_s3 with Dissolve(1.0)
    if mc_name_name:
        lewis "[mc]... with all due respect... what in the hells was that?"
    else:
        lewis "sir... with all due respect... what in the hells was that?"
    scene 116_s5 with dissolve
    if mc_harem_reham:
        reham "Yes, master. Since when do you have a talking crow friend?"
    else:
        reham "Yes, [mc]. Since when do you have a talking crow friend?"
    mc "I helped her a while back. She'll help us now."
    jump scene116_2

label scene116_choice01_op2:
    $ mc_princess_ava = True
    scene 116_s7 with dissolve
    mc "I need one of you to send a letter. To Ava."
    scene 116_s8 with dissolve
    if mc_name_name:
        lewis "[mc]... Ava is the royal examiner. She's the last person in the kingdom who would—"
    else:
        lewis "Sir... Ava is the royal examiner. She's the last person in the kingdom who would—"
    scene 116_s7 with dissolve
    mc "It's fine. I visited her. She's on board... I think."
    scene 116_s8 with dissolve
    joan "You visited the royal examiner... and she didn't burn a hole through you? We might actually have a chance."
    lewis "Very well. I'll send one of the guards we managed to convince."
    jump scene116_2
    
label scene116_choice01_op3:
    $ mc_princess_fail_early = True
    scene 116_s5 with Dissolve(1.0)
    mc "Shit... I have no one who can help."
    alex "We can't just surrender here! We've come too far! There has to be another way! We go in anyway, we hold our breath, we—"
    scene 116_s13 with Dissolve(1.0)
    reham "Did you not hear what they said? The poison is enough to melt bones. You would be there for only seconds before you fall."
    reham "And considering there's quite a walk before you reach the castle... You would die for nothing."
    scene 116_s14 with dissolve
    alex "Nghnn...! There has to be something! Anything!"
    scene 116_s17 with Dissolve(1.0)
    if mc_name_name:
        lewis "So, that's it, [mc]? This is where it ends?"
    else:
        lewis "So, that's it, sir? This is where it ends?"
    scene 116_s19 with dissolve
    mc "No. We'll save the princess. But through plan b now."
    mc "We'll set off to Nahraya at sunrise. We can still stop the execution if we convince their king."
    scene 116_s18 with dissolve
    joan "I hope you're quick enough."
    scene 116_s17 with dissolve
    if mc_name_name:
        lewis "Very well. I'm sorry we couldn't be more help, [mc]. We'll leave it up to you to save her. May the Gods be with you."
    else:
        lewis "Very well. I'm sorry we couldn't be more help, sir. We'll leave it up to you to save her. May the Gods be with you."
    scene 116_s18 with dissolve
    joan "May the Gods be with you."
    scene 116_s7 with Dissolve(1.0)
    mc "Everyone, get ready. We'll be heading out first thing tomorrow morning."
    mc "Back up everything you need. We can't waste any second."
    scene 116_s8 with dissolve
    scene 116_s15 with Dissolve(1.0)
    reham "Yes. We should have already left, but better late than never."
    scene 116_s6 with Dissolve(1.0)
    alex "How will we travel? On horses? What about supplies?"
    scene 116_s16 with dissolve
    if mc_helped_lena:
        mc "Already taken care of. Lena, the woman I helped, gave me a carriage, and she's giving us supplies aswell."
    elif mc_helped_jenny:
        mc "Already taken care of. A noble has provided us a carriage after I helped him, and he gave us supplies aswell."
    scene 116_s22 with Dissolve(1.0)
    m "The city... I... I'll miss it a lot."
    scene 116_s21 with dissolve
    mc "Everyone should get some rest. We need to be fully focused."
    scene 116_s24 with Fade(1.5,1.0,1.3)
    mc "Time to go."
    m "*yawn* But it's too early..."
    jump scene118

label scene116_2:
    scene 116_s19 with Dissolve(1.0)
    mc "What else is there?"
    scene 116_s17 with dissolve
    lewis "The poison itself isn't the only issue down there. The tunnels are also home to a colony of Sporehusks."
    scene 116_s19 with dissolve
    mc "...Sporehusks?"
    scene 116_s6 with dissolve
    alex "So they're the ones spreading the poison, huh? That figures. Those things thrive in toxic filth."
    scene 116_s16 with dissolve
    lewis "Exactly."
    mc "Wait a second. Back up. What the hell are Sporehusks?"
    scene 116_s6 with dissolve
    alex "It's a type of invasive species. They appear in sewers, or on battlefields, anywhere there's a lot of dead bodies left to rot."
    alex "They're fungal creatures. Part mushroom, part... I don't know, something else."
    alex "But they're usually dormant. If we can get through the poison, what's the issue? We just walk past them."
    scene 116_s17 with dissolve
    lewis "During the Zents invasion of Irda eighty years ago, so many people died that the city had no idea what to do with the bodies."
    lewis "Thousands of corpses, more every day. So they just... dumped them into the sewers. Stupid."
    lewis "The Sporehusks down there have been feeding on that rot for decades. They've grown... especially keen on living flesh."
    scene 116_s18 with dissolve
    joan "I hear they lay eggs inside the bodies. They keep them alive for as long as possible while doing that—paralyzed but conscious, feeling everything..."
    joan "Eugh... makes me shiver just thinking about it."
    scene 116_s19 with dissolve
    mc "So we need someone to take care of them."
    scene 116_s18 with dissolve
    joan "Yes. Someone who can hold their ground, keep the swarm occupied. Buy you time."
    joan "You have about one hour before my rotation starts. So we need to be quick, no fighting semi-immortal species."
    scene 116_s19 with dissolve
    mc "So we can't waste a single second..."
    scene 116_s18 with dissolve
    if mc_name_name:
        joan "Do you have someone, [mc]? Hopefully not a female. Just... just in case. The eggs. I wouldn't wish that on anyone."
    else:
        joan "Do you have someone, sir? Hopefully not a female. Just... just in case. The eggs. I wouldn't wish that on any woman."
    scene 116_s19 with dissolve
    call screen scene116_choice02 with dissolve

label scene116_choice02_op1:
    $ mc_princess_kat = True
    scene 116_s7 with Dissolve(1.0)
    mc "I need you to send a letter to Kathrine, a mercenary, she's living with Ava, the royal examiner."
    scene 116_s8 with dissolve
    if mc_princess_ava:
        lewis "So both Ava and Kathrine are helping us... Very well. The same guard as before—he'll complain, but he'll do it."
        scene 116_s4 with dissolve
        if mc_name_name:
            joan "Hold on, [mc]. Are you sure that Kathrine is the best fit for this? I heard she was out of it for a while."
        else:
            joan "Hold on, sir. Are you sure that Kathrine is the best fit for this? I heard she was out of it for a while."
        scene 116_s3 with dissolve
        lewis "Ah, she's right. Kathrine was imprisoned then quit the guild if I remember correctly. Might not be in the best shape after that."
    else:
        if mc_name_name:
            lewis "[mc]... Ava is the royal examiner. She's the last person in the kingdom who would—"
        else:
            lewis "sir... Ava is the royal examiner. She's the last person in the kingdom who would—"
        scene 116_s7 with dissolve
        mc "It's fine. I visited her. She's on board... I think."
        scene 116_s8 with dissolve
        joan "You visited the royal examiner... and she didn't burn a hole through you? We might actually have a chance recruting Kathrine then."
        lewis "I'll send one of the guards we managed to convince."
        scene 116_s4 with dissolve
        if mc_name_name:
            joan "Hold on, [mc]. Are you sure that Kathrine is the best fit for this? I heard she was out of it for a while."
        else:
            joan "Hold on, sir. Are you sure that Kathrine is the best fit for this? I heard she was out of it for a while."
        scene 116_s3 with dissolve
        lewis "Ah, she's right. Kathrine was imprisoned then quit the guild if I remember correctly. Might not be in the best shape after that."
    scene 116_s5 with dissolve
    call screen scene116_choice04 with dissolve
    mc "She's strong. It'll be fine."
    scene 116_s3 with dissolve
    lewis "Very well."
    jump scene116_3

label scene116_choice04_op1:
    $ mc_princess_kat_saved = True
    $ mc_princess_kat = False
    mc "You might be right. I'll pick another."
    call screen scene116_choice02 with dissolve
    
label scene116_choice02_op2:
    $ mc_princess_thulkin = True
    scene 116_s7 with Dissolve(1.0)
    mc "I need you to send a letter to Thulkin. A mercenary I know. He's most likely at the Adventurer's Guild."
    mc "Just look for a large man with the biggest axe and the loudest voice. You can't miss him."
    scene 116_s8 with dissolve
    if mc_name_name:
        lewis "Do you trust this person, [mc]? Mercenaries aren't exactly known for loyalty. They follow coin, not good causes."
    else:
        lewis "Do you trust this person, sir? Mercenaries aren't exactly known for loyalty. They follow coin, not good causes."
    scene 116_s7 with dissolve
    mc "I do. He's honorable {i}and{/i} pretty strong. Stronger than most."
    scene 116_s8 with dissolve
    lewis "Very well."
    jump scene116_3

label scene116_choice02_op3:
    $ mc_princess_mili = True
    scene 116_s7 with Dissolve(1.0)
    mc "I need you to send a letter to Millicent. A mercenary mage. She's most likely at the Adventurer's Guild."
    scene 116_s8 with dissolve
    if mc_name_name:
        lewis "A mage? Do you trust this person, [mc]? Magic users can be... unpredictable."
    else:
        lewis "A mage? Do you trust this person, sir? Magic users can be... unpredictable."
    scene 116_s7 with dissolve
    mc "I do. She's pretty strong and clever."
    scene 116_s8 with dissolve
    lewis "Very well."
    jump scene116_3
    
label scene116_choice02_op4:
    $ mc_princess_none = True
    scene 116_s7 with Dissolve(1.0)
    mc "We'll have to deal with them ourselves."
    scene 116_s8 with dissolve
    if mc_name_name:
        lewis "Is there no one who can help, [mc]?"
    else:
        lewis "Is there no one who can help, sir?"
    scene 116_s7 with dissolve
    mc "Afraid not..."
    scene 116_s8 with dissolve
    lewis "Then our time will be cut short becasue of this. We'll have to be quick."
    jump scene116_3

label scene116_3:
    scene 116_s4 with Dissolve(1.0)
    joan "The last thing you need is a getaway carriage. After pulling a stunt like that, the whole castle, no, the entire city will be on high alert."
    joan "You're going to need coin for this part. I know you have horses, but the princess... she's in a poor state, the last I laid eyes on her."
    scene 116_s3 with dissolve
    if mc_slap_avery:
        lewis "She's been in that cellar for weeks. Avery was really harsh on her for some reason. She was barely fed."
        lewis "You'll need lots of supplies if you want her to make it through the desert. Especially now that she's in a rough state."
    else:
        lewis "She's been in that cellar for weeks. You'll need lots of supplies if you want her to make it through the desert."
    scene 116_s4 with dissolve
    joan "Mhm. She'll need to lie down somewhere if she's to survive the journey. A carriage with blankets, medicine and food."
    scene 116_s5 with dissolve
    mc "I already have a carriage and some supplies. Hmm... but maybe it won't be enough if she's ill or malnourished."
    call screen scene116_choice03 with dissolve

label scene116_choice03_op1:
    $ mc_coin -= 100
    $ mc_princess_100 = True
    scene 116_s20 with Dissolve(1.0)
    mc "Here. Spend it all on supplies."
    lewis "A single gold coin...? That's not going to be nearly enough."
    mc "It's all I can afford right now."
    joan "*sigh* We'll have to pray that it's enough."
    jump scene116_4

label scene116_choice03_op2:
    if mc_coin >= 300:
        $ mc_coin -= 300
        $ mc_princess_300 = True
        scene 116_s20 with Dissolve(1.0)
        mc "Here. Spend it all on supplies."
        lewis "Three gold coins? That should about cover the whole journey."
        jump scene116_4
    else:
        mc "(I don't have that amount of coin...)"
        call screen scene116_choice03 with dissolve

label scene116_choice03_op3:
    if mc_coin >= 500:
        $ mc_coin -= 500
        $ mc_princess_500 = True
        scene 116_s20 with Dissolve(1.0)
        mc "Here. Spend it all on supplies."
        joan "Whoa, five gold coins?! That should definitely cover everything you need and them some."
        jump scene116_4
    else:
        mc "(I don't have that amount of coin...)"
        call screen scene116_choice03 with dissolve

label scene116_4:
    scene 116_s6 with Dissolve(1.0)
    alex "Is that it? Or do we also have to account for the rain? Maybe a stampede of gnolls?"
    scene 116_s16 with dissolve
    lewis "That's all. Here's the map of the castle district."
    scene 116_s17 with Dissolve(1.0)
    lewis "I need you to be on the red spot five minutes before midnight. Not a minute earlier, not a minute later."
    lewis "Joan's shift starts at midnight sharp. You must reach the princess before the shift change so Joan and I have enough time to get away."
    scene 116_s19 with dissolve
    mc "You'll run away?"
    scene 116_s17 with dissolve
    lewis "Obviously. We won't stick around to be questioned. We managed to find some connections. They will get us somewhere safe until you do your part."
    scene 116_s19 with dissolve
    mc "Got it. We'll be there."
    scene 116_s21 with Dissolve(1.0)
    mc "Maia and Reham. You two will come with us, you'll stay in the carriage. Not a single movement outside, no matter what. Understood?"
    reham "Understood."
    scene 116_s22 with dissolve
    m "The city... it's been so long. I... I missed it a lot."
    scene 116_s21 with dissolve
    mc "You two should return now."
    scene 116_s23 with Fade(0.5,0.5,0.5)
    joan "Oh man... I don't think I'll be able to sleep at all."
    if mc_name_name:
        lewis "[mc], I'll take your carriage east of the city walls, near the main gate."
    else:
        lewis "Sir, I'll take your carriage with me east of the city walls, near the main gate."
    lewis "Use it to get in the city. One of the guards I managed to convince will escort you inside. He's trustworthy."
    mc "I'll find it."
    if mc_name_name:
        lewis "Farewell, [mc]."
    else:
        lewis "Farewell, sir."
    scene 116_s13 with Dissolve(1.0)
    reham "I really hope you two know what you're walking into."
    reham "You have a plan set up, but rarely things go the way you want them to."
    scene 116_s14 with dissolve
    alex "I don't need your concern. You were against this from the start, but I'll show you we can make it happen."
    mc "Everyone should get some rest. We need to be fully focused."
    stop music fadeout 1.0 
    scene 116_s24 with Fade(1.3,1.0,1.2)
    play music "nature.mp3" fadein 1.0 loop
    mc "Time to go."
    m "*yawn* But it's too early..."
    mc "The city is far. If we leave now, we'll arrive right as night falls."
    stop music fadeout 1.0 
    scene 116_s25 with Fade(1.5,1.0,1.3)
    play music "night.mp3" fadein 1.0 loop
    mc "You're the guy?"
    scene 116_s27 with Dissolve(1.0)
    guard "An honor to meet you, sir. Lewis has told me about you... I actually used to serve in the castle with you."
    guard "*ahem* I'll hitch your horses to the wagon. Please, hop in. The others are already at the rendezvous point."
    scene 116_s26 with dissolve
    stop music fadeout 1.0 
    jump scene117

label scene117:
    scene 117_s1 with Fade(1.3,1.0,1.3)
    play music "thunder2.mp3" fadein 2.0 loop
    guard "There we are, sir. Please, save the princess."
    if mc_princess_ava:
        scene 117_s2 with Dissolve(1.0)
        perception "A single lantern illuminates the gathered party. You and Alex step off while Maia and Reham remain in the carriage."
        scene 117_s4 with Dissolve(1.0)
        ava "Do you have any idea how dangerous it is you're asking of me? This is treason, [mc]."
        ava "If this plan of yours fails, I don't just lose my position. I lose everything, and Kat loses everything, {i}again.{/i}"
        scene 117_s5 with dissolve
        mc "Please tell me you can actually cast the spell."
        scene 117_s4 with dissolve
        ava "It's not about the spell. It's about dragging me into this, [mc]."
        ava "I know you're trying to do something good here, but not to my detriment. Not to Kat's. We have a life. I was already kind enough to help you before."
        if mc_princess_kat:
            scene 117_s6 with Dissolve(1.0)
            kat "I'm here on my own free will. I promised [mc] to follow him anywhere he went."
            scene 117_s7 with dissolve
            ava "We talked about you staying SAFE!"
            scene 117_s6 with dissolve
            kat "Safe isn't why I became a mercenary. Safe isn't why we became one of the best parties in the guild... Let me do this, Ava."
        elif mc_princess_thulkin:
            scene 117_s9 with Dissolve(1.0)
            thulkin "Fret not, little elf! Our enemies will fall and your princess shall be free!"
        elif mc_princess_mili:
            scene 117_s8 with Dissolve(1.0)
            Millicent "Calm down, kin. This will only take a minute. Those Sporehusks won't stand a chance against my fire beam."
            Millicent "Honestly, I'm more worried about the smell."
        else:
            scene 117_s5 with dissolve
            mc "Come on, Ava. We need to be quick."
        scene 117_s4 with dissolve
        ava "*sigh* ...Let's get this over with so I can vanish as far away from here as possible."
        if mc_princess_kat:
            ava "You better make sure Kat is safe."

    else:
        scene 117_s3 with Dissolve(1.5)
        perception "A single lantern illuminates the gathered party. You and Alex step off while Maia and Reham remain in the carriage."
        perception "The crow perches on Lewis's shoulder, head cocked, black eyes glittering with intelligence that no bird should possess."
        scene 117_s10 with Dissolve(1.0)
        amelia "Caw! Caw!"
        mc "Can you cast the spell in this form? You're still a bird."
        amelia "Caw~ Mana flows all around. My power needs no human hand, to weave the spell that you demand~"
        if mc_princess_kat:
            scene 117_s6 with Dissolve(1.0)
            kat "Is our friend a druid in disguise? Or something else? I've never met a druid that rhymes. They're usually socially inept from all the reclusivity."
        elif mc_princess_thulkin:
            scene 117_s9 with Dissolve(1.0)
            thulkin "Is that a druid speaking? To take on any shape you want... surely there are better ones than a tiny bird."
        elif mc_princess_mili:
            scene 117_s8 with Dissolve(1.0)
            Millicent "Impressive magic at play here. Whoever is the original voice for this one is pretty far, yet still holds significant power."
            Millicent "Sustaining a familiar at this range... *chuckles* I have my work cut out for me."

    scene 117_s11 with Dissolve(1.0)
    lewis "Hold on. Before we begin! I want to make it absolutely clear that we must succeed."
    lewis "If we get caught... me and Joan are gone. Treason, conspiracy, aiding a fugitive... Yeah, we won't even get a trial."
    lewis "Not to mention that the princess will have her execution date pushed nearer, if not tomorrow."
    lewis "One hour! That's all we get once we enter the sewers."
    lewis "Thirty minutes to navigate the sewers and rescue the princess. Then another thirty for you to make it back while Joan and I run to our hideout."
    scene 117_s12 with dissolve
    if mc_princess_ava:
        mc "Can the spell last an hour, Ava?"
        scene 117_s11 with dissolve
        ava "Not a problem. But you shouldn't dally in there. The spell weakens with time."
        scene 117_s12 with dissolve
        mc "Then we won't fail."
    else:
        mc "Can the spell last an hour, Amelia?"
        scene 117_s11 with dissolve
        amelia "With ease~"
        scene 117_s12 with dissolve
        mc "Then we won't fail."
    scene 117_s11 with dissolve
    if mc_princess_kat:
        kat "Damn right!"
    elif mc_princess_thulkin:
        thulkin "Anyone who gets in our way will meet my axe!"
    elif mc_princess_mili:
        Millicent "I'll burn whoever stands in your way to ash."

    if mc_princess_ava:
        ava "Everyone, get close to each other. This won't hurt, but it will feel... strange. Like your skin is no longer your own."
        scene 117_s13 with Dissolve(1.0)
        perception "She raises her hand to her lips, then blows you a kiss... Actually, she just blows the air."
        ava "Great mother of earth and stone, harden their flesh to brittle bone."
        play sound "sound_effects/magic/magic_spell.mp3"
        scene 117_s14 with Dissolve(1.0)
        ava "It's done. [mc], I gave you potent protection so you can protect the princess too."
        ava "All you need to do is touch her for the spell to transfer to her body. Make sure it happens {i}before{/i} you return to the sewer."

    else:
        scene 117_s16 with Dissolve(1.0)
        amelia "Stick together and stand still, let magic bend to witch's will. CAW!"
        amelia "Great mother of earth and stone, harden their flesh to brittle bone!"
        play sound "sound_effects/magic/magic_spell.mp3"
        scene 117_s14 with Dissolve(1.0)
        amelia "You must touch her body for the spell to stick to her, [mc]. Caw!"
        play sound "sound_effects/wing_flap.mp3"
        scene 117_s17 with vpunch
        amelia "Farewell!"

    scene 117_s18 with Dissolve(1.5)
    lewis "I'll be your guide down there. The sewers are a maze. Without me, you'll be lost within seconds."
    lewis "Joan should be in her position right... about..."
    lewis "...Now!"
    stop music fadeout 1.0 
    scene black with Dissolve(1.0)
    play sound "sound_effects/manhole.mp3"
    perception "You lift the manhole and descend into the sewers. You wince as the smell assaults your nostrils instantly. Decay. Rot. And beneath it all, a faint hint of alcohol."
    mc "I can't see anything!"
    lewis "Hold on! The lantern turned off... it shouldn't have, I-I filled it myself."
    play sound "sound_effects/lantern.mp3"
    scene 117_s19 with Dissolve(1.4)
    stop sound
    lewis "Phew. There, we're all good."
    scene 117_s20 with Dissolve(1.0)
    play music "despair.mp3" fadein 3.0 loop
    perception "As the darkness recedes, the true horror of the sewers reveals itself. They are everywhere. Large, bulbous mushrooms cling to the floor, the walls, the ceiling."
    alex "Already here?! This city has a massive infestation!"
    if not mc_princess_none:
        mc "Get back, Alex. We got someone to fight for us."
    scene 117_s21 with Dissolve(1.0)
    lewis "Holy shit! I-I thought they'd be further in! The reports said the main colony was near the castle junction! T-They must have spread, they must have—"
    env "A wet, squelching sound fills the tunnel. A chittering echoes off the walls. The Sporehusks stir in unison, their pulsing glow quickening as if the whole colony shares a single heartbeat."

    if mc_princess_kat:
        scene 117_s22 with Dissolve(1.0)
        kat "Go ahead. I'll keep them occupied."
        scene 117_s23 with dissolve
        mc "Are you sure? You've been out of the field for a while. If you're not at full strength—"
        scene 117_s22 with dissolve
        kat "I can still kill a hundred of them. I'm sure of that much."
        kat "Gods, I missed this. The adrenaline. Just me, my blade, and a horde of things that need to die."
        scene 117_s23 with dissolve
        mc "Just be careful."
        scene 117_s26 with dissolve
        lewis "Come on, let's get out of here!"

    elif mc_princess_thulkin:
        scene 117_s25 with vpunch
        thulkin "*laughs* Hah! Looks like I won't have to go looking for a fight after all!"
        alex "There he goes..."
        thulkin "Come on, you overgrown mushrooms! Show me what passes for fury among fungus!"
        scene 117_s25 with vpunch
        thulkin "RAAAAGGHHH!"
        scene 117_s26 with dissolve
        lewis "Come on! Let's get out of here!"

    elif mc_princess_mili:
        scene 117_s24 with Dissolve(1.0)
        Millicent "So. They noticed us already... How convenient."
        Millicent "Go on. I'll keep them occupied. Just don't mind the smell of burning flesh and fungus."
        mc "We're counting on you, Millicent!"
        scene 117_s26 with dissolve
        lewis "Come on, let's get out of here!"

    else:
        scene 117_s26 with dissolve
        lewis "There's no one to hold them back! We have to run!"

    if mc_princess_kat:
        perception "You start running. Behind you, the sounds of combat erupt. Steel hitting slick, rubbery flesh. The tunnel blurs past."
    elif mc_princess_thulkin:
        perception "You start running. Behind you, the sounds of combat erupt. Steel hitting slick, rubbery flesh, the sound of Thulkin's laughter. The tunnel blurs past."
    elif mc_princess_mili:
        perception "You start running. Behind you, the sounds of combat erupt. The shriek of burning fungal matter. The tunnel blurs past."
    stop music fadeout 1.0 
    scene 117_s27 with Fade(1.0,0.5,0.5)
    play music "ambiance/caves_of_dawn.mp3" fadein 1.0 volume 0.5 loop
    lewis "Stop! I... I think we go left from here."
    alex "You {i}think?{/i}"
    lewis "W-We were running, alright? I might've... lost the path a bit. I had the map memorized, but everything looks so different in the dark and with those things."
    scene 117_s28 with Fade(0.5,0.5,0.5)
    lewis "Wait, what? This should be the correct way!"
    scene 117_s29 with dissolve
    alex "Get it together, Lewis!"
    scene 117_s28 with dissolve
    lewis "I-I'm sorry! I... I don't know! I thought I knew—I studied the map, I—"
    scene 117_s30 with dissolve
    mc "Breathe, Lewis. Breath and remember."
    scene 117_s31 with dissolve
    lewis "Look, man. I'm... I'm just a regular recruit!"
    lewis "I never passed the officer's exam. I never had a successful mission. I-I didn't even get to fight anyone or anything other than my combat instructor!"
    lewis "Oh Gods, I'm gonna die here! If the poison or Sporehusks don't get us, then I'll die after... Oh have mercy..."
    scene 117_s32 with dissolve
    mc "..."
    alex "..."
    scene 117_s33 with Dissolve(1.0)
    alex "*sigh* Useless. We'll have to find the way on our own."
    if mc_princess_ava:
        scene 117_s34 with dissolve
        mc "Hold on. I can feel my skin stinging... Do you feel it too?"
        scene 117_s33 with dissolve
        alex "I thought I was the only one... I didn't want to say anything."
        scene 117_s34 with dissolve
        mc "Dammit. Ava botched the casting, or the poison's stronger than she accounted for."
        mc "Or... do you think she did it on purpose?"
        scene 117_s33 with dissolve
        alex "We'll confront her about it later."
        alex "Either way, the protection's degrading faster than it should. We'll have less time to find our way now."
        
    scene 117_s34 with dissolve
    mc "Follow behind us, Lewis."
    lewis "Oh, Gods... oh, Gods... I think I'm gonna puke!"
    alex "*giggles*"
    mc "What's got you grinning so hard, Alex?"
    scene 117_s33 with dissolve
    alex "He reminds me of my brother. He's always trying to act brave, but underneath it all.... *chuckles*  he's just a scaredycat."
    scene 117_s34 with dissolve
    scene 117_sewer1 with Fade(0.5,0.5,0.5)
    alex "I'll keep track of where we go, [mc]. That way, we won't end up revisiting places we've already been."
    $ princess_timer = 30
    if mc_princess_ava:
        $ princess_timer -= 3
    if mc_princess_none:
        $ princess_timer -= 5
    $ in_free_roam = True
    $ free_roam_arrows = True

    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    
    $ current_objective = "I have to navigate this sewer and find the cellar \nwhere the princess is being held. This is by far the \nmost dangerous thing I've attempted since arriving \nhere. I should move quickly. \n\nThere's a strange red glow coming from certain \ntunnels. I assume it's being emitted by the \nSporehusks, so it's best to avoid those areas."

    $ second_objective = ""
    $ third_objective = ""
    call screen scene117_maze1 with dissolve

label scene117_maze_up:
    scene 117_sewer2 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze2 with dissolve

default scene117_maze_up_up = False
default scene117_maze_up_left = False
default scene117_maze_up_right_up_right = False
default scene117_maze_up_right_up_up_right = False
default scene117_maze_up_right_up_up_up = False

label scene117_maze_up_up:
    $ scene117_maze_up_up = True
    scene 117_sewer4 with dissolve
    lewis "Sporehusks ahead! Let's not wake them up. We should move slowly."
    $ princess_timer -= 2
    call screen scene117_maze3 with dissolve

default scene117_maze3_poster = True

label scene117_maze_up_left:
    $ scene117_maze_up_left = True
    if scene117_maze3_poster:
        scene 117_sewer3_2 with dissolve
        alex "Looks like a dead end."
        $ princess_timer -= 1
    else:
        scene 117_sewer3 with dissolve
    call screen scene117_maze3 with dissolve

label scene117_maze_up_left_poster:
    $ persistent.reb_render3 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene117_maze3_poster = False
    jump scene117_maze_up_left

default scene117_maze4_poster = True
label scene117_maze_up_right:
    if scene117_maze4_poster:
        scene 117_sewer5_2 with dissolve
    else:
        scene 117_sewer5 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze4 with dissolve

label scene117_maze_up_right_poster:
    $ persistent.diana_render3 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene117_maze4_poster = False
    jump scene117_maze_up_right

default scene117_maze_up_right_up_first = True
label scene117_maze_up_right_up:
    scene 117_sewer6 with dissolve
    $ princess_timer -= 1
    if scene117_maze_up_right_up_first:
        $ scene117_maze_up_right_up_first = False
        lewis "Cobwebs?! A-Are there spiders nearby? Ah! I feel something crawling on me!"
        alex "*laughs*"
    call screen scene117_maze5 with dissolve

default scene117_maze6_poster = True
label scene117_maze_up_right_up_right:
    $ scene117_maze_up_right_up_right = True
    if scene117_maze6_poster:
        scene 117_sewer7_2 with dissolve
        $ princess_timer -= 1
        alex "There's a massive drop here. I can't even see the bottom."
    else:
        scene 117_sewer7 with dissolve
    call screen scene117_maze6 with dissolve

label scene117_maze_up_right_up_right_poster:
    $ persistent.kat_render3 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene117_maze6_poster = False
    jump scene117_maze_up_right_up_right

label scene117_maze_up_right_up_up:
    scene 117_sewer8 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze7 with dissolve

default scene117_maze8_poster = True
label scene117_maze_up_right_up_up_up:
    $ scene117_maze_up_right_up_up_up = True
    if scene117_maze8_poster:
        scene 117_sewer9_2 with dissolve
        $ princess_timer -= 1
    else:
        scene 117_sewer9 with dissolve
    call screen scene117_maze8 with dissolve

label scene117_maze_up_right_up_up_up_poster:
    $ persistent.mix_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene117_maze8_poster = False
    jump scene117_maze_up_right_up_up_up

label scene117_maze_up_right_up_up_right:
    $ scene117_maze_up_right_up_up_right = True
    scene 117_sewer10 with dissolve
    $ princess_timer -= 2
    lewis "Eeeugh! Th-That sack looks too big for a rat. I hope it isn't what I think it is..."
    lewis "Walk slow. Don't stir them up."
    call screen scene117_maze9 with dissolve

label scene117_maze_up_right_up_up_left:
    scene 117_sewer11 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze10 with dissolve

label scene117_maze_up_right_up_up_left_up:
    scene 117_sewer12 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze11 with dissolve

default scene117_maze_up_right_up_up_left_up_up = False
label scene117_maze_up_right_up_up_left_up_up:
    $ scene117_maze_up_right_up_up_left_up_up = True
    scene 117_sewer13 with dissolve
    $ princess_timer -= 2
    call screen scene117_maze12 with dissolve

default scene117_maze13_poster = True
label scene117_maze_up_right_up_up_left_up_left:
    if scene117_maze13_poster:
        scene 117_sewer14_2 with dissolve
        $ princess_timer -= 1
    else:
        scene 117_sewer14 with dissolve
    call screen scene117_maze13 with dissolve

label scene117_maze_up_right_up_up_left_up_left_poster:
    $ persistent.maia_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene117_maze13_poster = False
    jump scene117_maze_up_right_up_up_left_up_left

default scene117_maze_up_right_up_up_left_up_left_left = False
label scene117_maze_up_right_up_up_left_up_left_left:
    $ scene117_maze_up_right_up_up_left_up_left_left = True
    scene 117_sewer15 with dissolve
    $ princess_timer -= 2
    lewis "There's a whole nest here! Let's back up slowly."
    call screen scene117_maze14 with dissolve

label scene117_maze_up_right_up_up_left_up_left_right:
    scene 117_sewer16 with dissolve
    $ princess_timer -= 1
    call screen scene117_maze15 with dissolve

label scene117_maze_up_right_up_up_left_up_left_right_up:
    scene 117_sewer17 with dissolve
    $ princess_timer -= 1
    $ in_free_roam = False
    lewis "I-I remember!"
    alex "Took you long enough."
    lewis "This is it! We're right underneath the castle cellar."
    mc "Up that ladder? Lead the way, Lewis."
    scene 117_s35 with Dissolve(1.0)
    perception "You ascend the ladder. With every rung, the smell of alcohol grows stronger. The faint echo of combat behind you finally ceases, swallowed by distance and dripping water."
    if mc_princess_kat:
        mc "I hope Kat is doing fine."
    elif mc_princess_thulkin:
        mc "I hope Thulkin is doing fine."
    elif mc_princess_mili:
        mc "I hope Millicent is doing fine."
    stop music fadeout 1.0 

    scene 117_s36 with Fade(1.0,1.0,1.0)
    ""
    scene 117_s37 with Dissolve(1.0)
    lewis "Oh, thank the Gods! We did it! We actually—"
    scene 117_s38 with dissolve
    alex "Shut your mouth!"
    scene 117_s39 with Dissolve(2.0)
    play music "sad/reb2.mp3" fadein 3.0 loop
    env "Barrels upon barrels of wine stack the walls, their wood blackened with age. Cobwebs fill every nook and cranny, thick as curtains. And behind it all, in the very middle of the cellar, a lonely princess sleeps on the cold stone."
    mc "Rebecca..."
    scene 117_s40 with Dissolve(1.0)
    mc "Look what she's done to you."
    if mc_karma >= 5:
        mc "I promise to make it right. I promise to save this city—so you can walk proud and high again."
    else:
        mc "Every single one who had a hand in this... I will burn them all. They will beg for mercy before the end, and I will give them exactly as much as they gave you. None."
    scene 117_s41 with Dissolve(1.0)
    alex "Step aside."
    play sound "sound_effects/sword/sword_swing2.mp3"
    scene 117_s42 with vpunch
    alex "Hnhn!"
    perception "Alex swings her sword with precision, aiming at the chain. The blade strikes true, but bounces back with a sharp clink."
    scene 117_s43 with Dissolve(1.0)
    alex "What? That should have cut through?"
    alex "Lewis!"
    scene 117_s44 with dissolve
    lewis "I-I don't know... surely they wouldn't chain a weak malnourished woman with something stronger than steel, r-right?"
    lewis "...I think they did. I think Avery used something stronger... Just to be sure."
    scene 117_s43 with dissolve
    alex "God, I wish I could strangle you right now!"
    scene 117_s44 with dissolve
    lewis "I'm sorry! I didn't know! None of the reports mentioned—"
    scene 117_s45 with Dissolve(1.0)
    joan "{size=30}Psst! Can you hurry it up?! Your time is almost over! We need time for ourselves to run away!{/size}"
    scene 117_s46 with Dissolve(1.0)
    mc "Let me try."
    if mc_influence_cheiftain_bad:
        $ minthra_love += 10
    if ava_dead:
        $ minthra_love += 10
    if mc_killed_lena:
        $ minthra_love += 10
    if mc_killed_alice:
        $ minthra_love += 10
    $ princess_timer -= 1
    if princess_timer < 0:
        $ princess_timer = 1
    call screen scene117_choice01 with dissolve

default mc_yank_times = 0
label scene117_choice01_op1:
    $ princess_timer -= 1
    play sound "sound_effects/doors/chain_rattle.mp3"
    scene 117_s48 with Dissolve(0.3)
    scene 117_s48 with vpunch
    stop sound fadeout 0.3
    if mc_yank_times == 0:
        $ mc_yank_times += 1
        mc "HNNGGG!"
        alex "Not even my sword could do it. You really think you can manage with our your hands?"
        mc "I don't need to break it. Just need to yank it out."
        scene 117_s46 with dissolve
    elif mc_yank_times == 1:
        $ mc_yank_times += 1
        mc "AGGHHHHH!"
        alex "Wait. I think the chain is weakening... or is that just me?"
        lewis "Please let it be weakening. Please, please, please..."
    elif mc_yank_times == 2:
        $ mc_yank_times += 1
        mc "FUUUCKK!"
        alex "I-I think you're actually doing it! One more time!"
    elif mc_yank_times == 3:
        mc "GET... OFF... OF... HER!"
        scene 117_s49 with Dissolve(0.3)
        play sound "sound_effects/boulder_fall.mp3"
        scene 117_s49 with vpunch
        perception "The chain rips from the wall with a deafening crack. A chunk of stone the size of a shield comes with it, crashing to the floor."
        if not princess_timer <= 0:
            $ mc_princess_success = True
            scene 117_s57 with Dissolve(1.0)
            alex "You... did it!"
            joan "About time!"
            alex "Come on. Carry her and follow me, I remember the way back."
            scene 117_s58 with Dissolve(1.0)
            lewis "Hurry, before someone notices."
            scene 117_s59 with Dissolve(1.0)
            mc "Take care, Lewis. Do you know where to go? Is it safe?"
            scene 117_s60 with dissolve
            lewis "A lot safer from here, that's for sure. Don't worry about us, we'll take care of ourselves. Just make sure the princess survives."
            lewis "Go!"
            jump scene117_2
        else:
            scene 117_s45 with Dissolve(1.0)
            joan "Time's out! Get out of there! NOW!"
            scene 117_s57 with dissolve
            alex "We will. Come on, let's carry her!"
            scene 117_s50 with dissolve
            lewis "No! Leave her! I-If they find out she's gone, they'll know someone was here! They'll trace it back to us! We'll be blamed!"
            scene 117_s51 with dissolve
            alex "You want us to leave her after we finally broke her chain?! After all of this?!"
            scene 117_s50 with dissolve
            lewis "Yes, please! My life's on the line here! Joan's life! We have families!"
            scene 117_s51 with dissolve
            alex "What happened to sacrificing yourself for her?"
            scene 117_s50 with dissolve
            lewis "Please just go! I don't want to die!"
            scene 117_s51 with dissolve
            call screen scene117_choice02 with dissolve
    if princess_timer <= 0:
        scene 117_s45 with Dissolve(1.0)
        if not mc_yank_times == 3:
            joan "Time's out! Get out of there! NOW!"
            scene 117_s51 with Dissolve(1.0)
            alex "But the princess is still chained up, we can't just—"
            scene 117_s50 with dissolve
            lewis "Just go, please! My life's on the line here! Joan's life! If they catch us—"
            scene 117_s51 with dissolve
            alex "What happened to sacrificing yourself for her?"
            scene 117_s50 with dissolve
            lewis "Please just go! I don't want to die!"
            scene 117_s51 with dissolve
            call screen scene117_choice02 with dissolve
    scene 117_s46 with dissolve
    call screen scene117_choice01 with dissolve

label scene117_choice01_op2:
    $ princess_timer -= 1
    mc "(Minthra, I need you.)"
    scene 117_s47 with Dissolve(1.0)
    if minthra_love >= 40:
        $ mc_princess_success = True
        minthra "It shall be done."
        minthra "Go ahead and break her chains, my champion. You have earned my help. You have followed my commands more often than you have strayed. That deserves reward."
        mc "(Thank you.)"
        play sound "sound_effects/doors/chain_rattle.mp3"
        scene 117_s48 with Dissolve(0.3)
        scene 117_s48 with vpunch
        stop sound fadeout 0.3
        sensation "Power floods through you, but not the wild, uncontrolled surge you've felt before. It's precise. Focused. It gathers in your arms, your shoulders, your core."
        mc "HNNGGGGN!"
        scene 117_s49 with Dissolve(0.3)
        play sound "sound_effects/boulder_fall.mp3"
        scene 117_s49 with vpunch
        perception "The chain rips from the wall with a deafening crack. A chunk of stone the size of a shield comes with it, crashing to the floor."
        alex "You did it! Impressive. I don't know how, but... impressive."
        scene 117_s57 with dissolve
        alex "Come on. Carry her and follow me, I remember the way back."
        scene 117_s58 with Dissolve(1.0)
        lewis "Hurry, before someone notices."
        scene 117_s59 with Dissolve(1.0)
        mc "Take care, Lewis. Do you know where to go? Is it safe?"
        scene 117_s60 with dissolve
        lewis "A lot safer from here, that's for sure. Don't worry about us, we'll take care of ourselves. Just make sure the princess survives."
        lewis "Go!"
        jump scene117_2
    elif minthra_love >= 20:
        minthra "You expect a lot from me, yet you do not always follow my commands, vessel. Tell me. Why should I assist you?"
        mc "(I... Look, I really need help. Just this one time.)"
        minthra "You will need my help again. And again. Many more times than you might think."
        minthra "You walk a line between defiance and devotion. For that... I shall allow you a favor here."
        minthra "But know that you must give something in return. Something of equal value. When I call for payment, you will not refuse."
        minthra "Promise that you won't refuse me next time."
        call screen scene117_choice03 with dissolve
        mc "*sigh* (I promise.)"
        $ mc_owe_minthra = True
        $ mc_princess_success = True
        play sound "sound_effects/doors/chain_rattle.mp3"
        scene 117_s48 with Dissolve(0.3)
        scene 117_s48 with vpunch
        stop sound fadeout 0.3
        sensation "Power floods through you, but not the wild, uncontrolled surge you've felt before. It's precise. Focused. It gathers in your arms, your shoulders, your core."
        mc "HNNGGGGN!"
        scene 117_s49 with Dissolve(0.3)
        play sound "sound_effects/boulder_fall.mp3"
        scene 117_s49 with vpunch
        perception "The chain rips from the wall with a deafening crack. A chunk of stone the size of a shield comes with it, crashing to the floor."
        alex "You did it! Impressive. I don't know how, but... impressive."
        scene 117_s57 with Dissolve(1.0)
        alex "Come on. Carry her and follow me, I remember the way back."
        scene 117_s58 with Dissolve(1.0)
        lewis "Hurry, before someone notices."
        scene 117_s59 with Dissolve(1.0)
        mc "Take care, Lewis. Do you know where to go? Is it safe?"
        scene 117_s60 with dissolve
        lewis "A lot safer from here, that's for sure. Don't worry about us, we'll take care of ourselves. Just make sure the princess survives."
        lewis "Go!"
        jump scene117_2
    else:
        $ mc_minthra_princess_refuse = True
        minthra "You have made it clear that you do not wish to follow my commands, vessel."
        minthra "You call on me only when it suits you. You take my power and give nothing in return. Deal with this on your own. Learn from your mistakes."
        minthra "Next time you forsake me, not only will this one die, but all those you love. You will watch them fall, and you will know it was your pride that killed them."
        mc "..."
    scene 117_s46 with dissolve
    call screen scene117_choice01 with dissolve

label scene117_choice03_op2:
    $ mc_minthra_princess_refuse = True
    mc "(Forget it. I'll do this on my own.)"
    scene 117_s46 with dissolve
    call screen scene117_choice01 with dissolve

label scene117_choice02_op1:
    $ mc_princess_success = True
    $ mc_sacrifice_lewis_joan = True
    mc "I'm not leaving the princess."
    scene 117_s52 with Dissolve(1.0)
    joan "S-Someone's coming!"
    scene 117_s53 with dissolve
    lewis "Gods... we're done for..."
    if not mc_yank_times == 3:
        play sound "sound_effects/doors/chain_rattle.mp3"
        scene 117_s48 with Dissolve(0.3)
        scene 117_s48 with vpunch
        stop sound fadeout 0.3
        mc "HNNGGGGN!"
        scene 117_s49 with Dissolve(0.3)
        play sound "sound_effects/boulder_fall.mp3"
        scene 117_s49 with vpunch
        perception "The chain rips from the wall with a deafening crack. A chunk of stone the size of a shield comes with it, crashing to the floor."
    scene 117_s53 with Dissolve(1.0)
    guard "What's going on in there?! Why are you standing next to the window and not the door? Joan, report!"
    scene 117_s52 with dissolve
    joan "S-Sir! It's not what it looks like! I was just checking—"
    scene 117_s53 with dissolve
    guard "There's been a break in! Sound the alarm!"
    scene 117_s57 with Dissolve(1.0)
    alex "Come on. Carry her and follow me, I remember the way back."
    scene 117_s58 with Dissolve(1.0)
    lewis "W-What about us?!"
    scene 117_s59 with Dissolve(1.0)
    mc "I'm sorry."
    scene 117_s60 with dissolve
    lewis "What!?"
    jump scene117_2

label scene117_choice02_op2:
    $ mc_princess_fail_late = True
    scene 117_s54 with Dissolve(1.0)
    mc "We can't let them die, Alex."
    scene 117_s55 with dissolve
    alex "You're going to leave after we've come so far? After everything?!"
    scene 117_s54 with dissolve
    mc "I am. We'll have to rescue the princess another way. She'll be fine if we hurry to Nahraya and stop the execution."
    mc "Lewis and Joan, on the other hand... they'll die if the guards know someone's been here. They trusted us. I won't let them pay for my failure to plan better."
    scene 117_s56 with dissolve
    alex "Nghnn... Goddammit! FINE!"
    scene 117_s57 with Dissolve(1.0)
    mc "Thank you. And I'm sorry, Rebecca. This isn't the end."
    alex "Move. Before I change my mind."
    stop music fadeout 1.0 
    scene 117_s67 with Fade(1.0,1.0,1.3)
    play music "dungeon.mp3" fadein 1.0 loop
    perception "You descend into the sewer, the trapdoor closing above you."
    jump scene117_2

label scene117_2:
    stop music fadeout 1.0 
    if mc_sacrifice_lewis_joan:
        scene 117_s61 with Fade(1.0,1.0,1.3)
        play music "dungeon.mp3" fadein 1.0 loop
        perception "You descend into the sewer, the trapdoor closing above you. Joan's screams echo through the cellar as guards seize her. Their fate is sealed."
    elif mc_princess_success:
        scene 117_s61 with Fade(1.0,1.0,1.3)
        play music "dungeon.mp3" fadein 1.0 loop
        perception "You descend into the sewer, the trapdoor closing above you."

    if mc_princess_kat:
        if mc_princess_success:
            scene 117_s62 with Fade(1.0,1.0,1.3)
            alex "Hmm? Where's that girl? We left her right here, didn't we?"
            scene 117_s63 with dissolve
            mc "Kat! Where are you? Time to go!"
            scene 117_s62 with dissolve
            alex "I don't hear anything. Come on, she probably left."
            scene 117_s63 with dissolve
            mc "That's not something she would do... I hope you're right."
            scene 117_s65 with Fade(1.1,1.0,1.3)
            ""
        else:
            scene 117_s77 with Fade(1.0,1.0,1.3)
            alex "Hmm? Where's that girl? We left her right here, didn't we?"
            mc "Kat! Where are you? Time to go!"
            alex "I don't hear anything. Come on, she probably left."
            mc "That's not something she would do... I hope you're right."
            scene 117_s65 with Fade(1.1,1.0,1.3)
            ""
    elif mc_princess_thulkin:
        if not mc_princess_success:
            scene 117_s66 with Fade(1.0,1.0,1.3)
            thulkin "Already? I was just getting started!"
            scene 117_s77 with Dissolve(1.0)
            mc "You've done enough, Thulkin. Time to leave."
            thulkin "I don't see anyone wearing a crown on you. Where's the lass?"
            mc "We... we couldn't do it. Lewis and Joan would have died if we'd stayed any longer."
            mc "But I promise that we'll rescue her later. This isn't over."
            thulkin "Don't be hard on yourself, you made the right choice. That Lewis is cowerdaly, but he has a heart of gold. I would also not wish harm on him."
        else:
            scene 117_s66 with Fade(1.0,1.0,1.3)
            thulkin "Already? I was just getting started!"
            scene 117_s64 with Dissolve(1.0)
            mc "You've done enough, Thulkin. Time to leave."

    elif mc_princess_mili:
        scene 117_s68 with Fade(1.0,1.0,1.3)
        Millicent "Finally! I seriously underestimated these things. They started learning my attacks!"
        scene 117_s69 with dissolve
        mc "You alright?"
        scene 117_s68 with dissolve
        Millicent "Mostly. My arms and legs got a few lacerations, but I'll live."
        scene 117_s64 with Dissolve(1.0)
        Millicent "Some even tried to lay eggs inside me! I barely got them off before one managed to stick its... proboscis thing in my mouth! Filthy, disgusting creatures!"
        mc "I appreciate your help. Come on, let's go."
        if not mc_princess_success:
            scene 117_s68 with dissolve
            Millicent "Wait, where's the girl? Don't tell me I did this for nothing."
            scene 117_s69 with dissolve
            mc "It wasn't for nothing. We found her. We just... couldn't get her out in time. We'll have to rescue her another way."

    stop music fadeout 1.0 
    scene 117_s70 with Fade(1.0,1.0,1.1)
    play music "thunder2.mp3" fadein 1.0 loop
    alex "*cough* *cough* Ahhh... fresh air."
    mc "To the carriage. Now. We're not safe yet."

    if mc_princess_thulkin:
        scene 117_s71 with Dissolve(1.0)
        thulkin "Farewell, [mc]!"
        if mc_princess_success:
            thulkin "It's never a boring time when I'm with you! My clan will sing songs of this night for generations!"
        else:
            thulkin "It's never a boring time when I'm with you! Although you couldn't save the princess, your bravery will be sung about for generations!"
    elif mc_princess_mili:
        scene 117_s72 with Dissolve(1.0)
        if mc_kiss_milesent:
            Millicent "Leaving after you took my lips? *chuckles* Men."
            scene 117_s73 with dissolve
            mc "I'm not leaving for good. And I did mean every word, Millicent. What happened at the goblin camp... and your help here tonight... I'll never forget that."
            scene 117_s72 with dissolve
            Millicent "I'm not getting any older, but you are. Just don't take too long."
            Millicent "Perhaps we'll meet there too... Who knows."
        else:
            Millicent "Take care out there. You shouldn't have many issues traversing the desert, but always keep an eye open."
            scene 117_s73 with dissolve
            mc "I will. Thank you for the help, Millicent. I won't forget this."
            scene 117_s72 with dissolve
            Millicent "Perhaps we'll meet there too... Who knows."
        scene 117_s73 with dissolve

    if not mc_princess_success:
        scene 117_s75 with dissolve
        reham "[mc], where's the princess?"
        scene 117_s76 with dissolve
        mc "We couldn't do it. I'm sorry."
        scene 117_s75 with dissolve
        m "No!"
        scene 117_s76 with dissolve
        mc "We'll have to do it your way, Reham."
        scene 117_s75 with dissolve
        reham "*sigh* We could have avoided this entirely. Let's hope you two haven't made even more unnessary enemies tonight."
    else:
        scene 117_s74 with Dissolve(1.5)
        reham "Set her here. Gently."
        scene 117_s75 with dissolve
        m "P-Princess... Will she be fine, [mc]? She looks so pale."
        scene 117_s76 with dissolve
        mc "She will be. She went through a lot. She can't lose now... not after all of this."
    
    scene 117_s75 with dissolve
    if mc_princess_100:
        reham "[mc]... I've counted the supplies. This is barely enough for the journey."
        reham "We must be very conservative. Some might not even get food for the day—or we all eat half-portions and hope it stretches."
        reham "The princess needs more than we do, but even she can't have full meals. Not with what we have."
        scene 117_s76 with dissolve
        mc "We'll manage. Put the biggest portion for Rebecca. The rest of us can survive on less."
        scene 117_s75 with dissolve
        reham "As you wish. May we have a swift journey."

    elif mc_princess_300:
        reham "I've counted the supplies. It should do us just before reaching the city—if we're careful. But we mustn't overeat."
        scene 117_s76 with dissolve
        mc "We'll be there long before we run out."
        scene 117_s75 with dissolve

    elif mc_princess_500:
        reham "[mc]... I've counted the supplies. This is more than enough to get us to the city. We could even feed an extra mouth and still have reserves."
        scene 117_s76 with dissolve
        mc "Yeah. I overdid it in case something happened."
        scene 117_s75 with dissolve
        reham "Good idea."
    stop music fadeout 1.0 
    scene black with Dissolve(2.0)
    alex "I'll take the reins."

label scene118:
    scene 118_s1 with Fade(1.3,1.0,1.5)
    play music "wind.mp3" fadein 3.0 loop
    env "Dawn comes freezing and gray. The road stretches endlessly ahead, a ribbon of pale dirt cutting through the forest. The wind howls, rattling the carriage canopy and finding every crack in the wood."
    if mc_princess_success:
        mc "Brrr... Is the princess covered? She's not shivering, is she?"
        reham "She has four layers on top of her. Any more and she'll overheat—even in this cold."
        reham "You, on the other hand need to warm up."
    else:
        mc "Brrr... Are you cold, Maia?"
        reham "*chuckles* She can't even hear us. She's too enthralled by the scenary."

    scene 118_s2 with Fade(1.3,1.0,1.5)
    alex "Looks like rain."
    mc "Take cover back there."
    reham "Already on it."
    scene 118_s3 with Dissolve(1.0)
    m "What's the food like in Nahraya?"
    scene 118_s4 with dissolve
    reham "*chuckles* Always thinking of your stomach."
    scene 118_s3 with dissolve
    m "I-I just want to know."
    scene 118_s4 with dissolve
    reham "Well, it's the best food you've ever tasted. Just wait. You'll never want to leave."

    scene 118_s5 with Fade(1.3,1.0,1.5)
    env "The trees decrease in number, then vanish entirely. The air grows warmer, then hot, then oppressive. The sun beats down on the carriage roof, turning the interior into an oven."
    m "*gag* ...I feel sick."
    scene 118_s6 with Dissolve(1.0)
    reham "Are you experiencing road sickness? Lie down and lift your legs up."
    scene 118_s7 with dissolve
    m "..."
    scene 118_s6 with dissolve
    reham "Maia?"
    scene 118_s8 with vpunch
    m "Blhaaaaghhhh!"
    reham "Oh dear... come here, hopefully it's just road sickness and not the flu."
    stop music fadeout 1.0 
    scene 118_s9 with Fade(1.3,1.0,1.5)
    play music "night.mp3" fadein 1.0 loop
    m "Please! I can't take it anymore! Can we stop and sleep? My legs feel numb from sitting."
    scene 118_s10 with dissolve
    mc "You know what? I also feel like shit. The horses need rest too."
    scene 118_s12 with Dissolve(1.0)
    mc "Alex?"
    scene 118_s11 with dissolve
    alex "...Y-Yeah, let's do that."
    scene 118_s12 with dissolve
    mc "Something on your mind? You've been quiet since we left the city. Well... quieter than usual."
    scene 118_s11 with dissolve
    alex "It's nothing."
    scene 118_s12 with dissolve

    scene 118_s13 with Fade(1.0,1.0,1.0)
    m "Ahhh... finally... Nghnnn! It feels so good to stretch."
    scene 118_s14 with Dissolve(1.0)
    reham "It's so calm and peaceful out here. I feel like... *yawn* taking a little nap."
    scene 118_s15 with dissolve
    mc "Get some rest, you two. You've earned it."
    scene 118_s14 with dissolve
    if mc_princess_success:
        reham "With pleasure. Wake me if the princess stirs."
    else:
        reham "With pleasure."
    scene 118_s15 with dissolve
    scene 118_s16 with Fade(1.5,1.0,1.3)
    if mc_princess_success:
        env "Stars litter the cloudless sky in white, orange, and red. The fire pops. The horses snort softly in the darkness. The princess breathes, steady and slow, wrapped in her cocoon of blankets."
    else:
        env "Stars litter the cloudless sky in white, orange, and red. The fire pops. The horses snort softly in the darkness."
    scene 118_s17 with Dissolve(1.0)
    mc "..."
    scene 118_s18 with Dissolve(1.0)
    alex "..."
    empathy "She glances toward you, a flicker of worry in her eyes. The kind you must confide with someone to lessen."
    mc "What's up?"
    if mc_hug_alex:
        $ alex_love += 10
    if mc_princess_success:
        $ alex_love += 10
    
    if alex_love < 40:
        scene 118_s19 with dissolve
        empathy "She looks away as soon as your eyes meet. You still haven't managed to earn her full trust yet. Whatever's bothering her, she's not ready to share it. Not with you... Maybe not with anyone."
        scene 118_s20 with dissolve
        alex "It's pretty."
        scene 118_s19 with dissolve
        mc "It is."
        scene 118_s16 with Dissolve(1.0)
        ""
        jump scene118_4

    else:
        stop music fadeout 1.0 
        scene 118_s21 with Dissolve(1.0)
        empathy "Her expression eases as her gaze stays fixed on you. Your actions and choices along have penetrated her cold heart. She trusts you fully."
        play music "alex.mp3" fadein 3.0 loop
        scene 118_s22 with dissolve
        alex "It's pretty, isn't it?"
        scene 118_s21 with dissolve
        mc "It is."
        alex "..."
        mc "Talk to me. What's bothering you?"
        scene 118_s22 with dissolve
        alex "I... I can't stop thinking about him."
        scene 118_s21 with dissolve
        call screen scene118_choice01 with dissolve

label scene118_choice01_op1:
    mc "Your brother?"
    alex "Mhm."
    scene 118_s22 with dissolve
    jump scene118_2

label scene118_choice01_op2:
    mc "Your father?"
    scene 118_s22 with dissolve
    alex "No—I mean, sure, but..."
    alex "I meant my brother."
    jump scene118_2
    
label scene118_choice01_op3:
    mc "Your lover back home?"
    scene 118_s22 with dissolve
    alex "Lover? You're seriously misjudging how my life was back there."
    alex "I meant my brother."
    jump scene118_2

label scene118_2:
    alex "He's so far away now and I'm only getting further."
    alex "Every mile this carriage rolls south, every day we cross this desert... I'm leaving him behind. Again."
    scene 118_s21 with dissolve
    mc "Does he not have anyone else there? Someone to look after him?"
    scene 118_s22 with dissolve
    alex "No. Not someone he can trust, at least."
    alex "I just... I just want to hug him. Tell him it's going to be fine. That I'm coming back... That I haven't abandoned him."
    alex "But I can't. And I don't know when I'll see him again... or {i}if{/i} I'll see him again."
    scene 118_s21 with dissolve
    call screen scene118_choice02 with dissolve

label scene118_choice02_op1:
    $ alex_love -= 40
    stop music fadeout 1.0 
    mc "I need you focused, Alex. Stop thinking about him."
    play music "night.mp3" fadein 1.0 loop
    scene 118_s25 with Dissolve(1.0)
    alex "...Huh?"
    alex "W-What, do you think I'm here because I want to be? Do you think I went through all this because... what?! For {i}fun{/i}?!"
    scene 118_s26 with dissolve
    mc "Calm down. You'll wake the others."
    scene 118_s25 with dissolve
    alex "W-Why are you saying that? Don't you feel for me?"
    scene 118_s26 with dissolve
    mc "I do. It's just that this distraction will make you slip up."
    alex "..."
    scene 118_s25 with dissolve
    alex "You know what? Screw you. I didn't know what I was doing... Opening up to you. Stupid."
    alex "Better to be alone. That's how it's always been. That's how it should have stayed."
    scene 118_s27 with Dissolve(1.0)
    mc "Alex—"
    alex "Enough. Take the watch yourself."
    jump scene118_4

label scene118_choice02_op2:
    mc "You will."
    scene 118_s24 with Dissolve(1.0)
    alex "*chuckles* I don't understand how you're so confident. All the odds are stacked against us."
    scene 118_s23 with dissolve
    mc "You don't trust me?"
    scene 118_s24 with dissolve
    alex "I do. You're always trying to help others. Always sticking your neck out for people who probably don't deserve it."
    if mc_agree_help_thulkin and mc_helped_lena:
        alex "Millicent and her brother... that stables woman with her slave problem."
        scene 118_s23 with dissolve
        mc "I just did what anyone would do."
        scene 118_s24 with dissolve
        alex "No. No, you didn't. Most people would look the other way."
    alex "As awful as it sounds... I'm glad it's your life that I ruined."
    scene 118_s23 with dissolve
    mc "Hey, come on. Don't be too harsh on yourself."
    alex "*giggles*"
    jump scene118_3

label scene118_choice02_op3:
    mc "He'll manage if he's your brother."
    scene 118_s24 with Dissolve(1.0)
    alex "What's that supposed to mean?"
    scene 118_s23 with dissolve
    mc "You're strong. Maybe it runs in the bloodline."
    scene 118_s24 with dissolve
    alex "*chuckles* That sounds so stupid... idiot."
    scene 118_s23 with dissolve
    mc "Hey... I was just trying to make you feel better."
    scene 118_s24 with dissolve
    alex "I appreciate it nonetheless... even though you're terrible at it."
    jump scene118_3

label scene118_3:
    $ mc_sat_with_alex = True
    scene 118_s28 with Dissolve(1.0)
    alex "You... you ermm..."
    alex "You always... nghnn... always make me feel better."
    scene 118_s29 with Dissolve(1.0)
    mc "Whoa... is that a compliment?"
    scene 118_s32 with dissolve
    alex "..."
    scene 118_s29 with dissolve
    mc "Thank you."

    if mc_hug_alex:
        scene 118_s30 with Dissolve(1.0)
        alex "Back then... when I told you the truth about everything. About who I was. About what I'd done."
        alex "Y-You hugged me."
        alex "I didn't get it at the time. I thought... I thought you were just being soft. That you... pitied me."
        alex "But I understand now. You weren't pitying me. You were... forgiving me before I'd even asked for it."
        alex "And I'm scared, [mc]. I'm scared of what might happen to someone like you. Someone who trusts that easily."
        alex "You're too good, and people like that don't last long. The world chews them up. I've seen it happen. I... I've {i}made it happen.{/i}"
        scene 118_s31 with dissolve
        mc "I get why you feel this way. Your... 'work' doesn't exactly allow someone to be kind."
        mc "But to me, people deserve a second chance. You were a pawn in a bigger scheme. You acted out of love for your brother."
        mc "There was nothing I could blame you for."
        mc "*chuckles* And I might not be as good as you think I am. I'm no saint, Alex. I'm just... trying. Like you are."
        scene 118_s32 with dissolve
        alex "..."
        scene 118_s33 with Dissolve(2.0)
        perception "She sits next to you and leans over, her shoulder touching yours. The weight of her is warm against the desert chill."
        mc "It's pretty, isn't it?"
        alex "It is."
        stop music fadeout 3.0 

    else:
        scene 118_s30 with Dissolve(1.0)
        alex "You're acting so kind to me... did you forgive me?"
        scene 118_s31 with dissolve
        mc "What do you mean?"
        scene 118_s30 with dissolve
        alex "Back then... when I told you the truth about everything. About who I was. About what I'd done."
        alex "You slapped me."
        alex "A-And don't worry. I completely understand why you did it. I deserved it."
        alex "It's my fault for putting everyone you love at risk."
        alex "I don't deserve kindness. And yet you keep giving it to me. Over and over. I... I don't understand."
        scene 118_s31 with dissolve
        mc "People deserve a second chance. You were a pawn in a bigger scheme. You acted out of love for your brother."
        scene 118_s30 with dissolve
        alex "But the things I did—"
        scene 118_s31 with dissolve
        mc "Perhaps I just didn't see it at the time. The slap... that was my anger, but anger fades."
        mc "What's important is that you're here. You're fighting beside me. You're risking your life to make things right."
        scene 118_s32 with dissolve
        alex "..."
        scene 118_s33 with Dissolve(2.0)
        perception "She sits next to you and leans over, her shoulder touching yours. The weight of her is warm against the desert chill."
        mc "It's pretty, isn't it?"
        alex "It is."
    jump scene118_4

label scene118_4:
    scene 118_s34 with Fade(2.0,1.0,1.5)
    play music "wind.mp3" fadein 1.0 loop
    perception "You hit the road again. It's day five since you left city. The desert stretches endlessly in every direction, heat shimmering on the horizon. The road ahead is still long."
    if mc_princess_100 or mc_princess_300:
        reham "We're almost completely out of supplies!"
        mc "How much is left?"
        reham "*sigh* Barely enough to feed three of us. For a single meal. After that..."
        alex "Don't count me. I've survived longer without food."
        mc "Me too."
        m "Mphmmm... I'm starving."
        reham "Alright. Just the three of us, then—myself, Maia, and the largest portion for the princess. She needs it more than any of us."
    else:
        m "Mphmmm... I'm starving."
        reham "I'll prepare something quick, but you shouldn't eat every three hours, Maia."

    if mc_princess_success:
        scene 118_s36 with Fade(1.1,1.0,1.2)
        if mc_princess_100 or mc_princess_300:
            m "[mc]! [mc]!"
            scene 118_s37 with dissolve
            mc "Huh? What?!"
            scene 118_s38 with dissolve
            m "The princess... she won't stop shaking!"
            scene 118_s35 with Dissolve(1.0)
            reham "Dammit! The medicine ran out yesterday. I knew we were cutting it close, but I thought—"
            mc "Is there anything we can do?"
            reham "Unless you're secretly stashing some herbs, then no."
            mc "Just... just do your best, alright?"
            reham "I will."
            alex "We really should have had more supplies."
            mc "How long till we get there?"
            alex "A day, two at most."
            mc "Then we'll just have to keep moving. No breaks."
        else:
            m "[mc]!"
            scene 118_s37 with dissolve
            mc "Huh? What?!"
            scene 118_s38 with dissolve
            m "Her color is coming back!"
            scene 118_s35 with Dissolve(1.0)
            reham "Yes, thank the Gods. The fever's breaking. Her breathing is steadier, and her pulse is stronger than yesterday."
            mc "How long till she... wakes up?"
            reham "Won't be long, if we keep her stable like this. She's been through hell, but she's strong."
            mc "*sigh* Thank you, Reham. Truly."
            reham "Of course."
    else:
        scene 118_s39 with Fade(1.1,1.0,1.2)
        m "You must be really excited to return. Right, Reham?"
        scene 118_s40 with dissolve
        reham "I am. It's been too long. *chuckles* I can already smell it. Home..."
        mc "We're counting on you to show us the way in the city."
        reham "Of course. You're in good hands."

    stop music fadeout 1.0 
    scene 118_s41 with Fade(1.5,1.0,1.5)
    play music "city_in_the_desert.mp3" fadein 1.0 loop
    perception "Massive walls made of sandstone finally break the monotony of sand. They rise from the desert adorned with carvings that glitter in the harsh light."
    alex "I can see it!"
    mc "Oh... finally."
    if mc_princess_success:
        if mc_princess_100 or mc_princess_300:
            m "Just a little further, princess! Please hold on! Just a little further!"
            reham "*sigh* I hope we make it in time. Her condition is critical. The fever's back, and she's dehydrated despite everything we've tried."
            reham "We'll need to bring her to the hospice as soon as we disembark."
        else:
            m "Can you see it, princess? We're almost there."
            m "Everything is going to be fine. You're safe now."
            reham "Her condition is getting better. It's all thanks to you, [mc]. She couldn't have gotten better without the supplies you purchased."
            mc "She deserves that much after everything."
            reham "We still need to get her to a healer as soon as we disembark."
    else:
        m "It's huge! I've never seen walls that tall! Are those gold carvings?"
        reham "Home. Finally home."
        reham "Welcome to Nahraya. The city of spice, silk, and hospitality. The king is sure to help us once we're allowed a chance to speak to him."
        mc "Then let's do that."

    scene 118_s42 with Fade(1.0,1.0,1.0)
    n_guard "Welcome to the Kingdom of Nahraya, travellers. State the purpose of your visit."
    if mc_princess_success:
        if mc_princess_100 or mc_princess_300:
            mc "We need urgent medical assistance! We have a girl here who's barely breathing, she needs a healer immediately!"
            empathy "The guard takes one look at your face—the desperation, the exhaustion and snaps into action."
            scene 118_s43 with Dissolve(1.0)
            n_guard "Clear the way!"
            n_guard "A guard will escort you to there. May the Gods watch over her."
            mc "Thank you."
            scene 118_s45 with Fade(1.0,1.0,1.0)
            perception "The desert is gone. Ahead stretches the city of Nahraya. The smell of cooking meat and incense fills the air. The noise is overwhelming after a week of wind and silence."
            alex "You didn't tell him about meeting the king?"
            reham "What would a gate-guard know about that? He's paid to check carts and collect tolls, not arrange royal audiences. We need to speak to a higher-up."
        else:
            reham "We need to get to Saint Al-Yar's hospice, sir."
            scene 118_s44 with Dissolve(1.0)
            n_guard "Very well. A guard will escort you to there."
            n_guard "Afterwards, you need to return to the post to issue you a temporary identification card."
            n_guard "You'll need it to conduct any business within the city walls. Keep it on you at all times."
            scene 118_s42 with dissolve
            reham "Thank you. We'll do that."
            scene 118_s45 with Fade(1.0,1.0,1.0)
            perception "The desert is gone. Ahead stretches the city of Nahraya. The smell of cooking meat and incense fills the air. The noise is overwhelming after a week of wind and silence."
            alex "You didn't tell him about meeting the king?"
            reham "What would a gate-guard know about that? He's paid to check carts and collect tolls, not arrange royal audiences. We need to speak to a higher-up."
        jump scene118_5
    else:
        call screen scene118_choice03 with dissolve

label scene118_choice03_op1:
    reham "We're here to trade, sir."
    scene 118_s44 with dissolve
    n_guard "Very well. Turn left from here and approach the post to issue you a temporary identification card. You'll need it to conduct any business within the city walls. Keep it on you at all times."
    reham "Thank you. We'll do that."
    scene 118_s45 with Fade(1.0,1.0,1.0)
    perception "The desert is gone. Ahead stretches the city of Nahraya. The smell of cooking meat and incense fills the air. The noise is overwhelming after a week of wind and silence."
    alex "You didn't tell him about meeting the king?"
    reham "What would a gate-guard know about that? He's paid to check carts and collect tolls, not arrange royal audiences. We need to speak to a higher-up."
    jump scene118_6

default mc_asked_sanoud = False
label scene118_choice03_op2:
    $ mc_asked_sanoud = True
    mc "We need to talk to your king."
    n_guard "What business do you have with our king, traveller?"
    mc "It's urgent business. The fate of cities depends on it."
    perception "You notice the guard attempt to hide a chuckle. His eyelids twitch before he regains his professional demeanor."
    scene 118_s44 with Dissolve(1.0)
    n_guard "Speak to Lord Sanoud at the post to the left. He handles... diplomatic matters. If what you say is {i}truly{/i} important, he shall arrange a date for you with the appropriate officials."
    scene 118_s45 with Fade(1.0,1.0,1.0)
    perception "The desert is gone. Ahead stretches the city of Nahraya. The smell of cooking meat and incense fills the air. The noise is overwhelming after a week of wind and silence."
    jump scene118_6
    
label scene118_choice03_op3:
    mc "We're here on vacation. Just... seeing the sights."
    scene 118_s44 with Dissolve(1.0)
    n_guard "Very well. Turn left and approach the post to issue you a temporary identification card. Enjoy your stay."
    scene 118_s45 with Fade(1.0,1.0,1.0)
    perception "The desert is gone. Ahead stretches the city of Nahraya. The smell of cooking meat and incense fills the air. The noise is overwhelming after a week of wind and silence."
    alex "'Vacation'? Seriously?"
    mc "I couldn't think of anything else that didn't sound suspicious."
    m "I thought it was convincing."
    jump scene118_6

label scene118_5:
    stop music fadeout 1.0
    scene 118_s46 with Fade(1.0,1.0,1.0)
    play music "wind.mp3" fadein 1.0 loop
    doctor "Are you the person in need?"
    scene 118_s47 with dissolve
    mc "Not me. The girl inside. Please, hurry."
    scene 118_s48 with Dissolve(1.0)
    if mc_princess_100 or mc_princess_300:
        reham "Ma'am, she's severely dehydrated and malnourished. We had medicine for the first few days, but it ran out. She needs—"
    else:
        reham "Her condition isn't severe, but she is still in need of proper medicene, Ma'am."
    scene 118_s49 with dissolve
    doctor "We will do what we can."
    scene 118_s50 with Dissolve(1.0)
    n_guard "They will take it from here. As for the rest of you, you need to return to the post and have an identification card issued."
    n_guard "All new arrivals must register. No exceptions."
    mc "Can't we stay to see what happens? Just until we know she's fine?"
    n_guard "No one is permitted to see the patient until it's confirmed that her illness isn't contagious."
    reham "Don't worry about the princess, [mc]. I trust the healers here. Saint Al-Yar's has a reputation across the entire desert. She's in good hands."
    mc "Fine. Lead the way."
    jump scene118_6

label scene118_6:
    stop music fadeout 1.0 
    scene 118_s51 with Fade(1.0,1.0,1.0)
    play music "talkingAmbiance.mp3" fadein 1.0 volume 0.3 loop
    perception "A guard escorts you to the post. A small sandstone building near the main gate, bustling with clerks and travellers."
    alex "I hate doing this. Let's finish up quickly."
    scene 118_s52 with Dissolve(2.0)
    perception "A while passes. Finally, a woman with a profoundly bored expression stands across from you. She doesn't even look at you."
    scene 118_s53 with dissolve
    guard_id "Name?"
    scene 118_s54 with dissolve
    mc "[mc]."
    scene 118_s53 with dissolve
    guard_id "*yawn* Sex, race, and purpose of visit?"
    scene 118_s54 with dissolve
    mc "Uhh... male, human, and here on official business."
    scene 118_s53 with dissolve
    guard_id "Official business, huh? What kind? Diplomatic? Trade? Military?"
    scene 118_s54 with dissolve
    mc "Diplomatic? I have to—"
    scene 118_s53 with dissolve
    guard_id "I really don't care about the details."
    scene 118_s54 with dissolve
    mc "..."
    scene 118_s53 with dissolve
    guard_id "There. Two weeks."
    scene 118_s56 with Dissolve(1.0)
    mc "Two weeks?"
    scene 118_s55 with dissolve
    guard_id "You're permitted to stay for two weeks. If you want to stay longer, you'll need to apply for an extension at least one day before your permit expires."
    guard_id "If you want to apply for permanent citizenship, you'll need to either start a business or live in Nahraya for at least two years."
    scene 118_s56 with dissolve
    mc "Got it. Thanks."
    if mc_asked_sanoud:
        mc "Are you Lord Sanoud?"
        scene 118_s57 with Dissolve(1.0)
        guard_id "Do I look like a 'Sanoud' to you?"
        scene 118_s58 with dissolve
        mc "I... I don't really know?"
        mc "I'd like an audience with the king. It's urgent. I mentioned it at the gate, they said Lord Sanoud could arrange—"
        scene 118_s57 with dissolve
    else:
        mc "I'd like an audience with the king. It's urgent."
        scene 118_s57 with Dissolve(1.0)
    guard_id "Ughh... why do I always get the weird ones?"
    guard_id "Next!"
    scene 118_s58 with dissolve
    mc "Hey, I'm serious here. We have information that could—"
    scene 118_s57 with dissolve
    guard_id "Next!"
    scene 118_s59 with Dissolve(1.0)
    reham "Don't waste your time, [mc]. Those are just regular guards."
    scene 118_s60 with dissolve
    mc "So what now?"
    scene 118_s59 with dissolve
    reham "Why don't we go out and visit my parents? It's been a while since I visited. Far too long, honestly. They might know a thing or two."
    if mc_princess_success:
        reham "I already have a card, so I don't need to go through this. We can visit them and return nighttime to check on the princess."
    else:
        reham "I already have a card, so I don't need to go through this. We can visit them and have some food in our bellies before we start doing anything."
    scene 118_s60 with dissolve
    mc "Alright. Let's wait for the others first."
    scene 118_s61 with Fade(1.0,1.0,1.0)
    alex "Finally! That girl needs to seriously get punched in the face."
    scene 118_s62 with Dissolve(1.0)
    mc "Don't start any fights."
    scene 118_s63 with dissolve
    alex "Right. You can go ahead without me. I don't care for meeting your parents, Reham—no offense. I'll go and see if I can arrange a meeting on my own."
    scene 118_s64 with Dissolve(1.4)
    m "Umm... [mc]?"
    scene 118_s66 with dissolve
    mc "What is it?"
    scene 118_s64 with dissolve
    m "{size=30}P-Please don't leave me with her...{/size}"
    scene 118_s66 with dissolve
    mc "*chuckles* Don't like being with Alex?"
    scene 118_s64 with dissolve
    m "{size=30}No... s-she's scary.{/size}"
    scene 118_s65 with dissolve
    reham "You're coming with me, Maia. You're safer away from her, and from [mc], now that I think about it."
    scene 118_s66 with dissolve
    stop music fadeout 1.0 
    jump scene119

label scene119:
    scene 119_s1 with Fade(1.5,1.0,1.5)
    play music "nahraya.mp3" fadein 1.0 volume 0.5 loop
    perception "You follow Reham into the bustling market. The contrast to Irda is overwhelming. Unlike the streets of the western city, Nahraya's market is a riot of color and noise."
    mc "It's so noisy! I can barely hear myself think!"
    reham "*chuckles* That's how it's done here, the loudest voice gets the most customers. It'll take time getting used to."
    scene 119_s2 with Dissolve(1.0)
    m "Ohh! Cakes!"
    m "Ren used to make these for me all the time!"
    scene 119_s3 with Dissolve(1.0)
    reham "Ah, freshly baked cake. It's not exactly the Nahrayan delicacy that I'd hoped you'd try first."
    m "Can we please get some?"
    reham "Hmm..."
    m "Pleaseeee!"
    reham "*chuckles* Fine, fine. I'm in the mood for one too."
    scene 119_s4 with Dissolve(1.0)
    reham "You want me to get you one, [mc]? My treat."
    scene 119_s6 with Dissolve(1.0)
    mc "..."
    perception "Near the entrance to a narrow alley, you see a man moving with purpose. He's wearing a sword. He glances over his shoulder, then slips into the alley."
    scene 119_s5 with Dissolve(1.0)
    mc "Hold on. I'll be right back."
    scene 119_s4 with dissolve
    reham "Alright. We'll wait for you here. Don't wander too far!"
    scene 119_s7 with Fade(1.0,1.0,1.0)
    perception "You walk into the alleyway and see three men, their swords unsheathed. A man and a woman are backed against the wall."
    scene 119_s8 with Dissolve(1.0)
    mc "(A holdup?)"
    scene 119_s9 with Dissolve(1.0)
    bandit "You kept us waiting too long, Rohan. Our patience is running thin. Mr. Victor doesn't like to be kept waiting."
    scene 119_s10 with dissolve
    rohan "B-But he assured me that I have more time! He said two more months—I have it in writing!"
    scene 119_s9 with dissolve
    bandit "He changed his mind. Happens all the time. He wants it now."
    bandit "Either you pay... or we do this the hard way."
    scene 119_s10 with dissolve
    rohan "Please, there's no need for this to get violent! I-I promise, only two more weeks! I'll pay with interest! I'll—"
    scene 119_s9 with dissolve
    bandit "*sigh* That's not gonna cut it, Rohan. We've heard your promises before."
    bandit "Perhaps you need some motivation."
    scene 119_s11 with Dissolve(1.0)
    bandit "We'll take your lovely wife here. Yasmine, isn't it? Pretty name. Pretty face. She'll help us pay off your debt."
    bandit "A few months working at one of Mr. Victor's brothels, and you'll be square. Isn't that right, ma'am? You'll help your dear ol' husband, won't you?"
    scene 119_s12 with dissolve
    yasmine "Off with you, brutes! I'd rather die than sell off my body!"
    scene 119_s11 with dissolve
    bandit "I'm afraid that isn't your choice. Unless your deadbeat husband coughs up our coin now, you're coming with us. One way or another."
    scene 119_s10 with Dissolve(1.0)
    rohan "Uhn..."
    scene 119_s13 with Dissolve(0.3)
    play sound "sound_effects/run.mp3" volume 0.3
    scene 119_s13 with vpunch
    rohan "I... I'm sorry, darling!"
    perception "The man suddenly bolts away without looking back. The bandits are so surprised they don't even try to stop him. Yasmine stares after her husband, her face crumbling."
    stop sound fadeout 1.0
    scene 119_s14 with  Dissolve(1.0)
    yasmine "Rohan! Y-You're leaving me?! Rohan!"
    scene 119_s15 with  Dissolve(1.0)
    bandit "*laughs* Fuckin' ferret just ran off!"
    bandit "I almost feel bad for you. Married to a coward and a deadbeat. Must be hard."
    scene 119_s12 with  Dissolve(1.0)
    yasmine "J-Just kill me. I won't work for you."
    scene 119_s11 with dissolve
    bandit "Oh no. We have better plans for you. Mr. Victor pays well, especially for the pretty ones with spunk."
    scene 119_s8 with dissolve
    yasmine "Get your hands off of me! I'll scream! I'll—"
    bandit "Scream all you want. No one's coming."
    call screen scene118_choice04 with dissolve

default mc_killed_reham_counted = False
label scene118_choice04_op1:
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 4
    if mc_karma <= 0:
        $ mc_karma = 1
    $ karma_less = True
    show screen stat_change with easeinright
    $ mc_killed_reham = True
    $ mc_killed_reham_counted = True
    scene 119_s16 with Fade(1.0,1.0,1.0)
    perception "Behind you, Yasmine screams. The sound follows you out of the alley and into the bright, noisy market, where no one notices and no one cares."
    m "Mmmmm~ It's sho good!"
    hide screen stat_change with easeoutright
    $ karma_less = False
    reham "Don't speak with food in your mouth. And please don't shove the whole thing at once..."
    scene 119_s17 with Dissolve(1.0)
    reham "Ah, [mc]. Where did you go to?"
    mc "I thought I saw something. It's all good."
    reham "Alright. Come on, through here."
    stop music fadeout 1.0 
    scene 119_s18 with Fade(1.0,1.0,1.0)
    play music "wind.mp3" fadein 1.0 loop
    reham "Here we are! This is it. The house I grew up in."
    reham "Hold on a moment, please."
    scene 119_s19 with Dissolve(1.0)
    reham "*knock* *knock*"
    m "Maybe they're not here?"
    reham "Can't be... my mother is a stay-at-home mom. She's always here at this time of day."
    mc "Maybe she's out visiting friends?"
    play sound "sound_effects/doors/door_open3.mp3"
    scene 119_s20 with Dissolve(1.0)
    man_in_house "Yes? Can I help you?"
    scene 119_s21 with dissolve
    reham "Umm... sorry, but who are you? I don't—"
    scene 119_s20 with dissolve
    man_in_house "Who are YOU?!"
    scene 119_s21 with dissolve
    reham "Excuse me, but this is my parents' house. I grew up here."
    scene 119_s20 with dissolve
    man_in_house "Your parents? ...Oh. You must be Rohan's daughter. Reham, isn't it? He mentioned you. Said you were off in Irda, making something of yourself."
    man_in_house "Sorry. I didn't mean to snap. It's just... Rohan sold the house three months ago. I bought it fair and square."
    scene 119_s21 with dissolve
    reham "Sold it?! B-But why? Where are they now?"
    scene 119_s20 with dissolve
    man_in_house "Couldn't tell ya. Last I heard, he was living west of here, near Gunther's tannery."
    scene 119_s21 with dissolve
    reham "I... *ahem* Thank you, sir. I appreciate the information."
    scene 119_s20 with dissolve
    man_in_house "Anytime. And oh, say hello to your father for me. He still owes me from our last poker match."
    scene 119_s21 with dissolve
    reham "Right..."
    play sound "sound_effects/doors/door_close3.mp3"
    scene 119_s22 with Dissolve(1.0)
    mc "You really think he sold it?"
    scene 119_s23 with dissolve
    reham "I guess so. He... he wasn't exactly good with coin. He liked to gamble."
    scene 119_s22 with dissolve
    m "That's awful. I'm sorry, Reham."
    mc "Let's go look for them. West of here, he said"
    scene 119_s23 with dissolve
    reham "I think... I think I know where they might have gone. There's a neighborhood with cheaper housing close by."
    scene 119_s22 with dissolve
    scene 119_s24 with Fade(1.0,1.0,1.0)
    mc "Al-Kins... Zenis... Any of these families you know?"
    scene 119_s25 with dissolve
    reham "No... No. None of them. This is the right district, but I don't recognize—"
    scene 119_s26 with Dissolve(1.0)
    reham "Here! This one!"
    m "Is this it?"
    reham "Yes! That's my family's name! That's my mother's name—Yasmine."
    mc "Hopefully they're here."
    scene 119_s27 with Dissolve(1.0)
    reham "Please, please, please..."
    rohan "Please leave me alone or I will call the guards!"
    rohan "I've done nothing wrong! I just need more time! Just give me two weeks!"
    reham "Father?!"
    rohan "W-Who's there? I don't know you. I don't owe you anything—"
    reham "It's me, Father. Reham."
    play sound "sound_effects/doors/door_open4.mp3"
    scene 119_s28 with Dissolve(1.0)
    rohan "Huh?"
    reham "Father..."
    play sound "sound_effects/clothing_rustle.mp3"
    scene 119_s29 with vpunch
    rohan "My dear... I-I didn't know you were visiting."
    scene 119_s30 with Dissolve(1.0)
    perception "She hugs him tightly."
    empathy "Knowing Rohan, you don't feel anything from this reunion."
    reham "*sniff* Sorry for not telling you in advance."
    rohan "No... no. It's fine. It's more than fine. Come inside. Gods, I missed you so much."
    rohan "Errm... Are these your friends?"
    reham "Yes. They're good people."
    rohan "Please, come in."
    stop music fadeout 1.0 
    scene 119_s31 with Fade(1.0,0.5,1.0)
    rohan "Oh, dear. Look at you. So beautiful, just like your mother."
    scene 119_s32 with dissolve
    reham "*giggles* Thank you. Speaking of which—where is she?"
    scene 119_s31 with dissolve
    rohan "She's... she's ermm..."
    scene 119_s32 with dissolve
    reham "Father? Where's mother?"
    scene 119_s31 with dissolve
    play music "tense/lie.mp3" fadein 1.0 loop
    rohan "*chuckles* Well... it's complicated, dear. She's... she's fine, I assure you. Just not... here. Right now. At this moment."
    scene 119_s33 with dissolve
    reham "Where's Mother? Why are you avoiding my question?!"
    scene 119_s34 with dissolve
    rohan "Now, Reham, there's no need to shout. What if the neioghbours hear—"
    scene 119_s33 with vpunch
    reham "Did something happen to her?! Is she hurt?! Is she sick?! Father, if something happened and you're not telling me—"
    scene 119_s34 with dissolve
    rohan "No, no... Gods, no. Nothing like that. She's not hurt. She's just..."
    scene 119_s33 with dissolve
    reham "Then WHY aren't you answering my question?!"
    reham "Is it... is it them? Those debt collectors that were always after us?"
    scene 119_s34 with dissolve
    rohan "H-How did yo—? I mean... No. Nothing like that. I paid them. Every last copper."
    scene 119_s33 with vpunch
    reham "You... you idiot! How could you let that happen?! I KNEW it! I knew this would happen! I told you to stop gambling! I begged you! Mother begged you! But you never listen! You never—"
    scene 119_s34 with dissolve
    rohan "And I did! I stopped! Years ago! I haven't touched a card or a die since you left! I swear it on my life!"
    scene 119_s33 with dissolve
    reham "Then WHERE is she?! If you're so reformed, if you're so blameless, then where is my mother?!"
    scene 119_s34 with dissolve
    rohan "I... You can't speak to me like that, young woman! I am still your father! This is still my house!"
    scene 119_s33 with vpunch
    reham "FUCK YOU! I want you to go out there and get her back! NOW!"
    scene 119_s34 with vpunch
    rohan "Shut your mouth! Don't you raise your voice at me! You don't know what I've been through! You don't know what it's cost!"
    scene 119_s46 with dissolve
    m "[mc]... should we do something? I hate seeing Reham like this."
    mc "..."
    call screen scene118_choice05 with dissolve

label scene118_choice05_op2:
    $ mc_sided_reham = True
    scene 119_s113 with Dissolve(1.0)
    mc "Reham is right."
    mc "Your wife is in danger because of your mistakes. And now she's paying the price while you hide here."
    scene 119_s35 with dissolve
    rohan "You don't understand! Those thugs... they're not just simple thugs—they work for Victor! I-I can't just barge in there!"
    scene 119_s113 with dissolve
    mc "Still. Standing here and telling your daughter she's wrong for wanting her mother back is terrible of you."
    scene 119_s36 with dissolve
    reham "...Thank you."
    scene 119_s35 with dissolve
    rohan "Ughnn... I'm not going anywhere! You don't understand, honey. Th-They're killers! They have no mercy!"
    scene 119_s33 with dissolve
    reham "Fine. Then I'll go back and get her myself since you don't have the balls to do it."
    scene 119_s37 with Dissolve(1.0)
    rohan "Wait! Honey, please! You don't know what you're walking into!"
    reham "Don't even start! I WILL get her back. At least then you'd have something real to cry about."
    scene 119_s40 with Dissolve(1.0)
    rohan "Reham! REHAM! Wait for me!"
    perception "Rohan follows after her and both vanish into the darkness. Unlikely to return."
    scene 119_s114 with Dissolve(1.0)
    $ minthra_love += 10
    minthra "My, my. Aren't you the master strategist? Cunning will take you far. Not only will these two die, but the commotion is likely to bring in many guards."
    minthra "You didn't lift a finger, and yet you have orchestrated a slaughter. Many souls delivered to me without a drop of blood on your hands."
    minthra "Good work, my champion. Very good work."
    scene 119_s38 with dissolve
    m "[mc]?! W-What do we do?! They're gone!"
    scene 119_s40 with dissolve
    call screen scene118_choice06 with dissolve

label scene118_choice05_op3:
    scene 119_s113 with Dissolve(1.0)
    mc "Reham. Listen to your father."
    scene 119_s36 with dissolve
    reham "What?! You're taking his side?!"
    scene 119_s113 with dissolve
    mc "Look at him. He's not a villain. He's a broken man who's lost everything."
    mc "And now his daughter is screaming at him, and he doesn't know how to fix any of it."
    mc "Whatever happened to your mother... I'm sure he's planning how to fix it right now. Right?"
    scene 119_s35 with dissolve
    rohan "I..."
    scene 119_s36 with dissolve
    reham "You know what? Screw all of you. I'm going there myself."
    scene 119_s37 with Dissolve(1.0)
    rohan "Wait! Honey, please! You don't know what you're walking into! They're killers!"
    reham "Don't even start! I WILL get her back, or I die trying. At least then you'd have something real to cry about."
    rohan "Reham! REHAM! Wait for me!"
    scene 119_s40 with Dissolve(1.0)
    perception "Rohan follows after her and both vanish into the market. Unlikely to return."
    scene 119_s114 with Dissolve(1.0)
    $ minthra_love += 10
    minthra "My, my. Aren't you the master strategist? Cunning will take you far. Not only will these two die, but the commotion is likely to bring in many guards."
    minthra "You didn't lift a finger, and yet you have orchestrated a slaughter. Many souls delivered to me without a drop of blood on your hands."
    minthra "Good work, my champion. Very good work."
    scene 119_s38 with dissolve
    m "[mc]?! W-What do we do?! They're gone!"
    scene 119_s40 with dissolve
    call screen scene118_choice06 with dissolve

label scene118_choice06_op1:
    stop music fadeout 1.0
    scene 119_s118 with dissolve
    mc "(Wait, what the hell I doing?! Are you influencing my thoughts, Minthra?)"
    mc "(I won't let them get hurt!)"
    scene 119_s42 with Dissolve(0.3)
    play sound "sound_effects/body/body_falling2.mp3"
    scene 119_s42 with vpunch
    sensation "A sudden, agonizing pain explodes through your entire body. It feels like a knife twisting in your stomach. Your legs give out beneath you."
    mc "AGGHHHHH!"
    m "[mc]!?"
    minthra "I won't let you ruin this. Sleep."
    scene black with Dissolve(5.0)
    sensation "The world spins violently. Then, darkness swallows you whole."
    jump scene119_2

label scene118_choice06_op2:
    $ mc_intended_reham = True
    scene 119_s39 with dissolve
    mc "We won't do anything. They made their choice."
    scene 119_s38 with dissolve
    m "B-But Reham! What if she gets hurt?! She helped us cross the desert! She—"
    scene 119_s39 with dissolve
    mc "She made her choice, Maia. I'm not responsible for her decisions."
    scene 119_s40 with dissolve
    m "..."
    scene 119_s38 with dissolve
    m "As you wish."
    scene 119_s39 with dissolve
    mc "Now that we've got a house to our selves... let's rest. We've been on the road for days. We've earned it."
    scene 119_s40 with dissolve
    m "..."
    jump scene119_2

label scene119_2:
    if not mc_intended_reham:
        scene 119_s43 with vpunch
        mc "Hah!?"
        scene 119_s44 with Dissolve(1.0)
        m "[mc]?!"
        scene 119_s45 with dissolve
        mc "Nfhnn... Where's Reham?! Is she back?!"
        scene 119_s44 with dissolve
        m "She's... still not back yet."
        scene 119_s45 with dissolve
        mc "Dammit!"
        mc "Fuck! My head!"
        mc "I'm so sorry, Maia... I didn't mean for this to happen. I tried to stop her, I really did!"
        scene 119_s44 with dissolve
        m "I know, [mc]. I don't blame you. You tried to help, but then you suddenly collapsed..."
        scene 119_s45 with dissolve
        mc "No! That's not enough! I should have gone after her! I should have—"
        scene 119_s44 with dissolve
        m "Please calm down... You might hurt yourself again."
        scene 119_s45 with dissolve
        mc "Reham... I'm so fucking sorry..."
        scene 119_s44 with dissolve
        m "I made you some food. I didn't find much in the cabinets, but I made two sandwiches."
        scene 119_s45 with dissolve
        mc "How long was I out?"
        scene 119_s44 with dissolve
        m "About four hours."
        scene 119_s45 with dissolve
        mc "*sigh* We missed the meeting with Alex... She's going to be furious."
        scene 119_s44 with dissolve
        m "Eat first, alright? You need your strength, [mc]."
        scene 119_s45 with dissolve
        mc "...Yeah, alright."
        scene 119_s44 with dissolve
        m "Come on, I'll help you stand up."
        scene 119_s45 with dissolve

    else:
        scene 119_s43 with Fade(1.0,1.0,1.0)
        mc "Mhnnn..."
        scene 119_s44 with Dissolve(1.0)
        m "[mc]?"
        scene 119_s45 with dissolve
        mc "Ahh... Maia."
        mc "How long did I sleep for?"
        scene 119_s44 with dissolve
        m "About four hours."
        scene 119_s45 with dissolve
        mc "Shit... I missed the meeting with Alex. She's gonna be furious."
        scene 119_s44 with dissolve
        m "I-I made you some food for you, [mc]! I didn't find much, but I made two sandwiches."
        scene 119_s45 with dissolve
        mc "*chuckles* Thank you."
        scene 119_s44 with dissolve
        m "Of course."
        if maia_love <= 50:
            m "And... I'm sorry for yelling at you before you collapsed. I know you have a plan for all of this. I'll always be with you... even if you don't like me very much."
        else:
            m "And... I'm sorry for yelling at you before you collapsed. I know you have a plan for all of this. I'll always be with you... I'll always love you, [mc]."
        scene 119_s45 with dissolve
        mc "You're a smart girl, Maia. You'll survive long."
    scene 119_s47 with Dissolve(2.0)

    mc "..."
    mc "(Time to carry on.)"
    jump scene120
    
label scene118_choice04_op2:
    stop music fadeout 1.0
    scene 119_s48 with Dissolve(1.0)
    mc "You heard the lady. Hands off."
    play music "tense/desert_battle.mp3" fadein 1.0 loop
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 119_s49 with Dissolve(1.0)
    bandit "Who the fuck are you?!"
    bandit "This is none of your business, foreigner."
    bandit "Usually I would gut you right on the spot, but I'm feeling rather merciful today. Walk away. Now."
    scene 119_s50 with dissolve
    hide screen stat_change with easeoutright
    $ karma_more = False
    mc "I'm not going anywhere. Let her go. The debt's between you and her husband, she's got nothing to do with it."
    scene 119_s49 with dissolve
    bandit "Or what? What can you possibly do?"
    bandit "Come on. I love those who act like heroes, they always end up in the same ditch."
    scene 119_s48 with Dissolve(1.0)
    if mc_owe_minthra:
        minthra "They offer you their lives on a platter. Take them. Don't hold back. You promised me an act in return for helping you. You cannot refuse."
    else:
        minthra "They offer you their lives on a platter. Take them. Don't hold back."
    logic "Brother, it's generally not a good idea to start trouble right after arriving to a new city."
    call screen scene118_choice07 with dissolve

label scene118_choice07_op1:
    scene 119_s51 with Dissolve(1.0)
    mc "..."
    bandit "What the fuck? I thought you were acting brave, but you're just a dumbass. One man against three? You've got a death wish."
    bandit "Get him, boys. Keep the girl in your sights—she tries to run, break her legs."
    scene 119_s52 with dissolve
    bandit "ARGGHH!"
    call screen scene118_choice08 with dissolve

label scene118_choice08_op1:
    if not mc_owe_minthra:
        $ mc_attack_yasmine_bandits = True
        play sound "sound_effects/punch5.mp3"
        scene 119_s53 with Dissolve(0.3)
        scene 119_s53 with vpunch
        perception "You move unnaturally fast. Your body becomes a blur. The bandit doesn't even have time to reach you. Your fist connects with his face before he can blink."
        scene 119_s55 with dissolve
        bandit "W-What?! Get up, you useless sack of shit! GET UP!"
        scene 119_s56 with dissolve
        mc "He won't be waking up any time soon."
        scene 119_s57 with dissolve
        bandit "R-Retreat! This aint over! I remember your face, foreighner!"
        jump scene119_3
    else:
        minthra "Your heart is in my palm. You promised. Don't disobey me."
        call screen scene118_choice08 with dissolve

label scene118_choice08_op2:
    $ mc_killed_yasmine_bandits = True
    play sound "sound_effects/punch6.mp3"
    scene 119_s54 with Dissolve(0.3)
    scene 119_s54 with vpunch
    perception "You move unnaturally fast. Your body becomes a blur. The bandit doesn't even have time to scream. Your fist connects with his face before he can blink."
    scene 119_s56 with dissolve
    bandit "..."
    scene 119_s55 with dissolve
    bandit "Wh... what the hell was that?! That wasn't... what ARE you?!"
    scene 119_s56 with dissolve
    mc "Who's next?"
    scene 119_s57 with vpunch
    bandit "H-He's a devil! Retreat! RETREAT!"
    bandit "This... this isn't over! Mr. Victor will hear about this! You'll regret it!"
    jump scene119_3

label scene118_choice07_op2:
    if not mc_owe_minthra:
        scene 119_s58 with Dissolve(1.0)
        mc "I'll pay off their debt. How much is it?"
        scene 119_s59 with dissolve
        bandit "What? Do you know these people?"
        scene 119_s58 with dissolve
        mc "Never met them before in my life."
        scene 119_s59 with dissolve
        bandit "Then why the hell do you care so much? You don't know them, so why stick your neck out for strangers?"
        scene 119_s58 with dissolve
        mc "Just tell me how much they owe."
        scene 119_s59 with dissolve
        bandit "*laughs* If you fancy playing the hero, it's seven hundred."
        scene 119_s58 with dissolve
        mc "Seven hundred... so, seven gold coins?"
        scene 119_s59 with dissolve
        bandit "You can count! Congratulations."
        call screen scene118_choice09 with dissolve
    else:
        minthra "Your heart is in my palm. You promised. Don't disobey me."
        call screen scene118_choice07 with dissolve

label scene118_choice09_op1:
    if mc_coin >= 700:
        $ mc_coin -= 700
        $ mc_paid_yasmine_debt = True
        scene 119_s58 with dissolve
        mc "I have the coin. I'll pay it all."
        scene 119_s60 with Dissolve(1.0)
        bandit "Wait... you're doing it? For a woman you don't know? For a deadbeat husband who ran?"
        scene 119_s61 with dissolve
        mc "Yeah?"
        scene 119_s60 with dissolve
        bandit "You're fucking weird, man. Actually starting to creep me out."
        bandit "But whatever. Debt's cleared. You're lucky to have a rich guy stumbling on you, sweetheart. Try not to marry another coward next time."
        scene 119_s57 with Dissolve(2.0)
        perception "The man takes your coin and leaves. His men follow behind. Yasmine remains still, her whole body trembling. She doesn't seem to understand what just happened."
        jump scene119_3
    else:
        mc "(I don't have that amount on me.)"
        call screen scene118_choice09 with dissolve

label scene118_choice09_op2:
    $ mc_gave_aldwin_bracelet = True
    $ mc_paid_yasmine_debt = True
    scene 119_s58 with dissolve
    mc "I'll give you this bracelet."
    scene 119_s59 with dissolve
    bandit "You think Mr. Victor sent us here for some shitty jewelry? Coin or nothing."
    scene 119_s61 with Dissolve(1.0)
    mc "I checked it myself. It's authentic gold. It has to be worth more than their debt."
    scene 119_s60 with dissolve
    bandit "...Shit. Fine. I'll take it."
    bandit "But if it's worth any less, we'll be paying you a visit. And if we can't find you, we'll come for these folks."
    scene 119_s61 with dissolve
    mc "Deal."
    scene 119_s57 with Dissolve(1.0)
    perception "The man takes the bracelet and leaves. His men follow, grumbling but relieved. Yasmine watches them go, then turns to you with an expression of stunned gratitude."
    jump scene119_3
    
label scene118_choice09_op3:
    scene 119_s58 with dissolve
    mc "Forget it. I'll just deal with you."
    scene 119_s51 with Dissolve(1.0)
    bandit "Dumbass! You could've just walked away! But no! You had to be a hero!"
    bandit "Oh well... Get him, boys! Make it painful!"
    scene 119_s52 with dissolve
    bandit "ARGGHH!"
    call screen scene118_choice08 with dissolve

label scene119_3:
    stop music fadeout 1.0 
    scene 119_s62 with Fade(0.5,0.5,0.5)
    play music "wind.mp3" fadein 1.0 loop
    yasmine "Who are you? Why did you risk your life for me?"
    scene 119_s63 with dissolve
    call screen scene119_choice01 with dissolve

label scene119_choice01_op1:
    mc "I couldn't let them take you. I saw what was happening, and I had to help."
    scene 119_s62 with dissolve
    yasmine "Thank you. Truly. You saved me. Who knows what those thugs might have done if they'd taken me... "
    scene 119_s63 with dissolve
    mc "I'm glad you didn't have to find out."
    scene 119_s62 with dissolve
    yasmine "Me too. How can I possibly return the favor? I know it's not enough, but I can't just let you walk away."
    yasmine "We... we don't have much. My husband's debts have taken almost everything. But if you aren't busy, come with me. I can treat you to some cinnamon tea."
    scene 119_s63 with dissolve
    mc "Come where?"
    scene 119_s64 with Dissolve(1.0)
    yasmine "Our home! It's right here. Please, don't be shy. I would feel terrible if I couldn't at least repay your kindness."
    if mc_killed_yasmine_bandits:
        yasmine "Come before the guards show up and find this huge puddle of blood with only the two of us standing nearby."
        scene 119_s63 with Dissolve(1.0)
        mc "Ah, right. Sorry for ruining your... neighborhood."
        scene 119_s62 with dissolve
        yasmine "Pay no mind to it. They deserved it. The guards will clean up when they arrive... hopefully not a week from now."
        scene 119_s63 with dissolve
    else:
        scene 119_s63 with Dissolve(1.0)
    call screen scene119_choice02 with dissolve

label scene119_choice01_op2:
    mc "Those annoying little shits? I had to get rid of them. They were getting on my nerves."
    scene 119_s62 with dissolve
    yasmine "*chuckles* I don't blame you. If only I had your strength..."
    yasmine "They've been harassing us for months and my husband just takes it. I wanted to claw their eyes out, but..."
    yasmine "But... there has to be more, right? Forgive me, I don't mean to presume, but people don't get involved in life-or-death situations without expecting something in return."
    scene 119_s63 with dissolve
    mc "No, seriously. I just couldn't stand them. Three armed men against one woman? It was pathetic."
    scene 119_s62 with dissolve
    yasmine "I see... How about you come with me? I can treat you to some cinnamon tea."
    scene 119_s63 with dissolve
    mc "Come where?"
    scene 119_s64 with Dissolve(1.0)
    yasmine "Our home! It's right here. Please, don't be shy. I would feel terrible if I couldn't at least repay your kindness."
    if mc_killed_yasmine_bandits:
        yasmine "Come before the guards show up and find this huge puddle of blood with only the two of us standing nearby."
        scene 119_s63 with Dissolve(1.0)
        mc "Ah, right. Sorry for ruining your... neighborhood."
        scene 119_s62 with dissolve
        yasmine "Pay no mind to it. They deserved it. The guards will clean up when they arrive... hopefully not a week from now."
        scene 119_s63 with dissolve
    else:
        scene 119_s63 with Dissolve(1.0)
    call screen scene119_choice02 with dissolve

label scene119_choice01_op3:
    $ mc_want_yasmine_ring = True
    mc "I expect a reward for my trouble."
    scene 119_s62 with dissolve
    yasmine "N-Naturally. Please, come with me. We don't have much, but I have a ring."
    yasmine "I've hidden it where the thugs couldn't find it."
    if mc_paid_yasmine_debt:
        yasmine "It won't sell for as much as you paid for us today, I still can't believe you did that, but I swear it's the only valuable thing we have left."
    scene 119_s63 with dissolve
    mc "Come where?"
    scene 119_s64 with Dissolve(1.0)
    yasmine "Our home! It's right here. Please, don't be modest. I hid my ring very well so none of these thugs could steal it."
    scene 119_s62 with Dissolve(1.0)
    yasmine "Well... it's not only those thugs I hid it from. My husband, you see. He's a... *sigh* forget it."
    yasmine "I'll give the ring to you. It's all that we have."
    if mc_killed_yasmine_bandits:
        yasmine "Come before the guards show up and find this huge puddle of blood with only the two of us standing nearby."
        scene 119_s63 with dissolve
        mc "Ah, right. Sorry for ruining your... neighborhood."
        scene 119_s62 with dissolve
        yasmine "Pay no mind to it. They deserved it. The guards will clean up when they arrive... hopefully not a week from now."
    scene 119_s63 with dissolve
    call screen scene119_choice02 with dissolve

label scene119_choice02_op1:
    mc "Lead the way."
    mc "(Reham is responsible. She can take care of Maia for a while.)"
    scene 119_s62 with dissolve
    yasmine "Over here... um..."
    scene 119_s63 with dissolve
    mc "[mc]."
    scene 119_s62 with dissolve
    yasmine "A pleasure to meet you, [mc]. I'm Yasmine. I wish it were under better circumstances, but perhaps fate knows what it's doing."
    scene 119_s63 with dissolve
    jump scene119_4

label scene119_choice02_op2:
    if mc_want_yasmine_ring:
        mc "You know what? Keep the ring. I've got places to be."
    else:
        mc "Forget it. I have places to be."
    scene 119_s62 with dissolve
    yasmine "Please. I insist."
    scene 119_s63 with dissolve
    mc "I already told you, I can't stay."
    scene 119_s62 with dissolve
    yasmine "Well, I'm insisting."
    yasmine "Just for a cup of tea. It won't take but a moment."
    scene 119_s63 with dissolve
    mc "You're not gonna let me go, are you?"
    scene 119_s62 with dissolve
    yasmine "*giggles* Not at all."
    scene 119_s63 with dissolve
    mc "*sigh* Alright. But only for a couple of minutes."
    scene 119_s62 with dissolve
    yasmine "I won't take too much of your time, um..."
    scene 119_s63 with dissolve
    mc "[mc]."
    scene 119_s62 with dissolve
    yasmine "A pleasure to meet you, [mc]. I'm Yasmine. I wish it were under better circumstances, but perhaps fate knows what it's doing."
    scene 119_s63 with dissolve
    jump scene119_4
    
label scene119_4:
    stop music fadeout 1.0 
    scene 119_s65 with Fade(1.0,1.3,1.3)
    play music "kitchen.mp3" fadein 1.0 volume 0.7 loop
    yasmine "There we are. Please, make yourself comfortable."
    scene 119_s66 with Dissolve(1.0)
    perception "The interior is small but kept. Hand-sewn curtains filter the afternoon light. A worn rug covers the stone floor. Dried flowers in a chipped vase. Everything is in its place except the man of the house."
    yasmine "Have a seat. I'll make the tea."
    scene 119_s67 with Fade(0.5,0.5,0.5)
    perception "She lights a fire, fills a clay pot with water, and sets it to boil. When the water begins to bubble, she adds the dark tea leaves then reaches for a small jar of cinnamon."
    mc "Smells really good."
    scene 119_s68 with Dissolve(1.0)
    yasmine "It tastes even better."
    scene 119_s69 with Dissolve(1.0)
    yasmine "Go on. It's my own special recipe. I haven't met anyone who didn't like it."
    scene 119_s70 with dissolve
    mc "*sip*"
    stop music fadeout 1.0
    mc "So, your husband..."
    play music "side_event6.mp3" fadein 1.0 volume 0.7 loop
    scene 119_s69 with dissolve
    yasmine "My husband? That coward who ran and left me with them?"
    yasmine "*scoff* I still can't believe he did that. I keep replaying it in my head—the way he looked at me, and then just... vanished. Like I was nothing."
    yasmine "Apparently, all our years together were worth less than his own skin."
    scene 119_s70 with dissolve
    mc "Where is he now?"
    scene 119_s69 with dissolve
    yasmine "Hiding somewhere I assume. He has a talent for disappearing when things get difficult."
    yasmine "He'll be back eventually. There's nowhere else for him to go."
    scene 119_s70 with dissolve
    mc "You sure they won't be after him?"
    scene 119_s69 with dissolve
    if mc_attack_yasmine_bandits or mc_killed_yasmine_bandits:
        yasmine "After what you did? They'll need time before someone comes knocking again. For a while, at least, they'll keep their distance."
        yasmine "Until then... maybe we can go somewhere else. It doesn't matter if we end up living in a tent. As long as they lose our trail, we'll be better off than we are here."
    else:
        yasmine "He's off the hook now that you paid his debt. As for how long it takes him to get a new one..."
        yasmine "I don't know. A month? A week? He always finds a way."
    scene 119_s71 with Dissolve(1.0)
    yasmine "Gods... what do I even tell him? How do I look him in the eyes again after what he did today?"
    yasmine "Do I pretend it didn't happen? Do I scream? Do I just... say nothing?"
    scene 119_s72 with dissolve
    call screen scene119_choice03 with dissolve
    
label scene119_choice03_op1:
    mc "Be straight with him. He has to stop gambling completely."
    scene 119_s71 with dissolve
    yasmine "Ugh... if only that worked. We've already had this conversation, [mc]. Many times."
    yasmine "I've packed my bags and walked out the door, and every time he chased after me, tears in his eyes, swearing on his mother's grave that this time would be different."
    scene 119_s72 with dissolve
    mc "And he still refuses to stop?"
    scene 119_s71 with dissolve
    yasmine "Yes."
    jump scene119_4_2

label scene119_choice03_op2:
    $ mc_told_yasmine_leave = True
    mc "You don't have to deal with this. It's unfair to you."
    scene 119_s71 with dissolve
    yasmine "I know..."
    scene 119_s72 with dissolve
    mc "I'm serious. If he doesn't stop, you should leave him."
    scene 119_s71 with dissolve
    yasmine "Leave him? And go where afterwards? I have no family except the one I married into."
    yasmine "What would I even do? Beg in the market? Sell what little scraps we have left? ...It's not that simple."
    jump scene119_4_2
    
label scene119_choice03_op3:
    $ mc_told_yasmine_stay = True
    mc "I think you two should make up."
    scene 119_s71 with dissolve
    yasmine "Make up? After what he did today?"
    scene 119_s72 with dissolve
    mc "You still need each other. Do you have anyone else to rely on? Family? Friends who would take you in if things got worse?"
    yasmine "*sigh* I don't... No. No family. No one wants to be associated with a gambler's wife. It's just me and him. It's been just me and him for years."
    yasmine "Still. He... he shouldn't be doing this. It could be so much better."
    jump scene119_4_2

label scene119_4_2:
    scene 119_s69 with Dissolve(1.0)
    yasmine "I'm sorry, [mc]. This is supposed to be a nice gesture to thank you for what you did."
    yasmine "*chuckles* Forgive me for ruining the tea with my whining. You didn't sign up to hear an old woman's troubles when you stepped into my house."
    scene 119_s70 with dissolve
    mc "What are you talking about? This tea is the best I've ever had."
    scene 119_s69 with dissolve
    yasmine "I'm glad."
    scene 119_s70 with dissolve
    call screen scene119_choice04 with dissolve

label scene119_choice04_op1:
    $ mc_listened_yasmine = True
    $ yasmine_love += 10
    mc "You shouldn't bury your problems like that. It's better to talk about them."
    scene 119_s73 with Dissolve(1.0)
    yasmine "A-Are you sure? I don't understand why you would care so much."
    scene 119_s74 with dissolve
    call screen scene119_choice05 with dissolve

label scene119_choice04_op2:
    mc "If you don't want to talk about it, then that's your choice. I'm not here to pry into your life."
    mc "Let's just enjoy the tea."
    scene 119_s69 with dissolve
    yasmine "*chuckles* Right. The tea isn't getting any warmer."
    scene 119_s70 with dissolve
    scene black with Dissolve(1.0)
    perception "Yasmine laughs as you begin chugging the tea like a beer."
    scene 119_s70 with Dissolve(1.0)
    mc "Mmm~ Thank you for the tea, Yasmine. It's time for me to leave."
    mc "I have a few... friends that I should have been with by now. They're probably wondering where I vanished to."
    scene 119_s69 with dissolve
    yasmine "Of course. Please, don't let me hold you."
    if mc_want_yasmine_ring:
        yasmine "Here's the ring I promised you."
        yasmine "And remember, my house is yours. The debt I owe you is bigger than any tea cup or cheap ring could hold."
    else:
        yasmine "And remember, my house is yours. The debt I owe you is bigger than any tea cup could hold."
    scene 119_s70 with dissolve
    jump scene119_6

label scene119_choice05_op1:
    mc "Because you deserve better. I barely know you, but I can tell how incredible you are."
    mc "You're strong, you're honest, and you're very kind for inviting me to your house and treating me."
    scene 119_s73 with dissolve
    yasmine "[mc]..."
    scene 119_s74 with dissolve
    mc "Your husband, on the other hand..."
    mc "Don't take this the wrong way, but he doesn't deserve you."
    scene 119_s73 with dissolve
    yasmine "No offense taken. And I know what you mean. I've thought the same thing myself, on the bad nights."
    yasmine "But it's easier to say than to act, [mc]. Despite his habits... he still earns some coin here and there. Enough to keep us fed, *scoff* barely."
    jump scene119_5

label scene119_choice05_op2:
    $ yasmine_love += 10
    scene 119_s75 with Dissolve(1.0)
    empathy "You reach across the table. Your fingers brush hers. She looks up at you startled. Then, slowly, a smile spreads across her face."
    scene 119_s76 with dissolve
    yasmine "*chuckles* [mc]?"
    scene 119_s75 with dissolve
    mc "You don't have to bottle it all up. Talk to me. I'm listening."
    yasmine "..."
    scene 119_s76 with dissolve
    yasmine "I... I really hate it, [mc]. I hate this so much."
    yasmine "We had it all once. A big house, it had a garden with a fig tree and a fountain. Rohan had a good job. I had a nice neighborhood, friends who came over for tea, a life I was proud of."
    yasmine "But it was all gone. All went to pay for my husband's awful 'hobby'."
    scene 119_s75 with dissolve
    mc "And you're still with him despite it all."
    scene 119_s76 with dissolve
    yasmine "Yes. Because I keep thinking maybe tomorrow he will change. Maybe something good will happen."
    yasmine "Maybe... maybe the man I married is still in there somewhere."
    yasmine "But it seems I've been living in denial."
    jump scene119_5

label scene119_5:
    scene 119_s71 with Dissolve(1.0)
    yasmine "*sigh* What do I do, [mc]? This is getting larger than I can handle."
    scene 119_s72 with dissolve
    mc "Hmm?"
    scene 119_s71 with dissolve
    yasmine "What if he gets in too much debt that they stop asking anymore and begin threatening immediately?"
    yasmine "What if next time, it's not thugs in an alley, it's men breaking down our door in the middle of the night?"
    yasmine "I am so lost... If I leave him, I leave with nothing to my name. If I stay, I risk my life every time he makes a bet."
    scene 119_s72 with dissolve
    call screen scene119_choice06 with dissolve

label scene119_choice06_op1:
    $ mc_told_yasmine_stay = False
    $ mc_told_yasmine_leave = True
    mc "Leave him. He did something today that can't be fixed. If you stay, you're gambling too."
    scene 119_s73 with dissolve
    yasmine "But where would I go? What would I—"
    scene 119_s74 with dissolve
    mc "You're strong. You faced down three armed men. You built a life once, you can build another one without him."
    scene 119_s69 with dissolve
    yasmine "...You know what? You're right."
    yasmine "I'll... I'll tell him! Once he finally shows his pathetic face."
    yasmine "T-Thank you, [mc]. I feel much better now. *chuckles* Talking to you feels so good for some reason."
    scene 119_s70 with dissolve
    mc "You're welcome."
    jump scene119_6

label scene119_choice06_op2:
    $ mc_told_yasmine_stay = True
    $ mc_told_yasmine_leave = False
    mc "Stay with him. But only if he changes."
    scene 119_s73 with dissolve
    yasmine "And if he doesn't?"
    scene 119_s74 with dissolve
    mc "You leave. But before that, start saving as much coin as you can."
    scene 119_s73 with dissolve
    yasmine "A-Alright. I'll give him another chance. It's all I do anyway."
    yasmine "Thank you."
    scene 119_s74 with dissolve
    jump scene119_6

label scene119_6:
    scene 119_s77 with Dissolve(1.5)
    stop music fadeout 1.0 
    "*click*"
    yasmine "Hmm? He must be back. That pathetic little..."
    scene 119_s79 with Dissolve(0.3)
    play sound "sound_effects/doors/door_open4.mp3"
    scene 119_s79 with vpunch
    play music "wind.mp3" fadein 3.0 loop
    perception "She marches to the door and yanks it open. Rohan stands there, sweating and gasping for air."
    scene 119_s78 with dissolve
    rohan "Wh-What?! How are you here?!"
    scene 119_s79 with vpunch
    yasmine "How am I here?! Is that really the first thing you say to me?!"
    scene 119_s78 with dissolve
    rohan "N-No! I-I mean... I'm so glad you're here!"
    rohan "My beautiful darling, I'm so, so sorry for leaving you! I panicked, I—"
    scene 119_s79 with dissolve
    yasmine "You're sorry? Rohan, I don't think 'sorry' can fix this. Not this time."
    scene 119_s80 with Dissolve(1.0)
    rohan "Who's this?"
    scene 119_s81 with dissolve
    yasmine "This is the man who actually saved me."
    if mc_attack_yasmine_bandits or mc_killed_yasmine_bandits:
        yasmine "He fought them off right after you ran away like a coward."
    else:
        yasmine "He paid off your entire debt. All of it."
    scene 119_s80 with dissolve
    rohan "R-Really? But... {i}why?{/i}"
    rohan "Thank you, sir. I owe you a great debt."
    scene 119_s81 with dissolve
    yasmine "Him and many others."
    scene 119_s80 with dissolve
    stop music fadeout 1.0 
    scene 119_s82 with Fade(0.5,0.5,0.5)
    play music "kitchen.mp3" fadein 1.0 loop
    rohan "Buttercup, I'm sorry. Truly. This... this is it. I promise. I'll never gamble again."
    scene 119_s83 with dissolve
    yasmine "*sigh* I've heard those words so many times before..."
    mc "(What the hell am I doing here...)"
    scene 119_s82 with dissolve
    rohan "This is the last time you'll hear them! I swear on my mother!"
    scene 119_s83 with dissolve
    if mc_told_yasmine_leave:
        yasmine "[mc] finally opened my eyes, Rohan."
        yasmine "You will never change. You'll never become the man I fell in love with."
        scene 119_s82 with dissolve
        rohan "What are you saying?"
        scene 119_s83 with dissolve
        yasmine "I'm leaving you, Rohan. This is it."
        scene 119_s84 with dissolve
        rohan "What?! You can't! I... I need you! I promise I'll be better!"
        scene 119_s85 with dissolve
        yasmine "These are just words. I'm sorry... but I can't do this anymore."
        scene 119_s84 with dissolve
        rohan "{i}He{/i} told you to leave me?! What does he have to do with our marriage?!"
        scene 119_s85 with dissolve
        yasmine "He has everything to do with it. I wouldn't even be standing here if not for him."
        yasmine "He's more of a man than you will ever be."
        scene 119_s84 with vpunch
        rohan "Excuse me?! I am still your husband, woman! You will treat me with respect!"
    elif mc_told_yasmine_stay:
        yasmine "*sigh* I talked with [mc]. He told me to give you another chance."
        yasmine "So... should I? Should I give you one last chance, Rohan?"
        scene 119_s82 with dissolve
        rohan "Yes! I promise I'll be better! I swear!"
        scene 119_s83 with dissolve
        yasmine "I need more than words this time."
        scene 119_s82 with dissolve
        rohan "Fine. I won't leave the house for an entire week! We'll start managing our finances together!"
        rohan "If you see even a single copper missing... then you can leave. I won't stop you."
        scene 119_s83 with dissolve
        yasmine "...Last chance. Got it?"
        scene 119_s82 with dissolve
        rohan "Yes! Thank you, my love!"
    else:
        yasmine "I'm so torn apart..."
        yasmine "Should I give you one last chance, Rohan?"
        scene 119_s82 with dissolve
        rohan "Yes! I promise I'll be better! I swear!"
        scene 119_s83 with dissolve
        yasmine "I need more than words this time."
        scene 119_s82 with dissolve
        rohan "Fine. I won't leave the house for an entire week! We'll start managing our finances together!"
        rohan "If you see even a single copper missing... then you can leave. I won't stop you."
        scene 119_s83 with dissolve
        yasmine "...Last chance. Got it?"
        scene 119_s82 with dissolve
        rohan "Yes! Thank you, my love!"
    play sound "sound_effects/doors/door_open4.mp3"
    scene 119_s86 with Dissolve(1.0)
    yasmine "Hahh! R-Reham!?"
    scene 119_s87 with Dissolve(0.3)
    play sound "sound_effects/clothing_rustle.mp3"
    scene 119_s87 with vpunch
    perception "Reham leaps and throws her arms around Yasmine. The force of the embrace nearly knocks Yasmine off her feet."
    yasmine "Dear, I'm so glad to see you again. So glad. I thought... after everything, I thought you might not come back."
    reham "*sniff* I missed you so much, Mother. Every day."
    scene 119_s89 with Dissolve(1.0)
    rohan "Reham? I-I thought you were out in Irda making coin. You didn't send word, I would have prepared something—"
    scene 119_s88 with dissolve
    reham "A lot of things happened, Father. More than I can explain right now. But... I'm back."
    scene 119_s89 with dissolve
    rohan "Look at you... so beautiful you've grown. Just like your mother."
    scene 119_s88 with dissolve
    reham "*giggles* Thank you. I'm so happy to see you again. Both of you."
    reham "Our whole family, back together again."
    scene 119_s89 with dissolve
    yasmine "..."
    rohan "..."
    scene 119_s90 with Dissolve(1.0)
    reham "Is something wrong?"
    scene 119_s91 with dissolve
    yasmine "We were just talking about... *sigh* Forget it. It's not important right now."
    scene 119_s90 with dissolve
    reham "Is father gambling again?"
    scene 119_s91 with dissolve
    if mc_told_yasmine_leave:
        yasmine "Something like that. I was about to give your father an ultimatum. Today was... today was the last straw. But then you walked through that door, and..."
        scene 119_s90 with dissolve
        reham "Please don't, Mother. Father is... I still love him."
        scene 119_s91 with dissolve
        yasmine "I know you do. And it would be awful of me to break things right now—right when you've finally returned to us after so long."
        scene 119_s92 with Dissolve(1.0)
        yasmine "Last chance, Rohan. Or I swear I'm leaving and taking Reham with me."
        scene 119_s92 with vpunch
        rohan "Taking her with you?! She's MY daughter too! You can't just—"
        reham "Enough! Please... I just got home."
        yasmine "*sigh* I'm sorry, dear. You're right. Come, you must be tired."
    else:
        yasmine "Something like that. I gave your father another chance. His last one."
        scene 119_s92 with Dissolve(1.0)
        reham "*sigh* Please, Father. No more."
        rohan "Last time. I know. I promise."
    
    reham "I... I just noticed! [mc]! What are you doing here?!"
    reham "I thought we lost you at the market!"
    scene 119_s93 with Dissolve(1.0)
    impulse "Milk these udders!"
    reham "[mc]?"
    scene 119_s94 with vpunch
    mc "Oh! Your mother was in some trouble. I helped her out."
    scene 119_s95 with dissolve
    reham "You... you helped her? How? When?!"
    yasmine "You two know each other?"
    reham "As a matter of fact, we traveled here together. All the way from Irda. [mc]'s the reason I made it home at all."
    scene 119_s94 with dissolve
    mc "Your daughter is exaggerating. She was a huge help too."
    scene 119_s95 with dissolve
    yasmine "*laughs* Strange how fate works, hm? The same man who saved me is also my daughter's companion."
    scene 119_s96 with Dissolve(1.0)
    rohan "Is that your friend standing all quiet out there? *giggles* Isn't she the cutest thing ever."
    reham "Yes. They're good people."
    yasmine "Every friend of my daughter is a friend of ours. Come in, dear. You're all family now."
    stop music fadeout 1.0 
    scene 119_s97 with Fade(1.0,1.0,1.0)
    play music "hope/mysterious_forest.mp3" fadein 1.0 loop
    perception "You sit at the dinner table. Leftover rice and vegetables with a single piece of chicken divided carefully among everyone."
    yasmine "It isn't much, but please. Eat."
    m "It's rearry tashty!"
    reham "That's not how you hold a spoon, Maia..."
    scene 119_s98 with Dissolve(1.0)
    rohan "So... [mc], was it?"
    scene 119_s99 with dissolve
    mc "Yup."
    scene 119_s98 with dissolve
    rohan "Err.. thank you. For saving my wife."
    scene 119_s99 with dissolve
    mc "Of course. It was the natural thing to do. Anyone would have done the same."
    scene 119_s98 with dissolve
    rohan "...Right."
    rohan "Just letting you know that you're in my seat. You see, it's our custom for the head of the household to sit facing everyone."
    rohan "*chuckles* But I will let it slide this time, since you're uneducated on our customs yet."
    scene 119_s100 with dissolve
    yasmine "*ahem* So! How long were you traveling? It must be a long journey from Irda."
    scene 119_s101 with dissolve
    reham "About a week."
    scene 119_s100 with dissolve
    yasmine "Ugh, that must have been awful."
    scene 119_s101 with dissolve
    reham "Mother, we need a place to stay for a bit. Is it alright if [mc] and Maia stay with us?"
    if mc_princess_success:
        reham "There's also two other girls who didn't come, Alex and Rebecca. They're... out in the city right now, but they will need a roof too."
    else:
        reham "There's also another girl who didn't come, Alex. She's out in the city right now, but she'll need a roof too."
    scene 119_s100 with dissolve
    yasmine "Of course, sweetheart. Your friends are welcome here. I already told [mc] to act as if this was his home after he helped me."
    scene 119_s102 with Dissolve(1.0)
    rohan "E-Excuse me... shouldn't I get a say in this?"
    rohan "I'm glad that [mc]... helped you. Truly. But... he's a man, dear. A grown man. And this is a small house."
    scene 119_s103 with dissolve
    yasmine "So?"
    scene 119_s102 with dissolve
    rohan "So?! We can't house another man under the same roof! No offense to [mc]... I'm sure he's a wonderful man, but it's forbidden."
    scene 119_s103 with dissolve
    yasmine "Oh, drop it. This is the least we can do after risking himself."
    scene 119_s102 with dissolve
    rohan "I get it. I do. But, dear..."
    scene 119_s115 with dissolve
    empathy "He's trying his best to maintain his calm, but beneath the words is something else... jealousy."
    reham "Please, father. [mc] is a good man."
    call screen scene119_choice07 with dissolve

label scene119_choice07_op1:
    $ mc_told_rohan_off = True
    mc "I'm staying here. Whether you like it or not."
    scene 119_s105 with dissolve
    rohan "Execuse me?! This is my house! You can't just—"
    scene 119_s106 with dissolve
    mc "I saved your wife. Not because I wanted your gratitude, but because she deserved to be saved."
    mc "If you have a problem with that, you can hit the door."
    rohan "..."
    yasmine "..."
    perception "Yasmine stays silent, but she looks at you with a genuine smile on her face."
    jump scene119_7
    
label scene119_choice07_op2:
    $ mc_told_rohan_support = True
    $ yasmine_love += 10
    mc "I can support the family. I can pay for food and other stuff."
    scene 119_s105 with dissolve
    rohan "You... you have coin? H-How much?"
    scene 119_s106 with dissolve
    mc "Enough. I can contribute with I got."
    scene 119_s116 with Dissolve(1.0)
    yasmine "[mc], you don't have to—"
    scene 119_s117 with dissolve
    mc "I want to. Don't worry."
    scene 119_s116 with dissolve
    yasmine "*giggles* Thank you. You're such a good man. We're blessed to have you with us."
    scene 119_s117 with dissolve
    rohan "..."
    jump scene119_7

label scene119_choice07_op3:
    scene 119_s103 with dissolve
    yasmine "He stays, Rohan. That's the end of it. Or do you suggest we throw him to the streets?"
    scene 119_s115 with dissolve
    reham "Please, Father. For me. For Mother. Just this once."
    scene 119_s102 with dissolve
    rohan "Nghnn... Fine. But he never gets close to either of you."
    scene 119_s115 with dissolve
    mc "..."
    jump scene119_7

label scene119_7:
    scene 119_s107 with Fade(1.0,1.0,1.0)
    mc "I'll take my leave. Alex must be waiting on me."
    mc "Thank you for the food, Yasmine. It was really good."
    scene 119_s108 with dissolve
    yasmine "You barely ate! No room for seconds?"
    scene 119_s107 with dissolve
    mc "*chuckles* Afraid not."
    scene 119_s109 with Dissolve(1.0)
    reham "Do you know your way?"
    scene 119_s110 with dissolve
    mc "I think I memorized it a little."
    scene 119_s108 with Dissolve(1.0)
    yasmine "Be careful, [mc]. And don't take too long! I'll prepare a soft mattress for you."
    rohan "Hmph..."
    scene 119_s107 with dissolve
    mc "Thank you."
    scene 119_s111 with Dissolve(1.0)
    mc "Be a good girl, Maia. Don't cause too much trouble for them."
    scene 119_s112 with dissolve
    m "I won't!"
    jump scene120

label scene120:
    stop music fadeout 1.0 
    scene 120_s1 with Fade(1.5,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    perception "You go past the market and into main road leading to the city's gate."
    scene 120_s2 with Dissolve(1.0)
    alex "There you are."
    alex "Where's Reham and Maia?"
    if mc_killed_reham:
        if not mc_intended_reham:
            scene 120_s3 with dissolve
            mc "I'm so sorry, Alex... I tried to stop it."
            scene 120_s2 with dissolve
            alex "The hell are you talking about?"
            scene 120_s3 with dissolve
            mc "Reham... she's gone. Her mother was taken by debt collectors. She went after her and her father followed. None of them came back."
            scene 120_s2 with dissolve
            alex "WHAT?! And you just stood there!?"
            scene 120_s3 with dissolve
            mc "I'm sorry. I couldn't help. I wanted to, I swear."
            scene 120_s2 with dissolve
            alex "How... how did this happen? I leave for a couple of HOURS and she..."
            alex "I... We didn't get along. She annoyed the hell out of me..."
            alex "But still... God, Reham..."
            scene 120_s3 with dissolve
            mc "I'm sorry. I know you two had your differences, but—"
            scene 120_s2 with dissolve
            alex "What about Maia? Don't tell me you got her killed too?"
            scene 120_s3 with dissolve
            mc "She's fine. She's at Reham's parents house."
            scene 120_s2 with dissolve
            alex "Goddammit. Whatever. I can't look back. I must... I must only look forward. That's how you survive. That's how I've always survived."
        else:
            scene 120_s3 with dissolve
            mc "She's staying with her parents."
            scene 120_s2 with dissolve
            alex "I mean yeah, that's what she said she wanted."
            scene 120_s3 with dissolve
            mc "No. I meant permanently."
            scene 120_s2 with dissolve
            alex "She's leaving?! Just like that? After everything we went through?"
            scene 120_s3 with dissolve
            mc "She's just a young woman, Alex. Do you expect her to keep traveling with two fugitives?"
            mc "She has a family here."
            scene 120_s2 with dissolve
            alex "I... I guess that's better for her. Just didn't think it would be so soon. I didn't think give her a goodbye..."
            scene 120_s3 with dissolve
            mc "It's better this way."
            scene 120_s2 with dissolve
            alex "We didn't see eye to eye. But... I'll miss her."
            alex "What about Maia?"
            scene 120_s3 with dissolve
            mc "We managed to find an abandoned house. She'll be safe there."
            scene 120_s2 with dissolve
            alex "Alright. I thought I'd had enough of abandoned houses, but... oh well."
    else:
        scene 120_s3 with dissolve
        mc "Both are staying at Reham's parents' house. They'll be safer there."
        scene 120_s2 with dissolve
        alex "Sounds good."
        scene 120_s3 with dissolve
        mc "Managed to find anything?"
        scene 120_s2 with dissolve
        alex "*sigh* Sadly, no. It's pretty much impossible to get an audience with the king without having a date already set up with the council."
        alex "It isn't like Irda where you could meet the Queen just by knocking."
        alex "Even then, it takes days to file a request. And even more for it to be reviewed and accepeted."

    scene 120_s3 with dissolve
    mc "So what now?"

    if mc_princess_success:
        scene 120_s2 with dissolve
        alex "We wait for the princess to wake up. She's the key. She wasn't hidden away like I was, surely some of the higher ups here will recognize who she is."
        scene 120_s3 with dissolve
        mc "Is there a chance she gets caught? The rumors that spread after the market explosion said she was complicit. That she and I planned it together."
        scene 120_s2 with dissolve
        alex "Unlikely. Different cities, different jurisdictions. Nahraya and Irda have no extradition treaty as far as I know."
        alex "They have no obligation to arrest her on Avery's word."
        scene 120_s3 with dissolve
        mc "Alright. So... wait for Rebecca it is. Speaking of which—did you check up on her?"
        scene 120_s2 with dissolve
        alex "I wasn't allowed anywhere near her. The healers said they need at least a day before they allow visi—"
        scene 120_s4 with dissolve
        r "Let me go!"
        scene 120_s5 with Dissolve(1.0)
        doctor "Ma'am, please! You're still ill! Your body isn't ready to stand, let alone walk! Please, come back inside!"
        r "I don't... Hahh... I don't care. I need to see... the king! I need to fix this! Avery is—"
        stop music fadeout 1.0 
        scene 120_s6 with Dissolve(1.0)
        mc "Rebecca!"
        play music "sad/reb3.mp3" fadein 3.0 volume 0.7 loop
        scene 120_s7 with dissolve
        r "Who... [mc]? Is that... is that really you?"
        scene 120_s6 with dissolve
        mc "You're awake!"
        scene 120_s7 with dissolve
        r "Is this your doing? Did... nghnn... did you get me here? I remember... I remember someone lifting me..."
        scene 120_s6 with dissolve
        mc "I did. A lot of us did. People you've never met who risked everything."
        mc "More importantly—you need to rest, Becky. You're in no shape to be out here."
        scene 120_s7 with dissolve
        r "No! I have to fix this... Avery is... she's going to destroy everything! The kingdom! My mother's legacy!"
        scene 120_s6 with dissolve
        mc "I know. I know. But look at yourself! You can barely stand!"
        scene 120_s8 with Dissolve(1.0)
        r "*hic*"
        r "Why did this happen? Why did she do this to me? I trusted her... she was my aunt!"
        scene 120_s9 with dissolve
        mc "I'm sorry."
        scene 120_s8 with dissolve
        r "Nghnn! It hurts! Everything hurts!"
        doctor "You! Help me pick her up. She can't be out here."
        scene 120_s10 with Fade(1.3,1.0,1.3)
        doctor "Don't be hasty now, ma'am. You have to recover first." 
        r "..."
        perception "She falls asleep instantly. The brief burst of energy that got her to the doorway has burned away."
        scene 120_s11 with Dissolve(1.0)
        doctor "Excuse me, but who are you to her? Are you family?"
        scene 120_s12 with dissolve
        jump scene120_2
    elif mc_save_queen:
        jump scene122
    else:
        jump scene123

label scene120_2:
    if not mc_reb_breakup and not mc_rejected_wedding_reb:
        mc "I'm her husband."
    else:
        mc "You could say that."
    scene 120_s11 with dissolve
    doctor "She should be glad that she has someone like you, sir. A minute more out there, and she... well... you know."
    scene 120_s12 with dissolve
    mc "I'm glad that wasn't the case."
    scene 120_s11 with dissolve
    if reb_pregnant:
        if mc_princess_100 or mc_princess_300:
            if mc_slap_avery:
                $ reb_pregnancy_fail = True
                if not mc_reb_breakup and not mc_rejected_wedding_reb:
                    doctor "There's something else you have to know, sir. Since you're her husband, it involves you too."
                else:
                    doctor "There's something else you have to know, sir. Since you're family, it involves you too."
                scene 120_s12 with dissolve
                mc "What is it?"
                scene 120_s11 with dissolve
                doctor "Unfortunately... her pregnancy has failed."
                scene 120_s12 with dissolve
                alex "What?"
                mc "Are you saying...?"
                scene 120_s11 with dissolve
                doctor "Yes, sir. Due to her condition, her body wasn't able to support the fetus."
                doctor "We did everything we could. But it looks like she was aggressively starved."
                doctor "I'll leave you with her for a bit. She'll need you when she wakes."
                scene 120_s12 with dissolve
                mc "Rebecca... I'm so sorry. I should have prepared more!"
                alex "..."
                scene 120_s13 with Dissolve(2.0)
            else:
                if not mc_reb_breakup and not mc_rejected_wedding_reb:
                    doctor "There's something else you have to know, sir. Since you're her husband, it involves you too."
                else:
                    doctor "There's something else you have to know, sir. Since you're family, it involves you too."
                scene 120_s12 with dissolve
                mc "What is it?"
                scene 120_s11 with dissolve
                doctor "Unfortunately... her pregnancy is in a rough state."
                scene 120_s12 with dissolve
                alex "What?"
                mc "Are you saying...?"
                scene 120_s11 with dissolve
                doctor "It's still alive, sir. But she wasn't properly fed and hydrated throughout your journey here. Her fetus was barely clinging to life."
                doctor "We did everything we could. Now it's up to the Gods to decide if the fetus lives or not."
                scene 120_s12 with dissolve
                mc "..."
                scene 120_s11 with dissolve
                doctor "I'll leave you with her for a bit. She'll need you when she wakes."
                scene 120_s12 with dissolve
                mc "Rebecca... I'm so sorry. I should have prepared more!"
                alex "..."
                scene 120_s13 with Dissolve(2.0)
        else:
            if mc_slap_avery:
                if not mc_reb_breakup and not mc_rejected_wedding_reb:
                    doctor "There's something else you have to know, sir. Since you're her husband, it involves you too."
                else:
                    doctor "There's something else you have to know, sir. Since you're family, it involves you too."
                scene 120_s12 with dissolve
                mc "What is it?"
                scene 120_s11 with dissolve
                doctor "Unfortunately... her pregnancy is in a rough state."
                scene 120_s12 with dissolve
                alex "What?"
                mc "Are you saying...?"
                scene 120_s11 with dissolve
                doctor "It's still alive, sir. But it appears she was aggressively starved for some time. Her fetus was barely clinging to life."
                doctor "We did everything we could. Now it's up to the Gods to decide if the fetus lives or not."
                scene 120_s12 with dissolve
                mc "Avery..."
                scene 120_s11 with dissolve
                doctor "I'll leave you with her for a bit. She'll need you when she wakes."
                scene 120_s12 with dissolve
                scene 120_s13 with Dissolve(2.0)
            else:
                if not mc_reb_breakup and not mc_rejected_wedding_reb:
                    doctor "There's something else you have to know, sir. Since you're her husband, it involves you too."
                else:
                    doctor "There's something else you have to know, sir. Since you're family, it involves you too."
                scene 120_s12 with dissolve
                mc "What is it?"
                scene 120_s11 with dissolve
                doctor "Breathe, sir. She was in a rough state when you brought her in, but was fed and hydrated just enough for her body to support the growing fetus."
                scene 120_s12 with dissolve
                mc "Thank you. I knew having more supplies was good."
                scene 120_s11 with dissolve
                doctor "I'll leave you with her for a bit."
                scene 120_s13 with Dissolve(2.0)
    else:
        doctor "I'll leave you with her for a bit."
        scene 120_s12 with dissolve
        scene 120_s13 with Dissolve(2.0)

    if reb_pregnancy_fail:
        alex "I'm sorry, [mc]."
        mc "..."
    else:
        mc "Get better quick, Becky. We're all counting on you."

    perception "Rebecca breathes softly under the covers. Her blonde hair shines brightly in the moonlight."
    stop music fadeout 3.0 
    scene black with Dissolve(2.0)
    r "[mc]..."
    scene 120_s14 with vpunch
    mc "Hhuh?!"
    mc "Becky! Do you feel better? Should I get the nurse?"
    scene 120_s15 with dissolve
    r "Mfhmm... better. A little."
    scene 120_s14 with dissolve
    mc "Alright, don't talk. Just rest."
    scene 120_s15 with dissolve
    r "What do I do, [mc]? I lost every... everything. My kingdom, my mother, my aunt..."
    scene 120_s14 with dissolve
    mc "We will get it all back."
    r "..."
    if mc_karma >= 5:
        mc "I promised to make it right, Becky. Back in that cellar. I promised to save this city so you could walk proud and high again. I meant every word."
    else:
        mc "I promised to kill everyone who wronged you, Becky. Everyone who had a hand in this. They will burn. I swear it."
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 120_s16 with Dissolve(1.5)
    r "Mhnn... I want to go outside. I want to see the sky. I've been in the dark for so long..."
    mc "Wait! You can't! What if you get sick again? The nurse said—"
    scene 120_s17 with Dissolve(1.5)
    mc "Becky!"
    perception "She stands up, wobbling. Her knees buckle. She stumbles forward, you think she's going to fall. You lunges to catch her. But in truth..."
    scene 120_s18 with Dissolve(0.3)
    play sound "sound_effects/body/clothes1.mp3"
    scene 120_s18 with vpunch
    empathy "She hugs you. Her arms wrap around your with surprising strength."
    r "*sob* [mc]... I missed you so much."
    scene 120_s20 with Dissolve(1.0)
    mc "I missed you too."
    scene 120_s19 with dissolve
    r "Oh, [mc]. I never stopped thinking about you..."
    r "At first, I thought maybe you would come and save me any moment. I kept waiting... but after some point... I stopped."
    r "I gave up thinking about it. I thought you ran away. I thought you... forgot about me."
    scene 120_s20 with dissolve
    mc "Never."
    scene 120_s19 with dissolve
    r "*sob* Please forgive me for doubting you."
    scene 120_s20 with dissolve
    mc "Of course. There's nothing to forgive."
    scene 120_s19 with dissolve
    r "I want to go outside. Come with me."
    scene 120_s20 with dissolve
    mc "I can't stop you once you're like this... Fine. Let's look at the stars. They look really pretty here."
    $ reb_love = 0
    jump scene120_3

label scene120_3:
    $ mc_reb_outside = True
    stop music fadeout 1.0 
    scene 120_s21 with Fade(1.0,1.0,1.5)
    play music "night.mp3" fadein 1.0 volume 0.5 loop
    perception "You step outside with Rebecca. The cold desert night air washes over you. The streets are empty at this hour except for a few stray cats."
    scene 120_s24 with Dissolve(1.0)
    alex "Erm... just pretend I'm not here."
    scene 120_s22 with dissolve
    r "Wh-Who? Wait... you're..."
    scene 120_s24 with dissolve
    alex "I'm Alex. Or Alexandria, if we're being royal about it."
    alex "Sorry if I scared you. I've always been good at being invisible."
    scene 120_s22 with dissolve
    r "What are you doing here? Are you... with [mc]?"
    scene 120_s24 with dissolve
    alex "Just go with him. It's a long story."
    scene 120_s22 with dissolve
    r "A-Alright."
    scene 120_s25 with Dissolve(1.4)
    alex "Don't mention me, please. I don't want her to get mad at me, not yet at least."
    if reb_pregnancy_fail:
        alex "Also, it's better not to talk about the... pregnancy too."
    scene 120_s26 with Fade(0.5,0.5,0.5)
    r "*inhale* Ahhh..."
    r "I never thought I'd see the sky again."
    mc "Beautiful, huh?"
    r "More beautiful than I remembered."
    r "sigh* My aunt told me what happened. One night she descended into the cellar... I was barely conscious, but I could tell she was drunk."
    r "Then she said it... how she killed my mother."
    r "*scoff* She started sobbing afterwards. Alligator tears."

    if mc_save_queen:
        mc "Your mother is alive, Becky."
        scene 120_s27 with vpunch
        r "What? H-How do you know?"
        scene 120_s28 with Dissolve(1.0)
        mc "Just... trust me. She's alive and well."
        scene 120_s29 with dissolve
        r "You're not saying that just to console me, right? You would be shattering my heart if you're lying."
        scene 120_s28 with dissolve
        mc "I'm not."
        scene 120_s29 with dissolve
        r "Thank the Gods... Oh mother... I don't know where I would've gone if she was gone."
        r "Where is she?"
        scene 120_s28 with dissolve
        mc "Somewhere safe. I'm sure she'll appear when we need her the most."
        scene 120_s29 with dissolve
        r "*sigh* So she's alive... but her kingdom is stolen. Everything I knew... everything I was supposed to inherit... it's all gone."
        scene 120_s30 with Dissolve(1.0)
        stop music fadeout 1.0 
        r "Right now... it feels like you're the only real thing I have left."
        play music "reb.mp3" fadein 5.0 loop
        r "Do you... love me, [mc]?"
        scene 120_s31 with dissolve
    else:
        mc "I'm sorry, Becky. You have my condolences. She was a great woman."
        r "I know."
        scene 120_s30 with Dissolve(1.0)
        stop music fadeout 1.0 
        r "My mother is gone, her kingdom is stolen. All I have left is... you."
        play music "reb.mp3" fadein 5.0 loop
        r "Do you... love me, [mc]?"
        scene 120_s31 with dissolve
        
    if mc_reb_breakup or mc_rejected_wedding_reb:
        mc "..."
        scene 120_s30 with dissolve
        r "You always ignored me before."
        r "When I tried to talk to you, tried to get close to you—you always found somewhere else to be."
        r "So... why? Why did you come back for me?"
        scene 120_s31 with dissolve
        mc "Does not loving you mean I can't still want to save you?"
        scene 120_s30 with dissolve
        r "...I guess not."
        if mc_rejected_wedding_reb:
            r "Thank you, nonetheless. I guess we'll stay as friends."
        else:
            r "Thank you, nonetheless. Although... I don't see us being wed anymore."
            r "The girl who dreamed of that... she died in that cellar."
            r "I'm someone else now. Someone who just wants to live long enough to see my mother's kingdom restored."
        scene 120_s31 with dissolve
        call screen scene120_choice03 with dissolve
    else:
        mc "Of course I do."
        scene 120_s30 with dissolve
        r "Prove it."
        scene 120_s31 with dissolve
        mc "Prove it?"
        scene 120_s30 with dissolve
        r "I want to feel something, [mc]. I've been deprived of touch... of a single kind word... for so long."
        r "I want to feel alive again."
        scene 120_s31 with dissolve
        mc "..."
        scene 120_s30 with dissolve
        r "Please."
        scene 120_s31 with dissolve
        scene 120_s32 with Dissolve(2.0)
        call screen scene120_choice04 with dissolve

label scene120_choice03_op1:
    scene 120_s28 with Dissolve(1.0)
    mc "I want us to have another chance, Becky."
    mc "I ignored you before. I was stupid."
    mc "But I've had a lot of time to think, and I kept coming back to you. To the way I treated you. To the way I let you slip away without ever telling you—"
    mc "I promise not to ignore you anymore. If you'll let me try again."
    scene 120_s30 with Dissolve(1.0)
    r "...Really?"
    scene 120_s31 with dissolve
    mc "Really. I mean it."
    scene 120_s30 with dissolve
    r "Then prove it."
    scene 120_s31 with dissolve
    mc "Prove it?"
    scene 120_s30 with dissolve
    r "Tell me how much you want it."
    scene 120_s31 with dissolve
    scene 120_s32 with Dissolve(2.0)
    call screen scene120_choice04 with dissolve

label scene120_choice03_op2:
    $ mc_reb_breakup_final = True
    mc "That's fine. I'm just happy that you're here."
    scene 120_s30 with dissolve
    r "*chuckles* Very well."
    scene 120_s31 with dissolve
    jump scene120_5

label scene120_choice04_op1:
    $ reb_love += 10
    mc "Your eyes are as blue as the sky. I've never seen anything like them."
    r "What else?"
    scene 120_s33 with Dissolve(2.0)
    call screen scene120_choice05 with dissolve

label scene120_choice04_op2:
    $ reb_love += 20
    mc "Your eyes are like an ocean. An ocean I could drown in, and... and I wouldn't even fight it."
    r "What else?"
    scene 120_s33 with Dissolve(2.0)
    call screen scene120_choice05 with dissolve

label scene120_choice04_op3:
    mc "Your eyes are like egg yolks if they were blue."
    r "Uhh..."
    r "What else?"
    scene 120_s33 with Dissolve(2.0)
    call screen scene120_choice05 with dissolve

label scene120_choice05_op1:
    mc "I like your haircut. It's... it's nice."
    r "*chuckles* Ermm... Well, thanks?"
    r "And?"
    scene 120_s34 with Dissolve(2.0)
    call screen scene120_choice06 with dissolve

label scene120_choice05_op2:
    $ reb_love += 10
    mc "Your silky hair... it flows like melted gold. It's mesmerizing."
    r "And?"
    scene 120_s34 with Dissolve(2.0)
    call screen scene120_choice06 with dissolve

label scene120_choice05_op3:
    $ reb_love += 20
    mc "Your bright hair makes me think of the sun. Warm and kind against my skin."
    r "And?"
    scene 120_s34 with Dissolve(2.0)
    call screen scene120_choice06 with dissolve
    
label scene120_choice06_op1:
    $ reb_love += 20
    mc "I'd follow you to the ends of the world. And when I reach the edge, I'd fall off in your embrace."
    jump scene120_4

label scene120_choice06_op2:
    mc "I'll never leave you."
    jump scene120_4
    
label scene120_choice06_op3:
    $ reb_love += 10
    mc "I'll always stay with you, until the very end."
    jump scene120_4

label scene120_4:
    if reb_love >= 60:
        scene 120_s35 with Dissolve(1.0)
        r "That... that was so beautiful, [mc]!"
        r "I'm surprised. Were you always this poetic?"
        scene 120_s36 with dissolve
        mc "*chuckles* Only for you."
        scene 120_s35 with dissolve
        r "Seriously, who taught you to speak like that?"
        scene 120_s36 with dissolve
        mc "Life, milady. Life taught me."
        scene 120_s37 with dissolve
        r "*laughs* Milday? {i}Milady?!{/i} You just ruined the entire moment!"
    else:
        scene 120_s35 with Dissolve(1.0)
        r "*laughs* You never were good at flirting, were you?"
        scene 120_s36 with dissolve
        mc "*chuckles* Not really. I've always been better with actions."
        scene 120_s35 with dissolve
        r "But I feel it still."
        r "You do love me... and right now, that's enough."
    scene 120_s38 with Dissolve(1.5)
    play sound "se_sfx/blowjob/kiss4.mp3" 
    r "Mwah~!"
    call screen scene120_choice07 with dissolve

label scene120_choice07_op1:
    scene 120_s39 with Dissolve(0.3)
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 120_s39 with vpunch
    r "Mfmm~!?"
    r "[mc]~ *lick* You're in heat, aren't you?"
    r "Well so am I. *slurp* You have no idea how horny I am. I never had the chance to let go while I was locked up in there."
    r "Let's finish up with the king and have ourselves some time, hmmn~?"
    mc "That sounds wonderful."
    jump scene120_5

label scene120_5:
    scene 120_s40 with Fade(1.0,1.0,1.0)
    r "Thanks for letting me out, [mc]! I feel really motivated right now, like I could take on the whole world!"
    scene 120_s41 with dissolve
    mc "Shall we storm the king's palace, then? Right now? Bust down the doors and just... talk to him?"
    scene 120_s42 with dissolve
    r "Let's go!"
    scene 120_s41 with dissolve
    mc "*chuckles* Hold on. I was just joking."
    mc "We'll do that first thing tomorrow. Gotta make sure you're in the best shape first."
    scene 120_s42 with dissolve
    if not mc_reb_breakup_final:
        r "Hmm~? Does my dear husband really care about me that much?"
        scene 120_s41 with dissolve
        mc "He does. More than you're willing to admit."
        scene 120_s42 with dissolve
        r "Hmph~ Fine. Tomorrow it is."
        scene 120_s41 with dissolve
        scene 120_s43 with Fade(0.5,0.5,0.5)
        alex "..."
        mc "See you tomorrow, Alex."
    else:
        scene 120_s42 with dissolve
        r "Yes, yes. Tomorrow it is!"
        scene 120_s41 with dissolve
        scene 120_s43 with Fade(0.5,0.5,0.5)
        alex "..."
        mc "See you tomorrow, Alex."

    if mc_sat_with_alex:
        scene 120_s44 with dissolve
        alex "Umm... just so you know... I-I really enjoyed our sit together under the stars too."
        scene 120_s43 with dissolve
        mc "Me too."
        scene 120_s44 with dissolve
        alex "Sleep tight, [mc]. I'll watch over both of you."
        scene 120_s43 with dissolve
    else:
        alex "Mhm."
    stop music fadeout 1.0 
    jump scene121

label scene121:
    scene 121_s1 with Fade(1.5,1.0,1.5)
    play music "nature.mp3" fadein 1.0 volume 0.5 loop
    ""
    scene 121_s1 with vpunch
    r "[mc]!"
    mc "I'm awake!"
    scene 121_s2 with Dissolve(1.0)
    r "Come on, sleepy head. I'm not spending another minute in this bed."
    scene 121_s3 with dissolve
    mc "*yawn* How are you so energetic already?"
    scene 121_s2 with dissolve
    r "Guess I'm tougher than you think~"
    scene 121_s3 with dissolve
    mc "*chuckles* Well, I'm glad you're already back to your old self. I'm right behind you, princess."
    scene 121_s2 with dissolve
    r "By the way... how is Maia doing? Is she—"
    scene 121_s3 with dissolve
    mc "She's fine. She's here with me actually, somewhere safe with Reham, another girl I travelled with."
    scene 121_s2 with dissolve
    r "Good. That girl is too pure for this world. I would never forgive myself if something happened to her."
    r "And another girl, huh~? You'll have to tell me about her."
    scene 121_s3 with dissolve
    mc "Haha..."
    scene 121_s4 with Dissolve(1.0)
    alex "You ready?"
    scene 121_s5 with vpunch
    r "AHHH!"
    r "Stop that! How do you {i}do{/i} that?! You're so unnerving."
    scene 121_s6 with Dissolve(1.0)
    alex "Sorry..."
    alex "I know where the palace is. Hopefully someone there knows who you are, princess."
    scene 121_s7 with dissolve
    r "I've been here before. A long time ago with my mother. She brought me here on a diplomatic visit, said I had to make connections and whatnot."
    r "If only I listened to her..."
    scene 121_s6 with dissolve
    alex "Someone might remember your face."
    scene 121_s44 with dissolve
    scene 121_s8 with Fade(1.3,1.0,1.3)
    perception "You check Rebecca out of the hospice and make your way further into the city. The streets grow wider, cleaner, the buildings taller and more ornate."
    alex "Through here."
    play sound "sound_effects/body/stomach_growl.mp3"
    perception "You hear Rebecca's stomach grumble. Her cheeks flush in embarrassment."
    scene 121_s10 with Dissolve(1.0)
    r "Oh... *ahem* don't mind me."
    scene 121_s9 with dissolve
    mc "Why don't we stop to eat once we're done with the king? Find the best restaurant in Nahraya and order everything on the menu."
    scene 121_s10 with dissolve
    r "*chuckles* You're already planning the victory feast?"
    scene 121_s9 with dissolve
    mc "What? You don't think you can do it?"
    scene 121_s10 with dissolve
    r "Well, I'm not exactly good with politics. My mother did all the work. I was just... there."
    scene 121_s9 with dissolve
    mc "You'll be fine. I trust you."
    scene 121_s45 with dissolve
    scene 121_s11 with Fade(1.4,1.0,1.4)
    perception "You reach a massive building with golden arches soaring overhead, colorful ceramic tiles forming intricate mosaic art."
    scene 121_s12 with Fade(1.0,1.0,1.0)
    mc "We're right behind you, Becky. All the way."
    r "I... ermm..."
    scene 121_s13 with Dissolve(1.0)
    r "*ahem* Excuse me! I want to see the king."
    guard "None may enter his presence without leave."
    r "D-Don't you know who I am? I am Irda's princess! Daughter of Queen Hannah!"
    guard "None may enter his presence without leave. Stand back!"
    mc "Maybe you can be a little more... professional? Less shouting, more... authority?"
    alex "I knew it wouldn't be that easy."
    scene 121_s14 with Dissolve(1.0)
    mc "Hmm? Wait..."
    amb "Open the gates! I have official business with the king. He's expecting me."
    guard "Right away, sir."
    mc "Wait—I know this guy! He was talking to the Queen back it Irda before all this went down."
    scene 121_s15 with Dissolve(1.0)
    r "I know him too! Excuse me! Ambassador Sanoud!"
    scene 121_s46 with dissolve
    amb "If you have issues, go to the court, citizen. This is his royal highness's palace, not a public forum. I don't have time for—"
    scene 121_s16 with vpunch
    amb "P-Princess of Irda?! What in the Gods' name are you doing here?"
    amb "I thought you were... on trial."
    amb "In fact, I've seen all three of you before! What's going on here?!"
    scene 121_s17 with dissolve
    r "I..."
    scene 121_s18 with dissolve
    mc "You can do it, Becky."
    scene 121_s17 with dissolve
    if not mc_save_queen:
        r "*inhale* I was falsely accused. Avery, the current queen, took the throne by force. She orchestrated a coup with Reiner of Eurina."
        r "My mother, Queen Hannah... she's been killed. Murdered. The ship accident was a lie."
    else:
        r "*inhale* I was falsely accused. Avery, the current queen, took the throne by force. She orchestrated a coup with Reiner of Eurina."
        r "My mother, Queen Hannah—she had an attempt on her life, but she survived. She's hiding right now."

    r "Please. I must speak to your king. This is of utmost importance to your kingdom as well."
    r "Reiner won't stop at Irda. Nahraya might be in danger too."
    scene 121_s18 with dissolve
    amb "..."
    scene 121_s16 with dissolve
    amb "Very well. I believe the conviction in your eyes. And I remember your mother. She didn't deserve what happened to her."
    amb "Leave any weapons you have with the guards and follow me."
    scene 121_s17 with dissolve
    r "Thank you."
    scene 121_s18 with dissolve
    play sound "sound_effects/doors/gate_open.mp3"
    scene 121_s19 with Fade(0.5,0.5,0.5)
    mc "You did it."
    r "Hmm~? Did I hear doubt in your voice earlier?"
    mc "Doubting my intelligent, incredibly beautiful princess? Heresy."
    alex "You two are starting to annoy me."
    stop sound fadeout 1.0
    stop music fadeout 1.0 
    scene 121_s20 with Fade(1.0,1.0,1.0)
    play music "ambiance/king_in_red.mp3" fadein 1.0 loop
    perception "You enter the palace, it's exceptionally beautiful and clean. Every surface polished to a mirror shine, every floor a mosaic of colored tiles depicting the history of Nahraya."
    amb "Please keep with me. Don't go anywhere, don't make any sudden moves, and don't touch anything."
    amb "When we reach the king, you kneel. You show respect. And most importantly, you never speak unless—"
    mc "Unless spoken to. I know. I already went through this before."
    amb "You're exempt from kneeling, princess of Irda. But that still doesn't mean you don't show proper respect."
    scene 121_s21 with Fade(1.0,1.0,1.0)
    amb "My liege, I have news of the grain bill with the Zents. Progress has been made, though they demand tariffs be lifted."
    amb "I also have a guest for—"
    scene 121_s22 with dissolve
    king "Shh."
    amb "..."
    scene 121_s21 with dissolve
    amb "{size=30}Kneel!{/size}"
    scene 121_s22 with dissolve
    call screen scene120_choice08 with dissolve

label scene120_choice08_op1:
    $ mc_knelt_hod = True
    scene 121_s23 with Dissolve(1.0)
    perception "You lower yourself to one knee. The marble is cold beneath you. Alex does the same, her movements stiff but obedient."
    scene 121_s25 with Dissolve(1.0)
    perception "You glance upwards. To the king's left stands a young woman dressed in flowing silks. Likely the princess. She doesn't look at you. Her gaze is fixed on Alex, her expression unreadable, curiosity? Recognition?"
    scene 121_s27 with Dissolve(1.0)
    perception "To the right of the king is a... man? Likely the prince. His eyes are fixed on you. More specifically, on your metal hand."
    if mc_princess_success:
        jump scene121_2
    elif mc_save_queen:
        jump scene122_2
    else:
        jump scene123_2

label scene120_choice08_op2:
    $ mc_stood_hod = True
    scene 121_s24 with Dissolve(1.0)
    perception "The ambassador shoots you a look of pure panic as you stay still. Your eyes are fixed on the king."
    scene 121_s26 with Dissolve(1.0)
    perception "You glance left. The young woman, likely the princess, stands beside the king and looks at you with worry. She's seen people defy her father before. She knows how it ends."
    scene 121_s28 with Dissolve(1.0)
    perception "To the right of the king is a... man? Likely the prince. He looks at you with a smirk as if your defiance is amusing."
    if mc_princess_success:
        jump scene121_2
    elif mc_save_queen:
        jump scene122_2
    else:
        jump scene123_2

label scene121_2:
    scene 121_s29 with Dissolve(1.0)
    king "You."
    scene 121_s30 with dissolve
    alex "M-Me?"
    scene 121_s29 with dissolve
    king "You're Reiner's daughter. He said you ran away again. He's been looking for you—sent letters, messengers, even a bounty at one point."
    king "I remember faces, and yours was described in great detail. Why did you come here?"
    scene 121_s30 with dissolve
    alex "I..."
    scene 121_s31 with Dissolve(1.0)
    r "Sir... I mean, my liege? Could I speak to you? Please. Before this goes any further."
    scene 121_s32 with dissolve
    if mc_stood_hod:
        king "Why isn't that man kneeling? Have you no control over your slaves?"
        scene 121_s31 with dissolve
        if not mc_reb_breakup_final:
            r "He's not a slave. He's my husband. Please forgive his disrespect... he's unused to court protocol."
        else:
            r "Please forgive his disrespect... he's unused to court protocol."
        scene 121_s32 with dissolve
    king "Have I seen you before? Your face is familiar too."
    scene 121_s31 with dissolve
    r "I'm Queen Hannah's daughter. The princess of Irda. Rebecca."
    king "..."
    scene 121_s33 with Dissolve(1.0)
    empathy "The king's expression suddenly changes. The anger and suspicion melt away, replaced by disbelief."
    scene 121_s34 with dissolve
    king "How? The reports said you were imprisoned. Charged with treason."
    scene 121_s33 with dissolve
    r "My aunt... Avery, she orchestrated a plan with Reiner of Eurina."
    if mc_save_queen:
        r "The plan was to assassinate my mother and have her take the throne. Thankfully, she survived and is now in hiding. She's completely powerless, but alive."
    else:
        r "The plan was to assassinate my mother and have her take the throne. She murdered her way into power."
    r "She held me in a cellar for weeks. I was on my way to be executed, but my husband here saved me before it happened."
    scene 121_s34 with dissolve
    king "Impossible... Last I heard was that your mother died in a ship accident. I mourned her. I sent condolences to your aunt. I—"
    scene 121_s33 with dissolve
    r "It was a lie. All of it. Every word Avery has spoken since the day she took the throne has been a lie."
    king "..."
    scene 121_s34 with dissolve
    king "Do you have proof for this?! Something beyond your word?"
    scene 121_s35 with Dissolve(1.0)
    r "I am telling you this as her only daughter. All I have is what I endured."
    r "She kept me locked in that cellar while she taunted me almost every night. She told me everything... how she'd planned it, how she'd executed it, how no one would ever know."
    scene 121_s36 with dissolve
    alex "She tells the truth."
    king "Reiner's daughter... and Irda's daughter... both here in my throne room. Both telling the same story."
    scene 121_s37 with Dissolve(1.0)
    king "It was all too convenient. The 'accident'. The 'treason'. The way everything fell so neatly into place for Avery..."
    king "*cough* I see it now."
    scene 121_s38 with dissolve
    prince "Father?!"
    amb "My liege?! Bring water! Quickly!"
    scene 121_s37 with dissolve
    king "They lied to me... They played me for a fool."
    king "Reiner... Avery... I welcomed them. I called them allies."
    if mc_save_queen:
        king "I will get them back for this. I swear on my life. On my crown."
    else:
        king "I will get them back for this. I swear on my life. On my crown. On the memory of your mother, who deserved none of this."
    scene 121_s38 with dissolve
    amb "M-My liege, please think this thoroughly. We can't lunge into war this quickly."
    scene 121_s37 with dissolve
    king "...Yes. They believe I am still blind to it... I can take advantage of that."
    king "Just you wait."
    scene 121_s39 with Dissolve(1.0)
    king "*sigh* As for now... prepare a bedchamber for the princess! The biggest one!"
    king "And assinge twenty servants for her."
    scene 121_s40 with dissolve
    servant "Yes, my liege."
    scene 121_s41 with Fade(1.0,1.0,1.0)
    mc "Great job, Becky."
    mc "You might get treated here better than in Irda."
    scene 121_s42 with dissolve
    r "Not complaning~"
    r "Come on! Let's check out the room."
    if not mc_reb_breakup_final:
        r "They better give us some privacy because I want you~"
    scene 121_s41 with dissolve
    mc "*chuckles* Coming."
    jump scene124

label scene122:
    scene 120_s2 with dissolve
    alex "I don't know... The princess could have gotten us a quick and easy way in."
    scene 120_s3 with dissolve
    mc "Enough, Alex. We're already here. Dwelling on it won't change anything."
    scene 120_s2 with dissolve
    if mc_princess_fail_late:
        alex "I'm not dwelling. I'm stating facts. Without Rebecca, we're nobody. But no! You had to save those two guards and leave her behind."
    elif mc_princess_fail_early:
        alex "I'm not dwelling. I'm stating facts. Without Rebecca, we're nobody. *sigh* We couldn't even begin our mission."
    else:
        alex "I'm not dwelling. I'm stating facts. Without Rebecca, we're nobody. But no! You had to listen to Reham."
    scene 120_s3 with dissolve
    mc "We'll just have to look more—"
    scene 122_s1 with Dissolve(1.0)
    alex "Holy shit!"
    scene 122_s2 with Dissolve(1.0)
    mc "What?"
    play sound "sound_effects/horse_snort.mp3"
    alex "That carriage!"
    mc "What about it?"
    scene 122_s3 with Dissolve(1.0)
    whitlaw "Don't come any closer!"
    scene 122_s4 with Dissolve(1.0)
    q "It's alright, Witlow. They're with me."
    q "Get in you two. We have much to discuss."
    stop music fadeout 1.0 
    scene 122_s22 with Fade(1.0,1.0,1.0)
    play music "the_queen_returns.mp3" fadein 1.0 loop
    perception "The carriage is cold. A complete contrast to the desert heat outside."
    mc "..."
    alex "..."
    scene 122_s6 with dissolve
    q "*chuckles* Too stunned to speak?"
    scene 122_s5 with dissolve
    mc "Queen! H-How did you get here?!"
    mc "Alex told me you were hiding!"
    scene 122_s6 with dissolve
    q "I was hiding. In a rather damp fishing village on the coast of Eurina, to be precise. Until a certain feeling pulled me here."
    q "I trained in prediction sorcery. It isn't much, but it helps me every now and then."
    q "When I felt the threads of fate converging on Nahraya, I knew I had to come."
    scene 122_s21 with dissolve
    alex "Does that mean... you already knew what I was about to do back then? When I—"
    scene 122_s6 with dissolve
    q "I did. I sensed your intent the moment you came near me."
    scene 122_s21 with dissolve
    alex "...Y-You knew. And you still trusted me?"
    scene 122_s6 with dissolve
    q "Indeed. Because I also sensed the desperation in your heart. Or rather seen in through your stoic expression."
    scene 122_s22 with dissolve
    alex "..."
    scene 122_s5 with dissolve
    mc "Why is it so chilly in here? It feels... unnatural."
    scene 122_s6 with dissolve
    q "Feels good, doesn't it? Journeying through the desert is so much easier when you have convenient magic like this."
    q "A simple cooling enchantment. It can be sustained for long periods as it drains very little mana."
    scene 122_s21 with dissolve
    alex "I-I thought you weren't that good with magic. You told me you knew basic protection spells."
    scene 122_s6 with dissolve
    q "What kind of ruler would lay all her cards on one table? Of course I knew more, little fledgling."
    scene 122_s5 with dissolve
    mc "Forget that. Isn't it dangerous for you to show up like this?"
    scene 122_s6 with dissolve
    q "I won't lie, escaping Eurina's seas was rather gut wrenching, but I couldn't ignore my premonition."
    q "My hope was that you two would bring my daughter here. She would have walked into the palace, and the king would have recognized her."
    q "She would have taken it from there. *chuckles* Perhaps even more. Perhaps she would even be the new ruler of Irda instead of my son."
    scene 122_s5 with dissolve
    if mc_princess_reham:
        mc "I'm sorry, your majesty. We thought we could convince the king without attempting a rescue that might endanger so many people."
        mc "We thought we could somehow get help regardless, but... well. Before we could think of anything else... there you were."
    else:
        if mc_princess_fail_late:
            mc "We tried, your majesty. We planned thoroughly. I even saw her, but... we still couldn't pull it off."
        else:
            mc "We tried, your majesty. We tried, but... we still couldn't pull it off."
        scene 122_s6 with dissolve
        q "I only hope your failure didn't bring down others with you."
        scene 122_s5 with dissolve
        mc "Everyone should be fine, we left before any alarms were raised."
        mc "We thought we could somehow get help regardless, but... well. Before we could think of anything else... there you were."
    scene 122_s6 with dissolve
    q "It doesn't matter now. Hod and I are old friends. He will listen once we arrive to his palace."
    scene 122_s7 with Dissolve(1.0)
    q "As for my daughter..."
    scene 122_s8 with dissolve
    alex "What is it?"
    scene 122_s7 with dissolve
    q "Marching an army west, declaring war would be a disaster."
    q "It's better to play it safe. To continue the oblivious act while we wait for the perfect time to strike."
    scene 122_s8 with dissolve
    mc "Your majesty... are you saying that we should forget about Rebecca?"
    scene 122_s7 with dissolve
    q "Unfortunately... yes. For the time being."
    scene 122_s8 with dissolve
    mc "How could you say that about your daughter?! She doesn't deserve what's happening to her!"
    scene 122_s7 with dissolve
    q "I didn't say she deserved it, [mc]."
    q "It's either a full-out war, or we play it smart and have them continue the charade. We will dismantle them from within. Then... and only then will we strike."
    scene 122_s10 with Dissolve(1.0)
    alex "..."
    scene 122_s9 with dissolve
    mc "Is... is there really no other choice?"
    scene 122_s10 with dissolve
    q "There isn't. It's her... or thousands. Maybe millions. I know who I will pick."
    q "And she would do the same in my place."
    q "Who knows? They might have a change of heart. Maybe they won't go through with it, but I wouldn't count on luck."
    empathy "Your heart stirs. The truth of her words settles into your chest. Going back and trying another rescue would be truly impossible now."
    stop music fadeout 1.0 
    scene 122_s11 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 1.0 volume 0.7 loop
    perception "The carriage breaks down time and time again, so you arrive almost a day late at a massive building with golden arches soaring overhead and colorful ceramic tiles forming intricate mosaics."
    whitlaw "We have arrived at the destination, your majesty."
    q "Behind me, you two. I will do the talking."
    scene 122_s12 with Fade(1.0,1.0,1.0)
    amb "What is the meaning of this? Who are you people? State your—"
    scene 122_s13 with dissolve
    q "Open the gates. I'm the rightful ruler of Irda. Queen Hannah."
    scene 122_s12 with dissolve
    amb "Q-Queen of Irda?! H-How?! I thought you were dead! The ship accident—"
    scene 122_s13 with dissolve
    q "I seem to have lived. Now, Sanoud—open the doors and let me in. I have urgent matters to discuss with the king."
    scene 122_s12 with dissolve
    amb "Open the doors! Immediately!"
    stop music fadeout 1.0 
    scene 122_s14 with Fade(1.0,1.0,1.0)
    play music "ambiance/king_in_red.mp3" fadein 1.0 loop
    perception "You enter the palace, it's exceptionally beautiful and clean. Every surface polished to a mirror shine, every floor a mosaic of colored tiles depicting the history of Nahraya."
    amb "Please keep with me. Don't go anywhere, don't make any sudden moves, and don't touch anything."
    amb "When we reach the king, you kneel. You show respect. And most importantly, you never speak unless—"
    mc "Unless spoken to. I know. I already went through this once."
    amb "You're exempt from kneeling, queen of Irda. But that still doesn't mean you don't show proper respect."
    scene 121_s21 with Fade(1.0,1.0,1.0)
    amb "My liege, I have... I cannot believe I'm saying this, but I have the Queen of Irda with me."
    king "..."
    amb "{size=30}Kneel!{/size}"
    scene 121_s22 with dissolve
    call screen scene120_choice08 with dissolve

label scene122_2:
    scene 121_s29 with Dissolve(1.0)
    king "How... Who are you?! Are you an impostor who came to fool me?!"
    scene 121_s30 with dissolve
    q "It's me, Hod."
    q "*chuckles* The news of my death has been greatly exaggerated. As you can see."
    scene 121_s29 with dissolve
    king "I-Impossible! Explain yourself! I mourned you! I—"
    scene 121_s30 with dissolve
    q "I had an attempt on my life. Orchestrated by my sister, Avery, and Reiner of Eurina. They wanted the throne."
    q "The one sent to act is right here with me."
    alex "..."
    scene 122_s16 with Dissolve(1.0)
    q "Thankfully, she knew better. She refused at the last second after I proposed faking my death."
    q "I was thrown onto a vessel with the intention of letting it sink, unmanned and doomed."
    q "*chuckles* But all those boating lessons benefited me greatly that day. I steered the ship into a nearby shore, where I—"
    scene 122_s15 with dissolve
    king "You met Whitlaw."
    scene 122_s16 with dissolve
    q "Exactly. The stubborn bastard yet lives."
    scene 122_s15 with dissolve
    king "Hannah... I—"
    scene 122_s16 with dissolve
    q "It was a lie, Hod. All of it."
    scene 121_s38 with Dissolve(1.0)
    king "*cough*"
    prince "Father?!"
    amb "My liege?! Bring water! Quickly!"
    scene 121_s37 with dissolve
    king "They lied to me... They played me for a fool."
    king "Reiner... Avery... I welcomed them. I called them allies."
    king "I will get them back for this. I swear on my life."
    scene 121_s38 with dissolve
    q "Calm yourself. We will play their charade. We will let them believe we're still blind. And we will dismantle them from within."
    scene 121_s37 with dissolve
    king "...Yes. They believe I am still blind to it... I can take advantage of that."
    king "Just you wait."
    scene 121_s39 with Dissolve(1.0)
    king "*sigh* As for now... prepare a bedchamber for the Queen and her slave! The biggest one!"
    king "And assign twenty servants to her!"
    scene 121_s40 with dissolve
    servant "Yes, my liege. Immediately."
    scene 122_s17 with Fade(1.0,1.0,1.0)
    q "*laughs* You hear that? I guess you are my slave now."
    scene 122_s18 with dissolve
    mc "If it means sleeping on an actual bed and having access to food and water... I don't mind it."
    mc "Incredible, your majesty. We're closer than ever to getting you right back where you belong."
    scene 122_s17 with dissolve
    q "Patience, [mc]. As I said, we will do this smart. It will take a while."
    scene 122_s18 with dissolve
    mc "Of course. If only Rebecca was... here to see this."
    scene 122_s19 with dissolve
    q "Mourn her. I have been mourning her since the start of my journey here. I thought it would be long enough to finish grieving, but..."
    q "*sigh* But it appears there's not enought time in the world for that."
    scene 122_s20 with dissolve
    jump scene124

label scene123:
    scene 120_s2 with dissolve
    alex "Fuck. I'm genuinely out of ideas."
    alex "If we had the princess, we'd have an easy way inside—but we don't."
    alex "This might be a long shot, but if the Queen were still alive, she might have been here before we even arrived and sorted things out."
    scene 120_s3 with dissolve
    mc "Well, we have neither of those options."
    mc "Hmm... The last time I managed to get an audience with royalty... I had to do something for the city. Something big."
    mc "Something that would benefit them greatly."
    scene 120_s2 with dissolve
    alex "And? What could we possibly offer Nahraya before the axe falls on the princess?"
    scene 120_s3 with dissolve
    mc "I know exactly how we're getting in."
    scene 120_s2 with dissolve
    alex "...And?! Don't keep me hanging."
    scene 120_s3 with dissolve
    mc "It's you. You're our ticket in."
    scene 120_s2 with dissolve
    alex "Me? What are you—"
    alex "Wait, [mc]. Are you talking about that?!"
    scene 120_s3 with dissolve
    mc "Look. I know you had no part in it, but to them, you were. I heard a Nahrayan ambassador talking about it."
    mc "They still think you had a part in it."
    mc "If I turn you in... I get a direct meeting with the king."
    scene 120_s2 with dissolve
    alex "What if they imprison me? Execute me? Have you thought that far ahead?!"
    alex "Besides, my name was already cleared when their ambassador visited us."
    scene 120_s3 with dissolve
    mc "Hmm... then I'll say I captuered you, and want to return you back to Eurina. Your father is looking for you afterall."
    scene 120_s2 with dissolve
    alex "Fuck. We really are desperate, huh?"
    scene 120_s3 with dissolve
    mc "It's the only immediate way I can think of."
    scene 120_s2 with dissolve
    alex "Nghnn... How do we even approach this? Just walk up to the guards and say hi?"
    scene 120_s3 with dissolve
    mc "Turn around. I'll cuff you up."
    mc "You know where the palace is, right?"
    scene 120_s2 with dissolve
    alex "I do. You're just gonna walk me there? Like a prisoner?"
    scene 120_s3 with dissolve
    mc "Yeah. I come in as the one who captured you."
    scene 120_s2 with dissolve
    alex "*sigh* I hope we're not walking into our deaths..."
    scene 123_s1 with Fade(1.0,1.0,1.0)
    perception "You find a length of rope on the ground, discarded from some merchant's stall. You use it to tie Alex's hands together."
    mc "Ready?"
    alex "No."
    impulse "You have no use for her anymore. You're strong on your own now. Use the king and lie to get rid of her."
    mc "..."
    stop music fadeout 1.0
    scene 123_s2 with Fade(1.4,1.0,1.4)
    play music "nature.mp3" fadein 1.0 volume 0.7 loop
    perception "You reach a massive building with golden arches soaring overhead, colorful ceramic tiles forming intricate mosaic art."
    alex "I have a really bad feeling about this, [mc]..."
    scene 123_s3 with Fade(1.0,1.0,1.0)
    mc "I have a prisoner for the king! Reiner's daughter who ran off!"
    guard "None may enter his presence presence without leave."
    mc "Did you not hear me? I said-"
    scene 123_s4 with Dissolve(1.0)
    amb "Hold on. I know this girl..."
    amb "You were at the meeting in Eurnia! Y-You're Reiner's daughter!"
    scene 123_s5 with dissolve
    alex "Yes, yes. I am."
    scene 123_s4 with dissolve
    amb "You! What is the meaning of this?"
    scene 123_s5 with dissolve
    mc "This girl ran off and her father wants her back. I'm here to deliver her to the king."
    mc "I'll only hand her over to the king himself. Directly. I have information he needs to hear."
    mc "Reiner has been lying to your king."
    scene 123_s4 with dissolve
    amb "Lying? About what?"
    scene 123_s5 with dissolve
    mc "About the death of the Queen of Irda."
    amb "..."
    scene 123_s4 with dissolve
    amb "Follow me. And if this is some sort of trick, you'll both regret it."
    scene 123_s5 with dissolve
    stop music fadeout 1.0 
    scene 123_s6 with Fade(1.0,1.0,1.0)
    play music "ambiance/king_in_red.mp3" fadein 1.0 loop
    perception "You enter the palace, it's exceptionally beautiful and clean. Every surface polished to a mirror shine, every floor a mosaic of colored tiles depicting the history of Nahraya."
    amb "Please keep with me. Don't go anywhere, don't make any sudden moves, and don't touch anything."
    amb "When we reach the king, you kneel. You show respect. And most importantly, you never speak unless—"
    mc "Unless spoken to. I know. I already went through this once."
    scene 121_s21 with Fade(1.0,1.0,1.0)
    amb "My liege. This foreigner claims that Reiner of Eurina's daughter was responsible for the attack on the Pleasure Queen."
    amb "He demands an audience in exchange for her capture."
    amb "{size=30}Kneel!{/size}"
    scene 121_s22 with dissolve
    call screen scene120_choice08 with dissolve

label scene123_2:
    scene 121_s29 with Dissolve(1.0)
    king "You match the description perfectly, daughter of Reiner."
    king "I thought her name was already cleared, Sanoud. Reiner himself vouched for her innocence. So what's the meaning of this?"
    scene 121_s30 with dissolve
    amb "My liege, this man claims that Reiner was lying about the death of Irda's queen."
    scene 121_s29 with dissolve
    king "Is that true? Is my trusted ally a liar?"
    scene 121_s30 with dissolve
    mc "He is. And I want you to hear the truth. The real truth."
    scene 121_s29 with dissolve
    king "Go on, then. Make it quick. Afterwards, I can decide to either execute you for wasting my time, or imprison you for kidnapping my friend's daughter."
    king "Choose your words carefully."
    scene 123_s7 with Dissolve(1.0)
    mc "I-I was there too. I know who was really behind the attack."
    mc "It was all a lie, my liege. All of it. Avery and Reiner orchestrated a coup. They assassinated queen Hannah and imprisoned her children, princess Rebecca and the prince."
    scene 123_s8 with dissolve
    king "What madness spills out of your forked tongue? The reports said she died in a ship accident."
    scene 123_s7 with dissolve
    mc "The reports were lies."
    alex "He's right. I was there with him. My father sent me to kill the Queen. And I—"
    scene 123_s8 with dissolve
    king "You accuse your own father of conspiracy? Of murder?"
    scene 123_s7 with dissolve
    alex "Because it's the truth!"
    empathy "The king looks at you with intense hatred, as if he could slice your neck open right there and then."
    mc "My liege, you have to trust me!"
    mc "I know how this sounds, but I'm telling you the truth!"
    scene 123_s12 with Dissolve(1.0)
    king "You enter my palace. You disrespect my name. You disrespect my friends. You dishonor the memory of a queen that I looked up to."
    scene 123_s10 with dissolve
    mc "W-What?"
    scene 123_s12 with dissolve
    king "I should rip off your head where you stand. But just because Reiner's daughter is watching... I will keep my calm. For her sake."
    scene 123_s9 with dissolve
    alex "...Run, [mc]! RUN!"
    scene 123_s12 with dissolve
    perception "Before you even think of running, guards surround you from every direction."
    king "Put this filth in the dungeons! I shall attend his execution myself."
    scene 123_s10 with dissolve
    mc "Please! You're being manipulated!"
    scene 123_s12 with dissolve
    king "Enough. Take him away."
    scene 123_s11 with dissolve
    alex "Get away from him! He's telling the truth! Why won't you listen?!"
    scene 123_s12 with dissolve
    king "It appears he planted false ideas in your mind. Stockholm syndrome, perhaps, or some sort of brainwashing magic."
    king "Don't worry, child. I will send for your father to come and take you home. He will set your thoughts right again."
    scene 123_s13 with Dissolve(1.0)
    minthra "No. No, it cannot end this way. This is wrong. This is all wrong. There must be something I missed..."
    minthra "It absolutely cannot end this way!"
    mc "(Minthra... what are you saying? You will help me, right?)"
    minthra "I will not die with you. I shall find another vessel. A thousand years from now... someone who is competent."
    mc "(W-Where are you going?!)"
    scene 123_s14 with Dissolve(1.0)
    stop music fadeout 5.0
    sensation "You feel your strength slowly sapping away. Your legs shake. Your arms become numb. You vision darkens."
    mc "(You're going to... you're going to kill me... I feel like... sleeping.)"
    scene black with Dissolve(4.0)
    sensation "As if someone reached into your chest and pulled out your heart. The world tilts."
    perception "The last thing you hear is Alex screaming your name."
    scene black with Dissolve(1.0)
    scene bad_ending1 with Dissolve(3.0)
    ""
    return

label scene124:
    scene 121_s43 with Dissolve(2.0)
    mc "(It's time we finally do some real change.)"
    jump scene124_2
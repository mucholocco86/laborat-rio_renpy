label ep12_smc_label:
if ep4_toldDerekAboutJade:
    scene ep12_smc1 with dissolve
    mc "Sage!?"
    scene ep12_smc2 with dissolve
    $ renpy.pause()
    scene ep12_smc3 with dissolve
    sa "What the hell did you do, [name]!? What the hell did you do!?"
    scene ep12_smc4 with dissolve
    $ renpy.pause()
    scene ep12_smc5 with dissolve
    mc "I didn't know who she was to you..."
    scene ep12_smc6 with dissolve
    sa "You didn't know!? Is that your defense!?"
    scene ep12_smc7 with dissolve
    mc "It happened during Hell Week... It was one of our tasks..."
    mc "She came on to me in class, and I didn't think...and...and..."
    scene ep12_smc6 with dissolve
    sa "My mother...? My mother!?"
    scene ep12_smc7 with dissolve
    mc "I'm so sorry... But when I found out she was your mother, it was too late to do anything about it or to tell you."
    mc "I didn't know you were a Burke until we went to your parents' place with Josy and Maya... I swear."
    play sound "sound_effects/shove.mp3"
    scene ep12_smc8 with hpunch
    sa "Get the fuck out of here! Leave!!!"
    scene ep12_smc9 with dissolve
    mc "Sage, no! You have to listen to me."
    mc "Please? What can I do to make it right?"
    play sound "sound_effects/hit.mp3"
    scene ep12_smc10 with hpunch
    sa "LEAVE!!!"
    scene ep12_smc11 with dissolve
    sa "Ow!!!"
    scene ep12_smc12 with dissolve
    mc "Sage... Please..."
    if branchSage:
        $ breakup.append("Sage")
        scene ep12_smc13 with dissolve
        sa "We're through, [name]. We're through."
        scene ep12_smc12 with dissolve
        if branchZoey:
            mc "I'm so sorry, Sage..."
            mc "I didn't mean to hurt you."
        else:
            mc "Not like this... Please?"
    else:
        scene ep12_smc13 with dissolve
        sa "What kind of friend are you? Really?"
        scene ep12_smc12 with dissolve
        mc "I never meant to hurt you. I didn't know... What could I have done?"
        scene ep12_smc13 with dissolve
        sa "You could have not stuck your dick in her!"
        sa "I can't look at you. Leave, [name]..."
        scene ep12_smc12 with dissolve
        mc "I'm so sorry, Sage..."
    if affinity == "DIK":
        scene ep12_smc14 with dissolve
        $ renpy.pause()
    else:
        scene ep12_smc15 with dissolve
        $ renpy.pause()
    scene ep12_smc68 with dissolve
    $ renpy.pause()
    scene ep12_smc69 with dissolve
    $ renpy.pause()
    scene ep12_smc70 with dissolve
    $ renpy.pause()
    if ep5_punchedTybalt:
        play sound "sound_effects/hit.mp3"
        scene ep12_smc73 with hpunch
        $ renpy.pause()
        scene ep12_smc72 with dissolve
    else:
        scene ep12_smc71 with dissolve
    mc "{i}And that was it...{/i}"
    mc "{i}That's how I broke Sage...{/i}"
    stop music fadeout 3
    mc "{i}Everyone makes big mistakes they regret, and this was one of mine.{/i}"
    if branchSage:
        $ new_bio("Sage", "Sage broke up with me after learning what I had done with Jade from Tybalt.")
    else:
        $ new_bio("Sage", "Sage was inconsolable after learning what I had done with Jade from Tybalt.")
elif (branchZoey and not wt_ep11_zoey_kiss_others) and branchSage:
    $ breakup.append("Sage")
    play music "music/ep9/licensed_music/track128.mp3"
    scene ep12_smc16 with fade
    $ renpy.pause()
    scene ep12_smc17 with dissolve
    $ renpy.pause()
    scene ep12_smc18 with dissolve
    mc "Say something..."
    scene ep12_smc19 with dissolve
    sa "Are you going back to your ex-fucking-girlfriend?"
    sa "I wanna strangle you!"
    scene ep12_smc18 with dissolve
    mc "I get it... I made a big mistake. But..."
    mc "As it turns out, I'm in love with her."
    scene ep12_smc20 with dissolve
    sa "You're such a fucking asshole, [name]!"
    scene ep12_smc19 with dissolve
    sa "You told me she was your friend!"
    sa "You made me feel stupid for being upset about it in the first place."
    sa "And now you proved me right in the worst way possible!"
    scene ep12_smc21 with dissolve
    mc "I didn't know what I felt before she told me she loved me."
    mc "And when she did, it all became clear to me."
    scene ep12_smc19 with dissolve
    sa "That's the worst fucking excuse I ever heard!"
    scene ep12_smc22 with dissolve
    sa "Did you cheat on me with her?"
    scene ep12_smc21 with dissolve
    mc "What?"
    scene ep12_smc22 with dissolve
    sa "Did you fuck Zoey while you were with me?"
    scene ep12_smc21 with dissolve
    mc "No... I...didn't fuck her."
    scene ep12_smc19 with dissolve
    sa "Don't you fucking hesitate on me! Tell me what you did!"
    scene ep12_smc21 with dissolve
    mc "We kissed, but that's all."
    scene ep12_smc22 with dissolve
    sa "Kissing is cheating, too."
    scene ep12_smc23 with dissolve
    mc "I know it's bad...but... At least I'm honest about it before taking it further."
    scene ep12_smc24 with dissolve
    sa "Oh, you're honest? Do you expect me to applaud that?"
    scene ep12_smc25 with dissolve
    mc "I get that you're angry. You have every right to be that."
    mc "I've never broken up with someone before, so I don't know what to say."
    mc "Please, don't hate me."
    scene ep12_smc26 with dissolve
    sa "What the fuck did you expect would happen, [name]?"
    sa "I care about you, and you betray me like that."
    sa "*{i}Sobs{/i}* You have no idea how that feels."
    scene ep12_smc25 with dissolve
    mc "I'm so sorry. I wish I didn't feel this way, but I do."
    scene ep12_smc26 with dissolve
    sa "Get out of my sight, [name]. I can't fucking look at you."
    scene ep12_smc27 with dissolve
    $ renpy.pause()
    scene ep12_smc28 with dissolve
    mc "{i}And that was it...{/i}"
    mc "{i}That's how I broke up with Sage...{/i}"
    mc "{i}I left my second girlfriend to return to my first...{/i}"
    stop music fadeout 3
    mc "{i}Maybe I was a cheater and an asshole, but at least I followed my heart.{/i}"
    $ new_bio("Sage", "I broke up with Sage to be with Zoey. Sage didn't take it well.")
elif branchSage and ep12_break_or_tell == "break":
    $ breakup.append("Sage")
    play music "music/ep9/licensed_music/track128.mp3"
    scene ep12_smc16 with fade
    $ renpy.pause()
    scene ep12_smc17 with dissolve
    $ renpy.pause()
    scene ep12_smc18 with dissolve
    mc "Say something..."
    scene ep12_smc29 with dissolve
    sa "[name]... I don't understand."
    sa "Why are you breaking up with me?"
    scene ep12_smc30 with dissolve
    mc "Because I'm not feeling it..."
    scene ep12_smc29 with dissolve
    sa "That's...bullshit."
    scene ep12_smc31 with dissolve
    mc "*{i}Sigh{/i}* I want to feel something, but I don't."
    scene ep12_smc29 with dissolve
    sa "You can't do all the things we've done together and then say you're not feeling anything."
    scene ep12_smc30 with dissolve
    mc "It doesn't matter, Sage. I can't be with you. I wish it were different."
    scene ep12_smc29 with dissolve
    sa "Is there someone else?"
    scene ep12_smc33 with dissolve
    mc "I swear on my life, there's no one else."
    scene ep12_smc34 with dissolve
    if RPsage >= 22:
        sa "Can't we try to figure it out then? Please?"
    else:
        sa "*{i}Sigh{/i}* I mean, I've had doubts too, but..."
    sa "It doesn't make sense to me."
    if RPsage >= 22:
        sa "We're great together."
        scene ep12_smc32 with dissolve
        mc "I can't."
        scene ep12_smc34 with dissolve
    sa "What happened, [name]?"
    scene ep12_smc33 with dissolve
    mc "I can't do this anymore."
    scene ep12_smc35 with dissolve
    sa "*{i}Sobs{/i}* You're not even giving me a fucking reason. What did I do wrong?"
    scene ep12_smc36 with dissolve
    mc "I'm so sorry... You haven't done anything wrong; it's me."
    scene ep12_smc35 with dissolve
    sa "Don't give me that one. That's even worse."
    scene ep12_smc37 with dissolve
    mc "{i}And that was it...{/i}"
    mc "{i}That's how I broke up with Sage...{/i}"
    mc "{i}At that point, I wanted to tell her what I had done.{/i}"
    mc "{i}I was so close to telling her, but I didn't...{/i}"
    stop music fadeout 3
    mc "{i}All I kept thinking was that this was for the best.{/i}"
    $ new_bio("Sage", "I broke up with Sage without telling her the real reason why. She was hurt and didn't understand why I couldn't tell her the truth.")
elif branchSage and ep12_break_or_tell == "tell":
    $ breakup.append("Sage")
    play music "music/ep9/licensed_music/track128.mp3"
    scene ep12_smc16 with fade
    $ renpy.pause()
    scene ep12_smc17 with dissolve
    $ renpy.pause()
    scene ep12_smc18 with dissolve
    mc "Say something..."
    scene ep12_smc38 with dissolve
    sa "I think I'm going to throw up."
    if ep3_acceptedJade and not ep4_fuckedJade:
        sa "You did what with my mother?"
        scene ep12_smc40 with dissolve
        mc "Back when college started, she came on to me in class... She was forward about it."
        mc "She gave me a...handjob in class. And I swear, that was it."
        mc "I know it still is way over the top, considering she's your mom, but..."
    else:
        scene ep12_smc39 with dissolve
        sa "You had sex with my mother?"
        scene ep12_smc40 with dissolve
        mc "Back when college started, she came on to me in class... She was forward about it."
        mc "We connected, and things happened between us..."
        mc "One thing led to another, and I ended up in bed with her."
    scene ep12_smc41 with dissolve
    mc "I didn't know who she was back then, and I didn't know you were related to her."
    mc "If I had known, I would never have done it."
    scene ep12_smc42 with dissolve
    mc "You and I had just started to get to know each other... I didn't know, I swear."
    mc "I know that doesn't undo what I did, and when I found out you were related... I... I..."
    mc "I've felt guilty ever since. And I can't go on pretending it didn't happen."
    scene ep12_smc43 with dissolve
    sa "And when did you find out that she's my mom?"
    scene ep12_smc41 with dissolve
    mc "After we decided to date... Back when we visited your place together with Josy and Maya..."
    if ep4_fuckedJade:
        mc "I realized that I had been there before...and my stomach turned."
    else:
        mc "That's when it clicked...and my stomach turned."
    mc "I wanted to tell you earlier...but I've felt so guilty, and I didn't know how to say it."
    scene ep12_smc42 with dissolve
    mc "I couldn't undo it, and I was scared of losing you."
    mc "But the longer I waited, the worse the guilt got."
    mc "The more my feelings for you grew, the guiltier I felt."
    mc "I considered all the options I had... Telling you, not telling you, breaking up with you to spare your relationship with your mom..."
    scene ep12_smc44 with dissolve
    mc "But I realized that if there was a chance that you could forgive me, I had to try."
    mc "I'm so sorry."
    scene ep12_smc45 with dissolve
    sa "You didn't know she was my mother!? Is that your defense!?"
    scene ep12_smc44 with dissolve
    mc "It is. Try to put yourself in my shoes."
    scene ep12_smc45 with dissolve
    if ep3_acceptedJade and not ep4_fuckedJade:
        sa "Does that make it any better? I would never do that with a teacher."
    else:
        sa "Does that make it any better? I would never fuck a teacher."
    sa "Who are you? I feel like I don't know you."
    scene ep12_smc46 with dissolve
    mc "I made a mistake. I admit it. But I can't take it back."
    play sound "sound_effects/shove.mp3"
    scene ep12_smc8 with hpunch
    sa "And you waited all this fucking time to tell me!"
    sa "Get the fuck out of here! Leave!!!"
    play sound "sound_effects/hit.mp3"
    scene ep12_smc10 with hpunch
    sa "Who does that to someone!?"
    scene ep12_smc11 with dissolve
    sa "Ow!!!"
    scene ep12_smc12 with dissolve
    mc "Sage... Please..."
    scene ep12_smc13 with dissolve
    if RPsage >= 22:
        sa "I thought I loved you. I wanted to be with you..."
    sa "We are so over, [name]. I can't even look at you."
    scene ep12_smc12 with dissolve
    mc "Please... Sage... I don't want this to end."
    scene ep12_smc13 with dissolve
    sa "Well, guess what..."
    sa "This ended the moment your dick touched my mother."
    sa "Get the fuck out of my sight!"
    if affinity == "DIK":
        scene ep12_smc14 with dissolve
    else:
        scene ep12_smc15 with dissolve
    mc "{i}I thought about that moment a lot...{/i}"
    mc "{i}What would have happened if I hadn't confessed?{/i}"
    scene ep12_smc47 with dissolve
    mc "{i}But I did it to try to save our relationship.{/i}"
    stop music fadeout 3
    mc "{i}And I don't regret it.{/i}"
    $ new_bio("Sage", "Sage broke up with me after I told her what I had done with Jade. She was inconsolable and felt betrayed.")
else:
    if not branchSage:
        jump ep12_mv_label
    play music "music/ep2/by_your_side.mp3"
    if ep11_gift_list[4] == 2:
        scene ep12_smc48 with fade
    else:
        scene ep12_smc48b with fade
    $ renpy.pause()
    scene ep12_smc49 with dissolve
    mc "Your brother is an ass."
    if ep11_gift_list[4] == 2:
        scene ep12_smc50 with dissolve
    else:
        scene ep12_smc50b with dissolve
    sa "Yes, he is."
    if ep11_gift_list[4] == 2:
        scene ep12_smc51 with dissolve
    else:
        scene ep12_smc51b with dissolve
    mc "Aren't you gonna ask what he did?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc52 with dissolve
    else:
        scene ep12_smc52b with dissolve
    sa "Oh, did he do something?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc51 with dissolve
    else:
        scene ep12_smc51b with dissolve
    mc "He dropped by to threaten us earlier."
    if ep11_gift_list[4] == 2:
        scene ep12_smc52 with dissolve
    else:
        scene ep12_smc52b with dissolve
    sa "He does that a lot. I wouldn't put much weight into it."
    if ep11_gift_list[4] == 2:
        scene ep12_smc53 with dissolve
    else:
        scene ep12_smc53b with dissolve
    sa "That party you threw got people on Rooster talking."
    if ep11_gift_list[4] == 2:
        scene ep12_smc54 with dissolve
    else:
        scene ep12_smc54b with dissolve
    mc "What are they saying?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc53 with dissolve
    else:
        scene ep12_smc53b with dissolve
    sa "There's a mix of reactions. Some say it was unhinged and derogatory, while many say it was one of the best parties of the year."
    if ep11_gift_list[4] == 2:
        scene ep12_smc54 with dissolve
    else:
        scene ep12_smc54b with dissolve
    mc "What can I say? You missed out on a good one."
    if ep11_gift_list[4] == 2:
        scene ep12_smc55 with dissolve
    else:
        scene ep12_smc55b with dissolve
    sa "I'd say Bella's party was better."
    if ep11_gift_list[4] == 2:
        scene ep12_smc54 with dissolve
    else:
        scene ep12_smc54b with dissolve
    if ep11_mg_party:
        mc "The people on Rooster don't need to know that."
    else:
        mc "I doubt it."
    if ep11_gift_list[4] == 2:
        scene ep12_smc56 with dissolve
    else:
        scene ep12_smc56b with dissolve
    $ renpy.pause()
    if ep11_gift_list[4] == 2:
        scene ep12_smc57 with dissolve
    else:
        scene ep12_smc57b with dissolve
    mc "Speaking of that party..."
    mc "There's something that happened during it that you should know about."
    if ep11_gift_list[4] == 2:
        scene ep12_smc55 with dissolve
    else:
        scene ep12_smc55b with dissolve
    sa "Something juicy?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc54 with dissolve
    else:
        scene ep12_smc54b with dissolve
    mc "Zoey dropped by."
    if ep11_gift_list[4] == 2:
        scene ep12_smc58 with dissolve
    else:
        scene ep12_smc58b with dissolve
    sa "I don't like where this is going."
    if ep11_gift_list[4] == 2:
        scene ep12_smc59 with dissolve
    else:
        scene ep12_smc59b with dissolve
    mc "Nothing happened between us. I mean, something happened, but you shouldn't worry about it."
    if ep11_gift_list[4] == 2:
        scene ep12_smc58 with dissolve
    else:
        scene ep12_smc58b with dissolve
    sa "Spit it out."
    if ep11_gift_list[4] == 2:
        scene ep12_smc59 with dissolve
    else:
        scene ep12_smc59b with dissolve
    mc "She told me she loves me. And she wanted us to get back together."
    if ep11_gift_list[4] == 2:
        scene ep12_smc60 with dissolve
    else:
        scene ep12_smc60b with dissolve
    sa "What the fuck?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc59 with dissolve
    else:
        scene ep12_smc59b with dissolve
    mc "Don't get mad."
    if ep11_gift_list[4] == 2:
        scene ep12_smc60 with dissolve
    else:
        scene ep12_smc60b with dissolve
    sa "Don't get mad!? Didn't I tell you something along these lines would happen?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc59 with dissolve
    else:
        scene ep12_smc59b with dissolve
    mc "You did. But you never had to worry about how I felt."
    if ep11_gift_list[4] == 2:
        scene ep12_smc58 with dissolve
    else:
        scene ep12_smc58b with dissolve
    sa "What did you tell her?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc59 with dissolve
    else:
        scene ep12_smc59b with dissolve
    mc "I told her it was too late for anything to happen. I rejected her."
    mc "And even though I knew this would upset you, I wanted you to know that it happened. You were right."
    if ep11_gift_list[4] == 2:
        scene ep12_smc61 with dissolve
    else:
        scene ep12_smc61b with dissolve
    $ renpy.pause()
    if ep11_gift_list[4] == 2:
        scene ep12_smc62 with dissolve
    else:
        scene ep12_smc62b with dissolve
    sa "Thank you... I appreciate that you told me."
    sa "But that she did that to you... That makes me fume."
    if ep11_gift_list[4] == 2:
        scene ep12_smc64 with dissolve
    else:
        scene ep12_smc64b with dissolve
    mc "Again. Nothing happened between us, Sage. She's just my friend."
    if ep11_gift_list[4] == 2:
        scene ep12_smc65 with dissolve
    else:
        scene ep12_smc65b with dissolve
    sa "Wait! What?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc66 with dissolve
    else:
        scene ep12_smc66b with dissolve
    mc "Huh?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc65 with dissolve
    else:
        scene ep12_smc65b with dissolve
    sa "Are you still calling her your friend? She told you she loves you. How can you be friends with her after that?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc66 with dissolve
    else:
        scene ep12_smc66b with dissolve
    mc "I mean, I... It doesn't change how I feel about her. She's still my childhood friend."
    if ep11_gift_list[4] == 2:
        scene ep12_smc65 with dissolve
    else:
        scene ep12_smc65b with dissolve
    sa "Come on, dude. You have to see it now. She doesn't look at you as a friend anymore."
    sa "She looks at you as someone who got away."
    if ep11_gift_list[4] == 2:
        scene ep12_smc67 with dissolve
    else:
        scene ep12_smc67b with dissolve
    sa "How can you possibly expect that to remain a friendship?"
    sa "It makes me feel ten times worse about you spending time with her now that I know her true intentions."
    sa "Before, it was just a hunch. Now, I know for sure."
    if ep11_gift_list[4] == 2:
        scene ep12_smc66 with dissolve
    else:
        scene ep12_smc66b with dissolve
    mc "I get what you're saying, but..."
    if ep11_gift_list[4] == 2:
        scene ep12_smc67 with dissolve
    else:
        scene ep12_smc67b with dissolve
    sa "But you still want to be her friend."
    if ep11_gift_list[4] == 2:
        scene ep12_smc66 with dissolve
    else:
        scene ep12_smc66b with dissolve
    mc "I haven't given it much thought."
    if ep11_sage_camila_lewd:
        mc "Do you want me to stop being Camila's friend now, too?"
    if ep11_gift_list[4] == 2:
        scene ep12_smc62 with dissolve
    else:
        scene ep12_smc62b with dissolve
    if ep11_sage_camila_lewd:
        sa "That's not the same thing, [name]. What we did with Camila, we did together as a couple."
    sa "To me, there's only one way to go. You can't stay her friend after this, [name]."
    stop music fadeout 3
    if ep11_gift_list[4] == 2:
        scene ep12_smc63 with dissolve
    else:
        scene ep12_smc63b with dissolve
    $ renpy.pause()
    $ new_bio("Sage", "I told Sage about what happened with Zoey at the Christmas party. Sage was concerned about my friendship with Zoey.")
jump ep12_mv_label

label ep12_sage_solo_label:
play sound "sound_effects/season3/lighter.mp3"
play music "music/ep12/licensed_music/track217.mp3"
scene ep12_sage_solo1 with wipeleft
if ep8_told_josy_chad:
    sa "*{i}Humming{/i}* Set us free. Set us free. Set us free..."
else:
    $ renpy.pause()
if ep8_told_josy_chad:
    scene ep12_sage_solo2b with dissolve
    sa "Damn you, catchy Christian radio..."
else:
    scene ep12_sage_solo2 with dissolve
    $ renpy.pause()
scene ep12_sage_solo3 with dissolve
mc "Hey... What's this all about?"
scene ep12_sage_solo4 with dissolve
sa "Surprise!"
scene ep12_sage_solo5 with dissolve
mc "What's the occasion?"
scene ep12_sage_solo7 with dissolve
sa "It's a \"congrats on making it through your first semester\" kind of occasion."
scene ep12_sage_solo6 with dissolve
mc "*{i}Phew{/i}* Good. I thought I missed an anniversary or something."
scene ep12_sage_solo8 with dissolve
sa "Hilarious."
sa "So, how did it go?"
scene ep12_sage_solo9 with dissolve
mc "I am beat. Thoroughly beat. All I see when I close my eyes is a white sheet of paper with my writing on it."
mc "I needed this tonight. Thank you for being so sweet to me."
scene ep12_sage_solo7 with dissolve
sa "You're welcome. I wanted you to have a relaxing evening."
scene ep12_sage_solo10 with dissolve
sa "I prepared something for us to eat..."
sa "Something for us to drink..."
scene ep12_sage_solo11 with dissolve
sa "And something for us to watch."
sa "My sisters watched it at our last movie night without me, and apparently, it's worth your time."
scene ep12_sage_solo9 with dissolve
mc "You're amazing. You did all this for me?"
scene ep12_sage_solo12 with dissolve
sa "I also wanted to apologize... I was rough on you last time, when you told me about Zoey."
sa "And look, I don't want to get into that. It's not about her tonight."
scene ep12_sage_solo13 with dissolve
sa "But what I want to say is that I didn't pose an ultimatum to you."
sa "Jill pointed out to me that maybe it might have felt that way for you..."
scene ep12_sage_solo14 with dissolve
mc "You told Jill about it?"
scene ep12_sage_solo7 with dissolve
sa "Girls talk, [name]. Does that surprise you?"
scene ep12_sage_solo9 with dissolve
mc "No, of course not."
scene ep12_sage_solo13 with dissolve
sa "Anyway, sorry if it came off that way. It wasn't a healthy response on my part."
scene ep12_sage_solo9 with dissolve
mc "I know you only reacted that way because you care. Don't worry, ok? But thanks for the apology."
mc "And again, thanks for this."
scene ep12_sage_solo15 with dissolve
sa "I'm a total noobie when it comes to cheese. They say the smellier the better, but I almost barfed at what the clerk showed me."
scene ep12_sage_solo16 with dissolve
mc "Haha! Did you get a smelly one?"
scene ep12_sage_solo17 with dissolve
sa "Yeah. That's why it's still in a closed container."
sa "It would have soured the mood if it weren't, and you entered the room to a repugnant fart smell."
scene ep12_sage_solo18 with dissolve
mc "HAHAHA! Why did you even buy it then?"
scene ep12_sage_solo19 with dissolve
sa "The clerk was super-convincing!"
sa "But I'm starting to suspect he fooled me into buying the cheese he couldn't normally sell."
scene ep12_sage_solo20 with dissolve
mc "*{i}Gags{/i}* Oh, holy hell! That reeks!"
scene ep12_sage_solo21 with dissolve
sa "See! It smells like ass! I'm so happy you feel that way about it, too."
scene ep12_sage_solo22 with dissolve
mc "You know you have to taste it, yeah?"
scene ep12_sage_solo21 with dissolve
sa "No, no, no. It's for {b}you{/b}."
scene ep12_sage_solo23 with dissolve
sa "No way! HAHA!"
scene ep12_sage_solo24 with dissolve
sa "How was it?"
scene ep12_sage_solo25 with dissolve
mc "I feel like it's not supposed to be in my body. It's so bitter... Fuck."
scene ep12_sage_solo26 with dissolve
sa "Here. Wash it down with some beer."
scene ep12_sage_solo27 with dissolve
$ renpy.pause()
scene ep12_sage_solo28 with dissolve
mc "Ah... Come here. Give me a kiss."
sa "Haha! Eww! Not after you put that ass-cheese in your mouth."
scene ep12_sage_solo29 with dissolve
sa "Haha! STOP!!!"
mc "*{i}Smack{/i}*"
scene ep12_sage_solo30 with dissolve
sa "Oh my God!"
sa "Haha! That was so funny. I didn't think you'd eat that."
scene ep12_sage_solo31 with dissolve
mc "Anything else on the table you want me to enjoy?"
scene ep12_sage_solo30 with dissolve
sa "All of it! That cheese was the only thing in need of a container."
scene ep12_sage_solo31 with dissolve
mc "The rest does look delicious."

scene ep12_sage_solo32 with dissolve
sa "So, when are you heading back home?"
scene ep12_sage_solo33 with dissolve
mc "I think the day after tomorrow. What are your holiday plans?"
scene ep12_sage_solo34 with dissolve
sa "I'll celebrate Christmas with Mom and Tybalt."
scene ep12_sage_solo33 with dissolve
menu:
    "What about your dad?":
        mc "What about your dad?"
        scene ep12_sage_solo35 with dissolve
        sa "He didn't even offer. Maybe he expected me to suggest it, but I didn't, so..."
        scene ep12_sage_solo33 with dissolve
        mc "That must be tough for you."
    "I'm sad to hear that":
        mc "I'm sad to hear that."
        scene ep12_sage_solo34 with dissolve
        sa "Which part of it? Celebrating with a broken family or with Tybalt."
        scene ep12_sage_solo33 with dissolve
        mc "Both, but for different reasons."
scene ep12_sage_solo35 with dissolve
sa "It wasn't going to be a merry Christmas regardless. I'll have to get through it."
scene ep12_sage_solo33 with dissolve
mc "I'd ask you to join us, but you should be with your family."
scene ep12_sage_solo34 with dissolve
sa "Yeah. Mom needs it."
sa "Other than that, I'll be around. The New Year's party won't take care of itself."
scene ep12_sage_solo33 with dissolve
mc "I swear, I'll help out more with it."
scene ep12_sage_solo32 with dissolve
sa "You did well already."
sa "Did you get your outfit sorted?"
scene ep12_sage_solo33 with dissolve
mc "For New Year's Eve?"
scene ep12_sage_solo32 with dissolve
sa "Yeah."
scene ep12_sage_solo33 with dissolve
menu:
    "Not yet":
        mc "No, not yet."
    "Joke":
        mc "I don't even know what underwear I'll wear tomorrow, let alone if I will change them."
        scene ep12_sage_solo36 with dissolve
        sa "Eww!"
        scene ep12_sage_solo33 with dissolve
mc "Do you think that far ahead?"
scene ep12_sage_solo32 with dissolve
sa "Normally, no. But for New Year's Eve, you'd better."
sa "I have ordered mine already. It's red and hot. You'll love it."
scene ep12_sage_solo37 with dissolve
mc "Show it to me."
scene ep12_sage_solo32 with dissolve
sa "You're not seeing it in advance. I want to surprise you with it."
scene ep12_sage_solo33 with dissolve
mc "I won't be surprised. I already know it's red."
scene ep12_sage_solo38 with dissolve
sa "It has a plunging neckline. Seriously. The cleavage is insane! "
if ep9_sage_vanilla:
    scene ep12_sage_solo39 with dissolve
    mc "I know you'll look amazing in it."
    scene ep12_sage_solo40 with dissolve
    sa "You'd say that to anything I'd choose to wear, wouldn't you?"
    scene ep12_sage_solo39 with dissolve
    mc "Seems like you're on to me."
else:
    scene ep12_sage_solo39 with dissolve
    mc "I bet your breasts will look amazing in it."
    scene ep12_sage_solo40 with dissolve
    sa "*{i}Scoffs{/i}* You would say that."

if ep11_sage_camila_lewd:
    scene ep12_sage_solo41 with dissolve
    sa "Oh! I saw Camila's dress too. If you think mine sounds sexy, you should see hers."
    sa "She's not even going to wear underwear underneath it."
    scene ep12_sage_solo42 with dissolve
    mc "How is that a part of the design?"
    scene ep12_sage_solo41 with dissolve
    sa "Well, it shows skin all the way from the top down to the toes, and wearing underwear would ruin how the dress is supposed to look."
    scene ep12_sage_solo42 with dissolve
    mc "Sounds hot."
    scene ep12_sage_solo41 with dissolve
    sa "Yeah."
    sa "Have you spoken to her since our threesome?"
    scene ep12_sage_solo43 with dissolve
    mc "Some, but not a lot."
    scene ep12_sage_solo44 with dissolve
    sa "And how were things between you?"
    scene ep12_sage_solo43 with dissolve
    mc "Do you mean if it was weird in any way?"
    scene ep12_sage_solo44 with dissolve
    sa "Yeah."
    scene ep12_sage_solo43 with dissolve
    mc "It was pretty much the same. She's still Cammy. Why? Did she say something?"
    scene ep12_sage_solo45 with dissolve
    sa "She made some comments to me. Girl talk, you know?"
    scene ep12_sage_solo43 with dissolve
    mc "No, I don't know what you'd say as a girl after doing that together. Enlighten me."
    scene ep12_sage_solo45 with dissolve
    sa "Well, she said she enjoyed it and found it cool that I would share you with her like that."
    sa "Actually, I'm downplaying it..."
    scene ep12_sage_solo46 with dissolve
    sa "She loved it..."
    scene ep12_sage_solo47 with dissolve
    mc "She loved it? Oh... That's nice. Or did that make you feel jealous?"
    scene ep12_sage_solo48 with dissolve
    sa "No, her comments didn't annoy me, and it was hot to watch you fuck her."
    scene ep12_sage_solo46 with dissolve
    sa "But that's not how I should have felt... Yet I did."
    scene ep12_sage_solo43 with dissolve
    mc "You both enjoyed it and didn't enjoy it?"
    scene ep12_sage_solo48 with dissolve
    sa "No, I enjoyed it."
    sa "But I feel like I shouldn't have enjoyed it that much. I'm not making any sense, am I?"
    scene ep12_sage_solo43 with dissolve
    mc "It's somewhat confusing, yeah."
    scene ep12_sage_solo46 with dissolve
    sa "I get it. I managed to confuse myself."
    sa "Anyway..."

scene ep12_sage_solo41 with dissolve
sa "Wanna watch the movie?"
scene ep12_sage_solo42 with dissolve
mc "Yeah, let's. You went through all this trouble for it."
scene ep12_sage_solo49 with dissolve
sa "I hope it doesn't suck. They said Arieth didn't laugh once, so I have high hopes for it."
if not ep9_sage_vanilla:
    stop music fadeout 3
    scene ep12_sage_solo50 with dissolve
    $ renpy.pause()
else:
    scene ep12_sage_solo51 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    scene ep12_sage_solo52 with dissolve
    $ renpy.pause()
$ new_bio("Sage", "Sage surprised me after my finals with food, drinks and a movie. It showed me that she truly cared about me. It was heartwarming.")
if not ep9_sage_vanilla:
    $ mgallery_add_photo("ep12_sage_solo_pic1")
else:
    $ mgallery_add_photo("ep12_sage_solo_pic1b")
$ mgallery_add_photo("ep12_sage_solo_pic2")



jump ep12_dikmas_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

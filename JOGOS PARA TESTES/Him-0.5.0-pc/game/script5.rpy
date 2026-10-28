label scene124_2:
    if mc_bought_brothel:
        $ princess_favor += 2
        $ queen_favor += 2
    if not ava_dead:
        $ princess_favor += 1
        $ queen_favor += 1
    if not mc_killed_alice:
        $ princess_favor += 1
        $ queen_favor += 1
    if mc_helped_lena or mc_helped_jenny:
        $ princess_favor += 1
        $ queen_favor += 1
    if mc_helped_ruby:
        $ princess_favor += 1
        $ queen_favor += 1
    if mc_agree_help_thulkin:
        if not mc_influence_cheiftain_bad:
            $ princess_favor += 1
            $ queen_favor += 1
    if mc_princess_alex:
        $ princess_favor += 1
        $ queen_favor += 1
    if mc_convinced_nadia_stay:
        $ princess_favor += 1
        $ queen_favor += 1
        if mc_offer_nadia_coin:
            $ princess_favor += 1
            $ queen_favor += 1
    if mc_save_queen:
        $ princess_favor += 1
        $ queen_favor += 1

    if mc_took_reiner_money and not mc_took_reiner_money_first:
        $ alex_love -= 30

    $ queen_love = 0

    if not mc_killed_reham_counted:
        if mc_killed_reham:
            $ mc_karma -= 6

    if not mc_killed_lena_counted:
        if mc_betray_lena:
            $ mc_karma -= 6
        elif mc_killed_lena:
            $ mc_karma -= 4

    if not mc_influence_cheiftain_bad_counted:
        if mc_influence_cheiftain_bad:
            $ mc_karma -= 5

    if not quest_witch_amelia_dead_counted:
        if quest_witch_amelia_dead:
            $ mc_karma -= 3

    if not mc_killed_alice_counted:
        if mc_killed_alice:
            $ mc_karma -= 4

    if mc_karma <= 0:
        $ mc_karma = 1

    if maia_pussy_sex > 0:
        $ maia_pussy_virgin = False
        $ maia_virgin = False
    if maia_anal_sex > 0:
        $ maia_anus_virgin = False
        $ maia_virgin = False
    if maia_pregnant:
        $ maia_pussy_virgin = False
        $ maia_virgin = False

    if mc_princess_100:
        $ reb_sick = True

    stop music fadeout 1.5
    scene 124_s1 with Fade(1.5,1.0,1.5)
    if mc_princess_success:
        n_palace "Here you are, princess of Irda. This room has been specifically arranged by his royal highness."
        n_palace "He assigned you several servants as well. They are at your disposal. Please call on them if you require anything at all."
        r "Ermm... thank you. You may leave. We'll manage from here."
        n_palace "As you wish, mistress."
        play music "side_event6.mp3" fadein 3.0 loop
        scene 124_s2 with Dissolve(1.0)
        r "Gods... This is nothing like my room in Irda."
        mc "Careful getting too attached. You still have a home somewhere else. A kingdom that needs its princess back."
        r "I know, I know. I haven't forgotten. But still—"
        scene 124_s3 with Dissolve(1.0)
        r "Do you see these silk sheets? The gold plating on everything? Even the doorknobs are gilded. I wonder how much all this cost them..."
        r "More than my entire wardrobe, probably. Maybe more than my entire wing of the castle."
        scene 124_s4 with Dissolve(1.0)
        mc "Is Nahraya wealthier than Irda?"
        scene 124_s5 with dissolve
        r "Are you kidding? It's not even close. They overshadow us in everything, not just wealth."
        r "Military, economy, size. They've got trade routes we can only dream of. Their navy controls the southern seas."
        r "Even I, who barely know anything about this stuff, know that."
        scene 124_s4 with dissolve
        call screen scene124_choice00 with dissolve
        mc "That's not true. There's one thing Irda is better at. One thing Nahraya can never match."
        scene 124_s5 with dissolve
        r "Hmm? And what is that?"
        scene 124_s4 with dissolve
        call screen scene124_choice01 with dissolve

    else:
        jump scene125

label scene124_choice00_op2:
    mc "That's... interesting and all, but come on, let's sit for a bit."
    scene 124_s5 with dissolve
    r "Fair enough. It would be a shame to not use all these gold gilded couches."
    r "I also want to talk to you about home."
    scene 124_s4 with dissolve
    jump scene124_3


label scene124_choice01_op1:
    $ reb_love += 10
    mc "Nahraya doesn't have... you."
    mc "All this gold. All this wealth and power doesn't even begin to compare. Just this one thing makes Irda better... Just you."
    scene 124_s6 with dissolve
    r "I—"
    if not mc_reb_breakup_final:
        r "[mc]... You seriously can't wait, huh?"
        r "We just finished convincing the king of Avery's plot, I still don't how I did it, and there are servants outside the door. And you're standing there, saying things like that..."
        scene 124_s8 with dissolve
        r "I told you we will. But please... keep it in your pants for the moment."
        scene 124_s7 with dissolve
        mc "It's hard, seeing after so long. I missed your... cold touch."
        scene 124_s8 with dissolve
        r "Cold? Ouch. Is that how you remember me?"
        scene 124_s7 with dissolve
        mc "People change."
        scene 124_s8 with dissolve
        r "Fine~ I'm not going to act like I don't want it too, but hold on. I need to know a few things about Irda."
        r "Come on. Sit with me."
        scene 124_s7 with dissolve
    else:
        scene 124_s8 with dissolve
        r "[mc]... Are you trying to flirt with me a day after you rejected me?"
        r "We just finished convincing the king of Avery's plot, I still don't how I did it, and there are servants outside the door. And you're standing there, saying things like that..."
        scene 124_s7 with dissolve
        mc "I didn't mean it in a romantic way, I meant your character. Your city needs you, your people need you."
        scene 124_s8 with dissolve
        r "Well... thank you. *giggles* I appriciate the 'not romantic' compliment."
        r "Come on. Sit with me. I need you to tell me about a few things."
        scene 124_s7 with dissolve
    jump scene124_3

label scene124_choice01_op2:
    scene 124_s10 with Dissolve(1.3)
    mc "The scenery looks better in Irda. Everywhere I look around here, it's just... yellow."
    mc "Even the sky looks beige half the time."
    r "Hmm... I suppose so. It might get tiring, waking up every morning to the same sand dune. Over and over. For the rest of your life."
    scene 124_s4 with Dissolve(1.0)
    mc "See? Irda has forests, mountains, and rivers."
    scene 124_s5 with dissolve
    r "True. But when you're wealthy enough, you can just bring the forest to the desert."
    r "Did you see the king's courtyard when we arrived? It's like a whole different world in there."
    r "Cool and green and... not yellow. They shipped in soil from the coast. The trees are probably older than the palace."
    scene 124_s4 with dissolve
    mc "*chuckles* Come on, that's cheating."
    scene 124_s5 with dissolve
    r "It is what it is. Come. Sit with me."
    scene 124_s4 with dissolve
    jump scene124_3

label scene124_choice01_op3:
    scene 124_s9 with Dissolve(1.3)
    mc "The food. Irda has better food. Hands down."
    r "The food?! We're in the culinary capital of the desert, and you're saying Irda has better food? Have you even tried eating anything from here yet?"
    scene 124_s4 with Dissolve(1.0)
    if not mc_killed_reham:
        mc "Well... I have had some tea, and rice..."
        scene 124_s5 with dissolve
        r "That's it? You have no right to judge yet."
    else:
        mc "No... not yet."
        scene 124_s5 with dissolve
        r "Nothing? Then how can you judge?"
    scene 124_s4 with dissolve
    mc "You're right. My bad."
    scene 124_s5 with dissolve
    r "Come on. Let's sit. My legs are aching."
    scene 124_s4 with dissolve
    jump scene124_3

label scene124_3:
    scene 124_s11 with Fade(1.0,0.5,1.0)
    r "I need to know a few things about what's happening. Back home. In our hometown... or just {i}my{/i} hometown?"
    r "I can't believe I'm only asking this now, but where are you from, [mc]? Really?"
    r "I've known you for so long, and I've never asked. I just... accepted that you were there."
    scene 124_s13 with dissolve
    mc "Well... it's complicated."
    scene 124_s12 with dissolve
    r "Ah, right. Back when Darius first brought you to the castle, he told my mother that you had some sort of amnesia."
    r "That you couldn't even remember basic things like where you lived, or what you used to do."
    scene 124_s13 with dissolve
    mc "He was right. I couldn't. At the time."
    scene 124_s12 with dissolve
    r "So you do now?"
    scene 124_s13 with dissolve
    mc "..."
    scene 124_s14 with dissolve
    r "What's wrong? [mc]?"
    r "I-If you don't want to talk about it, it's fine. In fact, forget I said anything. I didn't mean to pry."
    r "You're like Maia—some things are too painful to share I suppose."
    scene 124_s15 with dissolve
    mc "No, no. It's not like that. I'm not hiding it because it hurts. I'm hiding it because..."
    mc "...because I have no attachment to that world anymore. It isn't my place. It was never really my place, even when I lived there."
    if not mc_reb_breakup_final:
        mc "My place is here. With you. With everyone who's counting on me."
    else:
        mc "My place is here. With everyone who's counting on me."
    scene 124_s14 with dissolve
    r "'That world'? What do you mean, 'that world'? [mc], you're talking like you're from somewhere... else."
    r "Where are you from?"
    scene 124_s15 with dissolve
    call screen scene124_choice02 with dissolve

label scene124_choice02_op1:
    stop music fadeout 1.0
    $ mc_told_reb_other_world = True
    mc "I'm from a place that doesn't exist on any map you've ever seen. A world with no magic. No kings or queens. No ogres or dragons."
    play music "breakup.mp3" fadein 3.0 loop
    mc "It's a lot more boring than here, but... predictable."
    scene 124_s14 with dissolve
    r "[mc]..."
    scene 124_s15 with dissolve
    mc "I'm not making it up. I woke up in Irda with no memories of how I got there. Darius found me wandering near the border."
    mc "He took me in. Gave me a purpose. And over time, the memories started coming back—fragments, pieces, enough to know I don't really belong here."
    scene 124_s14 with dissolve
    r "Why didn't you tell me? All this time, you knew you were from another world, and you never said a word?"
    scene 124_s15 with dissolve
    mc "Would you have believed me?"
    scene 124_s16 with Dissolve(1.0)
    r "I don't know. Maybe not. But now... after everything I've seen... another world doesn't seem so impossible."
    r "Do you miss it? Your old life?"
    scene 124_s17 with dissolve
    mc "No, that's what I meant. I have no attachment to it. No family waiting for me, no life I'm desperate to return to."
    mc "It was... predictable, sure. But it wasn't home."
    if not mc_reb_breakup_final:
        mc "You on the other hand... You do."
        scene 124_s16 with dissolve
        r "That's stangly terrifying yet... beautiful. [mc]... You're from another world, and you chose me."
        scene 124_s17 with dissolve
        mc "I'd choose you every time."
    scene 124_s16 with dissolve
    r "I still don't understand... why? Why did you come here?"
    scene 124_s17 with dissolve
    mc "It wasn't my choice, it was because—"
    scene 124_s19 with dissolve
    mc "Gahnn!"
    sensation "Something twists around your windpipe, a sharp pain squeezes the breath from your lungs."
    scene 124_s18 with dissolve
    r "[mc]?!"
    scene 124_s19 with dissolve
    mc "I-I'm fine. I don't know... I couldn't, the words just..."
    scene 124_s18 with dissolve
    r "Don't strain yourself. Maybe it will come back to you one day? Like how other things did."
    scene 124_s19 with dissolve
    mc "...Maybe."
    scene 124_s20 with Dissolve(1.0)
    mc "(Fuck! I wanted to tell her about you, Minthra, but every time I try, my throat seizes up and I can't breathe!)"
    minthra "She does not need to know."
    jump scene124_4

label scene124_choice02_op2:
    mc "Let's change the subject. It's not important. What matters now is what happens next."
    scene 124_s14 with dissolve
    r "[mc]..."
    scene 124_s15 with dissolve
    mc "I'm serious. My past doesn't matter. Not compared to everything else we're facing. Let's focus on what's ahead, not what's behind."
    r "..."
    scene 124_s12 with Dissolve(1.0)
    r "Alright. We'll leave it for now. But one day, when this is all over... I want to know. Everything. Where you came from, who you were before. All of it."
    scene 124_s13 with dissolve
    mc "Maybe one day."
    scene 124_s12 with dissolve
    r "You're a mystery, [mc]. And somehow, despite all of it—despite not knowing where you came from or how you got here—you're the most real thing in my life."
    if not mc_reb_breakup_final:
        r "Don't ever disappear on me. I've lost too many people already. I can't lose you too."
    else:
        r "Don't ever disappear on me. I've lost too many people already. I can't lose you too."
        r "*ahem* As a friend, of course."
    scene 124_s13 with dissolve
    mc "*chuckles* I'm not going anywhere. At least not {i}too{/i} far."
    jump scene124_4

default princess_favor = 0
default queen_favor = 0

label scene124_4:
    if mc_told_reb_other_world:
        scene 124_s21 with dissolve
        r "Umm... Just to be sure... y-you're not... you know..."
        scene 124_s20 with dissolve
        empathy "Her tone lowers to almost a whisper. There's a fear of someone who's heard too many stories and is suddenly afraid one of them might be true."
        mc "Hmm?"
        scene 124_s21 with dissolve
        r "You know! The thing! The... the stories!"
        scene 124_s20 with dissolve
        mc "I don't..."
        scene 124_s21 with dissolve
        r "Ugh! You're not one of {i}them{/i}, are you? {size=30}A-A devil...{/size}"
        scene 124_s20 with dissolve
        mc "A devil!?"
        scene 124_s21 with dissolve
        r "Haha... right, no way, right? That's ridiculous."
        scene 124_s20 with dissolve
        mc "What brought this up? Becky, you're shaking."
        scene 124_s23 with dissolve
        r "Forget it. I just read too much creepy stuff as a child. The castle library had all these old texts. Ancient legends, forbidden lore. Stuff like that."
        r "There are so many stories of devils taking the form of other races. Humans, elves, beastfolk... they can look like anyone."
        r "I suppose the saving grace here is that they at least remember the memories of the person whose form they take. They have to, to maintain the disguise."
        scene 124_s22 with dissolve
        mc "Becky... are you seriously asking me if I'm some... demon in disguise? After everything I've done for you?"
        scene 124_s23 with dissolve
        r "You're right. I'm sorry. That was stupid."
        scene 124_s22 with dissolve
        mc "Besides, even if I was, would I really tell you?"
        scene 124_s23 with dissolve
        r "Heh. I guess not."
        scene 124_s22 with dissolve
        mc "Exactly. Terrible strategy for a master of deception."
        scene 124_s24 with dissolve
        if not mc_reb_breakup_final:
            r "But you're no devil. You're just my parasite husband who got really lucky~"
        else:
            r "But you're no devil. You're just my parasite saviour who got really lucky~"
        scene 124_s25 with Dissolve(1.0)
        mc "You're still on about that..."
    else:
        scene 124_s25 with Dissolve(1.0)
    stop music fadeout 1.0
    r "*giggles* Anyway, I wanted to ask you about Irda. What's happening out there? It's been too long in that cellar. Tell me everything."
    mc "Oh, man. Where do I even begin?"
    mc "Umm, there's... well. I'll just leave the complicated parts for last."
    play music "hope/mountain_mist.mp3" fadein 3.0 loop
    if mc_bought_brothel:
        scene 124_s26 with Dissolve(1.5)
        mc "*ahem* I'm proud to say that I'm the owner of a business right now! A legitimate establishment. Bought and paid for with hard-earned coin."
        r "*chuckles* Business? What business? What could you possibly—"
        if mc_changed_to_tavern:
            mc "A tavern! [brothel_name]."
            r "A tavern?"
            mc "Yup!"
        else:
            mc "A brothel! [brothel_name]."
            r "A... brothel? You bought a brothel."
            mc "I did."
        scene 124_s27 with Dissolve(1.0)
        r "Why? Were they the only ones willing to sell to a fugitive? Did every other merchant in the city slam their doors in your face?"
        mc "Nobody knew I was a fugitive. Diana—she's the manager, a former worker there—she told me she'd use a fake name on the ownership papers."
        mc "She'll manage the place in my place for now. She's terrifyingly sharp."

        if mc_hired_ruby and mc_hired_sarah:
            scene 124_s28 with Dissolve(1.0)
        elif mc_hired_ruby:
            scene 124_s48 with Dissolve(1.0)
        elif mc_hired_sarah:
            scene 124_s49 with Dissolve(1.0)
        else:
            scene 125_s12 with Dissolve(1.0)
            
        if mc_changed_to_tavern:
            r "I see. And the reason for this... acquisition was?"
            r "Honestly, I can't name a single reason why owning a tavern would benefit you, unless it was just to splurge on coin you didn't have."
            mc "That's where you're wrong. A tavern is a great place to learn information."
            mc "Think about it. Officials visit. Merchants visit. Guards, nobles."
        else:
            r "I see. And the reason for this... acquisition was?"
            r "Honestly, I can't name a single reason why owning a brothel would benefit you, unless it was just to splurge on coin you didn't have."
            mc "That's where you're wrong. A brothel is a great place to learn information."
            mc "Think about it. Officials visit. Merchants visit. Guards, nobles."

        mc "All of them with loose lips and too much to drink. And Diana's ears are large. Figuratively."
        scene 124_s32 with Dissolve(1.0)
        mc "She's the reason I was able to learn so much about Avery and Reiner."
        scene 124_s31 with dissolve
        r "If you put it that way... Fine. What else did you do?"
        scene 124_s32 with dissolve
    scene 124_s35 with Dissolve(1.3)
    mc "You know Ava, right? The royal examiner?"
    r "Yes. Of course. What about her?"

    if not ava_dead:
        if mc_princess_ava:
            mc "She's in on it too. As a matter of fact, she even helped in your rescue."
        else:
            mc "She's in on it too."
        r "A-Are you serious? Ava? The one my mother used to call 'the cold hearted sorceress'? I doubt it was easy to convince her."
        r "I never spoke to her directly, but I always had the impression she was... unswayable. Completely devoted to her role."
        mc "Well... I got lucky. There was a situation involving her friend, Kathrine—a mercenary who'd been thrown in the dungeon."
        scene 124_s36 with dissolve
        mc "I managed to get her out. Ava was indebted to me afterwards."
        r "You getting lucky has been quite the theme so far."
        r "Are you sure someone isn't pulling the strings for you behind the scenes?"
        mc "Haha... I... I'm not sure. Maybe."
        scene 125_s11 with Dissolve(1.0)
        if mc_killed_alice:
            mc "There's also, Alice the lieutenant. Well, {i}former{/i} lieutenant now. She attacked out of nowhere, trying to capture me. I had to defend myself."
            r "[mc]..."
            mc "I promise I had no other choice."
            r "*sigh* I believe you. Still. It's sad nontheless."
            scene 124_s34 with Dissolve(1.0)
        else:
            mc "There's also, Alice the lieutenant. Well, {i}former{/i} lieutenant now. She attacked out of nowhere, trying to capture me. But I managed to convince her not to. For now at least."
            r "Good. At the end of the day, they're our loyal soldiers."
            scene 124_s32 with Dissolve(1.0)
    else:
        mc "She's... dead. I killed her. After she attacked me."
        r "What? [mc]... you... y-you killed someone?"
        mc "I did. I wanted her help with something—needed it, actually. But she attacked me. Called me a traitor. Said she'd bring me to Avery... I had no choice."
        scene 124_s36 with dissolve
        r "I see... I never spoke to her directly, but I always had the impression she was... unswayable. Completely devoted to her role."
        r "If she attacked you, then... it's self defense, right?"
        if mc_killed_alice:
            scene 125_s11 with dissolve
            mc "Right. No choice. The same happened with Alice—a former lieutenant. She attacked out of nowhere. I had to defend myself."
            r "..."
            scene 124_s34 with Dissolve(1.0)
        else:
            mc "Right. No choice."
            scene 125_s11 with dissolve
            mc "There's also, Alice—a former lieutenant. She attacked out of nowhere, trying to capture me. But I managed to convince her not to. For now at least."
            r "Good. At the end of the day, they're our loyal soldiers."
            scene 124_s32 with Dissolve(1.0)

    $ people = ["Alex"]

    if mc_helped_lena:
        $ people.append("Lena, I saved her daughter from slavery")
    elif mc_helped_jenny:
        $ people.append("Jenny, the daughter of a rich noble")

    if mc_agree_help_thulkin:
        $ people.append("Thulkin and his sister, Millicent")

    $ people_part = ". ".join(people) + "."

    $ guards_part = "Joan and Lewis, two guards who risked their lives to get us access to the cellar."

    if quest_witch_amelia_alive_free:
        $ amelia_part = " Even the witch, Amelia."
    else:
        $ amelia_part = ""

    $ final_message = "There are a few others who were in on it too. " + people_part + " " + guards_part + amelia_part
    if mc_princess_ava:
        mc "[final_message]"
        if quest_witch_amelia_alive_free and mc_agree_help_amelia_milking:
            r "Amelia? Are you talking about the witch who kidnapped dozens of our people."
            scene 124_s34 with dissolve
            mc "She's changed. I promise."
            scene 124_s33 with dissolve
            r "Sure..."
            scene 124_s34 with dissolve
    else:
        mc "[final_message]"
        mc "During your rescue, I had the help of Amelia. Without her, we wouldn't have been able to get through the sewers."
        scene 124_s33 with dissolve
        r "I see... That Amelia. The witch who kidnapped dozens of our people."
        scene 124_s34 with dissolve
        mc "She's changed. I promise."
        scene 124_s33 with dissolve
        r "Sure..."
        scene 124_s34 with dissolve

    if mc_convinced_nadia_stay:
        scene 124_s30 with Dissolve(1.5)
        mc "There's also Nadia, a woman who I helped with her business problem. She's thinking of expanding into a bigger shop."
        mc "Maybe one day she'll be the new 'king of the market'. If I can make it happen, I'll get another window into the city."

    if princess_favor >= 7:
        scene 124_s31 with Dissolve(1.0)
        r "Aside from Alex, I don't really know any of the others. You sure were busy, huh? Building an entire resistance while I was chained to a wall."
        r "You have a knack for pulling others to you, [mc]. Perhaps..."
        scene 124_s32 with dissolve
        mc "Perhaps what?"
        scene 124_s31 with dissolve
        r "F-Forget it. We'll talk about it when the time is right."
        scene 124_s32 with dissolve
    else:
        scene 124_s33 with Dissolve(1.0)
        r "Sure. Is... is that all? The list of allies?"
        scene 124_s34 with dissolve
        mc "Hmm? Yeah, that's all. Well, there's one last thing, but you seem disappointed. Like you were expecting more."
        scene 124_s33 with dissolve
        r "*sigh* Forget it. I just thought... nevermind."
        scene 124_s34 with dissolve

    mc "If you say so. There's one last thing you need to know..."
    r "Hmm?"
    mc "After I left the castle to look for Maia, I got into quite a bit of trouble. With Abel. With Darius and his guards. And... with Gaius."
    scene 124_s33 with dissolve
    r "I heard tids and pieces from the guards outside the cellar. Something about the market being destroyed... an explosion..."
    scene 124_s34 with dissolve
    mc "Yeah. It was unavoidable, I assure you. But... because of what happened, because of the fight..."
    scene 124_s37 with Dissolve(1.0)
    mc "...this happened. I don't know if you never noticed or if you did and just didn't wanna say anything."
    r "Hmm? What is—"
    stop music fadeout 1.0
    scene 124_s38 with vpunch
    r "AHHHHHHHHHHH!"
    play music "sad/reb2.mp3" fadein 3.0 loop
    n_palace "Princess? Princess! Is everything fine in there?! Should I summon the guards?!"
    r "No! It isn't! Nothing is fine!"
    scene 124_s39 with Dissolve(1.0)
    mc "Hey, hey. Calm down... they'll think we're being assassinated in here."
    r "[mc]!"
    scene 124_s40 with dissolve
    r "How are you so calm?! You... you lost your hand! Your actual hand! Oh, Gods! It's gone! It's completely gone!"
    scene 124_s41 with dissolve
    mc "It's fine! I swear. In fact, it feels even better than before. I'm getting used to it."
    scene 124_s40 with dissolve
    r "Ghhhnn! I'm so, so sorry!"
    scene 124_s41 with dissolve
    mc "Please, Becky. You had nothing to do with it. I made my choices, and I'd make them again. Now, can you please stop screaming!"
    r "..."
    scene 124_s40 with dissolve
    r "A-Alright... Alright. I'm calm. I'm calm."
    
    if princess_favor >= 7:
        if mc_told_reb_other_world:
            if mc_bought_brothel:
                r "You're from another world. You managed to buy a buisness. You recruited lots of people to your cause. And you lost your hand. All while I was sitting in a cellar, feeling sorry for myself."
            else:
                r "You're from another world. You recruited lots of people to your cause. And you lost your hand. All while I was sitting in a cellar, feeling sorry for myself."
        else:
            if mc_bought_brothel:
                r "You managed to buy a buisness. You recruited lots of people to your cause. And you lost your hand. All while I was sitting in a cellar, feeling sorry for myself."
            else:
                r "You recruited lots of people to your cause. And you lost your hand. All while I was sitting in a cellar, feeling sorry for myself."
        
        r "This is too much for me... You've been out here fighting a war I didn't even know was happening."
        scene 124_s41 with dissolve
        mc "You're strong. You're still standing. That's what matters."
        scene 124_s40 with dissolve
        r "God's damn it!"
        scene 124_s41 with dissolve
        mc "What is it now?"
        scene 124_s43 with dissolve
        stop music fadeout 2.0 
        r "I'm... I'm falling for you... All over again. Harder than before. Harder than I thought was possible."
        play music "reb.mp3" fadein 4.0 loop
        r "You're... you're so incredible... you just kept going. You're so much more than me."
        scene 124_s42 with dissolve
        mc "Don't say that. Your story hasn't began yet."
        if not mc_reb_breakup_final:
            scene 124_s43 with dissolve
            r "I need you, Gods do I need you! Every part of you. Every scar. Every secret. Even that ridiculous metal hand."
            scene 124_s42 with dissolve
            mc "*chuckles* What's with that weird look? It's like you're seeing me differently now."
            scene 124_s43 with dissolve
            r "I do! I finally realized who my husband is. Not just the man who saved me, not just the stranger who wandered into my mother's court, but... {i}you{/i}."
            r "I-I love you! I love you so much!"
            scene 124_s42 with dissolve
            mc "*chuckles* I love you too."
            scene 124_s43 with dissolve
            if reb_pregnancy_fail or reb_sick:
                r "Take me~! NOW—"
                jump reb_pregfail
            else:
                r "Take me~! NOW!"
                scene 124_s42 with dissolve
                call screen scene124_choice03 with dissolve
        else:
            scene 124_s40 with dissolve
            r "W-Why?! Why do you not want to be with me?!"
            scene 124_s41 with dissolve
            mc "Huh? Didn't we already go through this? I thought we'd made peace with it."
            scene 124_s40 with dissolve
            r "I know... I'm so pitiful. So pathetic. B-But can you blame me? It's only you that I ever had."
            r "And now you don't even want that girl."
            scene 124_s41 with dissolve
            mc "I want her. I'll always want her. But wanting and being together... they're not the same thing. My heart is somewhere else, Becky."
            scene 124_s40 with dissolve
            r "Nghnn... fine!"
            r "Screw you for stealing my heart and not giving it back. Screw you for being so incredible that I can't even be angry at you properly..."
            scene 124_s41 with dissolve
            mc "*chuckles* I'm sorry."
            scene 124_s44 with Dissolve(1.4)
            r "Just... give me time. And don't expect me to stop loving you, because I don't think I can."
            mc "Of course. Take some rest, princess. I'll go see if I can find the baths."
            if reb_pregnancy_fail or reb_sick:
                jump reb_pregfail
            else:
                jump scene126
    else:
        if not mc_reb_breakup_final:
            r "Maybe we need to rest, [mc]. I'm sorry for teasing you on earlier, but there's too much to think about right now."
            scene 124_s41 with dissolve
            mc "Are you sure? I've missed you a lot."
            scene 124_s40 with dissolve
            if quest_witch_amelia_alive_free and mc_agree_help_amelia_milking:
                r "I did too. But I just can't now... Not with so many deaths on your hands. Not with Amelia the Witch as our ally. Not with so few people standing beside us. I need time to absorb it all."
            else:
                r "I did too. But I just can't now... Not with so many deaths on your hands. Not with so few people standing beside us. I need time to absorb it all."
            scene 124_s41 with dissolve
            mc "If you say so."
            scene 124_s40 with dissolve
            r "I'm going to bed."
            r "Thank you, [mc]. Really. I'd still be rotting in that cellar if you hadn't been there. But... *sigh* just leave me alone for a while."
            scene 124_s41 with dissolve
            scene 124_s44 with Dissolve(1.4)
            mc "Alright. I'll go see if I can find the baths."
            r "Mhm."
            if reb_pregnancy_fail or reb_sick:
                jump reb_pregfail
            else:
                jump scene126
        else:
            r "This is too much for me..."
            r "You've been out here fighting a war I didn't even know was happening, and the results are... terrible."
            scene 124_s41 with dissolve
            mc "We'll build from here. We'll find more allies. We'll make this work."
            scene 124_s40 with dissolve
            r "I know... still, I need to rest badly. Everything you've told me tonight—it's like trying to drink from a waterfall."
            scene 124_s41 with dissolve
            mc "Fine. Get some rest, princess."
            scene 124_s40 with dissolve
            r "Thank you, [mc]. Really. I'd still be rotting in that cellar if you hadn't been there. But... *sigh* just leave me alone for a while."
            scene 124_s41 with dissolve
            scene 124_s44 with Dissolve(1.4)
            mc "Alright. I'll go see if I can find the baths."
            r "Mhm."
            if reb_pregnancy_fail or reb_sick:
                jump reb_pregfail
            else:
                jump scene126

label reb_pregfail:
    stop music
    scene 124_s95 with vpunch
    r "*cough* *cough* Ahg!"
    mc "Rebecca?!"
    play music "sad/case_file.mp3" fadein 3.0 loop
    scene 124_s97 with Dissolve(1.0)
    r "S-Sorry... I don't know what came over me. *cough* It's nothing. Just... something in my throat."
    scene 124_s96 with dissolve
    mc "Shit... we should have stayed in the hospice for longer. You're clearly still sick from the journey here. You pushed yourself too hard, too fast."
    scene 124_s97 with dissolve
    r "N-No. I'm fine. I swear. I've been through worse. I can survive a little cough."
    scene 124_s96 with dissolve
    if not mc_reb_breakup_final:
        mc "We can't do anything with you like this, Becky. You're in no condition for—"
        scene 124_s97 with dissolve
        r "I told you, I'm fine! I don't need to be coddled like some porcelain doll! I'm not going to break just because I coughed once!"
        scene 124_s96 with dissolve
    mc "You're not fine. Please. Just listen to me. For once, just... let me take care of you."
    scene 124_s98 with vpunch
    r "Blaargh!"
    perception "She suddenly pukes onto the floor. She doubles over, retching, her whole body shaking with the force of it."
    mc "Here, here. I've got you. You're fine. You're going to be fine."
    r "What— *gag* the hell is wrong with me? I've never... I've never been sick like this before. Not even in the cellar. What's happening to me?"
    mc "I... I don't know."
    scene 124_s99 with Dissolve(1.0)
    if reb_pregnancy_fail:
        mc "(Could it really be because of her miscarriage? I don't know how to bring this up. I have to tell her. But... not now. Not when she's like this. Fuck. Fuck. Fuck.)"
    else:
        mc "(Could it really be because of not having enough supplies on the way here? Dammit...)"
    scene 124_s100 with dissolve
    mc "Is someone out there?! Bring a healer, quick! Anyone! Now!"
    n_palace "On it, Master! Right away!"
    r "I'm sorry. I'm so sorry. This is... this is disgusting. You shouldn't have to see me like this."
    scene 124_s101 with Fade(1.0,1.0,1.0)
    zahira "Hello, sir. I'm healer Zahira. I need you to tell me what happened. When did the nausea start? How long has she been like this?"
    scene 124_s102 with Dissolve(1.0)
    mc "She's been a little fatigued since we arrived, but nothing like this. She just... collapsed, and started throwing up. I don't know what triggered it."
    scene 124_s103 with dissolve
    if reb_pregnancy_fail:
        zahira "Hm. This isn't a regular sickness, I'm afraid. Has she experienced anything... traumatic recently? Any physical or emotional shock?"
        scene 124_s102 with dissolve
        mc "I know. It's because of—"
        scene 124_s103 with dissolve
        zahira "A miscarriage?"
        scene 124_s102 with dissolve
        mc "..."
        r "What? What did you just say?"
        scene 124_s103 with dissolve
        zahira "A miscarriage. That's what this is, isn't it? The symptoms match perfectly."
        scene 124_s102 with dissolve
        scene 124_s104 with Dissolve(1.0)
        r "A... a miscarriage? I was... I was pregnant? I don't understand. I didn't know. I didn't know I was... How could I not know?"
        scene 124_s105 with dissolve
        mc "Becky... I'm sorry. I should have told you. The healer in the hospice told me while you were unconscious."
        mc "She said... she said the malnutrition. The weeks in the cellar. Your body couldn't support it. It wasn't your fault, it just... happened."
        scene 124_s104 with dissolve
        r "I was pregnant. I was carrying a child. And I didn't even know..."
        r "I didn't even get to... to feel it. To... to love it. A-And now it's gone. It's gone and I didn't even know it existed."
        empathy "She breaks down in raw, ugly sobs that shake her whole body."
        scene 124_s103 with Dissolve(1.0)
        zahira "I'm sorry. I didn't mean to be so blunt, but she needed to know."
        scene 124_s102 with dissolve
        mc "Alright. Thank you. Truly. I don't think I could have brought this up this on my own."
        mc "Is there anything else I can do for her?"
        scene 124_s103 with dissolve
        zahira "Keep her warm and hydrated. You can leave the rest to me."
        zahira "I'll administer her a potent healing potion, then check on her in the morning. Let her sleep till then."
        scene 124_s106 with Dissolve(1.0)
        r "*hic* Leave!"
        mc "Huh? Becky—"
        scene 124_s106 with vpunch
        r "*sob* Leave me ALONE! Both of you! NOW!"
        mc "..."
        zahira "It's fine, sir. This is normal. Let her grieve."
        mc "Alright. I'll... I'll leave you alone, Becky. But I'll be back soon."
        r "..."
    else:
        zahira "It's not a regular sickness. That much is clear. But it's nothing life-threatening. You can relax, sir. She's not dying."
        scene 124_s102 with dissolve
        mc "Then what is it? What's wrong with her?"
        scene 124_s103 with dissolve
        zahira "Exhaustion. Severe, accumulated exhaustion. Combined with dehydration and mild malnutrition."
        scene 124_s102 with dissolve
        scene 124_s107 with Dissolve(1.0)
        r "So I'm not... I'm not dying?"
        scene 124_s108 with dissolve
        zahira "You're just tired, princess. More tired than you've ever been in your life. And your body is forcing you to rest, whether you want to or not."
        mc "Is there anything I can do to help her?"
        zahira "Keep her warm and hydrated. You can leave the rest to me."
        scene 124_s107 with dissolve
        r "I... I understand. I'm sorry. I didn't mean to cause trouble."
        scene 124_s108 with dissolve
        scene 124_s103 with Dissolve(1.0)
        zahira "I'll administer her a potent healing potion, then check on her in the morning. Let her sleep till then."
        scene 124_s102 with dissolve
        mc "A-Alright..."
        scene 124_s103 with dissolve
        zahira "You should leave her to rest, sir."
        scene 124_s102 with dissolve
        mc "Yes. I understand."
        scene 124_s108 with dissolve
        mc "I'll be right back, Becky. Do as the healer says and get some sleep."
        r "Mhm..."
    jump scene126

label scene124_choice03_op1:
    scene 124_s45 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    sensation "You press you lips against her in a firece kiss. She metls slightly from the sudden affection after so long."
    scene 124_s46 with dissolve
    mc "Let's do it."
    scene 124_s47 with dissolve
    if not reb_pregnant and not reb_pregnancy_fail:
        r "Put a kid in me~"
        scene 124_s46 with dissolve
        mc "Oh~?"
        scene 124_s47 with dissolve
        r "I know this isn't the best time for it, but to hell with it. I need to carry your seed in case something were to happen to you."
        scene 124_s46 with dissolve
        mc "*chuckles* So you only want to be pregnant in case I die?"
        scene 124_s47 with dissolve
        r "Don't say it like that... idiot."
        scene 124_s46 with dissolve
    else:
        r "I want it rough~ No lovey dovey stuff like last time."
        scene 124_s46 with dissolve
        mc "Oh~?"
        scene 124_s47 with dissolve
        r "Yes, to hell with all those romance novels I kept reading. A girl needs a real man every now and then. Make me moan your name on top of my lungs~"
        scene 124_s46 with dissolve
        mc "As you wish. I'll make sure every maid in this entire palace hears."
    stop music fadeout 1.0
    jump scene124_sex

label scene124_choice03_op2:
    mc "Not now, Becky. Look at you, I feel like a breeze could knock you on your butt."
    scene 124_s40 with dissolve
    r "Ugh! Would you please stop acting like one of my maids?!"
    scene 124_s41 with dissolve
    mc "*chuckles* I'm serious. I feel like I could seriously hurt you if I make a wrong move."
    scene 124_s40 with dissolve
    r "...So, it's because you care about me?"
    scene 124_s41 with dissolve
    mc "Of course, why else would I refuse a chance to lay with my princess?"
    scene 124_s43 with dissolve
    r "*giggles* Fine, you slitherd your way out of this one."
    scene 124_s42 with dissolve
    mc "I'll go and try to find the baths. It's been a... while. Rest well, princess."
    scene 124_s43 with dissolve
    r "Mhm. Just don't think too much about me when you're in there. I hear warm water gets the blood flowing~"
    scene 124_s42 with dissolve
    mc "No, {i}you{/i} don't think too much about me."
    scene 124_s43 with dissolve
    r "You don't get to order me~ Expect this room to smell... funny, when you come back."
    scene 124_s42 with dissolve
    jump scene126

image s124_vsex1 = Movie(play="images/chapter5/scene124/s124_vsex1.webm", loop=True)
image s124_vsex2 = Movie(play="images/chapter5/scene124/s124_vsex2.webm", loop=True)

image s124_asex1 = Movie(play="images/chapter5/scene124/s124_asex1.webm", loop=True)
image s124_asex2 = Movie(play="images/chapter5/scene124/s124_asex2.webm", loop=True)

image s124_cun1 = Movie(play="images/chapter5/scene124/s124_cun1.webm", loop=True)
image s124_cun2 = Movie(play="images/chapter5/scene124/s124_cun2.webm", loop=True)

image s124_thigh = Movie(play="images/chapter5/scene124/s124_thigh.webm", loop=True)

default s124_reb_choice1_op1 = False

label scene124_sex:
    $ mc_sexed_reb_palace = True

    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_5_replay:
        $ persistent.chapter5_p7_5_replay = True

    scene 124_s50 with Fade(1.0,1.3,1.0)
    perception "She slips her dress off her shoulders and lets it fall to the floor. Her body is flushed and sheened with sweat. Between her thighs, her pussy is already dripping, a thin trail of arousal sliding down."
    scene 124_s51 with dissolve
    r "Take off your clothes and come over here~"
    scene 124_s50 with dissolve
    scene 124_s52 with Fade(0.5,0.5,0.5)
    mc "Look at you... it's leaking down your thighs."
    scene 124_s53 with dissolve
    r "I wonder why~? Maybe you can help with that?"
    scene 124_s52 with dissolve
    mc "Hmm... let me check. I need a thorough investigation."
    scene 124_s54 with Dissolve(1.0)
    r "Of course. Get down and take a look, dear husband~"
    scene 124_s55 with Dissolve(1.0)
    sensation "You lower yourself in front of her. The heat radiating from her pussy hits your face first—thick, and humid. She's soaked. More aroused than you've seen her."
    scene 124_s56 with dissolve
    mc "Whoa... it's steaming hot!"
    scene 124_s55 with dissolve
    r "Mhm~ Go on. Get closer."
    scene 124_s56 with dissolve
    mc "Alright—"
    play sound "se_sfx/sex/sex4.mp3" 
    scene 124_s57 with vpunch
    sensation "She lifts one leg and presses her foot against your shoulder, guiding you forward. Your mouth and nose press flush against her dripping folds. The scent is dizzying and your cock twitches hard."
    mc "Mfhmm!"
    show s124_cun1 with dissolve
    r "Yes... right there~! Make me leak all over your face!"
    mc "Mmmm... you're getting bold."
    r "Push your tongue inside and nuzzle my little bean with your nose~!"
    mc "*chuckles* As you wish."
    sensation "You drag your tongue through her slit, then push deep. Thick, slick nectar floods your mouth, slightly sweet, and endless. It coats your lips, chin, and tongue, dripping down your neck as you suck and thrust."
    r "Fahhnnn~! [mc]! [mc]! Keep doing that!"
    mc "Right here?"
    r "YESSSSS~! Right there... right there!"
    r "I always thought it was too dirty for someone like me to try..."
    mc "Try what?"
    r "Haaaahnnn~! Gods—you pushing your tongue so deep inside me... Don't you feel ashamed?"
    mc "Ashamed? No. I'd do anything to hear those lewd moans. It's like you forget you're supposed to be a haughty princess."
    r "Mhnnn~ D-Don't say that... I can't help- AHHNNNN~!"
    n_palace "Princess?! Should I call the guards?"
    r "No! Stay out! Hnnmm~!"
    call screen s124_reb_choice1 with dissolve

label s124_reb_choice1_op1:
    $ s124_reb_choice1_op1 = True
    scene 124_s58 with Dissolve(1.0)
    perception "You wipe your finger across her slick thighs and your own chin, then press the tip of your middle finger against her tight rear entrance."
    r "Haahh?! [mc]! Don't do that so suddenly!"
    mc "Want me to? It'll feel even better."
    r "Hmmm... F-Fine. Push it slowly."
    play sound "se_sfx/sex/sex3.mp3" 
    scene 124_s59 with Dissolve(1.0)
    sensation "You ease the finger in. Intense, squeezing heat clamps down around it. The thought of burying your cock in that same place makes you throb almost painfully."
    show s124_cun2 with Dissolve(1.0)
    r "Hnaaaahhn~! This is overwhelming... I... I feel too overstimulated!"
    mc "Mhmmm... *slurp* How is it, princess? Is your husband satisfying you well enough?"
    r "Y-You're kidding? I can't feel my legs anymore... Hannn~ My pussy and my butt... I didn't know such pleasures even existed~!"
    call screen s124_reb_choice1 with dissolve

label s124_reb_choice1_op2:
    $ s124_pronebone = True

    perception "Her leg clamps onto your back. Her entire body starts to shiver and quake, thighs clamping around your ears."
    mc "Getting close?"
    r "..."
    mc "Becky?"
    r "Aah... Hah... I..."
    mc "Woah, are you okay?"
    r "Fhmnnn.... I... I'm coming!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 124_s60 with vpunch
    r "HAHHHHHHHH!"
    perception "Her orgasm hits like a flood. A thick, hot rush of clear liquid erupts from her, slamming into your face and soaking your hair, neck, and shirt in an instant."
    play sound "se_sfx/masturbate_female/masturbate_cum4.mp3"
    scene 124_s61 with vpunch
    r "MMMMNNNNNNNNNNNN~!"
    perception "The squirting doesn't stop for several long seconds. When it finally slows, you're completely drenched. Even the floor beneath you is glistening."
    scene 124_s62 with Dissolve(1.5)
    mc "Holy shit..."
    scene 124_s63 with dissolve
    r "Hahh... ahh... I'm so... sorry..."
    scene 124_s62 with dissolve
    mc "*chuckles* You good?"
    scene 124_s63 with dissolve
    r "Yeah..."
    scene 124_s62 with dissolve
    mc "Fuck, my eyes sting a little."
    scene 124_s63 with dissolve
    r "Sorry... that was the best feeling I've ever had in my life..."
    scene 124_s62 with dissolve
    mc "You wanna pay me back for making you feel this good?"
    scene 124_s63 with dissolve
    r "Y-Yes, it wouldn't be fair otherwise... j-just give a minute or an hour..."
    scene 124_s62 with dissolve
    scene 124_s64 with Fade(1.0,1.0,1.0)
    perception "She lies face-down on the bed, her ass raised slightly. In the warm evening light her cheeks glisten with sweat. She's still gasping from earlier, chest rising and falling in uneven, shaky breaths."
    call screen s124_reb_choice2 with dissolve

default s124_reb_choice2_op1 = False
default s124_reb_choice2_op2 = False

label s124_reb_choice2_op2:
    $ s124_reb_choice2_op2 = True
    $ s124_anal = True
    play sound "se_sfx/sex/touch5.mp3" 
    scene 124_s65 with Dissolve(1.0)
    sensation "You climb over her and settle between her thighs. The head of your cock presses against her tight rear entrance. She shivers the moment she feels it."
    r "Mnn... [mc]? What are you doing?"
    mc "Taking charge."
    r "Wha—?"
    play sound "se_sfx/sex/touch6.mp3" 
    scene 124_s66 with Dissolve(1.0)
    sensation "You push forward. There's a moment of resistance, then the head slips inside with a soft pop. Intense, searing heat wraps around you as you sink deeper into her rectum."
    r "Ahhhn! [mc]! That's— that's not the right place!"
    mc "Is there a right place? I chose this hole on purpose."
    if mc_reb_anal and not mc_reb_vaginal:
        show s124_asex1 with Dissolve(1.0)
        r "Ahnnn~! You're going into my ass again... Why always my butt?"
        mc "Because it's irresistible. The way you moan when I push in... that shocked little expression on your face. It never gets old."
        r "Y-You pervert!"
        r "Do you realize I'm still a virgin because of this?"
        mc "*chuckles* I know. I'm saving the other hole for later~"
        r "Ahhnn~ Gods... I might actually get used to this... as long as my degenerate husband is happy."
    elif mc_reb_anal:
        show s124_asex1 with Dissolve(1.0)
        r "Ahhnn~! You're penetrating my ass again!"
        mc "Didn't you like it last time?"
        r "...I did. But it's so humiliating to admit it!"
        r "Look at you... smiling while you push into my... butt! Nahnn~!"
        mc "Let me in deeper. I want to reach your stomach."
        r "Mnnnhh~! I-It doesn't go any deeper than that!"
    else:
        r "[mc]! You're putting it in my butt! Can you not see where you're aiming?!"
        mc "I can see perfectly. Your little anus is puckering around me... I think it needs this."
        r "Mhnn! j-just be careful! I've never done this before... not even when I touched myself..."
        show s124_asex1 with Dissolve(1.0)
        sensation "You begin to move. With each thrust, her body gradually accepts you, her rectum molding perfectly to your shape."
        r "A-Alright! Just... Ah— Ahn! S-Slowly! Oh, Gods, slowly!"
        r "Ahnn~! Fuck! Dammit! What is this?!"
        mc "Does it hurt?"
        r "N-No! Don't stop! Keep going~! Gods!"
        r "I feel it in my stomach... It's making me feel so... full! Ahh!"
        mc "You're so fucking tight."
        r "Nghn!"
        perception "You thrust deep into her tight backdoor and a powerful shudder courses through her frame, from her clenched toes to her trembling shoulders."
        mc "Ahhn... How does it feel? Having a cock up your ass?"
        r "It's w-weird~! Your penis is somehow brushing the weak spot in my womb."
        mc "Good. That means you'll learn to love it even more."
        r "Hahhn~!"
    call screen s124_reb_choice3 with dissolve

label s124_pronebone:
    $ s124_thighjob = False

    $ s124_pronebone = True
    $ s124_reversecow = False
    if s124_anal:
        if not s124_reb_choice2_op2:
            jump s124_reb_choice2_op2
        else:
            jump s124_pronebone_anal
    else:
        if not s124_reb_choice2_op1:
            jump s124_reb_choice2_op1
        else:
            jump s124_pronebone_vaginal

default s124_pronebone_anal_1 = True
default s124_pronebone_anal_2 = False

default s124_pronebone_vaginal_1 = True
default s124_pronebone_vaginal_2 = False

default s124_reversecow_anal_1 = True
default s124_reversecow_anal_2 = False

default s124_reversecow_vaginal_1 = True
default s124_reversecow_vaginal_2 = False

label s124_pronebone_anal:
    $ s124_vaginal = False
    $ s124_anal = True

    if not s124_reb_choice2_op2:
        jump s124_reb_choice2_op2

    scene black with Dissolve(0.3)
    show s124_asex1 with dissolve
    if s124_pronebone_anal_1:
        $ s124_pronebone_anal_1 = False
        $ s124_pronebone_anal_2 = True
        perception "Her moans grow louder and more unrestrained with every thrust. It's as if your cock has unlocked something new in her. A deep, aching hunger to keep her ass filled."
        r "Nhmmm~... My butt feels so empty the second you pull out..."
        mc "Oh~? Is your brain finally accepting that this hole is made for pleasure too?"
        r "Hnnn... y-yes~... I can't believe you're turning me into this... this kind of slut... the kind who wants her butthole stuffed and stretched by a thick cock..."
        mc "This is only the beginning. Soon you'll be the one begging me to start with your ass every time."
        mc "You'll feel incomplete without me inside it."
        r "N-No... don't say that~... My husband is such a pervert... pushing me down and taking my ass like I belong to him..."
        call screen s124_reb_choice3 with dissolve
    elif s124_pronebone_anal_2:
        $ s124_pronebone_anal_2 = False
        sensation "You drive back into her in one smooth, deep stroke. Her body accepts you easily without resistance, only eager heat. Rebecca gasps sharply as the familiar fullness returns."
        mc "Fuck... you really want me in here, don't you?"
        r "Ahhhhnnn~! Don't pull it out~... I want it deep... deeeeper!"
        mc "*chuckles* I'm already as deep as I can go."
        r "Gahhn~! Fuuuuck~ [mc]! You're messing with my head... I... I'm not supposed to like this..."
        r "I'm a princess! Not some brothel whore with a loose butthole!"
        mc "Who said a princess can't develop an anal addiction?"
        r "Hhnnnn~... y-you're right... this is fine... feeling good from my butt is... completely normal~ Mnnn~"
        call screen s124_reb_choice3 with dissolve
    else:
        r "Hahh~... yes! [mc]... keep thrusting deep into my butthole~"
        r "I'll squeeze tighter... so you spill everything inside it~... Gods, this is so lewd... making me scream and moan like this..."
        r "A princess... getting ruined from behind... and I can't even bring myself to stop you..."
    call screen s124_reb_choice3 with dissolve

label s124_reb_choice2_op1:
    $ s124_vaginal = True
    $ s124_anal = False

    $ mc_reb_vaginal = True

    $ s124_reb_choice2_op1 = True
    play sound "se_sfx/blowjob/facial7.mp3" 
    scene 124_s67 with Dissolve(1.0)
    sensation "You settle over her, the weight of your body pressing her into the sheets. The head of your cock brushes against her entrance. She shivers hard at the contact, hips twitching."
    r "[mc]... I'm sorry. I should be the one pleasing you, yet you're doing everything..."
    mc "You don't have to apologize for that. Just feel this."
    r "Hahh?"
    play sound "se_sfx/sex/touch7.mp3" 
    scene 124_s68 with Dissolve(1.0)
    sensation "You push forward. Inch by careful inch you sink into the tight, wet heat of her. Her walls flutter and cling, trying to pull you deeper even as she tenses."
    r "Mhnnm~! S-Slowly..."
    show s124_vsex1 with Dissolve(1.0)
    if mc_reb_vaginal:
        r "It's been... a while since I've taken you. Be gentle with me."
        mc "Fuck... you're burning up around me."
        r "*giggles* Too much for you already~?"
        mc "Nonsense, I'm going to make you forget how to keep quiet."
        r "Is that a challenge, husband? Fine. I'll try not to moan. Do your wor—"
        r "HAHHNNNNN~!"
        sensation "You drive the rest of the way home in one smooth thrust. The tip kisses the soft entrance of her womb."
        mc "Hmm? What was that about staying quiet?"
        r "Mnnhh...! [mc]~ you're so deep... stirring me up inside... I can feel you against my womb..."
        r "I'm sorry I challenged you, please don't— Ahhnmm~! don't make me moan like this!"
        r "The maids... what if they hear?"
        mc "That ship sailed a long time ago, love. They already know who you belong to."
        r "Oh Gods... they'll think the princess of Irda is a shameless slut—"
        mc "*chuckles* Let them. If anyone says a word, tell me. I'll handle it."
        r "Mhnnn~ That's right, my husband is so dependable~"
    else:
        r "Hnnngg~ Ahh! Ahhh! Ahnnn~"
        mc "There. It's done. How does it feel to lose your virginity?"
        r "It... hurts a little. But it also feels... safe. Like I was meant to open for you. I'm glad it was you, [mc]."
        mc "You're incredible. So tight it's almost painful."
        r "Mfhnn...! I can't stop squeezing... my body won't listen..."
        sensation "Every stroke drags along her sensitive walls, every push seats you fully against her cervix. Her back arches to meet you, toes curling into the sheets."
        mc "Does it feel good?"
        r "Y-Yes...! Don't stop... keep going... Gods, please..."
        r "You're so deep... filling me completely... ahh..."
        mc "God... You're steaming hot in there!"
        mc "Hahhn... As your husband, I'll take care of that heat whenever it rises. Understand?"
        r "Y-yes... please... take care of me..."
        perception "You thrust deep into her warm pink pussy and a powerful shudder wracks her frame, from her clenched toes to her trembling shoulders."
        r "Ahhn! Please, please put out this fire in my womb~!"
        mc "Do you want me to go deeper?!"
        r "Yes, yes, yes! {i}Deeeepeer!{/i}"
        r "Mhnng~! I can't think straight anymore."
    call screen s124_reb_choice3 with dissolve

label s124_pronebone_vaginal:
    $ s124_vaginal = True
    $ s124_anal = False

    if not s124_reb_choice2_op1:
        jump s124_reb_choice2_op1

    scene black with Dissolve(0.3)
    show s124_vsex1 with dissolve
    if s124_pronebone_vaginal_1:
        $ s124_pronebone_vaginal_1 = False
        sensation "Her pussy grows wetter with every thrust, slick sounds filling the room. The sheets beneath her grow damp, the air thickens with the scent of her arousal."
        mc "Keep squeezing me like that!"
        r "Yes, husband~ I will..."
        mc "Good girl. Who does this pussy belong to?"
        r "You! My pink pussy belongs to [mc]!"
        r "My pussy, my ass, my breasts... everything is yours. Only yours."
        mc "And what do I do with what's mine?"
        r "You use it... you mess it up... you stir it until I can't think..."
        r "Please, [mc]... discipline your wife's greedy little pussy. It never gets enough of you..."
    else:
        mc "God... you're making it hard to keep a steady pace. Every time I pull back you clamp down like you don't want to let me go, Becky."
        r "Ahnnnm... I can't help it... [mc]... I can't believe I almost died without ever feeling this..."
    call screen s124_reb_choice3 with dissolve

default s124_reversecow_first = True
label s124_reversecow:
    $ s124_thighjob = False

    $ s124_reversecow = True
    $ s124_pronebone = False

    if s124_reversecow_first:
        $ s124_reversecow_first = False
        mc "Climb on top of me, I want to try another position."
        r "I can barely move... b-but alright. Anything for you, my husband."
        mc "Don't worry. I'll do most of the work. Just sit on my cock and squeeze."
    
    if s124_anal:
        jump s124_reversecow_anal
    else:
        jump s124_reversecow_vaginal

label s124_reversecow_anal:
    $ s124_vaginal = False
    $ s124_anal = True

    if not s124_reb_choice2_op2:
        $ s124_reversecow = False
        $ s124_pronebone = True
        jump s124_reb_choice2_op2

    if s124_reversecow_anal_1:
        $ s124_reversecow_anal_1 = False
        $ s124_reversecow_anal_2 = True
        scene 124_s69 with Fade(1.0,0.5,1.0)
        play sound "se_sfx/sex/touch3.mp3" 
        sensation "She lowers herself carefully. The tight ring of her anus stretches around the head of your cock, then slowly yields. A sharp, broken moan spills out of her as she sinks down."
        show s124_asex2 with Dissolve(1.0)
        r "Goddssss~! At this rate, my pussy is going to start leaking again..."
        mc "You can feel it in your pussy too?"
        r "Y-Yes... You're so thick it presses against that weak spot inside me even from the other hole. I feel you in both places at once."
        mc "*chuckles* Intense, isn't it?"
        r "It is! I can't breathe properly... When you push into my colon it feels like something is lodged all the way up my throat."
    
    elif s124_reversecow_anal_2:
        $ s124_reversecow_anal_2 = False
        scene black with Dissolve(0.3)
        show s124_asex2 with dissolve
        r "You... you really want me walking around with a loose hole after this, don't you? Tell me the truth, [mc]."
        r "Do you want to see my ass gaping after you're- Gmnnn~! ...After you're done stirring up my insides?"
        mc "One of the reasons, yes. Watching that little ring try so hard to close again is extremely satisfying."
        mc "Like looking at a job well done."
        r "That's so dirty... I don't understand why you'd want to see something like that..."
        r "I can already feel it stretching open... You're making my butthole loose. W-what if the maids notice me walking funny?"
        mc "Wouldn't you feel a little proud that your husband is capable of that?"
        r "Ummm..."
        r "...I guess? Yes! *giggles* You're right. They'll be so jealous~"

    else:
        scene black with Dissolve(0.3)
        show s124_asex2 with dissolve
        perception "Sweat beads across her back and the nape of her neck even though she is barely moving. Pleasure has her body locked in a trembling, half-dazed state."
        r "[mc]... [mc]... my ass is finally accepting you properly, dear husband... This filthy little hole is learning to take you whenever you want..."

    call screen s124_reb_choice3 with dissolve

label s124_reversecow_vaginal:
    $ s124_vaginal = True
    $ s124_anal = False
    scene black with Dissolve(0.3)
    show s124_vsex2 with dissolve
    if s124_reversecow_vaginal_1:
        $ s124_reversecow_vaginal_1 = False
        $ s124_reversecow_vaginal_2 = True
        r "Fffnhmm... You're breeding me... Ahnn... My pussy is aching for every inch, [mc]."
        r "*giggles* Even when I was locked in that cellar I kept thinking about how you would take me..."
        r "I made up whole stories in my head about what you would say... how you would do it~"
        mc "*chuckles* What kind of stories?"
        r "Well, I would— Ahhnnm~! ...imagine myself as a peasant girl living on a quiet little farm, and one day the farm is suddenly under attack..."
        r "When all hope seems lost and the enemy is closing in, you suddenly ride in with your steed—"
        sensation "Her moans do something to you, penetrating your ears and settling in your heart. Your cock somehow gets slightly more erect. "
        r "Yeesssss~! Mhnnmmm~"
        mc "That's all?"
        r "Fhmmnn~ I-I can't think straight right now!"
    elif s124_reversecow_vaginal_2:
        $ s124_reversecow_vaginal_2 = False
        mc "You were telling me a story about being a peasant girl whose village got attacked. Care to finish it?"
        r "Oh, right! I calmed down a little, So..."
        r "You charge in on your horse and cut them all down with your sword. Then you come over to me. I'm on the ground, gasping and crying while my farm burns behind me..."
        r "You look down and say, 'Hey, pussycat, you alright?'"
        r "I answer, 'I-I'm fine... thank you for asking.' Then you just... get back on your horse and leave. Never knowing I fell in love with you right then and there. We never meet again afterwards."
        mc "That's your idea of a romantic story?! That was terrible! Why does it have to be so sad?!"
        r "Hhgnmmm~ But isn't it more realistic that way?"
        mc "He could have at least stayed long enough to make sure you were alright! What an asshole..."
    else:
        sensation "With every thrust her walls contract and flutter as if they have already decided you finished inside her. The rhythmic milking sensation makes holding back noticeably harder."
        mc "S-Stop that, Becky... I'm not done yet."
        r "Y-yes... I'm sorry... It's acting on its own... I can't control it..."
    call screen s124_reb_choice3 with dissolve

default s124_thighjob_1 = True

label s124_thighjob:
    $ s124_thighjob = True
    if s124_thighjob_1:
        $ s124_thighjob_1 = False
        mc "Let's take a break for a moment. I've been staring at those fat thighs and want to know how they feel."
        r "Fat?! Did you just call me fat!?"
        mc "W-Wait! I didn't mean it that way! It's actually a good thing that they're... fat."
        r "Hmm..."
        mc "I'm serious! The bigger the thighs the better they look."
        r "Alright, alright. Fine~ Anything for my depraved husband."
        scene black with Dissolve(0.3)
        show s124_thigh with Dissolve(1.0)
        perception "Your shaft slides between her closed thighs. They're slick with sweat and her own juices, the soft flesh yielding and clinging to you."
        r "Like this?"
        mc "Exactly. Fuck, this feels good already!"
        r "Ohh! You're thrusting between them... Is that really pleasurable?"
        mc "You have no idea. Your thighs are so soft... it feels like my cock is being smothered between two warm, squishy cushions."
        r "*giggles* Mmmnnn~ You make me feel good all the time, so I'll let you have this."
        r "Guess my butt and thighs being a little fat isn't so bad after all?"
        mc "That's right. These hips are to die for."
    else:
        scene black with Dissolve(0.3)
        show s124_thigh with dissolve
        sensation "You pick up the pace, sliding back and forth between the tight, wet press of her thighs. Every thrust makes a soft, wet sound as her skin grips and releases you."
        r "I can feel you throbbing against me... It's so hot..."
        mc "Keep them closed. Just like that."
        r "Mmm~ I'll keep them tight for you~"
        sensation "She presses her thighs together even tighter. The friction builds with every stroke, the head of your cock occasionally catching against the soft fold where her thighs meet her holes."
        r "I never thought something like this could feel... intimate. Guess I still have lots to learn, hm?"
        mc "I'll be there to teach you all of it."
    call screen s124_reb_choice3 with dissolve

label s124_reb_cum:
    if s124_thighjob:
        sensation "The wet glide between her thighs turns urgent. Your cock pulses harder with every pass, the pressure and heat pushing you right to the edge."
        mc "Becky... I'm close—"
        r "Already? From just my thighs...?"
        mc "Yes! Don't stop. Keep them together!"
        r "Alright, then... let it out. All over them if you want."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 124_s92 with vpunch
        sensation "A few more firm thrusts and the tension snaps. Thick ropes of cum spill between her thighs, coating the soft inner flesh in hot, sticky stripes. Some of it slides down toward her entrance, mixing with her own wetness."
        r "Ahh... it's so warm... there's so much..."
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 124_s93 with vpunch
        mc "Hahhh! Fuck!"
        r "Look at the mess you made on me... it's all over my butt and between my thighs."
        play sound "se_sfx/sex/touch4.mp3" 
        scene 124_s94 with Dissolve(1.0)
        mc "Hahh... ahn..."
        r "...Did that feel good releasing it like that?"
        mc "Hah... Yeah. I would do anything to try that again soon."
        r "*giggles* I'm glad I could give it to you after the way you ate me earlier~"
    else:
        if s124_vaginal:
            sensation "Her walls suddenly tighten around you in rhythmic pulses, the wet heat fluttering and squeezing as if trying to pull you deeper. Every movement drags a soft, broken sound from her throat."
            r "Ahhn~ [mc]~ I can feel it! You're throbbing so hard inside me...You're about to—"
            mc "Becky—!"
            r "Don't pull out! Please... I want it... all of it, spurt it inside me!"
            play sound "se_sfx/sex/sex_cum9.mp3" 
            if persistent.xray_mode:
                if s124_pronebone:
                    scene 124_s71_xray1 with vpunch
                else:
                    scene 124_s80_xray1 with vpunch
            else:
                if s124_pronebone:
                    scene 124_s71 with vpunch
                else:
                    scene 124_s80 with vpunch
            sensation "You spill inside her in heavy pulses, flooding her with thick, hot seed. Her body clenches tightly around you, milking every drop as a long, shaky moan escapes her lips."
            r "Hahhhnnn~!"
            play sound "se_sfx/sex/sex_cum10.mp3" 
            if persistent.xray_mode:
                if s124_pronebone:
                    scene 124_s72_xray2 with vpunch
                else:
                    scene 124_s81_xray2 with vpunch
            else:
                if s124_pronebone:
                    scene 124_s72 with vpunch
                else:
                    scene 124_s81 with vpunch
            perception "Her hips keep rolling weakly against yours even after the last spurt, as if her body refuses to let go just yet. A thin trail of cum already begins to leak around your shaft."
            if reb_pregnant:
                r "My womb is being flodded!"
            else:
                r "My womb is being flodded! I'm... I'm gonna be a mother!"
            play sound "se_sfx/sex/touch2.mp3" 
            if persistent.xray_mode:
                if s124_pronebone:
                    scene 124_s73_xray3 with Dissolve(1.0)
                else:
                    scene 124_s82_xray3 with Dissolve(1.0)
            else:
                if s124_pronebone:
                    scene 124_s73 with Dissolve(1.0)
                else:
                    scene 124_s82 with Dissolve(1.0)
            
            call pregnancy_check_reb from __call_pregnancy_check_reb 
            mc "Hahh.... Ahh..."
            mc "Shit... I noticed that I cum so much more if I'm with someone I love."
            r "Hnmm... I guess that's your own bodies way of telling you to impregnate someone?"
            mc "*chuckles* Maybe. An amount like this would surely do the job."
            if reb_pregnant:
                r "Too bad I'm already a upcoming mother~ But... don't stop finishing inside me. The feeling of your warm seed spilling into my womb is so intense, I came from it too~"
            else:
                r "Hopefully~ I need your child in me, [mc]. Sooner rather than later."

        else:
            sensation "Her tight ring clenches hard around the base of your cock, the heat and pressure almost overwhelming. Every small movement sends sharp sparks of pleasure through both of you."
            r "Ahh~ [mc]~ it's too much! My butt is... twitching..."
            mc "I'm close! Keep squeezing just like that!"
            r "That's disgusting, but... do it... spill your baby making juice inside my butthole!"
            play sound "se_sfx/sex/sex_cum9.mp3" 
            if s124_pronebone:
                scene 124_s74 with vpunch
            else:
                scene 124_s77 with vpunch
            sensation "You drive in deep one last time and break. Thick ropes of cum pour into her, the tight passage gripping and pulsing around you as if trying to keep every drop locked inside. A high, broken moan tears from her throat."
            r "Hnnnaaahhh~! It's so hot... I can feel it spreading deep in my stomach!"
            play sound "se_sfx/sex/sex_cum11.mp3" 
            if s124_pronebone:
                scene 124_s75 with vpunch
            else:
                scene 124_s78 with vpunch
            perception "Her body trembles under you, the soft flesh of her ass quivering with aftershocks. When you finally still, a slow trickle of cum begins to escape around your cock and slide down her thighs."
            r "Fuck... You really came inside my butt! Eeughh... it feels weird! Like I'm—"
            play sound "se_sfx/sex/touch2.mp3" 
            if s124_pronebone:
                scene 124_s76 with Dissolve(1.0)
            else:
                scene 124_s79 with Dissolve(1.0)
            mc "Don't finish that!"
            r "*laughs* Gods... just what are you doing to me... my poor hole wasn't made to take such a thick load and an even thicker penis~"
            mc "Hahh... ahh... Your hole is gaping wide now."
            r "D-Don't look at it!"
    
    scene 124_s83 with Fade(1.5,1.0,1.5)
    r "Hahh... that was intense. I'm still shaking from when you ate me out. There was some real dedication in that~"
    scene 124_s84 with dissolve
    mc "Of course. A healthy sex life is just as important as anything else."
    scene 124_s85 with dissolve
    r "You know what? You're right. Which means... I'll need you to come relieve me whenever I need it, got it?"
    scene 124_s86 with dissolve
    mc "*chuckles* Your wish is my command. I expect the same from you."
    scene 124_s85 with dissolve
    r "You don't even need to ask~ From now on, if you want me... just take me. No asking. Thrust it inside me whether I'm sleeping, cleaning, putting on makeup... Whenever~"
    scene 124_s86 with dissolve
    mc "Whoa... r-really?"
    scene 124_s85 with dissolve
    r "Yes~ If it means you'll make me feel as good as you did today, then... by all means. {i}My. Holes. Are. Yours. Husband~{/i}"
    scene 124_s86 with dissolve
    mc "S-Stop, you'll make me hard again..."
    scene 124_s85 with dissolve
    r "*laughs* You're adorable when you're flustered. I can't believe I never noticed before."
    r "Now stop thinking about it and go. I can see it in your eyes, you've been dying to explore this place since we arrived."
    scene 124_s86 with dissolve
    mc "You're not wrong. I desperately need to find the baths after how you drenched me."
    scene 124_s85 with dissolve
    r "*sniff* Mmmm~ You smell like me."
    scene 124_s87 with dissolve
    r "Just... be careful around the servants here. I've seen the way they watch the king's men. Eyes full of hunger."
    scene 124_s88 with dissolve
    mc "Really? I haven't noticed."
    scene 124_s87 with dissolve
    r "Mhm. Whenever mother and I visited, we'd see them whispering and hanging on every word from the king or the higher-ups. All the while, their breasts just hanging out... ugh..."
    r "If one of those scheming crows gets her dirty hands on you, I'll pull every last strand of hair from her head."
    scene 124_s88 with dissolve
    mc "Calm down... I doubt they'd spare me a glance. In their eyes I'm probably just your servant."
    scene 124_s85 with dissolve
    r "No. You're my husband. Make sure they know that."
    r "I don't care if you sleep with other women, [mc]... just don't stoop to their level."
    scene 124_s86 with dissolve
    mc "Now that I remember, didn't you wear that skimpy little dress back at the castle? The black one."
    scene 124_s87 with dissolve
    r "Ugh, don't remind me..."
    scene 124_s88 with dissolve
    mc "*chuckles* Why not?"
    scene 124_s87 with dissolve
    r "Because it's embarrassing. The thought of walking around the castle halls half-exposed like that still makes me shiver."
    scene 124_s88 with dissolve
    mc "So it was just a phase?"
    scene 124_s87 with dissolve
    r "I don't know. Maybe. I just feel less need to put myself on display now that I have a husband."
    scene 124_s88 with dissolve
    mc "I see. This body belongs only to me, after all."
    scene 124_s85 with dissolve
    r "It does~"
    r "Just remember that when you're off with the others. You're allowed to play... but you come back to me."
    scene 124_s83 with dissolve
    if s124_thighjob:
        r "Now that you covered my thighs and butt with your seed, please let me get my rest... *yawn*"
    elif s124_anal:
        r "Now that you filled up my butthole with your seed, please let me get my rest... *yawn*"
    else:
        r "Now that you filled my womb to the brim with your seed, please let me get my rest... *yawn*"
    scene 124_s84 with dissolve
    $ renpy.end_replay()
    call screen s124_reb_choice4 with dissolve

label s124_reb_choice4_op3:
    $ reb_love -= 10
    scene 124_s89 with Fade(1.0,1.0,1.0)
    mc "..."
    scene 124_s90 with Dissolve(0.7)
    r "Nghnn... [mc]? What in the Gods' names are you doing?"
    scene 124_s89 with Dissolve(0.7)
    mc "Cleaning myself up."
    scene 124_s90 with Dissolve(0.7)
    r "Wha—? Ugh, seriously? You said you were going to the baths... you bastard. Now I have to go too."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 124_s89 with Dissolve(0.7)
    mc "Your face made a better rag than anything else nearby."
    mc "Besides, you should head to the baths anyway. Don't be a stinky princess."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 124_s90 with Dissolve(0.7)
    r "I-I never stink... that's just your cock doing that..."
    scene 124_s89 with Dissolve(0.7)
    mc "*chuckles* Alright, I'm done. Thanks for letting me wipe my dick on your face, princess."
    scene 124_s90 with Dissolve(0.7)
    r "You can be really annoying sometimes, you know that?"
    scene 124_s89 with Dissolve(0.7)
    jump scene126

label s124_reb_choice4_op2:
    $ reb_love += 10
    scene 124_s91 with Fade(1.0,1.0,1.0)
    mc "*mwah* Sleep tight, Becky."
    r "Mmmm~ I love you so much, my savior husband~"
    jump scene126

default mc_left_reb_s124 = False
label s124_reb_choice4_op1:
    $ mc_left_reb_s124 = True
    mc "*chuckles* I'll leave you to rest, Becky. Seems like you really need it."
    r "Mmmmmm..."
    perception "She doesn't respond, only her eyes slowly shut down as she calms down."
    mc "I'll go straight to the baths, God knows I need it now."
    jump scene126

label scene125:
    n_palace "Here you are, queen of Irda. This room has been specifically arranged by his royal highness."
    n_palace "He assigned you several servants as well. They are at your disposal. Please call on them if you require anything at all."
    q "You may leave. I'll manage from here."
    n_palace "As you wish."
    play music "side_event6.mp3" fadein 3.0 loop
    scene 125_s1 with Dissolve(1.3)
    q "Hm. Interesting decorations. Gold on the bedframe, gold on the floor and ceiling."
    q "I see they're not afraid to splurge on useless things while their outer districts struggle with water shortages."
    scene 124_s3 with Dissolve(1.3)
    mc "Is it really a good thing to insult them when they're being hospitable?"
    mc "We just convinced the king not to execute us. Maybe we shouldn't criticize his interior design choices on the first night."
    scene 125_s2 with Dissolve(1.3)
    q "You can be critical without insulting, [mc]. It's a skill you'd do well to learn. Observation is not the same as condemnation."
    q "All this gold. Surely it would be more beneficial somewhere else..."
    q "But monarchs love their displays of wealth. I was guilty of it myself, in my younger years."
    scene 125_s3 with dissolve
    mc "They seem much better off than Irda. I don't even remember seeing gold... anything while I was in the castle."
    scene 125_s2 with dissolve
    q "Indeed. Nahraya is the biggest power in Illusian desert. The trade routes between them and the Zents are much less prone to attacks as the desert provides a natural barrier against bandits and raiders."
    q "And their navy controls the southern seas, allowing trade all over the world. Resources we could only dream of in Irda."
    q "Although, things are becoming sourer between the Nahrayans and the Zents. I'm still unsure of the reason."
    scene 125_s3 with dissolve
    mc "Hold on... Zents? Illusian? What or... who are these? You're throwing around names I've never heard before."
    scene 125_s2 with dissolve
    q "The Zents are a tribe of beastmen. They're the second largest power in the Illusian desert, which is the one we currently stand on."
    scene 125_s3 with dissolve
    mc "Ah. So both Irda and Nahraya are in the same continent?"
    scene 125_s2 with dissolve
    q "Yes. Just much further apart."
    scene 125_s3 with dissolve
    call screen scene124_choice000 with dissolve
    mc "Well, there's one thing Irda is better at. One thing Nahraya can never match."
    scene 125_s2 with dissolve
    q "Hm? Enlighten me, [mc]. What could that possibly be? As far as I'm concerned, they have us beaten at economy, military, and sheer size."
    scene 125_s3 with dissolve
    call screen scene125_choice01 with dissolve

label scene124_choice000_op2:
    mc "Let's sit. I'm a little bit tired."
    scene 125_s2 with dissolve
    q "Come. There are many things I want to know about."
    scene 125_s3 with dissolve
    jump scene125_2

label scene125_choice01_op1:
    $ queen_love += 10
    mc "For once, they don't have a beautiful, smart queen to lead them."
    scene 125_s4 with Dissolve(1.0)
    q "*chuckles* I see. There's no need for consolation, [mc]. I know my place in the grand scheme of things."
    q "I'm a deposed queen in exile, not a blushing maiden who needs her ego stroked."
    q "You should learn to accept how things are. It would benefit you in the future. Flattery is a tool, not a gift. Use it strategically, not freely."
    scene 125_s5 with Dissolve(1.0)
    mc "No. I'm serious. All this wealth and power doesn't even begin to compare."
    mc "Just this one thing—your leadership and your wisdom, not to mention your refusal to die, makes Irda better than Nahraya could ever be."
    q "..."
    scene 125_s6 with dissolve
    q "What exactly are you trying to get at, [mc]?"
    scene 125_s5 with dissolve
    mc "I'm just saying that I... missed you. I missed having you order me around. Irda without you is like a sinking ship."
    scene 125_s6 with dissolve
    q "*sigh* I won't lie to you, I missed it too."
    q "The feeling of actually being able to do something instead of hiding and waiting for news that might never come."
    scene 125_s5 with dissolve
    mc "We'll start making a change from here on out."
    scene 125_s6 with dissolve
    q "Indeed. Sit with me, [mc]. There are many things I want to know about."
    scene 125_s5 with dissolve
    jump scene125_2

label scene125_choice01_op2:
    scene 124_s10 with Dissolve(1.3)
    mc "The scenery looks better in Irda. Everywhere I look around here, it's just... yellow."
    mc "Even the sky looks beige half the time."
    q "The sceneray, huh? You know, I've spent so many years thinking about political machinations that I forget there's more to a kingdom than its strategic value."
    scene 125_s5 with Dissolve(1.3)
    mc "See? Irda has forests, mountains, and rivers."
    scene 125_s6 with dissolve
    q "It is beautiful indeed. I miss looking through the court room window into the vast snowy mountains nearby."
    q "On clear days, you could see the peaks glowing pink at sunset. The sight is unlike any other in the world."
    q "*chuckles* ...Fine. You got me there."
    scene 125_s5 with dissolve
    mc "Told you."
    scene 125_s6 with dissolve
    q "Sit with me, [mc]. There are many things I want to know about."
    scene 125_s5 with dissolve
    jump scene125_2

label scene125_choice01_op3:
    scene 124_s9 with Dissolve(1.3)
    mc "The food. Irda has better food. Hands down."
    q "The food? That's your argument? Sure, they tend to put too much spice on pretty much everything, but come, [mc]. Have you tried many dishes since you came here?"
    scene 125_s5 with Dissolve(1.3)
    if not mc_killed_reham:
        mc "Well... I have had some tea, and rice..."
    else:
        mc "No... nothing yet. Unless you count some cake."
    scene 125_s6 with dissolve
    q "Reserve your judgment then. That is nowhere near enough to make a decision yet."
    scene 125_s5 with dissolve
    mc "You're right. My bad."
    scene 125_s6 with dissolve
    q "Sit with me, [mc]. There are many things I want to know about."
    scene 125_s5 with dissolve
    jump scene125_2

label scene125_2:
    scene 125_s7 with Fade(1.0,0.5,1.0)
    q "Tell me, what's happening in my city?"
    q "I was cut off from the rest of the world. My information ends the day my ship left the harbor. Everything after that is... darkness."
    q "How different are things? Is there anything left of the Irda I knew?"
    scene 125_s8 with dissolve
    mc "I wasn't hiding in the city, so I don't know much. But I did visit every now and then, enough to get a picture."
    scene 125_s7 with dissolve
    q "Even if you hid in the city, I doubt Avery would have the manpower to look for you. While I was in charge, things were already grim."
    q "I didn't exactly leave her the keys to a kingdom in its prime. *chuckles* I imagine she's been struggling."
    scene 125_s8 with dissolve
    mc "There's something you need to know first."
    mc "Avery isn't exactly the 'queen' here. Not entirely. Reiner seems to be pulling her along. She's only queen on paper."
    scene 125_s9 with dissolve
    q "I see. She wasn't the brightest one in the room—my sister always let her emotions cloud her judgment."
    q "*sigh* Him taking advantage of her was something I considered. I'd... I'd hoped I was wrong."
    scene 125_s10 with dissolve
    mc "She seems... angry. And... sad? More on the angry side, though."
    mc "It feels like she's trying to prove something. To you. To herself."
    scene 125_s9 with dissolve
    q "Anger makes you vulnerable, sister."
    scene 125_s10 with dissolve
    mc "Reiner's soldiers fill the streets now. Rarely do I see Irdan guards walking around anymore. Those who are still there have been demoted, reassigned, or kicked out entirely."
    mc "She's also allowed slavery."
    scene 125_s7 with dissolve
    q "Slavery? Strange... It isn't like her to do that. When we were children, she cried when the servants disciplined a stable boy too harshly. She was soft. Too soft, our father said."
    q "Must be Reiner's influence. Although—they don't even allow slavery in Eurina as well."
    scene 125_s8 with dissolve
    mc "Maybe a last minute push to prop up the economy? She's desperate, after all."
    scene 125_s7 with dissolve
    q "How stupid. It would take multiple years, minimum, for merchants and traders to adapt their operations. Longer for the economy to feel any real benefit."
    q "In the meantime, she's alienated the population, destabilized the labor force, and handed Reiner exactly what he wants—a weakened Irda dependent on Eurina's support."
    scene 125_s13 with Dissolve(1.0)
    stop music fadeout 2.0
    q "What else is happening? Please tell me there's some good news buried in all this disaster."
    scene 125_s12 with dissolve
    play music "hope/mountain_mist.mp3" fadein 3.0 loop
    if mc_bought_brothel:
        scene 124_s26 with Dissolve(1.5)
        mc "*ahem* I'm proud to say that I'm the owner of a business right now! A legitimate establishment. Bought and paid for with hard-earned coin."
        q "*chuckles* Business? Is my sister so incompetent that she would allow a wanted fugitive to own a business in the city?"
        mc "Nobody knew I was a fugitive. Diana—she's the manager, a former worker there—she told me she'd use a fake name on the ownership papers."
        scene 124_s27 with Dissolve(1.0)
        mc "She'll manage the place in my place for now. She's terrifyingly sharp."
        q "I see. And what kind of business is this?"
        if mc_changed_to_tavern:
            mc "A tavern! [brothel_name]."
            q "A tavern? Smart move. Very smart. Some might overlook it, but a tavern is a major hub for information."
        else:
            mc "A brothel! [brothel_name]."
            q "A brothel? Smart move. Very smart. Some might overlook it, but a brothel is a major hub for information."
        if mc_hired_ruby and mc_hired_sarah:
            scene 124_s28 with Dissolve(1.0)
        elif mc_hired_ruby:
            scene 124_s48 with Dissolve(1.0)
        elif mc_hired_sarah:
            scene 124_s49 with Dissolve(1.0)
        else:
            scene 125_s12 with Dissolve(1.0)
        mc "You said it! Merchants visit. Guards, nobles. All of them with loose lips and too much to drink. And Diana's ears are large. Figuratively."
        mc "She's the reason I was able to learn so much about Avery and Reiner."
        scene 125_s13 with Dissolve(1.0)
        q "Good work, [mc]. I didn't know you had it in you. You've grown."
        q "What else did you do?"
        scene 125_s12 with dissolve

    scene 124_s35 with Dissolve(1.3)
    mc "You remember Ava, right? The royal examiner?"
    q "Of course. What about her?"
    
    if not ava_dead:
        mc "She's in on it too. She helped me out with my hand."
        q "*laughs* Don't mess with me, [mc]. I've known Ava for decades. She's unswayable, completely devoted to her role. She serves the law, not the ruler."
        scene 124_s36 with dissolve
        q "Regardless of whether it's me or Avery sitting on it, she follows the law to the letter. That's how elves are. Stubborn as stone. Ancient as the mountains."
        mc "Well... I got lucky. There was a situation involving her friend, Kathrine—a mercenary who'd been thrown in the dungeon."
        scene 125_s12 with Dissolve(1.0)
        mc "I managed to get her out. Ava was indebted to me afterwards."
        scene 125_s13 with dissolve
        q "Luck, huh? Didn't I tell you once that even luck can set you on the path to greatness? That fortune favors those who put themselves in its way?"
        scene 125_s12 with dissolve
        mc "You weren't wrong... Though I'm starting to wonder how much of it is luck and how much is something else."
        scene 125_s13 with dissolve
        q "Still, this is quite a bit of fortune piling up around you. Are you sure someone isn't pulling the strings for you behind the scenes?"
        scene 125_s12 with dissolve
        mc "Haha... I... I'm not sure. Maybe."
        scene 125_s11 with Dissolve(1.0)
        if mc_killed_alice:
            $ queen_love -= 30
            mc "There's also, Alice—a former lieutenant. She attacked out of nowhere, trying to capture me. I had to defend myself."
            q "Oh, Alice... She was one my favorites."
            mc "I promise I had no other choice."
            q "*sigh* I don't doubt you. Still..."
        else:
            mc "There's Alice, a former lieutenant. She attacked out of nowhere, trying to capture me. But I managed to convince her not to. For now at least."
            q "Good on you. Alice is very capable, I would hate to see anything happen to her."
    else:
        mc "She's... dead. I killed her. After she attacked me."
        q "What? Explain yourself, [mc]. This is treason of the highest order. Ava worked directly under me."
        scene 124_s36 with dissolve
        mc "I wanted her help with something—needed it, actually. But she attacked me. Called me a traitor. Said she'd bring me to Avery... I had no choice."
        q "I see... I've known Ava for decades. She's unswayable, completely devoted to her role. She serves the law, not the ruler."
        scene 125_s13 with dissolve
        q "Regardless of whether it's me or Avery sitting on it, she follows the law to the letter. That's how elves are. Stubborn as stone. Ancient as the mountains."
        q "I suppose I can chalk it up to self defense if she's the one that attacked first."
        scene 125_s12 with dissolve
        scene 125_s11 with dissolve
        if mc_killed_alice:
            mc "Right. No choice. The same happened with Alice—a former lieutenant. She attacked out of nowhere. I had to defend myself."
            q "*sigh* It seems many harbored loyalty to Avery, not just out of stubberness like Ava."
        else:
            mc "There's also, Alice—a former lieutenant. She attacked out of nowhere, trying to capture me. But I managed to convince her not to. For now at least."
            q "Good on you. Alice is very capable, I would hate to see anything happen to her."
        
    $ people = ["Alex"]

    if mc_helped_lena:
        $ people.append("Lena, I saved her daughter from slavery")
    elif mc_helped_jenny:
        $ people.append("Jenny, the daughter of a rich noble")

    if mc_agree_help_thulkin:
        $ people.append("Thulkin and his sister, Millicent")

    $ people_part = ". ".join(people) + "."

    if quest_witch_amelia_alive_free:
        $ amelia_part = " Even the witch, Amelia."
    else:
        $ amelia_part = ""
    
    $ final_message = "There are a few others who were in on it too. " + people_part + " " + amelia_part

    scene 125_s12 with Dissolve(1.2)
    mc "[final_message]"

    if quest_witch_amelia_alive_free:
        scene 125_s13 with dissolve
        q "I see... That Amelia. The witch who I specifically tasked you to capture. So she didn't run away after all."
        scene 125_s12 with dissolve
        mc "She's changed. I promise."
        scene 125_s13 with dissolve
        q "People change. Allies become enemies, and enemies become allies. I've seen stranger things."
        scene 125_s12 with dissolve

    if mc_convinced_nadia_stay:
        scene 124_s30 with Dissolve(1.0)
        mc "There's also Nadia, a woman who I helped with her business problem. She's thinking of expanding into a bigger shop."
        mc "Maybe one day she'll be the new 'king of the market'. If I can make it happen, I'll get another window into the city."

    if queen_favor >= 7:
        scene 125_s15 with Dissolve(1.0)
        q "That's good to hear. Truly. I just hope all those you mentioned are not putting their lives on the line solely for me."
        scene 125_s16 with dissolve
        mc "There's one last thing you need to know..."
        scene 125_s15 with dissolve
    else:
        scene 125_s13 with Dissolve(1.0)
        q "Is that all? The list of those who are still loyal to me?"
        scene 125_s12 with dissolve
        mc "Hmm? Yeah, that's all. Well, I'm sure there are more out there who I didn't meet."
        mc "...You seem disappointed. Like you were expecting more."
        scene 125_s13 with dissolve
        if quest_witch_amelia_alive_free:
            q "*sigh* I thought the that my years of rule would have earned more than a handful of loyalists and a reformed witch."
        else:
            q "*sigh* I thought the that my years of rule would have earned more than a handful of loyalists."
        q "You've been out here fighting a war I didn't even know was happening, and the results are..."
        scene 125_s12 with dissolve
        mc "We'll build from here. We'll find more allies. We'll make this work."
        mc "There's one last thing you need to know..."
        scene 125_s13 with dissolve
        
    q "What is it?"
    scene 125_s14 with Dissolve(1.0)
    mc "When I learned what happened to Maia, when I left the castle in a hurry, I got into quite a bit of trouble. With Abel. With Darius and his guards. And... with Gaius."
    q "Of course. That Gaius. Loyal to the bone—but only to whoever wears the crown."
    q "Is that why your hand is made of metal now? A goodbye kiss from him?"
    scene 125_s8 with Dissolve(1.0)
    mc "Yeah. He was too attached to me, I guess."
    mc "You're quite calm about this, by the way."
    scene 125_s7 with dissolve
    q "I noticed in the carriage on the way here. I just didn't think it was appropriate to bring it up yet."
    if not ava_dead:
        q "So, Ava helped with it? She's quite the capable sorceress, after all."
        scene 125_s8 with dissolve
        mc "Yes. Dean built it for me, and Ava cast the spell to bind it."
    else:
        q "So, that's what you meant when you said you needed help from Ava? Before she attacked you."
        scene 125_s8 with dissolve
        mc "Yes. Dean built it for me, and Ava cast the spell to bind it. She wasn't too happy doing it..."
    if queen_favor >= 7:
        $ queen_love += 10
        scene 125_s15 with Dissolve(1.0)
        if mc_bought_brothel:
            q "You managed to buy a buisness own. You recruited lots of people to your cause. And you lost your hand. All while I was hiding in some fishing village."
        else:
            q "You recruited lots of people to your cause. And you lost your hand. All while I was hiding in some fishing village."
        q "You've been busy."
        scene 125_s16 with dissolve
        mc "I wouldn't be able to do any of that if they weren't loyal to you in the first place, your majesty."
        mc "Your legacy. The hope that you'd return. They would risk everything for you. That's how much your people love you."
        q "..."
        scene 125_s15 with dissolve
        q "Huh... I see. Looks like not everything is lost."
        q "Thank you, [mc]. You have alighted the embers in my heart to continue fighting, harder than before."
        scene 125_s16 with dissolve
        mc "Of course."
        scene 125_s15 with dissolve
        q "But. I can't ignore your role in all of this. You kept going when anyone else would have stopped."
        q "You're incredible in your own right, [mc]. Don't diminish that."
        q "*chuckles* It feels good to have someone dependable to rely on."
        scene 125_s16 with dissolve
        call screen scene125_choice02 with dissolve

    else:
        scene 125_s9 with Dissolve(1.0)
        q "*sigh* This isn't good."
        q "I want the room to myself, [mc]. I need to rest badly. Please be kind and leave me to my thoughts."
        scene 125_s10 with dissolve
        mc "Uhh... sure. I'll go find the baths. Sorry if this isn't what you wanted to hear, but it's what's happening."
        jump scene126

label scene125_choice02_op1:
    scene 125_s18 with Dissolve(1.0)
    mc "Thank you, your majesty."
    scene 125_s17 with dissolve
    q "Get some rest. Tonight, we begin planning. It's going to be a long road."
    scene 125_s18 with dissolve
    mc "You should rest too. The journey here must have been awful."
    mc "Weeks at sea, then the desert crossing, all while worrying about the kingdom and Rebecca. Even a queen has limits."
    scene 125_s9 with dissolve
    q "*sigh* You're right. I feel like I could go into a deep slumber the moment I close my eyes."
    scene 125_s10 with dissolve
    mc "Then at least a few hours. You'll be no good to anyone if you collapse from exhaustion."
    scene 125_s7 with Dissolve(1.0)
    q "Look at you. Giving orders to your queen. You've gotten bold in my absence."
    scene 125_s8 with dissolve
    mc "*chuckles* I learned from the best. Goodbye, your majesty. I'll go see if I can find the baths first."
    jump scene126

label scene125_choice02_op3:
    $ mc_wants_reward_queen = True
    scene 125_s8 with dissolve
    mc "I'd like to be rewarded, your majesty."
    scene 125_s17 with Dissolve(1.0)
    q "Naturally. When we return to normal, you shall have whatever you desire."
    q "For now... I'm not exactly in the position to reward you with anything."
    scene 125_s18 with dissolve
    mc "I know. I'll look forward to it."
    mc "You should rest. The journey here must have been awful."
    mc "Weeks at sea, then the desert crossing, all while worrying about the kingdom and Rebecca. Even a queen has limits."
    scene 125_s9 with Dissolve(1.0)
    q "*sigh* You're right. I feel like I could go into a deep slumber the moment I close my eyes."
    scene 125_s8 with Dissolve(1.0)
    mc "Goodbye, your majesty. I'll go see if I can find the baths first."
    jump scene126

label scene125_choice02_op2:
    $ queen_love += 10
    $ mc_kiss_queen = True
    scene 125_s19 with dissolve
    q "[mc]? Where are you going?"
    scene 125_s20 with dissolve
    sensation "You close the distance between you. The world narrows to the space of a heartbeat. Before you can think, you lean in and press your lips to hers—warm, gentle, a question more than a demand."
    scene 125_s21 with dissolve
    q "[mc]?!"
    scene 125_s22 with dissolve
    mc "I-I... I couldn't resist, your majesty. Forgive me. I know I should have asked first..."
    mc "You looked so beautiful. Not just in appearance, but in character. The way you keep moving even after everything."
    mc "It did something to me. It's been doing something to me for a long time."
    scene 125_s24 with dissolve
    q "..."
    scene 125_s23 with dissolve
    q "I can say the same to you, [mc]. Everything you've done... it's not just loyalty. I know loyalty. This is something else, something I've been trying not to name."
    q "That was..."
    scene 125_s24 with dissolve
    mc "Should I have not done it? If I've overstepped, tell me. I'll leave. But I couldn't keep pretending I didn't—"
    scene 125_s23 with dissolve
    q "No. I didn't mean that."
    q "Well, it's just that the circumstances between us are different. I'm your queen. You're... you. I'm old enough to be your mother, [mc]."
    q "I'm at no age to be doing things like these. Running around kissing younger men like some lovestruck girl."
    scene 125_s24 with dissolve
    mc "That's not true! You still deserve love. You deserve it more than anyone I've ever met."
    q "..."
    if mc_queen_choice_sex:
        mc "I still remember that day we laid together. Fondly."
        scene 125_s23 with dissolve
        q "That was just a one-time thing, [mc]. You caught me at a vulnerable time. I wasn't thinking clearly. And this... this is another vulnerable time."
        scene 125_s24 with dissolve
        mc "Did you really not feel anything then?"
        scene 125_s23 with dissolve
        q "...I did."
        scene 125_s24 with dissolve
        mc "Then we can make it work."
    scene 125_s25 with dissolve
    q "*sigh* You're quite persistent, aren't you? Anyone else would have given up by now, accepted the polite rejection and moved on to someone more... appropriate."
    scene 125_s26 with dissolve
    mc "But I really do like you, your majesty. You're terrifying in the most beautiful way."
    mc "The way you're still fighting, even now, even after everything. How could I not fall for that?"
    scene 125_s25 with dissolve
    q "*laughs* Terrifying? That's your idea of a compliment?"
    scene 125_s26 with dissolve
    mc "For you? Absolutely."
    scene 125_s25 with dissolve
    q "I still don't know... I'll have to think about it, [mc]. Truly think. This isn't a decision I can make lightly."
    q "There are political and personal considerations. My... daughter."
    scene 125_s26 with dissolve
    mc "Of course. Take all the time you need. But I want you to know that I won't stop going after you. Not until you tell me, truly, that there's no hope."
    scene 125_s25 with dissolve
    q "Look at you. Giving orders to your queen. You've gotten bold in my absence."
    scene 125_s26 with dissolve
    mc "I learned from the best."
    scene 125_s25 with dissolve
    q "Now get off me before someone sees me like this."
    scene 125_s27 with dissolve
    mc "*chuckles* Goodbye, your majesty. I'll go see if I can find the baths."
    q "[mc]? That was... not unwelcome. The kiss. Just so you know."
    jump scene126

label scene126:
    stop music fadeout 3.0
    if mc_sexed_reb_palace:
        scene 126_s1 with Fade(1.5,1.0,1.5)
        nimah "Hello, my Master. I'm Nimah. How may I be of service? A-A towel perhaps? Or maybe some water? I can fetch anything you require."
        play music "side_event2.mp3" fadein 1.0 loop
        scene 126_s5 with Dissolve(1.0)
        mc "What's wrong? You're stuttering. You're reminding me of someone."
        scene 126_s4 with dissolve
        nimah "Forigve me. I'm one of the personal servants that were assigned to the princess."
        nimah "My role is to stand here and wait for anything you request of me. Day or night. Whatever you need."
        scene 126_s5 with dissolve
        mc "Oh... so you heard?"
        scene 126_s4 with dissolve
        nimah "Yes."
        scene 126_s5 with dissolve
        mc "Everything?"
        scene 126_s4 with dissolve
        nimah "Everything. I sincerely apologize, it wasn't my intention to eavesdrop."
        nimah "The walls are thick, but the doors are less so, and the princess was rather... vocal... and I couldn't exactly leave my post—"
        scene 126_s5 with dissolve
        mc "I get it. No need to apologize. You were doing your job."
        scene 126_s3 with dissolve
        nimah "Thank you, Master. I was so worried you'd be angry."
    
    elif reb_sick or reb_pregnancy_fail:
        scene 126_s1 with Fade(1.5,1.0,1.5)
        nimah "Hello, my Master. I'm Nimah. How may I be of service? Is there anything I could do for the princess?"
        play music "side_event2.mp3" fadein 1.0 loop
        scene 126_s5 with Dissolve(1.0)
        mc "She's resting now, so don't bother her."
        scene 126_s4 with dissolve
        nimah "I understand. I apologize that this happened, Master. And I wish the princess a swift recovery."
        scene 126_s5 with dissolve
        mc "Thank you... By the way, who are you?"
        scene 126_s3 with dissolve
        nimah "I'm one of the personal servants that were assigned to the princess."
        nimah "My role is to stand here and wait for anything you request of me. Day or night. Whatever you need."

    else:
        scene 126_s1 with Fade(1.5,1.0,1.5)
        nimah "Ah, Master. I'm Nimah. How may I be of service?"
        play music "side_event2.mp3" fadein 1.0 loop
        scene 126_s2 with Dissolve(1.0)
        mc "Hm? Who are you? I didn't notice you when we came in."
        scene 126_s3 with dissolve
        nimah "I'm one of the personal servants that were assigned to the princess."
        nimah "My role is to stand here and wait for anything you request of me. Day or night. Whatever you need."
    scene 126_s2 with dissolve
    mc "Interesting... outfit."
    scene 126_s3 with dissolve
    nimah "Thank you, Master. It's silk, adorned with gold thread. We wear it to look presentable for his royal highness's special guests."
    nimah "The royal palace takes great pride in its many servants. We are meant to be a reflection of the king's hospitality, and more importantly, his appreciation for beauty."
    scene 126_s2 with dissolve
    mc "I see. That's... that's quite a reflection."
    scene 126_s3 with dissolve
    nimah "His royal highness believes that every aspect of the palace should be pleasing to the eye. That extends to the servants too."
    nimah "It's all part of the experience. Part of what makes Nahraya the greatest kingdom in the Illusian desert."
    scene 126_s2 with dissolve
    mc "I'm still getting used to the experience. It's very different from Irda. We didn't have... this."
    scene 126_s3 with dissolve
    nimah "So I've heard. The servants from the western kingdom wear wool and linen, I'm told. Very modest and practical."
    nimah "But Master is in Nahraya now. Master should enjoy the differences. The beauty. The... hospitality."
    scene 126_s2 with dissolve
    call screen scene126_choice01 with dissolve

label scene126_choice01_op1:
    mc "I do need something."
    scene 126_s3 with dissolve
    nimah "Of course. What would you like, Master?"
    scene 126_s2 with dissolve
    mc "Before I ask... what exactly am I allowed to request of you?"
    scene 126_s3 with dissolve
    nimah "Anything within my ability to provide. That is the extent of my duties."
    nimah "There are no limits or rules that apply to guests of his honor. If it is within my power, it is yours."
    scene 126_s2 with dissolve
    mc "..."
    call screen scene126_choice02 with dissolve

label scene126_choice02_op1:
    $ mc_touched_nimah = True
    mc "I want to touch your breasts."
    if mc_sexed_reb_palace:
        mc "(I'm already doing what Rebecca told me not to... She literally just said to keep it in my pants around the palace servants.)"
    scene 126_s3 with dissolve
    nimah "As you wish, Master. Go ahead."
    scene 126_s2 with dissolve
    empathy "She answers without hesitation or change in tone, as if you had simply asked for a glass of water."
    scene 126_s8 with Dissolve(1.0)
    mc "Alright..."
    call screen scene126_boobs with dissolve

default scene126_boobs_first = True
default scene126_nips_first = True

label scene126_boobs:
    if scene126_boobs_first:
        $ scene126_boobs_first = False
        scene 126_s6 with Dissolve(1.0)
        sensation "You step closer and rest both hands on the soft swell of her breasts, feeling their weight."
        scene 126_s11 with dissolve
        nimah "Are they to your satisfaction, Master?"
        scene 126_s6 with dissolve
        mc "Yeah... they're soft."
        scene 126_s12 with dissolve
        nimah "I'm glad. The palace diet is designed to maintain optimal physical condition for all servants. It aids in duties such as these."
        nimah "If you require me to adjust my posture for better access, you need only say so."
        scene 126_s7 with dissolve
        mc "No... this is fine."
        scene 126_s12 with dissolve
        nimah "Very well. Take your time. I'm not going anywhere."
        scene 126_s7 with dissolve
    else:
        scene 126_s6 with Dissolve(1.0)
        sensation "You give a slow, testing squeeze. The flesh compresses beneath your fingers, then springs back the moment you ease the pressure."
        scene 126_s11 with dissolve
        nimah "You're being rather gentle."
        scene 126_s7 with dissolve
        mc "Should I be rougher?"
        scene 126_s12 with dissolve
        nimah "Only if it would please you more. I'm here for your convenience, not my own preference."
        scene 126_s7 with dissolve
    scene 126_s8 with Dissolve(1.0)
    call screen scene126_boobs with dissolve
    
label scene126_nips:
    if scene126_nips_first:
        $ scene126_nips_first = False
        scene 126_s10 with Dissolve(1.0)
        sensation "Your thumbs find the peaks of her nipples. You circle them slowly. A subtle breath leaves her—nothing more. Her heartbeat stays even under your hands."
        mc "Does this feel like anything to you? Anything at all?"
        scene 126_s9 with dissolve
        nimah "It feels like you're touching me, Master. Would you like me to moan?"
        scene 126_s10 with dissolve
        mc "Uhh..."
    else:
        scene 126_s10 with Dissolve(1.0)
        nimah "..."
        mc "(Why am I getting creeped out? This should be... I should be enjoying this. But she's so... blank. Like I'm touching a piece of furniture that talks.)"
    scene 126_s8 with Dissolve(1.0)
    call screen scene126_boobs with dissolve

label scene126_boobs2:
    scene 126_s2 with Dissolve(1.0)
    mc "(This woman... she's completely unfazed. It's kind of creepy if I'm being honest.)"
    mc "(Hmm... Maybe I can break her composure somehow? What would actually get a reaction out of her? I should be careful not to overstep, though.)"
    scene 126_s4 with dissolve
    nimah "You've gone quiet, Master. Is something the matter? Have I done something to displease you?"
    scene 126_s5 with dissolve
    call screen scene126_choice03 with dissolve

label scene126_choice03_op1:
    $ mc_slap_nimah = True
    play sound "sound_effects/slap03.mp3"
    scene 126_s13 with vpunch
    perception "You pull one hand back and bring it down in a slow, open-palmed slap across the soft flesh of her breast."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    nimah "Mhmm."
    perception "For the first time her composure cracks. She flinches hard, a small, genuine sound of shock escaping before she can stop it."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 126_s15 with dissolve
    empathy "When she looks at you again, the faint, pleasant smile is gone. Her expression is colder."
    scene 126_s14 with dissolve
    nimah "...Was that to your satisfaction, Master?"
    nimah "If you desire to continue in that manner, I will endure it. That is part of my duty. However... I would prefer a warning next time."
    scene 126_s15 with dissolve
    if mc_sexed_reb_palace:
        mc "(Fuck this! These maids are way too creepy. I get what Rebecca was saying now...)"
    else:
        mc "(Fuck this! These maids are way too creepy.)"
    jump scene126_2

label scene126_choice03_op2:
    $ aylin_love += 10
    $ mc_kiss_nimah = True
    scene 126_s16 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss1.mp3" 
    perception "You lean in and press your lips to hers. She doesn't pull away or lean in. Her mouth remains soft and still against yours."
    scene 126_s18 with Dissolve(1.0)
    nimah "..."
    mc "..."
    scene 126_s17 with dissolve
    nimah "Was that also part of what you required, Master?"
    scene 126_s18 with dissolve
    mc "You didn't... react. At all."
    scene 126_s17 with dissolve
    nimah "Should I have? You didn't instruct me to."
    nimah "If you would like me to show more affection, you only need to say so."
    scene 126_s18 with dissolve
    mc "You're acting like a robot!"
    scene 126_s17 with dissolve
    nimah "A... robot? Forgive me. I don't know that word, Master."
    scene 126_s18 with dissolve
    if mc_sexed_reb_palace:
        mc "(Fuck this! These maids are way too creepy. I get what Rebecca was saying now...)"
    else:
        mc "(Fuck this! These maids are way too creepy.)"
    jump scene126_2

label scene126_choice02_op2:
    $ reb_love += 10
    $ queen_love += 10
    $ mc_asked_wine_reb = True
    if mc_princess_success:
        mc "I want you to go and get the princess some wine. Something good."
    else:
        mc "I want you to go and get the Queen some wine. Something good."
    scene 126_s3 with dissolve
    nimah "As you desire, Master. What brand would she like?"
    nimah "We have a cellar of over three thousand bottles. Reds from the southern vineyards, whites from the coastal estates, and a particularly fine dessert wine from the Zentians."
    scene 126_s2 with dissolve
    mc "Brand? Well... just get the best you have here. Whatever the king drinks at his own table."
    scene 126_s3 with dissolve
    nimah "On it. I'll return shortly with a selection for her to choose from. Shall I also bring glasses? Some light refreshments to accompany it?"
    scene 126_s2 with dissolve
    mc "...Sure. Everything."
    scene 126_s3 with dissolve
    nimah "It will be done, Master."
    scene 126_s2 with dissolve
    jump scene126_2

label scene126_choice02_op3:
    mc "I'm so conflicted today. Sorry, I don't actually need anything."
    scene 126_s3 with dissolve
    nimah "It's fine, Master. Please don't apologize."
    nimah "I will be here when you do."
    scene 126_s2 with dissolve
    jump scene126_2

label scene126_choice01_op2:
    mc "Thank you, Nimah. But I don't need anything from you. At least not now."
    scene 126_s3 with dissolve
    nimah "As you desire. I will be here when you do."
    scene 126_s2 with dissolve
    jump scene126_2

label scene126_2:
    stop music fadeout 3.0
    scene 126_s19 with Dissolve(1.0)
    mc "(Alright. Time to explore on my own. How hard can it be? I've navigated a castle before. I won't get lost like I always did back in Irda.)"
    mc "(That was one time. Maybe two... Fine, several times. But this is different. I'm more focused, more alert. I'm—)"
    scene 126_s20 with wipeleft
    play music "nature.mp3" fadein 1.0 loop
    perception "You're lost. The palace is seemingly even bigger than Irda's castle, or maybe that's an illusion created by the endless identical corridors of gold and mosaic art."
    mc "(Dammit. How does a building this size even function? Do they have maps?)"
    mc "(Maybe I can find another cat-eared cook to guide me.)"
    scene 126_s21 with Dissolve(1.0)
    mc "(Hmm?)"
    mc "(Oh, shit. Did I seriously end up in the royal family's private wing?!)"
    scene 126_s22 with Dissolve(1.0)
    if mc_knelt_hod:
        prince "Huh. It's the stranger who came bearing news of our allies' treason."
    else:
        prince "Huh. It's the stranger who came bearing news of our allies' treason. The one who wouldn't kneel."
    scene 126_s23 with dissolve
    if mc_princess_success:
        if not mc_reb_breakup_final:
            mc "I'm no stranger. I'm the princess's husband."
        else:
            mc "I'm no stranger. I'm the princess's... ex-husband."
    else:
        mc "I'm no stranger. I'm the Queen's slav—I mean, steward. Her trusted steward."
    scene 126_s22 with dissolve
    prince "Please. I didn't mean to offend you. You are, by definition, a stranger. At least for now."
    prince "What are you doing here?"
    scene 126_s23 with dissolve
    mc "I'm not gonna sugarcoat it... I'm lost. I didn't mean to end up in the royal wing."
    scene 126_s22 with dissolve
    prince "*chuckles* This is no royal wing. This is our Goddess Eunice's church. We techniqually aren't even in the palace anymore."
    prince "And why {i}are{/i} you lost? There was no reason to leave your room. A guard would come for you and the princess when you're needed."
    prince "You simply had to wait."
    scene 126_s23 with dissolve
    mc "Can I not walk around at least? I was trying to find the baths while exploring a little. Stretch my legs. Is that a crime in Nahraya?"
    scene 126_s22 with dissolve
    prince "And you couldn't manage such a small feat? Finding the baths? There are signs. Servants or guards you could have asked."
    scene 126_s23 with dissolve
    mc "(This guy... is he trying to get a rise out of me on purpose? That smug little smile. That condescending tone.)"
    mc "*ahem* I'll be out of your hair. Sorry to intrude. I'll just... retrace my steps."
    scene 126_s22 with dissolve
    prince "Halt. I was on my way to the baths myself. Let me take you. Consider it a gesture of hospitality, or would you rather keep 'exploring'?"
    scene 126_s23 with dissolve
    mc "I'm coming. Thank you for the offer."
    scene 126_s22 with dissolve
    prince "Good. I'll—"
    scene 126_s24 with dissolve
    mc "Princess! I didn't notice you standing there. Forgive my rudeness, I should have greeted {i}you{/i} first."
    prince "Hah?"
    empathy "The prince suddenly gets flustered at your act of cutting him off. His carefully maintained composure cracks, just for a moment."
    mc "(Got you. Two can play that game.)"
    scene 126_s25 with Dissolve(1.0)
    princess "..."
    scene 126_s24 with Dissolve(1.0)
    mc "Umm... pleasure to meet you, princess."
    princess "..."
    scene 126_s26 with Dissolve(1.0)
    mc "Oh. Goodbye, then. I'll... leave you to it."
    scene 126_s27 with dissolve
    mc "Not much of a talker, is she? Your sister?"
    scene 126_s28 with dissolve
    prince "She's deaf. Has been since birth. She can read lips, but she prefers not to speak. Her voice is... she's self-conscious about it."
    scene 126_s27 with dissolve
    mc "Oh... I'm sorry. I didn't know. I wouldn't have—"
    scene 126_s28 with dissolve
    prince "You couldn't have known. But now you do. So if you want to communicate with her, face her directly and speak clearly. Don't mumble."
    prince "And don't treat her like she's stupid—she understands everything. She just responds differently."
    scene 126_s27 with dissolve
    mc "Got it."
    scene 126_s28 with dissolve
    prince "So. Like I was saying before I was so rudely—"
    scene 126_s27 with dissolve
    mc "The baths. Right. You were taking me there."
    scene 126_s29 with dissolve
    if mc_knelt_hod:
        prince "Ahaha... I see. You're doing this on purpose now. You're deliberately provoking me."
    else:
        prince "Ahaha... I see. You're doing this on purpose now. First you don't kneel for my father, and now you're deliberately provoking me."
    scene 126_s30 with dissolve
    mc "I'm not doing anything, I'm just agreeing with you. Lead the way, prince."
    scene 126_s29 with dissolve
    prince "Interesting. You're not nearly as dull as I expected. Most of my father's guests either grovel or bluster."
    prince "Fine. Follow me. Or don't. I don't care either way, but if you get lost again and end up in the harem, don't expect me to rescue you. My father's wives are not as forgiving as I am."
    scene 126_s30 with dissolve
    mc "Your father has a harem?"
    scene 126_s31 with Dissolve(1.0)
    perception "You try to whistle, impressed, but only a thin stream of air comes out."
    prince "..."
    stop music fadeout 1.0
    jump scene127

label scene127:
    scene 127_s1 with Fade(1.5,1.0,1.5)
    play music "bathhouse.mp3" fadein 2.0 loop
    perception "At the center of a massive chamber is an enormous bath. Steam rises from its surface in curls, giving the entire room a dreamlike, foggy feeling."
    mc "This is massive! You take baths here? This isn't a bath—this is a lake."
    prince "Yes. I'm surprised, do you not have baths like this back in Irda? I assumed all royal palaces had something similar."
    mc "Actually—"
    scene 127_s2 with dissolve
    prince "The towels and soaps are over there. Help yourself."
    mc "..."
    scene 127_s3 with Dissolve(1.0)
    perception "The prince begins undressing without any regards to your hulking manhood."
    scene 127_s4 with dissolve
    mc "W-Wait! What are you doing?!"
    scene 127_s5 with dissolve
    prince "*sigh* What is it now? Don't tell me you came here just to look. Do Irdans not bathe?"
    scene 127_s4 with dissolve
    mc "You're undressing... In front of me."
    scene 127_s5 with dissolve
    prince "And? We're both men."
    scene 127_s4 with dissolve
    mc "Right... right. Of course."
    mc "(Holy shit, did I seriously forget this was a guy for a moment? Those eyelashes... that feminine body.)"
    scene 127_s5 with dissolve
    prince "I'll start before you. Come when you're ready."
    scene 127_s4 with dissolve
    scene 127_s45 with Fade(1.0,1.0,1.0)
    sensation "The warm water is glorious as you sink deeper into the pool. It's the perfect temperature—hot enough to loosen every muscle, cool enough not to scald."
    scene 127_s6 with dissolve
    mc "Ahhhh... I didn't realize how much I missed this."
    scene 127_s7 with dissolve
    prince "You missed it? Ah, right. You were convicted of conspiracy, weren't you? Treason. The princess mentioned something about a cellar."
    prince "How did you manage evading the law for so long? I mean, I did hear of Irda's incompetence, but to this scale?"
    scene 127_s6 with dissolve
    mc "You're not wrong. They are incompetent, at least under Avery's rule. She gutted the guard force. Replaced veterans with foreign ones who don't know the city."
    mc "But I also hid... relatively well."
    scene 127_s45 with dissolve
    prince "Hm..."
    mc "..."
    scene 127_s8 with Dissolve(1.0)
    prince "So. What's next on your agenda? You've secured my father's support. What comes after?"
    scene 127_s9 with dissolve
    if mc_karma >= 5:
        mc "Agenda? Restoring the city to its rightful owners, for once. Dismantling Avery's regime. Freeing the people she's enslaved. Rebuilding what was broken."
        scene 127_s8 with dissolve
        prince "I see. Noble goals."
    else:
        mc "Agenda? Well, taking revenge on everyone who wronged me, for once. Avery. Reiner."
        mc "Every guard who looked the other way. Everyone who made my life hell."
        scene 127_s8 with dissolve
        prince "Revenge? That rarely goes well."
        scene 127_s9 with dissolve
        mc "Maybe. But I'm not planning to let go of the blade until the job's done."
        prince "..."
    scene 127_s10 with Dissolve(1.0)
    prince "Say... What happened to your arm? That's adamantite, isn't it? I recognize the sheen. My father has a ceremonial dagger made of it—cost more than a small warship."
    prince "How did someone like you get his hands on something so pricey? Adamantite isn't just rare—it's restricted. The mines are controlled by the dwarven clans."
    prince "They don't sell to outsiders. And the craftsmanship on those joints... that's not the work of a common blacksmith."
    scene 127_s9 with Dissolve(1.0)
    mc "I lost my hand fighting someone. He was the former queen's former protector. He didn't want me leaving the city."
    mc "Afterward, I got the help of a sorceress. She bound the new hand to me with a spell. It's as much a part of me now as the flesh one."
    scene 127_s8 with dissolve
    prince "Can I... touch it?"
    scene 127_s9 with dissolve
    mc "What?"
    scene 127_s8 with dissolve
    prince "Can I touch it? The metalwork. The joints. I've never seen adamantite prosthetics in person before."
    prince "I heard there's a general in the Zentian army who supposedly has full adamantite limbs, but no one's ever confirmed it."
    scene 127_s9 with dissolve
    mc "Well..."
    scene 127_s8 with dissolve
    prince "Tell me if you're uncomfortable. It's not like I'm eager to inspect it or anything..."
    scene 127_s9 with dissolve
    call screen scene127_choice01 with dissolve

label scene127_choice01_op1:
    $ mc_let_prince_hand = True
    mc "Sure. Come take a look."
    play sound "sound_effects/body/splash1.mp3"
    scene 127_s15 with vpunch
    prince "Yes! Thank you!"
    scene 127_s46 with Dissolve(1.0)
    perception "He swiftly stands up and comes over to you. His professional composed self is gone, it's clear that this subject interests him a lot."
    scene 127_s16 with dissolve
    prince "Incredible! The craftsmanship is... I've never seen anything like it. These runes... they're not just decorative, are they?"
    prince "They're channeling something. Mana, perhaps? A binding agent?"
    scene 127_s46 with dissolve
    mc "..."
    scene 127_s16 with dissolve
    prince "You said a friend did this? What kind of friends do you have?"
    scene 127_s17 with dissolve
    mc "He's a pretty well-known smith in Irda. The best in the city, probably. His daughter is exceptional as well."
    scene 127_s16 with dissolve
    prince "I have to admit... I was a little jealous when I first saw it. I'd love to have one at some point."
    scene 127_s17 with dissolve
    mc "You want a... prosthetic? What, are you hoping to lose one of your limbs someday?"
    scene 127_s16 with dissolve
    prince "Not a prosthetic. I want an adamantite blade!"
    prince "I've been obsessed with adamantite since I was old enough to read the metallurgy texts in the palace library."
    prince "It's the rarest metal in the known world. Stronger than steel, lighter than titanium, capable of holding enchantments that would shatter lesser materials."
    scene 127_s17 with dissolve
    mc "You want a blade? I... I actually have an adamantite sword too."
    scene 127_s18 with vpunch
    prince "You're messing with me!"
    scene 127_s19 with dissolve
    mc "I swear. It's in our carriage. Although... I don't know exactly where Alex placed it."
    scene 127_s18 with vpunch
    prince "Are you crazy?! Why the hell would you leave a blade like that out in the open?!"
    scene 127_s19 with dissolve
    mc "Whoa. Calm down. Alex is pretty good at hiding things. I doubt anyone will ever see the carriage, let alone the blade."
    scene 127_s18 with dissolve
    prince "Hmm... are you willing to sell that blade?"
    scene 127_s19 with dissolve
    mc "Sell it? No. Not really. I need it."
    scene 127_s18 with dissolve
    prince "Name your price. Three hundred gold pieces? Five hundred?"
    scene 127_s19 with dissolve
    mc "*gulp* Five hundred?! N-No. I can't. Seriously, I can't..."
    mc "(With that amount, I could clear my debt to Dean, and probably buy a castle on top of it...)"
    scene 127_s18 with dissolve
    prince "Tch. Fine. But you'll have to show it to me someday!"
    prince "The least you can do is let me hold the blade for being so hospitable with you."
    scene 127_s19 with dissolve
    mc "*chuckles* Sure."
    scene 127_s20 with Dissolve(1.3)
    prince "..."
    mc "(He's still inspecting it... too close...)"
    perception "The prince's body is curved—not in the way of a man who trains with swords and shields, but in a way that seems almost sculpted."
    scene 127_s22 with Dissolve(1.0)
    desire "A sense of confusion washes over you. You're unsure how to feel about him. It's better to set the record straight here and now."
    call screen scene127_choice02 with dissolve

label scene127_choice02_op1:
    $ mc_aroused_prince = True
    mc "(Why lie to myself? He arouses me, just like a woman would.)"
    mc "(S-Shit! I'm... I'm getting hard!)"
    scene 127_s18 with dissolve
    prince "You've gone quiet. What's the matter? Did I scare you with my adamantite obsession?"
    prince "I know I can be... intense about these things. My tutors used to say I had a one-track mind."
    scene 127_s23 with dissolve
    mc "N-No... that's not it. I'm just... thinking."
    scene 127_s22 with dissolve
    mc "(But what exactly arouses me in him? I need to figure this out.)"
    call screen scene127_choice03 with dissolve

label scene127_choice03_op1:
    $ mc_wants_prince_body = True
    scene 127_s24 with Dissolve(1.0)
    mc "(His feminine body. Definitely. That's what's doing it.)"
    mc "(My body is reacting to the feminine parts, not the masculine ones. I'm not gay. It's just because of that.)"
    jump scene127_prince

label scene127_choice03_op2:
    scene 127_s25 with Dissolve(1.0)
    mc "(That's right! I'm bisexual. I'm open to both men and women. Regardless of their appearance.)"
    mc "(Huh... I've never really said that to myself before. Not even in my own head, but it's true.)"
    jump scene127_prince

label scene127_prince:
    scene 127_s22 with Dissolve(1.0)
    mc "(I can't hide my erection... It's so obvious. I just hope he doesn't noti—)"
    scene 127_s26 with dissolve
    prince "[mc]!?"
    scene 127_s27 with dissolve
    mc "What?! What's wrong?!"
    scene 127_s26 with dissolve
    prince "What the hell is happening to you?!"
    scene 127_s27 with dissolve
    mc "What exactly are you referring to? I don't see anything wrong."
    scene 127_s26 with dissolve
    prince "Don't act stupid! What is that in the water?!"
    scene 127_s27 with dissolve
    mc "Well... you know. The water's hot. It gets the blood going and all that. Nothing to be concerned about."
    scene 127_s26 with dissolve
    prince "Stand up."
    scene 127_s27 with dissolve
    mc "Wha—?"
    scene 127_s26 with dissolve
    prince "I said stand up. I need to know if you're actually erect or if it's the water playing tricks. I won't stand for it if you are."
    scene 127_s27 with dissolve
    mc "I... Fine."
    play sound "sound_effects/body/splash2.mp3"
    scene 127_s28 with dissolve
    perception "You stand up. The water streams off your body. Your erection is now fully, unmistakably visible."
    mc "(Is this how I die? Getting executed for getting hard over the prince?)"
    scene 127_s30 with dissolve
    prince "*gasp* Y-You really are erect... Oh, Gods... I didn't... I thought maybe it was a shadow, or—"
    prince "Wh-Why?! Explain yourself, [mc]!"
    scene 127_s29 with dissolve
    call screen scene127_choice04 with dissolve

label scene127_choice04_op1:
    $ mc_told_truth_prince = True
    mc "It's because of you. Your body. The way you look. I've been trying not to notice, trying not to react, but... I couldn't help it."
    mc "I'm sorry. I know this is inappropriate. But you asked, and I'm not going to lie to you."
    scene 127_s30 with dissolve
    prince "Because of... me? You looked at me and you..."
    scene 127_s31 with dissolve
    perception "He glances down at his own body—the curves, the softness, he seems to know about it."
    scene 127_s30 with Dissolve(1.0)
    prince "*sigh* I'm not a woman, [mc]. I know I don't look like other men. I know my body is... different. I've heard the jokes and the whispers about me..."
    prince "...But I'm still a man."
    scene 127_s29 with dissolve
    mc "I know you are. That's... that's part of it, I think. I'm still figuring it out myself."
    scene 127_s30 with dissolve
    prince "A-Are you... homo?"
    scene 127_s29 with dissolve
    mc "Uhh..."
    scene 127_s32 with Dissolve(1.0)
    prince "*sigh* Forget it. Just... just sit back down. Please. You're making me uncomfortable."
    prince "And don't you dare tell anyone about this."
    mc "Deal."
    scene 127_s33 with Fade(1.0,1.0,1.0)
    prince "..."
    mc "..."
    scene 127_s40 with dissolve
    prince "It's umm... quite large. Never knew they can get that big."
    scene 127_s41 with dissolve
    mc "Thanks?"
    mc "Wanna compare length—?"
    scene 127_s40 with dissolve
    prince "Shut up. Not another word."
    scene 127_s33 with dissolve
    mc "..."
    jump scene127_choice04_op1_2

label scene127_choice04_op2:
    $ mc_backed_down_prince = True
    mc "It's nothing! Just the water. Promise."
    mc "Completely involuntary, nothing to do with you."
    scene 127_s30 with dissolve
    prince "Are you telling the truth?"
    scene 127_s29 with dissolve
    mc "I am. I swear."
    scene 127_s30 with dissolve
    prince "Thank the Gods..."
    scene 127_s29 with dissolve
    scene 127_s32 with Dissolve(1.0)
    prince "*sigh* You've made this bath extremely awkward..."
    prince "We will never speak of this again. Do you understand? This conversation never happened."
    prince "You are a stranger. I am a prince. And your... erection is a figment of both our imaginations."
    mc "Understood."
    scene 127_s33 with Fade(1.0,1.0,1.0)
    mc "(Well. That could have gone worse...)"
    prince "..."
    mc "..."
    jump scene127_2


label scene127_choice04_op1_2:
    scene 127_s40 with dissolve
    prince "You're not what I expected. When I first knew who you are, I pictured... I don't know. A desperate person. A broken man clinging to the scraps of a lost cause."
    prince "But you're not broken. You're just... strange. Strangely confident."
    scene 127_s41 with dissolve
    mc "I've been through too much to bother with lies anymore."
    scene 127_s33 with dissolve
    impulse "Look how vulnerable he is. One wrong word from you could break him. But... play it right, and you could turn him into your personal fucktoy."
    call screen scene127_choice05 with dissolve

label scene127_choice05_op1:
    scene 127_s36 with Dissolve(1.0)
    mc "You know, you talk a lot about how 'strange' I am. But you're not exactly a typical prince yourself."
    scene 127_s42 with dissolve
    prince "What's that supposed to mean?"
    scene 127_s36 with dissolve
    mc "I mean, look at you... Those hips... the curves. If I didn't know better, I'd think you were a princess playing dress-up."
    scene 127_s42 with dissolve
    prince "*scoff* I've heard that before, you're not original. 'The prince who looks like a princess'. 'The pretty boy who should have been born a girl'."
    prince "Even my father, he never says it, but I see the way he looks at me sometimes. Like I'm a disappointment. Like I was supposed to be something else."
    scene 127_s36 with dissolve
    mc "Do you think there's some... truth in what they say?"
    scene 127_s42 with dissolve
    prince "I... I don't know. Maybe. Sometimes I look in the mirror and I don't recognize myself."
    prince "Maybe it would have been better if I was born a girl. That way, at least, the outside would match the inside."
    scene 127_s36 with dissolve
    mc "You can still do that."
    scene 127_s44 with dissolve
    prince "*chuckles* Huh? Did you invent some miracle potion or spell that somehow transforms a man into a woman?"
    prince "Because if so, I'm about to become your first customer."
    scene 127_s43 with dissolve
    mc "Not like that. I mean that you can still be a girl, even if you're a boy."
    scene 127_s44 with dissolve
    prince "*sigh* Enough, [mc]. It's too late for that now. I'm the crown prince of Nahraya. I have duties and expectations. I can't just... change all of a sudden."
    scene 127_s43 with dissolve
    mc "It isn't too late. You have the body, the face, hell, even the voice."
    mc "If you wanted to walk out of this palace tomorrow in a skirt instead of what you usually wear, who could stop you?"
    mc "Sure, you're father might be angry. But he wouldn't love you any less, I think."
    scene 127_s42 with dissolve
    prince "If you're trying to comfort me, then you're doing a terrible job."
    scene 127_s33 with Dissolve(1.0)
    empathy "His patience is running thin. He's visibly getting more frustrated."
    call screen scene127_choice06 with dissolve

label scene127_choice06_op1:
    $ mc_angered_prince = True
    scene 127_s43 with Dissolve(1.0)
    mc "I'm not trying to comfort you. I'm trying to make you see what's right in front of your face. You're miserable as a—"
    play sound "sound_effects/body/splash1.mp3"
    scene 127_s37 with vpunch
    prince "Enough! You don't know me. You don't know my life. You've been in this palace for less than a day, and you think you can unravel twenty years of... of everything?!"
    prince "I thought you were different. I thought you might actually understand, but you're just like everyone else—pushing, pushing, pushing. Never listening."
    scene 127_s38 with dissolve
    mc "Wait, prince—"
    prince "Goodbye, [mc]. I'll send a servant to escort you back."
    mc "(Shit...)"
    jump scene127_2

label scene127_choice06_op2:
    $ prince_trans = True
    scene 127_s41 with dissolve
    mc "Alright. I'll stop. I was just... trying to help."
    scene 127_s40 with dissolve
    prince "Well, you're terrible at it."
    prince "*sigh* ...But you're not entirely wrong. About some of what you said."
    prince "I have thought about it. What it would be like. To be... different. To stop pretending. But every time I get close to the idea, I pull back."
    scene 127_s41 with dissolve
    mc "It doesn't have to happen all at once. You can just... try small things."
    scene 127_s40 with dissolve
    prince "Small things. Like what?"
    scene 127_s41 with dissolve
    mc "I don't know. Girly clothes instead of what you usually wear, maybe."
    mc "And I can... help you with that. Maybe start with a skirt?"
    scene 127_s42 with Dissolve(1.0)
    prince "Heh. You're ridiculous, but... I'll... umm... think about it."
    prince "And would you do if you saw me in a skirt tomorrow? Would you... *ahem* get erect again? What if everyone knew you were a homo?"
    scene 127_s36 with dissolve
    mc "Maybe. And trust me, I could care less what anyone thinks."
    scene 127_s42 with dissolve
    prince "Then... how about this, I'll wear skirt if you promise to show me your sword."
    scene 127_s36 with dissolve
    mc "A real sword, right? We're not talking metaphorically?"
    scene 127_s42 with dissolve
    prince "Idiot! I don't want to see your... thing again. I meant your adamantite sword."
    scene 127_s36 with dissolve
    mc "Right... Deal."
    scene 127_s47 with dissolve
    mc "(I didn't know I had it in me. I don't feel bad about this as much as I thought I would... Maybe he truly wanted this.)"
    jump scene127_2

label scene127_choice05_op2:
    $ prince_femboy = True
    scene 127_s43 with Dissolve(1.0)
    mc "You know... you said earlier that you don't look like other men."
    scene 127_s44 with dissolve
    prince "And? What about it?"
    scene 127_s43 with dissolve
    mc "I just wanted to say... I get it. Not the prince part. But the part about not fitting into the box people expect you to fit into."
    mc "I've spent my whole life not fitting. I was... different. Out of place. Never quite what people wanted me to be."
    scene 127_s36 with dissolve
    mc "So if I made you uncomfortable earlier... I'm sorry. I should have been more considerate."
    scene 127_s42 with dissolve
    prince "It wasn't... entirely your fault. I was the one who got too close."
    prince "You're the first person who's ever... reacted to me like that. Most people are too afraid of my father to even look at me the wrong way, let alone..."
    prince "You know."
    scene 127_s36 with dissolve
    mc "I know. And for what it's worth—I didn't react because I was mocking you. I reacted because you're... attractive. Genuinely."
    mc "I don't care if you're a boy. in fact... I'd prefer if you stayed that way. Just a boy with a girly side to him."
    scene 127_s42 with dissolve
    prince "*chuckles* Fool. Don't say that outloud or else the servants will hear, and that will be an entire new thing I have to deal with."
    prince "You're a very strange man, [mc]."
    scene 127_s36 with dissolve
    mc "Yeah."
    scene 127_s42 with dissolve
    prince "What would you do if you saw me in a skirt tomorrow? Would you get erect again? What if everyone knew you were a homo?"
    scene 127_s36 with dissolve
    mc "Maybe. And trust me, I could care less what anyone thinks."
    scene 127_s44 with dissolve
    prince "Then... how about this, I'll wear skirt if you promise to show me your sword."
    scene 127_s43 with dissolve
    mc "A real sword, right? You're not talking metaphorically?"
    scene 127_s42 with dissolve
    prince "Idiot! I don't want to see your... thing again. I meant your adamantite sword."
    scene 127_s36 with dissolve
    mc "Right... Deal."
    scene 127_s47 with dissolve
    mc "(Why do I feel bad about this? Like I'm taking advantage of his vulnaribitly... what if he actually wants to be a girl?)"
    jump scene127_2
    
label scene127_choice02_op2:
    mc "(Yeah. There's no feelings of arousal in me. My buddy down there can confirm it.)"
    scene 127_s18 with dissolve
    prince "Sorry for lingering too long. I'll let you continue your bath in peace now. Just don't forget to show me your blade!"
    scene 127_s19 with dissolve
    jump scene127_2

label scene127_choice01_op2:
    scene 127_s11 with Dissolve(1.0)
    mc "I'd rather you don't. It's not a museum piece. And I'm not entirely comfortable with people examining it like one."
    scene 127_s12 with dissolve
    prince "Fair enough. I understand. Some things are personal."
    prince "Still. It's an impressive piece of work. Whoever made it must be extraordinary. You're lucky to have someone like that in your corner."
    scene 127_s11 with dissolve
    mc "I know. I don't take it for granted."
    scene 127_s12 with dissolve
    prince "I have to admit... I was a little jealous when I first saw it. I'd love to have one at some point."
    scene 127_s11 with dissolve
    mc "You want a... prosthetic? What, are you hoping to lose one of you limbs oneday?"
    scene 127_s12 with dissolve
    prince "Not a prosthetic, I want an admantite blade!"
    scene 127_s11 with dissolve
    mc "A blade? I... I actually have an admantite sword too."
    scene 127_s13 with vpunch
    prince "You're messing with me!"
    scene 127_s14 with dissolve
    mc "I swear. It's in our carriage, although I don't know where Alex placed it."
    scene 127_s13 with vpunch
    prince "Are you crazy!? Why the hell would you leave a blade like that out in the open!?"
    scene 127_s14 with dissolve
    mc "Calm down. Alex is pretty good at hiding, so she's probably good at hiding things too. I doubt anyone will ever see the carriage, let alone the blade."
    scene 127_s13 with dissolve
    prince "A-Are you willing to sell it?"
    scene 127_s14 with dissolve
    mc "Sell it? No, not really. I need it."
    scene 127_s13 with dissolve
    prince "Name your price! Three hundred gold peices, five hundred?"
    scene 127_s14 with dissolve
    mc "*gulp* Five hundred?! N-No. I can't. Seriously, I can't..."
    if mc_debt:
        mc "(With that amount, I could clear my debt to Dean, and probably buy a castle on top of it...)"
    else:
        mc "(With that amount, I could probably buy a castle...)"
    scene 127_s13 with dissolve
    prince "Tch. Fine. But you'll have to show it to me someday!"
    scene 127_s14 with dissolve
    mc "*chuckles* If I have the time."
    jump scene127_2

label scene127_2:
    scene 127_s39 with Fade(1.3,1.0,1.3)
    if mc_angered_prince:
        mc "(I should go. I feel like I would turn into a prune if I stay any longer.)"
    else:
        mc "I have to go now, prince. I feel like I would turn into a prune if I stay any longer."
        if prince_trans or prince_femboy:
            prince "Go ahead. I'll stay a little longer. The night is still young, and I have... thinking to do."
        else:
            prince "Go ahead. I'll stay a little longer."

    jump scene128

label scene128:
    stop music fadeout 1.0
    scene 128_s1 with Fade(1.0,1.0,1.5)
    n_guard "Hold on. Are you [mc]? The one-armed man?"
    play music "ambiance/strange_forest.mov" fadein 1.0 loop
    scene 128_s3 with Dissolve(1.0)
    mc "That's me. Although I don't think 'one-armed man' is a good description. I have two arms. One of them is just... shinier than the other."
    scene 128_s2 with dissolve
    flint "*chuckles* Fair enough. I'm Flint. I'm the head of the guards here at the palace."
    if mc_knelt_hod:
        flint "A pleasure to meet you."
    else:
        flint "A pleasure to meet you. You're name was quite known after you refused to kneel."
    scene 128_s3 with dissolve
    mc "A pleasure to meet you too. I assume you want something from me?"
    scene 128_s2 with dissolve
    flint "Follow me. Ambassador Sanoud and Marshal Karim want to talk to you."
    scene 128_s3 with dissolve
    mc "What do they want? I just had a very long bath, and I was hoping to collapse into a bed for the first time in a while."
    scene 128_s2 with dissolve
    flint "They want to go over the plan that will ensue over the following weeks."
    if mc_princess_success:
        flint "We have quite a ways to go before you and the princess achieve your goals."
    else:
        flint "We have quite a ways to go before you and the Queen achieve your goals."
    scene 128_s3 with dissolve
    mc "The king is serious, isn't he? I didn't think he would accept to help us so quickly."
    mc "I thought he would offer us refuge—maybe a place to hide. But he's really going the extra mile. Even if it could be dangerous for his kingdom."
    scene 128_s2 with dissolve
    flint "Thank you. I'm sure his royal highness would appreciate your compliments."
    flint "But it isn't entirely for Irda's benefit. The king is a generous man, but he's also a pragmatic one."
    scene 128_s3 with dissolve
    mc "So it's mutual self-interest?"
    scene 128_s2 with dissolve
    flint "Indeed. Our enemies have already proven their willingless to assassinate a queen and imprison a princess. What's to stop them from turning their eyes south?"
    scene 128_s3 with dissolve
    mc "Yeah, I wouldn't put it past them. Reiner is a snake."
    scene 128_s2 with dissolve
    flint "Exactly. So helping Irda isn't just charity—it's self-defense. Cut off the snake's head before it reaches our borders."
    scene 128_s4 with Dissolve(1.0)
    flint "Here. Take this."
    mc "A map?"
    flint "Yes. Use it to navigate our city as well as the palace. *laughs* A few of my guards saw you wandering the halls with a dumbfounded look on your face."
    scene 128_s3 with Dissolve(1.0)
    mc "(He reminds me of Darius. I miss those times.)"
    scene 128_s2 with dissolve
    flint "Come on now. Marshal Karim doesn't like to be kept waiting. Reiner's daughter, Alexandria, is there too."
    scene 128_s3 with dissolve
    mc "Lead the way."
    stop music fadeout 1.0
    scene 128_s5 with Fade(1.5,1.0,1.5)
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    flint "Here we are. I wish you luck."
    mc "Thanks, Flint."
    scene 128_s6 with Dissolve(1.0)
    mc "Alex, is this where you were all this time?"
    scene 128_s7 with dissolve
    alex "I was in my room before a guard pulled me here an hour ago. *scoff* And these two have been arguing the whole time."
    alex "You look... damp. And you smell... good."
    scene 128_s6 with dissolve
    mc "You missed the best bath in your life. They have a pool the size of a small lake."
    scene 128_s7 with dissolve
    alex "That can wait. We have more important issues."
    scene 128_s6 with dissolve
    scene 128_s8 with Dissolve(1.0)
    stop music fadeout 1.0
    mc "Right, what are we working with?"
    play music "hope/desert_wind.mp3" fadein 1.0 loop
    amb "The only way to prevent this conflict from spilling across our borders is to unite the Illusian tribes."
    amb "It's the only path that doesn't end with Nahraya in flames."
    scene 128_s9 with dissolve
    karim "We already went through this, Sanoud. The tribes want nothing to do with us. Our relationships are already strained as is."
    karim "It's a miracle they let us move caravans through their territory. Let's not push them harder and risk losing even that."
    scene 128_s10 with dissolve
    amb "We only need the blessing of the Zents. If they agree to an alliance, the others will follow."
    amb "The Ol-ghouks respect strength. The Toukas respect pragmatism. If the Zents lead, they will fall in line."
    scene 128_s9 with dissolve
    karim "And how do you suppose we get this blessing? They're beastmen, Sanoud. They don't trust humans."
    scene 128_s10 with dissolve
    amb "The Zents value bravery above all. If we approach them with proper tribute, they'll at least listen."
    scene 128_s9 with vpunch
    karim "What tribute?! The new military buildup is costing a fortune. We can't just throw gold at the beastmen and hope they—"
    scene 128_s11 with Dissolve(1.0)
    curiosity "They go back and forth about the tribes. The Zents—a tribe of beastmen, fierce and honorable, the largest power in the Illusian desert after Nahraya itself."
    curiosity "The Ol-ghouks—peaceful orcs who'd abandoned their warlike ways generations ago. The Toukas—a smaller, isolationist tribe."
    desire "The conversation spirals into logistics and historical grievances and strategic positioning. Your attention is drifting further and further."
    scene 128_s12 with dissolve
    mc "Excuse me! Sorry to interrupt, but Flint told me you needed me."
    mc "You two are giving me a headache... No offense. It's just been a long day, and I think I heard the word 'tribe' about forty times."
    scene 128_s13 with dissolve
    amb "None taken. We've been at this for hours. But yes—we need to discuss your first mission. The king has agreed to support your cause, but support must be earned."
    scene 128_s12 with dissolve
    mc "Right. I know. Which tribe should I start with?"
    scene 128_s42 with dissolve
    karim "Tribe? You're not starting with any tribe, young man. We won't let you handle such delicate diplomatic matters."
    if mc_princess_success:
        karim "However, we learned from princess Rebecca that you're exceptional in solving... physical matters."
    else:
        karim "However, we learned from the Queen Hannah that you're exceptional in solving... physical matters."
    karim "She vouched for you personally when we brought this issue to her attention."
    scene 128_s12 with dissolve
    mc "What issue?"
    scene 128_s13 with dissolve
    amb "The market district has a major problem with a group of debt sharks. They call themselves 'the Ohm.'"
    amb "They act like a legitimate businessmen on the surface, but underneath, they're ruthless thugs."
    amb "Extortion. Kidnapping. Enslavement of debtors who can't pay. His royal highness has officially labeled them a group of bandits."
    scene 128_s12 with dissolve
    mc "Are you talking about the ones who call a 'Mr. Vic' their leader?"
    scene 128_s13 with dissolve
    amb "Yes. 'Mr. Vic' is the one we assume is running the whole operation. The change in leadership was somewhat recent."
    amb "I see you've already encountered them. A man who's only been in the city for two days."
    scene 128_s12 with dissolve
    if mc_princess_success:
        mc "I've seen what they do. Up close. If the princess vouched for me, then I can't fail. How do I start?"
    else:
        mc "I've seen what they do. Up close. If the Queen vouched for me, then I can't fail. How do I start?"
    scene 128_s42 with dissolve
    karim "Head to the market tomorrow morning, [mc]. Approach their compound openly. Try the diplomatic route first and convince them to change their ways."
    karim "If they refuse... you know what to do. You have permission from his royal highness."
    scene 128_s12 with dissolve
    mc "Hold on. You want me to take on an entire group of bandits by myself?"
    scene 128_s42 with dissolve
    karim "We will assign a group of guards to accompany you as well. They'll remain hidden, disguised as civilians. We don't want the Ohm to assume we're doing this by force."
    karim "If they think the king is sending soldiers to crush them, they'll scatter. And another group—even harsher, will rise to take their place within a month."
    scene 128_s12 with dissolve
    mc "I see. I won't let you down."
    scene 128_s13 with dissolve
    amb "Good. You may return to your room."
    scene 128_s14 with Dissolve(1.0)
    alex "I'll go with him."
    scene 128_s15 with dissolve
    amb "No, Alexandria. We have a seperate task for you."
    scene 128_s14 with dissolve
    alex "Are you sure? I can watch his back."
    scene 128_s15 with dissolve
    amb "You're needed somewhere else more important. You being Reiner's daughter is a valuable asset."

    if mc_sat_with_alex:
        scene 128_s16 with Dissolve(1.0)
        alex "...Fine. Good luck, [mc]."
        alex "Take care of yourself, you hear?"
        scene 128_s19 with Dissolve(1.0)
        alex "When you come back... I... I want to tell you something."
        mc "You can't tell me now?"
        alex "*giggles* No."
    else:
        scene 128_s17 with Dissolve(1.0)
        alex "...Fine. Good luck, [mc]."
        scene 128_s18 with dissolve
        mc "You too."
        mc "...Are you angry at me?"
        scene 128_s17 with dissolve
        alex "Hm? What gave that impression?"
        scene 128_s18 with dissolve
        mc "Your face. You look like you're about to attack me."
        scene 128_s17 with dissolve
        alex "I'm not."
        scene 128_s18 with dissolve
        mc "If you say so. I just wish you'd show different motions from time to time."
        scene 128_s17 with dissolve
        alex "Just go. And take care of yourself."
        scene 128_s18 with dissolve
    
    stop music fadeout 2.0
    scene 128_s20 with Fade(1.3,1.0,1.3)
    mc "(Could that Vic really be the same one from Irda? Abel mentioned something about him before we dragged his ass to his personal dungeon.)"
    if mc_princess_success:
        if reb_pregnancy_fail:
            mc "(*sigh* I'll think about it later. For now, I have to check on Becky.)"
            scene 128_s45 with Fade(0.5,0.5,0.5)
            play music "sad/maia3.mp3" fadein 1.0 loop
            mc "Becky? ...Are you feeling better? Is there anything I can do?"
            scene 128_s46 with dissolve
            r "..."
            scene 128_s45 with dissolve
            mc "*sigh* I'm sorry this happened to you. It was my fault for not purchasing enough supplies for the journey."
            mc "If you want to blame someone, then... blame me. But don't blame yourself. Please. You didn't do anything wrong."
            scene 128_s46 with dissolve
            r "*hic* I can't, [mc]... I don't know how to feel. I was carrying a child. A life. A future. And I didn't even know. *sob* I-I didn't even get to..."
            r "I don't know what to do."
            scene 128_s45 with dissolve
            mc "Me neither."
            scene 128_s46 with dissolve
            r "*sniff* Just... just give me some time alone. Please. I need to be alone with this for a while."
            scene 128_s45 with dissolve
            mc "Alright. I get it. I'll sleep on the couch. You can have the bed. Just know that I'll always be there for you whenever you need me."
            scene 128_s46 with dissolve
            scene 128_s27 with Fade(1.3,1.0,1.3)
            perception "You lay on the couch, staring at the gilded ceiling. The bed is only a few feet away, but it feels like miles."
            mc "..."
            stop music fadeout 1.0
            scene 128_s28 with Fade(1.3,1.0,1.3)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* (I should go. Better take care of this bandit problem as soon as possible.)"
            stop music fadeout 1.0
            scene 128_s40 with Fade(1.0,1.0,1.0)
            mc "You're still here, Nimah? Did you even sleep?"
            scene 128_s41 with dissolve
            nimah "I will always be here, Master. That is my duty. Would you like something before you depart? Breakfast is on the way."
            scene 128_s40 with dissolve
            mc "No need. I'll buy something in the market."
            scene 128_s41 with dissolve
            nimah "As you wish. Follow me—I will escort you out of the palace."
            scene 128_s40 with dissolve
            jump scene129
            
        play music "hope/mysterious_forest.mp3" fadein 3.0 loop
        scene 128_s21 with Dissolve(1.0)
        if mc_asked_wine_reb:
            if not mc_reb_breakup_final:
                r "Ah, if it isn't my wine entrepreneur husband."
            else:
                r "Ah, if it isn't the wine entrepreneur."
            scene 128_s22 with dissolve
            if reb_sick:
                mc "Becky! You're awake. And you're... you're glowing. You look so much better than in the morning. How have you been? Feeling better?"
                scene 128_s21 with dissolve
                r "Oh, don't worry about it. I'm back to normal now. Or at least, normal enough."
                r "The potion the healer gave me did the job, although not before burning my tongue and my intestines."
                scene 128_s22 with dissolve
                mc "*chuckles* Ouch. That sounds... awful, but I'm glad it worked. I was so worried about you. I thought—"
                scene 128_s21 with dissolve
                r "I know. I'm sorry for scaring you. And I'm sorry for... for being so dramatic."
                scene 128_s22 with dissolve
                mc "Don't apologize for that."
                scene 128_s21 with dissolve
                r "Well. Now that I'm feeling better, I can be dramatic about other things. Like you suddenly being a wine entrepreneur."
                mc "Wine entrepreneur? What are you talking about?"
            else:
                mc "Wine entrepreneur? That's a new one. What are you talking about?"
            scene 128_s21 with dissolve
            r "Yes. Apparently, you told the maid outside to bring me five different bottles of wine."
            r "Do you know how long it's been since I had wine? Real wine? Not the watered-down vinegar they had in that cellar?"
            r "You thought of me even when her breasts were fully out~ How nice of you. How very, very nice."
            scene 128_s22 with dissolve
            mc "*chuckles* Glad you enjoyed them. The wine, I mean. But seriously, what's up with that?"
            scene 128_s21 with dissolve
            r "I guess it's a dress code? All the maids were dressed like that. Even when I came here before with my mother, they were the same."
            r "Tell me, did you stare at them while telling her about the wine? Be honest. I'll know if you're lying."
            scene 128_s22 with dissolve
            mc "N-No... I didn't stare. I barely noticed."
            scene 128_s21 with dissolve
            r "I know you did. You're a terrible liar, bear. But it's fine. I'm not jealous. Why would I be jealous? Mine were bigger, weren't they?"
            scene 128_s22 with dissolve
            mc "They sure are. The biggest in the kingdom... kingdoms. All of them."
            scene 128_s21 with dissolve
            r "I know~ So, had fun out there? You were gone for ages. I was starting to think you'd drowned in the baths."
        else:
            r "Had fun out there? You were gone for ages. I was starting to think you'd drowned in the baths."
            if reb_sick:
                scene 128_s22 with dissolve
                mc "Becky! You're awake. And you're... you're glowing! You look so much better than in the morning. How have you been? Feeling better?"
                scene 128_s21 with dissolve
                r "Oh, don't worry about it. I'm back to normal now. Or at least, normal enough."
                r "The potion the healer gave me did the job, although not before burning my tongue and my intestines."
                scene 128_s22 with dissolve
                mc "*chuckles* Ouch. That sounds... awful, but I'm glad it worked. I was so worried about you. I thought—"
                scene 128_s21 with dissolve
                r "I know. I'm sorry for scaring you. And I'm sorry for... for being so dramatic."
                scene 128_s22 with dissolve
                mc "Don't apologize for that."
                scene 128_s21 with dissolve
                r "Tell me, did you have fun in the baths?"
        scene 128_s22 with dissolve
        mc "The baths were great, you should try them. Oh, and I got assigned a mission for tomorrow. Already."
        scene 128_s21 with dissolve
        r "They sure don't waste time here."
        r "And yes—that was my idea. They took me to the planning room about an hour after you left. Sanoud wanted to know what you were capable of, so I told him."
        scene 128_s22 with dissolve
        mc "Yeah, he said you vouched for me personally. I'm glad you think so highly of me, but... I hope you didn't exaggerate too much."
        scene 128_s21 with dissolve
        r "I wouldn't have told him about you in that way if I knew he was planning to send you into danger immediately."
        r "Just promise me you won't be reckless, love. "
        scene 128_s22 with dissolve
        mc "I will. Promise."
        if not mc_reb_breakup_final:
            scene 128_s23 with Dissolve(1.0)
            r "So... Come here. Let me feel your warmth~ I've been waiting in this giant bed all by myself."
            scene 128_s24 with Fade(1.0,1.0,1.0)
            perception "You slip under the covers beside her. She immediately curls into your side, her head finding your chest, her arm draping over your body."
            scene 128_s25 with Dissolve(1.0)
            r "Mmmm~ You smell so good."
            if mc_sexed_reb_palace and not mc_left_reb_s124:
                r "By the way, I almost used up all the tissues because of you. I had the servant, Nimah, bring me another box."
                mc "Huh? Did I make you sick?"
                if s124_thighjob:
                    r "No, you idiot. It's because you covered my entire lower half with your seed."
                    mc "*chuckles* Ah. I see."
                    r "Next time, I want you to fill me up. Finish inside me~"
                else:
                    r "No, you idiot. It's because I kept leaking with your seed."
                    mc "*chuckles* Ah. Did you manage to stop it?"
                    r "Yes. It does feel empty though. I might need a refill soon~"
                mc "Sure. I can provide that. I'm very good at it."
                r "*giggles* Close those eyes now and drift away."
                mc "..."
            scene black with Dissolve(2.0)
            stop music fadeout 3.0
            sensation "Her fragrance fills your senses, and her warmth seeps into you. The way she kisses your neck every now and then gets your heart beating fast. You lose about an hour of sleep because of it."
            scene 128_s29 with Fade(1.0,1.0,1.0)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* I'll be heading out, Becky. Get some more rest."
            scene 128_s30 with Dissolve(1.0)
            r "Nooooo.... Ugh, do you have to? Please don't go anywhere... Let the bandits handle themselves."
            mc "*laughs* I'll be back before you know it."
        else:
            scene 128_s26 with Dissolve(1.0)
            r "Get some sleep. You can take the couch."
            mc "*chuckles* Hogging the bed all to yourself?"
            scene 128_s21 with Dissolve(1.0)
            r "Yes~ It's reserved for my husband, which you're not. You made that choice. I'm just... respecting it."
            scene 128_s22 with dissolve
            call screen scene128_choice01 with dissolve
            mc "So be it. The couch it is."
            scene 128_s27 with Fade(1.3,1.0,1.3)
            perception "You lay on the couch, staring at the gilded ceiling. The bed is only a few feet away, but it feels like miles."
            r "Goodnight, [mc]. Try not to get yourself killed tomorrow. I'd still miss you, even if you're not my husband anymore."
            mc "Ahuh."
            r "I still love you... Y-You can come here if you want. I-I was just teasing!"
            mc "..."
            r "*sigh* Already asleep?"
            stop music fadeout 1.0
            scene 128_s28 with Fade(1.3,1.0,1.3)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* (I should go. Better take care of this bandit problem as soon as possible.)"

    else:
        if mc_asked_wine_reb:
            scene 128_s31 with Dissolve(1.0)
            q "[mc]. Was it you who told the servant to bring wine?"
            scene 128_s32 with dissolve
            mc "Yup. Thought you might want to wind down a little."
            scene 128_s31 with dissolve
            q "Thank you. That was thoughtful, but this isn't the time for that. I told the her to return the bottles."
            scene 128_s32 with dissolve
            mc "I see. I should have asked you first."
            scene 128_s31 with dissolve
            q "...Still, thank you. I'm glad you thought of me. Truly."
            q "Tell me, did Sanoud tell you of his plans?"
        else:
            scene 128_s31 with Dissolve(1.0)
            q "[mc]. Report. Did Sanoud tell you of his plans?"
    
        scene 128_s32 with dissolve
        mc "He did. Of one plan at least. I'm to go to the market tomorrow and sort out a bandit problem."
        scene 128_s31 with dissolve
        q "Good. Be swift and efficient. Don't draw it out longer than necessary."
        q "We need them to change, not just disappear. I'm sure he told you that if something were to happen to them, another group would simply take their place."
        scene 128_s32 with dissolve
        mc "I know. I'll try my charismatic side first."
        scene 128_s31 with dissolve
        q "This isn't a joking matter, [mc]. If you succeed on your first task, Hod will think highly of you."
        q "Your reputation will begin to build and doors will start to open."
        scene 128_s32 with dissolve
        mc "I'll handle it."
        mc "And please don't take this the wrong way, your majesty. But... is it not a good time to finally change your clothes?"
        scene 128_s31 with dissolve
        q "*chuckles* I get what you're saying. I look like a beggar wearing these rags. A street urchin who wandered into a palace by mistake."
        scene 128_s32 with dissolve
        mc "Well, I didn't mean it like that—"
        scene 128_s31 with dissolve
        q "It's fine. You're not wrong. I was actually offered a new dress by Hod himself. Something befitting a queen. Silk adorned with gold. A gown that would make the court gasp."
        q "But... I suppose I didn't feel like wearing it."
        scene 128_s32 with dissolve
        mc "Why's that? If you don't mind me asking."
        scene 128_s31 with dissolve
        q "It just doesn't feel right to dress up in gold and silk when my people are suffering under Avery's rule. It doesn't feel right to look like a queen when my kingdom is bleeding."
        q "I suppose it's my way of... staying connected. To the struggle. To... to the reality of what's happening."
        scene 128_s32 with dissolve
        mc "That's very considerate of you."
        scene 128_s33 with Dissolve(1.0)
        q "*sigh* I don't know about that. I need to rest and think. They barely gave me an hour before they pulled me into meetings."
        scene 128_s34 with dissolve
        mc "They won't bother us now, hopefully."
        mc "So..."
        q "Hmm?"
        mc "Where should I sleep? There's only one bed."
        scene 128_s26 with Dissolve(1.0)
        q "Ah. The couch over there, to your left."
        mc "The couch? Seriously?"
        if mc_kiss_queen and mc_queen_choice_sex and not mc_angered_queen:
            $ mc_harem_queen = True
            scene 128_s35 with Dissolve(1.0)
            q "*sigh* Fine. Come here. I suppose you wanting to sleep next to each other isn't too unexpected after you kissed me."
            scene 128_s36 with dissolve
            mc "Yes! Thank you."
            scene 128_s35 with dissolve
            q "Just don't get any ideas, [mc]. I'm still your queen, and I'm still twice your age."
            scene 128_s36 with dissolve
            mc "Me? Never."
            scene 128_s37 with Dissolve(2.0)
            sensation "You lay next to her. Her weight pulls down the mattress, creating a slope that you can't help but follow. You drift closer, like a planet caught in the gravity of a dying star."
            scene 128_s38 with Dissolve(1.0)
            q "Goodnight, [mc]. Try to get some sleep. Tomorrow will be... eventful."
            mc "Goodnight, your majesty."
            stop music fadeout 1.0
            scene 128_s39 with Fade(1.3,1.0,1.3)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* Mmph... your majesty?"
            mc "(She's already gone.)"
            mc "(I should go as well. Better take care of this bandit problem as soon as possible.)"
        elif mc_kiss_queen:
            scene 128_s35 with Dissolve(1.0)
            q "*sigh* Listen, [mc]. I thought about it really hard, and... I'm sorry. Whatever it is you want us to be, it simply can't happen."
            q "That kiss you gave will be the end of it. Please don't take it personally, I just... don't think of you like that."
            scene 128_s36 with dissolve
            mc "..."
            mc "Alright. I resepct you being forward with me. I'll stop trying to get you, but know that I still like you."
            scene 128_s35 with dissolve
            q "Thank you. The feeling is mutual, [mc]. I {i}do{/i} like you, but not in the way I assume you do to me."
            scene 128_s36 with dissolve
            scene 128_s27 with Fade(0.5,0.5,0.5)
            stop music fadeout 1.0
            perception "You lay on the couch, staring at the gilded ceiling. The bed is only a few feet away, but it feels like miles."
            scene 128_s28 with Fade(1.3,1.0,1.3)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* Mmph... your majesty?"
            mc "(She's already gone.)"
            mc "(I should go as well. Better take care of this bandit problem as soon as possible.)"
        else:
            scene 128_s33 with dissolve
            q "There's only one bed here, [mc]. I'm sorry they didn't account for you when they assigned the room."
            q "Maybe they will start doing that once you prove your worth to them."
            scene 128_s34 with dissolve
            mc "*sigh* Fine."
            scene 128_s27 with Fade(0.5,0.5,0.5)
            stop music fadeout 1.0
            perception "You lay on the couch, staring at the gilded ceiling. The bed is only a few feet away, but it feels like miles."
            scene 128_s28 with Fade(1.3,1.0,1.3)
            play music "nature.mp3" fadein 1.0 volume 0.3 loop
            mc "*yawn* Mmph... your majesty?"
            mc "(She's already gone.)"
            mc "(I should go as well. Better take care of this bandit problem as soon as possible.)"

    stop music fadeout 1.0
    scene 128_s40 with Fade(1.0,1.0,1.0)
    mc "You're still here, Nimah? Did you even sleep?"
    scene 128_s41 with dissolve
    nimah "I will always be here, Master. That is my duty. Would you like something before you depart? Breakfast is on the way."
    scene 128_s40 with dissolve
    mc "No need. I'll buy something in the market."
    scene 128_s41 with dissolve
    nimah "As you wish. Follow me—I will escort you out of the palace."
    scene 128_s40 with dissolve
    jump scene129

label scene128_choice01_op2:
    $ mc_scared_reb = True
    $ reb_love -= 30
    scene 128_s43 with Dissolve(1.0)
    mc "No. I'll take the bed. You sleep on the couch."
    scene 128_s44 with dissolve
    r "*chuckles* What? This is my bed. I'm the princess. You're the—"
    scene 128_s43 with dissolve
    mc "Come on. Move. I'm not asking."
    scene 128_s44 with dissolve
    r "A-Are you actually serious? You're ordering me out of my own bed?"
    scene 128_s43 with dissolve
    mc "I am. I'm too tired for this, Rebecca. Too tired for the teasing, too tired for the way you look at me like I'm something to be managed. Leave the bed. Get on the couch. Now."
    scene 128_s44 with dissolve
    r "..."
    r "[mc], you're scaring me... You're never like this. You're never—"
    scene 128_s43 with dissolve
    mc "*sigh* Get off the bed before I get angry, Rebecca. I don't have time for your spoiled self."
    scene 128_s44 with dissolve
    r "..."
    r "A-Alright. I'm sorry for making you angry... I-I didn't mean to... I just wanted..."
    scene 128_s39 with Fade(1.5,1.0,1.3)
    play music "nature.mp3" fadein 1.0 volume 0.3 loop
    mc "*yawn* (Mmph... that was a good sleep.)"
    mc "(Dammit... I should go. Better take care of this bandit problem as soon as possible.)"
    stop music fadeout 1.0
    scene 128_s40 with Fade(1.0,1.0,1.0)
    mc "You're still here, Nimah? Did you even sleep?"
    scene 128_s41 with dissolve
    nimah "I will always be here, Master. That is my duty. Would you like something before you depart? Breakfast is on the way."
    scene 128_s40 with dissolve
    mc "No need. I'll buy something in the market."
    scene 128_s41 with dissolve
    nimah "As you wish. Follow me—I will escort you out of the palace."
    scene 128_s40 with dissolve
    jump scene129
    
label scene129:
    if mc_touched_nimah:
        $ nimah_love += 10
    if mc_kiss_nimah:
        $ nimah_love += 10

    scene 129_s1 with Fade(1.0,1.0,1.0)
    play music "nature.mp3" fadein 1.0 loop
    perception "You step out of the palace and into the city. The sun shines harshly across the windows of the sandstone buildings, giving a blinding glare to your eyes."
    scene 129_s3 with Dissolve(1.0)
    nimah "Good luck with your mission, Master. I will be here when you return."
    scene 129_s2 with dissolve
    mc "Here? Like outside the palace? You're just going to stand at the gates all day waiting for me?"
    scene 129_s3 with dissolve
    if mc_princess_success:
        nimah "Yes. The princess is needed somewhere else and won't return to her room until nighttime. There is nothing for me to do inside. My place is wherever I might be of use."
    else:
        nimah "Yes. The Queen is needed somewhere else and won't return to her room until nighttime. There is nothing for me to do inside. My place is wherever I might be of use."
    scene 129_s2 with dissolve
    if mc_karma >= 5:
        mc "Alright... but make sure to drink some water. And stay in the shade."
    else:
        mc "Alright... I'm not entirely agaisnt this type of respect."
        scene 129_s3 with dissolve
        nimah "I will do as you ask."
    if mc_touched_nimah and mc_kiss_nimah:
        nimah "Would you like to fondle my breasts before heading out? You seemed to have an interest in them yesterday."
        scene 129_s2 with dissolve
        mc "Umm..."
        scene 129_s3 with dissolve
        nimah "Your touch was very gentle. And the kiss you gave me afterwards was... kind."
        scene 129_s2 with dissolve
        call screen scene129_choice01 with dissolve
        
    else:
        jump scene129_2

default scene129_choice01_op1_ye = False
label scene129_choice01_op1:
    $ scene129_choice01_op1_ye = True
    $ nimah_love += 10
    mc "Sure. Just a squeeze, for good luck."
    scene 129_s3 with dissolve
    nimah "Go ahead."
    scene 129_s2 with dissolve
    scene 129_s4 with Dissolve(1.0)
    sensation "You cup her pointy breasts, she is soft and warm. Some of the tension in your shoulders eases, just slightly."
    mc "Your nipples are already stiff. Were you expecting this?"
    scene 129_s5 with dissolve
    nimah "*giggles* I was. I remembered how you looked at me yesterday. How your hands felt."
    scene 129_s6 with dissolve
    mc "Whoa... you just giggled. You're not a robot after all. There's a person in there."
    scene 129_s5 with dissolve
    nimah "I still don't know what a robot is, Master. Is it a creature from your homeland? Some kind of magical construct?"
    scene 129_s6 with dissolve
    mc "Nevermind. Catch you later, Nimah."
    scene 129_s5 with dissolve
    nimah "You want to catch me? I did not realize we were playing a game."
    scene 129_s6 with dissolve
    mc "It's... it's just an expression. It means 'see you later'. That's all."
    scene 129_s3 with Dissolve(1.0)
    nimah "Ah. I understand. Then I will see you later, Master."
    jump scene129_2

label scene129_choice01_op2:
    mc "Now is not a good time, Nimah. I need to keep my head clear. Another time, maybe. If I come back."
    scene 129_s3 with dissolve
    nimah "Of course. Please forgive my imprudence."
    jump scene129_2

label scene129_2:
    nimah "By the way, the stablehands brought your mare here earlier. She's been fed, watered, and groomed."
    scene 129_s2 with dissolve
    mc "Good. She's been through a lot."
    scene 129_s3 with dissolve
    nimah "As for a weapon, you can borrow a sword from the guards at the mission site. Sir Flint has arranged it. Standard palace steel."
    scene 129_s2 with dissolve
    mc "What about my sword? Did Alex say anything?"
    scene 129_s3 with dissolve
    nimah "I don't know about that, Master. Sir Flint didn't mention any carriage. I only know what I was told."
    scene 129_s2 with dissolve
    mc "Hmm... alright. I'll ask Alex when I see her."
    if not scene129_choice01_op1_ye:
        mc "Catch you later, Nimah."
        scene 129_s3 with dissolve
        nimah "You want to catch me? I did not realize we were playing a game."
        scene 129_s2 with dissolve
        mc "It's... it's just an expression. It means 'see you later'. That's all."
        scene 129_s3 with dissolve
        nimah "Ah. I understand. Then I will see you later, master."
        scene 129_s2 with dissolve

    scene 129_s7 with Fade(1.0,1.0,1.0)
    mc "(Hmm... Man, this map is much bigger than Irda's. I can't even see where the market is... wait. There.)"
    mc "(It's close to the neighborhood where Reham's parents live.)"
    stop music fadeout 1.0
    scene 129_s8 with Fade(1.0,1.0,1.0)
    play music "talkingAmbiance.mp3" fadein 1.0 volume 0.1 loop
    mc "The map says their place is right on this street."
    scene 129_s9 with Dissolve(1.0)
    mc "Another tavern? Yeah, there's no mistaking it now—"
    mc "What the—? What are they doing?"
    scene 129_s10 with Dissolve(1.5)
    mc "Hey! You were supposed to be hidden. The was the whole point."
    guard_male "We were hidden, sir. For quite a while now. But we noticed something suspicious."
    mc "What is it?"
    guard_female "No matter how long we waited, nobody came out or went in. Not a single whisper was heard from inside."
    guard_female "We sent a scout to look closer, but he didn't find anything. No one is inside. The building is completely empty."
    mc "What? D-Did they all just leave?"
    guard_male "It appears so. There's simply nobody inside. However..."
    guard_male "The place inside is in perfect condition. There's food in the pantry, still fresh. We also found coin in the strongbox. Which suggests they didn't run away."
    mc "So... they're still in the city. But where would—"
    scene 129_s11 with dissolve
    if not mc_killed_reham:
        sensation "Your blood runs cold as a dozen images flash in your mind. Yasmine and Reham, alone in their house. Maia, sleeping under that same roof."
    else:
        sensation "Your blood runs cold as a dozen images flash in your mind. Maia, sleeping under the roof of a man wanted by those bandits."
    mc "Oh no."
    guard_female "Sir?"
    play sound "sound_effects/running_concrete.mp3"
    scene 129_s12 with vpunch
    guard_female "Sir?! Do you have an idea where they might be?!"
    mc "They didn't run! Follow me—NOW!"
    guard_male "You heard him! Follow the man with the metal hand!"
    stop music fadeout 2.0
    stop sound fadeout 1.0
    scene 129_s13 with Fade(1.3,1.0,1.3)
    mc "Hahhh... ahnn... Please. Please let me be wrong."
    scene 129_s14 with dissolve
    mc "(It's quiet... m-maybe I got it wrong.)"
    play sound "sound_effects/doors/door_open3.mp3"
    if not mc_killed_reham:
        scene 129_s15 with Dissolve(1.0)
        play music "sex01.mp3" fadein 3.0 loop
        perception "A dozen armed men sit or stand in casual poses, leaning against walls, one even chewing on a piece of bread."
        scene 129_s17 with Dissolve(1.0)
        vic "Ah, [mc]. We've been waiting. Come sit with me. We have much to talk about, you and I."
        scene 129_s18 with Dissolve(1.0)
        mc "..."
    else:
        scene 129_s16 with Dissolve(1.0)
        play music "sex01.mp3" fadein 3.0 loop
        perception "A dozen armed men sit or stand in casual poses, leaning against walls, one even chewing on a piece of bread."
        scene 129_s17 with Dissolve(1.0)
        vic "Hmm? Oh, [mc]. I see you've already made yourself comfortable here. Nice place."
        vic "We found the girl eating from the pantry like it was her own house. Can't blame her—it practically is now, isn't it?"
        vic "Come, come. Sit with me. We have much to talk about, you and I."
        scene 129_s19 with Dissolve(1.0)
        perception "The bandits circle the dinner table, their weapons drawn but relaxed. Maia looks up at you with worried look."

    scene 129_s20 with Dissolve(1.0)
    denovan_ "Sit."

    if mc_killed_reham:
        scene 129_s21 with Dissolve(1.0)
        vic "Tell me, [mc]. What kind of parasite are you?"
        scene 129_s22 with dissolve
        mc "Your people were the ones who destroyed the family living here with your threats. We simply... took refuge."
        scene 129_s21 with dissolve
        vic "Ah, makes perfect sense then. Like vultures circling a carcass. Very cold. I can respect that."
        scene 129_s22 with dissolve
        mc "..."
        scene 129_s21 with dissolve
        vic "By the way, are you free? I would like to formally invite you to join us. I think you'd fit right in."
        scene 129_s22 with dissolve
        if not mc_intended_reham:
            mc "I... I didn't mean for it to happen. I swear."
            scene 129_s21 with dissolve
            vic "What do you mean?"
            scene 129_s22 with dissolve
        mc "Your men took Yasmine—the mother. Then her daughter followed after, when she knew what happened to her mother."
        mc "I didn't know where they went. I didn't know if they were alive or dead... What did you do to them?"
        scene 129_s44 with dissolve
        vic "Both the mother and her daughter still live. You have my word on that. They wanted a fresh start, away from this house, away from the district."
        scene 129_s45 with dissolve
        minthra "I understand why I did not feel any strength when they vanished now."
        scene 129_s44 with dissolve
        vic "They ran off together. I can't say the same about the husband, Rohan."
        vic "He'll stay with us until he pays his debt. Cleaning, washing dishes, scrubbing floors. Whatever we need. It's not a dungeon—it's honest work."
        scene 129_s45 with dissolve
        mc "Y-You let them go? Yasmine and Reham? Just... let them walk away?"
        scene 129_s44 with dissolve
        vic "Please, [mc]. We're not monsters. At least not {i}me{/i}. I can't say the same would have happened if it was the previous one in charge."
        vic "Besides, we're here to make a deal. What better way to say we changed than to let an innocent family go free?"
        scene 129_s45 with dissolve
        mc "Where are they?"
        scene 129_s21 with dissolve
        vic "I doubt you would see them again. They've decided to start new lives somewhere else in a different district."
        scene 129_s22 with dissolve
        mc "..."
        mc "Then what do you want? Why are you here?"
    else:
        scene 129_s22 with Dissolve(1.0)
        mc "What do you want. Why are you here."

    scene 129_s21 with dissolve
    vic "We will get to that. Business can wait. For now—tell me, how are you? It's been a while."
    vic "You look well. And that hand... very impressive. Adamantite, isn't it? You've moved up in the world."
    scene 129_s22 with dissolve
    mc "Fine. I'm fine. Now tell me why you're in this house."
    scene 129_s21 with dissolve
    vic "Why so aggressive already? We've barely exchanged pleasantries."
    scene 129_s23 with dissolve
    if mc_killed_reham:
        vic "Look around you—this girl's face is scrunched up because she's scared, not because we've hurt her. We didn't even lay a single finger on her. You have my word."
    else:
        vic "Look around you—those ladies' faces are scrunched up because they're scared, not because we've hurt them. We didn't even lay a single finger on them. You have my word."
    scene 129_s22 with dissolve
    mc "Good. That would be a very bad thing if you did. For all of you."
    scene 129_s21 with dissolve
    vic "*chuckles* Man, it's so fucking hot here, huh? You can barely walk ten feet before getting drenched in sweat."
    scene 129_s22 with dissolve
    mc "..."
    scene 129_s21 with dissolve
    vic "*ahem* Anyway. You do remember me, right?"
    scene 129_s22 with dissolve
    if mc_helped_nadia:
        mc "I do. Your... 'guild' was harassing Nadia. I told you to stop."
        scene 129_s21 with dissolve
        vic "I'm so glad you remember. Honestly? I was worried you'd forgotten. That tavern was a nice establishment. Shame what happened to it... to Abel."
        vic "But that's how it is. People rise, get overconfidant, then fall."
    else:
        mc "I don't. Your face isn't familiar to me."
        scene 129_s21 with dissolve
        vic "Ah, that makes sense. We didn't directly meet before. I was always in the background."
        vic "Abel was the face of the operation. {i}I{/i} was the one who made things run."
    play sound "sound_effects/doors/door_knock_hard1.mp3"
    scene 129_s24 with dissolve
    n_guard "[mc]?! Are you in there? We're ready to breach on your command!"
    scene 129_s25 with dissolve
    vic "Tch. That won't do. This room is already cramped as is—adding more bodies would be... unpleasant. For everyone."
    vic "Would you kindly tell them to wait outside, [mc]?"
    scene 129_s24 with dissolve
    mc "...Stay outside! We're talking. It's... it's under control."
    n_guard "..."
    n_guard "We will stay here. If you're not out in ten minutes, we breach."
    scene 129_s21 with Dissolve(1.0)
    vic "Now. Where do we even begin?"
    if not mc_killed_reham:
        scene 129_s26 with dissolve
        vic "I see you have quite the family here. The man—what's his name, dear?"
        yasmine "..."
        bandit "Boss asked you a question."
        scene 129_s27 with dissolve
        yasmine "Rohan. His name is Rohan."
        scene 129_s26 with dissolve
        scene 129_s21 with Dissolve(1.0)
        vic "Rohan! That's right. He ran off. The little shit is too small to even catch. Slippery. Quick. Like a..."
        scene 129_s22 with dissolve
        bandit "Ferret."
        scene 129_s28 with dissolve
        vic "Ferret! They're quite elusive. *laughs* Last week I had men chasing him for three blocks before he disappeared into a drainage pipe."
        scene 129_s22 with dissolve
        mc "Get to the point, Vic. I'm losing my patience."
        scene 129_s21 with dissolve
        vic "Right. You're a busy man. I understand. So here it is—I'm here to propose a deal, [mc]. A mutually beneficial arrangement."
    else:
        vic "*ahem* I'm here to propose a deal, [mc]! A mutually beneficial arrangement."
    vic "You have a direct line to the king now. We can't ignore someone that important. And you... you can't ignore us either."
    scene 129_s22 with dissolve
    if not mc_killed_reham:
        mc "You come here, into this woman's house, uninvited. You get all your goons together like a coward and threaten innocent people. And you think you can take advantage of me?"
    else:
        mc "You come here, into this house, uninvited. You get all your goons together like a coward and threaten a single girl. And you think you can take advantage of me?"
    scene 129_s21 with dissolve
    if not mc_killed_reham:
        vic "Ugh, please. I already told you—we didn't do anything to them. Not a single hair harmed. The tea was lovely, by the way."
    else:
        vic "Ugh, please. I already told you—we didn't do anything to her. Not a single hair harmed."
    vic "And the men are for my protection. You have quite a reputation, [mc]. The man who fought Gaius. Who took down Abel. I'm not taking any chances."
    vic "Truth be told? I'm more scared of you than you are of me."
    scene 129_s22 with dissolve
    mc "Talk. What's this deal?"
    scene 129_s21 with dissolve
    vic "We need to settle some debts first. Clear the air. What you did to the tavern in Irda..."
    vic "...is completely forgiven! Water under the bridge."
    scene 129_s22 with dissolve
    mc "Huh?"
    scene 129_s21 with dissolve
    vic "The operation we ran under Abel—it was... old. We were past our prime. The laws were getting stricter, and our protection money was drying up."
    scene 129_s44 with dissolve
    vic "But then... I got a chance. When I learned from Abel that he'd captured a certain girl on behalf of Avery... I knew something was up."
    vic "A girl he'd been looking for for years suddenly shows up, delivered by the Queen's sister herself?"
    vic "Even an idiot would realize how suspicious that is. It was a baited hook. And Abel swallowed it like a cock."
    scene 129_s45 with dissolve
    mc "You knew? Why didn't you warn him, then? He was your boss."
    play sound "sound_effects/slam_wood.mp3"
    scene 129_s31 with vpunch
    play music "tense/the_devils_whisper.mp3" fadein 2.0 loop    
    vic "Tell him? Hah! I wanted this to happen. In fact, I should thank you for it. That ancient fuck deserved it."
    vic "Do you know how long I suffered under him? How many times I had to smile and nod while he made stupid decision after stupid decision? While he put our entire operation at risk for petty grudges?"
    vic "You'd be surprised at my happiness when I learned he was stabbed several times before being turned into charcoal."
    scene 129_s32 with dissolve
    mc "(Shit! I never brought this up with Maia. I should have talked to her... I should have prepared her.)"
    scene 129_s31 with dissolve
    vic "Was it you who did it? The stabbing?"
    vic "No... you're not that ruthless. Don't get me wrong—I don't doubt you could kill, but not with that kind of anger. That kind of... personal touch."
    scene 129_s33 with dissolve
    vic "Which means..."
    m "..."
    vic "You did it. The sweet little one."
    vic "*laughs* That was brutal, girl! The autopsy was difficult to perform, but the reports said he had multiple knife wounds in him before the fire started."
    scene 129_s34 with dissolve
    m "I... I don't—"
    scene 129_s33 with dissolve
    vic "You don't remember? How interesting. Do you at least remember how it felt killing a man like that? The first cut. The second."
    vic "Did it feel good? Did it feel like justice? Did it feel like... nothing at all?"
    scene 129_s34 with dissolve
    m "I... I don't remember... I don't want to..."
    scene 129_s33 with dissolve
    empathy "She buired it all away. It would be unwise to ignite the flames now, then again, unresolved trauama tends to come out at some point even harder."
    mc "(This piece of shit. He's tormenting her for fun. I'll show him. I'll show all of them!)"
    logic "Relax. He's messing with you. Steel yourself. Stay strong."
    call screen scene129_choice02 with dissolve

label scene129_choice02_op1:
    $ mc_killed_vic = True
    scene 129_s35 with dissolve
    sensation "You don't think. You just move. Your metal arm swings up in an arc, faster than sight. The distance between you and Vic vanishes in a heartbeat."
    play sound "sound_effects/body/stab4.mp3"
    scene 129_s36 with vpunch
    perception "Your fingers pierce his neck before he can finish his next breath."
    bandit "W-Wha?!"
    bandit "Boss?! He killed the boss!"
    scene 129_s37 with dissolve
    mc "You bastards! You think you can come into this woman's HOME, and get away with it?!"
    mc "You think you can threaten innocent people? Torment a girl who's already been through hell? Use them as leverage against ME?!"
    mc "Screw your talks. Screw your deals. Screw whoever comes to take your place after you're gone. I'll chase every single one of you to hell if I have to."
    scene 129_s38 with dissolve
    denovan_ "G-Get him!"
    if not mc_killed_reham:
        mc "Girls, get to the bedroom and don't come out until I tell you."
    else:
        mc "Maia, get to the bedroom and don't come out until I tell you."
    scene 129_s39 with Dissolve(2.0)
    sensation "You feel strange. Detached. As if you're not moving on your own free will—like your body is operating on autopilot."
    sensation "You don't feel the impacts. You don't hear their screams. One by one, they fall before you. One by one, the room grows quieter."
    stop music fadeout 3.0
    scene 129_s40 with Dissolve(1.0)
    ""
    play sound "sound_effects/doors/door_open3.mp3"
    scene 129_s41 with Dissolve(1.0)
    play music "night.mp3" fadein 1.0 volume 0.4 loop
    ""
    scene 129_s42 with Dissolve(1.0)
    mc "..."
    guard "S-Sir?! What happened in there?! We heard screaming—we were about to breach—"
    scene 129_s43 with dissolve
    mc "It's done. Take their bodies away. And clean the house while you're at it."
    mc "There's blood on the floor."
    scene 129_s42 with dissolve
    guard "Done? D-Did you... kill them? All of them? By yourself?"
    scene 129_s43 with dissolve
    mc "Yes. The diplomatic approach failed."
    scene 129_s42 with dissolve
    jump scene129_3

label scene129_choice02_op2:
    mc "That's enough, Vic. You're talking to me."
    scene 129_s31 with Dissolve(1.0)
    vic "Right, right. I got carried away."
    scene 129_s32 with dissolve
    logic "See? Breath. I'm on your side."
    scene 129_s31 with dissolve
    vic "Like I was saying—once I learned what happened to Abel, I saw an opportunity. I gathered those loyal to me, liquidated what assets I could, and came south."
    vic "I killed the man Abel appointed to run things here. Took his place and built the Ohm from the ashes of Abel's old network."
    scene 129_s32 with dissolve
    mc "Good for you. What's your goal now?"
    scene 129_s44 with dissolve
    vic "*sigh* Times are changing, [mc]. I know I can't keep this up forever. The laws were strict back in Irda, and they're even stricter here."
    vic "The guards are better trained. The courts are less corrupt. The people are more willing to fight back."
    scene 129_s51 with dissolve
    vic "I'd rather not make the same mistake Abel did. He thought he was untouchable. He thought his connections would protect him."
    vic "We'll change our ways. The Ohm will remain—but not as thugs. We'll rule this district and many others, just not how we used to do it."
    if not mc_killed_reham:
        scene 129_s52 with Dissolve(1.0)
    else:
        scene 129_s50 with Dissolve(1.0)
    vic "The kind of operation the king doesn't need to send soldiers to crush. However... we require protection from the king."
    mc "You're ready to drop everything and change, all of a sudden? Just like that?"
    if not mc_killed_reham:
        scene 129_s50 with Dissolve(1.0)
    else:
        scene 129_s45 with Dissolve(1.0)
    if mc_attack_yasmine_bandits or mc_killed_yasmine_bandits:
        mc "Your men attacked me in an alley two days ago while threatening a lonely woman. You really think they would go along with this?"
    else:
        mc "I was almost attacked by your men in an alley two days ago. You really think they would go along with this?"
    if not mc_killed_reham:
        vic "That was just the fading remnants of an old regime. They were used to doing things the brutal way. Old habits die hard, but I'll whip 'em into shape."
        scene 129_s44 with Dissolve(1.0)
    else:
        scene 129_s44 with Dissolve(1.0)
        vic "That was just the fading remnants of an old regime. They were used to doing things the brutal way. Old habits die hard, but I'll whip 'em into shape."
    vic "You'll find me very accommodating, [mc]. I'm the exact opposite of my old boss. I'm a businessman first and formost."
    if mc_helped_nadia:
        vic "I already told you that before, didn't I?"
    scene 129_s45 with Dissolve(1.0)
    mc "Good. So... that's it? We could've talked about this at your place. Why drag all your men here?"

    if mc_accept_ablegirl:
        $ mc_killed_vic = True
        scene 129_s46 with dissolve
        vic "I believe in the rule of an eye for an eye, [mc]."
        scene 129_s47 with dissolve
        mc "Hmm?"
        scene 129_s46 with dissolve
        vic "Andressa."
        scene 129_s47 with dissolve
        mc "Who?"
        scene 129_s46 with dissolve
        vic "*chuckles* Of course you don't remember. She was just another face in a room full of faces."
        vic "She was the woman you saw lying on the table when you spoke to Abel."
        scene 129_s47 with dissolve
        mc "Ah... Look, I'm sorry. But you said you had reports, right? Then you'll know she was killed by the guards."
        scene 129_s46 with dissolve
        vic "I know. Shot right through the neck. But... it doesn't change the fact that it wouldn't have happened if you weren't there."
        vic "You brought the guards. You brought the fire. You set everything in motion. And Andressa... she was collateral damage."
        vic "I loved her, you know?"
        vic "I really did. She was the only good thing in my life. The only person who looked at me and saw something worth saving. And now she's gone... Because of you."
        scene 129_s47 with dissolve
        mc "..."
        scene 129_s46 with dissolve
        vic "An eye for an eye. A tooth for a tooth. After this... we'll be square. Don't blame me for what happens next."
        vic "The king will overlook this once we present our deal. So should you."
        play sound "sound_effects/slash01.mp3"
        scene 129_s48 with vpunch
        perception "He grips his dagger and swings it sideways in Maia's direction."
        scene 129_s49 with Dissolve(2.0)
        mc "..."
        perception "Time slows to a crawl. A droplet of spilled tea hangs suspended in the air. A fly hovers motionless near the window. Vic's dagger swings in a arc toward Maia's throat just inches away."
        impulse "Let their blood spill."
        scene 129_s35 with dissolve
        sensation "You don't think. You just move. Your metal arm swings up in an arc, faster than sight. The distance between you and Vic vanishes in a heartbeat."
        play sound "sound_effects/body/stab4.mp3"
        scene 129_s36 with vpunch
        perception "Your fingers pierce his neck before he can finish his next breath."
        bandit "W-Wha?!"
        bandit "Boss?! He killed the boss!"
        scene 129_s37 with dissolve
        mc "You bastards! You think you can come into this woman's HOME, and get away with it?!"
        mc "You think you can threaten innocent people? Torment a girl who's already been through hell? Use them as leverage against ME?!"
        mc "Screw your talks. Screw your deals. Screw whoever comes to take your place after you're gone. I'll chase every single one of you to hell if I have to."
        scene 129_s38 with dissolve
        bandit "G-Get him!"
        if not mc_killed_reham:
            mc "Girls, get to the bedroom and don't come out until I tell you."
        else:
            mc "Maia, get to the bedroom and don't come out until I tell you."
        scene 129_s39 with Dissolve(2.0)
        sensation "You feel strange. Detached. As if you're not moving on your own free will—like your body is operating on autopilot, a machine of death and fury."
        sensation "You don't feel the impacts. You don't hear their screams. One by one, they fall before you. One by one, the room grows quieter."
        stop music fadeout 3.0
        scene 129_s40 with Dissolve(1.0)
        ""
        play sound "sound_effects/doors/door_open3.mp3"
        scene 129_s41 with Dissolve(1.0)
        play music "night.mp3" fadein 1.0 volume 0.4 loop
        ""
        scene 129_s42 with Dissolve(1.0)
        mc "..."
        n_guard "S-Sir?! What happened in there?! We heard screaming—we were about to breach—"
        scene 129_s43 with dissolve
        mc "It's done. Take their bodies away. And clean the house while you're at it."
        mc "There's blood on the floor."
        scene 129_s42 with dissolve
        n_guard "Done? D-Did you... kill them? All of them? By yourself?"
        scene 129_s43 with dissolve
        mc "Yes. H-He tried to kill Maia. He... he really tried to end her life."
        mc "I almost lost her today. If I'd been a second slower... if I hadn't..."
        scene 129_s42 with dissolve
        n_guard "We'll handle the cleanup, sir. You should... you should sit down. Get some water. You're shaking."
        
    elif mc_killed_yasmine_bandits:
        $ mc_convince_vic = True
        $ mc_vic_fee = True
        scene 129_s21 with dissolve
        vic "I believe in the rule of an eye for an eye, [mc]."
        vic "You made quite the mess of one of my men the other day. You didn't just wound him. His head... it was completely missing."
        vic "Just how much of a monster are you? To do that to a man? To remove his head like a barbarian at a ritual sacrifice?"
        scene 129_s22 with dissolve
        mc "Your men attacked first. They drew their weapons against an innocent woman. I defended her."
        vic "..."
        scene 129_s21 with dissolve
        vic "*sigh* Sure. You also could have, I don't know, stabbed him? Choked him? Anything. But you removed his head."
        scene 129_s22 with dissolve
        mc "I had my reasons. They were threatening to enslave her. I got... angry."
        scene 129_s21 with dissolve
        vic "Angry? That's an understatement. But, I'm willing to forgive that... for a fee."
        scene 129_s22 with dissolve
        mc "A fee? I'll tell the palace. They'll decide if your cooperation is worth a fee."
        scene 129_s21 with dissolve
        vic "I'm sure they'll find that a reformed criminal organization with deep roots in the community is far more valuable than a pile of corpses."
        vic "Farewell, [mc]. We'll be in touch. Next time, no more surprise visits."
        scene 129_s22 with dissolve
        stop music fadeout 2.0
        scene 129_s53 with Fade(1.0,1.0,1.0)
        play sound "sound_effects/doors/door_open3.mp3"
        perception "The door opens. The street lanterns flood the cramped little house as Vic and his men file out slowly."
        vic "And oh, Andressa says hello."
        mc "Andressa?"
        vic "It's the woman you left when you ran off. The one you didn't take with you. *chuckles* She told me about it herself."
        mc "Look, I—"
        vic "I get it. Who knows what might've happened if you took her? She was in no shape to run—Abel had worked her over pretty thoroughly before you showed up."
        vic "She's fine, by the way. Escaped through a window on the second floor. Got a broken leg because of it, but it's still better than burning to a crisp next to Abel."
        scene 129_s55 with Dissolve(1.5)
        play music "night.mp3" fadein 1.0 volume 0.4 loop
        guard "Halt! Guards, restrain them!"
        vic "Whoa, whoa. Calm down. We sorted things out peacefully, didn't we, [mc]?"
        mc "We did. Let them go. They're not prisoners."
        guard "Are you certain, sir? These men are wanted for extortion, assault, kidnapping—his royalty himself labeled them bandits. We have orders to bring them in."
        mc "We reached an agreement. They'll change their ways, no more threats or violence. I'll make sure of it, personally."
        guard "..."
        scene 129_s56 with Dissolve(1.0)
        guard "Return to your compound. A clerk will visit you in a an hour to formalize the arrangement."
        guard "You'll be expected to provide full accounting of your operations—past, present, and future."
        vic "Understood."

    else:
        $ mc_convince_vic = True
        scene 129_s21 with dissolve
        vic "I wanted your full attention, [mc]. No—scratch that. I wanted the {i}king's{/i} full attention."
        vic "If I'd just sent a messenger to the palace, do you think anyone would have listened?"
        vic "This wasn't a threat. It's just a way to show we're serious, that we're willing to negotiate, with a little leverage to make sure you'd actually hear us out."
        scene 129_s22 with dissolve
        mc "Leverage? You mean hostages."
        scene 129_s21 with dissolve
        vic "Think of it as our way of making levearge."
        vic "We'll be in touch, [mc]. Next time, no more surprise visits."
        scene 129_s22 with dissolve
        mc "If you break this deal and go back to the old ways, or if I hear even a whisper that you've threatened these women again—"
        scene 129_s21 with dissolve
        vic "You'll kill me. I know. I'm not stupid enough to make an enemy of you twice, love."
        scene 129_s22 with dissolve
        stop music fadeout 2.0
        scene 129_s53 with Fade(1.0,1.0,1.0)
        play sound "sound_effects/doors/door_open3.mp3"
        perception "The door opens. The street lanterns flood the cramped little house as Vic and his men file out slowly."
        vic "And oh, Andressa says hello."
        mc "Andressa?"
        vic "It's the woman you left when you ran off. The one you didn't take with you. *chuckles* She told me about it herself."
        mc "Look, I—"
        vic "I get it. Who knows what might've happened if you took her? She was in no shape to run—Abel had worked her over pretty thoroughly before you showed up."
        vic "She's fine, by the way. Escaped through a window on the second floor. Got a broken leg because of it, but it's still better than burning to a crisp next to Abel."
        scene 129_s55 with Dissolve(1.5)
        play music "night.mp3" fadein 1.0 volume 0.4 loop
        guard "Halt! Guards, restrain them!"
        vic "Whoa, whoa. Calm down. We sorted things out peacefully, didn't we, [mc]?"
        mc "We did. Let them go. They're not prisoners."
        guard "Are you certain, sir? These men are wanted for extortion, assault, kidnapping—his royalty himself labeled them bandits. We have orders to bring them in."
        mc "We reached an agreement. They'll change their ways, no more threats or violence. I'll make sure of it, personally."
        guard "..."
        scene 129_s56 with Dissolve(1.0)
        guard "Return to your compound. A clerk will visit you in a an hour to formalize the arrangement."
        guard "You'll be expected to provide full accounting of your operations—past, present, and future."
        vic "Understood."

    jump scene129_3

label scene129_3:
    scene 129_s57 with Fade(1.5,1.0,1.5)
    if mc_killed_vic:
        perception "An hour passes. The guards work in silence—dragging bodies out the door, scrubbing blood from the floor. But the house still smells of iron and salt."
        scene 129_s58 with dissolve
        guard "We're finished here, sir. I'll post four guards nearby in case any more of them arrive—unlikely, given the agreement, but protocol is protocol."
    else:
        guard "We're finished here, sir. I'll post four guards nearby in case any more of them arrive—unlikely, given the agreement, but protocol is protocol."
    scene 129_s59 with Dissolve(1.0)
    mc "Thank you. For handling this."
    scene 129_s58 with dissolve
    guard "I will deliver the news to Ambassador Sanoud. What about you, sir? Perhaps it would be better if you stayed here, as an extra precautionary measure."
    scene 129_s59 with dissolve
    mc "Yeah, I'm staying here. After what just happened... I can't leave them."
    scene 129_s58 with dissolve
    guard "Understood. Take care."
    if mc_killed_vic:
        guard "And please rest for a while. You look... deranged."
    else:
        guard "And please rest for a while."
    scene 129_s59 with dissolve

    if not mc_killed_reham:
        scene 129_s60 with Fade(1.0,1.0,1.0)
        empathy "Fear takes hold of Yasmine. She's clearly on the verge of fainting, the delayed shock of someone holding themself together for too long."
        mc "Will your mother be fine, Reham?"
        scene 129_s61 with dissolve
        reham "No! She's barely breathing—I think we need to bring her to a healer!"
        scene 129_s60 with dissolve
        yasmine "I'm fine, honey. I promise. It's just... it's just the shock. Give me a moment to breath."
        yasmine "Besides, no way we can afford the costs of a healer right now."
        scene 129_s61 with dissolve
        reham "[mc] can help! He works for the guards now."
        scene 129_s60 with dissolve
        yasmine "We can't keep relying on—"
        scene 129_s61 with dissolve
        reham "W-What if it's something serious? What if your heart gives out from the stress?"
        scene 129_s62 with dissolve
        yasmine "I really am fine. See? Look. *chuckles* I can already move my legs again."
        scene 129_s149 with dissolve
        if mc_karma >= 5:
            mc "I can take you there if you want. I'll cover it."
            scene 129_s62 with dissolve
            yasmine "No. I can't let you do that, [mc]."
        else:
            mc "She looks fine to me."
            scene 129_s62 with dissolve
            yasmine "Yes. He's right."
        scene 129_s63 with dissolve
        reham "Mother!"
        scene 129_s62 with dissolve
        yasmine "That's enough worrying about me. What about Maia? She's the one I'm concerned about."
        scene 129_s64 with Dissolve(1.0)
        mc "Are you alright, Maia?"
        m "..."
        mc "Maia? Talk to me. Please."
        scene 129_s65 with dissolve
        m "Oh! I-I'm also doing well, [mc]... I'm fine. Everything's fine."
        scene 129_s66 with dissolve
        mc "You clearly aren't. You look like you're about to cry. Is it about what he said? About Abel?"
        m "..."
        scene 129_s65 with dissolve
        m "I need to go back in the bedroom. I'm tired."
        scene 129_s67 with Dissolve(1.0)
        mc "Hey! Don't just walk away—you can't keep burying this!"
        m "S-Sorry... I just... I can't right now. Please don't make me."
        scene 129_s68 with Dissolve(1.0)
        reham "I will talk to her, [mc]. She needs someone right now, but maybe not you."
        scene 129_s69 with dissolve
        mc "Thank you. She trusts you. She'll listen to you."
        scene 129_s71 with dissolve
        reham "I'm going to the bedroom, Mother. One last time—are you sure everything's fine?"
        reham "If you're lying to me, I'll never forgive myself for not dragging you to the hospice myself."
        scene 129_s70 with dissolve
        yasmine "Yes. Go with Maia. She was trying hard to be brave at first, but I know she was the most terrified."
        if mc_killed_vic:
            yasmine "And after what he said... about that Abel man... about what she did... and then what [mc] did to them in response..."
            yasmine "No one should have to witness that. Especially not a girl like her."
            scene 129_s71 with dissolve
            reham "I'll do what I can. She's stronger than she looks. She'll get through this."
        else:
            yasmine "And after what he said... about that Abel man... about what she did..."
            yasmine "She's been carrying something terrible inside her. Something she buried so deep she forgot it was there."
            scene 129_s71 with dissolve
            reham "I understand. She needs to talk about it, not to bury it again. That will only makes it worse."

        scene 129_s72 with Fade(1.3,1.0,1.3)
        mc "*sigh*"
        scene 129_s73 with Dissolve(1.0)
        if mc_killed_vic:
            yasmine "Don't be too hard on yourself, [mc]. You did it to protect us, I know. But... it was quite the sight when you took out that first man."
            yasmine "I tried to look away the moment you killed him, but she... she just kept staring at you. She didn't look away once."
            scene 129_s74 with dissolve
            mc "You mean Maia? She watched?"
            scene 129_s73 with dissolve
            yasmine "Yes."
            scene 129_s74 with dissolve
            mc "Dammit, Maia... Why? Why would she do that?"
            mc "After everything she's already buried—why would she put herself through more?"
            scene 129_s73 with dissolve
            yasmine "I haven't a clue. But maybe... maybe it's because she sees something in you? Something she recognizes. Something that makes her feel less alone."
            scene 129_s74 with dissolve
            mc "..."
        else:
            yasmine "You did the right thing, [mc]. I saw the rage in your eyes, and I'm glad you didn't follow through."
            scene 129_s74 with dissolve
            mc "Then why does it feel like I failed? Why does it feel like no matter what I do, the people around me keep getting hurt?"
            scene 129_s73 with dissolve
            yasmine "Because you care. That's the curse of caring. Every wound feels like your fault, every scar feels like a failure. But it's not. It's just... being human."
        
        scene 129_s75 with Dissolve(1.0)
        yasmine "Regardless, I, for one, am glad that you were here. The look in their eyes... it gave me shivers. It's as if they didn't see us as living beings."
        yasmine "*chuckles* It's twice now that you saved me. And twice... twice that my husband has vanished when I needed him the most."
        scene 129_s76 with dissolve
        mc "Ah, right. I didn't even think about him. Where is he now?"
        scene 129_s75 with dissolve
        yasmine "I saw him, he took one glance inside the house from the window and decided it wasn't worth his time."
        yasmine "Imagine? Imagine looking into your own home and seeing a dozen men surrounding your family, and you decide the best thing to do is... run?!"
        if mc_told_yasmine_leave:
            scene 129_s76 with dissolve
            mc "I already told you to leave him, Yasmine. What good is a man like that?"
            scene 129_s75 with dissolve
            yasmine "You did, but it's just that... when Reham finally arrived, when she walked through that door... I didn't want us to separate so soon."
            yasmine "I would be the monster in her eyes."
            scene 129_s76 with dissolve
            mc "Does she love her father that much?"
            scene 129_s75 with dissolve
            yasmine "Always has. She keeps believing he will change, but I don't know if her opinion will stay the same after today."
            scene 129_s76 with dissolve
            mc "She'll have to open her eyes at some point."
            scene 129_s75 with dissolve
            yasmine "I hope so. For her sake."
        else:
            scene 129_s76 with dissolve
            mc "I'm sorry. No one should have to go through this alone."
            scene 129_s75 with dissolve
            yasmine "I really wanted to give him one last chance. Especially after Reham arrived. I thought... maybe this will be the wake-up call."
            yasmine "She loves her father, that girl. But I don't know if her opinion will stay the same after today."
            scene 129_s76 with dissolve
            mc "That means... whatever he was before all this, he was a good man?"
            scene 129_s75 with dissolve
            yasmine "He was. But that man is long gone now."
        
        scene 129_s77 with Dissolve(1.0)
        yasmine "Could you... umm... stay?"
        scene 129_s78 with dissolve
        mc "Hm?"
        scene 129_s77 with dissolve
        yasmine "*chuckles* I have never felt as safe as I do when I'm with you, [mc]... A-At least just until tomorrow."
        scene 129_s78 with dissolve
        mc "The guard commander already assigned some men around the house. You don't need to be scared."
        scene 129_s77 with dissolve
        yasmine "I heard him talking, but I mean you. I want {i}you{/i} to stay."
        scene 129_s78 with dissolve
        mc "*chuckles* I see. Well, I {i}am{/i} staying. The guard commander told me to stay inside—just as an extra safety measure."
        scene 129_s79 with dissolve
        yasmine "*laughs* Wonderful! I feel a lot safer already!"
        scene 129_s80 with dissolve

        if mc_killed_vic:
            yasmine "*sniff* *gag* This awful smell of blood is going to haunt me for weeks... Sit still while I clean up a little more."
            yasmine "These men sure can hold a sword, but are awful when it comes to domestic tasks."
        else:
            yasmine "Sit still while I clean up a little more. Those awful men were taking food from the pantry like it was their own house."
            yasmine "They knocked all the pots too."

        if mc_karma >= 5:
            scene 129_s74 with Dissolve(1.0)
            mc "I'll help you out"
            scene 129_s73 with dissolve
            yasmine "Aww, [mc], please. You have already done enough."
            scene 129_s74 with dissolve
            mc "Clearly not. Those guards don't know shit about cleaning."
            scene 129_s73 with dissolve
            yasmine "*chuckles* Very well~"
            scene 129_s74 with dissolve
        else:
            scene 129_s74 with Dissolve(1.0)
            mc "Could you make me some tea while you're at it?"
            scene 129_s73 with dissolve
            yasmine "Oh, of course! It's the least I can do for you."
            scene 129_s74 with dissolve
    else:
        jump scene131_2

    scene 129_s81 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/door.mp3"
    reham "*yawn* I'm going to bed, Mother. It's been... a very long day. Need anything before I turn in?"
    scene 129_s82 with dissolve
    yasmine "No, dear. I'm fine. How is Maia?"
    scene 129_s81 with dissolve
    reham "She slept not too long after I talked to her. I tried to get her to talk about it, but she just... closed off."
    scene 129_s82 with dissolve
    yasmine "I see. It won't be easy like that. Some wounds take time to heal. Perhaps you, [mc], can talk to her tomorrow?"
    mc "Yeah. I'll try."
    scene 129_s81 with dissolve
    reham "Goodnight, Mother. Goodnight, [mc]."
    scene 129_s82 with dissolve
    mc "Night."
    scene 129_s83 with Dissolve(2.0)
    mc "..."
    yasmine "What are you thinking about?"
    scene 129_s85 with Dissolve(1.0)
    mc "Hm? Nothing in particular."
    mc "(Is it me, or is her blouse looser than before? She's a lot closer too.)"
    mc "What's on {i}your{/i} mind? You've been staring at me nonstop."
    scene 129_s86 with dissolve
    yasmine "Have I?! Oh, forgive me... I didn't mean to stare. I was just... just lost in thought too."
    yasmine "*chuckles* I guess I... umm... feel a little lonely."
    scene 129_s87 with Dissolve(1.0)
    perception "Her hand rests on the table. Then, after a moment's hesitation, it moves towards you."
    mc "..."
    call screen scene129_choice03 with dissolve

label scene129_choice03_op1:
    $ mc_rejected_yasmine = True
    scene 129_s150 with Dissolve(1.0)
    yasmine "..."
    empathy "She doesn't say anything, but her expression changes. The warmth fades. The hopeful light in her eyes dims."
    scene 129_s88 with dissolve
    yasmine "*ahem* It's going to be a long night. The guards are outside, but I doubt I'll sleep much."
    yasmine "Every time I close my eyes, I see those men at my table."
    scene 129_s89 with dissolve
    mc "Go ahead, Yasmine. I can stay awake if you don't trust the guards."
    scene 129_s88 with dissolve
    yasmine "Are you certain? Not sleeping can take a toll on your health. You must be exhausted."
    scene 129_s89 with dissolve
    mc "I'm used to it at this point. Don't worry about me."
    scene 129_s88 with dissolve
    yasmine "I see... Thank you. For all you have done."
    play sound "sound_effects/doors/door_open5.mp3"
    scene 129_s109 with vpunch
    rohan "Darling?! I'm back! I-I saw the guards outside—they let me through when I told them I lived here—D-Did something happen? Is everyone alright? Are the girls—"
    scene 129_s110 with dissolve
    yasmine "You— Where the HELL were you?!"
    scene 129_s109 with dissolve
    rohan "Darling, I can explain! There was a situation at the market with a friend! I had to help him out. I didn't know there was trouble here—"
    scene 129_s110 with dissolve
    yasmine "Don't start with that! I already saw you when you glanced through the window."
    scene 129_s109 with dissolve
    rohan "Huh?! N-No! You're mistaking me for someone else... Th-that wasn't me... I was across town, I swear!"
    scene 129_s112 with Dissolve(1.0)
    rohan "I'm sorry... I really would have helped if I had known."
    scene 129_s111 with dissolve
    yasmine "*scoff* You left your daughter in a house full of armed men, and you didn't even shout for help."
    scene 129_s112 with vpunch
    rohan "S-Shut the hell up! Don't you dare talk to me like that, woman! Know your damn place!"
    rohan "Did you forget who brings in the food on your table? Who owns this house?! You'd be living in a fucking sewer without me!"
    scene 129_s112 with vpunch
    rohan "And why is the house all a mess?! I don't go to work all day to come back to a shithole!"
    scene 129_s113 with Dissolve(1.0)
    yasmine "*sigh* ...I-I'm too tired to argue right now. I can't. I don't have anything left."
    perception "Her anger is visible all over her body, she doesn't look at Rohan as she enters the bedroom."
    scene 129_s152 with Fade(0.5,0.5,0.5)
    mc "..."
    scene 129_s114 with dissolve
    rohan "What are you looking at?"
    scene 129_s115 with dissolve
    mc "Nothing. I'm looking at nothing."
    scene 129_s114 with dissolve
    rohan "Hmph. Don't you have somewhere to be? The palace, maybe? The guards said you were important."
    rohan "And why were you sitting with my wife alone in the middle of the night?"
    scene 129_s115 with dissolve
    if mc_karma >= 5:
        mc "She was scared, so I gave her company. That's all."
        scene 129_s114 with dissolve
        rohan "That so? At night? Why not in the morning? Why not when there were other people around?"
        scene 129_s115 with dissolve
        mc "*sigh* Drop it, Rohan. We just talked about... groceries."
        scene 129_s114 with dissolve
        rohan "Aha, I see. Well... if you're helping us with it, I understand. Supplies are tight. The debts are... well, you know."
        rohan "I'm not a bad man, you know. I just... I make bad choices."
        scene 129_s152 with dissolve
    else:
        mc "Shut the fuck up. I don't want to hear your voice at all."
        scene 129_s114 with dissolve
        rohan "W-What did you just say to me?"
        scene 129_s115 with dissolve
        mc "You heard me. Now zip it."
        scene 129_s152 with dissolve
        rohan "..."
    jump scene129_5

label scene129_choice03_op2:
    scene 129_s90 with Dissolve(1.0)
    sensation "Your hands entwine in a soft, gentle caress. Her skin is warm. Her pulse is quick, fluttering against your palm."
    stop music fadeout 1.0
    scene 129_s91 with vpunch
    yasmine "Hah—!"
    play music "hope/yasmine.mp3" fadein 3.0 loop
    scene 129_s92 with Dissolve(1.0)
    yasmine "I'm so sorry, [mc]! I don't know what came over me... That was inappropriate."
    scene 129_s93 with dissolve
    mc "What are you saying? We just held hands."
    scene 129_s92 with dissolve
    yasmine "*sigh* I'm a married woman, [mc]. By contract. By the vows I spoke in front of our Gods. We can't hold hands... not like that. Not the way I-I wanted you to."
    scene 129_s93 with dissolve
    mc "You're really too harsh on yourself. Has anyone ever told you that?"
    scene 129_s92 with dissolve
    yasmine "What?"
    scene 129_s93 with dissolve
    mc "Let go a little. Whatever relationship you have with Rohan, I wouldn't call it a 'marriage'. Not anymore."
    scene 129_s92 with dissolve
    yasmine "I get what you're trying to say, but still. I {i}am{/i} married. And this would be considered... {size=40}cheating{/size}."
    scene 129_s93 with dissolve
    mc "Who said we're doing anything that strong? We're just holding hands. We're comforting each other."
    yasmine "..."
    scene 129_s94 with Dissolve(1.0)
    sensation "She pulls her hand closer—slowly. Her fingers brush against yours. Then they intertwine again."
    mc "See? It isn't too bad. The Gods didn't strike us down."
    scene 129_s95 with dissolve
    yasmine "*chuckles* I guess so."
    yasmine "My... your metal hand feels cold, but also... warm? It's weird."
    scene 129_s94 with dissolve
    mc "You don't want to ask about it?"
    scene 129_s95 with dissolve
    yasmine "Reham told me. I didn't want to be rude and ask. But, it feels strong. Is this strength because of the hand, or because of you?"
    scene 129_s94 with dissolve
    mc "Some of it. I also used to train my muscles, back when... it's been a while."
    scene 129_s95 with dissolve
    yasmine "*chuckles* I can tell, your muscles are quite defined. I can see them through your clothes."
    scene 129_s94 with dissolve
    mc "Thank you."
    mc "You know, you're remarkably calm right now."
    scene 129_s95 with dissolve
    yasmine "Well... I may have added a little something to the tea when you weren't looking."
    scene 129_s94 with dissolve
    mc "You drugged my tea?!"
    scene 129_s96 with dissolve
    yasmine "Not yours! Mine! Just a little bit of mead to steady the nerves."
    scene 129_s97 with dissolve
    mc "*chuckles* Fair enough."
    scene 129_s99 with dissolve
    yasmine "Mhm~"
    call screen scene129_choice04 with dissolve

label scene129_choice04_op1:
    $ yasmine_love += 10
    mc "..."
    scene 129_s98 with dissolve
    yasmine "[mc]?"
    scene 129_s99 with dissolve
    mc "He really doesn't desereve you."
    mc "Seriously, how the hell did he manage to marry you? You belong in a palace, adorned with gold. While he... I don't know, in a sewer?"
    scene 129_s151 with dissolve
    yasmine "*chuckles* S-Stop it... you'll make me embarrassed... I'm an old married woman, I'm not supposed to blush like a girl at her first dance."
    scene 129_s100 with dissolve
    mc "You're not old. I didn't even know you were a mother when I first saw you."
    scene 129_s151 with dissolve
    yasmine "Who taught you to talk like that? Did they also teach you to flirt with defenseless women in their own kitchens?"
    scene 129_s100 with dissolve
    mc "Defenseless? You? The woman who stood her ground against three bandits and told them she'd rather die than be sold?"
    mc "You're many things, Yasmine. Defenseless isn't one of them."
    jump scene129_4

label scene129_choice04_op2:
    $ yasmine_love += 20
    mc "You look stunning tonight. The way your eyes shine in the candlelight... you're breathtaking."
    scene 129_s151 with dissolve
    yasmine "Oh..."
    yasmine "S-Sorry. I... I don't know what to say. No one's said anything like that to me in years."
    yasmine "Rohan used to, before... I didn't realize how much I missed it."
    scene 129_s100 with dissolve
    mc "Then he was a fool to stop. And you deserve to hear it again. Every day, from someone who means it."
    scene 129_s151 with dissolve
    yasmine "Stop it... You're going to make me cry."
    scene 129_s100 with dissolve
    mc "*chuckles* Alright, alright."
    jump scene129_4

label scene129_choice04_op3:
    $ yasmine_love -= 30
    $ mc_scared_yasmine = True
    mc "Want me to touch something else?"
    scene 129_s98 with dissolve
    yasmine "What?"
    scene 129_s99 with dissolve
    mc "I mean, my hands are already here. It wouldn't take much to—"
    scene 129_s102 with dissolve
    stop music fadeout 3.0
    yasmine "No. No, I... I think I should go to bed."
    yasmine "I appreciate everything you've done for me. Truly. But I'm not... I'm not that kind of woman."
    scene 129_s101 with Dissolve(1.0)
    mc "Yasmine, I didn't mean—"
    yasmine "I know what you meant. And I'm not angry, just... forget it."
    yasmine "Goodnight, [mc]. Please don't tell my husband about us... holding hands."
    mc "..."
    jump scene129_4

label scene129_4:
    if not mc_scared_yasmine and not mc_rejected_yasmine:
        scene 129_s102 with dissolve
        yasmine "This is dangerous, you know. Being here. W-With you. Like this."
        scene 129_s153 with dissolve
        mc "Dangerous how?"
        scene 129_s102 with dissolve
        yasmine "I haven't felt... anything for so long. I buried it all. The desire to be touched by someone who actually sees me."
        yasmine "I told myself I didn't need it, that surviving was enough. And now you're here, and you're holding my hand, a-and you're looking at me like I'm something precious..."
        yasmine "I don't know what to do with any of this. I've forgotten how to be... wanted."
        scene 129_s153 with dissolve
        mc "You haven't forgotten. You're just scared."
        mc "I don't want to hurt you, but I really want to make you feel wanted—if you let me."
        scene 129_s102 with dissolve
        yasmine "Let you? You're asking for permission?"
        scene 129_s153 with dissolve
        mc "Yes. I'm not Rohan. You've had enough of men making decisions for you. This one is yours."
        scene 129_s102 with dissolve
        yasmine "Please, don't compare yourself to him."
        yasmine "...You're not like him at all. When things got hard, you stayed. When I was in danger, you fought. When I needed someone... {i}you{/i} were here."
        scene 129_s153 with dissolve
        perception "The candlelight catches the silver in her hair, the lines around her eyes, the soft curve of her lips."
        scene 129_s102 with dissolve
        yasmine "I don't know what this is, I don't know what it could become. I just know that when I'm with you, I feel safe."
        yasmine "I feel like a woman. With desires and dreams and a heart that still beats, despite everything."
        yasmine "Wh-What are we doing, [mc]? What is this?"
        scene 129_s153 with dissolve
        call screen scene129_choice05 with dissolve
    else:
        scene 129_s109 with Fade(1.0,1.0,1.0)
        play sound "sound_effects/doors/door_open5.mp3"        
        play music "night.mp3" fadein 2.0 volume 0.4 loop
        rohan "Darling?! I'm back! I-I saw the— Huh? Is she not here?"
        rohan "What's with the guards outside?"
        scene 129_s110 with dissolve
        mc "There was an issue. You don't have to concern yourself with it."
        scene 129_s109 with dissolve
        rohan "*sigh* Good. My headache is strong as is. I'm glad she's sleeping right now, I don't want to have that argument yet."
        scene 129_s110 with dissolve
        scene 129_s114 with Dissolve(2.0)
        rohan "Are you staying up all night?"
        scene 129_s115 with dissolve
        mc "Yes."
        scene 129_s114 with dissolve
        rohan "If it means you won't enter the bedroom then by all means. Stay up."
        scene 129_s152 with dissolve
        mc "..."
        scene 129_s114 with dissolve
        rohan "Well, I'm too tired to even look at someone, you know... work has tired me out completely."
        scene 129_s115 with dissolve
        mc "Right."
        scene 129_s114 with dissolve
        rohan "*ahem* I'm off to bed. Don't touch anything."
        scene 129_s152 with dissolve
        jump scene129_5

label scene129_choice05_op1:
    $ mc_kiss_yasmine = True
    scene 129_s105 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    sensation "You stand up, lean forward, and press your lips to hers. The kiss is soft at first—"
    scene 129_s106 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss5.mp3" 
    sensation "—Then she leans in, and takes you fiercely in a hungry kiss. Her hands grip your hair, pulling you deeper into her mouth."
    scene 129_s108 with Dissolve(1.0)
    yasmine "Hahh... I... I haven't been kissed like that in... I don't even remember."
    scene 129_s107 with dissolve
    mc "Then it's been too long. You deserve to be kissed like that every day."
    scene 129_s108 with dissolve
    yasmine "*laughs* You're going to spoil me... You're going to make me forget that I'm a married woman."
    scene 129_s107 with dissolve
    mc "The marriage is already broken. You didn't break it, he did."
    scene 129_s108 with dissolve
    yasmine "This feeling... Oh, Gods... I haven't felt it in years."
    scene 129_s107 with dissolve
    mc "*chuckles* You mean that feeling down there? The ache?"
    scene 129_s108 with dissolve
    yasmine "Yes! Don't make me say it out loud, but yes. I didn't even know I was capable of it anymore. I thought it was just age taking its toll."
    scene 129_s107 with dissolve
    mc "It wasn't age. It was because you didn't have someone you truly wanted."
    scene 129_s108 with dissolve
    yasmine "Should... should we? Here? Now? But... quietly. Reham and Maia are asleep."
    yasmine "Just for a few minutes. No one will bother u—"
    stop music
    play sound "sound_effects/doors/door_open5.mp3"
    scene 129_s109 with vpunch
    play music "night.mp3" fadein 1.0 volume 0.4 loop
    rohan "Darling?! I'm back! I-I saw the guards outside—they let me through when I told them I lived here—D-Did something happen? Is everyone alright? Are the girls—"
    scene 129_s110 with dissolve
    yasmine "You— Where the HELL were you?!"
    scene 129_s109 with dissolve
    rohan "Darling, I can explain! There was a situation at the market with a friend! I had to help him out. I didn't know there was trouble here—"
    scene 129_s110 with dissolve
    yasmine "Don't start with that! I already saw you when you glanced through the window."
    scene 129_s109 with dissolve
    rohan "Huh?! N-No! You're mistaking me for someone else... Th-that wasn't me... I was across town, I swear!"
    scene 129_s112 with dissolve
    rohan "I'm sorry... I really would have helped if I had known."
    scene 129_s111 with dissolve
    yasmine "*scoff* You left your daughter in a house full of armed men, and you didn't even shout for help."
    scene 129_s112 with vpunch
    rohan "S-Shut the hell up! Don't you dare talk to me like that, woman! Know your damn place!"
    rohan "Did you forget who brings in the food on your table? Who owns this house?! You'd be living in a fucking sewer without me!"
    scene 129_s112 with vpunch
    rohan "And why is the house all a mess?! I don't go to work all day to come back to a shithole!"
    scene 129_s113 with Dissolve(1.0)
    yasmine "*sigh* ...I-I'm too tired to argue right now. I can't. I don't have anything left."
    yasmine "{size=30}I'm sorry, [mc]... I-I need to go to the bedroom. I can't... I can't do this right now. Not with him here.{/size}"
    perception "Her anger is visible all over her body, she doesn't look at Rohan as she enters the bedroom."
    scene 129_s152 with Fade(0.5,0.5,0.5)
    mc "..."
    scene 129_s114 with dissolve
    rohan "What are you looking at?"
    scene 129_s115 with dissolve
    mc "Nothing. I'm looking at nothing."
    scene 129_s114 with dissolve
    rohan "Hmph. Don't you have somewhere to be? The palace, maybe? The guards said you were important."
    rohan "And why were you sitting with my wife alone in the middle of the night? Like a pair of—"
    rohan "Were you... hugging her?! Tell me you weren't hugging her! Because if you did, there will be a punishment for her tomorrow."
    rohan "I swear it. I'll make her regret it. I'll make you both regret it."
    scene 129_s115 with dissolve
    if mc_karma >= 5:
        mc "She was scared, so I gave her company. That's all."
        scene 129_s114 with dissolve
        rohan "That so? At night? Why not in the morning? Why not when there were other people around?"
        scene 129_s115 with dissolve
        mc "*sigh* Drop it, Rohan. We just talked about... groceries."
        scene 129_s114 with dissolve
        rohan "Aha, I see. Well... if you're helping us with it, I understand. Supplies are tight. The debts are... well, you know."
        rohan "I'm not a bad man, you know. I just... I make bad choices."
        scene 129_s152 with dissolve
    else:
        mc "Shut the fuck up. I don't want to hear your voice at all."
        scene 129_s114 with dissolve
        rohan "W-What did you just say to me?"
        scene 129_s115 with dissolve
        mc "You heard me. Now zip it."
        scene 129_s152 with dissolve
        rohan "..."
    jump scene129_5

label scene129_choice05_op2:
    $ mc_rejected_yasmine = True
    mc "I just wanted to comfort you."
    scene 129_s103 with Dissolve(1.0)
    yasmine "Oh."
    scene 129_s104 with dissolve
    mc "Yasmine... I care about you, but I can't be what you need right now. You're vulnerable. If I let myself fall into this, I'd be taking advantage of you."
    scene 129_s103 with dissolve
    yasmine "*sigh* I already knew that. You didn't have to prove it by letting me go."
    scene 129_s104 with dissolve
    mc "I'm not letting you go. I'm just... not taking this further. My intention was to comfort you, nothing more."
    mc "You deserve someone who can give you their whole heart."
    scene 129_s103 with dissolve
    yasmine "And you deserve someone who isn't still tangled in the wreckage of a failed marriage. I understand."
    scene 129_s104 with dissolve
    mc "I'm glad you do."
    scene 129_s103 with dissolve
    yasmine "But tonight... tonight I'm going to sleep, and I'm going to dream of a world where things turned out differently."
    yasmine "Where you and I met, instead of him."
    scene 129_s104 with dissolve
    mc "..."
    mc "Goodnight, Yasmine."
    scene 129_s103 with dissolve
    yasmine "Goodnight, [mc]. Come over to the bedroom when you're ready. As I said before, I have a warm mattress ready for you."
    scene 129_s104 with dissolve
    stop music fadeout 1.0
    stop music fadeout 1.0
    stop music fadeout 1.0
    jump scene129_4

label scene129_5:
    if mc_squeeze_reham:
        $ reham_love -= 10
    else:
        $ reham_love += 10
    if mc_harem_reham:
        $ reham_love += 20
    if mc_harem_reham_dom_dom:
        $ reham_love += 10
    if mc_princess_reham:
        $ reham_love += 10
    if mc_gave_sword_reham:
        $ reham_love += 10
    if mc_inspected_reham:
        $ reham_love -= 10
    if mc_talked_reham:
        $ reham_love += 10
    if reham_pregnant:
        $ reham_love += 20
    stop music fadeout 1.0
    scene 129_s116 with Fade(1.3,1.0,1.3)
    play music "kitchen.mp3" fadein 1.0 loop
    mc "..."
    mc "(I always hated this silence. It's so fucking loud. But... there used to be someone who filled it without trying.)"
    if mc_harem_reham:
        reham "[mc]? I-I mean, Master? Umm... I hope you don't mind me saying your name while in our house. It's less awkward that way."
        reham "*giggles* I don't want to imagine the look on my father's face if I call you 'master' infront of him."
    else:
        reham "[mc]?"
    scene 129_s148 with Dissolve(1.0)
    mc "(Oh right. It was Reham. I'm hearing her voice. Is this a sign?)"
    mc "(The way she speaks... How she never raises her voice, even when she's angry. How she always seems to know when I'm drowning in my own head.)"
    mc "(She's been there this whole time and I never really noticed.)"
    mc "(Why do I feel sad all of a sudden? Is... is it because she might leave eventually? Can I really let her leave like that?)"
    scene 129_s117 with Dissolve(1.0)
    reham "[mc]? Are you alright?"
    scene 129_s118 with dissolve
    mc "Oh, Reham... Y-You're actually here."
    scene 129_s117 with dissolve
    reham "Yes? Is something wrong?"
    scene 129_s118 with dissolve
    mc "No. Just... thinking."
    scene 129_s117 with dissolve
    reham "About what?"
    scene 129_s118 with dissolve
    mc "Everything. About... about how lucky I am to have you around."
    scene 129_s117 with dissolve
    reham "...Oh. Thank you."
    scene 129_s118 with dissolve
    mc "You're welcome. Good morning."
    scene 129_s117 with dissolve
    reham "Morning to you too."
    reham "*ahem* Notice... something new?"
    scene 129_s118 with dissolve
    mc "Huh?"
    scene 129_s120 with dissolve
    reham "Look at me."
    scene 129_s119 with dissolve
    mc "Umm..."
    call screen scene129_choice06 with dissolve

label scene129_choice06_op1:    
    mc "You did your hair?"
    scene 129_s121 with dissolve
    reham "No! I mean... kind of? I just combed it a little."
    reham "Is that all you notice?"
    scene 129_s122 with dissolve
    mc "Yeah. It looks nice."
    scene 129_s121 with dissolve
    reham "*sigh* It's the makeup! Can't you see my eyes?"
    scene 129_s122 with dissolve
    mc "Oh, I see now."
    scene 129_s121 with dissolve
    reham "*chuckles* men."
    scene 129_s122 with dissolve
    mc "I'm sorry, I'm not good at this."
    scene 129_s121 with dissolve
    reham "No, you're not. But at least you noticed something."
    scene 129_s122 with dissolve
    jump scene129_6

label scene129_choice06_op2:
    mc "Are you wearing a new dress?"
    scene 129_s121 with dissolve
    reham "No need to rub it in, [mc]. I know I've been wearing the same dress since we met at the hideout."
    scene 129_s122 with dissolve
    mc "No, I didn't mean it like that—"
    scene 129_s121 with dissolve
    reham "*sigh* It's fine. It's the makeup. Can't you see my eyes?"
    scene 129_s122 with dissolve
    mc "Oh. Yes, now I see. They look..."
    scene 129_s121 with dissolve
    reham "They look what?"
    scene 129_s122 with dissolve
    mc "...Different?"
    scene 129_s121 with dissolve
    reham "*chuckles* men."
    scene 129_s122 with dissolve
    jump scene129_6

label scene129_choice06_op3:
    $ mc_guessed_reham_correct = True
    $ reham_love += 10
    mc "Is it your makeup? Around your eyes."
    scene 129_s120 with dissolve
    reham "Yes. *giggles* I'm so glad you noticed."
    reham "You didn't notice the last time I did it, back at the hideout. I was hoping you would now."
    scene 129_s119 with dissolve
    mc "I was blind before. Now I can see your beauty. Makeup or not."
    scene 129_s120 with dissolve
    reham "[mc]..."
    scene 129_s119 with dissolve
    mc "It looks beautiful, Reham."
    scene 129_s120 with dissolve
    reham "*giggles* Oh you~"
    scene 129_s119 with dissolve
    jump scene129_6

label scene129_choice06_op4:
    mc "You look tired."
    scene 129_s121 with dissolve
    reham "I... what?"
    scene 129_s122 with dissolve
    mc "There are shadows under your eyes. Did you sleep badly?"
    scene 129_s121 with dissolve
    reham "...I spent almost an hour on this."
    scene 129_s122 with dissolve
    mc "On what?"
    scene 129_s121 with dissolve
    reham "The makeup. Around my eyes."
    scene 129_s122 with dissolve
    mc "Oh... I thought those were... nevermind."
    scene 129_s121 with dissolve
    reham "*sigh* Men."
    scene 129_s122 with dissolve
    jump scene129_6

label scene129_6:
    if mc_guessed_reham_correct and mc_harem_reham:
        scene 129_s123 with Dissolve(1.0)
        play sound "se_sfx/blowjob/kiss2.mp3" 
        reham "*mwah* So, how is my strong, brave master doing?"
    scene 129_s124 with Dissolve(1.0)
    reham "Your body must be aching after sleeping in that chair all night. Why don't you go inside and rest a little longer?"
    reham "You can use my bed. I don't mind."
    scene 129_s125 with dissolve
    mc "*yawn* No point trying to go back to sleep now. The sun's up."
    mc "Where's Maia and your parents?"
    scene 129_s124 with dissolve
    reham "Everyone is still asleep. Mother went to bed late—I heard her moving around after Father came home."
    reham "And Maia... she's been asleep since I talked to her last night. I think her body just... shut down."
    reham "It's just us for now."
    if mc_killed_vic:
        scene 129_s126 with dissolve
        reham "*sniff* Ugh... I'll talk to father about moving houses as soon as he wakes up. The smell of blood will linger forever."
    scene 129_s125 with Dissolve(1.0)
    mc "..."
    scene 129_s127 with dissolve
    reham "What's wrong, [mc]? If you're hungry, don't be shy. Our home is yours too."
    reham "Or would you like me to make you a sandwitch? *giggles* I make a pretty good fig jam sandwitch."
    scene 129_s125 with dissolve
    call screen scene129_choice07 with dissolve

label scene129_choice07_op1:
    mc "Did I ever mention how important you are to me?"
    mc "Because I'll blame myself for the rest of my life if I never said it out loud."
    scene 129_s127 with dissolve
    reham "Huh? Are you flirting with me, [mc]?"
    scene 129_s128 with dissolve
    mc "What if I am?"
    scene 129_s127 with dissolve
    reham "Well... it would be strange, for starters. I'm not exactly in the servant business for romance."
    scene 129_s128 with dissolve
    mc "That's exactly what's wrong with it. You spend all your time looking after everyone else. You should get to feel wanted too."
    scene 129_s127 with dissolve
    reham "...Wanted?"
    scene 129_s130 with dissolve
    reham "*sigh* You're erect, [mc]. Don't pretend this is only about my feelings."
    scene 129_s129 with dissolve
    mc "*chuckles* You can see that?"
    scene 129_s130 with dissolve
    reham "It's not exactly easy to ignore that tent in your pants."
    scene 129_s129 with dissolve
    mc "But it's not just the morning wood talking. You make this place feel like a home even when everything outside is falling apart, always did."
    scene 129_s128 with dissolve
    mc "Back at the hideout, on the road, here in this little house. You're the one who holds things together."
    reham "..."
    scene 129_s127 with dissolve
    reham "You really know how to put someone on the spot, don't you?"
    scene 129_s128 with dissolve
    mc "Only when it's someone worth putting on the spot."
    scene 129_s127 with dissolve
    reham "Hmph. Flatterer."
    if mc_harem_reham_dom or mc_harem_reham_dom_dom:
        scene 129_s131 with dissolve
        reham "You know you don't have to do this, right? Just command me, and I'll follow. I'm your servant, after all."
        scene 129_s132 with dissolve
        mc "I don't need you to be my servant right now. I just... want to be close to you. Actually close."
        mc "I feel like I ignored you for too long. The real you."
        scene 129_s131 with dissolve
        reham "W-What exactly are you asking for, [mc]? You're giving me so many conflicting feelings..."
        scene 129_s132 with dissolve
        call screen scene129_choice08 with dissolve
    elif mc_harem_reham:
        scene 129_s131 with dissolve
        reham "If this is about helping you with... that, then fine. Even if our agreement never included anything sexual, you earned it."
        scene 129_s132 with dissolve
        mc "Forget the agreement. I don't want this to feel like business."
        mc "I want us to actually feel each other. No roles or obligations."
        scene 129_s131 with dissolve
        reham "W-What exactly are you asking for, [mc]? You're giving me so many conflicting feelings..."
        scene 129_s132 with dissolve
        call screen scene129_choice08 with dissolve
    else:
        mc "I—"
        scene 129_s131 with dissolve
        reham "That's enough, [mc]. I don't want to risk what we already have."
        scene 129_s132 with dissolve
        mc "I want us to be more than friends, Reham."
        scene 129_s131 with dissolve
        reham "Please don't say that right now..."
        scene 129_s132 with dissolve
        mc "..."
        scene 129_s131 with dissolve
        reham "I'm sorry. It isn't you. I'm just... not ready for that. Not with everything still so uncertain."
        scene 129_s132 with dissolve
        mc "Alright. I understand."
        jump scene131

label scene129_choice08_op2:
    mc "Reham..."
    scene 129_s133 with Dissolve(1.0)
    mc "You're the one who kept everything from falling apart. The meals you cooked, the quiet encouragement when I was at my worst..."
    mc "You pulled me back together when I thought I'd lost everything. There's no way I'm letting someone like that walk out of my life."
    reham "..."
    mc "I've been terrified that in the end you'd choose to stay with your parents, and that thought has been eating at me."
    mc "I like you, Reham. And I want you to stay with me."
    if reham_love >= 50:
        $ mc_harem_reham_true = True
        stop music fadeout 1.0
        scene 129_s134 with dissolve
        reham "You have no idea how long I've waited to hear something like that."
        play music "reham.mp3" fadein 2.0 loop
        scene 129_s133 with dissolve
        mc "R-Really?"
        scene 129_s134 with dissolve
        reham "To tell you the truth, [mc]... I've been pretending to be the sensible one this whole time. Inside I was scared and lonely."
        reham "It was only because of you that I managed to keep the act going."
        scene 129_s133 with dissolve
        mc "*chuckles* Looks like we needed each other more than we admitted."
        scene 129_s134 with dissolve
        reham "We did. I want a man who will actually be there for me. And so far... that man has been you. Every single time."
        reham "The thought of losing that was killing me too."
        scene 129_s133 with dissolve
        scene 129_s135 with Dissolve(2.0)
        perception "You hold out your hand, leading her to yourself. After a brief hesitation, Reham takes it. Her fingers are slightly trembling."
        scene 129_s136 with Dissolve(1.5)
        play sound "se_sfx/blowjob/kiss3.mp3" 
        empathy "The kiss is slow at first, then deeper. Whatever paper agreement existed between you quietly dissolves. This is real now."
        scene 129_s138 with Dissolve(1.0)
        reham "*giggles* I hope Maia doesn't mind sharing her man. So is the princess."
        scene 129_s137 with dissolve
        if mc_reb_breakup_final:
            mc "I'm not dating the princess anymore. We broke up a while ago."
        else:
            mc "The princess is fine with it. I just have to tell her about it later."

        if mc_maia_left_twice or mc_maia_left:
            mc "And me and Maia... well, we aren't together."
        else:
            if mc_slept_maia_reham_106:
                mc "Also you and Maia already shared me before."
                scene 129_s138 with dissolve
                reham "Yes, but that took quite a bit of convincing."
                scene 129_s137 with dissolve
                mc "She'll be fine. She'll understand how integral your to my life."
            else:
                scene 129_s137 with dissolve
                mc "And Maia... She'll understand how integral your to my life."

        reham "Mhmm~"
        scene 129_s138 with dissolve
        reham "Can you take me? Just for a while. I don't care if my parents knew. In fact, I want them to know that their daughter finally has a man in her life."
        scene 129_s137 with dissolve
        call screen scene129_choice09 with dissolve
        mc "Let's do it. I wanna make love to you in your own kitchen."
        jump scene130_sex
    else:
        $ reham_rejected_mc = True
        scene 129_s131 with Dissolve(1.0)
        reham "That's enough, [mc]. I don't want to risk what we already have. I'm your servant and you're my master. That's all there is to it."
        scene 129_s132 with dissolve
        mc "I want us to be more than that, Reham."
        scene 129_s131 with dissolve
        reham "Please don't say that right now..."
        scene 129_s132 with dissolve
        mc "..."
        scene 129_s131 with dissolve
        reham "I'm sorry. It isn't you. I'm just... not ready for that. Not with everything still so uncertain."
        scene 129_s132 with dissolve
        mc "Alright. I understand. I won't push it further."
        jump scene131

label scene129_choice09_op2:
    mc "I'd rather not wake them up. Let them sleep a little longer."
    scene 129_s138 with dissolve
    reham "Hm? Who knew you cared so much about my parents."
    scene 129_s137 with dissolve
    mc "There's Maia too. She's been through a lot."
    scene 129_s138 with dissolve
    reham "When you say it like that... Alright. But you have to promise me a good time later~"
    scene 129_s137 with dissolve
    stop music fadeout 2.0
    mc "*chuckles* Promise."
    play music "kitchen.mp3" fadein 1.0 loop
    jump scene131
    
label scene129_choice08_op1:
    mc "I want you to help me with my erection, Reham."
    reham "..."
    scene 129_s127 with dissolve
    reham "That's it?! You said all those serious things... just so you could ask me to deal with your morning problem?"
    scene 129_s128 with dissolve
    mc "Well... yes. I was trying to get you in the right mood."
    scene 129_s127 with dissolve
    reham "*sigh* You succeeded. For about five seconds. Not anymore."
    reham "And why did you say it in that tone? 'I want you to help me with my erection, Reham' like you were reading wedding vows."
    scene 129_s128 with dissolve
    mc "*chuckles* I guess I was trying to be charming."
    scene 129_s127 with dissolve
    reham "Ugh. Fine. Let's just get this over with before my mother wakes up."
    reham "You should have started with the honest version."
    scene 129_s128 with dissolve
    mc "How do you want to help me?"
    scene 129_s127 with dissolve
    reham "I'll use my hands. It's the quietest option I can think of."
    scene 129_s128 with dissolve
    mc "Aww. Only hands?"
    scene 129_s127 with dissolve
    reham "I am not risking waking the entire household, [mc]. I don't know if I could stay quiet if you actually put it in me."
    scene 129_s128 with dissolve
    mc "Fine. But you have to take off your clothes. I want to see that beautiful body."
    jump scene130_hj

label scene129_choice07_op2:
    mc "Come sit on my lap."
    scene 129_s127 with dissolve
    reham "*laughs* What?"
    reham "You want me to act like your granddaughter all of a sudden?"
    scene 129_s128 with dissolve
    mc "Just... sit here for a moment."
    scene 129_s127 with dissolve
    reham "Umm... alright. If it will make you feel better."
    scene 129_s128 with dissolve
    scene 129_s140 with Dissolve(1.0)
    play sound "sound_effects/clothing_rustle2.mp3"
    sensation "She steps closer and gently lowers herself onto your lap. She leans back slightly, the loose strands of her hair brushing against your cheek and neck."
    mc "Ahhh..."
    scene 129_s139 with dissolve
    reham "You're making strange noises..."
    scene 129_s140 with dissolve
    mc "Fuck... You're so warm. Your hair smells good. And you're soft too..."
    scene 129_s141 with Dissolve(1.0)
    reham "Ah!"
    reham "I... I feel something pressing against me from below."
    perception "Your cock has hardened completely, the thick length pushing upward against the fabric of her dress, nestled right between her thighs."
    scene 129_s143 with Dissolve(1.0)
    reham "Don't tell me you're... This isn't as innocent as I first thought, is it?"
    reham "You're erect... while I'm sitting on you."
    scene 129_s142 with dissolve
    call screen scene129_choice10 with dissolve

label scene129_choice10_op1:
    mc "I'll be honest. I've got a serious problem down here that doesn't look like it's going away on its own."
    mc "And it's because of you."
    scene 129_s139 with dissolve
    reham "M-Me? It was already like that before I even sat down, grandpa..."
    scene 129_s140 with dissolve
    mc "That just proves how fucking hot you are. The second you put your weight on me it got even worse."
    reham "..."

    if mc_harem_reham_dom or mc_harem_reham_dom_dom:
        scene 129_s143 with dissolve
        reham "*sigh* Fine. I'm your servant. I can't exactly refuse even something like this."
        reham "But we have to be quick. Before my mother wakes up."
        scene 129_s142 with dissolve
        mc "Fine. God, you're so warm..."
        mc "What do you want to do to me?"
        scene 129_s143 with dissolve
        reham "I'll use my hands. It's the quietest option I can think of."
        scene 129_s142 with dissolve
        mc "Aww. Only hands?"
        scene 129_s143 with dissolve
        reham "I am not risking waking the entire household, [mc]. I don't know if I could stay quiet if you actually put it in me."
        scene 129_s142 with dissolve
        mc "Fine. But you have to take off your clothes. I want to see that beautiful body."
        jump scene130_hj

    elif mc_harem_reham:
        if mc_slept_maia_reham_106:
            scene 129_s143 with dissolve
            reham "Didn't I already take care of you before? With Maia right there with us, no less."
            reham "You had two of us pleasuring you at the same time. Was that not enough?"
            scene 129_s142 with dissolve
            mc "It was incredible, and I'm grateful. But that doesn't mean I stop wanting you forever."
            scene 129_s143 with dissolve
            reham "...Right. Fine."
            scene 129_s142 with dissolve
            mc "What do you want to do to me?"
            scene 129_s143 with dissolve
            reham "I'll use my hands. It's the quietest option I can think of."
            scene 129_s142 with dissolve
            mc "Aww. Only hands?"
            scene 129_s143 with dissolve
            reham "I am not risking waking the entire household, [mc]. I don't know if I could stay quiet if you actually put it in me."
            scene 129_s142 with dissolve
            mc "Fine. But you have to take off your clothes. I want to see that beautiful body."
            jump scene130_hj
        else:
            scene 129_s143 with dissolve
            reham "*sigh* Can't you just go to Maia? Aren't the two of you together?"
            scene 129_s142 with dissolve
            mc "She's not in any state for that right now. You know that."
            scene 129_s143 with dissolve
            reham "...You're right. I'm sorry."
            scene 129_s143 with dissolve
            reham "Just this once, [mc]. Alright?"
            scene 129_s142 with dissolve
            mc "Yes!"
            scene 129_s143 with dissolve
            reham "Good. Remember that. I'm your servant, not your personal... erection helper every time this happens."
            reham "I'll use my hands. It's the quietest option I can think of."
            scene 129_s142 with dissolve
            mc "Aww. Only hands?"
            scene 129_s143 with dissolve
            reham "I am not risking waking the entire household, [mc]. I don't know if I could stay quiet if you actually put it in me."
            scene 129_s142 with dissolve
            mc "Fine. But you have to take off your clothes. I want to see that beautiful body."
            jump scene130_hj
    else:
        scene 129_s143 with dissolve
        reham "W-We can't."
        reham "How can you even say something like that? We're not... together. And I'm not your servant either."
        scene 129_s142 with dissolve
        mc "I'm just being honest. Last night left me wound up tight. I need to let it out."
        mc "Would you be kind and help the man who saved you?"
        scene 129_s143 with dissolve
        reham "I'm sorry, [mc]. My answer is no..."
        reham "Don't misunderstand—I'm grateful you were there for us. Truly. But this is different."
        reham "I'll happily cook for you, make you drinks, whatever else you need. Just... not this. There's a public bath nearby. Go take care of it yourself."
        scene 129_s142 with dissolve
        mc "Alright, alright. I understand. Can I at least hug you for a little longer?"
        scene 129_s143 with dissolve
        reham "*sigh* ...Fine."
        scene 129_s142 with dissolve
        jump scene131

label scene129_choice10_op2:
    $ reham_love -= 30
    scene 129_s145 with dissolve
    sensation "You pull her in without thinking, arms wrapping tightly around her waist. The scent of her hair penetrates deeper into your senses."
    scene 129_s144 with dissolve
    reham "Mphm! You're hugging too tight!"
    scene 129_s145 with dissolve
    mc "Reham..."
    scene 129_s144 with dissolve
    reham "What's gotten into you? Are you alright?"
    scene 129_s145 with dissolve
    mc "Hnnn..."
    scene 129_s144 with dissolve
    reham "Let go!"
    scene 129_s146 with dissolve
    empathy "The sharp edge in her voice finally cuts through the haze. Your mind catches up with your body and you release her at once."
    scene 129_s147 with dissolve
    reham "What the hell was that, [mc]?"
    scene 129_s146 with dissolve
    mc "Fuck... I'm sorry, Reham. I just... had a really bad night."
    scene 129_s147 with dissolve
    reham "I can see that. Still, that's no excuse to grab me like that."
    scene 129_s146 with dissolve
    mc "I know. I'm sorry."
    scene 129_s147 with dissolve
    reham "*sigh* Go take care of that... problem of yours before someone else walks in and sees."
    scene 129_s146 with dissolve
    mc "You can't... you know. Help me with it?"
    scene 129_s147 with dissolve
    if mc_harem_reham:
        reham "I've lost my appetite for that kind of help right now, [mc]."
    else:
        reham "No! How can you even say something like that? We're not... together. And I'm not your servant either."
    reham "There's a public bath nearby. Handle it yourself."
    scene 129_s146 with dissolve
    jump scene131

label scene129_choice07_op3:
    mc "It's nothing."
    scene 129_s124 with dissolve
    reham "Alright. Then I'll make you something to eat."
    reham "It's about time you tried real food from our kitchen—not that thin sludge we used to call soup back in the hideout."
    scene 129_s125 with dissolve
    mc "*chuckles* Sounds good."
    scene 129_s124 with dissolve
    reham "Go wash your face and sit down. I'll have it ready soon."
    scene 129_s125 with dissolve
    jump scene131

image s130_vsex1 = Movie(play="images/chapter5/scene130/s130_vsex1.webm", loop=True)
image s130_vsex2 = Movie(play="images/chapter5/scene130/s130_vsex2.webm", loop=True)
image s130_vsex3 = Movie(play="images/chapter5/scene130/s130_vsex3.webm", loop=True)

image s130_asex1 = Movie(play="images/chapter5/scene130/s130_asex1.webm", loop=True)
image s130_asex2 = Movie(play="images/chapter5/scene130/s130_asex2.webm", loop=True)
image s130_asex3 = Movie(play="images/chapter5/scene130/s130_asex3.webm", loop=True)

label scene130_sex:
    stop music fadeout 2.0
    $ s130_sitting = True
    $ s130_POV1 = True

    if reham_pregnant:
        $ reham_pussy_virgin = False

    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_6_replay:
        $ persistent.chapter5_p7_6_replay = True

    $ mc_sexed_reham_130 = True

    scene 130_s1 with Fade(1.0,1.0,1.0)
    perception "She undresses quickly and settles onto your lap with her back against your chest. The moment she shifts, you feel an intense, wet heat pressing down against you—she's already ready."
    scene 130_s2 with dissolve
    reham "Hug me. Let me feel how much you want me."
    scene 130_s3 with Dissolve(1.3)
    mc "Mhmm... I can't stop breathing you in. You always smell so good."
    scene 130_s4 with dissolve
    reham "You actually like my scent?"
    scene 130_s3 with dissolve
    mc "I do."
    scene 130_s4 with dissolve
    reham "*giggles* Really? It might just be pheromones playing tricks on you. My mother always says otherwise."
    scene 130_s3 with dissolve
    mc "*sniff* Then your mother doesn't know what she's talking about."
    if not reham_anus_virgin and reham_pussy_virgin:
        $ s130_anal = True
        play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
        scene 130_s8 with Dissolve(1.0)
        sensation "She reaches down, presses the head of your cock against her anus, and carefully pushes back. The pressure is intense; her body resists at first, then slowly yields, gripping you even harder than your arms around her."
        mc "Woah! Reham? Your ass?!"
        reham "Gahh! Yes... that's where you took me last time, remember?"
        reham "In fact... it's the only place you've taken me so far."
        play sound "se_sfx/masturbate_female/3_masturbate3.mp3"
        scene 130_s6 with Dissolve(1.0)
        reham "I'm still a virgin. My hymen is still there... that part of me is untouched."
        scene 130_s7 with dissolve
        mc "I know... but you guiding me in yourself like this is going to make me lose it just from the thought."
        scene 130_s6 with dissolve
        reham "Huh?!"
        scene 130_s7 with dissolve
        mc "I actually made you enjoy taking it there! That's a real achievement!"
        scene 130_s6 with dissolve
        reham "Fhnmmm~! C-Calm down... it's not like I like it or anything..."
        reham "This is just for you... my lover— AGHH!"
        show s130_asex1 with dissolve
        mc "Ahh! Lover?! Don't say that right now or I really will finish early."
        reham "You'll break me if you keep thrusting that hard! Gahhnn~!"
        mc "*chuckles* I love hearing your cute moans, but won't you wake them up at this rate?"
        reham "Oh, my! Y-You're right... move slower."
        mc "Not a chance. Keep it quiet while I enjoy ruining your asshole."
    else:
        $ reham_pussy_virgin = False
        $ s130_vaginal = True
        play sound "se_sfx/masturbate_female/3_masturbate3.mp3"
        scene 130_s5 with Dissolve(1.3)
        sensation "She reaches down, guides your cock to her entrance, and slowly sinks onto you. Her walls close around you in a tight embrace."
        if reham_pussy_virgin:
            reham "Ahhn...! You're stretching me so wide! My hymen is breaking!"
        else:
            reham "Ahhn...! You're stretching me so wide!"
        mc "Fuck... this tightness is unreal."
        play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
        scene 130_s6 with Dissolve(1.0)
        reham "Calm down, [mc]... you'll tear me apart if you—ahh!"
        scene 130_s7 with dissolve
        mc "Hmm? I just touched something, didn't I?"
        scene 130_s6 with dissolve
        reham "Y-Yes... that's my cervix. It feels like I might lose control... like I need to pee..."
        scene 130_s7 with dissolve
        mc "We haven't even started moving yet."
        show s130_vsex1 with dissolve
        sensation "You begin to thrust in quick, deep strokes. Her walls grow slicker with every motion, coating you and letting you press even deeper."
        reham "Mhnnn~ It feels so good~"
        if mc_slept_maia_reham_106:
            mc "Better than last time with Maia?"
            reham "So much better... It's because of what you said earlier. The way you looked at me and meant every word..."
            reham "It made me want you even more... Fhnn~!"
        mc "*chuckles* I love those cute sounds you make... but you're going to wake someone if you keep going like that."
        reham "Oh! You're right... go slower."
        mc "Not happening. Keep your voice down while I ravage your pussy."
        reham "Ammh! You're so cruel... I can't stay quiet when I feel your tip kissing my cervix like that..."
    call screen s30_sex with dissolve

default s130_POV1 = False
default s130_POV2 = False

label s130_POV:
    if s130_POV1:
        $ s130_POV1 = False
        $ s130_POV2 = True
    else:
        $ s130_POV1 = True
        $ s130_POV2 = False

    if s130_vaginal:
        jump s130_standing_vaginal
    else:
        jump s130_standing_anal

label s130_position:
    if s130_standing:
        if s130_vaginal:
            jump s130_sitting_vaginal
        else:
            jump s130_sitting_anal
    else:
        if s130_vaginal:
            jump s130_standing_vaginal
        else:
            jump s130_standing_anal

default s130_standing_vaginal_1 = True
default s130_standing_vaginal_2 = False
default s130_sitting_vaginal_1 = True
default s130_sitting_vaginal_2 = False

label s130_standing_vaginal:
    $ s130_standing = True
    $ s130_sitting = False
    $ s130_anal = False
    $ s130_vaginal = True

    if s130_standing_vaginal_1:
        $ s130_standing_vaginal_1 = False
        $ s130_standing_vaginal_2 = True
        mc "Stand up. I want to take you properly—I don't feel like I'm going fast enough like this."
        reham "You want to go faster? [mc], you're already moving fast enough! I'll wake my parents if you go any harder!"
        mc "*laughs* Then you'll just have to try your best not to."
        if reham_pussy_virgin:
            $ reham_pussy_virgin = False
            $ s130_vaginal = True
            scene 130_s9 with Fade(1.0,1.0,1.0)
            perception "She leans forward against the edge of the table, presenting herself to you. Her pussy is flushed, glistening, and clearly wants you."
            reham "Ahhn...! You're stretching me so wide! My hymen is breaking! Y-You're taking my virginity, [mc]~!"
            mc "Fuck... this tightness is unreal."
            reham "Calm down, [mc]... you'll tear me apart if you—ahh!"
            play sound "se_sfx/masturbate_female/3_masturbate3.mp3"
            scene 130_s10 with Dissolve(1.0)
            mc "Hmm? I just touched something, didn't I?"
            reham "Y-Yes... that's my cervix. It feels like I might lose control... like I need to pee..."
            mc "We haven't even started moving yet."
            if s130_POV1:
                show s130_vsex2 with dissolve
            else:
                show s130_vsex3 with dissolve
            sensation "You begin to thrust in quick, deep strokes. Her walls grow slicker with every motion, coating you and letting you press even deeper."
            reham "Mhnnn~ It feels so good~"
            if mc_slept_maia_reham_106:
                mc "Better than last time with Maia?"
                reham "So much better... It's because of what you said earlier. The way you looked at me and meant every word..."
                reham "It made me want you even more... Fhnn~!"
            mc "*chuckles* I love those cute sounds you make... but you're going to wake someone if you keep going like that."
            reham "Oh! You're right... go slower."
            mc "Not happening. Keep your voice down while I ravage your pussy."
            reham "Ammh! You're so cruel... I can't stay quiet when I feel your tip kissing my cervix like that..."
        else:
            scene 130_s9 with Fade(1.0,1.0,1.0)
            perception "She leans forward against the edge of the table, presenting herself to you. Her pussy is flushed, glistening, and clearly wants you."
            mc "Mhnm!"
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 130_s10 with Dissolve(1.0)
            perception "You grip her hips and push back inside in one smooth, deep thrust."
            reham "Ahhn~! Gods! [mc]! [mc]! C-Calm down-Mhnnmmm~"
            if s130_POV1:
                show s130_vsex2 with dissolve
            else:
                show s130_vsex3 with dissolve
            mc "Don't hold back! Let me hear you. Moan louder!"
            reham "MPHHNNMMMM! Yes~ Take me~ Make me your woman!"
            reham "I... I love you, [mc]!"
            mc "Is that for me, or just for how full my cock makes you feel right now?"
            reham "Both! I love you and the way you reach so deep it feels like you're touching my soul!"
            mc "*laughs* That's what I like to hear! Let the whole house—hell, the whole street—know that Rohan's daughter belongs to me!"
            reham "AGHNMM~! YES~! FHNNNNNN~! I'm yours... I'm [mc]'s woman!"
            mc "Alright—actually, ease up a little. You're going to wake everyone if you keep going like that... assuming they aren't already awake."
    elif s130_standing_vaginal_2:
        $ s130_standing_vaginal_2 = False
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_vsex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_vsex3 with dissolve
        sensation "Her walls begin to flutter and seize around you without warning, quivering in tight, rhythmic spasms that milk your cock with desperate intensity."
        mc "God, Reham... you want my load that badly?"
        reham "Mghnnn~ Yes, yes, yes, yes! Pease... give it to me... fill me..."
        reham "Don't pull out... don't you dare pull out... I want to feel every drop..."
        mc "Careful what you wish for!"
        reham "It's too good~ I can't think~ just keep fucking me until you empty everything inside!"
    else:
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_vsex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_vsex3 with dissolve
        sensation "he wet, filthy sound of your hips meeting hers fills the room as you pound into her without restraint. Her legs are shaking so hard she can barely keep herself upright."
        reham "Ahhhnn...! Yes—just like that...! I'm going to break... I'm really going to break...!"
        reham "I love you! I love your cock! I love how you use me! make me take it~ make me yours completely~"
    call screen s30_sex with dissolve

label s130_sitting_vaginal:

    $ s130_standing = False
    $ s130_sitting = True
    $ s130_anal = False
    $ s130_vaginal = True

    if reham_pussy_virgin:
        $ reham_pussy_virgin = False
        $ s130_vaginal = True
        play sound "se_sfx/masturbate_female/3_masturbate3.mp3"
        scene 130_s5 with Dissolve(1.3)
        sensation "She reaches down, guides your cock to her entrance, and slowly sinks onto you. Her walls close around you in a tight embrace."
        reham "Ahhn...! You're stretching me so wide! My hymen is breaking! You're taking my virginity, [mc]!"
        mc "Fuck... this tightness is unreal."
        play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
        scene 130_s6 with Dissolve(1.0)
        reham "Calm down, [mc]... you'll tear me apart if you—ahh!"
        scene 130_s7 with dissolve
        mc "Hmm? I just touched something, didn't I?"
        scene 130_s6 with dissolve
        reham "Y-Yes... that's my cervix. It feels like I might lose control... like I need to pee..."
        scene 130_s7 with dissolve
        mc "We haven't even started moving yet."
        show s130_vsex1 with dissolve
        sensation "You begin to thrust in quick, deep strokes. Her walls grow slicker with every motion, coating you and letting you press even deeper."
        reham "Mhnnn~ It feels so good~"
        if mc_slept_maia_reham_106:
            mc "Better than last time with Maia?"
            reham "So much better... It's because of what you said earlier. The way you looked at me and meant every word..."
            reham "It made me want you even more... Fhnn~!"
        mc "*chuckles* I love those cute sounds you make... but you're going to wake someone if you keep going like that."
        reham "Oh! You're right... go slower."
        mc "Not happening. Keep your voice down while I ravage your pussy."
        reham "Ammh! You're so cruel... I can't stay quiet when I feel your tip kissing my cervix like that..."
        call screen s30_sex with dissolve
        
    if s130_sitting_vaginal_1:
        $ s130_sitting_vaginal_1 = False
        $ s130_sitting_vaginal_2 = True
        scene black with Dissolve(0.3)
        show s130_vsex1 with dissolve
        sensation "Her walls clamps down even tighter, refusing to let you pull back even an inch. You lean over her, arms wrapping around her damp, trembling body as you keep driving into her depths."
        reham "Gaaahd~! I'm losing my mind~ I don't think I can go back to living without this... you... completely... ruined... meeee~!"
        reham "My pussy... it's completely yours now~ it only wants thi~ only wants you~"
        sensation "She pushes back against you as hard as she can, trying to take you even deeper despite how tightly she's already gripping you."
        reham "Harder... please... ruin me more... I don't care if they hear... just don't stoooppp..."
    elif s130_sitting_vaginal_2:
        scene black with Dissolve(0.3)
        show s130_vsex1 with dissolve
        sensation "Her entire body seizes up around you. Her pussy locks down in a series of violent, rhythmic contractions that try to pull you even deeper, milking you with pure desperate need. She is barely coherent now."
        reham "F-fill me... fill me... fill me... please... I need your seed... I need it so badly..."
        reham "Breed me... claim me... make sure everyone knows who I belong to when I walk around leaking you tomorrow~"
        mc "*laughs* R-Reham... are you alright?"
        reham "Please... cum... cum inside your woman, [mc]!"
    else:
        scene black with Dissolve(0.3)
        show s130_vsex1 with dissolve
        reham "Ahh~! Mhnm~ Hahnm~ Nmmh~! Hahn~"
    call screen s30_sex with dissolve

default s130_standing_anal_1 = True
default s130_standing_anal_2 = False

default s130_sitting_anal_1 = True
default s130_sitting_anal_2 = False

default reham_anus_virgin_dialogue = False

label s130_standing_anal:
    $ s130_standing = True
    $ s130_sitting = False
    $ s130_anal = True
    $ s130_vaginal = False
    if reham_anus_virgin:
        $ reham_anus_virgin_dialogue = True
        $ reham_anus_virgin = False
        mc "Reham! I wanna take you in the ass!"
        reham "W-What?! Back there?"
        mc "Yes! Let me know how your tighter hole feels like."
        reham "...O-Only if you promise to be gentle!"
        mc "Promise."
        reham "Alright. J-Just go slow. Please. My butt is untouched. This is the first time I'd be putting something inside of it..."
        play sound "se_sfx/masturbate_female/1_masturbate.mp3"
        scene 130_s11 with Fade(1.0,1.0,1.0)
        sensation "You push forward carefully. The head finally breaches her with a thick, resistant stretch. She gasps sharply, body going rigid in your arms as the tight heat slowly yields around you."
        reham "Gahh...! It's... so much thicker than I expected..."
        mc "Breathe. I've got you."
        play sound "se_sfx/sex/sex2.mp3" 
        scene 130_s12 with Dissolve(1.0)
        sensation "Inch by inch you sink deeper. Her walls grip you far tighter than anything else, fluttering and spasming around the unfamiliar stretch. When you finally bottom out, she is trembling."
        reham "It burns a little... but keep going. I want to give this to you."
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_asex3 with dissolve
        reham "Hahh... I can feel you so deep..."
        mc "You're taking me so well for your first time."
        reham "Don't... don't praise me like that right now. It makes it harder to stay quiet..."
        sensation "You begin with slow, shallow thrusts, giving her body time to accept the new sensation. Each drag pulls a soft, strained sound from her throat."
        reham "Nnh... it's strange... full in a way I've never felt before..."
        mc "Does it hurt?"
        reham "A little... but it's starting to feel... good too. In a heavy, overwhelming way."
        reham "Ahh... [mc]... you're really inside my ass... I can't believe I'm letting you do this..."
        mc "You're doing perfect. Just keep breathing for me."
        reham "I am... it just feels so intense... like you're claiming a part of me no one else has ever touched..."
        reham "You can go a little deeper now... I think I can take it."
        call screen s30_sex with dissolve

    if s130_standing_anal_1:
        $ s130_standing_anal_1 = False
        $ s130_standing_anal_2 = True
        if not reham_anus_virgin_dialogue:
            scene 130_s11 with Fade(1.0,1.0,1.0)
            perception "She stands up and sits on the edge of the dinner table. Her anus twitches slightly, gleaming with sweat."
            mc "Mhnm!"
            play sound "se_sfx/sex/sex2.mp3" 
            scene 130_s12 with Dissolve(1.0)
            sensation "You allign your cock and push back into her rectum in one steady thrust."
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_asex3 with dissolve
        reham "HAAAAAH~! Careful, [mc]! My ass isn't ready for that kind of roughness yet!"
        mc "It will be. I'll make sure this tight little asshole remembers my shape."
        reham "Y-You're going to keep using it, aren't you? You're going to turn my... my innocent ass into something that only exists for your pleasure..."
        mc "I will. But it won't just be for me. You'll end up craving it too."
        reham "Mhnmm... K-Keep talking like that..."
        mc "I'm going to ruin you for anything else... you won't be able to sit properly after I'm done with you."
        mc "You'll think about me every time you try."
        reham "Mnhh~! That's so unfair... yet I don't want you to stop..."
        reham "Harder, [mc]~ just a little harder... but please... don't make me scream..."
    elif s130_standing_anal_2:
        $ s130_standing_anal_2 = False
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_asex3 with dissolve
        perception "You set a deeper rhythm, each thrust stretching her open and forcing her to clench her toes. The table creaks faintly under her hands."
        reham "Ahh! [mc]... where are you trying to reach? I can already feel you stretching my intestines!"
        mc "Good. Take it. Every inch."
        reham "It's so deep... it feels like you're forcing your way somewhere you shouldn't be... but I can't make you stop..."
    else:
        if s130_POV1:
            scene black with Dissolve(0.3)
            show s130_asex2 with dissolve
        else:
            scene black with Dissolve(0.3)
            show s130_asex3 with dissolve
        reham "Ahhh~! I'm getting close... from my ass... I can't believe I'm getting close like this..."
        mc "You want me to fill this hole up?"
        reham "Yes~! please... I want to feel your seed leaking out of me afterward... I want to walk around knowing you came in the place no one else has touched~"
        reham "Breed my ass if you want~ claim every part of me, just don't stop until you've given me everything~!"
    call screen s30_sex with dissolve


label s130_sitting_anal:
    $ s130_standing = False
    $ s130_sitting = True
    $ s130_anal = True
    $ s130_vaginal = False

    if reham_anus_virgin:
        jump s130_standing_anal

    if s130_sitting_anal_1:
        $ s130_sitting_anal_1 = False
        scene black with Dissolve(0.3)
        show s130_asex1 with dissolve
        sensation "You wrap your arms around her waist and begin thrusting upward in short, powerful strokes. Each one forces a wet sound from the place where your bodies meet. Her earlier hesitation has almost completely vanished."
        reham "Nnhh...! Yes... just like that... use my ass however you want~"
        reham "I was so scared of this at first, and now I can't stop pushing back for more~"
        mc "Ahhnn!"
        reham "Ruin it~ make it so I only open this easily for you~ I don't care if it's wrong anymore~"
    else:
        scene black with Dissolve(0.3)
        show s130_asex1 with dissolve
        sensation "You pull her back down onto your lap, guiding her to sink onto your cock again. Gravity helps her take you to the base."
        reham "Ahmmm~ [mc]~ I can barely think... my whole body feels like it's melting~"
        reham "Gods~! I... I think I'm starting to like this too much... just what are you doing to my innocent backdoor?"
    call screen s30_sex with dissolve
    
label s130_cum:
    call screen s130_sex_cum with dissolve

label s130_sex_cum_inside:
    if s130_vaginal:
        mc "I'm gonna fill you up!"
        if s130_sitting:
            if s130_POV1:
                scene black with Dissolve(0.3)
                show s130_vsex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s130_vsex3 with dissolve
        if reham_pregnant:
            reham "Do it, [mc]~ My pussy is aching for your seed!"
            mc "Beg for it!"
            reham "Please, [mc]! Fill my womb! Flood it and let it spill from my sore pussy~!"
            play sound "se_sfx/sex/sex_cum11.mp3" 
            if persistent.xray_mode:
                scene 130_s13_xray1 with vpunch
            else:
                scene 130_s13 with vpunch
            mc "AGHNNNN!"
            sensation "A thick, continuous pulse of cum floods out of you, pumping straight into her already sensitive womb. You can feel her belly subtly tighten as more keeps coming."
            reham "Ahhhnn! It's too much... too hot!"
            play sound "se_sfx/sex/sex_cum4.mp3" 
            if persistent.xray_mode:
                scene 130_s14_xray2 with vpunch
            else:
                scene 130_s14 with vpunch
            sensation "Another strong spurt follows. Her walls are so full that the excess begins to leak out around your cock and drip onto the floor."
            reham "MPHMM~! I'm— I'm coming too!"
            play sound "se_sfx/sex/touch3.mp3" 
            if persistent.xray_mode:
                scene 130_s15_xray3 with Dissolve(1.0)
            else:
                scene 130_s15 with Dissolve(1.0)
            mc "Hahh... Ahh..."
            reham "Mhnn... hahnn... Gods. That amount... is it because you love me?"
            mc "What else would it be? You brought it out of me."
            reham "*chuckles* I... I want to tell you something. I just never found the right moment."
            mc "Of course. Anything."
            scene 130_s16 with Dissolve(1.0)
            reham "I-I'm already pregnant. Not from just now... from last time."
            scene 130_s17 with dissolve
            mc "R-Really? Congratulations!"
            scene 130_s19 with dissolve
            reham "..."
            scene 130_s18 with vpunch
            reham "Don't you congratulate me! You came inside me without a second thought—twice!"
            scene 130_s19 with dissolve
            mc "...Right."
            scene 130_s16 with dissolve
            reham "*sigh* I was so scared at first. I thought I was carrying the child of a man who didn't truly want me. But now..."
            reham "Now that we're actually together, I feel... safer."
            scene 130_s17 with dissolve
            mc "Good. I'll take care of you and the child in your belly."
            if maia_pregnant or reb_pregnant or nadia_pregnant or diana_pregnant:
                scene 130_s16 with dissolve
                reham "You'll be taking care of {i}many{/i} women with children in their bellies, you know."
                scene 130_s17 with dissolve
                mc "Uhh..."
                scene 130_s16 with dissolve
                reham "You think I didn't notice? I can practically smell your seed from a mile away, [mc]. And you don't look like the type who only takes care of it by himself, which means..."
                scene 130_s17 with dissolve
                mc "Alright, you caught me. But I'm strong enough. I can look after more than one."
                scene 130_s16 with dissolve
                reham "*giggles* You'd better. And you'd better look after me the most."
                scene 130_s17 with dissolve
                mc "*chuckles* I'll try my best."
        else:
            reham "Do it, [mc]~! My pussy is aching for your seed. My whole body wants it."
            mc "Beg for it!"
            reham "Please, [mc]! Fill my womb and make me swell with your child! I want to be pregnant with your baby!"
            play sound "se_sfx/sex/sex_cum11.mp3" 
            if persistent.xray_mode:
                scene 130_s13_xray1 with vpunch
            else:
                scene 130_s13 with vpunch
            mc "AGHNNNN!"
            sensation "A thick, continuous pulse of cum floods out of you, pumping straight into her already sensitive womb. You can feel her belly subtly tighten as more keeps coming."
            reham "Ahhhnn! It's too much... too hot!"
            play sound "se_sfx/sex/sex_cum4.mp3" 
            if persistent.xray_mode:
                scene 130_s14_xray2 with vpunch
            else:
                scene 130_s14 with vpunch
            sensation "Another strong spurt follows. Her walls are so full that the excess begins to leak out around your cock and drip onto the floor."
            reham "MPHMM~! I'm— I'm coming too!"
            play sound "se_sfx/sex/touch3.mp3" 
            if persistent.xray_mode:
                scene 130_s15_xray3 with Dissolve(1.0)
            else:
                scene 130_s15 with Dissolve(1.0)
            mc "Hahh... Ahh..."
            call pregnancy_check_reham from _call_pregnancy_check_reham
            reham "Mhnn... hahnn... You really wanted me pregnant, didn't you..."
            mc "I couldn't hold back. What you said just now... did you mean it?"
            reham "I did. What's a better way to keep a man close than carrying his child?"
            mc "*chuckles* You little snake."
            scene 130_s16 with Dissolve(1.0)
            reham "Don't blame me~ I just hope it actually took."
            scene 130_s17 with dissolve
            mc "If it did, I'll take responsibility. For you and for our child."
            if maia_pregnant or reb_pregnant or nadia_pregnant or diana_pregnant:
                scene 130_s16 with dissolve
                reham "You'll be taking care of {i}many{/i} women with children in their bellies, you know."
                scene 130_s17 with dissolve
                mc "Uhh..."
                scene 130_s16 with dissolve
                reham "You think I didn't notice? I can practically smell your seed from a mile away, [mc]. And you don't look like the type who only takes care of it by himself, which means..."
                scene 130_s17 with dissolve
                mc "Alright, you caught me. But I'm strong enough. I can look after more than one."
                scene 130_s16 with dissolve
                reham "*giggles* You'd better. And you'd better look after me the most."
                scene 130_s17 with dissolve
                mc "*chuckles* I'll try my best."
    else:
        if s130_sitting:
            if s130_POV1:
                scene black with Dissolve(0.3)
                show s130_asex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s130_asex3 with dissolve
        mc "I'm going to fill you up!"
        reham "W-Will you finish inside my ass, [mc]?"
        mc "Do you want me to?!"
        reham "Yes, yes, yes! I want to feel your seed slowly leaking from my butt!"
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene 130_s20 with vpunch
        mc "AGHN!"
        sensation "You drive in to the hilt and hold her tightly as the first thick pulse of cum erupts deep inside her rectum. The tight heat around you milks every spurt, forcing more out of you in long, heavy throbs."
        reham "Ahhhnn! It's so hot... I can feel it spreading in my belly!"
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 130_s21 with vpunch
        sensation "Another strong wave follows, then another. Her body clenches around you reflexively, trying to keep everything inside even as the excess begins to push back around your cock."
        reham "Mnhh~! There's so much... it's already starting to leak..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 130_s22 with Dissolve(1.0)
        mc "Hahh... ahh..."
        reham "Mhnn... hahnn... Gods... it feels so full..."
        reham "I don't know if I'm hungry anymore..."
        mc "*laughs* It's already spilling out. Just like you asked for."
        mc "You really wanted it that badly?"
        reham "I did. I wanted to feel marked by you... even in my butt~"
        
    jump s130_sex2

label s130_sex_cum_outside:
    if s130_vaginal:
        if s130_sitting:
            if s130_POV1:
                scene black with Dissolve(0.3)
                show s130_vsex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s130_vsex3 with dissolve
        mc "Ughh! I'll cover your ass!"
        reham "Do it~ Mark me, [mc]~"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene 130_s23 with vpunch
        sensation "You pull out at the last second and stroke yourself hard against her. The first thick pulse of cum streaks across her lower back and the soft curve of her ass."
        reham "Ahhhnn...! It's so hot... I can feel it dripping down my skin!"
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene 130_s24 with vpunch
        sensation "You keep stroking through the rest of your orgasm, painting her ass and the backs of her thighs in uneven white lines. A few weaker spurts land closer to her entrance and slowly begin to run downward."
        reham "MPHMM~! I'm— I'm coming too! just from that~!"
        scene 130_s25 with Dissolve(1.0)
        mc "Hahh... ahh..."
        reham "Mhnn... hahnn... Why didn't you finish inside me?"
        mc "I wanted to see you marked instead."
        reham "Mmmm~ There's something satisfying about being covered by you like this..."
        mc "*chuckles* That's so perverted."
        reham "Don't blame me~ It feels just as claiming in its own way."
    
    else:
        if s130_sitting:
            if s130_POV1:
                scene black with Dissolve(0.3)
                show s130_asex2 with dissolve
            else:
                scene black with Dissolve(0.3)
                show s130_asex3 with dissolve
        mc "Ughh! I'll cover your ass!"
        reham "Do it~ Mark me, [mc]~"
        play sound "se_sfx/blowjob/facial4.mp3" 
        scene 130_s26 with vpunch
        sensation "You pull free at the peak and stroke yourself rapidly. The first thick pulse of cum lands across the cleft of her ass and the tight, stretched ring of her hole."
        reham "Ahhhnn...! It's so hot... I can feel it running down between my cheeks!"
        play sound "se_sfx/blowjob/facial5.mp3" 
        scene 130_s27 with vpunch
        sensation "You keep going, painting her ass in messy white lines. Some of it drips directly onto her still-twitching anus and slowly begins to slide downward toward her thighs."
        reham "Mnhh~! There's so much~ it's already dripping everywhere..."
        scene 130_s28 with Dissolve(1.0)
        mc "Hahh... ahh..."
        reham "Mhnn... hahnn... Why didn't you finish inside me?"
        mc "I wanted to see you marked instead."
        reham "Mmmm~ There's something satisfying about being covered by you like this..."
        mc "*chuckles* That's so perverted."
        reham "Don't blame me~ It feels just as claiming in its own way."
    jump s130_sex2

label s130_sex2:
    scene 130_s30 with Fade(1.0,1.0,1.0)
    reham "Hahh... We really made a mess... I need to clean this up. My parents usually wake around this time."
    reham "I... also need to clean myself. *giggles* I can't exactly walk around dripping with your seed."
    scene 130_s29 with dissolve
    mc "I need to clean up too. You got your sweat all over me."
    scene 130_s30 with dissolve
    reham "Th-that's just the weather. You know how it is—"
    scene 130_s29 with dissolve
    scene black with Dissolve(1.0)
    "*click*"
    reham "Shit! I need to dress up quickly! You too, [mc]!"
    play sound "sound_effects/doors/door_open2.mp3"
    scene 131_s5 with Dissolve(1.0)
    yasmine "*yawn* Reham?"
    scene 131_s4 with dissolve
    reham "M-Mother?! You're... you're awake already."
    scene 131_s5 with dissolve
    yasmine "Mhm. Where's [mc]?"
    scene 131_s4 with dissolve
    mc "I'm here, ma'am. Just... cleaning up the shelfs."
    scene 131_s5 with dissolve
    yasmine "Ma'am? Please, just call me Yasmine."
    scene 131_s6 with dissolve
    yasmine "And—Ugh! What is that smell?"
    reham "Huh?! What smell?"
    yasmine "It smells like someone has been running for hours in here. All hot and... heavy."
    reham "M-Must be [mc]. I found him sleeping in the chair earlier. He... sweats a lot when he sleeps."
    mc "..."
    scene 131_s5 with Dissolve(1.0)
    yasmine "Well, whatever it's coming from, clean it up. And open the windows. It reeks in here."
    scene 131_s4 with dissolve
    reham "On it."
    scene 131_s1 with Dissolve(1.0)
    reham "S-Sorry for putting you on the spot like that, [mc]. I'll make it up to you later."
    scene 131_s2 with dissolve
    mc "*chuckles* Sure. By the way, your nipple's showing."
    $ renpy.end_replay()
    
    jump scene131

image s130_hj1 = Movie(play="images/chapter5/scene130/s130_hj1.webm", loop=True)
image s130_hj2 = Movie(play="images/chapter5/scene130/s130_hj2.webm", loop=True)

label scene130_hj:
    stop music fadeout 1.0
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_7_replay:
        $ persistent.chapter5_p7_7_replay = True

    $ s130_hj1 = True
    $ mc_hj_reham_130 = True

    scene 130_s31 with Fade(1.3,1.0,1.3)
    perception "She takes off her dress then kneels on the floor in front of you, carefully undoing your pants and working them down."
    scene 130_s32 with Dissolve(1.0)
    reham "Oh my... That really is quite an erection."
    scene 130_s33 with dissolve
    mc "I told you. It's like this every morning."
    scene 130_s32 with dissolve
    reham "I see... L-Let me take care of it, then."
    scene 130_s33 with dissolve
    show s130_hj1 with Dissolve(1.0)
    perception "She brings one hand to her mouth, wets her palm thoroughly with spit, then entwines her other hand with yours, gripping it lightly."
    reham "Does that feel alright? Should I add more spit?"
    mc "Ahh... No, this is good. Keep going like that."
    reham "It's so thick... It must be miserable trying to walk around or think straight when you're this hard."
    mc "Yeah. I'm glad I have someone willing to help."
    if mc_harem_reham_dom or mc_harem_reham_dom_dom:
        reham "Of course, Master. It's my duty as your personal servant. I just wish you'd pick better places or times for this..."
    else:
        reham "D-Don't get used to it, [mc]. I already told you—this is only a one-time thing."
    call screen s130_hj with dissolve

default s130_hj1_1 = True
default s130_hj1_2 = False

default s130_hj1 = False
default s130_hj2 = False

label s130_hj1:
    $ s130_hj1 = True
    $ s130_hj2 = False

    if s130_hj1_1:
        $ s130_hj1_1 = False
        $ s130_hj1_2 = True
        scene black with Dissolve(0.3)
        show s130_hj1 with dissolve
        sensation "She moves her hand with more confidence now, twisting slightly on the upstroke and squeezing just under the head. The wet sound of spit and skin fills the quiet room."
        mc "Ahmm..."
        reham "If you finish like this... it's going to go straight onto my face."
        mc "God... the thought of that is already pushing me closer."
        reham "You want to finish on me?"
        mc "Maybe. Marking that pretty face of yours doesn't sound like a bad idea."
        reham "..."
        reham "A-Alright. You can do it. Whenever you're ready... just let it out."
        mc "Reham..."
        reham "It's fine. I'll take it. You've been holding this in since you woke up... so go ahead. Spill it all over me if that's what you need."
        empathy "She's a little embarrassed, but she doesn't look away. She keeps working your cock, angling it upward toward her face, ready to catch everything you give her."
    elif s130_hj1_2:
        $ s130_hj1_2 = False
        scene black with Dissolve(0.3)
        show s130_hj1 with dissolve
        reham "Hmphh... Hahh..."
        mc "*chuckles* Getting tired?"
        reham "A-A little. This isn't something I usually do, you know."
        reham "You're still so hard... Does it ever go down on its own in the morning?"
        mc "Not when you're right in front of me like this."
        reham "...Flatterer."
    else:
        scene black with Dissolve(0.3)
        show s130_hj1 with dissolve
        reham "Hahm... Mhnmm... A-Are you close? You're leaking a lot from the tip."
    call screen s130_hj with dissolve

default s130_hj2_1 = True
default s130_hj2_2 = False
default s130_hj2_3 = False

label s130_hj2:
    $ s130_hj1 = False
    $ s130_hj2 = True

    if s130_hj2_1:
        $ s130_hj2_1 = False
        $ s130_hj2_2 = True
        mc "Come closer, Reham. I want to take in your scent while you do this."
        reham "Scent?! Don't say embarrassing things like that out of nowhere..."
        mc "It's true. You always smell good."
        reham "You actually like my scent?"
        mc "I do."
        reham "*laughs* Really? It might just be pheromones playing tricks on you. My mother always says otherwise."
        mc "*sniff* Then your mother doesn't know what she's talking about."
        scene black with Dissolve(1.0)
        show s130_hj2 with Dissolve(1.0)
        perception "She stands and sits on the chair beside you. Her body getting sweatier from working you through the heat."
        reham "S-Stare at my breasts... it should help you finish stronger."
        mc "Ahh... Reham, they look so soft."
        reham "The way you stare so intently... it's making my nipples hard."
        sensation "The pressure from her hand is perfect—firm enough to feel every ridge of her palm, smooth enough that the pleasure builds without rushing."
        mc "*sniff* *sniff* Keep doing it just like that..."
        if not mc_maia_left:
            reham "Gods... Are you always this intense with Maia too?"
        else:
            reham "Gods... Are you always this intense?" 
    elif s130_hj2_2:
        $ s130_hj2_2 = False
        $ s130_hj2_3 = True
        scene black with Dissolve(0.3)
        show s130_hj2 with dissolve
        sensation "Her coarse hand sends a sharp sparks of pleasure through you. Her exposed breasts rise and fall with her breathing, close enough that you can feel the warmth of her skin."
        reham "You're getting even harder... Are you close?"
        mc "Getting there. Don't stop."
        reham "I wasn't planning to. Whenever you're ready... just let go. I'll keep stroking you through it."
        reham "Go ahead, [mc]. Finish for me~"
        mc "*chuckles* Are you rushing me?"
        reham "It's not like we have all day... my parents will wake up any moment now."
    elif s130_hj2_3:
        $ s130_hj2_3 = False
        scene black with Dissolve(0.3)
        show s130_hj2 with dissolve
        perception "The wet sound grows louder. Her free hand rests on your shoulder, fingers twitching as if she's resisting the urge to do more."
        reham "Hahh... You're leaking so much... It's making my hand all sticky."
        mc "Feels too good to care."
        reham "Of course it does..."
    else:
        scene black with Dissolve(0.3)
        show s130_hj2 with dissolve
        reham "*giggles* That's it... just get lost in the pleasure while I tire myself out in the morning."
    call screen s130_hj with dissolve

label s130_cum2:
    if s130_hj1:
        mc "Reham... I'm close—"
        reham "I know. It's alright. Just let it out."
        sensation "Her hand speeds up, working you firmly from base to tip. She tilts her face upward, eyes half-lidded, waiting."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene 130_s38 with vpunch
        mc "Aghnn!"
        sensation "The first thick rope of cum shoots across her cheek and brow. A second follows immediately, landing on her other cheek."
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene 130_s39 with vpunch
        reham "Mphnm!"
        sensation "She keeps stroking you through it, milking out every pulse until the last weaker spurts drip onto her skin and her hand."
        scene 130_s40 with Dissolve(1.0)
        reham "Mhnn... there's so much..."
        scene 130_s41 with dissolve
        mc "Hahhh... who knew a handjob could feel this good."
        scene 130_s40 with dissolve
        reham "...There. All done."
        scene 130_s41 with dissolve
        mc "Hahh... right. sorry about the mess."
        scene 130_s40 with dissolve
        reham "It's fine. Just... give me a moment to wipe it off before anyone sees."
        reham "Sit there and catch your breath."
        scene 130_s41 with dissolve
        $ renpy.end_replay()
    else:
        mc "Reham... I'm close—"
        reham "I know. Keep looking at me if you want..."
        sensation "Her hand tightens and strokes faster, focused and steady. She angles your cock slightly downward so most of it will land on her palm and the floor rather than her body."
        play sound "se_sfx/blowjob/facial3.mp3" 
        scene 130_s34 with vpunch
        mc "Aghnn!"
        sensation "Hot cum spills over her fingers in thick pulses. The first few spurts coat her hand completely; the rest drips between her fingers and splatters onto the floor."
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene 130_s35 with vpunch
        mc "AHHNN!"
        sensation "She keeps moving her hand through the entire orgasm, slowing only when the last drops leak out."
        scene 130_s36 with Dissolve(1.0)
        reham "Hahh... that really was a lot."
        scene 130_s37 with dissolve
        mc "Fuck... you made me spill so much with just your hands."
        scene 130_s36 with dissolve
        reham "I'll clean this up. You just... catch your breath."
        scene 130_s37 with dissolve
        $ renpy.end_replay()
    jump scene131

label scene131:
    if mc_sexed_reham_130:
        scene 131_s7 with Fade(1.0,1.0,1.0)
        mc "I want to check on Maia."
        scene 131_s8 with Dissolve(1.0)
        yasmine "Of course. She's in the bedroom. But please try to be quiet, I don't want him to wake up yet..."
        yasmine "We have a long talk to go through."
        jump scene131_2

    elif mc_hj_reham_130:
        scene 131_s1 with Fade(1.3,1.0,1.3)
        reham "There. Feeling better now?"
        scene 131_s2 with dissolve
        mc "I feel rejuvinated!"
        scene 131_s1 with dissolve
        reham "*chuckles* Good."
        scene 131_s3 with dissolve
        yasmine "*yawn* Reham?"
        scene 131_s4 with dissolve
        reham "M-Mother?! You're... you're awake already."
        scene 131_s5 with dissolve
        yasmine "Mhm. Where's [mc]?"
        scene 131_s4 with dissolve
        mc "I'm here, ma'am."
        scene 131_s5 with dissolve
        yasmine "Ma'am? Please, just call me Yasmine."
        scene 131_s6 with dissolve
        yasmine "And—Ugh! What is that smell?"
        reham "Huh?! What smell?"
        yasmine "It smells like... I don't know, something... It's also smells like sweat in here."
        reham "M-Must be [mc]. I found him sleeping in the chair earlier. He... sweats a lot when he sleeps."
        yasmine "Whatever it's coming from, open the windows. It reeks in here."
        reham "On it."
        scene 131_s1 with dissolve
        reham "{size=30}S-Sorry for putting you on the spot like that, [mc]. I'll make it up to you later.{/size}"
        scene 131_s2 with dissolve
        mc "*chuckles* {size=30}Sure.{/size}"
        
    else:
        scene 131_s5 with Fade(1.0,1.0,1.0)
        yasmine "*yawn* Reham?"
        scene 131_s4 with dissolve
        reham "Mother? You're awake already."
        scene 131_s5 with dissolve
        yasmine "Mhm. Where's [mc]?"
        scene 131_s4 with dissolve
        mc "I'm here, ma'am."
        scene 131_s5 with dissolve
        yasmine "Ma'am? Please, just call me Yasmine."
        yasmine "Did you eat yet, [mc]?"
        scene 131_s4 with dissolve
        reham "I was about to make him a sandwitch."
        scene 131_s5 with dissolve
        yasmine "*yawn* Pour him some juice too."
        scene 131_s4 with dissolve
        reham "On it!"

    scene 131_s7 with Dissolve(1.5)
    mc "I want to check on Maia."
    scene 131_s8 with Dissolve(1.0)
    yasmine "Of course. She's in the bedroom. But please try to be quiet, I don't want him to wake up yet..."
    yasmine "We have a long talk to go through."
    jump scene131_2

label scene131_2:
    if mc_killed_reham:
        scene 129_s64 with Fade(1.0,1.0,1.0)
        mc "Are you alright, Maia?"
        m "..."
        mc "Maia? Talk to me. Please."
        scene 129_s65 with dissolve
        m "Oh! I-I'm also doing well, [mc]... I'm fine. Everything's fine."
        scene 129_s66 with dissolve
        mc "You clearly aren't. You look like you're about to cry. What's wrong? Is it about what he said? About Abel?"
        m "..."
        scene 129_s65 with dissolve
        m "I need to go rest. I'm tired."
        scene 129_s67 with dissolve
        mc "Hey! Don't just walk away—you can't keep burying this!"
        m "S-Sorry... I just... I can't right now. Please don't make me."
        empathy "She's retreating back into herself. Whatever Vic said have shaken something loose that she's been trying very hard to keep buried."
        scene 129_s57 with dissolve
        mc "*sigh* (I'll talk to her tomorrow.)"
        mc "(For now, I have to keep watch of the place in case anyone else tries to come.)"
        scene 129_s116 with dissolve
        sensation "You feel intense heat across your cheeks. The sun is relentless here in the desert. You wake up in a sweaty haze, your tunic clinging to your chest."
        scene 129_s148 with dissolve
        mc "Hnnm?"
        mc "(Ah, right... I can't believe I let myself sleep. Some bodyguard I am.)"
        mc "(I need to check on Maia.)"
    scene 131_s9 with Dissolve(1.5)
    ""
    play sound "sound_effects/doors/door_open2.mp3"
    stop music fadeout 1.0
    scene 131_s10 with dissolve
    perception "Maia is curled up in the far corner of the bed, knees drawn to her chest, staring at nothing. Her eyes are vacant, the light behind them almost completely gone."
    play music "sad/distorted_spiritual_realm.mp3" fadein 3.0 loop
    scene 131_s11 with Dissolve(1.0)
    mc "(She looks so broken...)"
    mc "(This isn't just about what Vic said. This runs much deeper than that. She's been carrying this fear for years... maybe for as long as she can remember.)"
    mc "(Is there anything I can even do to cheer her up at this point? Words feel useless.)"
    call screen scene129_choice11 with dissolve

default s129_maia_choice1 = False
default s129_maia_choice2 = False
default s129_maia_choice3 = False
default s129_maia_choice4 = False

label scene129_choice11_op1:
    $ s129_maia_choice1 = True
    scene 131_s12 with dissolve
    perception "You take a step back, lower your stance, and attempt a backflip in the middle of the quiet bedroom."
    scene 131_s13 with Dissolve(0.3)
    play sound "sound_effects/body/wood_slam.mp3"
    scene 131_s13 with vpunch
    mc "Tata!"
    scene 131_s11 with Dissolve(1.0)
    m "..."
    empathy "She doesn't even flinch. Her vacant eyes stay fixed on the same empty point."
    mc "(...Yeah. That did nothing. What the hell was I thinking?)"
    if not mc_killed_reham:
        reham "[mc]?! What was that noise?"
        mc "I-I just dropped something."
    call screen scene129_choice11 with dissolve

label scene129_choice11_op2:
    scene 131_s16 with Dissolve(1.0)
    mc "Hey, Maia. I know you're going through something really hard right now."
    mc "And I know you probably don't want to talk about it. That's okay, you don't have to."
    mc "But I was thinking... would you want to go somewhere with me? Just the two of us? A quiet place."
    m "..."
    mc "We can sit and talk and eat something and pretend everything is fine for a few hours. I'd like that... I think you might too."
    if maia_love >= 80:
        $ mc_harem_maia_true = True
        scene 131_s17 with dissolve
        m "...A date? With me? Even after... after what I did?"
        scene 131_s16 with dissolve
        mc "Especially after."
        mc "You're not a monster, Maia. You're a girl who survived something horrible and did what she had to do."
        mc "That doesn't make you unworthy of love. Or sunlight. Or someone who wants to sit across a table and watch you smile again."
        scene 131_s17 with dissolve
        m "...You really mean that? You're not just saying it to make me feel better?"
        scene 131_s16 with dissolve
        mc "I do. I've wanted to ask you for a while. Before we got into all this."
        mc "What do you say? Wanna breath some fresh air?"
        scene 131_s17 with dissolve
        m "I... I'd like that."
        scene 131_s16 with dissolve
        mc "Then it's a date!"
        play sound "sound_effects/body/clothing_rustle3.mp3"
        stop music fadeout 1.0
        scene 131_s18 with vpunch
        m "Ahn!"
        sensation "A rush dopamine floods your brain. Before you can stop yourself, you reach out and scoop Maia into your arms, lifting her like she weighs nothing at all."
        scene 131_s19 with dissolve
        mc "Let's go! Now! I want to see your smile again! No way I'm living without that."
        m "..."
        if not mc_killed_reham:
            scene 131_s20 with Fade(1.3,1.0,1.3)
            play music "kitchen.mp3" fadein 1.0 loop
            yasmine "Hmm? My, oh my!"
            scene 131_s21 with dissolve
            reham "How...? I spent almost an hour yesterday with her with nothing working."
            reham "And you just... did it? In a few minutes?"
            scene 131_s20 with dissolve
            yasmine "You two look so cute together."
            scene 131_s74 with dissolve
            mc "We're going on a date, aren't we, Maia?"
            m "Mhm..."
            mc "We'll be out! Don't wait up!"
            scene 131_s20 with dissolve
            yasmine "*chuckles* Look at them go. Whoo! Young love!"
            stop music fadeout 1.0
            scene 131_s74 with dissolve
        scene 131_s24 with Fade(1.3,1.0,1.3)
        play music "talkingAmbiance.mp3" fadein 1.0 volume 0.4 loop
        env "The sun beats down indifferently on everything living. Civilians walk through the dusty streets, their robes pulled tight against the glare. The city is alive, oblivious to the girl who's only now beginning to emerge from her shell."
        m "[mc]... this is embarrassing... people will stare."
        mc "Let them stare. Let the whole city know that Maia is going on a date and nothing is going to stop her."
        scene 131_s25 with Dissolve(1.0)
        mc "Hey, you!"
        scene 131_s26 with Dissolve(1.0)
        if mc_killed_reham:
            man_in_house "Hah? Yes? Wait, have I seen you before?"
            scene 131_s27 with dissolve
            mc "That's not important right now."
        else:
            man_in_house "Hah? Yes?"
            scene 131_s27 with dissolve
        mc "Where's the best place for a date in this city?"
        scene 131_s26 with dissolve
        man_in_house "Date? Ah, you two on your honeymoon? Congratulations. I remember when my wife and I were like that."
        man_in_house "But... you didn't exactly pick the best place for romance. Nahraya is beautiful, but this district is mainly for traders."
        scene 131_s27 with dissolve
        mc "Come on, there has to be somewhere worthwhile here."
        scene 131_s26 with dissolve
        man_in_house "Hmm... ah! Have you been to Eunice's peak yet?"
        scene 131_s27 with dissolve
        mc "I haven't. What is it?"
        scene 131_s26 with dissolve
        man_in_house "Then that's where you should go! It's a large mountain on the northern edge of the city—can't miss it."
        man_in_house "The climb will suck every ounce of energy out of you. But the view... it's unlike any other. You can see the massive water crater left by our elven Goddess Eunice from up there."
        man_in_house "The place houses a shrine to her, but tourists go there for the view."
        scene 131_s27 with dissolve
        mc "Water crater? Anyway, that sounds good. I have a map, could you point it out for me?"
        scene 131_s28 with Dissolve(1.0)
        man_in_house "Sure. Give it here."
        stop music fadeout 1.3
        scene 131_s29 with Fade(1.3,1.0,1.3)
        play music "wind.mp3" fadein 1.0 loop
        perception "After a long ride through the winding streets and out of the district, you reach a camp overlooking the base of a massive mountain."
        mc "Damn. The man wasn't kidding—this climb will take a long time."
        m "Are you sure about this, [mc]? We could just... go eat at a stall or something."
        mc "I'm sure. You've been cooped up in that house for days. You need to breathe some air."
        scene 131_s31 with Dissolve(2.0)
        camel "Welcome, sir! Are you here to ascend the mountain with your partner? Fine day for it. The view from the summit is spectacular this time of year."
        scene 131_s32 with dissolve
        mc "We sure are."
        scene 131_s31 with dissolve
        camel "Perfect! We offer a great price on the camel rides—only three coppers per person."
        scene 131_s32 with dissolve
        mc "We won't need that."
        scene 131_s33 with dissolve
        camel "A-Are you certain? The climb has gotten particularly harder over the years. Falling rocks and debris have made it almost impossible to scale on legs alone."
        camel "How about one copper for each? Special price, just for you! For the young couple!"
        scene 131_s32 with dissolve
        mc "Thank you, but I'm sure. Just take care of our mare here until we return."
        scene 131_s31 with dissolve
        camel "As you wish. But don't say I didn't warn you. When you're halfway up and your legs are begging for mercy, you'll wish you'd taken the camel."
        scene 131_s34 with dissolve
        m "Y-You can put me down now, [mc]. I can walk."
        scene 131_s35 with dissolve
        mc "You kidding? And risk ruining your delicate feet?"
        scene 131_s34 with dissolve
        m "It's fine. [mc], reall—"
        play sound "sound_effects/woosh2.mp3"
        pause(0.3)
        scene 131_s36 with vpunch
        sensation "You start running. Your legs pump against the slope of the mountain as if it were flat ground. Your speed is enough to send a shockwave of dust billowing behind you."
        m "W-W-What's happening?! We're going so fast!"
        mc "*chuckles* Hold on tight, Maia! Don't let go!"
        m "The city's getting smaller! I can see the camp we were just in! I can see the merchants and the camels and—and everything! We're so high up!"
        mc "Nghnn! Almost... almost there..."
        scene 131_s38 with Dissolve(1.0)
        mc "Hahh! Ahh! T-There..."
        m "H-How did you do that, [mc]? That was... that wasn't normal."
        scene 131_s39 with Dissolve(1.0)
        mc "*gag* Fuck..."
        scene 131_s40 with dissolve
        m "[mc]?! Are you alright?!"
        scene 131_s39 with dissolve
        mc "I-I'm fine. Just... overdid it a little."
        minthra "Fool. My power isn't something for you to use so irresponsibly. You drain yourself needlessly and weaken us both. Do not make a habit of this."
        mc "Let's go look at this view. It better be the best view in the history of views."
        stop music fadeout 1.0
        scene 131_s41 with Fade(1.0,1.0,1.5)
        play music "ocean.mp3" fadein 1.0 loop
        perception "An insanly large crater filled with water sprawls in beneath you. Beyond that, the desert stretches to the horizon—an endless ocean of sand dunes, shimmering in the heat. It feels like standing on the edge of the world."
        m "It's... so beautiful."
        mc "It is. This is... this is worth the climb."
        m "The water looks like glass. The sky looks like it goes on forever."
        stop music fadeout 1.0
        scene 131_s42 with dissolve
        m "..."
        mc "Maia?"
        scene 131_s43 with Dissolve(1.0)
        play music "hope/rose_of_may.mp3" fadein 3.0 loop
        m "*hic* [mc]! HAAAAAAA!"
        mc "..."
        scene 131_s45 with Dissolve(1.0)
        mc "I'm here. I'll always be here. I promise."
        scene 131_s44 with dissolve
        m "Ahhhhh! I killed him! I stabbed him so many times and I didn't stop—"
        scene 131_s45 with dissolve
        mc "Let it out. I'm here for you."
        scene 131_s44 with dissolve
        m "*hic* *sniff* I'm sorry... I'm so sorry... I ruined our date... I ruined the view... I ruin everything..."
        scene 131_s45 with dissolve
        mc "There's nothing for you to be sorry about. What you did, I completely understand it."
        mc "Abel was a monster who had hurt you and was going to keep hurting you. You did what you had to do to survive."
        mc "You know what? Even the most pious, forgiving soul who ever lived would take one glance at what Abel did to you and immediately know that what you did wasn't bad."
        scene 131_s44 with dissolve
        m "R-Really? *hic* You're not just trying to make me feel better?"
        scene 131_s45 with dissolve
        mc "Really. No one has or will ever will blame you for that. No one whose opinion matters anyway."
        scene 131_s44 with dissolve
        m "..."
        m "T-Thank you, [mc]."
        scene 131_s45 with dissolve
        mc "I love you."
        scene 131_s44 with dissolve
        m "*sniff* I love you too. I've loved you since the moment my eyes fell on you."
        scene 131_s45 with dissolve
        mc "Let me see your face."
        scene 131_s44 with dissolve
        scene 131_s46 with Dissolve(1.5)
        m "..."
        mc "You're so beautiful, you know that? No other girl even begins to compare."
        scene 131_s47 with dissolve
        m "*hic* He... hehe..."
        m "Y-You're just saying that because I'm a mess right now. My face is all puffy and my eyes are red. *laughs* I probably look like a tomato."
        scene 131_s48 with dissolve
        mc "*chuckles* That's the smile I wanted to see."
        scene 131_s47 with dissolve
        m "*giggles* [mc]..."
        scene 131_s48 with dissolve
        mc "Why don't we eat something? I'm sure you're hungry after all that. I know I'm starving."
        scene 131_s47 with dissolve
        m "Y-Yes."
        scene 131_s48 with dissolve
        mc "Sit here and enjoy the view. I'll be right back. There's gotta be a stall or something here. That man said this is a popular spot for tourists."
        stop music fadeout 1.0
        scene 131_s49 with Fade(1.5,0.5,0.5)
        play music "ocean.mp3" fadein 1.0 loop
        mc "Hey! Can I get two kebabs, please?"
        merchant "Kebabs? What's that? Never heard of it."
        mc "Come on. Everything so far has had the same name, and you're telling me kebabs aren't kebabs?!"
        mc "They're meat on a stick!"
        merchant "Ah, you mean the meat skewers! One copper each."
        if mc_coin >= 2:
            mc "Sure. Just give me two large ones."
        else:
            "How do you not have 2 coins at this point in the game?! Whatever, I'll let it slide."
        scene 131_s50 with Dissolve(1.5)
        mc "Hmm? Maia?! Where did you go?! Maia—"
        m "Over here!"
        mc "W-Where? I can't see you."
        scene 131_s51 with Dissolve(1.0)
        mc "Oh... behind the tree?"
        m "..."
        mc "*chuckles* What are you planning? You're not going to push me off the cliff, are you?"
        stop music fadeout 1.0
        scene 131_s52 with Dissolve(1.0)
        perception "You get closer. The leaves rustle. Then, suddenly, she steps from behind the tree—and thrusts something toward you."
        play music "hope/rose_of_may2.mp3" fadein 1.0 loop
        m "This... this is for you!"
        mc "..."
        m "I plucked them up from the ground while you were at the stall. There's lots of pretty flowers up here."
        m "I thought... I thought you might like them. I wanted to give you something after you've given me so much."
        mc "Maia..."
        scene 131_s53 with Dissolve(1.0)
        mc "Thank you. This is the best gift anyone's ever given me."
        m "Mhm!"
        mc "Come on. Let's eat. We've got kebabs—sorry, {i}meat skewers{/i}..."
        scene 131_s55 with Fade(1.0,0.5,1.0)
        m "Mmmm! That was really tasty, [mc]."
        m "But it was too much, though... I don't think I can finish the whole thing. I'm sorry. My stomach's not used to food this rich."
        m "*chuckles* I'm more used to eating sweets from Ren at the castle."
        scene 131_s54 with dissolve
        mc "Too much?! You're full from just one skewer? I could eat ten of these in one sitting!"
        scene 131_s55 with dissolve
        m "*giggles* Don't do that! You'll get fat. And then you won't be able to get down the mountain."
        m "*laughs* I'll have to... to roll you down. Like a barrel!"
        scene 131_s54 with dissolve
        mc "*chuckles* You're laughing at me? That's cold, Maia."
        mc "Say, what's it like? Back in your home. Your real home. Before Irda."
        scene 131_s56 with dissolve
        m "My home? You mean where I was born?"
        scene 131_s57 with dissolve
        if mc_maia_story:
            mc "Yes. You told me about it before, at the hideout. How Abel's men took you from your village."
        else:
            mc "Yes. Back at the hideout, I wanted you to tell me, but you refused."
        mc "Do you miss it?"
        scene 131_s56 with dissolve
        m "...I do."
        m "The sound of the river near our house. My mother's cooking. So many memories, but it's so... faded. It's like my brain stops me from grasping them."
        m "I can see them, but I can't touch them."
        scene 131_s55 with dissolve
        m "But I prefer being with you, [mc]. My home... it's probably not even there anymore. Not the way I remember it."
        scene 131_s54 with dissolve
        mc "Why say that? It hasn't been that long, has it? A few years? A few years isn't enough to erase a whole village."
        scene 131_s56 with dissolve
        m "My village was on surrounded by troops all year long. I don't remember everything, but it was placed on some borders."
        m "I hope I'm wrong, but... you know."
        scene 131_s57 with dissolve
        mc "You think it might have been attacked? Caught in some crossfire?"
        scene 131_s56 with dissolve
        m "Maybe. I don't know for sure... I haven't had any news since I was taken."
        m "My parents were old when I last saw them. My father's back was already hurting him. My mother's eyes were going cloudy... I don't know if anything's still there."
        scene 131_s57 with dissolve
        mc "Hmm..."
        mc "Once this is all over, let's go visit."
        mc "See if it's still standing. See if your parents are—"
        scene 131_s58 with dissolve
        m "..."
        mc "(Dammit! I just can't stop my mouth from running... she was smiling. And I had to bring this up. Idiot.)"
        scene 131_s55 with dissolve
        m "L-Let's do it! If it's with you, whatever happened... whatever we find... I can face it."
        m "You give me strength, [mc]. As long as you're with me, I can face anything."
        scene 131_s54 with dissolve
        mc "You don't need me to give you strength. It's already there, just buried deep. Hidden under all the fear and trauma."
        scene 131_s55 with dissolve
        m "Thank you."
        scene 131_s54 with dissolve
        call screen scene131_choice01 with dissolve

    else:
        scene 131_s17 with dissolve
        m "I don't want to. I want to stay here."
        scene 131_s16 with dissolve
        mc "Please, Maia. You'll feel a lot better if you go out with me."
        scene 131_s17 with dissolve
        mc "You have to breathe some air. You can't stay cooped up in here alone with your thoughts."
        m "..."
        mc "Please?"
        scene 131_s17 with dissolve
        m "I'm sorry."
        scene 131_s16 with dissolve
        mc "*sigh* (What do I do now?)"
        call screen scene129_choice11 with dissolve
        
label scene131_choice01_op1:
    $ scene131_choice01 = True
    mc "Tell me about Rebecca. You two were close, weren't you? Before everything fell apart?"
    scene 131_s55 with dissolve
    m "She's the best friend I ever had. *giggles* I was her personal servant, but she never treated me like one."
    m "She's the one that taught me how read and write. She stayed up late with me, night after night, helping me practice my letters."
    scene 131_s54 with dissolve
    mc "She sounds incredible."
    if not mc_princess_success:
        scene 131_s56 with dissolve
        m "She was. She is. S-She's still out there somewhere, isn't she? In the cellar? Waiting for us to save her?"
        scene 131_s57 with dissolve
        mc "I... I don't know."
        scene 131_s58 with Dissolve(1.0)
        m "Hm..."
    else:
        scene 131_s55 with dissolve
        m "She is. I hope they're treating her right at the palace."
        scene 131_s54 with dissolve
    mc "Do you miss her?"
    scene 131_s56 with dissolve
    m "A lot. I want to see her one day. Smiling and being mean to the guards and other servants."
    scene 131_s57 with dissolve
    if not mc_princess_success:
        mc "I see."
    else:
        mc "*chuckles* You two will get reunited soon. I'll make sure of it."
        scene 131_s55 with dissolve
        m "Thank you, [mc]. That means... that means more than you know."
        scene 131_s54 with dissolve
    call screen scene131_choice01 with dissolve

label scene131_choice01_op3:
    $ scene131_choice03 = True
    mc "What do you want to do after everything is over and back to normal?"
    scene 131_s55 with dissolve
    m "What do {i}you{/i} want to do, [mc]?"
    scene 131_s54 with dissolve
    mc "Me? I don't know. I haven't let myself think that far ahead. But... I'd like to rest for starters. *chuckles*"
    scene 131_s55 with dissolve
    m "That sounds nice. Maybe we could... find a place together? A small house somewhere. And we can get Crumps to live with us!"
    scene 131_s54 with dissolve
    mc "*chuckles* Alright, what else?"
    scene 131_s55 with dissolve
    m "A library? Not a big one—just a room full of books."
    scene 131_s54 with dissolve
    mc "A library? You don't strike me as a bookworm, Maia."
    scene 131_s55 with dissolve
    m "It's not for me. It's for the princess, when she comes to visit."
    scene 131_s54 with dissolve
    mc "*laughs* Ah... I see. But wouldn't you want to live in the castle again?"
    scene 131_s56 with dissolve
    m "No. I don't want anything to do with castles or palaces. I just want to live a quite life with people I love."
    scene 131_s57 with dissolve
    mc "Fair enough."
    call screen scene131_choice01 with dissolve

label scene131_choice01_op2:
    $ scene131_choice02 = True
    mc "I told you about my world, didn't I?"
    scene 131_s55 with dissolve
    m "You did! Tell me more about your world, [mc]. I want to know more!"
    scene 131_s54 with dissolve
    mc "It's hard to explain. It's so different from here. There were just... people. Billions of people. Living their lives. Going to work. Raising families. Complaining about the weather."
    scene 131_s55 with dissolve
    m "Billions? That's... that's so many. How do you even count that high?"
    scene 131_s54 with dissolve
    mc "*chuckles* We have machines for that. Machines for everything. Machines that fly. Machines that heal. Machines that let you talk to someone on the other side of the world as if they were standing right next to you."
    scene 131_s55 with dissolve
    m "That sounds like magic. It sounds more magical than magic."
    scene 131_s54 with dissolve
    mc "Maybe it is. Maybe that's all technology is—a different kind of magic."
    scene 131_s55 with dissolve
    m "...But you belong here now. With me. You know that, right?"
    scene 131_s54 with dissolve
    mc "I know. And that's what keeps me going. Knowing that you will always be there for me."
    m "Mhm~"
    call screen scene131_choice01 with dissolve

label scene131_choice01_op4:
    $ scene131_choice04 = True
    mc "Did you catch what was happening yesterday? With the guards who were with me?"
    scene 131_s56 with dissolve
    if mc_princess_success:
        m "Not fully... Are you working there now? With the princess?"
        scene 131_s57 with dissolve
        mc "Yes. She's... settling in nicely in her own bedroom."
        mc "You'd think nothing happened to her. The way she holds herself, the way she speaks—it's like the cellar never existed."
        scene 131_s56 with dissolve
        m "That's the princess. She's always been strong. Even when things were really hard, she never let it show. She always kept moving forward."
        m "She used to tell me that a princess doesn't have the luxury of breaking. That the kingdom needs her to be strong, even when she's falling apart inside."
        scene 131_s57 with dissolve
        mc "She's not the only one who's strong. You survived too. You're still here. Still smiling."
        scene 131_s56 with dissolve
        m "I had help. I had you. And Rebecca... Rebecca would want me to keep going. She'd want me to be happy."
        m "So, have you been helping the princess? With her recovery? With anything else?"
    else:
        m "Not fully... Are you working there now?"
        scene 131_s57 with dissolve
        mc "It's... complicated. I'm with Queen Hannah now. She's been working with King Hod to plan the retaking of Irda."
        scene 131_s55 with vpunch
        m "The queen is with you?! Queen Hannah?! I thought she wan in hiding!"
        scene 131_s54 with dissolve
        mc "I was as surprised as you are right now. Apparently, she made the journey all the way here from some fishing village in Eurina."
        scene 131_s55 with dissolve
        m "Oh Gods... That's... that's wonderful, [mc]! Rebecca will be so happy!"
        scene 131_s54 with dissolve
        mc "...She would."
        scene 131_s56 with dissolve
        m "So... have you been helping her majesty?"
    scene 131_s57 with dissolve
    mc "Yup. I was assigned to take care of those same bandits that came yesterday. They'd been terrorizing the market district in Nahraya for years."
    scene 131_s56 with dissolve
    m "Oh, so that's why they were so angry... They thought you would come hurt them, so they came there? To the house?"
    scene 131_s57 with dissolve
    mc "Not really. They were just 'making leverage'. Taking advantage of me, basically."
    mc "They knew I had a connection to the king, so they wanted to negotiate from a position of strength."
    if mc_killed_vic:
        scene 131_s58 with Dissolve(1.0)
        m "S-So... they were going to hurt us? Th-that's why... that's why you hurt them back? All of them?"
        mc "Yes. And anyone else who would dare put their hands on you will get the same fate. I won't hesitate. I won't show mercy."
        scene 131_s55 with Dissolve(1.0)
        m "*chuckles* I... feel safer now that you say that~"
        m "It's... it's strange. I should be scared of you, but I'm not. Because I know you'd never hurt me."
        scene 131_s54 with dissolve
    else:
        scene 131_s55 with dissolve
        m "Well, I'm glad no one got hurt, [mc]. You talked down the mean guy like nothing! He was so scary, with all his men and his threats, and you just... sat there. Calm."
        m "You didn't even raise your voice. You just... talked. And he listened. How did you do that?"
        scene 131_s54 with dissolve
        mc "*chuckles* Thank you. I've learned that violence is a tool, not a solution. Most of the time, words are enough. You just have to find the right ones."
        scene 131_s55 with dissolve
        m "That's... that's smart. I wish I could do that. Talk to people like that. Make them listen and understand."
        m "I'll make sure to remember that! I'll practice. And one day, I'll talk down a bandit all by myself. Just you wait."
        scene 131_s54 with dissolve
        mc "*laughs* Don't get too excited."
    call screen scene131_choice01 with dissolve

label scene131_choice01_op5:
    scene 131_s59 with Dissolve(1.0)
    m "Prrr..."
    mc "It's getting cold, huh? Weird—you'd think a desert would always be hot. Even during winter."
    scene 131_s60 with dissolve
    m "The desert gets a lot colder during nighttime. It's because there's no trees, and no water to hold the warmth. So all the heat from the day just... escapes."
    m "My father taught me that. He was always reading books about the natural world. He said understanding things are the key to surviving them."
    scene 131_s61 with dissolve
    mc "..."
    scene 131_s62 with dissolve
    m "Is... is that boring?"
    scene 131_s63 with dissolve
    mc "No. Not at all. I wish you'd talk like that even more."
    scene 131_s61 with dissolve
    m "Hehe~"
    mc "Time to go back?"
    scene 131_s60 with dissolve
    m "Yes! Thank you for taking me out, [mc]!"
    scene 131_s61 with dissolve
    mc "You're welcome. We should do this more often."
    scene 131_s60 with dissolve
    m "I'd like that. More than anything."
    scene 131_s61 with dissolve
    scene 131_s64 with Fade(0.5,0.5,0.5)
    perception "You descend the mountain—this time using your own body's natural strength. Maia follows beside you, her hand in yours."
    stop music fadeout 3.0
    if mc_killed_reham:
        scene 131_s70 with Fade(1.3,1.0,1.3)
        play music "kitchen.mp3" fadein 1.0 loop
        mc "You alright, Maia? Can I leave you here? I have to go and report to the palace."
        scene 131_s71 with dissolve
        m "I am. I feel... light. Like something heavy has been lifted off my chest."
        scene 131_s70 with dissolve
        mc "You're being honest, right? Because if you need me to stay—"
        scene 131_s72 with dissolve
        play sound "se_sfx/blowjob/kiss1.mp3" 
        m "*mwah*"
        scene 131_s71 with Dissolve(1.0)
        m "That should tell you."
        scene 131_s70 with dissolve
        mc "Message received! Loud and clear. I'll tell the guards to leave at least one person around, just in case."
        scene 131_s71 with dissolve
        m "Goodbye, [mc]! I'll be waiting for you! I'll even try to make you something!"
        scene 131_s70 with dissolve
        mc "*chuckles* Just don't burn the house down."
        mc "Actually... why don't you come with me to the palace? Why stay here alone?"
        scene 131_s71 with dissolve
        m "N-No. Thank you, [mc]. But I would prefer to stay here. It's like having my own house!"
        m "I always dreamt of that."
        scene 131_s70 with dissolve
        mc "I see. Hold on to that dream yet, because you deserve a much bigger house than this."
        scene 131_s71 with dissolve
        m "*giggles* A-Alright~"
        scene 131_s70 with dissolve
        jump scene132

    scene 131_s65 with Fade(1.3,1.0,1.3)
    play music "kitchen.mp3" fadein 1.0 loop
    yasmine "Welcome back, love birds. I saw you coming from the window. You two look... happy."
    yasmine "Dinner's ready, by the way. I made extra. Thought you might be hungry after who knows what you two did alone~"
    scene 131_s66 with dissolve
    reham "Mother!"
    scene 131_s67 with dissolve
    m "*gag* S-Sorry, miss. I would puke if I ate anymore."
    scene 131_s68 with dissolve
    reham "Where did you even go?"
    scene 131_s69 with dissolve
    m "[mc] took me to a mountain!"
    m "It was all up above—we almost touched the sky. You could see the whole city, and the desert, and everything."
    scene 131_s68 with dissolve
    reham "*chuckles* Ah, Eunice's Peak? I visited there once when I was little."
    reham "I still remember how sore my legs were the next day. I couldn't walk for a week."
    scene 131_s70 with Dissolve(1.0)
    mc "You alright, Maia? Can I leave you here? I have to go and report to the palace."
    scene 131_s71 with dissolve
    m "I am. I feel... light. Like something heavy has been lifted off my chest."
    scene 131_s70 with dissolve
    mc "You're being honest, right? Because if you need me to stay—"
    scene 131_s72 with dissolve
    play sound "se_sfx/blowjob/kiss1.mp3" 
    m "*mwah*"
    scene 131_s71 with Dissolve(1.0)
    m "That should tell you."
    scene 131_s70 with dissolve
    mc "Message received! Loud and clear. I'll tell the guards to leave at least one person around, just in case."
    scene 131_s73 with Dissolve(1.0)
    mc "Goodbye, Yasmine. Goodbye, Reham... and Rohan. Eat my share of dinner. I have to go."
    rohan "Hmph... you better stay there."
    jump scene132

label scene129_choice11_op3:
    $ s129_maia_choice3 = True
    mc "Maia... it's alright. You're safe now. No one can hurt you here."
    empathy "Her fingers press a little deeper into her legs. Whatever is going on inside her head is far beyond the reach of simple reassurance right now."
    mc "(She's not hearing me. I'm just... talking to a wall.)"
    call screen scene129_choice11 with dissolve

label scene129_choice11_op4:
    $ s129_maia_choice4 = True
    sensation "You try your hardest to start crying, you somewhat succesd as your eyes begin to tear up."
    mc "M-Maia... Please talk to me..."
    m "..."
    scene 131_s14 with Dissolve(1.0)
    m "...Why are you crying?"
    scene 131_s15 with dissolve
    mc "Because I... I want to make you feel better. I want to so badly, but I don't know how."
    scene 131_s14 with dissolve
    m "...Don't cry. Please."
    scene 131_s15 with dissolve
    mc "(That was so stupid! What the hell?! It's like I was making fun of her... I hope she didn't think of it that way.)"
    call screen scene129_choice11 with dissolve

label scene129_choice11_op5:
    $ maia_gone = True
    mc "(...Maybe she'll get over it on her own.)"
    scene black with Dissolve(2.0)
    if mc_killed_reham:
        perception "You linger for a second longer, then quietly step back toward the door and out of the house."
        shiver "You shiver, you feel like you just made a terrible mistake."
        jump scene132
    perception "You linger for a second longer, then quietly step back toward the door."
    scene 131_s22 with Fade(1.0,1.0,1.0)
    yasmine "Any news?"
    scene 131_s23 with dissolve
    mc "Sorry, no. She's... she might need some time alone."
    scene 131_s22 with dissolve
    yasmine "Are you sure, [mc]? She might really need someone to talk to."
    scene 131_s23 with dissolve
    mc "I'll trust my choice for now."
    scene 131_s22 with dissolve
    yasmine "Hmm... I hope you're not making a mistake you can't come back from."
    scene 131_s23 with dissolve
    mc "I need to return to the palace. Is that okay with you two?"
    scene 131_s22 with dissolve
    yasmine "Go ahead, [mc]. We'll take care of ourselves. I saw a guard outside, it seems they'll stay here for a while."
    scene 131_s23 with dissolve
    jump scene132

label scene132:
    stop music fadeout 1.5
    scene 132_s1 with Fade(1.3,1.0,1.3)
    play music "talkingAmbiance.mp3" fadein 1.0 volume 0.4 loop
    if mc_harem_maia_true:
        mc "*gag* (Why do I feel terrible? Is it because of running up the mountain? Or was the meat spoiled? That vendor looked trustworthy, but you never know with street food.)"
    else:
        ""
    scene 132_s2 with Dissolve(1.0)
    market_man1 "There he is! That's him! The foreigner with the metal hand!"
    market_woman2 "It's really him!"
    scene 132_s3 with Dissolve(1.0)
    mc "Huh?!"
    mc "I didn't do anything! Whatever it is, I can explain—"
    scene 132_s4 with Dissolve(1.0)
    market_man1 "Thank you, sir."
    scene 132_s36 with dissolve
    mc "You're thanking me? What for?"
    scene 132_s14 with dissolve
    market_woman1 "It was because of you that the Ohm is no longer doing their dirty business, isn't it? The whole district is talking about it!"
    market_woman1 "The king's guards came through this morning and announced it."
    scene 132_s36 with dissolve
    mc "Oh. *chuckles* Well... I had something to do with it. I won't deny that."
    if not mc_killed_vic:
        mc "Though it wasn't entirely my doing. Vic, the leader, was on his way to change the group too. Just needed protection."
    scene 132_s15 with dissolve
    man_in_house "Hey, that's my neighbour! He lives close to me!"
    man_in_house "You have no idea how grateful we are, sir. Those thugs were a plague on everyone in these parts. The guards were always turning a blind eye to them for some reason."
    man_in_house "They took advantage of the poor and needy. Men, women, even children!"
    scene 132_s4 with dissolve
    market_man1 "Indeed. Their hands knew no mercy. They'd take everything—your coin, your home, your dignity. And if you still couldn't pay, they'd take your family."
    market_man1 "I know a man whose daughter was sold to one of their... establishments. He never saw her again."
    scene 132_s36 with dissolve
    mc "How did the news get so fast?"
    scene 132_s14 with dissolve
    market_woman1 "The guards told the market master, who told the vendors, who told everyone else. Word spreads fast in this district."
    scene 132_s16 with dissolve
    market_woman2 "He's handsome too~ I didn't expect that."
    scene 132_s17 with dissolve
    market_woman3 "Thank you, sir. I can rest easy knowing my child will grow in a safer enivronment."
    scene 132_s36 with dissolve
    if mc_karma >= 5:
        mc "I'm glad I could help you all. I didn't know they had such a grip on this district. How many lives they'd ruined."
        mc "I just did what anyone should have done."
        scene 132_s4 with dissolve
        market_man1 "No, sir. Not anyone. Plenty of people should have, but they didn't. You did. That makes you a hero."
    else:
        mc "I didn't do it for a 'thank you'. I need more than that."
        scene 132_s4 with dissolve
        market_man1 "O-Of course! Whatever you need, sir. My stall will have a permanent discount for you."
        scene 132_s16 with dissolve
        market_woman2 "Mine too!"
        scene 132_s36 with dissolve
        mc "That's more like it."

    scene 132_s6 with Dissolve(1.0)
    mc "(H-Hold on, is that Negumi!?)"

    if mc_killed_vic:
        scene 132_s7 with dissolve
        market_woman4 "What are you all even praising him for? Did you not see what happened? Were you not watching from your windows like everyone else?"
        scene 132_s8 with dissolve
        market_man1 "What are you talking about? He stopped the Ohm. The guards said—"
        scene 132_s9 with dissolve
        market_woman4 "He killed them all! I saw it! I watched the guards carry out the bodies."
        scene 132_s8 with dissolve
        market_man1 "H-He probably didn't have a choice! What if they attacked him first?"
        scene 132_s9 with dissolve
        market_woman4 "Did you even see the bodies?! Some of them were so disfigured you couldn't tell they were human anymore!"
        scene 132_s22 with dissolve
        market_woman3 "That... that's terrible. I didn't know. The guards didn't say—"
        scene 132_s8 with dissolve
        mc "I did what I had to do."
        scene 132_s10 with dissolve
        market_woman4 "You're a devil! A devil masquerading as a hero! You didn't stop them—you slaughtered them!"
        scene 132_s11 with dissolve
        market_woman2 "I... I'm still grateful. But..."
        scene 132_s13 with Dissolve(1.0)
        market_woman3 "I can't believe I almost invited him to my shop... I have children. I almost let a murderer into my home. I almost—"
        empathy "They begin leaving, one by one. Their faces still show subtle gratitude, but more than that, there is fear. They are terrified of what you are."
        minthra "Do not let them get to you. You did the right thing. None of this will matter soon."
    else:
        scene 132_s18 with Dissolve(1.0)
        man_in_house "I heard you talked them down. I didn't even think those thugs could be reasoned with."
        scene 132_s19 with dissolve
        mc "Uhh... yeah, the new one in charge is more flexible than the previous one."
        mc "Vic is different. He's smarter. He saw the writing on the wall and chose to adapt rather than die."
        mc "Well, I don't know yet. Promises are cheap, but he should do better. He knows what'll happen if he doesn't."
        scene 132_s20 with dissolve
        market_woman3 "If there's ever anything you need, you come find us."
        scene 132_s12 with dissolve
        market_man1 "Here, here! The hero of the market district!"
        empathy "A small cheer goes up from the gathered crowd. Hope radiates from their tired faces."

    scene 132_s23 with Fade(1.5,0.5,0.5)
    mc "Negumi!"
    if mc_killed_vic:
        scene 132_s24 with dissolve
        negumi "Oof. That was tough. What was that about you killing a bunch of people?"
        scene 132_s23 with dissolve
        mc "You don't need to know the details, just know that I was in the right."
        mc "And what are you doing here? I was looking for you!"
    else:
        mc "What are you doing here?! I was looking for you!"
    mc "Honestly, I thought you were dead. Or maybe arrested."
    scene 132_s24 with dissolve
    negumi "Miss me?"
    scene 132_s23 with dissolve
    stop music fadeout 1.0
    mc "I—"
    play sound "sound_effects/woosh2.mp3"
    pause(0.3)
    play music "side_event2Talking.mp3" fadein 1.0 loop
    scene 132_s25 with vpunch
    negumi "Of course you have! How could you not? For it is not the sun that lights up the desert, it is the eternal flame that burns in my heart, a beacon that calls all who are lost to find their way home!"
    negumi "Yes... it is {i}I{/i} whom all seek. The one who illuminates the darkness. The one who—"
    scene 132_s23 with Dissolve(1.0)
    mc "Alright, alright! I get it. I see you still haven't changed."
    mc "But seriously—I really missed you. More than I thought I would."
    mc "I could have used your help more than once. Where did you go after... after the market incident?"
    scene 132_s24 with dissolve
    negumi "I snuck away during the chaos. If you could see the smoke rising from the buildings... Oooho~ It makes me shiver just remembering it."
    negumi "The flames. The screaming. Everyone was scrambling as everything was turning to ash. I could practically just stroll."
    scene 132_s23 with dissolve
    mc "It made you shiver? Negumi... do you not feel anything for what happened back there?"
    mc "I didn't see it, but others said that the whole market turned to smithereens. People got hurt. People who had nothing to do with it."
    scene 132_s26 with dissolve
    negumi "And? Should I feel empathy for them? They were trying to kill us, [mc]. You. That girl. Me."
    negumi "We would be dead if I hadn't acted. People get hurt and die all the time, but they're not my burden. They're the cost of survival. A... necessary sacrifice."
    scene 132_s27 with dissolve
    mc "A necessary sacrifice?"
    scene 132_s26 with dissolve
    negumi "Yes."
    scene 132_s27 with dissolve
    mc "...Anyway, did you leave Irda afterwards?"
    scene 132_s24 with dissolve
    negumi "Not immediately. I went to the guild first. I had... unfinished business. I wanted to see if I could steal some coin from Eireen."
    scene 132_s23 with dissolve
    mc "You tried to steal from the guild!?"
    scene 132_s26 with dissolve
    negumi "Don't blame me! She barely paid me anything during my time slaving there."
    negumi "But I'm glad I stopped before entering. I sensed something from inside. A murderous mana, thick and suffocating. It was coming from the guild hall."
    scene 132_s27 with dissolve
    mc "Murderous mana? What does that even mean? Is that one of your dramatic expressions?"
    scene 132_s26 with dissolve
    negumi "I can sense killing intent—it's a skill I developed during my study. A survival mechanism, really."
    negumi "The presence inside the guild was... potent. It was that of a mage. As ashamed as I am to admit it, they were perhaps as strong as I am."
    scene 132_s27 with dissolve
    mc "A mage... could it have been that old elven mage from the guild evaluation?"
    scene 132_s26 with dissolve
    negumi "No idea who that is. I wasn't at any evaluation."
    scene 132_s27 with dissolve
    mc "He was pretty new. Anyway, I'm glad you're here. I could use someone like you. Someone who... well, someone who can do what needs to be done."
    scene 132_s24 with dissolve
    negumi "That depends, big man. Is coin involved?"
    scene 132_s23 with dissolve
    mc "Naturally."
    scene 132_s28 with dissolve
    negumi "Very well. Then consider this mage at your service. Be honored!"
    scene 132_s23 with dissolve
    mc "...Ahuh."
    mc "You busy at the moment?"
    scene 132_s29 with Dissolve(1.0)
    negumi "No. I tried joining the adventuteres' guild here, but it turns out, they don't even have one. Just a board where locals put whatever they want on."
    negumi "It's all just boring tasks with little pay, but it gets me going."
    scene 132_s30 with dissolve
    mc "Alright. Then come with me to the palace. I might be able to get you set up with proper work."
    scene 132_s29 with dissolve
    negumi "The palace? The {i}royal{/i} palace?"
    scene 132_s30 with dissolve
    mc "That's the one. Just please, don't do any of your... bits."
    scene 132_s29 with dissolve
    negumi "Bits?"
    scene 132_s30 with dissolve
    mc "You know... when you start posing and acting all weird."
    scene 132_s29 with dissolve
    negumi "Acting weird?"
    scene 132_s30 with dissolve
    mc "Don't tell me you're doing it unironically... You really think you're some kind of legendary mage."
    scene 132_s29 with dissolve
    negumi "I don't {i}think{/i} I am. I {i}know{/i} I am."
    scene 132_s30 with dissolve
    mc "*sigh* Whatever. Come on. Just stay quiet in the palace."
    scene 132_s31 with Fade(0.5,0.5,0.5)
    negumi "What happened to that woman you rescued? The one from the market. Maria? Maya?"
    mc "Maia. She's doing fine. She's... she's been through a lot. But she's safe. And... thank you. For telling me about it."
    negumi "Of course. People call me coin-motivated all the time, but I always have time to help the weak, the meek, and the useless."
    mc "..."
    negumi "That was a joke. You're supposed to laugh."
    stop music fadeout 1.0
    scene 132_s32 with Fade(1.3,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    n_guard "Halt! You are permitted to enter, sir. But we are unfamiliar with this woman."
    negumi "I'm no mere woman! I am—"
    mc "She's with me. I trust her. She's a powerful mage. She helped me in Irda, and she'll be helping me here."
    scene 132_s33 with dissolve
    n_guard "Very well, sir. If you vouch for her. But protocol must be followed. Write your information on the registry, and hand over your staff before entering."
    negumi "M-My staff?! But—"
    scene 132_s35 with dissolve
    mc "Do it, Negumi. It's just for now. You'll get it back."
    scene 132_s34 with dissolve
    negumi "Hmph. Fine. It's not as if my power is concealed in my staff. The staff's purpose is merely to concentrate my spells—not hold them."
    negumi "My magic comes from within. From the depths of my soul. From the ancient and terrible forces that—"
    scene 132_s35 with dissolve
    mc "Negumi. The staff. Hand it over."
    stop music fadeout 1.0
    scene 133_s1 with Fade(1.0,1.0,1.0)
    play music "ambiance/king_in_red.mp3" fadein 1.0 volume 0.7 loop
    negumi "To, too, toa, toa... To-to-toa..."
    mc "What the hell are you saying? Are you casting something?!"
    negumi "It's singing. What, I can't sing too? Must I be silent as well as disarmed? Must I shuffle through these halls like a ghost?"
    mc "Just... just be quiet. Please. Try to be normal for {i}five minutes{/i}."
    scene 133_s2 with Dissolve(2.0)
    n_guard "Are you looking for Ambassador Sanoud, sir?"
    scene 133_s3 with dissolve
    mc "I am. Is he still here?"
    scene 133_s2 with dissolve
    n_guard "He left a while ago. You can find him in the throne room now."
    scene 133_s3 with dissolve
    mc "The throne room? What's happening?"
    scene 133_s2 with dissolve
    n_guard "An important diplomat from the Zents has arrived."
    scene 133_s4 with dissolve
    negumi "Meeting the king... The king of Nahraya... In his own throne room... Heh. Hehehaha!"
    negumi "This is my chance. This is where I reveal myself to the world."
    scene 133_s5 with dissolve
    mc "I'm starting to regret bringing you along."
    mc "*sigh* Come on. To the throne room."

    scene 133_s6 with Fade(1.3,1.0,1.3)
    n_guard "Halt. No one is permitted inside the throne room at the moment."
    n_guard "His royalty is in negotiations with the Zentian diplomat, and has requested not to be disturbed."
    scene 133_s7 with Dissolve(1.0)
    mc "It's alright. We can wait."
    mc "We can visit the baths, Negumi. What do you think? Or we could—"
    scene 133_s8 with dissolve
    n_guard "What do you think you're doing?! Halt! Stop right there!"
    mc "Negumi?!"
    stop music
    play sound "sound_effects/doors/large_door.mp3"
    scene 133_s9 with vpunch
    mc "What the FUCK, Negumi!"
    play music "negumi.mp3" fadein 1.0 loop
    perception "The throne room falls silent. King Hod turns his head slowly. Ambassador Sanoud's jaw drops. The Zents ambassador pauses mid-sentence. Every guard in the room reaches for their weapon."
    scene 133_s10 with Dissolve(1.0)
    negumi "Welcome, mortals! I shall permit you to gaze upon me! For I am Negumi, the sorceress of the eternal flame! Master of the arcane arts!"
    scene 133_s11 with dissolve
    amb "Guards! Who is this woman?! Seize her!"
    scene 133_s10 with dissolve
    negumi "You wish to lay hands on me? You wish to test the power of my flames? Very well! Come! Taste the—"
    scene 133_s12 with Dissolve(1.0)
    zent "This one. The small one. Who is she?"
    scene 133_s13 with dissolve
    king "I was about to ask the same question. Sanoud, is she one of yours?"
    amb "N-No, your highness! I have never seen her before! She must have come with the foreigner, with [mc], I don't know how she got past the guards—"
    negumi "I am here on my own merit, baldy."
    scene 133_s14 with dissolve
    zent "She has fire. A warrior's fire."
    zent "I like her. This one... she has the heart of a beastman. In a human's body."
    scene 133_s17 with Dissolve(1.0)
    amb "S-Sir? What are you saying? She isn't meant to be here."
    scene 133_s16 with dissolve
    zent "*laughs* Your negotiations were boring me, Hod. Too many words, no teeth. This... this is worth the journey."
    scene 133_s17 with dissolve
    king "...I see. Guards, stand down."
    king "It appears our uninvited guest has made a favorable impression on our other guest."
    amb "But, my liege! She interrupted a diplomatic session! She threatened the guards! She—"
    king "Stand down, Sanoud. That's an order."
    scene 133_s47 with Dissolve(1.0)
    mc "(What the hell?)"
    scene 133_s18 with dissolve
    negumi "At last! Someone who recognizes greatness when they see it! You, weird looking lion-man, have excellent taste."
    scene 133_s19 with dissolve
    zent "*laughs* I like her! I really do! Your name, little flame?"
    scene 133_s18 with dissolve
    negumi "I am Negumi! The most powerful of all fire magicians!"
    scene 133_s47 with dissolve
    king "Stand forward, [mc]. Is she with you?"
    scene 133_s20 with Dissolve(1.0)
    mc "She's with me. She's always like this."
    scene 133_s21 with dissolve
    if mc_knelt_hod:
        if mc_killed_vic:
            king "It seems trouble follows you like a shadow. First you bring down a criminal syndicate in a single day, and now you arrive with a mage who bursts through my doors like a conquering hero."
        else:
            king "It seems trouble follows you like a shadow. First you reform a criminal syndicate in a single day, and now you arrive with a mage who bursts through my doors like a conquering hero."
    else:
        if mc_killed_vic:
            king "It seems trouble follows you like a shadow. First you refuse to kneel, then you bring down a criminal syndicate in a single day. And now you arrive with a mage who bursts through my doors like a conquering hero."
        else:
            king "It seems trouble follows you like a shadow. First you refuse to kneel, then you reform a criminal syndicate in a single day. And now you arrive with a mage who bursts through my doors like a conquering hero."
    king "But it matters not now. As you can see, the Zentian diplomat is... fascinated with her. Against all odds."
    scene 133_s22 with dissolve
    zent "Hmm... Yes. This one. This small flame."
    zent "Perhaps... she can do it."
    amb "Sir, are you implying—? Surely you can't mean—?"
    scene 133_s24 with Dissolve(1.0)
    zent "Yes. She had the courage to enter this room and announce herself like a herald of the Gods."
    zent "I think she has the courage to slay them."
    scene 133_s25 with Dissolve(1.0)
    king "We already spoke of that, Zentian. The fragile alliance between us won't last long if you keep bringing that up."
    scene 133_s26 with dissolve
    zent "So be it. If none here have the courage to face the threat that strangles our trade and starves my people, then I am out."
    scene 133_s23 with Dissolve(1.0)
    mc "Hold on, sir. What exactly are you talking about?"
    scene 133_s24 with dissolve
    amb "Don't get involved, [mc]! This is beyond you!"
    zent "There is a problem between our peoples. Old as time. Two giants live between our borders. Twin monstrosities. They claim the northeastern pass as their territory."
    zent "They sleep for a decade. When they wake, they feed."
    zent "Before, this was not such a problem. But last month... They woke. And they have shut off the trade route completely. No caravan can pass."
    zent "Because of that... my people starve."
    scene 133_s23 with dissolve
    mc "Giants? {i}Actual{/i} giants?"
    mc "What exactly do you mean? You want to get rid of them?"
    scene 133_s16 with Dissolve(1.0)
    zent "Yes. Permanently. Only then will the pass open again. Only then will the alliance between our peoples be possible."
    zent "But the men here think it is useless. So many soldiers sent to their deaths against creatures that cannot be killed."
    zent "I offered to send my finest warriors. But without Nahraya's support, even my bravest would fall."
    scene 133_s25 with dissolve
    king "And many more will be lost if we continue sending soldiers to their deaths. I have lost three battalions to those monsters."
    king "We can afford to lose that trade route. There are many others between us—longer routes, but routes nonetheless. It isn't worth this cost."
    scene 133_s26 with dissolve
    zent "Your weakness disgusts me. You speak of loss as if my people have not lost more."
    scene 133_s25 with vpunch
    king "Watch your mouth, Zentian! You are a guest in my palace! You shall show proper respect, or you shall leave!"
    scene 133_s27 with Dissolve(1.0)
    negumi "We'll do it."
    scene 133_s48 with dissolve
    amb "What?!"
    scene 133_s27 with dissolve
    negumi "Why not? How hard can it be? I'll burn them to ash and scatter their remains across the heartless desert."
    scene 133_s48 with dissolve
    amb "You shut your mouth, woman! Who do you think you are?!"
    zent "I had a feeling you would say that. You are not like the men here, I sense little fear from you."
    zent "This one. This small flame. She will do what your battalions could not. She will slay the giants. And I will hold you to your word, Hod. If she succeeds—the alliance stands."
    scene 133_s28 with dissolve
    mc "Negumi, we don't even what we're walking into..."
    scene 133_s27 with dissolve
    negumi "It doesn't matter! The great Negumi will slay those giants and claim her name among history's greatest!"
    scene 133_s48 with dissolve
    zent "*chuckles* I wish you luck, little flame. You will need it."
    scene 133_s29 with Dissolve(1.0)
    zent "We have nothing more to discuss, Hod. The terms are set. I will await news of her victory... or her death."
    king "Leave. Your disrespect is noted. And none shall leave to fight any giants. Not her, not anyone. This discussion is over."
    stop music fadeout 1.0
    scene 133_s30 with Fade(1.0,1.0,1.0)
    play music "ambiance/king_in_red.mp3" fadein 1.0 loop
    amb "What the hell was that, you two?! Are you begging to be executed?! Do you have any idea what you've just done?!"
    scene 133_s31 with dissolve
    negumi "What he said is true. Why do you all sound so defeated?"
    scene 133_s30 with dissolve
    amb "Because we already went through this! Do you know how many soldiers were lost to those giants?! Thousands! All dead. All for nothing."
    amb "All because of a single trade route."
    scene 133_s31 with dissolve
    scene 133_s32 with Dissolve(1.0)
    king "I doubt our talk was going anywhere. But since there might have been a sliver of hope which you two have now destroyed..."
    king "Therefore, you must be punished."
    scene 133_s33 with dissolve
    amb "M-My liege?!"
    negumi "*sigh* Here we go again..."
    scene 133_s32 with dissolve
    king "You interrupt my meeting. You spout nonsense from your mouth. You make vows to fight without my blessing. You have embarrassed me in front of a foreign diplomat."
    king "I would have excused you, [mc]. But since you were the one to bring her here, I cannot but punish you too."
    scene 133_s33 with dissolve
    mc "...What kind of punishment?"
    scene 133_s32 with dissolve
    king "You want to fight giants? ...Fine. Do it! Both of you. You leave at dawn."
    scene 133_s33 with dissolve
    if mc_princess_success:
        amb "My liege?! You're sending them to their deaths! What would princess Rebecca say if [mc] was killed?!"
    else:
        amb "My liege?! You're sending them to their deaths! What would queen Hannah say if [mc] was killed?!"
    amb "They came here for an alliance, not to die in fighting creatures that have slaughtered thousands!"
    scene 133_s32 with dissolve
    king "If she is to rule one day, she will understand."
    scene 133_s33 with dissolve
    amb "Is... is this absolute, my liege? Is there no chance for you to reconsider?"
    scene 133_s32 with dissolve
    king "It is. You may leave the throne room."
    scene 133_s33 with dissolve
    amb "...As you wish."
    scene 133_s34 with Fade(1.3,1.0,1.3)
    negumi "I don't get it. He just told us to do what I wanted to do in the first place."
    mc "*sigh* Because, Negumi. We might actually die."
    negumi "Don't worry. That might be the case if you were alone, but you're with me."
    scene 133_s35 with Dissolve(1.0)
    if mc_princess_success:
        amb "This is bad. This is so, so bad. What am I going to tell princess Rebecca?"
    else:
        amb "This is bad. This is so, so bad. What am I going to tell queen Hannah?"
    scene 133_s36 with dissolve
    amb "*sigh* Listen up, you two. I won't lie to you, you're basically walking into your deaths."
    amb "This... this isn't something you can do, not the way it's been presented. However, there is a chance for you. I will not say it outright, but... you can, you know."
    negumi "Are you telling us to run? To flee like cowards?"
    scene 133_s39 with Dissolve(1.0)
    amb "Quiet! Keep your voice down! I'm telling you to keep your head on. Be smart."
    amb "If things get out of hand, if it's clear you can't win, don't try to push it. Don't be heroes."
    scene 133_s37 with dissolve
    amb "His royal highness doesn't want you to die. He's not a cruel man. He's a proud man who was backed into a corner by a foreign diplomat and a loud-mouthed woman."
    amb "He wants you to fight—to show that Nahraya still has courage. But he doesn't want your blood on his hands, espcially you, [mc]."
    scene 133_s38 with dissolve
    mc "If what you said is true about the giants killing thousands... then what chance do we have to even run?"
    scene 133_s37 with dissolve
    if mc_princess_success:
        amb "*sigh* I truly don't know. But I'll be praying for you. For both of you. For the princess's sake."
    else:
        amb "*sigh* I truly don't. But I'll be praying for you. For both of you. For the Queen's sake."
    scene 133_s40 with dissolve
    negumi "We don't need your prayers, baldy. We will do it."
    scene 133_s39 with dissolve
    amb "You are so lucky to have the Zentian diplomat's favor. Otherwise, you'd already be rotting in the deepest part of the dungeon."
    scene 133_s37 with dissolve
    amb "*sigh* Go and rest. Both of you need your strength. The loud-mouthed woman will be escorted out. You, [mc], return to your room."
    amb "I'll arrange a suit of armor for you. What you're wearing now won't withstand a simple sword attack, let alone a giant's fist."
    scene 133_s38 with dissolve
    mc "New armor? I'd appreciate that. The last set I had was... well. It didn't survive Irda."
    scene 133_s40 with dissolve
    negumi "Can I not stay with [mc]? Where do you expect me to go?"
    scene 133_s39 with dissolve
    amb "I don't care. What I care about is you showing up at dawn sharp. Don't risk angering his royal highness even more than you already have."
    scene 133_s40 with dissolve
    negumi "Fine. You better have my staff in good condition."
    scene 133_s37 with dissolve
    amb "I will send Flint to brief you further tomorrow."
    amb "He'll have maps of the pass. Intelligence on the giants. Whatever we've managed to gather from the survivors."
    scene 133_s38 with dissolve
    mc "What about Alex? She should know about this."
    scene 133_s37 with dissolve
    amb "Alexandria is doing her own task right now. And even if she wasn't, I would not allow her to accompany you under any circumstances. She is of great value to us."
    scene 133_s38 with dissolve
    mc "Right. Probably for the best."
    scene 133_s41 with Dissolve(1.0)
    negumi "Farewell, [mc] and the bald man."
    mc "You too, Negumi."
    scene 133_s42 with Dissolve(2.0)
    mc "(Huh?)"
    mc "(Is she... is she shaking? So it was an act. All of it. Or maybe... part of it?)"
    empathy "Her body shakes uncontrollably. The act finally wears off. All of it peels away, leaving behind her true self."
    mc "(But why, Negumi? What are you trying to prove?)"
    stop music fadeout 2.0
    scene 133_s43 with Fade(1.0,1.0,1.0)
    if mc_princess_success:
        mc "Becky?"
    else:
        mc "Your Majesty?"
    mc "(She's sleeping. Better not wake her up, or even tell her what I'm doing tomorrow morning. She's most likely not allowing it.)"
    mc "(The less she knows the better.)"
    scene 133_s44 with Fade(1.3,1.0,1.5)
    play music "nature.mp3" fadein 1.0 volume 0.5 loop
    mc "*yawn* Time to go. Looks like she's gone too. Hopefully no one told her."
    scene 133_s45 with Dissolve(1.0)
    nimah "Good morning, Master. We have your new armor ready for you."
    scene 133_s46 with dissolve
    mc "Whoa! W-What are you doing here? Were you standing there all night?!"
    scene 133_s45 with dissolve
    nimah "I didn't mean to scare you, Master. I was instructed to wait for you when you wake up. And I have been standing here for only three hours."
    scene 133_s46 with dissolve
    mc "{i}Only?{/i} Anyway.... my armor is ready? That quickly?"
    scene 133_s45 with dissolve
    nimah "It was already available. This particular suit was made for first rank recruits of his royal highness's special guard."
    scene 133_s46 with dissolve
    mc "Alright, where is it?"
    scene 133_s45 with dissolve
    nimah "I will go ahead and inform the other servants, two of them a will arrive to you shortly."
    scene 133_s46  with dissolve
    jump scene134

label scene134:
    scene 134_s1 with Fade(1.0,1.0,1.0)
    perception "Five minutes go by, and two servants arrive through the door. One of them is an elf, the other a human."
    scene 134_s3 with Dissolve(1.0)
    miralith "A pleasure to meet you, Master. I'm Miralith, and this is Aylin."
    miralith "We were instructed to help you dress up. The armor has been prepared. It is of the highest quality available for your station."
    miralith "First-rank steel. It will serve you well in whatever task his royalty has assigned."
    scene 134_s4 with dissolve
    aylin "We will assist you in wearing it. Please allow us to undress you."
    scene 134_s2 with dissolve
    mc "You want to undress me?"
    scene 134_s3 with dissolve
    miralith "If you feel comfortable, Master. We can leave if that is what you desire."
    scene 134_s2 with dissolve
    call screen scene134_choice01 with dissolve


label scene134_choice01_op1:
    $ mc_rejected_mira_alyin = True
    mc "I'll wear the armor on my own. You can leave me alone."
    scene 134_s4 with dissolve
    aylin "As you wish, Master. If you require assistance, we will be right outside the door."
    scene 134_s2 with dissolve
    jump scene134_2

label scene134_choice01_op2:
    
    mc "Go ahead. If it'll be faster."
    scene 134_s4 with dissolve
    aylin "As you wish."
    scene 134_s2 with dissolve
    scene 134_s5 with Fade(0.5,0.5,0.5)
    ""
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 134_s6 with Dissolve(1.0)
    sensation "Their soft hands brush against your skin as they undress you. Your body responds before your mind can stop it."
    mc "..."
    scene 134_s27 with dissolve
    miralith "You seem to be in good health, Master."
    scene 134_s7 with dissolve
    mc "What?"
    scene 134_s27 with dissolve
    miralith "Your cock. It's fully erect. That's a good sign."
    scene 134_s7 with dissolve
    mc "I see... Thanks for the help."
    scene 134_s27 with dissolve
    miralith "Of course."
    scene 134_s8 with dissolve
    mc "And uhh... congratulations."
    miralith "Hmm? Congratulations for what, Master?"
    mc "The pregnancy. How far along are you?"
    scene 134_s9 with Dissolve(1.0)
    miralith "Ah. Thank you, Master. I'm in my thirty-third week now. Only seven more to go, if the Gods are willing. This one feels strong. Eager to be born."
    miralith "This is my eleventh pregnancy. I'm hoping for a strong male this time. The last two were females."
    miralith "They were healthy, but not what his royal highness needs."
    scene 134_s10 with dissolve
    mc "E-Eleven pregnancies?! Damn, you're like a baby factory."
    scene 134_s9 with dissolve
    miralith "*chuckles* Yes. As his royal highness's concubine, I am to be bred and to bear his children. It also helps that I am an elf, we can live long and bear many."
    scene 134_s10 with dissolve
    mc "So you two are his harem girls? The ones the prince mentioned?"
    scene 134_s9 with dissolve
    miralith "Just me. I have served in his royalty's harem for twenty nine years."
    scene 134_s11 with Dissolve(1.0)
    mc "You aren't in the harem?"
    scene 134_s12 with dissolve
    aylin "No, Master. I'm new here. I'm hoping to be assigned soon."
    scene 134_s11 with dissolve
    mc "Aiming for the king?"
    scene 134_s12 with dissolve
    aylin "I doubt the his royal highness has room in his harem at this point. Besides, he seems to have a preference for elfs."
    scene 134_s11 with dissolve
    miralith "*chuckles* He sure does."
    scene 134_s10 with Dissolve(1.0)
    mc "Don't you ever feel... tired? I assume giving birth that many times takes a toll."
    scene 134_s9 with dissolve
    miralith "Not at all, Master. It's my duty."
    miralith "It's what all of us concubines strive and hope to do. To be chosen to bear children. It is the greatest purpose a woman can aspire to."
    scene 134_s12 with Dissolve(1.0)
    aylin "*chuckles* She is his favourite. Most of the harem women only carry two or three times before they're... moved out. Four, if they're lucky."
    aylin "But Aylin? Eleven pregnancies. She's been the king's favorite for... well, since he was of age."
    scene 134_s11 with dissolve
    mc "I see. That's... that's a lot."
    scene 134_s13 with dissolve
    miralith "Amfhmm!"
    scene 134_s14 with dissolve
    mc "Are you okay?"
    perception "A stream of milk drips from her breasts. She notices immediately, her cheeks flushing from embarrassment."
    aylin "Did you not feed the children this morning, Mira? You're holding too much in you."
    aylin "You need to express regularly, or you'll develop an infection. You'll be no good to his royal highness if you're bedridden with fever."
    scene 134_s13 with dissolve
    miralith "No. Not yet. I was busy cleaning Lord Edin's quarters. The dust in that wing is terrible. The work took longer than expected."
    scene 134_s15 with Dissolve(1.0)
    miralith "I apologize, Master. It happens involuntarily. I didn't mean for you to see me this way... leaking, unkempt."
    miralith "I hope you forgive my obscenity. I will report myself for disciplinary action if you wish."
    scene 134_s16 with dissolve
    aylin "Go, Mira. I will continue alone with master here. You go to the nursery before you develop an infection."
    scene 134_s15 with dissolve
    miralith "N-No! I was requested to for master [mc]'s by sir Flint. I can't go against his word."
    scene 134_s16 with dissolve
    call screen scene134_choice02 with dissolve

label scene134_choice02_op1:
    $ mc_drank_aylin_mira = True
    scene 134_s19 with Dissolve(1.0)
    mc "Actually... I want to drink your milk. If it's causing you discomfort. I could... help with that."
    scene 134_s28 with dissolve
    miralith "..."
    aylin "..."
    scene 134_s20 with dissolve
    miralith "M-Master? I don't think I heard you correctly. Could you... say that again?"
    scene 134_s19 with dissolve
    mc "I said I want to drink your breast milk. It would be a shame to waste it when someone is thirsty."
    scene 134_s26 with dissolve
    aylin "Master, that is..."
    scene 134_s20 with dissolve
    miralith "The milk is for the children in the nursery. I'm only producing it because of them."
    scene 134_s19 with dissolve
    mc "And right now it's causing you pain, isn't it?"
    scene 134_s20 with dissolve
    miralith "That's... true, but still—"
    scene 134_s26 with dissolve
    aylin "There are other ways to relieve the pressure. We have cloths, and—"
    scene 134_s19 with dissolve
    mc "I'm offering a simpler solution. One that benefits both of us."
    scene 134_s20 with dissolve
    miralith "Master... people would talk if anyone found out. I'm not allowed to sexually serve anyone other than his royalty."
    scene 134_s19 with dissolve
    mc "Then no one needs to find out. It's just the three of us here."
    scene 134_s20 with dissolve
    miralith "...You're serious about this."
    scene 134_s19 with dissolve
    mc "I am."
    scene 134_s20 with dissolve
    miralith "A-As you wish. Please... sit down. Make yourself comfortable."
    miralith "But please don't take too much. I still have to go to the nursery afterward."
    scene 134_s28 with dissolve
    scene 134_s30 with Fade(1.5,1.0,1.4)
    perception "She guides your head forward with surprising gentleness, cradling you as she offers her breast. The nipple is warm and slightly swollen against your lips."
    mc "Mmmm..."
    scene 134_s31 with dissolve
    miralith "Mphmmm!"
    scene 134_s30 with dissolve
    mc "Am I sucking too hard?"
    scene 134_s31 with dissolve
    miralith "N-No, Master. You can do as you like."
    miralith "Ughm... it feels weird having a grown adult do this..."
    scene 134_s30 with dissolve
    scene 134_s32 with Dissolve(1.0)
    sensation "Warm milk spills onto your tongue as you suck. It tastes faintly sweet, and earthy. Your cock twitches again."
    aylin "...Master. Your cock is getting even harder."
    scene 134_s33 with dissolve
    miralith "Oh my... it's... quite large. Much larger than his highness."
    scene 134_s32 with dissolve
    aylin "Mira! Don't say things like that. What if they overhear you? I really don't wanna get into trouble because of this."
    scene 134_s33 with dissolve
    miralith "I-I apologize! It just slipped out!"
    scene 134_s32 with dissolve
    scene 134_s34 with Dissolve(1.3)
    mc "(Is this the strangest thing I've done so far? ...I can't stop. *slurp* It really does taste good.)"
    miralith "Master... is that enough? P-Please—you'll empty me if you keep going... The children still need their share."
    call screen scene134_choice03 with dissolve

label scene134_choice03_op2:
    $ renpy.end_replay()
    scene 134_s35 with Dissolve(1.0)
    mc "*slurp* ...Sorry. It was too good to stop right away."
    scene 134_s36 with dissolve
    miralith "It's alright, Master. I'm... glad you found it enjoyable."
    scene 134_s35 with dissolve
    aylin "Do you feel better now? More nourished?"
    mc "Yes. Surprisingly so."
    scene 134_s36 with dissolve
    miralith "It has a lot of nutrients. That's why I was chosen to head the nursery."
    scene 134_s35 with dissolve
    aylin "Let's continue getting you properly fitted, Master."
    jump scene134_2

image s134_hj = Movie(play="images/chapter5/scene134/s134_hj.webm", loop=True)
image s134_bj = Movie(play="images/chapter5/scene134/s134_bj.webm", loop=True)

label s134_servants:
    $ mc_drank_more_aylin_mira = True

    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.chapter5_p7_8_replay:
        $ persistent.chapter5_p7_8_replay = True
    scene 134_s37 with Dissolve(1.3)
    mc "*suck* I don't care about no children right now. This milk belongs to me."
    miralith "But Master... the nursery—"
    scene 134_s38 with Dissolve(1.0)
    aylin "Let him, Mira."
    aylin "He has an important mission ahead of him. He needs his strength more than the children need one feeding."
    scene 134_s39 with dissolve
    miralith "...Alright. I understand. V-Very well, Master. It's yours. Take what you need."
    mc "*slurp* That's what I like to hear."
    scene 134_s40 with dissolve
    mc "You—Aylin. Don't just stand there."
    scene 134_s41 with dissolve
    aylin "Whaddya—? I-I mean... what do you want me to do, Master?"
    scene 134_s40 with dissolve
    empathy "For a second, her voice cuts sharp, almost another person's, before she catches herself and melts back into a soft, servant-like deference."
    mc "Make me feel good too. It's not fair that your friend is doing all the work."
    aylin "..."
    scene 134_s41 with dissolve
    aylin "As you wish, Master."
    scene 134_s40 with dissolve
    stop music fadeout 1.5
    show s134_hj with Fade(0.5,0.5,0.5)
    sensation "She kneels beside you, her hand wrapps around your cock. She begins stroking in steady, practiced motions while you continue to suckle."
    aylin "Just rest and drink. We'll take care of everything else."
    miralith "The king will understand... right?"
    aylin "He has to. [mc] is the one who will be fighting Hodir and Modir, after all."
    mc "*slurp* ...Hodir? Modir? Are those the giants names?"
    miralith "Yes. It's not their true names—just the ones we use when we speak of them."
    mc "I see. But don't remind me of that right now. I'm having a really good time."
    perception "You seal your lips around her nipple again and suck harder, drawing another warm mouthful. Miralith's breath catches; her hand rests lightly on the back of your head, neither pushing you away nor pulling you closer."
    aylin "Understood, Master. We won't speak of them further."
    sensation "Her palm drags over the sensitive head. At the same time Miralith's milk continues to flow, rich and warm, filling your mouth with every pull."
    miralith "You're... taking so much, Master..."
    aylin "Let him. He needs it more than the nursery does today."
    mc "Mmh... both of you feel good..."
    aylin "He's completely hard now. Look how much he's leaking just from drinking your milk, Mira."
    aylin "Does it feel good, Master? Having one of us feeding you while the other strokes this thick cock?"
    mc "Mmh... yeah..."
    aylin "Take as much as you want from her. And from me. This cock deserves to be spoiled before you go fight those giants."
    miralith "Aylin?! When did you learn to speak like that?"
    aylin "I... Why do you ask?"
    miralith "You sound like a different person. So... sultry."
    aylin "I'm... I'm just trying to make master feel better."
    miralith "I see. Good on you. You're a quick learner."
    miralith "Your mouth is so warm, Master... and the way you're sucking—ahh—it's making more milk come down..."
    aylin "*giggles* She's getting wet from this, you know. I can see it. Being used like your personal milk source is turning her on."
    miralith "D-Don't say it like that!"
    aylin "*chuckles* Why not? It's true. And Master clearly likes hearing it. Tell him, Mira. Tell him how it feels to have him draining you while I stroke him."
    miralith "It feels... shameful... but also good. Your mouth is greedy and warm and I... I don't want you to stop yet, Master..."
    sensation "Another mouthful of rich milk spills onto your tongue. The combined pleasure makes your cock throb hard in her grip."
    miralith "Ugnhn~! If you keep going like this I'm going to... my breasts are starting to feel so sensitive..."
    aylin "Whenever you're ready to release, Master... just let go. I'll catch it all. You can keep drinking from Mira right through your orgasm."
    call screen scene134_choice04 with dissolve

label scene134_choice03_op1:
    $ mc_aylin_bj = True
    mc "Aghhh... Aylin! Use your mouth and suck me off. Now!"
    aylin "A-As you wish, Master."
    aylin "{size=30}Tch... I didn't get the opportunity to work at the palace so I can suck cocks.{/size}"
    scene black with Dissolve(1.0)
    show s134_bj with Fade(0.5,0.5,0.5)
    sensation "She collects a few drops of milk that have leaked from the corner of your mouth and from Miralith's nipple. Then she returns her attention to your cock."
    aylin "*lick* Like this, Master?"
    mc "Yes! Exactly like that! Mhhnnn..."
    miralith "You're still drinking so deeply... it's making more milk come down every time you pull..."
    aylin "He's also throbbing hard against my throat now. The milk is making it even more sensitive, isn't it?"
    mc "It somehow is... Ufhhn... *slurp*"
    aylin "Does it feel better like this, Master? Having your cock milked while you drain her milk?"
    mc "Mmh... fuck... yes..."
    miralith "Master... if you keep drinking and she keeps doing that, I'm going to start leaking even when you're not sucking..."
    aylin "Then let it leak. He can drink that too. Or I can use it to stroke his large cock even more."
    mc "Am I really bigger than the king? I rememeber you said that."
    miralith "P-Please don't pay mind to that. I was just plurting out loud."
    mc "But is it true?"
    miralith "...Yes."
    mc "Then maybe I should be the one taking care of you. You deserve better than what he has."
    miralith "Please, Master... that's blasphemous. Be careful saying things like that."
    miralith "Just focus on taking as much as you need from me. Mhnnmm~! D-Don't stop."
    aylin "He won't stop. Not until he fills my mouth with his seed. Will you, Master?"
    mc "Agghhnn! I-I can't hold it anymore!"
    call screen scene134_choice05 with dissolve

label scene134_choice04_op2:
    if mc_aylin_bj:
        mc "I'm... close! Don't stop either of you—"
        sensation "Aylin tightens her throat mucsles and speeds up, sucking you like a vaccum. At the same time you seal your lips harder around Miralith's nipple and suck deeply."
        play sound "se_sfx/blowjob/blowjob_cum6.mp3" 
        scene 134_s46 with vpunch
        mc "Aghnn!"
        sensation "Your cock pulses hard in the Aylin's mouth. Thick ropes of cum spill in her mouth and down into her stomach."
        miralith "Ahh! Master! You're sucking so hard while you cum... I can feel it... more milk is coming down—"
        play sound "se_sfx/blowjob/blowjob_cum7.mp3" 
        scene 134_s47 with vpunch
        aylin "*gulp* That's it... let it all out. Empty those balls while you empty her breasts."
        sensation "She keeps her lips sealed as the last weaker spurts drip onto her tongue. Only then does she stop sucking, still holding your cock in her mouth as the aftershocks fade."
        mc "Phew... I feel so full."
        play sound "se_sfx/blowjob/blowjob1.mp3" 
        scene 134_s48 with Dissolve(1.3)
        aylin "Mmmm~ *gag* I feel full too. So... tasty... *gag*"
        mc "Hahh... hah..."
        miralith "Master... are you alright?"
        scene 134_s49 with Dissolve(1.0)
        aylin "He's fine. Just spent. You released quite a lot, Master. I suppose the milk helped. *gag*"
        scene 134_s50 with dissolve
        miralith "I... I feel a little light-headed. You really did take a lot from me."
        mc "*chuckles* Sorry, you kept leaking into my mouth. I just kept drinking it."
        scene 134_s49 with dissolve
        aylin "Let's get you both cleaned up. Well... I also need to clean myself too. Ptoo. So much thick, potent seed stuck to the back of my throat."
        scene 134_s50 with dissolve
        miralith "Don't spit in the presence of a guest, Aylin!"
        scene 134_s49 with dissolve
        aylin "Right... I apologize, Master."
        scene 134_s50 with dissolve
        play music "nature.mp3" fadein 3.0 volume 0.5 loop
    else:
        mc "I'm... close! Don't stop either of you—"
        sensation "Aylin tightens her grip and speeds up, stroking you in short, firm pumps focused on the head. At the same time you seal your lips harder around Miralith's nipple and suck deeply."
        play sound "se_sfx/blowjob/facial8.mp3" 
        scene 134_s42 with vpunch
        mc "Aghnn!"
        sensation "Your cock pulses hard in Aylin's hand. Thick ropes of cum spill over her fingers and across her palm in heavy spurts."
        miralith "Ahh! Master! You're sucking so hard while you cum... I can feel it... more milk is coming down—"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 134_s43 with vpunch
        aylin "That's it... let it all out. Empty those balls while you empty her breasts."
        sensation "She works you firmly until the last weaker spurts drip onto her fingers and the bed. Only then does she slow her hand, still holding your cock as the aftershocks fade."
        scene 134_s44 with Dissolve(1.0)
        mc "Phew... I feel so full."
        scene 134_s45 with dissolve
        aylin "Mmmm~ You painted my hand white, Master. So... nice."
        scene 134_s44 with dissolve
        miralith "Master... are you alright?"
        scene 134_s45 with dissolve
        aylin "He's fine. Just spent. He released quite a lot. I suppose the milk helped."
        scene 134_s44 with dissolve
        miralith "I... I feel a little light-headed. You really did take a lot from me."
        mc "*chuckles* Sorry. You kept leaking into my mouth. I just kept drinking it."
        scene 134_s45 with dissolve
        aylin "Let's get you both cleaned up. Well... I also need to clean myself. So much thick, potent seed coating my fingers."
        scene 134_s44 with dissolve
        play music "nature.mp3" fadein 3.0 volume 0.5 loop
    $ renpy.end_replay()
    jump scene134_2

label scene134_choice02_op2:
    $ mc_punished_mira = True
    $ aylin_love -= 30
    mc "I didn't need to see that. Get out."
    scene 134_s15 with dissolve
    miralith "You are right to be disgusted, Master. But I swear to you—it was not my will. It's—"
    scene 134_s16 with dissolve
    mc "I don't want any excuses. I'll be reporting you to the king or whoever you work under."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    aylin "Master, please! She'll be punished harshly if you do!"
    mc "Good. Maybe the punishment will teach her to control herself. Now leave. Both of you. Before I get the guards to drag you out."
    hide screen stat_change with easeoutright
    $ karma_less = False
    scene 134_s15 with dissolve
    miralith "It's all right, Aylin."
    miralith "I understand, Master. I apologize."
    scene 134_s16 with dissolve
    jump scene134_2

label scene134_choice02_op3:
    $ aylin_love += 10
    $ nimah_love += 10
    mc "You need take better care of yourself. You're pregnant."
    mc "Your body is doing something exhausting, and yet you're here, fitting armor onto a stranger instead of feeding children or resting. That's not right."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 134_s17 with dissolve
    miralith "Master, I... This is my duty. This is what I was trained for."
    scene 134_s18 with dissolve
    mc "Your needs matter, not just as a concubine, not just as a... baby-maker. As a person. You're not a piece of furniture."
    hide screen stat_change with easeoutright
    $ karma_more = False
    miralith "..."
    scene 134_s17 with dissolve
    miralith "Thank you, Master. I will... I will think about what you said."
    scene 134_s18 with dissolve
    mc "Good."
    if mc_kiss_nimah:
        aylin "I told you. He really is kind."
        aylin "He kissed Nimah out of nowhere. She talked about a lot in the closet room."
        miralith "Yes~"
    else:
        aylin "You're really kind, Master."
    mc "You two deserve better. Look how hard you're working."
    scene 134_s17 with dissolve
    miralith "*chuckles* Thank you."
    scene 134_s18 with dissolve
    aylin "*giggles* Mhm~"
    jump scene134_2

label scene134_2:
    if mc_drank_aylin_mira or mc_drank_more_aylin_mira:
        scene 134_s22 with Fade(1.3,1.0,1.3)
        miralith "I feel a lot lighter now. That was... that was much needed. The pressure was becoming unbearable. I didn't realize how much I'd been holding in."
        scene 134_s29 with dissolve
        mc "You had so much milk in you, it was probably weighing you down."
        scene 134_s21 with dissolve
        aylin "*giggles* you had us working extra, Master. Fitting armor is one thing. What came after... that was beyond our usual duties."
        scene 134_s29 with dissolve
        mc "I did. And I'll be sure to repay you. I'll tell Flint that you both went above and beyond."
        scene 134_s22 with dissolve
        miralith "Thank you. We don't often receive recognition. The king notices me, but only in certain ways."
        scene 134_s21 with dissolve
        aylin "Good luck out there, Master. We will be waiting for your return~"
        scene 134_s29 with dissolve
        scene 134_s25 with Fade(1.3,1.0,1.3)
        mc "(It feels bulky and heavy. Oh well, I'll get used to it. Time to go. Negumi's probably already at the gate.)"

    elif not mc_punished_mira and not mc_rejected_mira_alyin:
        scene 134_s23 with Fade(1.3,1.0,1.3)
        aylin "How does it look, Master? I think it looks good on you."
        scene 134_s24 with dissolve
        mc "Thank you. It feels a lot sturdier than my other armor."
        mc "I feel safe. Safer than I have in weeks, or months, even."
        scene 134_s23 with dissolve
        miralith "The blacksmiths deserve the credit for the craftsmanship."
        miralith "But I'm glad we could be of help anyway. Even in this small way."
        aylin "Good luck out there, Master. We will be waiting for your return."

    else:
        scene 134_s25 with Fade(1.3,1.0,1.3)
        mc "(Phew, there. That took a lot longer than I expected.)"
        mc "(I look a lot better now. Not to mention safer. But it feels bulky and heavy. Oh well, I'll get used to it.)"
        mc "(Alright. Time to go. Negumi's probably already at the gate.)"

    jump scene135

label scene135:
    stop music fadeout 1.0
    scene 135_s1 with Fade(1.3,1.0,1.4)
    play music "wind.mp3" fadein 1.0 loop
    ""
    scene 135_s2 with Dissolve(1.5)
    flint "[mc]! Hold on."
    scene 135_s3 with Dissolve(1.0)
    mc "Flint. I was supposed to meet you. The ambassador said you'd brief me. Do you have any info on what I'm up against?"
    scene 135_s4 with dissolve
    flint "I do. What little there is. Listen, [mc]... I—"
    scene 135_s3 with dissolve
    mc "Please. I already felt the horror from Sanoud. He practically held a funeral for me in the corridor. I know this may as well be a death sentence."
    mc "But I'd rather hear whatever might help me."
    scene 135_s4 with dissolve
    flint "I understand. I'm happy to see you're accepting so well."
    flint "Alright. Here's what we know. You're facing giants—two of them. A pair of brothers. And, if the legends are to be believed, they might be immortal."
    scene 135_s3 with dissolve
    mc "Immortal? The Zentian mentioned they sleep for decades. But immortal? As in... can't be killed? At all?"
    scene 135_s4 with dissolve
    flint "They have been here longer than you and I have lived. Even before our kingdom was established."
    flint "These two have somewhat of a pattern. The scholars have been tracking it for centuries. Generations of scholars, all recording the same thing."
    scene 135_s5 with Dissolve(1.0)
    flint "They sleep for about a decade. A full ten years of dormancy. Then they wake up for another decade."
    flint "During this decade, they raise hell. They roam and eat whatever their fingers catch."
    scene 135_s6 with dissolve
    mc "But they began inching closer and closer? The Zentian said they only recently blocked the trade route."
    scene 135_s5 with dissolve
    flint "Exactly. It's only very recently that they've fully blocked the northeastern trade route with the Zentians."
    flint "Of course, we knew this would happen eventually. The scholars predicted it decades ago, but... what would we even do about it?"
    scene 135_s3 with Dissolve(1.0)
    mc "Yeah. Those soldiers you guys sent weren't much help."
    scene 135_s7 with dissolve
    flint "Unfortunately... yes. So many good soldiers lost. Sanoud was underestimating the numbers, he always say thousands were lost, but that's only during our lifetimes."
    flint "The total since our kingdom was established is... in the tens of thousands."
    scene 135_s8 with dissolve
    mc "What hope do I even have, then? Do they have a weakness? Something... anything?"
    scene 135_s7 with dissolve
    flint "Not as far as we know. They tower over us regular humans—they're as tall as our city walls."
    scene 135_s8 with dissolve
    mc "That tall?!"
    scene 135_s4 with Dissolve(1.0)
    flint "Yes. And those are just estimates from the survivors. The ones who got close enough to see them clearly."
    scene 135_s3 with dissolve
    mc "You're not making this easy, Flint. You're really, really not making this easy."
    scene 135_s4 with dissolve
    flint "I'm sorry, [mc]. I'm not here to fill you with false hope."
    flint "My job is to prepare you. To give you the truth. And the truth is... is as close to impossible as anything I've ever seen."
    flint "I think Ambassador Sanoud already told you. You don't really have to fight. The king's orders were given in anger. He doesn't actually expect you to succeed."
    scene 135_s3 with dissolve
    mc "So he expects me to run, even if it means abandoning the mission?"
    scene 135_s4 with dissolve
    flint "Yes."
    scene 135_s3 with dissolve
    mc "..."
    mc "We'll see what happens. Point me to where they are."
    scene 135_s9 with dissolve
    flint "Give me your map. I'll mark the location. The pass is northeast, a two day's ride from here."
    scene 135_s10 with Dissolve(1.5)
    empathy "His expression is serious as he marks the location. His hand is steady, but his eyes betray him—haunted, almost vacant. He's already mourning you."
    scene 135_s11 with Dissolve(1.0)
    flint "There. I pray to the Gods that you come back alive, [mc]."
    flint "I heard from Alexandria that you already have a weapon. Adamantite, correct?"
    scene 135_s12 with dissolve
    mc "Shit! It's on the carriage we arrived with, and I don't know where it is!"
    scene 135_s11 with dissolve
    flint "Relax. She brought it to the palace before dawn arrived. We have it with us."
    flint "It's outside with the guards, attached to your horse."
    scene 135_s12 with dissolve
    mc "Phew... good. And yes, it's adamantite. Made by the best smith in Irda."
    scene 135_s11 with dissolve
    flint "I see. Adamantite is the bare minimum to even fight them. Regular steel shatters against their skin."
    flint "Even advanced magic spells wouldn't work. I hope your friend, Negumi, is powerful enough."
    scene 135_s12 with dissolve
    mc "I'll be off, Flint. That... that wasn't really helpful, but thank you anyway."
    scene 135_s7 with Dissolve(1.0)
    flint "I'm sorry. That's all I seem to be able to offer these days."
    flint "Not many people get back alive from that pass. And those who do... they usually come back missing several limbs, or their full mental capapilites."
    scene 135_s8 with dissolve
    mc "(Goddammit... just what have you put me through, Negumi?)"
    scene 135_s13 with Fade(1.5,1.0,1.3)
    shiver "You feel a knot in your throat. There's a grip on your stomach, cold and tight, like a fist squeezing from the inside."
    scene 135_s14 with Dissolve(1.0)
    mc "I don't know if I should punch you or not, Negumi."
    scene 135_s15 with dissolve
    negumi "...I'm sorry, [mc]. I know I put you in this position. I know this is my fault. But... but this is finally my chance to prove myself!"
    negumi "It's my chance to show the world what I can do! My chance to—"
    scene 135_s14 with dissolve
    mc "Prove yourself to what?! To who?!"
    mc "What is so important that you'd volunteer us both for a suicide mission without even asking me first?!"
    scene 135_s16 with vpunch
    negumi "To everyone!"
    negumi "To everyone who ever doubted me! To everyone who ever called me a mistake, a joke!"
    negumi "To the mages who said I'd never amount to anything! To my family, who told me I was wasting my life! To everyone who ever looked at me and saw nothing but an idiot playing pretend!"
    scene 135_s17 with dissolve
    mc "..."
    negumi "..."
    scene 135_s18 with dissolve
    negumi "Sorry. I... it's a promise from my childhood. Something I swore I'd do."
    negumi "Pulling you along wasn't my intention. I don't think, I just act. That's all I've ever done."
    scene 135_s17 with dissolve
    mc "*sigh* We're already past that now. The king gave his orders."
    mc "There's no going back now. So let's just survive, alright?"
    negumi "..."
    call screen scene135_choice01 with dissolve

label scene135_choice01_op1:
    $ mc_encouraged_negumi = True
    $ negumi_love += 10
    scene 135_s19 with dissolve
    mc "You know what? Let's do it! Let's kill those giants! Let's give the bards something to sing about for the next thousand years!"
    scene 135_s17 with dissolve
    negumi "..."
    scene 135_s21 with Dissolve(1.0)
    negumi "...Y-You're right! We got this, [mc]!"
    negumi "Let's go! To glory! And if we die, then at least we'll die together! At least we'll die as legends!"
    mc "*chuckles* That's the spirit."
    jump scene135_2

label scene135_choice01_op2:
    $ negumi_love -= 10
    scene 135_s20 with Dissolve(1.0)
    mc "That's enough sulking, Negumi. Let's move."
    mc "You put me through this. You put us both through this. The least you could do is own up to it."
    scene 135_s18 with dissolve
    negumi "*sigh* ...You're right. I don't blame you for hating me. I'd hate me too, if I were in your place."
    negumi "Let's go. I'll try to be out of your way. And if I fail, then... run."
    negumi "And if you'd rather run away right now... that's fine by me."
    scene 135_s17 with dissolve
    jump scene135_2

label scene135_2:
    stop music fadeout 1.0
    scene 135_s22 with Fade(1.3,1.0,1.5)
    play music "hope/wizards_journey.mp3" fadein 3.0 loop
    env "The city walls draw nearer, then further. The sandstone buildings of Nahraya shrink, replaced by rocky outcroppings and sparse desert scrub."
    scene 135_s23 with Fade(1.3,1.0,1.3)
    negumi "Can we rest for a little? An exhausted mage is a dead mage."
    scene 135_s24 with dissolve
    mc "Yeah, you're right. We've been riding for a while."
    scene 135_s23 with dissolve
    negumi "Let's set up camp near that oasis."
    scene 135_s24 with dissolve
    mc "Oasis? Where do you see an oasis?"
    scene 135_s25 with Dissolve(1.0)
    negumi "I can sense water through my mana. It's to the east, about ten minutes' ride."
    mc "Whoa. That's actually helpful."
    scene 135_s26 with Fade(1.3,1.0,1.3)
    env "Green trees break the monotony of yellow sand and gray rock. A small pond of water sits in the center of the oasis—crystal clear, surrounded by date palms."
    mc "You were right! There's really an oasis here."
    negumi "Heh. Of course I was right."
    scene 135_s27 with Fade(0.5,0.5,0.5)
    perception "You lead [horse] to the water's edge. She drink greedily. The sun sets through the palm fronds, casting shadows across the pond."
    negumi "What's your horse's name? He's quite strong for going this distance."
    mc "It's [horse]. And it's a she. She's been with me since Irda."
    scene 135_s28 with Dissolve(1.0)
    negumi "Hnnngg! There! My humble abode is set. You may enter, [mc]. I have faith in your manhood that you won't touch me inappropriately."
    negumi "You seem like the honorable type."
    scene 135_s28 with vpunch
    mc "Hey! Don't get the wrong idea about me!"
    scene 135_s29 with Fade(0.5,0.5,0.5)
    perception "She pulls off her boots, revealing her feet. A large sum of sand spills from each boot."
    negumi "Ugh... this sand. It's been driving me insane since the moment I arrived here."
    negumi "How do people live here? How does anyone live here?"
    scene 135_s30 with Dissolve(1.0)
    mc "You're not wearing socks? You've been walking around the desert, in boots, with no socks?"
    scene 135_s31 with Dissolve(1.0)
    negumi "No? Do I have to?"
    scene 135_s32 with dissolve
    mc "...You kinda do."
    scene 135_s31 with dissolve
    negumi "I'll just wash them in the pond."
    negumi "As for you, gather some wood. It gets really cold at night."
    scene 135_s124 with dissolve
    call screen scene135_choice02 with dissolve

label scene135_choice02_op1:
    $ mc_massage_negumi_feet = True
    scene 135_s32 with dissolve
    mc "Before I gather anything... do you want help? With your feet? They must be aching."
    scene 135_s31 with dissolve
    negumi "*laughs* What?"
    negumi "You're fine with touching my sweaty feet? Voluntarily? Without being asked?"
    scene 135_s32 with dissolve
    mc "Yeah. I don't mind."
    mc "I need you at your best. If that means taking a few minutes to work the tension out of your feet, then it's worth it."
    scene 135_s31 with dissolve
    negumi "I don't know... I feel embarrassed. I don't even let those boot shiners from the market near me."
    negumi "And it's not because I can't afford it! I just... don't want them near me."
    scene 135_s32 with dissolve
    mc "You can trust being around me. I really want to."
    scene 135_s31 with dissolve
    negumi "...Alright. Fine. Just... don't make this weird."
    scene 135_s32 with dissolve
    mc "You're usually the one who makes things weird. I'm the normal one here."
    scene 135_s31 with dissolve
    negumi "Not this time."
    scene 135_s124 with dissolve
    scene 135_s33 with Fade(0.5,0.5,0.5)
    sensation "You carefully lift one of her feet. The sole is warm, a little dusty. The arch is tight under your thumbs."
    scene 135_s34 with dissolve
    negumi "Ah~ Alright, that's... actually not terrible."
    scene 135_s33 with dissolve
    mc "Just tell me if I press too hard."
    scene 135_s34 with dissolve
    negumi "You're fine so far. It's just... strange having someone else do this."
    negumi "You really don't mind the sweat? Or the... smell?"
    scene 135_s33 with dissolve
    mc "Nothing I can't handle."
    scene 135_s36 with Dissolve(1.0)
    negumi "Mphmmm~ You're weirdly good at this. Have you done this before?"
    scene 135_s35 with dissolve
    mc "A couple of times."
    scene 135_s37 with dissolve
    perception "You keep massaging in silence for a short while, only the quiet sound of your hands moving and the desert wind filling the space between you."
    negumi "Ahhh~"
    mc "..."
    call screen scene135_choice03 with dissolve

label scene135_choice03_op1:
    $ mc_sniffed_negumi = True
    scene 135_s40 with Dissolve(1.0)
    perception "Without really thinking, you lean in a little closer while your thumbs press into her arch. You draw in a quiet breath near her toes."
    negumi "...Are... are you sniffing my foot?"
    scene 135_s41 with Dissolve(1.0)
    mc "I... uhh... I can explain—"
    scene 135_s42 with dissolve
    negumi "You're so weird! What the hell was that?! I specifically told you not to make it weird!"
    scene 135_s41 with dissolve
    mc "They don't smell bad! They just smell like... you."
    mc "I was curious. I'm sorry."
    scene 135_s42 with dissolve
    negumi "That is not a normal thing to say. Or do."
    scene 135_s43 with Dissolve(1.0)
    mc "I know. It just... happened."
    scene 135_s44 with dissolve
    negumi "'It just happened'? You leaned in and sniffed them on purpose!"
    negumi "You're lucky they don't actually stink right now."
    scene 135_s43 with dissolve
    mc "They don't? I beg to differ. But in a good way."
    scene 135_s44 with dissolve
    negumi "Alright, that's enough! You made this even weirder."
    scene 135_s43 with dissolve
    mc "*chuckles* Still doesn't smell that bad. Just saying."
    scene 135_s45 with Dissolve(1.5)
    negumi "*sigh* Whatever. Just go and get some wood already."
    negumi "Thank you for the massage. Before you got weird, it was actually really nice. I'll take care of myself now."
    jump scene135_wood1
    
label scene135_choice03_op2:
    $ mc_licked_negumi = True
    scene 135_s46 with Dissolve(1.0)
    perception "You pause the massage for a moment. Then, before you can second-guess yourself, you lean down and drag your tongue slowly along her toes."
    negumi "Ah! What are you—[mc], what are you DOING?!"
    scene 135_s41 with Dissolve(1.0)
    mc "I... I don't know. I just wanted to."
    scene 135_s42 with dissolve
    negumi "You licked my sweaty foot! Who does that!?"
    negumi "Did the desert heat cook your brain?!"
    scene 135_s41 with dissolve
    mc "I just... wanted to make you feel good. All of you. Even your feet... {i}especially{/i} your feet."
    scene 135_s44 with Dissolve(1.0)
    negumi "That is not a normal way to make someone feel good!"
    scene 135_s43 with dissolve
    empathy "Her face is burning. She looks equal parts scandalized and confused, as if her brain is still trying to process what just happened."
    scene 135_s44 with dissolve
    negumi "You're actually serious right now. You didn't slip or something. You... you did that on purpose!"
    scene 135_s43 with dissolve
    mc "Yeah. I did. And I'd do it again if you wanted me to."
    scene 135_s44 with dissolve
    negumi "I don't even know what to say to that..."
    negumi "If you ever do that again, I'm kicking you in the face."
    scene 135_s43 with dissolve
    mc "*chuckles* Fair."
    scene 135_s45 with Dissolve(1.5)
    negumi "I told you not to make this weird, and you made it werid."
    negumi "*sigh* Thank you for the massage, but just go and get some wood already."
    jump scene135_wood1

label scene135_choice03_op3:
    $ negumi_love += 10
    scene 135_s38 with dissolve
    mc "There. Do you feel better now?"
    scene 135_s39 with dissolve
    negumi "Yeessss~ They do feel better. A lot better, actually. The ache is gone."
    scene 135_s38 with dissolve
    mc "I'm good at these things."
    scene 135_s39 with dissolve
    negumi "...Thank you, [mc]. For the massage, and for not making it weird."
    scene 135_s38 with dissolve
    mc "Of course. Now let me go gather some wood."
    scene 135_s39 with dissolve
    jump scene135_wood1

label scene135_choice02_op2:
    scene 135_s32 with dissolve
    mc "On it."
    scene 135_s124 with dissolve
    jump scene135_wood1

default s135_wood = 0
label scene135_wood1:
    if mc_encouraged_negumi:
        $ current_objective = "Tomorrow will decide my fate. The giants. The pass. \nThe mission I never asked for. It will be the hardest \nchallenge I have faced yet, and Negumi is to blame \nfor putting me into this situation. She burst through \nthat door and handed us a death sentence. \n\nBut I don't blame her. She has something to prove to \nthe world. Maybe that's why I'm not angry. \n\nMaybe I'm here to prove something too."
    else:
        $ current_objective = "Tomorrow will decide my fate. The giants. The pass. \nThe mission I never asked for. It will be the hardest \nchallenge I have faced yet, and Negumi is to blame \nfor putting me into this situation. She burst through \nthat door and handed us a death sentence. \n\nI made sure to tell her about it. She says she has \nsomething to prove to the world. Maybe that's why \nI haven't ran away yet. \n\nMaybe I'm here to prove something too."
    if scene135_free_roam_poster1 and scene135_free_roam_stick1:
        scene 135_s47_all with dissolve
    elif scene135_free_roam_poster1:
        scene 135_s47_poster with dissolve
    elif scene135_free_roam_stick1:
        scene 135_s47_wood with dissolve
    else:
        scene 135_s47 with dissolve
    if s135_wood == 3:
        mc "(That should be enough wood for tonight.)"
        jump scene135_3
    call screen scene135_wood1 with dissolve

label scene135_wood1_poster:
    $ persistent.mix_render4 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene135_free_roam_poster1 = False
    jump scene135_wood1

label scene135_wood1_stick:
    $ s135_wood += 1
    play sound "sound_effects/wood_rattle.mp3"
    $ scene135_free_roam_stick1 = False
    jump scene135_wood1

label scene135_wood2:
    if scene135_free_roam_poster2 and scene135_free_roam_stick2:
        scene 135_s48_all with dissolve
    elif scene135_free_roam_poster2:
        scene 135_s48_poster with dissolve
    elif scene135_free_roam_stick2:
        scene 135_s48_wood with dissolve
    else:
        scene 135_s48 with dissolve
    if s135_wood == 3:
        mc "(That should be enough wood for tonight.)"
        jump scene135_3
    call screen scene135_wood2 with dissolve

label scene135_wood2_poster:
    $ persistent.nadia_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene135_free_roam_poster2 = False
    jump scene135_wood2

label scene135_wood2_stick:
    $ s135_wood += 1
    play sound "sound_effects/wood_rattle.mp3"
    $ scene135_free_roam_stick2 = False
    jump scene135_wood2

label scene135_wood3:
    if scene135_free_roam_poster3 and scene135_free_roam_stick3:
        scene 135_s49_all with dissolve
    elif scene135_free_roam_poster3:
        scene 135_s49_poster with dissolve
    elif scene135_free_roam_stick3:
        scene 135_s49_wood with dissolve
    else:
        scene 135_s49 with dissolve
    if s135_wood == 3:
        mc "(That should be enough wood for tonight.)"
        jump scene135_3
    call screen scene135_wood3 with dissolve

label scene135_wood3_poster:
    $ persistent.alex_render3 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene135_free_roam_poster3 = False
    jump scene135_wood3

label scene135_wood3_stick:
    $ s135_wood += 1
    play sound "sound_effects/wood_rattle.mp3"
    $ scene135_free_roam_stick3 = False
    jump scene135_wood3
    
label scene135_3:
    $ in_free_roam = False
    stop music fadeout 1.0
    scene 135_s50 with Fade(1.3,1.0,1.5)
    play music "night_fire.mp3" fadein 1.0 loop
    negumi "Ahhh~ So warm."
    if mc_encouraged_negumi:
        scene 135_s53 with dissolve
        mc "Go ahead and sleep, I'll keep watch."
        scene 135_s52 with dissolve
        negumi "Sleep? What's that? I'm a night hawk, [mc]. My eyes pierce the darkness. My senses remain alert while lesser mortals slumber."
        scene 135_s53 with dissolve
        mc "I think you mean 'night owl'."
        scene 135_s52 with dissolve
        negumi "Whatever it is. Hawk. Owl. Some creature that doesn't sleep at night."
        negumi "The point is, I'll stay awake with you. You won't have to face the darkness alone. That's what comrades do."
        scene 135_s53 with dissolve
        mc "Comrades, huh? Is that what we are now?"
        scene 135_s52 with dissolve
        if mc_licked_negumi:
            negumi "Don't make it weird again. I'm still recovering from you licking my toes. Eugh."
        elif mc_sniffed_negumi:
            negumi "Don't make it weird again. I'm still recovering from you sniffing my sweaty foot. Eww."

        negumi "Together. The sorceress of doom and the... you, against everything the world can throw at us. They'll sing songs about us for a thousand years!"
        scene 135_s53 with dissolve
        mc "They'd better. If we survive this."
        scene 135_s52 with dissolve
        negumi "And a statue!"
        scene 135_s53 with dissolve
        mc "*chuckles* Why not."
    scene 135_s54 with dissolve
    negumi "Can I ask you something?"
    scene 135_s55 with dissolve
    mc "Sure."
    scene 135_s54 with dissolve
    negumi "Why are you doing this? You can just walk away and pretend you fought them."
    if mc_encouraged_negumi:
        negumi "I'm the reason we're out here, waiting to fight monsters that have killed armies. You don't seem to hate me for putting you in this situation."
    else:
        negumi "I'm the reason we're out here, waiting to fight monsters that have killed armies. I know you hate me for it, so why stay?"
    scene 135_s55 with dissolve
    mc "Because I kinda understand why you did it. I saw it in the throne room—the fire in your eyes."
    mc "This wasn't just about glory. This was about something deeper."
    scene 135_s54 with dissolve
    negumi "...Yeah. A promise."
    negumi "To make them remember my name, even after I'm gone. Because if I don't... then what was the point of it all?"
    negumi "What was the point of every humiliation, of every time I had to hide who I really am?"
    scene 135_s55 with dissolve
    mc "Hide who you really are? What do you mean?"
    scene 135_s54 with dissolve
    negumi "I'm not human, [mc]. Not entirely."
    scene 135_s55 with dissolve
    mc "What?"
    scene 135_s56 with dissolve
    negumi "I'm a faerie. A half-elf. I was told that my mother was an elf, a high elf, from one of those ancient bloodlines that could live for millenniums. My father was human."
    negumi "I've spent my whole life hiding what I am, because if the wrong people found out... it won't be good for me."
    scene 135_s57 with dissolve
    mc "Oh... I didn't notice. I mean, I was a bit suspicous of how strong your magic is compared to a regular human, but that's about it."
    scene 135_s56 with dissolve
    negumi "It's on purpose. I've had decades of practice. I have to wear my hair down to hide my ears."
    negumi "And the mana... well, any mage worth shit can feel it, which is why I always keep it dampened."
    negumi "That's why I need the staff—it helps me focus without letting the full force of my nature leak out."
    scene 135_s57 with dissolve
    mc "But why hide it? I've never heard of anyone being executed for having pointy ears."
    mc "All the elves I've met so far seem to have it fine. Well, most of them."
    scene 135_s54 with dissolve
    negumi "It's not execution. It's... rejection. Isolation. We fairies sit in a weird spot."
    negumi "We aren't accepted in human communities, because we're too 'other'. And the elves... the elves despise us. We're a stain on their 'pure bloodlines'."
    negumi "It's better to just hide the fact and continue living normally."
    scene 135_s55 with dissolve
    mc "People hate half-elves that much?"
    scene 135_s54 with dissolve
    negumi "No. They hate elves. Humans fear them, see them as arrogant immortals who look down on everyone else. And elves? Elves hate everyone that isn't an elf."
    negumi "Even among elves, there's hatred. There are hierarchies. Pure bloodlines versus lesser ones. Elves who live for hundreds of years versus those who live for thousands."
    scene 135_s52 with dissolve
    negumi "*laughs* You can see how I don't fit in either group."
    scene 135_s53 with dissolve
    mc "Damn. That's... that's a heavy burden to carry."
    scene 135_s52 with dissolve
    negumi "Heh. You get used to anything."
    scene 135_s58 with dissolve
    negumi "But that's why I need this mission to succeed. Not just for the alliance. For {i}me{/i}."
    negumi "For the half-elf girl who was told she'd never amount to anything, who had to hide her own ears, eyes, and soul just to survive."
    scene 135_s59 with dissolve
    empathy "She stares at you with a fierce, desperate intensity that burns hotter than the fire between you."
    scene 135_s58 with dissolve
    negumi "I need to prove that I'm more than a mistake. More than the sum of two races that didn't want me."
    scene 135_s59 with dissolve
    mc "..."
    if mc_gave_coin_negumi:
        scene 135_s52 with dissolve
        negumi "Oh! And by the way, I have the silver you gave me before. Just remind me to give to you once we're done."
        scene 135_s53 with dissolve
        mc "The silver?"
        scene 135_s52 with dissolve
        negumi "You gave me a silver coin back when I was on the brink of sleeping on the street."
        negumi "That silver bought me three days of food and a night in a real bed. Thank you."
        scene 135_s53 with dissolve
        mc "*chuckles* Don't mention it."

    mc "You know... something's been on my mind for a while now."
    scene 135_s52 with Dissolve(1.0)
    negumi "What is it?"
    scene 135_s53 with dissolve
    mc "I'm just confused. When we reunited in the market, you dismissed innocent people getting hurt."
    mc "You were about to rob the adventuteres' guild, and the only reason you didn't is because you sensed something scary inside."
    scene 135_s52 with dissolve
    negumi "I'm a mage, [mc]. A mercenary. A survivor. I do what needs to be done to get what I want."
    negumi "I'm not a hero or a villain. I'm just... me."
    scene 135_s53 with dissolve
    mc "So why did you help me out back then? You warned me about Maia. You told me what was happening, even came along with me."
    mc "You had no incentive to do that. No coin or reward waiting for you. You could have gone on with your life, and I would have just stayed there in the castle, oblivious to what truly happened."
    scene 135_s54 with dissolve
    negumi "You're right. I barely knew you. You were just a man who worked at the castle. Nothing that should have mattered to me."
    negumi "But... I just felt a strange pull to you. Something I still can't explain. I just... felt like I had to. Like something was guiding me toward you."
    scene 135_s55 with dissolve
    mc "What does that even mean?"
    scene 135_s54 with dissolve
    negumi "No clue. Only that I did. I was compelled to do so, and so I did. It wasn't out of the goodness of my heart, if that's what you're wondering."
    scene 135_s55 with dissolve
    mc "Hmm..."
    scene 135_s54 with dissolve
    negumi "I've thought about it a lot. I've wondered if I made a mistake. If I should have never told you."
    scene 135_s52 with dissolve
    negumi "*chuckles* Maybe things would have turned out better for me if I never met you."
    scene 135_s53 with dissolve
    mc "...Why don't we share campfire stories to pass the time? I'd like to know more about you."

    if mc_encouraged_negumi:
        scene 135_s52 with dissolve
        negumi "Oh! That sounds fun! We'll stay up all night!"
        scene 135_s60 with wiperight
    else:
        scene 135_s54 with Dissolve(1.0)
        negumi "Sorry, [mc]. But I need to sleep. I told you, a tired mage is a dead mage."
        scene 135_s55 with dissolve
        mc "Alright, I get it."
        scene 135_s60 with Dissolve(2.0)
        
    play sound "sound_effects/body/cat_snore.mp3"
    perception "She snores loudly. Drool drips from the corner of her mouth, trailing down onto the sand."
    if mc_encouraged_negumi:
        mc "Eugh. 'Night hawk' my ass..."
    stop sound fadeout 2.0
    scene 135_s61 with Dissolve(2.0)
    mc "*sigh* (Minthra... I might really need your help tomorrow. More than I've ever needed you before.)"
    sensation "The fire warms your skin from the right. The cold desert wind blows from your left. Despite what lies ahead, you feel serene."
    scene 135_s62 with Dissolve(1.0)
    mc "*yawn* (Nothing's out here. No one will blame me if I take a little nap.)"
    mc "(Yeah... Just a few minutes. Then I'll be ready. Then I'll...)"
    scene black with Dissolve(1.7)
    stop music fadeout 1.5
    scene 135_s63 with Fade(1.5,1.0,1.5)
    play music "wind2.mp3" fadein 1.0 loop
    negumi "[mc]!"
    mc "Unnn..."
    scene 135_s65 with Dissolve(1.0)
    negumi "Wake up! Please wake up! [mc], you have to wake up RIGHT NOW!"
    scene 135_s64 with dissolve
    mc "Negumi? Fuck... I overslept. By a lot."
    scene 135_s65 with dissolve
    negumi "Shut up! Don't move a single muscle! Don't make any sudden movements!"
    scene 135_s64 with dissolve
    mc "What's wrong with you?"
    scene 135_s66 with dissolve
    negumi "..."
    mc "Hmm?"
    stop music fadeout 1.0
    scene 135_s67 with Dissolve(1.0)
    mc "..."
    play music "tense/giants.mp3" fadein 3.0 loop
    negumi "H-He's looking right at us."
    mc "No, that's impossible! They should still be much further ahead! Flint said the pass was another day's ride from here!"
    mc "M-Maybe they're looking at something else? We're tiny compared to them."
    scene 135_s68 with Dissolve(1.5)
    negumi "L-L-Let's run, [mc]! Please, let's just run!"
    negumi "I'm sorry! I'm so sorry for putting you into this!"
    scene 135_s70 with Dissolve(1.0)
    negumi "I just wanted to be someone who mattered, I just wanted to do something big and important and not be forgotten—I didn't want to die!"
    negumi "I don't want to die! I want to go home now!"
    scene 135_s69 with dissolve
    mc "Calm down! I told you—he's just looking at something else."
    mc "No way he sees us... We're two tiny specks in a massive desert."
    scene 135_s70 with dissolve
    negumi "We're sitting in the only oaises for miles, of course he sees us! But... maybe they aren't in the mood to fight."
    negumi "Can we please back up slowly?!"
    scene 135_s69 with dissolve
    mc "Alright! Alright! Move slowly... towards [horse]—"
    play sound "sound_effects/body/giant_steps.mp3"
    scene 135_s71 with vpunch
    perception "The giant suddenly dashes in your direction. One moment it's on the horizon. The next, it's crossed half the distance. The ground shakes with every footstep."
    scene 135_s72 with Dissolve(1.0)
    mc "GUHHHHH!"
    negumi "[mc]! No!"
    scene 135_s73 with Dissolve(1.0)
    mc "NGHNNNN! Negumi!"
    sensation "The giant's grip intensifies. You feel like you're going to puke. Your eyes bulge. Black spots dance at the edges of your vision."
    scene 135_s74 with Dissolve(1.0)
    mc "Huh?! What are you—Stop! What are you doing?!"
    play sound "sound_effects/body/giant_bite.mp3"
    scene 135_s75 with Dissolve(1.0)
    mc "AAAAGHHHHHHH!"
    mc "I'm... I'm gonna die!"
    scene 135_s76 with Dissolve(1.0)
    play sound "sound_effects/magic/magic_fire.mp3"
    negumi "Goddess of fire, I beseech thee! Bring flame!"
    scene 135_s77 with Dissolve(1.0)
    sensation "Flame engulfs the air around you. The heat is unimaginable—your internal water begins bubbling. Your skin sizzles. You feel your very flesh igniting."
    mc "What are you doing, Negumi?! You'll burn me too! I'm still in his mouth! I'm still—"
    negumi "I'm sorry! I have no other choice! It's this or watch you die! Please survive! PLEASE!"
    play sound "sound_effects/magic/magic_fire4.mp3"
    scene 135_s78 with vpunch
    mc "NGHAAAAA!"
    giant "AGHHHH!"
    scene 135_s79 with Dissolve(1.5)
    negumi "It worked! The giant is retreating!"
    scene 135_s80 with Dissolve(1.5)
    negumi "Are you alright?!"
    mc "..."
    scene 135_s81 with dissolve
    mc "W... Watch out!"
    negumi "Don't worry, I'll have my shield u—"
    play sound "sound_effects/body/body_squelch.mp3"
    scene 135_s82 with vpunch
    mc "No! No, no, no..."
    mc "Negumi... Fuck!"
    scene 135_s83 with Dissolve(1.0)
    mc "I'll kill you... I'll fucking kill you! You hear me?! I'll tear you apart! I'll burn what's left! I'll—"
    play sound "sound_effects/body/armor_hit.mp3"
    scene 135_s84 with vpunch
    ""
    scene 135_s85 with Dissolve(1.0)
    ""
    scene 135_s86 with Dissolve(1.0)
    ""
    scene 135_s87 with Dissolve(0.3)
    play sound "sound_effects/body/ground_impact.mp3"
    scene 135_s87 with vpunch
    ""
    scene 135_s88 with Dissolve(2.0)
    minthra "This is most vexing..."
    minthra "Wake up. You are not permitted to die yet."
    scene 135_s89 with vpunch
    mc "*gasp* HAHH!"
    mc "I don't feel anything... Why don't I feel anything?"
    scene 135_s90 with dissolve
    minthra "Because every bone in your body is shattered. If you felt the full extent of your injuries, you would die immediately. I am protecting you from the truth."
    scene 135_s89 with dissolve
    mc "I can't do it, Minthra... *cough* Not even with your power. Their strength is something else entirely."
    mc "It's hopeless."
    scene 135_s90 with dissolve
    minthra "Who says this is the extent of my power?"
    scene 135_s89 with dissolve
    mc "You're saying... it isn't?"
    scene 135_s90 with dissolve
    minthra "Yes. Did you think I would lend you all my power at once? Did you think I would trust a mortal vessel with the full extent of what I am?"
    scene 135_s91 with Dissolve(1.0)
    mc "What the hell?! You... I could have done so much if you did! I could have stopped so many things before they got worse!"
    scene 135_s92 with dissolve
    minthra "It would break your mind if I gave you everything. The mortal psyche is fragile. It was not designed to contain what I am."
    mc "..."
    minthra "Besides. That was not the only reason I didn't lend you my full strength."
    scene 135_s91 with dissolve
    mc "What? What are you talking about?"
    scene 135_s92 with dissolve
    minthra "It's because of her."
    scene 135_s91 with dissolve
    mc "Her? *cough* Negumi?"
    scene 135_s92 with dissolve
    minthra "You will see."
    scene 135_s91 with dissolve
    mc "Please... just do it. Whatever you've been holding back. I need to help Negumi, she got hit really bad. She might be... she might be dead."
    scene 135_s92 with dissolve
    minthra "You shall have what you ask. But remember this moment, my champion. Remember the cost."
    scene 135_s91 with dissolve
    mc "I don't care. Whatever it is. Whatever you want. Just give me the power... otherwise, I might just die here."
    scene 135_s93 with Dissolve(1.5)
    sensation "You suddenly feel invigorated. The pain doesn't vanish, it's still there, but it's a distant scream at the back of your mind."
    scene 135_s94 with dissolve
    mc "Ahh!"
    mc "I feel... I feel so powerful! Like I could take on everything! Like nothing in this world or any other could stop me!"
    scene 135_s93 with dissolve
    minthra "Do not be reckless. This full communion is lethal for your mortal body if maintained for too long."
    minthra "Your bones are still broken, your skin still flakes and peels. Your healing will be short, but it will take time to heal fully."
    scene 135_s94 with dissolve
    mc "Then I'll be quick."
    play sound "sound_effects/sword/sword_swing3.mp3"
    scene 135_s95 with vpunch
    mc "Huh!? My sword!"
    mc "Negumi? Did she do that? Fuck... that giant launched me so far away. I'll have to be quick."
    scene 135_s96 with Fade(1.0,1.0,1.0)
    mc "Negumi!"
    negumi "..."
    mc "Stay up there. I'll handle this."
    scene 135_s97 with Dissolve(1.5)
    mc "You've lived too long. You've killed too many. And now... now you're going to die."
    scene 135_s97 with Dissolve(0.3)
    play sound "sound_effects/sword/hard_slash3.mp3"
    scene 135_s98 with vpunch
    giant "GAHHH!?"
    scene 135_s99 with dissolve
    giant "BLAAGHGH!"
    play sound "sound_effects/body/injured_fall.mp3"
    scene 135_s100 with dissolve
    mc "Die already!"
    scene 135_s101 with Dissolve(0.3)
    play sound "sound_effects/sword/hard_slash2.mp3"
    scene 135_s101 with vpunch
    giant "*gag* NGHNNNN!"
    scene 135_s102 with Dissolve(1.0)
    mc "One down. One to go."
    play sound "sound_effects/body/giant_roar.mp3"
    scene 135_s103 with Dissolve(1.0)
    giant "ROAAAHHHHHH!"
    if mc_karma >= 5:
        mc "Angry that I killed your brother? Imagine how the families of those soldiers felt then."
    else:
        mc "Angry that I killed your brother? Don't worry, you'll be joining him soon enough."
    play sound "sound_effects/woosh2.mp3"
    scene 135_s104 with Dissolve(0.3)
    scene 135_s104 with vpunch
    mc "Too slow."
    play sound "sound_effects/sword/stab4.mp3"
    scene 135_s105 with vpunch
    giant "NGAAHHHH!"
    scene 135_s108 with dissolve
    mc "Nghnn!"
    scene 135_s106 with Dissolve(0.3)
    play sound "sound_effects/woosh1.mp3"
    scene 135_s106 with vpunch
    mc "This is for every soldier you crushed. Every family you destroyed. Every life you ended. This is for everyone who ever stood against you and fell."
    scene 135_s107 with Dissolve(0.3)
    play sound "sound_effects/stab01.mp3"
    scene 135_s107 with vpunch
    perception "Your blade sinks into his skull. The giant goes rigid. The light in his eyes dim. The massive body beneath you shudders once, then goes still."
    scene 135_s109 with Dissolve(2.0)
    mc "...It's done."
    scene 135_s110 with Dissolve(1.0)
    mc "Negumi! It's over! You can come down now!"
    stop music fadeout 1.0
    scene 135_s111 with Fade(1.0,1.0,1.0)
    play music "wind2.mp3" fadein 1.0 loop
    perception "The barrier around her dissolves into a shower of sparks. She collapses into your hands, limp and broken, blood spilling from the corners of her mouth."
    scene 135_s112 with dissolve
    mc "Negumi? Negumi, look at me. Will you be alright?"
    mc "Can you heal yourself? Can you—"
    scene 135_s111 with dissolve
    negumi "*cough* Just... just take me back... please. I don't want to die out here."
    scene 135_s112 with dissolve
    if mc_karma >= 5:
        mc "I got you. Let's get you back. You're going to be fine, you hear me?"
    else:
        mc "I got you."
    scene 135_s113 with dissolve
    mc "[horse]! Come here, girl! We need to move!"
    scene 135_s114 with Dissolve(1.0)
    mc "(Fuck, I feel so tired. Like I could sleep for a thousand years.)"
    minthra "Do not faint just yet. Something is coming."
    mc "(Huh? The giants are dead. We won. What could be worse than—)"
    stop music
    scene 135_s115 with dissolve
    play music "fear/beckoning.mp3" fadein 3.0 loop
    mc "Negumi?! Where are you?! What's happening?!"
    minthra "She is here. The one I warned you about. The one I have been hiding from."
    mc "Who?! Who is—"
    nueleth "So it is true. A devil has entered our realm."
    nueleth "A fragment of the old darkness, slumbering in the body of a mortal."
    nueleth "And that devil resides inside you. Twisted around your soul like a parasite."
    scene 135_s116 with dissolve
    mc "W-Who are you?!"
    nueleth "I don't care about your politics. Your wars. Your petty struggles. Let it all fade into nothing."
    nueleth "I exist to keep the balance. Between order and chaos. Between the mortal realm and the powers that would consume it."
    nueleth "And your existence, [mc], contradicts that very balance."
    scene 135_s117 with dissolve
    mc "Where are you hiding?! Reveal yourself! Let's talk!"
    shiver "You still feel the remnants of Minthra's full power coursing through your veins, yet it compares nothing gainst the presence around you."
    nueleth "However, I won't snuff out your life... yet. Perhaps you are exactly where the balance needs you to be. I have not yet decided."
    nueleth "If her presence grows—even for a tiny smidgen, then you will meet my wrath."
    nueleth "I will erase you from existence so completely that even the memory of you will fade from the minds of those who loved you."
    stop music fadeout 2.0
    scene 135_s118 with Dissolve(3.0)
    nueleth "You have been warned, [mc]. The choice is yours. The consequences are mine."
    play music "wind2.mp3" fadein 1.0 loop
    mc "..."
    minthra "Do you understand now? Why I hid myself for so long? Why I did not lend you more strength?"
    minthra "That is why. She—Nueleth, this planet's finest being, is why."
    minthra "She is the reason no devils exist anymore in this world."
    scene 135_s120 with Dissolve(1.0)
    minthra "Her power is immense. Vast beyond your comprehension. Strong enough to fully awaken me."
    minthra "That is your final goal, vessel. Let it be cemented in your brain that you will take her on someday. Once you become strong enough."
    minthra "But we will be more discreet from now on. Do not call on me unless there is no other choice. Do not let her feel my presence again."
    mc "..."
    scene 135_s119 with Dissolve(1.0)
    mc "(What the fuck, man!)"
    mc "(I'm caught between two Gods that can pull my soul apart like taffy!)"
    mc "(And I'm supposed to... what? Get strong enough to fight a being that makes Minthra look like a candle in the sun?!)"
    mc "(Goddammit, I'm starting to believe my old life wasn't so bad after all...)"
    scene 135_s121 with Dissolve(1.0)
    negumi "[mc]..."
    mc "Sorry, Negumi. I got distracted. I'll get us back to the palace, just hold on... a... little longer."
    play sound "sound_effects/body/armor_movement1.mp3"
    scene 135_s122 with vpunch
    mc "*weeze* W-What's happening? I'm... I'm losing all my strength!"
    minthra "Your body will not be able to sustain my power any longer. It is returning to normal."
    mc "(S-So what now? Do I... die?) *cough* (I... feel so tired... what happens if I... close my eyes?)"
    scene 135_s123 with Dissolve(2.0)
    minthra "Sleep. Along with my daughter."
    stop music fadeout 3.0
    scene black with Fade(1.5,1.0,1.5)
    play music "images/custom_gui/global/mainmenu/mainmenu_song.mp3" fadein 2.0 loop
    show expression "chapter1_journey_main" at center with dissolve
    window hide
    pause 0.5
    window show
    ""
    show chapter5_recap1 with dissolve
    if mc_agree_help_thulkin:
        "The ambush caught you off guard, but Thulkin's proposition had your attention from the first word. You agreed to help him and his sister raid the goblin camp. His laughter still rings through your ears."
    else:
        "After the sudden ambush, you told Thulkin and his sister to leave. Thulkin's expression hardened, but he honored your refusal."

    if mc_goblins_alex:
        show chapter5_recap2 with dissolve
        hide chapter5_recap1
        "You fought the goblins alongside Alex. Her blade danced with precision, every strike finding its mark, every movement purposeful."
    else:
        if mc_kiss_milesent: 
            show chapter5_recap4 with dissolve
            hide chapter5_recap1
            "You kissed Millicent beneath the moonlight, her pointed ears twitching at the contact. Wildflowers clung to the night air, their fragrance mingling with the memory of her lips."
        else:
            show chapter5_recap3 with dissolve
            hide chapter5_recap1
            "You fought the goblins with Millicent. Fire erupted from her palms, consuming them like dry kindling. But as the embers settled, you couldn't shake the feeling that you'd let something slip away."

    show chapter5_recap5 with dissolve
    hide chapter5_recap2
    hide chapter5_recap4
    hide chapter5_recap3
    if mc_killed_cheiftain:
        "You refused Minthra's commands and beheaded the goblin chieftain. Ridding the world of one less evil. You felt the presence inside you stir with displeasure."
    elif mc_influence_cheiftain_good: 
        "You rejected Minthra's bloodlust and reached the chieftain. The goblin's eyes widened with understanding before he slumped forward, forever changed for good."
    elif mc_influence_cheiftain_bad: 
        "Minthra's whispers slithered into the chieftain's ear, poison sweet as honey. He bent to her will, his mind no longer his own. A puppet, now, enslaved to your influence."

    show chapter5_recap6 with dissolve
    hide chapter5_recap5
    if mc_harem_serena:
        "You told Serena you'd be there for her—no matter what. Her fingers curled around yours, grip tightening as understanding dawned in her eyes. She knew exactly what that promise meant."
    else:
        "When Serena spoke of wanting someone, you said nothing. The moment passed, fragile, and she let it go without a fight."


    if mc_talked_nadia_leaving:
        if mc_convinced_nadia_stay:
            show chapter5_recap7 with dissolve
            hide chapter5_recap6
            "You followed Nadia home, listening as she spilled her struggles. Then, after a moment's hesitation, you closed the door. Literally. You made her stay, and promised to be the one who held her up."
        else:
            show chapter5_recap8 with dissolve
            hide chapter5_recap6
            "You followed Nadia home, and she told you everything—the weight she'd been carrying. But when the moment came, you left the door open. She slipped through. She's gone now, and you'll never know where the road took her."
    else:
        show chapter5_recap9 with dissolve
        hide chapter5_recap6
        "You saw Nadia leaving the city. She walked past you without a word, and you let her. No flinch. No call. Just silence."

    show chapter5_recap10 with dissolve
    hide chapter5_recap6
    hide chapter5_recap7
    hide chapter5_recap8
    hide chapter5_recap9
    if mc_promise_diana_queen:
        "You told Diana she would be queen. Your queen. A reward for helping you, for when the time was right."
    elif mc_promise_diana_harem:
        "You told Diana she would have a place in your harem as reward for helping you. She didn't refuse."
    elif mc_promise_diana_maid:
        "You told Diana she would be your personal maid. She tilted her head, considering, then smiled. It wasn't the future she'd envisioned—but it was a future where she'd be better off."
    else:
        "You shut her down. Diana meant nothing to you. Her help went unrewarded, and the light in her eyes dimmed. But she held her composure, even as something inside her fractured."
    
    if mc_helped_lena:
        show chapter5_recap11 with dissolve
        hide chapter5_recap10
        if mc_betray_lena:
            "Lena's face lit up when you offered to help her daughter. She trusted you too quickly. The moment coin entered the equation, you switched sides. She's dead now, and her daughter will never know why."
        else:
            if mc_convince_lena:
                "In the heat of her rage, you managed to calm Lena. Her sword lowered. Jenny and her father lived to see another day—because of you."
            else:
                "In the heat of her rage, you did nothing. The blade fell. The blood pooled. And you watched, silent and still."
    else:
        show chapter5_recap12 with dissolve
        hide chapter5_recap10
        if mc_killed_lena:
            "You refused to help Lena from the start. Choosing to help Jenny instead. She's dead now, and her daughter will never know why."
        else:
            "You refused to help Lena from the start. Choosing to help Jenny instead. She walked away, her daughter's future still hanging in the balance."

    if mc_freed_ruby:
        show chapter5_recap13 with dissolve
        hide chapter5_recap10
        hide chapter5_recap11
        hide chapter5_recap12
        "During your raid on Gheris's house, you found a document bearing Ruby's name. You demanded he revoke his ownership. His hand trembled as he signed her freedom away."

    show chapter5_recap14 with dissolve
    hide chapter5_recap10
    hide chapter5_recap11
    hide chapter5_recap12
    hide chapter5_recap13
    if mc_convince_alice:
        "You calmed lieutenant Alice as she hunted you. Her breathing steadied, and for a moment, she saw you not as a target, but as a person."
    elif mc_scare_alice:
        "You spoke her fears aloud, and lieutenant Alice fled. Terror flickered in her eyes as she vanished into the alleys, swallowed by the shadows."
    else:
        "You killed lieutenant Alice. Her body crumpled in the alley, and you walked away without looking back."

    show chapter5_recap15 with dissolve
    hide chapter5_recap14
    if mc_bought_brothel:
        "The brothel has a new owner—you. Vera handed over the keys with a smile after you proved yourself capable. [brothel_name] will never be the same."
    elif mc_failed_buy_brothel:
        "You stumbled through Vera's questions, and she sent you away. The brothel remains out of reach—a missed opportunity that might have served you well."
    else: 
        "You never learned about the brothel. An opportunity slipped through your fingers—a business that might have anchored you in the city."

    if mc_bought_brothel:
        show chapter5_recap16 with dissolve
        hide chapter5_recap15
        if mc_hired_ruby:
            if mc_hired_ruby_after_bj:
                "After freeing Ruby from Gheris's grip, you hired her as a worker in your new business. Although... not before she proved her enthusiasm in a very personal way."
            else:
                "After freeing Ruby from Gheris's grip, you hired her immediately. She started that same day—sharp-eyed and sharper-tongued, ready to prove herself."
        else:
            "After freeing Ruby from Gheris's grip, she arrived to you seeking help. But you turned her away. Who knows how long till she returns to her previous life and ends up in another trouble."

    if mc_princess_alex:
        if mc_princess_success:
            show chapter5_recap18 with dissolve
            hide chapter5_recap16
            hide chapter5_recap15
            "The princess breathes air that isn't tainted by the smell of alcohol. She's free, and the road to Nahraya stretches before her—wide open, full of promise."
        elif mc_princess_fail_early:
            show chapter5_recap17 with dissolve
            hide chapter5_recap16
            hide chapter5_recap15
            "Even before you set out to rescue the princess, you faltered. Not enough allies. Not enough strength. The cellar remains her prison."
        elif mc_princess_fail_late:
            show chapter5_recap18 with dissolve
            hide chapter5_recap16
            hide chapter5_recap15
            "You made the plan. You went through the sewers, saw the princess with your own eyes. But time ran out. You left her there—and because of that, Lewis and Joan still draw breath."


    if mc_princess_alex:
        show chapter5_recap19 with dissolve
        hide chapter5_recap18
        hide chapter5_recap17
        hide chapter5_recap16
        hide chapter5_recap15
        if mc_sacrifice_lewis_joan:
            "The clock ran dry. You made a choice that cost Lewis and Joan their lives. They paid for the princess's freedom with everything they had."
        else:
            "You slipped through the sewers without alerting anyone. Lewis and Joan live to fight another day."

    if mc_sat_with_alex:
        show chapter5_recap21 with dissolve
        hide chapter5_recap18
        hide chapter5_recap17
        hide chapter5_recap16
        hide chapter5_recap15
        hide chapter5_recap19
        "Alex finally opened up to you. Her heart poured out—all the fear, all the loneliness, all the things she'd never said aloud. She'll never forget that night."
    else:
        show chapter5_recap20 with dissolve
        hide chapter5_recap18
        hide chapter5_recap17
        hide chapter5_recap16
        hide chapter5_recap15
        hide chapter5_recap19
        "Alex looked away. She trusts you—but not enough to share what's truly in her heart. The distance between you remains."

    show chapter5_recap22 with dissolve
    hide chapter5_recap21
    hide chapter5_recap20
    if mc_killed_reham:
        if mc_intended_reham:
            "You left Yasmine to the mercy of those bandits. By doing so, you doomed Reham and her father. The family house now sits quiet. It was your choice. You knew what would happen."
        else:
            "You left Yasmine to the mercy of those bandits, and in doing so, doomed Reham and her father. The family house now sits quiet. Although you say you didn't mean it to happen—as if that matters."
    else:
        "You helped Yasmine when the bandits surrounded her. In doing so, you reunited a family. The food was delicious, and for a moment, everything felt right."
    
    if mc_princess_success:
        show chapter5_recap23 with dissolve
        hide chapter5_recap22
        if not mc_reb_breakup_final:
            if reb_pregnancy_fail:
                "The princess remains by your side, her affection deepening with every passing day. But the grief of her miscarriage lingers, and its shadow will hang over your relationship for as long as it lasts."
            else:
                "The princess stays by your side, her affection deepening with every passing day. For now, all is well between you."

        else:
            if reb_pregnancy_fail:
                "Rebecca still looks to you as her protector, trusting you despite the distance between you. But the princess still carries the grief of her miscarriage and the memory of the protector you once were."
            else:
                "The princess still looks to you as her protector, trusting you despite the distance between you."
    
    if not mc_princess_success:
        if mc_kiss_queen:
            show chapter5_recap25 with dissolve
            hide chapter5_recap24
            hide chapter5_recap22
            "You stood up and took the Queen's lips. Her surprise at your sudden affection still lingers in your mind. The taste of her, the warmth of her—it was everything you'd imagined and nothing you'd expected."

    show chapter5_recap26 with dissolve
    hide chapter5_recap25
    hide chapter5_recap24
    hide chapter5_recap23
    hide chapter5_recap22
    if mc_let_prince_hand:
        "You allowed the prince to examine your new metal hand. He inspected it thoroughly, fascination evident in every touch."
        show chapter5_recap27 with dissolve
        hide chapter5_recap26
        if mc_told_truth_prince:
            "The prince flushed when you told him the truth about your erection. He still doesn't know what to make of it, or of you."
        else:
            "The anger in his eyes softened when you lied about your erection. He told you never to mention it again."
    else:
        "The prince's curiosity burned even brighter after you refused to let him touch your new hand."
    
    if not mc_princess_success:
        if mc_harem_queen:
            show chapter5_recap28 with dissolve
            hide chapter5_recap27
            hide chapter5_recap26
            "You finally reached her. The Queen's mind stirs—her city, her daughter, and... you. You live in her thoughts now, perhaps as a new lover."
        else:
            show chapter5_recap35 with dissolve
            hide chapter5_recap27
            hide chapter5_recap26
            "The Queen treats you with more respect now, but nothing has fundamentally changed. You're still her recruit, her steward. Nothing more."

    show chapter5_recap29 with dissolve
    hide chapter5_recap35
    hide chapter5_recap26
    hide chapter5_recap27
    if mc_convince_vic:
        if mc_vic_fee:
            "You reformed the thugs who had been terrorizing the city's people. But not without a price—a consequence for killing one of Vic's men. The ledger is balanced. For now."
        else:
            "You reformed the thugs who had been terrorizing the city's people. No blood was spilled. The market breathes easier now."
    else:
        "Your metal fingers pierced Vic's throat, killing him instantly. His men followed soon after. Your mind still wonders what truly happened that day."

    
    if not mc_killed_reham:
        show chapter5_recap30 with dissolve
        hide chapter5_recap29
        if mc_kiss_yasmine:
            "You took her lips, and she took yours. This budding relationship with Yasmine might prove risky. Perhaps you should keep it hidden for now."
        elif mc_rejected_yasmine:
            "You didn't allow Yasmine to be with you. She understood—but it still hurt. You saw it in the way she folded her hands, the way she looked away."
        elif mc_scared_yasmine:
            "Your terrible attempt at flirtation made things worse. Yasmine is now uncomfortable around you. The warmth you once shared has curdled into awkwardness."
        else:
            "You let Yasmine go. Perhaps you didn't want to bring more trouble to her failing marriage. Or perhaps you simply weren't interested."

    if not mc_killed_reham:
        show chapter5_recap31 with dissolve
        hide chapter5_recap30
        hide chapter5_recap29
        if mc_harem_reham_true:
            "No longer a servant or a friend. Reham is now your lover, through and through. She'll follow you to the ends of the desert—and beyond."
        elif reham_rejected_mc:
            "You confessed your true feelings to Reham. She shut you down—not as a master, but as a lover. The sensible one remains sensible."
        else:
            "You never made a move on Reham. When things finally return to normal, she will likely stay with her parents."
    
    if mc_harem_maia_true:
        show chapter5_recap32 with dissolve
        hide chapter5_recap31
        hide chapter5_recap30
        hide chapter5_recap29
        "You lifted Maia from her gloom and set her atop a mountain where she finally broke free of her fear. She owes you her life, her soul, and... her body."
    else:
        show chapter5_recap33 with dissolve
        hide chapter5_recap31
        hide chapter5_recap30
        hide chapter5_recap29
        "You left her to her thoughts. And her thoughts are slowly killing her. The breaking point is near, and you may not be there when it comes."

    show chapter5_recap34 with dissolve
    hide chapter5_recap33
    hide chapter5_recap32
    hide chapter5_recap31
    hide chapter5_recap30
    hide chapter5_recap29
    if mc_encouraged_negumi:
        "You encouraged Negumi when she faltered. Your words lit a fire in her that even the desert winds couldn't extinguish."
    else:
        "You offered no comfort to Negumi. She rides with you in silence, her shoulders hunched, her fire dimmed."
    
    if reham_pregnant:
        $ pregnancies += 1
    if jenny_pregnant:
        $ pregnancies += 1
    if lena_pregnant:
        $ pregnancies += 1

    hide chapter5_recap34 with dissolve
    show chapter4_recap18 with dissolve

    if pregnancies == 9:
        "[pregnancies] out of 9 available women are now expecting. Looks like you're single-handedly repopulating the world..."
    elif pregnancies >= 5:
        "You've knocked up [pregnancies] of the 9 available lovely ladies. Leave some for the rest of us, stud!"
    elif pregnancies >= 1:
        "[pregnancies] out of 9 available women are carrying your child. Someone's been a busy bee, haven't they?"
    else:
        "You haven't impregnated a single woman so far. Are you feeling okay? Or just... responsible?"

    show chapter1_recap12 with dissolve
    "You have [mc_coin] coins to your name, and your honor stands at [mc_karma] out of 10. Whatever that means."

    scene chapter6 with Fade(1.5,0.5,1.5)
    ""
    window hide
    stop music fadeout 1.5
    scene 136_s1 with Fade(1.0,1.0,1.0)
    call screen update0_5_0_end with Dissolve(1.3)
    


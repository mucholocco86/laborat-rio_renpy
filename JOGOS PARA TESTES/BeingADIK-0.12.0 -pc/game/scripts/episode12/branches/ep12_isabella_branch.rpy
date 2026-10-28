label ep12_bella_lib_label:
play music "music/ep2/journey_of_hope.mp3"
$ guideSuggestedPage = 233
scene ep12_bella_lib1 with wipeleft
$ renpy.pause()
scene ep12_bella_lib2 with dissolve
mc "Hey... Slow day?"
if ep4_toldDerekAboutJade:
    scene ep12_bella_lib3 with dissolve
    isa "No. It's been eventful."
    scene ep12_bella_lib4 with dissolve
    mc "I'm glad I caught you. I'm here to study, but..."
    mc "We...uh...should talk."
    scene ep12_bella_lib5 with dissolve
    mc "There's something I need to tell you... Something that you should hear from me first..."
    scene ep12_bella_lib6 with dissolve
    isa "I talked to Sage and Jill about an hour ago."
    scene ep12_bella_lib7 with dissolve
    mc "Then you already know..."
    scene ep12_bella_lib8 with dissolve
    isa "What I don't get is why it took you this long to tell me."
    scene ep12_bella_lib11 with dissolve
    mc "Mainly because I was ashamed. When I realized Jade was Sage's mom, the damage was already done."
    scene ep12_bella_lib8 with dissolve
    isa "So, if she weren't her mother, it wouldn't have been a big deal to do that to Jade?"
    scene ep12_bella_lib11 with dissolve
    mc "Of course, it was..."
    scene ep12_bella_lib8 with dissolve
    isa "Would you have done that to me?"
    scene ep12_bella_lib7 with dissolve
    mc "No! It was during Hell Week, Bella... You did things you're ashamed of, too, right?"
    scene ep12_bella_lib6 with dissolve
    isa "You know I did, but they aren't comparable to this. *{i}Sigh{/i}*"
    isa "Your moral compass is broken, [name]. And I suppose mine needs a tune-up too."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        $ breakup.append("Isabella")
        scene ep12_bella_lib10 with dissolve
        mc "I made a big mistake."
        mc "I don't think Sage will forgive me for it... Please, don't tell me you won't either."
        scene ep12_bella_lib9 with dissolve
        isa "I wish I could tell you no, [name]. But I can't."
        isa "Besides, why does it matter to you? You've made your choice about us already."
        scene ep12_bella_lib10 with dissolve
        mc "Yeah, but that was different. I'm still in love with my ex-girlfriend Zoey."
        scene ep12_bella_lib9 with dissolve
        isa "The reason doesn't matter. It doesn't make it hurt less."
        isa "And in combination with Jade and Sage..."
        isa "Honestly, I think it's for the best that we both move on."
        scene ep12_bella_lib7 with dissolve
        mc "I can't let this go. You mean a lot to me."
        scene ep12_bella_lib8 with dissolve
        isa "You can't have it both ways, [name]. It doesn't work like that."
        scene ep12_bella_lib9 with dissolve
        isa "If it helps you move on, I don't wish to be with you either."
        isa "Whatever we had... It's over."
        scene ep12_bella_lib16 with dissolve
        $ renpy.pause()
        $ new_bio("Isabella", "I broke up with Bella to be with Zoey. Bella had learned about what I did with Jade and was severely disappointed in me.")
    else:
        scene ep12_bella_lib9 with dissolve
        isa "It's too much."
        scene ep12_bella_lib10 with dissolve
        mc "We're not breaking up over this, right?"
        scene ep12_bella_lib9 with dissolve
        isa "It doesn't bring us closer, [name]."
        scene ep12_bella_lib10 with dissolve
        mc "I care so much about you, Bella. I made a big mistake."
        mc "I don't think Sage will forgive me for it... Please, don't tell me you won't either."
        scene ep12_bella_lib8 with dissolve
        isa "I wish I could tell you no, [name]. But I can't. I need some time to process this."
        isa "I have to ask you to give me space."
        scene ep12_bella_lib16 with dissolve
        $ renpy.pause()
        $ new_bio("Isabella", "Bella had learned about what I did with Jade and was severely disappointed in me.")
else:
    scene ep12_bella_lib3 with dissolve
    isa "Hi. Not exactly. The library is always extra busy during finals week."
    scene ep12_bella_lib4 with dissolve
    mc "Ah... Of course."
    scene ep12_bella_lib3 with dissolve
    isa "But most of the students don't ask for my help. So, I've got ample time to do what I need to do."
    isa "I take it you're here to study, too."
    scene ep12_bella_lib4 with dissolve
    mc "I am, but I also needed to talk to you."
    scene ep12_bella_lib3 with dissolve
    isa "Follow me."
    scene ep12_bella_lib5 with dissolve
    mc "How are you feeling?"
    scene ep12_bella_lib6 with dissolve
    isa "I've been experiencing emotional whiplash. How about you?"
    if branchZoey and not wt_ep11_zoey_kiss_others:
        $ breakup.append("Isabella")
        scene ep12_bella_lib7 with dissolve
        mc "It's the same for me... I feel low."
        mc "I came here because we need to talk...and I didn't want to do it over the phone."
        scene ep12_bella_lib6 with dissolve
        isa "[name]. You already told me face-to-face."
        scene ep12_bella_lib7 with dissolve
        mc "But I didn't tell you the reason."
        scene ep12_bella_lib8 with dissolve
        isa "I don't need to hear it because I can come up with several reasons of my own why it's the smartest choice."
        isa "Hearing myself talk with you guys about James, my daughter, and everything that followed..."
        isa "It's too much for us to handle. Isn't it?"
        scene ep12_bella_lib11 with dissolve
        mc "It's a lot, but I had made up my mind before you told me that."
        mc "And now I feel worse because I'm hurting you further... And you don't deserve it."
        mc "I wanted to make sure that you understood that it's not because of you..."
        scene ep12_bella_lib10 with dissolve
        mc "I'm still in love with my ex-girlfriend Zoey. And she's in love with me, too."
        scene ep12_bella_lib9 with dissolve
        isa "Neither reason would make it hurt less, [name]. The outcome is the same."
        isa "That's why you didn't have to share it with me."
        scene ep12_bella_lib10 with dissolve
        mc "You told me that you were drowning...and that I was your air..."
        mc "I'm worried, Bella."
        isa "..."
        scene ep12_bella_lib9 with dissolve
        isa "I did say that. And I meant it."
        isa "Just like how I don't want you to treat me differently because of my past, I don't want you to stay with me out of pity."
        scene ep12_bella_lib10 with dissolve
        mc "Pity? I don't pity you, I-"
        scene ep12_bella_lib6 with dissolve
        isa "You don't have to worry."
        isa "It hurts... But I've been through much worse. I can handle this."
        scene ep12_bella_lib11 with dissolve
        mc "Are you sure?"
        scene ep12_bella_lib9 with dissolve
        isa "Let it go, [name]. And so will I."
        scene ep12_bella_lib11 with dissolve
        $ renpy.pause()
        scene ep12_bella_lib7 with dissolve
        mc "I can't let this go. You mean a lot to me."
        scene ep12_bella_lib8 with dissolve
        isa "You can't have it both ways, [name]. It doesn't work like that."
        scene ep12_bella_lib9 with dissolve
        isa "If it helps you move on, I don't wish to be with you either."
        isa "Whatever we had... It's over."
        scene ep12_bella_lib16 with dissolve
        $ renpy.pause()
        $ new_bio("Isabella", "I broke up with Bella to be with Zoey. She was mature about it, but seemed hurt and annoyed.")
    else:
        scene ep12_bella_lib7 with dissolve
        mc "I understand. I'm hanging in there."
        mc "Thank you for the party again."
        scene ep12_bella_lib12 with dissolve
        isa "At least it ended well."
        scene ep12_bella_lib7 with dissolve
        mc "Yeah."
        scene ep12_bella_lib8 with dissolve
        isa "Was there something on your mind?"
        scene ep12_bella_lib7 with dissolve
        mc "A lot of questions, but I don't know how to ask them."
        mc "Or maybe I already know the answers."
        scene ep12_bella_lib6 with dissolve
        isa "Please, tell me what you're thinking."
        scene ep12_bella_lib7 with dissolve
        mc "It's about James..."
        mc "I know that he's not been around and all, and I've made up scenarios in my head that don't match reality."
        mc "I always thought that he had left you somehow..."
        scene ep12_bella_lib6 with dissolve
        isa "Well, he did."
        scene ep12_bella_lib7 with dissolve
        mc "Yes, but in another sense. In an unhappy way... I mean, not that the way it happened was happy, but..."
        scene ep12_bella_lib8 with dissolve
        isa "I get what you mean. You thought I was in an unhappy marriage."
        scene ep12_bella_lib7 with dissolve
        mc "Exactly."
        mc "And that thought made me feel confident about us."
        scene ep12_bella_lib11 with dissolve
        mc "And now that I realized that you two were in love when he left you... And that your relationship ended, or...was put on pause?"
        mc "Fuck, I don't even know how to say it."
        scene ep12_bella_lib6 with dissolve
        isa "Go on."
        scene ep12_bella_lib7 with dissolve
        mc "After I realized it had ended and neither of you wanted it to..."
        mc "Uh..."
        mc "You're still in love with him... Aren't you?"
        scene ep12_bella_lib11 with dissolve
        isa "..."
        mc "And... If he's alive... He's still in love with you."
        scene ep12_bella_lib7 with dissolve
        mc "And that scares me. How do I handle that?"
        mc "How can I...uh...compete? Compare? Uh..."
        mc "I panic when I think about it."
        scene ep12_bella_lib10 with dissolve
        mc "Do you get what I mean, or did I explain it poorly?"
        scene ep12_bella_lib9 with dissolve
        isa "I understand you."
        isa "And what you say is true."
        scene ep12_bella_lib10 with dissolve
        mc "*{i}Sigh{/i}* Fuck..."
        scene ep12_bella_lib8 with dissolve
        isa "And you should know that I've been fighting the same battle in my head when I'm with you."
        scene ep12_bella_lib7 with dissolve
        mc "Like how?"
        scene ep12_bella_lib8 with dissolve
        isa "How can I feel for someone else when I'm already in love?"
        isa "Am I cheating on my husband with you?"
        scene ep12_bella_lib9 with dissolve
        isa "If he's still alive, I am. But if he's not... Am I moving on?"
        scene ep12_bella_lib6 with dissolve
        isa "Like I told you... The days we spent together, we spent without a guide to follow."
        isa "The way you and I have built our relationship... I feel like there's no right or wrong answer."
        scene ep12_bella_lib14 with dissolve
        isa "You have your concerns, and I have mine."
        isa "But we also have feelings for each other, and plenty of reasons to say what we do together is wrong."
        scene ep12_bella_lib12 with dissolve
        isa "I'd ask you to feel for yourself what your heart desires, [name]."
        isa "Because the only one who can answer that is you."
        if tc < 5 or persistent.no_cheater:
            scene ep12_bella_lib13 with dissolve
            mc "I care so much about you, Bella."
            scene ep12_bella_lib12 with dissolve
            isa "I know. And it's ok to not know what to do."
        scene ep12_bella_lib7 with dissolve
        mc "What about you? What will you do?"
        scene ep12_bella_lib8 with dissolve
        isa "I hope I'll be able to answer that same question one day."
        scene ep12_bella_lib15 with dissolve
        $ renpy.pause()
        $ new_bio("Isabella", "I talked to Bella about my concerns regarding her past. We didn't reach any clarity in what that meant for us.")
scene ep12_lib1 with dissolve
$ renpy.pause()
jump ep12_libb_label

label ep12_bella_solo_label:
play music "music/ep12/licensed_music/track208.mp3"
if ep4_toldDerekAboutJade:
    scene ep12_bella_solo1 with fade
    mc "(I can probably guess what's on Bella's mind...)"
    mc "(It's all that's been on my mind since Sage found out what I did.)"
    scene ep12_bella_solo2 with dissolve
    mc "(Put me out of my misery already...)"
else:
    scene ep12_bella_solo1 with fade
    mc "(I wonder what's on Bella's mind...)"
    if tc > 4 and not persistent.no_cheater:
        mc "(I still think our situation is too much to handle.)"
        mc "(The more I think about it, the more I'm sure. I can't have it like this.)"
        scene ep12_bella_solo2 with dissolve
        mc "(She's still in love with her husband, and I'm flirting with others.)"
        mc "(I feel like that's not how it's supposed to be when you're in a relationship.)"
    else:
        mc "(I'm still unsure about how to handle our situation.)"
        mc "(And when I think about what's bothering me, it's quite clear...)"
        scene ep12_bella_solo2 with dissolve
        mc "(She's still in love with her husband.)"
        mc "(And me... I'm in love with her.)"
        mc "(Fuck... It's not supposed to be that way in a relationship.)"
        mc "(And I don't know what to do about it.)"
play sound "sound_effects/season3/glass_knock.mp3"
"*{i}Knocking{/i}*"
play sound "sound_effects/season3/door_slide.mp3"
scene ep12_bella_solo3 with dissolve
mc "Welcome..."
mc "Finally done with the test, huh?"
scene ep12_bella_solo4 with dissolve
isa "Yes. It was a long day. I bet yours was too."
scene ep12_bella_solo5 with dissolve
mc "Yep... I have a slight headache from focusing too much."
mc "Did you ever get that back when you were in college?"
scene ep12_bella_solo6 with dissolve
isa "I remember getting sleepy after my tests. They do a good job of draining your energy."
scene ep12_bella_solo7 with dissolve
mc "Yeah... How are you?"
scene ep12_bella_solo8 with dissolve
isa "I didn't come here to talk about the test. I...uh..."
isa "I think it's time we have a talk, you and I."
isa "Just us, with no one else around."
scene ep12_bella_solo7 with dissolve
mc "I think we need it. Get yourself comfortable. Can I get you anything? Coffee?"
scene ep12_bella_solo6 with dissolve
isa "I wouldn't say no to a cup, thanks."
if ep4_toldDerekAboutJade:
    $ breakup.append("Isabella")
    scene ep12_bella_solo9 with dissolve
    isa "I got together with the girls, and we talked about what you did."
    scene ep12_bella_solo10 with dissolve
    mc "With everyone?"
    scene ep12_bella_solo9 with dissolve
    isa "With Sage, Jill, Josy and Maya."
    isa "We tried to make sense of it all. And while we could find some understanding of why it happened, that doesn't mean we could accept it."
    scene ep12_bella_solo11 with dissolve
    mc "..."
    scene ep12_bella_solo13 with dissolve
    isa "You've done something terrible, [name], and you're smart enough to know it."
    isa "Having sex with Jade... I get it. I can't say I don't because I'm sitting on this couch with you."
    scene ep12_bella_solo15 with dissolve
    isa "And it's not that I take issue with. Why did you have to record it and show it to your friends?"
    scene ep12_bella_solo12 with dissolve
    mc "It was for Hell Week. They needed proof that I did that, but I shouldn't have given it to them."
    scene ep12_bella_solo13 with dissolve
    isa "Bingo. You shouldn't."
    scene ep12_bella_solo14 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "Blame the alcohol \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "It doesn't help that I was constantly buzzed from beer all that week."
            scene ep12_bella_solo15 with dissolve
            isa "No, [name]. You can't blame it on alcohol. It wasn't the alcohol that did all that. It was you."
        "Own it \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "I made a mistake. And I will live with that forever."
            scene ep12_bella_solo15 with dissolve
            isa "Yes, you did."
    isa "You're allowed to make mistakes; everyone makes them."
    isa "But the mistakes also come with consequences. Your actions affect others in ways that could be permanent."
    scene ep12_bella_solo20 with dissolve
    isa "I'm not going to speak on behalf of the rest of the girls, but from what I heard during our talk, it sounded like a group of girls who were severely disappointed in you."
    isa "They saw you as a close friend, someone they adored, and now they fear they can't go back to that."
    scene ep12_bella_solo19 with dissolve
    isa "I know you're not a rotten person. I know you have many great sides, and we have had a wonderful time together."
    isa "But even I was affected by this. And I had to ask myself what I am doing together with you."
    scene ep12_bella_solo26 with dissolve
    isa "I started imagining how I would feel if I were Jade, or if you ever put me in a similar situation."
    isa "While Jade and I are different, we do share similarities. And those similarities made this feel all too real."
    scene ep12_bella_solo21 with dissolve
    mc "I would never do that to you, Bella."
    scene ep12_bella_solo20 with dissolve
    isa "I want to believe that. But I also have proof that you could slip up detrimentally."
    isa "You and I are far from a perfect couple. We're no fairytale; we've faced challenges since day one."
    isa "I think this is a sign that we shouldn't be together."
    scene ep12_bella_solo21 with dissolve
    mc "So, you're breaking up with me after all?"
    scene ep12_bella_solo19 with dissolve
    isa "It pains me to do this. I won't feel better from doing it, but I know myself. I can't forget what you did."
    scene ep12_bella_solo29 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo22 with dissolve
    mc "I'm so sorry."
    scene ep12_bella_solo30 with dissolve
    isa "I know. And I forgive you."
    isa "And I wish you nothing but the best."
    scene ep12_bella_solo45 with dissolve
    mc "{i}When Bella broke up with me, I couldn't blame her.{/i}"
    mc "{i}I regretted what I had done, and what I had failed to do was to realize how many were affected by my mistake.{/i}"
    stop music fadeout 3
    mc "{i}Sometimes in life, you don't get a second chance.{/i}"
    $ new_bio("Isabella", "Bella broke up with me. What I had done to Jade and Sage was too much to deal with, on top of the other challenges we already faced.")
    
    
    if ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
        $ guideSuggestedPage = 254
        jump ep12_sage_solo_label
    else:
        jump ep12_dikmas_label
    jump ep12_dikmas_label
else:
    scene ep12_bella_solo9 with dissolve
    isa "So... Where do we begin?"
    scene ep12_bella_solo10 with dissolve
    mc "*{i}Sigh{/i}* I feel like I'll be all over the place. But we have to start somewhere..."

$ temp_list = [False, False, False, False]
label ep12_bella_solo_loop_label:
if not False in temp_list:
    jump ep12_bella_solo_cont_label

scene ep12_bella_solo11 with dissolve
menu:
    "About James" if not temp_list[0]:
        $ temp_list[0] = True
        scene ep12_bella_solo12 with dissolve
        mc "I'd like to talk some more about James. And I'm afraid my questions might come off as insensitive, but I have to ask them..."
        scene ep12_bella_solo13 with dissolve
        isa "What do you want to know?"
        scene ep12_bella_solo12 with dissolve
        mc "It's been a long time since he went missing, right?"
        scene ep12_bella_solo13 with dissolve
        isa "Longer than three years."
        scene ep12_bella_solo12 with dissolve
        mc "And after he disappeared and you got that call about it... Did you hear any news?"
        scene ep12_bella_solo18 with dissolve
        isa "After he went missing, a case was opened to find him. And I got support from a case manager who handled the economics and everything surrounding it."
        isa "But any news of his whereabouts or progress on their search was limited."
        scene ep12_bella_solo19 with dissolve
        isa "At first, it felt comforting knowing that they were actively searching for him."
        isa "But as time passed, it got me upset that they didn't manage to find him."
        scene ep12_bella_solo20 with dissolve
        isa "I called and pleaded. I asked for any signs of life or new information. I wanted them to give me something to hold on to..."
        isa "But they couldn't tell me anything I didn't already know."
        scene ep12_bella_solo21 with dissolve
        mc "So, he could still be alive, or he could have been dead all this time, and you wouldn't know."
        scene ep12_bella_solo18 with dissolve
        isa "Living with that ambiguity has been the hardest part."
        isa "I compared it to the loss of my parents, and losing James has been way worse."
        scene ep12_bella_solo19 with dissolve
        isa "With my parents - as hard as that was - at least it was final. I could grieve them knowing that they wouldn't come back."
        isa "There was closure, and there was acceptance."
        isa "But with James, I don't have any closure. There's no comfort to be had from thinking that he's alive and captured, or tortured, or...or..."
        scene ep12_bella_solo20 with dissolve
        isa "And there's no comfort from thinking that he's dead and never to be found either."
        scene ep12_bella_solo21 with dissolve
        mc "I can't imagine how horrible that must feel for you."
        mc "If we assume that he's not coming back..."
        mc "Sorry... I know it's not something you want to think about."
        scene ep12_bella_solo20 with dissolve
        isa "Go on."
        scene ep12_bella_solo21 with dissolve
        mc "If we assume that he's not coming back, what are your plans? Do you intend to stay married to him, or what is the process here?"
        scene ep12_bella_solo18 with dissolve
        isa "I've had it explained to me. In a couple of years from now, if he's still missing, he can be declared deceased."
        isa "If that happens, our marriage will be dissolved. There's also an option for me to divorce him before that."
        scene ep12_bella_solo19 with dissolve
        isa "But I haven't thought about going through with either of those processes."
        scene ep12_bella_solo22 with dissolve
        mc "Why not?"
        scene ep12_bella_solo19 with dissolve
        isa "Because I never wanted them. I wanted to stay married to him, and I wanted him to be alive."
        scene ep12_bella_solo28 with dissolve
        $ renpy.pause()
        jump ep12_bella_solo_loop_label
    "About her daughter" if not temp_list[2]:
        $ temp_list[2] = True
        scene ep12_bella_solo12 with dissolve
        mc "Can we talk about your child? Um... Your daughter."
        scene ep12_bella_solo14 with dissolve
        mc "I know it's not easy for you, but if I don't ask..."
        scene ep12_bella_solo15 with dissolve
        isa "I know. We'll keep avoiding it."
        isa "But [name], this is a difficult topic for me."
        scene ep12_bella_solo14 with dissolve
        mc "I get it..."
        scene ep12_bella_solo15 with dissolve
        isa "We talked about naming her Emily. I lost her due to the trauma I faced during pregnancy."
        scene ep12_bella_solo12 with dissolve
        mc "And you kept her nursery in that way for James, yeah? And you locked the door to it."
        scene ep12_bella_solo13 with dissolve
        isa "Yes."
        scene ep12_bella_solo12 with dissolve
        mc "I don't understand why."
        scene ep12_bella_solo18 with dissolve
        isa "I believe I told you why. I felt like I had to leave it that way for James."
        scene ep12_bella_solo22 with dissolve
        mc "That must have been painful for you to do. Why would you keep it that way for him?"
        mc "You lost Emily already. But you kept that constant reminder of her in your home."
        scene ep12_bella_solo23 with dissolve
        mc "And you didn't even tell Jill about that room. And again... You locked it."
        mc "I have a hard time understanding why you would do that to yourself."
        mc "It's something that won't make you feel better. Right?"
        scene ep12_bella_solo22 with dissolve
        mc "You can't possibly look at that room with joy. And it's a constant reminder of your loss."
        mc "To me, it doesn't sound healthy. Can you help me understand it?"
        scene ep12_bella_solo19 with dissolve
        isa "It's just been me alone in that house, [name]."
        isa "A part of me knows that her nursery keeps me grieving, but I don't have the power to turn that room into anything else."
        scene ep12_bella_solo18 with dissolve
        isa "It used to be my parents' bedroom. Now they rest in their urns in that room."
        isa "I feel like they rest in there together with Emily's spirit."
        isa "And while the room itself makes me sad, I feel like I get comfort from those thoughts, too."
        isa "That they rest together in there, and that I can visit them when I feel the need."
        jump ep12_bella_solo_loop_label
    "About her attempted suicide" if not temp_list[3]:
        $ temp_list[3] = True
        scene ep12_bella_solo12 with dissolve
        mc "Bella, I'm worried about you."
        mc "You've been through so much that you decided to...to..."
        mc "Fuck, I can't even say the words."
        scene ep12_bella_solo30 with dissolve
        isa "I know."
        scene ep12_bella_solo31 with dissolve
        mc "It worries me that you already went to that dark place in your mind once before."
        mc "Could it happen again?"
        scene ep12_bella_solo32 with dissolve
        isa "I'm ashamed of what I did to myself, [name]."
        isa "I've always thought of myself as someone brave and strong, but in that moment, I felt tiny and scared."
        isa "I can't rationalize it. I wasn't myself, and I wanted it to be over. I didn't want to feel that way anymore."
        scene ep12_bella_solo31 with dissolve
        mc "And what about after it happened? Did you still feel that way? And what about now?"
        scene ep12_bella_solo33 with dissolve
        isa "It was tough to wake up and realize what I had done. Sadness and regret set in instantly."
        isa "I got plenty of help to process what I went through. And that was what I needed."
        scene ep12_bella_solo34 with dissolve
        isa "When James went M.I.A., I was offered help too, but I declined it. If I had only accepted it to begin with, maybe it wouldn't have come to this."
        isa "But I can't know that for sure. What I do know is that the group sessions helped me heal."
        scene ep12_bella_solo33 with dissolve
        isa "You don't have to worry about me doing {b}that{/b} again."
        isa "Mentally, I'm in a much better place today."
        isa "Granted, I still have a hard time sharing, but I think I've proven lately that I'm getting there."
        scene ep12_bella_solo35 with dissolve
        isa "Most of it is thanks to Jill. But some of it is also thanks to you."
        jump ep12_bella_solo_loop_label
    "About Jill" if not temp_list[1]:
        $ temp_list[1] = True
        scene ep12_bella_solo12 with dissolve
        mc "I didn't realize how important Jill has been to you. I knew she was a close friend of yours, but she seems to be so much more to you than that."
        scene ep12_bella_solo16 with dissolve
        isa "Jill is my angel. After I met her, she quickly became pivotal to me."
        isa "She was so easy to talk to. She made me feel heard and supported."
        scene ep12_bella_solo17 with dissolve
        isa "But more importantly, she made me feel needed."
        scene ep12_bella_solo12 with dissolve
        mc "In what way?"
        scene ep12_bella_solo13 with dissolve
        isa "She had experienced loss, too. And loss isn't something you deal with once, and then you're done."
        isa "It's something that can keep you up at night and return to visiting you when you least expect it."
        scene ep12_bella_solo18 with dissolve
        isa "Jill had been fighting her own dark thoughts about Lana for many years."
        isa "She still has nightmares about it. And she can never forget the moment when they told her Lana had passed away."
        scene ep12_bella_solo19 with dissolve
        isa "And then, later in life, to learn that her parents had lied to her about how Lana died..."
        isa "That made it a lot worse for her."
        scene ep12_bella_solo18 with dissolve
        isa "We have spent many late nights talking about ourselves to one another."
        isa "Often dedicating a whole night to each other's thoughts."
        isa "And that's how I felt that I was needed. She needed me to listen and to give her input. She needed my comfort."
        scene ep12_bella_solo24 with dissolve
        isa "And that's why our bond is something special."
        isa "I am ashamed that I kept the nursery from her in our talks..."
        isa "But she was always understanding with me. She never pushed me beyond what I was willing to share with her."
        scene ep12_bella_solo25 with dissolve
        mc "Your relationship sounds...amazing. It makes me even sadder knowing it got tested when you and I got together..."
        if ep9_b_kissed_jill:
            scene ep12_bella_solo24 with dissolve
            isa "I know you had feelings for her, [name]."
            scene ep12_bella_solo25 with dissolve
            mc "I did, but-"
            scene ep12_bella_solo18 with dissolve
            isa "And I know you kissed her around Halloween."
            scene ep12_bella_solo25 with dissolve
            mc "Did she tell you that?"
            scene ep12_bella_solo18 with dissolve
            isa "She said you chose to be with me because you couldn't choose both of us."
            isa "And she said she had feelings for you, too."
            scene ep12_bella_solo29 with dissolve
            $ renpy.pause()
            scene ep12_bella_solo25 with dissolve
            mc "Why are you telling me this?"
            scene ep12_bella_solo18 with dissolve
            isa "Why haven't you told me?"
            scene ep12_bella_solo25 with dissolve
            mc "It's been complicated."
            scene ep12_bella_solo26 with dissolve
            isa "My relationship with Jill has also been complicated."
            scene ep12_bella_solo27 with dissolve
            mc "Hm? You mean because of what I did?"
            scene ep12_bella_solo26 with dissolve
            isa "Before we met you."
            scene ep12_bella_solo27 with dissolve
            mc "I'm confused... Did something happen between you two?"
            scene ep12_bella_solo26 with dissolve
            isa "Late nights... The need to feel comfort..."
            isa "It shouldn't have happened, but it did."
            scene ep12_bella_solo18 with dissolve
            isa "It's weird that the three of us have that in common."
            isa "And for reasons I can't quite explain, it made it even more difficult for me to see Jill miss out on you."
            scene ep12_bella_solo25 with dissolve
            mc "I don't know what to say... Um..."
            scene ep12_bella_solo26 with dissolve
            isa "*{i}Sigh{/i}* Me neither. I shouldn't have gotten into it."
        else:
            scene ep12_bella_solo24 with dissolve
            isa "We survived it."
        jump ep12_bella_solo_loop_label

label ep12_bella_solo_cont_label:

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if tc > 4:
                           "scrappy" "You have too many cheater points and Bella's path will end here (need less than 4)"
scene ep12_bella_solo36 with dissolve
mc "Thank you for sharing all this with me... I've learned a great deal about you from your answers."
scene ep12_bella_solo37 with dissolve
isa "It feels good to have told you. But also worrisome, because I'm scared about how you will react to all of it."
isa "I'm sure you have your concerns now."
scene ep12_bella_solo38 with dissolve
mc "What worries me is something you said... You said you wanted to stay married to James..."
mc "And, of course, you want him to still be alive."
scene ep12_bella_solo39 with dissolve
mc "But this increases the worry I already have. And I keep coming back to it..."
mc "What about me? What about us?"
if tc > 4  and not persistent.no_cheater:
    $ breakup.append("Isabella")
    mc "I have thought long and hard about this, and I've come to a realization."
    scene ep12_bella_solo40 with dissolve
    mc "You're still in love with your husband, and I've been flirting around with others."
    scene ep12_bella_solo43 with dissolve
    isa "You have?"
    scene ep12_bella_solo39 with dissolve
    if tc > 9  and not persistent.no_cheater:
        mc "Yeah... I have. A lot, actually."
    else:
        mc "Yeah... I have."
    mc "You don't do that when you're in a relationship."
    mc "And I also feel like it's a weird relationship to have when the one you're with loves someone else."
    scene ep12_bella_solo40 with dissolve
    mc "And that's what makes this so damned difficult."
    mc "I'm scared that I will do you more harm than good."
    scene ep12_bella_solo39 with dissolve
    mc "I'm scared that you won't be able to love me the way you love James, and I'm scared that I'm not worth the effort to begin with."
    mc "On top of that, we're doing something unethical that can land us both in trouble..."
    scene ep12_bella_solo40 with dissolve
    mc "I feel so thankful that you've opened up to me like this, and I don't want you to think it's because of opening up that I'm saying this to you now..."
    mc "But I don't believe we will last long-term. And I think it's best if we end it today."
    scene ep12_bella_solo41 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo44 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo42 with dissolve
    isa "I'm aware that I come with a truckload of baggage. And I buy into your reasoning."
    isa "But I have to admit, it hurts to hear that you've been up to no good while you were with me."
    isa "That's not something you should take lightly, [name]. Have you been cheating on me?"
    scene ep12_bella_solo41 with dissolve
    mc "I have done things I'm not proud of. Things you don't do when you're in a committed relationship."
    mc "It wasn't just one single thing I did, and it all depends on where you draw the line for cheating."
    scene ep12_bella_solo39 with dissolve
    mc "But I know that what I did, I wouldn't want you to do with someone else."
    mc "So, yeah... I've crossed lines I shouldn't have crossed."
    scene ep12_bella_solo40 with dissolve
    mc "I think I've felt that I'm not ready for a relationship. I mean, why else would I have done that?"
    mc "I could stand here lying to you and say that I only have eyes for you..."
    mc "But I have felt the temptation, and I've caved to it in a way that I'm not proud of."
    scene ep12_bella_solo41 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo42 with dissolve
    isa "[name]..."
    isa "We never stood a chance, did we?"
    scene ep12_bella_solo41 with dissolve
    mc "I'm afraid we have too much against us to make it last."
    scene ep12_bella_solo44 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo45 with dissolve
    mc "{i}And that's how I broke up with Bella...{/i}"
    mc "{i}It was a long and illuminating conversation, but ultimately, I had to do it.{/i}"
    stop music fadeout 3
    mc "{i}I knew it would hurt her, but I felt confident knowing that she would be ok without me.{/i}"
    $ new_bio("Isabella", "Bella sat down and told me everything I needed to know about her past.")
    $ new_bio("Isabella", "I broke up with Bella because I felt that my heart wasn't fully in it.")
else:
    $ roadIsabella = True
    scene ep12_bella_solo40 with dissolve
    mc "I'm scared that you won't be able to love me the way you love James."
    mc "And I know that's a harsh thing to ask for. But if love isn't the point of this...then what is?"
    scene ep12_bella_solo46 with dissolve
    isa "Are you with me because you really want love?"
    scene ep12_bella_solo47 with dissolve
    mc "I am. That's what I've realized."
    mc "It's ok if you don't feel the same, because I get it."
    mc "But I love you. And I love us. I want you to be able to feel that for me someday, too."
    scene ep12_bella_solo46 with dissolve
    isa "[name]..."
    if check_ilove():
        $ ep12_bella_love = True
        scene ep12_bella_solo48 with dissolve
        isa "I already feel that for you."
        scene ep12_bella_solo47 with dissolve
        mc "You do?"
        scene ep12_bella_solo48 with dissolve
        isa "Yes, of course."
        isa "I love you too."
        scene ep12_bella_solo49 with dissolve
        mc "Wow... That feels amazing to hear..."
    else:
        scene ep12_bella_solo48 with dissolve
        isa "That's lovely to hear. I'm not quite there yet, but I'm heading in that direction."
        scene ep12_bella_solo47 with dissolve
        mc "That's fine. All I need to know is that you might feel that way at some point."
        scene ep12_bella_solo48 with dissolve
        isa "I can't promise you anything, but I do have loving feelings for you."
        scene ep12_bella_solo49 with dissolve
        mc "Ok... I'll take that."
    scene ep12_bella_solo50 with dissolve
    isa "*{i}Sigh{/i}* But it doesn't make the situation easier for us. Because the rest is still true..."
    isa "I have been living on hope for so long that stopping to feel hope is a way of letting go."
    scene ep12_bella_solo52 with dissolve
    isa "And that's the hardest part for me. To let go."
    isa "I'm so torn. *{i}Sniffles{/i}*"
    scene ep12_bella_solo53 with dissolve
    mc "It's ok."
    mc "You have to live with this burden. And I'll help you carry it."
    scene ep12_bella_solo54 with dissolve
    mc "I'll have to live with it, too. I'll be brutally honest here; it will be hard for me."
    mc "But I want to do it. I really do."
    scene ep12_bella_solo50 with dissolve
    isa "Thank you, [name]. Thank you for making this easier for me."
    isa "I never wanted you to have to live with this uncertainty, too."
    scene ep12_bella_solo51 with dissolve
    isa "But stopping here and now with you... That's not an option either."
    isa "That would take away one of the few things I love about my life."
    isa "And that's not happening."
    scene anim_bella_kiss_ep12 with dissolve
    pause
    scene ep12_bella_solo55 with dissolve
    $ renpy.pause()
    scene ep12_bella_solo56 with dissolve
    mc "Then, we're on the same page."
    scene ep12_bella_solo57 with dissolve
    isa "And on to another chapter."
    scene ep12_bella_solo56 with dissolve
    mc "Yeah. Let's end that chapter on a high note. I wonder what the next one holds for us."
    scene ep12_bella_solo57 with dissolve
    isa "Well... First, you're going to have your winter break and I'll have mine."
    isa "After that, we'll pick it up from where we left off."
    scene ep12_bella_solo56 with dissolve
    mc "Would you...?"
    mc "Would you like to meet my dad?"
    scene ep12_bella_solo58 with dissolve
    isa "Are you sure about this?"
    scene ep12_bella_solo59 with dissolve
    mc "I'm rarely sure about things I blurt out like that..."
    mc "And I'm not sure how he would take it... But yeah..."
    scene ep12_bella_solo56 with dissolve
    mc "I don't want to keep this secret from him."
    mc "He's so important to me; as are you."
    scene ep12_bella_solo57 with dissolve
    isa "Then, I'd love to meet him."
    stop music fadeout 3
    scene ep12_bella_solo60 with dissolve
    $ renpy.pause()
    $ new_bio("Isabella", "Bella sat down and told me everything I needed to know about her past.")
    if ep12_bella_love:
        $ new_bio("Isabella", "I told her that I loved her and she reciprocated. We both wanted to continue our relationship despite everything that had happened.")
    else:
        $ new_bio("Isabella", "I told her that I loved her but she wasn't ready to say it back. We both wanted to continue our relationship despite everything that had happened.")
    $ mgallery_add_photo("ep12_bella_solo_pic1")
    
    if ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
        $ guideSuggestedPage = 254
        jump ep12_sage_solo_label
    else:
        jump ep12_dikmas_label
    
jump ep12_dikmas_label

label ep12_bhome_label:
play music "music/ep12/licensed_music/track209.mp3"
scene ep12_bhome1 with fade
isa "Isabella."
scene ep12_bhome3 with dissolve
dad "Isabella... I'm Neil."
scene ep12_bhome2 with dissolve
isa "[name] has told me plenty about you."
scene ep12_bhome3 with dissolve
dad "All good things, I hope."
scene ep12_bhome2 with dissolve
isa "He adores you."
scene ep12_bhome4 with dissolve
dad "That's always nice to hear."
dad "Come in. Coffee?"
scene ep12_bhome5 with dissolve
isa "I'd love some."
scene ep12_bhome4 with dissolve
dad "I'll get right on it."
scene ep12_bhome6 with dissolve
mc "Feeling nervous?"
scene ep12_bhome7 with dissolve
isa "I did, on my way over here. But he seems easy-going."
scene ep12_bhome6 with dissolve
mc "I tried to prepare him as well as I could without oversharing."
mc "He knows you're my teacher and that we met before that."
scene ep12_bhome7 with dissolve
isa "That's good to know. What else?"
scene ep12_bhome8 with dissolve
mc "He knows your age and that I love you."
scene ep12_bhome9 with dissolve
isa "You told him that?"
scene ep12_bhome8 with dissolve
mc "It felt like a natural thing to tell him. Shouldn't I have?"
scene ep12_bhome9 with dissolve
isa "I didn't expect you to tell him that part. But that was sweet of you."
scene ep12_bhome10 with dissolve
dad "Sugar or milk, Isabella?"
scene ep12_bhome11 with dissolve
isa "Neither thanks."
scene ep12_bhome13 with dissolve
dad "Kindred spirits, we all are."
dad "I've tried milk and sugar, but it didn't feel right. And I don't get all these coffee drinks that people go for these days."
dad "Grande latte and tall mochaccinos... Why can't coffee simply be small or large? Why do they have to complicate things?"
scene ep12_bhome12 with dissolve
isa "Well, I assume if they called it \"tepid bean juice\", they wouldn't sell as much."
scene ep12_bhome14 with dissolve
dad "HAHA! Now that's a catchy name. Some black, tepid bean juice is coming right up."
scene ep12_bhome15 with dissolve
play sound "sound_effects/season2/pour.mp3"
mc "Eww. It sounds disgusting that way."
scene ep12_bhome16 with dissolve
dad "Where are you from, Isabella?"
scene ep12_bhome22 with dissolve
isa "I'm a local."
scene ep12_bhome16 with dissolve
dad "You don't say. Well, I didn't fly too far from home either."
dad "This place has its charm."
scene ep12_bhome17 with dissolve
dad "[name] told me that you're a librarian."
scene ep12_bhome22 with dissolve
isa "You've been well-informed. I am."
scene ep12_bhome16 with dissolve
dad "Always has been?"
scene ep12_bhome23 with dissolve
isa "I went to college with that profession in mind. I love to read."
scene ep12_bhome17 with dissolve
dad "So do I. There's nothing better than ending the night with a book."
dad "It takes the mind to a different place. I find it easier to fall asleep after reading."
scene ep12_bhome22 with dissolve
isa "And you work in construction, right?"
scene ep12_bhome18 with dissolve
dad "I swing the old hammer."
scene ep12_bhome24 with dissolve
mc "Dad's been working in construction since his early teens."
scene ep12_bhome17 with dissolve
dad "It's a great job. People will always need housing and repairs."
dad "It takes its toll on the body, but I doubt I'd be in better shape without it."
scene ep12_bhome22 with dissolve
if ep5_painted_fence:
    isa "[name] once helped me paint my fence, and he's done a great job with his room at the fraternity."
else:
    isa "[name] has done a great job with his room at the fraternity."
isa "Your handy genes seem to run in the family."
scene ep12_bhome17 with dissolve
dad "That they do, but this one is too brilliant for me."
dad "I never had any aptitude for academia, but I'm happy he does."
scene ep12_bhome27 with dissolve
mc "What a boring world it would be if everyone liked the same things."
scene ep12_bhome21 with dissolve
dad "True. But I'm happy I could impart some wisdom to you. Nowadays, when he talks, I can't even understand half of what he says."
scene ep12_bhome23 with dissolve
isa "Haha."
scene ep12_bhome28 with dissolve
mc "Tsk. You're not stupid, Dad."
scene ep12_bhome18 with dissolve
dad "How was the bean juice?"
scene ep12_bhome24 with dissolve
mc "Can we stop calling it that?"
scene ep12_bhome23 with dissolve
isa "It hit the spot."
scene ep12_bhome19 with dissolve
dad "Good."
dad "Isabella... I must admit, I was taken aback when [name] told me about you."
dad "I don't want you to feel uneasy about it, but I'm sure you understand why I had some reservations."
scene ep12_bhome25 with dissolve
isa "I do. As I told [name], I felt a tad nervous coming here today."
isa "Our situation is out of the ordinary, for many reasons..."
isa "But in the end..."
scene ep12_bhome26 with dissolve
mc "It feels right."
scene ep12_bhome25 with dissolve
isa "It does. He can be mature when he wants to."
isa "I hope that I'm not putting you in a weird spot here."
scene ep12_bhome17 with dissolve
dad "That's empathetic of you. I'm not the one to lack empathy either. Granted, I just met you, but you seem genuine."
dad "Undeniably, this is a tad weird. But if this is something you both want..."
dad "Nothing makes me happier than seeing my son happy."
scene ep12_bhome28 with dissolve
mc "I'm relieved, Dad. Thank you."
mc "I had a lot of different scenarios playing in my head before I told you about Bella."
scene ep12_bhome20 with dissolve
dad "Oh, is Bella what you prefer to be called?"
scene ep12_bhome26 with dissolve
mc "Haha! It took me a while until she allowed me to call her that."
scene ep12_bhome25 with dissolve
isa "Friends and family have always called me Bella. You may too."
scene ep12_bhome20 with dissolve
dad "Bella, then."
scene ep12_bhome21 with dissolve
dad "You were saying?"
scene ep12_bhome28 with dissolve
mc "I thought you wouldn't receive the news of our relationship as well as you did."
scene ep12_bhome21 with dissolve
dad "Were you worried about my reaction?"
scene ep12_bhome27 with dissolve
mc "You mean the world to me. Of course, I was worried."
mc "But I also know that you're able to listen and understand. I don't think most would give us that benefit before judging us."
scene ep12_bhome21 with dissolve
dad "Life is too short to care about what others think."
dad "You live life your way. You're meant to experience love and heartbreak."
dad "If things work out between you, then great. If not, well, we learn plenty from making mistakes, too."
scene ep12_bhome25 with dissolve
isa "For what it's worth, I truly believe this is not a mistake."
scene ep12_bhome17 with dissolve
dad "Now that's heartwarming to hear."
stop music fadeout 3
scene ep12_bhome29 with dissolve
$ renpy.pause()
$ new_bio("Isabella", "Bella met my Dad and I was relieved when they got along.")
$ new_bio("Dad", "Dad met Bella and I was relieved when they got along.")
$ mgallery_add_photo("ep12_bella_solo_pic2")
jump ep12_jsolo_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

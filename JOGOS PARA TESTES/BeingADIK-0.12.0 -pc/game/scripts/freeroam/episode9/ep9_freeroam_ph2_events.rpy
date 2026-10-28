label ep9_jill_banana_event_label:
scene ep9_jill_banana1 with dissolve
mc "Haha! No way!"
scene ep9_jill_banana2 with dissolve
ji "Hey!!!"
ji "I'm a banana!"
scene ep9_jill_banana3 with dissolve
mc "You sure are! Could you have picked a bigger costume or what?"
scene ep9_jill_banana4 with dissolve
ji "I know! I started regretting it already."
scene ep9_jill_banana4b with dissolve
mc "I wanna give you a hug, but I can't reach around you while you're wearing this."
ji "Yeah, I don't think it's possible."
scene ep9_jill_banana4c with dissolve
mc "*{i}Smack{/i}*"
scene ep9_jill_banana7 with dissolve
ji "But what about you? What a great costume!"
scene ep9_jill_banana8 with dissolve
mc "Thanks! I'm a Spartan!"
scene ep9_jill_banana7 with dissolve
ji "Oh, I can tell! It's so good!"
ji "Do you get my hints about my costume now?"
scene ep9_jill_banana6 with dissolve
mc "Something you can eat and go?"
$ guideSuggestedPage = 63
scene ep9_jill_banana5 with dissolve
ji "Go bananas! Get it?"
scene ep9_jill_banana6 with dissolve
menu:
    "You look cute":
        mc "You look so cute in that!"
        scene ep9_jill_banana7 with dissolve
        ji "You think? I feel stupid in it."
    "You look silly":
        mc "You look so silly in that!"
        scene ep9_jill_banana7 with dissolve
        ji "Haha! I know! I feel so sluggish walking in it too!"
        ji "I have to duck under doorways."
scene ep9_jill_banana9 with dissolve
bia "[name]!!!"
scene ep9_jill_banana10 with dissolve
mc "Bianca! And Olivia! Hey!"
bia "This is so great! I've never been to your Halloween parties, but I've heard so much about them that we had to come this year."
scene ep9_jill_banana11 with dissolve
ji "You're looking at the party planner for this one."
scene ep9_jill_banana12 with dissolve
oli "You did all of this?"
mc "It's a group effort, but yeah, I've been planning the party with others."
scene ep9_jill_banana13 with dissolve
bia "That is so cool! You've gotta show us around!"
scene ep9_jill_banana14 with dissolve
mc "Sure, let's take a group tour. Just give me a minute."
mc "Get yourself something to drink. There's beer over there and punch in that hallway."
jump ep9_freeroam_diks_ph2_label

label ep9_diks_ph2_sally_event_label:
scene ep9_diks_ph2_sally_event1 with dissolve
sy "Whoa..."
scene ep9_diks_ph2_sally_event2 with dissolve
mc "How's it going there, Sally?"
scene ep9_diks_ph2_sally_event3 with dissolve
sy "..."
scene ep9_diks_ph2_sally_event4 with dissolve
sy "..."
scene ep9_diks_ph2_sally_event5 with dissolve
sy "..."
scene ep9_diks_ph2_sally_event6 with dissolve
mc "All right. Good talking to you."
scene ep9_diks_ph2_sally_event7 with dissolve
mc "Uh... Are you ok?"
scene ep9_diks_ph2_sally_event8 with dissolve
sy "It's spinning."
sy "Oh, so fast! Make it stop."
scene ep9_diks_ph2_sally_event9 with hpunch
mc "Um... Sally?"
scene ep9_diks_ph2_sally_event10 with dissolve
mc "Hello? Are you alive?"
scene ep9_diks_ph2_sally_event11 with dissolve
sy "Can you put me on the sofa?"
if affinity == "DIK":
    scene ep9_diks_ph2_sally_event12 with dissolve
else:
    scene ep9_diks_ph2_sally_event13 with dissolve
mc "Sure."
scene ep9_diks_ph2_sally_event14 with dissolve
mc "Do you want some water or something?"
scene ep9_diks_ph2_sally_event15 with dissolve
sy "No. I'm fine. Wooo..."
sy "I'm gonna grab some air and then-"
scene ep9_diks_ph2_sally_event16 with dissolve
sy "Hnmmngn..."
scene ep9_diks_ph2_sally_event17 with dissolve
mc "Karen! Karen!"
mc "Sally needs to puke. Can you take her outside?"
scene ep9_diks_ph2_sally_event18 with dissolve
mc "(That wasn't because of that drink...was it?)"
$ task_list[13] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_ssolo_event_label:
$ event_list.append("ep9_diks_ph2_jmtalk_event_label")
scene ep9_diks_ph2_ssolo_event1 with dissolve
ky "Um. Are the preps coming to the party?"
scene ep9_diks_ph2_ssolo_event5 with dissolve
sa "Hell no. They have their stupid High Society Halloween party tonight."
scene ep9_diks_ph2_ssolo_event2 with dissolve
av "Which one is that again?"
scene ep9_diks_ph2_ssolo_event6 with dissolve
sa "They put on stupid masks and robes and pretend to be \"superior and elite\". They fail to see the irony of doing that during Halloween."
scene ep9_diks_ph2_ssolo_event3 with dissolve
ky "Ok. I thought it didn't add up."
scene ep9_diks_ph2_ssolo_event7 with dissolve
sa "What doesn't add up?"
scene ep9_diks_ph2_ssolo_event3 with dissolve
ky "Jill Royce being here."
scene ep9_diks_ph2_ssolo_event8 with dissolve
sa "Ugh. Don't get me started because I don't get it either."
sa "I'm surprised Tybalt didn't go wherever she goes for once."
if ep7_ruined_presentation:
    scene ep9_diks_ph2_ssolo_event4 with dissolve
    ky "Speaking of your brother - haha! Christie told me about him putting a huge dick pic in his field study presentation."
    scene ep9_diks_ph2_ssolo_event9 with dissolve
    sa "Haha! Yeah, I was there! It was so fucking funny!"
    sa "The entire auditorium gasped, and he stood there, not realizing what he just did."
    scene ep9_diks_ph2_ssolo_event4 with dissolve
    ky "Was it really his dick?"
    if pathSage or ep7_pathSage:
        scene ep9_diks_ph2_ssolo_event9 with dissolve
        sa "No. It was a prank. Let's leave it at that."
    else:
        scene ep9_diks_ph2_ssolo_event8 with dissolve
        sa "Why would you ask me that? Eww!"

scene ep9_diks_ph2_ssolo_event10 with dissolve
sa "[name]! Come with me."
scene ep9_diks_ph2_ssolo_event11 with dissolve
mc "Where are we off to?"
sa "Your room."
if branchSage:
    scene ep9_diks_ph2_ssolo_event12 with dissolve
    mc "Already, huh? I thought it would take longer for you to bring me there."
    sa "Haha, shut up! You know what for."
else:
    mc "My room?"
    sa "Duh!"
jump ep9_diks_ph2_photo_sage_event_label

label ep9_diks_ph2_jamie_event_label:
scene ep9_dik2_jamie_event1 with dissolve
le "It's not cool that you did that to me. I even bought you an outfit."
scene ep9_dik2_jamie_event4 with dissolve
jm "You did?"
scene ep9_dik2_jamie_event1 with dissolve
le "Yeah, I put it in your room with a note and everything."
scene ep9_dik2_jamie_event4 with dissolve
jm "Dany wanted us to go as magician and assistant, so she could find a reason to bring Franz to the party."
jm "He's been pooping weirdly lately and-"
scene ep9_dik2_jamie_event2 with dissolve
le "Because of Dany? Is that your defense?"
le "You're back with her now, and suddenly, I come in second place."
le "You don't even talk to me about your decisions anymore."
scene ep9_dik2_jamie_event5 with dissolve
jm "You're expecting me to talk to you about this?"
jm "I know where you stand. It's like I'm not allowed to make my own decisions if you don't agree with them!"
scene ep9_dik2_jamie_event2 with dissolve
le "That's so not what it is, dude! I'm looking out for you because I've seen how fucking miserable that bitch makes you."
le "Do you think it's fun for me to listen to my pal being sad and complain about her daily?"
le "Because that's been my reality since you two got together, barring your \"honeymoon\" period."
scene ep9_dik2_jamie_event5 with dissolve
jm "Oh, I'm so sorry I annoy you with my problems! Not everyone can be cool like you and only fuck girls without getting feelings for them!"
scene ep9_dik2_jamie_event3 with dissolve
le "You're throwing that in my face? You know I have a hard time committing!"
le "It's not my choice that I can't feel things for the girls I fuck. Believe me; I wish I could!"
scene ep9_dik2_jamie_event2 with dissolve
le "But then I look at you committing to a chick who doesn't even respect you and makes you ignore your friends and dress up like an idiot pulling shit out of your hat."
scene ep9_dik2_jamie_event6 with dissolve
jm "Gather around for the show! Here comes the truth!"
jm "Leon gets a little bit drunk and his true colors show."
jm "And I can pull something out of my hat just for you, my friend."
scene bg anim_jamie_trick_ep9 movie with dissolve
$ renpy.pause(3.0)
jm "Abracadabra, bitch!"
scene ep9_dik2_jamie_event7 with dissolve
$ renpy.pause()
scene ep9_dik2_jamie_event8 with dissolve
mc "Dude, what's going on? Why are you two yelling at each other?"
scene ep9_dik2_jamie_event9 with dissolve
jm "Leon's a dick! He's pissed at me for going back to Dany."
if ep8_leons_side:
    jm "And I don't wanna hear it from you too, [name]."
    jm "Leave me alone."
    scene ep9_dik2_jamie_event11 with dissolve
else:
    scene ep9_dik2_jamie_event10 with dissolve
    jm "He's not like you... He doesn't understand how it feels to see your ex-girlfriend all the time and how hard it is to move on."
    jm "And, yeah. All those nasty things I couldn't stand with Dany, they are still there, but I appreciate the other stuff a lot more these days."
    jm "So, it's kind of balanced."
    scene ep9_dik2_jamie_event11 with dissolve
menu:
    "Side with Jamie":
        $ ep9_leons_side = False
        if ep8_leons_side:
            mc "Calm down. I'm not gonna fight with you."
        else:
            mc "If you want to be with her despite all of that, go for it."
        mc "You're free to make your own choices, bro. We're just looking out for you."
        scene ep9_dik2_jamie_event10 with dissolve
        jm "You might be doing that, but Leon... I don't know..."
        scene ep9_dik2_jamie_event11 with dissolve
        if ep8_leons_side:
            mc "But I know because he told me."
            scene ep9_dik2_jamie_event10 with dissolve
            jm "What did he tell you?"
            scene ep9_dik2_jamie_event11 with dissolve
            mc "He said he doesn't want to see you get hurt, and I believe him."
            mc "Maybe he's going about it wrong, but I think he's got your best interest at heart."
            mc "And he's obviously bummed out that you didn't wear the theme costume he got for you."
            jm "..."
            scene ep9_dik2_jamie_event10 with dissolve
            jm "Fuck... Thanks, [name]."
            jm "*{i}Sigh{/i}* I'm going back to Dany..."
        else:
            mc "Follow your heart, Jamie."
            scene ep9_dik2_jamie_event10 with dissolve
            jm "Thanks, [name]."
            jm "*{i}Sigh{/i}* I'm going back to Dany..."
        $ new_bio("Jamie", "When Jamie and Leon argued, I took Jamie's side.")
        $ new_bio("Leon", "When Jamie and Leon argued, I took Jamie's side.")
    "Side with Leon":
        $ ep9_leons_side = True
        if ep8_leons_side:
            mc "I'm not gonna tell you I told you so, but Leon's right about this."
            scene ep9_dik2_jamie_event9 with dissolve
            jm "I told you I didn't want to hear it. I'm going back to Dany, and you two will have to find a way to accept that."
        else:
            mc "You know I want you to make your own choices, bro. But I have to stick up for Leon this time."
            scene ep9_dik2_jamie_event9 with dissolve
            jm "Sure! Stick up for him and how he doesn't want me to be happy."
            scene ep9_dik2_jamie_event11 with dissolve
            mc "I don't think it's that at all. He's doing what he thinks is best for his buddy."
            mc "But also, he's obviously hurt that you bailed on him with the costume."
            mc "Isn't theme costumes your thing?"
            scene ep9_dik2_jamie_event10 with dissolve
            jm "I mean, we did it last year, but..."
            jm "He's only mad about me going back to Dany."
            scene ep9_dik2_jamie_event11 with dissolve
            mc "I'm telling you, that's not it. I think you hurt him. Don't neglect your friends because of Dany."
            mc "But do what you want with it."
            jm "..."
            scene ep9_dik2_jamie_event10 with dissolve
            jm "*{i}Sigh{/i}* I'm going back to Dany..."
        $ new_bio("Jamie", "When Jamie and Leon argued, I took Leon's side.")
        $ new_bio("Leon", "When Jamie and Leon argued, I took Leon's side.")

$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_zoey_event_label:
$ event_list.append("ep9_diks_ph2_riona_event_label")
scene ep9_diks_ph2_zoey_event1 with dissolve
zo "You've got some real fucking talent. I'm so impressed."
scene ep9_diks_ph2_zoey_event2 with dissolve
jac "Thanks! I've been practicing since like forever."
jac "And the art classes they have here are the bomb. They teach you things you never thought of before."
jac "It makes you look at art in a completely different way."
scene ep9_diks_ph2_zoey_event3 with dissolve
zo "It sounds dope. You'll have to tell me more about it sometime..."
zo "I wanna have a word with Mr. Party Planner here."
scene ep9_diks_ph2_zoey_event4 with dissolve
zo "He keeps running around and away from me."
scene ep9_diks_ph2_zoey_event5 with dissolve
mc "I'm not. I'm here now."
scene ep9_diks_ph2_zoey_event6 with dissolve
jac "[name]... Dude... What a fucking great chick."
scene ep9_diks_ph2_zoey_event7 with dissolve
zo "Wanna drink with me, or are you too busy fighting off the Persian army?"
scene ep9_diks_ph2_zoey_event8 with dissolve
mc "No, I've defeated them already. Let's get a victory drink. Kitchen?"
scene ep9_diks_ph2_zoey_event9 with dissolve
zo "Actually... Can we grab some air?"
stop music fadeout 3
scene ep9_diks_ph2_zoey_event8 with dissolve
mc "I know the spot for it."

scene ep9_diks_ph2_zoey_event10 with wipeleft
play music "music/ep8/licensed_music/track82.mp3"
$ renpy.pause()
scene ep9_diks_ph2_zoey_event11 with dissolve
tm "Now it's a party..."
scene ep9_diks_ph2_zoey_event12 with dissolve
ri "We smoking? Can I get a hit?"
scene ep9_diks_ph2_zoey_event13 with dissolve
tm "Didn't you bring your own shit?"
scene ep9_diks_ph2_zoey_event14 with dissolve
ri "No, I'm out right now, but I'll get more next week."
scene ep9_diks_ph2_zoey_event13 with dissolve
tm "All right, I'll help you out. I heard you were in a tight spot."
scene ep9_diks_ph2_zoey_event15 with dissolve
ri "Huh? What do you mean?"
scene ep9_diks_ph2_zoey_event16 with dissolve
tm "Nothing."
scene ep9_diks_ph2_zoey_event15 with dissolve
ri "Seriously... What did you mean by that?"
scene ep9_diks_ph2_zoey_event16 with dissolve
tm "*{i}Whispers{/i}* Quinn told me you've been smoking for free, so I figured you were tight on cash."
scene ep9_diks_ph2_zoey_event15 with dissolve
ri "What? I pay for myself."
scene ep9_diks_ph2_zoey_event16 with dissolve
tm "Whatever you say."
scene ep9_diks_ph2_zoey_event17 with dissolve
tm "You don't want it?"
ri "Keep it."
scene ep9_diks_ph2_zoey_event18 with dissolve
tm "Fine by me."
scene ep9_diks_ph2_zoey_event19 with dissolve
mc "Looks like we had the same idea as others."
scene ep9_diks_ph2_zoey_event20 with dissolve
tm "I'm tripping balls over here. It's Halloween, right?"
zo "That dude is stoned."
if ep4_smoked_weed:
    scene ep9_diks_ph2_zoey_event21 with dissolve
    tm "[name]! Do you want another shot at it?"
    scene ep9_diks_ph2_zoey_event26 with dissolve
    zo "No fucking way! Do you smoke pot?"
    scene ep9_diks_ph2_zoey_event27 with dissolve
    mc "Well, I have tried it."
    scene ep9_diks_ph2_zoey_event28 with dissolve
    zo "You're full of surprises tonight."
    scene ep9_diks_ph2_zoey_event27 with dissolve
    mc "What do you mean?"
    scene ep9_diks_ph2_zoey_event22 with dissolve
    tm "What about you? Demon girl. Do you want a hit?"
else:
    scene ep9_diks_ph2_zoey_event22 with dissolve
    tm "I know broom-head won't hit this, but how about you?"
scene ep9_diks_ph2_zoey_event29 with dissolve
zo "Me? I'm just a figment of your imagination, dude."
zo "Don't do drugs! It will kill you! WAAAHH!!!"
scene ep9_diks_ph2_zoey_event23 with dissolve
tm "Whoa..."
scene ep9_diks_ph2_zoey_event30 with dissolve
mc "Let's sit over here."
scene ep9_diks_ph2_zoey_event31 with dissolve
mc "You can smoke if you want to."
scene ep9_diks_ph2_zoey_event32 with dissolve
zo "Nah, I quit smoking. Mom was right about it; it was just a phase."
zo "They smoke marijuana like crazy in California, but I didn't wanna fall back into bad habits."
scene ep9_diks_ph2_zoey_event33 with dissolve
mc "Bad habits? Who are you?"
scene ep9_diks_ph2_zoey_event34 with dissolve
zo "What?"
scene ep9_diks_ph2_zoey_event33 with dissolve
mc "You've been smoking since the day I first met you. I mean, not a lot, but continuously."
mc "And now you're over it?"
scene ep9_diks_ph2_zoey_event35 with dissolve
zo "Like I said, it was an addictive phase that I kicked. I wore spiked chokers and dyed my hair black back then too."
zo "And now I'm into blue, and I don't smoke. Also, not only do I still love beer, but also colorful girly drinks, thanks to my friend Jonah."
scene ep9_diks_ph2_zoey_event33 with dissolve
mc "If that's the case, you should visit Derek's closet bar if you want a drink like that tonight."
scene ep9_diks_ph2_zoey_event24 with dissolve
tm "[name]!"
scene ep9_diks_ph2_zoey_event25 with dissolve
mc "Yeah?"
scene ep9_diks_ph2_zoey_event24 with dissolve
if (minigames and pp_current_party_happiness[7] > 2) or (not minigames and pp_current_party_happiness[7] == 1):
    tm "You've thrown a hell of a party. I'm fucking amazed at how good it is! Bravo, [name]! Bravo!"
    scene ep9_diks_ph2_zoey_event25 with dissolve
    if affinity == "CHICK":
        mc "Thanks, Tommy. I couldn't have done it without you."
        scene ep9_diks_ph2_zoey_event24 with dissolve
        tm "I know you couldn't. I was throwing you a bone. Hear that, girls? He admitted it."
    else:
        mc "You're high as fuck, Tommy. Tell me that tomorrow."
        scene ep9_diks_ph2_zoey_event24 with dissolve
        tm "See, girls? He can't take a fucking compliment. I try, but what do I get for it?"
else:
    tm "This party is fucking shit; you know that, right?"
    scene ep9_diks_ph2_zoey_event25 with dissolve
    if affinity == "CHICK":
        mc "Speak for yourself. Most seem to enjoy it."
        scene ep9_diks_ph2_zoey_event24 with dissolve
        tm "You girls agree with me, right? Horrible party. Really horrible."
    else:
        mc "You helped me plan it. It's not all my fault."
        scene ep9_diks_ph2_zoey_event24 with dissolve
        tm "See, girls? That dude can't take any responsibility for his mistakes. It's pretty sad."

    if zoey_dik:
        scene ep9_diks_ph2_zoey_event36 with dissolve
        zo "Hey, vamp douche! Go shove some garlic up your asshole. This party rocks!"

scene ep9_diks_ph2_zoey_event37 with dissolve
zo "Who the hell is that guy?"
scene ep9_diks_ph2_zoey_event38 with dissolve
mc "That's Tommy. The vice president of the DIKs."
mc "I'm still getting used to him."
if (minigames and pp_current_party_happiness[7] > 2) or (not minigames and pp_current_party_happiness[7] == 1):
    mc "At least he complimented me."
scene ep9_diks_ph2_zoey_event35 with dissolve
if zoey_dik:
    if (minigames and pp_current_party_happiness[7] > 2) or (not minigames and pp_current_party_happiness[7] == 1):
        zo "He's using you to get into those chicks' underwear."
    else:
        zo "You know, he dissed you to look good in front of those chicks. That's an asshole in my book."
else:
    zo "He seems like a douche."
scene ep9_diks_ph2_zoey_event38 with dissolve
mc "It takes a while to see it, but he's got both good and bad sides. But yeah, he can be a real dick at times."
scene ep9_diks_ph2_zoey_event39 with dissolve
zo "That's the frat name, after all."
scene ep9_diks_ph2_zoey_event40 with dissolve
mc "True, but the DIKs are good guys once you get to know them."
scene ep9_diks_ph2_zoey_event39 with dissolve
zo "I've been chatting with a few of them tonight. They're pretty cool."
zo "But I was a bit surprised they didn't know who I was when I told them about you."
scene ep9_diks_ph2_zoey_event40 with dissolve
mc "We're bonding, but we haven't quite reached the point where we talk about every detail of our lives yet."
mc "It's mostly on-the-surface stuff; there's not a lot of talk about feelings."
scene ep9_diks_ph2_zoey_event41 with dissolve
zo "You must hate it here, then."
scene ep9_diks_ph2_zoey_event40 with dissolve
mc "I would have, but thankfully, I have many years of practice not talking about feelings with someone."
scene ep9_diks_ph2_zoey_event35 with dissolve
zo "You got me right back."
scene ep9_diks_ph2_zoey_event42 with dissolve
mc "But yeah, I haven't told them about you."
mc "Hell, I don't know anything about any of their exes either, so, it's how it is."
scene ep9_diks_ph2_zoey_event43 with dissolve
zo "..."
scene ep9_diks_ph2_zoey_event44 with dissolve
if (minigames and pp_current_party_happiness[7] > 2) or (not minigames and pp_current_party_happiness[7] == 1):
    zo "So... Uh... Tommy is right about the party. I'm having a blast."
else:
    zo "So... Uh... You know, Tommy is dead wrong about the party. I'm having a blast."
scene ep9_diks_ph2_zoey_event45 with dissolve
mc "That's good. Does it feel weird being here by yourself?"
scene ep9_diks_ph2_zoey_event46 with dissolve
zo "Not at all. I've gotten pretty used to it in San Diego."
zo "At the hostel, for one, people came and left all the time. Any friends you made had to be short-term."
scene ep9_diks_ph2_zoey_event47 with dissolve
zo "I got pretty good at striking up conversations with randoms."
zo "And your friends are great, so it's easy as hell with them. It's harder to get away from them than it is to talk to them."
scene ep9_diks_ph2_zoey_event48 with dissolve
mc "That's good to hear. I've still got things to do tonight and people to talk to, so..."
scene ep9_diks_ph2_zoey_event47 with dissolve
zo "I get it."
scene ep9_diks_ph2_zoey_event49 with dissolve
zo "Hey, I heard them talking about a photoshoot or something. What's that about?"
scene ep9_diks_ph2_zoey_event51 with dissolve
mc "Oh! It's the one in my room. Guests can have their pictures taken, with their costumes and everything."
mc "You can take your picture there if you want."
scene ep9_diks_ph2_zoey_event49 with dissolve
zo "My notebook is fucking begging for one! Do you want to take one with me?"
scene ep9_diks_ph2_zoey_event51 with dissolve
menu:
    "[mod_gr]Take a picture with Zoey":
        mc "If you want to."
        scene ep9_diks_ph2_zoey_event49 with dissolve
        zo "Let's do it! You can be the Spartan legend who slayed a demon."
        scene ep9_diks_ph2_zoey_event51 with dissolve
        mc "Haha! That sounds like a good picture!"
        scene ep9_diks_ph2_zoey_event49 with dissolve
        zo "Fuckin' legendary!"
    "No time for it":
        $ currentFreeRoamLabel = "ep9_diks_ph2_ua_label"
        mc "Sorry, but I have things to do."
        mc "You're free to take one by yourself, though."
        scene ep9_diks_ph2_zoey_event50 with dissolve
        zo "Ok... I'll do that!"
        stop music fadeout 3
        scene ep9_diks_ph2_zoey_event52 with dissolve
        mc "I'll have to get back to the party."
        scene ep9_diks_ph2_zoey_event53 with dissolve
        $ renpy.pause()
        if persistent.mod_wtenabled:
            $ task_list[6] = "Talk to Riona (Your room)"
        else:
            $ task_list[6] = "Talk to Riona"
       
        $ task_list[4] = ""
        $ updateTaskList()
        $ mphone_next_song()
        $ new_bio("Zoey", "Zoey seems to have changed a lot during this last year.")
        jump endEvent

$ ep9_photos[14] = True
scene ep9_diks_ph2_zoey_event54 with wipeleft
zo "Dude! Is THIS your room? It's huge!"
zo "Who did you bang to get this one?"
scene ep9_diks_ph2_zoey_event55 with dissolve
mc "It used to be an old, trashed library that no one used. They didn't put up a fight when I said I could take it."
mc "It took a lot of hard work to restore it, and I'm pretty sure they're jealous of it now."
scene ep9_diks_ph2_zoey_event56 with dissolve
zo "Who wouldn't be? It's even bigger than my studio apartment was."
scene ep9_diks_ph2_zoey_event57 with dissolve
zo "And wow... Your guitar..."
mc "Yeah, it's here."
scene ep9_diks_ph2_zoey_event58 with dissolve
zo "Of course it is. You wouldn't go anywhere without it."
scene ep9_diks_ph2_zoey_event59 with dissolve
mc "Ok, so for the picture. You just stand there."
scene ep9_diks_ph2_zoey_event60 with dissolve
zo "What about you?"
scene ep9_diks_ph2_zoey_event61 with dissolve
mc "Let me take a couple of pictures of you first; then I'll join you."
scene ep9_diks_ph2_zoey_event62 with dissolve
zo "I'm getting a creepy déjà vu about this."
scene ep9_diks_ph2_zoey_event63 with dissolve
mc "Why is that?"
scene ep9_diks_ph2_zoey_event62 with dissolve
zo "Eh... It's nothing. I'll make a scary pose for you!"
scene ep9_diks_ph2_zoey_event64 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_zoey_event64 with dissolve
mc "Nice! These will come out great."
scene ep9_diks_ph2_zoey_event66 with dissolve
zo "Group pic or whatever it's called! Get over here with me. Come slay the demon!"
scene ep9_diks_ph2_zoey_event67 with dissolve
mc "Like this?"
zo "Haha! Yeah!"
scene ep9_diks_ph2_zoey_event68 with dissolve
zo "I'll eat your soul! BLARGH!"
scene ep9_diks_ph2_zoey_event69 with dissolve
mc "Haha! Very convincing!"
scene ep9_diks_ph2_zoey_event68 with dissolve
zo "You're laughing at my demon face!? Come on, warrior! Slay me! BLARGH!"
scene ep9_diks_ph2_zoey_event70 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_zoey_event71 with dissolve
zo "What's wrong?"
scene ep9_diks_ph2_zoey_event69 with dissolve
mc "Show me that demon face again!"
scene ep9_diks_ph2_zoey_event68 with dissolve
zo "BLARGH!"
scene ep9_diks_ph2_zoey_event65 with dissolve
mc "ARGH!!!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_zoey_event65 with dissolve
$ renpy.pause(0.5)
scene ep9_diks_ph2_zoey_event72 with dissolve
zo "Nailed it!"
mc "We better have."
scene ep9_diks_ph2_zoey_event73 with dissolve
mc "Yeah, look!"
zo "Haha! That looks so good!"
zo "Are you gonna edit it?"
mc "I think Jacob's gonna do it. He knows that stuff."
scene ep9_diks_ph2_zoey_event74 with dissolve
zo "You have to send me that one!"
scene ep9_diks_ph2_zoey_event75 with dissolve
mc "You got it."
scene ep9_diks_ph2_zoey_event76 with dissolve
mc "Wanna...get back out there?"
scene ep9_diks_ph2_zoey_event77 with dissolve
zo "Actually, this demon's gonna slither away to find the restroom."
zo "Rad photoshoot!"
stop music fadeout 3
scene ep9_diks_ph2_zoey_event78 with dissolve
mc "Totally."
if persistent.mod_wtenabled:
            $ task_list[6] = "Talk to Riona (Your room)"
else:
            $ task_list[6] = "Talk to Riona"
$ task_list[4] = ""
$ updateTaskList()
$ mphone_next_song()
$ new_bio("Zoey", "Zoey seems to have changed a lot during this last year.")
$ new_bio("Zoey", "Zoey and I took a Halloween picture together.")
jump endEvent

label ep9_diks_ph2_scary_intro_event_label:
$ guideSuggestedPage = 68
if "ep9_diks_ph2_riona_event2_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_riona_event2_label")
scene ep9_diks_ph2_scary_event1 with dissolve
jac "Bro, scary stories time. Basement."
scene ep9_diks_ph2_scary_event2 with dissolve
mc "You got it under control?"
scene ep9_diks_ph2_scary_event3 with dissolve
jac "Yeah, I asked Derek to bring people. Are you coming?"
if branchAlone or branchMayaJosy:
    scene ep9_diks_ph2_scary_event2 with dissolve
    stop music fadeout 3
    mc "Yeah, let's go."
    jump ep9_diks_ph2_scary_event_label
if branchIsabella:
    scene ep9_diks_ph2_scary_event2 with dissolve
    stop music fadeout 3
    mc "Gimme a sec; I need to get someone too."
    scene ep9_diks_ph2_scary_event5 with wipeleft
    isa "Do you get scared easily?"
    mc "From horror movies, yeah. I don't think I'll get scared by this."
elif branchJill:
    scene ep9_diks_ph2_scary_event2 with dissolve
    stop music fadeout 3
    mc "Gimme a sec, I need to get someone too."
    scene ep9_diks_ph2_scary_event6 with wipeleft
    ji "Wow, you made the basement look scary too? This is going to be so fun!"
    mc "This is all Jacob's work."
elif branchSage:
    scene ep9_diks_ph2_scary_event4 with dissolve
    stop music fadeout 3
    sa "[name]! Storytime, let's go!"

label ep9_diks_ph2_scary_event_label:
play music "music/ep9/licensed_music/track116.mp3"
if branchSage:
    scene ep9_diks_ph2_scary_event7b with dissolve
elif branchJill:
    scene ep9_diks_ph2_scary_event7c with dissolve
elif branchIsabella:
    scene ep9_diks_ph2_scary_event7d with dissolve
else:
    scene ep9_diks_ph2_scary_event7 with dissolve

my "And still to this day, every time he goes to the basement to the spot where his wife hung herself, he feels a breeze and hears the sound of her clock."
scene ep9_diks_ph2_scary_event8 with dissolve
my "Tick-tock. Tick-tock."
scene ep9_diks_ph2_scary_event9 with dissolve
js "I'm so gonna have nightmares tonight. I should get super-drunk."
scene ep9_diks_ph2_scary_event18 with dissolve
jac "Cheers to that!"
scene ep9_diks_ph2_scary_event16 with dissolve
ri "That was a creepy story. Was it true?"
scene ep9_diks_ph2_scary_event10 with dissolve
my "Haha, no. It's something I made up."
scene ep9_diks_ph2_scary_event17 with dissolve
jac "You made that up? Damn. That's some vivid imagination."
scene ep9_diks_ph2_scary_event10 with dissolve
my "Thanks, well, I watch a lot of movies."

if branchSage:
    scene ep9_diks_ph2_scary_event36 with dissolve
    sa "Look! Boooooh!"
    scene ep9_diks_ph2_scary_event38 with dissolve
    mc "Is that your scary ghost sound?"
    scene ep9_diks_ph2_scary_event37 with dissolve
    sa "Scaaaaaary, huh?"
    scene ep9_diks_ph2_scary_event38 with dissolve
    mc "Yeah, I'm shaking."
    scene ep9_diks_ph2_scary_event39 with dissolve
    sa "Haha! Shut up!"
elif branchJill:
    scene ep9_diks_ph2_scary_event42 with dissolve
    mc "*{i}Muffled laugh{/i}*"
    scene ep9_diks_ph2_scary_event43 with dissolve
    ji "What?"
    scene ep9_diks_ph2_scary_event44 with dissolve
    mc "It's so funny looking your way. We're sitting here and it's supposed to be scary..."
    mc "And in the corner of my eye, I see a silly banana-Jill."
    scene ep9_diks_ph2_scary_event43 with dissolve
    ji "Haha! I guess I'm ruining the ambiance."
    scene ep9_diks_ph2_scary_event45 with dissolve
    mc "No, you're not. Well, maybe, but it doesn't matter. I wouldn't have it any other way."
elif branchIsabella:
    scene ep9_diks_ph2_scary_event48 with dissolve
    mc "You look scary in the dark."
    scene ep9_diks_ph2_scary_event49 with dissolve
    isa "Thank you. I feel more comfortable than I did at the start of the party. Mostly thanks to the dim lighting."
elif branchMayaJosy:
    scene ep9_diks_ph2_scary_event11 with dissolve
    my "How are you doing over there, [name]? Did I scare you?"
    scene ep9_diks_ph2_scary_event12 with dissolve
    mc "It was a good story, but I wasn't too scared."
    scene ep9_diks_ph2_scary_event11 with dissolve
    my "I guess you're doing better than when we watched that scary movie together."
    scene ep9_diks_ph2_scary_event13 with dissolve
    mc "(It feels weird that she's talking about that openly in a group...)"
    mc "(I don't know why that is. If it's the alcohol or something else, but she seems more comfortable.)"
    scene ep9_diks_ph2_scary_event14 with dissolve
    mc "(It makes me a bit uncomfortable. It's almost like she's flirting.)"
    mc "(All this time, trying to hide what's between us three from everyone, I guess it leaves those kinds of marks.)"

scene ep9_diks_ph2_scary_event28 with dissolve
cam "I have a true story if you want to hear one."
scene ep9_diks_ph2_scary_event19 with dissolve
jac "Hell yeah, lay it on us."
scene ep9_diks_ph2_scary_event29 with dissolve
cam "Have you ever heard of sleep paralysis?"
cam "It's when you're asleep and your brain wakes up, but your body doesn't."
cam "You cannot move your body voluntarily when it happens, but your mind is present."
scene ep9_diks_ph2_scary_event30 with dissolve
cam "Most people panic when they get it, but there's nothing you can do."
cam "You can't call out for help or do anything aside from trying to fall back to sleep or wait until your body wakes up."
scene ep9_diks_ph2_scary_event31 with dissolve
cam "Some say that if you focus on jiggling your fingertips or toes, eventually, your body wakes up, but that never worked for my mother."
scene ep9_diks_ph2_scary_event30 with dissolve
cam "My mother suffered from sleep paralysis. It happened many times and she told me how it made her see things in her dreams."
cam "Things that felt very real."
scene ep9_diks_ph2_scary_event53 with dissolve
cam "{i}She ate pills to fall asleep, hoping it would help her, but it didn't.{/i}"
scene ep9_diks_ph2_scary_event54 with dissolve
cam "{i}She never got used to the sleep paralysis; she got scared of it.{/i}"
scene anim_eyes_scared_ep9 with dissolve
cam "{i}She would wake up sweating as it happened. She wanted to scream but panicked because she couldn't.{/i}"
cam "{i}Her eyes quickly started wandering around the room.{/i}"
cam "{i}The ceiling.{/i}"
cam "{i}The bed.{/i}"
cam "{i}The walls.{/i}"
scene ep9_diks_ph2_scary_event55 with dissolve
cam "{i}But she didn't dare look at the door to her room because it was in the corner where {b}she{/b} always stood.{/i}"
my "Who was by the door?"
scene ep9_diks_ph2_scary_event56 with dissolve
cam "{i}My grandmother.{/i}"
cam "{i}Mom could feel her presence in the room.{/i}"
scene anim_eyes_scared_ep9 with dissolve
cam "{i}She started believing that the sleep paralysis was her mother's way of contacting her.{/i}"
cam "{i}It should have felt ridiculous since her mother had been dead for 13 years, and they didn't end it on good terms before she went.{/i}"
scene ep9_diks_ph2_scary_event57 with dissolve
cam "{i}Carefully, she brought her gaze toward the door.{/i}"
scene ep9_diks_ph2_scary_event58 with dissolve
cam "{i}And at the edge of her vision, she could just make out the dark silhouette standing in the corner.{/i}"
cam "{i}She whimpered, but still, not a word was uttered from her lips.{/i}"
scene ep9_diks_ph2_scary_event59 with dissolve
cam "{i}Grandma was just standing there.{/i}"
cam "{i}Looking at her.{/i}"
scene ep9_diks_ph2_scary_event60 with dissolve
cam "{i}That's all she ever did. Every time, she just stood there watching her daughter sleep.{/i}"
cam "{i}But not this night.{/i}"
scene ep9_diks_ph2_scary_event61 with dissolve
cam "{i}She moved.{/i}"
cam "{i}She took one step closer to Mom.{/i}"
scene anim_eyes_scared_ep9 with dissolve
cam "{i}Mom panicked and didn't know what to do.{/i}"
cam "{i}For a second, she averted her eyes, but as they returned to look at her mother...{/i}"
scene ep9_diks_ph2_scary_event62 with dissolve
cam "{i}...she had moved one step closer to the bed. And her eyes were opened wide, staring at her.{/i}"
scene ep9_diks_ph2_scary_event63 with dissolve
cam "{i}Another step. She was getting closer.{/i}"
scene anim_eyes_scared2_ep9 with dissolve
stop music fadeout 5
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
cam "{i}Mom managed to close her eyes. The first voluntary body control she had since the paralysis started that night.{/i}"
cam "{i}She must have closed her eyes for at least a minute before opening them again.{/i}"
scene ep9_diks_ph2_scary_event64 with dissolve
cam "{i}And as she looked...{/i}"
scene ep9_diks_ph2_scary_event65 with dissolve
cam "{i}The room was empty. Her mother was gone.{/i}"
scene ep9_diks_ph2_scary_event66 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=5)
cam "{i}Mom's panic subsided. Still sweating, but her breathing had finally slowed down.{/i}"
scene ep9_diks_ph2_scary_event67 with dissolve
cam "{i}Finally, some body control returned. Her limbs were about to wake up.{/i}"
cam "{i}She watched as her hand moved up to her face.{/i}"
scene ep9_diks_ph2_scary_event68 with dissolve
cam "{i}But, she thought, what's this? It's not me moving my limb, and that's not my arm.{/i}"
scene bg anim_eyes_scared3_ep9 movie with vpunch
cam "{i}Her mother lay beside her, grabbing her as she screamed!{/i}"
"AHHH!!!"
scene ep9_diks_ph2_scary_event32 with dissolve
"*{i}Laughter{/i}*"
cam "Haha! I got all of you! Didn't I?"
scene ep9_diks_ph2_scary_event35 with dissolve
play music "music/ep9/licensed_music/track116.mp3"
my "That was such a great story!"
js "Oh my God! That was so scary!"
scene ep9_diks_ph2_scary_event20 with dissolve
de "Getting a hug from your mom is scary?"
scene ep9_diks_ph2_scary_event33 with dissolve
cam "Come on; it was scary! It happened that way!"
if branchSage:
    scene ep9_diks_ph2_scary_event41 with dissolve
    sa "Yeah, dude. That was fucking scary! You're wrong on this one."
scene ep9_diks_ph2_scary_event20 with dissolve
de "It was an interesting story, but not scary."
scene ep9_diks_ph2_scary_event33 with dissolve
cam "How about you tell one then?"

scene ep9_diks_ph2_scary_event21 with dissolve
de "Ok. Prepare yourselves for this one. It will chill you to the bones."
scene ep9_diks_ph2_scary_event69 with dissolve
de "{i}Once upon a time, I was at a party.{/i}"
de "{i}It was very late and I was very drunk. Oh, so drunk.{/i}"
scene ep9_diks_ph2_scary_event70 with dissolve
de "{i}I must have drunk enough beers to sedate a horse, but I was still going.{/i}"
de "{i}I was laughing and having a good time when someone came to me and said...{/i}"
de "{i}Hey, Derek. I heard there's a hot chick outdoors who's calling your name.{/i}"
scene ep9_diks_ph2_scary_event71 with dissolve
stop music fadeout 3
de "{i}And I was like, \"Say no more\", as I straightened my bowtie and went outdoors to greet her.{/i}"
scene ep9_diks_ph2_scary_event72 with dissolve
play music "music/ep9/licensed_music/track120.mp3"
de "{i}As I got outside, I couldn't see her, but I could hear someone singing in the calmness of the night.{/i}"
scene ep9_diks_ph2_scary_event73 with dissolve
de "{i}A serene female voice. It soothed my soul.{/i}"
scene ep9_diks_ph2_scary_event74 with dissolve
de "{i}It was the most beautiful song I'd ever heard. It was like a siren beckoning me.{/i}"
scene ep9_diks_ph2_scary_event75 with dissolve
de "{i}I walked toward the song, and there she was in the bushes...{/i}"
de "{i}A naked and beautiful woman with breasts as big as-{/i}"
$ renpy.sound.set_volume(0,channel='music')
scene ep9_diks_ph2_scary_event22
my "Derek!"
scene ep9_diks_ph2_scary_event23 with dissolve
de "Just wait for it! Don't interrupt my story."
scene ep9_diks_ph2_scary_event24 with dissolve
de "She was a naked and beautiful woman. With breasts as big as... You all know Isabella, the librarian?"
de "They were big like hers."
if branchIsabella:
    scene ep9_diks_ph2_scary_event51 with dissolve
    mc "*{i}Whispers{/i}* Don't mind him; he's an idiot."
elif branchJill:
    scene ep9_diks_ph2_scary_event46 with dissolve
    ji "This is pretty disrespectful."
scene ep9_diks_ph2_scary_event76 with dissolve
$ renpy.sound.set_volume(1.0,channel='music')
de "{i}As I reached out to touch the woman, she grabbed me. She embraced me.{/i}"
scene ep9_diks_ph2_scary_event77 with dissolve
de "{i}She pulled down my pants and reached for my genitals.{/i}"
scene ep9_diks_ph2_scary_event15 with dissolve
js "Can we leave?"
scene ep9_diks_ph2_scary_event78 with dissolve
stop music fadeout 3
de "{i}And as she fondled my balls, she transformed!{/i}"
scene ep9_diks_ph2_scary_event79 with dissolve
play music "<from 58.3>music/ep9/licensed_music/track116.mp3"
de "{i}This was no longer a beautiful girl! It was a fat, waddling monstrosity!{/i}"
scene ep9_diks_ph2_scary_event80 with dissolve
de "{i}Lumps of fat formed around each crevice of her body. It was like I was stuck in human-shaped dough and the harder I pushed, the more inside of her I got.{/i}"
de "{i}This quicksand-like morbidly obese entity had a gravitational pull!{/i}"
scene ep9_diks_ph2_scary_event81 with dissolve
play sound "sound_effects/season3/whalenoise.mp3"
de "{i}I couldn't get loose from her grasp! And her song was replaced with whale-like moans, shaking the very foundation around us!{/i}"
de "{i}I WANT YOUR SEED! She screamed as she humped me.{/i}"
scene ep9_diks_ph2_scary_event34 with dissolve
cam "I'm done."
ri "Wait for me."
scene ep9_diks_ph2_scary_event25 with dissolve
de "I know you look disgusted and the story will do that as it is based on true events."
scene ep9_diks_ph2_scary_event26 with dissolve
stop music fadeout 3
jac "It was Wendy, wasn't it?"
scene ep9_diks_ph2_scary_event27 with dissolve
de "No comment."
if branchSage:
    scene ep9_diks_ph2_scary_event40 with dissolve
    sa "Scary, but for all the wrong reasons."
elif branchIsabella:
    scene ep9_diks_ph2_scary_event50 with dissolve
    isa "..."
    mc "I know. Wanna get out of here?"
elif branchJill:
    scene ep9_diks_ph2_scary_event46 with dissolve
    ji "Remind me; is this your best friend?"
    scene ep9_diks_ph2_scary_event47 with dissolve
    mc "Well...one of them. He's going through some stuff."
    mc "Dancing?"
    scene ep9_diks_ph2_scary_event46 with dissolve
    ji "Sure..."
else:
    scene ep9_diks_ph2_scary_event52 with dissolve
    mc "So, uh... It looks like story time is over..."
    mc "Dancing? Anyone?"
if minigames:
    scene ep9_diks_ph2_scary_event_eval with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
    $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
    $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)

    $ pp_update_happiness_icons()
    $ mphone_pp_history_list.append("• The {color=ffed00}Scary Stories{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Scary Stories{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Scary Stories{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
    show screen specialmsg
    pause
    hide screen specialmsg
$ mphone_next_song()
$ currentFreeRoamLabel = "ep9_diks_ph2_main_label"
$ task_list[14] = ""
$ updateTaskList()
jump ep9_diks_ph2_preps_event_label

label ep9_diks_ph2_haunted_event_label:
$ guideSuggestedPage = 68
stop music fadeout 3
hide screen new_phone_screen
if wt_ep9_branch_numbers > 1:
    "Do the Haunted Mansion with?"
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sage scene)","(+2 Maya)","(-DIK)","(+DIK)","(+Maya/Josy)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
    
    menu:
        "Isabella" if branchIsabella:
            $wt_hh_girl_pick="Isabella"
        "Jill" if branchJill:
           $wt_hh_girl_pick="Jill"
        "Sage [mod_gr][mod_choices[0]]" if branchSage:
           $wt_hh_girl_pick="Sage"
        "Maya & Josy" if branchMayaJosy:
           $wt_hh_girl_pick="Maya"
        "Camila and Riona" if branchAlone:
           $wt_hh_girl_pick="Camila"
else:
   if branchIsabella:
    $wt_hh_girl_pick="Isabella"
   if branchJill:
    $wt_hh_girl_pick="Jill"
   if branchMayaJosy:
    $wt_hh_girl_pick="Maya"
   if branchSage:
    $wt_hh_girl_pick="Sage"
   if branchAlone:
    $wt_hh_girl_pick="Camila"
if branchIsabella and wt_hh_girl_pick=="Isabella":
    scene ep9_diks_ph2_haunted_event1 with dissolve
    mc "Be- Um... Mummy!"
    isa "Close one."
    scene ep9_diks_ph2_haunted_event2 with dissolve
    mc "Slip of the tongue."
    mc "Come with me; I have something fun for us to do."
    scene ep9_diks_ph2_haunted_event3 with dissolve
    isa "What is it?"
    scene ep9_diks_ph2_haunted_event2 with dissolve
    mc "I'll tell you on the way. Come!"
    scene ep9_diks_ph2_haunted_event16 with dissolve
    play music "music/ep9/licensed_music/track116.mp3"
    isa "So, what exactly is a haunted basement?"
    mc "I don't exactly know; it was Jacob who prepared it. All I know is that it's something you can do as a small group in the basement."
    mc "It's supposed to be fun and scary."
    scene ep9_diks_ph2_haunted_event17 with dissolve
    mc "We're here. Wanna read the note?"
    isa "If you find the door unlocked, enter the haunted basement and lock the door behind you."
    isa "Warning! Not for the faint of heart. Once you enter, there's no turning back."
    scene ep9_diks_ph2_haunted_event18 with dissolve
    mc "Wanna head inside?"
    scene ep9_diks_ph2_haunted_event19 with dissolve
    isa "Yes, I look forward to locking myself in the basement with you."
    if ep9_body_shots and affinity == "DIK":
        mc "Sarcasm?"
    scene ep9_diks_ph2_haunted_event36 with dissolve
    mc "Ok, the door is locked. It's dark in here!"
    isa "Use that flashlight."
    scene ep9_diks_ph2_haunted_event37 with dissolve
    mc "Good idea. There's a note here as well."
elif branchSage and wt_hh_girl_pick=="Sage":
    scene ep9_diks_ph2_haunted_event4 with dissolve
    sa "There you are! Why are you moving around so much?"
    scene ep9_diks_ph2_haunted_event5 with dissolve
    mc "I'm checking up on people, making sure everything's fine."
    scene ep9_diks_ph2_haunted_event6 with dissolve
    sa "Aw, that's sweet."
    sa "I heard some talking about the haunted basement. Wanna check it out with me?"
    scene ep9_diks_ph2_haunted_event5 with dissolve
    mc "Oh, yeah! That's Jacob's handiwork; I wanna see what he did with it."
    scene ep9_diks_ph2_haunted_event6 with dissolve
    sa "Let's go!"
    play music "music/ep9/licensed_music/track116.mp3"
    scene ep9_diks_ph2_haunted_event20 with dissolve
    mc "Are you having fun at the party?"
    sa "So fun, dude! It's not quite what I thought it would be, but it's very good."
    mc "Yeah, we had to make some changes to the plans."
    sa "That's fine. If you come up with better stuff, you should always go for it. I think you've done great!"
    scene ep9_diks_ph2_haunted_event21 with dissolve
    mc "I think we're supposed to read this note before entering."
    mc "If you find the door unlocked, enter the haunted basement and lock the door behind you."
    mc "Warning! Not for the faint of heart. Once you enter, there's no turning back."
    scene ep9_diks_ph2_haunted_event22 with dissolve
    sa "He sure set my expectations high with that warning. Enter already!"
    scene ep9_diks_ph2_haunted_event38 with dissolve
    sa "You locked the door. There's no turning back now, [name]."
    scene ep9_diks_ph2_haunted_event39 with dissolve
    sa "Oh! A flashlight!"
    scene ep9_diks_ph2_haunted_event40 with dissolve
    sa "*{i}Scary ghost noises{/i}* WOOOOH!!!! AAAAHH!!!"
    scene ep9_diks_ph2_haunted_event41 with dissolve
    mc "Very scary. It's dark in here; you'll have to point that flashlight for us."
    scene ep9_diks_ph2_haunted_event42 with dissolve
    sa "Look! What does this note say?"
elif branchJill  and wt_hh_girl_pick=="Jill":
    scene ep9_diks_ph2_haunted_event7 with dissolve
    mc "Jill! Wanna go do something fun with me?"
    scene ep9_diks_ph2_haunted_event8 with dissolve
    ji "Always. Where are we going?"
    scene ep9_diks_ph2_haunted_event9 with dissolve
    mc "Jacob prepared this haunted basement activity and I thought it would be fun if we did it together."
    scene ep9_diks_ph2_haunted_event8 with dissolve
    ji "Oh! That sounds scary! Lead the way!"
    scene ep9_diks_ph2_haunted_event23 with dissolve
    play music "music/ep9/licensed_music/track116.mp3"
    mc "Watch your steps."
    ji "Walking normally in this costume is so hard, but going to the bathroom is even harder!"
    mc "I bet it is."
    scene ep9_diks_ph2_haunted_event24 with dissolve
    mc "We're here."
    ji "What does that note say?"
    mc "If you find the door unlocked, enter the haunted basement and lock the door behind you."
    mc "Warning! Not for the faint of heart. Once you enter, there's no turning back."
    scene ep9_diks_ph2_haunted_event25 with dissolve
    ji "Ohh! Scary!"
    scene ep9_diks_ph2_haunted_event26 with dissolve
    mc "Bananas first?"
    scene ep9_diks_ph2_haunted_event25 with dissolve
    ji "Haha! You wish! I thought the Spartans were fearless."
    scene ep9_diks_ph2_haunted_event26 with dissolve
    mc "Ok, I'll lead the way."
    scene ep9_diks_ph2_haunted_event44 with dissolve
    mc "The door is locked and there's a flashlight here."
    ji "And another note! What does it say?"
    scene ep9_diks_ph2_haunted_event37 with dissolve
elif branchMayaJosy  and wt_hh_girl_pick=="Maya":
    scene ep9_diks_ph2_haunted_event10 with dissolve
    my "[name]!!! Jacob told us there was something scary going on in the basement!"
    scene ep9_diks_ph2_haunted_event11 with dissolve
    mc "Ah! Yeah, we have a haunted basement and they say people who enter don't return to the party. Wanna check it out?"
    scene ep9_diks_ph2_haunted_event12 with dissolve
    js "Is it for real or a joke?"
    scene ep9_diks_ph2_haunted_event13 with dissolve
    mc "Are you scared?"
    scene ep9_diks_ph2_haunted_event12 with dissolve
    js "I'm not scared. I'm cautious."
    scene ep9_diks_ph2_haunted_event13 with dissolve
    mc "Let's go find out."
    scene ep9_diks_ph2_haunted_event27 with dissolve
    play music "music/ep9/licensed_music/track116.mp3"
    my "This is so scary; you did a great job with this!"
    mc "This is Jacob's work. I don't know what he did with it exactly."
    scene ep9_diks_ph2_haunted_event29 with dissolve
    js "Look! There's a note on the door!"
    my "If you find the door unlocked, enter the haunted basement and lock the door behind you."
    my "Warning! Not for the faint of heart. Once you enter, there's no turning back."
    js "Guys, I'm not sure about this. The door might be locked, let's head back to the party."
    scene ep9_diks_ph2_haunted_event30 with dissolve
    my "No, come on! Let's go!"
    scene ep9_diks_ph2_haunted_event31 with dissolve
    js "Do I have to?"
    scene ep9_diks_ph2_haunted_event32 with dissolve
    mc "No, you don't have to, but Maya and I are going."
    scene ep9_diks_ph2_haunted_event31 with dissolve
    js "Dammit, peer pressure! Ok, I'm coming! But if someone tries to scare me, I will punch you!"
    scene ep9_diks_ph2_haunted_event43 with dissolve
    js "Wow, it's dark in here."
    my "Lock the door."
    mc "It is locked. And there's a flashlight and a note here."
    scene ep9_diks_ph2_haunted_event37 with dissolve
    mc "Let me see what it says."
elif branchAlone  and wt_hh_girl_pick=="Camila":
    scene ep9_diks_ph2_haunted_event14 with dissolve
    ri "[name]! Cammy and I are gonna check out the haunted basement. Wanna join?"
    scene ep9_diks_ph2_haunted_event15 with dissolve
    if "ep9_diks_ph2_riona_event2_label" in event_list:
        mc "Hey... Feeling better?"
        scene ep9_diks_ph2_haunted_event15b with dissolve
        ri "Yeah, sorry about that. So... Are you coming with us?"
        scene ep9_diks_ph2_haunted_event15 with dissolve
    mc "Sure, I wanna see what Jacob did with it. I heard he's pretty proud of it."
    scene ep9_diks_ph2_haunted_event28 with dissolve
    play music "music/ep9/licensed_music/track116.mp3"
    cam "Is it scary?"
    mc "I think it is."
    ri "I heard some say they almost shat their pants."
    scene ep9_diks_ph2_haunted_event33 with dissolve
    cam "If you find the door unlocked, enter the haunted basement and lock the door behind you."
    cam "Warning! Not for the faint of heart. Once you enter, there's no turning back."
    scene ep9_diks_ph2_haunted_event34 with dissolve
    ri "You two are going first. I'm not about to get jumped by anything."
    scene ep9_diks_ph2_haunted_event35 with dissolve
    cam "Haha, that's why we brought [name]. He's dressed like a warrior; he'll protect us."
    mc "Sure..."
    mc "(I hope I don't get scared myself...)"
    scene ep9_diks_ph2_haunted_event45 with dissolve
    mc "Ok, the door is locked and there's a flashlight here. We're definitely gonna need it."
    ri "There's another note. What does it say?"
    scene ep9_diks_ph2_haunted_event37 with dissolve

if "ep9_diks_ph2_riona_event2_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_riona_event2_label")
mc "You are trapped in a haunted basement. You must find your way out."
mc "The door you came from is locked by a mysterious force."
mc "Turning around you find another door with three locks on it. But where are the keys?"
mc "Can you escape the haunted basement before the vengeful spirit is summoned? \"Goo\" luck."
show screen freeroam_help

if branchAlone   and wt_hh_girl_pick=="Camila":
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event46
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    if not persistent.fx_tip:
        $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        pause
        hide screen specialmsg
        $ persistent.fx_tip = True

    ri "That's ridiculous; it was clearly [name] who locked the door."
    scene ep9_diks_ph2_haunted_event47
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    cam "Haha! [name] is the mysterious force! We solved it!"
    ri "Haha!"
    scene ep9_diks_ph2_haunted_event48
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Are we supposed to find the keys?"
    scene ep9_diks_ph2_haunted_event47
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    cam "Let's look around; you have the flashlight."
elif branchIsabella  and wt_hh_girl_pick=="Isabella":
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event49
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    if not persistent.fx_tip:
        $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        pause
        hide screen specialmsg
        $ persistent.fx_tip = True

    mc "Spooky! Are you scared yet?"
    isa "Only of the educational system responsible for letting someone write a note that way."
    mc "Let's find those keys!"
elif branchSage  and wt_hh_girl_pick=="Sage":
    scene ep9_diks_ph2_haunted_event55 with dissolve
    mc "Oh? So, we have to find three keys?"
    scene ep9_diks_ph2_haunted_event56 with dissolve
    sa "Either that or we stay locked inside here forever."
    sa "Not that I mind, I can think of many things to do with you in the dark."
    scene ep9_diks_ph2_haunted_event57 with dissolve
    mc "Haha, I think we're supposed to be scared, not aroused."
    scene ep9_diks_ph2_haunted_event56 with dissolve
    sa "Why not both?"
    scene ep9_diks_ph2_haunted_event57 with dissolve
    mc "Let's find those keys."
    scene ep9_diks_ph2_haunted_event58 with dissolve
    sa "Just tell me where to point the flashlight."
elif branchJill and wt_hh_girl_pick=="Jill":
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event50
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    if not persistent.fx_tip:
        $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        pause
        hide screen specialmsg
        $ persistent.fx_tip = True

    ji "Is it a riddle?"
    scene ep9_diks_ph2_haunted_event51
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "I think it might be. We definitely should look for those keys in here."
    mc "Wanna hold the flashlight?"
    scene ep9_diks_ph2_haunted_event50
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    ji "I think it's best if you do it."
elif branchMayaJosy and wt_hh_girl_pick=="Maya":
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event52
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    if not persistent.fx_tip:
        $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        pause
        hide screen specialmsg
        $ persistent.fx_tip = True

    my "Oh! This is so cool! It's like one of those escape rooms!"
    js "A what?"
    my "You know, a game where you must find a way to escape. They are usually very clever!"
    scene ep9_diks_ph2_haunted_event53
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    js "What's this about a vengeful spirit?"
    scene ep9_diks_ph2_haunted_event54
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "So, what now? Do we have to find the keys to that door?"
    scene ep9_diks_ph2_haunted_event52
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    my "Yeah! Let's find them. You'll have to point that flashlight though, it's impossible for us to spread out when we can't see."

$ tmpList = []
$ tmpList.append("ep9_hm_note_event_label")
$ tmpList.append("ep9_hm_jar_event_label")
$ tmpList.append("ep9_hm_jar2_event_label")
$ tmpList.append("ep9_hm_freezer_lock_event")
$ tmpList.append("ep9_hm_torture_event_label")
$ tmpList.append("ep9_hm_torture_state")
$ tmpList.append("ep9_hm_key_event_label")
$ tmpList.append("ep9_hm_key_eventb_label")

label ep9_hm_main_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_main_label"

if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True


scene ep9_hm_main
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve

if not persistent.fx_tip:
    $ specialMessage = "{size=-%d}If you experience lag, disable Settings > Special effects{/size}" % (5 * persistent.scale_factor)
    show screen specialmsg
    pause
    hide screen specialmsg
    $ persistent.fx_tip = True

$ ui.imagebutton("ep9_hm_main_door_idle", "ep9_hm_main_door_hover", clicked=ui.returns("door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_main_stock_idle", "ep9_hm_main_stock_hover", clicked=ui.returns("stock"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_main_freezer_idle", "ep9_hm_main_freezer_hover", clicked=ui.returns("freezer"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_main_jars_idle", "ep9_hm_main_jars_hover", clicked=ui.returns("jars"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_main_cage_idle", "ep9_hm_main_cage_hover", clicked=ui.returns("cage"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_note_label
elif result == "jars":
    jump ep9_hm_jars_label
elif result == "cage":
    if not "ep9_hm_note_event_label" in tmpList:
        jump ep9_hm_torture2_label
    else:
        mc "A scary-looking cage."
        jump ep9_hm_main_label
elif result == "stock":
    jump ep9_hm_torture_label
elif result == "freezer":
    jump ep9_hm_freezer_label
elif result == "door":
    jump ep9_hm_door_label

label ep9_hm_note_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_note_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_note
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_note_idle", "ep9_hm_note_hover", clicked=ui.returns("note"), xpos=0, ypos=0, focus_mask=True)

$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "note":
    if "ep9_hm_note_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_note_event_label")
        jump ep9_hm_note_event_label
    else:
        mc "This note is probably a clue."
        jump ep9_hm_note_label

label ep9_hm_door_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_door_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_door
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_door_lock_idle", "ep9_hm_door_lock_hover", clicked=ui.returns("lock"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "lock":
    if "ep9_hm_jar2_event_label" in tmpList and "ep9_hm_key_event_label" in tmpList and "ep9_hm_freezer_lock_event" in tmpList:
        mc "These are the three locks the note mentioned. We need to find three keys."
        jump ep9_hm_door_label
    elif "ep9_hm_jar2_event_label" in tmpList or "ep9_hm_key_event_label" in tmpList or "ep9_hm_freezer_lock_event" in tmpList:
        mc "These are the three locks the note mentioned. I need three keys..."
        jump ep9_hm_door_label
    else:
        $ currentEvent = "ep9_hm_escape_event_label"
        jump startEvent


label ep9_hm_jars_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_jars_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_jars
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_jars1_idle", "ep9_hm_jars1_hover", clicked=ui.returns("jar1"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_jars2_idle", "ep9_hm_jars2_hover", clicked=ui.returns("jar2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_jars3_idle", "ep9_hm_jars3_hover", clicked=ui.returns("jar3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_jars4_idle", "ep9_hm_jars4_hover", clicked=ui.returns("jar4"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "jar1":
    if not "ep9_hm_jar2_event_label" in tmpList:
        mc "We already found a key in a jar. We don't need to do more with these."
        jump ep9_hm_jars_label
    elif "ep9_hm_note_event_label" in tmpList:
        mc "There are some jars here with slime or something. They look nasty."
        jump ep9_hm_jars_label
    elif "ep9_hm_jar_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_jar_event_label")
        jump ep9_hm_jar_event_label
    else:
        $ mouse_visible = True

        scene ep9_hm_jars1
        hide screen flashlight_screen
        with dissolve

        mc "Eww! I can't feel anything, only slime."
        jump ep9_hm_jars_label
elif result == "jar2":
    if not "ep9_hm_jar2_event_label" in tmpList:
        mc "We already found a key in a jar. We don't need to do more with these."
        jump ep9_hm_jars_label
    elif "ep9_hm_note_event_label" in tmpList:
        mc "There are some jars here with slime or something. They look nasty."
        jump ep9_hm_jars_label
    elif "ep9_hm_jar_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_jar_event_label")
        jump ep9_hm_jar_event_label
    else:
        $ mouse_visible = True

        scene ep9_hm_jars2
        hide screen flashlight_screen
        with dissolve

        mc "Eww! I can't feel anything, only slime."
        jump ep9_hm_jars_label
elif result == "jar3":
    if not "ep9_hm_jar2_event_label" in tmpList:
        mc "We already found a key in a jar. We don't need to do more with these."
        jump ep9_hm_jars_label
    elif "ep9_hm_note_event_label" in tmpList:
        mc "There are some jars here with slime or something. They look nasty."
        jump ep9_hm_jars_label
    elif "ep9_hm_jar_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_jar_event_label")
        jump ep9_hm_jar_event_label
    else:
        $ tmpList.remove("ep9_hm_jar2_event_label")
        jump ep9_hm_jar2_event_label
elif result == "jar4":
    if not "ep9_hm_jar2_event_label" in tmpList:
        mc "We already found a key in a jar. We don't need to do more with these."
        jump ep9_hm_jars_label
    elif "ep9_hm_note_event_label" in tmpList:
        mc "There are some jars here with slime or something. They look nasty."
        jump ep9_hm_jars_label
    elif "ep9_hm_jar_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_jar_event_label")
        jump ep9_hm_jar_event_label
    else:
        $ mouse_visible = True

        scene ep9_hm_jars3
        hide screen flashlight_screen
        with dissolve

        mc "Eww! I can't feel anything, only slime."
        jump ep9_hm_jars_label

label ep9_hm_jar_event_label:
hide screen new_phone_screen
if branchAlone and wt_hh_girl_pick=="Camila":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event59
    hide screen flashlight_screen
    with dissolve

    mc "That looks like slime."
    ri "Aren't slime and goo kind of the same thing?"
    scene ep9_diks_ph2_haunted_event60 with dissolve
    cam "Yeah, maybe this is what that clue meant?"
    scene ep9_diks_ph2_haunted_event69 with dissolve
elif branchIsabella and wt_hh_girl_pick=="Isabella":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event63
    hide screen flashlight_screen
    with dissolve

    mc "That looks like slime."
    isa "I think that's the \"goo\" we should look for."
    scene ep9_diks_ph2_haunted_event69 with dissolve
elif branchSage and wt_hh_girl_pick=="Sage":
    $ mouse_visible = True

    if affinity == "DIK":
        scene ep9_diks_ph2_haunted_event70
    else:
        scene ep9_diks_ph2_haunted_event70b
    hide screen flashlight_screen
    with dissolve

    mc "That looks like slime."
    sa "You should try drinking some."
    mc "Huh? You think?"
    sa "Haha! No!"
    sa "You get what these are, right?"
    scene ep9_diks_ph2_haunted_event69 with dissolve
    mc "Uh... Am I supposed to?"
    sa "Remember what that note said? {i}Goo{/i} luck? This must be the goo."
    mc "Oh! Yeah!"
elif branchJill  and wt_hh_girl_pick=="Jill":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event67
    hide screen flashlight_screen
    with dissolve

    mc "That looks like slime."
    ji "Slime? Maybe it's \"goo\"?"
    mc "Oh, yeah!"
    scene ep9_diks_ph2_haunted_event69 with dissolve
elif branchMayaJosy  and wt_hh_girl_pick=="Maya":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event68
    hide screen flashlight_screen
    with dissolve

    mc "That looks like slime."
    my "That must be the \"goo\" the note mentioned!"
    scene ep9_diks_ph2_haunted_event69 with dissolve
mc "Uh... So, I'm supposed to stick my hand in these?"
$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_jar2_event_label:
hide screen new_phone_screen
$ mouse_visible = True

scene ep9_diks_ph2_haunted_event62
hide screen flashlight_screen
with dissolve

mc "EWw! Wait! There's something in here. It's a key!"
if branchIsabella  and wt_hh_girl_pick=="Isabella":
    isa "A highly impractical place for a key if you ask me."
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event64
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    mc "So, you're only gonna remark things like that throughout this experience?"
    scene ep9_diks_ph2_haunted_event66
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "What? I'm humorous."
    scene ep9_diks_ph2_haunted_event64
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Oh. I thought you didn't find this fun."
    scene ep9_diks_ph2_haunted_event65
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "Well, that too."
    scene ep9_diks_ph2_haunted_event64
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Oh..."
    scene ep9_diks_ph2_haunted_event65
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "That was another joke."
    scene ep9_diks_ph2_haunted_event64
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "I can't read your face with that costume on and barely without it."
elif branchAlone  and wt_hh_girl_pick=="Camila":
    if persistent.fx:
        $ mouse_visible = False
    else:
        $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event61
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve

    ri "Good thing it wasn't for nothing, but that would have been even funnier!"
    cam "Haha!"
elif branchSage  and wt_hh_girl_pick=="Sage":
    sa "You should wipe your hand on something."
    scene ep9_diks_ph2_haunted_event71 with dissolve
    mc "Thanks for offering."
    sa "Haha! Hey! No! Not me!"
    scene ep9_diks_ph2_haunted_event72 with dissolve
    mc "Ok, we got this key. What now?"
elif branchJill  and wt_hh_girl_pick=="Jill":
    ji "It is? The clue was right!"
elif branchMayaJosy  and wt_hh_girl_pick=="Maya":
    js "Yes!"
    my "You found one! What's next?"
$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_freezer_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_freezer_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_freezer
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_freezer_key_idle", "ep9_hm_freezer_key_hover", clicked=ui.returns("key"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep9_hm_freezer_lock_idle", "ep9_hm_freezer_lock_hover", clicked=ui.returns("lock"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "lock":
    if "ep9_hm_freezer_lock_event" in tmpList:
        jump ep9_hm_freezer_lock_label
    else:
        mc "(I already found that key.)"
        jump ep9_hm_freezer_label
elif result == "key":
    mc "Someone drew a key on the freezer, but there's a combination lock on it."
    jump ep9_hm_freezer_label

label ep9_hm_freezer_lock_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_freezer_lock_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_freezer_lock
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_freezer_lock2_idle", "ep9_hm_freezer_lock2_hover", clicked=ui.returns("lock"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "lock":
    if "ep9_hm_torture_event_label" in tmpList:
        mc "I don't know the code... Maybe it's somewhere around here?"
        jump ep9_hm_freezer_lock_label
    else:
        $ tmpList.remove("ep9_hm_freezer_lock_event")
        jump ep9_hm_freezer_lock_event

label ep9_hm_freezer_lock_event:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_freezer_label"

mc "The combination must be the clue we found. 6-9-7!"
play sound "sound_effects/season3/enter_code.mp3"
scene ep9_hm_freezer_lockb with dissolve
mc "Yes, it's unlocked!"

if branchAlone  and wt_hh_girl_pick=="Camila":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event73
    hide screen flashlight_screen
    with dissolve

    cam "Eww! It looks like a brain."
    mc "I think it is."
    ri "That is so cool. And look! There's a key inside it."
    cam "Pull it out, [name]!"
elif branchIsabella  and wt_hh_girl_pick=="Isabella":
    isa "Who puts a lock on a freezer?"
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event74
    hide screen flashlight_screen
    with dissolve

    mc "Someone who put human remains inside of it, from the looks of it."
    mc "You're up."
    isa "What?"
    scene ep9_diks_ph2_haunted_event75 with dissolve
    mc "There's a key lodged in that brain. You get to remove it."
    scene ep9_diks_ph2_haunted_event76 with dissolve
    isa "I think I'll stick to narrating the experience and letting you do the dirty work."
    scene ep9_diks_ph2_haunted_event74 with dissolve
    mc "Ugh..."
    isa "The key is lodged in the brain in the freezer. That's a sentence I never thought I'd say."
elif branchJill  and wt_hh_girl_pick=="Jill":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event79
    hide screen flashlight_screen
    with dissolve

    ji "What is that? Is that a brain?"
    mc "Yeah, it is."
    scene ep9_diks_ph2_haunted_event80 with dissolve
    ji "Jacob did a very good job on this. Haha, it's so gross."
    ji "Look, there's a key in there! Get it out!"
elif branchMayaJosy  and wt_hh_girl_pick=="Maya":
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event81
    hide screen flashlight_screen
    with dissolve

    js "Oh my God! What the hell is that!?"
    my "Wow! It's not real, is it? Could it be the brain of the vengeful ghost?"
    scene ep9_diks_ph2_haunted_event82 with dissolve
    mc "There's a key stuck in the brain. We have to pull it out."
    js "You do it! I'm not touching that!"

if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_freezer2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


$ ui.imagebutton("ep9_hm_freezer2_idle", "ep9_hm_freezer2_hover", clicked=ui.returns("key"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

mc "There! That did it."
if branchAlone  and wt_hh_girl_pick=="Camila":
    cam "Yay! Can we escape yet?"
elif branchIsabella  and wt_hh_girl_pick=="Isabella":
    scene ep9_diks_ph2_haunted_event77
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "Through the moderate use of brain power, [name] found the key in the freezer and dislodged it from the brain."
    scene ep9_diks_ph2_haunted_event78
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "You don't have to narrate anymore."
    scene ep9_diks_ph2_haunted_event77
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "I'll be here if you need me."
$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_torture_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_torture_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True
if "ep9_hm_torture_state" in tmpList:
    scene ep9_hm_torture
else:
    scene ep9_hm_tortureb
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


if "ep9_hm_torture_state" in tmpList:
    $ ui.imagebutton("ep9_hm_torture_latch_idle", "ep9_hm_torture_latch_hover", clicked=ui.returns("latch"), xpos=0, ypos=0, focus_mask=True)
if "ep9_hm_torture_state" in tmpList:
    $ ui.imagebutton("ep9_hm_torture_symbols_idle", "ep9_hm_torture_symbols_hover", clicked=ui.returns("symbols"), xpos=0, ypos=0, focus_mask=True)
else:
    $ ui.imagebutton("ep9_hm_tortureb_symbols_idle", "ep9_hm_tortureb_symbols_hover", clicked=ui.returns("symbols2"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()


if result == "go_down":
    if not "ep9_hm_torture_state" in tmpList:
        $ tmpList.append("ep9_hm_torture_state")
    jump ep9_hm_main_label
elif result == "latch":
    mc "This looks like a torture device... I think the top part moves."
    play sound "sound_effects/door_lock.mp3"
    if "ep9_hm_torture_state" in tmpList:
        $ tmpList.remove("ep9_hm_torture_state")
    jump ep9_hm_torture_label
elif result == "symbols":
    if "ep9_hm_torture_event_label" in tmpList:
        mc "There are some weird symbols on it."
    else:
        mc "(Those symbols were numbers.)"
    jump ep9_hm_torture_label
elif result == "symbols2":
    if "ep9_hm_torture_event_label" in tmpList:
        $ tmpList.remove("ep9_hm_torture_event_label")
        jump ep9_hm_torture_event_label
    else:
        if not branchSage:
            mc "(6-9-7.)"
        else:
            mc "(It's supposed to be scary...not kinky... Right?)"
        jump ep9_hm_torture_label

label ep9_hm_torture_event_label:
hide screen new_phone_screen
mc "Look, it opens!"
mc "Those symbols; they are numbers!"
if branchAlone  and wt_hh_girl_pick=="Camila":
    ri "That's pretty clever."
    cam "6-9-7!"
elif branchIsabella  and wt_hh_girl_pick=="Isabella":
    isa "I saw that before you opened the latch, but I didn't want to ruin your experience."
    if affinity == "DIK":
        mc "Sarcasm?"
    else:
        mc "How thoughtful."
elif branchSage  and wt_hh_girl_pick=="Sage":
    mc "6-9-7!"
    scene ep9_diks_ph2_haunted_event83
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "Kinky as fuck! I didn't know Jacob was into this shit."
    mc "Uh... I'm pretty sure he isn't."
elif branchJill  and wt_hh_girl_pick=="Jill":
    ji "You're right! They are! 6-9-7!"
elif branchMayaJosy  and wt_hh_girl_pick=="Camila":
    my "Oh! Now they make sense!"
$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_torture2_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_torture2_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

scene ep9_hm_torture2
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


if "ep9_hm_key_eventb_label" in tmpList:
    mc "A scary-looking cage!"
    mc "Do you think this is the cage from the clue we found on that note?"
    if branchSage  and wt_hh_girl_pick=="Sage":
        sa "Either that or this vengeful ghost likes it kinky. Haha!"
        mc "Give me that flashlight; I need to check it out."
    $ tmpList.remove("ep9_hm_key_eventb_label")

$ ui.imagebutton("fr_go_up_small_hover", "fr_go_up_small_hover", clicked=ui.returns("go_up"), xpos=800 * persistent.scale_factor, ypos=100 * persistent.scale_factor)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_main_label
elif result == "go_up":
    jump ep9_hm_torture3_label


label ep9_hm_torture3_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ currentFreeRoamLabel = "ep9_hm_torture3_label"
if persistent.fx:
    $ mouse_visible = False
else:
    $ mouse_visible = True

if not "ep9_hm_key_event_label" in tmpList:
    scene ep9_hm_torture3
else:
    scene ep9_hm_torture3_key
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve


if "ep9_hm_key_event_label" in tmpList:
    $ ui.imagebutton("ep9_hm_torture3_key_hover", "ep9_hm_torture3_key_hover", clicked=ui.returns("key"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_go_down", "fr_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840 * persistent.scale_factor)
$ result = ui.interact()

if result == "go_down":
    jump ep9_hm_torture2_label
elif result == "key":
    $ tmpList.remove("ep9_hm_key_event_label")
    jump ep9_hm_key_event_label

label ep9_hm_key_event_label:
hide screen new_phone_screen
mc "A key! I found it!"
if branchAlone  and wt_hh_girl_pick=="Camila":
    scene ep9_diks_ph2_haunted_event84
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    ri "I didn't even see that one. That one was hard to spot."
elif branchIsabella  and wt_hh_girl_pick=="Isabella":
    scene ep9_diks_ph2_haunted_event85
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    isa "To the vengeful ghost's dismay."
elif branchSage  and wt_hh_girl_pick=="Sage":
    label ep9_sage_lewd2_label:
    if _in_replay:
        hide screen new_phone_screen
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_sage == None:
            $ mc_sage = name
        else:
            $ mc_sage = persistent.mc_sage
        if persistent.sage == None:
            $ sage = "Sage"
        else:
            $ sage = persistent.sage
        $ affinity = "CHICK"
        if persistent.fx:
            $ mouse_visible = False
        else:
            $ mouse_visible = True
        play music "music/ep9/licensed_music/track116.mp3"
    scene ep9_diks_ph2_haunted_event88
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Hey! What are you doing?"
    scene ep9_diks_ph2_haunted_event89
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "You fell into my trap, [name]. Now you're gonna stay down here with me forever."
    scene ep9_diks_ph2_haunted_event88
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "What?"
    scene ep9_diks_ph2_haunted_event90
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "I'm the vengeful kinky ghost! AHHHH!!!"
    scene ep9_diks_ph2_haunted_event91
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Very funny."
    scene ep9_diks_ph2_haunted_event90
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "It's hot seeing you in that cage."
    scene ep9_diks_ph2_haunted_event91
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "Come on, let me out."
    scene ep9_diks_ph2_haunted_event92
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "Nuh-uh. Not until you find the key and the lock."
    scene ep9_diks_ph2_haunted_event93
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    mc "What lock?"
    scene ep9_diks_ph2_haunted_event94
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    sa "This warm and moist lock. Can you guess what the key is?"
    if affinity == "DIK":
        $ mouse_visible = True

        scene ep9_diks_ph2_haunted_event95
        hide screen flashlight_screen
        with dissolve

        mc "(Must. Resist. Urge.)"
        scene ep9_diks_ph2_haunted_event94 with dissolve
    mc "I think I have a good guess."
    sa "Unlock me, [mc_sage]."
    $ mouse_visible = True

    scene ep9_diks_ph2_haunted_event96
    hide screen flashlight_screen
    with dissolve

    $ renpy.pause()
    scene ep9_diks_ph2_haunted_event97 with dissolve
    $ renpy.pause()
    scene anim_sage_hm_bj_ep9 with dissolve
    mc "So, we're not doing the haunted basement anymore?"
    sa "*{i}Suck suck{/i}* We'll get to it eventually."
    mc "What if the vengeful ghost shows up?"
    sa "*{i}Suck suck{/i}* We'll make her join! Haha!"
    pause
    scene anim_sage_hm_bj2_ep9 with dissolve
    sa "Hnn... Mmmphfff..."
    pause
    scene anim_sage_hm_bj3_ep9 with dissolve
    pause

    scene ep9_diks_ph2_haunted_event98 with dissolve
    sa "You unlocked the cage. Well done! Haha!"
    scene ep9_diks_ph2_haunted_event99 with dissolve
    mc "You got me so hard..."
    sa "Haha, whoops! What are we gonna do about it?"
    mc "You tell me."
    scene ep9_diks_ph2_haunted_event100 with dissolve
    sa "How about you try this thing?"
    mc "Isn't it for torturing people?"
    sa "Who cares?"
    scene ep9_diks_ph2_haunted_event101 with dissolve
    sa "What are you gonna do to me?"
    scene ep9_diks_ph2_haunted_event102 with dissolve
    mc "I haven't made up my mind yet."
    sa "You should punish me."
    scene ep9_diks_ph2_haunted_event103 with dissolve
    mc "Why? Have you been bad?"
    scene ep9_diks_ph2_haunted_event104 with dissolve
    sa "So bad! I'm locked in here; that should tell you how bad I've been."
    scene bg anim_sage_hm_spank_ep9 movie with dissolve
    sa "Ah!!! Oh!!!"
    mc "Are you gonna behave?"
    sa "Nuh-uh!"
    sa "AHHH!!!"
    pause
    scene ep9_diks_ph2_haunted_event105 with dissolve
    mc "I think I need to unlock you from this thing. I think I found another keyhole."
    scene ep9_diks_ph2_haunted_event106 with dissolve
    sa "[mc_sage]... This is fucking hot!"
    sa "*{i}Moans{/i}*"
    scene anim_sage_hm_fuck1_ep9 with dissolve
    sa "Fuck me! Punish me!"
    pause
    scene anim_sage_hm_fuck2_ep9 with dissolve
    sa "Deeper! Harder!"
    pause
    scene ep9_diks_ph2_haunted_event108 with dissolve
    sa "Fuck me, [mc_sage]!"
    scene anim_sage_hm_fuck2_ep9 with dissolve
    sa "Don't stop! I'm gonna cum! AAAHHHH!!!"
    pause
    scene ep9_diks_ph2_haunted_event107 with vpunch
    sa "AHHH!!!!"
    scene ep9_diks_ph2_haunted_event109 with dissolve
    py "Ah!!! Guys! What are you doing!?"
    sa "Huh!? What?"
    mc "Oh shit!"
    scene ep9_diks_ph2_haunted_event110 with dissolve
    sa "Who is that?"
    mc "Uh. It's Penny."
    mc "Are you the ghost?"
    scene ep9_diks_ph2_haunted_event111 with dissolve
    py "Yeah... Jacob asked me to scare people as they exited, but this is very uncomfortable."
    scene ep9_diks_ph2_haunted_event112 with dissolve
    mc "Uh... Sorry. We were looking for clues and got sidetracked."
    scene ep9_diks_ph2_haunted_event114 with dissolve
    sa "[name]!? Can you cover me up? I'm kind of exposed here."
    scene ep9_diks_ph2_haunted_event113b with dissolve
    $ renpy.pause(0.5)
    scene ep9_diks_ph2_haunted_event113 with dissolve
    mc "..."
    scene ep9_diks_ph2_haunted_event115 with dissolve
    py "I don't wanna do this anymore."
    scene ep9_diks_ph2_haunted_event116 with dissolve
    sa "Did we just ruin the haunted basement tour?"
    mc "Uh... I think so."
    scene ep9_diks_ph2_haunted_event117 with dissolve
    sa "I should apologize to her."
    stop music fadeout 3
    scene ep9_diks_ph2_haunted_event118 with dissolve
    mc "Yeah... Tell her I'm sorry too."
    hide screen freeroam_help
    $ renpy.end_replay()
    $ persistent.ep9_lewd_sage2 = True
    $ calcScenes()
    $ new_bio("Sage", "I had sex with Sage during the Haunted Mansion tour. We were being careless, and Penny saw everything.")
    $ mphone_stats_add_girl_s3("sage","You had sex with Sage during the Haunted mansion activity in episode 9.")
    jump ep9_hm_escape_event2_label
elif branchJill  and wt_hh_girl_pick=="Jill":
    scene ep9_diks_ph2_haunted_event86
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    ji "Great, I wish I could be of more help, but there's no way I could fit in that cage wearing this."
elif branchMayaJosy  and wt_hh_girl_pick=="Maya":
    scene ep9_diks_ph2_haunted_event87
    if persistent.fx:
        show screen flashlight_screen
    else:
        hide screen flashlight_screen
    with dissolve
    my "Way to go!"
    js "Great! Can we, like, get out of here already?"

$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_note_event_label:
hide screen new_phone_screen
scene ep9_diks_ph2_haunted_event119
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "Hm... Do you think the note itself is a clue?"
if branchAlone and wt_hh_girl_pick=="Camila":
    ri "Yeah... Why does it say \"goo luck\"? And goo is green."
    cam "And those capital letters spell something, I think."
    mc "C-A-G-E. Yeah! Cage!"
    ri "Those must be clues!"
elif branchIsabella and wt_hh_girl_pick=="Isabella":
    isa "If the capitalized letters spelling out CAGE and the glaring typo in green saying \"goo\" are intentional..."
    isa "Perhaps."
    mc "I think you're on to something."
elif branchSage and wt_hh_girl_pick=="Sage":
    sa "It sure looks like it."
elif branchJill and wt_hh_girl_pick=="Jill":
    ji "Possibly. It's weirdly written. Why are only a few letters capitalized?"
    mc "C-A-G-E. Cage! Is that a clue?"
    ji "It doesn't say \"good luck\", it says \"goo luck\". Is that a typo or another clue?"
elif branchMayaJosy and wt_hh_girl_pick=="Maya":
    my "It could be. Some letters are weirdly capitalized."
    mc "C-A-G-E. Cage! Is that a clue?"
    my "There's a cage over there!"
    js "What about the end of the letter? Look! It's misspelled."
    mc "Goo luck?"
    my "Goo! That might be another clue."
$ renpy.jump(currentFreeRoamLabel)

label ep9_hm_escape_event_label:
hide screen new_phone_screen
scene ep9_diks_ph2_haunted_event120
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "Ok, we have all keys. We can unlock the door now."
play sound "sound_effects/key_jiggle.mp3"
scene ep9_diks_ph2_haunted_event121
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
mc "It's open! We did it! We can exit now."
scene bg anim_haunted_hand_ep9 movie
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
with dissolve
$ renpy.pause(1)
$ renpy.play("sound_effects/scare.mp3","sfx1")
$ renpy.play("sound_effects/season2/shriek.mp3","sfx1")
stop music
$ renpy.pause(1)
mc "AAHH!!!"
py "OOOOHHHH!!! AAHHHH!!"
$ mouse_visible = True


if branchAlone and wt_hh_girl_pick=="Camila":
    scene ep9_diks_ph2_haunted_event122
    hide screen flashlight_screen
    with dissolve

    ri "Shit! AHH!!"
    cam "HAHAHA! WOW!"
    scene ep9_diks_ph2_haunted_event123 with dissolve
    ri "Penny! You asshole!"
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "Hahaha! Sorry! Don't blame me, this was Jacob's idea."
    py "He asked me to scare people when they unlocked the door. He told me I didn't have to pay the cover charge if I did, so..."
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "I gotta admit, you got me."
    scene ep9_diks_ph2_haunted_event123 with dissolve
    ri "You got me too! I think Cammy is the only one who wasn't scared."
    scene ep9_diks_ph2_haunted_event124 with dissolve
    cam "Haha! If I opened the door I would be, but I saw how [name] jumped and screamed like a girl and I started laughing!"
    scene ep9_diks_ph2_haunted_event127 with dissolve
    ri "Haha! Yeah! What's up with that? I thought you were going to protect us."
    scene ep9_diks_ph2_haunted_event128 with dissolve
    mc "I mean... Screaming is a way to assert dominance."
    scene ep9_diks_ph2_haunted_event124 with dissolve
    cam "Haha! Not with that pitch!"
    ri "Hahaha!"
elif branchIsabella and wt_hh_girl_pick=="Isabella":
    scene ep9_diks_ph2_haunted_event129
    hide screen flashlight_screen
    with dissolve

    isa "Oh, shit!"
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "Penny? You're the ghost?"
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "Haha! Sorry. Jacob asked me to scare people when they unlocked the door. He told me I didn't have to pay the cover charge if I did, so..."
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "You did a great job; I almost shit myself."
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "You escaped the haunted basement! Congratulations, now I don't have to kill you."
    scene ep9_diks_ph2_haunted_event130 with dissolve
    mc "Look at you. She scared you, didn't she?"
    scene ep9_diks_ph2_haunted_event131 with dissolve
    isa "The scary part was knowing she was in there all the time with us. I didn't say something revealing, did I?"
    scene ep9_diks_ph2_haunted_event132 with dissolve
    mc "No, I don't think you did."
    mc "I'm happy you got a bit scared."
    scene ep9_diks_ph2_haunted_event131 with dissolve
    isa "I wasn't scared."
    scene ep9_diks_ph2_haunted_event132 with dissolve
    mc "I think you were."
elif branchJill and wt_hh_girl_pick=="Jill":
    scene ep9_diks_ph2_haunted_event133
    hide screen flashlight_screen
    with dissolve

    ji "Oh, fuck!"
    scene ep9_diks_ph2_haunted_event134 with dissolve
    mc "What the hell?"
    ji "Haha! What is this!?"
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "Penny? You're the ghost?"
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "Haha! Sorry. Jacob asked me to scare people when they unlocked the door. He told me I didn't have to pay the cover charge if I did, so..."
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "You did a great job; I almost shit myself."
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "You escaped the haunted basement! Congratulations, now I don't have to kill you."
    scene ep9_diks_ph2_haunted_event135 with dissolve
    mc "Haha, did you say \"fuck\"?"
    ji "Did I? No, I didn't."
    mc "Haha! I think you did! You got so scared!"
    scene ep9_diks_ph2_haunted_event136 with dissolve
    ji "What about you? You screamed really loud!"
    mc "Hahaha!"
elif branchMayaJosy and wt_hh_girl_pick=="Maya":
    scene ep9_diks_ph2_haunted_event137
    hide screen flashlight_screen
    with dissolve

    js "Fuck! That scared me!"
    my "Hahaha! I loved this!"
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "Penny? You're the ghost?"
    scene ep9_diks_ph2_haunted_event125 with dissolve
    py "Haha! Sorry. Jacob asked me to scare people when they unlocked the door. He told me I didn't have to pay the cover charge if I did, so..."
    scene ep9_diks_ph2_haunted_event126 with dissolve
    mc "You did a great job; I almost shit myself."
    scene ep9_diks_ph2_haunted_event138 with dissolve
    my "That was SO fun!"
    js "Guys, my heart can't take this."
    scene ep9_diks_ph2_haunted_event139 with dissolve
    mc "Haha, I'm with you. Let's have a drink to calm our nerves."
hide screen freeroam_help
label ep9_hm_escape_event2_label:

if wt_ep9_branch_numbers > 1:
   "Replay Haunted Mansion with someone else?"
   menu:
      "Yes":
          jump ep9_diks_ph2_haunted_event_label
      "No":
          pass

$ mouse_visible = True

if minigames:
    scene ep9_diks_ph2_haunted_event69
else:
    scene black
hide screen flashlight_screen
with dissolve

show screen new_phone_screen
$ renpy.pause(0.5)


if minigames:
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
    $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
    $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)

    $ pp_update_happiness_icons()
    $ mphone_pp_history_list.append("• The {color=ffed00}Haunted Mansion{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Haunted Mansion{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Haunted Mansion{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Haunted Mansion{/color} activity increased Nick's happiness by {color=00ff00}+2%{/color}.")
    show screen specialmsg
    pause
    hide screen specialmsg
$ currentFreeRoamLabel = "ep9_diks_ph2_main_label"
jump ep9_diks_ph2_preps_event_label

label ep9_diks_ph2_no_event_label:
if "ep9_diks_ph2_riona_event2_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_riona_event2_label")
scene ep9_diks_ph2_no_event1 with dissolve
bc "So, you have nothing planned?"
scene ep9_diks_ph2_no_event2 with dissolve
qu "There's a competition later, but that's about it."
scene ep9_diks_ph2_no_event1 with dissolve
bc "Wow, that sucks! I thought there would be something more than this for Halloween."
scene ep9_diks_ph2_no_event2 with dissolve
if branchAlone and ep8_quinn_lewd:
    qu "Blame Tommy. He only wanted dancing and drinking."
else:
    qu "Blame Tommy and [name]. They only wanted dancing and drinking."
scene ep9_diks_ph2_no_event3 with dissolve
mc "(Hm... Damn. I mean, it's only Becky, but still...)"
mc "(I wonder if other guests feel the party is boring now too.)"
$ currentFreeRoamLabel = "ep9_diks_ph2_main_label"
jump ep9_diks_ph2_preps_event_label

label ep9_jm_dance_label:
stop music fadeout 3
scene ep9_jm_dance1 with dissolve
$ renpy.pause()
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track124.mp3","music/ep9/licensed_music/track127.mp3","music/ep9/licensed_music/track125.mp3"])
scene ep9_jm_dance2 with dissolve
mc "Look at you two dancing together."
scene ep9_jm_dance3 with dissolve
my "Shake your butt with us, [name]."
scene ep9_jm_dance4 with dissolve
if ep2_choseMayaOverParty:
    mc "You remember how bad I'm at dancing, right?"
else:
    mc "I'm not too good at dancing."
scene ep9_jm_dance3 with dissolve
my "Trust me; it doesn't matter on this dance floor."
scene ep9_jm_dance5 with dissolve
js "We think that's why there's police tape around it. Because of how we're all dancing, it should be a crime."
scene ep9_jm_dance6 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Dance with Maya":
        label ep9_mdance_label:
        $ ep9_maya_dance = True
        scene ep9_jm_dance7 with dissolve
        $ renpy.pause(13)
        show screen click_to_continue_screen with dissolve
        $ renpy.pause(2)
        hide screen click_to_continue_screen with dissolve
        $ renpy.pause()
        menu:
            "Kiss her [mod_gr][mod_choices[1]]":
                $ RPmaya += 1
                scene ep9_jm_dance9 with dissolve
                $ renpy.pause()
                scene ep9_jm_dance10 with dissolve
                my "You're daring tonight..."
            "Don't kiss her":
                $ renpy.pause(0.5)
        if ep9_josy_dance:
            jump ep9_ldance_label
        menu:
            "[mod_gr]Dance with Josy":
                jump ep9_jdance_label
            "Leave":
                jump ep9_ldance_label
    "Dance with Josy":
        label ep9_jdance_label:
        $ ep9_josy_dance = True
        scene ep9_jm_dance8 with dissolve
        $ renpy.pause(13)
        show screen click_to_continue_screen with dissolve
        $ renpy.pause(2)
        hide screen click_to_continue_screen with dissolve
        $ renpy.pause()
        menu:
            "Kiss her [mod_gr][mod_choices[0]]":
                $ RPjosy += 1
                scene ep9_jm_dance11 with dissolve
                $ renpy.pause()
                scene ep9_jm_dance12 with dissolve
                js "*{i}Whispers{/i}* You're trying to turn me on, aren't you?"
                scene ep9_jm_dance12b with dissolve
                mc "Is it working?"
                scene ep9_jm_dance12 with dissolve
                js "Mhm..."
            "Don't kiss her":
                $ renpy.pause(0.5)
        if ep9_maya_dance:
            jump ep9_ldance_label
        menu:
            "[mod_gr]Dance with Maya":
                jump ep9_mdance_label
            "Leave":
                jump ep9_ldance_label

label ep9_ldance_label:
scene ep9_jm_dance13 with dissolve
mc "*{i}Phew{/i}* I need a drink. Thanks for the dance, girls."
if wt_ep9_branch_numbers > 1:
    $ task_list[3] = task_list[3].replace("\n Dance with Josy & Maya (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("\n Dance with Josy & Maya", "")
    $ task_list[3] = task_list[3].replace("Dance with Josy & Maya (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("Dance with Josy & Maya", "")
else:
    $ task_list[3] = ""
if task_list[3] == " ":
    $ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_jill_dance_label:
stop music fadeout 3
scene ep9_jill_dance1 with dissolve
ji "Where are you taking me?"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track121.mp3","music/ep9/licensed_music/track127.mp3","music/ep9/licensed_music/track124.mp3"])
scene ep9_jill_dance2 with dissolve
mc "Over there."
ji "Hahaha! You want me to dance in this?"
mc "Everyone's up there looking hilarious already. Let's go!"
scene ep9_jill_dance3 with dissolve
ji "I'm so happy I came tonight. This party...it's amazing!"
scene ep9_jill_dance4 with dissolve
mc "Right? I'm so happy you're enjoying yourself!"
scene ep9_jill_dance5 with dissolve
ji "I was invited to another party tonight, but there's no way I'm going if I can be with you instead."
scene ep9_jill_dance6 with dissolve
mc "What kind of a party?"
scene ep9_jill_dance5 with dissolve
ji "The Alpha Nu Omega has a Halloween party tonight too, but it's nowhere near this much fun! I can't believe this is what I've been missing out on."
scene ep9_jill_dance4 with dissolve
mc "Not too shabby, huh?"
scene ep9_jill_dance7 with vpunch
ji "Umpff..."
mc "Hahaha!"
scene ep9_jill_dance8 with dissolve
ji "Gah! This costume just reached a new level of unbearable."
ji "Not to mention, it's really hot inside it."
mc "Do you need a hand?"
scene ep9_jill_dance10 with dissolve
mc "Pull your head out of the hole for a bit. Let your head breathe."
scene ep9_jill_dance11 with dissolve
ji "Thank you. This feels a lot better."
scene ep9_jill_dance12 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep9_jill_dance13 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Jill)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        
                        
                        
            
menu:
    "Kiss her [mod_gr][mod_choices[0]]":
        $ RPjill += 1
        scene ep9_jill_dance14 with dissolve
        $ renpy.pause()
        scene ep9_jill_dance17 with dissolve
        ji "[name]... You're making out with me in public like this?"
        scene ep9_jill_dance18 with dissolve
        mc "You don't mind, right?"
        scene ep9_jill_dance17 with dissolve
        ji "I never did this before."
        scene ep9_jill_dance19 with dissolve
        mc "I've never made out with a banana before, so, we're both new at this."
        scene ep9_jill_dance15 with dissolve
        $ renpy.pause()
        scene ep9_jill_dance16 with dissolve
        $ renpy.pause()
        scene ep9_jill_dance15 with dissolve
        $ renpy.pause()
        scene ep9_jill_dance23 with dissolve
    "Hug her":
        scene ep9_jill_dance20 with dissolve
        ji "Can you even reach around when I'm wearing this?"
        scene ep9_jill_dance21 with dissolve
        mc "Yeah, but it's barely!"
        scene ep9_jill_dance22 with dissolve
bia "Aw, look at you two! So cute! We're interrupting, aren't we?"
scene ep9_jill_dance24 with dissolve
ji "It's fine. Oh! Hi, Matthew!"
scene ep9_jill_dance25 with dissolve
mat "Jill! I managed to sneak in, haha."
scene ep9_jill_dance26 with dissolve
bia "You shouldn't say that out loud."
scene ep9_jill_dance27 with dissolve
mc "Don't worry; he's welcome here."
scene ep9_jill_dance28 with dissolve
mat "Thanks, [name]! It's been a while since my last college party. I thought I'd feel old coming here, but it's just like old times."
scene ep9_jill_dance29 with dissolve
ji "Are you guys going to dance too?"
scene ep9_jill_dance30 with dissolve
bia "I saw you up here and couldn't let you go crazier than me tonight! Haha!"
scene ep9_jill_dance29 with dissolve
ji "Is that what it looked like?"
scene ep9_jill_dance30 with dissolve
bia "Haha! Show me your best moves, banana!"
scene ep9_jill_dance31 with dissolve
mc "You go ahead, I need a break."

if wt_ep9_branch_numbers > 1:
    $ task_list[3] = task_list[3].replace("Dance with Jill (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("Dance with Jill", "")

else:
    $ task_list[3] = ""

if task_list[3] == " ":
    $ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_isabella_dance_label:
stop music fadeout 3
scene ep9_bella_dance1 with dissolve
mc "Drunk enough to dance with me?"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track124.mp3","music/ep9/licensed_music/track127.mp3","music/ep9/licensed_music/track125.mp3"])
scene ep9_bella_dance2 with dissolve
isa "It's been a while... Maybe we shouldn't..."
mc "You'll be fine. Especially while dancing next to me, because I can't even dance and people don't wanna watch me do it."
scene ep9_bella_dance3 with dissolve
isa "I loved dancing when I went to college."
mc "Yeah? Spent many parties doing it?"
scene ep9_bella_dance4 with dissolve
isa "Definitely. And there were dance classes at the local gym where you danced as exercise."
scene ep9_bella_dance5 with dissolve
mc "I'd say it sounds fun, but also like something I wouldn't enjoy."
mc "Dancing isn't something I do when I'm completely sober."
scene ep9_bella_dance6 with dissolve
isa "Do you expect yourself to excel without practice?"
scene ep9_bella_dance5 with dissolve
mc "Not really. But I feel so stupid dancing."
scene ep9_bella_dance6 with dissolve
isa "Move your body slowly to the beat of the bass."
isa "You don't have to go crazy when you dance."
scene ep9_bella_dance7 with dissolve
mc "Hm? Is that what I'm doing wrong? It feels like I should be moving around more."
scene ep9_bella_dance8 with dissolve
isa "Then dance with me like this. Now you can't move too much."
isa "Follow my lead. Small steps with your feet."
scene ep9_bella_dance9 with dissolve
isa "Good. But don't look at your feet. Look at my face."
menu:
    "Ok, looking at your face":
        mc "Ok. I'm looking..."
    "Was looking at your body":
        mc "I was looking at your body."
        isa "No, you weren't. I can tell when you are."
scene ep9_bella_dance10 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep9_bella_dance11b with Dissolve(2)
$ renpy.pause()
scene ep9_bella_dance11a with Dissolve(2)
$ renpy.pause()
scene ep9_bella_dance11c with Dissolve(2)
$ renpy.pause()
scene ep9_bella_dance11 with dissolve
isa "See?"
scene ep9_bella_dance12 with dissolve
mc "I can dance..."
scene ep9_bella_dance11 with dissolve
isa "You're doing great. Are you feeling more comfortable?"
scene ep9_bella_dance12 with dissolve
mc "I am."
scene ep9_bella_dance13 with dissolve
isa "Now, do the same but without me holding you in place."
mc "Yeah... This works."
scene ep9_bella_dance14 with dissolve
isa "You're getting the hang of it."
scene ep9_bella_dance15 with dissolve
mc "I preferred it when you had your arms around my neck."
scene ep9_bella_dance16 with dissolve
isa "Of course, you did."
scene ep9_bella_dance17 with dissolve
mc "I wish I could kiss you right now."
isa "Me too."
if not branchJill:
    scene ep9_bella_dance18 with dissolve
    $ renpy.pause()
    scene ep9_bella_dance19 with dissolve
    $ renpy.pause()
if wt_ep9_branch_numbers > 1:
    $ task_list[3] = task_list[3].replace("\n Dance with Bella (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("\n Dance with Bella", "")
else:
    $ task_list[3] = ""
if task_list[3] == " ":
    $ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_sage_dance_label:
stop music fadeout 3
scene ep9_sage_dance1 with dissolve
if ep2_danceSage:
    mc "(Seeing her on this dance floor... Haha, it takes me back.)"
else:
    mc "(There she is.)"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track127.mp3","music/ep9/licensed_music/track125.mp3","music/ep9/licensed_music/track124.mp3"])
scene ep9_sage_dance2 with dissolve
mc "Found you."
scene ep9_sage_dance3 with dissolve
sa "Dammit. I need to hide better from you."
scene ep9_sage_dance4 with dissolve
mc "That wouldn't work; I'd still find you."
scene ep9_sage_dance3 with dissolve
sa "What if I hide well? In a place where you'd never look?"
scene ep9_sage_dance4 with dissolve
mc "Simple, I'd look for the place I'd never look and find you."
scene ep9_sage_dance5 with dissolve
sa "Finally, you're drunk! Because that didn't make any sense."
sa "Dance with me."
scene ep9_sage_dance6 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
menu:
    "Pick her up":
        scene ep9_sage_dance7 with dissolve
        sa "Whoa! Haha!"
        sa "Are you showing everyone how strong you are?"
        scene ep9_sage_dance8 with dissolve
        mc "I'm dressed as a warrior; this is the way to do it."
        scene ep9_sage_dance9 with dissolve
        sa "Definitely makes sense if you ask me."
        scene ep9_sage_dance10 with dissolve
        sa "Haha! You're not letting me down, are you?"
        mc "I can hold you like this forever."
    "Get down low":
        scene ep9_sage_dance11 with dissolve
        sa "Haha! What are you doing down there?"
        scene ep9_sage_dance12 with dissolve
        mc "I go where the music takes me."
        scene ep9_sage_dance13 with dissolve
        sa "Pff! You're only looking for a reason to peek up my skirt. I see you."
        scene ep9_sage_dance12 with dissolve
        mc "I didn't think about that, but that's brilliant!"
        scene ep9_sage_dance14 with dissolve
        sa "Well? How about it?"
        scene ep9_sage_dance15 with dissolve
        mc "I'm never coming back up; I'm gonna stay down here forever."
        scene ep9_sage_dance16 with vpunch
        mc "Ow! Or until people start stepping on me, I guess."
scene ep9_sage_dance17 with dissolve
$ renpy.pause()
scene ep9_sage_dance18 with dissolve
menu:
    "Kiss her gently":
        scene ep9_sage_dance19 with dissolve
        $ renpy.pause()
        scene ep9_sage_dance20 with dissolve
        $ renpy.pause()
        scene ep9_sage_dance21 with dissolve
        sa "How can you make me feel fuzzy and horny at the same time?"
    "Wait and see what she does":
        scene ep9_sage_dance22 with dissolve
        sa "You stopped dancing."
        scene ep9_sage_dance23 with dissolve
        mc "So did you."
        scene ep9_sage_dance21 with dissolve
        sa "I'm waiting for you to kiss me."
        scene ep9_sage_dance23 with dissolve
        mc "Haha, well, so was I."
        scene ep9_sage_dance19 with dissolve
        $ renpy.pause()
        scene ep9_sage_dance20 with dissolve
        $ renpy.pause()
    "Grab her ass":
        scene anim_sage_grab_ep9 with dissolve
        $ renpy.pause()
        scene ep9_sage_dance22 with dissolve
        sa "You're always horny, aren't you?"
        scene ep9_sage_dance23 with dissolve
        mc "With you, I am."
        scene ep9_sage_dance24 with dissolve
        $ renpy.pause()
label ep9_sage_dance_loop_label:
menu:
    "Dance more":
        scene ep9_sage_dance6 with dissolve
        $ renpy.pause(13)
        show screen click_to_continue_screen with dissolve
        $ renpy.pause(2)
        hide screen click_to_continue_screen with dissolve
        $ renpy.pause()
        jump ep9_sage_dance_loop_label
    "Leave":
        scene ep9_sage_dance18 with dissolve
        mc "I need a break."
        scene ep9_sage_dance25 with dissolve
        sa "You may look strong, but your endurance is shit."
        scene ep9_sage_dance27 with dissolve
        mc "I'm saving myself for you later."
        scene ep9_sage_dance26 with dissolve
        sa "You're gonna need some kind of a sports drink. Just saying!"
        
if wt_ep9_branch_numbers > 1:
    $ task_list[3] = task_list[3].replace("\n Dance with Sage (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("\n Dance with Sage", "")
    $ task_list[3] = task_list[3].replace("Dance with Sage (Tommy's room)", "")
    $ task_list[3] = task_list[3].replace("Dance with Sage", "")
else:
    $ task_list[3] = ""
if task_list[3] == " ":
    $ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_jill_talk_label:
$ guideSuggestedPage = 64
if ep9_jill_mood == 0 or ep9_jill_mood == 2:
    scene ep9_jill_talk1 with dissolve
    mc "I almost didn't recognize you."
    scene ep9_jill_talk2 with dissolve
    ji "You didn't?"
    scene ep9_jill_talk3 with dissolve
    mc "Yeah, I don't know if it's the mask, the outfit...or maybe both?"
    scene ep9_jill_talk4 with dissolve
    ji "It's not me...is it?"
    scene ep9_jill_talk18 with dissolve
    bia "Oh, boy. Here we go..."
    scene ep9_jill_talk5 with dissolve
    menu:
        "It suits you":
            mc "It's a great costume. It suits you!"
            scene ep9_jill_talk19 with dissolve
            bia "Hah! Told you."
            scene ep9_jill_talk5 with dissolve
            mc "What? You don't like it?"
            scene ep9_jill_talk4 with dissolve
            ji "I do like it."
            scene ep9_jill_talk5 with dissolve
            mc "But?"
            scene ep9_jill_talk4 with dissolve
            ji "No but."
            scene ep9_jill_talk18 with dissolve
            bia "A big but. And surprisingly, the big but is her big butt."
            scene ep9_jill_talk6 with dissolve
            ji "Bianca!"
            scene ep9_jill_talk18 with dissolve
            bia "Jill is self-conscious. It's nothing new; she's always been this way."
            scene ep9_jill_talk7 with dissolve
            ji "Yeah, yeah. I'm wearing the costume. So, get off my case."
            scene ep9_jill_talk18 with dissolve
            bia "Not until you admit you look amazing in it."
            scene ep9_jill_talk7 with dissolve
            ji "Not happening tonight. Maybe in ten years."
            scene ep9_jill_talk18 with dissolve
            bia "Classic Jill."
        "Totally not you":
            mc "No, it's not you. Not one bit."
            scene ep9_jill_talk7 with dissolve
            ji "See?"
            scene ep9_jill_talk18 with dissolve
            bia "Big whoop? Halloween is all about not being yourself. So, you're nailing it."
            scene ep9_jill_talk5 with dissolve
            mc "That you are. It is a great-looking costume - no need to feel uncomfortable about it."
            scene ep9_jill_talk4 with dissolve
            ji "I'm not uncomfortable; I tend to overanalyze things."
            scene ep9_jill_talk18 with dissolve
            bia "Jill is self-conscious. It's nothing new; she's always been this way."
    if ep8_jill_state != 1:
        scene ep9_jill_talk20 with dissolve
        mc "Sorry...but you are...?"
        scene ep9_jill_talk21 with dissolve
        bia "Oh! I'm Bianca. A close friend."
        bia "And that was Olivia, who just left."
        scene ep9_jill_talk20 with dissolve
        if affinity == "DIK":
            mc "Cool! I'm [name]."
        else:
            mc "Nice to meet you. I'm [name]."
        if not ep8_recital_failed:
            scene ep9_jill_talk21 with dissolve
            bia "Oh, we know who you are. We were at the recital."
            bia "You're amazing!"
            scene ep9_jill_talk20 with dissolve
            mc "Oh? Thanks so much."
        else:
            scene ep9_jill_talk21 with dissolve
            bia "Yeah, I've heard about you."
    scene ep9_jill_talk5 with dissolve
    if affinity == "DIK":
        mc "I don't wanna sound like a complete dick, but who invited you?"
    else:
        mc "I don't wanna sound mean, but who invited you?"
    scene ep9_jill_talk8 with dissolve
    ji "Josy did."
    scene ep9_jill_talk5 with dissolve
    mc "I see. I would have invited you if I thought you wanted to come. Should I feel bad about that?"
    scene ep9_jill_talk8 with dissolve
    ji "I think I understand why you didn't... If things were normal, I would have declined anyway."
    scene ep9_jill_talk5 with dissolve
    mc "Oh?"
    scene ep9_jill_talk8 with dissolve
    ji "I meant I'm usually attending High Society Halloween. It's an Alpha Nu Omega party."
    scene ep9_jill_talk18 with dissolve
    bia "Even the name of it sounds crap."
    scene ep9_jill_talk4 with dissolve
    ji "Well, regardless, I'm here tonight."
    scene ep9_jill_talk5 with dissolve
    mc "You made the right call."
    if ep9_jill_mood == 2:
        scene ep9_jill_talk9 with dissolve
        mc "I... I hope you've been doing all right since...you know."
        scene ep9_jill_talk10 with dissolve
        ji "Mhm... Thanks."
        scene ep9_jill_talk9 with dissolve
    mc "Enjoy the party! I'll see you girls around."
    if ep8_jill_rejected_you:
        scene ep9_jill_talk22 with dissolve
        bia "So, if you don't want him, he's up for grabs?"
        scene ep9_jill_talk23 with dissolve
        ji "Haha! Bianca! Would you say that in front of Matthew?"
        scene ep9_jill_talk22 with dissolve
        bia "I'm joking! But some guys make you wish you were single."
        bia "And at the moment I can't believe that you said no to him. What's wrong with you?"
    elif ep8_jill_state != 1:
        scene ep9_jill_talk22 with dissolve
        if not ep8_recital_failed:
            bia "He's even hotter up front than on stage."
        else:
            bia "You didn't tell me how hot he was."
        scene ep9_jill_talk23 with dissolve
        ji "Haha! Bianca! Would you say that in front of Matthew?"
        scene ep9_jill_talk22 with dissolve
        bia "I'm just saying! Some guys make you wish you were single."
    $ new_bio("Jill", "Jill came to our Halloween party. I had a friendly talk with her and her friend, Bianca.")
else:
    scene ep9_jill_talk1b with dissolve
    mc "Hey... Welcome to our party."
    scene ep9_jill_talk11 with dissolve
    ji "Hi."
    scene ep9_jill_talk12 with dissolve
    ji "Um, Bianca?"
    scene ep9_jill_talk27 with dissolve
    bia "Yeah. Liv? Over here."
    scene ep9_jill_talk13 with dissolve
    mc "I'm surprised to see you here."
    scene ep9_jill_talk11 with dissolve
    ji "Josy invited me. I hope it's fine."
    scene ep9_jill_talk13 with dissolve
    mc "Of course. Uh... I would have invited you if I only knew you'd come."
    scene ep9_jill_talk11 with dissolve
    ji "It was either this or spending the night at a party with Tybalt, so..."
    scene ep9_jill_talk13 with dissolve
    mc "Haha... You made the right call."
    mc "How have you been?"
    scene ep9_jill_talk14 with dissolve
    ji "..."
    mc "Too soon?"
    scene ep9_jill_talk15 with dissolve
    $ renpy.pause()
    scene ep9_jill_talk16 with dissolve
    ji "It's...hard."
    scene ep9_jill_talk15 with dissolve
    mc "Yeah..."
    mc "For me too."
    scene ep9_jill_talk16 with dissolve
    ji "Is it?"
    scene ep9_jill_talk15 with dissolve
    mc "Yeah. I wish I could go back and undo things I've done. But I can't."
    scene ep9_jill_talk17 with dissolve
    mc "I'll get out of your hair. I hope you can enjoy yourself tonight. And I'm happy you're here."
    mc "Maybe..."
    mc "Maybe someday, when this isn't feeling like a fresh wound, we can...talk or something?"
    scene ep9_jill_talk16 with dissolve
    ji "Thanks..."
    scene ep9_jill_talk15 with dissolve
    mc "Try the punch. I hear it's great, but a bit strong."
    scene ep9_jill_talk24 with dissolve
    bia "That was...awkward."
    scene ep9_jill_talk25 with dissolve
    ji "It went better than I thought it would. At least I'm not crying..."
    scene ep9_jill_talk24 with dissolve
    bia "Yeah? Do you regret coming here?"
    scene ep9_jill_talk25 with dissolve
    ji "No. This will be good for me."
    scene ep9_jill_talk26 with dissolve
    bia "I couldn't agree more! Let's try that punch."
    $ new_bio("Jill", "Jill came to our Halloween party with her friends. I made an effort to talk with her. It was a bit awkward, but I'm glad I did it.")
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep9_quinn_talk_label:
scene ep9_quinn_talk7 with dissolve
$ renpy.pause()
scene ep9_quinn_talk8 with dissolve
qu "This punch is awful."
scene ep9_quinn_talk9 with dissolve
mc "There's more liquor in the kitchen if you wanna make yourself something."
scene ep9_quinn_talk8 with dissolve
qu "Show me."
scene ep9_quinn_talk31 with dissolve
mc "What do you want?"
scene ep9_quinn_talk32 with dissolve
qu "Is that rum?"
scene ep9_quinn_talk33 with dissolve
mc "Yeah. Here you go."
scene ep9_quinn_talk34 with dissolve
qu "It seems like plans changed with the party, or am I wrong?"
scene ep9_quinn_talk35 with dissolve
mc "A bit, yeah. I asked the DIKs for help and Tommy wanted some things done his way."
mc "I checked with Sage and she said the changes were fine."
scene ep9_quinn_talk36 with dissolve
qu "..."
scene ep9_quinn_talk35 with dissolve
mc "But you're obviously not cool with it."
scene ep9_quinn_talk37 with dissolve
qu "Do whatever you want with your party. But I think it's bullshit we sit down and plan with you if you're gonna change everything."
scene ep9_quinn_talk35 with dissolve
mc "We didn't change everything. Tommy had some ideas for it and I couldn't go over his head with it since he's been in charge of parties in the past."
scene ep9_quinn_talk38 with dissolve
qu "..."
scene ep9_quinn_talk39 with dissolve
mc "Don't you think it's time to bury the hatchet with him?"
scene ep9_quinn_talk41 with dissolve
qu "Why do you care?"
scene ep9_quinn_talk39 with dissolve
mc "Because it's affecting all of us and causing stupid arguments, like this one right now."
mc "Sometimes it feels like it's going to end with the DIKs and HOTs splitting up."
scene ep9_quinn_talk41 with dissolve
qu "You're exaggerating. It's not that bad."
scene ep9_quinn_talk39 with dissolve
mc "That's how Tommy talks about it at times."
mc "He once said the DIKs could go back to the roots, partying without the HOTs."
mc "And I guess that means you'd be back partying with the alphas. Traditions and all."
scene ep9_quinn_talk41 with dissolve
qu "Fuck those stupid traditions. I'm not going back to partying with the alphas."
scene ep9_quinn_talk40 with dissolve
mc "Haha, right? Fuck 'em!"
scene ep9_quinn_talk42 with dissolve
qu "Yeah. Fuck 'em!"


if not branchAlone and ep8_quinn_lewd:
    scene ep9_quinn_talk45 with dissolve
    jump ep9_skipq_label
if ep8_quinn_lewd:
    scene ep9_quinn_talk43 with dissolve
    $ renpy.pause()
    scene ep9_quinn_talk45 with dissolve
elif not ep6_quinn_lewd:
    scene ep9_quinn_talk40 with dissolve
    mc "Maybe I'm wrong, but I think that's the first time we see eye to eye on something."
    scene ep9_quinn_talk41 with dissolve
    qu "Even so, I still think you're a giant pussy."
    scene ep9_quinn_talk40 with dissolve
    if affinity == "DIK":
        mc "Yeah? Fuck you, too."
    else:
        mc "Agree to disagree on that one."
    scene ep9_quinn_talk43 with dissolve
    $ renpy.pause()
    scene ep9_quinn_talk45 with dissolve
elif ep8_quinn_rejected_you:
    scene ep9_quinn_talk39 with dissolve
    mc "Are you still pissed with me?"
    scene ep9_quinn_talk41 with dissolve
    qu "For what?"
    scene ep9_quinn_talk39 with dissolve
    mc "You know for what. That I'm dating others."
    mc "Sorry if that hurt you."
    scene ep9_quinn_talk44 with dissolve
    qu "Hurt me? Get over yourself. I was only using you."
    qu "Go ahead and stick your dick into any hole you want. See if I care."
    scene ep9_quinn_talk45 with dissolve
    mc "All right... So, um..."
else:
    scene ep9_quinn_talk45 with dissolve

label ep9_skipq_label:
mc "How did you solve the problem with the alphas, by the way? I'd imagine they wouldn't take no for an answer."
stop music fadeout 3
scene ep9_quinn_talk46 with dissolve
qu "Sometimes... two problems become a solution."

scene ep9_quinn_talk60
play music "music/ep8/licensed_music/track78.mp3"
ar "It's like super-important that I do this now, or I probably won't ever get to do it."
scene ep9_quinn_talk66 with dissolve
qu "Why do you think we're carving pumpkins? We already have Halloween covered."
qu "And I don't know where you got this idea from; you'd never get to do it. No one promised you this."
scene ep9_quinn_talk61 with dissolve
ar "It's so unfair! I have like six years left of college, and soon, it's all going to be over."
ar "I wanted to travel around the world, learn how to fish and see Wisconsin. None of that is going to happen now."
scene ep9_quinn_talk63 with dissolve
qu "What the fuck are you on about?"
scene ep9_quinn_talk61 with dissolve
ar "Elena talked about how she got these period cramps the other week, and I told her I don't get those anymore."
scene ep9_quinn_talk63 with dissolve
qu "Cramps?"
scene ep9_quinn_talk60 with dissolve
ar "No! Periods."
ar "I was like super-irregular when I took the pill but then they stopped altogether."
ar "And then I thought I was getting fatter, but as it turns out, I'm pregnant!"
scene ep9_quinn_talk55 with dissolve
qu "You're pregnant?"
scene ep9_quinn_talk60 with dissolve
ar "I have no clue how it happened!"
scene ep9_quinn_talk55 with dissolve
qu "How...many are you sleeping with right now, again?"
scene ep9_quinn_talk61 with dissolve
ar "Not that many. Just a few."
scene ep9_quinn_talk62 with dissolve
ar "How many are three per week?"
scene ep9_quinn_talk59 with dissolve
qu "Unprotected?"
scene ep9_quinn_talk60 with dissolve
ar "I'm not an idiot! I'm on the pill. Duh-doy!"
ar "I've been eating Dawe's pills for at least a year now."
scene ep9_quinn_talk56 with dissolve
qu "Wait... Dawe's pills? His birth control pills?"
scene ep9_quinn_talk60 with dissolve
ar "Yeah. He uses them to grow bigger."
scene ep9_quinn_talk55 with dissolve
qu "Oh, boy..."
scene ep9_quinn_talk61 with dissolve
ar "So, now I'm gonna have to learn how to paint, weld and drive a car before the baby comes. There's so little time!"
scene ep9_quinn_talk57 with dissolve
qu "..."
scene ep9_quinn_talk61 with dissolve
ar "Say something!"
scene ep9_quinn_talk58 with dissolve
qu "I don't know where to begin or what question is relevant."
scene ep9_quinn_talk64 with dissolve
ar "Can I plan the party or not? I have these amazing ideas, like, renting a bus."
scene ep9_quinn_talk65
if not persistent.ep9_cardji12:
    show screen ep9_render_screen("ji12")
with dissolve
qu "What? A bus?"
stop music fadeout 3
scene ep9_quinn_talk64
hide screen ep9_render_screen
with dissolve
ar "For the road trip! Duh!"

$ mphone_next_song()
scene ep9_quinn_talk45
mc "She's pregnant!?"
scene ep9_quinn_talk47 with dissolve
qu "Apparently so. Total shocker."
scene ep9_quinn_talk45 with dissolve
mc "Damn..."
mc "So, what did you end up doing?"
scene ep9_quinn_talk46 with dissolve
qu "Like I said. Two problems became a solution."

$ renpy.sound.set_volume(0,channel='music')
$ renpy.music.play("music/ep4/fluffing_a_duck.mp3", channel="music2")
scene ep9_quinn_talk67
ar "Who's excited about Halloween!?"
scene ep9_quinn_talk68 with dissolve
jcs "*{i}Cheers{/i}*"
scene ep9_quinn_talk69 with dissolve
jy "Where are we going again?"
scene ep9_quinn_talk70 with dissolve
al "Dunno. It's some kind of a surprise."
scene ep9_quinn_talk72 with dissolve
jo "Ashley? Will the rest of the HOTs meet us there when we arrive or what?"
scene ep9_quinn_talk73 with dissolve
ash "No? This is something Arieth wanted us to do."
ash "I'm just tagging along to show support. Plus, Ant's here, so..."
scene ep9_quinn_talk71
dw "Arieth!? Where are we going!?"
$ renpy.music.stop(channel="music2", fadeout=0)
$ renpy.sound.set_volume(1.0,channel='music')
scene ep9_quinn_talk47
qu "Trust me. They won't be a problem tonight."
scene ep9_quinn_talk45 with dissolve
mc "You sure know how to get things done."
$ new_bio("Quinn", "Quinn fooled the tri-alphas at Halloween by using Arieth.")
$ new_bio("Arieth", "Quinn told me that Arieth is pregnant.")

if not branchAlone and ep8_quinn_lewd:
    scene ep9_quinn_talk48 with dissolve
    qu "So... Have you turned gay or what?"
    scene ep9_quinn_talk49 with dissolve
    mc "What?"
    scene ep9_quinn_talk48 with dissolve
    qu "You're usually a pervert around me and now you're not even looking at my tits."
    scene ep9_quinn_talk49 with dissolve
    mc "I want to, but..."
    mc "I'm kind of seeing someone else, so..."
    scene ep9_quinn_talk48 with dissolve
    qu "Hold up... You got a relationship?"
    scene ep9_quinn_talk49 with dissolve
    if branchSage:
        mc "Yeah. Sage and I are dating, I guess you could say."
    else:
        mc "Yeah."
    scene ep9_quinn_talk50 with dissolve
    qu "Whatever."
    scene ep9_quinn_talk51 with dissolve
    if affinity == "DIK":
        mc "Are you ok? I know you and I got pretty close, but..."
        scene ep9_quinn_talk50 with dissolve
        qu "Get over yourself. I was only using you for sex."
    else:
        mc "I...hope that doesn't hurt you. We got pretty close, you and me."
        scene ep9_quinn_talk50 with dissolve
        qu "Hurt me? Get over yourself. I was only using you for sex."
    qu "You're an ok fuck, but that's all you were to me."
    qu "Go ahead and stick your dick into any hole you want. See if I care."
    scene ep9_quinn_talk52 with dissolve
    mc "All right..."
    $ task_list[8] = ""
    $ updateTaskList()
    $ new_bio("Quinn", "I told Quinn that I was dating someone, and she got mad. She said she only cared about sex when it came to me.")
    jump endEvent

if ep8_quinn_lewd:
    scene ep9_quinn_talk54 with dissolve
    qu "Thanks for showing me the stash. I'll probably raid it again later."
    $ event_list.append("ep9_diks_ph2_qpic_event_label")
    if persistent.mod_wtenabled:
        $ optional_task_list[1] = "Take a picture with Quinn (Main party room)"
    else:
        $ optional_task_list[1] = "Take a picture with Quinn"
else:
    scene ep9_quinn_talk53 with dissolve
    qu "Thanks for showing me the stash. I'll probably raid it again later."
$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_qpic_event_label:
scene ep9_quinn_talk1 with dissolve
mc "Wanna go take a picture together?"
scene ep9_quinn_talk2 with dissolve
qu "Why would I?"
scene ep9_quinn_talk3 with dissolve
mc "It's Elena's and Jacob's idea. It's like a photo booth in my room."
mc "Guests can have their pictures taken to remember the night or something."
scene ep9_quinn_talk4 with dissolve
qu "Look at you. You're just finding a way to get me back to your place."
scene ep9_quinn_talk6 with dissolve
mc "With a body looking like that, of course, I am."
scene ep9_quinn_talk5 with dissolve
qu "Let's snap some pervy pictures, then."
scene ep9_quinn_talk6b with dissolve
qu "What a setup."
scene ep9_quinn_talk7b with dissolve
mc "Ambitious, huh?"
scene ep9_quinn_talk8b with dissolve
qu "Ambitious? Is it a photo studio or a porn studio? Damn, you could record some high-quality nasties with this."
scene ep9_quinn_talk9b with dissolve
mc "You got me!"
scene ep9_quinn_talk8b with dissolve
qu "Oh, really? What's the vid gonna be? You jacking off in front of a green screen?"
scene ep9_quinn_talk9b with dissolve
mc "Yeah, and then I change the background to a field with flowers and profit."
scene ep9_quinn_talk10 with dissolve
qu "Hahaha!"
mc "Strike a pose for me."
scene ep9_quinn_talk11 with dissolve
qu "Let me prepare first."
scene ep9_quinn_talk12 with dissolve
mc "Awesome!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_quinn_talk12 with dissolve
$ renpy.pause(0.5)

scene ep9_quinn_talk19 with dissolve
mc "These aren't private photos. I don't know if that makes you rethink anything or not."
scene ep9_quinn_talk20 with dissolve
qu "I was thinking you could cover me up."
scene ep9_quinn_talk19 with dissolve
menu:
    "Hold her tits":
        $ ep9_photos[7] = True
        scene ep9_quinn_talk14 with dissolve
        qu "You're ok with people seeing these?"
        scene ep9_quinn_talk15 with dissolve
        mc "If I didn't think about that already, I'd do something more than hold your tits right now."
        scene ep9_quinn_talk14 with dissolve
        qu "So, it is a porn studio, after all?"
        scene ep9_quinn_talk13 with dissolve
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_quinn_talk13 with dissolve
        $ renpy.pause()
    "Funny picture":
        $ ep9_photos[8] = True
        scene ep9_quinn_talk17 with dissolve
        qu "You don't take hints, do you?"
        scene ep9_quinn_talk18 with dissolve
        mc "I do, but I couldn't pass up on this opportunity."
        scene ep9_quinn_talk16 with dissolve
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_quinn_talk16 with dissolve
        $ renpy.pause()
scene ep9_quinn_talk21 with dissolve
qu "So, are we done here?"
scene ep9_quinn_talk22 with dissolve
mc "Almost..."
menu:
    "Grab her ass":
        scene ep9_quinn_talk23 with dissolve
        qu "What are you doing?"
        mc "Your outfit's too hot. I don't want it to go to waste."
    "Lick her tits":
        scene ep9_quinn_talk24 with dissolve
        qu "What are you doing?"
        scene ep9_quinn_talk25 with dissolve
        mc "*{i}Suck suck{/i}* Your outfit's too hot. I don't want it to go to waste."
qu "My outfit, huh?"
scene ep9_quinn_talk26 with dissolve
qu "How badly do you wanna fuck me?"
scene ep9_quinn_talk27 with dissolve
mc "I'd walk out of the party right now for it."
scene ep9_quinn_talk26 with dissolve
qu "I got you where I want, then. My succubus powers work."
scene ep9_quinn_talk28 with dissolve
mc "Are you gonna leave me hanging?"
scene ep9_quinn_talk29 with dissolve
qu "I think you're warmed up to shoot that porno video of yours."
qu "Start jacking it, [mc_quinn]."
scene ep9_quinn_talk30 with dissolve
mc "Hngn..."
$ optional_task_list[1] = ""
$ updateTaskList()
$ new_bio("Quinn", "I took a picture together with Quinn at the Halloween party.")
jump endEvent

label ep9_diks_ph2_rusty_event_label:
scene ep9_diks_ph2_rusty_event1 with dissolve
rs "Do you want another drink?"
scene ep9_diks_ph2_rusty_event4 with dissolve
mic "I shouldn't. I'm already way too tipsy."
scene ep9_diks_ph2_rusty_event2 with dissolve
rs "Yeah? Are you getting drunk?"
scene ep9_diks_ph2_rusty_event5 with dissolve
mic "Pretty much! I even think I saw double before."
scene ep9_diks_ph2_rusty_event2 with dissolve
rs "There are three nurses at this party, so odds are you did."
scene ep9_diks_ph2_rusty_event5 with dissolve
mic "I should take it slow."
scene ep9_diks_ph2_rusty_event6 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_rusty_event7 with dissolve
mic "Um... Rusty?"
mic "Sorry, I... Damn it."
mic "Rusty, I really like you and all, but..."
mic "I'm kind of in a relationship."
scene ep9_diks_ph2_rusty_event3 with dissolve
rs "Kind of, or am?"
scene ep9_diks_ph2_rusty_event8 with dissolve
mic "Am. I got back together with my ex recently..."
scene ep9_diks_ph2_rusty_event3 with dissolve
rs "Why haven't you mentioned that to me?"
scene ep9_diks_ph2_rusty_event8 with dissolve
mic "It's not been the best between us for quite some time. We've been on and off..."
mic "*{i}Sigh{/i}* You've always been so nice and flirty around me and I liked it."
mic "Flirting is harmless."
scene ep9_diks_ph2_rusty_event3 with dissolve
rs "We had sex..."
scene ep9_diks_ph2_rusty_event9 with dissolve
mic "Yeah, we did, but it feels wrong now."
mic "I'm so sorry, Rusty. I can't do this to him. I want to make it work, this time."
scene ep9_diks_ph2_rusty_event10 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_rusty_event11 with dissolve
rs "..."
$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_food_event_label:
scene ep9_diks_ph2_food_event1 with dissolve
mc "(Guests have been eating a lot. I didn't think they would eat this much...)"
mc "(I should put out more cakes. I'll check the fridge for some.)"
$ event_list.append("ep9_diks_ph2_food2_event_label")
jump endEvent

label ep9_diks_ph2_food2_event_label:
scene ep9_diks_ph2_food2_event1 with dissolve
mc "(We still have plenty of muffins and cakes in here. I'll bring some extra for the table.)"
$ event_list.append("ep9_diks_ph2_food3_event_label")
jump endEvent

label ep9_diks_ph2_food3_event_label:
$ ep9_restocked_food = True
scene ep9_diks_ph2_food3_event1 with dissolve
mc "(There we go. I hope it will last longer than it did so far.)"
$ RPdiks += 1
$ optional_task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_sarah_event_label:
scene ep9_diks_ph2_sarah_event1 with dissolve
mc "What's this? You're not drinking?"
scene ep9_diks_ph2_sarah_event2 with dissolve
sar "Neither are you! I just finished my beer; what's your excuse?"
scene ep9_diks_ph2_sarah_event1 with dissolve
mc "I've got no excuse. I'll grab something soon. Did you try the punch?"
scene ep9_diks_ph2_sarah_event2 with dissolve
sar "Not yet."
scene ep9_diks_ph2_sarah_event1 with dissolve
menu:
    "[mod_gr]Offer to get her some":
        scene ep9_diks_ph2_sarah_event3 with dissolve
        mc "Let me bring you some."
        scene ep9_diks_ph2_sarah_event4 with dissolve
        sar "Sure. Let's see if it beats the punch at the dorm party."
        $ event_list.append("ep9_diks_ph2_sarah2_event_label")
        if persistent.mod_wtenabled:
            $ optional_task_list[4] = "Find punch for Sarah (Right hallway)"
        else:
            $ optional_task_list[4] = "Find punch for Sarah"
    "Tell her where it is":
        mc "It's downstairs on a table in the hallway if you're interested."
        scene ep9_diks_ph2_sarah_event2 with dissolve
        sar "Thanks, [name]."
        $ optional_task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_sarah2_event_label:
scene ep9_diks_ph2_sarah2_event1 with dissolve
mc "(Some punch for Sarah...)"
$ event_list.append("ep9_diks_ph2_sarah3_event_label")
if persistent.mod_wtenabled:
        $ optional_task_list[4] = "Bring punch to Sarah (Upper Main Room)"
else:
        $ optional_task_list[4] = "Bring punch to Sarah"

$ updateTaskList()
jump endEvent

label ep9_diks_ph2_sarah3_event_label:
$ ep9_sarah_punch = True
scene ep9_diks_ph2_sarah3_event1 with dissolve
mc "Here's your punch."
scene ep9_diks_ph2_sarah3_event2 with dissolve
sar "Cheers!"
scene ep9_diks_ph2_sarah3_event3 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_sarah3_event4 with dissolve
sar "Oof. How much alcohol is there in this one?"
scene ep9_diks_ph2_sarah3_event5 with dissolve
mc "Um. Not too much."
scene ep9_diks_ph2_sarah3_event8 with dissolve
sar "Am I crazy? It's stronger than mouthwash. Taste this."
scene ep9_diks_ph2_sarah3_event9 with dissolve
mc "Yeah, you're not kidding. That's pretty strong."
scene ep9_diks_ph2_sarah3_event6 with dissolve
sar "Thanks for the drink, [name]. You're such a nice DIK."
scene ep9_diks_ph2_sarah3_event7 with dissolve
menu:
    "[mod_gr]Take a picture together":
        jump ep9_diks_ph2_photo_sarah_mel_event_label
    "Leave":
        mc "Any time!"
        $ optional_task_list[4] = ""
        $ updateTaskList()
        jump endEvent

label ep9_diks_ph2_camila_dance_event_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ affinity = "DIK"
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track130.mp3"])
    show screen dance_filter_screen
scene ep9_diks_ph2_camila_dance_event1 with dissolve
mc "(I feel so stupid dancing... I'm not drunk enough to do this.)"
scene ep9_diks_ph2_camila_dance_event2 with dissolve
cam "Nice moves, [name]."
mc "Yeah, right."
menu:
    "[mod_gr]Dance with Camila":
        scene ep9_diks_ph2_camila_dance_event3 with dissolve
        mc "You, however..."
    "Leave" if not _in_replay:
        mc "(Nah. Maybe I'll dance later.)"
        $ optional_task_list[0] = ""
        $ updateTaskList()
        jump endEvent
scene ep9_diks_ph2_camila_dance_event4 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
scene ep9_diks_ph2_camila_dance_event5 with dissolve
cam "Careful, so you don't poke me with that sword."
scene ep9_diks_ph2_camila_dance_event6 with dissolve
mc "Don't worry about it. It's a flimsy and soft sword."
scene ep9_diks_ph2_camila_dance_event7 with dissolve
cam "What about that sword?"
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Camila scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        
                        
                        
            
menu:
    "Stop her" if not _in_replay:
        scene ep9_diks_ph2_camila_dance_event8 with dissolve
        mc "Haha! Don't worry about that, either. It's also soft right now."
        scene ep9_diks_ph2_camila_dance_event4 with dissolve
        $ renpy.pause()
        $ optional_task_list[0] = ""
        $ updateTaskList()
        jump endEvent
    "Tease her [mod_gr][mod_choices[0]]":
        $ ep9_camila_lewd = True
        hide screen new_phone_screen
        scene ep9_diks_ph2_camila_dance_event10 with dissolve
        mc "I can't make any promises about that sword. But it's blunter and heavier than it is sharp."
        scene ep9_diks_ph2_camila_dance_event9 with dissolve
        $ renpy.pause()
        scene anim_camila_dance_ep9 with dissolve
        cam "You seem to be right about that."
        cam "Do you like this?"
        mc "Who wouldn't?"
        cam "Do you think people can tell I'm grinding against your dick?"
        mc "Yeah, if they look our way, they can. But it's no worse than how they're dancing, right?"
        pause
        scene ep9_diks_ph2_camila_dance_event11 with dissolve
        cam "Let's dance over here..."
        scene ep9_diks_ph2_camila_dance_event12 with dissolve
        mc "You call this dancing?"
        scene ep9_diks_ph2_camila_dance_event13 with dissolve
        cam "What would you call it?"
        mc "Foreplay?"
        scene ep9_diks_ph2_camila_dance_event14 with dissolve
        cam "Haha! I don't think so."
        mc "It's not?"
        scene ep9_diks_ph2_camila_dance_event15 with dissolve
        cam "I'm not gonna have sex on the dance floor. I'm not Sarah."
        if affinity == "DIK":
            scene ep9_diks_ph2_camila_dance_event18 with dissolve
            mc "Is it ok if I have it?"
            cam "God... You didn't..."
            mc "This costume is convenient."
            scene ep9_diks_ph2_camila_dance_event15 with dissolve
            cam "My costume is...convenient, too."
            cam "Put it under my skirt. But be discreet..."
        else:
            scene ep9_diks_ph2_camila_dance_event16 with dissolve
            mc "Yeah, that would be a bad idea."
            scene ep9_diks_ph2_camila_dance_event17 with dissolve
            cam "It's very hard. You should do something about that."
            mc "Any suggestion?"
            scene ep9_diks_ph2_camila_dance_event15 with dissolve
            cam "I guess it wouldn't be the worst thing if you...put it under my skirt. But be discreet..."
        scene ep9_diks_ph2_camila_dance_event19 with dissolve
        cam "Dammit... I'm becoming someone like Sarah..."
        mc "You say that like it's a bad thing."
        scene anim_camila_dance2_ep9 with dissolve
        cam "I keep pushing limits. I don't know where I'll end up at this rate."
        mc "It's a first for me too - we're dance floor virgins."
        pause
        scene ep9_diks_ph2_camila_dance_event20 with dissolve
        cam "You might as well go all the way by now..."
        scene ep9_diks_ph2_camila_dance_event21 with dissolve
        mc "Are you sure?"
        scene ep9_diks_ph2_camila_dance_event20 with dissolve
        cam "Use my asshole... But go slow."
        scene ep9_diks_ph2_camila_dance_event22 with dissolve
        cam "Hngnn..."
        scene ep9_diks_ph2_camila_dance_event23 with dissolve
        cam "We're really doing this?"
        mc "Fuck yes, we are."
        scene anim_camila_dance3_ep9 with dissolve
        mc "Damn... This...{i}song{/i} is good."
        cam "Yeah... The beat...is awesome... Move to it."
        pause
        scene anim_camila_dance4_ep9 with dissolve
        mc "Such a tight...beat. Fuck, it's good."
        mc "Though, I feel... This is gonna be a short song."
        cam "It's over...soon, huh?"
        pause
        scene anim_camila_dance5_ep9 with dissolve
        mc "We're reaching the outro any second now."
        cam "Inside... Ok?"
        mc "Yeah..."
        pause
        scene anim_camila_dance3_ep9 with dissolve
        mc "I'm...coming..."
        pause
        scene ep9_diks_ph2_camila_dance_event24 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_camila_dance_event24 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_camila_dance_event24 at vpunch, cum1
        $ renpy.pause()
        scene ep9_diks_ph2_camila_dance_event25 with dissolve
        cam "*{i}Phew{/i}* Some bust a move, and you bust a nut."
        mc "Haha! Damn right."
        scene ep9_diks_ph2_camila_dance_event26 with dissolve
        cam "Excuse me. I'm gonna make an awkward walk to the bathroom now."
        scene ep9_diks_ph2_camila_dance_event27 with dissolve
        $ renpy.pause()
        if _in_replay:
            hide screen dance_filter_screen
        $ renpy.end_replay()
        $ persistent.ep9_lewd_camila = True
        $ calcScenes()
        $ new_bio("Camila", "I had sex with Camila on the dance floor at the Halloween party.")
        $ mphone_stats_add_girl_s3("camila","You had sex with Camila on the dance floor in episode 9.")
        if not persistent.ep9_card1:
            $ persistent.ep9_card1 = True
            $ persistent.rew_2d_unlocked += 1
            $ persistent.chat_new_rewards = True
            $ calcRenders()
        show screen new_phone_screen
$ optional_task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_dcam_event_label:
$ guideSuggestedPage = 65
$ event_list.append("ep9_diks_ph2_photo_camila_event_label")
scene ep9_diks_ph2_dcam_event1 with dissolve
de "And then she said that I-"
scene ep9_diks_ph2_dcam_event2 with dissolve
cam "Sorry, but I need to use the restroom."
scene ep9_diks_ph2_dcam_event3 with dissolve
de "Oh, ok. Sure."
scene ep9_diks_ph2_dcam_event4 with dissolve
mc "What's up? Chatting with Camila?"
scene ep9_diks_ph2_dcam_event5 with dissolve
de "Yeah!"
de "She's hot, right?"
scene ep9_diks_ph2_dcam_event6 with dissolve
mc "She's a pretty girl, for sure. And her outfit tonight is very nice."
scene ep9_diks_ph2_dcam_event5 with dissolve
de "I'm thinking about if I should make my move on her or not..."
if ep3_camilaDerek:
    de "You still think that's a good idea, right?"
else:
    scene ep9_diks_ph2_dcam_event6 with dissolve
    mc "You know what I think about this."
    scene ep9_diks_ph2_dcam_event5 with dissolve
    de "Yeah, but come on... It would be good for me, I think."
scene ep9_diks_ph2_dcam_event7 with dissolve
menu:
    "Go for it":
        mc "If it takes your mind off Ashley, go for it."
        scene ep9_diks_ph2_dcam_event8 with dissolve
    "Not when you're drunk":
        mc "If you're sincere about it, you shouldn't do it when you're drunk."
        mc "I get that you're hurting with Ashley not showing up, but you should treat Camila right."
        scene ep9_diks_ph2_dcam_event8 with dissolve
        de "I'm not that drunk, [mc_de]. And it's not the first time I've thought about this."
    "Don't do it":
        mc "Don't do it, bro. Not to Camila. I know you're only saying this to get over Ashley."
        scene ep9_diks_ph2_dcam_event8 with dissolve
        de "I'm not. I want this, [mc_de]."
        scene ep9_diks_ph2_dcam_event7 with dissolve
        mc "I don't think you do."
        label ep9_diks_ph2_dcam_eventb_label:
        scene ep9_diks_ph2_dcam_event9 with dissolve
        de "..."
        scene ep9_diks_ph2_dcam_event10 with dissolve
        de "Why didn't Ashley show up?"
        scene ep9_diks_ph2_dcam_event9 with dissolve
        mc "Try not to think about these things when you're drunk. Let's focus on the party and having fun."
        mc "Maybe you can go dancing or something instead?"
        if "ep9_diks_ph2_photo_bella_event_label" in event_list:
            scene ep9_diks_ph2_dcam_event11b with dissolve
        else:
            scene ep9_diks_ph2_dcam_event11 with dissolve
        de "Yeah. I just need a minute."
        if persistent.mod_wtenabled:
            $ optional_task_list[3] = "Take picture with Camila (Left Hallway)"
        else:
            $ optional_task_list[3] = "Take picture with Camila"
        $ task_list[15] = ""
        $ updateTaskList()
        jump endEvent

de "Can you ask her for me?"
scene ep9_diks_ph2_dcam_event7 with dissolve
mc "You want me to ask Camila if she's interested in you? Is that what you want?"
scene ep9_diks_ph2_dcam_event8 with dissolve
de "Yeah! Talk me up to her. Be my wingman, [mc_de]."
scene ep9_diks_ph2_dcam_event7 with dissolve
menu:
    "Ok, I'll do it":
        $ ep9_help_derek = True
        if branchAlone:
            mc "What if I like her too?"
            scene ep9_diks_ph2_dcam_event8 with dissolve
            de "You do?"
            scene ep9_diks_ph2_dcam_event7 with dissolve
            mc "I'll do this for you anyway."
            scene ep9_diks_ph2_dcam_event8 with dissolve
            de "What a bro."
        else:
            mc "I can try, but I won't promise anything."
            scene ep9_diks_ph2_dcam_event8 with dissolve
        de "Thanks, [mc_de]."
    "Not gonna happen":
        mc "Sorry, but that's not gonna happen."
        scene ep9_diks_ph2_dcam_event10 with dissolve
        de "I'll do it myself, then..."
        jump ep9_diks_ph2_dcam_eventb_label

scene ep9_diks_ph2_dcam_event12 with dissolve
mc "Camila! Hey! Can we talk in private for a moment?"
scene ep9_diks_ph2_dcam_event13 with dissolve
cam "Here?"
scene ep9_diks_ph2_dcam_event14 with dissolve
mc "Follow me."
scene ep9_diks_ph2_dcam_event15 with dissolve
mc "This is a better spot for it. Now I can hear what you're saying to me."
scene ep9_diks_ph2_dcam_event16 with dissolve
cam "The music is very loud tonight."
cam "So? What's up?"
scene ep9_diks_ph2_dcam_event17 with dissolve
mc "Wanna sit down for a bit?"
scene ep9_diks_ph2_dcam_event18 with dissolve
if ep9_camila_lewd:
    cam "Is it time for round two already?"
else:
    cam "Do I?"
scene ep9_diks_ph2_dcam_event17 with dissolve
mc "I'm not trying anything here; I wanted to talk to you."
scene ep9_diks_ph2_dcam_event18 with dissolve
cam "A girl can't be too sure when a guy pulls them away from the party to sit with them on a bed."
scene ep9_diks_ph2_dcam_event17 with dissolve
mc "If that were the case, I'd invite you back to my bed."
scene ep9_diks_ph2_dcam_event19 with dissolve
cam "Haha! Fair enough. What do you want?"
scene ep9_diks_ph2_dcam_event20 with dissolve
mc "Not much. Uh... How are you? Having fun?"
scene ep9_diks_ph2_dcam_event19 with dissolve
if ep9_camila_lewd:
    cam "Why are you asking me this?"
else:
    cam "This is what you wanted to ask me?"
scene ep9_diks_ph2_dcam_event20 with dissolve
mc "I'll cut to the chase. What do you think about Derek?"
scene ep9_diks_ph2_dcam_event21 with dissolve
cam "Derek? He's a fun guy, but he's also pretty immature - not to mention drunk as hell tonight."
scene ep9_diks_ph2_dcam_event24 with dissolve
mc "Sounds like you know him well."
scene ep9_diks_ph2_dcam_event22 with dissolve
cam "I wouldn't say that. I mean, we haven't talked a lot."
cam "But I've been around him and girls talk."
scene ep9_diks_ph2_dcam_event24 with dissolve
mc "He's a cool guy, though. Right?"
scene ep9_diks_ph2_dcam_event21 with dissolve
cam "Yeah. Sure."
scene ep9_diks_ph2_dcam_event24 with dissolve
mc "Would you like to get to know him more or...?"
if ep9_camila_lewd:
    scene ep9_diks_ph2_dcam_event23 with dissolve
    cam "You're trying to set me up with your friend the same night you fucked me?"
    scene ep9_diks_ph2_dcam_event24 with dissolve
    mc "I promised I'd ask."
    scene ep9_diks_ph2_dcam_event22 with dissolve
    cam "Well, the answer is no, ok? For many reasons."
else:
    scene ep9_diks_ph2_dcam_event22 with dissolve
    cam "I see what you're doing, but I'm gonna say no, ok? For many reasons."
    scene ep9_diks_ph2_dcam_event24 with dissolve
    mc "Ah. No worries. I wanted to check."
scene ep9_diks_ph2_dcam_event22 with dissolve
cam "It's not that he's a bad guy or something. He's cute, but I'm not fit to date someone now, and also..."
cam "He's clearly in love with Ashley."
scene ep9_diks_ph2_dcam_event24 with dissolve
mc "You know about that?"
scene ep9_diks_ph2_dcam_event21 with dissolve
cam "During our chat, he talked about her for more than half of it."
cam "And she talks a lot about him too. But it's complicated since she's with Anthony."
scene ep9_diks_ph2_dcam_event24 with dissolve
mc "We both seem to understand the situation then."
mc "I'll tell him you're not interested."
scene ep9_diks_ph2_dcam_event22 with dissolve
cam "Tell him what he needs to hear."
cam "If I were him, I wouldn't hit on girls while talking about my crush."

scene ep9_diks_ph2_dcam_event4 with dissolve
mc "Hey."
scene ep9_diks_ph2_dcam_event25 with dissolve
de "Did you talk to her?"
scene ep9_diks_ph2_dcam_event26 with dissolve
mc "Yeah. Sorry, bud... She's not interested."
scene ep9_diks_ph2_dcam_event10 with dissolve
de "Damn..."
scene ep9_diks_ph2_dcam_event9 with dissolve
mc "A little tip, if you want to hook up with a girl, don't spend time talking about Ashley with her."
mc "Imagine trying to get with a girl who always talked about her ex. It wouldn't feel good, would it?"
de "..."
scene ep9_diks_ph2_dcam_event10 with dissolve
de "Yeah, you're right. Thanks, [mc_de]. I owe you one."
$ task_list[15] = ""
if persistent.mod_wtenabled:
            $ optional_task_list[3] = "Take picture with Camila (Left Hallway)"
else:
            $ optional_task_list[3] = "Take picture with Camila"
$ updateTaskList()
$ new_bio("Derek", "I tried helping Derek hook up with Camila. It didn't go well since he's been talking too much about Ashley in front of her.")
$ new_bio("Camila", "Camila said that Derek was talking about Ashley a lot and that she wasn't interested in hooking up with him.")
jump endEvent

label ep9_diks_ph2_piss_event_label:
scene ep9_diks_ph2_piss_event1 with dissolve
uk "Huh?"
mc "Dude! What the fuck are you doing?"
uk "Isn't this the bathroom?"
scene ep9_diks_ph2_piss_event2 with dissolve
if affinity == "DIK":
    mc "No!? It's next door. Put your fucking cock away!"
else:
    mc "No!? It's next door."
scene ep9_diks_ph2_piss_event3 with dissolve
uk "No, that one is occupied. I could have sworn I used to piss in here."
scene ep9_diks_ph2_piss_event2 with dissolve
mc "Get out! This is not a fucking bathroom."
jump endEvent

label ep9_jill_tour_label:
$ ep9_photos[4] = True
scene ep9_jill_banana15 with dissolve
mc "Ok, I'm ready for that group tour."
scene ep9_jill_banana16 with dissolve
bia "Lead the way!"
scene ep9_jill_banana17 with wipeleft
mc "And finally, this is my room."
mc "Which is also where we have set up a camera to take pictures of everyone's costumes."
scene ep9_jill_banana18 with dissolve
ji "Oh! We have to take a picture together!"
scene ep9_jill_banana19 with dissolve
bia "Yes! [name]! Please, take one of us!"
scene ep9_jill_banana20 with dissolve
mc "Ok. Line up for me. Perfect. Say pumpkin!"
scene ep9_jill_banana21 with dissolve
"PUMPKIN!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_jill_banana21 with dissolve
mc "Done!"
scene ep9_jill_banana22 with dissolve
bia "Come, take one with us!"
ji "Yes!"
oli "I can shoot!"
scene ep9_jill_banana23 with dissolve
mc "We look so odd together, don't we?"
ji "A banana, a Spartan and a superhero? You don't say?"
oli "Pose for me, guys!"
scene ep9_jill_banana24 with dissolve
oli "You can do better than that. Bianca and Jill... Switch sides."
oli "[name]! Point your sword at the camera!"
oli "And... I'm thinking the banana and the superhero should kiss his cheeks."
scene ep9_jill_banana25 with dissolve
bia "Haha! Ok!"
ji "I can't reach him! Haha! This will have to do."
$ guideSuggestedPage = 64
scene ep9_jill_banana25a with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="\n{size=-4}(EP9 Touch Bianca){color=#E6F653}(+Cheater)"
                             $mod_choices[11]="\n{size=-4}(EP9 Touch Bianca){color=#E6F653}(+2 Cheater)"
menu:
    "Gently place your hand on ass [mod_gr][mod_choices[10]]":
        $ ep9_bianca_ass = True
        $ tc += 1
        scene ep9_jill_banana25b with dissolve
        $ renpy.pause()
        scene ep9_jill_banana25c with dissolve
    "Grab her ass [mod_gr][mod_choices[11]]":
        $ ep9_bianca_ass = True
        $ tc += 2
        scene ep9_jill_banana25e with dissolve
        $ renpy.pause()
        scene ep9_jill_banana25f with dissolve
    "Hover-hand [mod_gr][mod_choices[2]]":
        $ dk(-1)
        scene ep9_jill_banana25d with dissolve

oli "Wait, which button do I press?"
scene ep9_jill_banana26 with dissolve
mc "The one on top to the right."
oli "Got it!"
scene ep9_jill_banana27 with dissolve
bia "*{i}Smack{/i}*"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_jill_banana27 with dissolve
$ renpy.pause(0.5)

scene ep9_jill_banana34 with dissolve
ji "Can I have one with just [name]? No offense, Bianca."
bia "Of course!"
scene ep9_jill_banana28 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_jill_banana28 with dissolve
$ renpy.pause()
scene ep9_jill_banana29 with dissolve
mc "I'm so happy you're here."
scene ep9_jill_banana30 with dissolve
ji "[name]?"
ji "I know we're taking things slow and all..."
ji "But if it's fine with you, can I tell Bianca and Olivia about us?"
ji "I'd love to let them know. And Bella too."
scene ep9_jill_banana31 with dissolve
mc "I kind of told Derek earlier, so I can't tell you no."
scene ep9_jill_banana30 with dissolve
ji "We're doing this? We're going official?"
if pathMayaJosy and not branchMayaJosy:
    scene ep9_jill_banana31 with dissolve
    mc "Yeah, soon... I mean... Do we have to tell everyone right now?"
    scene ep9_jill_banana30 with dissolve
    ji "Well, maybe not everyone, but... Maybe those closest to us, at least?"
    scene ep9_jill_banana31 with dissolve
    mc "Yeah... Ok..."
    mc "(I wonder where she draws the line to that... Damn... I have to talk to Josy and Maya soon.)"
else:
    scene ep9_jill_banana31 with dissolve
    mc "I believe we are."
    scene ep9_jill_banana30 with dissolve
    ji "It's kind of scary, isn't it?"
    scene ep9_jill_banana31 with dissolve
    menu:
        "A bit":
            mc "A bit scary. I've never done it before."
            scene ep9_jill_banana30 with dissolve
            ji "Me neither. Let's take it slow even so. Ok?"
        "No":
            mc "I don't think so. I want to do it."
            scene ep9_jill_banana30 with dissolve
            ji "That's good, but let's take it slow even so. Ok?"
        "Joke":
            mc "Compared to the STD test? Not really."
            scene ep9_jill_banana32 with dissolve
            ji "Haha. Shush!"
scene ep9_jill_banana35 with dissolve
bia "What are you two whispering about?"
scene ep9_jill_banana33 with dissolve
ji "We have something to tell you. It's not quite official yet, so keep it to yourselves for now, but..."
ji "[name] and I are...together."
scene ep9_jill_banana36 with dissolve
oli "You're a couple!?"
bia "Oh my God! Really?"
scene ep9_jill_banana33 with dissolve
ji "Yes!"
scene ep9_jill_banana37 with dissolve
bia "Aw! Jill! Congratulations!"
ji "Thank you so much!"
scene ep9_jill_banana38 with dissolve
bia "And to you too!"
mc "Thanks, Bianca."
scene ep9_jill_banana39 with dissolve
oli "We should celebrate!"
bia "Yes! Let's!"
bia "Shoot! Matthew should be here soon. Can we tell him?"
ji "Yes, of course!"
$ new_bio("Jill", "I took a picture together with Jill and Bianca at the Halloween party.")
$ new_bio("Bianca", "I took a picture together with Jill and Bianca at the Halloween party.")
if pathMayaJosy and not branchMayaJosy:
    scene ep9_jill_banana40 with dissolve
    mc "(And I need to talk to Maya and Josy before they hear this second-hand... Fuck... I'm gonna ruin their night.)"
    mc "(But they deserve to hear it from me.)"
    $ new_bio("Jill", "Jill wanted our relationship to be official soon, but I hadn't broken up with Josy and Maya yet...")
else:
    $ new_bio("Jill", "Jill wanted our relationship to be official soon.")
$ event_list.append("ep9_jill_dance_label")
if persistent.mod_wtenabled:
    
    if wt_ep9_branch_numbers > 1:
        
            $task_list[3] = task_list[3].replace("Give Jill a tour (Main Party room)", "Dance with Jill (Tommy's room)")
            $task_list[3] = task_list[3].replace("Give Jill a tour", "Dance with Jill (Tommy's room)")
    else:
        $ task_list[3] = "Dance with Jill (Tommy's room)"
    
else:
    
    
    if wt_ep9_branch_numbers > 1:
        
            $task_list[3] = task_list[3].replace("Give Jill a tour (Main Party room)", "Dance with Jill")
            $task_list[3] = task_list[3].replace("Give Jill a tour", "Dance with Jill")
    else:
        $ task_list[3] = "Dance with Jill"
jump endEvent

label ep9_jill_test_label:
scene ep9_jill_test1b with dissolve
de "Checking up on the food?"
scene ep9_jill_test2b with dissolve
mc "Yeah, I need to. The guests eat and drink a lot."
scene ep9_jill_test3b with dissolve
de "I just remembered..."
de "You didn't finish your story before. I wanna hear what happened with you and Jill."
scene ep9_jill_test4b with dissolve
mc "Right... Where were we?"
scene ep9_jill_test5b with dissolve
de "You tested your dick or something. How's the fella doing?"
scene ep9_jill_test4b with dissolve
mc "Have you ever been to a clinic doing that?"
scene ep9_jill_test6b with dissolve
de "No. What I don't know doesn't hurt me."
scene ep9_jill_test7b with dissolve
stop music fadeout 3
mc "Sadly, that doesn't apply to STDs."
mc "Um... I felt exposed going there."
play music "music/ep5/rustic_ballad.mp3"
scene ep9_jill_test1 with dissolve
$ renpy.pause()
scene ep9_jill_test2 with dissolve
$ renpy.pause()
scene ep9_jill_test3 with dissolve
ji "Are you nervous?"
scene ep9_jill_test4 with dissolve
mc "Yeah, but I shouldn't be. I don't have any STDs...I just know it."
scene ep9_jill_test5 with dissolve
ji "Don't worry. It's not an invasive procedure."
mc "So, you did it before?"
scene ep9_jill_test6 with dissolve
ji "This might surprise you, but the internet has a lot of valuable information if you want to look something up."
scene ep9_jill_test7 with dissolve
mc "Very funny..."
scene ep9_jill_test8 with dissolve
nu "Apply the lotion and don't have sexual intercourse for at least two weeks and you will be fine."
scene ep9_jill_test9 with dissolve
dw "What if I shave my pubes? Will it get rid of the itch?"
scene ep9_jill_test10 with dissolve
nu "It will get rid of their eggs, but you still need that lotion."
scene ep9_jill_test11 with dissolve
dw "It's just... How could I have gotten crabs? I always shower after gym."
scene ep9_jill_test12 with dissolve
dw "..."
scene ep9_jill_test13 with dissolve
mc "*{i}Whispers{/i}* And you said I wouldn't know anyone here..."
scene ep9_jill_test14 with dissolve
ji "I have a feeling he's more embarrassed than you are."
scene ep9_jill_test15 with dissolve
nu "[name] [lname]?"
scene ep9_jill_test16 with dissolve
ji "Good luck!"

scene ep9_jill_test17 with dissolve
nu "Please, make yourself comfortable. There's a coat hanger by the door."
scene ep9_jill_test18 with dissolve
mc "Thanks... I gotta say I'm a bit nervous about this."
mc "I don't think I've got any STDs, but testing myself for one still feels scary."
nu "That's a normal reaction; I hear it all the time."
nu "Think of it as a standard health check and a way to make sure you can get treatment if you truly need it."
scene ep9_jill_test19 with dissolve
mc "Yeah, but still... It feels kind of embarrassing."
scene ep9_jill_test20 with dissolve
nu "Please, don't feel-"
scene ep9_jill_test21 with dissolve
nu "Um... You can keep your pants on for this."
scene ep9_jill_test22 with dissolve
mc "..."
scene ep9_jill_test8b
de "..."
scene ep9_jill_test9b with dissolve
mc "I thought she needed to see my dick."
scene ep9_jill_test8b with dissolve
de "..."

scene ep9_jill_test23
mc "I'm so sorry! I thought you needed to examine me."
scene ep9_jill_test24 with dissolve
nu "Well, I do. But we do that with blood analysis."
scene ep9_jill_test25 with dissolve
mc "..."
scene ep9_jill_test26 with dissolve
mc "This is confidential, right?"
scene ep9_jill_test27 with dissolve
nu "Haha... Yes, I'm sworn to professional secrecy."
scene ep9_jill_test26 with dissolve
mc "I bet guys do that all the time too."
stop music fadeout 3
scene ep9_jill_test28 with dissolve
nu "No, that was a first."
$ guideSuggestedPage = 70
$ mphone_next_song()
scene ep9_jill_test10b with dissolve
de "Hahaha!"
scene ep9_jill_test7b with dissolve
mc "I couldn't get out of there fast enough."
scene ep9_jill_test10b with dissolve
de "This is the best story ever!"
scene ep9_jill_test7b with dissolve
mc "I'm glad you're enjoying it."
mc "Anyway, the test came out clean."
scene ep9_jill_test11b with dissolve
de "Nice! At least that's some good news."
scene ep9_jill_test7b with dissolve
mc "Yeah, it is."
scene ep9_jill_test11b with dissolve
de "So...? No more condoms?"
scene ep9_jill_test12b with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        
                        
                        
            
menu:
    "Doesn't look like it [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "Nope. It doesn't look like it."
    "Never! [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "Never was. Never will be."
scene ep9_jill_test11b with dissolve
de "Cheers, [mc_de]! To raw dogging!"
scene ep9_jill_test13b with dissolve
mc "Sure. Cheers!"
$ new_bio("Jill", "I didn't have any STDs. I guess Jill won't make a fuss about me skipping the condom from now on.")
$ task_list[16] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_jsolo_event_label:
$ event_list.append("ep9_diks_ph2_zoey_event_label")
if branchMayaJosy:
    $ event_list.append("ep9_jsolo_label")
scene ep9_diks_ph2_jsolo_event1 with dissolve
js "Eww! Eyeballs and fingers? Are we supposed to eat those?"
scene ep9_diks_ph2_jsolo_event2 with dissolve
my "I dare you to try one."
scene ep9_diks_ph2_jsolo_event1 with dissolve
js "I'll have a muffin, but I'm not putting that eye thing into my mouth. No way! You do it."
scene ep9_diks_ph2_jsolo_event2 with dissolve
my "I don't even know what it is."
scene ep9_diks_ph2_jsolo_event3 with dissolve
jb "And over here, you have my contribution to the party."
scene ep9_diks_ph2_jsolo_event4 with dissolve
zo "You made these?"
scene ep9_diks_ph2_jsolo_event5 with dissolve
jb "Yep. Of course, I got some helping hands, but this is mainly me."
scene ep9_diks_ph2_jsolo_event6 with dissolve
zo "Looks awesome! Can I try one?"
jb "Yeah! You have to! Try the eyeballs."
scene ep9_diks_ph2_jsolo_event7 with dissolve
zo "Mmm! Strawberry!"
jb "You guessed it."
scene ep9_diks_ph2_jsolo_event8 with dissolve
js "Strawberries?"
my "Now you have to try one."
scene ep9_diks_ph2_jsolo_event9 with dissolve
zo "Yeah, do it! They're amazeballs! In fact, you should call them that, JB."
scene ep9_diks_ph2_jsolo_event10 with dissolve
js "Ok, they are very good, but they look gross. I can't look at them when I put them in my mouth."
scene ep9_diks_ph2_jsolo_event11 with dissolve
zo "Like any other balls, huh?"
scene ep9_diks_ph2_jsolo_event13 with dissolve
js "Uh."
jb "Hahah!"

scene ep9_diks_ph2_jsolo_event12 with dissolve
zo "Oh. Sorry. Not your kind of humor?"
scene ep9_diks_ph2_jsolo_event14 with dissolve
js "I just wasn't expecting that while eating this."
scene ep9_diks_ph2_jsolo_event15 with dissolve
jb "Let's continue the tour. Have you seen the movie theater? We're playing horror movies all night."
scene ep9_diks_ph2_jsolo_event16 with dissolve
if branchMayaJosy:
    my "Can I come with you?"
else:
    my "Horror movies? Really?"
scene ep9_diks_ph2_jsolo_event15 with dissolve
jb "Follow me."
scene ep9_diks_ph2_jsolo_event17 with dissolve
js "I'll be right with you, after I finish my...ball."
scene ep9_diks_ph2_jsolo_event18 with dissolve
mc "Aha, so you're the one who's been eating our cakes?"
scene ep9_diks_ph2_jsolo_event19 with dissolve
js "No, trust me. I had one ball and it was enough."
scene ep9_diks_ph2_jsolo_event18 with dissolve
mc "Not good?"
scene ep9_diks_ph2_jsolo_event19 with dissolve
js "It was, but I'm trying to process it."
scene ep9_diks_ph2_jsolo_event18 with dissolve
mc "Want some punch?"
scene ep9_diks_ph2_jsolo_event19 with dissolve
js "Please."
scene ep9_diks_ph2_jsolo_event20 with dissolve
js "Thank you."
scene ep9_diks_ph2_jsolo_event21 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_jsolo_event22 with dissolve
if branchMayaJosy:
    js "Oh... Strong punch."
    scene ep9_diks_ph2_jsolo_event23 with dissolve
    mc "Is it?"
    scene ep9_diks_ph2_jsolo_event22 with dissolve
    js "I like it, though."
    js "So, aren't you cold wearing that?"
    scene ep9_diks_ph2_jsolo_event24 with dissolve
    mc "Not at all. What about you? You're not covered up yourself."
    scene ep9_diks_ph2_jsolo_event26 with dissolve
    js "Tsk. I'm not the one walking around with my nipples showing."
    scene ep9_diks_ph2_jsolo_event28 with dissolve
    if dtype >= 0:
        mc "Wasted potential for your costume, I'd say."
        scene ep9_diks_ph2_jsolo_event44 with dissolve
        js "Haha! The night has just started, so..."
        scene ep9_diks_ph2_jsolo_event45 with dissolve
        mc "You serious?"
        scene ep9_diks_ph2_jsolo_event44 with dissolve
        js "In private, with you... Why not?"
        scene ep9_diks_ph2_jsolo_event45 with dissolve
        mc "Bathroom?"
        scene ep9_diks_ph2_jsolo_event46 with dissolve
        js "Looks like there's a queue... Sorry."
        scene ep9_diks_ph2_jsolo_event47 with dissolve
        js "*{i}Psst{/i}* Come closer."
        scene ep9_diks_ph2_jsolo_event48 with dissolve
        js "Happy?"
        mc "Your nipples look way hotter than mine."
        scene ep9_diks_ph2_jsolo_event37 with dissolve
        js "I hope no one saw that..."
    else:
        mc "That's probably for the best."
        scene ep9_diks_ph2_jsolo_event31 with dissolve
        js "I'll drink to that!"
    scene ep9_diks_ph2_jsolo_event36 with dissolve
    mc "Anything new with you?"
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "Not a lot. It's been nice to have some free time from studying, but I can't wait for Monday."
    jump ep9_diks_ph2_jsolo_event2_label
elif pathMayaJosy:
    js "Been busy lately?"
    scene ep9_diks_ph2_jsolo_event25 with dissolve
    mc "Yeah... I've had plenty to do. How about you?"
    scene ep9_diks_ph2_jsolo_event27 with dissolve
    js "Not at all. This is the calmest it has been since I came here. No classes, no nothing."
    scene ep9_diks_ph2_jsolo_event29 with dissolve
    mc "Yeah? Just time to relax."
    scene ep9_diks_ph2_jsolo_event30 with dissolve
    js "Yep. So, why aren't you?"
    scene ep9_diks_ph2_jsolo_event29 with dissolve
    mc "Planning parties takes time and I've been working extra for the frat too. And I went back home...and what else?"
    scene ep9_diks_ph2_jsolo_event32 with dissolve
    js "You'll have to fill me in."
    scene ep9_diks_ph2_jsolo_event33 with dissolve
    mc "I guess that's about it."
    js "..."
    scene ep9_diks_ph2_jsolo_event34 with dissolve
    js "Ok."
    js "I better catch up to Maya and the party tour."
    scene ep9_diks_ph2_jsolo_event33 with dissolve
    mc "Yeah. Sure. There's a camera in my room if you want your picture taken later."
    scene ep9_diks_ph2_jsolo_event34 with dissolve
    js "Yeah, I'm aware. Elena told me."
    scene ep9_diks_ph2_jsolo_event33 with dissolve
    mc "Great."
    scene ep9_diks_ph2_jsolo_event35 with dissolve
    mc "(Fuck... She can tell that there's something off.)"
    $ new_bio("Josy", "Josy could definitely tell that there was something off with me. I tried to play it cool before I got the chance to break up with her and Maya, but I don't think it worked.")
else:
    js "What have you been up to lately?"
    scene ep9_diks_ph2_jsolo_event24 with dissolve
    mc "I've been keeping busy doing all kinds of things. Party planning, work, went back home..."
    scene ep9_diks_ph2_jsolo_event26 with dissolve
    js "Fun! It feels good to have some time off from school, huh?"
    scene ep9_diks_ph2_jsolo_event28 with dissolve
    mc "Totally. Those midterm exams messed with my head."
    mc "What about you? What have you been up to?"
    scene ep9_diks_ph2_jsolo_event31 with dissolve
    js "A whole lot of nothing. Gym, friends and such."
    js "I can't wait for Monday, though."
    label ep9_diks_ph2_jsolo_event2_label:
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "How come?"
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "I'm adding a new class to my curriculum - Economic Analysis."
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "Wow... Sounds...boring."
    scene ep9_diks_ph2_jsolo_event39 with dissolve
    js "Boring? Haha! Please! Derek told me what you two are taking. Intro to...nerd stuff or something."
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "Science! That's hardly nerd stuff. And who are you to talk? Your class has the word analysis in it."
    mc "What do you sit around doing in that class? Look at economy stuff and analyze it?"
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "That is pretty much the nail on the head."
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "See!? Nerd!"
    scene ep9_diks_ph2_jsolo_event39 with dissolve
    js "Haha! You are! Lab nerd!"
    js "Gonna make all kinds of explosions in that class, I guess."
    scene ep9_diks_ph2_jsolo_event40 with dissolve
    mc "Why do non-scientists think that scientists make explosions? I'd say most wanna avoid that kind of thing."
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "Good luck with that if Derek's your lab partner."
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "Based on our last class together, we probably won't be partners."
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "Haha!"
    js "I better catch up to Maya and the party tour."
    if branchMayaJosy:
        scene ep9_diks_ph2_jsolo_event38 with dissolve
        mc "Skip the tour; wanna take a picture with me? There's a camera in my room for it."
        scene ep9_diks_ph2_jsolo_event41 with dissolve
        js "Yes! We totally should do that! Let's get Maya!"
        jump ep9_diks_ph2_photo_jm_event_label
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    mc "Sure. There's a camera in my room if you want your picture taken later."
    scene ep9_diks_ph2_jsolo_event42 with dissolve
    js "..."
    scene ep9_diks_ph2_jsolo_event37 with dissolve
    js "Wanna take one with me?"
    scene ep9_diks_ph2_jsolo_event38 with dissolve
    menu:
        "[mod_gr]Sure":
            $ ep9_photos[15] = True
            mc "I don't wanna split you up from your tour."
            scene ep9_diks_ph2_jsolo_event37 with dissolve
            js "Eh. Maya will show me what I missed. Let's go!"
            jump ep9_diks_ph2_photo_j_event_label
        "No":
            mc "Sorry, but I have things to do."
            scene ep9_diks_ph2_jsolo_event43 with dissolve
            js "Ok. Back to the tour, it is."
if persistent.mod_wtenabled:
    $ task_list[4] = "Talk to Zoey (Jacob's room)"
else:
    $ task_list[4] = "Talk to Zoey"
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_j_event_label:
scene ep9_diks_ph2_photo_j_event1 with dissolve
js "What's the green screen for?"
mc "You'll see soon enough."
scene ep9_diks_ph2_photo_j_event2 with dissolve
js "Ok. So, how should we pose?"
scene ep9_diks_ph2_photo_j_event3 with dissolve
mc "I don't know. Any ideas?"
scene ep9_diks_ph2_photo_j_event4 with dissolve
js "How about this?"
scene ep9_diks_ph2_photo_j_event5 with dissolve
mc "That way? Isn't it too boring?"
scene ep9_diks_ph2_photo_j_event6 with dissolve
js "Huh!? Boring? Ok, how about if you lift me?"
scene ep9_diks_ph2_photo_j_event7 with dissolve
mc "Or you lift me?"
scene ep9_diks_ph2_photo_j_event8 with dissolve
js "Haha! I may be shredding at the gym, but I'm nowhere near being able to do that."
scene ep9_diks_ph2_photo_j_event9 with dissolve
mc "Ok! Smile to the camera."
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_j_event9 with dissolve
$ renpy.pause(0.5)

scene ep9_diks_ph2_photo_j_event10 with dissolve
js "Haha! Thanks, that was fun."
scene ep9_diks_ph2_photo_j_event11 with dissolve
mc "So... About earlier..."
scene ep9_diks_ph2_photo_j_event12 with dissolve
js "Yeah?"
scene ep9_diks_ph2_photo_j_event13 with dissolve
mc "How is it between you and Maya? I picked up on some tension..."
scene ep9_diks_ph2_photo_j_event14 with dissolve
js "It's...choppy. But it's better than it was before, so... We're hanging in there."
scene ep9_diks_ph2_photo_j_event13 with dissolve
mc "Ok. Good."
scene ep9_diks_ph2_photo_j_event14 with dissolve
js "And what about you and love?"
scene ep9_diks_ph2_photo_j_event13 with dissolve
mc "Well, that's an interesting question..."
if branchAlone:
    mc "...with a pretty boring answer. I'm hanging in there as well, trying to explore a bit."
else:
    mc "It's actually pretty good."
scene ep9_diks_ph2_photo_j_event15 with dissolve
js "Good... Good."
scene ep9_diks_ph2_photo_j_event16 with dissolve
js "..."
scene ep9_diks_ph2_photo_j_event17 with dissolve
js "Do you...ever wonder how things might have turned out if it had been different?"
scene ep9_diks_ph2_photo_j_event16 with dissolve
mc "Different how?"
scene ep9_diks_ph2_photo_j_event17 with dissolve
js "Just...different?"
scene ep9_diks_ph2_photo_j_event18 with dissolve
mc "Like if you weren't with Maya?"
scene ep9_diks_ph2_photo_j_event19 with dissolve
js "Well, yeah, but you said it. I didn't."
scene ep9_diks_ph2_photo_j_event18 with dissolve
mc "You were thinking it."
$ guideSuggestedPage = 66
scene ep9_diks_ph2_photo_j_event19 with dissolve
js "Can't help but wonder, no?"
scene ep9_diks_ph2_photo_j_event18 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
menu:
    "All the time [mod_gr][mod_choices[11]]":
        if not branchAlone:
            $ tc += 2
        $ ep9_josy_wonder = 3
        mc "There's no way to tell. We can't reverse time and change stuff."
        mc "But yeah...I think about that all the time."
        scene ep9_diks_ph2_photo_j_event20 with dissolve
        js "All the time?"
        scene ep9_diks_ph2_photo_j_event21 with dissolve
        mc "Well, a lot. But it's good that it came to this."
        mc "Having you as a friend is awesome too."
        scene ep9_diks_ph2_photo_j_event20 with dissolve
        js "Yeah..."
        $ new_bio("Josy", "I told Josy I think about her and our relationship all the time. What would it have been like if things were different?")
    "A bit [mod_gr][mod_choices[10]]":
        if not branchAlone:
            $ tc += 1
        $ ep9_josy_wonder = 2
        mc "A bit, yeah. But there's no way to tell. We can't reverse time and change stuff."
        scene ep9_diks_ph2_photo_j_event22 with dissolve
        js "No... I guess we can't."
        $ new_bio("Josy", "I told Josy I think about her and our relationship from time to time. What would it have been like if things were different?")
    "We wouldn't have worked out":
        $ ep9_josy_wonder = 1
        mc "There's no way to tell. We can't reverse time and change stuff."
        mc "I think you and I were doomed to fail at the start without knowing it."
        scene ep9_diks_ph2_photo_j_event23 with dissolve
        js "Oof..."
        scene ep9_diks_ph2_photo_j_event24 with dissolve
        mc "..."
        mc "That wasn't what you wanted to hear?"
        scene ep9_diks_ph2_photo_j_event23 with dissolve
        js "I think you're wrong about that... That's all."
        $ new_bio("Josy", "I told Josy I thought our relationship would have been doomed to fail, even if it weren't for her and Maya.")
scene ep9_diks_ph2_photo_j_event25 with dissolve
js "I should get back to the tour now. They probably left without me."
scene ep9_diks_ph2_photo_j_event26 with dissolve
mc "..."
$ new_bio("Josy", "I took a picture together with Josy at the Halloween party.")
if persistent.mod_wtenabled:
    $ task_list[4] = "Talk to Zoey (Jacob's room)"
else:
    $ task_list[4] = "Talk to Zoey"
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_jmtalk_event_label:
scene ep9_diks_ph2_jmtalk_event1 with dissolve
$ renpy.pause()
play music "music/ep9/licensed_music/track116.mp3"
scene ep9_diks_ph2_jmtalk_event2 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_jmtalk_event3 with dissolve
sa "You like these movies?"
my "Love them! Horror is one of my favorite genres."
scene ep9_diks_ph2_jmtalk_event4 with dissolve
sa "[name] told me he didn't think people would be watching movies at a party."
scene ep9_diks_ph2_jmtalk_event5
if not persistent.ep9_cardji11:
    show screen ep9_render_screen("ji11")
with dissolve
my "Take a look around you. I don't see anyone watching."
scene ep9_diks_ph2_jmtalk_event6
hide screen ep9_render_screen
with dissolve
stop music fadeout 3
sa "Haha! So, that's why you're in here?"
scene ep9_diks_ph2_jmtalk_event7 with dissolve
play music "music/ep9/relaxed.mp3"
my "Didn't you figure that out yet? I obviously wanna make out with you."
scene ep9_diks_ph2_jmtalk_event9 with dissolve
sa "Tsk! I bet you would. I'm an awesome kisser."
scene ep9_diks_ph2_jmtalk_event8 with dissolve
my "Yeah? Did you ever kiss a girl?"
scene ep9_diks_ph2_jmtalk_event9 with dissolve
sa "Sure, I did. Plenty of times. Mostly at parties. It's not that weird when you kiss friends for fun."
scene ep9_diks_ph2_jmtalk_event8 with dissolve
my "I would never have guessed."
scene ep9_diks_ph2_jmtalk_event10 with dissolve
sa "What about you? Ever kissed a *{i}Whispers{/i}* guy?"
scene ep9_diks_ph2_jmtalk_event11 with dissolve
my "Yeah."
scene ep9_diks_ph2_jmtalk_event10 with dissolve
sa "You're shitting me? For fun?"
scene ep9_diks_ph2_jmtalk_event11 with dissolve
my "Um. Actually, no. It felt pretty real."
scene ep9_diks_ph2_jmtalk_event12 with dissolve
sa "Wow! So, you're not 100%%...?"
scene ep9_diks_ph2_jmtalk_event13 with dissolve
my "I don't know what I am, exactly."
scene ep9_diks_ph2_jmtalk_event14 with dissolve
sa "Must have been one hell of a guy."
scene ep9_diks_ph2_jmtalk_event17 with dissolve
if branchMayaJosy or ep5_followed_maya or ep7_solo_maya:
    my "Yeah. He is."
my "It was [name]."
scene ep9_diks_ph2_jmtalk_event15 with dissolve
sa "[name]? No kidding?"
scene ep9_diks_ph2_jmtalk_event17 with dissolve
my "Nope."
if branchSage:
    scene ep9_diks_ph2_jmtalk_event15 with dissolve
    sa "I see... Um..."
else:
    scene ep9_diks_ph2_jmtalk_event16 with dissolve
    sa "How about that...?"
scene ep9_diks_ph2_jmtalk_event18 with dissolve
sa "Ugh."
my "What?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event19 with dissolve
    sa "Jill Royce is here. And what the fuck is she wearing?"
else:
    scene ep9_diks_ph2_jmtalk_event19b with dissolve
    sa "Jill Royce is here."
my "Don't you like her?"
scene ep9_diks_ph2_jmtalk_event18 with dissolve
sa "I can't stand her."
my "Oh? Well, Josy is fond of her."
sa "Blows my mind."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event20 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event20b with dissolve
ji "Hi."
scene ep9_diks_ph2_jmtalk_event21 with dissolve
my "Hi, Jill."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event20 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event20b with dissolve
ji "Josy's fetching drinks. May I sit with you?"
scene ep9_diks_ph2_jmtalk_event21 with dissolve
my "Sure, there's room for all of us."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event22 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event22b with dissolve
ji "I love your costumes."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event23 with dissolve
    my "Thank you! Yours is very funny!"
else:
    scene ep9_diks_ph2_jmtalk_event23b with dissolve
    my "Thank you! You look pretty in yours."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event24 with dissolve
    ji "It's a tad impractical and very hot to wear..."
else:
    scene ep9_diks_ph2_jmtalk_event24b with dissolve
ji "Are we watching scary movies?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event29 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event29b with dissolve
sa "No, look around you. I was gonna make out with Maya on this couch."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event25 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event25b with dissolve
ji "Oh!? So, I was interrupting?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event30 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event30b with dissolve
my "She's joking."
my "Sage... I believe Jill wants to help."
scene ep9_diks_ph2_jmtalk_event31 with dissolve
sa "Huh? What do you mean?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event30 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event30b with dissolve
my "Josy told me she talked to you."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event26 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event26b with dissolve
ji "Oh, yes. I wasn't going to bring that up tonight, but she did."
ji "She told me you needed legal advice."
scene ep9_diks_ph2_jmtalk_event31 with dissolve
sa "*{i}Whispers{/i}* Did she tell {b}her{/b} about what's going on?"
scene ep9_diks_ph2_jmtalk_event32 with dissolve
my "*{i}Whispers{/i}* Not any details, I believe."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event30 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event30b with dissolve
my "Yes, I've been looking for someone to ask a few questions about something."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event26 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event26b with dissolve
ji "About your student loan, correct?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event30 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event30b with dissolve
my "Yes, exactly."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event27 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event27b with dissolve
ji "What do you want to ask?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event30 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event30b with dissolve
my "It's pretty complicated. This is not the place to talk about it."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event27 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event27b with dissolve
ji "Of course, I understand. Anyway, I'm willing to help you if you want."
ji "Also, my family's lawyer is at my disposal if need be, so..."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event33 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event33b with dissolve
my "Are you sure? That would be...perfect!"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event27 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event27b with dissolve
ji "It's not a problem. It seems to matter a lot to Josy, so I'd help with any questions."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event29 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event29b with dissolve
sa "Wait a minute. Don't agree to anything yet, Maya."
sa "You're just gonna offer help like that? What's the catch?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event28b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event28 with dissolve
ji "There's...no catch."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event29 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event29b with dissolve
sa "Yeah, right. So, you're telling me it's for free? No hidden agenda?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event28b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event28 with dissolve
ji "Yes? Why would there be?"
scene ep9_diks_ph2_jmtalk_event32 with dissolve
my "Sage..."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event29 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event29b with dissolve
sa "It doesn't add up."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event28b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event28 with dissolve
ji "Excuse me?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event29 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event29b with dissolve
sa "You're friends slash lover with my brother, and I know his kind. They are all the same."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event28b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event28 with dissolve
ji "I'm not sure of the nicest way to say this, but I'm not your brother's friend and - eww - lover? I'm not your brother's anything."
ji "Frankly, I don't want to be near him."
scene ep9_diks_ph2_jmtalk_event34 with dissolve
sa "What!?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event28b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event28 with dissolve
ji "I'm sorry if that offends you, but that's my truth. He's a real piece of...work."
scene ep9_diks_ph2_jmtalk_event34 with dissolve
sa "You hate him?"

if branchJill:
    scene ep9_diks_ph2_jmtalk_event37 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event37b with dissolve
ji "Hate is a rather strong word."

scene ep9_diks_ph2_jmtalk_event35 with dissolve
sa "You hate him!"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event36b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event36 with dissolve
ji "..."

scene ep9_diks_ph2_jmtalk_event35 with dissolve
sa "I hate him too!"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event37 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event37b with dissolve
ji "You hate your brother?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event40 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event40b with dissolve
sa "Hold on! Hold on! What the fuck?"
sa "The way he's been talking about you, I thought you were his soulmate."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event37 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event37b with dissolve
ji "Stop saying that. I've tried to be friendly to him, but he's not been treating me nicely lately."
scene ep9_diks_ph2_jmtalk_event41 with dissolve
my "So, uh... This is good, no?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event40 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event40b with dissolve
sa "Maya, this is mind-blowing to me. I've thought Jill was Tybalt's crony all this time."
sa "Jill, you gotta tell me more about this. What do you hate the most about him?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event37 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event37b with dissolve
ji "This is rather..."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event40 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event40b with dissolve
sa "Don't feel shy. We all hate him here. Right, Maya?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event42 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event42b with dissolve
my "I haven't talked a lot to him, but he once called lesbianism \"appalling\". That struck a chord with me."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event38 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event38b with dissolve
ji "I told him off recently, and since then, he's been trying to get my attention in different ways."
ji "One thing he started doing is what he believes to be yoga, on the balcony outside of my window."
scene ep9_diks_ph2_jmtalk_event43 with dissolve
sa "Hahaha! He does? Oh my fucking God! What a creep!"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event38 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event38b with dissolve
ji "And he started playing cello too, either when I'm sleeping or supposed to practice playing the piano."

$ renpy.sound.set_volume(0,channel='music')
scene ep9_diks_ph2_jmtalk_event46
$ renpy.pause()
scene ep9_diks_ph2_jmtalk_event47 with dissolve
play sound "sound_effects/season2/piano_c.mp3"
$ renpy.pause(1)
$ renpy.sound.play("sound_effects/season3/tybalt_cello.mp3", channel="sfx1", loop=False)
scene ep9_diks_ph2_jmtalk_event49 with vpunch
"*{i}Out of tune cello noise{/i}*"
scene ep9_diks_ph2_jmtalk_event48b with dissolve
$ renpy.pause()
scene ep9_diks_ph2_jmtalk_event48c with dissolve
$ renpy.pause()
scene ep9_diks_ph2_jmtalk_event48 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=0)
$ renpy.sound.set_volume(1.0,channel='music')
scene ep9_diks_ph2_jmtalk_event43
sa "Hahaha!"
sa "Did you ever see him moisturize?"
if branchJill:
    scene ep9_diks_ph2_jmtalk_event39 with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event39b with dissolve
ji "Oh, God! Yes! That olive smell is repugnant. It cuts through the hallway into my room."
stop music fadeout 3
scene ep9_diks_ph2_jmtalk_event44 with dissolve
sa "And the way he spreads his fingers while applying it."

if branchJill:
    scene ep9_diks_ph2_jmtalk_event45b with dissolve
else:
    scene ep9_diks_ph2_jmtalk_event45 with dissolve
$ renpy.pause()

$ task_list[0] = ""
$ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep9_diks_ph2_heather_event_label:
play sound "sound_effects/shower_curtain.mp3"
scene ep9_diks_ph2_heather_event1 with hpunch
he "Tommy?"
scene ep9_diks_ph2_heather_event2 with dissolve
mc "Nope. Just me. What are you up to?"
scene ep9_diks_ph2_heather_event3 with dissolve
he "Looking for him, what else? Have you seen him?"
scene ep9_diks_ph2_heather_event2 with dissolve
mc "Let me think... Hm... Not for a while, no."
mc "How about you call him?"
scene ep9_diks_ph2_heather_event3 with dissolve
he "And where the hell would I keep my phone?"
scene ep9_diks_ph2_heather_event4 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_heather_event2 with dissolve
if affinity == "DIK":
    mc "Do you want an answer to that or...?"
    scene ep9_diks_ph2_heather_event5 with dissolve
    he "Ugh."
else:
    mc "Yeah, I can see what you mean."
    scene ep9_diks_ph2_heather_event5 with dissolve
    $ renpy.pause()
jump endEvent

label ep9_diks_ph2_preps_event_label:
play music "music/ep2/freedom.mp3"
scene ep9_diks_ph2_preps_event1 with wipeleft
$ renpy.pause()
scene ep9_diks_ph2_preps_event2 with dissolve
ty "This is marvelous. Everyone is looking dapper for High Society Halloween and it's impossible to tell who's who from looks alone."
scene ep9_diks_ph2_preps_event3 with dissolve
lu "This is what we do for Halloween?"
scene ep9_diks_ph2_preps_event4 with dissolve
cr "It's Halloween-like, at least."
scene ep9_diks_ph2_preps_event3 with dissolve
lu "This is so not what I thought this fraternity would be like. It makes me hate that I'm legacy."
scene ep9_diks_ph2_preps_event5 with dissolve
go "It isn't the best - especially not when you know what others are doing tonight."
scene ep9_diks_ph2_preps_event7 with dissolve
lu "Others? Like who?"
scene ep9_diks_ph2_preps_event5 with dissolve
go "The gals from that dorm gathering, they're off to the Halloween party at the Delta Iota Kappa."
scene ep9_diks_ph2_preps_event7 with dissolve
lu "Oh, man..."
scene ep9_diks_ph2_preps_event4 with dissolve
cr "I wouldn't mind some more quality time with Avery."
scene ep9_diks_ph2_preps_event6 with dissolve
go "Beth was...amazing. I don't want to brag, but she let me do things to her butt."
scene ep9_diks_ph2_preps_event7 with dissolve
lu "We gotta go there... There are like zero girls here."
scene ep9_diks_ph2_preps_event4 with dissolve
cr "As much as I agree with you, we can't. We must attend these social events; it's our obligation."
scene ep9_diks_ph2_preps_event8 with dissolve
lu "But they won't even know that we're gone. Everyone is dressed the same!"
lu "If we sneak out, one by one, we can make it."
scene ep9_diks_ph2_preps_event5 with dissolve
go "Suppose we do find a way to sneak out..."
go "How would we even get into that party?"
scene ep9_diks_ph2_preps_event9 with dissolve
if ep8_prep_truce:
    cr "Those fraternity members we talked to at the party were ok with us. Maybe they will let us in?"
else:
    cr "We could probably talk our way in."
scene ep9_diks_ph2_preps_event8 with dissolve
stop music fadeout 3
lu "Yes! It's worth a try."

$ event_list.append("ep9_diks_ph2_rusty_event_label")
if branchSage:
    $ event_list.append("ep9_ssolo_label")
    if persistent.mod_wtenabled:
        $ task_list[10] = "Help Sage (Right Hallway)"
    else:
        $ task_list[10] = "Help Sage"
if "ep9_jsolo_label" not in event_list:
    if persistent.mod_wtenabled:
        $ task_list[13] = "Help Josy (Main party room)"
    else:
        $ task_list[13] = "Help Josy"
$ event_list.append("ep9_ph2_josy_event_label")
if persistent.mod_wtenabled:
    $ task_list[9] = "Find Rusty (Tommy's room)"
else:
    $ task_list[9] = "Find Rusty"
$ task_list[14] = ""
$ updateTaskList()
$ mphone_next_song()
$ tmpAppList = []

jump endEvent

label ep9_diks_ph2_photo_jm_event_label:
scene ep9_diks_ph2_photo_jm_event1 with fade
my "What are these pictures gonna be used for?"
scene ep9_diks_ph2_photo_jm_event2 with dissolve
mc "They are for remembering Halloween. Jacob will fix them after the party to make them look extra special."
scene ep9_diks_ph2_photo_jm_event1 with dissolve
my "What a great idea!"
scene ep9_diks_ph2_photo_jm_event2 with dissolve
mc "Yeah! Line up for me."
scene ep9_diks_ph2_photo_jm_event3 with dissolve
js "How should we do it?"
scene ep9_diks_ph2_photo_jm_event4 with dissolve
my "Um. Will everyone see these photos?"
scene ep9_diks_ph2_photo_jm_event3 with dissolve
js "It's not illegal for {i}friends{/i} to be in the same picture."
scene ep9_diks_ph2_photo_jm_event4 with dissolve
my "I'm just checking."
scene ep9_diks_ph2_photo_jm_event5 with dissolve
mc "You're fine. I'll take some photos with both of you too."
scene ep9_diks_ph2_photo_jm_event6 with dissolve
mc "Smile!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_jm_event6 with dissolve
mc "That's very cute."
scene ep9_diks_ph2_photo_jm_event11 with dissolve
js "Wow, I wasn't prepared for that flash."
scene ep9_diks_ph2_photo_jm_event12 with dissolve
my "Can we take one where we're all together?"
scene ep9_diks_ph2_photo_jm_event13 with dissolve
js "Yes! What should we do?"
scene ep9_diks_ph2_photo_jm_event14 with dissolve
menu:
    "Funny pose":
        $ ep9_photos[5] = True
        mc "Oh! I got it! Let's do something funny!"
        mc "Pretend that you're both trying to grab my arm while flying."
        scene ep9_diks_ph2_photo_jm_event13 with dissolve
        js "How?"
        scene ep9_diks_ph2_photo_jm_event15 with dissolve
        mc "Like this, we'll play with the perspective."
        mc "I'll take a couple and hope it comes out good."
        scene ep9_diks_ph2_photo_jm_event7 with dissolve
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_jm_event7 with dissolve
        $ renpy.pause()
    "Sweet pose":
        $ ep9_photos[6] = True
        mc "Let's make a cute pose together."
        mc "If Maya jumps up on my back and I carry you, that will look fun, no?"
        scene ep9_diks_ph2_photo_jm_event25 with dissolve
        my "You can do that?"
        scene ep9_diks_ph2_photo_jm_event26 with dissolve
        mc "I think so. We can try it at least."
        scene ep9_diks_ph2_photo_jm_event8 with dissolve
        my "Haha! It works!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_jm_event8 with dissolve
        $ renpy.pause(0.5)
scene ep9_diks_ph2_photo_jm_event16 with dissolve
mc "Perfect. I'm sure Jacob can do something with these."
scene ep9_diks_ph2_photo_jm_event17 with dissolve
my "This is fun! Let's do some more."
scene ep9_diks_ph2_photo_jm_event18 with dissolve
js "Wanna have one with just the two of you?"
scene ep9_diks_ph2_photo_jm_event19 with dissolve
mc "Sure."
scene ep9_diks_ph2_photo_jm_event21 with dissolve
mc "Let's do this!"
my "Whoa! Haha!"
scene ep9_diks_ph2_photo_jm_event9 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_jm_event9 with dissolve
$ renpy.pause(0.5)
js "That is beautiful! Can you do us, Maya?"
scene ep9_diks_ph2_photo_jm_event20 with dissolve
my "Yeah, if [name] lets me down already."
scene ep9_diks_ph2_photo_jm_event23 with dissolve
js "Are you gonna lift me too?"
scene ep9_diks_ph2_photo_jm_event24 with dissolve
mc "How about if you hop up on my back instead?"
scene ep9_diks_ph2_photo_jm_event22 with dissolve
js "Haha! Woho!"
scene ep9_diks_ph2_photo_jm_event10 with dissolve
my "Cheese!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_jm_event10 with dissolve
$ renpy.pause(0.5)

if ep8_maya_lewd:
    scene ep9_diks_ph2_photo_jm_event27 with dissolve
else:
    scene ep9_diks_ph2_photo_jm_event27b with dissolve
my "I can't wait to see everyone's pictures!"
js "I bet they are gonna look so good!"
$ new_bio("Josy", "I took a picture together with Josy and Maya at the Halloween party.")
$ new_bio("Maya", "I took a picture together with Josy and Maya at the Halloween party.")
if persistent.mod_wtenabled:
    $ task_list[4] = "Talk to Zoey (Jacob's room)"
else:
    $ task_list[4] = "Talk to Zoey"
if persistent.mod_wtenabled:
    $ task_list[5] = "Talk to Josy (Derek's room)"
else:
    $ task_list[5] = "Talk to Josy"
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_sage_event_label:
$ guideSuggestedPage = 63
scene ep9_diks_ph2_photo_sage_event1 with dissolve
sa "It's time to get creative."
scene ep9_diks_ph2_photo_sage_event3 with dissolve
mc "Ah, you meant that."
scene ep9_diks_ph2_photo_sage_event2 with dissolve
sa "Disappointed, huh?"
scene ep9_diks_ph2_photo_sage_event3 with dissolve
if branchSage:
    mc "Maybe a little bit."
    scene ep9_diks_ph2_photo_sage_event2 with dissolve
    sa "The night's still young. Take a picture while I still look stunning."
else:
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "Yes [mod_gr][mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            mc "Yes. Who wouldn't be when a hot girl takes you back to your room?"
            scene ep9_diks_ph2_photo_sage_event4 with dissolve
            sa "You're such a flirt."
        "No":
            mc "No, not really. It will be fun taking a picture together."
            scene ep9_diks_ph2_photo_sage_event4 with dissolve
            sa "Right?"
        "More like worried":
            mc "Honestly, I was more like worried."
            scene ep9_diks_ph2_photo_sage_event4 with dissolve
            sa "Tsk!"
    sa "The night's still young. Take a picture while I still look stunning."

scene ep9_diks_ph2_photo_sage_event3 with dissolve
mc "Like that would change anytime soon."
scene ep9_diks_ph2_photo_sage_event5 with dissolve
sa "Um, yeah? Alcohol, hello?"
scene ep9_diks_ph2_photo_sage_event6 with dissolve
mc "I'm gonna drink too, so I won't notice."
scene ep9_diks_ph2_photo_sage_event5 with dissolve
sa "But it's not about you noticing it; it's about what's in that camera after the night's over."
sa "I can't tell you how many times I've taken a picture of myself drunk, believing I look good, only to wake up to reality and having to wipe everything from the phone gallery."
scene ep9_diks_ph2_photo_sage_event6 with dissolve
mc "You got a point there."
scene ep9_diks_ph2_photo_sage_event2 with dissolve
sa "Take pictures, already!"
scene ep9_diks_ph2_photo_sage_event3 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_sage_event3 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_photo_sage_event9 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_sage_event9 with dissolve
$ renpy.pause()
scene ep9_diks_ph2_photo_sage_event8 with dissolve
mc "This memory card is gonna be full with your pictures, if I keep going."
scene ep9_diks_ph2_photo_sage_event10 with dissolve
sa "Not likely. Stand next to me for one."
scene ep9_diks_ph2_photo_sage_event11 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone and not branchSage:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
menu:
    "Funny pose":
        $ ep9_photos[10] = True
        mc "Can we do a funny pose?"
        scene ep9_diks_ph2_photo_sage_event12 with dissolve
        sa "Ok. Give me that sword."
        sa "Now, look scared!"
        scene ep9_diks_ph2_photo_sage_event13 with dissolve
        sa "AAARRGGG!!!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sage_event13 with dissolve
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sage_event19 with dissolve
        sa "Haha! Awesome!"
    "Sexy pose [mod_gr][mod_choices[10]]":
        $ ep9_photos[11] = True
        if not branchSage and not branchAlone:
            $ tc += 1
        mc "Should we do something sexy?"
        scene ep9_diks_ph2_photo_sage_event20 with dissolve
        sa "Keep it in your skirt, [name]."
        scene ep9_diks_ph2_photo_sage_event21 with dissolve
        mc "No? What about something funny?"
        scene ep9_diks_ph2_photo_sage_event20 with dissolve
        sa "No, let's try a sexy pose. You wanted it."
        scene ep9_diks_ph2_photo_sage_event14 with dissolve
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sage_event14 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph2_photo_sage_event15 with dissolve
        sa "You're liking this, aren't you?"
        scene ep9_diks_ph2_photo_sage_event16 with dissolve
        if branchSage:
            mc "Don't act like you aren't."
            scene ep9_diks_ph2_photo_sage_event17 with dissolve
            sa "I'm not acting one bit. I love it."
            scene ep9_diks_ph2_photo_sage_event18 with dissolve
            sa "*{i}Smack{/i}*"
        else:
            mc "..."
            scene ep9_diks_ph2_photo_sage_event17 with dissolve
            if branchAlone:
                sa "You're so liking it, you flirt."
            else:
                sa "You're so liking it, you flirt. But we both know you shouldn't."

scene ep9_diks_ph2_photo_sage_event22 with dissolve
sa "Tell more people to take pictures, so it's not just us on that camera when the night's over."
mc "Sure. Can you help me with that?"
sa "Of course!"
$ new_bio("Sage", "I took a picture together with Sage at the Halloween party.")
$ task_list[0] = "Go to the theater"
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_bella_event_label:
scene ep9_diks_ph2_photo_bella_event17 with dissolve
mc "I'm back. I had to greet the guests and whatnot. What are you up to?"
scene ep9_diks_ph2_photo_bella_event18 with dissolve
isa "I'm trying my best to blend in."
scene ep9_diks_ph2_photo_bella_event17 with dissolve
mc "By sitting here alone?"
scene ep9_diks_ph2_photo_bella_event19 with dissolve
isa "I've seen way too many students here that would blow my cover if I talked to them."
scene ep9_diks_ph2_photo_bella_event20 with dissolve
mc "Or so you think. No one's mentioned it so far. Try chatting with someone and you'll see it works."
scene ep9_diks_ph2_photo_bella_event19 with dissolve
isa "I'll let them all drink some more before I give it a try."
scene ep9_diks_ph2_photo_bella_event20 with dissolve
mc "That's not a bad idea."
mc "I'm assuming you didn't approach Jill yet."
scene ep9_diks_ph2_photo_bella_event19 with dissolve
isa "I'm working on it."
scene ep9_diks_ph2_photo_bella_event17 with dissolve
mc "I understand."
mc "Seeing as you're biding your time for stuff... Wanna go take a picture together or maybe dance some?"
scene ep9_diks_ph2_photo_bella_event18 with dissolve
isa "We can take a picture. I'm not sure I will be dancing in this tonight."

scene ep9_diks_ph2_photo_bella_event1 with wipeleft
mc "Make a scary mummy pose for me."
scene ep9_diks_ph2_photo_bella_event2 with dissolve
mc "Um..."
isa "What?"
mc "Can you put some effort into it? It looks like you're sleepwalking."
scene ep9_diks_ph2_photo_bella_event3 with dissolve
isa "Effort... Pff... I'll give you effort."
scene ep9_diks_ph2_photo_bella_event4 with dissolve
mc "Wow! Yes! That's so cool!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_bella_event4 with dissolve
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_bella_event7 with dissolve
mc "Wanna take a picture together?"
scene ep9_diks_ph2_photo_bella_event8 with dissolve
isa "Let's not get carried away with it, considering..."
mc "We won't."
menu:
    "Scary pose":
        $ ep9_photos[2] = True
        mc "Let's make a scary pose together."
        scene ep9_diks_ph2_photo_bella_event9 with dissolve
        isa "How?"
        scene ep9_diks_ph2_photo_bella_event10 with dissolve
        mc "Jump on my back and try to eat me."
        scene ep9_diks_ph2_photo_bella_event11 with dissolve
        isa "Are you sure?"
        scene ep9_diks_ph2_photo_bella_event12 with dissolve
        mc "Yeah, don't worry about it. I've got good core strength."
        scene ep9_diks_ph2_photo_bella_event5 with dissolve
        mc "Ahh! You don't have to bite me!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_bella_event5 with dissolve
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_bella_event13 with dissolve
        isa "I thought you wanted effort."
        mc "Yeah, but damn!"
    "Cute pose":
        $ ep9_photos[3] = True
        mc "But we can still make it cute, somehow."
        scene ep9_diks_ph2_photo_bella_event9 with dissolve
        isa "I thought you wanted me to be a scary mummy. Now I'm a cute one?"
        scene ep9_diks_ph2_photo_bella_event14 with dissolve
        mc "I want a nice picture to remember this party."
        mc "Here, take my sword."
        scene ep9_diks_ph2_photo_bella_event6 with dissolve
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_bella_event6 with dissolve
        $ renpy.pause()
scene ep9_diks_ph2_photo_bella_event15 with dissolve
mc "Well... That should do it. I'll show you when I get the final photos."
scene ep9_diks_ph2_photo_bella_event16 with dissolve
isa "I'll look forward to that, then."
$ new_bio("Isabella", "I took a picture together with Bella at the Halloween party.")
$ currentFreeRoamLabel = "ep9_diks_ph2_lib_right_label"
$ task_list[11] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_riona_event_label:
$ ep9_photos[9] = True
scene ep9_diks_ph2_photo_riona_event1 with dissolve
mc "Rio! Did you take your photo yet?"
scene ep9_diks_ph2_photo_riona_event2 with dissolve
ri "No, but I promised Elena I would."
scene ep9_diks_ph2_photo_riona_event3 with dissolve
mc "Wanna do it now or wait until later?"
scene ep9_diks_ph2_photo_riona_event4 with dissolve
ri "No, I've got time now. Let's do it!"
scene ep9_diks_ph2_photo_riona_event5 with fade
mc "Ok. Pose like a cat for me."
scene ep9_diks_ph2_photo_riona_event6 with dissolve
ri "Haha, how? You want me on all fours or something?"
scene ep9_diks_ph2_photo_riona_event7 with dissolve
mc "Haha! No, standing is best for the photo."
scene ep9_diks_ph2_photo_riona_event8 with dissolve
ri "I've got it. I'll do this."
scene ep9_diks_ph2_photo_riona_event9 with dissolve
mc "Great! Hold that pose."
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_diks_ph2_photo_riona_event9 with dissolve
ri "Done?"
mc "Yep, we got it."
scene ep9_diks_ph2_photo_riona_event10 with dissolve
ri "If it comes out stupid, I'm gonna say I was drunk."
scene ep9_diks_ph2_photo_riona_event11 with dissolve
mc "It won't look stupid, trust me. You looked like a cute cat."
scene ep9_diks_ph2_photo_riona_event12 with dissolve
ri "Awesome! Meow!"
$ new_bio("Riona", "I took a picture of Riona at the Halloween party.")
$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_camila_event_label:
scene ep9_diks_ph2_photo_camila_event6 with dissolve
mc "Camila?"
scene ep9_diks_ph2_photo_camila_event7 with dissolve
cam "Hi, you!"
scene ep9_diks_ph2_photo_camila_event9 with dissolve
mc "Want me to take your Halloween picture?"
scene ep9_diks_ph2_photo_camila_event8 with dissolve
cam "Right! I haven't done that yet. Go ahead."
scene ep9_diks_ph2_photo_camila_event9 with dissolve
mc "The camera is in my room. Come with me."
scene ep9_diks_ph2_photo_camila_event1 with fade
cam "Which pose should I go for?"
scene ep9_diks_ph2_photo_camila_event2 with dissolve
cam "The stern and smart look...?"
scene ep9_diks_ph2_photo_camila_event3 with dissolve
cam "...or the flirty look?"
scene ep9_diks_ph2_photo_camila_event1 with dissolve
menu:
    "Stern and smart look":
        $ ep9_photos[0] = True
        mc "I liked the stern and smart look. It suits your costume the best."
        scene ep9_diks_ph2_photo_camila_event2 with dissolve
        cam "Hmph."
        mc "Great, keep that pose."
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_camila_event2 with dissolve
        $ renpy.pause(0.5)
    "Flirty look":
        $ ep9_photos[1] = True
        mc "Definitely the flirty look. It will look great as a picture."
        scene ep9_diks_ph2_photo_camila_event3 with dissolve
        cam "*{i}Mwah{/i}*"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_camila_event3 with dissolve
        $ renpy.pause(0.5)
mc "Nailed it!"
scene ep9_diks_ph2_photo_camila_event4 with dissolve
cam "Thanks, [name]. I can't wait to see the pictures!"
scene ep9_diks_ph2_photo_camila_event5 with dissolve
mc "Me neither. If you see people who haven't gotten their pictures taken yet, let them know about this, ok?"
scene ep9_diks_ph2_photo_camila_event4 with dissolve
cam "Yes, sir."
$ new_bio("Camila", "I took a picture of Camila at the Halloween party.")
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_photo_sarah_mel_event_label:
$ guideSuggestedPage = 67
mc "Before I forget... There's a camera in my room if you want your picture taken for Halloween."
scene ep9_diks_ph2_sarah3_event6 with dissolve
sar "Let's bring Mel for that picture, too."
scene ep9_diks_ph2_sarah3_event7 with dissolve
mc "Sure."
scene ep9_diks_ph2_photo_sarah_event1 with fade
mc "What pose are you going for?"
scene ep9_diks_ph2_photo_sarah_event2 with dissolve
sar "I thought it was the photographer who was supposed to direct their subjects."
scene ep9_diks_ph2_photo_sarah_event3 with dissolve
mc "I'm happy with whatever you'll give me."
scene ep9_diks_ph2_photo_sarah_event4 with dissolve
ml "What a lame answer."
scene ep9_diks_ph2_photo_sarah_event3 with dissolve
menu:
    "Something sexy":
        $ ep9_photos[12] = True
        mc "Do something sexy, then."
        scene ep9_diks_ph2_photo_sarah_event5 with dissolve
        ml "Like this?"
        sar "Do we look fuckable, [name]?"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sarah_event5 with dissolve
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sarah_event7 with dissolve
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
        menu:
            "Yes [mod_gr][mod_choices[3]]":
                $ dk(1)
                mc "Yeah, very fuckable."
                scene ep9_diks_ph2_photo_sarah_event8 with dissolve
                sar "Awesome."
            "Looks good [mod_gr][mod_choices[2]]":
                $ dk(-1)
                mc "You look very good."
                scene ep9_diks_ph2_photo_sarah_event8 with dissolve
                sar "Awesome."
            "Not to me [mod_gr][mod_choices[3]]":
                $ dk(1)
                mc "Probably to someone, but not to me."
                scene ep9_diks_ph2_photo_sarah_event9 with dissolve
                ml "What an ass."
                sar "Yeah, I don't believe him, though."
    "Something cute":
        $ ep9_photos[13] = True
        mc "Pose in a cute way for the camera, then."
        scene ep9_diks_ph2_photo_sarah_event10 with dissolve
        ml "Cute? Hm..."
        scene ep9_diks_ph2_photo_sarah_event6 with dissolve
        sar "I suppose we can do it like this."
        mc "Looks great."
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep9_diks_ph2_photo_sarah_event6 with dissolve
        $ renpy.pause(0.5)
scene ep9_diks_ph2_photo_sarah_event11 with dissolve
mc "Thanks so much."
scene ep9_diks_ph2_photo_sarah_event12 with dissolve
ml "Wanna take a picture with us?"
scene ep9_diks_ph2_photo_sarah_event11 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
menu:
    "[mod_gr]Sure":
        mc "Sure. An odd combination, but let's do it."
        scene ep9_diks_ph2_photo_sarah_event13 with dissolve
        mc "Let's do it like this..."
        menu:
            "Grab their asses ({color=#ffffff}{size=-1}{font=fonts/collegiate.ttf}DIK{/font}{/size} affinity{/color}) [mod_gr][mod_choices[10]]" if affinity == "DIK":
                if not branchAlone:
                    $ tc += 1
                $ ep9_photos[16] = True
                scene ep9_diks_ph2_photo_sarah_event16 with dissolve
                sar "Easy there, haha."
                scene ep9_diks_ph2_photo_sarah_event17 with dissolve
                ml "Told you our asses would look irresistible in these outfits."
                scene ep9_diks_ph2_photo_sarah_event18 with dissolve
                mc "It's for the picture."
                sar "Sure."
                scene ep9_diks_ph2_photo_sarah_event15 with dissolve
                scene white
                play sound "sound_effects/camera_shutter.mp3"
                $ renpy.pause(0.5)
                scene ep9_diks_ph2_photo_sarah_event15 with dissolve
                $ renpy.pause()
            "Hold up sword":
                $ ep9_photos[17] = True
                scene ep9_diks_ph2_photo_sarah_event14 with dissolve
                scene white
                play sound "sound_effects/camera_shutter.mp3"
                $ renpy.pause(0.5)
                scene ep9_diks_ph2_photo_sarah_event14 with dissolve
                $ renpy.pause()
        scene ep9_diks_ph2_photo_sarah_event19 with dissolve
        ml "Back to the dance floor."
        mc "Thanks, girls."
        sar "Any time."
        $ new_bio("Sarah", "I took a picture together with Sarah and Melanie at the Halloween party.")
        $ new_bio("Melanie", "I took a picture together with Sarah and Melanie at the Halloween party.")
    "No thanks":
        mc "No thanks, I'm good."
        scene ep9_diks_ph2_photo_sarah_event12 with dissolve
        ml "All right. Back to the dance floor!"
        $ new_bio("Sarah", "I took a picture of Sarah and Melanie at the Halloween party.")
        $ new_bio("Melanie", "I took a picture of Sarah and Melanie at the Halloween party.")
$ optional_task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph2_mains_event_label:
scene ep9_diks_ph2_mains_event1 with dissolve
ti "WOOO!!!"
js "This party is...wild!"
scene ep9_diks_ph2_mains_event2 with dissolve
my "Yeah, and there are so many people here!"
scene ep9_diks_ph2_mains_event6 with dissolve
sa "It's good, huh?"
scene ep9_diks_ph2_mains_event7 with dissolve
sa "To me, it's already got last year's party beat."
scene ep9_diks_ph2_mains_event7b with dissolve
sa "And not just because the HOTs aren't all dressed the same..."
scene ep9_diks_ph2_mains_event8 with dissolve
sa "Um... No offense to you two, of course."
sa "Theme costumes are one thing, but identical ones get a bit boring."
scene ep9_diks_ph2_mains_event9 with dissolve
js "Well, I guess we chose similar ones by accident... Officially."
scene ep9_diks_ph2_mains_event10 with dissolve
sa "What are you doing?"
scene ep9_diks_ph2_mains_event11 with dissolve
js "Nothing..."

scene ep9_diks_ph2_mains_event12 with dissolve
sa "So... Maya? Did you think more about my proposition?"
scene ep9_diks_ph2_mains_event3 with dissolve
my "Which one?"
scene ep9_diks_ph2_mains_event12 with dissolve
sa "Joining the HOTs."
scene ep9_diks_ph2_mains_event3 with dissolve
my "Oh? Yes, I have. And it's like this..."
my "I think my dad would hate it if I joined the HOT sorority."
scene ep9_diks_ph2_mains_event13 with dissolve
sa "Come on, Maya! Don't let that stop you. I thought you would change your mind on this."
scene ep9_diks_ph2_mains_event4 with dissolve
my "Let me finish... But dad never said I couldn't join. So, I've decided I'm gonna do it."
scene ep9_diks_ph2_mains_event3 with dissolve
my "Being part of a sorority can only be beneficial for my future, right?"
scene ep9_diks_ph2_mains_event14 with dissolve
sa "You rebel! That's amazing!"
scene ep9_diks_ph2_mains_event3 with dissolve
my "I think it would be good for me. Everyone I've talked to about it seems to point that out."
scene ep9_diks_ph2_mains_event15 with dissolve
js "It would."

scene ep9_diks_ph2_mains_event14 with dissolve
sa "That's amazing. I didn't even have to play my Becky card to win you over."
scene ep9_diks_ph2_mains_event5 with dissolve
my "Your what?"
if branchIsabella:
    scene ep9_diks_ph2_mains_event16 with dissolve
else:
    scene ep9_diks_ph2_mains_event16b with dissolve
sa "An annoying little bird whispered that you had already joined us. She went on about how you weren't cool in high school and yada yada yada."
scene ep9_diks_ph2_mains_event5 with dissolve
my "About that... I may have mentioned my HOT outfit to shut her up. I hope I didn't cause a problem."
scene ep9_diks_ph2_mains_event14 with dissolve
sa "Nah, everyone knows that Becky gossips a lot. You can't trust half of the stuff she says."
sa "But enough about her... Welcome, sister! For real, this time!"
scene ep9_diks_ph2_mains_event3 with dissolve
my "Thanks!"
scene ep9_diks_ph2_mains_event15 with dissolve
js "Finally."
scene ep9_diks_ph2_mains_event14 with dissolve
sa "I'll make sure we'll do some proper welcoming for you later, ok?"
scene ep9_diks_ph2_mains_event3 with dissolve
my "You don't have to do that; I was at the ceremony. I don't want any special treatment."
scene ep9_diks_ph2_mains_event14 with dissolve
sa "Nope. It's gonna happen."

if branchIsabella:
    scene ep9_diks_ph2_mains_event17 with dissolve
else:
    scene ep9_diks_ph2_mains_event17b with dissolve
sa "Looks like we've got company. Are you enjoying our conversation or what?"
isa "Me? No."
if branchIsabella:
    scene ep9_diks_ph2_mains_event18 with dissolve
    js "Wow! You have a very cool costume!"
    scene ep9_diks_ph2_mains_event19 with dissolve
    isa "Thank you... Likewise."
else:
    scene ep9_diks_ph2_mains_event18b with dissolve
    js "Isn't that the DIKs' costume?"
    scene ep9_diks_ph2_mains_event17b with dissolve
    isa "No."
if branchIsabella:
    scene ep9_diks_ph2_mains_event20 with dissolve
else:
    scene ep9_diks_ph2_mains_event20b with dissolve
sa "Isabella?"
if branchIsabella:
    scene ep9_diks_ph2_mains_event21 with dissolve
else:
    scene ep9_diks_ph2_mains_event21b with dissolve
sa "Wait! Don't walk away."
sa "It's you, isn't it?"
isa "No."
if branchIsabella:
    scene ep9_diks_ph2_mains_event22 with dissolve
else:
    scene ep9_diks_ph2_mains_event22b with dissolve
sa "Right. I've worked next to you for weeks. I recognize your voice, tone and catchphrase by now."
if branchIsabella:
    scene ep9_diks_ph2_mains_event23 with dissolve
else:
    scene ep9_diks_ph2_mains_event23b with dissolve
isa "My catchphrase?"
if branchIsabella:
    scene ep9_diks_ph2_mains_event22 with dissolve
    sa "\"No\"."
else:
    scene ep9_diks_ph2_mains_event22b with dissolve
    sa "\"No\"."
    sa "Also, aside from the mask you clearly borrowed from the DIKs, I've seen you wear that outfit before."
if branchIsabella:
    scene ep9_diks_ph2_mains_event23 with dissolve
else:
    scene ep9_diks_ph2_mains_event23b with dissolve
isa "Please, don't bring any attention to me. I'll be leaving now."
if branchIsabella:
    scene ep9_diks_ph2_mains_event22 with dissolve
else:
    scene ep9_diks_ph2_mains_event22b with dissolve
sa "You don't have to do that. Come sit with us over here. It's cool."
if branchIsabella:
    scene ep9_diks_ph2_mains_event24 with dissolve
    js "Is it really you? Wow, I never would have guessed. That costume is so good!"
else:
    scene ep9_diks_ph2_mains_event24b with dissolve
    js "Is it really you? If I wasn't drunk, maybe I would have guessed."
if branchIsabella:
    scene ep9_diks_ph2_mains_event29 with dissolve
else:
    scene ep9_diks_ph2_mains_event29b with dissolve
isa "I'm not supposed to be at your parties, but..."
if branchIsabella:
    scene ep9_diks_ph2_mains_event24 with dissolve
else:
    scene ep9_diks_ph2_mains_event24b with dissolve
js "We get it. Jill must have invited you, right?"

if branchIsabella:
    scene ep9_diks_ph2_mains_event25 with dissolve
    $ renpy.pause()

scene ep9_diks_ph2_mains_event26 with dissolve
sa "Wait a minute; you're drinking too!?"
if branchIsabella:
    scene ep9_diks_ph2_mains_event29 with dissolve
else:
    scene ep9_diks_ph2_mains_event29b with dissolve
isa "This was a mistake."

scene ep9_diks_ph2_mains_event26 with dissolve
sa "No, stop! This makes me like you way more!"
scene ep9_diks_ph2_mains_event27 with dissolve
sa "I mean, I already kinda did, but now I definitely do."

if branchIsabella:
    scene ep9_diks_ph2_mains_event28b with dissolve
else:
    scene ep9_diks_ph2_mains_event28 with dissolve
$ renpy.pause()

scene ep9_diks_ph2_mains_event27 with dissolve
sa "Haha! Yes! Cheers!"
scene ep9_diks_ph2_mains_event26 with dissolve
sa "We should do shots!"

$ event_list.append("ep9_diks_ph2_end_event_label")
$ optional_task_list[4] = ""
if "ep9_diks_ph2_sarah_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_sarah_event_label")
if "ep9_diks_ph2_sarah2_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_sarah2_event_label")
if "ep9_diks_ph2_sarah3_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_sarah3_event_label")
jump endEvent

label ep9_diks_ph2_bmains_event_label:
$ mphone_music_genre = 2
stop music fadeout 3
if not branchIsabella:
    if branchJill:
        scene ep9_diks_ph2_bmains_event1 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event1b with dissolve
    ji "Bella! You came!"
    $ mphone_play_songs(["music/ep9/licensed_music/track127.mp3"])
    if branchJill:
        scene ep9_diks_ph2_bmains_event9 with dissolve
        isa "Haha! Your costume is amazing, Jill."
        scene ep9_diks_ph2_bmains_event10 with dissolve
        ji "Do you think so? It's not incredibly stupid?"
        scene ep9_diks_ph2_bmains_event6 with dissolve
        isa "Can it be both?"
        scene ep9_diks_ph2_bmains_event11 with dissolve
        ji "Haha! Thanks for your honesty."
    else:
        scene ep9_diks_ph2_bmains_event2 with dissolve
        isa "What a fun costume!"
        scene ep9_diks_ph2_bmains_event3 with dissolve
        ji "Thank you! I'm a bee and this is my stinger."
        scene ep9_diks_ph2_bmains_event5 with dissolve
        isa "Bees are evolving. It's the first time I've seen a bee carry its stinger."
        scene ep9_diks_ph2_bmains_event4 with dissolve
        ji "I wasn't going to attach it to my butt."
        scene ep9_diks_ph2_bmains_event5 with dissolve
        isa "You're looking very pretty tonight. One might even say you're bee-autiful."
        scene ep9_diks_ph2_bmains_event12 with dissolve
        ji "Aw! Haha! Thanks."

    scene ep9_diks_ph2_bmains_event5 with dissolve
    isa "How is the party? Are you having fun?"
    if branchJill:
        scene ep9_diks_ph2_bmains_event13 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event13b with dissolve
    ji "There are so many people here and I'm not sure I recognize most."
    ji "But I'm having a good time. Right now, anything is better than being forced to attend the High Society Halloween party."
    if ep9_jill_mood == 1:
        scene ep9_diks_ph2_bmains_event14 with dissolve
        ji "Even if \"he\" is here... This was a good choice."
        scene ep9_diks_ph2_bmains_event7 with dissolve
        isa "How do you feel about it?"
        scene ep9_diks_ph2_bmains_event14 with dissolve
        ji "It's a struggle... But I can't avoid him forever, right?"

    scene ep9_diks_ph2_bmains_event5 with dissolve
    if ep9_jill_mood == 1:
        isa "I think it's good that you came here. Enjoy yourself tonight."
    else:
        isa "That's good. Enjoy yourself tonight."
    if branchJill:
        scene ep9_diks_ph2_bmains_event13 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event13b with dissolve
    ji "Can't you come inside with me? Please?"
    ji "I so want you to be with my friends and me tonight."

    scene ep9_diks_ph2_bmains_event7 with dissolve
    isa "I believe I already told you why I can't."
    if branchJill:
        scene ep9_diks_ph2_bmains_event13 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event13b with dissolve
    ji "What if I find you something to wear?"
    ji "Come on, Bella! You're already here!"
    scene ep9_diks_ph2_bmains_event7 with dissolve
    isa "Does it mean that much to you?"
    if branchJill:
        scene ep9_diks_ph2_bmains_event13 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event13b with dissolve
    ji "It would make my night, yes."

    scene ep9_diks_ph2_bmains_event8 with dissolve
    isa "One drink! But only if you can find me a good enough mask."
    if branchJill:
        scene ep9_diks_ph2_bmains_event15 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event15b with dissolve
    ji "I'll find something for you really quick!"

    if branchJill:
        scene ep9_diks_ph2_bmains_event16 with wiperight
    else:
        scene ep9_diks_ph2_bmains_event16b with wiperight
    isa "This mask smells awful. Where did you get it?"
    if branchJill:
        scene ep9_diks_ph2_bmains_event17 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event17b with dissolve
    bia "It was hanging on the wall, haha! I asked someone if I could borrow it and they said it was ok."
    if branchJill:
        scene ep9_diks_ph2_bmains_event18 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event18b with dissolve
    ji "Are you coming, Bianca?"
    scene ep9_diks_ph2_bmains_event21 with dissolve
    bia "I'll be with you in a second, I'm trying to find Matty. I lost him a while back."
    if branchJill:
        scene ep9_diks_ph2_bmains_event19 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event19b with dissolve
    ji "Need help?"
    scene ep9_diks_ph2_bmains_event21 with dissolve
    bia "Can you?"
    if branchJill:
        scene ep9_diks_ph2_bmains_event20 with dissolve
    else:
        scene ep9_diks_ph2_bmains_event20b with dissolve
    ji "It will just be a second. Can you wait for me up there by the sofas?"
    isa "I'll try to...blend in."

    scene ep9_diks_ph2_bmains_event22 with dissolve
    le "Whoa... Look! Big-titty Diablo. Heather's kinky tonight."

jump ep9_diks_ph2_mains_event_label

label ep9_diks_ph2_mains2_event_label:
scene ep9_diks_ph2_mains2_event1 with dissolve
sa "[name]! We're doing shots! Wanna join us?"
scene ep9_diks_ph2_mains2_event2 with dissolve
mc "Shots? No, thanks... I'm...good."
if branchIsabella:
    scene ep9_diks_ph2_mains2_event3 with dissolve
    isa "They figured out it's me."
    scene ep9_diks_ph2_mains2_event9 with dissolve
    js "[name] knew?"
    my "Haha! Of course, he did!"
else:
    scene ep9_diks_ph2_mains2_event4 with dissolve
    mc "Um... Bella? You're here?"
    scene ep9_diks_ph2_mains2_event5 with dissolve
    isa "*{i}Sigh{/i}* I didn't even say anything. How did you know it was me?"
    if affinity == "DIK":
        mc "I can't answer that without offending you."
    else:
        mc "Um... Your aura, I guess."
    mc "But it's great that you're here. I would have invited you if I knew you'd be up for it."
    scene ep9_diks_ph2_mains2_event4 with dissolve
    isa "Jill convinced me to drop by."


scene ep9_diks_ph2_mains2_event13 with dissolve
mc "So, you're all drinking and having a good time, then?"

scene ep9_diks_ph2_mains2_event10 with dissolve
my "Yup! We convinced Bella to play truth or drink."
scene ep9_diks_ph2_mains2_event11 with dissolve
mc "What's that?"
scene ep9_diks_ph2_mains2_event12 with dissolve
js "You ask someone a question and if they don't wanna answer, they have to drink."

scene ep9_diks_ph2_mains2_event14 with dissolve
sa "And Bella would sure rather drink than tell us the truth."
js "Hahaha!"
if branchIsabella:
    scene ep9_diks_ph2_mains2_event6b with dissolve
else:
    scene ep9_diks_ph2_mains2_event6 with dissolve
isa "Hahaha!"
$ guideSuggestedPage = 72
scene ep9_diks_ph2_mains2_event15 with dissolve
sa "[name]! Did you select that costume knowing that girls would check out your hot body?"
sa "Truth or drink!"
scene ep9_diks_ph2_mains2_event16 with dissolve
menu:
    "Truth":
        mc "I mean, I... Maybe a little bit?"
        scene ep9_diks_ph2_mains2_event17 with dissolve
        js "Hahaha!"
        my "Haha! You got him to admit it!"
        sa "Haha! I know!"
    "Drink":
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event18 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event18b with dissolve
        "Hahaha!"
        js "He SO did!"

scene ep9_diks_ph2_mains2_event19 with dissolve
sa "Now it's your turn!"
scene ep9_diks_ph2_mains2_event16 with dissolve
menu:
    "Ask Bella":
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event7 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event4 with dissolve
        mc "Bella! Who are your top three students in our class?"
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event8 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event5 with dissolve
        isa "Ok, this one I'll answer."
        scene ep9_diks_ph2_mains2_event20 with dissolve
        my "Haha! No way? You will?"
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event8 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event4 with dissolve
        isa "I can't...drink more. Haha!"
        isa "Without any order..."
        isa "Ashley, Lily and Derek."
        scene ep9_diks_ph2_mains2_event20 with dissolve
        my "Wait, what!? Explain!"
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event8 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event5 with dissolve
        isa "That wasn't part of the question."
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event7 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event4 with dissolve
        mc "I didn't even make the cut? It's supposed to be truth, no?"

        if branchIsabella:
            scene ep9_diks_ph2_mains2_event21 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event21b with dissolve
        isa "My turn."
        isa "Josy. What is the wildest thing you've done in college so far?"

        scene ep9_diks_ph2_mains2_event22 with dissolve
        isa "Aha. I believe I found the button to push to make you drink."
        sa "Hahaha! So busted!!!"
        scene ep9_diks_ph2_mains2_event23 with dissolve
        js "That was like the first time I drank anyway. We're running out of shots because of Bella."
        "Hahaha!"
    "[mod_gr]Ask Josy":
        scene ep9_diks_ph2_mains2_event24 with dissolve
        mc "Josy! Make out with Sage."
        scene ep9_diks_ph2_mains2_event25 with dissolve
        js "It's not truth or dare, [name]. It's truth or drink."
        scene ep9_diks_ph2_mains2_event26 with dissolve
        my "Wow!"
        scene ep9_diks_ph2_mains2_event27 with dissolve
        sa "*{i}Smack{/i}*"
        scene ep9_diks_ph2_mains2_event28 with dissolve
        sa "Mmm! Lipgloss?"
        js "Strawberry."
        sa "Very nice!"
    "Ask Maya":
        scene ep9_diks_ph2_mains2_event29 with dissolve
        mc "Maya! Name someone you masturbate to."
        js "Haha! Oh my God!"
        sa "[name] is swinging hard!"
        scene ep9_diks_ph2_mains2_event30 with dissolve
        my "Cheers! Because you'll never know."
        js "Haha! Come on!!!"
        scene ep9_diks_ph2_mains2_event31 with dissolve
        my "Like you wouldn't drink?"
        my "Actually... Josy! Name someone {b}you{/b} masturbate to!"
        scene ep9_diks_ph2_mains2_event32 with dissolve
        my "And look at you drinking. Haha!"
    "Ask Sage":
        mc "Did you pick {b}your{/b} outfit, knowing that guys would check out your hot body?"
        scene ep9_diks_ph2_mains2_event33 with dissolve
        sa "Guilty as charged!"
        scene ep9_diks_ph2_mains2_event34 with dissolve
        mc "You're not even embarrassed about it..."
        scene ep9_diks_ph2_mains2_event33 with dissolve
        sa "That's right, you wasted your question on me."
        scene ep9_diks_ph2_mains2_event35 with dissolve
        sa "Josy! Out of the rest of the HOTs not here right now..."
        sa "Who would you rather make out with if you had to?"
        sa "And don't you dare drink!"
        scene ep9_diks_ph2_mains2_event36 with dissolve
        js "If I had to?"
        js "Damn you..."
        js "Lily? Maybe?"
        scene ep9_diks_ph2_mains2_event37 with dissolve
        sa "Oh!!! Interesting!"
        my "Why Lily?"
        scene ep9_diks_ph2_mains2_event36 with dissolve
        js "Remember during that spin the dildo game we played? She made out with Ashley and it looked like she knew how to kiss."
        js "So, why not make it a good kiss if I had to pick one?"
        if branchIsabella:
            scene ep9_diks_ph2_mains2_event21 with dissolve
        else:
            scene ep9_diks_ph2_mains2_event21b with dissolve
        isa "Spin the dildo? Do I even want to know?"
        js "Probably not."

scene ep9_diks_ph2_mains2_event38 with dissolve
js "[name]. Is it true that your ex-girlfriend is at the party?"
scene ep9_diks_ph2_mains2_event39 with dissolve
mc "What?"
scene ep9_diks_ph2_mains2_event40 with dissolve
my "Yeah, I wanna know that too. Derek told us he was gonna interrogate your ex."
scene ep9_diks_ph2_mains2_event41 with dissolve
mc "Um..."
$ new_bio("Isabella", "Bella played drinking games together with Josy, Maya, and Sage.")
jump ep9_pre_blackout_label

label ep9_ph2_bella_jill_event_label:
if not branchJill:
    scene ep9_ph2_bella_jill_event1 with dissolve
    isa "Hi..."
    scene ep9_ph2_bella_jill_event2 with dissolve
    ji "Hi! Uh..."
    scene ep9_ph2_bella_jill_event3 with dissolve
    ji "Oh... Bella...?"
    scene ep9_ph2_bella_jill_event7 with dissolve
    isa "Can we talk?"
    scene ep9_ph2_bella_jill_event3 with dissolve
    ji "You came here to talk?"
    scene ep9_ph2_bella_jill_event8 with dissolve
    isa "..."
    scene ep9_ph2_bella_jill_event3 with dissolve
    ji "Of course, you didn't... You came here for him..."
    scene ep9_ph2_bella_jill_event7 with dissolve
    isa "Not only for him. I was hoping that you'd show up."
    isa "It feels like I'm losing my best friend."
    if ep9_jill_mood == 3:
        scene ep9_ph2_bella_jill_event4 with dissolve
        ji "..."
        scene ep9_ph2_bella_jill_event5 with dissolve
        ji "I'm here with my friends for the party. I don't have the strength to deal with this tonight."
        scene ep9_ph2_bella_jill_event6 with dissolve
        ji "The truth is..."
        ji "I can't even look at you. Because every time I do, all I see is him."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "If I lose you because of this, every moment I will spend with him will remind me of you."
        isa "Please, Jill..."
        isa "Can I do something? Anything?"
        scene ep9_ph2_bella_jill_event4 with dissolve
        ji "..."
        scene ep9_ph2_bella_jill_event6 with dissolve
        ji "You can give me space and stop writing me every day."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "Is that going to make things better? It feels like that's only going to make us drift apart."
        scene ep9_ph2_bella_jill_event5 with dissolve
        ji "You constantly writing me will push me away too."
        ji "Please, give me space."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "If that's what you want... Just know that I'm here for you."
    else:
        scene ep9_ph2_bella_jill_event3 with dissolve
        ji "I'm trying to move past this, but it's hard. I need time..."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "Talk to me about it. What's bothering you the most?"
        scene ep9_ph2_bella_jill_event4 with dissolve
        ji "..."
        scene ep9_ph2_bella_jill_event3 with dissolve
        ji "I think it's the lack of honesty. I don't understand it."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "I'm so sorry about it, and you have to believe me when I say that I was going to tell you before you found out."
        scene ep9_ph2_bella_jill_event3 with dissolve
        ji "Why not earlier than that?"
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "It was too hard to admit it."
        isa "I felt like I've been cheating."
        scene ep9_ph2_bella_jill_event5 with dissolve
        ji "Bella..."
        scene ep9_ph2_bella_jill_event9 with dissolve
        isa "It's how I felt about it. I felt ashamed. And dirty. So, I kept those thoughts my secrets."
        isa "I've felt I don't have much dignity left. I didn't want to admit this to you."
        scene ep9_ph2_bella_jill_event4 with dissolve
        ji "..."
        scene ep9_ph2_bella_jill_event5 with dissolve
        ji "I need some space to process all of this."
        ji "But tonight, I'm here with my friends for the party."
        scene ep9_ph2_bella_jill_event7 with dissolve
        isa "Take all the time you need. But I'm not leaving your side."
    scene ep9_ph2_bella_jill_event10 with dissolve
$ renpy.pause()
if persistent.mod_wtenabled:
    
    if wt_ep9_branch_numbers > 1:
        $ task_list[3] = task_list[3]+"\n Dance with Bella (Tommy's room)"
    else:
        $ task_list[3] = "Dance with Bella (Tommy's room)"
else:
    $ task_list[3] = "Dance with Bella"
    if wt_ep9_branch_numbers > 1:
        $ task_list[3] = task_list[3]+"\n Dance with Bella"
    else:
        $ task_list[3] = "Dance with Bella"
$ task_list[12] = ""
$ event_list.append("ep9_isabella_dance_label")
jump endEvent

label ep9_ph2_josy_event_label:
$task_list[3]=""
$ guideSuggestedPage = 70
scene ep9_ph2_josy_event1 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event2 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event3 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event4 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event5 with dissolve
menu:
    "Are you ok?":
        mc "Josy? Are you ok?"
        scene ep9_ph2_josy_event6 with dissolve
        js "Huh? Yeah."
        scene ep9_ph2_josy_event5 with dissolve
        mc "You look annoyed."
        scene ep9_ph2_josy_event6 with dissolve
        js "That guy's an asshole."
    "What happened?":
        mc "Josy? What happened?"
        scene ep9_ph2_josy_event6 with dissolve
        js "That guy's an asshole. That's what happened."
    "Want me to kill him?":
        mc "Give me the word and I'll kill him for you."
        scene ep9_ph2_josy_event6 with dissolve
        js "You don't have to kill him. But I wouldn't say no to you punching him."
        scene ep9_ph2_josy_event5 with dissolve
        mc "What happened?"
        scene ep9_ph2_josy_event6 with dissolve
        js "That guy's an asshole. That's what happened."
js "We were chatting and I got the sense he was trying to flirt with me."
scene ep9_ph2_josy_event7 with dissolve
mc "Let me guess. You told him no and he didn't like that?"
scene ep9_ph2_josy_event8 with dissolve
js "Almost."
js "He asked me a lot about myself before that, pretending to be interested. Like, you know, hobbies and whatnot?"
scene ep9_ph2_josy_event7 with dissolve
mc "And?"
scene ep9_ph2_josy_event8 with dissolve
js "I was friendly and told him what I like to do, and after I dismissed his advances, he called me a run-of-the-mill boring and basic bitch."
scene ep9_ph2_josy_event7 with dissolve
mc "What an asshole."
scene ep9_ph2_josy_event8 with dissolve
js "Yeah."
scene ep9_ph2_josy_event7 with dissolve
$ mc_info = ["Punch him","ep9_josy_punch_label","Throw him out","ep9_josy_throw_label","Comfort Josy","ep9_josy_comfort_label",(ep2FoughtJocks or ep5_agitatedCaleb or ep6_foughtTommy)]
show screen major_choice_screen
$ renpy.pause()

label ep9_josy_punch_label:
$ event_list.append("oscar_block")
if "ep9_diks_ph2_photo_riona_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_photo_riona_event_label")
$ optional_task_list[2] = ""
$ updateTaskList()
$ ep9_josy_choice = "DIK"
mc "Let me handle this."
scene ep9_ph2_josy_event15 with dissolve
js "What are you doing?"

scene ep9_ph2_josy_event16 with dissolve
mc "Hey!"
play sound "sound_effects/hit.mp3"
scene ep9_ph2_josy_event18 with hpunch
"*{i}Gasps{/i}*"
scene ep9_ph2_josy_event19 with dissolve
osc "What the fuck are you doing?"
scene ep9_ph2_josy_event20 with dissolve
mc "Call my friend a bitch again and I'm gonna make you my bitch, you hear that?"
scene ep9_ph2_josy_event19 with dissolve
osc "Dude, what the hell...?"
scene ep9_ph2_josy_event20 with dissolve
mc "That doesn't sound like a lesson learned to me."
scene ep9_ph2_josy_event19 with dissolve
osc "Yeah... I got it."
scene ep9_ph2_josy_event21 with dissolve
mc "Good, get the fuck out of here!"
js "[name]... Calm down."
scene ep9_ph2_josy_event22 with dissolve
zo "Listen to the fairy. This isn't you, [name]. What's wrong?"
mc "I'm calm."
js "You're not. You punched him."
scene ep9_ph2_josy_event22b with dissolve
tm "What the fuck happened?"
scene ep9_ph2_josy_event23 with dissolve
gi "[name] punched Oscar. Like, what the fuck!?"
scene ep9_ph2_josy_event23b with dissolve
mc "He was rude and tried to get with your sister and then called her a bitch."
scene ep9_ph2_josy_event24 with dissolve
tm "Where is he now?"
gi "He left."
scene ep9_ph2_josy_event25 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event26 with dissolve
js "Thanks for sticking up for me... Are you ok?"
scene ep9_ph2_josy_event27 with dissolve
mc "Yeah, but that pissed me off... Let's not ruin the party over this."
scene ep9_ph2_josy_event28 with dissolve
js "No one can tell you that you're not in character for your costume."
mc "Spartans always hated bank robbers, didn't they?"
js "Oh, yes! Bank robbers were the worst for them."

if ep9_sally_drink:
    $ task_list[13] = "Check Right hallway"
    $ event_list.append("ep9_diks_ph2_sally_event_label")
else:
    $ task_list[13] = ""
$ updateTaskList()
$ new_bio("You", "I punched Oscar after he insulted Josy at the Halloween party.")
jump endEvent

label ep9_josy_throw_label:
$ event_list.append("oscar_block")
if "ep9_diks_ph2_photo_riona_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph2_photo_riona_event_label")
$ optional_task_list[2] = ""
$ updateTaskList()
$ ep9_josy_choice = "NEUTRAL"
mc "Let me handle this."
scene ep9_ph2_josy_event15b with dissolve
js "What are you doing?"
scene ep9_ph2_josy_event17 with dissolve
mc "Hey, you!"
osc "Yeah?"
scene ep9_ph2_josy_event29 with dissolve
mc "You've got some nerve insulting my friend and calling her bitch to her face. What kind of an asshole does that?"
scene ep9_ph2_josy_event30 with dissolve
osc "Dude, whatever... What are you? Her babysitter? Leave me alone."
scene ep9_ph2_josy_event29 with dissolve
mc "No, it's not fucking whatever. You come to our house and act like an ass, we're not having any of that."
mc "You're gone. Out! Leave!"
scene ep9_ph2_josy_event30 with dissolve
osc "Just because I called some skank a bitch?"
play sound "sound_effects/shove.mp3"
scene ep9_ph2_josy_event31 with hpunch
$ renpy.pause()
scene ep9_ph2_josy_event31b with dissolve
osc "Are you for real?"
mc "You wanna find out?"
scene ep9_ph2_josy_event21 with dissolve
mc "Get the fuck out!"
js "[name]... Calm down."
scene ep9_ph2_josy_event22 with dissolve
zo "Listen to the fairy. What's wrong?"
mc "I'm calm."
scene ep9_ph2_josy_event22b with dissolve
tm "What the fuck happened?"
scene ep9_ph2_josy_event23 with dissolve
gi "[name] shoved Oscar and made him leave. Like, what the fuck!?"
scene ep9_ph2_josy_event23b with dissolve
mc "He was rude and tried to get with your sister and then called her a bitch."
scene ep9_ph2_josy_event24 with dissolve
tm "Where is he now?"
gi "He left."
scene ep9_ph2_josy_event25 with dissolve
$ renpy.pause()
scene ep9_ph2_josy_event26 with dissolve
js "Thanks for sticking up for me. You didn't have to do that."
scene ep9_ph2_josy_event27 with dissolve
mc "No one should treat you that way. You deserve better."
scene ep9_ph2_josy_event28 with dissolve
js "No one can tell you that you're not in character for your costume."
mc "Spartans always hated bank robbers, didn't they?"
js "Oh, yes! Bank robbers were the worst for them."
if ep9_sally_drink:
    $ task_list[13] = "Check Right hallway"
    $ event_list.append("ep9_diks_ph2_sally_event_label")
else:
    $ task_list[13] = ""
$ updateTaskList()
$ new_bio("You", "I made Oscar leave after he insulted Josy at the Halloween party.")
jump endEvent

label ep9_josy_comfort_label:
$ ep9_josy_choice = "CHICK"

scene ep9_ph2_josy_event9 with dissolve
mc "Some guys are like that. They can't handle rejection, so they lash out to feel like they are in control."
scene ep9_ph2_josy_event10 with dissolve
js "Yeah, I know. It's pathetic, really."
scene ep9_ph2_josy_event11 with dissolve
mc "Exactly. You deserve to be treated better. Let's ignore him."
scene ep9_ph2_josy_event10 with dissolve
js "It's so annoying."
scene ep9_ph2_josy_event11 with dissolve
mc "You're a fairy, a magical being. How's that basic?"
scene ep9_ph2_josy_event12 with dissolve
js "Right! And he's a bank robber. One of the worst things you can be."
scene ep9_ph2_josy_event13 with dissolve
mc "Exactly! A bank robber lugging around a trash bag."
scene ep9_ph2_josy_event12 with dissolve
js "I bet that bag is full of garbage, not money."
scene ep9_ph2_josy_event14 with dissolve
mc "I bet it's not filled with girls' phone numbers, either."
js "Haha! If it is, they're all fake."
if ep9_sally_drink:
    $ task_list[13] = "Check Right hallway"
    $ event_list.append("ep9_diks_ph2_sally_event_label")
else:
    $ task_list[13] = ""
$ updateTaskList()
$ new_bio("You", "I comforted Josy after she was insulted by Oscar at the Halloween party.")
$ new_bio("Josy", "I comforted Josy after she was insulted by Oscar at the Halloween party.")
jump endEvent

label ep9_ssolo_label:
scene ep9_ssolo1 with dissolve
sa "Ugh..."
scene ep9_ssolo2 with dissolve
mc "What's wrong?"
scene ep9_ssolo3 with dissolve
sa "I forgot the stupid trophy in my room."
scene ep9_ssolo2 with dissolve
mc "The one for the best costume competition?"
scene ep9_ssolo3 with dissolve
sa "Yeah. We glued it together yesterday, and I completely forgot about it."
scene ep9_ssolo4 with dissolve
stop music fadeout 3
mc "Let's go get it. I could use some fresh air."
scene ep9_ssolo5 with wipeleft
play music "music/ep9/diks_spooky_halloween.mp3"
sa "There it is."
scene ep9_ssolo6 with dissolve
mc "Haha! No way. You made this?"
sa "As per Tommy's request."
mc "For someone who didn't want anything to do with the competition, he sure likes to come up with ideas for it."
scene ep9_ssolo7 with dissolve
sa "Yeah, what is it with you guys and dicks?"
sa "Dicks for helmets, dicks for trophies..."
scene ep9_ssolo8 with dissolve
mc "Dicks are funny, I guess."
mc "You did a good job on this trophy."
scene ep9_ssolo7 with dissolve
sa "Yeah? You'd wanna have that on your desk?"
scene ep9_ssolo8 with dissolve
mc "Well, I'm a judge in the contest. Luckily, I don't have to factor that into my opinion about how it looks."
scene ep9_ssolo9 with dissolve
sa "I know why you like the look of it."
sa "It's got an uncanny resemblance, no?"
scene ep9_ssolo10 with dissolve
mc "You modeled the trophy after me?"
scene ep9_ssolo11 with dissolve
sa "Haha! Don't be ridiculous. This one has you beat."
sa "I modeled it after my brother. Since, you know, he's a huge dick."
scene ep9_ssolo10 with dissolve
mc "I'm happy you said that last part."
scene ep9_ssolo12 with dissolve
sa "Eww!"
scene ep9_ssolo13 with dissolve
mc "They have their Halloween tonight too, right?"
scene ep9_ssolo12 with dissolve
sa "If you can call it that. I'd say it's more of a cult meeting. Creeps me the fuck out."
scene ep9_ssolo13 with dissolve
mc "Yeah, their parties don't seem normal at all."
scene ep9_ssolo14 with dissolve
sa "Well, you've been to one. They're all pretty similar."
scene ep9_ssolo15 with dissolve
mc "Yeah? Let's hope the sprinklers don't go off on this one too."
if pathMayaJosy or not pathSage:
    scene ep9_ssolo14 with dissolve
    sa "I got wet when you did that, you know."
    scene ep9_ssolo15 with dissolve
    mc "Yeah... Sorry about that."
else:
    scene ep9_ssolo16 with dissolve
    sa "Haha! I know who Tybalt would blame for that without hesitating."
scene ep9_ssolo17 with dissolve
mc "Your brother slapped me for that."
sa "He slapped you?"
mc "Yeah, a proper bitch slap. Straight across my face. And he also called me nasty names as he did it."
scene ep9_ssolo18 with dissolve
sa "For real? Please, tell me you punched him."
scene ep9_ssolo19 with dissolve
if ep5_punchedTybalt:
    mc "Oh, I left there with fake tanned knuckles."
    scene ep9_ssolo18 with dissolve
    sa "Good. Someone needs to bring him back to earth."
    scene ep9_ssolo19 with dissolve
    mc "Then Derek and I egged him."
else:
    mc "I walked away from it. He already looked ridiculous in his wet suit."
    scene ep9_ssolo18 with dissolve
    sa "You walked away from getting slapped? Talk about self-restraint."
    scene ep9_ssolo19 with dissolve
    mc "Well, Derek and I egged him afterward."
mc "It was part of our Hell Week pledge board."
scene ep9_ssolo20 with dissolve
sa "Haha! You guys egged him this year too? I would have loved to see that - him all covered in eggshells and yolk!"
scene ep9_ssolo21 with dissolve
mc "Pranking them is an annual thing, so..."
mc "Maybe you will see it next year?"
scene ep9_ssolo18 with dissolve
sa "He's graduating, too. So, that's not gonna happen..."
scene ep9_ssolo22 with dissolve
sa "..."
mc "What are you thinking about?"
scene ep9_ssolo20 with dissolve
sa "Mel just gave me an idea..."
sa "You know... We still have gallons of pumpkin pulp in our fridge from carving pumpkins."
scene ep9_ssolo21 with dissolve
mc "Yeah? So?"
scene ep9_ssolo20 with dissolve
sa "What do you say? Do we have time for a prank of our own?"
scene ep9_ssolo21 with dissolve
mc "You wanna prank your brother?"
scene ep9_ssolo20 with dissolve
sa "Let's fill his bed with it!"
scene ep9_ssolo21 with dissolve
mc "You're serious?"
scene ep9_ssolo23 with dissolve
sa "Oh, hell yes, I am!"
scene ep9_ssolo21 with dissolve
mc "It's risky. Didn't you say they have their party now?"
mc "I mean, how would we even get in there?"
scene ep9_ssolo23 with dissolve
sa "Have you met me?"
scene ep9_ssolo24 with wipeleft
mc "He let us pass, just like that...?"
scene ep9_ssolo25 with dissolve
sa "I told you he would. \"We're bringing food to the party\"."
mc "They're all out back, right?"
sa "They should be, unless they're using the bathrooms. We better watch out."
scene ep9_ssolo26 with dissolve
sa "The coast is clear. Let's do it."
scene ep9_ssolo27 with dissolve
sa "Haha! Yes! Spread it out."
mc "This is disgusting. He's gonna hate this."
scene ep9_ssolo28 with dissolve
sa "Haha! I bet he won't spot this. He might even get in bed on top of it when it's dark."
mc "We should get out of here."
scene ep9_ssolo29 with dissolve
mc "Think he'll freak out when he notices?"
scene ep9_ssolo30 with dissolve
sa "Oh, absolutely! And he'll blame everyone for it, not knowing who did it."
scene ep9_ssolo31 with dissolve
mc "I feel a bit bad, though."
scene ep9_ssolo30 with dissolve
sa "You don't have to feel bad. He deserves this."
scene ep9_ssolo31 with dissolve
mc "Not about him. But I swore off doing things like this after Hell Week."
mc "It got way too intense at times."
scene ep9_ssolo32 with dissolve
sa "This was just a harmless prank. Cut yourself some slack."
sa "It's not like we put the pulp in his suits."
scene ep9_ssolo33 with dissolve
mc "That would have been way worse, yes."
scene ep9_ssolo34 with dissolve
stop music fadeout 3
sa "We should put the pulp in his suits!"
scene ep9_ssolo35 with dissolve
mc "Haha! Easy now. Let's do one prank at a time."
$ task_list[10] = ""
$ updateTaskList()
$ mphone_next_song()
$ new_bio("Tybalt", "Sage and I poured pumpkin pulp on Tybalt's bed as a prank.")
jump endEvent

label ep9_jsolo_label:
scene ep9_jsolo1 with dissolve
js "Mhm. No, it's a laid-back party."
scene ep9_jsolo2 with dissolve
js "Uh-huh."
js "*{i}Mouths{/i}* Dad."
scene ep9_jsolo3 with dissolve
js "If I'm drinking?"
js "Well, what did you do in college at my age?"
scene ep9_jsolo6 with dissolve
js "Hahaha!"
js "What? No. It's just [name] being goofy."
scene ep9_jsolo4 with dissolve
js "Um... [name]? Yeah, the same one from before."
js "Well, he's a friend."
scene ep9_jsolo7 with dissolve
mc "*{i}Mouths{/i}* Friend!?"
scene ep9_jsolo5 with dissolve
js "Yeah, he's in my class."
js "No, engineering. But we share some classes during our first year."
scene ep9_jsolo4 with dissolve
js "Dad! Stop it."
js "No, I'm not putting him on the phone with you."
scene ep9_jsolo8 with dissolve
js "[name]... He wants to talk to you."
scene ep9_jsolo9 with dissolve
mc "Pete, right?"
scene ep9_jsolo10 with dissolve
mc "Um... Hello?"
$ guideSuggestedPage = 69
scene ep9_jsolo11 with dissolve
pt "Hi, is this Josy's friend?"
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        
                        
                        
            
menu:
    "Yes":
        mc "Yes, that's me. I'm [name]."
        scene ep9_jsolo12 with dissolve
        pt "Ah. That's nice. Since you were in the room, I figured I'd introduce myself."
    "More than a friend [mod_gr][mod_choices[0]]":
        $ RPjosy += 1
        scene ep9_jsolo13 with dissolve
        mc "Well, \"friend\" doesn't really describe it."
        play sound "sound_effects/hand.mp3"
        scene ep9_jsolo14 with hpunch
        mc "We're very good friends! Best friends."
        scene ep9_jsolo15 with dissolve
        pt "Haha, best friends, then. Since you were in the room, I figured I'd introduce myself."
pt "It's not the first time I heard your name come up in conversation."
scene ep9_jsolo16 with dissolve
mc "Oh, really?"
js "What?"
scene ep9_jsolo17 with dissolve
mc "She talks a lot about me?"
scene ep9_jsolo18 with dissolve
js "[name]. Give me the phone."
pt "Haha, enough times for me to want to put a voice to the name."
mc "That's very nice to hear. I appreciate it."
scene ep9_jsolo19 with dissolve
pt "Maybe I can put a face to the voice sometime soon, too?"
pt "We don't live far from B&R, so if you ever want to join her back home, feel free to do so."
mc "Thank you for the offer; I'll be sure to run it past Josy."
js "What!?"
scene ep9_jsolo20 with dissolve
pt "It was nice hearing from her friend. Please, take care of my baby girl tonight."
mc "Oh, absolutely. Will do."
pt "Bye, [name]."
"*{i}Click{/i}*"
scene ep9_jsolo21 with dissolve
mc "Yeah. She's cute, I agree."
js "WHAT!?"
scene ep9_jsolo22 with dissolve
mc "Yes, you guessed it. We have been dating a bit."
mc "We've done more than that, but I'm sure you don't want to hear the details."
js "[name]!!!"
mc "Yeah, she gets freaky."
scene ep9_jsolo23 with dissolve
js "Dad!? Dad!?"
mc "Hahahaha!"
scene ep9_jsolo24 with dissolve
mc "He hung up a while ago."
scene ep9_jsolo25 with dissolve
js "You are fucking horrible! Oh my God!!!"
mc "Hahaha!"
js "I'm sweating here!"
scene ep9_jsolo26 with dissolve
mc "Oh, come on. I was only joking."
scene ep9_jsolo25 with dissolve
js "You bastard..."
scene ep9_jsolo27 with dissolve
mc "Haha! Come here."
scene ep9_jsolo28 with dissolve
js "What did he really say?"
scene ep9_jsolo27 with dissolve
mc "He wanted to hear the voice of the guy you keep mentioning to him and also invite me back to your home at some point."
scene ep9_jsolo28 with dissolve
js "That's so embarrassing..."
scene ep9_jsolo27 with dissolve
mc "It was nice hearing it."
scene ep9_jsolo28 with dissolve
js "I don't talk {b}that{/b} much about you, so that you know."
scene ep9_jsolo29 with dissolve
mc "Sure you don't. But enough times that your dad wants to meet me."
scene ep9_jsolo30 with dissolve
js "I'm not bringing you back home with me."
scene ep9_jsolo29 with dissolve
mc "Why not?"
scene ep9_jsolo30 with dissolve
js "For one, I'm gonna die from embarrassment if what just happened happens again."
if ep2_fuckedJosy:
    js "And secondly, he is so gonna figure out that it was you who I had sex with in their bed."
    scene ep9_jsolo29 with dissolve
    mc "Damn... I forgot about that."
    scene ep9_jsolo30 with dissolve
    js "Well, I'm sure he didn't. And I'm also sure he wants to forget."
else:
    js "And secondly, he will probably figure out that it was you who I brought home for dinner that time when they grounded me."
    scene ep9_jsolo29 with dissolve
    mc "I forgot about that."
scene ep9_jsolo27 with dissolve
mc "You never brought a guy back home, did you?"
scene ep9_jsolo28 with dissolve
js "Nope. Never. Of course, they know who Maya is, but they think she's my friend."
js "With you, it would be different."
scene ep9_jsolo27 with dissolve
mc "Yeah..."
scene ep9_jsolo28 with dissolve
js "Did you ever bring a girl back home to meet your dad?"
scene ep9_jsolo27 with dissolve
mc "Not in this sense, no."
scene ep9_jsolo30 with dissolve
js "I wonder what he'd say if you brought Maya and me to see him."
scene ep9_jsolo29 with dissolve
mc "Oh, he'd be confused. 100%% confused."
scene ep9_jsolo30 with dissolve
js "See? It's not that easy to do it."
scene ep9_jsolo29 with dissolve
mc "At some point, you'd have to. Family is too important to be kept out of the loop."
scene ep9_jsolo30 with dissolve
js "I'm not sure Maya agrees with that."
scene ep9_jsolo29 with dissolve
mc "You know what I mean..."
scene ep9_jsolo31 with dissolve
js "When did things get this hard?"
scene ep9_jsolo32 with dissolve
mc "For me, it started when I took a job at a local minimart."
scene ep9_jsolo31 with dissolve
js "Imagine if we never did. We'd meet here at college instead; it might have been totally different."
scene ep9_jsolo32 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Reassure her [mod_gr][mod_choices[0]]":
        $ RPjosy += 1
        mc "Yeah, that's scary to think about. But I'd like to think we would sit here tonight like this even so."
        mc "It wasn't working with you that made me attracted to you; it was you being you who did it."
        scene ep9_jsolo33 with dissolve
        $ renpy.pause()
        scene ep9_jsolo34 with dissolve
        mc "*{i}Smack{/i}*"
    "Who knows?":
        mc "Yeah. Who knows what it would have been like?"
        scene ep9_jsolo31 with dissolve
        js "Yeah..."
scene ep9_jsolo27 with dissolve
mc "Sorry for almost giving you a heart attack before."
scene ep9_jsolo28 with dissolve
js "Yeah, you'll be sorry. Some day you will be."
$ task_list[5] = ""
if "ep9_ph2_josy_event_label" in event_list:
    if persistent.mod_wtenabled:
        $ task_list[13] = "Help Josy (Main party room)"
    else:
        $ task_list[13] = "Help Josy"
if branchMayaJosy and (ep8_maya_lewd or ep7_solo_maya):
    $ event_list.append("ep9_msolo_lewd_label")
    if persistent.mod_wtenabled:
        $ task_list[1] = "Find Maya (Right hallway)"
    else:
        $ task_list[1] = "Find Maya"
$ updateTaskList()
$ new_bio("Josy", "I talked to Josy's dad, Pete, over the phone. It led to us talking about meeting parents.")
jump endEvent

label ep9_msolo_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya
    $ event_list = []
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track132.mp3"])
scene ep9_msolo_lewd1 with dissolve
my "There you are."
scene ep9_msolo_lewd2 with dissolve
my "*{i}Smack{/i}*"
scene ep9_msolo_lewd3 with dissolve
mc "How drunk are you?"
scene ep9_msolo_lewd4 with dissolve
my "You think that's the only reason I'd kiss you? If I were drunk?"
scene ep9_msolo_lewd3 with dissolve
mc "Maybe? Hell, Derek spills secrets when he's drunk. Maybe you feel like kissing people when you are."
scene ep9_msolo_lewd2 with dissolve
my "*{i}Smack{/i}* You might be onto something."
scene ep9_msolo_lewd5 with dissolve
$ renpy.pause()
scene ep9_msolo_lewd6 with dissolve
$ renpy.pause()
scene ep9_msolo_lewd7 with dissolve
$ renpy.pause()
scene ep9_msolo_lewd8 with dissolve
mc "Maya... People can see us..."
scene ep9_msolo_lewd9 with dissolve
my "*{i}Smack{/i}* Actually, I've been thinking about that. If they see you and me... Would it matter?"
scene ep9_msolo_lewd10 with dissolve
my "Like, what difference does that make? I'm a girl, you're a boy and it's a party."
scene ep9_msolo_lewd8 with dissolve
mc "We've been so careful up until now that it feels like we're doing something wrong."
mc "But you're right... Nothing about this is wrong."
scene ep9_msolo_lewd9 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Maya scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Keep making out [mod_gr][mod_choices[0]]":
        $ ep9_maya_lewd = True
        scene ep9_msolo_lewd12 with dissolve
        mc "*{i}Smack{/i}* Mmm..."
        my "You're such a great kisser. *{i}Smack{/i}*"
        scene ep9_msolo_lewd13 with dissolve
        my "I love your lips."
        scene ep9_msolo_lewd14 with dissolve
        $ renpy.pause()
        scene ep9_msolo_lewd15 with dissolve
        $ renpy.pause()
    "Mention Josy" if not _in_replay:
        mc "Except that we're leaving Josy out of it, maybe?"
        mc "You think she'd be jealous?"
        scene ep9_msolo_lewd11 with dissolve
        my "I mean, would you be?"
        scene ep9_msolo_lewd8 with dissolve
        mc "I don't think so. What about you?"
        scene ep9_msolo_lewd11 with dissolve
        my "Um... No? Or...maybe? It depends."
        my "Hm... I guess I need to talk to her about it. We promised to include each other."
        scene ep9_msolo_lewd8 with dissolve
        mc "Yeah... So... Now?"
        scene ep9_msolo_lewd11 with dissolve
        my "I'll talk to her when I see her."
        $ task_list[1] = ""
        $ updateTaskList()
        $ new_bio("Maya", "Maya got frisky with me in public. But she stopped after I mentioned that Josy wasn't there with us.")
        jump endEvent

scene ep9_msolo_lewd16 with dissolve
my "Come..."
scene ep9_msolo_lewd17 with dissolve
mc "My room?"
my "Yeah, your room."

scene ep9_msolo_lewd18 with dissolve
if "ep9_diks_ph2_photo_jm_event_label" in event_list:
    my "A photo studio? Where's your couch?"
else:
    my "Damn, I forgot... Where's your couch?"
mc "It's behind the green screen."
scene ep9_msolo_lewd19 with dissolve
my "Oh! That's perfect."
scene ep9_msolo_lewd20 with dissolve
mc "What are you doing back there?"
scene ep9_msolo_lewd21 with dissolve
my "What do you think?"
scene ep9_msolo_lewd22 with dissolve
my "Are you coming?"
scene ep9_msolo_lewd23 with dissolve
mc "Can I bring the camera?"
scene ep9_msolo_lewd22 with dissolve
my "Haha! Hell no! We're not there yet."
scene ep9_msolo_lewd24 with dissolve
mc "So, you're telling me there's a time for it?"
scene ep9_msolo_lewd25 with dissolve
my "You seem to forget we already did stuff on camera."
scene ep9_msolo_lewd26 with dissolve
mc "Yeah, but that doesn't count. This would be for our pleasure, not some stupid scavenger hunt."
hide screen new_phone_screen
play sound "sound_effects/shove.mp3"
scene ep9_msolo_lewd27 with hpunch
mc "Why am I even talking now? Gimme!"
my "Hahaha!"
scene ep9_msolo_lewd28 with dissolve
mc "*{i}Suck suck{/i}*"
my "You'd really want a video like that?"
scene ep9_msolo_lewd29 with dissolve
mc "*{i}Suck suck{/i}* It doesn't have to be a video. A picture would do the job too."
scene ep9_msolo_lewd30 with dissolve
my "Uh-huh? And what would that job be?"
scene ep9_msolo_lewd31 with dissolve
mc "I'm sure you can guess."
scene ep9_msolo_lewd32 with dissolve
my "Would it be...one of these?"
scene anim_maya_hj_ep9 with dissolve
mc "Exactly one of those..."
pause
scene anim_maya_hj2_ep9 with dissolve
mc "Are we taking this too far?"
my "You tell me... Tell me to stop and I will."
pause

scene ep9_msolo_lewd33 with dissolve
mc "Dammit, [maya]... You're supposed to be the voice of reason."
scene anim_maya_boobjob1_ep9 with dissolve
my "Why is that?"
mc "Because I've got shit judgment when I have a boner."
pause
scene ep9_msolo_lewd34 with dissolve
my "*{i}Moans{/i}* [mc_maya]..."

scene anim_maya_finger_ep9 with dissolve
my "Hngn... Yes... Your finger feels so nice inside of me."
pause
scene anim_maya_finger2_ep9 with dissolve
my "*{i}Smack{/i}* Don't stop."
pause

scene ep9_msolo_lewd35 with dissolve
el "Here it is!"
scene ep9_msolo_lewd36 with dissolve
my "Huh?"
mc "Fuck..."
scene ep9_msolo_lewd37 with dissolve
ti "This is awesome!"
scene ep9_msolo_lewd38 with dissolve
ta "We just stand in front of it or what?"
scene anim_maya_finger_ep9 with dissolve
el "Yes, exactly. Try to stand close together and not too far against the green screen, or it might cast a bad shadow."
scene ep9_msolo_lewd39 with dissolve
my "Hngn..."
scene anim_maya_finger_ep9 with dissolve
ti "How's my hair?"
ta "No clue. I can barely see anything in this."
scene ep9_msolo_lewd40 with vpunch
my "*{i}Muffled moans{/i}*"
scene ep9_msolo_lewd40 with vpunch
ti "Why didn't you cut out holes for your eyes instead of drawing black all over them?"
scene ep9_msolo_lewd41 with dissolve
ta "I was in a hurry!"
el "That looks good. A little more to the right..."
scene ep9_msolo_lewd42 with dissolve
el "Look at the camera... And smile!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_msolo_lewd42 with dissolve
el "One more shot. Hold that pose."
scene ep9_msolo_lewd42 with dissolve
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep9_msolo_lewd42 with dissolve
$ renpy.pause(0.5)
scene ep9_msolo_lewd43 with dissolve
el "Aaaand we have it! Thanks, girls."
ti "Can we see it?"
el "Sure... But it's gonna look completely different after we've retouched it."
el "Thanks for the pictures! Now I don't have to kill you."
ti "Wanna have a drink with us?"
el "Maybe later. I'm gonna hunt for more victims first. People are camera shy."
scene ep9_msolo_lewd44 with dissolve
my "They left, right?"
scene ep9_msolo_lewd45 with dissolve
mc "Yeah..."
scene ep9_msolo_lewd42 with dissolve
my "*{i}Smack{/i}*"
scene ep9_msolo_lewd44 with dissolve
my "You're right. Your judgment is shit. How nuts was that?"
scene ep9_msolo_lewd45 with dissolve
mc "It was so hot... I couldn't help it."
scene ep9_msolo_lewd44 with dissolve
my "It was... It's so hard having a silent orgasm."
scene ep9_msolo_lewd45 with dissolve
mc "I wanna finish, but you heard what Elena said."
scene ep9_msolo_lewd44 with dissolve
my "Yeah, we got lucky this time, for sure. I'll take care of you later, ok?"
scene ep9_msolo_lewd45 with dissolve
mc "Deal!"
scene ep9_msolo_lewd46 with dissolve
mc "I loved the initiative..."
scene ep9_msolo_lewd47 with dissolve
my "You know what? Me too."
scene ep9_msolo_lewd48 with dissolve
mc "I guess you've got poor judgment too?"
my "Well, I am with you."
mc "Oof."
my "Haha! Joking! Come on! You know you're the best, right?"
$ renpy.end_replay()
$ persistent.ep9_lewd_maya = True
$ calcScenes()
$ new_bio("Maya", "I was about to have sex with Maya behind the green screen at the Halloween party, but we were interrupted by people having their pictures taken. It was wild!")
$ mphone_stats_add_girl_s3("maya","You had sex with Maya behind the green screen in episode 9.")
$ task_list[1] = ""
$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep9_diks_ph2_riona_event_label:
$ guideSuggestedPage = 68
scene ep9_diks_ph2_riona_event1 with dissolve
if affinity == "DIK":
    mc "In my bed already? I'm not ready yet."
else:
    mc "Taking a break already?"
scene ep9_diks_ph2_riona_event2 with dissolve
ri "..."
scene ep9_diks_ph2_riona_event3 with dissolve
mc "Why are you angry? Did something happen?"
scene ep9_diks_ph2_riona_event4 with dissolve
ri "Can you leave me alone? I need a minute."
scene ep9_diks_ph2_riona_event3 with dissolve
menu:
    "[mod_gr]Try to cheer her up":
        $ ep9_cheered_rio = True
        mc "I can, but I'd rather try to make you feel better."
    "Leave":
        mc "Sure. Take as long as you need."
        scene ep9_diks_ph2_riona_event5 with dissolve
        ri "..."
        $ event_list.append("ep9_diks_ph2_riona_event2_label")
        $ task_list[6] = ""
        $ updateTaskList()
        $ new_bio("Riona", "Riona was upset at the Halloween party, but I didn't press her on it.")
        jump endEvent
mc "Question is... How?"
scene ep9_diks_ph2_riona_event6 with dissolve
ri "..."
mc "I suppose you don't want to share what's got you upset?"
scene ep9_diks_ph2_riona_event7 with dissolve
ri "It's nothing."
scene ep9_diks_ph2_riona_event6 with dissolve
mc "Of course, it's nothing. I hate nothing. Nothing always makes me mad too."
play sound "sound_effects/whoosh.mp3"
scene ep9_diks_ph2_riona_event8 with vpunch
mc "Take that!"
play sound "sound_effects/whoosh.mp3"
scene ep9_diks_ph2_riona_event9 with vpunch
mc "Ha!!!"
scene ep9_diks_ph2_riona_event10 with dissolve
ri "What are you doing?"
scene ep9_diks_ph2_riona_event11 with dissolve
mc "What does it look like I'm doing? I'm fighting nothing."
play sound "sound_effects/whoosh.mp3"
scene ep9_diks_ph2_riona_event9 with vpunch
mc "Damn you for making Rio upset! You good-for-nothing!"
scene ep9_diks_ph2_riona_event12 with dissolve
mc "I killed nothing for you. You should be fine now."
scene ep9_diks_ph2_riona_event13 with dissolve
mc "[name] killed nothing and Rio's happiness was restored!"
scene ep9_diks_ph2_riona_event14 with dissolve
mc "Need me to kill something else while I'm at it?"
scene ep9_diks_ph2_riona_event15 with dissolve
ri "No, I don't want to see more blood spilled."
scene ep9_diks_ph2_riona_event14 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Maya scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "[mod_gr]Hug her":
        $ ep9_riona_confided = True
        scene ep9_diks_ph2_riona_event20 with dissolve
        mc "I'm here for you if you need me."
        mc "For real. And not just for killing stuff."
        scene ep9_diks_ph2_riona_event21 with dissolve
        ri "Thanks, [name]. "
        if branchAlone:
            scene ep9_diks_ph2_riona_event22 with dissolve
            menu:
                "[mod_gr]Kiss her":
                    $ ep9_kissed_rio = True
                    scene ep9_diks_ph2_riona_event23 with dissolve
                    mc "*{i}Smack{/i}*"
                    scene ep9_diks_ph2_riona_event24 with dissolve
                    $ renpy.pause()
                    scene anim_riona_kiss_ep9 with dissolve
                    pause
                    scene ep9_diks_ph2_riona_event14 with dissolve
                    mc "I slayed nothing and saved the princess."
                    scene ep9_diks_ph2_riona_event17 with dissolve
                    ri "Princess? I'm a cat."
                    scene ep9_diks_ph2_riona_event18 with dissolve
                    mc "Well, I'm not gonna say I got a boner from making out with a cat."
                    scene ep9_diks_ph2_riona_event19 with dissolve
                    ri "Hahaha!"
                    scene ep9_diks_ph2_riona_event15 with dissolve
                    ri "God, you're so stupid at times."
                    scene ep9_diks_ph2_riona_event21b with dissolve
                    ri "Thanks for the laugh..."
                    if not persistent.ep9_card8:
                        $ tmpBool = True
                        $ persistent.ep9_card8 = True
                        $ persistent.rew_2d_unlocked += 1
                        $ persistent.chat_new_rewards = True
                        $ calcRenders()
                        show screen srmsg
                        $ renpy.pause(3)
                        hide screen srmsg
                "Don't kiss her":
                    $ renpy.pause(0.5)

        ri "I'll be fine. I just got down because of something Tommy said."
        scene ep9_diks_ph2_riona_event16 with dissolve
        mc "All right, where is he? I'll have to kill him too."
        scene ep9_diks_ph2_riona_event14 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph2_riona_event16 with dissolve
        mc "What did he say? Something mean?"
        scene ep9_diks_ph2_riona_event25 with dissolve
        ri "No. That's just it, it wasn't mean at all. But..."
        ri "It made me question things."
        scene ep9_diks_ph2_riona_event26 with dissolve
        mc "If you want my advice, you have to stop being vague."
        scene ep9_diks_ph2_riona_event25 with dissolve
        ri "I asked him if we could share a smoke - a blunt, you know?"
        ri "And he told me I've been smoking for free. But I never did, I've always paid for myself."
        scene ep9_diks_ph2_riona_event26 with dissolve
        mc "Did you smoke his stuff a lot in the past or...?"
        scene ep9_diks_ph2_riona_event25 with dissolve
        ri "It wasn't about his pot, it was in general. He said that Quinn told him..."
        scene ep9_diks_ph2_riona_event26 with dissolve
        mc "Oh? So, she's lying?"
        scene ep9_diks_ph2_riona_event27 with dissolve
        if ep5_confrontedRiona and ep4_discussed_riona:
            ri "Yeah, she is. Remember when I told you that we had problems with money?"
            scene ep9_diks_ph2_riona_event26 with dissolve
            mc "Yes."
            scene ep9_diks_ph2_riona_event25 with dissolve
            ri "I think Quinn is blaming me for it by telling Tommy I smoked for free..."
        else:
            ri "Yeah, she is. Don't tell anyone, but we had problems with money some weeks ago."
            scene ep9_diks_ph2_riona_event26 with dissolve
            mc "Who are we?"
            scene ep9_diks_ph2_riona_event25 with dissolve
            ri "Me and Quinn."
            scene ep9_diks_ph2_riona_event26 with dissolve
            mc "I'm a bit confused. What kind of problems?"
            scene ep9_diks_ph2_riona_event27 with dissolve
            ri "Just money problems."
            scene ep9_diks_ph2_riona_event25 with dissolve
            ri "And I think Quinn is blaming me for it by telling Tommy I smoked for free..."
        ri "...and possibly...that it was her who actually smoked for free."
        scene ep9_diks_ph2_riona_event27 with dissolve
        ri "Sorry...but I can't tell you more than that."
        scene ep9_diks_ph2_riona_event26 with dissolve
        mc "It's fine, but I...don't understand."
        scene ep9_diks_ph2_riona_event28 with dissolve
        ri "Yeah, I know. And you don't have to, but it means a lot that you're listening to me."
        scene ep9_diks_ph2_riona_event26 with dissolve
        mc "Of course."
        scene ep9_diks_ph2_riona_event17 with dissolve
        ri "Sorry about the bloodshed in here."
        scene ep9_diks_ph2_riona_event14 with dissolve
        mc "Yeah, this place is going to take ages to clean. There's blood everywhere."
        jump ep9_diks_ph2_riona_event2_label
    "Cheer her up":

        mc "Understandable. This place is going to take ages to clean. There's blood everywhere."
        label ep9_diks_ph2_riona_event2_label:
        scene ep9_diks_ph2_riona_event16 with dissolve
        mc "What do you say? Wanna get back out there?"
        mc "I hear people dance after being victorious in battle."
        scene ep9_diks_ph2_riona_event15 with dissolve
        ri "Haha, yeah. Dancing sounds good."
        if ep9_rio_joke:
            ri "I'm feline better."
            scene ep9_diks_ph2_riona_event14 with dissolve
            mc "Haha! Hey! That's my joke!"
$ task_list[6] = ""
$ updateTaskList()
$ new_bio("Riona", "Riona was upset at the Halloween party, and I cheered her up.")
if ep9_riona_confided:
    $ new_bio("Riona", "Riona told me that she and Quinn have some issues.")
    $ new_bio("Quinn", "Riona told me that she and Quinn have some issues.")
jump endEvent

label ep9_diks_ph2_l_event_label:
$ guideSuggestedPage = 65
scene ep9_diks_ph2_l_event1 with dissolve
girl "Hahaha! No way. You must be joking."
scene ep9_diks_ph2_l_event2 with dissolve
le "..."
mc "Striking out with the girls, huh?"
scene ep9_diks_ph2_l_event3 with dissolve
le "It's impossible to get laid while wearing this."
scene ep9_diks_ph2_l_event4 with dissolve
menu:
    "Remove the wig":
        mc "I think it's weird for girls to get hit on by someone dressed like that."
        mc "What if you remove the wig?"
        scene ep9_diks_ph2_l_event6 with dissolve
        le "You think {b}THIS{/b} would help?"
        le "Instead of looking like a cute girl, I would look like a hardcore lesbian."
        scene ep9_diks_ph2_l_event7 with dissolve
        mc "We have different definitions of cute, I think."
    "I bet I could":
        $ dk(1)
        mc "I don't think it's impossible. I bet I could do it."
        scene ep9_diks_ph2_l_event3 with dissolve
        le "Sure... Only because your dick would be longer than the skirt."
scene ep9_diks_ph2_l_event4 with dissolve
mc "I know you want to blame Jamie for this, but you should have thought about this before dressing as a girl."
scene ep9_diks_ph2_l_event3 with dissolve
le "It's not just any girl; I'm dressed as Lily."
scene ep9_diks_ph2_l_event4 with dissolve
mc "You are?"
scene ep9_diks_ph2_l_event3 with dissolve
le "You don't see it?"
scene ep9_diks_ph2_l_event4 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        
                        
                        
            
menu:
    "Humor him [mod_gr][mod_choices[0]]":
        $ RPdiks += 1
        mc "You're right, it does look like Lily. Great job!"
        scene ep9_diks_ph2_l_event5 with dissolve
        le "Thanks."
    "No":
        mc "I don't think you're remotely close."
        scene ep9_diks_ph2_l_event3 with dissolve
        le "*{i}Sigh{/i}*"
le "I'm gonna try my luck on the dance floor. That dim lighting might help me."
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

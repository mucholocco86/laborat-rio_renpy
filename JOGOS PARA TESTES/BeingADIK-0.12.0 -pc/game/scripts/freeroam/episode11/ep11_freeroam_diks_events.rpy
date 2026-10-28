label ep11_freeroam_diks_intro_label:
if branchJill:
    scene ep11_freeroam_diks_intro1 with dissolve
    mc "Does that look straight to you?"
    scene ep11_freeroam_diks_intro5 with dissolve
    ji "It's perfect."
    scene ep11_freeroam_diks_intro6 with dissolve
    mc "I don't know about that."
    scene ep11_freeroam_diks_intro7 with dissolve
    ji "Trust me. It's fine."
    scene ep11_freeroam_diks_intro8 with dissolve
    mc "Fine? You said perfect."
    scene ep11_freeroam_diks_intro10 with dissolve
    ji "Perfectly fine."
    scene ep11_freeroam_diks_intro11 with dissolve
    ji "*{i}Smack{/i}*"
    scene ep11_freeroam_diks_intro9 with dissolve
    mc "Thanks for the help."
    scene ep11_freeroam_diks_intro10 with dissolve
    ji "It's fun decorating for Christmas. I wish we got to do it more at our place, but they hire people for that."
    scene ep11_freeroam_diks_intro9 with dissolve
    mc "Well, you're in luck. We've got more things to decorate."
    mc "I think we should help out with the rest of the mansion now."
    scene ep11_freeroam_diks_intro12 with dissolve
    $ renpy.pause()
else:
    scene ep11_freeroam_diks_intro1 with dissolve
    $ renpy.pause()
    scene ep11_freeroam_diks_intro2 with dissolve
    mc "(I think that's enough Christmas decor for my room.)"
    scene ep11_freeroam_diks_intro3 with dissolve
    mc "(With the snow and the lights Jamie put up outside, it looks comfy.)"
    scene ep11_freeroam_diks_intro4 with dissolve
    mc "(I should help the others with the rest of the mansion.)"
jump ep11_freeroam_diks_label

label ep11_fr_deco_lc_event_label:
scene ep11_fr_deco_lc_event1 with dissolve
le "[name]? Why are they telling me the Christmas party is canned?"
scene ep11_fr_deco_lc_event2 with dissolve
if "ep11_fr_deco_sage_event_label" in event_list:
    mc "Who's telling you that?"
    scene ep11_fr_deco_lc_event1 with dissolve
    le "Jacob and Jamie were talking about it earlier. The HOTs aren't coming because they're going to the tri-alpha's Christmas party."
    scene ep11_fr_deco_lc_event2 with dissolve
    mc "Oh? I'll have to check with Sage about that, but we made a deal to share the HOTs with them."
    mc "But we can still have a party."
    scene ep11_fr_deco_lc_event3 with dissolve
    le "It's gonna be a lame party without them."
else:
    mc "It's not canned, but it's affected by the deal we made with the alphas."
    mc "We can still have a party, but the HOTs are busy on our set date."
    scene ep11_fr_deco_lc_event3 with dissolve
    le "Then what are we gonna do? It's gonna be a lame party without them."
$ guideSuggestedPage = 168
scene ep11_fr_deco_lc_event4 with dissolve
che "Yes! Fuck that! I'm not going to party with those backstabbing dorm bitches."
scene ep11_fr_deco_lc_event5 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Jill)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Thank him for helping":
        mc "Chen, right?"
        mc "Thanks for helping Leon find out who put those posters up."
    "Fuck them \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Yep. Fuck them for doing what they did."
    "No need to call them that \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "You don't have to call them that. Disrespecting them is what started all of this."
scene ep11_fr_deco_lc_event4 with dissolve
che "Bitches, I tell you! Bitches! All of them."
che "Never even saw half of them on campus, but I could tell straight away they were bitches."
che "Short hair, ugly clothes, pale skin, short and skinny. I could smell them from a mile away."
scene ep11_fr_deco_lc_event6 with dissolve
che "Except for that one blonde bitch from our Sociology class. What's her face?"
scene ep11_fr_deco_lc_event7 with dissolve
le "Tara..."
scene ep11_fr_deco_lc_event8 with dissolve
che "Yes, Tara. She's got nice boobs. Still a bitch. But nice, big boobs. Gotta give her that."
scene ep11_fr_deco_lc_event7 with dissolve
le "And Kylie too... She's hot."
scene ep11_fr_deco_lc_event8 with dissolve
che "Oh, yes! Kylie! I'd do her."
scene ep11_fr_deco_lc_event9 with dissolve
che "What were we talking about?"
scene ep11_fr_deco_lc_event11 with dissolve
le "The party, [name]... What are we gonna do?"
scene ep11_fr_deco_lc_event10 with dissolve
mc "I'll figure something out."

$ new_bio("Leon", "Leon was upset that the Christmas party was affected by the deal the DIKs made with the tri-alphas about sharing the HOTs at parties.")
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_mem_event_label:
scene ep11_fr_deco_mem_event1 with dissolve
el "No... That box shouldn't be here. That's more of our Christmas tree ornaments."
scene ep11_fr_deco_mem_event2 with dissolve
mc "How's it going?"
if ep9_sarah_melanie_lewd or branchAlone:
    scene ep11_fr_deco_mem_event19 with dissolve
    ml "Hey, [name]... We brought the wrong boxes here."
else:
    scene ep11_fr_deco_mem_event3 with dissolve
    ml "We brought the wrong boxes here..."
scene ep11_fr_deco_mem_event8 with dissolve
el "Yeah. Sage said the boxes labeled \"kitchen\" are supposed to be at our place."
el "And the boxes labeled \"random\" are the ones you guys need. But we already got you those."
el "The kitchen boxes are missing."
scene ep11_fr_deco_mem_event9 with dissolve
mc "Want me to have a look around?"
scene ep11_fr_deco_mem_event4 with dissolve
ml "God, yes. My arms are tired from all the carrying."
scene ep11_fr_deco_mem_event9 with dissolve
mc "So, I'll just bring the kitchen boxes to your kitchen?"
scene ep11_fr_deco_mem_event8 with dissolve
el "The kitchen boxes don't contain kitchen stuff; that's just what the label says."
scene ep11_fr_deco_mem_event9 with dissolve
mc "Well, that's confusing."
scene ep11_fr_deco_mem_event10 with dissolve
el "There's supposed to be a system, but it got fucked up at some point, and now no one cares enough to fix it since we only have to deal with it once every year."
el "Instead, we're stuck with an even weirder system..."
el "Anyway, bring the kitchen boxes to John Boy. He's over at our place helping out."
scene ep11_fr_deco_mem_event9 with dissolve
mc "What's in the kitchen boxes?"
scene ep11_fr_deco_mem_event3 with dissolve
ml "Christmas lights."
scene ep11_fr_deco_mem_event5 with dissolve
mc "And in the random boxes?"
scene ep11_fr_deco_mem_event3 with dissolve
ml "Kitchen stuff."
scene ep11_fr_deco_mem_event5 with dissolve
mc "You're joking, right?"
scene ep11_fr_deco_mem_event6 with dissolve
ml "I wish..."
scene ep11_fr_deco_mem_event7 with dissolve
mc "Oook... I'll figure it out."
if ep9_sarah_melanie_lewd or branchAlone:
    scene ep11_fr_deco_mem_event20 with dissolve
    if ep9_sarah_melanie_lewd:
        ml "I'm sure you will. You're good at handling...boxes."
    else:
        ml "I'm sure you will. I think [name] can handle...a box."
    scene ep11_fr_deco_mem_event21 with dissolve
    el "Get a room."
    scene ep11_fr_deco_mem_event22 with dissolve
    ml "I wouldn't mind that."
    scene ep11_fr_deco_mem_event23 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_mem_event24 with dissolve

    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]    

    menu:
        "You earned yourself a break \n{size=-4}[m_c1][mod_choices[0]]":
            mc "I think you earned yourself a break."
            scene ep11_fr_deco_mem_event26 with dissolve
            el "Not to be that one, but she didn't."
            scene ep11_fr_deco_mem_event25 with dissolve
            ml "Later, [name]..."
            $ event_list.append("ep11_fr_mel_lewd_event_label")
        "Leave":
            $ renpy.pause(0.5)

scene ep11_fr_deco_mem_event11 with dissolve
mc "Hey, Maya."
scene ep11_fr_deco_mem_event12 with dissolve
my "Hm? Oh, hey!"
my "Sorry, I was in the middle of thinking."
scene ep11_fr_deco_mem_event13 with dissolve
mc "I'd be, too, if I got stuck with untangling Christmas lights."
scene ep11_fr_deco_mem_event14 with dissolve
my "Haha, yeah."
if branchMayaJosy:
    scene ep11_fr_deco_mem_event13 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Maya)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "Ask for a kiss \n{size=-4}[m_c1][mod_choices[0]]":
            $ RPmaya += 1
            scene ep11_fr_deco_mem_event15 with dissolve
            mc "I know I put the mistletoe upstairs, but can I steal a kiss from you?"
            scene ep11_fr_deco_mem_event16 with dissolve
            $ renpy.pause()
            scene ep11_fr_deco_mem_event17 with dissolve
            my "*{i}Smack{/i}*"
            scene ep11_fr_deco_mem_event18 with dissolve
            $ renpy.pause()
        "Don't let me interrupt":
            mc "Don't let me interrupt. I have some boxes to find."
else:
    scene ep11_fr_deco_mem_event13 with dissolve
    mc "Don't let me interrupt. I have some boxes to find."
show screen wt_boxes_update
$ task_list[0] = "Find boxes labeled Kitchen (0/3)"

$ event_list.append("ep11_fr_deco_box1_event_label")
$ event_list.append("ep11_fr_deco_box2_event_label")
$ event_list.append("ep11_fr_deco_box3_event_label")

$ updateTaskList()
jump endEvent

label ep11_fr_deco_rm_event_label:
scene ep11_fr_deco_rm_event1 with dissolve
mc "Rusty, do you...?"
scene ep11_fr_deco_rm_event2 with dissolve
mc "Oh. I didn't mean to interrupt. Um... Carry on."
scene ep11_fr_deco_rm_event3 with dissolve
rs "[name], wait."
scene ep11_fr_deco_rm_event4 with dissolve
mc "Dude... What are you doing?"
scene ep11_fr_deco_rm_event5 with dissolve
rs "I know what it looks like, but things happened."
scene ep11_fr_deco_rm_event4 with dissolve
mc "Did she break up with her guy again?"
scene ep11_fr_deco_rm_event5 with dissolve
rs "No. And frankly, I don't care about him. I care about her."
scene ep11_fr_deco_rm_event4 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Maya)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if branchJill or branchIsabella:
                           $ mod_choices[6]="(Possible Bianca path)"

menu:
    "What you do is your business \n{size=-4}[m_c1][mod_choices[6]]":
        $ ep11_rusty_choice = False
        mc "Well... What you do with her is your business."
        scene ep11_fr_deco_rm_event7 with dissolve
        mc "Both of you are making the same decision in there."
    "You're better than this":
        $ ep11_rusty_choice = True
        mc "I get it... You want her, but come on..."
        mc "You're better than this."
        scene ep11_fr_deco_rm_event7 with dissolve
        mc "Trust me, this situation you're putting yourself in sucks for everyone involved."

scene ep11_fr_deco_rm_event6 with dissolve
rs "She'll break up with him at some point; I can feel it."
if not ep11_rusty_choice:
    scene ep11_fr_deco_rm_event4 with dissolve
    mc "I don't care. I'm staying out of it."
    scene ep11_fr_deco_rm_event8 with dissolve
    rs "You don't care anymore?"
    scene ep11_fr_deco_rm_event7 with dissolve
    mc "What I mean is that you're free to make your own choices."
else:
    scene ep11_fr_deco_rm_event4 with dissolve
    mc "Did she say that?"
    scene ep11_fr_deco_rm_event6 with dissolve
    rs "I'm working on it."
    scene ep11_fr_deco_rm_event4 with dissolve
    mc "I won't tell you what to do, but I won't hide what I think."
    mc "This is a bad call."

scene ep11_fr_deco_rm_event5 with dissolve
rs "Well, it's what I choose."
scene ep11_fr_deco_rm_event4 with dissolve
if not ep11_rusty_choice:
    mc "Cool..."
else:
    mc "Then don't let me bother you."
if branchJill:
    mc "You can go back to ignoring me."
    scene ep11_fr_deco_rm_event9 with dissolve
    rs "Hey... What's that supposed to mean?"
    scene ep11_fr_deco_rm_event10 with dissolve
    mc "Stop pretending you don't know what I'm talking about."
    mc "You haven't even approached me to talk since Nick dropped that bomb about Jill. Did you expect me to forget about that?"
    scene ep11_fr_deco_rm_event9 with dissolve
    rs "What do you want me to say? That I liked Jill a lot?"
    rs "Would that make you feel better?"
    scene ep11_fr_deco_rm_event10 with dissolve
    mc "I thought you'd at least try to explain why he'd say such a hurtful thing."
    scene ep11_fr_deco_rm_event11 with dissolve
    rs "I'm trying to shut up and stay neutral because I don't intend to ruin your relationship with her."
    rs "Yes, there was some truth to what Nick said. But it wasn't yesterday I told him about Jill."
    scene ep11_fr_deco_rm_event12 with dissolve
    rs "It was before you came here, and you two getting together changed things."
    rs "But it doesn't take away that I regret how I acted and fucked up my chances with her."
    scene ep11_fr_deco_rm_event11 with dissolve
    rs "You don't have to worry. I don't look at Jill like someone who got away."
    rs "She's my wake-up call. She's the girl who made me realize that I was going down a path I didn't like with my frat mates."
    scene ep11_fr_deco_rm_event13 with dissolve
    rs "It's taken me a lot of willpower to try and change who I was."
    rs "Seeing her with you makes me think it could have been me. If I had only had the same courage as you do."
    scene ep11_fr_deco_rm_event14 with dissolve
    rs "You don't play any games around her. Even during the Walk of Shame, you stuck up for her like it was nothing."
    rs "You showed me how I should have acted back when I was in your position, but I didn't."
    scene ep11_fr_deco_rm_event13 with dissolve
    rs "And yeah, that made me feel angry. But I was mostly angry at myself."
    rs "Why couldn't I have done that?"
    scene ep11_fr_deco_rm_event11 with dissolve
    rs "It doesn't mean I hate you or resent your relationship with her."
    rs "I'm not denying that I'm jealous of what you got, but that speaks more to what I wish I had in my life."
    rs "It's not about Jill. Ok?"
    scene ep11_fr_deco_rm_event15 with dissolve
    mc "Why didn't you tell me this sooner?"
    scene ep11_fr_deco_rm_event14 with dissolve
    rs "Because I was ashamed, [name]. I couldn't deny what he said."
    scene ep11_fr_deco_rm_event13 with dissolve
    rs "I'm not sure if you can relate to this, but..."
    rs "No matter who the guy was, I always knew that seeing Jill in a relationship would hit me like a brick to the face."
    scene ep11_fr_deco_rm_event11 with dissolve
    rs "And that guy happened to be you."
    scene ep11_fr_deco_rm_event15 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_rm_event13 with dissolve
    rs "[name], I'm sorry. It's nothing personal against you. It's my history with her."
    scene ep11_fr_deco_rm_event15 with dissolve
    menu:
        "You need to deal with it":
            $ ep11_rusty_deal_with_it = True
            mc "It's not fun to hear that you feel that way, but you need to find a way to deal with it."
            mc "If you don't, it will be hard for me to stay your friend."
            scene ep11_fr_deco_rm_event13 with dissolve
            rs "That's why I didn't talk to you about it. Maybe that was wrong, but I'm trying, [name]."
        "I understand":
            $ ep11_rusty_deal_with_it = False
            if ep10_zoey_jacob:
                mc "You're right. I can't relate to that, but I think I understand what you mean. Still... It hurt hearing it like that."
            else:
                mc "You're wrong. I can relate to that feeling. And I understand what you mean. Still... It hurt hearing it like that."
    scene ep11_fr_deco_rm_event12 with dissolve
    rs "Again... I'm sorry."
    if ep11_rusty_choice:
        scene ep11_fr_deco_rm_event16 with dissolve
        mc "You said you didn't like the path you were going down..."
        mc "Do you like the path you're going down now with Micha any better?"
        scene ep11_fr_deco_rm_event15 with dissolve
        rs "..."
        mc "You should think about that."
    else:
        scene ep11_fr_deco_rm_event16 with dissolve
        mc "Ok."

$ new_bio("Micha", "Micha is still fooling around with Rusty despite being in a relationship.")
if ep11_rusty_choice:
    $ new_bio("Rusty", "I tried to make Rusty see the error of his ways for fooling around with Micha, who was cheating on her boyfriend with him.")
else:
    $ new_bio("Rusty", "I minded my own business when I saw Rusty fooling around with Micha.")
if branchJill:
    if ep11_rusty_deal_with_it:
        $ new_bio("Rusty", "I confronted Rusty about what Nick had said about Rusty and Jill. Rusty tried to explain himself to me, and I told him to get over it.")
    else:
        $ new_bio("Rusty", "I confronted Rusty about what Nick had said about Rusty and Jill. Rusty tried to explain himself to me, and I told him I understood where he was coming from.")

$ task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_tj_event_label:
scene ep11_fr_deco_tj_event1 with dissolve
tm "What's the deal with all the lights outside? Are you trying to blind the neighbors?"
scene ep11_fr_deco_tj_event2 with dissolve
jm "I think they look nice."
scene ep11_fr_deco_tj_event1 with dissolve
tm "Nice? I saw an airplane trying to land in our backyard earlier."
scene ep11_fr_deco_tj_event3 with dissolve
jm "Ha-ha. Lighten up. Santa gotta park his sleigh somewhere. It's good that he can find the place."
scene ep11_fr_deco_tj_event1 with dissolve
tm "You care too much about this stupid holiday."
scene ep11_fr_deco_tj_event2 with dissolve
jm "I saw you care about Christmas last year."
scene ep11_fr_deco_tj_event5 with dissolve
tm "The party, yeah. Because I get to dress up as Santa and make hot chicks sit in my lap!"
scene ep11_fr_deco_tj_event4 with dissolve
jm "We like different things, Tommy. It's for one month of the year; I think you'll survive."
$ guideSuggestedPage = 170
if ep9_heather_lewd == 2:
    scene ep11_fr_deco_tj_event7 with dissolve
    mc "About our Christmas party... The HOTs won't show for it. Alphas have called dibs."
    scene ep11_fr_deco_tj_event8 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_tj_event9 with dissolve
    mc "For how long do you think he'll be upset with me?"
    scene ep11_fr_deco_tj_event10 with dissolve
    jm "Did you apologize again?"
    scene ep11_fr_deco_tj_event11 with dissolve
    mc "Several times..."
    scene ep11_fr_deco_tj_event10 with dissolve
    jm "I have never seen him forgive someone. And since I don't see it happening with Nick... I'm not sure about you either."
    scene ep11_fr_deco_tj_event11 with dissolve
    mc "Thanks..."
    scene ep11_fr_deco_tj_event10 with dissolve
    jm "You did a bad thing, [name]."
    scene ep11_fr_deco_tj_event11 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(-DIKS)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
    
    menu:
        "I know":
            mc "I know, but I couldn't help it. She threw herself at me, and she was so hot in that swimsuit."
            scene ep11_fr_deco_tj_event10 with dissolve
            jm "If you're looking for sympathy, that's not the way to go at it."
            jm "Tommy won't say this, so I will. You broke a bro code and you hurt him."
            $ new_bio("Jamie", "I tried getting sympathy from Jamie when he said I did a bad thing by being intimate with Heather.")
        "He had it coming \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
            $ dk(1)
            $ RPdiks -= 1
            mc "I'm sorry, but he had it coming. You know how he treated Heather, yeah?"
            mc "What kind of a relationship is that? I figured it wasn't that big of a deal since he fucks other girls."
            scene ep11_fr_deco_tj_event12 with dissolve
            jm "It doesn't justify it. Especially not when it's your brother."
            scene ep11_fr_deco_tj_event11 with dissolve
            mc "Don't make me feel worse about it."
            scene ep11_fr_deco_tj_event12 with dissolve
            jm "I'm gonna because you should feel bad about it."
            $ new_bio("Jamie", "I told Jamie that Tommy had it coming to him when Jamie said I did a bad thing by being intimate with Heather.")
    scene ep11_fr_deco_tj_event11 with dissolve
    mc "*{i}Sigh{/i}* What can I do to make it better? He won't talk to me."
    scene ep11_fr_deco_tj_event13 with dissolve
    jm "For starters, you can help him feel better by throwing a kickass Christmas party."
else:
    scene ep11_fr_deco_tj_event6 with dissolve
    mc "About our Christmas party... The HOTs won't show for it. Alphas called dibs."
    scene ep11_fr_deco_tj_event8 with dissolve
    tm "*{i}Sigh{/i}* I don't even care anymore."
    jm "Come on, Tommy. Sure you do."
    scene ep11_fr_deco_tj_event10 with dissolve
    jm "He's been so bummed out lately."
    scene ep11_fr_deco_tj_event11 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(-DIKS)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "He had it coming \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
            $ dk(1)
            $ RPdiks -= 1
            mc "He had it coming."
            scene ep11_fr_deco_tj_event13 with dissolve
            $ new_bio("Jamie", "I told Jamie that Tommy had it coming to him when Jamie talked about Heather cheating with Nick.")
        "Haven't we all?":
            mc "Haven't we all?"
            scene ep11_fr_deco_tj_event13 with dissolve
            jm "Yeah, I know I have... I miss Franz a lot."
    jm "We need that Christmas party, but nobody is talking about it."
scene ep11_fr_deco_tj_event14 with dissolve
mc "Without the HOTs, who would we even bother inviting? Can we even trust the people who show up?"
scene ep11_fr_deco_tj_event13 with dissolve
jm "You can figure something out, can't you? You always have ideas to fix things."
scene ep11_fr_deco_tj_event14 with dissolve
mc "I can't change the deal they made with the alphas."
scene ep11_fr_deco_tj_event15 with dissolve
jm "No, but you can change the date of the party."
jm "WWTD?"
scene ep11_fr_deco_tj_event14 with dissolve
mc "Huh?"
scene ep11_fr_deco_tj_event15 with dissolve
jm "WWTD? What Would Tommy Do?"
scene ep11_fr_deco_tj_event14 with dissolve
mc "..."
mc "He'd say fuck the alphas and do whatever he'd like. He wouldn't respect their deal if it were up to him. Or...he'd find some loophole."
scene ep11_fr_deco_tj_event16 with dissolve
jm "There you have it."
scene ep11_fr_deco_tj_event14 with dissolve
mc "So...if we can't host our Christmas party on that Saturday..."
scene ep11_fr_deco_tj_event17 with dissolve
mc "We'll host one on the Friday. As a bonus, the HOTs will show up hungover to the alphas' party the day after."
scene ep11_fr_deco_tj_event16 with dissolve
jm "I think you got this. There's a little Tommy inside all of us. We just gotta find him."
scene ep11_fr_deco_tj_event14 with dissolve
mc "That sounds weird, bro."
scene ep11_fr_deco_tj_event18 with dissolve
if ep9_heather_lewd == 2:
    jm "Do it for Tommy. Redeem yourself."
else:
    jm "Make Tommy proud."
jm "And hey... Don't forget about yourself too. We all deserve a great party."
$ new_bio("Jamie", "Jamie wanted me to plan a Christmas party for Tommy's sake.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_ari_event_label:
scene ep11_fr_deco_ari_event1 with dissolve
ar "You gotta buy something!"
scene ep11_fr_deco_ari_event6 with dissolve
he "No, I don't."
scene ep11_fr_deco_ari_event1 with dissolve
ar "Come on! I'm sure you need something."
scene ep11_fr_deco_ari_event6 with dissolve
he "What am I going to do with a glow-in-the-dark double-headed dildo?"
scene ep11_fr_deco_ari_event2 with dissolve
ar "Use it with Tommy."
scene ep11_fr_deco_ari_event7 with dissolve
he "We broke up. I told you this."
scene ep11_fr_deco_ari_event3 with dissolve
ar "Oh, right! I forgot. Preggo-brain is affecting me like crazy. I'm not as sharp as I normally am."
scene ep11_fr_deco_ari_event2 with dissolve
ar "You can still use it with someone."
ar "Maybe with a friend who recently discovered she would be able to have sex without periods for plenty of more months to come?"
scene ep11_fr_deco_ari_event8 with dissolve
he "..."
scene ep11_fr_deco_ari_event4 with dissolve
ar "I'm single too, you know!? These toys work great for me!"
scene ep11_fr_deco_ari_event9 with dissolve
sar "Aren't you with Dawe?"
scene ep11_fr_deco_ari_event5 with dissolve
ar "Um, hello? I'm trying to make a sale!"
ar "No one wants to buy anything, and it cost me a $250 deposit to get started."
scene ep11_fr_deco_ari_event10 with dissolve
js "What is that you're selling?"
scene ep11_fr_deco_ari_event11 with dissolve
ar "Sex toys and pleasure products."
scene ep11_fr_deco_ari_event12 with dissolve
ar "Oh! Do you want to buy some?"

scene ep11_fr_deco_ari_event13 with dissolve
ar "They have these dick-cloning sets you can use on a guy you like."
scene ep11_fr_deco_ari_event14 with dissolve
ar "But, honestly, they aren't any good."
ar "I tried one on Dawe, but I had to push my thumb into it further to get something useful."
scene ep11_fr_deco_ari_event13 with dissolve
ar "I'll sell you that kit as slightly used."
scene ep11_fr_deco_ari_event15 with dissolve
js "No, thanks. I'm good."
scene ep11_fr_deco_ari_event13 with dissolve
ar "I have lots of other things in here, too! Let me show you!"
scene ep11_fr_deco_ari_event16 with dissolve
sar "Why are you selling sex toys?"
scene ep11_fr_deco_ari_event17 with dissolve
ar "I need the money. Having a baby is so freaking expensive!"
ar "Every week, I have to buy food, new clothes and diapers! And that's just for me. Think about when the baby comes!"
ar "I heard you could make a small fortune selling sex toys because everyone wants to buy them, but no one wants to sell them."
scene ep11_fr_deco_ari_event24 with dissolve
sa "Maybe you should ask girls in private. Being pushy won't get you any customers because you'll end up embarrassing them."
scene ep11_fr_deco_ari_event18 with dissolve
ar "Oh... Message received!"
scene ep11_fr_deco_ari_event19 with dissolve
ar "*{i}Whispers{/i}* So... How about it? Can I drop by your room later?"
if branchMayaJosy:
    scene ep11_fr_deco_ari_event21 with dissolve
    js "..."
    scene ep11_fr_deco_ari_event22 with dissolve
    js "Do you sell any lube?"
    scene ep11_fr_deco_ari_event19 with dissolve
    ar "By the gallon."
    scene ep11_fr_deco_ari_event23 with dissolve
    js "You do?"
    scene ep11_fr_deco_ari_event20 with dissolve
    ar "No, I don't sell it by the gallon."
    scene ep11_fr_deco_ari_event19 with dissolve
    ar "Unless you're interested."
    scene ep11_fr_deco_ari_event20 with dissolve
    ar "Josy. I need the money. If you scratch my back, I'll lube your vagina."
else:
    scene ep11_fr_deco_ari_event22 with dissolve
    js "Sure, I'll have a look..."

$ event_list.append("ep11_fr_deco_josy_event_label")
if branchMayaJosy:
    if persistent.mod_wtenabled:
        $ task_list[9] = "Talk to Josy (HOTS upstairs)"
    else:
        $ task_list[9] = "Talk to Josy"
else:
    if persistent.mod_wtenabled:
        $ optional_task_list[8] = "Talk to Josy (HOTS upstairs)"
    else:
        $ optional_task_list[8] = "Talk to Josy"
$ updateTaskList()
jump endEvent

label ep11_fr_deco_jb_event_label:
scene ep11_fr_deco_jb_event1 with dissolve
mc "All this running back and forth... Wouldn't it be easier if HOTs and DIKs didn't share decorations and kept their boxes separate?"
scene ep11_fr_deco_jb_event2 with dissolve
jb "Have you seen all the boxes we have to sort through? No one wants to re-organize that."
jb "And the current system works... Kind of."
scene ep11_fr_deco_jb_event4 with dissolve
mc "We could always organize it when we put it back into the boxes after Christmas."
scene ep11_fr_deco_jb_event3 with dissolve
jb "No, no, no. Hush, hush!"
scene ep11_fr_deco_jb_event4 with dissolve
mc "What?"
scene ep11_fr_deco_jb_event2 with dissolve
jb "We won't get much help putting everything up if we start doing that."
scene ep11_fr_deco_jb_event4 with dissolve
mc "So, keeping the boxes unorganized forces the HOTs to help us?"
scene ep11_fr_deco_jb_event2 with dissolve
jb "When you say it like that you make it sound devious."
scene ep11_fr_deco_jb_event4 with dissolve
mc "Isn't it?"
scene ep11_fr_deco_jb_event2 with dissolve
jb "They have the female touch we lack. We need their help, or the result won't look as good."
scene ep11_fr_deco_jb_event5 with dissolve
mc "Are you sure they wouldn't help if the boxes were sorted?"
scene ep11_fr_deco_jb_event6 with dissolve
jb "It was Tommy's idea."
scene ep11_fr_deco_jb_event5 with dissolve
mc "Wow, I'm surprised..."
scene ep11_fr_deco_jb_event6 with dissolve
jb "It doesn't hurt anyone. We're helping out over here, and they're helping out at our place. It's a win-win."
scene ep11_fr_deco_jb_event5 with dissolve
mc "Alright."

$ optional_task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_josy_event_label:
scene ep11_fr_deco_josy_event1 with dissolve
mc "(She's deep in thought...)"
mc "Do you like that gnome or what?"
scene ep11_fr_deco_josy_event2 with dissolve
js "Huh? Yeah. Uh...no. I was just thinking."
scene ep11_fr_deco_josy_event3 with dissolve
mc "Care to share?"
scene ep11_fr_deco_josy_event4 with dissolve
if branchMayaJosy:
    js "No, you have enough on your plate, with your dad and all."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "*{i}Sigh{/i}* Yeah..."
    scene ep11_fr_deco_josy_event6 with dissolve
    js "Sorry, I shouldn't have brought it up. You probably weren't even thinking about it now."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "No, I wasn't, but it's cool."
    scene ep11_fr_deco_josy_event13 with dissolve
    js "You don't have to pretend that it's cool, [name]. Sometimes, things just aren't. And that's perfectly fine."
    js "You're allowed to feel down."
    scene ep11_fr_deco_josy_event14 with dissolve
    mc "Thanks, Josy. I do feel down. But I'm trying to move past it."
    scene ep11_fr_deco_josy_event13 with dissolve
    js "And I get why you feel down. It's ok."
    js "About the stuff going on in my head... We'll save it for another time. I've been doing some soul-searching lately."
    scene ep11_fr_deco_josy_event14 with dissolve
    if branchMayaJosy:
        mc "About what?"
    else:
        mc "About Maya or something else?"
    scene ep11_fr_deco_josy_event13 with dissolve
    js "About...everything. I've been questioning myself a lot and trying to figure out things."
    scene ep11_fr_deco_josy_event14 with dissolve
    mc "Can I help in any way?"
    scene ep11_fr_deco_josy_event15 with dissolve
    js "I don't think you can. I think this is something I have to do on my own."
    scene ep11_fr_deco_josy_event12 with dissolve
    js "I wanna show you what I've been up to. But I'm embarrassed."
    scene ep11_fr_deco_josy_event11 with dissolve
    mc "Why are you embarrassed?"
    scene ep11_fr_deco_josy_event12 with dissolve
    js "It's hard to explain. But it's why I've kept to myself lately."
    js "I'll show you when we get a day off or something. Ok?"
    scene ep11_fr_deco_josy_event11 with dissolve
    mc "I'm looking forward to it."
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "Kiss her [m_c1][mod_choices[0]]":
            $ RPjosy += 1
            scene ep11_fr_deco_josy_event17 with dissolve
            js "*{i}Smack{/i}*"
        "Compliment her outfit [m_c1][mod_choices[0]]":
            $ RPjosy += 1
            mc "By the way, you're pretty in that outfit. You're glowing."
            scene ep11_fr_deco_josy_event16 with dissolve
            $ renpy.pause()
        "Leave":
            $ renpy.pause(0.5)
    $ task_list[9] = ""
    $ new_bio("Josy", "Josy told me she has been feeling down but wasn't ready to share why she's been keeping to herself lately.")
elif ep9_jm_sad:
    js "No, I do not."
    scene ep11_fr_deco_josy_event6 with dissolve
    js "And I know what you're thinking, but it's not about you."
    js "I've been doing some soul-searching lately. And it's...bleh..."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "Is it about Maya or something else?"
    scene ep11_fr_deco_josy_event6 with dissolve
    js "About...everything. I've been questioning myself a lot and trying to figure out things."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "Can I help in any way?"
    scene ep11_fr_deco_josy_event7 with dissolve
    js "No, I have to do this on my own."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "Well... You know where to find me."
    $ optional_task_list[8] = ""
    $ new_bio("Josy", "Josy told me she has been feeling down lately, but it had nothing to do with me.")
else:
    js "No... It's just a lot at the moment. I've been doing some soul-searching lately."
    scene ep11_fr_deco_josy_event5 with dissolve
    mc "About Maya or something else?"
    scene ep11_fr_deco_josy_event6 with dissolve
    js "About...everything. I've been questioning myself a lot and trying to figure out things."
    if ep10_feelingsForJosy:
        scene ep11_fr_deco_josy_event8 with dissolve
        js "..."
    scene ep11_fr_deco_josy_event9 with dissolve
    mc "Can I help in any way?"
    scene ep11_fr_deco_josy_event10 with dissolve
    js "I don't think you can. I think this is something I have to do on my own."
    scene ep11_fr_deco_josy_event9 with dissolve
    mc "Well... You know where to find me."
    if ep10_feelingsForJosy:
        scene ep11_fr_deco_josy_event11 with dissolve
        $ renpy.pause()
    else:
        scene ep11_fr_deco_josy_event10 with dissolve
        js "I know."
    $ optional_task_list[8] = ""
    $ new_bio("Josy", "Josy told me she has been feeling down lately.")
$ updateTaskList()
jump endEvent

label ep11_fr_deco_sarah_event_label:
$ guideSuggestedPage = 169
scene ep11_fr_deco_sarah_event1 with dissolve
$ renpy.pause()
if dtype > 0:
    scene ep11_fr_deco_sarah_event3 with dissolve
    $ renpy.pause()
scene ep11_fr_deco_sarah_event2 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Compliment her [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Nice job with the Christmas tree, Sarah. It's looking pretty."
        scene ep11_fr_deco_sarah_event4 with dissolve
        sar "Do you think pink is pretty, or is that the best you got to charm me?"
        scene ep11_fr_deco_sarah_event5 with dissolve
        mc "What? It suits you girls. Isn't pink your color?"
        scene ep11_fr_deco_sarah_event7 with dissolve
        ly "It is awfully pink."
        scene ep11_fr_deco_sarah_event8 with dissolve
        sar "Aha, what's the name of that club you work at again?"
        sar "Make yourself useful. Fetch another box of ornaments. This was the last ball."
    "Tease her [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Nice job with those balls, Sarah."
        scene ep11_fr_deco_sarah_event4 with dissolve
        sar "I'm somewhat of a ball expert."
        scene ep11_fr_deco_sarah_event6 with dissolve
        sar "You gotta grip the base and tickle them from below."
        scene ep11_fr_deco_sarah_event7 with dissolve
        ly "If you're asking me, she's being too gentle with them."
        scene ep11_fr_deco_sarah_event8 with dissolve
        sar "Trust me, I know how to handle balls."
        sar "Speaking of balls, that box is empty. Fetch another one, will you?"

scene ep11_fr_deco_sarah_event9 with dissolve
ly "Sure, I'll look for one in my room. It should take around 15 minutes."
scene ep11_fr_deco_sarah_event10 with dissolve
sar "Slacker."
scene ep11_fr_deco_sarah_event11 with dissolve
sar "What about you, [name]? Are you slacking off, too?"
scene ep11_fr_deco_sarah_event12 with dissolve
mc "No, I've done plenty today."
scene ep11_fr_deco_sarah_event11 with dissolve
sar "Still got some energy in you? Can you help me reach the highest branch?"
scene ep11_fr_deco_sarah_event12 with dissolve
mc "What for?"
scene ep11_fr_deco_sarah_event13 with dissolve
sar "For the star, of course."
scene ep11_fr_deco_sarah_event14 with dissolve
mc "Sure, I can reach that high."
scene ep11_fr_deco_sarah_event13 with dissolve
sar "No, no. You don't get to put it there. I've done a lot of work on this tree; the star is mine. Lift me up there."
scene ep11_fr_deco_sarah_event16 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sarah scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if branchAlone:
                           $ mod_choices[6] ="(Sarah scene)"

menu:
    "[m_c1]Lift her up":
        $ event_list.append("ep11_fr_deco_sarah_event4_label")
        scene ep11_fr_deco_sarah_event18 with dissolve
        mc "Alright. Here we go."
        scene ep11_fr_deco_sarah_event19 with dissolve
        $ renpy.pause()
        scene ep11_fr_deco_sarah_event21 with dissolve
        sar "Wheee!"
        scene ep11_fr_deco_sarah_event20 with dissolve
        sar "I can't reach it. Higher, [name]."
        scene ep11_fr_deco_sarah_event22 with dissolve
        mc "Hngn..."
        if not branchAlone:
            jump ep11_fr_deco_sarah_event2_label
        else:
            menu:
                "Bury your face in it \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
                    $ dk(2)
                    scene ep11_fr_deco_sarah_event25 with dissolve
                    mc "*{i}Chomp{/i}* Grr!"
                    scene ep11_fr_deco_sarah_event27 with dissolve
                    sar "Haha, hey!"
                    sar "You're such a horndog."
                    scene ep11_fr_deco_sarah_event26 with dissolve
                    mc "Did you say something?"
                    scene ep11_fr_deco_sarah_event28 with dissolve
                    sar "What was that about?"
                    if not ep9_sarah_melanie_lewd:
                        scene ep11_fr_deco_sarah_event29 with dissolve
                        menu:
                            "Just having fun":
                                mc "Nothing. I was just having fun."
                                scene ep11_fr_deco_sarah_event28 with dissolve
                                sar "Tsk. Thanks for the help."
                                jump ep11_fr_deco_sarah_event3_label
                            "I couldn't resist you \n{size=-4}[m_c2][mod_choices[6]]":
                                mc "I couldn't resist you and that hot ass in my face."
                                if ep4_ugliest_ass == "Sarah":
                                    mc "Did you work out a lot? Because it's gotten way better."
                    else:
                        scene ep11_fr_deco_sarah_event29 with dissolve
                        mc "Your ass looks amazing in those tights."
                    scene ep11_fr_deco_sarah_event28 with dissolve
                    sar "You didn't even use your tongue while you were at it. Boo..."
                    scene ep11_fr_deco_sarah_event30 with dissolve
                    $ renpy.pause()
                    scene ep11_fr_deco_sarah_event31 with dissolve
                    sar "Go, go, go."
                    mc "Huh?"
                    $ currentFreeRoamLabel = "ep11_hots_fr1_lobby_label"
                    label ep11_sarah_lewd_label:
                    if _in_replay:
                        hide screen new_phone_screen
                        if persistent.name == None:
                            $ name = "MC"
                        else:
                            $ name = persistent.name
                        $ ep11_mel_lewd = False
                        $ ep9_sarah_melanie_lewd = True
                        $ ep6_sarah_lewd = True
                        play music "music/ep11/licensed_music/track183.mp3"
                        queue music ["music/ep11/christmas_jazz.mp3","music/ep11/licensed_music/track160.mp3","music/ep11/licensed_music/track161.mp3","music/ep11/licensed_music/track179.mp3","music/ep11/licensed_music/track183.mp3","music/ep11/licensed_music/track168.mp3","music/ep11/licensed_music/track159.mp3"]
                    scene ep11_sarah_lewd1 with dissolve
                    mc "What are we doing down here?"
                    scene ep11_sarah_lewd2 with dissolve
                    sar "Trust me. This is the last place anyone would look for us today."
                    sar "Let's do it fast before Lily notices I'm gone."
                    scene ep11_sarah_lewd3 with dissolve
                    mc "Do what fast?"
                    scene ep11_sarah_lewd4 with dissolve
                    sar "Don't play dumb, you know what I mean."

                    if False:
                        sar "You buried your face in my ass at a time when I was particularly horny, and now you're gonna take care of it."
                        scene ep11_sarah_lewd5 with dissolve
                        mc "Can you give me like...an hour or so?"
                        scene ep11_sarah_lewd6 with dissolve
                        sar "We don't have an hour, you'll have to do it fast."
                        scene ep11_sarah_lewd5 with dissolve
                        mc "I mean... I have to \"reload\" downstairs."
                        scene ep11_sarah_lewd7 with dissolve
                        sar "What?"
                        scene ep11_sarah_lewd8 with dissolve
                        mc "Melanie beat you to it. She was...um... particularly horny, too."
                        scene ep11_sarah_lewd9 with dissolve
                        sar "That whore..."
                        scene ep11_sarah_lewd8 with dissolve
                        mc "Sorry... If I had known..."
                        scene ep11_sarah_lewd9 with dissolve
                        sar "Yeah, right. Gah."
                        scene ep11_sarah_lewd10 with dissolve
                        $ renpy.pause()
                        $ new_bio("Sarah", "Sarah wanted to have sex, but I had just fucked Melanie and wasn't ready to go another round.")
                        jump ep11_fr_deco_sarah_event3_label
                    else:
                        $ ep11_sarah_lewd = True
                        hide screen new_phone_screen
                        scene ep11_sarah_lewd12 with dissolve
                        if ep9_sarah_melanie_lewd:
                            mc "Hey... Last time, you told me to use my words and say what I wanted. I think it's your turn."
                            scene ep11_sarah_lewd11 with dissolve
                            sar "Fuck me fast, or don't fuck me at all. Capiche?"
                        else:
                            if ep6_sarah_lewd or in_bios("I skipped class with Sarah, but turned her down when she wanted me to pay for sex."):
                                mc "I'm not gonna pay for it. Maybe you should pay me?"
                                scene ep11_sarah_lewd11 with dissolve
                                sar "Good luck with that!"
                            else:
                                mc "Aha, do I?"
                                scene ep11_sarah_lewd11 with dissolve
                        sar "You buried your face in my ass at a time when I was particularly horny, and now you're gonna take care of it."

                    scene ep11_sarah_lewd13 with dissolve
                    mc "Do you think a guy can switch on and off like that? What if I'm not horny?"
                    scene ep11_sarah_lewd14 with dissolve
                    $ renpy.pause()
                    play sound "sound_effects/clothes.mp3"
                    scene ep11_sarah_lewd15 with vpunch
                    $ renpy.pause()
                    scene ep11_sarah_lewd16 with dissolve
                    mc "Well, aren't you a problem solver?"
                    scene ep11_sarah_lewd17 with dissolve
                    sar "No clothes are allowed in the pool area, [name]."
                    scene ep11_sarah_lewd18 with dissolve
                    $ renpy.pause()
                    scene ep11_sarah_lewd19 with dissolve
                    mc "Mmm!"
                    scene anim_sarah_tits_ep11 with dissolve
                    sar "Fast doesn't go hand in hand with foreplay."
                    mc "*{i}Suck suck{/i}* You said it yourself: this is the last place they'll look for you. I think we got some time for it."
                    pause
                    scene ep11_sarah_lewd20 with dissolve
                    sar "If that's the case... I wanna spend some time down there, too."
                    scene ep11_sarah_lewd21 with dissolve
                    mc "You don't need to convince me."
                    menu:
                        "[m_c1]Kiss her":
                            $ ep11_sarah_kiss = True
                            scene ep11_sarah_lewd22 with dissolve
                            sar "*{i}Smack{/i}*"
                            scene ep11_sarah_lewd23 with dissolve
                            $ renpy.pause()
                            scene ep11_sarah_lewd24 with dissolve
                            $ renpy.pause()
                            scene ep11_sarah_lewd25 with dissolve
                            sar "Kisses too? This is supposed to be a quick and dirty fuck, [name]."
                        "Don't kiss her":
                            $ renpy.pause(0.5)
                    scene ep11_sarah_lewd26 with dissolve
                    sar "*{i}Lick lick{/i}*"
                    scene ep11_sarah_lewd27 with dissolve
                    mc "Fuck..."
                    scene ep11_sarah_lewd28 with dissolve
                    sar "*{i}Suck suck{/i}*"
                    scene anim_sarah_bj_ep11 with dissolve
                    mc "Ahh... That feels amazing."
                    sar "*{i}Suck suck{/i}*"
                    pause
                    scene anim_sarah_bj2_ep11 with dissolve
                    sar "*{i}Suck suck glug glug{/i}*"
                    pause
                    scene ep11_sarah_lewd29 with dissolve
                    sar "Damn, you get hard fast."
                    scene ep11_sarah_lewd30 with dissolve
                    mc "Yeah... You found the on-switch, alright."
                    scene ep11_sarah_lewd29 with dissolve
                    sar "I'd hate to see the day when you need Viagra. You're gonna need a full bottle of pills to get this one up."
                    scene ep11_sarah_lewd31 with dissolve
                    $ renpy.pause()
                    scene ep11_sarah_lewd32 with dissolve
                    sar "Get over here and fuck me, [name]."
                    scene ep11_sarah_lewd33 with dissolve
                    sar "I need it inside me."
                    scene ep11_sarah_lewd34 with dissolve
                    sar "*{i}Moans{/i}* Slide it right in, [name]..."
                    scene ep11_sarah_lewd35 with dissolve
                    $ renpy.pause()
                    scene anim_sarah_miss1_ep11 with dissolve
                    sar "*{i}Moans{/i}* Fuck, yes. Give me that fat cock."
                    mc "Damn, you're wet."
                    sar "I told you I was horny."
                    pause
                    scene anim_sarah_miss2_ep11 with dissolve
                    pause
                    scene anim_sarah_miss3_ep11 with dissolve
                    pause
                    $ tmpInt = 0
                    label ep11_sarah_lewd_loop_label:
                    menu:
                        "Missionary":
                            $ tmpInt += 1
                            scene anim_sarah_miss1_ep11 with dissolve
                            pause
                            scene anim_sarah_miss2_ep11 with dissolve
                            pause
                            scene anim_sarah_miss3_ep11 with dissolve
                            pause
                            jump ep11_sarah_lewd_loop_label
                        "Doggystyle":
                            $ tmpInt += 1
                            scene anim_sarah_doggy1_ep11 with dissolve
                            pause
                            scene anim_sarah_doggy2_ep11 with dissolve
                            sar "*{i}Moans{/i}* Fuck me, [name]... Use my pussy how you want."
                            pause
                            scene anim_sarah_doggy3_ep11 with dissolve
                            pause
                            jump ep11_sarah_lewd_loop_label
                        "Doggystyle (Anal)":
                            $ tmpInt += 1
                            scene anim_sarah_doggy1_ep11 with dissolve
                            sar "*{i}Moans{/i}* Yes! Fuck my ass..."
                            pause
                            scene anim_sarah_doggy2_anal_ep11 with dissolve
                            pause
                            scene anim_sarah_doggy3_anal_ep11 with dissolve
                            pause
                            jump ep11_sarah_lewd_loop_label
                        "Cowgirl":
                            $ tmpInt += 1
                            scene anim_sarah_ride1_ep11 with dissolve
                            sar "Hnn... I wanna ride you until you cum. But don't cum yet..."
                            pause
                            scene anim_sarah_ride2_ep11 with dissolve
                            mc "Shit... You better slow down, then."
                            sar "No... *{i}Moans{/i}* This is just how I like it."
                            pause
                            jump ep11_sarah_lewd_loop_label
                        "Standing (Anal)":
                            $ tmpInt += 1
                            scene anim_sarah_stand1_ep11 with dissolve
                            sar "*{i}Moans{/i}* Yes... Bend me. Break me."
                            pause
                            scene anim_sarah_stand2_ep11 with dissolve
                            mc "Your ass feels so good around my cock."
                            pause
                            scene anim_sarah_stand3_ep11 with dissolve
                            sar "You're fucking me so good."
                            pause
                            jump ep11_sarah_lewd_loop_label
                        "Cum" if tmpInt > 2:
                            mc "I'm gonna cum."
                            sar "Cum inside. I'm not gonna clean up in here."
                            menu:
                                "In mouth":
                                    scene anim_sarah_bj3_ep11 with hpunch
                                    mc "Ahh!!! Fuck!"
                                    pause
                                    scene ep11_sarah_lewd36 with dissolve
                                    pause
                                    scene ep11_sarah_lewd37 with dissolve
                                    sar "*{i}Gulp{/i}*"
                                    scene ep11_sarah_lewd38 with dissolve
                                    sar "There we go. I got rid of that evidence."
                                    scene ep11_sarah_lewd39 with dissolve
                                    sar "*{i}Smack{/i}*"
                                    mc "That was so good."
                                "Creampie":
                                    scene anim_sarah_doggy3_ep11 with dissolve
                                    mc "I'm cumming..."
                                    scene anim_sarah_doggy4_ep11 with hpunch
                                    mc "Ahh!!! Fuck!"
                                    sar "Hngn! God! Empty your load in me, [name]. Cum!"
                                    pause
                                    scene ep11_sarah_lewd40 with dissolve
                                    sar "Are you done?"
                                    mc "Yeah... That was so good."
                                "Creampie (Anal)":
                                    scene anim_sarah_doggy3_anal_ep11 with dissolve
                                    mc "I'm cumming..."
                                    scene anim_sarah_doggy4_anal_ep11 with hpunch
                                    mc "Ahh!!! Fuck!"
                                    sar "Hngn! God! Empty your load in me, [name]. Cum!"
                                    pause
                                    scene ep11_sarah_lewd41 with dissolve
                                    sar "Are you done?"
                                    mc "Yeah... That was so good."

                    scene ep11_sarah_lewd42 with dissolve
                    sar "Totally... That was what I needed. Thanks, [name]."
                    scene ep11_sarah_lewd43 with dissolve
                    mc "The pleasure was mine. I'm up for it anytime, so that you know."
                    scene ep11_sarah_lewd42 with dissolve
                    sar "Haha, you're not that hard to persuade. That's good to know. Then I'll know where to drop by."
                    scene ep11_sarah_lewd44 with dissolve
                    sar "How's my hair?"
                    scene ep11_sarah_lewd45 with dissolve
                    mc "You look like you just exercised."
                    scene ep11_sarah_lewd46 with dissolve
                    sar "Ok, I'll tell Lily you forced me to carry some boxes."
                    if ep11_sarah_kiss:
                        scene ep11_sarah_lewd47 with dissolve
                        sar "*{i}Smack{/i}*"
                        scene ep11_sarah_lewd48 with dissolve
                        $ renpy.pause()
                        scene ep11_sarah_lewd49 with dissolve
                        sar "Thanks again."
                    scene ep11_sarah_lewd50 with dissolve
                    $ renpy.pause()
                    $ renpy.end_replay()
                    $ persistent.ep11_lewd_sarah = True
                    $ calcScenes()
                    if ep11_sarah_kiss:
                        $ new_bio("Sarah", "I had sex with Sarah in the HOTs' pool area. I even kissed her a couple of times. It was nice.")
                    else:
                        $ new_bio("Sarah", "I had sex with Sarah in the HOTs' pool area.")
                    $ mphone_stats_add_girl_s3("sarah","You had sex with Sarah in the HOTs' pool area in episode 11.")
                "Just hold her [m_c1][mod_choices[2]]":
                    $ dk(-1)
                    label ep11_fr_deco_sarah_event2_label:
                    scene ep11_fr_deco_sarah_event23 with dissolve
                    sar "I almost got it now!"
                    scene ep11_fr_deco_sarah_event24 with dissolve
                    sar "There we go! I'm done."
                    scene ep11_fr_deco_sarah_event28 with dissolve
                    sar "Thank you."
    "Get a stool":
        scene ep11_fr_deco_sarah_event15 with dissolve
        mc "Sage, can Sarah borrow that stool?"
        scene ep11_fr_deco_ari_event24 with dissolve
        sa "Yeah, in a minute. This fucking star refuses to hang straight. It's driving me nuts."
        scene ep11_fr_deco_sarah_event16 with dissolve
        mc "Looks like you got yourself a short break, too."
        scene ep11_fr_deco_sarah_event17 with dissolve
        sar "Suits me perfectly. I was looking for an excuse anyway."
        scene ep11_fr_deco_sarah_event16 with dissolve
        mc "Now, who's the slacker?"

label ep11_fr_deco_sarah_event3_label:
$ optional_task_list[6] = ""
$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep11_fr_deco_flower_event_label:
scene ep11_fr_deco_flower_event1 with dissolve
$ renpy.pause()
scene ep11_fr_deco_flower_event2 with dissolve
jm "Here. They seem to be ready."
scene ep11_fr_deco_flower_event3 with dissolve
mc "Ready for what?"
scene ep11_fr_deco_flower_event2 with dissolve
jm "This is as beautiful as they're going to look. You should put them in your room and enjoy them."
scene ep11_fr_deco_flower_event4 with dissolve
jm "Nicely done, [name]. This was all you. I'm proud of you."
scene ep11_fr_deco_flower_event5 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Josy)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        

menu:
    "Thanks, Jamie [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Thanks, Jamie, for showing me how to do it. I don't think I would have done it if it weren't for you."
    "You sound like my dad [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Stop it; you sound like my dad."
scene ep11_fr_deco_flower_event4 with dissolve
jm "Keep watering them and they'll last a while."
scene ep11_fr_deco_flower_event5 with dissolve
mc "Only for a while, huh?"
scene ep11_fr_deco_flower_event6 with dissolve
jm "They are flowers, [name]. Eventually, they will wither and die. It's sad, but that's how all life works."
jm "You gotta appreciate the moment you have with them. Just like I did with Franz..."
scene ep11_fr_deco_flower_event5 with dissolve
mc "It's a lot of effort for something that doesn't last long."
scene ep11_fr_deco_flower_event4 with dissolve
jm "If that makes you sad, I can teach you about perennials in the spring."
jm "Those flowers die but return to blossom again every year."
scene ep11_fr_deco_flower_event7 with dissolve
$ renpy.pause()
if steamAchievements:
    $ achievement.grant("IDS3_42")
    init:
        $ achievement.register("IDS3_42")
    $ achievement.Sync()
$ new_bio("Jamie", "Jamie gave me the flowers I had watered and taken care of. I put them in my room.")
$ ep11_flowers = True
$ optional_task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_sl_event_label:
scene ep11_fr_deco_sl_event1 with dissolve
ly "[name]... Can you decorate the tree instead of me?"
scene ep11_fr_deco_sl_event2 with dissolve
mc "Can't. I'm carrying boxes back and forth."
scene ep11_fr_deco_sl_event1 with dissolve
ly "Pretty please... I'll give you another blowjob."
scene ep11_fr_deco_sl_event3 with dissolve
sar "Unless you intend to give him one here, we don't need to know about it."
scene ep11_fr_deco_sl_event4 with dissolve
ly "Yeah, I bet you'd wanna watch, maybe even join."
if ep11_sarah_lewd:
    scene ep11_fr_deco_sl_event4b with dissolve
    sar "Haha... If you only knew."
scene ep11_fr_deco_sl_event5 with dissolve
$ renpy.pause()
scene ep11_fr_deco_sl_event6 with dissolve
sa "[name], can I talk to you?"
scene ep11_fr_deco_sl_event7 with dissolve
$ renpy.pause()
scene ep11_fr_deco_sl_event8 with dissolve
sa "I've noticed something that I'm not sure you're aware of."
scene ep11_fr_deco_sl_event10 with dissolve
mc "And that is...?"
scene ep11_fr_deco_sl_event11 with dissolve
sa "Lily. I know she's a sister, and I'm supposed to have her back and all, but when it comes to you, I..."
sa "Are you aware she's using you?"
scene ep11_fr_deco_sl_event10 with dissolve
mc "We're actually rolling."
scene ep11_fr_deco_sl_event12 with dissolve
sa "What the hell does that mean?"
scene ep11_fr_deco_sl_event10 with dissolve
mc "Uh... Ok, you got me. I don't know what it means either; I thought you did."
mc "We made a deal to act a certain way around each other and to hang out and have sex."
scene ep11_fr_deco_sl_event11 with dissolve
sa "So, you are aware she's using you?"
scene ep11_fr_deco_sl_event10 with dissolve
mc "She's not using me. We...uh... I know why you might think she is, but I can't explain this better than what I just did."
scene ep11_fr_deco_sl_event11 with dissolve
sa "And you're ok with that?"
scene ep11_fr_deco_sl_event10 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(For Lily path)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "I hope for something more \n{size=-4}[m_c1][mod_choices[0]]":
        $ ep11_lily_want_more = True
        mc "I like her, and maybe one day, Lily wants to be more serious with me. I mean... I hope so."
        mc "Rolling with her works for me while she figures it out."
        $ new_bio("Lily", "I told Sage I hoped my relationship with Lily would turn serious in the future.")
    "I like it the way it is":
        $ ep11_lily_want_more = False
        mc "Yeah. I like her, and we do things together without being a couple."
        mc "It's perfect for me. I can pursue whatever I want without worrying about what Lily thinks."
        mc "So, if you see her as using me, then you'd have to say that I'm using her too."
        $ new_bio("Lily", "I told Sage I was rolling with Lily and that it didn't mean anything serious.")
scene ep11_fr_deco_sl_event9 with dissolve
sa "From where I stand, she's making you look bad. You look like a tool."
scene ep11_fr_deco_sl_event14 with dissolve
mc "A tool? What the hell do you mean?"
scene ep11_fr_deco_sl_event13 with dissolve
sa "Dude, you're worth more than being used by someone like her."
sa "I don't know if you think it's a good look that she talks about you getting blowjobs from her in public like that, but trust me, it's not."
sa "It looks tacky and bad. That's not the [name] that I know."
scene ep11_fr_deco_sl_event10 with dissolve
mc "What do you want me to do? I enjoy spending time with Lily, so I'm gonna."
mc "And so what? She makes some sexual jokes in front of others - that doesn't bother me."
scene ep11_fr_deco_sl_event9 with dissolve
sa "It becomes something more than jokes, the way she's doing it."
sa "And when she talks about using you that way, it reinforces that bad image of you."
sa "I don't like to hear her talk about you like this. I've seen her do it when you're not around, too."
sa "I wanted you to have some self-respect."
scene ep11_fr_deco_sl_event10 with dissolve
menu:
    "I have self-respect":
        mc "I have self-respect. It's not a one-way street with Lily."
        scene ep11_fr_deco_sl_event14 with dissolve
        if ep4_fuckedSage:
            mc "It's not a lot different from what you and I once did. Fuck buddies, remember?"
        else:
            mc "I see it more like friends with benefits."
        mc "Yeah! That's a good description of it."
        scene ep11_fr_deco_sl_event12 with dissolve
        sa "If you say so."
        scene ep11_fr_deco_sl_event10 with dissolve
        mc "Why are you this upset about it?"
        scene ep11_fr_deco_sl_event13 with dissolve
        sa "Because I care about you, you moron. Like you care about me."
    "You're wrong":
        mc "You're wrong about her. And you're wrong about me, too. I know what I'm doing."
        scene ep11_fr_deco_sl_event12 with dissolve
        sa "You couldn't even describe what you guys were doing a minute ago."
        scene ep11_fr_deco_sl_event14 with dissolve
        mc "I don't have to be able to describe it to know that it's something I wanna do."
        scene ep11_fr_deco_sl_event13 with dissolve
        sa "Fine, then go ahead and do it!"
        scene ep11_fr_deco_sl_event14 with dissolve
        mc "I will! What's your damn problem?"
        scene ep11_fr_deco_sl_event15 with dissolve
        sa "..."
        scene ep11_fr_deco_sl_event13 with dissolve
        sa "My problem is that I care about you like you care about me."
scene ep11_fr_deco_sl_event15 with dissolve
mc "Sage..."
mc "I'm sorry."
scene ep11_fr_deco_sl_event16 with dissolve
sa "Don't be. I shouldn't have brought it up."

$ new_bio("Sage", "Sage told me Lily was using me and that it made me look bad.")
$ event_list.append("ep11_fr_deco_lily_event_label")
jump endEvent

label ep11_fr_deco_lily_event_label:
scene ep11_fr_deco_lily_event1 with dissolve
ly "Turning down a blowjob like that... *{i}Tsk tsk{/i}* Did you hit your head or something?"
scene ep11_fr_deco_lily_event2 with dissolve
mc "I'm not in the mood for one."
scene ep11_fr_deco_lily_event3 with dissolve
ly "Hm... My intuition picks up on anger or annoyance...or both."
ly "Ok, tell me what Sage said."
scene ep11_fr_deco_lily_event4 with dissolve
mc "She didn't say anything special."
scene ep11_fr_deco_lily_event3 with dissolve
ly "Lies. You were perfectly fine before you talked to her. She must have said something."
if ep11_follow_quinn and not ep10_lily_english and not wt_ep11_quinn_lilly:
    ly "You don't seem to get it, [name]. If you want to roll with me, you need to have my back."
scene ep11_fr_deco_lily_event4 with dissolve
mc "I'm not gonna start an argument about this. We had a misunderstanding, that's all."
scene ep11_fr_deco_lily_event5 with dissolve
$ renpy.pause()
scene ep11_fr_deco_lily_event6 with dissolve
ly "At the barbecue, Sage was annoyed at me when I talked about you. I think she doesn't like that we are together."
ly "I believe she's jealous."
scene ep11_fr_deco_lily_event8 with dissolve
if pathSage or ep7_pathSage:
    mc "We have some history, but I don't think she's jealous. We're good friends, and she cares about me."
else:
    mc "No, that's not what it is. We're good friends and she cares about me."
scene ep11_fr_deco_lily_event7 with dissolve
ly "Bullshit."
scene ep11_fr_deco_lily_event8 with dissolve
mc "It's not bullshit. You don't know how close I am to Sage."
scene ep11_fr_deco_lily_event7 with dissolve
ly "I'm not calling bullshit on you two being good friends, but I don't believe for a second that it's all there is to it."
ly "And you know I don't care if there is either."
ly "But I care if she's trying to turn you against me. I'm not gonna put up with that."
scene ep11_fr_deco_lily_event8 with dissolve
mc "She's not. She was concerned I was being used, but I told her I wasn't."
scene ep11_fr_deco_lily_event9 with dissolve
ly "Ugh... She should mind her fucking business. You know what this is."
ly "I'm not using you. We're using each other."
scene ep11_fr_deco_lily_event10 with dissolve
mc "That doesn't make it better."
scene ep11_fr_deco_lily_event9 with dissolve
ly "For whom? You or her?"
scene ep11_fr_deco_lily_event10 with dissolve
mc "I think it might look bad."
scene ep11_fr_deco_lily_event11 with dissolve
ly "That's not you talking. She put that thought in your head."
ly "You know it doesn't look bad; it looks good. We look good together."
scene ep11_fr_deco_lily_event10 with dissolve
mc "Maybe it looks bad when you talk about what you're gonna do to me and when we grope each other in public."
scene ep11_fr_deco_lily_event11 with dissolve
ly "I knew she put these thoughts in your head. I'm gonna talk to her."
scene ep11_fr_deco_lily_event12 with dissolve
mc "Wait. Don't... There's no need to do that."
scene ep11_fr_deco_lily_event13 with dissolve
ly "[name]... I'm not forcing you to do any of this, am I? Didn't you want this?"
scene ep11_fr_deco_lily_event15 with dissolve
mc "I wanted to try it, yeah. I wasn't sure what it entailed, and honestly, it's not gotten much clearer with time."
mc "But I am fine with it. However, I didn't think about what others would think of me."
scene ep11_fr_deco_lily_event13 with dissolve
ly "And why does it matter if someone doesn't like seeing it? People will judge you no matter what you do."
ly "You can be the most perfect girl in school and get ridiculed because you're too smart or ugly..."
scene ep11_fr_deco_lily_event14 with dissolve
ly "...or you can dress slutty and act cool, but others will think you're trash."
ly "There's no way to please all people, so please yourself."
scene ep11_fr_deco_lily_event15 with dissolve
ly "..."
scene ep11_fr_deco_lily_event14 with dissolve
ly "And yeah, I'm talking about myself."
scene ep11_fr_deco_lily_event15 with dissolve
mc "I figured you were. I'm not a perfect girl."
scene ep11_fr_deco_lily_event16 with dissolve
$ renpy.pause()
scene ep11_fr_deco_lily_event17 with dissolve
$ renpy.pause()
scene ep11_fr_deco_lily_event18 with dissolve
ly "I'm not stupid. I know what people think when they look at me."
ly "They see this girl who dresses provocatively and oozes confidence."
ly "They most likely think I've got daddy issues and come from a broken home, but that's so fucking far from the truth."
scene ep11_fr_deco_lily_event19 with dissolve
ly "I wasn't always like this..."
ly "What you see in front of you now, picture the opposite."
ly "I was this chunky, dorky girl who wore braces and sundresses because that's what my mom bought for me."
scene ep11_fr_deco_lily_event20 with dissolve
ly "And I've always been somewhat bright. That's also something people don't picture when they see me."
ly "If there is such a thing, I was too bright in school."
ly "You can figure out how classmates treat smart, fat, and ugly girls who get praised by teachers, especially when they feel too stupid in school themselves."
scene ep11_fr_deco_lily_event21 with dissolve
mc "You were bullied, too?"
scene ep11_fr_deco_lily_event20 with dissolve
ly "Too, huh?"
scene ep11_fr_deco_lily_event21 with dissolve
mc "Yep."
scene ep11_fr_deco_lily_event22 with dissolve
ly "Then you know how it was like. To not have any friends or to sit alone at recess every day..."
ly "...wishing the day would end so you could get back home and eat to feel something good."
scene ep11_fr_deco_lily_event23 with dissolve
ly "That was me until high school."
ly "We moved here, and I didn't know anyone, so this was my chance to start anew."
ly "I was so sick of my old self and wanted a change - any fucking change."
scene ep11_fr_deco_lily_event24 with dissolve
ly "I didn't want to be this girl with no friends, so I changed everything about myself."
ly "If everything I used to be was wrong in the eyes of others, I figured doing the opposite would take me where I wanted to go."
scene ep11_fr_deco_lily_event25 with dissolve
ly "I stopped eating, and my parents got concerned. I cut my clothes with scissors to make them look alternative."
ly "I skipped school. I started smoking. I met the same kind of people and made friends."
scene ep11_fr_deco_lily_event26 with dissolve
ly "All of a sudden I felt something different about myself. I felt accepted."
ly "But while doing that, I turned away others, and my family got increasingly worried about me."
scene ep11_fr_deco_lily_event27 with dissolve
ly "When I came back home with my tattoo, they were so angry. Mom screamed at me; Dad called it ugly and said I had ruined my skin."
ly "Mom and Dad said I was throwing away everything I had going for me. They said they couldn't even recognize me anymore."
scene ep11_fr_deco_lily_event28 with dissolve
ly "After graduating, I wanted to take a break from school, so I started working as a stripper."
ly "When Mom and Dad found out, it was like a death knell. In their eyes, I was gone."
scene ep11_fr_deco_lily_event29 with dissolve
ly "In a last-ditch effort, Dad told me to choose between living at home and working at The Pink Rose."
ly "I don't know if he thought that would work, and it didn't. I moved out that weekend and shared a flat with a friend."
scene ep11_fr_deco_lily_event24 with dissolve
ly "You can't please everyone, [name]. I made those choices, and I stand by them."
ly "Even if it weren't in the way my parents wished, I grew a lot from all of that."
ly "And that doesn't mean I'm throwing my life away. It's the opposite. I finally feel like I'm living it."
scene ep11_fr_deco_lily_event30 with dissolve
ly "So what if I make a joke about sucking your dick and people overhear?"
ly "They'd think I was boring if I never did something like that. And if I do, they either think I'm fun, sexy or disgusting."
ly "There's no winning. But I can tell you this..."
scene ep11_fr_deco_lily_event31 with dissolve
ly "Not once have I regretted changing the way I did."
ly "I prefer this version of me a hell of a lot more than the sad, fat and pathetic Lily who cried herself to sleep."
scene ep11_fr_deco_lily_event32 with dissolve
$ renpy.pause()
if not ep11_lily_want_more:
    scene ep11_fr_deco_lily_event33 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event34 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event35 with dissolve
    mc "Nor should you regret it. I think you turned out great."
    scene ep11_fr_deco_lily_event36 with dissolve
    ly "Thanks, [name]."
    ly "Don't tell anyone I told you this. Not a soul."
    scene ep11_fr_deco_lily_event35 with dissolve
    mc "Don't worry, I've got your back."
    scene ep11_fr_deco_lily_event36 with dissolve
    ly "I told you this so that you'll understand me better."
    scene ep11_fr_deco_lily_event35 with dissolve
    mc "Got it..."
else:
    scene ep11_fr_deco_lily_event39 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event40 with dissolve
    ly "This is not necessary, [name]."
    scene ep11_fr_deco_lily_event41 with dissolve
    mc "For me, it is."
    scene ep11_fr_deco_lily_event42 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event43 with dissolve
    ly "Don't tell anyone I told you this. Not a soul."
    scene ep11_fr_deco_lily_event44 with dissolve
    mc "I felt sad hearing it."
    scene ep11_fr_deco_lily_event43 with dissolve
    ly "You don't have to feel sad. I don't feel sad anymore."
    ly "I told you this so that you'll understand me better."
    scene ep11_fr_deco_lily_event44 with dissolve
    mc "You have no idea how much it helped me do that."
    scene ep11_fr_deco_lily_event45 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event46 with dissolve
    $ renpy.pause()
    scene ep11_fr_deco_lily_event47 with dissolve
    $ renpy.pause()

scene ep11_fr_deco_lily_event48 with dissolve
ly "I won't start something with Sage if you're worried."
ly "But I don't like her questioning what we're doing together. Don't let that get to you."
scene ep11_fr_deco_lily_event49 with dissolve
mc "I make my own choices just like you did."
scene ep11_fr_deco_lily_event48 with dissolve
ly "That's all I ask."
ly "And I'll tone down the innuendos and sex talk a tad, but I'm not gonna stop. That's not me."
scene ep11_fr_deco_lily_event49 with dissolve
mc "Don't worry. Be yourself. That's why I want to roll with you."
scene ep11_fr_deco_lily_event50 with dissolve
ly "I knew I picked you for a good reason."
if not ep11_lily_want_more:
    scene ep11_fr_deco_lily_event37 with dissolve
    $ renpy.pause()
else:
    scene ep11_fr_deco_lily_event38 with dissolve
    $ renpy.pause()

$ new_bio("Lily", "Lily shared about her past, and I understood her better. She was annoyed that Sage tried to meddle.")
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_camila_event_label:
scene ep11_fr_deco_camila_event1 with dissolve
mc "Are you not big on decorations?"
scene ep11_fr_deco_camila_event2 with dissolve
cam "I'm not big on Christmas. We don't celebrate it in my family."
cam "I like the decorations, but I don't know what I dare to put up without Rio's consent."
scene ep11_fr_deco_camila_event3 with dissolve
cam "Knowing her, I'd have to redo everything because it isn't straight or doesn't look good enough, haha..."
scene ep11_fr_deco_camila_event1 with dissolve
mc "Is Riona still sick?"
scene ep11_fr_deco_camila_event2 with dissolve
cam "Yeah, she hasn't even stopped by to get any of her clothes."
scene ep11_fr_deco_camila_event4 with dissolve
mc "It must be one hell of a bug. Is she ok?"
scene ep11_fr_deco_camila_event5 with dissolve
cam "She doesn't answer when I call but replies to some of my texts saying she's sick."
cam "I told her I was worried and even offered to bring her clothes and books, but she asked me to stay away."
scene ep11_fr_deco_camila_event4 with dissolve
mc "Aw, poor Rio. I hope she gets better soon, she's gonna miss a lot of school."
scene ep11_fr_deco_camila_event5 with dissolve
cam "Yeah, I know. She was already worried about her studies, thinking she wasn't doing well enough."
scene ep11_fr_deco_camila_event4 with dissolve
mc "I'd be stressed out if I were her. Do you think we can help her somehow?"
scene ep11_fr_deco_camila_event5 with dissolve
cam "We're not in any of her classes, so I doubt it. But you could always ask; I think she'd appreciate it."
scene ep11_fr_deco_camila_event4 with dissolve
mc "Noted."
mc "And hey, since she's not here, go nuts with the decorations. I think that will cheer her up."
scene ep11_fr_deco_camila_event6 with dissolve
cam "Haha, no. It would trigger her OCD."
cam "She'd laugh at it, but I know it would make her feel more stressed, and she doesn't need that. I will stay conservative with the decorations."
$ task_list[10] = ""

$ optional_task_list[5] = "Contact Riona"
$ new_chat_msg("Riona",False,1)

$ updateTaskList()
jump endEvent

label ep11_fr_deco_sage_event_label:
$ guideSuggestedPage = 169
scene ep11_fr_deco_sage_event1 with dissolve
mc "Good job! It's starting to look Christmassy."
scene ep11_fr_deco_sage_event2 with dissolve
sa "Yeah, it is. How is it going over at your place?"
scene ep11_fr_deco_sage_event1 with dissolve
mc "We're doing fine. We've gotten a lot done so far."
scene ep11_fr_deco_sage_event3 with dissolve
sa "I had a talk with Dawe earlier today. I don't know if the news reached you yet, but we have to attend their Christmas party."
scene ep11_fr_deco_sage_event5 with dissolve
mc "What does that mean for us?"
scene ep11_fr_deco_sage_event3 with dissolve
sa "They chose the same date as you guys, and we made that deal with them...so..."
scene ep11_fr_deco_sage_event5 with dissolve
menu:
    "Blow it off":
        mc "Can't you blow it off and come to ours instead?"
        scene ep11_fr_deco_sage_event4 with dissolve
        sa "The HOTs are honoring the deal, [name]. We have to."
        scene ep11_fr_deco_sage_event5 with dissolve
        mc "All of you? What if they get a few of you and the rest come to our party?"
        scene ep11_fr_deco_sage_event4 with dissolve
        sa "I'm sorry, but no. It's not gonna happen. You'll have to do without us."
    "I understand":
        mc "I understand. I'm aware of the deal."
        scene ep11_fr_deco_sage_event4 with dissolve
        sa "I'm sorry. You'll have to do without us at your Christmas party."
scene ep11_fr_deco_sage_event5 with dissolve
mc "What about New Year's Eve?"
scene ep11_fr_deco_sage_event3 with dissolve
sa "We haven't decided yet, but I fear there will be a heated discussion. Honestly, it's hard to say what's fair."
sa "It sounded like a good idea when we made the deal, but in reality, it's tricky to navigate without pissing anyone off."
scene ep11_fr_deco_sage_event4 with dissolve
sa "Dawe was gloating after I said we were coming to the jocks' Christmas party."
scene ep11_fr_deco_sage_event5 with dissolve
mc "Before you agree to anything else, include us in the discussion. We want you with us on New Year's Eve."
scene ep11_fr_deco_sage_event4 with dissolve
sa "This is hard, [name]."
scene ep11_fr_deco_sage_event5 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Sage)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "You're doing great \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[2]]":
        $ RPsage += 1
        $ dk(-1)
        scene ep11_fr_deco_sage_event1 with dissolve
        mc "I know, but I think you're doing great. It's not easy to please everyone. It's impossible even."
        scene ep11_fr_deco_sage_event2 with dissolve
        sa "Thank you."
    "I bet it is":
        mc "I bet it is."
    "Don't let the jocks win \n{size=-4}[m_c1][mod_choices[1]]":
        $ RPsage -= 1
        mc "I get it, but don't let the jocks win."
        scene ep11_fr_deco_sage_event3 with dissolve
        sa "That's not what I'm doing. Didn't you listen? I'm trying to be fair to everyone."
        scene ep11_fr_deco_sage_event5 with dissolve
        mc "I know. I'm just saying."

$ new_bio("Sage", "Sage told me she found it hard to deal with the DIKs and the jocks. She said it was hard not to piss someone off with her decisions.")
$ event_list.append("ep11_fr_deco_tj_event_label")
if persistent.mod_wtenabled:
    $ task_list[6] = "Talk to Jamie and Tommy (Main Party room)"
else:
    $ task_list[6] = "Talk to Jamie and Tommy"
if ep10_rolling:
    $ task_list[7] = "Talk to Lily"
    $ event_list.append("ep11_fr_deco_sl_event_label")
$ updateTaskList()
jump endEvent

label ep11_fr_deco_da_event_label:
scene ep11_fr_deco_da_event1 with dissolve
ash "Here we go."
scene ep11_fr_deco_da_event2 with vpunch
ash "Ouch!"
de "What's wrong?"
scene ep11_fr_deco_da_event3 with dissolve
ash "The stupid wreath pricked my finger."
scene ep11_fr_deco_da_event4 with dissolve
de "It doesn't look like much; you'll be fine."
scene ep11_fr_deco_da_event5 with dissolve
ash "Of course, I'll be fine. That's not the point. It stung like crazy."
scene ep11_fr_deco_da_event6 with dissolve
de "I can hang the wreath for you."
scene ep11_fr_deco_da_event5 with dissolve
ash "No. This is why you need me here. You won't put it straight."
scene ep11_fr_deco_da_event6 with dissolve
de "It's all yours, but watch your fingers."
scene ep11_fr_deco_da_event7 with dissolve
$ renpy.pause()
$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_q_event_label:
if branchAlone and ep8_quinn_lewd:
    if ep10_quinn_help:
        scene ep11_fr_deco_q_event1 with dissolve
        qu "Yeah?"
        scene ep11_fr_deco_q_event2 with dissolve
        mc "It's been too long now, Quinn. We've stopped talking. You don't contact me or try to initiate conversation anymore."
        mc "And you're not giving me a lot when I try to talk to you."
        scene ep11_fr_deco_q_event3 with dissolve
        qu "[name], I'm not ready."
        scene ep11_fr_deco_q_event4 with dissolve
        mc "Ready for what?"
        scene ep11_fr_deco_q_event3 with dissolve
        qu "To share things with you."
        scene ep11_fr_deco_q_event5 with dissolve
        $ renpy.pause()
        scene ep11_fr_deco_q_event4 with dissolve
        mc "Did I do something wrong? I thought I made it clear that you can trust me with it."
        if ep10_rolling:
            mc "Is this about Lily or something else?"
        scene ep11_fr_deco_q_event3 with dissolve
        if ep10_rolling:
            qu "It's not about Lily, and it's not about you."
        else:
            qu "It's not about you."
        scene ep11_fr_deco_q_event4 with dissolve
        mc "Ok."
        menu:
            "Hug her":
                scene ep11_fr_deco_q_event7 with dissolve
                qu "[name], no."
                scene ep11_fr_deco_q_event8 with dissolve
                mc "You'd feel better."
                scene ep11_fr_deco_q_event7 with dissolve
                qu "I won't."
            "Place a hand on her shoulder":
                scene ep11_fr_deco_q_event6 with dissolve
                $ renpy.pause()
            "Leave":
                $ renpy.pause(0.5)
        $ new_bio("Quinn", "Quinn wouldn't let me in despite my efforts, and we'd almost stopped talking.")
    else:
        scene ep11_fr_deco_q_event1 with dissolve
        qu "What do you want?"
        scene ep11_fr_deco_q_event2 with dissolve
        mc "Nothing. Just checking what's up."
        scene ep11_fr_deco_q_event1 with dissolve
        qu "Not much."
        scene ep11_fr_deco_q_event2 with dissolve
        mc "Alright... I'm helping up with decorations and such..."
        mc "..."
        mc "I...should get back to it."
        $ new_bio("Quinn", "Quinn and I continued to slip further away from each other. She wouldn't talk to me.")
else:
    scene ep11_fr_deco_q_event1 with dissolve
    qu "What do you want?"
    scene ep11_fr_deco_q_event2 with dissolve
    mc "Nothing. Just checking what's up."
    scene ep11_fr_deco_q_event1 with dissolve
    qu "Go away. I've got nothing to say to you."
    scene ep11_fr_deco_q_event2 with dissolve
    mc "(Moody...)"
    $ new_bio("Quinn", "Quinn didn't want to talk to me.")

$ task_list[9] = ""
$ optional_task_list[9] = ""
$ updateTaskList()
jump endEvent


label ep11_fr_deco_pp_event_label:
label ep11_pp_label:
scene ep11_pp1 with dissolve
mc "(One kickass party coming up...)"
scene ep11_pp2 with dissolve
mc "(WWTD?)"
mc "(He'd think a pure Christmas party is lame. Like he told Jamie, he wants girls to sit in his lap.)"
mc "(Tommy cares about keeping the party sexy.)"
if affinity == "DIK":
    mc "(And I have no fucking problem with that. That's easy to fix...)"
elif affinity == "CHICK":
    mc "(It will be outside my comfort zone to plan a sexy party without him, but... WWTD?)"
else:
    mc "(I should be able to manage that... Yeah...)"
scene ep11_pp3 with dissolve
mc "(It will be a Christmas party...but...)"
play sound "sound_effects/whoosh_2.mp3"
scene ep9_party_planning33
tm "And before you go asking me for advice again, let me say what I think."
tm "We should get dirty and naughty."
scene ep9_party_planning32 with dissolve
mc "Sure. So, what about that blindfold game I mentioned?"
scene ep9_party_planning34 with dissolve
tm "It's decent, but it's not for Halloween. Why would we? It's much better suited for a panty party or something."
scene ep9_party_planning32 with dissolve
mc "Panty parties? We have those?"
play sound "sound_effects/whoosh_2.mp3"
scene ep11_pp4
mc "(I've got it! It's a Christmas Panty party!)"
mc "(Everyone parties in their underwear, but we also celebrate Christmas!)"
mc "(Everyone will be almost naked; it doesn't get sexier than that. Tommy would love that!)"
scene ep11_pp5 with dissolve
mc "(I'll leave the budget as a question mark for now... I think I know how to balance it.)"
mc "(The theme should be ok because they've done it in the past. I need to make sure all guests are ok with it, though...)"
mc "(Then we have the usual stuff. Drinks, food...)"
mc "(I can't forget about the decor, but that one should be simple, considering we've been decorating today without realizing it was for the party.)"
scene ep11_pp6 with dissolve
mc "(Hm... If guests are uncomfortable, or to make them more comfortable in underwear, we can have cheap masks by the door.)"
mc "(That's not a bad idea.)"
scene ep11_pp7 with dissolve
mc "(What else would Tommy do?)"
mc "(I'm sure he would come up with some awesome stuff to do at the party.)"
scene ep11_pp8 with dissolve
mc "(Come on... Channel Tommy. What would he come up with?)"
scene ep11_pp9 with dissolve
mc "(He would make...girls...)"
scene ep11_pp10 with dissolve
mc "(...suck...?)"
mc "(...on a cucumber...)"
scene ep11_pp11 with dissolve
mc "(...in front of guys. And the first guy who gets a boner loses!)"
mc "(No, wait! The girl wins! That will make them wanna compete. Make it about the girl...)"
scene ep11_pp12 with dissolve
mc "(Dear God... I'm Tommy right now.)"
if affinity == "DIK":
    scene ep11_pp11 with dissolve
    mc "(This is awesome!)"
elif affinity == "CHICK":
    scene ep11_pp13 with dissolve
    mc "(I'm...disgusting...but it's working.)"
else:
    mc "(I...don't know how to feel about that.)"
scene ep11_pp14 with dissolve
mc "(A wet T-shirt contest! Girls, beer, boobs, what's not to love?)"
mc "(These ideas write themselves!)"
scene ep11_pp15 with dissolve
mc "(A Guess Who game? Like the one with the blindfold, maybe...)"
mc "(No. Think bigger. Include more people in it...)"
mc "(Some kind of a guessing game...)"
mc "(Girls stand behind a curtain...)"
scene ep11_pp16 with dissolve
mc "(They show a body part...and everyone on the other side must guess who it is.)"
mc "(Most correct answers win. Is that fun?)"
scene ep11_pp15 with dissolve
mc "(It could be, depending on what body part they'd show. There's potential there, for sure.)"
mc "(It would be fun if there were something that lasted the entire night, too...)"
mc "(...)"
scene ep11_pp16 with dissolve
mc "(There's a bowl by the door with folded pieces of paper.)"
mc "(Guests pick one paper each as they show up, and they get tasked with a mission.)"
scene ep11_pp17 with dissolve
mc "(Accomplish your mission before midnight, or you get booted.)"
mc "(And the missions are sexy like...um... Kiss a guy or make out with a girl...or... I will need some help with the missions, but this is good.)"
mc "(And I'll call it...)"
mc "(The Dirty Bowl.)"
scene ep11_pp18 with dissolve
mc "(That's a cheap activity in more ways than one. We're doing that one...)"
mc "(Let's add some other options and ask around later...)"
scene ep11_pp19 with dissolve
mc "(Ok, ok... Let's plan the details; we've got this.)"
$ pp_dik_list[5] = "mc"
if minigames:
    $ pp_happiness_level[5] = 10
else:
    $ pp_nm_dik_happiness[5] = 0
$ pp_happiness_icon[5] = 0
$ pp_update_happiness_icons()
$ guideSuggestedPage = 171
$ pp_activity_choices = [2,2,2]
if not minigames:

    $ pp_nm_party_preference = [[0,1,-1],[1,0,0],[0,-1,0],[0,2,-1],[-1,-1,0],[-1,0,0],[-1,-1,1],[-1,1,0]]
    $ pp_nm_activity_description = [["Alcohol and Food","Alcohol","Don't care","Not B.Y.O.B."],["Wet T-shirt","Cucumber Competition","Don't care","Anything"],["Guess Who? Game","Don't care"]]
    $ currentActivity = 0
    $ pp_money = 20
else:
    $ pp_money = 20

if not minigames:
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "(How much do we wanna spend on food and drinks?)"
menu:
    "Alcohol and Food ($4)" if minigames or pp_money > 3:
        $ pp_money -= 4
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 0
        mc "(Probably a lot. It's Christmas, after all.)"
    "Alcohol ($2)" if minigames or pp_money > 1:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_money -=2
        $ pp_activity_choices[0] = 1
        mc "(Probably some. It's Christmas, after all.)"
    "B.Y.O.B.":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 2
        mc "(Eh... Maybe people can bring their own booze for a change.)"

if not minigames:
    $ currentActivity = 1
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "(About those activities I thought of... What should we do first?)"
menu:
    "Wet T-shirt ($4)" if minigames or pp_money > 3:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 0
        $ pp_money -= 4
        mc "(The wet T-shirt contest, for sure... It will cost us, but it's a good one.)"
    "Cucumber Competition ($2)" if minigames or pp_money > 1:
        $ pp_money -= 2
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 1
        mc "(Let's do the cucumber contest. It's not that expensive, but it's still a fun one.)"
    "Nothing":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 2
        mc "(Maybe The Dirty Bowl will be enough at the start of the evening.)"


if not minigames:
    $ currentActivity = 2
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "(And later on at the party...)"
menu:
    "Guess Who? Game ($2)" if minigames or pp_money > 1:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 0
        $ pp_money -= 2
        mc "(We'll have that Guess Who game. Guests should be drunk by now. See, Tommy... I learned something from you.)"
    "Nothing":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 1
        mc "(Maybe we don't need anything... Hm... It's better to spend money on the party instead of the activities.)"

if minigames:
    stop music fadeout 3
    mc "(Let's start with this... It's ok to change my mind... What else can we do?)"
    $ tmpMenu = quick_menu
    $ quick_menu = 0
    play music "music/ep11/jingle_balls.mp3"
    queue music ["music/ep11/silent_night.mp3","music/ep11/oholynight.mp3","music/ep11/jingle_balls.mp3"]
    show screen pp_intro_screen
    pause
    label ep11_play_label:
    $ tmp_list = [-1,-1]
    $ pp_tut_state = 0
    show screen pp_bg_screen_ep11

    $ pp_round = 3
    $ pp_continue_label = "ep11_pp_cont_label"
    $ renpy.block_rollback()
    jump party_planner_setup_round_label
    label ep11_pp_cont_label:
    hide screen pp_bg_screen_ep11
    $ quick_menu = tmpMenu
    stop music fadeout 3
    mc "(Awesome... I hope.)"
else:
    label ep11_lock_in_label:
    $ pp_nm_tmp_happiness = [0,0,0,0,0,0,0,0]
    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][0] == -1 and pp_activity_choices[0] != 2:
                pp_nm_tmp_happiness[i] += 1
            elif pp_nm_party_preference[i][0] == pp_activity_choices[0] and pp_activity_choices[0] != 2:
                pp_nm_tmp_happiness[i] += 1
    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][1] == -1 and pp_activity_choices[1] != 2:
                pp_nm_tmp_happiness[i] += 1
            elif pp_nm_party_preference[i][1] == pp_activity_choices[1] and pp_activity_choices[1] != 2:
                pp_nm_tmp_happiness[i] += 1
    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][2] == pp_activity_choices[2] and pp_activity_choices[2] == 0:
                pp_nm_tmp_happiness[i] += 1

    python:
        for i in range(0,8):
            if pp_nm_tmp_happiness[i] > 1:
                pp_nm_tmp_happiness[i] = 1
                pp_current_party_happiness[i] = 1
            elif pp_nm_tmp_happiness[i] == 1:
                pp_nm_tmp_happiness[i] = 0
                pp_current_party_happiness[i] = 0
            else:
                pp_nm_tmp_happiness[i] = -1
                pp_current_party_happiness[i] = -1
    python:
        for i in range(0,8):
            pp_nm_tmp_happiness[i] += pp_nm_dik_happiness[i]
            if pp_nm_tmp_happiness[i] < 0:
                pp_nm_tmp_happiness[i] = 0
            elif pp_nm_tmp_happiness[i] > 3:
                pp_nm_tmp_happiness[i] = 3

    show screen pp_nm_happiness_screen
    menu:
        "{i}Are you done planning the activities?{/i}"
        "Done":
            $ renpy.block_rollback()
            hide screen pp_nm_happiness_screen
            python:
                for i in range(0,8):
                    pp_nm_dik_happiness[i] = pp_nm_tmp_happiness[i]
            stop music fadeout 3
            mc "(All done.)"
        "Start over":
            hide screen pp_nm_happiness_screen
            $ currentActivity = 0
            $ pp_money = 20
            show screen pp_dik_preferences_screen
            menu:
                "Alcohol and Food ($4)" if minigames or pp_money > 3:
                    $ pp_money -= 4
                    $ pp_activity_choices[0] = 0
                "Alcohol ($2)" if minigames or pp_money > 1:
                    $ pp_money -=2
                    $ pp_activity_choices[0] = 1
                "B.Y.O.B.":
                    $ pp_activity_choices[0] = 2
            $ currentActivity = 1
            menu:
                "Wet T-shirt ($4)" if minigames or pp_money > 3:
                    $ pp_activity_choices[1] = 0
                    $ pp_money -= 4
                "Cucumber Competition ($2)" if minigames or pp_money > 1:
                    $ pp_money -= 2
                    $ pp_activity_choices[1] = 1
                "Nothing":
                    $ pp_activity_choices[1] = 2
            $ currentActivity = 2
            menu:
                "Guess Who? Game ($2)" if minigames or pp_money > 1:
                    $ pp_activity_choices[2] = 0
                    $ pp_money -= 2
                "Nothing":
                    $ pp_activity_choices[2] = 1
            hide screen pp_dik_preferences_screen
            jump ep11_lock_in_label


$ ep11_pp_alcohol_food = pp_activity_choices[0]
$ ep11_pp_contest = pp_activity_choices[1]
$ ep11_pp_game = pp_activity_choices[2]
if minigames:
    python:
        for x in range(0,len(pp_needs_met)):
            tmpInt = 0
            for y in pp_needs_met[x]:
                if y:
                    tmpInt += 1
            pp_current_party_happiness[x] = tmpInt

jump ep11_sally_label

label ep11_fr_deco_box1_event_label:
scene ep11_fr_deco_box1_event with dissolve
mc "(That box reads...\"Kitchen\". Yep, I'm taking this one to the HOTs.)"

if "ep11_fr_deco_box2_event_label" in event_list and "ep11_fr_deco_box3_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (1/3)"
elif "ep11_fr_deco_box2_event_label" in event_list or "ep11_fr_deco_box3_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (2/3)"
else:
    $ task_list[0] = "Bring the boxes to the HOTs"
    mc "(I think that was the last box. I should bring them to the HOTs now.)"
    $ event_list.append("ep11_fr_deco_box_event_label")
$ updateTaskList()
jump endEvent

label ep11_fr_deco_box2_event_label:
scene ep11_fr_deco_box2_event with dissolve
mc "(Gee... I wonder how a box labeled kitchen ended up in the kitchen.)"

if "ep11_fr_deco_box1_event_label" in event_list and "ep11_fr_deco_box3_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (1/3)"
elif "ep11_fr_deco_box1_event_label" in event_list or "ep11_fr_deco_box3_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (2/3)"
else:
    $ task_list[0] = "Bring the boxes to the HOTs"
    mc "(I think that was the last box. I should bring them to the HOTs now.)"
    $ event_list.append("ep11_fr_deco_box_event_label")
$ updateTaskList()
jump endEvent

label ep11_fr_deco_box3_event_label:
scene ep11_fr_deco_box3_event with dissolve
mc "(Why would someone even put this box in Jacob's room?)"

if "ep11_fr_deco_box1_event_label" in event_list and "ep11_fr_deco_box2_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (1/3)"
elif "ep11_fr_deco_box1_event_label" in event_list or "ep11_fr_deco_box2_event_label" in event_list:
    $ task_list[0] = "Find boxes labeled Kitchen (2/3)"
else:
    $ task_list[0] = "Bring the boxes to the HOTs"
    mc "(I think that was the last box. I should bring them to the HOTs now.)"
    $ event_list.append("ep11_fr_deco_box_event_label")
$ updateTaskList()
jump endEvent

label ep11_fr_deco_box_event_label:
scene ep11_fr_deco_box_event with dissolve
mc "(There we go. Enjoy your Christmas lights. It's funny that no one noticed these boxes were too light to have appliances in them.)"
hide screen wt_boxes_update
if "ep11_fr_mel_lewd_event_label" in event_list:
    if persistent.mod_wtenabled:
        $ task_list[0] = "Talk to Melanie (Main Party Room)"
    else:
        $ task_list[0] = "Talk to Melanie"
else:
    $ task_list[0] = ""

$ updateTaskList()
jump endEvent

label ep11_fr_deco_ji_event_label:
scene ep11_fr_deco_ji_event1 with dissolve
mc "How is it going?"
scene ep11_fr_deco_ji_event2 with dissolve
ji "Fine. This Christmas music makes me feel the holiday spirit."
scene ep11_fr_deco_ji_event3 with dissolve
ji "*{i}Smack{/i}*"
scene ep11_fr_deco_ji_event4 with dissolve
$ renpy.pause()
scene ep11_fr_deco_ji_event5 with dissolve
jm "Jill? Can you help put these ones up?"
scene ep11_fr_deco_ji_event6 with dissolve
ji "I'd love to."
scene ep11_fr_deco_ji_event7 with dissolve
mc "Don't let me bother you guys. Have fun with it."
scene ep11_fr_deco_ji_event8 with dissolve
ji "So, Jamie? What have you been up to lately?"
scene ep11_fr_deco_ji_event10 with dissolve
jm "School and such. And, oh...my girlfriend's bunny...he died recently."
scene ep11_fr_deco_ji_event9 with dissolve
ji "Oh, no. That's so sad."
scene ep11_fr_deco_ji_event10 with dissolve
jm "Yeah, Franz was great."
scene ep11_fr_deco_ji_event9 with dissolve
ji "Do you want to tell me about him?"
$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_deco_ari2_event_label:
$ guideSuggestedPage = 169
scene ep11_fr_deco_ari2_event1 with dissolve
ar "Oh, [name]!"
ar "Wanna buy some condoms?"
scene ep11_fr_deco_ari2_event2 with dissolve
menu:
    "I don't use those":
        mc "Condoms? I don't use those."
        scene ep11_fr_deco_ari2_event4 with dissolve
        ar "Me neither, and look where it got me..."
        scene ep11_fr_deco_ari2_event2 with dissolve
        mc "You make a good point."
        scene ep11_fr_deco_ari2_event1 with dissolve
        ar "How about it?"
    "How much?":
        mc "How much?"
        scene ep11_fr_deco_ari2_event3 with dissolve
        ar "How much can you afford?"
        scene ep11_fr_deco_ari2_event2 with dissolve
        mc "Do you expect me to haggle over condoms?"
        scene ep11_fr_deco_ari2_event3 with dissolve
        ar "That depends... Do you want to haggle?"
    "No thanks":
        mc "No thanks. I'm all set."
        if branchSage:
            scene ep11_fr_deco_ari2_event5 with dissolve
            sa "Hah!"
            scene ep11_fr_deco_ari2_event6 with dissolve
            mc "What was that?"
            scene ep11_fr_deco_ari2_event5 with dissolve
            sa "Nothing."
        scene ep11_fr_deco_ari2_event3 with dissolve
        ar "Not even one condom? You never know when you're gonna need it."

scene ep11_fr_deco_ari2_event2 with dissolve
mc "Maybe another time. I didn't bring any money."
scene ep11_fr_deco_ari2_event1 with dissolve
ar "I'm gonna hold you to that."

$ new_bio("Arieth", "Arieth tried to sell me condoms.")
$ optional_task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep11_fr_mel_lewd_event_label:
scene ep11_fr_mel_lewd_event1 with dissolve
mc "I'm all done with the boxes."
scene ep11_fr_mel_lewd_event2 with dissolve
el "Thank you, [name]."
scene ep11_fr_mel_lewd_event1 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Melanie scene)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Steal Melanie for a while \n{size=-4}[m_c1][mod_choices[0]]":
        mc "Did I earn Melanie a break now, or what?"
        scene ep11_fr_mel_lewd_event2 with dissolve
        el "Fine. A short one. But I need someone to help me with this."
        scene ep11_fr_mel_lewd_event3 with dissolve
        mc "Oh, no problem. I saw Ashley and Derek upstairs. I'll send them right over."
        scene ep11_fr_mel_lewd_event4 with dissolve
        ml "Thanks, [name]. Elena's been riding my ass all afternoon."
        scene ep11_fr_mel_lewd_event5 with dissolve
        mc "I know. You looked like you could use a break."
    "Leave":
        mc "You're welcome."
        $ task_list[0] = ""
        $ updateTaskList()
        jump endEvent

label ep11_melanie_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep11_cammy_draught = False
    $ ep11_sarah_lewd = False
    $ ep9_sarah_melanie_lewd = True
    $ RPderek = 0
    $ ep8_melanie_lewd = True
    hide screen new_phone_screen
    play music "music/ep11/christmas_jazz.mp3"
    queue music ["music/ep11/licensed_music/track160.mp3","music/ep11/licensed_music/track161.mp3","music/ep11/licensed_music/track179.mp3","music/ep11/licensed_music/track183.mp3","music/ep11/licensed_music/track168.mp3","music/ep11/licensed_music/track159.mp3"]
scene ep11_fr_mel_lewd_event6 with dissolve
mc "Derek? Ashley? Elena needs your help downstairs."
scene ep11_fr_mel_lewd_event7 with dissolve
ash "But we're not done decorating."
scene ep11_fr_mel_lewd_event8 with dissolve
mc "Eh. Leave it for later."
scene ep11_fr_mel_lewd_event9 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Derek)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Call out the mistletoe \n{size=-4}[m_c1][mod_choices[0]]":
        $ RPderek += 1
        scene ep11_fr_mel_lewd_event10 with dissolve
        mc "Hey, you passed under the mistletoe. You gotta kiss."
        scene ep11_fr_mel_lewd_event11 with dissolve
        ash "Pssch. I didn't see you kiss Melanie."
        if not _in_replay:
            $ new_bio("Ashley", "I tried to make Ashley kiss Derek underneath the mistletoe.")
            $ new_bio("Derek", "I tried to make Ashley kiss Derek underneath the mistletoe.")
    "Let them leave":
        $ renpy.pause(0.5)
scene ep11_fr_mel_lewd_event12 with dissolve
ml "Alright... Let's go."
scene ep11_fr_mel_lewd_event13 with dissolve
mc "Hm?"
scene ep11_fr_mel_lewd_event14 with dissolve
ml "You flirted with me and worked hard to earn me a break. It can only mean one thing."
ml "Pull that cock out, I've got unfinished business with it."

if False:
    scene ep11_fr_mel_lewd_event13 with dissolve
    mc "Oh... I was just being nice and getting you a break."
    scene ep11_fr_mel_lewd_event14 with dissolve
    ml "Sure."
    scene ep11_fr_mel_lewd_event15 with dissolve
    mc "I wouldn't say no to you, but... Sarah just used it."
    scene ep11_fr_mel_lewd_event16 with dissolve
    ml "No way! So, it won't work now?"
    scene ep11_fr_mel_lewd_event15 with dissolve
    mc "I mean, unless you like it flaccid."
    scene ep11_fr_mel_lewd_event17 with dissolve
    ml "Haha, shut up!"
    scene ep11_fr_mel_lewd_event18 with dissolve
    ml "Fuck... Now, I have unfinished business with Sarah. What a bitch..."
    scene ep11_fr_mel_lewd_event19 with dissolve
    mc "Can you hit me up in like...20 minutes or so?"
    scene ep11_fr_mel_lewd_event18 with dissolve
    ml "For what? Sloppy seconds? I wanted a meal. And I'd be lucky if I got a 20-minute break tonight."
    scene ep11_fr_mel_lewd_event19 with dissolve
    mc "Oh well."
    scene ep11_fr_mel_lewd_event18 with dissolve
    ml "I might as well relieve Ashley from Elena..."
    scene ep11_fr_mel_lewd_event19 with dissolve
    mc "Sorry, Mel."
    scene ep11_fr_mel_lewd_event20 with dissolve
    ml "Yeah, whatever."
    $ task_list[0] = ""
    $ updateTaskList()
    $ new_bio("Melanie", "Melanie wanted to have sex, but I had just fucked Sarah and wasn't ready to go another round.")
    jump endEvent

scene ep11_fr_mel_lewd_event21 with dissolve
mc "In here?"
scene ep11_fr_mel_lewd_event22 with dissolve
ml "Exciting, huh?"
scene ep11_fr_mel_lewd_event21 with dissolve
mc "What will you do if someone walks in on us?"
scene ep11_fr_mel_lewd_event23 with dissolve
ml "Give them a show to remember."
scene ep11_fr_mel_lewd_event24 with dissolve
mc "You're crazy."
scene ep11_fr_mel_lewd_event23 with dissolve
ml "No, I'm extremely horny. You have no idea."
scene ep11_fr_mel_lewd_event24 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Melanie scene)","(-Sage)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Fuck her \n{size=-4}[m_c1][mod_choices[0]]":
        $ ep11_mel_lewd = True
    "Turn her down" if not _in_replay:
        scene ep11_fr_mel_lewd_event25 with dissolve
        mc "Raincheck?"
        scene ep11_fr_mel_lewd_event18 with dissolve
        ml "Ugh, come on. Don't be like that."
        scene ep11_fr_mel_lewd_event19 with dissolve
        mc "Someone could walk in on us and that makes me feel uneasy."
        scene ep11_fr_mel_lewd_event18 with dissolve
        ml "*{i}Sigh{/i}* Alright...ugh."
        ml "I might as well relieve Ashley from Elena and get done with the work."
        scene ep11_fr_mel_lewd_event19 with dissolve
        mc "Sorry, Mel."
        scene ep11_fr_mel_lewd_event20 with dissolve
        ml "Yeah, whatever."
        $ new_bio("Melanie", "Melanie wanted to have sex, but I turned her down.")
        $ task_list[0] = ""
        $ updateTaskList()
        jump endEvent

hide screen new_phone_screen
mc "Fuck it. Let's go for it."
scene ep11_fr_mel_lewd_event26 with dissolve
$ renpy.pause()
scene ep11_fr_mel_lewd_event27 with dissolve
$ renpy.pause()
scene ep11_fr_mel_lewd_event28 with dissolve
mc "But I'm gonna pull out the sliding door for this..."
scene ep11_fr_mel_lewd_event29 with dissolve
ml "Whatever works for you."
scene ep11_fr_mel_lewd_event30 with dissolve
$ renpy.pause()
scene ep11_fr_mel_lewd_event31 with dissolve
menu:
    "[m_c1]Kiss her":
        $ ep11_mel_kiss = True
        scene ep11_fr_mel_lewd_event32 with dissolve
        ml "*{i}Smack{/i}*"
        scene ep11_fr_mel_lewd_event33 with dissolve
        $ renpy.pause()
        scene ep11_fr_mel_lewd_event34 with dissolve
        $ renpy.pause()
        scene ep11_fr_mel_lewd_event35 with dissolve
        ml "If this is your way to make me extra horny because it's working."
        scene ep11_fr_mel_lewd_event36 with dissolve
        mc "I just wanted to kiss you, but that's good."
        scene ep11_fr_mel_lewd_event37 with dissolve
        ml "*{i}Smack{/i}*"
    "Push her head down":
        scene ep11_fr_mel_lewd_event38 with dissolve
        mc "Suck my cock, Mel."

scene ep11_fr_mel_lewd_event39 with dissolve
$ renpy.pause()
scene anim_mel_bj1_ep11 with dissolve
ml "*{i}Suck smack glug{/i}*"
pause
scene anim_mel_bj2_ep11 with dissolve
pause
scene anim_mel_bj3_ep11 with dissolve
ml "*{i}Suck suck glug glug{/i}*"
pause

scene ep11_fr_mel_lewd_event40 with dissolve
ml "At least something good came out of carrying all those boxes over here."
scene ep11_fr_mel_lewd_event41 with dissolve
mc "Don't remind me of carrying boxes, the only box I'm interested in right now is yours."
scene ep11_fr_mel_lewd_event42 with dissolve
ml "Yeah? Are you going to fuck my pussy, or maybe my ass?"
scene ep11_fr_mel_lewd_event43 with dissolve
ml "Or maybe both?"
scene ep11_fr_mel_lewd_event44 with dissolve
mc "Now you're asking me a tough question..."
scene ep11_fr_mel_lewd_event45 with dissolve
menu:
    "Vaginal":
        mc "No, I need to feel your pussy first..."
        scene ep11_fr_mel_lewd_event48 with dissolve
        ml "*{i}Moans{/i}*"
        scene ep11_fr_mel_lewd_event49 with dissolve
        ml "Fuck..."
        scene anim_mel_stand1_ep11 with dissolve
        ml "Yes... Yes! Fuck!"
        mc "Hey, I thought I was gonna do the humping..."
        ml "*{i}Moans{/i}* Shut up... Give it to me..."
        pause
        scene anim_mel_stand2_ep11 with dissolve
        mc "You're really craving it, aren't you?"
        ml "Mhm..."
        pause
    "Anal":
        mc "I can't resist that ass."
        scene ep11_fr_mel_lewd_event46 with dissolve
        ml "*{i}Moans{/i}*"
        scene ep11_fr_mel_lewd_event47 with dissolve
        ml "Shit... Ahh..."
        scene anim_mel_stand1_anal_ep11 with dissolve
        ml "Yes... Yes! Fuck!"
        mc "Hey, I thought I was gonna do the humping..."
        ml "*{i}Moans{/i}* Shut up... Give it to me..."
        pause
        scene anim_mel_stand2_anal_ep11 with dissolve
        mc "You're really craving it, aren't you?"
        ml "Mhm..."
        pause

$ tmpInt = 0
label ep11_mel_lewd_loop_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_mel_miss1_ep11 with dissolve
        ml "*{i}Moans{/i}* Oh, [name]... You feel so good..."
        pause
        scene anim_mel_miss2_ep11 with dissolve
        mc "That's the biggest smile I've ever seen on you."
        ml "Haha..."
        pause
        scene anim_mel_miss3_ep11 with dissolve
        mc "It's dangerous looking into your eyes like this, though."
        mc "If looks could make you cum, I'm in big trouble."
        ml "You and me both... *{i}Moans{/i}*"
        pause
        jump ep11_mel_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_mel_doggy1_anal_ep11 with dissolve
        ml "Fuck my ass, [name]..."
        pause
        scene anim_mel_doggy2_anal_ep11 with dissolve
        mc "Damn... You're so sexy, Mel."
        pause
        jump ep11_mel_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_mel_ride1_ep11 with dissolve
        ml "Did you ever have a girl ride you like this in here?"
        mc "No. You're taking my virginity in this room."
        ml "Haha, yay."
        pause
        scene anim_mel_ride2_ep11 with dissolve
        mc "Did I tell you how much I love your ass? I love holding it while you ride me."
        ml "I love it when you do. Push me down harder on your cock."
        pause
        jump ep11_mel_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_mel_stand1_ep11 with dissolve
        ml "*{i}Moans{/i}*"
        pause
        scene anim_mel_stand2_ep11 with dissolve
        pause
        jump ep11_mel_lewd_loop_label
    "Standing (Anal)":
        $ tmpInt += 1
        scene anim_mel_stand1_anal_ep11 with dissolve
        ml "*{i}Moans{/i}*"
        pause
        scene anim_mel_stand2_anal_ep11 with dissolve
        pause
        jump ep11_mel_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_mel_rev1_ep11 with dissolve
        ml "That's right... You just sit there and keep that cock hard for me. Let me take care of the rest."
        mc "Mel, you're spoiling me here."
        pause
        scene anim_mel_rev2_ep11 with dissolve
        ml "I'm the one being spoiled. Fuck..."
        pause
        scene anim_mel_rev3_ep11 with dissolve
        mc "Bounce that ass on me... Work it."
        pause
        jump ep11_mel_lewd_loop_label
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_mel_rev1_anal_ep11 with dissolve
        ml "Hnnn... *{i}Moans{/i}*"
        pause
        scene anim_mel_rev2_anal_ep11 with dissolve
        mc "I'm getting close here..."
        pause
        jump ep11_mel_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna cum."
        menu:
            "In mouth":
                scene anim_mel_bj4_ep11 with vpunch
                mc "Fuck! Ahhh..."
                pause
                scene ep11_fr_mel_lewd_event50 with dissolve
                ml "*{i}Lick lick{/i}* Did I do good?"
                scene ep11_fr_mel_lewd_event51 with dissolve
                mc "Fuck yes, you did."
                ml "Mmm..."
            "Creampie":
                scene anim_mel_rev1_ep11 with dissolve
                pause
                scene anim_mel_rev4_ep11 with vpunch
                mc "Fuck! Ahhh..."
                pause
                scene ep11_fr_mel_lewd_event53 with dissolve
                ml "You came a lot..."
                mc "I sure did."
            "Creampie (Anal)":
                scene anim_mel_stand1_anal_ep11 with dissolve
                pause
                scene anim_mel_stand3_anal_ep11 with vpunch
                mc "Fuck! Ahhh..."
                pause
                scene ep11_fr_mel_lewd_event52 with dissolve
                mc "Damn! That's a hot sight."

scene ep11_fr_mel_lewd_event54 with dissolve
ml "It's been a while..."
scene ep11_fr_mel_lewd_event55 with dissolve
mc "What's a while for you?"
scene ep11_fr_mel_lewd_event56 with dissolve
if ep9_sarah_melanie_lewd:
    ml "Since Halloween."
    scene ep11_fr_mel_lewd_event55 with dissolve
    mc "With me?"
    scene ep11_fr_mel_lewd_event56 with dissolve
    ml "Uh, duh."
else:
    ml "I barely remember."
scene ep11_fr_mel_lewd_event55 with dissolve
mc "That's a long time."
scene ep11_fr_mel_lewd_event56 with dissolve
ml "For me, it is. Sarah's feeling frustrated, too."
if ep11_cammy_draught:
    scene ep11_fr_mel_lewd_event57 with dissolve
    mc "Camila told me she also had a drought not that long ago. What's going on with you girls?"
    if ep2_fuckHOT or ep3_fuckedRionaQuinn or quinn_shop_japanese_lvl > 0 or quinn_shop_spicy_lvl > 0 or ep8_sarah_lewd:
        scene ep11_fr_mel_lewd_event58 with dissolve
        ml "Let's just say that Quinn decided to pause some \"services\"."
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "Oh... Why's that?"
        scene ep11_fr_mel_lewd_event60 with dissolve
        ml "What does it matter to you? It's not like you've been a busy customer."
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "I was just curious. Quinn didn't mention it to me."
        scene ep11_fr_mel_lewd_event58 with dissolve
        ml "You didn't hear this from me, but I think there's a lot she doesn't mention to you."
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "Like what?"
        scene ep11_fr_mel_lewd_event60 with dissolve
        ml "My lips are now sealed..."
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "Fine. Maybe I'll ask her."
        mc "And while I'm at it, I could pay Sarah a visit."
    else:
        scene ep11_fr_mel_lewd_event60 with dissolve
        ml "Have you never had a dry spell?"
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "Speaking for every guy, of course, I have. But I usually solve it myself."
        scene ep11_fr_mel_lewd_event60 with dissolve
        ml "That's not the same thing, is it? And it's still a dry spell, even if you masturbate."
        scene ep11_fr_mel_lewd_event59 with dissolve
        mc "Yeah, I know."
        mc "Thanks for the info... Maybe I should pay Sarah a visit?"
    scene ep11_fr_mel_lewd_event61 with dissolve
    ml "No, don't do that. Pay me one instead."
else:
    scene ep11_fr_mel_lewd_event57 with dissolve
    mc "Oh, poor Sarah."
    scene ep11_fr_mel_lewd_event61 with dissolve
    ml "No, don't give me poor Sarah. It's poor Mel. Got it?"
scene ep11_fr_mel_lewd_event62 with dissolve
mc "Haha! I hear you. You know where my room is."
scene ep11_fr_mel_lewd_event63 with dissolve
if ep8_melanie_lewd:
    ml "Awesome, [name]. Maybe this place could use a couple of new fuck zones. Don't you think?"
    scene ep11_fr_mel_lewd_event64 with dissolve
    mc "Well, this room was a good start to it."
    scene ep11_fr_mel_lewd_event63 with dissolve
else:
    ml "Awesome, [name]."
ml "I'm gonna relieve Ashley from Elena and get done with the work now. This was the best break ever."
if ep11_mel_kiss:
    scene ep11_fr_mel_lewd_event65 with dissolve
    ml "*{i}Smack{/i}*"
    scene ep11_fr_mel_lewd_event66 with dissolve
    $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep11_lewd_melanie = True
$ calcScenes()
$ task_list[0] = ""
$ updateTaskList()
if ep11_mel_kiss:
    $ new_bio("Melanie", "I had sex with Melanie in the DIKs' mansion. We even kissed some. It was nice.")
else:
    $ new_bio("Melanie", "I had sex with Melanie in the DIKs' mansion.")
$ new_bio("Sarah", "Melanie told me that Sarah was sexually frustrated.")
$ mphone_stats_add_girl_s3("melanie","You had sex with Melanie in the DIKs' mansion in episode 11.")
show screen new_phone_screen
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

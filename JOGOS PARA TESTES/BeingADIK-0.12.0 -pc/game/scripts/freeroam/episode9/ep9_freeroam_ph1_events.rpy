label ep9_diks_ph1_jamie_event_label:
scene ep9_dik1_jamie_event1 with dissolve
jm "And if you look at my lovely assistant, you'll see that she's-"
scene ep9_dik1_jamie_event4
dn "*Cough*"
scene ep9_dik1_jamie_event3 with dissolve
jm "*{i}Whispers{/i}* What pronoun is it this time?"
scene ep9_dik1_jamie_event4 with dissolve
dn "Them or they."
scene ep9_dik1_jamie_event2 with dissolve
jm "If you look at my lovely assistant, you'll see that them-they...*{i}Sigh{/i}*...is holding-"
scene ep9_dik1_jamie_event3 with dissolve
jm "It sounds weird."
scene ep9_dik1_jamie_event5 with dissolve
jm "Anyway, it's my hat!"
jm "An ordinary magician's hat."
scene ep9_dik1_jamie_event6 with dissolve
jm "If I give it a little bippety boppety with my wand, you can see how the hat has turned magic aaaaand..."
scene ep9_dik1_jamie_event7 with dissolve
jm "Voila!"
"*{i}Smatter of applause{/i}*"
scene ep9_dik1_jamie_event8 with dissolve
jm "Franz! How did you get in there?"
jm "Haha, I'm joking, of course. He's been there-"
scene ep9_dik1_jamie_event4
dn "*Cough*"
scene ep9_dik1_jamie_event9 with dissolve
jm "Them has been there-"
scene ep9_dik1_jamie_event4
dn "They."
scene ep9_dik1_jamie_event9 with dissolve
jm "They has-"
scene ep9_dik1_jamie_event4
dn "Have."
scene ep9_dik1_jamie_event10 with dissolve
jm "It's getting too complicated, Dany."
scene ep9_dik1_jamie_event11 with dissolve
le "Bippety boppety!? What the fuck, bro?"
scene ep9_dik1_jamie_event12 with dissolve
jm "Oh, no... You didn't..."
scene ep9_dik1_jamie_event14 with dissolve
le "Yeah, I did. And why haven't you?"
scene ep9_dik1_jamie_event15 with dissolve
jm "We were drunk, brainstorming ideas at The Pink Rose; I didn't think you meant it."
scene ep9_dik1_jamie_event16 with dissolve
dn "At where?"
scene ep9_dik1_jamie_event17 with dissolve
jm "Uh..."
scene ep9_dik1_jamie_event15 with dissolve
jm "I mean, it's women's clothing."
scene ep9_dik1_jamie_event16 with dissolve
dn "Don't put a gender on clothes, Jam-Jam."
scene ep9_dik1_jamie_event17 with dissolve
jm "But it's a skirt!"
scene ep9_dik1_jamie_event16 with dissolve
dn "The Scottish wear skirts."
scene ep9_dik1_jamie_event13 with dissolve
jm "Not like that one! Look at his legs; he's wearing stockings too."
scene ep9_dik1_jamie_event14 with dissolve
le "Real nice, bro."
scene ep9_dik1_jamie_event18 with dissolve
jm "Leon!"
scene ep9_dik1_jamie_event16 with dissolve
dn "Men can wear stockings too. They have legs, don't they?"
scene ep9_dik1_jamie_event19 with dissolve
jm "Can we just have fun for once?"
if persistent.mod_wtenabled:
    $ task_list[1] = "Talk to Leon (left Hallway)"
else:

    $ task_list[1] = "Talk to Leon"
$ updateTaskList()
$ event_list.append("ep9_diks_ph1_leon_event_label")
jump endEvent

label ep9_diks_ph1_zoey_event_label:
scene ep9_dik1_zoey_event1 with dissolve
zo "I just came back from San Diego. I've been working in the reception of a tattoo and piercing studio."
scene ep9_dik1_zoey_event4 with dissolve
jb "I love San Diego! My uncle lives in Oceanside, so I've been there many times."
scene ep9_dik1_zoey_event5 with dissolve
jac "You worked in a tattoo studio? That sounds dope as hell! Did you get those pieces there or what?"
scene ep9_dik1_zoey_event1 with dissolve
zo "Yeah, I did. It was like a job perk, you know? They inked each other for free."
scene ep9_dik1_zoey_event3 with dissolve
jac "I love that chest piece. Those colors are mint!"
scene ep9_dik1_zoey_event2 with dissolve
zo "Thanks, I actually designed it."
scene ep9_dik1_zoey_event5 with dissolve
jac "You draw?"
scene ep9_dik1_zoey_event4 with dissolve
jb "Hey, did you go to Mexico?"
scene ep9_dik1_zoey_event1 with dissolve
mc "(Zoey doesn't have a hard time talking to new people. They seem enthusiastic about talking to her.)"
mc "(I should come back later.)"
$ optional_task_list[3] = ""
$ new_bio("Zoey", "The DIKs seemed to like Zoey.")
jump endEvent

label ep9_diks_ph1_dormies_event_label:
scene ep9_dik1_dormies_event1 with dissolve
bc "No! This is why we talk before we buy costumes. I was going as a hot nurse this year, not you!"
scene ep9_dik1_dormies_event5 with dissolve
chr "I planned this year's outfit before we even got invited here."
scene ep9_dik1_dormies_event2 with dissolve
bc "Yeah? So did Penny. And can you see her over there right now?"
scene ep9_dik1_dormies_event6 with dissolve
bc "Is she a nurse or is she a dead ghost girl?"
scene ep9_dik1_dormies_event5 with dissolve
chr "It's too late now because I can't go change into something else. I don't have anything else to wear."
scene ep9_dik1_dormies_event3 with dissolve
bc "Gah! I can't believe you. You even bought the same brand I did."
ky "Oh, no..."
scene ep9_dik1_dormies_event4 with dissolve
bc "For realsies!? You've got to be kidding me!"
scene ep9_dik1_dormies_event7 with dissolve
ky "You're both?"
bc "At least one of you has to change costumes. I'm gonna be the hot nurse tonight!"
chr "Hell no! You go change!"
jump endEvent

label ep9_diks_ph1_tommy_event_label:
scene ep9_diks_ph1_tommy_event1 with dissolve
tm "[name]! Go get a keg."
scene ep9_diks_ph1_tommy_event2 with dissolve
mc "Why can't you do it?"
scene ep9_diks_ph1_tommy_event1 with dissolve
tm "Because shit rolls downhill."
scene ep9_diks_ph1_tommy_event2 with dissolve
mc "Ugh... Where's the tap?"
scene ep9_diks_ph1_tommy_event1 with dissolve
tm "It should be in the kitchen. Or maybe Nick's room. You need to look for it."
if persistent.mod_wtenabled:
    $ task_list[4] = "Find the beer tap (Nick's room)"
    $ task_list[5] = "Bring a keg to Tommy (Tommy's room)"
else:
    $ task_list[4] = "Find the beer tap"
    $ task_list[5] = "Bring a keg to Tommy"
$ updateTaskList()

$ event_list.append("ep9_diks_ph1_tap_event_label")
$ event_list.append("ep9_diks_ph1_keg_event_label")
jump endEvent

label ep9_diks_ph1_santa_event_label:
play sound "sound_effects/shove.mp3"
scene ep9_dik1_santa_event1 with vpunch
$ renpy.pause()
scene ep9_dik1_santa_event2 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Apologize [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "Sorry! I didn't see you there, Santa."
    "Confront [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "Hey! Watch it. What are you shoving me for?"
scene ep9_dik1_santa_event3 with dissolve
mc "Dude... What's going on?"
scene ep9_dik1_santa_event4 with dissolve
mc "Whatever..."
mc "(What the fuck is wrong with him? It felt like he was trying to pick a fight or something.)"
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph1_girls_event_label:
scene ep9_diks_ph1_girls_event1 with dissolve
mc "Hey, girls. I hope you're having fun; there's more than beer to drink downstairs. Or if you're feeling up for a scary drink, The Moose is around the corner."
scene ep9_diks_ph1_girls_event2 with dissolve
cla "The what?"
scene ep9_diks_ph1_girls_event1 with dissolve
mc "The Moose. It's Derek's pet project."
scene ep9_diks_ph1_girls_event4 with dissolve
ti "Oh! It's that bar that's all over Rooster."
scene ep9_diks_ph1_girls_event3 with dissolve
cla "Oh yeah! I heard about that one!"
scene ep9_diks_ph1_girls_event4 with dissolve
ti "We might check it out. Thanks!"
scene ep9_diks_ph1_girls_event2 with dissolve
cla "Do you know if something's about to happen soon or...?"
scene ep9_diks_ph1_girls_event1 with dissolve
if ep9_body_shots or ep9_drinking_competition:
    mc "Yeah, there will be a competition soon. You'll know when it starts."
    scene ep9_diks_ph1_girls_event3 with dissolve
    cla "Awesome!"
else:
    mc "You never know. Later, there will be something for sure."
    scene ep9_diks_ph1_girls_event2 with dissolve
    cla "Ok. Thanks."
scene ep9_diks_ph1_girls_event1 with dissolve
mc "Have fun!"
if not ep8_recital_failed:
    scene ep9_diks_ph1_girls_event5 with dissolve
    girl "*{i}Whispers{/i}* Isn't that the guy from that video?"
$ optional_task_list[5] = ""
jump endEvent

label ep9_diks_ph1_keg_event_label:
scene ep9_diks_ph1_keg_event1b with dissolve
mc "(Get the keg. Do this. Do that.)"
mc "(\"Shit rolls downhill\"...)"
scene ep9_diks_ph1_keg_event2 with dissolve
mc "(I don't mind helping out, but I don't like being bossed around like this.)"
scene ep9_diks_ph1_keg_event3 with dissolve
$ renpy.pause(2)
scene ep9_diks_ph1_keg_event4 with dissolve
mc "(I don't even wanna know.)"
scene ep9_diks_ph1_keg_event5 with dissolve
mc "Coming through."
scene ep9_diks_ph1_keg_event6 with dissolve
jb "Need any help?"
scene ep9_diks_ph1_keg_event7 with dissolve
if affinity == "DIK":
    mc "Now? I got it upstairs. The hard part is over."
    scene ep9_diks_ph1_keg_event6 with dissolve
    jb "Don't be a dick. You could have asked for help before."
    scene ep9_diks_ph1_keg_event7 with dissolve
    mc "Sorry. That was unfair."
    scene ep9_diks_ph1_keg_event8 with dissolve
    jb "Don't worry. You're clearly busting your ass for this party."
else:
    mc "Yeah, thanks."
    scene ep9_diks_ph1_keg_event8 with dissolve
    jb "Not a problem. You're clearly busting your ass for this party."
jb "Don't forget to have fun."
mc "Thanks, I won't."
scene ep9_diks_ph1_keg_event9 with dissolve
jb "So, that Zoey chick is pretty cool."
mc "Yeah?"
scene ep9_diks_ph1_keg_event10 with dissolve
jb "Yeah, I'm telling you. She's a total bro but a girl."
scene ep9_diks_ph1_keg_event11 with dissolve
mc "Yeah. She is great."
$ guideSuggestedPage = 54
scene ep9_diks_ph1_keg_event12 with dissolve
jb "How do you know her again?"
scene ep9_diks_ph1_keg_event11 with dissolve
menu:
    "Ex-girlfriend":
        $ ep9_jb_gf = True
        mc "She's sort of my ex-girlfriend."
        scene ep9_diks_ph1_keg_event13 with dissolve
        jb "Yeah? You still stay in touch with your exes, huh?"
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "Well, she's it."
        scene ep9_diks_ph1_keg_event12 with dissolve
        jb "I never did that. I usually cut all ties and move on."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "How so?"
        scene ep9_diks_ph1_keg_event13 with dissolve
        jb "At first, for my own sanity. Why keep someone you weren't happy with in your life?"
        jb "If it's toxic, cut it out. You know?"
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "You could end up as friends after."
        scene ep9_diks_ph1_keg_event13 with dissolve
        jb "I suppose. But what happens after that?"
        jb "Are you gonna keep your ex around your next girlfriend?"
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "It...could work."
        scene ep9_diks_ph1_keg_event13 with dissolve
        jb "You think? I'm not sure how Elena would react to that."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "It could be difficult. I see what you're saying."
        mc "Honestly, I don't know the best way to handle her. Zoey and I are-"
        scene ep9_diks_ph1_keg_event13 with dissolve
        jb "Oh? Shit! Sorry! I wasn't talking about cutting ties with Zoey; I was talking in general."
        jb "Guy talk, I mean."
        scene ep9_diks_ph1_keg_event12 with dissolve
        jb "But since we're on it..."
        jb "I think it's cool you're different that way."
        jb "It never hurts to learn from someone with a different perspective."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "I wish I had some wisdom to offer in that area."
        scene ep9_diks_ph1_keg_event14 with dissolve
        jb "If you need to talk about it, my door's always open."
        jb "And not just because there's no door to my room from the stairs."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "Thanks. I appreciate that."
    "Childhood friend":
        $ ep9_jb_gf = False
        mc "She's a childhood friend."
        scene ep9_diks_ph1_keg_event12 with dissolve
        jb "That's nice! I kind of outgrew mine. I wish I hadn't, but you know how it is."
        jb "Everyone wants something different, and you're either gonna be stuck in your parents' basement jerking off or try to make something out of yourself."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "Absolutely. You can jerk off in college too."
        scene ep9_diks_ph1_keg_event12 with dissolve
        jb "College is a surefire way to get something of your own, at least."
        jb "I love my parents, but something seriously bad has to happen for me to move back home."
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "I can agree that this is better. It's more..."
        scene ep9_diks_ph1_keg_event12 with dissolve
        jb "It's freedom!"
        scene ep9_diks_ph1_keg_event11 with dissolve
        mc "Yeah. Freedom."
        scene ep9_diks_ph1_keg_event14 with dissolve
        jb "Cool that you invited your friend, though. She's fun! I can see why you two would get along."

if (minigames and pp_current_party_happiness[3] > 2) or (not minigames and pp_current_party_happiness[3] == 1):
    scene ep9_diks_ph1_keg_event12 with dissolve
    jb "By the way, I love what youäve done with the party. I don't recall it ever being this good, and the night's barely started. I'm psyched!"
elif (minigames and pp_current_party_happiness[3] > 1) or (not minigames and pp_current_party_happiness[3] == 0):
    scene ep9_diks_ph1_keg_event12 with dissolve
    jb "By the way, nice job with the party. Keep it up!"

$ currentFreeRoamLabel = "ep9_diks_ph1_main_label"
if "ep9_diks_ph1_tap_event_label" in event_list:
    $ task_list[5] = ""
    $ updateTaskList()
    jump endEvent

jump ep9_diks_ph1_keg2_event_label


label ep9_diks_ph1_keg2_event_label:
scene ep9_diks_ph1_keg_event15 with dissolve
mc "Let there be beer."

$ task_list[4] = ""
$ task_list[5] = ""
$ updateTaskList()

if not branchIsabella:
    if ep9_body_shots or ep9_drinking_competition:
        jump ep9_diks_ph1_drinking_event_label
    else:
        $ event_list.append("ep9_diks_ph1_end_event_label")
elif branchIsabella and wt_ep9_branch_numbers > 1:
    $ event_list.append("ep9_diks_ph1_end_event_label")
jump endEvent

label ep9_diks_ph1_tap_event_label:
scene ep9_diks_ph1_keg_event1 with dissolve
mc "(There's that tap.)"
if not "ep9_diks_ph1_keg_event_label" in event_list:
    $ event_list.append("ep9_diks_ph1_keg2_event_label")
    $ task_list[4] = "Install the beer tap"
else:
    $ task_list[4] = ""

$ updateTaskList()

jump endEvent

label ep9_diks_ph1_sally_event_label:
$ currentFreeRoamLabel = "ep9_diks_ph1_1corr_label"
$ guideSuggestedPage = 53
scene ep9_dik1_sally_event1 with dissolve
mc "What are you two doing in here?"
scene ep9_dik1_sally_event2 with dissolve
sy "Is that how you greet your guests?"
scene ep9_dik1_sally_event3 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "How I greet you [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "No, it's how I greet you."
        scene ep9_dik1_sally_event3b with dissolve
        $ renpy.pause()
    "I was surprised":
        mc "I was surprised to see people in here, that's all."
    "Sorry [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "Sorry. Welcome to our party! What are you doing in here?"
        scene ep9_dik1_sally_event3c with dissolve
        $ renpy.pause()
scene ep9_dik1_sally_event4 with dissolve
ka "We're waiting for Derek. He said he was going to mix us drinks."
scene ep9_dik1_sally_event1 with dissolve
if "ep9_diks_ph1_derek_event_label" not in event_list:
    mc "Well, he's out there arguing, so that might be a while."
else:
    mc "Ok, I believe he's out there somewhere, but it might be a while."
menu:
    "[mod_gr]Offer to help":
        mc "Drinks, eh? I think I can manage that."
    "Leave":
        mc "Have fun waiting!"
        $ event_list.append("ep9_diks_ph1_sally_event_label_pass")
        $ task_list[2] = ""
        $ updateTaskList()
        if branchIsabella:
            scene ep9_diks_ph1_bella_call1 with dissolve
            play sound "sound_effects/cellphone.mp3"
            "*{i}Phone rings{/i}*"
            jump ep9_diks_ph1_bella_call_label
        else:
            jump ep9_diks_ph1_bella_library_label
scene ep9_dik1_sally_event5 with dissolve
sy "Do you even know how to make any?"
scene ep9_dik1_sally_event3 with dissolve
if ep7_becky_puke:
    mc "It depends on who you ask. You'll either like it a lot or not so much."
else:
    mc "I don't think I'm completely clueless."
scene ep9_dik1_sally_event6 with dissolve
mc "What can I get you?"
scene ep9_dik1_sally_event7 with dissolve
ka "Derek was gonna make me a margarita."
scene ep9_dik1_sally_event8 with dissolve
mc "Uh... Ok, what's in a margarita?"
scene ep9_dik1_sally_event11 with dissolve
sy "It's a tequila drink. You have no clue about anything, do you?"
scene ep9_dik1_sally_event8 with dissolve
mc "I can fix you something with tequila, for sure."
scene ep9_dik1_sally_event9 with dissolve
mc "And for you... How about something sweet?"
$ guideSuggestedPage = 54
scene ep9_dik1_sally_event10 with dissolve
sy "..."
menu:
    "Tease her more [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "No? You certainly don't need anything sour."
        scene ep9_dik1_sally_event11 with dissolve
        sy "What the hell is wrong with you?"
        scene ep9_dik1_sally_event10 with dissolve
        if affinity == "DIK":
            mc "I wouldn't know where to start."
        else:
            mc "I'm trying to lighten up the mood."
    "Don't tease her [mod_gr][mod_choices[2]]":
        $ dk(-1)
        scene ep9_dik1_sally_event9 with dissolve
        mc "I'll surprise you."
scene ep9_dik1_sally_event12 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    mc "A tequila drink for Karen is coming up..."
    "Soda, lemon and salt":
        play sound "sound_effects/season2/shake.mp3"
        scene ep9_dik1_sally_event13 with dissolve
        mc "Here you go, Karen. This one should be familiar."
        scene ep9_dik1_sally_event14 with dissolve
        $ renpy.pause()
        scene ep9_dik1_sally_event15 with dissolve
        ka "It's not even close to being a margarita. But it's not too bad."
        scene ep9_dik1_sally_event14 with dissolve
        mc "Happy you liked it!"
    "[mod_gr]Green mixer and lime":
        mc "Let's mix these..."
        play sound "sound_effects/season2/shake.mp3"
        scene ep9_dik1_sally_event13b with dissolve
        mc "Here you go!"
        ka "It looks like a margarita."
        scene ep9_dik1_sally_event14 with dissolve
        mc "Good, that's what the bottle said it was."
        scene ep9_dik1_sally_event16 with dissolve
        ka "It's delicious!"
        scene ep9_dik1_sally_event11 with dissolve
        sy "I'm surprised you didn't fuck that up."
        scene ep9_dik1_sally_event9 with dissolve
        menu:
            "I know what I'm doing":
                mc "I know what I'm doing."
                scene ep9_dik1_sally_event11 with dissolve
                sy "You said you didn't have much experience."
                scene ep9_dik1_sally_event9 with dissolve
                mc "I'm a natural at it, then."
            "Me too":
                mc "Honestly, me too."
                scene ep9_dik1_sally_event11 with dissolve
                sy "Pfff..."
            "Joke [mod_gr][mod_choices[3]]":
                $ dk(1)
                mc "Well, I like Karen. I'm not so sure about what drink you'll be getting."
                scene ep9_dik1_sally_event11 with dissolve
                sy "I'm gonna watch you like a hawk."
                if affinity == "DIK":
                    $ dk(1)
                    scene ep9_dik1_sally_event18 with dissolve
                    mc "If that's the case, I'm gonna take your glasses away."
                    sy "Stop that!"
                    scene ep9_dik1_sally_event19 with dissolve
                    ka "Hahaha!"
                    sy "Give them back!"
                    scene ep9_dik1_sally_event20 with dissolve
                    sy "Such an asshole!"
                    scene ep9_dik1_sally_event21 with dissolve
                    sy "Just make me a drink!"
    "Neat":
        play sound "sound_effects/season2/shake.mp3"
        scene ep9_dik1_sally_event13 with dissolve
        mc "Here you go. This is the best way to drink tequila if you ask me."
        scene ep9_dik1_sally_event14 with dissolve
        $ renpy.pause()
        scene ep9_dik1_sally_event17 with dissolve
        ka "Oh, God! This one is too strong. I'm not gonna ask you for anything after this."
        scene ep9_dik1_sally_event11 with dissolve
        sy "Did you just pour tequila into a shaker?"
        scene ep9_dik1_sally_event9 with dissolve
        mc "Secret recipe."
scene ep9_dik1_sally_event22 with dissolve
mc "What do you want?"
scene ep9_dik1_sally_event23 with dissolve
sy "Actually... My hopes of you making me something I'd enjoy are exceptionally low. Give me a beer."
scene ep9_dik1_sally_event22 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Beer":
        mc "If that's what you want, here you go."
        scene ep9_dik1_sally_event24 with dissolve
        sy "Hm... I thought you'd make a big deal out of it."
        mc "As you said, you're our guests. I want you to have fun at the party."
    "[mod_gr]Derek's special bottle [mod_gr][mod_choices[3]]":
        $ dk(1)
        $ ep9_sally_drink = True
        scene ep9_dik1_sally_event25 with dissolve
        mc "(\"Don't drink\"... It's almost full too...)"
        scene ep9_dik1_sally_event26 with dissolve
        mc "*{i}Sniff sniff{/i}*"
        mc "(It smells like alcohol... Let's give it a whirl.)"
        scene ep9_dik1_sally_event24 with dissolve
        mc "Here you go, Sally."
        sy "This is not beer."
        mc "You can get beer out there. Here at The Moose, we do it differently."
        scene ep9_dik1_sally_event27 with dissolve
        $ renpy.pause()
        scene ep9_dik1_sally_event28 with dissolve
        sy "..."
        scene ep9_dik1_sally_event29 with dissolve
        sy "Maybe I spoke too soon."
        scene ep9_dik1_sally_event27 with dissolve
        $ renpy.pause()
        scene ep9_dik1_sally_event30 with dissolve
        sy "Not in a million years would I think to compliment you, but I have no choice. This drink is amazing!"
        sy "So strong! But amazing!"
        scene ep9_dik1_sally_event27 with dissolve
        mc "Huh?"
        mc "That's...good!"
        scene ep9_dik1_sally_event31 with dissolve
        mc "(What the hell is in that bottle?)"
        $ new_bio("Sally", "I gave Sally a drink from Derek's special bottle. To my surprise, she loved it.")

$ task_list[2] = ""
$ updateTaskList()
if branchIsabella and wt_ep9_branch_numbers < 2:
    scene ep9_diks_ph1_bella_call1 with dissolve
    play sound "sound_effects/cellphone.mp3"
    "*{i}Phone rings{/i}*"
    jump ep9_diks_ph1_bella_call_label
else:
    stop music fadeout 3
    $ renpy.pause(1)
    jump ep9_diks_ph1_bella_library_label

label ep9_diks_ph1_movie_event_label:
scene ep9_diks_ph1_movie_event1 with dissolve
mc "(We're playing horror movies in here the entire night.)"
scene ep9_diks_ph1_movie_event2 with dissolve
mc "(I don't know if people will be watching since it's a party. But it looks like some already are.)"
scene ep9_diks_ph1_movie_event3 with dissolve
mc "(Ok... This might be a makeout spot instead.)"

jump endEvent

label ep9_diks_ph1_drinking_event_label:
if "ep9_diks_ph1_dormies_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph1_dormies_event_label")
if branchIsabella:
    scene ep9_diks_ph1_drinking_event1 with dissolve
    tm "There you are. The competition's about to start; get over here."
    scene ep9_diks_ph1_drinking_event2 with dissolve
    mc "I'll be right back. Just...blend into the crowd."
    scene ep9_diks_ph1_drinking_event3 with dissolve
    tm "Here you go. Knock 'em dead."
else:
    scene ep9_diks_ph1_drinking_event3 with dissolve
    tm "Here you go. Time to start the competition."
scene ep9_diks_ph1_drinking_event4 with dissolve
mc "You want me to MC it?"
scene ep9_diks_ph1_drinking_event5 with dissolve
tm "You planned the party. Give it a shot."
scene ep9_diks_ph1_drinking_event6 with dissolve
stop music fadeout 3
mc "Um... What do I say?"
scene ep9_diks_ph1_drinking_event7 with dissolve
tm "Give it back. You aren't ready. Watch this."
scene ep9_diks_ph1_drinking_event8 with dissolve
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track133.mp3"])
tm "DIKs, holes, and others! Welcome to the party!"
tm "I know the wait has been unbearable, but we're back as hosts, and we're going full force!"
scene ep9_diks_ph1_drinking_event9 with dissolve
tm "The time has come for the first competition of the night!"
tm "I can see all of you looking scary and hot out there. But the question is, are you ready to get freaky?"
scene ep9_diks_ph1_drinking_event21 with dissolve
"*{i}Cheers{/i}*"
scene ep9_diks_ph1_drinking_event9 with dissolve
tm "That doesn't sound very convincing to me. Are you ready to get FREAKY!?"
if branchIsabella:
    scene ep9_diks_ph1_drinking_event22b with dissolve
else:
    scene ep9_diks_ph1_drinking_event22 with dissolve
"*{i}Cheers{/i}*"
if ep9_body_shots:
    jump ep9_diks_ph1_shot_event_label

label ep9_diks_ph1_drinking_event3_label:
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Count Cockula is my name, and drinking is the game! I'm looking for three lady volunteers!"
scene ep9_diks_ph1_drinking_event11 with dissolve
tm "And before you say anything - not you, Leon."
scene ep9_diks_ph1_drinking_event12 with dissolve
"Hahaha!"
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "I expected some half-drunken enthusiasm, and I'm met with sober modesty. Then you leave me no choice but to handpick the contestants."
tm "I can see some repeat costumes in the audience; that's gotta suck."
scene ep9_diks_ph1_drinking_event14 with dissolve
tm "Becky! Christie! Kylie! Get up here."
scene ep9_diks_ph1_drinking_event15 with dissolve
bc "I told you people would notice!"
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Slutty nurses, eh? Is it last year already?"
$ guideSuggestedPage = 56
scene ep9_diks_ph1_drinking_event23 with dissolve
tm "How about we find out which nurse is the best by having a battle of the nurses!?"
scene ep9_diks_ph1_drinking_event24 with dissolve
tm "What do you say, my half-naked brother with a skirt? Who's your winner in this race?"

menu:
    "Becky":
        $ ep9_drink_win = "Becky"
        scene ep9_diks_ph1_drinking_event25 with dissolve
        mc "Probably Becky."
        scene ep9_diks_ph1_drinking_event26 with dissolve
        tm "Into the mic, ass face."
        scene ep9_diks_ph1_drinking_event27 with dissolve
        mc "I'd be surprised if Becky didn't win this one."
        scene ep9_diks_ph1_drinking_event29 with dissolve
        bc "He is right, you know."
        scene ep9_diks_ph1_drinking_event28 with dissolve
    "Christie":

        $ ep9_drink_win = "Christie"
        scene ep9_diks_ph1_drinking_event25 with dissolve
        mc "Christie, I think."
        scene ep9_diks_ph1_drinking_event26 with dissolve
        tm "Into the mic, ass face."
        scene ep9_diks_ph1_drinking_event27 with dissolve
        mc "I believe Christie is the thirstiest girl out of the bunch."
        scene ep9_diks_ph1_drinking_event28 with dissolve
        tm "Haha, she is a thirsty girl, that's for sure."
        scene ep9_diks_ph1_drinking_event30 with dissolve
        chr "Tommy..."
        scene ep9_diks_ph1_drinking_event28 with dissolve
    "Kylie":
        $ ep9_drink_win = "Kylie"
        scene ep9_diks_ph1_drinking_event25 with dissolve
        mc "Oh, it's gonna be Kylie, for sure."
        scene ep9_diks_ph1_drinking_event26 with dissolve
        tm "Into the mic, ass face."
        scene ep9_diks_ph1_drinking_event27 with dissolve
        mc "Kylie's gonna come out on top in this one, Count Cockula."
        scene ep9_diks_ph1_drinking_event28 with dissolve
        tm "Kylie, you say?"
    "Too close to call":

        $ ep9_drink_win = "Becky"
        scene ep9_diks_ph1_drinking_event25 with dissolve
        mc "I think it's too close to call."
        scene ep9_diks_ph1_drinking_event26 with dissolve
        tm "Into the mic, ass face."
        scene ep9_diks_ph1_drinking_event27 with dissolve
        mc "I said, I think it's too close to call."
        scene ep9_diks_ph1_drinking_event28 with dissolve

tm "There's only one way to find out!"
tm "The rules are simple: the first who downs three cups of beer wins!"
scene ep9_diks_ph1_drinking_event31 with dissolve
tm "If you spill too much, you're out."
if affinity == "DIK":
    scene ep9_diks_ph1_drinking_event32 with dissolve
    mc "*{i}Whispers{/i}* Spilling on the tits is kinda hot, no?"
    scene ep9_diks_ph1_drinking_event33 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph1_drinking_event34 with dissolve
    tm "Strike that! Spilling beer on your tits does NOT disqualify."
$ guideSuggestedPage = 57
scene ep9_diks_ph1_drinking_event35 with dissolve
tm "Ready! Set! CHUG!"
scene ep9_diks_ph1_drinking_event36 with dissolve
"*{i}Cheers{/i}*"
scene ep9_diks_ph1_drinking_event37 with dissolve
tm "Here you go. You saw what I did; MC this bitch."
scene ep9_diks_ph1_drinking_event38 with dissolve
menu:
    "Hype the crowd":
        scene ep9_diks_ph1_drinking_event39 with dissolve
        mc "Look at the nurses go! They're drinking beer like it's Hell Week."
        scene ep9_diks_ph1_drinking_event40 with dissolve
        tm "Inside joke, but all right."
    "Hype Becky":
        $ dk(-1)
        $ ep9_drink_win = "Becky"
        scene ep9_diks_ph1_drinking_event41 with dissolve
        mc "Becky is really going at it! I think she's in the lead!"
    "Hype Christie":
        $ dk(-1)
        $ ep9_drink_win = "Christie"
        scene ep9_diks_ph1_drinking_event42 with dissolve
        if affinity == "CHICK":
            mc "Look at Christie! She sure can drink!"
        else:
            mc "Look at Christie! That girl sure can swallow!"
    "Hype Kylie":
        $ dk(-1)
        $ ep9_drink_win = "Kylie"
        scene ep9_diks_ph1_drinking_event43 with dissolve
        mc "Kylie's going at it! I don't think the others stand a chance!"
    "Neg Becky":
        $ dk(1)
        scene ep9_diks_ph1_drinking_event46 with dissolve
        mc "You call that drinking, Becky? It looks like you're sipping tea."
        scene ep9_diks_ph1_drinking_event47 with vpunch
        bc "Fuck you!"
        scene ep9_diks_ph1_drinking_event49 with dissolve
        if affinity == "DIK":
            mc "I give you beer on tits, people!"
            scene ep9_diks_ph1_drinking_event48 with dissolve
            "*{i}Cheers{/i}*"
            scene ep9_diks_ph1_drinking_event50 with dissolve
            $ renpy.pause()
        else:
            mc "Uh oh! Becky spilled some beer!"
            scene ep9_diks_ph1_drinking_event48 with dissolve
            mc "Don't spill too much beer, Becky, or you'll be disqualified."
    "Neg Christie":
        $ dk(1)
        scene ep9_diks_ph1_drinking_event45 with dissolve
        mc "It's not looking good for Christie. It looks like she's struggling with that beer, especially when you check out Becky and Kylie."
    "Neg Kylie":
        $ ep9_drink_win = "Kylie"
        $ dk(1)
        scene ep9_diks_ph1_drinking_event44 with dissolve
        mc "Oh, no! What's up with Kylie? She's going so slow! I think this might be it for her."
scene ep9_diks_ph1_drinking_event39 with dissolve
mc "They're all on beer number three now! Shout out for your favorite, people!"
if branchIsabella:
    scene ep9_diks_ph1_drinking_event22b with dissolve
else:
    scene ep9_diks_ph1_drinking_event22 with dissolve
"*{i}Crowd shouts{/i}*"
scene ep9_diks_ph1_drinking_event39 with dissolve
if affinity == "DIK":
    menu:
        "Spilling doesn't disqualify":
            $ ep9_drink_win = "tie"
            $ dk(1)
            mc "A reminder to the contestants that spilling beer on your tits doesn't disqualify."
            scene ep9_diks_ph1_drinking_event51 with dissolve
            mc "Look at that! They all became clumsy at the same time!"
            scene ep9_diks_ph1_drinking_event53 with dissolve
            mc "Wow, people! That was a photo finish; it's almost too close to say who won. What do you think, Count Cockula?"
            scene ep9_diks_ph1_drinking_event54 with dissolve
            tm "I believe we're all winners here tonight."
            scene ep9_diks_ph1_drinking_event53 with dissolve
            mc "It's a tie! Give the girls a round of applause."
            "*{i}Applause{/i}*"
            scene ep9_diks_ph1_drinking_event52 with dissolve
            bc "That's bullshit; I clearly won!"
        "Hype the crowd":
            jump ep9_diks_ph1_drinking_event2_label
else:
    label ep9_diks_ph1_drinking_event2_label:
    mc "We're so close to crowning the best nurse! Who will it be?"
    if ep9_drink_win == "Christie":
        scene ep9_diks_ph1_drinking_event55 with dissolve
        chr "Done!"
        scene ep9_diks_ph1_drinking_event59 with dissolve
        mc "Christie wins!"
        scene ep9_diks_ph1_drinking_event57 with dissolve
        bc "Bullshit!"
        "*{i}Cheers{/i}*"
    elif ep9_drink_win == "Kylie":
        scene ep9_diks_ph1_drinking_event56 with dissolve
        ky "Suck it!"
        scene ep9_diks_ph1_drinking_event59 with dissolve
        mc "We have a winner! It's Kylie!"
        scene ep9_diks_ph1_drinking_event57 with dissolve
        bc "No way!!! She cheated!"
        "*{i}Cheers{/i}*"
    else:
        scene ep9_diks_ph1_drinking_event58 with dissolve
        bc "I WIN!"
        scene ep9_diks_ph1_drinking_event59 with dissolve
        mc "It looks like Becky is our winner!"
        "*{i}Cheers{/i}*"
        scene ep9_diks_ph1_drinking_event58 with dissolve
        bc "Yes! I'm the best nurse!"
        menu:
            "Neg Becky":
                $ dk(1)
                scene ep9_diks_ph1_drinking_event59 with dissolve
                mc "I don't know about that, but you sure can drink like a man."
            "Whatever you say":
                scene ep9_diks_ph1_drinking_event59 with dissolve
                mc "Whatever you say, Becky."

scene ep9_diks_ph1_drinking_event60 with dissolve
tm "Good job. The crowd enjoyed that."
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Now! Who's next!?"

scene ep9_diks_ph1_drinking_event61 with fade
rs "Nice job with that competition! Super-entertaining."
scene ep9_diks_ph1_drinking_event62 with dissolve
le "Girls are getting drunk early; I love it."
if minigames:
    scene ep9_diks_ph1_drinking_event69 with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
    $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
    $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
    $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)

    $ mphone_pp_history_list.append("• The {color=ffed00}Drinking Competition{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Drinking Competition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Drinking Competition{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Drinking Competition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg


if branchIsabella:
    scene ep9_diks_ph1_drinking_event63 with dissolve
    isa "That was...college-like."
    scene ep9_diks_ph1_drinking_event65 with dissolve
    mc "It's all for the guests."
    scene ep9_diks_ph1_drinking_event64 with dissolve
    isa "Sure..."
    scene ep9_diks_ph1_drinking_event65 with dissolve
    mc "I think you blended nicely into the crowd."
    mc "How about that drink now?"
    stop music fadeout 3
    scene ep9_diks_ph1_drinking_event64 with dissolve
    isa "Lead the way."
    jump ep9_bella_drink_cont_label
else:
    $ event_list.append("ep9_diks_ph1_end_event_label")
jump endEvent

label ep9_diks_ph1_shot_event_label:
$ guideSuggestedPage = 57
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Count Cockula is my name, and body shots is the game!"
tm "We need DIKs and chicks, bros and hoes, poles and holes on stage for this. Let's say three brave couples who aren't afraid to show some skin or get licked."
scene ep9_diks_ph1_drinking_event11 with dissolve
tm "I can see Leon moving toward the stage. Who's gonna be the brave guy to lick her?"
scene ep9_diks_ph1_drinking_event13 with dissolve
le "Fuck you! I'm not doing this with a dude!"
"Hahaha!"
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "I'm seeing triple here. Are we having three slutty nurses at the same party? Is it last year already?"
scene ep9_diks_ph1_drinking_event14 with dissolve
tm "Eh... Becky! Get up here."
scene ep9_diks_ph1_drinking_event15 with dissolve
bc "I told you people would notice!"
if branchIsabella:
    scene ep9_diks_ph1_drinking_event16 with dissolve
else:
    scene ep9_diks_ph1_drinking_event16b with dissolve
tm "I see Tiffani in the crowd! Get up here, you! You're not known to be shy."
scene ep9_diks_ph1_drinking_event17 with dissolve
ti "Do I have to?"
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Unless you're scared. I wouldn't blame you; it's Halloween after all."
scene ep9_diks_ph1_drinking_event17 with dissolve
ti "All right."
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Only Leon volunteering from the DIKs? What the hell, bros?"
tm "Jamie!? Where's Jamie?"
scene ep9_diks_ph1_drinking_event18 with dissolve
dn "Don't you dare."
scene ep9_diks_ph1_drinking_event11 with dissolve
tm "John Boy? Get your ass over here!"
scene ep9_diks_ph1_drinking_event19 with dissolve
jb "Sorry, I only lick girls together with Elena."
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Man, so whipped! Derek!!! Where's Derek?"
scene ep9_diks_ph1_drinking_event20 with dissolve
de "Is this gonna be like our first week or not?"
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Get the fuck up here. I'll have your brother join you so it will feel like it is."
menu:
    "Accept":
        scene ep9_diks_ph1_drinking_event71 with dissolve
        mc "All right, let's do it."
    "Refuse":
        scene ep9_diks_ph1_drinking_event71 with dissolve
        mc "Sorry, I'm not gonna do it."
        scene ep9_diks_ph1_drinking_event72 with dissolve
        tm "It wasn't a question. You're gonna do it. It's a show for the guests, and you're a host."
scene ep9_diks_ph1_drinking_event10 with dissolve
tm "Gina! Come up here!"
scene ep9_diks_ph1_drinking_event73 with dissolve
tm "Brothers! Couple up and show some skin."
tm "DIKs! Can we get 18 shots on the stage?"
menu:
    "Body shots with Becky":
        $ ep9_body_shots_becky = True
        scene ep9_diks_ph1_drinking_event74 with dissolve
        mc "You're with me then."
        scene ep9_diks_ph1_drinking_event75 with dissolve
        bc "We better win! I'm not gonna look like a fool in front of this many people, ok?"
        scene ep9_diks_ph1_drinking_event79 with dissolve
    "Body shots with Tiffani":
        $ ep9_body_shots_becky = False
        scene ep9_diks_ph1_drinking_event76 with dissolve
        mc "Wanna do it?"
        scene ep9_diks_ph1_drinking_event77 with dissolve
        ti "Sure. But let's do the body shots first."
        scene ep9_diks_ph1_drinking_event78 with dissolve

tm "All right, people! We have our contestants!"
tm "And the rules are simple and should be familiar to all the recurring degenerates of our parties!"
if ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event80 with dissolve
else:
    scene ep9_diks_ph1_drinking_event80b with dissolve
tm "Each couple does six body shots - that's three shots each for everyone on stage! All of them must be done while straddling your partner."
tm "First - the mouth shot! Pour a shot into your mouth and transfer it to your partner below you."
tm "Secondly - the body shot! Pour a shot on their mid part - that will be boobs for the girls and stomach for the guys - and slurp it up."
scene ep9_diks_ph1_drinking_event81 with dissolve
tm "And lastly?"
scene ep9_diks_ph1_drinking_event82 with dissolve
dikcs "Crotch shot!"
scene ep9_diks_ph1_drinking_event81 with dissolve
tm "Looks like we have some regulars in the crowd! The crotch shot!"
tm "Put a shot glass between your partner's legs, close to the crotch, and drink it!"
if ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event80 with dissolve
else:
    scene ep9_diks_ph1_drinking_event80b with dissolve
tm "After you've done your three shots, swap positions and do three more shots."
tm "The fastest couple wins!"
if not ep2_shotWon:
    if ep9_body_shots_becky:
        scene ep9_diks_ph1_drinking_event83 with dissolve
    else:
        scene ep9_diks_ph1_drinking_event83b with dissolve
    tm "Watch out for Derek; he tends to puke."

scene ep9_diks_ph1_drinking_event81 with dissolve
tm "Boys on top. Get into starting positions."

if ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event84 with dissolve
    bc "You got the order straight?"
    scene ep9_diks_ph1_drinking_event85 with dissolve
    if affinity == "DIK":
        mc "I think so. Lips, tits, pussy."
    else:
        mc "I think so. Mouth, chest, crotch."
    scene ep9_diks_ph1_drinking_event86 with dissolve
    bc "I want to win, so don't fuck this up."
else:
    scene ep9_diks_ph1_drinking_event112 with dissolve
    ti "I know it's a competition, but it's ok if you linger a bit."
    scene ep9_diks_ph1_drinking_event113 with dissolve
    if affinity == "DIK":
        mc "Haha, funny."
        scene ep9_diks_ph1_drinking_event114 with dissolve
        ti "I'm not joking."
    else:
        mc "What?"
        scene ep9_diks_ph1_drinking_event114 with dissolve
        ti "You'll see."

scene ep9_diks_ph1_drinking_event81 with dissolve
tm "Ready! Set! SHOTS!"
if persistent.mod_wtenabled and (not branchAlone or wt_ep9_branch_numbers > 1):
    "scrappy" "From this point on you get a new stat/points that's on non alone paths. I didn't see any info on it so I just assume it's cheating on you girl/path score and I'll show in menu with [mod_gr](+cheater)"
if persistent.mod_wtenabled: 
                        $mod_choices = ["(to win)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
$ tmpInt = 0
if ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event87 with dissolve
    mc "(Mouth shot!)"
    menu:
        "Transfer shot [mod_gr][mod_choices[0]]":
            $ tmpInt += 1
            scene ep9_diks_ph1_drinking_event88 with dissolve
            bc "*{i}Gulp{/i}*"
        "Spill shot":
            scene ep9_diks_ph1_drinking_event90 with vpunch
            mc "Pfff!"
            bc "Prrft! What are you doing!?"
        "Enjoy it too much [mod_gr][mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            scene ep9_diks_ph1_drinking_event88 with dissolve
            bc "*{i}Gulp{/i}*"
            scene ep9_diks_ph1_drinking_event89 with dissolve
            bc "*{i}Mmpfff{/i}* Are you using your tongue?"
    scene ep9_diks_ph1_drinking_event91 with dissolve
    bc "Pour it on my chest! Hurry!!!"
    menu:
        "Pour fast [mod_gr][mod_choices[0]]":
            $ tmpInt += 1
        "Pour slowly":
            scene ep9_diks_ph1_drinking_event92 with dissolve
            bc "What are you doing!? Hurry up!!!"
    scene ep9_diks_ph1_drinking_event93 with dissolve
    bc "Drink it already!!!"
    scene ep9_diks_ph1_drinking_event94 with dissolve
    bc "Crotch shot!!!"
    scene ep9_diks_ph1_drinking_event95 with dissolve
    bc "DRINK IT!!!"
    scene ep9_diks_ph1_drinking_event96 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph1_drinking_event97 with dissolve
    bc "What's taking so long!?"
    if branchIsabella:
        scene ep9_diks_ph1_drinking_event98 with dissolve
        $ renpy.pause()
else:
    scene ep9_diks_ph1_drinking_event115 with dissolve
    mc "(Mouth shot!)"
    menu:
        "Transfer shot":
            scene ep9_diks_ph1_drinking_event116 with dissolve
            ti "*{i}Gulp{/i}*"
            scene ep9_diks_ph1_drinking_event118 with dissolve
            mc "*{i}Mmppfhh{/i}* Hey!"
            scene ep9_diks_ph1_drinking_event119 with dissolve
            ti "Hahaha!"
            scene ep9_diks_ph1_drinking_event81 with dissolve
            tm "Everyone! Cheer for your favorite couple!"
        "Spill shot":
            scene ep9_diks_ph1_drinking_event121 with vpunch
            mc "Pfff!"
            ti "Hey! What the hell!?"
            scene ep9_diks_ph1_drinking_event81 with dissolve
            tm "Haha! I guess that's one way to do it! Cheer for your favorite couple, people!"
        "Enjoy it too much [mod_gr][mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            scene ep9_diks_ph1_drinking_event116 with dissolve
            ti "*{i}Gulp{/i}*"
            scene ep9_diks_ph1_drinking_event117 with dissolve
            $ renpy.pause()
            scene ep9_diks_ph1_drinking_event120 with dissolve
            ti "Wow... You're a good kisser."
            scene ep9_diks_ph1_drinking_event81 with dissolve
            tm "Everyone! Cheer for your favorite couple!"
    scene ep9_diks_ph1_drinking_event122 with dissolve
    ti "Get them good and wet."
    scene ep9_diks_ph1_drinking_event123 with dissolve
    ti "Haha! Yes! Get in there! Tongue me!"
    scene ep9_diks_ph1_drinking_event50 with dissolve
    "*{i}Crowd cheers{/i}*"
    if branchIsabella:
        scene ep9_diks_ph1_drinking_event98 with dissolve
        $ renpy.pause()
    scene ep9_diks_ph1_drinking_event124 with dissolve
    mc "The final shot... Put the glass...there."
    scene ep9_diks_ph1_drinking_event125 with dissolve
    ti "Don't shout it out, but I'm not wearing any panties."
    scene ep9_diks_ph1_drinking_event126 with dissolve
    mc "Holy..."
    scene ep9_diks_ph1_drinking_event127 with dissolve
    if branchAlone:
        mc "(This girl is wild.)"
    else:
        mc "(This girl is wild. I need to restrain myself.)"
    scene ep9_diks_ph1_drinking_event128 with dissolve
    bc "EWW!!! I don't wanna have your ass in my face!!!"
    "*{i}Laughter{/i}*"

scene ep9_diks_ph1_drinking_event81 with dissolve
if ep9_body_shots_becky and tmpInt > 1:
    tm "It looks like [name] and Becky are in the lead! But the race is not over yet!"
else:
    tm "It looks like Leon and Gina are in the lead!"

if ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event99 with dissolve
    if ep9_body_shots_becky and tmpInt > 1:
        bc "Let's not lose the lead! Open your fucking mouth!"
    else:
        bc "We need to go faster!!! Open your fucking mouth!"
    scene ep9_diks_ph1_drinking_event100 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph1_drinking_event101 with dissolve
    bc "*{i}Lick lick{/i}*"
    scene ep9_diks_ph1_drinking_event81 with dissolve
    tm "It's almost over now! It's still anyone's game!"
    scene ep9_diks_ph1_drinking_event102 with dissolve
    bc "Hold still! Don't drop the shot."
    menu:
        "Focus [mod_gr][mod_choices[0]]":
            scene ep9_diks_ph1_drinking_event105 with dissolve
            bc "*{i}Gulp{/i}*"
        "Drop the shot":
            $ tmpInt = 0
            scene ep9_diks_ph1_drinking_event104 with dissolve
            bc "No! What are you doing!?"
            scene ep9_diks_ph1_drinking_event103 with dissolve
            mc "Mmmphff!"

    if tmpInt >= 2:
        $ ep9_shot_win = True
        scene ep9_diks_ph1_drinking_event106 with dissolve
        bc "DONE!"
        tm "[name] and Becky win!"
        scene ep9_diks_ph1_drinking_event107 with dissolve
        bc "Yes! Suck it! I'm the best nurse!"
        scene ep9_diks_ph1_drinking_event108 with dissolve
        bc "Thanks to everyone cheering for me! I knew I would win!"
        scene ep9_diks_ph1_drinking_event109 with dissolve
        gi "Bitch, sit down. You won a drinking game, not a movie award."
    else:
        scene ep9_diks_ph1_drinking_event110 with dissolve
        gi "Done!"
        tm "What a sprint! Leon and Gina win!"
        scene ep9_diks_ph1_drinking_event111 with dissolve
        bc "No!!! This is your fault!"
else:
    scene ep9_diks_ph1_drinking_event129 with dissolve
    tm "We're halfway there now! Looks like everyone's doing the second mouth shot!"
    scene ep9_diks_ph1_drinking_event130 with dissolve
    mc "Glurggg!"
    ti "Mmm!!!"
    tm "Some are definitely enjoying this way more than others! Don't you love to see it!?"
    "*{i}Cheers{/i}*"
    scene ep9_diks_ph1_drinking_event131 with dissolve
    ti "Here comes the tongue!"
    ti "*{i}Lick lick{/i}*"
    scene ep9_diks_ph1_drinking_event132 with dissolve
    ti "Final shot now."
    scene ep9_diks_ph1_drinking_event133 with dissolve
    mc "Oh, damn!"
    ti "Don't be shy. Say hello to her."
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone  or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
    menu:
        "Try to ignore it [mod_gr][mod_choices[2]]":
            $ dk(-1)
            scene ep9_diks_ph1_drinking_event134 with dissolve
            mc "Do the shot already!"
        "Greet Tiffani's hole [mod_gr][mod_choices[3]]{color=#E6F653}[mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            $ dk(1)
            $ ep9_tiffani_lick = True
            scene ep9_diks_ph1_drinking_event135 with dissolve
            mc "*{i}Lick lick{/i}*"
            scene ep9_diks_ph1_drinking_event136 with dissolve
            ti "Hngn!!!"

    scene ep9_diks_ph1_drinking_event137 with dissolve
    gi "Done!"
    tm "What a sprint! Leon and Gina win!"
    bc "What!? No!!!"
    scene ep9_diks_ph1_drinking_event138 with dissolve
    bc "You suck!"
    de "Ugh. Fuck you, Becky."

scene ep9_diks_ph1_drinking_event81 with dissolve
tm "Give it up for the contestants! Let's get some fresh meat on stage! Who's next?"

if not ep9_body_shots_becky:
    scene ep9_diks_ph1_drinking_event139 with fade
    le "Nice battle, bros!"
    scene ep9_diks_ph1_drinking_event140b with dissolve
    de "Dude, Becky's pussy stinks."
    le "Was it smelly?"
    de "I don't know what it was, but it made me gag."
    $ new_bio("Tiffani", "I did body shots with Tiffani during the competition. She's wild!")
else:
    scene ep9_diks_ph1_drinking_event139b with fade
    le "Nice battle, bros!"
    scene ep9_diks_ph1_drinking_event140 with dissolve
    de "That Tiffani girl is crazy! She wasn't wearing any panties!"
    le "Damn! That sounds like a victory to me."
    $ new_bio("Becky", "I did body shots with Becky during the competition. She gets bossy.")
if minigames:
    scene ep9_diks_ph1_drinking_event70 with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[1] = min(pp_happiness_level[1]+3,100)
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+3,100)
    $ pp_happiness_level[5] = min(pp_happiness_level[5]+3,100)
    $ pp_happiness_level[7] = min(pp_happiness_level[7]+3,100)

    $ mphone_pp_history_list.append("• The {color=ffed00}Body Shots{/color} activity increased Jacob's happiness by {color=00ff00}+3%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Body Shots{/color} activity increased Jamie's happiness by {color=00ff00}+3%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Body Shots{/color} activity increased Nick's happiness by {color=00ff00}+3%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Body Shots{/color} activity increased Tommy's happiness by {color=00ff00}+3%{/color}.")
    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg

if branchIsabella:
    scene ep9_diks_ph1_drinking_event68 with dissolve
    if affinity == "DIK":
        mc "Did you see that!? I did pretty good."
        scene ep9_diks_ph1_drinking_event64 with dissolve
        isa "It looked like you did a thorough job."
        scene ep9_diks_ph1_drinking_event65 with dissolve
        mc "Let me guess; you didn't like it?"
        scene ep9_diks_ph1_drinking_event64 with dissolve
        isa "No, of course I liked watching you tongue another girl, and having her reciprocate. It's every girl's dream to see that."
        scene ep9_diks_ph1_drinking_event65 with dissolve
        mc "That's sarcasm, right? Sometimes I feel like you need to announce if it is. Especially when your face is covered like that, it's even harder to guess."
        scene ep9_diks_ph1_drinking_event66 with dissolve
        isa "SARCASM!"
        scene ep9_diks_ph1_drinking_event67 with dissolve
        mc "That's...better."
        mc "I'll try better to avoid those games then."
        scene ep9_diks_ph1_drinking_event64 with dissolve
    else:
        mc "Um... Sorry you had to see that. Tommy made me do it."
        scene ep9_diks_ph1_drinking_event64 with dissolve
        isa "Don't you have free will here?"
        scene ep9_diks_ph1_drinking_event65 with dissolve
        mc "I have, but he made the case it was entertainment for the guests. And since I planned the party and all..."
        scene ep9_diks_ph1_drinking_event64 with dissolve
        isa "*{i}Sigh{/i}* It's ok, [name]."

    isa "I know it's an innocent game to you, but I feel I outgrew these activities ten years ago."
    isa "I'm more irritated with the realization of how old it made me feel to watch and feel so disconnected."
    scene ep9_diks_ph1_drinking_event65 with dissolve
    mc "You could have volunteered, you know."
    scene ep9_diks_ph1_drinking_event64 with dissolve
    isa "Good one! Don't push it."
    stop music fadeout 3
    scene ep9_diks_ph1_drinking_event65 with dissolve
    mc "Let's go get that drink now."
    jump ep9_bella_drink_cont_label
else:
    $ event_list.append("ep9_diks_ph1_end_event_label")
jump endEvent

label ep9_diks_ph1_rusty_event_label:
$ guideSuggestedPage = 53
scene ep9_diks_ph1_rusty_event1 with dissolve
rs "Micha. You remember [name], right?"
scene ep9_diks_ph1_rusty_event2 with dissolve
if ep8_recital_failed:
    mic "Oh, right. From that dorm party, yeah."
    mic "You're the guy who got super-drunk."
    scene ep9_diks_ph1_rusty_event3 with dissolve
    if ep8_mansion_won:
        mc "We were celebrating and blowing off some steam. I might have gone over the top, but it was well-deserved."
    else:
        mc "Yeah, I suppose. The DIKs needed it that night."
    scene ep9_diks_ph1_rusty_event4 with dissolve
    if ep8_mansion_won:
        rs "It totally was. After all you did to get us back on track after the alphas trashed this place."
        scene ep9_diks_ph1_rusty_event5 with dissolve
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
        menu:
            "Don't mention it":
                mc "Hey, don't mention it."
            "You're the real leader [mod_gr][mod_choices[2]]{color=#E6F653}[mod_choices[0]]":
                $ dk(-1)
                $ RPdiks += 1
                mc "I did what I could, but it was under your leadership."
                scene ep9_diks_ph1_rusty_event4 with dissolve
                rs "Thanks, [name]."
                scene ep9_diks_ph1_rusty_event7 with dissolve
                mic "Wow, Rusty."
    else:
        rs "Yeah, we did. And look at us now. We're back in business."
        scene ep9_diks_ph1_rusty_event5 with dissolve
        mc "Honestly, I don't know how we're managing it, with the budget and all."
        scene ep9_diks_ph1_rusty_event6 with dissolve
        rs "None of that boring talk tonight, [name]. Tonight, we're all about drinking 'til we drop."
else:
    mic "You're Tremolo! Aren't you?"
    scene ep9_diks_ph1_rusty_event3 with dissolve
    if roosterNickMCCustom == "Tremolo":
        mc "Yeah, that's my nickname on Rooster."
    else:
        mc "I used to use that nickname on Rooster, yeah."
    scene ep9_diks_ph1_rusty_event9 with dissolve
    mic "No! Not from Rooster! From that concert. You played the guitar."
    scene ep9_diks_ph1_rusty_event8 with dissolve
    rs "There's a video of that online with like 100,000 views."
    scene ep9_diks_ph1_rusty_event7 with dissolve
    mic "Yeah, I saw it! It's so good!"
    scene ep9_diks_ph1_rusty_event10 with dissolve
    mc "Thank you. I'm a bit embarrassed; I'm not used to getting compliments for it."
    scene ep9_diks_ph1_rusty_event9 with dissolve
    mic "It was so cool. So, so cool!"
    scene ep9_diks_ph1_rusty_event4 with dissolve
    rs "You hear that, [name]? You're becoming a campus name."
    scene ep9_diks_ph1_rusty_event10 with dissolve
    if affinity == "DIK":
        mc "With the crazy stuff I've done so far, it's about time."
    else:
        mc "I hope not. It would feel weird."
    scene ep9_diks_ph1_rusty_event7 with dissolve
    mic "Wait, is this the guy you mentioned before too?"
    scene ep9_diks_ph1_rusty_event4 with dissolve
    rs "Yeah, it is."
    if ep8_mansion_won:
        rs "[name] is such a trouper. He helped us get back on track after the alphas trashed this place."
        scene ep9_diks_ph1_rusty_event5 with dissolve
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone:
                             $mod_choices[10]="(+Cheater)"
        menu:
            "Don't mention it":
                mc "Hey, don't mention it."
            "You're the real leader [mod_gr][mod_choices[2]]{color=#E6F653}[mod_choices[0]]":
                $ dk(-1)
                $ RPdiks += 1
                mc "I did what I could, but it was under your leadership."
                scene ep9_diks_ph1_rusty_event4 with dissolve
                rs "Thanks, [name]."
                scene ep9_diks_ph1_rusty_event7 with dissolve
                mic "Wow, Rusty."
    else:
        rs "He did what he could to help us get back on track after the alphas trashed this place."
        rs "And look at us now. We're back in business."
        scene ep9_diks_ph1_rusty_event5 with dissolve
        mc "Honestly, I don't know how we're managing it, with the budget and all."
        scene ep9_diks_ph1_rusty_event6 with dissolve
        rs "None of that boring talk tonight, [name]. Tonight, we're all about drinking 'til we drop."

scene ep9_diks_ph1_rusty_event10 with dissolve
mc "Cheers to you two! I'll see you around."
scene ep9_diks_ph1_rusty_event12 with dissolve
if ep8_mansion_won or not ep8_recital_failed:
    mic "I like that guy."
else:
    mic "He seems like a decent guy."
scene ep9_diks_ph1_rusty_event11 with dissolve
if ep8_mansion_won or not ep8_recital_failed:
    rs "Yeah, he's the best."
else:
    rs "He totally is."

rs "So, what have you been up to lately?"
$ task_list[3] = ""
$ updateTaskList()
$ new_bio("Rusty", "Rusty seems to be interested in Micha. He sure likes to talk to her.")
jump endEvent

label ep9_diks_ph1_derek_event_label:
scene ep9_dik1_derek_event1 with dissolve
de "I was only making friendly small talk!"
scene ep9_dik1_derek_event4 with dissolve
che "No, you're dissing me."
scene ep9_dik1_derek_event2 with dissolve
de "I was complimenting your outfit."
scene ep9_dik1_derek_event4 with dissolve
che "How was that a compliment?"
scene ep9_dik1_derek_event2 with dissolve
de "I said, \"What a cool ninja outfit\". What's wrong with that?"
scene ep9_dik1_derek_event5 with dissolve
che "I'm not a ninja! I'm a ghost, you bigot."
scene ep9_dik1_derek_event3 with dissolve
de "Don't you call me the B-word, bitch!"
scene ep9_dik1_derek_event7 with dissolve
mc "Hey, guys. Don't get riled up. We're here to party, right?"
scene ep9_dik1_derek_event8 with dissolve
de "I'm trying to, but this ninja is being a bitch."
scene ep9_dik1_derek_event5 with dissolve
che "I'm a bitch? I'll fuck your mother!"
scene ep9_dik1_derek_event6 with dissolve
ma "Chen. Chill."
scene ep9_dik1_derek_event9 with dissolve
mc "Derek will stop being a bigot, and Chen won't fuck your mother."
scene ep9_dik1_derek_event10 with dissolve
mc "You're obviously a very scary ghost, and you're...not even wearing a costume. Nice."
scene ep9_dik1_derek_event11 with dissolve
ma "Oh, yeah. Where did I put it?"
scene ep9_dik1_derek_event12 with dissolve
mc "Don't make it worse."
$ guideSuggestedPage = 53
scene ep9_dik1_derek_event13 with dissolve
de "Who even invited those two?"
scene ep9_dik1_derek_event12 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "We can throw them out [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "You can ask Tommy about that. If they're being assholes, we can throw them out."
        scene ep9_dik1_derek_event13 with dissolve
        de "No, it's cool. It was just a misunderstanding."
        scene ep9_dik1_derek_event12 with dissolve
        mc "Well... Let me know if they start something."
    "Don't start something [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "I don't know, but don't start a fight tonight."
        scene ep9_dik1_derek_event13 with dissolve
        de "I'm not. I was showing hospitality."

$ optional_task_list[4] = ""
jump endEvent

label ep9_diks_ph1_leon_event_label:
$ guideSuggestedPage = 52
scene ep9_dik1_leon_event1 with dissolve
le "And he even invites Dany! I feel humiliated."
scene ep9_dik1_leon_event2 with dissolve
mc "Leon? How are you doing? Not having a good time?"
scene ep9_dik1_leon_event3 with dissolve
le "It's Jamie. He fucked me over."
le "We were gonna have theme costumes, and he bailed on me. I feel ridiculous wearing this."
scene ep9_dik1_leon_event2 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Sympathize [mod_gr][mod_choices[3]]":
        $ dk(-1)
        mc "Bro, that sucks."
        scene ep9_dik1_leon_event4 with dissolve
        le "Tell me about it..."
    "Joke [mod_gr][mod_choices[2]]":
        $ dk(1)
        mc "Haha! Sorry, but I have a hard time seeing how anything Jamie would wear wouldn't make you look ridiculous."
        scene ep9_dik1_leon_event3 with dissolve
        le "You'd have to see it to get it."
        le "If it were both of us dressed up like this, it wouldn't feel like we were being serious about it."

scene ep9_dik1_leon_event2 with dissolve
mc "Go change into something else; there's still time before everyone shows up."
scene ep9_dik1_leon_event3 with dissolve
le "Who buys two costumes for Halloween?"
scene ep9_dik1_leon_event4 with dissolve
le "Hey, is it ok if we kick Dany out? I didn't see her on the guest list."
scene ep9_dik1_leon_event2 with dissolve
mc "You want me to kick out someone who Jamie invited to the party?"
scene ep9_dik1_leon_event3 with dissolve
le "She's a party killer, dude. In a few hours, she'll be lecturing people on why they shouldn't be wearing slutty outfits."
scene ep9_dik1_leon_event2 with dissolve
menu:
    "If it's needed [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "I'll see what I can do if it's needed."
    "I can't do that [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "I can't do that. She's Jamie's guest."
        scene ep9_dik1_leon_event4 with dissolve
        le "He's falling back into a destructive pattern."
    "Joke [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "She seemed supportive of your outfit."
        scene ep9_dik1_leon_event3 with dissolve
        le "Fuck you. Don't bust my balls tonight."
        scene ep9_dik1_leon_event2 with dissolve
        mc "Jamie made his choice about her."
        scene ep9_dik1_leon_event4 with dissolve
        le "It's the wrong choice."
scene ep9_dik1_leon_event5 with dissolve
mc "Cheer up. Drink some more and try to have fun. It's gonna be an awesome night."

if (minigames and pp_current_party_happiness[4] > 2) or (not minigames and pp_current_party_happiness[4] == 1):
    scene ep9_dik1_leon_event7 with dissolve
    le "You did amazing planning this party. I'll give you that."
elif (minigames and pp_current_party_happiness[4] > 1) or (not minigames and pp_current_party_happiness[4] == 0):
    scene ep9_dik1_leon_event7 with dissolve
    le "Aside from Dany being here, the party seems kind of cool."
else:
    scene ep9_dik1_leon_event6 with dissolve
    le "Meh. I'm not so sure about that. This party isn't what I had in mind."
$ task_list[1] = ""
$ updateTaskList()
$ new_bio("Leon", "Leon was upset that Jamie bailed on their theme costume and went back to Dany.")
$ new_bio("Jamie", "Jamie bailed on the theme costume idea with Leon, thinking it was just talk.")
jump endEvent

label ep9_diks_ph1_bella_call_label:
scene ep9_diks_ph1_bella_call2 with dissolve
mc "Hey! Are you here yet?"
scene ep9_diks_ph1_bella_call5 with dissolve
isa "No, but I'll be leaving work soon."
scene ep9_diks_ph1_bella_call4 with dissolve
mc "Work? Tonight?"
scene ep9_diks_ph1_bella_call5 with dissolve
isa "I'm grading the midterm papers."
scene ep9_diks_ph1_bella_call6 with dissolve
mc "Nice! I hope I passed."
scene ep9_diks_ph1_bella_call7 with dissolve
isa "The results are very...mixed. At times, I wondered if you took the same test."
scene ep9_diks_ph1_bella_call6 with dissolve
mc "Oof, that sounds bad..."
scene ep9_diks_ph1_bella_call7b with dissolve
isa "About tonight..."
scene ep9_diks_ph1_bella_call7c with dissolve
mc "You're not having second thoughts, are you?"
scene ep9_diks_ph1_bella_call7 with dissolve
isa "We'll see... Will you meet me by your window?"
scene ep9_diks_ph1_bella_call6 with dissolve
mc "Yeah, I'll head there and wait for you whenever you're ready."
scene ep9_diks_ph1_bella_call7 with dissolve
isa "Give me like 15 minutes or so."
scene ep9_diks_ph1_bella_call6 with dissolve
mc "You got it."
scene ep9_diks_ph1_bella_call3 with dissolve
mc "(She really is coming. I was sure she was going to bail on the party.)"
$ currentFreeRoamLabel = "ep9_diks_ph1_1corr_label"
$ event_list.append("ep9_diks_ph1_bella_event_label")
jump endEvent

label ep9_diks_ph1_bella_library_label:
scene ep9_diks_ph1_bella_library5 with wipeleft
isa "*{i}Mumbles{/i}* Nope. Completely wrong."
play music "music/ep9/relaxed.mp3"
scene ep9_diks_ph1_bella_library7 with dissolve
isa "*{i}Mumbles{/i}* \"Fuck\"? Who swears on a test in college? So juvenile..."
isa "*{i}Mumbles{/i}* God, I'm tempted to write \"Incorrect as fuck\" on this one."
scene ep9_diks_ph1_bella_library8 with dissolve
isa "*{i}Mumbles{/i}* Next..."
scene ep9_diks_ph1_bella_library9 with dissolve
isa "*{i}Mumbles{/i}* Great... Wait..."
isa "*{i}Mumbles{/i}* That's the right answer...but not to that question. Uh..."
isa "*{i}Mumbles{/i}* Did they mix up the order?"
scene ep9_diks_ph1_bella_library4 with dissolve
play sound "sound_effects/cellphone.mp3"
"*{i}Phone rings{/i}*"
scene ep9_diks_ph1_bella_library3 with dissolve
isa "Jill?"
if branchJill:
    scene ep9_diks_ph1_bella_library10 with dissolve
else:
    scene ep9_diks_ph1_bella_library10b with dissolve
ji "I hope I'm not interrupting your fun evening at work."
scene ep9_diks_ph1_bella_library2 with dissolve
isa "*{i}Sigh{/i}* It's a good interruption. What's on your mind?"
if branchJill:
    scene ep9_diks_ph1_bella_library10 with dissolve
    ji "So, I'm on my way to the Halloween party soon."
    scene ep9_diks_ph1_bella_library1 with dissolve
    isa "Good for you. Are you excited?"
    scene ep9_diks_ph1_bella_library11 with dissolve
    ji "Excited, yes. But also a bit worried."
    ji "I picked a pretty stupid costume. I can barely move with it."
    scene ep9_diks_ph1_bella_library1 with dissolve
    isa "Well, there's not much that can be done about that now."
    scene ep9_diks_ph1_bella_library10 with dissolve
    ji "No, there's not. I'll be fine."
    ji "What about you?"
    scene ep9_diks_ph1_bella_library2 with dissolve
    isa "I'll be correcting papers for a while, and then I'll probably head back home."
    scene ep9_diks_ph1_bella_library11 with dissolve
    ji "Are you sure you don't want to come to the party with me? I'm sure people won't mind."
    ji "Some of my friends are coming too. They practically begged me for an invite."
    scene ep9_diks_ph1_bella_library2 with dissolve
    isa "Pass. Back in college, I wouldn't have liked it if my teachers had come to our parties."
else:
    scene ep9_diks_ph1_bella_library10b with dissolve
    ji "So, I'm on my way to the Halloween party soon."
    scene ep9_diks_ph1_bella_library1 with dissolve
    isa "Good for you. Are you excited?"
    if ep9_jill_mood == 1:
        scene ep9_diks_ph1_bella_library11b with dissolve
        ji "Yes and no. While I want to spend the night with my friends, [name] will be there..."
        ji "It might feel too hard to see him after..."
        scene ep9_diks_ph1_bella_library2 with dissolve
        isa "You can't avoid him forever."
        scene ep9_diks_ph1_bella_library11b with dissolve
        ji "I'm not avoiding him, but it still hurts."
        scene ep9_diks_ph1_bella_library1 with dissolve
        isa "Don't think too much about it. Focus on having a fun time with your friends instead."
    else:
        scene ep9_diks_ph1_bella_library10b with dissolve
        ji "Hm... Yes and no. I get to spend the night with my friends, which I'll enjoy, but I'm not sure about what kind of party it will be."
        scene ep9_diks_ph1_bella_library1 with dissolve
        isa "Well, you know [name] by now. It could be anything between heaven and hell."
        scene ep9_diks_ph1_bella_library12b with dissolve
        ji "Yeah... I feel a bit weird about that."
        ji "He didn't invite me. Josy did."
        scene ep9_diks_ph1_bella_library2 with dissolve
        isa "I see."
        if ep8_jill_rejected_you:
            scene ep9_diks_ph1_bella_library12b with dissolve
            ji "I hope he's ok with it, but I'm not sure... Do you think I should have asked him first?"
            ji "I thought maybe he would have invited me, so now I don't know what to make of it."
        else:
            scene ep9_diks_ph1_bella_library12b with dissolve
            ji "I don't know what to make of it, really."
        scene ep9_diks_ph1_bella_library2 with dissolve
        isa "Maybe he didn't think you'd want to go. I mean, I'm kind of surprised you're going myself."
        scene ep9_diks_ph1_bella_library10b with dissolve
        ji "True. But Bianca and Olivia got all excited when I said I was invited."
        ji "It turns out they've wanted to go to their parties for a while to see what they're like."
        scene ep9_diks_ph1_bella_library2 with dissolve
        isa "Is peer pressure making you go?"
        scene ep9_diks_ph1_bella_library12b with dissolve
        ji "No, it's not like that. It also gives me a perfect reason to not attend High Society Halloween."
        scene ep9_diks_ph1_bella_library1 with dissolve
    isa "It will be good for you, Jill."
    isa "I frankly think you should have been going to these parties ages ago."
    scene ep9_diks_ph1_bella_library13b with dissolve
    ji "Really? Ages ago?"
    scene ep9_diks_ph1_bella_library1 with dissolve
    isa "You get my point."
    scene ep9_diks_ph1_bella_library13b with dissolve
    ji "Do you wanna come with us?"
    scene ep9_diks_ph1_bella_library2 with dissolve
    isa "It's kind of late for that question. I don't have anything to wear, and besides, I'd still say no if I had."
    isa "Back in college, I wouldn't have liked it if my teachers had come to our parties."
if branchJill:
    scene ep9_diks_ph1_bella_library10 with dissolve
else:
    scene ep9_diks_ph1_bella_library10b with dissolve
ji "Not even if they came to enjoy themselves?"
scene ep9_diks_ph1_bella_library2 with dissolve
isa "No. Definitely not. That'd have been even worse."
isa "No one wants to dance or get drunk with their teacher."
if branchJill:
    scene ep9_diks_ph1_bella_library13 with dissolve
else:
    scene ep9_diks_ph1_bella_library13b with dissolve
ji "Maybe that depends on the teacher?"
scene ep9_diks_ph1_bella_library1 with dissolve
isa "Well, perhaps..."
if branchJill:
    scene ep9_diks_ph1_bella_library13 with dissolve
else:
    scene ep9_diks_ph1_bella_library13b with dissolve
ji "Even so, you should stop by before you head back home. I'll meet you outside, and I can show you my costume."
if branchJill:
    ji "You'll either love it or hate it."
scene ep9_diks_ph1_bella_library1 with dissolve
if branchJill:
    isa "I'll do that. Have a nice evening and try not to fall."
else:
    isa "I'll do that. Have a nice evening."
if branchJill:
    scene ep9_diks_ph1_bella_library13 with dissolve
else:
    scene ep9_diks_ph1_bella_library13b with dissolve
if branchJill:
    ji "I'll try! Talk later."
else:
    ji "Talk later."
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track115.mp3"])
jump endEvent

label ep9_diks_ph1_sword_event_label:
scene ep9_diks_ph1_sword_event1 with dissolve
mc "(Oh, yeah! That's where I put it.)"
scene ep9_diks_ph1_sword_event2 with dissolve
mc "(It's a pretty flimsy sword.)"
mc "(But my costume is complete.)"
$ task_list[0] = ""
if persistent.mod_wtenabled:
    $ task_list[4] = "Talk to Tommy (Main Party Room)"
else:
    $ task_list[4] = "Talk to Tommy"
$ updateTaskList()
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

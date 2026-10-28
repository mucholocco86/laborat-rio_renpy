label ep11_freeroam_party_intro_label:
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep11/licensed_music/track176.mp3","music/ep11/licensed_music/track177.mp3","music/ep11/licensed_music/track178.mp3","music/ep11/licensed_music/track180.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track182.mp3"])
scene bg anim_party_intro_ep11 movie with dissolve
if persistent.seen_cutscene_ep11[0]:
    $ renpy.pause(55.27)
else:
    $ _skipping = False
    $ renpy.pause(55.27, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep11[0] = True

scene ep11_freeroam_party_intro1 with dissolve
le "Great idea for the party, [name]. I'm having a hard time not catching boners already."
scene ep11_freeroam_party_intro3 with dissolve
mc "Whose boner do you wanna catch?"
scene ep11_freeroam_party_intro2 with dissolve
le "You know what I mean."
le "A party with this much skin... It would be a miracle if you didn't get laid."
scene ep11_freeroam_party_intro3 with dissolve
mc "Isn't a miracle something good? Don't you want to get laid?"
scene ep11_freeroam_party_intro2 with dissolve
le "Stop it! You know what I mean. Man, I'm so excited. I can't decide who I'm gonna go for tonight."
scene ep11_freeroam_party_intro4 with dissolve
jac "How about Colonel Mustard over there?"
scene ep11_freeroam_party_intro5 with dissolve
"*{i}Laughter{/i}*"
le "What is she up to?"
scene ep11_freeroam_party_intro6 with dissolve
mc "I think she's trying to sell sex toys to the guests."
le "You know what? That's not a bad idea. Maybe I'll buy a whip from her."
scene ep11_freeroam_party_intro7 with dissolve
jac "You invited some hotties, [name]. Good job!"
scene ep11_freeroam_party_intro8 with dissolve
mc "I told people to invite friends and they got back to me with their names. I hope most of them are cool."
scene ep11_freeroam_party_intro2 with dissolve
le "I wonder what mission everyone has. That thing has started, right?"
scene ep11_freeroam_party_intro3 with dissolve
mc "Yeah, as soon as they enter the party, they get one. Derek's on bowl duty."
scene ep11_freeroam_party_intro9 with dissolve
mc "Derek!"
scene ep11_freeroam_party_intro10 with dissolve
de "Hey! You guys have grabbed one of these, right?"
scene ep11_freeroam_party_intro11 with dissolve
le "Not me."
scene ep11_freeroam_party_intro12 with dissolve
jac "Yep, I already did."
scene ep11_freeroam_party_intro13 with dissolve
de "What did you get?"
scene ep11_freeroam_party_intro12 with dissolve
jac "Grind on someone while dancing until I get hard. That should be easy enough..."
scene ep11_freeroam_party_intro14 with dissolve
le "Grab someone's dick? What the fuck is this?"
scene ep11_freeroam_party_intro15 with dissolve
de "Hey, no takebacks. Respect the bowl."
scene ep11_freeroam_party_intro16 with dissolve
le "I'm not doing this."
scene ep11_freeroam_party_intro15 with dissolve
de "Then you'll have to face the consequences at midnight."
scene ep11_freeroam_party_intro16 with dissolve
le "Stop fucking with me, and let me have a real one."
scene ep11_freeroam_party_intro17 with dissolve
mc "The consequences? What consequences?"
scene ep11_freeroam_party_intro18 with dissolve
de "It's meant to sound ominous, to motivate people to participate. But I haven't decided what the consequences are yet."
de "Did you take a mission?"
scene ep11_freeroam_party_intro17 with dissolve
mc "I don't even know what you guys wrote on these. Like, are they all lewd or...?"
scene ep11_freeroam_party_intro19 with dissolve
de "Most of them are quite daring, yeah."
scene ep11_freeroam_party_intro20 with dissolve
mc "Nope. I'm not sucking someone's cock tonight."
scene ep11_freeroam_party_intro21 with dissolve
de "What's up with all the takebacks!?"
scene ep11_freeroam_party_intro22 with dissolve
jac "You should have written give oral, to make it fit everyone."
scene ep11_freeroam_party_intro23 with dissolve
mc "Dress as Santa and make five girls sit in your lap. Ask them if they are naughty or nice and what they want for Christmas."
mc "Hm... Tell me how bad this one is compared to the rest so I know when to quit pulling missions."
scene ep11_freeroam_party_intro24 with dissolve
le "Jamie wrote that one with Tommy in mind. It's a good one."
scene ep11_freeroam_party_intro25 with dissolve
menu:
    "[m_c1]It's mine now":
        $ ep11_db_mission = True
        $ ep11_db_mission_progress = 0
        scene ep11_freeroam_party_intro26 with dissolve
        if branchAlone:
            mc "Well, it's mine now."
        else:
            mc "Well, it's mine now. It's harmless enough."
        scene ep11_freeroam_party_intro18 with dissolve
        de "It's gotta be five girls, or you'll face the consequences."
        $ new_bio("You", "I accepted the mission I pulled from The Dirty Bowl at the DIKs' Christmas Panty party.")
    "Save it for Tommy":
        $ ep11_db_mission = False
        scene ep11_freeroam_party_intro26 with dissolve
        mc "Save that one for him, then."
        mc "You know what? I'm gonna pass on the bowl. I'll be busy with the party as it is."
        scene ep11_freeroam_party_intro18 with dissolve
        de "Face the consequences, then."
        $ new_bio("You", "I rejected the mission I pulled from The Dirty Bowl at the DIKs' Christmas Panty party.")
scene ep11_freeroam_party_intro27 with dissolve
mc "Ohhh... I'm so scared."

jump ep11_freeroam_party_label

label ep11_pp_dildo_event_label:
scene ep11_pp_dildo_event1 with dissolve
ar "Changed your mind, did you?"
scene ep11_pp_dildo_event2 with dissolve
mc "About the sex toys... You wouldn't happen to have four dildos on you?"
scene ep11_pp_dildo_event3 with dissolve
ar "Say no more, [name]. Your pleasure is my business."
scene ep11_pp_dildo_event2 with dissolve
mc "They're not for me."
scene ep11_pp_dildo_event4 with dissolve
ar "I'm not judging. I would never judge. I once masturbated with a can of baked beans."
ar "It wasn't the best toy I've used, but also not the worst."
scene ep11_pp_dildo_event2 with dissolve
mc "The four dildos, do you have them?"
scene ep11_pp_dildo_event4 with dissolve
ar "I can get them for you. That will be $20 each. Let's call it an even $100."
scene ep11_pp_dildo_event2 with dissolve
mc "$100? For four?"
scene ep11_pp_dildo_event4 with dissolve
ar "$95. Final offer."
scene ep11_pp_dildo_event2 with dissolve
mc "I don't have that money on me. Can I borrow them for tonight? I'll get them back to you after - as good as new."
scene ep11_pp_dildo_event3 with dissolve
ar "Haha! Get a load of this guy."
ar "You can't return sex toys, [name]."
scene ep11_pp_dildo_event2 with dissolve
mc "We're having a Cucumber Sucking Competition soon, but the cucumbers we bought have perished."
mc "If you can lend us four dildos for tonight, we'd owe you one."
scene ep11_pp_dildo_event6 with dissolve
ar "A competition?"
scene ep11_pp_dildo_event5 with dissolve
mc "Yes. We're going to get girls to suck on those dildos in front of guys."
scene ep11_pp_dildo_event6 with dissolve
ar "Will everyone be watching?"
scene ep11_pp_dildo_event5 with dissolve
mc "Yeah, most will be watching, I'm sure."
scene ep11_pp_dildo_event3 with dissolve
ar "Well, why didn't you say so!?"
scene ep11_pp_dildo_event2 with dissolve
mc "Will you help out?"
scene ep11_pp_dildo_event3 with dissolve
ar "I will! But only if you tell everyone where you got the dildos from. Advertise my services so that everyone wants to buy from me afterward."
scene ep11_pp_dildo_event2 with dissolve
mc "So, you'd be a sponsor of sorts?"
scene ep11_pp_dildo_event4 with dissolve
ar "Honestly, I'm not selling a lot at the party so far. This is a golden opportunity for me."
scene ep11_pp_dildo_event2 with dissolve
mc "Let's do it. Are the dildos good for this purpose?"
scene ep11_pp_dildo_event4 with dissolve
ar "Trust me, they almost look like the real thing."
scene ep11_pp_dildo_event2 with dissolve
mc "Awesome! You just saved the party. Have them ready in a few, ok?"
scene ep11_pp_dildo_event3 with dissolve
ar "Aye, aye! Don't forget to hype my toys up!"
$ event_list.append("ep11_pp_d_start_event_label")
$ task_list[5] = ""
$ updateTaskList()
$ new_bio("Arieth", "Arieth helped me out with dildos for the competition at the DIKs' Christmas Panty party.")
jump endEvent

label ep11_pp_arieth_event_label:
$ guideSuggestedPage = 199
scene ep11_pp_arieth_event3 with dissolve
ar "Oh, you name it, I've got it! Butt plugs, condoms, vibrators, dildos, outfits, lube..."
ar "Everything you need to turn this night into a fun and sexy one."
scene ep11_pp_arieth_event4 with dissolve
guy "Did you bring all of that here?"
scene ep11_pp_arieth_event3 with dissolve
ar "You bet! I've got more stashed away by the front door."
scene ep11_pp_arieth_event5 with dissolve
ar "Oh, [name]! Just the guy I wanted to talk to. Give me a minute."
scene ep11_pp_dildo_event2 with dissolve
mc "I'm not buying anything. I'm all set on butt plugs, thanks."
scene ep11_pp_dildo_event4 with dissolve
ar "A guy like you, I bet you are."
scene ep11_pp_dildo_event2 with dissolve
mc "I was joking. I don't own any butt plugs."
scene ep11_pp_dildo_event4 with dissolve
ar "This isn't about your butt plugs. I have a business proposition for you."
scene ep11_pp_dildo_event2 with dissolve
mc "Thanks for considering me, but I don't want to sell sex toys."
scene ep11_pp_dildo_event4 with dissolve
ar "That's not what I'm proposing. Hear me out..."
ar "I've been looking for a guy who's hung like a horse, and word of mouth tells me that's you!"
scene ep11_pp_dildo_event2 with dissolve
mc "People say all kinds of things."
scene ep11_pp_arieth_event1 with dissolve
ar "Don't be modest. I saw the posters too. You're huge!"
scene ep11_pp_dildo_event2 with dissolve
menu:
    "I don't want to talk about this":
        mc "This is not a conversation I want to have."
    "So what?":
        mc "Yeah, so what?"
scene ep11_pp_arieth_event1 with dissolve
ar "I have these dick-cloning sets that aren't selling well. But I could sell a cloned rocket for a lot of money if I used a kit on you."
ar "Telling girls they could pleasure themselves with the legendary dick of a DIK would make me a fortune."
scene ep11_pp_dildo_event2 with dissolve
mc "You want to sell people my cock?"
scene ep11_pp_dildo_event3 with dissolve
ar "Not your cock, dummy. A rubber version of it. Like, a dildo that has the same size and details as your dick."
ar "It would be 100%% authentic. Every vein and wart would be seen on it."
ar "I'm telling you, I could easily sell it for $100. Any profit I make, I'd split with you. What do you say?"
scene ep11_pp_dildo_event2 with dissolve
mc "I say I don't need another reason for my dick to be spread around on campus. Enough is enough."
scene ep11_pp_arieth_event2 with dissolve
ar "Huh? I did not expect that from you."
$ new_bio("Arieth", "Arieth suggested using my cock for her dick-cloning sets.")
$ optional_task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_rusty_event_label:
scene ep11_pp_rusty_event1 with dissolve
mc "(Seems like they've made their choice. I'll have to be cool with it.)"
mc "(Knowing how much he likes her, it would suck to see him fall for someone who's in a relationship. Perhaps he already did?)"
scene ep11_pp_rusty_event2 with dissolve
rs "Hey! [name]! Dance with us!"
scene ep11_pp_rusty_event3 with dissolve
mc "I'm good, thanks. Too sober."
scene ep11_pp_rusty_event2 with dissolve
rs "Let's fix that then."
scene ep11_pp_rusty_event4 with dissolve
rs "I'll be back in a bit."
scene ep11_pp_rusty_event5 with dissolve
if (minigames and pp_current_party_happiness[6] > 2) or (not minigames and pp_current_party_happiness[6] == 1):
    rs "You've outdone yourself with the party, [name]."
elif (minigames and pp_current_party_happiness[6] > 1) or (not minigames and pp_current_party_happiness[6] == 0):
    rs "Nice party, [name]. It's great!"
else:
    rs "Good effort with the party, [name]."
scene ep11_pp_rusty_event6 with dissolve
mc "It was hard doing it alone."
scene ep11_pp_rusty_event7 with dissolve
rs "I should have helped out more. I...uh..."
rs "It's not your responsibility to do these things as a freshman, yet you are."
scene ep11_pp_rusty_event5 with dissolve
rs "Once again, our frat is tested, and you're trying to keep it together."
scene ep11_pp_rusty_event6 with dissolve
mc "I can't take all the credit. Derek did a lot, too."
scene ep11_pp_rusty_event5 with dissolve
rs "Yeah. We can always count on Derek, can't we?"
scene ep11_pp_rusty_event8 with dissolve
rs "Look... Sorry for being an ass lately. I haven't felt too good about myself."
rs "And I've missed your friendship."
scene ep11_pp_rusty_event9 with dissolve
mc "That's what annoyed me the most. You distanced yourself from me when you should have done the opposite."
mc "Especially after what Nick said. It made me feel horrible."
scene ep11_pp_rusty_event8 with dissolve
rs "I didn't realize it hit you that hard. I'm sorry. I thought those comments would roll right off you."
scene ep11_pp_rusty_event9 with dissolve
mc "They didn't. They stuck with me. But I'll be fine."
scene ep11_pp_rusty_event8 with dissolve
rs "It's not been easy for either of us. Nick has been a close friend of mine, and now he's gone."
rs "I've told him to cool down and talk to us again, but he's hurt too. He claims he didn't have anything to do with the cluck or the pictures."
scene ep11_pp_rusty_event9 with dissolve
mc "I haven't found anything to clear his name, but I've talked to Chad about the letters they claimed I sent."
scene ep11_pp_rusty_event10 with dissolve
rs "And...?"
scene ep11_pp_rusty_event9 with dissolve
mc "It was a misunderstanding, but he still blames us. And just like I knew, it was someone else sending the letters, but I'm no closer to figuring out who."
scene ep11_pp_rusty_event10 with dissolve
rs "I'm out of ideas..."
scene ep11_pp_rusty_event9 with dissolve
mc "Regarding Nick... I wanted to ask you something."
mc "He said something along the lines of Tommy stealing money from the treasury...and that you were cool with it."
mc "What was that about?"
scene ep11_pp_rusty_event11 with dissolve
rs "Tommy needed money and I lent him some from the treasury. Nick must have misunderstood why Tommy took money from the safe."
scene ep11_pp_rusty_event9 with dissolve
mc "But...you never told me that. When I noticed the budget was off, you didn't mention any loans. Why did you keep it a secret from me?"
scene ep11_pp_rusty_event11 with dissolve
rs "I told you to talk to Tommy about it."
scene ep11_pp_rusty_event9 with dissolve
mc "Yeah, but why couldn't you tell me?"
scene ep11_pp_rusty_event11 with dissolve
rs "Because of the DIKs' secret code."
scene ep11_pp_rusty_event9 with dissolve
mc "Oh?"
scene ep11_pp_rusty_event10 with dissolve
rs "Again... Talk to Tommy."
if ep9_heather_lewd == 2:
    scene ep11_pp_rusty_event9 with dissolve
    mc "We're not buddy-buddy at the moment."
    scene ep11_pp_rusty_event10 with dissolve
    rs "Make an effort with him. Maybe you can be again."
scene ep11_pp_rusty_event15 with dissolve
mic "Rusty! This is the song I was talking about! Come and dance with me!"
scene ep11_pp_rusty_event12 with dissolve
mc "Go dance with her."
scene ep11_pp_rusty_event13 with dissolve
rs "Are you sure?"
scene ep11_pp_rusty_event12 with dissolve
mc "Yeah, I don't want you to spend all night in underwear talking to me. What a waste of a party."
scene ep11_pp_rusty_event14 with dissolve
$ renpy.pause()
$ new_bio("Tommy", "Rusty told me Tommy borrowed money from the DIKs' treasury and that it was related to the DIKs' secret code.")
$ new_bio("Rusty", "Rusty told me Tommy borrowed money from the DIKs' treasury and that it was related to the DIKs' secret code.")
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_elena_event_label:
scene ep11_pp_elena_event1 with dissolve
el "Would you be ok with it?"
scene ep11_pp_elena_event2 with dissolve
jb "It depends on who it is, and you'd have to be ok with that, too."
scene ep11_pp_elena_event3 with dissolve
mc "Hey, guys. What are we drinking?"
scene ep11_pp_elena_event4 with dissolve
el "I'm drinking the \"egg\" nog. I have no clue what Derek put in it, but it's pretty damned good."
scene ep11_pp_elena_event5 with dissolve
mc "Inventive as always."
jb "The Naughty drink is great, [name]. You should ask him to make one for you."
scene ep11_pp_elena_event6 with dissolve
mc "Nah, he's busy out there tonight. I'm getting a beer."
scene ep11_pp_elena_event7 with dissolve
el "[name]. You're not 'X', are you?"
play sound "sound_effects/bottle_open.mp3"
scene ep11_pp_elena_event8 with dissolve
mc "X? What do you mean?"
scene ep11_pp_elena_event9 with dissolve
el "Have a look at this."
scene ep11_pp_elena_event10 with dissolve
mc "\"You are 'Y'. Find 'X' and have sex.\""
mc "Oof. Haha! I wouldn't want to be stuck with this mission."
scene ep11_pp_elena_event11 with dissolve
el "It's exciting, though, isn't it?"
scene ep11_pp_elena_event12 with dissolve
mc "It could be good, but it could also be horrendous."
mc "Or maybe it's a dud. What if no one pulled the other end of that mission?"
scene ep11_pp_elena_event11 with dissolve
el "If you find out, let us know."
scene ep11_pp_elena_event12 with dissolve
mc "Haha, ok. If you guys are up for it, I'll let 'X' know."

$ event_list.append("ep11_pp_leon_event_label")
$ task_list[2] = ""
$ optional_task_list[1] = "Find out who X is"
$ updateTaskList()
jump endEvent

label ep11_pp_tommy_event_label:
scene ep11_pp_tommy_event1 with dissolve
tm "Nipple tape? Hm... That doesn't classify as underwear to me."
gi "No?"
scene ep11_pp_tommy_event2 with dissolve
tm "No. You have to take it off."
scene ep11_pp_tommy_event3 with dissolve
gi "And play right into your hand?"
scene ep11_pp_tommy_event2 with dissolve
tm "It's the rules of the party, baby."
scene ep11_pp_tommy_event4 with dissolve
mc "(It looks like he's enjoying himself. That's good.)"
if ep9_heather_lewd == 2:
    scene ep11_pp_tommy_event5 with dissolve
    $ renpy.pause()
    scene ep11_pp_tommy_event6 with dissolve
    tm "[name]!"
    scene ep11_pp_tommy_event7 with dissolve
    mc "Yeah?"
else:
    scene ep11_pp_tommy_event6 with dissolve
    if branchMayaJosy:
        tm "Sisterfucker!"
    else:
        tm "[name]!"
    scene ep11_pp_tommy_event7 with dissolve
    if branchMayaJosy:
        mc "*{i}Sigh{/i}* Yeah?"
    else:
        mc "Yeah?"
scene ep11_pp_tommy_event8 with dissolve
tm "Gina's nipple tape. Is that underwear or not?"
scene ep11_pp_tommy_event7 with dissolve
mc "(I can tell what he wants me to say... I'll play along.)"
scene ep11_pp_tommy_event9 with dissolve
mc "Nope. Underwear is panties, bras and lingerie. Nipple tape? That's like censoring. And we know how bad that is."
scene ep11_pp_tommy_event10 with dissolve
tm "Exactly, Gina! You're like a walking piece of Japanese porn, only that it's your tits that are blurred."
tm "You gotta do it... Free the nipple."
scene ep11_pp_tommy_event9 with dissolve
mc "It's Christmas, after all."
play sound "sound_effects/season3/tape.mp3"
scene ep11_pp_tommy_event11 with dissolve
gi "This party better be worth it."
scene ep11_pp_tommy_event12 with dissolve
tm "That's what I'm talking about."
scene ep11_pp_tommy_event13 with dissolve
tm "Now, let's see what we can do about your Dirty Bowl mission."
scene ep11_pp_tommy_event14 with dissolve
gi "Let's do it."
scene ep11_pp_tommy_event15 with dissolve
if ep9_heather_lewd == 2:
    mc "(He talked to me again... That's a good sign.)"
mc "(I'd say him hooking up with chicks after breaking up with Heather was a sign of moving on...)"
mc "(...but he did that while they were together, too, so I don't know what's going on with him.)"
$ new_bio("Tommy", "Tommy tried to hook up with Gina at the DIKs' Christmas Panty party. It looked like he was trying to move on from Heather.")
$ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_sally_event_label:
$ guideSuggestedPage = 198
scene ep11_pp_sally_event1 with dissolve
sy "No, I think they also had a party like this last year. And, I'll say it, it sounds way worse than what it is."
scene ep11_pp_sally_event3 with dissolve
cla "It is silly, but at least everyone is doing it."
scene ep11_pp_sally_event2 with dissolve
sy "Yeah, and if you think about it, guys have it way worse than girls tonight."
scene ep11_pp_sally_event4 with dissolve
mc "What makes you say that?"
scene ep11_pp_sally_event5 with dissolve
sy "Isn't it obvious? I've seen at least three of you guys pitching tents already."
scene ep11_pp_sally_event8 with dissolve
cla "Hahaha! Totally!"
scene ep11_pp_sally_event6 with dissolve
mc "They're just happy that you girls came. I am too, but I won't pitch a tent to show it."
scene ep11_pp_sally_event7 with dissolve
sy "Ugh. You're the worst."
scene ep11_pp_sally_event13 with dissolve
mc "You don't look too comfortable there, Karen. Are you all right?"
scene ep11_pp_sally_event14 with dissolve
ka "I was on the fence and Sally forced me to come."
scene ep11_pp_sally_event13 with dissolve
mc "No one's forcing anyone to do anything tonight. We have the dress code and that's it."
scene ep11_pp_sally_event7 with dissolve
sy "Oh, yeah? What about that bowl game? We refused to take a piece of paper from it, and Derek said we'd be punished by midnight."
scene ep11_pp_sally_event17 with dissolve
mc "That one is just for fun. You should join in!"
scene ep11_pp_sally_event9 with dissolve
cla "Mine said to flash my tits to three guys."
scene ep11_pp_sally_event10 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]  

menu:
    "Sounds fun \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "That sounds fun to me!"
        scene ep11_pp_sally_event16 with dissolve
        sy "The worst, I tell you. The worst."
    "You don't have to do it \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "You don't have to do it unless you want to."
        mc "Honestly, I doubt that most will do their mission tonight. But we'll see."
    "Just three? \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Just three? You got off easy. I've seen worse missions than that."
        scene ep11_pp_sally_event16 with dissolve
        sy "The worst, I tell you. The worst."
scene ep11_pp_sally_event6 with dissolve
mc "My point is: have fun and relax. No one is judging anyone here tonight."
menu:
    "Boost Karen":
        scene ep11_pp_sally_event15 with dissolve
        if affinity == "DIK":
            mc "You look sexy tonight, Karen. You sure know how to rock those underwear."
        else:
            $ dk(-1)
            mc "You look pretty tonight, Karen. Drink and loosen up."
    "Ask if she wants a mask":
        scene ep11_pp_sally_event13 with dissolve
        mc "If you want a mask to help you relax, I can get one for you."
        scene ep11_pp_sally_event14 with dissolve
        ka "I can't see well without my glasses, and the mask won't fit with them."
scene ep11_pp_sally_event9 with dissolve
cla "Hey, [name]?"
scene ep11_pp_sally_event10 with dissolve
mc "Yeah?"
$ guideSuggestedPage = 199
scene ep11_pp_sally_event11 with dissolve
cla "You're number one now!"
scene ep11_pp_sally_event12 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]  

menu:
    "Only two more to go":
        mc "Oh, awesome! Only two more to go. You can do it."
        scene ep11_pp_sally_event11 with dissolve
        cla "Hahaha!"
    "Flirt":
        if affinity == "DIK":
            mc "Those are some nice tits. I can be number two and three if you want."
        else:
            mc "Nice! What an honor. Haha, I wasn't expecting that."
        scene ep11_pp_sally_event11 with dissolve
        cla "Hahaha!"
    "Taunt her ({color=#ffffff}{size=-[persistent.scale_factor]}{font=fonts/collegiate.ttf}DIK{/font}{/size} affinity{/color})\n{size=-4}[m_c1][mod_choices[3]]" if affinity == "DIK":
        $ dk(1)
        scene ep11_pp_sally_event12c with dissolve
        mc "Ahh! My eyes! My eyes!"
        scene ep11_pp_sally_event12b with dissolve
        cla "You asshole..."

$ new_bio("Sally", "Sally showed up at the DIKs' Christmas Panty party despite hesitating when I asked her.")
$ task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_derek_event_label:
scene ep11_pp_derek_event1 with dissolve
de "*{i}Cough cough{/i}* Melanie..."
scene ep11_pp_derek_event3 with dissolve
ml "Yeah?"
scene ep11_pp_derek_event2 with dissolve
de "You haven't taken a mission from the bowl yet. Don't think I haven't noticed."
scene ep11_pp_derek_event3 with dissolve
ml "Fine. I'll take one for the team."
scene ep11_pp_derek_event2 with dissolve
de "Yeah, you might have to."
scene ep11_pp_derek_event4 with dissolve
ml "Hm?"
scene ep11_pp_derek_event5 with dissolve
de "Enjoy your mission. You have until midnight or you'll face the consequences."
if ep11_mel_lewd:
    scene ep11_pp_derek_event6b with dissolve
else:
    scene ep11_pp_derek_event6 with dissolve
mc "You're keeping a tight ship around here tonight, Derek."
scene ep11_pp_derek_event7 with dissolve
de "It's easy math, [mc_de]. The more girls that grab a mission, the higher the chances are to get laid."
scene ep11_pp_derek_event8 with dissolve
mc "And here I thought you didn't pay attention in math class."
mc "Thanks for helping out with everything. It means a lot to me."
scene ep11_pp_derek_event9 with dissolve
de "I didn't want you to go at it alone. Sometimes, you gotta be proactive. You can't go around waiting for others to step up."
scene ep11_pp_derek_event8 with dissolve
mc "It's not just tonight, though. Don't think I haven't noticed you pull your weight and more around here."
scene ep11_pp_derek_event10 with dissolve
de "After Nick left, I obviously had to step up more. Things can change in an instant."
de "A wise man once said you should be the change you wanna see in the world. And I intend to be just that."
scene ep11_pp_derek_event11 with dissolve
de "So, I'll help out and be as loyal as I can to us."
de "Also, I wanna get laid more, so I'll try to put out more."
scene ep11_pp_derek_event12 with dissolve
mc "Haha, that's good!"
mc "How is dating life for you these days?"
scene ep11_pp_derek_event11 with dissolve
de "Like eating a buffet."
scene ep11_pp_derek_event12 with dissolve
mc "Awesome."
scene ep11_pp_derek_event13 with dissolve
de "Only that it's day two of the buffet and I'm eating everyone's cold scraps."
scene ep11_pp_derek_event14 with dissolve
mc "Hahaha! Come on, it can't be that bad."
scene ep11_pp_derek_event15 with dissolve
de "But I'll keep handing out these missions until guests stop showing. Tonight might be a good night. I have a feeling."

if ep11_pp_contest == 0 or ep11_pp_contest == 1:
    scene ep11_pp_derek_event16 with dissolve
    mc "Is everything set for the competition?"
    if ep11_pp_contest == 0:
        scene ep11_pp_derek_event17 with dissolve
        de "Yep. I've got T-shirts, beers, towels and a mop good to go."
        scene ep11_pp_derek_event16 with dissolve
        mc "What about the microphone and speaker?"
        scene ep11_pp_derek_event17 with dissolve
        de "I've got that, too. When do you wanna do it? Soon, yeah?"
        scene ep11_pp_derek_event16 with dissolve
        mc "Yeah. Let me check a few things first."
        scene ep11_pp_derek_event17 with dissolve
        de "No rush. When you're ready, I'll fetch the things and we can start the show."
        $ task_list[5] = ""
        $ event_list.append("ep11_pp_d_start_event_label")
    elif ep11_pp_contest == 1:
        scene ep11_pp_derek_event18 with dissolve
        de "About that... I'm not too sure about the cucumbers. When I bought them, they were hard, but they went soft, and I believe someone ate one for lunch."
        de "I'm not too sure girls wanna suck on a soggy cucumber... Should we abort?"
        scene ep11_pp_derek_event16 with dissolve
        mc "We can't abort! It's one of the highlights of the night."
        scene ep11_pp_derek_event18 with dissolve
        de "Unless you have a good substitute for the cucumbers, we can't do it."
        de "And don't say we'll do live blowjobs instead. Trust me, girls wouldn't sign up for that."
        scene ep11_pp_derek_event16 with dissolve
        mc "Well, duh..."
        mc "I'll figure something out. Don't abort yet. Get the microphone and chairs in place."
        scene ep11_pp_derek_event19 with dissolve
        mc "(Hm... What can I use instead of cucumbers?)"
        $ task_list[5] = "Replace the cucumbers with something"
        $ event_list.append("ep11_pp_dildo_event_label")
else:
    $ task_list[5] = ""
    $ event_list.append("ep11_pp_d_start_event_label")
$ updateTaskList()
jump endEvent

label ep11_pp_d_start_event_label:
if ep11_pp_contest == 0 or ep11_pp_contest == 1:
    scene ep11_pp_derek_event17 with dissolve
    de "Are we ready to start the competition?"
else:
    menu:
        "Pass some time?"
        "Yes":
            $ renpy.block_rollback()
            if minigames:
                $ pp_happiness_level[0] = max(pp_happiness_level[0]-2,0)
                $ pp_happiness_level[1] = max(pp_happiness_level[1]-2,0)
                $ pp_happiness_level[2] = max(pp_happiness_level[2]-2,0)
                $ pp_happiness_level[3] = max(pp_happiness_level[3]-2,0)
                $ pp_happiness_level[4] = max(pp_happiness_level[4]-2,0)
                $ pp_happiness_level[5] = max(pp_happiness_level[5]-2,0)
                $ pp_happiness_level[6] = max(pp_happiness_level[6]-2,0)
                $ pp_happiness_level[7] = max(pp_happiness_level[7]-2,0)
                $ mphone_pp_history_list.append("• The lack of activity decreased Derek's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased Jacob's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased Jamie's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased John Boy's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased Leon's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased [name]'s happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased Rusty's happiness by {color=ff0000}-2%{/color}.")
                $ mphone_pp_history_list.append("• The lack of activity decreased Tommy's happiness by {color=ff0000}-2%{/color}.")
            jump ep11_freeroam_party_pr_label
        "Not yet":
            $ event_list.append("ep11_pp_d_start_event_label")
            jump endEvent

scene ep11_pp_derek_event16 with dissolve
menu:
    "Yes":
        mc "Yes. We're ready."
    "Not yet":
        label ep11_pp_d_start_eventb_label:
        mc "Not yet. I need more time."
        $ event_list.append("ep11_pp_d_start_event_label")
        jump endEvent

if ep11_pp_contest == 1:
    scene ep11_pp_derek_event17 with dissolve
    de "So, what's the replacement?"
    scene ep11_pp_derek_event16 with dissolve
    mc "Arieth is providing us with dildos as long as we advertise that she's selling sex toys at the party."
    scene ep11_pp_derek_event20 with dissolve
    de "Dildos? Now, why the hell did you choose cucumbers instead of dildos to begin with?"
    scene ep11_pp_derek_event16 with dissolve
    mc "It doesn't matter. What matters is that we have a competition."

scene ep11_pp_derek_event20 with dissolve
de "Awesome, let's spread the word that it's starting."
jump ep11_freeroam_party_pr_label

label ep11_pp_girls_event_label:
scene ep11_pp_girls_event1 with dissolve
girl "Thanks for the invite, [name]. The party is bitching."
scene ep11_pp_girls_event2 with dissolve
mc "I have no clue who you girls are, but you're welcome."
scene ep11_pp_girls_event5 with dissolve
girl "For real? We were at the Halloween party."
scene ep11_pp_girls_event7 with dissolve
girl3 "I wasn't."
scene ep11_pp_girls_event8 with dissolve
girl2 "You weren't?"
scene ep11_pp_girls_event2 with dissolve
mc "See, it's not easy to tell, especially not with and without costumes."
scene ep11_pp_girls_event5 with dissolve
fel "I'm Felicia. I'm in the same classes as Jacob and I've been to many parties with you guys."
scene ep11_pp_girls_event6 with dissolve
cha "Charlotte. Elena invited me."
scene ep11_pp_girls_event7 with dissolve
lea "I'm Leanne. I came with these girls. Thanks for extending the invites."
scene ep11_pp_girls_event2 with dissolve
mc "No problem. I'm [name]."
scene ep11_pp_girls_event3 with dissolve
fel "Haha, yeah. We already know who you are."
scene ep11_pp_girls_event4 with dissolve
lea "I don't."
if not ep8_recital_failed:
    scene ep11_pp_girls_event9 with dissolve
    lea "No wait! I do. Now I recognize you."
    scene ep11_pp_girls_event10 with dissolve
    mc "Look, I know that poster is out there, but can we at least pretend it's not?"
    scene ep11_pp_girls_event11 with dissolve
    lea "What poster? I recognize you from that video. You're so good at playing guitar; it's nuts."
    scene ep11_pp_girls_event10 with dissolve
    mc "Oh... Crap."
scene ep11_pp_girls_event12 with dissolve
fel "*{i}Whispers{/i}*"
scene ep11_pp_girls_event13 with dissolve
lea "Ohhh... That's him?"
scene ep11_pp_girls_event14 with dissolve
lea "Well, hell-oooo."
fel "Hahaha!"
scene ep11_pp_girls_event15 with dissolve
lea "I can tell from those boxers it's true."
scene ep11_pp_girls_event16 with dissolve
mc "*{i}Sigh{/i}* Enjoy the party."
scene ep11_pp_girls_event17 with dissolve
lea "[name], wait! It's not bad to have a big cock."
"*{i}Laughter{/i}*"
$ task_list[11] = ""
$ updateTaskList()
$ event_list.append("ep11_pp_mt_event_label")
jump endEvent

label ep11_pp_mt_event_label:
$ guideSuggestedPage = 200
scene ep11_pp_mt_event1 with dissolve
fel "Mistletoe! You gotta kiss me!"
scene ep11_pp_mt_event2 with dissolve
fel "Don't give me that look - mistletoe rules and I'm not the one who put it up there."
scene ep11_pp_mt_event3 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                          $ mod_choices[6]="(+3 Cheater)"
                          $ mod_choices[7]="(+2 Cheater)"

menu:
    "Kiss her":
        scene ep11_pp_mt_event7 with dissolve
        mc "*{i}Smack{/i}*"
        scene ep11_pp_mt_event8 with dissolve
        fel "Hey, that was way too short of a kiss! Give me a real one."
        $ guideSuggestedPage = 201
        if (ep11_maya_love > 0 or ep11_josy_love > 0) and wt_ep9_branch_numbers == 1:
            jump ep11_pp_mt_eventb_label
        scene ep11_pp_mt_event9 with dissolve
        menu:
            "Give her a real one \n{size=-4}[m_c1][mod_choices[6]]":
                #$ ep11_girl_drink_opportunity = False
                $ ep11_mistletoe = 1
                if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                    $ tc += 3
                scene ep11_pp_mt_event10 with dissolve
                fel "*{i}Smack{/i}*"
                scene ep11_pp_mt_event11 with dissolve
                $ renpy.pause()
                scene ep11_pp_mt_event12 with dissolve
                $ renpy.pause()
                scene ep11_pp_mt_event13 with dissolve
                lea "Wooo!!! Look at Felicia! Haha!"
                scene ep11_pp_mt_event14 with dissolve
                $ renpy.pause()
                scene ep11_pp_mt_event15 with dissolve
                fel "Now, that's what I'm talking about!"
                scene ep11_pp_mt_event16 with dissolve
                lea "Mistletoe!"
                scene ep11_pp_mt_event17 with dissolve
                fel "Hahaha!"
                scene ep11_pp_mt_event18 with dissolve
                lea "*{i}Smack{/i}*"
                scene ep11_pp_mt_event19 with dissolve
                $ renpy.pause()
                scene ep11_pp_mt_event20 with dissolve
                $ renpy.pause()
                scene ep11_pp_mt_event21 with dissolve
                menu:
                    "Anyone else? \n{size=-4}[m_c1][mod_choices[7]][m_c2][mod_choices[3]]":
                        $ dk(1)
                        $ ep11_mistletoe = 2
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                            $ tc += 2
                        scene ep11_pp_mt_event22 with dissolve
                        mc "Anyone else, while I'm standing here?"
                        scene ep11_pp_mt_event23 with dissolve
                        cha "Yeah, what the hell?"
                        scene ep11_pp_mt_event24 with dissolve
                        cha "*{i}Smack{/i}*"
                        scene ep11_pp_mt_event25 with dissolve
                        $ renpy.pause()
                        scene ep11_pp_mt_event26 with dissolve
                        sar "Watch out for herpes, [name]."
                        scene ep11_pp_mt_event27 with dissolve
                        mc "Why do you have to ruin the fun? Get over here instead."
                    "Leave":
                        scene ep11_pp_mt_event22 with dissolve
                        mc "Ok, that's enough for me. Haha!"
            "Don't kiss her":
                label ep11_pp_mt_eventb_label:
                scene ep11_pp_mt_event4 with dissolve
                mc "Nah, that's all you get from me."
                scene ep11_pp_mt_event5 with dissolve
                fel "Why are you so boring, [name]? I thought you were a DIK."
    "Don't kiss her \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep11_pp_mt_event4 with dissolve
        mc "I don't think so."
        scene ep11_pp_mt_event5 with dissolve
        fel "Why are you so boring, [name]? I thought you were a DIK."
        scene ep11_pp_mt_event6 with dissolve
        mc "I don't kiss everyone that offers. But evidently, you do. So, go ahead and wait underneath that mistletoe for someone else."
$ map_fast_travel_enabled = True
$ currentFreeRoamLabel = "ep11_diks_pp_ua_label"
$ map_fast_travel_enabled = True
jump endEvent

label ep11_pp_chen_event_label:
$ guideSuggestedPage = 199
scene ep11_pp_chen_event1 with dissolve
che "Yeah, I wear these to bed. So what? You got a problem with fire?"
che "My dick is fire, and so is my underwear."
scene ep11_pp_chen_event2 with dissolve
girl "And what about the shades?"
scene ep11_pp_chen_event3 with dissolve
che "Shit's cash! And I've got cash. Mad cash."
che "Don't like them? That's your problem."
scene ep11_pp_chen_event4 with dissolve
menu:
    "Not every party is a costume party":
        mc "Chen, didn't someone tell you that not every party is a costume party?"
        scene ep11_pp_chen_event5 with dissolve
        girl "Hahaha!"
        scene ep11_pp_chen_event6 with dissolve
        che "Fuck you! This is not a costume! This is how I roll."
    "You're on fire":
        mc "Chen, I think you're standing too close to the fireplace; your underwear caught on fire."
        scene ep11_pp_chen_event6 with dissolve
che "I don't diss you or your orange boxers; don't diss my drip."
scene ep11_pp_chen_event7 with dissolve
che "As I was saying... I'm starting a threesome later; I'm looking for two girls to join."
scene ep11_pp_chen_event10 with dissolve
mc "That's the mission you got?"
scene ep11_pp_chen_event9 with dissolve
che "What fucking mission?"
scene ep11_pp_chen_event8 with dissolve
girl "It's a pass for us, but good luck with your hunt."
scene ep11_pp_chen_event7 with dissolve
che "Don't say no like that. At least hear me out."
scene ep11_pp_chen_event10 with dissolve
mc "A no is a no, Chen. Move on."
scene ep11_pp_chen_event11 with dissolve
che "Bah!"
scene ep11_pp_chen_event12 with dissolve
girl "Thanks."
scene ep11_pp_chen_event13 with dissolve
menu:
    "[m_c1]Get her a drink":
        mc "No problem. Can I get you something to drink?"
        scene ep11_pp_chen_event15 with dissolve
        girl "You don't have to do that. I can get it myself."
        scene ep11_pp_chen_event14 with dissolve
        mc "What kind of host would I be if I let a guest go thirsty? Let me get you some punch from downstairs."
        if persistent.mod_wtenabled:
            $ optional_task_list[2] = "Get the girl a drink (Right Hallway - table)"
        else:
            $ optional_task_list[2] = "Get the girl a drink"
        $ event_list.append("ep11_pp_drink1_event_label")
    "Leave":
        mc "No problem. Enjoy the party!"
        $ optional_task_list[2] = ""
        $ event_list.append("ep11_pp_drink_skip_event_label")

$ updateTaskList()
jump endEvent

label ep11_pp_drink2_event_label:
$ guideSuggestedPage = 200
scene ep11_pp_drink2_event1 with dissolve
mc "Here you go. I have no clue what Derek put in this, but it's pretty good."
scene ep11_pp_drink2_event2 with dissolve
girl "Thank you so much. You didn't have to."
scene ep11_pp_drink2_event3 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        

menu:
    "Naughty joke \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Now that I have your attention..."
        mc "I'm starting a threesome later; I'm looking for two girls to join."
        scene ep11_pp_drink2_event4 with dissolve
        girl "Hahaha! Not you, too!"
        scene ep11_pp_drink2_event3 with dissolve
        mc "Just kidding. Enjoy the party!"
    "You're welcome \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "You're welcome. Enjoy the party!"

$ map_fast_travel_enabled = False
$ optional_task_list[2] = ""
$ updateTaskList()
$ ep11_girl_drink_opportunity = True
jump endEvent

label ep11_pp_ashley_event_label:
$ guideSuggestedPage = 200
scene ep11_pp_ashley_event1 with dissolve
sar "It's simple: choose neither and sleep with both."
scene ep11_pp_ashley_event3 with dissolve
ash "That's your advice? You're terrible at this."
scene ep11_pp_ashley_event2 with dissolve
sar "No. Relationships are terrible, and guys have the right idea about them."
scene ep11_pp_ashley_event3 with dissolve
ash "And what idea is that?"
scene ep11_pp_ashley_event2 with dissolve
sar "That you can always score someone better, so there's no point in settling down."
scene ep11_pp_ashley_event4 with dissolve
ash "Not every guy is like that."
scene ep11_pp_ashley_event2 with dissolve
sar "Every hot guy is. Who wants to bother with the rest of them?"
scene ep11_pp_ashley_event4 with dissolve
ash "Nuh-uh. You're wrong and that's shallow."
scene ep11_pp_ashley_event5 with dissolve
sar "[name]! Can you settle the score for us?"
sar "No matter who you're with, isn't there always a hotter chick out there?"
scene ep11_pp_ashley_event6 with dissolve
menu:
    "Agree":
        mc "Very few in the world can say they are the best at something. There's always someone better out there."
        mc "Why would it be different with hotness?"
        scene ep11_pp_ashley_event7 with dissolve
        mc "But that doesn't mean the girl you're with isn't hot."
        scene ep11_pp_ashley_event9 with dissolve
        sar "Exactly! But the grass is always greener on the other side."
    "Disagree":
        mc "Nah. I figure when you're in a relationship with someone you're into, they'll be the hottest girl for you."
        scene ep11_pp_ashley_event8 with dissolve
        sar "That's called denial, [name]. It's something guys would say not to hurt the feelings of their girl. And it's total BS."
    "See both sides of it":
        mc "Sure, I think that goes for everyone and everything. Just like there's someone better than you at everything you can do, there is someone hotter than you, too."
        mc "But I'd like to think that you're not looking at those people when you're in a good relationship."
        scene ep11_pp_ashley_event8 with dissolve
        sar "That's called settling for something."
        scene ep11_pp_ashley_event7 with dissolve
        mc "That's an odd way to look at relationships."

scene ep11_pp_ashley_event10 with dissolve
ash "Whatever, guys. This doesn't help."
scene ep11_pp_ashley_event11 with dissolve
mc "Help with what?"
scene ep11_pp_ashley_event10 with dissolve
ash "It's private."
scene ep11_pp_ashley_event9 with dissolve
sar "Hypothetically, [name]. Do you think Ashley should dump Anthony for Derek, or what?"
scene ep11_pp_ashley_event13 with dissolve
ash "Sarah!"
scene ep11_pp_ashley_event1 with dissolve
sar "Hypothetically, Ash!"
scene ep11_pp_ashley_event13 with dissolve
ash "Oh my God, you're such an asshole."
scene ep11_pp_ashley_event11 with dissolve
mc "I'm biased in this question, so I'll say you should do what makes you happy."
scene ep11_pp_ashley_event12 with dissolve
ash "I didn't ask!"
scene ep11_pp_ashley_event11 with dissolve
mc "Hypothetically, of course. While he doesn't say it, I know Derek is still into you."
scene ep11_pp_ashley_event14 with dissolve
ash "..."
scene ep11_pp_ashley_event1 with dissolve
sar "See, it was good that I asked him, huh?"
scene ep11_pp_ashley_event13 with dissolve
ash "I'll get you back for this one day."

$ new_bio("Ashley", "Ashley was considering dumping Anthony for Derek and got mad at Sarah for telling me.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_drink1_event_label:
scene ep11_pp_drink1_event with dissolve
mc "(There we go... Some punch for that girl upstairs.)"
if persistent.mod_wtenabled:
            $ optional_task_list[2] = "Get the girl a drink (Upper Main Room)"
else:
            $ optional_task_list[2] = "Get the girl a drink"
$ event_list.append("ep11_pp_drink2_event_label")
jump endEvent

label ep11_pp_zoey_event_label:
scene ep11_pp_zoey_event1 with dissolve
he "Why shouldn't I come to a party with my friends? Because Tommy's there? Grow up."
scene ep11_pp_zoey_event7 with dissolve
ml "I was just asking if it was awkward."
scene ep11_pp_zoey_event2 with dissolve
he "It's not awkward. I'll go where I please. And if Tommy feels awkward that I'm here, he'll have to deal with it."
scene ep11_pp_zoey_event6 with dissolve
le "No, he's fine with it. I already asked."
scene ep11_pp_zoey_event3 with dissolve
he "What did he say?"
scene ep11_pp_zoey_event6 with dissolve
le "Not much. You know him. But I figured he would have put up a fight if he didn't want it."
scene ep11_pp_zoey_event5 with dissolve
zo "Did you guys break up recently?"
scene ep11_pp_zoey_event4 with dissolve
he "Around Thanksgiving. But there's been friction for quite some time before that."
he "But that's what happens when you agree to be in an open relationship that only was \"open\" for one of us."
scene ep11_pp_zoey_event5 with dissolve
zo "Oh..."
scene ep11_pp_zoey_event4 with dissolve
he "Yeah, \"Oh\". You don't have to sympathize or try to understand it. It's over now."
scene ep11_pp_zoey_event8 with dissolve
ml "What about you, Zoey? You're single, yeah?"
scene ep11_pp_zoey_event9 with dissolve
zo "Eh... Yeah. I'm single. Is it that obvious?"
scene ep11_pp_zoey_event8 with dissolve
ml "No, I could tell from how much Jacob likes you."
scene ep11_pp_zoey_event9 with dissolve
zo "He's just a friend."
scene ep11_pp_zoey_event8 with dissolve
ml "For now, haha."
scene ep11_pp_zoey_event11 with dissolve
le "Jacob is a great guy. Trustworthy, empathetic, funny..."
scene ep11_pp_zoey_event10 with dissolve
zo "I'm sure he is."
scene ep11_pp_zoey_event12 with dissolve
mc "Why are you all standing here? There's dancing in Tommy's room."
scene ep11_pp_zoey_event13 with dissolve
mc "Oh, shit. Sorry! I didn't see you there, Heather."
scene ep11_pp_zoey_event15 with dissolve
he "I'm ok! Ok? Can everyone stop assuming I'm not?"
scene ep11_pp_zoey_event13 with dissolve
if affinity == "DIK":
    mc "Now that we have established that Heather is doing ok... How are the rest of you doing?"
else:
    mc "I didn't mean to start something. Uh... So, how's everyone doing?"
scene ep11_pp_zoey_event14 with dissolve
ml "Weak party, so far. Did you even invite any guys?"
scene ep11_pp_zoey_event16 with dissolve
mc "Of course, we did. Here's one of them."
if affinity == "DIK":
    scene ep11_pp_zoey_event17 with dissolve
    mc "And he came dressed as a guy for this party for a change. Or maybe as a topless girl?"
    scene ep11_pp_zoey_event18 with dissolve
    le "You're such an ass."
else:
    mc "A hell of a guy, too."
scene ep11_pp_zoey_event19 with dissolve
ml "Mhm. So, only DIKs?"
scene ep11_pp_zoey_event20 with dissolve
mc "No, no. Others too. There is someone behind you... And I've seen some more hanging around."
scene ep11_pp_zoey_event21 with dissolve
zo "You see what she's getting at, don't you? There are way more girls than guys here."
scene ep11_pp_zoey_event20 with dissolve
mc "I'm sorry, but I had to do it WWTD style."
scene ep11_pp_zoey_event25 with dissolve
he "A what style?"
scene ep11_pp_zoey_event26 with dissolve
mc "WWTD. What would Tommy do? He'd invite more girls than guys to skew the ratio in favor of the dudes."
scene ep11_pp_zoey_event25 with dissolve
he "Don't tell me there are two of you."
scene ep11_pp_zoey_event26 with dissolve
mc "I did it for him. He's been pretty bummed out lately."
mc "Again... Sorry, Heather."
scene ep11_pp_zoey_event27 with dissolve
he "Has he really?"
scene ep11_pp_zoey_event22 with dissolve
ml "Nick isn't coming, right?"
scene ep11_pp_zoey_event24 with dissolve
le "We're not talking about him tonight. He's not here to defend himself."
scene ep11_pp_zoey_event23 with dissolve
ml "So, you guys are cool? I heard you weren't."
scene ep11_pp_zoey_event24 with dissolve
le "He's still one of us."
scene ep11_pp_zoey_event23 with dissolve
ml "But he left."

if ep11_nick_attitude > 1:
    scene ep11_pp_zoey_event20 with dissolve
    if affinity == "DIK":
        mc "Mel is right, though. We're far from cool. He's a fucking ass, if you ask me."
    else:
        mc "Mel is right, though. We're far from cool. I didn't invite him tonight."
    scene ep11_pp_zoey_event22 with dissolve
    ml "I didn't realize it was that bad."
else:
    scene ep11_pp_zoey_event20 with dissolve
    mc "What Leon's trying to say is that we're not done arguing and that anything can happen. And we're not going to talk badly about the guy."
    scene ep11_pp_zoey_event22 with dissolve
    ml "I wasn't saying you should talk smack; I was asking where he was tonight. But I get it, it's sensitive."

scene ep11_pp_zoey_event21 with dissolve
zo "Nick is a DIK, right? What did he do?"
scene ep11_pp_zoey_event28 with dissolve
he "*{i}Groans{/i}*"

scene ep11_pp_zoey_event29 with dissolve
mc "Let's chat over here for a while."
scene ep11_pp_zoey_event30 with dissolve
zo "Did I say something wrong? Everyone else was talking about him."
scene ep11_pp_zoey_event31 with dissolve
mc "No, you didn't... However, Nick is one of the reasons Heather broke up with Tommy."
if ep9_heather_lewd == 2:
    mc "Well... I am, too."
mc "Enough about that. How are you settling in? You seem more comfortable now than when you showed up."
scene ep11_pp_zoey_event32 with dissolve
zo "It's called liquid courage, and I'm increasing it by the minute."
scene ep11_pp_zoey_event33 with dissolve
mc "Haha, that's good. You don't have to do that Dirty Bowl mission if you don't want to, by the way. I'll give you a pass."
scene ep11_pp_zoey_event34 with dissolve
zo "What mission?"
scene ep11_pp_zoey_event33 with dissolve
mc "The ones Derek is handing out. I'd avoid him if I were you."
scene ep11_pp_zoey_event34 with dissolve
zo "That's fine. I only came here so I could talk to you. I bet you're gonna be busy tonight as always."
scene ep11_pp_zoey_event33 with dissolve
mc "Somewhat, yeah. But not as bad as it was during Halloween. And I've got some more help from Derek handling things."
mc "I have time to talk to you. So, what's up? Anything on your mind?"
scene ep11_pp_zoey_event37 with dissolve
zo "A lot."
scene ep11_pp_zoey_event38 with dissolve
mc "Let's hear it."
scene ep11_pp_zoey_event39 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_event40 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_event37 with dissolve
zo "Uh... I..."
zo "Guess who will maybe start at B&R in the spring?"
scene ep11_pp_zoey_event36 with dissolve
mc "No way...? Did you apply?"
scene ep11_pp_zoey_event35 with dissolve
zo "Kinda late, but yeah, I did. I'm scared my chances suck, but we'll see."
scene ep11_pp_zoey_event33 with dissolve
mc "What did you apply for?"
scene ep11_pp_zoey_event34 with dissolve
zo "A four-year digital design program. It's intimidating as fuck."
scene ep11_pp_zoey_event33 with dissolve
mc "That's awesome. I've always known you were talented with that."
scene ep11_pp_zoey_event34 with dissolve
zo "Digital design and drawing isn't the same, dude."
scene ep11_pp_zoey_event33 with dissolve
mc "No, but I think you will do amazing. I'm happy for you."
scene ep11_pp_zoey_event35 with dissolve
zo "You are?"
scene ep11_pp_zoey_event36 with dissolve
mc "Of course! I think it's great that you found something you want to do."
scene ep11_pp_zoey_event35 with dissolve
zo "Yeah... Same."
scene ep11_pp_zoey_event36 with dissolve
mc "We'll see each other a lot next year then."
scene ep11_pp_zoey_event34 with dissolve
zo "You're talking as if it's decided. I don't even know if I'll get in. A lot can happen in a month. Maybe I was too late?"
scene ep11_pp_zoey_event33 with dissolve
mc "Even so..."
scene ep11_pp_zoey_event38 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_event40 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_event33 with dissolve
mc "Thanks for sharing it with me."
scene ep11_pp_zoey_event34 with dissolve
zo "I wanted you to hear it first. After Mom, of course."
scene ep11_pp_zoey_event33 with dissolve
mc "Is she supportive?"
scene ep11_pp_zoey_event34 with dissolve
zo "Very."
scene ep11_pp_zoey_event33 with dissolve
mc "That was some big news. I'm happy you told me face-to-face."
scene ep11_pp_zoey_event37 with dissolve
zo "There's another thing too. But..."
zo "It can wait until later."
scene ep11_pp_zoey_event38 with dissolve
mc "I've got time."
scene ep11_pp_zoey_event37 with dissolve
zo "No. Not yet. I'm not in a rush tonight."
scene ep11_pp_zoey_event38 with dissolve
mc "Alright. I'll get back to checking up on the party then, and you can grab me whenever you want."
mc "With that first piece of news, you got me hyped for the second round already."
scene ep11_pp_zoey_event41 with dissolve
$ renpy.pause()
$ new_bio("Zoey", "Zoey told me she'd applied for a digital design program at B&R.")
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_bianca_event_label:
scene ep11_pp_bianca_event1 with dissolve
mc "Hey! How's it going?"
if branchIsabella or branchJill:
    scene ep11_pp_bianca_event2 with dissolve
    bia "There he is! We've been looking for you."
    scene ep11_pp_bianca_event4 with dissolve
    bia "Thank you so much for the invite."
    scene ep11_pp_bianca_event5 with dissolve
    mc "Don't mention it."
    scene ep11_pp_bianca_event6 with dissolve
    mc "Welcome, Carla. What a great party you chose for your first one."
else:
    scene ep11_pp_bianca_event2 with dissolve
    bia "Thank you so much for the invite. I had to bring Carla to one of your parties, haha!"
    scene ep11_pp_bianca_event3 with dissolve
    mc "Don't mention it. Welcome, Carla. What a great party you chose for your first one."
scene ep11_pp_bianca_event7 with dissolve
car "Oh, it's not my first. I went to one last year, but it wasn't anything like this."
car "This one makes me wonder what went through your mind when you planned it. This party is nuts."
scene ep11_pp_bianca_event9 with dissolve
mc "I have to take responsibility for this one... I planned it."
scene ep11_pp_bianca_event10 with dissolve
bia "Hahaha! No way! Was it your idea to have a lingerie Christmas party?"
scene ep11_pp_bianca_event9 with dissolve
mc "A Christmas Panty party, if you will... And yes. But also, they have had these parties in the past, so I can't take full credit for the idea."

if branchJill or branchIsabella:
    scene ep11_pp_bianca_event11 with dissolve
    bia "So, what was Jill's excuse for not showing up?"
    scene ep11_pp_bianca_event12 with dissolve
    mc "She's busy tonight with Bella and friends. I wish I could say she would have loved to come, but she wouldn't."
    scene ep11_pp_bianca_event11 with dissolve
    bia "Haha! Nope! We couldn't have convinced her either."
else:
    scene ep11_pp_bianca_event11 with dissolve
    bia "Did you invite Jill? She said she wasn't coming, but I was unsure if she was invited."
    scene ep11_pp_bianca_event12 with dissolve
    mc "Yeah, I invited her. But she was busy tonight."
    scene ep11_pp_bianca_event11 with dissolve
    bia "That's convenient, haha."
scene ep11_pp_bianca_event9 with dissolve
mc "I'm happy you two showed up. Did you bring anyone with you?"
if not ep9_told_jill:
    scene ep11_pp_bianca_event11 with dissolve
    if ep8_jill_state == 0:
        bia "I was going to bring my boyfriend, Matthew, but he had dinner plans with some friends."
    else:
        bia "Matty couldn't come; he had dinner plans with some friends."
scene ep11_pp_bianca_event13 with dissolve
if ep8_jill_state == 0:
    car "I asked my boyfriend, Jeff, to come, but he never goes to my college parties. He finds them too loud and annoying."
else:
    car "I asked Jeff to come, but he never tags along to my college parties. He finds them too loud and annoying."
car "He was worried about the theme when I showed him what I'd be wearing."
scene ep11_pp_bianca_event9 with dissolve
mc "Tell Jeff not to worry; you're in good hands tonight."
scene ep11_pp_bianca_event7 with dissolve
car "I'd tell him, if you guys didn't confiscate our phones."
scene ep11_pp_bianca_event8 with dissolve
mc "Ah, sorry about that. It's a party rule for all guests."
mc "You can always use it by the front door."
scene ep11_pp_bianca_event7 with dissolve
car "It's fine. I wouldn't know where to put it anyway. This outfit doesn't have pockets."
car "Did I emphasize how nuts the party is?"
scene ep11_pp_bianca_event14 with dissolve
de "New guests! Welcome! You have to pull a mission from The Dirty Bowl."
scene ep11_pp_bianca_event15 with dissolve
bia "What is that? It sounds scary."
scene ep11_pp_bianca_event16 with dissolve
if ep9_told_jill:
    mc "Carla has a boyfriend, Derek. Maybe you should let her slide."
else:
    mc "They have boyfriends, Derek. Maybe you should give them a free pass."
scene ep11_pp_bianca_event17 with dissolve
de "No way. Every guest must take a mission. No exceptions. Boyfriend or girlfriend, it doesn't matter."
de "We treat everyone equally tonight. I don't make the rules."
scene ep11_pp_bianca_event16 with dissolve
mc "Except that you did help make the rules."
scene ep11_pp_bianca_event17 with dissolve
de "No exceptions."
scene ep11_pp_bianca_event18 with dissolve
bia "It's fine. We'll take one each. There!"
scene ep11_pp_bianca_event19 with dissolve
de "Best of luck to you. Finish them by midnight or face the consequences."
scene ep11_pp_bianca_event20 with dissolve
car "Then, I'll be out of here come midnight. Look."
bia "Oh my God! Hahaha!"
scene ep11_pp_bianca_event21 with dissolve
mc "Let me guess, it's something bad."
scene ep11_pp_bianca_event22 with dissolve
car "Again... Nuts, I tell you. Nuts. And now I have to suck on someone's nuts too. Coincidence? I think not."
scene ep11_pp_bianca_event24 with dissolve
if ep9_told_jill:
    bia "I'd trade you mine, but I don't think you want it."
else:
    bia "Mine's not much better."
bia "Spanked, licked and bit? Kind of excessive, don't you think?"
scene ep11_pp_bianca_event21 with dissolve
mc "I should have told you to dodge Derek while I had the chance."
scene ep11_pp_bianca_event22 with dissolve
car "At least we have until midnight to party... Yay..."
if ep11_pp_game == 0 or ep11_pp_contest != 2:
    scene ep11_pp_bianca_event21 with dissolve
    mc "You didn't hear this from me, but there may be an opportunity to get out of doing the mission before midnight. You'll know when you hear it."
    scene ep11_pp_bianca_event22 with dissolve
    car "Well, that's good to know. Thanks."
scene ep11_pp_bianca_event23 with dissolve
bia "Did you get a mission, too?"
if ep11_db_mission:
    scene ep11_pp_bianca_event21 with dissolve
    mc "Yep. I have to dress as Santa and make five girls sit in my lap over there."
    scene ep11_pp_bianca_event25 with dissolve
    bia "Haha! Like a mall Santa?"
    scene ep11_pp_bianca_event26 with dissolve
    mc "Yes. Like a half-naked and drunk mall Santa. I have to ask them if they've been naughty or nice and what they want for Christmas."
    scene ep11_pp_bianca_event27 with dissolve
    car "Oh yeah? How many are you up to so far?"
    scene ep11_pp_bianca_event28 with dissolve
    if ep11_db_mission_progress == 0:
        mc "I haven't even started yet. Hopefully, I'll finish before midnight."
    else:
        mc "Just one..."
    scene ep11_pp_bianca_event23 with dissolve
    bia "Do you need our help? I'm sure we can help you out with that."
    scene ep11_pp_bianca_event22 with dissolve
    car "Yeah, it sounds innocent enough. I mean, it's not like mine."
    scene ep11_pp_bianca_event21 with dissolve
    mc "That would be great."
    scene ep11_pp_bianca_event23 with dissolve
    bia "Let us know when you wanna do it."
    $ event_list.append("ep11_pp_santa_bc_event_label")
else:
    scene ep11_pp_bianca_event21 with dissolve
    mc "I got a free pass because of my duties tonight."
    scene ep11_pp_bianca_event22 with dissolve
    car "So, the rules weren't the same for everyone."

$ new_bio("Bianca", "Bianca and Carla showed up for the DIKs' Christmas Panty party. She was excited to be there.")
$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_santa_event_label:
scene ep11_pp_santa_event1 with dissolve
mc "(Alright, let's see if we can do this mission...)"

if ep11_db_mission_progress == 0:
    $ guideSuggestedPage = 196
    scene ep11_pp_santa_event2 with dissolve
    mc "Ho ho ho!"
    scene ep11_pp_santa_event4 with dissolve
    sar "You are putting too much emphasis on the word ho."
    scene ep11_pp_santa_event5 with dissolve
    mc "I was?"
    scene ep11_pp_santa_event6 with dissolve
    sar "Why are you dressed like that?"
    scene ep11_pp_santa_event8 with dissolve
    mc "Because I'm Santa! Wanna sit in my lap for a while?"
    scene ep11_pp_santa_event6 with dissolve
    sar "Why?"
    scene ep11_pp_santa_event7 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "To help me with my mission":
            mc "I need help completing my mission. Can you humor me?"
        "Get your ass over here \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "Sarah, get your ass over here and sit in my lap."
    scene ep11_pp_santa_event9 with dissolve
    $ renpy.pause()
    scene ep11_pp_santa_event10 with dissolve
    $ renpy.pause()
    scene ep11_pp_santa_event11 with dissolve
    sar "Now what?"
    scene ep11_pp_santa_event12 with dissolve
    mc "What's your name, little girl?"
    scene ep11_pp_santa_event11 with dissolve
    sar "Little girl?"
    scene ep11_pp_santa_event13 with dissolve
    mc "Santa's old, you know?"
    scene ep11_pp_santa_event14 with dissolve
    sar "Haha, yeah, but still. Kinda creepy."
    scene ep11_pp_santa_event13 with dissolve
    mc "What's your name, Sarah?"
    scene ep11_pp_santa_event14 with dissolve
    sar "Haha, I'm Sarah!"
    scene ep11_pp_santa_event13 with dissolve
    mc "Ah, and have you been a good girl this year?"
    scene ep11_pp_santa_event15 with dissolve
    sar "Good how?"
    scene ep11_pp_santa_event16 with dissolve
    mc "Have you been nice or naughty?"
    scene ep11_pp_santa_event15 with dissolve
    sar "Aren't you supposed to know that already?"
    scene ep11_pp_santa_event16 with dissolve
    menu:
        "Nice list":
            mc "You're right; it was a test. My list tells me you've been a nice girl."
            scene ep11_pp_santa_event17 with dissolve
            sar "Oh, Santa. Your lists must be jumbled."
        "Naughty list":
            mc "You're right; it was a test. My list tells me you've been a naughty girl."
            scene ep11_pp_santa_event17 with dissolve
            sar "Oh, Santa. You don't know the half of it."
    scene ep11_pp_santa_event16 with dissolve
    mc "What do you want for Christmas?"
    scene ep11_pp_santa_event18 with dissolve
    sar "I haven't wished for anything."
    scene ep11_pp_santa_event16 with dissolve
    mc "Maybe something soft? Like a nice sweater?"
    scene ep11_pp_santa_event17 with dissolve
    sar "I'd rather get something hard for Christmas."
    scene ep11_pp_santa_event16 with dissolve
    mc "A book it is!"
    scene ep11_pp_santa_event18 with dissolve
    sar "Tsk. What about you, Santa? What do you want for Christmas?"
    scene ep11_pp_santa_event16 with dissolve
    mc "Santa doesn't get gifts; he brings them."
    scene ep11_pp_santa_event18 with dissolve
    sar "Aw, that's sad. Do you never get presents?"
    scene ep11_pp_santa_event16 with dissolve
    mc "I get milk and cookies."
    scene ep11_pp_santa_event18 with dissolve
    sar "But no gifts?"
    scene ep11_pp_santa_event16 with dissolve
    mc "Well, no..."
    scene ep11_pp_santa_event17 with dissolve
    sar "You're in luck, Santa. I came dressed as a gift."
    scene ep11_pp_santa_event19 with dissolve
    sar "Wanna unwrap me and taste my cookie?"
    if (ep11_maya_love > 0 or ep11_josy_love > 0) and wt_ep9_branch_numbers == 1:
        jump ep11_pp_santa_event_sarah_no_label
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"
    menu:
        "Where do I pull? \n{size=-4}[m_c1][mod_choices[6]]":
            if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                $ tc += 1
            scene ep11_pp_santa_event20 with dissolve
            mc "Where do I pull?"
            scene ep11_pp_santa_event21 with dissolve
            mc "Oh, well, that certainly did something."
            scene ep11_pp_santa_event22 with dissolve
            sar "Do you like it, Santa?"
            menu:
                "Where's the cookie? \n{size=-4}[m_c1][mod_choices[6]]":
                    if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                        $ tc += 1
                    mc "That's the milk. Now, where is the cookie?"
                    scene ep11_pp_santa_event23 with dissolve
                    sar "Down here."
                    scene ep11_pp_santa_event24 with dissolve
                    mc "It must be Christmas because my South pole is pointing North."
                    menu:
                        "Touch her \n{size=-4}[m_c1][mod_choices[7]]":
                            if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                                $ tc += 3
                            scene ep11_pp_santa_event25 with dissolve
                            mc "Fuck..."
                            sar "Nuh-uh... Hands out of the cookie jar."
                            $ new_bio("Sarah", "Sarah sat in my lap when I dressed as Santa. She had been a naughty girl, but ironically, I was the one who ended up being naughty with her.")
                        "Don't touch her":
                            mc "Very hot, Sarah..."
                "This wasn't what I wished for":
                    mc "Well, this wasn't what I wished for."
            scene ep11_pp_santa_event26 with dissolve
            sar "Bad, bad Santa. Hahaha!"
        "It's not Christmas yet":
            label ep11_pp_santa_event_sarah_no_label:
            mc "No. It's not Christmas yet."
            scene ep11_pp_santa_event17 with dissolve
            sar "It's fine, you can open it."
            scene ep11_pp_santa_event27 with dissolve
            mc "Naughty list, indeed. Santa doesn't have time for this. Off you go."
    scene ep11_pp_santa_event28 with dissolve
    $ renpy.pause()
    $ ep11_db_mission_progress += 1
elif "ep11_pp_santa_bc_event_label" in event_list:
    $ event_list.remove("ep11_pp_santa_bc_event_label")
    jump ep11_pp_santa_bc_event_label
elif "ep11_pp_santa_sandy_event_label" in event_list:
    $ event_list.remove("ep11_pp_santa_sandy_event_label")
    jump ep11_pp_santa_sandy_event_label
elif "ep11_pp_santa_heather_event_label" in event_list:
    $ event_list.remove("ep11_pp_santa_heather_event_label")
    jump ep11_pp_santa_heather_event_label
else:
    scene ep11_pp_santa_event2 with dissolve
    mc "Ho ho ho!"
    scene ep11_pp_santa_event3 with dissolve
    mc "(Hm... No one seems interested right now. I'll try again later.)"

if ep11_db_mission_progress == 5:
    scene ep11_pp_santa_event1 with dissolve
    mc "(I did it... I finished my mission. No consequence for me.)"
    if "ep11_pp_santa_event_label" in event_list:
        $ event_list.remove("ep11_pp_santa_event_label")
    $ optional_task_list[0] = ""
else:
    $ event_list.append("ep11_pp_santa_event_label")
    $ optional_task_list[0] = "Dirty Bowl Mission [ep11_db_mission_progress]/5"
$ updateTaskList()
jump endEvent

label ep11_pp_santa_heather_event_label:
scene ep11_pp_santa_heather_event1 with dissolve
mc "Heather! Ho ho ho!"
scene ep11_pp_santa_heather_event2 with dissolve
he "What did you call me?"
scene ep11_pp_santa_heather_event3 with dissolve
mc "I'm Santa!"
scene ep11_pp_santa_heather_event4 with dissolve
he "I thought that was Tommy's thing."
scene ep11_pp_santa_heather_event5 with dissolve
mc "This year it's my thing."
mc "Wanna sit in my lap for a while?"
scene ep11_pp_santa_heather_event4 with dissolve
he "Sure."
scene ep11_pp_santa_heather_event6 with dissolve
mc "How are you?"
scene ep11_pp_santa_heather_event7 with dissolve
he "Not too good, [name]."
scene ep11_pp_santa_heather_event9 with dissolve
mc "Santa."
scene ep11_pp_santa_heather_event8 with dissolve
he "Not too good, Santa."
scene ep11_pp_santa_heather_event9 with dissolve
mc "How so?"
scene ep11_pp_santa_heather_event10 with dissolve
he "I shouldn't have come here tonight. I only came to make a statement to Tommy... That I'll still be around even though we've broken up."
he "But it's falling on deaf ears. He's hooking up with girls and having fun..."
scene ep11_pp_santa_heather_event11 with dissolve
he "It's like nothing even happened. He's the same as he was when he was with me."
scene ep11_pp_santa_heather_event12 with dissolve
mc "Maybe that tells you what you need to know."
scene ep11_pp_santa_heather_event11 with dissolve
he "What do you mean?"
scene ep11_pp_santa_heather_event12 with dissolve
mc "If you can't spot a difference between him being with and without you..."
mc "Maybe he didn't care that much about you to begin with?"
scene ep11_pp_santa_heather_event13 with dissolve
he "You're wrong. He did care about me."
he "You don't know him as well as I do. We've gone through a lot together."
scene ep11_pp_santa_heather_event14 with dissolve
mc "I'm no relationship expert. I can't tell you where the line is drawn in the sand, but I think that having sex with others might be it."
scene ep11_pp_santa_heather_event13 with dissolve
he "All that put aside, I thought he'd at least react to me being here. But he's not."
scene ep11_pp_santa_heather_event14 with dissolve
mc "Maybe he is, but isn't showing it. I mean, he was upset about what happened. It caused a big fight among us."
mc "You want him to care, don't you?"
scene ep11_pp_santa_heather_event15 with dissolve
he "Yes, but not just post-breakup. I've wanted him to care more about me for a long time."
he "And to care doesn't mean to lose it and get angry. I wanted him to show me that I meant something to him."
scene ep11_pp_santa_heather_event13 with dissolve
he "He made me feel worthless. And I don't deserve that."
scene ep11_pp_santa_heather_event14 with dissolve
mc "No, you don't."
scene ep11_pp_santa_heather_event16 with dissolve
he "..."
scene ep11_pp_santa_heather_event17 with dissolve
he "Do you have anything that will make me feel less shitty in store for me this year?"
scene ep11_pp_santa_heather_event16 with dissolve
mc "Huh?"
scene ep11_pp_santa_heather_event17 with dissolve
he "Aren't you Santa?"
scene ep11_pp_santa_heather_event16 with dissolve
mc "Oh, yeah."
mc "For a nice girl like you, I want to give you what you wish, but I'm afraid my powers are limited to physical gifts."
mc "I can't change Tommy for you."
scene ep11_pp_santa_heather_event18 with dissolve
he "Neither could I."
he "Anyway, thanks for listening, [name]."
scene ep11_pp_santa_heather_event19 with dissolve
he "You look so stupid in that beard and boxers."
scene ep11_pp_santa_heather_event20 with dissolve
mc "I know. But it cheers people up."
scene ep11_pp_santa_heather_event19 with dissolve
he "It worked on me. You're a better Santa than Tommy ever was."
scene ep11_pp_santa_heather_event21 with dissolve
$ renpy.pause()

$ ep11_db_mission_progress += 1
if ep11_db_mission_progress == 5:
    scene ep11_pp_santa_event1 with dissolve
    mc "(I did it... I finished my mission. No consequence for me.)"
    $ optional_task_list[0] = ""
else:
    $ event_list.append("ep11_pp_santa_event_label")
    $ optional_task_list[0] = "Dirty Bowl Mission [ep11_db_mission_progress]/5"
$ updateTaskList()
$ new_bio("Heather", "Heather sat in my lap when I dressed as Santa. She told me about how she's been doing post-breakup.")
jump endEvent

label ep11_pp_santa_sandy_event_label:
$ guideSuggestedPage = 203
scene ep11_pp_santa_event2 with dissolve
mc "Ho! Ho! Ho!!!"
scene ep11_pp_santa_sandy_event1 with dissolve
sn "Santa!!!"
play sound "sound_effects/shove.mp3"
scene ep11_pp_santa_sandy_event2 with hpunch
mc "Oof! Hey!"
sn "Hahaha! There's no way that Santa is at this party too. That's fucking amazing!"
scene ep11_pp_santa_sandy_event3 with dissolve
mc "Indeed, I am! Now, who might you be?"
scene ep11_pp_santa_sandy_event4 with dissolve
sn "I'm Sandy, Mr. Santa Claus! Now that I think about it, Sandy Claus has a nice ring to it, don't you think?"
scene ep11_pp_santa_sandy_event3 with dissolve
mc "Hoho, clever."
scene ep11_pp_santa_sandy_event5 with dissolve
sn "How about you ditch your old wife and get some new spice in your life?"
scene ep11_pp_santa_sandy_event6 with dissolve
mc "I don't know about that. Santa Claus is very much in love with Mrs. Claus."
scene ep11_pp_santa_sandy_event5 with dissolve
sn "Aw, a happily married man, are you? Does she still put out?"
scene ep11_pp_santa_sandy_event7 with dissolve
mc "*{i}Coughs{/i}* Sandy, you said..."
mc "Tell me, have you been naughty or nice this year?"
scene ep11_pp_santa_sandy_event8 with dissolve
sn "Naughty. Naughty as fuck. Not a day goes by without me being naughty."
scene ep11_pp_santa_sandy_event7 with dissolve
mc "Santa doesn't like naughty girls. He's been known to give you girls lumps of coal."
scene ep11_pp_santa_sandy_event8 with dissolve
sn "I don't want coal for Christmas, Santa."
scene ep11_pp_santa_sandy_event7 with dissolve
mc "Then what do you want for Christmas?"
scene ep11_pp_santa_sandy_event8 with dissolve
sn "Your big fat cock in my pussy."
scene ep11_pp_santa_sandy_event7 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "I don't see that happening":
        mc "I don't see that happening this year."
        scene ep11_pp_santa_sandy_event8 with dissolve
        sn "Then I'll have to work on getting nice for next year."
    "I can give you that \n{size=-4}[m_c1][mod_choices[6]]":
        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
            $ tc += 1
        scene ep11_pp_santa_sandy_event9 with dissolve
        mc "I can give you that, but you better be nice."
        scene ep11_pp_santa_sandy_event10 with dissolve
        sn "I can't wait for Christmas day, Santa. I'll be waiting for you to come down my chimney."
        scene ep11_pp_santa_sandy_event11 with dissolve
        sn "All the way down..."
        scene ep11_pp_santa_sandy_event12 with dissolve
        $ renpy.pause()
        scene ep11_pp_santa_sandy_event13 with dissolve
        sn "If you're free during Christmas break, you should drop by The Pink Rose."
        sn "Just saying..."
scene ep11_pp_santa_sandy_event14 with dissolve
sn "Thaaanks, Santa!"
scene ep11_pp_santa_sandy_event15 with dissolve
$ renpy.pause()

$ ep11_db_mission_progress += 1
if ep11_db_mission_progress == 5:
    scene ep11_pp_santa_event1 with dissolve
    mc "(I did it... I finished my mission. No consequence for me.)"
    $ optional_task_list[0] = ""
else:
    $ event_list.append("ep11_pp_santa_event_label")
    $ optional_task_list[0] = "Dirty Bowl Mission [ep11_db_mission_progress]/5"
$ updateTaskList()
jump endEvent

label ep11_pp_santa_bc_event_label:
$ ep11_pp_santa_bc = True
$ guideSuggestedPage = 197
scene ep11_pp_santa_event2 with dissolve
mc "Ho ho ho! Santa is open for business."
scene ep11_pp_santa_bc_event1 with dissolve
car "For business? What's your business registration number? Do you have a permit to set up shop here?"
scene ep11_pp_santa_bc_event2 with dissolve
mc "Do you want any Christmas gifts or are you going to be difficult?"
scene ep11_pp_santa_bc_event3 with dissolve
car "Haha! Sure."
scene ep11_pp_santa_bc_event4 with dissolve
mc "Ho ho ho! So... What's your name?"
scene ep11_pp_santa_bc_event6 with dissolve
car "I'm Carla."
scene ep11_pp_santa_bc_event5 with dissolve
mc "Carla, you say? Ah, I've seen that name on one of my lists."
scene ep11_pp_santa_bc_event6 with dissolve
car "I bet you have. It's not an uncommon name."
scene ep11_pp_santa_bc_event7 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "Nice list":
        mc "Carla... Carla... I believe I've read your name on the Nice list. Are you a nice girl?"
        scene ep11_pp_santa_bc_event8 with dissolve
        car "Yes. I'd say I'm a nice girl."
        if affinity == "DIK":
            scene ep11_pp_santa_bc_event7 with dissolve
            mc "Indeed. You're a very nice girl."
            scene ep11_pp_santa_bc_event8 with dissolve
            car "Santa is creepy this year. What's up with that?"
        else:
            scene ep11_pp_santa_bc_event7 with dissolve
            mc "Of course you are. I can see it in your eyes."
            scene ep11_pp_santa_bc_event8 with dissolve
            car "Is Santa coming on to me?"
        scene ep11_pp_santa_bc_event13 with dissolve
        mc "*{i}Coughs{/i}* Hngnrr..."
        mc "Carla!"
    "Naughty list":
        mc "Ok, smartass. I bet you're on the Naughty list."
        scene ep11_pp_santa_bc_event9 with dissolve
        car "Hahaha!"
        menu:
            "Peek at her body \n{size=-4}[m_c1][mod_choices[3]]":
                $ dk(1)
                scene ep11_pp_santa_bc_event10 with dissolve
                $ renpy.pause()
                scene ep11_pp_santa_bc_event11 with dissolve
                $ renpy.pause()
                scene ep11_pp_santa_bc_event12 with dissolve
                car "Eyes up here, Santa."
                scene ep11_pp_santa_bc_event13 with dissolve
                mc "Erm... You still have some time to be nice before Christmas."
                scene ep11_pp_santa_bc_event14 with dissolve
                car "And so do you. Haha!"
                scene ep11_pp_santa_bc_event13 with dissolve
            "Don't peek \n{size=-4}[m_c1][mod_choices[2]]":
                $ dk(-1)
                scene ep11_pp_santa_bc_event13 with dissolve
                mc "You still have some time to change before Christmas."
        mc "And if you were to change and become nice..."
mc "What do you want for Christmas?"
scene ep11_pp_santa_bc_event15 with dissolve
car "Can I wish for anything?"
scene ep11_pp_santa_bc_event16 with dissolve
mc "Why, yes, of course!"
scene ep11_pp_santa_bc_event15 with dissolve
car "When I was seven, I had a dog named Poodles. I wish he would come back to life. I miss him so much."
scene ep11_pp_santa_bc_event16 with dissolve
mc "Not even Santa can bring back your dead dog, Carla."
scene ep11_pp_santa_bc_event15 with dissolve
car "That's what the genie in the lamp said, too. Can I wish for three more wishes?"
scene ep11_pp_santa_bc_event16 with dissolve
mc "Ok, off you go. You're holding up the line."
scene ep11_pp_santa_bc_event17 with dissolve
car "Haha! He's all yours. I need to visit the restroom."
scene ep11_pp_santa_bc_event18 with dissolve
if affinity == "DIK":
    mc "Ah, Bianca. Park your cute ass on my lap for a while."
else:
    mc "Ah, Bianca. Come sit in Santa's lap."
scene ep11_pp_santa_bc_event19 with dissolve
bia "Wow, you knew my name without even asking. How is that possible?"
scene ep11_pp_santa_bc_event21 with dissolve
mc "Well, Santa knows when you're awake and watches you when you're asleep."
scene ep11_pp_santa_bc_event20 with dissolve
bia "That sounds kinky."
scene ep11_pp_santa_bc_event22 with dissolve
mc "Have you been good this year?"
scene ep11_pp_santa_bc_event23 with dissolve
bia "Nuh-uh. I've been bad, Santa."
scene ep11_pp_santa_bc_event22 with dissolve
mc "Oh? What bad things have you been doing?"
scene ep11_pp_santa_bc_event23 with dissolve
bia "I've been kissing too many boys and sometimes even girls."
bia "And I've been dressing provocatively, too."
scene ep11_pp_santa_bc_event24 with dissolve
bia "Dresses with cleavage down to here."
scene ep11_pp_santa_bc_event25 with dissolve
bia "And I've been dreaming of you, Santa."
bia "To come into my room at night when I sleep."
scene ep11_pp_santa_bc_event26 with dissolve
bia "And wake me up and give me a good spanking."
scene ep11_pp_santa_bc_event27 with dissolve
mc "Santa cannot keep hearing about this."
scene ep11_pp_santa_bc_event28 with dissolve
mc "Santa is in a very delicate situation here."
scene ep11_pp_santa_bc_event23 with dissolve
bia "You're blushing, Santa. Did I say something bad?"
bia "I can't help it. I'm a naughty girl. Such a naughty girl."
scene ep11_pp_santa_bc_event22 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(+Isabella)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "No gifts for you \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep11_pp_santa_bc_event29 with dissolve
        mc "Then no gifts for you! Better luck next year."
        scene ep11_pp_santa_bc_event30 with dissolve
        mc "Sheesh."
    "I'll spank you \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "If it's a spanking you want for Christmas, Santa will give you one."
        scene ep11_pp_santa_bc_event23 with dissolve
        bia "I thought Santa didn't grant wishes for naughty girls."
        scene ep11_pp_santa_bc_event22 with dissolve
        mc "I'll make an exception for you."
        scene ep11_pp_santa_bc_event32 with dissolve
        car "What are you two doing?"
        scene ep11_pp_santa_bc_event31 with dissolve
        bia "Santa is calling my bluff here."
        scene ep11_pp_santa_bc_event32 with dissolve
        car "Yeah, right. Bluff, huh? Sounds like someone wants to stay past midnight."
        scene ep11_pp_santa_bc_event29 with dissolve
        mc "That's all the time Santa has. See you next year."
        scene ep11_pp_santa_bc_event30 with dissolve
bia "Haha, I thought your mission was too simple. Now you know how we feel."

$ ep11_db_mission_progress += 2
if ep11_db_mission_progress == 5:
    scene ep11_pp_santa_event1 with dissolve
    mc "(I did it... I finished my mission. No consequence for me.)"
    $ optional_task_list[0] = ""
else:
    $ event_list.append("ep11_pp_santa_event_label")
    $ optional_task_list[0] = "Dirty Bowl Mission [ep11_db_mission_progress]/5"

$ new_bio("Bianca", "Bianca sat in my lap when I dressed as Santa. It got a bit flirty...")
$ updateTaskList()
jump endEvent

label ep11_pp_tiffani_event_label:
$ guideSuggestedPage = 195
scene ep11_pp_tiffani_event1 with dissolve
jm "Is THAT what it is for?"
scene ep11_pp_tiffani_event2 with dissolve
ti "What did you think it was for?"
scene ep11_pp_tiffani_event3 with dissolve
jm "The hell if I know, but there is too much hair and folds of meat in there as it is. It's hard to know what anything is."
jm "Especially when the girls have a jungle bush."
scene ep11_pp_tiffani_event5 with dissolve
ma "Tell me about it. And all this time, I thought they peed out of the big hole and not that small one. I've never even seen that hole."
scene ep11_pp_tiffani_event4 with dissolve
jm "Hold on! Just for a second!"
jm "Female buttholes! What can you tell me about them?"
scene ep11_pp_tiffani_event6 with dissolve
mc "What the hell are you guys doing?"
scene ep11_pp_tiffani_event7 with dissolve
jm "My mission. \"Ask a girl to lecture you on vaginas\". And Tiffani was nice enough to help out."
scene ep11_pp_tiffani_event13 with dissolve
mc "I see... And what about you?"
scene ep11_pp_tiffani_event14 with dissolve
ma "I thought we were just learning."
scene ep11_pp_tiffani_event13 with dissolve
mc "Alright. Carry on."
scene ep11_pp_tiffani_event9 with dissolve
ti "What about you, [name]? You don't need a lecture on pussies, do you?"
scene ep11_pp_tiffani_event8 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "Brag \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep11_pp_tiffani_event10 with dissolve
        mc "I'm a learning-by-doing kind of guy. And I've gotten enough practice to know how to get girls off when I want to."
    "Diss the guys \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[1]]":
        $ dk(1)
        $ RPdiks -= 1
        mc "Back in high school, when they taught me, I did. Now, it would be sad to get one."
        scene ep11_pp_tiffani_event12 with dissolve
        jm "Hey!"
        scene ep11_pp_tiffani_event11 with dissolve
        ti "Haha!"
    "No, thank you \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep11_pp_tiffani_event10 with dissolve
        mc "I'm sure you're great at explaining vaginas, Tiffani, but I'm good. Thanks, though."

scene ep11_pp_tiffani_event3 with dissolve
jm "Now what about them buttholes?"
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_becky_event_label:
$ guideSuggestedPage = 195
scene ep11_pp_becky_event1 with dissolve
chr "Masturbate somewhere in the mansion."
scene ep11_pp_becky_event3 with dissolve
bc "It said that?"
scene ep11_pp_becky_event1 with dissolve
chr "Yeah. What about yours?"
scene ep11_pp_becky_event3 with dissolve
bc "\"Have sex with someone.\" And I hear it's not just me who got one of those."
bc "They either ran out of ideas or were desperate to get laid."
scene ep11_pp_becky_event1 with dissolve
chr "Like being in underwear isn't a layup as it is. They had to include these stupid missions to get people to fuck."
scene ep11_pp_becky_event3 with dissolve
bc "Totes. So lame. Are you gonna do yours?"
scene ep11_pp_becky_event2 with dissolve
chr "I can just say that I did it. It's not like anyone will check if I did. Yours is much harder to fake."
scene ep11_pp_becky_event4 with dissolve
mc "Did I hear that you will cheat on The Dirty Bowl tonight?"
scene ep11_pp_becky_event5 with dissolve
chr "No. You misheard."
scene ep11_pp_becky_event6 with dissolve
mc "Don't worry. I'm not enforcing it or anything. That's all Derek."
scene ep11_pp_becky_event5 with dissolve
chr "Then, yeah. You heard me right. Haha!"
scene ep11_pp_becky_event6 with dissolve
mc "I'm sure there's someone to help you with your mission. Didn't you and Tommy hook up on Halloween? I heard something about it."
scene ep11_pp_becky_event7 with dissolve
chr "He told people about that? That figures... What did he say?"
scene ep11_pp_becky_event8 with dissolve
mc "I heard from the guys you had sex. That's about it."
scene ep11_pp_becky_event7 with dissolve
chr "Did he leave out the part where he stopped in the middle of it and made me leave because of Quinn?"
scene ep11_pp_becky_event8 with dissolve
mc "That's news to me."
scene ep11_pp_becky_event7 with dissolve
chr "He's a douchebag for doing that. And even if I needed someone to carry out my mission tonight, it wouldn't be him."
scene ep11_pp_becky_event8 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "Good for you":
        mc "Good for you. At least you know what you want."
        scene ep11_pp_becky_event9 with dissolve
        chr "And it wouldn't be you either, so stop trying."
        scene ep11_pp_becky_event8 with dissolve
        mc "I wasn't trying. I was making conversation."
        scene ep11_pp_becky_event7 with dissolve
        chr "Sure you were. I know how guys like you work. You say something nice to get my attention, and later you neg me for control."
    "Flirt \n{size=-4}[m_c1][mod_choices[3]]":
        $ ep11_christie_flirt = True
        $ dk(1)
        mc "Good. You can do much better. You're looking hot tonight."
        scene ep11_pp_becky_event9 with dissolve
        chr "And it wouldn't be you either, so stop trying."
        scene ep11_pp_becky_event8 with dissolve
        mc "I'm calling it as I see it."
        scene ep11_pp_becky_event7 with dissolve
        chr "And I don't trust it. I know how guys like you work. You say something nice to get my attention, and later you neg me for control."
if affinity == "DIK":
    scene ep11_pp_becky_event10 with dissolve
    mc "Whoa, you sound damaged."
    scene ep11_pp_becky_event9 with dissolve
    chr "And there's the neg. Screw you."
    scene ep11_pp_becky_event10 with dissolve
else:
    scene ep11_pp_becky_event8 with dissolve
mc "Whatever."
scene ep11_pp_becky_event12 with dissolve
if ep11_christie_flirt:
    bc "What about me, [name]? I look hot, too, right?"
else:
    bc "[name]? Do you like what I'm wearing? It's hot, yeah?"
scene ep11_pp_becky_event13 with dissolve
$ renpy.pause()
scene ep11_pp_becky_event11 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "Yeah":
        mc "Yeah, sure. Very hot."
        scene ep11_pp_becky_event14 with dissolve
        $ renpy.pause()
    "No [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "No."
        scene ep11_pp_becky_event15 with dissolve
        bc "Aw, come on!"
        scene ep11_pp_becky_event16 with dissolve
        bc "See! He negged me too."
    "Have a nice party, Becky":
        mc "Have a nice party, Becky."
        scene ep11_pp_becky_event15 with dissolve
        bc "Aw, come on!"
        scene ep11_pp_becky_event16 with dissolve
        bc "See! He negged me, too."

scene ep11_pp_becky_event17 with dissolve
chr "Don't fall for his tricks."
scene ep11_pp_becky_event16 with dissolve
bc "I'm not. He's going to fall for mine."
scene ep11_pp_becky_event17 with dissolve
chr "What do you mean?"
scene ep11_pp_becky_event18 with dissolve
bc "I'm talking about my mission."
bc "I've had my eyes on him for a long time and now the stars have aligned. I'm going to fuck [name] tonight."

$ optional_task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_quinn_event_label:
scene ep11_pp_quinn_event1 with dissolve
qu "He's talking bullshit."
scene ep11_pp_quinn_event5 with dissolve
ly "I know he was, but his threat was serious."
scene ep11_pp_quinn_event2 with dissolve
qu "Vinny won't tell our supplier anything because he already knows enough."
scene ep11_pp_quinn_event5 with dissolve
ly "Your supplier knows that you stole us girls from Vinny?"
scene ep11_pp_quinn_event2 with dissolve
qu "Likely, but he doesn't care about that at all. What he cares about is that I made a profit from selling his stuff."
scene ep11_pp_quinn_event6 with dissolve
ly "Are you in trouble?"
scene ep11_pp_quinn_event3 with dissolve
qu "It's nothing I can't handle. My only reason for telling you this is so that you don't go back to Vinny. Ok?"
scene ep11_pp_quinn_event5 with dissolve
ly "Wait... How did your supplier find out?"
scene ep11_pp_quinn_event3 with dissolve
qu "It's irrelevant."
scene ep11_pp_quinn_event5 with dissolve
ly "Not to me."
scene ep11_pp_quinn_event3 with dissolve
qu "It doesn't concern you."
scene ep11_pp_quinn_event6 with dissolve
ly "Look, it wasn't just me who Vinny threatened. That threat was extended to my girls."
ly "I know them. Some of them will freak out when I tell them what Vinny said."
scene ep11_pp_quinn_event4 with dissolve
qu "Don't tell them anything."
scene ep11_pp_quinn_event7 with dissolve
ly "Someone cut his face with a knife, and he had a bad bruise. I wouldn't be surprised if something in his face were broken. This is serious, Quinn."
scene ep11_pp_quinn_event4 with dissolve
qu "Good, I can use that."
scene ep11_pp_quinn_event7 with dissolve
ly "Listen to me! I'm not going to jeopardize anything unless you have a damned good plan to deal with Vinny."
scene ep11_pp_quinn_event4 with dissolve
qu "I have a plan. And it will take care of everything."
scene ep11_pp_quinn_event7 with dissolve
ly "When?"
scene ep11_pp_quinn_event4 with dissolve
qu "Soon."
scene ep11_pp_quinn_event5 with dissolve
ly "You get a week, and that's me being generous. After that, I'm telling my girls about what happened. But I doubt Vinny will give me that long."
scene ep11_pp_quinn_event2 with dissolve
qu "I don't need a week."
scene ep11_pp_quinn_event5 with dissolve
ly "Are you sure?"
scene ep11_pp_quinn_event2 with dissolve
qu "Relax, ok? Enjoy whatever this party is."
scene ep11_pp_quinn_event8 with dissolve
mc "Did I hear someone say party?"
scene ep11_pp_quinn_event9 with dissolve
mc "Am I interrupting something?"

if ep10_quinn_help:
    if ep10_rolling:
        scene ep11_pp_quinn_event10 with dissolve
        qu "No. She's all yours."
    else:
        scene ep11_pp_quinn_event10 with dissolve
        qu "I need another beer."
else:
    scene ep11_pp_quinn_event11 with dissolve
    $ renpy.pause()

if ep10_rolling:
    scene ep11_pp_quinn_event12 with dissolve
    mc "What's up?"
    scene ep11_pp_quinn_event13 with dissolve
    ly "Nothing you have to worry about."
    ly "Having fun?"
    scene ep11_pp_quinn_event15 with dissolve
    mc "Yeah, I am! I'm happy with how the party came together."
    scene ep11_pp_quinn_event16 with dissolve
    ly "Christmas and sex are a wild theme."
    scene ep11_pp_quinn_event15 with dissolve
    mc "Christmas and underwear."
    scene ep11_pp_quinn_event17 with dissolve
    ly "Why lie, [name]?"
    scene ep11_pp_quinn_event15 with dissolve
    mc "Let's settle for calling it tradition, then."
    scene ep11_pp_quinn_event17 with dissolve
    ly "Ah, yes. It's quite the traditional party."
    scene ep11_pp_quinn_event15 with dissolve
    mc "How about you? Are you having fun?"
    scene ep11_pp_quinn_event16 with dissolve
    ly "Not yet, but I bet things will pick up. I'm waiting for my girls to show up."
    scene ep11_pp_quinn_event15 with dissolve
    mc "Awesome, who's coming?"
    scene ep11_pp_quinn_event16 with dissolve
    ly "Brandi had to work extra. Sky and Melody called in sick."
    scene ep11_pp_quinn_event15 with dissolve
    mc "I don't believe I've met them."
    scene ep11_pp_quinn_event18 with dissolve
    ly "I'm sure there are more who you haven't met. I don't usually work with them."
    ly "Anyway, Rose, Sandy, Nicole and Tania are coming tonight."
    scene ep11_pp_quinn_event15 with dissolve
    mc "That's great!"
    if ep10_date_nicole and not ep10_cancel_date_nicole:
        scene ep11_pp_quinn_event18 with dissolve
        ly "I bet you think so. What's up with you and Nicole, by the way? I heard you went out on a date."
        scene ep11_pp_quinn_event15 with dissolve
        mc "Yeah, we did. I went to her place for some drinks."
        scene ep11_pp_quinn_event18 with dissolve
        ly "Is it serious?"
        scene ep11_pp_quinn_event19 with dissolve
        mc "I got the feeling she liked it a lot and so did I."
        if ep10_nicole_questions[2]:
            if ep10_nicole_questions[0]:
                mc "There's potential there, for sure."
                mc "But she's a single mom... Getting involved in her kid's life could be too much."
            else:
                mc "There's some potential there, but I don't know if it will lead anywhere."
                mc "And she's a single mom... Getting involved in her kid's life could be too much."
        else:
            mc "At the moment, I think it's just about sex to me."
            mc "She's a single mom... Getting involved in her kid's life could be too much."
        scene ep11_pp_quinn_event20 with dissolve
        ly "Hm... You know I have to talk to her about this, right?"
        scene ep11_pp_quinn_event19 with dissolve
        mc "I can tell her that I have doubts."
        scene ep11_pp_quinn_event20 with dissolve
        ly "No. Not about your doubts. But you're dating my friend while we're rolling."
        ly "Nicole deserves better than that. She should at least be aware of it."
        scene ep11_pp_quinn_event19 with dissolve
        mc "It was just a date, Lily. If it gets serious, I won't fuck around."
        scene ep11_pp_quinn_event16 with dissolve
        ly "Are you sure about that, you slut?"
        scene ep11_pp_quinn_event15 with dissolve
        mc "I'm the slut, huh?"
        scene ep11_pp_quinn_event18 with dissolve
        ly "Don't you dare call me one."
        scene ep11_pp_quinn_event16 with dissolve
        ly "Well, in bed, it's fine."
        scene ep11_pp_quinn_event15 with dissolve
        mc "You're a good friend to have, Lily. Thinking about Nicole like that."
        mc "Given our threesome with her, I'm sure she wouldn't be surprised about us rolling, but even so, I'll mention it to her."
        scene ep11_pp_quinn_event17 with dissolve
        ly "The girls you invited are waiting. Off you go to play in the sandbox you created."
        $ new_bio("Lily", "Lily was concerned that I was dating Nicole while rolling with her. She asked me to talk to Nicole about it.")
    else:
        scene ep11_pp_quinn_event17 with dissolve
        ly "More girls equals more opportunities. Why don't you go play in the sandbox you created?"
    scene ep11_pp_quinn_event15 with dissolve
    mc "You wanna get rid of me?"
    scene ep11_pp_quinn_event17 with dissolve
    ly "I'm not your clingy girlfriend, [name]. Spread your oats or whatever you plan on doing tonight."
    scene ep11_pp_quinn_event21 with dissolve
    $ renpy.pause()
else:
    scene ep11_pp_quinn_event12 with dissolve
    mc "What's up?"
    scene ep11_pp_quinn_event14 with dissolve
    ly "Your cock in those boxers."
    scene ep11_pp_quinn_event12 with dissolve
    mc "No. It's not."
    scene ep11_pp_quinn_event13 with dissolve
    ly "Give it time. It will be at some point during tonight if I know you guys as well as I think I do."
    scene ep11_pp_quinn_event21 with dissolve
    mc "(They did not want to talk to me... Hm...)"
    $ new_bio("Lily", "Lily wasn't keen on chatting with me at the DIKs' Christmas Panty party.")
$ new_bio("Quinn", "Quinn seemed to avoid me at the DIKs' Christmas Panty party.")
$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_th_event_label:
$ guideSuggestedPage = 197
scene ep11_pp_th_event1 with dissolve
girl "*{i}Smack{/i}* Mmphhff..."
scene ep11_pp_th_event2 with dissolve
mia "How long do you think they'll keep going?"
scene ep11_pp_th_event3 with dissolve
er "Her mission said not to stop until the guy made her."
scene ep11_pp_th_event2 with dissolve
mia "At this rate, they won't stop at making out."
scene ep11_pp_th_event4 with dissolve
mc "I was going to check if the movie was still playing, but it looks like there is another type of entertainment in here."
scene ep11_pp_th_event5 with dissolve
er "How are you surprised by that? Didn't you and your friends plan this?"
scene ep11_pp_th_event6 with dissolve
mc "The Dirty Bowl was my idea, but I didn't write the missions."
scene ep11_pp_th_event7 with dissolve
mia "I can't believe people are going through with theirs. I thought it was a joke at first."
scene ep11_pp_th_event8 with dissolve
mc "It's for fun, to get guests to interact and talk."
scene ep11_pp_th_event9 with dissolve
er "How does flashing my boobs to people lead to conversation?"
scene ep11_pp_th_event8 with dissolve
if affinity == "DIK":
    mc "Oh, sweetie. It does."
else:
    mc "I bet it does."
scene ep11_pp_th_event9 with dissolve
er "Well, I'm supposed to do that and show myself fully naked to someone, too."
scene ep11_pp_th_event8 with dissolve
mc "Is yours as bad?"
scene ep11_pp_th_event7 with dissolve
mia "You tell me. I'm supposed to make out with three guys tonight."
scene ep11_pp_th_event8 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+3 Cheater)"

menu:
    "Better get to it, then \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Better get to it, then. I hear there are consequences if you don't."
        scene ep11_pp_th_event10 with dissolve
        mia "Psch..."
        scene ep11_pp_th_event14 with dissolve
        mc "And maybe yours doesn't have to be with a guy."
        scene ep11_pp_th_event15 with dissolve
        er "How about it, Mia?"
        scene ep11_pp_th_event16 with dissolve
        mia "Hell no. That wouldn't help me. You'll have to find others to do it, just like I have to find three guys for mine."
    "Nothing is forced \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Don't do it unless you want to. No one will force you; it's just for fun."
        scene ep11_pp_th_event11 with dissolve
        mia "We aren't against having fun. It was just unexpected."
        scene ep11_pp_th_event9 with dissolve
        er "Yup."

scene ep11_pp_th_event8 with dissolve
if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if (not branchAlone and not (ep11_maya_love > 0 or ep11_josy_love > 0)) or (branchAlone and wt_ep9_branch_numbers != 1):
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

menu:
    "Don't look at me":
        $ dk(-1)
        scene ep11_pp_th_event14 with dissolve
        mc "Don't look at me. I can't help you."
        scene ep11_pp_th_event17 with dissolve
        mc "But maybe that guy can? He seems to enjoy helping out."
    "[m_c1]Why are you looking at me?":
        $ guideSuggestedPage = 198
        mc "Why are you looking at me?"
        scene ep11_pp_th_event13 with dissolve
        er "Would you do it?"
        scene ep11_pp_th_event11 with dissolve
        mia "Wanna be my first one?"
        scene ep11_pp_th_event12 with dissolve
        er "Hahaha!"
        if (ep11_maya_love > 0 or ep11_josy_love > 0) and wt_ep9_branch_numbers == 1:
            jump ep11_pp_em_no_label
        menu:
            "Help them out \n{size=-4}[m_c1][mod_choices[7]]":
                $ ep11_helped_erin_mia = True
                $ dk(1)
                if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                    $ tc += 5
                if branchAlone:
                    mc "Yeah, what the hell? Let's have some fun."
                else:
                    mc "It's just for fun, right? There's no harm in looking at tits and an innocent kiss."
                scene ep11_pp_th_event20 with dissolve
                er "Don't brag to your friends about this."
                scene ep11_pp_th_event18 with dissolve
                mc "Very nice..."
                scene ep11_pp_th_event19 with dissolve
                er "How long do you reckon he has to look at them?"
                mia "If I'm making out with three guys, you better show them for longer than that."
                scene ep11_pp_th_event20 with dissolve
                er "That's enough... And what fun it was, haha."

                scene ep11_pp_th_event21 with dissolve
                mia "Is it my turn?"
                scene ep11_pp_th_event22 with dissolve
                mc "Oh... Like this?"
                scene ep11_pp_th_event24 with dissolve
                mia "*{i}Smack{/i}* Mmm..."
                scene ep11_pp_th_event25 with dissolve
                $ renpy.pause()
                scene ep11_pp_th_event26 with dissolve
                $ renpy.pause()
                scene ep11_pp_th_event27 with dissolve
                $ renpy.pause()
                scene ep11_pp_th_event28 with dissolve
                er "Way to go, Mia. That's one down."
                scene ep11_pp_th_event23 with dissolve
                mia "Thanks for the help."
                if not branchAlone:
                    scene ep11_pp_th_event29 with dissolve
                    mc "(That wasn't innocent... Um...)"
                    $ new_bio("You", "I helped Erin and Mia with their missions at the DIKs' Christmas Panty party. I thought it would be innocent, but it went further than that.")
                else:
                    scene ep11_pp_th_event30 with dissolve
                    mc "No problem. Good luck finding two more. I'm sure you can do it."
                    $ new_bio("You", "I helped Erin and Mia with their missions at the DIKs' Christmas Panty party.")
            "Don't help them \n{size=-4}[m_c2][mod_choices[2]]":
                label ep11_pp_em_no_label:
                $ dk(-1)
                scene ep11_pp_th_event14 with dissolve
                if not branchAlone:
                    mc "Sorry, but no."
                else:
                    mc "Nah. That would be too easy for you two. I'm sure you will find others to help you."
                scene ep11_pp_th_event17 with dissolve
                mc "Maybe that guy can help you? He seems to enjoy helping out."

$ optional_task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_group_event_label:
scene ep11_pp_group_event1 with dissolve
mc "(Hm... I don't recognize them, but it looks like they're having fun.)"
mc "(I hope they are cool people...)"
mc "(Ugh... I hate myself for being paranoid about guests' intentions now when it should be a fun party.)"
if ep11_invited_tara:
    mc "(I should talk to Tara about this when she shows up. Maybe she trusts me enough to tell me if any of these guests are against us.)"
jump endEvent

label ep11_pp_camila_event_label:
$ guideSuggestedPage = 198
scene ep11_pp_camila_event1 with dissolve
jac "Shake it! Shake it! There you go!"
scene ep11_pp_camila_event2 with dissolve
mc "Fewer people are dancing than I thought. Good for you that you started it."
scene ep11_pp_camila_event4 with dissolve
cam "You don't come to a party and don't dance! That's rude, you know?"
cam "[name]! This party was such a good idea!"
cam "Let me tell you! I'm sooooo fed up with the snow. Where is summer when you need it?"
scene ep11_pp_camila_event8 with dissolve
mc "I couldn't agree more with you. I miss summer too."
scene ep11_pp_camila_event6 with dissolve
cam "Let's dance to summer!"
cam "And to world peace!"
cam "And to jello shots. I could go for one now."
scene ep11_pp_camila_event5 with dissolve
mc "Haha! I don't think we have any jello shots tonight, but there's lots of beer."
scene ep11_pp_camila_event4 with dissolve
cam "I'm worried that I will drink too much tonight, [name]. You'll have to watch out for me, ok?"
scene ep11_pp_camila_event5 with dissolve
menu:
    "Ask Jacob to do it":
        mc "Jacob's your guy for that. Right, Jacob?"
        scene ep11_pp_camila_event7 with dissolve
        jac "Yeah, sure. I'll keep an eye out for you. No biggie."
    "Sure":
        mc "Sure, I will. And you can drink as much as you want, as long as it feels good."
        scene ep11_pp_camila_event4 with dissolve
        cam "Yeah, but usually I have someone to tell me to drink water, but tonight I don't."
        scene ep11_pp_camila_event5 with dissolve
        mc "Do you wanna have some water?"
        scene ep11_pp_camila_event6 with dissolve
        cam "Water? Hell no, I want beer! But thanks for asking!"
$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep11_freeroam_party_pr_label:
$ guideSuggestedPage = 201
play sound "sound_effects/bell.mp3"
scene ep11_freeroam_party_pr1 with dissolve
"*{i}Doorbell{/i}*"
mc "More guests? I'll take this one."
play sound "sound_effects/season3/door_open.mp3"
scene ep11_freeroam_party_pr2
show screen ep10_snow_screen
with dissolve
mc "Welcome to the p..."
scene ep11_freeroam_party_pr3
mc "Professor Hoff. I'm surprised to see you here. Uh... How can I help you?"
ph "..."
scene ep11_freeroam_party_pr4 with dissolve
ph "Good evening, [name]. May I have a word with you?"
scene ep11_freeroam_party_pr5 with dissolve
mc "Yeah! Just a moment!"
$ renpy.sound.set_volume(0.1,channel='music',delay=1.0)
play sound "sound_effects/door_close.mp3"
scene ep11_freeroam_party_pr6 with dissolve
mc "It's chilly outside tonight."
scene ep11_freeroam_party_pr7 with dissolve
ph "Indeed. I can't wait to get back inside my warm car."
ph "I was about to leave my office when a concerned student approached me."
scene ep11_freeroam_party_pr8 with dissolve
ph "This student was worried that there was an ongoing party at your fraternity with alcohol and drugs."
menu:
    "We do have a party":
        scene ep11_freeroam_party_pr10 with dissolve
        mc "Yes, we are having a Christmas party for the frat to celebrate the upcoming holiday."
        scene ep11_freeroam_party_pr11 with dissolve
        ph "Ah. Yes, it's almost Christmas, isn't it? Days fly by so fast."
    "There's no party here":
        scene ep11_freeroam_party_pr10 with dissolve
        mc "There's no party here."
        scene ep11_freeroam_party_pr12 with dissolve
        ph "I may be old, but my ears do not deceive me. I can tell from the music that you are celebrating."
        ph "[name], you don't have to act as if hosting a party is illegal."
        ph "It's the report of alcohol and drugs that has me concerned."
    "Who was the student?":
        scene ep11_freeroam_party_pr10 with dissolve
        mc "Who was the student?"
        scene ep11_freeroam_party_pr12 with dissolve
        ph "As you can understand, they asked me to be discrete about the matter."
        scene ep11_freeroam_party_pr10 with dissolve
        mc "Yeah, yeah. I get it."
        scene ep11_freeroam_party_pr12 with dissolve

ph "I could have let campus security handle it, but I figured I could make a quick stop here before bothering them."
scene ep11_freeroam_party_pr10 with dissolve
menu:
    "No alcohol or drugs here":
        mc "You don't have to bother security. There is neither alcohol nor drugs in here."
        mc "We're just a bunch of students having fun before finals and Christmas break."
        scene ep11_freeroam_party_pr11 with dissolve
        ph "That's all I needed to hear."
    "No drugs here":
        mc "You don't have to bother security. There are no drugs in here."
        scene ep11_freeroam_party_pr11 with dissolve
        ph "And the alcohol?"
        scene ep11_freeroam_party_pr10 with dissolve
        mc "..."
        mc "There may be some alcohol..."
        scene ep11_freeroam_party_pr11 with dissolve
        ph "Is everyone in there ok?"
        scene ep11_freeroam_party_pr10 with dissolve
        mc "Yes. There's nothing to worry about."
        mc "We're just a bunch of students having fun before finals and Christmas break."
        scene ep11_freeroam_party_pr11 with dissolve
        ph "That's all I needed to hear."
scene ep11_freeroam_party_pr12 with dissolve
ph "Well, you have a good night-"
scene ep11_freeroam_party_pr13
tan "Woho! We're here! It's frickin freezing! Let us in!!!"
play sound "sound_effects/season3/door_open.mp3"
$ renpy.sound.set_volume(1.0,channel='music',delay=2.0)
scene ep11_freeroam_party_pr14 with dissolve
mc "Head inside... I'll be with you soon."
scene ep11_freeroam_party_pr15 with dissolve
sn "[name]! Grr! Nice coat!"
scene ep11_freeroam_party_pr16 with dissolve
$ renpy.pause()
$ renpy.sound.set_volume(0.1,channel='music',delay=1.0)
play sound "sound_effects/door_close.mp3"
$ guideSuggestedPage = 202
scene ep11_freeroam_party_pr12 with dissolve
ph "Um. Are those girls students here?"
scene ep11_freeroam_party_pr8 with dissolve
mc "..."
menu:
    "Yes":
        scene ep11_freeroam_party_pr9 with dissolve
        mc "Yes. It's a big school."
        scene ep11_freeroam_party_pr12 with dissolve
        ph "Hm... Not really. But I struggle to keep up these days."
    "They are strippers":
        scene ep11_freeroam_party_pr9 with dissolve
        mc "No. They are strippers."
        scene ep11_freeroam_party_pr17 with dissolve
        $ renpy.pause()
        scene ep11_freeroam_party_pr18 with dissolve
        ph "Hahaha!"
        scene ep11_freeroam_party_pr19 with dissolve
        mc "Hahaha!"
        scene ep11_freeroam_party_pr12 with dissolve
ph "Have a nice Christmas party, [name]."
scene ep11_freeroam_party_pr20
hide screen ep10_snow_screen
with dissolve
play sound "sound_effects/door_close.mp3"
$ renpy.sound.set_volume(1.0,channel='music',delay=1.0)
mc "*{i}Phew{/i}*"
$ new_bio("Philip", "A concerned student alerted Professor Hoff that there was a party at the DIKs'. I tried my best to handle the situation, and he left without calling security.")

scene ep11_freeroam_party_pr21 with dissolve
mc "You girls have no idea how close you were to blowing it."
scene ep11_freeroam_party_pr22 with dissolve
sn "What do you want me to blow, cutie?"
scene ep11_freeroam_party_pr23 with dissolve
mc "Welcome to the party, Sandy..."
if ep11_pp_contest == 0 or ep11_pp_contest == 1:
    mc "Grab a secret mission from The Dirty Bowl and enjoy yourselves. A competition is about to start."
else:
    mc "Grab a secret mission from The Dirty Bowl and enjoy yourselves."

if branchAlone and ep10_date_nicole and not ep10_cancel_date_nicole:
    scene ep11_freeroam_party_pr24 with dissolve
elif ep11_pp_contest == 2:
    stop music fadeout 3
    scene ep11_freeroam_party_pr24 with dissolve
else:
    scene ep11_freeroam_party_pr24 with dissolve
tan "Come on, girls! Let's get wasted!"

if branchAlone and ep10_date_nicole and not ep10_cancel_date_nicole:
    scene ep11_freeroam_party_pr25 with dissolve
    nic "Was that your neighbor out there?"
    scene ep11_freeroam_party_pr27 with dissolve
    mc "Worse. It was a Professor. Our neighbors are cool."
    scene ep11_freeroam_party_pr26 with dissolve
    nic "I assume you'd have to be to live next to a frat."
    nic "Did we get you in any trouble with that Professor?"
    scene ep11_freeroam_party_pr28 with dissolve
    mc "No. But someone else almost did."
    mc "If you're heading outside tonight, no visible drinks, ok? There might be campus security hanging around."
    scene ep11_freeroam_party_pr29 with dissolve
    nic "If you think I'm going outside wearing this, you should think again. I'm staying inside until another taxi comes to pick me up, haha."
    scene ep11_freeroam_party_pr30 with dissolve
    mc "Yep... You can't go outside wearing that."
    scene ep11_freeroam_party_pr31 with dissolve
    nic "Cute coat. Is this what you wear to bed these days?"
    scene ep11_freeroam_party_pr32 with dissolve
    mc "Haha, yeah. I'm a sucker for women's clothes. Didn't I tell you?"
    nic "Haha, nice underwear. Your boxers leave little to the imagination."
    scene ep11_freeroam_party_pr33 with dissolve
    mc "Maybe it's because you don't have to imagine."
    scene ep11_freeroam_party_pr35 with dissolve
    nic "*{i}Smack{/i}*"
    scene ep11_freeroam_party_pr36 with dissolve
    $ renpy.pause()
    scene ep11_freeroam_party_pr34 with dissolve
    nic "I'm going to get a drink with the girls."
    if ep11_pp_contest == 2:
        stop music fadeout 3
    scene ep11_freeroam_party_pr33 with dissolve
    mc "You do that. I'll catch you later."
if ep11_pp_contest == 0:
    jump ep11_pp_tshirt_event_label
elif ep11_pp_contest == 1:
    jump ep11_pp_suck_event_label
else:
    jump ep11_main_party_label


label ep11_pp_tshirt_event_label:
scene ep11_pp_tshirt_event1 with dissolve
de "All good?"
stop music fadeout 3
scene ep11_pp_tshirt_event2 with dissolve
mc "Yep. It's time to entertain our guests."
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track125.mp3","music/ep10/licensed_music/track148.mp3"])
scene ep11_pp_tshirt_event3 with dissolve
mc "Welcome to the party! Is everyone having fun?"
scene ep11_pp_tshirt_event4 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event5 with dissolve
mc "I'm happy to see this many of you here. And I'm also happy to see this much of you."
mc "Usually, I have to imagine the audience naked when I'm giving a presentation, but you're making my life easy tonight."
scene ep11_pp_tshirt_event8 with dissolve
"*{i}Laughter{/i}*"
scene ep11_pp_tshirt_event5 with dissolve
mc "All joking aside, it's awesome that you all could come. And I heard that some of you came twice."
mc "For those who don't know how we do it here, we like to go crazy, and tonight is no different."
scene ep11_pp_tshirt_event6 with dissolve
mc "You've already gotten a task from The Dirty Bowl, and if you haven't, grab one ASAP."
mc "I hear that some of those tasks are pretty damned crazy and that there are some consequences for not completing them... Is that right, Derek?"
scene ep11_pp_tshirt_event7 with dissolve
de "Yep. Big consequences. Huge! You better finish your missions by midnight, is all I'm gonna say."
scene ep11_pp_tshirt_event6 with dissolve
mc "I don't like the sound of that. But we will have a competition right now, which might solve your problem for tonight."
scene ep11_pp_tshirt_event9 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event10 with dissolve
mc "We have beers and white T-shirts here. Put them together and you'll get a wet T-shirt competition!"
play sound "sound_effects/season2/drink_splash.mp3"
scene ep11_pp_tshirt_event11 with dissolve
mc "The rules are simple. Four topless girls put on a T-shirt. Derek and I will pour beer on them, and the crowd will decide on the winner by cheering the loudest for their favorite."
scene ep11_pp_tshirt_event12 with dissolve
mc "Any willing participants?"
mc "None? I heard a lot of cheers before."
scene ep11_pp_tshirt_event13 with dissolve
mc "Well... To give you an incentive to join... Every girl who participates gets out of doing their Dirty Bowl mission."
mc "Yep, you heard that correctly. All you need to do is get a beer poured on your chest while dressed in a T-shirt to get out of that one."
scene ep11_pp_tshirt_event14 with dissolve
mc "Oh, I see some hands in the audience now!"
cam "Woo!!!"
mc "Camila? Do you want to join? Get up here!"
scene ep11_pp_tshirt_event13 with dissolve
mc "Give it up for Camila, everyone!"

scene ep11_pp_tshirt_event21 with dissolve
"*{i}Cheers{/i}*"

scene ep11_pp_tshirt_event20 with dissolve
de "Christie is raising her hand."
mc "Oh, yeah! Christie, come on up."
scene ep11_pp_tshirt_event13 with dissolve
mc "We need two more girls!"
scene ep11_pp_tshirt_event19 with dissolve
tm "Sandy should do it!"
scene ep11_pp_tshirt_event22 with dissolve
sn "Aw, was that Tommy chanting my name!?"
scene ep11_pp_tshirt_event15 with dissolve
$ renpy.pause()
scene ep11_pp_tshirt_event23 with dissolve
mc "How about it, Sandy?"
scene ep11_pp_tshirt_event24 with dissolve
sn "Fuck it, it's a party! But I was excited about the mission I pulled, too."
scene ep11_pp_tshirt_event16 with dissolve
he "I'll do it!"
scene ep11_pp_tshirt_event13 with dissolve
mc "And Heather is the final contestant. We have our girls."
mc "Get behind the Christmas tree and change into your T-shirt. You have to be topless underneath it."
scene ep11_pp_tshirt_event17 with dissolve
tm "Haha! Girls are already in their underwear, and [name] is making them wear more clothes."
scene ep11_pp_tshirt_event18 with dissolve
gi "Hahaha! Yeah, what the hell is that about?"
scene ep11_pp_tshirt_event17 with dissolve
tm "I know... You can't hate the guy. He's funny without realizing it."

scene ep11_pp_tshirt_event25 with dissolve
mc "It looks like we are ready! Remember to cheer loudly for your favorite."
scene ep11_pp_tshirt_event26 with dissolve
mc "Derek, get ready!"
mc "Three, two, one... POUR!!!"
play sound "sound_effects/season2/drink_splash.mp3"
scene ep11_pp_tshirt_event27 with vpunch
cam "Ah!!! Hahaha!"
scene ep11_pp_tshirt_event28 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/drink_splash.mp3"
scene ep11_pp_tshirt_event29 with vpunch
chr "Oh! That's cold!!!"
scene ep11_pp_tshirt_event30 with dissolve
$ renpy.pause()
scene ep11_pp_tshirt_event31 with dissolve

menu:
    "Pour more on Sandy":
        $ ep11_tshirt_winner = "Sandy"
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event32 with vpunch
        $ renpy.pause()
        scene ep11_pp_tshirt_event33 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event35 with vpunch
        $ renpy.pause()
        scene ep11_pp_tshirt_event36 with dissolve
        $ renpy.pause()
    "Pour more on Heather":
        $ ep11_tshirt_winner = "Heather"
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event32 with vpunch
        mc "*{i}Psst{/i}* I'll make sure that you win."
        scene ep11_pp_tshirt_event34 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event35 with vpunch
        $ renpy.pause()
        scene ep11_pp_tshirt_event37 with dissolve
        $ renpy.pause()
    "Pour a little on both":
        $ ep11_tshirt_winner = "Camila"
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event32 with vpunch
        $ renpy.pause()
        scene ep11_pp_tshirt_event33 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/drink_splash.mp3"
        scene ep11_pp_tshirt_event35 with vpunch
        $ renpy.pause()
        scene ep11_pp_tshirt_event37 with dissolve
        $ renpy.pause()
if ep11_tshirt_winner == "Sandy":
    scene ep11_pp_tshirt_event38 with dissolve
else:
    scene ep11_pp_tshirt_event39 with dissolve
mc "Up on the chairs, girls! Let everyone see those T-shirts."
scene ep11_pp_tshirt_event40 with dissolve
"*{i}Cheers{/i}*"
mc "I can't hear you. Who's your favorite? Shout louder!!!"
scene ep11_pp_tshirt_event41 with dissolve
mc "Is it Camila!?"
scene ep11_pp_tshirt_event42 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event43 with dissolve
mc "Is it Christie!?"
scene ep11_pp_tshirt_event44 with dissolve
"*{i}Cheers{/i}*"
if ep11_tshirt_winner == "Heather":
    scene ep11_pp_tshirt_event45 with dissolve
else:
    scene ep11_pp_tshirt_event45b with dissolve
mc "Or is it Heather!?"
if ep11_tshirt_winner == "Heather":
    scene ep11_pp_tshirt_event46 with dissolve
else:
    scene ep11_pp_tshirt_event46b with dissolve
"*{i}Cheers{/i}*"
if ep11_tshirt_winner == "Sandy":
    scene ep11_pp_tshirt_event47 with dissolve
else:
    scene ep11_pp_tshirt_event47b with dissolve
mc "Is it Sandy!?"
if ep11_tshirt_winner == "Sandy":
    scene ep11_pp_tshirt_event48 with dissolve
else:
    scene ep11_pp_tshirt_event48b with dissolve
sn "Of course, it's me!!!"
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event49 with dissolve
mc "I've seen what I needed to see and heard what I needed to hear."
mc "It's clear from your shouting that the winner is..."
if ep11_tshirt_winner == "Camila":
    scene ep11_pp_tshirt_event52 with dissolve
    mc "[ep11_tshirt_winner]!!!"
    "*{i}Cheers{/i}*"
    cam "WOOO!!! I won! I won!!!"
elif ep11_tshirt_winner == "Sandy":
    scene ep11_pp_tshirt_event50 with dissolve
    mc "[ep11_tshirt_winner]!!!"
    "*{i}Cheers{/i}*"
    sn "Yay me!!!"
else:
    scene ep11_pp_tshirt_event51 with dissolve
    mc "[ep11_tshirt_winner]!!!"
    "*{i}Cheers{/i}*"

scene ep11_pp_tshirt_event49 with dissolve
mc "A thank you to all contestants. You've been brave tonight!"
mc "Now, who's up for another round?"
stop music fadeout 3
scene ep11_pp_tshirt_event4b with dissolve
"*{i}Cheers{/i}*"
if minigames:
    scene ep11_pp_tshirt_event10b with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
    $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
    $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
    $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
    $ mphone_pp_history_list.append("• The {color=ffed00}Wet T-shirt Competition{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Wet T-shirt Competition{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Wet T-shirt Competition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Wet T-shirt Competition{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Wet T-shirt Competition{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg

jump ep11_main_party_label

label ep11_pp_suck_event_label:
scene ep11_pp_tshirt_event1 with dissolve
de "All good?"
stop music fadeout 3
scene ep11_pp_tshirt_event2 with dissolve
mc "Yep. It's time to entertain our guests."
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track125.mp3","music/ep10/licensed_music/track148.mp3"])
scene ep11_pp_suck_event1 with dissolve
mc "Welcome to the party! Is everyone having fun?"
scene ep11_pp_tshirt_event4 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event5 with dissolve
mc "I'm happy to see this many of you here. And I'm also happy to see this much of you."
mc "Usually, I have to imagine the audience naked when I'm giving a presentation, but you're making my life easy tonight."
scene ep11_pp_tshirt_event8 with dissolve
"*{i}Laughter{/i}*"
scene ep11_pp_tshirt_event5 with dissolve
mc "All joking aside, it's awesome that you all could come. And I heard that some of you came twice."
mc "For those of you who don't know how we do it here, we like to go crazy and tonight is no different."
scene ep11_pp_tshirt_event6 with dissolve
mc "You've already gotten a task from The Dirty Bowl, and if you haven't, grab one ASAP."
mc "I hear that some of those tasks are pretty damned crazy and that there are some consequences for not completing them... Is that right, Derek?"
scene ep11_pp_tshirt_event7 with dissolve
de "Yep. Big consequences. Huge! You better finish your missions by midnight, is all I'm gonna say."
scene ep11_pp_tshirt_event6 with dissolve
mc "I don't like the sound of that. But we're going to have a competition right now, that might solve your problem for tonight."
scene ep11_pp_tshirt_event9 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_tshirt_event12 with dissolve
mc "This competition is sponsored by Arieth. Give it up for Arieth, everyone."
scene ep11_pp_suck_event2 with dissolve
mc "She's out here selling sex toys and such all night. If you're looking to get something private for your privates, talk to her later tonight."
scene ep11_pp_suck_event3 with dissolve
mc "Now, you're looking at the dildos on the chairs and wondering what the hell is going on."
scene ep11_pp_suck_event4 with dissolve
mc "You're nervous, maybe scared... Some of you might even be aroused. Don't worry, just like Arieth, we won't judge you."
mc "Girls will suck on these dildos in front of guys sitting on these chairs, and the last guy standing - figuratively - loses."
scene ep11_pp_tshirt_event12 with dissolve
mc "We'll need four girls and four guys on the stage for this competition. Any volunteers?"
scene ep11_pp_suck_event5 with dissolve
$ renpy.pause()
scene ep11_pp_tshirt_event12 with dissolve
mc "Wow! Not a single volunteer... We did so expect that."
mc "And that's why every contestant will get rewarded."
scene ep11_pp_tshirt_event13 with dissolve
mc "That's right! The four guys and girls who participate will get out of their Dirty Bowl mission for tonight and avoid the consequences."
scene ep11_pp_suck_event4 with dissolve
"*{i}Chatter{/i}*"
mc "Aha, that got you all talking. So, how about it? Who are the guys for this?"
scene ep11_pp_suck_event16 with dissolve
che "I'll fucking do it!"
scene ep11_pp_suck_event4 with dissolve
mc "Chen, come on up here. Who else?"
scene ep11_pp_suck_event17 with dissolve
mc "Jamie? I see you over there looking tempted."
scene ep11_pp_suck_event18 with dissolve
jm "Yeah, but I already did my mission."
scene ep11_pp_suck_event17 with dissolve
mc "You can give your pass to whoever you'd like. Now that's a nice reward, yeah?"
scene ep11_pp_suck_event18 with dissolve
jm "Well, alright."
scene ep11_pp_suck_event17 with dissolve
mc "And Jamie's on board. Give it up for our contestants!"
scene ep11_pp_tshirt_event21 with dissolve
"*{i}Cheers{/i}*"
scene ep11_pp_suck_event6 with dissolve
mc "Tommy? Are you up for it?"
scene ep11_pp_suck_event7 with dissolve
mc "Looks like he is! And it looks like we have our first female contestant, too. Gina!"
scene ep11_pp_tshirt_event15 with dissolve
$ renpy.pause()
scene ep11_pp_suck_event4 with dissolve
mc "Who else? It's just a boner, people. I bet you've all seen plenty of those at the party already."
scene ep11_pp_suck_event8 with dissolve
mc "(No more guys seem to be up for it...)"
if (ep11_maya_love > 0 or ep11_josy_love > 0) and wt_ep9_branch_numbers == 1:
    jump ep11_pp_d_vol_label

if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
menu:
    "Do it yourself \n{size=-4}[m_c1][mod_choices[6]]":
        scene ep11_pp_suck_event9 with dissolve
        $ ep11_dildo_sucking = True
        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
            $ tc += 1
        mc "Since no one wants to do it, I will have to volunteer. The show must go on!"
    "Volunteer Derek":
        label ep11_pp_d_vol_label:
        $ ep11_dildo_sucking = False
        scene ep11_pp_suck_event9 with dissolve
        mc "Since no one wants to do it, Derek will volunteer."
        scene ep11_pp_suck_event10 with dissolve
        de "Apparently, I will."
        scene ep11_pp_suck_event9 with dissolve

mc "Now for the rest of the girls. I saw a lot of eager hands in the air before."
scene ep11_pp_suck_event11 with dissolve
mc "Chen? Who do you want in front of you?"
scene ep11_pp_suck_event12 with dissolve
che "That one."
scene ep11_pp_suck_event14 with dissolve
mc "\"That one\"... She has a name."
scene ep11_pp_suck_event13 with dissolve
che "Well, I don't know it!"
scene ep11_pp_suck_event15 with dissolve
mc "I actually don't know it either... So, yeah, that one..."
scene ep11_pp_suck_event19 with dissolve
jm "Can I have Christie?"
scene ep11_pp_suck_event20 with dissolve
mc "That's up to Christie to decide."
scene ep11_pp_suck_event22 with dissolve
chr "Sure, I'm game."
if not ep11_dildo_sucking:
    scene ep11_pp_suck_event20 with dissolve
    mc "And for Derek, I'm choosing Ashley."
    scene ep11_pp_suck_event21 with dissolve
    de "Bro..."
else:
    scene ep11_pp_suck_event20 with dissolve
    mc "And that leaves me..."
    scene ep11_pp_suck_event27 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event30 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event24 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event31 with dissolve
    menu:
        "Bianca":
            label ep11_pp_suckb_event_label:
            $ ep11_dildo_sucking_girl = "Bianca"
            scene ep11_pp_suck_event27 with dissolve
            mc "Bianca. I didn't realize you wanted to get out of that mission this badly. Get up here."
            scene ep11_pp_suck_event28 with dissolve
            car "You're crazy for this."
            scene ep11_pp_suck_event29 with dissolve
            bia "Relax, I will be sucking on a piece of rubber. It's not a big deal."
        "Heather":
            scene ep11_pp_suck_event30 with dissolve
            mc "(Heather looks fuming and determined... Likely because of Tommy being up here.)"
            if ep9_heather_lewd == 2:
                mc "(But Tommy would kill me if I picked her... It's not worth it tonight.)"
                menu:
                    "Bianca":
                        jump ep11_pp_suckb_event_label
                    "Zoey":
                        jump ep11_pp_suckz_event_label
            $ ep11_dildo_sucking_girl = "Heather"
            mc "Heather, get up here. I choose you."
            scene ep11_pp_suck_event32 with dissolve
            $ renpy.pause()
        "Zoey":
            label ep11_pp_suckz_event_label:
            $ ep11_dildo_sucking_girl = "Zoey"
            scene ep11_pp_suck_event23 with dissolve
            mc "Zoey? Will you help me out here?"
            scene ep11_pp_suck_event25 with dissolve
            zo "Huh? Why?"
            scene ep11_pp_suck_event26 with dissolve
            mc "Come on."
            scene ep11_pp_suck_event33 with dissolve
            zo "Are you sure you want to do this?"
            menu:
                "Yeah":
                    scene ep11_pp_suck_event34 with dissolve
                    if branchAlone:
                        mc "Yeah. Why not? It's going to be fun."
                    else:
                        mc "Yeah. It's just a stupid competition anyway."
                "I feel like I have to":
                    scene ep11_pp_suck_event34 with dissolve
                    mc "With my position here, I feel like I have to. It was my idea to have this at the party."
            mc "I can pick someone else if you don't want to do it."
            scene ep11_pp_suck_event33 with dissolve
            zo "No, I'll do it."

if not ep11_dildo_sucking:
    scene ep11_pp_suck_event35 with dissolve
    mc "On your marks... Get set... Blow!"
    "*{i}Cheers{/i}*"
    scene ep11_pp_suck_event36 with dissolve
    mc "Keep your hands to yourselves, guys. There will be no touching the girl in this competition."
    mc "And always look at what she's doing in front of you. It's all about how much they can visually tease you."
    scene ep11_pp_suck_event37 with dissolve
    mc "And we're doing this the honorable way. The girls will yell when their partner loses."
    scene ep11_pp_suck_event38 with dissolve
    mc "You heard me. I'm not going around to check what's in your underwear. That would likely prolong the competition, too."
    "*{i}Laughter{/i}*"
    scene ep11_pp_suck_event39 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event40 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event41 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event42 with dissolve
    ash "Whoa... You're out already?"
    scene ep11_pp_suck_event44 with dissolve
    de "Yeah... You're my kryptonite."
    scene ep11_pp_suck_event42 with dissolve
    ash "Want me to tell them?"
    scene ep11_pp_suck_event45 with dissolve
    de "Not yet."
    scene ep11_pp_suck_event43 with dissolve
    $ renpy.pause()
    scene ep11_pp_suck_event46 with dissolve
    che "You call that sucking? Put some effort into it."
    che "Even I can suck a cock better than that."
    scene ep11_pp_suck_event47 with dissolve
    tm "There you go. Work it."
    scene ep11_pp_suck_event48 with dissolve
    tm "Don't forget the balls."
    scene ep11_pp_suck_event49 with dissolve
    jm "Oh, man... I haven't had sex in a long time..."
    scene ep11_pp_suck_event50 with dissolve
    jm "Ahhh..."
    scene ep11_pp_suck_event51 with dissolve
    chr "He's hard!"
    scene ep11_pp_suck_event52 with dissolve
    mc "Our first pair crosses the finish line. Jamie and Christie!"
    "*{i}Cheers{/i}*"
    scene ep11_pp_suck_event53 with dissolve
    ash "We're out over here, too."
    scene ep11_pp_suck_event54 with dissolve
    mc "And immediately after, Derek and Ashley."
    mc "Amazing job from the girls here tonight."
    scene ep11_pp_suck_event55 with dissolve
    mc "We're down to two couples. Which couple will lose?"
    scene ep11_pp_suck_event56 with dissolve
    tm "I'm getting a semi here. Keep going."
    scene ep11_pp_suck_event57 with dissolve
    che "Gah! What's wrong with you? Are you pretending that the dildo is your dad?"
    scene ep11_pp_suck_event58 with dissolve
    gi "Done."
    "*{i}Cheers{/i}*"
    scene ep11_pp_suck_event59 with dissolve
    mc "And there we have it! Tommy and Gina cross the finish line."
    scene ep11_pp_suck_event60 with dissolve
    mc "It was a good try, but it looks like everyone but Chen is a winner tonight."
    scene ep11_pp_suck_event62 with dissolve
    che "Nothing happened downstairs. Nothing!"
    scene ep11_pp_suck_event61 with dissolve
    mc "You had a lovely partner, so I'm sure that's entirely your fault."
    scene ep11_pp_suck_event63 with dissolve
    stop music fadeout 3
    mc "Now that the first round is over and done with... Who is up for round two?"
    "*{i}Cheers{/i}*"
else:
    if ep11_dildo_sucking_girl == "Bianca":
        scene ep11_pp_suck_event64 with dissolve
    elif ep11_dildo_sucking_girl == "Heather":
        scene ep11_pp_suck_event64b with dissolve
    else:
        scene ep11_pp_suck_event64c with dissolve
    de "Is everyone ready? 3-2-1-Suck on it!"
    scene ep11_pp_suck_event65 with dissolve
    "*{i}Cheers{/i}*"
    de "And we're off! Who will be the first one to pop a rod?"
    if ep11_dildo_sucking_girl == "Bianca":
        scene ep11_pp_suck_event66 with dissolve
    elif ep11_dildo_sucking_girl == "Heather":
        scene ep11_pp_suck_event66b with dissolve
    else:
        scene ep11_pp_suck_event66c with dissolve
    "*{i}Cheers{/i}*"
    de "The girls are certainly working it!"
    scene ep11_pp_suck_event47 with dissolve
    de "A reminder to the guys, just like in a strip club - that most of us never go to - you're not allowed to touch your partner."
    scene ep11_pp_suck_event39 with dissolve
    de "And girls, it doesn't count if the guys in the audience get hard; it has to be your partner."

    if ep11_dildo_sucking_girl == "Bianca":
        scene ep11_pp_suck_event70 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event71 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event72 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event73 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event74 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event75 with dissolve
        bia "Ok, this felt weirder than I thought it would. Haha..."
        scene ep11_pp_suck_event76 with dissolve
        bia "I'll still get out of the mission, even if we lose, right?"
        scene ep11_pp_suck_event77 with dissolve
        menu:
            "Yeah, you will":
                mc "Yeah, you will."
                scene ep11_pp_suck_event76 with dissolve
                bia "That's good."
            "I don't think we will lose":
                mc "Yeah, but I don't think we will lose."
                scene ep11_pp_suck_event78 with dissolve
                bia "Stop it."
                scene ep11_pp_suck_event79 with dissolve
                mc "What? You're doing good."
        scene anim_suck_bianca_ep11 with dissolve
        pause
    elif ep11_dildo_sucking_girl == "Heather":
        scene ep11_pp_suck_event97 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event96 with dissolve
        he "*{i}Suck suck{/i}*"
        scene anim_suck_heather_ep11 with dissolve
        pause
    elif ep11_dildo_sucking_girl == "Zoey":
        scene ep11_pp_suck_event106 with dissolve
        zo "Heh. Arieth got the size right."
        scene ep11_pp_suck_event107 with dissolve
        mc "Yeah, it's close, haha."
        scene ep11_pp_suck_event108 with dissolve
        zo "Yours is thicker, though. And not as pale."
        scene ep11_pp_suck_event109 with dissolve
        mc "And not as plastic."
        scene ep11_pp_suck_event110 with dissolve
        zo "So, um... I should start."
        scene ep11_pp_suck_event111 with dissolve
        zo "This reminds me of that night at the basketball court. Remember?"
        scene ep11_pp_suck_event112 with dissolve
        mc "How could I ever forget? There were no people there, though."
        scene ep11_pp_suck_event119 with Dissolve(2)
        mc "Of course, I'm horny, but we're in public."
        scene ep11_pp_suck_event120 with dissolve
        zo "It's 3 AM. Stop being a sissy. People are asleep."
        scene ep11_pp_suck_event121 with dissolve
        mc "We should be heading home..."
        scene ep11_pp_suck_event122 with dissolve
        zo "Dude... Don't tell me we should be heading home when I'm on my knees about to blow you. That's a turn-off."
        scene ep11_pp_suck_event123 with dissolve
        zo "Let me do this for you."
        scene anim_zoey_suck1_ep11 with dissolve
        pause

    scene ep11_pp_suck_event46b with dissolve
    che "You call that sucking? Put some effort into it."
    che "Even I can suck cock better than that."
    scene ep11_pp_suck_event47 with dissolve
    tm "There you go. Work it. Don't forget the balls."
    scene ep11_pp_suck_event49 with dissolve
    jm "Oh, man... I haven't had sex in a long time..."
    scene ep11_pp_suck_event50 with dissolve
    jm "Ahhh..."
    scene ep11_pp_suck_event51 with dissolve
    chr "He's hard!"
    scene ep11_pp_suck_event67 with dissolve
    de "And just like that, Jamie popped a rod and wins the competition. But he couldn't have done it without Christie!"
    "*{i}Cheers{/i}*"

    if ep11_dildo_sucking_girl == "Bianca":
        scene anim_suck_bianca2_ep11 with dissolve
        pause
        scene ep11_pp_suck_event80 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event81 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event82 with dissolve
        bia "Whoa... You're growing."
    elif ep11_dildo_sucking_girl == "Heather":
        scene anim_suck_heather_ep11 with dissolve
        pause
        scene anim_suck_heather2_ep11 with dissolve
        he "*{i}Suck suck{/i}*"
        pause
        scene ep11_pp_suck_event98 with dissolve
        he "Are you getting anything?"
        scene ep11_pp_suck_event99 with dissolve
        mc "Some, but not much. I see the back of your head go up and down, but it doesn't do much for me when I don't feel it. Do you get what I mean?"
        scene ep11_pp_suck_event100 with dissolve
        he "How about this?"
        scene anim_boob_heather_ep11 with dissolve
        mc "Damn... That's very hot. Much better."
        pause
        scene ep11_pp_suck_event101 with dissolve
        mc "Oh..."
        scene ep11_pp_suck_event102 with dissolve
        he "Don't have me lose to Gina, [name]. Get hard for me."

    scene ep11_pp_suck_event56 with dissolve
    tm "I'm getting a semi here. Keep going."
    if not ep11_dildo_sucking:
        scene ep11_pp_suck_event57 with dissolve
    else:
        scene ep11_pp_suck_event46b with dissolve
    che "Gah! What's wrong with you? Are you pretending that the dildo is your dad?"

    if ep11_dildo_sucking_girl == "Heather":
        scene ep11_pp_suck_event103 with dissolve
        he "Mmm... [name]. Look how I pinch my nipple for you. You like that, don't you?"
        mc "Almost there...keep going."
        scene ep11_pp_suck_event104 with dissolve
        he "This dick could be yours, [name]. Lodged right between my tits. I'd make you cum good all over them."
        scene ep11_pp_suck_event105 with dissolve
        he "Done!!!"
        "*{i}Cheers{/i}*"
        scene ep11_pp_suck_event87 with dissolve
        de "Wow! Heather sure went for it. What a performance."
        de "[name] is hard. I didn't have to announce it; you could see that from the back row."
        "*{i}Cheers{/i}*"


    scene ep11_pp_suck_event68 with dissolve
    gi "Done."
    "*{i}Cheers{/i}*"
    scene ep11_pp_suck_event69 with dissolve
    de "Tommy and Gina, everybody!"

    if ep11_dildo_sucking_girl == "Bianca":
        scene ep11_pp_suck_event83 with dissolve
        bia "Holy cow... If that's not hard, I don't wanna know what it is like."
        scene ep11_pp_suck_event84 with dissolve
        mc "Yep, it's up."
        scene ep11_pp_suck_event85 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event86 with dissolve
        de "Bianca is done! [name] is hard. I didn't have to announce it; you can see that from the back row."
        "*{i}Cheers{/i}*"
    elif ep11_dildo_sucking_girl == "Zoey":
        scene anim_zoey_suck1_ep11 with dissolve
        pause
        scene anim_zoey_suck2_ep11 with dissolve
        pause
        mc "Zoey... I'm cumming."

        scene ep11_pp_suck_event113 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event114 with dissolve
        $ renpy.pause()
        scene ep11_pp_suck_event115 with dissolve
        zo "Should I say something?"
        scene ep11_pp_suck_event116 with dissolve
        mc "Uh... Yeah."
        scene ep11_pp_suck_event117 with dissolve
        zo "Derek?"

        scene ep11_pp_suck_event88 with dissolve
        de "Zoey is done! [name] is hard. I didn't have to announce it; you can see that from the back row."
        "*{i}Cheers{/i}*"
        scene ep11_pp_suck_event89 with dissolve
        zo "I can stand here for as long as you need."
        scene ep11_pp_suck_event91 with dissolve
        mc "You don't have to do that. It's not easier to get it down with this view."
        scene ep11_pp_suck_event90 with dissolve
        $ renpy.pause()

    scene ep11_pp_suck_event92 with dissolve
    de "Which means that Chen has lost this round."
    scene ep11_pp_suck_event62 with dissolve
    che "Nothing happened downstairs. Nothing!"

    if ep11_dildo_sucking_girl == "Bianca":
        scene ep11_pp_suck_event93 with dissolve
        if branchJill:
            car "Not a big deal? You intentionally got Jill's boyfriend hard."
        else:
            car "Not a big deal? You intentionally got a guy hard doing that. I don't think Matthew would have liked to see it."
        scene ep11_pp_suck_event94 with dissolve
        bia "I wasn't thinking, ok? It doesn't mean anything; don't make such a big deal out of it."

    if ep11_dildo_sucking_girl == "Bianca":
        $ new_bio("Bianca", "I volunteered for the Dildo Sucking Competition and chose Bianca as my partner. It was sexy...")
    elif ep11_dildo_sucking_girl == "Heather":
        $ new_bio("Heather", "I volunteered for the Dildo Sucking Competition and chose Heather as my partner. It was sexy...")
    else:
        $ new_bio("Zoey", "I volunteered for the Dildo Sucking Competition and chose Zoey as my partner. It was sexy...")
    scene ep11_pp_suck_event95 with dissolve
    stop music fadeout 3
    de "I think we have time for another round. Can we get some new contestants on stage?"
    "*{i}Cheers{/i}*"

if minigames:
    scene ep11_pp_suck_event3 with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
    $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
    $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)

    $ mphone_pp_history_list.append("• The {color=ffed00}Dildo Sucking Competition{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Dildo Sucking Competition{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Dildo Sucking Competition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Dildo Sucking Competition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg
jump ep11_main_party_label

label ep11_pp_part2_event_label:
scene ep11_main_party1b with dissolve
mc "(They're having an underwear party too?)"
mc "(Damn, I wish I could be there for it...)"

#wt_ep11_party_bella

if wt_ep9_branch_numbers != 1:

    if persistent.mod_wtenabled:
                            $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                            #[mod_gr][mod_choices[0]]
                            #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                            if branchSage and ep11_cammy_draught and sage_dik > 0:
                               $ mod_choices[6]="(Possible Sage/Camila threesome)"
                               $ mod_choices[7]="(+5 Cheater)"
                            "scrappy" "Leaving the party means you could miss Elena's scene and kissing Sally."
        
        
        
    menu:
            "Mod: Do both":
                $ wt_ep11_party_bella = True
                scene ep11_main_party6b with dissolve
                mc "(No, what am I thinking? I'm having fun here and I can't ask Derek to take care of everything. I'm staying.)"
                $ new_bio("You", "I decided to stay at the DIKs' Christmas Panty Party and go to Bella's later.")
            "Stay at the party":
                $ ep11_mg_party = False
                scene ep11_main_party6b with dissolve
                mc "(No, what am I thinking? I'm having fun here and I can't ask Derek to take care of everything. I'm staying.)"
                $ new_bio("You", "I decided to stay at the DIKs' Christmas Panty Party.")
            "Go to Bella's party \n{size=-4}[m_c1][mod_choices[6]]":
                $ ep11_mg_party = True
                scene ep11_main_party6b with dissolve
                mc "(Yeah, fuck it. I'll find a way to leave this party early.)"
                $ new_bio("You", "I decided to leave the DIKs' Christmas Panty Party.")

else:

    if branchAlone:
        $ ep11_mg_party = False
        scene ep11_main_party6b with dissolve
        mc "(But I'm having a blast here as it is.)"
    elif ep11_josy_love > 0 or ep11_maya_love > 0:
        $ ep11_mg_party = True
        mc "(But it would be rude to leave this party...right?)"
        mc "(Derek could keep the party going if I left...)"
        scene ep11_main_party6b with dissolve
        mc "(Yeah, fuck it. I'll find a way to leave this party early. I wanna spend tonight with Josy, Maya and the rest.)"
    else:
        mc "(But it would be rude to leave this party...right?)"
        mc "(Derek would be able to keep the party going if I left...)"
        
        if persistent.mod_wtenabled:
                            $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                            #[mod_gr][mod_choices[0]]
                            #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                            if branchSage and ep11_cammy_draught and sage_dik > 0:
                               $ mod_choices[6]="(Possible Sage/Camila threesome)"
                               $ mod_choices[7]="(+5 Cheater)"
                            "scrappy" "Leaving the party means you could miss Elena's scene and kissing Sally."
        
        
        
        menu:
            "Mod: Do both":
                $ wt_ep11_party_bella = True
                scene ep11_main_party6b with dissolve
                mc "(No, what am I thinking? I'm having fun here and I can't ask Derek to take care of everything. I'm staying.)"
                $ new_bio("You", "I decided to stay at the DIKs' Christmas Panty Party and go to Bella's later.")
            "Stay at the party":
                $ ep11_mg_party = False
                scene ep11_main_party6b with dissolve
                mc "(No, what am I thinking? I'm having fun here and I can't ask Derek to take care of everything. I'm staying.)"
                $ new_bio("You", "I decided to stay at the DIKs' Christmas Panty Party.")
            "Go to Bella's party \n{size=-4}[m_c1][mod_choices[6]]":
                $ ep11_mg_party = True
                scene ep11_main_party6b with dissolve
                mc "(Yeah, fuck it. I'll find a way to leave this party early.)"
                $ new_bio("You", "I decided to leave the DIKs' Christmas Panty Party.")

$ freeRoamID = "ep11_4b"
if ep11_mg_party:
    $ current_task = ""
    if persistent.mod_wtenabled:
        $ task_list = ["","Tell Derek you're leaving","","","","","","","","","",""]
    else:
        $ task_list = ["","Tell Derek you're leaving (Right Hallway)","","","","","","","","","",""]
    $ optional_task_list = []
    $ event_list = []
    if (branchJill or branchIsabella) and (ep11_bianca_dick > 0 or ep11_bianca_flirt):
        if persistent.mod_wtenabled:
            $ task_list[6] = "Say goodbye to Bianca (Tommy's room)"
        else:
            $ task_list[6] = "Say goodbye to Bianca"
        $ event_list.append("ep11_pp_bia_event_label")
    if branchSage and ep11_cammy_draught and sage_dik > 0:
        if persistent.mod_wtenabled:
            $ task_list[10] = "Talk to Camila (Main Party Room)"
        else:
            $ task_list[10] = "Talk to Camila"
        $ event_list.append("ep11_pp_ctease_event_label")
    $ event_list.append("part2")
    $ event_list.append("ep11_pp_dleave_event_label")
    $ event_list.append("ep11_pp_kp_event_label")
    if persistent.mod_wtenabled:
        $ task_list[11] = "Deal with unwanted guests (Main Party room)"
    else:
        $ task_list[11] = "Deal with unwanted guests"
    if ep11_invited_tara:
        if persistent.mod_wtenabled:
            $ task_list[2] = "Greet Tara (Main Party room)"
        else:
            $ task_list[2] = "Greet Tara"
        $ event_list.append("ep11_pp_tara_event_label")
else:
    $ current_task = ""
     
    if persistent.mod_wtenabled:
        $ task_list = ["","","","Find Tommy (Tommy's room)","","","","","","Talk to Zoey (Main Party Room)","","",""]
        $ optional_task_list = ["","","Talk to Sally (Upper Main Room)",""]
    else:
        $ task_list = ["","","","Find Tommy","","","","","","Talk to Zoey","","",""]
        $ optional_task_list = ["","","Talk to Sally",""]

    if ep11_db_mission:
        $ optional_task_list[0] = "Dirty Bowl Mission [ep11_db_mission_progress]/5"

    if "ep11_pp_leon_event_label" in event_list:
        if persistent.mod_wtenabled:
            $ optional_task_list[1] = "Find out who X is (Leon - Tommy's room)"
        else:
            $ optional_task_list[1] = "Find out who X is"

    if "ep11_pp_santa_bc_event_label" in event_list:
        $ event_list = []
        $ event_list.append("ep11_pp_santa_bc_event_label")
    else:
        $ event_list = []

    if optional_task_list[1] == "Find out who X is" or optional_task_list[1] == "Find out who X is (Leon - Tommy's room)":
        $ event_list.append("ep11_pp_leon_event_label")
    $ event_list.append("ep11_pp_act2_event_label")
    $ event_list.append("ep11_pp_kp_event_label")
    if persistent.mod_wtenabled:
        $ task_list[11] = "Deal with unwanted guests (Main Party room)"
    else:
        $ task_list[11] = "Deal with unwanted guests"

    $ event_list.append("part2")
    if ep11_db_mission:
        $ event_list.append("ep11_pp_santa_event_label")
        $ event_list.append("ep11_pp_santa_sandy_event_label")
        $ event_list.append("ep11_pp_santa_heather_event_label")
    $ event_list.append("ep11_pp_dm_event_label")
    $ event_list.append("ep11_pp_sk_event_label")
    $ event_list.append("ep11_pp_st_event_label")
    if (branchJill or branchIsabella) and (ep11_bianca_dick > 0 or ep11_bianca_flirt):
        $ event_list.append("ep11_pp_bia_event_label")
        if persistent.mod_wtenabled:
            $ task_list[6] = "Talk to Bianca (Tommy's room)"
        else:
            $ task_list[6] = "Talk to Bianca"

    if ep10_date_nicole and not ep10_cancel_date_nicole:
        if persistent.mod_wtenabled:
            $ task_list[7] = "Talk to Nicole (Main Party Room)"
        else:
            $ task_list[7] = "Talk to Nicole"
        $ event_list.append("ep11_pp_nl_event_label")

    $ event_list.append("ep11_pp_zoey2_event_label")

    if ep11_invited_tara:
        if persistent.mod_wtenabled:
            $ task_list[2] = "Greet Tara (Main Party room)"
        else:
            $ task_list[2] = "Greet Tara"
        $ event_list.append("ep11_pp_tara_event_label")
        
    if wt_ep11_party_bella:
            
        if branchSage and ep11_cammy_draught and sage_dik > 0:
            if persistent.mod_wtenabled:
                $ task_list[10] = "Talk to Camila (Main Party Room)"
            else:
                $ task_list[10] = "Talk to Camila"
            $ event_list.append("ep11_pp_ctease_event_label")

$ updateTaskList()

$ map_system_list = []
$ map_system_list.append(["ep11_diks_fr2_lib_mid","ep11_diks4_fr2_lib_mid_label","Your room"])
$ map_system_list.append(["ep11_diks_pp2_derek","ep11_diks_pp_derek_label","Derek's room"])
$ map_system_list.append(["ep11_diks_pp_dining","ep11_diks_pp_dining_label","Dining room"])
$ map_system_list.append(["ep11_diks_fr1_jacob_no_box","ep11_diks_pp_jacob_label","Jacob's room"])
$ map_system_list.append(["ep11_diks_pp_jamie","ep11_diks_pp_jamie_label","Jamie's room"])
$ map_system_list.append(["ep11_diks_pp_jb","ep11_diks_pp_jb_label","John Boy's room"])
$ map_system_list.append(["ep11_diks_fr1_left_hall","ep11_diks_pp_left_hall_label","Left hallway"])
$ map_system_list.append(["ep11_diks_pp2_main","ep11_diks_pp_main_label","Main party room"])
$ map_system_list.append(["ep11_diks_party_nick","ep11_diks_pp_nick_label","Nick's room"])
$ map_system_list.append(["ep11_diks3_pp2_right_hall","ep11_diks_pp_right_hall_label","Right hallway"])
$ map_system_list.append(["ep11_diks_pp2_tommy_room","ep11_diks_pp_tommy_label","Tommy's room"])
$ map_system_list.append(["ep11_diks_pp2_ua","ep11_diks_pp_ua_label","Upper main room"])

$ currentFreeRoamLabel = "ep11_diks_pp_right_hall_label"
jump endEvent

label ep11_pp_dleave_event_label:
scene ep11_pp_dleave_event1 with dissolve
de "You're leaving!? You can't do that!"
scene ep11_pp_dleave_event2 with dissolve
mc "I want to go to Bella's tonight."
scene ep11_pp_dleave_event5 with dissolve
de "To Bella's? What for?"
scene ep11_pp_dleave_event2 with dissolve
mc "They're having a girl party."
scene ep11_pp_dleave_event5 with dissolve
de "Have you looked at where you're at?"
scene ep11_pp_dleave_event2 with dissolve
mc "I know, I know. But I want to go."
scene ep11_pp_dleave_event5 with dissolve
de "Bros before hos."
scene ep11_pp_dleave_event3 with dissolve
mc "Your sister is over there."
de "..."
scene ep11_pp_dleave_event4 with dissolve
de "I can't fucking win with this guy."
scene ep11_pp_dleave_event2 with dissolve
mc "I know it's a lot to ask for, but can you handle the rest of the party?"
if ep11_pp_game == 0:
    scene ep11_pp_dleave_event5 with dissolve
    de "Do you want me to handle the game you planned, too?"
    de "I thought you were excited about that."
else:
    scene ep11_pp_dleave_event5 with dissolve
    de "It's not like there's a lot more to handle, but still..."
    de "I thought you were excited for this party."
de "Hell, you spent so much energy on planning this, and now you're bailing just like that."
scene ep11_pp_dleave_event2 with dissolve
mc "I know. What you say is true, but... I still want to leave."
scene ep11_pp_dleave_event5 with dissolve
de "*{i}Sigh{/i}* Then leave the rest to me."
scene ep11_pp_dleave_event2 with dissolve
mc "Are you sure?"
scene ep11_pp_dleave_event6 with dissolve
de "I'm not gonna say I want you to leave because it's much more fun with you around, but you clearly have somewhere else to be tonight, so..."
scene ep11_pp_dleave_event2 with dissolve
mc "Thanks, bro... You're the best."
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_dm_event_label:
scene ep11_pp_dm_event1 with dissolve
girl "Mistletoe!!!"
scene ep11_pp_dm_event2 with dissolve
girl "*{i}Smack{/i}*"
scene ep11_pp_dm_event3 with dissolve
$ renpy.pause()
scene ep11_pp_dm_event4 with dissolve
$ renpy.pause()
scene ep11_pp_dm_event5 with dissolve
$ renpy.pause()
scene ep11_pp_dm_event6 with dissolve
de "Mistletoe!"
scene ep11_pp_dm_event7 with dissolve
girl "*{i}Smack{/i}*"
scene ep11_pp_dm_event8 with dissolve
$ renpy.pause()
scene bg anim_derek_mt_ep11 movie with dissolve
$ renpy.pause(2)
de "Mistletoe!"
play sound "sound_effects/slap.mp3"
scene ep11_pp_dm_event9 with hpunch
$ renpy.pause()
scene ep11_pp_dm_event10 with dissolve
$ renpy.pause()

$ updateTaskList()
jump endEvent

label ep11_pp_sk_event_label:
$ guideSuggestedPage = 209
scene ep11_pp_sk_event1 with dissolve
ka "Are you sure it's ok? Haha!"
scene ep11_pp_sk_event3 with dissolve
jm "Yeah, as you can tell from my face, I'm single."
scene ep11_pp_sk_event2 with dissolve
ka "Did Dany do that to you?"
scene ep11_pp_sk_event3 with dissolve
jm "She...um...encouraged it."
scene ep11_pp_sk_event4 with dissolve
sy "Ugh... You're not going through with it, are you?"
scene ep11_pp_sk_event5 with dissolve
ka "Look around you. Everyone is following through tonight."
scene ep11_pp_sk_event4 with dissolve
sy "What's gotten into you?"
scene ep11_pp_sk_event6 with dissolve
ka "It's about time I started getting a taste of college."
scene ep11_pp_sk_event7 with dissolve
mc "Now, here's a party. Go, Jamie..."
scene ep11_pp_sk_event8 with dissolve
sy "More like \"go away\"."
scene ep11_pp_sk_event9 with dissolve
mc "Aw, are you jealous?"
scene ep11_pp_sk_event8 with dissolve
sy "Of Jamie? Oh, please. He's not a good kisser."
sy "Just look how he's slobbering all over her."
scene ep11_pp_sk_event10 with dissolve
mc "They look good together. Way better than him and Dany, if you ask me."
sy "They're not hooking up. Karen is just doing her mission of going to second base with someone and Jamie is the tool."
scene ep11_pp_sk_event11 with dissolve
mc "I'd still call that hooking up. And good for Karen."
mc "What about you? Did you do yours already?"
scene ep11_pp_sk_event12 with dissolve
sy "No. And I've been meaning to ask you..."
sy "Who the hell came up with these lame ideas? Seven minutes in heaven?"
sy "Last time I checked, you did that in high school. This is college. Grow up!"
scene ep11_pp_sk_event11 with dissolve
mc "That's an easy one. You should see some of the other guests' missions."
mc "Trust me, there are way worse things to get."
scene ep11_pp_sk_event13 with dissolve
sy "Will you help me out with it?"
scene ep11_pp_sk_event11 with dissolve
mc "Do you want me to make out with you in a closet?"
scene ep11_pp_sk_event12 with dissolve
sy "No!?"
scene ep11_pp_sk_event14 with dissolve
mc "Isn't that what it is?"
scene ep11_pp_sk_event13 with dissolve
sy "By definition, you have to sit in a dark room or closet together for seven minutes and do whatever."
sy "While many choose to participate in sexual activities or kiss, it's enough to talk or sit and wait the time out."
scene ep11_pp_sk_event11 with dissolve
mc "So, you want me to sit in silence with you in a closet for seven minutes?"
scene ep11_pp_sk_event13 with dissolve
sy "It doesn't have to be a closet. Let's find an empty room and do it."
scene ep11_pp_sk_event11 with dissolve
menu:
    "Ok, but no funny business":
        mc "Ok, but no funny business."
        scene ep11_pp_sk_event12 with dissolve
        sy "As if."
    "[m_c1]Let's do it":
        mc "Ok. Let's find a room then."
    "Nah, I'm good.":
        mc "Nah, I'm good."
        $ optional_task_list[2] = ""
        $ updateTaskList()
        jump endEvent
scene ep11_pp_sk_event15 with wipeleft
mc "We'll have to turn the lights off, but this will do. It's as close to a closet as we get tonight."
scene ep11_pp_sk_event16 with dissolve
$ renpy.pause()
play sound "sound_effects/switch.mp3"
scene ep11_pp_sk_event17
$ renpy.pause()
scene ep11_pp_sk_event18 with dissolve
sy "We'll have to wing it because I don't have a phone or watch on me. What takes seven minutes?"
scene ep11_pp_sk_event19 with dissolve
mc "We can listen to a few songs from here. Two or three songs should do it."
scene ep11_pp_sk_event20 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event21 with dissolve
sy "To be clear... Don't expect me to do something with you. Ok?"
scene ep11_pp_sk_event22 with dissolve

if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

if branchAlone:
    $ guideSuggestedPage = 209
    menu:
        "I'm not expecting anything":
            mc "I'm not expecting anything. Let's sit here and wait together."
        "You can if you want to \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "You can if you want to."
            scene ep11_pp_sk_event23 with dissolve
            sy "Stop it."
        "Not even a little kiss?":
            scene ep11_pp_sk_event24 with dissolve
            mc "Not even a little kiss?"
            scene ep11_pp_sk_event25 with dissolve
            $ renpy.pause()
            scene ep11_pp_sk_event26 with dissolve
            sy "*{i}Smack{/i}*"
            scene ep11_pp_sk_event27 with dissolve
            sy "There, now shut up."
else:
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1): 
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    menu:
        "I'm taken \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "I'm taken, so I wasn't expecting anything. I wouldn't have done this otherwise."
        "I'm not expecting anything":
            mc "I'm not expecting anything. Let's sit here and wait together."
        "Not even a little kiss? \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[6]]":
            $ tc += 1
            $ dk(1)
            scene ep11_pp_sk_event24 with dissolve
            mc "Not even a little kiss?"
            scene ep11_pp_sk_event25 with dissolve
            $ renpy.pause()
            scene ep11_pp_sk_event26 with dissolve
            sy "*{i}Smack{/i}*"
            scene ep11_pp_sk_event27 with dissolve
            sy "There, now shut up."
scene ep11_pp_sk_event28 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event29 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event30 with dissolve
sy "What did you get?"
scene ep11_pp_sk_event31 with dissolve
mc "Hm?"
scene ep11_pp_sk_event30 with dissolve
sy "What did you pull from that bowl? What are you supposed to do tonight?"
scene ep11_pp_sk_event31 with dissolve
if ep11_db_mission:
    if ep11_db_mission_progress == 0:
        mc "I was supposed to dress as Santa and have girls sit in my lap, but I haven't even started. I don't think I'll complete it."
    elif ep11_db_mission_progress <= 4:
        mc "I was supposed to dress as Santa and have girls sit in my lap. I might finish it at some point."
    elif ep11_db_mission_progress == 5:
        mc "I was supposed to dress as Santa and have girls sit in my lap. It was pretty easy; I'm already done with it."
else:
    mc "I was supposed to dress as Santa and have girls sit in my lap. But I got out of it because I helped out hosting the party."
scene ep11_pp_sk_event32 with dissolve
sy "That's a good one. It's the first one that I heard that was Christmas-related."
scene ep11_pp_sk_event33 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event32 with dissolve
sy "Nice job on the report, by the way. Did you see what Dr. Jenkins wrote?"
scene ep11_pp_sk_event33 with dissolve
mc "Did she grade it already?"
scene ep11_pp_sk_event34 with dissolve
sy "Yeah, we passed. She thought we did a thorough job."
scene ep11_pp_sk_event33 with dissolve
mc "That's great. We make a good team."
scene ep11_pp_sk_event32 with dissolve
sy "Eh. I've had better."
scene ep11_pp_sk_event35 with dissolve
mc "My frame of reference was Derek, so I can't say the same."
scene ep11_pp_sk_event36 with dissolve
sy "Although not much of a feat, you're better than Ron. I'll give you that."
scene ep11_pp_sk_event37 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event38 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event37 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event38 with dissolve
mc "I gotta say, you're not as bad as I originally thought."
scene ep11_pp_sk_event39 with dissolve
sy "Is that supposed to be a compliment?"
scene ep11_pp_sk_event38 with dissolve
mc "It's my way of saying that I'm starting to like you. We never got along before we were forced to get along."
scene ep11_pp_sk_event39 with dissolve
sy "I've had my reasons."
scene ep11_pp_sk_event38 with dissolve
mc "To not like me?"
scene ep11_pp_sk_event40 with dissolve
sy "Stereotypes, preconceived notions, advice, rumors and whatnot."
scene ep11_pp_sk_event41 with dissolve
mc "That's a lot of reasons."
scene ep11_pp_sk_event40 with dissolve
if affinity == "DIK":
    sy "And while most of it seems to be true, and you can be a big fucking button pusher..."
elif affinity == "NEUTRAL":
    sy "And while some of it seems to be true, not all is..."
else:
    sy "But not much of it seems to be true..."
sy "You have some qualities that aren't detestable."
$ guideSuggestedPage = 210
scene ep11_pp_sk_event41 with dissolve
mc "Is {i}that{/i} supposed to be a compliment?"
scene ep11_pp_sk_event40 with dissolve
sy "You're kind of ok, too."
scene ep11_pp_sk_event41 with dissolve

if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

menu:
    "Tease her \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "You sure know how to make a guy feel special."
    "Thanks, Sally \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Thanks, Sally. I appreciate that."
scene ep11_pp_sk_event42 with dissolve
$ renpy.pause()
scene ep11_pp_sk_event44 with dissolve
sy "Has it been seven minutes yet?"
scene ep11_pp_sk_event43 with dissolve
mc "More like one minute."
scene ep11_pp_sk_event44 with dissolve
sy "This is boring."
scene ep11_pp_sk_event42 with dissolve
menu:
    "Let's call it seven":
        scene ep11_pp_sk_event43 with dissolve
        label ep11_pp_sk_event2_label:
        mc "On the other hand... Let's call it seven minutes."
        label ep11_pp_sk_event2b_label:
        scene ep11_pp_sk_event45 with dissolve
        sy "Uh... Ok. That means I'm done."
        scene ep11_pp_sk_event46 with dissolve
        mc "Yeah. No consequence for you."
        scene ep11_pp_sk_event47 with dissolve
        sy "Great. I assume I should thank you, but all you did was sit here for one minute with me, so I won't."
        scene ep11_pp_sk_event46 with dissolve
        mc "You're welcome."
        scene ep11_pp_sk_event48 with dissolve
        sy "Haha!"
        $ new_bio("Sally", "I helped Sally with her Dirty Bowl mission but didn't take any advantage of it.")
    "[m_c1]Not supposed to be boring":
        scene ep11_pp_sk_event43 with dissolve
        mc "It's not supposed to be boring. It's supposed to be heaven."
        scene ep11_pp_sk_event49 with dissolve
        $ renpy.pause()
        scene ep11_pp_sk_event50 with dissolve
        $ renpy.pause()
        scene ep11_pp_sk_event51 with dissolve
        sy "Should we make out to pass the time?"
        scene ep11_pp_sk_event50 with dissolve
        
        if persistent.mod_wtenabled:
                        $mod_choices = ["(Sally Kiss)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
        
        if branchAlone:
            menu:
                "Make out with her \n{size=-4}[m_c1][mod_choices[0]]":
                    mc "If you're up for it."
                    label ep11_pp_sk_event2c_label:
                    $ ep11_sally_kiss = True
                    scene ep11_pp_sk_event52 with dissolve
                    $ renpy.pause()
                    scene ep11_pp_sk_event53 with dissolve
                    $ renpy.pause()
                    scene ep11_pp_sk_event54 with dissolve
                    $ renpy.pause()
                    play sound "sound_effects/shove.mp3"
                    scene ep11_pp_sk_event55 with hpunch
                    mc "Whoa!"
                    scene anim_sally_kiss_ep11 with dissolve
                    pause
                    scene anim_sally_kiss2_ep11 with dissolve
                    pause
                    if not branchAlone:
                        scene ep11_pp_sk_event56 with dissolve
                        mc "I...um...think that's enough."
                        scene ep11_pp_sk_event57 with dissolve
                        sy "What's wrong?"
                        scene ep11_pp_sk_event56 with dissolve
                        mc "I think we took it too far."
                        scene ep11_pp_sk_event57 with dissolve
                        sy "What did you think making out meant?"
                        scene ep11_pp_sk_event56 with dissolve
                        mc "I don't know. I'm sorry."
                        scene ep11_pp_sk_event57 with dissolve
                        sy "You're weird."
                        scene ep11_pp_sk_event58 with dissolve
                        if ep11_helped_erin_mia or ep11_mistletoe > 0:
                            mc "(It's not the first questionable thing I did tonight... What am I doing?)"
                        else:
                            mc "(What am I doing?)"
                    else:
                        scene anim_sally_kiss3_ep11 with dissolve
                        pause
                        scene ep11_pp_sk_event59 with dissolve
                        sy "Hey, you're not a bad kisser."
                        scene ep11_pp_sk_event60 with dissolve
                        mc "You're not a bad kisser yourself."
                        scene ep11_pp_sk_event59 with dissolve
                        sy "I could have done without the dry humping and the ass-grabbing, but yeah, not bad."
                        scene ep11_pp_sk_event60 with dissolve
                        mc "Hey, you humped back."
                        scene ep11_pp_sk_event59 with dissolve
                        sy "We have to be at least close to seven minutes now. I think that's it."
                        scene ep11_pp_sk_event60 with dissolve
                        mc "Yeah, that's fine by me. Good times..."
                        scene ep11_pp_sk_event59 with dissolve
                        sy "I have to check on Karen now."
                        scene ep11_pp_sk_event60 with dissolve
                        mc "Are you sure? The mission put aside... I'd love to do more of this with you."
                        scene ep11_pp_sk_event61 with dissolve
                        sy "Oh, [name]. You're so predictable."
                        scene ep11_pp_sk_event62 with dissolve
                        mc "(That was pretty hot. I didn't think she'd be up for that. She keeps surprising me.)"
                    $ new_bio("Sally", "I helped Sally with her Dirty Bowl mission, and we made out on Leon's bed.")
                "Not interested":
                    jump ep11_pp_sk_event2_label
        else:
            menu:
                "Make out with her \n{size=-4}[m_c1][mod_choices[7]][m_c2][mod_choices[0]]":
                    $ tc += 5
                    mc "I shouldn't..."
                    scene ep11_pp_sk_event51 with dissolve
                    sy "That wasn't a no."
                    jump ep11_pp_sk_event2c_label
                "Not interested":
                    scene ep11_pp_sk_event43 with dissolve
                    mc "No, I won't do that. But you know what? Let's call it seven minutes."
                    jump ep11_pp_sk_event2b_label

$ currentFreeRoamLabel = "ep11_diks_pp_leon_room_label"
$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_tara_event_label:
if "ep11_pp_group_event_label" in event_list:
    $ event_list.remove("ep11_pp_group_event_label")
scene ep11_pp_tara_event1 with dissolve
ta "Hey, girls."
scene ep11_pp_tara_event2 with dissolve
ti "You came!"
scene ep11_pp_tara_event3 with dissolve
ta "Yep, I did."
scene ep11_pp_tara_event6 with dissolve
gi "I thought you weren't invited. Is that why you're wearing that mask?"
scene ep11_pp_tara_event5 with dissolve
ta "I wasn't at first, but [name] invited me."
scene ep11_pp_tara_event7 with dissolve
ti "See! I knew he was a cool guy. What did I tell you? I have an eye for these things."
scene ep11_pp_tara_event8 with dissolve
ti "Your friends are so stupid for getting you involved in their drama to begin with."
scene ep11_pp_tara_event4 with dissolve
ta "Some of what they said made sense. But I didn't think it would come to this."
$ guideSuggestedPage = 204
scene ep11_pp_tara_event19 with dissolve
mc "Tara! You came. Any trouble getting in?"
scene ep11_pp_tara_event20 with dissolve
ta "Hi, [name]. No, I didn't encounter or bring any trouble."
scene ep11_pp_tara_event21 with dissolve
mc "I talked to my brothers and told them you'd be showing up."
scene ep11_pp_tara_event22 with dissolve
ta "Were they ok with it?"
scene ep11_pp_tara_event21 with dissolve
mc "Hm... There were mixed reactions. You should talk to them tonight."
scene ep11_pp_tara_event20 with dissolve
ta "Thanks, I will."
ta "And thanks for being the only one who wanted to listen to me."
scene ep11_pp_tara_event21 with dissolve
mc "You're welcome."
scene ep11_pp_tara_event23 with dissolve
ta "Can I give you a hug?"
scene ep11_pp_tara_event24 with dissolve
if affinity == "DIK":
    $ renpy.pause()
    scene ep11_pp_tara_event25 with dissolve
menu:
    "Sure":
        mc "Sure, bring it in."
        scene ep11_pp_tara_event26 with dissolve
        $ renpy.pause()
    "You don't have to":
        mc "Nah, you don't have to do that. We're cool, Tara."
scene ep11_pp_tara_event21 with dissolve
mc "Enjoy the party."

scene ep11_pp_tara_event9 with dissolve
ti "Here you go. You need this drink to catch up."
scene ep11_pp_tara_event10 with dissolve
ta "Question... Why are you topless?"
scene ep11_pp_tara_event11 with dissolve
ti "It's for The Dirty Bowl, yeah?"
scene ep11_pp_tara_event10 with dissolve
ta "The what?"
scene ep11_pp_tara_event13 with dissolve
gi "No, it's not for that. Ask [name] and Tommy why."
gi "Because nipple tape didn't classify as underwear to them."
scene ep11_pp_tara_event14 with dissolve
ti "Haha! Of course, it didn't!"
scene ep11_pp_tara_event12 with dissolve
gi "And for that bowl thing, I did mine already with Tommy."
scene ep11_pp_tara_event10 with dissolve
ta "I feel lost. What's the bowl thing about?"
scene ep11_pp_tara_event13 with dissolve
gi "Derek has been handing out missions to all guests, which you should complete by midnight."
gi "If you don't, there will be some punishment later. But not for me, since I did mine."
gi "And Tiffani did hers, too."
scene ep11_pp_tara_event15 with dissolve
gi "Right?"
scene ep11_pp_tara_event16 with dissolve
ti "Derek never made me pick one, and I didn't bring it to his attention. Haha!"
scene ep11_pp_tara_event15 with dissolve
gi "That's unfair! Both of you need to get one now."
scene ep11_pp_tara_event17 with dissolve
ti "She just came here; let her enjoy herself."
scene ep11_pp_tara_event18 with dissolve
gi "And what's your excuse?"
ti "Hahaha!"
$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_mt2_event_label:
$ ep11_girl_leaving = True
scene ep11_pp_mt2_event1 with dissolve
$ renpy.pause()
scene ep11_pp_mt2_event2 with dissolve
mc "Do you want something more to drink?"
scene ep11_pp_mt2_event3 with dissolve
girl "You've given me enough punch for tonight, thanks."
scene ep11_pp_mt2_event4 with dissolve
mc "Ah, good. I've had enough, too."
scene ep11_pp_mt2_event3 with dissolve
girl "Have you been dodging mistletoes all night?"
scene ep11_pp_mt2_event4 with dissolve
mc "Hm?"
scene ep11_pp_mt2_event5 with dissolve
girl "From earlier. Upstairs."
scene ep11_pp_mt2_event4 with dissolve
mc "Oh, that. Yeah, I have been dodging them. I can't go around kissing every guest."
scene ep11_pp_mt2_event5 with dissolve
girl "It's not like kissing people has been the worst thing I saw here tonight."
scene ep11_pp_mt2_event6 with dissolve
mc "If you hadn't noticed, our parties are usually wild."
scene ep11_pp_mt2_event7 with dissolve
girl "But not you?"
scene ep11_pp_mt2_event6 with dissolve
if affinity == "DIK":
    mc "Sometimes. But it can get too much even for me."
    scene ep11_pp_mt2_event7 with dissolve
    girl "Right. But...you plan these parties."
else:
    mc "I try my best to avoid the crazy stuff."
    scene ep11_pp_mt2_event7 with dissolve
    girl "Right. You only plan that for others."
scene ep11_pp_mt2_event8 with dissolve
mc "Haha, you got me."
scene ep11_pp_mt2_event9 with dissolve
girl "Well, I think it's time to leave before I have to face any consequences."
scene ep11_pp_mt2_event10 with dissolve
mc "Oh, yeah. It's approaching midnight. Didn't you complete your mission?"
scene ep11_pp_mt2_event9 with dissolve
girl "No. You guessed it."
scene ep11_pp_mt2_event10 with dissolve
mc "You're in my Science class, right?"
scene ep11_pp_mt2_event11 with dissolve
girl "Hmph... And I was told this mask would conceal my identity at the party."
scene ep11_pp_mt2_event12 with dissolve
mc "Hey... Girl leaving before midnight... What's your name?"
scene ep11_pp_mt2_event13 with dissolve
$ renpy.pause()
scene ep11_pp_mt2_event14 with dissolve
girl "Maybe I'm Cinderella?"
scene ep11_pp_mt2_event13 with dissolve
mc "Haha, ok? I'm [name]."
if branchAlone:
    scene ep11_pp_mt2_event14 with dissolve
    if ep9_dangerous:
        girl "[name]? I thought you were Mr. Danger."
    else:
        girl "[name]? I thought you were Mr. Teddy Bear."
    scene ep11_pp_mt2_event13 with dissolve
    mc "Huh?"
scene ep11_pp_mt2_event15 with dissolve
$ renpy.pause()
scene ep11_pp_mt2_event16 with dissolve
$ renpy.pause()
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_zoey2_event_label:
scene ep11_pp_zoey2_event19 with dissolve
bc "Jacob? Oh, he's a hottie, for sure. But Clara is a nottie."
bc "I can't believe they are hooking up. He's settling below his league with her."
scene ep11_pp_zoey2_event1 with dissolve
fel "You're only saying that because you had sex with him."
scene ep11_pp_zoey2_event19 with dissolve
bc "Am not. We slept together because real recognizes real."
scene ep11_pp_zoey2_event10 with dissolve
$ renpy.pause()
scene ep11_pp_zoey2_event7 with dissolve
er "What are you talking about? I think Clara is cute."
er "But I'm much more into Rusty than Jacob. I have a thing for that scruffy look he has with the beard and all."
scene ep11_pp_zoey2_event2 with dissolve
fel "Rusty is ok, but he has the whole history with Joanne. It's off-putting to me."
scene ep11_pp_zoey2_event19 with dissolve
bc "Because he was with Joanne? All they did was fuck, or am I wrong?"
scene ep11_pp_zoey2_event1 with dissolve
fel "No, because it's like she's got dibs. You don't make moves on a guy that your friend likes."
scene ep11_pp_zoey2_event20 with dissolve
bc "If she likes him so much, then she shouldn't have left. Besides, he's sticking his tongue far down some other girl's throat as we speak."
bc "I don't think you should have to care about what Joanne thinks if he's ok with doing that."
scene ep11_pp_zoey2_event8 with dissolve
er "What about you, Zoey? Which DIK do you find hot?"
scene ep11_pp_zoey2_event11 with dissolve
zo "Hm? Eh... I don't know."
scene ep11_pp_zoey2_event5 with dissolve
fel "You don't like any of them?"
scene ep11_pp_zoey2_event18 with dissolve
bc "I saw you talk to Jacob at that barbecue party. You're into him, right?"
scene ep11_pp_zoey2_event14 with dissolve
zo "No. Not at all."
scene ep11_pp_zoey2_event18 with dissolve
bc "Good. Because he's out of your league. No offense."
scene ep11_pp_zoey2_event15 with dissolve
zo "No offense? Sheesh."
scene ep11_pp_zoey2_event8 with dissolve
er "So, who do you like?"
scene ep11_pp_zoey2_event12 with dissolve
$ renpy.pause()
scene ep11_pp_zoey2_event13 with dissolve
zo "I'd say...[name]."
scene ep11_pp_zoey2_event17 with dissolve
bc "And he's even more out of your league. No offense."
if ep7_becky_lewd:
    bc "[name] is a total hottie. I gave him a blowjob once."
    scene ep11_pp_zoey2_event6 with dissolve
    fel "As if."
    scene ep11_pp_zoey2_event20 with dissolve
    bc "I totally did. You should know that those pictures of his cock don't do him justice."
else:
    bc "[name] is a total hottie."
if ep11_helped_erin_mia:
    scene ep11_pp_zoey2_event4 with dissolve
    er "He helped me and Mia with our missions earlier tonight."
    scene ep11_pp_zoey2_event3 with dissolve
    fel "Haha! No way!"
    scene ep11_pp_zoey2_event21 with dissolve
    bc "But you're not in the same league."
scene ep11_pp_zoey2_event16 with dissolve
$ renpy.pause()
if not ep8_recital_failed:
    scene ep11_pp_zoey2_event7 with dissolve
    er "Did you see the video of him playing guitar?"
    scene ep11_pp_zoey2_event21 with dissolve
    bc "Like, the minute it was posted. I helped it go viral."
    scene ep11_pp_zoey2_event7 with dissolve
    er "You did?"
scene ep11_pp_zoey2_event2 with dissolve
if ep11_mistletoe > 0:
    fel "He is hot. And he sure knows how to kiss. I sampled him underneath the mistletoe earlier."
    fel "But I'd still pick Jacob over him."
else:
    fel "He is hot. But I'd still pick Jacob over him."
scene ep11_pp_zoey2_event9 with dissolve
er "You're crazy! You wouldn't get with [name] if he asked?"
scene ep11_pp_zoey2_event2 with dissolve
fel "Well, duh. But that's not what I was saying."
scene ep11_pp_zoey2_event17 with dissolve
bc "You're much closer to Jacob's league than [name]'s."
if zoey_dik:
    scene ep11_pp_zoey2_event15 with dissolve
    zo "*{i}Sigh{/i}* And you are not even playing the same sport."
    scene ep11_pp_zoey2_event17 with dissolve
    bc "What does sports have to do with this?"
else:
    scene ep11_pp_zoey2_event16 with dissolve
    $ renpy.pause()

if ep11_mg_party:
    jump ep11_pp_zoey_endb_label
if persistent.mod_wtenabled:
    $ task_list[5] = "Get approached by Becky (Right Hallway)"
else:
    $ task_list[5] = "Get approached by Becky"
$ event_list.append("ep11_becky_event_label")
$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_quinn2_event_label:
$ guideSuggestedPage = 212
scene ep11_pp_quinn2_event1 with dissolve
$ renpy.pause()
play music "music/ep6/licensed_music/track31.mp3"
scene ep11_pp_quinn2_event2 with dissolve
mc "Where have you been all night and why are you sitting here alone?"
scene ep11_pp_quinn2_event3 with dissolve
qu "I needed a break from the party. It's fucking loud tonight."
scene ep11_pp_quinn2_event2 with dissolve
mc "I thought you'd be into that."
scene ep11_pp_quinn2_event3 with dissolve
qu "Not tonight."
qu "[name]... I think I'm ready."
scene ep11_pp_quinn2_event4 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event5 with dissolve
mc "Ok... I've been waiting for it."
scene ep11_pp_quinn2_event8 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event6 with dissolve
qu "But first... Why do you care so much about how I feel?"
scene ep11_pp_quinn2_event5 with dissolve
menu:
    "[m_c1]I'm into you":
        $ ep11_quinn_question[0] = True
        mc "Don't you get it yet? I'm into you. That's why I care."
        mc "I care about you so much, Quinn. And it's annoying that you won't let me."
    "I'm worried about you":
        $ ep11_quinn_question[0] = False
        mc "I've never seen you like this before. Frankly, I'm worried about you."
scene ep11_pp_quinn2_event8 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event9 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event10 with dissolve
qu "I fucked up, [name]."
qu "I fucked up bad."
scene ep11_pp_quinn2_event9 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event11 with dissolve
mc "Tell me everything..."
scene ep11_pp_quinn2_event12 with dissolve
qu "When Dad died, I was seven years old."
qu "I went to bed early but couldn't sleep, so I got up to check what he was doing."
scene ep11_pp_quinn2_event13 with dissolve
qu "Mom was passed out on the floor from drugs and Dad was snorting coke with Buddy."
qu "Dad caught me peeking at them and knew what I had seen him do."
scene ep11_pp_quinn2_event14 with dissolve
qu "Even at that age, I knew what he was doing. I grew up around him selling drugs, but he tried not to use them in front of me. It was his way of protecting me."
scene ep11_pp_quinn2_event15 with dissolve
qu "Buddy told me to get back into bed. He called me a rat and Dad snapped at him."
qu "He screamed and threatened Buddy by holding a knife to his face."
scene ep11_pp_quinn2_event16 with dissolve
qu "I was shocked because I had never seen him be that mad at Buddy."
qu "Shortly thereafter... Dad had to sit down because he didn't feel good. He couldn't breathe..."
scene ep11_pp_quinn2_event17 with dissolve
qu "He...missed the chair and fell down on the floor."
qu "He started convulsing... Foam...like bubbles in a bath, erupted from his mouth and nose."
scene ep11_pp_quinn2_event18 with dissolve
qu "Buddy was panicking and didn't know what to do."
qu "He screamed at Mom, kicked her and tried to wake her up and help."
scene ep11_pp_quinn2_event19 with dissolve
qu "But that drugged-up bitch was dozed off as if nothing was happening right next to her."
scene ep11_pp_quinn2_event20 with dissolve
qu "All of a sudden, Dad stopped shaking. And it all became quiet."
qu "Then my ears started ringing. I saw Buddy shake Dad and scream at him, but I couldn't make out what he was shouting."
qu "It kept ringing."
scene ep11_pp_quinn2_event21 with dissolve
qu "And me... I just stood there."
qu "I don't even remember how long I stood there."
scene ep11_pp_quinn2_event22 with dissolve
qu "But it was well after Buddy and one of his friends carried Dad outside."
qu "All the while, Mom still passed out on the floor."
scene ep11_pp_quinn2_event23 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event12 with dissolve
qu "Buddy wasn't a bad guy. He was my Uncle, but he could never fill the void Dad left."
scene ep11_pp_quinn2_event13 with dissolve
qu "He was smart enough to realize that Mom wouldn't either. So, he dropped me off at social services with a note saying who I was and that I didn't have a family."
scene ep11_pp_quinn2_event24 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event12 with dissolve
qu "I was placed in a foster home with a family that has tried to prove to me daily that I'm better off with them."
qu "They took care of me, fed me, dressed me, and ensured I went to school... Eventually, they adopted me."
qu "And they did everything they could think of to make me forget about my past."
scene ep11_pp_quinn2_event25 with dissolve
qu "Anytime I brought up Dad, I was silenced."
qu "\"We shouldn't speak about him. You're in a better place now. Nothing will harm you here.\""
qu "Suppressing all my thoughts and trying to replace my childhood memories with these new fake ones that weren't me."
scene ep11_pp_quinn2_event26 with dissolve
qu "There's no way to describe the disdain I developed for them trying to make me repress memories of my past."
scene ep11_pp_quinn2_event27 with dissolve
qu "I never wanted to forget my dad."
scene ep11_pp_quinn2_event28 with dissolve
qu "*{i}Cries{/i}*"
scene ep11_pp_quinn2_event29 with dissolve
qu "And I never will."
scene ep11_pp_quinn2_event30 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event31 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event32 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event33 with dissolve
qu "That's why I returned to Buddy when I grew older."
qu "I skipped school, snuck away from my house, and would hang out at his place - the place I used to call home."
scene ep11_pp_quinn2_event34 with dissolve
qu "He made it clear to me that he wasn't letting me stay there with him; he didn't like that I was there to begin with. But I insisted that I wanted to hang around, so he let me."
qu "Years later, when I asked him for some weed, he gave me some. He taught me how to use it, how much to use, and what not to do with it."
qu "By the time I was in high school, I knew more than most guys my age about drugs."
scene ep11_pp_quinn2_event35 with dissolve
qu "I kept my front up to my new family, but they weren't gullible; they knew I was slipping."
qu "They confronted me about my drug use and even punished me in all the ways they could think of."
qu "They were desperate for me not to end up like I had started in life."
scene ep11_pp_quinn2_event36 with dissolve
qu "They told me they were losing their daughter and that they didn't know what to do about it. They begged me to help them help me."
qu "But I've only been their daughter on paper; it has never felt genuine to me. I've felt like a parasite."
scene ep11_pp_quinn2_event37 with dissolve
qu "Like someone who knows they don't belong in their home but stays to survive."
qu "Eating their food, sleeping in their bed...plainly using them."
scene ep11_pp_quinn2_event36 with dissolve
qu "That's how I felt."
qu "And I kept using them. I fooled them into thinking that I had changed my ways."
qu "I knew what they wanted from me and appearances make a world of difference."
scene ep11_pp_quinn2_event38 with dissolve
qu "As long as I did well in school, they were happy."
qu "They didn't have to know I was slinging drugs to classmates after class."
scene ep11_pp_quinn2_event39 with dissolve
qu "That's how I got started with all of this. I was born into it. It was my legacy."
qu "And that's how I met Riona..."
scene ep11_pp_quinn2_event40 with dissolve
qu "She was one of my favorite customers - a goth gullible girl without a father figure."
qu "She didn't even realize how much I was ripping her off."
qu "I'd charge her extra and pocket the surplus."
scene ep11_pp_quinn2_event41 with dissolve
qu "In time, I almost felt bad for her. This stupid addict couldn't quit smoking and spent all she had on what I could offer."
qu "We started talking more and ended up at the same parties."
scene ep11_pp_quinn2_event42 with dissolve
qu "Before I knew it, she had become something more than my customer. Somehow, she had managed to weasel her way into my life and become my friend."
qu "And I didn't like that. She had gotten way too close to me. And it had to stop."
scene ep11_pp_quinn2_event41 with dissolve
qu "I told her I had charged her extra for the drugs, just to provoke her."
qu "I wanted her to hate me. But she barely got annoyed. She even forgave me."
scene ep11_pp_quinn2_event42 with dissolve
qu "And that got me even madder."
qu "I was mad that she was ok with being used, so I figured I might as well keep using her until she had enough."
scene ep11_pp_quinn2_event43 with dissolve
qu "She started selling drugs and doing my work for me. Now that I had her to do the legwork, I barely had to lift a finger."
qu "She was my marionette. And controlling her became a new normal."
qu "I've kept at it for so long that it doesn't even feel weird anymore."
scene ep11_pp_quinn2_event44 with dissolve
qu "I didn't even think about what I was doing to her. I never put her best interest first."
qu "And at any moment I felt that she was slipping, I'd be sure to correct her..."
qu "...either by saying something nice to manipulate her, or with some tough love."
scene ep11_pp_quinn2_event45 with dissolve
qu "I didn't want the family that was handed to me. So, I treated them like shit."
qu "And I didn't want a friend who wanted to be mine. So, I treated her like shit, too."
qu "I haven't done anything to deserve them."
scene ep11_pp_quinn2_event46 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event47 with dissolve
mc "Why are you telling me all this? I mean...why now?"
scene ep11_pp_quinn2_event48 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event49 with dissolve
qu "Because I don't know if there will be a later."
scene ep11_pp_quinn2_event48 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event49 with dissolve
qu "Riona isn't sick."
qu "Vinny snitched on her to Buddy, and Buddy hurt her."
qu "He ripped her piercings from her face and beat the shit out of her after he found out she's been selling drugs for me."
qu "And he squeezed out every bit of information he needed and learned that I've been overcharging his products for personal gain."
scene ep11_pp_quinn2_event50 with dissolve
qu "And with how he handled it, there's no return from here."
qu "I've always thought I had nothing left to lose, but almost losing Riona made me realize that it didn't have to be like this."
qu "At least not for Riona."
scene ep11_pp_quinn2_event51 with dissolve
mc "Quinn... What the hell?"
scene ep11_pp_quinn2_event50 with dissolve
qu "I know. Say that you're angry with me."
qu "Tell me I'm a parasite and a horrible human being. Just say it."
scene ep11_pp_quinn2_event52 with dissolve
$ wt_ep11_quinn_riona_question_fix = True
if persistent.mod_wtenabled: 
                        $mod_choices = ["(For Quinn Path)","(Possible Riona path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Mod: Both":
        $ wt_ep11_quinn_riona_question=True
        jump wt_ep1_quinn_question_label
    "I won't say it \n{size=-4}[m_c1][mod_choices[0]]":
        label wt_ep1_quinn_question_label:
        $ ep11_quinn_question[1] = True
        mc "I won't say it. You've done horrible things. No one can deny that. But you've had a tough life."
        mc "Growing up the way you did made you refuse to see that you are worthy of something more."
        mc "You're worthy of your family and friends. You're self-sabotaging, treating them like you did."
        scene ep11_pp_quinn2_event53 with dissolve
        qu "No! Say that I'm horrible. I am broken beyond repair and you know it."
        scene ep11_pp_quinn2_event52 with dissolve
        mc "If you had only told me about the bad things you did, I would have believed that."
        mc "But I know that there is another side to you. The one I've seen, and the one I see right now."
        scene ep11_pp_quinn2_event54 with dissolve
        mc "And that's the side that makes me care, spend all this time with you, and sleep with you."
        mc "I'm sure that's the side that made Riona want to be your friend. And the side that made your family keep fighting for you, even when you didn't want it."
        scene ep11_pp_quinn2_event55 with dissolve
        $ renpy.pause()
        scene ep11_pp_quinn2_event56 with dissolve
        $ renpy.pause()
        scene ep11_pp_quinn2_event57 with dissolve
        qu "It's too late, [name]. I'm never gonna change."
        scene ep11_pp_quinn2_event56 with dissolve
        mc "As long as you're still breathing, it's not too late to change."
        mc "But what about Rio? How is she doing now?"
    "I can't defend you \n{size=-4}[m_c2][mod_choices[1]]":
        $ ep11_quinn_question[1] = False
        mc "I... I can't defend you. I guessed something serious was happening, but this...?"
        scene ep11_pp_quinn2_event54 with dissolve
        mc "You haven't had an easy life, but I don't understand how you can choose to use Riona like that... How do you choose to hurt someone wanting to be your friend?"
        mc "Quinn... That's horrible."
        scene ep11_pp_quinn2_event57 with dissolve
        qu "I know. I am horrible. You finally see it, too."
        scene ep11_pp_quinn2_event56 with dissolve
        mc "What about Rio? How is she doing? I thought she was sick, but this changes everything."
scene ep11_pp_quinn2_event57 with dissolve
qu "I went to see her immediately after it happened. It was a sight I wish to forget, but it's etched into my cornea."
qu "She punched me and told me to stay away and never speak to her again."
qu "It took her this long to say it... And when she finally did..."
scene ep11_pp_quinn2_event58 with dissolve
qu "I didn't want her to say it."
qu "With how her face looked... She'll need time to heal. And she'll be scarred..."
qu "I can't believe what he did to her."
scene ep11_pp_quinn2_event56 with dissolve
mc "Fuck... Poor Rio..."
scene ep11_pp_quinn2_event57 with dissolve
qu "You probably feel like you have to do something. To act or help in some way..."
qu "And if you truly want to help me or Rio, I'm asking you this one thing..."
qu "Don't do anything now. I need you to trust me to do the right thing."
scene ep11_pp_quinn2_event56 with dissolve
mc "What is this right thing you're going to do?"
scene ep11_pp_quinn2_event59 with dissolve
qu "I can't make up for what I've already done to Riona, but I owe her this."
qu "I will make Mick, Vinny and Buddy pay for what they did to her."
scene ep11_pp_quinn2_event60 with dissolve
mc "I want to trust you, but I can't just stand by and watch."
scene ep11_pp_quinn2_event62 with dissolve
mc "Quinn... I can't."
scene ep11_pp_quinn2_event59 with dissolve
qu "I've done dangerous things all my life, [name]."
qu "You're scared because this is the first time you're aware of it."
scene ep11_pp_quinn2_event61 with dissolve
qu "And this is why I was scared to tell you the truth."
if ep11_quinn_question[1]:
    qu "When I need you... Trust me. I won't hesitate to let you know."
    qu "I know you want to protect me. But understand that I want to protect you too."
else:
    qu "There is nothing that you can do to help anyone right now."
    qu "If you can't do this for me, do it for Riona."
qu "You're not cut out for this. It's not your kind of life, but it's mine."
scene ep11_pp_quinn2_event63 with dissolve
$ renpy.pause()
scene ep11_pp_quinn2_event64 with dissolve
mc "I need a drink..."
scene ep11_pp_quinn2_event65 with dissolve
qu "[name]?"
scene ep11_pp_quinn2_event67 with dissolve
mc "Yeah?"
scene ep11_pp_quinn2_event66 with dissolve
if ep11_quinn_question[1]:
    qu "Thank you."
else:
    qu "Please... Not a word about this to anyone."
stop music fadeout 3
scene ep11_pp_quinn2_event67 with dissolve
if ep11_quinn_question[1]:
    $ renpy.pause()
else:
    mc "*{i}Sigh{/i}* Fuck..."
scene ep11_pp_quinn2_event68 with dissolve
$ renpy.pause()
if ep11_quinn_question[1]:
    $ new_bio("Quinn", "Quinn opened up and told me what she was up to. She said she wanted to protect me from it all, and I understood why... She's in deep shit.")
else:
    $ new_bio("Quinn", "Quinn opened up and told me what she was up to. I was shocked, worried, and disappointed. I couldn't defend what she had done. She's in deep shit.")
$ new_bio("Quinn", "Quinn told me what happened to Riona. She asked me not to do anything.")
$ new_bio("Riona", "Quinn told me what happened to Riona. She asked me not to do anything.")
$ event_list.append("quinn_act2")
$ mphone_next_song()
$ task_list[8] = ""
$ updateTaskList()
$ currentFreeRoamLabel = "ep11_diks_pp_right_hall_label"
jump endEvent

label ep11_pp_zoey_end_label:
play sound "sound_effects/slap.mp3"
scene ep11_pp_zoey_end107 with vpunch
lea "OW!!!!"
scene ep11_pp_zoey_end108 with dissolve
de "There we go. And now you take a swig of this..."
scene ep11_pp_zoey_end109 with dissolve
de "Aaand you're welcome to stay at the party until you wanna leave."
scene ep11_pp_zoey_end110 with dissolve
lea "Wait a minute! Is that the big punishment you've been hyping all night!?"
scene ep11_pp_zoey_end111 with dissolve
de "Yeah?"
scene ep11_pp_zoey_end110 with dissolve
lea "No fucking way. I had to blow three guys to avoid it. It's tame as hell."
scene ep11_pp_zoey_end111 with dissolve
de "Why are you complaining? If you didn't blow any guys, you got off easy."
scene ep11_pp_zoey_end110 with dissolve
lea "Yeah, but some people left because they feared the punishment and others caved and did theirs."
scene ep11_pp_zoey_end112 with dissolve
de "Well, that's life for you. Enjoy the rest of the party!"

label ep11_pp_zoey_endb_label:
scene ep11_pp_zoey_end1 with dissolve
zo "Ugh..."
scene ep11_pp_zoey_end2 with dissolve
mc "What's ugh?"
scene ep11_pp_zoey_end3 with dissolve
zo "The brain rot I get from talking to that brown-haired chick."
scene ep11_pp_zoey_end2 with dissolve
mc "Becky? Yeah, she's the worst."
if ep7_becky_lewd:
    scene ep11_pp_zoey_end3 with dissolve
    zo "Is that what you really think about her? I've heard otherwise."
    scene ep11_pp_zoey_end2 with dissolve
    mc "She talks a lot. She's got a decent body but an ugly personality."
    mc "What did she say?"
    scene ep11_pp_zoey_end3 with dissolve
    zo "It doesn't matter."
    scene ep11_pp_zoey_end4 with dissolve
if ep11_mg_party:
    mc "I'm gonna leave soon... I've got this thing I gotta do."
    scene ep11_pp_zoey_end5 with dissolve
    zo "You're leaving your own party?"
    scene ep11_pp_zoey_end4 with dissolve
    mc "Yeah. I'm sorry... But I didn't wanna leave before we finished our talk."
    mc "I don't think it would be cool to bring you here and not hear you out."
else:
    mc "How about we continue our chat?"
scene ep11_pp_zoey_end5 with dissolve
zo "Ok... Can we get away from these people?"
stop music fadeout 3
scene ep11_pp_zoey_end4 with dissolve
mc "Let's go to my room."
$ guideSuggestedPage = 219
play music "music/ep11/licensed_music/track175.mp3"
scene ep11_pp_zoey_end6 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end7 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end8 with dissolve
zo "Where do I begin...?"
scene ep11_pp_zoey_end9 with dissolve
mc "Is it something important...?"
scene ep11_pp_zoey_end8 with dissolve
zo "Yeah."
scene ep11_pp_zoey_end9 with dissolve
mc "I'm all ears."
scene ep11_pp_zoey_end10 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end11 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end12 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end13 with dissolve
zo "Do you remember the day we met?"
scene ep11_pp_zoey_end14 with dissolve
mc "In detention? How could I ever forget that day?"
mc "It's etched into my memory."
scene ep11_pp_zoey_end15 with dissolve
zo "That was a bad day for you."
scene ep11_pp_zoey_end16 with dissolve
mc "I'll say."
scene ep11_pp_zoey_end15 with dissolve
zo "For me, it was a standard day. I had lost count of the number of days I spent in detention."
zo "And I could tell that you weren't the typical kid to be there."
scene ep11_pp_zoey_end17 with dissolve
zo "But you were so angry. So, I figured something big must have happened for you to earn detention."
scene ep11_pp_zoey_end18 with dissolve
mc "I remember I wondered what you were there for, too."
scene ep11_pp_zoey_end17 with dissolve
zo "Smoking in class. I was so stupid and edgy back then."
scene ep11_pp_zoey_end19 with dissolve
zo "Do you remember the first thing I said to you?"
scene ep11_pp_zoey_end20 with dissolve
mc "Yeah. \"Do you want some gum?\"."
mc "I wanted that gum, but I turned it down."
scene ep11_pp_zoey_end19 with dissolve
zo "You should have just said yes."
scene ep11_pp_zoey_end20 with dissolve
mc "I didn't want to take it; it was yours."
scene ep11_pp_zoey_end21 with dissolve
zo "I would have felt more comfortable talking to you earlier if you had."
scene ep11_pp_zoey_end22 with dissolve
mc "It worked out eventually, didn't it?"
scene ep11_pp_zoey_end21 with dissolve
zo "It sure did."
scene ep11_pp_zoey_end23 with dissolve
zo "I never told you this, but being in detention with you was the highlight of my day back then."
scene ep11_pp_zoey_end22 with dissolve
mc "It was?"
scene ep11_pp_zoey_end23 with dissolve
zo "Yeah. And you were gonna be there for two months."
zo "So, I smoked in class again on purpose to get more detention, knowing I would spend it with you."
scene ep11_pp_zoey_end22 with dissolve
mc "You did?"
scene ep11_pp_zoey_end21 with dissolve
zo "Stupid, huh?"
scene ep11_pp_zoey_end22 with dissolve
mc "Um, yeah. You could have gotten expelled."
scene ep11_pp_zoey_end23 with dissolve
zo "I know."
scene ep11_pp_zoey_end24 with dissolve
mc "We could have spent time after school, you know? It didn't have to be in detention."
scene ep11_pp_zoey_end25 with dissolve
zo "I was insecure. I wasn't sure if you would want to be around me outside of detention."
zo "I wasn't the best at expressing myself back then."
scene ep11_pp_zoey_end24 with dissolve
mc "Well... Who was?"
scene ep11_pp_zoey_end26 with dissolve
mc "We've come a long way since."
scene ep11_pp_zoey_end27 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end28 with dissolve
zo "Not really."
zo "Even though I draw and write a lot, I'm still not good at expressing myself."
scene ep11_pp_zoey_end27 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end29 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end30 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end31 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end32 with dissolve
zo "Thanks to you, I've realized some things about myself."
zo "And I've felt bad lately because there are many things I want to tell you, but I don't know the best way to say them."
scene ep11_pp_zoey_end33 with dissolve
mc "What has worked for me with you lately is that I say them even though it's hard."
scene ep11_pp_zoey_end32 with dissolve
zo "But I can't say them."

scene ep11_pp_zoey_end34 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end35 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end36 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end37 with dissolve
zo "I..."
scene ep11_pp_zoey_end38 with dissolve
zo "I love you."
scene ep11_pp_zoey_end39 with dissolve
$ renpy.pause()

$ ep11_zscore = 0

if not ep9_mad_at_zoey:
    $ ep11_zscore += 3
if ep11_zoey_hug:
    $ ep11_zscore += 1
if not ep9_derek_better_friend:
    $ ep11_zscore += 1
if ep9_zoey_crash:
    $ ep11_zscore += 1
if ep9_photos[14]:
    $ ep11_zscore += 1
if "Zoey" in ep9_top_three:
    $ ep11_zscore += 1
if not ep10_zoey_jacob:
    $ ep11_zscore += 3
if ep10_zoey_hangout:
    $ ep11_zscore += 2

if zoey_dik:
    scene ep11_pp_zoey_end40 with dissolve
    $ renpy.pause()
    scene ep11_pp_zoey_end42 with dissolve
    if ep11_zscore < 8 or ((ep11_josy_love > 0 or ep11_maya_love > 0) and wt_ep9_branch_numbers == 1):
        $ renpy.pause()
        jump ep11_pp_zoey_reject_no_choice_label
    else:
        if persistent.mod_wtenabled:
                        $mod_choices = ["(Zoey path)","(Possibly ends current path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
        menu:
            "Mod: Zoey path and keep other paths open":
                $ wt_ep11_zoey_kiss_others = True
                jump ep11_pp_zoey_accept_label
            "Return to Zoey \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[1]]":
                jump ep11_pp_zoey_accept_label
            "Reject Zoey":
                jump ep11_pp_zoey_reject_label
else:
    scene ep11_pp_zoey_end40 with dissolve
    $ renpy.pause()
    scene ep11_pp_zoey_end41 with dissolve
    if ep11_zscore < 8 or ((ep11_josy_love > 0 or ep11_maya_love > 0) and wt_ep9_branch_numbers == 1):
        $ renpy.pause()
        jump ep11_pp_zoey_reject_no_choice_label
    else:
        if persistent.mod_wtenabled:
                        $mod_choices = ["(Zoey path)","(Possibly ends current path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
        menu:
            "Mod: Zoey path and keep other paths open":
                $ wt_ep11_zoey_kiss_others = True
                jump ep11_pp_zoey_accept_label
            "Return to Zoey \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[1]]":
                jump ep11_pp_zoey_accept_label
            "Reject Zoey":
                jump ep11_pp_zoey_reject_label

label ep11_pp_zoey_accept_label:
$ ep11_zoey_kiss = 2
scene ep11_pp_zoey_end43 with dissolve
$ renpy.pause()
scene anim_zoey_kiss_ep11 with dissolve
pause
scene anim_zoey_kiss2_ep11 with dissolve
pause
scene ep11_pp_zoey_end44 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end45 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end46 with dissolve
mc "Zoey... What are we doing?"
scene ep11_pp_zoey_end47 with dissolve
zo "We're finally on the same page and being honest, aren't we?"
if not branchAlone:
    scene ep11_pp_zoey_end46 with dissolve
    mc "I'm... I'm in a relationship..."
    if zoey_dik:
        scene ep11_pp_zoey_end47 with dissolve
        zo "I don't care."
        zo "Pick me."
        scene ep11_pp_zoey_end48 with dissolve
        zo "[name]... Pick me."
    else:
        scene ep11_pp_zoey_end45 with dissolve
        $ renpy.pause()
else:
    zo "Don't you feel it, too?"

scene ep11_pp_zoey_end49 with dissolve
mc "..."
mc "I don't know what I feel..."
scene ep11_pp_zoey_end50 with dissolve
mc "Kissing you like this... It..."
mc "It feels different than it ever did before."
scene ep11_pp_zoey_end51 with dissolve
zo "I know."
scene ep11_pp_zoey_end52 with dissolve
mc "Do you love me?"
scene ep11_pp_zoey_end53 with dissolve
zo "Yes."
scene ep11_pp_zoey_end52 with dissolve
mc "Since...when?"
scene ep11_pp_zoey_end53 with dissolve
zo "Does it matter?"
scene ep11_pp_zoey_end52 with dissolve
mc "It does to me."
scene ep11_pp_zoey_end54 with dissolve
zo "..."
scene ep11_pp_zoey_end55 with dissolve
zo "For years."
scene ep11_pp_zoey_end56 with dissolve
mc "Years? Wow..."
scene ep11_pp_zoey_end57 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end58 with dissolve
zo "I know it's a lot to digest."
zo "So, take all the time you need, ok?"
scene ep11_pp_zoey_end59 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end60 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end61 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end62 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end63 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end64 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep11_pp_zoey_end65 with dissolve
$ renpy.pause()
play music "music/ep11/licensed_music/track182.mp3"
$ new_bio("Zoey", "Zoey told me she loved me and started kissing me. I kissed her back.")
if not branchAlone:
    if steamAchievements:
        $ achievement.grant("IDS3_35")
        init:
            $ achievement.register("IDS3_35")
        $ achievement.Sync()
if wt_ep11_party_bella:
    jump ep11_main2_party_label

jump ep11_main2_party_end_label

label ep11_pp_zoey_end2b_label:
play music "music/ep_interlude/licensed_music/track107.mp3"
scene ep11_pp_zoey_end66 with fade
$ renpy.pause()
scene ep11_pp_zoey_end67 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end68 with dissolve
$ renpy.pause()
if ep11_mg_party and not wt_ep11_party_bella:
    scene ep11_pp_zoey_end69 with dissolve
    zo "You never left tonight."
    scene ep11_pp_zoey_end70 with dissolve
    mc "After what happened between us, I couldn't."
    scene ep11_pp_zoey_end71 with dissolve
    $ renpy.pause()
scene ep11_pp_zoey_end70 with dissolve
mc "So, what now?"
scene ep11_pp_zoey_end69 with dissolve
zo "You should ask yourself that."
scene ep11_pp_zoey_end70 with dissolve
mc "I wish it was a simple question."
scene ep11_pp_zoey_end71 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end72 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end73 with dissolve
$ renpy.pause()
if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
    scene ep11_pp_zoey_end74 with dissolve
    mc "I'm supposed to go Christmas shopping tomorrow."
    scene ep11_pp_zoey_end75 with dissolve
    zo "Is that what's on your mind?"
    scene ep11_pp_zoey_end74 with dissolve
    if branchMayaJosy:
        mc "How can I buy Christmas gifts for my girlfriends now?"
        if not ep10_zoey_hangout:
            scene ep11_pp_zoey_end76 with dissolve
            zo "Girlfriends? Plural?"
            scene ep11_pp_zoey_end74 with dissolve
            mc "I'm dating two girls, yes."
            scene ep11_pp_zoey_end76 with dissolve
            zo "Whoa..."
            scene ep11_pp_zoey_end74 with dissolve
            mc "It's a long story."
    else:
        mc "How can I buy a Christmas gift for my girlfriend now?"
    scene ep11_pp_zoey_end75 with dissolve
    zo "It sounds like you have some thinking to do."
    if not zoey_dik:
        zo "But now you know where I stand."
        zo "I'm sorry you'd have to hurt someone to be with me. But I don't want to have any more regrets about us."
        zo "I know I want this. And it feels so good to finally say it out loud to you."
    else:
        zo "But now you know where I stand. And it feels so good to finally say it out loud to you."
scene ep11_pp_zoey_end74 with dissolve
mc "It's a big decision... And you've only been back for what? Not even two months?"
mc "And I tried so hard to get over you."
scene ep11_pp_zoey_end77 with dissolve
if zoey_dik:
    mc "And all it took was you kissing me to undo all that healing."
else:
    mc "And the moment I realized I could kiss you, I did and all that healing was undone."
mc "Since we're being honest with each other now..."
mc "I'm worried that I kissed you for the wrong reasons."
scene ep11_pp_zoey_end75 with dissolve
zo "What do you mean?"
scene ep11_pp_zoey_end78 with dissolve
mc "I'm worried that I kissed you because it felt safe and familiar and because this was something I subconsciously always wanted when we were younger."
mc "As opposed to kissing you because it was something I wanted right now."
scene ep11_pp_zoey_end79 with dissolve
mc "I have moved on since you left. Is kissing you a way for me to cling to the past...?"
mc "...or did I do it because my feelings for you are true even today?"
scene ep11_pp_zoey_end80 with dissolve
zo "You have moved on, but in so many ways, you're still the same person I've always known."
zo "[name], I don't think you romanticize our youth and years together."
zo "I know I'm not."
scene ep11_pp_zoey_end81 with dissolve
zo "But I've struggled to put words to my feelings, too. I can't believe I told you what I did tonight..."
zo "So, I understand why you can't find words for it now."
scene ep11_pp_zoey_end80 with dissolve
zo "I don't want you to be with me if you're not sure."
scene ep11_pp_zoey_end82 with dissolve
zo "And we can do it however you want to help you figure it out."
zo "Slow, fast, with or without space. Anything you need."
stop music fadeout 3
zo "Because I know I want you, and if the tiniest part of you still wants it... I'm going to fight for you."
scene ep11_pp_zoey_end83 with dissolve
$ renpy.pause()
if ep11_mg_party:
    $ new_bio("You", "After kissing Zoey, I stayed with her at the DIKs' Christmas Panty party.")
    $ new_bio("Zoey", "After kissing Zoey, I stayed with her at the DIKs' Christmas Panty party.")
$ new_bio("Zoey", "Zoey told me she would fight for me and help me in any way I wanted to figure out my feelings.")
jump ep11_gift_label

label ep11_pp_zoey_reject_label:
$ ep11_zoey_kiss = 1
scene ep11_pp_zoey_end84 with dissolve
mc "What's happening right now?"
scene ep11_pp_zoey_end85 with dissolve
zo "I think you know."
if not branchAlone:
    scene ep11_pp_zoey_end84 with dissolve
    mc "I'm... I'm in a relationship..."
    if zoey_dik:
        scene ep11_pp_zoey_end47 with dissolve
        zo "I don't care."
        zo "Pick me."
        scene ep11_pp_zoey_end48 with dissolve
        zo "[name]... Pick me."
    else:
        scene ep11_pp_zoey_end45 with dissolve
        $ renpy.pause()
scene ep11_pp_zoey_end49 with dissolve
mc "..."
mc "I don't know what I feel..."
scene ep11_pp_zoey_end52 with dissolve
mc "Do you love me?"
scene ep11_pp_zoey_end53 with dissolve
zo "Yes."
scene ep11_pp_zoey_end52 with dissolve
mc "Since...when?"
scene ep11_pp_zoey_end53 with dissolve
zo "Does it matter?"
scene ep11_pp_zoey_end52 with dissolve
mc "It does to me."
scene ep11_pp_zoey_end54 with dissolve
zo "..."
scene ep11_pp_zoey_end55 with dissolve
zo "For years."
scene ep11_pp_zoey_end56 with dissolve
mc "Years? Wow..."
scene ep11_pp_zoey_end57 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end58 with dissolve
zo "I know it's a lot to digest."
zo "Take all the time you need, ok?"
scene ep11_pp_zoey_end86 with dissolve
mc "I can't do this, Zoey. I can't."
mc "Since you left, I've moved on."
scene ep11_pp_zoey_end87 with dissolve
mc "Getting back together with you would be safe and familiar, and it was something I had subconsciously always wanted when we were younger."
mc "But...I don't think it's true to me today."
scene ep11_pp_zoey_end88 with dissolve
zo "You have moved on, but in so many ways, you're still the same person I've always known, [name]."
zo "I don't think you're romanticizing our youth and the years we spent together."
zo "I know I'm not."
scene ep11_pp_zoey_end89 with dissolve
zo "But I've struggled to put words to my feelings, too. So, I completely understand why you can't do it now, either."
scene ep11_pp_zoey_end88 with dissolve
zo "I don't want you to be with me if you're not sure."
zo "And we can do it however you want, to help you figure it out."
scene ep11_pp_zoey_end90 with dissolve
zo "Slow, fast, with or without space. Anything you need."
zo "Because I know I want you."
scene ep11_pp_zoey_end90b with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end92 with dissolve
mc "No... I can't."
mc "It's... Way too late."
scene ep11_pp_zoey_end93 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end94 with dissolve
zo "So, you're saying...?"
zo "Never?"
jump ep11_pp_zoey_reject_pt2_label

label ep11_pp_zoey_reject_no_choice_label:
$ ep11_zoey_kiss = 0
scene ep11_pp_zoey_end86 with dissolve
mc "Um... Zoey?"
scene ep11_pp_zoey_end91 with dissolve
zo "..."
zo "No..."
scene ep11_pp_zoey_end92 with dissolve
mc "It's too late for this."
mc "It's... Way too late."
scene ep11_pp_zoey_end93 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end94 with dissolve
zo "So, you're saying...?"
zo "Never?"
label ep11_pp_zoey_reject_pt2_label:

scene ep11_pp_zoey_end95 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end96 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end97 with dissolve
zo "*{i}Scoffs{/i}*"
scene ep11_pp_zoey_end98 with dissolve
mc "Zoey, I'm sorry."
scene ep11_pp_zoey_end99 with dissolve
zo "Don't be."
zo "It's not a big deal."
scene ep11_pp_zoey_end100 with dissolve
mc "It is. You told me you love me."
scene ep11_pp_zoey_end101 with dissolve
zo "Yeah, but what do I know? I don't know what love is."
scene ep11_pp_zoey_end102 with dissolve
$ renpy.pause()
scene ep11_pp_zoey_end101 with dissolve
zo "I'm gonna take off."
scene ep11_pp_zoey_end103 with dissolve
mc "Not like this."
scene ep11_pp_zoey_end104 with dissolve
zo "There's no good way to end this anyway."
zo "Fuck... I should have kept my mouth shut."
scene ep11_pp_zoey_end105 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep11_pp_zoey_end106 with dissolve
$ renpy.pause()
$ new_bio("Zoey", "Zoey told me she loved me but I told her it was too late, and I had to let her down.")

if ep11_mg_party or wt_ep11_party_bella:
    jump ep11_main2_party_label
else:
    jump ep11_main2_party_end_label

label ep11_pp_leon_event_label:
$ guideSuggestedPage = 205
scene ep11_pp_leon_event1 with dissolve
$ renpy.pause()
scene ep11_pp_leon_event2 with dissolve
le "Dammit..."
scene ep11_pp_leon_event4 with dissolve
mc "What's wrong?"
scene ep11_pp_leon_event3 with dissolve
le "I keep striking out with my mission."
scene ep11_pp_leon_event4 with dissolve
mc "Didn't you pull a good one?"
scene ep11_pp_leon_event5 with dissolve
le "It is a awesome one! It's a guaranteed lay."
le "If I can only find who I'm looking for."
scene ep11_pp_leon_event4 with dissolve
mc "Find who?"
scene ep11_pp_leon_event3 with dissolve
le "I'm supposed to find a chick named 'Y' and fuck her."
scene ep11_pp_leon_event6 with dissolve
mc "(Hm... I could either tell Leon that Elena is 'Y' or I could tell Elena that Leon is 'X' and have her decide what to do.)"

if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Elena scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if ep9_heather_lewd == 2:
                           $ mod_choices[6]="(Possible Elena scene)"
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

if ep10_elena_offer:
    menu:
        "Tell him about Elena":
            label ep11_pp_leon_eventa_label:
            scene ep11_pp_leon_event7 with dissolve
            mc "I know who you're looking for."
            scene ep11_pp_leon_event8 with dissolve
            le "You do!? Tell me."
            scene ep11_pp_leon_event7 with dissolve
            mc "It's Elena."
            scene ep11_pp_leon_event9 with dissolve
            le "Oh, man... Damn. I thought it was someone single."
            scene ep11_pp_leon_event7 with dissolve
            mc "She seemed up for it."
            scene ep11_pp_leon_event10 with dissolve
            le "Whaaaat?"
            scene ep11_pp_leon_event11 with dissolve
            mc "You should tell her you're 'X' at least."
            scene ep11_pp_leon_event9 with dissolve
            if ep9_heather_lewd == 2:
                le "No, I'm not going to be the next Nick or you. No offense."
            else:
                le "No, I'm not going to be the next Nick."
            scene ep11_pp_leon_event7 with dissolve
            mc "Do you know what you should do? Get another mission from the bowl. There's still time."
            scene ep11_pp_leon_event9 with dissolve
            le "You're not gonna tell Derek, are you? I don't wanna face any consequences. I fear he'll have weird ones."
            scene ep11_pp_leon_event7 with dissolve
            mc "Haha! No, I've got your back."
            scene ep11_pp_leon_event12 with dissolve
            le "Awesome. Thanks, [name]."
            $ new_bio("Leon", "I told Leon who he'd been looking for when searching for 'Y' at the DIKs' Christmas Panty party.")
            $ event_list.append("ep11_pp_elena1_event_label")
        "Tell Elena about Leon":
            label ep11_pp_leon_eventb_label:
            scene ep11_pp_leon_event7 with dissolve
            mc "Sounds hot. I'll see what I can find out."
            scene ep11_pp_leon_event12 with dissolve
            le "Will you? That would be great."
            scene ep11_pp_leon_event7 with dissolve
            mc "No problem."
            $ new_bio("Leon", "I didn't tell Leon who he'd been looking for when searching for 'Y' at the DIKs' Christmas Panty party.")
            $ event_list.append("ep11_pp_elena2_event_label")
        "Make him give you the mission \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
            $ dk(2)
            mc "(Or...maybe I can make Leon hand me his mission and I tell Elena I'm 'X'... That's a fun prank...)"
            scene ep11_pp_leon_event7 with dissolve
            mc "Hm... That sounds like a bad mission to me."
            scene ep11_pp_leon_event12 with dissolve
            le "No way! It's a hot one. I could bang someone I wouldn't have a shot with."
            scene ep11_pp_leon_event7 with dissolve
            mc "Or... Hm... No."
            scene ep11_pp_leon_event9 with dissolve
            le "What?"
            scene ep11_pp_leon_event11 with dissolve
            mc "Maybe it's not a girl."
            scene ep11_pp_leon_event8 with dissolve
            le "'Y' could be a guy... Fuck!"
            scene ep11_pp_leon_event11 with dissolve
            mc "Maybe that's why you haven't found who it is."
            scene ep11_pp_leon_event9 with dissolve
            le "Have you heard any guys ask for 'X'?"
            scene ep11_pp_leon_event11 with dissolve
            mc "No, but I wouldn't take the chance if I were you."
            mc "You know what you should do? Grab a new mission from the bowl. There's still time."
            scene ep11_pp_leon_event9 with dissolve
            le "You're not gonna tell Derek, are you? I don't wanna face any consequences. I fear he'll have a weird one."
            scene ep11_pp_leon_event7 with dissolve
            mc "Haha! No, I've got your back. Give me that mission and I'll take care of it."
            scene ep11_pp_leon_event13 with dissolve
            le "Awesome. Thanks, [name]."
            scene ep11_pp_leon_event14 with dissolve
            mc "(Ok, that was a dick move. But I'm 'X' now... Should I tell Elena?)"
            $ new_bio("Leon", "I made Leon give me his Dirty Bowl mission after discovering he was searching for 'Y' at the DIKs' Christmas Panty party.")
            $ event_list.append("ep11_pp_elena3_event_label")
else:
    $ guideSuggestedPage = 206
    menu:
        "Tell him about Elena":
            jump ep11_pp_leon_eventa_label
        "Tell Elena about Leon":
            jump ep11_pp_leon_eventb_label
if persistent.mod_wtenabled:
    $ optional_task_list[1] = "Talk to Elena (Upper Main room)"
else:
    $ optional_task_list[1] = "Talk to Elena"
$ updateTaskList()
jump endEvent

label ep11_pp_elena1_event_label:
scene ep11_pp_elena1_event1 with dissolve
mc "Bad news. The 'X' mission isn't in play tonight."
scene ep11_pp_elena1_event2 with dissolve
el "Aw, it's not?"
scene ep11_pp_elena1_event1 with dissolve
mc "Nope. You should get another mission."
scene ep11_pp_elena1_event2 with dissolve
el "It wasn't my mission; it was John Boy's."
scene ep11_pp_elena1_event1 with dissolve
mc "Wait... John Boy's been looking for 'X'?"
scene ep11_pp_elena1_event3 with dissolve
el "Yeah. Mine was to give a blowjob to someone. I'll do that with John Boy later."
scene ep11_pp_elena1_event1 with dissolve
mc "(Leon dodged a bullet. Haha!)"
scene ep11_pp_elena1_event3 with dissolve
el "Thanks for letting me know. I'll tell John Boy about it."
$ optional_task_list[1] = ""
$ updateTaskList()
$ new_bio("Elena", "I covered for Leon with The Dirty Bowl mission.")
$ new_bio("Leon", "I covered for Leon with The Dirty Bowl mission.")
jump endEvent

label ep11_pp_elena2_event_label:
scene ep11_pp_elena1_event1 with dissolve
mc "I found out who 'X' is..."
scene ep11_pp_elena2_event1 with dissolve
el "Shut up! You did?"
scene ep11_pp_elena2_event2 with dissolve
mc "It's Leon."
scene ep11_pp_elena2_event3 with dissolve
el "Hahaha!"
scene ep11_pp_elena2_event2 with dissolve
mc "Not the guy you were hoping for?"
scene ep11_pp_elena2_event3 with dissolve
el "Guy? Haha! I was hoping for a girl."
scene ep11_pp_elena2_event2 with dissolve
mc "Oh, nice."
scene ep11_pp_elena2_event3 with dissolve
el "John Boy will be sad, as he spent all night looking for Leon."
scene ep11_pp_elena1_event1 with dissolve
mc "Wait... John Boy's been looking for 'X'? I thought it was your mission."
scene ep11_pp_elena2_event3 with dissolve
el "Hahaha! No! It was his mission."
scene ep11_pp_elena1_event3 with dissolve
el "Mine was to give a blowjob to someone. I'll do that with John Boy later."
scene ep11_pp_elena1_event1 with dissolve
mc "Haha! Poor Leon is out there still looking for 'Y'... Should we tell him?"
scene ep11_pp_elena2_event3 with dissolve
el "No, let them look for each other. It will be funny when they realize who they've been looking for."
$ optional_task_list[1] = ""
$ updateTaskList()
$ new_bio("Elena", "I told Elena that Leon had the other end of her Dirty Bowl mission. She revealed it was John Boy's mission. We laughed and let them keep searching for each other at the party.")
jump endEvent

label ep11_pp_elena3_event_label:
scene ep11_pp_elena1_event1 with dissolve
mc "I found out who 'X' is..."
scene ep11_pp_elena2_event1 with dissolve
el "Shut up! You did?"
scene ep11_pp_elena3_event1 with dissolve
$ renpy.pause()
scene ep11_pp_elena3_event2 with dissolve
el "When did you get that?"
scene ep11_pp_elena3_event3 with dissolve
mc "What does it matter? I have it."
scene ep11_pp_elena3_event4 with dissolve
el "Well, you didn't have that one before. Sounds to me that you found it after I asked you to find out who 'X' was."
scene ep11_pp_elena3_event3 with dissolve
mc "Haha, guilty! Leon had it and I made him give it to me."
scene ep11_pp_elena3_event4 with dissolve
el "Well, John Boy is somewhere around here. Go get him."
scene ep11_pp_elena3_event3 with dissolve
mc "Huh? What do you mean?"
scene ep11_pp_elena3_event4 with dissolve
el "It's John Boy's mission."
el "Oh, you didn't think it was mine, did you?"
scene ep11_pp_elena3_event5 with dissolve
mc "No... Of course not."
scene ep11_pp_elena3_event6 with dissolve
el "Oh my God! You so did."
el "Hahaha!"
scene ep11_pp_elena3_event7 with dissolve
el "And you intended to carry it out, didn't you?"
scene ep11_pp_elena3_event8 with dissolve
mc "I remember the chat we had about it. So..."
scene ep11_pp_elena3_event9 with dissolve
el "You were serious about that?"
scene ep11_pp_elena3_event10 with dissolve
mc "Yeah. If you two were."
scene ep11_pp_elena3_event9 with dissolve
el "Aren't you worried it would change our friendship dynamics? Because I am."
scene ep11_pp_elena3_event10 with dissolve
mc "I haven't thought about that. I mean, sex is sex. It doesn't have to mean anything more than that."
scene ep11_pp_elena3_event9 with dissolve
el "Yeah, if you were some random guy, sure. But you're a close friend...so I'm not sure."
scene ep11_pp_elena3_event8 with dissolve
mc "If you're uncomfortable with it, I won't push it. I thought both of you wanted it, that's all."
scene ep11_pp_elena3_event9 with dissolve
el "I'll think about it."

$ ep11_x = True
if "part2_act2" in event_list:
    $ event_list.append("ep11_pp_elena_lewd_event_label")
    if persistent.mod_wtenabled:
        $ task_list[1] = "Find Elena (John Boy's room)"
    else:
        $ task_list[1] = "Find Elena"
$ new_bio("Elena", "I showed Elena the other end of her Dirty Bowl mission. She revealed it was John Boy's mission and realized I had been sneaky and gotten that mission on purpose.")
$ optional_task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_elena_lewd_event_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep9_heather_lewd = 0
    $ event_list = []
    play music "music/ep11/licensed_music/track181.mp3"
    queue music ["music/ep11/licensed_music/track178.mp3","music/ep11/licensed_music/track180.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track182.mp3"]
hide screen new_phone_screen
scene ep11_pp_elena_lewd_event1 with dissolve
jb "Yes... Fuck. That's it. Squeeze it."
scene ep11_pp_elena_lewd_event2 with dissolve
el "Fuck me, baby!"
scene ep11_pp_elena_lewd_event3 with dissolve
mc "Whoa! I'm so sorry."
if ep9_heather_lewd == 2:
    scene ep11_pp_elena_lewd_event4 with dissolve
    jb "Leave, [name]. I'm close here."
    scene ep11_pp_elena_lewd_event5 with dissolve
    mc "Sorry, sorry! I'm gone."
    scene ep11_pp_elena_lewd_event8 with dissolve
    el "Why did you make him leave? I thought you wanted him to join."
    scene ep11_pp_elena_lewd_event9 with dissolve
    jb "Eh... The whole Heather situation turned me off."
    jb "He did that behind Tommy's back. I don't want to jeopardize our relationship when I know he's capable of doing that to Tommy."
    scene ep11_pp_elena_lewd_event8 with dissolve
    el "Ok, baby. I get it."
    el "Come on, don't get soft inside me."
    $ new_bio("John Boy", "John Boy didn't like it when I walked in on Elena and him having sex.")
else:
    scene ep11_pp_elena_lewd_event6 with dissolve
    jb "Haha! Well, if it isn't 'X'?"
    scene ep11_pp_elena_lewd_event12 with dissolve
    mc "You told him about that?"
    scene ep11_pp_elena_lewd_event13 with dissolve
    el "Of course. We have no secrets between us."
    scene ep11_pp_elena_lewd_event6 with dissolve
    jb "My brother. No offense, but I ditched that mission for another one. You should, too."
    scene ep11_pp_elena_lewd_event7 with dissolve
    mc "It's too late now for those missions, anyway."
    scene ep11_pp_elena_lewd_event10 with dissolve
    jb "You hear that, babe? That means you didn't finish yours."
    scene ep11_pp_elena_lewd_event8 with dissolve
    el "I could give you one...or do you want him to get one?"
    scene ep11_pp_elena_lewd_event11 with dissolve
    jb "Oh, hell yeah!"
    scene ep11_pp_elena_lewd_event13 with dissolve
    el "[name], I thought about it and you're right. Sex is just sex."
    el "You can put your cock in my mouth if you want. I have to blow someone tonight."
    scene ep11_pp_elena_lewd_event14 with dissolve
    el "John Boy's going soft inside me. You should do it now."
    scene ep11_pp_elena_lewd_event15 with dissolve
    if "quinn_act2" in event_list:
        mc "Sorry, maybe another time. I'm not in the mood for it tonight."
        jump ep11_pp_elena_lewd_no_label
    menu:
        "Get a blowjob":
            $ ep11_elena_lewd = True
            mc "Are you sure?"
            scene ep11_pp_elena_lewd_event16 with dissolve
            $ renpy.pause()
            scene ep11_pp_elena_lewd_event17 with dissolve
            $ renpy.pause()
            scene ep11_pp_elena_lewd_event18 with dissolve
            jb "Oh, fuck. That's hot."
            scene ep11_pp_elena_lewd_event19 with dissolve
            el "Baby, be quiet. You might scare him away."
            scene ep11_pp_elena_lewd_event18 with dissolve
            jb "Yeah, yeah. Got it."
            scene ep11_pp_elena_lewd_event20 with dissolve
            $ renpy.pause()
            scene anim_elena_bj1_ep11 with dissolve
            el "*{i}Suck suck{/i}*"
            pause
            scene anim_elena_bj2_ep11 with dissolve
            mc "Fuck... You give great head."
            el "*{i}Suck glug glug{/i}*"
            jb "She does, doesn't she?"
            pause
            scene ep11_pp_elena_lewd_event21 at hpunch, cum1
            $ renpy.pause(0.5)
            scene ep11_pp_elena_lewd_event21 at hpunch, cum1
            $ renpy.pause(0.5)
            scene ep11_pp_elena_lewd_event21 at hpunch, cum1
            jb "Hngn!"
            el "*{i}Gasps{/i}* Ahhh..."
            scene ep11_pp_elena_lewd_event22 with dissolve
            el "God, he just came inside me."
            scene ep11_pp_elena_lewd_event23 with dissolve
            el "Was it too hot for you?"
            scene ep11_pp_elena_lewd_event24 with dissolve
            jb "You don't even know half of it... Keep going!"
            scene ep11_pp_elena_lewd_event25 with dissolve
            jb "Thanks for doing this, baby. This will go right into my spank bank."
            jb "Show me how deep you can take it."
            scene anim_elena_bj3_ep11 with dissolve
            el "*{i}Suck suck{/i}*"
            scene anim_elena_bj4_ep11 with dissolve
            pause
            scene anim_elena_bj5_ep11 with dissolve
            mc "Hey... I'm gonna cum... Do you want it in your throat, or..."
            pause
            scene ep11_pp_elena_lewd_event26 at hpunch, cum1
            mc "Ahhh!!!"
            scene ep11_pp_elena_lewd_event26 at hpunch, cum1
            $ renpy.pause(0.5)
            scene ep11_pp_elena_lewd_event26 at hpunch, cum1
            $ renpy.pause(0.5)
            scene ep11_pp_elena_lewd_event27 with dissolve
            el "*{i}Coughs{/i}*"
            scene ep11_pp_elena_lewd_event28 with dissolve
            el "*{i}Phew{/i}*"
            el "I can't believe I could take all of that."
            scene ep11_pp_elena_lewd_event29 with dissolve
            jb "Dude... That was...phenomenal!"
            scene ep11_pp_elena_lewd_event30 with dissolve
            mc "I'm not sure what to say to you two now. This was...new."
            scene ep11_pp_elena_lewd_event31 with dissolve
            jb "No words needed, brother. You just fulfilled a fantasy of mine. Up top!"
            play sound "sound_effects/slap.mp3"
            scene ep11_pp_elena_lewd_event32 with hpunch
            $ renpy.pause()
            scene ep11_pp_elena_lewd_event33 with dissolve
            el "Was it good for you, baby?"
            scene ep11_pp_elena_lewd_event34 with dissolve
            jb "I couldn't hold it for 20 seconds after I saw you suck him off."
            jb "I knew it would turn me on, but I didn't expect it to have that big effect."
            jb "Come here. I wanna know what you thought about it."
            scene ep11_pp_elena_lewd_event35 with dissolve
            mc "(And he's making out with her after I finished in her mouth and throat...)"
            mc "(Time to leave.)"
            $ renpy.end_replay()
            $ persistent.ep11_lewd_elena = True
            $ calcScenes()
            $ new_bio("John Boy", "John Boy was elated to watch me get a blowjob from Elena at the DIKs' Christmas Panty party.")
            $ new_bio("Elena", "Elena gave me a blowjob at the DIKs' Christmas Panty party while John Boy was watching.")
            $ mphone_stats_add_girl_s3("elena","You received a blowjob from Elena at the Christmas Panty party in episode 11.")
        "Leave" if not _in_replay:
            mc "You know what...? I thought I'd be ok with it, but it just hit me that it's too weird for me. Sorry, but I can't do this."
            label ep11_pp_elena_lewd_no_label:
            scene ep11_pp_elena_lewd_event6 with dissolve
            jb "Come on! Just do it! She gives great head."
            scene ep11_pp_elena_lewd_event7 with dissolve
            mc "Hm... Sorry. But have fun!"
            scene ep11_pp_elena_lewd_event9 with dissolve
            jb "Dammit. I thought we had him."
            scene ep11_pp_elena_lewd_event8 with dissolve
            el "It's ok, baby. Come on, get hard again for me."
            $ new_bio("John Boy", "Elena and John Boy asked me to join them while they were having sex, but I didn't.")
            $ new_bio("Elena", "Elena and John Boy asked me to join them while they were having sex, but I didn't.")

$ event_list.append("part2_elena")
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_lily_event_label:
if ep11_nicole_over_lily:
    scene ep11_pp_lily_event8 with dissolve
    ly "Hey... Nicole brought me up to speed on what you told her."
    scene ep11_pp_lily_event9 with dissolve
    mc "I was going to tell you."
    scene ep11_pp_lily_event8 with dissolve
    ly "So... That's it, huh?"
    scene ep11_pp_lily_event9 with dissolve
    mc "You were right. I should have told her about us rolling earlier."
    mc "And while I've had fun doing it with you, I'd like to see if there's something more between me and Nicole."
    scene ep11_pp_lily_event10 with dissolve
    mc "And since she admitted she felt weird dating me while you and I were rolling, I chose what I thought was best."
    scene ep11_pp_lily_event11 with dissolve
    ly "You better treat her the way she deserves."
    scene ep11_pp_lily_event10 with dissolve
    mc "I'll try my best."
    scene ep11_pp_lily_event12 with dissolve
    mc "Hey, I had fun rolling with you. I wasn't the best at it, but I had fun."
    mc "I hope we can still hang out and such."
    scene ep11_pp_lily_event13 with dissolve
    ly "Sure."
    mc "(I think she was hurt by that... But I also think she'd never admit it.)"
    $ new_bio("Lily", "Lily and I stopped rolling because I would rather keep dating Nicole.")
    $ task_list[12] = ""
    $ updateTaskList()
    jump endEvent
$ ep11_rolling = True
scene ep11_pp_lily_event1 with dissolve
lea "Are you free to help us? We need two more guys for body shots."
scene ep11_pp_lily_event2 with dissolve
mc "Body shots? Is it for your missions?"
scene ep11_pp_lily_event3 with dissolve
lea "Haha! No, we're just doing them for fun."
scene ep11_pp_lily_event4 with dissolve
fel "You're not going to say no to having wet tongues all over your body, are you?"
scene ep11_pp_lily_event5 with dissolve
$ renpy.pause()
scene ep11_pp_lily_event6 with dissolve
ly "[name]? Let's go."
lea "Hey? What the hell?"
scene ep11_pp_lily_event7 with dissolve
mc "Right behind you, Queen."
jump ep11_lily_lewd_label

label ep11_lily_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep11_lily_want_more = True
    $ ep10_date_nicole = False
    $ ep10_cancel_date_nicole = False
    play music "music/ep11/licensed_music/track182.mp3"
    queue music ["music/ep11/licensed_music/track177.mp3","music/ep11/licensed_music/track178.mp3","music/ep11/licensed_music/track180.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track182.mp3"]
hide screen new_phone_screen
scene ep11_lily_lewd1 with dissolve
ly "I was worried you wouldn't let me steal you for a minute."
scene ep11_lily_lewd2 with dissolve
mc "No questions asked, remember?"
scene ep11_lily_lewd3 with dissolve
ly "Yeah, but I wasn't sure how you'd react when thirsty girls fight over you."
scene ep11_lily_lewd4 with dissolve
mc "Girls are wilder tonight, for sure. I'm not sure if it's because of the masks or if people are feeling extra horny seeing each other wear almost nothing."
scene ep11_lily_lewd5 with dissolve
ly "I doubt it's the masks, they don't cover shit, and Halloween didn't bring this much crazy out of people."
ly "Your brothers are walking around with boners, and girls are being extra slutty too."
ly "I doubt people will be able to look at each other the same tomorrow."
scene ep11_lily_lewd6 with dissolve
mc "I'll look at you as I did before."
if ep11_lily_want_more:
    scene ep11_lily_lewd7 with dissolve
    ly "I hate to break it to you, but you're not."
    ly "The look in your eyes has changed."
    scene ep11_lily_lewd8 with dissolve
    mc "It's called alcohol, Lily. It has that effect."
    scene ep11_lily_lewd7 with dissolve
    ly "That's not it. You look hungrier for me than usual."
else:
    scene ep11_lily_lewd7 with dissolve
    ly "Hm... But not tonight."
    scene ep11_lily_lewd8 with dissolve
    mc "It's called alcohol, Lily. It has that effect."
    scene ep11_lily_lewd7 with dissolve
    ly "Is that it? You look hungrier for me than usual."
scene ep11_lily_lewd9 with dissolve
mc "Did you look at what you're wearing tonight? Isn't it obvious why I look at you with hungry eyes?"
scene ep11_lily_lewd7 with dissolve
ly "It's not just tonight, though."
scene ep11_lily_lewd8 with dissolve
if ep11_lily_want_more:
    mc "I don't know, Lily..."
else:
    mc "Maybe it's you who are looking at me differently because I don't feel like I have changed."

if ep10_date_nicole and not ep10_cancel_date_nicole:
    scene ep11_lily_lewd7b with dissolve
    ly "Nicole told me you talked to her."
    scene ep11_lily_lewd8b with dissolve
    mc "Yeah, you were right. It had to be done."
    scene ep11_lily_lewd7b with dissolve
    ly "You didn't let her down just for me, did you?"
    scene ep11_lily_lewd8b with dissolve
    mc "For you? Why are you asking me that? What do you want me to tell you?"

mc "I'm trying to be as aloof around you as possible. And I had fun at the party as always."
scene ep11_lily_lewd10 with dissolve
ly "Yeah, you sure are having fun attracting attention tonight."
scene ep11_lily_lewd11 with dissolve
mc "Wait a minute... Was that jealousy I heard?"
scene ep11_lily_lewd12 with dissolve
ly "No, that wasn't jealousy."
scene ep11_lily_lewd13 with dissolve
mc "Uh-huh... You're stealing me from the party for no reason this time."
mc "Usually, you want to parade me around others or make some statement, but this time, you pulled me away from the fun."
scene ep11_lily_lewd14 with dissolve
ly "Again, wrong. They saw me yoink the guy they wanted to bang in front of their eyes."
ly "That's all there was to it."
scene ep11_lily_lewd15 with dissolve
mc "If you say so. I thought it was something else, but apparently, I was wr-"
scene anim_lily_kiss_ep11 with dissolve
ly "*{i}Smack{/i}*"
pause
scene ep11_lily_lewd16 with dissolve
mc "...wrong."
scene ep11_lily_lewd17 with dissolve
ly "Don't make a big deal out of it. Can't a girl be drunk and horny?"
scene ep11_lily_lewd18 with dissolve
mc "..."
scene ep11_lily_lewd19 with dissolve
ly "There's that look again... Damn you, [name]..."
scene anim_lily_kiss_ep11 with dissolve
ly "*{i}Smack{/i}*"
pause
scene ep11_lily_lewd20 with dissolve
$ renpy.pause()
scene ep11_lily_lewd21 with dissolve
$ renpy.pause()

scene ep11_lily_lewd22 with dissolve
$ renpy.pause()

scene anim_lily_bj_ep11 with dissolve
ly "*{i}Suck suck{/i}*"
pause
scene anim_lily_bj2_ep11 with dissolve
ly "*{i}Suck gulp{/i}*"
pause

scene ep11_lily_lewd23 with dissolve
ly "*{i}Lick lick{/i}*"
scene ep11_lily_lewd24 with dissolve
ly "You're being too quiet..."
scene ep11_lily_lewd25 with dissolve
mc "Sorry, I just..."
scene ep11_lily_lewd24 with dissolve
ly "Grab my head and fuck it, ok? Get rough with me."

scene anim_lily_bj3_ep11 with dissolve
ly "*{i}Suck suck{/i}* Yes! Like that..."
pause
scene anim_lily_bj4_ep11 with dissolve
ly "*{i}Suck gag suck{/i}*"
pause
scene anim_lily_bj5_ep11 with dissolve
pause

scene bg anim_lily_bj6_ep11 movie with dissolve
ly "*{i}Gag{/i}* *{i}Cough{/i}*"
pause

scene ep11_lily_lewd26 with dissolve
$ renpy.pause()
scene ep11_lily_lewd27 with dissolve
if ep11_lily_want_more:
    mc "(There's tension between us... I'm not imagining it.)"
    mc "(I promised her I'd try to stay aloof and away from the feelings and all...)"
    menu:
        "Fuck her hard":
            $ ep11_lily_hard_fuck = True
            mc "(And I have to keep that promise for her. She might break this off if I don't.)"
            jump ep11_lily_lewd_hard_label
        "Fuck her gently":
            $ ep11_lily_hard_fuck = False
            mc "(But I can't help it... I wanna see if she's open to something different. I feel like she might be.)"
            jump ep11_lily_lewd_soft_label
else:
    $ ep11_lily_hard_fuck = True
    mc "(Fuck... I'm not imagining it... She's feeling different about me for some reason.)"
    mc "(This is supposed to be about sex, not feelings. I guess it's my turn to keep my guard up and force her to play by the rules.)"
    jump ep11_lily_lewd_hard_label

label ep11_lily_lewd_soft_label:
scene ep11_lily_lewd28 with dissolve
mc "*{i}Smack{/i}*"
scene ep11_lily_lewd29 with dissolve
$ renpy.pause()
scene ep11_lily_lewd30 with dissolve
$ renpy.pause()
scene ep11_lily_lewd31 with dissolve
$ renpy.pause()
scene ep11_lily_lewd32 with dissolve
$ renpy.pause()
scene ep11_lily_lewd33 with dissolve
$ renpy.pause()
scene ep11_lily_lewd34 with dissolve
$ renpy.pause()
scene anim_lily_tits_ep11 with dissolve
mc "*{i}Suck suck lick lick{/i}*"
ly "*{i}Moans{/i}*"
pause
scene ep11_lily_lewd35 with dissolve
ly "Mmm..."
scene ep11_lily_lewd36 with dissolve
$ renpy.pause()

scene anim_lily_cunn_ep11 with dissolve
mc "*{i}Lick lick{/i}*"
ly "*{i}Moans{/i}* Yes, do it like that."
pause
scene anim_lily_cunn2_ep11 with dissolve
ly "Fuck, you're so good with your tongue."
pause

scene ep11_lily_lewd37 with dissolve
ly "*{i}Soft moan{/i}*"
scene ep11_lily_lewd38 with dissolve
$ renpy.pause()
scene anim_lily_miss1_ep11 with dissolve
ly "Harder, [name]..."
mc "No."
ly "*{i}Moans{/i}* Why?"
mc "Shh..."
pause
scene anim_lily_miss2_ep11 with dissolve
ly "*{i}Exhales{/i}* Fuck..."
pause
scene anim_lily_miss2b_ep11 with dissolve
pause

$ tmpInt = 0
label ep11_lily_lewd_soft_loop_label:
menu:
    "From behind":
        $ tmpInt += 1
        scene anim_lily_doggy1_ep11 with dissolve
        mc "*{i}Smack{/i}*"
        ly "Harder..."
        mc "No."
        ly "Please?"
        pause
        scene anim_lily_doggy2_ep11 with dissolve
        ly "Mmm..."
        pause
        jump ep11_lily_lewd_soft_loop_label
    "Her on top":
        $ tmpInt += 1
        scene anim_lily_ride1_ep11 with dissolve
        ly "Come on...fuck me harder."
        mc "Slow down..."
        ly "Resisting like that...makes it better..."
        mc "Good... Enjoy it."
        pause
        scene anim_lily_ride2_ep11 with dissolve
        mc "I want to see you cum."
        ly "I won't cum from slow sex, [name]."
        mc "Give it time and you will."
        pause
        jump ep11_lily_lewd_soft_loop_label
    "Kissing":
        $ tmpInt += 1
        scene anim_lily_side1_ep11 with dissolve
        ly "*{i}Smack{/i}*"
        pause
        scene anim_lily_side2_ep11 with dissolve
        mc "You taste so good."
        ly "Mhm... You too."
        pause
        jump ep11_lily_lewd_soft_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_lily_miss1_ep11 with dissolve
        ly "Stop looking me in the eyes like that."
        mc "You're not looking away."
        ly "[name]..."
        pause
        scene anim_lily_miss2_ep11 with dissolve
        ly "*{i}Moans{/i}*"
        pause
        scene anim_lily_miss2b_ep11 with dissolve
        pause
        jump ep11_lily_lewd_soft_loop_label
    "Cum" if tmpInt > 2:
        menu:
            "From behind":
                scene anim_lily_doggy1_ep11 with dissolve
                ly "[name]... I'm cumming..."
                mc "Me too... Let's cum together."
                ly "Ok... I'm so close..."
                scene ep11_lily_lewd42 at vpunch, cum1
                ly "Ahhh..."
                scene ep11_lily_lewd43 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd43 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd43 at vpunch, cum1
                mc "Hngnn..."
                scene ep11_lily_lewd44 with dissolve
                $ renpy.pause()
            "Her on top":
                scene anim_lily_ride1_ep11 with dissolve
                ly "[name]... I'm cumming..."
                mc "Me too... Let's cum together."
                ly "Ok... I'm so close..."
                scene ep11_lily_lewd45 at vpunch, cum1
                ly "Ahhh..."
                scene ep11_lily_lewd46 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd46 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd46 at vpunch, cum1
                mc "Hngnn..."
                scene ep11_lily_lewd47 with dissolve
                $ renpy.pause()
            "Kissing":
                scene anim_lily_side1_ep11 with dissolve
                ly "*{i}Smack{/i}* [name]... I'm cumming..."
                mc "Me too... Let's cum together."
                scene anim_lily_side2_ep11 with dissolve
                ly "Mmppfff... I'm so close..."
                scene ep11_lily_lewd40 with vpunch
                ly "Ahhh..."
                scene ep11_lily_lewd41 with vpunch
                ly "Mmm..."
                scene ep11_lily_lewd86 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd86 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd86 at vpunch, cum1
                mc "Hngnn..."
                scene ep11_lily_lewd39 with dissolve
                $ renpy.pause()
            "Missionary":
                scene anim_lily_miss1_ep11 with dissolve
                ly "[name]... I'm cumming..."
                mc "Me too... Let's cum together."
                ly "Ok... I'm so close..."
                scene ep11_lily_lewd48 with vpunch
                ly "Ahhh..."
                scene ep11_lily_lewd49 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd49 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_lily_lewd49 at vpunch, cum1
                mc "Hngnn..."
                scene ep11_lily_lewd50 with dissolve
                $ renpy.pause()

scene ep11_lily_lewd51 with dissolve
$ renpy.pause()
scene ep11_lily_lewd52 with dissolve
$ renpy.pause()
scene ep11_lily_lewd53 with dissolve
$ renpy.pause()
scene ep11_lily_lewd54 with dissolve
mc "That was so good..."
scene ep11_lily_lewd55 with dissolve
mc "Where are you going?"
scene ep11_lily_lewd56 with dissolve
mc "Lily?"
scene ep11_lily_lewd57 with dissolve
stop music fadeout 3
mc "Lily!?"
mc "(Fuck... I shouldn't have done that.)"
jump ep11_lily_lewd_end_label

label ep11_lily_lewd_hard_label:
play sound "sound_effects/shove.mp3"
scene ep11_lily_lewd58 with hpunch
$ renpy.pause()
scene ep11_lily_lewd59 with dissolve
ly "Yes... Break me, [name]."
play sound "sound_effects/slap.mp3"
scene ep11_lily_lewd61 with vpunch
$ renpy.pause()
scene ep11_lily_lewd62 with dissolve
$ renpy.pause()
scene ep11_lily_lewd63 with dissolve
$ renpy.pause()
scene anim_lily_tease_ep11 with dissolve
ly "*{i}Moans{/i}*"
mc "How much do you want it?"
ly "So fucking badly..."
mc "Your ass is so fucking sexy."
pause
$ tmpBool3 = False
scene ep11_lily_lewd60 with dissolve
menu:
    "Prepare her for anal":
        $ tmpBool3 = True
        scene ep11_lily_lewd66 with dissolve
        ly "*{i}Gasps{/i}* [name]..."
        mc "You know you want it."
        scene ep11_lily_lewd59 with dissolve
        ly "Mhm... I want it in my ass."
        scene anim_lily_cunn3_ep11 with dissolve
        ly "Eat my ass, [name]. Eat it..."
        pause
        scene ep11_lily_lewd65 with dissolve
        mc "I'm gonna fuck you so hard."
        scene ep11_lily_lewd67 with dissolve
        ly "*{i}Moans{/i}* Fuck! You're too big... Take it easy."
        mc "You can take it."
        scene anim_lily_doggy_anal1_ep11 with dissolve
        ly "Oh my God! Fuck!!! Ahhh..."
        mc "I knew you could take it."
        pause
        scene anim_lily_doggy_anal2_ep11 with dissolve
        ly "Hngn... Damn..."
        mc "You have such a hot ass..."
        pause
        scene anim_lily_doggy_anal3_ep11 with dissolve
        ly "Fuck me, [name]... Fuck me!"
        pause
    "Stick to vaginal":
        $ tmpBool3 = False
        scene ep11_lily_lewd64 with dissolve
        mc "I'm gonna fuck you so hard."
        scene ep11_lily_lewd67 with dissolve
        ly "*{i}Moans{/i}* Fuck! Oh, [name]... Give me your dick."
        scene anim_lily_doggy3_ep11 with dissolve
        mc "Take it."
        ly "Oh my God... Ahhh..."
        mc "Do you like it rough?"
        pause
        scene anim_lily_doggy4_ep11 with dissolve
        ly "It's so good... Yes! More! Harder!"
        pause
        scene anim_lily_doggy_anal3_ep11 with dissolve
        ly "Fuck me, [name]... Fuck me!"
        pause

$ tmpInt = 0
label ep11_lily_lewd_hard_loop_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_lily_miss3_ep11 with dissolve
        pause
        scene anim_lily_miss4_ep11 with dissolve
        pause
        scene anim_lily_miss5_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_lily_doggy3_ep11 with dissolve
        pause
        scene anim_lily_doggy4_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_lily_ride3_ep11 with dissolve
        pause
        scene anim_lily_ride4_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Piledriver (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_lily_pile1_ep11 with dissolve
        pause
        scene anim_lily_pile2_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_lily_rev1_ep11 with dissolve
        pause
        scene anim_lily_rev2_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Reverse cowgirl (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_lily_rev_anal1_ep11 with dissolve
        pause
        scene anim_lily_rev_anal2_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Missionary (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_lily_miss_anal1_ep11 with dissolve
        pause
        scene anim_lily_miss_anal2_ep11 with dissolve
        pause
        scene anim_lily_miss5_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Doggystyle (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_lily_doggy_anal1_ep11 with dissolve
        pause
        scene anim_lily_doggy_anal2_ep11 with dissolve
        pause
        jump ep11_lily_lewd_hard_loop_label
    "Cum" if tmpInt > 2:
        mc "Fuck, I'm gonna cum."
        menu:
            "Facial":
                scene anim_lily_cum1_ep11 with dissolve
                ly "Cum all over my face, [name]. Give this slut what she craves and deserves."
                scene ep11_lily_lewd72 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_lily_lewd72 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_lily_lewd72 at vpunch, cum2
                mc "Ahhh... Fuck!!!"
                scene ep11_lily_lewd73 with dissolve
                ly "Mmm..."
            "On ass":
                if tmpBool3:
                    scene anim_lily_doggy_anal2_ep11 with dissolve
                    ly "Cum over my ass, [name]. Give this slut what she craves and deserves."
                    scene ep11_lily_lewd70 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd70 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd70 at vpunch, cum2
                    mc "Ahhh... Fuck!!!"
                    scene ep11_lily_lewd71 with dissolve
                    $ renpy.pause()
                else:
                    scene anim_lily_doggy4_ep11 with dissolve
                    ly "Cum over my ass, [name]. Give this slut what she craves and deserves."
                    scene ep11_lily_lewd70 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd70 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd70 at vpunch, cum2
                    mc "Ahhh... Fuck!!!"
                    scene ep11_lily_lewd71 with dissolve
                    $ renpy.pause()
            "Creampie":
                if tmpBool3:
                    scene anim_lily_pile2_ep11 with dissolve
                    ly "Cum in my ass, [name]. Fill me with your cum! Give this slut what she craves and deserves."
                    scene ep11_lily_lewd84 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd84 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd84 at vpunch, cum1
                    mc "Ahhh... Fuck!!!"
                    scene ep11_lily_lewd68 with dissolve
                    ly "Mmm... I can feel it oozing out of me."
                else:
                    scene anim_lily_doggy_anal3_ep11 with dissolve
                    ly "Cum inside, [name]. Fill me with your cum! Give this slut what she craves and deserves."
                    scene ep11_lily_lewd85 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd85 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep11_lily_lewd85 at vpunch, cum1
                    mc "Ahhh... Fuck!!!"
                    scene ep11_lily_lewd69 with dissolve
                    ly "Mmm... I can feel it oozing out of me."

scene ep11_lily_lewd74 with dissolve
$ renpy.pause()
scene ep11_lily_lewd75 with dissolve
ly "*{i}Exhales{/i}* That was...intense."
scene ep11_lily_lewd76 with dissolve
mc "Yeah... Did you like it?"
scene ep11_lily_lewd75 with dissolve
ly "Yeah."
scene ep11_lily_lewd77 with dissolve
ly "For a second, I didn't think you were gonna fuck me like that."
scene ep11_lily_lewd78 with dissolve
if ep11_lily_want_more:
    mc "To be honest...for a second, I wasn't."
    scene ep11_lily_lewd79 with dissolve
    ly "..."
    scene ep11_lily_lewd78 with dissolve
    mc "What are you thinking?"
    scene ep11_lily_lewd77 with dissolve
    ly "It's the alcohol. I'm drunk and emotional for some weird reason."
    scene ep11_lily_lewd78 with dissolve
    mc "Wanna talk about it?"
    scene ep11_lily_lewd77 with dissolve
    ly "Definitely not."
    ly "I...uh..."
else:
    mc "Did you want me to go softer on you or what?"
    scene ep11_lily_lewd77 with dissolve
    ly "I'm not saying that..."
    scene ep11_lily_lewd78 with dissolve
    mc "Lily... To be clear... You wanted a shallow deal."
    scene ep11_lily_lewd79 with dissolve
    ly "..."
scene ep11_lily_lewd80 with dissolve
ly "It's been fun, [name]."
ly "But I'm gonna head back home now."
if ep11_lily_want_more:
    scene ep11_lily_lewd78 with dissolve
    mc "Are you sure? You can stay here tonight if you want."
    scene ep11_lily_lewd77 with dissolve
    ly "And that's why I have to leave."
else:
    scene ep11_lily_lewd78 with dissolve
    mc "I think it's for the best."
scene ep11_lily_lewd81 with dissolve
ly "So... See you."
scene ep11_lily_lewd82 with dissolve
mc "See you."
stop music fadeout 3
scene ep11_lily_lewd83 with dissolve
$ renpy.pause()
jump ep11_lily_lewd_end_label

label ep11_lily_lewd_end_label:
$ renpy.end_replay()
$ persistent.ep11_lewd_lily = True
$ calcScenes()
$ currentFreeRoamLabel= "ep11_diks4_fr2_lib_mid_label"
$ mphone_next_song()
$ task_list[12] = ""
$ updateTaskList()
$ new_bio("Lily", "I had sex with Lily at the DIKs' Christmas Panty party, but it felt different than before. She blamed it on the alcohol, but I wasn't sure that was the reason.")
$ mphone_stats_add_girl_s3("lily","You had sex with Lily at the Christmas Panty party in episode 11.")
$ event_list.append("part2_lily")
show screen new_phone_screen
jump endEvent

label ep11_tiffani_event_label:
$ guideSuggestedPage = 211
if ep11_invited_tara:
    scene ep11_tiffani_event1 with dissolve
else:
    scene ep11_tiffani_event1b with dissolve
ti "[name]?"
scene ep11_tiffani_event2 with dissolve
mc "Yeah, what's up?"
scene ep11_tiffani_event4 with dissolve
ti "You're not being for real with this Dirty Bowl thing, are you? Like, come on? It's a funny joke, yeah?"
scene ep11_tiffani_event3 with dissolve
mc "The guys wanted it. I don't know what they put in there."
scene ep11_tiffani_event4 with dissolve
ti "Can you help me out? I need to change mine."
scene ep11_tiffani_event3 with dissolve
mc "Why? Was your mission that bad?"
scene ep11_tiffani_event5 with dissolve
ti "See for yourself."
scene ep11_tiffani_event6 with dissolve
mc "Oh, wow. Haha! It's not the first one of those I've seen tonight. They must have run out of ideas or thought they'd get a blowjob from someone."
ti "Lucky me..."
scene ep11_tiffani_event7 with dissolve
mc "You don't have to do it. It's a silly game to add some spice to the party."
scene ep11_tiffani_event8 with dissolve
ti "They said everyone had to do their mission, or they'd have to leave before the party was over."
scene ep11_tiffani_event7 with dissolve
mc "Lie and say that you did yours."
scene ep11_tiffani_event8 with dissolve
ti "What if they want to check?"
scene ep11_tiffani_event7 with dissolve
mc "Haha! How would they check that?"
scene ep11_tiffani_event8 with dissolve
ti "It feels stupid to risk it. I've seen others do their missions. I don't want to leave early."
scene ep11_tiffani_event9 with dissolve
mc "If that's the case, go ahead and do it."
scene ep11_tiffani_event10 with dissolve
ti "Aha... So, you want a blowjob?"
scene ep11_tiffani_event9 with dissolve
mc "Uh... Now you're reading into things."
scene ep11_tiffani_event10 with dissolve
ti "Don't play coy with me. Come, let's get it done with."
scene ep11_tiffani_event9 with dissolve
if branchAlone:
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Tiffani scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    menu:
        "Help her \n{size=-4}[m_c1][mod_choices[0]]":
            if ep11_tara_lewd:
                mc "I helped Tara recently... I'm not recharged."
                scene ep11_tiffani_event11 with dissolve
                ti "Are you saying no to me?"
                scene ep11_tiffani_event12 with dissolve
                mc "I'm saying I can't...at least not for a while."
                scene ep11_tiffani_event10 with dissolve
                ti "Let's give it a shot. I'm sure you'll get it working."
            else:
                mc "Well, alright..."
            jump ep11_tiffani_lewd_label
        "Don't help her":
            mc "Whoa, whoa, whoa. Tiffani, no."
            scene ep11_tiffani_event13 with dissolve
            mc "It was the truth. I wasn't trying to get you to do this with me."
            scene ep11_tiffani_event14 with dissolve
            ti "Oh!"
            scene ep11_tiffani_event13 with dissolve
            ti "..."
            scene ep11_tiffani_event11 with dissolve
            ti "Meh, who cares. Still wanna?"
            scene ep11_tiffani_event12 with dissolve
            mc "No, but thanks."
            scene ep11_tiffani_event11 with dissolve
            ti "*{i}Scoffs{/i}* Thanks?"
            ti "Yeah, thanks for nothing."
else:
    mc "Whoa, whoa, whoa. Tiffani, no."
    scene ep11_tiffani_event13 with dissolve
    mc "It was the truth. I wasn't trying to get you to do this with me."
    scene ep11_tiffani_event14 with dissolve
    ti "Oh!"
    scene ep11_tiffani_event13 with dissolve
    ti "..."
    scene ep11_tiffani_event11 with dissolve
    ti "Meh, who cares. Still wanna?"
    scene ep11_tiffani_event9 with dissolve
    
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Elena scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
    menu:
        "No, I'm taken":
            mc "No, I'm taken."
            scene ep11_tiffani_event10 with dissolve
            ti "That's fine. I can keep a secret if you can."
            scene ep11_tiffani_event9 with dissolve
            mc "I'm not that kind of guy."
            scene ep11_tiffani_event11 with dissolve
            ti "Yeah, right? That's what everyone says until they are."
            scene ep11_tiffani_event12 with dissolve
            mc "Well, I'm not..."
            scene ep11_tiffani_event11 with dissolve
            ti "Ok..."
        "I shouldn't... \n{size=-4}[m_c1][mod_choices[6]]":
            $ tc += 1
            mc "I shouldn't... I'm taken. But if I wasn't, I'd do it in a heartbeat. You're super hot."
            scene ep11_tiffani_event10 with dissolve
            ti "I can keep a secret if you can."
            scene ep11_tiffani_event9 with dissolve
            mc "Don't tempt me..."
            scene ep11_tiffani_event10 with dissolve
            ti "Come on... You know you want to."
            scene ep11_tiffani_event12 with dissolve
            mc "God damn... You're tempting, but I have to say no."
            scene ep11_tiffani_event11 with dissolve
            ti "Thanks for nothing, then."

scene ep11_tiffani_event15 with dissolve
mc "Hey..."
scene ep11_tiffani_event16 with dissolve
ti "What?"
scene ep11_tiffani_event15 with dissolve
mc "There's a pen and paper in the kitchen. Write yourself a new mission and pass it off as yours."
scene ep11_tiffani_event17 with dissolve
$ renpy.pause()
$ new_bio("Tiffani", "Tiffani asked me to help her with her Dirty Bowl mission, but I declined.")
$ task_list[4] = ""
if ep10_quinn_help and "ep11_tara_event_label" not in event_list:
    if persistent.mod_wtenabled:
        $ task_list[8] = "Talk to Quinn (Theater)"
    else:
        $ task_list[8] = "Talk to Quinn"
    $ event_list.append("ep11_pp_quinn2_event_label")
$ updateTaskList()
jump endEvent

label ep11_tiffani_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep11_tara_lewd = False
    $ mphone_music_genre = 2
    play music "music/ep11/licensed_music/track180.mp3"
    queue music ["music/ep11/licensed_music/track177.mp3","music/ep11/licensed_music/track178.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track182.mp3"]
$ ep11_tiffani_lewd = True
hide screen new_phone_screen
scene ep11_tiffani_lewd1 with wipeleft
ti "Did you lock the door?"
scene ep11_tiffani_lewd2 with dissolve
mc "Yeah."
scene ep11_tiffani_lewd3 with dissolve
ti "Pull those pants off."
scene ep11_tiffani_lewd4 with dissolve
mc "What about you? I'd feel weird to be the only one undressed."
scene ep11_tiffani_lewd5 with dissolve
ti "How about this?"
scene ep11_tiffani_lewd6 with dissolve
mc "That's much better."
scene ep11_tiffani_lewd7 with dissolve
mc "Give me your best."
scene ep11_tiffani_lewd8 with dissolve
ti "Don't worry, I will. It's not my first time."

scene ep11_tiffani_lewd9 with dissolve
ti "(Only with one of this size... It's bigger than in the picture.)"
mc "Fuck... That's nice and warm."

scene anim_tiff_bj1_ep11 with dissolve
ti "*{i}Suck suck{/i}*"
mc "That feels so good."
pause
scene anim_tiff_bj2_ep11 with dissolve
mc "Damn... You know how to do that, for sure. I love the way you suck it."
pause
scene ep11_tiffani_lewd10 with dissolve
if ep11_tara_lewd:
    ti "See! I knew you'd get it up with me."
ti "Do you want to see me deepthroat it?"
scene ep11_tiffani_lewd11 with dissolve
mc "Do you think you can do it?"
scene ep11_tiffani_lewd10 with dissolve
ti "No clue, but I wanna try. It's not every day a girl gets to try a cock of this size."
scene ep11_tiffani_lewd12 with dissolve
ti "*{i}Glug glug{/i}*"
scene ep11_tiffani_lewd13 with dissolve
mc "Yes... Fuck... That's all of it."
scene ep11_tiffani_lewd14 with dissolve
ti "*{i}Cough{/i}*"
ti "Wow! I fucking did it."
scene anim_tiff_bj3_ep11 with dissolve
ti "*{i}Suck glug{/i}*"
mc "Shit, I'm so deep in your throat... That suction is amazing..."
scene anim_tiff_bj4_ep11 with dissolve
ti "*{i}Suck suck{/i}*"
mc "Damn, Tiffani... You're gonna have me cumming in no time if you keep that up."
scene ep11_tiffani_lewd15 with dissolve
ti "Does that count as a blowjob?"
scene ep11_tiffani_lewd16 with dissolve
mc "You're not done, are you?"
scene ep11_tiffani_lewd15 with dissolve
ti "No, but it counts, right?"
scene ep11_tiffani_lewd16 with dissolve
mc "It depends... If I say yes, will you stop?"
scene ep11_tiffani_lewd17 with dissolve
ti "If you say yes, I have something else in mind."
scene ep11_tiffani_lewd18 with dissolve
$ renpy.pause()
scene ep11_tiffani_lewd19 with dissolve
ti "I take it that's a yes."
scene anim_tiff_cunn1_ep11 with dissolve
mc "*{i}Lick lick{/i}*"
ti "*{i}Moans{/i}* Yes... Eat me, [name]."
pause
scene anim_tiff_cunn2_ep11 with dissolve
pause
scene ep11_tiffani_lewd20 with dissolve
ti "Maybe I'll swap my mission for the fuck a guy task while we're at it."
scene ep11_tiffani_lewd21 with dissolve
mc "I'll help you out with that one, too."
scene anim_tiff_stand1_ep11 with dissolve
ti "Fuck me, [name]! Harder! *{i}Moans{/i}*"
ti "*{i}Suck suck{/i}* Yes! Give me that giant cock. Hngnn..."
ti "*{i}Moans{/i}* God, you're stretching me with that thing."
pause
label ep11_tiffani_lewd_loop_label:
menu:
    "Doggystyle":
        scene anim_tiff_doggy1_ep11 with dissolve
        ti "*{i}Moans{/i}* Oh, [name]... Fuck me!"
        pause
        scene anim_tiff_doggy2_ep11 with dissolve
        mc "Watching your sexy ass slapping against me as I fuck you is so fucking hot."
        pause
        jump ep11_tiffani_lewd_loop_label
    "Cowgirl":
        scene anim_tiff_ride1_ep11 with dissolve
        mc "Ride my cock, Tiffani."
        ti "Yeah, do you want me to ride you hard, [name]?"
        mc "Yes. I love it when you ride me like that."
        pause
        scene anim_tiff_ride2_ep11 with dissolve
        ti "You're the biggest one I've had, [name]."
        ti "*{i}Moans{/i}* It's so fucking good! It doesn't even matter that it's on the toilet."
        pause
        jump ep11_tiffani_lewd_loop_label
    "Facing":
        scene anim_tiff_stand1_ep11 with dissolve
        ti "*{i}Suck suck{/i}* Mhm... Mhm... Give it to me, [name]. Shove that cock in me."
        mc "Yeah, you want it?"
        ti "Mhm... I want your fat cock, [name]."
        ti "*{i}Moans{/i}* Fuck, you're gonna make me...cum..."
        pause
        scene ep11_tiffani_lewd22 with vpunch
        $ renpy.pause(0.5)
        scene ep11_tiffani_lewd22 with vpunch
        $ renpy.pause(0.5)
        scene ep11_tiffani_lewd22 with vpunch
        ti "Ahhh!!! Hngnnn..."
        scene ep11_tiffani_lewd23 with dissolve
        ti "Oh, my fucking God..."
        jump ep11_tiffani_lewd_loop_label
    "Cum":
        scene anim_tiff_cum_ep11 with dissolve
        mc "Fuck, I'm gonna cum..."
        ti "Cum on my face, [name]. I want to be covered in it."
        scene ep11_tiffani_lewd24 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep11_tiffani_lewd24 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep11_tiffani_lewd24 at vpunch, cum2
        mc "Ahhh!!!"
        scene ep11_tiffani_lewd25 with dissolve
        ti "Mmm... Mission completed, haha."
        scene ep11_tiffani_lewd26 with dissolve
        mc "Sure was. Wow..."
        scene ep11_tiffani_lewd27 with dissolve
        $ renpy.pause()

scene ep11_tiffani_lewd28 with dissolve
gi "*{i}Whistles{/i}* There you are..."
scene ep11_tiffani_lewd29 with dissolve
ti "It's not what you think."
scene ep11_tiffani_lewd30 with dissolve
gi "It can hardly be kinkier than what I'm thinking."
scene ep11_tiffani_lewd29 with dissolve
ti "Oh, shut up."
scene ep11_tiffani_lewd31 with dissolve
gi "Tell me about it."
ti "Not here."
$ renpy.end_replay()
$ persistent.ep11_lewd_tiffani = True
$ calcScenes()
$ new_bio("Tiffani", "Tiffani asked me to help her with her Dirty Bowl mission. We ended up having sex in the bathroom.")
$ mphone_stats_add_girl_s3("tiffani","You had sex with Tiffani at the Christmas Panty party in episode 11.")
show screen new_phone_screen
$ task_list[4] = ""
if ep10_quinn_help and "ep11_tara_event_label" not in event_list:
    if persistent.mod_wtenabled:
        $ task_list[8] = "Talk to Quinn (Theater)"
    else:
        $ task_list[8] = "Talk to Quinn"
    $ event_list.append("ep11_pp_quinn2_event_label")
$ updateTaskList()
jump endEvent

label ep11_tara_event_label:
$ guideSuggestedPage = 211
scene ep11_tara_event1 with dissolve
mc "Are you still sitting here?"
scene ep11_tara_event2 with dissolve
ta "Haha, yeah. We're having a good time. And we've been dancing some too."
scene ep11_tara_event3 with dissolve
mc "That's great."
scene ep11_tara_event4 with dissolve
ta "Can we have a private talk?"
scene ep11_tara_event3 with dissolve
mc "Sure."
scene ep11_tara_event5 with dissolve
ta "I spoke to Derek, Leon, Jamie and Rusty, so far."
ta "I wanted to let you know that I apologized to them for my part in this."
scene ep11_tara_event6 with dissolve
mc "You did? That's big of you."
scene ep11_tara_event7 with dissolve
ta "But I realized I never apologized to you. And, honestly, you are the one who should have heard it first."
ta "I'm sorry, [name]."
scene ep11_tara_event6 with dissolve
if ep11_tara_attitude > 0:
    mc "Maybe I was harsh on you at first... And for that, I'm sorry."
mc "It's all good. I forgive you."
scene ep11_tara_event8 with dissolve
$ renpy.pause()
scene ep11_tara_event9 with dissolve
$ renpy.pause()
scene ep11_tara_event10 with dissolve
ta "Oh, another thing I wanted to ask you..."
ta "About this mission I got...do I have to do it?"
scene ep11_tara_event11 with dissolve
mc "It depends on who you ask. If you ask Derek, he'd say yes. But I say no, it's just for fun."
scene ep11_tara_event12 with dissolve
ta "Then what's the point of the bowl if you tell guests not to do their tasks?"
scene ep11_tara_event11 with dissolve
mc "The bowl is there to spice up the party and to make guests talk and interact."
scene ep11_tara_event12 with dissolve
ta "So, I don't have to spell HORSE with someone?"
scene ep11_tara_event11 with dissolve
mc "Spell horse? What's that?"
scene ep11_tara_event12 with dissolve
ta "It's an acronym for...things."
scene ep11_tara_event11 with dissolve
mc "I'm gonna guess that the H isn't short for handholding or hugging."
scene ep11_tara_event10 with dissolve
ta "Haha, I wish it was."
scene ep11_tara_event19 with dissolve
ta "*{i}Whispers{/i}* It's handjob, oral, rimjob, sex, and ejaculation."
scene ep11_tara_event11 with dissolve
mc "Haha! What a stretch to make it spell HORSE."
scene ep11_tara_event10 with dissolve
ta "I must have pulled the worst one."
scene ep11_tara_event11 with dissolve
mc "It's up there. If I were you, I'd either swap missions or lie that you did it."
scene ep11_tara_event13 with dissolve
$ renpy.pause()
scene ep11_tara_event14 with dissolve
ta "Why? Don't you want to spell it with me?"
scene ep11_tara_event13 with dissolve
mc "Me? You're joking, right?"
scene ep11_tara_event14 with dissolve
ta "I mean... If I were to do it with someone at this party, I'd choose you."
if ep11_tiffani_lewd:
    ta "And I heard you helped Tiffani with hers, so why not me, too?"
scene ep11_tara_event13 with dissolve
$ renpy.pause()
scene ep11_tara_event20 with dissolve
$ renpy.pause()
scene ep11_tara_event13 with dissolve
if not branchAlone:
    menu:
        "I'm not available":
            mc "Sorry, I can't help you. I'm not available."
            scene ep11_tara_event15 with dissolve
            ta "Rats... I'll look into getting another mission, then."
            scene ep11_tara_event16 with dissolve
            mc "Yeah, either do that or make another guy happy. It's your call."
            $ new_bio("Tara", "Tara asked me to help her with her Dirty Bowl mission, but I declined.")
        "Don't you have a boyfriend?":
            jump ep11_tara_eventb_label
else:
    label ep11_tara_eventb_label:
    mc "Don't you have a boyfriend?"
    scene ep11_tara_event14 with dissolve
    ta "We've been on and off lately. Most recently off."
    if ep9_tara_kiss:
        ta "And besides, that didn't stop you from kissing me before."
    scene ep11_tara_event13 with dissolve
    if not branchAlone:
        if tc < 5:
            mc "Well, I'm not available, so... Thanks anyway."
        else:
            mc "You're killing me, Tara... Sorry, but I must stop you before I do something stupid."
        jump ep11_tara_eventc_label
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Tara scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    menu:
        "Help her \n{size=-4}[m_c1][mod_choices[0]]":
            mc "If you want to do it, I would be a fool to say no."
            scene ep11_tara_event17 with dissolve
            ta "A fool, huh?"
            scene ep11_tara_event18 with dissolve
            mc "Horse, cat, dog, elephant... We can spell anything you want together."
            scene ep11_tara_event17 with dissolve
            ta "Haha! I think we should start with horse."
            scene ep11_tara_event18 with dissolve
            mc "I know a place where we can get some privacy."
            jump ep11_tara_lewd_label
        "Decline":
            mc "Thanks for the offer, but I'm gonna pass on it."
            label ep11_tara_eventc_label:
            scene ep11_tara_event15 with dissolve
            ta "Rats... I'll look into getting another mission, then."
            scene ep11_tara_event16 with dissolve
            mc "Yeah, either do that or make another guy happy. It's your call."
            $ new_bio("Tara", "Tara asked me to help her with her Dirty Bowl mission, but I declined.")
$ task_list[2] = ""
if ep10_quinn_help and "ep11_tiffani_event_label" not in event_list:
    if persistent.mod_wtenabled:
        $ task_list[8] = "Talk to Quinn (Theater)"
    else:
        $ task_list[8] = "Talk to Quinn"
    $ event_list.append("ep11_pp_quinn2_event_label")
$ updateTaskList()
jump endEvent

label ep11_tara_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep8_sarah_lewd = True
    play music "music/ep11/licensed_music/track177.mp3"
    queue music ["music/ep11/licensed_music/track178.mp3","music/ep11/licensed_music/track180.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track182.mp3"]
$ ep11_tara_lewd = True
hide screen new_phone_screen
scene ep11_tara_lewd1 with dissolve
mc "No one will come in here tonight."
scene ep11_tara_lewd2 with dissolve
ta "Is that so?"
scene ep11_tara_lewd3 with dissolve
mc "Yeah."
scene ep11_tara_lewd4 with dissolve
$ renpy.pause()
scene ep11_tara_lewd5 with dissolve
$ renpy.pause()
scene ep11_tara_lewd5b with dissolve
$ renpy.pause()
scene ep11_tara_lewd6 with dissolve
ta "So... HORSE, was it?"
scene ep11_tara_lewd7 with dissolve
ta "I should have put the panties outside of the garter...but I didn't think I'd remove them at the party."
mc "Take your time. I'm enjoying the view."
scene ep11_tara_lewd8 with dissolve
$ renpy.pause()
scene ep11_tara_lewd9 with dissolve
mc "*{i}Smack{/i}*"
scene ep11_tara_lewd10 with dissolve
ta "Mmmpff..."
scene anim_tara_finger_ep11 with dissolve
ta "Mmm!!! Oh, fuck! *{i}Moans{/i}*"
ta "This isn't HORSE."
mc "I suck at spelling."
pause
scene ep11_tara_lewd11 with dissolve
ta "*{i}Smack{/i}* Your cock... Give it to me."
scene ep11_tara_lewd12 with dissolve
mc "Yeah, do you want it?"
ta "Mhm..."
scene ep11_tara_lewd13 with dissolve
mc "You know what you gotta do with it."

scene anim_tara_hj_ep11 with dissolve
ta "You learned how to spell all of a sudden?"
mc "You're the one who needs to know how to spell. I'm just along for the ride."
ta "Haha, I'm sure you are."
pause
scene ep11_tara_lewd14 with dissolve
ta "O...?"
mc "Go for it."
scene anim_tara_bj_ep11 with dissolve
ta "*{i}Suck suck{/i}*"
pause
scene anim_tara_bj2_ep11 with dissolve
pause
scene ep11_tara_lewd15 with dissolve
mc "Your boobs look so fucking sexy... Can I feel them?"
ta "You already did."
scene ep11_tara_lewd16 with dissolve
mc "I mean, around my cock."
scene ep11_tara_lewd17 with dissolve
ta "Oh! Ok."
scene anim_tara_boobjob_ep11 with dissolve
ta "How does this feel?"
mc "Push them harder together... Yeah... There you go."
pause
scene anim_tara_boobjob2_ep11 with dissolve
ta "Why do guys like this?"
mc "I think it's in our DNA."
pause

scene ep11_tara_lewd18 with dissolve
mc "Get up here..."
scene ep11_tara_lewd19 with dissolve
ta "Are you gonna do what I think you are?"
scene anim_tara_rimjob_ep11 with dissolve
ta "*{i}Moans{/i}* Yeah... I was right."
mc "*{i}Lick lick{/i}*"
pause

scene ep11_tara_lewd20 with dissolve
menu:
    "Vaginal":
        scene ep11_tara_lewd21 with dissolve
        ta "Mmm... Yes. Give me that cock."
        scene anim_tara_doggy1_ep11 with dissolve
        pause
        scene anim_tara_doggy2_ep11 with dissolve
        pause
    "Anal":
        scene ep11_tara_lewd22 with vpunch
        ta "*{i}Gasps{/i}* There's no A in HORSE."
        scene ep11_tara_lewd23 with dissolve
        ta "Hngn... Fuck..."
        scene anim_tara_doggy1_anal_ep11 with dissolve
        pause
        scene anim_tara_doggy2_anal_ep11 with dissolve
        pause

$ tmpInt = 0

label ep11_tara_lewd_loop_label:
menu:
    "Handjob":
        scene anim_tara_hj_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Blowjob":
        scene anim_tara_bj_ep11 with dissolve
        pause
        scene anim_tara_bj2_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Boobjob":
        scene anim_tara_boobjob_ep11 with dissolve
        pause
        scene anim_tara_boobjob2_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Rimjob":
        scene anim_tara_rimjob_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_tara_doggy1_ep11 with dissolve
        pause
        scene anim_tara_doggy2_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_tara_doggy1_anal_ep11 with dissolve
        pause
        scene anim_tara_doggy2_anal_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_tara_ride1_ep11 with dissolve
        pause
        scene anim_tara_ride2_ep11 with dissolve
        pause
        scene anim_tara_ride3_ep11 with dissolve
        pause
        jump ep11_tara_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_tara_stand1_ep11 with dissolve
        pause
        scene anim_tara_stand2_ep11 with dissolve
        pause
        ta "I'm cumming... [name]... Keep it up."
        menu:
            "Make her cum":
                mc "Alright. Cum, Tara."
                scene ep11_tara_lewd24 with vpunch
                $ renpy.pause(0.5)
                scene ep11_tara_lewd24 with vpunch
                ta "Ahhh!! Fuck!!!"
                scene ep11_tara_lewd25 with vpunch
                ta "*{i}Moans{/i}* Oh, God!!!"
            "Deny her":
                mc "No, you're not."
                ta "Hey..."
                mc "You cum when I say you can."
        jump ep11_tara_lewd_loop_label
    "Cum" if tmpInt > 1:
        menu:
            "Creampie":
                scene anim_tara_stand1_ep11 with dissolve
                pause
                scene ep11_tara_lewd26 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd26 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd26 at vpunch, cum1
                mc "Ahh!!!"
                scene ep11_tara_lewd27 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_tara_doggy1_anal_ep11 with dissolve
                pause
                scene ep11_tara_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd28 at vpunch, cum1
                mc "Ahh!!!"
                scene ep11_tara_lewd29 with dissolve
                $ renpy.pause()
            "On ass":
                scene anim_tara_doggy2_ep11 with dissolve
                pause
                scene ep11_tara_lewd30 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_tara_lewd30 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_tara_lewd30 at vpunch, cum2
                mc "Ahh!!!"
                scene ep11_tara_lewd31 with dissolve
                $ renpy.pause()
            "In mouth":
                scene anim_tara_bj_ep11 with dissolve
                pause
                scene ep11_tara_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_tara_lewd32 at vpunch, cum1
                mc "Ahh!!!"
                scene ep11_tara_lewd33 with dissolve
                $ renpy.pause()
                scene ep11_tara_lewd34 with dissolve
                $ renpy.pause()

scene ep11_tara_lewd35 with dissolve
$ renpy.pause()
scene ep11_tara_lewd36 with dissolve
ta "That wasn't HORSE. I can't even spell what that was."
ta "Maybe HOBRSE, or something."
scene ep11_tara_lewd37 with dissolve
mc "Eh, it was close enough. They'll give you a pass."
scene ep11_tara_lewd38 with dissolve
ta "You know, between you and me, I always found you incredibly sexy."
scene ep11_tara_lewd39 with dissolve
mc "You have?"
scene ep11_tara_lewd40 with dissolve
ta "I'm hardly alone. I've heard others say it, too."
scene ep11_tara_lewd39 with dissolve
mc "You're inflating my ego too much now."
if ep8_sarah_lewd:
    scene ep11_tara_lewd40 with dissolve
    ta "Haha, ok. I'll deflate it for you then."
    ta "Because while everyone knows your cock is big, you're not the biggest one I've had."
    scene ep11_tara_lewd39 with dissolve
    mc "Thanks, that lie makes it feel better."
    scene ep11_tara_lewd40 with dissolve
    ta "It's not a lie. And you're welcome."
else:
    scene ep11_tara_lewd38 with dissolve
    ta "Haha, sorry. But it's true."
scene ep11_tara_lewd41 with dissolve
ta "..."
scene ep11_tara_lewd38 with dissolve
ta "Let's head back."
scene ep11_tara_lewd42 with dissolve
ta "*{i}Smack{/i}*"

$ renpy.end_replay()
$ persistent.ep11_lewd_tara = True
$ calcScenes()
$ task_list[2] = ""
if ep10_quinn_help and "ep11_tiffani_event_label" not in event_list:
    if persistent.mod_wtenabled:
        $ task_list[8] = "Talk to Quinn (Theater)"
    else:
        $ task_list[8] = "Talk to Quinn"
    $ event_list.append("ep11_pp_quinn2_event_label")
$ updateTaskList()
$ currentFreeRoamLabel = "ep11_diks_pp_nick_label"
$ new_bio("Tara", "Tara asked me to help her with her Dirty Bowl mission. I ended up having sex with her in Nick's room.")
$ mphone_stats_add_girl_s3("tara","You had sex with Tara at the Christmas Panty party in episode 11.")
show screen new_phone_screen
jump endEvent

label ep11_pp_ctease_event_label:
$ guideSuggestedPage = 214
scene ep11_pp_ctease_event1 with dissolve
mc "Ladies... How's it going tonight? Is everyone treating you nicely?"
scene ep11_pp_ctease_event2 with dissolve
ml "Too nice! I'm not getting much of anything. It's like some of the guys never saw a girl in underwear before and don't know how to talk to you."
scene ep11_pp_ctease_event1 with dissolve
mc "Oh? That sucks. I'll make sure guys drink more, then."
scene ep11_pp_ctease_event2 with dissolve
ml "As that will improve it..."
scene ep11_pp_ctease_event1 with dissolve
mc "Hey, why the mood? Did something happen?"
scene ep11_pp_ctease_event3 with dissolve
cam "Melanie is going through a dry spell."
scene ep11_pp_ctease_event4 with dissolve
ml "You're the one to talk."
scene ep11_pp_ctease_event3 with dissolve
cam "[name] already knows about mine."
scene ep11_pp_ctease_event5 with dissolve
ml "Whatever... I need more beer."
scene ep11_pp_ctease_event6 with dissolve
mc "Is that still going on for you?"
scene ep11_pp_ctease_event7 with dissolve
cam "It's going to be a long winter."
scene ep11_pp_ctease_event6 with dissolve
mc "Haha, it's weird that you're making me feel bad somehow."
scene ep11_pp_ctease_event8 with dissolve
cam "Haha! It's not your fault."
scene ep11_pp_ctease_event6 with dissolve
mc "Exactly, that's why I feel weird about it."
scene ep11_pp_ctease_event8 with dissolve
cam "Don't feel bad, [name]. If you were my boyfriend, I bet you'd take good care of me."
scene ep11_pp_ctease_event9 with dissolve
mc "Oh, I would."
scene ep11_pp_ctease_event8 with dissolve
cam "Hit me up when you're single or if you and Sage want a third."
if ep10_dots_attitude >= 1 and not ep9_sage_vanilla:
    scene ep11_pp_ctease_event9 with dissolve
    
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Sage/Camila threesome)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
    menu:
        "Let's ask Sage \n{size=-4}[m_c1][mod_choices[0]]":
            $ ep11_camila_opportunity = True
            mc "I'll ask her if you want."
            scene ep11_pp_ctease_event10 with dissolve
            cam "I was fooling around. But what do you think she'd say?"
            scene ep11_pp_ctease_event11 with dissolve
            if ep8_sq_lewd:
                mc "I know for a fact that she's into threesomes."
                scene ep11_pp_ctease_event10 with dissolve
                cam "Look at you, you stud..."
            else:
                mc "She told me she's into threesomes."
                scene ep11_pp_ctease_event10 with dissolve
                cam "You don't say..."
            scene ep11_pp_ctease_event9 with dissolve
            mc "Let's ask her. Lemme get my phone..."
            hide screen new_phone_screen
            scene ep11_pp_ctease_event15 with dissolve
            $ tmpInt = 0
            $ tmpInt2 = 0
            $ text_message_screen_list = []
            $ text_message_screen_list.append(["%s" % name,"A totally random question... Do you think Camila is hot?",False])
            $ text_message_screen_list.append(["Sage","That doesn't sound like a random question to me, but yeah, she's a pretty girl. Why?",True])
            $ text_message_screen_list.append(["%s" % name,"Another totally random question... Would you do her? You know, in a threesome?",False])
            $ text_message_screen_list.append(["Sage","Are these random questions, or is Camila there with you right now?",True])
            show screen text_message_screen
            play sound "sound_effects/interlude/zoey_message.mp3"
            $ renpy.pause()
            scene ep11_pp_ctease_event16 with dissolve
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            scene ep11_pp_ctease_event14 with dissolve
            $ tmpInt += 1
            $ tmpInt2 = len(text_message_screen_list)
            $ text_message_screen_list.append(["%s" % name,"Camila says hi.",False])
            $ text_message_screen_list.append(["Sage","LOL. Tell her I'd definitely do her. mphone_emoji_kiss mphone_emoji_laugh",True])
            show screen text_message_screen
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            $ mphone_scene_to_chat("Sage",text_message_screen_list)
            scene ep11_pp_ctease_event12 with dissolve
            mc "See! I told you she would."
            scene ep11_pp_ctease_event13 with dissolve
            cam "Haha! Too bad she's not here..."
            $ new_bio("Camila", "Camila and I teased Sage about having a threesome.")
            $ new_bio("Sage", "Camila and I teased Sage about having a threesome.")
        "Will do":
            mc "Haha, will do!"
else:
    scene ep11_pp_ctease_event9 with dissolve
    mc "Tsk."
$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_act2_event_label:
if ep11_pp_game > 0:
    jump ep11_pp_act2_eventb_label
$ guideSuggestedPage = 207
scene ep11_pp_act2_event1
show screen dance_filter_screen
with dissolve
de "That's right, come on in. Come one, come all!"
scene ep11_pp_act2_event2 with dissolve
tm "What a bro..."
scene ep11_pp_act2_event3 with dissolve
de "They aren't for you; they're for the contest. You go out here with the rest of the guys."
scene ep11_pp_act2_event5 with dissolve
mc "Are you ready?"
scene ep11_pp_act2_event4 with dissolve
de "I feel like a dog herding sheep, but there are many girls behind that curtain."
scene ep11_pp_act2_event5 with dissolve
mc "Ok. If you prepare your end of the contest, I'll take care of mine."
scene ep11_pp_act2_event6 with dissolve
mc "Guys, guys. Gather around! Everyone get on the dance floor behind the rope."
mc "It's time for another contest that we've chosen to call \"Guess Who\", and you're all invited to play."
scene ep11_pp_act2_event8 with dissolve
mc "If you wonder where the girls went, they're all behind that curtain. Well, not everyone, but many of them."
mc "I hope you've been paying attention to the girls here tonight. One at a time, you will see a body part, and your task is to guess who it belongs to."
mc "How many contestants will we have, Derek?"
scene ep11_pp_act2_event9 with dissolve
de "So far, we're up to eight, but I'm working on getting it to ten."
scene ep11_pp_act2_event7 with dissolve
mc "The winner gets the honor, but everyone will get to see boobs, butts, and maybe more."
scene ep11_pp_act2_event8 with dissolve
mc "It all depends on how daring the girls are."
mc "Grab a pen and paper from the bar and let's get this show on the road."
scene ep11_pp_act2_event10 with dissolve
de "We're good to go. We've got ten of them, the order has been decided, and I have the correct answers."
de "Join them for the fun; I've got this."
scene ep11_pp_act2_event11 with dissolve
de "Here we go! Let the game begin!"
de "Contestant number one: get into place."
hide screen new_phone_screen
$ guess_who_list = [["ep11_pp_act2_event_tiffani",0],["ep11_pp_act2_event_gina",0],["ep11_pp_act2_event_melanie",0],["ep11_pp_act2_event_sarah",1],["ep11_pp_act2_event_rose",1],["ep11_pp_act2_event_felicia",1],["ep11_pp_act2_event_leanne",0],["ep11_pp_act2_event_elena",0],["ep11_pp_act2_event_becky",0],["ep11_pp_act2_event_bianca",1],["ep11_pp_act2_event_clara",0],["ep11_pp_act2_event_carla",1],["ep11_pp_act2_event_ashley",1],["ep11_pp_act2_event_mia",0],["ep11_pp_act2_event_erin",1],["ep11_pp_act2_event_micha",0],["ep11_pp_act2_event_camila",1],["ep11_pp_act2_event_tania",0],["ep11_pp_act2_event_sally",1]]
$ renpy.random.shuffle(guess_who_list)
$ guess_who_score = 0
$ tmpInt = 0
scene ep11_pp_act2_event12 with dissolve
$ renpy.pause()
label ep11_guess_who_loop:
play sound "sound_effects/shower_curtain.mp3"
scene expression guess_who_list[tmpInt][0] with dissolve
if tmpInt == 0:
    "*{i}Whistles{/i}*"
    le "No way, you put cardboard up for it? That makes it so much harder."
    guy "Are we supposed to know their names or...?"
    ma "Yeah, I suck at names. I'm better with faces."
    de "Only names will be accepted as answers. Write your guess for number one."
    mc "(Hm...)"
elif tmpInt == 1:
    "*{i}Whistles{/i}*"
    mc "(Who could that be?)"
elif tmpInt == 2:
    de "Spelling isn't important, but it's gotta be somewhat close to their name to count."
elif tmpInt == 3:
    guy "It's weird to complain when the game is this enjoyable, but it's harder than I thought..."
    mc "(For you, maybe...)"
elif tmpInt == 4:
    jac "Oh, I know that one."
    jm "Who?"
elif tmpInt == 5:
    de "Ladies, if you hadn't noticed, the guys are focusing hard over here - and that's a double entendre."
elif tmpInt == 6:
    che "Gah! This is too fucking hard."
    guy "You can do what I do. Just enjoy the show."
elif tmpInt == 7:
    le "Man, everyone is so hot! Awesome idea, [name]."
    mc "Oh? Thanks. I couldn't have done it without any of the girls."
    jac "Hahaha! I just pictured it reversed, and if it was guys hanging brains behind the curtain."
    "*{i}Guys laugh{/i}*"
elif tmpInt == 8:
    jb "I think I have most of them down, but then I get confused... I already put this name down before..."
    jb "Question: Have any of the girls appeared multiple times?"
    de "Nope. They are all different girls."
    jb "Well, fuck..."
else:
    de "This is the final girl, gents. I hope you've got ten names on your piece of paper after this one."
if persistent.mod_wtenabled:
    $ tmp_mod = guess_who_list[tmpInt][0]
    $ tmp_mod = tmp_mod.replace("ep11_pp_act2_event_","")
    $ tmp_mod = tmp_mod.capitalize()
    #$ renpy.notify("Pick %s" % (tmp_mod))
    show screen notify_mod ("Pick ",tmp_mod)
if guess_who_list[tmpInt][1] == 0:
    menu:
        "Becky":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_becky":
                $ guess_who_score += 1
            mc "(I think that's Becky...)"
        "Clara":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_clara":
                $ guess_who_score += 1
            mc "(Could that be Clara?)"
        "Elena":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_elena":
                $ guess_who_score += 1
            mc "(Elena, right?)"
        "Gina":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_gina":
                $ guess_who_score += 1
            mc "(I think that's Gina...)"
        "Leanne":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_leanne":
                $ guess_who_score += 1
            mc "(Leanne, was it?)"
        "Melanie":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_melanie":
                $ guess_who_score += 1
            mc "(Could that be Melanie?)"
        "Mia":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_mia":
                $ guess_who_score += 1
            mc "(I think that's Mia...)"
        "Micha":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_micha":
                $ guess_who_score += 1
            mc "(Micha, right?)"
        "Tania":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_tania":
                $ guess_who_score += 1
            mc "(Tania, I think...)"
        "Tiffani":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_tiffani":
                $ guess_who_score += 1
            mc "(I think that's Tiffani...)"
else:
    menu:
        "Ashley":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_ashley":
                $ guess_who_score += 1
            mc "(I think that's Ashley...)"
        "Bianca":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_bianca":
                $ guess_who_score += 1
            mc "(Could that be Bianca?)"
        "Camila":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_camila":
                $ guess_who_score += 1
            mc "(That's Camila, right? Damn, this disco light.)"
        "Carla":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_carla":
                $ guess_who_score += 1
            mc "(I think that's Carla...)"
        "Erin":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_erin":
                $ guess_who_score += 1
            mc "(Could that be that girl Erin?)"
        "Felicia":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_felicia":
                $ guess_who_score += 1
                mc "(Felicia, was it?)"
        "Gina":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_gina":
                $ guess_who_score += 1
            mc "(I think that's Gina...)"
        "Rose":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_rose":
                $ guess_who_score += 1
            mc "(Rose, right?)"
        "Sally":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_sally":
                $ guess_who_score += 1
            mc "(Sally, I think...)"
        "Sarah":
            if guess_who_list[tmpInt][0] == "ep11_pp_act2_event_sarah":
                $ guess_who_score += 1
            mc "(I think that's Sarah...)"

play sound "sound_effects/shower_curtain.mp3"
scene ep11_pp_act2_event13 with dissolve
if tmpInt == 0:
    de "May we have the next girl?"
elif tmpInt < 5:
    de "Next girl, please."
elif tmpInt == 5:
    de "We're in the home stretch now. Next girl!"
elif tmpInt < 9:
    de "Next!"
$ tmpInt += 1
if tmpInt < 10:
    jump ep11_guess_who_loop

de "And that's it! Guys, write your name on your paper and hand them to me."
scene ep11_pp_act2_event11 with dissolve
de "A round of cheers for our contestants behind that curtain."
"*{i}Cheers{/i}*"
show screen new_phone_screen

label ep11_pp_act2_eventb_label:
if ep5_dikWinner:
    $ event_list.append("part2_arieth")
    label ep11_pp_act2_event2_label:
    if ep11_mg_party or wt_ep11_party_bella:
        play sound "sound_effects/whoosh.mp3"
        scene ep11_pp_act2_event24
    else:
        scene ep11_pp_act2_event24
        hide screen dance_filter_screen
        with dissolve
    if in_bios("Arieth suggested to use my cock for her dick-cloning sets."):
        ar "[name]? I changed my mind on the dick-cloning sets; we can split it 60/50."
    else:
        ar "[name]? I have an idea that will make us millionaires."
    scene ep11_pp_act2_event25 with dissolve
    ar "[name]? Are you in here?"
    scene ep11_pp_act2_event26 with dissolve
    ar "Oh, hubba hubba."
    if ep11_mg_party:
        jump ep11_gift2_label
    elif ep11_pp_game > 0:
        jump ep11_pp_act2_eventc_label
elif ep11_pp_game > 0:
    jump ep11_pp_act2_eventc_label
scene ep11_pp_act2_event14
show screen dance_filter_screen
with dissolve
le "How many correct ones did you get?"
$ tmpBool3 = False
scene ep11_pp_act2_event15 with dissolve
menu:
    "All of them":
        $ tmpBool3 = True
        mc "All of them, of course! It was easy."
        scene ep11_pp_act2_event16 with dissolve
        le "What? No way. You can't possibly have aced it."
        scene ep11_pp_act2_event15 with dissolve
    "More than half":
        mc "Hopefully, more than half."
    "Not many":
        mc "It was hard. I don't think I got many."
mc "What about you?"
scene ep11_pp_act2_event16 with dissolve
le "It sounded like an easy competition, but it wasn't."
le "I didn't recognize a couple of them, but I know I identified at least three pairs of tits and ass."
scene ep11_pp_act2_event11 with dissolve
de "Alright, gather around. The scores have been tallied and I'm surprised by everyone's effort."
de "Overall, you did well. But there was one of you who stood out from the rest..."
scene ep11_pp_act2_event22 with dissolve
de "And I mean that in a bad way. Marc wrote ten names - all either incorrect or names of girls who weren't at this party."
scene ep11_pp_act2_event18 with dissolve
"*{i}Laughter{/i}*"
ma "I had to guess something. Maybe it was a trick question?"
scene ep11_pp_act2_event11 with dissolve
de "But on the other side of the spectrum..."
if guess_who_score > 7:
    if guess_who_score == 10:
        de "With ten out of ten freaking points, we have a winner."
        "*{i}Gasps{/i}*"
    elif guess_who_score > 7:
        de "With a whopping [guess_who_score] points, we have a winner."
else:
    de "With a whopping 8 points, we have a winner."
de "Man, this guy spent the better time at the party checking girls out. Am I right?"
scene ep11_pp_act2_event21 with dissolve
if guess_who_score > 7:
    de "The winner is [name]!"
    if guess_who_score == 10:
        if tmpBool3:
            scene ep11_pp_act2_event17 with dissolve
            mc "What did I tell you?"
            scene ep11_pp_act2_event19 with dissolve
            le "Do you have x-ray vision or something? That's insane."
        else:
            scene ep11_pp_act2_event19 with dissolve
            le "You got all of them and you didn't even know it... How?"
            scene ep11_pp_act2_event17 with dissolve
            mc "Beats me."
    else:
        if tmpBool3:
            scene ep11_pp_act2_event19 with dissolve
            le "All of them, huh?"
            scene ep11_pp_act2_event17 with dissolve
            mc "I still won."
        else:
            scene ep11_pp_act2_event19 with dissolve
            le "Congrats!"
    scene ep11_pp_act2_event21 with dissolve
    de "Congratulations to [name], and thanks to everyone behind the curtain."
else:
    de "The winner is Tommy!"
    scene ep11_pp_act2_event20 with dissolve
    "*{i}Cheers{/i}*"
    tm "It was easy. What can I say? I know my tits and ass."
    if tmpBool3:
        scene ep11_pp_act2_event19 with dissolve
        le "All of them, huh?"
        scene ep11_pp_act2_event17 with dissolve
        mc "Yeah, yeah."
    scene ep11_pp_act2_event21 with dissolve
    de "Congratulations to Tommy, and thanks to everyone behind the curtain."

if minigames:
    scene ep11_pp_act2_event23 with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
    $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
    $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
    $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
    $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)

    $ mphone_pp_history_list.append("• The {color=ffed00}Guess Who? Game{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Guess Who? Game{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Guess Who? Game{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Guess Who? Game{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}Guess Who? Game{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg

if guess_who_score == 10:
    if steamAchievements:
        $ achievement.grant("IDS3_44")
        init:
            $ achievement.register("IDS3_44")
        $ achievement.Sync()

label ep11_pp_act2_eventc_label:
$ freeRoamID = "ep11_4c"
if ep11_x:
    $ event_list.append("ep11_pp_elena_lewd_event_label")
    if persistent.mod_wtenabled:
        $ task_list[1] = "Find Elena (John Boy's room)"
    else:
        $ task_list[1] = "Find Elena"

if ep10_rolling:
    $ event_list.append("ep11_pp_lily_event_label")
    if persistent.mod_wtenabled:
        $ task_list[12] = "Talk to Lily (Main Party room)"
    else:
        $ task_list[12] = "Talk to Lily"
    

if ep11_invited_tara:
    $ event_list.append("ep11_tara_event_label")
    if persistent.mod_wtenabled:
        $ task_list[2] = "Talk to Tara (Main Party room)"
    else:
        $ task_list[2] = "Talk to Tara"
$ event_list.append("ep11_tiffani_event_label")
if persistent.mod_wtenabled:
    $ task_list[4] = "Talk to Tiffani (Main party room)"
else:
    $ task_list[4] = "Talk to Tiffani"
if ep11_girl_drink_opportunity:
    $ event_list.append("ep11_pp_mt2_event_label")
    if persistent.mod_wtenabled:
    
        $ optional_task_list[3] = "Inspect the table with refreshments\n(Right Hallway)"
    else:
        $ optional_task_list[3] = "Inspect the table with refreshments"
    
$ updateTaskList()
$ event_list.append("part2_act2")

$ updateTaskList()
$ currentFreeRoamLabel = "ep11_diks_pp_tommy_label"
jump endEvent

label ep11_becky_event_label:
$ guideSuggestedPage = 205
scene ep11_becky_event1 with dissolve
bc "There you are. I've been looking all over for you."
scene ep11_becky_event2 with dissolve
mc "What do you want?"
scene ep11_becky_event3 with dissolve
bc "I've decided that you're worthy."
scene ep11_becky_event4 with dissolve
mc "Worthy of what?"
scene ep11_becky_event3 with dissolve
bc "Let's put it like this..."
bc "I'm going to head into your room and undress on your bed..."
bc "Wait one minute, then come join me."
scene ep11_becky_event5 with dissolve
bc "I'm going to rock your world tonight."
bc "You've never had someone like me before. I go crazy in bed."
scene ep11_becky_event4 with dissolve

if persistent.mod_wtenabled:
                        $mod_choices = ["(Possible Melanie scene)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

if not branchAlone:
    menu:
        "Deny her":
            jump ep11_becky_event2_label
        "Prank her \n{size=-4}[m_c1][mod_choices[3]]":
            jump ep11_becky_event3_label
menu:
    "Have sex with her":
        mc "That's a bold claim."
        scene ep11_becky_event5 with dissolve
        bc "I'll show you."
        scene ep11_becky_event10 with dissolve
        bc "Don't forget to lock the door behind you."
        scene ep11_becky_event13 with dissolve
        mc "(It's sex... But it's with Becky...)"
        mc "(It's a battle between mind and cock right now, and oddly...my cock is making some good arguments for it...)"
        if ep10_rolling:
            mc "(But Lily told me I should wear a rubber with her... Where could I get one in a minute's notice?)"
        else:
            mc "(My mind is saying I should wear a rubber...and my cock is saying that's a fair compromise.)"
            mc "(Where could I get one in a minute's notice?)"
        scene ep11_becky_event16 with dissolve
        ar "I'm very discreet. Send me a text and I'll get you anything you need."
        ar "Dildos, lube, a Fuckdoll Sperminator 2000XXL BBC version with loadable cumshots... You name it!"
        scene ep11_becky_event17 with dissolve
        mc "Arieth. I need a condom."
        scene ep11_becky_event18 with dissolve
        ar "That will be $10."
        scene ep11_becky_event19 with dissolve
        mc "For one condom?"
        scene ep11_becky_event18 with dissolve
        ar "Normally, I'm cheaper, but you seem to need it."
        scene ep11_becky_event19 with dissolve
        mc "I'll pay you later."
        scene ep11_becky_event18 with dissolve
        ar "I'm gonna hold you to that. Follow me..."
        stop music fadeout 3
        scene ep11_becky_event20 with dissolve
        mc "($10 to fuck Becky... She better rock my world.)"
        jump ep11_becky_lewd_label
    "Deny her":
        label ep11_becky_event2_label:
        if affinity == "DIK":
            $ ep11_becky_lewd = 2
            mc "Eww... No."
            scene ep11_becky_event6 with dissolve
            bc "What do you mean \"Eww\"?"
            scene ep11_becky_event7 with dissolve
            mc "Go away, Becky. I'm not having sex with you."
            scene ep11_becky_event8 with dissolve
            $ renpy.pause()
        else:
            $ ep11_becky_lewd = 3
            mc "I'm not in the mood for world-rocking or craziness tonight, Becky. I'll have to pass."
            scene ep11_becky_event5 with dissolve
            bc "Come on... We've been doing this dance all semester long, [name]. It's Becky-time."
            scene ep11_becky_event7 with dissolve
            mc "No means no. You're a girl, you should know all about that."
            scene ep11_becky_event8 with dissolve
            $ renpy.pause()
        $ new_bio("Becky", "Becky wanted to have sex with me, but I turned her down.")
    "Prank her \n{size=-4}[m_c1][mod_choices[3]]":
        label ep11_becky_event3_label:
        $ dk(2)
        $ ep11_becky_lewd = 1
        mc "Rock my world, you say?"
        scene ep11_becky_event5 with dissolve
        bc "Super-rock your world. Are you in?"
        scene ep11_becky_event4 with dissolve
        mc "I'd be a fool to say no, wouldn't I?"
        scene ep11_becky_event3 with dissolve
        bc "Yes, you would."
        scene ep11_becky_event10 with dissolve
        bc "Don't forget to lock the door behind you."
        scene ep11_becky_event14 with dissolve
        mc "Hey, guys... Enjoying the party?"
        mc "There's a naked chick on my bed who wants to do her Dirty Bowl task, and it's first come, first serve."
        mc "You should head into that room right now."
        scene ep11_becky_event15 with dissolve
        mc "Good luck!"
        scene ep11_becky_event12 with dissolve
        mc "3...2...1..."
        bc "AHHH!!!"
        scene ep11_becky_event11 with dissolve
        mc "Hahaha!"
        scene ep11_becky_event9 with dissolve
        mc "Becky, where are you going?"
        $ new_bio("Becky", "Becky wanted to have sex with me, but I ended up pranking her instead.")
$ task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_st_event_label:
scene ep11_pp_st_event1 with dissolve
rs "She doesn't have to do it."
scene ep11_pp_st_event2 with dissolve
mic "I don't even know what it means. Does it have something to do with shots?"
scene ep11_pp_st_event6 with dissolve
sar "Aw, precious."
tm "Hahaha!"
scene ep11_pp_st_event3 with dissolve
rs "No, getting rimmed is something else..."
scene ep11_pp_st_event2 with dissolve
mic "What is it? Maybe I'll do it."
scene ep11_pp_st_event4 with dissolve
rs "*{i}Whispers{/i}*"
scene ep11_pp_st_event5 with dissolve
mic "You can't be serious! I'm not doing that!"
scene ep11_pp_st_event7 with dissolve
"Hahaha!"
scene ep11_pp_st_event8 with dissolve
sar "I swear, there's something wrong with [name] and his perverted brain coming up with these ideas and expecting us to do them."
if ep9_heather_lewd != 2:
    scene ep11_pp_st_event9 with dissolve
    tm "I taught him everything I know."
else:
    scene ep11_pp_st_event10 with dissolve
    tm "I think I taught him too much. He's a huge DIK."
    scene ep11_pp_st_event12 with dissolve
    rs "Did you try to iron it out with him?"
    scene ep11_pp_st_event11 with dissolve
    tm "Would you have?"
    scene ep11_pp_st_event12 with dissolve
    rs "I'm not sure... But it takes two to tango."
    scene ep11_pp_st_event11 with dissolve
    tm "Who the fuck wants to tango?"
scene ep11_pp_st_event14 with dissolve
$ renpy.pause()
scene ep11_pp_st_event13 with dissolve
tm "HEY! Get the fuck out of there."
scene ep11_pp_st_event15 with dissolve
tm "Don't fucking open my fridge! Who told you it was ok to be back here?"
scene ep11_pp_st_event16 with dissolve
guy "Whoa! Chillax! I was looking for beer."
scene ep11_pp_st_event15 with dissolve
tm "The keg is out there. Don't fucking touch my things or I'll kick your ass out."
scene ep11_pp_st_event16 with dissolve
guy "Yeah... Sorry."

$ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_kp_event_label:
$ guideSuggestedPage = 204
scene ep11_pp_kp_event1 with dissolve
le "[name]! [name]!"
le "We have a situation."
scene ep11_pp_kp_event2 with dissolve
mc "Can't you guys take care of it? I'm not a leader or a parent here."
scene ep11_pp_kp_event5 with dissolve
sar "Haha, papi [name]."
scene ep11_pp_kp_event6 with dissolve
mc "Stop that."
scene ep11_pp_kp_event4 with dissolve
jac "We can solve it, but we gotta know who's on the invite list before we do."
scene ep11_pp_kp_event2 with dissolve
mc "Lots of people are. It's faster if you say who you're wondering about."
scene ep11_pp_kp_event4 with dissolve
jac "Kylie and Penny showed up, bro."
scene ep11_pp_kp_event3 with dissolve
le "Yeah! And I thought we said no to all those girls."
if ep11_invited_tara:
    le "But then I remembered you invited Tara and got confused."
scene ep11_pp_kp_event2 with dissolve
mc "Kylie and Penny are here? No, I didn't invite them. Have any of you even talked to them lately?"
scene ep11_pp_kp_event3 with dissolve
le "Pff! Not since I caught them with those posters, no. They burned the bridge with me, let me tell you that much."
scene ep11_pp_kp_event4 with dissolve
jac "Yeah, I'm pretty sure someone would have mentioned it as a heads-up."
scene ep11_pp_kp_event7 with dissolve
sar "I heard them say they were showing up. That's about what I can tell you."
scene ep11_pp_kp_event2 with dissolve
mc "Well, then that does it. They crashed our party and did not apologize for what they did to us."
scene ep11_pp_kp_event3 with dissolve
le "We gotta kick them out. I'm on it!"
scene ep11_pp_kp_event2 with dissolve
$ mc_info = ["{size=-%d}Pull a mean prank{/size}" % persistent.scale_factor,"ep11_pp_kp_prank_event_label","{size=-%d}Let them handle it{/size}" % persistent.scale_factor,"ep11_pp_kp_boot_event_label","{size=-%d}Confront Kylie & Penny{/size}" % persistent.scale_factor,"ep11_pp_kp_confront_event_label",not ep11_invited_tara]
show screen major_choice_screen
$ renpy.pause()

label ep11_pp_kp_prank_event_label:
$ ep11_kp_choice = "DIK"
scene ep11_pp_kp_event9 with dissolve
mc "Hold on a second, Leon... They are here in their underwear, yeah?"
mc "An opportunity just presented itself... This is what we'll do."
scene ep11_pp_kp_event26
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_pp_kp_event27 with dissolve
jac "Back to where you came from."
ky "Get off me!"
py "Ah!"
play sound "sound_effects/door_lock.mp3"
$ renpy.sound.play("sound_effects/door_slam.mp3", channel="sfx2", loop=False)
scene ep11_pp_kp_event28 with dissolve
ky "Hey! What the hell!?"
play sound "sound_effects/door_bang.mp3"
scene ep11_pp_kp_event29 with hpunch
ky "What about our clothes!? Hello!? It's fucking freezing!"
mc "Kylie? Penny? Up here!"
scene ep11_pp_kp_event33 with dissolve
ky "[name]!? Let us back in!"
scene ep11_pp_kp_event34 with dissolve
mc "It's cold outside tonight. Where are your jackets?"
scene ep11_pp_kp_event30 with dissolve
py "You guys locked us outside!"
scene ep11_pp_kp_event34 with dissolve
mc "Oh yeah! That's why... You're not invited to our parties anymore... I knew there was something I forgot."
scene ep11_pp_kp_event35 with dissolve
mc "Do you seriously believe you're welcome back here after what you did?"
scene ep11_pp_kp_event31 with dissolve
mc "Fuck off to your dorms, will you?"
mc "And Kylie? Perhaps this will serve as a bonding experience with your sister. Say hi to her from us!"
scene ep11_pp_kp_event32 with dissolve
ky "You asshole!"
scene ep11_pp_kp_event35 with dissolve
mc "Go start another rumor, why don't you?"
scene ep11_pp_kp_event36 with dissolve
tm "Ice cold..."
scene ep11_pp_kp_event37 with dissolve
mc "It is, isn't it? Let's head back inside."
hide screen ep10_snow_screen
$ task_list[11] = ""
$ updateTaskList()
$ new_bio("You", "I decided to prank Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
$ new_bio("Kylie", "I decided to prank Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
jump endEvent

label ep11_pp_kp_boot_event_label:
$ ep11_kp_choice = "NEUTRAL"
scene ep11_pp_kp_event8 with dissolve
mc "Sounds like we're all in agreement here."
scene ep11_pp_kp_event26
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_pp_kp_event38 with dissolve
jac "Party is over, girls."
ky "Fuck you, Jacob!"
scene ep11_pp_kp_event39 with dissolve
jac "And have a nice night to you, too."
$ renpy.sound.play("sound_effects/door_slam.mp3", channel="sfx2", loop=False)
scene ep11_pp_kp_event40 with dissolve
ky "Assholes!!!"
hide screen ep10_snow_screen
$ task_list[11] = ""
$ updateTaskList()
$ new_bio("You", "I let Leon and Jacob handle Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
$ new_bio("Kylie", "I let Leon and Jacob handle Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
$ new_bio("Jacob", "I let Leon and Jacob handle Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
$ new_bio("Leon", "I let Leon and Jacob handle Kylie and Penny when they crashed the DIKs' Christmas Panty party.")
jump endEvent

label ep11_pp_kp_confront_event_label:
$ ep11_kp_choice = "CHICK"
mc "Hold on... Let me handle this."
scene ep11_pp_kp_event3 with dissolve
le "You said you didn't want to."
scene ep11_pp_kp_event2 with dissolve
mc "They're here in their underwear. That's pretty disarming, yeah? Maybe we could try some diplomacy instead of adding fuel to the fire."
scene ep11_pp_kp_event10
show screen dance_filter_screen
with dissolve
$ renpy.pause()
scene ep11_pp_kp_event11 with dissolve
mc "Well, what do we have here?"
scene ep11_pp_kp_event12 with dissolve
py "What?"
scene ep11_pp_kp_event13 with dissolve
mc "Do you seriously believe you're welcome here after what you did? Who invited you?"
if ep11_invited_tara:
    scene ep11_pp_kp_event14 with dissolve
    ky "You invited Tara."
    scene ep11_pp_kp_event15 with dissolve
    mc "We're cool with Tara. She's been talking to us about this and feels sorry. I haven't heard you two apologize."
else:
    mc "Who did you apologize to? I haven't heard it."
scene ep11_pp_kp_event14 with dissolve
ky "Relax, it's just a party."
scene ep11_pp_kp_event15 with dissolve
mc "No, it's not just a party. It's our party."
mc "Why do you even want to be here?"
scene ep11_pp_kp_event12 with dissolve
py "We're here because our friends are here."
scene ep11_pp_kp_event13 with dissolve
mc "Your friends were invited, but you weren't."
scene ep11_pp_kp_event14 with dissolve
ky "Come on, uninvited guests always show up."
scene ep11_pp_kp_event13 with dissolve
mc "But unwanted guests get kicked out. And that's what you are."
mc "Are you sorry for what you did? Do you plan on apologizing?"
scene ep11_pp_kp_event14 with dissolve
ky "Are you guys sorry about what YOU did?"
scene ep11_pp_kp_event20 with dissolve
le "There's your answer, [name]. There's no point in discussing it with them."
le "They don't see anything wrong with what they did."
scene ep11_pp_kp_event21 with dissolve
mc "If I had something to apologize for, I'd own it. But I can't speak for you guys."
scene ep11_pp_kp_event22 with dissolve
jac "Apologize for some harmless pranks? I don't think so."
scene ep11_pp_kp_event14 with dissolve
ky "You guys locked my sister outside naked and made her walk back to her dorm! How's that harmless!?"
scene ep11_pp_kp_event22 with dissolve
jac "It wasn't me; I've only been singing songs the day after chicks boned a DIK."
scene ep11_pp_kp_event23 with dissolve
le "I'm not sorry, either. You can fuck off!"
scene ep11_pp_kp_event13 with dissolve
mc "As I take it, the guy who's responsible for what happened to your sister isn't even with us anymore."
mc "It's unfair to punish us for that. And if the Walk of Shame bothered you so much...why did you sleep with DIKs?"
mc "It's a well-known tradition and pretty damned easy to avoid."
scene ep11_pp_kp_event14 with dissolve
ky "I'm not apologizing."
scene ep11_pp_kp_event16 with dissolve
mc "What about you?"
scene ep11_pp_kp_event18 with dissolve
ky "Don't apologize."
scene ep11_pp_kp_event17 with dissolve
py "I'm sorry."
scene ep11_pp_kp_event18 with dissolve
ky "Penny!"
scene ep11_pp_kp_event19 with dissolve
py "When he puts it like that... These guys aren't to blame for what happened to your sister."
scene ep11_pp_kp_event18 with dissolve
ky "What about the rest of us? What about what they did to Cathy?"
scene ep11_pp_kp_event22 with dissolve
jac "That wasn't us. Someone set us up."
scene ep11_pp_kp_event17 with dissolve
py "I don't know anymore. I'm tired of the drama... It's Christmas."
scene ep11_pp_kp_event16 with dissolve
mc "I accept your apology, Penny. Thank you, and you may stay at the party."
scene ep11_pp_kp_event21 with dissolve
mc "Guys?"
scene ep11_pp_kp_event22 with dissolve
jac "Yeah, whatever you say."
scene ep11_pp_kp_event20 with dissolve
le "This is wrong, [name]..."
scene ep11_pp_kp_event15 with dissolve
mc "Kylie, if you change your mind, let me know. Since it's Christmas, you get to stay. Consider it the DIKs' gift to you."
scene ep11_pp_kp_event24 with dissolve
le "Bad call, [name]..."
scene ep11_pp_kp_event25 with dissolve
mc "We won Penny over. Hopefully, she'll get the others to apologize, too."
jac "Coming to a party where you're unwanted... Women, I don't get them."

$ new_bio("You", "I let Kylie and Penny stay at the DIKs' Christmas Panty party.")
$ new_bio("Kylie", "I let Kylie and Penny stay at the DIKs' Christmas Panty party.")
$ event_list.append("part2_kp")
$ currentFreeRoamLabel = "ep11_diks_pp_tommy_label"
$ task_list[11] = ""
$ updateTaskList()
jump endEvent

label ep11_pp_bia_event_label:
$ event_list.append("part2_bia_done")
scene ep11_pp_bia_event1 with dissolve
bia "[name]! Wanna dance?"
if ep11_mg_party:
    scene ep11_pp_bia_event2 with dissolve
    mc "No, I'm taking off soon."
    scene ep11_pp_bia_event5 with dissolve
    bia "No! Where are you going?"
    scene ep11_pp_bia_event4 with dissolve
    if branchJill:
        mc "I'm going to Jill and some of my friends."
    else:
        mc "I'm going to Bella and some of my friends."
    scene ep11_pp_bia_event5 with dissolve
    bia "You should bring them here!"
    scene ep11_pp_bia_event4 with dissolve
    mc "Haha, I'll try."
    scene ep11_pp_bia_event3 with dissolve
    bia "Hey, do you have a moment before you leave?"
    scene ep11_pp_bia_event4 with dissolve
    mc "Sure."
else:
    scene ep11_pp_bia_event2 with dissolve
    mc "Nah. I feel like drinking at the moment."
    scene ep11_pp_bia_event3 with dissolve
    bia "I'll join you!"

scene ep11_pp_bia_event6 with dissolve
bia "You've done such a great job with the party."
scene ep11_pp_bia_event7 with dissolve
mc "I knew you'd enjoy it."
scene ep11_pp_bia_event6 with dissolve
bia "How so?"
scene ep11_pp_bia_event7 with dissolve
mc "You seem to be into wild things. Snowmobiles, skiing, partying and whatnot..."
scene ep11_pp_bia_event8 with dissolve
bia "We all have wild sides."
scene ep11_pp_bia_event9 with dissolve
mc "Yeah, maybe we do."
scene ep11_pp_bia_event8 with dissolve
bia "And, maybe we all got some sides that we didn't know we had in us."
scene ep11_pp_bia_event9 with dissolve
mc "What sides would that be?"
scene ep11_pp_bia_event10 with dissolve
bia "The ones that make you flirt with someone you shouldn't be flirting with, for one."
scene ep11_pp_bia_event11 with dissolve
$ renpy.pause()
scene ep11_pp_bia_event12 with dissolve
bia "See. You know what I'm saying."
scene ep11_pp_bia_event13 with dissolve
mc "Flirting can be innocent."
scene ep11_pp_bia_event12 with dissolve
bia "Of course. Until it isn't anymore."
scene ep11_pp_bia_event13 with dissolve
mc "I can be a flirty guy at times."
scene ep11_pp_bia_event14 with dissolve
bia "I feel bad. We shouldn't be flirting."
if ep11_bianca_dick > 0:
    bia "And we definitely shouldn't be naked touching stuff in hot tubs."
else:
    bia "And we definitely shouldn't be naked in hot tubs together."
scene ep11_pp_bia_event13 with dissolve
mc "See, what you're doing right now is flirting. How do you expect me not to respond to it?"
$ guideSuggestedPage = 206
scene ep11_pp_bia_event14 with dissolve
if ep9_told_jill:
    bia "I'm single. I can flirt. You, however...cannot. It's dangerous."
else:
    bia "We're not single. We shouldn't flirt... It's dangerous."
scene ep11_pp_bia_event13 with dissolve
if ep11_rusty_choice:
    jump ep11_bia_stop2_label
if persistent.mod_wtenabled:
                        $mod_choices = ["(More options)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
menu:
    "I hear you \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        label ep11_bia_stop2_label:
        mc "I hear you. There will be no more flirting on my end."
        scene ep11_pp_bia_event15 with dissolve
        bia "Are you sure?"
        label ep11_bia_stop_label:
        scene ep11_pp_bia_event16 with dissolve
        mc "Yes."
        scene ep11_pp_bia_event15 with dissolve
        bia "So... Platonic friends?"
        scene ep11_pp_bia_event16 with dissolve
        mc "Yes. Whatever that means."
        scene ep11_pp_bia_event14 with dissolve
        bia "Haha! Friends."
        scene ep11_pp_bia_event17 with dissolve
        bia "Good that we sorted it out."
        bia "Now, friends don't sit in underwear talking to each other. That's dangerous, too. I'm heading back out there."
        $ task_list[6] = ""
        $ updateTaskList()
        $ new_bio("Bianca", "I told Bianca to stop flirting with me.")
        if not ep11_mg_party and ep11_db_mission and not ep11_pp_santa_bc:
            $ specialMessage = "You failed to do The Dirty Bowl Mission."
            show screen specialmsg
            $ optional_task_list[0] = ""
            if "ep11_pp_santa_bc_event_label" in event_list:
                $ event_list.remove("ep11_pp_santa_bc_event_label")
            if "ep11_pp_santa_event_label" in event_list:
                $ event_list.remove("ep11_pp_santa_event_label")
            if "ep11_pp_santa_sandy_event_label" in event_list:
                $ event_list.remove("ep11_pp_santa_sandy_event_label")
            if "ep11_pp_santa_heather_event_label" in event_list:
                $ event_list.remove("ep11_pp_santa_heather_event_label")
            if "ep11_pp_santa_event_label" in event_list:
                $ event_list.remove("ep11_pp_santa_event_label")
        jump endEvent
    "You bring it out of me \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
        $ dk(1)
        mc "What can I say? You bring it out of me."
        scene ep11_pp_bia_event21 with dissolve
        bia "Stop that."
        scene ep11_pp_bia_event13 with dissolve
        mc "We're both aware that we're doing it."
        scene ep11_pp_bia_event18 with dissolve
        bia "Well, what are we gonna do about it?"
        scene ep11_pp_bia_event19 with dissolve
        
        if persistent.mod_wtenabled:
                        $mod_choices = ["(Bianca path)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
        
        menu:
            "We should stop \n{size=-4}[m_c1][mod_choices[2]]":
                $ dk(-1)
                mc "We should stop before it escalates. You're right; it can be dangerous."
                scene ep11_pp_bia_event15 with dissolve
                bia "Ok... Are you sure?"
                jump ep11_bia_stop_label
            "Flirt more \n{size=-4}[m_c2][mod_choices[0]][m_c3][mod_choices[7]]":
                $ ep11_bianca_path = True
                if not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1):
                    $ tc += 5
                mc "That's up to you."
                scene ep11_pp_bia_event23 with dissolve
                bia "Nuh-uh. You're not leaving me with that responsibility. You gotta own it, too."
                scene ep11_pp_bia_event24 with dissolve
                mc "I can't stop flirting with you. Have you looked at yourself in the mirror?"
                scene ep11_pp_bia_event23 with dissolve
                bia "I have. That's why we're having this talk."
                scene ep11_pp_bia_event24 with dissolve
                mc "No, I meant an actual mirror. Like...damn... You know?"
                scene ep11_pp_bia_event25 with dissolve
                bia "*{i}Sigh{/i}*"
                scene ep11_pp_bia_event23 with dissolve
                if branchJill:
                    bia "Jill's one of my closest friends. I feel so bad."
                    if ep9_told_jill:
                        bia "And I know how it feels to be on the receiving end of this because of Matty and Olivia."
                    else:
                        bia "And Matty would punch you if he heard this conversation."
                else:
                    bia "Bella is a friend, and she's Jill's close friend. I feel so bad."
                scene ep11_pp_bia_event24 with dissolve
                mc "Sounds like you've decided then."
                scene ep11_pp_bia_event18 with dissolve
                bia "But like I said earlier, there's that side of me I didn't know I had."
                bia "That shameless side that gets a good kick out of this."
                scene ep11_pp_bia_event19 with dissolve
                mc "Yeah... How good of a kick do you get?"
                scene ep11_pp_bia_event20 with dissolve
                bia "..."
                scene ep11_pp_bia_event18 with dissolve
                bia "I've touched myself thinking about you. How's that for an answer?"
                $ new_bio("Bianca", "I told Bianca that I liked flirting with her.")
                scene ep11_pp_bia_event19 with dissolve
                mc "Fuck..."
                scene ep11_pp_bia_event26 with dissolve
                bia "Give me your number."
                scene ep11_pp_bia_event27 with dissolve
                mc "Are you sure you want it?"
                scene ep11_pp_bia_event26 with dissolve
                bia "I think I do. But Carla is here tonight, so I can't...you know?"
                scene ep11_pp_bia_event27 with dissolve
                mc "I'll send you a DM on Rooster."
                scene ep11_pp_bia_event28 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event29 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event30 with dissolve
                bia "Bad... We're so bad."
                scene ep11_pp_bia_event31 with dissolve
                mc "Hey... Did you get around to doing those three things tonight?"
                scene ep11_pp_bia_event30 with dissolve
                if ep11_dildo_sucking_girl == "Bianca":
                    bia "I don't have to. I got a free pass thanks to that contest, remember?"
                    scene ep11_pp_bia_event31 with dissolve
                    mc "Oh, yeah."
                    mc "You could give that one to Carla."
                    scene ep11_pp_bia_event30 with dissolve
                    bia "Why?"
                    scene ep11_pp_bia_event31 with dissolve
                    mc "If you do your task, both of you could stay."
                else:
                    bia "I'm not staying past midnight if that's what you're asking."
                    scene ep11_pp_bia_event31 with dissolve
                    mc "Do you want to?"
                scene ep11_pp_bia_event32 with dissolve
                $ renpy.pause()
                play sound "sound_effects/shower_curtain.mp3"
                scene ep11_pp_bia_event33 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event34 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event35 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event36 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event37 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event38 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event39 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event40 with dissolve
                $ renpy.pause()
                play sound "sound_effects/slap.mp3"
                scene ep11_pp_bia_event41 with hpunch
                $ renpy.pause()
                scene ep11_pp_bia_event42 with dissolve
                bia "Hnn... Mmm..."
                scene ep11_pp_bia_event43 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event44 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event45 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event46 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event47 with dissolve
                bia "*{i}Gasps{/i}*"
                scene ep11_pp_bia_event48 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event49 with dissolve
                $ renpy.pause()
                scene ep11_pp_bia_event50 with dissolve
                $ renpy.pause()
                $ task_list[6] = ""
                $ updateTaskList()
                $ new_bio("Bianca", "I helped Bianca with her Dirty Bowl mission. But the mission didn't matter; we wanted to do that regardless.")
                jump endEvent

label ep11_pp_nl_event_label:
$ guideSuggestedPage = 203
scene ep11_pp_nl_event1 with dissolve
nic "[name]!"
scene ep11_pp_nl_event2 with dissolve
nic "Do I have something fun for us to do..."
scene ep11_pp_nl_event3 with dissolve
mc "Is it a Dirty Bowl kind of fun thing?"
scene ep11_pp_nl_event2 with dissolve
nic "Oh, that? No, I didn't take one after seeing what the others got."
scene ep11_pp_nl_event3 with dissolve
mc "Naughty, naughty..."
scene ep11_pp_nl_event2 with dissolve
nic "Let's sneak away for a while. Meet me in your room, I'm gonna fetch something."
scene ep11_pp_nl_event4 with dissolve
nic "Finally, we get some alone time together. How have you been?"
scene ep11_pp_nl_event5 with dissolve
nic "*{i}Smack{/i}*"

if persistent.mod_wtenabled:
                        $mod_choices = ["(Bianca path)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"

menu:
    "I've been doing good":
        scene ep11_pp_nl_event6 with dissolve
        mc "I've been doing good. School, gym, and all that. How about you?"
        scene ep11_pp_nl_event7 with dissolve
        nic "It's been hectic. Marvin got sick, and I had to stay home from work for several days."
        nic "Which, in turn, meant that I had to work extra to cover the shifts I missed."
    "I've missed you \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep11_pp_nl_event6 with dissolve
        mc "I've missed you."
        scene ep11_pp_nl_event8 with dissolve
        nic "Aw, I've missed you too."
scene ep11_pp_nl_event9 with dissolve
nic "I can't tell you how much I needed this party."
scene ep11_pp_nl_event11 with dissolve
nic "I figured we could share some of this. What do you say?"
mc "Hm... Not tonight. I need most of my senses available."
scene ep11_pp_nl_event9 with dissolve
nic "It's not that strong."
scene ep11_pp_nl_event10 with dissolve
mc "Go ahead and smoke. Maybe I'll have one inhale of it - tops."
scene ep11_pp_nl_event9 with dissolve
nic "In here? Are you sure that's ok?"
scene ep11_pp_nl_event10 with dissolve
mc "Let's crack the window open."
scene ep11_pp_nl_event12 with dissolve
nic "Mmm... That's the stuff..."
nic "I haven't smoked in a couple of weeks. I never do it when I have Marvin."
scene ep11_pp_nl_event13 with dissolve
nic "Here. Have some."
scene ep11_pp_nl_event14 with dissolve
nic "You're pretty tonight."
if affinity == "DIK":
    scene ep11_pp_nl_event16 with dissolve
    mc "What do you mean \"tonight\"? I'm always pretty."
    scene ep11_pp_nl_event15 with dissolve
    nic "Hahaha!"
    scene ep11_pp_nl_event16 with dissolve
else:
    scene ep11_pp_nl_event16 with dissolve
    mc "Thanks. So are you."
mc "I like what you're wearing."
scene ep11_pp_nl_event17 with dissolve
nic "Red is not my color."
scene ep11_pp_nl_event16 with dissolve
mc "No, it suits you."
if ep10_rolling:
    scene ep11_pp_nl_event18 with dissolve
    mc "I talked to Lily earlier tonight..."
    mc "I'm not sure if you're aware, but Lily and I started to roll together after Halloween."
    scene ep11_pp_nl_event19 with dissolve
    nic "Is that slang for something?"
    scene ep11_pp_nl_event18 with dissolve
    mc "I've had a hard time understanding what it was myself. But it's like hanging out and having sex."
    scene ep11_pp_nl_event19 with dissolve
    nic "Do you mean that you're dating Lily?"
    scene ep11_pp_nl_event18 with dissolve
    mc "No, that's not what it is."
    scene ep11_pp_nl_event20 with dissolve
    nic "It sounds like it."
    scene ep11_pp_nl_event18 with dissolve
    mc "She's been very clear it's not dating or a relationship. It's more like an open relationship, but not even that."
    mc "We're just having fun together."
    scene ep11_pp_nl_event20 with dissolve
    nic "Ok. Why are you telling me this?"
    scene ep11_pp_nl_event18 with dissolve
    mc "Lily was concerned that you and I were dating while I was rolling with her. She wanted you to know and be cool about it."
    scene ep11_pp_nl_event20 with dissolve
    nic "Oh, I get it."
    nic "Um..."
    scene ep11_pp_nl_event18 with dissolve
    mc "So? Are you cool about it or...?"
    scene ep11_pp_nl_event21 with dissolve
    nic "Whatever it is that you're doing with her..."
    nic "It's not like you'd continue doing that if things got serious between you and me. Or am I wrong?"
    scene ep11_pp_nl_event18 with dissolve
    
    if persistent.mod_wtenabled:
                        $mod_choices = ["(Lily path)","(Nicole path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
    
    menu:
        "Mod: Both paths":
            mc "I can't promise you anything, but I want to continue dating you."
            scene ep11_pp_nl_event25 with dissolve
            nic "Then, it's settled."
            nic "Thanks for telling me. I feel not many guys would."
            pass
        
        "I'm not looking for something serious \n{size=-4}[m_c1][mod_choices[0]]":
            $ ep11_nicole_over_lily = False
            mc "You're not wrong, but I'm not looking for something serious."
            mc "Maybe you are, but I'm happy as it is."
            scene ep11_pp_nl_event20 with dissolve
            nic "Ok... I must have read the signals wrong then. I thought we got along great together."
            scene ep11_pp_nl_event22 with dissolve
            mc "Oh, no. We do. But..."
            mc "I can't be a stepfather at 19."
            scene ep11_pp_nl_event23 with dissolve
            nic "I'm not asking you to be a stepfather. Marvin is my responsibility, not yours."
            nic "That would be the case even if we were in a relationship. Is that what's stopping you?"
            scene ep11_pp_nl_event22 with dissolve
            mc "It's a big reason, yeah."
            scene ep11_pp_nl_event20 with dissolve
            nic "Look... You go ahead and \"roll\" with Lily. If you're happy doing that, I think that's what you should do."
            scene ep11_pp_nl_event22 with dissolve
            mc "What about us? I like you a lot, Nicole."
            scene ep11_pp_nl_event23 with dissolve
            nic "I like you too. But I want to like you even more. And if this is all you can offer..."
            nic "[name], I'm not sure, but it feels better to call it quits before someone - a.k.a. me - gets hurt."
            jump ep11_pp_nl_event2_label
        "You're not wrong \n{size=-4}[m_c2][mod_choices[1]]":
            $ guideSuggestedPage = 204
            mc "No, you're not wrong. What I do with Lily isn't something you'd do when you're in a relationship."
            scene ep11_pp_nl_event21 with dissolve
            nic "Do you think you'll ever get serious with her?"
            scene ep11_pp_nl_event18 with dissolve
            mc "She would want me to say no, but truthfully, I don't know."
            scene ep11_pp_nl_event20 with dissolve
            nic "If Lily is concerned, I think I should be concerned too."
            nic "Maybe it's best if I back off?"
            scene ep11_pp_nl_event18 with dissolve
            mc "Why?"
            scene ep11_pp_nl_event21 with dissolve
            nic "I don't want to risk getting involved in some love triangle with you and my friend."
            scene ep11_pp_nl_event18 with dissolve
            
            if persistent.mod_wtenabled:
                        $mod_choices = ["(Lily path)","(Nicole path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not branchAlone:
                           $ mod_choices[6]="(+Cheater)"
                           $ mod_choices[7]="(+5 Cheater)"
            
            menu:
                "I'll stop rolling with her \n{size=-4}[m_c2][mod_choices[1]]":
                    $ ep11_nicole_over_lily = True
                    mc "If this is what it comes down to, I'll stop rolling with Lily."
                    mc "I can't promise you anything, but I want to continue dating you."
                    scene ep11_pp_nl_event20 with dissolve
                    nic "I feel bad for Lily."
                    scene ep11_pp_nl_event22 with dissolve
                    mc "She's the one who wanted the rolling to be devoid of emotions from the get-go. She'll be fine."
                    scene ep11_pp_nl_event25 with dissolve
                    nic "Then, it's settled."
                    nic "Thanks for telling me. I feel not many guys would."
                    scene ep11_pp_nl_event26 with dissolve
                    mc "You should thank Lily. She made me realize that I had to let you know."
                    $ new_bio("Envy", "I told Nicole I would stop rolling with Lily because I'd rather date her.")
                "That's fair \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep11_nicole_over_lily = False
                    mc "I see what you mean. That's fair..."
                    mc "I don't want to stop doing what I'm doing with Lily right now. But I like you a lot too."
                    scene ep11_pp_nl_event23 with dissolve
                    nic "I get it. But it's better to call it quits before someone - a.k.a. me - gets hurt."
                    label ep11_pp_nl_event2_label:
                    scene ep11_pp_nl_event24 with dissolve
                    mc "I'm sorry."
                    scene ep11_pp_nl_event23 with dissolve
                    nic "Me too. Thank you for being honest."
                    scene ep11_pp_nl_event24 with dissolve
                    mc "Thanks for taking it well."
                    scene ep11_pp_nl_event23 with dissolve
                    nic "What am I gonna do? Be mad that you feel different? It's how it is, [name]."
                    scene ep11_pp_nl_event27 with dissolve
                    $ renpy.pause()
                    $ new_bio("Envy", "I ended it with Nicole after discussing our relationship. We agreed it was fair to stop dating before she got hurt.")
                    $ task_list[7] = ""
                    $ updateTaskList()
                    jump endEvent
else:
    scene ep11_pp_nl_event28 with dissolve
    $ renpy.pause()

$ ep11_nicole_dating = True
scene ep11_pp_nl_event29b with dissolve
nic "So... When will I see you again?"
scene ep11_pp_nl_event30 with dissolve
mc "I'm right here."
scene ep11_pp_nl_event29 with dissolve
nic "You know what I meant."
scene ep11_pp_nl_event30 with dissolve
mc "December is a busy month for me."
scene ep11_pp_nl_event31 with dissolve
nic "Don't I know it. It's my turn to have Marvin over the holidays."
nic "Putting the pieces together in the life puzzle isn't always easy."
scene ep11_pp_nl_event32 with dissolve
mc "Let's try to fit something in, even if it's just a coffee break."
scene ep11_pp_nl_event33 with dissolve
nic "I'll try to call you more."
scene ep11_pp_nl_event32 with dissolve
mc "It's a start."
scene ep11_pp_nl_event34 with dissolve
nic "Brr... It's chilly... I'm done smoking."
scene ep11_pp_nl_event35 with dissolve
mc "Let's get you warm again."
scene ep11_pp_nl_event36 with dissolve
nic "*{i}Smack{/i}*"
scene ep11_pp_nl_event37 with dissolve
$ renpy.pause()
scene ep11_pp_nl_event38 with dissolve
$ renpy.pause()
scene ep11_pp_nl_event40 with dissolve
nic "Mmm... I don't know if it's the joint or alcohol, or neither...but that kiss tasted so good."
nic "It's rude of me to keep you away from the party like this."
scene ep11_pp_nl_event39 with dissolve
mc "It would be even more rude to let you freeze."
scene ep11_pp_nl_event41 with dissolve
$ renpy.pause()
$ new_bio("Envy", "Nicole told me she had been busy lately with her kid, but she wanted to find a way to see me more.")
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep11_becky_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep7_becky_lewd = True
    $ ep10_rolling = False
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track131.mp3"])
hide screen new_phone_screen
$ ep11_becky_lewd = 4

scene ep11_becky_lewd1 with dissolve
bc "That was a long minute... I'm waiting..."
scene ep11_becky_lewd2 with dissolve
mc "Yeah, I can see that."
scene ep11_becky_lewd3 with dissolve
bc "Hurry up, I'm horny."
scene ep11_becky_lewd2 with dissolve
mc "Can't you, like, suck my cock or something first? Let's get things going before we fuck."
scene ep11_becky_lewd3 with dissolve
bc "Don't tell me you're one of those guys who have problems getting hard."
scene ep11_becky_lewd2 with dissolve
if ep7_becky_lewd:
    mc "You know I don't."
else:
    mc "I definitely don't."
scene ep11_becky_lewd3 with dissolve
bc "Then come on over here. We don't need foreplay when the entire semester has been a long foreplay between us."
scene ep11_becky_lewd2 with dissolve
mc "It has?"
scene ep11_becky_lewd4 with dissolve
bc "Do you realize how lucky you are? Not everyone gets to fuck me."
scene ep11_becky_lewd5 with dissolve
if ep10_rolling:
    mc "(That's not what I heard.)"
else:
    mc "You don't say..."
bc "What are you doing?"
scene ep11_becky_lewd6 with dissolve
mc "I'm putting on a condom."
scene ep11_becky_lewd8 with dissolve
bc "You don't have to do that. Look at that poor rubber. That's gonna fall off."
scene ep11_becky_lewd6 with dissolve
mc "I'll stretch it some more and it won't."
play sound "sound_effects/season3/rubber.mp3"
scene ep11_becky_lewd7 with vpunch
"*{i}Frrrtt{/i}*"
mc "Fuck! It broke."
mc "$10 for this!? These condoms suck."
scene ep11_becky_lewd8 with dissolve
bc "Don't bother with it; I'm cool without one."
scene ep11_becky_lewd9 with dissolve
mc "Ok... What the hell?"
scene ep11_becky_lewd10 with dissolve
$ renpy.pause()
scene anim_becky_tease_ep11 with dissolve
bc "I can't wait to tell Christie about this."
mc "Can you not talk about your friends now?"
bc "Yeah, yeah. Sure!"
pause
scene ep11_becky_lewd11 with dissolve
bc "*{i}Moans{/i}* Damn! That's a big cock!"
scene ep11_becky_lewd12 with dissolve
bc "You're like two times as big as Jacob!"
scene ep11_becky_lewd13 with dissolve
mc "Can you also not talk about other guys now?"
scene ep11_becky_lewd14 with dissolve
bc "I was saying you have a big dick."
scene ep11_becky_lewd13 with dissolve
mc "Yeah, sure. It is big."
scene anim_becky_miss1_ep11 with dissolve
mc "Yeah... This feels good. You feel great, Becky."
bc "*{i}Moans{/i}*"
pause
scene anim_becky_miss2_ep11 with dissolve
mc "(She's a lot tighter than I thought she'd be.)"
pause
scene ep11_becky_lewd18 with dissolve
mc "How do you want to fuck?"
scene ep11_becky_lewd19 with dissolve
bc "What do you mean?"
scene ep11_becky_lewd18 with dissolve
mc "Like, in what position? I thought you said you were crazy in bed."
scene ep11_becky_lewd19 with dissolve
bc "Oh! I get what you mean. Pull it out."
scene ep11_becky_lewd20 with dissolve
bc "Ok! Put it back in."
scene ep11_becky_lewd21 with dissolve
mc "(This is how it's gonna be, huh? She expects me to do all the work.)"
scene ep11_becky_lewd22 with dissolve
bc "*{i}Moans{/i}*"
scene anim_becky_prone1_ep11 with dissolve
bc "Ok, fuck me."
mc "(Ok, she's not crazy in bed. She doesn't know what guys want at all.)"
mc "(Fuck it, I'll take what I can get with her. I can still have a good time even if she sucks in bed.)"
pause
scene anim_becky_prone2_ep11 with dissolve
mc "(At least I don't have to worry about making her cum now that I don't care.)"
pause

$ tmpInt = 0
label ep11_becky_lewd_loop_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_becky_miss1_ep11 with dissolve
        pause
        scene anim_becky_miss2_ep11 with dissolve
        pause
        jump ep11_becky_lewd_loop_label
    "Prone":
        $ tmpInt += 1
        scene anim_becky_prone1_ep11 with dissolve
        pause
        scene anim_becky_prone2_ep11 with dissolve
        pause
        jump ep11_becky_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene ep11_becky_lewd23 with dissolve
        mc "Ride me."
        scene ep11_becky_lewd24 with dissolve
        bc "Uh... What?"
        scene ep11_becky_lewd23 with dissolve
        mc "Sit on my cock and bounce up and down. It's not hard."
        scene ep11_becky_lewd24 with dissolve
        bc "What? Did you go soft again?"
        scene anim_becky_ride1_ep11 with dissolve
        mc "Just do this..."
        bc "*{i}Moans{/i}* Wow, you're crazy in bed too..."
        mc "Just...shut up."
        pause
        scene anim_becky_ride2_ep11 with dissolve
        bc "*{i}Moans{/i}*"
        pause
        jump ep11_becky_lewd_loop_label
    "Cum" if tmpInt > 0:
        mc "All right. I'm close to cumming."
        bc "Already?"
        menu:
            "On ass":
                scene anim_becky_prone1_ep11 with dissolve
                bc "Don't get it on me; I don't want to get sticky."
                scene ep11_becky_lewd25 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_becky_lewd25 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_becky_lewd25 at vpunch, cum2
                mc "Ahh!!!"
                bc "Hey!!!"
                scene ep11_becky_lewd26 with dissolve
                bc "Didn't you hear me say not on me?"
                mc "No, I must have zoned out."
                bc "Well...eww. Now I have to clean up."
            "On pussy":
                scene anim_becky_miss1_ep11 with dissolve
                bc "Don't get it on me; I don't want to get sticky."
                scene ep11_becky_lewd15 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_becky_lewd15 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep11_becky_lewd15 at vpunch, cum2
                mc "Ahh!!!"
                bc "Hey!!!"
                scene ep11_becky_lewd16 with dissolve
                bc "Didn't you hear me say not on me?"
                mc "No, I must have zoned out."
                scene ep11_becky_lewd17 with dissolve
                bc "Well...eww. Now I have to clean up."
            "Creampie":
                scene anim_becky_prone1_ep11 with dissolve
                bc "Don't get it on me; I don't want to get sticky."
                scene ep11_becky_lewd27 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_becky_lewd27 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_becky_lewd27 at vpunch, cum1
                mc "Ahh!!!"
                bc "Hey!!!"
                scene ep11_becky_lewd28 with dissolve
                bc "Didn't you hear me say not on me?"
                mc "Technically, it's in you, not on you."
                bc "Well...eww. Now I have to clean up."

scene ep11_becky_lewd29 with dissolve
bc "But I'm happy you came that much. I told you I was crazy in bed."
scene ep11_becky_lewd30 with dissolve
mc "*{i}Sigh{/i}*"
mc "(Dammit cock... I should never have listened to you.)"
$ renpy.end_replay()
$ persistent.ep11_lewd_becky = True
$ calcScenes()
$ task_list[5] = ""
$ updateTaskList()
$ new_bio("Becky", "I had sex with Becky...")
$ mphone_stats_add_girl_s3("becky","You had sex with Becky at the Christmas Panty party in episode 11.")
show screen new_phone_screen

scene ep11_becky_after_lewd1
show screen dance_filter_screen
with dissolve
mc "*{i}Sigh{/i}*"
scene ep11_becky_after_lewd2 with dissolve
jac "Bad night?"
scene ep11_becky_after_lewd3 with dissolve
mc "I just had sex with Becky."
scene ep11_becky_after_lewd2 with dissolve
jac "Oh no... How was it?"
scene ep11_becky_after_lewd3 with dissolve
mc "Eh... The saddest orgasm I ever had."
scene ep11_becky_after_lewd2 with dissolve
jac "Dead fish in the water?"
scene ep11_becky_after_lewd4 with dissolve
mc "She said she was crazy in bed. But the only thing she did that was crazy...was saying she was crazy in bed."
scene ep11_becky_after_lewd5 with dissolve
jac "Hahaha! Cheer up. At least you got laid."

scene ep11_becky_after_lewd6 with dissolve
if (minigames and pp_current_party_happiness[1] > 2) or (not minigames and pp_current_party_happiness[1] == 1):
    if (minigames and pp_happiness_icon[1] == 3 ) or (not minigames and pp_nm_dik_happiness[1] == 3):
        jac "Nice party, [name]. You've got talent."
    else:
        jac "Nice party, [name]. You're learning."
    scene ep11_becky_after_lewd7 with dissolve
    mc "Thanks. I did my best."
else:
    jac "This is a weird party."
    scene ep11_becky_after_lewd7 with dissolve
    mc "Very... I did my best with it."
mc "I'm not sure if it can be called a Christmas party with everything going on tonight."
scene ep11_becky_after_lewd6 with dissolve
jac "I don't celebrate it, so I wouldn't know."

scene ep11_becky_after_lewd8 with dissolve
jac "Man... To think... With all these hotties here, you decided to waste your load on Becky."
scene ep11_becky_after_lewd7 with dissolve
mc "I'll refill. I always have more than one in me."
scene ep11_becky_after_lewd8 with dissolve
jac "Sure, bro."
scene ep11_becky_after_lewd7 with dissolve
mc "How's it going for you?"
scene ep11_becky_after_lewd9 with dissolve
jac "I've got my sights on Clara."
scene ep11_becky_after_lewd10 with dissolve
mc "Her? Again? It's not the first time, right?"
scene ep11_becky_after_lewd9 with dissolve
jac "It's more like the fourth or so tonight. But who's counting?"
scene ep11_becky_after_lewd10 with dissolve
mc "Girlfriend potential?"
scene ep11_becky_after_lewd9 with dissolve
jac "We only talk when we're drunk. So... She's hot and all, but I don't know if she's got substance."
scene ep11_becky_after_lewd7 with dissolve
mc "Why don't you find out?"
scene ep11_becky_after_lewd8 with dissolve
jac "Because it's my dick who's talking now - I'm just horny."
scene ep11_becky_after_lewd7 with dissolve
mc "Oh... Well, the same thing happened to me with Becky. Take my advice, don't listen to him too much."
$ currentFreeRoamLabel = "ep11_diks_pp_tommy_label"
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

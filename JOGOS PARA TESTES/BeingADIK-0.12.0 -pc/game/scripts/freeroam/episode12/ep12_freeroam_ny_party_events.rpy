label ep12_freeroam_np_label:
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep12/licensed_music/track197.mp3", "music/ep12/licensed_music/track210.mp3", "music/ep12/licensed_music/track211.mp3", "music/ep12/licensed_music/track212.mp3", "music/ep12/licensed_music/track201.mp3","music/ep12/licensed_music/track203.mp3"])
if maya_shiny_dress:
    scene bg anim_party_introb_ep12 movie with dissolve
else:
    scene bg anim_party_intro_ep12 movie with dissolve
if persistent.seen_cutscene_ep12[2]:
    $ renpy.pause(93)
else:
    #$ _skipping = False
    $ renpy.pause(93, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep12[2] = True
show screen new_phone_screen
scene ep12_freeroam_np1 with dissolve
dw "This line, right here, goes from the balcony all the way to the end of the dance floor."
scene ep12_freeroam_np2 with dissolve
dw "It is what separates our parties. Got it?"
scene ep12_freeroam_np8 with dissolve
tm "You put up a line for this? Are you 12?"
scene ep12_freeroam_np3 with dissolve
dw "Fuck you! You stay on your side of the line, and we stay on ours."
scene ep12_freeroam_np4 with dissolve
an "What about the HOTs?"
scene ep12_freeroam_np5 with dissolve
dw "As long as DIKs stay on that end of the party, the HOTs and all other guests can walk freely across the line."
scene ep12_freeroam_np10 with dissolve
rs "Dawe, this line isn't necessary."
scene ep12_freeroam_np5 with dissolve
dw "Oh, it is! The line is the only reason we agreed to share the HOTs at this party."
dw "And it will keep you guys from fucking with us."
scene ep12_freeroam_np11 with dissolve
mc "*{i}Whispers{/i}*"
scene ep12_freeroam_np12 with dissolve
$ renpy.pause()
scene ep12_freeroam_np8 with dissolve
tm "And what happens if someone breaks these rules?"
scene ep12_freeroam_np3 with dissolve
dw "Oh, there will be consequences."
scene ep12_freeroam_np9 with dissolve
tm "Consequences it is."
scene ep12_freeroam_np6 with dissolve
$ renpy.pause()
scene ep12_freeroam_np13 with dissolve
tm "By the way, the bathroom is on our side of the party. Have fun pissing your pants."
play sound "sound_effects/season2/fistbump.mp3"
show ep12_freeroam_np14
if not persistent.ep12_cardcam17:
    show screen ep12_render_screen("cam17")
with hpunch
$ renpy.pause()
show ep12_freeroam_np7
hide screen ep12_render_screen
with dissolve
dw "Ant...?"
dw "Do we have any empty kegs?"
$ new_bio("Dawe", "Dawe wanted a visible line to separate DIKs from jocks at the New Year's Eve party.")
jump ep12_freeroam_party_label

label ep12_np_fem_label:
$ guideSuggestedPage = 259
scene ep12_np_fem1 with dissolve
li "I don't own a fucking dress!"
li "And you have no idea how hard it was to get into these jeans. You couldn't even relate because you're all skin and bones."
scene ep12_np_fem5 with dissolve
sar "Excuse me?"
scene ep12_np_fem1 with dissolve
li "It was either these clothes or I wouldn't come."
scene ep12_np_fem5 with dissolve
sar "What a shame that would have been."
scene ep12_np_fem2 with dissolve
li "Look! Dany isn't wearing a dress either!"
scene ep12_np_fem3 with dissolve
dn "Don't throw me under the bus."
scene ep12_np_fem4 with dissolve
dn "I'm wearing a suit. If it's fine for every guy in here to wear it, it's fine for me too."
scene ep12_np_fem6 with dissolve
sar "Like it or not. The party has a dress code, and you're violating it."
sar "Did you even check your invitations? Who invited you, by the way?"
scene ep12_np_fem4 with dissolve
dn "Hey, get off our case. Jamie invited us."
scene ep12_np_fem6 with dissolve
sar "Didn't you guys break up a while ago?"
scene ep12_np_fem4 with dissolve
dn "Jamie invited us before that."
scene ep12_np_fem7 with dissolve
menu:
    "Let Sarah handle it":
        scene ep12_np_fem8 with dissolve
        mc "(Eh... She'll manage.)"
        $ new_bio("Sarah", "I let Sarah handle the feminists showing up at the New Year's Eve party on her own.")
    "Help her out":
        scene ep12_np_fem9 with dissolve
        mc "Want me to handle it?"
        scene ep12_np_fem10 with dissolve
        sar "Puh-lease..."
        scene ep12_np_fem11 with dissolve
        mc "Alright, show me your invitations."
        scene ep12_np_fem12 with dissolve
        dn "We already told her, Jamie invited us."
        scene ep12_np_fem14 with dissolve
        mc "He didn't mention that to me."
        mc "And I can't find you on the seating plan..."
        scene ep12_np_fem11 with dissolve
        mc "Sorry. But we're full."
        scene ep12_np_fem15 with dissolve
        suz "Nuh-uh! It says that there are extra tables if we're not on the list."
        suz "Look! It says it right there."
        scene ep12_np_fem11 with dissolve
        mc "Oh, yeah... Now I see it."
        mc "But I can't have you girls break the party rules."
        scene ep12_np_fem12 with dissolve
        dn "Who are you calling a girl?"
        scene ep12_np_fem11 with dissolve
        mc "Look, the dress code says formal wear only..."
        mc "If I let this one slide, you will have to make sure you don't break any other rules, or I'll be in trouble."
        scene ep12_np_fem16 with dissolve
        suz "Yes! Yes! Anything. What's the rule?"
        scene ep12_np_fem18 with dissolve
        mc "I'm doing you a big favor here..."
        mc "Since you'll be dining in dining room B, you're going to have to stay on that side of the line for the entire party."
        mc "The line extends to the balcony and dance floor. Other than that, you're free to enjoy yourselves."
        scene ep12_np_fem13 with dissolve
        mc "Eat as much as you want, get as drunk as you possibly can, and go crazy! But stay on that side of the line, or we'll have to ask you to leave."
        scene ep12_np_fem16 with dissolve
        suz "We promise. Right everyone?"
        scene ep12_np_fem17 with dissolve
        dn "That's fair. I appreciate it. You are more welcoming than your co-host."
        scene ep12_np_fem19 with dissolve
        mc "Hey. Hey. It's all good. Welcome to the party."
        mc "Now what are you waiting for? Get over that line already."
        scene ep12_np_fem20 with dissolve
        $ renpy.pause()
        scene ep12_np_fem21 with dissolve
        sar "You're evil."
        scene ep12_np_fem22 with dissolve
        mc "Am I?"
        scene ep12_np_fem21 with dissolve
        sar "Yes. And I fucking love it."
        sar "Well... If only I weren't dining over there too."
        scene ep12_np_fem22 with dissolve
        mc "You're welcome to change tables, Sarah. We'd love to have you."
        scene ep12_np_fem23 with dissolve
        $ renpy.pause()
        $ new_bio("Sarah", "I helped Sarah handle the feminists showing up at the New Year's Eve party.")
if persistent.mod_wtenabled:
    $ task_list[7] = "Find Tiffani (Dance floor)"
else:
    $ task_list[7] = "Find Tiffani"
$ updateTaskList()
$ event_list.append("ep12_np_bct_label")
jump endEvent

label ep12_np_ca_label:
scene ep12_np_ca1 with dissolve
cb "Back up."
scene ep12_np_ca2 with dissolve
mc "You guys are taking this too seriously."
scene ep12_np_ca3 with dissolve
cb "Oh, yeah? Cross the line. See what happens."
scene ep12_np_ca2 with dissolve
mc "You're not gonna bait me into a fight tonight."
scene ep12_np_ca3 with dissolve
cb "Pussy."
jump endEvent

label ep12_np_rtb_label:
scene ep12_np_rtb1 with dissolve
mc "Hey! I didn't see you girls walk in. Welcome to the party."
scene ep12_np_rtb2 with dissolve
tan "[name]! Hi!!! Come over here!"
scene ep12_np_rtb3 with dissolve
mc "I...uh...can't."
scene ep12_np_rtb2 with dissolve
tan "What?"
scene ep12_np_rtb4 with dissolve
cb "Girls on this side of the line don't need to talk to you."
scene ep12_np_rtb5 with dissolve
mc "You're joking."
scene ep12_np_rtb4 with dissolve
cb "Does it look like I am?"
scene ep12_np_rtb5 with dissolve
if affinity == "DIK":
    mc "(Part of me thinks the line is good... But then there's that other part that wants to fuck with it.)"
else:
    mc "(Ugh... The line is good... But also annoying.)"
$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep12_np_nick_label:
scene ep12_np_nick1
hide screen dance_filter_screen
with dissolve
ni "Hey, [name]."
scene ep12_np_nick2 with dissolve
if ep11_nick_attitude > 2:
    mc "What the hell are you doing here?"
else:
    mc "I'm confused... Why are you here?"
scene ep12_np_nick1 with dissolve
ni "I'm invited."
scene ep12_np_nick2 with dissolve
if ep11_nick_attitude > 2:
    mc "The hell you are."
else:
    mc "I seriously doubt that."
scene ep12_np_nick3 with dissolve
mc "Huh?"
scene ep12_np_nick4 with dissolve
mc "Tommy. Do you know what this is about?"
scene ep12_np_nick5 with dissolve
$ renpy.pause()
scene ep12_np_nick6 with dissolve
$ renpy.pause()
scene ep12_np_nick7 with dissolve
mc "Who invited you?"
scene ep12_np_nick8 with dissolve
sa "I did."
if breakup or ep4_toldDerekAboutJade:
    scene ep12_np_nick10 with dissolve
else:
    scene ep12_np_nick9 with dissolve
mc "{b}You{/b} invited Nick?"
if breakup or ep4_toldDerekAboutJade:
    scene ep12_np_nick11 with dissolve
    sa "I'm free to invite whomever I want to our party."
else:
    scene ep12_np_nick12 with dissolve
    sa "I did."
scene ep12_np_nick9 with dissolve
mc "Why would you do that? Does Rusty know about this?"
scene ep12_np_nick13 with dissolve
ni "I'm right here, dude."
if ep11_nick_attitude > 2:
    scene ep12_np_nick14 with dissolve
    mc "I don't give a flying fuck."
    scene ep12_np_nick15 with dissolve
    sa "[name]. Knock it off."
    sa "Rusty knows Nick was invited. He wanted to give him another chance. You should follow his lead."
    scene ep12_np_nick16 with dissolve
    mc "The problem is, Rusty didn't tell Tommy or me about this."
    scene ep12_np_nick15 with dissolve
    sa "Tommy might not be cool with it, but he's aware Nick is here."
    sa "It's time to bury the hatchet. And not just for your guys' sake, it's for Heather and us too."
    if breakup or ep4_toldDerekAboutJade:
        scene ep12_np_nick17 with dissolve
        sa "Don't make this harder than it has to be."
    else:
        scene ep12_np_nick18 with dissolve
        sa "Please?"
else:
    scene ep12_np_nick15 with dissolve
    sa "Rusty knows Nick was invited. He wanted to give him another chance."
    scene ep12_np_nick14 with dissolve
    mc "Nick... Do you think this is a good idea? If you wanted to talk, you could have done it outside of the party."
    mc "You're not gonna have a good time here when you're unwanted."
    scene ep12_np_nick15 with dissolve
    sa "[name], it's time to bury the hatchet. And not just for your guys' sake, it's for Heather and us too."
    if breakup or ep4_toldDerekAboutJade:
        scene ep12_np_nick17 with dissolve
        sa "Don't make this harder than it has to be."
    else:
        scene ep12_np_nick18 with dissolve
        sa "Please?"
scene ep12_np_nick20 with dissolve
$ renpy.pause()
scene ep12_np_nick19 with dissolve
sa "Nick, come. Let me show you the party."

scene ep12_np_nick21 with dissolve
if ep11_nick_attitude > 2:
    mc "(What a shit idea... Is Rusty ok with this?)"
else:
    mc "(I don't know about this...)"

$ event_list.append("ep12_np_tm_label")

$ new_bio("Nick", "Nick showed up to our New Year's Eve party. Sage had invited him.")
$ new_bio("Sage", "Sage wanted us to bury the hatchet with Nick at our New Year's Eve party.")
if persistent.mod_wtenabled:
    $ task_list[6] = "Talk to Tommy (Dance floor)"
else:
    $ task_list[6] = "Talk to Tommy"
$ updateTaskList()
jump endEvent

label ep12_np_bj_label:
scene ep12_np_bj1 with dissolve
js "A chaperone? Why? It's not a high school party."
if breakup or ep4_toldDerekAboutJade:
    scene ep12_np_bj6 with dissolve
else:
    scene ep12_np_bj5 with dissolve
isa "Well... It's on campus grounds, and those were the negotiated terms."
isa "But not many were thrilled to work on New Year's Eve."
scene ep12_np_bj7 with dissolve
isa "As for me, it worked out well. I get to spend the evening with you girls."
scene ep12_np_bj2 with dissolve
js "Haha, so you get paid for doing this."
scene ep12_np_bj8 with dissolve
isa "Yes, but I'm here to ensure students are safe."
scene ep12_np_bj3 with dissolve
js "But what about the alcohol?"
scene ep12_np_bj7 with dissolve
isa "I'm not going to tell everyone in here not to drink because we know that's futile."
isa "And besides, many are 21. I cannot know who's not."
scene ep12_np_bj8 with dissolve
isa "My only concern is how my co-chaperone will handle it. She might not be as lenient as I am."
scene ep12_np_bj3 with dissolve
js "Sage said Jade was under control."
js "She'll do her job and all, but won't interfere unless it's absolutely needed."
scene ep12_np_bj8 with dissolve
isa "I suppose I should talk to her later on."
scene ep12_np_bj2 with dissolve
js "Yeah, you should. Want to have a drink with me, or do you have to stay sober?"
scene ep12_np_bj7 with dissolve
isa "My only obligation is to keep students safe. How can I do that without tasting what they are drinking?"
scene ep12_np_bj4 with dissolve
js "Haha! A drink it is."

$ event_list.append("ep12_np_bmc_label")
$ event_list.append("ep12_np_josy_label")
$ task_list[17] = ""
if persistent.mod_wtenabled:
    $ task_list[13] = "Find Josy (Dining room)"
    $ optional_task_list[5] = "Find Bella (Dance floor)"
else:
    $ task_list[13] = "Find Josy"
    $ optional_task_list[5] = "Find Bella"

$ updateTaskList()
jump endEvent

label ep12_np_he_label:
$ guideSuggestedPage = 261
scene ep12_np_he1 with dissolve
el "I love how everything came together. This venue was a great choice."
scene ep12_np_he3 with dissolve
he "Don't celebrate too early. There's a reason they put up that tape, and why we had to split the dining room into two."
scene ep12_np_he1 with dissolve
el "Don't you think they'll behave tonight?"
scene ep12_np_he3 with dissolve
he "Have you met them? I'm calling it. By 10 p.m., there will be at least one big fight."
scene ep12_np_he2 with dissolve
el "Blame it on the alcohol."
scene ep12_np_he4 with dissolve
he "I'll blame it on everyone who thought this party was a good idea to begin with."
scene ep12_np_he5 with dissolve
mc "10 p.m.? I'll take that bet."
scene ep12_np_he6 with dissolve
he "You don't think so?"
scene ep12_np_he7 with dissolve
menu:
    "No one will fight":
        $ ep12_eh_fight = False
        mc "Not with this line separating us. It may seem stupid and juvenile..."
        mc "...but it could work."
        mc "The problems usually happen when we interact with them."
        scene ep12_np_he8 with dissolve
        he "And how will an imaginary barrier prevent you from starting something?"
        scene ep12_np_he9 with dissolve
        mc "Oh, I'm sure they'll say shit to our faces, but I'm saying no one will fight."
        mc "At least none of the DIKs are looking to fight them."
        scene ep12_np_he8 with dissolve
        he "I don't think that goes both ways."
        scene ep12_np_he9 with dissolve
        mc "I've been to a party with the alphas before, and I didn't fight them."
        scene ep12_np_he10 with dissolve
        el "Exactly. It was our party, and [name] behaved."
        if ep7_alphas_leave:
            scene ep12_np_he11 with dissolve
            mc "Hm... Behave is a strong word..."
    "You're right":
        $ ep12_eh_fight = True
        mc "I think there will be a fight, but I think that's too early for it."
        scene ep12_np_he10 with dissolve
        el "Why are you two so negative?"
        scene ep12_np_he11 with dissolve
        mc "I've been to a party with the alphas before."
        scene ep12_np_he10 with dissolve
        el "Exactly. And you behaved, didn't you?"
if ep7_alphas_leave:
    scene ep12_np_he7 with dissolve
    mc "I made it my mission to make the alphas leave early, so..."
    scene ep12_np_he12 with dissolve
    el "What?"
    scene ep12_np_he7 with dissolve
    mc "For starters, I pushed Dawe into the pool, had a horny Arieth sic two of them, and I snitched on the dude who passed out in Heather's bed to Heather."
    scene ep12_np_he13 with dissolve
    he "Yeah, I remember that. It was Jimmy."
    if ep12_eh_fight:
        scene ep12_np_he10 with dissolve
        el "Aha, I see how it is. You know you will start a fight tonight, and that's why you're so negative."
        scene ep12_np_he11 with dissolve
        mc "I don't start things. I finish them."
        scene ep12_np_he10 with dissolve
        el "Listen here, macho man. I'll be on you like a hound tonight if I get a whiff of you starting or finishing anything."
    else:
        scene ep12_np_he11 with dissolve
        mc "What I'm saying is that there are ways to fuck with them without turning it into a fight."
        scene ep12_np_he10 with dissolve
        el "Listen here, fuck boy. I'll be on you like a hound tonight if I get a whiff of you starting anything."
    scene ep12_np_he16 with dissolve
    el "That goes for you, too."
    scene ep12_np_he17 with dissolve
    he "What would I even start?"
    scene ep12_np_he16 with dissolve
    el "Just be mindful."
else:
    scene ep12_np_he7 with dissolve
    mc "It took all my willpower, but I did."
    if ep12_eh_fight:
        scene ep12_np_he10 with dissolve
        el "See! That makes it possible for you to behave tonight, too."
        scene ep12_np_he7 with dissolve
        mc "It's not me you should worry about. It's the rest of my brothers."
        mc "Collectively... There's a chance something will happen."
        scene ep12_np_he15 with dissolve
        el "Then, I think the three of us should work together to prevent that from happening."
    else:
        scene ep12_np_he13 with dissolve
        he "You're such a saint."
        scene ep12_np_he14 with dissolve
        mc "Hah! I didn't say that. But I'm not getting into a fight tonight."
        scene ep12_np_he15 with dissolve
        el "I think the three of us should work together and keep everyone smoking peace pipes."
    scene ep12_np_he11 with dissolve
    mc "I've worked enough for tonight. Now, it's party time."
    scene ep12_np_he10 with dissolve
    el "Listen here, party boy. You're not letting me do all the heavy lifting with this one. I'm asking you as a friend."
    scene ep12_np_he11 with dissolve
    mc "Not as a friend..."
    scene ep12_np_he16 with dissolve
    el "That goes for you too."
    scene ep12_np_he17 with dissolve
    he "Oh, no... Please... Stop. Something like that?"
    scene ep12_np_he16 with dissolve
    el "Yes, but enthusiastic."
scene ep12_np_he17 with dissolve
he "Gotcha."
$ new_bio("Elena", "Elena was worried that the DIKs would end up fighting the jocks at the New Year's Eve party.")
$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep12_np_cal_label:
$ guideSuggestedPage = 261
scene ep12_np_cal1 with dissolve
le "*{i}Psst{/i}*"
le "See that group of girls over there."
scene ep12_np_cal2 with dissolve
mc "Yeah. That short-haired one in the middle is Avery. Tara told me about her."
le "The other two are Lisa and Celine. Have you met them?"
mc "No. I've never seen them before, I think."
scene ep12_np_cal1 with dissolve
le "They were with the rest of the girls when I busted Beth putting posters up."
scene ep12_np_cal2 with dissolve
mc "Ah. It's good to know their faces, then."
le "Jamie banged Celine, and Lisa was before our time... I think she was with Tommy."
le "Hell hath no fury like a woman scorned."
menu:
    "Will they be a problem?":
        mc "Do you think they'll start something tonight?"
        scene ep12_np_cal3 with dissolve
        le "Maybe. I wanted to put them on the ban list, but the jocks invited them."
        le "We made sure to seat them at their end of the party."
        scene ep12_np_cal4 with dissolve
        mc "So, that's why they're here."
        scene ep12_np_cal3 with dissolve
        le "Yeah, I doubt they came to party with us."
        scene ep12_np_cal4 with dissolve
        mc "Thanks for looking out."
        scene ep12_np_cal5 with dissolve
        le "Oh, you better believe it. I don't trust them one bit after what they did."
    "Don't let it get to you":
        mc "Don't let it get to you. We're here for the party."
        scene ep12_np_cal3 with dissolve
        le "That's easy to say, but harder to do."
        le "I think we let them off too easily. They should get expelled for what they did."
        scene ep12_np_cal4 with dissolve
        mc "You're right. But put it on the back burner for tonight."
        mc "Trust me. You'll enjoy the party more that way."
        scene ep12_np_cal5 with dissolve
        le "I'll try."
$ task_list[10] = ""
$ updateTaskList()
$ new_bio("Leon", "Leon was concerned that the dorm girls who put up posters of Cathy were at the New Year's Eve party.")
jump endEvent

label ep12_np_lmc_label:
$ guideSuggestedPage = 259
play sound "sound_effects/bottle_clink.mp3"
scene ep12_np_lmc1 with dissolve
le "Cheers!"
che "Hell yeah! Cheers!"
scene ep12_np_lmc2 with dissolve
mc "Drinking in the gent's room? That's pretty much the opposite of its purpose."
scene ep12_np_lmc3 with dissolve
che "Pssch! Everyone knows that real talk happens when you hold your genitals."
scene ep12_np_lmc4 with dissolve
mc "Is that right? What's the real talk about?"
scene ep12_np_lmc5 with dissolve
le "We got ourselves some potential spring pledgers."
scene ep12_np_lmc4 with dissolve
mc "These two? What were your names again?"
scene ep12_np_lmc6 with dissolve
if name == "Chen":
    che "Out of all people, how could YOU possibly forget!? It's Chen. And that's Marc."
else:
    che "Bro, I've told you like five times! It's Chen. And that's Marc."
scene ep12_np_lmc7 with dissolve
mc "I'm not entirely sure you can decide that you'll pledge just like that."
scene ep12_np_lmc8 with dissolve
che "Huh!? That's what Leon told me."
scene ep12_np_lmc9 with dissolve
le "Well... Marc and Chen, Jamie and I... We have some similarities. I figured it would work out."
scene ep12_np_lmc7 with dissolve
mc "I don't think we can decide that. Aren't new pledgers usually tested?"
scene ep12_np_lmc10 with dissolve
le "Yeah, of course."
scene ep12_np_lmc8 with dissolve
che "Tested? What fucking test?"
scene ep12_np_lmc7 with dissolve
mc "I believe you need to get us a pair of panties from the HOTs or something."
scene ep12_np_lmc8 with dissolve
che "What!? Leon? Is this guy for real?"
scene ep12_np_lmc10 with dissolve
le "Yeah, but that's Tommy's territory... I'm unsure what to do."
scene ep12_np_lmc7 with dissolve
mc "Maybe we could come up with our own tests."
scene ep12_np_lmc11 with dissolve
che "You fucking name it. Anything! Panties, boxers, buttplugs... Say the word; I'll bring all of it."
scene ep12_np_lmc7 with dissolve
mc "Hold on. I need a private word with my brother..."
scene ep12_np_lmc11 with dissolve
che "Totally."
scene ep12_np_lmc12 with dissolve
$ renpy.pause()
scene ep12_np_lmc13 with dissolve
mc "Are you gonna leave or...?"
scene ep12_np_lmc14 with dissolve
che "Yeah, yeah, yeah. Marc, let's go!"
scene ep12_np_lmc15 with dissolve
menu:
    "Haze them":
        $ ep12_chen_marc_toilet = True
        mc "Hold on. Where are you going?"
        scene ep12_np_lmc16 with dissolve
        che "You said-"
        scene ep12_np_lmc17 with dissolve
        mc "I know what I said. But you're not waiting out there."
        scene ep12_np_lmc18 with dissolve
        mc "Corner booth. Both of you."
        ma "Together? In there?"
        scene ep12_np_lmc17 with dissolve
        mc "Is this guy going to ask a lot of questions, Chang?"
        scene ep12_np_lmc16 with dissolve
        che "It's Chen! And no. No, he won't."
        play sound "sound_effects/shove.mp3"
        scene ep12_np_lmc19 with hpunch
        che "Don't fucking ruin this for us."
        scene ep12_np_lmc20 with dissolve
        ma "It's tight in here."
        play sound "sound_effects/zipper.mp3"
        che "WHOA! Hey! Why are you pulling down your pants? No one said anything about pulling down your pants."
        ma "I've been holding it in."
        che "Hold it longer, asswipe! Put that cock back!"
        play sound "sound_effects/season2/pour.mp3"
        che "NO! Don't start pissing!"
    "Be nice":
        $ ep12_chen_marc_toilet = False
        mc "It will just be a minute."
scene ep12_np_lmc21 with dissolve
le "What are you thinking?"
scene ep12_np_lmc23 with dissolve
mc "They seem like cool guys and all. They helped out with the dorm girls and have been at our parties before..."
scene ep12_np_lmc22 with dissolve
le "I sense a but."
scene ep12_np_lmc23 with dissolve
mc "Can we decide they can pledge just like that?"
scene ep12_np_lmc22 with dissolve
le "Someone has to decide it. Why not us?"
le "And besides, pledging isn't the same as being accepted. They still need to go through the process like everyone else."
scene ep12_np_lmc23 with dissolve
mc "Alright. You're right about that."
scene ep12_np_lmc21 with dissolve
le "So, what do you want to do?"
scene ep12_np_lmc24 with dissolve
mc "I don't think we should promise them anything. No one promised us we'd get accepted, yeah?"
scene ep12_np_lmc25 with dissolve
le "Are you kidding? Tommy called me and Jamie gay pussies when we wanted to apply."
le "To get treated like crap is all part of the hazing."
scene ep12_np_lmc26 with dissolve
mc "Then we should haze them too, yeah?"
scene ep12_np_lmc27 with dissolve
le "With the panties?"
scene ep12_np_lmc26 with dissolve
mc "Yeah, but also, we can come up with something of our own."
scene ep12_np_lmc28 with dissolve
le "Haha... I like that. What do you have in mind?"
scene ep12_np_lmc26 with dissolve
mc "Let's spitball some ideas."
scene ep12_np_lmc28 with dissolve
le "We could do it at the party. It would make it more entertaining."
scene ep12_np_lmc26 with dissolve
mc "And we'd all get to watch them do it. That's good..."
mc "And better yet, they aren't bound to the same rules we are."
scene ep12_np_lmc27 with dissolve
le "What rules?"
scene ep12_np_lmc26 with dissolve
mc "I'm talking about the yellow tape that splits this party into two."
mc "They can cross over it freely."
scene ep12_np_lmc29 with dissolve
le "They can fuck with the alphas for us!"
scene ep12_np_lmc26 with dissolve
mc "And we wouldn't get any backlash because the alphas don't know they will pledge the DIKs."
scene ep12_np_lmc27 with dissolve
le "It depends on the prank."
scene ep12_np_lmc26 with dissolve
menu:
    "Mean prank":
        $ ep12_mean_prank = True
        mc "It has to be a mean one. Think about all the shit we had to do."
        scene ep12_np_lmc27 with dissolve
        le "How about they do something to their drinks?"
        scene ep12_np_lmc26 with dissolve
        mc "Hmm... It needs to be something that doesn't affect everyone else on their side of the party."
        scene ep12_np_lmc27 with dissolve
        le "Yeah, you're right..."
        scene ep12_np_lmc26 with dissolve
        mc "Hey... We have the seating plan out there. We know where everyone will sit."
        scene ep12_np_lmc29 with dissolve
        le "Yeah! Let's have them shove the jocks' forks up their assholes!"
        scene ep12_np_lmc26 with dissolve
        mc "Is that where your mind went?"
        scene ep12_np_lmc27 with dissolve
        le "Didn't yours?"
        scene ep12_np_lmc26 with dissolve
        mc "No... I thought about licking their glasses or something."
        mc "But fuck it, let's do yours."
        scene ep12_np_lmc31 with dissolve
        le "Haha! Not mine. Ours."
    "Harmless prank":
        $ ep12_mean_prank = False
        mc "It can't be too mean. Just in case the jocks would trace it back to us."
        scene ep12_np_lmc25 with dissolve
        le "You're right... Good call. Um... Non-mean pranks, on the other hand..."
        le "Do those exist?"
        scene ep12_np_lmc26 with dissolve
        mc "Maybe we could have them leave fake notes for the jocks."
        scene ep12_np_lmc27 with dissolve
        le "They can pretend they're chicks who wanna hook up with them or something."
        scene ep12_np_lmc26 with dissolve
        mc "Oh! Yeah. Let's leave a note to one of them, telling him to meet up somewhere at midnight to make out."
        scene ep12_np_lmc29 with dissolve
        le "I've got one better! Leave that same note to two of them. And by midnight, they'll show up and meet each other."
        scene ep12_np_lmc30 with dissolve
        mc "Hahaha! They're gonna think the other one sent it."
        scene ep12_np_lmc29 with dissolve
        le "That's perfect! But how can Marc and Chen pull that off?"
        scene ep12_np_lmc26 with dissolve
        mc "That's their problem... But..."
        mc "There's a seating plan in the corridor. They can leave the notes on the plates for the jocks of their choosing."
        scene ep12_np_lmc28 with dissolve
        le "Now we're cooking."

if ep12_chen_marc_toilet:
    scene ep12_np_lmc20 with dissolve
    che "Hello!? Did you guys leave or?"

scene ep12_np_lmc26 with dissolve
mc "Got this one? I need to take a leak."

if ep12_chen_marc_toilet:
    scene ep12_np_lmc32 with dissolve
    le "You're free to come out."
    scene ep12_np_lmc34 with dissolve
else:
    scene ep12_np_lmc33 with dissolve
    le "Hey, guys! Get back in here."
    scene ep12_np_lmc35 with dissolve
che "So, what will it be?"

$ task_list[0] = ""
$ updateTaskList()

$ tmpInt = 0
python:
    for x in range(0,len(mphone_bios_chars_list)):
        if mphone_bios_chars_list[x][0] == "Chad":
            tmpInt = x + 1
$ mphone_bios_chars_list.insert(tmpInt,["Chen",[2],bios_txt_chen,mbios_history_chen,0])
$ tmpInt = 0
python:
    for x in range(0,len(mphone_bios_chars_list)):
        if mphone_bios_chars_list[x][0] == "Magnar":
            tmpInt = x + 1
$ mphone_bios_chars_list.insert(tmpInt,["Marc",[2],bios_txt_marc,mbios_history_marc,0])

if ep12_mean_prank:
    $ new_bio("Leon", "Leon and I hazed Marc and Chen by making them pull a mean prank on the alphas.")
    $ new_bio("Chen", "Leon and I hazed Marc and Chen by making them pull a mean prank on the alphas.")
    $ new_bio("Marc", "Leon and I hazed Marc and Chen by making them pull a mean prank on the alphas.")
else:
    $ new_bio("Leon", "Leon and I hazed Marc and Chen by making them pull a harmless prank on the alphas.")
    $ new_bio("Chen", "Leon and I hazed Marc and Chen by making them pull a harmless prank on the alphas.")
    $ new_bio("Marc", "Leon and I hazed Marc and Chen by making them pull a harmless prank on the alphas.")
jump endEvent

label ep12_np_rj_label:
scene ep12_np_rj1 with dissolve
rs "Great job with the plating, Mel."
rs "How are things going at your end of the party?"
scene ep12_np_rj2 with dissolve
ml "Why do you care? It's not like that's your problem."
scene ep12_np_rj1 with dissolve
rs "I want every guest to have a nice experience, regardless of whether they eat with us or the jocks."
scene ep12_np_rj3 with dissolve
mc "Rusty? Do you need an extra set of hands?"
scene ep12_np_rj4 with dissolve
rs "Didn't I tell you to relax and enjoy the party for once?"
scene ep12_np_rj3 with dissolve
mc "I always enjoy myself, but it doesn't sit right not to help out."
scene ep12_np_rj5 with dissolve
rs "You did your part already. But..."
scene ep12_np_rj3 with dissolve
mc "Name it."
scene ep12_np_rj4 with dissolve
rs "If you don't mind... We keep the cold beer in the second-floor storage room."
rs "Can you get some for the drink table?"
scene ep12_np_rj3 with dissolve
mc "Say less."
$ event_list.append("ep12_np_storage_locked_label")
$ task_list[3] = "Get beer from the storage room"
$ updateTaskList()
jump endEvent

label ep12_np_storage_locked_label:
play sound "sound_effects/door_lock.mp3"
scene ep12_np_storage1 with dissolve
mc "(It's locked... I don't have a key.)"
mc "(I'll have to ask Rusty about it.)"
$ event_list.append("ep12_np_rkey_label")
if persistent.mod_wtenabled: 
    $ task_list[4] = "Ask Rusty for the key (Dining room)"
else:
    $ task_list[4] = "Ask Rusty for the key"
$ updateTaskList()
jump endEvent

label ep12_np_rkey_label:
scene ep12_np_rj3 with dissolve
mc "It would make my job a lot easier if you gave me the key to the storage room."
scene ep12_np_rj5 with dissolve
rs "Oh, it's locked? I was unaware."
rs "Uh... Check with Sage or a chaperone. I don't have the key on me."
if "sage_gone" in event_list:
    $ event_list.append("ep12_np_jkey_label")
    if persistent.mod_wtenabled: 
        $ task_list[4] = "Ask Jade for the key (Dining room)"
    else:
        $ task_list[4] = "Ask Jade for the key"
else:
    $ event_list.append("ep12_np_skey_label")
    if persistent.mod_wtenabled: 
        $ task_list[4] = "Ask Sage for the key (Dance floor)"
    else:
        $ task_list[4] = "Ask Sage for the key"
$ updateTaskList()
jump endEvent

label ep12_np_ja_label:
scene ep12_np_ja1 with dissolve
$ renpy.pause()
if branchZoey and not wt_ep11_zoey_kiss_others:
    scene ep12_np_ja2 with dissolve
    mc "(I have to tell her about Zoey... But it's not the ideal place for it.)"
else:
    scene bg anim_jade_pan_ep12 movie with dissolve
    mc "(Fuck... She looks sexy tonight...)"
    scene ep12_np_ja3 with dissolve
    $ renpy.pause()
$ optional_task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_np_jkey_label:
$ currentFreeRoamLabel = "ep12_np_storage_label"
scene ep12_np_jkey1 with dissolve
mc "Jade?"
mc "Do you have the key to the storage room? I need to prepare the drink table."
scene ep12_np_jkey2 with dissolve
ja "I don't have it on me; it's in my purse. Can't you ask my daughter? She's supposed to have a copy."
scene ep12_np_jkey3 with dissolve
mc "I tried, but...um... We've not been on speaking terms lately."
scene ep12_np_jkey2 with dissolve
ja "*{i}Sigh{/i}* Follow me."
scene ep12_np_jkey4 with dissolve
ja "Will that be all?"
scene ep12_np_jkey5 with dissolve
mc "I think so, yeah. Thanks."
scene ep12_np_jkey6 with dissolve
ja "So, my daughter doesn't want to talk to you anymore?"
scene ep12_np_jkey7 with dissolve
if "Sage" in breakup:
    mc "Not since we broke up."
else:
    mc "Not since she found out about us, no."
if ep12_break_or_tell == "break" and not ep4_toldDerekAboutJade:
    scene ep12_np_jkey6 with dissolve
    ja "And why was that?"
    scene ep12_np_jkey7 with dissolve
    mc "Are you kidding? You know why."
    mc "The guilt made me do it..."
    scene ep12_np_jkey8 with dissolve
    $ renpy.pause()
    scene ep12_np_jkey9 with dissolve
    label ep12_np_jkey2_label:
    ja "Did you...tell her anything?"
    scene ep12_np_jkey8 with dissolve
    mc "No. I decided not to tell her the reason."
    mc "It was enough for me to ruin my relationship with her. I didn't want to ruin yours too."
    scene ep12_np_jkey10 with dissolve
    mc "I made a mistake, doing what I did with you. But Sage shouldn't have to suffer because of it."
    scene ep12_np_jkey9 with dissolve
    ja "She's heartbroken. She is suffering."
    scene ep12_np_jkey8 with dissolve
    mc "*{i}Snorts{/i}* Thanks for the consolation."
    scene ep12_np_jkey11 with dissolve
    ja "I wish it were different. But you did the right thing."
    scene ep12_np_jkey10 with dissolve
    mc "After doing wrong things."
    scene ep12_np_jkey9 with dissolve
    ja "Does your conscience feel lighter?"
    scene ep12_np_jkey8 with dissolve
    mc "It's too early to tell. It felt like crap breaking up with her."
    mc "My feelings haven't been sorted yet. I don't know what's what."
    scene ep12_np_jkey11 with dissolve
    ja "I'm sorry, [name]. It was my fault."
    scene ep12_np_jkey8 with dissolve
    mc "Don't say that. You didn't force yourself on me."
    scene ep12_np_jkey10 with dissolve
    mc "I know you're going through things with your divorce right now..."
    mc "But please be more present for Sage."
    label ep12_np_jkey3_label:
    scene ep12_np_jkey12 with dissolve
    mc "It's likely she hasn't told you, but she wants you to be there for her."
    mc "She wants you to talk to her about your feelings and ask her about hers. But she's unsure how to reach you."
    scene ep12_np_jkey13 with dissolve
    ja "How to reach me? I'm always there for her."
    scene ep12_np_jkey12 with dissolve
    mc "That's not how she sees it. You get angry and shut down conversations."
    mc "That's why she feels like she can't talk to you."
    mc "I think she needs it."
    mc "Now probably more than ever."
    scene ep12_np_jkey10 with dissolve
    ja "..."
    scene ep12_np_jkey14 with dissolve
    ja "Point taken."
    scene ep12_np_jkey10 with dissolve
    mc "Good."
elif ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
    mc "What about you?"
    scene ep12_np_jkey6 with dissolve
    ja "She's been talking to me plenty. I've gotten earfuls."
    ja "It's been a mix of accusations, curse words, and hate."
    scene ep12_np_jkey7 with dissolve
    mc "I'm sorry..."
    scene ep12_np_jkey6 with dissolve
    ja "*{i}Snorts{/i}*"
    ja "I don't think she'll ever trust me again. She doesn't even believe me when I tell her the truth."
    scene ep12_np_jkey8 with dissolve
    mc "It's because you withheld it."
    scene ep12_np_jkey9 with dissolve
    ja "That, and she believes I don't care about how it affected her. Which I do."
    ja "She doesn't understand that I was heartbroken too. Married and heartbroken at the same time..."
    ja "It's not easy to explain that to someone who's not living it."
    scene ep12_np_jkey11 with dissolve
    ja "And when I try to explain it, it gets mistaken. She thinks I feel pitiful, but all I wanted her to know was how we got to this point."
    scene ep12_np_jkey8 with dissolve
    mc "Sage is... She's very emotional. And her emotions tend to come out as anger at first."
    mc "But I've found that beneath all that anger there's often insecurity."
    scene ep12_np_jkey10 with dissolve
    mc "When she feels insecure, she gets mad. It's like a self-defense mechanism."
    scene ep12_np_jkey11 with dissolve
    ja "It sounds like she's my daughter after all..."
    scene ep12_np_jkey10 with dissolve
    mc "Yeah..."
    mc "I know you're going through a hard time, but if you could do me a favor..."
    mc "Please, be more present for Sage."
    jump ep12_np_jkey3_label
else:
    scene ep12_np_jkey6 with dissolve
    ja "And why was that?"
    scene ep12_np_jkey7 with dissolve
    mc "Because I'm in love with someone else."
    if jade_state > 0:
        scene ep12_np_jkey9 with dissolve
        ja "I wasn't sure if it was because of something else..."
        jump ep12_np_jkey2_label
    else:
        mc "I wish I could have let her down easy, but I fucked up."
        scene ep12_np_jkey9 with dissolve
        ja "She's heartbroken."
        scene ep12_np_jkey8 with dissolve
        mc "Thanks... I know. I don't blame her for not wanting to talk to me."
        mc "But if you could do me a favor..."
        mc "Please, be more present for Sage."
        jump ep12_np_jkey3_label
scene ep12_np_jkey15 with dissolve
ja "Will you need the key more tonight?"
scene ep12_np_jkey16 with dissolve
mc "Probably."
scene ep12_np_jkey15 with dissolve
ja "I don't want to fetch my purse every time you do. Return it to me at the end of the party."
scene ep12_np_jkey17 with dissolve
mc "Thank you."
$ event_list.append("key")
$ task_list[4] = ""
$ updateTaskList()
if "Sage" in breakup:
    $ new_bio("Jade", "I talked to Jade about my breakup with Sage.")
else:
    $ new_bio("Jade", "I talked to Jade about my situation with Sage.")
jump endEvent

label ep12_np_beer_label:
scene ep12_np_beer1 with dissolve
mc "(There's the cold beer. Time for some heavy lifting...)"
play sound "sound_effects/bottle_clink.mp3"
scene ep12_np_beer2 with dissolve
$ renpy.pause()
$ event_list.append("ep12_np_btable_label")
$ task_list[3] = "Serve beer in dining room"
$ updateTaskList()
jump endEvent

label ep12_np_btable_label:
play sound "sound_effects/bottle_clink.mp3"
scene ep12_np_btable1 with dissolve
mc "(Let there be cold beer...)"
$ task_list[3] = ""
$ updateTaskList()
$ event_list.append("table")
jump endEvent

label ep12_np_jj_label:
scene ep12_np_jj1 with dissolve
mc "How's it going guys?"
scene ep12_np_jj2 with dissolve
jac "I'm breaking a sweat here. But at least we're done carrying food and drinks."
jac "This should be the last of it all."
scene ep12_np_jj3 with dissolve
jy "Hey, those fireworks are ours."

scene ep12_np_jj4 with dissolve
if ep12_pp_fireworks != 2:
    jm "How can you be sure? We bought fireworks too."
    scene ep12_np_jj5 with dissolve
    jac "I already carried ours. It's theirs."
    scene ep12_np_jj7 with dissolve
    mc "Did you set the fireworks up?"
    scene ep12_np_jj8 with dissolve
    jac "Nah. Jamie and I will do it before midnight."
    scene ep12_np_jj7 with dissolve
    mc "Need any help with it?"
    scene ep12_np_jj8 with dissolve
    jac "Funny you should ask..."
    jac "Derek volunteered to help out, but I told him he needed the rest of his nine fingers."
    scene ep12_np_jj7 with dissolve
    mc "Haha! Yeah. Don't let him anywhere near those fireworks."
    scene ep12_np_jj9 with dissolve
    jac "He'd end up shooting fireworks from his ass or something."
    scene ep12_np_jj7 with dissolve
    mc "And don't tell him that idea either."
else:
    jm "I know, we didn't get any."
    scene ep12_np_jj3 with dissolve
    jy "You guys didn't buy any fireworks? Are you fucking broke or what?"
    scene ep12_np_jj6 with dissolve
    jac "We knew you'd get it, so we'll leech on yours."
    scene ep12_np_jj14 with dissolve
    jo "Dawe won't stand for that. He's gonna force you to chip in."
    scene ep12_np_jj15 with dissolve
    mc "Good luck with that. We already paid our part, and no one forced you guys to buy fireworks."

scene ep12_np_jj8 with dissolve
jac "How are things inside?"
scene ep12_np_jj7 with dissolve
mc "They are under control."
scene ep12_np_jj10 with dissolve
jm "Have all the girls shown yet?"
scene ep12_np_jj11 with dissolve
mc "Many came."
scene ep12_np_jj10 with dissolve
jm "Oh, man. How do they look?"
scene ep12_np_jj11 with dissolve
mc "It's a gorgeous mix of girls in there."
if "ep12_np_fem_label" not in event_list:
    if affinity == "DIK":
        mc "Except for the cows you invited."
    else:
        mc "Except for the ones you invited."
    scene ep12_np_jj12 with dissolve
    jm "Fuck! I forgot I invited Dany and her friends..."
    scene ep12_np_jj13 with dissolve
    mc "Not cool, bro."
scene ep12_np_jj7 with dissolve
mc "See you guys at dinner."
scene ep12_np_jj8 with dissolve
jac "Yeah. We're almost done here."
$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep12_np_om_label:
$ guideSuggestedPage = 261
if ep9_told_jill:
    scene ep12_np_om1 with dissolve
    mc "(Who invited them to the party?)"
    mc "(I wonder how Bianca and Jill feel about it.)"
    scene ep12_np_om2 with dissolve
    mc "(Hm... They look happy together.)"
    mc "(That's good for them, I guess.)"
    scene ep12_np_om3 with dissolve
    mat "Hey, [name]! Great party!"
    scene ep12_np_om6 with dissolve
    mc "Yeah. I'm surprised to see you two here."
    scene ep12_np_om7 with dissolve
    mat "*{i}Sigh{/i}* Yeah, I get it. We're trying to make amends."
    scene ep12_np_om8 with dissolve
    mc "Yeah? How's that going for you?"
    scene ep12_np_om7 with dissolve
    mat "It's easier with some than others."
    scene ep12_np_om9 with dissolve
    mat "I have to tell you, I was so pissed at you for telling Bianca about us."
    scene ep12_np_om8 with dissolve
    mc "You had yourself to blame for making out at our party like that."
    scene ep12_np_om7 with dissolve
    mat "Let me finish."
    mat "It wasn't your fault. We deserved it."
    scene ep12_np_om9 with dissolve
    mat "The truth is, Liv and I have been in love for what feels like ages."
    mat "For the longest time, we didn't know the other one felt the same. But as we realized it, there was no going back."
    scene ep12_np_om10 with dissolve
    mat "It was an awful way to do it. Behind our partners' backs and all..."
    mat "But ultimately, I have to thank you."
    scene ep12_np_om11 with dissolve
    mc "Thank me?"
    scene ep12_np_om10 with dissolve
    mat "If it weren't for you, I'd still be with Bianca, and Liv would be with Andy."
    mat "I don't think either of us would have pulled the trigger and told them how we felt. Right, Liv?"
    scene ep12_np_om12 with dissolve
    oli "Yeah, it was a big change, and those are scary."
    scene ep12_np_om10 with dissolve
    mat "So, anyway, that's what I wanted to tell you."
    mat "Thank you for setting us straight. We're much happier today because of you."
    scene ep12_np_om11 with dissolve
    menu:
        "What about Bianca and Andy?":
            mc "And what about Bianca and Andy? Do you think they are happier today, too?"
            scene ep12_np_om7 with dissolve
            mat "They have to be better off without us. It might have looked different from the outside, but we were in unhappy relationships."
            scene ep12_np_om8 with dissolve
            mc "Yeah. But they'll have to live with you guys betraying them."
            if tc > 4:
                mc "That's a scar that... *{i}Sigh{/i}*"
                scene ep12_np_om15 with dissolve
                mc "Don't be this happy about how you did it. Show some respect."
            else:
                mc "That's a scar that won't go away."
                scene ep12_np_om14 with dissolve
                mc "I don't think you should be this happy about it all."
        "Congratulate them":
            mc "Congratulations, then."
            scene ep12_np_om10 with dissolve
            mat "Thanks!"
            scene ep12_np_om11 with dissolve
            menu:
                "Leave it there":
                    scene ep12_np_om10 with dissolve
                    mat "Again... Great party, [name]."
                    scene ep12_np_om11 with dissolve
                    mc "Awesome... Enjoy."
                    $ task_list[11] = ""
                    $ updateTaskList()
                    $ new_bio("Bianca", "Matthew thanked me for outing his relationship with Olivia to Bianca. I didn't pick a fight with him over it.")
                    jump endEvent
                "Make it sarcastic":
                    scene ep12_np_om13 with dissolve
                    mc "Congratulations on your affair that hurt Bianca and Andy!"
                    if tc > 4:
                        mc "I'm happy that your betrayal... *{i}Sigh{/i}*"
                        scene ep12_np_om15 with dissolve
                        mc "Don't be this happy about how you did it. Show some respect."
                    else:
                        scene ep12_np_om14 with dissolve
                        mc "I'm happy that your betrayal only gave two people permanent scars."
                    scene ep12_np_om9 with dissolve
                    mat "Come on..."
    scene ep12_np_om13 with dissolve
    mc "You both did horrible things. And I'm surprised anyone would want to bury that hatchet."
    mc "I, for one, don't want to hear anything about it. To me, you're unwelcome here."
    scene ep12_np_om16 with dissolve
    $ renpy.pause()
    $ new_bio("Bianca", "Matthew thanked me for outing his relationship with Olivia to Bianca. I gave him an earful.")
else:
    scene ep12_np_om1 with dissolve
    mc "(Who invited them to the party?)"
    scene ep12_np_om2 with dissolve
    mc "(Hm... It looks like they're still sneaking around with each other.)"
    if ep12_bianca_lewd:
        mc "(Maybe Bianca deserves to know that.)"
    scene ep12_np_om4 with dissolve
    mat "Hey, [name]...uh... Great party!"
    scene ep12_np_om5 with dissolve
    menu:
        "Leave":
            scene ep12_np_om17 with dissolve
            $ renpy.pause()
        "Confront them":
            mc "Are you two kidding me? Again with this?"
            scene ep12_np_om4 with dissolve
            mat "Uh... Wha-?"
            scene ep12_np_om18 with dissolve
            mc "\"Uh. Uh. Whaaa?\""
            scene ep12_np_om6 with dissolve
            mc "Seriously... Aren't you sick of sneaking around like this?"
            mc "I think an explanation to your partners is long overdue."
            scene ep12_np_om19 with dissolve
            mat "Stay out of our business. You don't know what you saw."
            scene ep12_np_om20 with dissolve
            mc "I saw you two kiss at Halloween. I know that."
            scene ep12_np_om19 with dissolve
            mat "No, you didn't. You're mistaken."
            scene ep12_np_om21 with dissolve
            mc "The web camera in Rusty's room would back me up."
            scene ep12_np_om22 with dissolve
            mat "There was a camera in there?"
            mat "Fuck..."
            scene ep12_np_om21 with dissolve
            mc "No, there wasn't. You're a shit liar. I'm surprised you've lasted this long."
            scene ep12_np_om19 with dissolve
            mat "What do you want from us?"
            scene ep12_np_om20 with dissolve
            mc "What do you think?"
            scene ep12_np_om19 with dissolve
            mat "Money? Is that it?"
            scene ep12_np_om20 with dissolve
            mc "Wow... You really are clueless."
            if tc > 4 and not persistent.no_cheater:
                scene ep12_np_om15 with dissolve
                mc "Both of you should be ashamed of yourselves for... *{i}Sigh{/i}*"
            else:
                scene ep12_np_om14 with dissolve
                mc "Both of you should be ashamed of yourselves for doing what you're doing to your partners."
            scene ep12_np_om13 with dissolve
            mc "To me, you're unwelcome here. Stop acting like we're friends."
            scene ep12_np_om16 with dissolve
            $ renpy.pause()
            $ new_bio("Bianca", "I gave Matthew an earful for sneaking around with Olivia at the New Year's Eve party.")
$ task_list[11] = ""
$ updateTaskList()
jump endEvent

label ep12_np_mia_label:
$ guideSuggestedPage = 261
scene ep12_np_mia1 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Check them out \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep12_np_mia2 with dissolve
        $ renpy.pause()
        scene ep12_np_mia3 with dissolve
        $ renpy.pause()
        scene ep12_np_mia4 with dissolve
        $ renpy.pause()
        scene ep12_np_mia5 with dissolve
        $ renpy.pause()
        scene ep12_np_mia6 with dissolve
        $ renpy.pause()
    "Leave \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
jump endEvent

label ep12_np_skey_label:
if breakup or ep4_toldDerekAboutJade:
    scene ep12_np_skey1 with dissolve
    mc "Sage? Do you have the key for the storage room?"
    if "Sage" in breakup or ep4_toldDerekAboutJade:
        scene ep12_np_skey15 with dissolve
        mc "(Alright... Maybe Bella or Jade has a copy of it.)"
        $ event_list.append("ep12_np_jkey_label")
        if persistent.mod_wtenabled: 
            $ task_list[4] = "Ask Jade for the key (Dining room)"
        else:
            $ task_list[4] = "Ask Jade for the key"
    else:
        scene ep12_np_skey3 with dissolve
        sa "What do you need it for?"
        scene ep12_np_skey6 with dissolve
        mc "I need to carry cases of beer to the dining room. And we'll need to do it more than once tonight."
        scene ep12_np_skey9 with dissolve
        $ renpy.pause()
        scene ep12_np_skey10 with dissolve
        sa "Here. Can you be responsible for the key?"
        scene ep12_np_skey12 with dissolve
        mc "Yeah, you can trust me with it. Thanks."
        scene ep12_np_skey13 with dissolve
        $ renpy.pause()
        $ event_list.append("key")
        $ task_list[4] = ""
else:
    scene ep12_np_skey2 with dissolve
    mc "Sage? Do you have the key for the storage room?"
    scene ep12_np_skey4 with dissolve
    sa "I do. We can't have everyone walking about in there."
    scene ep12_np_skey5 with dissolve
    mc "Can I borrow it?"
    scene ep12_np_skey7 with dissolve
    sa "The key is supposed to be my responsibility."
    scene ep12_np_skey5 with dissolve
    mc "I need to carry cases of beer to the dining room. And we'll need to do it more than once tonight."
    scene ep12_np_skey4 with dissolve
    sa "Oh... It's easier if you have the key then."
    sa "But, seriously, don't lose it."
    scene ep12_np_skey5 with dissolve
    mc "I won't lose it. I have a pocket for it."
    mc "I think you're more likely to lose it. Where do you even keep it?"
    scene ep12_np_skey8 with dissolve
    $ renpy.pause()
    scene ep12_np_skey11 with dissolve
    mc "Yeah... I'd better take full responsibility for this one."
    scene ep12_np_skey14 with dissolve
    $ renpy.pause()
    $ event_list.append("key")
    $ task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep12_np_tm_label:
scene ep12_np_tm1 with dissolve
mc "Hey."
scene ep12_np_tm2 with dissolve
tm "Looking good, [name]."
scene ep12_np_tm3 with dissolve
mc "Thanks again for the shirt."
scene ep12_np_tm5 with dissolve
tm "I seriously can't believe you didn't own a plain white shirt."
scene ep12_np_tm3 with dissolve
mc "I never had a use for one. I'm not big on fashion; I only buy casual clothes and things that look good."
scene ep12_np_tm5 with dissolve
tm "That doesn't explain your camouflage shirts."
scene ep12_np_tm4 with dissolve
mc "What's wrong with camouflage patterns?"
scene ep12_np_tm6 with dissolve
tm "Nothing. If you want to hide in a bush."
tm "I'm telling you, your wardrobe could use a set of basic clothes. Then I won't have to save you at the eleventh hour."
scene ep12_np_tm3 with dissolve
mc "And what are basic clothes?"
scene ep12_np_tm5 with dissolve
tm "You don't even know? Fine, I'll teach you, but not tonight."
tm "I've heard enough talk about clothes as it is."
scene ep12_np_tm3 with dissolve
mc "Tonight?"
scene ep12_np_tm7 with dissolve
tm "Dude, turn the volume up. Can't you hear every girl talk about how good they all look?"
scene ep12_np_tm8 with dissolve
mc "I don't think I've noticed."
scene ep12_np_tm7 with dissolve
tm "Trust me. They are blowing smoke up each other's asses. Every conversation out there right now goes like this..."
scene ep12_np_tm19 with dissolve
tm "\"Oh, Christie... That silver dress is so shiny and sparkly.\""
scene ep12_np_tm20 with dissolve
tm "\"Oh, thank you! I bought it specially for tonight's party. I looked everywhere to find something my size.\""
tm "\"After the holidays, the stores are all out of the petite sizes.\""
scene ep12_np_tm19 with dissolve
tm "\"Oh, but you found the most amazing dress, and that size is perfect!\""
tm "\"That dress accentuates your perky, and totally-not-fake tits.\""
scene ep12_np_tm3 with dissolve
mc "How do you know they are fake?"
scene ep12_np_tm5 with dissolve
tm "I've banged her. Trust me; they are fake."
scene ep12_np_tm21 with dissolve
mc "Oh, look! Becky..."
mc "\"Hi, girls! Have you seen my dress? It's cut down to my huge belly button. It's not one of the oversized, leftover dresses Christie mentioned.\""
tm "Haha! Yes!"
scene ep12_np_tm9 with dissolve
tm "Man, Becky is such a fucking drag."
scene ep12_np_tm10 with dissolve
mc "She is."
scene ep12_np_tm9 with dissolve
tm "Yeah, I hate that she looks hot in her dress tonight."
scene ep12_np_tm10 with dissolve
mc "Careful. You're starting to sound like them."
scene ep12_np_tm22 with dissolve
tm "Look who else is here tonight."
if ep11_kp_choice == "DIK":
    tm "You're not gonna throw them out naked from this one, yeah?"
    mc "They deserved it."
    tm "I don't know about that. I've done some mean shit, but I wouldn't have done that."
    scene ep12_np_tm10 with dissolve
    mc "Right. You only do that to guys who fetch you panties."
    scene ep12_np_tm5 with dissolve
    tm "Haha! Dudes get over that sort of thing easier than girls."
    scene ep12_np_tm10 with dissolve
    mc "It depends on the person. But I don't regret teaching them a lesson."
    mc "So... Nick's here tonight too."
    scene ep12_np_tm9 with dissolve
    tm "Mhm."
elif ep11_kp_choice == "NEUTRAL":
    tm "I heard they were thrown out of our party."
    mc "Jacob and Leon dealt with them as they saw fit."
    tm "It was effective. They've been giving me the stink eye."
    scene ep12_np_tm10 with dissolve
    mc "I assume they're not our guests tonight."
    scene ep12_np_tm9 with dissolve
    tm "Fuck 'em."
    scene ep12_np_tm10 with dissolve
    mc "And what about Nick?"
    scene ep12_np_tm9 with dissolve
    tm "Fuck him too."
else:
    tm "I heard you made them apologize."
    mc "That's a half-truth. I didn't make them do it. Penny apologized after I talked to them, but Kylie wouldn't."
    mc "I hoped that Penny would talk some sense into Kylie, but I don't know if she has."
    tm "Kylie isn't over it. I can tell."
    scene ep12_np_tm10 with dissolve
    mc "How so?"
    scene ep12_np_tm9 with dissolve
    tm "She's given me some cold glances."
    scene ep12_np_tm11 with dissolve
    mc "Maybe that's a you problem? You're not sunshine and rainbows when looked at from a distance."
    scene ep12_np_tm12 with dissolve
    tm "Hahaha!"
    scene ep12_np_tm10 with dissolve
    mc "So... Nick's here tonight too."
    scene ep12_np_tm9 with dissolve
    tm "Mhm."
tm "With this many people who don't like each other, all together in a room, it's a wonder this party even happened."
scene ep12_np_tm13 with dissolve
mc "Will you talk to him tonight?"
scene ep12_np_tm14 with dissolve
tm "Nah. Rusty is the one who wanted him here. Nick is his problem."
scene ep12_np_tm13 with dissolve
mc "Sage and Heather wanted Nick here, too."
scene ep12_np_tm14 with dissolve
tm "It's pathetic."
scene ep12_np_tm13 with dissolve
mc "What is?"
scene ep12_np_tm14 with dissolve
tm "That they expect us to get along again."
tm "He did unforgivable levels of shit. I'm allowed to hate him after that."
scene ep12_np_tm15 with dissolve
tm "Putting us together in a room won't solve the issues."
tm "He can't unfuck Heather, can he?"
if ep9_heather_lewd == 2:
    scene ep12_np_tm13 with dissolve
    mc "I can't undo what I did either... Yet here we stand laughing and talking to each other."
    scene ep12_np_tm15 with dissolve
    tm "Yeah, but... It's different."
scene ep12_np_tm13 with dissolve
mc "Is this really about what he did with Heather?"
scene ep12_np_tm14 with dissolve
tm "He lashed out at all of us. That's when he truly lost me."
tm "Nick was with us from the start. He helped form the DIKs."
scene ep12_np_tm15 with dissolve
tm "And then he threw everyone under the bus."
scene ep12_np_tm13 with dissolve
if ep11_nick_attitude > 2:
    mc "I'm with you... The only thing I'll say in his defense is that he didn't do it publicly. He kept it between brothers."
else:
    mc "In his defense, he didn't do it publicly. He kept it between brothers."
mc "At least, I hope he did..."
scene ep12_np_tm15 with dissolve
tm "What's your point? Brothers fight?"
scene ep12_np_tm13 with dissolve
mc "I don't know if I have a point. I've been trying to see more than one side to this..."
mc "All I know is that I'm tired of being upset and angry."
scene ep12_np_tm16 with dissolve
$ renpy.pause()
scene ep12_np_tm17 with dissolve
tm "Not the worst argument I've heard."
tm "Give me a few more of these, and maybe I'll change my mind."
play sound "sound_effects/bottle_clink.mp3"
scene ep12_np_tm18 with dissolve
$ renpy.pause()

if breakup or ep4_toldDerekAboutJade:
    $ event_list.append("ep12_np_bujill_label")
    if persistent.mod_wtenabled: 
        $ task_list[12] = "Talk to Jill (Dance floor)"
    else:
        $ task_list[12] = "Talk to Jill"
if not breakup and branchJill:
    $ event_list.append("ep12_np_jill_label")
    if persistent.mod_wtenabled: 
        $ task_list[12] = "Talk to Jill (Dance floor)"
    else:
        $ task_list[12] = "Talk to Jill"
$ event_list.append("ep12_np_zmc_label")
if persistent.mod_wtenabled: 
    $ task_list[13] = "Find Zoey (Dining room)"
else:
    $ task_list[13] = "Find Zoey"

if branchSage and not breakup:
    $ event_list.append("ep12_np_smc_label")
    if persistent.mod_wtenabled: 
        $ task_list[6] = "Talk to Sage (Dance floor)"
    else:
        $ task_list[6] = "Talk to Sage"
elif breakup or ep4_toldDerekAboutJade:
    $ event_list.append("ep12_np_s2mc_label")
    if persistent.mod_wtenabled: 
        $ task_list[6] = "Talk to Sage (Dance floor)"
    else:
        $ task_list[6] = "Talk to Sage"
elif not branchJill:
    $ event_list.append("ep12_np_s3mc_label")
    if persistent.mod_wtenabled: 
        $ task_list[6] = "Talk to Sage (Dance floor)"
    else:
        $ task_list[6] = "Talk to Sage"
else:
    $ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np_nikita_label:
scene ep12_np_nikita1 with dissolve
$ renpy.pause()
scene ep12_np_nikita2 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/party_horn.mp3"
scene ep12_np_nikita3 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season3/party_horn.mp3"
scene ep12_np_nikita4 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season3/party_horn.mp3"
scene ep12_np_nikita5 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season3/party_horn.mp3"
scene ep12_np_nikita4 with hpunch
$ renpy.pause()
scene ep12_np_nikita6 with dissolve
$ renpy.pause()
scene ep12_np_nikita7 with dissolve
$ renpy.pause()
$ optional_task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep12_np_dj_label:
if mphone_music_genre != 2:
    $ mphone_music_genre = 2
    $ mphone_next_song()
if ep12_dj_return:
    $ ep12_dj_return = False
    scene ep12_np_dj2 with dissolve
    mc "(We're back, baby! No one can keep DJ [roosterNickMCCustom] off the dials!)"
$ dj_reset()
scene ep12_np_dj1
call screen ep12_dj_screen
with dissolve
pause

label ep12_np_dj_interrupted_label:
$ ep12_dj_return = True
$ ep12_dj_interrupted = 2
$ currentFreeRoamLabel = "ep12_np_party_room_dj_label"
if breakup:
    jump ep12_np_dj_interrupted2_label
else:
    if branchMayaJosy:
        if maya_shiny_dress:
            scene ep12_np_dj3 with dissolve
        else:
            scene ep12_np_dj3b with dissolve
        my "[name]... Come, I want to show you something."
        if maya_shiny_dress:
            scene ep12_np_dj4 with dissolve
        else:
            scene ep12_np_dj4b with dissolve
        mc "Not now, Maya. I'm having the time of my life."
        if maya_shiny_dress:
            scene ep12_np_dj3 with dissolve
        else:
            scene ep12_np_dj3b with dissolve
        my "I have a feeling it's not mutual for the poor people on the dance floor."
        my "Come."
    elif branchSage:
        scene ep12_np_dj6 with dissolve
        sa "[name]. You stink."
        scene ep12_np_dj7 with dissolve
        mc "Sorry, I don't take requests."
        scene ep12_np_dj5 with dissolve
        sa "Get off the console. It sounds horrible!"
    elif branchIsabella:
        scene ep12_np_dj8 with dissolve
        isa "I'm torn."
        scene ep12_np_dj9 with dissolve
        mc "Huh? What do you mean?"
        scene ep12_np_dj8 with dissolve
        isa "I'm torn between my role as a chaperone and our relationship, whether to let you mash buttons like a toddler or to kick you out of the party."
        scene ep12_np_dj9 with dissolve
        mc "Does it sound that bad?"
        scene ep12_np_dj8 with dissolve
        isa "I tried my best not to offend you, but I'd rather jam pencils in my ears than keep listening to it."
        isa "Off the console you go."
    elif branchJill:
        scene ep12_np_dj10 with dissolve
        ji "[name]?"
        scene ep12_np_dj11 with dissolve
        mc "Yeah?"
        scene ep12_np_dj10 with dissolve
        ji "You know I enjoy your music and think you're talented on the guitar..."
        scene ep12_np_dj11 with dissolve
        mc "Yeah?"
        scene ep12_np_dj12 with dissolve
        ji "But maybe your skills don't translate well to DJing."
        scene ep12_np_dj11 with dissolve
        mc "I think I sound good."
        scene ep12_np_dj10 with dissolve
        ji "I'll try that again."
        ji "Your skills don't translate well to DJing."
        scene ep12_np_dj13 with dissolve
        mc "*{i}Sigh{/i}*"
    else:
        label ep12_np_dj_interrupted2_label:
        scene ep12_np_dj14 with dissolve
        el "Looks like someone had too much to drink."
        scene ep12_np_dj15 with dissolve
        mc "Hey! I'm not done up here."
        scene ep12_np_dj14 with dissolve
        el "That's what I feared."

jump ep12_np_dj2_label

label ep12_np_dj2_label:
$ event_list.append("ep12_np_dj_label")
jump endEvent

label ep12_np_tara_label:
scene ep12_np_tara1 with dissolve
mc "You look stunning tonight, Tara."
scene ep12_np_tara2 with dissolve
ta "Everyone does! You included."
scene ep12_np_tara1 with dissolve
mc "However, your outfit doesn't beat what you wore for the last party."
scene ep12_np_tara2 with dissolve
ta "Haha, you would say that."
scene ep12_np_tara5 with dissolve
osc "Tara. Come over here."
scene ep12_np_tara6 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        


menu:
    "She's busy \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "She's busy."
    "Your boyfriend needs you":
        scene ep12_np_tara3 with dissolve
        mc "Sounds like your boyfriend needs you."
        scene ep12_np_tara4 with dissolve
        ta "No, we're not back together, but-"
scene ep12_np_tara7 with dissolve
osc "What the hell, man?"
scene ep12_np_tara10 with dissolve
ta "Oscar, don't start something."
scene ep12_np_tara8 with dissolve
mc "Listen to her."
scene ep12_np_tara7 with dissolve
if ep9_josy_choice == "DIK":
    osc "Or what? Are you gonna punch me again?"
    scene ep12_np_tara8 with dissolve
    mc "If you start calling girls bitches to their faces again, I will."
    scene ep12_np_tara11 with dissolve
    ta "Is that what happened? You told me it was out of the blue."
elif ep9_josy_choice == "NEUTRAL":
    osc "Or what? Are you gonna throw me out of this party, too?"
    scene ep12_np_tara8 with dissolve
    mc "If you start calling girls bitches to their faces again, I will."
    scene ep12_np_tara11 with dissolve
    ta "Is that what happened? You told me it was out of the blue."
else:
    osc "Or what?"
scene ep12_np_tara13 with dissolve
mc "I thought you were done with this guy."
scene ep12_np_tara14 with dissolve
ta "It's complicated. He asked me if I was going to the party, and when I said I was, he wanted to come together."
scene ep12_np_tara7 with dissolve
osc "The only one who's done here is you."
scene ep12_np_tara10 with dissolve
ta "Oscar!"
ta "I think both of you need to walk it off or something."
scene ep12_np_tara13 with dissolve
mc "It's cool. I just wanted to catch up with you and thank you for the last party."
scene ep12_np_tara9 with dissolve
osc "Don't tell me you hooked up with him."

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Let Tara handle it":
        scene ep12_np_tara10 with dissolve
        ta "Who are you to speak? You've done things with almost every girl at this party."
        scene ep12_np_tara9 with dissolve
        osc "That's both uncalled for and untrue."
        scene ep12_np_tara13 with dissolve
        mc "I would never do that to you, Tara."
        scene ep12_np_tara7 with dissolve
        osc "Oh, shut up!"
    "Tease him \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep12_np_tara8 with dissolve
        mc "Don't blame her for trying the plus-size menu."
        scene ep12_np_tara7 with dissolve
        osc "Oh, shut up!"
scene ep12_np_tara13 with dissolve
mc "You deserve better, Tara. Have a great night."
scene ep12_np_tara12 with dissolve
ta "Why do you have to be that way?"
scene ep12_np_tara9 with dissolve
osc "He's such an asshole."
scene ep12_np_tara12 with dissolve
ta "No, he's not! He stood up for me when no one else did."
ta "When did you ever do that?"
scene ep12_np_tara9 with dissolve
osc "*{i}Snorts{/i}*"
$ new_bio("Tara", "Oscar was salty that I had hooked up with Tara.")
$ optional_task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np_bct_label:
scene ep12_np_bct1 with dissolve
bc "Giiiirls! Who's the target tonight?"
scene ep12_np_bct9 with dissolve
ti "Target for what?"
scene ep12_np_bct1 with dissolve
bc "The midnight kiss. Don't tell me you don't have a plan for it."
bc "Standing alone at midnight with no one to kiss in front of everyone is pathetic."
scene ep12_np_bct15 with dissolve
chr "Ugh... I haven't even thought about that yet. I was too busy figuring out what to wear."
scene ep12_np_bct14 with dissolve
ti "You look amazing."
scene ep12_np_bct16 with dissolve
chr "You think? Can you believe they were out of my size? I had to buy one size plus and ask Mom to sew it."
scene ep12_np_bct3 with dissolve
bc "Hello!? Snap back to it, Christie. Who are you two aiming for?"
bc "I don't want to stand there at a quarter to midnight and realize we're going for the same guy."
scene ep12_np_bct9 with dissolve
ti "I don't think I'll kiss someone. It's not that big of a deal to me."
scene ep12_np_bct2 with dissolve
bc "What? Didn't you hear me say it's pathetic?"
scene ep12_np_bct15 with dissolve
chr "Maybe I'll check out one of the tri-alphas... I'm kind of tired of the DIKs."
scene ep12_np_bct10 with dissolve
ti "If you're into big, bulky muscles, go for it."
ti "I like them tall and toned."
scene ep12_np_bct1 with dissolve
bc "Like who?"
scene ep12_np_bct10 with dissolve
ti "Like [name]. He's got the perfect body."
scene ep12_np_bct5 with dissolve
if ep11_becky_lewd == 4:
    bc "Oh, I can attest to that! We fucked at the last party."
    scene ep12_np_bct15 with dissolve
    chr "You've been bragging about that too much. It's not a big deal. He's a DIK; who hasn't he screwed?"
    scene ep12_np_bct4 with dissolve
    bc "Not you."
    scene ep12_np_bct1 with dissolve
    bc "The sex was fire! We did so many kinky things."
    bc "But I had to teach him a thing or two about it."
elif ep11_becky_lewd > 0:
    bc "Totes. But he's playing hard to get. And I hate how that makes me want him even more."
    scene ep12_np_bct15 with dissolve
    chr "Give it a rest. You sound obsessed."
    scene ep12_np_bct4 with dissolve
    bc "Excuse me for having goals in life. I bet you couldn't fuck him either."
else:
    bc "Totes. I'd do him in a heartbeat."
    scene ep12_np_bct15 with dissolve
    chr "Again with [name]? Let it go. You sound obsessed."
    scene ep12_np_bct4 with dissolve
    bc "Excuse me for having goals in life. I bet he wouldn't fuck you either."

if ep11_tiffani_lewd:
    if ep11_becky_lewd == 4:
        scene ep12_np_bct11 with dissolve
        ti "You had sex with him at their Christmas party? I did him, too."
        scene ep12_np_bct6 with dissolve
        bc "No way!?"
        bc "We should have done him together. That would have made us BFFs!"
    else:
        scene ep12_np_bct12 with dissolve
        ti "I can tell you for a fact that he's great in bed."
        scene ep12_np_bct13 with dissolve
        ti "Wait... I can't say that."
        scene ep12_np_bct16 with dissolve
        chr "Did he ask you not to tell anyone about it?"
        scene ep12_np_bct12 with dissolve
        ti "No. It's because we technically didn't fuck in a bed. We did it in the bathroom."
        ti "And holy... It's even bigger in person than in those pictures."
        scene ep12_np_bct7 with dissolve
        bc "Lucky..."
elif ep9_tiffani_lick:
    scene ep12_np_bct10 with dissolve
    ti "I wouldn't say no to him. He did some naughty stuff to me at their Halloween party."
    scene ep12_np_bct5 with dissolve
    bc "Naughty how?"
    scene ep12_np_bct12 with dissolve
    ti "Remember that shot game?"
    scene ep12_np_bct8 with dissolve
    bc "Ugh. How can I forget having Derek's nasty ass in my face?"
    scene ep12_np_bct12 with dissolve
    ti "Let's just say I had my ass in his face, and he took advantage of that."
    scene ep12_np_bct7 with dissolve
    bc "No way! You're so lucky!"
else:
    scene ep12_np_bct10 with dissolve
    ti "I wouldn't say no to him."
    if ep9_tiffani_gina_tara:
        ti "But I don't think he's interested in me."
        ti "I slept half-naked next to him at Halloween, and he didn't even try something."

scene ep12_np_bct1 with dissolve
bc "I call dibs on him for the midnight kiss."
scene ep12_np_bct15 with dissolve
chr "You gotta ask him about that first."
scene ep12_np_bct3 with dissolve
bc "I know! But you two have to respect the dibs."
scene ep12_np_bct15 with dissolve
chr "I'm not even interested."
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep12_np_mcc_label:
scene ep12_np_mcc1 with dissolve
mc "Hey, Chad. Having a good time?"
scene ep12_np_mcc2 with dissolve
ch "Fuck off."
scene ep12_np_mcc3 with dissolve
mc "What?"
scene ep12_np_mcc2 with dissolve
ch "You heard me."
scene ep12_np_mcc3 with dissolve
mc "I understand you have to keep appearances up, but come on."
scene ep12_np_mcc4 with dissolve
mc "(What the hell?)"
mc "(Was someone watching us or what?)"
$ task_list[15] = ""
$ updateTaskList()
$ new_bio("Chad", "Chad told me to fuck off without reason at the New Year's Eve party.")
jump endEvent

label ep12_np_cam_label:
$ guideSuggestedPage = 260
scene ep12_np_cam1 with dissolve
$ renpy.pause()
scene ep12_np_cam2 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "You're gorgeous \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Holy... Camila, you're gorgeous."
        scene ep12_np_cam3 with dissolve
        cam "Haha! Don't I know it!"
        cam "You look great, too!"
        scene ep12_np_cam4 with dissolve
        mc "Oh, please. There's no comparison."
    "I barely recognized you \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Wow, I barely recognized you. Nice getup."
        scene ep12_np_cam3 with dissolve
        cam "Aw, come on! Do I usually look THAT unattractive?"
        scene ep12_np_cam4 with dissolve
        mc "That's not what I meant. You look great!"
scene ep12_np_cam6 with dissolve
cam "I bought the dress this summer, and I saved it for a special occasion."
scene ep12_np_cam4 with dissolve
mc "Don't hide that dress. Wear it again!"
scene ep12_np_cam3 with dissolve
cam "If it survives the night, I will. It's delicate and hard to get in and out of."
scene ep12_np_cam4 with dissolve
mc "Better dance carefully, then. It would suck if it ripped."
scene ep12_np_cam5 with dissolve
cam "It so would. I'm not wearing any underwear."
scene ep12_np_cam7 with dissolve
mc "I'd say that's TMI, but I can tell."
scene ep12_np_cam8 with dissolve
mc "Hey, if it does rip, I'll lend you my underwear. But I doubt the dress will have the same effect with boxers underneath."
scene ep12_np_cam3 with dissolve
cam "Hahaha! Let's hope it doesn't come to that."
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep12_np_dwa_label:
scene ep12_np_dwa2 with dissolve
$ renpy.pause()
scene ep12_np_dwa1 with dissolve
$ renpy.pause()
scene ep12_np_dwa3 with dissolve
dw "Don't be sad about Ashley. You breaking up with her was the best news I had this year."
scene ep12_np_dwa4 with dissolve
an "The best? It was the worst for me."
an "I miss her so much."
scene ep12_np_dwa5 with dissolve
dw "Fuck her! Look at this from the bright side!"
dw "It's you and me now! Like it always was."
dw "I have my brother back, and I couldn't be happier!"
scene ep12_np_dwa4 with dissolve
an "Do you think she'll get together with Derek now?"
scene ep12_np_dwa3 with dissolve
dw "Who knows? These hoes are never loyal."
dw "Arieth has cheated on me so many times that I lost count."
dw "That's why we shouldn't be loyal to girls either."
scene ep12_np_dwa6 with dissolve
an "So, you've cheated on Ari, too?"
scene ep12_np_dwa7 with dissolve
dw "I've tried, but it's slim pickins out there."
dw "You'd think girls dressed like this would be into sex, but trust me, they're not."
scene ep12_np_dwa6 with dissolve
an "The only holes I'm interested in belong to Ashley."
scene ep12_np_dwa8 with dissolve
dw "Stop being romantic. It creeps me out."
dw "You know what? You're getting laid tonight! And so am I."
scene ep12_np_dwa6 with dissolve
an "I don't know, Dawe. I don't think I can do it."
scene ep12_np_dwa7 with dissolve
dw "Let's make a pact for it."
scene ep12_np_dwa6 with dissolve
an "A pact to get laid?"
scene ep12_np_dwa9 with dissolve
dw "Yes! We both have to get laid before the night is over."
scene ep12_np_dwa10 with dissolve
an "What if we don't?"
scene ep12_np_dwa9 with dissolve
dw "Failure is not an option."
scene ep12_np_dwa10 with dissolve
an "That's easy for you to say. You have a girlfriend."
scene ep12_np_dwa9 with dissolve
dw "Don't worry. I'll help you."
dw "We have to find someone who'd do you."
scene ep12_np_dwa11 with dissolve
dw "Oh! What about that one - with the great ass?"
scene ep12_np_dwa12 with dissolve
an "That's Ashley."
scene ep12_np_dwa13 with dissolve
dw "It is? Man... I didn't see her from behind. She's looking fine tonight."
scene ep12_np_dwa14 with dissolve
$ renpy.pause()
jump endEvent

label ep12_np_bianca_label:
if ep12_bianca_lewd:
    scene ep12_np_bianca1 with dissolve
    bia "Hi."
    scene ep12_np_bianca2 with dissolve
    mc "Bianca... You look amazing tonight."
    scene ep12_np_bianca9 with dissolve
    if ep9_told_jill:
        bia "Be careful with what you say..."
    else:
        bia "A word of warning... Matthew is around here somewhere."
        scene ep12_np_bianca10 with dissolve
        if branchJill:
            mc "And Jill."
        else:
            mc "And Bella. I want to be respectful, even though we're not together anymore."
    scene ep12_np_bianca11 with dissolve
    mc "But you and I are friends, so..."
    scene ep12_np_bianca12 with dissolve
    bia "Sure. We can still talk, but don't look too flirty while doing it."
    scene ep12_np_bianca11 with dissolve
    mc "I look flirty when I talk to you?"
    scene ep12_np_bianca12 with dissolve
    bia "You're doing it now. Stop it. You know how I get around you."
    scene ep12_np_bianca11 with dissolve
    mc "I've been thinking about you a lot."
    scene ep12_np_bianca13 with dissolve
    bia "Mhm..."
    scene ep12_np_bianca14 with dissolve
    mc "Have you thought about me?"
    scene ep12_np_bianca15 with dissolve
    bia "Daily. Nightly. Non-stop."
    scene ep12_np_bianca14 with dissolve
    mc "Good... I was worried you thought it was a mistake."
    scene ep12_np_bianca15 with dissolve
    bia "If {b}I{/b} thought that? I was sure you'd call me to say you regretted it."
    scene ep12_np_bianca14 with dissolve
    mc "I didn't regret it, but I've felt remorseful for other reasons."
    scene ep12_np_bianca16 with dissolve
    bia "You don't have to say it. I know what you mean."
    bia "But we're just going to have to live with those feelings."
    scene ep12_np_bianca17 with dissolve
    if branchJill and not "Jill" in breakup and wt_ep9_branch_numbers == 1:
        mc "Hm... No, not me. I figured I'd talk to you before I did what I'm about to do."
        scene ep12_np_bianca18 with dissolve
        bia "Meaning?"
        scene ep12_np_bianca17 with dissolve
        mc "I haven't been myself around Jill lately. I'm going to break up with her."
        scene ep12_np_bianca20 with dissolve
        bia "Oh, wow... I don't know how I feel about that."
        scene ep12_np_bianca17 with dissolve
        mc "I don't want to keep doing bad things behind her back, and I'm not cut out for a relationship with her."
    else:
        mc "As I see it... Whatever happens between us, I don't think Jill will be ok with what we did."
        mc "If she learned the full story, that is..."

    scene ep12_np_bianca18 with dissolve
    if branchJill and not "Jill" in breakup and wt_ep9_branch_numbers == 1:
        bia "What will you tell her?"
    else:
        bia "What would you tell her?"
    scene ep12_np_bianca17 with dissolve
    if branchJill and not "Jill" in breakup and wt_ep9_branch_numbers == 1:
        mc "I don't intend to ruin your friendship with Jill, if that's what you're worried about. But I'll tell her some of the truth."
    else:
        mc "I don't intend to ruin your friendship with Jill, if that's what you're worried about."
    scene ep12_np_bianca22 with dissolve
    bia "*{i}Sigh{/i}*"
    bia "That puts it all on my conscience."
    scene ep12_np_bianca17 with dissolve
    mc "It doesn't."
    scene ep12_np_bianca18 with dissolve
    bia "If we came clean to Jill..."
    if not ep9_told_jill:
        bia "That would end my relationship with Matthew and her."
    else:
        bia "That would end my relationship with her."
    scene ep12_np_bianca17 with dissolve
    mc "I know. That's why I wanted to talk to you. What do you suggest that we do?"
    mc "Was this a one-time thing or...?"
    scene ep12_np_bianca18 with dissolve
    bia "You're putting me on the spot here, [name]."
    bia "I didn't think of it as a \"one-time thing\"."
    scene ep12_np_bianca25 with dissolve
    bia "I mean... We did it four times already."
    bia "I felt like I needed what you gave me."
    scene ep12_np_bianca26 with dissolve
    mc "Sex?"
    scene ep12_np_bianca25 with dissolve
    bia "Attention. You made me feel desired."
    bia "I know it sounds shallow, but I haven't felt that in quite some time."
    scene ep12_np_bianca27 with dissolve
    bia "But also, I felt desire too."
    scene ep12_np_bianca25 with dissolve
    bia "If you think it should stay a one-night stand, I'm fine with that."
    bia "And if you think otherwise..."
    scene ep12_np_bianca18 with dissolve
    bia "Fuck... I need to think about this some more. Don't tell Jill anything."
    if branchJill and not "Jill" in breakup and wt_ep9_branch_numbers == 1:
        scene ep12_np_bianca23 with dissolve
        mc "I'm going into the new year single."
        scene ep12_np_bianca24 with dissolve
        bia "What!? Are you breaking up with her tonight?"
        bia "It's New Year's Eve. That would be monstrous."
        scene ep12_np_bianca21 with dissolve
        mc "I've already done worse things to her behind her back."
        mc "At least it's honest."
        scene ep12_np_bianca22 with dissolve
        bia "If that's the case... Keep me out of that conversation."
        scene ep12_np_bianca21 with dissolve
        mc "Ok."
    else:
        scene ep12_np_bianca17 with dissolve
        mc "I won't."
    scene ep12_np_bianca22 with dissolve
    bia "I'd hug you, if that wouldn't raise eyebrows."
    scene ep12_np_bianca28 with dissolve
    mc "Welcome to the party, Bianca! I hope you'll have fun."
    scene ep12_np_bianca29 with dissolve
    bia "Smooth..."
    scene ep12_np_bianca30 with dissolve
    $ renpy.pause()
    if branchJill and wt_ep9_branch_numbers == 1:
        $ new_bio("Bianca", "Bianca got concerned when I told her I intended to break up with Jill.")
    else:
        $ new_bio("Bianca", "Bianca got concerned when she thought about how Jill would react to learning about me and Bianca.")
else:
    scene ep12_np_bianca1 with dissolve
    bia "Hi. Do you have a minute?"
    scene ep12_np_bianca2 with dissolve
    mc "Sure do."
    scene ep12_np_bianca3 with dissolve
    bia "I've been thinking about what happened between us."
    if branchJill:
        bia "I heard that you broke up with Jill."
    else:
        bia "I heard that you broke up with Bella."
    scene ep12_np_bianca4 with dissolve
    mc "Yeah, I did."
    scene ep12_np_bianca3 with dissolve
    bia "Because there was someone else, yeah?"
    scene ep12_np_bianca6 with dissolve
    mc "I'm back together with my ex-girlfriend."
    mc "Listen, what happened between you and me was a mistake."
    scene ep12_np_bianca5 with dissolve
    bia "Sure. You can call it that if you want."
    bia "What I'm more interested in is that you'll keep your word about not telling anyone about it."
    scene ep12_np_bianca6 with dissolve
    mc "Let me reassure you... I won't."
    scene ep12_np_bianca5 with dissolve
    bia "Because it would screw with things on my end."
    scene ep12_np_bianca6 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        

    
    menu:
        "It didn't bother you before \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "It didn't bother you before. Did you grow a conscience all of a sudden?"
            scene ep12_np_bianca5 with dissolve
            bia "I'm not going to get a lecture from you. You've been as bad as me."
        "Not good for me either":
            scene ep12_np_bianca31 with dissolve
            mc "It wouldn't put me in a better position with my friends either."
            scene ep12_np_bianca7 with dissolve
            bia "I'm glad we sorted that out."
            bia "That's all I wanted to hear."
    scene ep12_np_bianca8 with dissolve
    $ renpy.pause()
    $ new_bio("Bianca", "Bianca got concerned when I told her I was breaking up with Jill.")
$ task_list[16] = ""
$ updateTaskList()
jump endEvent

label ep12_np_jill_label:
$ guideSuggestedPage = 260
if tc > 8:
    scene ep12_np_jill1 with dissolve
    ji "So...?"
    scene ep12_np_jill2 with dissolve
    mc "Huh?"
    scene ep12_np_jill1 with dissolve
    ji "What do you think?"
    scene ep12_np_jill2 with dissolve
    mc "Oh... You look great."
    scene ep12_np_jill3 with dissolve
    sa "She spent hours on her dress and makeup. Would some enthusiasm kill you?"
    scene ep12_np_jill4 with dissolve
    mc "Yeah, of course. Sorry..."
    mc "You do look amazing. I'm not entirely myself tonight."
    scene ep12_np_jill5 with dissolve
    ji "Did something happen?"
    scene ep12_np_jill4 with dissolve
    mc "I've got lots on my mind, but we don't have to get into it now."
    scene ep12_np_jill6 with dissolve
    ji "Can you excuse us?"
    scene ep12_np_jill7 with dissolve
    sa "Sure."
    scene ep12_np_jill8 with dissolve
    ji "Do you want to tell me why you've not been yourself lately?"
    scene ep12_np_jill9 with dissolve
    mc "..."
    mc "Now is not a good time."
    scene ep12_np_jill8 with dissolve
    ji "You don't have to shut your feelings in. It's me, [name]. You can tell me anything."
    scene ep12_np_jill9 with dissolve
    mc "It's not that simple. And I don't want to have this conversation with you here on the dance floor."
    scene ep12_np_jill10 with dissolve
    ji "That's fine. We can go somewhere else and have it."
    scene ep12_np_jill9 with dissolve
    mc "It's almost time for dinner. It's bad timing."
    scene ep12_np_jill10 with dissolve
    ji "I worry about you. I want you to be happy, and I get the feeling that you're not."
    ji "Promise you'll tell me what it's all about later."
    scene ep12_np_jill9 with dissolve
    mc "I promise."
    scene ep12_np_jill11 with dissolve
    ji "Good. I'll let you have some space for now, then."
    scene ep12_np_jill12 with dissolve
    ji "*{i}Smack{/i}*"
    scene ep12_np_jill13 with dissolve
    ji "Try smiling. Even when you're feeling down, it can trick you into feeling better."
    scene ep12_np_jill14 with dissolve
    mc "Will do."
    scene ep12_np_jill15 with dissolve
    mc "(Fuck...)"
else:
    scene bg anim_jill_pan_ep12 movie with dissolve
    pause
    scene ep12_np_jill16 with dissolve
    mc "Wow... Look at you."
    menu:
        "Notice Jill":
            scene ep12_np_jill17 with dissolve
            mc "Jill, you look amazing!"
            scene ep12_np_jill18 with dissolve
            $ renpy.pause()
        "Notice both":
            scene ep12_np_jill19 with dissolve
            mc "Both of you look amazing!"
            scene ep12_np_jill20 with dissolve
            $ renpy.pause()
    scene ep12_np_jill21 with dissolve
    ji "Look at yourself! How stylish! I didn't think you owned a shirt like that."
    scene ep12_np_jill22 with dissolve
    mc "I didn't. I got it from Tommy for Christmas."
    mc "Good news, though. He promised he'd help me shop for some nice clothes."
    scene ep12_np_jill23 with dissolve
    ji "But you have nice clothes."
    scene ep12_np_jill22 with dissolve
    mc "Evidently, that's debatable."
    mc "Anyway..."
    scene ep12_np_jill24 with dissolve
    mc "Great job with the party, Sage."
    scene ep12_np_jill25 with dissolve
    sa "We're a dream team, I'll say. However, I'm disappointed with the decision to use confetti."
    scene ep12_np_jill24 with dissolve
    mc "What's wrong with confetti?"
    scene ep12_np_jill25 with dissolve
    sa "It's going to be a bitch to clean it up."
    scene ep12_np_jill24 with dissolve
    mc "Save that problem for future us. That's their problem."
    scene ep12_np_jill23 with dissolve
    ji "Did you take any pictures yet?"
    scene ep12_np_jill22 with dissolve
    mc "Of what?"
    scene ep12_np_jill23 with dissolve
    ji "Of the party... Of people."
    scene ep12_np_jill22 with dissolve
    mc "Ask Josy; she's the paparazzi."
    scene ep12_np_jill26 with dissolve
    ji "You rarely take pictures of us."
    scene ep12_np_jill27 with dissolve
    mc "That's not true. I take some pictures."
    scene ep12_np_jill26 with dissolve
    ji "Seldom on your own initiative."
    ji "Most recently, remember how I had to ask you to take pictures of me wearing Lana's clothes?"
    ji "I have hundreds of pictures of us together."
    scene ep12_np_jill27 with dissolve
    mc "I usually forget to do it."
    scene ep12_np_jill25 with dissolve
    sa "Maybe that should be your New Year's resolution."
    scene ep12_np_jill28 with dissolve
    ji "Oh, that's a good one!"
    scene ep12_np_jill22 with dissolve
    mc "I don't make those resolutions."
    scene ep12_np_jill23 with dissolve
    ji "Have you never made a New Year's resolution?"
    scene ep12_np_jill22 with dissolve
    mc "Maybe once or twice for fun, but I forget about them the day after."
    scene ep12_np_jill26 with dissolve
    ji "You should consider making one for next year."
    scene ep12_np_jill29 with dissolve
    ji "Sage? Can you take a picture of us?"
    scene ep12_np_jill30 with dissolve
    sa "Sure. Give me a camera."
    scene ep12_np_jill29 with dissolve
    ji "I don't have my phone on me."
    scene ep12_np_jill31 with dissolve
    mc "You can use mine. I think it has a camera."
    scene ep12_np_jill32 with dissolve
    ji "Ha-ha..."
    scene ep12_np_jill33 with dissolve
    sa "Um... What's up with that face, [name]?"
    scene ep12_np_jill35 with dissolve
    ji "You're doing the monkey face again, aren't you!?"
    ji "Stop ruining pictures with it."
    scene ep12_np_jill36 with dissolve
    mc "*{i}Monkey noises{/i}* OO OO AA AA!"
    mc "I mean, I'm not making a monkey face."
    scene ep12_np_jill33 with dissolve
    sa "Does he do that a lot?"
    scene ep12_np_jill37 with dissolve
    ji "During that cabin trip I told you about, he made that face when we took a group photo."
    ji "He ruined the one good picture of the rest of us."
    scene ep12_np_jill34 with dissolve
    sa "Hahaha!"
    scene ep12_np_jill38 with dissolve
    mc "Mom used to do it; that's why I find it fun."
    scene ep12_np_jill39 with dissolve
    ji "That doesn't make it excusable."
    scene ep12_np_jill38 with dissolve
    mc "Take a normal, boring picture of us then. I promise I'll smile."
    play sound "sound_effects/camera_shutter.mp3"
    scene ep12_np_jill40 with dissolve
    $ renpy.pause()
    scene ep12_np_jill39 with dissolve
    ji "See... That wasn't hard, was it?"
    scene ep12_np_jill38 with dissolve
    mc "It wasn't hard, but it wasn't fun either."
    scene ep12_np_jill39 with dissolve
    ji "You'll cherish these photos someday. I know it."
    ji "Use that camera at the party, ok?"
    $ mgallery_add_photo("ep12_np_jill_picture")
$ task_list[12] = ""
$ updateTaskList()
jump endEvent

label ep12_np_bujill_label:
scene ep12_np_bujill1 with dissolve
$ renpy.pause()
if "Jill" in breakup:
    scene ep12_np_bujill2 with dissolve
    ji "*{i}Deep breath{/i}*"
    ji "*{i}Exhales{/i}*"
    scene ep12_np_bujill4 with dissolve
    ji "Yes?"
    scene ep12_np_bujill5 with dissolve
    mc "I wanted to wish you a Happy New Year..."
    scene ep12_np_bujill4 with dissolve
    ji "It can't get worse than this year."
    scene ep12_np_bujill5 with dissolve
    mc "I deserve that one."
    scene ep12_np_bujill6 with dissolve
    ji "Can we please not do this?"
    scene ep12_np_bujill5 with dissolve
    mc "Do what?"
    scene ep12_np_bujill6 with dissolve
    ji "The bit where we pretend we can be friends again."
    scene ep12_np_bujill5 with dissolve
    if branchZoey:
        mc "I know how tough it must be for you. I wish I could do something for you."
    else:
        mc "Jill... I miss you."
        scene ep12_np_bujill4 with dissolve
        ji "No. You don't get to say that to me."
        scene ep12_np_bujill5 with dissolve
        mc "But I do."
    scene ep12_np_bujill4 with dissolve
    ji "I'd feel a lot better if you weren't in my life."
    ji "It's hard enough that I have to see you at these parties and on campus..."
    scene ep12_np_bujill6 with dissolve
    ji "Could you at least try not to make me feel worse?"
    scene ep12_np_bujill5 with dissolve
    mc "I'm trying, Jill."
    scene ep12_np_bujill4 with dissolve
    ji "Then stay away from me. Stay away from me, [name]."
    $ new_bio("Jill", "After our breakup, Jill didn't want to be around me.")
else:
    scene ep12_np_bujill3 with dissolve
    ji "*{i}Deep breath{/i}*"
    ji "*{i}Exhales{/i}*"
    scene ep12_np_bujill7 with dissolve
    ji "Yes?"
    scene ep12_np_bujill8 with dissolve
    mc "I wanted to wish you a Happy New Year..."
    scene ep12_np_bujill7 with dissolve
    ji "You too..."
    if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
        scene ep12_np_bujill6 with dissolve
        ji "Listen... I'm sure you've noticed, but it's going to be hard for me to be around you."
        ji "Frankly, I'm disgusted by what you did."
        scene ep12_np_bujill5 with dissolve
        mc "Yeah, I've noticed. I suppose you don't want to hear my side of the story."
        scene ep12_np_bujill4 with dissolve
        ji "I don't think there's anything you can say that would make me feel different."
        if branchIsabella:
            ji "So, out of respect to Sage and Bella..."
        else:
            ji "So, out of respect to Sage..."
        ji "I don't think we can be friends anymore."
        scene ep12_np_bujill5 with dissolve
        mc "I wish there was a way for us all to hang out again..."
        mc "...but I've realized that it won't happen."
        mc "What I did was unforgivable. But I need you to believe that I didn't do it on purpose."
        scene ep12_np_bujill10 with dissolve
        if ep4_toldDerekAboutJade:
            ji "Not on purpose? You recorded a video of it for Hell Week."
        else:
            ji "How do you do THAT with someone without purpose?"
        scene ep12_np_bujill11 with dissolve
        if ep4_toldDerekAboutJade:
            mc "I did. But what I meant was that I didn't do that to harm either Jade or Sage."
        else:
            mc "What I meant was that I didn't do that to harm either Jade or Sage."
        mc "I did something stupid, and I regret it. That's all."
        scene ep12_np_bujill12 with dissolve
        ji "[name]... I'm sorry, but it doesn't cut it."
        scene ep12_np_bujill11 with dissolve
        if branchIsabella:
            mc "Can you please take care of Sage and Bella for me?"
        else:
            mc "Can you please take care of Sage for me?"
        scene ep12_np_bujill12 with dissolve
        ji "I will."
        scene ep12_np_bujill11 with dissolve
        mc "And if you keep an open mind about everything... Maybe in time, we..."
        scene ep12_np_bujill7 with dissolve
        ji "I can't promise you that, [name]."
        scene ep12_np_bujill8 with dissolve
        mc "I'm sorry."
        $ new_bio("Jill", "After what I did with Jade, Jill didn't want to be around me.")
    else:
        ji "I'm sure you've noticed, but it's not the easiest time for any of us right now."
        scene ep12_np_bujill8 with dissolve
        mc "I'm aware. Can I tell you that I don't blame you for choosing sides?"
        scene ep12_np_bujill7 with dissolve
        ji "I don't want to choose sides. But you put me in this position..."
        scene ep12_np_bujill8 with dissolve
        if branchZoey:
            mc "I'm in love with Zoey. I had to be honest about that."
            scene ep12_np_bujill13 with dissolve
            ji "I'm happy you found love, [name]. I hope that feeling keeps you strong now."
            scene ep12_np_bujill8 with dissolve
            mc "Thanks."
        if "Sage" in breakup:
            mc "How's Sage doing?"
        elif "Isabella" in breakup:
            mc "How's Bella doing?"
        else:
            mc "How are Josy and Maya doing?"
        scene ep12_np_bujill14 with dissolve
        ji "Like you'd expect."
        ji "I'm not a child of divorce, but I can imagine how hard that must be for the kids involved."
        ji "And I can only imagine that from how hard it has been for me to stay friends with you at the same time as..."
        scene ep12_np_bujill8 with dissolve
        if "Maya" in breakup:
            mc "Take care of them for me."
        else:
            mc "Take care of her for me."
        scene ep12_np_bujill13 with dissolve
        ji "I will be there."
        scene ep12_np_bujill8 with dissolve
        mc "And maybe in time, if things get easier..."
        scene ep12_np_bujill13 with dissolve
        ji "Who knows, right?"
        scene ep12_np_bujill9 with dissolve
        mc "You're the best, Jill."
        if branchZoey:
            scene ep12_np_bujill13 with dissolve
            ji "Good luck with Zoey. I wish you both happiness."
        if "Sage" in breakup:
            $ new_bio("Jill", "I put Jill in an awkward position after breaking up with Sage. She didn't know how to be around me and support Sage at the same time.")
        if "Isabella" in breakup:
            $ new_bio("Jill", "I put Jill in an awkward position after breaking up with Bella. She didn't know how to be around me and support Bella at the same time.")
        if "Josy" in breakup and "Maya" in breakup:
            $ new_bio("Jill", "I put Jill in an awkward position after breaking up with Josy and Maya. She didn't know how to be around me and support them at the same time.")

scene ep12_np_bujill15 with dissolve
$ renpy.pause()
$ task_list[12] = ""
$ updateTaskList()
jump endEvent

label ep12_np_zmc_label:
if branchZoey:
    play sound "sound_effects/season2/vibrate.mp3"
    scene ep12_np_zmc4
    hide screen dance_filter_screen
    with dissolve
    $ tmpInt = 0
    $ tmpInt2 = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["Zoey","I think I'm here. Meet me outside?",True])
    $ text_message_screen_list.append(["%s" % name,"I'll be right there.",False])
    hide screen new_phone_screen
    show screen text_message_screen
    play sound "sound_effects/interlude/zoey_message.mp3"
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ mphone_scene_to_chat("Zoey",text_message_screen_list)
    show screen new_phone_screen

    scene ep12_np_zmc5 with dissolve
    mc "You found the place."
    scene ep12_np_zmc6 with dissolve
    zo "Yeah, but thank God for phones. It wasn't the most obvious location."
    scene ep12_np_zmc7 with dissolve
    mc "I feel dumb... I should have met you at the station, but it's been a busy day preparing for tonight."
    scene ep12_np_zmc9 with dissolve
    zo "Don't sweat it. I'm here, and I'm ready to party."
    scene ep12_np_zmc7 with dissolve
    mc "Awesome to hear that. Despite being busy, I've waited all night for you to show up."
    scene ep12_np_zmc11 with dissolve
    zo "Don't you want to kiss me?"
    scene ep12_np_zmc8 with dissolve
    mc "Oh, I do. I wasn't sure if you wanted me to."
    scene ep12_np_zmc10 with dissolve
    zo "You don't think I want you to kiss me? What are you saying?"
    scene ep12_np_zmc8 with dissolve
    mc "I meant the whole PDA deal. I didn't want to push you."
    scene ep12_np_zmc18 with dissolve
    $ renpy.pause()
    scene ep12_np_zmc19 with dissolve
    zo "Sweet. But ditch those thoughts. I'll always want to kiss you."
    zo "So, tonight will be challenging for us, won't it?"
    if breakup:
        scene ep12_np_zmc12 with dissolve
        mc "As much as I've looked forward to you coming here, I've been dreading it too."
        scene ep12_np_zmc13 with dissolve
        if branchMayaJosy:
            zo "Are they here?"
        else:
            zo "Is she here?"
        scene ep12_np_zmc12 with dissolve
        mc "Yeah."
        scene ep12_np_zmc13 with dissolve
        if branchMayaJosy:
            zo "Still not talking to them?"
        else:
            zo "Still not talking to her?"
        scene ep12_np_zmc12 with dissolve
        mc "I've tried, but..."
        if zoey_dik:
            scene ep12_np_zmc14 with dissolve
            if branchMayaJosy:
                zo "It's their problem. It shouldn't have to affect us."
            else:
                zo "It's her problem. It shouldn't have to affect us."
            scene ep12_np_zmc12 with dissolve
            mc "That's cold..."
            scene ep12_np_zmc13 with dissolve
            zo "How am I wrong?"
            scene ep12_np_zmc12 with dissolve
            if branchMayaJosy:
                mc "I'd like to do this without upsetting them."
            else:
                mc "I'd like to do this without upsetting her."
            scene ep12_np_zmc14 with dissolve
            zo "I don't think that's an option. You do you, but I'm gonna do me."
            zo "I'm not gonna gloat or anything. But if I want to kiss you, I'm not checking behind my shoulder to see if someone's watching."
            scene ep12_np_zmc12 with dissolve
            mc "I'm ok with that."
        else:
            scene ep12_np_zmc15 with dissolve
            zo "I know how hard it's been for me."
            if branchMayaJosy:
                zo "It must be hard for them, too."
            else:
                zo "It must be hard for her, too."
            scene ep12_np_zmc12 with dissolve
            if branchMayaJosy:
                mc "Yeah. I don't know how they will react to seeing us together."
            else:
                mc "Yeah. I don't know how she will react to seeing us together."
            scene ep12_np_zmc13 with dissolve
            zo "It will happen at some point. But I'll try my best to be respectful about it."
            scene ep12_np_zmc12 with dissolve
            mc "You changed..."
            scene ep12_np_zmc16 with dissolve
            zo "It's called growing up."
            scene ep12_np_zmc12 with dissolve
            if affinity == "DIK":
                mc "I like it... But don't be too respectful. I still want to make out with you at some point."
                scene ep12_np_zmc16 with dissolve
                zo "Haha! Good. Kill it with humor."
            else:
                mc "I like it."
    else:
        scene ep12_np_zmc12 with dissolve
        mc "What makes you say that?"
        scene ep12_np_zmc16 with dissolve
        zo "Can you tell me with a straight face that there won't be any disgruntled chicks in there, glaring at me for snatching you off the market?"
        scene ep12_np_zmc17 with dissolve
        if len(mphone_stats_girl_list) > 10:
            mc "Haha, you never know with a slut like me..."
        else:
            mc "Haha, you never know."
        scene ep12_np_zmc16 with dissolve
        zo "It doesn't matter. You're mine now."
        scene ep12_np_zmc17 with dissolve
        mc "I love the way you say that."
    scene ep12_np_zmc20 with dissolve
    mc "Let's head in and have fun. You can hang your coat in here."
    scene ep12_np_zmc21 with dissolve
    zo "Dude, you laid out the red carpet for me? You didn't have to do that."
    mc "I did, but it's stupid... Everyone else keeps walking all over it."
    zo "Those bastards."
    scene ep12_np_zmc22 with dissolve
    mc "Hold on for a moment."
    scene ep12_np_zmc23 with dissolve
    zo "What's wrong?"
    scene ep12_np_zmc24 with dissolve
    mc "I want to enjoy this moment."
    scene ep12_np_zmc23 with dissolve
    zo "Are we having a moment now? We're just walking upstairs."
    scene ep12_np_zmc25 with dissolve
    mc "I can't believe how pretty you look."
    scene ep12_np_zmc26 with dissolve
    zo "Stahp it."
    scene ep12_np_zmc30 with dissolve
    mc "You are. And something else I can't believe..."
    scene ep12_np_zmc31 with dissolve
    zo "That I'm your girlfriend or something corny like that?"
    scene ep12_np_zmc25 with dissolve
    mc "That you own two dresses."
    scene ep12_np_zmc27 with dissolve
    zo "Haha! You fucking dick!"
    scene ep12_np_zmc28 with dissolve
    mc "I was low-key worried you'd show up in ripped jeans and a hoodie."
    scene ep12_np_zmc29 with dissolve
    zo "Like you're the one to talk about fashion. Since when do you own shirts?"
    scene ep12_np_zmc28 with dissolve
    mc "Tommy gave it to me for Christmas."
    scene ep12_np_zmc29 with dissolve
    zo "That's nice!"
    scene ep12_np_zmc28 with dissolve
    mc "But I do own a couple of other shirts."
    scene ep12_np_zmc29 with dissolve
    zo "They must be horrible if you couldn't wear them tonight."
    zo "I liked what you wore for Christmas. Even though it made you look like a moonlighting lumberjack."
    scene ep12_np_zmc31 with dissolve
    mc "Yeah? And of course, the dress you wear tonight had to be ripped somewhere."
    scene ep12_np_zmc29 with dissolve
    zo "Stop pretending you don't love it."
    scene ep12_np_zmc28 with dissolve
    mc "I love that it's see-through..."
    scene ep12_np_zmc29 with dissolve
    if assman:
        zo "Then you should walk behind me, [mc_de]..."
    else:
        zo "I take it you haven't seen the best part."
    scene ep12_np_zmc32 with dissolve
    if assman:
        mc "I don't like that the nickname is catching on."
    mc "Fuck... Is it ok to leave before midnight?"
    scene ep12_np_zmc33 with dissolve
    zo "I hate to break it to you, but you're not having sex with me this year."
    scene ep12_np_zmc34 with dissolve
    mc "Then let's bring in the new year with a bang."
    scene ep12_np_zmc35 with dissolve
    zo "Were you always this punny, or did that come with your age?"
else:
    scene ep12_np_zmc1
    hide screen dance_filter_screen
    with dissolve
    mc "(Zoey... She came... Why am I not surprised?)"
    scene ep12_np_zmc2 with dissolve
    mc "(I wonder if it was Tommy or Jacob who invited her. Maybe she invited herself.)"
    if branchSage:
        mc "(One thing is for sure. It wasn't Sage who invited Zoey.)"
    scene ep12_np_zmc3 with dissolve
    mc "*{i}Sigh{/i}*"
    mc "(It feels like she'll be around regardless of how I feel about it.)"
    mc "(Or did she show up because she still wants my friendship?)"
    scene ep12_np_zmc2 with dissolve
    mc "(I can't ignore her tonight.)"
    mc "(She deserves an answer from me...)"
    if branchSage and not breakup:
        mc "(And I bet Sage wants one too.)"
    mc "(But I'm not having that conversation on an empty stomach.)"
    $ new_bio("Zoey", "Zoey showed up to our New Year's Eve party. I hadn't invited her.")

$ task_list[13] = ""
$ updateTaskList()
jump endEvent

label ep12_np_josy_label:
scene ep12_np_josy1
hide screen dance_filter_screen
with dissolve
js "Wow! You look stunning in that dress!"
scene ep12_np_josy5 with dissolve
ml "Thank you! But what about you!?"
ml "Where did you buy that?"
scene ep12_np_josy2 with dissolve
js "It's from Bitty Bop Shop."
scene ep12_np_josy5 with dissolve
ml "They sell dresses like that? I never knew."
scene ep12_np_josy3 with dissolve
js "Do you mind if I take your picture? I'm writing a blog post on how to dress to impress."
js "You'd be perfect for it."
scene ep12_np_josy6 with dissolve
ml "Oh, I don't know about that... Your blog is getting big, and I've seen the weirdos who stalk you online."
scene ep12_np_josy2 with dissolve
js "I wouldn't post your handle or name if you're worried about that."
js "And it's not as bad as you'd think. Those followers are harmless."
scene ep12_np_josy6 with dissolve
ml "It wouldn't just be me in that blog post, right?"
scene ep12_np_josy4 with dissolve
js "No, I will ask others at the party too. But if you're uncomfortable, I get it."
scene ep12_np_josy6 with dissolve
ml "It's...how do I put it? Scary exciting."
scene ep12_np_josy4 with dissolve
js "Yep. It is!"
scene ep12_np_josy5 with dissolve
ml "If you show me the pictures you take before you post anything, you can do it."
scene ep12_np_josy7 with dissolve
js "Chin up, and turn your head to your left. Don't look into the camera. Look above and beyond it."
play sound "sound_effects/camera_shutter.mp3"
js "That's perfect!"
play sound "sound_effects/camera_shutter.mp3"
scene ep12_np_josy8 with dissolve
js "You're done. Thanks for doing this for me!"

if breakup or ep4_toldDerekAboutJade:
    mc "(Looks like Josy is working the room for her blog... She seems happy doing that.)"
else:
    scene ep12_np_josy9 with dissolve
    mc "Aren't you going to tell me I look stunning, too?"
    scene ep12_np_josy10 with dissolve
    js "Aw. Are you jealous of the attention?"
    scene ep12_np_josy9 with dissolve
    mc "No. Melanie is beautiful, like you said. But I think I'd be perfect for your blog too."
    scene ep12_np_josy10 with dissolve
    js "Sure. Put on Melanie's dress, and we'll snap a couple."
    scene ep12_np_josy12 with dissolve
    ml "Hahaha! Let's not. It's not his size."
    scene ep12_np_josy13 with dissolve
    mc "So, you're not taking any pictures of guys looking nice? Only girls?"
    scene ep12_np_josy11 with dissolve
    js "It's for a post on women's fashion."
    scene ep12_np_josy13 with dissolve
    mc "Sexist much? Take it from someone who got a passing grade in Gender Studies..."
    mc "Men and women are equal, or should be equal, or aren't equal...or something like that."
    if branchMayaJosy:
        scene ep12_np_josy11 with dissolve
        js "I'll tell you what. I'll pose in a picture together with you."
        js "And if it's good, I'll post it on my blog. Deal?"
        scene ep12_np_josy14 with dissolve
        mc "Make sure you show me at my best, Mel. I'm about to break the internet."
        scene ep12_np_josy36 with dissolve
        $ renpy.pause()
        scene ep12_np_josy55 with dissolve
        ml "[name]? Can you not smile like that?"
        scene ep12_np_josy37 with dissolve
        mc "Can't I smile for a picture?"
        scene ep12_np_josy55 with dissolve
        ml "Look at how Josy does it."
        scene ep12_np_josy38 with dissolve
        mc "What's that face?"
        scene ep12_np_josy39 with dissolve
        js "It's called posing for a picture."
        scene ep12_np_josy38 with dissolve
        mc "I like it more when you smile."
        scene ep12_np_josy39 with dissolve
        js "For a normal picture of us, I would. But not when it's for my blog."
        scene ep12_np_josy40 with dissolve
        mc "You don't want people to see that you're happy?"
        scene ep12_np_josy41 with dissolve
        js "It's fashion, [name]."
        scene ep12_np_josy40 with dissolve
        mc "You lost me."
        scene ep12_np_josy41 with dissolve
        js "I can't believe I have to help you with this. Hold on."
        js "Don't slouch; stand straight."
        scene ep12_np_josy42 with dissolve
        js "Not that straight."
        scene ep12_np_josy43 with dissolve
        js "Better. Now, turn your head to your right."
        scene ep12_np_josy44 with dissolve
        js "Your OTHER right."
        scene ep12_np_josy45 with dissolve
        js "Not that much. *{i}Sigh{/i}* You're doing this on purpose aren't you?"
        scene ep12_np_josy46 with dissolve
        mc "I'm not a model, Josy. Cut me some slack!"
        scene ep12_np_josy47 with dissolve
        js "Good. Open your mouth slightly."
        scene ep12_np_josy48 with dissolve
        js "Not like you're about to eat a sandwich. It needs to be slightly ajar."
        scene ep12_np_josy49 with dissolve
        js "And finally, raise your lower eyelids."
        mc "Huh?"
        scene ep12_np_josy50 with dissolve
        js "Flex your cheeks to gain the model look."
        scene ep12_np_josy51 with dissolve
        js "Yes. Hold that pose!"
        scene ep12_np_josy52 with dissolve
        ml "Taking the picture!"
        play sound "sound_effects/camera_shutter.mp3"
        scene ep12_np_josy53 with dissolve
        ml "Much better! You can probably use this."
        scene ep12_np_josy37 with dissolve
        mc "I felt like a douche."
        scene ep12_np_josy54 with dissolve
        js "Trust me. This is what sells. You did great..."
        js "Eventually."
    if True:
        scene ep12_np_josy11 with dissolve
        js "Pose in a picture together with Melanie."
        js "And if it's good, I'll post it on my blog. Deal?"
        scene ep12_np_josy14 with dissolve
        mc "Make sure you get me at my best. I'm about to break the internet."
        scene ep12_np_josy15 with dissolve
        $ renpy.pause()
        scene ep12_np_josy30 with dissolve
        js "Mel, hold it; you're perfect. [name], what the hell are you doing?"
        scene ep12_np_josy17 with dissolve
        mc "I'm being myself."
        scene ep12_np_josy16 with dissolve
        js "Well, it looks wrong."
        scene ep12_np_josy17 with dissolve
        mc "If being myself is wrong, I don't want to live in this world."
        scene ep12_np_josy30 with dissolve
        js "For a normal picture, you can smile as much as you want. But not when it's for my blog."
        scene ep12_np_josy18 with dissolve
        mc "You don't want people to see that we're happy?"
        scene ep12_np_josy31 with dissolve
        js "It's fashion, [name]."
        scene ep12_np_josy18 with dissolve
        mc "You lost me."
        scene ep12_np_josy30 with dissolve
        js "I can't believe I have to help you with this."
        js "Don't slouch; stand straight."
        scene ep12_np_josy19 with dissolve
        js "Not that straight."
        scene ep12_np_josy20 with dissolve
        js "Better. Now, turn your head to your right."
        scene ep12_np_josy21 with dissolve
        js "Your OTHER right."
        scene ep12_np_josy22 with dissolve
        js "Not that much. *{i}Sigh{/i}* You're doing this on purpose aren't you?"
        scene ep12_np_josy23 with dissolve
        mc "I'm not a model, Josy. Cut me some slack!"
        scene ep12_np_josy24 with dissolve
        js "Good. Open your mouth slightly."
        scene ep12_np_josy25 with dissolve
        js "Not like you're about to eat a sandwich. It needs to be slightly ajar."
        scene ep12_np_josy26 with dissolve
        js "And finally, raise your lower eyelids."
        mc "Huh?"
        scene ep12_np_josy27 with dissolve
        js "Flex your cheeks to gain the model look. A little bit less... Almost..."
        scene ep12_np_josy28 with dissolve
        js "Yes. Hold that pose!"
        play sound "sound_effects/camera_shutter.mp3"
        js "We got the picture!"
        scene ep12_np_josy29 with dissolve
        mc "I felt like a douche."
        scene ep12_np_josy31 with dissolve
        js "Trust me. This is what sells. You did great..."
        js "Eventually."
        scene ep12_np_josy32 with dissolve
        ml "*{i}Whispers{/i}* Would you mind using the other picture with just me in it for the blog?"
        scene ep12_np_josy35 with dissolve
        js "*{i}Whispers{/i}* Duh. That's a no-brainer."
    scene ep12_np_josy34 with dissolve
    js "Oh! Have you seen Heather? She also looks amazing!"
    scene ep12_np_josy33 with dissolve
    ml "I saw her with Elena not that long ago."
    scene ep12_np_josy34 with dissolve
    js "Thanks!"

$ task_list[13] = ""
$ updateTaskList()
if "Maya" not in breakup:
    $ event_list.append("ep12_np_maya_label")
    if persistent.mod_wtenabled: 
        $ task_list[5] = "Talk to Maya (Dining room)"
    else:
        $ task_list[5] = "Talk to Maya"
    $ updateTaskList()
$ new_bio("Josy", "Josy was snapping photos of girls in their dresses for her blog.")
jump endEvent

label ep12_np_maya_label:
if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
    scene ep12_np_maya1b with dissolve
    mc "Hi Maya... What are you up to?"
    scene ep12_np_maya4b with dissolve
    my "I'm helping with the final preparations for dinner. How about you?"
    scene ep12_np_maya5b with dissolve
    mc "I'm walking around bothering people."
    scene ep12_np_maya6b with dissolve
    $ renpy.pause()
    scene ep12_np_maya7b with dissolve
    mc "How was...your holiday?"
    scene ep12_np_maya8b with dissolve
    my "Christmas with family was great. Mom had good moments, and Dad felt different, in a good way."
    scene ep12_np_maya9b with dissolve
    my "*{i}Sigh{/i}*"
    my "How have you been? I heard from Sage that...uh..."
    scene ep12_np_maya10b with dissolve
    mc "I've felt horrible."
    scene ep12_np_maya4b with dissolve
    my "Yeah. I can't believe you did that."
    if ep4_toldDerekAboutJade:
        my "It felt like something you wouldn't do. And that it was for Hell Week made it even worse."
    else:
        my "It felt like something you wouldn't do."
    scene ep12_np_maya5b with dissolve
    mc "There's a lot of layers to that story... I didn't do it with malicious intent."
    if ep4_toldDerekAboutJade:
        mc "Remember your scavenger hunt? That one was pretty out there, too."
    scene ep12_np_maya4b with dissolve
    my "I understand urges and temptations, but...still... It's hard for me to swallow."
    scene ep12_np_maya10b with dissolve
    mc "For you and everyone else, it seems."
    scene ep12_np_maya11b with dissolve
    my "Huh? How many know about it?"
    scene ep12_np_maya10b with dissolve
    mc "I meant, among our closest friends."
    scene ep12_np_maya9b with dissolve
    my "Yeah, well, I hope it doesn't spread beyond that for everyone's sake."
    scene ep12_np_maya10b with dissolve
    mc "Sage looks at me like I'm disgusting. I think she hates me."
    scene ep12_np_maya6b with dissolve
    my "..."
    mc "Do you hate me too?"
    scene ep12_np_maya9b with dissolve
    my "*{i}Sigh{/i}* [name]..."
    my "You'll always be the fun and caring guy I met in college."
    my "But everything about this feels so weird."
    scene ep12_np_maya12b with dissolve
    my "I don't know which leg to stand on."
    my "I only know that I empathize with what Sage is going through."
    scene ep12_np_maya13b with dissolve
    my "I'm not sure if I empathize with you. Mistake or not... You caused this."
    my "You made that choice."
    scene ep12_np_maya9b with dissolve
    my "It's hard for me to pretend it was nothing. But at the same time, I don't want to lose your friendship."
    my "What would you do in my situation?"
    scene ep12_np_maya14b with dissolve
    mc "You should be there for Sage."
    scene ep12_np_maya9b with dissolve
    my "What about you?"
    scene ep12_np_maya14b with dissolve
    mc "I'm still going to call you my friend. But I'll back off and give you space."
    mc "I wish I could undo everything... But I'll have to live with this."
    scene ep12_np_maya15b with dissolve
    my "Take care of yourself, [name]. I'm rooting for you."
    $ new_bio("Maya", "Maya didn't want to lose my friendship, but didn't know what to do after learning about what I had done with Jade.")
elif breakup:
    scene ep12_np_maya2b with dissolve
    mc "Hi Maya... What are you up to?"
    scene ep12_np_maya16b with dissolve
    my "I'm helping with the final preparations for dinner. How about you?"
    scene ep12_np_maya17b with dissolve
    mc "I'm walking around bothering people."
    scene ep12_np_maya18b with dissolve
    $ renpy.pause()
    scene ep12_np_maya17b with dissolve
    mc "How was your holiday?"
    scene ep12_np_maya16b with dissolve
    my "Christmas with family was great. Mom had good moments, and Dad felt different, in a good way."
    scene ep12_np_maya19b with dissolve
    my "*{i}Sigh{/i}*"
    my "How have you been?"
    if "Isabella" in breakup:
        my "I heard about you and...uh...Bella."
        scene ep12_np_maya20b with dissolve
    if "Sage" in breakup:
        mc "I take it you know about Sage?"
    elif "Jill" in breakup:
        mc "I take it you know about Jill?"
    mc "It's not been great."
    scene ep12_np_maya5b with dissolve
    mc "The breakup had to happen..."
    mc "But I realize I fucked up the friendship in our group by doing that."
    scene ep12_np_maya4b with dissolve
    my "I can't lie, [name]. You did."
    scene ep12_np_maya5b with dissolve
    mc "Does that make you not want to be my friend?"
    scene ep12_np_maya19b with dissolve
    my "No, [name]. You'll always be my friend."
    my "But I'm still friends with them, and there are some mixed feelings..."
    scene ep12_np_maya20b with dissolve
    mc "I know."
    if branchZoey:
        scene ep12_np_maya21b with dissolve
        my "Amid everything, I'm happy for you. For finding love."
        my "You deserve that."
        scene ep12_np_maya17b with dissolve
        mc "I wish it had happened differently, but I'm also happy about it."
    scene ep12_np_maya22b with dissolve
    my "I'm here for you if you need to talk."
    my "Uncomfortable as it may be to the rest of them, I'm not picking a side."
    scene ep12_np_maya23b with dissolve
    my "They are smart women. They will understand that I can be friends with you, too."
    my "You're still you."
    scene ep12_np_maya24b with dissolve
    mc "Thank you so much, Maya. I needed to hear that."
    if "Sage" in breakup:
        $ new_bio("Maya", "Maya told me she still wanted my friendship, but that it was a hard situation since she's still friends with Sage.")
    if "Isabella" in breakup:
        $ new_bio("Maya", "Maya told me she still wanted my friendship, but that it was a hard situation since she's still friends with Bella.")
    if "Jill" in breakup:
        $ new_bio("Maya", "Maya told me she still wanted my friendship, but that it was a hard situation since she's still friends with Jill.")
else:
    if maya_shiny_dress:
        scene bg anim_maya_pan1_ep12 movie with dissolve
    else:
        scene bg anim_maya_pan1b_ep12 movie with dissolve
    pause
    if maya_shiny_dress:
        scene ep12_np_maya3 with dissolve
    else:
        scene ep12_np_maya3b with dissolve
    mc "Hey, gorgeous... What are you up to?"
    if maya_shiny_dress:
        scene ep12_np_maya25 with dissolve
    else:
        scene ep12_np_maya25b with dissolve
    my "I'm helping with the final preparations for dinner. How about you?"
    if maya_shiny_dress:
        scene ep12_np_maya26 with dissolve
    else:
        scene ep12_np_maya26b with dissolve
    mc "I'm walking around bothering people."
    if maya_shiny_dress:
        scene ep12_np_maya27 with dissolve
    else:
        scene ep12_np_maya27b with dissolve
    my "Haha! You need chores not to get restless, don't you?"
    if maya_shiny_dress:
        scene ep12_np_maya26 with dissolve
    else:
        scene ep12_np_maya26b with dissolve
    mc "When people are busy helping out, it's hard to have fun."
    if maya_shiny_dress:
        scene ep12_np_maya25 with dissolve
    else:
        scene ep12_np_maya25b with dissolve
    my "Don't worry. Soon everyone will be done with the chores and will have fun together with you."
    my "Did you see Josy anywhere? I wonder what she's up to."
    if maya_shiny_dress:
        scene ep12_np_maya26 with dissolve
    else:
        scene ep12_np_maya26b with dissolve
    mc "She's harassing guests."
    if maya_shiny_dress:
        scene ep12_np_maya27 with dissolve
    else:
        scene ep12_np_maya27b with dissolve
    my "I don't believe that."
    if maya_shiny_dress:
        scene ep12_np_maya28 with dissolve
    else:
        scene ep12_np_maya28b with dissolve
    mc "She's taking pictures of hot girls for her blog."
    if maya_shiny_dress:
        scene ep12_np_maya25 with dissolve
    else:
        scene ep12_np_maya25b with dissolve
    my "Ah... Is she out to get new material for it?"
    my "I'm not surprised. With how everyone looks tonight, it's the perfect opportunity for her."
    if maya_shiny_dress:
        scene ep12_np_maya28 with dissolve
    else:
        scene ep12_np_maya28b with dissolve
    mc "I guess. Did she take your picture yet?"
    if maya_shiny_dress:
        scene ep12_np_maya29 with dissolve
    else:
        scene ep12_np_maya29b with dissolve
    my "No. I don't think I'd fit in her blog, and she knows it."
    if maya_shiny_dress:
        scene ep12_np_maya28 with dissolve
    else:
        scene ep12_np_maya28b with dissolve
    mc "I had to force her to take my picture. I don't fit in that blog either."
    if maya_shiny_dress:
        scene ep12_np_maya30 with dissolve
    else:
        scene ep12_np_maya30b with dissolve
    mc "But! That doesn't mean we're not hot."
    mc "Don't let Josy define you."
    if maya_shiny_dress:
        scene ep12_np_maya31 with dissolve
    else:
        scene ep12_np_maya31b with dissolve
    my "I see that you've been hitting the bar early tonight."
    if maya_shiny_dress:
        scene ep12_np_maya30 with dissolve
    else:
        scene ep12_np_maya30b with dissolve
    mc "I'm not drunk. I'm tipsy. But that doesn't mean I'm wrong about us."
    if branchMayaJosy:
        if maya_shiny_dress:
            scene ep12_np_maya32 with dissolve
        else:
            scene ep12_np_maya32b with dissolve
        my "You're adorable."
        if maya_shiny_dress:
            scene ep12_np_maya33 with dissolve
        else:
            scene ep12_np_maya33b with dissolve
        mc "Josy doesn't like my smile. There's nothing wrong with it, right?"
        if check_mlove():
            if maya_shiny_dress:
                scene ep12_np_maya32 with dissolve
            else:
                scene ep12_np_maya32b with dissolve
            my "It always brightens my day up."
            if maya_shiny_dress:
                scene ep12_np_maya33 with dissolve
            else:
                scene ep12_np_maya33b with dissolve
            mc "You'd put it on your blog, right?"
        if maya_shiny_dress:
            scene ep12_np_maya34 with dissolve
        else:
            scene ep12_np_maya34b with dissolve
        $ renpy.pause()
        if maya_shiny_dress:
            scene ep12_np_maya32 with dissolve
        else:
            scene ep12_np_maya32b with dissolve
    else:
        if maya_shiny_dress:
            scene ep12_np_maya31 with dissolve
        else:
            scene ep12_np_maya31b with dissolve
        my "You're cute."
    my "I need to finish up here, [name]."
    if maya_shiny_dress:
        scene ep12_np_maya30 with dissolve
    else:
        scene ep12_np_maya30b with dissolve
    mc "Fine. I'll go bother someone else."
$ task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep12_np_bmc_label:
if breakup or ep4_toldDerekAboutJade:
    scene ep12_np_bmc1
    show screen dance_filter_screen
    with dissolve
    mc "Enjoying your gig?"
    scene ep12_np_bmc2 with dissolve
    isa "Babysitting adults? It's the perfect way to end the year."
    scene ep12_np_bmc3 with dissolve
    mc "You didn't have to volunteer."
    scene ep12_np_bmc2 with dissolve
    if branchIsabella:
        isa "Yeah, I'm starting to regret it."
    else:
        isa "I know."
    scene ep12_np_bmc3 with dissolve
    mc "How are things with you?"
    if branchIsabella:
        scene ep12_np_bmc4 with dissolve
        isa "I'd prefer it if we didn't do this charade. It would make it much easier for me if we could keep it to the bare necessities."
        scene ep12_np_bmc3 with dissolve
        mc "*{i}Sigh{/i}* Alright... You know where to find me if you need me for something party-related."
        $ new_bio("Isabella", "Bella worked as a chaperone at our New Year's Eve party. She didn't want to speak to me to make our breakup easier.")
    else:
        scene ep12_np_bmc4 with dissolve
        isa "I'm doing fine. And you?"
        scene ep12_np_bmc3 with dissolve
        mc "It could be better."
        if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
            mc "Are you mad at me?"
            scene ep12_np_bmc4 with dissolve
            isa "Severely disappointed."
            scene ep12_np_bmc6 with dissolve
            mc "Can we...uh...repair the damages?"
            scene ep12_np_bmc5 with dissolve
            isa "Not under these circumstances, no."
            isa "It would make it much easier for me if we could keep it to the bare necessities."
            scene ep12_np_bmc6 with dissolve
            mc "*{i}Sigh{/i}* Alright... You know where to find me if you need me for something party-related."
            $ new_bio("Isabella", "Bella worked as a chaperone at our New Year's Eve party. She didn't want to speak to me because of what I did with Jade.")
        else:
            if ep12_break_or_tell == "break":
                scene ep12_np_bmc5 with dissolve
                isa "I get that you're going through a tough time."
                scene ep12_np_bmc6 with dissolve
                mc "I am. And it sucks that it has affected my friends. I mean, you girls..."
                scene ep12_np_bmc5 with dissolve
                isa "Your breakup is none of my business. But I do feel it's a shame because I can see how it affects everyone in our group."
                scene ep12_np_bmc7 with dissolve
                mc "Do you still hang out with everyone?"
            else:
                scene ep12_np_bmc5 with dissolve
                isa "Are you not happy with your girlfriend?"
                scene ep12_np_bmc6 with dissolve
                mc "I am. But I'm unhappy with my friends."
                scene ep12_np_bmc5 with dissolve
                isa "Your breakup is none of my business. But I do feel it's a shame because I can see how it affects everyone in our group."
                scene ep12_np_bmc7 with dissolve
                mc "I know it does. Do you still hang out with everyone?"
            scene ep12_np_bmc8 with dissolve
            isa "Derek hasn't been around, but I've spent time with the rest of them."
            scene ep12_np_bmc7 with dissolve
            mc "Are you mad at me?"
            scene ep12_np_bmc9 with dissolve
            isa "Of course not. I'm not a teenager; I know how these relationships come and go."
            isa "You're in a soul-searching phase of your life. Everyone goes through it."
            scene ep12_np_bmc10 with dissolve
            isa "I'm not mad at you at all. But I'm sad because I thought our group had something special together."
            isa "A very special friendship. And now that bubble has burst."
            scene ep12_np_bmc8 with dissolve
            isa "While I adore the girls, I miss you."
            scene ep12_np_bmc7 with dissolve
            mc "I miss you too. I can't tell if we'll ever hang out like that again, but I don't hold anything against any of you."
            scene ep12_np_bmc8 with dissolve
            if branchSage:
                isa "Sage is hurting now. But who knows how she'll feel in a month or two. Let's give it time and see."
            elif branchJill:
                isa "Jill is hurting now. But who knows how she'll feel in a month or two. Let's give it time and see."
            else:
                isa "Josy and Maya are hurting now. But who knows how they'll feel in a month or two. Let's give it time and see."
            scene ep12_np_bmc7 with dissolve
            if branchMayaJosy:
                mc "Thank you for being there for them."
            else:
                mc "Thank you for being there for her."
            scene ep12_np_bmc9 with dissolve
            isa "You can always call me if you need me."
            scene ep12_np_bmc7 with dissolve
            mc "You too."
            $ new_bio("Isabella", "Bella worked as a chaperone at our New Year's Eve party. Bella told me she missed me and that she didn't hold anything against me.")
else:
    scene bg anim_bella_pan_ep12 movie
    show screen dance_filter_screen
    with dissolve
    pause
    scene ep12_np_bmc11 with dissolve
    isa "*{i}Cough cough{/i}*"
    scene ep12_np_bmc12 with dissolve
    mc "What?"
    scene ep12_np_bmc11 with dissolve
    isa "Why are you drinking?"
    scene ep12_np_bmc13 with dissolve
    mc "Why are YOU drinking?"
    scene ep12_np_bmc14 with dissolve
    isa "Good point. Carry on."
    scene ep12_np_bmc15 with dissolve
    mc "Enjoying your gig?"
    scene ep12_np_bmc16 with dissolve
    isa "Babysitting adults? It's the perfect way to end the year."
    scene ep12_np_bmc17 with dissolve
    mc "You didn't have to volunteer."
    scene ep12_np_bmc16 with dissolve
    if branchIsabella:
        isa "How else could I spend the evening with you?"
        scene ep12_np_bmc17 with dissolve
        mc "You could have reused your mummy outfit."
        mc "But you wouldn't be as pretty as you are tonight."
        scene ep12_np_bmc25 with dissolve
        mc "10 out of 10. Would hire this chaperone again."
    else:
        isa "How else could I spend the evening with you guys?"
        scene ep12_np_bmc17 with dissolve
        mc "You could have borrowed our Diablo mask again."
        mc "But I have to say, I prefer this outfit."

    scene ep12_np_bmc16 with dissolve
    isa "Jill and I bought ours together. It required us to muster up courage."
    isa "She, more so than I."
    isa "Perhaps it is too much for a chaperone to wear..."
    scene ep12_np_bmc27 with dissolve
    mc "Did you see Jade? Cleavage down to here."
    scene ep12_np_bmc18 with dissolve
    isa "I did. Sage raged into my ear that Jade showed up in a similar outfit."
    scene ep12_np_bmc17 with dissolve
    mc "They are not that similar."
    scene ep12_np_bmc18 with dissolve
    isa "That's what I said. No one else will notice."
    scene ep12_np_bmc15 with dissolve
    $ renpy.pause()
    scene ep12_np_bmc16 with dissolve
    isa "What were the worst and best things that happened to you this year?"
    scene ep12_np_bmc17 with dissolve
    mc "Do we have to do the worst?"
    scene ep12_np_bmc16 with dissolve
    isa "Fine. What was the best thing?"
    scene ep12_np_bmc17 with dissolve
    mc "Coming here to B&R. Without a doubt."
    mc "It led to many wonderful things... Ironically, most of the bad things, too."
    mc "But yeah... That's my answer. How about you?"
    scene ep12_np_bmc16 with dissolve
    isa "This has been a good year."
    isa "I feel like I've made big personal progress."
    scene ep12_np_bmc19 with dissolve
    isa "The year didn't start off eventful, but after you showed up..."
    isa "Something happened to my year."
    scene ep12_np_bmc17 with dissolve
    mc "In other words, the best thing about the year was that I came to B&R for you, too."
    scene ep12_np_bmc16 with dissolve
    isa "Haha. There's more to it than that. But yes, you're a part of it."
    isa "I hope I can continue to make progress. It feels nice."
    scene ep12_np_bmc18 with dissolve
    isa "In some ways, I feel more like myself than I have in many years."
    isa "Even before James left me. Like, before my parents passed away."
    scene ep12_np_bmc20 with dissolve
    mc "Putting it mildly, you've had it rough..."
    scene ep12_np_bmc21 with dissolve
    isa "That's an apt description. And it kills me..."
    isa "Before all of that. Before James disappeared, before my parents died, I was so much different."
    scene ep12_np_bmc18 with dissolve
    isa "I was a happy and bubbly girl."
    scene ep12_np_bmc20 with dissolve
    mc "That's a long time ago. You were in college back then."
    scene ep12_np_bmc18 with dissolve
    isa "It has nothing to do with age, [name]. It has everything to do with life experiences."
    isa "Do you know how hard it is to be happy when the world is falling down around you?"
    scene ep12_np_bmc21 with dissolve
    isa "It takes a certain kind of person to push through the pain and stay true to themselves."
    isa "I want to be that person, but I'm not."
    isa "I crumble."
    scene ep12_np_bmc16 with dissolve
    isa "And that's why this year ultimately felt good. I'm finding my way back to the person I used to be."
    isa "Even though it saddens me that I've missed out on plenty of good years."
    scene ep12_np_bmc17 with dissolve
    mc "You're not old. You're not even halfway through your life yet."
    scene ep12_np_bmc18 with dissolve
    isa "You cannot know that."
    scene ep12_np_bmc17 with dissolve
    mc "If you're optimistic, you can say that."
    mc "I think it's great that you're finding yourself again."
    mc "One thing I've noticed about you this year is that you've felt happier each month."
    mc "You didn't exactly smile or laugh when I first met you."
    scene ep12_np_bmc22 with dissolve
    isa "I smiled and laughed."
    scene ep12_np_bmc17 with dissolve
    mc "No. Bella. Stop. When?"
    scene ep12_np_bmc22 with dissolve
    isa "Maybe you were a drag to be around at first. Did you think of that?"
    scene ep12_np_bmc23 with dissolve
    mc "No. I'm a hoot."
    scene ep12_np_bmc24 with dissolve
    isa "Hahaha!"
    scene ep12_np_bmc23 with dissolve
    mc "See. You didn't give me any of that."
    mc "Though I didn't see you during the first two-thirds of this year, I've witnessed this progress you speak of."
    scene ep12_np_bmc17 with dissolve
    if branchIsabella:
        mc "I'm proud of you. And being with you is another of the best things that happened this year."
        scene ep12_np_bmc16 with dissolve
        isa "You cannot pick two best things."
        scene ep12_np_bmc17 with dissolve
        mc "The first best thing led to us, so I think it's implied."
    else:
        mc "I'm proud of you. And I'm happy to call you my friend."
    scene ep12_np_bmc23 with dissolve
    mc "Cheers to the end of the year."
    play sound "sound_effects/bottle_clink.mp3"
    scene ep12_np_bmc26 with dissolve
    $ renpy.pause()
    $ new_bio("Isabella", "Bella worked as a chaperone at our New Year's Eve party.")
$ optional_task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep12_np_qmc_label:
scene ep12_np_qmc1 with dissolve
mc "Nice dress. If you can call it that."
scene ep12_np_qmc2 with dissolve
qu "Nice \"suit\"."
scene ep12_np_qmc3 with dissolve
mc "The invitation didn't say suit."
scene ep12_np_qmc2 with dissolve
qu "Whatever. Rules are made to be broken."
scene ep12_np_qmc3 with dissolve
mc "Are dresses made to be ripped?"
scene ep12_np_qmc4 with dissolve
qu "Aha, so you did check out my ass already."
scene ep12_np_qmc5 with dissolve
mc "Me and everyone else in here."
qu "Not everyone in here gets to tap it."
scene ep12_np_qmc6 with dissolve
mc "Don't remind me... These pants are tight enough."
mc "How are things on your end?"
scene ep12_np_qmc7 with dissolve
qu "My end, or my end of the party?"
scene ep12_np_qmc8 with dissolve
mc "Both."
scene ep12_np_qmc7 with dissolve
qu "The party is taken care of, and on my end...nothing new."
scene ep12_np_qmc8 with dissolve
mc "That's good, right?"
scene ep12_np_qmc9 with dissolve
qu "I wouldn't want it any other way."
scene ep12_np_qmc8 with dissolve
mc "When can you let your guard down?"
scene ep12_np_qmc9 with dissolve
qu "I kind of have."
scene ep12_np_qmc8 with dissolve
mc "You have?"
scene ep12_np_qmc10 with dissolve
qu "It was scary for a few days after, but not anymore."
qu "I won, [name]."
scene ep12_np_qmc11 with dissolve
mc "So, that's why you feel more relaxed."
mc "Then I'll try to do that too."
scene ep12_np_qmc10 with dissolve
qu "I didn't mean to worry you."
scene ep12_np_qmc11 with dissolve
mc "You did. I didn't know what the hell to do."
mc "I wanted to help you, but I couldn't because you wouldn't let me."
scene ep12_np_qmc12 with dissolve
qu "I'm sorry I had you worried."
qu "But if I had dragged you into my mess..."
qu "You don't deserve it."
scene ep12_np_qmc13 with dissolve
mc "What's next on your agenda? Are you dropping out of college next year?"
scene ep12_np_qmc14 with dissolve
qu "I don't know yet. But there's no way I'll leave when you're still around."
scene ep12_np_qmc15 with dissolve
mc "Quinn..."
scene ep12_np_qmc16 with dissolve
qu "What?"
scene ep12_np_qmc15 with dissolve
mc "That didn't sound like you."
scene ep12_np_qmc16 with dissolve
qu "Whatever..."
scene ep12_np_qmc14 with dissolve
qu "Wipe that grin off."
scene ep12_np_qmc17 with dissolve
mc "What's next? Will you kiss me at midnight?"
scene ep12_np_qmc18 with dissolve
qu "If I kiss you now, can we skip that?"
scene ep12_np_qmc17 with dissolve
mc "Sure."
scene anim_quinn_kiss_ep12 with dissolve
pause
scene ep12_np_qmc19 with dissolve
$ renpy.pause()
scene ep12_np_qmc20 with dissolve
mc "Now, who will I kiss at midnight?"
play sound "sound_effects/shove.mp3"
scene ep12_np_qmc21 with hpunch
mc "Haha, I'm joking."
scene ep12_np_qmc22 with dissolve
$ renpy.pause()
scene ep12_np_qmc23 with dissolve
qu "After dinner, when all this formal crap is over and done with..."
qu "I'm gonna be your party bitch."
scene ep12_np_qmc22 with dissolve
mc "What does that mean?"
scene ep12_np_qmc23 with dissolve
qu "They might ask us to leave. But it will be worth it."
$ task_list[14] = ""
$ updateTaskList()
$ new_bio("Quinn", "Quinn was in a good mood at the New Year's Eve party. She seemed relaxed and more like herself than she had been for a long time.")
jump endEvent

label ep12_np_nicmc_label:
if ep12_nicole_breakup or ep12_nicole_ditch:
    scene ep12_np_nicmc1 with dissolve
    $ renpy.pause()
    scene ep12_np_nicmc3 with dissolve
    $ renpy.pause()
    scene ep12_np_nicmc4 with dissolve
    if ep12_nicole_ditch:
        mc "(Yep... She's still upset with me for skipping our dinner date. I can't blame her.)"
        mc "(I should have called her...)"
    else:
        mc "(Yep... She's still upset with me. I can't blame her.)"
    $ new_bio("Envy", "Nicole wasn't happy with me at the New Year's Eve party.")
else:
    scene ep12_np_nicmc2 with dissolve
    nic "There he is!"
    scene ep12_np_nicmc5 with dissolve
    nic "*{i}Smack{/i}* Mmm..."
    scene ep12_np_nicmc6 with dissolve
    nic "I've missed you."
    scene ep12_np_nicmc7 with dissolve
    mc "I've missed you, too. My God, you're beautiful."
    scene ep12_np_nicmc6 with dissolve
    nic "Aw... You too!"
    scene ep12_np_nicmc8 with dissolve
    nic "Look at what Sandy's wearing. Isn't she pretty?"
    scene ep12_np_nicmc9 with dissolve
    mc "Sandy? Wow!"
    scene ep12_np_nicmc10 with dissolve
    sn "Yeah, yeah. Go ahead and mock me."
    scene ep12_np_nicmc11 with dissolve
    mc "Why would I mock you? You look incredible."
    nic "She doesn't like formal wear. It took me a lot of convincing to make her come here wearing that dress."
    scene ep12_np_nicmc10 with dissolve
    sn "[name], formal wear isn't for me! This dress makes me look like a prude."
    scene ep12_np_nicmc9 with dissolve
    mc "I think it doesn't look formal at all."
    scene ep12_np_nicmc10 with dissolve
    sn "You're just saying that to make me feel better."
    scene ep12_np_nicmc11 with dissolve
    mc "No, I'm not. I'm sure it's intended to be a formal dress, but the way you wear it makes it feel..."
    
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    menu:
        "Informal \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "Informal."
            scene ep12_np_nicmc12 with dissolve
            sn "I'll take it..."
            sn "Everyone else wears dresses like mine, so I shouldn't complain."
        "Slutty \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "Slutty."
            scene ep12_np_nicmc13 with dissolve
            sn "That's the nicest thing anyone has said to me tonight."
            scene ep12_np_nicmc14 with dissolve
            sn "Thank you so much, [name]!"
            scene ep12_np_nicmc15 with dissolve
            mc "You're welcome?"

    scene ep12_np_nicmc16 with dissolve
    nic "How was your holiday? I wanna know all about it."
    scene ep12_np_nicmc17 with dissolve
    mc "And I want to know all about yours. Did everything work out well with Christmas?"
    scene ep12_np_nicmc18 with dissolve
    nic "We had a great Christmas together, and I dropped Marvin off with Luke earlier today."
    scene ep12_np_nicmc19 with dissolve
    sn "Aw, sweetie... I know it blows, but you have to make the best of it."
    sn "Celebrate with us tonight and try not to think about stupid Luke and his shitty relatives."
    scene ep12_np_nicmc18 with dissolve
    nic "I'm not going to mope around. But [name] asked, and he knows how I feel about it."
    scene ep12_np_nicmc20 with dissolve
    sn "You two are like a match made in heaven. And I'm not talking about the strip club."
    scene ep12_np_nicmc17 with dissolve
    mc "There's a strip club called Heaven?"
    scene ep12_np_nicmc16 with dissolve
    nic "There are at least three of them in this city alone."
    nic "But yes, I think [name] and I go well together. Wouldn't you say?"
    scene ep12_np_nicmc17 with dissolve
    mc "I do like standing next to you because you make me look prettier."
    scene ep12_np_nicmc21 with dissolve
    sn "Ugh... Such a line. I need to find myself a boy toy, too."
    scene ep12_np_nicmc22 with dissolve
    mc "A boy toy?"
    scene ep12_np_nicmc23 with dissolve
    nic "You know how she is. She doesn't mean that."
    nic "You know I don't view you as a toy."
    scene ep12_np_nicmc22 with dissolve
    mc "I know what you're after, and a boy toy doesn't fit the description."
    scene ep12_np_nicmc23 with dissolve
    nic "No, [name]. You're a man."
    nic "You're young, but still a man."
    scene ep12_np_nicmc24 with dissolve
    nic "And you know how to treat me."
    nic "You're never dull to be around."
    nic "And you're fantastic in bed."
    scene ep12_np_nicmc25 with dissolve
    mc "That's quite the performance review."
    scene ep12_np_nicmc24 with dissolve
    nic "You're nailing it."
    scene ep12_np_nicmc26 with dissolve
    nic "*{i}Smack{/i}*"
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep12_np_cf_label:
scene ep12_np_cf0a with dissolve
cha "Really? In the bathroom?"
scene ep12_np_cf0b with dissolve
fel "Yeah, go check for yourself. It was some kind of powder."
scene ep12_np_cf1 with dissolve
fel "Damn... Looking hot tonight, [name]."
scene ep12_np_cf2 with dissolve
cha "Love that shirt and the casual yet formal look."
scene ep12_np_cf5 with dissolve
fel "How is something casual and formal at the same time?"
scene ep12_np_cf6 with dissolve
cha "That is."
if ep11_mistletoe > 0:
    scene ep12_np_cf4 with dissolve
    fel "I should have brought a mistletoe with me tonight."
    fel "Maybe I'll find one close to midnight. What do you say, [name]?"
    scene ep12_np_cf3 with dissolve
    menu:
        "Looking good":
            mc "You two look nice tonight, too."
            scene ep12_np_cf7 with dissolve
            cha "Haha, he so dodged your invite."
            scene ep12_np_cf8 with dissolve
            fel "Whatever."
        "I don't remember you \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "Who are you again?"
            scene ep12_np_cf9 with dissolve
            fel "Pff. So, that's how you want to play this, huh?"
else:
    scene ep12_np_cf3 with dissolve
    mc "Thanks, girls. You look nice too."
jump endEvent

label ep12_np_smc_label:
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc9 with dissolve
    sa "Hey! What's up?"
    scene ep12_np_smc8 with dissolve
    mc "Not much. I'm looking for people to party with."
else:
    scene ep12_np_smc1 with dissolve
    sa "There's my boyfriend."
    scene ep12_np_smc2 with dissolve
    mc "I've been here all the time."
    scene ep12_np_smc3 with dissolve
    sa "Yes, but now I finally have time for you."
    scene ep12_np_smc2 with dissolve
    mc "That's great! I've been looking for people to party with."
mc "Most are starting slow tonight."
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc9 with dissolve
else:
    scene ep12_np_smc4 with dissolve
sa "Duh! Girls are all dressed in fancy dresses, and they spent hours doing their makeup."
sa "They want to look as good as they can for this party, and they won't do that if they get drunk at a quarter to seven."
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc8 with dissolve
else:
    scene ep12_np_smc2 with dissolve
mc "And what's the guys' excuse?"
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc9 with dissolve
else:
    scene ep12_np_smc4 with dissolve
sa "I assume no one wants to pass out before midnight."
sa "At a party with this many girls, there's a high chance for a midnight makeout session."
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc10 with dissolve
else:
    scene ep12_np_smc2 with dissolve
mc "I wonder what my chances are for that?"
if ep11_sage_love == 1 or RPsage < 22:
    scene ep12_np_smc17 with dissolve
    sa "Heh. Yeah!"
else:
    scene ep12_np_smc3 with dissolve
    sa "I wouldn't say 100%%, but probably close to it."
    scene ep12_np_smc2 with dissolve
    menu:
        "Love it":
            mc "I love those odds."
            scene ep12_np_smc4 with dissolve
            sa "I bet you do."
        "With you or...? \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "With you or...?"
            scene ep12_np_smc5 with dissolve
            sa "And now it's probably closer to 50%%."
scene bg anim_sage_pan_ep12 movie with dissolve
mc "I haven't had the chance to tell you this yet, but you're gorgeous tonight."
pause
scene ep12_np_smc6 with dissolve
if ep11_sage_love == 1 or RPsage < 22:
    sa "Thanks! You look good, too. Even though I know Tommy dressed you up for tonight."
else:
    sa "And you're very handsome. Even though I know Tommy dressed you up for tonight."
scene ep12_np_smc7 with dissolve
mc "He told you that?"
scene ep12_np_smc6 with dissolve
sa "He did. I thought it was a weird thing to brag about, but then it clicked..."
sa "I seriously think he likes you."
scene ep12_np_smc8 with dissolve
mc "It took him a while to get there, but I think so, too."
mc "I'm coming around on him as well."
scene ep12_np_smc9 with dissolve
sa "How so?"
scene ep12_np_smc10 with dissolve
mc "I can't tell you. It's a DIK secret code thing."
scene ep12_np_smc11 with dissolve
sa "*{i}Whispers{/i}* How is it about his diabetes?"
scene ep12_np_smc10 with dissolve
mc "You know about it?"
scene ep12_np_smc11 with dissolve
sa "Heather told me. She worries about him a lot."
sa "When they were together, she took care of him more than you'd think."
sa "It was how they got together."
scene ep12_np_smc10 with dissolve
mc "I didn't know about it until recently."
scene ep12_np_smc11 with dissolve
sa "For real?"
scene ep12_np_smc12 with dissolve
mc "Yeah. He had collapsed on the bathroom floor, and I found him in there."
mc "It could have ended badly."
scene ep12_np_smc9 with dissolve
sa "No wonder he likes you then."
scene ep12_np_smc8 with dissolve
mc "There's more to it than that. We talked after and have been bonding well this last month or so."
scene ep12_np_smc11 with dissolve
sa "I'm glad he's alright. I'm not gonna tell Heather that it happened. She'd freak out."
scene ep12_np_smc8 with dissolve
mc "Does she still care about him?"
scene ep12_np_smc11 with dissolve
sa "She pretends she doesn't, but she does."
sa "The problem is that he doesn't feel the same. Or if he does, he doesn't show it."
scene ep12_np_smc10 with dissolve
mc "He can be a shut book at times."
scene ep12_np_smc13 with dissolve
sa "Yeah, but he can't be like that with his girlfriend."
if not (ep11_sage_love == 1 or RPsage < 22):
    sa "Look at how you are. You talk to me about everything, even when I don't want you to."
    scene ep12_np_smc8 with dissolve
    if tc < 5 or persistent.no_cheater:
        mc "I try, but it's hard at times."
    else:
        mc "I don't talk to you about everything..."
    scene ep12_np_smc13 with dissolve
    sa "Tommy didn't talk about how he felt for Heather at all. I don't think he has that kind of talk in him."
    sa "Heather needs someone more affectionate. But at the same time, she needs someone like Tommy."
    sa "So, what can you do?"
scene ep12_np_smc10 with dissolve
mc "Who knows what makes a relationship work out? I couldn't tell you."
if not (ep11_sage_love == 1 or RPsage < 22):
    scene ep12_np_smc14 with dissolve
    sa "You couldn't? What about ours?"
    sa "Can you tell if it will work out?"
    if ep11_sage_love == 2:
        scene ep12_np_smc8 with dissolve
        mc "We'll make it work. I can't see a reason why it wouldn't."
        scene ep12_np_smc9 with dissolve
        sa "You're sweet, but not realistic."
        scene ep12_np_smc8 with dissolve
        mc "Why? I didn't enter our relationship thinking that it would fail."
        scene ep12_np_smc13 with dissolve
        sa "Neither did I, but couples break up for all kinds of reasons."
        sa "Let's not be naive and promise each other forever afters. Because you never know."
        scene ep12_np_smc15 with dissolve
        mc "(Maybe it has something to do with her parents' divorce...)"
        scene ep12_np_smc8 with dissolve
        mc "Well, I say we have a near 100%% chance to make it work then."
        scene ep12_np_smc18 with dissolve
        sa "*{i}Smack{/i}*"
    elif tc < 5 or persistent.no_cheater:
        if not ep9_sage_vanilla:
            scene ep12_np_smc10 with dissolve
            mc "I can't tell you that either. But I like what we have."
            mc "The sex is amazing, and we have a lot of fun."
            scene ep12_np_smc14 with dissolve
            sa "And that's enough for you?"
            scene ep12_np_smc10 with dissolve
            mc "It is for now. But I feel we're growing as a couple every day."
            mc "I'd like to see us in a year from now and see how much we have changed."
            scene ep12_np_smc9 with dissolve
            sa "I have a feeling next year will be full of challenges and surprises."
            scene ep12_np_smc18 with dissolve
            sa "*{i}Smack{/i}*"
        else:
            scene ep12_np_smc10 with dissolve
            mc "No, I can't tell that. But I can tell you that I want to make it work."
            scene ep12_np_smc9 with dissolve
            sa "I like that you have that as an ambition. That makes me feel more confident about you."
            scene ep12_np_smc10 with dissolve
            mc "Do you have doubts?"
            scene ep12_np_smc13 with dissolve
            sa "Yes, but I doubt everything. I've yet to see one relationship up close that stood the test of time."
            scene ep12_np_smc15 with dissolve
            mc "(Of course... Her parents' divorce... I'm not gonna push her on this tonight.)"
            scene ep12_np_smc8 with dissolve
            mc "Well, I say we have a near 100%% chance to make it work then."
            scene ep12_np_smc18 with dissolve
            sa "*{i}Smack{/i}*"
    else:
        scene ep12_np_smc10 with dissolve
        mc "No, I can't."
        scene ep12_np_smc14 with dissolve
        sa "But you want it to work out, right?"
        scene ep12_np_smc10 with dissolve
        mc "Uh... I have a great time with you, and you're my girlfriend."
        mc "That should tell you something."
        scene ep12_np_smc17 with dissolve
        sa "You'll have to do better than that. You're not convincing me here."
        scene ep12_np_smc12 with dissolve
        mc "What do you expect me to say?"
        scene ep12_np_smc14 with dissolve
        sa "It's an easy question, isn't it? Would you rather be single than with me?"
        scene ep12_np_smc10 with dissolve
        mc "With you."
        scene ep12_np_smc11 with dissolve
        sa "Ok."
        scene ep12_np_smc10 with dissolve
        mc "Was that better?"
        scene ep12_np_smc13 with dissolve
        sa "Yes, but I doubt everything. I've yet to see one relationship up close that stood the test of time."
        scene ep12_np_smc15 with dissolve
        mc "(Of course... Her parents' divorce...)"
        scene ep12_np_smc16 with dissolve
        mc "Don't overthink it."
else:
    scene ep12_np_smc14 with dissolve
    sa "Yeah, me neither."
    scene ep12_np_smc16 with dissolve
    mc "How have you been lately? I feel like we haven't talked much."
    scene ep12_np_smc17 with dissolve
    sa "I know. I've had a lot on my plate. Christmas, family, preparations for this party, and the next semester..."
    scene ep12_np_smc12 with dissolve
    mc "Yeah, I get it. Things should return to normal once the new semester starts."
    scene ep12_np_smc15 with dissolve
    mc "You ok?"
    scene ep12_np_smc13 with dissolve
    sa "Hm? Oh, yeah! Totally."
    scene ep12_np_smc10 with dissolve
    mc "Alright. I'm gonna mingle some more. Maybe someone wants to drink with me."
    scene ep12_np_smc9 with dissolve
    sa "Have fun!"

$ new_bio("Heather", "Sage told me that Heather still cares about Tommy.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np_s2mc_label:
scene ep12_np_s2mc1 with dissolve
mc "Hey... Can we talk?"
if "Sage" in breakup or ep4_toldDerekAboutJade:
    scene ep12_np_s2mc3 with dissolve
    sa "Why? I have nothing to say to you."
    scene ep12_np_s2mc4 with dissolve
    mc "You wanted me to bury the hatchet with Nick tonight."
    mc "Why can't you do the same with me?"
    scene ep12_np_s2mc3 with dissolve
    sa "Are you kidding me? Do you think it's remotely the same thing?"
    if ep12_break_or_tell != "break":
        sa "Don't talk to me anymore, [name]."
        sa "I don't want anything to do with you. Get that into your head."
    else:
        sa "I don't want to be around you anymore, [name]."
    scene ep12_np_s2mc4 with dissolve
    mc "But-"
    scene ep12_np_s2mc8 with dissolve
    sa "Thank fuck for this line."
    $ new_bio("Sage", "Sage didn't want to be around me anymore.")
    $ event_list.append("sage_gone")
else:
    scene ep12_np_s2mc2 with dissolve
    sa "[name], I don't know what to say to you now."
    scene ep12_np_s2mc1 with dissolve
    mc "Are we still friends? It feels like you're avoiding me."
    scene ep12_np_s2mc2 with dissolve
    sa "I am avoiding you."
    sa "I know I wasn't a part of your relationship, and you might think that I'm overreacting, but..."
    sa "...I have a hard time pretending it didn't affect me."
    scene ep12_np_s2mc1 with dissolve
    mc "How does it affect you?"
    scene ep12_np_s2mc5 with dissolve
    if branchJill:
        sa "I'm gonna ask you straight up. Did you cheat on Jill?"
    elif branchIsabella:
        sa "I'm gonna ask you straight up. Did you cheat on Bella?"
    else:
        sa "I'm gonna ask you straight up. Did you cheat on Josy and Maya?"
    scene ep12_np_s2mc6 with dissolve
    mc "It depends on how you see it."
    scene ep12_np_s2mc5 with dissolve
    sa "Anything but a plain no is an admission of guilt to me."
    scene ep12_np_s2mc6 with dissolve
    if branchZoey:
        mc "It's complicated. I didn't return to my friendship with Zoey with the intention of getting her back."
        mc "Somewhere along the line, it evolved, and before I knew it, it was too late."
        mc "We kissed and, yeah, if that's cheating... Yeah... I cheated."
        if branchJill:
            mc "I had feelings for Zoey when I was with Jill."
        elif branchIsabella:
            mc "I had feelings for Zoey when I was with Bella."
        else:
            mc "I had feelings for Zoey when I was with Josy and Maya."
    else:
        mc "I lived life as if I were single when I shouldn't have."
    scene ep12_np_s2mc5 with dissolve
    sa "Thank you for being honest. But I have a big problem with cheaters."
    if pathSage:
        sa "Call me a hypocrite if you must, but it's a dealbreaker to me."
    else:
        sa "It's a dealbreaker to me."
    scene ep12_np_s2mc7 with dissolve
    sa "I didn't think you'd do such a thing. And it made me question you."
    sa "I find it hard to stay friends with you after what you did."
    if branchMayaJosy:
        sa "And you did that to two of my friends."
    else:
        sa "And you did that to one of my friends."
    sa "That's why I'm avoiding you."
    scene ep12_np_s2mc6 with dissolve
    mc "I'm sorry..."
    if branchZoey:
        mc "I'm in love with Zoey. I should have handled it better... And I regret what I did, but not what I chose."
    else:
        mc "I should have acted better... And I regret what I did."
    scene ep12_np_s2mc5 with dissolve
    sa "*{i}Sigh{/i}* Take care of yourself, [name]."
    if branchZoey:
        sa "I find comfort in that you're happy."
    scene ep12_np_s2mc6 with dissolve
    mc "I miss you."
    scene ep12_np_s2mc7 with dissolve
    sa "I miss you too."
    $ new_bio("Sage", "Sage told me she had a problem with cheaters and had been avoiding me lately. She missed me, but said it was hard to stay friends with me.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np_s3mc_label:
scene ep12_np_s3mc1 with dissolve
sa "Alright, catch me up. What did I miss?"
if jade_state > 0:
    scene ep12_np_s3mc2 with dissolve
    mc "Not much is going on."
    scene ep12_np_s3mc1 with dissolve
    sa "No? What about you? What are you up to?"
    scene ep12_np_s3mc3 with dissolve
    mc "Not much either..."
    scene ep12_np_s3mc4 with dissolve
    sa "Ok..."
    sa "Wanna have a drink together or something?"
    scene ep12_np_s3mc3 with dissolve
    mc "Nah, I'm good. I'm gonna work the room some more."
    scene ep12_np_s3mc4 with dissolve
    sa "Have fun..."
    scene ep12_np_s3mc5 with dissolve
    mc "(I hate this...)"
    $ new_bio("Sage", "I tried to distance myself from Sage. It was hard.")
else:
    scene ep12_np_s3mc2 with dissolve
    mc "Haven't you been here the whole time?"
    scene ep12_np_s3mc1 with dissolve
    sa "Yes, but now I'm finally free of my chores for tonight."
    scene ep12_np_s3mc2 with dissolve
    mc "That's great! Um... I don't think you missed much."
    mc "You're aware of the line, and so far, there's been little to no drama."
    scene ep12_np_s3mc1 with dissolve
    sa "We're off to a great start. And what have you been up to?"
    scene ep12_np_s3mc6 with dissolve
    mc "I've been looking for people to party with."
    mc "Most are starting slow tonight."
    scene ep12_np_s3mc7 with dissolve
    sa "Duh! Girls are all dressed in fancy dresses, and they spent hours doing their makeup."
    sa "They want to look as good as they can for this party, and they won't do that if they get drunk at a quarter to seven."
    scene ep12_np_s3mc6 with dissolve
    mc "And what's the guys' excuse?"
    scene ep12_np_s3mc7 with dissolve
    sa "I assume no one wants to pass out before midnight."
    sa "At a party with this many girls, there's a high chance for a midnight makeout session."
    scene ep12_np_s3mc6 with dissolve
    mc "I wonder what my chances are for that?"
    scene ep12_np_s3mc8 with dissolve
    if branchIsabella:
        sa "*{i}Whispers{/i}* If you find somewhere private to sneak off with her, I'm sure Bella will kiss you."
        scene ep12_np_s3mc6 with dissolve
        mc "Hm... She's a chaperone tonight. I shouldn't risk it."
        scene ep12_np_s3mc8 with dissolve
        sa "Like I said, sneak off with her. She'll love it."
        scene ep12_np_s3mc6 with dissolve
    elif branchMayaJosy:
        sa "200%% since you get to make out with two girls."
        scene ep12_np_s3mc6 with dissolve
        mc "Yeah, we'll see."
        scene ep12_np_s3mc9 with dissolve
        sa "Aren't things good between you guys?"
        scene ep12_np_s3mc10 with dissolve
        mc "We've had many ups and downs. It's hard to know at times what's on everyone's mind."
        mc "Sometimes, it's hard for me to understand girls, and with them, I have to figure out two at once."
        scene ep12_np_s3mc9 with dissolve
        sa "No offense to you three, but I wouldn't want to be in that kind of a relationship."
        sa "I don't think I have what it takes to share a guy with another girl."
        scene ep12_np_s3mc11 with dissolve
        sa "And I mean emotionally. Sexually, that's a different story. That's just fun."
        scene ep12_np_s3mc10 with dissolve
        mc "Yeah, it's way different dealing with emotions."
        mc "When we're not in bed together, it's been harder to get along."
        mc "And it's been easier for me to hang out with one of them at the time."
        scene ep12_np_s3mc9 with dissolve
        sa "Why do you think that is?"
        scene ep12_np_s3mc10 with dissolve
        mc "I have no clue. We're good together, too, but that's usually when the friction happens."
        scene ep12_np_s3mc9 with dissolve
        sa "Is it friction between you and them or between them?"
        scene ep12_np_s3mc10 with dissolve
        mc "Between them..."
        mc "They've known each other for much longer than I have. So, I guess they are more comfortable speaking their mind and arguing."
        scene ep12_np_s3mc11 with dissolve
        sa "No relationship is perfect."
        scene ep12_np_s3mc10 with dissolve
        if tc > 4 and not persistent.no_cheater:
            mc "I know. And I'm nowhere near perfect either..."
            mc "Frankly, I... I have doubts."
            mc "I should talk with them about this, not you."
            scene ep12_np_s3mc9 with dissolve
            sa "Sounds like it."
        else:
            mc "Wouldn't it be nice if it were?"
            scene ep12_np_s3mc11 with dissolve
            sa "Amen."
        scene ep12_np_s3mc6 with dissolve
    else:
        sa "It has to be at least 50%%. Many girls at the party are single."
        sa "Sure, you've got some healthy competition for them. But if you lock in early, your chances should improve."
        scene ep12_np_s3mc6 with dissolve
        if branchZoey:
            mc "I just started a relationship."
            scene ep12_np_s3mc13 with dissolve
            sa "You haven't told me that. With who?"
            scene ep12_np_s3mc6 with dissolve
            mc "Zoey."
            scene ep12_np_s3mc9 with dissolve
            sa "Zoey? Wow... Are you going back to your ex?"
            scene ep12_np_s3mc14 with dissolve
            mc "Yeah. We feel the same about each other."
            scene ep12_np_s3mc7 with dissolve
            sa "Congratulations. That's huge."
            scene ep12_np_s3mc6 with dissolve
            mc "Thank you."
        else:
            mc "Maybe I will."
            scene ep12_np_s3mc6 with dissolve

    mc "What about you? Who are you kissing at midnight?"
    scene ep12_np_s3mc9 with dissolve
    sa "It's...complicated."
    scene ep12_np_s3mc10 with dissolve
    mc "Oh? So, there is someone?"
    scene ep12_np_s3mc11 with dissolve
    sa "Not that complicated."
    sa "I know everyone at this party. The jocks... You know, with Chad and all..."
    sa "I've looked at the rest of them as my friends, and that made me lose all interest."
    scene ep12_np_s3mc9 with dissolve
    sa "And with the DIKs, there's not much potential for me."
    scene ep12_np_s3mc19 with dissolve
    if branchAlone and not branchZoey:
        sa "I mean, you friend-zoned me."
    else:
        sa "Besides, the best one is already taken."
    scene ep12_np_s3mc11 with dissolve
    sa "The rest of the guys are, eh..."
    sa "Also, there's something else on my mind."
    scene ep12_np_s3mc10 with dissolve
    mc "I'm all ears."
    scene ep12_np_s3mc12 with dissolve
    sa "The next semester is my last one at B&R..."
    sa "Who knows what I'll do after that? Maybe I'll move away for work or continue my studies somehow..."
    sa "I'm close to the finish line, but I haven't figured that part out yet."
    scene ep12_np_s3mc9 with dissolve
    sa "Finding a guy right now would be the worst thing that could happen to me."
    sa "What I need now is to focus on the last stretch. And I don't want to be tied down after because it would limit my choices."
    scene ep12_np_s3mc10 with dissolve
    mc "Sage... We're talking about a midnight kiss, not a midnight boyfriend."
    scene ep12_np_s3mc11 with dissolve
    sa "You never know how those things go. Maybe it starts with a kiss and ends with a relationship."
    sa "That would be detrimental to me."
    scene ep12_np_s3mc10 with dissolve
    mc "Those are some harsh words. Will you ever have time for it if that's how you think about relationships?"
    scene ep12_np_s3mc12 with dissolve
    sa "It's selfish, I know. But I think that's what I need to be right now."
    sa "That's why a midnight kiss is 100%% out of the question."
    scene ep12_np_s3mc14 with dissolve
    mc "So, your New Year's resolution is basically to abstain from men for six months."
    scene ep12_np_s3mc15 with dissolve
    sa "Hahaha! I guess it is."
    scene ep12_np_s3mc6 with dissolve
    mc "That's the worst thing I've ever heard."
    mc "I mean, I would be able to go a whole year without fucking a guy. Hey, make it ten years! But for you...?"
    scene ep12_np_s3mc15 with dissolve
    sa "Hahaha! Stop it."
    sa "Sex for fun would be ok. But finding someone who would be ok with that without getting feelings for me is borderline impossible."
    scene ep12_np_s3mc6 with dissolve
    mc "It sounds tricky, yeah. You're a lovable girl."
    scene ep12_np_s3mc16 with dissolve
    sa "If I could find a couple who wouldn't mind a third for a change, it would work."
    if branchAlone or branchZoey:
        scene ep12_np_s3mc6 with dissolve
        mc "Haha, good luck on your hunt."
        mc "I'm gonna work the room some. Let's chat later!"
    else:
        if branchMayaJosy:
            sa "Or maybe a fourth?"
            scene ep12_np_s3mc6 with dissolve
            mc "I'll run it by them."
        else:
            scene ep12_np_s3mc6 with dissolve
            mc "I'll run it by her."
        scene ep12_np_s3mc7 with dissolve
        sa "Haha! I'm joking."
        scene ep12_np_s3mc6 with dissolve
        mc "No, you're not."
        scene ep12_np_s3mc13 with dissolve
        sa "I wouldn't do that to your relationship."
        scene ep12_np_s3mc17 with dissolve
        $ renpy.pause()
        scene ep12_np_s3mc18 with dissolve
        sa "I think it's time to end this conversation now that you got all awkward about that thought."
        scene ep12_np_s3mc17 with dissolve
        mc "Haha, yeah."
        scene ep12_np_s3mc8 with dissolve
        if branchMayaJosy:
            sa "But maybe I'll talk to Josy and Maya about it."
        elif branchJill:
            sa "But maybe I'll talk to Jill about it."
        else:
            sa "But maybe I'll talk to Bella about it."
        scene ep12_np_s3mc6 with dissolve
        mc "You're not gonna last six months, Sage."
        mc "You're already horny, and it's not even January 1st."
    $ new_bio("Sage", "Sage told me about her concerns regarding dating someone this close to completing her studies. She didn't want to be tied down after college.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np_dinner_label:
scene ep12_np_dinner1 with dissolve
mc "Rio? You came."
scene ep12_np_dinner2 with dissolve
ri "Surprised?"
scene ep12_np_dinner1 with dissolve
mc "Very. In a good way."
if ep12_riona_side == "Riona" or wt_ep11_quinn_riona_question:
    scene ep12_np_dinner3 with dissolve
    mc "I'm so happy to see you."
scene ep12_np_dinner4 with dissolve
ri "Be honest with me... How do I look? Can you notice the scars and bruises?"
scene ep12_np_dinner5 with dissolve
mc "Um... You look a lot better than the last time I saw you. You'll be fine."
scene ep12_np_dinner4 with dissolve
ri "But you can still tell, can't you?"
scene ep12_np_dinner6 with dissolve
mc "I wish I could tell you no, but I can't lie to you. They'll notice that you're not wearing any piercings, if nothing else."
mc "But the makeup looks great. I can't tell that you're bruised."
scene ep12_np_dinner4 with dissolve
ri "It hurt like hell to put on all that makeup."
ri "But I sat at home thinking about tonight, and I didn't want to miss it."
scene ep12_np_dinner7 with dissolve
ri "After all, what is a few days extra? I'll have to return to school soon anyway."
ri "This way, I get the chance to talk and explain myself to people in private."
scene ep12_np_dinner6 with dissolve
mc "Everyone will love that you came."
scene ep12_np_dinner7 with dissolve
ri "Quinn probably won't, but the rest will. I chatted some with them earlier this week about it."
scene ep12_np_dinner6 with dissolve
mc "That's good. You have our support, Rio."
if ep12_riona_side == "Riona" or wt_ep11_quinn_riona_question:
    scene ep12_np_dinner8 with dissolve
    ri "I take great comfort in knowing you're on my side."
    ri "You're the only one who knows the truth."
    scene ep12_np_dinner9 with dissolve
    mc "Call on me if you need anything."
    scene ep12_np_dinner8 with dissolve
    ri "I will."
else:
    scene ep12_np_dinner4 with dissolve
    ri "Mhm..."
ri "I'm gonna have to lie like never before."
scene ep12_np_dinner6 with dissolve
mc "What will you say?"
scene ep12_np_dinner7 with dissolve
ri "I'm gonna blame it on an infection and allergies."
ri "I'll say that I developed some allergy to my piercings, and that's why I had to remove them. Which led to scarring and such."
scene ep12_np_dinner6 with dissolve
mc "That could work."
mc "And how will you handle Quinn?"
scene ep12_np_dinner4 with dissolve
ri "We'll see. I hope she stays away from me."
scene ep12_np_dinner10 with dissolve
ri "Fuck... Did you seat me at her table?"
mc "Oh? No, that wasn't me..."
mc "That's bad planning, but they couldn't have known."
scene ep12_np_dinner4 with dissolve
ri "I'm not gonna sit next to her and have dinner. Maybe I should leave..."
scene ep12_np_dinner6 with dissolve
mc "No, no, no. You don't have to leave. I can fix this."
scene ep12_np_dinner11 with dissolve
play sound "sound_effects/season3/pen_writing.mp3"
mc "Let's move this Leanne girl to your spot, and you to her spot."
ri "I'd rather not sit with the jocks at all."
scene ep12_np_dinner12 with dissolve
play sound "sound_effects/season3/pen_writing.mp3"
mc "Yeah, who would? In that case, let's get rid of Becky while we're at it and move you to her spot."
mc "Hey, this plan is even better than the first one."
scene ep12_np_dinner9 with dissolve
mc "You'll sit with John Boy, Maya, and Jill. You'll have a great time with them, I'm sure."
scene ep12_np_dinner8 with dissolve
ri "Thank you, [name]."

scene ep12_np_dinner13 with dissolve
cam "Oh my God! It's true! You came!!!"
scene ep12_np_dinner14 with dissolve
ri "I've missed you, Cammy."
scene ep12_np_dinner15 with dissolve
cam "I'm going to ruin my makeup crying, but it's worth it."
$ new_bio("Riona", "Riona showed up at the New Year's Eve party. She had tried to hide her scars and bruises as best she could.")

scene ep12_np_dinner16 with dissolve
dwy "[name]! Looking slick!"
play sound "sound_effects/season2/fistbump.mp3"
scene ep12_np_dinner17 with hpunch
mc "Hey, guys. Welcome."
play sound "sound_effects/season2/fistbump.mp3"
scene ep12_np_dinner18 with hpunch
chao "[name]! This party seems promising. Red carpet and all."
if ep10_troy_mad:
    scene ep12_np_dinner19 with dissolve
    mc "(He invited Troy? Oh, well... I bet the jocks will hate that more than me.)"
else:
    scene ep12_np_dinner20 with dissolve
    mc "Troy! Cool that you came. Um... The jocks are on that side of the party, but you'll sit with us."
    scene ep12_np_dinner21 with dissolve
    troy "Thanks for the invite. I'll be ok."
scene ep12_np_dinner22 with dissolve
mc "Micha? Are you with them?"
scene ep12_np_dinner23 with dissolve
dwy "You know my girl? Haha! She mentioned she knew people at the party, and now I get what she meant."
scene ep12_np_dinner22 with dissolve
mc "She's your girl? Uh..."
mc "She's your girl! Of course."
scene ep12_np_dinner24 with dissolve
le "Dinner time, everyone. Check the seating plan and get to your table."
scene ep12_np_dinner22 with dissolve
mc "Uh... Have a look around. The seating plan is on the wall, and the dining room is behind you."
mc "The party is everywhere on this floor. Feel like home, ok? I need to do something."
scene ep12_np_dinner25 with dissolve
mc "Rusty. Quick. Over here."
scene ep12_np_dinner26 with dissolve
rs "I can't right now, [name]. The dinner is about to start."
scene ep12_np_dinner25 with dissolve
mc "This is high priority; trust me."
scene ep12_np_dinner27 with dissolve
mc "Micha is here with her boyfriend."
scene ep12_np_dinner28 with dissolve
rs "With her boyfriend!?"
scene ep12_np_dinner27 with dissolve
mc "Turns out, her boyfriend is my trainer and friend Dwyane."
mc "And I invited him and some friends to the party."
scene ep12_np_dinner29 with dissolve
rs "Fuck! Ok, ok... Uh... I can't deal with that right now, but thanks for the info."
rs "Dwyane... Can you point him out to me?"
scene ep12_np_dinner30 with dissolve
mc "He's the guy with his hand on her ass..."
if ep11_rusty_choice:
    mc "I warned you this was a bad choice."
    scene ep12_np_dinner28 with dissolve
    rs "I'm not the one who invited her boyfriend."
    scene ep12_np_dinner27 with dissolve
    mc "Dude, you don't know what you're saying. I'm not taking the blame for this one."
    mc "You put me in a weird spot tonight, too."
    mc "I came to warn you about it. What you do from here on is up to you."
else:
    scene ep12_np_dinner28 with dissolve
    rs "This is bad... Why did you invite him?"
    scene ep12_np_dinner27 with dissolve
    mc "He's my friend. I didn't know Micha was his girlfriend."
    scene ep12_np_dinner29 with dissolve
    rs "I'll handle it."

if branchZoey:
    scene ep12_np_dinner31 with dissolve
    zo "Couldn't you have seated me next to you at dinner?"
    if breakup:
        scene ep12_np_dinner32 with dissolve
        if ep4_toldDerekAboutJade:
            mc "At least we're in the same room."
        else:
            mc "I think you're lucky to be seated at an actual table, if I'm honest."
        scene ep12_np_dinner33 with dissolve
        zo "I take it you weren't in charge of it."
        scene ep12_np_dinner34 with dissolve
        mc "No. Who's at your table?"
    else:

        scene ep12_np_dinner32 with dissolve
        mc "I had nothing to do with the seating plans. Will you be alright?"
        scene ep12_np_dinner33 with dissolve
        zo "I'm not a stranger to talking to randoms."
        scene ep12_np_dinner34 with dissolve
        mc "Who's at your table?"
    scene ep12_np_dinner33 with dissolve
    zo "Chao, Tommy, and Lily."
    scene ep12_np_dinner34 with dissolve
    mc "Not a bad table. You'll hear stories, I'm sure."
    scene ep12_np_dinner35 with dissolve
    zo "*{i}Smack{/i}*"

scene ep12_np_dinner36 with dissolve
$ renpy.pause()
scene ep12_np_dinner37 with dissolve
mc "(And suddenly, I understand why Sage put both of them at my table...)"
mc "(Fuck, Rusty... Why did you have to do this to me?)"
if ep11_rusty_choice:
    mc "(I warned you...)"
scene ep12_np_dinner38 with dissolve
mc "(Dwyane is such a great guy, too.)"
if ep11_quinn_question[0] and ep11_quinn_question[1] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch and (not branchZoey or wt_ep11_zoey_kiss_others):
    scene ep12_np_dinner39 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner40 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner41 with dissolve
    $ renpy.pause()

scene ep12_np_dinner42 with dissolve
sy "Hello to you too."
scene ep12_np_dinner43 with dissolve
mc "Sally... I didn't see you there."
scene ep12_np_dinner44 with dissolve
sy "I'm not THAT short."
scene ep12_np_dinner43 with dissolve
mc "You look nice tonight."
scene ep12_np_dinner42 with dissolve
sy "As do you."
scene ep12_np_dinner45 with dissolve
dwy "Looks like we got a winner table for the dinner, yeah?"
scene ep12_np_dinner46 with dissolve
mc "Yeah... The best."
scene ep12_np_dinner45 with dissolve
dwy "Sage even spelled my name right. I'm amazed; most get it wrong."

scene ep12_np_dinner47 with dissolve
che "Hey! [name]?"
scene ep12_np_dinner48 with dissolve
mc "What?"
scene ep12_np_dinner47 with dissolve
che "Mission accomplished."
scene ep12_np_dinner48 with dissolve
mc "It was?"
scene ep12_np_dinner49 with dissolve
if ep12_mean_prank:
    ma "The silverware is now brownware."
else:
    ma "Two lovebirds will meet at midnight."

scene ep12_np_dinner49b with dissolve
che "Also... Here. We got you some HOT panties."
scene ep12_np_dinner49c with dissolve
mc "Put those away!"
scene ep12_np_dinner48 with dissolve
mc "I can't believe you got those..."
scene ep12_np_dinner47 with dissolve
che "It was easy! We just asked Arieth for hers. She didn't even question why we wanted them."
che "Let us know when you have another mission for us."
scene ep12_np_dinner45 with dissolve
dwy "What was that about?"
scene ep12_np_dinner46 with dissolve
mc "Frat things... You don't want to know."

play sound "sound_effects/season3/glass_clink.mp3"
scene ep12_np_dinner50 with dissolve
"*{i}Clink clink clink{/i}*"
scene ep12_np_dinner51 with dissolve
rs "Welcome to our New Year's Eve party. I'm thrilled to have you all here."
scene ep12_np_dinner53 with dissolve
mc "(Starting with a lie. Nice...)"
if maya_shiny_dress:
    scene ep12_np_dinner54 with dissolve
else:
    scene ep12_np_dinner54b with dissolve
rs "You all look beautiful tonight. And I bet it's refreshing to be at one of our parties wearing clothes."
rs "Thanks for that one, [name]. Glad you could make it happen."
scene ep12_np_dinner53 with dissolve
"*{i}Laughter{/i}*"
mc "(Not my original idea, but sure.)"
scene ep12_np_dinner103 with dissolve
sa "Enjoy as much of the buffet as you'd like. There should be something in there for everyone."
sa "If you have any food allergies, you'll find your food at the table to the right."
scene ep12_np_dinner104 with dissolve
sa "You'll find the bathrooms in dining hall A..."
scene ep12_np_dinner52 with dissolve
rs "...and the dance floor is outside to the left. I'm sure you haven't missed it."
rs "Come midnight, you can watch the fireworks from outside, or if you'd rather watch from the balcony, that's fine too."
scene ep12_np_dinner51 with dissolve
rs "I know I speak for all of my brothers when I say: have a great end to the year, we're excited to end it together with you!"
rs "Cheers and enjoy!"

if ep12_mean_prank:
    scene ep12_np_dinner105 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner106 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner107 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner113 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner112 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner110 with dissolve
    dw "I think the nut-flavored beef tastes weird."
    scene ep12_np_dinner111 with dissolve
    gi "Nut flavored? Mine tastes nothing like that."
    scene ep12_np_dinner108 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner109 with dissolve
    $ renpy.pause()
else:
    scene ep12_np_dinner116 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner115 with dissolve
    $ renpy.pause()
    scene ep12_np_dinner114 with dissolve
    $ renpy.pause()

scene ep12_np_dinner55 with dissolve
if ep12_pp_food == 0:
    dwy "Amazing food, [name]! But I could do without the balloons."
elif ep12_pp_food == 1:
    dwy "Great food, [name]. But I could do without the balloons."
else:
    dwy "Homemade food, huh? It's alright, but I could do without the balloons."
scene ep12_np_dinner56 with dissolve
mc "Haha! Yeah, they obscure the view, don't they?"
scene ep12_np_dinner55 with dissolve
dwy "Did you spend all night and day in the kitchen cooking or what?"
scene ep12_np_dinner56 with dissolve
mc "Yeah. One of my secret talents is cooking for 100 guests."
scene ep12_np_dinner65 with dissolve
sy "Wow, are we that many?"
scene ep12_np_dinner66 with dissolve
mc "It's something close to it, yeah."
scene ep12_np_dinner55 with dissolve
dwy "I don't know many here, but you all seem like a friendly bunch."
dwy "So, [name]. How do you know Micha?"
scene ep12_np_dinner56 with dissolve
mc "*{i}Cough cough{/i}*"
scene ep12_np_dinner55 with dissolve
dwy "No rush, bro. Swallow before you talk."
scene ep12_np_dinner78 with dissolve
mc "Micha, you can take this one."
scene ep12_np_dinner79 with dissolve
mic "From parties."
scene ep12_np_dinner59 with dissolve
dwy "I get it. These are the people you spend your weekends with, yeah?"
dwy "She's funny. There's always a party in college, I hear."
scene ep12_np_dinner56 with dissolve
mc "Not every weekend. We study too."
scene ep12_np_dinner55 with dissolve
dwy "That red-haired guy with the speech seems cool. Is he in your frat?"
scene ep12_np_dinner56 with dissolve
mc "Yep. That's Rusty, he's the president of the DIKs."
scene ep12_np_dinner59 with dissolve
dwy "Oh! So, that's why he held a speech."
dwy "Then, you probably know him, Micha."
scene ep12_np_dinner79 with dissolve
mic "I know him, yeah. We study together sometimes."
scene ep12_np_dinner60 with dissolve
dwy "Huh? Is he a president and a sophomore like you?"
scene ep12_np_dinner79 with dissolve
mic "No, but we have one class together."
scene ep12_np_dinner80 with dissolve
mc "(They haven't... She lies well, though.)"
scene ep12_np_dinner56 with dissolve
mc "How did you two meet?"
$ guideSuggestedPage = 262
scene ep12_np_dinner57 with dissolve
dwy "We met at a party, like two years ago."
dwy "I went to the party with two friends, and I saw her there sitting on a couch nursing a drink."
scene ep12_np_dinner55 with dissolve
dwy "We flirted a bit, and I asked for her digits. The rest is history."
scene ep12_np_dinner76 with dissolve
sy "Have you been together for two years? That's nice."
scene ep12_np_dinner61 with dissolve
dwy "Ehhhh... Not two years straight."
dwy "[name] knows the story... It's how do you call it...?"
scene ep12_np_dinner62 with dissolve
menu:
    "Don't feel ashamed":
        mc "You don't have to feel ashamed about it."
        mc "The past is the past, right?"
        scene ep12_np_dinner57 with dissolve
        dwy "You know what? You're right."
        dwy "I was a dickhead back then, looking for fights."
        scene ep12_np_dinner59 with dissolve
        dwy "And Micha, she sorted me out. We've been together, we've been apart..."
        dwy "But now we're tighter than ever. Right, babe?"
        scene ep12_np_dinner81 with dissolve
        mic "Super-tight."
        scene ep12_np_dinner80 with dissolve
        mc "(Super-liar.)"
    "Personal":
        mc "It's personal."
        scene ep12_np_dinner61 with dissolve
        dwy "It's not that I don't want to share it, but that guy I was..."
        dwy "I'm not him anymore."
        scene ep12_np_dinner75 with dissolve
        sy "Oh, I see."
scene ep12_np_dinner63 with dissolve
dwy "What about you two? You look like a fine couple."
scene ep12_np_dinner75 with dissolve
sy "Us? You mean, me and [name]?"
scene ep12_np_dinner56 with dissolve
mc "Yeah, we're not a couple."
if branchZoey:
    mc "I'm in a relationship, though. I'll introduce you later if you want."
    scene ep12_np_dinner55 with dissolve
    dwy "Yeah, I gotta meet the girl making my boy happy."
elif branchAlone or breakup:
    mc "I'm single."
else:
    if branchIsabella:
        mc "I'm in a relationship, though."
    else:
        mc "I'm in a relationship, though. I'll introduce you later if you want."
        scene ep12_np_dinner55 with dissolve
        dwy "Yeah, I gotta meet the girl making my boy happy."
    if branchMayaJosy:
        scene ep12_np_dinner56 with dissolve
        menu:
            "Sure":
                mc "Sure."
            "Girls":
                mc "Girls."
                scene ep12_np_dinner57 with dissolve
                dwy "'Scuse me?"
                scene ep12_np_dinner56 with dissolve
                mc "We'll talk."
scene ep12_np_dinner63 with dissolve
dwy "Damn. Shame about you. You two have a good fit."
scene ep12_np_dinner67 with dissolve
$ renpy.pause()
scene ep12_np_dinner73 with dissolve
mc "Hahaha!"
sy "HAH!"
scene ep12_np_dinner55 with dissolve
dwy "Something funny about that?"
scene ep12_np_dinner73 with dissolve
sy "Yeah. If you knew how we didn't get along this semester, you'd laugh too."
scene ep12_np_dinner67 with dissolve
mc "Yeah... Sally used to be a...um..."
scene ep12_np_dinner72 with dissolve
sy "I wasn't a bitch."
scene ep12_np_dinner67 with dissolve
mc "That's not the word I tried to substitute."
mc "...difficult person."
scene ep12_np_dinner72 with dissolve
sy "A pain in the ass, huh?"
scene ep12_np_dinner64 with dissolve
dwy "Hahaha! What happened?"
scene ep12_np_dinner72 with dissolve
sy "Everything about [name] used to annoy me."
scene ep12_np_dinner67 with dissolve
mc "What did I even do?"
scene ep12_np_dinner70 with dissolve
sy "Ehh..."
scene ep12_np_dinner66 with dissolve
mc "See! You don't even know."
mc "I'll tell you what the problem was. It was you."
scene ep12_np_dinner71 with dissolve
sy "Me!?"
scene ep12_np_dinner67 with dissolve
mc "You had an attitude toward me, and I think that's what started everything."
mc "Then we were forced to work together in our science class, and we both found out the other one wasn't that bad."
scene ep12_np_dinner63 with dissolve
dwy "From enemy to friend. That's nice!"
scene ep12_np_dinner75 with dissolve
sy "I wouldn't call him a friend..."
scene ep12_np_dinner67 with dissolve
mc "Wouldn't you?"
scene ep12_np_dinner70 with dissolve
sy "You'd call me a friend?"
scene ep12_np_dinner68 with dissolve
mc "I would."
mc "Friends can fight. But yeah, you're my friend."
scene ep12_np_dinner69 with dissolve
$ renpy.pause()
scene ep12_np_dinner55 with dissolve
dwy "She liked that."
scene ep12_np_dinner76 with dissolve
sy "Oh, shut up."
scene ep12_np_dinner55 with dissolve
dwy "And I see what you mean about that attitude."
scene ep12_np_dinner74 with dissolve
mc "Right?"

if ep12_brawler_comp_won:
    scene ep12_np_dinner55 with dissolve
    dwy "Did you make up your mind on that deal yet?"
    scene ep12_np_dinner56 with dissolve
    mc "No... I haven't. But I've stared at her card, thinking I should contact her."
    scene ep12_np_dinner55 with dissolve
    dwy "You should."
    scene ep12_np_dinner65 with dissolve
    sy "What's the deal?"
    scene ep12_np_dinner63 with dissolve
    dwy "This guy is one hell of a fighter. He got scouted by an agency after winning a fight a few days ago."
    dwy "He can have it all. A trainer, a gym, a career... But he's too much of a chicken to go through with it."
    scene ep12_np_dinner56 with dissolve
    mc "I already have a trainer and a gym."
    scene ep12_np_dinner57 with dissolve
    dwy "It's a career, bro. You've got talent. Don't waste your potential."
    scene ep12_np_dinner56 with dissolve
    mc "But I also have college, classes, a life, and..."
    scene ep12_np_dinner58 with dissolve
    dwy "Excuses."
    dwy "The only good reason to pass on this is if you don't want the opportunity at all."
    dwy "You use the excuses as a shield. You either want it or you don't. Which is it?"
    scene ep12_np_dinner56 with dissolve
    mc "I don't know yet."
    scene ep12_np_dinner58 with dissolve
    dwy "You're scared. And that's fine."
    scene ep12_np_dinner56 with dissolve
    mc "I'm not scared to fight."
    scene ep12_np_dinner57 with dissolve
    dwy "Not to fight. To take the leap. That's why you make those excuses."
    scene ep12_np_dinner56 with dissolve
    mc "*{i}Sigh{/i}* I don't know. Maybe that's it..."
scene ep12_np_dinner82 with dissolve
mic "What's everyone's New Year's resolution? Do you have any?"
scene ep12_np_dinner77 with dissolve
sy "I haven't had one since I was a kid. I was never any good at keeping them."
scene ep12_np_dinner63 with dissolve
dwy "Don't promise to go to the gym a lot. The January surge of people is coming..."
dwy "It gets so crowded that you can't work out during rush hours."
scene ep12_np_dinner75 with dissolve
sy "You don't have to worry about that. I avoid the gym like the plague."
sy "Hm... If I had to make a resolution, it would be to read more."
scene ep12_np_dinner66 with dissolve
mc "We read every day. How much more do you want to read?"
scene ep12_np_dinner65 with dissolve
sy "I want to read more fiction and not just class literature."
sy "I think I've read like five books this year."
sy "And that was during the summer. I barely read anything during semesters."
scene ep12_np_dinner64 with dissolve
dwy "That's five more books than I read."
scene ep12_np_dinner79 with dissolve
mic "Maybe that should be your promise too."
scene ep12_np_dinner59 with dissolve
dwy "Nah! My resolution is to do more cardio."
scene ep12_np_dinner56 with dissolve
mc "More gym? That one will be easy for you."
scene ep12_np_dinner55 with dissolve
dwy "I hope so. If your resolution is simple, it's easier to complete it."
scene ep12_np_dinner56 with dissolve
mc "In that case, I promise I'll stop smoking."
scene ep12_np_dinner65 with dissolve
sy "Do you smoke?"
scene ep12_np_dinner66 with dissolve
mc "Nope."
scene ep12_np_dinner73 with dissolve
sy "Haha! You're such a wise-ass!"

if maya_shiny_dress:
    scene ep12_np_dinner83 with dissolve
else:
    scene ep12_np_dinner83b with dissolve
my "And that's about it. Aside from the finals, I bet you didn't miss too much."
scene ep12_np_dinner85 with dissolve
ji "I'm happy you got help with postponing your tests."
scene ep12_np_dinner89 with dissolve
ri "I know what I'll be doing tomorrow. I shouldn't even be here; I should be at home, buried in books."
if maya_shiny_dress:
    scene ep12_np_dinner83 with dissolve
else:
    scene ep12_np_dinner83b with dissolve
my "I think you made the right call to come here. One night off won't hurt you."
scene ep12_np_dinner88 with dissolve
jb "What happened to your piercings?"
scene ep12_np_dinner90 with dissolve
ri "Um... When I was sick, I got infections from my jewelry."
ri "My eye got inflamed, and the skin reacted badly to my piercings."
ri "I had to get them removed, but it was too late to avoid scarring."
scene ep12_np_dinner86 with dissolve
ji "Are you allergic to nickel?"
scene ep12_np_dinner91 with dissolve
ri "Yeah. I must have gotten it late in life. It's the weirdest thing."
if maya_shiny_dress:
    scene ep12_np_dinner84 with dissolve
else:
    scene ep12_np_dinner84b with dissolve
my "I always thought your jewelry was silver."
scene ep12_np_dinner87 with dissolve
ji "I believe some can contain nickel, even so."
scene ep12_np_dinner91 with dissolve
ri "Either way... I hope it heals fast."

scene ep12_np_dinner92 with dissolve
jy "Damn, that bitch talks on inhale and exhale."
scene ep12_np_dinner94 with dissolve
jo "Who?"
scene ep12_np_dinner93 with dissolve
jy "Becky! How the fuck did she end up at my table? I thought I was going to sit with Leanne..."
if ep12_mean_prank:
    jy "It's not enough that the dinner tasted like shit; I had to spend it with Becky."
jy "It sucks! I've had my eyes on Leanne for a month."
scene ep12_np_dinner95 with dissolve
jo "I wish I knew, but the seating plans are over there... I dare you to cross the line and take a look at them."
scene ep12_np_dinner97 with dissolve
jy "Nah... Dawe will scold me if I do. He's been so pissy lately."
scene ep12_np_dinner96 with dissolve
jo "The competition means a lot to him. You'll understand it if we lose it."
scene ep12_np_dinner102 with dissolve
jy "What's he doing here?"
jo "We sure as hell didn't invite him."
scene ep12_np_dinner98 with dissolve
jy "He's on their side of the party..."
scene ep12_np_dinner99 with dissolve
jo "How are we gonna handle this one? Dawe will be pissed off that he's here."
scene ep12_np_dinner98 with dissolve
jy "Let's pretend we didn't see him."
scene ep12_np_dinner99 with dissolve
if ep12_mean_prank:
    jo "That works for me."
else:
    jo "That works for me. I don't plan to fight tonight. I've got a hookup at midnight."
    scene ep12_np_dinner101 with dissolve
    jy "Bullshit!"
    scene ep12_np_dinner100 with dissolve
    jo "Nah! She wants me."

$ freeRoamID = "ep12_3b"
$ event_list = []
$ event_list.append("ep12_np_dj_label")
$ event_list.append("key")
$ event_list.append("table")
$ event_list.append("part2")
$ firstTimeFreeRoam = True
$ currentFreeRoamLabel = "ep12_np_dining_label"
$ new_bio("Rusty", "Rusty has been cheating with Micha on my friend Dwyane.")
$ new_bio("Micha", "Micha has been cheating on Dwyane with Rusty.")
$ new_bio("Sally", "Sally was pleased when she realized that I thought of her as my friend.")

jump endEvent

label ep12_np2_jaj_label:
scene ep12_np2_jaj1 with dissolve
al "You're joking! 30-40%% of guys have issues with premature ejaculation?"
al "That means that four out of ten guys cum within a minute!"
scene ep12_np2_jaj2 with dissolve
jo "I swear to God! It's true!"
scene ep12_np2_jaj6 with dissolve
jm "Yeah. Lasting long with girls is different from lasting long when you're alone and stroking it."
jm "It doesn't have to mean that you cum in a minute; sometimes, a stroke from the girl is all it takes."
scene ep12_np2_jaj3 with dissolve
"..."
scene ep12_np2_jaj8 with dissolve
jm "Or so I'm told."
scene ep12_np2_jaj2 with dissolve
jo "I don't like the guy, but he's right."
scene ep12_np2_jaj1 with dissolve
al "I refuse to believe it. How would you even come up with that statistic?"
al "No one would admit they cum early, would they?"
scene ep12_np2_jaj2 with dissolve
jo "That's what makes it true! If guys don't wanna admit it, that's at least 30%%!"
scene ep12_np2_jaj7 with dissolve
jm "You can't argue with that logic."
scene ep12_np2_jaj1 with dissolve
al "You know who we should ask? The strippers."
al "They grind on cocks every day, yeah? I bet they would tell us if three out of ten guys cream in their boxers under a minute."
scene ep12_np2_jaj2 with dissolve
jo "Yeah! Where did they go?"
scene ep12_np2_jaj6 with dissolve
jm "I saw some of them drinking with us."
scene ep12_np2_jaj4 with dissolve
al "What the hell! They were all in our dining room during dinner."
scene ep12_np2_jaj6 with dissolve
jm "Blame it on the line."
scene ep12_np2_jaj5 with dissolve
jo "Can you go ask them?"
scene ep12_np2_jaj9 with dissolve
jm "I'll bring one stripper if you can beat me at chugging beer."
scene ep12_np2_jaj10 with dissolve
mc "Jamie? Are you gonna compete with the jocks?"
scene ep12_np2_jaj11 with dissolve
jm "Ever heard of diplomacy?"
scene ep12_np2_jaj13 with dissolve
al "Don't mind him; he's an ass. Let's chug for it."
scene ep12_np2_jaj11 with dissolve
jm "Relax, [name]. I've got this."
scene ep12_np2_jaj10 with dissolve
mc "Got what? What do you gain from this?"
scene ep12_np2_jaj12 with dissolve
jm "*{i}Whispers{/i}* They have the hot chicks on their side of the party."
jm "*{i}Whispers{/i}* I'm gonna try to get him drunk and then make a trade."
scene ep12_np2_jaj10 with dissolve
mc "A trade? You're talking about people here."
scene ep12_np2_jaj13 with dissolve
al "John, count us in. No cheating."
scene ep12_np2_jaj17 with dissolve
jo "Ready... Set... GO!"
scene ep12_np2_jaj18 with dissolve
jo "Come on, Alex! You've got this!"
jm "*{i}Glug glug{/i}*"
scene ep12_np2_jaj13 with dissolve
al "DONE!"
scene ep12_np2_jaj15 with dissolve
jm "Fuck... I wasn't even halfway done. How do you do that? Did you cheat?"
scene ep12_np2_jaj13 with dissolve
al "Fuck no! I didn't cheat. I'm all about chugging."
scene ep12_np2_jaj15 with dissolve
jm "Best out of seven?"
scene ep12_np2_jaj14 with dissolve
al "Seven!? Fuck no. I won."
scene ep12_np2_jaj15 with dissolve
jm "Best out of five?"
scene ep12_np2_jaj16 with dissolve
jo "You're gonna win either way. Take the bet."
scene ep12_np2_jaj13 with dissolve
al "Alright! Best out of five."
scene ep12_np2_jaj12 with dissolve
jm "*{i}Whispers{/i}* That's three big beers. Four if I win one."
scene ep12_np2_jaj10 with dissolve
mc "Haha, good luck then."
$ optional_task_list[0] = "Go to the bathroom"
$ updateTaskList()
$ event_list.append("ep12_np2_jd_label")
jump endEvent

label ep12_np2_jd_label:
scene ep12_np2_jd1
hide screen dance_filter_screen
with dissolve
de "Yeah. 30-40%% sounds about right if you ask me."
scene ep12_np2_jd2 with dissolve
jm "I think so too."
scene ep12_np2_jd1 with dissolve
de "You know, if you want to last longer with a girl, you should do what I do."
scene ep12_np2_jd3 with dissolve
mc "Ugh... Do I even wanna know what's going on in here?"
scene ep12_np2_jd5 with dissolve
de "Don't mind the noise. Here's what you do."
de "When you're edging and you're about to cum, stop all movement immediately."
scene ep12_np2_jd6 with dissolve
de "Then imagine that your dick is a straw and you want to suck the cum back into your balls."
de "Use your dick muscles to suck it back and then hold that muscle tight until the tingle goes away."
de "Then you're good to go for another five minutes, easy!"
scene ep12_np2_jd4 with dissolve
mc "Dude, you need serious help."
scene ep12_np2_jd7 with dissolve
de "I'll gladly receive your thanks after you realize it works, [mc_de]."
scene ep12_np2_jd4 with dissolve
mc "That's funny because Wendy told me you only lasted six minutes with her."
mc "A fact I'm desperately trying to forget."
scene ep12_np2_jd5 with dissolve
de "This trick only works if you WANT to last longer. With Wendy...hell no."
de "She was only a tad better than the wank you do when donating sperm."
scene ep12_np2_jd8 with dissolve
jm "You did that?"
scene ep12_np2_jd5 with dissolve
de "Someone's gonna carry the Derek genes into the future, and it sure as shit won't be me. Also, I needed the money."
scene ep12_np2_jd3 with dissolve
mc "I'm out of this discussion. Jamie... Don't listen to his advice too much."

$ optional_task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_tc_label:
scene ep12_np2_tc1 with dissolve
ch "You shouldn't have come here tonight."
scene ep12_np2_tc2 with dissolve
troy "Great to see you too..."
scene ep12_np2_tc1 with dissolve
ch "With the threat and all, we can't be seen together."
scene ep12_np2_tc2 with dissolve
troy "Don't worry about that, I'm sticking to the DIKs' side of the party."
scene ep12_np2_tc1 with dissolve
ch "That doesn't make it better. What if someone's watching you too?"
scene ep12_np2_tc3 with dissolve
$ renpy.pause()
if ep10_troy_mad:
    scene ep12_np2_tc5 with dissolve
    $ renpy.pause()
else:
    scene ep12_np2_tc4 with dissolve
    mc "Everything ok?"
    scene ep12_np2_tc6 with dissolve
    troy "Chad doesn't want me to talk about it."
    scene ep12_np2_tc7 with dissolve
    mc "What's up with Chad? He told me to fuck off earlier tonight."
    mc "We're not exactly buddies, but it felt weird."
    scene ep12_np2_tc6 with dissolve
    troy "He got another letter."
    scene ep12_np2_tc7 with dissolve
    mc "Another threat?"
    scene ep12_np2_tc6 with dissolve
    troy "Yeah... Someone doesn't want the two of you to get close."
    scene ep12_np2_tc7 with dissolve
    mc "How would anyone even know about it?"
    mc "All I've done is send him some texts in private, and we discreetly met once in the library."
    scene ep12_np2_tc9 with dissolve
    troy "Chad thinks it might be one of the tri-alphas."
    scene ep12_np2_tc8 with dissolve
    mc "His brothers?"
    scene ep12_np2_tc9 with dissolve
    troy "Yeah. Maybe one of them read your texts somehow or followed him to the library."
    troy "Or maybe it was you or your fault."
    scene ep12_np2_tc8 with dissolve
    mc "It wasn't me, Troy. Is he seriously suspecting me again?"
    scene ep12_np2_tc10 with dissolve
    troy "He's paranoid."
    troy "*{i}Sigh{/i}* It's not you, right?"
    scene ep12_np2_tc7 with dissolve
    mc "Hand on my heart. I had nothing to do with it."
    scene ep12_np2_tc9 with dissolve
    troy "Even if you're not involved, he doesn't want to risk anything."
    troy "There's too much at stake for him."
    scene ep12_np2_tc7 with dissolve
    mc "Alright. Let him know what I said."
    scene ep12_np2_tc6 with dissolve
    troy "I will."
    $ new_bio("Chad", "Troy told me that Chad was feeling paranoid after receiving another threatening letter.")
    $ new_bio("Troy", "Troy told me that Chad was feeling paranoid after receiving another threatening letter.")

$ task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_an_label:
scene ep12_np2_an1
hide screen dance_filter_screen
with dissolve
$ renpy.pause()
scene ep12_np2_an2 with dissolve
$ renpy.pause()
play sound "sound_effects/zipper.mp3"
scene ep12_np2_an3 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/pour.mp3"
scene ep12_np2_an4 with dissolve
an "Ahhh..."
scene ep12_np2_an5 with dissolve
ja "You're not doing what I think you're doing, are you?"
scene ep12_np2_an6 with dissolve
an "The bathroom is on their side of the party. And there was a line to the keg."
scene ep12_np2_an5 with dissolve
ja "Put that thing back inside your pants, or I'll have you leave early tonight."
ja "Either stop your childish fraternal games and use the restroom like a grown-up, or take your business someplace else."
scene ep12_np2_an6 with dissolve
an "Like outside?"
scene ep12_np2_an5 with dissolve
ja "*{i}Sigh{/i}* Leave."
if ep11_jade_lewd:
    $ event_list.append("ep12_np2_jade_label")
    if persistent.mod_wtenabled:
        $ task_list[2] = "Talk to Jade (Outside)"
    else:
        $ task_list[2] = "Talk to Jade"
else:
    $ task_list[2] = ""
$ updateTaskList()
$ event_list.append("ep12_np_fem_event_label")
jump endEvent

label ep12_np2_jade_label:
scene ep12_np2_jade1 with dissolve
mc "Aren't you freezing?"
scene ep12_np2_jade2 with dissolve
ja "It is cold, but peaceful out here."
scene ep12_np2_jade3 with dissolve
mc "Are you on a break?"
scene ep12_np2_jade4 with dissolve
ja "Could you imagine that a college party isn't all that fun when you're my age?"
scene ep12_np2_jade5 with dissolve
mc "I can."
mc "You didn't have to volunteer. You could have been off doing something more fun."
scene ep12_np2_jade6 with dissolve
ja "Cathy is celebrating with her company, and I wanted to avoid running into Stephen at other parties."
ja "While I'm technically working, this option was the winner for this year."
scene ep12_np2_jade5 with dissolve
mc "I'm sorry that you've had a rough year."
scene ep12_np2_jade6 with dissolve
ja "It couldn't end fast enough."
scene ep12_np2_jade4 with dissolve
ja "Enough about me and my misery... How about you and yours?"
scene ep12_np2_jade5 with dissolve
mc "Hah. My misery?"
mc "I can't complain."
if branchZoey and not wt_ep11_zoey_kiss_others:
    scene ep12_np2_jade7 with dissolve
    mc "Over the holidays, I got a girlfriend. I wanted to tell you that in person."
    scene ep12_np2_jade8 with dissolve
    ja "I suppose that's a fitting end to this year."
    scene ep12_np2_jade7 with dissolve
    mc "I'm sorry. I had a great time with you, but..."
    scene ep12_np2_jade6 with dissolve
    ja "I understand, [name]."
    ja "You were one of the highlights of my year. But it makes sense that you've found someone more age-appropriate."
    scene ep12_np2_jade7 with dissolve
    mc "The age gap was never an issue for me."
    mc "I love this girl, and that's why I can't continue with you."
    mc "I look forward to staying your friend, though."
    scene ep12_np2_jade9 with dissolve
    ja "I look forward to that too."
    scene ep12_np2_jade10 with dissolve
    $ renpy.pause()
    scene ep12_np2_jade6 with dissolve
    ja "Get back inside, [name]. Enjoy that party for both of us."
    scene ep12_np2_jade10 with dissolve
    $ renpy.pause()
    $ new_bio("Jade", "I told Jade about my relationship with Zoey.")
else:
    scene ep12_np2_jade11 with dissolve
    mc "It's been an eventful year. Weird, but eventful."
    scene ep12_np2_jade12 with dissolve
    ja "And what about your predictions for the next year? Will it be as eventful?"
    scene ep12_np2_jade11 with dissolve
    mc "I hope I find time for an adventure or two."
    scene ep12_np2_jade12 with dissolve
    ja "Haha! I bet you will. You seem to have a knack for it."
    ja "What about us? Do you think we'll have a joint adventure?"
    scene ep12_np2_jade11 with dissolve
    mc "That depends on you."
    scene ep12_np2_jade13 with dissolve
    ja "You have free will, too."
    scene ep12_np2_jade11 with dissolve
    mc "And parts of me have a will of their own."
    mc "I love the fun we've had together."
    scene ep12_np2_jade14 with dissolve
    ja "As I see it, we could continue doing it. But for every day it goes on, we're casting the die."
    ja "What happens if we get caught? But also, what happens if we don't?"
    scene ep12_np2_jade15 with dissolve
    ja "There's no easy answer. There's a logical and convenient answer, and there's a passionate and adventurous one."
    ja "Introspection says I should go with the first answer, but every time I talk to you, I lean toward the second one."
    scene ep12_np2_jade16 with dissolve
    mc "I don't want to stop you if you feel like this has run its course, but I see a lot of potential with you."
    scene ep12_np2_jade14 with dissolve
    ja "That's your dick speaking, [name]."
    scene ep12_np2_jade16 with dissolve
    mc "Even if it is, there's nothing wrong with that. Is there?"
    scene ep12_np2_jade15 with dissolve
    ja "One day, that steady stream of hormones flowing through your system will diminish, and you'll realize how stupid you were going after me."
    scene ep12_np2_jade16 with dissolve
    mc "I don't think I will. I already know it's risky and stupid in a sense, but that's just because of the rules."
    scene ep12_np2_jade12 with dissolve
    ja "Without those rules, it wouldn't be this hot. Admit it. You get a kick from breaking those rules with me."
    scene ep12_np2_jade11 with dissolve
    mc "Of course, I do. And don't say you don't."
    scene ep12_np2_jade15 with dissolve
    ja "You know I do. But I have considered going into the new year without you."
    ja "I could use a fresh start. After all, I don't see a future with you."
    ja "Last time I told you that, I put it too bluntly, but that doesn't mean it's not true."
    scene ep12_np2_jade12 with dissolve
    ja "There's a now, and there may be a later, but I can also see that there's an end to it."
    ja "Can't you?"
    scene ep12_np2_jade17 with dissolve
    mc "I can't say what I want for my future. That's part of why I'm here at B&R."
    mc "I thought that studying here would buy me some time to figure out what I truly want to do with my life."
    scene ep12_np2_jade16 with dissolve
    mc "And that extends to you. I don't know what I want to get out of this."
    mc "All I know is that we're good at what we do together, and that we both enjoy it."
    scene ep12_np2_jade18 with dissolve
    mc "That doesn't mean that it's something I'll do for the rest of my life."
    mc "Maybe our expiration date is when I quit college, or maybe it's earlier."
    scene ep12_np2_jade19 with dissolve
    mc "But no, I don't see us living together in the future, if that's what you're asking."
    mc "This isn't a relationship; it's sex and a friendship between two people who found each other in a weird way."
    mc "Part of it is wrong... So wrong... And the other part is extremely good."
    scene ep12_np2_jade20 with dissolve
    ja "You don't have an answer either."
    scene ep12_np2_jade19 with dissolve
    mc "Nope..."
    scene ep12_np2_jade20 with dissolve
    ja "That's ok, [name]. At least we're on the same page about the future."
    ja "I think it's good that you're realistic with your expectations of me."
    scene ep12_np2_jade21 with dissolve
    $ renpy.pause()
    scene ep12_np2_jade22 with dissolve
    ja "How about this? If you wish to continue this adventure next year..."
    ja "Find me at midnight, and we'll start the year together with the seal of a kiss."
    scene ep12_np2_jade23 with dissolve
    mc "You're putting our adventure to the test?"
    scene ep12_np2_jade22 with dissolve
    ja "I'm not asking you to commit to us. But I'm testing you and your hormones."
    ja "At a party with this many pretty girls, how does our adventure measure up?"
    ja "Do you truly want it? Or is it time for us to go our separate ways?"
    scene ep12_np2_jade23 with dissolve
    mc "You ask an interesting question... I will think about it."
    $ new_bio("Jade", "Jade put me to the test at the New Year's Eve party. She wanted to see how much our fling meant to me.")

$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep12_np_ly_label:
scene bg anim_lily_pan_ep12 movie with dissolve
pause
scene ep12_np_ly2 with dissolve
$ renpy.pause()
scene ep12_np_ly1 with dissolve
$ renpy.pause()
scene ep12_np_ly3 with dissolve
$ renpy.pause()
$ new_bio("Lily", "Lily has distanced herself from me.")
jump endEvent

label ep12_np_de_label:
scene ep12_np_de1 with dissolve
mc "Nice glasses."
scene ep12_np_de2 with dissolve
de "Funny, huh?"
scene ep12_np_de1 with dissolve
mc "Don't expect to get laid wearing those."
scene ep12_np_de3 with dissolve
de "That sounds like a bet."
scene ep12_np_de1 with dissolve
mc "$5 says you won't."
scene ep12_np_de3 with dissolve
de "$1000!"
scene ep12_np_de1 with dissolve
mc "..."
mc "$10?"
scene ep12_np_de2 with dissolve
de "Sure. Let's do $10."
scene ep12_np_de1 with dissolve
mc "What are you up to?"
scene ep12_np_de4 with dissolve
de "I was gonna have some Champagne, but Sis confiscated the bottle."
scene ep12_np_de5 with dissolve
mc "Déjà vu..."
scene ep12_np_de4 with dissolve
de "It's not like I would sever it again."
scene ep12_np_de5 with dissolve
mc "I think I speak for both Maya and me when I say that you'd find a way to make it shorter."
scene ep12_np_de4 with dissolve
de "Speaking of feeling short... What's up with everyone wearing heels tonight?"
scene ep12_np_de1 with dissolve
mc "Haha, right? There are a lot of pretty girls at the party."
scene ep12_np_de2 with dissolve
de "I've only got my eyes on one..."
de "I'm telling you, those $1000 are mine."
$ task_list[2] = ""
$ updateTaskList()
$ new_bio("Derek", "Derek bet me $10 that he could get laid wearing some stupid New Year's Eve-themed glasses.")
jump endEvent

label ep12_np2_ad_label:
scene ep12_np2_ad1 with dissolve
$ renpy.pause()
scene ep12_np2_ad2 with dissolve
mc "Aw, look at you two."
mc "Did it finally happen?"
scene ep12_np2_ad3 with dissolve
ash "It did..."
scene ep12_np2_ad4 with dissolve
mc "Are you together now?"
scene ep12_np2_ad5 with dissolve
de "I don't know..."
scene ep12_np2_ad6 with dissolve
ash "Derek?"
scene ep12_np2_ad5 with dissolve
de "Yeah, we're together."
scene ep12_np2_ad4 with dissolve
mc "*{i}Phew{/i}* Good answer. You were close to having the shortest relationship ever."
scene ep12_np2_ad5 with dissolve
de "I love this girl."
scene ep12_np2_ad7 with dissolve
ash "Aw... I love you!"
scene ep12_np2_ad4 with dissolve
mc "It's about time. Congratulations!"
mc "I'm not gonna bother you, keep doing what you're doing."
scene ep12_np2_ad1 with dissolve
$ renpy.pause()
scene ep12_np2_ad8 with dissolve
$ renpy.pause()
scene ep12_np2_ad9 with dissolve
$ renpy.pause()
$ task_list[7] = ""
$ updateTaskList()
$ new_bio("Derek", "It finally happened. Derek and Ashley got together at the New Year's Eve party.")
$ new_bio("Ashley", "It finally happened. Derek and Ashley got together at the New Year's Eve party.")
jump endEvent

label ep12_np2_rdm_label:
scene ep12_np2_rdm1 with dissolve
$ renpy.pause()
scene ep12_np2_rdm2 with dissolve
$ renpy.pause()
scene ep12_np2_rdm3 with dissolve
rs "I've been thinking... Um..."
rs "I think I've made a huge mistake."
scene ep12_np2_rdm4 with dissolve
if ep4_toldDerekAboutJade:
    mc "I'm the King of making mistakes, and I think you made one too."
else:
    mc "I think so too."
scene ep12_np2_rdm3 with dissolve
rs "Yeah... I just went with it."
rs "As long as I didn't see her guy, I didn't care about what I did to him."
rs "But that was me being stupid. I thought it was hot to sneak around with her, but I fucked up big time."
scene ep12_np2_rdm4 with dissolve
mc "Dwyane is a great guy, Rusty..."
mc "And I sat with him and Micha during dinner. She's a good liar..."
scene ep12_np2_rdm5 with dissolve
mc "She was lying straight to his face about you, and he was clueless."
mc "He doesn't deserve this, and Micha doesn't deserve him."
scene ep12_np2_rdm3 with dissolve
rs "She lied to him?"
scene ep12_np2_rdm4 with dissolve
mc "Like a pro. And if a girl can do that to someone they're with, they can do it to you. If not now, later."
if (tc > 4 and not branchAlone) or affinity == "DIK" or ep4_toldDerekAboutJade:
    mc "I'm not the best guy to speak on morals, but that girl is trouble. And not the good kind."
else:
    mc "That girl is trouble, Rusty. And not the good kind."
scene ep12_np2_rdm6 with dissolve
rs "You're right."
scene ep12_np2_rdm5 with dissolve
mc "What are you going to do about it?"
scene ep12_np2_rdm7 with dissolve
$ renpy.pause()
scene ep12_np2_rdm8 with dissolve
$ renpy.pause()
scene ep12_np2_rdm9 with dissolve
$ renpy.pause()
scene ep12_np2_rdm10 with dissolve
$ renpy.pause()
if persistent.mod_wtenabled:
    $ task_list[0] = "Find Dwyane (3F corridor)"
else:
    $ task_list[0] = "Find Dwyane"
$ event_list.append("ep12_np2_dr_label")
$ updateTaskList()
$ new_bio("Rusty", "Rusty felt guilty about having sex with Micha now that he saw her with Dwyane at the party.")
jump endEvent

label ep12_np2_dr_label:
$ guideSuggestedPage = 263
play sound "sound_effects/shove.mp3"
scene ep12_np2_dr1 with hpunch
dwy "What the fuck are you saying to me?"
scene ep12_np2_dr2 with dissolve
rs "I'm sorry. But it's the truth."
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep12_np2_dr3 with hpunch
mc "Whoa!"
scene ep12_np2_dr4 with dissolve
mc "Dwyane! Calm down!"
scene ep12_np2_dr6 with dissolve
dwy "Out of my way, [name]. This is between him and me."
scene ep12_np2_dr4 with dissolve
mc "He doesn't stand a chance against you, and you know it. I'm not gonna let you beat my friend up."
scene ep12_np2_dr6 with dissolve
dwy "He's fucking my girl. What would you do?"
scene ep12_np2_dr5 with dissolve
mc "I know, Dwyane. It sucks."
scene ep12_np2_dr7 with dissolve
dwy "You know?"
scene ep12_np2_dr8 with dissolve
mic "Dwyane, stop it!"
scene ep12_np2_dr9 with dissolve
dwy "Is this what I'm worth to you?"
dwy "I try to provide and get us a better future, and you do this to me?"
scene ep12_np2_dr13 with dissolve
rs "Dwyane, I'm sorry."
scene ep12_np2_dr10 with dissolve
dwy "You shut your fucking clown mouth."
scene ep12_np2_dr14 with dissolve
$ renpy.pause()
scene ep12_np2_dr11 with dissolve
dwy "I can't believe you knew and didn't tell me."
scene ep12_np2_dr12 with dissolve
$ renpy.pause()
scene ep12_np2_dr15 with dissolve
al "Haha, it's funny because they thought we were gonna fight them. It turns out no one can stand the DIKs."
scene ep12_np2_dr16 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKS)","(-DIKS)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Follow Dwyane \n{size=-4}[m_c2][mod_choices[1]]":
        $ RPdiks -= 1
        $ ep12_rusty_over_dwyane = False
        scene ep12_np2_dr27 with dissolve
        $ renpy.pause()
        scene ep12_np2_dr28 with dissolve
        mc "Dwyane, wait!"
        scene ep12_np2_dr29 with dissolve
        dwy "I can't deal with you now, [name]."
        scene ep12_np2_dr30 with dissolve
        mc "Why are you running away? That's not the Dwyane I know."
        scene ep12_np2_dr31 with dissolve
        dwy "The [name] I know doesn't betray his friends like that."
        scene ep12_np2_dr32 with dissolve
        mc "I didn't betray you. I had no idea that Micha was your girlfriend."
        mc "When you showed up with her tonight, it clicked."
        scene ep12_np2_dr33 with dissolve
        mc "And what was I going to do? Tell you straight up?"
        mc "Do you know what I did?"
        scene ep12_np2_dr34 with dissolve
        mc "I went to Rusty and told him who you were. I told him that you are my friend and a great guy."
        mc "And before the night was even over, he came clean to you."
        mc "He's a good guy, too, but he did a bad thing. And he owned up to it."
        scene ep12_np2_dr35 with dissolve
        dwy "How long has it been going on?"
        scene ep12_np2_dr34 with dissolve
        mc "Rusty and Micha? I first saw them flirting at a dorm party earlier this semester."
        mc "The best estimate I can give you is a couple of months."
        scene ep12_np2_dr35 with dissolve
        dwy "Months!?"
        scene ep12_np2_dr36 with dissolve
        dwy "I can't believe her, [name]."
        dwy "Everything I did, I did for her and Ma."
        scene ep12_np2_dr37 with dissolve
        dwy "I wanted to show them that I could change."
        dwy "But she wasn't worth changing for."
        scene ep12_np2_dr38 with dissolve
        mc "But your mom was."
        mc "And based on what you've told me, you turned out for the better."
        scene ep12_np2_dr39 with dissolve
        mc "You didn't deserve to get cheated on. And if she were a good person, she'd be the one standing here in front of you now telling you that."
        mc "I'm so sorry, Dwyane..."
        scene ep12_np2_dr40 with dissolve
        dwy "You're a real one, [name]."
        scene ep12_np2_dr39 with dissolve
        mc "Wanna get back in there?"
        scene ep12_np2_dr41 with dissolve
        dwy "Nah. Nothing good waits for me in there."
        scene ep12_np2_dr39 with dissolve
        mc "Take it easy, Dwyane."
        scene ep12_np2_dr42 with dissolve
        dwy "Yeah..."
        scene ep12_np2_dr26 with dissolve
        mc "Rusty? Are you ok?"
        scene ep12_np2_dr23 with dissolve
        rs "*{i}Sigh{/i}* This was a shit end to the year."
        scene ep12_np2_dr19 with dissolve
        mc "I caught up to Dwyane and calmed him down."
        scene ep12_np2_dr23 with dissolve
        rs "Hmpff..."
        rs "I didn't think he'd punch me like that."
        scene ep12_np2_dr19 with dissolve
        mc "Wouldn't you have done it in his shoes?"
        scene ep12_np2_dr24 with dissolve
        rs "Still, I wanted to come clean to him. I didn't expect it to turn out that way."
        scene ep12_np2_dr20 with dissolve
        mc "Anything can happen when you love someone and they betray you."
        mc "He saw you as the bad guy."
        scene ep12_np2_dr23 with dissolve
        rs "Whatever. I'm done with her."
        scene ep12_np2_dr20 with dissolve
        mc "For what it's worth, you did the right thing."
    "Check on Rusty \n{size=-4}[m_c1][mod_choices[0]]":
        $ RPdiks += 1
        $ ep12_rusty_over_dwyane = True
        scene ep12_np2_dr17 with dissolve
        mc "Rusty? Are you ok?"
        scene ep12_np2_dr18 with dissolve
        rs "I need to sit down."
        scene ep12_np2_dr19 with dissolve
        mc "Does it hurt?"
        scene ep12_np2_dr23 with dissolve
        rs "He punches harder than you'd think."
        scene ep12_np2_dr19 with dissolve
        mc "I've caught his punches when sparring with him, and yeah, he punches hard."
        mc "For what it's worth, you did the right thing."
        scene ep12_np2_dr23 with dissolve
        rs "It doesn't feel like it at the moment."
        rs "Micha won't forgive me, and Dwyane probably hates me."
        scene ep12_np2_dr20 with dissolve
        mc "Yeah, but it doesn't matter. You made a sacrifice for the greater good."
        mc "You spared Dwyane from wasting his time on Micha."
        mc "And maybe you changed Micha for the better by exposing her like that."
        scene ep12_np2_dr23 with dissolve
        rs "*{i}Sigh{/i}* Maybe you're right."
        scene ep12_np2_dr20 with dissolve
        mc "Did you love Micha?"
        scene ep12_np2_dr23 with dissolve
        rs "If I loved her? No. I liked her a lot."
        rs "She was fun to be with."
        scene ep12_np2_dr24 with dissolve
        rs "But that's not the kind of relationship I want to be in..."
        rs "I don't want to be the other guy. I want to be the guy."
        scene ep12_np2_dr25 with dissolve
        rs "And I want to be with someone who wants me and no one else."
        rs "Micha wasn't that for me."
        scene ep12_np2_dr20 with dissolve
        mc "Like I said, you did the right thing."
        scene ep12_np2_dr23 with dissolve
        rs "Thanks, [name]. You're a true friend."
        scene ep12_np2_dr22 with dissolve
        rs "Uh... What about Dwyane?"
        scene ep12_np2_dr21 with dissolve
        mc "I'll let him calm down, then I'll reach out to him."
        scene ep12_np2_dr22 with dissolve
        rs "I hope I didn't ruin your friendship."
        scene ep12_np2_dr21 with dissolve
        mc "He's a smart guy. He'll listen to reason."
if ep12_pp_game == 0:
    $ event_list.append("ep12_np2_cg_label")
    if persistent.mod_wtenabled: 
        $ task_list[0] = "Play card game (Dining room)"
    else:
        $ task_list[0] = "Play card game"
else:
    $ task_list[0] = ""
if ep12_rusty_over_dwyane:
    $ new_bio("Rusty", "Rusty got into a fight with Dwyane after confessing that he had sex with Micha. I chose to stay behind to check up on Rusty after.")
else:
    $ new_bio("Rusty", "Rusty got into a fight with Dwyane after confessing that he had sex with Micha. I chose to check up on Dwyane after the fight.")
$ updateTaskList()
jump endEvent

label ep12_np2_rq_label:
scene ep12_np2_rq1 with dissolve
$ renpy.pause()
scene ep12_np2_rq2 with dissolve
qu "..."
scene ep12_np2_rq3 with dissolve
qu "I know you told me to stay away from you, but there are things you should know."
scene ep12_np2_rq7 with dissolve
$ renpy.pause()
scene ep12_np2_rq4 with dissolve
qu "I took care of everything. You won't have to worry anymore."
qu "Buddy is in jail. Mick is dead. And Vinny has left town for good."
scene ep12_np2_rq8 with dissolve
$ renpy.pause()
scene ep12_np2_rq5 with dissolve
qu "I know that's a lot to take in. I didn't kill Mick; Vinny did."
qu "But I made sure that Buddy was caught and the rest unraveled."
scene ep12_np2_rq9 with dissolve
qu "I have all his money. I have all his drugs."
qu "And I want to share everything with you."
scene ep12_np2_rq6 with dissolve
qu "I know that it won't make up for what happened to you."
qu "But I don't know how else to tell you how sorry I am."
qu "And I promise you... You're not in danger anymore."
scene ep12_np2_rq10 with dissolve
$ renpy.pause()
play sound "sound_effects/slap.mp3"
scene ep12_np2_rq13 with hpunch
$ renpy.pause()
scene ep12_np2_rq12 with dissolve
$ renpy.pause()
scene ep12_np2_rq11 with dissolve
$ renpy.pause()
scene ep12_np2_rq14 with dissolve
$ renpy.pause()
if maya_shiny_dress:
    scene ep12_np2_rq15 with dissolve
else:
    scene ep12_np2_rq15b with dissolve
$ renpy.pause()

if ep12_riona_side == "Riona" or wt_ep11_quinn_riona_question:
    if persistent.mod_wtenabled: 
        $ task_list[3] = "Talk to Riona (Balcony)"
    else:
        $ task_list[3] = "Talk to Riona"
    $ event_list.append("ep12_np2_rio_label")
else:
    $ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_had_label:
scene ep12_np2_had1 with dissolve
he "Are you going to do a paternity test?"
scene ep12_np2_had2 with dissolve
ar "You mean, to check if the baby is mine?"
scene ep12_np2_had1 with dissolve
he "To check who the father is."
scene ep12_np2_had2 with dissolve
ar "I don't have to do that. Dawe is my only boyfriend; he's the father."
scene ep12_np2_had1 with dissolve
he "Yeah, but that's not how it works."
scene ep12_np2_had3 with dissolve
ar "Well, let's ask him! Dawe!?"
scene ep12_np2_had4 with dissolve
dw "Yeah?"
scene ep12_np2_had5 with dissolve
ar "You're the father of my baby, aren't you?"
scene ep12_np2_had6 with dissolve
dw "About that, I was thinking... Is it too late to...not be a dad?"
scene ep12_np2_had5 with dissolve
ar "What are you saying?"
scene ep12_np2_had6 with dissolve
dw "With college and all... I don't think I can afford a baby right now."
dw "I would have to ask my parents for money, and they are already kinda disappointed in me."
scene ep12_np2_had11 with dissolve
ar "You want me to give the baby away?"
scene ep12_np2_had7 with dissolve
dw "Is that an option?"
scene ep12_np2_had11 with dissolve
ar "The pregnancy test is one of the few tests I've taken this year that I passed."
ar "You're not taking this baby away from me!"
scene ep12_np2_had7 with dissolve
dw "Don't get upset. I'm not! Ok? I was just checking!"
scene ep12_np2_had11 with dissolve
ar "It's the hormones. I've been super-sensitive lately."
scene ep12_np2_had8 with dissolve
dr "Hey... Don't you want to be a dad anymore?"
scene ep12_np2_had9 with dissolve
dw "It's so damn expensive... And..."
scene ep12_np2_had10 with dissolve
dw "I didn't know she would get this fat. It's a total turn-off."
$ optional_task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_jsl_label:
scene ep12_np2_jsl1 with dissolve
suz "Mmmphfff *{i}Smack{/i}*"
scene ep12_np2_jsl2 with dissolve
li "Mmmphfff *{i}Smack smack{/i}*"
scene ep12_np2_jsl3 with dissolve
li "Are you kidding me!?"
scene ep12_np2_jsl4 with dissolve
mi "What?"
scene ep12_np2_jsl6 with dissolve
li "Suzy bagged a total hottie!"
li "I'm supposed to be the cute one of the bunch."
scene ep12_np2_jsl5 with dissolve
mi "I know... How did she do that? Isn't that a jock too?"
scene ep12_np2_jsl3 with dissolve
li "Oh my God! You're right. It is a jock."
li "I'd be wicked thin if I were with him."
scene ep12_np2_jsl5 with dissolve
mi "How do you figure?"
scene ep12_np2_jsl7 with dissolve
li "He's probably into all kinds of adventurous sex."
li "We'd be all over each other and roll around so much that I'd burn all my calories in an instant."
scene ep12_np2_jsl6 with dissolve
li "I have to find myself a jock, too."
scene ep12_np2_jsl5 with dissolve
mi "What if Suzy can introduce us to all of his friends?"
scene ep12_np2_jsl7 with dissolve
li "That would be so hot..."
jump endEvent

label ep12_np2_nik_label:
scene ep12_np2_nik1 with dissolve
$ renpy.pause()
scene ep12_np2_nik2 with dissolve
mc "Hey..."
scene ep12_np2_nik3 with dissolve
$ renpy.pause()
scene ep12_np2_nik4 with dissolve
nik "Why are you standing over there?"
scene ep12_np2_nik5 with dissolve
$ renpy.pause()
scene ep12_np2_nik4 with dissolve
nik "So, that's what it's for."
scene ep12_np2_nik3 with dissolve
mc "Stupid, huh?"
scene ep12_np2_nik4 with dissolve
nik "You should cross it."
scene ep12_np2_nik3 with dissolve
mc "I have crossed many lines, but I don't think I should cross this one."
scene ep12_np2_nik6 with dissolve
$ renpy.pause()
scene ep12_np2_nik7 with dissolve
mc "Now you're just teasing me."
scene ep12_np2_nik8 with dissolve
nik "Are you having fun at the party?"
scene ep12_np2_nik9 with dissolve
mc "Yeah, it's ok. I enjoyed the food, and it's always nice to see people enjoy themselves when you host a party."
mc "How about you?"
scene ep12_np2_nik10 with dissolve
nik "I'm having a good time."
nik "But there's something about New Year's Eve that makes me feel..."
scene ep12_np2_nik11 with dissolve
menu:
    "Weird?":
        mc "Weird?"
        scene ep12_np2_nik10 with dissolve
        nik "Sad."
    "Sad?":
        mc "Sad?"
        scene ep12_np2_nik10 with dissolve
        nik "Yes."
    "Horny? \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Horny?"
        scene ep12_np2_nik10 with dissolve
        nik "Hah! You're not very good at finishing someone's-"
        scene ep12_np2_nik12 with dissolve
        mc "Sentences?"
        scene ep12_np2_nik10 with dissolve
        nik "That one was a lay-up."
        nik "I was going to say \"sad\"."
scene ep12_np2_nik13 with dissolve
mc "Why are you sad?"
scene ep12_np2_nik14 with dissolve
nik "It makes me think about how fast one year can pass."
nik "I know I'm young, but life is short and fragile."
nik "I get stuck on those thoughts, and they scare me."
scene ep12_np2_nik13 with dissolve
mc "Are you scared of life passing you by?"
scene ep12_np2_nik15 with dissolve
nik "Aren't you?"
scene ep12_np2_nik16 with dissolve
mc "Hm..."
mc "I'm only 19, but I've had an eventful life so far."
mc "I think it's too early to worry about life being short."
scene ep12_np2_nik18 with dissolve
nik "Then what would you do about it, if you were me?"
scene ep12_np2_nik19 with dissolve
mc "I'd try to focus more on living in the moment."
mc "Because if you do that, then you wouldn't waste time worrying."
scene ep12_np2_nik18 with dissolve
nik "You make a great point."
nik "I'm worrying about wasting my time. And ironically, I'm wasting time by worrying."
scene ep12_np2_nik20 with dissolve
nik "So, how many years have you spent living in the moment?"
scene ep12_np2_nik17 with dissolve
mc "None so far. You see, I'm a procrastinator."
scene ep12_np2_nik21 with dissolve
nik "Hahaha!"
scene ep12_np2_nik20 with dissolve
nik "You should make it your New Year's resolution."
scene ep12_np2_nik22 with dissolve
mc "I don't do those... But I will, if you will."
scene ep12_np2_nik23 with dissolve
$ renpy.pause()
scene ep12_np2_nik24 with dissolve
$ renpy.pause()
play sound "sound_effects/whoosh.mp3"
scene ep12_np2_nik25 with hpunch
mc "Whoa!"
scene ep12_np2_nik26 with dissolve
mc "Hey, that was..."
scene ep12_np2_nik27 with dissolve
nik "Aren't you living in the moment now?"
scene ep12_np2_nik28 with dissolve
mc "It's scarier than I thought it would be."
scene ep12_np2_nik29 with dissolve
$ renpy.pause()
scene ep12_np2_nik30 with dissolve
mc "What are you looking at?"
scene ep12_np2_nik31 with dissolve
nik "I'm enjoying watching you squirm like you're doing something forbidden."
scene ep12_np2_nik30 with dissolve
mc "I am doing something forbidden. I could start a frat war by being on this side of the party."
scene ep12_np2_nik32 with dissolve
mc "And you're smiling about it... You are trouble."
scene ep12_np2_nik33 with dissolve
nik "Haha! I've never been described as trouble before in my life."
scene ep12_np2_nik34 with dissolve
mc "Probably because nobody dared to tell it to your face."
scene ep12_np2_nik33 with dissolve
nik "Is that so?"
scene ep12_np2_nik34 with dissolve
mc "I've been called trouble, caused trouble, and been in trouble."
mc "That's why I recognize trouble."
scene ep12_np2_nik35 with dissolve
mc "I don't mean to alarm you, but... Um..."
mc "Your dress is hanging low."
scene ep12_np2_nik36 with dissolve
nik "Oh..."
scene ep12_np2_nik37 with dissolve
nik "Well... Every other girl at the party and I."
scene ep12_np2_nik38 with dissolve
mc "Sorry for pointing it out."
scene ep12_np2_nik37 with dissolve
nik "Don't be. Some people will let you walk around with spinach between your teeth without telling you."
nik "I'm a bit embarrased, though."
scene ep12_np2_nik39 with dissolve
mc "Here. Let's get even already. Living in the moment!"
nik "Hahaha!"
scene ep12_np2_nik40 with dissolve
nik "You always make me laugh."
scene ep12_np2_nik41 with dissolve
$ renpy.pause()
scene ep12_np2_nik42 with dissolve
$ renpy.pause()
scene ep12_np2_nik43 with dissolve
$ renpy.pause()
scene ep12_np2_nik47 with dissolve
cb "That's what I've been telling you. Bitches are only loyal until there's a new shiny toy around the corner."
play sound "sound_effects/shove.mp3"
scene ep12_np2_nik44 with hpunch
$ renpy.pause()
scene ep12_np2_nik47 with dissolve
cb "They are like monkeys. They won't let go of the old branch until they've grabbed a new one."
scene ep12_np2_nik45 with dissolve
$ renpy.pause()
scene ep12_np2_nik46 with dissolve
$ renpy.pause()

$ new_bio("Nikita", "Nikita and I almost kissed at the New Year's Eve party. We flirted with each other and had an enjoyable conversation.")
$ task_list[4] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_ari_label:
scene ep12_np2_ari1
hide screen dance_filter_screen
with dissolve
ar "*{i}Phew{/i}* What a night."
ar "I'm eating for two, but tonight I felt like I ate for three."
scene ep12_np2_ari2 with dissolve
ar "Ahhhh..."
scene ep12_np2_ari3 with dissolve
ar "You did not have a good night. Oh, boy..."
ar "My instincts were right about you."
scene ep12_np2_ari4 with dissolve
mc "Were they?"
scene ep12_np2_ari3 with dissolve
ar "Yep."
ar "Between you and me, I'm happy Quinn didn't put me in the spotlight tonight."
scene ep12_np2_ari4 with dissolve
mc "Is that right...?"
scene ep12_np2_ari3 with dissolve
ar "I like sex, but there's a limit."
ar "One of my dreams has been to sleep with every DIK."
scene ep12_np2_ari5 with dissolve
ar "And I was saving you for last. And not because you showed up after I had already slept with most."
ar "I've had some dirty thoughts about you."
scene ep12_np2_ari6 with dissolve
ar "But then I got turned off after all the rumors started."
ar "I can't have sex with someone who's that loose."
ar "I just can't do it."
scene ep12_np2_ari3 with dissolve
ar "Oh, well."
scene ep12_np2_ari4 with dissolve
mc "Thanks for the pep talk."
scene ep12_np2_ari3 with dissolve
ar "Anytime!"
ar "Now I need to visit the ladies' room."
scene ep12_np2_ari7 with dissolve
ar "Even that I do for three. Hah!"
jump endEvent

label ep12_np2_qsm_label:
scene ep12_np2_qsm1 with dissolve
qu "I have some good news for us."
scene ep12_np2_qsm7 with dissolve
sar "I'd say it's about time."
scene ep12_np2_qsm2 with dissolve
qu "We won't continue our operation as normal..."
scene ep12_np2_qsm10 with dissolve
ml "We won't?"
scene ep12_np2_qsm2 with dissolve
qu "No. But I can reassure you that the tuition will last as is."
qu "There's no new development there, good or bad."
scene ep12_np2_qsm6 with dissolve
qu "But... We will need to sell more than we used to from now on."
scene ep12_np2_qsm8 with dissolve
sar "More? Are we scaling up?"
scene ep12_np2_qsm6 with dissolve
qu "I've got a supply that will last us for a long time. But I'm sitting on too much of it. We need to sell off lots quickly."
qu "And I need your help with that."
scene ep12_np2_qsm10 with dissolve
ml "I don't know... It seems risky."
scene ep12_np2_qsm2 with dissolve
qu "We'll split the money we earn. I'll get 50%% and you two share the other half."
scene ep12_np2_qsm11 with dissolve
ml "Wait a minute... Are we splitting the money we earn from the sales now?"
ml "It's not coming from...higher up?"
scene ep12_np2_qsm2 with dissolve
qu "I run the show now. This means more money than you can imagine."
qu "But I can't do it without you."
scene ep12_np2_qsm8 with dissolve
sar "What's the catch?"
scene ep12_np2_qsm6 with dissolve
qu "There's no catch."
scene ep12_np2_qsm10 with dissolve
ml "There has to be a catch. It sounds too good to be true."
scene ep12_np2_qsm3 with dissolve
qu "Well... You have to sell some harder drugs, too."
scene ep12_np2_qsm9 with dissolve
sar "And there it is..."
sar "Fuck... Quinn... This is starting to feel criminal."
scene ep12_np2_qsm5 with dissolve
qu "Bitch, wake up. You've been a criminal all year."
scene ep12_np2_qsm10 with dissolve
ml "I'm with Sarah... Something about this doesn't feel right."
scene ep12_np2_qsm3 with dissolve
qu "Why are you two so stupid?"
qu "You don't want to sell anything? You don't want to make money?"
qu "We're talking real money... You owe me this. Think of everything I did for you. I have lots to sell."
scene ep12_np2_qsm7 with dissolve
sar "Then ask Rio to sell more."
sar "I'll sell some weed here and there, but only to my friends, and that's it."
scene ep12_np2_qsm10 with dissolve
ml "Yeah. That's my limit too."
scene ep12_np2_qsm4 with dissolve
qu "..."
scene ep12_np2_qsm5 with dissolve
qu "Fine. But that will significantly reduce your cut."
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_nick_label:
$ guideSuggestedPage = 264
scene ep12_np2_nick1 with dissolve
ni "[name]. I've been talking to Rusty and Jacob... I think it's our turn to have a chat."
scene ep12_np2_nick2 with dissolve
mc "Is this the best time and place to have this talk, Nick?"
scene ep12_np2_nick1 with dissolve
ni "Give me five minutes to say what I need to say. If you don't feel like talking to me after, then it's fine."
scene ep12_np2_nick2 with dissolve
mc "It's too loud in here. Let's take a walk."

scene ep12_np2_nick3 with dissolve
qu "Alright, party people! How are we doing?"
scene ep12_np2_nick5 with dissolve
"*{i}Cheers{/i}*"
scene ep12_np2_nick3 with dissolve
qu "You're all looking beautiful, but not drunk enough. And I'm here to fix that!"
qu "Let's have a good old-fashioned drinking game."
scene ep12_np2_nick4 with dissolve
qu "If you don't have a drink in your hand, you're doing it wrong. Go get one! And fetch a sober friend while you're at it."
if (not breakup and branchSage) and not wt_ep11_zoey_kiss_others:
    scene ep12_np2_sz1 with dissolve
    $ renpy.pause()
    scene ep12_np2_sz2 with dissolve
    sa "Hey."
    scene ep12_np2_sz8 with dissolve
    zo "Yeah?"
    scene ep12_np2_sz3 with dissolve
    sa "What's your deal?"
    scene ep12_np2_sz8 with dissolve
    zo "My deal?"
    scene ep12_np2_sz3 with dissolve
    sa "You told my boyfriend you love him."
    scene ep12_np2_sz9 with dissolve
    zo "Oh? That... I-"
    scene ep12_np2_sz7 with dissolve
    sa "Let me spell it out for you..."
    sa "Where I come from, you get punched in the fucking face for doing that."
    if zoey_dik:
        scene ep12_np2_sz8 with dissolve
        zo "Aha. You're opening that door."
        scene ep12_np2_sz3 with dissolve
        sa "You're lucky we're at a party."
        scene ep12_np2_sz10 with dissolve
        zo "I don't buy it. You try to talk tough while wearing the girliest dress I ever saw."
        zo "Where was it that you came from? Because it neither sounds nor looks like you came from the streets."
        scene ep12_np2_sz7 with dissolve
        sa "Do yourself a favor and stay the fuck away from him."
        sa "I don't want you around. Do you get it?"
        if ep12_zoey_friend:
            scene ep12_np2_sz10 with dissolve
            zo "It's not your call. [name] wants me around."
            scene ep12_np2_sz4 with dissolve
            sa "I wouldn't be too sure about that."
            scene ep12_np2_sz11 with dissolve
            zo "Check again. He just told me he wants to stay friends."
            zo "I don't think you know him as well as you think you do."
            scene ep12_np2_sz6 with dissolve
            $ renpy.pause()
        else:
            scene ep12_np2_sz8 with dissolve
            zo "Calm your tits. You can have him."
            zo "He doesn't even want my friendship anymore."
            scene ep12_np2_sz4 with dissolve
            sa "He told you that?"
            scene ep12_np2_sz8 with dissolve
            zo "Mhm."
            scene ep12_np2_sz5 with dissolve
            sa "Ok... Good. Then we understand each other."
    else:
        scene ep12_np2_sz8 with dissolve
        zo "Relax. Don't take it personally."
        zo "It didn't concern you. What I told [name], was between him and me."
        scene ep12_np2_sz9 with dissolve
        zo "I wanted to see if there was a chance he felt the same, but he didn't."
        scene ep12_np2_sz4 with dissolve
        sa "You're wrong. It does concern me. It directly affects me when you shoot your shot at my boyfriend."
        sa "In your head, you might think it's alright and that it doesn't matter. But it matters to me."
        scene ep12_np2_sz5 with dissolve
        sa "And he gave your an answer. He doesn't feel something for you anymore."
        sa "And now I think you should do the right thing... Since you already disrespected me once..."
        sa "Stay away from him. Please?"
        if ep12_zoey_friend:
            scene ep12_np2_sz8 with dissolve
            zo "Look... It's not that simple."
            scene ep12_np2_sz4 with dissolve
            sa "It is. Why would you even want to be his friend now?"
            sa "He rejected you and his girlfriend will never stand for you."
            scene ep12_np2_sz8 with dissolve
            zo "But he will. He just told me he's not giving up on our friendship."
            zo "And again... My friendship with him doesn't concern you."
            scene ep12_np2_sz9 with dissolve
            zo "I get that it sucks for you, but he's been there for me all my life..."
            zo "If he still wants me around, guess what? I'll be there."
            zo "And there's nothing you can say that will stop me."
            scene ep12_np2_sz6 with dissolve
            $ renpy.pause()
        else:
            scene ep12_np2_sz8 with dissolve
            zo "It seems like this conversation is pointless."
            scene ep12_np2_sz4 with dissolve
            sa "To me it's not."
            scene ep12_np2_sz8 with dissolve
            zo "It is. [name] doesn't want to stay friends with me. You can exhale now."
            scene ep12_np2_sz5 with dissolve
            sa "He doesn't?"
            scene ep12_np2_sz9 with dissolve
            zo "No. He said we outgrew each other. And he picked you, so..."
            zo "I don't know why you're this upset. You've got no reason to be."
            scene ep12_np2_sz4 with dissolve
            sa "I still didn't like what you did."
            scene ep12_np2_sz8 with dissolve
            zo "Yeah, no shit. But I don't care."
            zo "It's not like you and I ever will be friends."
            scene ep12_np2_sz6 with dissolve
            sa "..."

scene ep12_np2_nick6
hide screen dance_filter_screen
with dissolve
ni "I'm sorry for everything, [name]."
ni "What Tommy and I fought about ended up affecting everyone in the frat."
scene ep12_np2_nick7 with dissolve
ni "I didn't know how to act in that situation, and it felt like you all ganged up on me..."
ni "I snapped."
scene ep12_np2_nick8 with dissolve
mc "Yeah, you did."
scene ep12_np2_nick9 with dissolve
ni "Nothing of what I said back then...uh..."
ni "I won't tell a soul about it. It was our fight."
scene ep12_np2_nick10 with dissolve
ni "I regret it. And I know you probably don't think I deserve a second chance..."
ni "Hell, I don't even think I deserve one. But our fraternity is all that's any good in my life."
scene ep12_np2_nick11 with dissolve
ni "I've never had many friends, but coming to college changed all that."
ni "I feel like I'm back in high school, where I was a nobody."
scene ep12_np2_nick12 with dissolve
ni "The DIKs made me feel like I was somebody."
ni "The brotherhood made me feel confident, and for the first time, I felt like I belonged."
scene ep12_np2_nick13 with dissolve
ni "I know Vinny wasn't the best friend to everyone in the frat, but he was my first real friend."
ni "And I think his fights with Tommy affected me a lot more than I realized."
scene ep12_np2_nick9 with dissolve
ni "I told Vinny about my crush on Heather when he still was a DIK, and do you know what he told me?"
scene ep12_np2_nick8 with dissolve
mc "What?"
scene ep12_np2_nick9 with dissolve
ni "That I should go for it."
ni "He said it like it was a natural thing. To go for someone else's girl."
ni "If you want something, take it. He said."
scene ep12_np2_nick14 with dissolve
ni "That was shit advice, but I felt confident knowing I had him on my side."
ni "But it didn't lead anywhere with Heather."
scene ep12_np2_nick15 with dissolve
ni "I think that's why it was so easy for me to do that to Tommy when I got the chance."
ni "I only wanted Heather. I still do."
scene ep12_np2_nick14 with dissolve
ni "I'm not blaming Vinny for it. But I wanted you to know where I come from."
ni "I'm a fucking loser, [name]... You have no idea how that feels."
scene ep12_np2_nick16 with dissolve
mc "You're wrong. I know how that feels."
scene ep12_np2_nick15 with dissolve
ni "How could you? You're so damn cool all the time."
scene ep12_np2_nick16 with dissolve
mc "Dude, I was bullied when I was young. I was a loner too. I know how that feels."
scene ep12_np2_nick15 with dissolve
ni "But you're not like that at all now."
scene ep12_np2_nick16 with dissolve
mc "I decided to change and not be like that anymore."
mc "College gives you that chance. It resets your social life and gives you a do-over. I took it."
scene ep12_np2_nick17 with dissolve
mc "And honestly, if you hadn't told me this now, I wouldn't have guessed you were the same."
mc "You must have changed, too."
scene ep12_np2_nick15 with dissolve
ni "Like I said, being with the DIKs changed me for the better...and for the worse."
ni "Rusty and Jacob were willing to give me another shot."
ni "I'm here asking if you will, too. And if you don't... That's fine."
ni "I've said what I wanted to say."
scene ep12_np2_nick16 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Forgive Nick)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        


menu:
    "Give him another chance \n{size=-4}[m_c1][mod_choices[0]]":
        $ ep12_forgave_nick = True
        mc "I can forgive, but not forget."
        mc "*{i}Sigh{/i}* But I think everyone deserves a second chance."
        scene ep12_np2_nick19 with dissolve
        ni "Thank you, [name]. You have no idea how much that means to me."
        scene ep12_np2_nick18 with dissolve
        mc "I'm not a dictator, though. In this brotherhood, the majority vote should decide it."
        scene ep12_np2_nick15 with dissolve
        ni "I will talk to the rest of our brothers, too."
    "Don't give him another chance":
        $ ep12_forgave_nick = False
        scene ep12_np2_nick17 with dissolve
        mc "I can forgive, but not forget."
        mc "I'm not a dictator, but my vote is no."
        mc "If my brothers feel different, I'll respect the majority vote."
        scene ep12_np2_nick14 with dissolve
        ni "Ok... I hear you."
scene ep12_np2_nick16 with dissolve
mc "Good luck to you, Nick."
stop music fadeout 3
scene ep12_np2_nick15 with dissolve
ni "Thanks for listening to me."

if ep12_forgave_nick:
    $ new_bio("Nick", "Nick asked me to forgive him for his outburst. I chose to give him another chance.")
else:
    $ new_bio("Nick", "Nick asked me to forgive him for his outburst. I chose not to give him another chance.")

$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep12/licensed_music/track202.mp3"])
scene ep12_np2_game1
show screen dance_filter_screen
with dissolve
qu "Haha! That one seems to have gotten the lot of you."
scene ep12_np2_game13 with dissolve
mc "What's going on?"
scene ep12_np2_game14 with dissolve
tm "Quinn is hosting a drinking game. She wants everyone to get drunk, haha."
scene ep12_np2_game13 with dissolve
mc "It's about time. Midnight is approaching."
scene ep12_np2_game2 with dissolve
qu "Oh! I have a good one."
qu "Never have I ever...?"
scene ep12_np2_game15 with dissolve
qu "Fooled around with [name]."
scene ep12_np2_game16 with dissolve
mc "Say what?"
scene ep12_np2_game73 with dissolve
qu "You heard me. I see those eyes wander around the room."
scene ep12_np2_game7 with dissolve
qu "Never have I ever sucked, fucked, groped, made out, you name it...with that guy!"

$ calculateGirlsDrinking()

if "Jade" in ep12_drinking_list:
    scene ep12_np2_game32 with dissolve
    ja "*{i}Spits and coughs{/i}*"

if branchIsabella and not breakup:
    scene ep12_np2_game36 with dissolve
    $ renpy.pause()
    if maya_shiny_dress:
        scene ep12_np2_game40a with dissolve
    else:
        scene ep12_np2_game40b with dissolve
    $ renpy.pause()
    scene ep12_np2_game37 with dissolve
    $ renpy.pause()
    if "Jill" in ep12_drinking_list:
        $ ep12_girl_count += 1
        scene ep12_np2_game35 with dissolve
        $ renpy.pause()
    scene ep12_np2_game33 with dissolve
    sa "This is so not cool..."
elif branchSage and not breakup:
    scene ep12_np2_game33 with dissolve
    sa "This is so not cool..."
    if "Isabella" in ep12_drinking_list:
        scene ep12_np2_game36 with dissolve
        $ renpy.pause()
    $ ep12_girl_count += 1
    if maya_shiny_dress:
        scene ep12_np2_game40a with dissolve
    else:
        scene ep12_np2_game40b with dissolve
    $ renpy.pause()
    $ ep12_girl_count += 1
    scene ep12_np2_game37 with dissolve
    $ renpy.pause()
    if "Jill" in ep12_drinking_list:
        $ ep12_girl_count += 1
        scene ep12_np2_game35 with dissolve
        $ renpy.pause()
    scene ep12_np2_game33 with dissolve
    sa "Please... Don't encourage her."
elif branchJill and not breakup:
    scene ep12_np2_game34 with dissolve
    ji "..."
    if "Isabella" in ep12_drinking_list:
        scene ep12_np2_game36 with dissolve
        $ renpy.pause()
    $ ep12_girl_count += 1
    if maya_shiny_dress:
        scene ep12_np2_game40a with dissolve
    else:
        scene ep12_np2_game40b with dissolve
    $ renpy.pause()
    $ ep12_girl_count += 1
    scene ep12_np2_game37 with dissolve
    $ renpy.pause()
    scene ep12_np2_game33 with dissolve
    sa "This is so not cool..."
elif branchMayaJosy and not breakup:
    if maya_shiny_dress:
        scene ep12_np2_game39a with dissolve
    else:
        scene ep12_np2_game39b with dissolve
    js "I guess we have to drink."
    scene ep12_np2_game37 with dissolve
    $ renpy.pause()
    if maya_shiny_dress:
        scene ep12_np2_game40a with dissolve
    else:
        scene ep12_np2_game40b with dissolve
    $ renpy.pause()
    $ ep12_girl_count += 2
    if "Isabella" in ep12_drinking_list:
        scene ep12_np2_game36 with dissolve
        $ renpy.pause()
    if "Jill" in ep12_drinking_list:
        $ ep12_girl_count += 1
        scene ep12_np2_game35 with dissolve
        $ renpy.pause()
        if maya_shiny_dress:
            scene ep12_np2_game38a with dissolve
        else:
            scene ep12_np2_game38b with dissolve
        $ renpy.pause()
    scene ep12_np2_game33 with dissolve
    sa "This is so not cool..."
else:
    if "Isabella" in ep12_drinking_list:
        scene ep12_np2_game36 with dissolve
        $ renpy.pause()
    $ ep12_girl_count += 1
    if maya_shiny_dress:
        scene ep12_np2_game40a with dissolve
    else:
        scene ep12_np2_game40b with dissolve
    $ renpy.pause()
    $ ep12_girl_count += 1
    scene ep12_np2_game37 with dissolve
    $ renpy.pause()
    if "Jill" in ep12_drinking_list:
        $ ep12_girl_count += 1
        scene ep12_np2_game35 with dissolve
        $ renpy.pause()
    scene ep12_np2_game33 with dissolve
    sa "This is so not cool..."

if "Quinn" in ep12_drinking_list:
    scene ep12_np2_game23 with dissolve
    qu "Whoops! Turned out I did it."
    qu "Cheers, everyone!"
    scene ep12_np2_game24 with dissolve
    $ renpy.pause()

if "Tiffani" in ep12_drinking_list:
    scene ep12_np2_game47 with dissolve
    ti "I'll drink, but not to something as innocent as a kiss."
    if "Becky" in ep12_drinking_list:
        scene ep12_np2_game48 with dissolve
        bc "Me too."
        scene ep12_np2_game49 with dissolve
        $ renpy.pause()
    else:
        scene ep12_np2_game48 with dissolve
        bc "No way!"
elif "Becky" in ep12_drinking_list:
    scene ep12_np2_game51 with dissolve
    bc "And it wasn't just a kiss!"
    scene ep12_np2_game50 with dissolve
    $ renpy.pause()

if branchZoey:
    scene ep12_np2_game52 with dissolve
else:
    scene ep12_np2_game53 with dissolve
$ renpy.pause()

if "Sarah" in ep12_drinking_list:
    scene ep12_np2_game20 with dissolve
    sar "I'll drink to fucking!"
    if "Melanie" in ep12_drinking_list:
        scene ep12_np2_game21 with dissolve
        ml "Hear, hear."
elif "Melanie" in ep12_drinking_list:
    scene ep12_np2_game22 with dissolve
    ml "He's great in bed. I have to drink."

if "Heather" in ep12_drinking_list:
    if ep11_dildo_sucking_girl == "Heather":
        scene ep12_np2_game58 with dissolve
        he "Does getting him hard during a dildo sucking game count?"
        scene ep12_np2_game59 with dissolve
        qu "Fucking drink, girl."
    else:
        scene ep12_np2_game59 with dissolve
        $ renpy.pause()

if "Elena" in ep12_drinking_list:
    scene ep12_np2_game57 with dissolve
    qu "Oh, Elena?"

if "Sally" in ep12_drinking_list:
    scene ep12_np2_game60 with dissolve
    $ renpy.pause()

if "Lily" in ep12_drinking_list:
    if ep12_rolling:
        scene ep12_np2_game62 with dissolve
    else:
        scene ep12_np2_game63 with dissolve
    $ renpy.pause()

if "Ashley" in ep12_drinking_list:
    scene ep12_np2_game54 with dissolve
    qu "I can spot some shameful drinking in the audience."

if "Camila" in ep12_drinking_list:
    scene ep12_np2_game55 with dissolve
    cam "WOO!!!"

if "Riona" in ep12_drinking_list:
    scene ep12_np2_game56 with dissolve
    $ renpy.pause()

if "Bianca" in ep12_drinking_list:
    scene ep12_np2_game61 with dissolve
    $ renpy.pause()

if "Nicole" in ep12_drinking_list:
    scene ep12_np2_game64 with dissolve
    $ renpy.pause()
if "Sandy" in ep12_drinking_list:
    scene ep12_np2_game65 with dissolve
    sn "Chugging it!"
if "Tania" in ep12_drinking_list:
    scene ep12_np2_game66 with dissolve
    $ renpy.pause()
if "Rose" in ep12_drinking_list:
    scene ep12_np2_game67 with dissolve
    $ renpy.pause()

if "Kylie" in ep12_drinking_list:
    scene ep12_np2_game25 with dissolve
    sar "You two should drink, girls."
    scene ep12_np2_game26 with dissolve
    ky "Why? I never did anything with him."
    scene ep12_np2_game25 with dissolve
    sar "*{i}Whispers{/i}* Remember the glory hole?"
    scene ep12_np2_game27 with dissolve
    ky "*{i}Gasps{/i}* No way! Fuck..."
    scene ep12_np2_game28 with dissolve
    $ renpy.pause()
    scene ep12_np2_game29 with dissolve
    osc "No... Why are you drinking, Tara?"
elif "Tara" in ep12_drinking_list:
    scene ep12_np2_game31 with dissolve
    $ renpy.pause()
    scene ep12_np2_game30 with dissolve
    osc "No... Why are you drinking, Tara?"


if "Mia" in ep12_drinking_list:
    scene ep12_np2_game68 with dissolve
    er "Does mine count?"
    scene ep12_np2_game70 with dissolve
    mia "Nah, but mine sure does."
    scene ep12_np2_game68 with dissolve
    er "I'll drink some; it felt sexual."
    scene ep12_np2_game69 with dissolve
    $ renpy.pause()

if "Felicia" in ep12_drinking_list:
    if "Leanne" in ep12_drinking_list:
        scene ep12_np2_game72 with dissolve
    else:
        scene ep12_np2_game71 with dissolve
    $ renpy.pause()

if ep12_girl_count > 10:
    $ ep12_mc_slut = True
    scene ep12_np2_game3 with dissolve
    if steamAchievements:
        $ achievement.grant("IDS3_47")
        init:
            $ achievement.register("IDS3_47")
        $ achievement.Sync()
    qu "Holy shit! I think we found the real slut in here, and it's not a girl. Haha!"
elif ep12_girl_count > 8:
    $ ep12_mc_slut = True
    scene ep12_np2_game4 with dissolve
    qu "Wow! I'm not gonna lie, I knew it was a lot, but it was more than I expected. [name] is a slut!"
elif ep12_girl_count > 5:
    $ ep12_mc_slut = False
    scene ep12_np2_game5 with dissolve
    qu "Meh, I was sure it was going to be more."
else:
    $ ep12_mc_slut = False
    scene ep12_np2_game5 with dissolve
    qu "Either we have a bunch of liars in here, or [name] has like zero game. Haha!"
    if not breakup and branchMayaJosy:
        if maya_shiny_dress:
            scene ep12_np2_game39ac with dissolve
        else:
            scene ep12_np2_game39bc with dissolve
        $ renpy.pause()
if ep12_mc_slut and persistent.mod_wtenabled:
   "scrappy" "Remove the slut variable? Can keep your paths open."
   menu:
       "Yes":
          $ ep12_mc_slut=False
       "No":
          pass
    
if ep12_mc_slut:
    if not breakup and branchJill:
        scene ep12_np2_game41 with dissolve
        ji "Oh my God..."
        scene ep12_np2_game46 with dissolve
        mc "Jill..."
    elif not breakup and branchMayaJosy:
        if maya_shiny_dress:
            scene ep12_np2_game43 with dissolve
        else:
            scene ep12_np2_game43b with dissolve
        js "Damn, [name]..."
        my "Yeah, that's a lot."
        if maya_shiny_dress:
            scene ep12_np2_game81 with dissolve
        else:
            scene ep12_np2_game81a with dissolve
        js "[name]? Are you ok?"
        if maya_shiny_dress:
            scene ep12_np2_game82 with dissolve
        else:
            scene ep12_np2_game82a with dissolve
        mc "I'm fine, but embarrassed by it all."
        if maya_shiny_dress:
            scene ep12_np2_game81 with dissolve
        else:
            scene ep12_np2_game81a with dissolve
        js "We get it... Um... Can you meet us on the balcony? There's something we need to discuss."
    elif not breakup and branchIsabella:
        scene ep12_np2_game42 with dissolve
        $ renpy.pause()
        scene ep12_np2_game45 with dissolve
        mc "..."
    elif not breakup and branchSage:
        scene ep12_np2_game45 with dissolve
        mc "..."
        scene ep12_np2_game44 with dissolve
        sa "I can't fucking believe her!"
    elif branchZoey:
        scene ep12_np2_game74 with dissolve
        zo "That's quite a body count you got yourself there."
        scene ep12_np2_game75 with dissolve
        mc "I told you..."
        scene ep12_np2_game74 with dissolve
        zo "Yeah, you did."
    else:
        if affinity == "DIK":
            scene ep12_np2_game19 with dissolve
            mc "I guess I have to drink too. Cheers, girls!"
        else:
            scene ep12_np2_game17 with dissolve
            mc "Pff... I'm not a slut."
        if ep12_nikita:
            scene ep12_np2_game83 with dissolve
            $ renpy.pause()
            if "ep12_np2_nik_label" in event_list:
                $ event_list.remove("ep12_np2_nik_label")
                $ task_list[4] = ""
else:
    if not breakup and branchJill:
        scene ep12_np2_game77 with dissolve
        ji "Um... Are you ok?"
        scene ep12_np2_game78 with dissolve
        mc "I'm embarrassed."
        scene ep12_np2_game77 with dissolve
        ji "You have nothing to be embarrassed about."
        ji "Let's get out of here."
    elif not breakup and branchMayaJosy:
        if maya_shiny_dress:
            scene ep12_np2_game81 with dissolve
        else:
            scene ep12_np2_game81a with dissolve
        js "[name]? Are you ok?"
        if maya_shiny_dress:
            scene ep12_np2_game82 with dissolve
        else:
            scene ep12_np2_game82a with dissolve
        mc "I'm fine, but embarrassed by it all."
        if maya_shiny_dress:
            scene ep12_np2_game81 with dissolve
        else:
            scene ep12_np2_game81a with dissolve
        js "We get it... Um... Can you meet us on the balcony? There's something we need to discuss."
    elif not breakup and branchIsabella:
        scene ep12_np2_game79 with dissolve
        isa "I'd give you a hug now if I could."
        scene ep12_np2_game80 with dissolve
        mc "Meet me on the balcony in a couple of minutes..."
    elif not breakup and branchSage:
        scene ep12_np2_game44 with dissolve
        sa "I can't fucking believe her!"
    elif branchZoey:
        scene ep12_np2_game74 with dissolve
        zo "Are you ok?"
        scene ep12_np2_game75 with dissolve
        mc "I've gotten used to being embarrassed. It's not the worst thing that happened to me this year."
    else:
        scene ep12_np2_game18 with dissolve
        $ renpy.pause()
        if ep12_nikita:
            scene ep12_np2_game84 with dissolve
            $ renpy.pause()

scene ep12_np2_game6 with dissolve
qu "Hahaha!"
if branchZoey:
    scene ep12_np2_game76 with dissolve
    zo "What the hell is her deal?"
    scene ep12_np2_game75 with dissolve
    mc "She likes to play weird games with people."
    if zoey_dik:
        scene ep12_np2_game76 with dissolve
        zo "If she fucks around like that, I'm gonna make her find out."
        scene ep12_np2_game75 with dissolve
        mc "Don't get involved with her."
    else:
        scene ep12_np2_game74 with dissolve
        zo "I don't like her."
        scene ep12_np2_game75 with dissolve
        mc "I think most in here don't either."

scene ep12_np2_game8 with dissolve
sa "That's enough of that game."
scene ep12_np2_game9 with dissolve
qu "What? We're having fun!"
scene ep12_np2_game10 with dissolve
sa "That's so fucking disrespectful. I don't even know where to begin."
scene ep12_np2_game12 with dissolve
qu "You're overreacting as usual. Get off your high horse."
scene ep12_np2_game11 with dissolve
"*{i}Audience gasps{/i}*"

if ep12_mc_slut:
    $ new_bio("Quinn", "During a drinking game, Quinn outed me as a slut in front of everyone at the New Year's Eve party.")
else:
    $ new_bio("Quinn", "During a drinking game, Quinn tried to embarrass me in front of everyone at the New Year's Eve party.")

$ map_system_list = []
$ map_system_list.append(["ep12_np_2f_corridor","ep12_np_2f_corridor_label","2F corridor"])
$ map_system_list.append(["ep12_np_corridor2","ep12_np_corridor_label","3F corridor"])
$ map_system_list.append(["ep12_np_balconyb","ep12_np_balcony_label","Balcony"])
$ map_system_list.append(["ep12_np_party_roomb","ep12_np_party_room_label","Dance floor"])
$ map_system_list.append(["ep12_np_dining2","ep12_np_dining_label","Dining room"])
$ map_system_list.append(["ep12_np_outsideb","ep12_np_outside_label","Outside"])

$ current_task = ""
$ freeRoamID = "ep12_3c"
if "sally_break" in event_list:
    $ event_list = []
    $ event_list.append("sally_break")
else:
    $ event_list = []
$ event_list.append("ep12_np_dj_label")
$ event_list.append("key")
$ event_list.append("table")
$ event_list.append("part2")
$ event_list.append("part3")


$ task_list = ["",""]
$ optional_task_list = [""]

if "Tara" in ep12_drinking_list:
    $ event_list.append("ep12_np2_ot_label")
    if persistent.mod_wtenabled:
        $ task_list[1] = "Talk to Oscar (3F corridor)"
    else:
        $ task_list[1] = "Talk to Oscar"
if not (not breakup and branchSage):
    $ event_list.append("ep12_np2_mjmc_label")

if ep12_mc_slut:
    if ep11_quinn_question[0] and ep11_quinn_question[1] and ep12_riona_side == "Quinn" and not ep12_quinn_ditch and not branchZoey:
        $ event_list.append("ep12_np2_ari_label")
    else:
        if not branchZoey:
            $ event_list.append("ep12_np2_ari_label")
        $ event_list.append("ep12_np2_mchen_label")
$ updateTaskList()

if not breakup and branchJill:
    jump ep12_np2_jmc_label
elif not breakup and branchMayaJosy:
    jump endEvent
elif not breakup and branchIsabella:
    jump ep12_np2_bmc_label
elif not breakup and branchSage:
    stop music fadeout 3
    jump ep12_np2_smc_label
elif branchZoey:
    jump ep12_np2_zmc_label
elif ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch:
    jump ep12_np2_mchen_label
else:
    jump endEvent

label ep12_np2_mchen_label:
scene ep12_np2_mchen1
hide screen dance_filter_screen
with dissolve
che "Bro!!! LEGEND!"
scene ep12_np2_mchen2 with dissolve
mc "What?"
scene ep12_np2_mchen3 with dissolve
che "How did you bag that many chicks?"
che "Teach me!"
scene ep12_np2_mchen4 with dissolve
che "HOW!?"
if ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch and (not branchZoey or wt_ep11_zoey_kiss_others):
    jump ep12_np2_qmc_label
jump endEvent

label ep12_np2_zmc_label:
scene ep12_np2_zmc1 with dissolve
zo "Looks like she's getting scolded by Sage."
scene ep12_np2_zmc2 with dissolve
$ renpy.pause()

scene ep12_np2_zmc3 with dissolve
$ renpy.pause()
if zoey_dik:
    scene ep12_np2_zmc4 with dissolve
    $ renpy.pause()
    play sound "sound_effects/shove.mp3"
    scene ep12_np2_zmc5 with vpunch
    $ renpy.pause()
    scene ep12_np2_zmc6 with dissolve
    qu "Hey! What the fuck?"
    scene ep12_np2_zmc7 with dissolve
    mc "Stop it now."
    scene ep12_np2_zmc8 with dissolve
    mc "You shouldn't have done that."
    scene ep12_np2_zmc9 with dissolve
    zo "I wouldn't have if she hadn't tried to get a second shot in."
else:
    scene ep12_np2_zmc10 with dissolve
    zo "Hey."
    scene ep12_np2_zmc11 with dissolve
    zo "*{i}Smack{/i}*"
    scene ep12_np2_zmc12 with dissolve
    $ renpy.pause()
scene ep12_np2_zmc13 with dissolve
mc "Dance with me."
scene ep12_np2_zmc14 with dissolve
zo "You can't dance."
scene ep12_np2_zmc13 with dissolve
mc "You don't have to tell me."
mc "But if you put your arms around me, no one will notice."
scene ep12_np2_zmc15 with dissolve
zo "I think that Quinn bitch is jealous or something."
scene ep12_np2_zmc16 with dissolve
mc "Jealous of me?"
scene ep12_np2_zmc15 with dissolve
zo "No. In general. Some people get their kicks from putting others down."
scene ep12_np2_zmc16 with dissolve
mc "Where do you get your kicks from?"
scene ep12_np2_zmc17 with dissolve
zo "Skateboarding. Drawing. Headbanging to bangers."
scene ep12_np2_zmc18 with dissolve
mc "Yeah, this isn't your kind of music."
scene ep12_np2_zmc17 with dissolve
zo "It works for parties. Could you imagine them playing heavy metal for this crowd?"
scene ep12_np2_zmc18 with dissolve
mc "HAHA! I'm picturing all the girls headbanging in their dresses."
scene ep12_np2_zmc17 with dissolve
zo "There's no way they would. You know how most get."
scene ep12_np2_zmc19 with dissolve
mc "Yeah. \"Turn that noise off!\""
scene ep12_np2_zmc20 with dissolve
zo "\"Does it have to be this loud?\""
scene ep12_np2_zmc19 with dissolve
mc "\"You can't hear what he's singing. Why is he screaming?\""
scene ep12_np2_zmc20 with dissolve
zo "Yep. That's them. But not us."
scene ep12_np2_zmc18 with dissolve
mc "It would be amazing to go to a show together."
scene ep12_np2_zmc17 with dissolve
zo "ShitFaced has a national tour next year. I'm just saying..."
scene ep12_np2_zmc18 with dissolve
mc "To see them live... That would be a dream."
scene ep12_np2_zmc17 with dissolve
zo "Let's do it."
scene ep12_np2_zmc22 with dissolve
mc "Isn't it expensive?"
scene ep12_np2_zmc21 with dissolve
zo "I don't think they'll play anywhere near us until summer or fall. We can save up for it."
zo "It can be our New Year's resolution."
scene ep12_np2_zmc22 with dissolve
mc "I can't promise that... But we can look into it."
scene ep12_np2_zmc21 with dissolve
zo "No! Come on. It has to be a promise."
zo "It's easy to say you'll do something and then bail."
scene ep12_np2_zmc22 with dissolve
mc "I promise to try."
scene ep12_np2_zmc21 with dissolve
zo "Boo... Promise."
scene ep12_np2_zmc19 with dissolve
mc "I promise."
scene ep12_np2_zmc20 with dissolve
zo "There you go."
scene ep12_np2_zmc23 with dissolve
"*{i}Smack{/i}*"

if ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch:
            jump ep12_np2_mchen_label
jump endEvent

label ep12_np2_jmd_label:
if maya_shiny_dress:
    scene ep12_np2_jmd1
    show screen dance_filter_screen
    with dissolve
else:
    scene ep12_np2_jmd1b
    show screen dance_filter_screen
    with dissolve
my "Come! You haven't danced yet!"
if maya_shiny_dress:
    scene ep12_np2_jmd2 with dissolve
else:
    scene ep12_np2_jmd2b with dissolve
mc "How would you know?"
if maya_shiny_dress:
    scene ep12_np2_jmd1 with dissolve
else:
    scene ep12_np2_jmd1b with dissolve
my "Well, have you?"
if maya_shiny_dress:
    scene ep12_np2_jmd2 with dissolve
else:
    scene ep12_np2_jmd2b with dissolve
mc "No..."
if maya_shiny_dress:
    scene ep12_np2_jmd1 with dissolve
else:
    scene ep12_np2_jmd1b with dissolve
my "Then you're not getting out of it."
if maya_shiny_dress:
    scene ep12_np2_jmd3 with dissolve
else:
    scene ep12_np2_jmd3b with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
play sound "sound_effects/camera_shutter.mp3"
scene ep12_np2_jmd4 with dissolve
"*{i}Camera shutter{/i}*"
if maya_shiny_dress:
    scene ep12_np2_jmd5 with dissolve
else:
    scene ep12_np2_jmd5b with dissolve
mc "Who invited the paparazzi?"
if maya_shiny_dress:
    scene ep12_np2_jmd6 with dissolve
else:
    scene ep12_np2_jmd6b with dissolve
js "Don't mind me. Do your thing!"
if maya_shiny_dress:
    scene ep12_np2_jmd5 with dissolve
else:
    scene ep12_np2_jmd5b with dissolve
mc "Nah, now I feel the pressure."
scene ep12_np2_jmd9 with dissolve
bc "Josy!!! Come!!! You should totally take a picture of me for your blog!"
scene ep12_np2_jmd7 with dissolve
js "A little help here?"
scene ep12_np2_jmd10 with dissolve
mc "She totally should, Becky! You'd be perfect for it!"
if maya_shiny_dress:
    scene ep12_np2_jmd6 with dissolve
else:
    scene ep12_np2_jmd6b with dissolve
js "Thanks..."
if maya_shiny_dress:
    scene ep12_np2_jmd8 with dissolve
else:
    scene ep12_np2_jmd8b with dissolve
my "Haha! That was mean."

$ updateTaskList()
if "ep12_np2_jmd_label" not in event_list or "ep12_np2_jomc_label" not in event_list or "ep12_np2_lily_label" not in event_list or "ep12_np2_ji_label" not in event_list:
    $ task_list[8] = ""
elif "ep12_np2_ji_label" in event_list or "ep12_np2_jomc_label" in event_list or "ep12_np2_lily_label" in event_list:
    $ task_list[8]=task_list[8].replace("Find Josy and Maya (Dance floor)","")
    $ task_list[8]=task_list[8].replace("Find Josy and Maya","")
else:
    $ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_ji_label:
scene ep12_np2_ji1 with dissolve
ji "How's the photography coming along, [name]?"
scene ep12_np2_ji2 with dissolve
mc "Oh, right..."
scene ep12_np2_ji3 with dissolve
ji "You're kidding. Didn't you take any pictures?"
scene ep12_np2_ji4 with dissolve
mc "Uh... I took these."
scene ep12_np2_ji5 with dissolve
ji "Haha! Those are the ones that Sage took."
scene ep12_np2_ji4 with dissolve
mc "Right..."
scene ep12_np2_ji6 with dissolve
mc "Oh! But I also have this one, but it's not from the party"
mc "Remember that monkey face I talked about. I scanned Mom's picture of it to show you."
scene ep12_np2_ji7 with dissolve
mc "That's Mom doing the monkey, haha."
scene ep12_np2_ji8 with dissolve
mc "It's funny, isn't it?"
scene ep12_np2_ji9 with dissolve
ji "[name]... What is this?"
scene ep12_np2_ji8 with dissolve
mc "That's my Mom."
scene ep12_np2_ji9 with dissolve
ji "No... Behind her... That's my house."
scene ep12_np2_ji10 with dissolve
mc "What?"
scene ep12_np2_ji11 with dissolve
ji "In the background! That's my house!"
ji "Why do you have this picture? When was it taken? How?"
scene ep12_np2_ji12 with dissolve
mc "It was in my Mom's diary. She got a photo album from her friends."
mc "I don't know when or where it was taken. But it was before her family sold their house and moved into a hotel they bought."
scene ep12_np2_ji13 with dissolve
ji "That house?"
scene ep12_np2_ji12 with dissolve
mc "I wouldn't know. Are you sure it's the same house?"
scene ep12_np2_ji13 with dissolve
ji "I think I'd recognize it."
scene ep12_np2_ji14 with dissolve
ji "Bianca!!! Get over here!"
scene ep12_np2_ji15 with dissolve
bia "What's up!?"
scene ep12_np2_ji21 with dissolve
ji "[name] showed me something mindblowing!"
ji "Look! That's his Mom taking a picture in front of my house."
ji "Can you tell him that's my house? He doesn't believe it is."
scene ep12_np2_ji17 with dissolve
bia "Yeah. It is."
scene ep12_np2_ji20 with dissolve
bia "Wait a minute! That's my aunt!"
scene ep12_np2_ji21 with dissolve
ji "Oh, wow! It is! She looks so young, and so much like you."
scene ep12_np2_ji16 with dissolve
mc "Hold on... That's not your aunt... That's-"
scene ep12_np2_ji15 with dissolve
bia "Miranda!?"
scene ep12_np2_ji16 with dissolve
mc "Miranda..."
scene ep12_np2_ji15 with dissolve
bia "It is her, [name]."
scene ep12_np2_ji22 with dissolve
ji "And that's my house."
scene ep12_np2_ji16 with dissolve
mc "Did your aunt live in that house?"
scene ep12_np2_ji17 with dissolve
bia "No, but Dad is the reason why Jill's parents bought the place."
scene ep12_np2_ji21 with dissolve
ji "Maybe Miranda is the reason your dad knew it was for sale?"
scene ep12_np2_ji16 with dissolve
mc "Did you ever see the other girls in the picture?"
scene ep12_np2_ji17 with dissolve
bia "I'm not that close to my aunt that I'd know her friends. But none of them rings a bell."
bia "Who's your mom?"
scene ep12_np2_ji16 with dissolve
mc "The monkey..."
scene ep12_np2_ji18 with dissolve
bia "Haha! Of course! She looks just like you."
scene ep12_np2_ji19 with dissolve
mc "You think?"
scene ep12_np2_ji22 with dissolve
ji "And the other one was Vivian, you said?"
scene ep12_np2_ji16 with dissolve
mc "Yeah."
scene ep12_np2_ji22 with dissolve
ji "Maybe it was her house..."
ji "Or maybe... What if it were your mom's house and they sold it to my parents?"
scene ep12_np2_ji23 with dissolve
mc "Didn't Geoff say something about why it was sold? There was some money issue or something."
scene ep12_np2_ji22 with dissolve
ji "Yes. The previous owners needed money fast."
scene ep12_np2_ji23 with dissolve
mc "It doesn't line up with what I've read in her diary... They were selling their old home, but they weren't in debt from the sound of it."
scene ep12_np2_ji22 with dissolve
ji "It doesn't mean they were in debt, [name]. Sometimes you need to liquidate assets."
ji "I have to ask Mom and Dad about this picture. Can you send it to me?"
scene ep12_np2_ji16 with dissolve
mc "Yeah... I'm confused. I don't know what I feel."
mc "I think I'm in shock..."
scene ep12_np2_ji24 with dissolve
ji "How crazy would it be if I were raised in your mom's old home?"
ji "It's destiny, [name]. I can feel it."
scene ep12_np2_ji25 with dissolve
$ renpy.pause()
$ updateTaskList()
if "ep12_np2_jmd_label" in event_list or "ep12_np2_jomc_label" in event_list or "ep12_np2_lily_label" in event_list:
    $ task_list[8]=task_list[8].replace("\nTalk to Jill (Dance floor)","")
    $ task_list[8]=task_list[8].replace("\nTalk to Jill","")
else:
    $ task_list[8] = ""
    
if "ep12_np2_jmd_label" not in event_list or "ep12_np2_jomc_label" not in event_list or "ep12_np2_lily_label" not in event_list or "ep12_np2_ji_label" not in event_list:
    $ task_list[8] = ""
$ updateTaskList()
$ new_bio("Jill", "Jill discovered that her family's house was in the background of my Mom's picture with her friends.")
$ new_bio("Bianca", "Bianca discovered that her aunt was in the background of my Mom's picture with her friends.")
$ new_bio("Lynette", "Jill's house seemed to be connected to Mom in some way.")
jump endEvent

label ep12_np2_zu_label:
$ guideSuggestedPage = 263
scene ep12_np2_zu1 with dissolve
menu:
    "What are you doing here?":
        mc "What are you doing here?"
        if zoey_dik:
            scene ep12_np2_zu2 with dissolve
            zo "Hello to you too..."
            zo "Your brothers invited me."
            scene ep12_np2_zu3 with dissolve
            mc "I wish you had let me know."
            scene ep12_np2_zu2 with dissolve
            zo "Let me get it straight. Is it ok for you to barge into my home at Christmas unannounced, but I can't show up to a party with an invitation?"
        else:
            scene ep12_np2_zu4 with dissolve
            zo "Your brothers invited me."
            scene ep12_np2_zu3 with dissolve
            mc "I wish you had let me know."
            scene ep12_np2_zu4 with dissolve
            zo "I wasn't sure how you'd react and I wanted to come."
    "Who invited you?":
        mc "I was surprised to see you. Who invited you?"
        if zoey_dik:
            scene ep12_np2_zu2 with dissolve
            zo "Your brothers did."
            scene ep12_np2_zu3 with dissolve
            mc "I wish you had let me know."
            scene ep12_np2_zu2 with dissolve
            zo "Let me get it straight. Is it ok for you to barge into my home at Christmas unannounced, but I can't show up to a party with an invitation?"
        else:
            scene ep12_np2_zu4 with dissolve
            zo "Your brothers did."
            scene ep12_np2_zu3 with dissolve
            mc "I wish you had let me know."
            scene ep12_np2_zu4 with dissolve
            zo "I wasn't sure how you'd react and I wanted to come."
scene ep12_np2_zu3 with dissolve
mc "Did you come here to talk to me or hang out with my friends?"
if zoey_dik:
    scene ep12_np2_zu5 with dissolve
    zo "They are my friends too. I had no other plans for tonight and didn't want to spend it alone."
    scene ep12_np2_zu7 with dissolve
    mc "Why are you getting defensive?"
    scene ep12_np2_zu5 with dissolve
    zo "Well, what do you want coming at me like that?"
    scene ep12_np2_zu7 with dissolve
    mc "I'm not coming at you. Stop trying to pick a fight."
    scene ep12_np2_zu8 with dissolve
    zo "..."
    scene ep12_np2_zu9 with dissolve
    zo "This isn't gonna work, is it?"
else:
    scene ep12_np2_zu6 with dissolve
    zo "I had no other plans for tonight, and I didn't want to spend it alone."
    zo "I wasn't sure if you were ready to talk."
    scene ep12_np2_zu7 with dissolve
    mc "Do you feel ready?"
    scene ep12_np2_zu6 with dissolve
    zo "Yeah. I know how I feel."
    zo "You may not feel the same, but I want to stay friends."
    zo "That way you'd still be in my life, even if it's not the way I had hoped."
scene ep12_np2_zu7 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Zoey Friends)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]    
                        if branchSage:
                            $ mod_choices[6]="(Can end Sage's path)"
menu:
    "Stay friends with Zoey \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[6]]":
        $ ep12_zoey_friend = True
        if zoey_dik:
            mc "Not if this is how we talk to each other."
            mc "Let's dial it back."
            scene ep12_np2_zu8 with dissolve
            mc "I still want to be your friend, Zoey."
            mc "But we have to find a way that works for both of us."
            scene ep12_np2_zu12 with dissolve
            mc "It will be tough, but you mean too much to me."
            mc "It's because of you that I am who I am today. Well... You and Dad."
            mc "I'm willing to give it another shot, but only if you feel the same."
        else:
            scene ep12_np2_zu12 with dissolve
            mc "I feel the same. It will be hard, but I still want to be your friend, Zoey."
            mc "You mean so much to me."
            mc "It's because of you that I am who I am today."
            mc "Well... You and Dad."
        scene ep12_np2_zu13 with dissolve
        zo "Friends..."
        scene ep12_np2_zu14 with dissolve
        mc "Strangers shake hands. Friends hug."
        scene ep12_np2_zu15 with dissolve
        zo "Thank you, [name]... Thank you for not giving up on me."
        scene ep12_np2_zu16 with dissolve
        mc "You were there for me when I was at a low point in my life."
        mc "There's no question about it. I'll be there for you, too."
        mc "We just have to get past this awkward phase. And we will."
    "End friendship":
        $ ep12_zoey_friend = False
        scene ep12_np2_zu8 with dissolve
        if zoey_dik:
            mc "If we can't even be at the same party without fighting, how do you think it will work in college?"
            scene ep12_np2_zu5 with dissolve
            zo "You don't want me to come now?"
            scene ep12_np2_zu7 with dissolve
            mc "That's not what I'm saying."
            scene ep12_np2_zu5 with dissolve
            zo "It sounds like it. I'm not going anywhere."
            zo "If I get accepted, I'm taking that chance. And that's not because of you, it's because of me and my ambitions."
            scene ep12_np2_zu9 with dissolve
            zo "Friend or not, you have to find a way to be cool with that."
            scene ep12_np2_zu8 with dissolve
            mc "We're not gonna be friends anymore, Zoey."
            mc "Thank you for everything you did growing up with me."
            scene ep12_np2_zu10 with dissolve
            mc "You were a fantastic friend, and I will always remember our friendship."
            mc "But we have outgrown each other. It's too hard for me to continue having you in my life."
            if not branchAlone and not breakup and tc < 5:
                if branchMayaJosy:
                    mc "And out of respect to my girlfriends... I think this is for the best."
                else:
                    mc "And out of respect to my girlfriend... I think this is for the best."
            mc "I think we both will be happier without each other."
            scene ep12_np2_zu11 with dissolve
            mc "I don't care if you want to stick around or hang out with my friends."
            mc "You do what you want, but now you know how I feel."
            mc "Good luck to you."
        else:
            mc "You're right... I don't feel the same way you do."
            mc "I don't think I can be your friend anymore, Zoey."
            mc "Thank you for everything you did growing up with me."
            scene ep12_np2_zu10 with dissolve
            mc "You were a fantastic friend, and I will always remember our friendship."
            mc "But we have outgrown each other. It's too hard for me to continue having you in my life."
            if not branchAlone and not breakup and tc < 5:
                if branchMayaJosy:
                    mc "And out of respect to my girlfriends... I think this is for the best."
                else:
                    mc "And out of respect to my girlfriend... I think this is for the best."
            mc "I think we both will be happier without each other."
            scene ep12_np2_zu8 with dissolve
            mc "If you decide to come here to B&R and hang around my friends and such, that's up to you."
            mc "I wouldn't mind it. You do what you want, but it will be without me."
            scene ep12_np2_zu9 with dissolve
            zo "Is that what you want?"
            scene ep12_np2_zu11 with dissolve
            mc "It's what I need."
            mc "Good luck to you."
        scene ep12_np2_zu17 with dissolve
        $ renpy.pause()
$ task_list[9] = ""
$ updateTaskList()
if ep12_zoey_friend:
    $ new_bio("Zoey", "I chose to stay friends with Zoey.")
else:
    $ new_bio("Zoey", "I chose to end my friendship with Zoey.")
jump endEvent

label ep12_np2_cg_label:
if not breakup and not ep4_toldDerekAboutJade and (jade_state == 0 or wt_ep9_branch_numbers > 1):
    if maya_shiny_dress:
        scene ep12_np2_cg1 with dissolve
    else:
        scene ep12_np2_cg1b with dissolve
    mc "Did you guys break out the cards?"
    scene ep12_np2_cg2 with dissolve
    sa "Why not? You planned for this, but no one cared to play so far."
    scene ep12_np2_cg3 with dissolve
    mc "I thought people would get bored, but everyone has kept busy eating, dancing, and drinking."
    if maya_shiny_dress:
        scene ep12_np2_cg4 with dissolve
    else:
        scene ep12_np2_cg4b with dissolve
    my "The party has been great, [name]. You should feel proud."
    scene ep12_np2_cg2 with dissolve
    sa "Yeah, I'm most impressed that you guys didn't fight the tri-alphas. Kudos to you."
    scene ep12_np2_cg5 with dissolve
    de "The line separating us helped a lot."
    if maya_shiny_dress:
        scene ep12_np2_cg1 with dissolve
    else:
        scene ep12_np2_cg1b with dissolve
    menu:
        "Join them":
            mc "Can I join you?"
        "Don't play cards":
            mc "Well, have fun! I'm off to drink some more."
            $ task_list[0] = ""
            $ updateTaskList()
            jump endEvent
    if maya_shiny_dress:
        scene ep12_np2_cg5 with dissolve
    else:
        scene ep12_np2_cg5b with dissolve
    de "Yeah, we're just getting started."
    if maya_shiny_dress:
        scene ep12_np2_cg6 with dissolve
    else:
        scene ep12_np2_cg6b with dissolve
    my "How do you play this game again?"
    scene ep12_np2_cg7 with dissolve
    sa "This game is one of my favorites. It's called \"Wrong Questions and Answers\"."
    sa "It's a game where you try to be as funny as possible by playing cards that you think will make each other laugh."
    scene ep12_np2_cg8 with dissolve
    mc "That sounds fun. Are the rules hard to learn?"
    scene ep12_np2_cg7 with dissolve
    sa "Not at all."
    scene ep12_np2_cg9 with dissolve
    sa "You get five answer cards in your hand. And you can swap up to three answer cards during the game."
    my "Why would I want to swap an answer card?"
    sa "Let's say you get a boring answer card. Then you can exchange it."
    scene ep12_np2_cg10 with dissolve
    sa "Then we take turns reading from a question card."
    sa "The person who reads the question card is also the judge for that round."
    sa "And the rest will try to make him or her laugh."
    scene ep12_np2_cg7 with dissolve
    sa "That means you gotta know the judge's humor and try to play the answer card that fits best."
    sa "For example, I have a feeling Derek will like more immature jokes than Maya."
    scene ep12_np2_cg11 with dissolve
    de "Your feeling would be correct. Haha!"
    scene ep12_np2_cg7 with dissolve
    sa "Anyway, all players except the judge play an answer card, and the judge will decide the winner without knowing whose card is whose."
    sa "First to five points wins."
    if maya_shiny_dress:
        scene ep12_np2_cg12 with dissolve
    else:
        scene ep12_np2_cg12b with dissolve
    my "You guys will have to remind me of those rules."
    scene ep12_np2_cg13 with dissolve
    sa "Don't worry. It's easy to follow along when you play."
    scene ep12_np2_cg11 with dissolve
    de "Let's start and see how it goes."
    scene ep12_np2_cg13 with dissolve
    sa "Yeah. Derek, you can start as the judge. Everyone, take five answer cards. You may read them, but not show them to anyone."
    jump ep12_cg_main_label
else:
    if maya_shiny_dress:
        scene ep12_np2_cg14 with dissolve
    else:
        scene ep12_np2_cg14b with dissolve
    my "Hahaha! That's so funny!"
    scene ep12_np2_cg15 with dissolve
    de "What? You gotta be joking. It's not as funny as \"big butt\"."
    if maya_shiny_dress:
        scene ep12_np2_cg14 with dissolve
    else:
        scene ep12_np2_cg14b with dissolve
    my "Haha, to me it is!"
    scene ep12_np2_cg16 with dissolve
    sa "You can't argue with the judge, Derek."
    scene ep12_np2_cg17 with dissolve
    $ renpy.pause()
    scene ep12_np2_cg18 with dissolve
    sa "Alright, it's my turn!"
    scene ep12_np2_cg19 with dissolve
    $ renpy.pause()
    scene ep12_np2_cg20 with dissolve
    $ renpy.pause()
    $ task_list[0] = ""
    $ updateTaskList()
    jump endEvent

label ep12_cg_main_label:
$ cg_init_card_game()
show screen cg_ol_screen
$ cg_get_next_question()
$ renpy.block_rollback()
scene ep12_cg_derek_ask with dissolve
de "Alright, here's the first question..."
$ cg_tmp_str = cg_get_current_question_string()
de "[cg_tmp_str]"

scene ep12_cg_mc_play_card
call screen cg_mc_cards_screen
with dissolve
$ renpy.pause()
$ renpy.pause()
$ cg_simulate_winner()
$ cg_shuffle_responses()
$ renpy.block_rollback()
scene ep12_cg_read
hide screen cg_ol_screen
with dissolve
de "Thank you. Now, I'll read the question and answers without knowing whose is whose, and the funniest answer to me gets a point."

scene ep12_cg_read1
show screen cg_read_answers_screen
with dissolve
label ep12_cg_derek_read_loop:
$ renpy.block_rollback()
$ cg_tmp_str = cg_get_current_question_string()
de "[cg_tmp_str]"
if cg_read_idx == 0:
    scene ep12_cg_read2
    show screen cg_read_answers_screen1
    with dissolve
elif cg_read_idx == 1:
    scene ep12_cg_read3
    show screen cg_read_answers_screen2
    with dissolve
else:
    scene ep12_cg_read4
    show screen cg_read_answers_screen3
    with dissolve
$ cg_tmp_str =  cg_answers_and_reactions[cg_read_idx][0]
de "[cg_tmp_str]"

if cg_answers_and_reactions[cg_read_idx][1] == "very bad":
    scene ep12_cg_derek_vb_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very bad")
    de "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "bad":
    scene ep12_cg_derek_bad_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "bad")
    de "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "fun":
    scene ep12_cg_derek_fun_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "fun")
    de "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "very fun":
    scene ep12_cg_derek_vf_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very fun")
    de "[cg_tmp_str]"

if cg_read_idx == 0:
    $ cg_read_idx += 1
    scene ep12_cg_read2
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    with dissolve
    jump ep12_cg_derek_read_loop
elif cg_read_idx == 1:
    $ cg_read_idx += 1
    scene ep12_cg_read3
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    show screen cg_read_answers_screen2
    with dissolve
    jump ep12_cg_derek_read_loop

scene ep12_cg_derek_read
show screen cg_ol_screen
with dissolve
$ cg_tmp_str = cg_winning_string
de "The funniest one to me was \"[cg_tmp_str]\". Whose was that?"

$ cg_update_scores()
if cg_current_winner == 1:
    if maya_shiny_dress:
        scene ep12_cg_maya_winb with dissolve
    else:
        scene ep12_cg_maya_win with dissolve
    my "Haha, that one was mine!"
elif cg_current_winner == 2:
    scene ep12_cg_sage_win with dissolve
    sa "Hahaha! I won one!"
else:
    scene ep12_cg_mc_win with dissolve
    mc "That's mine! Haha!"

$ cg_discard_card(cg_mc_selected_card)
$ renpy.block_rollback()
if maya_shiny_dress:
    scene ep12_cg_maya_ask with dissolve
else:
    scene ep12_cg_maya_askb with dissolve
my "It's my turn to read a question."
$ cg_get_next_question()
$ cg_tmp_str = cg_get_current_question_string()
my "[cg_tmp_str]"

scene ep12_cg_mc_play_card
call screen cg_mc_cards_screen
with dissolve
$ renpy.pause()
$ cg_simulate_winner()
$ cg_shuffle_responses()
$ renpy.block_rollback()
scene ep12_cg_read
hide screen cg_ol_screen
with dissolve
my "I wonder who'll win this one."

scene ep12_cg_read1
show screen cg_read_answers_screen
with dissolve
label ep12_cg_maya_read_loop:
$ cg_tmp_str = cg_get_current_question_string()
my "[cg_tmp_str]"

if cg_read_idx == 0:
    scene ep12_cg_read2
    show screen cg_read_answers_screen1
    with dissolve
elif cg_read_idx == 1:
    scene ep12_cg_read3
    show screen cg_read_answers_screen2
    with dissolve
else:
    scene ep12_cg_read4
    show screen cg_read_answers_screen3
    with dissolve
$ cg_tmp_str = cg_answers_and_reactions[cg_read_idx][0]
my "[cg_tmp_str]"

if cg_answers_and_reactions[cg_read_idx][1] == "very bad":
    if maya_shiny_dress:
        scene ep12_cg_maya_vb_reaction
    else:
        scene ep12_cg_maya_vb_reactionb
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very bad")
    my "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "bad":
    if maya_shiny_dress:
        scene ep12_cg_maya_bad_reaction
    else:
        scene ep12_cg_maya_bad_reactionb
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "bad")
    my "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "fun":
    if maya_shiny_dress:
        scene ep12_cg_maya_fun_reaction
    else:
        scene ep12_cg_maya_fun_reactionb
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "fun")
    my "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "very fun":
    if maya_shiny_dress:
        scene ep12_cg_maya_vf_reaction
    else:
        scene ep12_cg_maya_vf_reactionb
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very fun")
    my "[cg_tmp_str]"

if cg_read_idx == 0:
    $ cg_read_idx += 1
    scene ep12_cg_read2
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    with dissolve
    jump ep12_cg_maya_read_loop
elif cg_read_idx == 1:
    $ cg_read_idx += 1
    scene ep12_cg_read3
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    show screen cg_read_answers_screen2
    with dissolve
    jump ep12_cg_maya_read_loop

if maya_shiny_dress:
    scene ep12_cg_maya_read
else:
    scene ep12_cg_maya_readb
show screen cg_ol_screen
with dissolve
$ cg_tmp_str = cg_winning_string
my "I think I liked \"[cg_tmp_str]\" the most."

$ cg_update_scores()
if cg_current_winner == 0:
    scene ep12_cg_derek_win with dissolve
    de "Yes! That's my point."
elif cg_current_winner == 2:
    scene ep12_cg_sage_win with dissolve
    sa "Yay! That was me!"
else:
    scene ep12_cg_mc_win with dissolve
    mc "That was my card."

$ cg_discard_card(cg_mc_selected_card)
$ renpy.block_rollback()
scene ep12_cg_sage_ask with dissolve
sa "My turn!"
$ cg_get_next_question()
$ cg_tmp_str = cg_get_current_question_string()
sa "[cg_tmp_str]"

scene ep12_cg_mc_play_card
call screen cg_mc_cards_screen
with dissolve
$ renpy.pause()
$ cg_simulate_winner()
$ cg_shuffle_responses()
$ renpy.block_rollback()
scene ep12_cg_read
hide screen cg_ol_screen
with dissolve
sa "Here goes..."

scene ep12_cg_read1
show screen cg_read_answers_screen
with dissolve
label ep12_cg_sage_read_loop:
$ cg_tmp_str = cg_get_current_question_string()
sa "[cg_tmp_str]"
if cg_read_idx == 0:
    scene ep12_cg_read2
    show screen cg_read_answers_screen1
    with dissolve
elif cg_read_idx == 1:
    scene ep12_cg_read3
    show screen cg_read_answers_screen2
    with dissolve
else:
    scene ep12_cg_read4
    show screen cg_read_answers_screen3
    with dissolve
$ cg_tmp_str = cg_answers_and_reactions[cg_read_idx][0]
sa "[cg_tmp_str]"

if cg_answers_and_reactions[cg_read_idx][1] == "very bad":
    scene ep12_cg_sage_vb_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very bad")
    sa "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "bad":
    scene ep12_cg_sage_bad_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "bad")
    sa "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "fun":
    scene ep12_cg_sage_fun_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "fun")
    sa "[cg_tmp_str]"
elif cg_answers_and_reactions[cg_read_idx][1] == "very fun":
    scene ep12_cg_sage_vf_reaction
    hide screen cg_read_answers_screen
    hide screen cg_read_answers_screen1
    hide screen cg_read_answers_screen2
    hide screen cg_read_answers_screen3
    with dissolve
    $ cg_tmp_str = cg_get_reaction_string(cg_answers_and_reactions[cg_read_idx][0], "very fun")
    sa "[cg_tmp_str]"

if cg_read_idx == 0:
    $ cg_read_idx += 1
    scene ep12_cg_read2
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    with dissolve
    jump ep12_cg_sage_read_loop
elif cg_read_idx == 1:
    $ cg_read_idx += 1
    scene ep12_cg_read3
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    show screen cg_read_answers_screen2
    with dissolve
    jump ep12_cg_sage_read_loop

scene ep12_cg_sage_read
show screen cg_ol_screen
with dissolve
$ cg_tmp_str = cg_winning_string
sa "\"[cg_tmp_str]\" was the best one!"

$ cg_update_scores()
if cg_current_winner == 0:
    scene ep12_cg_derek_win with dissolve
    de "Mine!"
elif cg_current_winner == 1:
    if maya_shiny_dress:
        scene ep12_cg_maya_winb with dissolve
    else:
        scene ep12_cg_maya_win with dissolve
    my "Haha! That's one point to me!"
else:
    scene ep12_cg_mc_win with dissolve
    mc "Hey, I got one!"

$ cg_discard_card(cg_mc_selected_card)
$ cg_get_next_question()
$ renpy.block_rollback()
scene ep12_cg_mc_ask with dissolve
$ cg_tmp_str = cg_get_current_question_string()
mc "[cg_tmp_str]"

scene ep12_cg_mc_get_cards with dissolve
$ renpy.pause()
$ cg_shuffle_responses()

scene ep12_cg_read1
hide screen cg_ol_screen
show screen cg_read_answers_screen
with dissolve
label ep12_cg_mc_read_loop:
$ cg_tmp_str = cg_get_current_question_string()
mc "[cg_tmp_str]"
if cg_read_idx == 0:
    scene ep12_cg_read2
    show screen cg_read_answers_screen1
    with dissolve
elif cg_read_idx == 1:
    scene ep12_cg_read3
    show screen cg_read_answers_screen2
    with dissolve
else:
    scene ep12_cg_read4
    show screen cg_read_answers_screen3
    with dissolve
$ cg_tmp_str = cg_answers_and_reactions[cg_read_idx][0]
mc "[cg_tmp_str]"
menu:
    "[m_c1]Laugh":
        $ cg_tmp_str = cg_get_reaction_string("","fun")
        scene ep12_cg_mc_laugh
        hide screen cg_read_answers_screen
        hide screen cg_read_answers_screen1
        hide screen cg_read_answers_screen2
        hide screen cg_read_answers_screen3
        with dissolve
        mc "[cg_tmp_str]"
    "Don't laugh":
        $ cg_tmp_str = cg_get_reaction_string("","bad")
        scene ep12_cg_mc_neutral
        hide screen cg_read_answers_screen
        hide screen cg_read_answers_screen1
        hide screen cg_read_answers_screen2
        hide screen cg_read_answers_screen3
        with dissolve
        mc "[cg_tmp_str]"

if cg_read_idx == 0:
    $ cg_read_idx += 1
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    scene ep12_cg_read2 with dissolve
    jump ep12_cg_mc_read_loop
elif cg_read_idx == 1:
    $ cg_read_idx += 1
    show screen cg_read_answers_screen
    show screen cg_read_answers_screen1
    show screen cg_read_answers_screen2
    scene ep12_cg_read3 with dissolve
    jump ep12_cg_mc_read_loop

mc "Haha! The winner is..."
scene ep12_cg_read4
show screen cg_read_answers_screen
show screen cg_read_answers_screen1
show screen cg_read_answers_screen2
show screen cg_read_answers_screen3
call screen cg_mc_pick_winner_screen
with dissolve
$ renpy.pause(0.5)
$ renpy.block_rollback()
scene ep12_cg_mc_choose
hide screen cg_read_answers_screen
hide screen cg_read_answers_screen1
hide screen cg_read_answers_screen2
hide screen cg_read_answers_screen3
show screen cg_ol_screen
with dissolve
$ cg_tmp_str =  cg_winning_string
mc "[cg_tmp_str]"
$ renpy.block_rollback()
$ cg_update_scores()
if cg_current_winner == 0:
    scene ep12_cg_derek_win with dissolve
    de "Haha! That one was mine!"
elif cg_current_winner == 1:
    if maya_shiny_dress:
        scene ep12_cg_maya_winb with dissolve
    else:
        scene ep12_cg_maya_win with dissolve
    my "Oh, yes! Give me that point."
else:
    scene ep12_cg_sage_win with dissolve
    sa "Yes! I'm on fire!"

$ cg_get_next_question()
$ renpy.block_rollback()
scene ep12_cg_derek_ask with dissolve
de "It's me again..."
$ cg_tmp_str = cg_get_current_question_string()
de "[cg_tmp_str]"

scene ep12_cg_mc_play_card
call screen cg_mc_cards_screen
with dissolve
$ renpy.pause()
$ cg_simulate_winner()
$ cg_shuffle_responses()
$ renpy.block_rollback()
scene ep12_cg_read1
hide screen cg_ol_screen
show screen cg_read_answers_screen
with dissolve
jump ep12_cg_derek_read_loop

label cg_game_over_label:
$ renpy.block_rollback()
hide screen cg_ol_screen
if cg_winner == "Derek":
    scene ep12_cg_derek_won2 with dissolve
    de "That was me! And now I have five points! I win!"
    scene ep12_cg_derek_won3 with dissolve
    sa "Congrats, Derek."
    if maya_shiny_dress:
        scene ep12_cg_derek_won4 with dissolve
    else:
        scene ep12_cg_derek_won4b with dissolve
    my "Well deserved!"
    scene ep12_cg_derek_won1 with dissolve
    mc "You were the funniest. Congratulations!"
    scene ep12_cg_derek_won2 with dissolve
    de "Thanks. But I owe it to my funny cards."
elif cg_winner == "Maya":
    if maya_shiny_dress:
        scene ep12_cg_maya_won4 with dissolve
    else:
        scene ep12_cg_maya_won4b with dissolve
    my "Yes! I win! That's five points!"
    scene ep12_cg_mc_won3 with dissolve
    sa "Yay! Go Maya!"
    scene ep12_cg_maya_won2 with dissolve
    de "I never realized you were this funny."
    scene ep12_cg_maya_won1 with dissolve
    mc "Yep, you were the funniest one. Congrats!"
    if maya_shiny_dress:
        scene ep12_cg_maya_won4 with dissolve
    else:
        scene ep12_cg_maya_won4b with dissolve
    my "Haha... Thanks!"
elif cg_winner == "Sage":
    scene ep12_cg_sage_won3 with dissolve
    sa "Yes!!! I win! I win!"
    scene ep12_cg_sage_won2 with dissolve
    de "Is it already over? Wow! You were great!"
    if maya_shiny_dress:
        scene ep12_cg_sage_won4 with dissolve
    else:
        scene ep12_cg_sage_won4b with dissolve
    my "Congratulations, Sage."
    scene ep12_cg_sage_won1 with dissolve
    mc "Haha! You were so funny."
    scene ep12_cg_sage_won3 with dissolve
    sa "Haha! It's the weirdest thing! I didn't even have to cheat this time."
else:
    $ ep12_card_game_won = True
    scene ep12_cg_mc_won1 with dissolve
    mc "Oh! That's me! Does that mean that I win? I have five points."
    if maya_shiny_dress:
        scene ep12_cg_mc_won4 with dissolve
    else:
        scene ep12_cg_mc_won4b with dissolve
    my "Yes! You won! Haha!"
    scene ep12_cg_mc_won2 with dissolve
    de "Congrats, [mc_de]. You were hilarious!"
    scene ep12_cg_mc_won3 with dissolve
    sa "Haha, you all did great!"
    if not persistent.ep12_cardisa13:
        $ persistent.ep12_cardisa13 = True
        $ persistent.rew_isa_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg

scene ep12_cg_over with dissolve
mc "Thanks a lot for the game. It was fun."

if ep12_card_game_won:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("IDS3_45")
        init:
            $ achievement.register("IDS3_45")
        $ achievement.Sync()

$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_jomc_label:
scene ep12_np2_jomc1
show screen dance_filter_screen
with dissolve
$ renpy.pause()
scene ep12_np2_jomc2 with dissolve
js "Smile..."
play sound "sound_effects/camera_shutter.mp3"
"*{i}Click{/i}*"
scene ep12_np2_jomc3 with dissolve
if branchZoey:
    mc "It's hard to smile tonight."
else:
    mc "I haven't got a lot to smile about."
scene ep12_np2_jomc4 with dissolve
js "I get it..."
scene ep12_np2_jomc6 with dissolve
$ renpy.pause()
scene ep12_np2_jomc4 with dissolve
js "It's hard to see you like this."
if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
    js "A part of me wants to hug you, and the other part wants to punch you for what you did..."
    scene ep12_np2_jomc7 with dissolve
    mc "There's no need to punch me. It feels like I'm punching myself daily."
    scene ep12_np2_jomc4 with dissolve
    js "*{i}Sigh{/i}* Well, that's not nice to hear..."
js "I heard you talked to Maya... I don't think I can add anything that she didn't already tell you."
scene ep12_np2_jomc5 with dissolve
if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
    js "I'm disappointed in you, but..."
else:
    js "I'm sad to hear about your breakup, but..."
js "You're strong. You'll survive this."
scene ep12_np2_jomc7 with dissolve
mc "Yeah... Thanks."
if "Bella" in breakup:
    $ new_bio("Josy", "Josy tried to be supportive of me after my breakup with Bella.")
elif "Sage" in breakup:
    $ new_bio("Josy", "Josy tried to be supportive of me after my breakup with Sage.")
elif "Jill" in breakup:
    $ new_bio("Josy", "Josy tried to be supportive of me after my breakup with Jill.")
#$ task_list[8] = ""
$ updateTaskList()
if "ep12_np2_jmd_label" in event_list or "ep12_np2_ji_label" in event_list or "ep12_np2_lily_label" in event_list:
    $ task_list[8]=task_list[8].replace("\nTalk to Josy (Dance floor)","")
    $ task_list[8]=task_list[8].replace("\nTalk to Josy","")
else:
    $ task_list[8] = ""
if "ep12_np2_jmd_label" not in event_list or "ep12_np2_jomc_label" not in event_list or "ep12_np2_lily_label" not in event_list or "ep12_np2_ji_label" not in event_list:
    $ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_lily_label:
scene ep12_np2_lily1 with dissolve
nic "Did you talk to him tonight?"
scene ep12_np2_lily5 with dissolve
ly "Nope..."
ly "I keep looking his way, but he hasn't come up to me."
scene ep12_np2_lily1 with dissolve
nic "What did he tell you when you last spoke?"
scene ep12_np2_lily5 with dissolve
ly "He said he didn't want to help me with my problem because he didn't want to choose for me."
scene ep12_np2_lily2 with dissolve
nic "He didn't try to convince you to stay together?"
scene ep12_np2_lily6 with dissolve
ly "No. He said he wanted it, but also that he'd be ok with it if I wanted to stick to my plan."
scene ep12_np2_lily2 with dissolve
nic "So, he's supportive no matter what you choose?"
scene ep12_np2_lily5 with dissolve
ly "Yes."
scene ep12_np2_lily3 with dissolve
nic "That's...awesome."
scene ep12_np2_lily6 with dissolve
ly "It's not awesome. It would have been better if he had ended it with me."
ly "It would have made everything easier."
scene ep12_np2_lily3 with dissolve
nic "You still have that option."
scene ep12_np2_lily7 with dissolve
ly "..."
scene ep12_np2_lily1 with dissolve
nic "But you don't want it."
scene ep12_np2_lily6 with dissolve
ly "It's the smart decision."
scene ep12_np2_lily1 with dissolve
nic "Sometimes... What's smart isn't necessarily what's best for you."
scene ep12_np2_lily4 with dissolve
nic "When I got pregnant with Marvin, I second-guessed myself daily."
nic "The smart choice would have been not to go through with the pregnancy."
scene ep12_np2_lily3 with dissolve
nic "But in my heart, I knew I wanted a child."
nic "And while that decision led to plenty of grief, there's no way I'd make any other choice if given the choice again."
nic "I'd pick Marvin a million times over."
scene ep12_np2_lily9 with dissolve
nic "My advice to you is: stop listening to what's in here too much..."
scene ep12_np2_lily10 with dissolve
nic "And start listening more to what's in here."
scene ep12_np2_lily8 with dissolve
$ renpy.pause()
#$ task_list[8] = ""
$ updateTaskList()
if "ep12_np2_jmd_label" in event_list or "ep12_np2_ji_label" in event_list or "ep12_np2_jomc_label" in event_list:
    $ task_list[8]=task_list[8].replace("\nFind Lily (Dance floor)","")
    $ task_list[8]=task_list[8].replace("\nFind Lily","")
else:
    $ task_list[8] = ""
if "ep12_np2_jmd_label" not in event_list or "ep12_np2_jomc_label" not in event_list or "ep12_np2_lily_label" not in event_list or "ep12_np2_ji_label" not in event_list:
    $ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_bc_label:
scene ep12_np2_bc1 with dissolve
bc "There you are! I've been looking all over for you."
scene ep12_np2_bc2 with dissolve
mc "Me? What for?"
scene ep12_np2_bc3 with dissolve
bc "To tell you that you're the lucky one. I called dibs on you for tonight."
scene ep12_np2_bc2 with dissolve
mc "Huh?"
scene ep12_np2_bc3 with dissolve
if ep11_becky_lewd == 4:
    bc "I think it's time that we continue our love story with part two of it."
    scene ep12_np2_bc2 with dissolve
    mc "There won't be a part two, Becky. I'd like to retcon part one of that story."
    scene ep12_np2_bc4 with dissolve
    bc "Hahaha! You're hilarious."
    scene ep12_np2_bc2 with dissolve
    mc "It wasn't a joke."
else:
    bc "You need to stop playing hard to get with me, [name]."
    bc "We're going to kiss at midnight. It's written in the stars."
    scene ep12_np2_bc6 with dissolve
    $ renpy.pause()
    scene ep12_np2_bc2 with dissolve
    mc "I don't see it."
    scene ep12_np2_bc4 with dissolve
    bc "Hahaha! You're hilarious."
    scene ep12_np2_bc2 with dissolve
    mc "No, but seriously. I don't see it."
scene ep12_np2_bc5 with dissolve
bc "Shh! You might not know it yet, [name]. But we belong together. We're like ketchup and fries, banana and chicken or-"
scene ep12_np2_bc2 with dissolve
mc "Oil and water?"
scene ep12_np2_bc3 with dissolve
bc "Exactly! We go together."
scene ep12_np2_bc7 with dissolve
mc "No. I go this way, and you go the other way."
scene ep12_np2_bc3 with dissolve
bc "I will have you, you know?"
scene ep12_np2_bc2 with dissolve
mc "Good luck with that."
scene ep12_np2_bc8 with dissolve
bc "And the song and dance continue."
$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_fw_label:
$ guideSuggestedPage = 271
if roadSage and wt_ep9_branch_numbers == 1:
    stop music fadeout 3
    scene ep12_np2_smc29 with dissolve
    mc "I'm ready. Let's go."
    jump ep12_sage_lewd_label
if branchMayaJosy and wt_ep9_branch_numbers > 1 and not wt_ep12_maya_josy_seen:
    jump ep12_np2_mjmc_label
scene ep12_np2_fw1 with dissolve
de "The fireworks are starting soon! Everyone, get ready for the countdown!"

if wt_ep9_branch_numbers > 1:
    "Pick the girls for the midnight kiss/scenes"
    label wt_midnight_page1menu:
    menu:
       "Zoey" if branchZoey and "Zoey" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Zoey")
           $ ep12_midnight_kiss += " Zoey"
           jump wt_midnight_page1menu
       "Jill" if roadJill and "Jill" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Jill")
           $ ep12_midnight_kiss += " Jill"
           jump wt_midnight_page1menu
       "Sage" if roadSage and "Sage" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Sage")
           $ ep12_midnight_kiss += " Sage"
           jump wt_midnight_page1menu
       "Isabella" if roadIsabella and "Isabella" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Isabella")
           $ ep12_midnight_kiss += " Isabella"
           jump wt_midnight_page1menu
       "Maya & Josy" if (roadMayaJosy or roadMaya or roadJosy) and ("Josy & Maya" not in wt_ep12_midnight_kiss):
           if roadMayaJosy:
            $ wt_ep12_midnight_kiss.append("Josy & Maya")
            $ ep12_midnight_kiss += " Josy & Maya"
           if roadMaya:
            $ wt_ep12_midnight_kiss.append("Maya")
            $ ep12_midnight_kiss += " Josy & Maya"
           if roadJosy:
            $ wt_ep12_midnight_kiss.append("Josy")
            $ ep12_midnight_kiss += " Josy & Maya"
           jump wt_midnight_page1menu
       "Quinn" if roadQuinn and "Quinn" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Quinn")
           $ ep12_midnight_kiss += " Quinn"
           jump wt_midnight_page1menu
       "Nicole" if ep12_nicole_path and not ep12_nicole_breakup and "Nicole" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Nicole")
           $ ep12_midnight_kiss += " Nicole"
           jump wt_midnight_page1menu
       "Riona" if (ep12_riona_side == "Riona" or wt_ep11_quinn_riona_question) and ep10_riona_lewd and "Riona" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Riona")
           $ ep12_midnight_kiss += " Riona"
           jump wt_midnight_page1menu
       "Jade" if ep11_jade_lewd and "Jade" not in wt_ep12_midnight_kiss:
           $ wt_ep12_midnight_kiss.append("Jade")
           $ ep12_midnight_kiss += " Jade"
           jump wt_midnight_page1menu
       "Next page":
          jump wt_midnight_page2menu
       "Continue":
          jump wt_ep12_midnight_control_label
    label wt_midnight_page2menu:
        menu:
            "Lily" if ep12_rolling and "Lily" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Lily")
                $ ep12_midnight_kiss += " Lily"
                jump wt_midnight_page2menu
            "Sally" if ep11_sally_kiss and "Sally" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Sally")
                $ ep12_midnight_kiss += " Sally"
                jump wt_midnight_page2menu
            "Camila" if "Camila" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Camila")
                $ ep12_midnight_kiss += " Camila"
                jump wt_midnight_page2menu
            "Nikita" if ep12_nikita and not ep12_mc_slut and "Nikita" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Nikita")
                $ ep12_midnight_kiss += " Nikita"
                jump wt_midnight_page2menu
            "Bianca" if ep12_bianca_lewd and "Bianca" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Bianca")
                $ ep12_midnight_kiss += " Bianca"
                jump wt_midnight_page2menu
            "Elena" if ep11_elena_lewd and "Elena" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Elena")
                $ ep12_midnight_kiss += " Elena"
                jump wt_midnight_page2menu
            "Sarah" if ep11_sarah_lewd and "Sarah" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Sarah")
                $ ep12_midnight_kiss += " Sarah"
                jump wt_midnight_page2menu
            "Melanie" if ep11_mel_lewd and "Melanie" not in wt_ep12_midnight_kiss:
                $ wt_ep12_midnight_kiss.append("Melanie")
                $ ep12_midnight_kiss += " Melanie"
                jump wt_midnight_page2menu
            "Back":
                 jump wt_midnight_page1menu

if branchZoey:
    $ ep12_midnight_kiss = "Zoey"
if roadJill:
    $ ep12_midnight_kiss = "Jill"
if roadSage:
    $ ep12_midnight_kiss = "Sage"
if roadIsabella:
    $ ep12_midnight_kiss = "Isabella"
if roadMayaJosy:
    $ ep12_midnight_kiss = "Josy & Maya"
if roadMaya:
    $ ep12_midnight_kiss = "Maya"
if roadJosy:
    $ ep12_midnight_kiss = "Josy"
if branchAlone:
  if ep12_midnight_kiss == "":
    if roadQuinn:
        $ ep12_midnight_kiss = "Quinn"
        jump ep12_np2_fwb_label
    if ep12_nicole_ditch:
        $ ep12_nicole_breakup = True
    if ep12_nicole_path and not ep12_nicole_breakup:
        scene ep12_np2_fw2 with dissolve
        nic "It's almost midnight, [name]! Time for some lips meeting lips."
        scene ep12_np2_fw3 with dissolve
        if roadQuinn:
            jump ep12_np2_fwc_label
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Ends Nicole path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        menu:
            "Kiss Nicole at midnight":
                $ ep12_midnight_kiss = "Nicole"
                mc "Yes! Let's get a good spot to watch the fireworks together."
                jump ep12_np2_fwb_label
            "Don't kiss Nicole \n{size=-4}[m_c2][mod_choices[0]]":
                label ep12_np2_fwc_label:
                $ ep12_nicole_breakup = True
                mc "I'm not gonna kiss you at midnight."
                scene ep12_np2_fw5 with dissolve
                nic "Are you kidding me?"
                scene ep12_np2_fw4 with dissolve
                mc "I'm sorry, but it's not what I want to do."
                scene ep12_np2_fw5 with dissolve
                nic "Why? Is there someone else you'd rather kiss, or what is it?"
                scene ep12_np2_fw4 with dissolve
                mc "I don't feel like getting into it."
                scene ep12_np2_fw5 with dissolve
                nic "You're unbelievable. And this is how I find out..."
                scene ep12_np2_fw6 with dissolve
    else:
        scene ep12_np2_fw6 with dissolve
        if "sad" in event_list:
            mc "(Let's leave this year behind us...)"
        else:
            mc "(If I want a midnight kiss, I'd better prepare for it.)"

    $ ep12_np_endings = ["Alone","???","???","???","???","With Camila","???","???","???","???"]

    if ep12_riona_side == "Riona" and ep10_riona_lewd:
        $ ep12_np_endings[1] = "With Riona"
    if ep12_rolling:
        $ ep12_np_endings[2] = "With Lily"
    if ep11_sally_kiss:
        $ ep12_np_endings[3] = "With Sally"

    if ep11_jade_lewd:
        $ ep12_np_endings[4] = "With Jade"
    $ ep12_np_endings[5] = "With Camila"
    if ep12_nikita and not ep12_mc_slut:
        $ ep12_np_endings[6] = "With Nikita"

    if ep12_bianca_lewd:
        if branchJill:
            $ ep12_np_endings[7] = "With Bianca"
        else:
            $ ep12_np_endings[7] = "With Bianca"

    if ep11_elena_lewd:
        $ ep12_np_endings[8] = "With Elena and John Boy"
    if ep11_sarah_lewd:
        $ ep12_np_endings[9] = "With Sarah"
    elif ep11_mel_lewd:
        $ ep12_np_endings[9] = "With Melanie"

    menu:
        "How do you end the night?"
        "[ep12_np_endings[0]]":
            $ ep12_midnight_kiss = "Alone"
        "[ep12_np_endings[1]]" if ep12_np_endings[1] != "???":
            $ ep12_midnight_kiss = "Riona"
        "[ep12_np_endings[2]]" if ep12_np_endings[2] != "???":
            $ ep12_midnight_kiss = "Lily"
        "[ep12_np_endings[3]]" if ep12_np_endings[3] != "???":
            $ ep12_midnight_kiss = "Sally"
        "[ep12_np_endings[4]]" if ep12_np_endings[4] != "???":
            $ ep12_midnight_kiss = "Jade"
        "[ep12_np_endings[5]]":
            $ ep12_midnight_kiss = "Camila"
        "[ep12_np_endings[6]]" if ep12_np_endings[6] != "???":
            $ ep12_midnight_kiss = "Nikita"
        "[ep12_np_endings[7]]" if ep12_np_endings[7] != "???":
            $ ep12_midnight_kiss = "Bianca"
        "[ep12_np_endings[8]]" if ep12_np_endings[8] != "???":
            $ ep12_midnight_kiss = "Elena"
        "[ep12_np_endings[9]]" if ep12_np_endings[9] != "???":
            if ep11_sarah_lewd:
                $ ep12_midnight_kiss = "Sarah"
            else:
                $ ep12_midnight_kiss = "Melanie"
if breakup:
    if ep12_midnight_kiss == "":
        $ ep12_np_endings = ["Alone","???","???","???"]
        if ep11_sally_kiss:
            $ ep12_np_endings[1] = "With Sally"
        if ep12_bianca_lewd:
            if branchJill:
                $ ep12_np_endings[2] = "With Bianca"
            else:
                $ ep12_np_endings[2] = "With Bianca"
        if ep12_nikita and not ep12_mc_slut:
            $ ep12_np_endings[3] = "With Nikita"
        menu:
            "How do you end the night?"
            "[ep12_np_endings[0]]":
                $ ep12_midnight_kiss = "Alone"
            "[ep12_np_endings[1]]" if ep12_np_endings[1] != "???":
                $ ep12_midnight_kiss = "Sally"
            "[ep12_np_endings[2]]" if ep12_np_endings[2] != "???":
                $ ep12_midnight_kiss = "Bianca"
            "[ep12_np_endings[3]]" if ep12_np_endings[3] != "???":
                $ ep12_midnight_kiss = "Nikita"
else:
    if ep12_midnight_kiss == "":
        $ ep12_midnight_kiss = "Alone"

label ep12_np2_fwb_label:
if ep12_midnight_kiss == "Jade":
    label ep12_jade_lewd_label:
    if _in_replay:
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_jade == None:
            $ mc_jade = name
        else:
            $ mc_jade = persistent.mc_jade
        if persistent.jade == None:
            $ jade = "Jade"
        else:
            $ jade = persistent.jade
        $ ep12_pp_fireworks = 2
        play music "music/ep12/licensed_music/track204.mp3"
    hide screen new_phone_screen
    scene ep12_np2_fw7 with dissolve
    mc "It's almost midnight."
    scene ep12_np2_fw8 with dissolve
    ja "So it is. What's on your mind?"
    scene ep12_np2_fw9 with dissolve
    mc "That I'm not ready to give up on my adventure with you."
    scene ep12_np2_fw10 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw11 with dissolve
    ja "If that's the case... Meet me in a stall in the women's bathroom."
    scene ep12_np2_fw12 with dissolve
    mc "In there?"
    scene ep12_np2_fw11 with dissolve
    ja "Go there now."
    scene ep12_np2_fw13 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw205 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw206 with dissolve
    play sound "sound_effects/door_knock.mp3"
    "*{i}Door knocking{/i}*"
    ja "It's me."
    scene ep12_np2_fw207 with dissolve
    ja "The coast is clear. Everyone is outside waiting for the fireworks."
    scene ep12_np2_fw208 with dissolve
    mc "It's still five minutes to midnight."
    scene ep12_np2_fw209 with dissolve
    ja "Fuck it, [name]. Happy New Year!"
    scene ep12_np2_fw210 with dissolve
    ja "Mmm!!!"
    scene ep12_np2_fw211 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene anim_jade_kiss_ep12 with dissolve
    ja "*{i}Moans{/i}* Mmm..."
    mc "*{i}Smack{/i}* Fuck. It's so good."
    pause
    scene anim_jade_kiss2_ep12 with dissolve
    pause
    $ tmpInt = 0
    label ep12_jade_lewd_loop_label:
    menu:
        "Blowjob":
            $ tmpInt += 1
            scene anim_jade_bj1_ep12 with dissolve
            ja "*{i}Suck suck glug glug{/i}*"
            pause
            jump ep12_jade_lewd_loop_label
        "Boobjob":
            $ tmpInt += 1
            scene anim_jade_tits1_ep12 with dissolve
            ja "Mmm... Yes, [mc_jade]... I'm not done with you either..."
            ja "I'm so happy you feel the same."
            mc "Fuck... Yes, me too."
            pause
            scene anim_jade_tits2_ep12 with dissolve
            pause
            jump ep12_jade_lewd_loop_label
        "Doggystyle":
            $ tmpInt += 1
            scene anim_jade_doggy1_ep12 with dissolve
            ja "*{i}Moans{/i}* Fuck me, [mc_jade]..."
            pause
            scene anim_jade_doggy2_ep12 with dissolve
            ja "Starting the new year with your cock inside wasn't on my plans for tonight."
            pause
            scene anim_jade_doggy3_ep12 with dissolve
            ja "But I fucking love it. Mmm..."
            pause
            jump ep12_jade_lewd_loop_label
        "Facing":
            $ tmpInt += 1
            scene anim_jade_facing1_ep12 with dissolve
            ja "Yes! Take me... Fuck me."
            ja "Push it all the way in."
            pause
            scene anim_jade_facing2_ep12 with dissolve
            ja "*{i}Moans{/i}* Yes, you know exactly how I want it."
            pause
            jump ep12_jade_lewd_loop_label
        "Cum" if tmpInt > 2:
            mc "[jade], I'm gonna cum any second now..."
            menu:
                "On tits":
                    scene anim_jade_tits2_ep12 with dissolve
                    ja "Cum over my tits, [mc_jade]."
                    mc "Are you sure?"
                    ja "Yes. I want you to unleash yourself over me."
                    pause
                    scene ep12_np2_fw212 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw212 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw212 at vpunch, cum2
                    mc "Hngn... Fuck..."
                    scene ep12_np2_fw213 with dissolve
                    ja "*{i}Smack{/i}* Mmm..."
                    scene ep12_np2_fw214 with dissolve
                "In mouth":
                    scene anim_jade_bj1_ep12 with dissolve
                    ja "*{i}Suck suck glug glug{/i}*"
                    pause
                    scene ep12_np2_fw215 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw215 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw215 at vpunch, cum1
                    mc "Hngn... Fuck..."
                    scene ep12_np2_fw216 with dissolve
                    ja "*{i}Suck suck gulp{/i}*"
                    scene ep12_np2_fw217 with dissolve
                "Creampie":
                    scene anim_jade_facing2_ep12 with dissolve
                    ja "Fill me up, [mc_jade]. Let me feel the warmth of the cum shooting into me."
                    pause
                    scene ep12_np2_fw218 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw218 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep12_np2_fw218 at vpunch, cum1
                    mc "Hngn... Fuck..."
                    scene ep12_np2_fw220 at vpunch, cum1
                    ja "Fuck, I'm cumming! Ahhh..."
                    scene ep12_np2_fw219 with dissolve
                    ja "You filled me up good, [mc_jade]..."
    mc "Happy New Year..."
    $ renpy.end_replay()
    $ persistent.ep12_lewd_jade = True
    $ calcScenes()
    $ mphone_stats_add_girl_s3("jade","You had sex with Jade during the New Year's Eve party in episode 12.")
    $ new_bio("Jade", "During the New Year's Eve party, I ended up having sex with Jade at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I ended up having sex with Jade at midnight.")
    $ wt_ep12_midnight_seen.append("Jade")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
    show screen new_phone_screen
elif ep12_midnight_kiss == "Riona":
    label wt_ep12_midnight_riona_label:
    scene ep12_np2_fw14 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw15 with dissolve
    ri "It's finally midnight... I can get out of here."
    scene ep12_np2_fw16 with dissolve
    mc "Congratulations on making it through the evening."
    scene ep12_np2_fw15 with dissolve
    ri "Thanks. Somehow I survived."
    ri "Why aren't you doing what everyone else is doing?"
    scene ep12_np2_fw16 with dissolve
    mc "What's that?"
    scene ep12_np2_fw17 with dissolve
    ri "Looking for someone to make out with."
    scene ep12_np2_fw16 with dissolve
    mc "Who said I wasn't?"
    scene ep12_np2_fw17 with dissolve
    ri "Haha."
    scene ep12_np2_fw18 with dissolve
    ri "Oh..."
    ri "Me?"
    scene ep12_np2_fw19 with dissolve
    mc "If you want to."
    scene ep12_np2_fw18 with dissolve
    ri "Why do you want to do that?"
    scene ep12_np2_fw19 with dissolve
    mc "I looked back at this semester today, thinking about everything that had happened."
    mc "The dates, the parties, not knowing what I want..."
    scene ep12_np2_fw20 with dissolve
    mc "You popped up in my head a lot."
    mc "I thought about how we met and our date at the arcade."
    scene ep12_np2_fw21 with dissolve
    ri "That was so much fun."
    scene ep12_np2_fw20 with dissolve
    mc "It was. I had the best time with you."
    if ep10_shroom_choice == "DIK":
        mc "I remember how you calmed me down at Thanksgiving."
        scene ep12_np2_fw21 with dissolve
        ri "You were tripping so bad. Haha! You thought you saw dinosaurs."
        scene ep12_np2_fw22 with dissolve
        mc "I did see dinosaurs."
        mc "I remember that, and how we... You know?"
    else:
        mc "I remember our talk on the bench at Thanksgiving and how we...you know?"
    scene ep12_np2_fw21 with dissolve
    ri "It was amazing doing those things with you."
    ri "It all feels so long ago... Like from a time when everything was different."
    scene ep12_np2_fw20 with dissolve
    mc "I want to feel like that again."
    if ep10_shroom_choice == "DIK":
        scene ep12_np2_fw23 with dissolve
        ri "High on shrooms?"
        scene ep12_np2_fw22 with dissolve
        mc "Everything but that."
    scene ep12_np2_fw24 with dissolve
    mc "And I want you to feel like you did back then, too."
    mc "Even though I know it's going to be hard for you."
    scene ep12_np2_fw25 with dissolve
    ri "I won't kiss you if it's out of pity, [name]."
    scene ep12_np2_fw24 with dissolve
    mc "It's not pity. It's something more than that."
    mc "I think you need someone like me in your life."
    mc "And I think I need someone like you in mine."
    scene ep12_np2_fw25 with dissolve
    ri "You got that from one date and sex on a park bench?"
    scene ep12_np2_fw24 with dissolve
    mc "You know it's more than those times, right?"
    scene ep12_np2_fw26 with dissolve
    ri "I'll kiss you at midnight."
    ri "But I don't think I'm in a good state of mind to date you, if that's what you're trying to tell me."
    scene ep12_np2_fw24 with dissolve
    mc "No pressure, Rio. None at all."
    mc "If there's magic, there's magic. And if there's none, so be it."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw27 with dissolve
    ri "Don't push your lips too hard against mine. I'm worried it will hurt my nose."
    scene ep12_np2_fw29 with dissolve
    mc "This will be the softest kiss you have ever experienced."
    scene ep12_np2_fw28 with dissolve
    ri "Is that right?"
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_rio_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw30 with dissolve
    mc "Did it hurt?"
    scene ep12_np2_fw31 with dissolve
    ri "You were right. The softest one ever."
    scene ep12_np2_fw30 with dissolve
    mc "Happy New Year, Rio."
    scene ep12_np2_fw31 with dissolve
    ri "It's not happy yet, but it's off to a good start."
    scene ep12_np2_fw29 with dissolve
    mc "For me too."
    $ new_bio("Riona", "During the New Year's Eve party, I kissed Riona at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Riona at midnight.")
    $ wt_ep12_midnight_seen.append("Riona")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Quinn":
    label wt_ep12_midnight_quinn_label:
    scene ep12_np2_fw32 with dissolve
    qu "Don't even look this way, [name]. Off you go."
    scene ep12_np2_fw32b with dissolve
    mc "What are you doing over there?"
    scene ep12_np2_fw33 with dissolve
    mc "Come over to my side of the party. I wanna show you something."
    scene ep12_np2_fw32 with dissolve
    qu "I won't fall for your dirty tricks."
    scene ep12_np2_fw34 with dissolve
    qu "Foul play, [name]."
    scene ep12_np2_fw35 with dissolve
    mc "That's how we do it, isn't it?"
    mc "Don't be stubborn. Come watch the fireworks together with me."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw40 with hpunch
    mc "Hngn... Hey."
    scene ep12_np2_fw41 with dissolve
    qu "Not what you expected for midnight, was it?"
    play sound "sound_effects/shove.mp3"
    scene ep12_np2_fw37 with vpunch
    qu "Whoa!"
    scene ep12_np2_fw36 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    scene ep12_np2_fw38 with dissolve
    qu "Alright. Fuck it..."
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_quinn_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw39 with dissolve
    mc "Happy New Year."
    scene ep12_np2_fw38 with dissolve
    qu "Yeah, yeah. You too."
    qu "You've had your fun. Let me down."
    $ new_bio("Quinn", "During the New Year's Eve party, I kissed Quinn at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Quinn at midnight.")
    $ wt_ep12_midnight_seen.append("Quinn")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Nicole":
    label wt_ep12_midnight_nicole_label:
    scene ep12_np2_fw186 with dissolve
    nic "Up front spots? Who did you pay to get these?"
    scene ep12_np2_fw187 with dissolve
    mc "It's chilly over here, and there's always a risk that the fireworks will hit someone. We're the first line of defense, you and I."
    scene ep12_np2_fw188 with dissolve
    nic "Haha! And here I thought you wanted to be romantic."
    scene ep12_np2_fw189 with dissolve
    mc "Oh, I do. Because the view is also the best."
    mc "You get to feel the pulse of the explosions-"
    scene ep12_np2_fw190 with dissolve
    nic "While they're almost hitting your face?"
    scene ep12_np2_fw189 with dissolve
    mc "Haha! Yes!"
    mc "But you'll be happy to know we won't light the fireworks from up here. It's all happening down there."
    scene ep12_np2_fw191 with dissolve
    nic "Aw, those poor guys have to celebrate down there alone?"
    scene ep12_np2_fw189 with dissolve
    mc "They have each other. As do we."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw192 with dissolve
    "SEVEN!"
    nic "Oh! Is it the countdown already?"
    scene ep12_np2_fw193 with dissolve
    "SIX! FIVE! FOUR!"
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_nicole_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw194 with dissolve
    mc "Happy New Year!"
    scene ep12_np2_fw195 with dissolve
    nic "Happy New Year, [name]. And thank you for the last."
    $ new_bio("Envy", "During the New Year's Eve party, I kissed Nicole at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Nicole at midnight.")
    $ wt_ep12_midnight_seen.append("Nicole")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Lily":
    label wt_ep12_midnight_lily_label:
    scene ep12_np2_fw171 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw174 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw172 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw173 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw159 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw160 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw161 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw162 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_lily_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw163 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw164 with dissolve
    mc "Happy New Year, Lily. I hope this year becomes everything you want it to be."
    scene ep12_np2_fw165 with dissolve
    ly "*{i}Smack{/i}*"
    scene ep12_np2_fw166 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw167 with dissolve
    ly "Happy New Year, [name]. I know I'm not the easiest one to deal with right now..."
    ly "I wish it were easier to be decisive, but it's not. I'm at a crossroads, walking down one path only to run back and stare at the signs again."
    scene ep12_np2_fw168 with dissolve
    mc "You don't have to explain yourself to me. Do what you need to do."
    mc "But know that I will too... I don't know what this new year will hold, but I'm not gonna dwell on us."
    scene ep12_np2_fw169 with dissolve
    mc "That was the kind of person I was last year, but not anymore. Never again."
    mc "That's wasting time on not being happy. And that's what I want to be, and what I wish for you too."
    scene ep12_np2_fw166 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw170 with dissolve
    $ renpy.pause()
    $ new_bio("Lily", "During the New Year's Eve party, I spent midnight next to Lily.")
    $ new_bio("You", "During the New Year's Eve party, I spent midnight next to Lily.")
    $ wt_ep12_midnight_seen.append("Lily")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Nikita":
    label wt_ep12_midnight_nikita_label:
    scene ep12_np2_fw185 with dissolve
    "Three, two, one! HAPPY NEW YEAR!!!"
    scene ep12_np2_fw42 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw43 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw44 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw45 with dissolve
    mc "(Fuck it...)"
    scene ep12_np2_fw46 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw47 with dissolve
    mc "How's this for living in the moment?"
    scene ep12_np2_fw48 with dissolve
    $ renpy.pause()
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_nikita_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw48 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw47 with dissolve
    mc "Happy New Year, Nikita."
    scene ep12_np2_fw49 with dissolve
    nik "Happy New Year, [name]."
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene ep12_np2_fw49b with dissolve
    $ renpy.pause()
    scene ep12_np2_fw49c with dissolve
    nik "*{i}Smack{/i}*"

    scene ep12_np2_fw50 with dissolve
    $ renpy.pause()
    $ new_bio("You", "During the New Year's Eve party, I kissed Nikita at midnight.")
    $ new_bio("Nikita", "During the New Year's Eve party, I kissed Nikita at midnight.")
    $ wt_ep12_midnight_seen.append("Nikita")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Zoey":
    label wt_ep12_midnight_zoey_label:
    scene ep12_np2_fw175 with dissolve
    zo "I feel this year went by in a flash. How about you?"
    scene ep12_np2_fw176 with dissolve
    mc "The good parts of it sure did, but there were times before college when I felt like time stood still."
    mc "But I bet now that you're here with me again, next year will be over in the blink of an eye."
    scene ep12_np2_fw175 with dissolve
    zo "I don't like the sound of that. How do we stop that from happening?"
    zo "I mean, when we were kids, time stood still. Was it because school was boring?"
    scene ep12_np2_fw176 with dissolve
    mc "I don't know, but time always moves fast when you're having fun. Like most of tonight."
    mc "I think we need to get better at enjoying ourselves in the moment."
    scene ep12_np2_fw177 with dissolve
    zo "Are you ending the year on a philosophical note?"
    scene ep12_np2_fw178 with dissolve
    mc "It makes sense, doesn't it?"
    scene ep12_np2_fw179 with dissolve
    zo "I want to enjoy the moments together with you."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw180 with dissolve
    mc "Any final words?"
    scene ep12_np2_fw181 with dissolve
    zo "Final words? Are you about to push me over the railing or what?"
    scene ep12_np2_fw180 with dissolve
    mc "Not like that... I meant, the year's almost over. Any final words for it?"
    scene ep12_np2_fw182 with dissolve
    zo "I'm sorry for everything."
    scene ep12_np2_fw180 with dissolve
    mc "Let's leave the sorries in this year."
    scene ep12_np2_fw183 with dissolve
    zo "Yeah. I know the words I'll start the next year with."
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    scene ep12_np2_fw183 with dissolve
    zo "I love you, [name]."
    scene ep12_np2_fw184 with dissolve
    mc "Yeah, you do. And I do too."
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_zoey_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    $ new_bio("Zoey", "During the New Year's Eve party, I kissed Zoey at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Zoey at midnight.")
    $ wt_ep12_midnight_seen.append("Zoey")
    if wt_ep9_branch_numbers > 1:
        jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Sally":
    label wt_ep12_midnight_sally_label:
    scene ep12_np2_fw51 with dissolve
    mc "Sally? Are you still available for midnight?"
    if "sally_break" in event_list:
        scene ep12_np2_fw52 with dissolve
        sy "What about your girlfriend?"
        scene ep12_np2_fw53 with dissolve
        mc "My relationship is over."
        scene ep12_np2_fw52 with dissolve
        sy "It happened tonight?"
        scene ep12_np2_fw53 with dissolve
        mc "Yeah. I don't feel like talking about it."
        scene ep12_np2_fw54 with dissolve
        sy "I don't know how I feel about doing that with you now."
        sy "You didn't break up because of me, right?"
        scene ep12_np2_fw53 with dissolve
        mc "Nah, it's more to it than that. It wasn't a happy relationship."
        scene ep12_np2_fw55 with dissolve
        mc "I'm looking to have some fun tonight to get it off my mind. Are you up for it?"
        scene ep12_np2_fw54 with dissolve
        sy "Yes. But I'm not gonna kiss you at midnight."
        scene ep12_np2_fw55 with dissolve
        mc "Are you not?"
        scene ep12_np2_fw56 with dissolve
        sy "No. But you're coming home with me after."
        scene ep12_np2_fw57 with dissolve
        mc "I can work with that."
        scene ep12_np2_fw65 with dissolve
        $ renpy.pause()
        scene ep12_np2_fw185 with dissolve
        "THREE! TWO! ONE!"
        "HAPPY NEW YEAR!!!"
        $ renpy.sound.play("sound_effects/season3/fireworks_mc.mp3",channel="dj1", loop=False)
        scene bg anim_fireworks_mc_ep12 movie with dissolve
        pause 9.33
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
        scene bg anim_fireworks_lots_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks < 2:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
            scene bg anim_fireworks_lots2_ep12 movie with dissolve
            pause 10.66
            if ep12_pp_fireworks == 0:
                $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
                scene bg anim_fireworks_lots3_ep12 movie with dissolve
                pause 11.33
        scene ep12_np2_fw66 with dissolve
        sy "Happy New Year, [name]."
        scene ep12_np2_fw67 with dissolve
        mc "Happy New Year, Sally."
        $ new_bio("Sally", "During the New Year's Eve party, I spent midnight next to Sally.")
        $ new_bio("You", "During the New Year's Eve party, I spent midnight next to Sally.")
    else:
        scene ep12_np2_fw58 with dissolve
        sy "You're playing it too cool, [name]. I thought you weren't going to ask."
        scene ep12_np2_fw59 with dissolve
        mc "Did you make other plans?"
        scene ep12_np2_fw58 with dissolve
        sy "Would that bother you?"
        scene ep12_np2_fw59 with dissolve
        mc "Yes. Forget about your plans. I'm kissing you at midnight."
        scene ep12_np2_fw60 with dissolve
        sy "On one condition."
        scene ep12_np2_fw59 with dissolve
        mc "Name it."
        scene ep12_np2_fw60 with dissolve
        sy "You're coming home with me after."
        scene ep12_np2_fw59 with dissolve
        mc "That's not a condition I'd oppose."
        scene ep12_np2_fw61 with dissolve
        sy "Let's go."
        scene ep12_np2_fw185 with dissolve
        "TEN! NINE! EIGHT!"
        scene ep12_np2_fw62 with dissolve
        sy "Don't use too much tongue."
        scene ep12_np2_fw63 with dissolve
        mc "I know how to kiss."
        scene ep12_np2_fw185 with dissolve
        "THREE! TWO! ONE!"
        "HAPPY NEW YEAR!!!"
        $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
        scene bg anim_sally_kiss_ep12 movie with dissolve
        pause 10.58
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
        scene bg anim_fireworks_lots_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks < 2:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
            scene bg anim_fireworks_lots2_ep12 movie with dissolve
            pause 10.66
            if ep12_pp_fireworks == 0:
                $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
                scene bg anim_fireworks_lots3_ep12 movie with dissolve
                pause 11.33
        scene ep12_np2_fw62 with dissolve
        sy "That was an adequate amount of tongue. You pass."
        scene ep12_np2_fw63 with dissolve
        mc "You pass too."
        scene ep12_np2_fw64 with dissolve
        sy "Pff! Happy New Year, [name]."
        sy "Don't forget the second part of the deal."
        $ new_bio("Sally", "During the New Year's Eve party, I kissed Sally at midnight.")
        $ new_bio("You", "During the New Year's Eve party, I kissed Sally at midnight.")
        $ wt_ep12_midnight_seen.append("Sally")
        if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Sarah":
    label wt_ep12_midnight_sarah_label:
    scene ep12_np2_fw68 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw69 with dissolve
    sar "It's cold out here..."
    scene ep12_np2_fw70 with dissolve
    mc "I'd offer you my shirt, but then I'd show more skin than you."
    scene ep12_np2_fw71 with dissolve
    sar "The new year is coming for us, [name]."
    scene ep12_np2_fw72 with dissolve
    mc "Out with the old... In with the new..."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw71 with dissolve
    sar "No one to make out with?"
    scene ep12_np2_fw72 with dissolve
    mc "By choice."
    scene ep12_np2_fw71 with dissolve
    sar "Sure. Choice."
    scene ep12_np2_fw72 with dissolve
    mc "You?"
    scene ep12_np2_fw73 with dissolve
    sar "We can call it a choice, too."
    scene ep12_np2_fw74 with dissolve
    mc "Let's...?"
    scene ep12_np2_fw75 with dissolve
    sar "Let's show them how to do it, papi."
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_sarah_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw77 with dissolve
    sar "Happy New Year, [name]."
    scene ep12_np2_fw76 with dissolve
    mc "You too, Sarah."
    $ new_bio("Sarah", "During the New Year's Eve party, I kissed Sarah at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Sarah at midnight.")
    $ wt_ep12_midnight_seen.append("Sarah")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Melanie":
    label wt_ep12_midnight_melanie_label:
    scene ep12_np2_fw203 with dissolve
    mc "Mel. How does you, me, and a kiss at midnight sound?"
    scene ep12_np2_fw204 with dissolve
    ml "Will it ruin my makeup?"
    scene ep12_np2_fw203 with dissolve
    mc "No, I'll limit the amount of tongue by 50%%."
    scene ep12_np2_fw204 with dissolve
    ml "Sold. But isn't it like midnight right now?"
    scene ep12_np2_fw203 with dissolve
    if ep12_pp_fireworks < 2:
        mc "It is. We need to hurry. I wanna watch the fireworks we paid for."
    else:
        mc "It is. We need to hurry. I wanna watch the fireworks I didn't pay shit for."

    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw197 with dissolve
    mc "Looks like we made it just in time."
    scene ep12_np2_fw196 with dissolve
    ml "It seems like this means a lot to you. It's just another year, [name]."
    scene ep12_np2_fw197 with dissolve
    mc "I want to get the bad aftertaste from this one out of my mouth."
    mc "And I'll be able to do that with your help."
    scene ep12_np2_fw198 with dissolve
    ml "I don't know if that's sweet or if I should be worried your kiss will taste funny."

    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_mel_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw199 with dissolve
    ml "That was a good kiss. It tasted well, and there was an adequate amount of tongue."
    scene ep12_np2_fw201 with dissolve
    mc "And your makeup still looks perfect. Up close, you're even prettier. Did you know that?"
    scene ep12_np2_fw199 with dissolve
    ml "Haha, alright. You had your kiss. No need to convince me further."
    scene ep12_np2_fw201 with dissolve
    mc "Happy New Year, Melanie. I hope there will be more kisses for us this year."
    scene ep12_np2_fw200 with dissolve
    ml "From each other or?"
    scene ep12_np2_fw202 with dissolve
    mc "Yeah, why not?"
    scene ep12_np2_fw199 with dissolve
    ml "You're drunk. But Happy New Year to you too."
    $ new_bio("Melanie", "During the New Year's Eve party, I kissed Melanie at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Melanie at midnight.")
    $ wt_ep12_midnight_seen.append("Melanie")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Bianca":
    label wt_ep12_midnight_bianca_label:
    scene ep12_np2_fw78 with dissolve
    bia "Hey..."
    scene ep12_np2_fw79 with dissolve
    mc "So it's midnight, huh?"
    scene ep12_np2_fw78 with dissolve
    bia "Yeah... I'm not going to stand here for long."
    bia "I'm not saying I don't want to. I'm saying \"I can't\"..."
    scene ep12_np2_fw80 with dissolve
    mc "Celebrate midnight together? I know. I wasn't even expecting it."
    mc "And honestly, I think I need the space and time to spend it by myself."
    scene ep12_np2_fw81 with dissolve
    bia "Talk tomorrow?"
    scene ep12_np2_fw80 with dissolve
    mc "I have a feeling we'll talk a lot next year."
    if "Jill" in breakup and not ep4_toldDerekAboutJade:
        scene ep12_np2_fw81 with dissolve
        bia "I heard the news."
        scene ep12_np2_fw82 with dissolve
        mc "You did?"
        scene ep12_np2_fw81 with dissolve
        bia "Yep."
        scene ep12_np2_fw80 with dissolve
        mc "And?"
        scene ep12_np2_fw81 with dissolve
        bia "She was inconsolable. And I know I'm to blame for that."
        scene ep12_np2_fw82 with dissolve
        mc "It wasn't just you. It would have ended anyway. I made the right call."
        scene ep12_np2_fw81 with dissolve
        bia "Yeah, maybe you did."
        scene ep12_np2_fw82 with dissolve
        mc "So... Where does that leave us?"
        scene ep12_np2_fw83 with dissolve
        $ renpy.pause()
        scene ep12_np2_fw80 with dissolve
        mc "It's ok. You don't need to answer me now."
    scene ep12_np2_fw84 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_mc.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_mc_ep12 movie with dissolve
    pause 9.33
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    $ new_bio("Bianca", "During the New Year's Eve party, I spent a moment with Bianca near midnight.")
    $ new_bio("You", "During the New Year's Eve party, I spent a moment with Bianca near midnight.")
    $ wt_ep12_midnight_seen.append("Bianca")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Camila":
    label wt_ep12_midnight_camila_label:
    scene ep12_np2_fw85 with dissolve
    mc "Cammy. I have no one to kiss at midnight. Will you do me the honor?"
    scene ep12_np2_fw86 with dissolve
    cam "Maybe if you ask me without sounding so sad about it."
    scene ep12_np2_fw85 with dissolve
    mc "Hey, you. Kiss me at midnight."
    scene ep12_np2_fw87 with dissolve
    cam "A midnight kiss is usually something romantic."
    scene ep12_np2_fw88 with dissolve
    mc "It doesn't have to be romantic."
    scene ep12_np2_fw87 with dissolve
    cam "What I'm saying is that a midnight kiss implies there's romance between the couple kissing."
    scene ep12_np2_fw88 with dissolve
    mc "We have chemistry, you and I. I'll show you."
    scene ep12_np2_fw89 with dissolve
    cam "But I'm not looking for chemistry. I'm looking for fun."
    scene ep12_np2_fw88 with dissolve
    mc "Well, you're in luck. So, am I."
    scene ep12_np2_fw87 with dissolve
    cam "But you just said you'd show me chemistry. Which is it?"
    scene ep12_np2_fw90 with dissolve
    mc "What do I know? I'm doing everything I can right now to get lucky with you."
    scene ep12_np2_fw91 with dissolve
    cam "HAHA! Now that was fun! I'm sold."
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_camila_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw92 with dissolve
    cam "Happy New Year, [name]!"
    scene ep12_np2_fw93 with dissolve
    mc "Happy New Year, Cammy."
    $ new_bio("Camila", "During the New Year's Eve party, I kissed Camila at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Camila at midnight.")
    $ wt_ep12_midnight_seen.append("Camila")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Isabella":
    label wt_ep12_isabella_label:
    scene ep12_np2_fw94 with dissolve
    mc "It's almost midnight."
    scene ep12_np2_fw95 with dissolve
    isa "Corked up the forbidden juice, did you?"
    scene ep12_np2_fw94 with dissolve
    mc "One is for you."
    scene ep12_np2_fw96 with dissolve
    isa "We shouldn't be seen drinking together."
    scene ep12_np2_fw97 with dissolve
    mc "I happen to have the keys to the facility."
    scene ep12_np2_fw96 with dissolve
    isa "So do I. Where are you going with this?"
    scene ep12_np2_fw97 with dissolve
    mc "I saw a balcony that no one will use."
    mc "How about we sneak off to it?"
    scene ep12_np2_fw96 with dissolve
    isa "Where is it?"
    scene ep12_np2_fw98 with dissolve
    mc "You can reach it from the dance floor."
    scene ep12_np2_fw99 with dissolve
    isa "I know the one. Head there now, and I'll meet you there in a few."
    scene ep12_np2_fw98 with dissolve
    mc "Don't take too long. It's almost midnight."
    scene ep12_np2_fw100 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw101 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw106 with dissolve
    isa "Is the coast clear?"
    scene ep12_np2_fw107 with dissolve
    mc "Yes."
    scene ep12_np2_fw108 with dissolve
    mc "Tell me... What are you most excited about with the upcoming year, and why is it our relationship?"
    scene ep12_np2_fw109 with dissolve
    isa "Haha..."
    isa "It is us because of many reasons."
    scene ep12_np2_fw108 with dissolve
    mc "Name one."
    scene ep12_np2_fw109 with dissolve
    isa "Because of how you make me feel. Because of how annoying you can be."
    scene ep12_np2_fw110 with dissolve
    mc "Is that a good reason?"
    scene ep12_np2_fw111 with dissolve
    isa "It's a weirdly amusing reason. I've come to like your quirks, and I want to see how you manage to both please and annoy me next year."
    scene ep12_np2_fw112 with dissolve
    mc "Good answer."
    scene ep12_np2_fw111 with dissolve
    isa "And what are your reasons?"
    scene ep12_np2_fw110 with dissolve
    mc "Bold of you to assume it's our relationship I'm most excited about."
    scene ep12_np2_fw113 with dissolve
    isa "See! There's that annoying part again."
    scene ep12_np2_fw114 with dissolve
    mc "You said you liked it."
    scene ep12_np2_fw115 with dissolve
    isa "*{i}Sigh{/i}*"
    scene ep12_np2_fw102 with dissolve
    mc "It is us. And why?"
    mc "Because I haven't felt this way before."
    mc "I haven't cared about anyone in the way that I care for you."
    mc "And I love how it feels when we're together. I want to continue and see where it takes us."
    scene ep12_np2_fw105 with dissolve
    "*{i}Distant cheering{/i}* Happy New Year!"
    scene ep12_np2_fw102 with dissolve
    mc "Happy New Year, Bella."
    scene ep12_np2_fw103 with dissolve
    isa "Happy New Year, [name]."
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_bella_ny_kiss_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw102 with dissolve
    mc "Did I tell you how beautiful you look tonight?"
    scene ep12_np2_fw103 with dissolve
    isa "You did. But that was last year."
    scene ep12_np2_fw104 with dissolve
    mc "Oh my God, was that a joke? It sounded like a dad joke."
    scene ep12_np2_fw103 with dissolve
    isa "It was funny."
    scene ep12_np2_fw104 with dissolve
    mc "Yeah, if you're a dad."
    scene ep12_np2_fw116 with dissolve
    isa "*{i}Sigh{/i}* I should get back to chaperoning..."
    scene ep12_np2_fw117 with dissolve
    mc "Do you have to?"
    scene ep12_np2_fw116 with dissolve
    isa "Yeah..."
    scene ep12_np2_fw117 with dissolve
    mc "Because I haven't had sex all year."
    scene ep12_np2_fw119 with dissolve
    isa "HAHA! Oh my God! That one was even worse than mine!"
    scene ep12_np2_fw118 with dissolve
    mc "See what I mean? Those jokes stink."
    scene ep12_np2_fw116 with dissolve
    isa "There might be a way for us to sneak off later..."
    isa "I have to check a few things, and then I'll let you know."
    isa "Sound good?"
    scene ep12_np2_fw117 with dissolve
    mc "I'll wait for you as long as I have to."
    scene ep12_np2_fw120 with dissolve
    isa "*{i}Smack{/i}*"
    $ new_bio("Isabella", "During the New Year's Eve party, I kissed Bella at midnight.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Bella at midnight.")
    $ wt_ep12_midnight_seen.append("Isabella")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Josy" or ep12_midnight_kiss == "Maya" or ep12_midnight_kiss == "Josy & Maya":
    label wt_ep12_mayajosy_label:
    if branchMayaJosy:
        scene ep12_np2_fw127 with dissolve
        $ renpy.pause()
        scene ep12_np2_fw128 with dissolve
        $ renpy.pause()
    else:
        scene ep12_np2_fw127b with dissolve
        $ renpy.pause()
        scene ep12_np2_fw128b with dissolve
        $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_mc.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_mc_ep12 movie with dissolve
    pause 9.33
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33

    if branchMayaJosy:
        if roadJosy:
            scene ep12_np2_fw221 with dissolve
            js "I hate seeing you like this..."
            scene ep12_np2_fw222 with dissolve
            mc "It's not fair, Josy. It's not fair."
            scene ep12_np2_fw223 with dissolve
            $ renpy.pause()
            $ new_bio("Josy", "During the New Year's Eve party, I ended the night together with Josy.")
            $ new_bio("You", "During the New Year's Eve party, I ended the night together with Josy.")
        elif roadMaya:
            if maya_shiny_dress:
                scene ep12_np2_fw229 with dissolve
            else:
                scene ep12_np2_fw229b with dissolve
            my "[name]... I can't watch you stand here alone."
            if maya_shiny_dress:
                scene ep12_np2_fw230 with dissolve
            else:
                scene ep12_np2_fw230b with dissolve
            mc "It's not fair, Maya. It's not fair."
            if maya_shiny_dress:
                scene ep12_np2_fw231 with dissolve
            else:
                scene ep12_np2_fw231b with dissolve
            my "I know. Shh... I know."
            $ new_bio("You", "During the New Year's Eve party, I ended the night together with Maya.")
            $ new_bio("Maya", "During the New Year's Eve party, I ended the night together with Maya.")
        else:
            if maya_shiny_dress:
                scene ep12_np2_fw238 with dissolve
            else:
                scene ep12_np2_fw238b with dissolve
            my "[name]... We can't watch you stand here alone."
            if maya_shiny_dress:
                scene ep12_np2_fw239 with dissolve
            else:
                scene ep12_np2_fw239b with dissolve
            mc "It's not fair. It's not fair..."
            $ new_bio("You", "During the New Year's Eve party, I ended the night together with Josy & Maya.")
            $ new_bio("Josy", "During the New Year's Eve party, I ended the night together with Josy & Maya.")
            $ new_bio("Maya", "During the New Year's Eve party, I ended the night together with Josy & Maya.")
    else:
        if roadJosy:
            scene ep12_np2_fw224 with dissolve
            js "Hey..."
            scene ep12_np2_fw225 with dissolve
            mc "You're back. Why aren't you with Maya?"
            scene ep12_np2_fw224 with dissolve
            js "She just left; she wanted to be alone. Can I stand here with you for a while?"
            scene ep12_np2_fw225 with dissolve
            mc "Of course."
            play sound "sound_effects/season3/firework_sage.mp3"
            scene ep12_np2_fw226 with dissolve
            $ renpy.pause()
            scene ep12_np2_fw227 with dissolve
            js "It's always been you to me too, [name]..."
            js "The crush never went away."
            scene ep12_np2_fw228 with dissolve
            mc "Will it be too hard for us to start a relationship like this?"
            scene ep12_np2_fw227 with dissolve
            js "One thing I know for sure - and I rarely know things for sure..."
            js "If I didn't give us a shot, I'd regret it all my life."
            play sound "sound_effects/season3/firework_sage.mp3"
            scene ep12_np2_fw226 with dissolve
            $ renpy.pause()
            $ new_bio("You", "During the New Year's Eve party, I ended the night together with Josy.")
            $ new_bio("Josy", "During the New Year's Eve party, I ended the night together with Josy.")
        elif roadMaya:
            scene ep12_np2_fw232 with dissolve
            mc "Hey... Why aren't you with Josy?"
            scene ep12_np2_fw233 with dissolve
            my "She insisted that I should be with you."
            scene ep12_np2_fw234 with dissolve
            mc "Ever since the day we first met, I knew you were special."
            mc "I can't believe I was right all this time about us."
            mc "So much time wasted on not being together..."
            scene ep12_np2_fw235 with dissolve
            my "..."
            scene ep12_np2_fw234 with dissolve
            mc "I'll let you be alone though. For as long as you need it."
            scene ep12_np2_fw236 with dissolve
            my "Can we be alone together?"
            scene ep12_np2_fw234 with dissolve
            mc "How would that even work?"
            scene ep12_np2_fw236 with dissolve
            my "I think we'll figure it out."
            scene ep12_np2_fw237 with dissolve
            $ renpy.pause()
            $ new_bio("You", "During the New Year's Eve party, I ended the night together with Maya.")
            $ new_bio("Maya", "During the New Year's Eve party, I ended the night together with Maya.")
    $ wt_ep12_midnight_seen.append("MayaJosy")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Jill":
    label wt_ep12_midnight_jill_label:
    scene ep12_np2_fw145 with dissolve
    ji "It's already midnight. I lost track of time."
    scene ep12_np2_fw146 with dissolve
    mc "Yeah, I did too."
    scene ep12_np2_fw147 with dissolve
    ji "Will there be a lot of fireworks?"
    scene ep12_np2_fw148 with dissolve
    mc "I don't care about the fireworks as long as I get to kiss you when the clock strikes twelve."
    scene ep12_np2_fw149 with dissolve
    ji "I've never kissed someone at midnight before..."
    scene ep12_np2_fw150 with dissolve
    mc "Neither have I."
    scene ep12_np2_fw149 with dissolve
    ji "It feels romantic. Like it's something you do with someone special."
    scene ep12_np2_fw185 with dissolve
    "TEN! NINE! EIGHT!"
    scene ep12_np2_fw151 with dissolve
    ji "I can't believe how lucky I am."
    scene ep12_np2_fw152 with dissolve
    mc "Then you know how I feel."
    mc "I get to end the year with the woman of my dreams."
    scene ep12_np2_fw153 with dissolve
    $ renpy.pause()
    if check_jilove():
        $ ep12_jill_love = True
        scene ep12_np2_fw154 with dissolve
        ji "[name]... I think I..."
        scene ep12_np2_fw155 with dissolve
        mc "I love you."
        scene ep12_np2_fw156 with dissolve
        ji "I love you more."
        scene ep12_np2_fw155 with dissolve
        mc "I don't think that's possible."
    else:
        scene ep12_np2_fw155 with dissolve
        mc "I love you."
        scene ep12_np2_fw156 with dissolve
        ji "Oh... That's so sweet."
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_jill_ep12 movie with dissolve
    pause 10.58
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    scene ep12_np2_fw157 with dissolve
    mc "Happy New Year."
    scene ep12_np2_fw158 with dissolve
    ji "Happy New Year, love."
    if ep12_jill_love:
        $ new_bio("Jill", "During the New Year's Eve party, I kissed Jill at midnight. I told her that I loved her, and she reciprocated.")
    else:
        $ new_bio("Jill", "During the New Year's Eve party, I kissed Jill at midnight. I told her that I loved her, but she didn't reciprocate.")
    $ new_bio("You", "During the New Year's Eve party, I kissed Jill at midnight.")
    $ wt_ep12_midnight_seen.append("Jill")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Elena":
    label wt_ep12_midnight_elena_label:
    scene ep12_np2_fw121 with dissolve
    mc "Hey, guys."
    scene ep12_np2_fw122 with dissolve
    jb "[name]! You're just in time for midnight."
    scene ep12_np2_fw121 with dissolve
    mc "I'm not gonna ruin your midnight moment. I wanted to borrow Elena for ten seconds."
    scene ep12_np2_fw123 with dissolve
    el "A nod or a shake is fine. I'll know what you mean."
    scene ep12_np2_fw121 with dissolve
    mc "A nod it is."
    scene ep12_np2_fw123 with dissolve
    el "I'll let him know. Thanks."
    scene ep12_np2_fw124 with dissolve
    jb "Let me know what?"
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    $ renpy.sound.play("sound_effects/season3/fireworks_mc.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_mc_ep12 movie with dissolve
    "HAPPY NEW YEAR!!!"
    pause 9.33
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33
    play sound "sound_effects/shove.mp3"
    scene ep12_np2_fw125 with hpunch
    jb "I fucking love you, man."
    scene ep12_np2_fw126 with dissolve
    mc "Haha... Happy New Year, JB."
    scene ep12_np2_fw125 with dissolve
    jb "Oh, it will be. It will be."
    $ new_bio("You", "During the New Year's Eve party, I spent midnight alone.")
    $ wt_ep12_midnight_seen.append("Elena")
    if wt_ep9_branch_numbers > 1:
            jump wt_ep12_midnight_control_label
elif ep12_midnight_kiss == "Alone":
    scene ep12_np2_fw127 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw128 with dissolve
    $ renpy.pause()
    scene ep12_np2_fw185 with dissolve
    "THREE! TWO! ONE!"
    "HAPPY NEW YEAR!!!"
    $ renpy.sound.play("sound_effects/season3/fireworks_mc.mp3",channel="dj1", loop=False)
    scene bg anim_fireworks_mc_ep12 movie with dissolve
    pause 9.33
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks < 2:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj3", loop=False)
        scene bg anim_fireworks_lots2_ep12 movie with dissolve
        pause 10.66
        if ep12_pp_fireworks == 0:
            $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
            scene bg anim_fireworks_lots3_ep12 movie with dissolve
            pause 11.33

    scene ep12_np2_fw129 with dissolve
    ti "Alone, too, huh?"
    scene ep12_np2_fw130 with dissolve
    if breakup and (tc > 4 or ep4_toldDerekAboutJade or ep12_break_or_tell == "tell" or ep12_break_or_tell == "break"):
        mc "Yeah, but it's alright. I deserve to be."
    else:
        mc "Yeah. But it's alright."
    scene ep12_np2_fw129 with dissolve
    if breakup and (tc > 4 or ep4_toldDerekAboutJade or ep12_break_or_tell == "tell" or ep12_break_or_tell == "break"):
        ti "No one deserves to be alone."
    ti "Wanna join our club?"
    scene ep12_np2_fw130 with dissolve
    mc "What's your club?"
    scene ep12_np2_fw131 with dissolve
    mia "Hotties without prospects."
    if "sad" in event_list:
        jump ep12_rej_fw_label
    scene ep12_np2_fw130 with dissolve
    menu:
        "Join their club":
            $ ep12_hotties_club = True
            scene ep12_np2_fw133 with dissolve
            mc "Haha! What a sad club. Count me in."
            scene ep12_np2_fw134 with dissolve
            er "I can't believe none of us are getting kissed tonight..."
            scene ep12_np2_fw133 with dissolve
            mc "It doesn't have to end that way. I'm here to help."
            scene ep12_np2_fw135 with dissolve
            mia "No, no. We agreed. Either we all get kissed, or none of us do."
            scene ep12_np2_fw133 with dissolve
            mc "Is that the club motto?"
            scene ep12_np2_fw136 with dissolve
            ti "[name] will kiss all three of us. Right?"
            scene ep12_np2_fw133 with dissolve
            mc "All for one, one for all."
            scene ep12_np2_fw137 with dissolve
            mia "Bring it in here."
            scene ep12_np2_fw138 with dissolve
            "*{i}Smack{/i}*"
            scene ep12_np2_fw139 with dissolve
            ti "*{i}Smack{/i}* Mmm..."
            scene ep12_np2_fw140 with dissolve
            mia "*{i}Smack{/i}*"
            scene ep12_np2_fw141 with dissolve
            er "*{i}Smack{/i}*"
            scene ep12_np2_fw142 with dissolve
            mc "Well, Happy New Year..."
            mc "This is a great club, girls."
            scene ep12_np2_fw143 with dissolve
            "Hahaha!"
            if "Sage" in breakup:
                scene ep12_np2_fw143b with dissolve
            elif "Jill" in breakup:
                scene ep12_np2_fw143c with dissolve
            $ renpy.pause()
            scene ep12_np2_fw144 with dissolve
            $ renpy.pause()
            $ new_bio("Tiffani", "During the New Year's Eve party, I kissed Mia, Erin, and Tiffani at midnight.")
            $ new_bio("You", "During the New Year's Eve party, I kissed Mia, Erin, and Tiffani at midnight.")
        "Stay alone":
            label ep12_rej_fw_label:
            scene ep12_np2_fw132 with dissolve
            if "sad" in event_list:
                mc "Sorry, but I need to be alone with my thoughts."
            else:
                mc "Sorry, but I'm more of an \"Alone is strong\" kind of club member."
            $ new_bio("You", "During the New Year's Eve party, I spent midnight alone.")

jump ep12_np2_afterny_label

label ep12_np2_smc_label:
scene ep12_np2_smc1
hide screen dance_filter_screen
with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if tc > 4 and persistent.no_cheater:
                           "scrappy" "You have too many cheater points and Sage's path will end here (need less than 4)"
                        if tc <= 4 and (ep11_sage_love == 1 or RPsage < 22 or ep12_zoey_friend):
                           if ep11_sage_love == 1:
                                "scrappy" "Sage didn't say the she loved you and her path will end here"
                           if RPsage < 22:
                                "scrappy" "You have too low Sage's points and her path will end here (need more than 22)"
                           if ep12_zoey_friend:
                                "scrappy" "You remained friends with Zoey and will end Sage's path here"
sa "Are you feeling ok?"
play music "music/ep12/licensed_music/track208.mp3"
scene ep12_np2_smc2 with dissolve
mc "Yeah. You didn't have to do that."
scene ep12_np2_smc1 with dissolve
sa "You don't single people out like that for fun."
sa "It could have ended horribly."
scene ep12_np2_smc2 with dissolve
if ep12_mc_slut:
    mc "Don't you think it ended horribly?"
    scene ep12_np2_smc3 with dissolve
    sa "A lot of them drank, I saw..."
else:
    mc "I know."
scene ep12_np2_smc4 with dissolve
sa "Do you want to talk about it?"
if tc > 4 and not persistent.no_cheater:
    $ event_list.append("sad")
    $ breakup.append("Sage")
    scene ep12_np2_smc5 with dissolve
    mc "Maybe we should."
    scene ep12_np2_smc4 with dissolve
    sa "Go ahead."
    scene ep12_np2_smc6 with dissolve
    mc "I'm not sure what's up with me. I've felt off and weird lately. And I'm not quite sure about what I'm doing."
    mc "I've made some questionable choices during our time together, and I've found myself drawn to others."
    scene ep12_np2_smc7 with dissolve
    sa "I...didn't expect you to say that. Are you drawn to others? Who?"
    scene ep12_np2_smc6 with dissolve
    mc "Like, in general. You know?"
    scene ep12_np2_smc7 with dissolve
    sa "Well, everyone can find someone attractive. There's nothing wrong with that..."
    sa "But that's not what you're saying, are you?"
    scene ep12_np2_smc6 with dissolve
    mc "If I'm having these thoughts and urges while I'm in a relationship with you..."
    mc "I feel like I'm not ready for our relationship."
    scene ep12_np2_smc8 with dissolve
    sa "So, you want to be single and fuck others? Is that what you're saying?"
    scene ep12_np2_smc6 with dissolve
    mc "Not quite. But..."
    mc "I think we rushed into our relationship. And then I think about the challenges we'd face next year after you quit college."
    mc "Combined with all that... Maybe it's for the best if we end it."
    if RPsage >= 22:
        scene ep12_np2_smc10 with dissolve
        sa "*{i}Sobs{/i}* I didn't want to make this decision already, [name]."
        sa "I know next year will be different, but I still wanted to do this with you."
        scene ep12_np2_smc13 with dissolve
        sa "But I can't do that if you want to live like you're single."
        sa "Fuck..."
        scene ep12_np2_smc11 with dissolve
        mc "I'm sorry for upsetting you..."
        mc "I love being together with you. We've had an amazing time and friendship..."
        mc "...but I'm not in love with you, and I don't think I'll get there."
    else:
        scene ep12_np2_smc7 with dissolve
        sa "*{i}Sigh{/i}* I didn't want to think about this for at least another six months, [name]."
        sa "Don't you think I know how hard it will be for us? Of course, I do."
        sa "Everything will change after I graduate."
        scene ep12_np2_smc10 with dissolve
        sa "But that's not the real issue. You want to live the single life..."
        scene ep12_np2_smc11 with dissolve
        mc "I'm sorry for upsetting you..."
        mc "I love being together with you. We have an amazing time and friendship..."
        mc "...but I'm not in love with you, and I don't think I'll get there."
        scene ep12_np2_smc10 with dissolve
        sa "I'm not in love with you either. At least not in that way."
    scene ep12_np2_smc12 with dissolve
    $ renpy.pause()
    scene ep12_np2_smc13 with dissolve
    sa "Let's end it then."
    scene ep12_np2_smc11 with dissolve
    mc "I think we have to."
    stop music fadeout 3
    scene ep12_np2_smc14 with dissolve
    $ renpy.pause()
    scene ep12_np2_smc15 with dissolve
    $ renpy.pause()
    $ mphone_next_song()
    $ new_bio("Sage", "I broke up with Sage during the New Year's Eve party.")
    $ event_list.append("ep12_np2_mjmc_label")
else:
    scene ep12_np2_smc5 with dissolve
    if ep12_mc_slut:
        mc "What else can I say?"
    else:
        mc "And say what?"
    if ep11_sage_love == 1 or RPsage < 22 or ep12_zoey_friend:
        $ event_list.append("sad")
        $ breakup.append("Sage")
        $ breakup.append("amicable")
        scene ep12_np2_smc9 with dissolve
        $ renpy.pause()
        scene ep12_np2_smc6 with dissolve
        mc "It looks like you have something on your mind."
        scene ep12_np2_smc7 with dissolve
        sa "I don't know if it's the New Year or if there's something wrong with me, but I think we need to talk."
        scene ep12_np2_smc6 with dissolve
        mc "It doesn't feel great when you put it like that."
        scene ep12_np2_smc7 with dissolve
        sa "*{i}Sigh{/i}* It doesn't feel great for me at all, [name]."
        sa "Next year will be different for me. I'll graduate and don't know what's next."
        scene ep12_np2_smc16 with dissolve
        sa "I feel sad when I think about leaving B&R and you, but I need to start thinking about my future."
        sa "Your time here has barely begun, and mine is close to an end."
        scene ep12_np2_smc7 with dissolve
        sa "All these questions are whirling around in my head... How will we do it? Can we keep a strong connection after college?"
        scene ep12_np2_smc6 with dissolve
        mc "Anything is possible if we want it."
        scene ep12_np2_smc7 with dissolve
        sa "Yeah... But that's what bothers me."
        sa "When I think about all of that... I'm not sure how much I want it."
        scene ep12_np2_smc6 with dissolve
        mc "The future or me?"
        scene ep12_np2_smc7 with dissolve
        sa "Us..."
        scene ep12_np2_smc16 with dissolve
        if ep11_sage_love == 1 or RPsage < 22:
            sa "Everything about you is amazing, but I don't think I can fall in love with you."
            sa "And it's not because I'm not willing to try."
            sa "I'm simply not feeling those feelings for you."
            sa "There have been times when I thought I was feeling something. Times when I pushed myself to feel something."
            scene ep12_np2_smc7 with dissolve
            sa "But all I felt was love for you as a person. But that's not the same kind of love that I need it to be."
            if ep9_sage_vanilla:
                sa "There's an attraction between us. We have great talks. But that's not enough."
            else:
                sa "There's an attraction between us. We have great sex. But that's not enough."
            sa "And I don't want to hurt you later by leading you on."
            scene ep12_np2_smc6 with dissolve
            mc "What you're saying is that you want to break up with me now..."
            scene bg anim_sage_nod_ep12 movie with dissolve
            pause
            scene ep12_np2_smc6 with dissolve
            mc "*{i}Sigh{/i}*"
            mc "I get it... Hey, if you don't feel something, you don't."
            if ep12_zoey_friend:
                mc "This isn't about Zoey, right?"
            else:
                mc "This isn't about Zoey, right? Because I'm no longer her friend."
            scene ep12_np2_smc17 with dissolve
            sa "No. She might have been a part of it, but there's much more to it than her."
            sa "I wish it were different. But I can't force my feelings. It's not true to do that."
            scene ep12_np2_smc6 with dissolve
            mc "You need to stay true to yourself, then..."
            scene ep12_np2_smc7 with dissolve
            sa "You have no idea how hard this is for me."
            sa "But at the same time, I don't want to go on for another six months knowing this has to happen."
            scene ep12_np2_smc6 with dissolve
            mc "I can tell something has weighed on your mind lately. You haven't been present."
            scene ep12_np2_smc16 with dissolve
            sa "Please, don't hate me."
            scene ep12_np2_smc6 with dissolve
            mc "Sage... I could never hate you."
            mc "But this makes it difficult for me, because I feel something different for you."
        else:
            sa "I talked to Zoey tonight...and she told me you're staying friends."
            scene ep12_np2_smc6 with dissolve
            mc "Yeah... I was planning to talk to you about that."
            scene ep12_np2_smc7 with dissolve
            sa "I'm sure you were. But it doesn't matter to me, [name]..."
            sa "I already know how I feel about it."
            scene ep12_np2_smc16 with dissolve
            sa "And if you respected me and my feelings enough, this wouldn't be the case."
            sa "I can't stay in this relationship with you any longer."
            scene ep12_np2_smc6 with dissolve
            mc "What? I thought you said my friendship with Zoey wasn't an ultimatum."
            scene ep12_np2_smc7 with dissolve
            sa "It wasn't. But I know myself..."
            sa "I won't be able to stand for it. She's already proven my point, and you choosing to stay friends with her after what she did..."
            scene ep12_np2_smc8 with dissolve
            sa "It hurts. Her telling you that she loved you hurt. And you brushing that off like it's nothing hurts even more."
            sa "And I get it, you value her friendship a lot. It's clear."
            if ep11_sage_love == 2:
                scene ep12_np2_smc6 with dissolve
                mc "Yes, I value it a lot, but I'm in love with you."
            scene ep12_np2_smc16 with dissolve
            sa "But to me, it looks like you value that friendship more than our relationship. And that's why I have to leave."
            sa "It becomes especially true when combined with all the other doubts on my mind."
            scene ep12_np2_smc6 with dissolve
            mc "I'm not choosing Zoey over you, Sage."
            scene ep12_np2_smc8 with dissolve
            sa "Maybe not romantically... But emotionally, you already did."
            scene ep12_np2_smc6 with dissolve
            mc "Sage... I don't know what to say..."
            mc "We don't look at this the same way. But I don't want this to be over because of Zoey."
            scene ep12_np2_smc7 with dissolve
            sa "I know... But you made your choice, and I made mine."
            sa "I'm sorry..."
        stop music fadeout 3
        scene ep12_np2_smc18 with dissolve
        $ renpy.pause()
        scene ep12_np2_smc19 with dissolve
        $ renpy.pause()
        $ mphone_next_song()
        $ currentFreeRoamLabel = "ep12_np_balcony_label"
        if ep11_sage_love == 1 or RPsage < 22:
            $ new_bio("Sage", "Sage broke up with me during the New Year's Eve party. She wasn't in love with me and didn't see our relationship lasting past her graduation.")
        else:
            $ new_bio("Sage", "Sage broke up with me during the New Year's Eve party. My friendship with Zoey was too much for her to handle.")
        $ event_list.append("ep12_np2_mjmc_label")
    else:
        $ roadSage = True
        scene ep12_np2_smc4 with dissolve
        sa "I wanted to check that you're truly ok. That's it."
        scene ep12_np2_smc5 with dissolve
        mc "I think you're sweet for caring this much about me."
        scene ep12_np2_smc9 with dissolve
        $ renpy.pause()
        scene ep12_np2_smc6 with dissolve
        mc "It looks like you have something on your mind."
        scene ep12_np2_smc20 with dissolve
        sa "I don't know if it's New Year or if there's something wrong with me, but I think we need to talk."
        scene ep12_np2_smc6 with dissolve
        mc "Um... I gotta say it doesn't feel great when you put it like that."
        scene ep12_np2_smc20 with dissolve
        sa "Next year will be different for me. I'll graduate, and I'm unsure what's next."
        scene ep12_np2_smc21 with dissolve
        sa "I feel sad when I think about leaving B&R and you, but I need to start thinking about my future."
        sa "Your time here has barely begun, and mine is close to and end."
        scene ep12_np2_smc22 with dissolve
        sa "And you came into my life this late here... Yet you've had the biggest impact of everything that's happened."
        scene ep12_np2_smc21 with dissolve
        sa "All these questions are whirling around in my head... How will we do it? Can we keep a strong connection after college?"
        scene ep12_np2_smc6 with dissolve
        mc "Anything is possible if we want it."
        scene ep12_np2_smc22 with dissolve
        sa "Do you want it? Do you want us?"
        if ep11_sage_love == 2:
            sa "Because I'm in love with you, and I need to know how to plan my future."
            scene ep12_np2_smc6 with dissolve
            mc "This worries you a lot, huh?"
            scene ep12_np2_smc20 with dissolve
            sa "It does."
            scene ep12_np2_smc23 with dissolve
            mc "I love you, Sage. You know that."
        else:
            sa "Because I'm falling in love with you, and it's keeping me from planning my future."
            scene ep12_np2_smc23 with dissolve
            mc "Sage... I'm falling in love with you, too."
            scene ep12_np2_smc24 with dissolve
            sa "You are?"
            scene ep12_np2_smc23 with dissolve
            mc "Truth is, I fell for you quite some time ago. But I've been too scared to tell you."
            scene ep12_np2_smc24 with dissolve
            sa "Have you been scared to tell me?"
            scene ep12_np2_smc23 with dissolve
            mc "Yeah... What if you didn't feel the same way? Ugh..."
            mc "I'm so relieved and happy to hear you say that."
            scene ep12_np2_smc30 with dissolve
            mc "But it's not fun to hear that you worry this much."
        mc "Why don't we spend this last semester of yours together and find out if our bond is strong enough to survive?"
        scene ep12_np2_smc25 with dissolve
        mc "If it's still worth fighting for us in 5-6 months, the answer will be easy."
        mc "And maybe during that time, you can think more about what you want your future to be like."
        scene ep12_np2_smc26 with dissolve
        mc "I know that I want to be with you."
        if ep9_sage_vanilla:
            mc "You're amazing on so many levels, and you surprise me daily with your thoughts and warmth."
            mc "There's so much more to you than meets the eye."
        else:
            mc "And that's not just because of the amazing sex we have."
        scene ep12_np2_smc27 with dissolve
        sa "I think I needed to hear you say that I'm in your plans."
        scene ep12_np2_smc26 with dissolve
        mc "In my plans? You are the plan."
        mc "I love you, Sage."
        scene ep12_np2_smc27 with dissolve
        sa "I love you so much."
        scene anim_sage_kiss_ep12 with dissolve
        $ renpy.pause()
        scene ep12_np2_smc31 with dissolve
        jo "Get a room..."
        scene ep12_np2_smc28 with dissolve
        sa "Shall we?"
        scene ep12_np2_smc29 with dissolve
        if branchZoey:
            jump ep12_np2_zmc_label
        elif ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch:
            jump ep12_np2_mchen_label
        if "ep12_np2_ot_label" in event_list:
            jump ep12_fr_party_notyet_label
        menu:
            "End freeroam":
                stop music fadeout 3
                mc "A room sounds good."
                $ phone_clear_jump_label = "ep12_sage_lewd_label"
                jump end_freeroam
            "Not yet":
                label ep12_fr_party_notyet_label:
                stop music fadeout 3
                mc "A room sounds good. But I need to do something first."
                scene ep12_np2_smc28 with dissolve
                sa "Hurry up."
                $ mphone_next_song()
                $ currentFreeRoamLabel = "ep12_np_balcony_label"
jump endEvent

label ep12_sage_lewd_label:
jump ep12_np2_mjmc_label
label ep12_sage_lewdb_label:

if _in_replay:
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
    $ ep12_pp_fireworks = 0
    play music "music/ep12/licensed_music/track204.mp3"
$ ep12_midnight_kiss = "Sage"
hide screen new_phone_screen
scene ep12_sage_lewd1 with dissolve
mc "This room?"
scene ep12_sage_lewd2 with dissolve
sa "Would you prefer the dining hall or the stage?"
scene ep12_sage_lewd3 with dissolve
mc "Hm... Fair point."
scene ep12_sage_lewd4 with dissolve
sa "What's not to like about it? It's private and has a couch to fuck on."
scene ep12_sage_lewd5 with dissolve
mc "I'm with you. But who's got access here tonight?"
scene ep12_sage_lewd6 with dissolve
sa "Well, it's me, Mom, Bella, and Rusty."
scene ep12_sage_lewd5 with dissolve
mc "That's a spectrum of mixed feelings I get when I imagine them walking in on us."
scene ep12_sage_lewd7 with dissolve
sa "Haha, yeah! With Mom, it would be awkward."
scene ep12_sage_lewd5 with dissolve
mc "Rusty is cool. He'd understand. And Bella..."
scene ep12_sage_lewd8 with dissolve
sa "That would be hot."
scene ep12_sage_lewd9 with dissolve
mc "Hot?"
scene ep12_sage_lewd8 with dissolve
sa "I'm teasing you. What were you gonna say?"
scene ep12_sage_lewd9 with dissolve
mc "When we met, I was naked, so she had already seen it."
scene ep12_sage_lewd10 with dissolve
sa "I can't believe she got to see it before me."
scene ep12_sage_lewd11 with dissolve
mc "You get to see it tonight."
scene ep12_sage_lewd10 with dissolve
sa "Haha, I better! I didn't dress this nicely not to get lucky with you."
scene ep12_sage_lewd12 with dissolve
mc "You look amazing in red."
sa "It's the cleavage, not the color, that you like."
scene ep12_sage_lewd11 with dissolve
mc "I like the entire package."
scene ep12_sage_lewd13 with dissolve
sa "*{i}Smack{/i}*"
scene ep12_sage_lewd10 with dissolve
sa "Do you think someone ever fucked in here before? Or are we the first ones to do it?"
scene ep12_sage_lewd11 with dissolve
mc "No one's ever done what I'm gonna do to you in here before."
scene ep12_sage_lewd10 with dissolve
sa "You think?"
scene ep12_sage_lewd11 with dissolve
mc "I'll show you..."
scene ep12_sage_lewd13 with dissolve
sa "*{i}Smack{/i}*"
scene ep12_sage_lewd14 with dissolve
$ renpy.pause()
scene ep12_sage_lewd15 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_sage_lewd16 with dissolve
$ renpy.pause()
scene ep12_sage_lewd17 with dissolve
$ renpy.pause()
scene ep12_sage_lewd18 with dissolve
$ renpy.pause()
scene ep12_sage_lewd19 with dissolve
$ renpy.pause()
play sound "sound_effects/clothes.mp3"
scene ep12_sage_lewd21 with dissolve
$ renpy.pause()
scene ep12_sage_lewd20 with dissolve
$ renpy.pause()
scene ep12_sage_lewd22 with dissolve
$ renpy.pause()
scene ep12_sage_lewd23 with dissolve
$ renpy.pause()
scene ep12_sage_lewd24 with dissolve
$ renpy.pause()
scene ep12_sage_lewd25 with dissolve
$ renpy.pause()
scene ep12_sage_lewd26 with dissolve
$ renpy.pause()
scene ep12_sage_lewd27 with dissolve
$ tmpInt = 0
label ep12_sage_lewd_loop1_label:
menu:
    "Kiss her":
        $ tmpInt += 1
        scene anim_sage_lewd_kiss_ep12 with dissolve
        sa "Mmm... *{i}Smack{/i}*"
        pause
        jump ep12_sage_lewd_loop1_label
    "Rub her":
        $ tmpInt += 1
        scene anim_sage_rub_ep12 with dissolve
        sa "Mhm... Do it like that..."
        pause
        scene anim_sage_rub2_ep12 with dissolve
        sa "*{i}Moans{/i}* Yes... Keep massaging my clit."
        pause
        jump ep12_sage_lewd_loop1_label
    "69":
        $ tmpInt += 1
        scene anim_sage_69_ep12 with dissolve
        sa "*{i}Suck suck{/i}*"
        mc "*{i}Lick lick{/i}*"
        pause
        scene anim_sage_692_ep12 with dissolve
        sa "*{i}Suck suck glug glug{/i}*"
        pause
        jump ep12_sage_lewd_loop1_label
    "Boobjob":
        $ tmpInt += 1
        scene anim_sage_boob_ep12 with dissolve
        mc "Oh, [sage]... Your tits feel so good."
        pause
        scene anim_sage_boob2_ep12 with dissolve
        sa "And your cock fits so well between them."
        mc "We're a perfect fit, alright."
        pause
        jump ep12_sage_lewd_loop1_label
    "Continue" if tmpInt > 1:
        $ renpy.pause(0.5)

scene ep12_sage_lewd27b with dissolve
sa "I need to have you..."

$ tmpInt = 0
$ tmpBool3 = False
label ep12_sage_lewd_loop2_label:
menu:
    "Cowgirl":
        $ tmpInt += 1
        scene anim_sage_ride_ep12 with dissolve
        sa "*{i}Moans{/i}*"
        mc "Yes... Ride me, [sage]..."
        pause
        scene anim_sage_ride2_ep12 with dissolve
        sa "Hngn... Stretch me out, [mc_sage]. My pussy wants you."
        pause
        scene anim_sage_ride3_ep12 with dissolve
        mc "You're the best girlfriend ever."
        sa "*{i}Moans{/i}* Because I ride you like this?"
        mc "No. You just are."
        pause
        jump ep12_sage_lewd_loop2_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_sage_ride_anal_ep12 with dissolve
        sa "Ahh... *{i}Moans{/i}*"
        mc "I love your ass so much."
        pause
        scene anim_sage_ride2_anal_ep12 with dissolve
        sa "Hngn... It's so tight that I have to pull my cheeks aside for your dick."
        mc "Whatever you're doing, keep doing it."
        pause
        jump ep12_sage_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_sage_doggy_ep12 with dissolve
        sa "Fuck me, [mc_sage]! Fuck me!"
        pause
        scene anim_sage_doggy2_ep12 with dissolve
        mc "This is too hot."
        sa "Haha, you've seen my ass like a hundred times. Does it still excite you?"
        mc "You always make me rock hard."
        pause
        jump ep12_sage_lewd_loop2_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_sage_doggy_ep12 with dissolve
        sa "*{i}Moans{/i}* Ahh... Take it easy, [mc_sage]."
        mc "Am I going too deep?"
        sa "Yeah, slow it down a bit..."
        pause
        scene anim_sage_doggy_anal_ep12 with dissolve
        mc "Like this?"
        sa "Mmm... Yes... Much better. Fuck!"
        pause
        jump ep12_sage_lewd_loop2_label
    "Standing":
        $ tmpInt += 1
        scene anim_sage_stand_ep12 with dissolve
        sa "God, you're so sexy tonight."
        mc "You think?"
        pause
        scene anim_sage_stand2_ep12 with dissolve
        sa "*{i}Moans{/i}* Yeah, I've been watching you all night."
        sa "And looking at you from afar, all I kept thinking was..."
        sa "There he is... There's my hot boyfriend."
        pause
        scene anim_sage_stand3_ep12 with dissolve
        mc "Haha... That's so sweet..."
        pause
        jump ep12_sage_lewd_loop2_label
    "Standing (Anal)":
        $ tmpInt += 1
        scene anim_sage_stand_anal_ep12 with dissolve
        sa "Ahhh... Ahhh!!! Yes! Yes!"
        sa "Fuck my ass, [mc_sage]! Fuck it!"
        pause
        scene anim_sage_stand2_anal_ep12 with dissolve
        mc "I'm gonna cum from this..."
        sa "Not yet, [mc_sage]. Not yet..."
        pause
        jump ep12_sage_lewd_loop2_label
    "Missionary":
        $ tmpInt += 1
        scene anim_sage_miss_ep12 with dissolve
        sa "*{i}Moans{/i}* Yes... Yes!"
        pause
        scene anim_sage_miss2_ep12 with dissolve
        if not tmpBool3:
            $ tmpBool3 = True
            sa "Fuck, [mc_sage]... I'm gonna cum. I'm gonna cum."
            mc "That's so sexy. Cum for me, [sage]. Cum!"
            scene ep12_sage_lewd27c with vpunch
            sa "Ahh!!!"
            scene ep12_sage_lewd27d with vpunch
            sa "*{i}Moans{/i}* FUCK!!!"
            scene ep12_sage_lewd27e with vpunch
            sa "Ahhh..."
        else:
            pause
        jump ep12_sage_lewd_loop2_label
    "Missionary (Anal)":
        $ tmpInt += 1
        scene anim_sage_miss_anal_ep12 with dissolve
        sa "Do you like that feeling, [mc_sage]?"
        sa "Having my asshole wrapped around your cock..."
        pause
        scene anim_sage_miss2_anal_ep12 with dissolve
        mc "Yeah, I fucking love this feeling."
        mc "Your body is so sexy."
        sa "*{i}Moans{/i}*"
        pause
        jump ep12_sage_lewd_loop2_label
    "Cum" if tmpInt > 2:
        mc "Hngn... Fuck! I can't help it... I'm gonna cum."
        menu:
            "Facial":
                scene anim_sage_boob2_ep12 with dissolve
                sa "Cum, [mc_sage]! Cum! Shoot your load over me!"
                scene ep12_sage_lewd34 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_sage_lewd34 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_sage_lewd34 at vpunch, cum2
                mc "Ahh!!! Fuck!"
                scene ep12_sage_lewd35 with dissolve
                sa "Mmm..."
            "Creampie":
                scene anim_sage_stand3_ep12 with dissolve
                sa "Cum, [mc_sage]! Cum! Cum inside me... Give me your warm cum."
                scene ep12_sage_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sage_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sage_lewd32 at vpunch, cum1
                mc "Ahh!!! Fuck!"
                scene ep12_sage_lewd33 with dissolve
                sa "Mmm..."
            "Creampie (Anal)":
                scene anim_sage_stand2_anal_ep12 with dissolve
                sa "Cum, [mc_sage]! Cum! Cum inside me... Give me your warm cum."
                scene ep12_sage_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sage_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sage_lewd28 at vpunch, cum1
                mc "Ahh!!! Fuck!"
                scene ep12_sage_lewd29 with dissolve
                sa "Mmm..."
            "On ass":
                scene anim_sage_doggy2_ep12 with dissolve
                sa "Cum, [mc_sage]! Cum! Give me your warm cum."
                scene ep12_sage_lewd30 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_sage_lewd30 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_sage_lewd30 at vpunch, cum2
                mc "Ahh!!! Fuck!"
                scene ep12_sage_lewd31 with dissolve
                sa "Mmm..."

scene ep12_sage_lewd36 with dissolve
$ renpy.pause()
scene ep12_sage_lewd37 with dissolve
$ renpy.pause()
scene ep12_sage_lewd38 with dissolve
sa "You were right. No one ever did what we did in here."
scene ep12_sage_lewd39 with dissolve
mc "Told you."
scene ep12_sage_lewd40 with dissolve
sa "5 out of 5."
scene ep12_sage_lewd41 with dissolve
mc "You're kidding me?"
scene ep12_sage_lewd40 with dissolve
sa "Kind of. Haha..."
scene ep12_sage_lewd41 with dissolve
mc "Aha... So, it wasn't..."
scene ep12_sage_lewd42 with dissolve
sa "You've always been 5 out of 5, [name]."
scene ep12_sage_lewd43 with dissolve
mc "Haha, I don't believe that. Even I don't think so."
scene ep12_sage_lewd42 with dissolve
sa "Well, I do. There have been some disappointing fives, but they were all fives nonetheless."
play sound "sound_effects/season3/firework_sage.mp3"
scene ep12_sage_lewd44 with dissolve
mc "Look... Fireworks... It must be midnight."
scene ep12_sage_lewd45 with dissolve
sa "Haha! We missed it!"
scene ep12_sage_lewd44 with dissolve
mc "We can watch it from in here."
$ renpy.sound.play("sound_effects/season3/fireworks_kiss.mp3",channel="dj1", loop=False)
scene bg anim_fireworks_sage_ep12 movie with dissolve
pause 10.58
if ep12_pp_fireworks < 2:
    $ renpy.sound.play("sound_effects/season3/fireworks_lots1.mp3",channel="dj2", loop=False)
    scene bg anim_fireworks_lots2_ep12 movie with dissolve
    pause 10.66
    if ep12_pp_fireworks == 0:
        $ renpy.sound.play("sound_effects/season3/fireworks_lots2.mp3",channel="dj4", loop=False)
        scene bg anim_fireworks_lots3_ep12 movie with dissolve
        pause 11.33
scene ep12_sage_lewd46 with dissolve
sa "Happy New Year, [name]."
mc "Happy New Year, Sage."
$ renpy.end_replay()
$ persistent.ep12_lewd_sage = True
$ calcScenes()
show screen new_phone_screen
if ep11_sage_love == 2:
    $ new_bio("Sage", "During the New Year's Eve party, I had sex with Sage at midnight.")
else:
    $ new_bio("Sage", "During the New Year's Eve party, I had sex with Sage at midnight. Sage told me that she loved me.")
$ new_bio("You", "During the New Year's Eve party, I had sex with Sage at midnight.")
$ mphone_stats_add_girl_s3("sage","You had sex with Sage during the New Year's Eve party in episode 12.")
$ wt_ep12_midnight_seen.append("Sage")
if wt_ep9_branch_numbers > 1:
    jump wt_ep12_midnight_control_label
jump ep12_np2_afterny_label

label ep12_np2_jmc_label:
$ currentFreeRoamLabel = "ep12_np_balcony_label"
if ep12_mc_slut:
    $ event_list.append("sad")
    $ breakup.append("Jill")
    scene ep12_np2_jmc1
    hide screen dance_filter_screen
    with dissolve
    mc "Jill. Please, talk to me."
    scene ep12_np2_jmc2 with dissolve
    ji "What can I even say? What the hell happened back there?"
    ji "Is this some sick joke?"
    scene ep12_np2_jmc3 with dissolve
    mc "We all have history, don't we?"
    scene ep12_np2_jmc4 with dissolve
    ji "You call that history? How many girls were there?"
    ji "And they all have been with you during your short time in college. What have you been up to?"
    scene ep12_np2_jmc5 with dissolve
    ji "[name]... How do you think that makes me feel?"
    if tc > 4 and not persistent.no_cheater:
        scene ep12_np2_jmc6 with dissolve
        mc "..."
        scene ep12_np2_jmc4 with dissolve
        ji "Don't you have anything to say for yourself?"
    else:
        scene ep12_np2_jmc6 with dissolve
        mc "I'm sorry, but... Jill. You're the one for me."
        mc "Those girls in there... We weren't a couple when that happened."
        scene ep12_np2_jmc4 with dissolve
        ji "But we've dated almost since you got here. It's too much, I..."
    ji "Uhhhh... I feel sick."
    scene ep12_np2_jmc6 with dissolve
    $ renpy.pause()
    if tc > 4 and not persistent.no_cheater:
        mc "I'm sorry, Jill... I've meant to talk to you about this."
        scene ep12_np2_jmc5 with dissolve
        ji "About all the girls you've been with?"
        scene ep12_np2_jmc6 with dissolve
        mc "No... Not that, but us."
        mc "I don't think I'm ready for a relationship."
        mc "I thought I wanted it, but..."
        mc "The more time I've spent at parties and such, the more I've realized I'm not ready yet."
        scene ep12_np2_jmc7 with dissolve
        mc "I think your heart is in this more than mine. And it wouldn't be fair to you to keep going like this."
        mc "And it's especially true after seeing how much this hurt you."
        mc "I can't keep up with that, and I think I'm heading in the other direction. It wouldn't be honest to keep that from you."
        scene ep12_np2_jmc8 with dissolve
        ji "*{i}Sobs{/i}* Damn you, [name]..."
        scene ep12_np2_jmc9 with dissolve
        mc "{i}Our breakup was brutal.{/i}"
        if ep12_bianca_lewd or ep12_ts_lewd:
            mc "{i}Which is ironic, since I withheld something from her that would have made it even worse.{/i}"
            mc "{i}But I meant what I said to her. I wasn't falling in love with her. I wasn't ready to be tied up.{/i}"
            mc "{i}But I didn't expect Quinn outing me like that before I had the chance to talk to Jill.{/i}"
        else:
            mc "{i}I would have told Jill about my feelings earlier if I had known how.{/i}"
            mc "{i}I don't think my feelings were clear until that point.{/i}"
            mc "{i}But I didn't expect Quinn outing me like that before I had the chance to talk to Jill.{/i}"

        $ new_bio("Jill", "Jill broke up with me after learning about my extensive history with girls on campus. I confessed that my heart wasn't fully in our relationship.")
    else:
        mc "You didn't want to talk about my sexual history."
        mc "Did you expect me to tell you about everyone I had been with, even so?"
        mc "I didn't cheat on you, Jill. I don't think it's cheating when you're dating and not committed. Do you?"
        scene ep12_np2_jmc5 with dissolve
        ji "I think it's clear to see how little I mattered to you, if you could be intimate with that many girls while we were dating."
        scene ep12_np2_jmc6 with dissolve
        mc "It's the past, Jill. It's not now. You know how much I feel for you now."
        scene ep12_np2_jmc4 with dissolve
        ji "It's not the past, [name]. Our relationship was built during that time..."
        ji "It's in our foundation."
        ji "You may not call it cheating, but I'm not fine with it."
        scene ep12_np2_jmc8 with dissolve
        ji "*{i}Sobs{/i}* [name]... We're through."
        scene ep12_np2_jmc7 with dissolve
        mc "Please, don't... Jill."
        scene ep12_np2_jmc9 with dissolve
        mc "{i}Our breakup was brutal.{/i}"
        mc "{i}I wanted to blame Quinn for it...{/i}"
        mc "{i}...but in the end, I knew it was me.{/i}"
        $ new_bio("Jill", "Jill broke up with me after learning about my extensive history with girls on campus. It was too much for her to handle.")
else:
    scene ep12_np2_jmc12
    hide screen dance_filter_screen
    with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if tc > 4  and not persistent.no_cheater:
                           "scrappy" "You have too many cheater points and Jill's path will end here (need less than 4)"
    
    ji "Don't let it get to you."
    scene ep12_np2_jmc13 with dissolve
    mc "Wasn't it embarrassing for you?"
    scene ep12_np2_jmc12 with dissolve
    ji "It was revealing, and I couldn't avoid it."
    if ep12_girl_count > 5:
        ji "But I wasn't embarrassed. Slightly surprised, maybe. But uh..."
        ji "It wasn't a dealbreaker."
    else:
        ji "But I wasn't embarrassed. It reaffirmed what I already knew."
    scene ep12_np2_jmc14 with dissolve
    ji "I feel so strongly for you, [name]."
    if tc > 4 and not persistent.no_cheater:
        $ event_list.append("sad")
        $ breakup.append("Jill")
        scene ep12_np2_jmc16 with dissolve
        mc "Wait..."
        scene ep12_np2_jmc11 with dissolve
        ji "What?"
        scene ep12_np2_jmc10 with dissolve
        mc "I...can't do this to you anymore."
        mc "What you saw in there wasn't the full truth."
        scene ep12_np2_jmc11 with dissolve
        ji "What do you mean? Was there more to it?"
        scene ep12_np2_jmc10 with dissolve
        mc "I'm not ready for a relationship."
        mc "I'm sorry, Jill... I've meant to talk to you about this."
        mc "I thought I wanted it, but..."
        mc "The more time I've spent at parties, the more I've realized I'm not cut out for this relationship."
        scene ep12_np2_jmc6 with dissolve
        mc "I think your heart is in it more than mine. And it wouldn't be fair to you to keep going like this."
        mc "And it's especially true after seeing how you continue to develop feelings for me."
        mc "I can't keep up with that, and I think I'm heading in the other direction. It wouldn't be honest to keep that from you."
        scene ep12_np2_jmc5 with dissolve
        ji "What? Are you breaking up with me?"
        scene ep12_np2_jmc6 with dissolve
        mc "I am..."
        scene ep12_np2_jmc7 with dissolve
        ji "*{i}Sobs{/i}* Damn you, [name]..."
        scene ep12_np2_jmc9 with dissolve
        mc "{i}It was brutal to break up with Jill like that.{/i}"
        if ep12_bianca_lewd or ep12_ts_lewd:
            mc "{i}Which is ironic, since I withheld something from her that would have made it even worse.{/i}"
            mc "{i}But I meant what I said to her. I wasn't falling in love with her. I wasn't ready to be tied up.{/i}"
            if ep12_bianca_lewd:
                mc "{i}And seeing how it went with Rusty and Dwyane earlier that night was an eye-opener. That could very well have been Bianca and Jill.{/i}"
        else:
            mc "{i}I would have told Jill about my feelings earlier if I had known how.{/i}"
            mc "{i}But I don't think my feelings were clear until that point.{/i}"
            mc "{i}I wasn't ready to be tied up. And seeing how it went with Rusty and Dwyane earlier that night was an eye-opener.{/i}"
        $ new_bio("Jill", "I broke up with Jill during the New Year's Eve party. I confessed that my heart wasn't fully in our relationship.")
    else:
        $ roadJill = True
        scene ep12_np2_jmc15 with dissolve
        mc "Jill... I feel the same."
        scene ep12_np2_jmc17 with dissolve
        $ renpy.pause()
        scene ep12_np2_jmc18 with dissolve
        mc "*{i}Sigh{/i}* Thanks... I feel so much better now."
        scene ep12_np2_jmc19 with dissolve
        mc "Let's get back to the party."
        $ new_bio("Jill", "Jill supported me after Quinn tried to embarrass me with her drinking game.")

if not breakup and branchIsabella:
    jump ep12_np2_bmc_label
elif not breakup and branchSage:
    stop music fadeout 3
    jump ep12_np2_smc_label
elif branchZoey:
    jump ep12_np2_zmc_label
elif ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch:
    jump ep12_np2_mchen_label
else:
   jump endEvent
jump endEvent

label ep12_np2_bmc_label:
$ currentFreeRoamLabel = "ep12_np_balcony2_label"
if ep12_mc_slut:
    scene ep12_np2_bmc1
    hide screen dance_filter_screen
    with dissolve
    mc "All those girls drinking... Um... How do I put it?"
    scene ep12_np2_bmc2 with dissolve
    isa "You've been busy."
    scene ep12_np2_bmc1 with dissolve
    mc "I wouldn't put it like that."
    scene ep12_np2_bmc2 with dissolve
    isa "Can you put it in the past? That's all I'm interested in."
    scene ep12_np2_bmc1 with dissolve
    mc "How do you mean?"
    scene ep12_np2_bmc3 with dissolve
    isa "What you and I have is special. I'm asking you to be ok with a whole lot of the baggage I'm carrying."
    isa "My baggage isn't yours to carry, but it still affects you."
    scene ep12_np2_bmc4 with dissolve
    isa "It appears you have baggage of your own, and I'm not surprised. Everyone carries some."
    isa "What I'm asking you is whether it's the past I saw in there, or the present."
    scene ep12_np2_bmc5 with dissolve
    mc "It's the past-me, Bella. Present-me is all about you."
    mc "And you don't have to worry about that."
    scene ep12_np2_bmc6 with dissolve
    isa "That's all I needed to know."
    scene ep12_np2_bmc5 with dissolve
    mc "I didn't lie to you when I told you that I love you."
    scene ep12_np2_bmc12 with dissolve
    $ renpy.pause()
    scene ep12_np2_bmc14 with dissolve
    if ep12_bella_love:
        isa "I love you, [name]."
    else:
        isa "I can tell."
    scene ep12_np2_bmc12 with dissolve
    mc "And please don't make it a thing to call me a slut."
    scene ep12_np2_bmc14 with dissolve
    isa "You know me too well. I was about to call you that."
    scene ep12_np2_bmc12 with dissolve
    mc "Haha, no, you weren't!"
    $ new_bio("Isabella", "Bella supported me despite learning that my history with girls on campus was extensive.")
else:
    scene ep12_np2_bmc15
    hide screen dance_filter_screen
    with dissolve
    mc "Over here..."
    scene ep12_np2_bmc13 with dissolve
    mc "Thank you. I needed that."
    scene ep12_np2_bmc2 with dissolve
    isa "Did she make you feel ashamed?"
    scene ep12_np2_bmc1 with dissolve
    mc "She tried to make a fool out of me in front of everyone."
    scene ep12_np2_bmc2 with dissolve
    isa "What's her deal anyway?"
    scene ep12_np2_bmc1 with dissolve
    mc "Who knows? She's got issues."
    scene ep12_np2_bmc3 with dissolve
    isa "Even if everyone in that room had drunk, I wouldn't have been worried."
    scene ep12_np2_bmc5 with dissolve
    mc "Even the guys?"
    scene ep12_np2_bmc6 with dissolve
    isa "Ok, that would have worried me."
    scene ep12_np2_bmc5 with dissolve
    mc "Tsk. It's ok for you to worry."
    mc "I just didn't think I'd be exposed like that."
    scene ep12_np2_bmc6 with dissolve
    isa "Let's be honest. You've been exposed in worse ways before this semester."
    scene ep12_np2_bmc5 with dissolve
    mc "Don't remind me."
    scene ep12_np2_bmc7 with dissolve
    isa "When I first met you, you were exposed."
    scene ep12_np2_bmc8 with dissolve
    mc "Not entirely true, is it? Earlier than that... Remember the library?"
    scene ep12_np2_bmc7 with dissolve
    isa "Not to mention the posters all over campus."
    scene ep12_np2_bmc8 with dissolve
    mc "That's enough. You've made your point. I'm an embarrassment."
    scene ep12_np2_bmc7 with dissolve
    isa "No. That's not my point."
    isa "My point is..."
    scene ep12_np2_bmc9 with dissolve
    isa "We persevere. You and I."
    isa "Somehow, through adultery, secrets, and public nudity... We persevere."
    isa "And I'm still standing here with you tonight, feeling happy."
    scene ep12_np2_bmc10 with dissolve
    mc "You're right. We rock."
    scene ep12_np2_bmc11 with dissolve
    isa "We rock so hard."
    scene ep12_np2_bmc12 with dissolve
    $ renpy.pause()
    $ currentFreeRoamLabel = "ep12_np_balcony_label"
    $ new_bio("Isabella", "Bella supported me after Quinn tried to embarrass me with her drinking game.")

if not breakup and branchSage:
    stop music fadeout 3
    jump ep12_np2_smc_label
elif branchZoey:
    jump ep12_np2_zmc_label
elif ep11_quinn_question[0] and (ep12_riona_side == "Quinn" or wt_ep11_quinn_riona_question) and not ep12_quinn_ditch:
    jump ep12_np2_mchen_label
else:
   jump endEvent
jump endEvent

label ep12_jill_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_jill == None:
        $ mc_jill = name
    else:
        $ mc_jill = persistent.mc_jill
    if persistent.jill == None:
        $ jill = "Jill"
    else:
        $ jill = persistent.jill
    $ ep12_jill_love = True
    play music "music/ep12/licensed_music/track204.mp3"
hide screen new_phone_screen

scene ep12_np2_fw158 with dissolve
ji "Will you follow me home?"
scene ep12_np2_fw157 with dissolve
mc "Are we leaving already?"
scene ep12_np2_fw158 with dissolve
ji "If you don't mind."
scene ep12_np2_fw157 with dissolve
mc "If you're tired, you're tired."
scene ep12_jill_lewd1 with dissolve
ji "I'm not tired yet. But I want to show you something."
scene ep12_jill_lewd2 with wipeleft
mc "Is there no one here tonight?"
scene ep12_jill_lewd3 with dissolve
ji "No, they rented a hotel in the city for their party. One with a spa and a big conference hall."
ji "I'd say their party is even bigger than yours since they didn't limit the invite list to students."
scene ep12_jill_lewd4 with dissolve
mc "It sounds like you missed out on a nice party."
scene ep12_jill_lewd5 with dissolve
ji "Haha... I was exactly where I wanted to be tonight."
stop music fadeout 3
ji "I was with you. And I had a wonderful time."
play music "music/ep12/licensed_music/track222.mp3"
scene ep12_jill_lewd6 with dissolve
$ renpy.pause()
scene ep12_jill_lewd7 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

stop music fadeout 3
scene ep12_jill_lewd8 with dissolve
mc "Simply beautiful..."
play music "music/ep12/licensed_music/track204.mp3"
scene ep12_jill_lewd9 with dissolve
$ renpy.pause()
scene ep12_jill_lewd10 with dissolve
$ renpy.pause()
scene ep12_jill_lewd11 with dissolve
$ renpy.pause()
scene ep12_jill_lewd12 with dissolve
$ renpy.pause()
scene ep12_jill_lewd13 with dissolve
$ renpy.pause()
scene ep12_jill_lewd14 with dissolve
$ renpy.pause()
scene ep12_jill_lewd15 with dissolve
mc "What are you-?"
scene ep12_jill_lewd16 with dissolve
ji "Shh..."
scene ep12_jill_lewd17 with dissolve
$ renpy.pause()
scene ep12_jill_lewd18 with dissolve
$ renpy.pause()
scene ep12_jill_lewd19 with dissolve
$ renpy.pause()
scene ep12_jill_lewd20 with dissolve
ji "*{i}Smack{/i}*"
scene ep12_jill_lewd21 with dissolve
$ renpy.pause()

scene ep12_jill_lewd22 with dissolve
ji "*{i}Soft moan{/i}*"
mc "Oh, [jill]... This is something else..."
scene ep12_jill_lewd23 with dissolve
ji "Follow my lead, [mc_jill]."
ji "I want to show you how much I appreciate you."
scene anim_jill_stand1b_ep12 with dissolve
mc "We're having sex on your piano... I think it shows."
pause
scene anim_jill_stand2b_ep12 with dissolve
ji "*{i}Moans{/i}*"
pause

scene ep12_jill_lewd23 with dissolve
ji "Sit down for me..."
scene ep12_jill_lewd24 with dissolve
mc "I love seeing you this confident in your own skin."
scene ep12_jill_lewd25 with dissolve
ji "What we are when we're together, is thanks to you."
scene ep12_jill_lewd26 with dissolve
mc "No, [jill]. I think we both bring the best out of one another."
scene ep12_jill_lewd27 with dissolve
ji "*{i}Moans{/i}*"
scene anim_jill_rev1_ep12 with dissolve
ji "Fuck... Oh, [mc_jill]..."
pause
scene anim_jill_rev2_ep12 with dissolve
mc "You're unbelievable... Hngn..."
pause

scene ep12_jill_lewd28 with dissolve
ji "Your cock feels amazing, [mc_jill]."
scene ep12_jill_lewd29 with dissolve
mc "Hey... Where are you going?"
scene ep12_jill_lewd30 with dissolve
$ renpy.pause()
scene ep12_jill_lewd31 with dissolve
ji "Let's go to my room."
scene ep12_jill_lewd30 with dissolve
mc "Naked?"
scene ep12_jill_lewd31 with dissolve
ji "Scared?"
scene ep12_jill_lewd30 with dissolve
mc "A little scared of what got into you, maybe."
scene ep12_jill_lewd33 with dissolve
ji "Don't be. I know what I'm doing."
scene ep12_jill_lewd32 with dissolve
mc "Clearly."
scene ep12_jill_lewd34 with dissolve
ji "Wait."
mc "Something the matter?"
scene ep12_jill_lewd35 with dissolve
ji "I need you to stay right here for a while."
scene ep12_jill_lewd36 with dissolve
mc "Whatever it is that you're doing... You're turning me on."
scene ep12_jill_lewd38 with dissolve
ji "*{i}Smack{/i}*"
scene ep12_jill_lewd37 with dissolve
ji "*{i}Smack{/i}*"
scene ep12_jill_lewd39 with dissolve
mc "Fuck... You've gotta be kidding me."
ji "*{i}Smack{/i}* Shh... Trust me."
scene ep12_jill_lewd40 with dissolve
ji "*{i}Smack{/i}*"
scene anim_jill_bj1_ep12 with dissolve
ji "*{i}Suck suck{/i}*"
mc "Oh, [jill]... That feels amazing."
pause
scene anim_jill_bj2_ep12 with dissolve
mc "I can't believe you're sucking my cock out here. You're wild... You know that?"
pause
scene ep12_jill_lewd41 with dissolve
mc "What? Are you leaving again? Why do you keep teasing me?"

scene ep12_jill_lewd42 with dissolve
mc "What's the belt for?"
scene ep12_jill_lewd43 with dissolve
ji "Come over here and find out."
scene ep12_jill_lewd44 with dissolve
$ renpy.pause()
scene ep12_jill_lewd45 with dissolve
ji "Fuck me, [mc_jill]..."
ji "Come and take me from behind."
scene ep12_jill_lewd46 with dissolve
mc "Wow... This is amazing..."
scene ep12_jill_lewd47 with dissolve
ji "Mmm... Put it in, [mc_jill]. Put it all in."
scene anim_jill_doggy1_ep12 with dissolve
ji "*{i}Moans{/i}* Yes! Fuck me!"
pause
scene anim_jill_doggy2_ep12 with dissolve
mc "Oh my God... Where did you learn how to do this? This is so good, [jill]."
pause
scene anim_jill_doggy1_ep12 with dissolve
ji "I'm glad I can surprise you."
mc "Your ass is so sexy... If I'm not careful, I will cum all over it in an instant."
ji "We don't want that to happen yet, do we?"
mc "No... Definitely not."
scene ep12_jill_lewd52 with dissolve
ji "Good... Because I have another surprise..."
ji "But I'm not sure if you're up for it."
ji "Would you like to have anal sex?"
scene ep12_jill_lewd53 with dissolve
mc "Anal sex? Are you sure?"
scene ep12_jill_lewd52 with dissolve
ji "I bought the lubrication for it. So, it's up to you. I feel ready to try it."
scene ep12_jill_lewd53 with dissolve
menu:
    "Have anal sex":
        $ ep12_jill_anal = True
        mc "If you're up for it, so am I."
        scene ep12_jill_lewd52 with dissolve
        ji "Ok... I'll get the lube."
    "Stick to vaginal":
        $ ep12_jill_anal = False
        mc "I appreciate it, but I honestly don't feel like doing that tonight."
        mc "Don't get me wrong, though... It's because you're so damned sexy that I want to keep fucking your pussy."
        scene ep12_jill_lewd52 with dissolve
        ji "That's fine by me. I just wanted to throw the idea out there."
        ji "I find it amusing that I managed to push your limit, too."
        scene ep12_jill_lewd53 with dissolve

if ep12_jill_anal:
    scene ep12_jill_lewd50a with dissolve
    mc "I'll start with a finger."
    ji "Ok."
    scene ep12_jill_lewd50b with dissolve
    mc "There..."
    ji "That was easy."
    scene ep12_jill_lewd50a with dissolve
    mc "Yeah, it was just my pinky. How about if I try two fingers?"
    ji "Yes, do two of them at once."
    scene ep12_jill_lewd50d with dissolve
    ji "Hngn..."
    mc "All good?"
    ji "It was a bit more challenging, but the lube definitely helps."
    scene ep12_jill_lewd50c with dissolve
    ji "Are you going to do three next?"
    mc "No, I was thinking to try with the tip."
    ji "Oh... Just the tip?"
    scene ep12_jill_lewd50e with dissolve
    mc "Yeah, we'll take it from there."
    scene ep12_jill_lewd50 with dissolve
    ji "Ahh..."
    mc "How is it?"
    ji "It's not as bad as I feared. Is it really in there?"
    mc "It is. Can I push it in some more?"
    ji "Yes, but go slow. Very slow."
    mc "Of course..."
    scene ep12_jill_lewd49 with dissolve
    ji "*{i}Moans{/i}* Ahhh..."
    mc "Still good?"
    ji "Mhm... But it's getting tight."
    mc "Yeah. It will get even tighter. Are you up for it?"
    ji "Yes. Do a bit more..."
    scene ep12_jill_lewd51 with dissolve
    ji "Hngn... Fuck!"
    scene ep12_jill_lewd48 with dissolve
    mc "Am I too deep?"
    ji "No. How much is left of you?"
    mc "Um... Maybe half."
    ji "Half!? Wow..."
    mc "If I start fucking you, it might feel easier for you to take it all."
    ji "Ok... Fuck me slowly, [mc_jill]."
    scene ep12_jill_lewd48b with dissolve
    ji "*{i}Moans{/i}*"
    scene ep12_jill_lewd48 with dissolve
    ji "Yes..."
    scene ep12_jill_lewd48b with dissolve
    $ renpy.pause()
    scene ep12_jill_lewd48 with dissolve
    mc "You're doing good..."
    scene ep12_jill_lewd48c with dissolve
    ji "I think you can go faster."
    scene ep12_jill_lewd48 with dissolve
    mc "Are you sure?"
    scene ep12_jill_lewd48c with dissolve
    ji "Yes. Try it. I think I'm ready."

    scene anim_jill_doggy_anal1_ep12 with dissolve
    ji "Hngn... Ahhh..."
    mc "Wow, that is tight. It's so good for me."
    ji "Is that still half?"
    mc "It's a bit more than half."
    ji "Don't go deeper than that."
    mc "I won't."
    pause
    scene anim_jill_doggy2_ep12 with dissolve
    mc "How about the speed? Am I going too fast?"
    ji "Hngn... No. It's actually starting to feel good."
    mc "That's great... [jill], I gotta say, you feel incredible."
    pause
    scene ep12_jill_lewd51 with dissolve
    ji "I hope you enjoy it. It's all for you."

$ tmpInt = 0
$ tmpBool = False
label ep12_jill_lewd_loop_label:
if ep12_jill_anal:
    menu:
        "Doggystyle":
            jump ep12_jill_lewd_doggy_label
        "Doggystyle (Anal)":
            jump ep12_jill_lewd_doggy_anal_label
        "Blowjob":
            jump ep12_jill_lewd_bj_label
        "Missionary":
            jump ep12_jill_lewd_miss_label
        "Cowgirl":
            jump ep12_jill_lewd_ride_label
        "Cowgirl (Anal)":
            jump ep12_jill_lewd_ride_anal_label
        "Reverse cowgirl (Anal)":
            jump ep12_jill_lewd_rev_anal_label
        "Standing":
            jump ep12_jill_lewd_stand_label
        "Cum" if tmpInt > 2:
            mc "[jill]... I'm gonna cum."
            menu:
                "Creampie":
                    jump ep12_jill_lewd_cum_creampie_label
                "Creampie (Anal)":
                    jump ep12_jill_lewd_cum_creampie_anal_label
                "In mouth":
                    jump ep12_jill_lewd_cum_mouth_label
                "On ass":
                    jump ep12_jill_lewd_cum_ass_label
                "On ass (Anal)":
                    jump ep12_jill_lewd_cum_ass_anal_label
else:
    menu:
        "Doggystyle":
            jump ep12_jill_lewd_doggy_label
        "Blowjob":
            jump ep12_jill_lewd_bj_label
        "Missionary":
            jump ep12_jill_lewd_miss_label
        "Cowgirl":
            jump ep12_jill_lewd_ride_label
        "Standing":
            jump ep12_jill_lewd_stand_label
        "Cum" if tmpInt > 2:
            mc "[jill]... I'm gonna cum."
            menu:
                "Creampie":
                    jump ep12_jill_lewd_cum_creampie_label
                "In mouth":
                    jump ep12_jill_lewd_cum_mouth_label
                "On ass":
                    jump ep12_jill_lewd_cum_ass_label

label ep12_jill_lewd_doggy_label:
$ tmpInt += 1
scene anim_jill_doggy1_ep12 with dissolve
ji "*{i}Moans{/i}* Fuck me, [mc_jill]!"
pause
scene anim_jill_doggy2_ep12 with dissolve
ji "Hngn..."
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_doggy_anal_label:
$ tmpInt += 1
scene anim_jill_doggy_anal1_ep12 with dissolve
ji "Ahhh!!!"
mc "Do you want me to slow down?"
ji "No. It comes and goes. It's a mix of pain and enjoyment. Hngn."
pause
scene anim_jill_doggy2_ep12 with dissolve
ji "Believe me, I'll stop you if need be."
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_bj_label:
$ tmpInt += 1
scene anim_jill_bj3_ep12 with dissolve
ji "*{i}Suck suck glug glug{/i}*"
mc "Damn... You're really going for it tonight."
pause
scene anim_jill_bj4_ep12 with dissolve
mc "Keep going... Suck it."
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_miss_label:
$ tmpInt += 1
scene anim_jill_miss1_ep12 with dissolve
ji "Fuck me, [mc_jill]... Fuck me!"
mc "Damn, it's so sexy hearing you say it like that."
pause
scene anim_jill_miss2_ep12 with dissolve
ji "*{i}Moans{/i}* You're so sexy too when you fuck me like this."
mc "Aha? You like when we do it like this?"
ji "Mmm... I love it."
pause
scene anim_jill_miss3_ep12 with dissolve
ji "It feels so good, [mc_jill]."
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_ride_label:
$ tmpInt += 1
scene anim_jill_ride1_ep12 with dissolve
mc "This belt is really coming in handy..."
ji "Pull me in closer to you... Harder."
mc "I'm all the way in, baby."
pause
scene anim_jill_ride2_ep12 with dissolve
ji "*{i}Moans{/i}* I love your cock."
mc "And I love your wet and tight pussy, [jill]."
pause
scene anim_jill_ride3_ep12 with dissolve
mc "Ride me, [jill]."
ji "I want to ride you until you cum..."
pause
if not tmpBool:
    ji "[mc_jill]... In fact, I... I think... I think I'm gonna..."
    jump ep12_jill_lewd_cum_label
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_ride_anal_label:
$ tmpInt += 1
scene anim_jill_ride_anal1_ep12 with dissolve
mc "I can't believe I'm fucking you in the ass now... Is this a dream?"
ji "Haha... It's not a dream. It's happening, [mc_jill]."
pause
scene anim_jill_ride_anal2_ep12 with dissolve
mc "You're amazing. Do you know that?"
ji "Mmm... We should have tried this earlier. It's not bad at all."
pause
scene anim_jill_ride_anal3_ep12 with dissolve
mc "Maybe in time you'll love it even more."
ji "Hngn... I can see that happening. *{i}Moans{/i}*"
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_rev_anal_label:
$ tmpInt += 1
scene anim_jill_rev_anal1_ep12 with dissolve
ji "Does this feel good for you, baby?"
mc "So good. You have no idea..."
pause
scene anim_jill_rev_anal2_ep12 with dissolve
ji "Let me know if I'm doing it wrong."
mc "Wrong? You've done everything right tonight, [jill]."
mc "You're even taking the whole thing, right now."
ji "*{i}Gasps{/i}* I am? I can't even tell."
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_stand_label:
$ tmpInt += 1
scene anim_jill_stand1_ep12 with dissolve
ji "*{i}Moans{/i}* I want you inside me..."
mc "I'm doing my best here."
ji "More, [mc_jill]... More. Push your pelvis hard against mine."
ji "I want your cock to penetrate me deeply!"
pause
scene anim_jill_stand2_ep12 with dissolve
mc "If I could fuck you all night, I would. But I gotta warn you... I'm getting close here..."
pause
scene anim_jill_stand3_ep12 with dissolve
ji "Are you gonna cum for me now?"
pause
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_cum_label:
$ tmpBool = True
scene ep12_jill_lewd72 with vpunch
$ renpy.pause(0.5)
scene ep12_jill_lewd72 with vpunch
$ renpy.pause(0.5)
scene ep12_jill_lewd72 with vpunch
ji "*{i}Moans{/i}* Ahh!!! I'm cumming!"
scene ep12_jill_lewd72 with vpunch
$ renpy.pause(0.5)
scene ep12_jill_lewd72 with vpunch
ji "OH!!! FUCK!!!"
scene ep12_jill_lewd73 with dissolve
ji "Oh my God... I'm sorry. I couldn't hold it back any longer."
scene ep12_jill_lewd74 with dissolve
mc "Never feel sorry for that. Making you cum makes me feel good about myself."
mc "And I love watching you scream with pleasure."
jump ep12_jill_lewd_loop_label

label ep12_jill_lewd_cum_creampie_label:
scene anim_jill_ride3_ep12 with dissolve
ji "Cum inside me, [mc_jill]... Cum for me. Cum!!!"
pause
scene ep12_jill_lewd62 at vpunch, cum1
$ renpy.pause(0.5)
scene ep12_jill_lewd62 at vpunch, cum1
$ renpy.pause(0.5)
scene ep12_jill_lewd62 at vpunch, cum1
mc "Ahhh!!!"
scene ep12_jill_lewd72 at vpunch, cum1
ji "Hngn... FUCK! *{i}Moans{/i}* I'm cumming too!"
scene ep12_jill_lewd63 with dissolve
$ renpy.pause()
scene ep12_jill_lewd64 with dissolve
$ renpy.pause()
jump ep12_jill_lewd_after_label

label ep12_jill_lewd_cum_creampie_anal_label:
scene anim_jill_ride_anal_cum_ep12 with vpunch
mc "Ahh! I'm cumming!!!"
pause
scene ep12_jill_lewd65 with dissolve
mc "Oh my God... Oh my God..."
ji "Hihi... I could tell you loved when I kept going like that."
mc "Yeah... That was an amazing orgasm."
jump ep12_jill_lewd_after_label

label ep12_jill_lewd_cum_mouth_label:
scene anim_jill_bj4_ep12 with dissolve
ji "*{i}Suck suck suck{/i}*"
mc "Here I cum..."
scene ep12_jill_lewd66 at vpunch, cum1
$ renpy.pause(0.5)
scene ep12_jill_lewd66 at vpunch, cum1
ji "*{i}Glug glug{/i}*"
scene ep12_jill_lewd66 at vpunch, cum1
mc "Ahh..."
scene ep12_jill_lewd67 with dissolve
$ renpy.pause()
scene ep12_jill_lewd68 with dissolve
ji "*{i}Gulp{/i}*"
scene ep12_jill_lewd69 with dissolve
mc "Wow... You swallowed it too."
scene ep12_jill_lewd69b with dissolve
mc "You're such a sexy girlfriend..."
jump ep12_jill_lewd_after_label

label ep12_jill_lewd_cum_ass_label:
scene anim_jill_doggy1_ep12 with dissolve
mc "I wanna cum all over your ass."
ji "Cum on it, [mc_jill]! Cum on my ass!!!"
scene ep12_jill_lewd70 at vpunch, cum2
$ renpy.pause(0.5)
scene ep12_jill_lewd70 at vpunch, cum2
$ renpy.pause(0.5)
scene ep12_jill_lewd70 at vpunch, cum2
mc "Ahh!!!"
scene ep12_jill_lewd71 with dissolve
$ renpy.pause()
jump ep12_jill_lewd_after_label

label ep12_jill_lewd_cum_ass_anal_label:
scene anim_jill_doggy_anal1_ep12 with dissolve
mc "I wanna cum all over your ass."
ji "Cum on it, [mc_jill]! Cum on my ass!!!"
scene ep12_jill_lewd70 at vpunch, cum2
$ renpy.pause(0.5)
scene ep12_jill_lewd70 at vpunch, cum2
$ renpy.pause(0.5)
scene ep12_jill_lewd70 at vpunch, cum2
mc "Ahh!!!"
scene ep12_jill_lewd71 with dissolve
$ renpy.pause()
jump ep12_jill_lewd_after_label

label ep12_jill_lewd_after_label:
scene ep12_jill_lewd54 with dissolve
mc "You're amazing..."
scene ep12_jill_lewd55 with dissolve
ji "Did you enjoy it?"
scene ep12_jill_lewd54 with dissolve
mc "I loved it. You were so sexy and brave."
mc "You took control and looked comfortable doing it."
scene ep12_jill_lewd55 with dissolve
ji "I felt comfortable, too."
scene ep12_jill_lewd57 with dissolve
mc "You never answered my question before... Where did you learn how to do that?"
scene ep12_jill_lewd56 with dissolve
ji "Which thing?"
scene ep12_jill_lewd57 with dissolve
mc "Everything!"
scene ep12_jill_lewd56 with dissolve
ji "Haha! I may have gotten some pointers."
scene ep12_jill_lewd57 with dissolve
mc "Pointers? From who? Should I be jealous?"
scene ep12_jill_lewd58 with dissolve
ji "Oh! No! From Sage."
scene ep12_jill_lewd57 with dissolve
mc "What? Sage taught you that?"
mc "What would you even-? Where did you-? What?"
scene ep12_jill_lewd58 with dissolve
ji "Hahaha! You don't need to know everything."
scene ep12_jill_lewd57 with dissolve
mc "Do I have to thank her now?"
scene ep12_jill_lewd56 with dissolve
ji "Haha, no. But I will."
ji "It wasn't all her ideas, by the way. The belt was my idea."
scene ep12_jill_lewd57 with dissolve
mc "That was a nice touch for sure."
scene ep12_jill_lewd59 with dissolve
ji "So, tell me..."
ji "Did you decide on a New Year's resolution?"
if ep12_jill_love:
    scene ep12_jill_lewd61 with dissolve
    mc "Hm... How about this one?"
    mc "I promise to love you daily for every day next year."
    scene ep12_jill_lewd59 with dissolve
    ji "And to take more pictures?"
    scene ep12_jill_lewd61 with dissolve
    mc "Hm... The best I can do is love you daily."
else:
    scene ep12_jill_lewd61 with dissolve
    mc "I guess I'll try to take more pictures of us."
    scene ep12_jill_lewd59 with dissolve
    ji "And what about the monkey face? Will you stop doing it?"
    scene ep12_jill_lewd61 with dissolve
    mc "No, I can't promise you that."
scene ep12_jill_lewd60 with dissolve
ji "Hahaha!"
$ renpy.end_replay()
$ persistent.ep12_lewd_jill = True
$ calcScenes()
show screen new_phone_screen
$ new_bio("Jill", "Jill and I had sex in the preps' mansion after the New Year's Eve party.")
$ mphone_stats_add_girl_s3("jill","You had sex with Jill in the preps' mansion after the New Year's Eve party in episode 12.")
if wt_ep9_branch_numbers > 1:
   
   if "Sally" in wt_ep12_midnight_kiss:
       jump ep12_sally_lewd_label
   if "Elena" in wt_ep12_midnight_kiss:
       jump ep12_elena_lewd2_label
jump ep12_evaluation_label

label ep12_np2_kp_label:
if ep11_kp_choice == "CHICK":
    scene ep12_np2_kp1 with dissolve
    mc "Happy end of the year to you."
    scene ep12_np2_kp2 with dissolve
    ky "Happy whatever, [name]."
    scene ep12_np2_kp3 with dissolve
    py "Thanks for not making a fuss about tonight."
    scene ep12_np2_kp1 with dissolve
    mc "You're welcome."
    scene ep12_np2_kp4 with dissolve
    py "*{i}Whispers{/i}* Come on. Do it."
    scene ep12_np2_kp5 with dissolve
    ky "[name]..."
    scene ep12_np2_kp6 with dissolve
    mc "Yeah?"
    scene ep12_np2_kp5 with dissolve
    ky "I'm sorry for blaming you for what happened to my sister."
    ky "I know that you had nothing to do with it."
    scene ep12_np2_kp7 with dissolve
    ky "And I know that just because the rest of your fratmates might have done those things..."
    ky "It doesn't mean that you have."
    scene ep12_np2_kp5 with dissolve
    ky "It was unfair to treat you with the same disgust as I have for your brothers."
    ky "And for that I apologize."
    scene ep12_np2_kp8 with dissolve
    mc "Apology accepted."
    mc "And I'm sorry that they did that to your sister. And for all the other crap they put you through."
    scene ep12_np2_kp6 with dissolve
    mc "They might see it differently from you, and I know they look at that as harmless pranks..."
    mc "...but if it ended up hurting you and your friends..."
    mc "The pranks weren't harmless."
    scene ep12_np2_kp8 with dissolve
    mc "I'll do my best during my time in the frat to help out in those situations."
    scene ep12_np2_kp9 with dissolve
    ky "You will?"
    scene ep12_np2_kp8 with dissolve
    mc "I never participated in the Walk of Shame. I don't see the point of teasing a girl who spent the night with a brother."
    mc "They should be getting a high-five."
    scene ep12_np2_kp9 with dissolve
    ky "Tsk. Don't start with that now."
    scene ep12_np2_kp10 with dissolve
    mc "We're cool, Kylie."
    mc "You too, Penny."
    scene ep12_np2_kp4 with dissolve
    py "Aren't you happy you did that?"
    $ new_bio("Kylie", "Kylie apologized for blaming me for what happened to her sister.")
else:
    if ep11_kp_choice == "DIK":
        scene ep12_np2_kp11 with dissolve
        $ renpy.pause()
        scene ep12_np2_kp12 with dissolve
        $ renpy.pause()
        scene ep12_np2_kp16 with dissolve
        $ renpy.pause()
        scene ep12_np2_kp13 with dissolve
        ky "FYI, you're not kicking us out of this party."
        scene ep12_np2_kp14 with dissolve
        menu:
            "Fuck off \n{size=-4}[m_c1][mod_choices[1]]":
                $ dk(1)
                mc "FYI, fuck off."
            "Alright":
                mc "Alright."
        scene ep12_np2_kp15 with dissolve
        ky "*{i}Snorts{/i}*"
    else:
        scene ep12_np2_kp11 with dissolve
        $ renpy.pause()
        scene ep12_np2_kp13 with dissolve
        ky "FYI, you're not kicking us out of this party."
        scene ep12_np2_kp14 with dissolve
        mc "Aha, so that's what they did to you."
        scene ep12_np2_kp13 with dissolve
        ky "Don't act like you didn't know."
        scene ep12_np2_kp14 with dissolve
        mc "The DIKs aren't a hivemind. We each have free will."
        scene ep12_np2_kp15 with dissolve
        ky "*{i}Snorts{/i}*"

$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_ht_label:
scene ep12_np2_ht1 with dissolve
$ renpy.pause()
scene ep12_np2_ht3 with dissolve
tm "Happy new one."
scene ep12_np2_ht2 with dissolve
he "One second."
scene ep12_np2_ht9 with dissolve
he "Happy almost New Year."
he "How's your party?"
scene ep12_np2_ht4 with dissolve
tm "I bet it's better than yours."
scene ep12_np2_ht9 with dissolve
he "What makes you say that?"
scene ep12_np2_ht4 with dissolve
tm "For one, people on our end of the party know how to dress."
scene ep12_np2_ht10 with dissolve
he "Don't you think the girls are pretty enough on our side?"
scene ep12_np2_ht15 with dissolve
tm "I was talking about the guys. Somehow, the jocks forgot one of the most basic human abilities."
he "Either that or they can't afford shirts."
scene ep12_np2_ht5 with dissolve
tm "Hahaha!"
scene ep12_np2_ht11 with dissolve
he "How have you been?"
scene ep12_np2_ht6 with dissolve
tm "You know...?"
scene ep12_np2_ht13 with dissolve
he "I don't. I heard you had a falling out, but that's about it."
scene ep12_np2_ht6 with dissolve
tm "These last couple of months have been shit."
scene ep12_np2_ht12 with dissolve
$ renpy.pause()
scene ep12_np2_ht6 with dissolve
tm "And you?"
scene ep12_np2_ht13 with dissolve
he "I can't say they have been the best months of my life."
he "But they helped me get some perspective."
scene ep12_np2_ht7 with dissolve
tm "How's that?"
scene ep12_np2_ht13 with dissolve
he "I think I know where we went wrong."
scene ep12_np2_ht14 with dissolve
$ renpy.pause()
scene ep12_np2_ht4 with dissolve
tm "Are you gonna leave me hanging?"
scene ep12_np2_ht10 with dissolve
he "Do you want to know?"
scene ep12_np2_ht6 with dissolve
tm "I guess it was my fault somehow."
scene ep12_np2_ht10 with dissolve
he "Don't say you consider yourself the innocent victim."
scene ep12_np2_ht7 with dissolve
tm "I thought you were cool about things you weren't cool about."
scene ep12_np2_ht13 with dissolve
he "It's called having feelings for someone. And the problem is that a relationship only works if both have them."
scene ep12_np2_ht7 with dissolve
tm "You don't think I had feelings for you? Do you know how hard I punched Nick when I found out what he did?"
scene ep12_np2_ht10 with dissolve
he "Those aren't the feelings I'm talking about."
scene ep12_np2_ht8 with dissolve
tm "*{i}Sigh{/i}*"
scene ep12_np2_ht10 with dissolve
he "You know I'm right."
scene ep12_np2_ht6 with dissolve
tm "And you know how I'm like. I'm not that kind of guy."
scene ep12_np2_ht13 with dissolve
he "I know. And I'm not saying you have to be it all the time."
he "But if you, once in a while, had shown me the same Tommy I fell in love with..."
he "That's all it would have taken."
scene ep12_np2_ht6 with dissolve
tm "I don't think that's all you want, though."
tm "You want me to change into someone I'm not."
scene ep12_np2_ht10 with dissolve
he "That's not true. You might be projecting."
scene ep12_np2_ht7 with dissolve
tm "Hell no. There's nothing wrong with you. Not a damned thing."
scene ep12_np2_ht12 with dissolve
$ renpy.pause()
$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep12_np2_sally_label:
scene ep12_np2_sally1 with dissolve
sy "Hey!!! Why aren't you dancing?"
scene ep12_np2_sally2 with dissolve
mc "I leave that to the pros and do what I'm good at."
scene ep12_np2_sally1 with dissolve
sy "Is that drinking or ogling girls?"
scene ep12_np2_sally2 with dissolve
mc "Both."
scene ep12_np2_sally1 with dissolve
sy "Pff!"
scene ep12_np2_sally3 with dissolve
sy "I could use a break. It's hot in here."
sy "You'd think the ventilation would be good in a gymnasium."
scene ep12_np2_sally4 with dissolve
mc "You'd think? It often smells of sweat and rubber."
scene ep12_np2_sally3 with dissolve
sy "Ah... I skipped gym a lot in school. What do I know?"
scene ep12_np2_sally4 with dissolve
mc "There's another balcony over there if you want to grab some air with me."
scene ep12_np2_sally5 with dissolve
sy "Lead the way!"
scene ep12_np2_sally6
hide screen dance_filter_screen
with dissolve
sy "I wanted to ask you something."
scene ep12_np2_sally7 with dissolve
mc "What's that?"
scene ep12_np2_sally6 with dissolve
sy "Next semester, do we have any joint classes?"
scene ep12_np2_sally7 with dissolve
mc "Aside from our chemistry class, you mean?"
scene ep12_np2_sally6 with dissolve
sy "Yeah. What are you taking?"
scene ep12_np2_sally8 with dissolve
mc "Intro to College Research, Mathematical Statistics, and Engineering Economics."
scene ep12_np2_sally9 with dissolve
sy "No way! Are you in Engineering Economics, too?"
scene ep12_np2_sally8 with dissolve
mc "It was my free pick; the rest was mandatory."
scene ep12_np2_sally9 with dissolve
sy "Then you'll have to stick with me for that one as well."
scene ep12_np2_sally10 with dissolve
mc "Haven't you had enough of me?"
scene ep12_np2_sally11 with dissolve
sy "Yeah, I'm merely using you to get a better grade."
scene ep12_np2_sally10 with dissolve
mc "Haha!"
scene ep12_np2_sally12 with dissolve
$ renpy.pause()
scene ep12_np2_sally13 with dissolve
sy "No, I'm not. But I could use the company. I don't know anyone else who signed up for it."
scene ep12_np2_sally14 with dissolve
mc "Neither do I. Don't worry, we'll knuckle it out together."
scene ep12_np2_sally15 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/fistbump.mp3"
scene ep12_np2_sally16 with dissolve
mc "Haha! You're getting good at that."
if ep11_sally_kiss:
    scene ep12_np2_sally17 with dissolve
    sy "Will you kiss someone at midnight?"
    scene ep12_np2_sally18 with dissolve
    mc "That came out of nowhere."
    scene ep12_np2_sally17 with dissolve
    sy "You think? Your friend told us we looked good together at dinner."
    sy "Are you telling me you didn't set him up to do that?"
    scene ep12_np2_sally18 with dissolve
    mc "I didn't set him up. I swear."
    scene ep12_np2_sally19 with dissolve
    sy "Oh... I thought you did."
    if branchZoey or wt_ep11_zoey_kiss_others:
        scene ep12_np2_sally20 with dissolve
        mc "Thanks for asking, but I'm gonna kiss my girlfriend Zoey."
        mc "We got together over the holidays."
        scene ep12_np2_sally21 with dissolve
        sy "I wasn't asking you to kiss me, if that's what you think."
        scene ep12_np2_sally20 with dissolve
        mc "Sure, you weren't."
        scene ep12_np2_sally21 with dissolve
        sy "I'm gonna get back to dancing. Forget I said anything."
        scene ep12_np2_sally20 with dissolve
        mc "Tear it up. I'll be watching."
    elif breakup or branchAlone:
        if breakup:
            scene ep12_np2_sally22 with dissolve
            mc "I don't think I should kiss anyone at midnight. I just had a breakup, and..."
            mc "I'm not sure it would be tasteful for me to do that."
            scene ep12_np2_sally23 with dissolve
            sy "If you're single, you're single."
            sy "If you change your mind on that... You know?"
        else:
            scene ep12_np2_sally22 with dissolve
            mc "I haven't made any plans for midnight yet, if that's what you're asking."
            scene ep12_np2_sally23 with dissolve
            sy "Good to know. Me neither."
        scene ep12_np2_sally22 with dissolve
        mc "Noted..."
        scene ep12_np2_sally24 with dissolve
        sy "..."
        scene ep12_np2_sally23 with dissolve
        sy "I'm gonna get back to dancing. Maybe I'll see you at midnight."
        scene ep12_np2_sally26 with dissolve
        $ renpy.pause()
    else:
        scene ep12_np2_sally20 with dissolve
        mc "I'm in a relationship... What we did at the panty party was wrong."
        scene ep12_np2_sally25 with dissolve
        sy "Oh, I see how it is... Yeah, you shouldn't have done that."
        scene ep12_np2_sally20 with dissolve
        mc "I know."
        scene ep12_np2_sally23 with dissolve
        sy "That's a shame. You're a good kisser."
        sy "If things change before midnight, haha..."
        scene ep12_np2_sally22 with dissolve
        mc "Noted..."
        scene ep12_np2_sally24 with dissolve
        sy "..."
        scene ep12_np2_sally23 with dissolve
        sy "I'm gonna get back to dancing. Maybe I'll see you at midnight."
        scene ep12_np2_sally26 with dissolve
        $ renpy.pause()
        $ event_list.append("sally_break")
$ task_list[11] = ""
$ updateTaskList()
jump endEvent

label ep12_sally_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep12_mc_slut = False
    play music "music/ep12/licensed_music/track204.mp3"
hide screen new_phone_screen
$ ep12_sally_lewd = True
if wt_ep9_branch_numbers == 1:
    scene ep12_sally_lewd1 with dissolve
    mc "Let's leave."
    scene ep12_sally_lewd2 with dissolve
    sy "Already? Can I say goodnight to a few people?"
    scene ep12_sally_lewd1 with dissolve
    mc "Do that and meet me outside. We're heading back to your dorm, yeah?"
    scene ep12_sally_lewd2 with dissolve
    sy "We are, I have the place to myself."
    scene ep12_sally_lewd3 with wipeleft
mc "Nice place."
scene ep12_sally_lewd4 with dissolve
sy "It's a dorm."
scene ep12_sally_lewd5 with dissolve
mc "Yeah, but it's got charm."
scene ep12_sally_lewd4 with dissolve
sy "It does?"
scene ep12_sally_lewd6 with dissolve
mc "Yeah. Do you still play with dolls?"
sy "They're not dolls; they are figurines. And I'll have you know that they are collector's items!"
scene ep12_sally_lewd7 with dissolve
mc "I didn't mean it in a bad way. I didn't know you were into this."
scene ep12_sally_lewd8 with dissolve
sy "They are from manga I enjoy."
scene ep12_sally_lewd9 with dissolve
mc "I know nothing about that, but it's cool that you have a hobby."
scene ep12_sally_lewd10 with dissolve
sy "I have plenty of hobbies."
scene ep12_sally_lewd12 with dissolve
mc "What's that staff for?"
sy "It's my witch's staff for my DnG character. I use it when we dress as game characters or when we LARP."
scene ep12_sally_lewd7 with dissolve
mc "Larp?"
scene ep12_sally_lewd8 with dissolve
sy "LARP! Live action role-playing."
scene ep12_sally_lewd7 with dissolve
mc "Role-playing? Is that a sex thing?"
scene ep12_sally_lewd8 with dissolve
sy "You don't know much about anything, do you?"
scene ep12_sally_lewd9 with dissolve
mc "Not about this."
scene ep12_sally_lewd10 with dissolve
sy "*{i}Sigh{/i}* That's fine. Maybe I'll teach you someday."
scene ep12_sally_lewd13 with dissolve
mc "Cool keyboard. Do you play?"
sy "It's my roomie's."
scene ep12_sally_lewd9 with dissolve
mc "Who's your roomie anyway?"
scene ep12_sally_lewd10 with dissolve
sy "Wilma Gilroy. I don't think you know her."
sy "She's not big on parties or people. She's spending New Year's back home with her parents."
sy "The place is all ours."
scene ep12_sally_lewd11 with dissolve
sy "Are you done inspecting my dorm? I'd like to do what we came here for."
scene ep12_sally_lewd9 with dissolve
mc "Yeah, yeah. I'm just making small talk."
scene ep12_sally_lewd11 with dissolve
sy "There's no need for small talk. You brought a condom, right?"
scene ep12_sally_lewd14 with dissolve
$ renpy.pause()
scene ep12_sally_lewd15 with dissolve
mc "I have a strong pull-out game."
scene ep12_sally_lewd16 with dissolve
sy "I'm not making any babies with you, [name]."
scene ep12_sally_lewd17 with dissolve
mc "Don't you have any protection?"
scene ep12_sally_lewd16 with dissolve
sy "I have a character sheet with a protection spell. But I doubt it will be efficient enough to ward off your seed."
scene ep12_sally_lewd18 with dissolve
mc "I'll head back home and get a condom. I'm sure I can find one somewhere."
scene ep12_sally_lewd19 with dissolve
sy "I'm fucking with you. Don't you think I have protection?"
sy "Guys are useless with condoms."
scene ep12_sally_lewd18 with dissolve
mc "You like giving me a hard time, don't you?"
scene ep12_sally_lewd19 with dissolve
sy "I wanted to see how much you wanted it."
if ep12_mc_slut:
    scene ep12_sally_lewd20 with dissolve
    sy "But... You don't have any STDs, do you?"
    scene ep12_sally_lewd21 with dissolve
    mc "No. Why would you even ask that?"
    scene ep12_sally_lewd20 with dissolve
    sy "Why do you think? With that many girls under your belt, I wouldn't be surprised."
    scene ep12_sally_lewd21 with dissolve
    mc "I think I'm clean."
    scene ep12_sally_lewd22 with dissolve
    sy "He thinks... Ugh..."
    sy "The odds of not getting STDs with him would be like rolling a natural 20."
    scene ep12_sally_lewd23 with dissolve
    mc "Whatever that means... All I can tell you is that my cock is smooth and clean."
    scene ep12_sally_lewd22 with dissolve
    sy "Dammit, Sally. Stop being rational. You're drunk. Worry about that tomorrow."
scene ep12_sally_lewd24 with dissolve
$ renpy.pause()
scene ep12_sally_lewd25 with dissolve
$ renpy.pause()
scene ep12_sally_lewd26 with dissolve
mc "You have nice tits."
sy "Stop it. They're too small."
mc "No, they're not. They're sexy."
scene ep12_sally_lewd27 with dissolve
sy "You're just horny."
scene ep12_sally_lewd28 with dissolve
mc "Men like boobs of all sizes, Sally. And if I'm horny, it's because you turned me on."
sy "That's clear to see."
scene ep12_sally_lewd29 with dissolve
sy "Should I be worried about your size?"
mc "Have you had anything like it before?"
scene ep12_sally_lewd30 with dissolve
sy "No. Your cock has the girth of my arm, and I wouldn't put that inside me."
scene ep12_sally_lewd31 with dissolve
mc "You don't want it then?"
scene ep12_sally_lewd32 with dissolve
sy "I do, but you're gonna have to act like it's my first time."
sy "It's hot, but it looks like it will hurt."
scene ep12_sally_lewd33 with dissolve
mc "It won't hurt. We just need to get you up and going before you take it."
scene ep12_sally_lewd34 with dissolve
sy "Yeah? Let's try."
scene ep12_sally_lewd35 with dissolve
sy "*{i}Spits{/i}*"
scene ep12_sally_lewd36 with dissolve
sy "Do you want me to suck your cock?"
scene ep12_sally_lewd37 with dissolve
mc "I won't say no to that."
scene ep12_sally_lewd38 with dissolve
sy "I'll do it, but only if you eat me."
scene ep12_sally_lewd37 with dissolve
mc "Best deal ever. I want to eat you."
scene ep12_sally_lewd39 with dissolve
sy "You do?"
scene ep12_sally_lewd37 with dissolve
mc "Yeah. I want to taste you."
scene ep12_sally_lewd38 with dissolve
sy "I thought you would protest. That's a pleasant surprise."
scene ep12_sally_lewd40 with dissolve
sy "Maybe I'll put in some extra effort into this then."
scene ep12_sally_lewd41 with dissolve
$ renpy.pause()
scene ep12_sally_lewd42 with dissolve
$ renpy.pause()
scene anim_sally_bj1_ep12 with dissolve
sy "*{i}Suck suck{/i}*"
pause
scene anim_sally_bj2_ep12 with dissolve
mc "That's some extra effort, alright. I love how your lips feel around my dick."
pause
$ tmpInt = 0
label ep12_sally_lewd_loop1_label:
menu:
    "Eat her pussy":
        $ tmpInt += 1
        scene ep12_sally_lewd43 with dissolve
        mc "Let me eat you..."
        scene ep12_sally_lewd44 with dissolve
        sy "Alright. Lie down."
        scene ep12_sally_lewd43 with dissolve
        mc "Me?"
        scene ep12_sally_lewd45 with dissolve
        sy "Yeah. If you're gonna do it, you're gonna do it my way."
        scene anim_sally_cunn1_ep12 with dissolve
        sy "Stiffen up your tongue. I want to grind on it."
        mc "*{i}Lick lick{/i}*"
        pause
        scene anim_sally_cunn2_ep12 with dissolve
        sy "*{i}Moans{/i}* Yes. That's it."
        pause
        jump ep12_sally_lewd_loop1_label
    "Eat her ass":
        $ tmpInt += 1
        scene ep12_sally_lewd46 with dissolve
        mc "Bend over like that..."
        scene ep12_sally_lewd47 with dissolve
        sy "Are you going to eat my ass?"
        scene ep12_sally_lewd48 with dissolve
        mc "Yeah."
        sy "I wasn't aware you were into that. This is getting better by the minute."
        scene anim_sally_ass1_ep12 with dissolve
        mc "*{i}Lick lick{/i}*"
        sy "Hngn..."
        pause
        jump ep12_sally_lewd_loop1_label
    "Blowjob":
        scene anim_sally_bj1_ep12 with dissolve
        sy "*{i}Suck suck{/i}*"
        pause
        scene anim_sally_bj2_ep12 with dissolve
        sy "*{i}Mmmpfh{/i}*"
        pause
        jump ep12_sally_lewd_loop1_label
    "Fuck her face":
        scene ep12_sally_lewd49 with dissolve
        sy "You can fuck my face if you want."
        scene ep12_sally_lewd50 with dissolve
        mc "Do you think you can take it?"
        scene ep12_sally_lewd49 with dissolve
        sy "I'll let you know if I can't."
        scene anim_sally_bj3_ep12 with dissolve
        sy "*{i}Suck glug glug{/i}*"
        mc "Fuck! That's so good."
        pause
        scene anim_sally_bj4_ep12 with dissolve
        sy "*{i}Glug glug{/i}*"
        mc "Yeah, you sure can take it. It's amazing..."
        pause
        jump ep12_sally_lewd_loop1_label
    "Continue" if tmpInt > 0:
        $ renpy.pause(0.5)

scene ep12_sally_lewd51 with dissolve
sy "Enough with this teasing. I'm ready to try it for real."
scene ep12_sally_lewd52 with dissolve
mc "I'll be gentle."
scene ep12_sally_lewd53 with dissolve
sy "I sure hope it doesn't hurt because I'm ready to pounce on it."
scene ep12_sally_lewd54 with dissolve
sy "Ahh..."
scene ep12_sally_lewd55 with dissolve
sy "*{i}Moans{/i}* Slowly..."
scene ep12_sally_lewd56 with dissolve
sy "Hngn! Wow... I did it."
mc "Are you good?"
sy "Yeah. Haha! It looks more intimidating than it feels."
scene ep12_sally_lewd57 with dissolve
mc "You think it feels small inside you?"
scene ep12_sally_lewd58 with dissolve
sy "No. But I mean, it doesn't feel scary big."
sy "Hell, that's a good thing! I might even be able to take it up the ass."
scene ep12_sally_lewd57 with dissolve
mc "Whoa! Really?"
scene ep12_sally_lewd58 with dissolve
sy "Come on. Fuck me already. If you won't, I'm gonna cuff you and grind you down to a knob."
scene anim_sally_miss1_ep12 with dissolve
sy "*{i}Moans{/i}* Yes! There we go. Fuck!"
mc "Too fast?"
sy "Not at all. You don't have to ask if it's ok anymore."
mc "Just checking. You told me to be careful earlier."
pause
scene anim_sally_miss2_ep12 with dissolve
sy "Don't worry. It hurts in a good way. *{i}Moans{/i}* Fuck!!!"
mc "You're amazingly tight, Sally."
sy "*{i}Moans{/i}* Have you had anyone as tight as me before?"
mc "No. I'm positive."
sy "We're both breaking new ground tonight, then."
pause

$ tmpInt = 0
$ tmpBool = False
$ tmpBool2 = False
label ep12_sally_lewd_loop_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_sally_miss1_ep12 with dissolve
        sy "*{i}Moans{/i}* Fuck me, [name]! HARDER!"
        pause
        scene anim_sally_miss2_ep12 with dissolve
        sy "YES! YES!!!"
        pause
        jump ep12_sally_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_sally_ride1_ep12 with dissolve
        mc "It's so tight. Damn..."
        sy "*{i}Moans{/i}* Fuck! Why does it feel so good when it's way past the G-spot?"
        mc "I'm glad you like it."
        sy "Don't dare cum yet."
        pause
        scene anim_sally_ride2_ep12 with dissolve
        sy "Hngn! Yes! Right there. Fuck, fuck, fuck..."
        pause
        if not tmpBool:
            $ tmpBool = True
            scene ep12_sally_lewd68 with vpunch
            sy "AHHH!!!"
            scene ep12_sally_lewd69 with vpunch
            sy "HOLY!!!"
            scene ep12_sally_lewd70 with dissolve
            sy "*{i}Sigh{/i}*"
            mc "But it's ok for you to cum, huh?"
            scene ep12_sally_lewd71 with dissolve
            sy "Sex doesn't end when I cum; that's why it's not double standards."
        jump ep12_sally_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_sally_doggy1_ep12 with dissolve
        sy "Pound me, [name]!"
        mc "You're into it now. Back when we started, you wanted to be treated like a virgin."
        sy "Shut up and fuck me!"
        pause
        scene anim_sally_doggy2_ep12 with dissolve
        mc "Your ass is so fucking nice. I don't ever want this to end."
        sy "Whatever keeps you going. Don't stop!"
        sy "Hngn... It's been too long since last time. I don't remember sex being this good. *{i}Moans{/i}*"
        pause
        jump ep12_sally_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_sally_stand1_ep12 with dissolve
        sy "Ahh!! *{i}Moans{/i}*"
        sy "Give it to me, [name]. Give it!"
        pause
        scene anim_sally_stand2_ep12 with dissolve
        mc "You're so slutty. I love it."
        if ep12_mc_slut:
            sy "Peas in a pod."
        pause
        jump ep12_sally_lewd_loop_label
    "Missionary (Anal)":
        $ tmpInt += 1
        if not tmpBool2:
            $ tmpBool2 = True
            scene ep12_sally_lewd76 with dissolve
            sy "Be careful when you put it in."
            scene ep12_sally_lewd75 with dissolve
            mc "Did you apply enough lube?"
            sy "Yeah, but that doesn't mean it will be easy. If I say stop, you stop!"
            scene ep12_sally_lewd74 with dissolve
            sy "Just the tip..."
            sy "*{i}Moans{/i}* That feels good... Do some more."
            scene ep12_sally_lewd73 with dissolve
            sy "Ahhh!!!"
            mc "Too much?"
            sy "Did I say stop? More."
            scene ep12_sally_lewd72 with dissolve
            sy "FUCK!!!"
            mc "It's in there now."
            sy "Hngn! Take it easy! Don't fuck me too hard."
        scene anim_sally_miss1_anal_ep12 with dissolve
        sy "Ahh! Yes... Like that!"
        mc "All good?"
        sy "*{i}Moans{/i}* Yeah. Perfect pace and depth."
        mc "It's good for me too, by the way."
        sy "I'm sorry I didn't ask, but I'm busy not dying while getting impaled over here."
        pause
        scene anim_sally_miss2_anal_ep12 with dissolve
        mc "Damn, you're even tighter in your ass."
        sy "How does that even surprise you?"
        mc "Well, your pussy was already tight enough for me. And I didn't think it was possible for this to squeeze my cock even harder."
        pause
        jump ep12_sally_lewd_loop_label
    "Doggystyle (Anal)" if tmpBool2:
        $ tmpInt += 1
        scene anim_sally_doggy_anal1_ep12 with dissolve
        sy "*{i}Moans{/i}* Yes! Pound my ass, [name]!"
        pause
        scene anim_sally_doggy_anal2_ep12 with dissolve
        pause
        jump ep12_sally_lewd_loop_label
    "Reverse cowgirl (Anal)" if tmpBool2:
        $ tmpInt += 1
        scene anim_sally_rev_anal1_ep12 with dissolve
        sy "Fuck me, [name]!"
        mc "Take it."
        pause
        scene anim_sally_rev_anal2_ep12 with dissolve
        mc "Your ass slapping against my hip is such a sexy sight."
        sy "*{i}Moans{/i}*"
        pause
        jump ep12_sally_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna cum!"
        menu:
            "Creampie":
                scene anim_sally_stand2_ep12 with dissolve
                sy "Fill me with your cum. I want to feel it explode inside me."
                pause
                scene ep12_sally_lewd66 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sally_lewd66 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sally_lewd66 at vpunch, cum1
                mc "Ahh!!!"
                sy "*{i}Moans{/i}* AHHHH!!!"
                scene ep12_sally_lewd67 with dissolve
                sy "Oh my God... I fucking came too..."
            "Creampie (Anal)":
                scene anim_sally_rev_anal2_ep12 with dissolve
                sy "Fill me with your cum. I want to feel it explode inside me."
                pause
                scene ep12_sally_lewd59 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sally_lewd59 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_sally_lewd59 at vpunch, cum1
                mc "Ahh!!!"
                scene ep12_sally_lewd60 with dissolve
                mc "Amazing..."
                scene ep12_sally_lewd61 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_sally_bj4_ep12 with dissolve
                sy "*{i}Glug glug{/i}*"
                pause
                scene ep12_sally_lewd64 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_sally_lewd64 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_sally_lewd64 at vpunch, cum3
                mc "Ahhh!!!"
                scene ep12_sally_lewd65 with dissolve
                sy "Do I look good covered in your cum?"
                mc "Yes, you do. Fuck..."
            "On ass":
                scene anim_sally_doggy2_ep12 with dissolve
                sy "Cum for me, [name]. Spray it all over my ass!"
                pause
                scene ep12_sally_lewd62 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_sally_lewd62 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_sally_lewd62 at vpunch, cum3
                mc "Ahhh!!!"
                scene ep12_sally_lewd63 with dissolve
                sy "Mmm... Just like that... Yes."

scene ep12_sally_lewd77 with dissolve
mc "You did well."
scene ep12_sally_lewd78 with dissolve
sy "Well? I did amazing. You did well."
scene ep12_sally_lewd77 with dissolve
mc "Haha!"
scene ep12_sally_lewd78 with dissolve
sy "I'll probably hurt tomorrow, but I'm also likely to have a headache. So, it doesn't matter."
scene ep12_sally_lewd79 with dissolve
mc "Yeah. Tomorrow is already a wasted day."
scene ep12_sally_lewd78 with dissolve
sy "Technically, it's today."
scene ep12_sally_lewd80 with dissolve
mc "Do you want me to stay over?"
scene ep12_sally_lewd81 with dissolve
sy "Eh... I don't know. We might get company tomorrow. That would be awkward for me."
scene ep12_sally_lewd80 with dissolve
mc "And this bed is kind of small."
scene ep12_sally_lewd81 with dissolve
sy "And you're not sleeping in Wilma's bed."
scene ep12_sally_lewd82 with dissolve
mc "I'd better leave before I get too comfortable, then."
mc "But I gotta say, it's been nice. I never thought we'd end up having sex."
scene ep12_sally_lewd83 with dissolve
sy "You didn't?"
scene ep12_sally_lewd84 with dissolve
mc "No. Not with the way you've treated me in the past."
scene ep12_sally_lewd83 with dissolve
sy "Can we leave all that in the past?"
scene ep12_sally_lewd86 with dissolve
mc "All I'm saying is I'm happy we did this tonight."
mc "I think you're pretty cool, Sally."
scene ep12_sally_lewd83 with dissolve
sy "Thanks, I guess."
scene ep12_sally_lewd84 with dissolve
mc "Talk soon?"
scene ep12_sally_lewd83 with dissolve
sy "Of course."
scene ep12_sally_lewd85 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep12_lewd_sally = True
$ calcScenes()
show screen new_phone_screen
$ new_bio("Sally", "I had sex with Sally in her dorm after the New Year's Eve party.")
$ mphone_stats_add_girl_s3("sally","You had sex with Sally in her dorm after the New Year's Eve party in episode 12.")

if wt_ep9_branch_numbers > 1:
  
   if "Elena" in wt_ep12_midnight_kiss:
       jump ep12_elena_lewd2_label

jump ep12_evaluation_label

label ep12_np2_afterny_label:
if not ep12_mean_prank:
    scene ep12_np2_afterny1
    show screen dance_filter_screen
    with dissolve
    $ renpy.pause()
    scene ep12_np2_afterny2 with dissolve
    $ renpy.pause()
    scene ep12_np2_afterny3 with dissolve
    al "*{i}Whispers{/i}* I'm here."
    jo "*{i}Whispers{/i}* Step carefully, it's dark in here."
    al "*{i}Whispers{/i}* Haha, I don't recognize your voice. It's so soft and pretty."
    jo "*{i}Whispers{/i}* It's me, babe."
    scene ep12_np2_afterny4 with dissolve
    "*{i}Smack smack{/i}*"
    al "Mmm.. You feel tight."
    jo "WHOA! WHOA! WHOA!"
    al "WHAT THE FUCK!"
scene ep12_np2_afterny5
hide screen dance_filter_screen
with dissolve
jm "Happy New Year, Leon."
scene ep12_np2_afterny6 with dissolve
le "Oh, hey... Hey... Uh..."
le "To you too, pal."
scene ep12_np2_afterny7 with dissolve
jac "Happy New Year, everyone!"
jac "Just because it's a new year, doesn't mean last year's party ended! Let's keep this one going!"

scene ep12_np2_afterny8 with dissolve
$ renpy.pause()
scene ep12_np2_afterny9 with dissolve
$ renpy.pause()
scene ep12_np2_afterny10 with dissolve
dw "*{i}Sigh{/i}* Wanna have sex?"
scene ep12_np2_afterny11 with dissolve
ar "With you?"
scene ep12_np2_afterny10 with dissolve
dw "Who else?"
scene ep12_np2_afterny11 with dissolve
ar "I can't tonight. I got my period."
scene ep12_np2_afterny12 with dissolve
dw "Oh..."
scene ep12_np2_afterny9 with dissolve
$ renpy.pause()

if wt_ep9_branch_numbers > 1:
   if "Isabella" in wt_ep12_midnight_kiss:
       jump ep12_bella_lewd_label 
   if "Zoey" in wt_ep12_midnight_kiss:
       jump ep12_zoey_lewd_label
   if "Jill" in wt_ep12_midnight_kiss:
        jump ep12_jill_lewd_label
   if "Sally" in wt_ep12_midnight_kiss:
       jump ep12_sally_lewd_label
   if "Elena" in wt_ep12_midnight_kiss:
       jump ep12_elena_lewd2_label

if ep12_midnight_kiss == "Zoey":
    jump ep12_zoey_lewd_label
elif ep12_midnight_kiss == "Sally":
    jump ep12_sally_lewd_label
elif ep12_midnight_kiss == "Quinn":
    jump ep12_np2_qend_label
elif ep12_midnight_kiss == "Isabella":
    jump ep12_bella_lewd_label
elif ep12_midnight_kiss == "Jill":
    jump ep12_jill_lewd_label
elif ep12_midnight_kiss == "Elena":
    jump ep12_elena_lewd_label
else:
    jump ep12_evaluation_label

label ep12_bella_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_isabella == None:
        $ mc_isabella = name
    else:
        $ mc_isabella = persistent.mc_isabella
    if persistent.isabella == None:
        $ isabella = "Isabella"
    else:
        $ isabella = persistent.isabella
    menu:
        "Kissed Jill in Episode 9":
            $ ep9_b_kissed_jill = True
        "Didn't kiss Jill":
            $ ep9_b_kissed_jill = False
    play music "music/ep12/licensed_music/track204.mp3"
hide screen new_phone_screen
scene ep12_bella_lewd1 with dissolve
isa "Hey. What are you drinking now?"
scene ep12_bella_lewd2 with dissolve
mc "I think it's whisky...or scotch. What's the difference between those two anyway?"
scene ep12_bella_lewd1 with dissolve
isa "I couldn't tell you without looking it up first."
scene ep12_bella_lewd2 with dissolve
mc "I bet that's why you stick to wine. Red and white. Simple."
scene ep12_bella_lewd4 with dissolve
isa "And sparkling, rosé, dessert wine... Then there are different regions and grapes."
scene ep12_bella_lewd3 with dissolve
mc "Yeah, yeah. I get it. How's it going?"
scene ep12_bella_lewd6 with dissolve
isa "I...um... *{i}Cough cough{/i}*"
scene ep12_bella_lewd3 with dissolve
mc "Oh! Now?"
scene ep12_bella_lewd4 with dissolve
isa "Yes."
scene ep12_bella_lewd3 with dissolve
mc "Where to?"
scene ep12_bella_lewd4 with dissolve
isa "In a place where I assume neither of us has done it before."
scene ep12_bella_lewd5 with dissolve
mc "I'll tail you there."
scene ep12_bella_lewd7 with dissolve
$ renpy.pause()
if ep9_b_kissed_jill:
    scene ep12_bella_lewd8 with dissolve
    $ renpy.pause()
    scene ep12_bella_lewd9 with dissolve
    $ renpy.pause()
scene ep12_bella_lewd10 with dissolve
mc "The gym locker room..."
scene ep12_bella_lewd11 with dissolve
isa "Was I right?"
scene ep12_bella_lewd12 with dissolve
mc "You were. I've never done it in here."
scene ep12_bella_lewd13 with dissolve
isa "Not just in here... Never in a locker room, yes?"
scene ep12_bella_lewd16 with dissolve
$ renpy.pause()
scene ep12_bella_lewd15 with dissolve
isa "Do you have to think?"
scene ep12_bella_lewd14 with dissolve
mc "No, I'm sure. This is a first."
mc "I'm a bit worried someone would casually walk in on us, though."
scene ep12_bella_lewd13 with dissolve
isa "Who would walk in on us? It's been locked all night."
scene ep12_bella_lewd14 with dissolve
mc "But you didn't lock it now."
scene ep12_bella_lewd13 with dissolve
isa "That's because it doesn't lock from the inside."
scene ep12_bella_lewd14 with dissolve
mc "I don't know, Bella... This is daring."
scene ep12_bella_lewd17 with dissolve
isa "*{i}Smack{/i}*"
scene ep12_bella_lewd18 with dissolve
mc "Ok. What the hell?"
scene ep12_bella_lewd17 with dissolve
isa "*{i}Smack{/i}* Mmm..."
scene ep12_bella_lewd17b with dissolve
isa "Mmm... Yes. *{i}Sighs{/i}*"
scene ep12_bella_lewd19 with dissolve
isa "*{i}Smack{/i}*"
scene ep12_bella_lewd20b with dissolve
mc "Fuck... Those sexy breasts are calling out my name."
scene ep12_bella_lewd20 with dissolve
mc "Yeah... I can't resist you. You're so damned gorgeous tonight."
scene ep12_bella_lewd21 with dissolve
isa "Just tonight?"
scene ep12_bella_lewd22 with dissolve
mc "No. Always."

scene ep12_bella_lewd21b with dissolve
mc "*{i}Smack{/i}* Mmmphff..."
scene ep12_bella_lewd21c with dissolve
isa "Mmm... You've missed them, haven't you?"
scene ep12_bella_lewd21d with dissolve
mc "They looked amazing in that dress tonight. I'm so happy I finally get to do what entered my mind to them."
scene ep12_bella_lewd21b with dissolve
mc "*{i}Smack{/i}*"
scene ep12_bella_lewd22 with dissolve
mc "And that ass..."
scene ep12_bella_lewd22b with dissolve
mc "Fuck!"
isa "Oh, my. All it takes for me is to undress and you go gaga over me."
scene ep12_bella_lewd22d with dissolve
mc "Isn't that a good thing? It should tell me how much you turn me on."
scene ep12_bella_lewd22e with dissolve
mc "*{i}Mmmphhff{/i}*"
isa "Mmm... It's very sexy seeing you get turned on like this."
mc "*{i}Smack{/i}*"
isa "But I don't think it's fair that you get all the fun."
scene ep12_bella_lewd22f with dissolve
mc "Oh, yeah?"
scene ep12_bella_lewd22g with dissolve
isa "*{i}Suck suck{/i}* Mhm..."
scene ep12_bella_lewd22h with dissolve
isa "*{i}Lick lick{/i}*"
scene ep12_bella_lewd22i with dissolve
isa "*{i}Lick lick{/i}*"
mc "Oh, God... Haha... Mmm..."
scene ep12_bella_lewd22j with dissolve
isa "I think we'll both have fun tonight."

scene ep12_bella_lewd23 with dissolve
mc "Where are you going?"
scene ep12_bella_lewd24 with dissolve
mc "You're such a tease."
scene ep12_bella_lewd25 with dissolve
mc "Wow... You're stunning."
scene ep12_bella_lewd26 with dissolve
isa "Do you prefer me with or without the dress?"
scene ep12_bella_lewd27 with dissolve
mc "Well, the dress was beautiful on you. But right now it's natural beauty."
scene ep12_bella_lewd28 with dissolve
isa "*{i}Smack{/i}* Mmm..."
scene ep12_bella_lewd29 with dissolve
$ renpy.pause()

if ep9_b_kissed_jill:
    scene ep12_bella_lewd30 with dissolve
    $ renpy.pause()
    scene ep12_bella_lewd31 with dissolve
    $ renpy.pause()
    scene ep12_bella_lewd32 with dissolve
    isa "Mmm... Yes."
    scene ep12_bella_lewd33 with dissolve
    mc "I want you, [isabella]."
    isa "Then go ahead and take me."

$ tmpInt = 0
label ep12_bella_lewd_loop1_label:
menu:
    "Kiss":
        $ tmpInt += 1
        scene anim_bkiss_ep12 with dissolve
        isa "Mmm... *{i}Smack{/i}*"
        pause
        jump ep12_bella_lewd_loop1_label
    "Rub her":
        $ tmpInt += 1
        scene anim_bella_finger_ep12 with dissolve
        isa "Yes, [mc_isabella]... Right there... Rub my clit."
        mc "Mmm... You feel wet."
        isa "It's because you made me wet."
        pause
        scene anim_bella_finger2_ep12 with dissolve
        isa "Mhm... That's the spot. Not too hard now. Be gentle with your fingers."
        mc "Alright, how about this?"
        isa "Yes... Much better."
        pause
        jump ep12_bella_lewd_loop1_label
    "Eat ass":
        $ tmpInt += 1
        scene anim_bella_eat_ep12 with dissolve
        mc "Mmmppfff... *{i}Smack{/i}*"
        isa "*{i}Moans{/i}* Yes... Eat me."
        pause
        jump ep12_bella_lewd_loop1_label
    "Assjob":
        $ tmpInt += 1
        scene anim_bella_assjob1_ep12 with dissolve
        mc "I can't get enough of your ass."
        isa "And I can't get enough of your cock... Although, I prefer to have it inside of me."
        mc "We'll get there... Just give me a moment here."
        pause
        scene anim_bella_assjob2_ep12 with dissolve
        isa "There's no rush... Enjoy my ass, [mc_isabella]."
        isa "I love the feeling of having your throbbing cock between my cheeks."
        pause
        jump ep12_bella_lewd_loop1_label
    "Blowjob":
        $ tmpInt += 1
        scene anim_bella_bj1_ep12 with dissolve
        isa "*{i}Suck suck{/i}*"
        mc "I think I could cum just by looking in your eyes. They're dangerous to get lost in."
        mc "Especially during a blowjob... Fuck!"
        pause
        scene anim_bella_bj2_ep12 with dissolve
        isa "*{i}Suck glug glug{/i}*"
        mc "Yes... Keep sucking the tip like that."
        pause
        jump ep12_bella_lewd_loop1_label
    "Continue" if tmpInt > 1:
        scene ep12_bella_lewd34 with dissolve
        isa "*{i}Moans{/i}* I want it, [mc_isabella]. I want you to fuck me. Right here. Right now."
        if ep9_b_kissed_jill:
            scene ep12_bella_lewd35 with dissolve
            mc "How do you want it?"
            scene ep12_bella_lewd36 with dissolve
            isa "In whatever way you want it... And I mean whatever."
        else:
            scene ep12_bella_lewd37 with dissolve
            mc "How do you want it?"
            scene ep12_bella_lewd34 with dissolve
            isa "In whatever way you want it... And I mean whatever."
        isa "On the floor, on a bench, against the wall... You name it, and I'm yours."

scene ep12_bella_lewd33c with dissolve
mc "I'm thinking... Against the wall. For starters..."
scene ep12_bella_lewd33b with dissolve
isa "Back or front?"
scene ep12_bella_lewd33c with dissolve
mc "You mean anal or not?"
scene ep12_bella_lewd33b with dissolve
isa "That wasn't what I meant, but sure... Why not?"
scene ep12_bella_lewd33d with dissolve
menu:
    "Vaginal":
        mc "Let's start from the front..."
        scene ep12_bella_lewd33e with dissolve
        isa "Like this?"
        scene ep12_bella_lewd33f with dissolve
        mc "Yeah, that's hot... I wanna push it inside you."
        isa "Mmm... How about if you do it slowly? I want to enjoy every second of it entering me."
        scene ep12_bella_lewd33g with dissolve
        mc "There's something special about when it first slides in, isn't there?"
        isa "*{i}Moans{/i}* Yes. The anticipation. The lust. It makes it so much better."
        scene ep12_bella_lewd33h with dissolve
        isa "*{i}Moans{/i}* Fuck! Yes... Just the tip..."
        mc "Oh, [isabella]... Your warmth envelops me."
        isa "Look at you being poetic. Give me a bit more of that cock, [mc_isabella]."
        scene ep12_bella_lewd33i with dissolve
        isa "Mhm... Mhm..."
        isa "Now... Give it all to me. All the way in."
        scene ep12_bella_lewd44 with hpunch
        mc "Oh, fuck!"
        isa "*{i}Moans{/i}* YES!!!"
        scene anim_bella_wall1_ep12 with dissolve
        isa "*{i}Moans{/i}* Ahhh... Yes! Yes!"
        pause
        scene anim_bella_wall2_ep12 with dissolve
        isa "Fuck me, [mc_isabella]."
        pause
    "Anal":
        mc "Let's start from the back then... Because your ass is calling out my name too."
        scene ep12_bella_lewd34a with dissolve
        isa "I know you want to, but don't put it all in at once, [mc_isabella]."
        mc "Oh, I know. I'll let you guide it in, if you want."
        scene ep12_bella_lewd34b with dissolve
        isa "Mmm... I'll guide it for us. Just stay perfectly still."
        scene ep12_bella_lewd34c with dissolve
        isa "*{i}Moans{/i}* Oh, fuck..."
        mc "Yes... You're doing great."
        scene ep12_bella_lewd34c2 with dissolve
        isa "Hngn... I'm gonna need a second here."
        mc "Take all the time you need. I'm not going anywhere."
        isa "I bet you aren't."
        scene ep12_bella_lewd34d with dissolve
        isa "Ahhh..."
        mc "There you go... Do it a bit more."
        scene ep12_bella_lewd34e with dissolve
        isa "*{i}Moans{/i}* Hngn..."
        mc "Damn, that's a tight ass."
        isa "Do you think I can take the rest?"
        mc "I know you can. You've done it before."
        scene ep12_bella_lewd34f with dissolve
        mc "Oh, fuck!"
        isa "Mmm... Yes... That's it."
        scene ep12_bella_lewd34d with dissolve
        isa "Yes..."
        scene ep12_bella_lewd34f with dissolve
        isa "Mhm..."
        scene ep12_bella_lewd34d with dissolve
        mc "Fuck! This is amazing."
        scene ep12_bella_lewd34f with dissolve
        isa "Ok, [mc_isabella]. You can pick up the speed now."
        scene ep12_bella_lewd34d with dissolve
        mc "Are you sure?"
        scene ep12_bella_lewd34f with dissolve
        isa "Yes. Fuck my ass, [mc_isabella]."
        scene anim_bella_doggy1_anal_ep12 with dissolve
        mc "I need to have it..."
        isa "*{i}Moans{/i}* Ahhh! Take it! Fuck me!"
        pause
        scene anim_bella_doggy2_anal_ep12 with dissolve
        pause

$ tmpInt = 0
$ tmpBool = False
label ep12_bella_lewd_loop2_label:
if ep9_b_kissed_jill and tmpInt == 3:
    jump ep12_bella_lewd_jill_label
elif ep9_b_kissed_jill and tmpInt == 7:
    jump ep12_bella_lewd_jillb_label
menu:
    "Against the wall":
        $ tmpInt += 1
        scene anim_bella_wall1_ep12 with dissolve
        isa "*{i}Moans{/i}* Ahhh... Yes! Yes!"
        pause
        scene anim_bella_wall2_ep12 with dissolve
        isa "Fuck me, [mc_isabella]."
        pause
        jump ep12_bella_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        if ep9_b_kissed_jill:
            scene anim_bella_doggy1b_ep12 with dissolve
        else:
            scene anim_bella_doggy1_ep12 with dissolve
        mc "Damn, you feel amazing."
        isa "As do you... *{i}Moans{/i}*"
        pause
        scene anim_bella_doggy2_ep12 with dissolve
        isa "*{i}Moans{/i}* You feel....too good..."
        pause
        if not tmpBool:
            $ tmpBool = True
            scene ep12_bella_lewd38 with vpunch
            isa "*{i}Moans{/i}* Ahh!!!"
            scene ep12_bella_lewd39 with vpunch
            isa "Fuck! Mmm..."
            scene ep12_bella_lewd40 with dissolve
            mc "I love making you cum."
            scene ep12_bella_lewd41 with dissolve
            isa "Mmm... You're so damn good at it."
        jump ep12_bella_lewd_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_bella_ride1_ep12 with dissolve
        mc "Yes... Ride me. Just like that."
        isa "Mhm... You like it when I bounce up and down on you, don't you?"
        mc "Yes, I love feeling your powerful thrusts from above. I feel like you're in complete control over me."
        isa "Well, I am. I can do whatever I want from here, I'll have you know."
        pause
        scene anim_bella_ride2_ep12 with dissolve
        mc "And I love watching your big tits from this angle... Fuck, they're great."
        isa "*{i}Moans{/i}*"
        pause
        jump ep12_bella_lewd_loop2_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_bella_rev1_ep12 with dissolve
        mc "Hngn... Fuck."
        isa "What's the matter, [mc_isabella]? Are you getting close?"
        mc "Yeah, but I don't want to cum yet."
        isa "Then don't. Close your eyes or think about something else."
        mc "And miss out on enjoying the view? No way!"
        pause
        scene anim_bella_rev2_ep12 with dissolve
        mc "But I gotta admit... Watching your ass jiggle up and down like that doesn't help."
        isa "I wouldn't blame you if you came, [mc_isabella]."
        pause
        jump ep12_bella_lewd_loop2_label
    "Against the wall (Anal)":
        $ tmpInt += 1
        scene anim_bella_doggy1_anal_ep12 with dissolve
        mc "I need to have your ass..."
        isa "*{i}Moans{/i}* Ahhh! Take it! Fuck me!"
        pause
        scene anim_bella_doggy2_anal_ep12 with dissolve
        pause
        jump ep12_bella_lewd_loop2_label
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_bella_rev1_anal_ep12 with dissolve
        isa "I'll have you cum in no time."
        mc "You will, when you ride it like that. But please... Let me savor the moment a bit longer."
        pause
        scene anim_bella_rev2_anal_ep12 with dissolve
        isa "*{i}Moans{/i}* Why, [mc_isabella]?"
        isa "Don't you want to fill my ass with cum? Aren't you on the brink of cumming right about now?"
        isa "You know... I can feel your cock twitching inside me. You can't fool me... You're close."
        mc "Hngn... Fuck!!!"
        pause
        jump ep12_bella_lewd_loop2_label
    "Missionary (Anal)":
        $ tmpInt += 1
        scene anim_bella_miss1_anal_ep12 with dissolve
        isa "Ah! Ahhh!"
        mc "Is it good?"
        isa "So good... Mmm..."
        mc "For me too. I love fucking your ass."
        pause
        scene anim_bella_miss2_anal_ep12 with dissolve
        mc "It's incredible how good you've gotten at this."
        isa "Oh, please. Like I didn't nail it the first time we tried."
        mc "Yeah, you did. But it feels natural to do this with you now."
        mc "You don't even flinch or hesitate when I push my cock into your ass."
        isa "That thing between your legs doesn't scare me."
        mc "Haha, good..."
        pause
        jump ep12_bella_lewd_loop2_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_bella_ride1_anal_ep12 with dissolve
        mc "Oh, fuck.... [isabella]... This is too much."
        isa "*{i}Moans{/i}* Don't you dare cum yet..."
        mc "Why not now?"
        isa "Because it's hitting the right spot. It started to feel really good for me. *{i}Moans{/i}*"
        mc "I'm happy it's not just me."
        pause
        scene anim_bella_ride2_anal_ep12 with dissolve
        isa "*{i}Moans{/i}* Oh, God!"
        mc "Oh, [isabella]!"
        pause
        jump ep12_bella_lewd_loop2_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna cum..."
        menu:
            "Facial":
                scene anim_bella_bj1_ep12 with dissolve
                isa "*{i}Suck suck suck{/i}*"
                mc "Yes... Yes... I'm cumming!"
                pause
                scene ep12_bella_lewd48 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bella_lewd48 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bella_lewd49 at vpunch, cum2
                mc "Ahhh!!! Fuck!"
                scene ep12_bella_lewd50 with dissolve
                $ renpy.pause()
                jump ep12_bella_lewd_cont_label
            "On tits":
                scene anim_bella_bj1_ep12 with dissolve
                isa "*{i}Suck suck suck{/i}*"
                mc "Yes... Yes... I'm cumming!"
                pause
                scene ep12_bella_lewd51 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bella_lewd51 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bella_lewd51 at vpunch, cum2
                mc "Ahhh!!! Fuck!"
                scene ep12_bella_lewd52 with dissolve
                $ renpy.pause()
                jump ep12_bella_lewd_cont_label
            "Creampie":
                scene anim_bella_wall1_ep12 with dissolve
                isa "Do it, [mc_isabella]. Cum inside me... Unload."
                pause
                scene ep12_bella_lewd44 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_bella_lewd44 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_bella_lewd44 at vpunch, cum1
                mc "Ahhh!!! Fuck!"
                scene ep12_bella_lewd45 with dissolve
                $ renpy.pause()
                jump ep12_bella_lewd_cont_label
            "Creampie (Anal)":
                scene anim_bella_ride2_anal_ep12 with dissolve
                isa "Do it, [mc_isabella]. Cum inside me... Unload."
                pause
                scene ep12_bella_lewd42 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_bella_lewd42 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_bella_lewd42 at vpunch, cum1
                mc "Ahhh!!! Fuck!"
                scene ep12_bella_lewd43 with dissolve
                $ renpy.pause()
                jump ep12_bella_lewd_cont_label
            "On ass":
                scene anim_bella_doggy2_ep12 with dissolve
                isa "Do it, [mc_isabella]. Cum all over me..."
                pause
                scene ep12_bella_lewd46 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_bella_lewd46 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_bella_lewd46 at vpunch, cum3
                mc "Ahhh!!! Fuck!"
                scene ep12_bella_lewd47 with dissolve
                $ renpy.pause()
                jump ep12_bella_lewd_cont_label

label ep12_bella_lewd_jill_label:
$ tmpInt += 1
scene ep12_bella_lewd53 with dissolve
isa "*{i}Moans{/i}* Fuck me, [mc_isabella]."
scene anim_bella_jill1_ep12 with dissolve
pause
scene ep12_bella_lewd54 with hpunch
$ renpy.pause()
scene ep12_bella_lewd55 with hpunch
$ renpy.pause()
scene ep12_bella_lewd56 with dissolve
$ renpy.pause()
jump ep12_bella_lewd_loop2_label

label ep12_bella_lewd_jillb_label:
$ tmpInt += 1
scene ep12_bella_lewd53b with dissolve
isa "*{i}Moans{/i}* Yes! Oh, [mc_isabella]."
mc "I love fucking you like this, [isabella]."
scene ep12_bella_lewd54 with hpunch
$ renpy.pause()
scene ep12_bella_lewd54 with hpunch
$ renpy.pause()
scene ep12_bella_lewd54 with hpunch
ji "*{i}Moans{/i}*"
jump ep12_bella_lewd_loop2_label

label ep12_bella_lewd_cont_label:
scene ep12_bella_lewd57 with dissolve
mc "That was fucking fantastic..."
scene ep12_bella_lewd58 with dissolve
isa "Yeah. We're getting good at this."
if ep9_b_kissed_jill:
    scene ep12_bella_lewd54 with dissolve
    ji "Hngn..."
    scene ep12_bella_lewd64 with dissolve
    isa "Wait... Do you hear something?"
    scene ep12_bella_lewd65 with dissolve
    mc "What?"
    scene ep12_bella_lewd64 with dissolve
    isa "I thought I heard a voice."
    scene ep12_bella_lewd65 with dissolve
    mc "I'll check it out; stay here."
    play sound "sound_effects/door_close.mp3"
    scene ep12_bella_lewd66 with dissolve
    mc "Hello?"
    scene ep12_bella_lewd67 with dissolve
    isa "Was someone there?"
    scene ep12_bella_lewd68 with dissolve
    mc "I think so. Someone left when I got around the corner."
    scene ep12_bella_lewd67 with dissolve
    isa "Do you think they saw us?"
    scene ep12_bella_lewd68 with dissolve
    mc "We'd better get out of here."
    scene ep12_bella_lewd67 with dissolve
    isa "Let's not waste any time doing so."
    scene ep12_bella_lewd69 with dissolve
    mc "Ouch! I stepped on something sharp."
    scene ep12_bella_lewd70 with dissolve
    mc "Whoa. That's a nice ring. Is it yours?"
    isa "..."
    scene ep12_bella_lewd71 with dissolve
    isa "No..."
    scene ep12_bella_lewd70 with dissolve
    mc "Do you think it could belong to whoever was in here? I mean, who drops a nice ring like this in a locker room?"
    scene ep12_bella_lewd72 with dissolve
    isa "I think I have a clue."
    isa "Leave it to me, ok?"
    scene ep12_bella_lewd73 with dissolve
    $ renpy.pause()
else:
    isa "How do I look?"
    scene ep12_bella_lewd57 with dissolve
    mc "Beautiful."
    scene ep12_bella_lewd59 with dissolve
    isa "Thanks, but I meant, will I have to fix my hair before going out there?"
    scene ep12_bella_lewd57 with dissolve
    mc "Nah, you're good. Everyone's a mess by now."
    scene ep12_bella_lewd59 with dissolve
    isa "Or too drunk to walk straight. I appreciate you not overdoing it tonight."
    scene ep12_bella_lewd57 with dissolve
    mc "I rarely overdo it. Often, there's a good reason for it."
    scene ep12_bella_lewd58 with dissolve
    isa "Like being forced to drink during Hell Week?"
    scene ep12_bella_lewd60 with dissolve
    mc "Haha! That would be one."
    mc "Speaking of... The new semester starts soon."
    scene ep12_bella_lewd61 with dissolve
    isa "Another Hell Week?"
    scene ep12_bella_lewd62 with dissolve
    mc "Yeah."
    scene ep12_bella_lewd61 with dissolve
    isa "Just take it easy with this one."
    scene ep12_bella_lewd62 with dissolve
    mc "It's not my Hell Week. I'm not going through that ordeal again."
    scene ep12_bella_lewd63 with dissolve
    $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep12_lewd_isabella = True
$ calcScenes()
$ mphone_stats_add_girl_s3("isabella","You had sex with Bella in the locker room at the New Year's Eve party in episode 12.")
if ep9_b_kissed_jill:
    $ new_bio("Isabella", "Bella and I had sex in the locker room at the New Year's Eve party. We thought we heard someone in the room with us.")
else:
    $ new_bio("Isabella", "Bella and I had sex in the locker room at the New Year's Eve party.")
show screen new_phone_screen

if wt_ep9_branch_numbers > 1:

   if "Zoey" in wt_ep12_midnight_kiss:
       jump ep12_zoey_lewd_label
   if "Jill" in wt_ep12_midnight_kiss:
        jump ep12_jill_lewd_label
   if "Sally" in wt_ep12_midnight_kiss:
       jump ep12_sally_lewd_label
   if "Elena" in wt_ep12_midnight_kiss:
       jump ep12_elena_lewd2_label

jump ep12_evaluation_label

label ep12_zoey_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    play music "music/ep12/licensed_music/track204.mp3"
    $ ep12_mc_slut = False
hide screen new_phone_screen
scene ep12_np_zoey_prelewd1 with dissolve
zo "No offense to this party. It's bitching, and all..."
zo "But when can we get the fuck out of here?"
scene ep12_np_zoey_prelewd2 with dissolve
mc "It ends when it fizzles out."
scene ep12_np_zoey_prelewd1 with dissolve
zo "I'm afraid I'll get tired too early."
zo "And if I get too tired to do the things I want to do with you, we're gonna have a big problem."
scene ep12_np_zoey_prelewd2 with dissolve
mc "Aha... Is that how it is?"
mc "Tell me more about those things. Maybe you can convince me to leave."
scene ep12_np_zoey_prelewd4 with dissolve
zo "We're gonna fuck, [name]."
scene ep12_np_zoey_prelewd3 with dissolve
mc "Haha, not so loud."
scene ep12_np_zoey_prelewd4 with dissolve
zo "I'm gonna strip you down naked and do nasty things to you."
scene ep12_np_zoey_prelewd3 with dissolve
mc "Stop telling me. I got your point."
scene ep12_np_zoey_prelewd5 with dissolve
che "If he doesn't want to do that, I'm up for it."
scene ep12_np_zoey_prelewd4 with dissolve
zo "[name], I'm horny... Let's go."
scene ep12_np_zoey_prelewd3 with dissolve
mc "Ok, ok... We're going."
scene ep12_np_zoey_prelewd5 with dissolve
che "Cool! Where are we going?"
scene ep12_np_zoey_prelewd6 with dissolve
$ renpy.pause()
scene ep12_np_zoey_prelewd7 with dissolve
che "Marc... We have to be DIKs this year."
play sound "sound_effects/shove.mp3"
scene ep12_np_zoey_prelewd8 with hpunch
zo "Mmm..."
scene ep12_np_zoey_prelewd10 with dissolve
mc "You weren't kidding about being horny."
scene ep12_np_zoey_prelewd9 with dissolve
zo "*{i}Smack{/i}* It's too far to walk back home... Can't we do it here?"
scene ep12_np_zoey_prelewd10 with dissolve
mc "In the hallway where people have to pass to leave? I don't think so."
scene ep12_np_zoey_prelewd11 with dissolve
mc "I can't believe that I'm the sensible one here..."
mc "If you keep going like this, I won't be."
scene ep12_np_zoey_prelewd12 with dissolve
zo "Touch me, [name]."
scene ep12_np_zoey_prelewd13 with dissolve
mc "You're playing with fire, Zoey."
scene ep12_np_zoey_prelewd12 with dissolve
zo "We won't get burned."
scene ep12_np_zoey_prelewd14 with dissolve
zo "*{i}Moans{/i}*"
mc "You're all wet... Fuck..."
zo "Mhm..."
scene ep12_np_zoey_prelewd15 with dissolve
mc "Fuck, I want you bad."
scene ep12_np_zoey_prelewd13 with dissolve
mc "My place. Now!"
scene bg anim_zoey_pulled_ep12 movie with dissolve
pause

scene ep12_zoey_lewd1 with wipeleft
zo "You're not too tired, right?"
scene ep12_zoey_lewd2 with dissolve
mc "The only thing I'm tired of is waiting for this moment."
mc "You've looked so hot tonight."
scene ep12_zoey_lewd3 with dissolve
zo "We're not rushing into things, are we?"
scene ep12_zoey_lewd2 with dissolve
mc "Rushing into things? What does that even mean?"
mc "We've had lots of sex before. I see this as a continuation of where we left off."
scene ep12_zoey_lewd3 with dissolve
zo "Don't you feel like it's different this time around? It's not like riding a skateboard after winter."
scene ep12_zoey_lewd4 with dissolve
mc "For me it is. Because I always sucked at skateboarding."
mc "You were horny out of your mind ten minutes ago. What happened?"
scene ep12_zoey_lewd5 with dissolve
zo "I still am."
scene ep12_zoey_lewd4 with dissolve
mc "Then go with that feeling."
scene ep12_zoey_lewd5 with dissolve
zo "I would, but for once I need to know whether we're acting on impulse."
zo "I don't want you to wake up tomorrow morning with any regrets. Because I know I won't, and if you do...then..."
scene ep12_zoey_lewd6 with dissolve
mc "Zoey, you don't have to worry about that. I know I want this. I know I want you."
mc "Us getting back together was sudden; I'll give you that. And even if we're acting on impulse, that's not bad."
scene ep12_zoey_lewd7 with dissolve
mc "You know what impulses are, yeah? You burn your hand on the stove, and you pull away the hand before you feel the pain."
mc "Impulses can be good that way. Like, I wouldn't regret removing the hand from the stove. Nor will I regret what we do tonight."
scene ep12_zoey_lewd8 with dissolve
mc "Also, I won't wake up tomorrow morning. We're at least sleeping until lunch."
scene ep12_zoey_lewd9 with dissolve
zo "Haha..."
zo "If you're completely sure."
scene ep12_zoey_lewd8 with dissolve
mc "I appreciate you taking the time to think about it and ask me."
mc "I wouldn't be able to do that when I'm horny. I get how hard it must be for you."
scene ep12_zoey_lewd9 with dissolve
zo "Haha! We're not the same that way."
zo "Your brain is in your dick, isn't it?"
scene ep12_zoey_lewd10 with dissolve
mc "Come here, already. Let's see if we still got it."
scene ep12_zoey_lewd11 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_zoey_lewd12 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd13 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd14 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd15 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd16 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd17 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd18 with dissolve
$ renpy.pause()
$ tmpInt = 0
label ep12_zoey_lewd_loop1_label:
menu:
    "Suck tits":
        $ tmpInt += 1
        scene ep12_zoey_lewd19 with dissolve
        mc "Those piercings are sexy. Do they hurt?"
        scene ep12_zoey_lewd20 with dissolve
        zo "Not anymore. You can pull on them if you're careful."
        scene ep12_zoey_lewd21 with dissolve
        mc "I want to put my mouth on them."
        scene anim_zoey_tits_ep12 with dissolve
        mc "*{i}Suck suck{/i}*"
        zo "*{i}Moans{/i}* That feels good."
        pause
        jump ep12_zoey_lewd_loop1_label
    "Fondle ass":
        $ tmpInt += 1
        scene anim_zoey_fondle_ep12 with dissolve
        mc "What a view..."
        zo "Mmm... Stop teasing me, [name]..."
        mc "I'm teasing both of us. But it will be worth it once I put my cock inside you."
        zo "*{i}Groans{/i}*"
        pause
        jump ep12_zoey_lewd_loop1_label
    "Lick pussy":
        $ tmpInt += 1
        scene ep12_zoey_lewd22 with dissolve
        mc "I want to eat you..."
        scene anim_zoey_eat_ep12 with dissolve
        zo "*{i}Moans{/i}* Fuck! [name]... Hngn..."
        mc "*{i}Lick lick{/i}* You taste great. I could eat you for hours."
        pause
        jump ep12_zoey_lewd_loop1_label
    "Continue" if tmpInt > 1:
        scene ep12_zoey_lewd23 with dissolve
        mc "I can't wait any longer... I have to fuck you now."
scene ep12_zoey_lewd24 with dissolve
zo "I love how talkative you are."
scene ep12_zoey_lewd23 with dissolve
mc "Do I talk too much?"
scene ep12_zoey_lewd24 with dissolve
zo "No. But old you talked too little. I had to drag the words out of you."
zo "You've matured."
scene ep12_zoey_lewd23 with dissolve
mc "I don't know if I have matured. But I think I've gained some confidence."
scene ep12_zoey_lewd25 with dissolve
zo "Damn... You with confidence is a dangerous combination."
zo "You'd be unstoppable with that dick plus confidence."
zo "I'm glad you're with me now, but should I be worried?"
scene ep12_zoey_lewd23 with dissolve
mc "You don't have anything to worry about. I'm all yours."
scene ep12_zoey_lewd24 with dissolve
zo "Mmm... I like the way you say that."
scene ep12_zoey_lewd23 with dissolve
mc "Now you say it."
scene ep12_zoey_lewd26 with dissolve
zo "Not yet."
scene ep12_zoey_lewd23 with dissolve
mc "Why not?"
scene ep12_zoey_lewd26 with dissolve
zo "You said you were all mine... Why would I let you have all the fun?"
zo "I want to give you a taste of your own medicine."
scene ep12_zoey_lewd23 with dissolve

$ tmpInt = 0
label ep12_zoey_lewd_loop2_label:
menu:
    "Blowjob":
        $ tmpInt += 1
        scene anim_zoey_bj1_ep12 with dissolve
        zo "*{i}Suck suck{/i}*"
        mc "Fuck... I feel sensitive tonight. You're so good at sucking cock, Zoey."
        pause
        scene anim_zoey_bj2_ep12 with dissolve
        pause
        jump ep12_zoey_lewd_loop2_label
    "Tease dick":
        $ tmpInt += 1
        scene anim_zoey_tease_ep12 with dissolve
        mc "Mmm... That's hot."
        zo "I want you as hard as you can get."
        mc "It feels like all my blood is in my cock right now. I doubt it will get harder than this."
        zo "We'll see..."
        pause
        jump ep12_zoey_lewd_loop2_label
    "Assjob":
        $ tmpInt += 1
        scene anim_zoey_assjob_ep12 with dissolve
        zo "Be perfectly still..."
        mc "Fuck... That's impossible. I wanna push hard against your ass."
        zo "Oh, I bet you do. But you're not allowed to."
        pause
        scene anim_zoey_assjob2_ep12 with dissolve
        zo "How much do you want it?"
        mc "I can't even describe how much. Slide it in any hole, and I'm good to go."
        zo "Haha! Now that's horny."
        pause
        jump ep12_zoey_lewd_loop2_label
    "Continue" if tmpInt > 1:
        scene ep12_zoey_lewd29 with dissolve
        zo "You win."
        zo "I'm all yours, [name]. Give it to me..."
scene ep12_zoey_lewd30 with dissolve

$ tmpInt = 0
label ep12_zoey_lewd_loop3_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_zoey_miss_ep12 with dissolve
        mc "Fuck..."
        zo "*{i}Moans{/i}* Yes... This feels just like I remembered."
        pause
        scene anim_zoey_miss2_ep12 with dissolve
        mc "You're so hot with your tattoos and piercings."
        zo "Yeah? You like em?"
        mc "Yeah, they turn me on."
        pause
        scene anim_zoey_miss3_ep12 with dissolve
        pause
        jump ep12_zoey_lewd_loop3_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_zoey_doggy_ep12 with dissolve
        zo "Fuck me, [name]! Fuck me!"
        pause
        scene anim_zoey_doggy2_ep12 with dissolve
        mc "I've missed your sexy ass. It feels amazing slapping against me like that."
        pause
        jump ep12_zoey_lewd_loop3_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_zoey_ride_ep12 with dissolve
        zo "Hnhn... It's so good!"
        pause
        scene anim_zoey_ride2_ep12 with dissolve
        zo "*{i}Moans{/i}* Fuck, [name]... I think I'm getting close."
        mc "Cum whenever you feel like it, Zoey."
        pause
        scene anim_zoey_ride3_ep12 with vpunch
        zo "Ahh!!! I'm cumming!"
        mc "Fuck! That's hot!"
        pause
        jump ep12_zoey_lewd_loop3_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_zoey_rev_ep12 with dissolve
        mc "Ride me, Zoey."
        zo "Haha..."
        mc "What?"
        zo "Nothing. Just memories."
        pause
        scene anim_zoey_rev2_ep12 with dissolve
        zo "*{i}Moans{/i}*"
        pause
        scene anim_zoey_rev3_ep12 with dissolve
        pause
        jump ep12_zoey_lewd_loop3_label
    "Prone (Anal)":
        $ tmpInt += 1
        scene ep12_zoey_lewd27 with dissolve
        mc "I wanna fuck that ass..."
        zo "Careful... This position makes it so tight for me. Let me set the pace, ok?"
        scene ep12_zoey_lewd28 with dissolve
        mc "Yeah, of course."
        scene anim_zoey_prone_ep12 with dissolve
        zo "*{i}Moans{/i}*"
        mc "Yeah, that's damn tight..."
        pause
        scene anim_zoey_prone2_ep12 with dissolve
        pause
        jump ep12_zoey_lewd_loop3_label
    "Piledriver (Anal)":
        $ tmpInt += 1
        scene anim_zoey_pile_ep12 with dissolve
        zo "Ahh! Ahh!!!"
        zo "*{i}Moans{/i}* Keep going!"
        pause
        scene anim_zoey_pile2_ep12 with dissolve
        mc "I wanna cum all over your ass."
        zo "Not yet. More! Give me more!"
        pause
        jump ep12_zoey_lewd_loop3_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_zoey_ride_anal_ep12 with dissolve
        zo "Mmm... Yes. It's so good."
        pause
        scene anim_zoey_ride2_anal_ep12 with dissolve
        mc "You're taking it all."
        zo "Mhm. It's stretching me out."
        pause
        scene anim_zoey_ride3_anal_ep12 with dissolve
        mc "I've missed you so much..."
        zo "Dude... Don't make me cry here... Make me cum, haha..."
        pause
        jump ep12_zoey_lewd_loop3_label
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_zoey_rev_anal_ep12 with dissolve
        zo "Are you gonna cum for me, [name]?"
        mc "I'm getting there just watching your ass bounce up and down like that."
        pause
        scene anim_zoey_rev2_anal_ep12 with dissolve
        zo "Mmm... I want your cum, [name]."
        pause
        jump ep12_zoey_lewd_loop3_label
    "Cum" if tmpInt > 2:
        menu:
            "Creampie":
                scene anim_zoey_miss_ep12 with dissolve
                mc "Fuck, I'm gonna cum!"
                zo "Cum, [name]! Cum!!!"
                pause
                scene ep12_zoey_lewd34 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd34 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd34 at hpunch, cum1
                mc "Ahh!!!"
                scene ep12_zoey_lewd35 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_zoey_rev2_anal_ep12 with dissolve
                mc "Fuck, I'm gonna cum!"
                zo "Cum, [name]! Cum!!!"
                pause
                scene ep12_zoey_lewd31 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd31 at hpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd31 at hpunch, cum1
                mc "Ahh!!!"
                scene ep12_zoey_lewd32 with dissolve
                $ renpy.pause()
                scene ep12_zoey_lewd33 with dissolve
                $ renpy.pause()
            "On ass":
                scene anim_zoey_doggy2_ep12 with dissolve
                mc "Fuck, I'm gonna cum!"
                zo "Cum, [name]! Cum!!!"
                pause
                scene ep12_zoey_lewd36 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd36 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd36 at hpunch, cum2
                mc "Ahh!!!"
                scene ep12_zoey_lewd37 with dissolve
                $ renpy.pause()
            "On tits":
                scene anim_zoey_bj2_ep12 with dissolve
                mc "Fuck, I'm gonna cum!"
                zo "*{i}Suck suck glug glug{/i}*"
                pause
                scene ep12_zoey_lewd40 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd40 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd40 at hpunch, cum2
                mc "Ahh!!!"
                scene ep12_zoey_lewd41 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_zoey_bj2_ep12 with dissolve
                mc "Fuck, I'm gonna cum!"
                zo "*{i}Suck suck glug glug{/i}*"
                pause
                scene ep12_zoey_lewd38 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd38 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_zoey_lewd38 at hpunch, cum2
                mc "Ahh!!!"
                scene ep12_zoey_lewd39 with dissolve
                $ renpy.pause()


scene ep12_zoey_lewd42 with dissolve
$ renpy.pause()
scene ep12_zoey_lewd43 with dissolve
zo "Yep... We still got it."
scene ep12_zoey_lewd44 with dissolve
mc "We sure do..."
scene ep12_zoey_lewd43 with dissolve
zo "Do you think they're still partying over there?"
scene ep12_zoey_lewd44 with dissolve
mc "Some probably are. But I think all the lucky ones have already left."
scene ep12_zoey_lewd43 with dissolve
zo "Including us. This was even better than I remembered it."
if ep12_mc_slut:
    scene ep12_zoey_lewd45 with dissolve
    mc "This slut has learned some moves."
    scene ep12_zoey_lewd46 with dissolve
    zo "Haha! Fuck off. That's not a joke I want to hear."
    scene ep12_zoey_lewd47 with dissolve
    zo "You're all mine. And we're gonna learn new moves together."
    scene ep12_zoey_lewd48 with dissolve
    mc "Love it. Love you."
else:
    scene ep12_zoey_lewd48 with dissolve
    mc "Yeah, I wonder why that is."
    scene ep12_zoey_lewd47 with dissolve
    zo "I think I know why."
    scene ep12_zoey_lewd48 with dissolve
    mc "Yeah... I do too."
scene ep12_zoey_lewd47 with dissolve
zo "I love you."
scene ep12_zoey_lewd49 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_zoey_lewd50 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep12_lewd_zoey = True
$ calcScenes()
$ new_bio("Zoey", "Zoey and I had sex after the New Year's Eve party.")
$ mphone_stats_add_girl_s3("zoey","You had sex with Zoey in your room after the New Year's Eve party in episode 12.")

if wt_ep9_branch_numbers > 1:
   if "Jill" in wt_ep12_midnight_kiss:
        jump ep12_jill_lewd_label
   if "Sally" in wt_ep12_midnight_kiss:
       jump ep12_sally_lewd_label
   if "Elena" in wt_ep12_midnight_kiss:
       jump ep12_elena_lewd2_label

show screen new_phone_screen
jump ep12_evaluation_label

label ep12_np2_qmc_label:
$ currentFreeRoamLabel = "ep12_np_dining_label"
scene ep12_np2_qmc1
hide screen dance_filter_screen
with dissolve
$ renpy.pause()
scene ep12_np2_qmc2 with dissolve
qu "Party bitch checking in."
if ep12_mc_slut:
    qu "There's my little slut."
else:
    qu "There's my little eunuch."
scene ep12_np2_qmc3 with dissolve
mc "Was that necessary?"
scene ep12_np2_qmc5 with dissolve
qu "I needed to know."
scene ep12_np2_qmc3 with dissolve
mc "You could have asked me instead of asking the room."
scene ep12_np2_qmc5 with dissolve
qu "There's no fun in that."
scene ep12_np2_qmc4 with dissolve
if ep12_mc_slut and affinity == "DIK":
    qu "Don't tell me that got to you. You were joking around, too."
else:
    qu "Don't tell me that got to you."
scene ep12_np2_qmc3 with dissolve
if ep12_mc_slut and affinity == "DIK":
    mc "Yeah, to save face."
mc "I feel I have had enough exposure this year. People have already seen my junk on display; they didn't need to know my sexual history."
scene ep12_np2_qmc6 with dissolve
qu "Aw, shit... I pissed my guy off."
scene ep12_np2_qmc3 with dissolve
mc "What do you mean by your guy?"
scene ep12_np2_qmc6 with dissolve
qu "What do you think I meant?"
qu "I meant what I said. You're mine."
scene ep12_np2_qmc3 with dissolve
mc "And what if I don't want to be yours?"
scene ep12_np2_qmc7 with dissolve
qu "Not an option. There's no off-ramp from this freeway."
scene ep12_np2_qmc8 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Quinn path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]                    

menu:
    "Ride or die \n{size=-4}[m_c1][mod_choices[0]]":
        $ roadQuinn = True
        scene ep12_np2_qmc9 with dissolve
        mc "Ride or die, huh?"
        scene ep12_np2_qmc12 with dissolve
        qu "I see nothing but good times on the horizon. Tell me you're with me for the ride."
    "Hit the off-ramp":
        scene ep12_np2_qmc10 with dissolve
        mc "There is... And I'm taking it."
        scene ep12_np2_qmc13 with dissolve
        qu "Come on. Don't be that way."
        scene ep12_np2_qmc11 with dissolve
        mc "No. Fuck this. I don't know what it is, but you've changed."
        mc "*{i}Sigh{/i}* This isn't gonna work out."
        $ new_bio("Quinn", "I decided to ditch Quinn after she tried to embarrass me at the New Year's Eve party with her drinking game.")
        jump endEvent
scene ep12_np2_qmc14 with dissolve
$ renpy.pause()
scene ep12_np2_qmc12 with dissolve
qu "Cheer up."
scene ep12_np2_qmc16 with dissolve
$ renpy.pause()
scene ep12_np2_qmc17 with dissolve
qu "*{i}Smack{/i}*"
scene ep12_np2_qmc15 with dissolve
qu "Yeah, there's that genuine smile."
scene ep12_np2_qmc17 with dissolve
qu "*{i}Smack{/i}*"
scene ep12_np2_qmc18 with dissolve
mc "Another kiss? How much did you have to drink?"
scene ep12_np2_qmc19 with dissolve
qu "Not enough."
scene ep12_np2_qmc18 with dissolve
mc "Smoke?"
scene ep12_np2_qmc19 with dissolve
qu "Way earlier today."
scene ep12_np2_qmc18 with dissolve
mc "So, you're sober and doing this."
scene ep12_np2_qmc20 with dissolve
qu "Not really."
qu "I pissed you off, didn't I? It's my way of saying I'm sorry without actually saying it."
scene ep12_np2_qmc21 with dissolve
mc "Stop doing things that will piss me off, and you won't have to."
scene ep12_np2_qmc20 with dissolve
qu "I'm not wired that way. But I'll try."
scene ep12_np2_qmc23 with dissolve
$ renpy.pause()
scene ep12_np2_qmc22 with dissolve
qu "I've got a surprise for you."
scene ep12_np2_qmc21 with dissolve
mc "What's the surprise?"
scene ep12_np2_qmc22 with dissolve
qu "Meet me at the DJ table in five minutes, and I'll show you."
scene ep12_np2_qmc21 with dissolve
mc "This better not be a continuation of that drinking game."

$ event_list.append("ep12_np2_q_lewd_label")
$ task_list[0] = "Head to the DJ table"
$ updateTaskList()
$ new_bio("Quinn", "Despite her attempt to embarrass me at the New Year's Eve party, I decided I wanted to be with Quinn.")
jump endEvent

label ep12_np2_q_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_quinn == None:
        $ mc_quinn = name
    else:
        $ mc_quinn = persistent.mc_quinn
    if persistent.quinn == None:
        $ quinn = "Quinn"
    else:
        $ quinn = persistent.quinn
    play music "music/ep12/licensed_music/track203.mp3"
    queue music["music/ep12/licensed_music/track210.mp3", "music/ep12/licensed_music/track211.mp3", "music/ep12/licensed_music/track212.mp3", "music/ep12/licensed_music/track201.mp3","music/ep12/licensed_music/track203.mp3"]
hide screen new_phone_screen
scene ep12_np2_q_lewd1
show screen dance_filter_screen
with dissolve
mc "What are you doing down there?"
scene ep12_np2_q_lewd2 with dissolve
qu "I'm the surprise."
scene ep12_np2_q_lewd1 with dissolve
mc "I don't get it."
scene ep12_np2_q_lewd2 with dissolve
qu "You will. Pretend to mix some music, and I'll take care of the rest."
scene ep12_np2_q_lewd3 with dissolve
mc "Whoa, whoa! Not here."
qu "Why not? Are you worried the drunk people dancing will notice?"
mc "Yes. That's exactly it."
scene ep12_np2_q_lewd4 with dissolve
play sound "sound_effects/zipper.mp3"
qu "They won't. Make sure your waist doesn't show, and you'll be fine."
scene ep12_np2_q_lewd5 with dissolve
mc "You're crazy. You know that?"
scene ep12_np2_q_lewd6 with dissolve
qu "Crazy fun."
scene ep12_np2_q_lewd7 with dissolve
$ renpy.pause()
scene anim_q_bj_ep12 with dissolve
mc "Oh, fuck..."
qu "*{i}Suck suck{/i}*"
pause
scene ep12_np2_q_lewd8 with dissolve
mc "This isn't going well..."
qu "Want me to stop?"
scene ep12_np2_q_lewd9 with dissolve
mc "Fuck... No... Keep going..."
scene anim_q_bj2_ep12 with dissolve
qu "*{i}Suck suck{/i}*"
pause
scene anim_q_bj3_ep12 with dissolve
mc "Damn, you know how to do that..."
pause
scene ep12_np2_q_lewd9 with dissolve
mc "Quinn, this isn't gonna work out. I look stupid as fuck up here."
scene ep12_np2_q_lewd8 with dissolve
qu "Coast clear?"
mc "Yeah, if you hurry."
scene ep12_np2_q_lewd10 with dissolve
qu "Get behind me. I'll take it from here."
scene ep12_np2_q_lewd11 with dissolve
qu "Slide it in."
scene ep12_np2_q_lewd12 with dissolve
$ renpy.pause()
scene ep12_np2_q_lewd13 with dissolve
mc "Fuck, that feels good... Your pussy is so warm, and your ass is so hot."
qu "*{i}Moans{/i}* Focus now. Pretend that you're dancing."
scene anim_q_doggy1_ep12 with dissolve
qu "There you go. Feel the beat."
mc "Amazing..."
qu "I knew you'd love it."
pause
scene anim_q_doggy2_ep12 with dissolve
mc "I feel like we're gonna get caught any second."
qu "Relax. We're just dancing together. But don't hold it back; cum when you're close."
mc "I've been close since you put your lips around my dick."
qu "Mmm... When you cum, cum inside me."
mc "Are you sure?"
qu "Unless you want to wipe the console of cum, I suggest you do."
pause
scene anim_q_doggy3_ep12 with dissolve
qu "*{i}Moans{/i}* Fuck... How's it going back there?"
mc "Quinn, I'm gonna cum soon..."
qu "Fuck... You've got me on the edge now, too. The moment you burst, I can feel that I will cum too."
pause
scene ep12_np2_q_lewd14 at vpunch, cum1
$ renpy.pause(0.5)
scene ep12_np2_q_lewd14 at vpunch, cum1
$ renpy.pause(0.5)
scene ep12_np2_q_lewd14 at vpunch, cum1
mc "Ahh..."
scene ep12_np2_q_lewd15 at vpunch, cum1
qu "*{i}Moans{/i}* Hngn..."
scene ep12_np2_q_lewd16 with dissolve
$ renpy.pause()
scene ep12_np2_q_lewd17 with dissolve
mc "Fuck..."
scene ep12_np2_q_lewd18 with dissolve
qu "Surprise."
scene ep12_np2_q_lewd19 with dissolve
mc "Yeah. That was one hell of a surprise."
scene ep12_np2_q_lewd18 with dissolve
qu "Put your cock back where it belongs."
scene ep12_np2_q_lewd19 with dissolve
mc "You want it inside again?"
scene ep12_np2_q_lewd20 with dissolve
qu "Haha! In your pants! Although I liked that."
$ renpy.end_replay()
$ persistent.ep12_lewd_quinn2 = True
$ calcScenes()
$ task_list[0] = ""
$ updateTaskList()
$ new_bio("Quinn", "Quinn and I had sex behind the DJ booth at the New Year's Eve party.")
$ mphone_stats_add_girl_s3("quinn","You had sex with Quinn behind the DJ booth in episode 12.")
show screen new_phone_screen
jump endEvent

label ep12_np2_qend_label:
scene ep12_np2_qend1 with dissolve
mc "Has anyone seen Quinn?"
scene ep12_np2_qend2 with dissolve
mc "(Figures... She left without telling me.)"
play sound "sound_effects/shove.mp3"
scene ep12_np2_qend3 with vpunch
qu "Boo!"
scene ep12_np2_qend4 with dissolve
mc "There you are."
scene ep12_np2_qend5 with dissolve
qu "Heading home?"
scene ep12_np2_qend4 with dissolve
mc "Yeah. It's time. Are you coming?"
scene ep12_np2_qend5 with dissolve
qu "Giddy up!"
scene ep12_np2_qend6 with dissolve
mc "Did your legs stop working?"
scene ep12_np2_qend7 with dissolve
qu "No, but my feet hurt like cray cray..."
scene ep12_np2_qend6 with dissolve
mc "This horse won't stop at your place. And you know what that means."
scene ep12_np2_qend7 with dissolve
qu "Oh, no..."
scene ep12_np2_qend6 with dissolve
mc "Yep. Next stop, my bed."
scene ep12_np2_qend8 with dissolve
qu "*{i}Groans{/i}* Fine..."
jump ep12_evaluation_label

label ep12_np2_rio_label:
scene ep12_np2_rio1 with dissolve
mc "No one is happier than I to see you here tonight."
scene ep12_np2_rio2 with dissolve
ri "You might be competing with Cammy, but not with Quinn."
scene ep12_np2_rio3 with dissolve
mc "Did you talk to her?"
scene ep12_np2_rio4 with dissolve
ri "She forced herself into a conversation with me."
scene ep12_np2_rio3 with dissolve
mc "How did that go?"
scene ep12_np2_rio4 with dissolve
ri "Ask her face."
scene ep12_np2_rio3 with dissolve
mc "That bad?"
scene ep12_np2_rio5 with dissolve
ri "Not bad enough. She thinks she can bribe me or buy my loyalty back."
ri "She fucking hates that she can't."
scene ep12_np2_rio6 with dissolve
$ renpy.pause()
$ tmpInt = _preferences.get_volume("music")
$ renpy.sound.set_volume(0,channel="music")
play sound "sound_effects/whoosh_2.mp3"
scene ep12_np2_rio19
bd "Hold her still!!!"
ri "No! Please!!! No!!!"
scene ep12_np2_rio7
$ renpy.sound.set_volume(tmpInt,channel="music")
ri "*{i}Shudders{/i}*"
mc "What's wrong?"
scene ep12_np2_rio8 with dissolve
ri "Please... Don't do that."
ri "When it's around the neck like that, I..."
scene ep12_np2_rio9 with dissolve
mc "I'm so sorry."
scene ep12_np2_rio10 with dissolve
ri "I know it's you, but..."
scene ep12_np2_rio9 with dissolve
mc "Can I give you a hug?"
scene ep12_np2_rio11 with dissolve
$ renpy.pause()
scene ep12_np2_rio12 with dissolve
mc "Better?"
scene ep12_np2_rio13 with dissolve
ri "*{i}Sigh{/i}* Yes..."
scene ep12_np2_rio12 with dissolve
$ renpy.pause()
scene ep12_np2_rio13 with dissolve
ri "I was stupid for coming here. I'm not enjoying myself at all."
ri "I'm lying my ass off to everyone, and no one is the wiser."
scene ep12_np2_rio14 with dissolve
ri "Everyone except you."
ri "But if I told them the truth, I'd incriminate myself."
scene ep12_np2_rio15 with dissolve
mc "I'll support you in whatever you choose to do."
scene ep12_np2_rio16 with dissolve
$ renpy.pause()
scene ep12_np2_rio17 with dissolve
ri "Even if I went to the cops?"
scene ep12_np2_rio16 with dissolve
mc "Would you do that, since you've been a part of it all?"
scene ep12_np2_rio17 with dissolve
ri "Quinn told me she took care of things."
ri "And if what she said was true, Mom and I are safe..."
ri "And that's what I needed... But I can't take her word for it."
ri "I need proof."
scene ep12_np2_rio16 with dissolve
mc "It sounds like you have something to think about."
mc "I want you to be safe. Don't do anything that would put you in harm's way."
scene ep12_np2_rio18 with dissolve
$ renpy.pause()
$ task_list[3] = ""
$ updateTaskList()
$ new_bio("Riona", "Riona wasn't enjoying the New Year's Eve party, and I tried to support her.")
jump endEvent

label ep12_np2_ot_label:
scene ep12_np2_ot1 with dissolve
osc "Hey, you!"
ta "Oscar, stop it."
scene ep12_np2_ot2 with dissolve
osc "You fucked my girl, didn't you?"
scene ep12_np2_ot3 with dissolve

    

if ep11_tara_lewd:
    menu:
        "Admit it \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            if affinity == "DIK":
                scene ep12_np2_ot4 with dissolve
                mc "Pretty hard too."
            else:
                mc "If she drank, she drank."
        "Deny it":
            if affinity == "DIK":
                mc "I don't remember. Probably not."
            else:
                mc "No, I didn't."
            scene ep12_np2_ot2 with dissolve
            osc "Yes, you did! Fucking admit it."
    scene ep12_np2_ot5 with dissolve
    ta "Stop it, Oscar. Let it go!"
else:
    mc "I don't think so."
    scene ep12_np2_ot5 with dissolve
    if ep8_sarah_lewd:
        ta "Stop it, Oscar. Let it go!"
    else:
        ta "It was just a kiss, Oscar. Let it go!"

scene ep12_np2_ot6 with dissolve
osc "One of these days, I'm going to fuck someone you like."
scene ep12_np2_ot7 with dissolve
mc "This is my friend, Derek. I like him."
scene ep12_np2_ot8 with dissolve
de "You stay far away from my butthole, Oscar."
scene ep12_np2_ot12 with dissolve
de "Dude, you made him cry."

if ep11_tara_lewd:
    scene ep12_np2_ot14 with dissolve
    mc "You didn't have to drink, Tara."
    scene ep12_np2_ot15 with dissolve
    ta "With what we did together, I didn't drink enough."
    if not branchZoey:
        scene ep12_np2_ot14 with dissolve
        mc "Are you guys back together?"
        scene ep12_np2_ot16 with dissolve
        ta "We're not, but you know how it is..."
        scene ep12_np2_ot17 with dissolve
        if not roadQuinn:
            mc "Oh, well... You know where to find me."
        else:
            mc "Oh, well..."
        scene ep12_np2_ot18 with dissolve
        $ renpy.pause()
elif ep8_sarah_lewd:
    scene ep12_np2_ot14 with dissolve
    mc "Why did you tell him we had sex? We never did."
    scene ep12_np2_ot15 with dissolve
    ta "We did, but you don't know it. At the dorm party..."
    scene ep12_np2_ot14 with dissolve
    mc "Oh... That was you?"
    scene ep12_np2_ot18 with dissolve
    $ renpy.pause()
    scene ep12_np2_ot13 with dissolve
    de "How do you have sex with someone without knowing it? What kind of a game are you playing here, [mc_de]?"
else:
    scene ep12_np2_ot16 with dissolve
    ta "I shouldn't have kissed you... Now he's all pissed for no good reason."
$ task_list[1] = ""
$ updateTaskList()
$ new_bio("Tara", "Oscar got mad at me because Tara drank during Quinn's drinking game.")
jump endEvent

label ep12_np2_elena_label:
scene ep12_np2_elena1 with dissolve
el "[name]... Can you help me out with something?"
scene ep12_np2_elena2 with dissolve
mc "What do I have to carry?"
scene ep12_np2_elena3 with dissolve
el "Why did you assume you had to carry something? Because I'm a woman?"
scene ep12_np2_elena2 with dissolve
mc "Oh, not at all. Because that's all I've been helping out with tonight."
scene ep12_np2_elena4 with dissolve
el "It's nothing like that."
el "I've promised to do something for John Boy, and I wanted to check if you're up for it."
scene ep12_np2_elena2 with dissolve
mc "Does it have anything to do with what we did together at the panty party?"
scene ep12_np2_elena3 with dissolve
el "You saved me from awkwardly beating around the bush."
el "Would you be interested in that?"
scene ep12_np2_elena2 with dissolve
if branchZoey:
    mc "I can't. I have a girlfriend now."
    scene ep12_np2_elena4 with dissolve
    el "I thought so. I wasn't 100%% sure that was the case, but I suspected it."
    scene ep12_np2_elena2 with dissolve
    mc "If things were different, my answer might have been too."
    scene ep12_np2_elena4 with dissolve
    el "The question is always free, isn't it? Thanks for not making a big deal out of it."
    scene ep12_np2_elena5 with dissolve
    mc "I would never."
else:
    mc "Tonight?"
    scene ep12_np2_elena4 with dissolve
    el "Yes."
    scene ep12_np2_elena2 with dissolve
    mc "Can I think about it?"
    scene ep12_np2_elena4 with dissolve
    el "If we're doing it, we'll do it after midnight."
    scene ep12_np2_elena6 with dissolve
    mc "And by it, you mean...\"it\"?"
    scene ep12_np2_elena7 with dissolve
    el "*{i}Nervous chuckle{/i}* Yes. It."
    scene ep12_np2_elena6 with dissolve
    mc "Like last time?"
    scene ep12_np2_elena7 with dissolve
    el "No. This time it would be just you and me, and he'd be watching us."
    scene ep12_np2_elena6 with dissolve
    mc "He wants that?"
    scene ep12_np2_elena7 with dissolve
    el "It's his top fantasy since like forever."
    el "If you want to be a part of that, let me know. It would be a surprise to him from me."

$ task_list[12] = ""
$ updateTaskList()
$ new_bio("Elena", "Elena asked me if I wanted to have sex with her in front of John Boy.")
jump endEvent

label ep12_np2_mjmc_label:
$ wt_ep12_maya_josy_seen = True
play music "music/ep12/licensed_music/track204.mp3"
if maya_shiny_dress:
    scene ep12_np2_mjmc1 with dissolve
else:
    scene ep12_np2_mjmc1b with dissolve
js "So, next semester, I'll stop paying for my dorm then."
if maya_shiny_dress:
    scene ep12_np2_mjmc2 with dissolve
else:
    scene ep12_np2_mjmc2b with dissolve
my "Yeah. I think you should. Thank you so much for doing that all this time."
my "I know I haven't thanked you enough for it."
if maya_shiny_dress:
    scene ep12_np2_mjmc1 with dissolve
else:
    scene ep12_np2_mjmc1b with dissolve
js "You should come live with us."
if maya_shiny_dress:
    scene ep12_np2_mjmc2 with dissolve
else:
    scene ep12_np2_mjmc2b with dissolve
my "*{i}Sigh{/i}* I don't know... It's a big decision."
if maya_shiny_dress:
    scene ep12_np2_mjmc1 with dissolve
else:
    scene ep12_np2_mjmc1b with dissolve
js "Like we haven't already made big decisions tonight."
if maya_shiny_dress:
    scene ep12_np2_mjmc3 with dissolve
else:
    scene ep12_np2_mjmc3b with dissolve
my "Yeah... What is it about New Year's Eve that makes you want to make those?"
my "You could change on a Thursday if you wanted to. Yet, life-changing decisions are often made today."
if branchMayaJosy and not breakup:
    if maya_shiny_dress:
        scene ep12_np2_mjmc4 with dissolve
    else:
        scene ep12_np2_mjmc4b with dissolve
else:
    if maya_shiny_dress:
        scene ep12_np2_mjmc1 with dissolve
    else:
        scene ep12_np2_mjmc1b with dissolve
js "In our case, I think it's more of a coincidence. Wouldn't you agree?"

if branchMayaJosy and not breakup:
    if maya_shiny_dress:
        scene ep12_np2_mjmc5 with dissolve
    else:
        scene ep12_np2_mjmc5b with dissolve
    mc "Alright, what is it you needed to talk to me about?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc7 with dissolve
    else:
        scene ep12_np2_mjmc7b with dissolve
    my "[name]..."
    my "*{i}Sigh{/i}* There's no easy way to start this conversation with you."
    my "You might feel like it's sudden, but you should know that it's been in the air for months. And Josy and I have been talking over the last few weeks about it."
    my "More than we ever did before. We've pretty much let it all out."
    if maya_shiny_dress:
        scene ep12_np2_mjmc6 with dissolve
    else:
        scene ep12_np2_mjmc6b with dissolve
    mc "Let what out?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc8 with dissolve
    else:
        scene ep12_np2_mjmc8b with dissolve
    js "Our thoughts and feelings..."
    js "We've been completely unfiltered. And it's been draining, but also good for us."
    js "I feel like it's the first time Maya has truly heard what I had to say. And I understand her better now too."
    if maya_shiny_dress:
        scene ep12_np2_mjmc7 with dissolve
    else:
        scene ep12_np2_mjmc7b with dissolve
    my "You see, while we are three in this relationship, at times it has felt like we weren't."
    my "Sometimes, it's been us three, then it's been you and I, or you and Josy, but rarely just Josy and I."
    if maya_shiny_dress:
        scene ep12_np2_mjmc9 with dissolve
    else:
        scene ep12_np2_mjmc9b with dissolve
    js "And with everything that has been going on in our lives as of late, it was clear that Maya and I needed to talk without you."
    if maya_shiny_dress:
        scene ep12_np2_mjmc6 with dissolve
    else:
        scene ep12_np2_mjmc6b with dissolve
    mc "Did I do something wrong?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc7 with dissolve
    else:
        scene ep12_np2_mjmc7b with dissolve
    my "It wasn't about what you did. It was about what Josy and I didn't do - communicate."
    my "But now we have..."
    if maya_shiny_dress:
        scene ep12_np2_mjmc9 with dissolve
    else:
        scene ep12_np2_mjmc9b with dissolve
    js "This will be hard for you to hear..."
    js "...but Maya and I have decided that we want to be friends."
    if maya_shiny_dress:
        scene ep12_np2_mjmc6 with dissolve
    else:
        scene ep12_np2_mjmc6b with dissolve
    mc "What?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc7 with dissolve
    else:
        scene ep12_np2_mjmc7b with dissolve
    my "We need a break from each other. There's no other way to put it."
    if ep12_jsolo:
        if maya_shiny_dress:
            scene ep12_np2_mjmc10 with dissolve
        else:
            scene ep12_np2_mjmc10b with dissolve
        js "Like you know, [name]... You and me, spending time at Mom's place... It felt so good to me."
        if maya_shiny_dress:
            scene ep12_np2_mjmc11 with dissolve
        else:
            scene ep12_np2_mjmc11b with dissolve
        js "Then I pictured doing that toghether with Maya...and it wasn't the same."
        js "It would be so much more difficult."
    if check_mlove():
        if maya_shiny_dress:
            scene ep12_np2_mjmc12 with dissolve
        else:
            scene ep12_np2_mjmc12b with dissolve
        my "Picturing our relationship with just you and me in it, [name]..."
        my "It made me feel things I believed I wasn't allowed to feel."
        if maya_shiny_dress:
            scene ep12_np2_mjmc13 with dissolve
        else:
            scene ep12_np2_mjmc13b with dissolve
        my "And I also saw how you would fit well in with my family, and all my problems would be solved just like that..."
    if not ep12_jsolo and not check_mlove():
        scene ep12_np2_mjmc9b with dissolve
        js "Let's face it, our parents will never be ok with our relationship."

    if maya_shiny_dress:
        scene ep12_np2_mjmc14 with dissolve
    else:
        scene ep12_np2_mjmc14b with dissolve
    mc "Well, that's not news. We all share that issue with our parents and our relationship."
    mc "What happened to trying to be together despite that?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc15 with dissolve
    else:
        scene ep12_np2_mjmc15b with dissolve
    my "We know... But we're not sure we are in love with each other anymore."
    my "And we're not willing to risk our families when we feel that way."
    if maya_shiny_dress:
        scene ep12_np2_mjmc16 with dissolve
    else:
        scene ep12_np2_mjmc16b with dissolve
    js "I think the love we once felt for each other has turned into a very beautiful friendship..."
    js "But it's no longer about lust and desire."
    if ep12_jsolo:
        if maya_shiny_dress:
            scene ep12_np2_mjmc10 with dissolve
        else:
            scene ep12_np2_mjmc10b with dissolve
        js "It's not the same feelings as I've felt for you."
    if check_mlove():
        if maya_shiny_dress:
            scene ep12_np2_mjmc12 with dissolve
        else:
            scene ep12_np2_mjmc12b with dissolve
        my "Exactly... What I feel for you, [name], is so much different."
    if maya_shiny_dress:
        scene ep12_np2_mjmc14 with dissolve
    else:
        scene ep12_np2_mjmc14b with dissolve
    mc "But... A break from each other? What does that mean?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc18 with dissolve
    else:
        scene ep12_np2_mjmc18b with dissolve
    js "It means we want to find out for sure that it's how we truly feel. And the only way of doing that is to be without each other."
    if maya_shiny_dress:
        scene ep12_np2_mjmc14 with dissolve
    else:
        scene ep12_np2_mjmc14b with dissolve
    mc "You mean we should break up?"
    if maya_shiny_dress:
        scene ep12_np2_mjmc17 with dissolve
    else:
        scene ep12_np2_mjmc17b with dissolve
    my "That's not how we'd like to put it..."
    if maya_shiny_dress:
        scene ep12_np2_mjmc14 with dissolve
    else:
        scene ep12_np2_mjmc14b with dissolve
    if tc > 4:
        mc "But that's what it is, isn't it? If you're not together anymore...you've broken up."
    else:
        mc "But that's what it is, isn't it? If you're not together anymore...you've broken up. How would that make things better?"
        
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if tc > 4 and ep11_josy_love == 0 and ep11_maya_love == 0:
                           "scrappy" "You have too many cheater points and Maya & Josy's path will end here (need less than 4)"

    if ep10_got_contracts:
        if maya_shiny_dress:
            scene ep12_np2_mjmc19 with dissolve
        else:
            scene ep12_np2_mjmc19b with dissolve
        mc "And what about the contract, Maya? I thought you'd finally allow yourself to have us as a choice now."
        if maya_shiny_dress:
            scene ep12_np2_mjmc20 with dissolve
        else:
            scene ep12_np2_mjmc20b with dissolve
        my "That's true. I can make that choice, and for the first time it's not being forced upon me."
        my "It was us who decided we needed this break. It wasn't Patrick, or Pete, or anyone else. It was us."
        my "If anything... Staying together now on principle would be for the wrong reasons."

    if tc < 5 or ep11_josy_love > 0 or ep11_maya_love > 0:
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "And what about me? Don't I have a say in this?"
        if maya_shiny_dress:
            scene ep12_np2_mjmc18 with dissolve
        else:
            scene ep12_np2_mjmc18b with dissolve
        js "We know this affects you... And therein lies the problem. If it was just about Maya and me, it would have been easier."
    if (tc > 4 and persistent.no_cheater) and ep11_josy_love == 0 and ep11_maya_love == 0:
        $ breakup.append("Josy")
        $ breakup.append("Maya")
        $ event_list.append("sad")
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "Well... If you're honest with me, I have to return the favor..."
        mc "I've had a great time together with you two, and I will always remember the things we did together."
        if maya_shiny_dress:
            scene ep12_np2_mjmc21 with dissolve
        else:
            scene ep12_np2_mjmc21b with dissolve
        mc "I'm fully aware there's been friction between you two, and truth be told... I haven't felt 100%% about our relationship either."
        mc "And the more time I've spent at parties - not having to deal with our problems..."
        mc "I felt more relaxed and more like myself."
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "I can't say if I had felt different if I only had been in a relationship with one of you..."
        mc "But if you two want a break from each other, I feel like I need one too. From both of you."
        if check_jlove():
            if maya_shiny_dress:
                scene ep12_np2_mjmc22 with dissolve
            else:
                scene ep12_np2_mjmc22b with dissolve
            js "That's not what I expected to hear, but I don't blame you for it. This whole thing has been a mess, hasn't it?"
            if maya_shiny_dress:
                scene ep12_np2_mjmc23 with dissolve
            else:
                scene ep12_np2_mjmc23b with dissolve
            mc "Don't say that."
            if maya_shiny_dress:
                scene ep12_np2_mjmc22 with dissolve
            else:
                scene ep12_np2_mjmc22b with dissolve
            js "But that's how it feels like right now."
        if check_mlove():
            if maya_shiny_dress:
                scene ep12_np2_mjmc24 with dissolve
            else:
                scene ep12_np2_mjmc24b with dissolve
            my "It makes me sad to hear that you also want a break, but maybe it is for the best."
        if not check_mlove() and not check_jlove():
            scene ep12_np2_mjmc25b with dissolve
            js "It sounds like we're on the same page..."
            scene ep12_np2_mjmc26b with dissolve
            my "Yeah... I guess that's a good thing."
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "*{i}Sigh{/i}* I did not expect this tonight..."
        $ new_bio("Josy", "Josy and Maya decided they wanted to take a break from their relationship.")
        $ new_bio("Maya", "Josy and Maya decided they wanted to take a break from their relationship.")
        $ new_bio("Josy", "During the New Year's Eve party, I broke up with Josy and Maya.")
        $ new_bio("Maya", "During the New Year's Eve party, I broke up with Josy and Maya.")
        $ new_bio("You", "During the New Year's Eve party, I broke up with Josy and Maya.")
    elif check_jlove() and check_mlove():
        if ep11_maya_love == 2:
            if maya_shiny_dress:
                scene ep12_np2_mjmc25 with dissolve
            else:
                scene ep12_np2_mjmc25b with dissolve
            js "I know you're in love with Maya."
            if maya_shiny_dress:
                scene ep12_np2_mjmc27 with dissolve
            else:
                scene ep12_np2_mjmc27b with dissolve
            menu:
                "[m_c1]I'm in love with you, too":
                    $ ep12_both_love = True
                    mc "I'm in love with you, too..."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc28 with dissolve
                    else:
                        scene ep12_np2_mjmc28b with dissolve
                    js "*{i}Sigh of relief{/i}* I feel the same way about you."
                    js "I love you, [name]. I really do..."
                    js "But that makes this so much more difficult."
                "Don't say it":
                    $ ep12_both_love = False
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc22 with dissolve
                    else:
                        scene ep12_np2_mjmc22b with dissolve
                    js "And that's good, [name]... You two deserve happiness."
        elif ep11_josy_love == 2:
            if maya_shiny_dress:
                scene ep12_np2_mjmc26 with dissolve
            else:
                scene ep12_np2_mjmc26b with dissolve
            my "You're in love with Josy, [name]... We both know it."
            if maya_shiny_dress:
                scene ep12_np2_mjmc19 with dissolve
            else:
                scene ep12_np2_mjmc19b with dissolve
            menu:
                "[m_c1]I'm in love with you, too":
                    $ ep12_both_love = True
                    mc "I'm in love with you, too..."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc29 with dissolve
                    else:
                        scene ep12_np2_mjmc29b with dissolve
                    my "I...love you too, [name]."
                "Don't say it":
                    $ ep12_both_love = False
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc20 with dissolve
                    else:
                        scene ep12_np2_mjmc20b with dissolve
                    my "And I don't blame you for it. It makes sense."

        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "Where does that leave us?"
        if maya_shiny_dress:
            scene ep12_np2_mjmc18 with dissolve
        else:
            scene ep12_np2_mjmc18b with dissolve
        js "We don't expect you to decide right now, but I think you understand where this is heading, [name]."
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with dissolve
        else:
            scene ep12_np2_mjmc14b with dissolve
        mc "You expect me to choose between you two?"
        mc "I'm not the one who wants a break. I want to be with both of you."
        if maya_shiny_dress:
            scene ep12_np2_mjmc17 with dissolve
        else:
            scene ep12_np2_mjmc17b with dissolve
        my "We know, [name]..."
        if maya_shiny_dress:
            scene ep12_np2_mjmc30 with dissolve
        else:
            scene ep12_np2_mjmc30b with dissolve
        $ renpy.pause()
        scene ep12_np2_mjmc31 with Dissolve(2)
        js "I've had a crush on you too."
        scene ep12_np2_mjmc32 with Dissolve(2)
        js "I'm so happy you wanted to come over this weekend."
        js "It's been on my mind every day since you called..."
        scene ep12_np2_mjmc33 with dissolve
        js "Well... That feeling split with guilt..."
        js "Because of..."
        js "You know..."
        scene ep12_np2_mjmc34 with dissolve
        mc "You don't seem happy in that relationship, Josy."
        mc "I know it's not my thing to say...but you're attracted to me and I'm attracted to you."
        mc "I don't want to be the other guy, but look at us right now."
        mc "Don't you want this?"
        mc "Or am I just here because you're lonely?"
        scene ep12_np2_mjmc33 with dissolve
        js "No...you're not here just because I'm lonely."
        js "You're right...I want this, but..."
        js "...it's complicated..."
        js "...and I feel like I shouldn't."
        scene ep12_np2_mjmc41 with Dissolve(2)
        mc "Dammit..."
        my "Haha. Do you need a hand?"
        mc "Oh, hi..."
        scene ep12_np2_mjmc35 with Dissolve(2)
        my "I don't have a boyfriend."
        my "I tell guys I have a boyfriend because I'm not interested in attracting them."
        my "It may sound weird...but it's the only way that seems to work."
        scene ep12_np2_mjmc36 with dissolve
        mc "Ok, so you don't want me to be attracted to you?"
        scene ep12_np2_mjmc37 with dissolve
        my "Hey...you promised not to ask any more questions..."
        my "..."
        scene ep12_np2_mjmc38 with dissolve
        my "...but yeah..."
        my "...it would probably be for the best if you weren't."
        scene ep12_np2_mjmc40 with dissolve
        if ep1_maya_attracted:
            mc "..."
            mc "I think it's too late for that."
            scene ep12_np2_mjmc39 with dissolve
            my "Oh..."
        else:
            mc "Ok. I'll try."
        if maya_shiny_dress:
            scene ep12_np2_mjmc14 with Dissolve(2)
        else:
            scene ep12_np2_mjmc14b with Dissolve(2)
            
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Maya path)","(Josy path)","(Maya/Josy path)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        

        menu:
            "I can't choose \n{size=-4}[m_c1][mod_choices[2]]" if ep12_both_love or (ep11_josy_love == 0 and ep11_maya_love == 0):
                $ roadMayaJosy = True
                $ ep12_both_love = True
                mc "You know... I've spent so much time and energy on making sure you both felt good. That you both felt loved."
                mc "And now you're telling me this."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc42 with dissolve
                else:
                    scene ep12_np2_mjmc42b with dissolve
                mc "I understand that you're not feeling those feelings for each other, but I love both of you."
                mc "I love you... So much..."
                mc "I'm not choosing, because to me...my love for you two is equal."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc43 with dissolve
                else:
                    scene ep12_np2_mjmc43b with dissolve
                mc "I don't love you more than I love Josy..."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc44 with dissolve
                else:
                    scene ep12_np2_mjmc44b with dissolve
                mc "And I don't love you more than I love Maya..."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc42 with dissolve
                else:
                    scene ep12_np2_mjmc42b with dissolve
                mc "I love us. And if you're telling me that us is not an option..."
                mc "Then I refuse to choose."
                mc "We'll all have a break then."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc45 with dissolve
                else:
                    scene ep12_np2_mjmc45b with dissolve
                js "[name]... I know it's hard, but..."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc42 with dissolve
                else:
                    scene ep12_np2_mjmc42b with dissolve
                mc "I can't break either of your hearts. I'd rather break my own."
                $ new_bio("Josy", "Josy and Maya decided they wanted to take a break from their relationship.")
                $ new_bio("Maya", "Josy and Maya decided they wanted to take a break from their relationship.")
                $ new_bio("You", "During the New Year's Eve party, I couldn't decide between Josy and Maya and ended up taking a break from both of them.")
                $ new_bio("Josy", "During the New Year's Eve party, I couldn't decide between Josy and Maya and ended up taking a break from both of them.")
                $ new_bio("Maya", "During the New Year's Eve party, I couldn't decide between Josy and Maya and ended up taking a break from both of them.")
            "Josy \n{size=-4}[m_c2][mod_choices[1]]" if ep11_josy_love == 2 or (ep11_josy_love == 0 and ep11_maya_love == 0) or ep12_both_love:
                $ roadJosy = True
                jump ep12_np2_mjmc2_label
            "Maya \n{size=-4}[m_c1][mod_choices[0]]" if ep11_maya_love == 2 or (ep11_josy_love == 0 and ep11_maya_love == 0) or ep12_both_love:
                $ roadMaya = True
                label ep12_np2_mjmc2_label:
                mc "Expecting me to choose between you two is cruel..."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc46 with dissolve
                else:
                    scene ep12_np2_mjmc46b with dissolve
                my "This whole situation is cruel. I wish we didn't have to put you through it."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc42 with dissolve
                else:
                    scene ep12_np2_mjmc42b with dissolve
                mc "So, don't..."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc45 with dissolve
                else:
                    scene ep12_np2_mjmc45b with dissolve
                js "You have to try and see it from our perspective, [name]."
                js "We're both dying to get some sort of normalcy in our lives. A break from everything we've gone through this semester and before that."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc46 with dissolve
                else:
                    scene ep12_np2_mjmc46b with dissolve
                my "And this relationship that we're in together, won't give us that. We need that break."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc42 with dissolve
                else:
                    scene ep12_np2_mjmc42b with dissolve
                mc "But how can I look one of you in the eyes and break up with you? To me, that's not me taking a break from someone..."
                mc "That's me putting it out there. That I'd rather be with one over the other."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc45 with dissolve
                else:
                    scene ep12_np2_mjmc45b with dissolve
                js "It would hurt to hear, yes... But we knew this would hurt even so."
                if maya_shiny_dress:
                    scene ep12_np2_mjmc46 with dissolve
                else:
                    scene ep12_np2_mjmc46b with dissolve
                my "We've been honest with you, [name]. We want you to be honest with us too."
                if roadJosy:
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc47 with dissolve
                    else:
                        scene ep12_np2_mjmc47b with dissolve
                    mc "Josy and I... We've developed something I'm not willing to give up..."
                    mc "Maya... I'm so sorry."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc50 with dissolve
                    else:
                        scene ep12_np2_mjmc50b with dissolve
                    mc "I hate that you're doing this to me. I hate it."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc51 with dissolve
                    else:
                        scene ep12_np2_mjmc51b with dissolve
                    my "*{i}Sigh{/i}* I understand, [name]... I understand."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc50 with dissolve
                    else:
                        scene ep12_np2_mjmc50b with dissolve
                    $ renpy.pause()
                    $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship with Josy.")
                    $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship without Maya.")
                    $ new_bio("Josy", "During the New Year's Eve party, I decided to continue my relationship with Josy.")
                    $ new_bio("Maya", "During the New Year's Eve party, I decided to continue my relationship without Maya.")
                else:
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc48 with dissolve
                    else:
                        scene ep12_np2_mjmc48b with dissolve
                    mc "I've grown attached to both of you... But I believe I have developed a special bond to Maya."
                    mc "I'm not willing to give that up. I'm so sorry, Josy..."
                    if maya_shiny_dress:
                        scene ep12_np2_mjmc49 with dissolve
                    else:
                        scene ep12_np2_mjmc49b with dissolve
                    js "It's... It's ok... *{i}Sniffles{/i}*"
                    mc "It's not ok, Josy..."
                    $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship without Josy.")
                    $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship with Maya.")
                    $ new_bio("Josy", "During the New Year's Eve party, I decided to continue my relationship without Josy.")
                    $ new_bio("Maya", "During the New Year's Eve party, I decided to continue my relationship with Maya.")
                $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
                $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
    elif check_jlove():
        $ roadJosy = True
        scene ep12_np2_mjmc26b with dissolve
        if ep11_josy_love == 2:
            my "You're in love with Josy, [name]... We both know it. And I don't blame you for it. It makes sense."
        my "While this is hard, I'm going to make this easy for you, [name]."
        my "You two belong together. I think it's obvious."
        scene ep12_np2_mjmc52b with dissolve
        my "So, I'll leave..."
        scene ep12_np2_mjmc53b with dissolve
        mc "Maya..."
        scene ep12_np2_mjmc52b with dissolve
        my "You'll always have a special place in my heart, [name]. But this is how it has to be."
        scene ep12_np2_mjmc10b with dissolve
        js "I love you, [name]..."
        scene ep12_np2_mjmc55b with dissolve
        mc "I love you too. And there shouldn't be a \"but\" that follows that sentence, but there is..."
        scene ep12_np2_mjmc10b with dissolve
        js "I know. It's ok."
        scene ep12_np2_mjmc54b with dissolve
        mc "No, it's not ok."
        $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship with Josy.")
        $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship without Maya.")
        $ new_bio("Josy", "During the New Year's Eve party, I decided to continue my relationship with Josy.")
        $ new_bio("Maya", "During the New Year's Eve party, I decided to continue my relationship without Maya.")
        $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
        $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
    elif check_mlove():
        $ roadMaya = True
        if maya_shiny_dress:
            scene ep12_np2_mjmc25 with dissolve
        else:
            scene ep12_np2_mjmc25b with dissolve
        if ep11_maya_love == 2:
            js "I know you're in love with Maya."
            js "And that's good, [name]... You two deserve happiness."
        js "I'll be the one to say it... [name], you should be with Maya."
        if maya_shiny_dress:
            scene ep12_np2_mjmc56 with dissolve
        else:
            scene ep12_np2_mjmc56b with dissolve
        mc "What?"
        if maya_shiny_dress:
            scene ep12_np2_mjmc25 with dissolve
        else:
            scene ep12_np2_mjmc25b with dissolve
        js "We could pretend that you and I would make it work one day, but I see the chemistry you share with Maya and I can't compare."
        js "She's the one for you. I'm not. And I know she loves you."
        if maya_shiny_dress:
            scene ep12_np2_mjmc12 with dissolve
        else:
            scene ep12_np2_mjmc12b with dissolve
        my "I do. I love you, [name]."
        if maya_shiny_dress:
            scene ep12_np2_mjmc58 with dissolve
        else:
            scene ep12_np2_mjmc58b with dissolve
        mc "I love you too. And there shouldn't be a \"but\" that follows that sentence, but there is..."
        if maya_shiny_dress:
            scene ep12_np2_mjmc25 with dissolve
        else:
            scene ep12_np2_mjmc25b with dissolve
        js "It's ok."
        if maya_shiny_dress:
            scene ep12_np2_mjmc57 with dissolve
        else:
            scene ep12_np2_mjmc57b with dissolve
        mc "No, it's not ok."
        $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship without Josy.")
        $ new_bio("You", "During the New Year's Eve party, I decided to continue my relationship with Maya.")
        $ new_bio("Josy", "During the New Year's Eve party, I decided to continue my relationship without Josy.")
        $ new_bio("Maya", "During the New Year's Eve party, I decided to continue my relationship with Maya.")
        $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
        $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
    else:
        scene ep12_np2_mjmc59b with dissolve
        js "We both feel that our break extends to you."
        scene ep12_np2_mjmc14b with dissolve
        mc "What?"
        scene ep12_np2_mjmc59b with dissolve
        js "We need to be sure what we're feeling, and right now we aren't."
        scene ep12_np2_mjmc60b with dissolve
        my "So, we think it's for the best if we all go our separate ways for a while."
        my "And if that feels right, well... Then we made the right choice."
        scene ep12_np2_mjmc59b with dissolve
        js "And if we feel different, then we'll know that too."
        scene ep12_np2_mjmc14b with dissolve
        mc "So... We'll all have a break then."
        scene ep12_np2_mjmc59b with dissolve
        js "[name]... I know it's hard... But can you tell either of us with a straight face that this is working out?"
        scene ep12_np2_mjmc14b with dissolve
        mc "I mean... We've had great times together. We've had amazing sex. And I care so much about both of you."
        scene ep12_np2_mjmc60b with dissolve
        my "That's all true... And while I have loved our time together, and I love you as a person... I don't think I'm in love with you."
        scene ep12_np2_mjmc59b with dissolve
        js "And that's what we need to feel sure about."
        scene ep12_np2_mjmc14b with dissolve
        mc "..."
        $ breakup.append("Josy")
        $ breakup.append("Maya")
        $ event_list.append("sad")
        $ new_bio("Josy", "Josy and Maya decided they wanted to take a break from their relationship.")
        $ new_bio("Maya", "Josy and Maya decided they wanted to take a break from their relationship.")
        $ new_bio("You", "During the New Year's Eve party, I broke up with Josy and Maya.")
        $ new_bio("Josy", "During the New Year's Eve party, I broke up with Josy and Maya.")
        $ new_bio("Maya", "During the New Year's Eve party, I broke up with Josy and Maya.")

    if maya_shiny_dress:
        scene ep12_np2_mjmc61 with dissolve
    else:
        scene ep12_np2_mjmc61b with dissolve
    if tc > 4:
        mc "Sorry, but I think I need to be alone..."
    else:
        mc "I can't take more of this... I need to be alone."
    jump ep12_np2_fw_label
else:
    js "We've talked about this for weeks now."
    scene ep12_np2_mjmc62 with dissolve
    my "And it's been months in the making."
    my "I think we'll have a very beautiful friendship. After all, I feel like that's what we've had as of late."
    scene ep12_np2_mjmc65 with dissolve
    js "..."
    scene ep12_np2_mjmc66 with dissolve
    js "I feel sad."
    scene ep12_np2_mjmc63 with dissolve
    my "Me too. But it's the right choice."
    my "We keep fighting with each other when it comes to us, but have the best time together when we hang out as a group."
    my "You deserve more than what I can give you."
    scene ep12_np2_mjmc66 with dissolve
    js "And you deserve more than the options you've had to choose between."
    scene ep12_np2_mjmc64 with dissolve
    my "..."
    if not ep10_got_contracts:
        scene ep12_np2_mjmc63 with dissolve
        my "I don't want to give you any false hope. Even if things are different for me in a few years from now..."
        my "I think this truly is it for us."
        scene ep12_np2_mjmc66 with dissolve
        js "I know."
    scene ep12_np2_mjmc62 with dissolve
    my "A break then... We finally agreed on something."
    scene ep12_np2_mjmc67 with dissolve
    js "Yes, but I wish it wasn't this."
    scene ep12_np2_mjmc70 with dissolve
    $ renpy.pause()
    scene ep12_np2_mjmc69 with dissolve
    my "We'll get through it together."
    scene ep12_np2_mjmc68 with dissolve
    js "Haha, I don't think we're supposed to do it that way."
    scene ep12_np2_mjmc69 with dissolve
    my "Let's face it. We've never been normal."
    my "We're different, but there's nothing wrong with that."
    scene ep12_np2_mjmc71 with dissolve
    $ renpy.pause()
    if not breakup and not ep4_toldDerekAboutJade and (not roadSage and wt_ep9_branch_numbers == 1):
        scene ep12_np2_mjmc72 with dissolve
        mc "Look at you two holding hands in public."
        scene ep12_np2_mjmc73 with dissolve
        js "It's not what you think. It's the opposite."
        scene ep12_np2_mjmc74 with dissolve
        mc "What was I thinking?"
        scene ep12_np2_mjmc75 with dissolve
        my "We've decided to take a break from our relationship tonight."
        scene ep12_np2_mjmc74 with dissolve
        mc "Oh... I'm sorry to hear that."
        scene ep12_np2_mjmc73 with dissolve
        js "Don't be. It was the right call for us."
        if branchAlone and (ep10_feelingsForMaya or ep10_feelingsForJosy):
            scene ep12_np2_mjmc74 with dissolve
            mc "I have to ask... This didn't have anything to do with me...did it?"
            if ep10_feelingsForMaya:
                scene ep12_np2_mjmc76 with dissolve
                my "You're not the only reason. But yes, you were one of my reasons."
                scene ep12_np2_mjmc73 with dissolve
                js "Even if you hadn't been a reason... This still would have happened."
                js "I know you two have some unresolved feelings... I'll leave you alone."
                scene ep12_np2_mjmc77 with dissolve
                my "Josy?"
                scene ep12_np2_mjmc78 with dissolve
                js "It's ok, Maya. It's ok."
                scene ep12_np2_mjmc79 with dissolve
                $ renpy.pause()
                scene ep12_np2_mjmc80 with dissolve
                mc "I wish I knew what to say."
                scene ep12_np2_mjmc81 with dissolve
                my "Where's your heart at, [name]? Go ahead. After tonight, you can tell me anything."
                if branchZoey or (ep11_quinn_question[0] and ep11_quinn_question[1] and not ep12_quinn_ditch) or (ep12_nicole_path and not ep12_nicole_breakup) or ep12_rolling:
                    scene ep12_np2_mjmc82 with dissolve
                    if branchZoey:
                        mc "I'm back together with Zoey. I'm in love with her."
                        mc "It's been a tumultuous time for me. I've been all over the place."
                    elif (ep11_quinn_question[0] and ep11_quinn_question[1] and not ep12_quinn_ditch) or (ep12_nicole_path and not ep12_nicole_breakup) or ep12_rolling:
                        label ep12_np2_mjmc_label1:
                        mc "I'm single, but... I'm not available for you anymore. At least, that's how I feel."
                    scene ep12_np2_mjmc81 with dissolve
                    my "Are you happy the way it is now?"
                    scene ep12_np2_mjmc80 with dissolve
                    mc "I am."
                    scene ep12_np2_mjmc81 with dissolve
                    my "Then that's all that matters to me."
                else:
                    scene ep12_np2_mjmc80 with dissolve
                    
                    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Maya path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        

                    menu:
                        "I want to be with you \n{size=-4}[m_c1][mod_choices[0]]":
                            $ roadMaya = True
                            mc "I still feel the same about you, Maya."
                            mc "But I can't put that pressure on you. You just broke up with Josy."
                            scene ep12_np2_mjmc83 with dissolve
                            $ renpy.pause()
                            scene ep12_np2_mjmc84 with dissolve
                            my "*{i}Smack{/i}*"
                            scene ep12_np2_mjmc85 with dissolve
                            $ renpy.pause()
                            scene ep12_np2_mjmc86 with dissolve
                            my "You're right. But you should know that I feel the same way you do."
                            my "I will take some time alone because I need it."
                            my "But there's no question in my mind where my heart belongs."
                            scene ep12_np2_mjmc87 with dissolve
                            mc "You should be with Josy now..."
                            scene ep12_np2_mjmc86 with dissolve
                            my "Are you sure?"
                            scene ep12_np2_mjmc87 with dissolve
                            mc "I'm not going anywhere, Maya."
                            scene ep12_np2_mjmc88 with dissolve
                            $ renpy.pause()
                        "I'm not available":
                            scene ep12_np2_mjmc82 with dissolve
                            jump ep12_np2_mjmc_label1
                scene ep12_np2_mjmc80 with dissolve
                mc "I'm sorry about your breakup."
                scene ep12_np2_mjmc81 with dissolve
                my "Don't be. It's time we were honest with ourselves."
                my "Admitting that a relationship didn't work out is not the end of the world."
                my "I see this as a new beginning."
                scene ep12_np2_mjmc89 with dissolve
                $ renpy.pause()
                $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
                $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
                if roadMaya:
                    $ new_bio("Maya", "During the New Year's Eve party, I decided to enter into a relationship with Maya.")
                    $ new_bio("You", "During the New Year's Eve party, I decided to enter into a relationship with Maya.")
            else:
                scene ep12_np2_mjmc73 with dissolve
                js "I have told her about everything, [name]. And of course, that has affected us."
                scene ep12_np2_mjmc75 with dissolve
                my "But you weren't the deciding factor for me. Josy and I are better off as friends."
                my "We don't feel that way about each other anymore."
                my "And as for you two... You're two of my favorite people in the world. You two make more sense together than Josy and me do now."
                scene ep12_np2_mjmc77 with dissolve
                my "It won't be easy for me, but I'll try my best to be happy for you guys."
                my "You two should talk... I'll join the others."
                scene ep12_np2_mjmc78 with dissolve
                js "Thank you, Maya."
                scene ep12_np2_mjmc90 with dissolve
                $ renpy.pause()
                scene ep12_np2_mjmc92 with dissolve
                js "What are you thinking?"
                if branchZoey or (ep11_quinn_question[0] and ep11_quinn_question[1] and not ep12_quinn_ditch) or (ep12_nicole_path and not ep12_nicole_breakup) or ep12_rolling:
                    scene ep12_np2_mjmc93 with dissolve
                    if branchZoey:
                        mc "We're not gonna happen, Josy."
                        mc "I'm back together with Zoey. I'm in love with her."
                        mc "It's been a tumultuous time for me. I've been all over the place."
                    elif (ep11_quinn_question[0] and ep11_quinn_question[1] and not ep12_quinn_ditch) or (ep12_nicole_path and not ep12_nicole_breakup) or ep12_rolling:
                        label ep12_np2_mjmc_label2:
                        mc "I'm single, but... I'm not available for you anymore. At least, that's how I feel."
                    scene ep12_np2_mjmc94 with dissolve
                    $ renpy.pause()
                    scene ep12_np2_mjmc95 with dissolve
                    js "Maybe in another world, another time, another place..."
                    js "We'd walk hand in hand."
                    scene ep12_np2_mjmc93 with dissolve
                    mc "I'm sorry."
                    scene ep12_np2_mjmc95 with dissolve
                    js "It's alright, [name]... As it appears, we were never meant to be."
                    scene ep12_np2_mjmc94 with dissolve
                    $ renpy.pause()
                    scene ep12_np2_mjmc96 with dissolve
                    $ renpy.pause()
                else:
                    scene ep12_np2_mjmc91 with dissolve
                    
                    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Josy path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                    
                    menu:
                        "I want to be with you \n{size=-4}[m_c1][mod_choices[0]]":
                            $ roadJosy = True
                            mc "It's always been you, Josy. That's what I think, and that's how I feel."
                            scene ep12_np2_mjmc97 with dissolve
                            js "*{i}Smack{/i}*"
                            scene ep12_np2_mjmc98 with dissolve
                            $ renpy.pause()
                            scene ep12_np2_mjmc99 with dissolve
                            mc "But we should take it slow. Out of respect for Maya."
                            scene ep12_np2_mjmc100 with dissolve
                            js "I wholeheartedly agree."
                            js "I'm going to join her now... I want to end this night together with her."
                            scene ep12_np2_mjmc101 with dissolve
                            $ renpy.pause()
                        "I'm not available":
                            scene ep12_np2_mjmc93 with dissolve
                            jump ep12_np2_mjmc_label2
                $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
                $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
                if roadMaya:
                    $ new_bio("Josy", "During the New Year's Eve party, I decided to enter into a relationship with Josy.")
                    $ new_bio("You", "During the New Year's Eve party, I decided to enter into a relationship with Josy.")
        else:
            scene ep12_np2_mjmc74 with dissolve
            mc "Ok... I'm gonna let you have some space."
            $ new_bio("Josy", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
            $ new_bio("Maya", "Josy and Maya decided they wanted to be friends instead of in a relationship with each other.")
if roadSage and wt_ep9_branch_numbers == 1:
    jump ep12_sage_lewdb_label
else:
    jump ep12_np2_fw_label

label ep12_elena_lewd_label:
scene ep12_elena_prelewd1 with dissolve
el "[name]? Are you good to go?"
scene ep12_elena_prelewd2 with dissolve
mc "Sure am."
stop music fadeout 3
scene ep12_elena_prelewd3 with dissolve
jb "Aw, yeah! Let's fucking do this."

label ep12_elena_lewd2_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name

play music "music/ep2/jingle.mp3"
hide screen new_phone_screen
$ ep12_elena_lewd = True
scene ep12_elena_lewd1 with dissolve
mc "I have to ask again... Are you 100%% sure about this?"
scene ep12_elena_lewd2 with dissolve
jb "Bro... I had to walk here with a boner. You're not quitting on me now, are you?"
scene ep12_elena_lewd3 with dissolve
mc "I'm only making sure. You guys mean a lot to me. I wouldn't want to do something you'd regret tomorrow."
scene ep12_elena_lewd4 with dissolve
jb "The only thing I regret is that we didn't ask you sooner."
scene ep12_elena_lewd5 with dissolve
mc "Elena?"
scene ep12_elena_lewd6 with dissolve
el "Yeah?"
scene ep12_elena_lewd5 with dissolve
mc "Some reassurance would be nice."
scene ep12_elena_lewd6 with dissolve
el "This is a late Christmas gift to John Boy. We've talked about doing this for a long time."
el "I mean, not with you, but in general."
scene ep12_elena_lewd5 with dissolve
mc "And you want it too, yeah?"
scene ep12_elena_lewd4 with dissolve
jb "Trust me. She wants it."
scene ep12_elena_lewd7 with dissolve
jb "Look. I'm gonna sit in this corner. You guys do whatever you want over there."
jb "Don't mind me! I'm not even here."
scene ep12_elena_lewd8 with dissolve
mc "I'm sorry, but I'm gonna need to hear you say that you want this."
mc "And not just because it's a gift to him."
scene ep12_elena_lewd9 with dissolve
el "Will it feel weird to do this? Yeah, probably."
el "It's his fetish, not mine."
scene ep12_elena_lewd10 with dissolve
el "But John Boy doesn't see this as cheating, so neither should I."
el "And you shouldn't feel like you're an accessory to cheating either."
scene ep12_elena_lewd8 with dissolve
mc "You're still not saying it..."
scene ep12_elena_lewd9 with dissolve
el "[name]. It's not a simple yes-or-no answer you're asking for."
el "I want to do it, and I'll try my best to make John Boy enjoy it."
el "I'll get past the weird feeling in my stomach; I'm sure."
scene ep12_elena_lewd11 with dissolve
jb "Guys... Is it happening or what?"
scene ep12_elena_lewd10 with dissolve
el "It's up to [name]."
scene ep12_elena_lewd11 with dissolve
jb "Go on. Kiss her."
scene ep12_elena_lewd12 with dissolve
el "Merry Christmas, baby."
scene ep12_elena_lewd13 with dissolve
$ renpy.pause()
scene anim_elena_kiss_ep12 with dissolve
pause
scene ep12_elena_lewd14 with dissolve
$ renpy.pause()

scene ep12_elena_lewd16 with dissolve
$ renpy.pause()
scene ep12_elena_lewd15 with dissolve
$ renpy.pause()
scene anim_elena_hj1_ep12 with dissolve
el "*{i}Smack smack{/i}*"
pause
scene anim_elena_hj2_ep12 with dissolve
pause
scene ep12_elena_lewd18 with dissolve
$ renpy.pause()
scene ep12_elena_lewd17 with dissolve
$ renpy.pause()
scene ep12_elena_lewd19 with dissolve
$ renpy.pause()
scene ep12_elena_lewd20 with dissolve
$ renpy.pause()
scene ep12_elena_lewd21 with dissolve
$ renpy.pause()
scene ep12_elena_lewd22 with dissolve
$ renpy.pause()
scene ep12_elena_lewd23 with dissolve
$ renpy.pause()
scene ep12_elena_lewd25 with dissolve
el "Eat me, [name]."

scene anim_elena_lick1_ep12 with dissolve
mc "*{i}Lick lick{/i}*"
pause
scene anim_elena_lick2_ep12 with dissolve
el "*{i}Moans{/i}* Hngn... Yes... Ahh..."
pause

scene ep12_elena_lewd26 with dissolve
mc "Um... Do you want me to wear a condom?"
scene ep12_elena_lewd27 with dissolve
el "Only if you want to."
scene ep12_elena_lewd26 with dissolve
mc "No, I'm good."
scene anim_elena_bj1_ep12 with dissolve
el "*{i}Suck suck{/i}*"
pause
scene anim_elena_bj2_ep12 with dissolve
mc "Your lips feels amazing around my cock."
el "*{i}Glug glug{/i}*"
pause

scene ep12_elena_lewd28 with dissolve
$ renpy.pause()
scene ep12_elena_lewd29 with dissolve
el "*{i}Whispers{/i}* Go easy on me... I've never had one of your size."
scene ep12_elena_lewd28 with dissolve
mc "Let me know if I'm doing something you don't like. I wanna try making you cum..."
el "Haha... I like that ambition, but I'm not sure if you'll be able to-"
scene bg anim_elena_insert_ep12 movie with hpunch
el "*{i}Moans{/i}* Holy... Ahh..."
mc "Is it good?"
el "Ahh... So, this is how it feels like? Wow... Amazing."
pause

scene anim_elena_miss1_ep12 with dissolve
el "*{i}Moans{/i}* Yes... Fuck... Mmm...."
pause
scene anim_elena_miss2_ep12 with dissolve
mc "You feel so good."
el "I'm so fucking wet, [name]. Haha..."
mc "I can tell. It's sexy as hell."
pause
scene anim_elena_miss3_ep12 with dissolve
mc "Is the pace alright?"
el "*{i}Moans{/i}* Mmm... You're fucking me just right."
pause

$ tmpInt = 0
$ tmpBool = False
label ep12_elena_lewd_loop_label:

menu:
    "Missionary":
        $ tmpInt += 1
        scene anim_elena_miss1_ep12 with dissolve
        el "*{i}Moans{/i}*"
        pause
        scene anim_elena_miss2_ep12 with dissolve
        el "*{i}Moans{/i}* Fuck me, [name]."
        pause
        scene anim_elena_miss3_ep12 with dissolve
        pause
        jump ep12_elena_lewd_loop_label
    "Prone":
        $ tmpInt += 1
        scene anim_elena_prone1_ep12 with dissolve
        el "Yes... Hngn... It's so good. Fuck me hard, [name]."
        pause
        scene anim_elena_prone2_ep12 with dissolve
        mc "Mmm... I love your ass."
        pause
        scene anim_elena_prone3_ep12 with dissolve
        el "Yes... Yes... Keep going! Don't stop..."
        pause
        if not tmpBool:
            $ tmpBool = True
            scene ep12_elena_lewd46 with hpunch
            el "Ahhh! FUCK!!!"
            scene ep12_elena_lewd46 with hpunch
            el "*{i}Moans{/i}* YES!!!"
            scene ep12_elena_lewd47 with hpunch
            el "*{i}Moans{/i}* Fuck, [name]... You just made me cum so hard..."
        jump ep12_elena_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_elena_rev1_ep12 with dissolve
        el "I love how deep inside me you're getting."
        mc "I'm surprised you can take it all that easily."
        pause
        scene anim_elena_rev2_ep12 with dissolve
        el "At first, it felt like I was expanding in all directions, but now I've gotten used to it."
        mc "As long as it doesn't hurt."
        el "*{i}Moans{/i}* Hurt? It feels incredible."
        pause
        scene anim_elena_rev3_ep12 with dissolve
        el "*{i}Moans{/i}* Ahh! Yes... Yes..."
        pause
        jump ep12_elena_lewd_loop_label
    "Blowjob":
        $ tmpInt += 1
        scene anim_elena_bj3_ep12 with dissolve
        el "*{i}Suck glug glug{/i}*"
        mc "Fuck, you're pretty much deepthroating it."
        pause
        scene anim_elena_bj4_ep12 with dissolve
        el "*{i}Suck suck{/i}* Mmmpfff..."
        pause
        jump ep12_elena_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_elena_ride1_ep12 with dissolve
        mc "Fuck, yes. Ride me, Elena."
        el "Oh, [name]... Hngn..."
        pause
        scene anim_elena_ride2_ep12 with dissolve
        mc "Yeah... Take it all the way. You're loving it, aren't you?"
        el "Yes... I love it!"
        pause
        scene anim_elena_ride3_ep12 with vpunch
        el "*{i}Moans{/i}* Ahh!!! Ahh!!! I'm cumming!!!"
        pause
        scene anim_elena_ride4_ep12 with vpunch
        el "Fuck, [name]! FUCK!!!"
        pause
        jump ep12_elena_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_elena_doggy1_ep12 with dissolve
        el "Yes! Fuck me! Make me feel that big cock."
        pause
        scene anim_elena_doggy2_ep12 with dissolve
        el "God damn! You're so good! Wow! Ahhh..."
        pause
        jump ep12_elena_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "Elena, I'm gonna cum!"
        menu:
            "In mouth":
                scene anim_elena_bj4_ep12 with dissolve
                el "*{i}Suck suck glug{/i}*"
                pause
                scene ep12_elena_lewd30 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_elena_lewd30 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_elena_lewd30 at vpunch, cum1
                mc "Ahh!!!"
                scene ep12_elena_lewd31 with dissolve
                $ renpy.pause()
                scene ep12_elena_lewd32 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_elena_bj3_ep12 with dissolve
                el "*{i}Suck suck glug{/i}*"
                pause
                scene ep12_elena_lewd33 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd33 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd33 at vpunch, cum2
                mc "Ahh!!!"
                scene ep12_elena_lewd34 with dissolve
                $ renpy.pause()
            "On ass":
                scene anim_elena_prone3_ep12 with dissolve
                el "Cum all over my ass, [name]. Paint it with your cum!"
                pause
                scene ep12_elena_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd35 at vpunch, cum2
                mc "Ahh!!!"
                scene ep12_elena_lewd36 with dissolve
                $ renpy.pause()
            "Body shot":
                scene anim_elena_miss1_ep12 with dissolve
                el "Cum all over me, [name]. Paint me with your cum!"
                pause
                scene ep12_elena_lewd37 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd37 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_elena_lewd37 at vpunch, cum2
                mc "Ahh!!!"
                scene ep12_elena_lewd38 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_elena_ride2_ep12 with dissolve
                el "Cum inside me, [name]. Give me that creampie..."
                pause
                scene ep12_elena_lewd39 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_elena_lewd39 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_elena_lewd39 at vpunch, cum1
                mc "Ahh!!!"
                scene ep12_elena_lewd40 with dissolve
                $ renpy.pause()


stop music fadeout 3
scene ep12_elena_lewd41 with dissolve
el "Wow... That was..."
el "That was..."
play music "music/ep12/licensed_music/track204.mp3"
scene ep12_elena_lewd42 with dissolve
jb "That was the hottest thing I've ever seen."
jb "[name]... Thank you!"
scene ep12_elena_lewd43 with dissolve
mc "Um... You're welcome?"
scene ep12_elena_lewd42 with dissolve
jb "I'm gonna have to ask you to leave now."
scene ep12_elena_lewd43 with dissolve
mc "Sure... Let me just get dressed, and I'll see you guys tomorrow."
scene ep12_elena_lewd44 with dissolve
el "Oh, baby. After that, I don't have the energy for you, too."
jb "Forget about me! What I really want to know is how it was for you. Tell me all about it, babe."
scene ep12_elena_lewd45 with dissolve
mc "(This year got off to a weird start.)"
mc "(I loved the sex, but I'm gonna have to check in with Elena how she felt about it.)"
mc "(It was a weird situation for her, but she seemed to enjoy it.)"

$ renpy.end_replay()
$ persistent.ep12_lewd_elena = True
$ calcScenes()
$ new_bio("Elena", "I fucked Elena in front of John Boy during the New Year's Eve party.")
$ new_bio("John Boy", "I fucked Elena in front of John Boy during the New Year's Eve party.")
$ mphone_stats_add_girl_s3("elena","You had sex with Elena in her room in episode 12.")
show screen new_phone_screen
jump ep12_evaluation_label

label ep12_np_fem_event_label:
$ tmpInt = _preferences.get_volume("music")
$ renpy.sound.set_volume(0,channel="music")
$ renpy.sound.play("music/ep10/licensed_music/track146.mp3",channel="sfx2", loop=True)
scene ep12_np_fem_event1 with dissolve
$ renpy.pause()
scene ep12_np_fem_event2 with dissolve
dw "Can you feel that?"
scene ep12_np_fem_event3 with dissolve
$ renpy.pause()
scene ep12_np_fem_event4_fr0 with dissolve
$ renpy.pause(.5)
scene ep12_np_fem_event4 with hpunch
$ renpy.pause()
$ renpy.music.stop(channel="sfx2")
$ renpy.sound.set_volume(tmpInt,channel="music")
scene ep12_np_fem_event5
show screen dance_filter_screen
$ renpy.sound.play("sound_effects/season3/fem_rumble.mp3",channel="sfx3", loop=True)
with vpunch
mi "WOOOOOO!!!"
scene ep12_np_fem_event5 with vpunch
li "HAHAHA!"
$ renpy.music.stop(channel="sfx3")
$ renpy.music.stop(channel="sfx2")
jump endEvent

label ep12_c_enter_event_label:
hide screen new_phone_screen
hide screen map_screen
play music "music/ep12/redacted.mp3"
scene ep12_c_enter_event
show screen redacted_noise_screen
with dissolve
mc "(What the...? What is this place?)"
mc "(I don't think I'm supposed to be here.)"
$ currentFreeRoamLabel = "ep12_np_crypt_label"
jump endEvent

label ep12_m_event_label:

scene ep12_m_event with dissolve
mc "(What does this mean? It's written in some weird kind of language.)"
scene ep12_m_event2 with dissolve
mc "(There is some red paint near the symbols, but the symbols themselves seem to be written in a white substance.)"
scene ep12_m_event3 with dissolve
mc "(Hm... That's sweet.)"
scene ep12_m_event with dissolve
$ renpy.pause()
jump endEvent

label ep12_se_event_label:
scene ep12_se_event with dissolve
mc "(Hey... This one is not supposed to be here.)"

jump endEvent

label ep12_cr_event_label:
mc "(Maybe it's me, but something feels off when I touch things.)"
jump endEvent

label ep12_et_event_label:
mc "(What's that? A shaker?)"
jump endEvent

label ep12_c_event_label:
stop music
play sound "sound_effects/season3/redacted2.mp3"
scene ep12_c_event1
hide screen redacted_noise_screen
with vpunch
mc "AHH!!!"
scene ep12_c_event2 with dissolve
mc "(Huh!? What the hell?)"
show screen new_phone_screen
$ mphone_music_genre = 2
$ mphone_next_song()
scene ep12_c_event3 with dissolve
mc "(I must have passed out... No more alcohol for me tonight.)"
$ ep12_jewels.append("DONE")
$ currentFreeRoamLabel = "ep12_np_party_balcony_label"
hide screen redacted_noise_screen
jump endEvent

screen redacted_noise_screen:
    tag redacted_noise_screen
    modal False
    add "redacted_noise"
    add "redacted_symbols"

image redacted_noise:
    choice:
        "red_noise1"
    choice:
        "red_noise2"
    choice:
        "red_noise3"
    choice:
        "red_noise4"
    pause 0.1
    repeat

image redacted_symbols:
    linear 1 alpha 0
    choice:
        "red_sym1"
    choice:
        "red_sym2"
    choice:
        "red_sym3"
    choice:
        "red_sym4"
    choice:
        "red_sym5"
    choice:
        "red_sym6"
    choice:
        "red_sym7"
    choice:
        "red_sym8"
    choice:
        "red_sym9"
    choice:
        "red_sym10"
    choice:
        "red_sym11"
    choice:
        "red_sym12"
    choice:
        "red_sym13"
    choice:
        "red_sym14"
    choice:
        "red_sym15"
    choice:
        "red_sym16"
    choice:
        "red_sym17"
    choice:
        "red_sym18"
    choice:
        "red_sym19"
    choice:
        "red_sym20"
    choice:
        "red_sym21"
    choice:
        "red_sym22"
    choice:
        "red_sym23"
    choice:
        "red_sym24"
    choice:
        "red_sym25"
    choice:
        "red_sym26"
    choice:
        "red_sym27"
    choice:
        "red_sym28"
    choice:
        "red_sym29"
    choice:
        "red_sym30"
    choice:
        "red_sym31"
    choice:
        "red_sym32"
    choice:
        "red_sym33"
    choice:
        "red_sym34"
    choice:
        "red_sym35"
    choice:
        "red_sym36"
    choice:
        "red_sym37"
    choice:
        "red_sym38"
    choice:
        "red_sym39"
    choice:
        "red_sym40"
    choice:
        "red_sym41"

    linear 1 alpha 0.1

    choice:
        pause 0.1
    choice:
        pause 0.4
    choice:
        pause 0.8
    choice:
        pause 1.2
    choice:
        pause 2.0
    repeat

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

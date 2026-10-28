label startUpdate9:
jump header_ep9_label
label previousEp9Label:
$ guideSuggestedPage = 44
play music "music/patched/track_previous2.mp3"
scene black
$ renpy.pause(2)
hide screen new_phone_screen
$ previousEpLabel = "startUpdate9b"
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen

scene bg anim_ending_zoey_ep8 movie with dissolve
mc "I've been in one relationship. I don't want to talk about that."
my "Ended poorly, huh?"
mc "I didn't see her as a girlfriend until we said our goodbyes to each other."

scene ep5_return21 with wipeleft
rs "Dildos... Alphas."
jac "They fucking trashed everything!"

if ep5_agitatedCaleb:
    scene ep5_ending18i
else:
    scene ep5_ending18i2
mc "This isn't how a normal fraternity works."
scene ep5_ending20
mc "We slowly rebuild this place. Piece by piece. Together."

scene ep6_mansion_eve8
le "It's hard work, but we're a pretty big team."

scene ep8_rusty21
rs "I don't think we've earned enough to pay for the windows."
if ep8_mansion_won:
    scene ep8_rusty20
    mc "Dude... We're in the clear!"
else:
    scene ep8_rusty24
    mc "Yeah... We aren't where we need to be."
    scene ep8_ending2d
    rs "I'm glad I listened to Tommy..."
    scene ep8_ending2e
    rs "He told me we needed a plan B."

scene ep5_qt9 with wipeleft
tm "Because of you, our maggots' big night was ruined."
scene ep5_qt14
tm "You're not worth shit to me anymore."
scene ep6_after_fight20
tm "They may be the only sorority, but we'll still throw big parties without them."

scene ep8_pr_drugs7
ly "Vinny can't find out that we're changing dealers."
scene ep8_tommy_lily9
tm "Where do you score your weed?"
scene ep8_tommy_lily13
ly "Vinny and your burned bridge..."
scene ep8_tommy_lily14
ly "I can get you some extra from her if you're that desperate."

scene ep8_diks_tommy_event_2nd3
mc "We're gonna host parties again, starting with Halloween."
scene ep8_ending11
tm "I'm still in charge of the party planning, but you can help out."
scene ep8_ending11b
$ renpy.pause()
scene ep8_ending11c
$ renpy.pause()

scene ep8_math22b with wipeleft
de "You know Ashley? I kinda like her."
scene ep8_math22c
de "My gut is telling me to give up on her and move on..."
scene ep8_lq76
de "...but it's hard."

if not pathMayaJosy:
    scene ep5_burn84 with wiperight
    de "And all feelings for my sis and Josy, they are gone just like that?"
    if ep5_feelingsForJosy:
        scene ep7_jmc20
        mc "I still have feelings for Josy..."
    elif ep5_feelingsForMaya:
        scene ep7_mj33
        mc "I still have feelings for your sis..."
    else:
        scene ep5_burn81
        mc "Yeah. I think so."
else:
    scene ep5_burn55 with wipeleft
    mc "Josy and your sis... I'm a part of their relationship."
    scene ep5_mj_hang
    de "They agreed to this?"
    scene ep5_mj_day40
    my "I think it's best if there are no strings attached yet. For any of us."

if ep8_recital_failed:
    scene ep8_failed_recital129c
else:
    scene ep8_recital_play117d
mc "(Not long ago, I didn't know these people, and now we've grown quite close.)"

scene ep8_breakfast48
el "It's better to choose. If things are serious between you, you already know who you want to be with."

if branchIsabella:
    scene ep8_breakfast_bella2
    mc "(All I can think about right now...is Bella.)"
    scene ep8_bd56
    isa "What are your feelings for Jill?"
    scene ep8_bd61
    mc "I won't date her anymore. But I haven't told her that."
    scene ep8_bella_morning59
    mc "I want to date you, Bella."
    scene ep8_bella_morning64
    isa "I'm in the same boat as you."
    if ep8_jill_state == 1:
        scene ep8_bella_morning67
    else:
        scene ep8_bella_morning66
    isa "I'll have to tell her about us too."
elif branchSage:
    scene ep8_breakfast_sage6
    mc "(I want to see where it goes with Sage...)"
    scene ep8_sage_walk33
    mc "Long-term, I want more than to be friends with you."
    scene ep8_sage_walk30
    sa "Fine. I'll go out on a date with you."
    scene ep8_sage_walk35
    $ renpy.pause()
elif branchMayaJosy:
    scene ep8_breakfast_mj1
    mc "(Josy and Maya... I want to be with them...)"
elif branchJill:
    scene ep8_breakfast_jill6
    mc "(Jill is the one I want.)"
    scene ep8_jdate70
    mc "Let's be scared together... Let's give us a try."
    scene ep8_jill_lewd139
    ji "We actually did it."
    scene ep8_jill_lewd144
    scene ep8_jill_lewd145 with Dissolve(4)
    ji "[name], do you believe in destiny?"
    ji "I believe it's all connected somehow."
else:
    if ep8_jill_rejected_you:
        scene ep8_breakfast_jill6
        mc "(I wanna see where it goes with Jill.)"
        scene ep8_jdate50
        if not ep6_jill_lewd:
            ji "[name]... I'm sorry... The spark's not there for me."
        else:
            ji "[name]... I'm sorry... You're not what I'm looking for."
    else:
        scene ep8_breakfast29c
        mc "(Maybe I'll want a relationship someday, but it's not today.)"

scene ep3_office2 with wipeleft
sb "I'm Professor Stephen Burke..."
scene ep3_office_chad_jade
sb "...this is my wife, Dr. Jade Burke."
scene ep2_gender_after20
ja "If there's ever an odd couple in the class you and I could pair up and have a good..."
scene ep3_gender_jade4
ja "...back and forth."

if ep3_acceptedJade:
    scene ep3_jade_student8
    mc "(Let's find out if she's serious or not.)"
    if ep4_jadeOffer:
        scene ep4_gender_jade21
        ja "Not here... Tonight... The school parking lot at 10 p.m."
        if ep4_rejectedJade:
            scene ep4_josy_maya_talk72
            js "Haha! What the hell are we doing?"
            my "We are following our hearts!"
            play sound "sound_effects/burnout.mp3"
            scene ep4_rejected_jade3 with dissolve
            $ renpy.pause()
        else:
            scene ep4_jade_lewd76
            ja "Pound me as hard as you fucking can!"
            if ep4_toldDerekAboutJade:
                scene ep6_mj_dorm24b
                ja "Are you sure you're capable of keeping this secret?"
                scene ep6_mj_dorm24c
                mc "Yeah."
else:
    scene ep3_gender_jade4b
    mc "(Is she crazy!?)"
    scene ep3_gender_jade4c
    ja "You should spend the time left in this class reading and be {b}quiet{/b}..."
    ja "That way I might not fail you..."


scene ep3_mansion72
ty "Jill, please! This student has no business in the mansion."
ty "Get security to show this boy out."
scene ep3_mansion80
mc "Jill."
scene ep3_mansion85
mc "Would you like to go out on a date with me?"

scene ep5_water22
ty "Why are you within our gates?"
play sound "sound_effects/slap.mp3"
scene ep5_water24 with hpunch
ty "Get off my property, you filthy and disgusting loser."
if ep5_punchedTybalt:
    scene bg anim_punch_ep5r movie
    $ renpy.pause(4)

scene ep5_bella_night56
ji "There was a fire at the mansion!"
scene ep6_jt11
ty "Your \"friend\" caused all of it."


scene ep7_pre_tennis26
ji "Are we ready for some doubles?"
scene ep7_pre_tennis36
ty "*{i}Mumbles{/i}* I'll show you, you ugly-faced, wearing rags piece of filth."

if ep7_tybalt_state == 2:
    play sound "sound_effects/tennis_hit.mp3"
    scene bg anim_tybalt_smash3_ep7r movie with dissolve
    $ renpy.pause()
    scene ep7_tennis_tybalt_smashed12
    ji "Oh my God, Tybalt. Your teeth..."

scene ep7_shower14c
mc "Using me to get to Jill is not something a winner would do."
if ep7_tybalt_state == 2:
    scene ep7_shower3a
    ty "Shhe'sh warming up to me. I can feel it."
    ty "Meanwhile, have fun not sheeing her again."
else:
    scene ep7_shower3c
    ty "She's warming up to me. I can feel it."
    ty "Meanwhile, have fun not seeing her again."

if ep7_ruined_presentation:
    scene ep5_tybalts_phone
    mc "(Is that Tybalt's phone?)"
    scene ep5_tybalt_phone2
    mc "(Hahaha, he's totally gonna freak out!)"
    scene ep7_tyb_pres_dp
    if ep7_tybalt_state == 2:
        ty "Any queshtionsh so far?"
    else:
        ty "Any questions so far?"
    "*{i}Gasps{/i}* *{i}Chatter{/i}*"

scene ep8_jdate2
ty "Jill... Will you...marry me?"
scene ep8_jdate32
ji "No. I do {b}NOT{/b} want to marry you, and I am done playing along with this bullshit!"


scene ep7_sage_maya13 with wipeleft
sa "I want to help you, Maya."
scene ep7_sage_maya12
my "But you don't know what you'd be helping me with."

scene ep8_sage_walk8
sa "I talked to my dad about Maya."
scene ep8_ending22
sa "He wants to meet us next week to discuss it."
scene ep8_ending44
js "What the hell are we walking in on?"
scene ep8_ending48
mc "{i}Fuck.{/i}"
scene ep8_ending49
mc "{i}Fuck. Fuck. Fuck. Fuck.{/i}"

label startUpdate9b:
if steamConfig or nonPatreonConfig:
    if branchIsabella:
        $ state = "ep9_steam_isabella"
    elif branchSage:
        $ state = "ep9_steam_sage"
    elif branchMayaJosy:
        if ep8_maya_lewd:
            $ state = "ep9_steam_maya"
        else:
            $ state = "ep9_steam_josy"
    elif branchJill:
        $ state = "ep9_steam_jill"
    else:
        $ state = "ep9_steam_others"
else:
    if branchIsabella:
        $ state = "ep9_isabella"
    elif branchSage:
        $ state = "ep9_sage"
    elif branchMayaJosy:
        if ep8_maya_lewd:
            $ state = "ep9_maya"
        else:
            $ state = "ep9_josy"
    elif branchJill:
        $ state = "ep9_jill"
    else:
        $ state = "ep9_others"
call rpc from _call_rpc_1
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black
$ renpy.pause(0.5)

label ep9_intro_label:
show screen ep9_snow_screen
scene bg anim_intro_ep9 movie with fade
if persistent.seen_cutscene_ep9[0]:
    $ renpy.pause(64.67)
else:
    $ _skipping = False
    $ renpy.pause(64.67, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep9[0] = True
hide screen ep9_snow_screen
hide screen ep10_snow_queue_screen
$ renpy.music.stop(channel="music2", fadeout=0)
$ renpy.music.stop(channel="music", fadeout=0)
play sound "sound_effects/scare.mp3"
scene ep9_intro1 with vpunch
tm "BOO!"
show ep9_intro2
if not persistent.ep9_cardji5:
    show screen ep9_render_screen("ji5")
with dissolve
tm "Did I scare you?"
play music "music/ep9/licensed_music/track117.mp3"
jac "Dude... Where the fuck are your pants?"
show ep9_intro3
hide screen ep9_render_screen
with dissolve
tm "You barged in while I was getting dressed."
scene ep9_intro4 with dissolve
jac "We have a problem. I can't find the kegs."
scene ep9_intro6 with dissolve
tm "Ask [name]. He wanted to be a party planner, and he'll have to learn things the hard way."
scene ep9_intro4 with dissolve
jac "Huh? You don't know anything about it?"
scene ep9_intro6 with dissolve
tm "I told you. Ask [name]."
scene ep9_intro4 with dissolve
jac "Aight."
scene ep9_intro6 with dissolve
tm "What about the rest? Everything looks good?"
scene ep9_intro5 with dissolve
stop music fadeout 3
jac "For sure, it's one scary fucking mansion."


play music "music/ep9/licensed_music/track113.mp3"
scene bg anim_halloween_ep9 movie with dissolve
if persistent.seen_cutscene_ep9[1]:
    $ renpy.pause(65.33)
else:
    $ _skipping = False
    $ renpy.pause(65.33, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep9[1] = True
scene 2d_jacob_screen_main with dissolve
show screen episode_title_screen
stop music fadeout 5
$ renpy.pause(5)
play music "music/ep9/licensed_music/track117.mp3"
scene bg anim_pan_leon_ep9 movie with dissolve
$ renpy.pause(5)
scene ep9_intro7 with dissolve
tm "Oh, hell yeah! You came early!"
scene ep9_intro8 with dissolve
tm "Lily! You're such a hottie!"
play sound "sound_effects/whoosh.mp3"
scene ep9_intro9 with hpunch
le "Dude, shut up and don't touch me!"
scene ep9_intro10 with dissolve
tm "*{i}Retching noises{/i}* Leon!? What the fuck!?"
scene ep9_intro13 with dissolve
le "Have you seen Jamie? I have a bone to pick with him."
scene ep9_intro11 with dissolve
tm "Why the fuck are you dressed like a chick?"
scene ep9_intro13 with dissolve
le "It was Jamie's idea! And now he's fucking bailed on me."
scene ep9_intro12 with dissolve
tm "Hahaha! I gotta hand it to Jamie. That's a fucking good prank."
scene ep9_intro14 with dissolve
tm "Hey, wait, wait!"
tm "That's not the ladies' room!"
scene ep9_intro15 with dissolve
tm "Haha!"

scene ep9_intro16 with dissolve
rs "Slow down. Tell me again, what's the problem?"
scene ep9_intro19 with dissolve
mc "People are inviting themselves to our party."
scene ep9_intro17 with dissolve
rs "There will always be party crashers. That's what happens when you host a party."
scene ep9_intro20 with dissolve
mc "Tommy told me to fix it, even though I know he is responsible for the guest list."
mc "The same thing happened with the party budget. It was his responsibility, but it didn't add up at all."
scene ep9_intro16 with dissolve
rs "Aha... Ok... Well, take it up with Tommy again. I don't wanna get involved."
scene ep9_intro16b with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "You're not gonna help? [mod_gr][mod_choices[3]]":
        $ tmpInt = 1
        $ dk(1)
        scene ep9_intro20 with dissolve
        mc "Really? You're not gonna help out?"
        scene ep9_intro16 with dissolve
        rs "I thought we agreed on this already."
        scene ep9_intro20 with dissolve
    "I've got this [mod_gr][mod_choices[2]]":
        $ tmpInt = 2
        $ dk(-1)
        scene ep9_intro20 with dissolve
        mc "Ok... I've got this. It's just..."
mc "He told me I could plan the party and he even wanted to be my mentor, but he's treating me like I'm his slave."
scene ep9_intro17 with dissolve
rs "And this is why I'm out. Look, I'm thrilled you're throwing this party and thankful for all you did to make it work..."
rs "...but if Tommy wants to run this his way, it's up to him. Parties are his responsibility, and I don't wanna feel like I'm micromanaging everything."
rs "He accepted that I took charge when we fixed the mansion, just like I can accept that he's taking charge with parties when he wants to."
if tmpInt == 1:
    scene ep9_intro21 with dissolve
    mc "But the DIKs are a team."
    scene ep9_intro17 with dissolve
    rs "We are. And it's time you and Tommy act like it together."
    rs "You'll likely learn a lot from him if you give it a chance. He's thrown some amazing parties in the past."
    scene ep9_intro21 with dissolve
    mc "Right... I'm trying to learn from him, but he's being impossible."
else:
    scene ep9_intro21 with dissolve
    mc "Yeah, I get it. I do. But it's way different working with him than working with you."
    scene ep9_intro17 with dissolve
    rs "Tommy's got a lot to teach; I know it. He's thrown some amazing parties in the past."
    scene ep9_intro21 with dissolve
    mc "I don't doubt that, but I expected it to be easier."
scene ep9_intro22 with dissolve
jac "[name]! I can't find the kegs."
mc "Uh... Go ask Tommy."
jac "He told me to ask you. Do we have any kegs or not? We're gonna be short on beer."
scene ep9_intro18 with dissolve
rs "Relax. I ordered them. They should be here somewhere."
scene ep9_intro23 with dissolve
jac "You need to help me find them, bro."
if tmpInt == 1:
    scene ep9_intro24 with dissolve
    mc "Wait a second. This is Tommy's responsibility, too. Rusty, he's doing it again."
    scene ep9_intro16 with dissolve
    rs "I'm not getting involved."
else:
    scene ep9_intro22 with dissolve
    mc "*{i}Sigh{/i}* I'll handle it."
scene ep9_intro25 with dissolve
chr "How come you chose to be a vampire?"
scene ep9_intro27 with dissolve
tm "I'm not just a vampire; I'm Count Cockula!"
scene ep9_intro26 with dissolve
chr "Haha, ok. How come you chose to be Count Cockula?"
scene ep9_intro27 with dissolve
tm "Aside from having a big cock, I can't stand sunlight and I love to suck girls' necks."
scene ep9_intro28 with dissolve
chr "Hahah! Tommy! Stop that!"
mc "Tommy!"
scene ep9_intro29 with dissolve
tm "Bro... Are you wearing a skirt too? What's up with the DIKs tonight? Everyone has turned queer for Halloween."
scene ep9_intro30 with dissolve
mc "I'm not finished putting on my costume because I'm busy trying to solve your problems."
scene ep9_intro31 with dissolve
tm "What problems?"
scene ep9_intro30 with dissolve
mc "The uninvited guests, for one and, secondly, we can't find the kegs and we need them."
scene ep9_intro32 with dissolve
chr "There's no beer?"
scene ep9_intro33 with dissolve
tm "Zip it, crossdresser. My room, now."
scene ep9_intro34 with dissolve
tm "There's beer. You see, I'm his party planning mentor and he's having some learning disabilities."
tm "Grab a drink, and I'll be right back with you. Keep that neck warm for me."
scene ep9_intro35 with dissolve
tm "Look, you wanted to be a party planner. Admit you fucked up and need my help."
tm "It's fine, you know. Everyone makes mistakes."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "No mistakes [mod_gr][mod_choices[2]]":
        $ dk(-1)
        scene ep9_intro36 with dissolve
        mc "I haven't made any mistakes; everything's been going great until now, when everything seems to happen at once."
    "Blame Tommy [m_c2][mod_choices[3]]":
        $ dk(1)
        scene ep9_intro36 with dissolve
        if affinity == "DIK":
            mc "Yeah, I made the mistake of trusting you to help out. I should have known I couldn't count on you."
        else:
            mc "My only mistake is trusting you to do your tasks."
scene ep9_intro37 with dissolve
tm "I feel you. I do. You're dressed as a girl and can't handle the pressure. I get it. It's a big day for you."
scene ep9_intro38 with dissolve
mc "I'm trying to fix {b}your{/b} problems and you're not helping me."
scene ep9_intro37 with dissolve
tm "No, that's not what I remember. I clearly remember ordering you to do those things."
scene ep9_intro39 with dissolve
stop music fadeout 3
mc "Did not!"
tm "Did too!"

label ep9_party_planning_label:
play sound "<from 0.2>sound_effects/whoosh.mp3"
play music "music/ep6/licensed_music/track20.mp3"
queue music ["music/ep8/licensed_music/track68.mp3","music/ep7/good_old_days.mp3","music/ep6/licensed_music/track20.mp3"]
if ep8_elena_shot:
    scene ep9_party_planning7
    mc "You're amazing! Level 8008!? On Easy mode, right? How do you do that?"
    scene ep9_party_planning7b with dissolve
    el "No, it's Normal mode. It's pretty simple when you know a few tricks."
    el "But you have to be patient; it took me many hours and bathroom breaks to get to this level in Triple Tile."
    scene ep9_party_planning7c with dissolve
    mc "I don't think anyone can beat that."
else:
    scene ep9_party_planning7d
    $ renpy.pause()

scene ep9_party_planning8 with dissolve
tm "Did you invite the Pink Rose girls?"
if ep8_elena_shot:
    scene ep9_party_planning9 with dissolve
else:
    scene ep9_party_planning9b with dissolve

if not ep8_pink_rose_picture:
    mc "Uh... You said you were going to."
    if ep8_elena_shot:
        scene ep9_party_planning10 with dissolve
    else:
        scene ep9_party_planning10b with dissolve
    tm "Wrong. But I can do it if you can't handle it."
else:
    mc "I talked to Lily, and they'll be here."
    if ep8_elena_shot:
        scene ep9_party_planning10 with dissolve
    else:
        scene ep9_party_planning10b with dissolve
    tm "As guests or entertainment?"
    mc "Uh..."
    tm "I thought I told you to check, but I will do it if you can't handle it."
scene ep9_party_planning11 with dissolve
mc "I'm trying my best, but it's not easy throwing parties."
mc "When I planned with Sage and Quinn, we made some great decisions, but there's so much to consider when it comes down to the details."
scene ep9_party_planning12 with dissolve
mc "Like, will there be food? What kind of food? How do we decorate and did we get enough decorations? What's the schedule for activities gonna be like? Gah!"
scene ep9_party_planning13 with dissolve
tm "Damn, you seem even more lost doing this than I ever was."
if ep8_mansion_won:
    tm "How did you manage to get this place fixed again? I'm beginning to think Derek did all the heavy lifting."
else:
    tm "No wonder Rusty had to pay out of his pocket to fix this place."
scene ep9_party_planning12 with dissolve
mc "Since you've been doing this for a couple of years, will you help me?"
scene ep9_party_planning13 with dissolve
tm "Hey, you went around my back and started planning the party with the HOTs. I can't help you."
scene ep9_party_planning12 with dissolve
mc "As a surprise, dude. You didn't seem against it when I first told you."
scene ep9_party_planning14 with dissolve
tm "I'm not against the party, but I've been thinking a lot about what you did..."
tm "You waltzed into my office when I wasn't there, sat naked in my chair, and rubbed your balls all over it..."
tm "...and then started throwing papers around like a monkey, thinking that you did a job well done."
tm "And now, you're asking me to come back to work and clean up the mess you made."
scene ep9_party_planning12 with dissolve
mc "I heard you throw the best parties, and I want this party to be great, don't you?"
scene ep9_party_planning13 with dissolve
tm "You're gonna have to stick your nose a bit further up my ass than that."
scene ep9_party_planning12 with dissolve
mc "I have already asked for your help. Help me. Please?"
scene ep9_party_planning15 with dissolve
if affinity == "DIK":
    tm "I see potential in you. You remind me of a shittier version of me. So, I'll do it."
else:
    tm "I see potential in you. Not much, but a little. I'll be the bigger man with this one; I'll do it."
scene ep9_party_planning16 with dissolve
mc "Thanks...I guess."
scene ep9_party_planning15 with dissolve
tm "I'll be your mentor."
scene ep9_party_planning16 with dissolve
mc "My mentor?"
scene ep9_party_planning17 with dissolve
tm "I admit my efforts as your father were subpar. But can you blame me? I got stuck with the dud and didn't think you'd make it two days before giving up."
tm "But I'm not gonna be in college forever, and I want the DIK legacy to live on for centuries after I leave."
tm "So, I know that torches will have to be passed on, and someone will have to take care of the parties after me."
scene ep9_party_planning18 with dissolve
mc "Oh. I don't appreciate the dud part, but that's nice."
scene ep9_party_planning19 with dissolve
tm "Don't ruin it."
tm "I'm gonna teach you how it's done."
tm "So, you've made the big decisions already and now it's time for the details."
$ guideSuggestedPage = 45
tm "Ask yourself, what's most important when you're planning a party?"
scene ep9_party_planning20 with dissolve
menu:
    "The alcohol?":
        mc "That there's enough alcohol to go around?"
        scene ep9_party_planning21 with dissolve
        tm "Wrong!"
    "The girls?":
        mc "That there are plenty of girls there?"
        scene ep9_party_planning21 with dissolve
        tm "Good thinking, but wrong!"
    "The decorations?":
        mc "That the decorations are spot on?"
        scene ep9_party_planning21 with dissolve
        tm "Pff! Both gay and wrong!"
    "The food?":
        mc "That there's food for everyone?"
        scene ep9_party_planning21 with dissolve
        tm "Food? We're not looking to attract fatties with our parties. Wrong!"
tm "The most important thing about planning a party is realizing that even a perfect plan will fail, no matter what you do."
tm "It doesn't matter if the food sucks, if we run out of some liquor, or if the place looks like shit."
scene ep9_party_planning22 with dissolve
tm "The moment the party starts, everyone's gonna have a good time anyway because we're the fucking DIKs."
tm "Students love our parties! They get to drink at them! They think we're cool no matter what we do."
tm "If the decor is shit, they think we're being ironic. If we only serve vodka, they think it's a theme."
scene ep9_party_planning24 with dissolve
tm "If we order pizza last minute, they think we're awesome for \"caring about them being hungry\"."
scene ep9_party_planning23 with dissolve
mc "So, we shouldn't even plan the party?"
scene ep9_party_planning22 with dissolve
tm "I didn't say that. We're gonna plan, but if things don't work out, it's not a big deal."
scene ep9_party_planning23 with dissolve
mc "Ok, so you want me to be more relaxed about it?"
scene ep9_party_planning22 with dissolve
tm "Now you're getting it. You're always so fucking serious about shit, you need to dial it back."
tm "Planning a party, it's a form of art. Yin and yang! You need to strive for balance."
tm "A little bit of beauty inside of the shit, and a little bit of shit inside of the beauty."
scene ep9_party_planning23 with dissolve
mc "I never heard you talk like this before."
scene ep9_party_planning22 with dissolve
tm "Do you even know what makes a great party?"
scene ep9_party_planning23 with dissolve
mc "That everyone's having fun?"
scene ep9_party_planning22 with dissolve
tm "Yeah, you're not far off. Everyone should have fun."
tm "It's not gonna happen because alcohol always finds a way to ruin it for some, but it's what we should aim for."
tm "And when I say that everyone should have fun, I mean, the DIKs should have fun. A happy host means a great party, and seriously, fuck what the guests want."
scene ep9_party_planning26 with dissolve
tm "But you've gotta pick your battles. Someone might get disappointed by your choices, but there are other parties, and maybe you take care of them a bit extra next time."
scene ep9_party_planning27 with dissolve
mc "I see... I can't make everyone happy."
scene ep9_party_planning28 with dissolve
tm "You can try, but it might cost a lot more than we have a budget for, or there might not be room for it."
tm "Don't go blowing the budget early, though. The more money you save, the better the party activities will be."

scene ep9_party_planning27 with dissolve
mc "Right... The activities."
scene ep9_party_planning28 with dissolve
tm "The problem is that while the party might last all night, at some point people will get too drunk to wanna do the shit you've planned."
tm "Again, we need a balance!"
tm "And since I'm your mentor, I'll help you choose what we'll do for Halloween."
scene ep9_party_planning29 with dissolve
mc "Actually, I already talked to Sage and Quinn about this."
mc "We talked about having a best costume competition and maybe some blindfold games."
scene ep9_party_planning30 with dissolve
tm "Boring!"
scene ep9_party_planning29 with dissolve
mc "That's not boring."
scene ep9_party_planning30 with dissolve
tm "You need to learn, bro. So, I'm not gonna be a dick about this. I'll give you some options and you'll pick."
scene ep9_party_planning31 with dissolve
tm "Picture this! It's early on in the party. People are arriving and have started drinking. No one's dancing yet because they're not drunk."
tm "Everyone is walking around talking, checking each other out being like, \"What are you supposed to be tonight?\" and \"Damn, that's a nice costume\"."
tm "And now's the time for the first activity of the night. What should it be?"
scene ep9_party_planning32 with dissolve
mc "What are my options?"
scene ep9_party_planning33 with dissolve
tm "People are still sober, and they want to get drunk. A drinking competition would work."
tm "It will cost money since we're encouraging people to drink more. And it can backfire if someone gets too drunk and has to end the night early."
tm "If we wanna spend more money, we could have a body shot battle. That will surely get girls drunk, and it's pretty damn hot."
$ guideSuggestedPage = 46
$ pp_activity_choices = [2,2,1]
if not minigames:
    $ pp_nm_party_preference = [[0,0,0],[1,1,1],[2,0,1],[1,-1,1],[0,-1,0],[1,1,0],[-1,1,1],[0,2,0]]
    $ pp_nm_activity_description = [["Body Shots","Drinking Competition","Don't care","Any activity"],["Scary Stories","Haunted Mansion","Don't care","Any activity"],["CUM-petition","Don't care"]]
    $ currentActivity = 0
    $ pp_money = 20
else:
    $ pp_money = 20
scene ep9_party_planning32 with dissolve
if not minigames:
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
menu:
    "Body shots ($2)" if minigames or pp_money > 2:
        
        $ pp_money -= 2
        
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 0
        mc "Body shots sound fun. Let's do that one."
        scene ep9_party_planning33 with dissolve
        tm "All right. Lower your expectations for it, though. Think of it as a warm-up. Girls will still be sober and odds are they won't go too crazy."
    "Drinking competition ($1)" if minigames or pp_money > 1:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_money -= 1
        $ pp_activity_choices[0] = 1
        mc "I like that drinking competition idea. Let's do that one."
        scene ep9_party_planning33 with dissolve
        tm "Awesome. We'll adjust the budget for it."
        tm "People are gonna get wasted, for sure."
    "No activity":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 2
        mc "Let's save some money instead. Let people talk and have fun on their own for the first part of the night."
        scene ep9_party_planning34 with dissolve
        tm "Our parties aren't remembered for being boring. Things need to happen to make them fun."
        tm "We can save some money here as long as we do something fun later on."

scene ep9_party_planning31 with dissolve
tm "Now, it's the middle of the party and most people have shown up. Many are drunk and the others are working on it."
tm "People are in the mood to dance and have fun, and their inhibitions are lowered. What do we do?"
scene ep9_party_planning33 with dissolve
tm "And before you go asking me for advice again, let me say what I think."
tm "We should get dirty and naughty."
scene ep9_party_planning32 with dissolve
mc "Sure. So, what about that blindfold game I mentioned?"
scene ep9_party_planning34 with dissolve
tm "It's decent, but it's not for Halloween. Why would we? It's much better suited for a panty party or something."
scene ep9_party_planning32 with dissolve
mc "Panty parties? We have those?"
scene ep9_party_planning33 with dissolve
tm "You've got a lot to learn."
tm "Many will be dancing, but for the ones who aren't, I say, huddling up and telling scary stories or having some haunted mansion tour where you have to work close to each other."
scene ep9_party_planning32 with dissolve
mc "Let's do that, then. All of it is free, no?"
scene ep9_party_planning34 with dissolve
tm "That's naive; it's not free. And the real issue is that we won't have time or space to do all of it."
scene ep9_party_planning32 with dissolve
if not minigames:
    $ currentActivity = 1
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        
                        if branchSage:
                            $mod_choices[10]="(Later Sage scene)"
menu:
    "Telling scary stories":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 0
        mc "Let's do the storytelling, then."
        scene ep9_party_planning33 with dissolve
        tm "That will work. While active people wanna dance, lazy asses can sit and tell stories."
    "Haunted mansion ($2) [mod_gr][mod_choices[10]]" if minigames or pp_money > 2:
        $ pp_money -= 2
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 1
        mc "Let's do dancing and the haunted mansion thingy."
        scene ep9_party_planning33 with dissolve
        tm "Yeah, whatever. Make sure you put someone in charge of that haunted mansion tour. It will cost some money."
    "Only dancing":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 2
        mc "Let's stick to dancing only. It's hot enough."

scene ep9_party_planning36 with dissolve
tm "Ok, we're almost done."
tm "It's late in the party. Some people will start dropping off soon, while others might stay until morning."
tm "Most people are wasted by now. It's the last chance to do something before people don't care about activities."
tm "Hell, some might be off fucking or puking."
scene ep9_party_planning33 with dissolve
tm "Strippers are gonna be here, and while you might think it's enough that they came to party, I wanna get my dick some action."
tm "I wanna have a private CUM-petition, so make a budget for it."
scene ep9_party_planning32 with dissolve
mc "What about the best costume competition?"
scene ep9_party_planning34 with dissolve
tm "Ok, do that one, but don't involve me in it."
scene ep9_party_planning32 with dissolve
if not minigames:
    $ currentActivity = 2
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
menu:
    "CUM-petition ($5)" if minigames or pp_money > 4:
        $ pp_money -= 5
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 0
        mc "Ok, I think we have money to spare for the CUM-petition."
        scene ep9_party_planning33 with dissolve
        tm "See, that's how you do it!"
    "No CUM-petition":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 1
        mc "Sorry, but the budget doesn't cover the CUM-petition."
        scene ep9_party_planning34 with dissolve
        tm "Are you fucking kidding me!?"
        tm "Fuck it. I'm still gonna have it. Guess I won't invite any of you to it."

if minigames:
    tm "Ok. Let's start with that, but change your mind if you need to."
    stop music fadeout 3
    tm "Go ahead. Let me see you do it for the Halloween party."
    tm "How would you make the DIKs happy?"
    $ tmpMenu = quick_menu
    $ quick_menu = 0
    play music "music/ep9/diks_spooky_halloween.mp3"
    queue music ["music/ep6/skeleton_keys.mp3","music/ep6/the_crown.mp3","music/ep8/licensed_music/track94.mp3","music/ep9/diks_spooky_halloween.mp3"]
    scene ep9_party_planning32 with dissolve
    show screen pp_intro_screen
    $ renpy.pause(1.5)
    $ renpy.play("sound_effects/slash.mp3", "sfx2")
    $ renpy.sound.play("sound_effects/rain_outside.mp3", channel="sfx3", loop=True)
    $ renpy.pause(1.5)
    play sound "sound_effects/season2/thunder2.mp3"
    $ renpy.pause(2)
    pause

    label ep9_skip_tut_label:
    $ renpy.pause(1.0)
    $ renpy.music.stop(channel="sfx3", fadeout=3)
    hide screen pp_intro_screen
    hide screen specialmsg
    jump ep9_skip_tutorial_label
    label ep9_play_tut_label:
    $ renpy.pause(1.0)
    $ renpy.music.stop(channel="sfx3", fadeout=3)
    hide screen pp_intro_screen
    hide screen specialmsg
    label ep9_pp_tutorial_label:
    $ persistent.pp_tutorial = 1

    $ pp_tut_state = 0
    $ pp_tut_multiplier = 1.25
    $ pp_tut_money = 20
    $ renpy.block_rollback()
    scene ep9_party_planning25
    call screen pp_tutorial_screen
    $ renpy.block_rollback()

    label ep9_skip_tutorial_label:
    $ tmp_list = [-1,-1]
    $ pp_continue_label = "ep9_pp_continue_label1"
    $ pp_tut_state = 0
    show pp_sky at pp_sky_transform_ep9
    show screen party_planner_item_perk_screen
    hide screen pp_tutorial_screen
    pause
    label ep9_pp_continue_label1:
    show pp_pumpkin_bg

    $ pp_round = 1
    $ pp_continue_label = "ep9_pp_cont_label"
    $ renpy.block_rollback()
    jump party_planner_setup_round_label

    label ep9_pp_cont_label:
    stop music fadeout 3
    $ quick_menu = tmpMenu
    scene ep9_party_planning26 with dissolve
    mc "Maybe like that?"
    $ tmpInt = 0
    python:
        for y in pp_needs_met[7]:
            if y:
                tmpInt += 1
    if tmpInt == 4:
        tm "I don't know how well you'd have done without my help, but definitely not this good. Let's give it a go, but I expect the plan to fail anyway."
    elif tmpInt > 2:
        tm "Ok. It's decent. Not the best, but let's give it a go because the plan will fail anyway."
    else:
        tm "Meh. Kind of shitty, to be honest, but it doesn't matter because the plan will fail anyway."
    scene ep9_party_planning32 with dissolve
else:
    scene ep9_party_planning32 with dissolve
    label ep9_lock_in_label:
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
            mc "That's it, then."
        "Start over":
            hide screen pp_nm_happiness_screen
            $ currentActivity = 0
            $ pp_money = 8
            show screen pp_dik_preferences_screen
            menu:
                "Body Shots ($2)":
                    $ pp_money = 6
                    $ pp_activity_choices[0] = 0
                "Drinking Competition ($1)":
                    $ pp_money = 7
                    $ pp_activity_choices[0] = 1
                "No activity":
                    $ pp_activity_choices[0] = 2
            $ currentActivity = 1
            menu:
                "Telling scary stories":
                    $ pp_activity_choices[1] = 0
                "Haunted Mansion ($2)":
                    $ pp_money -= 2
                    $ pp_activity_choices[1] = 1
                "Only dancing":
                    $ pp_activity_choices[1] = 2
            $ currentActivity = 2
            menu:
                "Private CUM-petition ($5)" if pp_money > 4:
                    $ pp_money -= 5
                    $ pp_activity_choices[2] = 0
                "No CUM-petition":
                    $ pp_activity_choices[2] = 1
            hide screen pp_dik_preferences_screen
            jump ep9_lock_in_label

if pp_activity_choices[0] == 0:
    $ ep9_body_shots = True
elif pp_activity_choices[0] == 1:
    $ ep9_drinking_competition = True
if pp_activity_choices[1] == 0:
    $ ep9_scary_stories = True
elif pp_activity_choices[1] == 1:
    $ ep9_haunted_mansion = True
if pp_activity_choices[2] == 0:
    $ ep9_cumpetition = True

if minigames:
    python:
        for x in range(0,len(pp_needs_met)):
            tmpInt = 0
            for y in pp_needs_met[x]:
                if y:
                    tmpInt += 1
            pp_current_party_happiness[x] = tmpInt

$ mphone_stats_unlocked_state = 1
mc "I'll talk to Sage again about the costume competition."
scene ep9_party_planning34 with dissolve
tm "Yeah, whatever."
tm "That's it for planning. Any thoughts?"
scene ep9_party_planning32 with dissolve
mc "It's gonna be a fun party."
scene ep9_party_planning37 with dissolve
tm "It better be, or it will be the last one you'll plan."
mc "So, can you be responsible for some of these?"
tm "Yeah, I'll do some of it."
show ep9_party_planning38
if not persistent.ep9_cardji6:
    show screen ep9_render_screen("ji6")
with dissolve
mc "Great. I'll take food, music and check with the guys about helping out, and you can take care of beer and help with the guest list, maybe?"
stop music fadeout 3
mc "Tommy?"

show ep9_party_planning1
hide screen ep9_render_screen
with dissolve
play music "music/ep9/licensed_music/track117.mp3"
mc "I told you to take care of it."
scene ep9_intro37 with dissolve
tm "Look. Do you need me to take care of it or not?"
scene ep9_party_planning1 with dissolve
mc "Yes."
scene ep9_intro37 with dissolve
tm "Say the magic words."
if affinity == "DIK":
    scene ep9_intro38 with dissolve
    mc "Fuck. You."
else:
    scene ep9_party_planning2 with dissolve
    mc "Please, Tommy. Help me find the kegs."
play sound "sound_effects/shower_curtain.mp3"
scene ep9_party_planning3 with hpunch
if affinity == "DIK":
    tm "Found them. Now you can stop being a baby."
else:
    tm "Found them."
scene ep9_party_planning4 with dissolve
tm "The guest list doesn't matter, either. Uninvited guests always show up."
tm "It's cool if they do. The only exceptions are jocks, preps and nerds; kick them out if they show up."
scene ep9_party_planning6 with dissolve
mc "You had the beer all this time?"
scene ep9_party_planning4 with dissolve
tm "I'm trying to teach you a lesson."
scene ep9_party_planning6 with dissolve
mc "Is the lesson that I can't trust you?"
scene ep9_party_planning5 with dissolve
tm "Eh, shut up. Go put on the matching bra to your outfit."
stop music fadeout 3
tm "I have some necks to suck."
$ new_bio("Tommy", "Tommy wanted to plan the party with me, but he's not doing what we agreed on.")

label ep9_derek1_talk_label:
scene ep9_derek1_talk1 with dissolve
play music "music/ep9/licensed_music/track118.mp3"
de "[mc_de_up]! There you are. I've been meaning to ask you something."
scene ep9_derek1_talk2 with dissolve
mc "Hey! Sorry, I'm a bit all over the place right now. What do you need?"
scene ep9_derek1_talk3 with dissolve
de "First off, what the fuck are you wearing?"
scene ep9_derek1_talk4 with dissolve
mc "Yes, I'm wearing a skirt. I got interrupted while putting on my outfit."
scene ep9_derek1_talk5 with dissolve
de "Are you kidding? The party's already started!"
scene ep9_derek1_talk4 with dissolve
mc "Yeah, and I've been running around trying to put out fires. Party planning isn't as much fun as I thought it would be."
mc "It's super-stressful!"
scene ep9_derek1_talk5 with dissolve
de "Chill out. Come, have a beer with me."
scene ep9_derek1_talk6 with dissolve
mc "Thanks... It's the first one of the night."
scene ep9_derek1_talk7 with dissolve
de "Drink up and you'll feel better soon."
scene ep9_derek1_talk8 with dissolve
mc "You went with astronaut, huh?"
scene ep9_derek1_talk9 with dissolve
de "No. I'm an ASS-tronaut."
scene ep9_derek1_talk10 with dissolve
mc "Funny. That looks like an expensive outfit."
scene ep9_derek1_talk9 with dissolve
de "It wasn't too much. Still, it's Halloween! I'm gonna win that best costume contest, hands down."
scene ep9_derek1_talk10 with dissolve
mc "Haha, we'll see what the judges say about that."
scene ep9_derek1_talk7 with dissolve
de "You're one of them, aren't you?"
scene ep9_derek1_talk8 with dissolve
mc "Yeah. It's gonna be me, Sage and Quinn."
$ guideSuggestedPage = 49
scene ep9_derek1_talk7 with dissolve
de "Great. That's one out of three votes."
scene ep9_derek1_talk8 with dissolve
menu:
    "Don't count on it":
        mc "Don't count on it."
        scene ep9_derek1_talk11 with dissolve
        de "You don't have my back?"
        scene ep9_derek1_talk10 with dissolve
        mc "I can't vote on my buddy, can I?"
        scene ep9_derek1_talk9 with dissolve
        de "Of course, you can!"
        scene ep9_derek1_talk10 with dissolve
        mc "I'm gonna try to be fair."
        scene ep9_derek1_talk9 with dissolve
        de "I guess I'm gonna have to bribe you then."
        scene ep9_derek1_talk10 with dissolve
    "Maybe":
        mc "Yeah, maybe. I'm gonna try to be fair."
    "Joke":
        mc "Why? Is Sage voting for you?"
        scene ep9_derek1_talk11 with dissolve
        de "[mc_de_up]! What the fuck?"
        scene ep9_derek1_talk10 with dissolve
mc "You wanted to ask me something?"
scene ep9_derek1_talk12 with dissolve
de "Yeah... Speaking of feeling stressed... I've noticed you've felt that a lot lately. And not just about the party planning."
scene ep9_derek1_talk13 with dissolve
mc "*{i}Sigh{/i}* Thanks for noticing. No, it's been rough."
scene ep9_derek1_talk12 with dissolve
de "So, what's up about that?"
scene ep9_derek1_talk13 with dissolve
mc "Where the fuck should I begin?"
stop music fadeout 3
mc "I guess it started at the Burkes..."

label ep9_burkes_label:
play music "music/ep6/licensed_music/track21.mp3"
$ jade_state = 0
if ep4_fuckedJade and not ep6_reject_jade:
    if branchAlone:
        $ jade_state = 1
    else:
        $ jade_state = 2
else:
    if (ep4_fuckedJade and ep6_reject_jade) or (ep3_acceptedJade and not ep4_fuckedJade):
        $ jade_state = 3
    else:
        $ jade_state = 0

scene ep9_burkes1 with dissolve
$ renpy.pause()
scene ep9_burkes2 with dissolve
$ renpy.pause()
scene ep9_burkes3 with dissolve
mc "They're all...related?"
js "What?"
scene ep9_burkes4 with dissolve
mc "Is Sage a Burke!?"
scene ep9_burkes5 with dissolve
my "No, I think it's Morgan Burke, but she uses Morgan."
scene ep9_burkes6 with dissolve
mc "Yes! Exactly! Morgan! This is so bad... I... I shouldn't be here."
scene ep9_burkes7 with dissolve
js "Why?"
scene ep9_burkes8 with dissolve
sa "Ok... They're waiting."
sa "And I'm sorry in advance; I didn't think my brother would be here tonight. I'll make sure he doesn't cause any trouble for us."
scene ep9_burkes9 with dissolve
sa "[name]? Are you coming?"
scene ep9_burkes10 with dissolve
mc "..."
scene ep9_burkes11 with dissolve
sb "Welcome, Maya. I see you've brought quite the support group. Heh."
scene ep9_burkes12 with dissolve
ty "What is he doing in our home!?"
if affinity == "DIK":
    if ep7_ruined_presentation:
        scene ep9_burkes13b2 with dissolve
    else:
        scene ep9_burkes13a with dissolve
else:
    if ep7_ruined_presentation:
        scene ep9_burkes13b with dissolve
    else:
        scene ep9_burkes13 with dissolve
sa "He's our guest. And what the fuck are you doing here? I told you not to come."
scene ep9_burkes12 with dissolve
ty "I'll come and go whenever I want to in {b}MY{/b} home."
scene ep9_burkes14 with dissolve
sb "Knock it off. We have guests."
scene ep9_burkes15 with dissolve
ty "Yes, Daddy."
if ep4_toldDerekAboutJade:
    scene ep9_burkes16 with dissolve
    sb "..."
scene ep9_burkes17 with dissolve
ja "I'm sorry, I had to freshen up. Welcome..."
if jade_state == 1:
    scene ep9_burkes18b with dissolve
elif jade_state == 2:
    scene ep9_burkes18c with dissolve
else:
    scene ep9_burkes18 with dissolve
ja "...everyone."
if jade_state > 0:
    scene ep9_burkes19 with dissolve
else:
    scene ep9_burkes19b with dissolve
$ renpy.pause()
scene ep9_burkes18d with dissolve
$ renpy.pause()

scene ep9_burkes20 with dissolve
sb "Please, make yourselves at home."
sb "We'll be having dinner soon, so I thought I could borrow my daughter and Maya for a while."
sb "As I understand, the rest of you have great things to tell me about Maya, but I think it's best if we start this way."
scene ep9_burkes21 with dissolve
sb "Honey. Refreshments?"
if jade_state > 0:
    scene ep9_burkes23 with dissolve
    ja "Yes, of course."
    ja "[name]. Will you help me?"
    mc "Uh... Sure..."
    scene ep9_burkes42 with dissolve
    $ renpy.pause()
    if jade_state == 1:
        scene ep9_burkes43 with dissolve
        ja "What are you doing here? Are you crazy? I'm trying to keep our affair a secret and you show up unannounced!"
        scene ep9_burkes44 with dissolve
        mc "I didn't know you were Sage's mom! Do you think I would have shown up if I did?"
        scene ep9_burkes43 with dissolve
        ja "We're the Burkes. We're among the elite of B&R."
        scene ep9_burkes45 with dissolve
        mc "I don't care about school politics or whatever."
        mc "I wanna get out of here, but I can't because I'm here to help my friend and it will look bad if I leave."
        mc "I'm feeling uncomfortable about this."
        scene ep9_burkes46 with dissolve
        ja "Look. Don't do anything irrational."
        ja "No one suspects a thing. This situation is manageable."
        scene ep9_burkes47 with dissolve
        mc "Yeah. You're right."
        scene ep9_burkes49 with dissolve
        ja "After this, don't ever show up here like this, ok?"
        scene ep9_burkes48 with dissolve
        mc "I'm gonna try, you know, unless Sage invites me for some reason."
        scene ep9_burkes49 with dissolve
        ja "You're friends with my daughter? I thought you were here for Maya."
        scene ep9_burkes50 with dissolve
        mc "Yeah, I'm very good friends with Sage."
        if pathSage or ep7_pathSage:
            mc "We actually... Fuck..."
            scene ep9_burkes51 with dissolve
            ja "You what?"
            scene ep9_burkes50 with dissolve
            mc "I need to tell you this... I may have... Um... Sage and I..."
            play sound "sound_effects/slap.mp3"
            scene ep9_burkes52 with vpunch
            ja "Don't you dare tell me that!"
            scene ep9_burkes53 with dissolve
            mc "I didn't know you were related! I already told you!"
            mc "It just happened! I never planned to have sex with {b}your{/b} daughter."
            scene ep9_burkes54 with dissolve
            ja "Oh God... Eww... This is too much."
            scene ep9_burkes53 with dissolve
            mc "But I'll never do it again. I promise!"
            scene ep9_burkes51 with dissolve
            ja "Can you really promise that?"
            scene ep9_burkes50 with dissolve
            mc "I have to promise it. For Sage's sake..."
            scene ep9_burkes51 with dissolve
            ja "If this reaches her, she will get very hurt."
        else:
            scene ep9_burkes51 with dissolve
            ja "If this reaches her, she will get very hurt."
            scene ep9_burkes50 with dissolve
            mc "I can't undo this! It's not like I planned to hurt her. I happened to have an affair with a woman who turned out to be her mother."
            scene ep9_burkes51 with dissolve
        ja "Listen to me... No one will ever know about us. There's no harm done."
        ja "And as I see it right now, we both have a mutual understanding and interest in keeping this our secret. And that's good."
        ja "You shut your mouth about it and never come back here without checking with me after tonight."
        scene ep9_burkes47 with dissolve
        mc "I'm gonna try. Because you know I don't wanna stop this."
        scene ep9_burkes55 with dissolve
        ja "And I hate it, but you're gonna have to lie to my daughter."
        ja "It would be best if you stopped seeing her altogether."
        scene ep9_burkes56 with dissolve
        mc "I can't stop seeing her... We're too close."
        scene ep9_burkes55 with dissolve
        ja "God, this is a mess..."
        ja "*{i}Sigh{/i}*"
        ja "Don't lower your guard tonight; I'll try to do the same."
        scene ep9_burkes57 with dissolve
        ja "Help me with the drinks. There are glasses in that cupboard."
        label ep9_jade_lewd_label:
        if _in_replay:
            hide screen new_phone_screen
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
            play music "music/ep6/licensed_music/track21.mp3"
            $ affinity = "DIK"
        scene ep9_burkes58 with dissolve
        $ renpy.pause()
        scene ep9_burkes59 with dissolve
        ja "*{i}Inhales{/i}*"
        scene ep9_burkes60 with dissolve
        mc "Did you just smell me?"
        scene ep9_burkes61 with dissolve
        ja "You smell incredibly good."
        scene ep9_burkes62 with dissolve
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
        menu:
            "Don't stop her [mod_gr][mod_choices[0]]":
                $ ep9_jade_lewd = True
                scene ep9_burkes64 with dissolve
                ja "God... I've been missing you."
                scene ep9_burkes65 with dissolve
                ja "*{i}Smack{/i}*"
                mc "Fuck... This isn't good..."
                scene ep9_burkes66 with dissolve
                mc "I can't resist you..."
                scene ep9_burkes67 with dissolve
                ja "What are you doing?"
                scene ep9_burkes68 with dissolve
                mc "I got so fucking hard thinking about bending you over the counter and fucking you..."
                scene ep9_burkes69 with dissolve
                ja "*{i}Moans{/i}*"
                scene ep9_burkes70 with dissolve
                ja "God, no... [name]..."
                scene ep9_burkes71 with dissolve
                ja "[name]! Are you out of your mind?"
                scene ep9_burkes72 with dissolve
                mc "I got so turned on by you... I can't help it."
                $ tmp_bool = True
                menu:
                    "Vaginal":
                        $ tmp_bool = True
                    "Anal":
                        $ tmp_bool = False
                if tmp_bool:
                    scene anim_jade_finger_ep9 with dissolve
                else:
                    scene anim_jade_finger_ass_ep9 with dissolve
                ja "Hngh... Someone could walk in on us."
                mc "I don't know why that makes me harder..."
                ja "*{i}Moans{/i}*"
                ja "This is so bad..."
                scene ep9_burkes73 with dissolve
                mc "Then stop me because I can't."
                ja "No. Don't stop."
                if tmp_bool:
                    scene anim_jade_finger2_ep9 with dissolve
                else:
                    scene anim_jade_finger2_ass_ep9 with dissolve
                mc "You're so wet..."
                ja "Just like you got harder, I got wetter..."
                mc "It's exciting, isn't it?"
                ja "(It's like I'm a young adult again, fucking in the room next to my parents.)"
                ja "(FUCK! I'M SO HORNY!)"
                pause
                scene ep9_burkes74 with dissolve
                ty "Mommy?"
                play sound "sound_effects/shove.mp3"
                if tmp_bool:
                    scene ep9_burkes75 with vpunch
                else:
                    scene ep9_burkes75b with vpunch
                ty "What's taking so long!?"
                scene ep9_burkes78 with dissolve
                ja "TYBALT! LEAVE!"
                scene ep9_burkes76 with dissolve
                ty "Huh? But I-"
                scene ep9_burkes79 with dissolve
                ja "Don't you talk back to me! Go sit on the couch and don't you dare come back unless I say so."
                scene ep9_burkes77 with dissolve
                ty "Hurry up! I can't stand the company."
                scene ep9_burkes80 with dissolve
                ja "*{i}Gasps{/i}*"
                scene ep9_burkes81 with dissolve
                ja "[name]... I just...came..."
                if tmp_bool:
                    scene ep9_burkes82 with dissolve
                else:
                    scene ep9_burkes82b with dissolve
                ja "Oh my God! Are you...? Oh, fuck!"
                if tmp_bool:
                    scene bg anim_jade_insert_ep9 movie with dissolve
                else:
                    scene bg anim_jade_insert_ass_ep9 movie with dissolve
                ja "*{i}Moans{/i}* Oh, God!!!"
                if tmp_bool:
                    scene anim_jade_doggy_ep9 with dissolve
                else:
                    scene anim_jade_doggy_ass_ep9 with dissolve
                mc "I gotta have you, [jade]..."
                ja "Make it quick. Don't hold anything back!"
                pause

                scene anim_jade_doggy2_ass_ep9 with dissolve
                ja "If someone walks in now, we're done for..."
                mc "(What the fuck am I doing!? Holy fuck, this escalated so quickly!)"
                mc "(I'm fucking Sage's...mom!?)"
                pause
                if tmp_bool:
                    scene anim_jade_doggy3_ep9 with dissolve
                else:
                    scene anim_jade_doggy3_ass_ep9 with dissolve
                mc "I'm close... I'm gonna cum."
                ja "Finish inside. We don't have time to clean up any mess."
                pause
                if tmp_bool:
                    scene ep9_burkes85 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep9_burkes85 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep9_burkes85 at vpunch, cum1
                    $ renpy.pause()
                    scene ep9_burkes86 with dissolve
                    $ renpy.pause()
                else:
                    scene ep9_burkes83 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep9_burkes83 at vpunch, cum1
                    $ renpy.pause(0.5)
                    scene ep9_burkes83 at vpunch, cum1
                    $ renpy.pause()
                    scene ep9_burkes84 with dissolve
                    $ renpy.pause()
                scene ep9_burkes87 with dissolve
                ja "You're gonna be the end of me, [name]..."
                ja "This is exactly why you can't show up."
                if tmp_bool:
                    scene ep9_burkes88 with dissolve
                else:
                    scene ep9_burkes88b with dissolve
                mc "I can't restrain myself when I'm with you..."
                ja "I know... It's so hard..."
                scene ep9_burkes89 with dissolve
                stop music fadeout 3
                ja "...but you better find some way to get a grip, or we won't be able to hide this forever, let alone for the night."
                $ renpy.end_replay()
                $ persistent.ep9_lewd_jade = True
                $ calcScenes()
                $ mphone_stats_add_girl_s3("jade","You had sex with Jade in her kitchen in episode 9.")
                $ new_bio("Jade", "I fucked Jade in her kitchen while her family was at home.")
            "Keep it together" if not _in_replay:
                mc "Keep it together. Everyone's out there."
                scene ep9_burkes63 with dissolve
                stop music fadeout 3
                ja "You're right."
                $ new_bio("Jade", "I resisted Jade in the kitchen of her home. Her family was in the other room, and it was too risky.")
    else:
        scene ep9_burkes90 with dissolve
        ja "Now, you listen to me, you little shit, and you listen good!"
        if jade_state == 3:
            if ep4_fuckedJade:
                ja "I've come to terms with that what we had was a one-time thing, but how stupid do you have to be to come here tonight?"
            else:
                ja "What we did in class was a one-time thing, but how stupid do you have to be to come here tonight?"
        else:
            ja "How stupid do you have to be to come here tonight?"
            ja "Is this some kind of a sick game to you? I want you out of my life completely. Do you understand me?"
        scene ep9_burkes92 with dissolve
        mc "I didn't know you were Sage's mom! Do you think I would have shown up if I did?"
        scene ep9_burkes91 with dissolve
        ja "How dense are you? We're the Burkes. We're among the elite on B&R."
        scene ep9_burkes92 with dissolve
        mc "I don't care about school politics or whatever."
        mc "I wanna get out of here, but I can't because I'm here to help my friend and it will look bad if I leave."
        scene ep9_burkes90 with dissolve
        ja "Ok. Good. Because if you don't-!"
        scene ep9_burkes92 with dissolve
        if jade_state == 3:
            if ep4_fuckedJade:
                mc "You don't have to threaten me. We had sex once, and that's it. There's nothing more to it than that."
            else:
                mc "You don't have to threaten me. There's nothing more to it than that time in class between us."
        else:
            mc "You don't have to threaten me. I wanted to have a clean break with you; instead, it ended up in this mess."
        scene ep9_burkes93 with dissolve
        ja "Listen to me... No one will ever know."
        ja "You shut your mouth about it, and you never come back here after tonight."
        ja "I don't wanna see you and I don't want to hear anything about you after this. We're completely through."
        scene ep9_burkes92 with dissolve
        mc "That's gonna be pretty damned hard..."
        if branchSage:
            mc "Sage and I are getting... Pretty close."
            scene ep9_burkes94 with dissolve
            $ renpy.pause()
            play sound "sound_effects/slap.mp3"
            scene ep9_burkes52 with vpunch
            ja "Don't you dare tell me that!"
            scene ep9_burkes53 with dissolve
            mc "I didn't know! I already told you!"
            play sound "sound_effects/slap.mp3"
            scene ep9_burkes52 with vpunch
            ja "You're not gonna do this to my daughter!"
            scene ep9_burkes53 with dissolve
            mc "I can't undo it! It's already done."
            scene ep9_burkes90 with dissolve
            ja "No. You will find a way."
            ja "You're going to break up with my daughter before you start anything. I will not let this happen to her."
            scene ep9_burkes92 with dissolve
            if jade_state == 3 or not ep4_fuckedJade:
                mc "I like her a lot. She means something to me."
            else:
                mc "I like her a lot. That's why I had to stop fooling around with you."
                scene ep9_burkes54 with dissolve
                ja "Eww! Don't say that!"
                scene ep9_burkes92 with dissolve
            mc "I'm not gonna break up with her."
            scene ep9_burkes91 with dissolve
            ja "So, you intend to lie to my daughter?"
            scene ep9_burkes95 with dissolve
            mc "You're lying to your husband. I don't see the difference."
            if ep4_fuckedJade:
                mc "And it's not like I did this on purpose. I happened to fuck two girls who were related by mistake."
            else:
                mc "And it's not like I did this on purpose."
            scene ep9_burkes96 with dissolve
            stop music fadeout 3
            ja "The guilt will eat you alive."
            $ new_bio("Jade", "Jade was mad at me for dating Sage. She thought it was too risky and wanted me to end our relationship. I told her I wasn't going to stop dating Sage.")
        else:
            mc "Sage is a good friend to me."
            scene ep9_burkes93 with dissolve
            ja "You're gonna have to find a way to stop being her friend."
            scene ep9_burkes92 with dissolve
            mc "What? No!"
            scene ep9_burkes91 with dissolve
            ja "If this reaches her, she will get very hurt."
            scene ep9_burkes92 with dissolve
            if ep4_fuckedJade:
                mc "I can't undo this! It's not like I planned to hurt her. I happened to have an affair with a woman who turned out to be her mother."
            else:
                mc "I can't undo this! It's not like I planned to hurt her."
            scene ep9_burkes93 with dissolve
            ja "So, you intend to lie to my daughter?"
            scene ep9_burkes95 with dissolve
            mc "You're lying to your husband. I don't see the difference."
            mc "It's better to keep this a secret than to let her know."
            scene ep9_burkes96 with dissolve
            stop music fadeout 3
            if ep4_fuckedJade:
                ja "The guilt will eat you alive."
            else:
                ja "I can't believe you..."
            $ new_bio("Jade", "Jade was mad at me for being Sage's friend. She thought it was too risky and wanted me to end our friendship. I told her I wasn't going to stop being her friend.")
else:
    scene ep9_burkes22 with dissolve
    ja "Yes. Of course."
    scene ep9_burkes24 with dissolve
    $ renpy.pause()
    scene ep9_burkes25 with dissolve
    $ renpy.pause()
    scene ep9_burkes24 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
    menu:
        "Talk to Josy":
            scene ep9_burkes27 with dissolve
            mc "*{i}Whispers{/i}* So, this is awkward."
            scene ep9_burkes28 with dissolve
            js "*{i}Whispers{/i}* You think?"
            scene ep9_burkes27 with dissolve
            mc "*{i}Whispers{/i}* Yeah, I don't know what I should say to him. I don't want to talk to him at all, but it's awkward sitting here in silence."
            scene ep9_burkes29 with dissolve
            if ep7_ruined_presentation:
                js "*{i}Whispers{/i}* You probably shouldn't mention his presentation."
                scene ep9_burkes30 with dissolve
                if affinity == "DIK":
                    mc "Hahaha!"
                    js "Shh... Haha..."
                else:
                    mc "Yeah..."
                    js "Haha..."
            else:
                js "*{i}Whispers{/i}* I have the same problem. It's the first time I can't think of things to talk about to break the silence."
        "Antagonize Tybalt [mod_gr][mod_choices[3]]":
            $ dk(2)
            scene ep9_burkes31 with dissolve
            mc "So... Tybalt..."
            mc "Read any good books lately?"
            scene ep9_burkes26 with dissolve
            ty "..."
            scene ep9_burkes31 with dissolve
            if ep7_tybalt_state == 2:
                mc "Nice teeth, by the way. It's good that they could fix that problem for you."
                scene ep9_burkes29 with dissolve
                js "*{i}Whispers{/i}* Haha, you're so mean."
            else:
                mc "Not the one for small talk, eh?"
    scene ep9_burkes29b with dissolve
    mc "So... Um... Quick question..."
    scene ep9_burkes29c with dissolve
    js "Yeah?"
    scene ep9_burkes29b with dissolve
    mc "Josephine Taylor... Right?"
    scene ep9_burkes29c with dissolve
    js "Um...yeah?"
    scene ep9_burkes29b with dissolve
    mc "Just Josephine Taylor?"
    scene ep9_burkes29c with dissolve
    stop music fadeout 3
    js "Yes? Just Josephine Taylor."
    scene ep9_burkes29b with dissolve
    mc "Ok... I'm just making sure."
play music "music/ep9/neils_theme.mp3"
scene ep9_dz1 with wipeleft
zo "Yeah, the waves were really big. I fell off my board a lot."
scene ep9_dz10 with dissolve
dad "It sounds like you had a great time, after all. And, if I may say, you're beaming with positive energy."
scene ep9_dz2 with dissolve
zo "Haha... Yeah... I am happy to be back."
scene ep9_dz3 with dissolve
zo "So, you're living alone these days?"
scene ep9_dz11 with dissolve
dad "Yes. I've still not gotten used to it."
scene ep9_dz3 with dissolve
zo "How's that going for you?"
scene ep9_dz12 with dissolve
dad "Well, some mornings and nights, I set the table with two plates before I remember it's just me here."
dad "On the upside, it's nice that I don't have to wait to use the shower and that hot water is always running."
dad "But the house has one too many rooms for me alone. I thought it would feel luxurious, but it makes it feel more..."
dad "*{i}Sigh{/i}* ..."
scene ep9_dz11 with dissolve
dad "Sorry. I'm doing well, is the answer I should have gone with."
scene ep9_dz4 with dissolve
if zoey_dik:
    zo "It's all right. You don't have to give the token bullshit response. You miss your son. Who wouldn't?"
else:
    zo "It's all right. You miss your son. Who wouldn't?"
zo "How's college for him?"
scene ep9_dz10 with dissolve
dad "Oh, as I gather, it's great! He's got a lot going on for him these days."
dad "He has a lot of classes and tests, and he is part of a Greek group."
dad "The dick boys! Yes, that's the name."
scene ep9_dz6 with dissolve
zo "The dick boys?"
scene ep9_dz10 with dissolve
dad "Please don't ask me where they come up with all those crazy ideas."
scene ep9_dz5 with dissolve
zo "Haha!"
scene ep9_dz4 with dissolve
zo "So, since I left...has he been...um...happy?"
scene ep9_dz13 with dissolve
dad "Err..."
scene ep9_dz14 with dissolve
dad "Yes! Very much so! After you left, he's been as happy as a clam-"
scene ep9_dz13 with dissolve
dad "I mean, not because you left, but-"
scene ep9_dz4 with dissolve
zo "He's been happy?"
scene ep9_dz13 with dissolve
dad "Yes."
scene ep9_dz7 with dissolve
zo "*{i}Phew{/i}* That's good! Really good."
zo "I've been wondering about that a lot."
scene ep9_dz8 with dissolve
zo "I don't know how much he's told you, but we didn't talk for a while."
scene ep9_dz15 with dissolve
dad "Is that so?"
scene ep9_dz8 with dissolve
zo "Yeah. I tried calling him tonight before I came here, but I couldn't reach him."
zo "I was worried he maybe blocked me, because of...him not liking me anymore or something."
scene ep9_dz13 with dissolve
dad "Blocked you? No. I'm sure he didn't block you."
scene ep9_dz8 with dissolve
zo "There was some message saying his number was disconnected, so, it must be something, right?"
scene ep9_dz14 with dissolve
dad "You know what it is? He got a new phone not that long ago. It's got a new number and everything!"
dad "He probably shut off his old one without thinking much about it. I'm sure he still has your number."
scene ep9_dz9 with dissolve
zo "Oh! That explains it, then."
zo "Can you tell him to call me or something? I wanna talk to him again."
scene ep9_dz14 with dissolve
stop music fadeout 3
dad "Of course. I'm sure he'll be happy to hear that."

play music "music/ep6/licensed_music/track21.mp3"
scene ep9_burkes32 with dissolve
ja "Here you go, darling. Some refreshments."
ty "Thank you, Mommy."
scene ep9_burkes33 with dissolve
js "*{i}Whispers{/i}* Is it weird that he calls them Mommy and Daddy, or is it just me?"
scene ep9_burkes34 with dissolve
ja "What was that?"
scene ep9_burkes35 with dissolve
js "Uh... You have a lovely home!"
scene ep9_burkes34 with dissolve
ja "Thank you, you're too kind. I'm not particularly fond of this conversation pit. It's a little bit too '70s for my taste, but Stephen insisted..."

if jade_state == 1:
    scene ep9_burkes36 with dissolve
    mc "(Take deep breaths...)"
    mc "(You couldn't have known this...)"
    if pathSage:
        mc "(So what? You're having an affair with your former fuck buddy's mom... There's nothing wrong with that.)"
    elif ep7_pathSage:
        mc "(So what? You're having an affair with your friend's mom, a friend you've also fucked... There's nothing wrong with that.)"
    else:
        mc "(So what? You're having an affair with your friend's mom... There's nothing wrong with that.)"
    if ep9_jade_lewd:
        mc "(Aaaand you can't resist her, so you banged her in the kitchen when her entire family was at home...)"
    scene ep9_burkes37 with dissolve
    mc "(...)"
    mc "(Hell was made for people like me.)"
elif jade_state == 2 or jade_state == 3:
    scene ep9_burkes36 with dissolve
    mc "(Take deep breaths...)"
    mc "(You couldn't have known this...)"
    if ep4_fuckedJade:
        if branchSage:
            mc "(So what? You had an affair with your new almost-girlfriend's mom... There's nothing wrong with that.)"
        elif pathSage and not branchSage:
            mc "(So what? You had an affair with your former fuck buddy's mom... There's nothing wrong with that.)"
        elif ep7_pathSage and not branchSage:
            mc "(So what? You had an affair with your friend's mom; a friend you've also fucked... There's nothing wrong with that.)"
        else:
            mc "(So what? You had an affair with your friend's mom... There's nothing wrong with that.)"
        if ep6_reject_jade:
            mc "(We pretty much stopped it after that one time... So, I'm good...)"
        else:
            mc "(I broke it off... So, I'm good...)"
    else:
        if branchSage:
            mc "(So what? You fooled around in class with your new almost-girlfriend's mom... There's nothing wrong with that.)"
        elif pathSage and not branchSage:
            mc "(So what? You fooled around in class with your former fuck buddy's mom... There's nothing wrong with that.)"
        elif ep7_pathSage and not branchSage:
            mc "(So what? You fooled around in class with your friend's mom, a friend you've also fucked... There's nothing wrong with that.)"
        else:
            mc "(So what? You fooled around in class with your friend's mom... There's nothing wrong with that.)"
        mc "(It was just an innocent footjob and a handjob... So, I'm good...)"
    scene ep9_burkes37 with dissolve
    mc "(...)"
    mc "(Yeah, I'm going to hell.)"
    mc "(I need to get through the night without saying something stupid.)"
else:
    scene ep9_burkes36b with dissolve
    mc "(Take deep breaths...)"
    mc "(You couldn't have known this...)"
    if branchSage:
        mc "(So what? Your new almost-girlfriend's mom happens to be the teacher who tried to seduce you by putting her foot on your cock in class...)"
    elif pathSage and not branchSage:
        mc "(So what? Your former fuck buddy's mom happens to be the teacher who tried to seduce you by putting her foot on your cock in class...)"
    else:
        mc "(So what? Your friend's mom happens to be the teacher who tried to seduce you by putting her foot on your cock in class...)"
    scene ep9_burkes37 with dissolve
    mc "(...)"
    mc "(Sage can never know about this. It would be horrible!)"

stop music fadeout 3
mc "(I hope my issues with Tybalt don't affect Maya's chances in any way. It's probably good they're off talking in private.)"

play music "music/ep5/licensed_music/track4.mp3"
scene ep9_burkes97 with dissolve
sa "Maya's more than an eligible candidate for a scholarship. She graduated Magna Cum Laude and is aiming for a social work degree."
scene ep9_burkes98 with dissolve
sb "Social work, you say? Maya. Please tell me why you've chosen that line of study."
scene ep9_burkes101 with dissolve
sa "She's-"
scene ep9_burkes100 with dissolve
sb "I asked Maya."
scene ep9_burkes104 with dissolve
my "Well, I...um..."
sa "*{i}Whispers{/i}* Speak up. Be confident."
scene ep9_burkes105 with dissolve
my "I want to help people. Families. I want to help families."
scene ep9_burkes99 with dissolve
sb "In which ways?"
scene ep9_burkes105 with dissolve
my "It's the kids I want to help, really. When they're young, and their parents fight with each other or them, they have nowhere to turn."
my "It's like they are prisoners in their homes. I want to support these families so the kids can get the help they need."
scene ep9_burkes106 with dissolve
my "I feel it's too hard for the current system to give proper help and that there's not enough that can be done until it's too late and the damage is done."
my "I want to work in a way that makes positive changes so they can get help earlier and easier when there are warning signs of domestic abuse, for one."
my "So, their entire upbringing gets better."
scene ep9_burkes99 with dissolve
sb "That sounds very noble. And B&R does have an excellent social work program."
scene ep9_burkes105 with dissolve
my "I agree. That's one of the reasons I applied."
my "And I wish to be able to continue my studies, but I'm-"
scene ep9_burkes101 with dissolve
sa "If Maya could get a scholarship, it would ensure that she can put more focus into her studies instead of having to split focus on finding other ways to fund college."
sa "For example, having to work at the same time as studying isn't optimal for a student wanting to achieve the high goals Maya has set for herself."
scene ep9_burkes102 with dissolve
sa "So, I thought we could do something to help her with that."
show ep9_burkes100
if not persistent.ep9_cardji16:
    show screen ep9_render_screen("ji16")
with dissolve
sb "Sweetie, you've made it clear where your heart lies regarding Maya. However, I'd like to hear more from her."
show ep9_burkes103
hide screen ep9_render_screen
with dissolve
hide ep9_burkes100
sa "Sorry, I..."
show ep9_burkes100
if not persistent.ep9_cardji16:
    show screen ep9_render_screen("ji16")
with dissolve
sb "Join the others. I have a few more questions for Maya."
show ep9_burkes107
hide screen ep9_render_screen
with dissolve
$ renpy.pause()
scene ep9_burkes108 with dissolve
sb "You'll have to excuse my daughter. I can see that she's very passionate about helping you."
sb "When she's passionate, she accomplishes great things."
scene ep9_burkes109 with dissolve
sb "So... You're under the impression that I can help you with a scholarship, correct?"
scene ep9_burkes111 with dissolve
my "Well, yes. That's what I've been told."
scene ep9_burkes109 with dissolve
sb "Helping students fund college is something I take pride in and enjoy; I'm sure you've read the newspapers."
sb "Why do you need help with funding, if I may ask? What is your current situation?"
scene ep9_burkes111 with dissolve
my "I have a cosigned loan that my father prepared, but truth be told, I'm having some family issues affecting my studies."
my "I don't know if I can continue studying for long because of it."
my "If I can get help to fund college, I believe it would change everything."
scene ep9_burkes110 with dissolve
sb "So, this is not about wanting the help, but more about needing the help?"
scene ep9_burkes112 with dissolve
play sound "sound_effects/season3/type1.mp3"
my "Yes, exactly. It's quite pressing."
scene ep9_burkes113 with dissolve
sb "And even though you have funding at the moment, this family dispute somehow impacts it?"
scene ep9_burkes111 with dissolve
my "Yes. And I've tried everything I could think of to fix it."
scene ep9_burkes113 with dissolve
sb "Is that right? Well, what have you done?"
scene ep9_burkes111 with dissolve
my "At first, I tried to talk to my dad about it, but reasoning with him didn't help."
my "Then I tried making it work by not causing a fuss about it, but it's not going well."
my "And it's so stupid, but I even pledged the sorority thinking I'd get help with free tuition."
scene ep9_burkes114 with dissolve
sb "..."
scene ep9_burkes115 with dissolve
sb "And by the sorority...um...you mean...?"
scene ep9_burkes111 with dissolve
my "The Eta Omicron Tau sorority. Your...daughter's sorority."
scene ep9_burkes115 with dissolve
sb "Yes... Haha. Of course."
sb "I'm confused. Did they say you'd get tuition from pledging?"
scene ep9_burkes117 with dissolve
my "As I said, it's stupid, but you asked, so..."
my "I heard this rumor that they offered free tuition for their sisters, and I pledged to try to get it."
my "And when I pledged, I was told there was a way to get it, but apparently, it was some joke. I'm not entirely sure what it was-"
scene ep9_burkes116 with dissolve
sb "Oh? But you didn't join the sorority now, correct?"
scene ep9_burkes117 with dissolve
my "Because of your daughter, I've been thinking about joining."
my "She's been pushing me to do it, and I'm starting to come around."
play sound "sound_effects/season3/type2.mp3"
scene ep9_burkes118 with dissolve
$ renpy.pause()
scene ep9_burkes119 with dissolve
my "Anyway, um... Sage told me it could be worth applying for a scholarship, which is the story up until now."
scene ep9_burkes122 with dissolve
sb "Ah."
sb "You know, Maya..."
scene ep9_burkes124 with dissolve
sb "I think the problem we're faced with is that these...scholarships are highly sought after."
sb "We get many applicants every year, and while you're welcome to apply - I'm going to be honest out of respect for you and my daughter..."
scene ep9_burkes123 with dissolve
sb "It's going to be very difficult to find a fitting scholarship for you. The funds we have available are mostly earmarked for the financial division."
sb "You can always apply and hope for the best. But it's a fairly long process, and as I gather, you're more in need of immediate help."
sb "And since you already have funding, it's going to be even harder for me to advocate why you should receive a scholarship, especially after having started college."
scene ep9_burkes120 with dissolve
my "*{i}Sigh{/i}* I understand."
my "I...don't know what to do anymore."
my "Sorry, I'm not gonna put that guilt on you. It's just-"
scene ep9_burkes124 with dissolve
sb "You know, there are always ways to get out of situations like these."
sb "May I suggest quitting college and repaying the loan? You could find a cheaper alternative going forward."
sb "I hear online classes are getting reputable, and there are even cheaper colleges than B&R."
scene ep9_burkes121 with dissolve
my "Won't I lose time doing that?"
scene ep9_burkes123 with dissolve
sb "I'm stating some of the options you have at your disposal. It might take a year of your life, but put that in comparison to the uncertainty you're facing, and it's a good deal."
sb "Of course, I'll assist with any paperwork and issues arising from this. I'd happily write you a letter of recommendation too."
scene ep9_burkes120 with dissolve
my "Thanks, but I don't want that. I'm not sure it's even possible..."
my "I don't want to quit college; I like it here. That's why I'm trying to fight; I'm looking for a way to keep going."
scene ep9_burkes123 with dissolve
sb "I thought the circumstances were different, but as we have it... I'm very sorry. I wish I could do more for you, but my hands are tied."
sb "Please, don't blame my daughter for this. She doesn't know the limits and procedures of my work."
stop music fadeout 3
scene ep9_burkes125 with dissolve
$ renpy.pause()

play music "music/ep5/subtle_break.mp3"
scene ep9_burkes38 with dissolve
ty "Mommy. I refuse to have dinner if he's at the table."
ty "Frankly, the thought of you feeding him our food is appalling."
ty "He is a horrible human being and he's all that's wrong with this world. We cannot nurture that!"
scene ep9_burkes39 with dissolve
js "I understand why you felt you shouldn't be here now."
scene ep9_burkes40 with dissolve
mc "I'm gonna fuck over Maya's chances if I stay."
scene ep9_burkes38 with dissolve
if ep7_ruined_presentation:
    ty "MOMMY! HE PUT A PENIS PICTURE IN MY PRESENTATION!"
    ja "I don't want to hear it."
    js "*{i}Muffled laugh{/i}*"
    mc "Josy..."
    js "Sorry, but I can't control it! It's too funny! You didn't see his face when he found out."
if ep5_punchedTybalt:
    ty "MOMMY! HE PUNCHED ME!"
    ja "I don't want to hear it..."
if ep7_tybalt_state == 2:
    ty "MOMMY! HE KNOCKED OUT MY TEETH WITH A TENNIS BALL!"
    ja "Tybalt..."
ty "MOMMY! HE IS DESPICABLE! HE'S BEEN RUINING MY LOVE LIFE!"
ja "Take it up with your father."
ty "I will! And let me be perfectly clear; there is no way that I would support any decision making his or his friends' lives easier with our help."
scene ep9_burkes41 with dissolve
mc "I'll be right back..."

scene epi_ending20 with dissolve
$ renpy.pause()
scene epi_ending21 with dissolve
$ renpy.pause()
if branchSage and ep4_fuckedJade:
    scene epi_ending22b with dissolve
    $ renpy.pause()
elif ep4_fuckedJade or branchSage:
    scene epi_ending22a with dissolve
    $ renpy.pause()
else:
    scene epi_ending22 with dissolve
    $ renpy.pause()
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep9_burkes126
if not persistent.ep9_cardji9:
    show screen ep9_render_screen("ji9")
with dissolve
dad "Son. I hope I'm not interrupting, but you'll never guess who just dropped by."
scene epi_ending23_nocard
hide screen ep9_render_screen
with dissolve
mc "Dad. Now is not a good time for me. I-"
scene ep9_burkes127 with dissolve
dad "It's Zoey. She's back home."
scene epi_ending24 with dissolve
mc "Wait, what!?"
mc "S-she's back? Why?"
scene ep9_burkes128 with dissolve
dad "Oh, that's a rather long story. An interesting one! But long."
dad "She's been telling it to me over a cup of tea, and I'm sure she wants to tell it to you herself."
dad "That is... If you're ok with it? I wasn't sure..."
scene epi_ending25 with dissolve
mc "Uh... I guess..."
scene ep9_burkes127 with dissolve
dad "It's why she dropped by. She couldn't reach you."
dad "She tried calling you on your old number and found it weird that it was disconnected... She even thought you blocked her..."
scene epi_ending26 with dissolve
mc "..."
scene epi_ending27 with dissolve
mc "Give her my new number."
scene ep9_burkes129 with dissolve
dad "Son... I didn't tell her the truth about it."
dad "I was blindsided when she asked, and I lied and told her that you had recently changed your phone and number."
dad "And that your old phone still has her number but is shut off- You stopped using that one, right?"
scene epi_ending27 with dissolve
mc "Yeah, my old phone is switched off."
scene ep9_burkes130 with dissolve
dad "I'm sorry... I shouldn't have lied to her. But I didn't want to embarrass you."
dad "I remember how determined you were to move on that day and..."
scene epi_ending28 with dissolve
mc "Hey..."
mc "Is she ok?"
scene ep9_burkes131 with dissolve
dad "She looked healthy. And happy."
scene epi_ending29 with dissolve
dad "It's quite the contrast from my last memory of her after the funeral."
scene epi_ending28 with dissolve
mc "I see."
play sound "sound_effects/door_bang.mp3"
scene epi_ending31 with vpunch
sa "[name]! You better fucking open up!"
scene epi_ending30 with dissolve
mc "Dad, I gotta go."

scene ep9_burkes132 with dissolve
sa "This is all going to shit! I can't fucking believe this!"
scene ep9_burkes133 with dissolve
mc "I'm sorry, it's my fault..."
scene ep9_burkes134 with dissolve
sa "What?"
scene ep9_burkes136 with dissolve
mc "With your brother and all, I-"
scene ep9_burkes135 with dissolve
sa "I'm talking about Dad!"
sa "He's not gonna grant Maya any scholarship."
scene ep9_burkes136 with dissolve
mc "He said that?"
scene ep9_burkes134 with dissolve
sa "He made me leave, but I stayed in the hallway and eavesdropped on them. I couldn't make everything out, but he said he couldn't help her."
scene ep9_burkes135 with dissolve
sa "I don't fucking get it! He said he might be able to help when I first asked; he was even positive that there were funds for it."
sa "But now he tells her he can't help because she's not studying economics or something."
scene ep9_burkes136 with dissolve
menu:
    "What can we do to help?":
        mc "What can we do to help?"
        scene ep9_burkes135 with dissolve
        sa "Nothing! He made up his mind in there. He won't go back on it; I know him."
        sa "Fucking shit!"
    "Don't take it personally":
        mc "Hey, don't take it personally. Remember that Maya told you she wouldn't blame you for this."
        scene ep9_burkes135 with dissolve
        sa "It doesn't matter! I'm gonna feel like shit for bringing her and you guys here only to walk away being rejected like that."
sa "I thought..."
scene ep9_burkes137 with dissolve
sa "..."
scene ep9_burkes138 with dissolve
sa "I thought I could help her."
scene ep9_burkes137 with dissolve
mc "..."
scene ep9_burkes139 with dissolve
mc "You tried... That counts. You went out of your way to help someone in need."
mc "Don't beat yourself up over it. You've given her hope. We'll find another way."
scene ep9_burkes140 with dissolve
sa "How?"
scene ep9_burkes139 with dissolve
mc "I don't know. But there's gotta be something we can do."
scene ep9_burkes140 with dissolve
sa "We should go back out there. Dinner is almost ready."
scene ep9_burkes139 with dissolve
mc "About that... Your brother doesn't wanna have dinner with me."
scene ep9_burkes141 with dissolve
sa "Good, then he can leave."
scene ep9_burkes142 with dissolve
mc "Sage, listen. I don't get along with him. Like, at all."
scene ep9_burkes141 with dissolve
sa "I'm not blind, dude. I know that."
scene ep9_burkes142 with dissolve
mc "I feel like I'm the blind one... How come you've never told me you're a Burke? Or a Morgan Burke, or whatever it is."
mc "I didn't know Jade and Stephen were your parents, and Jade's been my teacher."
$ guideSuggestedPage = 50
scene ep9_burkes143 with dissolve
sa "I don't know, dude. What does it matter? I mean, what's your dad's name?"
scene ep9_burkes142 with dissolve
label getPlayerlName:
$ lname = renpy.input("What is your last name?", length=15, default="Miller")
$ lname = lname.strip()
if lname.lower() == "burke" or lname.lower() == "morgan" or lname.lower() == "morgan burke" or lname.lower() == "burke morgan" or lname.lower() == "roberts" or lname.lower() == "taylor" or lname.lower() == "bailey" or lname.lower() == "royce" or lname.lower() == "burgmeister":
    mc "It's Neil [lname]."
    scene ep9_burkes143 with dissolve
    sa "No, it's not. Stop fucking around."
    scene ep9_burkes142 with dissolve
    jump getPlayerlName
elif lname.lower() == "armstrong" or lname.lower() == "young" or lname.lower() == "diamond" or lname.lower() == "peart" or lname.lower() == "steele" or lname.lower() == "neil":
    scene ep9_burkes143 with dissolve
    sa "Neil [lname]? Really? Stop fucking around."
    scene ep9_burkes142 with dissolve
    jump getPlayerlName
elif lname.lower() == name.lower():
    scene ep9_burkes143 with dissolve
    sa "Yeah? That would make you [name] [lname]. Stop fucking around."
    scene ep9_burkes142 with dissolve
    jump getPlayerlName
elif lname == "":
    jump getPlayerlName
mc "It's Neil [lname]."
scene ep9_burkes143 with dissolve
sa "See!? I didn't know that."
scene ep9_burkes144 with dissolve
sa "I don't like talking about my family when I'm with you. You know that we have issues, right?"
sa "And I've only started trusting you with these personal things... It's hard for me to talk about them."
scene ep9_burkes142 with dissolve
mc "Ok. I can understand that."
scene ep9_burkes144 with dissolve
if branchSage:
    sa "And about Morgan... I'll tell you some other time... This isn't the time or place for it."
else:
    sa "And about Morgan... Ugh... This isn't the time or place for it."
sa "They're waiting for us."
if branchSage:
    scene ep9_burkes145 with dissolve
    sa "Wait..."
    scene ep9_burkes146 with dissolve
    sa "*{i}Smack{/i}*"
    scene ep9_burkes147 with dissolve
    sa "Mmm..."
    scene ep9_burkes148 with dissolve
    sa "*{i}Sigh{/i}* I needed that..."
    sa "You're the best."
    if jade_state > 0:
        scene ep9_burkes149 with dissolve
        mc "..."

$ new_bio("Sage", "Sage's last name is Morgan Burke...but she uses Morgan.")
$ new_bio("Sage", "Sage told me her dad wouldn't help Maya with her tuition.")
$ new_bio("Maya", "Maya didn't get any help from Stephen Burke.")
$ new_bio("Zoey", "Zoey is back in town, and she tried to reach me on my old number... Dad lied and covered for what really happened.")

scene ep9_burkes150 with dissolve
$ renpy.pause()
scene ep9_burkes151 with dissolve
js "*{i}Whispers{/i}* How did it go?"
scene ep9_burkes152 with dissolve
my "*{i}Whispers{/i}* Not that well... He can't help me."
scene ep9_burkes151 with dissolve
js "*{i}Whispers{/i}* Really? Is there anything we can do to change his mind?"
scene ep9_burkes152 with dissolve
my "*{i}Whispers{/i}* No, it doesn't look that way..."

if jade_state == 1 and (pathSage or ep7_pathSage):
    scene ep9_burkes153 with dissolve
    mc "(Well, this is an awkward situation...)"
    mc "(I have a hand on my cock, and I can't guess if it's the mother's or the daughter's.)"
    mc "(And if I look down to check, both would notice... Fuck...)"
    scene ep9_burkes154 with dissolve
    $ renpy.pause()
    scene ep9_burkes155 with dissolve
    mc "(Ok... I figured it out...)"
    scene ep9_burkes156 with dissolve
    mc "(She is crazy for doing it here... I'm fucking sweating...)"
    mc "(What have I gotten myself into?)"
elif jade_state == 1:
    scene ep9_burkes153 with dissolve
    mc "(Well, this is an awkward situation...)"
    mc "(Jade's got her hand on my cock in front of my friends, her husband, and her kids.)"
    scene ep9_burkes154 with dissolve
    $ renpy.pause()
    scene ep9_burkes156 with dissolve
    mc "(Is she this crazy? She's doing it here... I'm fucking sweating...)"
    mc "(What have I gotten myself into?)"

scene ep9_burkes157 with dissolve
ty "Father. Will you pass me the salt?"
scene ep9_burkes165 with dissolve
sa "*{i}Mumbles{/i}* Like you need more salt."
scene ep9_burkes158 with dissolve
ty "Pardon?"
scene ep9_burkes166 with dissolve
sa "Nothing."
scene ep9_burkes164 with dissolve
ja "So, what did you decide?"
scene ep9_burkes163 with dissolve
sb "We've come to an understanding, but let's not ruin dinner over it."
sb "I'm positive there are ways for Maya to get out of her predicament. And if she's interested, I'll assist her in the ways I mentioned."
scene ep9_burkes167 with dissolve
$ renpy.pause()
scene ep9_burkes169 with dissolve
my "*{i}Mouths{/i}* It's fine."
scene ep9_burkes168 with dissolve
$ renpy.pause()
scene ep9_burkes171 with dissolve
js "I like the beef. It's very moist and tasty!"
scene ep9_burkes159 with dissolve
ty "It's not beef; it's venison."
scene ep9_burkes171 with dissolve
js "Ah. Maybe that's why I like it so much, then?"
scene ep9_burkes159 with dissolve
ty "It's not your fault. You've likely not had the chance to train your palate in life."
scene ep9_burkes172 with dissolve
js "Wow, that's rude."
scene ep9_burkes162 with dissolve
sb "Tybalt. Apologize."
scene ep9_burkes161 with dissolve
ty "Pardon?"
scene ep9_burkes162 with dissolve
sb "You heard me."
scene ep9_burkes159 with dissolve
ty "I'm sorry if I have offended you by speaking the truth."
scene ep9_burkes170 with dissolve
my "She's right, though. This beef is delicious."
scene ep9_burkes160 with dissolve
ty "..."
scene ep9_burkes173 with dissolve
$ renpy.pause()
scene ep9_burkes174 with dissolve
mc "*{i}Whispers{/i}* What are you up to?"
scene ep9_burkes174b with dissolve
sa "*{i}Whispers{/i}* Just some Rooster stuff."
scene ep9_burkes177 with dissolve
$ renpy.pause()
mc "*{i}Whispers{/i}* What the hell!?"
scene ep9_burkes175 with dissolve
mc "*{i}Whispers{/i}* It's you? You're Tyballs?"
scene ep9_burkes176 with dissolve
sa "Eh. Guilty pleasures..."
scene ep9_burkes178 with dissolve
mc "*{i}Whispers{/i}* But why?"
scene ep9_burkes180 with dissolve
sa "*{i}Whispers{/i}* Isn't it obvious?"
scene ep9_burkes178 with dissolve
if ep6_cluckTybaltState == 2:
    $ RPsage += 1
    mc "*{i}Whispers{/i}* Why haven't you told me?"
    scene ep9_burkes180 with dissolve
    sa "*{i}Whispers{/i}* I'm not exactly proud of it."
    sa "*{i}Whispers{/i}* But I almost did. Remember when we trash-talked him together?"
    scene ep9_burkes179 with dissolve
    mc "*{i}Whispers{/i}* Haha! Yes!"
    scene ep9_burkes181 with dissolve
    sa "*{i}Whispers{/i}* I fucking enjoyed that. Haha!"
else:
    mc "*{i}Whispers{/i}* I've seen your comments, but I'd never guess it was you."
    scene ep9_burkes180 with dissolve
    sa "*{i}Whispers{/i}* I'm not exactly proud of it, but no one else puts him in his place, so..."
    scene ep9_burkes179 with dissolve
    mc "*{i}Whispers{/i}* Haha! That's so funny!"

$ new_bio("Sage", "Sage is creating troll accounts to fuck with Tybalt on Rooster. She seems to hate her brother. While I'm not surprised that someone would hate Tybalt, I'm a bit surprised that she would hate her brother.")
scene ep9_burkes182 with fade
$ renpy.pause()
scene ep9_burkes183 with dissolve
$ renpy.pause()
scene ep9_burkes186 with dissolve
sa "I'm so sorry."
scene ep9_burkes184 with dissolve
my "Don't be. You did what you could."
scene ep9_burkes188 with dissolve
mc "He told you to quit college?"
scene ep9_burkes185 with dissolve
my "As a way to get out of the loan, I guess."
my "It's advice, but it's not what I want. And I'm not sure it would work since dad's got the money."
my "How would I even repay a loan without it?"
scene ep9_burkes187 with dissolve
sa "Maya, I think the next step is to get some legal help."
scene ep9_burkes184 with dissolve
my "I can't afford that."
scene ep9_burkes187 with dissolve
sa "Maybe there's someone we know who could help for free, then?"
scene ep9_burkes184 with dissolve
my "I don't know any lawyers. Do you?"
scene ep9_burkes186 with dissolve
sa "No, not personally. I could ask Dad again."
scene ep9_burkes184 with dissolve
my "You don't have to do that. You've helped me enough."
scene ep9_burkes189 with dissolve
js "I'll ask around for you."
scene ep9_burkes190 with dissolve
my "Thanks, everyone."
my "Shall we?"
scene ep9_burkes191 with dissolve
mc "*{i}Whispers{/i}* How come she's the only one not feeling down right now?"
js "*{i}Whispers{/i}* It's a defense mechanism... She's trying her best to cope."
stop music fadeout 3
scene ep9_burkes192 with dissolve
$ renpy.pause()
scene ep9_burkes193 with dissolve
sb "Priscilla. This is Stephen Burke."
sb "We need to talk."
$ new_bio("Josy", "Sage recommended that Maya get legal help, and Josy told Maya she'd ask around for it.")
$ new_bio("Sage", "Sage recommended that Maya get legal help, and Josy told Maya she'd ask around for it.")
$ new_bio("Maya", "Sage recommended that Maya get legal help, and Josy told Maya she'd ask around for it.")

label ep9_derek2_talk_label:
play music "music/ep9/licensed_music/track118.mp3"
scene ep9_derek2_talk14 with wipeleft
de "Maya told me about what happened. It sucked that you didn't invite me to it."
scene ep9_derek1_talk13 with dissolve
mc "It wasn't my call, and as you've said, you usually make things worse."
scene ep9_derek2_talk14 with dissolve
de "To me, it sounds like you did worse than I would have."
scene ep9_derek1_talk13 with dissolve
mc "Well... It wasn't the best. Fucking Tybalt..."
if ep4_toldDerekAboutJade:
    scene ep9_derek1_talk12 with dissolve
    de "What about Jade? That had to be awkward."
    scene ep9_derek1_talk13 with dissolve
    mc "Hey... Respect the secret code."
    scene ep9_derek2_talk14 with dissolve
    de "Sorry. You're right. Um..."

scene ep9_derek1_talk12 with dissolve
de "So... Another thing... Who is that hot girl you invited?"
scene ep9_derek2_talk15 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep9_derek2_talk16 with dissolve
$ renpy.pause()
label ep9_zoey_talk_label:
play music "<from 4>music/ep_interlude/licensed_music/track109.mp3"
scene ep9_zoey_talk1 with dissolve
$ renpy.pause()
scene ep9_zoey_talk2 with dissolve
$ renpy.pause()
$ renpy.sound.play("sound_effects/season3/skateboard.mp3", channel="sfx1", loop=True)
scene ep9_zoey_talk3 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep9_zoey_talk4 with dissolve
$ renpy.pause()
scene ep9_zoey_talk5 with dissolve
$ renpy.pause()
scene ep9_zoey_talk7 with dissolve
$ renpy.pause()

scene ep9_zoey_talk8 with dissolve
$ renpy.pause(0.5)
scene ep9_zoey_talk8b with Dissolve(3)
$ renpy.pause()

scene ep9_zoey_talk5 with dissolve
$ renpy.pause(0.5)
scene ep9_zoey_talk5b with Dissolve(3)
$ renpy.pause()

scene ep9_zoey_talk6 with dissolve
$ renpy.pause()
play sound "sound_effects/shove.mp3"
scene ep9_zoey_talk9 with hpunch
$ renpy.pause()
scene ep9_zoey_talk10 with dissolve
$ renpy.pause()
scene ep9_zoey_talk11 with dissolve
zo "Hey!"
menu:
    "Hey...":
        scene ep9_zoey_talk11b with dissolve
        mc "Hey..."
    "...":
        mc "..."
scene ep9_zoey_talk12 with dissolve
zo "Wow. You look good! Really good!"
scene ep9_zoey_talk13 with dissolve
menu:
    "Thanks":
        mc "Thanks... I got a new haircut."
        mc "Well, I got a few of them since last time."
        scene ep9_zoey_talk14 with dissolve
        $ renpy.pause()
    "You too":
        mc "You too. You've got a nice tan."
        scene ep9_zoey_talk14 with dissolve
        $ renpy.pause()
    "...":
        mc "..."
scene ep9_zoey_talk15 with dissolve
mc "How...are you?"
scene ep9_zoey_talk16 with dissolve
zo "I'm good. You?"
scene ep9_zoey_talk16b with dissolve
menu:
    "I don't know":
        scene ep9_zoey_talk17 with dissolve
        mc "I don't know. I've got mixed feelings about this... I've been both nervous and a bit shocked."
    "I'm fine":
        scene ep9_zoey_talk17 with dissolve
        mc "I'm fine."
mc "I don't know where to start... I had this speech practiced in my head for this day, but now it feels so stupid."
scene ep9_zoey_talk16 with dissolve
zo "You practiced a speech for me? Let's hear it."
scene ep9_zoey_talk17 with dissolve
mc "No, it's... It doesn't quite fit."
scene ep9_zoey_talk18 with dissolve
zo "We have a lot to catch up on, don't we?"
scene ep9_zoey_talk17 with dissolve
mc "Overwhelmingly much... It's been a while..."
scene ep9_zoey_talk18 with dissolve
zo "Yeah... It really has, huh? I don't even remember the last time we talked. Was it on Rooster?"
scene ep9_zoey_talk20 with dissolve
mc "No. I remember when it was. It was almost eight months ago..."
mc "That's when you stopped replying to my messages."
scene ep9_zoey_talk19 with dissolve
zo "Oh..."
scene ep9_zoey_talk20 with dissolve
mc "Yeah."
scene ep9_zoey_talk19 with dissolve
zo "I'm so sorry... You still remember that...?"
scene ep9_zoey_talk20 with dissolve
mc "Vividly."
mc "It was a Friday, which marked one week since I last texted you without a reply."
scene ep9_zoey_talk21 with dissolve
mc "I looked at my phone one last time. I scrolled through our chat history and it got me sad for the hundredth time since you left."
mc "I remembered how I felt with every single message I wrote to you. How the words I typed weren't the words I felt or wanted to say."
mc "So, I headed into town."
scene ep9_zoey_talk22 with dissolve
mc "It was raining that day; I wore my beige jeans as I rode my bike."
mc "I got drenched and it looked like I had pissed all over myself."
scene ep9_zoey_talk23 with dissolve
mc "I passed the courtyard where you taught me how to skate and smoke."
mc "I saw the lamp post I crashed into when I lost my balance skateboarding."
scene ep9_zoey_talk24 with dissolve
mc "I saw the dumpsters we used to sit on. The wall still had our half-assed graffiti attempt on it."
mc "I passed the corner where we'd wait for Debbie to get liquor for you from her brother."
mc "And I went to our mall..."
mc "That entire bike ride was like a trip down memory lane."
scene ep9_zoey_talk25 with dissolve
mc "I'm actually happy it rained that day. If it hadn't, everyone I passed would have seen the tears streaming down my face."
mc "It was the day I got my fresh start."
mc "I deleted everything on my phone and I bought a new SIM card...and I never sent you my new phone number."
scene ep9_zoey_talk26 with dissolve
mc "And after that day, I didn't have to stare at our chat history, hoping you'd send me something."
mc "I even stopped using Rooster for a long time."
mc "Knowing that you couldn't reach me felt so good, because I didn't have to keep lying to myself and pretend to be happy when I wrote you."
zo "..."
scene ep9_zoey_talk27 with dissolve
mc "And until now, I wasn't sure if you ever replied to me."
mc "And Dad telling me that you couldn't reach me now...after all these months. I don't know if it should make me feel better or worse."
scene ep9_zoey_talk26 with dissolve
zo "..."
scene ep9_zoey_talk25b with dissolve
zo "Your dad told me you've been happy..."
scene ep9_zoey_talk24 with dissolve
mc "Dad didn't want to embarrass me. He's seen me go through all these emotions and was unsure what to say to you."
mc "Besides, it's my story to tell you and, as I said, I'm done pretending everything's been fine."

scene ep9_zoey_talk28
if not persistent.ep9_cardji10:
    show screen ep9_render_screen("ji10")
with dissolve
$ renpy.pause()
scene ep9_zoey_talk27
hide screen ep9_render_screen
with dissolve
mc "I guess I can start by asking you..."
mc "Why are you back?"
scene ep9_zoey_talk29 with dissolve
zo "Damn... I already feel like a pile of human garbage, and now you're immediately hitting me with the million-dollar question."
scene ep9_zoey_talk30 with dissolve
mc "I mean... It's us."
mc "It wouldn't feel right to ignore the bad feelings and start pretending how great it's been to not see each other for all this time."
mc "I did enough of that this year..."
mc "And don't give me anything about how you don't like talking feelings because this time you're gonna fucking have to."
scene ep9_zoey_talk31 with dissolve
zo "You're mad at me..."
scene ep9_zoey_talk32 with dissolve
menu:
    "I'm mad":
        $ ep9_mad_at_zoey = True
        mc "You're damned right I'm mad at you."
        $ new_bio("Zoey", "When I met Zoey, I told her that I was mad at her.")
    "[mod_gr]I'm not mad":
        $ ep9_mad_at_zoey = False
        mc "My feelings are all over the place right now."
        $ new_bio("Zoey", "When I met Zoey, I told her my feelings were all over the place.")
zo "..."
scene ep9_zoey_talk31 with dissolve
zo "You're right. It wouldn't feel right to skip through that."
zo "I guess I'm back because... I've realized a lot about myself lately."
scene ep9_zoey_talk33 with dissolve
zo "I don't fit in on the West Coast. It wasn't me."
zo "The more time I spent over there, the more I started missing home."
zo "I was running out of money and San Diego never felt like my home."
scene ep9_zoey_talk35 with dissolve
mc "What about surfing?"
scene ep9_zoey_talk34 with dissolve
zo "I'm horrible at it. Like, seriously, I fucking stink."
scene ep9_zoey_talk35 with dissolve
mc "From what I remember, you were getting the hang of it."
scene ep9_zoey_talk33 with dissolve
zo "I did. Kinda. But I never got great at it, and I think it's because I didn't like it that much."
zo "It's so weird, you know? You build something up in your head for years, and when you finally get to do it, it's not nearly as good as you pictured it."
scene ep9_zoey_talk36 with dissolve
zo "And since it was the reason I went there, with time, I felt that... *{i}Sigh{/i}* What's the point?"
zo "And like I said, I missed this place. And I..."
zo "I missed you."
scene ep9_zoey_talk37 with dissolve
mc "..."
scene ep9_zoey_talk36 with dissolve
zo "You might have a hard time believing that because we haven't talked since before that Friday, eight months ago, but I did."
zo "And it became painfully clear with time."
scene ep9_zoey_talk37 with dissolve
mc "I didn't expect to hear that."
mc "I felt that we had drifted apart in all kinds of ways- Actually, it's part of the speech I wrote..."
scene ep9_zoey_talk33 with dissolve
zo "Yeah... There's a long story behind it I need to tell you sometime."
zo "There's just so much to say."
scene ep9_zoey_talk35 with dissolve
mc "Yeah..."
mc "And what about your boyfriend? You just left him there?"
scene ep9_zoey_talk38 with dissolve
zo "My boyfriend? I don't have a boyfriend."
scene ep9_zoey_talk35 with dissolve
mc "You do, that-"
scene ep9_zoey_talk34 with dissolve
zo "You do!"
scene ep9_zoey_talk37 with dissolve
mc "..."
scene ep9_zoey_talk36 with dissolve
zo "Sorry, wrong moment."
scene ep9_zoey_talk37 with dissolve
mc "That Bret guy."
scene ep9_zoey_talk33 with dissolve
zo "Bret's a close friend. You didn't think he was-?"
scene ep9_zoey_talk35 with dissolve
mc "I did, and then I saw this cluck you were tagged in."
scene ep9_zoey_talk36 with dissolve
zo "Oh, God..."
scene ep9_zoey_talk37 with dissolve
mc "Maybe I read into things... I tried to avoid looking at your feed, but some nights..."
mc "I had my weak moments..."
scene ep9_zoey_talk36 with dissolve
zo "*{i}Sigh{/i}* Maybe we should have started with the easy questions?"
scene ep9_zoey_talk37 with dissolve
mc "..."
scene ep9_zoey_talk33 with dissolve
zo "Here's one for you..."
zo "What are you up to these days?"
scene ep9_zoey_talk35 with dissolve
mc "Do you know I'm in college?"
scene ep9_zoey_talk34 with dissolve
zo "Yeah, I saw it. Congrats!"
scene ep9_zoey_talk35 with dissolve
mc "It's pretty much that. I'm studying and I pledged a frat."
scene ep9_zoey_talk34 with dissolve
zo "Your dad told me a bit about it. The dick boys or something?"
scene ep9_zoey_talk39 with dissolve
mc "Haha... Almost. Dad's not that good with names. It's the DIKs."
scene ep9_zoey_talk34 with dissolve
zo "Props to you. You've moved on to doing what you wanted, with college and all."
scene ep9_zoey_talk35 with dissolve
mc "What about you? What are you gonna do now?"
scene ep9_zoey_talk33 with dissolve
zo "Another easy question..."
scene ep9_zoey_talk35 with dissolve
mc "You don't know?"
scene ep9_zoey_talk33 with dissolve
zo "Right now, it feels good to be back home. Like, really good. I'll figure something out."
zo "I don't wanna live at home forever, but I don't have any rush to move out this time."
zo "And when I move out, I won't be going far; that I know."
scene ep9_zoey_talk35 with dissolve
mc "You could look for a job."
scene ep9_zoey_talk36 with dissolve
zo "Yeah. I probably will."
zo "Look, I... Fuck me. Why is it so hard to ask you stuff?"
zo "We've known each other for years!"
scene ep9_zoey_talk37 with dissolve
mc "..."
scene ep9_zoey_talk36 with dissolve
zo "I think it's hard because I'm scared of the answer when I see the look on your face..."
zo "Anyway, here it goes..."
scene ep9_zoey_talk40 with dissolve
zo "Can we, like, hang out again? I know it's hard to go back to how it was..."
zo "...but what I mean is that I wanna see you again. I miss talking to you."
zo "I was hoping that we could press play on what we paused..."
scene ep9_zoey_talk37 with dissolve
mc "Zoey. Things are different now. College and work are taking up most of my time."
mc "I'm different too. This last year has changed me."
scene ep9_zoey_talk36 with dissolve
zo "Yeah, I get it. You're busy. It's not a problem."
zo "I mean... Maybe I'll see you around when you come back home to visit your dad, at least?"
scene ep9_zoey_talk37 with dissolve
mc "Zoey..."
mc "Even though it felt like you threw me away..."
scene ep9_zoey_talk41 with dissolve
mc "Fuck... I tried so hard not to cry..."
scene ep9_zoey_talk42 with dissolve
$ renpy.pause()
scene ep9_zoey_talk43 with dissolve
mc "I wouldn't have been able to get through my speech anyway."
scene ep9_zoey_talk44 with dissolve
mc "I still wanna see you. I mean..."
mc "You've been my best friend for so many years."
scene ep9_zoey_talk45 with dissolve
zo "*{i}Sigh of relief{/i}*"
scene ep9_zoey_talk46 with dissolve
mc "But that's why it also hurts... It's gonna take some time for me. Because..."
mc "..."
scene ep9_zoey_talk47 with dissolve
zo "I have all the fucking time in the universe. I'm not losing your friendship..."
zo "...again."
scene ep9_zoey_talk46 with dissolve
mc "You've changed too."
scene ep9_zoey_talk47 with dissolve
zo "Yeah, I've got some tattoos and more piercings now."
scene ep9_zoey_talk46 with dissolve
mc "It's not just that."
mc "You're not punching me or telling me to stop crying."
mc "The old you wouldn't have lasted in this conversation very long."
scene ep9_zoey_talk48 with dissolve
zo "Haha!"
scene ep9_zoey_talk47 with dissolve
zo "Yeah... Maybe I softened up a little?"
scene ep9_zoey_talk46 with dissolve
mc "Is it a West Coast mentality?"
scene ep9_zoey_talk47 with dissolve
if zoey_dik:
    zo "I've not stopped being a dick, but I won't be today."
else:
    zo "Maybe that's it? I feel different."
scene ep9_zoey_talk46 with dissolve
mc "Whatever it is, I like it..."
scene ep9_zoey_talk49 with dissolve
zo "So... How's college?"
mc "It's...chaotic at times."
zo "Is it fun?"
scene ep9_zoey_talk46 with dissolve
mc "It has its ups and downs, but in general, it's a blast."
mc "You learn and party a lot."
scene ep9_zoey_talk47 with dissolve
zo "Don't tell me you're a party guy these days."
scene ep9_zoey_talk46 with dissolve
mc "A bit more than before, yeah. I think you'd be surprised."
mc "I still can't dance, though."
mc "And don't laugh, but I'm somewhat of a party planner now too."
scene ep9_zoey_talk48 with dissolve
zo "Hahaha! No way!"
scene ep9_zoey_talk48b with dissolve
mc "I just started, ok? Halloween's gonna be the first party I've helped plan."
scene ep9_zoey_talk49 with dissolve
stop music fadeout 3
zo "Halloween!? Dude, that's awesome! Tell me all about it."
$ new_bio("Zoey", "I told Zoey my side of the story, and we both cried. I just can't let go of her. She's meant too much to me over the years. But I'm not ready to just forget about this last year.")

label ep9_derek_talk4_label:
play music "music/ep9/licensed_music/track118.mp3"
scene ep9_derek4_talk1 with dissolve
de "So, you invited your ex to our Halloween party?"
scene ep9_derek4_talk2 with dissolve
mc "Yes."
scene ep9_derek4_talk1 with dissolve
de "Your ex?"
scene ep9_derek4_talk2 with dissolve
mc "Yes..."
scene ep9_derek4_talk1 with dissolve
de "To our Halloween party?"
scene ep9_derek4_talk2 with dissolve
mc "What's your point?"
scene ep9_derek4_talk3 with dissolve
de "Don't you see why that's a bad idea?"
scene ep9_derek4_talk2 with dissolve
mc "She's not just my ex... I don't think she ever saw me that way..."
mc "She's my best friend."
scene ep9_derek4_talk4 with dissolve
de "How dare you!"
scene ep9_derek4_talk5 with dissolve
mc "Well, she is...or was... I don't know. It's complicated."
$ guideSuggestedPage = 51
scene ep9_derek4_talk4 with dissolve
de "Answer me this - and don't you lie to me."
de "Is she a better friend than me?"
scene ep9_derek4_talk5b with dissolve
menu:
    "Yes":
        $ ep9_derek_better_friend = False
        if ep9_mad_at_zoey:
            mc "She's treated me like shit by ghosting me, and part of me is still mad at her for that...but still..."
        mc "She's my oldest friend, bro. You're a great friend, but she's pretty much irreplaceable."
        scene ep9_derek4_talk6 with dissolve
        de "*{i}Gasps{/i}*"
        scene ep9_derek4_talk7 with dissolve
        mc "Don't be like that. Zoey helped me get through some hard times-"
        scene ep9_derek4_talk11 with dissolve
        de "No, no. I heard you. Loud and clear."
        de "Derek out."
        $ new_bio("Derek", "I told Derek that Zoey is a better friend to me than he is.")
    "No":
        $ ep9_derek_better_friend = True
        if ep9_mad_at_zoey:
            mc "No, she's not a better friend than you."
        else:
            mc "No, she's not a better friend than you. She's great, but she left me and stopped talking to me."
        scene ep9_derek4_talk5c with dissolve
        if ep9_mad_at_zoey:
            mc "She cut me out of her life without even talking to me about it. I'm having a hard time forgiving her for that."
        else:
            mc "It felt like she was cutting me out of her life. It's hard to forget about that."
        mc "But we used to be best friends and she's helped me get through some hard times in life."
        scene ep9_derek4_talk8 with dissolve
        de "I got it. Let me talk to her and see what I can do for you."
        scene ep9_derek4_talk9 with dissolve
        mc "Hey. You don't have to do anything for me. Don't talk to her and tell her things about me."
        scene ep9_derek4_talk10 with dissolve
        de "Don't worry, [mc_de]. I can be a real sweetheart."
        $ new_bio("Derek", "I told Derek that he is a better friend to me than Zoey.")
scene ep9_derek4_talk12 with dissolve
$ renpy.pause()
scene ep9_derek4_talk13
if not persistent.ep9_cardji7:
    show screen ep9_render_screen("ji7")
with dissolve
mc "*{i}Sigh{/i}*"
stop music fadeout 3
mc "(I better get my costume ready.)"

label ep9_wave1_label:
scene ep9_wave1_1
hide screen ep9_render_screen
with dissolve
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track115.mp3"])
mc "{i}That night, the guests came in waves.{/i}"
scene ep9_wave1_2 with dissolve
mc "{i}First to the party were the dormies.{/i}"
mc "{i}As Tommy explained, dorm people who love to party with us come early, so they don't miss out.{/i}"
scene ep9_wave1_3 with dissolve
mc "{i}They aren't the most fun people to hang around, but some of them might surprise you.{/i}"
if pp_activity_choices[0] == 1:
    mc "{i}We all looked forward to the drinking competition. The party was off to a great start.{/i}"
elif pp_activity_choices[0] == 0:
    mc "{i}We had a shot battle coming up, so fun times started early on.{/i}"
else:
    mc "{i}We didn't have anything special planned for them, but fun times started early even so.{/i}"

scene ep9_wave1_4 with dissolve
mc "(There. Now it's not just a skirt.)"
scene ep9_wave1_5 with dissolve
mc "(Where's my sword...?)"
mc "(Dammit... Where did I put it?)"

jump ep9_freeroam_diks_ph1_label

label ep9_after_ph1_freeroam_label:
if branchIsabella:
    jump ep9_bella_branch_label
elif branchSage:
    jump ep9_sage_branch_label
elif branchJill:
    jump ep9_jill_branch_label
elif branchMayaJosy:
    jump ep9_jm_branch_label
else:
    jump ep9_others_branch_label

label ep9_wave2_label:
if branchIsabella:
    scene ep9_wave2_1 with dissolve
else:
    scene ep9_wave2_1b with dissolve
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track126.mp3","music/ep9/licensed_music/track125.mp3"])
mc "{i}The HOTs came later than expected.{/i}"
mc "{i}At least it felt that way; maybe it's because the dormies came early.{/i}"
scene ep9_wave2_8 with dissolve
mc "{i}Showing up a bit late was the HOTs' thing tonight. It was like they were the main event.{/i}"
mc "{i}And boy, did they look the part.{/i}"
scene ep9_wave2_9 with dissolve
qu "All right, party people! You can stop wondering where the party's at - it just arrived."
scene ep9_wave2_10 with dissolve
$ renpy.pause()
scene ep9_wave2_11 with dissolve
$ renpy.pause()
scene ep9_wave2_12 with dissolve
$ renpy.pause()
scene ep9_wave2_13 with dissolve
$ renpy.pause()
scene ep9_wave2_14 with dissolve
$ renpy.pause()
scene ep9_wave2_15 with dissolve
$ renpy.pause()
scene ep9_wave2_16 with dissolve
$ renpy.pause()
scene ep9_wave2_17 with dissolve
$ renpy.pause()
scene ep9_wave2_18 with dissolve
$ renpy.pause()
scene ep9_wave2_19 with dissolve
$ renpy.pause()
scene ep9_wave2_20 with dissolve
$ renpy.pause()
scene ep9_wave2_21 with dissolve
$ renpy.pause()
scene ep9_wave2_22 with dissolve
$ renpy.pause()
scene ep9_wave2_23 with dissolve
$ renpy.pause()
scene ep9_wave2_24 with dissolve
$ renpy.pause()
scene ep9_wave2_25 with dissolve
$ renpy.pause()
scene ep9_wave2_26 with dissolve
$ renpy.pause()
scene ep9_wave2_27 with dissolve
$ renpy.pause()
scene ep9_wave2_28 with dissolve
$ renpy.pause()
scene ep9_wave2_29 with dissolve
$ renpy.pause()
scene ep9_wave2_30 with dissolve
$ renpy.pause()
scene ep9_wave2_2 with dissolve
de "I don't see Ashley..."
scene ep9_wave2_3 with dissolve
mc "Maybe she's in a costume? It can be hard to tell."
scene ep9_wave2_2 with dissolve
de "Yeah, I'm gonna look for her."
$ guideSuggestedPage = 60
if branchIsabella and not branchJill:
    scene ep9_wave2_31 with dissolve
    mc "There's Jill."
    scene ep9_wave2_4 with dissolve
    isa "I see her."
    scene ep9_wave2_5 with dissolve
    mc "So, what's the plan?"
    scene ep9_wave2_6 with dissolve
    isa "I don't know yet. I don't want to scare her away."
    scene ep9_wave2_5 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
    menu:
        "Take it easy [mod_gr][mod_choices[2]]":
            $ dk(-1)
            mc "Take it easy with her and you won't."
            scene ep9_wave2_6 with dissolve
            isa "I hope so."
        "Joke [mod_gr][mod_choices[3]]":
            $ dk(1)
            mc "Is she scared of mummies?"
            scene ep9_wave2_7 with dissolve
            isa "..."

    if pathMayaJosy:
        scene ep9_wave2_32 with dissolve
        mc "(And there are Josy and Maya...)"
        mc "(I can't avoid them tonight... Fuck... Now I regret not telling them sooner about my decision.)"
        mc "(If I play it cool and friendly, I should be fine.)"
    scene ep9_wave2_5 with dissolve
    mc "I'm gonna greet the HOTs and check if everything's under control with the party. Will you be ok?"
    scene ep9_wave2_6 with dissolve
    isa "Don't worry about me. Come find me when you're done."
elif not branchMayaJosy and pathMayaJosy:
    scene ep9_wave2_32 with dissolve
    mc "(There's Josy and Maya...)"
    mc "(I can't avoid them tonight... Fuck... Now, I regret not telling them sooner about my decision.)"
    mc "(If I play it cool and friendly, I should be fine.)"

scene ep9_wave2_33
if not persistent.ep9_cardji8:
    show screen ep9_render_screen("ji8")
with dissolve
sa "[name]!"
if branchSage:
    scene ep9_wave2_34
    hide screen ep9_render_screen
    with dissolve
    sa "*{i}Smack{/i}*"
    scene ep9_wave2_34b with dissolve
    $ renpy.pause()
    scene ep9_wave2_34c with dissolve
    sa "*{i}Smack{/i}* Mmm! Finally!"
    if not branchMayaJosy and pathMayaJosy:
        scene ep9_wave2_35 with dissolve
        mc "(They didn't see that...right?)"
        sa "Uh? [name]? Over here?"
        scene ep9_wave2_36 with dissolve
        mc "Hey!"
    else:
        scene ep9_wave2_36 with dissolve
        mc "Yeah! Finally! I've been waiting for you."
    scene ep9_wave2_37 with dissolve
else:
    scene ep9_wave2_37
    hide screen ep9_render_screen
    with dissolve
    mc "Whoa! Hey!"
menu:
    "Nice costume":
        mc "Nice costume!"
        scene ep9_wave2_39 with dissolve
        sa "Likewise! I thought it would be a tad boring, but after trying it on I went with it."
    "You look hot":
        mc "Wow! You look hot in that!"
        scene ep9_wave2_39 with dissolve
        sa "Duly noted. And likewise!"
    "Where's your costume?":
        mc "I'm confused. Where's your costume?"
        scene ep9_wave2_38 with dissolve
        sa "Tsk! That's all you got?"
        scene ep9_wave2_37 with dissolve
        mc "Haha! You look good."
        scene ep9_wave2_39 with dissolve
        sa "You too!"

scene ep9_wave2_40 with dissolve
qu "Yeah, yeah. You're a hottie, I'm a hottie, we're all a bunch of hotties."
qu "[name], give me the rundown."
scene ep9_wave2_41 with dissolve
mc "Uh... I think everything's under control now."
mc "But people are still dropping in by the minute, and many came uninvited."
scene ep9_wave2_42 with dissolve
sa "It doesn't look too crowded to me."
scene ep9_wave2_41 with dissolve
mc "Luckily, it's a big mansion. As long as the alphas don't show up, we're good. Did you take care of that?"
scene ep9_wave2_43 with dissolve
qu "Haha! Oh, yeah. I took care of it."
scene ep9_wave2_44 with dissolve
mc "What did you do?"
scene ep9_wave2_43 with dissolve
qu "Let's just say they're on a road trip."
scene ep9_wave2_44 with dissolve
mc "What?"
scene ep9_wave2_45 with dissolve
qu "I'll tell you later. Right now, I aim to get hammered."

if branchSage:
    scene ep9_wave2_46 with dissolve
    sa "Fucking same! Come, [name]. I wanna talk to you."
    scene ep9_wave2_48 with dissolve
    mc "I'll join you in a minute; I'm gonna say hi to everyone first."
else:
    scene ep9_wave2_47 with dissolve
    sa "Wait for me!"

scene ep9_wave2_49 with dissolve
my "Look! There's [name]!"
js "Wow!"
scene ep9_wave2_50 with dissolve
mc "En garde!"
scene ep9_wave2_51 with dissolve
my "Isn't that a fencing term?"
scene ep9_wave2_52 with dissolve
mc "I don't know. Probably."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+2 Josy)","(+2 Maya)","(-DIK)","(+DIK)","(+Maya/Josy)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
if branchMayaJosy:
    mc "I see you're still looking great in those outfits."
    menu:
        "Notice Josy's hairstyle [mod_gr][mod_choices[0]]":
            $ RPjosy += 2
            scene ep9_wave2_53 with dissolve
            mc "And wow! I think this is the first time I've seen you wear your hair like that."
            scene ep9_wave2_54 with dissolve
            js "I wanted something special for Halloween."
            scene ep9_wave2_53 with dissolve
            mc "It looks great!"
            scene ep9_wave2_55 with dissolve
            js "Thank you! Have you seen Maya, though? It took us ages to do that."
            scene ep9_wave2_56 with dissolve
            my "No kidding. But it was worth it."
            scene ep9_wave2_57 with dissolve
            js "Totally!"
        "Notice Maya's hairstyle [m_c2][mod_choices[1]]":
            $ RPmaya += 2
            scene ep9_wave2_57 with dissolve
            mc "Maya, your hair is amazing!"
            scene ep9_wave2_56 with dissolve
            my "Thanks! That's good, considering the time Josy and I spent on it."
            scene ep9_wave2_54 with dissolve
            js "It was such a nightmare, but we did it!"
            scene ep9_wave2_57 with dissolve
            mc "Beautiful."
        "Notice their hairstyles [mod_gr][mod_choices[4]]":
            $ RPjosy += 1
            $ RPmaya += 1
            mc "I don't know who to compliment first. You both look amazing."
            mc "And your hairstyles! Wow!"
            scene ep9_wave2_55 with dissolve
            js "I get why you think Maya's hair is great, but mine? Come on."
            scene ep9_wave2_53 with dissolve
            mc "It's just that I haven't seen you wear it like that before. You always have it in a ponytail or buns."
            scene ep9_wave2_54 with dissolve
            js "Well... Thanks."
            scene ep9_wave2_57 with dissolve
            mc "And yours... I just wanna touch it!"
            scene ep9_wave2_58 with dissolve
            my "Haha! Don't! We spent a full hour making it."
            scene ep9_wave2_54 with dissolve
            js "Yeah, it was a nightmare!"
    scene ep9_wave2_52 with dissolve
    mc "So, welcome to our party. I hope you're not scared easily."
    scene ep9_wave2_59 with dissolve
    my "Considering how scared you were from watching movies, it can't be too scary or we'd notice."
    scene ep9_wave2_52 with dissolve
    mc "It's more fun than scary to me. But some decorations might surprise you. Have a look around and enjoy."
    mc "There are drinks all over the place, so grab anything you want and have fun!"
    scene ep9_wave2_60 with dissolve
    js "Are you having a drink with us later?"
    scene ep9_wave2_52 with dissolve
    mc "Of course! Let me greet the rest of the guests and I'll come find you after."
else:
    mc "Those are some great costumes."
    scene ep9_wave2_54 with dissolve
    js "Thanks! It was pretty damn hard finding something to wear."
    scene ep9_wave2_53 with dissolve
    mc "Oh? Were the stores out of stock?"
    scene ep9_wave2_62 with dissolve
    my "*{i}Sigh{/i}* No. It's because of me."
    scene ep9_wave2_54 with dissolve
    js "I thought we could buy something cheap to wear, but Maya insisted we should get something good for Halloween."
    js "After some back and forth, we got these."
    scene ep9_wave2_53 with dissolve
    mc "That's a good choice, if you ask me."
    scene ep9_wave2_62 with dissolve
    my "See...? [name] gets it."
    scene ep9_wave2_63 with dissolve
    js "Excuse me for trying to save us money."
    scene ep9_wave2_61 with dissolve
    menu:
        "[mod_gr]Don't fight tonight":
            $ ep9_jm_fight = False
            mc "Hey, don't fight tonight. We're here to have fun!"
            scene ep9_wave2_62 with dissolve
            my "We're not fighting. It's..."
            my "Ok, I guess we were fighting a bit. Sorry, Josy."
            scene ep9_wave2_63 with dissolve
            js "I only mean well."
            scene ep9_wave2_62 with dissolve
            my "I know you do. But I wanted to have fun tonight and not, you know, think about..."
            scene ep9_wave2_63 with dissolve
            js "We should."
            scene ep9_wave2_52 with dissolve
            mc "Yes, you absolutely should!"
            mc "There are drinks just about everywhere, so have fun! I have to greet some more guests."
        "Anyway...":
            $ ep9_jm_fight = True
            mc "Anyway... There are drinks just about everywhere, so have fun! I have to greet some more guests."
scene ep9_wave2_54 with dissolve
js "Don't forget to greet Jill; she came with us and some friends of hers."
scene ep9_wave2_64 with dissolve
mc "Will do."
if branchJill:
    if pathMayaJosy:
        mc "(Luckily, Josy and Maya don't seem to know about Jill and me yet...)"
    else:
        mc "(Josy and Maya don't seem to know about Jill and me yet.)"
else:
    scene ep9_wave2_65 with dissolve
    mc "(Jill...)"
    scene ep9_wave2_66 with dissolve
    if ep9_jill_mood == 1:
        mc "(I haven't talked to her since I told her the news...)"
        stop music fadeout 3
        scene ep9_wave2_72 with dissolve
        $ renpy.pause()
        hide screen new_phone_screen
        jump ep9_jill_closure_label
        label ep9_jill_after_closure_label:
        show screen new_phone_screen
        $ mphone_play_songs(["music/ep8/starfire.mp3"])
        scene ep9_wave2_72 with dissolve
        mc "(It was one of the most awful moments in my life...)"
        mc "(We sat there for an hour crying before she walked away.)"
        mc "(I hope she's been doing all right.)"
        scene ep9_wave2_67 with dissolve
        $ renpy.pause()
        scene ep9_wave2_68 with dissolve
        $ renpy.pause()
        scene ep9_wave2_73 with dissolve
        $ renpy.pause()
        scene ep9_wave2_71 with dissolve
        mc "(I guess I should take it as a good sign that she came. That must count for something.)"
        scene ep9_wave2_74 with dissolve
        mc "(Fuck... Snap out of it. Do what Derek told you...)"
        mc "(Force a smile on your face and you'll manage through the toughest of times.)"
        $ new_bio("Jill", "I broke up with Jill. Well, we weren't a couple, but I told her I couldn't date her anymore, and she didn't take it well.")
    elif ep9_jill_mood > 1:
        stop music fadeout 3
        mc "(I wonder how she's been since I talked to her about Bella...)"
        scene ep9_wave2_72 with dissolve
        $ renpy.pause()
        hide screen new_phone_screen
        jump ep9_jill_bclosure_label
        label ep9_jill_after_bclosure_label:
        show screen new_phone_screen
        $ mphone_play_songs(["music/ep8/starfire.mp3"])
        scene ep9_wave2_72 with dissolve
        if ep9_jill_mood == 3:
            mc "(It was one of the most awful moments in my life...)"
            mc "(We sat there for an hour crying before she walked away.)"
            $ new_bio("Jill", "I opened up to Jill about my feelings for Bella. It was awful breaking her heart like that, but I had to be honest with her.")
            if ep9_b_kissed_jill:
                $ new_bio("Jill", "When I broke up with her, Jill tried to kiss me, and I kissed her back. Maybe it was stupid, but I have feelings for her too.")
        else:
            mc "(It felt like she understood what I told her. But still... Can she forgive Bella?)"
            $ new_bio("Jill", "I opened up to Jill about my feelings for Bella. It was weird, but I hope that Jill will understand our relationship someday.")
        mc "(I hope she's been doing all right.)"
        if ep9_jill_mood == 3:
            scene ep9_wave2_67 with dissolve
            $ renpy.pause()
            scene ep9_wave2_68 with dissolve
            $ renpy.pause()
            scene ep9_wave2_73 with dissolve
            $ renpy.pause()
            scene ep9_wave2_71 with dissolve
            mc "(Well, that's something.)"
        else:
            scene ep9_wave2_70 with dissolve
            $ renpy.pause()
            scene ep9_wave2_69 with dissolve
            $ renpy.pause()
            scene ep9_wave2_73 with dissolve
            $ renpy.pause()
    else:
        if pathJill:
            stop music fadeout 3
            if ep8_jill_rejected_you:
                mc "(I'm happy we could talk about us again after that horrible rejection...)"
            else:
                mc "(It was tough having that talk with her...)"
            scene ep9_wave2_72 with dissolve
            $ renpy.pause()
            hide screen new_phone_screen
            jump ep9_jill_closure_label
            label ep9_jill_after_closure2_label:
            show screen new_phone_screen
            $ mphone_play_songs(["music/ep8/starfire.mp3"])
            scene ep9_wave2_72 with dissolve
            if ep8_jill_rejected_you:
                mc "(It sucked hard...but I understand her better because of it...)"
            else:
                mc "(Even though I hated talking about it, I'm glad I did it.)"
            $ new_bio("Jill", "I talked to Jill about our relationship. It went well, and we left as friends.")
        else:
            mc "(I'm both happy and surprised she showed up.)"
        scene ep9_wave2_70 with dissolve
        $ renpy.pause()
        scene ep9_wave2_69 with dissolve
        $ renpy.pause()
        scene ep9_wave2_73 with dissolve
        if ep8_jill_rejected_you:
            mc "(Ok... It still hurts a bit to see her. But I can't force her to feel the same way as me.)"
            mc "(At least we can stay friends... It's better than nothing.)"
        elif pathJill:
            mc "(I'm happy she's taking it well.)"
        else:
            mc "(Looks like she's happy being here too. That's good.)"
$ guideSuggestedPage = 61
scene ep9_wave2_75 with dissolve
mc "Sarah... Melanie..."
if not pp_activity_choices[0] == 0 and persistent.mod_wtenabled and (not branchAlone or wt_ep9_branch_numbers > 1):
    "scrappy" "From this point on you get a new stat/points that's on non others/alone paths. I didn't see any info on it so I just assume it's cheating on you girl/path score and I'll show in menu with [mod_gr](+cheater)"

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="{color=#E6F653}(+Cheater)"
                             
menu:
    "[mod_gr]Hot!":
        mc "You're looking very hot tonight! Loving the theme costume."
        scene ep9_wave2_77 with dissolve
        sar "You haven't even seen the best part of it."
        scene ep9_wave2_78 with dissolve
        mc "What's that?"
        scene ep9_wave2_80 with dissolve
        mc "Oof..."
        scene ep9_wave2_79 with dissolve
        menu:
            "[mod_gr]You're killing me":
                mc "You girls are killing me here..."
                if affinity == "DIK":
                    menu:
                        "Grab asses [mod_gr][mod_choices[3]][mod_gr][mod_choices[10]]":
                            $ dk(1)
                            if not branchAlone or wt_ep9_branch_numbers > 1:
                                $ tc += 1
                            scene ep9_wave2_81 with dissolve
                            ml "Not even 10 minutes into the party and someone grabs our asses."
                            scene ep9_wave2_82 with dissolve
                            sar "I'd expect nothing less from this guy."
                        "Don't grab them":
                            $ renpy.pause(0.5)
            "I prefer the front":
                $ dk(1)
                mc "Meh. I prefer the front."
                scene ep9_wave2_83 with dissolve
                sar "Dick!"
                scene ep9_wave2_84 with dissolve
                if affinity == "CHICK":
                    mc "That's a compliment, but whatever."
                else:
                    mc "You know it."
    "Fun costumes":
        mc "Fun costumes! Animal theme, huh?"
        scene ep9_wave2_76 with dissolve
        sar "Animal theme? This guy."
        ml "Haha!"
$ guideSuggestedPage = 62
scene ep9_wave2_85 with dissolve
tm "[name]. Can you do me a solid?"
scene ep9_wave2_87 with dissolve
mc "More shit that rolls downhill?"
scene ep9_wave2_86 with dissolve
tm "Eh..."
tm "Look out for my sister tonight."
scene ep9_wave2_87 with dissolve
mc "Why?"
scene ep9_wave2_86 with dissolve
tm "There are a lot of cocks in disguise here. Make sure some asshole doesn't harass her."
scene ep9_wave2_87 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Ok [mod_gr][mod_choices[0]]":
        $ RPdiks += 1
        mc "I'll keep an eye out."
    "She doesn't need it":
        mc "I think she can take care of herself."
mc "It sounds like you care about her."
scene ep9_wave2_88 with dissolve
tm "Fuck you. I don't want some dick to tell me he fucked my sister. You can't shake that label once you have it."

scene ep9_wave2_89 with dissolve
mc "Whoa! Heather?"
scene ep9_wave2_90 with dissolve
he "What?"
scene ep9_wave2_89 with dissolve
menu:
    "Nice hair":
        mc "Nice hair!"
        scene ep9_wave2_91 with dissolve
        he "Nice hair? You were looking 20 inches south of my \"nice hair\"."
        scene ep9_wave2_92 with dissolve
        mc "I'm a judge in the best costume competition, don't blame me."
    "Tease":
        scene ep9_wave2_92 with dissolve
        mc "A little late for the beach season, don't you think?"
        scene ep9_wave2_91 with dissolve
        he "Yeah, but I fucking hate winter. This makes me feel better."
    "I recognize that outfit":
        scene ep9_wave2_92 with dissolve
        mc "I recognize that outfit..."
        mc "Wait a minute! Is that the bathing suit I wore during Hell Week?"
        scene ep9_wave2_91 with dissolve
        he "Yeah, but I've washed it many times since."
        if affinity == "DIK":
            scene ep9_wave2_93 with dissolve
            mc "That's the closest my dick has ever been to your pussy."
            scene ep9_wave2_94 with dissolve
            he "What's wrong with you?"
            scene ep9_wave2_93 with dissolve
            mc "I was only joking."
        else:
            scene ep9_wave2_92 with dissolve
            mc "Yikes... I can't believe we're the same size."
    "Flirt":
        if affinity == "DIK":
            $ dk(1)
            scene ep9_wave2_93 with dissolve
            mc "If I drown in the bathtub, will you come and save me? I might need mouth-to-mouth."
            scene ep9_wave2_94 with dissolve
            he "What's wrong with you?"
            scene ep9_wave2_93 with dissolve
            mc "I was only joking."
            mc "You're looking great! Tommy's a lucky guy."
        else:
            scene ep9_wave2_92 with dissolve
            mc "Top three costumes at the party, hands down! Loving it!"

scene ep9_wave2_95 with dissolve
mc "Camila!"
scene ep9_wave2_96 with dissolve
cam "Haha, [name]. Go ahead and get it done. Gush over how good I look."
scene ep9_wave2_97 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
menu:
    "Flirt":
        mc "If I only knew where to start! You should consider wearing that outfit in class. Grr!"
        scene ep9_wave2_96 with dissolve
        cam "Haha, someone's in a good mood tonight."
        scene ep9_wave2_97 with dissolve
        mc "Join me, will you? There are drinks everywhere. Go nuts!"
        jump ep9_cammy_kiss_label
    "[mod_gr]Tease":
        mc "I was gonna ask why you didn't put on a costume."
        scene ep9_wave2_96 with dissolve
        cam "Oh! Come on! Are you that blind? Do you think I would wear this normally?"
        scene ep9_wave2_97 with dissolve
        mc "It looks hot and sophisticated at once, but is it a costume? Hm...?"
        scene ep9_wave2_98 with dissolve
        cam "Look. It is a hot costume."
        scene ep9_wave2_99 with dissolve
        cam "We clearly had the same ideas, you and I. Showing off the goods."
        mc "I...don't know what you mean by that."
        scene ep9_wave2_96 with dissolve
        cam "Yeah, let's pretend it's not."
        label ep9_cammy_kiss_label:
        scene ep9_wave2_100 with dissolve
        menu:
            "Kiss [mod_gr][mod_choices[10]]":
                if not branchAlone:
                    $ tc += 1
                scene ep9_wave2_101 with dissolve
                cam "*{i}Mwah{/i}*"
            "Don't kiss":
                scene ep9_wave2_102 with dissolve
                cam "*{i}Mwah{/i}*"
        scene ep9_wave2_96 with dissolve
        cam "Cutie."
    "Compliment her":
        mc "You do look great. Guys are going to flock around you tonight."
        scene ep9_wave2_96 with dissolve
        cam "Oh, really? Including you?"
        scene ep9_wave2_103 with dissolve
        mc "Me? I have battles to fight. Brought my sword."

scene ep9_wave2_104 with dissolve
mc "Oh no! Rio the cat monster!"
ri "Monster? What the fuck!"
scene ep9_wave2_105 with dissolve
mc "I'm joking, of course."
menu:
    "Cute costume":
        mc "That is such a cute costume!"
        scene ep9_wave2_107 with dissolve
        ri "Aw! Thank you!"
        ri "But it's hot too, right? Camila said it wasn't."
        scene ep9_wave2_108 with dissolve
        mc "I mean, the makeup and the paws and all... That's what's cute."
        scene ep9_wave2_114 with dissolve
        mc "But yeah... Looking closer, it's also hot!"
        scene ep9_wave2_110 with dissolve
        ri "I nailed it, huh?"
        scene ep9_wave2_108 with dissolve
        mc "You sure did! Who doesn't like cats?"
    "Compliment her":
        mc "What a great costume. I'm happy you've put this much effort into it."
        scene ep9_wave2_107 with dissolve
        ri "It may not look like it, but the face painting was so hard."
        scene ep9_wave2_108 with dissolve
        mc "It was? It's only a couple of lines, no?"
        scene ep9_wave2_107 with dissolve
        ri "Well... The lines have to be perfect and straight."
        scene ep9_wave2_108 with dissolve
        if ep7_riona_lewd:
            mc "Right. I forgot about your OCD."
            scene ep9_wave2_111 with dissolve
            ri "I don't have OCD."
            scene ep9_wave2_112 with dissolve
            mc "Of course, you don't. If you had OCD, you'd notice one of those lines being far off to the left."
            ri "What?"
            mc "Got you!"
            scene ep9_wave2_113 with dissolve
            ri "*{i}Sigh{/i}* Ha-ha. Not!"
        else:
            mc "Yeah, imagine if they weren't."
    "Joke":
        $ ep9_rio_joke = True
        mc "Feline good tonight?"
        scene ep9_wave2_109 with dissolve
        ri "HAHA! God, what a corny joke!"
        scene ep9_wave2_108 with dissolve
        mc "You don't like puns?"
        scene ep9_wave2_110 with dissolve
        ri "Who does? Only dads and old people, no?"
        scene ep9_wave2_108 with dissolve
        mc "Hey! Don't be catty."
        scene ep9_wave2_109 with dissolve
        ri "Ugh... Cringe! Please, stop."
        scene ep9_wave2_108 with dissolve
        mc "Haha, ok. You're very cute in that outfit."
scene ep9_wave2_106 with dissolve
ri "Meow!"

scene ep9_wave2_115 with dissolve
mc "(I think I missed some of the HOTs. Oh well, I'll catch them later.)"
mc "(Everyone's looking great tonight. It feels like most girls are dressed sexy.)"

if branchSage:
    jump ep9_sage_drink_label
elif branchJill:
    jump ep9_jill_banana_event_label
else:
    jump ep9_freeroam_diks_ph2_label

label ep9_jill_closure_label:
play music "music/ep9/getting_closure.mp3"
scene ep9_jill_closure1 with dissolve
mc "Thanks for coming."

if ep8_jill_rejected_you:
    scene ep9_jill_closure2 with dissolve
    ji "Of course... [name]... I don't feel good about how we left things off at the restaurant."
    ji "Can we talk about it?"
    scene ep9_jill_closure4 with dissolve
    mc "That was why I asked you to come."
    scene ep9_jill_closure5 with dissolve
    ji "Oh? Good... How are you feeling?"
    scene ep9_jill_closure4 with dissolve
    mc "I've been ok. It was rough at first because I didn't expect you to shoot me down like that..."
    scene ep9_jill_closure5 with dissolve
    ji "I'm terribly sorry, [name]. I was fired up and it wasn't the right moment to say those things to you."
    scene ep9_jill_closure4 with dissolve
    mc "Well, you're entitled to your feelings."
    mc "For me, it still hurts, but I'll be ok."
    scene ep9_jill_closure5 with dissolve
    ji "[name]... I'm very sorry."
    scene ep9_jill_closure4 with dissolve
    mc "There's one thing I wanted to ask you about it..."
else:
    scene ep9_jill_closure3 with dissolve
    ji "Of course. I've missed you. How have you been?"
    scene ep9_jill_closure4 with dissolve
    mc "*{i}Sigh{/i}* Lately... Not that good."
    scene ep9_jill_closure5 with dissolve
    ji "Did something happen?"
    scene ep9_jill_closure4 with dissolve
    mc "Yeah... Please, don't hate me for this."
    scene ep9_jill_closure6 with dissolve
    mc "Not that long ago, I made a decision that involves you."
    mc "I'm gonna rip the band-aid off and say it..."
    mc "I can't date you anymore."
    scene ep9_jill_closure7 with dissolve
    if branchAlone:
        mc "I was unsure about us and realized I wasn't ready for a relationship."
        mc "And that I look forward to dating others."
    else:
        mc "There's someone else I want to be with."
    mc "You and I never felt completely right for each other."
    mc "Fuck... *{i}Exhales{/i}* I'm so sorry."

if ep8_jill_rejected_you or (not ep7_jill_lewd or affinity == "DIK" or ep8_jill_state != 1):
    if not ep8_jill_rejected_you:
        scene ep9_jill_closure8 with dissolve
        ji "[name]. It's ok. Breathe."
        ji "Trust me. It's ok."
        ji "You're not alone in thinking about us that way."
        ji "Recently, I've felt that I'm not cut out for dating you either."
        scene ep9_jill_closure10 with dissolve
        ji "To be perfectly honest, I don't feel cut out for dating at all."
        if branchAlone:
            ji "I feel this need to be alone. Just like you do."
        else:
            ji "I feel this need to be alone."
        scene ep9_jill_closure6 with dissolve
        mc "Are you sure that's what you feel?"
        scene ep9_jill_closure8 with dissolve
        ji "[name]. You're sweet, and you make me laugh. You're challenging..."
        if not ep8_recital_failed:
            ji "And how you helped me during the recital I'll be forever grateful to you."
        if not ep6_jill_lewd:
            ji "But...the spark's not there for me. I don't know if it will be, either."
        else:
            ji "But...I'm not sure about us either."
        ji "And when I have these doubts about us, and you seem sure I'm not who you're looking for..."
        scene ep9_jill_closure11 with dissolve
        ji "..."
        scene ep9_jill_closure12 with dissolve
        if branchAlone:
            ji "It makes me happy that you've decided to find love elsewhere."
        else:
            ji "It makes me happy that you've found someone else."
        ji "It feels like a smart choice... Even though I've had a wonderful time with you."
        scene ep9_jill_closure13 with dissolve
        mc "That's very big of you..."
        mc "I've been wondering where it went wrong between us."
    else:
        scene ep9_jill_closure6 with dissolve
        mc "I've been wondering where it went wrong. Because I don't get it..."
        mc "I thought it felt good between us."
    if ep8_jill_rejected_you:
        scene ep9_jill_closure7 with dissolve
    else:
        scene ep9_jill_closure10 with dissolve
    ji "It's hard to pinpoint it..."
    if not ep6_jill_lewd:
        ji "But for me... We didn't spend enough time together."
        ji "Instead of exploring to see if there was a spark, we didn't."
        ji "And it turned into a nice friendship instead."
    else:
        ji "I thought we had a spark at first."
        if not ep7_jill_lewd:
            ji "But it might just have been a crush that didn't fully develop into something."
            ji "And Tybalt didn't do us any good either."
            ji "It ended up staying a friendship."
        else:
            ji "But it might just have been a crush. There's no denying we are quite different from each other."
            ji "I think that's what made me hesitate."
            ji "I wanted to try and push myself, but my gut kept telling me no and that's what I feel."
    if not ep8_jill_rejected_you:
        scene ep9_jill_closure14 with dissolve
        ji "What about you? What do you think it was?"
        scene ep9_jill_closure13 with dissolve
        menu:
            "Feelings for someone else" if not branchAlone:
                mc "I simply think it's because I found someone else I wanted to be with."
                scene ep9_jill_closure14 with dissolve
            "Didn't click with you":
                mc "I felt that we didn't click."
                if not ep6_jill_lewd:
                    mc "I thought I was falling for you at one point, but as you said, it was probably just a crush."
                else:
                    mc "I don't think you have to be the same person to click with someone, but it never happened to us."
                mc "I'm such a rookie with love..."
                scene ep9_jill_closure14 with dissolve
                ji "That makes two of us..."
            "Too complicated relationship":
                mc "For me, I think it was our relationship."
                mc "It got too complicated. I couldn't even come to see you without climbing your balcony or sneaking in."
                mc "And we didn't exactly get off on the right foot with the student counselors and all."
                mc "I want something where everything feels right for me, and this never did."
                scene ep9_jill_closure14 with dissolve
        ji "Thank you for talking to me like this. I feel most guys wouldn't do this."
        if affinity == "DIK":
            ji "You're way more mature than I gave you credit for."
        else:
            ji "It means a lot to me."
        scene ep9_jill_closure13 with dissolve
        mc "Despite all of this... It would mean a lot to me if we could still be friends."
        scene ep9_jill_closure14 with dissolve
        stop music fadeout 3
        ji "Of course, we can!"
    else:
        scene ep9_jill_closure6 with dissolve
        mc "I obviously don't feel the same... *{i}Sigh{/i}* But..."
        mc "Either way, it has to feel right for both of us, or there's no point in dating."
        scene ep9_jill_closure8 with dissolve
        ji "[name]... You have many wonderful sides. Believe me, you do!"
        scene ep9_jill_closure34 with dissolve
        ji "But I'm struggling a lot with myself and my thoughts and doubts..."
        ji "I feel I need to be alone and get in touch with my feelings more. Dating is new to me and... It's just..."
        scene ep9_jill_closure35 with dissolve
        mc "I think I understand."
        mc "But I still wish you would have given me an honest chance because I think we're missing out on something great."
        scene ep9_jill_closure34 with dissolve
        ji "I'm so sorry... I hate that I've hurt you."
        scene ep9_jill_closure35 with dissolve
        mc "I'll be fine. At least I got to say what I wanted and hear your thoughts on it."
        scene ep9_jill_closure7 with dissolve
        ji "I hope this hasn't ruined our friendship..."
        scene ep9_jill_closure6 with dissolve
        mc "I don't know. It's going to be tough to act like nothing ever happened between us, Jill."
        mc "But if I can't be with you, and staying your friend is my only option..."
        stop music fadeout 3
        mc "I'll try to get over this."

    scene ep9_jill_closure15 with dissolve
    $ renpy.pause()
    jump ep9_jill_after_closure2_label
else:
    scene ep9_jill_closure16 with dissolve
    ji "We never felt completely right for each other?"
    ji "Are you...serious?"
    ji "You can't possibly mean that!"
    scene ep9_jill_closure17 with dissolve
    mc "It felt great, but my heart tells me I want to be with someone else. And I can't fight that feeling anymore."
    scene ep9_jill_closure18 with dissolve
    ji "*{i}Sobs{/i}* I can't believe you."
    mc "Jill, I've never done this before."
    mc "I don't know how you're supposed to do it when you want to stop dating someone you've grown attached to."
    scene ep9_jill_closure19 with dissolve
    ji "*{i}Cries{/i}*"
    mc "(Fuck!)"
    scene ep9_jill_closure18 with dissolve
    mc "Jill... I'm so sorry."
    ji "*{i}Sobs{/i}*"
    mc "I don't know how else I can explain it."
    scene ep9_jill_closure20 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure21 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure22 with dissolve
    ji "Everything we did together... The dates, the kisses, the feelings... Were they all lies?"
    scene ep9_jill_closure23 with dissolve
    mc "No. They were real. Which is why it's so hard to tell you this."
    scene ep9_jill_closure22 with dissolve
    ji "*{i}Sobs{/i}* Then what was it?"
    scene ep9_jill_closure23 with dissolve
    mc "I have strong feelings for you..."
    mc "...but I have stronger feelings for someone else."
    mc "And I can't continue dating like this; it would only get worse for everyone."
    scene ep9_jill_closure21 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure23 with dissolve
    mc "Do you want me to leave?"
    scene ep9_jill_closure22 with dissolve
    ji "I wanted to be with you."
    ji "I thought you were...perfect."
    scene ep9_jill_closure24 with dissolve
    mc "..."
    scene ep9_jill_closure25 with dissolve
    mc "*{i}Sobs{/i}* I'm so sorry."
    mc "I never wanted to hurt you."
    mc "And I'm not perfect. Not for you or for anything."
    mc "I don't have a clue about what I'm doing. I'm just following my heart. It's the only way I know."
    stop music fadeout 3
    scene ep9_jill_closure26 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure27 with dissolve
    $ renpy.pause()
    jump ep9_jill_after_closure_label

label ep9_jill_bclosure_label:
play music "music/ep9/getting_closure.mp3"
scene ep9_jill_closure28 with dissolve
mc "Thanks for coming."
scene ep9_jill_closure29 with dissolve
if ep9_jill_mood == 3:
    ji "I almost didn't."
else:
    ji "I wasn't sure if I should have."
scene ep9_jill_closure30 with dissolve
mc "I understand."
scene ep9_jill_closure31 with dissolve
mc "Where to start...?"
mc "Jill..."
mc "I should have told you this a long time ago."
mc "But the truth is that I didn't know what I felt back then."
scene ep9_jill_closure32 with dissolve
mc "When I came to college, I was heartbroken."
mc "I told you about Josy and me, and you know how I felt about that during our date."
scene ep9_jill_closure33 with dissolve
mc "And before that, I was also heartbroken. I had a girlfriend, who I don't think ever saw me as her boyfriend, leave me."
mc "I had a very hard time dealing with that."
mc "Basically, my short but entire dating history has been this way."
mc "I thought it felt good, but it always ended with disappointment."
scene ep9_jill_closure32 with dissolve
mc "When I came here, I wanted to be happy, and I tried to find someone who would make me that."
mc "But I was stupid. I went after several girls at the same time."
mc "And as it turns out, you all know each other. And by the time I realized what I had done, it was already too late."
mc "And it got worse the longer I waited."
scene ep9_jill_closure6 with dissolve
mc "So, I thought about it and I finally made my decision. It's not been easy for me."
mc "And I chose that I wanted to continue to date Bella..."
scene ep9_jill_closure6b with dissolve
ji "..."
scene ep9_jill_closure32 with dissolve
mc "I went to talk to her about it. We spent a long time talking about all the obstacles in our way."
mc "We're both aware that we don't exactly make sense when looking at us from the outside..."
mc "...but there's something between us neither of us can ignore."
scene ep9_jill_closure6 with dissolve
mc "She asked me what my feelings were for you. It was clear to me that you were a deciding factor for her."
mc "I told her what I felt, and we agreed to tell you about us."
mc "But before we had the chance to do it... You... Well, you know the rest."
scene ep9_jill_closure6b with dissolve
ji "..."
scene ep9_jill_closure34 with dissolve
ji "When Bella asked you what your feelings were for me..."
ji "What was your answer?"
scene ep9_jill_closure35 with dissolve
if ep7_jill_talk:
    $ guideSuggestedPage = 61
    mc "I told her that I like both of you. But also that I wanted to date her and not you."
    scene ep9_jill_closure34 with dissolve
    ji "What made you choose her and not me?"
    scene ep9_jill_closure35 with dissolve
    menu:
        "Followed my heart":
            mc "I followed my heart... And it told me to choose her."
        "[mod_gr]Couldn't choose both":
            mc "Because I had to choose and I couldn't choose both of you."
            scene ep9_jill_closure40 with dissolve
            mc "I'm not sure if I made the right decision, but I couldn't go on dating both of you any longer."
            mc "I feel so guilty for doing this to you two. I never wanted to hurt your friendship."
            if ep8_jill_state == 1:
                scene ep9_jill_closure41 with dissolve
                menu:
                    "[mod_gr]Kiss her back":
                        $ ep9_b_kissed_jill = True
                        scene ep9_jill_closure42 with dissolve
                        $ renpy.pause()
                        scene ep9_jill_closure43 with dissolve
                        $ renpy.pause()
                        scene ep9_jill_closure44 with dissolve
                        mc "Fuck..."
                        scene ep9_jill_closure45 with dissolve
                        ji "Damn you, [name]..."
                    "Stop":
                        $ ep9_b_kissed_jill = False
                        scene ep9_jill_closure46 with dissolve
                        mc "Jill... I can't..."
                        mc "I'm sorry..."
    scene ep9_jill_closure38 with dissolve
    ji "..."
    mc "What I felt for you weren't lies, and neither is what I feel for her."
    if ep8_jill_state == 1:
        scene ep9_jill_closure39 with dissolve
        ji "I would have loved you."
        scene ep9_jill_closure40 with dissolve
        mc "..."
        scene ep9_jill_closure39 with dissolve
        ji "I hope she will too."
    else:
        scene ep9_jill_closure36 with dissolve
        ji "My truth is that I wasn't sure about us."
        ji "While there are many things with you that I love and adore, you have sides that make me unsure."
        scene ep9_jill_closure37 with dissolve
        ji "Nevertheless, it came as a shock, and it did hurt."
        ji "It still does."
        ji "But I wish that...you'll be happy with her. So that all of this wasn't for nothing."
        scene ep9_jill_closure39 with dissolve
    ji "Thank you for your honesty."
    ji "It's too late...but thank you."
    scene ep9_jill_closure40 with dissolve
else:
    if ep6_jill_lewd:
        mc "I told her that I was starting to fall for you, but that what she and I have is something I wanted to explore."
    else:
        mc "I told her I wasn't sure about you, but that I wanted to explore something with her."
        mc "I mean, you and I... We only went out on one date."
    scene ep9_jill_closure36 with dissolve
    ji "My truth is that I wasn't sure about us."
    ji "While there are many things with you that I love and adore, you have sides that make me unsure."
    if not ep6_jill_lewd:
        ji "And while we did date, we didn't spend enough time together for the spark to be there."
    scene ep9_jill_closure37 with dissolve
    ji "Nevertheless, you and Bella came as a shock to me. And at some level...it did hurt."
    ji "It still does."
    if ep9_jill_mood == 3:
        ji "But I wish that...you'll be happy with her. So that all of this wasn't for nothing."
    else:
        ji "But I wish that...you'll be happy with her."
    scene ep9_jill_closure6 with dissolve
mc "I'm so sorry for hurting you, Jill."
mc "But what pains me the most is hurting your relationship with Bella."
if ep9_jill_mood == 3:
    scene ep9_jill_closure38 with dissolve
else:
    scene ep9_jill_closure6b with dissolve
mc "I don't expect you to forgive me, but I hope you can find it in your heart to forgive her."
mc "If you can't...she'd be devastated."
if ep9_jill_mood == 3:
    scene ep9_jill_closure18 with dissolve
    ji "*{i}Sobs{/i}*"
    scene ep9_jill_closure19 with dissolve
    ji "*{i}Cries{/i}*"
    scene ep9_jill_closure18 with dissolve
    mc "Jill... I'm so sorry."
    scene ep9_jill_closure20 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure21 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure22 with dissolve
    if ep9_b_kissed_jill:
        ji "Everything we did together... The dates, the kisses, the feelings... How can I forget about that?"
    else:
        ji "Everything we did together... The dates, the kisses, the feelings... Were they all lies?"
    scene ep9_jill_closure23 with dissolve
    if ep9_b_kissed_jill:
        mc "I can't forget about that either. They meant so much to me."
    else:
        mc "No. They were real. Which is why it's so hard to tell you this."
    scene ep9_jill_closure21 with dissolve
    $ renpy.pause()
    scene ep9_jill_closure23 with dissolve
    mc "Do you want me to leave?"
    scene ep9_jill_closure22 with dissolve
    ji "I wanted to be with you."
    ji "I thought you were...perfect."
    scene ep9_jill_closure24 with dissolve
    mc "..."
    scene ep9_jill_closure25 with dissolve
    mc "*{i}Sobs{/i}* I'm so sorry."
    mc "I never wanted to hurt you."
    mc "And I'm not perfect. Not for you or for anything."
    mc "I don't have a clue about what I'm doing. I'm just following my heart. It's the only way I know."
    scene ep9_jill_closure26 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    scene ep9_jill_closure27 with dissolve
    $ renpy.pause()
else:
    scene ep9_jill_closure47 with dissolve
    ji "I'll try."
    stop music fadeout 3
    scene ep9_jill_closure48 with dissolve
    $ renpy.pause()
jump ep9_jill_after_bclosure_label

label ep9_pre_blackout_label:
play sound "sound_effects/zap.mp3"
scene ep9_blackout1 with vpunch
stop music
"AHHH!!!"
play sound "sound_effects/water_splash.mp3"
scene ep9_blackout2 with vpunch
"*{i}Splash{/i}*"
bc "AHHH!!! What the fuck!?"
scene ep9_blackout3 with dissolve
"What's happening?"
scene ep9_blackout5 with dissolve
"Huh!?"
scene ep9_blackout4 with dissolve
"What's going on?"

if branchIsabella:
    scene ep9_blackout6b with dissolve
else:
    scene ep9_blackout6 with dissolve
play sound "sound_effects/switch.mp3"
mc "(It's not the best flashlight, but my phone will do.)"
sa "This is not something you've planned, right?"
play music "music/ep8/licensed_music/track94.mp3"
if branchIsabella:
    scene ep9_blackout7 with dissolve
else:
    scene ep9_blackout7b with dissolve
mc "No. This must be something else. Hold on and let me check."
jump ep9_blackout_label

label ep9_blackout2_label:
scene ep9_blackout8 with dissolve
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
mc "Hello?"
jac "[name]? Over here, bro!"
show ep9_blackout9 with dissolve
if persistent.fx:
    show screen flashlight_screen
else:
    hide screen flashlight_screen
mc "Did you find the problem? Is a fuse blown?"
jb "Uh... I'm not sure. I'm not good at these things. There are {color=#00ff00}3{/color} rows of switches here..."
jb "But from what I can tell, everything looks the same. That's good, right?"
stop music fadeout 3
mc "What about that big red handle?"
play sound "sound_effects/season3/fusebox.mp3"
window hide
scene ep9_blackout10
hide screen flashlight_screen
with vpunch
window show
$ mouse_visible = True
jb "Unbelievable... That did it."
$ mphone_next_song()
jac "Great! The lights are back on."
ni "Let's check if it's working upstairs too."
scene ep9_blackout11 with dissolve
jac "What was the problem?"
scene ep9_blackout12 with dissolve
mc "I don't know. Maybe we hit the power limit with the smoke machine and everything?"
scene ep9_blackout11 with dissolve
jac "Right. That could be it. I'll go check what we can turn off to save some juice."
show ep9_blackout13
if not persistent.ep9_cardji17:
    show screen ep9_render_screen("ji17")
with dissolve
mc "..."
scene ep9_blackout14
hide screen ep9_render_screen
with dissolve
$ renpy.pause()
scene ep9_blackout15 with dissolve
bc "Are you freaking kidding me!? Eww!"
scene ep9_blackout16 with dissolve

label ep9_wave3_label:
mc "{i}The party was by no means perfect. Just like Tommy tried to warn me when we planned it, things would go wrong.{/i}"
scene ep9_wave3_1 with dissolve
mc "{i}Last to our party came The Pink Rose girls.{/i}"
stop music fadeout 3
scene ep9_wave3_2 with dissolve
mc "{i}I'd say this was around when trouble started, but it had been brewing all night.{/i}"
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/halloween.mp3"])

scene bg anim_wave3_ep9 movie with dissolve
if persistent.seen_cutscene_ep9[2]:
    $ renpy.pause(83.13)
else:
    $ _skipping = False
    $ renpy.pause(83.13, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep9[2] = True

scene ep9_wave3_3 with dissolve
ti "Hell no!"
de "IT'S NOT PRETTY, BUT IT COMES WITH A SOUL!"
scene ep9_wave3_4 with dissolve
de "..."
de "Sup?"


scene ep9_wave3_5 with dissolve
nic "Holy shit! This party seems wild!"
scene ep9_wave3_6 with dissolve
sn "College boys, grrr!"
scene ep9_wave3_7 with dissolve
ro "Ok, who's on Sandy-watch tonight?"
scene ep9_wave3_8 with dissolve
ly "Let her traumatize some boys who can't handle her, will you?"
ly "Off you go, Sandy!"
scene ep9_wave3_9 with dissolve
sn "Grr!!"

if branchJill:
    jump ep9_jillsolo_label
elif not branchIsabella:
    scene ep9_wave3_10 with dissolve
    sa "Drink! Drink! Drink!"
    scene ep9_wave3_11 with dissolve
    isa "It doesn't matter how many times you say that word. I've had enough."
    scene ep9_wave3_12 with dissolve
    ji "Drink! Drink! Drink!"
    isa "You too?"
    scene ep9_wave3_13 with dissolve
    sa "Hell yes!"
    ji "Hahaha!"
    "Drink! Drink! Drink!"

jump ep9_freeroam_diks_ph3_label

label ep9_ending_label:
$ guideSuggestedPage = 89
if minigames:
    scene ep9_ending22 with Fade(1,1,1)
    $ renpy.block_rollback()
    $ pp_continue_label = "ep9_pp_cont2_label"
    $ renpy.pause(1)
    jump party_planner_setup_evaluation_label
    label ep9_pp_cont2_label:
    $ persistent.pp_tutorial = 2
    $ renpy.block_rollback()
    $ tmpStr = ""
    if ep9_body_shots:
        $ tmpStr += "• Body shots "
    elif ep9_drinking_competition:
        $ tmpStr += "• Drinking competition "
    if ep9_scary_stories:
        $ tmpStr += "• Scary stories "
    elif ep9_haunted_mansion:
        $ tmpStr += "• Haunted mansion "
    if ep9_cumpetition:
        $ tmpStr += "• CUM-petition "
    if tmpStr == "":
        $ tmpStr = "None"
    $ mphone_pp_history_list.append("DIKs' Halloween party\n{color=fe9416}Activities:{/color} %s\n{color=fe9416}Total Party Score:{/color} {color=ffed00}%d{/color}\n{color=fe9416}Total Score:{/color} {color=ffed00}%d{/color}\n{color=e51475}Multiplier: %sx{/color}\n{color=fe9416}Rank:{/color} {color=ffed00}%s{/color}" % (tmpStr,pp_round_score,pp_score,pp_multiplier,pp_party_rank[0][1]))
    $ mphone_pp_history_list.append("")
    $ mphone_pp_history_list.append("")
    $ mphone_pp_history_list.append("")

    if steamAchievements and not config.console and not config.developer:
        if pp_party_rank[0][0]==9 and pp_party_rank[0][1]=="S":
            $ achievement.grant("IDS3_20")
            init:
                $ achievement.register("IDS3_20")
            $ achievement.Sync()
else:
    $ party_planner_get_nm_rank(pp_current_party_happiness)
    scene black with fade
    $ renpy.pause(2)

show screen new_phone_screen
play music "music/ep9/licensed_music/track119.mp3"
scene ep9_ending11 with dissolve
$ renpy.pause()
show ep9_ending10
if not persistent.ep9_cardjo17:
    show screen ep9_render_screen("jo17")
with dissolve
$ renpy.pause()
show ep9_ending9
hide screen ep9_render_screen
with dissolve
$ renpy.pause()
scene ep9_ending13 with dissolve
$ renpy.pause()
scene ep9_ending14 with dissolve
$ renpy.pause()
if ep9_jm_sad:
    scene ep9_ending16 with dissolve
    $ renpy.pause()
    scene ep9_ending15 with dissolve
    $ renpy.pause()

if not branchJill and ep8_jill_state == 1:
    if ep9_b_kissed_jill:
        scene ep9_ending17 with dissolve
        $ renpy.pause()
        scene ep9_ending17c with dissolve
    else:
        scene ep9_ending17e with dissolve
        $ renpy.pause()
        scene ep9_ending17b with dissolve
        $ renpy.pause()
        scene ep9_ending17d with dissolve
    $ renpy.pause()

if branchJill and wt_ep9_end_pick=="Jill":
    jump ep9_ending_jill_label
elif branchSage and wt_ep9_end_pick=="Sage":
    jump ep9_ending_sage_label
elif branchIsabella and wt_ep9_end_pick=="Bella":
    jump ep9_ending_isabella_label
elif branchMayaJosy and wt_ep9_end_pick=="Maya":
    jump ep9_ending_maya_josy_label
else:
    if ep9_lily_nicole_lewd and wt_ep9_end_pick=="Lily":
        jump ep9_ending_nicole_lily_label
    elif ep9_quinn_lewd and wt_ep9_end_pick=="Quinn":
        jump ep9_ending_quinn_label
    elif ep9_sarah_melanie_lewd and wt_ep9_end_pick=="Sarah":
        jump ep9_sm_ending_label
    elif wt_ep9_end_pick=="Other":
        jump ep9_ending2_others_label

label ep9_ending2_label:
scene ep9_ending12 with dissolve
$ renpy.pause()
scene ep9_ending2 with dissolve
$ renpy.pause()
scene ep9_ending1 with dissolve
$ renpy.pause()
scene ep9_ending3 with dissolve
$ renpy.pause()
scene ep9_ending4 with dissolve
$ renpy.pause()
scene ep9_ending5 with dissolve
$ renpy.pause()
scene ep9_ending6 with dissolve
$ renpy.pause()
scene ep9_ending7 with dissolve
$ renpy.pause()
scene ep9_ending8 with dissolve
$ renpy.pause()
stop music fadeout 3
scene black
$ renpy.pause(2)
jump ep9_save_here_label

label ep9_save_here_label:
hide screen new_phone_screen
scene black
$ renpy.pause(1)
$ persistent.ep9_completed = True
$ updateDikScore()

if steamAchievements and not config.console and not config.developer:
    if ep9_jm_sad and ep8_jill_state == 1 and not branchJill and (branchSage or branchIsabella):
        $ achievement.grant("IDS3_30")
        init:
            $ achievement.register("IDS3_30")
    $ achievement.grant("IDS3_02")
    init:
        $ achievement.register("IDS3_02")
    $ achievement.Sync()
    call check_steam_achievements_label from _call_check_steam_achievements_label

if renpy.loadable("scripts/episode10/update10.rpyc"):
    scene ep9_episode_endb
else:
    scene ep9_episode_end
$ renpy.pause()

scene black
show screen scoremsg
$ renpy.pause(2)
hide screen scoremsg

$ episodeIsEnding = True
show screen endingScreen
$ renpy.pause()
$ episodeIsEnding = False
hide screen endingScreen


jump ep9_generate_report_text_label
$ renpy.pause()

label ep9EndLabel:
stop music fadeout 2
$ renpy.pause(2)

if renpy.loadable("scripts/episode10/update10.rpyc"):
    jump startUpdate10
$ qM = persistent.quick_menu
$ persistent.quick_menu = 0
jump game_credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

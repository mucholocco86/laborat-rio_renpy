label startUpdate11:
jump header_ep11_label
label previousEp11Label:
$ phone_clear_jump_label = "previousEp11Labelb"
jump end_freeroam
label previousEp11Labelb:
$ guideSuggestedPage = 150
play music "music/patched/track_previous2.mp3"
scene black
$ renpy.pause(2)
hide screen new_phone_screen
$ previousEpLabel = "startUpdate11b"
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen

scene ep10_dik2_intro10 with wipeleft
de "I found something in my room today. It's some kind of a security camera, no?"
if ep4_derekFuckedArieth:
    scene ep10_after_bbq19
else:
    scene ep10_after_bbq19b
jac "What the fuck is that!?"
scene ep10_after_bbq29
jac "Derek: Where did he get those pictures from? Is it their camera?"
jac "Ashley: Someone dropped a letter off. Chad told them it was [name]."
scene ep10_after_bbq25
de "It all makes sense now. Cathy's cluck. The camera. The pictures. The posters..."
de "It's one of us."
scene ep10_after_bbq30
jac "It's a DIK... It's a fucking DIK."

scene ep10_bbq_nick_event17 with wiperight
mc "Are you in love with Heather!?"
scene ep10_bbq_nick_event16
ni "From the first moment I saw her."
ni "At Halloween, I ended up in bed with her."
scene ep10_ending3
if ep10_nick_response == 1:
    mc "She tried to use me at our Halloween party too."
elif ep10_nick_response == 2:
    mc "You can't tell Tommy about that. He would kill you."
elif ep10_nick_response == 3:
    mc "You need to tell Tommy about this."
elif ep10_nick_response == 4:
    mc "She gave me a blowjob and a titjob at Halloween in Leon's room."

scene ep10_library4 with wipeleft
isa "Then what I would suggest is to read the contract."
scene ep10_library5
my "I fear he'd suspect that I'm up to something if I asked him to see it."
scene ep10_library15
my "Derek and I are going home for Thanksgiving dinner. We can try to get it then."
scene ep10_tg45
pa "There you are! Welcome!"
if ep7_patrick_score < 0:
    if ep8_told_josy_chad:
        scene ep10_tg52
    else:
        scene ep10_tg52b
else:
    if ep8_told_josy_chad:
        scene ep10_tg52c
    else:
        scene ep10_tg52d
pa "Oh, I remember you. [name], was it?"
if ep8_told_josy_chad:
    scene ep10_tg2_mp5
else:
    scene ep10_tg2_mp4
my "Any luck with the contract yet?"
scene ep10_tg2_mp3
mc "No, not yet. The door is locked."
scene ep10_tg_dinner98 with hpunch
my "Dad, let go! You're hurting me!"
if ep10_patrick_choice == "DIK":
    play sound "sound_effects/hit.mp3"
    scene ep10_tg_dinner112 with hpunch
    my "[name]! No!"
elif ep10_patrick_choice == "NEUTRAL":
    scene ep10_tg_dinner115
    mc "What the hell are you doing?"
else:
    scene ep10_tg_dinner105
    mc "Patrick, let's calm down. We don't have to resort to violence."

if ep10_got_contracts:
    if ep8_told_josy_chad:
        scene ep10_fr_tg_end21
    else:
        scene ep10_fr_tg_end21b
    mc "I did it! Maya, I did it!"
    scene ep10_fr_tg_end22
    my "You got the contract?"
else:
    if ep8_told_josy_chad:
        scene ep10_tg_sus11
    else:
        scene ep10_tg_sus11b
    mc "I blew it..."

if jade_state == 1:
    scene ep9_burkes43 with wiperight
    ja "What are you doing here? Are you crazy? I'm trying to keep our affair a secret and you show up unannounced!"
    scene ep9_burkes44
    mc "I didn't know you were Sage's mom! Do you think I would have shown up if I did?"
    scene ep10_sb34
elif jade_state > 0:
    scene ep9_burkes90 with wiperight
    ja "How stupid do you have to be to come here tonight?"
    scene ep9_burkes92
    mc "I didn't know you were Sage's mom! Do you think I would have shown up if I did?"
    scene ep10_sb34
else:
    scene ep10_sb34 with wiperight
ja "We are NOT getting a divorce."
scene ep10_sb41
sb "Sign the papers."
play sound "sound_effects/shove.mp3"
scene ep9_zoey_talk9 with hpunch
mc "Why are you back?"
zo "I missed you."
scene ep10_bbq_z2_event19
mc "...you were my first love."
scene ep10_bbq_jz_event20
mc "If I had said that... Would you have stayed?"
scene ep10_bbq_jz_event21
zo "Oh, fuck..."
scene ep10_bbq_jz_event22
$ renpy.pause()

scene ep7_intro34 with wipeleft
sis "Kick him hard between his legs if he gets close again. It's a weak spot."
scene ep7_intro35
ji "Are you leaving again? I miss you when you're gone."
scene ep7_intro38
ji "Look at the moon."
sis "And you'll know I'll be looking at it too."
scene ep7_intro52
ji "{i}Dear Jonathan. I made an attempt to start a campaign in Lana's honor, but I need help with the first steps.{/i}"

if branchJill:
    scene ep10_jill_solo29
else:
    scene ep10_library47
ji "This one is from our mansion. That's Tybalt's bed."
ji "Did you steal from me and Tybalt?"
mc "What? No!"

scene ep10_jt15
ji "Tybalt said you would press charges for the fire. And he called you petty for it."
scene ep10_jt19
tr "Wait a minute. What?"
play sound "sound_effects/door_slam.mp3"
scene ep10_jt7 with hpunch
tr "Tybalt, what is this I'm hearing that-"
scene ep10_jt9
ty "Ahhh!!! Get out!"

if branchJill:
    scene ep10_bbq_jill2_event19
    mc "If I try to come around on winter stuff, you try to come around on spring break."
    scene ep10_bbq_jill2_event18
    ji "Ok... Deal."

scene ep9_ph2_josy_event4 with wiperight
js "He called me a run-of-the-mill boring and basic bitch."
scene ep10_josy20
js "He asked me a lot about myself before that, pretending to be interested. Like, hobbies and whatnot?"
scene ep10_josy16
$ renpy.pause()
if branchMayaJosy:
    scene ep10_mj_solo27
    bc "Are you three in a sexual three-way relationship?"
    scene ep10_mj_solo24
    js "People are passing along some pretty wrong information."

scene ep10_fr1_sage_event10 with wipeleft
dw "We're gonna talk about what happened yesterday. We are PISSED off!"
scene ep10_fr1_alphas_event2
sa "The DIKs will party more with the HOTs than the tri-alphas..."
scene ep10_fr1_alphas_event7
sa "And in return... I'll get you Chad back."

if branchSage:
    scene ep9_sage_branch25 with wiperight
    mc "Did you ever look into who your mom was?"
    scene ep9_sage_branch31
    sa "Talking about my family during sex. God, you're such a boner-killer!"
    scene ep10_sage_chill17
    sa "I'm sorry, but some of your questions hit too close to home."
    scene ep10_bbq_s_event24
    sa "I'm your girl?"
    scene ep10_bbq_s_event23
    mc "You're my girl."

if branchIsabella:
    scene ep10_bsolo46 with wiperight
    mc "You checked the handbook. What did it say?"
    scene ep10_bsolo40
    isa "The lines are blurry, but let's not be concerned."
    scene ep10_bsolo45
    mc "That's amazing... Wow! I was kinda expecting the worst."
    scene ep10_bbq_isabella_end34
    isa "I feel like I've been constantly drowning, [name]."
    scene ep10_bbq_isabella_end36
    isa "You're the air I need."
if branchAlone:
    if ep10_rolling:
        scene ep10_bbq_lroll_event4 with wiperight
        ml "What's up with you and [name]? I didn't know you were together."
        scene ep10_bbq_lily_jetty_event32
        ly "Don't be gross. We're not together."
        sa "It sounds like you're using him."
        scene ep10_bbq_lily_jetty_event15
        ly "I don't want you to fall for me."

    if ep10_dating_nora:
        scene ep10_nora_lewd11 with wipeleft
        no "Can I be your bad kitty tonight?"
        scene ep10_lab13
        no "Why haven't you told me that you are a student?"
        if ep10_shroom_choice == "DIK":
            scene ep10_bbq_nora_event8
        else:
            scene ep10_bbq_nora_event12
        no "It's simply too complicated to date someone I'm teaching. I can't date you anymore."

    if ep10_date_nicole and not ep10_cancel_date_nicole:
        scene ep10_nicole_date23 with wiperight
        nic "I can't believe that I'm having a wonderful date with a teenager I met at work."
        scene anim_envy_lick_ep10 with dissolve
        nic "What are we doing, really?"
        if ep10_nicole_questions[1]:
            mc "Let's just have fun together and figure it out as we go."
        else:
            mc "Do you have to know it?"
        scene ep10_nicole_lewd47
        mc "(Wow... What a night that was. Nicole is incredible.)"
        scene ep10_nicole_lewd48
        mc "(If only she didn't have a kid...)"

    if ep10_riona_date:
        if ep8_mansion_won:
            scene ep10_rio_solo45b with wiperight
        else:
            scene ep10_rio_solo45 with wiperight
        ri "Holy crap, this was a date!"
        scene ep10_bbq_rio_event30
        ri "I haven't been able to stop thinking about the arcade since we went there."
        scene ep10_bbq_rio_event19
        ri "*{i}Smack{/i}*"

scene ep3_quri3 with wipeleft
qu "I'm telling you, we're short."
scene ep3_quri8
ri "I was relaxed, until you started bringing in more girls."
ri "You're getting cocky."
play sound "sound_effects/slap.mp3"
scene ep3_quri13 with hpunch
$ renpy.pause()

scene ep6_qr4
ri "Lately... I've felt like someone is watching me."
scene ep6_qr5
qu "It sounds like paranoia to me."
scene ep6_qr8
qu "No one even knows you. You're nothing."
scene ep7_lq23
ly "I'm looking for a new supplier. Reliable and cheap."
ly "I've got $500 for you if you hook me and my girls up."
scene ep7_lq21
qu "How many girls are we talking about?"
scene ep8_lq81
ri "Quinn is making some plan with Lily but doesn't let me in on it."
scene ep8_lq95
ri "I don't intend to stick this out if it doesn't get a lot better fast."

scene ep10_ending11
ri "Quinn? I'm on my way, but I think I'm being followed. Can you meet me up?"
scene ep10_ending12
ri "Vinny?"
play sound "sound_effects/shove.mp3"
scene ep10_ending13 with hpunch
ri "HEY! LET ME GO!"
ri "HELP! HELP!!!"
play sound "sound_effects/burnout.mp3"
scene ep10_ending14
$ renpy.pause()

label startUpdate11b:
if steamConfig or nonPatreonConfig:
    if branchIsabella:
        $ state = "ep11_steam_isabella"
    elif branchSage:
        $ state = "ep11_steam_sage"
    elif branchMayaJosy:
        if ep10_jm_solo == "Josy":
            $ state = "ep11_steam_jm"
        else:
            $ state = "ep11_steam_jm2"
    elif branchJill:
        $ state = "ep11_steam_jill"
    else:
        if ep10_quinn_help:
            $ state = "ep11_steam_others2"
        elif ep10_rolling:
            $ state = "ep11_steam_others3"
        elif jade_state == 1:
            $ state = "ep11_steam_others5"
        elif not ep10_zoey_jacob:
            $ state = "ep11_steam_others4"
        else:
            $ state = "ep11_steam_others"
else:
    if branchIsabella:
        $ state = "ep11_isabella"
    elif branchSage:
        $ state = "ep11_sage"
    elif branchMayaJosy:
        if ep10_jm_solo == "Josy":
            $ state = "ep11_jm"
        else:
            $ state = "ep11_jm2"
    elif branchJill:
        $ state = "ep11_jill"
    else:
        if ep10_quinn_help:
            $ state = "ep11_others2"
        elif ep10_rolling:
            $ state = "ep11_others3"
        elif jade_state == 1:
            $ state = "ep11_others5"
        elif not ep10_zoey_jacob:
            $ state = "ep11_others4"
        else:
            $ state = "ep11_others"
call rpc from _call_rpc_3
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black
$ renpy.pause(0.5)

label ep11_intro_label:
play music "music/ep11/licensed_music/track152.mp3"
scene ep11_intro12 with dissolve
lan "Please?"
scene ep11_intro13 with dissolve
than2 "No."
scene ep11_intro12 with dissolve
lan "Pretty please?"
scene ep11_intro13 with dissolve
than2 "What has gotten into you?"
scene ep11_intro14 with dissolve
lan "I wanna try it. Come on! It's my birthday."
scene ep11_intro15 with dissolve
than2 "You've been playing the birthday card all week with me. We both know it's not your birthday today."

scene ep11_intro16 with dissolve
lan "Argh... Why do you gotta be so lame?"
scene ep11_intro17 with dissolve
than2 "..."
scene ep11_intro18 with dissolve
than2 "You can have some of my weed."
scene ep11_intro19 with dissolve
lan "I'm tired of weed. It's not the mood I'm in for tonight."
scene ep11_intro20 with dissolve
than2 "There's beer, too. Weed and beer sound like a great party if you ask me."
scene ep11_intro21 with dissolve
lan "Beer doesn't do it for me either."
scene ep11_intro20 with dissolve
than2 "How do you even know what coke does for you?"
scene ep11_intro21 with dissolve
lan "Lex told me it was awesome and she stayed up all night partying after having some."
scene ep11_intro20 with dissolve
than2 "Then, get it from Alex."
scene ep11_intro22 with dissolve
lan "{i}Lex{/i} doesn't have any. She only got to try it because a guy wanted to bang her at a party."
scene ep11_intro23 with dissolve
than2 "I don't have any either."
scene ep11_intro24 with dissolve
lan "Fine... I'll have to ask everyone at the party for some. Let's hope there aren't any narcs there."
scene ep11_intro25 with dissolve
than2 "That reverse psychology doesn't work on me."
scene ep11_intro26 with dissolve
lan "Why are you so against trying it?"
scene ep11_intro27 with dissolve
than2 "Because I'm not as curious about it as you are."
scene ep11_intro26 with dissolve
lan "Then let me have some. You don't have to try it."
scene ep11_intro27 with dissolve
than2 "And... I'd rather not deal with those guys more than when I need to buy something. They creep me out."
scene ep11_intro29 with dissolve
lan "Aw! Are you scared?"
scene ep11_intro28 with dissolve
than2 "I'm not scared."
scene ep11_intro29 with dissolve
lan "Li'l Than is scured."
scene ep11_intro28 with dissolve
than2 "Stop that."
scene ep11_intro30 with dissolve
lan "The big boys are scury. Than is walking on his tippy toes to avoid them."
scene ep11_intro31 with dissolve
than2 "You think you're cute, but you're just annoying."
scene ep11_intro32 with dissolve
lan "Wrong! I wanted to be annoying."
scene ep11_intro33 with dissolve
lan "*{i}Smack{/i}*"
scene ep11_intro34 with dissolve
than2 "Big birthday party next week?"
scene ep11_intro35 with dissolve
lan "The only party I'm interested in is tonight."
scene ep11_intro36 with dissolve
than2 "I know, but..."
scene ep11_intro37 with dissolve
lan "No buts. I'm done pretending everything is fine with my family."
lan "Another year older, another level of their bitching."
scene ep11_intro38a with dissolve
than2 "I thought you said they were trying with you."
scene ep11_intro38 with dissolve
$ renpy.pause(0.5)
scene ep11_intro39 with dissolve
lan "Trying, as in they're expecting me to \"grow up\" and will wait for it to happen."
lan "But they don't want me to grow up how I want to. They're impossible."
scene ep11_intro40 with dissolve
lan "And I know they're doing that with Jill, too. Seeing how they failed with me makes them try harder with her."
lan "They're so controlling! Jill isn't a lump of clay they can shape however they want."
lan "What about her dreams, thoughts, and ideas, which she shares with me when we're alone? Don't they matter?"
scene ep11_intro41 with dissolve
than2 "That's parents for you. Mine are the same, but at least they act like my lifestyle doesn't bother them."
than2 "I don't want to be a doctor or a realtor. Just because they're smart doesn't mean that I am."
scene ep11_intro42 with dissolve
lan "But you are smart. You're talented and have way more brains than you give yourself credit for."
scene ep11_intro41 with dissolve
than2 "I'm not smart. I'm stupid and I'm perfectly fine with that. I have nothing to prove, especially not to my parents."
scene ep11_intro42 with dissolve
lan "I'll go to the birthday party... But I'm only going because of Jill."
lan "Mom had already spoiled the surprise and told me that Jill had made me something in school. That was Mom's way of making sure I'd show up."
lan "She knows Jill's the only reason I'm still going back there."

show ep11_intro43
if not persistent.ep11_cardly1:
    show screen ep11_render_screen("ly1")
with dissolve

lan "Well... Jill and the weed. But Mom doesn't have to know about my secret stash."
lan "I'd hide it at your place if I trusted you not to smoke it."
show ep11_intro44
hide screen ep11_render_screen
with dissolve
than2 "That's hilarious because it's the other way around, and you know it..."
scene ep11_intro45 with dissolve
lan "I'm bored... Wanna head to the party early?"
scene ep11_intro46 with dissolve
than2 "Yeah. But let's make a stop on the way."
scene ep11_intro45 with dissolve
lan "Where at?"
scene ep11_intro46 with dissolve
than2 "At the scary big boys."
scene ep11_intro47 with dissolve
lan "No way!?"
scene ep11_intro48 with dissolve
than2 "But you can't use your birthday on me again until next year."
scene ep11_intro49 with dissolve
lan "Haha! I don't have to use it. Christmas is coming."
scene ep11_intro48 with dissolve
than2 "Yeah, and you're still wearing shorts. What the fuck is wrong with you?"
scene ep11_intro50 with dissolve
lan "Do you want me to wear the clothes Mom laid out for me? Is that a secret fetish of yours?"
scene ep11_intro51 with dissolve
than2 "Freeze to death, then. Be my guest."
lan "You sound just like her."
scene ep11_intro52 with wipeleft
than2 "Wait here."
scene ep11_intro53 with dissolve
lan "I thought you said I could come with you."
scene ep11_intro54 with dissolve
than2 "I need to use the payphone and call ahead. They're not cool with me walking in there unannounced."
scene ep11_intro53 with dissolve
lan "Oh, alright."
scene ep11_intro55 with dissolve
$ renpy.pause()
scene ep11_intro56 with dissolve
$ renpy.pause()
scene ep11_intro57 with dissolve
$ renpy.pause()
scene ep11_intro58 with dissolve
$ renpy.pause()
scene ep11_intro59 with dissolve
play sound "sound_effects/season3/car_door.mp3"
$ renpy.pause()
scene ep11_intro60 with dissolve
lan "So?"
scene ep11_intro64 with dissolve
than2 "You're not getting much. You're getting some."
scene ep11_intro61 with dissolve
lan "Is that your call or his?"
scene ep11_intro65 with dissolve
than2 "Why do you gotta be difficult all the time?"
scene ep11_intro61 with dissolve
lan "Got it. It's your call."
scene ep11_intro64 with dissolve
than2 "Since it's your first time, I'm not letting you have much."
scene ep11_intro61 with dissolve
lan "You don't even know what much of it is."
scene ep11_intro64 with dissolve
than2 "But they do. I told him I wanted a party's worth for a rookie."
scene ep11_intro62 with dissolve
lan "Haha! He's gonna think you're the rookie now."
scene ep11_intro66 with dissolve
than2 "..."
than2 "Damn... I didn't think about that."
scene ep11_intro54 with dissolve
than2 "But they will see you with me and understand it."
scene ep11_intro62 with dissolve
lan "Drug dealers are all understanding, aren't they?"
scene ep11_intro64 with dissolve
than2 "On second thought... Maybe it's best if you wait in the car."
scene ep11_intro62 with dissolve
lan "Then who's gonna protect you from the big boys?"
scene ep11_intro64 with dissolve
than2 "I'm not joking around. They carry guns."
scene ep11_intro63 with dissolve
lan "I'm not scared of them."
scene ep11_intro64 with dissolve
than2 "And that makes me scared."
than2 "Look, it's just a business transaction. We walk in, we present him the money, he hands us the merchandise, and we're on our way."
than2 "No pleasantries or other exchange of words."
scene ep11_intro63 with dissolve
lan "You sound like Dad when you talk all formal like that."
scene ep11_intro54 with dissolve
than2 "Your dad used coke?"
scene ep11_intro63 with dissolve
lan "I wouldn't put it past him, at least when he was young. Not that he'd ever tell me."
scene ep11_intro54 with dissolve
than2 "I think Dad used it, too."
scene ep11_intro63 with dissolve
lan "That's likely why they get along so well. Double standards galore."
scene ep11_intro71 with dissolve
than2 "Ok. No more talking until we're back in the car. Be cool and quiet."
stop music fadeout 5
scene ep11_intro72 with dissolve
lan "When am I not cool?"
scene ep11_intro71 with dissolve
than2 "When are you ever quiet?"
scene ep11_intro72 with dissolve
lan "Haha, shut up! I'll show you."
scene ep11_intro73 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/door_squeek.mp3"
play music "music/ep6/licensed_music/track33.mp3"
scene ep11_intro11 with dissolve
bd "That's what I'm saying! With the rats!"
scene ep11_intro1 with dissolve
bd "He should have killed him, pushed him over the ledge and down there in the gutter-"
scene ep11_intro2 with dissolve
bd "-there's the fucking rat!"
scene ep11_intro3 with dissolve
rx "That would have fucked with the whole message of the movie!"
rx "The rat was the message!"
scene ep11_intro5 with dissolve
rx "Yeah, it was a bit cheesy, I'll give you that. But point is, no matter how high you climb..."
scene ep11_intro4 with dissolve
rx "...the rats find their way to get to you. You can't get rid of the rats."
bd "That rat was some CGI bullshit anyway."
scene ep11_intro6 with dissolve
rx "Hehe! You don't think they trained one to do that?"
scene ep11_intro7 with dissolve
rx "You know, like a- What's the word?"
scene ep11_intro8 with dissolve
rx "Off you go."
scene ep11_intro9 with dissolve
bd "Like a circus?"
rx "Yeah, something like that."
scene ep11_intro10 with dissolve
bd "I fucking hate rats."
stop music fadeout 3
scene ep11_intro74 with dissolve
than2 "Are you good?"
play music "music/ep11/licensed_music/track152.mp3"
scene ep11_intro75 with dissolve
lan "I'm not gonna lie. When I heard them talking about killing someone, my heart skipped a beat."
scene ep11_intro74 with dissolve
than2 "I think it was movie talk."
scene ep11_intro75 with dissolve
lan "Yeah, I got that. But fuck..."
scene ep11_intro76 with dissolve
than2 "Aw..."
scene ep11_intro77 with dissolve
lan "Aw, what?"
scene ep11_intro76 with dissolve
than2 "Is Li'l Lana scured?"
scene ep11_intro77 with dissolve
lan "Haha! Shut up."
play sound "sound_effects/season3/car_door.mp3"
scene ep11_intro67 with dissolve
than2 "Here you go."
scene ep11_intro68 with dissolve
lan "It looks like your business transaction transpired with a great deal of success."
scene ep11_intro69 with dissolve
than2 "Pff... Happy Birthday, Lana."
scene ep11_intro68 with dissolve
lan "Much obliged, Jonathan."
stop music fadeout 5
scene ep11_intro70 with dissolve
$ renpy.pause()

scene 2d_jacob_screen_main with dissolve
show screen episode_title_screen
$ renpy.pause(5)
$ renpy.block_rollback()

label ep11_quinn_label:
play music "music/ep11/licensed_music/track153.mp3"
scene ep11_quinn1 with fade
$ renpy.pause()
scene ep11_quinn2 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/melody2.mp3"
scene ep11_quinn3 with dissolve
"*{i}Phone rings{/i}*"
scene ep11_quinn4 with dissolve
qu "What?"
scene ep11_quinn6 with dissolve
qu "I told you why not. I was busy today."
qu "It's just Thanksgiving; it's not a big deal."
scene ep11_quinn4 with dissolve
qu "I meant it's not a big deal to me."
qu "No, don't put him on."
scene ep11_quinn5 with dissolve
qu "Fuck... Hiii, Henry..."
qu "Can you tell her I was busy?"
show ep11_quinn7
if not persistent.ep11_cardly2:
    show screen ep11_render_screen("ly2")
with dissolve
qu "Doing stuff."
qu "Yeah, with my friends. They're all here."
show ep11_quinn6
hide screen ep11_render_screen
with dissolve
qu "Because Thanksgiving sucks."
qu "Nope, I'm not coming home this weekend either."
qu "I was home some weeks ago, wasn't I?"
scene ep11_quinn8 with dissolve
qu "Yep. I'm busy all weekend."
qu "Studies, too. Study, study, study. With the finals and all, the profs aren't letting us catch any early breaks."
scene ep11_quinn9 with dissolve
qu "Christmas? Eh...we'll see."
qu "Look, I don't wanna have this conversation. I'm with my friends."
qu "Yeah, later. Bye!"
scene ep11_quinn10 with dissolve
qu "Annoying..."
scene ep11_quinn11 with dissolve
$ renpy.pause()
scene ep11_quinn12 with dissolve
qu "Bitch, are you done yet?"
scene ep11_quinn13 with dissolve
ri "Quinn? Yeah, it went ok, but listen-"
scene ep11_quinn12 with dissolve
qu "You're taking your sweet time. The ice cream is melting."
scene ep11_quinn14 with dissolve
ri "I'm on my way, but I think I'm being followed. Can you meet me up?"
scene ep11_quinn15 with dissolve
qu "Huh? Followed by who?"
stop music fadeout 3
scene ep11_quinn14 with dissolve
ri "Vinny?"
play music "music/ep11/licensed_music/track154.mp3"
scene ep11_quinn16 with dissolve
ri "HEY! LET ME GO!"
ri "HELP!"
play sound "sound_effects/shove.mp3"
scene ep11_quinn17 with vpunch
qu "Rio!? Rio!? Hello!?"
scene ep11_quinn18 with dissolve
qu "FUCK!"
play sound "sound_effects/season2/snow_footsteps.mp3"
scene ep11_quinn19
show screen ep10_snow_screen
with dissolve
qu "Rio!?"
scene ep11_quinn20 with dissolve
qu "Rio?"
scene ep11_quinn21 with dissolve
$ renpy.pause()
play sound "sound_effects/cellphone.mp3"
scene ep11_quinn22 with dissolve
"*{i}Phone rings{/i}*"
scene ep11_quinn23 with dissolve
$ renpy.pause()
scene ep11_quinn24 with dissolve
$ renpy.pause()

scene bg anim_quinn_phone_ep11 movie with dissolve
pause

play sound "sound_effects/door_slam.mp3"
scene ep11_quinn25
hide screen ep10_snow_screen
with hpunch
$ renpy.pause()
scene ep11_quinn26 with dissolve
$ renpy.pause()
scene ep11_quinn27 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/chair_move.mp3"
scene ep11_quinn28 with hpunch
$ renpy.pause()
scene ep11_quinn29 with dissolve
$ renpy.pause()
scene ep11_quinn30 with dissolve
qu "Pick up, you asshole... Pick up!"
scene ep11_quinn31 with dissolve
qu "Fuck!"
scene ep11_quinn32 with dissolve
$ renpy.pause()
scene ep11_quinn33 with dissolve
$ renpy.pause()

scene ep11_quinn36 with dissolve
bd "That was faster than I expected. I barely just got company."
scene ep11_quinn34 with dissolve
qu "Buddy, what the fuck is going on!?"
scene ep11_quinn37 with dissolve
bd "That's funny. I was about to ask your friend the same question."
scene ep11_quinn35 with dissolve
qu "Look... Look. Can you talk to me? What's wrong? Don't touch her, ok?"
scene ep11_quinn37 with dissolve
bd "No. I think I will talk to your friend instead."
bd "I have a feeling she won't lie. At least not for long."
scene ep11_quinn38 with dissolve
qu "DON'T YOU FUCKING HURT HER!"
scene ep11_quinn39 with dissolve
bd "Now, where were we?"
scene ep11_quinn40 with dissolve
bd "Oh, that's right."
stop music fadeout 4
scene bg anim_pliers_ep11 movie with dissolve
$ renpy.pause(4)

label ep11_tg_label:
play music "music/ep10/pineapple_pizza.mp3"
if ep8_told_josy_chad:
    scene ep11_tg1 with fade
else:
    scene ep11_tg2 with fade
$ renpy.pause()

scene ep11_tg3 with dissolve
ji "So... Nothing yet, huh?"
scene ep11_tg4 with dissolve
js "No."
scene ep11_tg5 with dissolve
js "..."
scene ep11_tg6 with dissolve
js "Is radio silence good or bad?"
if not ep8_told_josy_chad:
    scene ep11_tg10 with dissolve
    sa "I'm not aware if they have some weird traditions, but it can't be much longer now."
if ep8_told_josy_chad:
    scene ep11_tg8 with dissolve
else:
    scene ep11_tg9 with dissolve
isa "Try not to think about it. A watched pot never boils."
scene ep11_tg5 with dissolve
$ renpy.pause()

if ep8_told_josy_chad:
    scene ep11_tg8 with dissolve
else:
    scene ep11_tg9 with dissolve
isa "Speaking of... Who wants coffee?"
if not ep8_told_josy_chad:
    scene ep11_tg11 with dissolve
    sa "Yes, please."
scene ep11_tg5 with dissolve
isa "Josy?"
scene ep11_tg7 with dissolve
js "Huh? Coffee? Yes. Thank you."
scene ep11_tg12 with dissolve
ji "I'll help you."

if branchIsabella:
    scene ep11_tg33 with dissolve
    isa "It means a lot to me that you're here tonight."
    isa "Not just because of why we're here, but..."
    scene ep11_tg34 with dissolve
    ji "I kept thinking about our last Thanksgiving, and it made me feel sad to remember how nice it was."
    ji "I didn't want to lose someone else to have this tradition with."
    scene ep11_tg35 with dissolve
    $ renpy.pause()
    scene ep11_tg36 with dissolve
    isa "When are you visiting her grave?"
    scene ep11_tg37 with dissolve
    ji "Mom and Dad always visit her on the day she passed away, and I visit her on her birthday as usual."
    scene ep11_tg36 with dissolve
    isa "How are your parents this year?"
    scene ep11_tg37 with dissolve
    ji "Like every year, but Dad has gotten worse."
    ji "He's been drinking more than usual. Mom told me his depression has gotten worse after he cut back on work."
    ji "It was like work kept him sober. She's been pushing him to increase his hours, but he hasn't yet."
    scene ep11_tg38 with dissolve
    ji "It's tough."
    scene ep11_tg39 with dissolve
    $ renpy.pause()
    scene ep11_tg40 with dissolve
    $ renpy.pause()
    scene ep11_tg41 with dissolve
    ji "I don't want to lose your friendship. That's what I've realized. You mean so much to me, Bella."
    ji "And I want you to be happy. That's what I've wanted since the day we met."
    ji "It would be weird if I felt different about that now."
    scene ep11_tg42 with dissolve
    isa "It's not weird. You have the right to your feelings."
    scene ep11_tg27 with dissolve
    $ renpy.pause()
    scene ep11_tg28 with dissolve
    isa "But the line I crossed, I didn't cross on purpose. And I can't undo it."
    scene ep11_tg29 with dissolve
    isa "I know that [name] meant a lot to you. I didn't think there would be a spark between us."

    scene ep11_tg41 with dissolve
    ji "Is it...love?"
    scene ep11_tg42 with dissolve
    isa "It's too early to say."
    if ep9_b_kissed_jill:
        scene ep11_tg41 with dissolve
        ji "I kissed him."
        scene ep11_tg42 with dissolve
        isa "I figured."
        scene ep11_tg41 with dissolve
        ji "No. You don't get it."
        ji "When he broke up with me, I kissed him, and he kissed me back."
        scene ep11_tg43 with dissolve
        isa "Oh...?"
        scene ep11_tg44 with dissolve
        $ renpy.pause()
        scene ep11_tg45 with dissolve
        ji "He told me he chose you because he couldn't choose us both."
        scene ep11_tg43 with dissolve
        isa "I... I know it was difficult for him."
        scene ep11_tg41 with dissolve
        ji "I still have feelings for him, Bella. So, please..."
        ji "Tell me that you have too."
    else:
        scene ep11_tg41 with dissolve
        ji "Is it?"
    scene ep11_tg46 with dissolve
    $ renpy.pause()
    scene ep11_tg47 with dissolve
    isa "I have feelings for [name]. Being together with him isn't just about sex."
    if ep9_b_kissed_jill:
        scene ep11_tg45 with dissolve
        ji "Sorry... I had to tell you."
        scene ep11_tg43 with dissolve
        isa "I understand."
    scene ep11_tg46 with dissolve
    ji "When I saw you two dancing together on Halloween, I suspected there was more to it than I thought."

    scene ep11_tg48 with dissolve
    ji "Bella... I'm concerned about it."
    ji "You're not allowed to have teacher-student relations at B&R."
    scene ep11_tg49 with dissolve
    isa "*{i}Sigh{/i}* The rules about it aren't clear."
    scene ep11_tg48 with dissolve
    ji "Am I wrong?"
    scene ep11_tg49 with dissolve
    isa "It didn't say anything about employee-student relations, and that's what it was at the start."
    scene ep11_tg50 with dissolve
    ji "But you knew you'd be his teacher someday. And now you are..."
    scene ep11_tg51 with dissolve
    isa "I know... It's just that..."
    isa "I felt happy for the first time in years, and I didn't want a rulebook to decide it was wrong."
    scene ep11_tg50 with dissolve
    ji "Bella..."
    scene ep11_tg30 with dissolve
    ji "What are you going to do about it? You're risking your job by doing this."
    isa "I only wanted to have time to figure our relationship out without complicating it with rules."
    scene ep11_tg31 with dissolve
    ji "Does [name] know about it?"
    isa "No. I've kept it from him because I fear he'd make a big deal out of it."
    scene ep11_tg32 with dissolve
    ji "It is a big deal, Bella."
    if ep8_told_josy_chad:
        scene ep11_tg14 with dissolve
        $ renpy.pause()
        scene ep11_tg15 with dissolve
        $ renpy.pause()
    else:
        scene ep11_tg20 with dissolve
        sa "Where's the coffee?"
        scene ep11_tg21 with dissolve
        js "Oh, uh... I forgot about it."
        scene ep11_tg16 with dissolve
        sa "Then what were you up to?"
        scene ep11_tg17 with dissolve
        js "I must have gone to the bathroom instead."
        scene ep11_tg22 with dissolve
        sa "It's ok. I understand why you're absent-minded tonight."
        scene ep11_tg23 with dissolve
        $ renpy.pause()
else:
    scene ep11_tg13 with dissolve
    if ep8_told_josy_chad:
        js "Come on... Do something."
    else:
        js "Come on... Do something."
        scene ep11_tg19 with dissolve
        sa "It won't do anything when you're watching it like that."
        scene ep11_tg13 with dissolve
        js "Maybe it will if I focus extra hard."
        scene ep11_tg22 with dissolve
        sa "Come here."
        scene ep11_tg23 with dissolve
        $ renpy.pause()


if ep8_told_josy_chad:
    scene ep11_tg26 with dissolve
    ji "Josy! They're here."
    scene ep11_tg18 with dissolve
else:
    scene ep11_tg25 with dissolve
    ji "Josy! Sage! They're here."
    scene ep11_tg24 with dissolve
$ renpy.pause()

if ep10_got_contracts:
    if ep8_told_josy_chad:
        scene ep11_tg52 with dissolve
    else:
        scene ep11_tg53 with dissolve
    js "How did it go!? Oh my God! Are those the papers?"
    scene ep11_tg54 with dissolve
    my "Haha! Yes! [name] did it!"
    scene ep11_tg55 with dissolve
    my "Jill! Here!"
    scene ep11_tg56 with dissolve
    ji "Oh, do you want me to read them?"
    scene ep11_tg57 with dissolve
    sa "Let's read them together."
    scene ep11_tg58 with dissolve
    isa "I'll put on more coffee."
    if ep8_told_josy_chad:
        scene ep11_tg59 with dissolve
        sa "We should wait for the boys."
        scene ep11_tg61 with dissolve
        js "Where are they? Are they ok?"
        scene ep11_tg60 with dissolve
        my "Derek needed a minute."
    else:
        scene ep11_tg59 with dissolve
        sa "Where the fuck are the boys?"
        scene ep11_tg60 with dissolve
        my "Derek needed a minute. They'll be here soon."
    show screen new_phone_screen
    scene ep11_tg67 with wipeleft
    $ renpy.pause()
    scene ep11_tg68 with dissolve
    $ renpy.pause()
    scene ep11_tg69 with dissolve
    my "See? I did sign a contract for it. I told you I did!"
    scene ep11_tg70 with dissolve
    sa "We're still reading it."
    scene ep11_tg71 with dissolve
    my "Sorry. I don't want to stress you... Take your time."
    if ep10_quinn_help:
        play sound "sound_effects/cellphone.mp3"
        scene ep11_tg71b with dissolve
        "*{i}Phone rings{/i}*"
        mc "(Not now, Quinn...)"
    scene ep11_tg72 with dissolve
    mc "Maya, stop pacing. Sit down over here."
    scene ep11_tg73 with dissolve
    $ renpy.pause()
    scene ep11_tg74 with dissolve
    $ renpy.pause()
    scene ep11_tg75 with dissolve
    my "You did it, [name]... I still can't believe you did it."
    scene ep11_tg77 with dissolve
    $ renpy.pause()
    scene ep11_tg78 with dissolve
    $ renpy.pause()
    scene ep11_tg76 with dissolve
    my "What?"
    scene ep11_tg79 with dissolve
    sa "Go ahead."
    scene ep11_tg80 with dissolve
    ji "Ok... So, um... How do I start?"
    scene ep11_tg81 with dissolve
    mc "Just tell us... Do you know what she signed or what?"
    scene ep11_tg82 with dissolve
    ji "These are papers of a loan made out to your dad from Finnman Banking."
    ji "The good thing about that is that it's his loan. In their eyes, he's the borrower."
    ji "And that makes sense since you told us that your dad is in charge of the money."
    scene ep11_tg83 with dissolve
    ji "That also explains why the loan wasn't on your credit report; it's not your loan."
    scene ep11_tg84 with dissolve
    my "It's not my loan? It's not cosigned!? That's amazing news! Isn't it?"
    play sound "sound_effects/interlude/page_turn.mp3"
    scene ep11_tg89 with dissolve
    ji "Yes, but I'm not done yet. We also have these papers - the ones you signed."
    scene ep11_tg85 with dissolve
    my "Is it bad news?"
    scene ep11_tg90 with dissolve
    sa "It's not a student loan."
    scene ep11_tg89 with dissolve
    ji "And you didn't cosign any loan. You entered a contract with your dad."
    scene ep11_tg85 with dissolve
    my "It's not a student loan?"
    scene ep11_tg90 with dissolve
    sa "The contract you signed says that the funds lent by Finnman Banking to Patrick Bailey, Party 'A', are used to pay for college for the signee Maya Victoria Bailey, Party 'B'."
    sa "Party 'B' - that's you, Maya - agrees to repay the loan to Party 'A' in full after graduation, with monthly payments at an interest rate equal to federal student loans."
    scene ep11_tg91 with dissolve
    sa "Party 'A' will finance tuition, fees, and allowances while Party 'B' studies full-time for a maximum of four years or $75,000."
    sa "Then there are some terms and conditions here... But as a whole... I don't see anything that would allow him to control you, and if it were in here, it couldn't be legally binding - I'm sure."
    scene ep11_tg92 with dissolve
    isa "But it does seem like a valid contract."
    scene ep11_tg94 with dissolve
    ji "Yes... To me, it looks like it is. I'm not a lawyer, but I took a basic course in Corporate law, and from what I can see..."
    ji "There's an offer, acceptance, consideration, and - while you could argue that you didn't understand what you signed - there's capacity."
    scene ep11_tg89 with dissolve
    ji "And the rest of the papers seem to be part of the loans for you and Derek."
    ji "But none of the loans are in any of your names. As the contract states, it's in his name - a private loan from Finnman Banking."

    scene ep11_tg93 with dissolve
    isa "Wow... That loan has a very low interest rate. How did he get that?"
    scene ep11_tg96 with dissolve
    de "Finnman Banking... I know about them from Dad's workplace... They are partners and used to finance customers' auto loans."
    scene ep11_tg93 with dissolve
    isa "So, he's got benefits?"
    scene ep11_tg95 with dissolve
    sa "It's not a student loan, Maya."
    scene ep11_tg85 with dissolve
    my "What does this mean for me?"
    scene ep11_tg94 with dissolve
    ji "I'll run these by my family's lawyer to make sure, but from what we can tell..."
    ji "Your contract is a personal loan binding you to your dad."
    scene ep11_tg85 with dissolve
    my "Ok?"
    scene ep11_tg94 with dissolve
    ji "I'm not sure if you can void the contract unless you both agree on it. I don't see any cancellation clause..."
    ji "But he can't stop paying for college if you go against his wishes. He would be breaching his contract."
    ji "And let's say he does anyway. There's nothing here stopping you from applying for a student loan."
    scene ep11_tg85 with dissolve
    my "This is a good thing, right?"
    scene ep11_tg95 with dissolve
    sa "It's both. But mostly good. Now, you have options you couldn't consider before."
    sa "It changes a lot."
    scene ep11_tg86 with dissolve
    my "I don't know what to do with all of this..."
    scene ep11_tg97 with dissolve
    js "This is the first time we get good news, Maya. You finally have a choice."
    scene ep11_tg85 with dissolve
    my "I have a choice now...?"
    scene ep11_tg98 with dissolve
    ji "You can refinance college and get a student loan."
    scene ep11_tg87 with dissolve
    my "But I would have to confront Dad about this..."
    scene ep11_tg88 with dissolve
    menu:
        "Why not destroy the contract?":
            mc "Sorry if I'm stupid, but I'd like to point out something obvious here..."
            mc "If that's the original document... Just destroy it."
            scene ep11_tg99 with dissolve
            ji "[name], that's illegal."
            scene ep11_tg100 with dissolve
            mc "And is what he does to her legal? He's lying to her and manipulating her."
            mc "And tonight, I caught him abusing her. So, I don't feel bad to suggest we tear it up."
            scene ep11_tg102 with dissolve
            ji "Oh my God..."
            scene ep11_tg103 with dissolve
            js "What? Maya...?"
            scene ep11_tg104 with dissolve
            mc "If there's no proof of a signed contract, how can he hold her to it?"
            scene ep11_tg106 with dissolve
            sa "It could cause a dispute, [name]. We're trying to avoid that."
            sa "And think about the consequences for Maya if Patrick is abusive."
            scene ep11_tg107 with dissolve
            ji "If negotiating with Patrick is out of the question... It's better to refinance the loan and use some of that money to pay him back."
            scene ep11_tg108 with dissolve
            isa "If you already have taken care of it, confronting him will be easier."
        "Get a student loan first":
            mc "You should get a student loan first. So that when you confront him, he has no say in it."
            scene ep11_tg101 with dissolve
            ji "If there is a slim chance he can be reasoned with, I'd recommend doing that first. Perhaps they could reach a mutual agreement."
            scene ep11_tg109 with dissolve
            mc "He can't be reasoned with... Tonight, I caught him abusing her."
            scene ep11_tg102 with dissolve
            ji "He abused her? Oh my God..."
            scene ep11_tg103 with dissolve
            js "What? Maya...?"
            scene ep11_tg108 with dissolve
            isa "Then perhaps, if you have already taken care of the loan, confronting him will be easier."
    scene ep11_tg104 with dissolve
    mc "If you're scared about confronting him, I'll be there with you if you want."
    scene ep11_tg105 with dissolve
    my "I'm not scared; I'm worried about how it could affect Mom."
    scene ep11_tg110 with dissolve
    de "Dad would walk through fire to protect Mom. But Mom would do it too, to protect you."
    de "Mom may be ill, but she'd find a way to be strong for you."
    de "I'll be there with you when you tell him."
    scene ep11_tg111 with dissolve
    ji "And I can help you refinance college if you wish to go through with this. I'll sit with you, and we'll do it together."
    scene ep11_tg112 with dissolve
    $ renpy.pause()
    scene ep11_tg113 with dissolve
    my "I can't believe this..."
    my "I can be free, and that's all thanks to you guys."
    scene ep11_tg114 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season2/vibrate.mp3"
    scene ep11_tg115 with dissolve
    "*{i}Vibrations{/i}*"
    play sound "sound_effects/season2/vibrate.mp3"
    scene ep11_tg116 with dissolve
    mc "Derek!"
    de "I swear, I didn't push it on purpose."
    scene ep11_tg118 with dissolve
    ji "Um... Is that...? Uh... Why do you have that?"
    scene ep11_tg117 with dissolve
    stop music fadeout 3
    my "Don't ask. You don't want to know."
    "*{i}Laughter{/i}*"
    $ new_bio("Maya", "Maya found out that she didn't have a co-signed loan and she could get a student loan to get out of her situation with Patrick.")
    $ new_bio("Jill", "Jill offered Maya her help with applying for a student loan.")
    $ new_bio("Patrick", "Patrick loaned money from a banking partner to cover the tuition and living expenses for Derek and Maya.")
else:
    if ep8_told_josy_chad:
        scene ep11_tg62 with dissolve
    else:
        scene ep11_tg63 with dissolve
    js "How did it go!?"
    scene ep11_tg64 with dissolve
    my "Not well."
    scene ep11_tg66 with dissolve
    js "No... What happened?"
    scene ep11_tg65 with dissolve
    my "We tried our best but didn't get enough time to do it."
    show screen new_phone_screen
    scene ep11_tg119 with wipeleft
    $ renpy.pause()
    scene ep11_tg120 with dissolve
    $ renpy.pause()
    if ep10_quinn_help:
        play sound "sound_effects/cellphone.mp3"
        scene ep11_tg71b with dissolve
        "*{i}Phone rings{/i}*"
        mc "(Not now, Quinn...)"
    scene ep11_tg131 with dissolve
    js "What do we do now? We gotta be able to do something, right?"
    scene ep11_tg138 with dissolve
    sa "If we can't get the contract this way, we must confront him about it and force him to show it."
    scene ep11_tg139 with dissolve
    ji "There's probably some way we can go about it, but none that comes to mind now."
    scene ep11_tg121 with dissolve
    my "It's ok, guys."
    scene ep11_tg132 with dissolve
    js "How can you say it's ok? It's not ok!"
    scene ep11_tg121 with dissolve
    my "I've thought about this for a long time."
    my "We've wracked our heads trying to solve it, only to come up short every time we get an idea."
    scene ep11_tg122 with dissolve
    my "But the more I think about ways to solve it, the less it matters if we do."
    my "Because with all of you here trying to help me, I feel like I've already won."
    scene ep11_tg132 with dissolve
    js "But you haven't won, Maya. Your dad still controls you."
    scene ep11_tg121 with dissolve
    my "Yeah, you're right. He does."
    my "But I look at it like this... In a few more years from now, it won't matter."
    my "The day I graduate from college, it stops mattering. There is an end to this; it's just not today."
    scene ep11_tg132 with dissolve
    js "That's the whole point of this! We want it to end today! Not in years from now."
    js "Do you plan on living like this during that time? Because I don't think I can do that."
    scene ep11_tg121 with dissolve
    my "Don't get me wrong. It sucks!"
    my "But I've finally reached a point where I get to study something I'm passionate about."
    scene ep11_tg122 with dissolve
    my "I love college so much..."
    my "And I don't want to let go of that."
    scene ep11_tg123 with dissolve
    my "We will be in college for what seems like a long time, but look at how fast we reached the end of our first semester. It's almost here..."
    my "I want to focus on what I came here to do and not waste energy fighting this."
    scene ep11_tg133 with dissolve
    js "And what about everything we've done so far? How we've brought everyone together to help you..."
    js "Doesn't that matter anymore?"
    scene ep11_tg123 with dissolve
    my "Of course, you guys matter. You're the ones who've made it easier for me."
    my "Before, I didn't have anyone else to share this with. I felt so alone, but now you are helping me carry this burden."
    scene ep11_tg122 with dissolve
    my "And opening up about it has done a lot for me, more than I thought it would."
    my "I don't see this as giving up, Josy. I will remember how everyone did their best."
    scene ep11_tg133 with dissolve
    js "This is not what I want, Maya."
    scene ep11_tg130 with dissolve
    my "It's not what I want, either. But it's what I choose."
    scene ep11_tg137 with dissolve
    mc "Tonight, I caught Patrick abusing her."
    scene ep11_tg140 with dissolve
    ji "Oh my God..."
    scene ep11_tg134 with dissolve
    js "What? Maya...?"
    scene ep11_tg127 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "You're forced to choose this \n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]":
            $ RPjosy += 5
            $ RPmaya -= 5
            scene ep11_tg124 with dissolve
            mc "This is not what you choose, Maya. It's what's left when all options are exhausted."
            mc "You're forced to choose this."
            scene ep11_tg125 with dissolve
            my "You might think that, but there is a choice as long as options exist."
            my "It's just that my options scare me too much. There's too much risk involved in confronting Dad."
            scene ep11_tg126 with dissolve
            my "If I choose to do that and he takes college away from me... If he takes you guys away from me..."
            my "I wouldn't want to live with that choice."
            my "And that's why I choose this. Because you guys will still be here, and I can go to school every day."
            $ new_bio("Maya", "I didn't agree with Maya when she chose to focus on college instead of finding another way to get the contract from Patrick.")
        "Respect Maya's choice \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[5]]":
            $ RPjosy -= 5
            $ RPmaya += 5
            scene ep11_tg128 with dissolve
            mc "Since the first day I wanted to help you, it's been about letting you make your own choices."
            mc "If this is what you choose and you don't want us to keep trying to find new ways for it to end, I will respect it."
            scene ep11_tg135 with dissolve
            js "But [name]..."
            scene ep11_tg136 with dissolve
            mc "The options she gets to choose between aren't what we want them to be, but it's still a choice."
            mc "If we choose for her, we're no better than Patrick."
            scene ep11_tg129 with dissolve
            my "Thank you, [name]."
            $ new_bio("Maya", "I chose to respect Maya's choice and let her focus on college instead of finding another way to get the contract from Patrick.")
    scene ep11_tg133 with dissolve
    js "Maya? A word?"
    scene ep11_tg141 with dissolve
    js "What about me? What about us? Where's us in your choice?"
    scene ep11_tg143 with dissolve
    my "It's been hard, but you've been here alongside me so far. Haven't you?"
    scene ep11_tg142 with dissolve
    js "..."
    scene ep11_tg143 with dissolve
    my "I'm not choosing to leave you."
    my "You're still a part of my choice. But I can't decide if you want to be."
    stop music fadeout 3
    scene ep11_tg142 with dissolve
    $ renpy.pause()
    $ new_bio("Maya", "Maya chose to focus on college and stop wasting time trying to solve her issues with Patrick.")
jump ep11_ho_main_label

label ep11_quinn_dt_label:
hide screen new_phone_screen
play music "music/ep10/licensed_music/track149.mp3"
scene ep11_quinn41
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_quinn42 with dissolve
$ renpy.pause()

scene ep11_quinn44 with dissolve
$ renpy.pause()
scene ep11_quinn46 with dissolve
$ renpy.pause()
scene ep11_quinn42 with dissolve
$ renpy.pause()
scene ep11_quinn43 with dissolve
qu "Let me in."
scene ep11_quinn45 with dissolve
$ renpy.pause()

scene ep11_quinn47
hide screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_quinn48 with dissolve
$ renpy.pause()

scene ep11_quinn49 with dissolve
qu "Where is she?"
scene ep11_quinn50 with dissolve
bd "Take off your jacket."
scene ep11_quinn53 with dissolve
$ renpy.pause()
scene ep11_quinn50 with dissolve
bd "I'm gonna assume you brought some kind of a weapon."
bd "Raise your arms and let Mick search you."
scene ep11_quinn54 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/thud.mp3"
scene ep11_quinn55 with vpunch
$ renpy.pause()
scene ep11_quinn51 with dissolve
bd "Haha!"
bd "Why would you bring that?"
bd "It's like from those corny movies your dad liked."
bd "You don't bring a knife to a gunfight. He loved that line."
scene ep11_quinn56 with dissolve
qu "Don't flatter yourself. I'm not planning to dull that blade on your sad ass. I always carry it."
scene ep11_quinn57 with dissolve
bd "Remove your shoes, too. I don't need you making the place dirtier."
scene ep11_quinn58 with dissolve
$ renpy.pause()
scene ep11_quinn52 with dissolve
bd "*{i}Sigh{/i}*"
bd "Then again, what's a little mud on the floor when we have to clean up the blood from your friend?"
scene ep11_quinn59 with dissolve
$ renpy.pause()
scene ep11_quinn60 with dissolve
bd "Sit the fuck down!"
scene ep11_quinn61 with dissolve
bd "..."
scene ep11_quinn62 with dissolve
bd "I always had a hunch there were things you weren't telling me..."
bd "I'll give you one chance to tell me the truth. And it better be the truth."
bd "Because you should know that I've grown tired of your bullshit excuses and vaguery."
scene ep11_quinn66 with dissolve
qu "Where is Riona?"
scene ep11_quinn63 with dissolve
bd "I'll tell you where she is. Better yet, let's make a deal for it."
bd "For every piece of truth you tell me, I'll give you a piece of your friend back."
scene ep11_quinn67 with dissolve
bd "And I'm feeling generous tonight. I'll kick it off."
$ renpy.sound.play("sound_effects/table_slam.mp3", channel="sfx2", loop=False)
play sound "sound_effects/season3/piercing.mp3"
scene ep11_quinn68 with vpunch
$ renpy.pause()
scene ep11_quinn69 with dissolve
$ renpy.pause()
scene ep11_quinn62 with dissolve
bd "Now it's your turn."
scene ep11_quinn70 with dissolve
qu "..."
scene ep11_quinn71 with dissolve
qu "What did you do to her?"
scene ep11_quinn64 with dissolve
bd "No way. Are you crying?"
scene ep11_quinn72 with dissolve
bd "You didn't even shed a tear for your dad as he spasmed to death on the floor in front of us, but for this bitch you cry?"
play sound "sound_effects/table_slam.mp3"
scene ep11_quinn62 with vpunch
bd "THIS BITCH THAT YOU USED TO FUCK ME OVER WITH, YOU CRY FOR!?"
scene ep11_quinn73 with dissolve
bd "I'm not getting a story from you, am I?"
bd "You don't have to bother. Wipe that snot off your face."
scene ep11_quinn65 with dissolve
bd "Your bitch ass friend told us everything."
bd "She whimpered and squealed like a pig as she ratted you out."
scene ep11_quinn74 with dissolve
$ renpy.pause()
scene ep11_quinn75 with dissolve
bd "Bring me the money you owe. Every single dollar you've charged extra belongs to me."
bd "And every penny you'll make extra from now on also belongs to me."
scene ep11_quinn76 with dissolve
bd "And if you're doing good - and that's a big fucking if..."
bd "...we can work on building back trust between us."
bd "You can thank Rox for that. Because if this was anyone but you sitting in front of me..."
scene ep11_quinn77 with dissolve
bd "You'd be lying face down in the gutter with a bullet in the back of your fucking skull."
scene ep11_quinn78 with dissolve
qu "Where's...Riona?"
scene ep11_quinn79 with dissolve
$ renpy.pause()
scene ep11_quinn80 with dissolve
qu "Is she...dead?"
scene ep11_quinn81 with dissolve
bd "She suffered, but it was over pretty damned fast."
scene ep11_quinn82 with dissolve
qu "Oh, God..."
scene ep11_quinn83 with dissolve
bd "You really have a soft spot for that bitch."
bd "Whatever you did with her is history. You hear?"
bd "You work for me now, which is hilarious because that's what you were supposed to be doing in the first place."
scene ep11_quinn84 with dissolve
bd "Go to your bitch ass friend. She's alive for now."
bd "Mick dropped her off at her mom's place."
bd "It's always good to know your customer, right?"
scene ep11_quinn85 with dissolve
qu "What?"
scene ep11_quinn86 with dissolve
bd "Bring me the money. All of it. Tonight. I'm done playing games."
bd "Let me hear you say it, you fucking rat!"
scene ep11_quinn87 with dissolve
qu "I'll bring it. I'll bring it..."

stop music fadeout 3
scene ep11_quinn88
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_quinn89 with dissolve
$ renpy.pause()
scene ep11_quinn90 with dissolve
$ renpy.pause()
scene ep11_quinn91 with dissolve
$ renpy.pause()
play music "music/ep11/licensed_music/track155.mp3"

scene ep11_quinn92
hide screen ep10_snow_screen
with dissolve
play sound "sound_effects/door_knock.mp3"
"*{i}Doorknock{/i}*"
scene ep11_quinn93 with dissolve
qu "..."
rim "Who is it?"
scene ep11_quinn94 with dissolve
qu "It's me. Quinn."
$ renpy.sound.play("sound_effects/door_lock.mp3", channel="sfx2", loop=False)
scene ep11_quinn95 with dissolve
play sound "sound_effects/season3/door_squeek.mp3"
$ renpy.pause()
scene ep11_quinn98 with dissolve
qu "Is Riona here?"
scene ep11_quinn96 with dissolve
rim "Y-yes."
rim "Did you...? Did you come alone?"
scene ep11_quinn99 with dissolve
qu "Yes, it's just me."
scene ep11_quinn97 with dissolve
rim "Quinn, what have they done to my girl?"
rim "I'm too scared to call the police."
scene ep11_quinn98 with dissolve
qu "Don't involve the police. Things will be fine."
qu "Can I see her?"
scene ep11_quinn100 with dissolve
$ renpy.pause()
scene ep11_quinn101 with dissolve
qu "Rio...? It's me..."
scene ep11_quinn102 with dissolve
ri "*{i}Rapid breathing{/i}*"
scene ep11_quinn103 with dissolve
qu "Are you ok?"
scene ep11_quinn105 with dissolve
ri "*{i}Breathing intensifies{/i}*"
scene ep11_quinn106 with dissolve
ri "Do I look fucking ok!?"
scene ep11_quinn104 with dissolve
qu "..."
qu "Rio... What have they done to you?"
scene ep11_quinn106 with dissolve
ri "You said you were protecting me from them."
ri "You fucking lied to me... You lied to me."
scene ep11_quinn104 with dissolve
qu "Rio..."
scene ep11_quinn107 with dissolve
ri "I told them everything! Every-fucking-thing!"
ri "And they still did this..."
scene ep11_quinn108 with dissolve
$ renpy.pause()
scene ep11_quinn109 with dissolve
qu "I'll make them pay for what they did to you."
play sound "sound_effects/shove.mp3"
scene ep11_quinn110 with hpunch
ri "No, you fucking won't! You're nothing, Quinn! YOU ARE NOTHING!"
scene ep11_quinn111 with dissolve
ri "When did you ever have things under control? You never did."
ri "All this time, you told me everything was fine and that you could handle it."
ri "But you can't handle shit. You're pathetic!"
scene ep11_quinn112 with dissolve
ri "They threatened me! They threatened Mom!"
ri "This is your fault. All of this is your fucking fault."
ri "And I'm so fucking done with you. Do you hear me!?"
play sound "sound_effects/hit.mp3"
scene ep11_quinn113 with hpunch
ri "I'M DONE!"
scene ep11_quinn113b with dissolve
$ renpy.pause()
scene ep11_quinn114 with dissolve
$ renpy.pause()
scene ep11_quinn115 with dissolve
ri "Don't ever talk to me again."
ri "Get the fuck away from me before they come after Mom too."
scene ep11_quinn116 with dissolve
$ renpy.pause()
scene ep11_quinn117 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep11_quinn118 with dissolve
qu "..."
play sound "sound_effects/door_close.mp3"
scene ep11_quinn119 with dissolve
$ renpy.pause()

play music "music/ep11/licensed_music/track156.mp3"
scene ep11_quinn120 with dissolve
$ renpy.pause()
scene ep11_quinn121 with dissolve
$ renpy.pause()
scene ep11_quinn122 with dissolve
$ renpy.pause()
scene ep11_quinn123 with dissolve
$ renpy.pause()
scene ep11_quinn124 with dissolve
$ renpy.pause()
scene ep11_quinn125 with dissolve
$ renpy.pause()
scene ep11_quinn126 with dissolve
$ renpy.pause()
scene ep11_quinn127 with dissolve
$ renpy.pause()
scene ep11_quinn128 with dissolve
$ renpy.pause()

label ep11_quinn_story_label:
$ guideSuggestedPage = 151
scene ep11_quinn130 with Dissolve(2)
$ renpy.pause()
scene ep11_quinn131 with dissolve
qu "What's an ermine?"
scene ep11_quinn132 with dissolve
rx "It's an animal - like a weasel."
scene ep11_quinn131 with dissolve
qu "Like a rat? Why do you have rats tattooed on your face?"
scene ep11_quinn133 with dissolve
rx "Hold on. Rats? We need to set this shit straight."
rx "Gimme a second. I need my book."
show ep11_quinn134
if not persistent.ep11_cardly4:
    show screen ep11_render_screen("ly4")
with dissolve
rx "Here. I got this book from my mother. When I was a kid, she used to tell me a buncha stories, and there's one that always stuck with me."
play sound "sound_effects/interlude/page_turn.mp3"
show ep11_quinn135
hide screen ep11_render_screen
with dissolve
rx "Look. This is an ermine. Does that look like a rat to you?"
scene bg anim_ermine1_ep11 movie with dissolve
qu "Wow... It's so cute. And white."
rx "Don't be fooled by its appearance."
rx "This animal is a vicious predator."
rx "While you think it looks like a fucking rat, in reality..."
play sound "sound_effects/season3/ermine_bite.mp3"
scene bg anim_ermine2_ep11 movie with hpunch
rx "It's a rat killer!"
rx "It sneaks up on its prey at night and attacks it from behind."
rx "It bites its victim with its sharp teeth repeatedly in the neck until it dies."
qu "Wow..."
scene bg anim_ermine3_ep11 movie with dissolve
rx "Way back in time, this symbol of the ermine meant authority."
rx "Powerful people, to be feared and respected, wore them."
$ renpy.sound.play("sound_effects/season3/ermine_hunt.mp3", channel="sfx2", loop=True)
scene bg anim_ermine4_ep11 movie with dissolve
rx "Humans hunted the ermine for its fur."
rx "They wanted to make majestic coats out of the ermine fur - high-quality shit."
qu "It's running away from them!"
rx "Yes, but..."
play sound "sound_effects/season3/cat_hiss.mp3"
scene bg anim_ermine5_ep11 movie with vpunch
rx "The ermine would rather risk its life and die than run through mud and sully its white fur coat."
rx "Now, that's bravery. And that's pride."
qu "Is that true?"
rx "It's a legend, and legends usually sound better than reality. But I've always found the legend cool as fuck."
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep11_quinn136 with dissolve
rx "You see, in this world, you and me - us - we are the little guys."
rx "We aren't like the rest out there."
scene ep11_quinn137 with dissolve
rx "They sit in their ivory towers with fancy cars, money, and jobs. And they look down on us for being who we are born to be."
rx "And even though we are the little guys doing what we can to survive, bigger predators hunt us and want to see us dead for what we do."
scene ep11_quinn142 with dissolve
rx "That's why we hunt at night, too. We need to be as cunning, fast, and aggressive as the ermine."
scene ep11_quinn137 with dissolve
rx "Q. Always be brave. Always have pride."
scene ep11_quinn138 with dissolve
$ renpy.pause()
scene ep11_quinn139 with dissolve
rx "How about it? Does it still sound like I have a cute animal tattooed on my face?"
stop music fadeout 3
scene ep11_quinn140 with dissolve
qu "Nuh-uh."
scene ep11_quinn141 with dissolve
rx "Good. Don't you ever forget it."

play music "music/ep11/licensed_music/track157.mp3"
scene ep11_quinn128 with dissolve
$ renpy.pause()
scene ep11_quinn129 with dissolve
$ renpy.pause()

play sound "sound_effects/season3/thud.mp3"
scene ep11_quinn143 with vpunch
$ renpy.pause()
scene ep11_quinn144 with dissolve
qu "That's all of it."
scene ep11_quinn148 with dissolve
bd "Looks like you've been busy."
bd "But how can I trust it's everything when your friend tells me otherwise?"
scene ep11_quinn146 with dissolve
qu "It is everything I have. If Rio said anything else, she'd be talking out of her ass. I kept this money from her."
qu "If you want me to continue to sell for you, I need some of it back for my expenses."
scene ep11_quinn149 with dissolve
bd "Hahaha!"
bd "The fucking nerve on you."
scene ep11_quinn145 with dissolve
bd "Who are you? You're not the crying bitch who left here a couple of hours ago."
scene ep11_quinn147 with dissolve
vi "She was crying?"
scene ep11_quinn150 with dissolve
bd "Shut the fuck up."
scene ep11_quinn151 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/paperbag.mp3"
scene ep11_quinn152 with dissolve
bd "I was half-expecting you to skip town, but you seem to be smarter than that."
bd "Well... You gotta spend money to make money."
scene ep11_quinn153 with dissolve
bd "Here. I'm feeling generous. The jacked-up prices put me in a good mood."
scene ep11_quinn146 with dissolve
qu "I don't want to do this, but I'll do this for you if you never hurt my friend ever again."
scene ep11_quinn154 with dissolve
bd "Another demand? You're getting greedy."
bd "You're not in a place to make any fucking demands."
scene ep11_quinn145 with dissolve
$ renpy.pause()
scene ep11_quinn154 with dissolve
bd "Sell the fucking drugs. Bring me the money. And I won't hurt anyone you love."
bd "Now, fuck off."

scene ep11_quinn159 with dissolve
$ renpy.pause()
scene ep11_quinn161 with dissolve
qu "About those increased prices... Who do you think gave me that idea?"
qu "Blood and dirt are not the only things you have to clean up here. You've got an infestation."
scene ep11_quinn162 with dissolve
$ renpy.pause()
scene ep11_quinn160 with dissolve
$ renpy.pause()

scene ep11_quinn155 with dissolve
$ renpy.pause()
scene ep11_quinn156
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
scene ep11_quinn157 with dissolve
bd "{i}Sell the fucking drugs. Bring me the money. And I won't hurt anyone you love.{/i}"
stop music fadeout 3
scene ep11_quinn158 with dissolve
$ renpy.pause()

scene black
hide screen ep10_snow_screen
with Fade(2,1,2)

label ep11_tyb_label:
play music "music/ep11/licensed_music/track158.mp3"
play sound "sound_effects/whoosh_2.mp3"
$ renpy.sound.play("sound_effects/season3/melon.mp3", channel="sfx2", loop=True)
scene ep11_tyb1
$ renpy.pause()
scene ep11_tyb2 with dissolve
$ renpy.pause()
scene ep11_tyb3 with dissolve
$ renpy.pause()
scene ep11_tyb4 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep11_tyb5 with dissolve
ty "Ahhh!!! Get out!"
scene ep11_tyb6 with dissolve
ty "Jiiiiill!!!"
scene bg anim_tyb1_ep11 movie with dissolve
$ renpy.pause()
scene ep11_tyb7 with dissolve
ty "It's noooot whaaat it looooks liiike."
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx2", loop=False)
scene ep11_tyb8
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx1", loop=False)
scene ep11_tyb9
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx2", loop=False)
scene ep11_tyb10
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx1", loop=False)
scene ep11_tyb11
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx2", loop=False)
scene ep11_tyb12
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/whoosh_2.mp3", channel="sfx1", loop=False)
scene ep11_tyb13
ty "Nooo..."

scene bg anim_tyb2_ep11 movie with dissolve
ty "NOOOOOOOOOOO!!!"
pause
$ renpy.music.stop(channel="sfx1", fadeout=0)
$ renpy.music.stop(channel="sfx2", fadeout=0)
$ renpy.music.stop(channel="sfx3", fadeout=0)
stop music
play sound "sound_effects/cloth.mp3"
scene ep11_tyb14 with vpunch
ty "No! Jill! No!!!"

play music "music/ep2/freedom.mp3"
show ep11_tyb15
if not persistent.ep11_cardly5:
    show screen ep11_render_screen("ly5")
with dissolve
ty "Ahhh!!!"
scene ep11_tyb16
hide screen ep11_render_screen
with dissolve
nu "Tybalt? What's wrong?"
scene ep11_tyb17 with dissolve
ty "It hurts!"
scene ep11_tyb19 with dissolve
nu "Try not to move around too much."
nu "It was a nasty tear in your scrotum. It will take a couple of weeks for the wound to heal."
scene ep11_tyb18 with dissolve
nu "Try to separate your legs some more, even in bed."
scene ep11_tyb20 with dissolve
doc "Good evening..."
doc "Is it Tybalt, Archibald or Stewart?"
scene ep11_tyb24 with dissolve
ty "Tybalt."
scene ep11_tyb22 with dissolve
doc "*{i}Mumbles{/i}* What awful names."
scene ep11_tyb20 with dissolve
doc "I'm afraid I have to bring you some bad news. Surgery was successful, so you should not feel worried about that."
doc "Your scrotum will heal fine."
scene ep11_tyb21 with dissolve
doc "But sadly, the same can't be said about your vas deferens."
scene ep11_tyb24 with dissolve
ty "My what?"
scene ep11_tyb21 with dissolve
doc "The tube from your left testicle transporting semen to the ejaculatory ducts was severed in multiple places."
doc "We tried to repair the damages, as one would during a reverse vasectomy, but time will tell if its function can be restored."
scene ep11_tyb23 with dissolve
doc "Although there was some damage to your right testicle, luckily, it should work just fine. And you can hopefully have kids in the future if you wish."
doc "Wait until the scar heals before you ejaculate again. You will likely feel discomfort ejaculating for the upcoming month. If the pain doesn't subside, you need to return."
scene ep11_tyb25 with dissolve
doc "Moreover, you have an infected urinary tract."
doc "I'd advise you to be careful when pleasuring yourself with sugary goods in the future."
scene ep11_tyb23 with dissolve
doc "But if the temptation is insurmountable, at least use a condom to avoid infections."
scene ep11_tyb26 with dissolve
ty "That's absurd! I wasn't pleasuring myself with that watermelon. I fell onto it."
scene ep11_tyb22 with dissolve
doc "Then, staying clear of any watermelons you encounter in the future should not be a problem."
stop music fadeout 5
scene ep11_tyb25 with dissolve
$ renpy.pause()
scene ep11_tyb27 with dissolve
$ renpy.pause()

label ep11_home_label:

if wt_ep9_branch_numbers > 1:

    "Visit home on path?"
    menu:

         "Sage" if branchSage:
            $tmp_mod2="Sage"
         "Maya & Josy" if branchMayaJosy:
            $tmp_mod2="Maya"
         "Jill" if branchJill:
            $tmp_mod2="Jill"
         "Isabella" if branchIsabella:
             $tmp_mod2="Isabella"
         "Others" if branchAlone:
            $tmp_mod2="Others"
         
else:
   if branchSage:
    $tmp_mod2="Sage"
   elif branchMayaJosy:
     $tmp_mod2="Maya"
   elif branchJill:
      $tmp_mod2="Jill"
   elif branchIsabella:
      $tmp_mod2="Isabella"
   elif branchAlone:
      $tmp_mod2="Others"

show screen new_phone_screen
play music "music/ep11/licensed_music/track165.mp3"
queue music ["music/ep9/neils_theme.mp3","music/ep11/licensed_music/track165.mp3"]
if branchJill and tmp_mod2 == "Jill":
    scene ep11_home1 with fade
    $ renpy.pause()
    scene ep11_home2 with dissolve
    mc "This is me. This is where I grew up."
    scene ep11_home3 with dissolve
    ji "Have you lived in this house all your life?"
    scene ep11_home4 with dissolve
    mc "Yes. Dad got this place before I was born."
    mc "It's...um...nothing compared to your home. But you knew that."
    scene ep11_home3 with dissolve
    ji "I think it looks homey. I can't wait to see the inside."
    scene ep11_home5 with dissolve
    ji "What did your dad say when you invited me back home with this short notice?"
    mc "He said he was happy to have you over and that there should be enough food to go around."
    scene ep11_home12 with dissolve
    mc "Dad? We're here."
    scene ep11_home13 with dissolve
    dad "Welcome home!"
    scene ep11_home14 with dissolve
    mc "Dad, this is Jill. Jill, this is my dad, Neil."
    scene ep11_home15 with dissolve
    ji "I'm pleased to meet you, Neil. Or do you prefer Mr. [lname]?"
    scene ep11_home16 with dissolve
    dad "No misters or last names are needed in this house. Neil's fine."
    scene ep11_home17 with dissolve
    dad "Oh! Your coat! Let me get that for you."
    scene ep11_home18 with dissolve
    dad "You'll have to excuse me. It's the first time he brings home a girlfriend; I haven't had a chance to practice."
    scene ep11_home19 with dissolve
    mc "Dad..."
    scene ep11_home20 with dissolve
    dad "But I've had a lot of practice on embarrassing him in front of his friends, so at least I got that bit covered."
    scene ep11_home21 with dissolve
    ji "Haha! Is that so? I take it you have plenty of awkward stories to share."
    scene ep11_home20 with dissolve
    dad "The look on my son's face tells me to stay quiet, but I'm not letting you leave here without hearing a few of them."
    scene ep11_home22 with dissolve
    mc "Why do you do this to me?"
    scene ep11_home20 with dissolve
    dad "Don't worry, I won't scare her away. I think."
    dad "Why don't you show Jill around while I finish up in the kitchen? I'm almost done."
    scene ep11_home23 with dissolve
    mc "Sure, we can do that. Let's head upstairs."
    scene ep11_home24 with dissolve
    dad "What a lovely girl you've found yourself, son."
    scene ep11_home25 with dissolve
    mc "Thanks, Dad. I'm so happy with her."
    scene ep11_home44 with dissolve
    mc "Oh, it looks like Dad brought some new furniture home. That's nice."
    mc "It didn't look like this last time I was home."
    scene ep11_home45 with dissolve
    mc "Behind you, that's the bathroom, if you need to use it. It's in better shape than the rest of the house."
    mc "Dad has been doing some renovations whenever he gets scraps from work."
    mc "But it's going slow because he doesn't want to feel like he's working all day and night."
    scene ep11_home47 with dissolve
    mc "Yeah, so this is my room. Um..."
    mc "I brought some stuff with me when I left for college. That's why it's empty."
    scene ep11_home48 with dissolve
    mc "It's usually not a mess. I guess that's how I left it."
    scene ep11_home49 with dissolve
    mc "Don't mind the boxes. I kept things in them."
    mc "Well, that's what boxes are for..."
    scene ep11_home50 with dissolve
    mc "Oh, I realized there's a stain on the carpet."
    scene ep11_home51 with dissolve
    ji "So, this is the room you grew up in?"
    scene ep11_home52 with dissolve
    mc "Yeah... It's not as neat as your room, haha."
    scene ep11_home53 with dissolve
    ji "Why do I get the feeling that you're ashamed of it?"
    scene ep11_home52 with dissolve
    mc "..."
    mc "I know you know our situation, but it's one thing to discuss and another to show."
    mc "As you can tell... We didn't have much. I've never had much."
    scene ep11_home53 with dissolve
    ji "You don't have to feel ashamed of that."
    scene ep11_home54 with dissolve
    ji "This is you, [name]. I can feel that this is your room."
    ji "Is this where you learned how to play the guitar?"
    scene ep11_home55 with dissolve
    mc "Yeah. My guitar used to be by the bed in that corner."
    mc "I almost always sat on my bed when I played it."
    mc "I'd look out the window when I played for inspiration and got lost in the music."
    scene ep11_home56 with dissolve
    mc "I did my homework on that desk. That's pretty much all I used it for."
    mc "I used to have more toys here when I was younger, but I put them in the attic when I grew too old."
    scene ep11_home57 with dissolve
    ji "Thank you so much for showing it to me. I appreciate it so much."
    scene ep11_home58 with dissolve
    mc "Do you really?"
    scene ep11_home59 with dissolve
    ji "Of course I do. Every bit of yourself that you show me makes me feel closer to you."
    ji "I don't want you to change who you are, and you can't change where you come from, so never hide it."
    ji "Instead, feel proud of yourself and what you've accomplished."
    scene ep11_home60 with dissolve
    $ renpy.pause()
    play sound "sound_effects/door_knock.mp3"
    scene ep11_home61 with dissolve
    "*{i}Doorknock{/i}*"
    scene ep11_home62 with dissolve
    mc "Yeah?"
    scene ep11_home65 with dissolve
    dad "It's been a while since I had to knock on this door."
    dad "I was never quite sure what I'd walk in on."
    scene ep11_home63 with dissolve
    mc "Dad!"
    ji "Hahaha!"
    scene ep11_home66 with dissolve
    dad "Dinner is ready."
    scene ep11_home64 with dissolve
    ji "I feel like I should have brought you something for dinner."
    scene ep11_home67 with dissolve
    dad "Oh, please. All you had to bring was your appetite."
elif branchSage  and tmp_mod2 == "Sage":
    if ep9_sage_vanilla or not ep10_sage_lewd:
        scene ep11_home6 with fade
    else:
        scene ep11_home6b with fade
    $ renpy.pause()
    if ep9_sage_vanilla or not ep10_sage_lewd:
        scene ep11_home7 with dissolve
    else:
        scene ep11_home7b with dissolve
    sa "So, this is your house?"
    scene ep11_home8 with dissolve
    mc "Yep. This is my home."
    scene ep11_home9 with dissolve
    sa "I gotta say, the way you described it to me made me think it was worse."
    scene ep11_home8 with dissolve
    mc "It's not as fancy as your family's apartment."
    scene ep11_home9 with dissolve
    sa "It's not a competition, dude. This looks nice."
    scene ep11_home27 with dissolve
    mc "Dad? We're here."
    scene ep11_home13 with dissolve
    dad "Welcome home!"
    scene ep11_home28 with dissolve
    mc "Dad, this is Sage. Sage, this is my dad, Neil."
    scene ep11_home29 with dissolve
    sa "Hi, it's nice to finally meet you. I've heard a lot of nice things about you."
    scene ep11_home30 with dissolve
    dad "Likewise! Except for the stories about you. I haven't heard many."
    dad "But that's because [name] is embarrassed to share about his love life."
    scene ep11_home32 with dissolve
    mc "Dad..."
    scene ep11_home33 with dissolve
    sa "Yeah, I bet he is. I hear his love life is quite extensive."
    play sound "sound_effects/shove.mp3"
    scene ep11_home34 with hpunch
    mc "Hey..."
    scene ep11_home31 with dissolve
    dad "Oh! Your jacket! Let me get that for you."
    play sound "sound_effects/clothes.mp3"
    scene ep11_home35 with dissolve
    dad "You'll have to excuse me. It's the first time he brings home a girlfriend; I haven't had a chance to practice."
    scene ep11_home36 with dissolve
    sa "You're doing great so far. But I can tell by the look on his face that he's worried about how you'll act in front of me."
    scene ep11_home35 with dissolve
    dad "Haha! He does look worried, doesn't he?"
    scene ep11_home37 with dissolve
    mc "I'm starting to regret this already."
    scene ep11_home35 with dissolve
    dad "Don't worry. I'll try my best not to scare her away."
    dad "Why don't you show Sage around while I finish in the kitchen? I'm almost done."
    scene ep11_home38 with dissolve
    mc "Sure, we can do that. Let's head upstairs."
    scene ep11_home24 with dissolve
    dad "What a lovely girl you've found yourself, son. She seems like a hoot."
    scene ep11_home25 with dissolve
    mc "Thanks, Dad. I'm so happy with her."
    scene ep11_home46 with dissolve
    mc "Oh, it looks like Dad brought some new furniture home. That's nice."
    mc "It didn't look like this last time I was home."
    scene ep11_home68 with dissolve
    sa "At least it took him a while to change the place. My parents turned my room into a home library the moment I moved out."
    scene ep11_home69 with dissolve
    mc "They did?"
    scene ep11_home68 with dissolve
    sa "Yup. They had my things boxed up and stored away by my first visit back home."
    scene ep11_home69 with dissolve
    mc "Oof... How did that feel?"
    scene ep11_home68 with dissolve
    sa "Not too good. It was as if it was final. Like, there's no going back now."
    scene ep11_home70 with dissolve
    mc "Anyway... Behind you, that's the bathroom, if you need to use it. It's in better shape than the rest of the house."
    mc "Dad has been doing some renovations here and there whenever he gets scraps from work."
    mc "But it's going slow because he doesn't want to feel like he's working all day and night."
    scene ep11_home71 with dissolve
    sa "That sounds healthy if you ask me."
    scene ep11_home72 with dissolve
    mc "This is my room. Um..."
    mc "I brought some stuff with me when I left for college, that's why it's empty."
    scene ep11_home73 with dissolve
    mc "It's usually not a mess. I guess that's how I left it."
    scene ep11_home74 with dissolve
    sa "To be fair, your room at the DIKs used to be way worse than this."
    scene ep11_home75 with dissolve
    mc "Thanks for being cool about it. I know this room isn't much."
    scene ep11_home74 with dissolve
    sa "It has what a room needs."
    scene ep11_home75 with dissolve
    mc "Barely."
    scene ep11_home76 with dissolve
    sa "Haha, well, I like it."
    scene ep11_home77 with dissolve
    mc "No, you don't. There's not much to like about it. Just say it sucks."
    scene ep11_home78 with dissolve
    sa "Would that make you feel better?"
    scene ep11_home79 with dissolve
    mc "I feel weird trying to show this off to you as if it's something special."
    scene ep11_home78 with dissolve
    sa "Well, you grew up and made memories in here."
    sa "Sure, it doesn't look like much, but knowing this is where you spent your childhood makes it a special room."
    sa "I'm happy you showed it to me."
    scene ep11_home77 with dissolve
    mc "You're right. It is a special room."
    scene ep11_home76 with dissolve
    sa "There you go."
    scene ep11_home80 with dissolve
    sa "*{i}Smack{/i}*"
    play sound "sound_effects/door_knock.mp3"
    scene ep11_home81 with dissolve
    "*{i}Doorknock{/i}*"
    scene ep11_home65 with dissolve
    dad "It's been a while since I had to knock on this door."
    dad "I was never quite sure what I'd walk in on."
    scene ep11_home82 with dissolve
    mc "Dad!"
    scene ep11_home83 with dissolve
    sa "Haha! That's why I always knock when I visit him, too."
    scene ep11_home66 with dissolve
    dad "Dinner is ready."
else:
    scene ep11_home10 with fade
    $ renpy.pause()
    scene ep11_home11 with dissolve
    $ renpy.pause()
    scene ep11_home26 with dissolve
    mc "Dad, I'm home."
    scene ep11_home13 with dissolve
    dad "Took you long enough. Was the train not on time?"
    scene ep11_home39 with dissolve
    mc "Just a slight delay. Lots of people were traveling today. How are you?"
    scene ep11_home40 with dissolve
    dad "I'm doing well. But I want to hear all about what's up with you."
    scene ep11_home41 with dissolve
    mc "Where do I even start...?"
    scene ep11_home42 with dissolve
    dad "Let's start with food. I hope you're hungry; I'm finishing up in the kitchen."
    scene ep11_home43 with dissolve
    mc "Great! Need a hand?"

if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home84 with fade
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home99 with fade
else:
    scene ep11_home108 with fade
dad "..."
scene ep11_home85 with dissolve
dad "I'm speechless..."
if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home91 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home100 with dissolve
else:
    scene ep11_home109 with dissolve
mc "I know. That's why I couldn't be here with you yesterday."
scene ep11_home86 with dissolve
dad "Did it work out ok?"
if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home93 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home101 with dissolve
else:
    scene ep11_home111 with dissolve
if ep10_got_contracts:
    mc "We found a way to help her with one of her problems, but not all of them."
    mc "I don't know how to handle her being abused by her dad."
    mc "I don't even get how she handles it."
else:
    mc "No, nothing did. But Maya says she's fine with it."
    mc "How can she be fine with it?"

if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home94 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home102 with dissolve
else:
    scene ep11_home110 with dissolve
mc "I can't imagine being in her spot."
mc "That's like if you would abuse me. I feel bad saying those words."
scene ep11_home86 with dissolve
if ep10_got_contracts:
    dad "Is there anything you can do to help her with that? What about filing a report against her dad?"
else:
    dad "Is there anything else you can do to help her? What about filing a report against her dad?"
if branchSage and tmp_mod2 == "Sage":
    scene ep11_home94 with dissolve
elif branchJill and tmp_mod2 == "Jill":
    scene ep11_home103 with dissolve
else:
    scene ep11_home111 with dissolve
mc "Maya says she couldn't because - like it or not - her dad is basically what keeps her mom alive."
mc "She cares so much about her mom's well-being that she'd even put up with those things for her."
scene ep11_home87 with dissolve
dad "It sounds like she had to grow up awfully fast."
if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home91 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home100 with dissolve
else:
    scene ep11_home110 with dissolve
mc "Yeah, and her brother, too."
scene ep11_home86 with dissolve
dad "And so did you."
dad "I wish I could have let you be a kid for longer, but what you said about Patrick not having it easy raising them..."
dad "...I can relate to that."
if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home95 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home104 with dissolve
else:
    scene ep11_home112 with dissolve
mc "Dad, you did amazing on your own."
scene ep11_home87 with dissolve
dad "No, I didn't. It's...been hard. And I've made a lot of mistakes."
if branchSage  and tmp_mod2 == "Sage":
    scene ep11_home92 with dissolve
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home105 with dissolve
else:
    scene ep11_home113 with dissolve
mc "You never resorted to violence. Hell, you rarely got mad at me."
mc "I'm telling you, you did great."
scene ep11_home87 with dissolve
dad "I didn't do great every day."
if branchSage:
    scene ep11_home96 with dissolve
elif branchJill:
    scene ep11_home105 with dissolve
else:
    scene ep11_home113 with dissolve
mc "Every day that mattered, you did."
scene ep11_home88 with dissolve
dad "..."
if branchSage or branchJill and (tmp_mod2 == "Jill" or tmp_mod2 == "Sage"):
    scene ep11_home89 with dissolve
    dad "I'm sorry. Perhaps this is a bad conversation to have when your girlfriend is home with you."
    if branchSage  and tmp_mod2 == "Sage":
        scene ep11_home97 with dissolve
        sa "Not at all. Don't stop yourself if you have things to say."
        sa "I couldn't talk about tough topics with my family; this is refreshing to see."
    else:
        scene ep11_home106 with dissolve
        ji "Please, don't feel that way for my sake."
    scene ep11_home90 with dissolve
    $ renpy.pause()
    if branchSage  and tmp_mod2 == "Sage":
        scene ep11_home98 with dissolve
    else:
        scene ep11_home107 with dissolve
    mc "We can move on from it..."
else:
    scene ep11_home114 with dissolve
mc "I love what you did with the place..."
scene ep11_home115 with dissolve
dad "Heh. You do? Doesn't the furniture make it look like a hotel?"
mc "No hotel I've ever been to."
scene ep11_home116 with dissolve
dad "The hotel bed I brought home is the best bed I've ever slept in."
dad "It hurt my back the first few nights, but some light yoga helped sort that out."
if branchJill  and tmp_mod2 == "Jill":
    scene ep11_home120 with dissolve
    ji "Do you like yoga, too?"
    scene ep11_home124 with dissolve
    dad "My body and mind like it very much. That and meditation - you know, simple breathing exercises? How about you?"
    scene ep11_home120 with dissolve
    ji "Oh, I couldn't agree more. I enjoy it a lot and have tried to get [name] to enjoy it more with me."
    scene ep11_home124 with dissolve
    dad "I'm happy you have common interests. Not that I'd say yoga is one of his."
    dad "Stretching after sparring sessions was pretty much what he'd agree to do with me."
    scene ep11_home117 with dissolve
    mc "So, you're into yoga these days?"
else:
    scene ep11_home117 with dissolve
    mc "Are you doing yoga these days?"
scene ep11_home116 with dissolve
dad "I needed something to stay in shape after I lost my sparring partner."
scene ep11_home117 with dissolve
mc "Like your work doesn't keep you in shape."
if branchJill  and tmp_mod2 == "Jill":
    scene ep11_home124 with dissolve
    dad "It does, but my muscles are like old rubber bands at my age. They need this kind of exercise."
    dad "Are you two taking yoga classes together?"
    scene ep11_home126 with dissolve
    mc "I tagged along to one, but it wasn't the best for me."
    scene ep11_home121 with dissolve
    ji "It wasn't proper exercise for him."
    scene ep11_home125 with dissolve
    dad "[name]... You didn't say that, did you?"
    scene ep11_home126 with dissolve
    mc "Well, it's not. I didn't get tired from it."
    scene ep11_home125 with dissolve
    dad "*{i}Sigh{/i}* [name]..."
    scene ep11_home122 with dissolve
    ji "That's not always the point with exercise."
    scene ep11_home123 with dissolve
    mc "To me, it is."
    scene ep11_home117 with dissolve
    mc "At the gym, I met this guy who's a personal trainer, and he helps me out with sparring."
else:
    scene ep11_home116 with dissolve
    dad "It does, but my mind needed some mental exercise, too. I've been meditating as well."
    if branchSage and tmp_mod2 == "Sage":
        scene ep11_home119 with dissolve
    else:
        scene ep11_home118 with dissolve
    mc "That's funny. I've been doing yoga, too. I tagged along to it, at least."
    mc "And now, at the gym, I've met this guy who's a personal trainer, and he helps me out with sparring."

scene ep11_home116 with dissolve
dad "I'm happy you're still practicing it."
scene ep11_home117 with dissolve
mc "Me too. I'm having so much fun, Dad."
mc "There are highs and lows of being in college, but with everything combined, I'm enjoying it a lot."
scene ep11_home116 with dissolve
dad "There are highs and lows to everything in life, son. It's because of it life is worth living."

if branchMayaJosy  and tmp_mod2 == "Maya":
    scene ep11_home127 with dissolve
    mc "Another high in my life that I gotta tell you about... Um..."
    mc "I'm in a relationship, Dad. Or better said, I'm in two relationships."
    mc "Wait... Maybe that's not better."
    scene ep11_home136 with dissolve
    dad "Did you find yourself a girlfriend?"
    scene ep11_home127 with dissolve
    mc "Um... Girlfriends."
    scene ep11_home137 with dissolve
    dad "Multiple?"
    scene ep11_home127 with dissolve
    mc "Two, to be precise."
    scene ep11_home137 with dissolve
    dad "Son... You can't have two girlfriends."
    dad "Aren't you thinking about their well-being?"
    scene ep11_home128 with dissolve
    mc "It's not like that. We're all dating each other."
    scene ep11_home137 with dissolve
    dad "What...does that mean?"
    scene ep11_home128 with dissolve
    mc "Maya - the girl I just told you about - is one of them. And remember that girl I worked with this summer?"
    scene ep11_home138 with dissolve
    dad "Uh... Jody, right?"
    scene ep11_home129 with dissolve
    if name == "Jody":
        mc "No, that's my name. It is Josy."
    else:
        mc "No, Josy."
    scene ep11_home138 with dissolve
    dad "Oh, was that it?"
    scene ep11_home128 with dissolve
    mc "Yeah. It's them."
    scene ep11_home140 with dissolve
    dad "..."
    scene ep11_home130 with dissolve
    mc "Look, I can hear that it sounds weird when I'm explaining it to you."
    scene ep11_home138 with dissolve
    dad "Son... *{i}Sigh{/i}* What you do with your life is your business. I can't tell you what to do and what not to do."
    dad "I can only give you advice along the way."
    dad "I've also been young and done some questionable things, and I regret many mistakes."
    scene ep11_home131 with dissolve
    mc "Dad... Josy and Maya aren't mistakes, nor are they questionable things. They are my girlfriends."
    scene ep11_home138 with dissolve
    dad "I'm only saying that this Maya girl seems to have a lot on her plate as it is."
    dad "Don't go breaking her heart by having another girlfriend."
    scene ep11_home132 with dissolve
    mc "Dad, I'm telling you it's not like that."
    mc "We're all together in a relationship and we're ok with it."
    scene ep11_home141 with dissolve
    dad "Son... Two girls and a guy... It sounds like fun, but it doesn't sound like a relationship."
    scene ep11_home132 with dissolve
    mc "Stop being old-fashioned. It is a relationship and we're all in it."
    scene ep11_home141 with dissolve
    dad "When I was young, I also had my eyes on multiple women. I know all there is about temptation and that choosing can be hard."
    dad "I don't want you to hurt those girls that you care about."
    scene ep11_home132 with dissolve
    mc "I'm not. Ok?"
    scene ep11_home139 with dissolve
    dad "I'm sorry. I should have kept my mouth shut."
    scene ep11_home133 with dissolve
    mc "I wanted to bring you happy news, but now I feel bad about it."
    mc "You always told me to follow my heart and this is where it's at, Dad."
    scene ep11_home138 with dissolve
    dad "Are you telling me that you love these girls equally much and that they feel the same on their end?"
    scene ep11_home134 with dissolve
    mc "I don't know how they feel..."
    scene ep11_home138 with dissolve
    dad "Relationships are hard. And if there's something I've learned, many women say one thing when they mean another."
    dad "And we men can have a hard time reading the signals that women send us."
    scene ep11_home139 with dissolve
    dad "Just because a woman says they are fine doesn't necessarily mean that they are. You have to stop at that moment and consider if that's how they truly feel."
    dad "And they might go along with something you want, for your sake, but not for them. And this can happen without you even realizing it."
    scene ep11_home132 with dissolve
    mc "Let's drop this. You obviously don't understand anything."
    scene ep11_home139 with dissolve
    dad "Dammit, I've made it worse."
    scene ep11_home132 with dissolve
    mc "I have two girlfriends. You can think whatever you want about it, but that's what it is. You have to find a way to be ok with it."
    scene ep11_home138 with dissolve
    dad "Son..."
    scene ep11_home141 with dissolve
    dad "I'm sorry. I hear you."
    dad "Forgive me for being too blunt."
    scene ep11_home140 with dissolve
    dad "..."
    scene ep11_home135 with dissolve
    $ renpy.pause()
elif branchSage  and tmp_mod2 == "Sage":
    scene ep11_home146 with dissolve
    sa "I see where you get it from now. You two are so much alike."
    scene ep11_home147 with dissolve
    mc "You think?"
    scene ep11_home146 with dissolve
    sa "Totally."
    scene ep11_home154 with dissolve
    dad "We're not completely alike. I've got the looks in the family."
    scene ep11_home148 with dissolve
    sa "Hahaha!"
    scene ep11_home153 with dissolve
    mc "Dad..."
    scene ep11_home148 with dissolve
    sa "And the humor, too."
    sa "I'm sure you have a fun story about [name] you'd wanna share with me."
    scene ep11_home124 with dissolve
    dad "Oh, do I ever?"
    scene ep11_home117 with dissolve
    mc "Dad. No."
    scene ep11_home146 with dissolve
    sa "Pay him no attention. It's story time."
    scene ep11_home124 with dissolve
    dad "When [name] was young, I found him in the attic looking through some boxes-"
    scene ep11_home117 with dissolve
    mc "I know where you're going with this one, and I'll stop you right there."
    scene ep11_home149 with dissolve
    sa "What was in the boxes?"
    scene ep11_home124 with dissolve
    dad "Some of his mother's old clothes."
    dad "When I found him up there, he put on a pair of stockings and sat down, stroking his legs."
    scene ep11_home148 with dissolve
    sa "BAHAHA!"
    scene ep11_home153 with dissolve
    mc "Dad! Stop it."
    scene ep11_home148 with dissolve
    sa "So, your son is a crossdresser?"
    scene ep11_home124 with dissolve
    dad "He said he put them on because he liked how they felt against his hand. He found them very soft."
    scene ep11_home153 with dissolve
    mc "This day was a big mistake."
    scene ep11_home146 with dissolve
    sa "So, that's why you love stockings?"
    scene ep11_home147 with dissolve
    mc "No comment..."
    scene ep11_home149 with dissolve
    sa "Did he wear them a lot growing up?"
    scene ep11_home124 with dissolve
    dad "Haha, no, it was just the one time. But it's not easy to forget."
    scene ep11_home117 with dissolve
    mc "If you stop bringing it up, it will be easier."
    scene ep11_home124 with dissolve
    dad "Now I want to hear your story. Who is Sage?"
    scene ep11_home149 with dissolve
    sa "Oh? Um... Where do I begin?"
    play sound "sound_effects/cellphone.mp3"
    scene ep11_home150 with dissolve
    "*{i}Phone rings{/i}*"
    sa "Shoot... It's Jill. We've got plans tomorrow. Mind if I take this?"
    scene ep11_home154 with dissolve
    dad "Go ahead, but don't try to get out of telling me that story."
    scene ep11_home151 with dissolve
    sa "I won't."
    scene ep11_home152 with dissolve
    sa "Jill! What's up!?"
    scene ep11_home136 with dissolve
    dad "I can see why you like her so much. She seems easy-going."
    scene ep11_home144 with dissolve
    mc "You two are certainly hitting it off... But don't embarrass me like that. I like her a lot."
    scene ep11_home142 with dissolve
    dad "You worry too much. I'm not embarrassing you at all."
    scene ep11_home145 with dissolve
    mc "You told her you had to knock on my door because you'd walk in on me doing stuff and that I used to wear stockings."
    scene ep11_home142 with dissolve
    dad "Well, you did!"
    scene ep11_home143 with dissolve
    mc "She doesn't need to know that."
    mc "Stop smiling."
    scene ep11_home142 with dissolve
    dad "Haha! I've missed you."
    scene ep11_home144 with dissolve
    mc "Me too."
elif branchJill  and tmp_mod2 == "Jill":
    scene ep11_home155 with dissolve
    ji "Thanks for dinner. You sure know how to cook."
    scene ep11_home124 with dissolve
    dad "You are too kind."
    scene ep11_home156 with dissolve
    mc "It was great. Thanks, Dad."
    scene ep11_home155 with dissolve
    ji "May I use the restroom?"
    scene ep11_home158 with dissolve
    mc "You remember where it is, yeah?"
    scene ep11_home159 with dissolve
    ji "Yes. The door from across your room."
    scene ep11_home154 with dissolve
    dad "I had to knock a lot on that door, too."
    scene ep11_home157 with dissolve
    mc "Dad... Could you not?"
    ji "Hahaha!"
    scene ep11_home154 with dissolve
    dad "Don't mind me; I'm just poking fun."
    scene ep11_home145 with dissolve
    mc "At first, I was sad she couldn't stay until Sunday, but maybe that's for the best with the way you're embarrassing me."
    scene ep11_home136 with dissolve
    dad "I'm not being rude, am I?"
    scene ep11_home144 with dissolve
    mc "No, but every time you get that smile on your lips before you start talking, I worry you'll say something weird about me."
    scene ep11_home142 with dissolve
    dad "Haha, you better stay on your toes, then. You were a weird kid."
    scene ep11_home145 with dissolve
    mc "*{i}Sigh{/i}* Thanks..."
    scene ep11_home142 with dissolve
    dad "Happy Thanksgiving, son. I'm thankful you're here."
    scene ep11_home144 with dissolve
    mc "Happy Thanksgiving. Me too."
    mc "Thanks for making Jill feel comfortable. It means a lot."
    scene ep11_home136 with dissolve
    dad "You're welcome."
elif branchIsabella  and tmp_mod2 == "Isabella":
    scene ep11_home160 with dissolve
    mc "(How should I tell him about Bella?)"
    stop music fadeout 3
    mc "(I can't even imagine how he'd react to it.)"
    play sound "sound_effects/whoosh_2.mp3"
    play music "music/ep3/hot_mustard.mp3"
    scene ep11_home164
    mc "Dad! I'm pretty much in a relationship now. She's my teacher and she's married."
    play sound "sound_effects/season2/drink_splash.mp3"
    scene ep11_home170 with vpunch
    dad "*{i}PFFRRRTT{/i}*"
    play sound "sound_effects/whoosh_2.mp3"
    scene ep11_home165
    mc "So, Dad! I am banging my teacher and it's not to get a bump in my grades."
    play sound "sound_effects/slap.mp3"
    scene ep11_home171 with vpunch
    dad "Hell yeah! Put it there, son!"

    play sound "sound_effects/whoosh_2.mp3"
    scene ep11_home166
    mc "Dad! I'm dating a woman who's almost twice my age. Hell, you're even closer to her age than I am!"
    scene ep11_home172
    dad "Oh, no! God, why!?"
    scene ep11_home173
    dad "I HAVE NO SON!"
    dad "I HAVE NO SOOOON!!!"
    play sound "sound_effects/whoosh_2.mp3"
    stop music

    play music "music/ep11/licensed_music/track165.mp3"
    queue music ["music/ep9/neils_theme.mp3","music/ep11/licensed_music/track165.mp3"]
    scene ep11_home160
    mc "..."
    scene ep11_home167 with dissolve
    dad "Everything ok, son?"
    scene ep11_home161 with dissolve
    mc "Uh-huh. The food was amazing."
    scene ep11_home167 with dissolve
    dad "Who would have thought I'd eventually learn to cook a half-decent meal?"
    scene ep11_home162 with dissolve
    mc "So, Dad..."
    scene ep11_home167 with dissolve
    dad "Yes?"
    scene ep11_home162 with dissolve
    mc "I'm dating someone. It's a relationship, I'd say."
    scene ep11_home168 with dissolve
    dad "You are?"
    scene ep11_home161 with dissolve
    mc "Yes!"
    scene ep11_home168 with dissolve
    dad "That's great news! What's her name?"
    scene ep11_home162 with dissolve
    mc "Isabella."
    scene ep11_home167 with dissolve
    dad "Isabella? What a beautiful name! Did you meet her in school?"
    scene ep11_home161 with dissolve
    mc "I... I did!"
    scene ep11_home167 with dissolve
    dad "What is she like?"
    scene ep11_home162 with dissolve
    mc "She's...uh... She's got dark brown hair and sometimes wears fake glasses for looks..."
    mc "She's tall. She's almost my height..."
    mc "She's into reading books and drinking wine."
    scene ep11_home169 with dissolve
    dad "Wine? At her age?"
    scene ep11_home163 with dissolve
    mc "Mhm..."
    scene ep11_home167 with dissolve
    dad "It took me many years to even down a glass of it."
    dad "Is she in your class?"
    scene ep11_home161 with dissolve
    mc "Technically, in one of them. And likely another one next semester."
    scene ep11_home168 with dissolve
    dad "I'm happy for you. When will I get to meet her?"
    scene ep11_home161 with dissolve
    mc "You never know... Someday, maybe."
    scene ep11_home168 with dissolve
    dad "Well, I look forward to it. Tell Isabella I'd love to meet her and that she's welcome here anytime."
    scene ep11_home163 with dissolve
    mc "Mhm."

scene ep11_home174 with dissolve
dad "So... Any news about Zoey? Did you guys get back in touch?"
scene ep11_home178 with dissolve
mc "Uh... We talked, yeah."
if ep9_mad_at_zoey:
    mc "But it's weird between us. It's not like it used to be."
    scene ep11_home176 with dissolve
    dad "Are you not getting along?"
    scene ep11_home178 with dissolve
    mc "I'm trying my best with her, but I'm angry around her and I don't like that."
    mc "I try not to be angry, but I can't help it. I'm having a hard time forgiving her for leaving like she did."
else:
    mc "And we've been hanging out some. It doesn't quite feel like old times, but there are moments when it feels like she never left."
    mc "And when those moments happen, I feel like...uh..."
    mc "I remember the good times we had and how I felt back then."
    scene ep11_home174 with dissolve
    dad "Do you feel nostalgic?"
    scene ep11_home178 with dissolve
    mc "Yes, exactly. And I think she feels the same. But she's gotten harder to read for some reason."
mc "We talked some more the other night and... I told her that I..."
mc "I told her she was my first love."
scene ep11_home176 with dissolve
dad "Oh... You did? How did she respond?"
scene ep11_home178 with dissolve
mc "She went silent... And before she could say something, I stopped her."
mc "Because I feared she would have told me she never felt the same way about me. And that would have made me feel worse."
scene ep11_home177 with dissolve
dad "Putting yourself out there to a girl and not having them reciprocate is a horrible feeling."
dad "I think you were brave for doing that."
if (branchJill and tmp_mod2 == "Jill") or (branchSage and tmp_mod2 == "Sage"):
    dad "But maybe it's not wise to tell her how you feel when you have a girlfriend."
scene ep11_home178 with dissolve
if (branchJill and tmp_mod2 == "Jill") or (branchSage and tmp_mod2 == "Sage"):
    mc "I know, but I had to tell Zoey how I felt because that's all I think about when I see her."
mc "Maybe I should have waited and let Zoey say what she felt, but I got too scared."
mc "And that's where we left off... She's probably at home now."

if (branchJill and tmp_mod2 == "Jill") or (branchSage and tmp_mod2 == "Sage"):
    if branchJill and tmp_mod2 == "Jill":
        mc "Maybe I'll visit her tomorrow after Jill has left."
        scene ep11_home174 with dissolve
        dad "It's up to you. But don't forget about your girlfriend's feelings, that is all I will say."
        jump ep11_jhome_label
    else:
        mc "If Sage is spending tomorrow with Jill, maybe I'll visit Zoey."
        scene ep11_home174 with dissolve
        dad "It's up to you. But don't forget about your girlfriend's feelings, that is all I will say."
        jump ep11_shome_label
else:
    scene ep11_home174 with dissolve
    dad "Go and visit her while you're here."
    scene ep11_home178 with dissolve
    mc "I think I will do that tomorrow. I'm too full after dinner."
    if not (branchAlone and ep10_quinn_help):
        stop music fadeout 3
    scene ep11_home175 with dissolve
    dad "Me too. Let's take a walk around the block. We've been sitting down too much."
    if branchAlone and ep10_quinn_help and "Quinn" not in tmp_mod_list:
        scene ep11_home182 with fade
        $ renpy.pause()
        scene ep11_home179 with dissolve
        $ renpy.pause()
        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"Everything ok? I've tried calling you. I'm getting worried here.",False])
        $ text_message_screen_list.append(["Quinn","Been busy.",True])
        $ text_message_screen_list.append(["%s" % name,"Ok. Good to know that you're alive at least. I'm back home over the weekend. I'm available on Sunday if you need me for something.",False])
        $ text_message_screen_list.append(["Quinn","Ok.",True])
        hide screen new_phone_screen
        scene ep11_home180 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        stop music fadeout 3
        scene ep11_home181 with dissolve
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Quinn",text_message_screen_list)
        $ tmp_mod_list.append("Quinn")
        show screen new_phone_screen
    if branchMayaJosy and "Maya" not in tmp_mod_list:
        $ new_bio("Dad", "I tried to tell Dad about my relationship with Josy and Maya, but he didn't understand it and feared I'd end up hurting them.")
        $ tmp_mod_list.append("Maya")
    if branchIsabella and "Isabella" not in tmp_mod_list:
        $ new_bio("Dad", "I told Dad about my relationship with Bella but hid the fact that she was my teacher and closer to his age than mine.")
        $ tmp_mod_list.append("Isabella")

if wt_ep9_branch_numbers > 1:

    "scrappy" "Do you want to see this scene on other paths?"
    menu:
        "Yes":
            jump ep11_home_label
        "No. Continue the game.":
            pass
            
label ep11_zoey_home_label:



if "Jill" not in tmp_mod_list and branchJill:
    $ new_bio("Jill", "Dad and Jill got along great when I brought her home to meet him.")
    $ new_bio("Jill", "I told Jill about Zoey and what she meant to me. She didn't have many questions about it.")
    $ new_bio("Dad", "Dad and Jill got along great when I brought her home to meet him.")
    
if "Sage" not in tmp_mod_list and branchSage:
    $ new_bio("Sage", "Dad and Sage got along great when I brought her home to meet him.")
    $ new_bio("Sage", "I told Sage about Zoey and what she meant to me. To my surprise, it turned into a fight.")
    $ new_bio("Dad", "Dad and Sage got along great when I brought her home to meet him.")
if "Maya" not in tmp_mod_list and branchMayaJosy:
    $ new_bio("Dad", "I tried to tell Dad about my relationship with Josy and Maya, but he didn't understand it and feared I'd end up hurting them.")
if "Isabella" not in tmp_mod_list and branchIsabella:
    $ new_bio("Dad", "I told Dad about my relationship with Bella but hid the fact that she was my teacher and closer to his age than mine.")
if "Quinn" not in tmp_mod_list and branchAlone and ep10_quinn_help:
        scene ep11_home182 with fade
        $ renpy.pause()
        scene ep11_home179 with dissolve
        $ renpy.pause()
        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"Everything ok? I've tried calling you. I'm getting worried here.",False])
        $ text_message_screen_list.append(["Quinn","Been busy.",True])
        $ text_message_screen_list.append(["%s" % name,"Ok. Good to know that you're alive at least. I'm back home over the weekend. I'm available on Sunday if you need me for something.",False])
        $ text_message_screen_list.append(["Quinn","Ok.",True])
        hide screen new_phone_screen
        scene ep11_home180 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        stop music fadeout 3
        scene ep11_home181 with dissolve
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Quinn",text_message_screen_list)
        show screen new_phone_screen

play music "music/ep_interlude/licensed_music/track109.mp3"
scene ep11_zoey_home1 with fade
$ renpy.pause()
scene ep11_zoey_home3 with dissolve
$ renpy.pause()
play sound "sound_effects/interlude/page_turn.mp3"
scene ep11_zoey_home2 with dissolve
$ renpy.pause()
scene ep11_zoey_home4 with dissolve
zo "{i}Fuck.{/i}"
zo "{i}It wasn't the alcohol. And it wasn't the hangover. I still feel it today.{/i}"
scene ep11_zoey_home5 with dissolve
zo "{i}Every page of this damn notebook hits differently.{/i}"
zo "{i}Every little sketch of him. Every little word about him. Every little heart that I drew.{/i}"
zo "{i}Suddenly, they all mean something else...{/i}"
scene ep11_zoey_home6 with dissolve
zo "{i}I don't know where to go from here.{/i}"
zo "{i}I can't tell him this. It's too late now. Isn't it?{/i}"
scene ep11_zoey_home7 with dissolve
zo "{i}He called me his first love and he fucking meant it.{/i}"
zo "{i}How could I have been this blind? It felt like he put glasses on my face and I could see all of a sudden.{/i}"
scene ep11_zoey_home8 with dissolve
zo "{i}My feelings are starting to make sense. Yet, I can't say those words to him.{/i}"
zo "{i}I can't even write them on this page.{/i}"
zo "{i}Even now, just thinking those words... I panic. And I don't know why!{/i}"
scene ep11_zoey_home9 with dissolve
zo "{i}Is it because admitting it would change things?{/i}"
zo "{i}Realizing it had already changed everything. But those words aren't written on paper yet. Neither are they soundwaves in the air going into his ears.{/i}"
zo "{i}What if I keep them in my head?{/i}"
zo "{i}What the fuck am I even writing?{/i}"
scene ep11_zoey_home10 with dissolve
$ renpy.pause()

play sound "sound_effects/season2/pencil.mp3"
scene ep11_zoey_home11 with dissolve
zmom "Zoey. You have a visitor."
scene ep11_zoey_home12 with dissolve
zo "Who is it?"
scene ep11_zoey_home11 with dissolve
zmom "It's [name]."
scene ep11_zoey_home13 with dissolve
zo "Tell him I'm not feeling well."
scene ep11_zoey_home15 with dissolve
mc "I can come back at another time."
scene ep11_zoey_home16 with dissolve
zmom "Oh! I'm so sorry. I thought-"
scene ep11_zoey_home14 with dissolve
zo "Thanks, Mom... It's fine."
scene ep11_zoey_home17 with dissolve
mc "Are you under the weather?"
scene ep11_zoey_home18 with dissolve
zo "Yeah, I think I caught something at the party. You should keep your distance."
scene ep11_zoey_home19 with dissolve
mc "Oh... Well, you look tired."
scene ep11_zoey_home20 with dissolve
zo "*{i}Groans{/i}* Thanks..."
scene ep11_zoey_home21 with dissolve
mc "I was home over the weekend and wanted to check in on you."
mc "You left the party before I could say goodbye."
scene ep11_zoey_home22 with dissolve
zo "Yeah, I... I was in a hurry. I didn't want to miss my ride home."
scene ep11_zoey_home21 with dissolve
mc "I had this weird feeling it had something to do with our talk."
scene ep11_zoey_home22 with dissolve
zo "No, no. It's all good."
scene ep11_zoey_home23 with dissolve
zo "What about you? You didn't catch anything, did you?"
scene ep11_zoey_home21 with dissolve
mc "No, I'm feeling fine."
scene ep11_zoey_home24 with dissolve
mc "So... What are you up to? Drawing?"
play sound "sound_effects/interlude/book_close.mp3"
scene ep11_zoey_home25 with dissolve
zo "Yeah. Same old, you know?"
scene ep11_zoey_home26 with dissolve
mc "I bet I missed out on many cool sketches."
scene ep11_zoey_home27 with dissolve
zo "Another time, maybe."
scene ep11_zoey_home28 with dissolve
mc "..."
scene ep11_zoey_home29 with dissolve
mc "Look... I was out of line telling you those things at the party."
mc "You wanted me to tell you what I felt and I did. And I know it must have felt sudden to you."
scene ep11_zoey_home30 with dissolve
mc "I think I had to say those things to you because I couldn't be your friend if I didn't."
mc "I've never been one to hide my feelings around you, and it felt like I was."
scene ep11_zoey_home31 with dissolve
zo "..."
scene ep11_zoey_home32 with dissolve
zo "It did take me by surprise."
scene ep11_zoey_home30 with dissolve
mc "I knew it."
mc "You might think you'd hurt me by telling me you don't feel the same."
mc "That's why I think it's best if you don't say anything, and that's why I stopped you from answering."
mc "Truth is, I've tried my best to move on, and I don't know how I'd react to being rejected by you and learning that I was the only one having those feelings."
scene ep11_zoey_home33 with dissolve
zo "(What if I told you I was?)"
scene ep11_zoey_home32 with dissolve
zo "I respect that."
show ep11_zoey_home34
if not persistent.ep11_cardly6:
    show screen ep11_render_screen("ly6")
with dissolve
$ renpy.pause()
show ep11_zoey_home30
hide screen ep11_render_screen
with dissolve
mc "Anyway... I'm sorry. I could have handled it better."
scene ep11_zoey_home32 with dissolve
zo "Don't be sorry."
scene ep11_zoey_home30 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Zoey)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Hug her [m_c1][mod_choices[0]]":
        $ ep11_zoey_hug = True
        mc "I hope this doesn't make things turn weird between us."
        scene ep11_zoey_home32 with dissolve
        zo "Who are we kidding? It already was weird."
        scene ep11_zoey_home30 with dissolve
        mc "Yeah, you're right."
        scene ep11_zoey_home37 with dissolve
        mc "So...? Hug it out?"
        scene ep11_zoey_home38 with dissolve
        $ renpy.pause()
        scene ep11_zoey_home39 with dissolve
        $ renpy.pause()
        scene ep11_zoey_home40 with dissolve
        $ renpy.pause()
        scene ep11_zoey_home41 with dissolve
        $ renpy.pause()
        scene ep11_zoey_home42 with dissolve
        zo "That's a pretty damn good hug..."
        scene ep11_zoey_home43 with dissolve
        mc "Oh..."
        scene ep11_zoey_home42 with dissolve
        zo "What?"
        scene ep11_zoey_home43 with dissolve
        mc "You wanted me to keep my distance."
        scene ep11_zoey_home44 with dissolve
        zo "Huh?"
        scene ep11_zoey_home45 with dissolve
        mc "You're sick."
        scene ep11_zoey_home44 with dissolve
        zo "Oh! Fuck..."
        scene ep11_zoey_home45 with dissolve
        mc "It's fine. I'll take my chances."
        scene ep11_zoey_home46 with dissolve
        $ renpy.pause()
        scene ep11_zoey_home47 with dissolve
        mc "I hope you'll feel better soon."
        scene ep11_zoey_home48 with dissolve
        zo "No sweat. Thanks for dropping by."
        scene ep11_zoey_home49 with dissolve
        $ renpy.pause()
        stop music fadeout 3
        scene ep11_zoey_home50 with dissolve
        $ renpy.pause()
        $ new_bio("Zoey", "I visited Zoey and tried to explain to her how I felt. She understood what I meant, and we hugged it out.")
    "Say goodbye":
        mc "I hope you'll feel better soon."
        scene ep11_zoey_home32 with dissolve
        zo "No sweat. Thanks for dropping by."
        scene ep11_zoey_home35 with dissolve
        $ renpy.pause()
        stop music fadeout 3
        scene ep11_zoey_home36 with dissolve
        $ renpy.pause()
        $ new_bio("Zoey", "I visited Zoey and tried to explain to her how I felt. She understood what I meant.")

label ep11_sj_label:
if not branchSage and not branchJill:
    jump ep11_diks_fight_label
play music "music/ep2/by_your_side.mp3"
scene ep11_sj1 with dissolve
$ renpy.pause()
scene ep11_sj2 with dissolve
sa "I've walked by this place many times but never went inside."
scene ep11_sj3 with dissolve
ji "Are you loving it yet?"
scene ep11_sj4 with dissolve
sa "They seem great at what they're doing."
scene ep11_sj5 with dissolve
ji "What did you decide to get?"
scene ep11_sj6 with dissolve
sa "Anything that keeps me from chewing on my nails."
scene ep11_sj7 with dissolve
ji "Oh, are you one of those?"
scene ep11_sj6 with dissolve
sa "Only when I get bored. Or when I study. Sometimes, those two coincide."
scene ep11_sj8 with dissolve
ji "I hope you're feeling better today."
scene ep11_sj9 with dissolve
sa "I know what you're getting at, but I don't want to have this conversation now."
scene ep11_sj8 with dissolve
ji "I understand. If you feel like you want to at some point..."

if branchSage:
    scene ep11_sj9 with dissolve
    sa "Sorry... I didn't mean to sound like a bitch. I appreciate that you ask, but another thing has soured my mood."
    scene ep11_sj28 with dissolve
    ji "Do you mind sharing?"
    scene ep11_sj10 with dissolve
    sa "I went back home with [name] to meet his dad and have some late Thanksgiving dinner."
    scene ep11_sj30 with dissolve
    ji "Sorry for interrupting, but are you and [name]...?"
    scene ep11_sj11 with dissolve
    sa "He's my boyfriend, yeah."
    if ep9_jill_mood == 1:
        scene ep11_sj30 with dissolve
        ji "I see."
    else:
        scene ep11_sj29 with dissolve
        ji "That's sweet."
    scene ep11_sj10 with dissolve
    sa "[name] wanted to help me take my mind off the divorce and it worked."
    sa "Everything was great until we went to bed, and he told me he still spent time with his ex."
    scene ep11_sj30 with dissolve
    ji "Oh?"
    scene ep11_sj12 with dissolve
    sa "Yeah! \"Oh?\" indeed."
    sa "We got into a stupid argument about it, and it was hard to sleep after."
    scene ep11_sj13 with dissolve
    sa "Look, I get it. He's got a past, and he's had sex before..."
    sa "But why can't he leave that girl in the past where she belongs? Especially now, when he's with me."
    scene ep11_sj12 with dissolve
    sa "He told me he would see her today because they recently started reconnecting after being on a hiatus."
    sa "And because she was his best friend from childhood, he feels that it trumps her being his ex-girlfriend."
    scene ep11_sj30 with dissolve
    ji "And naturally... You don't feel that way."
    scene ep11_sj14 with dissolve
    sa "Nope. Not one bit."
    sa "He wants to spend private time with his ex - a girl he fucked and had feelings for?"
    sa "And I'm supposed to be ok with that? Nuh-uh. I don't think so."
    scene ep11_sj34 with dissolve
    ji "But if it's his best friend from childhood, she clearly means a lot to him."
    scene ep11_sj15 with dissolve
    sa "And that's the problem!"
    sa "Girl, that friend{b}ship{/b} sailed the moment she sat on his dick."
    sa "It's a hierarchy, yeah? And best friend is..."
    scene bg anim_sj_hand_ep11 movie with dissolve
    sa "...waaay below ex-girlfriend. In that hierarchy, it's either up and get promoted to a spouse or get the fuck out."
    scene ep11_sj16 with dissolve
    sa "You can't get demoted back to best friend once you've gotten that promotion."
    scene ep11_sj36 with dissolve
    ji "I wish I could advise you on what to do, but I can only sympathize with you."
    ji "Ultimately, I think it comes down to trust. I think that's what you need in a relationship."
    scene ep11_sj17 with dissolve
    sa "I trust him, but I don't trust her. What are her intentions?"
    sa "She probably knows all the right buttons to push with him, too."
    sa "I know way too little about her to trust that something won't happen between them again."
    sa "Sorry... I'm rambling."
    scene ep11_sj36 with dissolve
    ji "It's good. You're agitated and need to say these things to someone."
    scene ep11_sj18 with dissolve
    sa "I should have tried to keep my cool around him..."
    sa "I basically scolded him and sent him off to the embrace of his ex."
    scene ep11_sj38 with dissolve
    ji "I don't think you did. You're being too hard on yourself."
    ji "Sometimes, it's good to wear your heart on your sleeve."
    scene ep11_sj18 with dissolve
    sa "If you knew me better, you'd know I usually don't."
    scene ep11_sj38 with dissolve
    ji "Then, I'm happy you're comfortable enough sharing this with me."
    scene ep11_sj18 with dissolve
    sa "Thanks for listening and caring. Usually, I talk to [name] when I need to vent, but I can't do that this time."
    scene ep11_sj38 with dissolve
    ji "Of course."
    scene ep11_sj19 with dissolve
    sa "[name] taught me how to fight. Little did he know that I'd end up using those moves on his ex-girlfriend."
    sa "I'm gonna break the nails we make here today on her face."
    scene ep11_sj39 with dissolve
    ji "Hahaha! Oh God. That's way too graphic!"
    scene ep11_sj20 with dissolve
    sa "Hahaha!"
    stop music fadeout 3
    scene ep11_sj40 with dissolve
    ji "I will make it my mission today to convince you not to do that."
elif branchJill:
    scene ep11_sj9 with dissolve
    sa "Thanks."
    scene ep11_sj29 with dissolve
    ji "You're welcome."
    scene ep11_sj22 with dissolve
    sa "So... I overheard you were going back home with [name]."
    scene ep11_sj28 with dissolve
    ji "Yes, I came back from there today. We celebrated Thanksgiving with his dad, and I got to see where he grew up."
    scene ep11_sj22 with dissolve
    sa "How was it?"
    scene ep11_sj30 with dissolve
    ji "It was...mostly good."
    scene ep11_sj23 with dissolve
    sa "Mostly? Did his dad make a move on you or something?"
    scene ep11_sj31 with dissolve
    ji "Oh, God! No! Nothing of the sort."
    scene ep11_sj22 with dissolve
    sa "Haha, then what's wrong?"
    scene ep11_sj32 with dissolve
    ji "I'm not sure if it's oversharing..."
    scene ep11_sj24 with dissolve
    sa "Oh, no... He couldn't get it up?"
    scene ep11_sj33 with dissolve
    ji "Get what up?"
    scene ep11_sj24 with dissolve
    sa "His dick."
    scene ep11_sj31 with dissolve
    ji "No!"
    scene ep11_sj23 with dissolve
    sa "Ok, good. So, he got it up?"
    scene ep11_sj33 with dissolve
    ji "Are you trying to embarrass me?"
    scene ep11_sj22 with dissolve
    sa "Haha, I'm having fun with it."
    scene ep11_sj32 with dissolve
    ji "*{i}Sigh{/i}* We were in bed talking..."
    ji "And he told me he was going to visit his ex-girlfriend today."
    scene ep11_sj25 with dissolve
    sa "What the fuck? He just said that?"
    scene ep11_sj34 with dissolve
    ji "No, not as blunt as that, but that was the gist of it."
    ji "Apparently, she'd been his childhood friend before they got together."
    scene ep11_sj25 with dissolve
    sa "I know who it is. I think her name is Zoey."
    scene ep11_sj34 with dissolve
    ji "Yes. From the barbecue party."
    scene ep11_sj25 with dissolve
    sa "And from Halloween. She's certainly been around lately."
    scene ep11_sj35 with dissolve
    ji "He told me not to worry and brought her up because he didn't want to hide her from me."
    scene ep11_sj25 with dissolve
    sa "And then he's off today, spending time alone with her."
    scene ep11_sj35 with dissolve
    ji "Am I wrong for worrying about it? I feel bad."
    scene ep11_sj14 with dissolve
    sa "Nope. You're not wrong at all. If it were me, I would be pissed off."
    sa "He wants to spend private time with his ex? A girl he fucked a lot and had feelings for?"
    sa "And you're supposed to be ok with that? Nuh-uh. I don't think so."
    scene ep11_sj36 with dissolve
    ji "Yes, but also...she's been his best friend since childhood. She clearly means a lot to him."
    scene ep11_sj15 with dissolve
    sa "And that's the problem, isn't it? She means a lot to him."
    sa "Girl, that friend{b}ship{/b} sailed the moment she sat on his dick."
    sa "It's a hierarchy, yeah? And best friend is..."
    scene bg anim_sj_hand_ep11 movie with dissolve
    sa "...waaay below ex-girlfriend. In that hierarchy, it's either up and get promoted to a spouse or get the fuck out."
    scene ep11_sj16 with dissolve
    sa "You can't get demoted back to best friend once you've gotten that promotion."
    scene ep11_sj35 with dissolve
    if branchJill and ep9_jm_sad:
        ji "It's a weird situation. [name] is close to Maya, and they've dated. It feels like I should be ok with Zoey, too."
        scene ep11_sj26 with dissolve
        sa "No, I disagree. Maya and Zoey are completely different. You're not out of line reacting to it."
    else:
        ji "I've never been in this situation before."
        scene ep11_sj26 with dissolve
        sa "Well, you're not out of line reacting to it."
    scene ep11_sj36 with dissolve
    ji "I'm not sure what to do about it. I trust him, so I'm trying not to make a big deal out of his history."
    scene ep11_sj26 with dissolve
    sa "Just because you trust him doesn't mean you trust her. What are her intentions?"
    sa "She probably knows all the right buttons to push with him, too. I wouldn't trust her."
    scene ep11_sj37 with dissolve
    ji "..."
    scene ep11_sj27 with dissolve
    sa "Sorry... I'm making you more worried."
    scene ep11_sj36 with dissolve
    ji "*{i}Sigh{/i}* No, it's good. I needed to hear this. I tend to be naive."
    scene ep11_sj27 with dissolve
    sa "Aw..."
    sa "Want me to kick her ass for you?"
    scene ep11_sj38 with dissolve
    ji "Haha! No. There's no need to get violent."
    scene ep11_sj19 with dissolve
    sa "[name] taught me how to fight. Little did he know that I'd end up using those moves on his ex-girlfriend."
    sa "I'm gonna break the nails we make here today on her face."
    scene ep11_sj39 with dissolve
    ji "Hahaha! Oh God. That's way too graphic!"
    scene ep11_sj21 with dissolve
    sa "Haha! Cheered up?"
    stop music fadeout 3
    scene ep11_sj40 with dissolve
    ji "Yeah. You certainly have a way to make me laugh."

label ep11_diks_fight_label:
$ guideSuggestedPage = 152
play music "music/ep11/licensed_music/track166.mp3"
scene ep11_diks_fight1 with wipeleft
"*{i}Indistinct yelling{/i}*"
mc "What's going on?"
scene ep11_diks_fight2 with dissolve
rs "It's chaos..."
scene ep11_diks_fight3 with dissolve
tm "No! You can go fuck YOURSELF!"
scene ep11_diks_fight4 with dissolve
rs "Can we talk without screaming at each other?"
rs "We obviously have a lot to discuss, and it all comes at once. Leon has things to say, I know Derek has things to say, and you got things to say."
scene ep11_diks_fight5 with dissolve
tm "You're damned fucking right I have things to say! Who the hell fucked Heather!?"
scene ep11_diks_fight8 with dissolve
rs "No one here has fucked Heather, Tommy. What's the problem?"
scene ep11_diks_fight5 with dissolve
tm "No, you're wrong about that! Someone has. She told me someone did."
scene ep11_diks_fight9 with dissolve
jm "Heather said a DIK fucked her?"
scene ep11_diks_fight6 with dissolve
tm "She broke up with me! Ok?"
tm "And her words were that she fucked someone at our Halloween party, and I wanna know who the hell it was!"
scene ep11_diks_fight11 with dissolve
$ renpy.pause()
scene ep11_diks_fight7 with dissolve
tm "John Boy! You know something! I can fucking tell that you do."
scene ep11_diks_fight12 with dissolve
jb "Tommy... I have never fucked Heather!"
scene ep11_diks_fight7 with dissolve
tm "Then who the hell are you covering for!? You look guilty as hell."
scene ep11_diks_fight10 with dissolve
jm "He clearly feels uncomfortable that you want us to point fingers at each other. It's not cool doing this to a bro."
scene ep11_diks_fight6 with dissolve
tm "And do you think fucking someone's girlfriend behind their back is cool?"
tm "Not that anyone would fuck her, but what if it was Dany?"
scene ep11_diks_fight10 with dissolve
jm "Fuck you! I didn't fuck Heather! Don't come at me like I did. There were more guys at the party than DIKs."
scene ep11_diks_fight13 with dissolve
jac "Heather was in your room at the Halloween party, right?"
scene ep11_diks_fight14 with dissolve
le "Me? I didn't have sex with her! What are you accusing me of?"
scene ep11_diks_fight13 with dissolve
jac "I'm not saying you did anything, but you found her buoy there the day after, didn't you?"
scene ep11_diks_fight14 with dissolve
le "Yeah, but what the hell does that have to do with this?"
play sound "sound_effects/shove.mp3"
scene ep11_diks_fight15 with hpunch
tm "Was it you?"
scene ep11_diks_fight16 with dissolve
le "Get off me! No one wanted to bang me the way I looked on Halloween! I was an ugly little girl. Be real, Tommy!"
le "And I was with you a lot that night. Have you already forgotten about it? When would I have done it?"
scene ep11_diks_fight15 with dissolve
tm "Well, if it weren't you guys, then who was it?"
scene ep11_diks_fight17 with dissolve
rs "Tommy! It must have been someone else."
scene ep11_diks_fight17b with dissolve
if ep9_heather_lewd == 2:
    menu:
        "Nudge Nick to come clean together":
            $ ep11_tommy_admit = True
        "Don't say anything":
            $ ep11_tommy_admit = False
else:
    menu:
        "Nudge Nick to come clean":
            $ ep11_tommy_admit = True
        "Don't say anything":
            $ ep11_tommy_admit = False

if ep11_tommy_admit:
    scene ep11_diks_fight18 with dissolve
    if ep10_nick_response == 4:
        mc "Nick, we gotta do it... Look at what's happening."
    else:
        mc "Nick, you gotta do it... Look at what's happening."
    ni "Huh?"
else:
    scene ep11_diks_fight12 with dissolve
    jb "Stop fighting! Look... I saw Heather the morning after Halloween, walking downstairs."
    jb "I talked to [name] about this, too... That's why it's awkward for me."
    jb "I wasn't sure if anything happened, but since you seem to know she did something..."
    jb "Jacob? Nick? Can you make things clear?"
    scene ep11_diks_fight13b with dissolve
    jac "I would if I knew what the fuck you were talking about. Hand on my heart, I slept alone all night."
    scene ep11_diks_fight12 with dissolve
    jb "That means..."
scene ep11_diks_fight19 with dissolve
tm "What? Nick?"
scene ep11_diks_fight20 with dissolve
ni "Well... Y-you..."
scene ep11_diks_fight21 with dissolve
ni "You treat her like shit! All the fucking time! And she's far from it!"
ni "She's the most amazing girl on campus, and you choose to treat her like garbage at any chance you get to fuck someone new!"
scene ep11_diks_fight22 with dissolve
tm "You're doing this to me? After all we've been through..."
scene ep11_diks_fight23 with dissolve
tm "It all makes fucking sense now! The way you're always asking about her... Why you ratted me out to her when I cheated in the past..."
tm "You're in love with my girl!"
scene ep11_diks_fight21 with dissolve
ni "At least one of us is. And it doesn't sound like she's your girl anymore. It looks like she's as fed up with you as I am!"
play sound "sound_effects/hit.mp3"
scene ep11_diks_fight24 with hpunch
tm "You motherfucker!"
rs "Tommy! Stop!"
scene ep11_diks_fight25 with dissolve
tm "You're a fucking traitor!"
scene ep11_diks_fight28 with dissolve
ni "Fuck you! I fucked her, but I'm not the only one who would if she tried to jump them like she did me."
ni "How she feels and how you treat her isn't news to anyone!"
scene ep11_diks_fight29 with dissolve
ni "If you look around the room, everyone knows how fed up Heather is with you."
ni "That's why they all look so fucking guilty!"
ni "They're shutting up to protect themselves, and it's making me look like I'm the bad guy when it's you who's the real asshole here."
scene ep11_diks_fight26 with dissolve
tm "You're a fucking liar!"
play sound "sound_effects/shove.mp3"
scene ep11_diks_fight27 with vpunch
tm "Get off me!"
scene ep11_diks_fight29 with dissolve
ni "I'm a liar? I know for a fact I'm not the only one here who knows about it."
scene ep11_diks_fight30 with dissolve
if ep11_tommy_admit:
    if ep10_nick_response == 4:
        ni "And I find it funny how [name] wants me to confess when he's done the same thing! At the same fucking party too!"
        ni "That's why the buoy was in Leon's room! She tried to get with us all."
        scene ep11_diks_fight31 with dissolve
        mc "That's why I said that \"we\" gotta do it. Not just you."
        scene ep11_diks_fight34 with dissolve
        mc "Tommy... Heather jumped me on Halloween, too. And she gave me a blowjob to use me like you use other chicks."
        mc "She was hurt, and I was drunk and horny. I shouldn't have done it, but I did it because she kept pushing herself on me. But I didn't fuck her."
        mc "It doesn't excuse me, but it wasn't about any feelings. For her, it was all about getting even."
        scene ep11_diks_fight32 with dissolve
        ni "Wow, how honorable of you to just get a blowie from her."
        scene ep11_diks_fight35 with dissolve
        $ renpy.pause()
    elif ep10_nick_response == 1:
        ni "And I find it funny how [name] wanted me to confess when he knows she tried to fuck him too."
        scene ep11_diks_fight31 with dissolve
        mc "She tried to, but I told her no because I respected Tommy. I didn't do anything with her."
        scene ep11_diks_fight32 with dissolve
        ni "How honorable of you. You're such a bro!"
    else:
        if ep10_nick_response == 2:
            ni "And I find it funny how [name] wants me to confess when he advised me not to tell you before."
            ni "First, you tell me to shut up about it, and now you want me to confess. What the fuck is wrong with you?"
        else:
            ni "And, of course, [name] has to take the fucking high ground and stab me in the back."
        scene ep11_diks_fight31 with dissolve
        mc "I think you should own your mistake and not let your brothers take the hit like this."
        if ep9_heather_lewd == 2:
            mc "And now you can watch me do it."
            scene ep11_diks_fight34 with dissolve
            mc "Tommy... Heather jumped me on Halloween too. And she gave me a blowjob to use me like you use other chicks."
            mc "She was hurt, and I was drunk and horny. I shouldn't have done it, but I did it because she kept pushing herself on me. But I didn't fuck her."
            mc "It doesn't excuse me, but it wasn't about any feelings. For her, it was all about getting even."
            scene ep11_diks_fight32 with dissolve
            ni "Wow, how honorable of you to just get a blowie from her."
            scene ep11_diks_fight35 with dissolve
            $ renpy.pause()
        else:
            scene ep11_diks_fight32 with dissolve
            ni "How honorable of you. You're such a bro."
    scene ep11_diks_fight33 with dissolve
    mc "I'm only trying to help out, dude. I'm not perfect, but I want the best for our frat."
else:
    if ep10_nick_response == 4:
        ni "And I find it funny how [name] watches me take the hit when he's done the same thing! At the same fucking party too!"
        ni "That's why the buoy was in Leon's room! She tried to get with us all."
        scene ep11_diks_fight31 with dissolve
        mc "Dude... *{i}Sigh{/i}*"
        scene ep11_diks_fight34 with dissolve
        mc "He's right... Tommy... Heather jumped me on Halloween, too. And she gave me a blowjob to use me like you use other chicks."
        mc "She was hurt, and I was drunk and horny. I shouldn't have done it, but I did it because she kept pushing herself on me. But I didn't fuck her."
        mc "It doesn't excuse me, but it wasn't about any feelings. For her, it was all about getting even."
        scene ep11_diks_fight32 with dissolve
        ni "Wow, how honorable of you to just get a blowie from her."
        scene ep11_diks_fight35 with dissolve
        $ renpy.pause()
    elif ep10_nick_response == 1:
        ni "And I find it funny how [name] watches me take the hit when he knows she tried to fuck him too."
        scene ep11_diks_fight31 with dissolve
        mc "Yeah, she tried to, but I told her no because I respected Tommy. I didn't do anything with her."
        scene ep11_diks_fight32 with dissolve
        ni "How honorable of you. You're such a bro!"
    else:
        if ep10_nick_response == 2:
            ni "And I find it funny how [name] advises me not to tell you anything and then rats me out to John Boy."
            ni "First, you tell me to shut up about it, and then you do this to me. What the fuck is wrong with you?"
        else:
            ni "And, of course, [name] stabs me in the back and rats me out to John Boy."
        scene ep11_diks_fight31 with dissolve
        mc "I didn't tell John Boy what you did. I chatted with him the morning after Halloween, and you told me what you did at the barbecue."
        if ep9_heather_lewd == 2:
            mc "But don't worry, I'll confess too."
            scene ep11_diks_fight34 with dissolve
            mc "Tommy... Heather jumped me on Halloween too. And she gave me a blowjob to use me like you use other chicks."
            mc "She was hurt, and I was drunk and horny. I shouldn't have done it, but I did it because she kept pushing herself on me. But I didn't fuck her."
            mc "It doesn't excuse me, but it wasn't about any feelings. For her, it was all about getting even."
            scene ep11_diks_fight32 with dissolve
            ni "Wow, how honorable of you to just get a blowie from her."
            scene ep11_diks_fight35 with dissolve
            $ renpy.pause()
    scene ep11_diks_fight33 with dissolve
    if ep9_heather_lewd == 2:
        mc "I'm not perfect, and I regret what I did."
    else:
        mc "I don't like that you're calling me out like that. I haven't done anything wrong."

if ep9_heather_lewd == 2:
    $ RPdiks -= 2
    scene ep11_diks_fight36 with dissolve
    jb "So, when I asked you if you knew something, you lied to me?"
    scene ep11_diks_fight37 with dissolve
    if ep10_told_jb_about_heather:
        mc "I tried to tell you parts of it but didn't know what to say when you asked me. I'm sorry."
    else:
        mc "I'm sorry. I felt like shit doing that...but it had just happened the day before, and I didn't know what to say when you asked me."
    scene ep11_diks_fight36 with dissolve
    jb "Wow..."

scene ep11_diks_fight38 with dissolve
rs "Guys... What the hell is going on here? We're supposed to be a family, but now we're fighting like we hate each other."
scene ep11_diks_fight39 with dissolve
tm "A brother doesn't fuck your girl."
scene ep11_diks_fight29 with dissolve
ni "And a brother doesn't steal from the treasury to feed his habits."
scene ep11_diks_fight43 with dissolve
tm "There's a difference between borrowing and stealing, and it's not for a fucking habit, you asshole."
tm "I was short on cash and I needed it. Rusty was cool with it, too."

scene ep11_diks_fight40 with dissolve
rs "This is draining...and I don't know what to say..."
scene ep11_diks_fight41 with dissolve
le "We're in it now. We have to put all cards on the fucking table. I won't be able to trust any of you until we do."
le "It looks like we're about to murder each other, and there are still important things left to discuss."
scene ep11_diks_fight42 with dissolve
le "Earlier tonight, me, Marc and Chen found out who's been posting the pictures of us on campus."
scene ep11_diks_fight43 with dissolve
tm "Do you think we care about that now?"
scene ep11_diks_fight44 with dissolve
le "Well, I fucking care about it! And I bet you guys will, too, after I tell you what happened."
scene ep11_diks_fight45 with dissolve
le "We caught Beth putting up those posters of us! Beth!"
scene ep11_diks_fight46 with dissolve
jb "Cafeteria Beth?"
scene ep11_diks_fight45 with dissolve
le "Yes! Fucking Hamburger Beth! She was putting up posters of us and Cathy when we spotted her. She tried to run away from us, but we chased her ass."
le "She ran into her dorm, and there they were - a group of them, sitting there conspiring together."
scene ep11_diks_fight48 with dissolve
jac "What group?"
scene ep11_diks_fight108 with Dissolve(2)
le "I recognized most of them. Avery, Kylie, that brown-haired bitch Jamie banged..."
scene ep11_diks_fight109 with dissolve
jm "Celery, cereal...um...Celine!?"
le "Yes! Fucking Celine!"
scene ep11_diks_fight112 with dissolve
le "Girls we've banged who stopped coming to our parties and some that still do."
scene ep11_diks_fight110 with dissolve
le "They had printed piles of posters and started yelling when I accused them of doing what they had done."
scene ep11_diks_fight111 with dissolve
le "They screamed about how the DIKs were disgusting and how we've humiliated them in the past."
scene ep11_diks_fight47 with dissolve
jb "We haven't humiliated them!"
scene ep11_diks_fight49 with dissolve
le "That's what I said!"
le "But the Walk of Shame, dude. They said we had humiliated them with that on top of some other bullshit that I think Vinny once did."
le "Locking them outdoors with only underwear or nude, I don't know what it was."
scene ep11_diks_fight51 with dissolve
rs "So, they tried to frame us with that cluck? And they kept bullying Cathy until she quit to get back at us?"
scene ep11_diks_fight50 with dissolve
le "It's them, and we gotta do something about it."
scene ep11_diks_fight52 with dissolve
jm "We should report them for this!"
scene ep11_diks_fight54 with dissolve
jac "I can't believe Beth would do that to us. She still parties with us like it's nothing."
scene ep11_diks_fight55 with dissolve
le "Avery, Kylie, Penny and Tara, too."
scene ep11_diks_fight53 with dissolve
jm "Tara!? No way."
scene ep11_diks_fight55 with dissolve
le "She was in there with them. And, yeah, that one hurt."
le "And I caught them doing it - red-fucking-handed."
scene ep11_diks_fight54 with dissolve
jac "But this doesn't make sense based on what Derek said..."
scene ep11_diks_fight56 with dissolve
de "Yeah... You're right. But at the same time, I don't think I am wrong, especially not about the rest."
scene ep11_diks_fight57 with dissolve
le "With what now?"
scene ep11_diks_fight58 with dissolve
de "With this! This hidden fucking camera that has recorded me in my room!"
de "Someone has to come clean about this right fucking now, or I swear I'm out of here..."
scene ep11_diks_fight59 with dissolve
de "Really? No one is gonna fess up?"
scene ep11_diks_fight60 with dissolve
tm "So many traitors among us..."
scene ep11_diks_fight61 with dissolve
rs "Derek found this camera in his room - in his ceiling spotlight."
rs "And a picture from it was sent to the jocks in a letter earlier this semester."
rs "And not only that. More pictures were sent together with it. Pictures from our laptop..."
rs "The ones where some of us are having sex with Arieth."
scene ep11_diks_fight57 with dissolve
le "What?"
scene ep11_diks_fight59 with dissolve
de "And someone here is lying through their teeth, not admitting they had something to do with it."
de "Someone in here has recorded me doing things in that room and is using this camera and our laptop to fuck us all over."
de "And I don't believe that it's those dorm girls for one second. They couldn't have installed this camera."
scene ep11_diks_fight62 with dissolve
jm "What did the jocks say about it? Did they just get a letter with the pictures?"
scene ep11_diks_fight63 with dissolve
jac "Anthony and Chad say it was [name] who sent it. That's why Chad fought him and got suspended."
scene ep11_diks_fight64 with dissolve
mc "Whoa, hold up! I never sent them a letter with any pictures."
mc "Why the fuck would they even say that? That's made up!"
scene ep11_diks_fight65 with dissolve
de "They seemed sure about it, but I know it's not you."
scene ep11_diks_fight66 with dissolve
ni "Why couldn't it have been [name]? Is he free from scrutiny because Derek is his pal?"
scene ep11_diks_fight67 with dissolve
mc "It's not me! Chad fought me during Hell Week! And you guys barely allowed me in here back then."
mc "How could I have already installed a fucking camera in a random closet and sent the jocks pictures I didn't know existed?"
scene ep11_diks_fight68 with dissolve
rs "...from a laptop you didn't use."
scene ep11_diks_fight69 with dissolve
le "But the laptop went missing...anyone could have used it."
scene ep11_diks_fight70 with dissolve
mc "That happened after Chad and I fought."
mc "And besides, it wasn't me who sent it. I can't answer why the jocks would pin the blame on me for it."
scene ep11_diks_fight71 with dissolve
jm "Then who was it? It's not me, either."
scene ep11_diks_fight72 with dissolve
de "That's the thing! No one is confessing. But someone here knows something they're not sharing, and that pisses me off!"
de "What kind of brotherhood is this!?"
scene ep11_diks_fight73 with dissolve
$ renpy.pause()
scene ep11_diks_fight74 with dissolve
rs "Here's a thought..."
rs "Could it have been Vinny who put the camera in your room? Didn't he use to fuck girls all over the place?"
scene ep11_diks_fight75 with dissolve
tm "It sounds like something he would do."
scene ep11_diks_fight79 with dissolve
ni "You're always quick to blame Vinny. Let's not forget who hung those poster pics of us on our wall to begin with."
ni "For all we know, it could have been you who sent the jocks the pictures. You're just as shady as Vinny."
scene ep11_diks_fight76 with dissolve
tm "From the sound of it, it's more up your alley, you sneaky motherfucker."
tm "You've lied and betrayed us in so many ways already."
tm "What else have you done that you've gotten away with?"
scene ep11_diks_fight79 with dissolve
ni "In so many ways, huh? I've done nothing! You're clutching at straws because you're blinded by rage. It's your typical M.O."
scene ep11_diks_fight76 with dissolve
tm "You've done nothing?"
tm "You fucked my girl behind my back and got close to her."
scene ep11_diks_fight77 with dissolve
tm "You jump on the chance to let other DIKs take the blame to save your pathetic ass... You didn't speak up when I accused anyone else in here."
scene ep11_diks_fight80 with dissolve
ni "I'm not the only one who did bad shit!"
scene ep11_diks_fight77 with dissolve
tm "See! You're doing it again."
tm "And you constantly protect Vinny like he couldn't have done anything wrong. Even when you knew he did illegal shit all the time and still does."
tm "And you just called Derek out for protecting [name] as if that was wrong. But I guess it's fine when you're the one doing it."
scene ep11_diks_fight79 with dissolve
ni "And you always tried to fight Vinny because he did things better than you, just like you do with [name]."
scene ep11_diks_fight78 with dissolve
tm "This is not about [name]. Stop throwing him under the fucking bus."
scene ep11_diks_fight80 with dissolve
ni "I'm not throwing him under the bus!"
scene ep11_diks_fight77 with dissolve
if ep9_heather_lewd == 2:
    tm "You are! And [name] is owning his fuck ups. You're blaming others for yours."
else:
    tm "You are!"
if not ep11_tommy_admit and ep9_heather_lewd == 2 and ep10_nick_response == 4:
    scene ep11_diks_fight80 with dissolve
    ni "He didn't own anything! I had to bring it up!"
    scene ep11_diks_fight77 with dissolve
    tm "You're doing it again to him."
scene ep11_diks_fight78 with dissolve
tm "And what about you trying to hide the fact that the jocks suspiciously didn't trash your room back when they trashed everyone else's?"
tm "That's been bothering me for a long fucking time. And now it's starting to make sense."
scene ep11_diks_fight80 with dissolve
ni "What? What about that makes any sense?"
scene ep11_diks_fight78 with dissolve
tm "They break every window in here and trash every room, but for some reason, they skipped yours."
scene ep11_diks_fight81 with dissolve
ni "What did you want me to do? Brag that my room wasn't as ruined as yours?"
ni "I'm telling you that I cleaned it the first night! And I didn't wanna rub it in your faces, so I didn't talk much about it."
ni "I don't see what it has to do with anything!"
scene ep11_diks_fight83 with dissolve
tm "It didn't have something to do with anything until tonight..."
tm "When we now know that the jocks are framing [name] for something he didn't do."
scene ep11_diks_fight81 with dissolve
ni "So?"
scene ep11_diks_fight84 with dissolve
tm "So? Someone with access to our dirty pictures and laptop sent the jocks those pictures. Maybe that person also ratted out [name]."
tm "And in return, as a favor, they didn't get their room trashed."
scene ep11_diks_fight79 with dissolve
ni "That's so far from the truth and you know it. You're bending pieces to make them fit."
scene ep11_diks_fight84 with dissolve
tm "You always hated how Vinny left and blamed me for it. Is this your revenge, Nick?"
tm "Maybe you helped those dorm bitches with posting the cluck too. Where even were you that night when it was posted?"
scene ep11_diks_fight80 with dissolve
ni "What? I was here at the party with you guys."
scene ep11_diks_fight85 with dissolve
tm "No. Where were you that moment when the naked cluck of Cathy was posted, Nick?"
scene ep11_diks_fight81 with dissolve
ni "Uh... How could I remember that? It was months ago."
scene ep11_diks_fight84 with dissolve
tm "How could you forget what you were doing during a big moment that affected all of us?"
tm "I was arguing with Quinn after she made my sister play spin the dildo."
scene ep11_diks_fight83 with dissolve
tm "Derek and [name] were playing that game with a bunch of girls."
tm "Rusty ran to his room after he saw the cluck and discovered that the laptop was missing. Then he burst out past me."
scene ep11_diks_fight86 with dissolve
tm "What about you guys?"
scene ep11_diks_fight87 with dissolve
le "I was talking to Jamie and having beers."
scene ep11_diks_fight89 with dissolve
jm "Yeah, we were in here drinking together..."
scene ep11_diks_fight88 with dissolve
jac "I was trying to hook up with some chick upstairs. John Boy was there with me."
scene ep11_diks_fight90 with dissolve
jb "Yeah, I was. Until I had to take a piss, but that was after it happened."
scene ep11_diks_fight81 with dissolve
ni "I...don't remember what I was doing. But that doesn't mean that I did it!"
ni "After it happened, I helped you guys look for the laptop! I remember that."
scene ep11_diks_fight91 with dissolve
mc "Yeah... And I saw you search for the laptop..."
mc "In my room... After Rusty had found it in there."
scene ep11_diks_fight92 with dissolve
rs "After I had found it in there?"
scene ep11_diks_fight93 with dissolve
tm "It doesn't get any clearer than that."
tm "You can't say where you were because you were with the laptop."
tm "And you were searching for it where you had left it. Hoping to cover your tracks."
scene ep11_diks_fight81 with dissolve
ni "This is ridiculous! You guys can't be serious."
scene ep11_diks_fight93 with dissolve
tm "You're not saying anything that would make me think otherwise."
tm "Hell, you're not even defending yourself. You're trying to gaslight us."
scene ep11_diks_fight82 with dissolve
ni "Ok, fine! I was with the laptop."
scene ep11_diks_fight93 with dissolve
tm "And there you have it..."
scene ep11_diks_fight82 with dissolve
ni "But I didn't post that cluck. I swear!"
scene ep11_diks_fight93 with dissolve
tm "Bullshit. We know it was posted from the laptop. And now we caught you in your lie."
scene ep11_diks_fight81 with dissolve
ni "I know it looks bad, and that's why I was silent... What can I even say to defend myself!? I didn't post that cluck!"
ni "Bro, I've been nothing but loyal. You gotta believe me!"
scene ep11_diks_fight94 with dissolve
tm "I'm not your fucking bro. The fucking nerve on you saying you've been loyal after what you did."
tm "I vote that we banish Nick."
scene ep11_diks_fight95 with dissolve
rs "Can we slow down? This is moving way too fast."
rs "We're jumping to conclusions because we're all riled up."
scene ep11_diks_fight96 with dissolve
tm "How is this jumping to conclusions? Have you gone deaf? Didn't you hear everything he said tonight?"
tm "Does that sound like he's a brother to you?"
scene ep11_diks_fight95 with dissolve
rs "The jocks, the dorm girls, a traitor? Who did what and when? It's all so confusing."
scene ep11_diks_fight98 with dissolve
ni "You know what? Don't bother. I won't be a part of a fraternity that unites against me like this. You can all fuck off."
scene ep11_diks_fight97 with dissolve
jb "Nick, come on. We're trying to figure out what happened."
scene ep11_diks_fight98 with dissolve
ni "And I'm the easy one to blame! Like you're all so fucking perfect?"
ni "Peachy fucking perfect! Spot-fucking-free, huh?"
if branchIsabella:
    ni "Perfect, like how [name] fucks the librarian in secret and even brings her here on Halloween?"
if branchMayaJosy:
    ni "Perfect, like how [name] is fucking, not one, but two of you guys' sisters?"
if branchJill:
    ni "Perfect, like how Rusty is salty because [name] is with Jill and how he's been in love with her?"
    ni "That's not different from me being in love with Heather, is it!?"
if branchSage and ep4_toldDerekAboutJade:
    ni "Perfect, like how [name] fucked both Sage and her mom!?"
    ni "She'd be thrilled to hear that, right?"

scene ep11_diks_fight99 with dissolve
ni "Perfect, like how Leon is constantly spewing how Jamie is a pussy behind his back for being with Dany and wishes that they'd break up?"
scene ep11_diks_fight103 with dissolve
jm "What!?"
scene ep11_diks_fight99 with dissolve
ni "Or how about Jamie saying Leon only fights with him because of jealousy and that Leon can't fall in love with girls?"
scene ep11_diks_fight102 with dissolve
le "You told him that?"
scene ep11_diks_fight100 with dissolve
ni "Or perfect like Jacob, who told me he would fuck Heather if she asked him to be a plus one?"
scene ep11_diks_fight101 with dissolve
jac "Bro... That was guy talk."
scene ep11_diks_fight98 with dissolve
ni "And he also wants nothing more than to bang [name]'s ex. What a bro."
ni "And meanwhile, John Boy has been telling me how he wants [name] to cuck him with Elena because of cock envy."
ni "And he calls Tommy insecure and in need of validation because he sleeps around like he does."
ni "And Tommy, in turn, calls Rusty's leadership pathetic because he gets swayed too easily by [name]."
scene ep11_diks_fight104 with dissolve
ni "And all of you are so damned perfect when you're jealous of how [name] got popular with the girls for his dick pic..."
ni "...but pretend he's the best because he bosses us around and gets us some discarded furniture."
scene ep11_diks_fight105 with dissolve
ni "From the look of your faces, you're all shocked I'm saying these things you already know."
ni "And while you call me a traitor, I haven't told anyone these things until now! That's how loyal I've been to you!"
scene ep11_diks_fight106 with dissolve
ni "You guys are fucking assholes, and I see why Vinny left. I would have left with him if I had some balls back then."
ni "Who are you guys kidding? This frat is so beyond saving, and it's not even worth trying anymore!"
play sound "sound_effects/door_slam.mp3"
scene ep11_diks_fight107 with vpunch
stop music
$ renpy.pause(1)
scene black
$ renpy.pause(2)

if ep11_tommy_admit:
    $ new_bio("Nick", "I nudged Nick to come clean and didn't try to keep his secret.")
    $ new_bio("Nick", "Nick snapped after I nudged him to come clean about what he did together with Heather. It turned into a big fight, and he started throwing every DIK under the bus, telling everyone what they had told him in confidence.")
else:
    $ new_bio("Nick", "I didn't nudge Nick to come clean and kept his secret.")
    $ new_bio("Nick", "Nick snapped when he had to come clean about what he did together with Heather. It turned into a big fight, and he started throwing every DIK under the bus, telling everyone what they had told him in confidence.")

if branchJill:
    $ new_bio("Rusty", "Nick said Rusty was in love with Jill and was salty about my relationship.")

$ new_bio("Jacob", "Jacob told Nick he wanted to fuck Heather and Zoey.")
$ new_bio("Tommy", "Heather broke up with Tommy. Tommy went haywire because he found out someone had fucked her on Halloween.")
$ new_bio("Heather", "Heather broke up with Tommy.")
$ new_bio("Tommy", "Tommy accused Nick of being a traitor and did his best to expose him as one.")
$ new_bio("Nick", "Nick admitted he was with the laptop during the party when Cathy's cluck got posted, but he denied having posted it.")
if ep9_heather_lewd == 2:
    $ new_bio("John Boy", "John Boy was shocked and hurt to hear that I had lied to him about what I did with Heather on Halloween.")

$ new_bio("Beth", "Leon, Marc, and Chen caught Beth putting up posters of Cathy and the DIKs.")
$ new_bio("Beth", "According to Leon, Beth conspired together with dorm girls against the DIKs.")
$ new_bio("Kylie", "According to Leon, Kylie conspired together with dorm girls against the DIKs.")
$ new_bio("Tara", "According to Leon, Tara conspired together with dorm girls against the DIKs.")
$ new_bio("Derek", "Derek confronted the DIKs about the hidden camera in his room, but no one confessed.")
$ new_bio("You", "I was accused of sending letters to the jocks with pictures of DIKs having sex with Arieth.")
if ep9_heather_lewd == 2:
    $ new_bio("Tommy", "Even though Heather cheated on him with me, Tommy defended me when Nick tried to throw me under the bus.")
else:
    $ new_bio("Tommy", "Tommy defended me when Nick tried to throw me under the bus.")
$ new_bio("Nick", "Nick didn't want to stay a DIK after the huge fight.")

label ep11_campus_label:
play music "music/ep2/journey_of_hope.mp3"
queue music ["music/ep2/relaxing_ballad.mp3","music/ep2/simple_ballad.mp3","music/ep2/journey_of_hope.mp3"]
show ep11_campus1
if not persistent.ep11_cardly7:
    show screen ep11_render_screen("ly7")
with fade
$ renpy.pause()
scene ep11_campus2
hide screen ep11_render_screen
with dissolve
$ renpy.pause()
scene ep11_campus3 with dissolve
mc "Why are you wearing that?"
scene ep11_campus4 with dissolve
de "You said I should."
scene ep11_campus5 with dissolve
mc "I... Ever heard of bad advice?"
scene ep11_campus6 with dissolve
de "I needed to cheer up today. Just let me wear my stupid top hat."
scene ep11_campus7 with dissolve
de "Yesterday was intense..."
scene ep11_campus8 with dissolve
mc "Yeah, I feel physically ill today. It's like I'm hungover, but I didn't drink last night."
scene ep11_campus9 with dissolve
mc "Thanks for sticking up for me."
scene ep11_campus10 with dissolve
de "Always."
de "I can't believe Nick said all those things. You think you know a guy, and then he does that..."
scene ep11_campus11 with dissolve
mc "He was backed into a corner and kept attacking us, trying to save himself."
scene ep11_campus12 with dissolve
de "Why he'd fight with Tommy I understand, but the way he lashed out on you and everyone else like that..."
de "That was way over the top."
scene ep11_campus11 with dissolve
mc "Yeah, I don't know what that was, and I didn't know there were so many things underneath the surface in the frat."
mc "I thought they all liked me, but apparently, things I do bother them."
mc "I've gotta talk to them later. But right now, I don't even want to return there tonight."
scene ep11_campus12 with dissolve
de "Yeah, I feel the same way."
de "*{i}Sigh{/i}* I'm not even sure we got all the answers last night."
scene ep11_campus13 with dissolve
de "Everyone quickly blamed Nick, but he never admitted to doing all those things. And he did admit he fucked Heather."
scene ep11_campus11 with dissolve
mc "And that he was with the laptop during that party... But he also tried to hide it from us..."
mc "I don't know if he posted the cluck or helped the dorm girls do it, but much of what Tommy said made sense."
scene ep11_campus12 with dissolve
de "But do you think Nick and Vinny had something to do with it?"
scene ep11_campus11 with dissolve
menu:
    "Can't trust Nick":
        $ ep11_nick_attitude = 1
        mc "I don't know who did what. All I know is that I can't trust Nick after this."
        mc "He did a good job burning that bridge yesterday."
        $ new_bio("Nick", "I told Derek that Nick couldn't be trusted.")
        $ new_bio("Derek", "I told Derek that Nick couldn't be trusted.")
    "Need more answers":
        $ ep11_nick_attitude = 0
        mc "I don't know who did what. And I agree with you that we need more answers."
        mc "I don't think we should blame Nick for everything until we know more."
        $ new_bio("Nick", "I told Derek we needed more answers before we blamed Nick for everything.")
        $ new_bio("Derek", "I told Derek we needed more answers before we blamed Nick for everything.")
scene ep11_campus14 with dissolve
ta "Um... Hi, guys. Can we talk?"
scene ep11_campus16 with dissolve
de "Go away. I have nothing to say to you."
scene ep11_campus15 with dissolve
ta "But I have things to say to you."
scene ep11_campus16 with dissolve
de "Then I'll leave."
scene ep11_campus17 with dissolve
ta "[name]?"
scene ep11_campus18 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Zoey)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Go fuck yourself \n{size=-4}[m_c1][mod_choices[3]]":
        $ ep11_tara_attitude += 1
        $ dk(1)
        mc "Go fuck yourself."
        scene ep11_campus19 with dissolve
        ta "Whoa! That's rude."
        scene ep11_campus20 with dissolve
        mc "No shit."
        scene ep11_campus21 with dissolve
        ta "Can you just listen to me?"
    "What do you want?":
        mc "What do you want?"
        scene ep11_campus21 with dissolve
        ta "I want to explain things."
ta "I've tried talking to you guys, but no one wants to listen."
scene ep11_campus18 with dissolve
mc "After what you girls did, can you blame us?"
scene ep11_campus21 with dissolve
ta "It wasn't me, ok?"
scene ep11_campus18 with dissolve
mc "Did you know about it?"
scene ep11_campus22 with dissolve
ta "Well, yeah."
scene ep11_campus18 with dissolve
mc "Then you're part of the problem."
scene ep11_campus23 with dissolve
ta "Wait!"
ta "Just because some think one way doesn't mean we all agree."
scene ep11_campus24 with dissolve
if dtype > 0 or ep11_tara_attitude > 0:
    mc "What the fuck are you yapping about?"
else:
    mc "What are you getting at?"
scene ep11_campus25 with dissolve
ta "It wasn't my idea, ok?"
ta "Some of my friends feel you guys have treated them badly in the past. I didn't tell you about what they did because they're my friends."
ta "But I always thought they were overreacting."
scene ep11_campus26 with dissolve
ta "This whole thing was Avery's idea. She's the one who found the pictures on your wall on Halloween."
ta "I was against putting the posters up, but the rest of them wanted to do it."
scene ep11_campus27 with dissolve
ta "Kylie insisted on it."
scene ep11_campus24 with dissolve
mc "Kylie? Who the fuck is Kylie again?"
scene ep11_campus25 with dissolve
ta "Long hair. Large...um...breasts. She hangs out with Christie and Becky a lot."
scene ep11_campus28 with dissolve
ta "She's on the right."
mc "Oh, her? Why?"
scene ep11_campus25 with dissolve
ta "You guys treated her sister poorly in the past. She even dropped out of college because of it."
ta "She had sex with this Vinny guy, and he locked her outside naked after they were done and made his friends chant as she tried to get her clothes back."
scene ep11_campus29 with dissolve
ta "She had to run naked back to her dorm."
ta "And my friends have many more of those stories, too. You might think you're having fun, but they think you're assholes for doing that."
scene ep11_campus30 with dissolve
mc "Not every one of us has done that to you girls."
scene ep11_campus29 with dissolve
ta "Every time there's a party at your place, you guys do something to humiliate someone. That's not nice, you know?"
scene ep11_campus30 with dissolve
mc "I never did anything like that. And you posted my picture all over campus, humiliating me. That makes you the bad ones."
scene ep11_campus31 with dissolve
ta "They're giving all of you a taste of your own medicine. They want all the DIKs to be punished."
scene ep11_campus30 with dissolve
mc "Do you think what the DIKs did is comparable to what you girls did? You tried to ruin our frat by posting those pictures all over campus."
scene ep11_campus31 with dissolve
ta "That's how they see it. It's tit for tat."
scene ep11_campus30 with dissolve
mc "And what about Cathy? What did she do to deserve what she got? She had to quit her job because of those posters and the bullying."
mc "How did she humiliate any of you? Was she just collateral damage, or what?"
scene ep11_campus25 with dissolve
ta "They just posted what you guys already did."
scene ep11_campus30 with dissolve
mc "What?"
scene ep11_campus29 with dissolve
ta "You posted that cluck and bragged about it, remember?"
scene ep11_campus30 with dissolve
mc "We don't know who posted it. We suspected you girls were involved in it somehow."
scene ep11_campus32 with dissolve
ta "Oh... But it wasn't them."
ta "Avery said putting those posters up on campus was fair game because you already humiliated Cathy on Rooster."
ta "She knew you guys were to blame for it and didn't want it to slip by unpunished."
scene ep11_campus30 with dissolve
mc "(This doesn't look good for Nick...)"
mc "Who the fuck is Avery!?"
scene ep11_campus33 with dissolve
ta "Hold on."
scene ep11_campus28b with dissolve
ta "This is Avery. The scarecrow."
scene ep11_campus30 with dissolve
mc "She's the cause of all this?"
mc "Is that why she's coming to our parties? To find ways to screw us over?"
scene ep11_campus25 with dissolve
ta "It's not just her; more girls are in on it."
scene ep11_campus30 with dissolve
mc "Why are you snitching on them like this? What do you even want?"
scene ep11_campus25 with dissolve
ta "As I said in the beginning, I'm not in on this, but they are my friends."
scene ep11_campus30 with dissolve
mc "Some friend you are."
scene ep11_campus29 with dissolve
ta "I'm a friend of you guys, too. I like the DIKs and your parties."
ta "I think we'd all get along if you guys apologized to my friends for what you did and stopped doing it to them."
scene ep11_campus30 with dissolve
mc "I have nothing to apologize for; you're the ones who owe me an apology."
mc "And if what my brothers do bothers you so much, why the hell do you keep coming back to our parties?"
mc "I know those guys, and they didn't mean anything bad with what they did. They're just having fun together; it's a stupid brotherhood thing."
scene ep11_campus29 with dissolve
ta "Yeah, so can you talk to them? And maybe get them to apologize?"
scene ep11_campus30 with dissolve
mc "..."

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Zoey)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Tell her off \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        $ ep11_tara_attitude += 1
        if ep10_rolling and not branchMayaJosy:
            scene ep11_campus34 with dissolve
        else:
            scene ep11_campus34b with dissolve
        mc "The fucking nerve on you..."
        mc "I should have left with Derek."
        $ new_bio("Tara", "She tried to explain herself to me and told me how she was involved with the other dorm girls. I ended up telling her off.")
    "I'll talk to them \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        if ep10_rolling and not branchMayaJosy:
            scene ep11_campus35 with dissolve
        else:
            scene ep11_campus35b with dissolve
        mc "I'll tell them what you said, but it's not enough to forget what you girls did."
        mc "Don't expect any apologies."
        $ new_bio("Tara", "She tried to explain herself to me and told me how she was involved with the other dorm girls.")

if branchMayaJosy:
    jump ep11_jmc_label
elif ep10_rolling:
    jump ep11_lily_campus_label
elif branchAlone and ep8_quinn_lewd:
    jump ep11_quinn_campus_label
else:
    jump ep11_jade_campus_label

label ep11_lily_campus_label:
$ guideSuggestedPage = 153
if branchMayaJosy:
    scene ep11_lily_campus3 with dissolve
else:
    scene ep11_lily_campus1 with dissolve
ly "Don't tell me that bimbo was making moves on you."
scene ep11_lily_campus2 with dissolve
mc "What? No, she wasn't."
scene ep11_lily_campus3 with dissolve
ly "Hm... She must have done something to you. You look annoyed. Want me to slap that bitch?"
scene ep11_lily_campus4 with dissolve
menu:
    "Would you?":
        mc "Would you?"
        scene ep11_lily_campus3 with dissolve
        ly "Say the word and I'll make a fist before the slap."
        scene ep11_lily_campus4 with dissolve
        mc "Well, that's good to know."
    "Don't bother":
        mc "Don't bother. She's not worth it."
        scene ep11_lily_campus3 with dissolve
        ly "Clearly."
scene ep11_lily_campus5 with dissolve
ly "Talk to me. What's got you upset?"
scene ep11_lily_campus6 with dissolve
mc "At the moment...a lot."
scene ep11_lily_campus7 with dissolve
ly "Wanna be alone?"
scene ep11_lily_campus8 with dissolve
mc "No, I could use a distraction."
scene ep11_lily_campus9 with dissolve
ly "I excel at distractions. Just grab my ass and you'll forget about your troubles."
scene ep11_lily_campus10 with dissolve
mc "I wish."
scene ep11_lily_campus9 with dissolve
ly "Seriously. Grab it."
scene ep11_lily_campus10 with dissolve
mc "Alright."
scene ep11_lily_campus11 with dissolve
mc "That does feel better."
scene ep11_lily_campus12 with dissolve
ly "Magical, isn't it?"
ly "Whenever you feel like sharing what's up, let me know."
scene ep11_lily_campus13 with dissolve
mc "What happened to keeping things shallow?"
scene ep11_lily_campus14 with dissolve
ly "I was thinking about what you said at the jetty."
ly "Perhaps it's ok to share things about ourselves to some degree."
ly "If we're not, we're gonna run out of conversation pretty damned fast, yeah?"
scene ep11_lily_campus15 with dissolve
mc "I'm happy you came around, but I don't feel like talking about the DIKs now."
scene ep11_lily_campus16 with dissolve
ly "Trouble in paradise?"
scene ep11_lily_campus15 with dissolve
mc "Paradise? Try hell."
scene ep11_lily_campus16 with dissolve
ly "Sounds serious."
scene ep11_lily_campus17 with dissolve
mc "It is."
scene ep11_lily_campus18 with dissolve
ly "*{i}Smack{/i}*"
scene ep11_lily_campus19 with dissolve
ly "Don't make a big deal out of it. You looked like you could use it."
scene ep11_lily_campus20 with dissolve
mc "You better stop that. You almost make me think you care about me."
scene ep11_lily_campus21 with dissolve
$ renpy.pause()

if ep8_quinn_lewd:
    scene ep11_lily_campus22 with dissolve
    ly "Sup, Quinn!"
    scene ep11_lily_campus23 with dissolve
    ly "She's clearly not a morning person."
    scene ep11_lily_campus24 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(For Lily path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
    
    menu:
        "Mod: Both":
            $ wt_ep11_quinn_lilly = True
            mc "Yeah..."
            jump ep11_lily_campus2_label
        
        "Stay with Lily \n{size=-4}[m_c1][mod_choices[0]]":
            $ ep11_follow_quinn = False
            mc "Yeah..."
            jump ep11_lily_campus2_label
        "Go after Quinn":
            $ ep11_follow_quinn = True
            mc "I'm gonna talk to her."
            scene ep11_lily_campus25 with dissolve
            ly "Huh? Now?"
            scene ep11_lily_campus26 with dissolve
            mc "Yeah? Is that a problem?"
            scene ep11_lily_campus25 with dissolve
            ly "Your hand is still on my ass, and you're gonna chase another girl down the hall."
            scene ep11_lily_campus26 with dissolve
            mc "That's a yes, right?"
            scene ep11_lily_campus32 with dissolve
            ly "I've got other things to do before class anyway."
            scene ep11_lily_campus33 with dissolve
            mc "(Ok... She did not like that. But I don't care, I wanna talk to Quinn.)"
            $ new_bio("Lily", "Lily tried to make me feel better when I was bummed out about the big fight with the DIKs.")
            $ new_bio("Lily", "Lily was annoyed that I wanted to talk to Quinn when I was with her.")
            jump ep11_quinn_campus_label
else:
    label ep11_lily_campus2_label:
    scene ep11_lily_campus27 with dissolve
    ly "How about if we continue this tonight? I've got some time before work."
    ly "Off the top of my head, I'm thinking I'll give you a private dance like I wouldn't give anyone else."
    scene ep11_lily_campus29 with dissolve
    mc "Fuck, I'd love that... The problem is I have to sort through some stuff today because of what happened yesterday."
    scene ep11_lily_campus28 with dissolve
    ly "Wow, it must be serious for you to say no to sex."
    scene ep11_lily_campus29 with dissolve
    mc "We can skip class and do it now."
    scene ep11_lily_campus27 with dissolve
    ly "Let's take a raincheck."
    ly "I gotta hit the ladies' room before class. Catch you in there."
    scene ep11_lily_campus29 with dissolve
    mc "In the ladies' room?"
    scene ep11_lily_campus27 with dissolve
    ly "You wish."
    scene ep11_lily_campus31 with dissolve
    ly "*{i}Smack{/i}*"
    scene ep11_lily_campus29 with dissolve
    menu:
        "See you in class":
            mc "See you in class."
        "Tease her":
            mc "Can I make a big deal out of that one?"
            scene ep11_lily_campus30 with dissolve
            ly "No. We're in public, you know what this is."
    $ new_bio("Lily", "Lily tried to make me feel better when I was bummed out about the big fight with the DIKs.")
    if wt_ep11_quinn_lilly:
        jump ep11_quinn_campus_label
jump ep11_jade_campus_label

label ep11_quinn_campus_label:
scene ep11_quinn_campus1 with dissolve
mc "Hey, what are you up to?"
scene ep11_quinn_campus2 with dissolve
qu "I'm busy."
scene ep11_quinn_campus3 with dissolve
mc "You don't look busy to me."
scene ep11_quinn_campus2 with dissolve
qu "But I am."
scene ep11_quinn_campus4 with dissolve
mc "Doing what?"
if ep9_prep_truce:
    scene ep11_quinn_campus5 with dissolve
else:
    scene ep11_quinn_campus5b with dissolve
qu "..."
scene ep11_quinn_campus6 with dissolve
mc "Let me guess... You can't talk about it here."
if ep10_quinn_help:
    scene ep11_quinn_campus7 with dissolve
    qu "You got it."
    scene ep11_quinn_campus8 with dissolve
    mc "I know it's probably not it, but this hasn't got anything to do with me not answering your phone call, right?"
    mc "It was poor timing that night."
    scene ep11_quinn_campus9 with dissolve
    qu "Yes and no, but it's got nothing to do with you."
    qu "And right now, you can't help me."
    scene ep11_quinn_campus8 with dissolve
    mc "I {i}can't{/i} help, or you don't want me to help?"
    scene ep11_quinn_campus9 with dissolve
    qu "Both."
    scene ep11_quinn_campus8 with dissolve
    mc "Will you let me try?"
    scene ep11_quinn_campus10 with dissolve
    qu "..."
    scene ep11_quinn_campus11 with dissolve
    qu "No. I think you should stay out of it."
    scene ep11_quinn_campus12 with dissolve
    mc "You're not giving me much to work with..."
    scene ep11_quinn_campus13 with dissolve
    gi "*{i}Psst{/i}*"
    if ep10_rolling:
        scene ep11_quinn_campus14 with dissolve
        qu "You should return to Lily. I bet she misses you."
        scene ep11_quinn_campus15 with dissolve
        mc "(That's two for two... I seem to have a knack for making girls jealous.)"
        $ new_bio("Quinn", "I tried talking to Quinn on campus, but she didn't want to share what was bothering her. She also made a dig at me for hanging out with Lily.")
    else:
        scene ep11_quinn_campus16 with dissolve
        qu "It's one of those days, babe."
        scene ep11_quinn_campus17 with dissolve
        $ renpy.pause()
        scene ep11_quinn_campus18 with dissolve
        mc "You're not gonna scare me away if that's what you're afraid of."
        scene ep11_quinn_campus20 with dissolve
        qu "I know."
        scene ep11_quinn_campus19 with dissolve
        mc "Hey... Anything. Ok?"
        scene ep11_quinn_campus21 with dissolve
        $ renpy.pause()
        $ new_bio("Quinn", "I tried talking to Quinn on campus, but she didn't want to share what was bothering her.")
else:
    scene ep11_quinn_campus7 with dissolve
    qu "I'm busy with things you don't want to be involved with."
    scene ep11_quinn_campus6 with dissolve
    mc "Ah... I understand."
    scene ep11_quinn_campus8 with dissolve
    mc "Well, I hope it works out for you."
    scene ep11_quinn_campus13 with dissolve
    gi "*{i}Psst{/i}*"
    scene ep11_quinn_campus14 with dissolve
    qu "It will."
    scene ep11_quinn_campus15 with dissolve
    mc "*{i}Sigh{/i}*"
    mc "(I know I made the right call. I don't want to get mixed up with what she's doing...)"
    mc "(But it sucks having her blow me off like this... I like her...)"
    $ new_bio("Quinn", "I tried talking to Quinn on campus, but she didn't want to share what was bothering her.")

jump ep11_jade_campus_label

label ep11_jade_campus_label:
$ guideSuggestedPage = 153
scene ep11_jade_campus1 with dissolve
$ renpy.pause()
if ep4_toldDerekAboutJade:
    stop music fadeout 3
    scene ep11_jade_campus5 with dissolve
    ja "You..."
    play music "music/ep3/black_box.mp3"
    mc "(Uh oh...)"
    scene ep11_jade_campus6 with dissolve
    ja "Follow me this instant."
    scene ep11_jade_campus7 with dissolve
    mc "I can't. I've got class."
    scene ep11_jade_campus6 with dissolve
    ja "Your mother could be dying, and I wouldn't excuse you from this. You're coming with me."
    scene ep11_jade_campus8 with dissolve
    mc "(I think I'll let that comment slide...)"
    scene ep11_jade_campus11 with dissolve
    $ renpy.pause()
    scene ep11_jade_campus12 with dissolve
    ja "Sit down."
    scene ep11_jade_campus13 with dissolve
    mc "Uh... Why?"
    scene ep11_jade_campus14 with dissolve
    ja "Sit!"
    scene ep11_jade_campus15 with dissolve
    ja "What was the one thing I asked you to do?"
    scene ep11_jade_campus16 with dissolve
    mc "Is this about class or...?"
    scene bg anim_jade_slap_ep11 movie with dissolve
    pause
    scene ep11_jade_campus17 with dissolve
    ja "You kept the video of us having sex after you promised to delete it!"
    mc "Uh..."
    scene ep11_jade_campus18 with dissolve
    ja "Why did you send it to my husband?"
    scene ep11_jade_campus19 with dissolve
    mc "To your husband!? I would never!"
    scene ep11_jade_campus18 with dissolve
    ja "Then who did you send it to? Because that's where it ended up."
    scene ep11_jade_campus19 with dissolve
    mc "Shit, give me a moment to think!"
    play sound "sound_effects/slap.mp3"
    scene ep11_jade_campus21 with hpunch
    ja "Do you need to think? How many have you shown it? You sick, perverted freak!"
    scene ep11_jade_campus19 with dissolve
    mc "I didn't send it to anyone! I swear."
    scene ep11_jade_campus18 with dissolve
    ja "And now you're lying to me!"
    scene ep11_jade_campus19 with dissolve
    mc "Look, I didn't send it to anyone... But I may have transferred it to a computer."
    play sound "sound_effects/slap.mp3"
    scene ep11_jade_campus21 with hpunch
    mc "Ow!!!"
    scene ep11_jade_campus18 with dissolve
    ja "You promised me you'd delete it."
    scene ep11_jade_campus19 with dissolve
    mc "I know! I know!"
    scene ep11_jade_campus18 with dissolve
    ja "But you never did."
    scene ep11_jade_campus19 with dissolve
    mc "I needed it for Hell Week."
    scene ep11_jade_campus20 with dissolve
    ja "You showed it to your frat!?"
    mc "(Fuck, I shouldn't have said that.)"
    play sound "sound_effects/shove.mp3"
    scene ep11_jade_campus22 with hpunch
    ja "Aargh!!!"
    play sound "sound_effects/shove.mp3"
    scene ep11_jade_campus25 with vpunch
    $ renpy.pause()
    play sound "sound_effects/slap.mp3"
    scene ep11_jade_campus23 with hpunch
    ja "Of course, you fucking did! I should never have trusted you to keep it between us!"
    scene ep11_jade_campus24 with dissolve
    if affinity == "DIK":
        mc "Stop fucking slapping me!"
    else:
        mc "Ow!!! Stop slapping me! Please."
    scene ep11_jade_campus26 with dissolve
    ja "Do you have the slightest idea of what you have done?"
    scene ep11_jade_campus24 with dissolve
    mc "I haven't got a clue."
    scene ep11_jade_campus27 with dissolve
    ja "You have cost me everything."
    scene ep11_jade_campus28 with dissolve
    mc "What...? Jade?"
    scene ep11_jade_campus29 with dissolve
    ja "Stephen has filed for a divorce and is using that video to make me settle for breadcrumbs."
    ja "Thanks to you... I have to choose between money or my career and kids."
    scene ep11_jade_campus30 with dissolve
    mc "..."
    mc "I swear... I never thought this would happen when I showed them the video."
    mc "Someone I trusted has betrayed me too."
    scene ep11_jade_campus29 with dissolve
    ja "You've ruined me, [name]. You've literally ruined me."
    ja "All of this because you had to prove to your friends that you had sex with your teacher... I hope it was worth it."
    scene ep11_jade_campus35 with dissolve
    $ renpy.pause()
    scene ep11_jade_campus30 with dissolve
    mc "What will you do?"
    scene ep11_jade_campus31 with dissolve
    ja "*{i}Scoffs{/i}* What will I do? Don't pretend that you care after doing this to me."
    scene ep11_jade_campus30 with dissolve
    mc "Jade... I feel horrible."
    scene ep11_jade_campus29 with dissolve
    ja "All I wanted was a family."
    ja "I couldn't make one of my own, and now I can't keep the one I had to settle for."
    scene ep11_jade_campus34 with dissolve
    $ renpy.pause()
    scene ep11_jade_campus32 with dissolve
    mc "What can I do to make it right?"
    scene ep11_jade_campus33 with dissolve
    ja "Go to class, [name]."
    ja "One day, you'll get yours."
    scene ep11_jade_campus36 with dissolve
    mc "(It was me... I'm the reason they're divorcing. This can't be real...)"
    mc "(That video...)"
    mc "(Did Nick do this or what's going on? Fuck! I want to punch a wall or something.)"
    stop music fadeout 3
    mc "(What the fuck have I done!? I need answers!)"
    play music "music/ep2/simple_ballad.mp3"
    queue music ["music/ep2/relaxing_ballad.mp3","music/ep2/journey_of_hope.mp3","music/ep2/simple_ballad.mp3"]
    $ new_bio("Jade", "Jade confronted me about the Hell Week sex tape I recorded. Someone had sent it to her husband, and he wanted to file for a divorce.")
else:
    scene ep11_jade_campus2 with dissolve
    mc "(Ugh... Jade... I can tell what she's going through by looking at her.)"
    mc "(It feels like there aren't a lot of happy faces on campus today.)"
    if jade_state == 1:
        scene ep11_jade_campus3 with dissolve
        mc "Hey... I heard what happened."
        mc "Can we talk?"
        scene ep11_jade_campus4 with dissolve
        ja "Please, not here."
        scene ep11_jade_campus9 with dissolve
        $ renpy.pause()
        scene ep11_jade_campus11 with dissolve
        $ renpy.pause()
        scene ep11_jade_campus37 with dissolve
        ja "What did you hear?"
        scene ep11_jade_campus38 with dissolve
        mc "I heard about your divorce. I'm so sorry."
        scene ep11_jade_campus39 with dissolve
        ja "Why would you be sorry? It's not like my marriage to Stephen did you any good."
        scene ep11_jade_campus38 with dissolve
        mc "That's a weird thing to say. I'm sorry for your sake, of course. And for Sage..."
        scene ep11_jade_campus40 with dissolve
        ja "You do not talk to me about my daughter."
        scene ep11_jade_campus41 with dissolve
        mc "Well, she talks to me about you. Odd as it is, I happen to care."
        scene ep11_jade_campus42 with dissolve
        ja "Mhm. And in your talks with her, do you tell her about us?"
        ja "Do you tell her what you did to her mother? Do you tell her how many times we fucked?"
        scene ep11_jade_campus43 with dissolve
        mc "Uh... Of course not."
        scene ep11_jade_campus42 with dissolve
        ja "Exactly. Don't pretend it's fine for you to insert yourself in our family matters."
        scene ep11_jade_campus43 with dissolve
        mc "Whoa... This is not what I wanted to say to you."
        mc "I wanted to show you some comfort when I know you're hurting."
        scene ep11_jade_campus45 with dissolve
        ja "*{i}Scoffs{/i}*"
        scene ep11_jade_campus44 with dissolve
        mc "I know this is an odd situation to be in. But-"
        scene ep11_jade_campus45 with dissolve
        ja "You should leave. And stop caring about me."
        ja "I'm not yours to care about, nor will I be."
        scene ep11_jade_campus44 with dissolve
        
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Better for Jade path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        
        menu:
            "I want to care about you \n{size=-4}[m_c1][mod_choices[0]]":
                $ ep11_jade_care = True
                mc "But I want to care about you."
                mc "Despite things being weird, I don't regret everything I did."
                scene ep11_jade_campus46 with dissolve
                ja "What do you regret?"
                scene ep11_jade_campus44 with dissolve
                mc "As Dad would put it, I can't regret things that were out of my control, like Sage being your daughter."
                mc "But I wish I had known that before having sex with you."
                mc "Even so, I don't think it would have stopped me. But I'd have a different relationship with Sage today."
                mc "I've had a lot of fun with you. And I know it's selfish to say that I don't want that to stop, but I don't."
                scene ep11_jade_campus45 with dissolve
                ja "Look at us, [name]. There's no future for us."
                ja "I know this. You know this."
                ja "The sex we had was just that - sex."
                scene ep11_jade_campus46 with dissolve
                ja "I was deprived and needed someone to fuck me good. And that's all there was to it."
                scene ep11_jade_campus44 with dissolve
                mc "But what about the deep conversations we had? Didn't they mean anything to you?"
                scene ep11_jade_campus45 with dissolve
                ja "They sure as hell didn't mean I was looking to get something more from you."
                ja "And you must be out of your mind thinking anything different."
                scene ep11_jade_campus46 with dissolve
                ja "You're young. You'll find someone else to sleep with."
                ja "You're the least of my problems now."
                scene ep11_jade_campus44 with dissolve
                mc "I think you're wrong..."
                scene ep11_jade_campus47 with dissolve
                $ renpy.pause()
                $ new_bio("Jade", "I talked to Jade about her divorce, but she didn't want me to care about her anymore. I figured that was talk and tried to show her I still wanted to care.")
            "I hear you":
                $ ep11_jade_care = False
                mc "Ok, I hear you. If that's what you need me to do, you got it."
                scene ep11_jade_campus48 with dissolve
                $ renpy.pause()
                $ new_bio("Jade", "I talked to Jade about her divorce, but she didn't want me to care about her anymore.")
    else:
        scene ep11_jade_campus10 with dissolve
        if jade_state == 2 or jade_state == 3:
            mc "(I wonder if I'm part of why they're getting divorced... I can't be...right?)"
            mc "(If I could reverse time and undo things...everything I did with her would be undone.)"
        else:
            mc "(Poor thing...)"
        $ new_bio("Jade", "Jade seemed sad. I bet it had something to do with her divorce.")

label ep11_english_label:
$ guideSuggestedPage = 153
scene ep11_english1 with wipeleft
mc "Hey, Ashley? Got a moment?"
show ep11_english2
if not persistent.ep11_cardly8:
    show screen ep11_render_screen("ly8")
with dissolve
ash "What's up?"
show ep11_english3 with dissolve
mc "*{i}Sigh{/i}* You've put me in a bad spot with the DIKs with what you said to Derek."
mc "About what Anthony told you that I did."
show ep11_english4
hide screen ep11_render_screen
with dissolve
ash "Let's talk over here..."
scene ep11_english5 with dissolve
ash "Look, it's not my fault. I told Derek that in confidence."
ash "Listen, [name]... I don't want to talk about this. In fact, I don't want anyone to talk about this."
ash "I hate all the rumors and how people talk behind backs all the freaking time."
scene ep11_english6 with dissolve
mc "I'm the same as you; I hate it. And I get why you don't want to talk about it. You're worried that there's a tape circulating of you and Derek...doing things."
mc "But you gotta help me set things straight with the DIKs. We have to get to the bottom of this."
scene ep11_english5 with dissolve
ash "I can't."
scene ep11_english6 with dissolve
mc "Ashley... Please? I need your help. The DIKs need to know what happened."
mc "The frat is falling apart, and someone is sabotaging us. I'm worried there won't be anything left of us unless we get to the bottom of this now."
scene ep11_english7 with dissolve
ash "..."
scene ep11_english5 with dissolve
ash "What do you want to know?"
scene ep11_english6 with dissolve
mc "I want to know why the jocks think it was me who sent them some pictures."
scene ep11_english5 with dissolve
ash "I don't know why, but Ant and Chad said it was you."
scene ep11_english6 with dissolve
mc "Can we ask Anthony?"
scene ep11_english8 with dissolve
ash "No, don't do that."
scene ep11_english6 with dissolve
mc "Why not?"
scene ep11_english8 with dissolve
ash "Because he, out of all people... He can't know what I did with Derek... Ok?"
if ep7_hot_ashley_phase == 4:
    ash "Even if it was before I got together with Anthony, I don't want him to know about the sex tape."
else:
    ash "I don't want him to know about the potential sex tapes. Especially...because..."
    ash "*{i}Whispers{/i}* I slept with Derek while I was with Ant."
scene ep11_english6 with dissolve
mc "I understand. But trust me, I won't tell him any of that."
mc "I only want some answers and I know he has them."
scene ep11_english5 with dissolve
ash "What if he puts two and two together and figures out that you're asking because I told Derek about it?"
scene ep11_english9 with dissolve
$ renpy.pause()
scene ep11_english10 with dissolve
$ renpy.pause()
scene ep11_english11 with dissolve
mc "Call me crazy, but I don't think he will."
scene ep11_english6 with dissolve
mc "I'll be smooth about it, ok? I won't even mention Derek's name."
scene ep11_english12 with dissolve
mc "Anthony? There's something I need to ask you."
scene ep11_english13 with dissolve
an "Huh?"
scene ep11_english14 with dissolve
mc "I'm not looking to start something. I just want to talk."
scene ep11_english13 with dissolve
an "What is it?"
scene ep11_english14 with dissolve
mc "Why did you tell Ashley that I sent you guys pictures of DIKs having sex with Arieth?"
scene ep11_english13 with dissolve
an "Uh... I didn't say that."
scene ep11_english16 with dissolve
ash "You said he dropped off a letter addressed to Dawe, remember?"
scene ep11_english17 with dissolve
an "No, I said Chad said he did something like that. And that's why Chad beat him up and got suspended."
scene ep11_english14 with dissolve
mc "I didn't send you those pictures. I've got nothing to do with those pictures at all."
scene ep11_english15 with dissolve
an "That's what I told Chad. Those pictures are older than you."
scene ep11_english14 with dissolve
mc "Uh... They're not older than me; they are like a couple of years old or something."
scene ep11_english15 with dissolve
an "That's what I meant."
scene ep11_english14 with dissolve
mc "*{i}Sigh{/i}* Why does Chad think I sent them?"
scene ep11_english15 with dissolve
an "He had his reasons."
an "But it doesn't matter because it's still all DIKs on those pictures with Dawe's girl."
an "And you guys did that. You took those pictures and sent them to provoke us."
scene ep11_english14 with dissolve
mc "I won't argue that it's the DIKs in those pictures. But I'm unsure if the rest of what you said is true."
mc "And to be clear, {b}you{/b} - Anthony - don't know who sent them to you? You're just going off on what Chad said, right?"
scene ep11_english15 with dissolve
an "Dude, I've got no clue. You'd have to ask Chad."
scene ep11_english14 with dissolve
mc "Ok... Thanks. That was surprisingly helpful."
scene ep11_english18 with dissolve
ash "[name]..."
scene ep11_english5 with dissolve
ash "All these pictures, posters and sex tapes... What's going on with you guys?"
scene ep11_english6 with dissolve
mc "It's bad, Ashley. It's so bad. And I'm trying to fix it."
mc "But I can't fix it without finding out more information."
mc "If Chad thought it was me who sent him pictures... I understand why he jumped me during Hell Week, but some other things Chad said don't line up."
mc "I gotta talk to him."
scene ep11_english5 with dissolve
ash "Are you going to talk to Chad?"
scene ep11_english6 with dissolve
mc "Yeah... I have to."
$ new_bio("Ashley", "Ashley was worried that Anthony would find out that she had sex with Derek.")
$ new_bio("Ashley", "I talked to Ashley about the letters the jocks had received. She had misunderstood Anthony about who sent them.")
$ new_bio("Anthony", "I talked to Anthony about the letters the jocks had received. He told me he knew it wasn't me who sent them but that Chad blamed me.")
$ new_bio("Chad", "According to Anthony, Chad blamed me for sending letters to the jocks.")

scene ep11_english19 with dissolve
isa "*{i}Sigh{/i}*"
scene ep11_english21 with dissolve
de "What?"
scene ep11_english20 with dissolve
isa "Do I have to say it?"
scene ep11_english23 with dissolve
de "..."
scene ep11_english22 with dissolve
de "Aren't you teaching a class that's all about communication?"
scene ep11_english20 with dissolve
isa "Remove the hat. Stop being difficult. And I'm not even going to acknowledge your shirt."
scene ep11_english24 with dissolve
de "..."
$ guideSuggestedPage = 154
scene ep11_english25 with dissolve
cam "Saved you a seat."
scene ep11_english26 with dissolve
mc "That's the nicest thing someone's done for me today."
scene ep11_english27 with dissolve
cam "Bad day?"
scene ep11_english26 with dissolve
mc "Yeah, I don't know if you heard, and I don't want to talk about it."
scene ep11_english27 with dissolve
cam "I didn't hear, but it's fine. I'm not having the best day myself."
scene ep11_english28 with dissolve
mc "What's wrong?"
scene ep11_english29 with dissolve
cam "It was a long weekend. Usually, that's great, but after spending too many days back at home, I get restless."
cam "And when I got back here, Rio hadn't returned."
scene ep11_english30 with dissolve
cam "She was supposed to be back here yesterday but wasn't."
cam "She seems to be taking an extra long weekend."
scene ep11_english28 with dissolve
mc "You miss your friend, huh?"
scene ep11_english30 with dissolve
cam "It's lonely in my room... It's the weirdest thing..."
cam "I was forced to share a room here, but when I got it to myself, I didn't want it."
cam "It feels empty without her."
scene ep11_english28 with dissolve
mc "I can't relate; I love having my own room."
scene ep11_english31 with dissolve
cam "Of course you do. Your room is huge!"
cam "Need a roommate while Rio is gone?"
scene ep11_english28 with dissolve
if (branchAlone or branchSage) and not ep4_toldDerekAboutJade:
    menu:
        "[m_c1]My bed is big enough":
            $ ep11_cammy_draught = True
            mc "Sure, why not? My bed is big enough for both of us."
            if ep10_rolling:
                scene ep11_english30 with dissolve
                cam "Haha! I bet Lily would be mad."
                scene ep11_english28 with dissolve
                mc "Nah, she's cool with it."
                scene ep11_english31 with dissolve
                cam "Is that so?"
                scene ep11_english28 with dissolve
                mc "Yep."
                scene ep11_english31 with dissolve
                cam "Good to know."
                scene ep11_english29 with dissolve
                cam "Buuuut... I'd hate to wake up to the Walk of Shame."
            if branchSage:
                scene ep11_english30 with dissolve
                cam "Haha! I bet Sage would kill me."
                scene ep11_english28 with dissolve
                mc "She probably would."
                scene ep11_english31 with dissolve
                cam "But she was cool with me grinding you when we played Dots."
                scene ep11_english28 with dissolve
                mc "That was her idea, wasn't it!? I knew it!"
                scene ep11_english35 with dissolve
                cam "Hahaha!"
                scene ep11_english29 with dissolve
                cam "But I won't stay with you because I'd hate to wake up to the Walk of Shame."
            else:
                scene ep11_english29 with dissolve
                cam "Buuuut... I'd hate to wake up to the Walk of Shame."
            scene ep11_english28 with dissolve
            mc "Trust me, you're not alone in hating that..."
            scene ep11_english29 with dissolve
            cam "Don't you like it?"
            scene ep11_english28 with dissolve
            mc "I wasn't talking about me, but I think it's stupid. Let people have sex. Why bust their balls about it?"
            scene ep11_english31 with dissolve
            cam "Stop talking about sex..."
            scene ep11_english32 with dissolve
            mc "Haha, why?"
            scene ep11_english33 with dissolve
            cam "I'm going through a bit of a drought..."
            scene ep11_english34 with dissolve
            mc "You are?"
            scene ep11_english29 with dissolve
            cam "Yeah, it's frustrating."
            scene ep11_english34 with dissolve
            mc "Well, you got the room to yourself. Go nuts. Take care of yourself."
            scene ep11_english31 with dissolve
            cam "That's not the same thing now, is it?"
            scene ep11_english32 with dissolve
            mc "The feeling after is."
            scene ep11_english30 with dissolve
            cam "For you, maybe, but I prefer the real thing."
            scene ep11_english28 with dissolve
            mc "Oh, don't get me wrong... I prefer the real thing, too."
            if branchSage:
                scene ep11_english31 with dissolve
                cam "Ok, Sage would mind me talking sex with you. I'm gonna zip it."
                if ep9_sage_vanilla:
                    scene ep11_english28 with dissolve
                    mc "Yeah, let's."
                else:
                    scene ep11_english28 with dissolve
                    mc "It's just flirty talk. It doesn't mean anything if I talk about sex with you."
                    scene ep11_english31 with dissolve
                    cam "Well, I told you I was sexually frustrated, and you keep bringing it up. What do you think that does to me?"
                    scene ep11_english28 with dissolve
                    
                    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Better for Jade path)","(+Cheater)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if branchAlone:
                           $ mod_choices[6]="(Camila scene)"
                    
                    menu:
                        "I'll stop":
                            mc "You make a good point. I'll stop."
                        "Flirt more \n{size=-4}[m_c1][mod_choices[3]][m_c2][mod_choices[1]][m_c3][mod_choices[6]]":
                            $ ep11_camila_flirt = True
                            $ dk(1)
                            $ tc += 1
                            scene ep11_english32 with dissolve
                            if affinity == "DIK":
                                mc "Do you miss the feeling of a dick inside you? The moment it goes in there is the best, yeah?"
                            else:
                                mc "Tell me all about what it does to you. Spare me no details; I'd like to picture it."
                            scene ep11_english31 with dissolve
                            cam "You're bad."
            else:
                scene ep11_english31 with dissolve
                cam "It's the best."
                scene ep11_english28 with dissolve
                mc "What part of it is the best?"
                scene ep11_english30 with dissolve
                cam "All of it. The beginning, the middle and the end."
                scene ep11_english31 with dissolve
                cam "Fuck, now you made me think about it."
                scene ep11_english32 with dissolve
                
                if persistent.mod_wtenabled: 
                        $mod_choices = ["(Better for Jade path)","(Camila scene)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                
                menu:
                    "I'll stop":
                        mc "Yeah, I bet I did. I'll stop. I wouldn't want to ruin class for you."
                        scene ep11_english31 with dissolve
                        cam "Ruin it? This was way better."
                    "Flirt more \n{size=-4}[m_c1][mod_choices[1]]":
                        $ ep11_camila_flirt = True
                        mc "Yeah, me too."
                        scene ep11_english40 with dissolve
                        cam "You did not do that."
                        mc "Oh, sorry. I was looking for my pencil."
                        scene ep11_english41 with dissolve
                        cam "Yeah? Me too."
                        mc "Whoa, hey."
                        scene ep11_english37 with dissolve
                        cam "Two can play that game."
                        scene ep11_english38 with dissolve
                        mc "As we've established, two does make it better."
                        mc "But the funny thing is that I'm not as frustrated as you are. What you're doing will only make things worse for you."
                        scene ep11_english39 with dissolve
                        cam "Yup. You're right. Damn you."
                        scene ep11_english37 with dissolve
                        cam "You're bad."
            $ new_bio("Camila", "Camila told me she was sexually frustrated.")
        "Nope":
            if ep8_share_room:
                mc "Haha, no thanks. Derek's been staying with me a few times and that's enough."
            else:
                mc "Haha, nope."
else:
    if ep4_toldDerekAboutJade:
        mc "No, I'm good."
    elif ep8_share_room:
        mc "Haha, no thanks. Derek's been staying with me a few times and that's enough."
    else:
        mc "Haha, nope."
scene ep11_english33 with dissolve
if ep4_toldDerekAboutJade:
    cam "I get the feeling I'm annoying you. Maybe we should get some work done."
else:
    cam "We should get some work done."
$ guideSuggestedPage = 155
if minigames:
    stop music fadeout 3
scene ep11_english36 with dissolve
if ep4_toldDerekAboutJade:
    mc "It's not you... You just caught me on a bad day. Let's study."
else:
    mc "I'm so not in the mood for this today..."
$ new_bio("Riona", "Camila told me that Riona was sick.")
if minigames:
    play music "music/ep3/sing_along_with_jim.mp3"
    $ qM = quick_menu
    $ quick_menu = 0
    hide screen new_phone_screen
    $ renpy.block_rollback()
    jump init_eng_test_ep11_label

label after_eng_test_ep11_label:
hide screen word_cheat
if minigames:
    $ renpy.block_rollback()
    show screen new_phone_screen
    $ quick_menu = qM
    play music "music/ep2/journey_of_hope.mp3"
    queue music ["music/ep2/relaxing_ballad.mp3","music/ep2/simple_ballad.mp3","music/ep2/journey_of_hope.mp3"]

scene ep11_after_eng_test1 with fade
$ renpy.pause()
scene ep11_after_eng_test2 with dissolve
$ renpy.pause()
scene ep11_after_eng_test3 with dissolve
isa "Here's what I don't get... Somewhere, deep down inside, you are a good guy. I know it. You know it."
isa "Why can't you make my life easier in class?"
scene ep11_after_eng_test4 with dissolve
my "Listen to her."
scene ep11_after_eng_test7 with dissolve
de "I have a short attention span."
scene ep11_after_eng_test4 with dissolve
my "Nope. You know how to focus when you want to."
scene ep11_after_eng_test7 with dissolve
de "That's right! When I want to. I have a short attention span here."
play sound "sound_effects/interlude/page_turn.mp3"
scene ep11_after_eng_test12 with dissolve
isa "Looking at this... You've obviously paid some attention."
scene ep11_after_eng_test13 with dissolve
isa "Cathy was right about you. If you change your attitude, the sky is the limit for what you can achieve."
scene ep11_after_eng_test6 with dissolve
my "He does cheat a lot."
scene ep11_after_eng_test8 with dissolve
de "Hey! Don't tell the teacher I'm cheating."
scene ep11_after_eng_test5 with dissolve
my "She's not just our teacher, she's our friend. And you do cheat. I worry about how that will affect you."
scene ep11_after_eng_test13 with dissolve
isa "I don't see how he could have written this if he were cheating."
scene ep11_after_eng_test6 with dissolve
my "He is smarter than he thinks, but he chooses to cheat for some reason."
scene ep11_after_eng_test7 with dissolve
de "It's a learning tool. And I've changed. I'm all about mnemonics now."
scene ep11_after_eng_test14 with dissolve
isa "Mnemonics? How?"
scene ep11_after_eng_test7 with dissolve
de "If it's something I only want to learn on a surface level - you know, to shut teachers up? - I use different memory techniques."
de "There, I said it. It's not technically cheating, but it's not learning, either."
scene ep11_after_eng_test9 with dissolve
de "Can I recite the math formulas I need by looking at my hand and humming a song? Yes."
de "Do I actually know what the formulas do?"
scene ep11_after_eng_test7 with dissolve
de "Well... Yes, because I have to know when to use them, or they won't make sense."
scene ep11_after_eng_test10 with dissolve
de "But! Can I memorize and recite a useless page of this drivel you call learning material?"
de "Yes, that's what I did for the midterms. Full score, by the way."
scene ep11_after_eng_test9 with dissolve
de "But does that mean that I've learned something? I don't think so."
scene ep11_after_eng_test15 with dissolve
isa "..."
scene ep11_after_eng_test14 with dissolve
isa "Yep... You are a genius."
scene ep11_after_eng_test10 with dissolve
de "I'm not a genius! And I'm offended by that."
de "Would a genius light their fart on fire for laughs? Because I call that Friday."
scene ep11_after_eng_test14 with dissolve
isa "I'll make you a deal. For the rest of the semester, albeit short, I will stop bothering you about this drivel that I'm teaching you..."
isa "And, in return, you will at least act like you respect me and other students while we're in class."
scene ep11_after_eng_test11 with dissolve
de "That sounds like a sweet deal. I can do that."
scene ep11_after_eng_test6 with dissolve
my "You're not going to teach him anymore?"
scene ep11_after_eng_test16 with dissolve
if not ep11_camila_flirt:
    stop music fadeout 3
isa "I see it now. He doesn't need me. I believe he teaches himself more than I ever could."

if ep11_camila_flirt:
    scene ep11_after_eng_test17 with dissolve
    mc "What are you doing later?"
    scene ep11_after_eng_test18 with dissolve
    cam "I'm studying with Ashley, and then I'm off to yoga class."
    scene ep11_after_eng_test19 with dissolve
    mc "Do you do that often?"
    scene ep11_after_eng_test18 with dissolve
    cam "Yoga? Yeah, regularly."
    cam "Oh, that's right. You're doing it too."
    scene ep11_after_eng_test19 with dissolve
    mc "Nope. It was just the one time."
    scene ep11_after_eng_test20 with dissolve
    cam "You didn't enjoy it?"
    scene ep11_after_eng_test19 with dissolve
    mc "I...enjoyed the view."
    scene ep11_after_eng_test20 with dissolve
    cam "The view?"
    scene ep11_after_eng_test19 with dissolve
    mc "I was behind you, remember?"
    scene ep11_after_eng_test24 with dissolve
    cam "[name]..."
    scene ep11_after_eng_test19 with dissolve
    mc "Thanks for sitting with me in class. If you need help with your problem, you know where to find me."
    if branchSage and branchAlone:
        mc "You'd have to check with Sage first, though."
        scene ep11_after_eng_test21 with dissolve
        cam "Are you serious or just joking?"
        scene ep11_after_eng_test19 with dissolve
        mc "I was joking...but I'd be up for it."
        scene ep11_after_eng_test22 with dissolve
        cam "I...know a place. Wanna fuck?"
        scene ep11_after_eng_test23 with dissolve
        mc "Now!?"
        scene ep11_after_eng_test22 with dissolve
        cam "If we go quickly, I can make it to my next class."
        scene ep11_after_eng_test19 with dissolve
        stop music fadeout 3
        mc "Lead the way..."
        jump ep11_camila_lewd_label
    if branchSage and not branchAlone:
        mc "You'd have to check with Sage first, though."
        scene ep11_after_eng_test21 with dissolve
        cam "Yeah, right."
        scene ep11_after_eng_test19 with dissolve
        stop music fadeout 3
        mc "See you later."
    else:
        scene ep11_after_eng_test20 with dissolve
        cam "Are you serious or just joking?"
        scene ep11_after_eng_test19 with dissolve
        mc "I was joking...but I'd be up for it."
        scene ep11_after_eng_test22 with dissolve
        cam "I...know a place. Wanna fuck?"
        scene ep11_after_eng_test23 with dissolve
        mc "Now!?"
        scene ep11_after_eng_test22 with dissolve
        cam "If we go quickly, I can make it to my next class."
        scene ep11_after_eng_test19 with dissolve
        stop music fadeout 3
        mc "Lead the way..."
        jump ep11_camila_lewd_label
jump ep11_freeroam_room1_intro_label

label ep11_camila_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_camila == None:
        $ mc_camila = name
    else:
        $ mc_camila = persistent.mc_camila
    if persistent.camila == None:
        $ camila = "Camila"
    else:
        $ camila = persistent.camila
    $ ep6_genderMaya = False
    $ ep11_camila_came = False
play music "music/ep1/funk_rock.mp3"
hide screen new_phone_screen
$ ep11_camila_lewd = True
scene ep11_camila_lewd1 with dissolve
if ep6_genderMaya:
    mc "How did you find this place?"
    scene ep11_camila_lewd2 with dissolve
    cam "Sarah showed me. No one comes here, but the door is never locked for some reason."
else:
    mc "I know this place! Sarah once showed me this exit when we ducked out of Gender studies."
    scene ep11_camila_lewd2 with dissolve
    cam "Yeah, she's the one who showed me it too."
scene ep11_camila_lewd3 with dissolve
mc "You wanna do it here?"
scene ep11_camila_lewd5 with dissolve
cam "Yeah, trust me, it's safe."
scene ep11_camila_lewd4 with dissolve
mc "Hey, I'm up for it if you are."
scene ep11_camila_lewd5 with dissolve
cam "I'd take you back to my room, but then I'd have to wait until tonight..."
scene ep11_camila_lewd6 with dissolve
cam "...and considering you spent the better part of class fucking me with your eyes, I don't think I can."
scene ep11_camila_lewd7 with dissolve
cam "*{i}Smack{/i}*"
scene ep11_camila_lewd8 with dissolve
mc "Maybe if I don't give it to you now, you will be even wilder tonight?"
scene ep11_camila_lewd9 with dissolve
cam "Don't even think that thought."
scene ep11_camila_lewd10 with dissolve
mc "Haha! You're super horny, aren't you?"
scene ep11_camila_lewd11 with dissolve
cam "Do you think girls don't get horny or what?"
cam "Shut up and fuck me. I need to get it out of my system."
scene ep11_camila_lewd12 with dissolve
mc "I love to see you like this. It turns me on, too."
scene ep11_camila_lewd13 with dissolve
cam "Mhm..."
scene ep11_camila_lewd14 with dissolve
$ renpy.pause()
scene ep11_camila_lewd15 with dissolve
$ renpy.pause()
scene ep11_camila_lewd16 with dissolve
cam "I want you, [mc_camila]."
scene ep11_camila_lewd17 with dissolve
cam "Hngn... Fuck... You don't have to do that, we don't have time."
scene ep11_camila_lewd18 with dissolve
mc "You were sex deprived, no? I'm making sure you're properly taken care of."
scene anim_cam_cunn_ep11 with dissolve
mc "*{i}Lick lick{/i}*"
cam "*{i}Moans{/i}* Ok... Fuck it. I'll be late. Keep going."
pause
scene ep11_camila_lewd19 with dissolve
cam "That was so good... Now I wanna taste you."
scene ep11_camila_lewd20 with dissolve
mc "Go ahead."

scene anim_cam_bj1_ep11 with dissolve
cam "*{i}Suck glug glug{/i}*"
pause
scene anim_cam_bj2_ep11 with dissolve
pause
scene anim_cam_bj3_ep11 with dissolve
pause

$ tmpInt = 0
label ep11_camila_lewd_loop_label:
menu:
    "Cowgirl":
        $ tmpInt += 1
        scene anim_cam_ride1_ep11 with dissolve
        pause
        scene anim_cam_ride2_ep11 with dissolve
        pause
        if tmpInt > 2 and not ep11_camila_came:
            $ ep11_camila_came = True
            scene ep11_camila_lewd21 with vpunch
            cam "Ahhh..."
            scene ep11_camila_lewd21 with vpunch
            $ renpy.pause(0.5)
            scene ep11_camila_lewd21 with vpunch
            $ renpy.pause()
            scene ep11_camila_lewd22 with vpunch
            cam "*{i}Moans{/i}*"
            scene ep11_camila_lewd23 with dissolve
            cam "[mc_camila]... Hngn... I fucking came... You're so good at this."
            scene anim_cam_ride2_ep11 with dissolve
            cam "Give me more of it..."
            pause
        jump ep11_camila_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_cam_doggy1_ep11 with dissolve
        cam "Fuck me, [mc_camila]! Fuck me good..."
        pause
        scene anim_cam_doggy2_ep11 with dissolve
        cam "Hngn... God... I've missed sex so damned much..."
        pause
        jump ep11_camila_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_cam_doggy1_ep11 with dissolve
        mc "You're so tight..."
        cam "Yeah? You like that? Hngn..."
        mc "I love that!"
        pause
        scene anim_cam_doggy3_ep11 with dissolve
        mc "Your ass is so fucking sexy, like, you have no idea!"
        pause
        jump ep11_camila_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_cam_rev1_ep11 with dissolve
        cam "Remind me to thank Sarah for showing me this place later."
        mc "I'm not gonna think about Sarah while I'm fucking you."
        cam "Haha! Why not?"
        mc "Because I'm all about enjoying you, right now."
        pause
        scene anim_cam_rev2_ep11 with dissolve
        cam "Enjoy away... I'm doing that, too."
        pause
        jump ep11_camila_lewd_loop_label
    "Standing (Anal)":
        $ tmpInt += 1
        scene anim_cam_stand1_anal_ep11 with dissolve
        cam "Hnnn... Damn... How does it feel to have that big cock, [mc_camila]?"
        cam "Is it like walking around with a winning lottery ticket in your pants?"
        mc "Haha! I don't know how it feels not to have one, so I can't tell you."
        pause
        scene anim_cam_stand2_anal_ep11 with dissolve
        cam "Well, you are lucky to have it. Let me tell you that. Hnnn..."
        pause
        scene anim_cam_stand3_anal_ep11 with dissolve
        cam "*{i}Moans{/i}*"
        pause
        jump ep11_camila_lewd_loop_label
    "Facing her":
        $ tmpInt += 1
        scene anim_cam_stand1_ep11 with dissolve
        cam "Fuck me, [mc_camila]. Give it to me harder."
        pause
        scene anim_cam_stand2_ep11 with dissolve
        mc "Is this what you want?"
        cam "Mhm... Ever since you sexed me up in class this morning, I kept thinking of how much I wanted your cock inside me."
        pause
        scene anim_cam_stand3_ep11 with dissolve
        if ep11_camila_came:
            mc "Then take it."
        else:
            mc "Then take it. I wanna see you cum from it."
            cam "Let me ride you and I just might..."
        pause
        jump ep11_camila_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "Fuck... I'm gonna cum."
        cam "Don't get any cum on me! You gotta do it inside or aim somewhere else."
        menu:
            "In mouth":
                mc "Let me cum in your mouth, then."
                scene anim_cam_bj2_ep11 with dissolve
                cam "*{i}Suck suck{/i}*"
                mc "Yeah, that's it... I'm cumming!"
                scene ep11_camila_lewd24 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd24 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd24 at vpunch, cum1
                $ renpy.pause()
                scene ep11_camila_lewd25 with dissolve
                cam "Ahhh..."
                scene ep11_camila_lewd26 with dissolve
                cam "*{i}Gulp{/i}*"
                scene ep11_camila_lewd27 with dissolve
                cam "Fuck, that was more than a mouthful. Are you sure you're not sexually frustrated, too?"
            "Creampie":
                mc "I'll shoot it inside you."
                scene anim_cam_stand2_ep11 with dissolve
                mc "Almost there now... Fuck, I'm cumming!"
                scene ep11_camila_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd28 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd28 at vpunch, cum1
                $ renpy.pause()
                scene ep11_camila_lewd29 with dissolve
                cam "Fuck, that was more than it should be, right? Are you sure you're not sexually frustrated, too?"
            "Creampie (Anal)":
                mc "I'll shoot it inside your ass."
                scene anim_cam_stand2_anal_ep11 with dissolve
                mc "Almost there now... Fuck, I'm cumming!"
                scene ep11_camila_lewd30 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd30 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep11_camila_lewd30 at vpunch, cum1
                $ renpy.pause()
                scene ep11_camila_lewd31 with dissolve
                cam "Fuck, that was more than it should be, right? Are you sure you're not sexually frustrated, too?"

scene ep11_camila_lewd32 with dissolve
mc "If I were, I'm not anymore."
scene ep11_camila_lewd33 with dissolve
cam "Fuck... Thank you, [name]... That was exactly what I needed."
scene ep11_camila_lewd34 with dissolve
mc "Stop talking like I did you a favor. I enjoyed the hell out of it."
scene ep11_camila_lewd33 with dissolve
cam "No no. You did! I owe you one."
scene ep11_camila_lewd34 with dissolve
mc "Haha, if you insist."
scene ep11_camila_lewd35 with dissolve
cam "Let me know when I can return the favor, ok? Any time."
scene ep11_camila_lewd36 with dissolve
mc "It's gonna be an awkward math class later this week, then."
scene ep11_camila_lewd35 with dissolve
cam "Haha! Almost at any time."
scene ep11_camila_lewd37 with dissolve
cam "How does my hair look?"
scene ep11_camila_lewd38 with dissolve
mc "You might want to visit the restroom before class."
scene ep11_camila_lewd37 with dissolve
stop music fadeout 3
cam "I figured as much."

$ renpy.end_replay()
$ persistent.ep11_lewd_camila = True
$ calcScenes()
$ new_bio("Camila", "I helped Camila with her sexual frustration by having sex with her on campus after class.")
$ mphone_stats_add_girl_s3("camila","You had sex with Camila on campus in episode 11.")
show screen new_phone_screen
jump ep11_freeroam_room1_intro_label

label ep11_zoey_call_label:
$ guideSuggestedPage = 165
hide screen new_phone_screen
play sound "sound_effects/cellphone.mp3"
play music "music/ep_interlude/licensed_music/track99.mp3"
scene ep11_zoey_call16 with dissolve
"*{i}Phone rings{/i}*"
show ep11_zoey_call1
if not persistent.ep11_cardly9:
    show screen ep11_render_screen("ly9")
with dissolve
bre "BMI! How can I help you?"
show ep11_zoey_call17
hide screen ep11_render_screen
with dissolve
zo "Haha! Is that how you answer the phone?"
scene ep11_zoey_call2 with dissolve
bre "Zoey?"
scene ep11_zoey_call17 with dissolve
zo "It's me. How may I help you, Bret?"
scene ep11_zoey_call2 with dissolve
bre "Yeah, yeah. What's up?"
scene ep11_zoey_call18 with dissolve
zo "I'm not done mocking you. What's up with the BMI thing?"
scene ep11_zoey_call3 with dissolve
bre "You ought to know; you came up with it. Bret's Metal & Ink."
scene ep11_zoey_call18 with dissolve
zo "No way! What about Tattoos?"
scene ep11_zoey_call3 with dissolve
bre "It sucked ass."
scene ep11_zoey_call18 with dissolve
zo "Haha, it sure did! But dude, you can't answer the phone with BMI; say the whole thing."
scene ep11_zoey_call3 with dissolve
bre "Point taken. Why are you calling? Please, tell me you want to book a session."
scene ep11_zoey_call19 with dissolve
zo "You wish."
scene ep11_zoey_call4 with dissolve
jn "Is that Zoey!?"
scene ep11_zoey_call5 with dissolve
bre "It is!"
scene ep11_zoey_call9 with dissolve
jn "ZOEY!!! We fucking miss you!"

if emma_calm:
    scene ep11_zoey_call15 with dissolve
    em "Tell her I'll call her tonight!"
    scene ep11_zoey_call6 with dissolve
    bre "Emma says she'll call you later."
    scene ep11_zoey_call19 with dissolve
    zo "Awesome."
else:
    scene ep11_zoey_call19 with dissolve
    zo "Aw! I miss you guys too."
zo "How's business?"
scene ep11_zoey_call6 with dissolve
bre "I'll be honest... Not bad. Not bad at all."
bre "Things are starting to pick up."
bre "I'm considering hiring someone for the reception again. Are you interested?"
scene ep11_zoey_call19 with dissolve
zo "Is that your attempt to get me back there?"
scene ep11_zoey_call7 with dissolve
bre "It was worth a shot, but no, I'm being serious. Since the name change, we're seeing more customers."
bre "Emma has gotten more work. And the money flow is...great!"
scene ep11_zoey_call20 with dissolve
zo "I'm shocked. Who would have known that advertising Emma's services would be good for business?"
scene ep11_zoey_call7 with dissolve
bre "Haha, right? Let me know if you change your mind."
scene ep11_zoey_call20 with dissolve
zo "Believe me, you'd be the first one to know."
scene ep11_zoey_call7 with dissolve
bre "What about you? Everything good? Still happy being back there?"
scene ep11_zoey_call21 with dissolve
zo "I'm not on speaker, am I?"
scene ep11_zoey_call8 with dissolve
bre "No, you're good. What's wrong?"
scene ep11_zoey_call21 with dissolve
zo "[name] told me he loved me."
scene ep11_zoey_call10 with dissolve
bre "Oh... Damn... He's in love with you?"
scene ep11_zoey_call22 with dissolve
zo "Loved. Not loves. He said he thought of me as his ex-girlfriend and that I was his first love."
zo "And... I didn't know what the hell to tell him."
scene ep11_zoey_call10 with dissolve
bre "That's a tough one to be faced with... What did you end up saying?"
scene ep11_zoey_call22 with dissolve
zo "I said nothing. He stopped me before I could respond... Which was good because my thoughts were everywhere."
zo "It led me to think about you and Emma."
scene ep11_zoey_call10 with dissolve
bre "I see..."
if emma_calm:
    scene ep11_zoey_call23 with dissolve
    zo "And I know you can't talk loudly about it now."
else:
    scene ep11_zoey_call23 with dissolve
    zo "Is she there right now?"
    scene ep11_zoey_call10 with dissolve
    bre "Yeah."
    scene ep11_zoey_call23 with dissolve
    zo "Then I know you can't talk loudly about it."
zo "But I need your advice on this one."
scene ep11_zoey_call11 with dissolve
bre "Well... What do you feel? Have you figured it out?"
scene ep11_zoey_call23 with dissolve
zo "I think so."
scene ep11_zoey_call11 with dissolve
bre "And?"
scene ep11_zoey_call23 with dissolve
zo "He seems to have moved on, so why does it matter how I feel?"
scene ep11_zoey_call11 with dissolve
bre "It matters. Even if [name] has moved on, he talked to you about his feelings."
bre "To me, that doesn't sound like someone who's truly moved on."
scene ep11_zoey_call24 with dissolve
zo "Maybe he was trying to get some closure."
scene ep11_zoey_call25 with dissolve
bre "Maybe..."
bre "If you're gonna tell him you don't feel the same about him, maybe it's better if you let him know."
bre "It would hurt, but you wouldn't be stuck in his head as a \"what if?\"."
scene ep11_zoey_call24 with dissolve
zo "But what about... What if it's the opposite?"
scene ep11_zoey_call11 with dissolve
bre "You love him?"
scene ep11_zoey_call26 with dissolve
zo "*{i}Groans{/i}*"
scene ep11_zoey_call11 with dissolve
bre "Do you?"
scene ep11_zoey_call24 with dissolve
zo "I've never used the L word THAT way."
scene ep11_zoey_call25 with dissolve
bre "Then, what are your feelings?"
scene ep11_zoey_call24 with dissolve
zo "I'm not sure."
scene ep11_zoey_call25 with dissolve
bre "You said you had figured it out."
scene ep11_zoey_call26 with dissolve
zo "*{i}Sigh{/i}*"
scene ep11_zoey_call12 with dissolve
bre "If you're scared to say it to me, how will you be able to say it to him?"
scene ep11_zoey_call24 with dissolve
zo "I'm leaning toward not telling him anything. It's not like he has to know that I feel things too."
zo "I could keep it locked inside my head. At least, that's what I'm thinking."
scene ep11_zoey_call13 with dissolve
bre "I hate to break it to you, but you already let it out of your head by telling me about it."
bre "Do you want my advice or not?"
scene ep11_zoey_call23 with dissolve
zo "Yeah..."
scene ep11_zoey_call13 with dissolve
bre "Learn from my mistakes. Just tell him. Go for it. All fucking in."
bre "I have a feeling you will regret that you never did. Sometimes, you have to be selfish, too."
bre "Instead of thinking how he will react to it, think about how you would feel if you never told him."
bre "To me, regretting things you did is way better than regretting things you never did."
scene ep11_zoey_call23 with dissolve
zo "I figured you'd say something like that..."
scene ep11_zoey_call25 with dissolve
bre "And that's why you called. You wanted to hear it."
scene ep11_zoey_call24 with dissolve
zo "Maybe."
scene ep11_zoey_call14 with dissolve
bre "Good luck with it, Zoey. Call me if you need me, ok?"
scene ep11_zoey_call26 with dissolve
stop music fadeout 3
zo "*{i}Groans{/i}*"
scene ep11_zoey_call27 with dissolve
$ renpy.pause()

label ep11_chad_label:
show screen new_phone_screen
play music "music/ep11/licensed_music/track166.mp3"
scene ep11_chad1 with wipeleft
$ renpy.pause()
scene ep11_chad2 with dissolve
mc "Hey, thanks for coming."
scene ep11_chad3 with dissolve
ch "Make it quick."
scene ep11_chad4 with dissolve
mc "Out in the open like this?"
scene ep11_chad5 with dissolve
$ renpy.pause()
scene ep11_chad6 with dissolve
mc "I wanna know why you're telling your friends I sent you pictures."
scene ep11_chad7 with dissolve
ch "Look, you know what you did. It had to be you."
scene ep11_chad6 with dissolve
mc "I swear on my life, it wasn't me. What makes you so sure it was?"
scene ep11_chad8 with dissolve
ch "..."
mc "I remember you accusing me of blackmailing you... There must be a reason."
scene ep11_chad9 with dissolve
ch "I got a letter with a threat, and it was clear that you had sent it."
scene ep11_chad8 with dissolve
mc "A threat? Did it say it was from me?"
scene ep11_chad9 with dissolve
ch "No. But what was in it was something no one else would know."
scene ep11_chad8 with dissolve
mc "Huh? What would I know that nobody else does?"
scene ep11_chad9 with dissolve
ch "Quit your bullshit. You know what I'm talking about."
scene ep11_chad8 with dissolve
mc "I don't."
scene ep11_chad10 with dissolve
ch "..."
scene ep11_chad11 with dissolve
ch "It wasn't you?"
scene ep11_chad10 with dissolve
mc "I'm telling you, it wasn't me. I know we got off on the wrong foot, with Sage and all, but I would never blackmail you."
if affinity == "DIK":
    mc "Punch you in the face, sure. But blackmail? That's for pussies."
scene ep11_chad12 with dissolve
ch "Are you telling me it was someone else?"
play sound "sound_effects/thud.mp3"
scene ep11_chad13 with hpunch
ch "Fuck!"
scene ep11_chad14 with dissolve
mc "Chill... What was in the letter?"
scene ep11_chad15 with dissolve
ch "If you don't know, you don't need to know."
scene ep11_chad16 with dissolve
mc "I do because I'm also trying to find out who sent it. Someone is dragging me and my frat in the mud and causing stupid fights between you guys and us, and even among ourselves."
mc "It even got you kicked out of the tri-alphas! Don't you see how much damage it has caused?"
scene ep11_chad15 with dissolve
ch "There were pictures of DIKs banging Arieth. You guys aren't innocent."
scene ep11_chad16 with dissolve
mc "I'm not gonna lie and say those pictures don't exist because I know they do."
mc "But no one is admitting to sending them to you to provoke, and it sure as hell wasn't me."
scene ep11_chad17 with dissolve
mc "What was the threat?"
scene ep11_chad18 with dissolve
ch "Your five minutes are up."
scene ep11_chad19 with dissolve
mc "Was it about you and Troy?"
play sound "sound_effects/thud.mp3"
scene ep11_chad20 with hpunch
ch "It was you."
scene ep11_chad21 with dissolve
mc "No. I found that one out way later."
mc "You should be more careful in the gym locker room; I walked in on you two kissing."
scene ep11_chad22 with dissolve
ch "Who have you told?"
scene ep11_chad21 with dissolve
mc "I haven't told anyone about it."
scene ep11_chad22 with dissolve
ch "Liar!"
scene ep11_chad21 with dissolve
if not ep8_told_sage_chad_troy and not ep8_told_josy_chad:
    mc "I'm not lying. The moment I saw it, I realized a lot about you."
    scene ep11_chad23 with dissolve
    $ renpy.pause()
    scene ep11_chad25 with dissolve
elif ep8_told_sage_chad_troy:
    if ep8_told_josy_chad:
        mc "I told one friend of mine, and I know I can trust her not to tell anyone."
        mc "And...I had to let Sage know."
    else:
        mc "I had to let Sage know..."
    scene ep11_chad23 with dissolve
    $ renpy.pause()
    scene ep11_chad24 with dissolve
    ch "Sage knows?"
    scene ep11_chad25 with dissolve
    mc "And has known for quite a while."
    scene ep11_chad26 with dissolve
    $ renpy.pause()
    scene ep11_chad27 with dissolve
    ch "I had a feeling she knew something... So, that's why?"
    ch "She didn't tell me she knew... Why?"
    scene ep11_chad25 with dissolve
    mc "You hurt her a lot, breaking up with her like you did. You made her believe she did something wrong."
    mc "I told her because you refused to do it. She needed to hear it to move on."
    mc "And you didn't have the balls to be honest with her."
    scene ep11_chad26 with dissolve
    $ renpy.pause()
    scene ep11_chad25 with dissolve
    mc "And for her not to hold it against you or throw it in your face, that's the Sage I know."
    mc "She's worth more than the way you treated her."
    scene ep11_chad28 with dissolve
    ch "You're acting like I had a choice!"
    scene ep11_chad29 with dissolve
    mc "Of course, you had a choice. You chose to be with Sage and to cheat on her."
    scene ep11_chad28 with dissolve
    ch "You don't know what you're getting yourself into."
    ch "If you think this ends with Sage or who the hell is sending those letters, you're dead wrong."
    scene ep11_chad30 with dissolve
    mc "What do you mean?"
    scene ep11_chad31 with dissolve
    ch "You have no idea. Let it go. Just let all of it go."
    scene ep11_chad25 with dissolve
    mc "I can't do that. It's not just about you. I'm in this mess, too."
else:
    mc "I told one friend of mine, and I know I can trust her not to tell anyone."
    scene ep11_chad23 with dissolve
    $ renpy.pause()
    scene ep11_chad25 with dissolve

mc "Let me say that I get why you need to hide this from your friends. I would too, if the jocks were my friends."
scene ep11_chad24 with dissolve
ch "What will I have to do to keep you from telling them?"
scene ep11_chad25 with dissolve
if affinity == "DIK":
    mc "I meant it when I said blackmailing is for pussies. I'm not using this against you."
else:
    mc "Nothing. I didn't bring it up to use it against you."
mc "I brought it up because I had a hunch that it was involved, and it turned out I was right."
mc "All I want is to find out who's fucking us over - you and me both."
scene ep11_chad32 with dissolve
ch "I received two letters, ok? One was addressed to Dawe, and the other had my name written on it."
ch "Dawe's letter had pictures of DIKs banging Arieth."
scene ep11_chad33 with dissolve
ch "And it's not like that's any news. She's the rusty town bike that everyone rides."
ch "Dawe gets all naive and dismissive about her doing that behind his back. But he couldn't dodge this one."
scene ep11_chad25 with dissolve
mc "What about your letter?"
scene ep11_chad34 with dissolve
ch "It was a veiled threat saying, \"Is this what you're hiding?\"."
ch "And it included a picture of me with...you know... Again, in the locker room."
scene ep11_chad27 with dissolve
ch "Dawe caught you sneaking around in there while I was talking to Troy on the phone."
ch "That's why I thought you sent it. I figured you overheard and knew all about it and even took that photo of us."
ch "And since I treated you like shit for talking to Sage, it was your revenge."
ch "The content of Dawe's letter reinforced my suspicions that it was related to you and the DIKs."
scene ep11_chad25 with dissolve
mc "I heard the phone call, yeah. But I thought it was another girl you were talking to."
mc "You're not completely wrong, after all."
scene ep11_chad32 with dissolve
ch "Anyway... That's all I know."
scene ep11_chad35 with dissolve
mc "It helped clear some things out, for sure..."
mc "But who the hell sent those letters, and what do they gain from blackmailing you?"
scene ep11_chad32 with dissolve
ch "It beats me. And I'm fucking worried... Someone else knows, and from the looks of it, they aren't afraid to use that against me."
ch "All this time, the thought that it was you kept me cool because it felt like we had a non-verbal understanding."
ch "And now I know it was all in my head..."
ch "My best bet is that it's someone in your frat. Who else would have those pictures of Arieth other than you guys?"
scene ep11_chad35 with dissolve
mc "It could be, yeah. Those pictures exist on our laptop, and everything seems to point to that laptop - except for that picture you got. It's the first time I've heard of it."
mc "But I'm not completely sure one of us has been sending those letters."
mc "Did you see or hear about someone from your frat talking to one of us in private?"
scene ep11_chad32 with dissolve
ch "We hate you guys. There's not a chance in hell that would ever happen."
ch "Well...this is one hell of an exception."
ch "I can't vouch for you with my brothers and say you didn't send those letters."
scene ep11_chad35 with dissolve
mc "I get why, but that's not what I'm concerned about."
mc "Telling your friends anything about our talk would make them ask questions you couldn't answer. I understand that."
mc "And I can't clear my name either...because you'd deny it. I could try telling my brothers, but we have somewhat of a trust issue going on..."
scene ep11_chad36 with dissolve
ch "If it helps you clear it up with them, I'd settle for calling it a misunderstanding, but that I still blame them."
scene ep11_chad35 with dissolve
mc "I'm cool with that."
scene ep11_chad36 with dissolve
ch "Anything else?"
scene ep11_chad35 with dissolve
mc "Yes... This might be a long shot, but do you know why you guys didn't trash Nick's room when our mansion got wrecked?"
scene ep11_chad36 with dissolve
ch "I had nothing to do with that. I don't care and I wouldn't know."
scene ep11_chad35 with dissolve
mc "Can you find out? It might be a clue that you and I need."
scene ep11_chad36 with dissolve
ch "*{i}Sigh{/i}* I'll look into it. Let me know if you figure shit out."
scene ep11_chad35 with dissolve
mc "You too. Thanks for hearing me out."
show ep11_chad37
if not persistent.ep11_cardly10:
    show screen ep11_render_screen("ly10")
with dissolve
stop music fadeout 3
mc "(Fuck... I got some answers, but this was kind of a dead end...)"
$ new_bio("Chad", "Chad explained why he accused me of sending the letters to the jocks. He got mad when I told him it wasn't me. Someone blackmailed him for a reason I didn't understand.")

label ep11_lab_label:
play music "music/ep7/good_old_days.mp3"
queue music ["music/ep8/licensed_music/track67.mp3","music/ep8/licensed_music/track80.mp3","music/ep7/good_old_days.mp3"]
show ep11_lab1
hide screen ep11_render_screen
with wipeleft
li "You can't be serious!"
scene ep11_lab5 with dissolve
no "I have made myself perfectly clear on this. Eating in the lab is strictly forbidden."
no "I've warned you once before and now you leave me with no choice."
scene ep11_lab2 with dissolve
li "I have problems with my blood sugar! You're discriminating against my human rights."
scene ep11_lab5 with dissolve
no "You can take it up with the disciplinary committee. I won't have anyone in the lab who's jeopardizing their safety or that of others."
no "I am responsible for you when you are in class, and you have shown a blatant disregard by breaking the established rules."
scene ep11_lab3 with dissolve
li "For fuck's sake! It's just a bacon cheeseburger! I'm not drinking any chemicals!"
li "Show me a chemical or beaker that I could have mistaken for this burger."
scene ep11_lab6 with dissolve
no "Surfaces where you put your food could be contaminated, and then you'd ingest the potentially hazardous contaminants."
scene ep11_lab2 with dissolve
li "But I didn't put down the burger anywhere. I've had it in my pocket and hands this whole time."
scene ep11_lab6 with dissolve
no "This is not a debate, Linda. Please, leave my class."
scene ep11_lab4 with dissolve
li "Racist!"
scene ep11_lab7 with dissolve
no "What?"
scene ep11_lab8 with dissolve
stu "Um... Dr. Jenkins? She was my lab partner."
scene ep11_lab9 with dissolve
no "Join another pair of students for today."
scene ep11_lab12 with dissolve
sy "He can take Ron, and I'll do the lab on my own."
scene ep11_lab10 with dissolve
no "Sally, haven't we discussed this already? You're not going solo."
scene ep11_lab12 with dissolve
sy "But if he's changing pairs, I wanna do it too."
scene ep11_lab13 with dissolve
rn "Fine by me. Let's switch everything up!"
scene ep11_lab18 with dissolve
rn "Hey, wanna be my partner? I'm very smart."
rn "And not to brag, but..."
scene ep11_lab14 with dissolve
rn "This lab coat doesn't do justice to the muscles underneath it."
scene ep11_lab22 with dissolve
no "Derek! Are you seriously playing with the burner?"
de "No, ma'am..."
scene ep11_lab20 with dissolve
no "I'd hate to banish two students on the same day."
scene ep11_lab15 with dissolve
sy "Dr. Jenkins? Hello?"
scene ep11_lab11 with dissolve
no "Three would be even worse. Don't you think, Sally?"
no "This is taking up far too much time in class. This is what we'll do..."
scene ep11_lab17 with dissolve
no "You're with Ron."
scene ep11_lab10 with dissolve
no "Sally, you're with [name]."
scene ep11_lab16 with dissolve
sy "[name]? That's even worse!"
scene ep11_lab19 with dissolve
mc "Thanks..."
scene ep11_lab20 with dissolve
no "And Derek, you're with me."
scene ep11_lab23 with dissolve
de "With...you?"
scene ep11_lab20 with dissolve
no "That's your punishment. I don't think it's fair that your lab partner gets affected negatively by your antics."
scene ep11_lab23 with dissolve
de "Uh... Fine. But you better do half of the work. And the lab report isn't gonna write itself."
scene ep11_lab21 with dissolve
no "*{i}Mumbles{/i}* Maybe two banished students would be better..."
scene ep11_lab24 with dissolve
sy "Ugh... I can't believe this."
scene ep11_lab25 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Better for Jade path)","(Camila scene)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Be positive [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Hey, it's an improvement to me. With Derek, it was like I was working alone."
        scene ep11_lab26 with dissolve
    "Let's just focus":
        mc "Let's just focus on the experiment. I don't want to spend all day here."
        scene ep11_lab26 with dissolve
    "Dismiss Sally [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Yeah, I know. I got stuck with the dud."
        scene ep11_lab27 with dissolve
        sy "Screw you!"
sy "I hope you know what you're doing. I don't want to carry your weight."

scene ep11_lab25 with dissolve
if ep11_chem_status == 2:
    mc "I'm great at theory, and Nora said I did a great job in the lab before."
elif ep11_chem_status == 1:
    mc "I'm good at theory, and Nora said I did a decent job in the lab before."
else:
    mc "I'm better at theory than practical lab work."
scene ep11_lab26 with dissolve
sy "I don't need to hear your life story. Just work, ok?"

$ new_bio("Linda", "Nora banned Linda from the lab after she caught her eating multiple times.")
$ new_bio("Sally", "To Sally's dismay, Nora paired me with her in lab class after Linda was banned.")
if minigames:
    $ sm_init_mg(2)
    $ qM = quick_menu
    $ quick_menu = 0
    $ renpy.block_rollback()
    hide screen new_phone_screen
    $ science_jump_label = "science_game_end_ep11_label"
    scene science_minigame_neutral with dissolve
    jump sm_setup_experiment_ep11_label

    label science_game_end_ep11_label:
    $ renpy.block_rollback()
    $ quick_menu = qM
    hide screen wt_science_cheat2
    show screen new_phone_screen
    hide screen science_screen
    $ sm_play_stirrer_stop()
    scene ep11_after_lab1 with dissolve
else:
    scene ep11_after_lab1 with wipeleft
mc "And then, you decant it to the beaker."
scene ep11_after_lab2 with dissolve
sy "All of it?"
scene ep11_after_lab3 with dissolve
mc "No, just the supernate. Be careful so you don't get any precipitate with it."
scene ep11_after_lab2 with dissolve
sy "What's the supernate again?"
scene ep11_after_lab4 with dissolve
mc "Uh... The liquid on top of the precipitate at the bottom."
sy "Oh yeah. That."
scene ep11_after_lab5 with dissolve
mc "(She's struggling a lot in class... It's like the third time she has no clue what she's doing.)"
if ep10_dating_nora:
    scene ep11_after_lab6 with dissolve
    $ renpy.pause()
    if ep10_nora_encourage:
        scene ep11_after_lab9 with dissolve
    else:
        scene ep11_after_lab9b with dissolve
    $ renpy.pause()
    scene ep11_after_lab7 with dissolve
    $ renpy.pause()
    scene ep11_after_lab8 with dissolve
    de "Hey. Hey. I'm gonna need you to focus here."
$ guideSuggestedPage = 166
scene ep11_after_lab10 with dissolve
mc "Do you understand why we're doing this?"
scene ep11_after_lab11 with dissolve
sy "Um, duh! Because the experiment says so."
scene ep11_after_lab12 with dissolve
mc "Yeah, but I meant the theory of it."
scene ep11_after_lab13 with dissolve
sy "Yes! But I'm not gonna give you a lecture on it."
scene ep11_after_lab12 with dissolve
mc "Ok."
scene ep11_after_lab13 with dissolve
sy "But if you want to check if {b}you{/b} know why we're doing it, tell me why you think that is."
scene ep11_after_lab14 with dissolve
mc "(Smooth... Ok, I'll bite.)"
mc "We're performing a separation right now. Precipitation allows us to remove an unwanted compound from our solution."
mc "It won't be perfectly pure when we decant it like this, but it should be good enough for our purposes."
scene ep11_after_lab15 with dissolve
no "And how would you achieve a higher purity, [name]?"
scene ep11_after_lab16 with dissolve
mc "Oh..."
scene ep11_after_lab18 with dissolve
no "Go ahead."
scene ep11_after_lab17 with dissolve
mc "I assume there are many ways to do it."
scene ep11_after_lab18 with dissolve
no "Name one."
scene ep11_after_lab17 with dissolve
mc "Maybe pass it through a filter?"
scene ep11_after_lab18 with dissolve
no "Great. That could work."
no "Did you know there are tubes with built-in filters you can put in centrifuges?"
no "I can show you sometime if you're interested in methods of separation."
scene ep11_after_lab19 with dissolve
menu:
    "[m_c1]I want to learn more":
        $ ep11_scientist = True
        mc "Sure. I want to learn more about lab work; it's interesting."
        scene ep11_after_lab18 with dissolve
        no "I can tell."
        $ new_bio("Nora", "I told Nora I found lab work interesting and wanted to learn more about it.")
    "I'm not that interested":
        $ ep11_scientist = False
        mc "It's fine. Save your time for someone more interested in this."
        scene ep11_after_lab21 with dissolve
        sy "*{i}Mumbles{/i}* Haha... Burn."
        $ new_bio("Nora", "I told Nora I didn't find lab work interesting when she asked me if I wanted to learn more about it.")
scene ep11_after_lab20 with dissolve
no "Are you ready to assess the purity?"
scene ep11_after_lab22 with dissolve
sy "Yeah, I'm finishing up here."
scene ep11_after_lab23 with dissolve
sy "By the way, I already knew what you told me."
scene ep11_after_lab24 with dissolve
mc "Awesome! Then you can write about it in the lab report, and I'll write about our calculations."
scene ep11_after_lab25 with dissolve
mc "Turn off the burner when you're done."
sy "Uh... Um..."
scene ep11_after_lab26 with dissolve
no "Let's see what you've achieved today..."
scene ep11_after_lab27 with dissolve
sy "It was mostly me. [name] didn't do a lot."
scene ep11_after_lab28 with dissolve
mc "(Wow... That's not true at all... I should say something.)"
scene ep11_after_lab29 with dissolve
no "That's odd. That's not what I observed."
scene ep11_after_lab30 with dissolve
mc "(Never mind.)"
if (minigames and sm_purity == 0) or (not minigames and affinity == "DIK"):
    scene ep11_after_lab33 with dissolve
    no "Either or... This doesn't seem right. The purity is way off. You must have done something wrong."
    scene ep11_after_lab35 with dissolve
    sy "Dammit, [name]!"
    scene ep11_after_lab31 with dissolve
    mc "Hey, you said it yourself... You did most of the work."
else:
    if minigames:
        if sm_purity <= 50:
            scene ep11_after_lab33 with dissolve
            no "Either or... This isn't good. The purity is off. You must have done something wrong."
            scene ep11_after_lab35 with dissolve
            sy "Dammit, [name]!"
            scene ep11_after_lab31 with dissolve
            mc "Hey, you said it yourself... You did most of the work."
        else:
            if sm_purity < 75:
                scene ep11_after_lab34 with dissolve
                no "[sm_purity]%% pure. That's a solid effort. Well done."
                scene ep11_after_lab35 with dissolve
                sy "Not higher? What the hell did you do to it?"
                scene ep11_after_lab31 with dissolve
                mc "Me? I thought you said you did most of the work."
                scene ep11_after_lab34 with dissolve
                no "Please don't be upset; it's a good result. Lab work takes a lot of practice."
                $ ep11_chem_status += 1
            else:
                scene ep11_after_lab34 with dissolve
                if ep11_chem_status == 2:
                    no "You've done it again, [name]. I am impressed. It's [sm_purity]%% pure."
                else:
                    no "I am impressed. It's [sm_purity]%% pure."
                no "I think you two work well together."
                scene ep11_after_lab36 with dissolve
                sy "I wouldn't go that far."
                scene ep11_after_lab32 with dissolve
                mc "You did well, Sally."
                $ ep11_chem_status += 2
                if not persistent.ep11_cardmy12:
                    $ persistent.chat_new_rewards = True
                    $ persistent.rew_maya_unlocked += 1
                    $ persistent.ep11_cardmy12 = True
                    $ calcRenders()
                    show screen srmsg
                    $ renpy.pause(3)
                    hide screen srmsg
    else:
        scene ep11_after_lab34 with dissolve
        no "You should be proud. This is a very good result. It's the best I've seen today."
        scene ep11_after_lab32 with dissolve
        mc "You did well, Sally."

scene ep11_after_lab34 with dissolve
no "Clean up your desk, and then you're free to leave."
scene ep11_after_lab37 with dissolve
sy "When do you want to do it?"
if affinity == "DIK":
    scene ep11_after_lab38 with dissolve
    mc "I'm not interested in doing you, but thanks for asking."
    scene ep11_after_lab40 with dissolve
    sy "The lab report, stupid!"
    scene ep11_after_lab39 with dissolve
else:
    scene ep11_after_lab39 with dissolve
mc "We can split the lab report in two and write the parts on our own. Choose if you want to write the theory or about the results and calculations."
scene ep11_after_lab41 with dissolve
sy "No, I want to write it together."
scene ep11_after_lab42 with dissolve
mc "Do we have to? It will be faster if we work on our own."
scene ep11_after_lab43 with dissolve
sy "Hell no. I don't wanna have to double-check whatever you wrote."
stop music fadeout 3
scene ep11_after_lab42 with dissolve
mc "Fine... We'll write it together. Let me know when you have time for it."
$ mphone_contact_list.insert(-3,["Sally","NONE",False])
$ mphone_chat_history_list.insert(-3,["Sally",0,[],[]," ",0])
$ new_bio("Sally", "Sally tried to take full credit for the work we did together in lab class.")

if jade_state == 0:
    jump ep11_josy_hobby_label

label ep11_ds_talk_label:
play music "music/ep9/passing_time.mp3"
scene ep11_ds_talk1 with wipeleft
mc "Hey, what are you up to?"
scene ep11_ds_talk2 with dissolve
de "I'm trying out new holiday drink recipes."
scene ep11_ds_talk3 with dissolve
mc "If you only took lab class this seriously..."
scene ep11_ds_talk4 with dissolve
de "That's one chunky eggnog... It's like drinking custard. What the fuck happened?"
scene ep11_ds_talk5 with dissolve
de "Dammit... The milk is expired. That's why..."
play sound "sound_effects/bottle_pour.mp3"
scene ep11_ds_talk6 with dissolve
mc "What's that bottle for?"
scene ep11_ds_talk7 with dissolve
de "I mix a lot of drinks in here. The failed ones go into it. During parties, I empty cups and glasses into it, too."
de "I know the bathroom is next door, but it's simpler going once than a lot, especially during parties when it's occupied."
if ep9_sally_drink:
    scene ep11_ds_talk8 with dissolve
    mc "It's safe to drink from, yeah?"
    scene ep11_ds_talk9 with dissolve
    de "It's a mix of spit and all kinds of alcohol, [name]... Don't drink out of it. Ever."
else:
    scene ep11_ds_talk8 with dissolve
    mc "That's one nasty bottle."
    scene ep11_ds_talk9 with dissolve
    de "Yeah. It's a mix of spit and all kinds of alcohol. Don't drink out of it. Ever."
scene ep11_ds_talk10 with dissolve
mc "Do you have a moment to talk? I need your advice."
scene ep11_ds_talk11 with dissolve
de "I don't know if I can help, but I'm all ears."
scene ep11_ds_talk12 with dissolve
mc "I'm in a bit of a predicament and don't know what to do."
scene ep11_ds_talk13 with dissolve
de "You are? What did you do?"
scene ep11_ds_talk12 with dissolve
mc "This has to stay between us, ok? I have no one else I can talk to about this."
scene ep11_ds_talk14 with dissolve
de "Trust me. Whatever you say will stay between us. The bro code, remember?"
scene ep11_ds_talk12 with dissolve
mc "And I don't want you to joke about this with me, either."
scene ep11_ds_talk13 with dissolve
de "I'll be serious. What's on your mind?"
scene ep11_ds_talk12 with dissolve
mc "It's about Sage...and Jade."
if ep4_toldDerekAboutJade:
    scene ep11_ds_talk15 with dissolve
    de "It's time for this talk, huh? I'm not gonna lie; I've been expecting it to happen sooner or later."
else:
    scene ep11_ds_talk15 with dissolve
    de "What about them?"
    scene ep11_ds_talk16 with dissolve
    mc "Remember what I told you about Jade? What she did to me in class."
    scene ep11_ds_talk15 with dissolve
    de "The handjob? Yeah..."
scene ep11_ds_talk16 with dissolve
if ep4_toldDerekAboutJade:
    mc "Jade and Stephen are getting divorced, and Jade told me it's my fault..."
    scene ep11_ds_talk15 with dissolve
    de "How is it your fault?"
    scene ep11_ds_talk16 with dissolve
    mc "That video I showed everyone at the Hell Week evaluation... Someone sent it to Stephen, and he confronted Jade about it."
    scene ep11_ds_talk18 with dissolve
    de "What!? How the fuck did that happen?"
    scene ep11_ds_talk16 with dissolve
    mc "Once again, that laptop is in the center of it unless someone somehow got a hold of my phone."
    scene ep11_ds_talk18 with dissolve
    de "Oh my fucking God... What's gonna happen?"
    scene ep11_ds_talk16 with dissolve
    mc "Stephen is using that video as leverage in their divorce. He's making Jade settle for next to nothing."
    mc "And Jade was mad as hell at me for leaking the video after I promised her I'd delete it."
    mc "She blamed me and told me I'd get what was coming to me one day."
    scene ep11_ds_talk17 with dissolve
    mc "And now, I have no clue what to do."
    if branchSage:
        mc "Sage is my girlfriend, and I'm the reason for her parents' divorce. I..."
        mc "I don't want to lose her, so I haven't told her anything. She'd leave me in a heartbeat, wouldn't she?"
    else:
        mc "Sage is my close friend, and I'm the reason for her parents' divorce. I..."
        mc "If I mention this to her, I'll ruin our friendship. I don't want to lose her."
    scene ep11_ds_talk16 with dissolve
    mc "What do I do? I need your help."
else:
    if ep3_acceptedJade and not ep4_fuckedJade:
        mc "Yeah, exactly... That."
    elif ep4_fuckedJade and ep6_reject_jade:
        mc "It didn't end there. I met up with Jade one night to have lots of sex."
    elif jade_state == 1:
        if ep11_jade_care:
            mc "It didn't end there. We've been fucking since, but she wanted to end it recently. We've had sex on numerous occasions."
        else:
            mc "It didn't end there. We've been fucking since, but she ended it recently. We've had sex on numerous occasions."
    elif jade_state == 2:
        mc "It didn't end there. We've had sex on numerous occasions before I ended our sexual relationship."
    mc "And now Jade and Stephen are getting divorced."
    mc "I'm unsure if I am part of why they are getting divorced, but my biggest concern is how this affects Sage."
    scene ep11_ds_talk17 with dissolve
    if branchSage:
        mc "I mean, Sage is my girlfriend, and I did that with her mom."
        mc "I don't want to lose her, and that's why I haven't said anything about this to her."
        mc "She'd leave me in a heartbeat, wouldn't she?"
    else:
        mc "I mean, Sage is my close friend, and I did that with her mom."
        mc "If I mention this to her, I'll ruin our friendship and I don't want to lose her."
    if not (ep3_acceptedJade and not ep4_fuckedJade):
        scene ep11_ds_talk15 with dissolve
        de "Wow... I uh... I don't know what to say."
        scene ep11_ds_talk16 with dissolve
    mc "What do I do? I need your help."

scene ep11_ds_talk17 with dissolve
$ renpy.pause()
scene ep11_ds_talk19 with dissolve
de "It's one hell of a situation..."
scene ep11_ds_talk16 with dissolve
mc "I didn't know Sage was Jade's daughter."
scene ep11_ds_talk19 with dissolve
de "Ignorance or not, I can't see any scenario where Sage would be happy about it."
if branchSage:
    de "It's one thing if you're friends with Sage, but if you're a couple...that's another level of problems for you."
else:
    de "Even if you're just friends with Sage... Shit... I'd be pissed if it were my mom."
scene ep11_ds_talk15 with dissolve
de "You have to look at your options. Weigh them against each other, and there's your answer."
scene ep11_ds_talk16 with dissolve
mc "What are my options? Please tell me if you can see an option that I can't."
scene ep11_ds_talk15 with dissolve
de "First off, don't be too hard on yourself. What you did to Sage was unknowingly, yeah?"
if jade_state == 1:
    scene ep11_ds_talk16 with dissolve
    mc "Yeah. As you know, I found out before Halloween that they were family."
    mc "But honestly, the sex with Jade is amazing - I love it. Even though I know the sensible choice is to stop."
    if ep4_toldDerekAboutJade:
        mc "Well... She might have put an end to it now either way."
    scene ep11_ds_talk19 with dissolve
    de "Ok... Hm..."
else:
    scene ep11_ds_talk16 with dissolve
    mc "Yes, it was. As you know, I found out before Halloween that they were family."

scene ep11_ds_talk20 with dissolve
de "It didn't help that you kept it a secret when you found out. The time between finding out they're family and telling Sage about it is pretty long."
de "Sorry, but that makes the situation even worse."
scene ep11_ds_talk16 with dissolve
mc "I didn't want to tell Sage. I thought I could keep it a secret, but I question whether it's the right way."
scene ep11_ds_talk21 with dissolve
de "That's your conscience speaking. Bad decisions don't always make you a bad guy. I'd worry more about you if you didn't feel any guilt."
scene ep11_ds_talk16 with dissolve
mc "What are my options here? Help me..."
scene ep11_ds_talk21 with dissolve
de "Well, option one is what you've been doing so far. Staying silent about it."
de "Aside from this talk between us, take this secret to the grave."
if ep4_toldDerekAboutJade:
    de "But I'm not gonna lie, that sex tape of yours leaking to her husband worries me... Someone else saw it and sent it to Professor Burke to fuck you over."
scene ep11_ds_talk16 with dissolve
mc "What about the guilt I feel?"
scene ep11_ds_talk21 with dissolve
de "Pray that it will go away. Learn to live with it. What more can I say?"
de "And if the guilt is too much, you have option two. Sit down with Sage and tell her everything."
de "Maybe not in detail, but tell her what she needs to know - what you did and why you did it. And also why it took you all this time to tell her."
scene ep11_ds_talk15 with dissolve
de "That may help you get rid of the guilt, but it won't be pretty."
de "Let me ask you this... What does Sage mean to you?"
if branchSage:
    de "Is she someone you think you'll be in a long-term relationship with or not?"
    if tc > 4:
        jump ep11_sage_stance_label
    scene ep11_ds_talk16 with dissolve
    menu:
        "Long-term":
            $ ep11_sage_stance = 1
            mc "I want it to be long-term. I've got feelings for her. I care about her deeply."
            scene ep11_ds_talk15 with dissolve
            de "Fuck... It has reached that point, huh?"
            $ new_bio("Sage", "I told Derek that I thought my relationship with Sage would be long-term.")
        "Short-term":
            $ ep11_sage_stance = 2
            mc "I think it will be short-term. Jade put aside, Sage is graduating, and I'm not sure if it's realistic to expect our relationship to last past graduation."
            mc "But I care deeply about her."
            scene ep11_ds_talk15 with dissolve
            de "I see. It sounds like you're aware of your future challenges when you put it like that."
            $ new_bio("Sage", "I told Derek that I thought my relationship with Sage would be short-term.")
        "I don't know":
            label ep11_sage_stance_label:
            $ ep11_sage_stance = 3
            mc "I don't know. I haven't been able to think about that. I've focused on getting to know her."
            mc "But I can't predict the future, especially not with these problems hanging over us."
            scene ep11_ds_talk21 with dissolve
            de "I hear that this problem is taking too much focus and affecting your relationship even when you're being passive."
            $ new_bio("Sage", "I told Derek I didn't know what kind of a relationship I would have with Sage in the future.")
else:
    scene ep11_ds_talk16 with dissolve
    mc "She's a great friend of mine. I like her so much."
    mc "But...she's graduating next year, and I'm unsure if expecting our friendship to last past graduation is realistic."
    mc "It certainly will be different... I care a lot about her. She's a wonderful person. I want to think I'd still be in her life somehow."

scene ep11_ds_talk21 with dissolve
de "I can't make this choice for you. You gotta make it yourself. But I'm with you, whatever that choice is."
if jade_state == 1:
    de "I know you didn't do it on purpose - at least at first - but there's no malice behind your actions."
else:
    de "I know you didn't do it on purpose and there's no malice behind your actions."
scene ep11_ds_talk17 with dissolve
mc "If you were me, what would you do?"
scene ep11_ds_talk15 with dissolve
de "Are you sure you want to know?"
scene ep11_ds_talk16 with dissolve
mc "Yes."
if branchSage:
    scene ep11_ds_talk22 with dissolve
    de "I'd go with option three."
    scene ep11_ds_talk23 with dissolve
    mc "You only gave me two options."
    scene ep11_ds_talk22 with dissolve
    de "Because I think you'd punch me if I told you what it was."
    scene ep11_ds_talk23 with dissolve
    mc "If it's something like keep doing stuff to both of them, I would."
    scene ep11_ds_talk24 with dissolve
    de "Is that what you think of me?"
    scene ep11_ds_talk23 with dissolve
    mc "It's not?"
    scene ep11_ds_talk24 with dissolve
    de "No, I'm being serious here."
    scene ep11_ds_talk23 with dissolve
    mc "What's option three?"
    scene ep11_ds_talk22 with dissolve
    de "You're not gonna like it."
    scene ep11_ds_talk23 with dissolve
    mc "Tell me what it is."
    scene ep11_ds_talk22 with dissolve
    de "I'd break up with Sage."
    scene ep11_ds_talk23 with dissolve
    mc "..."
    mc "You would break up with her?"
    if ep3_acceptedJade and not ep4_fuckedJade:
        mc "Over a handjob from her mom in class?"
        mc "Ok, I hear it when I say it out loud like that... But..."
    scene ep11_ds_talk25 with dissolve
    de "This is me talking, ok? I'm not trying to influence you."
    de "But if it were me, that's the best option by deduction."
    scene ep11_ds_talk22 with dissolve
    de "With option two, if I told her what I did, I don't think she would forgive me, and the relationship would end anyway."
    de "She'd go on to hate me and maybe even her mom. And I would hate myself for doing that to her."
    scene ep11_ds_talk24 with dissolve
    de "On the other hand, with option one, if I never told her, I'd feel like you do now. Ridden with guilt."
    de "Now, I can carry a lot, but I couldn't carry that burden. No matter how much I liked the girl."
    de "And as we've established, the problem and guilt grow with time. The lie will never go away if you bury it. No matter how much time passes."
    if ep4_toldDerekAboutJade:
        de "And there's always the uncertainty about Jade telling her at some point, or that the tape leaks even further. That dials the worry up to eleven."
    else:
        de "And there's always the uncertainty about Jade telling her at some point. That dials the worry up to eleven."
    scene ep11_ds_talk25 with dissolve
    de "But with option three..."
    de "Sure, you're still lying to her, and she'll get hurt from the breakup. But at least you didn't ruin her mom for her."
    scene ep11_ds_talk22 with dissolve
    de "And from the sounds of it, Jade didn't know jumping you would affect her relationship with her daughter."
    de "Neither option is fair to everyone. You'd still have some remorse, but I think you'd feel relieved knowing you did what you could and salvaged Sage's relationship with her mom."
    scene ep11_ds_talk23 with dissolve
    mc "..."
    mc "I don't want to break up with her."
    scene ep11_ds_talk22 with dissolve
    de "It's a shit choice to make. But if you think Sage would forgive you and still have a relationship with you after telling her what you did with her mom..."
    de "I'm not an expert on women, but I think the odds are slim at best."
    scene ep11_ds_talk23 with dissolve
    mc "That's a shit option! I'm not breaking up with her."
    scene ep11_ds_talk26 with dissolve
    de "..."
    stop music fadeout 3
    mc "I'm not."
    scene ep11_ds_talk27 with dissolve
    $ renpy.pause()
else:
    scene ep11_ds_talk20 with dissolve
    de "I'm torn."
    de "With option two, if I told her, I'd be ruining her mom for her and potentially even our friendship."
    de "She'd go on to possibly hate me and maybe even her mom."
    scene ep11_ds_talk21 with dissolve
    de "On the other hand, with option one, if I never told her, I'd feel like you do now. Ridden with guilt."
    de "Now, I can carry a lot, but I couldn't carry that burden."
    de "If I valued the friendship highly, the guilt would be even worse."
    scene ep11_ds_talk15 with dissolve
    de "And as we've established, the problem and guilt grow with time. The lie will never go away if you bury it. No matter how much time passes."
    if ep4_toldDerekAboutJade:
        de "And there's always the uncertainty about Jade telling her at some point, or that the tape leaks even further. That dials the worry up to eleven."
    else:
        de "And there's always the uncertainty about Jade telling her at some point. That dials the worry up to eleven."
    scene ep11_ds_talk22 with dissolve
    de "I'd go with option three."
    scene ep11_ds_talk23 with dissolve
    mc "What's option three?"
    scene ep11_ds_talk22 with dissolve
    de "I'd distance myself from Sage as much as I could and try to be less of a friend to her."
    scene ep11_ds_talk23 with dissolve
    mc "You'd stop being her friend?"
    scene ep11_ds_talk25 with dissolve
    de "This is me talking, ok? I'm not trying to influence you."
    de "With this option, you'd still be lying to her. And while your friendship would slowly fade away, at least you wouldn't ruin her mom for her."
    scene ep11_ds_talk22 with dissolve
    de "And from the sounds of it, Jade didn't jump you with the intention of affecting her relationship with her daughter."
    de "Neither option is fair to everyone. You'd still have some remorse, but I also think you'd feel relief knowing you did what you could and salvaged Sage's relationship to her mom."
    scene ep11_ds_talk23 with dissolve
    mc "..."
    mc "That's such a bad option... I don't want to stop being her friend."
    scene ep11_ds_talk22 with dissolve
    de "It's a shit choice to make. But if you think Sage would forgive you after telling her what you did with her mom..."
    de "I'm not an expert on women, but I think the odds are slim at best."
    scene ep11_ds_talk23 with dissolve
    mc "I'm not gonna stop being her friend."
    scene ep11_ds_talk26 with dissolve
    de "..."
    stop music fadeout 3
    mc "I'm not."
    scene ep11_ds_talk27 with dissolve
    $ renpy.pause()

$ new_bio("Derek", "Derek advised me on what to do about the situation with Jade and Sage. I didn't like his reasoning, but I didn't have a better solution for my problem either.")

label ep11_josy_hobby_label:
hide screen new_phone_screen
play music "music/ep8/licensed_music/track72.mp3"
scene ep11_josy_hobby5 with wiperight
he "What is this all about?"
scene ep11_josy_hobby1 with dissolve
he "Are you opening a clothing store in our room?"
scene ep11_josy_hobby2 with dissolve
js "I'm sorry for spreading it all over the place. I'm trying to get organized."
scene ep11_josy_hobby5 with dissolve
he "Those are a lot of nice new clothes."
scene ep11_josy_hobby3 with dissolve
js "Thank you. I'm trying something new. And, no, it's not a clothing store."
scene ep11_josy_hobby6 with dissolve
he "Then what is it?"
scene ep11_josy_hobby3 with dissolve
js "I'm embarrassed to say."
scene ep11_josy_hobby6 with dissolve
he "How so?"
scene ep11_josy_hobby4 with dissolve
js "Because it's new and I'm unsure if it's for me yet."
js "But I feel excited about it and think I would be good at it."
scene ep11_josy_hobby7 with dissolve
he "New clothes... You're doing something with them... Uh... Are you selling them?"
scene ep11_josy_hobby3 with dissolve
js "I told you I wasn't opening a store."
scene ep11_josy_hobby7 with dissolve
he "I meant online. Are you flipping clothes for profit?"
scene ep11_josy_hobby4 with dissolve
js "No, I'm keeping these for myself."
scene ep11_josy_hobby6 with dissolve
he "We could do this guessing game all day, or you could just tell me."
he "Living in the same room together, I'll find out eventually unless you plan on sneaking around."
scene ep11_josy_hobby3 with dissolve
js "I've started a blog on CB, ok?"
scene ep11_josy_hobby7 with dissolve
he "Oh? You have?"
scene ep11_josy_hobby3 with dissolve
js "It's nothing much yet, but I've gained a few hundred followers in a short time."
scene ep11_josy_hobby6 with dissolve
he "Why would you be embarrassed about that? That sounds cool."
he "The big bloggers on there make a ton of cash each month from sponsorships and whatnot."
scene ep11_josy_hobby8 with dissolve
js "I know. But it's not about the money for me. It's...hm..."
js "Do you ever feel like you're lost?"
scene ep11_josy_hobby9 with dissolve
he "Lost how?"
scene ep11_josy_hobby13 with dissolve
js "Like, if you don't know what the hell you're doing with everything."
scene ep11_josy_hobby10 with dissolve
he "I've second-guessed myself a lot over the years. Are my studies right and what the hell am I doing with Tommy?"
he "Uh... Maybe I shouldn't have said that to you."
scene ep11_josy_hobby14 with dissolve
js "It's fine. But that's what I'm talking about."
js "I feel that way with everything right now. And that's when I came up with the idea of the blog."
js "Most bloggers you see on CB, with tens of thousands of followers, seem to know what they are doing."
scene ep11_josy_hobby13 with dissolve
js "They live these bizarre lives that feel so far out of reach."
js "I can't relate to them at all. So, I thought, what if I become a blogger that people like me can relate to?"
js "A blog about not having a clue and trying to figure yourself out."
scene ep11_josy_hobby11 with dissolve
he "It sounds interesting. What do you write about?"
scene ep11_josy_hobby14 with dissolve
js "It's an ordinary blog about all those topics, and by interacting with followers, it can turn into a community where similar-minded people can get together and be reassured."
js "And hopefully, even figure themselves out with the help of others."
scene ep11_josy_hobby10 with dissolve
he "And where do the clothes fit in all of this?"
scene ep11_josy_hobby14 with dissolve
js "It's for a weekly fashion segment that I'm doing to inspire girls on what to wear."
js "I also plan on writing segments on exercise and healthy food. I've got so many ideas!"
scene ep11_josy_hobby11 with dissolve
he "You shouldn't feel embarrassed; I think it sounds great. DM me a link to your blog."
scene ep11_josy_hobby15 with dissolve
js "Thanks for being supportive."
scene ep11_josy_hobby11 with dissolve
he "No problem."
he "And, oh! Do you want to chip in for some flowers for Rio? I thought we could send her some to cheer her up."
scene ep11_josy_hobby15 with dissolve
js "Sure, I'll chip in. But I don't know how much she'll be able to enjoy the scent - with the flu and all."
js "Stupid flu season. It's thoughtful of her not being here and spreading it to us."
scene ep11_josy_hobby12 with dissolve
he "Flu? I heard it was pneumonia."
scene ep11_josy_hobby16 with dissolve
js "Oh? I must have missed that. That's so much worse. Get her something beautiful from us."
show ep11_josy_hobby18
if not persistent.ep11_cardmy3:
    show screen ep11_render_screen("my3")
with dissolve
he "..."
he "We might want to consider getting another wardrobe in here."
show ep11_josy_hobby15
hide screen ep11_render_screen
with dissolve
js "I won't buy more clothes. Much more. I won't buy much more."
scene ep11_josy_hobby17 with dissolve
js "..."
stop music fadeout 3
scene ep11_josy_hobby15 with dissolve
js "For now..."
show screen new_phone_screen
if branchSage:
    jump ep11_sage_party_label

label ep11_pass_time_label:
play music "music/ep11/licensed_music/track159.mp3"
queue music ["music/ep11/christmas_jazz.mp3","music/ep11/licensed_music/track160.mp3","music/ep11/licensed_music/track161.mp3","music/ep11/licensed_music/track179.mp3","music/ep11/licensed_music/track183.mp3","music/ep11/licensed_music/track168.mp3","music/ep11/licensed_music/track159.mp3"]
scene ep11_pass_time1
show screen ep10_snow_screen
with fade
mc "{i}December... Here we go again. It has come to remind me why I hate winter.{/i}"
mc "{i}The only thing that consoles me this time of year is that the snow doesn't last long. Some years, we barely get any.{/i}"
mc "{i}But this year we got lots of it...{/i}"
if branchJill:
    scene ep11_pass_time2 with dissolve
    mc "{i}December hit differently. I was happy. I was with Jill.{/i}"
    mc "{i}And she was deadset on proving to me that winter can be fun.{/i}"
    play sound "sound_effects/season3/snowball1.mp3"
    scene ep11_pass_time3 with hpunch
    $ renpy.pause()
    scene ep11_pass_time4 with dissolve
    mc "{i}I don't know why she thought covering my face in snow would be fun.{/i}"
    scene ep11_pass_time5 with dissolve
    mc "{i}She claims it wasn't on purpose, but that was one hell of a throw.{/i}"
    scene ep11_pass_time6
    hide screen ep10_snow_screen
    with dissolve
    mc "{i}We played music together. It was hard to agree on what to play, as we were into different kinds of songs.{/i}"
    scene ep11_pass_time7 with dissolve
    mc "{i}We bonded more.{/i}"
    mc "{i}And thanks to Sage, I tried to pay more attention to Jill's feelings in our talks.{/i}"
    scene ep11_pass_time8 with dissolve
    mc "{i}We explored each other, too.{/i}"
    scene ep11_pass_time9 with dissolve
    mc "{i}I could tell she was getting more comfortable with herself. And she tried her best to use her sexuality to get me turned on. I loved seeing her trying.{/i}"
if branchSage:
    scene ep11_pass_time10
    hide screen ep10_snow_screen
    with dissolve
    mc "{i}I didn't mind the snow that much. I was too occupied with Sage.{/i}"
    scene ep11_pass_time11 with dissolve
    if ep2SageGuitarTeacher:
        mc "{i}We played guitar.{/i}"
    else:
        mc "{i}I got around to teaching Sage how to play the guitar.{/i}"
    if ep9_sage_vanilla or not ep10_sage_lewd:
        scene ep11_pass_time12 with dissolve
        mc "{i}We took long walks together.{/i}"
        scene ep11_pass_time13 with dissolve
        mc "{i}We talked, talked, and talked...{/i}"
        if jade_state > 0:
            mc "{i}...about everything but {b}that{/b}.{/i}"
        scene ep11_pass_time14 with dissolve
        mc "{i}And, of course, we had sex. And it felt better with each time.{/i}"
        scene ep11_pass_time15 with dissolve
        mc "{i}We started being more in sync and picked up on how to get each other off better.{/i}"
        scene ep11_pass_time16 with dissolve
        mc "{i}It was amazing how we connected on that level.{/i}"
    else:
        mc "{i}We talked...{/i}"
        if jade_state > 0:
            mc "{i}But not about Jade.{/i}"
        scene ep11_pass_time17 with dissolve
        if jade_state > 0:
            mc "{i}Honestly, most of the time we spent fucking.{/i}"
        else:
            mc "{i}But honestly, most of the time we spent fucking.{/i}"
        scene ep11_pass_time18 with dissolve
        mc "{i}And we were getting good at it.{/i}"
        scene ep11_pass_time19 with dissolve
        mc "{i}The sex was amazing.{/i}"
        scene ep11_pass_time20 with dissolve
        mc "{i}She wanted to try to push the boundaries more.{/i}"
        scene ep11_pass_time21 with dissolve
        mc "{i}The way she talked made me feel like she wanted a third in bed with us.{/i}"
        scene ep11_pass_time22 with dissolve
        mc "{i}She always had the best orgasms when we talked about threesomes.{/i}"
        scene ep11_pass_time23 with dissolve
        mc "{i}Other than that...{/i}"
    $ mgallery_add_photo("ep11_pass_time10b")
if branchIsabella:
    scene ep11_pass_time24
    hide screen ep10_snow_screen
    with dissolve
    mc "{i}I was lucky to have Bella by my side to get through it.{/i}"
    scene ep11_pass_time25 with dissolve
    mc "{i}She took great care of me by small gestures.{/i}"
    scene ep11_pass_time26 with dissolve
    mc "{i}She would slip me a gift card for the cafeteria in class with a sweet note.{/i}"
    scene ep11_pass_time27 with dissolve
    mc "{i}It wasn't the money but the thought and gesture that made me feel warm inside.{/i}"
    scene ep11_pass_time28 with dissolve
    mc "{i}Or, she would pull my jacket zipper all the way up and brush any dirt off my shoulders before I left the library at night.{/i}"
    scene ep11_pass_time29 with dissolve
    mc "{i}Those moments made staying late at the library worth it.{/i}"
    scene ep11_pass_time30 with dissolve
    mc "{i}The extra study time was just a bonus.{/i}"
    scene ep11_pass_time31 with dissolve
    $ renpy.pause()
    scene ep11_pass_time36 with dissolve
    mc "{i}She'd also send me pictures of herself, knowing how much I enjoyed them.{/i}"
    scene ep11_pass_time35 with dissolve
    mc "{i}Some casual ones...{/i}"
    scene ep11_pass_time34 with dissolve
    $ renpy.pause()
    scene ep11_pass_time32 with dissolve
    mc "{i}And some not casual ones. Haha...{/i}"
    scene ep11_pass_time33 with dissolve
    mc "{i}I tried to return those gestures - no, not the nude pictures - but I don't have the same nurturing side she does.{/i}"
    $ mgallery_add_photo("ep11_pass_time32")
    $ mgallery_add_photo("ep11_pass_time33")
    $ mgallery_add_photo("ep11_pass_time34")
    $ mgallery_add_photo("ep11_pass_time35")
    scene ep11_pass_time37 with dissolve
    mc "{i}I was also happy to see Jill and Bella spend time together again.{/i}"
    mc "{i}I admired Jill a lot for forgiving Bella.{/i}"
if branchMayaJosy:
    scene ep11_pass_time38
    hide screen ep10_snow_screen
    with dissolve
    mc "{i}I was bummed out by the way Dad received the news of my relationship with Josy and Maya.{/i}"
    scene ep11_pass_time39 with dissolve
    mc "{i}I tried not to let it get to me, but I kept thinking of the future and if he'd ever understand it.{/i}"
    scene ep11_pass_time40 with dissolve
    mc "{i}That energy must have rubbed off on Josy and Maya.{/i}"
    scene ep11_pass_time41 with dissolve
    mc "{i}They tried to support me in the ways they could think of. But even though the reason why I was sad was because of them...{/i}"
    scene ep11_pass_time42 with dissolve
    mc "{i}...it wasn't their fault.{/i}"
    scene ep11_pass_time43 with dissolve
    mc "{i}They hadn't done anything wrong. And I didn't want to mope around, so I told myself to let it go and try to enjoy our relationship.{/i}"
    scene ep11_pass_time44 with dissolve
    mc "{i}After all... It was the relationship I wanted to be in... Right?{/i}"
    scene ep11_pass_time45 with dissolve
    mc "{i}But, yeah... I could have handled it better than I did back then.{/i}"
    scene ep11_pass_time46 with dissolve
    mc "{i}Luckily for me. They could handle me.{/i}"
    scene ep11_pass_time47 with dissolve
    $ renpy.pause()
    scene ep11_pass_time48 with dissolve
    $ renpy.pause()
if branchAlone:
    scene ep11_pass_time49
    hide screen ep10_snow_screen
    with dissolve
    mc "{i}I mostly stayed indoors unless I had to go out.{/i}"
    if ep10_rolling:
        if ep11_follow_quinn and not ep10_lily_english and not wt_ep11_quinn_lilly:
            scene ep11_pass_time50 with dissolve
            mc "{i}Lily wasn't around much. I don't know if it had anything to do with how I treated her. Rolling with her got off to a bumpy start.{/i}"
            scene ep11_pass_time52 with dissolve
            mc "{i}And I thought it would feel weird seeing her at work. So, I stayed away from The Pink Rose.{/i}"
        else:
            scene ep11_pass_time51 with dissolve
            mc "{i}Lily kept me company whenever she didn't have to work.{/i}"
            if ep11_follow_quinn and not wt_ep11_quinn_lilly:
                mc "{i}She was salty about how I treated her at times. Rolling with her wasn't always easy.{/i}"
            scene ep11_pass_time52 with dissolve
            mc "{i}After deciding to roll together, I thought seeing her at work would feel weird. So, I stayed away from The Pink Rose.{/i}"
        if ep7_pinkrose:
            scene ep11_pass_time53 with dissolve
            mc "{i}Whenever I didn't have to work there myself...{/i}"
            scene ep11_pass_time54 with dissolve
            $ renpy.pause()

    if ep10_date_nicole:
        scene ep11_pass_time55 with dissolve
        mc "{i}I talked some to Nicole, but she was busy with her kid, and I didn't want to bother her.{/i}"
        scene ep11_pass_time56 with dissolve
        mc "{i}It was clear she was swamped.{/i}"

    if branchAlone and ep8_quinn_lewd:
        scene ep11_pass_time57 with dissolve
        mc "{i}Quinn was up to whatever she was doing.{/i}"
        mc "{i}She didn't seem to want my help or company at the time.{/i}"
        scene ep11_pass_time58 with dissolve
        mc "{i}It did bum me out, but I wasn't going to force her to spend time with me.{/i}"
        mc "{i}She obviously had important things to deal with.{/i}"
        if not ep10_quinn_help:
            mc "{i}And knowing what I knew, I wouldn't want to help with those things either.{/i}"
        else:
            mc "{i}I just wished she'd share what they were with me.{/i}"

    scene ep11_pass_time59 with dissolve
    mc "{i}It was a dull start to the month.{/i}"
    mc "{i}But it was understandable.{/i}"

scene ep11_pass_time60 with dissolve
mc "{i}Sage found herself closer to our newly formed circle of friends.{/i}"
scene ep11_pass_time61 with dissolve
mc "{i}Well, everybody did. We got along great as a group.{/i}"
if ep9_jm_sad:
    scene ep11_pass_time62b with dissolve
    mc "{i}Josy did her best to move on, but I could tell it was still hard for her.{/i}"

if ep10_got_contracts:
    scene ep11_pass_time62 with dissolve
    mc "{i}Maya was gearing up to deal with Patrick.{/i}"
    mc "{i}She felt brimming with confidence and joy. And that feeling was contagious.{/i}"
else:
    scene ep11_pass_time63 with dissolve
    if ep9_jm_sad:
        mc "{i}It didn't help that Maya tried to convince her that her way of dealing with Patrick was best for them.{/i}"
    else:
        mc "{i}Maya tried to convince Josy that her way of dealing with Patrick was best for them.{/i}"

scene ep11_pass_time65 with dissolve
mc "{i}Josy spent a lot of time alone.{/i}"
scene ep11_pass_time64 with dissolve
if ep9_jm_sad:
    mc "{i}I wasn't sure what she was up to, but I figured she needed time off from me.{/i}"
else:
    mc "{i}I wasn't sure what she was up to, but I figured she'd eventually let us know.{/i}"
$ guideSuggestedPage = 167
scene ep11_pass_time66 with dissolve
mc "{i}It wasn't just the snow that was cold. The mood at the DIKs was as well.{/i}"
scene ep11_pass_time68 with dissolve
mc "{i}After Nick left, Tommy mostly kept to himself.{/i}"
if ep9_heather_lewd == 2:
    mc "{i}I was likely part of the problem... But all I could do was to apologize and give him space.{/i}"
mc "{i}His breakup with Heather might have been the bigger reason for his mood, but it was hard to tell.{/i}"
mc "{i}He didn't talk much to anyone and my brothers were feeling low.{/i}"
scene ep11_pass_time67 with dissolve
mc "{i}After the big fight, we ironed some of it out. But things were left hanging in the air, and everyone pretended they were fine.{/i}"
mc "{i}Typical guys...{/i}"
scene ep11_pass_time69b with dissolve
mc "{i}But I got a break from them. And I needed it.{/i}"
mc "{i}I had to sort my thoughts and think about my future at B&R.{/i}"
mc "{i}I knew it was only a matter of time until I had to bring up the subject again...{/i}"
mc "{i}But I hoped to have something more to tell my brothers than what I had learned from Chad.{/i}"

show ep11_pass_time71
if not persistent.ep11_cardmy2:
    show screen ep11_render_screen("my2")
with dissolve
mc "{i}And besides, the DIKs had their own issues going on.{/i}"
mc "{i}Dany's pet rabbit...or bunny? Whatever he was... He... Well, he died.{/i}"
mc "{i}I don't know what happened, but Jamie got bummed out by it.{/i}"
show ep11_pass_time72
hide screen ep11_render_screen
with dissolve
mc "{i}Truthfully, I'm unsure if he was more bummed out by Franz's death or that he had to attend a funeral.{/i}"
mc "{i}Who even has a funeral for a pet? It's sad - I get it - but a funeral?{/i}"

scene ep11_pass_time73 with dissolve
mc "{i}I saw Rusty hang out with Micha again...{/i}"
mc "{i}I would have advised him not to do it if things were normal. But he was agitated enough by everything that was going on.{/i}"
if branchJill:
    scene ep11_pass_time74 with dissolve
    mc "{i}He didn't even try to talk to me about whatever his feelings for Jill were...{/i}"
    mc "{i}I figured he'd be quick to dismiss that and have a talk to me. So, I waited for him to approach me... But he didn't do it.{/i}"
    mc "{i}I admit, that was the first time I got annoyed with Rusty. I should have confronted him about it earlier, but again...{/i}"
    mc "{i}Typical guys...{/i}"
scene ep11_pass_time75 with dissolve
mc "{i}I saw Nick on campus a few times. He ignored me. His jaws were clenched, too.{/i}"
if ep11_nick_attitude > 1:
    mc "{i}Such a coward...{/i}"
else:
    mc "{i}I didn't know what to say, so I gave him space, just like Tommy.{/i}"
if branchIsabella:
    if ep11_nick_attitude > 1:
        mc "{i}Well, maybe I was a coward too...{/i}"
    mc "{i}I was worried he'd blow the lid off my relationship with Bella... I felt it was better to ignore him.{/i}"
if branchSage and ep4_toldDerekAboutJade:
    if ep11_nick_attitude > 1:
        mc "{i}Well, maybe I was a coward too...{/i}"
    mc "{i}I was worried he'd expose what I had done with Jade... I mean...maybe he already had.{/i}"
    mc "{i}I felt it was better to ignore him.{/i}"

scene ep11_pass_time76 with dissolve
mc "{i}The end of my first semester at B&R was approaching.{/i}"
mc "{i}And while it was the end of the year, it was also the beginning of something big.{/i}"
scene ep11_pass_time77 with dissolve
mc "{i}Something I never could have anticipated.{/i}"

label ep11_jocks_label:
hide screen new_phone_screen
play sound "sound_effects/whoosh.mp3"
scene ep11_jocks1
show screen ep10_snow_screen
with hpunch
an "Guess what I did today?"
play sound "sound_effects/season3/snowball1.mp3"
scene ep11_jocks2 with dissolve
cb "Cranked one out?"
scene ep11_jocks3 with dissolve
an "What?"
scene ep11_jocks2 with dissolve
cb "Get that ear checked out, already."
scene ep11_jocks3 with dissolve
an "What?"
scene ep11_jocks4 with dissolve
cb "Did you crank one out?"
play sound "sound_effects/season3/snowball2.mp3"
scene ep11_jocks5 with hpunch
an "No."

scene ep11_jocks6 with dissolve
cb "Ate a cheat meal?"
scene ep11_jocks7 with dissolve
an "No."
scene ep11_jocks6 with dissolve
cb "Personal best at the gym?"
scene ep11_jocks7 with dissolve
an "No."
scene ep11_jocks6 with dissolve
cb "Had a protein shake."
scene ep11_jocks9 with dissolve
an "That and..."
scene ep11_jocks10 with dissolve
cb "Played video games?"
scene ep11_jocks9 with dissolve
an "No."
scene ep11_jocks10 with dissolve
cb "Drank beer?"
scene ep11_jocks7 with dissolve
an "No."
scene ep11_jocks6 with dissolve
cb "Man, you didn't do a lot today."
scene ep11_jocks7 with dissolve
an "I shaved my balls, man."
scene ep11_jocks8 with dissolve
cb "Why would you tell me that?"

scene ep11_jocks11 with dissolve
dw "And that's how you do it."
play sound "sound_effects/season3/snowball1.mp3"
scene ep11_jocks12 with vpunch
cb "Do what?"
scene ep11_jocks13 with dissolve
dw "I just secured the HOTs for our Christmas party."
scene ep11_jocks14 with dissolve
an "That is awesome."
cb "Meh. Who needs them?"
scene ep11_jocks13 with dissolve
dw "Even if you don't like them, you should be happy to know that the DIKs won't have them at their party."
scene ep11_jocks15 with dissolve
cb "Fuck the fucking DIKs."
scene ep11_jocks16 with dissolve
an "What about New Year's?"
scene ep11_jocks17 with dissolve
dw "Caleb is right. Fuck the DIKs! I'm not planning on giving that one up either. I feel the HOTs owe us New Year's, too."
play sound "sound_effects/whoosh.mp3"
scene ep11_jocks18 with hpunch
$ renpy.sound.play("sound_effects/season3/snowball1.mp3", channel="sfx2", loop=False)
$ renpy.pause()

label ep11_maya_label:
if ep10_got_contracts:
    scene ep11_maya2
    hide screen ep10_snow_screen
    with wipeleft
    sa "So, you went through with it?"
    scene ep11_maya3 with dissolve
    my "Yes. I'm all set up starting next semester. I've got a student loan now."
    scene ep11_maya5 with dissolve
    sa "That's awesome... Congrats."
    scene ep11_maya8 with dissolve
    my "Thank you. It's a surreal feeling..."
    my "But I'm not completely out of the woods yet. There's still one matter that remains."
    scene ep11_maya9 with dissolve
    sa "Talking to your dad?"
    scene ep11_maya14 with dissolve
    my "He will realize something is wrong when it's time to pay my tuition."
    scene ep11_maya9 with dissolve
    sa "Are you nervous?"
    scene ep11_maya14 with dissolve
    my "I thought I'd be nervous. I should be nervous. But I'm not."
    scene ep11_maya9 with dissolve
    sa "How will you do it?"
    scene ep11_maya15 with dissolve
    my "I will tell him how it is. That I've decided to fund college independently in a way that doesn't involve him."
    my "I will thank him for lending me the money for one semester and that I won't need his money from now on."
    scene ep11_maya16 with dissolve
    my "At this point, he'll probably get mad. And that's why Derek will be there with me to help defuse the situation."
    my "And I will tell Dad that I'll pay him back what I owe him and that he will have to decide."
    scene ep11_maya9 with dissolve
    sa "Decide on what?"
    scene ep11_maya15 with dissolve
    my "If he can ever be ok with having a daughter who is gay or not."
    my "And if he can't... I will tell him that the day Mom passes away is the last day I pretend to be his daughter."
    my "And that every day until that day, I'll do it for Mom - not for him."
    scene ep11_maya10 with dissolve
    sa "You're going to say that to him?"
    scene ep11_maya16 with dissolve
    my "Believe me when I say I've had these thoughts for a long time."
    my "I want to give him a final chance on my terms. And if he can't accept that, I won't accept him as my dad."
    scene ep11_maya20 with dissolve
    $ renpy.pause()
    scene ep11_maya21 with dissolve
    $ renpy.pause()
    show ep11_maya22
    if not persistent.ep11_cardly11:
        show screen ep11_render_screen("ly11")
    with dissolve
    $ renpy.pause()
    show ep11_maya23
    hide screen ep11_render_screen
    with dissolve
    my "*{i}Sigh{/i}* This is supposed to feel like a victory... Yet it feels like a loss."
    scene ep11_maya24 with dissolve
    sa "If it is a loss, it's his loss, not yours. You need to understand that."
    scene ep11_maya25 with dissolve
    $ renpy.pause()
    scene ep11_maya26 with dissolve
    sa "Grab some Christmas lights from that box. Help us decorate and get some Christmas spirit."
    sa "Maybe you'll cheer up."
else:
    scene ep11_maya1
    hide screen ep10_snow_screen
    with wipeleft
    sa "I understand..."
    scene ep11_maya4 with dissolve
    my "But I don't think Josy will ever understand it. And I've tried to explain it to her several times now."
    scene ep11_maya6 with dissolve
    sa "You have to give her time. It's still a fresh wound."
    scene ep11_maya7 with dissolve
    my "More like a wound that had begun to heal, only to be slit open again."
    my "Only that this time... We're not fighting about it."
    scene ep11_maya9 with dissolve
    sa "Well, that's something."
    scene ep11_maya14 with dissolve
    my "No. You don't understand."
    my "When Josy and I fight, we sometimes say mean things to each other that we don't mean, and it can get pretty heated."
    my "But we've always fought for the same thing in different ways."
    scene ep11_maya16 with dissolve
    my "And now... We're not fighting anymore."
    my "We're not getting upset or yelling."
    my "And we talk way less about it."
    scene ep11_maya11 with dissolve
    sa "And you don't think that's good? Do you want to fight with her?"
    scene ep11_maya17 with dissolve
    my "Of course, I don't want to fight with her. Who in their right mind wants to fight? Fighting is horrible."
    my "But I have this bad feeling growing inside of me."
    scene ep11_maya19 with dissolve
    my "Like, we're supposed to fight, but we don't."
    my "If you're not fighting for something...have you given up?"
    scene ep11_maya11 with dissolve
    sa "Is that how you look at your choice with Patrick? Have you given up or chosen to adapt because you've run out of options?"
    scene ep11_maya15 with dissolve
    my "No, I'm adapting for sure."
    scene ep11_maya12 with dissolve
    sa "Then, there you have it. Maybe she's adapting too?"
    scene ep11_maya16 with dissolve
    my "I guess I'm worried...that's all."
    scene ep11_maya13 with dissolve
    sa "Wait. Are you worried about her feelings or yours?"
    scene ep11_maya18 with dissolve
    my "..."
    scene ep11_maya15 with dissolve
    my "It's complicated."
    if branchMayaJosy:
        scene ep11_maya12 with dissolve
        sa "No shit, it's complicated. There are three of you in that relationship."
        scene ep11_maya16 with dissolve
        my "Maybe that's why we're not fighting."
        scene ep11_maya13 with dissolve
        sa "Huh? Because of [name]?"
        scene ep11_maya18 with dissolve
        my "..."
        scene ep11_maya19 with dissolve
        my "I don't know what I'm saying. I'm talking out loud without thinking."
    scene ep11_maya12 with dissolve
    sa "You can't control Josy's feelings, but you can be in charge of your own emotions."
    sa "It's good that you're talking about this to me, but honestly, you're not talking to the person you should be having this conversation with."
    scene ep11_maya15 with dissolve
    my "You're right. And that's what I'm saying... But you're the one I felt like I could talk to."
    scene ep11_maya20 with dissolve
    $ renpy.pause()
    scene ep11_maya21 with dissolve
    $ renpy.pause()
    show ep11_maya22
    if not persistent.ep11_cardly11:
        show screen ep11_render_screen("ly11")
    with dissolve
    $ renpy.pause()
    show ep11_maya24
    hide screen ep11_render_screen
    with dissolve
    sa "Things will work out fine, Maya - one way or the other."
    sa "You have friends and support. Don't forget that."
    scene ep11_maya25 with dissolve
    $ renpy.pause()
    scene ep11_maya26 with dissolve
    sa "Grab some Christmas lights from that box. Help us decorate and get lost in your thoughts while doing it."
    sa "Maybe you'll find some answers there."
show screen new_phone_screen
jump ep11_freeroam_diks_intro_label

label ep11_sally_label:
play music "music/ep6/uplifting_ballad.mp3"
scene ep11_sally43 with dissolve
sy "I'm here. Let's get over and done with this crap."
scene ep11_sally44 with dissolve
mc "Oh, yeah... I forgot about the time. I'm in the middle of planning a party here."
scene ep11_sally45 with dissolve
sy "I'm not rescheduling. You'll have to postpone that."
scene ep11_sally44 with dissolve
mc "Sure, um... Let's sit on my bed. This place is somewhat of an organized mess at the moment."
scene ep11_sally1 with dissolve
sy "This better not take all evening."
scene ep11_sally2 with dissolve
mc "It won't. I already wrote parts of it."
scene ep11_sally3 with dissolve
sy "You did?"
scene ep11_sally4 with dissolve
mc "You don't mind, do you?"
scene ep11_sally5 with dissolve
sy "No, that's great. That saves me the trouble."
sy "Did you write the theory...?"
scene ep11_sally6 with dissolve
mc "Yeah, I got the feeling you wanted me to."
mc "Look... I know you're struggling in class, and I'm not gonna be a dick about it."
scene ep11_sally7 with dissolve
sy "I'm not struggling!"
scene ep11_sally8 with dissolve
mc "You are. You were all over the place in the lab and didn't know what the hell you were doing. But it's fine."
scene ep11_sally9 with dissolve
sy "You ARE a dick."
scene ep11_sally10 with dissolve
mc "You don't have to feel ashamed. I think some stuff is hard, too."
scene ep11_sally11 with dissolve
sy "Speak for yourself. I'm doing fine in school."
scene ep11_sally10 with dissolve
mc "Alright. I was gonna offer you extra help if you needed it. That's all."
scene ep11_sally12 with dissolve
sy "..."
scene ep11_sally13 with dissolve
mc "But I'm guessing you have all the help you need from your friends. With the notes and old tests."
scene ep11_sally14 with dissolve
sy "Ugh, well, I would have if they weren't being assholes to me right now."
scene ep11_sally13 with dissolve
mc "Who's being an asshole?"
scene ep11_sally14 with dissolve
sy "Ron, Magnar, Bert... Everyone!"
sy "They're not sharing anything with me anymore."
scene ep11_sally15 with dissolve
mc "Why not? Did something happen?"
scene ep11_sally16 with dissolve
sy "Mind your business."
scene ep11_sally15 with dissolve
mc "If you're gonna be like this about it, forget I asked."
scene ep11_sally12 with dissolve
sy "..."
scene ep11_sally17 with dissolve
sy "Hypothetically... What help are you offering?"
scene ep11_sally12 with dissolve
mc "You could ask me about what you don't understand, and I could tell you what I know."
mc "Maybe I don't understand it either, but I could teach you if I do. And vice versa."
scene ep11_sally18 with dissolve
mc "Sometimes, when they teach us new things in class, I don't want to ask what they mean because I fear I'd look dumb."
mc "So, instead, I don't ask questions and have to learn on my own. Maybe you are the same way."
scene ep11_sally17 with dissolve
sy "Sometimes. Not a lot. But you know...?"
sy "It happens."
scene ep11_sally19 with dissolve
sy "Like, freaking Professor Willcock's lectures... They are impossible."
scene ep11_sally20 with dissolve
mc "Haha! I know, right? He wanted us to interrupt him and ask questions, but I couldn't even come up with a question about what he was talking about."
scene ep11_sally21 with dissolve
sy "Right? What am I supposed to ask?"
sy "\"Professor Willcock? What the hell are you talking about!?\""
scene ep11_sally20 with dissolve
mc "Yeah, you can't ask that. Haha!"
scene ep11_sally21 with dissolve
sy "So, you have no clue either?"
scene ep11_sally22 with dissolve
mc "Some clue. But only because I read a lot after class."
scene ep11_sally23 with dissolve
sy "I don't even understand when I do that."
scene ep11_sally24 with dissolve
mc "How about we study together sometime? If we're gonna be lab partners from now on, we might as well, right?"
scene ep11_sally25 with dissolve
sy "Maybe."
scene ep11_sally24 with dissolve
if minigames and sm_purity <= 50 or (not minigames and affinity == "DIK"):
    mc "But we should write the report today. I think I figured out where we went wrong during lab."
    scene ep11_sally25 with dissolve
    sy "Show me."
else:
    mc "But we should write the report today."
    scene ep11_sally25 with dissolve
    sy "Right. Show me what you wrote."
scene ep11_sally26 with Dissolve(2)
$ renpy.pause()
scene ep11_sally27 with Dissolve(2)
$ renpy.pause()
scene ep11_sally28 with Dissolve(2)
mc "Then multiply that with the molar mass..."
scene ep11_sally29 with dissolve
sy "Done."
scene ep11_sally28 with dissolve
mc "And divide that with the theoretical mass."
scene ep11_sally29 with dissolve
sy "And multiply by 100 to get the purity..."
scene ep11_sally28 with dissolve
mc "Yep, you got it."
scene ep11_sally30 with dissolve
sy "I can't believe it was this easy."
scene ep11_sally31 with dissolve
mc "That's because we analyzed the units of measurement. It's easy to get lost if you skip that step."
scene ep11_sally30 with dissolve
sy "What's left?"
scene ep11_sally31 with dissolve
mc "We write a short conclusion about what we did right and wrong, and that should be it."
scene ep11_sally32 with dissolve
sy "Ok, you can leave that one to me."
scene ep11_sally31 with dissolve
mc "Are you sure?"
scene ep11_sally32 with dissolve
sy "Yeah. You spent extra time writing the theory section; it's the least I can do."
scene ep11_sally31 with dissolve
mc "I appreciate it."
play sound "sound_effects/season3/type1.mp3"
scene ep11_sally33 with dissolve
$ renpy.pause()
scene ep11_sally34 with dissolve
sy "So, what's that party you're planning?"
scene ep11_sally35 with dissolve
mc "It's the Christmas party."
scene ep11_sally34 with dissolve
sy "Ah, figures."
scene ep11_sally35 with dissolve
mc "Wanna come?"
scene ep11_sally34 with dissolve
sy "Sure."
scene ep11_sally35 with dissolve
mc "Um... About the theme... It's gonna be a hybrid party because of reasons."
play sound "sound_effects/season3/type2.mp3"
scene ep11_sally34 with dissolve
sy "A hybrid of what?"
scene ep11_sally36 with dissolve
mc "Christmas and underwear. It's a Christmas Panty party."
scene ep11_sally37 with dissolve
sy "I swear, you guys always do these things. I'd have to show up in my underwear?"
scene ep11_sally36 with dissolve
mc "Yeah, but there will be masks for those who want one."
scene ep11_sally37 with dissolve
sy "Can I cover my private parts with it?"
scene ep11_sally36 with dissolve
mc "Haha, no."
scene ep11_sally37 with dissolve
sy "Then probably no... We'll see."
play sound "sound_effects/season3/type1.mp3"
scene ep11_sally38 with dissolve
sy "And...done! I'll mail you a copy and submit the report to Dr. Jenkins."
scene ep11_sally39 with dissolve
mc "Good job. It went smoother than I dared to hope."
scene ep11_sally38 with dissolve
sy "Likewise."

scene ep11_sally40 with dissolve
sy "Wanna study some before class? Like, later this week or whenever?"
scene ep11_sally41 with dissolve
mc "Maybe not this week, but someday, sure. How about if I shoot you a message when I plan on dropping by the library?"
scene ep11_sally40 with dissolve
sy "Sounds good. Don't forget about it."
scene ep11_sally42 with dissolve
stop music fadeout 3
mc "(I knew she wasn't all bad.)"
$ new_bio("Sally", "We wrote a lab report together, and it went better than I had expected. We started bonding.")

label ep11_jill_grave_label:
play music "music/ep11/licensed_music/track169.mp3"
if not branchJill and not ep9_b_kissed_jill:
    hide screen new_phone_screen
    scene ep11_jill_grave1 with fade
    $ renpy.pause()
    scene ep11_jill_grave2 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave3 with dissolve
    ji "Happy Birthday, Sis."
    ji "You probably already guessed what you're getting this year."
    scene ep11_jill_grave4 with dissolve
    isa "Happy Birthday, Lana."
    scene ep11_jill_grave5 with dissolve
    isa "Her grave is as pretty as last year."
    scene ep11_jill_grave6 with dissolve
    ji "Thank you for coming with me."
    scene ep11_jill_grave7 with dissolve
    isa "I'm glad you asked me to."
    scene ep11_jill_grave8 with dissolve
    ji "You didn't even ask why I wanted you to come here again."
    scene ep11_jill_grave9 with dissolve
    isa "Oh? Was there a particular reason?"
    scene ep11_jill_grave8 with dissolve
    ji "Lately, I've been thinking a lot about her. And a lot of bad feelings resurfaced."
    scene ep11_jill_grave9 with dissolve
    isa "I'm sorry to hear that."
    scene ep11_jill_grave10 with dissolve
    ji "I think something triggered me at that Thanksgiving barbecue."
    if ep10_shroom_choice == "DIK":
        ji "When I realized that [name] and his friends were on drugs, it was hard to stop thinking about Lana."
        scene ep11_jill_grave13 with dissolve
        isa "[name] was on drugs?"
        scene ep11_jill_grave11 with dissolve
        ji "He was. They had eaten mushrooms and were noticeably intoxicated."
        if branchIsabella:
            scene ep11_jill_grave14 with dissolve
            isa "..."
        else:
            scene ep11_jill_grave13 with dissolve
            isa "That makes me surprised and sad to hear."
        scene ep11_jill_grave10 with dissolve
        ji "I did not expect that from him."
    else:
        ji "When I realized that some of the guys were on drugs, it was hard to stop thinking about Lana."
        scene ep11_jill_grave13 with dissolve
        isa "What kind of drugs?"
        scene ep11_jill_grave10 with dissolve
        ji "I believe they had eaten mushrooms or something and were noticeably affected."
    ji "They all acted weirdly during the evening, and it was concerning."
    scene ep11_jill_grave13 with dissolve
    isa "I can see how that triggered you."
    scene ep11_jill_grave11 with dissolve
    ji "It made me think about Lana and Jonathan. And I remembered the bad years before I talked to Jonathan again."
    ji "I used to be so mad at him."
    scene ep11_jill_grave10 with dissolve
    ji "Like, how could this nice guy who was wonderful to me and my sister be the reason my sister died?"
    ji "Mom told me it was his fault, and I believed her."
    scene ep11_jill_grave12 with dissolve
    ji "Did I tell you that I ran into him at the mall once?"
    scene ep11_jill_grave13 with dissolve
    isa "Remind me."
    scene ep11_jill_grave12 with dissolve
    ji "It was some years before I met you. I didn't expect to see Jonathan there; he was far from my mind."
    ji "But the moment I saw him..."
else:
    scene ep11_jill_grave28 with fade
    $ renpy.pause()
    scene ep11_jill_grave2 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave3 with dissolve
    ji "Happy Birthday, Sis."
    ji "You probably already guessed what you're getting this year."
    scene ep11_jill_grave4 with dissolve
    mc "What's that?"
    ji "It's a birthday gift I never got to give her."
    ji "I made it at school for her birthday. Perhaps it's hard to tell, but that's supposed to be her if she were a troll."
    scene ep11_jill_grave29 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave30 with dissolve
    ji "Haha! It's so ugly."
    scene ep11_jill_grave4 with dissolve
    mc "Haha! It has its...charm."
    ji "I give it to her every year, along with flowers and a candle. It has become a tradition."
    if branchJill:
        scene ep11_jill_grave31 with dissolve
    else:
        scene ep11_jill_grave34 with dissolve
    mc "It's peaceful here."
    if branchJill:
        scene ep11_jill_grave32 with dissolve
    else:
        scene ep11_jill_grave35 with dissolve
    ji "Isn't it? It's a nice place for her final rest."
    if branchJill:
        scene ep11_jill_grave31 with dissolve
    else:
        scene ep11_jill_grave34 with dissolve
    mc "How does it feel coming here? Does it make you sad?"
    if branchJill:
        scene ep11_jill_grave32 with dissolve
    else:
        scene ep11_jill_grave35 with dissolve
    ji "I feel somber yet weirdly calm."
    ji "I used to cry a lot coming here, but now I don't."
    scene ep11_jill_grave33 with dissolve
    ji "It's not that her grave has lost its meaning, but I've processed her death for so long."
    ji "I don't think Lana would want me to show up on her birthday every year to cry."
    scene ep11_jill_grave36 with dissolve
    ji "This year, I brought you here. She would have wanted to meet you."
    scene ep11_jill_grave37 with dissolve
    mc "Do you think Lana and I would have gotten along?"
    scene ep11_jill_grave36 with dissolve
    ji "Like a house on fire."
    scene ep11_jill_grave38 with dissolve
    if ep10_shroom_choice == "DIK":
        ji "Even with the drugs..."
    else:
        ji "Probably not with the drugs..."
    scene ep11_jill_grave37 with dissolve
    mc "What do you mean by that?"
    scene ep11_jill_grave38 with dissolve
    if branchJill and ep10_shroom_choice == "DIK":
        ji "I should have told you this earlier, but it's not something I enjoy bringing up."
    else:
        ji "I haven't told you this, but it's not something I enjoy bringing up."
    ji "It's about how my sister died."
    scene ep11_jill_grave39 with dissolve
    ji "When I was young, Mom and Dad told me it was an accident. And they tried to spare me from the details."
    ji "But when I grew older, I wanted to hear the full version about how she died."
    scene ep11_jill_grave40 with dissolve
    ji "Mom told me she died because of drugs and that it was her boyfriend's fault."
    scene ep11_jill_grave39 with dissolve
    ji "Lana had a boyfriend named Jonathan. He was the son of one of Dad's acquaintances."
    ji "He was always nice to me and got along very well with Lana. That's how they got together."
    scene ep11_jill_grave40 with dissolve
    ji "When Mom told me it was his fault that Lana died, I was so mad at him."
    ji "He didn't even show up at her funeral, and he was the reason I lost my sister."
    scene ep11_jill_grave41 with dissolve
    ji "I ran into him at the mall a few years ago, and it was like I couldn't breathe."
ji "Looking into his eyes, all I saw was my sister."
ji "I could see the panic in his eyes as he spotted me."
ji "I couldn't hold it together, so I ran in the other direction crying. I ran far from him."
if not branchJill and not ep9_b_kissed_jill:
    scene ep11_jill_grave15 with dissolve
else:
    scene ep11_jill_grave42 with dissolve
ji "Not that long after, I received a letter from him. He wanted to meet me and talk about Lana."
ji "He wanted to explain what had happened and how he felt, which surprised me."
ji "Why would he want to do that? Why care now when he hasn't cared for so many years about Lana or me?"
if not branchJill and not ep9_b_kissed_jill:
    scene ep11_jill_grave12 with dissolve
    ji "It took all my courage to meet up with him to talk."
else:
    scene ep11_jill_grave43 with dissolve
    mc "What did you do? Did you meet up with him?"
    scene ep11_jill_grave12 with dissolve
    ji "It took all my courage, but I did. I was so nervous."

scene ep11_jill_grave55 with Dissolve(2)
$ renpy.pause()
scene ep11_jill_grave56 with dissolve
than "You came."
scene ep11_jill_grave57 with dissolve
ji "..."
scene ep11_jill_grave58 with dissolve
ji "I needed to hear what you had to say."
scene ep11_jill_grave66 with dissolve
than "Where do I even begin?"
scene ep11_jill_grave59 with dissolve
ji "*{i}Breathing heavily{/i}* Maybe you could explain why you killed my sister and didn't have the courage to care about us after!?"
scene ep11_jill_grave67 with dissolve
than "..."
scene ep11_jill_grave68 with dissolve
than "I didn't kill your sister, but I used to blame myself for her death for a long time. I don't anymore."
scene ep11_jill_grave60 with dissolve
ji "How can you say that!?"
scene ep11_jill_grave68 with dissolve
than "I loved Lana. And I still do."
than "I tried talking her out of trying cocaine, but she insisted."
than "And since it was her birthday wish...I caved and got her some."
scene ep11_jill_grave61 with dissolve
ji "*{i}Sobs{/i}*"
scene ep11_jill_grave69 with dissolve
than "But I couldn't have known that the cocaine was poisoned."
scene ep11_jill_grave60 with dissolve
ji "What?"
scene ep11_jill_grave68 with dissolve
than "The coke they sold me that night... It was laced with fentanyl. It's something dealers add to dilute the drug to sell more for less product."
than "But they must have put too much in it, which ended up killing Lana."
scene ep11_jill_grave62 with dissolve
$ renpy.pause()
scene ep11_jill_grave69 with dissolve
than "At the party, down to the last moments before she used it, I tried to talk her out of it."
scene ep11_jill_grave75 with dissolve
than "She was going to use it no matter what I said."
than "She thought I was a hypocrite for buying it in the first place if I was going to tell her not to use it."
scene ep11_jill_grave76 with dissolve
than "She got annoyed, and I told her, \"Fine, do what you want. But I don't wanna watch it\"."
than "I headed outside to smoke with my friends."
scene ep11_jill_grave77 with dissolve
than "When I came back inside to check on her, I found her dozing off on the couch."
scene ep11_jill_grave78 with dissolve
than "Only that she..."
scene ep11_jill_grave79 with dissolve
than "..."
scene ep11_jill_grave80 with dissolve
than "She wasn't sleeping. She had foam coming from her mouth, and her lips were blue."
scene ep11_jill_grave70 with dissolve
than "We tried to give her CPR while we waited for the paramedics, but there wasn't anything we could do. She was already gone."
scene ep11_jill_grave63 with dissolve
than "She was declared dead on arrival. But I went with her to the hospital even so."
scene ep11_jill_grave69 with dissolve
than "I faced your parents, and tried to explain myself to them. They were devastated and inconsolable."
than "As was I."
scene ep11_jill_grave70 with dissolve
than "The coward that I was couldn't even admit that it was me who got her the coke."
than "But it didn't matter. I could tell from everyone's looks that I was to blame."
than "I wanted to come to the funeral, but they told me I wasn't welcome."
scene ep11_jill_grave71 with dissolve
than "I still came to say my goodbyes, but I kept myself at a distance out of respect for your family."
than "Letting go of Lana has been the hardest struggle of my life."
than "I've gone through years of therapy and dedicated my career to Lana's memory."
scene ep11_jill_grave64 with dissolve
ji "Your career? How?"
scene ep11_jill_grave72 with dissolve
than "I give lectures on drug use to young adults and how it can ruin your life."
than "And I've started a support group for survivors and victims of drug use and abuse."
than "We meet every Wednesday to talk and process the drug-related events that have changed our lives."
scene ep11_jill_grave73 with dissolve
than "To provide comfort and be heard in that setting is meaningful for everyone who attends."
than "It becomes a part of everyone's healing process, and the group has helped many battle their inner demons."
scene ep11_jill_grave65 with dissolve
$ renpy.pause()
scene ep11_jill_grave64 with dissolve
ji "Do you talk about my sister there?"
scene ep11_jill_grave73 with dissolve
than "Sometimes, I do. When there are newcomers, and no one feels like sharing their stories, I talk about Lana."
than "Your sister's story has a way of making people open up and talk."
scene ep11_jill_grave65 with dissolve
ji "..."
scene ep11_jill_grave71 with dissolve
than "Would you like to come? You don't have to share anything about Lana unless you want to."
than "You could just be there and listen. Come and see for yourself how your sister's story helps people."
scene ep11_jill_grave74 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 175
if not branchJill and not ep9_b_kissed_jill:
    scene ep11_jill_grave16 with Dissolve(2)
    $ renpy.pause()
    scene ep11_jill_grave15 with dissolve
    ji "All those feelings resurfaced at the barbecue."
    ji "To see them use drugs like that, knowing how it could go horribly wrong, it bothered me. But I didn't speak up."
    ji "If something bad had happened, would I have felt like Jonathan?"
    scene ep11_jill_grave18 with dissolve
    isa "I understand you. But you can't control what others do."
    isa "They don't have the same experience and look at life differently."
    isa "As sad as it is, experimenting with drugs is common. I mean, even I smoked pot when I was in college."
    scene ep11_jill_grave17 with dissolve
    ji "I know. *{i}Sigh{/i}* But seeing it happen in front of me made me feel bad."
    if ep10_shroom_choice == "DIK":
        ji "And seeing [name] on drugs... That was the hardest part."
    scene ep11_jill_grave16 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave19 with dissolve
    ji "Anyway... That's why it felt extra good to have you here today."
    ji "Thank you."
    scene ep11_jill_grave20 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave21 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave24 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave25 with dissolve
    ji "Would you like to accompany Bianca and me to her family's cabin next weekend?"
    scene ep11_jill_grave22 with dissolve
    isa "Her cabin? What are you doing there?"
    scene ep11_jill_grave25 with dissolve
    ji "We're going skiing and having some needed R&R before the finals."
    scene ep11_jill_grave22 with dissolve
    if branchIsabella:
        isa "I'd love to."
        scene ep11_jill_grave21 with dissolve
        ji "You can bring [name] if you'd like."
        scene ep11_jill_grave23 with dissolve
        isa "Are you sure that would be ok?"
        scene ep11_jill_grave25 with dissolve
        ji "I think he'd enjoy it."
    else:
        isa "I'd love to."
    scene ep11_jill_grave21 with dissolve
    $ renpy.pause()
    scene ep11_jill_grave26 with dissolve
    ji "Thank you for this time, Sis. The moon has been beautiful lately. I bet you had something to do with it. I'll see you soon."
    stop music fadeout 3
    scene ep11_jill_grave27 with dissolve
    $ renpy.pause()
else:
    scene ep11_jill_grave44 with Dissolve(2)
    $ renpy.pause()
    scene ep11_jill_grave43 with dissolve
    mc "I didn't realize that's how she died. I've wanted to ask but didn't want to be insensitive."
    scene ep11_jill_grave45 with dissolve
    ji "All those feelings resurfaced at the barbecue."
    if ep10_shroom_choice == "DIK":
        ji "To see you and your friends use drugs like that, knowing how it could go horribly wrong, it bothered me."
    else:
        ji "To see your friends use drugs like that, knowing how it could go horribly wrong, it bothered me. But I didn't speak up."
    ji "If something bad had happened, would I have felt like Jonathan?"
    if ep10_shroom_choice == "DIK":
        scene ep11_jill_grave43 with dissolve
        mc "Jill..."
        scene ep11_jill_grave45 with dissolve
        ji "I'm not trying to make you feel bad about it."
        if ep10_jill_promise:
            ji "I appreciate that you promised not to do it again."
        else:
            ji "But I am worried you'll keep doing it."
    scene ep11_jill_grave44 with dissolve
    if ep10_shroom_choice == "DIK":
    
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Jill)","(+Jill)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        menu:
            "Can't live life scared \n{size=-4}[m_c1][mod_choices[0]]":
                label ep11_jill_grave2_label:
                $ RPjill -= 1
                scene ep11_jill_grave43 with dissolve
                mc "You can't live life being scared that something will kill you. Because in the end, something will."
                mc "Tomorrow, you could walk in front of a bus or fall down the stairs."
                scene ep11_jill_grave45 with dissolve
                ji "But you can make sensible choices."
                scene ep11_jill_grave43 with dissolve
                mc "And live all sheltered? Never trying new things?"
                mc "What about parachuting or bungee jumping? Bad things could happen doing that, but people still do it."
                scene ep11_jill_grave48 with dissolve
                ji "Maybe I'm wrong, but I don't feel like I am."
                scene ep11_jill_grave49 with dissolve
                mc "We don't have to agree on everything. I'm very sorry drugs killed your sister."
                scene ep11_jill_grave47 with dissolve
                ji "Me too. You two would have gotten along great, haha."
            "It was stupid of me \n{size=-4}[m_c1][mod_choices[1]]":
                $ RPjill += 1
                scene ep11_jill_grave43 with dissolve
                mc "I haven't looked at it the same way you do. It was a stupid thing to try with my friends."
                mc "Maybe it was peer pressure, but I didn't think it would be harmful."
                scene ep11_jill_grave45 with dissolve
                ji "Lana didn't think it would be harmful either. That's all I'm saying."
                scene ep11_jill_grave43 with dissolve
                mc "You're right. I should have thought more about it."
                scene ep11_jill_grave47 with dissolve
                ji "Thank you."
    else:
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Jill)","(+Jill)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        menu:
            "Can't live life scared":
                jump ep11_jill_grave2_label
            "It was stupid of them \n{size=-4}[m_c1][mod_choices[1]]":
                $ RPjill += 1
                scene ep11_jill_grave43 with dissolve
                mc "I haven't looked at it the same way you do. But it was a stupid thing they did."
                if ep10_shroom_choice == "NEUTRAL":
                    mc "Maybe I should have told them not to use it, but I figured they could decide for themselves."
                else:
                    mc "I did try stopping them, but they still wanted to try it."
                scene ep11_jill_grave46 with dissolve
                mc "That's how guys are at times. We do stupid things for laughs and try things for fun."
                mc "They weren't thinking about how it could be harmful when they chose to eat those shrooms."
                scene ep11_jill_grave45 with dissolve
                ji "Lana didn't think it would be harmful either. That's all I'm saying."
                scene ep11_jill_grave43 with dissolve
                mc "You're right."
                scene ep11_jill_grave47 with dissolve
                ji "Thank you."
    scene ep11_jill_grave50 with dissolve
    ji "Like Jonathan devoted his career to the memory of Lana, I want to do something similar for her as well."
    ji "I'm meeting him later this month to discuss a campaign to raise awareness about substance abuse."
    ji "It's something I've wanted to do for a long time."
    mc "If it means that much to you, you should do it."
    ji "It does. Thanks for listening."
    mc "Thanks for sharing."

    if branchJill:
        scene ep11_jill_grave51 with dissolve
        ji "About something else... Something merrier... I've been thinking of fun things to do together during winter."
        scene ep11_jill_grave52 with dissolve
        mc "Tell me about them."
        scene ep11_jill_grave51 with dissolve
        ji "Would you like to accompany Bianca and me to her family's cabin next weekend?"
    else:
        scene ep11_jill_grave51 with dissolve
        ji "About something else... Something merrier... Would you like to accompany Bianca and me to her family's cabin next weekend?"
    scene ep11_jill_grave52 with dissolve
    mc "A cabin? Where is it?"
    scene ep11_jill_grave51 with dissolve
    if branchJill:
        ji "It's some hours away from here by car. Woods and mountains surround it, and I think it's a perfect opportunity for me to teach you how to ski."
    else:
        ji "It's some hours away from here by car. Woods and mountains surround it and offer a great opportunity to ski."
    scene ep11_jill_grave52 with dissolve
    mc "Mountains, woods, snow, skiing... That's a lot of things I don't like."
    if branchJill:
        scene ep11_jill_grave53 with dissolve
        ji "Haha, I know. It's the point of it and part of our deal. To make you come around on winter."
        scene ep11_jill_grave52 with dissolve
        mc "But what about my finals? I need to study, don't you?"
        scene ep11_jill_grave53 with dissolve
        ji "I will cram extra during next week so I can take a couple of days off."
        scene ep11_jill_grave52 with dissolve
        mc "Ok... Let's do it."
        scene ep11_jill_grave53 with dissolve
        ji "Do you mean it?"
        scene ep11_jill_grave52 with dissolve
        mc "I promised, didn't I? So, you, me and Bianca, is it?"
        scene ep11_jill_grave51 with dissolve
        ji "I'm asking Bella, too. I'm sure she'll love it."
        scene ep11_jill_grave52 with dissolve
        mc "It does sound fun."
    else:
        scene ep11_jill_grave53 with dissolve
        ji "I was thinking it would be nice to get away together. I'm asking Bella, too."
        scene ep11_jill_grave52 with dissolve
        mc "I'm not sure I have time for it, with my finals and all."
        scene ep11_jill_grave51 with dissolve
        ji "I will cram extra during next week so I can take a couple of days off. You could do that, too."
        scene ep11_jill_grave52 with dissolve
        mc "Ok... Let's do it."

    scene ep11_jill_grave26 with dissolve
    ji "Thank you for this time, Sis. The moon has been beautiful lately. I bet you had something to do with it. I'll see you soon."
    stop music fadeout 3
    scene ep11_jill_grave54 with dissolve
    $ renpy.pause()
    $ new_bio("Jill", "I went to Lana's grave together with Jill. Jill told me about how Lana died and about Lana's boyfriend Jonathan.")

label ep11_cathy_jade_label:
hide screen new_phone_screen
play music "music/ep11/licensed_music/track167.mp3"
scene ep11_cathy_jade1 with wipeleft
$ renpy.pause()
scene ep11_cathy_jade2 with dissolve
$ renpy.pause()
scene ep11_cathy_jade18 with dissolve
$ renpy.pause()
scene ep11_cathy_jade19 with dissolve
ca "I'm shocked and...angry hearing that. It feels like rain from a clear sky."
scene ep11_cathy_jade3 with dissolve
ja "Trust me, there hasn't been a clear sky in years. It's been perpetually cloudy, and the thunderstorm has finally started."
scene ep11_cathy_jade20 with dissolve
ca "Have you considered couples therapy?"
scene ep11_cathy_jade4 with dissolve
ja "Hah, therapy! That's rich. Try getting Stephen to open up about anything other than sports and money."
ja "No therapist in this world would make a dent in his rock-hard shell."
scene ep11_cathy_jade3 with dissolve
ja "He's determined to go through with it. He has already signed the divorce papers. All that's left is for me to decide what to do."
scene ep11_cathy_jade20 with dissolve
ca "I'm so sorry... So, the divorce is inevitable?"
scene ep11_cathy_jade3 with dissolve
ja "It's now a matter of going through a mediator or separation lawyer."
scene ep11_cathy_jade21 with dissolve
ca "As I understand, all divorce lawyers care about is inflicting maximum damage to maximize their earnings."
ca "It would be best and fair for everyone if you can reach an agreement through mediation."
if ep4_toldDerekAboutJade:
    scene ep11_cathy_jade5 with dissolve
    ja "Nothing would be fair. Stephen wants me to agree on a 90/10 split, even without a prenup."
    scene ep11_cathy_jade22 with dissolve
    ca "That's ridiculous! He can't be serious."
    scene ep11_cathy_jade5 with dissolve
    ja "Oh, he is serious."
    scene ep11_cathy_jade23 with dissolve
    ca "He sounds delusional. If you take it to court, I doubt he'd even get close to that."
    scene ep11_cathy_jade6 with dissolve
    ja "He said I could get half if I wanted. But..."
    scene ep11_cathy_jade21 with dissolve
    ca "But what?"
    scene ep11_cathy_jade6 with dissolve
    ja "I don't think I should say... He has leverage, and he's using it."
    scene ep11_cathy_jade26 with dissolve
    ca "What did you do?"
    scene ep11_cathy_jade5 with dissolve
    ja "Nothing that he hasn't done. The only difference is that he can prove it."
    scene ep11_cathy_jade22 with dissolve
    ca "Is he blackmailing you?"
    scene ep11_cathy_jade7 with dissolve
    ja "Yes. There's no other way to describe it. He could ruin my career and what's left of my family."
    scene ep11_cathy_jade26 with dissolve
    ca "It must be some damning evidence."
    scene ep11_cathy_jade7 with dissolve
    ja "I had sex with a student. And Stephen has video proof of it."
    if branchSage:
        scene ep11_cathy_jade8 with dissolve
        ja "And to make matters worse, this student is in a relationship with my daughter."
        ja "And before you ask me, no, I wasn't aware that I fucked my daughter's boyfriend."
        ja "I would never have done that knowingly. But I have a hard time Sage would believe me, and even if she did, would she ever forgive me?"
    else:
        scene ep11_cathy_jade8 with dissolve
        ja "And to make matters worse, this student is a close friend of my daughter."
        ja "I have a hard time imagining she'd forgive me for doing this with any student, let alone her friend."
    scene ep11_cathy_jade24 with dissolve
    ca "..."
    scene ep11_cathy_jade25 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade9 with dissolve
    ja "I see that you grasp the situation I'm in."
    ja "What choice does he leave me with? I have to accept the 10%%, or I'd risk losing everything that means something to me."
    scene ep11_cathy_jade24 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade29 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade9 with dissolve
    ja "Will you say something?"
    scene ep11_cathy_jade30 with dissolve
    ca "My head is in many places at once, so you must forgive me."
    ca "I'm guessing that 10%% is still a lot of money and assets for you."
    ca "It's not like you'd end up on the streets."
    scene ep11_cathy_jade32 with dissolve
    ja "I would have to move."
    scene ep11_cathy_jade30 with dissolve
    ca "Wouldn't that still be the case if you got 50%%? Why would you want to live in a home tainted by him?"
    scene ep11_cathy_jade32 with dissolve
    ja "It's more than money and the actual apartment. It's my pride and the symbolic meaning of agreeing to his terms."
    ja "Men always have it easier. Stephen has always gotten opportunities he didn't deserve or worked hard enough for."
    scene ep11_cathy_jade33 with dissolve
    ja "And now, he wants to silence me and rob me of the fortune we made together as a family."
    ja "It cuts deep."
    scene ep11_cathy_jade34 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade30 with dissolve
    ca "I can only imagine how angry you must feel."
    ca "As your friend, I will always support you, regardless of your choice. But I would advise you to meet with a lawyer and hear what they say."
    scene ep11_cathy_jade36 with dissolve
    ja "We have joint accounts; Stephen will monitor my transactions. The moment he learns I've met with a lawyer is the moment I lose."
    ja "He's not bluffing, Cathy. He would use that video against me."
    scene ep11_cathy_jade35 with dissolve
    ja "And all of this happened because I wanted to get back at him..."
    ja "No... All of this happened because [name] decided to screw me over with that recording."
    scene ep11_cathy_jade31 with dissolve
    ca "[name] [lname]!?"
    ca "You're not saying..."
    scene ep11_cathy_jade17 with dissolve
    ja "..."
    scene ep11_cathy_jade31 with dissolve
    ca "Is he the student you slept with?"
    scene ep11_cathy_jade16 with dissolve
    ja "He's the student I ravished in our car, marital bed and bathroom..."
    label ep11_cathy_jade2_label:
    scene ep11_cathy_jade44 with dissolve
    ca "So, it wasn't just the one time either?"
    scene ep11_cathy_jade37 with dissolve
    ja "Well, those three were the same night."
    scene ep11_cathy_jade51 with dissolve
    $ renpy.pause()
    if pathCathy:
        scene ep11_cathy_jade49 with dissolve
        ca "And here I thought it was just me..."
        scene ep11_cathy_jade40 with dissolve
        ja "Come again."
        scene ep11_cathy_jade50 with dissolve
        ca "..."
        scene ep11_cathy_jade49 with dissolve
        if ep7_rejected_cathy:
            ca "Nothing happened between us. We made out a little bit before I quit my job..."
            ca "...and I may have performed fellatio on him during a car ride."
        else:
            ca "Nothing big happened between us..."
            ca "...but I may have performed fellatio on him during a car ride."
        scene ep11_cathy_jade41 with dissolve
        ja "May have? You make it sound like it was an accident. Did his cock fall into your mouth?"
        scene ep11_cathy_jade45 with dissolve
        ca "Oh my God, haha. No. It's... Forget I said anything."
        scene ep11_cathy_jade41 with dissolve
        ja "He ravished you too, didn't he?"
        if ep10_cathy_lewd:
            scene ep11_cathy_jade46 with dissolve
            ca "More like the other way around. Recently, I almost devoured him."
            scene ep11_cathy_jade41 with dissolve
            ja "Haha! I can't believe what I'm hearing."
            scene ep11_cathy_jade42 with dissolve
            ja "Well... Actually, I can. It's typical for a guy like him."
            ja "Him and his smooth talk..."
            ja "It doesn't surprise me that he tries to fuck anything that smiles at him."
        else:
            scene ep11_cathy_jade45 with dissolve
            ca "Believe me, I wanted him to. But no, that's all that happened."
            scene ep11_cathy_jade41 with dissolve
            ja "It was only a matter of time. He wasn't hard to persuade at all."
            scene ep11_cathy_jade42 with dissolve
            ja "Him and his smooth talk..."
            ja "It doesn't surprise me that he tries to insert his cock in any willing hole."
        scene ep11_cathy_jade44 with dissolve
        ca "Hey, you don't have to be rude to me."
        scene ep11_cathy_jade43 with dissolve
        ja "No offense, darling. He got us both."
        scene ep11_cathy_jade45 with dissolve
        ca "It seems I can relate to your situation well. In a sense, I'm lucky I quit my job."
    else:
        scene ep11_cathy_jade38 with dissolve
        ja "Damn [name] and his smooth talk..."
        ja "*{i}Sigh{/i}* Such a typical frat guy; only looking for one thing."
    scene ep11_cathy_jade47 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade46 with dissolve
    if ep10_cathy_lewd:
        ca "He's good in bed, isn't he?"
    else:
        ca "How is he in bed?"
    scene ep11_cathy_jade39 with dissolve
    if ep4_toldDerekAboutJade:
        ja "One of the best lays I have ever had. But sadly, he turned out to be the most expensive one, too."
    else:
        ja "One of the best lays I ever had."
    stop music fadeout 3
    scene ep11_cathy_jade48 with dissolve
    ca "Hahaha!"
    scene ep11_cathy_jade52 with dissolve
    $ renpy.pause()
else:
    scene ep11_cathy_jade5 with dissolve
    ja "Stephen has already agreed to split everything down the middle."
    scene ep11_cathy_jade21 with dissolve
    ca "That's good news, isn't it?"
    scene ep11_cathy_jade5 with dissolve
    ja "He called 50%% a small price to get rid of me. Can you believe that?"
    scene ep11_cathy_jade23 with dissolve
    ca "What an asshole!"
    scene ep11_cathy_jade24 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade25 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade10 with dissolve
    ja "It makes me want to take everything he's got because that's what it feels like he's doing to me by dissolving our marriage."
    scene ep11_cathy_jade26 with dissolve
    ca "As your friend, I will always support you, regardless of what you choose."
    ca "But do you want to go through a nasty divorce like that?"
    scene ep11_cathy_jade11 with dissolve
    ja "I want him to hurt as much as he hurt me."
    scene ep11_cathy_jade26 with dissolve
    ca "I understand that you're feeling angry."
    scene ep11_cathy_jade10 with dissolve
    ja "That's putting it mildly. I've had to put up with Stephen cheating on me, and now he decides to leave me all of a sudden."
    ja "For what!?"
    scene ep11_cathy_jade26 with dissolve
    ca "I don't know, darling. Do you think it's for someone else?"
    scene ep11_cathy_jade12 with dissolve
    $ renpy.pause()
    scene ep11_cathy_jade13 with dissolve
    ja "Why would you ask that?"
    scene ep11_cathy_jade27 with dissolve
    ca "You said he's been cheating on you. Do you know with whom?"
    scene ep11_cathy_jade14 with dissolve
    ja "It's irrelevant."
    if ep4_fuckedJade:
        ja "And it's not like he was the only one who cheated in our relationship."
        scene ep11_cathy_jade27 with dissolve
        ca "No... You didn't?"
        scene ep11_cathy_jade15 with dissolve
        ja "Sure did... And I could get fired for it, too."
        scene ep11_cathy_jade26 with dissolve
        ca "Wait... That means... You had sex with a student?"
        scene ep11_cathy_jade16 with dissolve
        ja "With [name]."
        scene ep11_cathy_jade28 with dissolve
        ca "[name]!?"
        scene ep11_cathy_jade16 with dissolve
        ja "I ravished him in our car, marital bed and bathroom..."
        jump ep11_cathy_jade2_label
    stop music fadeout 3
    ja "If I had a way to prove that he was unfaithful, I'd ruin him without hesitation."
    scene ep11_cathy_jade29 with dissolve
    $ renpy.pause()

show screen new_phone_screen
if branchIsabella:
    jump ep11_bella_home_label

label ep11_diary_label:
play music "music/ep_interlude/licensed_music/track100.mp3"
scene ep11_diary1 with wipeleft
$ renpy.pause()
scene ep11_diary2 with dissolve
de "Your mom!"
mc "That's your answer to everything."
scene ep11_diary4 with dissolve
de "If you don't know the answer, you might as well make your attempt entertaining."
scene ep11_diary5 with dissolve
mc "I'd love to watch you on one of these shows."
scene ep11_diary4 with dissolve
de "I'd kill it."
scene ep11_diary5 with dissolve
mc "Yeah, you'd kill it for sure. The entire show would get canceled."
scene ep11_diary6 with dissolve
de "What are you studying?"
scene ep11_diary7 with dissolve
mc "I'm not studying anything. I'm reading Mom's diary."
scene ep11_diary6 with dissolve
de "Did she write a diary?"
scene ep11_diary7 with dissolve
mc "Yeah. Reading how she met Dad through her words and thoughts is a lot of fun."
scene ep11_diary8 with dissolve
de "It sounds boring."
stop music fadeout 3
scene ep11_diary9 with dissolve
mc "To me, it's not."
play music "music/ep11/licensed_music/track170.mp3"
scene ep11_diary40 with dissolve
mir "Shut up!"
scene ep11_diary44 with dissolve
ln "I will not."
scene ep11_diary40 with dissolve
mir "And by shut up, I mean tell me more."
mir "Did you make out with him?"
scene ep11_diary45 with dissolve
ln "I'm not telling you that."
scene ep11_diary41 with dissolve
mir "Second base, yes or no?"
scene ep11_diary45 with dissolve
ln "Not telling you that either."
scene ep11_diary42 with dissolve
mir "Did you...fuck him?"
scene ep11_diary46 with dissolve
ln "Where did that come from!?"
scene ep11_diary43 with dissolve
mir "You did! You so did!"
scene ep11_diary47 with dissolve
ln "Never did. Not even once."
scene ep11_diary42 with dissolve
mir "You should. Who are you saving yourself for?"
scene ep11_diary47 with dissolve
ln "I'm not saving myself for someone; it just hasn't happened yet."
scene ep11_diary48 with dissolve
mir "But you think it will happen with him, right?"
scene ep11_diary49 with dissolve
ln "Uh..."
scene ep11_diary50 with dissolve
mir "Oh! That's him, isn't it!?"
scene ep11_diary51 with dissolve
ln "Don't stare at him."
scene ep11_diary50 with dissolve
mir "Oh my God! He's so hot in his uniform."
scene ep11_diary52 with dissolve
ln "Uniform? He's a carpenter, not a cop."
scene ep11_diary83 with dissolve
$ renpy.pause()
play sound "sound_effects/shove.mp3"
scene ep11_diary53 with vpunch
ln "Get down!"
mir "Ah!!!"
scene ep11_diary54 with dissolve
mir "Hahaha! What are you doing? He saw us!"
ln "God, you're so embarrassing!"
scene ep11_diary55 with dissolve
mir "Like you haven't snuck peeks."
scene ep11_diary56 with dissolve
ln "Yeah, and he already caught me doing it once. Now, it's twice."
scene ep11_diary55 with dissolve
mir "That's good. Then he knows you're interested."
mir "How was the date?"
scene ep11_diary56 with dissolve
ln "It was fine."
scene ep11_diary57 with dissolve
mir "Just fine?"
scene ep11_diary60 with dissolve
ln "Great?"
scene ep11_diary58 with dissolve
mir "Was it?"
scene ep11_diary60 with dissolve
ln "I don't know how to describe it. We went into town and had hot dogs."
scene ep11_diary58 with dissolve
mir "I knew you ate sausage. How big was he?"
scene ep11_diary61 with dissolve
ln "Haha! You're the worst!"
scene ep11_diary62 with dissolve
ln "I did nothing of the sort. We talked and took a stroll together."
ln "We ate some hot dogs, and he drove me back home."
scene ep11_diary59 with dissolve
mir "Seriously? Is that all you did?"
scene ep11_diary60 with dissolve
ln "Yes?"
scene ep11_diary59 with dissolve
mir "Not even a kiss?"
scene ep11_diary63 with dissolve
ln "We were going to kiss when he dropped me off, but..."
scene ep11_diary59 with dissolve
mir "You chickened out?"
scene ep11_diary63 with dissolve
ln "Dad showed up. And I wasn't going to kiss in front of him."
scene ep11_diary64 with dissolve
mir "Ok, I'll give you a pass for that."
scene ep11_diary66 with dissolve
ln "Dad was being curt with Neil, too. He did not like that I went for a ride with him."
scene ep11_diary65 with dissolve
mir "Maybe he thought you did more than that?"
scene ep11_diary66 with dissolve
ln "It doesn't matter what he thinks. It's none of his business."
scene ep11_diary65 with dissolve
mir "Actually, it kinda is. He's hired the guy to do a job, no?"
mir "And now the hired help is feeling up his daughter. That's more than he bargained for."
scene ep11_diary66 with dissolve
ln "Whose side are you on?"
scene ep11_diary65 with dissolve
mir "I'm just saying that's how daddies are. You have to be more discreet with Neil."
mir "Don't make out in front of your home. At the very least, sneak him into your room before you do."
scene ep11_diary67 with dissolve
ln "Is that what you would have done?"
scene ep11_diary68 with dissolve
mir "Me? Nope. I would have stopped that van of his in the middle of the woods and worn his helmet."
scene ep11_diary70 with dissolve
ln "Why would you wear his helmet?"
scene ep11_diary69 with dissolve
mir "Because Mom taught me I should always wear protection."
scene ep11_diary71 with dissolve
ln "Hahaha!"
scene ep11_diary72 with dissolve
ln "So, I took some of Miranda's advice."
ln "Well... Not the helmet part. And I didn't have any other protection either."
ln "But that didn't matter because I only snuck him into my room to make out with him."
scene ep11_diary73 with dissolve
ln "Hurry! Close the door."
show ep11_diary74
if not persistent.ep11_cardly12:
    show screen ep11_render_screen("ly12")
with dissolve
dad "*{i}Smack smack{/i}*"
show ep11_diary75
hide screen ep11_render_screen
with dissolve
dad "Your lips are just the best..."
scene ep11_diary76 with dissolve
ln "*{i}Smack{/i}* Mmm... Neil..."
scene ep11_diary77 with dissolve
dad "I've wanted to kiss you since the day we met."
scene ep11_diary78 with dissolve
ln "I can't say the same. You were annoying as hell."
scene ep11_diary77 with dissolve
dad "Do you still think I'm annoying?"
scene ep11_diary78 with dissolve
ln "Obviously not."
ln "We can make out, but you have to be quiet when talking. They might overhear us if we're too loud."
scene ep11_diary77 with dissolve
dad "Don't worry. I don't intend to talk a lot."
scene ep11_diary76 with dissolve
"*{i}Smack{/i}*"
scene ep11_diary79 with dissolve
$ renpy.pause()
scene ep11_diary80 with dissolve
$ renpy.pause()
scene ep11_diary81 with dissolve
ln "Yeah... About the damned protection... Just like with a helmet, the moment you realize you need one is when it's too late."
scene ep11_diary82 with dissolve
ln "But I figured I was late enough in my cycle, so I went with it."
stop music
scene ep11_diary10
mc "Uh..."
play music "music/ep_interlude/licensed_music/track100.mp3"
scene ep11_diary3 with dissolve
de "Your mom!"
scene ep11_diary11 with dissolve
mc "..."
de "What's wrong?"
scene ep11_diary12 with dissolve
mc "Mom and Dad are having sex..."
scene ep11_diary13 with dissolve
de "I hate to break it to you, but that's what moms and dads do."
de "You see, the man inserts his penis into the woman's vagina-"
scene ep11_diary14 with dissolve
mc "In the diary, bro... She's describing the first time they fucked. I can't read this."
scene ep11_diary15 with dissolve
de "Let me see it."
scene ep11_diary16 with dissolve
mc "No!"
scene ep11_diary15 with dissolve
de "Why not?"
scene ep11_diary16 with dissolve
mc "I don't think my no requires an explanation."
scene ep11_diary17 with dissolve
tv "I'm sorry. The answer we were looking for was \"Your mom\"."
scene ep11_diary18 with dissolve
de "No fucking way!"
scene ep11_diary15 with dissolve
de "Come on. Let me read it."
scene ep11_diary16 with dissolve
mc "No."
scene ep11_diary15 with dissolve
de "So, you're gonna read it yourself?"
scene ep11_diary16 with dissolve
mc "I'm not reading it at all."
scene ep11_diary15 with dissolve
de "Then, how will you know how far along to skip forward? Maybe the nasty stuff keeps going?"
scene ep11_diary19 with dissolve
mc "..."
scene ep11_diary15 with dissolve
de "Let me read it. I can tell you where it ends."
scene ep11_diary16 with dissolve
mc "I swear... If you ever tell anyone about this..."
scene ep11_diary20 with dissolve
de "Yeah, yeah. It's just some text on a page. How graphic can it be?"
scene ep11_diary21 with dissolve
$ renpy.pause()
scene ep11_diary22 with dissolve
menu:
    "See what Derek reads":
        stop music fadeout 3
        label ep11_diary_lewd_label:
        if _in_replay:
            hide screen new_phone_screen
        play music "music/ep1/slow_day_blues.mp3"
        scene ep11_diary84 with dissolve
        ln "We were naked and embracing as he put his finger inside me."
        scene ep11_diary85 with dissolve
        ln "I gasped, partly because I wasn't prepared for it and also because of how good it felt."
        scene anim_lynette_finger_ep11 with dissolve
        ln "I've done it plenty of times with my fingers, but having someone else inside me was an unreal sensation."
        ln "He even knew how to do it well... I didn't want to ask if he had done it before, and I didn't have to."
        ln "His confidence showed me that he knew what he was doing to my body."
        scene anim_lynette_finger2_ep11 with dissolve
        ln "His thick finger penetrated me as he kissed my lips. I could have orgasmed right then and there, but I tried my best to hold it back."
        ln "This wasn't how I pictured my first time being at all. Based on what my friends told me, it was supposed to be an awkward moment with a guy who lasts inside you for a few minutes."
        ln "My first time with Neil was nothing like that."
        scene ep11_diary86 with dissolve
        ln "I admit, I was nervous as I felt his warm cock down there. At first, I didn't even want to look at it."
        ln "We both knew it was down there between us, and no piece of fabric was holding it back."
        scene ep11_diary87 with dissolve
        ln "He put his cock between my legs and slowly pushed his pelvis toward mine."
        ln "I could feel it starting to enter me."
        scene ep11_diary88 with dissolve
        ln "He looked into my eyes as if to check if I was ok."
        ln "I nodded without saying a word."
        scene ep11_diary90 with dissolve
        ln "He grabbed my butt with a firm grip and continued to push his cock deeper inside me."
        scene ep11_diary89 with dissolve
        ln "It was ecstasy..."
        ln "He was way thicker than a finger or two. I could feel how I wrapped perfectly around his cock."
        scene ep11_diary91 with dissolve
        ln "What was a few seconds felt like a minute. I thought his cock would never end."
        ln "But as our hip bones almost touched, it was fully inside me."
        scene ep11_diary92 with dissolve
        ln "He asked me if it hurt, but it didn't."
        ln "At that moment, all I could think about was that I wasn't a virgin anymore."
        scene ep11_diary91 with dissolve
        ln "He pulled it out and slowly went back deep inside."
        ln "Gone was the friction that I felt with the first thrust. The second thrust felt even better."
        scene anim_lynette_side_ep11 with dissolve
        ln "I was wetter, and his cock became more slippery."
        ln "As he continued to thrust, I got used to the great sensation."
        ln "So, this was what sex is about? It was amazing."
        scene anim_lynette_ride_ep11 with dissolve
        ln "He pulled me on top of him, and at this point, I felt exposed. I thought he expected me to take control, but I didn't know what to do."
        ln "But he didn't allow me to feel uncomfortable. He helped me create this wave-like motion between our hips."
        ln "It was like riding a horse, and I sure knew how to do that."
        ln "I could see how he enjoyed himself as I rode him. He gave me a look that I had never seen on anyone before."
        scene anim_lynette_ride2_ep11 with dissolve
        ln "His peaceful eyes gazed into mine as we enjoyed each others' bodies."
        ln "I loved how he looked at me, so I wanted to show him how much I liked it."
        ln "I started riding him faster and pushed harder down on him."
        ln "This time, I made him gasp, haha. I still feel proud of shocking him like that."
        ln "I'm sure he didn't expect me to be this good at it. I definitely didn't expect it."
        scene anim_lynette_ride3_ep11 with dissolve
        ln "I rode him even harder. And I could feel how something started building up inside of me."
        ln "Holy hell, I was going to orgasm on him. I was going to reach climax from my first time having sex."
        ln "Miranda told me guys don't know how to make girls do that. But here I am, about to do it."
        scene ep11_diary93 with vpunch
        ln "And as I came..."
        scene ep11_diary95 with vpunch
        ln "He came too!"
        scene ep11_diary96 with vpunch
        ln "Warmth filled me... I couldn't comprehend what was happening."
        ln "My mind was so focused on my orgasm that it took me a while to realize he had come, too."
        stop music fadeout 3
        scene ep11_diary94 with dissolve
        ln "I let him orgasm inside me..."
        $ renpy.end_replay()
        $ persistent.ep11_lewd_lynette = True
        $ calcScenes()
        play music "music/ep_interlude/licensed_music/track100.mp3"
    "Skip it":
        $ renpy.pause(0.5)
play sound "sound_effects/cellphone.mp3"
scene ep11_diary23 with dissolve
"*{i}Phone rings{/i}*"
scene ep11_diary24 with dissolve
mc "Hello?"
scene ep11_diary33 with dissolve
zo "Yo! It's me."
scene ep11_diary24 with dissolve
mc "Hey! What's up?"
scene ep11_diary34 with dissolve
zo "Not much... You?"
scene ep11_diary25 with dissolve
mc "Uh... We're...um..."
scene ep11_diary27 with dissolve
de "Holy fuck! Lynette sure knows how to paint a picture with her words."
scene ep11_diary28 with dissolve
mc "Not much here either."
scene ep11_diary34 with dissolve
zo "Cool... Let's get together soon and hang out."
scene ep11_diary24 with dissolve
if ep10_zoey_hangout:
    mc "Uh... Yeah, sure. Why not?"
    mc "It's a busy month for me, though."
else:
    mc "Uh... I'm not feeling it."
    mc "And it's a busy month for me."
scene ep11_diary35 with dissolve
zo "I get it, but still... I need to see you."
scene ep11_diary25 with dissolve
mc "Is something wrong?"
scene ep11_diary35 with dissolve
zo "It's a face-to-face kind of talk."
scene ep11_diary24 with dissolve
mc "We're having another party soon, would that work?"
scene ep11_diary36 with dissolve
zo "Yeah, a party would be great!"
scene ep11_diary25 with dissolve
mc "There's this theme to it..."
scene ep11_diary36 with dissolve
zo "Cool, another dress-up party?"
scene ep11_diary26 with dissolve
mc "More like dress-down... It's underwear only."
scene ep11_diary36 with dissolve
zo "Alright. Makes sense."
scene ep11_diary37 with dissolve
mc "It does?"
scene ep11_diary38 with dissolve
zo "Haha, hell no. What the hell is wrong with you? Is everyone gonna be in their underwear?"
scene ep11_diary26 with dissolve
mc "I know. But it's a theme, and the DIKs had it in the past. Plus, it's a cold month."
scene ep11_diary38 with dissolve
zo "And what does that have to do with anything?"
scene ep11_diary25 with dissolve
mc "I don't know, but that's what they told me when I asked why."
scene ep11_diary36 with dissolve
zo "Do I have to show up in my underwear, or I can't come?"
scene ep11_diary24 with dissolve
mc "I think most will dress up - or down - when they get here. And we'll have masks to cover your face."
mc "Look, you don't have to come."
scene ep11_diary39 with dissolve
zo "If you're busy and can't see me, you're not leaving me with much choice."
zo "If I skip eating a meal daily, I should be fit by the time of the party."
scene ep11_diary24 with dissolve
if ep10_zoey_hangout:
    mc "It's up to you. Or we can find another day for it...somehow."
else:
    mc "It's up to you."
scene ep11_diary36 with dissolve
zo "I'll be there."
scene ep11_diary24 with dissolve
mc "Talk soon, then."
scene ep11_diary29 with dissolve
de "[mc_de_up]... I was wrong about this diary. It's not boring...it's a treasure."
scene ep11_diary30 with dissolve
mc "Are you done?"
scene ep11_diary29 with dissolve
de "Yeah... I left it on the page you wanted me to."
scene ep11_diary31 with dissolve
de "I need to take a dump. Don't wait for me."
scene ep11_diary32 with dissolve
stop music fadeout 3
mc "Ugh... Gross."
$ new_bio("Zoey", "I invited Zoey to the DIKs' Christmas Panty party. She wanted to talk to me about something important.")
$ new_bio("Lynette", "Mom wrote about losing her virginity to Dad. Gross!")

label ep11_pr_label:
hide screen new_phone_screen
play music "music/ep10/licensed_music/track142.mp3"
scene ep11_pr1
show screen dance_filter_screen
with wipeleft
uk "Hey! How about a dance?"
scene ep11_pr2 with dissolve
ly "Sure."
scene ep11_pr3 with dissolve
$ renpy.pause()
scene ep11_pr7 with dissolve
$ renpy.pause()
scene ep11_pr4 with dissolve
ly "What are you doing here?"
scene ep11_pr8 with dissolve
vi "Damn, that's cold. Is that how you treat all your customers?"
scene ep11_pr4 with dissolve
ly "Only the ones I know won't pay. You're not here for a dance, so cut the bullshit."
scene ep11_pr9 with dissolve
vi "You lied to me, Lily. I know everything. I know about you and Quinn, and how you switched from me to her."
scene ep11_pr5 with dissolve
ly "No, I never did."
scene ep11_pr9 with dissolve
vi "And you're still lying."
vi "Quinn told my supplier that's what happened. She claimed I was overcharging, and I know she meant I overcharged you."
scene ep11_pr11 with dissolve
vi "As you can tell, he didn't like that news. And neither do I."
scene ep11_pr5 with dissolve
ly "What? Did he do something to your face? I can't tell. You were always an ugly bastard."
scene ep11_pr9 with dissolve
vi "We worked it out. And so will you girls and me."
scene ep11_pr4 with dissolve
ly "Sorry, but there's nothing to work out here. We're done doing business with each other. I'm getting back to work."
scene ep11_pr9 with dissolve
vi "And do you think your deal with Quinn will last when I tell my guys what you've been up to? You're trying to undercut my supplier. *{i}Tsk tsk{/i}*"
scene ep11_pr5 with dissolve
ly "Do you know how I know you're lying?"
ly "Your mouth is making noise."
scene ep11_pr10 with dissolve
vi "Either you girls buy from me again, or you all get what's coming to you."
vi "Go ahead and test me. I'd fucking love it."
scene ep11_pr6 with dissolve
ly "..."
stop music fadeout 3
scene ep11_pr8 with dissolve
vi "Now, how about that dance?"
hide screen dance_filter_screen

if branchMayaJosy:
    show screen new_phone_screen
    
    if persistent.mod_wtenabled:
        menu:
             "Mod: Both":
                $ wt_ep11_maya_josy = True
                jump ep11_jsolo_label
             "Spend time with Josy":
                jump ep11_jsolo_label
             
             "Spend time with Maya":
             
                jump ep11_msolo_label
             
    if check_jm_solo_ep11() == "Maya":
        jump ep11_msolo_label
    else:
        jump ep11_jsolo_label
elif branchIsabella or branchJill:
    show screen new_phone_screen
    jump ep11_trip_label
else:
    jump ep11_franz_label

label ep11_franz_label:
$ guideSuggestedPage = 180
hide screen new_phone_screen
play music "music/ep6/licensed_music/track35.mp3"
scene ep11_franz1
hide screen ep10_snow_screen
with wipeleft
$ renpy.pause()
scene ep11_franz2 with dissolve
li "Franz was a bunny. But to many of us, Franz was more than that. Franz was a friend."
scene ep11_franz3 with dissolve
li "A friend who left us fast, but other friends left us faster."
scene ep11_franz4 with dissolve
li "Like some other {i}friend{/i} who left you alone at the table when you hadn't finished eating at Burgers and Burgers."
scene ep11_franz9 with dissolve
suz "Again, with this!? You came 40 minutes late and expected me to stay while you chowed down a truckload?"
scene ep11_franz8 with dissolve
li "It wasn't a truckload, Suzy! It was dinner, and I had a low blood sugar level!"
scene ep11_franz12 with dissolve
wen "Can you guys stop? Today isn't about you; it's about Franz."
scene ep11_franz7 with dissolve
$ renpy.pause()
scene ep11_franz10 with dissolve
dn "*{i}Sobs{/i}*"
scene ep11_franz3 with dissolve
li "Franz was a bunny."
scene ep11_franz9 with dissolve
suz "You said that already."
scene ep11_franz8 with dissolve
li "It's another paragraph! Can someone shut her the hell up?"
scene ep11_franz5 with dissolve
li "Franz was a bunny..."
scene ep11_franz3 with dissolve
li "Franz wasn't big, nor did Franz weigh much. But Franz had a big place in our hearts."
li "Franz will be sorely missed."
scene ep11_franz6 with dissolve
li "Dany? Do you wanna say some words about Franz?"
scene ep11_franz11 with dissolve
dn "I can't... *{i}Sobs{/i}*"
scene ep11_franz13 with dissolve
jm "I can say some words if that's ok."
scene ep11_franz14 with dissolve
$ renpy.pause()
scene ep11_franz15 with dissolve
$ renpy.pause()
scene ep11_franz16 with dissolve
jm "Franz was my furry little buddy. I liked him a lot."
jm "I never had a bunny in my life before, but it was kinda cool."
scene ep11_franz17 with dissolve
jm "I remember everything Dany and I used to do with Franz."
jm "We put him on the floor and let him roam the room in this maze we built out of books."
scene ep11_franz18 with dissolve
jm "He ended up taking a dump on one of my algebra books, and that's when I knew I liked him. He hated math like most of us do."
scene ep11_franz17 with dissolve
jm "At parties, I checked up on him to make sure he was feeling ok."
jm "The loud noise seemed to stress him out at times; his feet kept going - smacking fast and hard onto the floor. But I felt like he was ok when I was with him."
jm "I sat beside him and drank beer while he sipped water from his bowl."
scene ep11_franz18 with dissolve
jm "And not that long ago, we even shared a burger. Haha!"
scene ep11_franz23 with dissolve
dn "You fed Franz a burger?"
scene ep11_franz19 with dissolve
jm "No, no. I didn't feed him the whole burger - just some leftover burger I found in here."
show ep11_franz22
if not persistent.ep11_cardly13:
    show screen ep11_render_screen("ly13")
with dissolve
li "My burger!?"
show ep11_franz20
hide screen ep11_render_screen
with dissolve
jm "He started nibbling on some of the lettuce."
scene ep11_franz23 with dissolve
dn "The iceberg lettuce!? You're not supposed to feed Franz that!"
scene ep11_franz19 with dissolve
jm "I mean...it wasn't a lot of lettuce."
jm "If anything, he ate more of the beef and onions than the lettuce."
scene ep11_franz23 with dissolve
dn "Oh my God... It was you. You killed Franz!"
scene ep11_franz19 with dissolve
jm "Huh?"
scene ep11_franz24 with dissolve
dn "You murderer!"
scene ep11_franz21 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep11_franz25 with dissolve
mi "Get him!!!"

label ep11_gym_label:
if not minigames:
    hide screen new_phone_screen
    play music "music/ep11/licensed_music/track171.mp3"
    jump brawler_story_dwyane1_label
show screen new_phone_screen
play music "music/ep11/licensed_music/track171.mp3"
label ep11_after_spar_label:
play sound "sound_effects/clang.mp3"
scene ep11_gym17 with vpunch
cf "AHHHH!!!!"
scene ep11_gym18 with dissolve
cf2 "THAT'S RIGHT! YOU'RE NOT WORKING OUT IF YOU AREN'T SLAMMING YOUR WEIGHTS ONTO THE FLOOR WITH ALL YOUR MIGHT!"
cf2 "LET EVERYONE AT THE GYM HEAR THAT YOU ARE HERE!"
scene ep11_gym1 with dissolve
dwy "Man, I don't know what's worse - vegans or crossfitters."
scene ep11_gym2 with dissolve
chao "Hahaha! I can't wait for the day you get your first crossfitter client."
chao "If it's a vegan one, too, I'd happily pay for his fees."
scene ep11_gym19 with dissolve
mc "Why is he running back and forth with a weight over his head like that?"
dwy "You haven't seen anything yet. They have some good exercises, but most are like they were high while making them up."
mc "It sounds like you can't stand them."
scene ep11_gym1 with dissolve
dwy "Eh. Gym aside, they're all right. It's not like they're rude."
dwy "And I don't need to hate on them. I get my kicks from watching them go head-to-head with the bodybuilders."
scene ep11_gym20 with dissolve
cf "NO! I AM USING THOSE!"
scene ep11_gym21 with dissolve
jo "I'm so fucking tired of you guys hogging equipment!"
jo "How are you using it? How!? What kind of exercise would you even use two unloaded barbells for?"
scene ep11_gym20 with dissolve
cf "YOU NEED A RUBBERBAND TO UNDERSTAND WHY."
scene ep11_gym22 with dissolve
jo "..."
scene ep11_gym21 with dissolve
jo "What!?"
scene ep11_gym3 with dissolve
chao "So, [name]... Are you entering the December tournament?"
scene ep11_gym4 with dissolve
mc "There's a tournament?"
scene ep11_gym3 with dissolve
chao "Competitions are held every month. All members are free to sign up for them."
scene ep11_gym5 with dissolve
dwy "And required to help out before and after. It will eat up your time."
scene ep11_gym6 with dissolve
chao "You don't have to undersell it."
scene ep11_gym5 with dissolve
dwy "My boy needs to know all the details, not just the fun parts."
scene ep11_gym4 with dissolve
menu:
    "[m_c1]I'm interested":
        $ ep11_fighter = True
        mc "All of it sounds fun to me. But, fuck... December is a busy month for me."
        scene ep11_gym3 with dissolve
        chao "You don't have to join in December."
        scene ep11_gym4 with dissolve
        mc "I could make time for it at the expense of my studies, though..."
        mc "But then there's the membership fee... Honestly, it's too expensive for me."
        scene ep11_gym5 with dissolve
        dwy "The cheapest membership is $750. You on the Bronze gym plan?"
        scene ep11_gym7 with dissolve
        mc "Silver."
        scene ep11_gym5 with dissolve
        dwy "Silver? I thought you were bronze."
        scene ep11_gym7 with dissolve
        mc "Bronze had some restrictions that didn't work for me. Silver wasn't much extra, so it made it the obvious choice."
        scene ep11_gym5 with dissolve
        dwy "For a student with a Silver membership, it's just $300. That's like $30 per month."
        scene ep11_gym6 with dissolve
        chao "Excuse Dwyane's poor math. It would be $25 per month."
        scene ep11_gym5 with dissolve
        dwy "That's the point I'm making. You can't spare $25 per month? Cut back on something else to make up for it."
        dwy "Don't have those pizzas or go to that movie. There's your $25."
        scene ep11_gym8 with dissolve
        mc "..."
        scene ep11_gym9 with dissolve
        mc "Ok. I wanna do it."
        scene ep11_gym10 with dissolve
        dwy "That's my boy."
        scene ep11_gym11 with dissolve
        chao "I'll sign you up."
        scene ep11_gym12 with dissolve
        mc "When's the competition?"
        scene ep11_gym11 with dissolve
        chao "On the 29th."
        scene ep11_gym12 with dissolve
        mc "Oh, that's better for me than I thought it would be."
        scene ep11_gym13 with dissolve
        dwy "I'll walk you through it another time."
        $ new_bio("You", "Dwyane asked me to join a fighting competition in December, and I said I was interested.")
    "I'm not interested":
        $ ep11_fighter = False
        mc "It sounds fun, but December is a busy month for me."
        scene ep11_gym3 with dissolve
        chao "You don't have to join in December; it can be later."
        scene ep11_gym4 with dissolve
        mc "Yeah, but I'd have to pay for the membership. It's too expensive."
        mc "And I am not looking to compete either. That's not what I'm training for."
        scene ep11_gym11 with dissolve
        chao "Fair enough."
        chao "You're welcome to watch. Maybe it will make you change your mind."
        scene ep11_gym12 with dissolve
        mc "Thanks for the invite."
        $ new_bio("You", "Dwyane asked me to join a fighting competition in December, and I said I wasn't interested.")
scene ep11_gym9 with dissolve
mc "It's been fun today. I'm gonna head off."
if ep11_fighter:
    scene ep11_gym14 with dissolve
    dwy "Remember! Cut back on shit so you can afford it. I'll work on a plan to prepare you for the 29th."
    scene ep11_gym15 with dissolve
    dwy "Don't you think it's too early for him to compete?"
    scene ep11_gym16 with dissolve
    chao "I lost my first five matches. My father thought it was too early for me, too."
    chao "He was wrong. I learned more during those five matches than I would have without them."
    chao "It's never too early."
else:
    scene ep11_gym14 with dissolve
    dwy "Good work today."

scene ep11_gym23 with dissolve
sar "[name]... What did you do?"
scene ep11_gym24 with dissolve
mc "From the sound of it... I did something. Why don't you tell me what I did?"
scene ep11_gym25 with dissolve
he "You ruined yoga for us."
scene ep11_gym24 with dissolve
if affinity == "DIK":
    mc "I know you guys miss me when I'm not around, but don't let that ruin yoga for you."
else:
    mc "Huh? How did I ruin it? I went there once."
scene ep11_gym26 with dissolve
sar "You told your friends about it."
scene ep11_gym24 with dissolve
mc "Yeah? So?"
scene ep11_gym26 with dissolve
sar "Really? So?"
show ep11_gym31
$ renpy.sound.set_volume(0,channel='music')
$ renpy.music.play("music/ep4/fluffing_a_duck.mp3", channel="music2")
if not persistent.ep11_cardly14:
    show screen ep11_render_screen("ly14")
pau "Breathe in. And breathe out."
show ep11_gym33
hide screen ep11_render_screen
with dissolve
le "Dude, look at Sarah."
scene ep11_gym32 with dissolve
jb "Wow, she's got a nice ass!"
jac "[name] was on the money with this class."
le "Remind me to thank him later."
scene ep11_gym33 with dissolve
le "Guys. Guys. Check Camila out."
$ renpy.music.stop(channel="music2", fadeout=0)
$ renpy.sound.set_volume(1.0,channel='music')
scene ep11_gym24
mc "Haha! They went there?"
scene ep11_gym25 with dissolve
he "They weren't participating and kept saying they were rookies and needed to learn."
scene ep11_gym24 with dissolve
mc "I didn't put them up to it."
scene ep11_gym26 with dissolve
sar "Doesn't matter. You ruined it."
sar "What's something you like? I wanna ruin it for you."
scene ep11_gym24 with dissolve
if affinity == "DIK":
    mc "Orgasms."
    scene ep11_gym27 with dissolve
    sar "Hahaha! Didn't even skip a beat."
    sar "I would ruin that for you."
else:
    mc "Nice try. I'm not sharing."
if ep11_jade_care:
    scene ep11_gym28 with dissolve
else:
    scene ep11_gym28b with dissolve
if not ep11_camila_lewd:
    stop music fadeout 3
mc "Well... I'm sorry, but I didn't put them up to it. I'll ask them to stop showing up."
scene ep11_gym29 with dissolve
$ renpy.pause()
if ep11_camila_lewd:
    stop music fadeout 3
    scene ep11_gym30 with dissolve
    cam "*{i}Smack{/i}*"

$ new_bio("Sarah", "Sarah told me I had ruined yoga by telling the DIKs about my experience.")
$ new_bio("Leon", "Leon went to yoga class to check out girls.")
$ new_bio("John Boy", "John Boy went to yoga class to check out girls.")
$ new_bio("Jacob", "Jacob went to yoga class to check out girls.")

if branchAlone and jade_state == 1 and ep11_jade_care:
    jump ep11_jade_pre_lewd_label

elif branchMayaJosy:
    jump ep11_jm_prelewd_label

elif branchSage:
    jump ep11_ssolo_label

label ep11_math_label:
play music "music/ep11/licensed_music/track172.mp3"
scene ep11_math1 with wipeleft
$ renpy.pause()
if branchMayaJosy:
    scene ep11_math2 with dissolve
    cam "Josy, are you ok? You're walking funny."
    scene ep11_math3 with dissolve
    js "I...uh... Sprained my ankle."
    scene ep11_math4 with dissolve
    mc "*{i}Whispers{/i}* I didn't know your ankle was in your asshole."
    scene ep11_math5 with dissolve
    js "Shush!!!"
    scene ep11_math6 with dissolve
    mc "I'm not sitting with you today. I want to have a full side view."
    if ep11_josy_dare:
        scene ep11_math7 with dissolve
        js "Don't go too crazy with it. Promise."
        scene ep11_math6 with dissolve
        mc "Remember what to say. \"This problem is too hard.\""
        scene ep11_math7 with dissolve
        js "Damn you."
    else:
        scene ep11_math8 with dissolve
        my "Is it too late to back out of the dare?"
        scene ep11_math6 with dissolve
        mc "Remember what to say. \"This problem is too hard.\""
        scene ep11_math8 with dissolve
        my "This is plain wrong, [name]."

scene ep11_math9 with dissolve
de "[mc_de_up], I can't wait for the party tonight. I even bought a new pair of underwear for it."
scene ep11_math10 with dissolve
mc "That's good. The last thing you wanna wear tonight is underwear with skid marks."
scene ep11_math9 with dissolve
de "Totally. And whites are off the table, too."
de "What's the headcount for the party?"
scene ep11_math10 with dissolve
mc "Worse than I had hoped. Half of the HOTs aren't even showing, and since I planned to steal them from the jocks before their party tomorrow..."
mc "What will the party be like without them?"
scene ep11_math11 with dissolve
de "Wait. Who's not coming?"
scene ep11_math12 with dissolve
mc "Sage, Maya, Josy and Jill are hanging out at Bella's tonight. So, they're all out."
mc "Riona is still sick, and I don't think Heather will show up."
scene ep11_math13 with dissolve
de "What about other girls? Who did you invite?"
scene ep11_math12 with dissolve
mc "I asked the usuals and extended the invite to friends of friends. So, who knows which dorm girls will show up?"
scene ep11_math13 with dissolve
de "It better be none from our shit list."
scene ep11_math12 with dissolve
mc "I doubt they will show up."
scene ep11_math14 with dissolve
de "You'd make them leave, right?"
scene ep11_math12 with dissolve
mc "It depends on what they have to say."
mc "They did stop putting the posters up."
scene ep11_math14 with dissolve
de "Because they don't want to face any consequences now that they got caught."
scene ep11_math12 with dissolve
mc "Whatever. It's not gonna stop us from having a great time."
scene ep11_math15 with dissolve
de "I'll do my part."
scene ep11_math12 with dissolve
mc "Yeah? Got the bowl ready?"
scene ep11_math15 with dissolve
de "Yep. It's all done. I asked the boys to come up with some ideas for the missions. There were only so many I could think of that didn't involve my penis."
scene ep11_math16 with dissolve
mc "I hope you're joking."
scene ep11_math17 with dissolve
ph "Good morning. It looks like we are a few students short today."
ph "It's ironic how flu season always coincides with the remaining optional recap math classes."
scene ep11_math22 with dissolve
"*{i}Laughter{/i}*"
scene ep11_math23 with dissolve
dw "This was optional?"
scene ep11_math24 with dissolve
$ renpy.pause()
play sound "sound_effects/door_close.mp3"
scene ep11_math18 with dissolve
$ renpy.pause()
scene ep11_math19 with dissolve
ph "It's their loss. They miss out on the festive hat I wear during the last classes before Christmas."
scene ep11_math20 with dissolve
ph "I will go easy on you today. You might not have realized how unusual this semester has been, given that it's the first semester for most of you."
ph "But we made it through the curriculum just in time, and I want to take this opportunity to commend all of you for bearing with me."
ph "You've certainly helped make my job easier."
scene ep11_math21 with dissolve
ph "Today, I will briefly summarize everything you have learned during the semester. If you feel that there's something you don't quite understand from this summary, study it extra."
if not branchMayaJosy and minigames:
    stop music fadeout 3
ph "I hope I'll be able to cover everything today without rushing. Let's dive into it."
$ guideSuggestedPage = 182
if branchMayaJosy:
    scene ep11_math25 with dissolve
    $ renpy.pause()
    scene ep11_math26 with dissolve
    $ renpy.pause()
    if ep11_josy_dare:
        scene ep11_math27 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/vibrator.mp3"
        scene ep11_math28 with vpunch
        "*{i}Vibrating{/i}*"
        scene ep11_math29 with dissolve
        js "Hnn... Mmphf..."
        scene ep11_math30 with dissolve
        my "What's wrong?"
        scene ep11_math31 with dissolve
        my "Haha... Oh..."
        scene ep11_math32 with dissolve
        $ renpy.pause()
        scene ep11_math33 with dissolve
        $ renpy.pause()
        scene ep11_math34 with dissolve
        $ renpy.pause()
        scene ep11_math38 with dissolve
        $ renpy.pause()
        scene ep11_math35 with dissolve
        js "*{i}Breathing heavily{/i}*"
        scene ep11_math36 with dissolve
        $ renpy.pause()
        scene ep11_math37 with dissolve
        $ renpy.pause()
        scene ep11_math39 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/vibrator.mp3"
        scene ep11_math40 with dissolve
        js "Hngn..."
        scene ep11_math41 with dissolve
        $ renpy.pause()
        scene ep11_math42 with dissolve
        $ renpy.pause()
        scene ep11_math43 with dissolve
        js "Hnnn..."
        scene ep11_math44 with dissolve
        js "This problem is too hard."
        scene ep11_math21 with dissolve
        ph "Thank you for letting me know that you're not following along. Let me explain it from the top again."
        scene ep11_math45 with dissolve
        js "Mhm."
        scene ep11_math46 with dissolve
        $ renpy.pause()
        scene ep11_math47 with dissolve
        mc "(Haha, she hit her limit already. I promised I'd stop if she said that...)"
        
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Josy)","(+Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
        
        menu:
            "Honor the safe phrase \n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[2]]":
                $ dk(-1)
                $ RPjosy += 1
                $ ep11_honor_safe_word = True
                scene ep11_math48 with dissolve
                mc "(I'd be an asshole if I didn't. She trusted me and followed through with the dare after all.)"
            "Start the vibrator again \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[3]]":
                $ dk(1)
                $ RPjosy -= 1
                $ ep11_honor_safe_word = False
                mc "(But that playful look in her eyes tells me part of her wants it.)"
                scene ep11_math48 with dissolve
                $ renpy.pause()
                play sound "sound_effects/season2/vibrator.mp3"
                scene ep11_math49 with dissolve
                js "No..."
                scene ep11_math50 with dissolve
                js "Ahh..."
                scene ep11_math51 with dissolve
                js "Ahhhhhh..."
                my "Josy...?"
                scene ep11_math52 with dissolve
                mc "(Uh oh...)"
                scene ep11_math53 with dissolve
                mc "(Whoops.)"
    else:
        scene ep11_math56 with dissolve
        $ renpy.pause()
        play sound "sound_effects/season2/vibrator.mp3"
        scene ep11_math57 with dissolve
        $ renpy.pause()
        scene ep11_math58 with dissolve
        my "Nuh-uh. Nope."
        scene ep11_math59 with dissolve
        js "What?"
        scene ep11_math60 with dissolve
        my "He's doing it."
        my "This game has gotten out of hand."
        scene ep11_math61 with dissolve
        js "You know how to make him stop. Just say that phrase."
        scene ep11_math62 with dissolve
        my "Mhm..."
        js "But maybe you're enjoying it..."
        scene ep11_math63 with dissolve
        my "Shut up, will you? I'm trying to focus."
        scene ep11_math64 with dissolve
        js "*{i}Mouths{/i}* More!"
        play sound "sound_effects/season2/vibrator.mp3"
        scene ep11_math65 with vpunch
        my "Ahhh..."
        scene ep11_math66 with dissolve
        $ renpy.pause()
        scene ep11_math67 with dissolve
        $ renpy.pause()
        scene ep11_math68 with dissolve
        mc "(Wow... She's going with it.)"
        scene ep11_math71 with dissolve
        js "Is he still doing it?"
        play sound "sound_effects/season2/vibrator.mp3"
        scene ep11_math68 with vpunch
        my "*{i}Moans{/i}*"
        scene ep11_math69 with vpunch
        my "Fuck... I'm cumming."
        scene ep11_math70 with dissolve
        my "Hnnnn..."
        scene ep11_math72 with dissolve
        js "*{i}Mouths{/i}* Stop!"
        mc "(Huh?)"
        scene ep11_math73 with dissolve
        mc "(She came? Wow... She didn't even try to stop me, but Josy did.)"
        scene ep11_math74 with dissolve
        $ renpy.pause()
    scene ep11_math55 with dissolve
    ph "[name]? Are you paying attention?"
    if minigames:
        stop music fadeout 3
    scene ep11_math54 with dissolve
    mc "Mhm."

if minigames:
    scene ep10_math17b with dissolve
    $ renpy.pause(1)
    hide screen new_phone_screen
    play music "music/ep3/sing_along_with_jim.mp3"
    $ renpy.block_rollback()
    $ qM = quick_menu
    $ quick_menu = 0
    $ math_jump_label = "after_math_setup_ep11_label"
    jump math_setup_ep11_label
    label after_math_setup_ep11_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_ep11_label"

    show screen math_screen
    $ renpy.pause()

    label after_math_ep11_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_result_ep11_label"
    $ quick_menu = qM
    show screen new_phone_screen
    hide screen math_screen
    hide screen math_tool_tip_screen
    show screen math_result_screen
    $ renpy.pause()
    label after_math_result_ep11_label:
    $ renpy.block_rollback()
    hide screen math_result_screen
    stop music fadeout 3

if minigames:
    scene ep11_math21 with wipeleft
    play music "music/ep11/licensed_music/track172.mp3"
else:
    scene ep11_math19 with fade
ph "All of this will be on the finals."
ph "For most of you, this will be your first finals week. But if you recall the midterms, it should feel familiar."
scene ep11_math20 with dissolve
ph "Now that we have covered everything in the curriculum, the remaining class before the finals will be spent on exercises that further prepare you for the test."
ph "You may think you have ample time to prepare for the finals, but I'd advise you to start studying today."
scene ep11_math21 with dissolve
ph "I've seen many students procrastinate, and procrastination will rarely get you anywhere."
ph "Set a healthy standard for yourself when it comes to your studies. And let that standard be with you for the duration at B&R."
ph "We have too much stress in our lives as it is, and you have the choice to reduce it by studying early."
if branchSage:
    play sound "sound_effects/season2/vibrate.mp3"
    scene ep11_math75 with dissolve
    "*{i}Phone vibrates{/i}*"
    scene ep11_math76 with dissolve
    $ tmpInt = 0
    $ tmpInt2 = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["Sage","Wanna meet up between classes? I could use a hug.",True])
    $ text_message_screen_list.append(["%s" % name,"Sure. Why a hug? Did something happen?",False])
    $ text_message_screen_list.append(["Sage","I miss you. That's all. mphone_emoji_heart",True])
    $ text_message_screen_list.append(["%s" % name,"Meet me at the main entrance in five minutes. mphone_emoji_kiss",False])
    hide screen new_phone_screen
    show screen text_message_screen
    play sound "sound_effects/interlude/zoey_message.mp3"
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    scene ep11_math77 with dissolve
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ mphone_scene_to_chat("Sage",text_message_screen_list)
    show screen new_phone_screen

scene ep11_math20 with dissolve
ph "That's all for today. You are dismissed."

if branchMayaJosy:
    if ep11_josy_dare:
        scene ep11_math78 with dissolve
        if ep11_honor_safe_word:
            js "I'm never doing that again. You have no idea how close I was to cumming."
            scene ep11_math79 with dissolve
            mc "Maybe you didn't want me to stop?"
            scene ep11_math80 with dissolve
            js "I didn't want to cum in class, [name]."
            scene ep11_math81 with dissolve
            mc "Haha!"
            $ new_bio("Josy", "I dared Josy to come to class with a remote-controlled vibrator in her. I respected her when she said the safe phrase.")
        else:
            js "That was so not cool."
            scene ep11_math79 with dissolve
            mc "Come on..."
            scene ep11_math80 with dissolve
            js "Nope. Not cool. You made me cum in class."
            scene ep11_math79 with dissolve
            mc "I'm sorry. It looked like you enjoyed it."
            scene ep11_math80 with dissolve
            js "I was, but... In class, [name]..."
            $ new_bio("Josy", "I dared Josy to come to class with a remote-controlled vibrator in her. I ended up taking it too far, and she had an orgasm in class.")
    else:
        scene ep11_math84 with dissolve
        mc "Hey... Did you cum?"
        scene ep11_math82 with dissolve
        my "Yes. I need to change my underwear."
        scene ep11_math83 with dissolve
        mc "Oh my God..."
        scene ep11_math82 with dissolve
        my "Haha... Yeah."
        $ new_bio("Maya", "I dared Maya to come to class with a remote-controlled vibrator in her. She was supposed to yell a safe phrase when it got too intense, but she never did and ended up having an orgasm.")
$ guideSuggestedPage = 193
if not ep8_recital_failed:
    scene ep11_math85 with dissolve
    ph "[lname]. Can I have a word with you?"
    scene ep11_math86 with dissolve
    mc "Um. Sure."
    scene ep11_math87 with dissolve
    ph "Are you aware that the faculty has an annual Christmas party?"
    scene ep11_math89 with dissolve
    menu:
        "Is this an invitation?":
            mc "Is this an invitation?"
            scene ep11_math88 with dissolve
            ph "Haha. No. Well..."
        "No":
            mc "No, I didn't know that."
    scene ep11_math87 with dissolve
    ph "It's often the highlight of the year for us."
    ph "We eat tasty food, enjoy each other's company, network with select guests and collaborators..."
    ph "...and there's usually some entertainment, too."
    scene ep11_math89 with dissolve
    mc "That sounds great. But what does that have to do with me?"
    scene ep11_math87 with dissolve
    ph "I'm on the party committee this year, and we have arranged the entertainment."
    ph "We have decided to hire musicians for the event and have asked some students to attend."
    ph "Among others, I have asked Ms. Royce to bless us with her piano music, and I wanted to extend that invitation to you - with your guitar, of course."
    scene ep11_math90 with dissolve
    mc "Do you want me to perform for the faculty?"
    scene ep11_math94 with dissolve
    ph "And esteemed guests. Nothing much. I'm thinking a smaller performance of 20 minutes or so should suffice."
    ph "In return, you'd get a meal and $100, but the real treasure is the excellent opportunity to network. Who knows who you might end up impressing?"
    scene ep11_math92 with dissolve
    mc "Oh... It's sudden. I have a lot on my plate in December, as it is, with the finals and all."
    scene ep11_math94 with dissolve
    ph "I understand, but this event is after your finals. But I admit it doesn't leave you much time to prepare."
    scene ep11_math95 with dissolve
    mc "When is it?"
    scene ep11_math94 with dissolve
    ph "On December 29."
    scene ep11_math91 with dissolve
    if ep11_fighter:
        mc "(Crap... That's the date for the fighting competition...)"
        menu:
            "Play guitar at the party":
                $ ep11_music = True
                $ ep11_fighter = False
                mc "(But to hell with that competition, I'd rather perform again.)"
                $ new_bio("You", "I decided to perform at the faculty's Christmas party instead of participating in the fighting competition.")
                jump ep11_math_agree_label
            "Participate in competition":
                $ ep11_music = False
                mc "(And I'd much rather do that.)"
                $ new_bio("You", "I decided to participate in the fighting competition instead of performing at the faculty's Christmas party.")
                jump ep11_math_decline_label
    else:
        menu:
            "Play guitar at the party":
                $ ep11_music = True
                $ new_bio("You", "I decided to perform at the faculty's Christmas party.")
                label ep11_math_agree_label:
                scene ep11_math93 with dissolve
                mc "Ok, I'll do it. It sounds fun!"
                scene ep11_math96 with dissolve
                ph "That's excellent."
                ph "We're currently looking into the venue, but I'll get back to you with the details."
                scene ep11_math95 with dissolve
                mc "I'm looking forward to it."
                scene ep11_math91 with dissolve
                mc "(20 minutes... That's more than a song or two. Maybe Philip isn't aware, but it would require a lot of preparation.)"
            "Don't perform at the party":
                $ ep11_music = False
                $ new_bio("You", "I declined to perform at the faculty's Christmas party.")
                label ep11_math_decline_label:
                scene ep11_math92 with dissolve
                if ep11_fighter:
                    mc "Sorry, but I'm busy that day. I have a competition at the gym, and I think it will be an all-day event."
                    mc "And with the time needed to put a performance together and all... I have to say no."
                else:
                    mc "I think I have to say no. With Christmas and all, I don't think I'll have the time for it."
                if affinity == "CHICK":
                    mc "Thanks for asking, though. I appreciate it."
                scene ep11_math94 with dissolve
                ph "What a shame. I enjoyed your last performance a great deal. Pachelbel was an amazing composer."
                ph "But I respect your decision. Thanks for entertaining the thought, at least."
                scene ep11_math91 with dissolve
                mc "(As much fun as it would be, this was the right choice. It takes a lot of preparation to put together a 20-minute set.)"
        if not branchJill and not branchIsabella:
            mc "(Jill hasn't mentioned she was asked to perform. I wonder how she feels about it.)"
    $ new_bio("Philip", "Professor Hoff asked me to perform at the faculty's Christmas party.")

if (branchJill or branchIsabella) and ep11_music:
    $ tmpInt = 0
    $ tmpInt2 = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["%s" % name,"Guess who also got invited to play at the faculty Christmas party.",False])
    $ text_message_screen_list.append(["Jill","I know... Tybalt. He's going to embarrass himself. I don't know how I feel about that.",True])
    $ text_message_screen_list.append(["%s" % name,"What? Tybalt is performing too?",False])
    $ text_message_screen_list.append(["Jill","Yeah, I believe he's going to play the cello badly. But wait, who were you talking about?",True])

    hide screen new_phone_screen
    scene ep11_math97a with dissolve
    show screen text_message_screen
    $ renpy.pause()
    play sound "sound_effects/interlude/zoey_message.mp3"
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep11_math97b with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"I was talking about me! Philip just asked me, and I accepted. mphone_emoji_smile",False])
    if ep8_recital_failed:
        $ text_message_screen_list.append(["Jill","Oh! That's great news! That means we get to do it together. mphone_emoji_smile",True])
        $ text_message_screen_list.append(["%s" % name,"So, you decided to go through with it?",False])
        $ text_message_screen_list.append(["Jill","It's scary, but yes... I have to give it another shot.",True])
        if branchJill:
            $ text_message_screen_list.append(["%s" % name,"I believe in you. mphone_emoji_kiss",False])
        else:
            $ text_message_screen_list.append(["%s" % name,"You can do it. mphone_emoji_smile",False])
    else:
        $ text_message_screen_list.append(["Jill","Oh! That's great news! That means we get to do it together. mphone_emoji_smile",True])
        $ text_message_screen_list.append(["%s" % name,"Yes! I couldn't wait to tell you. It's going to be so much fun, but boy, what a lot of pressure deciding what to play...",False])
        if branchJill:
            $ text_message_screen_list.append(["Jill","I'll help you out with it. mphone_emoji_heart",True])
        else:
            $ text_message_screen_list.append(["Jill","I'm sure you'll figure something out. mphone_emoji_smile",True])
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ mphone_scene_to_chat("Jill",text_message_screen_list)
    show screen new_phone_screen

scene ep11_math97 with dissolve
ta "Hey, [name]."
scene ep11_math98 with dissolve
mc "Hey."
scene ep11_math99 with dissolve
ta "Did you talk to your friends? Because I didn't hear anything from them."
scene ep11_math98 with dissolve
mc "Yeah, I told them."
scene ep11_math99 with dissolve
ta "Ok..."
scene ep11_math98 with dissolve
mc "Don't tell me you expected them to apologize."
scene ep11_math99 with dissolve
ta "It's a mess anyway."
scene ep11_math98 with dissolve
mc "What makes you say that?"
scene ep11_math100 with dissolve
ta "Everyone's mad at me now."
scene ep11_math98 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(-Josy)","(+Josy)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Karma is a bitch \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        $ ep11_tara_attitude += 1
        mc "Karma is a bitch."
    "Everyone?":
        mc "Everyone?"
$ guideSuggestedPage = 194
scene ep11_math100 with dissolve
ta "I only tried to fix things, and now some of my friends are mad at me. It's not fair."
scene ep11_math98 with dissolve
mc "Why are your friends mad at you?"
scene ep11_math99 with dissolve
ta "For talking to you. They saw it as meddling."
scene ep11_math98 with dissolve
mc "Nice friends you have."
scene ep11_math99 with dissolve
ta "At the moment, I don't have a lot of them. The ones I have are coming to your party tonight."
ta "They weren't involved with the posters in any way, in case you're wondering."
scene ep11_math98 with dissolve
menu:
    "[m_c1]Invite Tara to the party":
        $ ep11_invited_tara = True
        mc "..."
        mc "Wanna come?"
        scene ep11_math101 with dissolve
        ta "To your party?"
        scene ep11_math98 with dissolve
        mc "I mean...yeah."
        mc "I'm not cool that you were one of the girls who tried to fuck us over, but them giving you the cold shoulder like that..."
        scene ep11_math102 with dissolve
        mc "It tells me your intentions are good."
        mc "Come to the party. Have fun with your friends and bury the hatchet with mine."
        scene ep11_math104 with dissolve
        ta "Do you think your friends will be ok with that?"
        scene ep11_math102 with dissolve
        mc "We'll see. But you can consider yourself my guest."
        scene ep11_math103 with dissolve
        ta "Thank you."
        scene ep11_math102 with dissolve
        mc "Oh. You know what the party is about, yeah? You better be cool with it."
        scene ep11_math103 with dissolve
        ta "I know. And I meant what I said before. I like your parties."
        if not branchSage:
            stop music fadeout 3
        scene ep11_math105 with dissolve
        mc "See you tonight, then. The party will be crazy fun."
        $ new_bio("Tara", "I invited Tara to the DIKs' Christmas Panty party. I felt that she was remorseful for her part in the drama.")
    "Leave":
        if not branchSage:
            stop music fadeout 3
        scene ep11_math106 with dissolve
        mc "Good to know. The party will be crazy fun."
        if ep11_tara_attitude > 1:
            $ new_bio("Tara", "I didn't invite Tara to the DIKs' Christmas Panty party. Fuck her.")
        else:
            $ new_bio("Tara", "I didn't invite Tara to the DIKs' Christmas Panty party.")
if branchSage:
    scene ep11_math107 with dissolve
    $ renpy.pause()
    scene ep11_math108 with dissolve
    $ renpy.pause()
    scene ep11_math109 with dissolve
    sa "Haha! Don't break your back."
    scene ep11_math110 with dissolve
    $ renpy.pause()
    scene ep11_math111 with dissolve
    mc "Damn, you're pretty today."
    scene ep11_math112 with dissolve
    $ renpy.pause()
    scene ep11_math113 with dissolve
    mc "Are you sure you're not coming to the party tonight?"
    scene ep11_math114 with dissolve
    sa "Yeah, I'm sure."
    sa "Your parties are great, but life has been too hectic lately. I want and need a calm Friday with my girls."
    scene ep11_math113 with dissolve
    mc "I'll miss you."
    scene ep11_math115 with dissolve
    sa "Ha! Yeah, right."
    scene ep11_math113 with dissolve
    mc "I will."
    scene ep11_math114 with dissolve
    sa "I'm sure you'll stop thinking about me the moment the party starts."
    stop music fadeout 3
    scene ep11_math116 with dissolve
    mc "Now, what would make you say that?"

jump ep11_freeroam_party_intro_label

label ep11_main_party_label:
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep11/licensed_music/track182.mp3"])
scene ep11_main_party1 with dissolve
if branchIsabella:
    isa "Yes, I'm aware."
    scene ep11_main_party3 with dissolve
    sa "He told you about their underwear party?"
    scene ep11_main_party2 with dissolve
    isa "He can be brazen at times."
else:
    isa "A party in their underwear?"
    scene ep11_main_party4 with dissolve
    my "He didn't tell you?"
    scene ep11_main_party2 with dissolve
    isa "He must have left that part out."
scene ep11_main_party5 with dissolve
js "I'm surprised how many went to it. Did you see the cluck the DIKs posted?"
scene ep11_main_party6 with dissolve
sa "Yup. Everyone has seen that cluck by now."
if branchJill:
    scene ep11_main_party7 with dissolve
    sa "How do you feel about [name] hosting that party?"
    scene ep11_main_party8 with dissolve
    ji "I'd say he explained it pretty well to me."
    ji "He said it was for his frat mates and not something he did for his benefit."
    scene ep11_main_party10 with dissolve
    sa "HA! Classic [name]."
    scene ep11_main_party9 with dissolve
    ji "What? Don't you believe him?"
    scene ep11_main_party11 with dissolve
    sa "Look, I'm sure [name] is faithful, but come on! A party with semi-nude girls..."
    sa "Unless he's walking around with a blindfold all night, it's for him too."
    scene ep11_main_party9 with dissolve
    ji "I don't think so."
    scene ep11_main_party12 with dissolve
    isa "I'm with Sage on this one. Boys will be boys."
    scene ep11_main_party11 with dissolve
    sa "Did he at least try to make you come?"
    scene ep11_main_party9 with dissolve
    ji "Yes, but he asked in a way that you do when you already know the answer."
    ji "I was never going to show up for something like that."
    scene ep11_main_party13 with dissolve
    js "You don't have to explain that to us. We were all invited, but now we're here."
if branchSage:
    scene ep11_main_party14 with dissolve
    isa "Why aren't you there?"
    scene ep11_main_party15 with dissolve
    sa "Because I'd rather be here tonight. I was at one of those parties last year."
    sa "Let's be honest, underwear parties are no different than bikini beach parties, but people act like they are."
    sa "But I'm not interested in watching [name] drool over girls in lingerie all night. He has some weird sock fetish."
    scene ep11_main_party16 with dissolve
    my "Haha! Yeah, it's not hard to notice that."
    if not branchJill:
        scene ep11_main_party11 with dissolve
        sa "What about you, Jill? Did he invite you?"
if branchIsabella and not branchJill:
    scene ep11_main_party11 with dissolve
    sa "What about you, Jill? Did he invite you?"
if branchMayaJosy:
    scene ep11_main_party17 with dissolve
    isa "And you girls aren't there because...?"
    scene ep11_main_party18 with dissolve
    js "I've already walked around in my panties there once. It's enough for me."
    scene ep11_main_party19 with dissolve
    sa "Say what?"
    scene ep11_main_party20 with dissolve
    my "Josy tried to save me from their Walk of Shame tradition the morning after Halloween."
    scene ep11_main_party21 with dissolve
    sa "Ah. That."
    scene ep11_main_party20 with dissolve
    my "And I wouldn't want to spend the entire night drunk in my underwear over there."
    scene ep11_main_party21 with dissolve
    sa "Let's be honest, underwear parties are no different than bikini beach parties, but people act like they are."
    sa "But I wouldn't wanna watch [name] drool over girls in lingerie all night if I were you, either."
    scene ep11_main_party22 with dissolve
    js "He's not gonna do that. Is he?"
    scene ep11_main_party12 with dissolve
    isa "Well... Boys will be boys."
    if not branchJill:
        scene ep11_main_party11 with dissolve
        sa "What about you Jill? Did he invite you?"
if not branchJill and not branchIsabella and not branchSage and not branchMayaJosy:
    scene ep11_main_party11 with dissolve
    sa "What about you, Jill? Did he invite you?"
if not branchJill:
    scene ep11_main_party9 with dissolve
    ji "Yes, but he asked in a way that you do when you already know the answer."
    ji "I was obviously never going to show up for something like that."
    scene ep11_main_party13 with dissolve
    js "You don't have to explain that to us. We were all invited, but now we're here."
scene ep11_main_party23 with dissolve
isa "I wasn't invited."
scene ep11_main_party24 with dissolve
sa "Did you want an invite? I can ask him now; he's online."
scene ep11_main_party2 with dissolve
isa "No, I did not expect an invite."
scene ep11_main_party24 with dissolve
sa "Yeah, but still. Let's fuck with him."

hide screen new_phone_screen
scene ep11_main_party1b with dissolve
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Sage","Hey! Where the hell is Bella's invitation to your party? She feels left out.",True])
$ text_message_screen_list.append(["%s" % name,"Huh? Does she really?",False])
$ text_message_screen_list.append(["Sage","It's custom to invite your friends... Just saying.",True])
$ text_message_screen_list.append(["%s" % name,"She doesn't want to come to this party. Let's be real, Sage.",False])
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()
scene ep11_main_party2b with dissolve
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ text_message_screen_list.append(["%s" % name,"There's no chance Bella would party in her underwear. She's a mature woman. She likes drinking wine and having her clothes on. In fact, I bet that's what she's doing right now.",False])
$ mphone_scene_to_chat("Sage",text_message_screen_list)
scene ep11_main_party25 with dissolve
sa "\"She doesn't want to come to this party. Let's be real, Sage.\""
sa "Wow! Not cool, [name]. Not cool at all."
scene ep11_main_party28 with dissolve
isa "He knows me. I wouldn't have come tonight."
scene ep11_main_party25 with dissolve
sa "\"There's no chance Bella would be partying in her underwear. She's a mature woman. She likes drinking wine and having her clothes on. In fact, I bet that's what she's doing right now.\""
scene ep11_main_party29 with dissolve
isa "Ok, now he's pushing it. What is it with you guys? You assume that I don't know how to have fun."
scene ep11_main_party30 with dissolve
sa "Huh? [name] is the one doing that."
scene ep11_main_party29 with dissolve
isa "No. You once assumed I wouldn't dance, and now he assumes I'm too old to party in my underwear."
isa "And you all were surprised when I invited you to the party we're having tonight."
scene ep11_main_party31 with dissolve
js "Did we offend you in any way?"
scene ep11_main_party32 with dissolve
isa "If I were your age and in college with you... I'm sorry to break it to you, but I wouldn't be sitting here on this couch tonight."
isa "I'd be at that underwear party."
scene ep11_main_party33 with dissolve
my "Haha! No way. You're making this up."
scene ep11_main_party29 with dissolve
isa "Tell [name] that he's right. There's no chance I'd be partying in my underwear at his party because we're too busy partying in underwear at my place."
isa "And that his invite must have gotten lost, too."
scene ep11_main_party26 with dissolve
sa "Haha! I'm so telling him that!"
hide screen new_phone_screen
scene ep11_main_party3b with dissolve
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Sage","She says there's no chance she'd party in her underwear at your party because we're busy doing that at her place tonight. And she didn't invite you because she thought you wouldn't come.",True])
$ text_message_screen_list.append(["%s" % name,"Yeah, right. I'll believe that when I see it.",False])
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ text_message_screen_list.append(["Sage","chat_sage_group_pic1_ep11_thumb",True])
$ mphone_scene_to_chat("Sage",text_message_screen_list)
$ mgallery_add_photo("chat_sage_group_pic1_ep11_zoomed")
scene ep11_main_party27 with dissolve
sa "Dammit. I knew he'd call your bluff."
scene ep11_main_party28 with dissolve
isa "Is it a bluff if we do it?"
scene ep11_main_party34 with dissolve
ji "What are we doing?"
scene ep11_main_party35 with dissolve
isa "Come on. Let's wipe the smirk off his face."
scene ep11_main_party37 with dissolve
sa "Haha! Are you for real!?"
scene ep11_main_party36 with dissolve
js "You gotta be joking."
scene ep11_main_party38 with dissolve
isa "$20 says I can make [name] hop on the next bus over here with a single picture of us."
isa "Any takers?"
play sound "sound_effects/interlude/zoey_message.mp3"
scene ep11_main_party1b with dissolve
"*{i}Text message{/i}*"
scene ep11_main_party4b with dissolve
mc "Dear Lord..."
scene ep11_main_party5b with dissolve
$ renpy.pause()
scene ep11_main_party39 with dissolve
"*{i}Laughter{/i}*"
play sound "sound_effects/cellphone.mp3"
scene ep11_main_party40 with dissolve
sa "He's calling! Haha! What do we do now?"
scene ep11_main_party41 with dissolve
isa "Don't answer. Commence radio silence."
scene ep11_main_party42 with dissolve
sa "You're not dull and mature. You're fun and inappropriate."
scene ep11_main_party41 with dissolve
isa "I'll drink to that."
jump ep11_pp_part2_event_label

label ep11_main2_party_label:
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track125.mp3"])
play sound "sound_effects/season3/ping_pong_splash.mp3"
scene ep11_main2_party1 with vpunch
js "No!"
scene ep11_main2_party2 with dissolve
isa "Loser!"
isa "You have some beer to drink."
scene ep11_main2_party4 with dissolve
js "You are way too good at this."
scene ep11_main2_party3 with dissolve
isa "I told you I was. Now, who else wants their butt kicked?"
scene ep11_main2_party5 with dissolve
sa "No, not again."
scene ep11_main2_party3 with dissolve
isa "Wusses, all of you."
scene ep11_main2_party6 with dissolve
my "Hahaha!"
scene ep11_main2_party7 with dissolve
sa "This is quite liberating."
scene ep11_main2_party8 with dissolve
ji "What is?"
scene ep11_main2_party7 with dissolve
sa "Chilling in our underwear like this."
scene ep11_main2_party8 with dissolve
ji "It's one thing doing it with you girls, but I still wouldn't do it at [name]'s party among God knows how many people."
scene ep11_main2_party10 with dissolve
isa "Not even after a few drinks?"
scene ep11_main2_party9 with dissolve
ji "Just because I get tipsy doesn't mean I lose my inhibitions."
scene ep11_main2_party11 with dissolve
isa "You bathed naked in the snow."
scene ep11_main2_party12 with dissolve
sa "She what?"
scene ep11_main2_party9 with dissolve
ji "I thought what happened at Bianca's cabin stayed there."
scene ep11_main2_party11 with dissolve
isa "I did not agree to those terms."
scene ep11_main2_party13 with dissolve
js "She's not lying? Did you do that?"
scene ep11_main2_party14 with dissolve
ji "We went from the sauna into the snow and then into the hot tub."
scene ep11_main2_party16 with dissolve
my "Naked?"
scene ep11_main2_party15 with dissolve
if branchJill or branchIsabella:
    ji "It was Bianca's idea. She, [name] and Bella egged me on."
else:
    ji "It was Bianca's idea. She and Bella egged me on."
scene ep11_main2_party11 with dissolve
isa "But your inhibitions were lowered from alcohol, is all I'm saying."
scene ep11_main2_party13 with dissolve
js "How was it?"
scene ep11_main2_party14 with dissolve
ji "It was super cold! But the hot tub made up for it."
scene ep11_main2_party17 with dissolve
mc "No way! You're actually in your underwear!?"
scene ep11_main2_party18 with dissolve
sa "Party crasher! Haha!"
scene ep11_main2_party19 with dissolve
isa "Called it! Maya and Jill, you owe me $20!"
scene ep11_main2_party20 with dissolve
isa "But also... Waltz right in much? It's invitation-only, \"bro\"."
scene ep11_main2_party21 with dissolve
ji "This is a girls' party, [name]. What are you doing here?"
scene ep11_main2_party22 with dissolve
sa "To be fair, they probably had the same girl-to-guy ratio at their party tonight."
scene ep11_main2_party23 with dissolve
mc "Not you girls, too... Look, I can't be held responsible for that."
scene ep11_main2_party22 with dissolve
sa "Didn't you plan everything?"
scene ep11_main2_party23 with dissolve
mc "So, what are you girls up to?"
scene ep11_main2_party24 with dissolve
js "Nice deflection."
scene ep11_main2_party23 with dissolve
if ep11_zoey_kiss == 1:
    mc "Give me a break here. I had a rough night... And I left that party for you."
else:
    mc "Give me a break here. I left that party for you."
scene ep11_main2_party22 with dissolve
sa "Hoping to achieve what?"
scene ep11_main2_party23 with dissolve
mc "I happened to miss you girls."
scene ep11_main2_party27 with dissolve
isa "HA!"
scene ep11_main2_party25 with dissolve
ji "Hahaha!"
scene ep11_main2_party26 with dissolve
mc "I can leave..."
scene ep11_main2_party27 with dissolve
isa "Sure. Bye!"
scene ep11_main2_party26 with dissolve
mc "Ok, I'm leaving... Don't stop me..."
scene ep11_main2_party29 with dissolve
mc "Someone, please stop me."
scene ep11_main2_party28 with dissolve
isa "You can stay, but your dress code is not up to par."
scene ep11_main2_party26 with dissolve
mc "Say no more."
scene ep11_main2_party30 with dissolve
isa "I'll be right back."
scene ep11_main2_party31 with dissolve
mc "I was having fun at our party, but I'd rather spend the night with you."
mc "You all should have come tonight."
scene ep11_main2_party32 with dissolve
sa "Oh, yeah? What is it like over there?"
scene ep11_main2_party31 with dissolve
mc "Everyone's having a lot of fun."
scene ep11_main2_party33 with dissolve
isa "Nope. You're not done yet. We have a dress code here."
scene ep11_main2_party34b with dissolve
mc "You're seriously not asking me to remove my underwear... Are you?"
scene ep11_main2_party34 with dissolve
isa "No, I'm asking you to put on this. Honor the dress code."
scene ep11_main2_party35 with dissolve
$ renpy.pause()
scene ep11_main2_party40 with dissolve
js "Hahaha! No way!"
scene ep11_main2_party41 with dissolve
my "This party continues to deliver."
scene ep11_main2_party36 with dissolve
mc "That's very funny."
scene ep11_main2_party37 with dissolve
isa "Am I laughing? My house, my party, my rules."
isa "If you don't like it, consider inviting me to your party next time."
scene ep11_main2_party38 with dissolve
mc "Whatever."
scene ep11_main2_party39 with dissolve
mc "It's a bra. Sure, it's weird, but it's not as demeaning as you think."
play sound "sound_effects/camera_shutter.mp3"
scene ep11_main2_party42 with dissolve
"*{i}Click{/i}*"
sa "Haha, I'm not too sure about that."
scene ep11_main2_party43 with dissolve
mc "Hey! No photos! What the hell!"
scene ep11_main2_party44 with dissolve
mc "Give it here!"
sa "Hahaha!"
scene ep11_main2_party45 with dissolve
isa "You were saying, [name]?"
scene ep11_main2_party46 with dissolve
mc "Give it!"
sa "Girls, help me!"
scene ep11_main2_party47 with dissolve
ji "Haha! No, you don't!"
my "Pay the price of admission, [name]."
scene ep11_main2_party48 with dissolve
mc "No! Stop it!"
play sound "sound_effects/shove.mp3"
scene ep11_main2_party49 with vpunch
mc "Ow! Ok! Ok! You win!"
scene ep11_main2_party50 with dissolve
"*{i}Laughter{/i}*"
scene ep11_main2_party51 with dissolve
sa "Bella, get in the frame!"
scene ep11_main2_party52 with dissolve
sa "Cheese!"
play sound "sound_effects/camera_shutter.mp3"
"*{i}Click{/i}*"
scene ep11_main2_party53 with dissolve
mc "Sheesh..."
scene ep11_main2_party54 with dissolve
mc "You girls fight dirty! This party sucks."
scene ep11_main2_party55 with dissolve
isa "Oh, boo-hoo. Have something to drink and be happy I didn't ask you to put on a thong."
scene ep11_main2_party56 with dissolve
sa "Oh, you should!"
scene ep11_main2_party57 with dissolve
mc "Sage. Be quiet."
scene ep11_main2_party58 with dissolve
my "What are you guys up to at that thong party of yours?"
scene ep11_main2_party59 with dissolve
if ep11_pp_contest == 0:
    mc "We had a big wet T-shirt contest and something we call The Dirty Bowl."
    scene ep11_main2_party60 with dissolve
    isa "A wet T-shirt contest? Aren't girls already undressed?"
    scene ep11_main2_party61 with dissolve
    mc "Yeah, but they were topless under the T-shirt, and there were beers, so..."
elif ep11_pp_contest == 1:
    mc "We had a...um...Dildo Sucking Competition and something we call The Dirty Bowl."
    scene ep11_main2_party60 with dissolve
    isa "A Dildo Sucking Competition?"
    scene ep11_main2_party61 with dissolve
    mc "It was originally supposed to be cucumbers, but those either perished or got eaten."
    scene ep11_main2_party62 with dissolve
    isa "Good thing you had dildos then."
    scene ep11_main2_party61 with dissolve
    mc "Sarcasm?"
else:
    mc "We have something we call The Diry Bowl."
scene ep11_main2_party63 with dissolve
ji "What's The Dirty Bowl?"
scene ep11_main2_party61 with dissolve
mc "Guests take a secret mission from a bowl and have to accomplish it by midnight."
mc "Most of the missions were sexy or made guests interact."
scene ep11_main2_party64 with dissolve
if ep11_pp_contest == 2:
    js "And this was your idea, huh?"
else:
    js "And these were all your ideas, huh?"
scene ep11_main2_party65 with dissolve
if ep11_pp_contest == 2:
    mc "The concept was my idea, but the boys helped with the details."
else:
    mc "The concepts were my ideas, but the boys helped with the details."
scene ep11_main2_party63 with dissolve
ji "Now I'm even more glad I didn't come."
scene ep11_main2_party61 with dissolve
mc "It sounds worse than what it is."
mc "What about you? What adventures have you been having at your crazy party?"
scene ep11_main2_party64 with dissolve
js "Bella beat us in beer pong."
scene ep11_main2_party66 with dissolve
mc "Is that why you're in your underwear?"
scene ep11_main2_party67 with dissolve
isa "We didn't play the strip version of it. But I got them all good and drunk."
scene ep11_main2_party68 with dissolve
mc "What a good hostess you are."
scene ep11_main2_party69 with dissolve
if ep11_pp_contest == 0:
    my "Haha! Well, she doesn't force us to pour beer on our tits or make us do sexy stuff before midnight, so..."
elif ep11_pp_contest == 1:
    my "Haha! Well, she doesn't force us to suck on vegetables or make us do sexy stuff before midnight, so..."
else:
    my "Haha! Well, she doesn't force us to do sexy stuff before midnight, so..."
scene ep11_main2_party67 with dissolve
isa "I'll beat your ass at it, too, if you're up for it."
scene ep11_main2_party70 with dissolve
mc "The drinking version of beer pong is too boring for me."
scene ep11_main2_party71 with dissolve
isa "We're not playing the strip version if that's what you had in mind. But I'll make you a bet."
scene ep11_main2_party70 with dissolve
mc "What's the bet?"
scene ep11_main2_party71 with dissolve
isa "If I beat you, you put on a thong."
scene ep11_main2_party72 with dissolve
sa "Hahaha! Yes! Now that's a bet!"
scene ep11_main2_party70 with dissolve
mc "That's not happening..."
scene ep11_main2_party73 with dissolve
my "*{i}Chicken noises{/i}*"
scene ep11_main2_party71 with dissolve
isa "What a sissy."
scene ep11_main2_party70 with dissolve
mc "Let me finish my sentence."
mc "That's not happening...because if I beat you..."
scene ep11_main2_party78 with dissolve
mc "...the bra disappears from the dress code. And I mean for all of us."
scene ep11_main2_party74 with dissolve
ji "What? No way."
scene ep11_main2_party75 with dissolve
js "You would say that..."
scene ep11_main2_party76 with dissolve
sa "Now, that's a bet!"
scene ep11_main2_party79 with dissolve
isa "I'm sorry, but I cannot stake what's not mine to stake."
isa "I'll let you remove yours."
scene ep11_main2_party70 with dissolve
mc "That's not good enough. Do you know what I'd look like wearing a thong?"
mc "I'd fall out of it...if you know what I mean."
scene ep11_main2_party76 with dissolve
sa "Make the bet, Bella. Given how you beat us tonight, I'm fully confident that you'd turn bra-boy into thong-boy."
scene ep11_main2_party80 with dissolve
isa "Is everyone ok with it?"
scene ep11_main2_party83 with dissolve
ji "No, I'm not."
scene ep11_main2_party84 with dissolve
mc "For one hour! Or maybe two?"
scene ep11_main2_party86 with dissolve
my "If there are no cameras... I'm on board."
scene ep11_main2_party85 with dissolve
mc "Ask Sage. She's the paparazzi."
scene ep11_main2_party77 with dissolve
sa "Tsk."
scene ep11_main2_party80 with dissolve
isa "Josy, Jill? How about it?"
scene ep11_main2_party81 with dissolve
js "If everyone else is doing it... Sure. For one hour! And we can cover up with our hands and pillows."
scene ep11_main2_party82 with dissolve
isa "You're making it sound like I will lose."
scene ep11_main2_party83 with dissolve
ji "If what Josy said are the terms... Ok. But you better win."
scene ep11_main2_party84 with dissolve
mc "Don't worry, Jill. I'll do my best to win."
scene ep11_main2_party87 with dissolve
ji "I meant Bella, bra-boy."
scene ep11_main2_party76 with dissolve
sa "Soon to be thong-boy! Haha!"

scene ep11_main2_party88 with dissolve
isa "Now is your final chance to get out of the bet. What's it going to be, [name]?"
scene ep11_main2_party89 with dissolve
mc "I'm here for it!"
mc "One-hour thong vs. one-hour bra... The Battle of the Titans. No wait..."
mc "Thong Pong!"
scene ep11_main2_party90 with dissolve
isa "That's right. Embrace your impending defeat."

hide screen new_phone_screen
if minigames and not bp_tut_ep10_seen and (tutorials or not persistent.bp_tutorial):
    menu:
        "Watch tutorial":
            $ bp_tut_ep10_seen = True
            $ bp_dlg = 0
            $ bp_jump_label = "ep11_bp_match_bella_label"
            show screen bp_tut_screen
            pause
            $ persistent.bp_tutorial = True
        "Skip tutorial":
            $ renpy.pause(0.5)

label ep11_bp_match_bella_label:
hide screen new_phone_screen
$ renpy.block_rollback()
$ bp_init_game("Isabella","ep11", "ep11_after_bp_bella_label")
if minigames:
    show screen bp_screen
else:
    show screen bp_screen_nm
pause

label ep11_after_bp_bella_label:
show screen new_phone_screen
$ guideSuggestedPage = 220
if bp_player_won:
    $ ep11_bp_won_bella = True
    if minigames:
        scene ep11_main2_party91
        hide screen bp_screen
        with dissolve
    else:
        scene ep11_main2_party91
        hide screen bp_screen_nm
        with dissolve
    if not persistent.ep11_cardmy9:
        $ persistent.chat_new_rewards = True
        $ persistent.rew_maya_unlocked += 1
        $ persistent.ep11_cardmy9 = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
    $ new_bio("Isabella", "I won at Beer Pong against Bella, and she lost the bet.")
    if minigames and steamAchievements:
        $ achievement.grant("IDS3_43")
        init:
            $ achievement.register("IDS3_43")
        $ achievement.Sync()
    sa "No!!!"
    ji "You lost!?"
    scene ep11_main2_party92 with dissolve
    mc "3-2-1-Lose it!"
    scene ep11_main2_party93 with dissolve
    mc "*{i}Cough cough{/i}*"
    mc "In the words of our hostess, honor the dress code."
    scene ep11_main2_party94 with dissolve
    js "How did you lose?"
    scene ep11_main2_party95 with dissolve
    isa "Best out of three?"
    scene ep11_main2_party96 with dissolve
    menu:
        "Nope":
            mc "Nope. Not happening."
        "Double or nothing":
            mc "The best I can do is double or nothing for the panties."
            scene ep11_main2_party97 with dissolve
            ji "That's a no. Don't make any more bets with my clothes."
    scene ep11_main2_party98 with dissolve
    sa "It's not that big of a deal. We agreed that we could cover ourselves up with our hands and pillows."
    scene ep11_main2_party99 with dissolve
    mc "And you thought that my parties were too much. Bella's parties are way worse than mine."
    scene ep11_main2_party100 with dissolve
    isa "Can someone set the timer for one hour?"
    scene ep11_main2_party101 with dissolve
    mc "I can do it."
    scene ep11_main2_party102 with dissolve
    js "No way. I'll do it. If I know you well enough, you'd set it to something else completely."
    scene ep11_main2_party103 with dissolve
    my "Haha!"
    scene ep11_main2_party104 with dissolve
    mc "I'd like to make a toast. To Bella and her amazing party! Cheers, anyone? Bring it in."
    scene ep11_main2_party105 with dissolve
    my "No. We know what you're trying to do."
    scene ep11_main2_party106 with dissolve
    ji "Go ahead and gloat."
    scene ep11_main2_party107 with dissolve
    sa "It would have been funnier to see you wear a thong."
    scene ep11_main2_party108 with dissolve
    mc "Maybe next time?"
    scene ep11_main2_party106 with dissolve
    ji "It's the last bet of this kind I'll do."
else:
    if minigames:
        scene ep11_main2_party109
        hide screen bp_screen
        with dissolve
    else:
        scene ep11_main2_party109
        hide screen bp_screen_nm
        with dissolve
    $ new_bio("Isabella", "I lost the bet against Bella when we played Beer Pong.")
    $ ep11_bp_won_bella = False
    js "Yes!!!"
    scene ep11_main2_party110 with dissolve
    my "Haha! [name] is the Thong Pong loser!"
    scene ep11_main2_party111 with dissolve
    mc "That's not fair. Bella's been practicing all night long."
    scene ep11_main2_party112 with dissolve
    isa "You should have taken that into account when you made the bet. Excuse me while I find you something nice to wear."
    scene ep11_main2_party113 with dissolve
    sa "Oh, please! Make it the tiniest one you can find."
    scene ep11_main2_party114 with dissolve
    mc "Sage! Please!"
    scene ep11_main2_party115 with dissolve
    ji "Hahaha!"
    my "And don't you dare put it on top of your boxers. We want to see you replace your underwear!"
    scene ep11_main2_party116 with dissolve
    sa "Oh! Nice catch. He would try to find a loophole."
    scene ep11_main2_party117 with dissolve
    isa "I didn't even have to second-guess myself. Here you go. Suit up."
    scene ep11_main2_party118 with dissolve
    mc "Really...? Those?"
    scene ep11_main2_party117 with dissolve
    isa "They're delicate and match your bra. Also, I think they will bring out your eyes."
    scene ep11_main2_party118 with dissolve
    mc "And my penis. I won't fit in them."
    scene ep11_main2_party119 with dissolve
    isa "I'm sure you'll work something out."
    isa "And oh..."
    isa "Welcome to the party, [name]. I'm happy to have you here."
    scene ep11_main2_party120 with dissolve
    mc "This isn't dignified."
    scene ep11_main2_party121 with dissolve
    isa "That's how we do it at the Roberts'. Cheers, everyone!"
    scene ep11_main2_party122 with dissolve
    mc "Question... Are they supposed to go up this tightly in the crack? It's very uncomfortable."
    scene ep11_main2_party124 with dissolve
    ji "Oh, dear... That's quite a sight..."
    js "Hahaha!"
    scene ep11_main2_party125 with dissolve
    sa "Oh my God!!! Hahaha! Turn around! Show us the other side!!!"
    scene ep11_main2_party123 with dissolve
    mc "I'm thinking no..."
    scene ep11_main2_party126 with dissolve
    isa "Go ahead and keep those. I don't want to wear them again."
    scene ep11_main2_party127 with dissolve
    mc "Can someone put the timer at one hour already?"

jump ep11_ho_main_party_label

label ep11_main2_party_end_label:
if (ep11_mg_party or wt_ep11_party_bella) and (ep11_zoey_kiss < 2 and not wt_ep11_party_bella):
    if ep11_bp_won_bella:
        scene ep11_main2_party236 with fade
        js "Time's up. Bras back on!"
        scene ep11_main2_party237 with dissolve
        ji "Finally... That was one long hour."
        scene ep11_main2_party238 with dissolve
        mc "Not to me. And I'm keeping mine off as an extra reward or I'll get marks from it."
        stop music fadeout 3
        scene ep11_main2_party235 with dissolve
        $ renpy.pause()
    else:
        scene ep11_main2_party232 with fade
        js "Time's up, [name]. You're free to change back into your boxers if you want."
        scene ep11_main2_party233 with dissolve
        mc "If I want? That question needs no answer. And I'll remove the bra before I get marks from it."
        stop music fadeout 3
        scene ep11_main2_party234 with dissolve
        $ renpy.pause()
play music "music/ep11/licensed_music/track185.mp3"
scene ep11_main2_party_end1 with dissolve
my "Are you having fun tonight?"
scene ep11_main2_party_end3 with dissolve
js "So much fun. Bella sure knows how to entertain."
scene ep11_main2_party_end2 with dissolve
my "Haha, yeah. I didn't know she had this in her. I was surprised."
scene ep11_main2_party_end4 with dissolve
$ renpy.pause()
scene ep11_main2_party_end13 with dissolve
my "How are you other than tonight? I've noticed you've been withdrawn lately. It's not like you..."
scene ep11_main2_party_end5 with dissolve
js "I've needed time to think."
scene ep11_main2_party_end14 with dissolve
my "About...?"
scene ep11_main2_party_end5 with dissolve
js "Everything."
scene ep11_main2_party_end14 with dissolve
my "Wanna talk about it?"
scene ep11_main2_party_end6 with dissolve
js "It's not a talk you have during a party."
scene ep11_main2_party_end13 with dissolve
my "I get it. Just answer this...are you ok?"
scene bg anim_josy_shake_ep11 movie with dissolve
pause
scene ep11_main2_party_end13 with dissolve
my "I had a feeling you weren't."
scene ep11_main2_party_end7 with dissolve
js "What about you?"
scene ep11_main2_party_end15 with dissolve
my "When have I ever been ok? Haha..."
my "There are good things in my life and there are bad things."
scene ep11_main2_party_end7 with dissolve
js "And where would you put you and me on that scale?"
scene ep11_main2_party_end14 with dissolve
my "Where would you?"
scene ep11_main2_party_end6 with dissolve
js "That's one of the things that I'm trying to figure out."
if branchMayaJosy:
    scene ep11_main2_party_end13 with dissolve
    my "Are you uncertain about us three?"
    scene ep11_main2_party_end6 with dissolve
    js "I don't know how I should put it. But it's one of the things I've been thinking about a lot."
    js "Especially after [name]'s dad had a hard time accepting it, I started thinking about how unusual it was."
    scene ep11_main2_party_end7 with dissolve
    js "I think we're not communicating well."
    scene ep11_main2_party_end16 with dissolve
    my "I don't agree with that. I think [name] is great at it."
    scene ep11_main2_party_end6 with dissolve
    js "When I said we, I meant you and me."
    scene ep11_main2_party_end13 with dissolve
    my "Oh... I think we do. At times..."
else:
    scene ep11_main2_party_end14 with dissolve
    if ep10_got_contracts:
        my "It should be easy to figure out when Dad's not an issue for us."
    else:
        my "And it's not easy for us to figure out when Dad is an issue."
    scene ep11_main2_party_end8 with dissolve
    js "Here's the thing... I don't think our problems start or end with Patrick."
    js "It's easy to pin the blame on him for everything, but I think there are more problems in our relationship that he overshadowed."
    scene ep11_main2_party_end6 with dissolve
    js "Like us not communicating well."
    scene ep11_main2_party_end14 with dissolve
    my "You don't think that we do?"
    scene ep11_main2_party_end7 with dissolve
    js "Do you?"
    scene ep11_main2_party_end13 with dissolve
    my "Uh... At times."

scene ep11_main2_party_end8 with dissolve
js "You never told me that Patrick was abusive to you. I'm trying to wrap my head around it, but I don't understand why you never told me."
scene ep11_main2_party_end17 with dissolve
my "I didn't want to talk about it because I was ashamed."
scene ep11_main2_party_end8 with dissolve
js "It hurt to hear it, but it hurt even more not to hear it directly from you."
js "I would have been supportive had you told me."
scene ep11_main2_party_end13 with dissolve
my "I'm sure you have things you never told me."
scene ep11_main2_party_end7 with dissolve
js "I have. And that's why I think we're not communicating well. It's not just you, it's me too."
js "And I'm trying to figure out why."
scene ep11_main2_party_end8 with dissolve
js "I think with everything you've gone through, I didn't want to bother you with my problems."
js "You already carry so much, and maybe you can't take it if I weigh you down."
scene ep11_main2_party_end13 with dissolve
my "Have you been scared to tell me stuff?"
scene ep11_main2_party_end9 with dissolve
js "Subconsciously, yeah. And it snowballed... And now it's this huge snowball that I can't push anymore."
scene ep11_main2_party_end16 with dissolve
my "Tell me the things you've wanted to tell me. I won't break."
scene ep11_main2_party_end18 with dissolve
$ renpy.pause()
scene ep11_main2_party_end9 with dissolve
js "I don't know who I am anymore. I feel like I'm following the stream. Just tagging along."
js "I don't know if the things I do are for me or someone else."
scene ep11_main2_party_end7 with dissolve
js "Like college, I used to think I wanted it. But am I here for me, or am I doing it to make Dad proud? Do I want this?"
js "What am I even good at? I feel like I'm mediocre at everything."
js "If someone asked me what my skills are, I wouldn't know what to say."

if branchMayaJosy:
    scene ep11_main2_party_end9 with dissolve
    js "And with us...again, you and me. I follow the stream, too."
    js "There's not a lot of focus on my feelings... It's almost always about you and your problems."
    js "And I know that's a horrible thing to say, and I feel so sorry for you that it has to be this way..."
    js "But I feel I do not matter a lot."
    if ep11_josy_solo:
        scene ep11_main2_party_end10 with dissolve
        js "And when I'm alone with [name], I feel something different."
        if ep11_josy_love > 0:
            scene ep11_main2_party_end11 with dissolve
            js "Last time when we were alone, he told me he loved me."
            scene ep11_main2_party_end10 with dissolve
            if ep11_josy_love == 1:
                js "I was at a loss for words. Even with him, I didn't know what I felt."
                js "I used to be able to tell you that I love you..."
                js "And I can't say how I feel about you anymore, either. And I don't understand why."
            else:
                js "And without hesitation, I told him I love him too."
                js "I used to be able to tell you that I love you..."
                js "But I can't say how I feel about you anymore. And I don't understand why."
        else:
            js "I used to be able to tell you that I love you..."
            js "But I can't say how I feel about you anymore. And I don't understand why."
    else:
        scene ep11_main2_party_end10 with dissolve
        js "With [name], I feel something completely different."
        js "I used to be able to tell you that I love you..."
        js "But I can't say how I feel about you anymore. And I don't understand why."

    scene ep11_main2_party_end11 with dissolve
    js "And I can't go on and pretend this isn't an issue."
else:
    scene ep11_main2_party_end9 with dissolve
    js "And with us... I follow the stream, too."
    js "There's not a lot of focus on us or love... It's almost always about you and your problems."
    js "And I know that's a horrible thing to say, and I feel so sorry for you that it has to be this way..."
    js "But I feel I do not matter a lot."
    if ep10_jm_solo == "Josy":
        scene ep11_main2_party_end10 with dissolve
        js "And... I have a crush on [name] that started this summer, and it hasn't gone away."
        js "And I told him this not that long ago. We built a pillow fort in my room, and I put on lingerie for him."
        js "Then I just said it."
        scene ep11_main2_party_end11 with dissolve
        if ep10_feelingsForJosy:
            js "And he told me he felt the same way, but neither of us could cheat behind your back after all we've been through."
        elif branchAlone:
            js "And he told me he was over me and that I had to tell you about my feelings."
        else:
            js "And he told me he was in a relationship and that I had to tell you about my feelings."
            if branchIsabella:
                js "I now know that relationship is with Bella."
                scene ep11_main2_party_end19 with dissolve
                $ renpy.pause()
        scene ep11_main2_party_end10 with dissolve
        js "I used to be able to tell you that I love you..."
        js "But I can't say how I feel about you anymore. And I don't understand why."
    else:
        if ep9_jm_sad:
            scene ep11_main2_party_end11 with dissolve
            js "And... I'm so sad that [name] broke up with us. And what scares me the most about that is that I think I loved him."
        else:
            scene ep11_main2_party_end11 with dissolve
            js "And... I have a crush on [name] that started this summer, and it hasn't gone away yet."
            js "Every time I look at him, I feel it..."
        if branchIsabella:
            js "And now I know that he's in a relationship with Bella."
        scene ep11_main2_party_end10 with dissolve
        js "I used to be able to tell you that I love you..."
        js "But I can't say how I feel about you anymore. And I don't understand why."

scene ep11_main2_party_end12 with dissolve
js "It scares me. It scares me to be confused. I hope the love between us isn't gone and can return to blossom again."
js "And telling you about this now... I can feel the weight coming off my shoulders."
js "But I'm scared to stop talking and hearing how you will react. But I'm gonna do it..."
scene ep11_main2_party_end20 with dissolve
$ renpy.pause()
scene ep11_main2_party_end21 with dissolve
$ renpy.pause()
scene ep11_main2_party_end23 with dissolve
$ renpy.pause()
scene ep11_main2_party_end22 with dissolve
$ renpy.pause()
scene ep11_main2_party_end24 with dissolve
my "I'm sorry that you feel this way about it all..."
my "You matter, Josy. You matter to me."
scene ep11_main2_party_end26 with dissolve
my "I thought we had good communication... Well, maybe not lately... And apparently, it's not good enough."
my "I'm so thankful for everything you've done for me and how well you've supported me, but I failed to see that you were losing yourself while doing that."

if branchMayaJosy:
    scene ep11_main2_party_end24 with dissolve
    my "If we are happy as a group but not when we're alone, we need to find out why that is."
    my "I can only speak for myself, but I've not been thinking a lot about the relationship you and I have when we're with [name]."
    my "All those nasty thoughts I didn't want to have when Dad posed his ultimatum almost disappeared when the three of us got together."
    if ep11_maya_love >= 2:
        scene ep11_main2_party_end26 with dissolve
        my "When we spent time alone, [name] and I told each other that we were in love."
        scene ep11_main2_party_end27 with dissolve
        js "You...said that to each other?"
        scene ep11_main2_party_end26 with dissolve
        my "Yes... And it's been quite a while since I said those words to you."
        scene ep11_main2_party_end24 with dissolve
    elif ep11_maya_love == 1:
        scene ep11_main2_party_end26 with dissolve
        my "When we spent time alone, [name] told me he loved me."
        scene ep11_main2_party_end27 with dissolve
        js "He did?"
        scene ep11_main2_party_end26 with dissolve
        my "But I didn't say it back because I felt unsure."
        my "And it's been quite a while since I said those words to you, too."
        scene ep11_main2_party_end24 with dissolve
    my "So, there is something I don't understand either."
else:
    scene ep11_main2_party_end24 with dissolve
    my "And you're right; the focus hasn't been on our relationship for a long time. It's been all about trying to put out fires to have a better future."
    my "While doing that, I feel we've taken each other for granted. And that's not good."
    if ep10_jm_solo == "Maya":
        if ep10_feelingsForMaya:
            scene ep11_main2_party_end26 with dissolve
            my "I think I have unresolved feelings for [name], too. And I know this will hurt for you to hear, but recently, he told me he had feelings for me."
            scene ep11_main2_party_end27 with dissolve
            js "He did?"
            scene ep11_main2_party_end26 with dissolve
            my "Yeah..."
        else:
            scene ep11_main2_party_end26 with dissolve
            my "I haven't thought that much about you and me, and our future. I've been procrastinating when it comes to having those thoughts."
    else:
        if ep10_feelingsForJosy:
            scene ep11_main2_party_end26 with dissolve
            my "It hurts to hear that you did those things for [name] and that you are confused about us... But I can't say that I'm surprised, given our history."
        elif branchAlone:
            scene ep11_main2_party_end26 with dissolve
            my "It hurts to hear that you did those things for [name] and that you are confused about us..."
        else:
            scene ep11_main2_party_end26 with dissolve
            my "It hurts to hear that you did those things for [name] and that you are confused about us..."
        my "I haven't thought that much about you and me, and our future. I've been procrastinating when it comes to having those thoughts."
    scene ep11_main2_party_end24 with dissolve
    my "So, I'm in the same boat about us as you are."

my "I think it's good that you've spent some time alone thinking about all of this."
my "But I don't think we should postpone sharing these thoughts and having these talks anymore."
scene ep11_main2_party_end26 with dissolve
if ep10_got_contracts:
    my "My future and possibilities are changing now - hopefully for something much better."
else:
    my "Now that I've decided what to do with Dad, we can't continue to live on hope. We need to be realistic and think about how this will affect us."
if branchMayaJosy:
    my "You and I need to figure out where we'll go from here together."
    my "[name] is a part of it, too, but I feel you and I have issues between us on our own."
else:
    my "We need to figure out where we'll go from here together."
my "We owe each other to be open about everything, and I'm sorry I've kept secrets from you."
scene ep11_main2_party_end28 with dissolve
js "*{i}Exhales{/i}*"
js "I didn't expect you to take it this well."
scene ep11_main2_party_end24 with dissolve
my "Again, we understand each other better than we think. We share a lot of these worries and thoughts."
my "Are you willing to try it with me?"
scene ep11_main2_party_end28 with dissolve
js "I want and need that."
scene ep11_main2_party_end25 with dissolve
my "And you're right. We shouldn't have this talk during this party."
my "Let's make time for us and allow ourselves to dig in."
my "And also, let me support you for a while."
scene ep11_main2_party_end28 with dissolve
js "You're the best."
scene ep11_main2_party_end25 with dissolve
my "Let's have some more fun tonight."
scene ep11_main2_party_end29 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep11_main2_party_end30 with dissolve
$ renpy.pause()

if ep11_zoey_kiss == 2 and not wt_ep11_party_bella:
    jump ep11_pp_zoey_end2b_label
elif ep11_mg_party or wt_ep11_party_bella:
    if wt_ep9_branch_numbers != 1:
        label wt_ep11_bella_party_label:
        "scrappy" "On which route to play the next scene?"
        $ tmp_mod_list = []
        menu:
             "Sage" if branchSage:
                $tmp_mod2="Sage"
                if wt_ep9_branch_numbers != 1 and ep11_sage_camila_lewd:
                    menu:
                         "Sage scene on Bella's couch":
                            $ tmp_mod_list.append("Sage couch")
                            jump wt_ep11_bella_party_sage_label
                         "Sage x Camila threesome":
                            $ tmp_mod_list.append("Sage Camila")
                            if tmp_mod==1:
                                jump ep11_sage2_lewd_label
                            else:
                                jump wt_ep11_bella_party_sagexcamila_label
             "Maya & Josy" if branchMayaJosy:
                $tmp_mod2="Maya"
             "Isabella" if branchIsabella:
                $tmp_mod2="Isabella"
             "Jill" if branchJill:
                $tmp_mod2="Jill"
    else:
        if branchSage:
           $tmp_mod2="Sage"
        if branchIsabella:
           $tmp_mod2="Isabella"
        if branchJill:
           $tmp_mod2="Jill"
        if branchMayaJosy:
           $tmp_mod2="Maya"
    
    $tmp_mod=1
    if branchSage and tmp_mod2 == "Sage":
        
        
        
        if ep11_sage_camila_lewd:
            label wt_ep11_bella_party_sagexcamila_label:
            play music "music/ep11/licensed_music/track178.mp3"
            queue music ["music/ep11/licensed_music/track177.mp3","music/ep11/licensed_music/track181.mp3","music/ep11/licensed_music/track178.mp3"]
            scene ep11_main2_party_end31 with dissolve
            sa "Thanks for the party, everyone. [name] and I are taking off."
            scene ep11_main2_party_end32 with dissolve
            mc "We are?"
            scene ep11_main2_party_end33 with dissolve
            sa "We are."
            scene ep11_main2_party_end32 with dissolve
            mc "Oh... Ok."
            scene ep11_main2_party_end34 with dissolve
            isa "You're welcome to stay here if you want to."
            scene ep11_main2_party_end36 with dissolve
            sa "Thanks, but we'll take a raincheck on that."
            scene ep11_main2_party_end37 with dissolve
            mc "Thank you for the party, it was great. It made me look forward to the Christmas dinner."
            scene ep11_main2_party_end35 with dissolve
            isa "Don't get too excited. You'll have to wear clothes during that dinner."
            scene ep11_main2_party_end38 with dissolve
            mc "Bye, everyone!"
            jump ep11_sage2_lewd_label
        else:
            label wt_ep11_bella_party_sage_label:
            play music "music/ep11/oholynight.mp3"
            scene ep11_main2_party_end39 with dissolve
            ji "*{i}Yawns{/i}*"
            scene ep11_main2_party_end40 with dissolve
            js "It's getting late, isn't it?"
            scene ep11_main2_party_end43 with dissolve
            isa "You're welcome to stay here if you want to."
            scene ep11_main2_party_end42 with dissolve
            my "Can we?"
            scene ep11_main2_party_end43 with dissolve
            isa "I have a big bed and sofas. Take your pick."
            scene ep11_main2_party_end41 with dissolve
            sa "Yay, sleepover. Dibs on this sofa."
            scene ep11_main2_party_end40 with dissolve
            js "Maya and I can take the ones downstairs."
            jump ep11_sage_lewd_label
    elif branchJill  and tmp_mod2 == "Jill":
        play music "music/ep11/oholynight.mp3"
        scene ep11_main2_party_end39 with dissolve
        ji "*{i}Yawns{/i}*"
        scene ep11_main2_party_end40 with dissolve
        js "It's getting late, isn't it?"
        scene ep11_main2_party_end43 with dissolve
        isa "You're welcome to stay here if you want to."
        scene ep11_main2_party_end42 with dissolve
        my "Can we?"
        scene ep11_main2_party_end43 with dissolve
        isa "I have a big bed and sofas. Take your pick."
        scene ep11_main2_party_end53 with dissolve
        ji "Are you coming?"
        scene ep11_main2_party_end54 with dissolve
        mc "To the bed? Yeah."
        $ guideSuggestedPage = 222
        scene ep11_main2_party_end74 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end75 with dissolve
        ji "Good night. Thank you for this fun evening."
        scene ep11_main2_party_end76 with dissolve
        isa "Thank you. It was you guys who made it fun. Good night."
        scene ep11_main2_party_end77 with dissolve
        mc "Sleep tight. Thanks for letting us crash here tonight."
        scene ep11_main2_party_end78 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end79 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end80 with dissolve
        $ renpy.pause()
        if ep7_bella_lewd:
            scene ep11_main2_party_end81 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end82 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end83 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end84 with dissolve
            menu:
                "[m_c1]Comfort her":
                    $ ep11_bella_comfort = True
                    scene ep11_main2_party_end85 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end86 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end87 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end88 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end89 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end90 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end91 with dissolve
                    $ renpy.pause()
                    scene ep11_main2_party_end92 with dissolve
                    $ renpy.pause()
                    $ new_bio("Isabella", "I slept in the same bed as Bella and Jill. I comforted Bella when she looked sad, and we held hands together with Jill on my chest.")
                    $ new_bio("Jill", "I slept in the same bed as Bella and Jill. I comforted Bella when she looked sad, and we held hands together with Jill on my chest.")
                "Go to sleep":
                    scene ep11_main2_party_end80 with dissolve
                    $ renpy.pause()
    elif branchMayaJosy and tmp_mod2 == "Maya":
        play music "music/ep11/oholynight.mp3"
        scene ep11_main2_party_end39 with dissolve
        ji "*{i}Yawns{/i}*"
        scene ep11_main2_party_end40 with dissolve
        js "It's getting late, isn't it?"
        scene ep11_main2_party_end43 with dissolve
        isa "You're welcome to stay here if you want to."
        scene ep11_main2_party_end42 with dissolve
        my "Can we?"
        scene ep11_main2_party_end43 with dissolve
        isa "I have a big bed and sofas. Take your pick."
        scene ep11_main2_party_end41 with dissolve
        sa "Can you fit three people in that bed?"
        scene ep11_main2_party_end43 with dissolve
        isa "Sure can."
        
        if ep11_maya_love >= 2 and ep11_josy_love >= 2:
            scene ep11_main2_party_end56 with wipeleft
            $ renpy.pause()
            scene ep11_main2_party_end57 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end55 with dissolve
            $ renpy.pause()
            menu:
                "Spoon with Josy":
                    $ ep11_josy_spoon = True
                "Spoon with Maya":
                    $ ep11_josy_spoon = False

        elif ep11_maya_love >= 2:
            $ ep11_josy_spoon = False
            scene ep11_main2_party_end55 with wipeleft
            $ renpy.pause()
            scene ep11_main2_party_end56 with dissolve
            $ renpy.pause()
        elif ep11_josy_love >= 2:
            $ ep11_josy_spoon = True
            scene ep11_main2_party_end55 with wipeleft
            $ renpy.pause()
            scene ep11_main2_party_end57 with dissolve
            $ renpy.pause()
        else:
            scene ep11_main2_party_end56 with wipeleft
            $ renpy.pause()
            scene ep11_main2_party_end57 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end55 with dissolve
            $ renpy.pause()
            menu:
                "Spoon with Josy":
                    $ ep11_josy_spoon = True
                "Spoon with Maya":
                    $ ep11_josy_spoon = False

        if ep11_josy_spoon:
            scene ep11_main2_party_end58 with dissolve
            mc "Is there room for me?"
            scene ep11_main2_party_end59 with dissolve
            js "I'm sure there is room if you don't mind lying tight against me."
            scene ep11_main2_party_end58 with dissolve
            mc "I'd never mind that."
            scene ep11_main2_party_end60 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end61 with dissolve
            js "Good night, guys. *{i}Yawns{/i}* It's been one hell of a night."
            scene ep11_main2_party_end63 with dissolve
            my "Yeah... Good night."
            scene ep11_main2_party_end64 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end62 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end65 with dissolve
            $ renpy.pause()
        else:
            scene ep11_main2_party_end66 with dissolve
            mc "Is there room for me?"
            scene ep11_main2_party_end68 with dissolve
            my "We'll make it work somehow."
            my "But if I wake up with a boner between my asscheeks in the middle of the night, I'll spoon with Josy instead."
            scene ep11_main2_party_end67 with dissolve
            mc "Haha! I'll try my best to control it, but you never know."
            scene ep11_main2_party_end68 with dissolve
            my "I never do."
            scene ep11_main2_party_end69 with dissolve
            my "Good night, Josy."
            scene ep11_main2_party_end71 with dissolve
            js "Night..."
            scene ep11_main2_party_end72 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end70 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end73 with dissolve
            $ renpy.pause()
    elif branchIsabella and tmp_mod2 == "Isabella":
        play music "music/ep11/oholynight.mp3"
        scene ep11_main2_party_end39 with dissolve
        ji "*{i}Yawns{/i}*"
        scene ep11_main2_party_end40 with dissolve
        js "It's getting late, isn't it?"
        scene ep11_main2_party_end43 with dissolve
        isa "You're welcome to stay here if you want to."
        scene ep11_main2_party_end42 with dissolve
        my "Can we?"
        scene ep11_main2_party_end43 with dissolve
        isa "I have a big bed and sofas. Take your pick."
        scene ep11_main2_party_end44 with dissolve
        mc "Dibs on the bed..."
        scene ep11_main2_party_end46 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end45 with dissolve
        isa "*{i}Whispers{/i}* Not so subtle..."

        scene ep11_main2_party_end48 with dissolve
        isa "Jill?"
        scene ep11_main2_party_end49 with dissolve
        ji "Hm?"
        scene ep11_main2_party_end48 with dissolve
        isa "There's room for you, too."
        scene ep11_main2_party_end50 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end49 with dissolve
        ji "Ok..."
        scene ep11_main2_party_end47 with dissolve
        isa "You find blankets and such in the basket or the wardrobe in the hall. Go ahead and take whatever you need. Good night, everyone."
        scene ep11_main2_party_end51 with dissolve
        sa "They're going to sleep in the same bed? Am I missing something here?"
        scene ep11_main2_party_end52 with dissolve
        js "Well... There's something you should know..."

        scene ep11_main2_party_end74 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end93 with dissolve
        $ renpy.pause()
        scene ep11_main2_party_end94 with dissolve
        ji "You don't mind, do you?"
        scene ep11_main2_party_end95 with dissolve
        mc "No. As long as you don't."
        scene ep11_main2_party_end96 with dissolve
        isa "Lately, we've spent a lot of time together doing far worse things than sleeping in the same bed."
        isa "I'm sure we will survive."
        scene ep11_main2_party_end97 with dissolve
        $ renpy.pause()
        if ep9_b_kissed_jill:
            scene ep11_main2_party_end98 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end99 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end100 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end101 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end102 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end103 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end104 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end105 with dissolve
            $ renpy.pause()
            scene ep11_main2_party_end106 with dissolve
            $ renpy.pause()
            $ new_bio("Jill", "I slept in the same bed as Bella and Jill. They ended up holding hands together with Bella on my chest.")
            $ new_bio("Isabella", "I slept in the same bed as Bella and Jill. They ended up holding hands together with Jill on my chest.")
        
        if wt_ep9_branch_numbers != 1:
           "scrappy" "Watch the scene again on other paths?"
           menu:
               "Yes":
                  jump wt_ep11_bella_party_label
               "No. Continue the game.":
                   if ep11_zoey_kiss == 2:
                        jump ep11_pp_zoey_end2b_label
                   else:
                        pass
        
        jump ep11_gift_label
else:
    jump ep11_gift_label
if wt_ep9_branch_numbers != 1:
           "scrappy" "Watch the scene again on other paths?"
           menu:
               "Yes":
                  jump wt_ep11_bella_party_label
               "No. Continue the game.":
                   if ep11_zoey_kiss == 2:
                        jump ep11_pp_zoey_end2b_label
                   else:
                        pass
label ep11_gift_label:
$ guideSuggestedPage = 223
stop music fadeout 3
scene black with fade
$ renpy.pause(2)
hide screen new_phone_screen
play music "music/ep11/licensed_music/track186.mp3"
scene ep11_gift9 with Fade(1,1,1)
$ renpy.pause()
if minigames:
    $ renpy.block_rollback()
    $ pp_continue_label = "ep11_pp_cont2_label"

    if ep11_pp_game == 0 and ep11_mg_party:
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

    if ep11_pp_alcohol_food != 2:
        $ specialMessage = "DIKs' happiness increased!"
        if ep11_pp_alcohol_food == 0:
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+3,100)
            $ pp_happiness_level[1] = min(pp_happiness_level[1]+3,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+3,100)
            $ pp_happiness_level[3] = min(pp_happiness_level[3]+3,100)
            $ pp_happiness_level[4] = min(pp_happiness_level[4]+3,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+3,100)
            $ pp_happiness_level[6] = min(pp_happiness_level[6]+3,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+3,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Derek's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Jacob's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Jamie's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased John Boy's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Leon's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased [name]'s happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Rusty's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol and Food{/color} activity increased Tommy's happiness by {color=00ff00}+3%{/color}.")
        elif ep11_pp_alcohol_food == 1:
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
            $ pp_happiness_level[1] = min(pp_happiness_level[1]+2,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol{/color} activity increased Jacob's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Alcohol{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    else:
        $ specialMessage = "All DIKs' happiness decreased!"
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-2,0)
        $ pp_happiness_level[1] = max(pp_happiness_level[1]-2,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-2,0)
        $ pp_happiness_level[3] = max(pp_happiness_level[3]-2,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-2,0)
        $ pp_happiness_level[5] = max(pp_happiness_level[5]-2,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-2,0)
        $ pp_happiness_level[7] = max(pp_happiness_level[7]-2,0)

        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Derek's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Jacob's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Jamie's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased John Boy's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Leon's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased [name]'s happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Rusty's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}B.Y.O.B.{/color} activity decreased Tommy's happiness by {color=ff0000}-2%{/color}.")

    $ pp_update_happiness_icons()
    show screen specialmsg
    pause
    hide screen specialmsg
    jump party_planner_setup_evaluation_label
    label ep11_pp_cont2_label:
    $ renpy.block_rollback()

    $ tmpStr = ""
    if ep11_pp_alcohol_food == 2:
        $ tmpStr += "• B.Y.O.B. "
    elif ep11_pp_alcohol_food == 1:
        $ tmpStr += "• Alcohol "
    else:
        $ tmpStr += "• Alcohol and Food "
    if ep11_pp_contest == 1:
        $ tmpStr += "• Dildo Sucking Competition "
    elif ep11_pp_contest == 0:
        $ tmpStr += "• Wet T-shirt "
    if ep11_pp_game == 0:
        $ tmpStr += "• Guess Who? game"

    $ mphone_pp_history_list.append("DIKs' Christmas Panty party\n{color=fe9416}Activities:{/color} %s\n{color=fe9416}Total Party Score:{/color} {color=ffed00}%d{/color}\n{color=fe9416}Total Score:{/color} {color=ffed00}%d{/color}\n{color=e51475}Multiplier: [pp_multiplier]x{/color}\n{color=fe9416}Rank:{/color} {color=ffed00}%s{/color}" % (tmpStr,pp_round_score,pp_score,pp_party_rank[2][1]))
    $ mphone_pp_history_list.append("\n")
    $ mphone_pp_history_list.append("\n")

    if steamAchievements and not config.console and not config.developer:
        if pp_party_rank[2][0]==11 and pp_party_rank[2][1]=="S":
            $ achievement.grant("IDS3_22")
            init:
                $ achievement.register("IDS3_22")
            $ achievement.Sync()
else:
    $ party_planner_get_nm_rank(pp_current_party_happiness)
    $ party_planner_get_nm_score(pp_nm_dik_happiness)
show screen new_phone_screen
scene ep11_gift1 with dissolve
$ renpy.pause()
scene ep11_gift2 with dissolve
$ renpy.pause()

if ep11_zoey_kiss == 2:
    scene ep11_gift10 with dissolve
    $ renpy.pause()
    scene ep11_gift11 with dissolve
    zo "[name]? I'm gonna leave."
    scene ep11_gift12 with dissolve
    mc "Hm? Oh?"
    scene ep11_gift13 with dissolve
    zo "Thanks for letting me crash here."
    scene ep11_gift14 with dissolve
    menu:
        "What about last night?":
            mc "What about last night?"
            scene ep11_gift15 with dissolve
            zo "Nothing has changed for me overnight. But I think it's best if you get a chance to think and feel for yourself."
        "Stay for breakfast":
            mc "Why don't you stay for breakfast?"
            scene ep11_gift15 with dissolve
            zo "No. With what I said last night and all... I think it's best if you get a chance to think and feel for yourself."
    scene ep11_gift14 with dissolve
    mc "Ok..."
    scene ep11_gift13 with dissolve
    zo "You know where to find me."
    scene ep11_gift16 with dissolve
    $ renpy.pause()
    scene ep11_gift17 with dissolve
    mc "(She's right... I do need that.)"
    scene ep11_gift4 with dissolve
    $ renpy.pause()
if (ep11_mg_party or wt_ep11_party_bella) and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others):
    $ mgallery_add_photo("pic_group_mains_ep11")
    scene ep11_gift3 with dissolve
    mc "(It's eerily quiet. It must have been a great night here.)"
else:
    scene ep11_gift20 with dissolve
    $ renpy.pause()
    scene ep11_gift18 with dissolve
    mc "*{i}Yawns{/i}*"
    scene ep11_gift19 with dissolve
    mc "(Ugh... Stupid hangover... Dammit, yesterday-[name]... Why did you drink all that?)"
scene ep11_gift5 with dissolve
$ renpy.pause()
scene ep11_gift6 with dissolve
$ renpy.pause()
scene ep11_gift7 with dissolve
$ renpy.pause()
scene ep11_gift8 with dissolve
$ renpy.pause()

if ep5_dikWinner:
    if ep11_mg_party and ep11_zoey_kiss != 2 :
        scene ep11_gift21 with dissolve
    else:
        scene ep11_gift22 with dissolve
    mc "(Hm? Isn't that...?)"
    scene ep11_gift23 with dissolve
    mc "(Who the hell broke this?)"
    if ep11_mg_party and ep11_pp_game < 1:
        $ renpy.sound.set_volume(0,channel='music')
        $ renpy.music.play("music/ep11/licensed_music/track181.mp3", channel="music2")
        jump ep11_pp_act2_event2_label
        label ep11_gift2_label:
        $ renpy.music.stop(channel="music2", fadeout=0)
        $ renpy.sound.set_volume(1.0,channel='music')
    scene bg anim_helmet_ep11 movie with dissolve
    pause
    scene ep11_gift24 with dissolve
    mc "(Crappy glue... Get back on there...)"

scene ep11_gift25 with dissolve
if (ep11_mg_party or wt_ep11_party_bella):
    mc "(I had a great time last night. I made the right call about Bella's party, for sure.)"
    scene ep11_gift26 with dissolve
    if ep9_b_kissed_jill and branchIsabella:
        mc "(Maybe I'm reading into things, but it was weird how Bella and Jill held their hands on me when we went to sleep.)"
        mc "(Bella knows I've got a history with Jill... But Jill didn't seem to mind it... I don't know what to make of it.)"
    elif branchJill and ep11_bella_comfort:
        mc "(It was nice how Bella and Jill held hands on my chest when we went to sleep like that...)"
        mc "(But... Jill doesn't know that I have some history with Bella...)"
        mc "(Maybe I shouldn't have comforted Bella, but she looked sad... I wonder if it was because of me.)"
    else:
        $ renpy.pause()


    if branchSage and ep11_sage_love > 0:
        if ep11_sage_love == 2:
            scene ep11_gift27 with dissolve
            mc "(I love Sage. And she loves me... It's such a wonderful feeling.)"
        else:
            scene ep11_gift27 with dissolve
            mc "(I can't believe I told Sage that I love her...)"
            mc "(Maybe I'm reading into things but she never said it back... But the sex we had was so good and different...)"
            mc "(I think she feels the same and that was her way of showing it... But I'm not sure. I hope she loves me...)"
    if branchSage and ep11_sage_camila_lewd:
        scene ep11_gift27 with dissolve
        mc "(And that threesome was something else... Sage is amazing. I have the best girlfriend ever.)"
    else:
        scene ep11_gift27 with dissolve
else:
    $ renpy.pause()
    scene ep11_gift27 with dissolve
$ ep11_gift_opp = 0
if (not branchAlone or (branchAlone and wt_ep9_branch_numbers != 1)) and ep11_zoey_kiss == 2:
    mc "(Ugh... The Christmas gifts... I need to get something nice for Dad. And Bella's Christmas party is on Monday...)"
    if branchSage:
        scene ep11_gift28 with dissolve
        mc "(But it feels weird getting something for Sage after kissing Zoey...)"
        mc "(Sage is going to freak out on me... Especially since I reassured her about Zoey when she was concerned...)"
        if jade_state > 0:
            mc "(...I just keep finding ways to make it worse, and Sage doesn't even know it.)"
    if branchJill:
        scene ep11_gift28 with dissolve
        mc "(Buying something for Jill after kissing Zoey... That gift has guilt all written over it.)"
        mc "(But not giving her anything...? Fuck...)"
    if branchIsabella:
        scene ep11_gift28 with dissolve
        mc "(Buying something for Bella after kissing Zoey... That gift has guilt all written over it.)"
        mc "(What do I do?)"
    if branchMayaJosy:
        scene ep11_gift28 with dissolve
        mc "(Buying gifts for Josy and Maya after kissing Zoey... It feels so weird.)"
        mc "(What do I do?)"
    $ renpy.block_rollback()
    scene ep11_gift30 with dissolve
    call screen giftMsgScreen
    $ renpy.pause(0.5)
    stop music fadeout 3
    if ep11_gift_money > 0:
        $ specialMessage = "{size=-5}Extra money was returned to your wallet if possible.{/size}"
        show screen specialmsg
        $ mny(ep11_gift_money)
    mc "(Maybe I'll figure it out when I get to the mall. I've got some thinking to do.)"
else:
    mc "(I should buy Christmas gifts today. I need to get something nice for Dad... And Bella's Christmas party is on Monday...)"
    scene ep11_gift29 with dissolve
    mc "(Who else do I need to buy something for...?)"
    $ renpy.block_rollback()
    scene ep11_gift30 with dissolve
    call screen giftMsgScreen
    $ renpy.pause(0.5)
    if not branchJill or (branchJill and tc > 4):
        stop music fadeout 3
    if ep11_gift_money > 0:
        $ specialMessage = "{size=-%d}Extra money was returned to your wallet if possible.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ mny(ep11_gift_money)
    mc "(Maybe I'll figure it out when I get to the mall. I've got some thinking to do.)"
    if branchJill and tc < 5:
        stop music fadeout 3
        scene ep11_gift31 with dissolve
        mc "(Hm... Let's ask Jill if she wants to tag along...)"
if steamAchievements:
    if 0 not in ep11_gift_list and 1 not in ep11_gift_list:
        $ achievement.grant("IDS3_32")
        init:
            $ achievement.register("IDS3_32")
        $ achievement.Sync()
if branchJill and (ep11_zoey_kiss < 2 or wt_ep11_zoey_kiss_others): 
    jump ep11_jgifts_label

label ep11_jparty_label:
$ guideSuggestedPage = 225
play music "music/ep9/licensed_music/track131.mp3"
scene ep11_jparty1
show screen dance_filter_screen
with wipeleft
$ renpy.pause()
scene ep11_jparty2 with dissolve
dw "What's up with the HOTs? Are they sick or something?"
scene ep11_jparty3 with dissolve
al "I talked to Sarah and she said she's hungover."
al "The DIKs had a Christmas party, and the HOTs went there."
scene ep11_jparty4 with dissolve
dw "Get the fuck out of here!"
dw "Sage!"
show ep11_jparty5
if not persistent.ep11_cardmy4:
    show screen ep11_render_screen("my4")
with dissolve
sa "Hm?"
show ep11_jparty8
hide screen ep11_render_screen
with dissolve
dw "You girls broke our agreement."
scene ep11_jparty6 with dissolve
sa "We didn't. We're at your Christmas party tonight, as agreed upon. Aren't we?"
scene ep11_jparty8 with dissolve
dw "Yeah, but you went to the DIKs yesterday! All of you are completely hungover tonight."
scene ep11_jparty7 with dissolve
sa "We're not. I wasn't at their party, and neither were Josy and Maya. We were with friends all night. What the other HOTs did is up to them."
sa "We're HOTs, but we're also individuals, Dawe. We all make our own choices. And we're honoring the agreement tonight."
scene ep11_jparty9 with dissolve
al "They're here tonight, but they were there yesterday... Where do we draw the line with this?"
scene ep11_jparty11 with dissolve
dw "They're cheating, I'm telling you. And there's zero chance they're getting the New Year's party now."
scene ep11_jparty10 with dissolve
al "Didn't you already say it was ours?"
scene ep11_jparty11 with dissolve
dw "Yeah, but it's even more ours now."
stop music fadeout 3
scene ep11_jparty12 with dissolve
dw "Sage!"
hide screen dance_filter_screen

jump ep11_freeroam_room2_intro_label

label ep11_md_label:
hide screen new_phone_screen
play music "music/ep8/licensed_music/track72.mp3"
scene ep11_md1 with fade
my "Hey, Dad."
scene ep11_md2 with dissolve
pa "Your mom's resting. She's having a bad day."
scene ep11_md3 with dissolve
my "Is she sleeping?"
scene ep11_md2 with dissolve
pa "She's on the verge of it."
pa "Come on in."
scene ep11_md4 with dissolve
pa "You two are looking nice. What's the occasion?"
scene ep11_md5 with dissolve
de "We're celebrating Christmas tonight with friends."
scene ep11_md7 with dissolve
pa "Already? It's not even the weekend."
pa "So, that's why you need the car."
scene ep11_md8 with dissolve
pa "I'm happy you came... There's something I'd like to talk to you about..."
if ep10_got_contracts:
    scene ep11_md6 with dissolve
    my "We need to talk to you, too."
    scene ep11_md8 with dissolve
pa "Let's sit down. I made coffee."
scene ep11_md10 with dissolve
$ renpy.pause()
scene ep11_md9 with dissolve
$ renpy.pause()
scene ep11_md11 with dissolve
$ renpy.pause()
scene ep11_md12 with dissolve
pa "I've done some thinking...and it shouldn't have taken this long, but..."
pa "I want to apologize for Thanksgiving. It didn't turn out the way I wanted."
scene ep11_md25 with dissolve
$ renpy.pause()
scene ep11_md12 with dissolve
if ep8_told_josy_chad:
    pa "Your friends deserve an apology, too."
else:
    pa "Your friend deserves an apology, too."
scene ep11_md13 with dissolve
$ renpy.pause()
scene ep11_md28 with dissolve
if ep8_told_josy_chad:
    my "I'm sure they would appreciate that."
else:
    my "I'm sure he would appreciate that."
my "But..."
my "Are you sorry for what you did, or are you sorry that someone saw it?"
scene ep11_md29 with dissolve
$ renpy.pause()
scene ep11_md14 with dissolve
$ renpy.pause()
scene ep11_md15 with dissolve
$ renpy.pause()
scene ep11_md16 with dissolve
pa "Helen has had very dark thoughts lately. When she gets her episodes after taking her meds, she says horrible things."
pa "Things I don't want you to hear. Thoughts I want to protect you from."
scene ep11_md17 with dissolve
pa "But I don't know how long I can stand to hear about them myself."
scene ep11_md26 with dissolve
my "What is she saying?"
scene ep11_md15 with dissolve
pa "..."
scene ep11_md26 with dissolve
my "Dad? Tell us. We deserve to know."
scene ep11_md18 with dissolve
pa "How can I put this mildly to you...?"
pa "She says she doesn't want to go on living anymore. She says she wants to go to Canada or New Jersey to... Do you understand?"
scene ep11_md27 with dissolve
de "Does she mean it?"
scene ep11_md19 with dissolve
pa "No. I don't think that she does. It's the pain that makes her say it. And those meds are affecting her mood."
pa "She gets so mad. She screams at me. Nothing I do for her is enough."
pa "The Helen we know shines through that darkness when the episode is over."
scene ep11_md17 with dissolve
pa "But it's..."
pa "It eats me up hearing her say those things."
scene ep11_md30 with dissolve
de "Why haven't you told us earlier?"
scene ep11_md17 with dissolve
pa "I didn't want to put that burden on you."
scene ep11_md28 with dissolve
my "So, you chose to carry it all on your own? That's not healthy..."
scene ep11_md20 with dissolve
pa "I was raised not to talk about feelings."
pa "My father used to beat me up if I cried. And he'd get drunk and get abusive with my brother and mother, too."
scene ep11_md21 with dissolve
pa "The day he died...drunk in that bathtub. I felt relief."
pa "And I promised myself that I wouldn't turn out like him."
scene ep11_md22 with dissolve
pa "And I can see it now... I broke that promise on Thanksgiving."
scene ep11_md23 with dissolve
pa "*{i}Sobs{/i}*"
pa "I'm sorry. It wasn't supposed to turn out this way. Nothing was."
scene ep11_md24 with dissolve
pa "Life was supposed to be amazing for us."
pa "I'm sorry I couldn't fix everything."
scene ep11_md31 with dissolve
$ renpy.pause()
scene ep11_md32 with dissolve
$ renpy.pause()
scene ep11_md33 with dissolve
my "It wasn't just Thanksgiving, Dad."
my "But I...forgive you."
scene ep11_md34 with dissolve
$ renpy.pause()
if ep10_got_contracts:
    scene ep11_md33 with dissolve
    my "There's something you should know..."
    my "I'm paying for college on my own from now on."
    scene ep11_md35 with dissolve
    my "Thank you for lending me the money, but I've signed up for a student loan. I'll pay you back what I owe you."
    my "And if you're truly sorry about what you did... You can show me that by letting me do this."
    scene ep11_md36 with dissolve
    $ renpy.pause()
scene ep11_md37 with dissolve
$ renpy.pause()
scene ep11_md38 with dissolve
$ renpy.pause()

scene ep11_md39 with dissolve
$ renpy.pause()
if ep10_got_contracts:
    scene ep11_md40 with dissolve
    de "That didn't go the way I expected..."
    scene ep11_md43 with dissolve
    my "I practiced everything I wanted to say to him...and all those feelings and words I had prepared changed right then and there."
    scene ep11_md40 with dissolve
    de "You did the right thing."
else:
    scene ep11_md40 with dissolve
    de "I didn't expect him to apologize or say all those things."
    scene ep11_md43 with dissolve
    my "I know... I was stunned."
    scene ep11_md40 with dissolve
    de "You keep surprising me... You're amazing, you know that, right?"

scene ep11_md44 with dissolve
my "Do you think so?"
scene ep11_md40 with dissolve
de "I had a hard time doing what you did."
scene ep11_md44 with dissolve
my "But you forgave him, too."
scene ep11_md42 with dissolve
de "Only because my hero did it."
scene ep11_md45 with dissolve
my "Who? Me?"
scene ep11_md46 with dissolve
$ renpy.pause()
scene ep11_md40 with dissolve
de "Do you think he'll change, though?"
scene ep11_md43 with dissolve
my "Today, I saw something I never saw in him before."
my "I want to give him that chance."
scene ep11_md41 with dissolve
de "It was the first time I heard him talk about his dad."
scene ep11_md43 with dissolve
my "I know. I only knew that story through Mom."
my "He's had a rough childhood. He's carrying a lot."
if ep10_got_contracts:
    scene ep11_md40 with dissolve
    de "You did it, Sis... You took the leap."
    scene ep11_md44 with dissolve
    my "And I wish it felt better than it does."
    my "I didn't tell him anything about Josy... But I felt it could wait."
    scene ep11_md41 with dissolve
    de "Do you regret not telling him?"
    scene ep11_md43 with dissolve
    my "No. It wasn't the right time for it. The result is the same for me; I no longer have to hide it from him."
    my "He lost that power over me today."
    stop music fadeout 3
    scene ep11_md40 with dissolve
    de "That must feel great."
    scene ep11_md44 with dissolve
    my "I'm not sure yet."
else:
    scene ep11_md41 with dissolve
    de "You're carrying loads yourself."
    scene ep11_md44 with dissolve
    my "You're helping me carry it."
    my "Promise me we'll always be able to talk about feelings."
    scene ep11_md40 with dissolve
    de "I promise."
    stop music fadeout 3
    scene ep11_md44 with dissolve
    my "I hope he'll change. But I'm not willing to risk anything yet."

label ep11_christmas_label:
$ guideSuggestedPage = 226
show screen new_phone_screen
play music "music/ep11/licensed_music/track183.mp3"
scene ep11_christmas1 with wipeleft
ji "The place looks great. Did you do all of this by yourself?"
scene ep11_christmas2 with dissolve
isa "Thank you. Yes, I wanted to make room for everyone, and as a bonus, we get to view the Christmas tree while we're eating."
isa "And by the way, you can put the gifts you brought underneath it."
scene ep11_christmas3 with dissolve
ji "Can I help out with the food?"
scene ep11_christmas2 with dissolve
isa "I could use another set of hands."
scene ep11_christmas4 with dissolve
sa "Haha! I love that Christmas sweater. Where did you get it?"
scene ep11_christmas5 with dissolve
my "I got it for Christmas last year from Mom and Dad. It's both stupid and cute at the same time."
scene ep11_christmas6 with dissolve
de "Wow, everyone's dressed as if it's the real deal tonight."
scene ep11_christmas7 with dissolve
sa "Yes, we all look amazing. Nice bow tie."
scene ep11_christmas6 with dissolve
de "Classy, huh?"
show ep11_christmas8
if not persistent.ep11_cardmy5:
    show screen ep11_render_screen("my5")
with dissolve
ji "You went out of your way. This looks delicious."
show ep11_christmas9
hide screen ep11_render_screen
with dissolve
isa "It's the one Christmas I plan to celebrate this year, so why not?"
scene ep11_christmas12 with dissolve
ji "Are you holding up ok?"
scene ep11_christmas10 with dissolve
isa "Thank you. I feel better than I did last year."
isa "How about you? How is the family?"
scene ep11_christmas13 with dissolve
ji "It won't be the best Christmas at our place, I can tell you that much. Dad's been drinking a bit too much lately."
scene ep11_christmas10 with dissolve
isa "*{i}Sigh{/i}*"
scene ep11_christmas14 with dissolve
ji "But I have some good news, too. I met up with Jonathan. It's going to happen this spring."
scene ep11_christmas11 with dissolve
isa "It is?"
scene ep11_christmas14 with dissolve
ji "We started making plans for it and he's on board."
ji "There are many possibilities, but I don't know where to start. But luckily, he does."
ji "He'll help me set everything up. We talked about a website, donations, outreach, seminars..."
scene ep11_christmas11 with dissolve
isa "It sounds like it will require a lot of time and effort on your end."
scene ep11_christmas15 with dissolve
ji "It will. But it's what I want to do."
scene ep11_christmas11 with dissolve
isa "I know, and I'm so happy for you. It must feel incredible to get started."
stop music fadeout 3
scene ep11_christmas14 with dissolve
ji "It does."

label ep11_prep_label:
play music "music/ep2/freedom.mp3"
scene ep11_prep1 with dissolve
$ renpy.pause()
scene ep11_prep2 with dissolve
$ renpy.pause()
scene ep11_prep3 with dissolve
$ renpy.pause()
scene ep11_prep4 with dissolve
cr "Oh, man... That won't stop being funny."
scene ep11_prep5 with dissolve
go "I feel bad for him but can't hide my laughter. It hurts my balls to watch him walk."
scene ep11_prep6 with dissolve
lu "Hey, guys. So... Notice anything different?"
scene ep11_prep8 with dissolve
cr "New suit?"
scene ep11_prep9 with dissolve
lu "Sure is."
scene ep11_prep7 with dissolve
go "Wait a minute..."
scene ep11_prep6 with dissolve
lu "Yeah? Do you see it?"
scene ep11_prep7 with dissolve
go "Isn't that...?"
scene ep11_prep8 with dissolve
cr "Is that Tybalt's suit?"
scene ep11_prep9 with dissolve
lu "Don't be ridiculous. It's my suit. It just happens to be identical."
scene ep11_prep10 with dissolve
go "Haha, you didn't!"
go "He's going to punish you for stealing his look like that. He didn't want me to get the same glasses he wears."
scene ep11_prep11 with dissolve
lu "He can't punish me for wearing a suit. I'd like to see him try."
scene ep11_prep10 with dissolve
cr "What are you doing? It's fun, but...think about your future network. Do you want to be on his bad side?"
stop music fadeout 3
scene ep11_prep12 with dissolve
$ renpy.pause()
scene ep11_prep13 with dissolve
$ renpy.pause()
play music "music/ep11/licensed_music/track162.mp3"
scene ep11_prep14 with dissolve
$ renpy.pause()
scene ep11_prep15 with dissolve
$ renpy.pause()
scene ep11_prep16 with dissolve
$ renpy.pause()

scene ep11_jocks_end1 with dissolve
dw "Hey!!! Guys! We got more letters in our names!"
scene ep11_jocks_end2 with dissolve
cb "Who the fuck sends letters these days?"
play sound "sound_effects/interlude/page_turn.mp3"
scene ep11_jocks_end3 with dissolve
dw "Hey!"
scene ep11_jocks_end4 with dissolve
ch "I'm sparing you the horror."
scene ep11_jocks_end5 with dissolve
jo "How many more guys has Arieth banged since last time?"
scene ep11_jocks_end6 with dissolve
jy "Not me. I can tell you that much."
scene ep11_jocks_end5 with dissolve
jo "You'll get your turn, I'm sure."
scene ep11_jocks_end6 with dissolve
jy "I don't want a turn; she's getting fat."

play sound "sound_effects/interlude/page_turn.mp3"
scene ep11_jocks_end7 with hpunch
cb "Stop hogging the letters. Who are they for?"
scene ep11_jocks_end8 with dissolve
ch "Give them back."
cb "Dawe."
scene ep11_jocks_end9 with dissolve
cb "Anthony."
scene ep11_jocks_end10 with dissolve
cb "Chad."
scene ep11_jocks_end11 with dissolve
ch "Give it."
scene ep11_jocks_end12 with dissolve
cb "What are you mad about?"
scene ep11_jocks_end11 with dissolve
ch "It's not yours to read."
scene ep11_jocks_end13 with dissolve
dw "The DIKs put the condom in my shaker!? I drank their cum!?"
scene ep11_jocks_end14 with dissolve
jo "You drank someone's splooge?"
scene ep11_jocks_end15 with dissolve
an "Ashley...? What is this?"
scene ep11_jocks_end16 with dissolve
cb "I bet yours has something to do with Sage... Let's find out."
play sound "sound_effects/hit.mp3"
scene ep11_jocks_end17 with hpunch
$ renpy.pause()
play sound "sound_effects/hit.mp3"
scene ep11_jocks_end18 with hpunch
cb "Grrr!!!"
scene ep11_jocks_end19 with dissolve
dw "Hey! Hey! Stop it!"
al "Dammit! You were supposed to stop taking those supplements before the competition. Did you forget?"
scene ep11_jocks_end20 with dissolve
$ renpy.pause()
scene ep11_jocks_end21 with dissolve
cb "What the fuck is in that letter? He's hiding something. That's not a normal reaction."
scene ep11_jocks_end22 with dissolve
an "I knew Derek was up to something. I'm gonna kill him!"
scene ep11_jocks_end23 with dissolve
al "Sign me up. I'm getting tired of this bullshit deal you guys made."
al "It took them what? One party to find a way to screw us over."
scene ep11_jocks_end24 with dissolve
jy "Yeah! Dawe? This gotta warrant a pass, right? They can't do all this and expect us not to fight with them."
scene ep11_jocks_end25 with dissolve
dw "..."

label ep11_war_label:
scene ep11_war14 with dissolve
$ renpy.pause()
scene ep11_war15 with dissolve
$ renpy.pause()
scene ep11_war16 with dissolve
$ renpy.pause()
scene ep11_war17 with dissolve
$ renpy.pause()
scene ep11_war18 with dissolve
$ renpy.pause()
scene ep11_war19 with dissolve
$ renpy.pause()
scene ep11_war20 with dissolve
$ renpy.pause()
scene ep11_war21 with dissolve
$ renpy.pause()
scene ep11_war22 with dissolve
$ renpy.pause()
scene ep11_war23 with dissolve
$ renpy.pause()
scene ep11_war29 with dissolve
$ renpy.pause()
scene ep11_war24 with dissolve
$ renpy.pause()
scene ep11_war25 with dissolve
$ renpy.pause()
scene ep11_war26 with dissolve
$ renpy.pause()
scene ep11_war27 with dissolve
$ renpy.pause()
if ep11_rio_text > 0:
    if ep11_rio_text == 1:
        scene ep11_war28 with dissolve
    elif ep11_rio_text == 2:
        scene ep11_war28b with dissolve
    elif ep11_rio_text == 3:
        scene ep11_war28c with dissolve
    elif ep11_rio_text == 4:
        scene ep11_war28d with dissolve
    elif ep11_rio_text == 5:
        scene ep11_war28e with dissolve
    $ renpy.pause()
scene ep11_war11 with dissolve
$ renpy.pause()
scene ep11_war12 with dissolve
$ renpy.pause()
scene ep11_war13 with dissolve
$ renpy.pause()
scene ep11_war1 with dissolve
$ renpy.pause()
scene ep11_war2 with dissolve
$ renpy.pause()
scene ep11_war3 with dissolve
qu "I'm sorry, Dad..."
scene ep11_war4 with dissolve
$ renpy.pause()
scene ep11_war3 with dissolve
qu "We do anything to survive, yeah? Maybe the ermine learned one of the tricks from the rat?"
scene ep11_war5 with dissolve
$ renpy.pause()
scene ep11_war6 with dissolve
$ renpy.pause()
scene ep11_war7 with dissolve
$ renpy.pause()
scene ep11_war8 with dissolve
$ renpy.pause()
scene ep11_war9 with dissolve
$ renpy.pause()
scene ep11_war10 with dissolve
$ renpy.pause()
scene bg anim_quinn_end_ep11 movie with dissolve
pause
stop music fadeout 5

label ep11_nerds_label:
scene ep11_nerds1b
show screen redacted_screen
with dissolve
$ renpy.pause()
scene ep11_nerds2
hide screen redacted_screen
with dissolve
rn "Hey..."
scene ep11_nerds3 with dissolve
mg "Hm?"
play music "music/ep6/skeleton_keys.mp3"
scene ep11_nerds4 with dissolve
rn "Someone dropped this letter off for you."
scene ep11_nerds5 with dissolve
mg "What? Who?"
rn "It was a good-looking guy."
scene ep11_nerds6 with dissolve
$ renpy.pause()
scene ep11_nerds7 with dissolve
mg "Very funny."
scene ep11_nerds8 with dissolve
rn "Hahaha! You should have seen your face."
scene ep11_nerds10 with dissolve
mg "Were you successful?"
scene ep11_nerds9 with dissolve
rn "Yeah, but you have no idea how hard it was..."
scene ep11_nerds10 with dissolve
mg "I don't care as long as it's done."
scene ep11_nerds9 with dissolve
rn "It's done. The only one I'm worried about not taking the bait is Chad."
scene ep11_nerds11 with dissolve
mg "I wouldn't worry too much about it. He can't afford to buddy up with [name]."
mg "And if things don't transpire as planned, there's always plan B."
mg "Ron... Good times are coming."
scene ep11_nerds12 with dissolve
mg "The tri-alphas, the alpha nu omegas, the delta iota kappas... Finally, they will all get what's coming to them."
mg "And before they realized what happened, they would have punched each other out."
mg "When we're done, the only frat worth its salt on campus is ours."
scene ep11_nerds13 with dissolve
rn "I can't fucking wait. It's going to be one hell of a show."
scene ep11_nerds14 with dissolve
mg "The war of retribution is coming. Let the underlings know."
scene ep11_nerds15 with dissolve
rn "Will do, Sir Magnar."
scene ep11_nerds14 with dissolve
mg "Ready thy shivs and sharpen my blade."
mg "The DIKs won't see the dawn of spring. And like a house of cards, they all shall fall."
stop music fadeout 3
scene ep11_nerds16 with dissolve
mg "Oh, and bring me a milkshake when you're done. I've got a craving for one."

label ep11_ending_label:
play music "music/ep9/licensed_music/track114.mp3"
scene ep11_ending1 with dissolve
de "If I may, I'd like to say something..."
scene ep11_ending2 with dissolve
de "I'd like to thank Bella for bringing us all together here tonight."
de "Maybe I'm only speaking for myself, but it's great that we celebrate Christmas an extra time this year - it's a great way to kick finals week off."
de "Now, Christmas is all about traditions - every family has different ones. And I'd like to propose a tradition of our own."
scene ep11_ending3 with dissolve
de "As a tradition in our new weird family, I'd like to start us off with some Champagne."
scene ep11_ending4 with dissolve
my "That's sparkling wine."
scene ep11_ending6 with dissolve
de "Same thing."
scene ep11_ending11 with dissolve
sa "It's not."
scene ep11_ending6 with dissolve
de "Almost."
scene ep11_ending12 with dissolve
isa "Luckily, none of us is French. You would have gotten punched."
scene ep11_ending5 with dissolve
de "Don't ruin this moment for me."
scene ep11_ending7 with dissolve
de "I've waited all day to use this."
scene ep11_ending14 with dissolve
ji "Uhm... What is that?"
scene ep11_ending7 with dissolve
de "It's a saber."
scene ep11_ending8 with dissolve
mc "Dude, be careful! Watch where you point that thing."
scene ep11_ending13 with dissolve
isa "Is that a saber? It looks more like a sword."
scene ep11_ending9 with dissolve
de "Look, these things get expensive. I had to cut some corners, but the thought is what matters."
de "Let's have some Champagne together to celebrate Christmas, ok?"
scene ep11_ending15 with dissolve
ji "Sure. Did you bring some?"
scene ep11_ending16 with dissolve
"*{i}Laughter{/i}*"
scene ep11_ending9 with dissolve
de "You know what? I'll bring this tradition to another family. You guys suck."
scene ep11_ending17 with dissolve
js "We're just joking around. I won't say no to some of that bubbly."
scene ep11_ending10 with dissolve
de "At least one of you gets to share this bottle with me."
scene ep11_ending18 with dissolve
de "Merry Christmas, everyone!!!"
play sound "sound_effects/season3/champagne_pop.mp3"
scene bg anim_saber_ep11 movie with dissolve
pause
stop music
scene ep11_ending19
de "AHHHH!!!"
play music "music/ep11/licensed_music/track154.mp3"
scene ep11_ending20 with dissolve
ji "Oh my God! What did you do!?"
scene ep11_ending21 with dissolve
my "Derek!?"
play sound "sound_effects/table_slam.mp3"
$ renpy.sound.play("sound_effects/glass.mp3", channel="sfx2", loop=False)
$ renpy.sound.play("sound_effects/season2/bottle_smash.mp3", channel="sfx3", loop=False)
scene ep11_ending22 with vpunch
de "AHHHHH!!!"
"*{i}Gasps{/i}*"
scene ep11_ending23 with dissolve
mc "Bro, what the fuck!?"
scene ep11_ending24 with dissolve
js "What do we do? What do we do?"
scene ep11_ending25 with dissolve
sa "Someone help me find the finger! We need to put it on ice!"
scene ep11_ending26 with dissolve
isa "I'll get the ice! Wrap his hand and finger with towels! We need to get to a hospital as soon as possible!"
scene ep11_ending27 with dissolve
de "I'm gonna pass out here, [mc_de]! I'm bleeding out!!!"
scene ep11_ending28 with dissolve
mc "Hey! Hey! Stay awake!"
mc "Everything is gonna be ok. Look! We'll find your finger and be off to the hospital, ok?"
scene ep11_ending29 with dissolve
my "Where are the towels!?"
scene ep11_ending30 with dissolve
my "Uh..."
scene ep11_ending31 with dissolve
mc "What is it?"
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
scene ep11_ending32 with dissolve
mc "..."
stop music fadeout 3
scene ep11_ending33 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep11_ending34 with dissolve
$ renpy.pause()

scene black
stop music fadeout 10
$ renpy.pause(2)
jump ep11_save_here_label

label ep11_save_here_label:
hide screen new_phone_screen
scene black
$ renpy.pause(1)
$ persistent.ep11_completed = True
$ updateDikScore()

if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("IDS3_04")
    init:
        $ achievement.register("IDS3_04")
    $ achievement.Sync()
    call check_steam_achievements_label from _call_check_steam_achievements_label_3

if renpy.loadable("scripts/episode12/update12.rpyc"):
    scene ep11_episode_endb
else:
    scene ep11_episode_end
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


jump ep11_generate_report_text_label
$ renpy.pause()

label ep11EndLabel:
stop music fadeout 2
$ renpy.pause(2)

if renpy.loadable("scripts/episode12/update12.rpyc"):
    jump startUpdate12
$ qM = persistent.quick_menu
$ quick_menu = 0
jump game_credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

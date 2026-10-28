label startUpdate10:
jump header_ep10_label
label previousEp10Label:
$ guideSuggestedPage = 91
play music "music/patched/track_previous2.mp3"
scene black
$ renpy.pause(2)
hide screen new_phone_screen
$ previousEpLabel = "startUpdate10b"
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen
scene ep3_maya_wedb with wipeleft
mc "Say, who was that man leaving our dorm?"
scene ep3_maya_wedd
my "That was my dad, you see?"
scene ep6_mj_end10
my "My dad is keeping my life hostage."
scene ep6_mj_end29
my "He fooled me into co-signing my student loan and afterward he gave me the ultimatum that I couldn't see Josy ever again."

scene ep9_burkes109
sb "So... You're under the impression that I can help you with a scholarship, correct?"
scene ep9_burkes111
my "I'm having some family issues affecting my studies."
my "I even pledged the sorority thinking I'd get help with free tuition."
scene ep9_burkes115
sb "I'm confused. Did they say you'd get tuition from pledging?"
scene ep9_burkes151
js "*{i}Whispers{/i}* How did it go?"
scene ep9_burkes152
my "*{i}Whispers{/i}* Not that well... He can't help me."

if branchJill:
    scene ep9_diks_ph2_jmtalk_event30
else:
    scene ep9_diks_ph2_jmtalk_event30b
my "I've been looking for someone to ask a few questions about something."
if branchJill:
    scene ep9_diks_ph2_jmtalk_event27
else:
    scene ep9_diks_ph2_jmtalk_event27b
ji "My family's lawyer is at my disposal if need be, so..."


scene ep8_midterms27 with wiperight
mc "(Uh... What the fuck!? These seem like test questions and answers.)"
if ep8_midterms_cheated == "CHICK":
    scene ep8_midterms28 with dissolve
    mc "(I'm flushing these. I can't risk leaving them here.)"
elif ep8_midterms_cheated == "DIK":
    scene ep8_midterms28 with dissolve
    mc "(Let me look at some of the answers, though...)"
else:
    scene ep8_midterms28 with dissolve
    mc "(I think it's best to put them back and hide them better.)"

play sound "sound_effects/shove.mp3"
scene ep8_midterms77 with hpunch
mc "Dude... You can't leave papers in the bathroom during an exam like that."
scene ep8_midterms81
de "They weren't mine. Was someone cheating? For real?"


scene ep9_zoey_talk27 with wipeleft
mc "Why are you back?"

scene ep9_zoey_talk36
zo "I missed this place. And I...I missed you."
scene ep9_zoey_talk31
zo "You're mad at me..."
scene ep9_zoey_talk32
if ep9_mad_at_zoey:
    mc "You're damned right I'm mad at you."
else:
    mc "My feelings are all over the place right now."
scene ep9_derek4_talk1
de "You invited your ex to our Halloween party?"
scene ep9_dik1_zoey_event1
mc "(Zoey doesn't have a hard time talking to new people. They seem enthusiastic about talking to her.)"

if ep9_photos[14]:
    scene ep9_diks_ph2_zoey_event68
    zo "You're laughing at my demon face!? Come on, warrior! Slay me! BLARGH!"
    scene ep9_diks_ph2_zoey_event70 with dissolve
    $ renpy.pause()

if ep9_mad_at_zoey:
    scene ep9_diks_ph3_zoey2_event9
    mc "I still have things to say to you and thoughts to process."
    scene ep9_diks_ph3_zoey2_event8
    zo "So, say them."
    scene ep9_diks_ph3_zoey2_event9
    mc "I can't tonight."

scene ep9_party_planning22 with wiperight
tm "Do you even know what makes a great party?"

if ep9_drinking_competition:
    scene ep9_diks_ph1_drinking_event39
    mc "They're all on beer number three now! Shout out for your favorite, people!"
elif ep9_body_shots:
    if ep9_body_shots_becky:
        scene ep9_diks_ph1_drinking_event84
    else:
        scene ep9_diks_ph1_drinking_event112
    tm "Count Cockula is my name and body shots is the game!"
else:
    tm "Our parties aren't remembered for being boring. Things need to happen to make them fun."

scene ep9_quinn_talk67 with wipeleft
ar "Who's excited about Halloween!?"
scene ep9_quinn_talk71
dw "Arieth!? Where are we going!?"
scene ep9_quinn_talk47
qu "Trust me. They won't be a problem tonight."

scene ep9_diks_ph3_preps_event1
jb "[name]. We need some backup at the front door. Preps are showing up."
scene ep9_diks_ph3_preps_event8
lu "Can we join your party? We really wanna go."
if ep9_prep_truce:
    scene ep9_diks_ph3_preps_event9
    mc "Ok. Get in here. But if anything happens..."
    scene ep9_diks_ph3_preps_event12
    go "Much obliged!"
else:
    if affinity == "DIK" and not ep8_prep_truce:
        play sound "sound_effects/door_slam.mp3"
        scene ep9_diks_ph3_preps_event14 with hpunch
        mc "Hell no. Fuck off!"
    else:
        scene ep9_diks_ph3_preps_event13
        mc "Stick to your party and leave ours alone."

if branchIsabella:
    scene ep9_diks_ph3_costume_event1c
else:
    if branchJill:
        scene ep9_diks_ph3_costume_event1b
    else:
        scene ep9_diks_ph3_costume_event1
sa "Is everyone having a good time?"
"*{i}Cheers{/i}*"


scene ep9_ph2_josy_event4 with wiperight
js "He asked me a lot about myself before that, pretending to be interested. Like, hobbies and whatnot?"
js "He called me a run-of-the-mill boring and basic bitch."

if ep9_josy_choice == "DIK":
    play sound "sound_effects/hit.mp3"
    scene ep9_ph2_josy_event18 with hpunch
    "*{i}Gasps{/i}*"
    scene ep9_ph2_josy_event22b
    tm "What the fuck happened?"
    scene ep9_ph2_josy_event23
    gi "[name] punched Oscar. Like, what the fuck!?"
elif ep9_josy_choice == "NEUTRAL":
    play sound "sound_effects/shove.mp3"
    scene ep9_ph2_josy_event31 with hpunch
    mc "Get the fuck out!"
    scene ep9_ph2_josy_event22b
    tm "What the fuck happened?"
    scene ep9_ph2_josy_event23
    gi "[name] shoved Oscar and made him leave. Like, what the fuck!?"
else:
    scene ep9_ph2_josy_event11
    mc "Exactly. You deserve to be treated better. Let's ignore him."

if ep9_jm_sad:
    scene ep9_jm_breakup9 with wipeleft
    if branchJill:
        mc "I didn't stop dating Jill, and with time we... She's my girlfriend."
    elif branchSage:
        mc "Sage and I have gotten close. Ever since I got here, we've been hanging out."
    elif branchIsabella:
        mc "I didn't stop dating, and I think I found something I want to pursue..."
    scene ep9_jm_breakup13 with dissolve
    $ renpy.pause()
    scene ep9_jm_breakup14 with dissolve
    mc "Josy, please, don't go..."

if branchMayaJosy and wt_ep9_end_pick=="Maya":
    scene ep9_jm_committing20 with wipeleft
    my "Do I have a girlfriend and a boyfriend now?"
    scene ep9_jm_committing22
    mc "I'm luckier than you. I have TWO girls."
    scene ep9_jm_bed14
    js "Something I think we three have in common is our mothers, in a sense."
    js "We've all got weird \"mother situations\"."
    scene ep9_jm_bed18
    mc "Oh? That means..."
    scene ep9_jm_bed19
    my "I'm drunk. I feel like I'm gonna cry if I start talking about it."
    scene ep9_ending_maya_josy15
    le "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the waaaalk!"
    scene ep9_ending_maya_josy17
    tm "..."
if branchSage and wt_ep9_end_pick=="Sage":
    scene anim_sage_wakeup_ep9 with wipeleft
    sa "[name]...? Wake up..."
    scene ep9_ending_sage6
    sa "So... I was gonna do the walk. Are you ok with that?"
    scene ep9_ending_sage18
    dikcs "*{i}Sings{/i}* The walk of shaaaame! The walk of shaaaame!"
    scene ep9_ending_sage13
    sa "Damn, you guys are out of tune. You need singing lessons."
if branchJill and wt_ep9_end_pick=="Jill":
    if ep9_told_jill:
        scene ep9_diks_ph3_bm_event1 with wipeleft
        mc "I saw them making out."
        scene ep9_diks_ph3_bm_event4
        ji "Matthew? And...Olivia? Oh my God... Bianca..."
        scene ep9_ending_jill12
    else:
        scene ep9_ending_jill12 with wipeleft
    mc "Everyone. This is my girlfriend. Jill."
    scene ep9_ending_jill18
    le "*{i}Whispers{/i}* Jill Royce? That's fucking huge."
if branchIsabella and wt_ep9_end_pick=="Bella":
    scene ep9_bella_branch108 with wipeleft
    mc "No one knows it's you."
    scene ep9_bella_branch117
    de "And...hm... Who did you bring? I can't even guess..."
    de "Seriously, who are you?"
    scene ep9_bella_branch120
    isa "*{i}Low voice{/i}* A thirsty mummy."
    scene ep9_ending_isabella14
    isa "*{i}Smack{/i}*"
    scene ep9_ending_isabella16
    ni "Morning... Uh... Someone's in the bathroom..."
if branchAlone and (wt_ep9_end_pick=="Other" or wt_ep9_end_pick=="Quinn" or wt_ep9_end_pick=="Sarah" or wt_ep9_end_pick=="Lily"):
    scene ep9_others_branch6 with wipeleft
    de "So, who are you dating right now?"
    scene ep9_others_branch7
    if ep8_nora_number or ep7_lily_lewd or ep6_envy_lewd or envyLikesYou or ep8_quinn_lewd or jade_state == 1:
        mc "I'm not dating anyone, but I see the potential."
    else:
        mc "No one... I literally have nothing going on for me."
    if ep9_lily_nicole_lewd:
        if ep9_spoon_nicole:
            scene ep9_ending_nicole_lily21
            nic "*{i}Smack{/i}*"
            scene ep9_ending_nicole_lily22
            nic "[name]... Who are you? I really wanna know."
        elif ep9_spoon_lily:
            scene ep9_ending_nicole_lily32
            ly "Don't fall in love with me, [name]."
            scene ep9_ending_nicole_lily33
            mc "Huh? Why is that? I mean, I'm not, but...why?"
    elif ep9_quinn_lewd:
        scene ep9_quinn_lewd71
        qu "Fall the fuck asleep already, so I can pretend this doesn't suck."
        scene ep9_quinn_lewd76 with dissolve
        mc "*{i}Smack{/i}*"
        scene ep9_quinn_lewd77 with dissolve
        $ renpy.pause()
        scene ep9_quinn_lewd78 with dissolve
        qu "*{i}Smack{/i}*"
    elif ep9_sarah_melanie_lewd:
        scene ep9_sm_lewd25
        if ep9_sm_anal:
            mc "I wanna fuck your asses. Both of yours."
        else:
            mc "I wanna fuck you. Both of you."
        scene bg anim_sm_ending_ep9 movie with dissolve
        $ renpy.pause()
    else:
        scene ep9_ending_others8
        mc "Girls? You're in my bed."
        if ep9_tiffani_gina_tara:
            scene ep9_ending_others29
            mc "(It's gonna be a long night...)"
        else:
            scene ep9_ending_others35
            mc "(Next party, I'm locking my door before the party ends.)"
scene ep9_ending5 with wiperight
$ renpy.pause()
scene ep9_ending7
$ renpy.pause()

label startUpdate10b:
if steamConfig or nonPatreonConfig:
    if branchIsabella:
        $ state = "ep10_steam_isabella"
    elif branchSage:
        $ state = "ep10_steam_sage"
    elif branchMayaJosy:
        $ state = "ep10_steam_jm"
    elif branchJill:
        $ state = "ep10_steam_jill"
    else:
        if ep9_lily_nicole_lewd and ep9_spoon_nicole:
            $ state = "ep10_steam_others"
        elif ep9_quinn_lewd:
            $ state = "ep10_steam_others3"
        elif ep9_lily_nicole_lewd and ep9_spoon_lily:
            $ state = "ep10_steam_others4"
        elif ep9_riona_choice == "DIK":
            $ state = "ep10_steam_others2"
        else:
            $ state = "ep10_steam_others5"
else:
    if branchIsabella:
        $ state = "ep10_isabella"
    elif branchSage:
        $ state = "ep10_sage"
    elif branchMayaJosy:
        $ state = "ep10_jm"
    elif branchJill:
        $ state = "ep10_jill"
    else:
        if ep9_lily_nicole_lewd and ep9_spoon_nicole:
            $ state = "ep10_others"
        elif ep9_quinn_lewd:
            $ state = "ep10_others3"
        elif ep9_lily_nicole_lewd and ep9_spoon_lily:
            $ state = "ep10_others4"
        elif ep9_riona_choice == "DIK":
            $ state = "ep10_others2"
        else:
            $ state = "ep10_others5"
call rpc from _call_rpc_2
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black
$ renpy.pause(0.5)

label ep10_intro_label:
play music "music/ep10/licensed_music/track138.mp3"
scene ep10_intro1 with fade
$ renpy.pause()
scene ep10_intro2 with dissolve
$ renpy.pause()
scene ep10_intro3 with dissolve
$ renpy.pause()
scene ep10_intro4 with dissolve
doc "Good morning, Helen. How are you feeling today?"

scene ep10_intro5 with dissolve
hl "It's still before noon. I'm not at my best, doctor. Haha!"
scene ep10_intro6 with dissolve
doc "Are you doing your exercises?"
scene ep10_intro7 with dissolve
hl "Three times per day. But my joints are locking up."
scene ep10_intro6 with dissolve
doc "Yes, I can tell that they are stiff."
scene ep10_intro7 with dissolve
hl "Doctor... Will I ever get better?"
scene ep10_intro8 with dissolve
doc "Auto-immune diseases aren't curable, but they are treatable."
doc "There are treatments for arthritis we can try, and we have a lot of available options."
doc "I'll make sure to guide you through what else we can offer after we're done with the examination."
scene ep10_intro9 with dissolve
hl "..."
scene ep10_intro10 with dissolve
doc "Helen. It's treatable."
doc "You must not lose hope."
scene ep10_intro11 with dissolve
hl "Oh, believe me. I've got hope - an abundance of it."
hl "And a wonderful family worth fighting for."

scene ep10_intro12 with dissolve
$ renpy.pause()
scene ep10_intro13 with dissolve
hl "Ahhh!"
play sound "sound_effects/glass.mp3"
scene ep10_intro14 with vpunch
hl "Oh!"
scene ep10_intro15 with dissolve
pa "Honey!? Do you need help?"
hl "No! It's fine!"
scene ep10_intro16 with dissolve
hl "*{i}Sobs{/i}*"
scene ep10_intro17 with dissolve
pa "Come here."
scene ep10_intro18 with dissolve
play sound "sound_effects/season3/monitor.mp3"
"*{i}Baby cries{/i}*"
scene ep10_intro19 with dissolve
hl "Darn it. I woke them up."
scene ep10_intro20 with dissolve
pa "I'll take care of this. Go hold our babies."
show ep10_intro21
if not persistent.ep10_cardzo1:
    show screen ep10_render_screen("zo1")
with dissolve
$ renpy.pause()

show ep10_intro22
hide screen ep10_render_screen
with dissolve
pa "Did they fall asleep?"

scene ep10_intro23 with dissolve
hl "Yes."
hl "They are so beautiful - our tiny miracles."
scene ep10_intro24 with dissolve
$ renpy.pause()
scene ep10_intro25 with dissolve
hl "What if...?"
hl "What if the day comes when I can't hold them anymore?"
hl "When they grow too heavy and I am too weak?"
scene ep10_intro26 with dissolve
pa "That's not going to happen."
scene ep10_intro25 with dissolve
hl "It could. What if I drop them like I dropped that plate?"
scene ep10_intro26 with dissolve
pa "If that happens, they'll be grown up and you won't have to worry about holding them by then."
scene ep10_intro25 with dissolve
hl "What if it happens sooner than that?"
hl "I don't recognize my body anymore. I've become a stranger to it."
scene ep10_intro26 with dissolve
pa "Then I'll hold them for you."
scene ep10_intro27 with dissolve
hl "..."
scene ep10_intro28 with dissolve
pa "Dinner is ready."
scene ep10_intro29 with dissolve
hl "Easy there, hungry."
scene ep10_intro30 with dissolve
pa "*{i}Mmpff{/i}* Right."
scene ep10_intro34 with dissolve
hl "Do you want to say it tonight?"
scene ep10_intro31 with dissolve
pa "No, I'm not good with the words."
scene ep10_intro35 with dissolve
hl "Our Heavenly Father."
hl "We thank you for our food and our drink. We are so thankful."
hl "In a world where many go hungry, we share this food with grateful hearts."
scene ep10_intro32 with dissolve
pa "You've always been wonderful with your words, Helen. I admire you for it."
scene ep10_intro36 with dissolve
hl "It's not hard saying a prayer, love. You just let your heart speak loudly to him."
hl "You should try it more."
scene ep10_intro32 with dissolve
pa "What do you pray for?"
scene ep10_intro36 with dissolve
hl "I pray for us."
hl "I pray for our well-being."
hl "I pray for our children and that they grow up to live long and happy lives."
scene ep10_intro33 with dissolve
hl "I pray to see them graduate and become adults."
scene ep10_intro37 with dissolve
hl "I pray that, one day..."
hl "I get to see their father walk them down the aisle."
hl "And I pray for beautiful grandkids and a long and healthy life together with you by my side."
scene ep10_intro32 with dissolve
pa "Those are indeed things worth praying for."
scene ep10_intro38 with dissolve
play sound "sound_effects/season3/monitor.mp3"
"*{i}Baby cries{/i}*"
pa "I've got it this time."
scene ep10_intro39 with dissolve
hl "No, please. Let me."
scene ep10_intro28 with dissolve
pa "Of course, sweetheart."

scene ep10_intro40 with Dissolve(4)
$ renpy.pause()
scene ep10_intro41 with dissolve
pa "Are you full?"
scene ep10_intro42 with dissolve
hl "No, I'm not full! My medication hasn't helped yet and I don't have an appetite this time of the day! You know that!"
hl "And I'm sweating too much! I'm overheating! I need to lie down!"
scene ep10_intro43 with dissolve
my "Derek! Stop it! DAAAD!!!"
my "Derek took my doll!!!"
scene ep10_intro44 with dissolve
pa "Derek! Be nice to your sister! You only get one!"
scene ep10_intro45 with dissolve
pa "I have to return to work, but I'll try coming home early."
pa "Call Susan if you need to, you know she won't mind and she's just next door."
scene ep10_intro46 with dissolve
hl "You don't have to remind me! Go to work! That's all you ever do."
hl "And it's a constant reminder of what I can't do."
hl "Work, work, work..."
scene ep10_intro47 with dissolve
pa "..."
scene ep10_intro48 with dissolve
pa "If you're looking for a reliable RV, this is it."
pa "I own a caravan of the same brand and it's been a blessing every summer with the wife and kids and all."
pa "Getting away from daily life and being one with nature..."
pa "This RV is even a step up. You'd be lucky to own it."
scene ep10_intro49 with dissolve
cs "It sure looks the part, but I'll have to look around more before I decide."
scene ep10_intro48 with dissolve
pa "Absolutely! If you need me for anything, I'll be in my office. Please don't hesitate."
scene ep10_intro50 with dissolve
$ renpy.pause()
scene ep10_intro51 with dissolve
$ renpy.pause()
scene ep10_intro52 with dissolve
pa "..."
scene ep10_intro53 with dissolve
pa "Father...? Uh..."
pa "I know we don't talk much and I haven't been the most devout Christian, but..."
pa "I don't know where else to turn."
pa "I've tried to learn from Helen, but forgive me if I say the wrong things."
scene ep10_intro54 with dissolve
pa "I want to ask you..."
pa "Why...?"
pa "Why are you doing this to me?"
scene ep10_intro55 with dissolve
pa "I work and I make a great living. I can provide for my family."
pa "And while I can give my wife a lot, I cannot give her health."
pa "I cannot give her a normal life. How I wish I could."
scene ep10_intro54 with dissolve
pa "I wish I had healing hands to restore her to what she used to be."
pa "I wish there were medication strong enough to take her pain away, even if it's just for one day."
pa "I'd even accept her pain, to feel what she feels."
scene ep10_intro53 with dissolve
pa "I wish for all of her dreams to come true."
pa "You already took away one of them; don't take away the rest."
pa "Please?"

scene ep10_intro56 with dissolve
cs "Excuse me."
pa "Yes?"
cs "I've made up my mind. I'll take it."
scene ep10_intro57 with dissolve
pa "That's...great! I'll get the paperwork ready."

scene ep10_intro62 with dissolve
pa "{i}I pray for you, Helen.{/i}"
pa "{i}I know who you are deep down inside. And I have learned to separate your sickness from the real you.{/i}"
scene ep10_intro63 with dissolve
pa "{i}I'll be there for you, through thick and thin.{/i}"
pa "{i}Just like I promised you in our vows, I promise this to you now...{/i}"
scene ep10_intro64 with dissolve
pa "{i}I'll do it all for you. Every wish I can fulfill will come true.{/i}"
pa "{i}I'll bounce our kids on my knees for you.{/i}"
scene ep10_intro65 with dissolve
pa "{i}I'll make sure that you'll live long enough to see our children grow old.{/i}"
scene ep10_intro58 with dissolve
pa "{i}To see them graduate.{/i}"
scene ep10_intro59 with dissolve
pa "{i}To see them walk down the aisle.{/i}"
scene ep10_intro60 with Dissolve(2)
pa "{i}To see them have children of their own.{/i}"
stop music fadeout 5
scene ep10_intro61 with dissolve
pa "{i}All of this...{/i}"
pa "{i}I promise you.{/i}"

scene 2d_jacob_screen_main with dissolve
play music "music/ep10/bonfire.mp3"
show screen episode_title_screen
$ renpy.pause(5)
$ renpy.block_rollback()

$ renpy.sound.play("sound_effects/season3/zoey_intro.mp3", channel="sfx1", loop=False)
scene bg anim_zoey_run_ep10 movie with dissolve
$ renpy.pause(26)
zo "Fuck! Shitballs! Fuck!"
stop music fadeout 6
$ renpy.music.stop(channel="sfx1", fadeout=6)
scene black with Fade(2,2,2)

$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep7/licensed_music/track57.mp3","music/ep8/licensed_music/track72.mp3","music/ep5/licensed_music/track6.mp3","music/ep2/wings.mp3"])
show screen new_phone_screen
if wt_ep9_branch_numbers < 2:
    if branchMayaJosy:
        scene ep10_intro_diks with fade
        $ renpy.pause()
        jump ep10_jm_intro_label
    elif branchIsabella:
        scene ep10_intro_diks with fade
        $ renpy.pause()
        jump ep10_isabella_intro_label
    elif branchSage:
        scene ep10_intro_diks with fade
        $ renpy.pause()
        jump ep10_sage_intro_label
    elif branchJill:
        scene ep10_intro_diks with fade
        $ renpy.pause()
        jump ep10_jill_intro_label
    else:
        if ep9_lily_nicole_lewd:
            jump ep10_ln_intro_label
        elif ep9_quinn_lewd:
            jump ep10_smq_intro_label
        elif ep9_sarah_melanie_lewd:
            jump ep10_smq_intro_label
        else:
            jump ep10_others_intro_label
else:
    
       
       if wt_ep9_end_pick=="Jill":
            scene ep10_intro_diks with fade
            $ renpy.pause()
            jump ep10_jill_intro_label
               
       if wt_ep9_end_pick=="Sage":
            scene ep10_intro_diks with fade
            $ renpy.pause()
            jump ep10_sage_intro_label
       
       if wt_ep9_end_pick=="Maya":
            scene ep10_intro_diks with fade
            $ renpy.pause()
            jump ep10_jm_intro_label
       
       if wt_ep9_end_pick=="Bella":
            scene ep10_intro_diks with fade
            $ renpy.pause()
            jump ep10_isabella_intro_label
       
       if wt_ep9_end_pick=="Other":
            jump ep10_others_intro_label
       if wt_ep9_end_pick=="Quinn":
            jump ep10_smq_intro_label
       if wt_ep9_end_pick=="Sarah":
            jump ep10_smq_intro_label
       if wt_ep9_end_pick=="Lily":
            jump ep10_ln_intro_label

label ep10_dik_intro_label:
show screen new_phone_screen
if ep9_sarah_melanie_lewd or ep9_quinn_lewd or ep9_lily_nicole_lewd:
    scene ep10_dik_intro1c with wipeleft
else:
    scene ep10_dik_intro1b with wipeleft
jac "Tell me there's hot coffee in that pot..."
if ep9_sarah_melanie_lewd or ep9_quinn_lewd or ep9_lily_nicole_lewd:
    scene ep10_dik_intro2c with dissolve
else:
    scene ep10_dik_intro2b with dissolve
mc "Yeah, help yourself. I'm on cup three already."
scene ep10_dik_intro3b with dissolve
jac "That sounds like a nasty hangover."
scene ep10_dik_intro4b with dissolve
mc "It's not bad. I'm mostly feeling tired. That party drained me."
scene ep10_dik_intro3b with dissolve
if branchMayaJosy:
    jac "I bet that something did drain you, you lucky dog."
else:
    jac "Same. I had one too many shots. Derek knows how to make them."
    jac "I woke up at 8 a.m. and had to hurl."
scene ep10_dik_intro5b with dissolve
de "[mc_de_up]?"
if branchMayaJosy:
    scene ep10_dik_intro6b with dissolve
    mc "Coffee?"
    scene ep10_dik_intro5b with dissolve
    de "Nah, I'm good."
else:
    scene ep10_dik_intro6b with dissolve
    mc "Hey, he lives."
scene ep10_dik_intro7b with dissolve
jac "Hungover, yet? Or are you still buzzing?"
scene ep10_dik_intro8b with dissolve
de "I don't get hangovers."
scene ep10_dik_intro7b with dissolve
jac "Man, fuck you. You're lucky."
scene ep10_dik_intro5b with dissolve
de "[mc_de_up]? A word?"
scene ep10_dik_intro6b with dissolve
mc "Sure."

label ep10_dik2_intro_label:
scene ep10_dik2_intro1 with dissolve
if branchMayaJosy:
    mc "If it's about earlier... Let me just say that I'm sorry it came out that way."
else:
    mc "What's up?"
scene ep10_dik2_intro2 with dissolve
play sound "sound_effects/shower_curtain.mp3"
if branchMayaJosy:
    de "It's not about that."
    mc "Ok..."
mc "Why are you closing the drapes?"
scene ep10_dik2_intro3 with dissolve
mc "Sunlight's that bad, huh? You don't have to pretend you don't get hangovers if you do."
mc "I wouldn't think less of you if you did."
scene ep10_dik2_intro4 with dissolve
de "Help me check the ceiling for any flashing lights."
scene ep10_dik2_intro5 with dissolve
mc "Are you feeling ok?"
scene ep10_dik2_intro4 with dissolve
de "I'm feeling a bit sick, but I'm fine."
$ guideSuggestedPage = 94
show ep10_dik2_intro6
if not persistent.ep10_cardzo2:
    show screen ep10_render_screen("zo2")
with dissolve
mc "That does sound like a hangover to me."
show ep10_dik2_intro7 with dissolve
de "It's not that. Can you find anything?"
hide ep10_dik2_intro7 with dissolve
mc "No, everything is dark. Can we let some sunlight in or...?"
scene ep10_dik2_intro8
hide screen ep10_render_screen
with dissolve
de "This room seems clean."
scene ep10_dik2_intro9 with dissolve
mc "Clean from what?"
scene ep10_dik2_intro8 with dissolve
de "Listen, this has to stay between you and me."
de "You're the only one I can trust."
scene ep10_dik2_intro9 with dissolve
mc "What's the matter? Why are you so secretive?"
scene ep10_dik2_intro8 with dissolve
de "I found something in my room today."
de "When I woke up, I saw this faint red flashing light in one of my ceiling spotlights."
scene ep10_dik2_intro10 with dissolve
de "I found this inside of it."
mc "What is that?"
de "What does it look like? It's some kind of a security camera, no?"
scene ep10_dik2_intro11 with dissolve
mc "Why would there be a security camera in your closet?"
scene ep10_dik2_intro12 with dissolve
de "That's what I'm trying to figure out."
scene ep10_dik2_intro11 with dissolve
mc "Did someone put it there last night?"
scene ep10_dik2_intro12 with dissolve
de "Nah, no way."
scene ep10_dik2_intro11 with dissolve
mc "But if it was flashing, you would have spotted it earlier."
scene ep10_dik2_intro13 with dissolve
de "Yeah. Unless something happened to it during that blackout. What if it's been there all this time?"
de "What if someone has spied on me in that room?"
scene ep10_dik2_intro11 with dissolve
mc "Why would someone spy on you?"
scene ep10_dik2_intro13 with dissolve
de "I have no clue, but you're the only one I can trust with this. Because I know you'd never do that to me."
scene ep10_dik2_intro11 with dissolve
mc "Wait... Are you suggesting that a DIK put it there?"
scene ep10_dik2_intro12 with dissolve
de "It sure as hell wasn't installed at a party."
scene ep10_dik2_intro11 with dissolve
mc "How can you be sure?"
scene ep10_dik2_intro10 with dissolve
de "Look at the cable... I had to rip it out. It's not a simple plug-in camera... This one requires some proper installation."
de "Who else would have the time and opportunity to install it besides someone living here?"
de "Didn't we change the lights after the alphas trashed the mansion?"
scene ep10_dik2_intro11 with dissolve
mc "Yeah, I remember we replaced some broken ones. Were there any broken lights in your room?"
scene ep10_dik2_intro13 with dissolve
de "I don't remember. Every room was a mess back then. Who replaced the lights?"
scene ep10_dik2_intro11 with dissolve
mc "I can't remember. We could ask Rusty if he does."
scene ep10_dik2_intro13 with dissolve
de "We could, but it's his laptop, right? What if it has a direct feed to the camera?"
scene ep10_dik2_intro11 with dissolve
mc "Are you saying we can't even trust Rusty? I thought you two were close."
scene ep10_dik2_intro13 with dissolve
de "We are close and I'm not saying that... But like I said, I can only trust you right now."
de "I've done some nasty stuff in that closet, and if someone has recordings of me..."
de "Not only would that be it for my reputation, but it could also hurt Ashley."
de "I want to understand this better before I start confronting people about it."
scene ep10_dik2_intro11 with dissolve
mc "Ok. I'm with you."
scene ep10_dik2_intro12 with dissolve
de "I will check if I can find more flashing red lights in the mansion. If you get the chance to check some rooms, do it."
scene ep10_dik2_intro11 with dissolve
mc "I'll be discreet and check what I can."
scene ep10_dik2_intro12 with dissolve
de "Flip the light to the room and look for anything that flashes."
de "[mc_de_up]... Thanks."
scene ep10_dik2_intro11 with dissolve
mc "Any time, bro."
stop music fadeout 3
scene ep10_dik2_intro14 with dissolve
mc "(It sounds crazy that someone would put a hidden camera in his closet... Who would do that?)"
$ new_bio("Derek", "Derek found a security camera in one of the ceiling spotlights in his room. He confided in me about it but didn't want anyone else to know until he could investigate it more.")
jump ep10_freeroam_diks

label ep10_ip_label:
scene ep10_ip1 with fade
play music "music/ep5/rustic_ballad.mp3"
$ renpy.pause()
scene ep10_ip2 with dissolve
isa "Professor Hoff, can I borrow a moment of your time?"
scene ep10_ip3 with dissolve
ph "Certainly, Mrs. Roberts. What can I do for you?"
scene ep10_ip4 with dissolve
isa "It's about the midterms for our freshman classes."
scene ep10_ip7 with dissolve
ph "Yes, of course. What about them?"
scene ep10_ip4 with dissolve
isa "I wanted to ask if you have noticed anything unusual when correcting the tests."
scene ep10_ip7 with dissolve
ph "Anything unusual? No, I can't say that I have. There was a healthy mix of pass and fail."
ph "There were a couple of students who were nowhere near close to passing. And on the other side of the spectrum, a handful of students excelled."
scene ep10_ip5 with dissolve
isa "About the students who excelled... Did all of their test answers seem coherent to you?"
scene ep10_ip7 with dissolve
ph "Meaning?"
scene ep10_ip5 with dissolve
isa "Did their conclusions seem logical for all answers?"
scene ep10_ip7 with dissolve
ph "Um, yes? Honestly, I'm unsure what you're asking me right now."
scene ep10_ip6 with dissolve
if ep8_midterms_cheated != "DIK":
    isa "Let me explain. When I corrected my tests, I came across one that had odd answers."
    isa "Seeing that several answers had discrepancies, while others were spot on made me analyze the test in detail."
    isa "I suspect that this student may have cheated on the test somehow."
else:
    isa "Let me explain. When I corrected my tests, I came across a couple of tests that had odd answers and shared the same reasoning for multiple answers."
    isa "Seeing that several answers had discrepancies, while others were spot on made me analyze the tests in detail."
    isa "I suspect that these students may have cheated on the test somehow."
scene ep10_ip8 with dissolve
if ep8_midterms_cheated != "DIK":
    ph "And you want to inquire if the same student shows signs of cheating on my test."
else:
    ph "And you want to inquire if the same students show signs of cheating on my test."
scene ep10_ip6 with dissolve
isa "Exactly."
scene ep10_ip7 with dissolve
ph "This is tough, Mrs. Roberts. While I don't condone cheating, students are entitled to anonymity and privacy regarding the test results."
scene ep10_ip5 with dissolve
if ep8_midterms_cheated != "DIK":
    isa "I'm not asking you to divulge the test results to me. I'm asking you to take a closer look at one of your tests and see if you can find something."
else:
    isa "I'm not asking you to divulge the test results to me. I'm asking you to take a closer look at two of your tests and see if you can find something."
scene ep10_ip7 with dissolve
if ep8_midterms_cheated != "DIK":
    ph "Do you have the student ID?"
else:
    ph "Do you have their student IDs?"
scene ep10_ip9 with dissolve
isa "Thank you."

label ep10_perks_update_label:
if branchJill:
    scene ep10_perks_updatej4 with wipeleft
    ji "It wouldn't have been a problem to help out with the cleaning."
    scene ep10_perks_updatej6 with dissolve
    mc "I know, but it was our party. I didn't want to make you do chores; I only wanted you to have fun."
    scene ep10_perks_updatej5 with dissolve
    ji "Next time, I will stay and help regardless."
    scene ep10_perks_updatej6 with dissolve
    mc "Oh, there will be a next time?"
    scene ep10_perks_updatej5 with dissolve
    ji "Won't there?"
    scene ep10_perks_updatej6 with dissolve
    mc "There will be many parties, but from what I hear, I'm not sure if you'd be interested in them."
    scene ep10_perks_updatej8 with dissolve
    ji "Halloween was very fun. I'm starting to think that you think I can't handle your kind of parties."
    scene ep10_perks_updatej7 with dissolve
    mc "There are things the guys want to do that I'm sure you would mind."
    scene ep10_perks_updatej8 with dissolve
    ji "Try me!"
    scene ep10_perks_updatej7 with dissolve
    mc "Tommy's been talking about some kind of a panty party, where I believe everyone's dressed in underwear."
    mc "Would you be able to handle that?"
    scene ep10_perks_updatej9 with dissolve
    ji "Ok, now I think that you know me better than I thought."
    scene ep10_perks_updatej6 with dissolve
    mc "Haha! See? I'm only looking out for you."
    scene ep10_perks_updatej5 with dissolve
    ji "I like that you are, but please don't feel like you have to protect me from what you guys are up to."
    scene ep10_perks_updatej6 with dissolve
    mc "I promise I won't make choices for you and to ask if you're interested, even if I can probably guess the answer. How does that sound?"
    scene ep10_perks_updatej10 with dissolve
    ji "*{i}Smack{/i}*"

    if ep9_josy_choice == "CHICK":
        scene ep10_perks_update1 with dissolve
    else:
        scene ep10_perks_update1b with dissolve
else:
    if ep9_josy_choice == "CHICK":
        scene ep10_perks_update1 with wipeleft
    else:
        scene ep10_perks_update1b with wipeleft
mg "Good morning, fellow students! Great day, isn't it?"
if branchMayaJosy:
    scene ep10_perks_update2a with dissolve
elif ep10_rolling:
    scene ep10_perks_update2b with dissolve
elif branchJill:
    scene ep10_perks_updatej2 with dissolve
else:
    scene ep10_perks_update2 with dissolve
mg "Well, if it isn't [name]!"
if branchMayaJosy:
    scene ep10_perks_update3a with dissolve
elif ep10_rolling:
    scene ep10_perks_update3b with dissolve
elif branchJill:
    scene ep10_perks_updatej3 with dissolve
else:
    scene ep10_perks_update3 with dissolve
mc "Magnar. You seem happy."
if branchJill:
    scene ep10_perks_updatej3b with dissolve
    ji "Hi, Magnar!"
    scene ep10_perks_updatej3c with dissolve
    mg "And Jill, how do you do?"
    scene ep10_perks_updatej3b with dissolve
    ji "Fine, thanks. And about to be late for class. Take care!"
    scene ep10_perks_update8 with dissolve
    mc "How are things?"
scene ep10_perks_update4 with dissolve
mg "I am in an excellent mood today. Thanks for noticing."
mg "Midterms are over and it's time for a batch of brand-new classes and tests to pass."
if branchMayaJosy:
    scene ep10_perks_update4a with dissolve
elif ep10_rolling:
    scene ep10_perks_update4b with dissolve
else:
    scene ep10_perks_update8 with dissolve
mc "I can't say I'm as happy about that, but it's nice that the midterms are over."
scene ep10_perks_update5 with dissolve
mg "Any new courses on your end?"
if branchMayaJosy:
    scene ep10_perks_update4a with dissolve
elif ep10_rolling:
    scene ep10_perks_update4b with dissolve
else:
    scene ep10_perks_update8 with dissolve
mc "I have an Intro to Science class. Other than that, I'm still taking English and math."
scene ep10_perks_update5 with dissolve
mg "Oh! That's the Applied Chemistry class. It's a fun one!"
mg "Perhaps you'd be interested in some of our knowledge? Old exams, notes, and such."
if branchMayaJosy:
    scene ep10_perks_update4a with dissolve
elif ep10_rolling:
    scene ep10_perks_update4b with dissolve
else:
    scene ep10_perks_update8 with dissolve
mc "Yeah, possibly."
if nerdNotes:
    mc "And I can send more of my notes your way if you wish."
    scene ep10_perks_update5 with dissolve
    mg "While I'm thankful for your efforts in providing us with notes from your earlier classes, we won't need them in the future."
    scene ep10_perks_update6 with dissolve
    mc "Weren't they good?"
    scene ep10_perks_update7 with dissolve
    mg "Eh... We won't be needing them."
    $ specialMessage = "{size=-%d}Your Nerd Notes perk lost its effect{/size}" % (5 * persistent.scale_factor)
    scene ep10_perks_update6 with dissolve
    show screen specialmsg
    $ renpy.pause(2)
    hide screen specialmsg
scene ep10_perks_update5 with dissolve
mg "Do let me know if you need something."
if minigames:
    $ englishBoost = englishBoost/5
    $ mathBoost = mathBoost/5
    scene ep10_perks_update6 with dissolve
    show screen newmoneymsg
    call screen shop_magnar_screen
    $ renpy.pause(0.5)
    hide screen newmoneymsg
    scene ep10_perks_update5 with dissolve
mg "I'll be seeing you! Have a great day, [name]."
if branchMayaJosy:
    scene ep10_perks_update9a with dissolve
    de "Sup, [mc_de]. What was that about?"
elif ep10_rolling:
    scene ep10_perks_update9b with dissolve
    de "Sup, [mc_de]."
    scene ep10_perks_update9c with dissolve
    de "Lily."
    scene ep10_perks_update9d with dissolve
    ly "Hey."
    scene ep10_perks_update9e with dissolve
    de "What was that about?"
else:
    scene ep10_perks_update9 with dissolve
    de "Sup, [mc_de]. What was that about?"
scene ep10_perks_update10 with dissolve
mc "Magnar offered me to buy some of their old notes and whatnot."
scene ep10_perks_update12 with dissolve
de "You don't need those. You know who to come to if you need help passing the tests, right?"
scene ep10_perks_update11 with dissolve
if minigames:
    show screen newmoneymsg
    call screen shop_derek_screen
    $ renpy.pause(0.5)
    hide screen newmoneymsg
mc "Yeah, I know who I'd ask if I wanna cheat, for sure."
scene ep10_perks_update12 with dissolve
de "Don't insult me. As I told you, it's a tool for learning."
scene ep10_perks_update11 with dissolve
mc "If that makes you feel better about it, sure."
if ep8_midterms_cheated == "DIK" and not ep10_rolling:
    scene ep10_perks_update12 with dissolve
    de "*{i}Whispers{/i}* Well, was it you or me who cheated on the midterms?"
    scene ep10_perks_update11 with dissolve
    mc "Hey... Keep it down."
    scene ep10_perks_update12 with dissolve
    de "I was. And I'm just saying."
if branchMayaJosy:
    scene ep10_perks_update13b with dissolve
elif ep10_rolling:
    scene ep10_perks_update13a with dissolve
else:
    scene ep10_perks_update13 with dissolve
mc "So... What's up with the shirt? I didn't know you liked anime."
de "Pff... I'm not a weeb, [mc_de]. I'm in it for the hentai."
jump ep10_english_label

label ep10_english_label:
$ guideSuggestedPage = 102
if ep10_rolling:
    scene ep10_english1 with fade
else:
    scene ep10_english1b with fade
$ renpy.pause()
if ep10_rolling:
    scene ep10_english2 with dissolve
    ly "Hey, saved you a seat."
    scene ep10_english6 with dissolve
    de "[mc_de_up]?"
    scene ep10_english3 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Derek)","(-Derek)","(-DIK)","(+DIK)","(Lily path)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Go with Lily \n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]":
            $ ep10_lily_english = True
            $ RPderek -= 1
            scene ep10_english5 with dissolve
            mc "Sorry, bro. I gotta go with Lily for this one."
            scene ep10_english8 with dissolve
            ly "Give me your jacket."
            scene ep10_english9 with dissolve
            mc "Are you cold?"
            scene ep10_english10 with dissolve
            ly "It's all about being noticed by others now, [name]."
            scene ep10_english11 with dissolve
            mc "I see. Give me your bra, then."
            scene ep10_english10 with dissolve
            ly "Not in that way."
            $ new_bio("Lily", "I chose to sit with Lily instead of Derek during English class.")
        "Stay with Derek [m_c1][mod_choices[0]]":
            $ ep10_lily_english = False
            $ RPderek += 1
            mc "Sorry, Lily. I can't leave my bro for this."
            scene ep10_english4 with dissolve
            ly "Oh, really? Uh-huh."
            scene ep10_english7 with dissolve
            de "Such a bro."
            $ new_bio("Derek", "I chose to sit with Derek instead of Lily during English class.")
            jump ep10_derek_english_label

if ep10_lily_english:
    scene ep10_english12 with dissolve
else:
    scene ep10_english12b with dissolve
isa "Good morning, class. Welcome back! I hope you enjoyed your time off after the midterms and feel energized and invigorated to continue your studies."
scene ep10_english13 with dissolve
isa "Now, let's power through until Christmas and the finals. Believe me, time will fly by even faster than it did since the start of the semester."
isa "Make sure you study hard, especially if you didn't do well on your midterm exam."
scene ep10_english14 with dissolve
ash "How do we know if we did? Are we getting the results soon?"
scene ep10_english15 with dissolve
isa "The results will be published later this week. I need a few extra days to correct the tests due to unforeseen circumstances."
scene ep10_english16 with dissolve
isa "In the first half of the class, you've been focusing a lot on the writing aspect, in how to write essays for college and communicate in writing."
isa "For the second half of the class, you will focus more on communication in discussions of texts."
isa "You can, of course, expect written tests."

scene ep10_english13 with dissolve
isa "We're being nice with the finals of this class and will have them before Christmas."
isa "That way, you don't have to spend your Christmas break studying and can spend it with your family or however you choose."
isa "That is, unless you have other courses to study for."
if ep8_maya_lewd:
    scene ep10_english17 with dissolve
    isa "Make a note of this date..."
    scene ep10_english18 with dissolve
    isa "Uh..."
    de "Who's Dr. Dick?"
    scene ep10_english21 with dissolve
    $ renpy.pause()
    scene ep10_english22 with dissolve
    my "..."
    if branchMayaJosy:
        scene ep10_english23 with dissolve
        js "Is that...?"
        my "Shh!"
    scene ep10_english19 with dissolve
    isa "Apparently, it's a doctor who doesn't know that permanent markers aren't meant for blackboards."
    isa "You know what? The finals date is in your syllabus."
    scene ep10_english20 with dissolve
    isa "(Dear God, what happened in here?)"

scene ep10_english16 with dissolve
isa "Now, please start discussing today's text with your partner."

if branchIsabella:
    scene ep10_english24 with dissolve
    mc "Hey, what was that about the unforeseen circumstances?"
    scene ep10_english25 with dissolve
    isa "It's something I have to investigate further."
    scene ep10_english24 with dissolve
    mc "You can just say you didn't finish your job. I don't think anyone will blame you."
    scene ep10_english26 with dissolve
    isa "Ok, funny guy. Back to your studies."

if ep10_lily_english:
    jump ep10_derek_english2_label
if not branchIsabella and not ep9_jm_sad and not branchMayaJosy:
    jump ep10_derek_english3_label

label ep10_derek_english_label:
scene ep10_english27 with dissolve
mc "I guess we should get started."
scene ep10_english28 with dissolve
de "Yeah... Ok. You go ahead and do that."
if branchIsabella:
    scene ep10_english29 with dissolve
    isa "*{i}Cough{/i}*"
    scene ep10_english30 with dissolve
    de "..."
    scene ep10_english29 with dissolve
    isa "*{i}Cough{/i}*"
    scene ep10_english31 with dissolve
    de "Flu season, eh?"
    scene ep10_english33 with dissolve
    isa "Give me your phone."
    scene ep10_english31 with dissolve
    de "Uh... My phone is in my pocket."
    scene ep10_english33 with dissolve
    isa "Well, give me that one, too, and the one in your book."
    scene ep10_english32 with dissolve
    de "..."
    scene ep10_english34 with dissolve
    isa "You can have it back after class. Do you have one in your pocket, or is this the only one?"
    scene ep10_english36 with dissolve
    de "..."
    scene ep10_english35 with dissolve
    isa "I thought as much. Now, read your book. You figured out how to open it, so you're halfway there."
else:
    scene ep10_english27 with dissolve
    mc "All right."
label ep10_derek_english2_label:
if ep9_jm_sad:
    scene ep10_english44 with dissolve
    $ renpy.pause()
    scene ep10_english47 with dissolve
    js "I can't focus today."
    scene ep10_english48 with dissolve
    my "Me neither..."
    scene ep10_english49 with dissolve
    js "Everything feels...different."
    scene ep10_english48 with dissolve
    my "Looking at him all the time won't help."
    scene ep10_english50 with dissolve
    js "..."
    scene ep10_english51 with dissolve
    js "I snapped at him yesterday... I can't forgive him for what he did."
    scene ep10_english50 with dissolve
    my "What did you say?"
    scene ep10_english51 with dissolve
    js "I told him I didn't want to be friends with him anymore."
    scene ep10_english50 with dissolve
    my "You said that?"
    scene ep10_english51 with dissolve
    js "Something to that effect."
    scene ep10_english50 with dissolve
    my "Do you mean it?"
    scene ep10_english52 with dissolve
    js "Yes. I mean, how could I?"
    js "Even though we weren't a real couple, it still felt like we were in a real relationship with each other."
    js "And now, I feel like I'm his ex-girlfriend, but I never got to show him the real me in a relationship."
    scene ep10_english50 with dissolve
    my "I knew you liked him but didn't realize you liked him this much."
    scene ep10_english52 with dissolve
    js "I... *{i}Sigh{/i}*"
    if branchSage or branchJill:
        scene ep10_english50 with dissolve
        if branchSage:
            my "And what about...Sage?"
        else:
            my "And what about Jill?"
        scene ep10_english52 with dissolve
        js "I don't know... I mean... *{i}Sigh{/i}*"
    scene ep10_english53 with dissolve
    my "It's ok. I struggle to put words for my feelings, too."
    scene ep10_english55 with dissolve
    my "But what you said, that you don't want to be his friend..."
    my "I don't feel the same."
    scene ep10_english53 with dissolve
    my "Despite what happened between us, I feel he's one of the few people I can trust."
    my "And I could tell it hurt him a lot doing what he had to do when he broke up with us."
    scene ep10_english54 with dissolve
    my "We can't control him or his feelings. He's allowed to make his own choices, and he did."
    my "Even if it hurts, I still wanna be around him. And I hope you can find a way to do it, too."
    scene ep10_english55 with dissolve
    js "..."
elif branchMayaJosy:
    scene ep10_english45 with dissolve
    $ renpy.pause()
    scene ep10_english46 with dissolve
    js "I can't focus today."
    scene ep10_english47b with dissolve
    my "Me neither."
    scene ep10_english47c with dissolve
    js "Everything feels...different. But in a good way."
    scene ep10_english47b with dissolve
    my "I'm not quite there yet."
    scene ep10_english56 with dissolve
    js "Yeah, about that... I know it's an odd feeling, but I think it's the way to go."
    js "At least for now."
    scene ep10_english61 with dissolve
    my "Do we have to act differently around each other now?"
    scene ep10_english56 with dissolve
    js "Like how?"
    scene ep10_english61 with dissolve
    my "Doesn't it appear weird for us always to sit next to each other? Can we hang out constantly without people asking more questions?"
    scene ep10_english56 with dissolve
    js "Don't make a big deal out of it. That's what I think."
    js "If you ignore what people say, those problems tend to go away."
    scene ep10_english61 with dissolve
    my "It's scary, though."
    scene ep10_english57 with dissolve
    js "Scary but also exciting."
    js "Do you realize you can kiss him publicly without worrying that someone will see it?"
    scene ep10_english59 with dissolve
    my "Yeah. Haha..."
    scene ep10_english57 with dissolve
    js "I think you should do it."
    scene ep10_english60 with dissolve
    my "Here!?"
    scene ep10_english57 with dissolve
    js "Haha! No, not here. That would be socially awkward."
    scene ep10_english59 with dissolve
    my "Haha, could you imagine? Walking up to him, tapping him on the shoulder and kissing him."
    scene ep10_english58 with dissolve
    js "I dare you to."
    scene ep10_english59 with dissolve
    my "No, we are done with that game. Look how it ended last time."
    my "We almost showed our tits to strangers."
    scene ep10_english58 with dissolve
    js "I still dare you to do it. Are you gonna?"
    scene ep10_english60 with dissolve
    my "Pschh... Haha!"
    my "No. Not in class. No way."
    scene ep10_english58 with dissolve
    js "Ok."
    scene ep10_english59 with dissolve
    my "Who even does that?"
    scene ep10_english58 with dissolve
    js "I'm not talking about making out with him. A kiss on the lips is what I'm asking for."
    scene ep10_english59 with dissolve
    my "You said it was socially awkward."
    scene ep10_english57 with dissolve
    js "Because I was picturing the way how I'd do it."
    scene ep10_english62 with dissolve
    my "Aha!"
    scene ep10_english63 with dissolve
    js "No way..."
    scene ep10_english64 with dissolve
    $ renpy.pause()
    scene ep10_english65 with dissolve
    my "*{i}Smack{/i}*"
    scene ep10_english66 with dissolve
    mc "Hi..."
    my "Hi."
    scene ep10_english67 with dissolve
    mc "Don't look at me that way. Take it up with your sister."

if branchIsabella:
    scene ep10_english37 with dissolve
    $ renpy.pause()
    scene ep10_english38 with dissolve
    de "*{i}Whispers{/i}* [mc_de_up]? She's staring at me. What does she want?"
    scene ep10_english39 with dissolve
    mc "I think she wants you to study and not wait for an opportunity to slack off."
    scene ep10_english38 with dissolve
    de "*{i}Whispers{/i}* Did you tell her something about me? I feel like she's onto me."
    scene ep10_english39 with dissolve
    mc "Nope. She must have ESP."
    if minigames:
        stop music fadeout 3
    scene ep10_english38 with dissolve
    de "*{i}Whispers{/i}* This is freaking me out... Can we start discussing this?"
if ep10_lily_english:
    scene ep10_english68 with dissolve
    mc "..."
    scene ep10_english69 with dissolve
    $ renpy.pause()
    scene ep10_english70 with dissolve
    ly "..."
    scene ep10_english71 with dissolve
    ly "No romantic stuff, ok?"
    scene ep10_english69 with dissolve
    mc "This isn't romantic. It's kinda dirty."
    ly "All right, I'll give you that."
    mc "Your legs are irresistible in those pants."
    scene ep10_english71 with dissolve
    ly "So, you're horny all the time?"
    scene ep10_english70 with dissolve
    mc "*{i}Sigh{/i}* Yes."
    if minigames:
        stop music fadeout 3
    scene ep10_english71 with dissolve
    ly "I'll let you keep your hand there if we hurry up and discuss this text. I want to get out of class early today."
else:
    label ep10_derek_english3_label:
    scene ep10_english40 with dissolve
    de "Gah! This book sucks."
    scene ep10_english41 with dissolve
    mc "What section of it?"
    scene ep10_english40 with dissolve
    de "Not the text, the book. It's too heavy. It makes it harder to hold my phone."
    scene ep10_english42 with dissolve
    mc "Put it away for a while. I wanna discuss the text and answer these questions with you."
    mc "Even though I fear it will be a one-sided discussion."
    if minigames:
        stop music fadeout 3
    scene ep10_english43 with dissolve
    de "Lay it on me, [mc_de]."
$ guideSuggestedPage = 103
if minigames:
    play music "music/ep3/sing_along_with_jim.mp3"
    $ qM = quick_menu
    $ quick_menu = 0
    hide screen new_phone_screen
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    jump init_eng_test_ep10_label

label after_eng_test_ep10_label:
hide screen word_cheat
if minigames:
    $ _game_menu_screen = "save"
    $ renpy.block_rollback()
    show screen new_phone_screen
    $ quick_menu = qM
    play music "music/ep5/rustic_ballad.mp3"
hide screen word_cheat
if ep10_lily_english:
    scene ep10_after_eng_test1b with dissolve
else:
    scene ep10_after_eng_test1 with dissolve
isa "How is it going?"
scene ep10_after_eng_test6 with dissolve
hide screen word_cheat
if ep9_jm_sad:
    js "Ok, I guess."
else:
    js "It's going well."
if ep10_lily_english:
    scene ep10_after_eng_test1b with dissolve
else:
    scene ep10_after_eng_test1 with dissolve
hide screen word_cheat
isa "Any questions so far?"
scene ep10_after_eng_test7 with dissolve
my "Yeah. But wait..."
my "Shouldn't you get a cup in case you need to drink when we ask them?"
scene ep10_after_eng_test3 with dissolve
isa "..."
scene ep10_after_eng_test2 with dissolve
isa "Will this be a recurring joke? Or will I be able to do my job without getting teased?"
scene ep10_after_eng_test6 with dissolve
js "We had a lot of fun with you this weekend."
scene ep10_after_eng_test8 with dissolve
my "So much fun. And we won't tease you in class for it."
scene ep10_after_eng_test2 with dissolve
isa "I had fun, too."
scene ep10_after_eng_test6 with dissolve
js "We should do it again sometime."
if ep10_lily_english:
    scene ep10_after_eng_test5b with dissolve
else:
    scene ep10_after_eng_test5 with dissolve
isa "I regret to inform you that I won't attend any more of your parties."
isa "Halloween provided a native excuse for it, with the costumes and all."
isa "But I'm sure that most students would normally mind my presence at a college party."
scene ep10_after_eng_test6 with dissolve
js "It doesn't have to be at a college party. Jill mentioned you two party together."
if ep10_lily_english:
    scene ep10_after_eng_test5b with dissolve
else:
    scene ep10_after_eng_test5 with dissolve
isa "Oh, yes. Jill and I are known for our wild parties where booze flows into the wee hours of the morning."
scene ep10_after_eng_test8 with dissolve
my "I knew it."
scene ep10_after_eng_test4 with dissolve
isa "It was sarcasm."
stop music fadeout 3
scene ep10_after_eng_test9 with dissolve
my "Oh?"

label ep10_after_english_label:
play music "music/ep9/licensed_music/track118.mp3"
if ep10_lily_english:
    $ mgallery_add_photo("ep10_lily_english_pic")
    scene ep10_after_english1 with wipeleft
    ly "Thanks for sitting with me in class. It didn't go by unnoticed."
    scene ep10_after_english3 with dissolve
    ly "*{i}Smack{/i}*"
    mc "Hey... No romance."
    scene ep10_after_english2 with dissolve
    ly "Oof. Shoot! I guess I owe you one."
    scene ep10_after_english4 with dissolve
    de "Don't ever do that to me again."
    mc "Huh?"
    scene ep10_after_english5 with dissolve
    de "I had to discuss the text with Isabella."
    scene ep10_after_english6 with dissolve
    mc "How did that go?"
    scene ep10_after_english5 with dissolve
    de "She made me read it! Can you believe it?"
    scene ep10_after_english6 with dissolve
    mc "A teacher doing their job? I'm shocked."

scene ep10_after_english7 with dissolve
de "Gah! Fuck this class with a fat wooden log."
scene ep10_after_english9 with dissolve
mc "We're more than halfway through with it now. That's something."
scene ep10_after_english8 with dissolve
de "I miss Cathy."
scene ep10_after_english9 with dissolve
mc "I think Bella is doing a great job."
scene ep10_after_english8 with dissolve
de "She is doing a great job! At fucking things up."
de "It's like she cares about her students learning. That's the worst kind of teacher there is!"
de "In high school, they just told me I was impossible to teach and left me alone. I would have cherished it more if I had known it was bliss."

if ep9_jm_sad:
    scene ep10_after_english10 with dissolve
    mc "Hi, Josy."
    scene ep10_after_english11 with dissolve
    my "Hey, [name]."
    mc "*{i}Sigh{/i}* Hi, Maya."
    my "You need to give her time."
    scene ep10_after_english12 with dissolve
    mc "I'm trying. But I don't wanna ignore her."
    scene ep10_after_english13 with dissolve
    my "Do you guys have time to meet up later?"
    scene ep10_after_english12 with dissolve
    mc "Yeah, I've got time today. For what?"
    scene ep10_after_english13 with dissolve
    my "Josy asked Jill for legal help, and we wanted to fill her in on the situation."
    my "I think it would feel best if everyone involved were there so we can discuss it."
    scene ep10_after_english12 with dissolve
    mc "Sure. I'm there for you. When and where?"
    scene ep10_after_english13 with dissolve
    my "I'll let you know after I've talked to Sage. Ok?"
else:
    if branchMayaJosy:
        scene ep10_after_english14 with dissolve
        mc "Hi, girls."
        scene ep10_after_english15 with dissolve
        mc "Maya, what was that in class?"
        scene ep10_after_english18 with dissolve
        de "Yeah! What the hell was that!?"
        scene ep10_after_english16 with dissolve
        js "I dared her to do it."
        scene ep10_after_english15 with dissolve
        mc "Are you two still playing?"
        scene ep10_after_english18 with dissolve
        de "Playing what?"
        scene ep10_after_english17 with dissolve
        my "This doesn't concern you."
        scene ep10_after_english18 with dissolve
        de "The fourth wheel, I tell you. Always the fourth wheel."
        scene ep10_after_english15 with dissolve
        mc "Ok... Let's include Derek in the chat and talk about this later."
        scene ep10_after_english16 with dissolve
        js "I'm in a rush anyway. Off to my next class! See you guys!"
    else:
        scene ep10_after_english14 with dissolve
        mc "Hi, girls."
        scene ep10_after_english16 with dissolve
        js "Classes again, huh? Who else missed it?"
        scene ep10_after_english18 with dissolve
        de "Not me, that's for sure."
        scene ep10_after_english16 with dissolve
        js "Well, I sure did. And I'm in a rush to my next one. See you guys!"
    scene ep10_after_english19 with dissolve
    my "Don't forget to talk to Jill."
    js "I won't!"
    scene ep10_after_english20 with dissolve
    mc "Talk to Jill about what?"
    scene ep10_after_english21 with dissolve
    my "Josy has asked Jill for legal help, and we wanted to fill her in on the situation."
    scene ep10_after_english20 with dissolve
    mc "Oh?"
    scene ep10_after_english22 with dissolve
    my "Do you guys have time to meet up later? Like afternoonish?"
    my "I think it would feel best if everyone involved were there so we can discuss it."
    scene ep10_after_english23 with dissolve
    mc "Sure. I'm there for you. When and where?"
    scene ep10_after_english22 with dissolve
    my "I'll let you know after I've talked to Sage. Ok?"

scene ep10_after_english24 with dissolve
de "[mc_de_up]! What the hell is that?"
scene ep10_after_english25 with dissolve
mc "Huh?"
mc "Our... Our Hell Week photos?"
my "Um... Aren't those the disgusting pictures from your wall? You know, the one with that devil mask."
scene ep10_after_english26 with dissolve
mc "They are... Who would do this?"
de "Small dick!? My dick isn't small! It was cold in that mall!"
de "And it doesn't help that I had to run next to the Loch Ness monster cock."
mc "No body hair? Why would someone write that?"
scene ep10_after_english27 with dissolve
my "These pictures are less than flattering, even without the text."
de "They didn't have to write my name on it. This is an attack on all of us."
scene ep10_after_english28 with dissolve
mc "I'll let the DIKs know about it. They'll help us tear down the posters."
scene ep10_after_english29 with dissolve
de "We gotta do it now, [mc_de]! Let's split up and walk around campus."
scene ep10_after_english28 with dissolve
mc "We can't. We need to be at the city lab for our lecture in 30 minutes."
scene ep10_after_english30 with dissolve
my "It's not on campus?"
scene ep10_after_english32 with dissolve
mc "No, they have lecture halls and laboratories over there."
scene ep10_after_english33 with dissolve
de "Rusty! It's me! Look, I have no time to explain, but our cocks are all over campus! You need to fix this!"
scene ep10_after_english32 with dissolve
mc "Looks like he beat me to it."
scene ep10_after_english30 with dissolve
my "You don't seem too bothered by it."
scene ep10_after_english32 with dissolve
mc "I am, but mine is probably not as bad as what the other guys got."
scene ep10_after_english30 with dissolve
my "Your dick is on that poster..."
scene ep10_after_english32 with dissolve
mc "Yeah...but it doesn't have my name on it, at least. And I'm wearing a mask. I hope that helps..."
scene ep10_after_english30 with dissolve
my "I'll help remove the posters I find."
scene ep10_after_english32 with dissolve
mc "Could you?"
scene ep10_after_english31 with dissolve
my "Yeah, it's not a problem. I did it with Cathy's posters, too."
my "I don't get it. Even after she quit, someone still puts them up in the hallways."
scene ep10_after_english32 with dissolve
mc "Thanks, Maya."
scene ep10_after_english33 with dissolve
de "Yes! It says it right here under your name!"
de "Manwhore."
stop music fadeout 3
de "Are you a whore, Rusty? Are you?"
$ new_bio("Derek", "Someone put up posters on campus of our Hell Week photos with derogatory comments, and Derek got upset.")

label ep10_riqu_label:
play music "music/ep8/licensed_music/track65.mp3"
scene ep10_riqu1 with wipeleft
$ renpy.pause()
scene ep10_riqu2 with dissolve
ri "Is everything there this time?"
scene ep10_riqu5 with dissolve
qu "Yeah. We're back where we need to be, thanks to everyone's efforts."
scene ep10_riqu3 with dissolve
ri "No shortage? No surplus of anything?"
scene ep10_riqu5 with dissolve
qu "Nope, none. I told you. We're right on the money."
scene ep10_riqu3 with dissolve
ri "And no drugs missing this time?"
scene ep10_riqu6 with dissolve
qu "Bitch, I told you twice. Don't make me repeat it again."
scene ep10_riqu3 with dissolve
ri "I'm making sure."
scene ep10_riqu6 with dissolve
qu "You don't have to make sure. That's my job."
scene ep10_riqu4 with dissolve
ri "Yeah, but considering you blamed me for it last time, I figured I'd check one time extra."
scene ep10_riqu7 with dissolve
qu "What?"
scene ep10_riqu4 with dissolve
ri "You told Tommy I smoked for free. And you know damned well I never did!"
scene ep10_riqu7 with dissolve
qu "What's going on here?"
scene ep10_riqu4 with dissolve
ri "Don't play dumb with me. You know exactly what I'm talking about!"
ri "It was you, wasn't it? You're the one who smoked for free and then blamed me for it. That's why we were short, to begin with."
scene ep10_riqu8 with dissolve
qu "Watch your tongue!"
scene ep10_riqu4 with dissolve
ri "Tell me what happened. I deserve to know."
scene ep10_riqu6 with dissolve
qu "I don't know what happened."
scene ep10_riqu3 with dissolve
ri "Right. But you blamed me without batting an eye."
scene ep10_riqu6 with dissolve
qu "It's not Tommy's business anyway. What happened doesn't concern him."
scene ep10_riqu9 with dissolve
ri "But it concerns me. I wanna see the book."
scene ep10_riqu10 with dissolve
qu "The hell you will."
scene ep10_riqu11 with dissolve
ri "Why? Because it would show me what I already know? That you're using and not paying for it."
scene ep10_riqu10 with dissolve
qu "Because it's my book. No one touches it but me."
scene ep10_riqu11 with dissolve
ri "You're fucking full of yourself."
scene ep10_riqu14 with dissolve
qu "Drop the bitch fit. Didn't you hear me say that we're back on track?"
qu "I won't use you like that in the future."
qu "I only said it was you because I tried to defend myself when Tommy got mad at me."
scene ep10_riqu11 with dissolve
ri "I'm not your convenient excuse."
scene ep10_riqu15 with dissolve
qu "I know you're not."
qu "You're valuable to me. Without you, I couldn't do this."
scene ep10_riqu12 with dissolve
ri "..."
scene ep10_riqu13 with dissolve
ri "Do you mean it?"
scene ep10_riqu16 with dissolve
qu "I do."
qu "Don't you see everything I do to protect you?"
qu "Can we stop fighting about this and focus on the task ahead?"
qu "We're good to go now! And considering we could make up for it this fast, think of the possibilities!"
qu "We'll be making a fortune in no time and we don't have to go all the way back to our usual prices."
scene ep10_riqu12 with dissolve
ri "..."
scene ep10_riqu13 with dissolve
ri "Don't do that to me again... Ok?"
scene ep10_riqu16 with dissolve
qu "I promise."
stop music fadeout 3
qu "Are we good?"
scene ep10_riqu13 with dissolve
ri "Yeah. We're good."

label ep10_science_intro_label:
play music "music/ep8/licensed_music/track63.mp3"
scene ep10_science_intro1 with wipeleft
$ renpy.pause()
scene ep10_science_intro2 with dissolve
$ renpy.pause()
scene ep10_science_intro3 with dissolve
if dtype > 0:
    mc "Hold the fuck up..."
else:
    mc "Wait a minute..."
scene ep10_science_intro4 with dissolve
mc "What are you doing here?"
scene ep10_science_intro5 with dissolve
sy "What does it look like I'm doing here?"
scene ep10_science_intro4 with dissolve
mc "This is an intro class. Did you flunk it in the past?"
scene ep10_science_intro5 with dissolve
sy "Eww! I do not flunk courses. Just because that's your frame of reference to college doesn't mean it's my reason for attendance."
scene ep10_science_intro4 with dissolve
mc "Then why are you here?"
scene ep10_science_intro5 with dissolve
sy "I need the STEM credits, ok?"
scene ep10_science_intro4 with dissolve
mc "Ah! And this is an easy course to get that. Gotcha."
scene ep10_science_intro6 with dissolve
sy "Easy course, my ass! I may lack the prerequisites for a more advanced class, but that doesn't make this class easy."
scene ep10_science_intro4 with dissolve
mc "I'm confused. You're saying classes are easy since you don't flunk them, but that this class is hard for you?"
mc "Is the class easy or hard, Sally? Make up your mind."
scene ep10_science_intro6 with dissolve
sy "Bite me!"
if affinity == "DIK":
    scene ep10_science_intro4 with dissolve
    mc "*{i}Bite sound{/i}*"
    scene ep10_science_intro7 with dissolve
    sy "Pff..."
else:
    scene ep10_science_intro4 with dissolve
    mc "Do you want me to?"
if ep9_helped_sally:
    scene ep10_science_intro5 with dissolve
    sy "And if you're wondering about your clothes, I'll drop them off later."
    scene ep10_science_intro4 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Tease her [m_c1][mod_choices[3]]":
            $ dk(1)
            scene ep10_science_intro3 with dissolve
            if dtype > 0:
                mc "I wasn't. But that's fine. I like you more when you're nude and drunk."
            else:
                mc "I wasn't. But that's fine. I like you more when you drink."
        "Whatever works for you [m_c1][mod_choices[2]]":
            $ dk(-1)
            scene ep10_science_intro3 with dissolve
            mc "Whatever works for you."
else:
    scene ep10_science_intro3 with dissolve
    mc "Well, good luck with it."

scene ep10_science_intro8 with dissolve
mc "How are you holding up?"
scene ep10_science_intro9 with dissolve
de "I feel raped, [mc_de]. Raped."
scene ep10_science_intro10 with dissolve
menu:
    "You're not raped":
        mc "Relax. You're not raped."
        scene ep10_science_intro9 with dissolve
        de "Then why do I wanna curl up in the shower and scald my body with hot water?"
        scene ep10_science_intro10 with dissolve
        mc "Because you're overly dramatic at times."
    "I get that":
        mc "Yeah, I get that feeling. I feel sorry for you."
        scene ep10_science_intro9 with dissolve
        de "You don't get this feeling at all."
        scene ep10_science_intro10 with dissolve
        mc "You saw me on that poster, too, didn't you?"
        mc "I don't think you're the only one at college named Derek, and at least you're wearing a mask."
        scene ep10_science_intro9 with dissolve
        de "It said we were DIKs, too. People will know it's me."
        scene ep10_science_intro10 with dissolve
        mc "Oh, yeah... But try to stay positive."
    "The picture wasn't that bad":
        mc "The picture wasn't that bad. It didn't show your face; someone assumed it was you."
        scene ep10_science_intro9 with dissolve
        de "They assumed correctly..."
        scene ep10_science_intro10 with dissolve
        mc "Still, it's an assumption."
$ guideSuggestedPage = 104
scene ep10_science_intro9 with dissolve
de "It's easy for you to say. They didn't write your name next to your cock. Not that it would do you anything bad if they did."
de "They'd probably have a parade for the monument they built out of it."
de "Couldn't they have assumed that I was the one with the big one?"
scene ep10_science_intro10 with dissolve
mc "My comment wasn't that flattering either... I mean...I can grow body hair."
mc "But haven't we learned something from what happened to Cathy?"
mc "Someone tried to make her look bad and it bullied her into quitting."
mc "And now, someone is trying to do the same with us for some reason."
scene ep10_science_intro11 with dissolve
de "Wait a minute... Do you think it's the same person doing it? It could be, right?"
scene ep10_science_intro12 with dissolve
menu:
    "Similar methods":
        mc "The method is similar, but anyone can put up a poster."
        scene ep10_science_intro11 with dissolve
        de "But only someone who was in our mansion could have gotten those pictures. They're on our wall."
        scene ep10_science_intro12 with dissolve
        mc "True. But many have been, so it doesn't narrow it down by a lot."
    "Why would it be?":
        mc "Why would it be the same person?"
        scene ep10_science_intro11 with dissolve
        de "Because it's happened two times now and both have been targeting us somehow."
        de "And only someone who was in our mansion could have gotten those pictures. They're on our wall and Cathy's picture was posted from our computer."
        scene ep10_science_intro12 with dissolve
        mc "True. But a lot of people have been to our mansion, so it doesn't narrow it down by a lot."
scene ep10_science_intro11 with dissolve
de "It must be someone from the Halloween party. I can feel it in my gut."
scene ep10_science_intro13 with dissolve
de "First, someone makes dirty movies of me in my room, and now my average-sized penis is put on display and called small to everyone on campus."
de "Why is this happening to me?"
scene ep10_science_intro14 with dissolve
mc "We'll bounce back from this, bro."
scene ep10_science_intro16 with dissolve
te5 "Welcome to Introduction to Science - Applied Chemistry In Theory & Practice."
te5 "I can see that the class consists of freshman and older students. That's nice."
te5 "For those of you who don't know me, I am Professor Willcock."
scene ep10_science_intro15 with dissolve
de "Haha! Cock."
mc "Haha... Grow up."
scene ep10_science_intro16 with dissolve
te5 "I will be your teacher for the theoretical portion of this course."
te5 "That means that it's me who you want to impress to get a higher grade."
te5 "Haha, I'm kidding. But I am the one grading your papers, so it's not all a joke."
scene ep10_science_intro17 with dissolve
te5 "While I will teach you the basics of the chemistry you should master at a university level, Dr. Jenkins will be in charge of the lab work."
te5 "The lab portion will focus on developing your skills in calculations, measuring and various forms of analysis."
te5 "Since the class is too big for the lab, we will split the class into two groups. Make sure you sign up for one of the groups before you leave today."
scene ep10_science_intro16 with dissolve
te5 "These lectures will primarily be me up here teaching you the theory. Make notes - a lot of them - and ask questions when you have one. Please don't be shy to interrupt me."
stop music fadeout 5
te5 "Today, we will start with atom orbitals. Fascinating stuff!"
show ep10_science_intro18
if not persistent.ep10_cardzo4:
    show screen ep10_render_screen("zo4")
with dissolve
$ renpy.pause()
$ new_bio("Sally", "Sally attended my science class, and I triggered her a bit about it.")

label ep10_ipb_label:
play music "music/ep4/inspiring_acoustic.mp3"
show ep10_ipb1
hide screen ep10_render_screen
with wipeleft
$ renpy.pause()
scene ep10_ipb2 with dissolve
ph "Good afternoon, Mrs. Roberts."
scene ep10_ipb3 with dissolve
isa "Professor Hoff."
scene ep10_ipb4 with dissolve
if ep8_midterms_cheated != "DIK":
    ph "I have parsed the test at your request."
else:
    ph "I have parsed the tests at your request."
scene ep10_ipb7 with dissolve
isa "Oh, thank you. Did you find anything?"

if ep8_midterms_cheated == "CHICK":
    scene ep10_ipb4 with dissolve
    ph "I'm afraid I have to disappoint you. There is nothing that suggests the student in question had cheated."
    ph "In fact, he or she didn't do well on the test. It's passable but below average."
    scene ep10_ipb7 with dissolve
    isa "I see..."
    scene ep10_ipb5 with dissolve
    ph "But the lack of evidence on my end doesn't mean that your findings are for naught."
    scene ep10_ipb8 with dissolve
    isa "No, I know. I was hoping to support my theory with your help. Now, I don't know what to do with it."
    scene ep10_ipb6 with dissolve
    ph "If you want my professional advice, I'd tell you to correct the test fairly."
    ph "And I'd tell you to also keep a watchful eye on your students during class and future tests."
    scene ep10_ipb7 with dissolve
    isa "Thank you, Professor."
    scene ep10_ipb5 with dissolve
    ph "And thank you, Mrs. Roberts. If this matter crosses my path in the future, I'll make sure to let you know."
    stop music fadeout 3
    scene ep10_ipb12 with dissolve
    $ renpy.pause()
elif ep8_midterms_cheated == "NEUTRAL":
    scene ep10_ipb4 with dissolve
    ph "I did. I missed it the first time, but some lines of reasoning didn't justify the answer."
    ph "That's not necessarily surprising, but when the answer was correct down to the last decimal while showing an erroneous calculation, it strikes me as odd."
    scene ep10_ipb5 with dissolve
    ph "That, combined with your data, makes me concerned that you are right about this student."
    ph "I believe you are onto something, but I cannot prove how they cheated on the test."
    scene ep10_ipb6 with dissolve
    ph "And my findings are hardly sufficient to make these grave accusations. And when you add that we aren't supposed to share this knowledge with each other..."
    ph "...as much as it hurts my academic heart, I move to let it slide this time. But also to keep a watchful eye on the student during class and future tests."
    ph "Perhaps we have a chance to find damning evidence now that you've opened our eyes to it."
    scene ep10_ipb8 with dissolve
    isa "I have to agree."
    scene ep10_ipb5 with dissolve
    ph "Excellent. The only remaining conundrum is translating the student ID number into a name."
    scene ep10_ipb7 with dissolve
    isa "I have the tools for it. The library connects the student ID card to the students."
    scene ep10_ipb5 with dissolve
    ph "Well, then, let's have a look. We might as well go all the way."
    scene ep10_ipb9 with dissolve
    isa "There it is..."
    scene ep10_ipb10 with dissolve
    ph "Anderson, huh? *{i}Sigh{/i}* Such a shame."
    scene ep10_ipb5 with dissolve
    ph "Thank you, Mrs. Roberts. If this matter becomes an issue in the future, I'll make sure to share it with you."
    stop music fadeout 3
    scene ep10_ipb12 with dissolve
    $ renpy.pause()
else:
    scene ep10_ipb4 with dissolve
    ph "I did. I missed it the first time, but some lines of reasoning in one of them didn't justify the answer."
    ph "That's not necessarily surprising, but when the answer was correct down to the last decimal while showing an erroneous calculation, it strikes me as odd."
    ph "The cheating in the other test wasn't as blatant, but I gave half a point for some questionable conclusions in my initial assessment."
    ph "Honestly, I could have chalked it up to guesswork with this one. But it had the same exact sentence as the first test."
    scene ep10_ipb5 with dissolve
    ph "Which could mean that someone was reading their neighbor's answers and copying them. If that's the case, I believe it's the first who cheated off the second one."
    ph "Anyway... That's pure speculation."
    ph "But, that, combined with your data, makes me concerned that there is some truth to your suspicions."
    ph "I believe you are onto something, but I cannot prove how they cheated on the test."
    scene ep10_ipb6 with dissolve
    ph "And my findings are hardly sufficient to make these grave accusations. And when you add that we aren't supposed to share this knowledge with each other..."
    ph "...as much as it hurts my academic heart, I move to let it slide this time. But also to keep a watchful eye on the students during class and future tests."
    ph "Perhaps we have a chance to find damning evidence now that you've opened our eyes to it."
    scene ep10_ipb8 with dissolve
    isa "I have to agree."
    scene ep10_ipb5 with dissolve
    ph "Excellent. The only remaining conundrum is translating the student ID numbers into names."
    scene ep10_ipb7 with dissolve
    isa "I have the tools for it. The library connects the student ID card to the students."
    scene ep10_ipb5 with dissolve
    ph "Well, then, let's have a look. We might as well go all the way."
    scene ep10_ipb9 with dissolve
    isa "There it is..."
    scene ep10_ipb10 with dissolve
    ph "Anderson, huh? *{i}Sigh{/i}* Such a shame."
    ph "And the other one?"
    isa "Uh..."
    if lname == "Anderson":
        ph "The other [lname]... They're not related, are they?"
    else:
        ph "[lname]."
    scene ep10_ipb9 with dissolve
    isa "No, this must be a mistake."
    scene ep10_ipb6 with dissolve
    ph "I'm sorry, Mrs. Roberts. This hurts me, too."
    scene ep10_ipb5 with dissolve
    ph "Thank you for bringing it to my attention. If this matter becomes an issue in the future, I'll make sure to share it with you."
    stop music fadeout 3
    scene ep10_ipb12 with dissolve
    $ renpy.pause()
    scene ep10_ipb11 with dissolve
    $ renpy.pause()

label ep10_plan_label:
play music "music/ep7/licensed_music/track49.mp3"
play sound "sound_effects/season3/scratch.mp3"
scene ep10_plan1 with wipeleft
$ renpy.pause()
scene ep10_plan2 with dissolve
sa "Seriously? Lottery tickets? Is this your big idea?"
scene ep10_plan3 with dissolve
de "A million dollars, Sage! Did you ever have that?"
scene ep10_plan4 with dissolve
sa "You don't buy a million dollars, moron. You buy a minuscule chance to win it."
sa "And simple probabilistic analysis would tell you that buying one ticket is the better option."
sa "When you're buying this many, you're basically throwing money away hoping to get struck by lightning."
scene ep10_plan3 with dissolve
de "I'll show you."
scene ep10_plan5 with dissolve
mc "What's the actual plan?"
scene ep10_plan6 with dissolve
my "We'll see what Jill has to say."
scene ep10_plan5 with dissolve
mc "And does she know about you and Josy?"
scene ep10_plan6 with dissolve
my "Not yet."
scene ep10_plan5 with dissolve
mc "Are you gonna let her know or...?"
scene ep10_plan6 with dissolve
my "I probably have to, but it's tough..."
my "It's nothing against her personally, but I feel like too many people already know."
scene ep10_plan7 with dissolve
sa "Yes. And I'm not entirely sure we can trust her."
scene ep10_plan8 with dissolve
mc "We can trust her. I know it."
if ep9_jm_sad and branchJill:
    scene ep10_plan9 with dissolve
    $ renpy.pause()

scene ep10_plan10 with dissolve
js "Jill's incoming."
scene ep10_plan11 with dissolve
sa "Finally."
if ep9_jm_sad:
    scene ep10_plan12 with dissolve
    $ renpy.pause()
    scene ep10_plan13 with dissolve
    $ renpy.pause()
    scene ep10_plan14 with dissolve
    js "I'll wait for her outside."
    if branchSage:
        scene ep10_plan15 with dissolve
        $ renpy.pause()
    else:
        scene ep10_plan16 with dissolve
        sa "*{i}Whispers{/i}* Is there something up with Josy and [name]?"
        scene ep10_plan17 with dissolve
        my "*{i}Whispers{/i}* I...can't tell you."
        scene ep10_plan18 with dissolve
        sa "*{i}Whispers{/i}* He seems low and she seems angry. What happened?"
        scene ep10_plan17 with dissolve
        my "*{i}Whispers{/i}* You'll have to ask her about that."
elif branchMayaJosy:
    scene ep10_plan21 with dissolve
    js "Hey, you."
    mc "Hi."
    scene ep10_plan22 with dissolve
    $ renpy.pause()
    scene ep10_plan23 with dissolve
    sa "So... Two girlfriends, huh?"
    scene ep10_plan24 with dissolve
    mc "I had to cover for Josy and Maya when the DIKs found out."
    scene ep10_plan23 with dissolve
    sa "That doesn't make it less true, does it?"
    scene ep10_plan25 with dissolve
    js "It feels weird telling others about this..."
    scene ep10_plan24 with dissolve
    mc "I got Derek's blessing, so yeah."
    scene ep10_plan26 with dissolve
    de "Don't push it. Maya's basically 99%% me. Think about that next time you stick something in her."
    scene ep10_plan27 with dissolve
    my "Eww! Stop it, Derek! And you know that's not how our kind of twins work."
    scene ep10_plan23 with dissolve
    sa "And I thought Elena's and John Boy's relationship was special."
    sa "Good for you, guys."
    scene ep10_plan28 with dissolve
    $ renpy.pause()
else:
    scene ep10_plan19 with dissolve
    js "What's he doing?"
    scene ep10_plan20 with dissolve
    if dtype > 0:
        mc "He's working on a gambling addiction. It was his idea of helping."
    else:
        mc "He's scratching lottery tickets. It was his idea of helping."

if ep9_jm_sad:
    scene ep10_plan30 with dissolve
else:
    scene ep10_plan29 with dissolve
ji "Hi, everyone."
scene ep10_plan31 with dissolve
sa "Great, we're all here. Shall we?"
scene ep10_plan32 with dissolve
my "Yes. Um...Jill? Come over here. We need to fill you in."

scene ep10_plan33 with dissolve
mc "Any winners?"
de "If you help me scratch, this will be faster."
mc "No thanks, I'll leave that excitement to you."
scene ep10_plan34 with dissolve
mc "But for real, do you have another plan or...?"
scene ep10_plan35 with dissolve
de "No, [mc_de]. I don't have another plan."
de "I've tried thinking about one, but I come up with nothing every time."
de "This is not as easy as you think it is."
scene ep10_plan34 with dissolve
mc "I never thought it was easy."
scene ep10_plan35 with dissolve
de "Still, it's harder than you think."
de "You're on the outside looking in. You're not living it."
scene ep10_plan34 with dissolve
mc "It's tough for you, too, huh?"
scene ep10_plan36 with dissolve
de "..."

scene ep10_plan37 with dissolve
ji "I'm confused. So...you two are...?"
scene ep10_plan41 with dissolve
if branchMayaJosy:
    js "Yes. And we're with [name], too. The three of us are in a relationship, but it's supposed to be a secret."
    if ep9_jill_mood == 1:
        scene ep10_plan38 with dissolve
        ji "Uh... Ok... That's a lot of information to digest."
        scene ep10_plan39 with dissolve
        $ renpy.pause()
    else:
        scene ep10_plan38 with dissolve
        ji "Oh... That's a lot of information to digest."
else:
    js "Yes."
scene ep10_plan42 with dissolve
if branchMayaJosy:
    my "But Josy's and my relationship is what Dad's ultimatum was about."
else:
    my "That's what Dad's ultimatum was about."
scene ep10_plan40 with dissolve
ji "I didn't expect you to tell me this when you asked me for help. I thought it was something simpler."
ji "Everything about this sounds very...unusual. And I don't know where to start."
scene ep10_plan37 with dissolve
ji "The first question that comes to mind is: Is it actually a student loan? Because the way you describe it, it doesn't sound like one."
scene ep10_plan43 with dissolve
my "It is. He said it was a student loan application."
scene ep10_plan46 with dissolve
sa "He said so...?"
scene ep10_plan44 with dissolve
my "I mean, isn't any loan that will fund college technically a student loan?"
scene ep10_plan47 with dissolve
ji "No, not at all. It depends on the nature of the contract."
ji "You can fund college in many different ways. For one, if it's a private loan used to fund college, it's not a student loan."
scene ep10_plan46 with dissolve
sa "Don't you know what you signed?"
scene ep10_plan44 with dissolve
my "He showed me a pile of papers and told me what they meant."
scene ep10_plan47 with dissolve
ji "Did you read the papers?"
scene ep10_plan43 with dissolve
my "No, I trusted him. Derek did it, too."
scene ep10_plan47 with dissolve
ji "Where are your copies?"
scene ep10_plan43 with dissolve
my "I don't have any."
scene ep10_plan48 with dissolve
ji "..."
scene ep10_plan46 with dissolve
sa "Why wouldn't you have copies?"
scene ep10_plan45 with dissolve
my "Because I don't, ok!?"
scene ep10_plan49 with dissolve
js "Maya..."
scene ep10_plan50 with dissolve
my "Dad had it rough when we grew up, and it's not been easy for any of us."
my "But not in a million years did I think he'd fuck me over like this."
scene ep10_plan51 with dissolve
my "He's the one who's supposed to care for me. The one who's supposed to teach me everything about life and protect me."
my "I know that it sounds stupid, naive and irresponsible, but the only thing I did was to trust Dad."
scene ep10_plan50 with dissolve
my "..."
scene ep10_plan48 with dissolve
$ renpy.pause()
scene ep10_plan52 with dissolve
ji "This is tough."
ji "I'm so sorry, Maya."
scene ep10_plan54 with dissolve
mc "Jill... Do you have any ideas?"
scene ep10_plan48 with dissolve
ji "..."
scene ep10_plan52 with dissolve
ji "I'm hardly an expert, but I can ask our family's lawyer."
ji "However, I feel that I need to bring him more information to make sense of it."
scene ep10_plan42 with dissolve
my "I've told you all that I know."
scene ep10_plan34 with dissolve
mc "What about you, Derek? Can you add anything?"
scene ep10_plan35 with dissolve
de "I'm shamefully in the same spot as her. Sort of, but not as bad. He's not threatening to take college away from me."
scene ep10_plan53 with dissolve
ji "My first thought was that we should ask someone who works here for advice. Someone who knows B&R's system."
ji "Maybe there is something we're missing."
ji "And since it's a sensitive topic... I think Bella would be the one to help."
ji "And I can assure you that she can be trusted."
if ep9_jill_mood > 1:
    scene ep10_plan56 with dissolve
    $ renpy.pause()
    scene ep10_plan55 with dissolve
    $ renpy.pause()
scene ep10_plan57 with dissolve
js "Maya... You're already letting more people in on this. One more won't hurt."
scene ep10_plan58 with dissolve
sa "We will get to the bottom of this. You know that, right?"
scene ep10_plan44 with dissolve
my "Ok."
scene ep10_plan59 with dissolve
de "I won!"
scene ep10_plan62 with dissolve
sa "You did?"
scene ep10_plan59 with dissolve
de "I fucking won!"
scene ep10_plan60 with dissolve
sa "You won $10..."
de "But I won! It's proof of concept."
scene ep10_plan61 with dissolve
mc "You spent $50 on buying these."
stop music fadeout 3
scene ep10_plan53 with dissolve
ji "If we leave now, we can catch her before she returns home."

label ep10_library_label:
play music "music/ep3/guitar_melancholy2.mp3"
show ep10_library1
if not persistent.ep10_cardzo5:
    show screen ep10_render_screen("zo5")
with fade
$ renpy.pause()
show ep10_library2
hide screen ep10_render_screen
with dissolve
$ renpy.pause()
scene ep10_library3 with dissolve
isa "I agree with Jill on this. It sounds peculiar."
scene ep10_library4 with dissolve
isa "If what you say is true, that it's your father paying the school for your studies, any answers I'd possibly find wouldn't help you."
isa "On top of that, I neither have rights nor access to view those records."
isa "Have you checked your credit report?"
scene ep10_library5 with dissolve
my "I have, but it wasn't on there last time when I checked."
my "It's probably because it's co-signed or maybe because it's too recent."
scene ep10_library4 with dissolve
isa "I think it would still show. All your loans should be on it."
scene ep10_library5 with dissolve
my "But it's not, and I know I signed a contract for a loan."
scene ep10_library4 with dissolve
isa "Then what I would suggest is to read the contract."
scene ep10_library5 with dissolve
my "I told you I don't have it."
scene ep10_library4 with dissolve
isa "I know. But your dad has it. He has to."
isa "Would he let you view it?"
scene ep10_library5 with dissolve
my "I fear he'd suspect that I'm up to something if I asked him to see it."
scene ep10_library7 with dissolve
de "He keeps it in his home office."
scene ep10_library6 with dissolve
my "Are you sure?"
scene ep10_library7 with dissolve
de "Well, he keeps mine there. I saw him put it in a binder after I signed it."
scene ep10_library9 with dissolve
sa "You need to get that binder."
scene ep10_library8 with dissolve
de "I can't do that. He locks that door and brings the key with him. There is no way I could get it on my own without him noticing."
scene ep10_library11 with dissolve
mc "What if we helped you get it somehow?"
scene ep10_library12 with dissolve
de "Sure, just tell me why you would be invited to my parents' house and snoop around, and we'll do it."
scene ep10_library11 with dissolve
mc "I'm spitballing ideas here. There's no need to be like that."
scene ep10_library15 with dissolve
my "Thanksgiving."
scene ep10_library16 with dissolve
mc "What about it?"
scene ep10_library15 with dissolve
my "Derek and I are going home for Thanksgiving dinner. We can try to get it then."
scene ep10_library7 with dissolve
de "I'm telling you, you and me alone aren't enough to do that."
if ep8_told_josy_chad:
    scene ep10_library17 with dissolve
    js "I've got it! You need a beard!"
    scene ep10_library7 with dissolve
    de "Why would me growing one help with that?"
    scene ep10_library18 with dissolve
    js "No! Not you! Maya!"
    scene ep10_library7 with dissolve
    de "That will require hormones. Are you up for it?"
    scene ep10_library18 with dissolve
    js "Be quiet!"
    scene ep10_library17 with dissolve
    js "What if you told your dad you got a boyfriend and wanted to bring him back home for Thanksgiving?"
    scene ep10_library19 with dissolve
    my "A boyfriend?"
    scene ep10_library17 with dissolve
    js "He'll be overjoyed about that, don't you think? Isn't that what he wants for you?"
    js "Then you distract him, sneak into his office and get that binder."
    scene ep10_library19 with dissolve
    my "That...could work."
    scene ep10_library22 with dissolve
    mc "Who? Me?"
    scene ep10_library23 with dissolve
    my "Could you?"
    scene ep10_library10 with dissolve
    if branchMayaJosy:
        sa "It has to be you. I mean, isn't it you?"
    else:
        sa "It has to be you."
    scene ep10_library12 with dissolve
    de "It can't be me. I think that would make things even worse."
    scene ep10_library11 with dissolve
    mc "Ok. I'll do it. But will it be enough?"
    scene ep10_library13 with dissolve
    de "Oh! I know!"
    de "I can get a girlfriend to come too! It would be four against one. We'd have enough distractions to do it easily."
    de "Any takers?"
    scene ep10_library18 with dissolve
    js "It can't be me, for obvious reasons."
    scene ep10_library14 with dissolve
    de "You don't like me?"
    scene ep10_library6 with dissolve
    my "Derek..."
    scene ep10_library14 with dissolve
    de "Don't say yes all at once."
    scene ep10_library21 with dissolve
    sa "Fine, I'll do it."
    scene ep10_library13 with dissolve
    de "Yes! Amazing."
else:
    scene ep10_library16 with dissolve
    mc "How about if you invite a friend for dinner? Would that work?"
    scene ep10_library15 with dissolve
    my "Yes, that could work!"
    scene ep10_library12 with dissolve
    de "Thanks, [mc_de]. I knew you had our backs."
    scene ep10_library22 with dissolve
    mc "Oh... I'm the friend?"
    scene ep10_library15 with dissolve
    my "Yeah. I mean, who else?"
    my "I don't feel comfortable bringing home a girl to meet Dad, even if it's a friend only."
    scene ep10_library12 with dissolve
    de "And my friends aren't girls. It would be suspicious."
    scene ep10_library11 with dissolve
    mc "Ok. I'll do it. Let's hope that's enough to do it."

scene ep10_library19 with dissolve
my "Does it sound like a good plan?"
scene ep10_library20 with dissolve
js "It's a plan, at least."
scene ep10_library25 with dissolve
isa "I'm sorry that I couldn't be of more help."
scene ep10_library24 with dissolve
my "Don't be. We came here without a plan and we'll leave here with one..."
my "So, thank you for that."
scene ep10_library25 with dissolve
isa "If there's anything else I can do, let me know."
scene ep10_library26 with dissolve
my "And Jill... Thank you, too."
my "She's the one who suggested us to come here."

if branchIsabella:
    scene ep10_library27 with dissolve
    $ renpy.pause()

if branchJill:
    scene ep10_library28 with dissolve
    if ep8_midterms_cheated != "DIK":
        stop music fadeout 5
    ji "Do you want to come back to my place? I need to talk to you in private."
    scene ep10_library29 with dissolve
    mc "Sure, I'd love to."
else:
    scene ep10_library39 with dissolve
    ji "[name]. Can we talk about something in private?"
    if ep8_midterms_cheated != "DIK":
        stop music fadeout 3
    scene ep10_library40 with dissolve
    mc "Sure."

$ new_bio("Maya", "Maya let Jill and Bella know about her student loan issues, and we all tried to come up with a plan to help her.")
$ new_bio("Jill", "Jill was supportive when Maya let her know about her student loan issues, and we all tried to come up with a plan to help her.")
$ new_bio("Isabella", "Bella was supportive when Maya let her know about her student loan issues, and we all tried to come up with a plan to help her.")
if ep8_told_josy_chad:
    $ new_bio("Josy", "Josy came up with the idea to have me act like Maya's boyfriend during Thanksgiving so that we could steal the contract Maya signed from Patrick.")
else:
    $ new_bio("Maya", "I agreed to help Maya steal the contract she signed from Patrick by showing up at Thanksgiving dinner as Derek's and Maya's friend.")

if ep8_midterms_cheated == "DIK":
    scene ep10_library30 with dissolve
    isa "[name]? Can you stay behind for a while?"
    if branchJill:
        scene ep10_library29 with dissolve
        mc "I'll drop by soon, ok?"
    else:
        scene ep10_library41 with dissolve
        ji "I'll wait for you outside."
        scene ep10_library40 with dissolve
        mc "I'll be right with you."
    if branchIsabella:
        scene ep10_library31 with dissolve
        mc "So... Still thinking about our make-out session?"
        scene ep10_library32 with dissolve
        isa "That's not why I asked you to stay behind."
    else:
        scene ep10_library31 with dissolve
        mc "What's up?"
        scene ep10_library32 with dissolve

    isa "Why are you cheating on your midterm tests?"
    scene ep10_library33 with dissolve
    mc "..."
    mc "Uh..."
    scene ep10_library34 with dissolve
    isa "*{i}Sigh{/i}* I knew it..."
    scene ep10_library33 with dissolve
    mc "Fuck... How did you know?"
    scene ep10_library34 with dissolve
    isa "There were too many things that didn't add up with your test."
    isa "And I asked Professor Hoff to investigate his exam, too."
    scene ep10_library33 with dissolve
    mc "You told Professor Hoff I cheated!?"
    scene ep10_library35 with dissolve
    isa "That was before I knew it was you."
    isa "And that shouldn't even matter. Why the hell are you cheating?"
    isa "You're not this stupid! This will get you into big trouble, [name]. Don't you get that?"
    scene ep10_library33 with dissolve
    mc "I didn't think ahead... I went to the bathroom, found some papers lodged behind the toilet tank, and started reading them."
    mc "It turned out they were test answers-"
    scene ep10_library35 with dissolve
    isa "Test answers? {b}The{/b} test answers?"
    scene ep10_library33 with dissolve
    mc "No, not just the answers to the test, but a bunch of test questions and answers."
    mc "I found a few on my test and read the answers to them."
    mc "And after the math test, the same thing happened during the English test."
    scene ep10_library35 with dissolve
    isa "There were papers behind the toilet tank again?"
    scene ep10_library33 with dissolve
    mc "Yes..."
    scene ep10_library35 with dissolve
    isa "Describe the papers to me."
    scene ep10_library33 with dissolve
    mc "They were printed pages full of questions and answers. They weren't in any kind of order or anything."
    scene ep10_library32 with dissolve
    isa "How many papers were there?"
    scene ep10_library33 with dissolve
    mc "I don't know - a lot."
    scene ep10_library37 with dissolve
    mc "Like this much when stacked together."
    scene ep10_library36 with dissolve
    mc "So...what's gonna happen to me?"
    scene ep10_library35 with dissolve
    isa "Huh?"
    scene ep10_library33 with dissolve
    mc "Am I getting expelled?"
    scene ep10_library32 with dissolve
    isa "Luckily for you, you didn't get caught on Philip's test."
    scene ep10_library33 with dissolve
    mc "Oh?"
    scene ep10_library32 with dissolve
    isa "But he's keeping an eye on you from now on. He is suspicious and if you cheat again, make no mistake, he will catch you."
    isa "And if that happens, you will get expelled."
    scene ep10_library33 with dissolve
    mc "And what about you? You're not gonna punish me, are you?"
    scene ep10_library32 with dissolve
    isa "I'm not going to report you, [name]."
    scene ep10_library33 with dissolve
    mc "*{i}Phew{/i}* Thank you. That's good..."
    scene ep10_library34 with dissolve
    isa "It's not good."
    isa "Do you realize what situation you've put me in?"
    scene ep10_library33 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "I won't do it again [m_c1][mod_choices[2]]":
            $ ep10_bella_overreacting = False
            $ dk(-1)
            mc "I do... I'm sorry! I won't do it again."
            scene ep10_library34 with dissolve
            isa "Even so. If it was anyone but you doing this, I would have reported it."
        "You're overreacting [m_c1][mod_choices[3]]":
            $ ep10_bella_overreacting = True
            $ dk(1)
            mc "You're overreacting, Bella. It was just a couple of tests. There's no harm done."
            scene ep10_library34 with dissolve
            isa "No harm done?"
            isa "If it was anyone but you doing this, I would have reported it."
    isa "And because I care so damned much about you, I have to tarnish my professional integrity to protect you."
    scene ep10_library33 with dissolve
    mc "..."
    mc "Bella... You don't have to protect me. Go ahead and report me."
    scene ep10_library32 with dissolve
    isa "I can't do that."
    scene ep10_library33 with dissolve
    mc "If I knew you'd be affected by me cheating on a stupid test, I wouldn't have done it."
    mc "I'd rather face the consequences than hurt you like that."
    scene ep10_library32 with dissolve
    isa "You don't need to cheat, [name]. You are smarter than this."
    scene ep10_library33 with dissolve
    mc "What if I'm not? College isn't that easy for me. I don't understand everything they try to teach me."
    mc "And I guess I'm scared to fail...that's why I cheated."
    scene ep10_library35 with dissolve
    isa "When you're cheating, you are failing yourself, [name]. What if you make it through college like that?"
    isa "Every day for the rest of your life, you'll look back at college, wondering if you could have done it without cheating."
    scene ep10_library33 with dissolve
    mc "..."
    mc "How do you know?"
    scene ep10_library32 with dissolve
    isa "Because I copied the answers from a neighbor on a test in college, it was during my freshman year, too."
    isa "I had partied too much and neglected my studies. And when I wrote the test, I didn't know the answers to half of the questions."
    isa "I panicked, glanced to my right, and copied everything I could see from Jessica..."
    scene ep10_library34 with dissolve
    isa "I passed the test, barely. But I wouldn't have passed if I hadn't copied her answers."
    isa "And I have regretted that ever since."
    isa "And that's what I hope you will do too."
    scene ep10_library32 with dissolve
    isa "Learn from this mistake, [name]. That's all I will ask of you."
    stop music fadeout 3
    isa "If this happens again, you'll leave me no choice."
    scene ep10_library38 with dissolve
    $ renpy.pause()
    if ep10_bella_overreacting:
        $ new_bio("Isabella", "Bella caught me cheating on the midterms but didn't report me for it. She warned me that she would if I did it again, and I told her she was overreacting.")
    else:
        $ new_bio("Isabella", "Bella caught me cheating on the midterms but didn't report me for it. She warned me that she would if I did it again.")

if branchJill:
    jump ep10_jill_solo_label
else:
    play music "music/ep5/licensed_music/track16.mp3"
    scene ep10_library42 with dissolve
    if ep8_midterms_cheated == "DIK":
        mc "So... How are you?"
    else:
        mc "How are you?"
    scene ep10_library43 with dissolve
    ji "Not well. I don't know where to start."
    ji "*{i}Sigh{/i}* I saw the posters on campus today."
    scene ep10_library44 with dissolve
    mc "Yeah, those. It sucks... Someone is spreading the pictures we have on a wall in the mansion."
    mc "Maybe you saw them at Halloween?"
    scene ep10_library45 with dissolve
    ji "No, I didn't. I mean, I think I saw some of the pictures, but I didn't pay attention to them until today."
    ji "I'm sorry they spread like that, but it's not why I'm bringing them up."
    scene ep10_library46 with dissolve
    ji "There was this one picture that caught my eye...and I need you to be honest with me."
    scene ep10_library47 with dissolve
    ji "This one is from our mansion. Isn't it?"
    ji "That's Tybalt's bed."
    mc "Yeah. You called it. It's a Hell Week thing at the DIKs."
    ji "And those masks... They look like burglars, don't they?"
    scene ep10_library48 with dissolve
    ji "It led me to think about a break-in we had at the start of the semester when two burglars entered our mansion and stole things from us."
    ji "This was during the time you had your Hell Week."
    scene ep10_library49 with dissolve
    ji "Is there anything you'd like to tell me?"
    scene ep10_library50 with dissolve
    mc "..."
    mc "I'm sorry... It was before I knew you."
    scene ep10_library49 with dissolve
    ji "[name]..."
    scene ep10_library50 with dissolve
    mc "We had to do it for Hell Week. They wanted us to take funny pictures in Tybalt's room. And we had to enter your mansion through your room."
    mc "Your window was open."
    scene ep10_library49 with dissolve
    ji "And you stole from me and Tybalt."
    scene ep10_library50 with dissolve
    mc "What? No!"
    mc "Wait... Derek stole Tybalt's mounted deer head."
    if ep2_stole_money:
        $ RPjill -= 5
        mc "And oh... I may have taken some of your money, but it was only a few dollars and they were just lying there."
    else:
        mc "But that's it."

    if ep2_stole_money:
        scene ep10_library48 with dissolve
        ji "Wasn't a lot...? Are you justifying the amount you stole from me? And just because something lies there, it's ok to take it?"
        scene ep10_library50 with dissolve
        mc "No... Fuck, of course not. I don't know why I did that. I didn't think clearly; I was high on adrenaline. I'll pay you back."

    scene ep10_library49 with dissolve
    if ep2_stole_money:
        ji "It's not about the money, [name]. It's more about the underwear you stole and the feeling you left me feel."
    else:
        ji "And you stole my underwear and left me feeling horrible."
    ji "I had trouble sleeping because I felt like my privacy was violated."
    scene ep10_library50 with dissolve
    mc "No! I never did that. Tybalt must have stolen those."
    scene ep10_library48 with dissolve
    ji "Oh, [name]..."
    scene ep10_library51 with dissolve
    mc "I'm telling you the truth! When we were escaping through your window, we saw Tybalt in your room."
    mc "It looked like he was smelling underwear from your dresser. He saw us and called on security, not that he'd ever admit that."
    scene ep10_library50 with dissolve
    mc "Jill... You have to believe me."
    mc "I did a shitty thing because of Hell Week, and I should have told you sooner, but part of me wanted to forget about it."
    mc "And after getting to know you, I didn't think it mattered anymore."
    scene ep10_library52 with dissolve
    mc "I didn't steal your underwear. Come on. You can't believe that."
    mc "With everything Tybalt has done to you and me... You have to see through him by now."
    scene ep10_library49 with dissolve
    ji "I thought I knew you too, [name]. And I don't get it... You do good things; you do bad things..."
    ji "And right now, I don't know what to believe."
    scene ep10_library50 with dissolve
    mc "You can ask Derek if you want. He'd tell you the same story because he was there with me."
    scene ep10_library53 with dissolve
    stop music fadeout 3
    mc "Jill. I'm sorry."
    scene ep10_library54 with dissolve
    mc "Fuck..."
    $ new_bio("Jill", "Jill confronted me about Hell Week, and I told her what happened. She was obviously hurt by what I had done and had a hard time forgiving me.")

label ep10_mc_room_label:
if branchJill:
    if ep9_jm_sad or ep2_stole_money:
        scene ep10_mc_room1 with wipeleft
    else:
        scene ep10_mc_roomj0 with wipeleft
        jm "This is a fucking disaster, Tommy!"
        scene ep10_mc_roomj1 with dissolve
        mc "Wait for me in my room. I have to deal with this."
        scene ep10_mc_room1 with dissolve
else:
    scene ep10_mc_room1b with wipeleft
play music "music/ep3/black_box.mp3"
mc "Hey, what's going on?"
scene ep10_mc_room2 with dissolve
le "Uh...? How did you even miss it? These fucking posters are everywhere on campus!"
mc "Yeah, I saw them."
scene ep10_mc_room3 with dissolve
le "And you're not freaking out?"
scene ep10_mc_room7 with dissolve
if not branchMayaJosy:
    tm "I knew [name] would be cool with it. Those are just some dick pics. Who cares?"
else:
    tm "Those are just some dick pics. Who cares?"
scene ep10_mc_room5 with dissolve
jm "They're {b}our{/b} dick pics and they aren't flattering. My cock isn't even showing... People are asking questions."
jm "All they did to you is insinuate you have STDs."
scene ep10_mc_room14 with dissolve
jac "I've gotten cross-dresser comments all day from my classmates. It's getting annoying."
scene ep10_mc_room4 with dissolve
le "And I don't fuck anything with a hole. That's not true!"
le "Sometimes it's a blowjob!"
scene ep10_mc_room15 with dissolve
rs "These are obviously lies and slander someone made up to make us look bad. But we have ourselves to blame for hanging those pictures on our walls."
scene ep10_mc_room4 with dissolve
le "I blame Tommy. That wall was his idea!"
scene ep10_mc_room7 with dissolve
tm "Shut the fuck up! I didn't hear any complaints when I put those pictures up and you've had a long time to say something."
scene ep10_mc_room16 with dissolve
de "Girls know that dicks shrink when it's cold, right? That picture removed at least 2 inches."
scene ep10_mc_room18 with dissolve
jm "I don't think that argument holds when you're running next to [name]."
scene ep10_mc_room17 with dissolve
de "Fuck! Why the fuck did you have to put those pictures on the wall, Tommy!?"
scene ep10_mc_room8 with dissolve
tm "Don't fucking blame me for this. If you should blame someone, blame Mr. Party Planner, who let preps roam the mansion freely at the party."
tm "I bet they are involved in this somehow."
scene ep10_mc_room11 with dissolve
rs "You let preps in?"
scene ep10_mc_room10 with dissolve
if ep9_prep_truce:

    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-DIKs)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

    menu:
        "Those preps are cool [m_c1][mod_choices[0]]":
            $ RPdiks -= 1
            mc "Yeah, I did. But the three I let in are kinda cool."
            mc "I talked to them at a dorm party and we agreed to settle our differences back then. So, I thought, what the hell?"
            scene ep10_mc_room9 with dissolve
            tm "Kinda cool? What the fuck are you even saying?"
            scene ep10_mc_room6 with dissolve
            le "Preps aren't cool, [name]. They suck."
        "I didn't think this would happen":
            mc "Yeah, but I didn't think this would happen. And we don't know for sure if it was them, to begin with."
            scene ep10_mc_room6 with dissolve
            le "You can't let preps into our mansion, [name]. That's just wrong."
    scene ep10_mc_room13 with dissolve
    jac "Yeah. You shouldn't have done that."
    scene ep10_mc_room19 with dissolve
    $ RPdiks -= 1
    $ new_bio("You", "I upset the DIKs when they found out that I had let preps into the mansion during our Halloween party.")
    if minigames:
        $ specialMessage = "All DIKs' happiness decreased!"
        $ pp_happiness_level[7] = max(pp_happiness_level[7]-10,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-10,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-10,0)
        $ pp_happiness_level[1] = max(pp_happiness_level[1]-10,0)
        $ pp_update_happiness_icons()
        $ mphone_pp_history_list.append("• Letting preps into the party decreased Jacob's happiness by {color=ff0000}10%{/color}.")
        $ mphone_pp_history_list.append("• Letting preps into the party decreased Leon's happiness by {color=ff0000}10%{/color}.")
        $ mphone_pp_history_list.append("• Letting preps into the party decreased Rusty's happiness by {color=ff0000}10%{/color}.")
        $ mphone_pp_history_list.append("• Letting preps into the party decreased Tommy's happiness by {color=ff0000}10%{/color}.")
        show screen specialmsg
else:
    if affinity == "DIK":
        mc "Fuck no. Those idiots snuck into our party and I forced them to leave. I threw them out the moment I spotted them. Just ask John Boy, Nick or Jacob."
    else:
        mc "I didn't let them in. They snuck into our party and I made sure they left."
    scene ep10_mc_room12 with dissolve
    ni "It's true. I saw him telling them to leave when they first showed up at our door."
    scene ep10_mc_room19 with dissolve
mc "Everybody, take a deep breath."
if minigames:
    hide screen specialmsg
mc "We can stand here and be angry at each other all night, but that won't accomplish anything."
scene ep10_mc_room2 with dissolve
mc "Those pictures are already out there, and we can't change that."
mc "If we wanna do something about them, let's not point fingers at ourselves. We need to figure out who's doing this and why."
scene ep10_mc_room19 with dissolve
mc "I talked to Derek about this earlier today and one thing we can start by doing is ask people who came to our Halloween party about it."
mc "We feel it's too big of a coincidence to have these pictures out there the days after our big party. Don't you?"
scene ep10_mc_room14 with dissolve
jac "Shit... That's a lot of people we have to ask."
scene ep10_mc_room15 with dissolve
rs "It's a good idea. Text people who you know were at the party and ask around. Let's split the guest list so the task gets easier."
scene ep10_mc_room20 with dissolve
tm "There's no way anyone would confess when we ask."
tm "And the guest list isn't even complete. What about the uninvited guests and friends of friends? Some didn't even pay, yet they showed up."
scene ep10_mc_room15 with dissolve
rs "We'll help out adding as many names as we can to it. And even if they don't confess, maybe it will give us something."
scene ep10_mc_room16 with dissolve
de "Don't forget to tear down any posters you find."
scene ep10_mc_room21 with dissolve
le "And to keep your eyes open. Maybe we can catch whoever is putting them up that way."
scene ep10_mc_room19 with dissolve
if not ep8_share_room and not (branchJill and not (ep9_jm_sad or ep2_stole_money)):
    stop music fadeout 3
mc "Great. This already sounds a lot better than blaming each other."
if ep8_share_room:
    mc "Are we done here? It's been a long day. I'm gonna head to my room."

if branchJill and not (ep9_jm_sad or ep2_stole_money):
    scene ep10_mc_roomj6 with dissolve
    mc "Ok... I dealt with it."
    stop music fadeout 15
    scene ep10_mc_roomj7 with dissolve
    ji "How did it go?"
    scene ep10_mc_roomj8 with dissolve
    mc "They're feeling pretty upset about the posters."
    scene ep10_mc_roomj7 with dissolve
    ji "That's understandable."
    scene ep10_mc_roomj8 with dissolve
    mc "We're going to ask around and hope for the best. I guess that's all we can do about it."
    scene ep10_mc_roomj2 with dissolve
    $ renpy.pause()
    scene ep10_mc_roomj3 with dissolve
    mc "I'm happy you're here."
    scene ep10_mc_roomj4 with dissolve
    ji "Things will be fine, [name]."
    scene ep10_mc_roomj5 with dissolve
    $ renpy.pause()
elif ep8_share_room:
    scene ep10_mc_room23 with dissolve
    $ renpy.pause()
    stop music fadeout 15
    scene ep10_mc_room24 with dissolve
    mc "Hello?"
    scene ep10_mc_room26 with dissolve
    de "It's me, [mc_de]."
    scene ep10_mc_room27 with dissolve
    mc "What's up?"
    scene ep10_mc_room26 with dissolve
    de "Can I crash on your couch? I'm feeling iffy about my room..."
    scene ep10_mc_room27 with dissolve
    if affinity == "DIK":
        mc "Keep your dick in your underwear and it's fine."
    else:
        mc "Of course, bro. Whatever you need."
    scene ep10_mc_room26 with dissolve
    de "Thanks."
    scene ep10_mc_room27 with dissolve
    mc "It's been a tough couple of days for you."
    scene ep10_mc_room26 with dissolve
    de "Yeah, but it feels good knowing I have a true friend."
    scene ep10_mc_room27 with dissolve
    mc "Same, buddy."
    scene ep10_mc_room28 with dissolve
    $ renpy.pause()
    $ new_bio("Derek", "I let him crash on my couch because he felt weird about sleeping in his room.")

label ep10_yb_label:
scene black with fade
$ renpy.pause(2)
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
play music "music/ep3/sunny_acoustic_rock.mp3"
scene ep10_yb1 with dissolve
$ renpy.pause()
scene ep10_yb2 with dissolve
pho "And you're done. Fill in your name and quote for the yearbook before you leave."
scene ep10_yb3 with dissolve
mc "My quote?"
show ep10_yb4
if not persistent.ep10_cardzo6:
    show screen ep10_render_screen("zo6")
with dissolve
pho "Jeez. Didn't you do it back in high school?"
pho "Next!"
show ep10_yb5
hide screen ep10_render_screen
with dissolve
$ renpy.pause()
scene ep10_yb7
show screen yearbook_quote_screen
mc "(Hm... My quote? I need to think about this.)"
label getQuote_label:
$ renpy.block_rollback()
$ ep10_quote = ""
$ tmpStr = ""
$ renpy.block_rollback()
$ tmpInt = 9 * persistent.scale_factor
menu:
    "{size=-5}All our dreams can come true! Except...{/size}":
        $ renpy.block_rollback()
        label getQuote1_label:
        $ ep10_quote = "All our dreams can come true! Except getting a decent meal in the cafeteria."
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Change your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote1_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote1_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote1_label
    "{size=-[tmpInt]}Thanks for the memories! But I wish I could forget...{/size}":
        $ renpy.block_rollback()
        label getQuote2_label:
        $ ep10_quote = "Thanks for the memories! But I wish I could forget what I learned in Gender Studies."
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Change your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote2_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote2_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote2_label
    "The best thing about college was...":
        $ renpy.block_rollback()
        label getQuote3_label:
        $ ep10_quote = "The best thing about college was the time between the classes."
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Change your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote3_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote3_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote3_label
    "Note to future me:":
        $ renpy.block_rollback()
        label getQuote4_label:
        $ ep10_quote = "Note to future me: Don't tell your kids about Hell Week."
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Change your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote4_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote4_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote4_label
    "If anyone reads my quote,...":
        $ renpy.block_rollback()
        label getQuote5_label:
        $ ep10_quote = "If anyone reads my quote, plan your quote in advance."
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Change your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote5_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote5_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote5_label
    "...":
        $ renpy.block_rollback()
        label getQuote6_label:
        $ ep10_quote = ""
        show screen yearbook_quote_input_screen
        $ specialMessage = "{size=-%d}Type your quote as you wish.{/size}" % (5 * persistent.scale_factor)
        show screen specialmsg
        $ renpy.pause(4)
        hide screen specialmsg
        pause
        hide screen yearbook_quote_input_screen
        $ ep10_quote = ep10_quote.strip()
        if ep10_quote == "":
            $ specialMessage = "{size=-%d}Yearbook quote cannot be empty.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote6_label
        if checkYbSpace(ep10_quote):
            $ specialMessage = "{size=-%d}Keep words shorter than 20 characters each.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote6_label
        elif checkProfanity(ep10_quote):
            $ specialMessage = "{size=-%d}Keep it clean. No profanity.{/size}" % (5 * persistent.scale_factor)
            show screen specialmsg
            $ renpy.pause(2)
            hide screen specialmsg
            jump getQuote6_label
menu:
    "Change quote":
        $ renpy.block_rollback()
        jump getQuote_label
    "Done":
        $ renpy.block_rollback()
        scene ep10_yb6
        hide screen yearbook_quote_screen
        with dissolve
        mc "(Perfect.)"

scene ep10_yb8 with dissolve
my "I have a feeling I had my eyes closed in the picture. I'm gonna look like I'm drunk..."
scene ep10_yb9 with dissolve
cam "I don't understand why he didn't show us the picture before moving on. It's kinda lazy."
scene ep10_yb10 with dissolve
de "And why do they need quotes for the yearbook? Are we gonna have to be funny every year?"
scene ep10_yb11 with dissolve
my "Did you write something funny?"
scene ep10_yb10 with dissolve
de "What else would you write?"
scene ep10_yb11 with dissolve
my "Something inspirational or a nice memory, perhaps?"
scene ep10_yb10 with dissolve
de "Nah, that's not for me."
scene ep10_yb12 with dissolve
be "Give it back!"
dw "Haha, what are you gonna do about it shorty?"
scene ep10_yb13 with dissolve
an "Shorty? He's taller than you."
scene ep10_yb15 with dissolve
ash "Ant... Don't be a jerk. Give it back to him."
scene ep10_yb14 with dissolve
an "What? It's a joke."
$ guideSuggestedPage = 105
if branchSage:
    scene ep10_yb16 with dissolve
    sa "Hey, guys. Classes, huh?"
    scene ep10_yb17 with dissolve
    mc "Yeah, math. We just had our picture taken for the yearbook."
    scene ep10_yb18 with dissolve
    sa "Fuck! Was that today? I'm such a scatterbrain."
    scene ep10_yb19 with dissolve
    mc "Busy schedule?"
    scene ep10_yb20 with dissolve
    sa "Tell me about it. And on the one day I don't put on makeup, it's today."
    scene ep10_yb21 with dissolve
    menu:
        "You look cute":
            mc "I think you look cute and casual. There's nothing wrong with that."
            scene ep10_yb22 with dissolve
            sa "That's a sweet lie."
        "You got time to do it":
            mc "You got time to do it. Run back home and slap some on."
            scene ep10_yb22 with dissolve
            sa "Slap some on? You have no clue how girls do makeup, do you?"

    scene ep10_yb20 with dissolve
    sa "It's my last yearbook picture, dude. I wanted it to look good, but I guess it won't."
    scene ep10_yb21 with dissolve
    mc "Mine probably won't look good either. It's not a big deal."
    scene ep10_yb23 with dissolve
    sa "I certainly hope it's more flattering than that picture of you."
    play sound "sound_effects/season3/paper_ball.mp3"
    scene ep10_yb24 with dissolve
    if affinity == "DIK":
        mc "Yeah. It should be, the photographer had to tell me to put my pants back on."
    else:
        mc "*{i}Sigh{/i}* One would hope."
    scene ep10_yb22 with dissolve
    sa "I gotta go. Can I stay at your place tonight?"
    scene ep10_yb21 with dissolve
    mc "Works for me."
    scene ep10_yb25 with dissolve
    sa "*{i}Smack{/i}* Have a good day."

label ep10_math_label:
scene ep10_math1 with wipeleft
de "Ashley? Do you have a minute?"
scene ep10_math2 with dissolve
ash "What do you want, Derek?"
scene ep10_math3 with dissolve
de "I need to talk to you about something important."
scene ep10_math4 with dissolve
ash "Ant's over there..."
scene ep10_math3 with dissolve
de "Another time, then. Whenever you're free. It's important."
scene ep10_math5 with dissolve
ph "Good afternoon, students. Please be seated."
scene ep10_math6 with dissolve
ph "The results from the midterms have been published. You can find them online on your student home page."
scene ep10_math8 with dissolve
ph "I'd tell you to wait until after class to view them, but I see that I have made the mistake of announcing it prematurely."
ph "Very well, take a minute and check them."
scene ep10_math11 with dissolve
dw "What the fuck!? This is horse shit!"
scene ep10_math12 with dissolve
an "Hey, you passed. That's great!"
ash "Yeah. What about you?"
scene ep10_math13 with dissolve
an "I'm scared to look."
scene ep10_math14 with dissolve
an "I passed!"
dw "What!? No fucking way!"
scene ep10_math15 with dissolve
dw "How could you do this to me?"
scene ep10_math9 with dissolve
my "Yes! I passed. What about you?"
scene ep10_math10 with dissolve
js "It's not what I had hoped for, but it's good, considering how hard that test was."
scene ep10_math16 with dissolve
mc "Aren't you looking?"
scene ep10_math17 with dissolve
de "I already know I passed."
scene ep10_math16 with dissolve
mc "Look at the confidence on you."
scene ep10_math17 with dissolve
de "What about you?"
if ep8_midterms_cheated == "DIK":
    scene ep10_math16 with dissolve
    mc "Yeah... I passed."
    scene ep10_math18 with dissolve
    mc "(And now I feel ashamed about it... Bella was right.)"
    scene ep10_math19 with dissolve
    mc "(And I guess my punishment is the guilt and knowing that Philip has his eyes on me...)"
    $ new_bio("Philip", "In math class, I could feel that I was on Philip's radar after cheating on the midterms.")
else:
    scene ep10_math16 with dissolve
    mc "I passed."
    scene ep10_math17 with dissolve
    de "Nice. But it doesn't matter; they're not our final grades."
    scene ep10_math16 with dissolve
    mc "They're a part of it."

scene ep10_math6 with dissolve
ph "Ok, the minute is up. I don't want to see anyone fiddling with their phones now."
ph "You can discuss the test after class."
scene ep10_math7 with dissolve
ph "If you felt that the first half of the course went by fast, you will be surprised about the second half."
ph "You'll take the finals before winter break and, as I'm sure all other teachers also say, it will be here in no time."
scene ep10_math6 with dissolve
ph "We have plenty left of the curriculum to cover before that, so let's begin."
ph "Thanks to Cathy, I believe you are somewhat familiar with this next chapter. We will dive head first into Lagrange interpolation."
if minigames:
    stop music fadeout 3
ph "But do not be frightened by it. With some studying, you will soon understand it well."
if minigames:
    scene ep10_math17b with dissolve
    hide screen new_phone_screen
    if minigames and (tutorials or not persistent.math_tutorial):
        $ specialMessage = "{size=-%d}You can turn on color blindness support in Settings.{/size}" %  (5* persistent.scale_factor)
        if not persistent.colorblind:
            show screen specialmsglong
        menu:
            "Watch tutorial":
                hide screen specialmsglong
                $ renpy.block_rollback()
                $ math_tut_ep10()
                $ math_jump_label = "after_math_tut_ep10_label"
                $ persistent.math_tutorial = True
                play music "music/ep3/sing_along_with_jim.mp3"
                show screen math_tut_screen
                $ renpy.pause()
            "Skip tutorial":
                hide screen specialmsglong
                $ renpy.block_rollback()
                play music "music/ep3/sing_along_with_jim.mp3"
                jump after_math_tut_ep10_label
    else:
        play music "music/ep3/sing_along_with_jim.mp3"
    label after_math_tut_ep10_label:
    $ renpy.block_rollback()
    $ qM = quick_menu
    $ quick_menu = 0
    $ math_jump_label = "after_math_setup_ep10_label"
    $ _game_menu_screen = None
    jump math_setup_ep10_label
    label after_math_setup_ep10_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_ep10_label"

    show screen math_screen
    $ renpy.pause()

    label after_math_ep10_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_result_ep10_label"
    $ quick_menu = qM
    $ _game_menu_screen = "save"
    show screen new_phone_screen
    hide screen math_screen
    hide screen math_tool_tip_screen
    show screen math_result_screen
    $ renpy.pause()
    label after_math_result_ep10_label:
    $ renpy.block_rollback()
    hide screen math_result_screen
    stop music fadeout 3

scene ep10_math20 with fade
js "I didn't understand this the first time...and it doesn't make much more sense the second time."
if minigames:
    play music "music/ep3/sunny_acoustic_rock.mp3"
scene ep10_math21 with dissolve
my "*{i}Sigh{/i}* When will I ever use this in my line of work?"
scene ep10_math22 with dissolve
ly "Yup. I'm with you, sister. I'm thankful this is the only math credit I need."
scene ep10_math21 with dissolve
my "Sister? So, you know about it?"
scene ep10_math27 with dissolve
ly "Yeah, I heard that you're returning to the HOTs."
scene ep10_math23 with dissolve
my "I've been meaning to tell everyone."
scene ep10_math27 with dissolve
ly "Don't bother. Everyone already knows. Sage wants us to throw a party for you."
scene ep10_math24 with dissolve
my "Ugh... Yeah, she mentioned that. I told her it wasn't necessary."
scene ep10_math27 with dissolve
ly "Think of it as any other party. She asked me to find out what you wanna do but in secret."
ly "And I'm not one for beating around the bush, so I figured I'd just ask you. What do you wanna do?"
scene ep10_math25 with dissolve
js "Lily... You're not meant to ruin the surprise."
scene ep10_math29 with dissolve
ly "What surprise? She already knows about the party."
ly "I think it's better if we come up with something fun instead of pretending it's not happening or guessing what she wants."
scene ep10_math23 with dissolve
my "I don't know what I want to do. I'm up for everything, I guess."
scene ep10_math28 with dissolve
ly "You're not up for everything."
scene ep10_math24 with dissolve
my "Maybe not everything, but I don't have any demands."
scene ep10_math28 with dissolve
ly "Let's simplify things... Do you want me to invite guys to the party or not?"
scene ep10_math25 with dissolve
js "Didn't Sage want a HOTs-only party?"
scene ep10_math29 with dissolve
ly "She asked me to find out what Maya wanted. And, Josy, let's be real..."
ly "Girls-only parties are no fun."
scene ep10_math23 with dissolve
my "I don't mind if there are guys at the party."
scene ep10_math27 with dissolve
ly "See! Maya wants guys to come. It's a good thing I asked her."
scene ep10_math26 with dissolve
js "Haha, I guess it is."
scene ep10_math27 with dissolve
ly "Now, I have to check with the DIKs and we got ourselves a party. And that's how you do it."

scene ep10_math7 with dissolve
if not ep10_rolling:
    stop music fadeout 3
ph "That's it for today. Have a nice end to your day, everyone. Class dismissed."

if ep10_rolling:
    scene ep10_math30 with dissolve
    ly "Did you pass the test?"
    scene ep10_math31 with dissolve
    mc "I did. You?"
    scene ep10_math32 with dissolve
    ly "Sure did."
    scene ep10_math31 with dissolve
    mc "No way."
    scene ep10_math33 with dissolve
    ly "What? You insult me. Don't you think I'm smart?"
    scene ep10_math31 with dissolve
    if affinity == "DIK":
        mc "Now I do."
    else:
        mc "I don't know what I was thinking when I said that. I'm happy you passed."
        mc "And now I know you're smart."
    scene ep10_math32 with dissolve
    ly "Haha! You still have things to learn about me."
    scene ep10_math33 with dissolve
    ly "But it seems like everyone on campus has learned about you. Wink wink..."
    scene ep10_math31 with dissolve
    mc "The posters? Yeah, that shit is embarrassing. They keep popping up..."
    scene ep10_math33 with dissolve
    ly "You know that you have to own it, right? That's the only way to do it."
    scene ep10_math31 with dissolve
    mc "I've been trying to ignore it."
    scene ep10_math32 with dissolve
    ly "It's not bad to have everyone know you're hung like a horse."
    scene ep10_math31 with dissolve
    mc "My brothers don't look at it that way. Some of them feel embarrassed."
    scene ep10_math33 with dissolve
    ly "Tough shit. Then they shouldn't have made a fucking memorabilia wall full of those pictures."
    scene ep10_math32 with dissolve
    ly "But I'm thrilled they did. Even though people laugh and stare, there's no such thing as bad news."
    stop music fadeout 5
    scene ep10_math34 with dissolve
    ly "When they figure out it's you, guys will be jealous of you, and you bet your ass that girls will be jealous of me."

label ep10_zoey_label:
play music "music/ep8/licensed_music/track78.mp3"
scene ep10_zoey1 with dissolve
zmom "And if you leave the register, make sure you click log out."
scene ep10_zoey2 with dissolve
zo "Log out when I stretch my legs - got it."
zo "I don't know how you do this every day. Is it always this slow?"
scene ep10_zoey3 with dissolve
zmom "This time of day, it is. It's when we get time to restock the shelves and do other tasks such as updating prices and putting up sales signs."
zmom "Speaking of which, I have some work to do with just that. Will you be ok here on your own?"
scene ep10_zoey2 with dissolve
zo "Yeah, I'll shout if I need you."
zo "And, oh! Can I draw while I wait for customers to show?"
scene ep10_zoey3 with dissolve
zmom "Hm... Sorry, sweetheart. But it doesn't look professional if you do that."
hide screen new_phone_screen
scene ep10_zoey4 with dissolve
zo "(Phone it is... Like everyone else at this place... Because that looks {b}way{/b} more professional.)"
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Jacob","Sup! The Halloween pics are almost ready. I'll send you a link for them later.",True])
$ text_message_screen_list.append(["Zoey","Dope! Can't wait. Loved the party, by the way.",False])
$ text_message_screen_list.append(["Jacob","Awesome! It was so cool that you came. You've got such a great vibe. After Halloween, you got yourself a standing invite to all our parties. LOL",True])
$ text_message_screen_list.append(["Jacob","Or if you wanna hang, you can drop by any time.",True])
$ text_message_screen_list.append(["Zoey","Cool.",False])
play sound "sound_effects/interlude/zoey_message.mp3"
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

scene ep10_zoey5 with dissolve
$ tmpInt = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Zoey","What up?",False])
$ text_message_screen_list.append(["Jonah","Not much. Stopped by Bret to check up on him. You?",True])
$ text_message_screen_list.append(["Zoey","Say hi from me. I'm working with Mom at a makeup store/beauty salon.",False])
$ text_message_screen_list.append(["Jonah","You traded a tattoo parlor for a beauty salon? Haha!",True])
play sound "sound_effects/interlude/zoey_message.mp3"
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ tmpInt = 0
$ text_message_screen_list = []
show screen text_message_screen
$ text_message_screen_list.append(["Zoey","I know. I have to wear casual clothes to fit in here, too. And I'm not allowed to sketch while I'm at the register. Shit blows.",False])
$ text_message_screen_list.append(["Jonah","Yeah, dressing like a girl for once must suck. mphone_emoji_laugh",True])
$ text_message_screen_list.append(["Zoey","Yeah, you'd fit in here way better than I do. Slap on a dress and come join me. I'm happy to be back home, but the days feel different.",False])
$ text_message_screen_list.append(["Jonah","LOL! And what about [name]?",True])
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ tmpInt = 0
$ text_message_screen_list = []
if ep9_mad_at_zoey:
    scene ep10_zoey6 with dissolve
    $ text_message_screen_list.append(["Zoey","It's tough. He's not as happy to see me as I am to see him. I'm not sure if he will forgive me.",False])
    $ text_message_screen_list.append(["Jonah","You're awesome, and he knows it. If he doesn't want you in his life anymore, it's his loss.",True])
    $ text_message_screen_list.append(["Zoey","It's my loss, too. I can't believe I might lose my best friend like that.",False])
    $ text_message_screen_list.append(["Jonah","I don't know what to tell you. I wish I had some words of wisdom for you, but I'm blank.",True])
    play sound "sound_effects/interlude/zoey_message.mp3"
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
else:
    scene ep10_zoey7 with dissolve
    $ text_message_screen_list.append(["Zoey","It went better than I thought it would. We were both quite emotional about seeing each other again, but I think that's a good sign.",False])
    $ text_message_screen_list.append(["Jonah","It sounds like it. Hell, I'd be emotional too if I reunited with a lifelong friend.",True])
    $ text_message_screen_list.append(["Zoey","Seeing him again made me realize how much I missed him. I've been thinking about him constantly since I got back home...",False])
    play sound "sound_effects/interlude/zoey_message.mp3"
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen

$ tmpInt = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Jonah","How was the party?",True])
$ text_message_screen_list.append(["Zoey","It was great. He's got a lot of fun friends, and they were very interested in me. Some more than others.",False])
$ text_message_screen_list.append(["Jonah","Any cute guys?",True])
$ text_message_screen_list.append(["Zoey","You sound like such a girl.",False])
scene ep10_zoey5 with dissolve
play sound "sound_effects/interlude/zoey_message.mp3"
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen

$ tmpInt = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Jonah","That wasn't a no.",True])
$ text_message_screen_list.append(["Zoey","Whatever.",False])
$ text_message_screen_list.append(["Jonah","Give it time. Heading out. Bret says hi!",True])
$ text_message_screen_list.append(["Zoey","Later, chrome dome.",False])
scene ep10_zoey8 with dissolve
play sound "sound_effects/interlude/zoey_message.mp3"
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
stop music fadeout 3
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
show screen new_phone_screen

label ep10_gym_label:
$ guideSuggestedPage = 117
play music "music/ep5/licensed_music/track11.mp3"
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym1 with hpunch
$ renpy.pause()
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym2 with hpunch
$ renpy.pause()
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym3 with hpunch
$ renpy.pause()
scene ep10_gym4 with dissolve
mc "(Come on, [name]! Don't get gassed out yet.)"
if ep8_nora_number:
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep10_gym1 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep10_gym2 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_kick.mp3"
    scene ep10_gym3 with hpunch
    $ renpy.pause()
    scene ep10_gym5 with dissolve
    no "What a shame. Here I am, done with my workout, and I run into you."
    scene ep10_gym6 with dissolve
    mc "Oh, Nora! Hi!"
    if not branchAlone:
        scene ep10_gym7 with dissolve
        no "I've been waiting for your phone call. Are you playing hard to get or what?"
        scene ep10_gym6 with dissolve
        mc "About that... I was gonna call you, but since we saw each other last time, I've gotten serious with someone."
        scene ep10_gym8 with dissolve
        no "Really?"
        scene ep10_gym9 with dissolve
        mc "Yeah. And as my interest in you wasn't a friendship on my end, I didn't pick up the phone. Sorry."
        scene ep10_gym8 with dissolve
        no "No harm done, [name]. At least you're telling me now."
        no "Good luck with the punching bag."
        scene ep10_gym9 with dissolve
        mc "Thanks! I'll see you around."
        scene ep10_gym13 with dissolve
        mc "(That sucked, but it had to be done.)"
    else:
        mc "If you have some stretching left, I'd gladly help out."
        scene ep10_gym7 with dissolve
        no "Haha, I bet you would."
        scene ep10_gym6 with dissolve
        mc "What have you been up to?"
        scene ep10_gym7 with dissolve
        no "Not much. I recently came off an antibiotic treatment. My inner ear has been acting up."
        no "It feels good to be back at the gym."
        scene ep10_gym6 with dissolve
        mc "That sucks. Are you feeling ok?"
        scene ep10_gym8 with dissolve
        no "I'm much better, thanks. I've been prone to ear infections all my life. It's annoying, but nothing to worry about."
        no "How about you?"
        scene ep10_gym6 with dissolve
        mc "I'm healthy and full of energy."
        scene ep10_gym10 with dissolve
        no "That's good. I should be off now, but..."
        no "Since you're here, may I be bold enough to ask you for a date?"
        scene ep10_gym11 with dissolve
        mc "Oh, wow! A date?"
        scene ep10_gym10 with dissolve
        no "I take it you're still interested. Are you?"
        scene ep10_gym11 with dissolve
        
        if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Nora date)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
        
        menu:
            "Accept  [m_c1][mod_choices[0]]":
                $ ep10_dating_nora = True
                mc "You know it. Tell me when and where."
                scene ep10_gym10 with dissolve
                no "Would Saturday be ok? I was thinking evening drinks at my place. What do you say?"
                scene ep10_gym11 with dissolve
                if ep10_date_nicole:
                    mc "(Fuck... I'm supposed to meet Nicole on Saturday...)"
                    menu:
                        "Mod: Date both":
                            pass
                        "Date Nora instead":
                            $ ep10_cancel_date_nicole = True
                            mc "(But I'm more into Nora... It sucks, but I'll have to cancel on Nicole.)"
                            mc "I'll have to move some things around, but I'm up for it."
                            $ new_bio("Envy", "I had to cancel my date with Nicole because I wanted to date Nora.")
                        "Suggest another time":
                            mc "Oh, that's not good for me. How about Sunday instead?"
                            scene ep10_gym10 with dissolve
                            no "Sadly, I'm busy."
                            scene ep10_gym11 with dissolve
                            mc "Damn..."
                            menu:
                                "Tell Nora you can't":
                                    $ ep10_dating_nora = False
                                    mc "That's a shame. I can't cancel my plans."
                                    scene ep10_gym10 with dissolve
                                    no "That's ok. It was a spontaneous invite. There will be another time for it. Now I know that you're interested."
                                    no "Until next time."
                                    scene ep10_gym13 with dissolve
                                    mc "See you, Nora."
                                "Cancel on Nicole":
                                    $ ep10_cancel_date_nicole = True
                                    mc "(I'm more into Nora than Nicole... It sucks, but I'll have to cancel on Nicole.)"
                                    mc "You know what? I'll have to move some things around, but I'm up for it."
                                    $ new_bio("Envy", "I had to cancel my date with Nicole because I wanted to date Nora.")
                    if ep10_dating_nora:
                        scene ep10_gym10 with dissolve
                        no "I'll send you the directions."
                        no "Does 8 p.m. work for you?"
                        scene ep10_gym11 with dissolve
                        mc "It's a date."
                        scene ep10_gym13 with dissolve
                        mc "(She asked me out... That's hot.)"
                else:
                    mc "I'm free as a bird."
                    scene ep10_gym10 with dissolve
                    no "I'll send you the directions."
                    no "Does 8 p.m. work for you?"
                    scene ep10_gym11 with dissolve
                    mc "It's a date."
                    scene ep10_gym13 with dissolve
                    mc "(She asked me out... That's hot.)"
            "Reject Nora":
                $ ep10_dating_nora = False
                mc "I gotta be honest with you. I was interested back when I asked for your number..."
                mc "...but my gut feeling is telling me no."
                scene ep10_gym12 with dissolve
                no "It is?"
                scene ep10_gym9 with dissolve
                mc "Yeah, I'm sorry. Things happen, you know?"
                scene ep10_gym8 with dissolve
                no "Perhaps I should have been more eager."
                scene ep10_gym9 with dissolve
                mc "It's not you, Nora. It's me."
                scene ep10_gym8 with dissolve
                no "That's the oldest lie in the book. But I understand. A no is a no."
                scene ep10_gym9 with dissolve
                mc "I'll see you around, Nora."
                scene ep10_gym8 with dissolve
                no "Sure."
                scene ep10_gym13 with dissolve
                mc "(Ugh... That didn't feel too good when she put herself out there and asked me out...)"
                mc "(But I had to be honest with myself. I don't feel it anymore.)"

play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym1 with hpunch
$ renpy.pause()
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym2 with hpunch
$ renpy.pause()
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym3 with hpunch
$ renpy.pause()
scene ep10_gym14 with dissolve
dwy "You wrapped your hands, huh?"
scene ep10_gym15 with dissolve
mc "Hey! It's you. Yeah, thanks for that."
mc "I spent some time reading up on exercises and whatnot and realized I was stupid."
scene ep10_gym16 with dissolve
dwy "It's not stupid being a rookie."
dwy "Listening to advice from someone with experience tells me you're smart."
dwy "Some dudes around here get all pissy and defensive when you try to teach them how to do something."
scene ep10_gym18 with dissolve
mc "I'm [name], by the way."
scene ep10_gym19 with dissolve
dwy "Dwyane."
scene ep10_gym16 with dissolve
dwy "I take it you're not in a club."
scene ep10_gym15 with dissolve
mc "A fight club?"
scene ep10_gym16 with dissolve
dwy "Yeah."
scene ep10_gym15 with dissolve
mc "No, I could never afford that."
scene ep10_gym16 with dissolve
dwy "Missing out on the basics like that, you oughta think about joining one. There's one here."
scene ep10_gym15 with dissolve
mc "I'm fighting for self-defense and to stay in shape, but that's it."
mc "What about you?"
scene ep10_gym16 with dissolve
dwy "I used to scrap, but it was no way to make money. Not the way I was going at it."
scene ep10_gym17 with dissolve
dwy "So, I shaped up and became a PT."
scene ep10_gym15 with dissolve
mc "A personal trainer?"
scene ep10_gym16 with dissolve
dwy "Mhm."
dwy "These days, I'm like you. But I also spar with the boys so I don't lose it."
scene ep10_gym15 with dissolve
mc "So, you're not in the club either?"
scene ep10_gym16 with dissolve
dwy "I hang around but ain't got the time to stay competitive."
dwy "You gotta be devoted to keep up with the best of them, you know what I'm saying?"
scene ep10_gym15 with dissolve
mc "Not really."
scene ep10_gym16 with dissolve
dwy "Eh."
dwy "If you ever need coaching, holler at me."
scene ep10_gym15 with dissolve
mc "Thanks, but I can't afford a PT. This gym membership is what I could spare."
stop music fadeout 3
scene ep10_gym20 with dissolve
$ renpy.pause()
scene ep10_gym16 with dissolve
dwy "Come with."
play music "music/ep10/licensed_music/stand_and_fight.mp3"
scene ep10_gym21 with dissolve
mc "Wow! You have a ring in here."
scene ep10_gym22 with dissolve
dwy "Told you you're missing out."
scene ep10_gym23 with dissolve
dwy "Start punching the bag."
scene ep10_gym24 with dissolve
mc "What for?"
scene ep10_gym23 with dissolve
dwy "I've been in your spot. All broke and shit."
dwy "I can always use someone else to train with, but if you're not up to speed, I ain't gonna bother."
scene ep10_gym24_neutral with dissolve
dwy "Aight. Show me your speed. Pummel that bag."
mc "Speed? Don't you train that on a speed bag?"
dwy "A heavy bag works better for you. You're fighting at chest height, aren't you?"
dwy "The heavy bag is gonna let you pack on muscle. You look like you need some."
scene ep10_gym24 with dissolve
mc "Are you calling me scrawny?"
scene ep10_gym23 with dissolve
dwy "I remember that dude you tried to fight. His left asscheek weighs more than you."
dwy "You're not gonna stand a chance without packing power in that fist."
scene ep10_gym24_neutral with dissolve
$ tutorial_ongoing = False
if minigames and (tutorials or not persistent.brawler_tutorial):
    menu:
        "Watch tutorial":
            $ tutorial_ongoing = True
            $ persistent.brawler_tutorial = True
        "Skip tutorial":
            $ tutorial_ongoing = False

if minigames and tutorial_ongoing:
    hide screen new_phone_screen
    $ bn_mc_stamina = 4
    $ bn_combo_idx = 0
    $ bn_arrow_input_tut = 3
    $ bn_arrow_selection = ["MISS","COMBO","RAGE","FIST"]
    $ renpy.block_rollback()
    $ bn_tut_msg = 1
    $ jumpLabel = "ep10_dwy_tut1_label"
    show screen brawler_dwyane_tutorial_screen
    show screen brawler_arrow_choice_screen_tutorial
    pause
    label ep10_dwy_tut1_label:

    $ bn_tut_msg = 2
    $ bn_arrow_combination = ["up","up","down","right","left"]
    $ jumpLabel = "ep10_dwy_tut2_label"
    show screen brawler_arrow_combo_screen_tutorial
    pause
    label ep10_dwy_tut2_label:
    $ renpy.block_rollback()
    $ bn_tut_msg = 0
else:
    $ renpy.pause()

play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym27 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
$ renpy.pause(0.1)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym27 with hpunch
$ renpy.pause(0.1)

scene ep10_gym24_neutral with dissolve
mc "*{i}Phew{/i}*"
dwy "That's 'nuff. Switch to kicks."
mc "Can I take a breather?"
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 3
dwy "Nah. I wanna see your stamina. Powerful kicks, 30 seconds. Go!"
if minigames and tutorial_ongoing:
    $ bn_arrow_input_tut = 2
    $ bn_arrow_selection = ["BAD","HIT","COMBO","THUD"]
    $ renpy.block_rollback()
    $ bn_tut_msg = 4
    $ jumpLabel = "ep10_dwy_tut3_label"
    show screen brawler_arrow_choice_screen_tutorial
    pause
    label ep10_dwy_tut3_label:

    $ bn_tut_msg = 0
    $ bn_combo_idx = 0
    $ bn_arrow_combination = ["down","right","up","down","left","left"]
    $ jumpLabel = "ep10_dwy_tut4_label"
    show screen brawler_arrow_combo_screen_tutorial
    pause
    label ep10_dwy_tut4_label:
    $ renpy.block_rollback()
    $ bn_mc_stamina = 2

play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym28 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym29 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym28 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym29 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym28 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym29 with hpunch
$ renpy.pause(0.5)
scene ep10_gym24_neutral with dissolve
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 5
dwy "Dude, you're gassed out."
dwy "Your kicks are lazy when you're gassed out. You need to work on that, for sure."
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 0
scene ep10_gym30 with dissolve
dwy "A well-placed low kick will cripple your opponent."
if minigames and tutorial_ongoing:
    $ bn_mc_stamina = 3
dwy "If you're fighting a big dude, some swift kicks to the side of his knee are gonna slow him down."
dwy "You need to learn that, for sure."

scene ep10_gym24_neutral with dissolve
if minigames and tutorial_ongoing:
    $ bn_mc_stamina = 4
dwy "Aight. You had your rest. I wanna see you rage. Dig deep into that bag. 30 seconds. Go!"
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 6
    $ bn_arrow_input_tut = 0
    $ bn_combo_idx = 0
    $ bn_arrow_selection = ["RAGE","LOW","OUCH","SLIP"]
    $ renpy.block_rollback()
    $ jumpLabel = "ep10_dwy_tut5_label"
    show screen brawler_arrow_choice_screen_tutorial
    pause
    label ep10_dwy_tut5_label:

    $ bn_rage_ending = False
    $ bn_rage_flash = False
    $ bn_tut_msg = 7
    $ bn_combo_idx = 0
    $ bn_arrow_combination = ["down","right","up","down","left","left"]
    $ jumpLabel = "ep10_dwy_tut6_label"
    show screen brawler_rage_screen_tutorial
    pause
    label ep10_dwy_tut6_label:
    $ renpy.block_rollback()
    $ bn_tut_msg = 0
    $ bn_mc_stamina = 0
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
dwy "Remember what I told you. Aim into the bag and follow through."
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
dwy "Mix it up. Alternate. Highs and lows."
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym28 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym25 with hpunch
dwy "Dig deep."
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym26 with hpunch
dwy "Finish with a strong blow from the side."
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep10_gym28 with hpunch
$ renpy.pause(0.5)

scene ep10_gym31 with dissolve
if minigames and tutorial_ongoing:
    $ bn_mc_stamina = 1
dwy "Now you do that to that walking fridge and you'll reset his brain to factory settings."
play sound "sound_effects/whoosh.mp3"
scene ep10_gym32 with hpunch
if minigames and tutorial_ongoing:
    $ bn_mc_stamina = 2

dwy "Think fast!"
if minigames and tutorial_ongoing:
    $ bn_arrow_input_tut = 0
    $ bn_arrow_selection = ["DODGE","BLOCK","BLOCK","MISS"]
    $ renpy.block_rollback()
    $ bn_tut_msg = 11
    $ jumpLabel = "ep10_dwy_tut7_label"
    show screen brawler_arrow_choice_screen_tutorial
    pause
    label ep10_dwy_tut7_label:

    $ bn_mc_stamina = 0
    $ bn_tut_msg = 0
    $ bn_combo_idx = 0
    $ bn_arrow_combination = ["up","up","down","left","up"]
    $ jumpLabel = "ep10_dwy_tut8_label"
    show screen brawler_arrow_combo_screen_tutorial
    pause
    label ep10_dwy_tut8_label:
    $ renpy.block_rollback()

play sound "sound_effects/season3/counter.mp3"
scene ep10_gym33 with hpunch
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 12
    $ jumpLabel = "ep10_dwy_tut9_label"
    $ renpy.block_rollback()
    show screen brawler_counter_screen_tutorial
    pause
    label ep10_dwy_tut9_label:
    $ renpy.block_rollback()
else:
    $ renpy.pause(0.5)
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep10_gym34 with hpunch
dwy "Quick thinking."
if minigames and tutorial_ongoing:
    $ bn_tut_msg = 13
    pause
hide screen brawler_dwyane_tutorial_screen
show screen new_phone_screen
$ renpy.block_rollback()
scene ep10_gym35 with dissolve
dwy "Aight, I've seen 'nuff."
scene ep10_gym36 with dissolve
mc "What do you think?"
scene ep10_gym35 with dissolve
dwy "You're a rookie. Ain't no way around it."
dwy "But it ain't bad. Because on a street level, yeah, you can scrap. You got a mad kick."
dwy "With some practice, you can hang with the best of us here."
dwy "Hit me up the next time you're here and we'll train. No extra charge."
scene ep10_gym36 with dissolve
mc "That would be great!"
scene ep10_gym35 with dissolve
dwy "But if you start sucking, I'm gonna charge you."
scene ep10_gym36 with dissolve
mc "Oh..."
stop music fadeout 5
scene ep10_gym37 with dissolve
dwy "This is not gonna work if you be all gullible and shit all the time."
scene ep10_gym38 with dissolve
mc "Haha... Got it."

label ep10_party_plan_label:
play music "music/ep10/licensed_music/track139.mp3"
scene ep10_party_plan1 with wiperight
le "Tommy! Come on! Be reasonable."
tm "I am being reasonable, but you lost the bet."
scene ep10_party_plan2 with dissolve
le "Even after all those posters, you still want this picture on the wall?"
scene ep10_party_plan3 with dissolve
tm "..."
scene ep10_party_plan4 with dissolve
tm "Yeah."
scene ep10_party_plan2 with dissolve
le "*{i}Sigh{/i}* It's not fair..."
scene ep10_party_plan5 with dissolve
le "[name]! Can you convince Tommy to remove my picture from the wall?"
if branchMayaJosy:
    scene ep10_party_plan6 with dissolve
    mc "I'm probably the last guy Tommy wants to listen to."
    scene ep10_party_plan7 with dissolve
    tm "I don't know who said that, but if you see [name], tell him about DIKs' Thanksgiving. I'm counting on you for it."
    scene ep10_party_plan6 with dissolve
    mc "Great... I'm invisible to you now. Real mature."
else:
    if affinity == "DIK":
        scene ep10_party_plan8 with dissolve
        mc "Didn't you lose a bet?"
        scene ep10_party_plan9b with dissolve
        tm "He sure did."
        scene ep10_party_plan8b with dissolve
        mc "Then, I'm with Tommy on this one."
    else:
        scene ep10_party_plan8 with dissolve
        mc "Tommy? How about it?"
        scene ep10_party_plan9 with dissolve
        tm "No. A bet is a bet."
        scene ep10_party_plan8 with dissolve
        mc "Sorry, I tried."
    scene ep10_party_plan9 with dissolve
    tm "Leon, fill him in on DIKs' Thanksgiving. Will you?"
    scene ep10_party_plan10 with dissolve
    le "Sure..."
scene ep10_party_plan11 with dissolve
mc "It's a tradition, right?"
scene ep10_party_plan13 with dissolve
le "Yeah, and it's our turn to host it."
scene ep10_party_plan12 with dissolve
mc "Oh, you never did it before?"
scene ep10_party_plan13 with dissolve
le "I wasn't a DIK last year. We just partied with them."
scene ep10_party_plan12 with dissolve
mc "Right, I forgot."
scene ep10_party_plan13 with dissolve
le "Let's get Derek and Jamie for this."
scene ep10_party_plan14 with wipeleft
de "What is DIKs' Thanksgiving?"
scene ep10_party_plan19 with dissolve
jm "They told me that it's when the recent maggots show their thanks to the elder DIKs by hosting a dinner party."
scene ep10_party_plan20 with dissolve
mc "DIKs-only?"
scene ep10_party_plan23 with dissolve
jm "I'm not sure if there are any rules for it. I can check with Jacob."
scene ep10_party_plan22 with dissolve
le "I don't think they are expecting anything spectacular. But it's a way to honor our brothers, so let's do our best."
scene ep10_party_plan25 with dissolve
mc "Ok. Let's begin with the big questions. When, where and what will it be?"
scene ep10_party_plan22 with dissolve
le "We can't do it during actual Thanksgiving. How about the day before? Our break starts that Wednesday, anyway."
scene ep10_party_plan23 with dissolve
jm "Yeah, I'm sure many want to visit their real families that Thursday and maybe even over the weekend."
scene ep10_party_plan20 with dissolve
mc "That Wednesday sounds good. What about the location?"
scene ep10_party_plan14 with dissolve
de "We can do it here, but maybe it's a bit boring."
scene ep10_party_plan19 with dissolve
jm "Thinking about it, I know that Jacob and John Boy didn't host it here last year."
jm "They went to a restaurant and then to the strip club."
scene ep10_party_plan16 with dissolve
de "That sounds great! Let's do that!"
scene ep10_party_plan22 with dissolve
le "We can't copy what they did, can we? It would feel cheap."
scene ep10_party_plan15 with dissolve
de "Yeah, but what else can you do in November? It's gotten pretty cold outdoors."
scene ep10_party_plan17 with dissolve
mc "I guess outdoors could work if we made a fire, but that's about it."
scene ep10_party_plan23 with dissolve
jm "We could throw a barbecue."
scene ep10_party_plan21 with dissolve
le "Yeah! That could work. There's a spot for it near the lake."
le "We can have a big bonfire. And if people feel up for it, we could bring tents and spend the night."
le "The fire should keep us warm, but if it doesn't, it's just a short walk home."
scene ep10_party_plan16 with dissolve
de "Yes! Let's have a fire theme!"
de "I can make flaming shots for everyone!"
scene ep10_party_plan17 with dissolve
mc "Flaming shots?"
scene ep10_party_plan16 with dissolve
de "Let me get my bottle and show you!"
scene ep10_party_plan24 with dissolve
jm "We could make s'mores and drink beer all night. It sounds pretty damn fun if you ask me."
scene ep10_party_plan20 with dissolve
mc "These are all good ideas. I'm not too sure about the flaming shots. Derek will have to show us what that's about."
scene ep10_party_plan28 with wiperight
de "And all that's left is to ignite the shots like...this."
play sound "sound_effects/season3/lighter.mp3"
scene ep10_party_plan29 with dissolve
de "Cool, huh?"
mc "How can you drink that? Won't you catch on fire?"
scene ep10_party_plan30 with dissolve
stop music fadeout 3
de "Obviously, you should put the fire out before you drink it. With your palm, like this!"
play sound "sound_effects/season3/flaming_shot.mp3"
scene ep10_party_plan31 with hpunch
play music "music/ep10/faked_reality.mp3"
de "Oh, fuck!"
mc "Derek! What did you do?"
scene ep10_party_plan32 with dissolve
de "Don't panic! It's just a small house fire. No one's ever died from that."
scene ep10_party_plan33 with dissolve
jm "Get a fire extinguisher!"
scene ep10_party_plan34 with dissolve
de "*{i}Blows frenetically{/i}*"
mc "Should we use water!?"
scene ep10_party_plan35 with dissolve
de "Huh? Won't that make it worse?"
scene ep10_party_plan34 with dissolve
mc "I don't know!"
de "*{i}Blows frenetically{/i}*"
scene ep10_party_plan36 with dissolve
le "Get back!"
scene ep10_party_plan37 with dissolve
le "Huh? It doesn't work!"
mc "Why doesn't it work?"
scene ep10_party_plan38 with dissolve
de "..."
play sound "sound_effects/whoosh_2.mp3"
scene ep10_party_plan42
de "Ground control. This is a beautiful night for new steps of man."
scene ep10_party_plan43 with dissolve
de "Prepare for lift-off."
play sound "sound_effects/season3/fire_extinguisher2.mp3"
scene ep10_party_plan44 with dissolve
de "ROCKET MAAAAN!!!"
play sound "sound_effects/shove.mp3"
scene ep10_party_plan45 with vpunch
de "Ow! Ow! Ow! Fuck! My nuts!"
scene ep10_party_plan38
de "Fuck."
scene ep10_party_plan39 with vpunch
play sound "sound_effects/season3/fire_extinguisher.mp3"
"*{i}PSSCCCHHHHH{/i}*"
stop music fadeout 3
scene ep10_party_plan40 with dissolve
$ renpy.pause()

$ guideSuggestedPage = 118
play music "music/ep10/licensed_music/track139.mp3"
scene ep10_party_plan46 with wipeleft
mc "No flaming shots. We don't wanna cause a forest fire."
scene ep10_party_plan21 with dissolve
le "Hear, hear."
scene ep10_party_plan18 with dissolve
de "Can I still help out with the alcohol?"
scene ep10_party_plan17 with dissolve
mc "Yeah, sure. Let's get into some specifics..."

hide screen new_phone_screen
$ pp_activity_choices = [2,2,2]
if not minigames:
    $ party_planner_get_nm_score(pp_nm_dik_happiness)
    $ pp_nm_party_preference = [[0,1,0],[0,2,0],[1,1,1],[2,0,0],[-1,0,0],[-1,-1,0],[1,0,1],[0,-1,1]]
    $ pp_nm_activity_description = [["New Alcohol","Leftover Alcohol","Don't care","Anything"],["BBQ Quality meat","BBQ Pork","Don't care","Not Hot Dogs"],["Beer Pong","Don't care"]]
    $ currentActivity = 0
    $ pp_money = 20
else:
    $ pp_money = 20

scene ep10_party_plan20 with dissolve
mc "We need to be smart with the budget for this party."
mc "About the alcohol... It's for us guys and whoever might show up after our barbecue. We should bring some extra."
mc "How much do we have left after our Halloween party?"
scene ep10_party_plan15 with dissolve
de "Some. Not a lot. We could use it, but many bottles are half-full or less."
scene ep10_party_plan26 with dissolve
if not minigames:
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
menu:
    "New alcohol ($3)" if minigames or pp_money > 2:
        $ pp_money -= 3
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 0
        mc "Let's splurge on some new alcohol, then. It's for showing the DIKs our thanks, after all."
    "Leftover alcohol ($1)" if minigames or pp_money > 0:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_money -= 1
        $ pp_activity_choices[0] = 1
        mc "Let's use the leftover alcohol and buy as little as possible of what we need on top of it."
    "B.Y.O.B.":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 2
        mc "We can save some money here by making people bring what they want to drink."
        mc "It's cheap, but we can make up for it."


scene ep10_party_plan23 with dissolve
jm "I wish John Boy could help us with the food."
scene ep10_party_plan21 with dissolve
le "I'm sure he won't mind us asking."
scene ep10_party_plan20 with dissolve
mc "Still, it should be us who plan this. It can also be nice for him to catch a break and enjoy himself."
scene ep10_party_plan15 with dissolve
de "What food should we buy?"
scene ep10_party_plan17 with dissolve

if not minigames:
    $ currentActivity = 1
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
menu:
    "BBQ quality meat ($4)" if minigames or pp_money > 3:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 0
        $ pp_money -= 4
        mc "Let's buy some high-quality meat and the fixings needed for this party. They deserve it."
    "BBQ pork ($2)" if minigames or pp_money > 1:
        $ pp_money -= 2
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 1
        mc "Let's buy some pork and the fixings needed for the barbecue. Nothing too fancy."
    "Hot dogs":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 2
        mc "I think I saw hot dogs in the freezer. Let's save some money by keeping the food simple."


scene ep10_party_plan20 with dissolve
mc "Camping and the barbecue put aside, should we do something else for them?"
mc "Should I bring my guitar?"
scene ep10_party_plan22 with dissolve
le "You could, but we could play some games, maybe?"
scene ep10_party_plan23 with dissolve
jm "We can always dust off the Beer Pong table. It's not that heavy to bring with us."
scene ep10_party_plan16 with dissolve
de "That would work."
scene ep10_party_plan21 with dissolve
le "Beer Pong usually gets expensive."
scene ep10_party_plan26 with dissolve

if not minigames:
    $ currentActivity = 2
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
menu:
    "Beer Pong ($5)" if minigames or pp_money > 4:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 0
        $ pp_money -= 5
        mc "Playing beer pong would be fun. I think they will enjoy it."
    "Nothing":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 1
        mc "I don't think we have to do anything at the party. Let's keep it calm. I think drinking and talking will be enough to have a good time."

scene ep10_party_plan27 with dissolve
mc "It looks like we have a plan here."

if minigames:
    stop music fadeout 3
    mc "As for the details... How about this?"
    $ tmpMenu = quick_menu
    $ quick_menu = 0
    play music "music/ep10/isolation.mp3"
    queue music ["music/ep10/licensed_music/track139.mp3","music/ep10/faked_reality.mp3","music/ep10/isolation.mp3"]
    $ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx2", loop=True)
    $ renpy.sound.play("sound_effects/season3/fire_burning.mp3", channel="sfx3", loop=True)
    show screen pp_intro_screen
    $ renpy.pause(0.5)
    play sound "sound_effects/bottle_clink.mp3"
    $ renpy.pause(0.5)
    play sound "sound_effects/bottle_open.mp3"
    pause

    label ep10_play_label:
    $ renpy.music.stop(channel="sfx2", fadeout=12)
    $ renpy.music.stop(channel="sfx3", fadeout=12)
    $ tmp_list = [-1,-1]

    $ pp_tut_state = 0
    show screen pp_bg_screen_ep10


    $ pp_round = 2
    $ pp_continue_label = "ep10_pp_cont_label"
    $ renpy.block_rollback()
    jump party_planner_setup_round_label

    label ep10_pp_cont_label:
    hide screen pp_bg_screen_ep10
    $ quick_menu = tmpMenu
    mc "Yeah, that will work."
    $ tmpInt = 0
    python:
        for y in pp_needs_met[0]:
            if y:
                tmpInt += 1
    if tmpInt == 4:
        scene ep10_party_plan16 with dissolve
        de "That's awesome if you ask me."
    elif tmpInt > 2:
        scene ep10_party_plan16 with dissolve
        de "That will work, I think."
    else:
        scene ep10_party_plan18 with dissolve
        de "I'm not too sure about this."

    $ tmpInt = 0
    python:
        for y in pp_needs_met[4]:
            if y:
                tmpInt += 1
    if tmpInt == 4:
        scene ep10_party_plan21 with dissolve
        le "I think this is perfect."
    elif tmpInt > 2:
        scene ep10_party_plan21 with dissolve
        le "Pretty good, in my opinion."
    else:
        scene ep10_party_plan22 with dissolve
        le "I would have done it way differently, but ok."
else:
    scene ep10_party_plan26 with dissolve
    label ep10_lock_in_label:
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
            $ pp_money = 9
            show screen pp_dik_preferences_screen
            menu:
                "New alcohol ($3)":
                    $ pp_money = 6
                    $ pp_activity_choices[0] = 0
                "Leftover alcohol ($1)":
                    $ pp_money = 8
                    $ pp_activity_choices[0] = 1
                "B.Y.O.B.":
                    $ pp_activity_choices[0] = 2
            $ currentActivity = 1
            menu:
                "BBQ quality meat ($4)" if minigames or pp_money > 3:
                    $ pp_money -= 4
                    $ pp_activity_choices[1] = 0
                "BBQ pork ($2)" if minigames or pp_money > 1:
                    $ pp_money -= 2
                    $ pp_activity_choices[1] = 1
                "Hot dogs":
                    $ pp_activity_choices[1] = 2
            $ currentActivity = 2
            menu:
                "Beer Pong ($5)" if minigames or pp_money > 4:
                    $ pp_money -= 5
                    $ pp_activity_choices[2] = 0
                "Nothing":
                    $ pp_activity_choices[2] = 1
            hide screen pp_dik_preferences_screen
            jump ep10_lock_in_label


$ ep10_pp_alcohol = pp_activity_choices[0]
$ ep10_pp_meat = pp_activity_choices[1]
$ ep10_pp_activity = pp_activity_choices[2]
show screen new_phone_screen
scene ep10_party_plan23 with dissolve
jm "I guess we're not hiring strippers."
scene ep10_party_plan18 with dissolve
de "Can't we ask the HOTs to come? Maybe they wanna camp with us?"
scene ep10_party_plan17 with dissolve
mc "I can always check with them. Maybe we can come up with something."
mc "After the barbecue, we can invite the girls to hang with us."
scene ep10_party_plan21 with dissolve
le "I like the sound of that. I need a rematch after the Halloween fiasco."
le "I'm not gonna sleep in my tent alone, let me tell you that much."
scene ep10_party_plan20 with dissolve
mc "All right, we're done here for tonight."
mc "I guess the only question that remains is..."
stop music fadeout 3
scene ep10_party_plan41 with dissolve
mc "Who will tell John Boy his darling kitchen caught on fire?"


label ep10_quinn_dt_label:
if not (branchAlone and ep8_quinn_lewd):
    play music "music/ep6/licensed_music/track21.mp3"
    jump ep10_quinn_dt2_label

play music "music/ep4/midnight_stroll.mp3"
scene ep10_quinn_dt1 with wipeleft
qu "Hahaha!"
scene ep10_quinn_dt2 with dissolve
mc "Beat me over the head with it."
scene ep10_quinn_dt3 with dissolve
qu "It's fucking funny. Planning an outdoor party in November. Where do you come up with this shit?"
scene ep10_quinn_dt4 with dissolve
mc "Derek, Jamie and Leon thought it was a good idea."
scene ep10_quinn_dt3 with dissolve
qu "Haha! You guys are all morons, then."
qu "I can't wait to see the clucks about how miserable that party was."
scene ep10_quinn_dt4 with dissolve
mc "Oh, didn't you hear?"
scene ep10_quinn_dt3 with dissolve
qu "Hear what?"
scene ep10_quinn_dt4 with dissolve
mc "You girls are doing it too."
scene ep10_quinn_dt5 with dissolve
qu "Come again?"
scene ep10_quinn_dt6 with dissolve
mc "Maya's HOT party... We're having it at the same spot and will turn it into a mixer after dinner."
scene ep10_quinn_dt7 with dissolve
qu "This is why I should be in charge of shit. Sage is fucking killing me here!"
scene ep10_quinn_dt6 with dissolve
if ep8_mansion_won:
    mc "Actually, it was Lily's idea to join us. I got Sage's confirmation before I picked you up."
else:
    mc "Actually, it was Lily's idea to join us. I got Sage's confirmation before we went here."
scene ep10_quinn_dt8 with dissolve
qu "Lily? Come on! You can't trust a freshman with these decisions!"
qu "Is Sage punishing me by letting Lily plan it? Gah!"
scene ep10_quinn_dt9 with dissolve
mc "You're just looking to complain. Freshmen can do great with these things, too."
scene bg anim_quinn_clap_ep10 movie with dissolve
"*{i}Slow clap{/i}*"
qu "Thanks to you, we'll all get pneumonia from camping in November. Good job, [name]! You nailed it."
scene ep10_quinn_dt10 with dissolve
mc "I know that's sarcasm, but I'm gonna pretend it's not. The party will be fun."
mc "Camping is optional, but you can stay in my tent if you're lucky."
scene ep10_quinn_dt11 with dissolve
qu "Only two creatures sleep in the woods. Bears and hobos."
scene ep10_quinn_dt10 with dissolve
mc "Those two, huh?"
scene ep10_quinn_dt11 with dissolve
qu "I can't believe you're forcing me to come."
scene ep10_quinn_dt10 with dissolve
mc "Hey, you made me come with you tonight. I was gonna relax on my couch."
mc "What are we doing here, by the way?"
scene ep10_quinn_dt11 with dissolve
qu "We're hanging out."
scene ep10_quinn_dt12 with dissolve
mc "Having dinner, talking, being alone together..."
mc "If I didn't know better, I'd say it sounds like a date."
scene ep10_quinn_dt13 with dissolve
qu "It's a fucking burger. I don't get why you keep trying to push the romantic shit on things we do."
qu "One day, I'm not gonna ask you to do things because of it."
scene ep10_quinn_dt12 with dissolve
mc "Dates don't have to be romantic. They can be completely casual."
scene ep10_quinn_dt13 with dissolve
qu "Good. Because there's nothing romantic about tonight."
scene ep10_quinn_dt14 with dissolve
mc "I agree."
mc "But it doesn't change the fact that it's a date."
scene ep10_quinn_dt15 with dissolve
qu "Don't go anywhere."
scene ep10_quinn_dt16 with dissolve
mc "Quinn, it was a joke."
scene ep10_quinn_dt17 with dissolve
qu "I know. Wipe that grin off before I get back."
scene ep10_quinn_dt18 with dissolve
$ renpy.pause()

play sound "sound_effects/season3/slurp.mp3"
scene ep10_quinn_dt19 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/soda_machine.mp3"
scene ep10_quinn_dt20 with dissolve
$ renpy.pause()
scene ep10_quinn_dt21 with dissolve
uk "Do you know why I'm here?"
scene ep10_quinn_dt22 with dissolve
qu "I'm guessing you didn't come for another soda can."
scene ep10_quinn_dt21 with dissolve
uk "Fuck your soda cans."
scene ep10_quinn_dt23 with dissolve
cas "Sir. Did you pay for that?"
mc "Yeah, it's my refill."
scene ep10_quinn_dt21 with dissolve
uk "You made me delete it!"
scene ep10_quinn_dt23 with dissolve
cas "I'm sorry. You have a good evening."
mc "Yeah, don't mention it."
scene ep10_quinn_dt24 with dissolve
uk "Stop pushing! You already got what you wanted."
scene ep10_quinn_dt25 with dissolve
cs "Excuse me? Are you done?"
mc "Yeah, go ahead."
scene ep10_quinn_dt26 with dissolve
uk "I don't want to see you ever again."
scene ep10_quinn_dt27 with dissolve
qu "Tch... You called me, bitch. Go back to your career. I didn't realize junkies could have one."
scene ep10_quinn_dt28 with dissolve
$ renpy.pause()
scene ep10_quinn_dt14 with dissolve
mc "Who was that?"
scene ep10_quinn_dt13 with dissolve
qu "None of your business."
scene ep10_quinn_dt14 with dissolve
mc "Why were you fighting?"
scene ep10_quinn_dt13 with dissolve
qu "Didn't I just say it's none of your business?"
scene ep10_quinn_dt14 with dissolve
mc "..."
mc "What was that about the soda can?"
scene ep10_quinn_dt29 with dissolve
qu "Oh my fucking God!"
scene ep10_quinn_dt30 with dissolve
mc "Come on. Share stuff with me. Maybe I can help you with it."
scene ep10_quinn_dt29 with dissolve
qu "I don't need your fucking help with it. And I don't have to share anything with you."
scene ep10_quinn_dt30 with dissolve
mc "..."
mc "All right..."
mc "I think I'm gonna head back."
scene ep10_quinn_dt31 with dissolve
qu "What? Not yet."
scene ep10_quinn_dt32 with dissolve
mc "Don't sweat it. You can stay as long as you want."
$ renpy.sound.play("sound_effects/rain_outside.mp3", channel="sfx1", loop=True)
scene ep10_quinn_dt33
show screen rain_screen
with dissolve
qu "[name]! Wait."
scene ep10_quinn_dt34 with dissolve
mc "For what?"
scene ep10_quinn_dt35 with dissolve
qu "Are you seriously leaving?"
scene ep10_quinn_dt34 with dissolve
mc "Why don't you trust me with things?"
scene ep10_quinn_dt35 with dissolve
qu "I trust you."
scene ep10_quinn_dt36
hide screen rain_screen
with dissolve
mc "No, you don't. Despite everything we've done together, you still don't let me in on things."
mc "I love hanging out with you and the sex we have is fucking amazing..."
mc "...but I don't know who you are. And that bothers me. You're a closed book."
scene ep10_quinn_dt37 with dissolve
qu "I've told you things about me."
scene ep10_quinn_dt36 with dissolve
mc "Barely."
scene ep10_quinn_dt37 with dissolve
qu "Remember broccoli?"
scene ep10_quinn_dt36 with dissolve
mc "Yeah. And I also remember meeting you at night in the rain all bloody and you not telling me why."
mc "And now this. Something I witnessed with my own eyes that you refuse to talk about."
scene ep10_quinn_dt39 with dissolve
qu "So, I have to tell you everything? You gotta know every single detail about me?"
qu "I'm not allowed to have some fucking privacy?"
scene ep10_quinn_dt38 with dissolve
mc "When did I say that? I'm not asking for a lot here. I'm asking for a little."
scene ep10_quinn_dt39 with dissolve
qu "You don't know what you're asking for. So, shut the hell up!"
scene ep10_quinn_dt38 with dissolve
mc "Wow... I don't have to take this."
scene ep10_quinn_dt40
show screen rain_screen
with dissolve
mc "As soon as the rain slows down, I'm leaving."
scene ep10_quinn_dt41 with dissolve
$ renpy.pause()
scene ep10_quinn_dt42 with dissolve
$ renpy.pause()
scene ep10_quinn_dt43 with dissolve
$ renpy.pause()
scene ep10_quinn_dt44
hide screen rain_screen
with dissolve
qu "I got mugged."
qu "That night you helped me...with the bloody nose..."
qu "Someone jumped me and stole all my cash."
scene ep10_quinn_dt46 with dissolve
mc "You got mugged? Why didn't you say something?"
qu "Because it wouldn't have mattered."
mc "Of course, it would. We could have gone to the police."
scene ep10_quinn_dt44 with dissolve
qu "*{i}Sigh{/i}* This is why I can't tell you shit."
scene ep10_quinn_dt45 with dissolve
mc "What?"
scene ep10_quinn_dt44 with dissolve
qu "I couldn't go to the police because the money comes from..."
qu "It's drug money, ok?"
scene ep10_quinn_dt45 with dissolve
mc "Oh..."
scene ep10_quinn_dt44 with dissolve
qu "Where do you think Tommy gets his weed from?"
scene ep10_quinn_dt46 with dissolve
mc "I haven't thought a lot about it, but I heard he bought from Vinny."
qu "That's not how it has been."
mc "Are you selling drugs to him?"
qu "Him...and others."
mc "That girl you fought with, too?"
scene ep10_quinn_dt47
show screen rain_screen
with dissolve
qu "I used to, but it's more complicated than that."
scene ep10_quinn_dt48 with dissolve
$ renpy.pause()
scene ep10_quinn_dt47 with dissolve
qu "Don't think that I don't want you to know things about me."
scene ep10_quinn_dt49 with dissolve
mc "That's how it feels like at times. Like you're scared to tell me the truth."
scene ep10_quinn_dt50 with dissolve
qu "Maybe I am scared."
scene ep10_quinn_dt49 with dissolve
mc "Scared to tell the truth?"
scene ep10_quinn_dt50 with dissolve
qu "Scared that you will be scared of me."
scene ep10_quinn_dt51 with dissolve
$ renpy.pause()
scene ep10_quinn_dt52 with dissolve
qu "*{i}Smack{/i}*"
scene ep10_quinn_dt53
hide screen rain_screen
with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=5)
stop music fadeout 5
scene ep10_quinn_dt54 with dissolve
$ renpy.pause()
scene ep10_quinn_dt55 with dissolve
qu "It stopped raining."
qu "Still wanna leave?"
scene ep10_quinn_dt56 with dissolve
mc "Yeah. Let's go."
scene ep10_quinn_dt57 with dissolve
$ renpy.pause()
play sound "sound_effects/slap.mp3"
scene ep10_quinn_dt58 with hpunch
$ renpy.pause()
scene ep10_quinn_dt59 with dissolve
$ renpy.pause()

if not persistent.ep10_card11:
    $ persistent.ep10_card11 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep10_card12:
    $ persistent.ep10_card12 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
$ mgallery_add_photo("ep10_quinn_solo_pic0")
$ guideSuggestedPage = 119
if ep8_mansion_won:
    scene ep10_quinn_dt60 with dissolve
    mc "Won't you freeze without the soft top?"
    scene ep10_quinn_dt61 with dissolve
    qu "Not more than I will from camping in November."
    scene ep10_quinn_dt61b with dissolve
    play music "music/ep10/licensed_music/track141.mp3"
    $ renpy.pause()
    scene ep10_quinn_dt61 with dissolve
    qu "This is the way to ride, babe."
    scene anim_quinn_car_ep10 with dissolve
    pause
    scene ep10_quinn_dt62 with dissolve
    $ renpy.pause()
    scene ep10_quinn_dt63 with dissolve
    $ renpy.pause()
    scene ep10_quinn_dt64 with dissolve
    $ renpy.pause()
    scene ep10_quinn_dt65 with dissolve
    mc "Where to?"
    scene ep10_quinn_dt66 with dissolve
    qu "I'll tell you when to turn. Keep going straight ahead."
    scene ep10_quinn_dt65 with dissolve
    mc "And where are we going?"
    scene ep10_quinn_dt66 with dissolve
    qu "To my dad's old place. Uncle Buddy lives there now."
    scene ep10_quinn_dt67 with dissolve
    mc "Oh, to your uncle, then."
    qu "Not by blood."
    qu "I grew up around him. He was Dad's best friend before he died."
    scene ep10_quinn_dt68 with dissolve
    mc "You mentioned your dad before, but I didn't know he was dead."
    scene ep10_quinn_dt69 with dissolve
    qu "Well, he is."
    scene ep10_quinn_dt68 with dissolve
    mc "I'm sorry to hear that."
    scene ep10_quinn_dt70 with dissolve
    qu "I get the drugs from Buddy. I sell them. I return the money and I keep a share."
    scene ep10_quinn_dt71 with dissolve
    mc "And someone mugged you for it?"
    scene ep10_quinn_dt70 with dissolve
    qu "Yeah."
    scene ep10_quinn_dt71 with dissolve
    mc "It doesn't sound safe..."
    mc "And that's why you really asked me to come tonight."
    scene ep10_quinn_dt72 with dissolve
    qu "..."
    scene ep10_quinn_dt70 with dissolve
    qu "Can't there be more reasons than one?"
    scene ep10_quinn_dt71 with dissolve
    mc "I don't like being used like that, and if you had told me that was the reason from the start..."
    scene ep10_quinn_dt74 with dissolve
    qu "Yeah, I know!"
    if affinity == "CHICK":
        jump ep10_quinn_no_help_label
        
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Quinn path)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "I still would have come [m_c1][mod_choices[0]]":
            $ ep10_quinn_help = True
            scene ep10_quinn_dt71 with dissolve
            mc "I still would have come."
            scene ep10_quinn_dt73 with dissolve
            $ renpy.pause()
            scene ep10_quinn_dt71 with dissolve
            mc "I'm not that scared. And it would have felt better to be prepared for it."
            scene ep10_quinn_dt71b with dissolve
            $ renpy.pause()
            scene ep10_quinn_dt75 with dissolve
            qu "Left turn at the next intersection."
            scene ep10_quinn_dt76 with wipeleft
            qu "Wait for me here, ok?"
            scene ep10_quinn_dt77 with dissolve
            mc "I'm not going anywhere."
            scene ep10_quinn_dt78 with dissolve
            $ renpy.pause()
        "I wouldn't have come":
            label ep10_quinn_no_help_label:
            $ ep10_quinn_help = False
            scene ep10_quinn_dt71 with dissolve
            mc "I wouldn't have come."
            scene ep10_quinn_dt72 with dissolve
            $ renpy.pause()
            scene ep10_quinn_dt71 with dissolve
            mc "I'll help you out this time, but I won't take part in this again."
            scene ep10_quinn_dt69 with dissolve
            qu "Yeah, I get it. Left turn at the next intersection."
            scene ep10_quinn_dt76 with wipeleft
            qu "Wait for me here, ok?"
            scene ep10_quinn_dt77 with dissolve
            mc "Hurry, ok?"
else:
    play music "music/ep10/licensed_music/track141.mp3"
    scene ep10_quinn_dt79 with dissolve
    mc "It's a long walk..."
    qu "We're almost there."
    mc "And where is \"there\"?"
    scene ep10_quinn_dt80 with dissolve
    qu "My dad's old place. Uncle Buddy lives there now."
    scene ep10_quinn_dt81 with dissolve
    mc "Oh, to your uncle, then."
    scene ep10_quinn_dt80 with dissolve
    qu "Not by blood."
    qu "I grew up around him. He was Dad's best friend before he died."
    scene ep10_quinn_dt81 with dissolve
    mc "You mentioned your dad before, but I didn't know he was dead."
    scene ep10_quinn_dt80 with dissolve
    qu "Well, he is."
    scene ep10_quinn_dt81 with dissolve
    mc "I'm sorry to hear that."
    scene ep10_quinn_dt82 with dissolve
    qu "I get the drugs from Buddy. I sell them. I return the money and I get a share."
    mc "And someone mugged you for it?"
    qu "Yeah."
    mc "It doesn't sound safe..."
    mc "And that's why you really asked me to come tonight."
    scene ep10_quinn_dt83 with dissolve
    qu "..."
    scene ep10_quinn_dt84 with dissolve
    qu "Can't there be more reasons than one?"
    scene ep10_quinn_dt85 with dissolve
    mc "I don't like being used like that, and if you had told me that was the reason from the start..."
    scene ep10_quinn_dt86 with dissolve
    qu "Yeah, I know!"
    if affinity == "CHICK":
        jump ep10_quinn_no_help2_label
        
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Quinn path)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "I still would have come [m_c1][mod_choices[0]]":
            $ ep10_quinn_help = True
            scene ep10_quinn_dt85 with dissolve
            mc "I still would have come."
            scene ep10_quinn_dt87 with dissolve
            mc "I'm not that scared. And it would have felt better to be prepared for it."
            scene ep10_quinn_dt88 with wipeleft
            qu "Wait for me here, ok?"
            scene ep10_quinn_dt89 with dissolve
            mc "You got it."
            scene ep10_quinn_dt90 with dissolve
            $ renpy.pause()
        "I wouldn't have come":
            label ep10_quinn_no_help2_label:
            $ ep10_quinn_help = False
            scene ep10_quinn_dt85 with dissolve
            mc "I wouldn't have come."
            scene ep10_quinn_dt83 with dissolve
            $ renpy.pause()
            scene ep10_quinn_dt85 with dissolve
            mc "I'll help you out this time, but I won't take part in this again."
            scene ep10_quinn_dt88 with wipeleft
            qu "Wait for me here, ok?"
            scene ep10_quinn_dt89 with dissolve
            mc "Hurry, ok?"

scene ep10_quinn_dt91 with dissolve
if ep10_quinn_help:
    mc "(It's kinda crazy that she's doing this...)"
    mc "(Maybe it's stupid of me to agree to help her out with it.)"
    mc "(But I'm not doing anything wrong... I'm just tagging along.)"
else:
    mc "(It's fucking crazy that she's doing this...)"
    mc "(I didn't realize she was in this deep with it.)"
    mc "(Is it wrong for me to even be here?)"
stop music fadeout 3
mc "(Her telling me about this... It explains a lot...)"

scene ep10_quinn_dt92 with dissolve
"*{i}Whistles{/i}*"
play music "music/ep6/licensed_music/track21.mp3"
scene ep10_quinn_dt93 with dissolve
vi "Haha... Dog knows what the whistle is."
scene ep10_quinn_dt94 with dissolve
mc "..."
if ep8_mansion_won:
    scene ep10_quinn_dt95 with dissolve
    vi "Rusty's car is so sweet... I can't believe you get to borrow it."
scene ep10_quinn_dt96 with dissolve
vi "Question is... What the hell are you doing here?"
scene ep10_quinn_dt97 with dissolve
$ renpy.pause()
scene ep10_quinn_dt98 with dissolve
vi "Is Quinn here?"
scene ep10_quinn_dt99 with dissolve
$ renpy.pause()
scene ep10_quinn_dt100 with dissolve
vi "I knew it."
vi "She left her dog outside, tied to a pole as she should."
scene ep10_quinn_dt101 with dissolve
$ renpy.pause()

label ep10_quinn_dt2_label:
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt102b with dissolve
else:
    scene ep10_quinn_dt102 with dissolve
$ renpy.pause()
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt103b with dissolve
else:
    scene ep10_quinn_dt103 with dissolve
bd "Here's your cut."
bd "What's your next order?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt107b with dissolve
else:
    scene ep10_quinn_dt107 with dissolve
qu "The same as last time."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt108b with dissolve
else:
    scene ep10_quinn_dt108 with dissolve
qu "No, wait. Fluoxetine, can you get it?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt104b with dissolve
else:
    scene ep10_quinn_dt104 with dissolve
bd "How much?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt107b with dissolve
else:
    scene ep10_quinn_dt107 with dissolve
qu "At least 20 pills. Start with some blisters."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt104b with dissolve
else:
    scene ep10_quinn_dt104 with dissolve
bd "What else?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt107b with dissolve
else:
    scene ep10_quinn_dt107 with dissolve
qu "Shrooms. A party's worth for like five to ten people."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt104b with dissolve
else:
    scene ep10_quinn_dt104 with dissolve
bd "Should I get a pen?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt107b with dissolve
else:
    scene ep10_quinn_dt107 with dissolve
qu "No, that's all."
scene ep10_quinn_dt105 with dissolve
bd "..."
scene ep10_quinn_dt106 with dissolve
bd "I gotta say... You've been staying busy."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt107b with dissolve
else:
    scene ep10_quinn_dt107 with dissolve
qu "Meh."
scene ep10_quinn_dt106 with dissolve
bd "No. Not meh. You've scored more customers."
bd "I'm not used to giving you this much money for two weeks of hustling."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt109b with dissolve
else:
    scene ep10_quinn_dt109 with dissolve
qu "Is that a problem?"
scene ep10_quinn_dt106 with dissolve
bd "Why are you running defense?"
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt109b with dissolve
else:
    scene ep10_quinn_dt109 with dissolve
qu "Because it doesn't sound like a compliment. It sounds like you're fishing for something."
qu "I've got a few new customers. It wasn't a problem in the past. Why is it a problem now?"
scene ep10_quinn_dt106 with dissolve
bd "Not a problem. Not a problem at all."
bd "Your daddy would have been proud."
if not (branchAlone and ep8_quinn_lewd):
    scene ep10_quinn_dt110b with dissolve
else:
    scene ep10_quinn_dt110 with dissolve
$ renpy.pause()
scene ep10_quinn_dt111 with dissolve
vi "What did you tell her? Bitch's moody tonight. She needs a fucking tampon."
scene ep10_quinn_dt112 with dissolve
bd "You're not supposed to be here until Sunday."
scene ep10_quinn_dt113 with dissolve
vi "Chill. I'm not presenting."
scene ep10_quinn_dt117 with dissolve
bd "You're not hanging out, either. What do you want?"
scene ep10_quinn_dt113 with dissolve
vi "I'm here to talk."
scene ep10_quinn_dt117 with dissolve
bd "Then talk."
scene ep10_quinn_dt114 with dissolve
vi "I lost some customers."
scene ep10_quinn_dt117 with dissolve
bd "Cops or OD?"
scene ep10_quinn_dt114 with dissolve
vi "Another dealer."
scene ep10_quinn_dt118 with dissolve
bd "I'm listening."
scene ep10_quinn_dt114 with dissolve
vi "How much do you trust her?"
scene ep10_quinn_dt119 with dissolve
bd "Quinn?"
scene ep10_quinn_dt114 with dissolve
vi "Yeah."
scene ep10_quinn_dt118 with dissolve
bd "She's my extended family."
scene ep10_quinn_dt115 with dissolve
vi "Yeah?"
vi "Is that why Mick's watching her?"
scene ep10_quinn_dt119 with dissolve
bd "What do you think you know about Mick?"
scene ep10_quinn_dt115 with dissolve
vi "That he's not as covert as you think he is."
scene ep10_quinn_dt118 with dissolve
bd "Like I said, Quinn's my extended family."
bd "And I trust her as much as I trust my own mother."
scene ep10_quinn_dt120 with dissolve
bd "Which is nothing."
scene ep10_quinn_dt118 with dissolve
bd "But I owe it to Rox. There's no way around it."
scene ep10_quinn_dt115 with dissolve
vi "Noticed any increase in her orders lately?"
scene ep10_quinn_dt119 with dissolve
stop music fadeout 3
bd "What exactly do you know?"
scene ep10_quinn_dt116 with dissolve
$ renpy.pause()

if branchAlone and ep8_quinn_lewd:
    $ new_bio("Vinny", "Vinny tried to get under my skin when I was waiting for Quinn to finish her business with her uncle Buddy.")
    if ep10_quinn_help and ep8_mansion_won:
        jump ep10_quinn_lewd_label
    else:
        if ep10_quinn_help:
            $ new_bio("Quinn", "Quinn told me she was selling drugs and about how she does it. She used my company as protection without letting me know, and I told her I would have done it even if she asked.")
        else:
            $ new_bio("Quinn", "Quinn told me she was selling drugs and about how she does it. She used my company as protection without letting me know, and I told her I didn't want to be a part of it.")
        jump ep10_freeroam_room1_label
else:
    jump ep10_freeroam_room1_label

label ep10_quinn_lewd_label:
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

hide screen new_phone_screen
play music "music/ep10/licensed_music/track142.mp3"
$ ep10_quinn_lewd = True
scene ep10_quinn_lewd1 with dissolve
mc "Do you want me to park back here?"
scene ep10_quinn_lewd2 with dissolve
qu "This spot is perfect."
scene ep10_quinn_lewd3 with dissolve
mc "For what?"
play sound "sound_effects/season3/car_recline.mp3"
scene ep10_quinn_lewd4 with dissolve
mc "Oh?"
scene ep10_quinn_lewd5 with dissolve
qu "Whip it out for me."
scene anim_quinn_hj_ep10 with dissolve
mc "We're gonna do this in an alley?"
qu "Are you scared?"
mc "No, but I'm surprised. I thought you were taking me to some other place you had to go."
qu "I figured since we're done for tonight, we could end it in the way we do it best."
pause
scene anim_quinn_bj_ep10 with dissolve
mc "Oh, God... You're dirty."
qu "*{i}Suck suck{/i}* And you love it."
pause

scene ep10_quinn_lewd6 with dissolve
qu "What's wrong? Never done it in an alley before?"
scene ep10_quinn_lewd7 with dissolve
mc "No. And neither in a sports car."
scene ep10_quinn_lewd6 with dissolve
qu "Let's pop those cherries, then."
qu "The driver's seat reclines for this reason."
scene ep10_quinn_lewd8 with dissolve
mc "Rusty's gonna kill me."
scene ep10_quinn_lewd9 with dissolve
qu "Haha, you'll be fine. Don't shoot your load on the leather seats and he won't even know we did this."
scene ep10_quinn_lewd10 with dissolve
qu "Fuck... *{i}Moans{/i}*"
qu "Get in there... All the way in there."
scene anim_quinn_ride1_ep10 with dissolve
mc "You're so fucking naughty, you little slut."
qu "Yes, I'm a slut. Your little fuck slut."
pause
play sound "sound_effects/slap.mp3"
scene ep10_quinn_lewd11 with vpunch
mc "Ride me, [quinn]."
scene anim_quinn_ride2_ep10 with dissolve
qu "You like it dirty, don't you?"
mc "I fucking love it dirty."
qu "Uh-huh. Called it."
pause
$ tmpInt = 0
label ep10_quinn_lewd_loop_label:

menu:
    "Doggystyle":
        $ tmpInt += 1
        scene anim_quinn_doggy1_ep10 with dissolve
        qu "Shove that dick inside of me, [mc_quinn]. Don't you dare hold back on me."
        pause
        jump ep10_quinn_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_quinn_miss1_ep10 with dissolve
        pause
        scene anim_quinn_miss2_ep10 with dissolve
        pause
        scene anim_quinn_miss3_ep10 with dissolve
        pause
        jump ep10_quinn_lewd_loop_label
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_quinn_rev1_ep10 with dissolve
        qu "Put it in my ass... *{i}Moans{/i}*"
        pause
        scene anim_quinn_rev2_ep10 with dissolve
        pause
        scene anim_quinn_rev3_ep10 with dissolve
        pause
        jump ep10_quinn_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_quinn_ride1_ep10 with dissolve
        pause
        scene anim_quinn_ride2_ep10 with dissolve
        pause
        jump ep10_quinn_lewd_loop_label
    "Cum" if tmpInt > 2:
        menu:
            "Facial":
                scene anim_quinn_cum_ep10 with dissolve
                pause
                scene ep10_quinn_lewd22 with dissolve
                $ renpy.pause()
            "On ass":
                scene anim_quinn_doggy1_ep10 with dissolve
                pause
                scene ep10_quinn_lewd15 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_quinn_lewd15 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_quinn_lewd15 at vpunch, cum2
                $ renpy.pause()
                scene ep10_quinn_lewd16 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_quinn_miss2_ep10 with dissolve
                pause
                scene ep10_quinn_lewd12 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_quinn_lewd12 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_quinn_lewd12 at vpunch, cum1
                $ renpy.pause()
                scene ep10_quinn_lewd13 with dissolve
                $ renpy.pause()
                scene ep10_quinn_lewd14 with dissolve
                $ renpy.pause()

scene ep10_quinn_lewd17 with dissolve
mc "This was wild..."
scene ep10_quinn_lewd18 with dissolve
qu "It sure was fun, babe."
scene ep10_quinn_lewd17 with dissolve
mc "We should do this more often."
scene ep10_quinn_lewd18 with dissolve
qu "I would have done it earlier with you if I knew you were up for it."
scene ep10_quinn_lewd20 with dissolve
mc "We fucked on a rooftop. Wasn't that enough for you to know?"
scene ep10_quinn_lewd19 with dissolve
qu "Yeah, but you were high. Didn't think you had this in you sober."
qu "You're a kinky fucker, aren't you?"
scene ep10_quinn_lewd20 with dissolve
mc "Says you."
scene ep10_quinn_lewd21 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep10_lewd_quinn = True
$ calcScenes()
$ new_bio("Vinny", "Vinny tried to get under my skin when I was waiting for Quinn to finish her business with her uncle Buddy.")
$ new_bio("Quinn", "Quinn told me she was selling drugs and about how she does it. She used my company as protection without letting me know and I told her I would have done it even if she asked.")
$ mphone_stats_add_girl_s3("quinn","You had sex with Quinn in Rusty's car in episode 10.")
show screen new_phone_screen
stop music fadeout 3
$ mgallery_add_photo("ep10_quinn_solo_pic1")
jump ep10_freeroam_room1_label

label ep10_tq_label:
play music "music/ep3/get_back.mp3"
scene ep10_tq1 with wipeleft
$ renpy.pause()
scene ep10_tq2 with dissolve
ti "Hey, Tommy. Thanks again for hosting that awesome Halloween party. I can't remember the last time I had that much fun!"
scene ep10_tq3 with dissolve
tm "No problem. I bet it was fun; I heard you let your girls out again."
scene ep10_tq6 with dissolve
ti "I don't know what you're talking about."
scene ep10_tq8 with dissolve
gi "She sure did. She made me chase her half-nude through your mansion."
scene ep10_tq6 with dissolve
ti "Haha, whatever! I was drunk."
scene ep10_tq3 with dissolve
tm "Don't ever excuse yourself for that. No one that matters would complain about it."
scene ep10_tq4 with dissolve
tm "I was gonna ask you. The posters on campus, what do you know about them?"
scene ep10_tq7 with dissolve
ti "The DIK posters?"
scene ep10_tq4 with dissolve
tm "No, the ones advertising the chess club. Yes, the fucking DIK posters."
scene ep10_tq6 with dissolve
ti "Everyone's talking about them. They're hilarious!"
ti "People knew you guys were crazy, and they're laughing at the shit you're doing."
scene ep10_tq8 with dissolve
gi "Who's that guy with the big dick? Depending on who you ask, they say it's you, Leon or [name]."
scene ep10_tq6 with dissolve
if ep9_tiffani_gina_tara:
    ti "I can see it being [name]. I definitely felt something big against my leg when we slept next to him."
    if not ep9_body_shots_becky and ep9_body_shots:
        ti "Also, I got a close look at his crotch during that shot battle. And I don't think it was the costume."
elif not ep9_body_shots_becky and ep9_body_shots:
    ti "I can see it being [name]. I got a close look at his crotch during that shot battle. And I don't think it was the costume."
else:
    ti "I heard it was fake."
scene ep10_tq4 with dissolve
tm "Meh, who cares? I wanna know who's posting them."
scene ep10_tq7 with dissolve
ti "We don't know."
scene ep10_tq5 with dissolve
tm "Nobody fucking knows anything. But someone does. Can you help out?"
scene ep10_tq6 with dissolve
ti "I can ask around, sure."
if ep9_josy_choice != "CHICK":
    scene ep10_tq7 with dissolve
    ti "And, oh! Tara's mad at you."
    scene ep10_tq5 with dissolve
    tm "I don't give a fuck if she is."
    scene ep10_tq7 with dissolve
    ti "I'm just saying."
scene ep10_tq9 with dissolve
$ renpy.pause()
scene ep10_tq10 with dissolve
qu "I'm late, I know. Something came up."
scene ep10_tq11 with dissolve
tm "Problems?"
scene ep10_tq12 with dissolve
qu "When are there none?"
scene ep10_tq11 with dissolve
tm "Need my help?"
scene ep10_tq12 with dissolve
qu "You can't help with this."
scene ep10_tq13 with dissolve
qu "What did Tiff and Gina want?"
scene ep10_tq17 with dissolve
tm "Nothing. I asked them about the posters."
scene ep10_tq14 with dissolve
qu "Those posters prove that you can't trust anyone here."
qu "This campus is a ground-zero cesspool of backstabbing cunts."
scene ep10_tq17 with dissolve
tm "Yeah, and I'm getting the blame for this one. I mean, yeah, I put those pictures on that wall, but is this my fault?"
tm "My brothers are acting butthurt about it."
scene ep10_tq14 with dissolve
qu "No, it's not your fault."
qu "You throw a big ass party for people and this is how they repay you? Fucking scum."
qu "I'll do some digging for you if you want."
scene ep10_tq17 with dissolve
tm "The boys want it, yeah."
scene ep10_tq13 with dissolve
qu "It's done."
scene ep10_tq15 with dissolve
qu "So... A question for your ears only..."
qu "Can I trust Lily?"
scene ep10_tq16 with dissolve
tm "With...?"
scene ep10_tq15 with dissolve
qu "I'm selling to her."
scene ep10_tq16 with dissolve
tm "I know. That's it? You can trust her with that."
scene ep10_tq15 with dissolve
qu "It's more in general. You know, with information and such."
scene ep10_tq13 with dissolve
qu "She's been helping me sell to her stripper friends."
qu "I need to know if she's putting middleman prices on that or not."
scene ep10_tq17 with dissolve
tm "I wouldn't know anything about that, but I don't think she would."
scene ep10_tq13 with dissolve
qu "And I think she would. She's sneaky."
scene ep10_tq17 with dissolve
tm "Those girls are tight as fuck. I doubt she'd use them like that."
tm "And with stripping for a living, she definitely doesn't need more money. Trust me on this."
tm "I think she's just looking to score cheap weed and not get fucked over with the prices she pays for it."
scene ep10_tq15 with dissolve
qu "Ok. Cool."
stop music fadeout 3
qu "I gotta bounce."
scene ep10_tq18 with dissolve
$ renpy.pause()

if branchJill and ep9_told_jill:
    jump ep10_jb_label
elif branchIsabella:
    jump ep10_bsolo_label

label ep10_zoey_hangout_label:
if not ep10_zoey_hangout:
    scene ep10_pre_diary1 with fade
    $ renpy.pause()
    scene ep10_pre_diary2 with dissolve
    $ renpy.pause()
    jump ep10_diary_label
$ guideSuggestedPage = 122
scene ep10_zoey_hangout1 with fade
play music "music/ep_interlude/licensed_music/track108.mp3"
$ renpy.pause()
scene ep10_zoey_hangout2 with dissolve
zo "Haha! I swear these Halloween pictures are the best thing ever."
zo "People look drunk as hell in them, and then there's this awesome totally serious post-processing that Jacob did."
scene ep10_zoey_hangout3 with dissolve
zo "I get the feeling that it's a professional doing his job, even though the time could be spent on something better."
zo "And I fucking love it. Mine came out awesome!"
scene ep10_zoey_hangout4 with dissolve
mc "I didn't realize how many had their picture taken. I thought I was busy getting people to pose for the camera, but it seems like Elena did most of the work."
scene ep10_zoey_hangout3 with dissolve
zo "Haha! Did you see the one of Leon?"
scene ep10_zoey_hangout5 with dissolve
mc "Do you know who Leon is?"
scene ep10_zoey_hangout3 with dissolve
zo "It's the guy dressed as the girl with the pigtails, right?"
scene ep10_zoey_hangout5 with dissolve
mc "Yeah, it is."
scene ep10_zoey_hangout6 with dissolve
zo "Look at this picture! Jacob definitely knew what he was doing with it."

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Quinn path)","(-Isabella)","(-DIK)","(+DIK)"," ","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if not branchAlone:
                        $mod_choices[4]="(+Cheater)"
                    elif branchAlone and wt_ep9_branch_numbers != 1:
                        $mod_choices[4]="(+Cheater)"
menu:
    "Look at picture [m_c1][mod_choices[2]]":
        $ dk(-1)
    "Look at Zoey [m_c1][mod_choices[3]][m_c2][mod_choices[4]]":
        $ dk(1)
        if not branchAlone:
            $ tc += 1
        elif branchAlone and wt_ep9_branch_numbers != 1:
            $ tc += 1
        scene ep10_zoey_hangout7 with dissolve
        zo "What do you think?"
        mc "Um..."
scene ep10_zoey_hangout8 with dissolve
menu:
    "That's funny [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Yeah, that's funny as hell. At least to everyone but Leon."
        mc "It's not bullying, is it?"
        zo "Bullying? If he put on that costume for Halloween, he was begging for it."
    "Poor Leon [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Poor Leon... He thought it was a funny idea, but boy, did it backfire on him."
        zo "Do you feel bad for him?"
        if affinity == "DIK":
            mc "Not really, but he's gotten a lot of shit for it. Mainly from me. Haha!"
        else:
            mc "A little bit, yeah."

if ep9_photos[14]:
    scene ep10_zoey_hangout8b with dissolve
    zo "This pic is my favorite. It looks as awesome as I imagined it would."
    mc "Yeah, we nailed it. We don't even look drunk!"
    zo "Haha!"

if branchJill:
    scene ep10_zoey_hangout8c with dissolve
    zo "Cute picture. Who's the banana?"
    mc "That's my girlfriend, Jill."
    scene ep10_zoey_hangout9 with dissolve
    zo "No way."
    scene ep10_zoey_hangout10 with dissolve
    mc "Yep. It's pretty fresh and not public yet, but it feels good."
    scene ep10_zoey_hangout11 with dissolve
    zo "That's rad..."
if branchSage:
    if ep9_photos[10]:
        scene ep10_zoey_hangout8d with dissolve
    else:
        scene ep10_zoey_hangout8e with dissolve
    zo "She's hot. Sage, right?"
    mc "Yeah, that's Sage. We're dating."
    scene ep10_zoey_hangout9 with dissolve
    zo "You are?"
    scene ep10_zoey_hangout10 with dissolve
    mc "Yeah. I mean, we haven't dated yet, but almost."
    scene ep10_zoey_hangout11 with dissolve
    zo "You almost date, then."
if branchIsabella:
    if ep9_photos[2]:
        scene ep10_zoey_hangout8f with dissolve
    else:
        scene ep10_zoey_hangout8g with dissolve
    zo "Who's this?"
    mc "Just a mummy."
    zo "Ah. I thought it was someone you knew."
if branchMayaJosy:
    if ep9_photos[5]:
        scene ep10_zoey_hangout8h with dissolve
    else:
        scene ep10_zoey_hangout8i with dissolve
    zo "You're such a chick magnet."
    mc "Haha, maybe."
    zo "I told a sexually inappropriate joke to the short one."
    mc "Josy?"
    zo "Is that her name?"
    mc "Yeah."
    zo "And the other one?"
    mc "That's Maya."
    zo "Are they good friends of yours?"
    mc "You can say that."
    scene ep10_zoey_hangout12 with dissolve
    zo "What's that supposed to mean?"
    scene ep10_zoey_hangout13 with dissolve
    mc "We're dating."
    scene ep10_zoey_hangout12 with dissolve
    zo "You and Maya? Or Josy?"
    scene ep10_zoey_hangout13 with dissolve
    mc "Both."
    scene ep10_zoey_hangout9 with dissolve
    zo "Whoa! Please, tell me they know about each other."
    scene ep10_zoey_hangout10 with dissolve
    mc "Yeah. It's weird to talk about, but it's started to spread and I don't think it will be a secret for long."
    scene ep10_zoey_hangout12 with dissolve
    zo "Hey, you know me. My lips are sealed."
    scene ep10_zoey_hangout11 with dissolve
    zo "Two girlfriends, though... That one I didn't see coming."
if ep9_photos[7] or ep9_photos[8]:
    if ep9_photos[7]:
        scene ep10_zoey_hangout8j with dissolve
    else:
        scene ep10_zoey_hangout8k with dissolve
    zo "This picture, though..."
    mc "Haha, yeah? What about it?"
    zo "What about it? Really? You seem to be enjoying college."
    scene ep10_zoey_hangout14 with dissolve
    mc "I definitely am."
    scene ep10_zoey_hangout16 with dissolve
    zo "*{i}Cough{/i}* Slut! *{i}Cough{/i}*"
    scene ep10_zoey_hangout14 with dissolve
    mc "She's not a slut."
    scene ep10_zoey_hangout15 with dissolve
    zo "I meant you are."
    scene ep10_zoey_hangout14 with dissolve
    mc "Oh... Come on, everyone has an inner slut we need to let out at times."
    if ep9_photos[16] or ep9_photos[17]:
        if ep9_photos[16]:
            scene ep10_zoey_hangout8l with dissolve
        else:
            scene ep10_zoey_hangout8l2 with dissolve
        zo "You sure let that slut out that night."
        mc "Yeah, I was thirsty."
    else:
        scene ep10_zoey_hangout15 with dissolve
        zo "Haha!"

scene ep10_zoey_hangout17 with dissolve
$ renpy.pause()
scene ep10_zoey_hangout18 with dissolve
zo "You have way too many books in here."
mc "And funny enough, it's not even half of what it used to be."
zo "Do you even read any of these?"
scene ep10_zoey_hangout19 with dissolve
mc "Nope. They're pretty much decorative only."
mc "The only books I read these days are class literature."
mc "Oh...and my Mom's diary."
play sound "sound_effects/shove.mp3"
scene ep10_zoey_hangout20 with vpunch
zo "Shut up!"
mc "Yeah, I know."
zo "You gotta show me that!"
scene ep10_zoey_hangout21 with dissolve
mc "Here it is."
scene ep10_zoey_hangout22 with dissolve
zo "Where the hell did you even get it?"
scene ep10_zoey_hangout23 with dissolve
mc "On my birthday, I got a box of her things and an inheritance... $5000."
scene ep10_zoey_hangout22 with dissolve
zo "On your birthday? Why?"
scene ep10_zoey_hangout23 with dissolve
mc "I don't know why, but that's when I got it."
mc "I believe it's her last diary. Dad told me she wrote a lot."
mc "And I get to experience her life through it... It's pretty amazing."
if not zoey_dik:
    scene ep10_zoey_hangout24 with dissolve
    zo "Dude... You're gonna make me cry over here."
    play sound "sound_effects/hit.mp3"
    scene ep10_zoey_hangout28 with hpunch
    $ renpy.pause()
    scene ep10_zoey_hangout25 with dissolve
    mc "You are a softie now."
    scene ep10_zoey_hangout26 with dissolve
    zo "Haha, shut up! I'm not a softie. But this is your Mom's diary!"
else:
    scene ep10_zoey_hangout27 with dissolve
    zo "This is your Mom's diary!"
zo "It's huge!"
scene ep10_zoey_hangout29 with dissolve
zo "From not knowing a lot about her to having access to her actual fucking outlet..."
zo "I know how I treat my notebook; if it's anything like it, this is the best birthday gift you could have gotten."
mc "That's exactly the way I feel about it. It's a gift that keeps giving..."
mc "What I do is I read a few pages at a time, and then I put it away for a while."
scene ep10_zoey_hangout30 with dissolve
mc "I don't wanna rush through it. To me, it feels like she's still filling it with her daily stories."
mc "Like, I get to read what just happened. And I'm living alongside it."
mc "Maybe that doesn't make much sense."
scene ep10_zoey_hangout31 with dissolve
zo "Can you read some for me?"
scene ep10_zoey_hangout32 with dissolve
mc "..."
scene ep10_zoey_hangout31 with dissolve
zo "I totally get it if you don't want to. But I'm dying to find out how she was."
zo "And I wanna see if there are any uncanny resemblances between you two."
scene ep10_zoey_hangout30 with dissolve
mc "Ok... I'll read a few pages with you."
scene ep10_zoey_hangout33 with dissolve
$ renpy.pause()
scene ep10_zoey_hangout34 with dissolve
zo "I'm so excited... What's happened until now?"
scene ep10_zoey_hangout35 with dissolve
mc "Oh... She's moved to a big place they're turning into a hotel."
mc "They are in the midst of renovations and she doesn't like it there one bit, and Dad's working there."
scene ep10_zoey_hangout34 with dissolve
zo "That's how they met, right?"
scene ep10_zoey_hangout35 with dissolve
mc "Yeah. And last time I read it, he asked her out on a date, but she kinda turned him down because he's been annoying her with the construction noise."
scene ep10_zoey_hangout36 with dissolve
zo "Hahaha! No way!"
stop music fadeout 3
scene ep10_zoey_hangout37 with dissolve
mc "Ok. Here goes..."

label ep10_diary_label:
$ guideSuggestedPage = 123
play music "music/ep10/licensed_music/track143.mp3"
scene ep10_diary1 with dissolve
$ renpy.pause(2)
scene ep10_diary2 with dissolve
$ renpy.pause()
scene ep10_diary3 with dissolve
$ renpy.pause()
play sound "sound_effects/thud.mp3"
scene ep10_diary4 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/season2/truck.mp3"
ln "Here we go again..."
play sound "sound_effects/shower_curtain.mp3"
scene ep10_diary5 with hpunch
$ renpy.pause()
scene ep10_diary8 with dissolve
$ renpy.pause()
scene ep10_diary9 with dissolve
$ renpy.pause()
scene ep10_diary6 with dissolve
$ renpy.pause()
play sound "sound_effects/shower_curtain.mp3"
scene ep10_diary7 with hpunch
$ renpy.pause()
scene ep10_diary10 with dissolve
ln "Dear diary."
ln "They are still doing it."
$ renpy.sound.play("sound_effects/shower.mp3", channel="sfx1", loop=False)
scene ep10_diary11 with dissolve
ln "Every day. Amazingly, it keeps getting louder and louder."
scene ep10_diary12 with dissolve
ln "I'm now at that point where I'm seriously considering changing my sleeping schedule to avoid the daily heart attack-inducing wake-up calls."
scene ep10_diary13 with dissolve
ln "And I might have to install a lock in my room, too. This...thing...happened with that annoying guy I wrote about."
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep10_diary14 with dissolve
play sound "sound_effects/season3/hairdryer.mp3"
$ renpy.pause()
scene ep10_diary15 with dissolve
$ renpy.pause()
scene ep10_diary16 with dissolve
$ renpy.pause()
scene ep10_diary17 with dissolve
ln "Ahhh..."
dad "Oh no."
scene ep10_diary18 with vpunch
ln "*{i}Screams{/i}* Ahh!!!"
scene ep10_diary19 with dissolve
dad "I'm so sorry! I knocked!"
scene ep10_diary21 with dissolve
ln "You knocked!? Does that permit you to enter my room!?"
ln "I wasn't even in here! What the hell is wrong with you!?"
scene ep10_diary20 with dissolve
dad "I'm so sorry! I'm such an idiot!"
dad "I just wanted to see you."
scene ep10_diary21 with dissolve
ln "Yeah, you've seen me, alright!"
scene ep10_diary22 with dissolve
dad3 "Honey? Are you ok?"
scene ep10_diary23 with dissolve
ln "Oh my God! Hide!"
scene ep10_diary24 with dissolve
ln "Not there! In the closet! He's coming from that door."
scene ep10_diary25 with dissolve
dad "You have too much crap in here!"
scene ep10_diary26 with dissolve
dad3 "What's up with the commotion?"
ln "Dad! I'm not decent."
dad3 "I heard yelling."
play sound "sound_effects/season3/door_squeek.mp3"
scene ep10_diary27 with dissolve
ln "Oh, that? It was just...you know... Those damn idiot workers!"
ln "They are utterly incompetent!"
ln "They keep waking me up and making all that noise, which gets on my nerves."
scene ep10_diary28 with dissolve
dad3 "I understand, honey. But you'll have to find a way to tolerate it. This will be our life for the next few months."
dad3 "After the construction crew finishes demolition, it will settle down with the heavy machinery."
scene ep10_diary30 with dissolve
dad3 "But you'll have to get used to it being people in here, running about."
scene ep10_diary29 with dissolve
ln "Oh, they are running about. Like freaking toddlers exploring every nook and cranny!"
scene ep10_diary28 with dissolve
dad3 "Are they disturbing you in other ways, too? I can have a chat with them."
scene ep10_diary29 with dissolve
ln "No. I will give them an earful later, believe you me."
scene ep10_diary28 with dissolve
dad3 "Get dressed and join your mother for breakfast. I'll be heading out shortly."
scene ep10_diary29 with dissolve
ln "Yes, Dad."
scene ep10_diary31 with dissolve
$ renpy.pause()
dad "You did great."
scene ep10_diary32 with dissolve
$ renpy.pause()
scene ep10_diary33 with dissolve
ln "What the hell is wrong with you!?"
scene ep10_diary34 with dissolve
dad "I know you want to give me an earful, but he's still within earshot. So..."
dad "Thanks for covering for me... I don't know why you did that, but I appreciate it."
scene ep10_diary35 with dissolve
ln "Don't flatter yourself."
ln "If I didn't do that, you would be leaving through a hole in the wall like that wrecking ball of yours."
scene ep10_diary36 with dissolve
ln "And trust me, we have enough ruined walls in our home."
scene ep10_diary35 with dissolve
ln "You could at least have the decency to look at me when I scold you!"
scene ep10_diary37 with dissolve
dad "I would, but I can still kinda see your tit."
scene ep10_diary38 with dissolve
ln "*{i}Gasp{/i}* Argh!"
dad "I'll leave and let you put on some clothes."
scene ep10_diary39 with dissolve
ln "Hell no! I'm not done with you. You're not going anywhere until I get some answers."
scene ep10_diary36 with dissolve
ln "Didn't I tell you to look at me!?"
scene ep10_diary37 with dissolve
dad "Again... I'd do it... But when you pulled your towel up..."
scene ep10_diary41 with dissolve
dad "...you kinda exposed your hoo-ha."
scene ep10_diary40 with dissolve
$ renpy.pause()
scene ep10_diary42 with vpunch
ln "Oh my God!!! Turn around!"
scene ep10_diary43 with dissolve
dad "I wasn't planning on embarrassing you like this, just so that you know."
scene ep10_diary45 with dissolve
ln "You certainly have a talent for it!"
scene ep10_diary44 with dissolve
dad "I'd compliment you, but I'm afraid it would come off creepy."
scene ep10_diary46 with dissolve
ln "Great, you almost know when to shut your mouth."
scene ep10_diary47 with dissolve
dad "You have a very fit body."
scene ep10_diary48 with dissolve
ln "Will you shut up!?"
scene ep10_diary49 with dissolve
ln "Now, tell me what you're doing in here."
scene ep10_diary50 with dissolve
dad "Now? Don't you want to put on more clothes?"
scene ep10_diary49 with dissolve
ln "Does it matter? You've already seen me in my full glory. \"Hoo-ha\" and everything."
scene ep10_diary51 with dissolve
dad "You're extremely pretty."
scene ep10_diary52 with dissolve
ln "FYI, I'm this close to kicking you in the nuts."
scene ep10_diary51 with dissolve
dad "I'm so sorry! This wasn't how it was supposed to go."
dad "I was coming up here to talk to you. I haven't been able to stop thinking about you since we met downtown."
scene ep10_diary53 with dissolve
ln "..."
scene ep10_diary57 with dissolve
dad "And I wanted to give you this."
dad "It's just a small gift - something to apologize for all the noise we're making."
scene ep10_diary58 with dissolve
ln "What is it?"
scene ep10_diary59 with dissolve
dad "Earplugs."
scene ep10_diary58 with dissolve
ln "Earplugs?"
scene ep10_diary54 with dissolve
dad "The best earplugs you can find. Trust me, they might not make you completely deaf, but they should help you get your beauty sleep."
dad "Which, if I might add, you don't need a lot of."
scene ep10_diary56 with dissolve
ln "Ugh."
scene ep10_diary55 with dissolve
ln "Earplugs? Is that why you had to enter my room?"
scene ep10_diary54 with dissolve
dad "The earplugs were the conversation starter. I was going to ask you out on a date, but before I could do that, you showed up naked."
dad "Haha! Which is, ironically, what a good date would lead to."
scene ep10_diary53 with dissolve
ln "..."
dad "I sense that I should leave."
scene ep10_diary60 with dissolve
dad "I'm leaving."
scene ep10_diary61 with dissolve
$ renpy.pause()
scene ep10_diary62 with dissolve
dad "Where did we land on that date?"
play sound "sound_effects/door_close.mp3"
scene ep10_diary63 with dissolve
dad "Well... You know where to find me. Just follow the noise."

scene ep10_diary65 with dissolve
ln "Mom warned me that it would feel exposed to live in the house while construction workers were here..."
ln "...but not in my wildest guesses did I think this is what she meant."
ln "Earplugs. Pff! A date? Pfff!!!"
ln "I have no interest in dating that guy at all. EVER!"

scene ep10_diary64 with fade
ln "Dear diary..."
ln "It's 9 a.m."
ln "Yes, that's right. 9 freaking a.m.!"
scene ep10_diary66 with dissolve
ln "I thought I had woken up early, but that wasn't the case."
play sound "sound_effects/season2/truck.mp3"
scene ep10_diary67 with dissolve
ln "What the hell?"
scene ep10_diary68 with dissolve
ln "Earplugs! These wonderful earplugs! How is it possible?"
ln "They're so small, yet they stop big noise from disturbing my \"not needed\" beauty sleep. Haha!"
play sound "sound_effects/shower_curtain.mp3"
scene ep10_diary69 with hpunch
$ renpy.pause()
scene ep10_diary72 with dissolve
$ renpy.pause()
scene ep10_diary70 with dissolve
$ renpy.pause()
scene ep10_diary71 with dissolve
$ renpy.pause()

scene ep10_diary73 with dissolve
$ renpy.pause()
scene ep10_diary74 with dissolve
$ renpy.pause()
scene ep10_diary75 with dissolve
$ renpy.pause()
scene ep10_diary76 with dissolve
$ renpy.pause()
scene ep10_diary77 with dissolve
$ renpy.pause()
scene ep10_diary80 with dissolve
dad "Lynette?"
scene ep10_diary78 with dissolve
ln "Oh! It's you. I didn't see you there."
scene ep10_diary79 with dissolve
dad "Sure you did. I saw you look in my direction."
scene ep10_diary78 with dissolve
ln "I wasn't looking at you. I was looking at...at..."
ln "Something else!"
scene ep10_diary79 with dissolve
dad "Something else?"
scene ep10_diary78 with dissolve
ln "Yeah! So what?"
ln "Err... What do you want?"
scene ep10_diary81 with dissolve
dad "I wanted to apologize again for the other day."
dad "I won't enter your room ever again without your permission."
scene ep10_diary82 with dissolve
ln "Good."
scene ep10_diary83 with dissolve
dad "Have a nice evening."
scene ep10_diary82 with dissolve
ln "That's it?"
scene ep10_diary83 with dissolve
dad "Sorry?"
scene ep10_diary84 with dissolve
ln "You usually have more things to say than that."
scene ep10_diary85 with dissolve
dad "Call me crazy, but when a woman stares at me angrily, it doesn't scream, \"Stay and talk to me\"."
ln "..."
scene ep10_diary84 with dissolve
ln "Thank you for the earplugs."
scene ep10_diary85 with dissolve
dad "Oh, you're welcome. How are they?"
scene ep10_diary84 with dissolve
ln "Annoying at first, but once I fell asleep, I slept well throughout the night."
ln "And I didn't hear you this morning, either."
scene ep10_diary85 with dissolve
dad "That's great. I'm happy you like them."
scene ep10_diary86 with dissolve
ln "Are you off work now or...?"
scene ep10_diary85 with dissolve
dad "Yeah, I'm heading back into town to my room."
scene ep10_diary86 with dissolve
ln "Ok..."
scene ep10_diary85 with dissolve
dad "..."
dad "Wanna come with?"
scene ep10_diary87 with dissolve
ln "To your room?"
scene ep10_diary88 with dissolve
dad "No. Into town. We could eat dinner together if you'd like."
scene ep10_diary87 with dissolve
ln "I'm not that hungry."
scene ep10_diary88 with dissolve
dad "That's perfect. I don't have too much money to spend on food."
scene ep10_diary89 with dissolve
ln "..."
dad "How about it? A car ride and a hot dog?"
scene ep10_diary90 with dissolve
ln "Will you bring me back here after?"
scene ep10_diary89 with dissolve
dad "You got it."
scene ep10_diary91 with dissolve
ln "So... What kind of a hot dog are we having?"
scene ep10_diary92 with dissolve
dad "Any kind you like. Mustard?"
show ep10_diary93
if not persistent.ep10_cardzo7:
    show screen ep10_render_screen("zo7")
with dissolve
ln "Yuck."
dad "Yuck? You're a weirdo."
ln "Excuse me?"
stop music fadeout 5
dad "You can't eat hot dogs without mustard. That's like eating cake without beer."
ln "Who drinks beer with cake? Are you for real?"
if not ep10_zoey_hangout:
    jump ep10_yoga_label

label ep10_zoey_hangout2_label:
play music "music/ep_interlude/licensed_music/track108.mp3"
show ep10_zoey_hangout38
hide screen ep10_render_screen
with dissolve
zo "She is totally digging him!"
scene ep10_zoey_hangout37 with dissolve
mc "She is, isn't she?"
scene ep10_zoey_hangout38 with dissolve
zo "That's hilarious, dude. Did Neil ever tell you that story?"
scene ep10_zoey_hangout37 with dissolve
mc "That he saw her naked? No. He never told me that."
mc "It was awkward to read this."
scene ep10_zoey_hangout39 with dissolve
mc "But he did tell me that he got her earplugs, so he must have spared me those details."
scene ep10_zoey_hangout40 with dissolve
zo "Is it me or does she complain a lot?"
scene ep10_zoey_hangout41 with dissolve
mc "She does. She's 18, right? And she doesn't sound like she's in a happy place in life, having to move away from her best friends and all."
mc "I think that's the reason why she's moody."
scene ep10_zoey_hangout40 with dissolve
zo "Still, I can't believe this is her diary... I'm so happy for you."
scene ep10_zoey_hangout39 with dissolve
mc "Thanks, Zoey... I knew you'd understand how much it means to me. I didn't even have to explain it to you."
scene ep10_zoey_hangout42 with dissolve
$ renpy.pause(1)
scene ep10_zoey_hangout42b with dissolve
$ renpy.pause()
scene ep10_zoey_hangout43 with dissolve
$ renpy.pause()
scene ep10_zoey_hangout44 with dissolve
zo "Thanks for letting me hang out here. I needed it."
zo "I think I'm gonna bounce."
scene ep10_zoey_hangout45 with dissolve
mc "Um... Barbecue."
scene ep10_zoey_hangout44 with dissolve
zo "What?"
scene ep10_zoey_hangout45 with dissolve
mc "We're having a barbecue the night before Thanksgiving. If you wanna come, it would be great."
scene ep10_zoey_hangout46 with dissolve
zo "Sounds dope. Shoot me the details later."
scene ep10_zoey_hangout47 with dissolve
mc "Yeah, I'll make sure to do it."
scene ep10_zoey_hangout48 with dissolve
zo "So... See you!"
scene ep10_zoey_hangout49 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep10_zoey_hangout50 with dissolve
$ renpy.pause()
$ new_bio("Zoey", "I hung out with Zoey and showed her Mom's diary. There was an awkward tension between us and she left without talking about it.")

if branchSage and ep9_jm_sad:
    jump ep10_sage_mj_label
elif ep9_jm_sad:
    jump ep10_sage_mj2_label

label ep10_yoga_label:
play music "music/ep2/by_your_side.mp3"
if branchJill:
    show ep10_yoga1
    hide screen ep10_render_screen
    with fade
    mc "Why did I agree to this?"
    scene ep10_yoga2 with dissolve
    isa "I'd like to think it was because of the opportunity for personal growth, but perhaps it was because it was free this time."
    scene ep10_yoga3 with dissolve
    ji "And it's also fun to do together."
    scene ep10_yoga4 with dissolve
    mc "I don't belong in this class. One position into it and I will stick out like a sore thumb."
    scene ep10_yoga5 with dissolve
    isa "I see beginners here often. Granted, some of them don't return after the initial experience, but several do."
    scene ep10_yoga4 with dissolve
    mc "My gym card normally doesn't cover these classes, so this will likely be a one-and-done for me."
    scene ep10_yoga8 with dissolve
    ji "You can always upgrade it if you enjoy it."
    scene ep10_yoga9 with dissolve
    mc "The Silver membership was already expensive enough."
    if ep9_told_jill:
        scene ep10_yoga12 with dissolve
        mc "How's Bianca doing?"
        scene ep10_yoga8 with dissolve
        ji "Go ahead and ask her."
        scene ep10_yoga9 with dissolve
        mc "She's with Carla now."
        scene ep10_yoga8 with dissolve
        ji "She won't mind."
        scene ep10_yoga13 with dissolve
        mc "Bianca. Carla."
        scene ep10_yoga14 with dissolve
        bia "Aw, [name]."
        scene ep10_yoga15 with dissolve
        bia "I'm so happy to see you."
        scene ep10_yoga16 with dissolve
        mc "Me too."
        scene ep10_yoga17 with dissolve
        menu:
            "Hug Carla":
                mc "Hey, Carla. Are you a hugger, too?"
                scene ep10_yoga18 with dissolve
                car "Haha! Sure am."
            "Greet Carla":
                mc "Hey, Carla! Nice to see you."
        scene ep10_yoga19 with dissolve
        mc "I missed you at our party."
        scene ep10_yoga20 with dissolve
        car "I heard all about it. I couldn't come because I was busy."
        scene ep10_yoga19 with dissolve
        mc "Maybe next time, then."
        scene ep10_yoga21 with dissolve
        mc "So, Bianca..."
        scene ep10_yoga21b with dissolve
        mc "Um... I wanted to check up on you... How have you been since yesterday?"
        scene ep10_yoga22 with dissolve
        bia "I've been better."
        scene ep10_yoga23 with dissolve
        mc "Is it ok to ask how it went?"
        scene ep10_yoga24 with dissolve
        bia "I threw Matty out of the house."
        bia "You were completely right about him. He admitted everything."
        bia "He even said he wished he'd told me sooner so they could finally be honest about it and be together."
        scene ep10_yoga25 with dissolve
        car "Such a piece of shit. Liv too."
        scene ep10_yoga24 with dissolve
        bia "They deserve each other."
        scene ep10_yoga23 with dissolve
        mc "What an asshole..."
        mc "I'm so sorry for this mess. If I can help you with anything, let me know."
        scene ep10_yoga26 with dissolve
        bia "*{i}Smack{/i}* You already did."
        scene ep10_yoga27 with dissolve
        bia "If it wasn't for you... *{i}Sigh{/i}* It couldn't have been easy for you to take responsibility for his actions. I won't forget that."
        bia "Now, I need to clear my head with some yoga."
        $ new_bio("Bianca", "She thanked me for telling her about Matthew and Olivia.")
elif branchIsabella:
    show ep10_yoga1b
    hide screen ep10_render_screen
    with fade
    mc "Why did I agree to this?"
    scene ep10_yoga2 with dissolve
    isa "Because it's an easy way to spend time together in public."
    scene ep10_yoga4 with dissolve
    mc "Are you sure they won't laugh?"
    scene ep10_yoga5 with dissolve
    isa "I see beginners here often. Granted, some of them don't return after the initial experience, but several do."
    scene ep10_yoga4 with dissolve
    mc "I prefer doing this in private."
    scene ep10_yoga6 with dissolve
    isa "Is it because it's easier to joke around in private?"
    scene ep10_yoga7 with dissolve
    mc "Well, there's that, but also because there's more pressure on me now."
    scene ep10_yoga6 with dissolve
    isa "That's why we're in the back of the class. Fewer people will be watching you do the positions wrong."
    scene ep10_yoga7 with dissolve
    mc "Way to boost my confidence."
    scene ep10_yoga6 with dissolve
    isa "You'll do fine. I'll help you."
    scene ep10_yoga28 with dissolve
    ji "Hey, guys."
    scene ep10_yoga29 with dissolve
    isa "Hi..."
    scene ep10_yoga30 with dissolve
    ji "Yoga, huh?"
    scene ep10_yoga31 with dissolve
    mc "An attempt at it, at least."
    scene ep10_yoga32 with dissolve
    ji "I think you'll get the hang of it soon enough."
    if affinity != "CHICK":
        scene ep10_yoga33 with dissolve
        mc "(Don't look. Don't look.)"
    scene ep10_yoga34 with dissolve
    mc "This is good..."
    scene ep10_yoga35 with dissolve
    isa "Yes. I'm afraid I will scare her away if I talk too much to her. What do you think?"
    scene ep10_yoga34 with dissolve
    mc "Stay casual. She approached us; I think she's trying hard."
    mc "Wanna switch spots?"
    scene ep10_yoga35 with dissolve
    isa "No. This is fine."
    scene ep10_yoga36 with dissolve
    bia "Hi, [name]! Thanks for the party again!"
    scene ep10_yoga37 with dissolve
    mc "Hey! You're welcome. I hope you had fun."
    scene ep10_yoga36 with dissolve
    bia "Oh, I had so much fun! I'd love to come to more of them."
else:
    show ep10_yoga1
    hide screen ep10_render_screen
    with fade
    mc "Why did I agree to this?"
    scene ep10_yoga2 with dissolve
    isa "I'd like to think it was because of the opportunity for personal growth, but perhaps it was because it was free this time."
    scene ep10_yoga4 with dissolve
    mc "I don't belong in this class. One position into it and I will stick out like a sore thumb."
    scene ep10_yoga10 with dissolve
    ji "..."
    scene ep10_yoga5 with dissolve
    isa "I see beginners here often. Granted, some of them don't return after the initial experience, but several do."
    scene ep10_yoga4 with dissolve
    mc "My gym card normally doesn't cover these classes, so this will likely be a one-and-done for me."
    scene ep10_yoga11 with dissolve
    ji "You can always upgrade it if you enjoy it."
    scene ep10_yoga9 with dissolve
    mc "The Silver membership was already expensive enough."
    mc "Do you come here often?"
    scene ep10_yoga11 with dissolve
    ji "Sometimes."
    scene ep10_yoga11b with dissolve
    if ep9_jill_mood == 1:
        mc "(Even after breaking up with her and getting accused of stealing her panties, she's still trying with me...)"
        mc "(It feels weird, but I appreciate that... I hope this means she believes me.)"
    else:
        mc "(It feels weird between us...but at least she's trying. That's good. I hope this means she believes me.)"
    scene ep10_yoga12 with dissolve
    mc "I see that you brought your friends."
    scene ep10_yoga11 with dissolve
    ji "Carla comes here more often than we do."
    scene ep10_yoga38 with dissolve
    bia "Hi, [name]! Thanks again for the party!"
    scene ep10_yoga39 with dissolve
    mc "Hey! You're welcome. I hope you had fun."
    scene ep10_yoga38 with dissolve
    bia "Oh, I had so much fun! I'd love to come to more of them."

scene ep10_yoga53 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Quinn path)","(-Isabella)","(-DIK)","(+DIK)"," ","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchJill and ep9_told_jill:
                        $mod_choices[4]="(+Cheater)"

menu:
    "Look at them [m_c1][mod_choices[3]][m_c2][mod_choices[4]]":
        $ dk(1)
        if branchJill and ep9_told_jill:
            $ tc += 1
        scene ep10_yoga50 with dissolve
        $ renpy.pause()
        scene ep10_yoga51 with dissolve
        $ renpy.pause()
        scene ep10_yoga52 with dissolve
        $ renpy.pause()
    "Focus [m_c1][mod_choices[2]]":
        $ dk(-1)

scene ep10_yoga40 with dissolve
ji "You've got to be kidding me."
mc "No way."
scene ep10_yoga41 with dissolve
ji "Is he going to show up at my yoga classes now? Is it not enough that he does yoga in front of my window every morning?"
scene ep10_yoga42 with dissolve
isa "Don't pay him attention. He thrives on it."
scene ep10_yoga43 with dissolve
ji "That's easier said than done."
scene ep10_yoga44 with dissolve
ji "I didn't expect him to stop existing after I told him off, but neither did I think it would come to this."
scene ep10_yoga45 with dissolve
mc "What can you do about it? Like it or not, he's not doing something wrong."
scene ep10_yoga44 with dissolve
ji "Not doing something wrong? [name], he's doing all these things to annoy me."
scene ep10_yoga43 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(+Bella)","(-DIK)","(+DIK)"," ","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchJill and ep9_told_jill:
                        $mod_choices[4]="(+Cheater)"

menu:
    "Antagonize Tybalt [m_c1][mod_choices[3]][m_c2][mod_choices[0]]":
        $ dk(1)
        $ RPjill += 1
        scene ep10_yoga48 with dissolve
        mc "Tybalt!? I thought that was you. What are you doing here?"
        mc "Are you into yoga too?"
        mc "Oh, wait! I get it. It was free this time, that's probably it, right? I love free things, too. These classes are expensive."
        scene ep10_yoga49 with dissolve
        mc "I forgot to thank you for having me and my friends over for dinner. I enjoyed eating your food and relaxing in your home."
        mc "We must do it again sometime."
        scene ep10_yoga46 with dissolve
        ji "What are you doing?"
        scene ep10_yoga47 with dissolve
        mc "Trust me. This is annoying the hell out of him."
        mc "He was fuming that Sage invited me to their parents' place."
        scene ep10_yoga46 with dissolve
        ji "You don't have to do this."
        scene ep10_yoga47 with dissolve
        mc "He's annoying you; I'm just returning the favor."
        $ new_bio("Tybalt", "I messed with Tybalt during yoga class.")
    "Ignore him [m_c1][mod_choices[2]][m_c4][mod_choices[1]]":
        $ dk(-1)
        $ RPisabella += 1
        scene ep10_yoga45 with dissolve
        mc "Take Bella's advice on this. Ignore him."
        mc "Not that it will do a lot, but we can switch spots if you'd like."
        scene ep10_yoga44 with dissolve
        ji "No, I'll be fine."

if ep9_sarah_melanie_lewd:
    scene ep10_yoga54b with dissolve
else:
    scene ep10_yoga54 with dissolve
sar "Haha, look who it is."
scene ep10_yoga55 with dissolve
ml "Are you into yoga, [name]?"
scene ep10_yoga56 with dissolve
sar "Or is it the chicks in yoga pants that you wanna be into?"
scene ep10_yoga57 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(+Bella)","(-DIK)","(+DIK)"," "," ","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchJill:
                        $mod_choices[4]="(-Jill)"
                    if branchIsabella:
                        $mod_choices[5]="(-Isabella)"


menu:
    "Yoga [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "The yoga, of course."
        scene ep10_yoga56 with dissolve
        sar "Hard doubt on that one."
    "Yoga pants [m_c1][mod_choices[3]][m_c2][mod_choices[4]][m_c4][mod_choices[5]]":
        $ dk(1)
        mc "Definitely the yoga pants."
        if branchJill:
            $ RPjill -= 1
            scene ep10_yoga58 with dissolve
            ji "[name]...?"
            mc "What?"
        if branchIsabella:
            $ RPisabella -= 1
            scene ep10_yoga59 with dissolve
            isa "*{i}Sigh{/i}*"
    "Ignore them":
        scene ep10_yoga56 with dissolve
        sar "Your silence says it all."

scene ep10_yoga60 with dissolve
he "[name]. A word?"
scene ep10_yoga61 with dissolve
mc "What's up?"
scene ep10_yoga62 with dissolve
he "About the Halloween party..."
scene ep10_yoga63 with dissolve
mc "Yeah?"
if ep9_heather_lewd == -1:
    scene ep10_yoga62 with dissolve
    he "I wanted to apologize for how I behaved. You tried to give me advice and I didn't wanna hear what you said."
    scene ep10_yoga63 with dissolve
    mc "Don't sweat it. You were drunk and a bit hurt, I believe."
    scene ep10_yoga62 with dissolve
    he "I wish I could forget that entire night."
    scene ep10_yoga63 with dissolve
    mc "Can I help you somehow?"
    scene ep10_yoga64 with dissolve
    he "No. I wanted to apologize and say thanks. I should have listened to you."
    scene ep10_yoga63 with dissolve
    mc "Are you gonna talk to Tommy about it?"
    scene ep10_yoga64 with dissolve
    he "Yeah, I need to find the right words for it."
    scene ep10_yoga63 with dissolve
    mc "Good luck with it."
    scene ep10_yoga65 with dissolve
    $ renpy.pause()
elif ep9_heather_lewd == 0:
    scene ep10_yoga62 with dissolve
    he "I wanted to apologize for how I behaved. I shouldn't have tried to use you like that."
    scene ep10_yoga63 with dissolve
    mc "No harm done, Heather. You were drunk and felt hurt."
    scene ep10_yoga62 with dissolve
    he "I wish I could forget that entire night."
    scene ep10_yoga63 with dissolve
    mc "Can I help you somehow?"
    scene ep10_yoga64 with dissolve
    he "No. I wanted to apologize. You were right to say no to me."
    scene ep10_yoga63 with dissolve
    mc "Don't worry about it, nothing happened. Ok?"
    scene ep10_yoga65 with dissolve
    $ renpy.pause()
elif ep9_heather_lewd == 1:
    scene ep10_yoga62 with dissolve
    he "I wanted to apologize for how I behaved. I shouldn't have tried to use you like that."
    scene ep10_yoga63 with dissolve
    mc "No harm done, Heather. You were drunk and felt hurt."
    scene ep10_yoga62 with dissolve
    he "I wish I could forget that entire night."
    scene ep10_yoga63 with dissolve
    mc "Can I help you somehow?"
    scene ep10_yoga64 with dissolve
    he "No. I wanted to apologize."
    scene ep10_yoga63 with dissolve
    mc "Don't worry about it, nothing happened. Ok?"
    scene ep10_yoga65 with dissolve
    $ renpy.pause()
elif ep9_heather_lewd == 2:
    scene ep10_yoga62 with dissolve
    he "I wanted to apologize for how I behaved. I used you to get back at Tommy without thinking how it could hurt you."
    scene ep10_yoga63 with dissolve
    mc "..."
    mc "Yeah, I wasn't thinking clearly, either. I mean, I wanted to do it, but I should probably not have done it."
    scene ep10_yoga62 with dissolve
    he "Yeah, Tommy won't be happy about it."
    scene ep10_yoga63 with dissolve
    mc "Fuck... Are you planning on telling him?"
    scene ep10_yoga62 with dissolve
    he "I got you into this by jumping on you like that. It wasn't your choice to start with."
    he "I won't tell him it was you, but I have to talk to him about what I did."
    scene ep10_yoga64 with dissolve
    he "This fucking thing is killing me, [name]."
    he "Him going from girl to girl and thinking I'm cool with it."
    scene ep10_yoga65 with dissolve
    mc "You don't deserve that."
    scene ep10_yoga64 with dissolve
    he "After Halloween... Yes. Yes, I do."
    scene ep10_yoga63 with dissolve
    mc "He started it."
    scene ep10_yoga64 with dissolve
    he "Well, I sure got back at him."
    scene ep10_yoga63 with dissolve
    mc "I'm sorry, Heather. I should have said no."
    scene ep10_yoga62 with dissolve
    he "It wasn't just you, ok?"
    scene ep10_yoga63 with dissolve
    mc "Oh?"
    scene ep10_yoga65 with dissolve
    $ renpy.pause()

if ep9_heather_lewd == 2:
    $ new_bio("Heather", "Heather apologized for using me at the Halloween party. She felt remorseful about that night and said she planned on talking to Tommy about her feelings.")
else:
    $ new_bio("Heather", "Heather apologized for her behavior at the Halloween party. She felt remorseful about that night and said she planned on talking to Tommy about her feelings.")

if "Ok, I'm getting a bit tired of this. Any chance to see some more nudes? That yoga pic was hot and that's kinda why I swiped up on you." in swyper_paula_history or "That's a really hot picture! Got any more?" in swyper_paula_history or "Yeah, for sure! Got any more?" in swyper_paula_history or "Yeah, it's way hotter than the first one." in swyper_paula_history:
    $ ep10_paula_state = 3
elif "The only way I wanna connect with you is with my meaty penis in your vegan vagina. I'm guessing that blowjobs are off the table since that would be putting meat in your mouth." in swyper_paula_history:
    $ ep10_paula_state = 4
elif "Creating a pure race... I think I read about a guy in history books who wanted to do that." in swyper_paula_history:
    $ ep10_paula_state = 5
elif swyper_rejected_by_paula:
    $ ep10_paula_state = 2
elif swyper_liked_paula:
    $ ep10_paula_state = 1
else:
    $ ep10_paula_state = 0

scene ep10_yoga66 with dissolve
pau "Welcome, my butterflies."
if ep10_paula_state > 1:
    scene ep10_yoga67 with dissolve
    mc "(She looks familiar.)"
    scene ep10_yoga67fr with dissolve
    mc "(Oh fuck no! That's the nude yoga chick from Swyper.)"
elif ep10_paula_state == 1:
    scene ep10_yoga67 with dissolve
    mc "(She looks familiar.)"
    scene ep10_yoga67fr with dissolve
    mc "(Oh wait... That's the nude yoga chick from Swyper.)"

scene ep10_yoga67b with dissolve
pau "Peace and tranquility to you all."
pau "Follow my instructions to the best of your abilities and feel free to focus on your preferred chakra for the best effect."
scene ep10_yoga68 with dissolve
pau "Sukhasana."
scene ep10_yoga69 with dissolve
mc "What the hell does that mean?"
scene ep10_yoga70 with dissolve
isa "You can disregard it."
scene ep10_yoga72 with dissolve
mc "But what does it mean? That chakra thing."
scene ep10_yoga70 with dissolve
isa "Your body has different chakras, and some feel that the effect yoga has is increased by focusing on them."
scene ep10_yoga72 with dissolve
mc "But what is a chakra?"
scene ep10_yoga70 with dissolve
isa "It's an energy center on your body. One is in the tailbone, one is in your reproductive organ-"

if affinity == "DIK":
    scene ep10_yoga73 with dissolve
else:
    scene ep10_yoga73b with dissolve
mc "My butt and dick are chakras?"

if affinity == "DIK":
    scene ep10_yoga71 with dissolve
    isa "This is why I asked you to disregard it. I knew you'd make fun of it."
    scene ep10_yoga73 with dissolve
    mc "She's asking me to focus on my dick while doing yoga. How's that not funny?"
    scene ep10_yoga71 with dissolve
    isa "*{i}Sigh{/i}*"
    scene ep10_yoga73 with dissolve
    mc "And the butt too?"
    scene ep10_yoga74 with dissolve
    ji "[name]. Focus."
    scene ep10_yoga75 with dissolve
    mc "Right. Right."
    mc "*{i}Mumbles{/i}* Dick butt energy... Activate! Haha..."
else:
    scene ep10_yoga70 with dissolve
    isa "Well, yes. But there is more to it than that."
    scene ep10_yoga72 with dissolve
    mc "Ok, but I don't think I will focus on those."
    scene ep10_yoga71 with dissolve
    isa "I think it would be best if you didn't."
    scene ep10_yoga72 with dissolve
    mc "Are you focusing on it?"
    scene ep10_yoga71 with dissolve
    isa "*{i}Sigh{/i}*"
    scene ep10_yoga74 with dissolve
    ji "[name]. Focus."
    scene ep10_yoga75b with dissolve
    mc "Right. Right."
    mc "I'm focused."

scene ep10_yoga76 with dissolve
$ renpy.pause()
scene ep10_yoga77 with dissolve
pau "Urdhva Mukha Svanasana."
scene ep10_yoga78 with dissolve
$ renpy.pause()
scene ep10_yoga79 with dissolve
mc "How is this for beginners? I don't understand what she's saying."
scene ep10_yoga80 with dissolve
ji "If you're lost, look at everyone else and follow what we are doing. You'll pick up what she means with time and practice."
scene ep10_yoga81 with dissolve
mc "Um... Ok."
scene ep10_yoga82 with dissolve
$ renpy.pause()
if affinity == "CHICK":
    scene ep10_yoga83 with dissolve
    mc "(This class is testing me... No wonder the rest of them close their eyes while doing the poses.)"
else:
    scene ep10_yoga83b with dissolve
    mc "(Ok... So, yoga class is kinda cool.)"
pau "Bitilasana."
scene bg anim_yoga1_ep10 movie with dissolve
pause
scene ep10_yoga84 with dissolve
mc "(Holy...)"
scene ep10_yoga85 with dissolve
mc "(...fuck.)"
scene ep10_yoga86 with dissolve
if branchIsabella and assman:
    isa "Having problems, [mc_de]?"
else:
    isa "Having problems?"
scene ep10_yoga87 with dissolve
if branchIsabella and assman:
    mc "Aw, come on. I'm trying to follow what you're doing."
else:
    mc "Uh. Yeah, I'm trying to follow what you're doing."
scene ep10_yoga88 with dissolve
isa "Sure. But this is not a new pose to you."
scene ep10_yoga89 with dissolve
mc "(Can she blame me? If this was a room full of dudes doing the same thing...)"
if affinity != "CHICK":
    scene ep10_yoga90 with dissolve
    mc "(...ok, she probably wouldn't care, but that doesn't mean I should feel ashamed...right?)"
    scene ep10_yoga91 with dissolve
    mc "(I mean, I probably shouldn't be staring at them, but if I closed my eyes, I couldn't follow the poses either.)"
    scene ep10_yoga92 with dissolve
    mc "(So, she can't demand that I don't look at their asses...)"
    scene ep10_yoga93 with dissolve
    mc "(Why am I justifying this to myself...?)"
    scene ep10_yoga94 with dissolve
    mc "(There are hot girls doing yoga in front of me, and I'm gonna look. So what?)"
    scene ep10_yoga95 with dissolve
    mc "(But I should probably be more discreet about it.)"
else:
    mc "(...ok, she probably wouldn't care, but that doesn't mean I should feel ashamed...right?)"
    mc "(I mean, I probably shouldn't be staring at them, but if I closed my eyes, I couldn't follow the poses either.)"
$ guideSuggestedPage = 124
scene ep10_yoga96 with dissolve
pau "Tadasana."
scene ep10_yoga97 with dissolve
mc "(Ok... This pose was simple. More like these, please.)"
scene ep10_yoga98 with dissolve
pau "Ardha Uttanasana. Or if you're feeling flexible, Uttanasana."
mc "..."

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Jill)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchIsabella:
                        $mod_choices[5]="(+Isabella)"
                    if branchIsabella:
                        $mod_choices[4]="(-Isabella)"

menu:
    "Focus [m_c1][mod_choices[2]][m_c2][mod_choices[5]]":
        $ dk(-1)
        scene ep10_yoga107 with dissolve
        mc "(Nope. Nope. Not looking. Not today.)"
        if branchIsabella:
            $ RPisabella += 1
            scene ep10_yoga108 with dissolve
            isa "(At least he's trying not to stare at their asses anymore.)"
            isa "(Perhaps it was evil to stay at the back of class? Haha...)"
    "Look closer [m_c1][mod_choices[3]][m_c2][mod_choices[4]]":
        $ dk(1)
        scene ep10_yoga99 with dissolve
        mc "(Oh my God... I didn't know this is what yoga class is all about.)"
        scene ep10_yoga100 with dissolve
        $ renpy.pause()
        scene ep10_yoga101 with dissolve
        $ renpy.pause()
        scene ep10_yoga102 with dissolve
        $ renpy.pause()
        scene ep10_yoga103 with dissolve
        $ renpy.pause()
        scene ep10_yoga104 with dissolve
        $ renpy.pause()
        if branchIsabella:
            $ RPisabella -= 1
            scene ep10_yoga105 with dissolve
            isa "Focus on your own butt chakra, [name], not that of others."
            scene ep10_yoga106 with dissolve
            mc "If it was your butt in my face, I would look too."
            mc "(Hah. Dodged that one.)"

scene ep10_yoga109 with dissolve
pau "Parivrtta Trikonasana."
scene ep10_yoga110 with dissolve
play sound "sound_effects/fart.mp3"
ty "*{i}Farts{/i}*"
bc "Eww! What the fuck!?"
"*{i}Laughter{/i}*"
scene ep10_yoga111 with dissolve
pau "No need to laugh at the passing of gas. Gas is merely energy released from our systems."

scene ep10_yoga112 with dissolve
pau "Interesting pose. It's not quite right."
scene ep10_yoga113 with dissolve
ty "I don't need you to tell me that."
scene ep10_yoga112 with dissolve
pau "Am I sensing rage?"
pau "You need to focus on your root chakra."
scene ep10_yoga113 with dissolve
ty "Spare me the mumbo jumbo."
scene ep10_yoga112 with dissolve
pau "Hm..."
pau "You need help."
scene ep10_yoga114 with dissolve
pau "Look at me. Tadasana."
scene ep10_yoga116 with dissolve
ty "..."
scene ep10_yoga115 with dissolve
pau "Yes. And now, envision a colorful red light at your tailbone. Let it grow toward the ground and become one with the earth."
pau "Close your eyes. Keep it up and don't forget to breathe."
scene ep10_yoga117 with dissolve
mc "Breathing is an autonomic function. We can't forget to breathe."
scene bg anim_bella_smartass_ep10 movie with dissolve
$ renpy.pause(3.0)
mc "Haha, what? It is!"
scene ep10_yoga118 with dissolve
pau "Breathe. Don't talk."
mc "Gotcha."
if ep10_paula_state > 1:
    scene ep10_yoga119 with dissolve
    pau "Hm... Have you been here before? I recognize you from somewhere."
    scene ep10_yoga120 with dissolve
    mc "I'm breathing here. No talking."
    scene ep10_yoga121 with dissolve
    if ep10_paula_state == 3:
        mc "(I hope she doesn't remember me. If she does, she sure will remember me asking her for nudes.)"
    elif ep10_paula_state == 4:
        mc "(I hope she doesn't remember me. I made a pretty offensive joke aimed at her.)"
    elif ep10_paula_state == 5:
        mc "(I hope she doesn't remember me. I pretty much called her Hitler before she blocked me.)"
    else:
        mc "(I hope she doesn't remember me.)"

scene ep10_yoga122 with fade
pau "That will be all for today. You did great, my butterflies."
pau "Namaste."

if branchJill:
    scene ep10_yoga123 with dissolve
    ji "Congratulations! You made it through class. How was it?"
    scene ep10_yoga131 with dissolve
    mc "I don't mind tagging along for these things, but it's not for me."
    scene ep10_yoga124 with dissolve
    mc "And I feel like I need to get rid of more energy. I need a proper training session before I leave."
    scene ep10_yoga124b with dissolve
    ji "Then you should go ahead and do that."
    scene ep10_yoga124 with dissolve
    mc "Yeah, I'm gonna."
    if ep7_bella_lewd:
        scene ep10_yoga125 with dissolve
    else:
        scene ep10_yoga125b with dissolve
    ji "Oh! Before I forget..."
    ji "Would you be up to meeting my parents this weekend?"
    scene ep10_yoga126 with dissolve
    mc "This weekend? Uh... Sure!"
    scene ep10_yoga127 with dissolve
    ji "I talked to Mom about it and she wanted to meet you."
    scene ep10_yoga128 with dissolve
    mc "Did you break the news to her?"
    scene ep10_yoga129 with dissolve
    ji "No, I didn't. But I told her I wanted them to meet someone special and she suggested lunch."
    scene ep10_yoga128 with dissolve
    mc "Ok, I'll make sure I'm free for it."
    stop music fadeout 3
    scene ep10_yoga130 with dissolve
    ji "*{i}Smack{/i}*"
if branchIsabella:
    scene ep10_yoga135 with dissolve
    isa "[name]?"
    scene ep10_yoga136 with dissolve
    mc "Yes, my butterfly?"
    scene ep10_yoga137 with dissolve
    isa "I'm not bringing you here again."
    scene ep10_yoga136 with dissolve
    mc "Come on, it was fun."
    scene ep10_yoga137 with dissolve
    isa "You didn't think it was fun."
    scene ep10_yoga136 with dissolve
    mc "I made it fun."
    scene ep10_yoga137 with dissolve
    isa "No, you made fun of it. There's a big difference."
    isa "And you looked at root chakras in yoga pants."
    scene ep10_yoga136 with dissolve
    mc "Huh?"
    scene ep10_yoga137 with dissolve
    isa "You stared at butts, [name]."
    scene ep10_yoga136 with dissolve
    menu:
        "I tried not to":
            scene ep10_yoga138 with dissolve
            mc "I tried not to, but they were in my line of sight when I tried to follow her instructions."
        "Not a lot":
            scene ep10_yoga138 with dissolve
            mc "Not a lot."
    scene ep10_yoga136 with dissolve
    mc "I'm sorry I didn't take it seriously, but you should have known that before bringing me here."
    mc "Yoga isn't me, Bella. It was fun being here with you, but I feel I need a proper training session after this."
    scene ep10_yoga137 with dissolve
    isa "*{i}Sigh{/i}* Suit yourself."
    scene ep10_yoga136 with dissolve
    mc "Don't be mad."
    scene ep10_yoga137 with dissolve
    isa "I'm not mad. I guess I expected something else."
    scene ep10_yoga136 with dissolve
    mc "I thought you knew what to expect from me."
    stop music fadeout 3
    scene ep10_yoga139 with dissolve
    mc "(Fuck... Was I too insensitive about this?)"
if not branchIsabella and not branchJill:
    scene ep10_yoga135 with dissolve
    isa "What did you think?"
    scene ep10_yoga136b with dissolve
    mc "Do you want my honest thoughts or my polite ones?"
    scene ep10_yoga137b with dissolve
    isa "Was it that bad?"
    scene ep10_yoga136b with dissolve
    mc "I know why the class was free. Let's leave it at that."
    scene ep10_yoga137b with dissolve
    isa "Sometimes, they do that to attract new clientele."
    scene ep10_yoga136b with dissolve
    mc "It was fun being with you. But I think I will head back to the gym and get some other exercise before I leave."
    scene ep10_yoga137b with dissolve
    isa "Well, at least you tried."
    scene ep10_yoga133 with dissolve
    mc "I'm happy you brought me along. I like hanging out with you."
    scene ep10_yoga134 with dissolve
    stop music fadeout 5
    isa "Me too. But you have to ask Jill to teach you about chakras because I'm out."

if branchIsabella:
    $ new_bio("Isabella", "She invited me to a yoga class, and it ended up being too weird for my taste. I made fun of it, and I think she got annoyed.")
else:
    $ new_bio("Isabella", "She invited me to a yoga class, and it ended up being too weird for my taste.")

label ep10_jocks_label:
play music "music/ep8/licensed_music/track70.mp3"
scene ep10_jocks1 with dissolve
"*{i}Cheers{/i}*"
dw "To Chad!"
scene ep10_jocks2 with dissolve
ch "Thanks, bros. You have no idea how much I missed this jacket."
scene ep10_jocks13 with dissolve
jo "I can't believe she followed through. I was sure it was all talk to shut us up."
scene ep10_jocks3 with dissolve
ch "I asked her to fix this back when it happened, but she never did. I'm surprised she did it this time."
scene ep10_jocks6 with dissolve
dw "She said she didn't even try back then. You can't trust those hos for shit."
dw "She only did it now to protect the fucking DIKs from us."
scene ep10_jocks8 with dissolve
ch "What do you mean?"
scene ep10_jocks6 with dissolve
dw "We made a deal with them to get you back into the frat."
dw "We're not supposed to fuck with them from now on and we'll have to share the HOTs with them at some parties."
scene ep10_jocks8 with dissolve
ch "Did you make that deal for me?"
scene ep10_jocks7 with dissolve
dw "Not for you. It's for us!"
dw "With you and Caleb, we'll smash the Metal Men competition."
scene ep10_jocks4 with dissolve
ch "Are you a tri-alpha now?"
scene ep10_jocks10 with dissolve
cb "I got my jacket earlier today."
cb "The competition isn't too far off and since I can't be used to fuck with the DIKs now...why not?"
scene ep10_jocks9 with dissolve
dw "I mean, we could wait another month... If you think we'll need it."
scene ep10_jocks12 with dissolve
cb "I don't trust that frat to keep their promise."
scene ep10_jocks4 with dissolve
ch "Sage held up her end of the bargain. Let's wait and see."
ch "I doubt they'll strip me of the jacket again without another reason, and I'm sure as hell not looking to give them one."
scene ep10_jocks11 with dissolve
cb "You've gotten soft all of a sudden? This doesn't match the impression I got of you."
scene ep10_jocks5 with dissolve
ch "Try losing everything you've worked hard for, and then you get to have that opinion."
scene ep10_jocks13 with dissolve
jo "But what about the parties? Are we gonna have to check with them every time we wanna throw one?"
scene ep10_jocks10 with dissolve
cb "Those girls don't seem worth fighting over to me. I can't say I've missed them at our parties."
scene ep10_jocks14 with dissolve
al "That's because you haven't partied with them much. The HOT-alpha mixers are the shit."
scene ep10_jocks15 with dissolve
jy "Yeah, I'm telling you. There's so much pussy at those parties it gets ridiculous. I'm like drowning in it."
jy "Last mixer, I ended up in someone's bed."

scene ep10_jocks16 with dissolve
dw "Everybody be quiet! I wanna say something."
scene ep10_jocks17 with dissolve
dw "We've come a long fucking way, bros."
scene ep10_jocks21 with dissolve
an "Speech!"
scene ep10_jocks20 with dissolve
dw "You're fucking interrupting it!"
scene ep10_jocks17 with dissolve
dw "As I was saying... We've come a long way!"
dw "Every day, every week, we're at it. Hitting the gym, eating our proteins, drinking our shakes."
scene ep10_jocks22 with dissolve
al "Taking our \"supplements\"."
"*{i}Laughter{/i}*"
scene ep10_jocks18 with dissolve
dw "Yes! And I take it everyone knows it's time to stop doing that, or they'll show up on the tests."
dw "They've helped us grow huge and strong, but that won't matter if we get caught."
dw "Learn from the mistakes of our elders who didn't stop in time because they thought \"Spring\" meant Spring and not Spring semester - which it is."
scene ep10_jocks17 with dissolve
dw "I feel like we have a golden opportunity right now."
dw "I mean, look at us! We've never been this strong before!"
scene ep10_jocks19 with dissolve
dw "This competition, right here. That's what deserves our focus."
dw "I know you're bummed out about the HOTs and the parties, but fuck those parties! They'll come later."
scene ep10_jocks24 with dissolve
dw "And fuck these beers! There will be time for drinking later, too!"
play sound "sound_effects/season3/bottle_break.mp3"
scene ep10_jocks25 with vpunch
dw "But another shot at winning the competition big like this won't come again."
play sound "sound_effects/season3/bottle_break.mp3"
scene ep10_jocks23 with vpunch
jy "Yes! Fuck them!"
scene ep10_jocks26 with dissolve
dw "HEY! Don't smash the bottles! We're the ones who have to clean it up!"
scene ep10_jocks30 with dissolve
$ renpy.pause()
scene ep10_jocks25 with dissolve
dw "For some of us, it's the last time we get to compete."
dw "And I, for one, wanna win it. Think about your future and how it will affect you."
scene ep10_jocks27 with dissolve
dw "Look at our idols and how they used to compete in this competition."
dw "Let's become like them, but better! We can fucking win it!"
dw "And once we do, we can do whatever we want! By then, we've earned everyone's respect."
dw "We can become more than gym teachers or PTs. We can become influencers and rake in millions in endorsement deals!"
scene ep10_jocks28 with dissolve
dw "At the end of that competition, I want to be able to show off and brag the fuck outta that trophy!"
scene ep10_jocks29 with dissolve
an "Instant noodles?"
dw "It's a fucking placeholder - shut up!"
scene ep10_jocks27 with dissolve
dw "And I need everyone to be fully fucking focused! Who's with me!?"
scene ep10_jocks31 with dissolve
"*{i}Cheers{/i}*"
al "Let's hit the fucking gym!"
scene ep10_jocks32 with dissolve
ch "Nice speech. I'm with you."
scene ep10_jocks37 with dissolve
an "Chad, are you moving back in? Because Darius has been using your room."
scene ep10_jocks33 with dissolve
ch "It's fine. I've got a good dorm; I'm not complaining."
scene ep10_jocks37 with dissolve
an "A dorm? You're not gonna live with us?"
scene ep10_jocks33 with dissolve
ch "I'll be around all the time."
scene ep10_jocks35 with dissolve
dw "It's fucking good to have you back. I hope you're ok with me as the leader."
scene ep10_jocks34 with dissolve
ch "You're doing awesome with it and it makes passing the torch easier. Keep it up and I'll mentor you whenever you need it."
ch "Oh, and congrats. I heard you're gonna be a daddy."
scene ep10_jocks36 with dissolve
dw "*{i}Groans{/i}* It's my fault for not using condoms."
dw "I just can't wear those. They keep falling off."
scene ep10_jocks35 with dissolve
dw "But I'm on these Gorilla penis pills now. I'm expecting big changes soon."
dw "And don't worry, they won't show up on any test. They're 100%% organic, so you know they're the real deal."
scene ep10_jocks34 with dissolve
ch "Yeah? But what about the kid?"
scene ep10_jocks35 with dissolve
dw "Oh, I'll make her adopt it or something."
scene ep10_jocks34 with dissolve
ch "You mean abort it?"
stop music fadeout 3
scene ep10_jocks35 with dissolve
dw "Potato, po-tah-to."

label ep10_spar_label:
play music "music/ep10/licensed_music/burn_you_down.mp3"
queue music ["music/ep10/licensed_music/stand_and_fight.mp3","music/ep10/licensed_music/burn_you_down.mp3"]
if not minigames:
    jump brawler_story_troy0_label
label ep10_spar2_label:
scene ep10_spar1 with wipeleft
dwy "Come on. Hit the gloves."
play sound "sound_effects/hit.mp3"
scene ep10_spar2 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep10_spar3 with hpunch
$ renpy.pause(0.5)
scene ep10_spar1 with dissolve
dwy "You gotta go faster than that."
play sound "sound_effects/hit.mp3"
scene ep10_spar2 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep10_spar3 with hpunch
$ renpy.pause(0.5)
scene ep10_spar1 with dissolve
dwy "You holdin' out on me? 100%%. Come on, give it."
play sound "sound_effects/hit.mp3"
scene ep10_spar2 with hpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep10_spar3 with hpunch
$ renpy.pause(0.5)
scene ep10_spar4 with dissolve
dwy "Aight. You're on the defense now. Put 'em up and don't let them down."

play sound "sound_effects/hit.mp3"
scene ep10_spar6 with hpunch
mc "Oof! Hey!"
scene ep10_spar4 with dissolve
dwy "You get sloppy; you get hit."
dwy "Can't take it in training, how are you gonna take it in the ring?"
scene ep10_spar5 with dissolve
mc "You could have warned me."
scene ep10_spar4 with dissolve
dwy "Yeah, that's how they do it on the street, too."
dwy "Heads up! Watch my fist hit your face!"
scene ep10_spar5 with dissolve
mc "Yeah, but still."
play sound "sound_effects/hit.mp3"
scene ep10_spar6 with vpunch
mc "What the fuck!?"
scene ep10_spar4 with dissolve
dwy "Sheesh! Even with that warning, you let your guard down."

play sound "sound_effects/whoosh.mp3"
scene ep10_spar7 with hpunch
dwy "Missed me."
play sound "sound_effects/shove.mp3"
scene ep10_spar8 with hpunch
dwy "Denied."
play sound "sound_effects/whoosh.mp3"
scene ep10_spar7 with hpunch
dwy "This on pay-per-view? Cuz you televised it."
scene ep10_spar9 with dissolve
dwy "Aight. Stop. 'Nuff looking like a fool."
dwy "They're laughing at you."

if affinity == "DIK":
    scene ep10_spar10 with dissolve
    $ renpy.pause()
    scene ep10_spar12 with dissolve
    dwy "Cut that shit. Sit down."
    scene ep10_spar15 with dissolve
    dwy "Someone laughs at you and you're ready to throw fists?"
    scene ep10_spar16 with dissolve
    mc "You got me amped up and they pushed me over the edge."
    scene ep10_spar15 with dissolve
    dwy "You've got to chill, dude. All that hothead attitude gonna get you in life is trouble."
    dwy "Trust me. I know all about it."
    dwy "Life throws shit at you and you think you can solve it by acting tough. It doesn't end well that way. Never has."
    scene ep10_spar16 with dissolve
    mc "Yeah? How do you know?"
    scene ep10_spar15 with dissolve
    dwy "Because I was a punk, I kept looking for trouble."
else:
    scene ep10_spar11 with dissolve
    $ renpy.pause()
    scene ep10_spar13 with dissolve
    dwy "Hm? That's the first thing you did to impress me today."
    scene ep10_spar14 with dissolve
    mc "What is?"
    scene ep10_spar13 with dissolve
    dwy "Sit down."
    scene ep10_spar15 with dissolve
    dwy "Someone laughs at you and you shrug it off."
    scene ep10_spar16 with dissolve
    mc "It's not worth getting into a fight over it."
    scene ep10_spar15 with dissolve
    dwy "I wish I had found my calm at your age."
    dwy "I was a punk. I kept looking for trouble."

scene ep10_spar17 with dissolve
dwy "Trouble is easy to find when you're the one causing it."
scene ep10_spar18 with dissolve
mc "I don't get that feeling from talking to you. What changed?"
scene ep10_spar17 with dissolve
dwy "I got sick of it. Friday night used to be fight night."
dwy "Get wasted and either get checked or check someone."
scene ep10_spar19 with dissolve
dwy "Ma hated it. She was all stressed out about it."
dwy "I woke up one day and realized that the fighting would either get me snuffed or send my Ma to an early grave."
dwy "I had to stop it, but I didn't know how."
scene ep10_spar20 with dissolve
dwy "But I found myself a girl. Tight ass - *{i}Whistles{/i}* - boy, let me tell you."
dwy "And she told me to get my shit together. So, I tried."
scene ep10_spar17 with dissolve
dwy "I slipped up here and there. I got back into the pit some weekends but had to pull myself out of it to keep her."
dwy "I got myself a job and worked my way up."
dwy "And lemme tell you something. Real talk, life's better spent not looking over your shoulder every day."
scene ep10_spar18 with dissolve
mc "Yeah, I've been doing that since I was a kid and I always hated it."
scene ep10_spar17 with dissolve
dwy "So, you see what I'm saying."
scene ep10_spar18 with dissolve
mc "Sure do."
scene ep10_spar17 with dissolve
dwy "But that aggression...it still needs that outlet."
scene ep10_spar18 with dissolve
mc "That's why you keep sparring, huh?"
scene ep10_spar19 with dissolve
dwy "It keeps my body and mind in check. It's how I stay sane."
dwy "I ain't about to lose my girl again, lemme tell you that."
scene ep10_spar18 with dissolve
if affinity == "DIK":
    mc "It's not that easy to switch it off for me. When someone pisses me off, I don't like letting them have the last word."
else:
    mc "I don't enjoy the fights. It's been a way to bond with Dad and get more confident."
    mc "But I'd fight if I had to."
scene ep10_spar17 with dissolve
dwy "The key is to learn how to control your rage."
dwy "You don't learn the biggest lesson in fighting with those fists or legs."
scene ep10_spar21 with dissolve
dwy "You learn it here."
scene ep10_spar18 with dissolve
mc "Got it."
if minigames:
    stop music fadeout 3
scene ep10_spar17 with dissolve
dwy "Aight. Keep it up. You got work to do."
hide screen new_phone_screen
if minigames:
    $ bn_quit_message = "Fight Troy to Quit."
    $ init_brawler_mg(True)
    $ bn_money_reward = True
    $ bn_jump_label = "ep10_after_bn2_label"
    $ bn_freeroam = False
    jump app_new_brawler_story_label
    label ep10_after_bn2_label:
else:
    jump brawler_story_alex0_label

label ep10_after_spar_label:
scene ep10_after_spar1 with dissolve
if minigames:
    $ specialMessage = "{size=-%d}The Brawler app works during some free roam events.{/size}" % (5 * persistent.scale_factor)
    show screen specialmsglong
stop music fadeout 3
$ mphone_stats_unlocked_state = 3
show screen new_phone_screen
mc "(*{i}Phew{/i}* I'm so tired... That's it for today.)"
if minigames:
    hide screen specialmsglong


label ep10_josy_label:
play music "music/ep7/licensed_music/track52.mp3"
scene ep10_josy1 with dissolve
$ renpy.pause()
scene ep10_josy2 with dissolve
$ renpy.pause()
if ep9_jm_sad:
    scene ep10_josy3 with dissolve
    $ renpy.pause()
    scene ep10_josy4 with dissolve
    $ renpy.pause()
    play sound "sound_effects/interlude/select_choice.mp3"
    scene ep10_josy5 with dissolve
    $ renpy.pause()
    play sound "sound_effects/interlude/select_choice.mp3"
    scene ep10_josy6 with dissolve
    $ renpy.pause()
    play sound "sound_effects/interlude/select_choice.mp3"
    scene ep10_josy8 with dissolve
    $ renpy.pause()
    scene ep10_josy7 with dissolve
    $ renpy.pause()
    play sound "sound_effects/interlude/select_choice.mp3"
    scene ep10_josy9 with dissolve
    $ renpy.pause()
    scene ep10_josy10 with dissolve
    $ renpy.pause()

play sound "sound_effects/interlude/select_choice.mp3"
scene ep10_josy11 with dissolve
$ renpy.pause()
scene ep10_josy12 with dissolve
$ renpy.pause()

play sound "sound_effects/whoosh_2.mp3"
scene ep10_josy12d
js "No, no. Stop that! I don't want to make out with you."
scene ep10_josy12c with dissolve
osc "Pff... Why did I even bother throwing you a bone?"
osc "The way you described yourself, I should have known you're just a basic bitch."
scene ep10_josy12e with dissolve
js "Uh! Excuse me?"
scene ep10_josy12c with dissolve
osc "You heard me. And by the way, those things you mentioned you like to do aren't even hobbies."
scene ep10_josy12f with dissolve
osc "I can throw a rock and hit ten girls just like you. You're run-of-the-mill, shorty. Boring and basic."
scene ep10_josy12ba with dissolve
$ renpy.pause()

play sound "sound_effects/interlude/select_choice.mp3"
scene ep10_josy17 with dissolve
$ renpy.pause()
scene ep10_josy13 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/type2.mp3"
scene ep10_josy14
$ renpy.pause()
play sound "sound_effects/interlude/select_choice.mp3"
scene ep10_josy15 with dissolve
$ renpy.pause()

play sound "sound_effects/season3/type1.mp3"
scene ep10_josy18 with dissolve
$ renpy.pause()

play sound "sound_effects/interlude/select_choice.mp3"
scene ep10_josy16
if not persistent.ep10_cardzo13:
    show screen ep10_render_screen("zo13")
with dissolve
$ renpy.pause()
show ep10_josy19
hide screen ep10_render_screen
with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep10_josy20 with dissolve
$ renpy.pause()

$ renpy.sound.play("sound_effects/rain_outside.mp3", channel="sfx2", loop=True)
scene ep10_after_spar2
show screen rain_screen
with fade
$ renpy.pause()

scene white
$ renpy.pause(0.2)
scene ep10_after_spar2
play sound "sound_effects/season2/thunder2.mp3"
$ renpy.pause()

if ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy":
    $ renpy.sound.play("sound_effects/bell.mp3", channel="sfx3", loop=False)
    pause(0.5)
    $ renpy.sound.play("sound_effects/bell.mp3", channel="sfx3", loop=False)
    jump ep10_maya_solo_label
else:
    $ renpy.music.stop(channel="sfx2", fadeout=5)
    jump ep10_josy_solo_label

label ep10_maya_solo_label:
scene ep10_maya_solo1
hide screen rain_screen
with dissolve
play music "music/ep10/licensed_music/track144.mp3"
queue music ["music/ep7/licensed_music/track58.mp3"]
my "Hey! I'm here!"
scene ep10_maya_solo2 with dissolve
mc "Are you drenched?"
scene ep10_maya_solo3 with dissolve
my "No, I think I'm fine. I was more worried about getting struck by lightning than getting wet."

if branchMayaJosy:
    scene ep10_maya_solo8 with dissolve
    my "*{i}Smack{/i}*"
    scene ep10_maya_solo6 with dissolve
    mc "You taste like rain."
    scene ep10_maya_solo7 with dissolve
    my "I'll dry fast."
$ guideSuggestedPage = 126
scene white
$ renpy.pause(0.2)
scene ep10_maya_solo4 with vpunch
play sound "sound_effects/season2/thunder3.mp3"
mc "Ah!!!"
scene ep10_maya_solo5 with dissolve
mc "That was a close one. Come inside."
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_maya_solo9 with dissolve
my "What are you guys up to?"
if branchMayaJosy:
    scene ep10_maya_solo10 with dissolve
else:
    scene ep10_maya_solo10b with dissolve
mc "Not much. The guys are watching some movie."
my "Oh, cool! Should we join?"
mc "We could, but they started like an hour ago, so we're a bit late."
if branchMayaJosy:
    mc "I thought we could grab something to eat from the kitchen and maybe watch something in my room."
else:
    mc "I thought we could grab something to eat from the kitchen and maybe talk and watch something in my room."
if branchMayaJosy:
    scene ep10_maya_solo11 with dissolve
    my "Oh, right! It's time to test that TV for real!"
    my "Have you even been watching it?"
    scene ep10_maya_solo12 with dissolve
    mc "Not a lot. Some here and there."
    mc "But I wanna watch a movie on it with you."
    scene ep10_maya_solo13 with dissolve
    my "Aw, have you been saving that moment for me?"
    scene ep10_maya_solo12 with dissolve
    mc "You are the first one I thought of, for sure."
scene ep10_maya_solo14 with dissolve
if not ep9_jm_sad:
    my "This is gonna be so much fun!"
    my "I need this distraction."
else:
    my "I've both been looking forward to and dreading tonight."
    my "But I can't deny that I need this distraction."
scene ep10_maya_solo15 with dissolve
if not ep9_jm_sad:
    mc "I know you do."
    mc "About that... Things will work out. You know that, right?"
else:
    mc "I'm happy you wanted to come; I wasn't sure if you would."
    mc "And I know you could use a distraction from the other thing, too."
    mc "And about that... Things will work out. You know that, right?"
scene ep10_maya_solo16 with dissolve
my "I'm glad you're sure about it."
scene ep10_maya_solo17 with dissolve
mc "I have a feeling, don't you?"
mc "Everyone is rooting for you and doing their best to help out."
scene ep10_maya_solo18 with dissolve
my "I can feel that, yes."
scene ep10_maya_solo19 with dissolve
mc "No matter what happens on Thanksgiving..."
mc "Remember that you have our support."
scene ep10_maya_solo20 with dissolve
my "..."
scene ep10_maya_solo21 with dissolve
my "Do you have a plan on how to do it?"
scene ep10_maya_solo19 with dissolve
mc "How to get the contract?"
scene ep10_maya_solo21 with dissolve
my "Yeah. You can't just waltz in there."
scene ep10_maya_solo19 with dissolve
mc "Maybe I'll excuse myself, head to the bathroom and get {i}lost{/i} on the way."
scene ep10_maya_solo21 with dissolve
my "And if Dad spots you in his office, snooping around his papers...then what?"
scene ep10_maya_solo19 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    

menu:
    "I'll think of something":
        mc "I'll think of something. But let's hope it doesn't come to that."
    "Joke [m_c1][mod_choices[0]]":
        $ RPmaya += 1
        scene ep10_maya_solo22 with dissolve
        mc "If I do it while having my dick out I believe I can sell him a story that I was looking for toilet paper."
        scene ep10_maya_solo23 with dissolve
        my "Hahaha!"
        scene ep10_maya_solo24 with dissolve
mc "Derek had an idea that he wanted to talk to me about."
mc "I'm not sure what it is, but he seemed confident it would work."

scene ep10_maya_solo25 with dissolve
my "Whatever happens... I trust you."
if branchMayaJosy:
    scene ep10_maya_solo26 with dissolve
    mc "That's good. I would be a bad boyfriend if you couldn't trust me."
    scene ep10_maya_solo27 with dissolve
    my "It still feels weird hearing or saying those words."
    scene ep10_maya_solo26 with dissolve
    mc "To me, it feels right."
    scene ep10_maya_solo27 with dissolve
    my "I'm very happy about it."
    scene ep10_maya_solo28 with dissolve
    my "Um..."
    my "The only thing that feels a bit weird is that Josy's not here tonight."
    scene ep10_maya_solo26 with dissolve
    mc "Yeah, but I thought having some alone time with you would feel nice."
    scene ep10_maya_solo28 with dissolve
    my "I also want to have alone time with you, but I can't shake that thought."
    scene ep10_maya_solo26 with dissolve
    mc "Look, you have alone time with her, too, right?"
    scene ep10_maya_solo27 with dissolve
    my "Yeah."
    scene ep10_maya_solo26 with dissolve
    mc "And so can I if I want to. I think you're making too big of a deal of it."
    mc "I wanted to sit on this couch and watch a movie with you tonight - just the two of us."
    scene ep10_maya_solo29 with dissolve
    my "Is that why you locked the door?"
    scene ep10_maya_solo30 with dissolve
    mc "Well... You're wearing thigh-high knee socks, and that's one of my weaknesses."
    scene ep10_maya_solo29 with dissolve
    my "Guess what?"
    scene ep10_maya_solo26 with dissolve
    mc "What?"
    scene ep10_maya_solo31 with dissolve
    my "*{i}Whispers{/i}* I wouldn't be wearing them if I didn't already know that."
    scene ep10_maya_solo32 with dissolve
    mc "See! You're as sneaky as I am about this."
    my "Hahaha!"
    scene ep10_maya_solo33 with dissolve
    my "Are we gonna watch a movie? Because it feels like you won't be able to focus."
    scene ep10_maya_solo34 with dissolve
    mc "Maybe we can watch one after...?"
    scene ep10_maya_solo35 with dissolve
    my "After what?"
    scene ep10_maya_solo34 with dissolve
    mc "After, you know?"
    scene ep10_maya_solo35 with dissolve
    my "I don't think I could focus either, so...sure."
    scene ep10_maya_solo36 with dissolve
    mc "Wanna go to the bed?"
    my "No, I had something else in mind."
    jump ep10_maya_lewd_label
else:
    my "I can feel that you care a lot about me."
    scene ep10_maya_solo24 with dissolve
    mc "Good. Because I do."
    scene ep10_maya_solo37 with dissolve
    my "And I want you to know I care a lot about you, too."
    if ep9_jm_sad:
        scene ep10_maya_solo38 with dissolve
        my "I wish it were different between us. But I'm also happy that you're happy. You deserve that."
        my "And I wouldn't want you to stay with me and Josy if you weren't truly happy. That would have felt a lot worse."
        scene ep10_maya_solo39 with dissolve
        mc "It means the world to me that we still can hang out like this. I'm not sure if this is normal, but it doesn't feel like it is."
        scene ep10_maya_solo37 with dissolve
        my "Who's normal?"
        scene ep10_maya_solo40 with dissolve
        my "Do you want to talk about her?"
        scene ep10_maya_solo39 with dissolve
        mc "About who?"
        scene ep10_maya_solo40 with dissolve
        my "Your girlfriend."
        if branchJill:
            scene ep10_maya_solo39 with dissolve
            mc "Jill is great. We are unlike each other in many ways, but that doesn't stop us."
            mc "We learn a lot from each other and can relate more than you'd think."
            mc "I started dating her early when I came here, but our feelings grew pretty fast."
        if branchSage:
            scene ep10_maya_solo39 with dissolve
            mc "Sage is amazing, but she's not my girlfriend yet."
            mc "We have made a great connection, but we're still learning how to handle each other."
            mc "We're both emotional but in different ways."
            mc "Ever since I met her, she's grown as a person in my eyes, and my feelings for her grew, too."
        if branchIsabella:
            scene ep10_maya_solo39 with dissolve
            mc "I shouldn't."
            scene ep10_maya_solo41 with dissolve
            my "Why are you so secretive about it?"
            scene ep10_maya_solo39 with dissolve
            mc "..."
            mc "Because I have to."
            scene ep10_maya_solo41 with dissolve
            my "[name]... Who is it?"
            scene ep10_maya_solo39 with dissolve
            mc "..."
            scene ep10_maya_solo41 with dissolve
            my "[name]. You can trust me. It's me."
            scene ep10_maya_solo39 with dissolve
            mc "It's..."
            mc "It's Isabella."
            scene ep10_maya_solo42 with dissolve
            my "..."
            scene ep10_maya_solo41 with dissolve
            my "I did not expect that."
            my "How?"
            scene ep10_maya_solo39 with dissolve
            mc "If I only knew where to begin."
            mc "It's been growing since my first week here. Before I knew she'd be our teacher."
            mc "She helped me out when I came here and we quickly got a good connection that led to something more."
            mc "And after we found out she'd be teaching me, we couldn't announce it to the world."
            scene ep10_maya_solo40 with dissolve
            my "I can't believe you're living in the same situation as I am."
            scene ep10_maya_solo39 with dissolve
            mc "Hey, you're right... I kind of am."
            scene ep10_maya_solo38 with dissolve
            my "You don't have to explain it to me, [name]."
            my "If Isabella makes you happy, that's who you should be with. But..."
            my "I thought she was married."
            scene ep10_maya_solo39 with dissolve
            mc "Yeah, she is, but... It's complicated. And she does make me happy. A lot."
        mc "And meanwhile, with you and Josy... It felt amazing but also hard."
        scene ep10_maya_solo43 with dissolve
        mc "I enjoyed spending time with you two and loved everything we did together."
        mc "But eventually, I had to make a choice."
        scene ep10_maya_solo40 with dissolve
        my "I know."
        my "And you followed your heart like you always do."
        scene ep10_maya_solo39 with dissolve
        mc "I did."
        scene ep10_maya_solo38 with dissolve
        my "I've thought a lot about this."
        my "Part of me feels like I should hate whoever you chose to be with."
        my "Like, she's the reason why we aren't together."
        scene ep10_maya_solo37 with dissolve
        if branchJill:
            my "But I can't hate her."
            my "Talking to her, seeing how wonderful she is, it makes sense that you'd want to be with her."
            my "I can't hate that; it would be out of principle if I did. She didn't do anything wrong."
            my "She fell for the same guy I fell for."
        elif branchSage:
            my "But I could never hate Sage. I fucking love her!"
            my "And since I love her. It makes perfect sense that you'd want to be with her."
            my "Sage didn't do anything wrong. She fell for the same guy I fell for."
        elif branchIsabella:
            my "But I can't hate her."
            my "She's a lot of fun and, from what I can tell, she's a wonderful person. It makes sense that you'd want to be with someone like that."
            my "I can't hate that; it would be out of principle if I did. She didn't do anything wrong."
            my "She fell for the same guy I fell for."
        scene ep10_maya_solo39 with dissolve
        mc "You... You fell for me?"
        scene ep10_maya_solo38 with dissolve
        my "I don't think you want to hear this, but if I don't say it now, I'll never get it said, which would suck."
        my "I did fall for you, [name]."
        if affinity == "CHICK":
            my "You are everything a person should be. You're gentle, you're kind, and you're amazing."
        else:
            my "You have so many good qualities that I adore."
        scene ep10_maya_solo39 with dissolve
        mc "Everything about me isn't great, Maya."
        scene ep10_maya_solo44 with dissolve
        my "[name]. You can be flawed but still be perfect for someone."
        my "I wanted to let you know how I feel. And not because I want to change your mind about me or make you feel bad about it."
        my "It was for my sake. I wanted you to hear it so that I can move on, too."
        scene ep10_maya_solo38 with dissolve
        my "It will be hard to move past what we've been. But I still want to try."
        my "Because when I look at Josy and see how badly she's taking it... It makes me realize I don't want it to be like that."
        scene ep10_maya_solo40 with dissolve
        my "I want it to be like it always has been in our short history here."
        my "With you there by my side, supporting me. And me loving every second of it."
        scene ep10_maya_solo41 with dissolve
        my "And I want to be there for you too. Especially now when I know you're hurting."
        my "I know it's easy to feel pitiful about myself and Josy, but I know this was hard on you, too."
        scene ep10_maya_solo45 with dissolve
        $ renpy.pause()
        scene ep10_maya_solo46 with dissolve
        my "*{i}Phew{/i}* It feels so good to get this off my chest."
        scene ep10_maya_solo47 with dissolve
        $ renpy.pause()
        scene ep10_maya_solo48 with dissolve
        my "How are you feeling?"
        scene ep10_maya_solo49 with dissolve
        mc "Thank you, Maya."
        scene ep10_maya_solo50 with dissolve
        my "*{i}Smack{/i}*"
    elif branchAlone:
        if ep5_feelingsForMaya:
            scene ep10_maya_solo39 with dissolve
            mc "..."
            scene ep10_maya_solo41 with dissolve
            my "What's wrong?"
            scene ep10_maya_solo39 with dissolve
            
            if persistent.mod_wt_enabled: 
                    $mod_choices = ["(feelings for Maya)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
            
            menu:
                "Still have feelings \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep10_feelingsForMaya = True
                    mc "(I can't tell her how I feel...can I?)"
                    scene ep10_maya_solo41 with dissolve
                    my "[name]?"
                    scene ep10_maya_solo39 with dissolve
                    mc "Sorry... It means a lot having someone like you around. I was just feeling so happy about it."
                "I'm over Maya":
                    $ ep10_feelingsForMaya = False
                    mc "Nothing. Thanks, Maya. It feels great having someone like you around."
        else:
            scene ep10_maya_solo39 with dissolve
            mc "Thanks, Maya. It feels great having someone like you around."
    else:
        scene ep10_maya_solo40 with dissolve
        my "Do you want to talk about her?"
        scene ep10_maya_solo39 with dissolve
        mc "About who?"
        scene ep10_maya_solo40 with dissolve
        my "Your girlfriend."
        if branchJill:
            scene ep10_maya_solo39 with dissolve
            mc "Oh..."
            mc "Jill is great. We are unlike each other in many ways, but that doesn't stop us."
            mc "We learn a lot from each other and can relate more than you'd think."
            mc "I started dating her early when I came here, but our feelings grew pretty fast."
        if branchSage:
            scene ep10_maya_solo39 with dissolve
            mc "Haha... Well... We're dating, but I guess I'd call her my girlfriend."
            mc "Sage is amazing. We have made a great connection, but we're still learning how to handle each other."
            mc "We're both emotional people, but in a different way."
            mc "Ever since I met her, she's grown as a person in my eyes, and my feelings for her grew, too."
        if branchIsabella:
            scene ep10_maya_solo39 with dissolve
            mc "W-what?"
            scene ep10_maya_solo37 with dissolve
            my "I knew it."
            my "You ARE in a relationship."
            scene ep10_maya_solo39 with dissolve
            mc "How did you know?"
            scene ep10_maya_solo37 with dissolve
            my "Josy and I have been discussing it. You've been spending time with someone but not letting anyone in on it."
            my "It was either a girlfriend or something illegal."
            scene ep10_maya_solo39 with dissolve
            mc "I didn't think it was that obvious."
            scene ep10_maya_solo41 with dissolve
            my "Why are you so secretive about it?"
            scene ep10_maya_solo39 with dissolve
            mc "..."
            mc "Because I have to."
            scene ep10_maya_solo41 with dissolve
            my "[name]... Who is it?"
            scene ep10_maya_solo39 with dissolve
            mc "..."
            scene ep10_maya_solo41 with dissolve
            my "[name]. You can trust me. It's me."
            scene ep10_maya_solo39 with dissolve
            mc "It's..."
            mc "It's Isabella."
            scene ep10_maya_solo42 with dissolve
            my "..."
            scene ep10_maya_solo41 with dissolve
            my "I did not expect that."
            my "How?"
            scene ep10_maya_solo39 with dissolve
            mc "If I only knew where to begin."
            mc "It's been growing since my first week here. Before I knew she'd be our teacher."
            mc "And after we found out, we couldn't announce it to the world."
            scene ep10_maya_solo40 with dissolve
            my "I can't believe you're living in the same situation as I am. Haha..."
            scene ep10_maya_solo39 with dissolve
            mc "Hey, you're right... I am."
            scene ep10_maya_solo38 with dissolve
            my "You don't even have to explain it to me, [name]."
            my "If Isabella makes you happy, that's who you should be with."
            scene ep10_maya_solo39 with dissolve
            mc "She does make me happy. A lot."
            scene ep10_maya_solo37 with dissolve
            my "That's awesome... Your secret is safe with me."
scene ep10_maya_solo51 with dissolve
my "Wanna watch that movie already?"
scene ep10_maya_solo53 with dissolve
mc "I'm not in the mood for anything heavy."
scene ep10_maya_solo51 with dissolve
my "Horror slasher it is!"
scene ep10_maya_solo52 with dissolve
mc "Oh no..."
my "Hahaha!"
jump ep10_maya_movie_label

label ep10_maya_lewd_label:
if _in_replay:
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
    play music "music/ep10/licensed_music/track144.mp3"
    queue music ["music/ep7/licensed_music/track58.mp3"]
hide screen new_phone_screen
scene ep10_maya_lewd1 with dissolve
my "*{i}Smack{/i}*"
scene ep10_maya_lewd2 with dissolve
$ renpy.pause()
scene ep10_maya_lewd3 with dissolve
$ renpy.pause()
scene ep10_maya_lewd4 with dissolve
my "*{i}Lick lick{/i}*"
scene anim_maya_hj_ep10 with dissolve
mc "You know how to get me going..."
my "*{i}Whispers{/i}* Do you like that, [mc_maya]?"
mc "Mhm..."
pause
scene anim_maya_hj2_ep10 with dissolve
my "Do you want me to put it in my mouth?"
mc "Yeah..."
pause
scene ep10_maya_lewd5 with dissolve
my "Wanna feel my lips around your cock?"
scene ep10_maya_lewd6 with dissolve
mc "Yeah... Do it."
scene anim_maya_bj_ep10 with dissolve
my "*{i}Suck suck{/i}*"
mc "Oh God..."
pause
scene anim_maya_bj2_ep10 with dissolve
mc "You've gotten so good at that. And your piercing makes it feel so much better on top of it."
pause
scene anim_maya_bj3_ep10 with dissolve
pause
scene ep10_maya_lewd7 with dissolve
$ renpy.pause()
scene ep10_maya_lewd8 with dissolve
mc "Those are some sexy underwear."
scene ep10_maya_lewd9 with dissolve
my "Do you like them?"
scene ep10_maya_lewd10 with dissolve
mc "You look amazing in them."
scene ep10_maya_lewd9 with dissolve
my "I'll keep them on, then."
scene ep10_maya_lewd10 with dissolve
mc "No, no, no. I don't like them that much."
my "Haha!"
scene ep10_maya_lewd11 with dissolve
my "Don't get up. Stay seated."
scene ep10_maya_lewd12 with dissolve
$ renpy.pause()
scene anim_maya_lick_ep10 with dissolve
mc "Oh, yes..."
mc "*{i}Lick lick{/i}*"
my "[mc_maya]... Yes, lick me..."
pause
scene ep10_maya_lewd13 with dissolve
my "*{i}Moans{/i}*"
scene ep10_maya_lewd14 with dissolve
$ renpy.pause()
scene bg anim_maya_insert_ep10 movie with dissolve
mc "Fuck!"
my "*{i}Moans{/i}*"
pause
scene anim_maya_ride1_ep10 with dissolve
mc "Fuck me, [maya]. Ride my cock."
pause
scene anim_maya_ride2_ep10 with dissolve
my "Haha, I'm riding my boyfriend's cock."
mc "Why's that funny?"
my "It's not that it's funny. It's weird to say out loud like that, but it makes me happy."
pause
scene anim_maya_ride3_ep10 with dissolve
mc "One of my girlfriends is riding me hard."
my "Haha! {i}One{/i} of your girlfriends. That sounds even weirder."
pause
$ tmpInt = 0
label ep10_maya_lewd_loop_label:
menu:
    "Cowgirl":
        $ tmpInt += 1
        scene anim_maya_ride1_ep10 with dissolve
        pause
        scene anim_maya_ride2_ep10 with dissolve
        pause
        scene anim_maya_ride3_ep10 with dissolve
        pause
        jump ep10_maya_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_maya_doggy1_ep10 with dissolve
        mc "Take it!"
        my "*{i}Moans{/i}* Yes... Give it to me."
        pause
        scene anim_maya_doggy2_ep10 with dissolve
        my "Pound me like that, [mc_maya]."
        mc "Yeah? Do you like it when I fuck you from behind?"
        pause
        scene anim_maya_doggy3_ep10 with dissolve
        my "Mhm... *{i}Moans{/i}* I love it."
        pause
        jump ep10_maya_lewd_loop_label
    "Sideways":
        $ tmpInt += 1
        scene anim_maya_side1_ep10 with dissolve
        my "Yes... Go slow... Like that..."
        my "*{i}Moans{/i}*"
        pause
        scene anim_maya_side2_ep10 with dissolve
        pause
        jump ep10_maya_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_maya_stand1_ep10 with dissolve
        pause
        scene anim_maya_stand2_ep10 with dissolve
        pause
        jump ep10_maya_lewd_loop_label
    "Cum" if tmpInt > 1:
        menu:
            "Creampie":
                scene anim_maya_ride1_ep10 with dissolve
                mc "I'm close to cumming..."
                my "Cum inside of me, [mc_maya]."
                scene ep10_maya_lewd15 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_maya_lewd15 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_maya_lewd15 at vpunch, cum1
                $ renpy.pause()
                scene ep10_maya_lewd16 with dissolve
                $ renpy.pause()
            "On ass":
                mc "I'm close to cumming..."
                scene anim_maya_doggy3_ep10 with dissolve
                my "Cum, [mc_maya]. Cum!"
                scene ep10_maya_lewd17 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_maya_lewd17 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_maya_lewd17 at vpunch, cum3
                $ renpy.pause()
                scene ep10_maya_lewd18 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_maya_cum_ep10 with dissolve
                mc "I'm close to cumming..."
                my "Cum, [mc_maya]. Cum for me..."
                scene ep10_maya_lewd19 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_maya_lewd19 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep10_maya_lewd19 at vpunch, cum3
                $ renpy.pause()
                scene ep10_maya_lewd20 with dissolve
                $ renpy.pause()

scene ep10_maya_lewd21 with dissolve
$ renpy.pause()
scene ep10_maya_lewd22 with dissolve
mc "I love movie nights."
scene ep10_maya_lewd23 with dissolve
my "Right? Haha... I love them, too."
my "Now that we had sex, we might actually be able to watch one."
scene ep10_maya_lewd22 with dissolve
mc "Unless I fall asleep."
scene ep10_maya_lewd23 with dissolve
my "I'll keep you awake. I know a fun movie that you'll enjoy."

$ renpy.end_replay()
$ persistent.ep10_lewd_maya = True
$ calcScenes()
$ mphone_stats_add_girl_s3("maya","You had sex with Maya during movie night in episode 10.")
show screen new_phone_screen

label ep10_maya_movie_label:
if branchMayaJosy:
    scene ep10_maya_solo54 with fade
    $ renpy.pause()
    scene ep10_maya_solo55 with dissolve
    $ renpy.pause()
    scene ep10_maya_solo56 with dissolve
    $ renpy.pause()
    scene ep10_maya_solo57 with dissolve
    my "Watch the movie."
    scene ep10_maya_solo58 with dissolve
    mc "I am."
    scene ep10_maya_solo57 with dissolve
    my "No, you're looking at my legs a lot."
    scene ep10_maya_solo58 with dissolve
    mc "Can you blame me?"
    scene ep10_maya_solo57 with dissolve
    my "No, but I can put my skirt back on."
    scene ep10_maya_solo58 with dissolve
    mc "No, no. Don't do that."
    scene ep10_maya_solo59 with dissolve
    $ renpy.pause()
    scene ep10_maya_solo60 with dissolve
    my "I thought having sex before the movie would make you less horny."
    scene ep10_maya_solo61 with dissolve
    mc "You were wrong."
    mc "Damn, you're pretty to look at."
    scene ep10_maya_solo62 with dissolve
    my "Can I lie down on your lap?"
    mc "Of course."
    scene ep10_maya_solo63 with dissolve
    my "Do you know what the movie is about?"
    scene ep10_maya_solo64 with dissolve
    mc "I have no clue. I don't know if you noticed, but I've been looking at your legs a lot."
    scene ep10_maya_solo63 with dissolve
    my "Haha..."
    my "We don't have to watch it."
    scene ep10_maya_solo64 with dissolve
    mc "Honestly, I just wanna sit like this with you. I couldn't care less about the movie."
    scene ep10_maya_solo65 with dissolve
    my "This feels good, doesn't it?"
    mc "Being with you always felt good."
    my "Come on, not always."
    mc "Most of the time."
    scene ep10_maya_solo66 with dissolve
    my "I feel comfortable with you. It's a weird feeling."
    mc "That's great. I want you to feel comfortable."
    scene ep10_maya_solo67 with dissolve
    my "I never felt this comfortable with Josy."
    scene ep10_maya_solo68 with dissolve
    mc "Oh?"
    scene ep10_maya_solo67 with dissolve
    my "I think it's because of Dad."
    scene ep10_maya_solo68 with dissolve
    mc "Yeah, I get it."
    scene ep10_maya_solo67 with dissolve
    my "Or at least that's what I keep telling myself."
    scene ep10_maya_solo68 with dissolve
    mc "..."
    scene ep10_maya_solo69 with dissolve
    my "*{i}Sigh{/i}* That didn't come off good."
    my "I wanted to say that this - you and I - feels great. That's all."
    scene ep10_maya_solo68 with dissolve
    menu:
        "Focus on Maya":
            $ ep10_msolo_josy_focus = False
            mc "I agree. Being with you is the best."
            mc "I still think about our first movie night together. How you had your body close to mine and your leg across my body."
            scene ep10_maya_solo72 with dissolve
            if ep1_maya_attracted:
                my "Yeah, and you told me you were attracted to me with no chill."
                scene ep10_maya_solo73 with dissolve
                mc "See where it got us."
                scene ep10_maya_solo72 with dissolve
                my "Yeah..."
            else:
                my "Yeah, and you promised you'd try not to get attracted to me. Boy, did you fail that."
                scene ep10_maya_solo73 with dissolve
                mc "Hey, I did try for like five seconds or something."
                scene ep10_maya_solo72 with dissolve
            my "Can I stay the night?"
            scene ep10_maya_solo73 with dissolve
            mc "Of course. I was gonna ask you to."
        "Focus on Josy":
            $ ep10_msolo_josy_focus = True
            mc "I hope that it will feel great for you and Josy, too."
            mc "And I think it will be after we deal with your dad."
            mc "Then you can put those bad feelings away and I bet you will feel comfortable with Josy, too."
            scene ep10_maya_solo67 with dissolve
            my "You say this as if you're sure that it will work out."
            my "I like that. It makes me feel like it will. That it's only a matter of time before it does."
            scene ep10_maya_solo70 with dissolve
            my "I hope you are right about what you just said. I want to feel comfortable with both of you two."
            scene ep10_maya_solo71 with dissolve
            mc "It's still raining like crazy."
            my "Sure is. Can I stay the night?"
            mc "I was gonna ask."
    scene ep10_maya_solo72 with dissolve
    my "Good. I don't wanna leave."
    scene ep10_maya_solo73 with dissolve
    mc "Stay forever."
    scene ep10_maya_solo72 with dissolve
    my "Then you'll have to get me a DIK jacket."
    scene ep10_maya_solo73 with dissolve
    mc "And a penis."
    mc "Why did I say that?"
    scene ep10_maya_solo74 with dissolve
    stop music fadeout 3
    my "Hahaha!"
    scene ep10_maya_solo75 with dissolve
    $ renpy.pause()
    $ mgallery_add_photo("ep10_maya_solo_pic1")
    $ mgallery_add_photo("ep10_maya_solo_pic2")
    $ new_bio("Maya", "I had a wonderful night alone with Maya in my room. We watched a movie and had sex.")
else:
    scene ep10_maya_solo76 with fade
    mc "This movie isn't that bad."
    scene ep10_maya_solo77 with dissolve
    if ep7_solo_maya:
        my "It's better than your mom's taste in movies."
        scene ep10_maya_solo76 with dissolve
        mc "Oh, didn't I tell you? She also hated Wings of a Butterfly. So, maybe her taste wasn't that bad?"
        scene ep10_maya_solo77 with dissolve
        my "That's a big relief. I was genuinely worried about her, haha."
    else:
        my "It's average."
    scene ep10_maya_solo76 with dissolve
    mc "Thanks for choosing a comedy."
    scene ep10_maya_solo78 with dissolve
    my "Haha, I wouldn't want you to be scared tonight."
    my "With the thunder and all, you'd likely crap your pants."
    scene ep10_maya_solo79 with dissolve
    mc "But I'm not scared of thunder."
    scene ep10_maya_solo80 with dissolve
    my "Until you get struck by lightning."
    scene ep10_maya_solo81 with dissolve
    mc "I still respect it, but I'm not scared of it."
    scene ep10_maya_solo80 with dissolve
    my "Sometimes, it makes me jump, but me neither."
    scene ep10_maya_solo81 with dissolve
    mc "You look cute in that outfit, by the way."
    scene ep10_maya_solo82 with dissolve
    my "Thanks. Do you like my skirt?"
    mc "Yeah, but why would you wear it when it's fall? Isn't it cold?"
    my "Says you who's planning a camping trip."
    scene ep10_maya_solo83 with dissolve
    mc "It's a barbecue. Camping is optional... But yeah, maybe it was stupid."
    scene ep10_maya_solo84 with dissolve
    my "It's not too cold, but it's definitely getting there. Also, it was just a short walk here. I feel warm again now."
    scene ep10_maya_solo83 with dissolve
    mc "I like the socks more than the skirt."
    scene ep10_maya_solo84 with dissolve
    my "Haha, I'm aware. I thought about you when I put them on."
    scene ep10_maya_solo83 with dissolve
    mc "You did? Why?"
    scene ep10_maya_solo85 with dissolve
    my "When we lived together, you used to sneak peeks whenever I wore them."
    scene ep10_maya_solo83 with dissolve
    mc "I wasn't peeking."
    scene ep10_maya_solo85 with dissolve
    my "You were. And not in a subtle way."
    scene ep10_maya_solo83 with dissolve
    mc "*{i}Sigh{/i}*"
    scene ep10_maya_solo84 with dissolve
    my "Talk to me about it."
    scene ep10_maya_solo83 with dissolve
    mc "About socks?"
    scene ep10_maya_solo85 with dissolve
    my "Have you always known that you loved thigh-high socks?"
    scene ep10_maya_solo87 with dissolve
    mc "Haha! Yeah. I've always known it. It's not just socks I like, but stockings too."
    scene ep10_maya_solo84 with dissolve
    my "Those are great! I'm with you on that."
    scene ep10_maya_solo83 with dissolve
    mc "Yeah, they make any girl look better. You can go from being a 5/10 to an 8/10 with them on."
    scene ep10_maya_solo86 with dissolve
    my "Hahaha!"
    scene ep10_maya_solo83 with dissolve
    mc "It's true!"
    scene ep10_maya_solo84 with dissolve
    my "What is it that you like about them? Is it the feeling or the look?"
    scene ep10_maya_solo83 with dissolve
    mc "Both. Definitely both."
    mc "But I can't go around and touch people wearing them."
    scene ep10_maya_solo84 with dissolve
    my "No, that would be creepy."
    my "Do you want to touch my socks?"
    scene ep10_maya_solo83 with dissolve
    mc "Haha, I'm good."
    $ guideSuggestedPage = 127
    scene ep10_maya_solo85 with dissolve
    my "Are you sure? I'm giving you a free pass here."
    scene ep10_maya_solo88 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if not branchAlone:
                        $mod_choices[4]="(+Cheater)"
                    if branchAlone and wt_ep9_branch_numbers != 1:
                        $mod_choices[4]="(+Cheater)"
                    
    
    menu:
        "Touch them [m_c1][mod_choices[0]][m_c2][mod_choices[4]]":
            $ RPmaya += 1
            if not branchAlone:
                $ tc += 1
            if branchAlone and wt_ep9_branch_numbers != 1:
                $ tc += 1
            mc "Ok..."
            scene ep10_maya_solo89 with dissolve
            my "You put your hand there?"
            mc "When it comes to socks... This is the best part."
            scene ep10_maya_solo90 with dissolve
            mc "Where it transitions from warm thigh meat to sock fabric."
            my "Hahaha! You are so fucking weird!"
            scene ep10_maya_solo91 with dissolve
            mc "It is! Maya, feel it!"
            mc "This right here is where the money is."
            scene ep10_maya_solo92 with dissolve
            my "Stop it. You're gonna get a rod if you don't."
        "Don't touch them":
            if ep9_jm_sad:
                mc "No, I don't think it's appropriate...you know?"
                scene ep10_maya_solo84 with dissolve
                my "Ah, gotcha."
            else:
                mc "No, really. I'm good."
                scene ep10_maya_solo84 with dissolve
                my "Your loss."
    scene ep10_maya_solo83 with dissolve
    mc "What about you? What's your thing?"
    scene ep10_maya_solo85 with dissolve
    my "My thing?"
    scene ep10_maya_solo83 with dissolve
    mc "Yeah. What's the thing that you go crazy about?"
    scene ep10_maya_solo84 with dissolve
    my "Like clothing or?"
    scene ep10_maya_solo83 with dissolve
    mc "It can be anything. Clothes, traits, a thing that someone does..."
    scene ep10_maya_solo93 with dissolve
    my "..."
    mc "Haha! You know something. Tell me."
    scene ep10_maya_solo84 with dissolve
    my "No, I don't think I will."
    scene ep10_maya_solo83 with dissolve
    mc "You've gotta tell me. I let you in on my stocking fetish."
    scene ep10_maya_solo85 with dissolve
    my "Oh! Is fetish the word you'd use for it? Interesting!"
    scene ep10_maya_solo83 with dissolve
    mc "Preference?"
    scene ep10_maya_solo94 with dissolve
    my "Hey, if it's a fetish, it's a fetish."
    scene ep10_maya_solo87 with dissolve
    mc "You're trying to dodge my question. What's your thing!?"
    scene ep10_maya_solo84 with dissolve
    my "Ok... I have one thing that came to mind, but it's private."
    scene ep10_maya_solo83 with dissolve
    mc "It can't be more private than mine."
    scene ep10_maya_solo84 with dissolve
    my "It's up there."
    my "Ok, wanna know what it is?"
    scene ep10_maya_solo83 with dissolve
    mc "Lay it on me."
    scene ep10_maya_solo95 with dissolve
    my "I like it when someone whispers softly into my ear."
    scene ep10_maya_solo83 with dissolve
    mc "Huh? That's it? Whispering is hot?"
    scene ep10_maya_solo85 with dissolve
    my "So hot!"
    scene ep10_maya_solo83 with dissolve
    mc "Nuh-uh."
    scene ep10_maya_solo94 with dissolve
    my "It totally is! It gives me goosebumps all over."
    my "But it has to be the perfect whisper. If it's too loud, it hurts."
    my "It's gotta be loud enough to make the words out but soft enough to make everything tingle."
    scene ep10_maya_solo83 with dissolve
    mc "Show me."
    scene ep10_maya_solo85 with dissolve
    my "I'm warning you, if I do this, you'll want to jump me."
    scene ep10_maya_solo83 with dissolve
    mc "Haha, no. I can control myself."
    scene ep10_maya_solo96 with dissolve
    my "*{i}Whispers{/i}* It's gotta be soft like this..."
    my "*{i}Whispers{/i}* And it doesn't hurt if... *{i}Moans{/i}* You moan a little bit too."
    mc "Ahhh..."
    scene ep10_maya_solo86 with dissolve
    my "Haha! I told you! You like it too!"
    scene ep10_maya_solo83 with dissolve
    mc "Let me try it!"
    scene ep10_maya_solo94 with dissolve
    my "Hell no!"
    scene ep10_maya_solo83 with dissolve
    mc "Come on! I wanna learn how to do it."
    scene ep10_maya_solo85 with dissolve
    if branchAlone:
        my "Yeah? So you can use my sex trick on other girls?"
    elif branchSage:
        my "Yeah? So you can use my sex trick on Sage?"
    else:
        my "Yeah? So you can use my sex trick on your girlfriend?"
    scene ep10_maya_solo83 with dissolve
    mc "Come here."
    scene ep10_maya_solo97 with dissolve
    mc "*{i}Whispers{/i}* Does it work if I whisper like this?"
    scene ep10_maya_solo98 with dissolve
    my "It's too loud. You gotta whisper softly."
    scene ep10_maya_solo99 with dissolve
    mc "*{i}Whispers{/i}* I'm whispering softly into your ear, Maya..."
    scene ep10_maya_solo100 with dissolve
    my "Yeah... That's the stuff."
    scene ep10_maya_solo99 with dissolve
    mc "*{i}Whispers{/i}* And now I'm gonna moan too... *{i}Moans{/i}*"
    scene ep10_maya_solo101 with dissolve
    my "Hahaha... This shouldn't be working as well as it does."
    scene ep10_maya_solo99 with dissolve
    mc "*{i}Whispers{/i}* Peanut butter sandwich..."
    scene ep10_maya_solo86 with dissolve
    my "Hahaha! Stop it!"
    my "I have goosebumps all over because you whispered peanut butter sandwich into my ear."
    mc "The three magic words."
    scene ep10_maya_solo83 with dissolve
    my "..."
    if ep10_feelingsForMaya:
        scene ep10_maya_solo103 with dissolve
        $ renpy.pause()
        scene ep10_maya_solo84 with dissolve
        my "Are you ok? I hope I didn't turn you on too much."
        scene ep10_maya_solo83 with dissolve
        mc "It's not that."
        scene ep10_maya_solo84 with dissolve
        my "Then what is it?"
        scene ep10_maya_solo83 with dissolve
        mc "I..."
        mc "I still have feelings for you."
        scene ep10_maya_solo104 with dissolve
        my "What?"
        scene ep10_maya_solo105 with dissolve
        mc "I have feelings for you, Maya."
        scene ep10_maya_solo104 with dissolve
        my "What? Uh... When?"
        scene ep10_maya_solo105 with dissolve
        mc "It's been in the back of my mind since what feels like forever."
        mc "And I know that it's a horrible thing to say to you when you're with Josy - someone I absolutely adore."
        mc "I want you two to be happy together, but I can't help it..."
        mc "I have tried so damned hard to let go and opening my eyes to someone new to stop feeling the way I do about you."
        scene ep10_maya_solo106 with dissolve
        mc "And it's like every time I am near you, everything we do together..."
        mc "It makes it worse. It reinforces those feelings."
        mc "But I can't stop seeing you. I don't want that."
        scene ep10_maya_solo105 with dissolve
        mc "So, what I do is that I lie to myself. I pretend that I don't feel anything for you anymore."
        mc "But I don't know for how long I can keep on doing that."
        scene ep10_maya_solo106 with dissolve
        mc "I'm so sorry... Fuck... I shouldn't have told you this. I'm such an asshole."
        my "..."
        scene ep10_maya_solo107 with dissolve
        my "..."
        mc "Can you say something?"
        scene ep10_maya_solo105 with dissolve
        my "..."
        scene ep10_maya_solo108 with dissolve
        my "I'm with Josy, [name]."
        scene ep10_maya_solo105 with dissolve
        mc "I know."
        scene ep10_maya_solo108 with dissolve
        my "I can't think of what to tell you."
        scene ep10_maya_solo105 with dissolve
        mc "Why?"
        scene ep10_maya_solo108 with dissolve
        my "Because it's a thought process that I don't want to have."
        my "It's scary. And if I start thinking about it, I will start questioning things."
        my "Things that I don't want to question."
        scene ep10_maya_solo107 with dissolve
        mc "I should have kept my mouth shut."
        scene ep10_maya_solo108 with dissolve
        my "I should get back to my dorm."
        scene ep10_maya_solo109 with dissolve
        mc "Maya... This feels like shit."
        scene ep10_maya_solo110 with dissolve
        my "Well, how do you think I feel!?"
        scene ep10_maya_solo111 with dissolve
        mc "Please, don't be mad..."
        scene ep10_maya_solo110 with dissolve
        my "You have no right to say those things to me. What are you thinking?"
        scene ep10_maya_solo111 with dissolve
        mc "That I'm not over you. That's all I keep thinking."
        stop music fadeout 3
        scene ep10_maya_solo112 with dissolve
        my "Fuck, [name]! Fuck!"
        scene ep10_maya_solo113 with dissolve
        $ renpy.pause()
        $ new_bio("Maya", "I had a movie night with Maya in my room. But I ruined it by confessing that I still have feelings for her.")
    else:
        scene ep10_maya_solo84 with dissolve
        my "Thanks so much for tonight, [name]. I had a blast."
        my "It reminded me of living together with you."
        scene ep10_maya_solo83 with dissolve
        mc "Those were some good times."
        scene ep10_maya_solo84 with dissolve
        my "Right?"
        scene ep10_maya_solo83 with dissolve
        mc "Don't get struck by lightning on the way back now."
        scene ep10_maya_solo84 with dissolve
        my "I'll try my best."
        stop music fadeout 3
        scene ep10_maya_solo102 with dissolve
        my "*{i}Smack{/i}* Good night."
        if ep9_jm_sad:
            $ new_bio("Maya", "I had a movie night with Maya in my room. We talked about our breakup and tried to get over it together.")
        else:
            $ new_bio("Maya", "I had a movie night with Maya in my room. It felt great to spend some alone time with her.")

if ep10_jm_solo=="Maya Josy":
    jump ep10_josy_solo_label
jump ep10_after_solo_label

label ep10_josy_solo_label:
scene ep10_josy_solo1
hide screen rain_screen
with dissolve
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx3", loop=True)
play music "music/ep10/licensed_music/track145.mp3"
queue music ["music/ep7/licensed_music/track58.mp3"]
mc "There's not an umbrella made for this weather."
scene ep10_josy_solo2 with dissolve
js "Did you even use one? You're soaked!"
scene ep10_josy_solo3 with dissolve
mc "I did but my pants got wet."
mc "I suppose you don't have anything in my size to wear?"
scene ep10_josy_solo4 with dissolve
js "Will a skirt do?"
scene ep10_josy_solo5 with dissolve
mc "No oversized sweatpants?"
scene ep10_josy_solo4 with dissolve
js "The best I can do is tight yoga pants that make your butt look extra cute."
scene ep10_josy_solo5 with dissolve
mc "Pass..."
if branchMayaJosy:
    mc "Would it be ok if I removed them?"
    scene ep10_josy_solo4 with dissolve
    js "Of course. Go ahead."
    scene ep10_josy_solo8 with dissolve
    js "*{i}Smack{/i}*"
    scene ep10_josy_solo9 with dissolve
    js "I'm happy you came."
    scene ep10_josy_solo9b with dissolve
    mc "Me too."
else:
    mc "Would it be weird if I removed them?"
    scene ep10_josy_solo6 with dissolve
    js "Maybe a little bit?"
    scene ep10_josy_solo5 with dissolve
    mc "Do you want me to remove them a little bit?"
    scene ep10_josy_solo4 with dissolve
    js "No, I meant it would be a little bit weird."
    scene ep10_josy_solo5 with dissolve
    mc "Ah, that's fine. I'm sure they'll dry soon."
    scene ep10_josy_solo6 with dissolve
    js "Looking at them...I doubt it."
    scene ep10_josy_solo5 with dissolve
    mc "I can head back and get a dry pair."
    scene ep10_josy_solo4 with dissolve
    js "Then you'd probably end up with two pairs of soaked pants. Go ahead, remove them."
    scene ep10_josy_solo5 with dissolve
    mc "Thanks. I promise I won't shake my butt and tease you."
    scene ep10_josy_solo4 with dissolve
    js "Haha, that wouldn't work on me."
    scene ep10_josy_solo5 with dissolve
    mc "Are you sure? I've been doing squats lately. My ass is pretty firm."
    scene ep10_josy_solo7 with dissolve
    js "Do you squeeze your ass to feel if it is or what?"
    scene ep10_josy_solo5 with dissolve
    mc "Haha! This got weird."
scene ep10_josy_solo10 with dissolve
mc "What are you up to?"
scene ep10_josy_solo11 with dissolve
js "Not much. I've been on my laptop for a while."
scene ep10_josy_solo12 with dissolve
mc "Browsing stuff?"
scene ep10_josy_solo11 with dissolve
js "Uh-huh. Something like that."
play sound "sound_effects/season2/thunder2.mp3"
scene ep10_josy_solo13 with vpunch
js "Ah!!!"
mc "That one was close!"
scene ep10_josy_solo14 with dissolve
mc "Are you scared of thunderstorms?"
scene ep10_josy_solo15 with dissolve
js "I'm not {b}that{/b} scared. Just a bit."
scene ep10_josy_solo16 with dissolve
mc "Aw."
scene ep10_josy_solo15 with dissolve
js "Haha, don't aw me! I know it's stupid to fear thunder, but it's loud and sudden. Also, it's not unheard of that people get struck by lightning."
scene ep10_josy_solo16 with dissolve
mc "But it's not that likely to happen in here."
scene ep10_josy_solo17 with dissolve
js "When I was young, I built a pillow fort to keep me safe during thunderstorms."
scene ep10_josy_solo19 with dissolve
mc "You did?"
scene ep10_josy_solo18 with dissolve
js "Yeah, and then I slept in it overnight or stayed in it until it had stopped."
js "It made me feel safer."
scene ep10_josy_solo19 with dissolve
mc "I haven't built a pillow fort in ages."
scene ep10_josy_solo18 with dissolve
js "So, you did it too?"
scene ep10_josy_solo19 with dissolve
mc "A few times. Who hasn't built one?"
scene ep10_josy_solo18 with dissolve
js "Wanna do it now?"
scene ep10_josy_solo19 with dissolve
mc "Now? We're not kids anymore."
scene ep10_josy_solo20 with dissolve
js "It will be fun! I'll fetch some pillows!"
scene ep10_josy_solo21 with wipeleft
mc "This is starting to look like something. It's very...ambitious."
scene ep10_josy_solo22 with dissolve
js "I take pillow forts seriously."
js "Let me slip into something more comfortable. You can crawl inside if you want."
scene ep10_josy_solo23 with dissolve
mc "All right... Let's give it a whirl."
scene ep10_josy_solo24 with dissolve
mc "This is cozy, for sure."
play sound "sound_effects/switch.mp3"
scene ep10_josy_solo25 with dissolve
js "Uh-huh. I told you!"
if branchMayaJosy:
    scene ep10_josy_solo26 with dissolve
    mc "Yeah, and it's pretty spacious. I didn't think it would be."
    scene ep10_josy_solo29 with dissolve
    $ renpy.pause()
else:
    scene ep10_josy_solo27 with dissolve
    mc "Yeah, and it's pretty spacious. I didn't think it would be."
    scene ep10_josy_solo28 with dissolve
    $ renpy.pause()

if ep9_winner == "Josy":
    scene ep10_josy_solo30 with dissolve
    mc "Where did you put your Best Costume trophy? I thought it would be proudly on display, but I can't see it."
    scene ep10_josy_solo31 with dissolve
    js "Someone stole it from me."
    mc "Yeah, right."
    js "They did! I put it in the hallway when I got back the day after, and later it was gone."
    scene ep10_josy_solo30 with dissolve
    mc "Why didn't you ask around? Someone's bound to have it."
    scene ep10_josy_solo31 with dissolve
    js "Let's just say it's a kind of theft that I didn't mind."

    play sound "sound_effects/whoosh_2.mp3"
    scene ep10_josy_solo30b
    $ renpy.pause()
    scene ep10_josy_solo30c with dissolve
    $ renpy.pause()
    scene ep10_josy_solo30d with dissolve
    ar "Oh? Hubba hubba."

    scene ep10_josy_solo30
else:
    scene ep10_josy_solo30 with dissolve
mc "We did a great job with this, Josy. We could be architects."
scene ep10_josy_solo31 with dissolve
js "Uh-huh."
js "Is it big enough for both of us?"
scene ep10_josy_solo32 with dissolve
$ renpy.pause()
scene ep10_josy_solo33 with dissolve
$ renpy.pause()
scene ep10_josy_solo34 with dissolve
$ renpy.pause()
scene ep10_josy_solo35 with dissolve
mc "Y-yeah."
if branchMayaJosy:
    scene ep10_josy_solo36 with dissolve
    mc "You're wearing that for this?"
    scene ep10_josy_solo37 with dissolve
    js "You're not wearing pants, so... It's only fair, I think."
    scene ep10_josy_solo38 with dissolve
    mc "You look unbelievably hot in it."
    scene ep10_josy_solo37 with dissolve
    js "I figured you'd like it."
else:
    scene ep10_josy_solo39 with dissolve
    if branchAlone:
        mc "..."
    else:
        mc "(I shouldn't be here...)"
$ guideSuggestedPage = 125
scene ep10_josy_solo40 with dissolve
mc "Heather will probably wonder what the hell you did with the room."
scene ep10_josy_solo41 with dissolve
js "She'll be back tomorrow. She's visiting family for a birthday, I believe."
scene ep10_josy_solo40 with dissolve
mc "Ah."
scene ep10_josy_solo42 with dissolve
js "So... What kind of shenanigans were you up to when you played in your pillow fort?"
scene ep10_josy_solo43 with dissolve
mc "Not much. The fun part about building a pillow fort was the actual building part."
mc "Playing in it or cleaning up after sucked."
scene ep10_josy_solo42 with dissolve
js "You never relaxed inside of it?"
scene ep10_josy_solo43 with dissolve
mc "I ate ice cream in it once. That's about what I can remember."
mc "What did you use to do?"
scene ep10_josy_solo44 with dissolve
js "Often, I built it with friends. So, we used to play in it."
js "Talk, gossip, have fun, read magazines, eat... We used to do whatever came to mind."
scene ep10_josy_solo45 with dissolve
mc "That sounds more fun than what I did."
scene ep10_josy_solo46 with dissolve
js "Let's do some of it."
scene ep10_josy_solo45 with dissolve
mc "I'm not sure I have a lot to gossip about."
scene ep10_josy_solo47 with dissolve
js "I'm sure you have some gossip."
scene ep10_josy_solo45 with dissolve
mc "I have secrets and such, but that's not gossip, is it?"
scene ep10_josy_solo47 with dissolve
js "I can go first."
js "This is some juicy gossip, ok? Don't tell anyone I told you this."
scene ep10_josy_solo45 with dissolve
mc "You have my word."
scene ep10_josy_solo47 with dissolve
js "Someone in this very house...is pregnant."
scene ep10_josy_solo45 with dissolve
mc "Arieth? Yeah, I know."
scene ep10_josy_solo48 with dissolve
js "What!? Do you already know?"
scene ep10_josy_solo49 with dissolve
mc "Quinn told me at the Halloween party."
scene ep10_josy_solo48 with dissolve
js "Wow!"
scene ep10_josy_solo45 with dissolve
mc "Do you know who the father is?"
scene ep10_josy_solo47 with dissolve
js "She says it's Dawe, but..."
scene ep10_josy_solo49 with dissolve
mc "But what?"
scene ep10_josy_solo50 with dissolve
js "I'm not sure I can trust that."
scene ep10_josy_solo45 with dissolve
mc "Yeah, I wouldn't trust that either. She's been with almost every DIK."
scene ep10_josy_solo48 with dissolve
js "Huh!? No way!"
scene ep10_josy_solo45 with dissolve
mc "Oh! This is gossiping, isn't it?"
scene ep10_josy_solo46 with dissolve
js "You're spilling the tea, all right. Go on!"
scene ep10_josy_solo45 with dissolve
mc "I don't want them to look bad, but most of them have been with her."
scene ep10_josy_solo47 with dissolve
js "You haven't...right?"
scene ep10_josy_solo45 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchMayaJosy:
                        $mod_choices[4]="(-Josy)"
                    if not branchMayaJosy and affinity=="DIK" and not branchAlone:
                        $mod_choices[4]="(+Cheater)"

menu:
    "Hell no!":
        mc "Hell no!"
        scene ep10_josy_solo46 with dissolve
        js "Haha! That's an emphatic no."
        scene ep10_josy_solo45 with dissolve
        if branchMayaJosy:
            if affinity == "DIK":
                mc "Going from you and Maya to her would be a huge downgrade."
            else:
                scene ep10_josy_solo51b with dissolve
                mc "Can you blame me? I have two wonderful girlfriends."
        else:
            if affinity == "DIK":
                mc "Let's just say I want my cock to stay healthy."
                scene ep10_josy_solo51 with dissolve
                $ renpy.pause()
            else:
                mc "Let's just say there are reasons I never would do it."
    "Not yet [m_c1][mod_choices[4]]":
        mc "Not yet."
        if branchMayaJosy:
            $ RPjosy -= 1
            scene ep10_josy_solo48 with dissolve
            js "Wait... Did you just consider it?"
            scene ep10_josy_solo49 with dissolve
            if affinity == "DIK":
                $ dk(1)
                mc "I can't tell the future, Josy. I was just saying I haven't been with her yet."
            else:
                mc "No! I mean, I'm with you and Maya. I'm saying I haven't been with her yet."
                mc "Not yet! I haven't been with her. Period."
        else:
            scene ep10_josy_solo48 with dissolve
            js "But you're considering it, huh?"
            scene ep10_josy_solo49 with dissolve
            if affinity == "DIK":
                if not branchAlone:
                    $ dk(1)
                    $ tc += 1
                mc "I can't tell the future, Josy. I was just saying I haven't been with her yet. Who knows if I will be?"
            else:
                if branchAlone:
                    if affinity == "NEUTRAL":
                        mc "Never say never. She seems to have some kind of a bucket list going on for her. Would I want to stand in the way of her goals and happiness?"
                        scene ep10_josy_solo44 with dissolve
                        js "Eww! Haha..."
                    else:
                        mc "I think you're reading too much into what I said."
                else:
                    mc "No, I'm not."
scene ep10_josy_solo47 with dissolve
js "Do you think the father could be one of the DIKs?"
scene ep10_josy_solo45 with dissolve
mc "We would need to do some math on that, but the thought has entered my mind."
mc "I should probably alert them about it, but I don't want to spread her secret."
scene ep10_josy_solo47 with dissolve
js "Trust me. This won't stay a secret for long. It started to spread, but I didn't want you to get involved if it gets ugly."
scene ep10_josy_solo45 with dissolve
mc "What is she planning to do? Will she keep it?"
scene ep10_josy_solo47 with dissolve
js "I haven't asked her about that because I didn't hear it from her. I think approaching her with that question would be awkward."
js "Could you imagine if that was you?"
scene ep10_josy_solo45 with dissolve
mc "Do you suck at anatomy or what?"
scene ep10_josy_solo46 with dissolve
js "I meant, if you were the dad, stupid. What would you do?"
scene ep10_josy_solo45 with dissolve
mc "It's scary to think about that. My entire life would be flipped upside down if she kept it."
if branchMayaJosy:
    scene ep10_josy_solo47 with dissolve
    js "Yeah, it's nuts."
    scene ep10_josy_solo45 with dissolve
else:
    scene ep10_josy_solo46 with dissolve
    js "Yup. I hope you've been wearing condoms."
    scene ep10_josy_solo45 with dissolve
    mc "I probably should be more careful..."
mc "What would you do?"
scene ep10_josy_solo47 with dissolve
js "That's a tough question."
js "I mean, in the future, I know I want a family and kids. But now!?"
js "It's too early for that. I haven't done what I dream of yet."
scene ep10_josy_solo50 with dissolve
js "I haven't gotten my education or my dream job. It would be a horrible situation."
js "But if I got pregnant, even though I'm feeling all of this, it would be hard as hell to decide against keeping it."
js "It's a baby..."
if branchMayaJosy:
    scene ep10_josy_solo45 with dissolve
    mc "I have to be careful around you then."
    scene ep10_josy_solo46 with dissolve
    js "Haha, you don't have to worry that much. I use protection."
    scene ep10_josy_solo45 with dissolve
    mc "And I have a strong pull-out game."
    scene ep10_josy_solo46 with dissolve
    js "Pff. No, you don't."
    scene ep10_josy_solo45 with dissolve
    mc "Huh? What do you mean I don't?"
    scene ep10_josy_solo46 with dissolve
    js "You're telling me you have full control of every single drop of it?"
    scene ep10_josy_solo45 with dissolve
    mc "Of course."
    scene ep10_josy_solo47 with dissolve
    js "Don't you know that you cum a bit during sex too? It's not just at the end of it."
    scene ep10_josy_solo45 with dissolve
    mc "Well, that can hardly be a lot of cum."
    scene ep10_josy_solo46 with dissolve
    js "All it takes is one strong swimmer..."
    scene ep10_josy_solo45 with dissolve
    mc "Yeah, but with your protection, they'd have to swim through a chemical warzone to make it."
    scene ep10_josy_solo52 with dissolve
    js "Hahaha!"
else:
    scene ep10_josy_solo45 with dissolve
    mc "Remind me to wear a condom around you."
    scene ep10_josy_solo48 with dissolve
    js "Uh... What? We're not having sex."
    scene ep10_josy_solo49 with dissolve
    mc "I know. It was a stupid joke."
    scene ep10_josy_solo51 with dissolve
    js "..."

scene ep10_josy_solo45 with dissolve
mc "Any more gossip?"
scene ep10_josy_solo46 with dissolve
js "Not a lot. You already knew the best one I had."
scene ep10_josy_solo45 with dissolve
mc "Ah. Is it time for magazines and food?"
scene ep10_josy_solo46 with dissolve
js "How about funny videos on the phone?"
scene ep10_josy_solo45 with dissolve
mc "Or picture time? Can't you show me some old photos of yourself?"
scene ep10_josy_solo47 with dissolve
js "Why would you want to see them?"
scene ep10_josy_solo45 with dissolve
mc "It would be nice to see what you looked like when you were young."
scene ep10_josy_solo47 with dissolve
js "I don't have pictures that go way back on this phone. But maybe some from a year ago or so."
scene ep10_josy_solo45 with dissolve
mc "That will do, show me."
scene ep10_josy_solo53 with dissolve
js "Let me fetch my phone!"
if not branchAlone and not branchMayaJosy:
    scene ep10_josy_solo54 with dissolve
    $ renpy.pause()
scene ep10_josy_solo55 with dissolve
js "Hahaha! These are good ones! It's from when Maya got her piercing and I bailed out."
scene ep10_josy_solo55a with dissolve
js "This is before she got it..."
scene ep10_josy_solo55b with dissolve
js "And this is after."
mc "Haha! She does not look happy."
js "Yeah, I can't blame her."
mc "What made you wanna do it?"
scene ep10_josy_solo56 with dissolve
js "It was a spur-of-the-moment thing. Maya never did many wild things, and I wanted to change that."
scene ep10_josy_solo57 with dissolve
mc "Haha! And then you bailed on her?"
scene ep10_josy_solo56 with dissolve
js "Haha! I know! I feel horrible about it. But it looked so scary when she did it, and there was so much blood. And she screamed!"
scene ep10_josy_solo57 with dissolve
mc "You owe her for that."
scene ep10_josy_solo59 with dissolve
js "I made it up to her."
scene ep10_josy_solo58 with dissolve
mc "How?"
scene ep10_josy_solo59 with dissolve
js "You don't want to know the details of that."
scene ep10_josy_solo58 with dissolve
mc "Aha... Or do I?"
scene ep10_josy_solo59 with dissolve
js "Well... She couldn't use her tongue for a while, so I let her use mine."
scene ep10_josy_solo57 with dissolve
mc "That's hot."
scene ep10_josy_solo69b with dissolve
js "..."
scene ep10_josy_solo70 with dissolve
js "You'll be able to help her at Thanksgiving, right?"
scene ep10_josy_solo69 with dissolve
mc "I hope so."
scene ep10_josy_solo70 with dissolve
js "Do whatever it takes...for her. Ok?"
scene ep10_josy_solo69b with dissolve
mc "I'll do my best for both of you."
scene ep10_josy_solo55c with dissolve
js "This one is nice. It's me and Dad. I love this picture."
mc "It's a sweet one, for sure."
scene ep10_josy_solo60 with dissolve
js "Let's see... What else is there?"
mc "Wait! That's me."
scene ep10_josy_solo61 with hpunch
js "Uh, no, it's not."
scene ep10_josy_solo62 with dissolve
mc "I saw it! Haha, that's my old profile picture from Rooster!"
scene ep10_josy_solo61 with dissolve
js "I don't know how it got in there."
scene ep10_josy_solo62 with dissolve
mc "Why are you blushing if you don't know?"
scene ep10_josy_solo63 with dissolve
js "This is so embarrassing..."
scene ep10_josy_solo64 with dissolve
mc "What is?"
scene ep10_josy_solo65 with dissolve
js "Did you never save someone's photo before?"
scene ep10_josy_solo64 with dissolve
mc "Of course, I have. Why did you save mine?"
js "..."
mc "Are you too shy to tell me?"
scene ep10_josy_solo65 with dissolve
js "I saved it because..."
js "It's stupid."
if affinity == "CHICK":
    scene ep10_josy_solo64 with dissolve
    mc "I'm not gonna mock you for it."
else:
    scene ep10_josy_solo64 with dissolve
    mc "I'm sure it is."
    scene ep10_josy_solo66 with dissolve
    js "Haha... You're not helping."
scene ep10_josy_solo67 with dissolve
js "I liked looking at it."
scene ep10_josy_solo68 with dissolve
mc "No way."
scene ep10_josy_solo67 with dissolve
js "I told you I had a crush on you, too."
scene ep10_josy_solo68 with dissolve
mc "You really did, didn't you?"
if branchMayaJosy:
    scene ep10_josy_solo85 with dissolve
    js "I still do. A major one."
    scene ep10_josy_solo86 with dissolve
    mc "That...feels so good to hear."
    mc "Me too."
    scene ep10_josy_solo88 with dissolve
    js "*{i}Smack{/i}*"
    scene ep10_josy_solo89 with dissolve
    js "*{i}Smack{/i}*"
    scene ep10_josy_solo87 with dissolve
    js "Do you know what else you can do in a pillow fort?"
    scene ep10_josy_solo86 with dissolve
    mc "Is it the real reason why you put on that lingerie?"
    scene ep10_josy_solo87 with dissolve
    js "Haha... Something like that."
    js "Do you wanna?"
    scene ep10_josy_solo86 with dissolve
    mc "If I ever say no to that, punch me."
else:
    stop music fadeout 3
    scene ep10_josy_solo69 with dissolve
    js "..."
    scene ep10_josy_solo70 with dissolve
    js "I still do."
    play music "music/ep4/all_of_the_pieces.mp3"
    scene ep10_josy_solo69 with dissolve
    mc "..."
    scene ep10_josy_solo71 with dissolve
    js "And saying that out loud isn't something I planned to do. Can we reverse time and undo that?"
    scene ep10_josy_solo72 with dissolve
    mc "Josy..."
    scene ep10_josy_solo73 with dissolve
    js "Look, we both know there's been something between us. We can't deny that."
    js "And I know I shouldn't feel this way when I'm with Maya, but I did in the past and still do."
    if ep9_josy_wonder == 1:
        js "And I know you don't think we would have worked out, but I think we would have."
    elif ep9_josy_wonder == 2:
        js "And - don't lie - I know you still think about it too."
    elif ep9_josy_wonder == 3:
        js "And you told me you think about it all the time, and so do I."
    if branchAlone:
        if ep5_feelingsForJosy and ep9_josy_wonder != 1:
            scene ep10_josy_solo74 with dissolve
            
            if persistent.mod_wt_enabled: 
                    $mod_choices = ["(feelings for Josy)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    
            
            menu:
                "Still have feelings \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep10_feelingsForJosy = True
                "I'm over you":
                    $ ep10_feelingsForJosy = False

        if ep10_feelingsForJosy:
            mc "Since we're being honest here..."
            mc "I haven't been able to let go of my feelings for you, either."
            scene ep10_josy_solo75 with dissolve
            js "..."
            scene ep10_josy_solo74 with dissolve
            mc "I thought that I could. I tried my best, but I still feel them."
            mc "But because of Maya, I want it to be different now."
            mc "It has to be different because you are my friends and we've grown so close."
            scene ep10_josy_solo76 with dissolve
            mc "Back when I didn't know about you two, dismissing that thought and being selfish was easier."
            mc "But now I know that if I do something together with you, I will hurt someone I care about at the same time."
            scene ep10_josy_solo74 with dissolve
            mc "And I fear that by admitting this to you, I've already done it."
            mc "I could see it in your eyes when I told you just now. I could feel the chemistry between us."
            mc "But if I reach out and kiss you..."
            scene ep10_josy_solo78 with dissolve
            mc "..."
            scene ep10_josy_solo79 with dissolve
            js "..."
            scene ep10_josy_solo74 with dissolve
            mc "There's no turning back from it."
            mc "All my power right now goes into focusing on something else. Because you make me feel weak in my knees, Josy."
            scene ep10_josy_solo80 with dissolve
            js "I put on lingerie for you! What's wrong with me!?"
            js "I don't want to cheat. I'm so stupid!"
            scene ep10_josy_solo81 with dissolve
            mc "It didn't happen, Josy. It didn't happen."
            scene ep10_josy_solo80 with dissolve
            js "Something did happen just now, [name]. Something did."
            js "We both admitted how we have feelings for each other. We both looked into each other's eyes, knowing it and picturing what it could be like."
            scene ep10_josy_solo82 with dissolve
            js "Feelings suck. Love sucks. I suck."
            js "What the hell should I do?"
            scene ep10_josy_solo83 with dissolve
            mc "I don't have an answer to what to do, Josy. But I know I can't do this while you're with Maya."
            mc "And I could never tell you to end it with her. I would feel guilty knowing it was my fault you weren't together."
            mc "You have to figure this one out on your own."
            stop music fadeout 3
            $ renpy.music.stop(channel="sfx3", fadeout=3)
            scene ep10_josy_solo84 with dissolve
            js "..."
            $ new_bio("Josy", "I hung out with Josy, and we ended up confessing our feelings to each other. But we both felt guilty doing it because she's with Maya.")
            jump ep10_after_solo_label
        else:
            scene ep10_josy_solo74 with dissolve
            mc "Josy..."
            mc "I'm over you."
            scene ep10_josy_solo75 with dissolve
            js "..."
            scene ep10_josy_solo74 with dissolve
            mc "I know that must hurt to hear, but since this is how you feel about me, you should hear it."
            jump ep10_josy_solo_label2
    else:
        scene ep10_josy_solo74 with dissolve
        if branchSage:
            mc "I'm with Sage..."
            scene ep10_josy_solo73 with dissolve
            js "I know. And I'm with Maya."
            scene ep10_josy_solo74 with dissolve
        if branchJill:
            mc "I'm with Jill..."
            scene ep10_josy_solo73 with dissolve
            js "I know. And I'm with Maya."
            scene ep10_josy_solo74 with dissolve
        else:
            mc "I'm with someone..."
            scene ep10_josy_solo77 with dissolve
            js "I had a feeling you were..."
            scene ep10_josy_solo74 with dissolve
        label ep10_josy_solo_label2:
        mc "Listen... I'm sorry that you still feel that way about me."
        mc "I mean, I'm not sorry because it makes me happy that you like me, but at the same time it makes me sad."
        mc "I don't want you to feel like that about me. I want you to be happy with Maya."
        scene ep10_josy_solo73 with dissolve
        js "I know that's what you want. And I want that, too."
        js "But no matter how much I want that... You've always been on my mind, and I can't seem to shake you."
        scene ep10_josy_solo80 with dissolve
        js "Ugh... I put on lingerie for you. What's wrong with me?"
        js "I don't want to cheat. I'm so stupid."
        scene ep10_josy_solo81 with dissolve
        mc "It didn't happen, Josy. It didn't happen."
        scene ep10_josy_solo80 with dissolve
        js "Are you sure? Can you pretend I didn't say these things to you?"
        scene ep10_josy_solo81 with dissolve
        mc "I'll try."
        scene ep10_josy_solo82 with dissolve
        js "Feelings suck. Love sucks. I suck."
        scene ep10_josy_solo83 with dissolve
        mc "Honestly, you should talk to Maya about how you feel."
        mc "We already did that together once, but I think it's bad if you hide what just happened from her."
        scene ep10_josy_solo82 with dissolve
        js "Do you want me to tell her that I put on lingerie for you and told you I have a crush on you?"
        scene ep10_josy_solo83 with dissolve
        mc "Maybe not the first part, but I don't think you will be happy with her if you hide your feelings. You don't seem happy, Josy."
        mc "And if I were Maya, I'd want to know this even though it would hurt."
        stop music fadeout 3
        $ renpy.music.stop(channel="sfx3", fadeout=3)
        scene ep10_josy_solo84 with dissolve
        js "..."
        $ new_bio("Josy", "I hung out with Josy, and she ended up confessing her feelings to me.")
        jump ep10_after_solo_label

label ep10_josy_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_josy == None:
        $ mc_josy = name
    else:
        $ mc_josy = persistent.mc_josy
    if persistent.josy == None:
        $ josy = "Josy"
    else:
        $ josy = persistent.josy

    $ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx3", loop=True)
    play music "music/ep10/licensed_music/track145.mp3"
    queue music ["music/ep7/licensed_music/track58.mp3"]
hide screen new_phone_screen

scene ep10_josy_lewd1 with dissolve
if _in_replay:
    menu:
        "Shaven version":
            $ ep5_josy_shaven = True
            $ ep5_followed_josy = True
        "Pubic hair version":
            $ ep5_josy_shaven = False
            $ ep5_followed_josy = True
mc "I'm gonna remove the rest of my clothes and be right back with you."
scene ep10_josy_lewd2 with dissolve
js "[mc_josy]... I want it."
scene ep10_josy_lewd3 with dissolve
mc "Where do you want it?"
scene ep10_josy_lewd4 with dissolve
js "I want it in my mouth."
scene ep10_josy_lewd5 with dissolve
$ renpy.pause()
scene anim_josy_bj1_ep10 with dissolve
js "*{i}Lick suck{/i}*"
mc "That feels amazing... I fucking love blowjobs."
mc "Those pigtails... They make me wanna do nasty things to you."
pause
scene ep10_josy_lewd6 with dissolve
js "Get in here and I'll let you."
scene anim_josy_bj2_ep10 with dissolve
js "*{i}Suck glug glug{/i}*"
mc "Fuck! That's so good!"
pause
scene ep10_josy_lewd7 with dissolve
js "*{i}Cough{/i}*"
mc "Shit! Did I go too hard?"
scene ep10_josy_lewd8 with dissolve
js "I'll be fine. I'm still not used to going that deep."

scene ep10_josy_lewd9 with dissolve
mc "Relax for a bit. Let me take care of you."
scene ep10_josy_lewd10 with dissolve
$ renpy.pause()
scene ep10_josy_lewd11 with dissolve
$ renpy.pause()
scene anim_josy_tits_ep10 with dissolve
mc "*{i}Lick lick{/i}*"
js "*{i}Soft moan{/i}*"
pause

if ep5_followed_josy and not ep5_josy_shaven:
    scene ep10_josy_lewd13 with dissolve
    js "I did something for you."
    mc "You did that for me?"
    scene ep10_josy_lewd14 with dissolve
    js "Mhm. Do you like it?"
    mc "Yeah, it's hot! What about you? Do you like it?"
    scene ep10_josy_lewd18 with dissolve
    js "I'm not that crazy about it; I prefer to be shaven."
    js "But I wanted to do this for you."
    scene ep10_josy_lewd17 with dissolve
    mc "You have no idea how much I appreciate that."
else:
    scene ep10_josy_lewd12 with dissolve
    mc "There it is."
    scene ep10_josy_lewd16 with dissolve
    js "Haha, that smile..."
    scene ep10_josy_lewd15 with dissolve
    mc "It's like meeting an old friend."
    js "Haha, eww!"
    scene ep10_josy_lewd17 with dissolve
    mc "I mean, not like an actual friend. I don't look at them this way. It would be creepy."
    scene ep10_josy_lewd16 with dissolve
    js "Haha! Just shush!!! Don't ruin this."

scene ep10_josy_lewd18 with dissolve
js "Can you eat me?"
scene ep10_josy_lewd17 with dissolve
mc "Fuck yes, I wanna taste you."
if ep5_followed_josy and not ep5_josy_shaven:
    scene anim_josy_lick1_ep10 with dissolve
else:
    scene anim_josy_lick2_ep10 with dissolve
js "*{i}Moans{/i}* Yes! Go slower with your tongue, [mc_josy]."


scene ep10_josy_lewd19 with dissolve
js "Enter me, [mc_josy]. I want you."
if ep5_followed_josy and not ep5_josy_shaven:
    scene ep10_josy_lewd20b with dissolve
else:
    scene ep10_josy_lewd20 with dissolve
$ renpy.pause()
if ep5_followed_josy and not ep5_josy_shaven:
    scene ep10_josy_lewd21b with dissolve
else:
    scene ep10_josy_lewd21 with dissolve
js "*{i}Moans{/i}*"

scene anim_josy_doggy1_ep10 with dissolve
pause
scene anim_josy_doggy2_ep10 with dissolve
js "*{i}Moans{/i}* Fuck me, [mc_josy]. I love your cock inside me."
pause

$ tmpInt = 0
label ep10_josy_lewd_loop_label:
menu:
    "Doggystyle":
        $ tmpInt += 1
        scene anim_josy_doggy1_ep10 with dissolve
        js "*{i}Moans{/i}*"
        pause
        scene anim_josy_doggy2_ep10 with dissolve
        pause
        jump ep10_josy_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        if ep5_followed_josy and not ep5_josy_shaven:
            scene anim_josy_ride1_ep10 with dissolve
        else:
            scene anim_josy_ride1b_ep10 with dissolve
        mc "Ride me, [josy]."
        js "Uh-huh."
        pause

        scene anim_josy_ride2_ep10 with dissolve
        mc "You look so hot doing that. I can feel the desire in your eyes."
        js "*{i}Moans{/i}* I want you, [mc_josy]. I want all of you."
        pause

        if ep5_followed_josy and not ep5_josy_shaven:
            scene anim_josy_ride3_ep10 with dissolve
        else:
            scene anim_josy_ride3b_ep10 with dissolve
        mc "Yeah. Keep riding my cock."
        js "*{i}Moans{/i}*"
        pause
        jump ep10_josy_lewd_loop_label
    "Sideways":
        $ tmpInt += 1
        if ep5_followed_josy and not ep5_josy_shaven:
            scene anim_josy_side1_ep10 with dissolve
        else:
            scene anim_josy_side1b_ep10 with dissolve
        js "Ahhh... Fuck, [mc_josy]... That's so deep."
        mc "Yeah, I'm pushing it in all the way."
        js "Ahhhh... *{i}Moans{/i}*"
        pause
        scene anim_josy_side2_ep10 with dissolve
        js "You're so fucking big. Like fuck... Just when I think I've gotten used to it, it feels like it grew longer."
        mc "If it hurts, let me know."
        js "It's not a pain that I mind. *{i}Moans{/i}*"
        pause
        jump ep10_josy_lewd_loop_label
    "Prone":
        $ tmpInt += 1
        scene anim_josy_prone1_ep10 with dissolve
        mc "Oh, [josy]... Your ass makes me go crazy."
        mc "Take my cock."
        pause
        scene anim_josy_prone2_ep10 with dissolve
        js "Give it to me, [mc_josy]. *{i}Moans{/i}*"
        pause
        jump ep10_josy_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        if ep5_followed_josy and not ep5_josy_shaven:
            scene anim_josy_miss1_ep10 with dissolve
            pause
        else:
            scene anim_josy_miss2_ep10 with dissolve
            pause
        js "Yes... Keep going like that..."
        jump ep10_josy_lewd_loop_label
    "Cum" if tmpInt > 2:
        menu:
            "Cum together":
                if ep5_followed_josy and not ep5_josy_shaven:
                    scene anim_josy_ride1_ep10 with dissolve
                else:
                    scene anim_josy_ride1b_ep10 with dissolve
                js "[mc_josy]... I'm so...close..."
                mc "Me too."
                js "Can we...cum...together?"
                mc "Yeah. Let's do it. Cum, [josy]."
                js "I'm...cumming..."
                scene ep10_josy_lewd22 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_josy_lewd22 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_josy_lewd22 at vpunch, cum1
                js "*{i}Moans{/i}* Ahhh!!! [mc_josy]!!!"
                if ep5_followed_josy and not ep5_josy_shaven:
                    scene anim_josy_ride4_ep10 with vpunch
                else:
                    scene anim_josy_ride4b_ep10 with vpunch
                mc "Fuck!!! Ahh..."
                if ep5_followed_josy and not ep5_josy_shaven:
                    scene ep10_josy_lewd23 with dissolve
                else:
                    scene ep10_josy_lewd23b with dissolve
                $ renpy.pause()
            "In mouth":
                scene anim_josy_bj2_ep10 with dissolve
                js "*{i}Suck suck{/i}*"
                mc "I'm gonna cum if you keep going like that..."
                mc "[josy]? I'm not joking... Fuck... I'm gonna shoot my load in your mouth."
                js "*{i}Suck suck{/i}* Mmm..."
                pause
                scene ep10_josy_lewd24 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_josy_lewd24 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_josy_lewd24 at vpunch, cum1
                mc "Ahhh!!! [josy]! Fuck!!!"
                scene ep10_josy_lewd25 with dissolve
                mc "Fuck... That was too good."
                scene ep10_josy_lewd26 with dissolve
                js "*{i}Lick lick{/i}*"
            "On pussy":
                if ep5_followed_josy and not ep5_josy_shaven:
                    scene anim_josy_side1_ep10 with dissolve
                else:
                    scene anim_josy_side1b_ep10 with dissolve
                mc "[josy]... I'm cumming."
                js "Cum for me, [mc_josy]... Cum!!!"
                if ep5_followed_josy and not ep5_josy_shaven:
                    scene ep10_josy_lewd27 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep10_josy_lewd27 at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep10_josy_lewd28 at vpunch, cum2
                else:
                    scene ep10_josy_lewd27b at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep10_josy_lewd27b at vpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep10_josy_lewd28b at vpunch, cum2
                mc "Ahhh!!! [josy]! Fuck!!!"
            "On ass":
                scene anim_josy_prone1_ep10 with dissolve
                mc "I can't hold it back any longer... I'm gonna cum."
                js "Cum for me, [mc_josy]. Cum!!!"
                scene ep10_josy_lewd29 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_josy_lewd29 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_josy_lewd29 at vpunch, cum2
                mc "Ahhh!!! [josy]! Fuck!!!"
                scene ep10_josy_lewd30 with dissolve
                mc "Your pretty little ass looks so sexy, covered in cum."


scene ep10_josy_lewd31 with dissolve
$ renpy.pause()
scene ep10_josy_lewd33 with dissolve
js "Never did that in a pillow fort before."
scene ep10_josy_lewd32 with dissolve
mc "Haha. Nope."
scene ep10_josy_lewd33 with dissolve
js "You even made me forget about the thunderstorm."
scene ep10_josy_lewd32 with dissolve
mc "Don't fall asleep now."
scene ep10_josy_lewd33 with dissolve
js "Haha, I probably could. I feel so at peace."
scene ep10_josy_lewd32 with dissolve
mc "Sex will do that."
scene ep10_josy_lewd32b with dissolve
$ renpy.pause()
scene ep10_josy_lewd34 with dissolve
js "You're not leaving yet, are you?"
scene ep10_josy_lewd35 with dissolve
mc "I'm not in a rush. We got all night if we want."
scene ep10_josy_lewd33 with dissolve
js "Good. Let's get some ice cream. You made me hungry for it."
stop music fadeout 3
scene ep10_josy_lewd36 with dissolve
$ renpy.pause()

$ renpy.music.stop(channel="sfx3", fadeout=3)

$ renpy.end_replay()
$ persistent.ep10_lewd_josy = True
$ calcScenes()
$ new_bio("Josy", "I hung out with Josy and had such a great time with her. We built a pillow fort that we had sex in.")
$ mphone_stats_add_girl_s3("josy","You had sex with Josy in a pillow fort in episode 10.")

$ mgallery_add_photo("ep10_josy_solo_pic1")
$ mgallery_add_photo("ep10_josy_solo_pic2")
show screen new_phone_screen

jump ep10_after_solo_label

label ep10_after_solo_label:

scene ep10_after_solo1 with fade
play music "music/ep6/licensed_music/track20.mp3"
$ renpy.pause()
scene ep10_after_solo2 with dissolve
mc "(Maybe I could let it grow? That will show them...)"

if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy") and branchMayaJosy:
    scene ep10_after_solo2b with dissolve
    my "What are you thinking about?"
    scene ep10_after_solo2c with dissolve
    mc "Oh, it's nothing."
    scene ep10_after_solo2d with dissolve

play sound "sound_effects/door_knob.mp3"
jac "Is someone in there? I just wanna brush my teeth."
if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy") and branchMayaJosy:
    scene ep10_after_solo2e with dissolve
    mc "What do you say?"
    my "It's fine by me. I'm done here."
    scene ep10_after_solo2f with dissolve
else:
    scene ep10_after_solo3 with dissolve
mc "Go ahead."
if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy") and branchMayaJosy:
    jac "Oh, sorry. I thought you were alone in here."
else:
    jac "Thanks, bro."

if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy") and branchMayaJosy:
    scene ep10_after_solo2h with dissolve
    my "I was going to leave now, anyway."
    scene ep10_after_solo2i with dissolve
    my "*{i}Smack{/i}* See you soon."
    scene ep10_after_solo8 with dissolve
    jac "You're one lucky son of a bitch."
    scene ep10_after_solo7 with dissolve
    mc "Haha, I can't complain."

scene ep10_after_solo4 with dissolve
mc "How often do you shave?"
scene ep10_after_solo5 with dissolve
jac "I trim my beard every other day."
scene ep10_after_solo4 with dissolve
mc "That often? Ever shave your body?"
scene ep10_after_solo5 with dissolve
jac "All the time. Both my beard and body hair grow like weeds."
scene ep10_after_solo4 with dissolve
mc "Yeah, yeah. Me too..."
scene ep10_after_solo6 with dissolve
jac "What are you up to today?"
scene ep10_after_solo7 with dissolve
if branchJill:
    mc "I'm meeting Jill's parents today."
    scene ep10_after_solo6 with dissolve
    jac "First time?"
    scene ep10_after_solo4 with dissolve
    mc "Yeah... I'm nervous."
    scene ep10_after_solo6 with dissolve
    jac "I don't know a lot about the Royces, but I'd be nervous, too."
    jac "You only get one shot at making that first impression. If you blow it that's what they'll remember."
    scene ep10_after_solo7 with dissolve
    mc "Man... Why did you have to say that?"
    mc "I didn't even think about that, but now I will."
    scene ep10_after_solo6 with dissolve
    jac "Oh... Then what are you worried about?"
    scene ep10_after_solo4 with dissolve
    mc "Many things...but mostly that I'll stick out like a sore thumb."
    mc "I don't know that much about them either, but I'm definitely different from them."
    scene ep10_after_solo12 with dissolve
    mc "Wish me luck."
    stop music fadeout 3
    jac "You've got this, bro."
if branchIsabella:
    mc "Today? Not a lot. Gonna study some and later tonight, I've got this thing..."
    scene ep10_after_solo6 with dissolve
    jac "What thing?"
    scene ep10_after_solo7 with dissolve
    mc "Just a thing."
    mc "I'll be back tomorrow."
    scene ep10_after_solo6 with dissolve
    jac "An overnight thing? That thing sounds like a fling."
    scene ep10_after_solo4 with dissolve
    mc "It's...uh..."
    scene ep10_after_solo8 with dissolve
    jac "Haha. You don't have to tell me about it. It's fresh, huh?"
    scene ep10_after_solo4 with dissolve
    mc "Yeah."
    scene ep10_after_solo6 with dissolve
    jac "Good luck with it."
    scene ep10_after_solo7 with dissolve
    mc "Thanks. What about you?"
    scene ep10_after_solo6 with dissolve
    jac "Not much. Might drop by a classmate tonight for some beers."
    scene ep10_after_solo7 with dissolve
    mc "No party tonight?"
    scene ep10_after_solo8 with dissolve
    jac "We'll see where the night takes us."
    stop music fadeout 3
    scene ep10_after_solo12 with dissolve
    mc "Have fun."
if branchSage:
    mc "I'm gonna spend the day with Sage."
    scene ep10_after_solo6 with dissolve
    jac "Yeah? I heard you two were a thing or something."
    scene ep10_after_solo4 with dissolve
    mc "We're not a thing. It's...uh... I don't know what you'd call it."
    mc "I guess we're dating. But we haven't been on a date."
    scene ep10_after_solo6 with dissolve
    jac "But you fucked?"
    scene ep10_after_solo7 with dissolve
    mc "Oh, yeah."
    scene ep10_after_solo8 with dissolve
    jac "I'd call that dating."
    scene ep10_after_solo7 with dissolve
    mc "I have high hopes for it."
    scene ep10_after_solo6 with dissolve
    jac "Man, who wouldn't? Sage is a beauty."
    jac "I'm rooting for you. Congrats!"
    stop music fadeout 3
    scene ep10_after_solo12 with dissolve
    mc "Thanks."
if branchMayaJosy:
    mc "I'm gonna hang out with my girlfriends."
    scene ep10_after_solo6 with dissolve
    jac "Man..."
    jac "I don't wanna think about the things you're gonna do."
    scene ep10_after_solo7 with dissolve
    mc "We'll probably just study."
    scene ep10_after_solo6 with dissolve
    jac "Yeah, but still. Two at the same time... How did you even get them to agree on that?"
    scene ep10_after_solo7 with dissolve
    mc "Who knows?"
    scene ep10_after_solo8 with dissolve
    jac "Are you not gonna tell me about it?"
    scene ep10_after_solo12 with dissolve
    mc "Maybe someday."
    stop music fadeout 3
    scene ep10_after_solo13 with dissolve
    jac "Haha. Fucking legend."
if ep10_date_nicole and not ep10_cancel_date_nicole:
    mc "I've got a date tonight."
    scene ep10_after_solo6 with dissolve
    jac "Awesome! Who with?"
    scene ep10_after_solo7 with dissolve
    mc "Nicole."
    scene ep10_after_solo6 with dissolve
    jac "Nicole who-?"
    scene ep10_after_solo9 with vpunch
    jac "Envy!?"
    scene ep10_after_solo10 with dissolve
    mc "That's Nicole, yeah."
    scene ep10_after_solo8 with dissolve
    jac "Dude! Details! How did that happen?"
    scene ep10_after_solo7 with dissolve
    mc "It started at The Pink Rose, and after that, we got a connection."
    mc "We had some fun together and she asked me out on a date."
    scene ep10_after_solo6 with dissolve
    jac "Bullshit."
    scene ep10_after_solo4 with dissolve
    mc "She did."
    scene ep10_after_solo6 with dissolve
    jac "When did she ask you?"
    scene ep10_after_solo7 with dissolve
    mc "The morning after Halloween."
    scene ep10_after_solo6 with dissolve
    jac "You banged her?"
    scene ep10_after_solo7 with dissolve
    mc "I don't like to kiss and tell, but yeah. I had a threesome with her and Lily."
    scene ep10_after_solo8 with dissolve
    jac "Haha, just when I thought you were serious."
    scene ep10_after_solo4 with dissolve
    mc "I did."
    scene ep10_after_solo6 with dissolve
    jac "Who are you really dating tonight?"
    scene ep10_after_solo7 with dissolve
    mc "Haha! Nicole! I'm not lying."
    scene ep10_after_solo9 with dissolve
    jac "You had a threesome with Nicole and Lily?"
    scene ep10_after_solo10 with dissolve
    mc "That's what I've been telling you."
    scene ep10_after_solo9 with dissolve
    jac "You're a fucking God. Bro... How?"
    scene ep10_after_solo4 with dissolve
    mc "I don't know... I was being myself and it kinda happened."
    scene ep10_after_solo11 with dissolve
    jac "You're being serious, right?"
    scene ep10_after_solo7 with dissolve
    mc "Hey, don't believe me, then. It's your choice."
    scene ep10_after_solo12 with dissolve
    mc "I'll send you a pic from my date tonight."
    if not (branchAlone and ep9_riona_choice == "DIK"):
        stop music fadeout 3
    scene ep10_after_solo13 with dissolve
    jac "He's lying. Haha. Classic [name]."
if ep10_dating_nora:
    mc "I've got a date tonight."
    scene ep10_after_solo6 with dissolve
    jac "Awesome! Who with?"
    scene ep10_after_solo7 with dissolve
    mc "You don't know her. I met her on Swyper and we go to the same gym."
    scene ep10_after_solo6 with dissolve
    jac "Is she hot?"
    scene ep10_after_solo7 with dissolve
    mc "She's smoking."
    scene ep10_after_solo6 with dissolve
    jac "What class is she?"
    scene ep10_after_solo4 with dissolve
    mc "She's not a student. She works with something. I haven't asked yet."
    scene ep10_after_solo6 with dissolve
    jac "Yeah? Young, though?"
    scene ep10_after_solo7 with dissolve
    mc "Yeah, pretty young. Early thirties."
    scene ep10_after_solo8 with dissolve
    jac "Thirties!? Dude... Are you into older chicks?"
    scene ep10_after_solo7 with dissolve
    mc "Obviously. Her body is amazing and she's like super-smart."
    scene ep10_after_solo8 with dissolve
    jac "Sheesh. I'm jelly."
    jac "Where are you taking her?"
    scene ep10_after_solo7 with dissolve
    mc "She invited me over to her place for drinks."
    scene ep10_after_solo6 with dissolve
    jac "Drinks, huh? Sounds like she wants some."
    scene ep10_after_solo4 with dissolve
    mc "You think?"
    scene ep10_after_solo8 with dissolve
    jac "A girl doesn't invite you to her place for drinks unless she's into you."
    jac "Plus, it's fast and easy access to a bed."
    if not (branchAlone and ep9_riona_choice == "DIK"):
        stop music fadeout 3
    scene ep10_after_solo12 with dissolve
    mc "Huh, maybe. But I think it will be drinks and she'll show me her place - and that's that. I'm not gonna expect something more."
    if branchAlone and ep9_riona_choice == "DIK":
        jac "You never know. Have fun."
else:
    mc "Not a damned thing."
    scene ep10_after_solo6 with dissolve
    jac "Later tonight, I'm having beers with some classmates. You're free to come if you want."
    scene ep10_after_solo7 with dissolve
    mc "Thanks for the invite, but I think I'm gonna take it slow for once."
    scene ep10_after_solo6 with dissolve
    jac "Suit yourself."
    jac "Leon and I are gonna shoot some hoops. Join if you're bored."
    scene ep10_after_solo12 with dissolve
    mc "Cool."

if branchJill:
    jump ep10_jill_fam_label
if branchMayaJosy:
    jump ep10_mj_solo_label

if branchSage:
    jump ep10_sage_solo_label

if branchAlone and ep9_riona_choice == "DIK":
    jump ep10_rio_solo_label    

if ep10_dating_nora:
    jump ep10_nora_date_label    

    
if branchIsabella:
    jump ep10_bella_solo_label    


    
if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label

label ep10_science_label:
show screen new_phone_screen
scene ep10_science1 with Fade(2,2,2)
play music "music/ep_interlude/licensed_music/track108.mp3"
$ renpy.pause()
scene ep10_science21 with dissolve
mc "Do you think I'd look good with a beard?"
scene ep10_science23 with dissolve
de "Can you grow one?"
scene ep10_science21 with dissolve
mc "I shave, dude. Of course, I can."
scene ep10_science23 with dissolve
de "All right, I thought you couldn't."
scene ep10_science21 with dissolve
mc "Why? Because of the poster?"
scene ep10_science23 with dissolve
de "Huh?"
scene ep10_science22 with dissolve
mc "The no body hair comment. Is that why you thought I couldn't grow one?"
scene ep10_science24 with dissolve
de "No, I didn't think about it that much, but when you asked just now I thought you couldn't. That's all."
scene ep10_science22 with dissolve
mc "Well, I can. It grows a lot, I'll have you know."
scene ep10_science24 with dissolve
de "Then go for it. It might look cool."
scene ep10_science21 with dissolve
mc "Sorry for snapping at you..."
scene ep10_science23 with dissolve
de "Those posters got to all of us. I'm surprised you kept it in for this long."
scene ep10_science2 with dissolve
mc "I guess we're set for Thanksgiving."
scene ep10_science3 with dissolve
de "Yep, I've picked up our communication system."
scene ep10_science2 with dissolve
mc "Communication system? Like phones?"
scene ep10_science3 with dissolve
de "We can't rely on our phones for this. It needs to be subtle."
scene ep10_science2 with dissolve
mc "Will you tell me what it is?"
scene ep10_science3 with dissolve
de "I'll do you one better. I can show you. But don't be all judgmental about it, ok?"
scene ep10_science4 with dissolve
mc "What is that?"
de "A remote vibrator."
mc "How the hell is that subtle? You're insane."
scene ep10_science5 with dissolve
de "It works perfectly! Press a button and it vibrates. That's how we can warn each other!"
de "Now, am I insane or am I a genius?"
scene ep10_science6 with dissolve
mc "..."
mc "Insane."
scene ep10_science5 with dissolve
de "While it would be the easiest way to conceal it, I'm not asking you to shove it up your asshole, [mc_de]."
de "You put the vibrator in your pocket, and I keep the controller in mine."
de "A communication system! It has a great range too!"
scene ep10_science6 with dissolve
mc "Do you know what else has a great range? Our phones. Can't we use them?"
scene ep10_science4 with dissolve
de "Anyone could call or text when we snoop around. With this communication system, you'd know who's sending the message without checking your pocket for it."
de "Try it with me. Put the button in your pants and press it."
scene ep10_science7 with dissolve
mc "*{i}Sigh{/i}*"
play sound "sound_effects/season2/vibrator.mp3"
scene anim_vibrator_ep10 with vpunch
"*{i}Vibration{/i}*"
de "Whoa! That's way too much."
play sound "sound_effects/season2/vibrator.mp3"
scene ep10_science20 with dissolve
te5 "Whose phone is that? Turn it off."
scene ep10_science8 with dissolve
play sound "sound_effects/season2/vibrator.mp3"
de "Turn it off, [mc_de]."
mc "I'm fucking trying to!"
scene ep10_science20 with dissolve
te5 "*{i}Cough{/i}*"
scene ep10_science9 with dissolve
mc "It's off. It's off..."
scene ep10_science10 with dissolve
de "We need to practice on this."
scene ep10_science11 with dissolve
mc "The vibration is way too much. There's nothing subtle about it."
scene ep10_science10 with dissolve
de "You can adjust it. Let me set it up for us. Trust me on this."
scene ep10_science11 with dissolve
mc "Ok..."

scene ep10_science12 with dissolve
mc "Are there any other surprises you have planned for me? I want to go in knowing as much as possible beforehand."
scene ep10_science13 with dissolve
de "There are no more surprises. I swear."
scene ep10_science14 with dissolve
de "..."
scene ep10_science15 with dissolve
de "Um...wait... Maya told you about Mom, right?"
scene ep10_science14 with dissolve
if branchMayaJosy:
    mc "Almost. I got the feeling she didn't want to talk about her and that it's a sensitive topic."
    scene ep10_science15 with dissolve
    de "Yeah... It kinda is."
else:
    mc "Nope. What about her?"
    scene ep10_science15 with dissolve
de "There is something you should know."
de "Our Mom is chronically ill."
scene ep10_science14 with dissolve
mc "Ok? How ill?"
scene ep10_science15 with dissolve
de "It's hard to know for sure. She hasn't worked since we were kids and gets worse with every year."
de "It's rough to talk about, but you'd have questions about it after Thanksgiving anyway."
scene ep10_science14 with dissolve
mc "What's her illness?"
scene ep10_science15 with dissolve
de "Rheumatism. It's a rare case of it, too."
scene ep10_science14 with dissolve
mc "Is that like arthritis?"
scene ep10_science16 with dissolve
de "Yeah, and a lot of other stuff that comes with it. It's gotten worse every year since she got her diagnosis."
de "Her immune system is shit. She's at the point where she eats medicine so she can eat her real medicine to avoid side effects."
de "It's broken her down completely."
scene ep10_science17 with dissolve
mc "Dude... I'm so sorry to hear that."
scene ep10_science15 with dissolve
de "It's cool. I can handle it pretty well these days."
de "I've thought Mom was going to die every day since I was like five."
scene ep10_science16 with dissolve
de "After thinking and worrying about it for that long, it gets easier to handle with every year that passes."
de "I mean... You have to be able to handle it and live your life or there's no point."
scene ep10_science17 with dissolve
mc "I don't know what to say..."
scene ep10_science15 with dissolve
de "I wanted you to know. In case she says something weird or acts inappropriate, it's her dementia."
scene ep10_science14 with dissolve
mc "Dementia too?"
scene ep10_science15 with dissolve
de "Vascular dementia, yeah. Like I said, it's bad."
if branchMayaJosy:
    scene ep10_science14 with dissolve
    mc "Fuck... Poor Maya. I hope I didn't push her too hard on it."
    scene ep10_science15 with dissolve
    de "It's not news to her that Mom's sick. She doesn't cope with it in the same way as I do."
scene ep10_science14 with dissolve
mc "..."
scene ep10_science18 with dissolve
de "Boy, we're so not listening to what the Cock professor is yapping about. Am I right?"
scene ep10_science19 with dissolve
mc "I've learned to read ahead in advance, knowing that I have to sit next to you in class."
stop music fadeout 3
scene ep10_science18 with dissolve
de "You're such a nerd, [mc_de]."
$ new_bio("Derek", "Derek told me about his mom and her illness. It was tough hearing about it, and I understood why it was a sensitive issue for him and Maya.")

label ep10_lab_label:
$ guideSuggestedPage = 132
play music "music/ep8/licensed_music/track67.mp3"
show ep10_lab1
if not persistent.ep10_cardzo8:
    show screen ep10_render_screen("zo8")
with wipeleft
de "I feel pretty cool in this lab coat."
show ep10_lab3
hide screen ep10_render_screen
with dissolve
mc "Yeah, until you wear the safety goggles. Then you don't."
scene ep10_lab2 with dissolve
de "I'm not gonna wear those."
scene ep10_lab4 with dissolve
eu "Actually, goggles aren't optional. Safety comes first!"
scene ep10_lab6 with dissolve
de "You're not my teacher."
scene ep10_lab5 with dissolve
eu "While that is true, I have taken several scientific classes and become quite experienced with lab work."
eu "Goggles are always mandatory. If you get acid in your eyes, then what will you do?"
scene ep10_lab6 with dissolve
de "Yeah, yeah. Go away."
scene ep10_lab5 with dissolve
eu "By the way, the answer to that question is to use the emergency eyewash station."
scene ep10_lab7 with dissolve
de "[mc_de_up]. Look! They have a shower in here."
mc "Don't do anything stupid with it."

scene ep10_lab8 with dissolve
$ renpy.pause()
if ep10_nora_lewd or ep6_nora_lewd:
    scene ep10_lab9 with dissolve
    $ renpy.pause()
    scene ep10_lab10 with dissolve
    no "No... No."
    scene ep10_lab11 with dissolve
    mc "Nora?"
    scene ep10_lab12 with dissolve
    mc "What are you doing here?"
    scene ep10_lab13 with dissolve
    if ep10_nora_lewd:
        no "Why haven't you told me that you are a student?"
    else:
        no "Are you a student here?"
    scene ep10_lab14 with dissolve
    if ep10_nora_lewd:
        mc "Haven't I? Uh... I thought I did. Wait... Are you a teacher?"
    else:
        mc "Yeah. What the hell! Are you my teacher?"
    scene ep10_lab15 with dissolve
    no "I'm not a teacher, per se. I'm a scientist and this is just a minor part of my salary."
    scene ep10_lab14 with dissolve
    mc "But you're teaching this class, no?"
    scene ep10_lab15 with dissolve
    no "Yes. And I surely didn't expect to see you here."
    no "You have to promise not to tell anyone about us. It would look bad."
    scene ep10_lab14 with dissolve
    if affinity == "DIK":
        mc "Maybe you would look bad, but me? Not so much."
        scene ep10_lab16 with dissolve
        mc "Bad time for that joke..."
    else:
        mc "Yeah, totally."
    scene ep10_lab15 with dissolve
    no "Get in there. Class is about to begin."
    scene ep10_lab19 with dissolve
    no "(Damn it! Stay calm. Stay professional and think about this later.)"
elif ep8_nora_number or swyper_nora_state == "ep5_done":
    scene ep10_lab9b with dissolve
    $ renpy.pause()
    scene ep10_lab10 with dissolve
    no "You've got to be kidding me."
    scene ep10_lab12 with dissolve
    if ep8_nora_number:
        mc "Nora..."
    else:
        mc "Oh, wait... We chatted on Swyper, didn't we?"
    scene ep10_lab17 with dissolve
    no "I believe I have dodged a bullet with you."
    no "Are you a student?"
    scene ep10_lab18 with dissolve
    mc "Yeah. Didn't I tell you that?"
    scene ep10_lab17 with dissolve
    no "You most definitely did not."
    scene ep10_lab18 with dissolve
    mc "And you... You're a teacher?"
    scene ep10_lab17 with dissolve
    no "It's not my primary profession. It's more of a work task I do as a part of my salary."
    scene ep10_lab18 with dissolve
    mc "I see..."
    scene ep10_lab17 with dissolve
    if ep8_nora_number:
        no "If you'll excuse me, I will now pretend as if I never squatted in front of you."
    else:
        no "If you'll excuse me, I will now pretend I never swiped up on you."
    scene ep10_lab20 with dissolve
    no "Good afternoon, everybody. We'll begin shortly."
else:
    scene ep10_lab20 with dissolve
    no "Good afternoon, everybody. We'll begin shortly."

$ renpy.sound.play("sound_effects/shower.mp3", channel="sfx1", loop=False)
scene ep10_lab21 with vpunch
de "Whoa!"
mc "What are you doing?"
scene ep10_lab22 with dissolve
no "Release that handle!"
$ renpy.music.stop(channel="sfx1", fadeout=1)
scene ep10_lab23 with dissolve
de "The shower works."
scene ep10_lab25 with dissolve
no "This is not how I wanted to introduce myself to you today, but if you touch things you're not supposed to touch in here, you will be asked to leave."
scene ep10_lab26 with dissolve
no "That goes for you, too."
scene ep10_lab24 with dissolve
mc "I didn't do anything."
scene ep10_lab25 with dissolve
no "You two are working together. That's your punishment."
scene ep10_lab27 with dissolve
de "Haha, what a sucker. That's not punishment at all."
play sound "sound_effects/shove.mp3"
scene ep10_lab28 with hpunch
de "Ouch!"
scene ep10_lab29 with dissolve
de "[mc_de_up]..."
de "Lab partners!"
scene ep10_lab30 with dissolve
no "Welcome to the practical part of the course. I'm Dr. Nora Jenkins and I will be your supervisor."
no "I see a couple of familiar faces here from other courses. Most of what I say won't surprise you, but you'll have to bear with me for the sake of everyone else who's here for the first time."
scene ep10_lab31 with dissolve
no "We will learn how to work professionally in a laboratory environment during our sessions."
no "That includes using the lab equipment correctly and learning to measure, weigh, mix and assess chemicals properly."
scene ep10_lab32 with dissolve
no "You will be working with hazardous chemicals and must read the risk assessments before you're allowed to begin work."
no "Keep lab coats and safety goggles on at all times during class. Wear gloves when you need them."
scene ep10_lab33 with dissolve
no "There are hazardous, transparent and odorless solutions you might catastrophically mistake for water."
no "For this reason, if I see anyone drinking or eating during class, you will be banished."
no "Safety is key and I have no humor when it comes to this."
scene ep10_lab34 with dissolve
li "*{i}Mumbles{/i}* This is bullshit..."
scene ep10_lab31 with dissolve
no "You will be working in pairs with your assignments. Follow the instructions for the experiments and ask me if you need assistance along the way."
$ tutorial_ongoing = False
if minigames:
    hide screen new_phone_screen
if minigames and (tutorials or not persistent.science_tutorial):
    menu:
        "Watch tutorial":
            $ persistent.science_tutorial = True
            $ tutorial_ongoing = True
        "Skip tutorial":
            $ tutorial_ongoing = False
if minigames and tutorial_ongoing:
    $ renpy.block_rollback()
    scene science_minigame_neutral
    show screen science_tut_screen
    with dissolve
    pause
    label ep10_science_tut0_label:
    scene ep10_lab35
    hide screen science_tut_screen
    with dissolve
else:
    scene ep10_lab35 with dissolve
no "Now, let's start by learning how to weigh salts."
no "A scale is most accurate when the difference in weight between the container and the chemical is low."
scene ep10_lab36 with dissolve
no "Therefore, use a small beaker or a weighing dish when weighing small amounts."
no "Reset the scale after you put the weighing dish or beaker on it and add your chemical."
if minigames and tutorial_ongoing:
    show screen sm_weigh_tut_screen
    pause
    label ep10_science_tut1_label:
    scene ep10_lab35
    hide screen sm_weigh_tut_screen
    with dissolve
    $ sm_weigh_result = 0
else:
    scene ep10_lab35 with dissolve
no "Don't forget to weigh your beakers after you apply the chemical and adjust your calculations for the error."
if minigames and tutorial_ongoing:
    $ sm_tut_text = 10
    $ sm_scale_str = "full"
    scene science_minigame_neutral
    show screen science_tut_screen
    with dissolve
    pause
    label ep10_science_tut1b_label:
    scene ep10_lab37
    hide screen science_tut_screen
    with dissolve
    $ sm_weigh_result = 0
else:
    scene ep10_lab37 with dissolve
no "When measuring liquids, use pipettes for smaller volumes and volumetric flasks for larger volumes."
if minigames and tutorial_ongoing:
    show screen sm_measure_tut_screen
    pause
    label ep10_science_tut2_label:
    scene ep10_lab38
    hide screen sm_measure_tut_screen
    with dissolve
    $ sm_measure_phase = 0
else:
    scene ep10_lab38 with dissolve
no "When the meniscus is even with the graduation mark, that's when you have measured the perfect volume."

if minigames and tutorial_ongoing:
    $ sm_vol_str = "red"
    $ sm_tut_text = 14
    scene science_minigame_neutral
    show screen science_tut_screen
    with dissolve
    pause
    label ep10_science_tut2b_label:
    scene ep10_lab39
    hide screen science_tut_screen
    with dissolve
else:
    scene ep10_lab39 with dissolve
no "The magnetic stirrer shouldn't be novel to you. I take it that everyone's comfortable with using one."
no "Adjust the speed setting according to the instructions and never stir too violently."
if minigames and tutorial_ongoing:
    show screen sm_stirrer_tut_screen
    pause
    label ep10_science_tut3_label:
    $ sm_measure_phase = 0
    $ sm_tut_text = 16
    $ sm_stirrer_str = "clear"
    $ sm_play_notepad()
    scene ep10_lab40
    scene science_minigame_neutral
    hide screen sm_stirrer_tut_screen
    show screen science_tut_screen
    with dissolve
    pause
    label ep10_science_tut3b_label:
    scene ep10_lab40
    hide screen science_tut_screen
    with dissolve
else:
    scene ep10_lab40 with dissolve
no "And finally, the burner. Needless to say, exercise caution when you're using the burner. And if there's an emergency, the off switch to the gas is the red-lit switch by the door."
if minigames and tutorial_ongoing:
    $ sm_tut_text = 22
    $ sm_round_str = "red"
    scene ep10_lab40
    scene science_minigame_neutral
    show screen science_tut_screen
    with dissolve
    pause
    label ep10_science_tut4_label:
    scene ep10_lab32
    hide screen science_tut_screen
    with dissolve
else:
    scene ep10_lab32 with dissolve
no "Any questions?"
scene ep10_lab33 with dissolve
no "Ok. You may begin your experiments. You have three hours to complete them. Best of luck to you!"

if minigames:
    $ sm_init_mg(1)
    $ specialMessage = "{size=-%d}You can turn on color blindness support in Settings.{/size}" % (5 * persistent.scale_factor)
    if not persistent.colorblind:
        show screen specialmsglong
    menu:
        "Select your difficulty. Hard mode has a 50%% shorter timer.\nColor blind friendly mode will show colors in text."
        "Hard mode":
            hide screen specialmsglong
            $ sm_hard_mode = True
        "Easy mode":
            hide screen specialmsglong
            $ sm_hard_mode = False
    $ qM = quick_menu
    $ quick_menu = 0
    $ _game_menu_screen = None
    $ renpy.block_rollback()
    hide screen new_phone_screen
    $ science_jump_label = "science_game_end_ep10_label"
    scene science_minigame_neutral with dissolve
    jump sm_setup_experiment_ep10_label

    label science_game_end_ep10_label:
    $ renpy.block_rollback()
    $ _game_menu_screen = "save"
    $ quick_menu = qM
    hide screen wt_science_cheat
    hide screen science_screen
    hide screen sm_timer_screen
    scene ep10_lab41 with dissolve
else:
    scene ep10_lab41 with Fade(2,2,2)
hide screen wt_science_cheat
hide screen sm_timer_screen
de "Let's turn it in. It won't get better than this."
if (minigames and sm_purity == 0) or (not minigames and affinity == "DIK"):
    scene ep10_lab42 with dissolve
    mc "It won't get better than {b}this{/b}? Dude, we just fucked around for three hours. She will notice."
    scene ep10_lab41 with dissolve
    de "We can probably fake it. Look! It's got the right color. Or does it?"
else:
    scene ep10_lab43 with dissolve
    mc "Well, we did our best and there were no accidents. I'm happy with it."
scene ep10_lab44 with dissolve
mc "Dr. Jenkins?"
scene ep10_lab45 with dissolve
no "Please, call me Nora."

scene ep10_lab44 with dissolve
if ep10_nora_lewd or ep6_nora_lewd:
    mc "Ok... Nora."
mc "We think we're finished."
scene ep10_lab45 with dissolve
no "Alright, let's measure the purity of your chemical, shall we?"
if minigames:
    if sm_purity <= 50:
        scene ep10_lab46 with dissolve
        no "This doesn't seem to be the right chemical. Did you follow the instructions?"
        scene ep10_lab48 with dissolve
        mc "Uh... We tried our best."
        scene ep10_lab46 with dissolve
        no "There's no time to start over, but I want you to analyze your steps in the report and find out what you did wrong along the way."
        no "Make sure you include detailed notes and calculations."
        scene ep10_lab48 with dissolve
        mc "Damn... We suck."
        de "Well, what are you gonna do? At least we can leave."
    else:
        if sm_purity < 75:
            scene ep10_lab46 with dissolve
            no "It's not the cleanest sample I've seen. It has a [sm_purity]%% purity."
            no "It will have to do. Make sure you analyze the steps in your report and find out what you could have done to improve your result."
            scene ep10_lab48 with dissolve
            mc "Hey, we did pretty good."
            de "Better than I thought we would."
        else:
            scene ep10_lab47 with dissolve
            no "This is brilliant. Your chemical is [sm_purity]%% pure."
            scene ep10_lab48 with dissolve
            mc "[sm_purity]%%? That's awesome!"
            scene ep10_lab47 with dissolve
            no "However, note that the purity assessment has a degree of error."
            no "It's likely less than [sm_purity]%%. Nevertheless, you should be proud."
            if not persistent.ep10_cardsa20:
                $ persistent.ep10_cardsa20 = True
                $ persistent.rew_sage_unlocked += 1
                $ persistent.chat_new_rewards = True
                $ calcRenders()
                show screen srmsg
                $ renpy.pause(3)
                hide screen srmsg
    scene ep10_lab49 with dissolve
    no "Stay away from the safety shower next time."
else:
    if affinity == "DIK":
        scene ep10_lab46 with dissolve
        no "This doesn't seem to be the right chemical. Did you follow the instructions?"
        scene ep10_lab48 with dissolve
        mc "Uh... We tried our best."
        scene ep10_lab46 with dissolve
        no "There's no time to start over, but I want you to analyze the steps in your report and find out what you did wrong along the way."
        no "Make sure you include detailed notes and calculations."
        scene ep10_lab48 with dissolve
        mc "Damn... We suck."
        de "Well, what are you gonna do? At least we can leave."
        scene ep10_lab49 with dissolve
        no "Stay away from the safety shower next time."
    else:
        scene ep10_lab47 with dissolve
        no "That was a decent effort. If you stay away from the safety shower next time, there may be hope for you."
scene ep10_lab50 with dissolve
de "What if I catch on fire?"
scene ep10_lab49 with dissolve
no "That's a different scenario and that's, of course, permitted."
scene ep10_lab50 with dissolve
de "Noted."
scene ep10_lab51 with dissolve
mc "Permitted, Derek. It's not a challenge. Don't make any more of those flaming shots now."

$ tmpInt = 50
python:
    for x in range(0,len(mphone_bios_chars_list)):
        if mphone_bios_chars_list[x][0] == "Nick":
            tmpInt = x + 1
$ mphone_bios_chars_list.insert(tmpInt,["Nora",[1,8],bios_txt_nora,mbios_history_nora,0])

if ep10_nora_lewd:
    $ new_bio("Nora", "Nora is our teacher...and I have dated and fucked her in the past. She seemed worried about that.")
elif ep6_nora_lewd:
    $ new_bio("Nora", "Nora is our teacher...and I fucked her in the past. She seemed concerned about it.")

$ new_bio("Nora", "Nora doesn't have any humor when it comes to fucking around in her class.")
show screen new_phone_screen

scene ep10_lab52 with dissolve
de "We did it. Our first science class!"
de "Did you like it?"
if ep10_nora_lewd or ep6_nora_lewd:
    scene ep10_lab54 with dissolve
    mc "I'm so happy we got out of there. Dude..."
    mc "I fucked our teacher."
    scene ep10_lab55 with dissolve
    de "..."
    scene ep10_lab56 with dissolve
    de "Get out of here..."
    scene ep10_lab55 with dissolve
    mc "I swear!"
    if ep6_nora_lewd:
        mc "I met her at a bar after chatting with her on Swyper..."
        scene ep10_lab56 with dissolve
        de "At a bar, huh? The story is already bullshit."
        scene ep10_lab55 with dissolve
        if ep10_nora_lewd:
            mc "It's not! I fucked her in the bathroom stalls and, more recently, back at her place after our date."
        else:
            mc "It's not! I fucked her in the bathroom stalls."
        scene ep10_lab56 with dissolve
    elif ep10_nora_lewd:
        mc "I dated her recently and fucked her at her place."
        scene ep10_lab56 with dissolve
        de "Dated and fucked her, huh? Sure..."
    de "I almost bought it, but you took it one step too far."
    scene ep10_lab57 with dissolve
    mc "I'm not making it up, dude. I talked to her outside of class before it started. Didn't you notice that?"
    mc "She told me not to tell anyone, but I fucking had to tell you. What should I do?"
    scene ep10_lab58 with dissolve
    if branchAlone:
        de "You're a single guy. If you're lucky enough to bang that beauty, go nuts!"
        de "Did you see her tits? They are so big! Her lab coat didn't even fit her."
    else:
        de "If it's not something ongoing, then who cares?"
        de "You ran into someone you fucked and it's awkward. That's about it."
        de "It's cool as hell that this someone is a hot teacher, but yeah, don't sweat it."
    scene ep10_lab59 with dissolve
    mc "So, you think I'm overreacting? There's nothing to worry about?"
    scene ep10_lab60 with dissolve
    de "If the roles were reversed and it was me banging her, I'd be strutting right now."
    scene ep10_lab59 with dissolve
    mc "Would you?"
    scene ep10_lab60 with dissolve
    de "Hell yes! I'd be walking into class like I owned the place."
    de "Enjoy it, bro! You hit the mother lode."
    scene ep10_lab59 with dissolve
    mc "Thanks for reassuring me..."
    scene ep10_lab60 with dissolve
    de "You're welcome."
    de "How is she in bed?"
    scene ep10_lab61 with dissolve
    mc "That's crossing a line."
    scene ep10_lab62 with dissolve
    de "You're gonna tell me someday, right? I need it for my spank bank."
    scene ep10_lab61 with dissolve
    mc "I don't wanna be in your spank bank."
    scene ep10_lab63 with dissolve
    de "Speaking of hot teachers... Look who it is."
else:
    scene ep10_lab53 with dissolve
    if minigames and sm_purity == 0:
        mc "Yeah, I did! It was cool but we should do better next time."
    else:
        mc "Yeah, I did! It was cool but kinda simple."
    scene ep10_lab63 with dissolve
    de "[mc_de_up]... Look who it is."

scene ep10_lab64 with dissolve
mc "Cathy?"
de "It's weird seeing her again."
mc "Yeah, I'm gonna go say hi to her. Are you coming?"
de "Nah, I'm meeting up with Ashley soon. Tell her I said hi."

label ep10_cathy_label:
scene ep10_cathy1 with dissolve
mc "Cathy! Hi!"
scene ep10_cathy2 with dissolve
ca "[name]? What a pleasant surprise."
scene ep10_cathy3 with dissolve
ca "Hi! How are you?"
scene ep10_cathy4 with dissolve
mc "I'm ok. How about you? It's been a while."
scene ep10_cathy3 with dissolve
ca "I'm doing great, [name]. Absolutely great."
scene ep10_cathy5 with dissolve
mc "I'm glad. You look happy. Did you get another job?"
scene ep10_cathy6 with dissolve
ca "I did. I reached out to an old acquaintance and was hired pretty much on the spot."
scene ep10_cathy5 with dissolve
mc "That's awesome. What's the job? It's not a teaching one, I'm assuming."
scene ep10_cathy7 with dissolve
ca "Actually, it kind of is, but it's different. I'm working as a corporate trainer now. It's mostly administration, but there's also an aspect of teaching involved."
scene ep10_cathy5 with dissolve
mc "I see."
scene ep10_cathy6 with dissolve
ca "And how is life at B&R, [name]? Are my replacements treating you well?"
scene ep10_cathy5 with dissolve
mc "Both Professor Hoff and Bella are doing great, but you are missed among students."
mc "Derek, for one, misses you. He says hi, by the way."
scene ep10_cathy6 with dissolve
ca "That's nice of you to say. I'm happy that the transition went smoothly."
scene ep10_cathy8 with dissolve
ca "Oh, my bus home is incoming."
scene ep10_cathy5 with dissolve
mc "It was nice catching up. Even if just for a moment."

if pathCathy and not ep7_rejected_cathy:
    scene ep10_cathy9 with dissolve
    ca "..."
    scene ep10_cathy10 with dissolve
    ca "Would you like to join me? It's only a couple of stops from here. We could continue this chat over a cup of coffee if you'd like."
    scene ep10_cathy9 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(possible Cathy scene)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[4]]
                    if branchAlone:
                        $mod_choices[4]="(possible Cathy scene)"
    
    menu:
        "Go with Cathy \n{size=-4}[m_c1][mod_choices[4]]":
            $ ep10_cathy_coffee = True
            stop music fadeout 3
            mc "Yeah, why not? I've got some time for it."
        "Decline":
            $ ep10_cathy_coffee = False
            mc "Thanks, but I must be going too."
            stop music fadeout 3
            scene ep10_cathy6 with dissolve
            ca "Take care, [name]. Say hi to Professor Hoff and Isabella from me."
            $ new_bio("Cathy", "I ran into Cathy, and she told me she was happy with her new job. That felt good to hear, especially considering that she left B&R on such a bad note.")
            jump ep10_sb_label
else:
    stop music fadeout 3
    scene ep10_cathy6 with dissolve
    ca "It was. Take care, [name]. Say hi to Bella from me."
    $ new_bio("Cathy", "I ran into Cathy, and she told me she was happy with her new job. That felt good to hear, especially considering that she left B&R on such a bad note.")
    jump ep10_sb_label

play music "music/ep6/uplifting_ballad.mp3"
scene ep10_cathy11 with wipeleft
ca "After everything that happened, it felt so refreshing to start this new job."
scene ep10_cathy12 with dissolve
ca "I truly feel like I've left the past behind me."
scene ep10_cathy13 with dissolve
mc "It sounds like you needed it more than I realized."
scene ep10_cathy14 with dissolve
ca "And what I realized is that it wasn't just because of the posters. I've felt so energized lately and happy with myself."
ca "It's odd because I thought I'd teach at B&R until I retired. I viewed my teaching job as permanent and secure, not knowing how liberating it would feel to start a new career."
scene ep10_cathy13 with dissolve
mc "It must have felt scary to change your mindset that fast. But you should do what makes you happy."
scene ep10_cathy14 with dissolve
ca "But at the time, I didn't know if it would make me happy. I was trying to escape the miserable situation I found myself in."
ca "I've been rethinking it over and over. If I chickened out by leaving like that or if I was strong for standing up for myself and my integrity."
scene ep10_cathy13 with dissolve
mc "It turned out great for you. That's what matters, I think."
mc "And I kinda know the feeling you had, being exposed like that. I've gotten to experience it lately first-hand."
scene ep10_cathy14 with dissolve
ca "Oh? How so?"
scene ep10_cathy16 with dissolve
mc "Much like yours, some distasteful pictures of me and the DIKs have been printed and spread around on campus."
scene ep10_cathy15 with dissolve
ca "That's horrible, [name]."
ca "Are you getting bullied for it too?"
scene ep10_cathy16 with dissolve
mc "Eh... Yes and no."
mc "I'm wearing a mask in the picture, but some seem to know it's me."
mc "They laugh and point when I walk by. But I'm not too bothered by it."
mc "Of course, I'd rather not have the pictures out there, but they were already hanging on the wall in our mansion."
mc "I should have put my foot down earlier if I didn't want people to see it."
scene ep10_cathy13 with dissolve
mc "And I think some of the attention I get from it is due to jealousy."
scene ep10_cathy14 with dissolve
ca "What do you mean?"
scene ep10_cathy13 with dissolve
mc "Well, I'm naked in it...and let's just say I'm blessed downstairs. Well, you should know."
scene ep10_cathy17 with dissolve
ca "Haha. Yes... I remember. I believe I still have your picture somewhere on my phone."
scene ep10_cathy13 with dissolve
mc "You do? I don't have any of yours on mine. I never bothered to install Swyper on my new phone."
mc "Have you been using Swyper lately?"
scene ep10_cathy17 with dissolve
ca "No, I've taken a break from all dating - even the internet kind. I'm all about my career now."
ca "But I haven't forgotten the last time you and I talked and how you wished that it didn't end like it did..."
ca "That was stupid. Wasn't it?"
$ guideSuggestedPage = 133
scene ep10_cathy18 with dissolve
menu:
    "It was daring":
        mc "It wasn't stupid, but pretty daring."
        scene ep10_cathy17 with dissolve
        ca "Yes. A teacher and student...fornicating. That's trouble with a capital 't'."
    "Not to me":
        mc "No, not to me. I knew I wanted it."
        scene ep10_cathy17 with dissolve
        ca "Wanting it doesn't make it right."
ca "I wasn't thinking clearly back then."
scene ep10_cathy13 with dissolve
mc "Do you regret it?"
scene ep10_cathy17 with dissolve
ca "[name]. You are tempting. Very tempting."
ca "Try to put yourself in my shoes."
ca "You've been a teacher for many years and spent most of those years single."
scene ep10_cathy19 with dissolve
ca "You're responsible for the education of, as in as a position of power over, your students."
ca "And one day, an attractive student, much younger than you, starts to flirt."
ca "Would you not have dirty thoughts about it?"
scene ep10_cathy18 with dissolve
mc "I probably would."
scene ep10_cathy17 with dissolve
ca "And if you acted on those urges, wouldn't you feel like you did something wrong?"
scene ep10_cathy13 with dissolve
mc "I can't relate, but maybe I would."
mc "Put yourself in my shoes, too."
mc "You're young and find mature women hot."
mc "One day, you browse a dating app and discover you're flirting with your sexy teacher."
mc "The fantasies of what could happen start popping into your head, making everything so damned exciting."
mc "Wouldn't you feel that way?"
scene ep10_cathy17 with dissolve
ca "I'm sure I would."
scene ep10_cathy18 with dissolve
mc "Cathy, you've been tempting, too."

scene ep10_cathy17 with dissolve
ca "You're not still tempted...are you?"
scene ep10_cathy18 with dissolve
if branchAlone:
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Cathy scene)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchAlone:
                        $mod_choices[4]="(possible Cathy scene)"
    
    menu:
        "Yes [m_c1][mod_choices[0]]":
            $ ep10_cathy_lewd = True
            mc "Aside from you leaving B&R, nothing changed for me in that area."
            stop music fadeout 3
            scene ep10_cathy20 with dissolve
            mc "Stupid or not, I'd jump on it if you gave me the go-ahead."
            jump ep10_cathy_lewd_label
        "Reject her advances":
            mc "Sadly, no. I think you're great and all, but I've thought a lot about it."
            mc "The moment has passed and the attraction we felt for each other isn't there anymore for me."
else:
    mc "Objectively, yeah. But I can't be."
    mc "The moment has passed and I'm pretty much in a relationship now."

scene ep10_cathy14 with dissolve
ca "Ah... It's for the best, anyway. It would just have been us relenting to carnal desires, wouldn't it?"
scene ep10_cathy13 with dissolve
mc "It does sound like it."
mc "I'm happy we could catch up. I hope we'll meet again sometime."
scene ep10_cathy14 with dissolve
stop music fadeout 3
ca "Maybe we will, [name]. You know where I live."
$ new_bio("Cathy", "I ran into Cathy, and she told me she was happy with her new job. I ended up having coffee with her at her place. We talked about the past, but that's all that happened.")
jump ep10_sb_label

label ep10_cathy_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_cathy == None:
        $ mc_cathy = name
    else:
        $ mc_cathy = persistent.mc_cathy
    if persistent.cathy == None:
        $ cathy = "Cathy"
    else:
        $ cathy = persistent.cathy

hide screen new_phone_screen
play music "music/ep3/some_obsession.mp3"
scene ep10_cathy_lewd1 with dissolve
$ renpy.pause()
scene ep10_cathy_lewd2 with dissolve
$ renpy.pause()
scene ep10_cathy_lewd3 with dissolve
ca "Go ahead!"
scene ep10_cathy_lewd4 with dissolve
mc "Don't mind if I do."
scene ep10_cathy_lewd6 with dissolve
ca "*{i}Smack{/i}* I want you, [mc_cathy]."
scene ep10_cathy_lewd5 with dissolve
ca "And not as a fantasy this time. I want the real thing."
ca "I want to feel your fat, throbbing cock inside of my pussy."
scene ep10_cathy_lewd6 with dissolve
mc "Oh, [cathy]."
ca "Oh, [mc_cathy]..."

play sound "sound_effects/shove.mp3"
scene ep10_cathy_lewd7 with vpunch
$ renpy.pause()
scene ep10_cathy_lewd8 with dissolve
$ renpy.pause()
play sound "sound_effects/shove.mp3"
scene ep10_cathy_lewd9 with vpunch
$ renpy.pause()
scene ep10_cathy_lewd10 with dissolve
$ renpy.pause()
scene ep10_cathy_lewd11 with dissolve
ca "Yes! Eat me!"
scene ep10_cathy_lewd12 with dissolve
$ renpy.pause()
scene ep10_cathy_lewd13 with dissolve
ca "*{i}Moans{/i}* Oh fuck!!!"
scene anim_cathy_cunn1_ep10 with dissolve
mc "*{i}Lick lick{/i}* I've wanted to taste you for so long."
ca "Yes! Taste me! Do whatever you want with me! I'm yours to taste."
pause
scene anim_cathy_cunn2_ep10 with dissolve
pause

label ep10_cathy_lewd_loop_label:
menu:
    "Handjob":
        scene anim_cathy_mast_ep10 with dissolve
        mc "*{i}Smack{/i}*"
        ca "Oh my God... It's so sexy feeling your cock get hard in my hand."
        mc "You make me hard, [cathy]."
        ca "You're so good with your fingers."
        ca "[mc_cathy], you're making me so wet! *{i}Moans{/i}*"
        mc "I can feel that. It's so sexy feeling your juices on my fingers."
        ca "Your cock is so warm and hard."
        pause
        jump ep10_cathy_lewd_loop_label
    "Blowjob":
        scene ep10_cathy_lewd14 with dissolve
        ca "You look even bigger up close than in your pictures."
        scene ep10_cathy_lewd15 with dissolve
        mc "Does that scare you?"
        scene ep10_cathy_lewd16 with dissolve
        ca "Scare me? It makes me horny as hell."
        scene anim_cathy_bj_ep10 with dissolve
        ca "*{i}Suck suck{/i}* Mmm... I wanna *{i}Glug glug{/i}* taste every inch of you."
        mc "Suck my cock, [cathy]."
        pause
        jump ep10_cathy_lewd_loop_label
    "Continue":
        jump ep10_cathy_lewd_cont_label

label ep10_cathy_lewd_cont_label:
scene ep10_cathy_lewd17 with dissolve
ca "Are you going to give it to me?"
scene ep10_cathy_lewd18 with dissolve
mc "Yeah, I'm gonna fuck you good. Until you scream from your orgasm."
scene ep10_cathy_lewd17 with dissolve
ca "Fuck me, [mc_cathy]. I'm yours. How do you want me?"
$ tmpInt = 0
scene ep10_cathy_lewd18 with dissolve
label ep10_cathy_lewd_loop2_label:
menu:
    "Missionary":
        $ tmpInt += 1
        scene ep10_cathy_lewd19 with dissolve
        ca "Yes... Put it in."
        scene anim_cathy_miss_ep10 with dissolve
        ca "*{i}Moans{/i}* Yes! Give it to me."
        pause
        scene anim_cathy_miss2_ep10 with dissolve
        ca "God, it feels amazing!"
        pause
        scene anim_cathy_miss3_ep10 with dissolve
        ca "I never knew you would be this good at it. *{i}Moans{/i}*"
        ca "If I knew, I would have made you fuck me the moment we met."
        pause
        scene anim_cathy_miss4_ep10 with dissolve
        ca "Fuck me, [mc_cathy]!"
        pause
        jump ep10_cathy_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene ep10_cathy_lewd20 with dissolve
        mc "Arch your back, I'm gonna give it to you hard."
        scene ep10_cathy_lewd21 with dissolve
        $ renpy.pause()
        scene bg anim_cathy_doggy_ep10 movie with dissolve
        ca "Yes, [mc_cathy]. Make me feel like I'm your slut."
        pause
        scene bg anim_cathy_doggy2_ep10 movie with dissolve
        ca "Spank me! Harder!"
        pause
        scene bg anim_cathy_doggy3_ep10 movie with dissolve
        pause
        jump ep10_cathy_lewd_loop2_label
    "Sitting":
        $ tmpInt += 1
        scene anim_cathy_chair_ep10 with dissolve
        ca "Right there... Yes... You're hitting my G spot... Fuck!!!"
        pause
        scene anim_cathy_chair2_ep10 with dissolve
        pause
        jump ep10_cathy_lewd_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_cathy_ride_ep10 with dissolve
        mc "*{i}Suck suck{/i}* Do you like it when I suck on your nipples?"
        ca "Yes! I love it! More!"
        pause
        scene anim_cathy_ride2_ep10 with dissolve
        ca "*{i}Moans{/i}* Fuck me, [mc_cathy]!"
        pause
        scene anim_cathy_ride3_ep10 with dissolve
        ca "I want to ride your cock until you cum inside me, [mc_cathy]..."
        pause
        jump ep10_cathy_lewd_loop2_label
    "Against the wall":
        $ tmpInt += 1
        scene anim_cathy_wall_ep10 with dissolve
        ca "You're so strong! Fuck me, [mc_cathy]! Fuck me hard!"
        pause
        scene anim_cathy_wall2_ep10 with dissolve
        ca "Oh God! Yes! Yes!"
        pause
        scene anim_cathy_wall3_ep10 with dissolve
        ca "More! Harder! Deeper!"
        pause
        scene anim_cathy_wall4_ep10 with dissolve
        mc "Yeah? Is this what you want?"
        scene anim_cathy_wall5_ep10 with dissolve
        ca "Fuck! Yes! HARDER!!!"
        jump ep10_cathy_lewd_loop2_label
    "Prone":
        $ tmpInt += 1
        scene anim_cathy_prone_ep10 with dissolve
        ca "Yes! Pin me down and fuck me! Hard!"
        pause
        scene anim_cathy_prone2_ep10 with dissolve
        mc "Your ass is so fucking sexy. I could cum from looking at it."
        pause
        jump ep10_cathy_lewd_loop2_label
    "Cum" if tmpInt > 2:
        menu:
            "Body and facial":
                scene anim_cathy_cum2_ep10 with dissolve
                pause
                mc "[cathy], I wanna cum all over you."
                ca "Do it, [mc_cathy]. Cover me in cum. Make me feel your warm seed all over my body."
                scene anim_cathy_cum_ep10 with vpunch
                mc "Ahhh!!!"
                pause
                scene ep10_cathy_lewd22 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_cathy_ride_ep10 with dissolve
                ca "I want to feel your cum deep inside of me."
                scene ep10_cathy_lewd23 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_cathy_lewd23 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_cathy_lewd23 at vpunch, cum1
                mc "Ahh... Fuck!!!"
                scene ep10_cathy_lewd24 with dissolve
                $ renpy.pause()
            "On Ass":
                scene anim_cathy_prone2_ep10 with dissolve
                mc "[cathy], I wanna cum all over your ass."
                ca "Do it, [mc_cathy]. Cover my ass in cum. Make me feel your warm seed all over it."
                scene ep10_cathy_lewd25 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_cathy_lewd25 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_cathy_lewd25 at vpunch, cum2
                mc "Ahh... Fuck!!!"
                scene ep10_cathy_lewd26 with dissolve
                $ renpy.pause()
stop music fadeout 3
scene ep10_cathy_lewd27 with dissolve
$ renpy.pause()
scene ep10_cathy_lewd28 with dissolve
play music "music/ep8/licensed_music/track68.mp3"
ca "That...was...amazing..."
ca "[name]... The way you made me cum... It's insane."
scene ep10_cathy_lewd29 with dissolve
mc "You've waited for it for a long time, huh?"
scene ep10_cathy_lewd28 with dissolve
ca "Yes... And what a release it was."
scene ep10_cathy_lewd30 with dissolve
ca "I won't be able to go back to using toys after this."
scene ep10_cathy_lewd31 with dissolve
mc "Haha! I can be your toy if you want."

$ renpy.end_replay()
$ persistent.ep10_lewd_cathy = True
$ calcScenes()
$ new_bio("Cathy", "I ran into Cathy, and she told me she was happy with her new job. I ended up having coffee with her at her place. We talked about the past and ended up having sex.")
$ mphone_stats_add_girl_s3("cathy","You had sex with Cathy at her place in episode 10.")

scene ep10_cathy_lewd32 with dissolve
ca "I'll be right back."
mc "Take your time."
scene ep10_cathy_lewd33 with dissolve
mc "(Wow... That was intense.)"
mc "(She really craved it. It made me feel good about myself. Haha!)"
mc "(There's no way I'm as good as she made me out to be, right?)"
scene ep10_cathy_lewd34 with dissolve
mc "(Be Grateful. Haha! This reminds me of that dorm party.)"
mc "(Derek's gonna love this sign.)"
scene ep10_cathy_lewd35 with dissolve
$ renpy.pause()
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"Check this sign out.",False])
$ text_message_screen_list.append(["%s" % name,"chat_derek_pic1_ep10_thumb",False])
$ text_message_screen_list.append(["Derek","LMAO! BE GRATEFUL! OR ELSE!",True])
$ text_message_screen_list.append(["%s" % name,"Right!? LOL! mphone_emoji_laugh",False])
hide screen new_phone_screen
show screen text_message_screen
$ tmpInt += 1
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ mphone_scene_to_chat("Derek",text_message_screen_list)
$ mgallery_add_photo("chat_derek_pic1_ep10_zoomed")
show screen new_phone_screen
scene ep10_cathy_end1 with wipeleft
mc "It was nice catching up with you."
scene ep10_cathy_end2 with dissolve
ca "Yes. We should catch up more often."
scene ep10_cathy_end3 with dissolve
mc "Haha! Totally."
scene ep10_cathy_end4 with dissolve
ca "*{i}Smack{/i}*"
scene ep10_cathy_end2 with dissolve
ca "Bye, [name]."

scene ep10_cathy_end5 with dissolve
if ep10_nora_lewd or ep6_nora_lewd:
    mc "(Derek's gonna have a hard time believing me again...)"
else:
    mc "(Derek's not gonna believe this.)"
stop music fadeout 3
mc "(College rocks.)"

if not persistent.ep10_card13:
    $ persistent.ep10_card13 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep10_card14:
    $ persistent.ep10_card14 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

jump ep10_sb_label

label ep10_sb_label:
if branchSage:
    jump ep10_sage_date_label
label ep10_sb2_label:
hide screen new_phone_screen
$ guideSuggestedPage = 134
if branchSage:
    scene ep10_sb1 with Fade(2,2,2)
    play music "music/ep2/relaxing_ballad.mp3"
else:
    play music "music/ep2/relaxing_ballad.mp3"
    scene ep10_sb1 with dissolve
bn1 "New guy! Chief wants a word with you."
scene ep10_sb2 with dissolve
ng "Are you ever going to drop the \"new guy\" crap? I've been here for eight years, just because I've worked on a different floor than you doesn't make me new."
scene ep10_sb3 with dissolve
bn1 "You're new to me."
scene ep10_sb4 with dissolve
ng "*{i}Mumbles{/i}* I beat your billables, moron."
show ep10_sb5
if not persistent.ep10_cardzo17:
    show screen ep10_render_screen("zo17")
with dissolve
wl "I don't care how. Get it done."
show ep10_sb6
hide screen ep10_render_screen
with dissolve
wl "Peterson is killing me. He's killing me."
scene ep10_sb7 with dissolve
ng "You wanted to see me, Mr. Wallace."
scene ep10_sb6 with dissolve
wl "Yes, sit down."
scene ep10_sb8 with dissolve
wl "I'm disappointed in you, Stephen."
scene ep10_sb9 with dissolve
sb "Why? What did I do?"
scene ep10_sb10 with dissolve
wl "It's not about what you did; it's about what you didn't do."
wl "The Levenson contract. You never gave him the go-ahead on the trade."
scene ep10_sb12 with dissolve
sb "It was insider information. The SEC would have been all over it. You saw how their stock value skyrocketed after their quarterly report."
scene ep10_sb10 with dissolve
wl "It's not insider information; they are \"leads\". Get it? You can always claim you heard about it from somewhere else."
wl "And everything works out if you base the trade on your own analysis. I've told you this!"
scene ep10_sb12 with dissolve
sb "I know, but my analysis didn't support that trade. There was no way to motivate it."
scene ep10_sb11 with dissolve
wl "You know... I like you. You're a smart man. Very smart. Sometimes, you're too smart for your own good."
wl "You've been the only disobedient employee I've kept for this long."
scene ep10_sb13 with dissolve
sb "With good reason. I've made your company a fortune."
scene ep10_sb11 with dissolve
wl "You've made yourself rich too. What's that word you always use for it?"
scene ep10_sb13 with dissolve
sb "Symbiosis. We help each other grow."
scene ep10_sb11 with dissolve
wl "Yes. It used to be like that, but you've grown too fast for us."
wl "You've become expensive. And there is younger talent out there who are both cheaper and...hungrier."
wl "I'm going to have to let you go."
scene ep10_sb12 with dissolve
sb "Because of the Levenson trade?"
scene ep10_sb10 with dissolve
wl "Because you keep refusing to get your hands dirty. You need to take some personal risks on these safe bets."
scene ep10_sb12 with dissolve
sb "Knowing everyone here has something to hide and shutting up about it isn't dirty enough for you?"
scene ep10_sb11 with dissolve
wl "It's nothing personal. But we're in the money-making business and enough is enough."
wl "It's time for us to part ways. You came out of this successfully. Let's keep it that way."

scene ep10_sb14 with dissolve
sb "Hey, it's me."
sb "I know you're at work, but listen-"
scene ep10_sb15 with dissolve
sb "Hello?"
sb "Fuck..."
scene ep10_sb16 with dissolve
sb "Hey, doc. Do you have time for a walk-in session?"
sb "I'm just around the corner."
sb "Got it. Um... Thank you."

scene ep10_sb17 with dissolve
sb "I can't talk to her anymore. She's not the person she used to be."
scene ep10_sb18 with dissolve
doc2 "When did you first notice this change?"
scene ep10_sb19 with dissolve
sb "I guess...the first time was...um..."
sb "Yeah. Around the time I started my job."
scene ep10_sb18 with dissolve
doc2 "The one you just discontinued?"
scene ep10_sb19 with dissolve
sb "Yes. Around eight years ago."
sb "I worked a lot. I stayed at the office late, even after the market had closed."
scene ep10_sb20 with dissolve
sb "I made my analyses and procured contacts... I did everything I could to stay in front of the pack."
sb "As a result, we stopped talking because there was little time of the day left for it."
scene ep10_sb21 with dissolve
sb "And this was also around the time when we found out that my wife..."
sb "That she was barren."
scene ep10_sb23 with dissolve
doc2 "That must have been hard for you two, Stephen."
scene ep10_sb20 with dissolve
sb "It didn't make things easier for us."
sb "She decided to go for a Ph.D. instead of having kids..."
scene ep10_sb22 with dissolve
sb "Something that felt smart to do, but she was just using it as a distraction from that horrible news."
sb "Halfway into her doctoral studies, we decided to adopt. She couldn't let go of her desire to be a mother."
scene ep10_sb21 with dissolve
sb "It was...not the best choice. But how could I deny her that wish? First being barren and then having a husband tell her she can't adopt."
scene ep10_sb24 with dissolve
doc2 "When you say it wasn't the best choice, can you elaborate on that?"
scene ep10_sb22 with dissolve
sb "I was too preoccupied with work and she was in the middle of writing her thesis. Neither of us had the time for it. It didn't make sense to have kids."
sb "Sure, because of me, we had the money... But those kids..."
scene ep10_sb21 with dissolve
sb "*{i}Sigh{/i}*"
sb "They were already damaged. They were old enough to have bad memories, for Christ's sake."
sb "I failed to see how we could make that work. I don't have the tools for that."
scene ep10_sb26 with dissolve
sb "You don't grow to be a father to kids like that overnight."
sb "And why did we have to get both of them?"
scene ep10_sb24 with dissolve
doc2 "What did you tell your wife? Did you voice your concerns and thoughts?"
scene ep10_sb26 with dissolve
sb "I tried, but she wouldn't hear me out. Early on in our relationship, we talked about having kids in the future."
sb "She remembered me saying I wanted a son if I ever had kids. It was just a hypothetical answer for me."
sb "And she... She told me she wanted to have a daughter."
sb "Adopting both was her way to fulfill that as if it was a dream we shared."
scene ep10_sb21 with dissolve
sb "It was such a mistake. I've never felt like a father to those kids. I try my best and they call me \"Dad\", but..."
sb "I don't feel like I'm their father. I don't feel connected to them... I try my best, but..."
scene ep10_sb27 with dissolve
sb "I'm raising someone else's kids. That's all I'm thinking."
sb "They deserve better than me, but this is as good as they can get."
scene ep10_sb21 with dissolve
sb "And now I got fired... My wife won't talk to me... She rarely sleeps with me..."
sb "I don't feel like a man when I'm with her anymore. I feel like I'm living someone else's life."
scene ep10_sb24 with dissolve
doc2 "May I suggest couples therapy? It's a great way to communicate with your wife."
doc2 "You obviously have things to tell her. And every relationship needs maintenance and communication is the tool for it."
scene ep10_sb22 with dissolve
sb "That's not going to happen. I've tried talking to her. And it either ends with her getting mad at me or her shutting down the conversation before it takes off."
sb "And she also has the guts to tell me that I'm not listening! It's nuts..."
sb "The only way that works for us is to ignore all the bad feelings and live life like nothing's wrong."
scene ep10_sb24 with dissolve
doc2 "That's not a sustainable lifestyle, Stephen."
scene ep10_sb21 with dissolve
sb "*{i}Sigh{/i}*"
sb "Saying what I say to you within these four walls... If she knew about it, it would break her."
sb "If my kids ever knew what I felt, it would fuck them up even further - likely beyond repair."
scene ep10_sb25 with dissolve
doc2 "And not saying what you feel to your wife... Do you think it doesn't wear you down?"
scene ep10_sb21 with dissolve
sb "I never talked to my parents like this. I've been raised to be strong and not to talk about my feelings."
scene ep10_sb25 with dissolve
doc2 "It's not a weakness to talk about your feelings. After all, you've been strong enough to admit you need my help."
scene ep10_sb21 with dissolve
sb "I needed someone to listen to me. Just for once..."
scene ep10_sb24 with dissolve
doc2 "How about if we change the subject for now?"
scene ep10_sb22 with dissolve
sb "Yes, please."
scene ep10_sb25 with dissolve
doc2 "Let's return to your work situation. What are your thoughts?"
scene ep10_sb28 with dissolve
sb "My thoughts? Um...let's see..."
sb "How about my boss firing me for not breaking laws for him? That's a fun thought."
scene ep10_sb29 with dissolve
$ ui.timer(2.0, Play("sfx1", "sound_effects/season3/finger_snap.mp3",loop=False))
sb "Or how about me putting in eight years for that company and it's gone *{i}Snaps fingers{/i}* like that?"
scene ep10_sb25 with dissolve
doc2 "That doesn't sound legal."
scene ep10_sb28 with dissolve
sb "Well, neither is doing blow together at meetings. I'm not looking to go down the road for mutual destruction, thanks."
sb "Guess from now on, I'll have to become a stay-at-home dad."
scene ep10_sb24 with dissolve
doc2 "You can take some time to reflect. Maybe there is something else in life that you've always wanted to pursue. A change of vocation, perhaps?"
scene ep10_sb28 with dissolve
sb "I'm sure as shit not going back to investment banking, I can tell you that much."
sb "Maybe I'll sit on my ass all day doing nothing for a change."
scene ep10_sb25 with dissolve
doc2 "Do you think you'd feel fulfilled that way?"
scene ep10_sb30 with dissolve
sb "Fulfilled? Who the hell feels fulfilled?"
sb "I've got enough money to last lifetimes. It doesn't make me feel fulfilled."
scene ep10_sb31 with dissolve
sb "Do you want to know what it does to me?"
sb "It makes me realize that there is a void that normal people can fill with the stress of work and the struggle of providing for their families and trying to get rich."
sb "And when you get rich, that stress and struggle disappear... Revealing the true emptiness of life. It's like all there is to life is the chase to make it."
scene ep10_sb30 with dissolve
sb "I don't have anything left to accomplish - nothing left to prove."
sb "And thinking about this... These thoughts scare the fuck out of me. And a normal person could never relate to them."
sb "They'd call it rich privilege and belittle it because they have this fairytale fantasy of how good it is to be wealthy."
scene ep10_sb24 with dissolve
doc2 "You can always set new goals for yourself, Stephen. Personal goals don't have to revolve around money."
scene ep10_sb32 with dissolve
doc2 "Perhaps you'll think of something. That's all I have time for today, but I want you to come here again soon so we can explore this further."
stop music fadeout 3
show screen new_phone_screen
scene ep10_sb33 with Dissolve(2)
$ renpy.pause()
scene ep10_sb34 with dissolve
ja "What the hell is this?"
play music "music/ep3/black_box.mp3"
scene ep10_sb38 with dissolve
sb "Divorce papers. It's been long overdue."
scene ep10_sb34 with dissolve
ja "We are NOT getting a divorce."
scene ep10_sb38 with dissolve
sb "I thought you'd be happier about this."
sb "You've been threatening me with one for long enough. I'm granting you that wish."
sb "The truth is we should have broken up many years ago. We've been living a lie and now it's time."
scene ep10_sb35 with dissolve
ja "Oh, really!? It's time all of a sudden!?"
ja "You've been cheating on me for God knows how long and now it's finally time!?"
scene ep10_sb36 with dissolve
ja "What about your children? What about our family?"
ja "Do you realize how this will affect them and our reputation?"
scene ep10_sb39 with dissolve
sb "This isn't a spur-of-the-moment decision, Jade."
sb "I've thought about this for a long time - years, actually. But you don't want to hear what I think or feel. You never listen."
sb "I can't walk through the rest of my life living like this. I need changes. I need peace of mind."
sb "When I look into the mirror, I don't see the man I used to be."
scene ep10_sb36 with dissolve
ja "This screams life crisis, Stephen. It's pathetic. You've grown old, put on a few pounds and lost some hair - it happens to everyone."
ja "You don't make these rash decisions without thinking them through."
scene ep10_sb39 with dissolve
sb "I have thought it through."
sb "I don't like the man in the mirror staring back at me. I've been wracking my head about how it all came to this, and I believe all of it is deeply rooted in us."
scene ep10_sb36 with dissolve
ja "You don't have a prenup! I will take half of your shit if you go through with this! Do you realize that!?"
if ep4_toldDerekAboutJade:
    scene ep10_sb40 with dissolve
    sb "A good samaritan sent me a video of your sexual adventure with a student in our bed."
    scene ep10_sb37 with dissolve
    sb "I believe it requires no further explanation."
    scene ep10_sb39 with dissolve
    sb "I have agreed to a generous 90/10 split in the divorce settlement agreement."
    sb "You're, of course, entitled to an equal 50/50 split if you wish. But me deleting that video won't be a part of that deal."
    scene ep10_sb37 with dissolve
    ja "You bastard..."
    scene ep10_sb40 with dissolve
    sb "Fucking a student..."
    sb "How will that affect your career and your children?"
    scene ep10_sb36 with dissolve
    ja "You did it, too!"
    scene ep10_sb40 with dissolve
    sb "Good luck proving that."
else:
    scene ep10_sb39 with dissolve
    sb "I realize that. It's all there in the divorce settlement agreement."
    sb "In the bigger scheme of things, 50%% is a small price to pay."
    scene ep10_sb36 with dissolve
    ja "That's millions, Stephen! MILLIONS!"
    ja "In fact, you cheated on me and want a divorce!? You'd be lucky to get anything! I'll sue you for everything!"
    scene ep10_sb40 with dissolve
    sb "If you believe that will work, you need to brush up on marital laws."
scene ep10_sb41 with dissolve
stop music fadeout 3
sb "Sign the papers."
ja "STEPHEN!!!"

label ep10_jt_label:
play music "music/ep2/freedom.mp3"
scene ep10_jt1 with dissolve
$ renpy.pause()
scene ep10_jt2 with dissolve
$ renpy.pause()
scene ep10_jt3 with dissolve
$ renpy.pause()
scene ep10_jt4 with dissolve
$ renpy.pause()
scene ep10_jt10 with dissolve
$ renpy.pause()
scene ep10_jt11 with dissolve
$ renpy.pause()
scene ep10_jt12 with dissolve
$ renpy.pause()
scene ep10_jt13 with dissolve
ji "Trent... Do you have a moment?"
scene ep10_jt17 with dissolve
tr "Of course."
scene ep10_jt14 with dissolve
ji "Do you recall a couple of months ago, there was a party here for alums, among others?"
scene ep10_jt18 with dissolve
tr "The party that got ruined by the sprinklers going off?"
scene ep10_jt14 with dissolve
ji "That's the one."
ji "Perhaps it's a bit late, but I wanted to thank you for not pressing charges."
scene ep10_jt18 with dissolve
tr "Pressing charges against who?"
scene ep10_jt14 with dissolve
if branchJill:
    ji "Against my boyfriend."
else:
    ji "Against a friend of mine."
ji "Tybalt said he was responsible for starting the fire that night."
scene ep10_jt19 with dissolve
tr "A fire? No, no. A couple of DIK fraternity members set the sprinkler system off. But there was no fire."
tr "They ruined our evening with it, but I wouldn't waste my time and money on a pointless lawsuit when there's insurance to rely on."
scene ep10_jt15 with dissolve
ji "Interesting... Because Tybalt said you would press charges for the fire - that evidently didn't happen."
ji "He told me you insisted on doing that. And he called you petty for it."
scene ep10_jt19 with dissolve
tr "Wait a minute. What?"
scene ep10_jt16 with dissolve
ji "He said you would listen to his reasoning and he could convince you not to go through with it."
ji "I'm sorry. His words, not mine."
scene ep10_jt20 with dissolve
tr "What are you talking about? It was me who convinced him that we should drop it!"
tr "He's the one who was furious, acting all childishly, and wouldn't let it go. I had to convince him not to do it - not the other way around."
tr "He wouldn't stop crying over the ruined party and his damned custom-made Italian suit. And he called {b}me{/b} petty?"
tr "I am not petty! I take pride in being reasonably level-headed."
scene ep10_jt16 with dissolve
ji "Again, I'm sorry. Those were his words. It took me a while to see that he was lying about it, and I had a hunch he might have lied about you, too."
scene ep10_jt20 with dissolve
tr "Follow me. We're going to settle this with him at this instant."
scene ep10_jt5 with dissolve
ji "He's been obnoxious lately and disturbing me a lot."
scene ep10_jt6 with dissolve
tr "He certainly seems to be going through something. We've all noticed his subpar behavior."
scene ep10_jt5 with dissolve
ji "I don't mean to cause a big fight or anything, but is there something you can do about it? He's making my stay here insufferable."
scene ep10_jt6 with dissolve
tr "He crossed a line with me by involving me in his lies. I don't care if he's the President; we all have to abide by rules of conduct."
tr "If what you say is true, this won't get by without punishment."
play sound "sound_effects/door_slam.mp3"
scene ep10_jt7 with hpunch
tr "Tybalt, what is this I'm hearing that-"
stop music
scene ep10_jt9
ty "Ahhh!!! Get out!"
scene ep10_jt8 with dissolve
$ renpy.pause()
jump ep10_freeroam_bbq_intro_label

label ep10_after_bbq_label:
play music "music/ep10/licensed_music/track148.mp3"
scene ep10_after_bbq12 with dissolve
rs "Derek. Stop humping the trashcan!"
scene ep10_after_bbq13 with dissolve
de "Her name is Jessie and I'm not humping her - we're making love!"
scene ep10_after_bbq15 with dissolve
jac "Tommy ruined the vibe of the party with these shrooms."
scene ep10_after_bbq16 with dissolve
rs "I don't hear you complaining when you smoke weed with him."
scene ep10_after_bbq15 with dissolve
jac "This is how you feel every time we do that, huh?"
scene ep10_after_bbq16 with dissolve
rs "What you do with your body is your business. But experimenting with hallucinogens like this...it's way too extreme for me."
rs "Even when it comes to watching you do it, I'm not comfortable."
rs "I'm genuinely worried someone will do something stupid and get hurt tonight."
scene ep10_after_bbq13 with dissolve
de "Rusty. Why the camera!? Why?"
scene ep10_after_bbq14 with dissolve
jac "No one's got a camera on you. You're tripping."
scene ep10_after_bbq13 with dissolve
de "There is a camera on my ceiling watching everything I do."
de "It watches me masturbate!"
scene ep10_after_bbq18 with dissolve
rs "You're in the woods, dude. You shouldn't have eaten that mushroom."
scene ep10_after_bbq13 with dissolve
de "Not in the woods, Rusty. In my room."
scene ep10_after_bbq15 with dissolve
jac "It's like talking to toddlers."
scene ep10_after_bbq17 with dissolve
rs "Haha, yep."
stop music fadeout 3
if ep4_derekFuckedArieth:
    scene ep10_after_bbq19 with dissolve
else:
    scene ep10_after_bbq19b with dissolve
de "Look!"
jac "What the fuck is that!?"
play music "music/ep5/suspense5.mp3"
rs "Uh..."
scene ep10_after_bbq20 with dissolve
de "The camera!"
scene ep10_after_bbq21 with dissolve
rs "Ok, I think we need to listen to him."
scene ep10_after_bbq22 with dissolve
jac "Derek! Where did you get that picture from?"
scene ep10_after_bbq20 with dissolve
de "Ashley. My beautiful Ashley."
scene ep10_after_bbq22 with dissolve
jac "Ashley sent you this?"
scene ep10_after_bbq21 with dissolve
rs "That's from Derek's closet, right?"
scene ep10_after_bbq20 with dissolve
de "Ashley and I fooled around in there. I had to tell her about it."
de "She said that Anthony told her about some pictures they got... He blamed us."

scene ep10_after_bbq21 with dissolve
rs "The jocks did this?"
scene ep10_after_bbq20 with dissolve
de "Take it. Read Ashley's text. My reputation is already ruined..."
scene ep10_after_bbq23 with dissolve
jac "Ok, I'm browsing it."
jac "And there's your penis... Why are you sending her dick pics?"
scene ep10_after_bbq24 with dissolve
de "After that."
scene ep10_after_bbq23 with dissolve
jac "Dude."
scene ep10_after_bbq27 with dissolve
rs "What does it say?"
scene ep10_after_bbq29 with dissolve
if ep7_hot_ashley_phase == 4:
    jac "Ashley: I feel sick thinking about the camera. Do you think there's a sex tape of us out there?"
else:
    jac "Ashley: I feel sick thinking about the camera. Do you think there are sex tapes of us out there?"
jac "Derek: I don't know. It makes me feel sick, too. Did you get a hold of the pictures?"
scene ep10_after_bbq31 with dissolve
jac "Ashley: Not yet. I'm going to ask Ant about it later tonight."
jac "Ashley: He showed me the pictures. You're totally right. There is a camera in there."
scene ep10_after_bbq29 with dissolve
jac "And there's the picture..."
jac "Derek: What the fuck! That's from my room! It's from that camera!"
if ep4_derekFuckedArieth:
    scene ep10_after_bbq26 with dissolve
    jac "Ashley: I can't believe you had sex with Arieth... Who haven't you slept with?"
    jac "Derek: That was before I was with you."
    jac "Ashley: Yeah, whatever. This is why I have a hard time trusting you. I don't know if I mean anything to you or not."
    jac "Derek: You mean the world to me, Ash."

scene ep10_after_bbq31 with dissolve
jac "Ashley: Ant said you guys provoked them with a bunch of pictures of everyone having sex with Arieth. And that this was one of them."
jac "Ashley: I saw the pictures and he wasn't lying. Rusty. Leon. Jamie. I don't remember everyone because I didn't wanna look at them. They were disgusting."
scene ep10_after_bbq27 with dissolve
rs "What the hell is she talking about?"
scene ep10_after_bbq30 with dissolve
jac "The pictures from our laptop of you guys banging her... It's gotta be those!"
scene ep10_after_bbq27 with dissolve
rs "The jocks did this?"
scene ep10_after_bbq24 with dissolve
de "It's not the jocks! Read!"
scene ep10_after_bbq29 with dissolve
jac "Derek: Where did he get those pictures from? Is it their camera?"
jac "Ashley: Someone dropped a letter off with them addressed to Dawe. Chad told them it was [name], so he got into a fight with him."
jac "Ashley: That fight is what got Chad suspended from the frat."
scene ep10_after_bbq27 with dissolve
rs "[name] did this? It can't be."
scene ep10_after_bbq29 with dissolve
jac "Derek: That's the dumbest thing I heard. There's no way it can be [name]."
jac "Ashley: That's what Chad said."
jac "Derek: I talked to [name] about the camera. He even helped me look for more of them in the mansion. It can't be him."

scene ep10_after_bbq31 with dissolve
if ep7_hot_ashley_phase == 4:
    jac "Ashley: And I trust Ant and he says it was [name] who did it. There's no way that camera is theirs, either. God, I don't want that sex tape to leak..."
else:
    jac "Ashley: And I trust Ant and he says it was [name] who did it. There's no way that camera is theirs, either. God, I don't want those sex tapes to leak..."

scene ep10_after_bbq28 with dissolve
rs "..."
scene ep10_after_bbq27 with dissolve
rs "It can't be [name]. I'm not buying it."
scene ep10_after_bbq24 with dissolve
de "It's not [name]."
de "But it all makes sense now. Cathy's cluck. The camera. The pictures. The posters..."
scene ep10_after_bbq25 with dissolve
de "It's one of us."
scene ep10_after_bbq30 with dissolve
stop music fadeout 3
jac "It's a DIK... It's a fucking DIK."
scene ep10_after_bbq28 with dissolve
rs "..."
play music "music/ep8/licensed_music/track72.mp3"
if wt_ep9_branch_numbers != 1:
    if branchSage:
        jump ep10_bbq_sage_lewd_label
    else:
            "End the night with?"
            if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Bella scene)","(+Josy)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
            menu:
                "Jill" if branchJill:
                    $ep10_wt_end_bbq="Jill"
                    jump ep10_bbq_jill_end_event_label
                "Josy & Maya" if branchMayaJosy:
                    $ep10_wt_end_bbq="Josy"
                    jump ep10_bbq_jm_end_event_label
                "Isabella" if branchIsabella:
                    $ep10_wt_end_bbq="Bella"
                    jump ep10_party_eval_label
                "Lily" if ep10_rolling:
                    $ep10_wt_end_bbq="Lily"
                    scene ep10_after_bbq1 with dissolve
                    ly "No way... Is this where you're sleeping?"
                    scene ep10_after_bbq3 with dissolve
                    mc "Since I put up the tent and all, I figured why not?"
                    mc "Wanna join?"
                    scene ep10_after_bbq2 with dissolve
                    ly "I don't think so. I can hear my bed calling my name from here."
                    scene ep10_after_bbq3 with dissolve
                    mc "I can't blame you. This night will get cold."
                    mc "But now that most seem to be leaving, I'm gonna turn in."
                    scene ep10_after_bbq4 with dissolve
                    ly "What the hell... Make some room for me."
                    scene ep10_after_bbq5 with dissolve
                    mc "For real?"
                    scene ep10_after_bbq6 with dissolve
                    ly "I don't want you to freeze to death."
                    scene ep10_after_bbq5 with dissolve
                    mc "Ah, so you're gonna keep me warm?"
                    scene ep10_after_bbq6 with dissolve
                    ly "Don't make me regret it."
                    scene ep10_after_bbq7 with dissolve
                    if ep9_spoon_lily:
                        mc "I thought the rules said no spooning."
                    else:
                        mc "So, the rules are ok with spooning?"
                    scene ep10_after_bbq8 with dissolve
                    ly "Only to assert dominance, remember?"
                    scene ep10_after_bbq7 with dissolve
                    mc "Dominance against what? A bear?"
                    scene ep10_after_bbq9 with dissolve
                    ly "Haha! Yes! If a bear shows up, he'll get scared shitless seeing us like this."
                    ly "Also, grope my tits or something and it won't feel like spooning."
                    scene ep10_after_bbq10 with dissolve
                    mc "Hahaha."
                    scene ep10_after_bbq9 with dissolve
                    ly "And wipe that smile off your face. I can feel it in the back of my skull."
                    scene ep10_after_bbq11 with dissolve
                    $ renpy.pause()
                    $ new_bio("Lily", "At the DIKs' Thanksgiving party, I ended the night in my tent together with Lily. It surprised me that she was cool with it, since it didn't feel like it was a part of our rolling deal.")
                    jump ep10_party_eval_label

else:                    
    if branchJill:
        $ep10_wt_end_bbq="Jill"
    elif branchMayaJosy:
        $ep10_wt_end_bbq="Josy"
    elif branchSage:
        $ep10_wt_end_bbq="Sage"
    elif branchIsabella:
        $ep10_wt_end_bbq="Bella"
    elif ep10_rolling:
        $ep10_wt_end_bbq="Lily"
    else:
        $ep10_wt_end_bbq="Alone"
        
if branchJill:
    jump ep10_bbq_jill_end_event_label
if branchMayaJosy:
    jump ep10_bbq_jm_end_event_label
if branchSage:
    jump ep10_bbq_sage_lewd_label
if ep10_rolling:
    scene ep10_after_bbq1 with dissolve
    ly "No way... Is this where you're sleeping?"
    scene ep10_after_bbq3 with dissolve
    mc "Since I put up the tent and all, I figured why not?"
    mc "Wanna join?"
    scene ep10_after_bbq2 with dissolve
    ly "I don't think so. I can hear my bed calling my name from here."
    scene ep10_after_bbq3 with dissolve
    mc "I can't blame you. This night will get cold."
    mc "But now that most seem to be leaving, I'm gonna turn in."
    scene ep10_after_bbq4 with dissolve
    ly "What the hell... Make some room for me."
    scene ep10_after_bbq5 with dissolve
    mc "For real?"
    scene ep10_after_bbq6 with dissolve
    ly "I don't want you to freeze to death."
    scene ep10_after_bbq5 with dissolve
    mc "Ah, so you're gonna keep me warm?"
    scene ep10_after_bbq6 with dissolve
    ly "Don't make me regret it."
    scene ep10_after_bbq7 with dissolve
    if ep9_spoon_lily:
        mc "I thought the rules said no spooning."
    else:
        mc "So, the rules are ok with spooning?"
    scene ep10_after_bbq8 with dissolve
    ly "Only to assert dominance, remember?"
    scene ep10_after_bbq7 with dissolve
    mc "Dominance against what? A bear?"
    scene ep10_after_bbq9 with dissolve
    ly "Haha! Yes! If a bear shows up, he'll get scared shitless seeing us like this."
    ly "Also, grope my tits or something and it won't feel like spooning."
    scene ep10_after_bbq10 with dissolve
    mc "Hahaha."
    scene ep10_after_bbq9 with dissolve
    ly "And wipe that smile off your face. I can feel it in the back of my skull."
    scene ep10_after_bbq11 with dissolve
    $ renpy.pause()
    $ new_bio("Lily", "At the DIKs' Thanksgiving party, I ended the night in my tent together with Lily. It surprised me that she was cool with it since it didn't feel like it was a part of our rolling deal.")

label ep10_party_eval_label:
hide screen new_phone_screen
if minigames:
    scene ep10_bbq_guitar_jm_event7_fr1 with Fade(1,1,1)
    $ renpy.block_rollback()
    $ pp_continue_label = "ep10_pp_cont2_label"
    $ renpy.pause(1)
    jump party_planner_setup_evaluation_label
    label ep10_pp_cont2_label:
    $ renpy.block_rollback()

    $ tmpStr = ""
    if ep10_pp_meat == 2:
        $ tmpStr += "• Hot Dogs "
    elif ep10_pp_meat == 1:
        $ tmpStr += "• BBQ Pork "
    else:
        $ tmpStr += "• BBQ Quality Meat "
    if ep10_pp_alcohol == 2:
        $ tmpStr += "• B.Y.O.B.  "
    elif ep10_pp_alcohol == 1:
        $ tmpStr += "• Leftover Alcohol "
    else:
        $ tmpStr += "• New Alcohol "
    if ep10_pp_activity == 0:
        $ tmpStr += "• Beer Pong"

    $ mphone_pp_history_list.append("DIKs' Thanksgiving Party\n{color=fe9416}Activities:{/color} %s\n{color=fe9416}Total Party Score:{/color} {color=ffed00}%d{/color}\n{color=fe9416}Total Score:{/color} {color=ffed00}%d{/color}\n{color=e51475}Multiplier: %sx{/color}\n{color=fe9416}Rank:{/color} {color=ffed00}%s{/color}" % (tmpStr,pp_round_score,pp_score,pp_multiplier,pp_party_rank[1][1]))
    $ mphone_pp_history_list.append("\n")
    $ mphone_pp_history_list.append("\n")
    $ mphone_pp_history_list.append("\n")

    if steamAchievements and not config.console and not config.developer:
        if pp_party_rank[1][0]==10 and pp_party_rank[1][1]=="S":
            $ achievement.grant("IDS3_21")
            init:
                $ achievement.register("IDS3_21")
            $ achievement.Sync()
else:
    $ party_planner_get_nm_rank(pp_current_party_happiness)
    $ party_planner_get_nm_score(pp_nm_dik_happiness)
show screen new_phone_screen
if branchIsabella and ep10_wt_end_bbq=="Bella":
    jump ep10_bbq_isabella_end_label
stop music fadeout 3
scene black with fade
$ renpy.pause(2)
play music "music/ep9/licensed_music/track120.mp3"
if branchJill and ep10_wt_end_bbq=="Jill":
    scene ep10_pre_tg20 with dissolve
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    scene ep10_pre_tg33 with dissolve
elif branchSage and ep10_wt_end_bbq=="Sage":
    scene ep10_pre_tg27 with dissolve
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    scene ep10_pre_tg1 with dissolve
else:
    scene ep10_pre_tg4 with dissolve
$ renpy.pause()

if branchJill and ep10_wt_end_bbq=="Jill":
    scene ep10_pre_tg21 with dissolve
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    scene ep10_pre_tg34 with dissolve
elif branchSage and ep10_wt_end_bbq=="Sage":
    scene ep10_pre_tg28 with dissolve
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    scene ep10_pre_tg2 with dissolve
else:
    scene ep10_pre_tg3 with dissolve
mc "Ahhh... Wha... Hnnn..."

scene ep10_pre_tg41 with dissolve
tm "[name]! Open up wide!"
mc "AHHH!! IS IT ANOTHER SHOT?"
tm "Derek! Do it!"
scene ep10_pre_tg42 with dissolve
mc "No! Get that cock away from me!"
de "Hahaha!"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg43
mc "Dad taught me everything I know. He knows all kinds of stuff."
scene ep10_pre_tg44 with dissolve
tm "That's fucking cool."
play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg45
mc "Why don't you like me?"
scene ep10_pre_tg46 with dissolve
tm "I do! We're bonding here, aren't we?"
scene ep10_pre_tg45 with dissolve
mc "You're drunk! Where are the shots?"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg47
mc "I'M HAVING THE BEST TIME OF MY LIFE!"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg39
rs "[name], you can't take your clothes off in the club like that."
scene ep10_pre_tg40 with dissolve
mc "*{i}Sobs{/i}* I just wanted to dance for them!"

play sound "sound_effects/whoosh_2.mp3"
$ renpy.sound.play("sound_effects/season2/puke.mp3", channel="sfx3", loop=False)
scene ep10_pre_tg48 with vpunch
mc "*{i}Pukes{/i}*"
my "How much did you drink?"

stop music
if branchJill and ep10_wt_end_bbq=="Jill":
    scene ep10_pre_tg22 with vpunch
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    scene ep10_pre_tg35 with vpunch
elif branchSage and ep10_wt_end_bbq=="Sage":
    scene ep10_pre_tg29 with vpunch
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    scene ep10_pre_tg6 with vpunch
else:
    scene ep10_pre_tg5 with vpunch
$ renpy.sound.play("sound_effects/season3/forest_soundscape.mp3", channel="sfx3", loop=True)
mc "Huh!?"

if branchJill and ep10_wt_end_bbq=="Jill":
    scene ep10_pre_tg23 with dissolve
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    scene ep10_pre_tg36 with dissolve
elif branchSage and ep10_wt_end_bbq=="Sage":
    scene ep10_pre_tg30 with dissolve
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    scene ep10_pre_tg7 with dissolve
else:
    scene ep10_pre_tg8 with dissolve
mc "Ugh..."

if branchSage and ep10_wt_end_bbq=="Sage":
    scene ep10_pre_tg32 with dissolve
    sa "*{i}Snores{/i}*"
    scene ep10_pre_tg31 with dissolve
    mc "(It looks like she's sleeping well. Surprisingly, I did too.)"
elif branchJill and ep10_wt_end_bbq=="Jill":
    scene ep10_pre_tg24 with dissolve
    ji "Good morning..."
    scene ep10_pre_tg25 with dissolve
    mc "Morning... Have you been up for long?"
    scene ep10_pre_tg24 with dissolve
    ji "No, I just awoke. But it was hard to fall asleep. How was your sleep?"
    scene ep10_pre_tg25 with dissolve
    mc "I slept like a log. But the air is kinda funky in here."
    scene ep10_pre_tg26_b with dissolve
    ji "Yes. Get some fresh air. I'll join you in a few."
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    scene ep10_pre_tg37 with dissolve
    $ renpy.pause()
    scene ep10_pre_tg38 with dissolve
    mc "(They're still sleeping. I need some fresh air.)"
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    scene ep10_pre_tg9 with dissolve
    mc "(This was a nice surprise last night...)"
    scene ep10_pre_tg10 with dissolve
    mc "(I thought she would have left when I woke up. I'm happy she didn't.)"
else:
    scene ep10_pre_tg11 with dissolve
    mc "(I wonder if I'm the only one here...)"

$ renpy.sound.play("sound_effects/season3/bonfire.mp3", channel="sfx2", loop=True)
scene ep10_pre_tg12 with dissolve
jac "Morning..."
scene ep10_pre_tg13 with dissolve
mc "Jacob? Are you still here?"
scene ep10_pre_tg14 with dissolve
jac "Derek refused to leave and someone had to stay with him."
if branchSage and ep10_wt_end_bbq=="Sage":
    jac "I had to listen to you and Sage going at it all night."
    scene ep10_pre_tg13 with dissolve
    mc "It wasn't {i}all{/i} night."
    scene ep10_pre_tg14 with dissolve
    jac "It felt like it."
elif branchMayaJosy and ep10_wt_end_bbq=="Josy":
    jac "I'd rather spend the night in your tent, you lucky dog."
    scene ep10_pre_tg13 with dissolve
    mc "Haha... Yeah. It was a nice night."
elif branchJill and ep10_wt_end_bbq=="Jill":
    jac "Looks like you had it better."
    scene ep10_pre_tg13 with dissolve
    mc "Yeah. I can't complain."
elif ep10_rolling and ep10_wt_end_bbq=="Lily":
    jac "Who was in there with you?"
    scene ep10_pre_tg13 with dissolve
    mc "Lily."
    scene ep10_pre_tg14 with dissolve
    jac "Really? Damn... You're lucky."
else:
    scene ep10_pre_tg13 with dissolve
    mc "You're a good brother, Jacob. What about everyone else?"
    scene ep10_pre_tg14 with dissolve
    jac "They went back to the mansion when people started to drop off."

scene ep10_pre_tg18 with dissolve
mc "*{i}Yawns{/i}*"
scene ep10_pre_tg14 with dissolve
jac "You look like a mess today."
scene ep10_pre_tg13 with dissolve
mc "Thanks."
scene ep10_pre_tg14 with dissolve
jac "I think it's the beard. You need to give it time to grow some more."
scene ep10_pre_tg19 with dissolve
mc "No thanks. It's itching like crazy."
scene ep10_pre_tg14 with dissolve
jac "Yeah, it will do that at first. It stops when it grows longer."
scene ep10_pre_tg13 with dissolve
mc "I'm shaving it off later. I don't like it."
scene ep10_pre_tg14 with dissolve
jac "What a bummer."
scene ep10_pre_tg15 with dissolve
mc "You said I looked like a mess."
scene ep10_pre_tg16 with dissolve
jac "A cool mess."
scene ep10_pre_tg15 with dissolve
mc "Haha."
scene ep10_pre_tg14 with dissolve
jac "[name]...?"
scene ep10_pre_tg13 with dissolve
mc "Yeah?"
scene ep10_pre_tg14 with dissolve
jac "You're with us, right?"
scene ep10_pre_tg13 with dissolve
mc "With who?"
scene ep10_pre_tg14 with dissolve
jac "The DIKs. 100%%?"
scene ep10_pre_tg13 with dissolve
mc "Dude, 110%%. You know that."
scene ep10_pre_tg14 with dissolve
jac "Just checking."
$ renpy.music.stop(channel="sfx3", fadeout=3)
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep10_pre_tg17 with dissolve
$ renpy.pause()

label ep10_tg_label:
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep10/hollow_sky.mp3"])
scene ep10_tg1 with wipeleft
$ renpy.pause()
play sound "sound_effects/season3/shave.mp3"
scene ep10_tg2 with dissolve
$ renpy.pause()
scene ep10_tg3 with dissolve
play sound "sound_effects/season2/faucet2.mp3"
mc "(Bye-bye, beard. At least I proved I can grow you guys.)"
scene ep10_tg4 with dissolve
mc "(And now I look like I'm five years younger... Weird.)"
jump ep10_freeroam_room2_label

label ep10_tg2_label:
play music "music/ep10/now_or_never.mp3"
scene ep10_tg5 with dissolve
mc "Are you ready to leave?"
scene ep10_tg6 with dissolve
de "That's what you're wearing?"
scene ep10_tg5 with dissolve
mc "Uh... That's what {i}you're{/i} wearing?"
scene ep10_tg7 with dissolve
de "It's a holiday, [mc_de]. You gotta look the best you can for this."
scene ep10_tg8 with dissolve
de "Don't worry, I'll find you something good to wear."
mc "I can't say I have high expectations for any clothes you'd pull out of a trash bag."
de "The trash bag is for logistics. Everything in it is clean."
scene ep10_tg9 with dissolve
de "Here, wear this."
scene ep10_tg12 with dissolve
mc "I'm not sure if this sweater is me."
scene ep10_tg10 with dissolve
de "It is you today."
de "Now, where did we land on the vibrator?"
scene ep10_tg11 with dissolve
mc "I'll put it in my pocket. Far away from my asshole."
scene ep10_tg10 with dissolve
de "It's your call."
de "If I buzz you one time, it means hide. Two times means go."
scene ep10_tg11 with dissolve
mc "One for hide, two for go. Got it."
mc "I still think it should be you who gets the contract."
scene ep10_tg10 with dissolve
de "I'll do my best and I've got your back. Also, you have an easy excuse if you get caught."

scene ep10_tg13 with dissolve
my "We're here."
scene ep10_tg14 with dissolve
sa "Wow... That sweater is so not you."
scene ep10_tg16 with dissolve
mc "Thank you!"
scene ep10_tg15 with dissolve
my "Why? I think you look great in it."
scene ep10_tg17 with dissolve
mc "It's itchy and Derek pulled it out from a trash bag."
scene ep10_tg18 with dissolve
js "Hey, guys."
if ep9_jm_sad:
    if branchJill:
        scene ep10_tg19b with dissolve
    else:
        scene ep10_tg19 with dissolve
    mc "Hey..."
else:
    if branchJill:
        scene ep10_tg20b with dissolve
    else:
        scene ep10_tg20 with dissolve
    mc "Hey!"
if branchIsabella:
    mc "Wow... All of you are here."
else:
    mc "Wait a minute... Why are all of you here?"
scene ep10_tg21 with dissolve
isa "You'll need a ride, won't you?"
if ep9_jm_sad:
    if branchJill:
        scene ep10_tg19b with dissolve
    else:
        scene ep10_tg19 with dissolve
else:
    if branchJill:
        scene ep10_tg20b with dissolve
    else:
        scene ep10_tg20 with dissolve
mc "What about Thanksgiving?"

scene ep10_tg22 with dissolve
js "Even if I'm not coming with you guys, I still want to be there for you."
js "Thanksgiving is usually a big deal."
js "You're supposed to be with friends and family... The ones you love."
js "But Thanksgiving at my place is a mess. Mom and Dad don't celebrate together, and these days, it's not an enjoyable day for me."
scene ep10_tg23 with dissolve
if ep8_told_josy_chad:
    sa "And I promised you guys I'd come. Besides, Mom canceled Thanksgiving today...because..."
else:
    sa "Mom canceled Thanksgiving today...because..."
scene ep10_tg24 with dissolve
sa "Um... It's whatever."
sa "I'd rather be here with you now anyway."
if branchIsabella:
    scene ep10_tg25 with dissolve
    ji "I talked to Bella and we both felt we could spend it helping you instead."
    ji "I mean, we can't do much, but we can do something."
    scene ep10_tg26 with dissolve
    $ renpy.pause()
else:
    scene ep10_tg25 with dissolve
    ji "I've been celebrating Thanksgiving with Bella these last couple of years."
    ji "We both felt we could spend it helping you instead."
    ji "I mean, we can't do much, but we can do something."
scene ep10_tg27 with dissolve
my "You guys... This means so much to me."
scene ep10_tg28 with dissolve
my "What about you, [name]? Are you still ok with this?"
scene ep10_tg29 with dissolve
mc "It sucked to tell Dad I wasn't coming home for today, but he understood and we'll celebrate it this weekend instead."
mc "Like all of you, I'm here for Maya."
mc "It feels like we're close to solving this problem for her once and for all."
scene ep10_tg28 with dissolve
my "Let's go do it."
scene ep10_tg30 with dissolve
de "To be clear... We're not all barging in there together, right?"
scene ep10_tg31 with dissolve
js "No, we'll wait for you guys at Bella's place."
scene ep10_tg32 with dissolve
mc "Are you guys in?"
scene ep10_tg33 with dissolve
my "We're doing this!"
de "There is no turning back now."
scene ep10_tg34 with dissolve
js "For Maya."
sa "For Maya."
scene ep10_tg35 with dissolve
stop music fadeout 3
isa "For Maya."
ji "For Maya."

play music "music/ep7/morning_routine.mp3"
queue music ["music/ep9/passing_time.mp3","music/ep1/fresh_air.mp3","music/ep9/getting_closure.mp3","music/ep9/relaxed.mp3","music/ep7/morning_routine.mp3"]

if ep8_told_josy_chad:
    scene ep10_tg36 with wipeleft
else:
    scene ep10_tg36b with wipeleft
mc "This is a nice house. Did you grow up here?"
my "We did."
scene ep10_tg37 with dissolve
mc "Any last words of advice?"
scene ep10_tg38 with dissolve
my "Yes. Be yourself."
scene ep10_tg39 with dissolve
de "But also be someone else completely."
scene ep10_tg40 with dissolve
my "No!"
scene ep10_tg39 with dissolve
de "Trust me, if [mc_de] was himself, Dad wouldn't like it."
scene ep10_tg40 with dissolve
my "[name] has a filter and knows how to behave. It's not like he will streak through our house together with you, now, is it?"
if ep8_told_josy_chad:
    scene ep10_tg41 with dissolve
    de "And you..."
    de "Feel free to touch my butt in front of Dad."
    scene ep10_tg42 with dissolve
    sa "What's wrong with you?"
if ep8_told_josy_chad:
    scene ep10_tg43 with dissolve
else:
    scene ep10_tg43b with dissolve
play sound "sound_effects/bell.mp3"
"*{i}Doorbell{/i}*"
if ep8_told_josy_chad:
    scene ep10_tg44 with dissolve
else:
    scene ep10_tg44b with dissolve
de "Mom? Dad? We're here."
scene ep10_tg45 with dissolve
pa "There you are! Welcome!"

if ep8_told_josy_chad:
    scene ep10_tg46 with dissolve
    pa "I heard you'd be bringing guests."
    pa "Who is this?"
    scene ep10_tg48 with dissolve
    de "Dad! This is Sage. She is my girlfriend."
    scene ep10_tg47 with dissolve
    pa "You've got yourself a girlfriend?"
    scene ep10_tg48 with dissolve
    de "Sure did! Right, hun?"
    scene ep10_tg49 with dissolve
    sa "I'm a close friend of Derek. He's just making jokes, as usual."
    scene ep10_tg46 with dissolve
    pa "Oh? Yeah, he is a bit of a joker. He's always been like that."
    pa "Girlfriend or friend - you're welcome to join us. I'm Patrick."
    scene ep10_tg50 with dissolve
    de "*{i}Whispers{/i}* Stick to the script."
    scene ep10_tg51 with dissolve
    sa "*{i}Whispers{/i}* Not when you're gonna act like we're a married senior couple."
    sa "*{i}Whispers{/i}* From now on, I'm your friend. You can stick with that."
    scene ep10_tg50 with dissolve
    de "*{i}Whispers{/i}* A girl as a close friend... It's amazing you fooled Dad with that one."

if ep7_patrick_score < 0:
    if ep8_told_josy_chad:
        scene ep10_tg52 with dissolve
    else:
        scene ep10_tg52b with dissolve
else:
    if ep8_told_josy_chad:
        scene ep10_tg52c with dissolve
    else:
        scene ep10_tg52d with dissolve
pa "Oh, I remember you. [name], was it?"
if ep7_patrick_score < 0:
    scene ep10_tg53 with dissolve
    mc "You've got a good memory."
    scene ep10_tg54 with dissolve
    pa "Aha. Well... Welcome."
else:
    scene ep10_tg53b with dissolve
    mc "You've got a good memory. It's nice to see you again, sir."
    scene ep10_tg54b with dissolve
    pa "Please, call me Patrick. And likewise. Welcome in!"

if ep8_told_josy_chad:
    scene ep10_tg55 with dissolve
else:
    scene ep10_tg55b with dissolve
de "Where's Mom?"
scene ep10_tg56 with dissolve
pa "She's resting. It's almost time for her morphine. You know how she is before that."
if ep8_told_josy_chad:
    pa "Let her greet your friends at her own pace."
if ep8_told_josy_chad:
    scene ep10_tg55 with dissolve
else:
    scene ep10_tg55b with dissolve
de "I'll go say hi to her."
if ep8_told_josy_chad:
    scene ep10_tg57 with dissolve
    sa "What should I do?"
    scene ep10_tg58 with dissolve
    de "Have a tour of the house. You can check my room upstairs!"
    de "*{i}Whispers{/i}* Turn right when you get upstairs; the office is the second door to your left."
    scene ep10_tg57 with dissolve
    sa "Gotcha."
$ guideSuggestedPage = 140
scene ep10_tg59 with dissolve
pa "You two seem to have grown close to each other."
if ep8_told_josy_chad:
    scene ep10_tg60 with dissolve
    my "Yes, we have. [name] is actually my boyfriend."
    scene ep10_tg62 with dissolve
    pa "..."
    scene ep10_tg63 with dissolve
    pa "Your {i}boyfriend{/i}?"
    scene ep10_tg67 with dissolve
    my "He is."
    scene ep10_tg70 with dissolve
    my "*{i}Smack{/i}*"
    scene ep10_tg68 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Bella)","(-DIK)","(+DIK)","","","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if branchAlone:
                        $mod_choices[4]="(possible Cathy scene)"
    
    menu:
        "Kiss her back [m_c1][mod_choices[0]]":
            $ RPmaya += 1
            if branchMayaJosy:
                scene ep10_tg72 with dissolve
            else:
                scene ep10_tg71 with dissolve
            mc "*{i}Smack{/i}*"
            if branchMayaJosy:
                scene ep10_tg73 with dissolve
                $ renpy.pause()
        "Play it cool":
            scene ep10_tg69 with dissolve
            mc "Yep. It's true."
    scene ep10_tg64 with dissolve
    pa "So, you lived together with my daughter and now you're her boyfriend?"
    scene ep10_tg69 with dissolve
    mc "Yeah, well, I...uh... This happened after I moved out."
    mc "I moved into a fraternity."
    scene ep10_tg60 with dissolve
    my "I've told you about that, Dad."
else:
    scene ep10_tg65 with dissolve
    mc "Yeah, we have. Maya's a great friend of mine and we've spent a lot of time together in class."
    scene ep10_tg64 with dissolve
    pa "In class? Are you studying social work, too?"
    scene ep10_tg65 with dissolve
    mc "No, I'm in the engineering program. But we share a few common classes."
    scene ep10_tg64 with dissolve
    pa "Ok, because I assumed you were close because you shared a dorm."
    scene ep10_tg65 with dissolve
    mc "Oh...right! That too."
    scene ep10_tg66 with dissolve
    $ renpy.pause()
    scene ep10_tg65 with dissolve
    mc "But I moved out. I live in a fraternity now."
    scene ep10_tg60 with dissolve
    my "I've told you about that, Dad."
scene ep10_tg59 with dissolve
pa "I remember."
pa "Maya, will you help me out in the kitchen with dinner?"
scene ep10_tg61 with dissolve
my "Sure..."
scene ep10_tg74 with dissolve
play sound "sound_effects/season2/vibrate.mp3"
"*{i}Vibrations{/i}*"
mc "(Two for go. That's my cue. Time to look around.)"
jump ep10_freeroam_tg_label

label ep10_ending_label:

mc "{i}What am I thankful for?{/i}"
mc "{i}I'm thankful for that Thanksgiving. It brought everyone a lot closer.{/i}"
scene ep10_ending1 with dissolve
mc "{i}Which is ironic, because it was also the worst Thanksgiving I've ever experienced.{/i}"

scene ep10_ending2
hide screen ep10_snow_screen
with dissolve
mc "{i}And that horrible holiday weekend was only just beginning.{/i}"
scene ep10_ending3 with dissolve
$ renpy.pause()

scene ep10_ending4 with dissolve
$ renpy.pause()
scene ep10_ending6 with dissolve
$ renpy.pause()
scene ep10_ending5 with dissolve
$ renpy.pause()

scene ep10_ending7
show screen ep10_snow_screen
with dissolve
mc "{i}I got to see new sides of both Derek and Maya. And I understand them much better for it.{/i}"
mc "{i}Derek wanted his sister to be safe. And out of all the things he's ever told me - usually disgusting - this was the most beautiful thing he ever said.{/i}"
mc "{i}Who doesn't want someone they love to be safe?{/i}"
scene ep10_ending8 with dissolve
mc "{i}Who doesn't want to feel safe?{/i}"

play sound "sound_effects/cellphone.mp3"
scene ep10_ending9 with dissolve
"*{i}Phone rings{/i}*"
scene ep10_ending10 with dissolve
ri "Quinn? Yeah, it went ok, but listen-"
scene ep10_ending11 with dissolve
ri "I'm on my way, but I think I'm being followed. Can you meet me up?"
scene ep10_ending12 with dissolve
ri "Vinny?"
play sound "sound_effects/shove.mp3"
scene ep10_ending13 with hpunch
ri "HEY! LET ME GO!"
ri "HELP! HELP!!!"
play sound "sound_effects/burnout.mp3"
scene ep10_ending14 with dissolve
$ renpy.pause()
scene ep10_ending15 with dissolve
$ renpy.pause()

scene black
stop music fadeout 10
hide screen ep10_snow_screen
$ renpy.pause(2)
jump ep10_save_here_label

label ep10_save_here_label:
hide screen new_phone_screen
scene black
$ renpy.pause(1)
$ persistent.ep10_completed = True
$ updateDikScore()

if steamAchievements:
    $ achievement.grant("IDS3_03")
    init:
        $ achievement.register("IDS3_03")
    $ achievement.Sync()
    call check_steam_achievements_label from _call_check_steam_achievements_label_2

if renpy.loadable("scripts/episode11/update11.rpyc"):
    scene ep10_episode_endb
else:
    scene ep10_episode_end
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


jump ep10_generate_report_text_label
$ renpy.pause()

label ep10EndLabel:
stop music fadeout 2
$ renpy.pause(2)

if renpy.loadable("scripts/episode11/update11.rpyc"):
    jump startUpdate11
$ qM = persistent.quick_menu
$ persistent.quick_menu = 0
jump game_credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

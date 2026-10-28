label brawler_story_alex0_label:
if minigames:
    $ renpy.block_rollback()
scene brawler_story_alex1 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene brawler_story_alex2 with hpunch
$ renpy.pause()
scene brawler_story_alex3 with dissolve
al "Pff!!!"
scene brawler_story_alex4 with dissolve
mc "What's your problem?"
scene brawler_story_alex5 with dissolve
$ renpy.pause()
scene brawler_story_alex4 with dissolve
mc "You're on the wrong side of the gym. Leave me alone."
scene brawler_story_alex6 with dissolve
al "You can punch that sack all day long, but it won't make a difference."
al "You've barely got any muscles."
scene brawler_story_alex4 with dissolve
mc "You're delusional if you think that a weightlifter would win against someone who practices fighting because of how much muscle they're packing."
scene brawler_story_alex6 with dissolve
al "Yeah? You don't look that tough to me."
scene brawler_story_alex7 with dissolve
mc "I'd wipe the floor with you any day."
scene brawler_story_alex6 with dissolve
al "How much do you wanna bet?"
scene brawler_story_alex7 with dissolve
mc "Don't bother."
scene brawler_story_alex6 with dissolve
al "You're scared, huh?"
scene brawler_story_alex7 with dissolve
mc "I'd happily punch that smile off your face."
scene brawler_story_alex8 with dissolve
al "{color=00ff00}$2{/color} says you'll lose."
scene brawler_story_alex7 with dissolve
if not minigames:
    menu:
        "Fight him":
            $ renpy.pause(0.5)
        "Don't fight him":
            mc "Fuck off. Leave me alone."
            scene brawler_story_alex9 with dissolve
            dwy "You're not fighting him?"
            scene brawler_story_alex10 with dissolve
            mc "No. He's not worth my time."
            scene brawler_story_alex11 with dissolve
            dwy "I hear you."
            jump ep10_after_spar_label

mc "Sure. I'll take your money too."
scene brawler_story_alex9 with dissolve
dwy "You're doing this?"
scene brawler_story_alex10 with dissolve
mc "Yeah. That asshole is practically begging me to fight him."
scene brawler_story_alex11 with dissolve
dwy "Sounds like the sucka has it coming."
dwy "Don't let your emotions get the best of you. The rules of the fight are the same, even when you hate the guy."
scene brawler_story_alex10 with dissolve
mc "I'll show him."
scene brawler_story_alex12 with dissolve
dwy "We got a fight, people!"
$ renpy.pause(0.5)
$ renpy.block_rollback()
if minigames:
    $ bn_history_list[1] = 1
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Alex":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_alex_fight_nomg_label

label brawler_story_alex_after0_label:
$ renpy.block_rollback()
$ bn_history_list[1] = 2
if not minigames:
    $ mny(2)
scene brawler_story_alex14 with dissolve
mc "Pay up."
scene brawler_story_alex15 with dissolve
al "You got lucky."
scene brawler_story_alex14 with dissolve
mc "Maybe I did, maybe I didn't. You can always bet me more money and find out."
scene brawler_story_alex13 with dissolve
dwy "You whooped his ass."
mc "Haha, sure did."
if not minigames:
    jump ep10_after_spar_label
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_alex_after0b_label:
$ renpy.block_rollback()
scene brawler_alex_mc_lose with dissolve
al "Haha! Beat your ass. Fucking loser."
if not minigames:
    jump ep10_after_spar_label
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_chao0_label:
$ renpy.block_rollback()
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene brawler_story_chao1 with hpunch
$ renpy.pause()
scene brawler_story_chao2 with dissolve
chao "You've got good moves."
scene brawler_story_chao3 with dissolve
if currentEpisode > 10:
    mc "Thanks!"
else:
    mc "Thanks. I'm [name]."
    scene brawler_story_chao4 with dissolve
    chao "Pleased to meet you. I'm Chao."
scene brawler_story_chao5 with dissolve
chao "Your kick is sloppy."
scene brawler_story_chao3 with dissolve
if currentEpisode > 10:
    mc "You think? Dwyane thinks it looks good."
else:
    mc "I'm trying my best."
    scene brawler_story_chao5 with dissolve
    chao "Dwyane told me he's teaching you how to fight."
    scene brawler_story_chao3 with dissolve
    mc "He wants to help me improve, yeah. So, we're gonna train together."
scene brawler_story_chao6 with dissolve
chao "Dwyane's kick can be sloppy too."
scene brawler_story_chao3 with dissolve
mc "Are you trash-talking Dwyane?"
scene brawler_story_chao5 with dissolve
chao "No. I'm stating what I see."
chao "Dwyane disagrees with me. He doesn't want to learn it my way."
scene brawler_story_chao3 with dissolve
mc "Well, that's up to him."
scene brawler_story_chao7 with dissolve
chao "How about you? Do you disagree too?"
scene brawler_story_chao3 with dissolve
mc "No, I know my fighting is sloppy. I want to tighten it up."
scene brawler_story_chao8 with dissolve
chao "Good. Show me your best. Up there."
scene brawler_story_chao3 with dissolve
mc "Do you want to fight me?"
scene brawler_story_chao5 with dissolve
chao "While the bag is good for practice, it won't give you as much knowledge as a true fight does."
scene brawler_story_chao9 with dissolve
mc "You'll have to go easy on me."
scene brawler_story_chao10 with dissolve
chao "You lead, and I will respond. Show me what you got."
$ renpy.pause(0.5)
$ renpy.block_rollback()
$ bn_history_list[2] = 1
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Chao":
            bn_init_fight(i)
pause

label brawler_story_chao_after0_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_chao11 with dissolve
    chao "Hm... Again?"
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

scene brawler_story_chao12 with dissolve
chao "That's enough for now."
scene brawler_story_chao13 with dissolve
mc "How did I do?"
scene brawler_story_chao12 with dissolve
chao "Your style interests me. You blend Muay Thai into it."
scene brawler_story_chao13 with dissolve
mc "When my dad taught me, we didn't exactly stick to one school of practice. We tried a lot of different things together."
scene brawler_story_chao12 with dissolve
chao "Interesting. Yet still..."
chao "Sloppy."
scene brawler_story_chao14 with dissolve
chao "You guide your leg with your body, yes?"
chao "And when you kick..."
play sound "sound_effects/whoosh.mp3"
scene brawler_story_chao15 with hpunch
chao "Pivot hard and strike through your opponent."
$ renpy.pause(0.5)
$ bn_history_list[2] = 2
$ renpy.block_rollback()
show screen brawler_result_screen
pause


label brawler_story_dwyane0_label:
$ renpy.block_rollback()
if not minigames:
    scene brawler_story_dwyane1 with wipeleft
else:
    scene brawler_story_dwyane1 with dissolve
dwy "[name]! Get up here."
scene brawler_story_dwyane3 with dissolve
mc "Yeah? Are we doing this?"
scene brawler_story_dwyane2 with dissolve
dwy "That's what you want, right?"
scene brawler_story_dwyane4 with dissolve
mc "How should we do it?"
scene brawler_story_dwyane6 with dissolve
dwy "Give me all you got."
scene brawler_story_dwyane4 with dissolve
mc "Are you sure? It would be stupid if we got hurt."
scene brawler_story_dwyane6 with dissolve
dwy "If you're afraid of getting hurt, you're in the wrong room, dawg."
dwy "What's it gonna be?"
scene brawler_story_dwyane4 with dissolve
mc "Ok."
scene brawler_story_dwyane6 with dissolve
dwy "We stop when you tap out."
scene brawler_story_dwyane4 with dissolve
mc "What if you tap out first?"
scene brawler_story_dwyane5 with dissolve
dwy "Make me."
if not minigames:
    jump brawler_story_dwyane_fight_nomg_label
$ renpy.pause(0.5)
$ bn_history_list[3] = 1
$ renpy.block_rollback()
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Dwyane":
            bn_init_fight(i)
pause

label brawler_story_dwyane_after0_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_dwyane10 with dissolve
    dwy "Had enough?"
    scene brawler_story_dwyane4 with dissolve
    mc "Yeah... Fuck, you almost hurt me."
    scene brawler_story_dwyane6 with dissolve
    dwy "Nah, I didn't. You'll walk it off."
    if not minigames:
        jump ep10_after_spar_label
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

if minigames:
    $ bn_history_list[3] = 2
scene brawler_story_dwyane6 with dissolve
dwy "Aight, that's enough."
scene brawler_story_dwyane4 with dissolve
mc "Are you tapping out?"
scene brawler_story_dwyane6 with dissolve
dwy "Nah, but that's enough."
scene brawler_story_dwyane4 with dissolve
mc "That sounds like you're tapping out to me."

play sound "sound_effects/season3/counter.mp3"
scene brawler_story_dwyane7 with hpunch
mc "Whoa..."
scene brawler_story_dwyane8 with dissolve
dwy "We're stopping, or I'd have to hurt you. I don't want that."
dwy "We have to know and respect our limits."
scene brawler_story_dwyane9 with dissolve
mc "I hear you. Thanks for the fight."
scene brawler_story_dwyane6 with dissolve
dwy "Come. I wanna teach you something."
scene brawler_story_dwyane4 with dissolve
mc "Lay it on me."
scene brawler_story_dwyane6 with dissolve
dwy "I'll show you at the bag."
if not minigames:
    jump ep10_after_spar_label
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_tate0_label:
$ renpy.block_rollback()
if currentEpisode > 10:
    scene brawler_story_tate3 with dissolve
    tate "[name]? Got time to spar?"
    scene brawler_story_tate2 with dissolve
    mc "Sure."
else:
    scene brawler_story_tate1 with dissolve
    tate "It looks like we're the same weight class."
    scene brawler_story_tate2 with dissolve
    mc "Yeah, looks like it."
    scene brawler_story_tate3 with dissolve
    tate "New in the club?"
    scene brawler_story_tate2 with dissolve
    mc "I'm not with you guys. Dwyane told me it was cool to practice here."
    scene brawler_story_tate3 with dissolve
    tate "Ah, Dwyane. He's a cool guy."
    tate "I'm Tate."
    scene brawler_story_tate2 with dissolve
    mc "[name]."
    scene brawler_story_tate3 with dissolve
    tate "That's a shame about the club, though. Would have loved to fight someone other than Chao."
    tate "I'd actually thought I had a chance to win for once, haha."
    scene brawler_story_tate4 with dissolve
    mc "I'll still fight you if you want."
    scene brawler_story_tate3 with dissolve
    tate "You will?"
    scene brawler_story_tate2 with dissolve
    mc "I'm a rookie here, though."
    scene brawler_story_tate3 with dissolve
    tate "You're not a rookie. I saw you pummel that heavy bag before."
    tate "Got time for it now?"
    scene brawler_story_tate2 with dissolve
    mc "Sure."
$ renpy.pause(0.5)
$ bn_history_list[4] = 1
$ renpy.block_rollback()
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Tate":
            bn_init_fight(i)
pause

label brawler_story_tate_after0_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_tate5 with dissolve
    chao "Nice job. You won one."
    scene brawler_story_tate6 with dissolve
    tate "That sounded sarcastic."
    scene brawler_story_tate5 with dissolve
    chao "Because it was."
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

$ bn_history_list[4] = 2
scene brawler_story_tate7 with dissolve
tate "Ok, stop!"
scene brawler_story_tate8 with dissolve
mc "Are you ok?"
if currentEpisode > 10:
    scene brawler_story_tate9 with dissolve
    tate "Yeah, I just need to catch my breath."
else:
    scene brawler_story_tate9 with dissolve
    tate "You're definitely not a rookie. And if you say you are, you're gonna make me doubt my abilities hard."
    scene brawler_story_tate10 with dissolve
    mc "My dad taught me how to fight to defend myself when I was younger. But I'm a rookie when it comes to fighting like this."
    scene brawler_story_tate9 with dissolve
    tate "Ok, that makes me feel better. You don't have to pay to learn how to do things in life."
    tate "Obviously, your training made a big difference."
    tate "I will have to practice more, and maybe next time I'll beat you."
    scene brawler_story_tate10 with dissolve
    mc "Looking forward to it."
    scene brawler_story_tate9 with dissolve
    tate "Welcome to the fun side of the gym."
    scene brawler_story_tate10 with dissolve
    mc "Haha! Thanks, Tate."
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_troy0_label:
if not minigames:
    scene brawler_story_troy1 with wipeleft
else:
    $ renpy.block_rollback()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene brawler_story_troy1 with hpunch
mc "(Troy...)"
mc "(So, he fights too? Huh, I had no clue he did.)"
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene brawler_story_troy2 with hpunch
dwy "[name]! Get your ass over here."
scene brawler_story_troy3 with dissolve
dwy "[name], this is Troy."
scene brawler_story_troy4 with dissolve
mc "Yeah, I know who he is. We shared a dorm for a brief time."
scene brawler_story_troy5 with dissolve
dwy "Oh, you two go back, huh?"
scene brawler_story_troy6 with dissolve
if ep1_beat_up_troy and ep1_beat_up_troy_won:
    troy "I'm not surprised to see him here. He beat me up in the past."
elif ep1_beat_up_troy:
    troy "I'm not surprised to see him here. He fought me in the past."
else:
    troy "I'm not surprised to see him here. It felt like he wanted to beat me up in the past."
scene brawler_story_troy7 with dissolve
mc "You let Chad steal my guitar."
scene brawler_story_troy8 with dissolve
dwy "Whoa! I didn't think you two were mortal enemies."
scene brawler_story_troy6 with dissolve
troy "He's not my enemy."
scene brawler_story_troy4 with dissolve
if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Troy mad)","(-Isabella)","(-DIK)","(+DIK)","(Sage or Sarah scene)","(Sarah scene)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
menu:
    "Troy's nothing [m_c1][mod_choices[0]]":
        $ ep10_troy_mad = True
        mc "Troy's nothing to me."
        scene brawler_story_troy9 with dissolve
        dwy "Those sound like fighting words to me."
        scene brawler_story_troy10 with dissolve
        troy "Fuck you."
        scene brawler_story_troy9 with dissolve
        dwy "No point in trying to have you two get along, then, I see."
        $ new_bio("Troy", "I didn't want to get along with Troy at the gym and told him he was nothing to me.")
    "It's in the past":
        $ ep10_troy_mad = False
        scene brawler_story_troy11 with dissolve
        mc "Whatever it was, it's in the past. I'm not angry about it anymore."
        scene brawler_story_troy13 with dissolve
        dwy "Aight, it's cool then."
        $ new_bio("Troy", "I tried to bury the hatchet with Troy at the gym.")

dwy "Troy is a new member here."
dwy "Figured I'd introduce you. In case you ever needed someone else to train with."
if ep10_troy_mad:
    scene brawler_story_troy12 with dissolve
    mc "I'd fight him, but I won't train with him."
    scene brawler_story_troy10 with dissolve
    troy "That's the same thing, idiot."
    scene brawler_story_troy9 with dissolve
    dwy "Damn, I need to get myself some popcorn. Do we got a fight?"
    scene brawler_story_troy10 with dissolve
    if ep1_beat_up_troy:
        if ep1_beat_up_troy_won:
            troy "Bring it. I won't lose to you a second time."
        else:
            troy "Bring it. I'll beat your ass again."
    else:
        troy "Bring it."
    scene brawler_story_troy12 with dissolve
    mc "You're on."
else:
    scene brawler_story_troy11 with dissolve
    mc "I'm up for a fight if you are."
    scene brawler_story_troy14 with dissolve
    troy "Sure. I didn't think I'd be fighting someone today, but I could use the practice."
$ renpy.pause(0.5)
if not minigames:
    jump brawler_story_troy_fight_nomg_label
$ bn_history_list[0] = 1
$ renpy.block_rollback()
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Troy":
            bn_init_fight(i)
pause

label brawler_story_troy_after0_label:
$ renpy.block_rollback()
$ bn_quit_message = ""
if not bn_mc_won:
    if ep10_troy_mad:
        scene brawler_story_troy15 with dissolve
        troy "Boom. And down he goes."
        if ep1_beat_up_troy:
            mc "(Fuck... He's gotten good.)"
        else:
            mc "(Fuck... He's good.)"
    else:
        scene brawler_story_troy16 with dissolve
        troy "Are you hurt?"
        scene brawler_story_troy17 with dissolve
        mc "No, I just need to catch my breath."
        scene brawler_story_troy16 with dissolve
        troy "Let's fight again sometime."
        scene brawler_story_troy17 with dissolve
        mc "Yeah, I definitely want a rematch. Haha..."
    if not minigames:
        jump ep10_spar2_label
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

$ bn_history_list[0] = 2
if ep10_troy_mad:
    scene brawler_story_troy18 with dissolve
    troy "Fuck..."
    mc "I think I brought it."
    troy "I'll get you next time..."
else:
    scene brawler_story_troy19 with dissolve
    troy "Dammit..."
    scene brawler_story_troy20 with dissolve
    mc "Hey, you're pretty good."
    scene brawler_story_troy21 with dissolve
    troy "Obviously not good enough."
    scene brawler_story_troy20 with dissolve
    mc "I didn't think I'd say this, but..."
    mc "It was fun fighting you. We should do it again sometime."
    scene brawler_story_troy21 with dissolve
    troy "Ok."
if not minigames:
    jump ep10_spar2_label
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

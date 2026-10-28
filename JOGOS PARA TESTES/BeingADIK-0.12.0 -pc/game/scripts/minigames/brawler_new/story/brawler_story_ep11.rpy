label brawler_story_chao1_label:
$ renpy.block_rollback()
play sound "sound_effects/season2/punching_bag_kick.mp3"
scene ep11_brawler_story_chao1 with hpunch
$ renpy.pause()
scene ep11_brawler_story_chao2 with dissolve
chao "Have you improved your leg game?"
scene ep11_brawler_story_chao3 with dissolve
mc "I'm working on it. Thanks for the tips."
scene ep11_brawler_story_chao2 with dissolve
chao "I'd like to see it. Will you do me the honors?"
scene ep11_brawler_story_chao3 with dissolve
menu:
    "Always up for a fight":
        $ brawler_attitude += 1
        mc "Sure! I'm always up for a fight."
    "We can spar":
        $ brawler_attitude -= 1
        mc "More sparring? Sure!"

$ renpy.pause(0.5)
$ renpy.block_rollback()
$ bn_history_list[2] = 3
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Chao":
            bn_init_fight(i)
pause

label brawler_story_chao_after1_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_chao11 with dissolve
    chao "Hm... Again?"
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

scene brawler_story_chao12 with dissolve
chao "There's no denying it. You are improving."
chao "If you want my advice, it would be to loosen up when you kick."
scene brawler_story_chao13 with dissolve
mc "I thought I was."
scene brawler_story_chao12 with dissolve
chao "You are a bit stiff. Are you exhaling as you throw the kick?"
scene brawler_story_chao13 with dissolve
mc "I think I am."
scene ep11_brawler_story_chao4 with dissolve
chao "Let me see how you do it at the bag. I believe I have some pointers for you."

$ renpy.pause(0.5)
$ bn_history_list[2] = 4
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_dwyane1_label:
if minigames:
    $ renpy.block_rollback()
play sound "sound_effects/season2/fistbump.mp3"
scene ep11_brawler_story_dwyane1 with vpunch
dwy "[name]."
dwy "I spotted your nemesis here today."
scene ep11_brawler_story_dwyane2 with dissolve
mc "Spotted as in helped or saw?"
scene ep11_brawler_story_dwyane3 with dissolve
dwy "Saw. The tri-alphas don't do PTs."
dwy "He was benching at least 400 lbs, and I think he'd call it warmup."
dwy "You're seriously not gonna fight him, are you?"
scene ep11_brawler_story_dwyane4 with dissolve
menu:
    "Preparing for it":
        $ brawler_attitude += 1
        mc "I'm preparing myself for a fight. I have a feeling it could happen if our frats go head-to-head again."
        mc "And no one else in my frat would ever fight him. That's why I want to feel confident enough to kick his ass."
        scene ep11_brawler_story_dwyane3 with dissolve
        dwy "Man, you're crazy. But I've made bad calls, too. I'll let you make yours."
    "Want to defend myself":
        $ brawler_attitude -= 1
        mc "It's not so much a goal as it is self-defense. That's what fighting always was to me."
        mc "If the day comes when he comes at me, I want to be prepared to defend myself. That's all."
        scene ep11_brawler_story_dwyane3 with dissolve
        dwy "Ain't nothing wrong with that."
dwy "I thought of a kicking technique that will work great for you. To slow down any bigger opponent."
dwy "It works wonders on lesser ones, too. Want me to teach you?"
scene ep11_brawler_story_dwyane2 with dissolve
mc "I liked what you showed me last time. Sign me up."
scene ep11_brawler_story_dwyane3 with dissolve
dwy "You gotta earn it, though. I want to spar, and I'm looking at you."
scene ep11_brawler_story_dwyane4 with dissolve
mc "Sure, we can go a bout."
scene ep11_brawler_story_dwyane2 with dissolve
dwy "Prove that you're worth it."

$ renpy.pause(0.5)
$ renpy.block_rollback()
$ bn_history_list[3] = 3
if minigames:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Dwyane":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_dwyane_fight_nomg_label

label brawler_story_dwyane_after1_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_dwyane6 with dissolve
    if not minigames:
        dwy "Hm... You're getting better, but you're still not good enough."
        dwy "You gotta practice more. Let's take a break."
        jump ep11_after_spar_label
    else:
        dwy "I'm not sharing my technique with you if that's all you'll give me."
        dwy "Try it again."
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

$ bn_history_list[3] = 4
scene ep11_brawler_story_dwyane5 with dissolve
dwy "Oof."
mc "Did I hurt you?"
scene ep11_brawler_story_dwyane6 with dissolve
dwy "I swear, if you ask me if I'm tapping out again, you're outta here."
scene ep11_brawler_story_dwyane7 with dissolve
mc "I'm not. I know better by now. But still, I hit you hard with that one."
scene ep11_brawler_story_dwyane6 with dissolve
dwy "Lost my breath for a second. You faked me out good, looking up high while going low like that."
dwy "Didn't know you had that in you."
scene ep11_brawler_story_dwyane7 with dissolve
mc "I'll take that as a compliment."
mc "So... Will you show me that technique, or do you need a minute?"
scene ep11_brawler_story_dwyane8 with dissolve
if not minigames:
    dwy "Haha, cocky ass. Aight, I'll show you next time. Let's take a break."
    jump ep11_after_spar_label
else:
    dwy "Haha, cocky ass. Aight, I'll show you."

$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_tate1_label:
$ renpy.block_rollback()
scene ep11_brawler_story_tate1 with dissolve
tate "[name], I think I have improved some. I want a rematch."
tate "And don't go easy on me."
scene ep11_brawler_story_tate2 with dissolve
menu:
    "I'd never go easy on you":
        $ brawler_attitude += 1
        mc "Sparring or not, I'd never go easy on you."
        scene ep11_brawler_story_tate3 with dissolve
        tate "Damn, you really enjoy fighting, huh?"
    "I don't want to hurt you":
        $ brawler_attitude -= 1
        mc "If I give it my all, I could hurt you. I don't wanna do that."
        scene ep11_brawler_story_tate1 with dissolve
        tate "I know, and I wasn't being literal. What I meant is that I want you to put up somewhat of a challenge."
        tate "Push the limits of sparring some, and I'll be happy."

scene ep11_brawler_story_tate2 with dissolve
mc "Let's do it."

$ renpy.pause(0.5)
$ bn_history_list[4] = 3
$ renpy.block_rollback()
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Tate":
            bn_init_fight(i)
pause

label brawler_story_tate_after1_label:
$ renpy.block_rollback()
if not bn_mc_won:
    scene brawler_story_tate5 with dissolve
    chao "Interesting fight. But why did [name] let you win?"
    scene brawler_story_tate6 with dissolve
    tate "He didn't let me win!"
    scene ep11_brawler_story_tate5 with dissolve
    tate "You didn't, did you?"
    scene ep11_brawler_story_tate4 with dissolve
    chao "Hahaha!"
    scene ep11_brawler_story_tate5 with dissolve
    tate "Come at me again; I want to shut him up and show him what I can do. Please?"
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

$ bn_history_list[4] = 4
scene brawler_story_tate7 with dissolve
tate "Damn... Not again."
scene ep11_brawler_story_tate7 with dissolve
chao "You're improving."
scene ep11_brawler_story_tate8 with dissolve
mc "Thanks!"
scene brawler_story_tate5 with dissolve
chao "I was talking to Tate. He was slightly less - how should I put it? - bad at fighting this time."
scene brawler_story_tate6 with dissolve
tate "I already tapped out. There's no need to continue beating me up."
scene ep11_brawler_story_tate4 with dissolve
chao "Hahaha!"
scene ep11_brawler_story_tate6 with dissolve
mc "He likes to joke around with you. What's the deal with that?"
scene brawler_story_tate9 with dissolve
tate "I think he's intimidated by me because we're the same weight class and I'm making progress."
tate "He's a great guy, but he has a habit of busting my chops any chance he gets."
scene brawler_story_tate10 with dissolve
mc "I hope you do the same to him."
scene ep11_brawler_story_tate5 with dissolve
tate "Nah. I saw him lose one of his recent fights, and I didn't have it in me."
tate "He loves the sport so much, and I don't want to make fun of his weakest moments."
scene brawler_story_tate10 with dissolve
mc "You're a good guy."
mc "And I think you're right. You are improving."
scene brawler_story_tate9 with dissolve
tate "I know, right?"
scene brawler_story_tate10 with dissolve
mc "Maybe it's because we're sparring and holding back. I'm sure I'd have a much harder time going against you in a real fight."
scene brawler_story_tate9 with dissolve
tate "Thanks, [name]."

$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_troy1_label:
if not minigames:
    scene ep11_brawler_story_troy3 with wipeleft
else:
    $ renpy.block_rollback()
    scene ep11_brawler_story_troy3 with dissolve
$ renpy.pause()

if ep10_troy_mad:
    scene ep11_brawler_story_troy4 with dissolve
    troy "I want a rematch."
    scene ep11_brawler_story_troy5 with dissolve
    mc "Good. Let's go. Because I want to kick your ass again."
else:
    scene ep11_brawler_story_troy7 with dissolve
    troy "Got time to go a round?"
    scene ep11_brawler_story_troy6 with dissolve
    mc "Yeah, why not?"

$ renpy.pause(0.5)
if not minigames:
    jump brawler_story_troy_fight_nomg2_label
$ bn_history_list[0] = 3
$ renpy.block_rollback()
python:
    for i in range(0,len(bn_opponent_list)):
        if bn_opponent_list[i][0] == "Troy":
            bn_init_fight(i)
pause

label brawler_story_troy_after1_label:
$ renpy.block_rollback()
$ bn_quit_message = ""
if not bn_mc_won:
    if ep10_troy_mad:
        scene brawler_story_troy15 with dissolve
        troy "Fuck yes! I knew I could do it."
    else:
        scene brawler_story_troy16 with dissolve
        troy "Shit, I actually won one."
    $ renpy.pause(0.5)
    $ renpy.block_rollback()
    show screen brawler_result_screen
    pause

$ bn_history_list[0] = 4
if ep10_troy_mad:
    scene ep11_brawler_story_troy2 with dissolve
    troy "How the hell do you do that kick?"
    scene brawler_story_troy20 with dissolve
    mc "Wouldn't you like to know?"
    scene brawler_story_troy21 with dissolve
    troy "I would."
    scene brawler_story_troy20 with dissolve
    menu:
        "Share it":
            $ brawler_attitude -= 1
            mc "I'd show you if I liked you. But if you're desperate to learn it, ask Dwyane. He's the one who showed me."
            scene brawler_story_troy21 with dissolve
            troy "Alright. Thanks."
        "Piss him off":
            $ brawler_attitude += 1
            mc "Then figure it out, or I'll keep using it against you."
            scene ep11_brawler_story_troy2 with dissolve
            troy "Asshole."
else:
    scene brawler_story_troy19 with dissolve
    troy "How do you do that kick?"
    scene brawler_story_troy20 with dissolve
    menu:
        "Share it":
            $ brawler_attitude -= 1
            mc "It's good, huh? Dwyane showed me how to do it."
            scene ep11_brawler_story_troy1 with dissolve
            troy "Oh, it's one of Dwyane's kicks?"
            scene brawler_story_troy20 with dissolve
            mc "I don't think he has a patent on it. Go ahead and ask him; he's a better teacher than I am."
            scene ep11_brawler_story_troy1 with dissolve
            troy "Thanks, I'll do that."
        "Keep it a secret":
            $ brawler_attitude += 1
            mc "Sorry, but I'm not gonna share it. It's a secret."
            scene brawler_story_troy21 with dissolve
            troy "Come on. Everyone shares techniques here. That's how we improve as a group."
            scene brawler_story_troy20 with dissolve
            mc "I don't want to share it, though."
            scene brawler_story_troy21 with dissolve
            troy "Alright..."

$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_dawe0_label:
if minigames:
    $ renpy.block_rollback()
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene brawler_story_dawe1 with hpunch
dw "No way he beat you."
scene brawler_story_dawe3 with dissolve
al "Yeah, but he cheated."
scene brawler_story_dawe2 with dissolve
mc "Being better isn't cheating. And I can hear you dumbasses talking from over here."
scene brawler_story_dawe4 with dissolve
dw "Who the fuck do you think you're calling dumbass? You're a freshman!"
dw "I've taken so many more classes than you in college."
scene brawler_story_dawe5 with dissolve
mc "It doesn't count when you have to retake first-year classes every year."
scene brawler_story_dawe12 with dissolve
tate "Hahaha!"
scene brawler_story_dawe11 with dissolve
dw "What the fuck are you laughing at, blondie?"
scene brawler_story_dawe13 with dissolve
tate "Is this guy for real?"
scene brawler_story_dawe4 with dissolve
dw "You and me! Right now."
scene brawler_story_dawe5 with dissolve
mc "What do you want me to beat you at? Math, English, or human decency?"
scene brawler_story_dawe4 with dissolve
dw "I'm talking about a fight, asswipe!"
scene brawler_story_dawe7 with dissolve
mc "You're a dirty fighter. We don't do that here."
scene brawler_story_dawe8 with dissolve
dw "And you're a pussy! They don't allow women in here."
scene brawler_story_dawe14 with dissolve
tate "We do; many women practice here."
scene brawler_story_dawe9 with dissolve
dw "Are we fighting or what?"
scene brawler_story_dawe10 with dissolve
mc "As much as I want to say no just to have you put your top back on, let's do it."

$ renpy.pause(0.5)
$ renpy.block_rollback()
if minigames:
    $ bn_history_list[1] = 3
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Dawe":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_dawe_fight_nomg_label

label brawler_story_dawe_after0_label:
$ renpy.block_rollback()
$ bn_history_list[1] = 4
if not minigames:
    $ mny(2)
play sound "sound_effects/season3/kick_body.mp3"
scene brawler_story_dawe15 with vpunch
dw "Hngn!"
play sound "sound_effects/thud.mp3"
scene brawler_story_dawe16 with vpunch
al "Oh, damn! Dawe!? Are you ok?"
dw "Pro-Pro... Protein shakes?"
scene brawler_story_dawe17 with dissolve
tate "Whoa... Do you think he needs medical attention after that?"
scene brawler_story_dawe18 with dissolve
mc "I went too hard on him, didn't I?"
scene brawler_story_dawe17 with dissolve
tate "The dude is an ass, but yeah...kinda."
tate "To be fair, he didn't hold back either. But he can't fight for shit."
scene brawler_story_dawe19 with dissolve
menu:
    "No regret":
        $ brawler_attitude += 1
        scene brawler_story_dawe20 with dissolve
        mc "I hope he remembers this the next time he tries to provoke me."
        scene brawler_story_dawe21 with dissolve
        tate "No doubt he will."
    "Some regret":
        $ brawler_attitude -= 1
        scene brawler_story_dawe18 with dissolve
        mc "Yeah... I shouldn't have treated him as an equal in the ring or accepted the fight to begin with."
        mc "I lowered myself to his level."
        scene brawler_story_dawe22 with dissolve
        tate "He was asking for it, but it's good that you know there's a line between fighting as a sport and just plain fighting."

$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause

label brawler_story_dawe_after0b_label:
$ renpy.block_rollback()
scene brawler_dawe_mc_lose2 with dissolve
dw "Hahaha! I told you I'd win!"
scene brawler_dawe_mc_lose1 with dissolve
tate "Hey! What the hell? We said no dirty fighting."
scene brawler_dawe_mc_lose2 with dissolve
dw "Stop looking for an excuse. He lost! Deal with it."
scene brawler_dawe_mc_lose3 with dissolve
dw "What's that? Wanna have another round of ass whopping?"
$ renpy.pause(0.5)
$ renpy.block_rollback()
show screen brawler_result_screen
pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label scene71_2:
    r "It's open! Get in!"
    scene 71_s3 with Fade(1.0,0.5,1.0)
    play music "side_event3.mp3" fadein 2.0 loop
    mc "Looking for something?"
    r "I'm— Aha! Got it!"
    scene 71_s4 with dissolve
    mc "What's that?"
    r "It's a board game! A really, really good one."
    mc "...A board game?"
    scene 71_s5 with Dissolve(1.0)
    r "Don't tell me you've never played one before. Even commoners have games, don't they?"
    scene 71_s6 with dissolve
    mc "I have. It's just... I never expected to—Never mind. What's this about? Is it related to what you told me this this morning?"
    scene 71_s5 with dissolve
    r "Mhm. Exactly."
    r "So, [mc]. A question before we begin. On the scale of a loyal knight to a conquering warlord... where do you see yourself?"
    scene 71_s6 with dissolve
    mc "A... what now?"
    scene 71_s7 with dissolve
    r "Must I spell everything out? Do you prefer to follow or to lead? To serve or to command?"
    scene 71_s8 with dissolve
    mc "Oh, well..."
    call screen scene71_choice01 with dissolve

label scene71_choice01_op1:
    $ mc_sub = True
    mc "I'll be honest... I like it when the woman takes charge."
    scene 71_s6 with dissolve
    r "Hmmm~?"
    scene 71_s5 with dissolve
    r "I didn't take you for that type. You always seem so... stubbornly self reliant."
    scene 71_s6 with dissolve
    mc "Why not? It's nice to not be in control sometimes."
    scene 71_s9 with dissolve
    r "Interesting. This might actually complicate my plans a little."
    scene 71_s10 with dissolve
    mc "You're losing me..."
    jump scene71_3

label scene71_choice01_op2:
    $ mc_switch = True
    mc "In between. Sometimes I feel like taking charge, other times I'm happy to follow. It really depends on the mood."
    scene 71_s9 with dissolve
    r "Depends on the {i}mood{/i}, huh? I guess I can work with that."
    scene 71_s10 with dissolve
    mc "Why do you mean?"
    jump scene71_3

label scene71_choice01_op3:
    $ mc_dom = True
    mc "I like to take charge. I'm a MAN."
    scene 71_s5 with dissolve
    r "Oooh~ Is that so? This is going to be far more interesting than I anticipated then."
    scene 71_s6 with dissolve
    mc "What is?"
    jump scene71_3

label scene71_3:
    scene 71_s5 with dissolve
    r "We're going to play this game, and it will decide our fate for the entire day!"
    scene 71_s6 with dissolve
    mc "..."
    scene 71_s11 with Dissolve(1.0)
    r "Alright, alright. Let me explain. This is Realms and Runes. It's a game of puzzles and imagination."
    r "Here's the wager. If you can help me win, you get an {i}ejcaulation permit.{/i} For one whole day, you have my permission to... ejaculate anywhere you want on my body. No questions, no complaints."
    if mc_rejected_reb_first and (not persistent.scene5_p5_replay or not persistent.scene6_p5_replay):
        mc "Becky... I never even touched you before. How can you jump straight to a game with stakes like this?"
        scene 71_s5 with dissolve
        r "Then it's a perfect time to start! No better way to break the ice than a little friendly competition, right?"
        scene 71_s6 with dissolve
        mc "I don't know about this..."
        scene 71_s7 with dissolve
        r "What!? Don't you {i}want{/i} to finally do something with me? Why do you look so sad about it?"
        scene 71_s8 with dissolve
        mc "Forget it. Just... what's the penalty? What if we lose?"
        scene 71_s15 with dissolve
        r "..."
        mc "Becky?"
        scene 71_s14 with dissolve
        r "*sigh* Then you don't get your reward. Simple as that."
        r "And I might have you clean up my room while you're at it, too. Make yourself useful."
        scene 71_s15 with dissolve
        mc "Ah... now I get why you asked if I'm dominant or submissive."
        r "Mhm."
        mc "Hey... cheer up, Becky. I didn't mean to get you down. I just... I want to do this right."
        scene 71_s14 with dissolve
        r "But you're right. You never touched me before. Not like that. Even that time I outright told you to sleep with me... you found a way out."
        scene 71_s7 with dissolve
        r "You {i}will{/i} this time. One way or another, you're going to touch me. Got it?"
        scene 71_s8 with dissolve
        call screen scene71_choice02 with dissolve
        
    else:
        mc "Woah, you're actually serious?"
        r "Mhm. I told you I wanted to add some spice. I'm a woman of my word."
        mc "What if we lose?"
        scene 71_s5 with dissolve
        r "Then you don't get your reward. Simple as that."
        scene 71_s12 with dissolve
        r "And I might have you clean up my room while you're at it, too~."
        scene 71_s13 with dissolve
        mc "Ah... now I get why you asked if I'm dominant or submissive."

    if mc_dom:
        scene 71_s7 with dissolve
        r "Exactly. Since you said you like being in charge, I guess you'll have to fight extra hard to stay that way, hmm?"
        scene 71_s8 with dissolve
        mc "Don't worry. I'll win and make you mine."
        scene 71_s5 with dissolve
        r "Big words~ We'll see if you live up to them."

    elif mc_sub:
        scene 71_s7 with dissolve
        r "Exactly. But since you said you like to follow orders, I suppose losing wouldn't bother you too much, hmm?"
        scene 71_s8 with dissolve
        mc "*laughs* It doesn't work that way."

    elif mc_switch:
        scene 71_s7 with dissolve
        r "Exactly. Always ready to adapt, huh? Let's see which side of you wins today."

    scene 71_s6 with dissolve
    call screen scene71_choice02 with dissolve

label scene71_choice02_op1:
    $ mc_play_bgame = True
    mc "You're on! Let's do it!"
    scene 71_s5 with dissolve
    r "Heh~ Excellent!"
    scene 71_s6 with dissolve
    scene 71_s16 with Fade(1.0,1.0,1.0)
    r "Let me explain the basics. I don't want your character to die a tragic death in the first five minutes."
    scene 71_s17 with dissolve
    mc "Lay it on me."
    scene 71_s25 with dissolve
    r "The premise is simple. We are a group of adventurers, trapped in a... specialized dungeon. Our only goal is to escape."
    mc "So we're a team? I figured we'd be playing against each other."
    r "Not a chance. This game is notoriously difficult. It's designed for a full party, actually. You'd be completely lost without me."
    mc "I see... Wait a minute."
    scene 71_s17 with dissolve
    mc "Is this the real reason you asked me to play? You couldn't beat it alone?"
    scene 71_s19 with dissolve
    r "..."
    scene 71_s18 with dissolve
    r "...Maybe. Don't look so smug. I actually tried playing it with Maia before. I even had to buy it under her name."
    scene 71_s16 with dissolve
    r "The poor girl got the strangest looks from the court for a week straight. I felt terrible."
    scene 71_s17 with dissolve
    mc "*chuckles* I can just imagine. Didn't want everyone in the castle gossiping about their innocent princess and her... horny tastes?"
    scene 71_s18 with dissolve
    r "Shut up..."
    scene 71_s19 with dissolve
    mc "So, what happened? Why didn't you finish it with Maia?"
    scene 71_s20 with Dissolve(1.5)
    r "Well... that's the other thing. This board game. It's, um... for adults only. It's got some {i}really{/i} lewd stuff."
    r "After a few sessions, the role playing got a little too... immersive. Things became awkward, and we decided to retire the campaign."
    scene 71_s21 with dissolve
    mc "If you knew it would be awkward, why buy it in the first place?"
    scene 71_s20 with dissolve
    r "I was curious, alright? It's the same as picking up a book with a scandalous cover..."
    scene 71_s21 with dissolve
    mc "Alright, alright, I get it. No judgment here. So... should we start our new, hopefully less awkward campaign?"
    scene 71_s16 with Dissolve(1.5)
    r "Let's do it. Don't worry, I'll explain the rest as we go. It's more fun that way. And I wouldn't have to talk your ears off."
    scene 71_s22 with Dissolve(1.0)
    r "Alright, so this is me. I'm playing the Mage, specializing in... Come on, you know what a mage is specialized in. And you are the Warrior. Strong, sturdy, and the leader of the group."
    mc "What if I want to be the Necromancer instead?"
    mc "Don't be childish. The Mage-Warrior combo is a classic for a reason. We complement each other."
    r "*ahem*"
    jump scene72

label scene71_choice02_op2:
    $ mc_play_bgame = True
    $ mc_noprize_bgame = True
    mc "Becky... can we just play it normally? Without the... reward thing? I just want to play a game with you."
    if mc_rejected_reb_first and (not persistent.scene5_p5_replay or not persistent.scene6_p5_replay):
        scene 71_s14 with dissolve
        r "Figures. You still don't want to touch me."
        scene 71_s15 with dissolve
        mc "I just don't want our time together to be about winning or losing sexual favors."
        scene 71_s14 with dissolve
        r "Fine. I see how it is, [mc]. Whatever... I'd rather spend time with you than not at all."
        r "Come on, sit down."
        scene 71_s15 with dissolve
    else:
        scene 71_s7 with dissolve
        r "R-Really? I thought you'd be over the moon. I practically had to convince myself that it was fine for you to cover me in your seed."
        scene 71_s8 with dissolve
        mc "I'm flattered, really. But I don't want our time together to be about winning or losing sexual favors."
        scene 71_s7 with dissolve
        r "...*sigh* Fine. Your loss, then. Still, I'd rather spend time with you than not at all."
        r "Come on, sit down."
        scene 71_s8 with dissolve

    scene 71_s16 with Fade(1.0,1.0,1.0)
    r "Alright, just to be clear, this board game. It's, um... for adults only. It's got some {i}really{/i} lewd stuff."
    scene 71_s17 with dissolve
    mc "Adults only?! How did you even get your hands on this? Did you just stroll out into the market and buy it?"
    scene 71_s18 with dissolve
    r "Of course not! I... I had Maia buy it under her name."
    scene 71_s16 with dissolve
    r "The poor girl got the strangest looks for a week straight. I felt terrible."
    scene 71_s17 with dissolve
    mc "*chuckles* I can just imagine. Didn't want everyone in the castle gossiping about their innocent princess and her... horny tastes?"
    scene 71_s18 with dissolve
    r "Shut up..."
    scene 71_s19 with dissolve
    mc "So, what happened? Did you play it with Maia?"
    scene 71_s20 with Dissolve(1.5)
    r "After a few sessions, the role playing got a little too... immersive. Things became awkward, and we decided to retire the campaign."
    scene 71_s21 with dissolve
    mc "If you knew it would be awkward, why buy it in the first place?"
    scene 71_s20 with dissolve
    r "I was curious, alright? It's the same as picking up a book with a scandalous cover..."
    scene 71_s21 with dissolve
    mc "Alright, alright, I get it. No judgment here. So... should we start our new, hopefully less awkward campaign?"
    scene 71_s16 with Dissolve(1.5)
    r "Let's do it. The premise is simple. We are a group of adventurers, trapped in a dungeon. Our only goal is to escape."
    scene 71_s17 with dissolve
    mc "So we're a team? I figured we'd be playing against each other."
    scene 71_s16 with dissolve
    r "Not a chance. This game is notoriously difficult. It's designed for a full party, actually. You'd be completely lost without me."
    scene 71_s17 with dissolve
    mc "I see."
    scene 71_s22 with Dissolve(1.0)
    r "Alright, so this is me. I'm playing the Mage, specializing in... Come on, you know what a mage is specialized in. And you're the Warrior. Strong, sturdy, and the leader of the group."
    mc "What if I want to be a necromancer instead?"
    mc "Don't be childish. The Mage-Warrior combo is a classic for a reason. We complement each other."
    r "I'll explain the rest as we go. It's more fun that way. And I wouldn't have to talk your ears off."
    r "*ahem*"
    jump scene72

label scene71_choice02_op3:
    $ mc_playnot_bgame = True
    mc "Becky... I don't want to play."
    if mc_rejected_reb_first and (not persistent.scene5_p5_replay or not persistent.scene6_p5_replay):
        $ mc_reb_breakup = True
        scene 71_s14 with Dissolve(1.0)
        stop music fadeout 2.0 
        r "...Do you even like me, [mc]?"
        r "You've been avoiding me like I'm some... some disgusting creature you can't stand to be near!"
        scene 71_s15 with dissolve
        mc "Becky, that's not— Let's just talk, okay? How was your day?"
        scene 71_s14 with dissolve
        r "Screw you."
        scene 71_s15 with dissolve
        mc "What?"
        scene 71_s14 with dissolve
        r "Get out."
        scene 71_s15 with dissolve
        mc "Becky, just—"
        scene 71_s14 with vpunch
        r "GET OUT!"
        scene 71_s15 with dissolve
        mc "..."
        scene black with Fade(1.0,1.0,1.0)
        perception "You turn slowly and walk to the door. You take one last glance back. She isn't looking at you. Her head is bowed, her shoulders shaking with silent, angry sobs she is too proud to let you hear."
        jump scene74

    else: 
        scene 71_s7 with dissolve
        r "W-What!? Why? I spent all morning planning this!"
        scene 71_s8 with dissolve
        mc "I believe you. And I'm flattered, really. I just don't want our time together to be about winning or losing sexual favors."
        scene 71_s14 with dissolve
        r "Ugh! And I was so excited... Do you even like me?"
        scene 71_s15 with dissolve
        mc "Huh? Where did that come from? Of course I do."
        scene 71_s14 with dissolve
        r "Then why are you avoiding doing things with me? It feels like you're always holding back."
        scene 71_s15 with dissolve
        mc "I'm not holding back. Maybe I just want us to have a normal, healthy relationship sometimes."
        scene 71_s14 with dissolve
        r "But... my way is more fun."
        scene 71_s15 with dissolve
        mc "Let's just talk. How was your day? What's the latest gossip? I'm out of the loop."
        scene 71_s7 with dissolve
        r "Talk? About my day? You sound like my old, stuffy etiquette tutor. Is this your secret fetish? Mundanity?"
        scene 71_s8 with dissolve
        mc "Humor me. Any city secret or potential assassination plot?"
        scene 71_s7 with dissolve
        r "Ugh, fiiine."
        stop music fadeout 2.0 
        scene 71_s8 with dissolve
        scene 71_s26 with Fade(1.0,1.0,1.0)
        play music "reb.mp3" fadein 2.0 loop
        r "Let's see... A new cook tried a new recipe for lemon tarts. They were so sour Avery's eye twitched for an hour, but she was too polite to say anything. It was hilarious."
        scene 71_s27 with dissolve
        mc "*chuckles* See? That's a good start."
        scene 71_s29 with Dissolve(1.0)
        r "Okay, your turn. What's something boring that happened to you?"
        scene 71_s28 with dissolve
        mc "Ran into Captain Alice today. She cornered me and asked me to train a new recruit."
        scene 71_s30 with dissolve
        r "{i}You?{/i} Why you? Don't they have seasoned sergeants for that?"
        scene 71_s31 with dissolve
        mc "My thoughts exactly. She said the usual trainers were tied up with other duties."
        scene 71_s29 with dissolve
        r "I doubt that was all there was to it. Alice doesn't do anything without three layers of calculation. She must have chosen you specifically."
        scene 71_s32 with dissolve
        r "Is there something you're not telling me, [mc]?"
        scene 71_s33 with dissolve
        mc "Huh? No, it's not like that... I guess it's just because I've been reliable to your mother a few times now. My name probably came up."
        scene 71_s29 with dissolve
        r "Hmm, maybe. So, what did you say? Don't leave me in suspense."
        scene 71_s28 with dissolve

        if mc_accept_joan:
            mc "I told her I'd do it. Seemed like the right thing to do. I sent the recruit home for the day, though. She looked like a startled deer. No sense in breaking her on the first day."
            scene 71_s30 with dissolve
            r "Well, aren't you a gentle instructor?"
            scene 71_s29 with dissolve
            r "Just remember. That {i}startled deer{/i} will be facing monsters. If she dies because you went too easy on her, I doubt you'd sleep well with that on your conscience."
            scene 71_s28 with dissolve
            mc "I get that. It's a heavy responsibility."
            scene 71_s32 with dissolve
            r "And you better not have agreed to train her just because she's a girl."
            scene 71_s33 with dissolve
            mc "Uhh... Of course not."
        else:
            mc "I told her to find someone else. I'm not ready for that kind of responsibility. One wrong move, and it's someone's life on the line."
            scene 71_s28 with dissolve
            r "Hmm... Probably for the best."
            scene 71_s29 with dissolve
            r "If that recruit had gotten hurt due to your inexperience, that's a ghost that would haunt your halls. I doubt you'd sleep well with that on your conscience."
            scene 71_s32 with dissolve
            r "And you better not have agreed to train her just because she's a girl."
            scene 71_s33 with dissolve
            mc "Uhh... Of course not."

        mc "What else is going on with you?"
        scene 71_s29 with dissolve
        r "Not much, really. I haven't set foot outside the castle grounds in a while, if you remember. I'm just... waiting. Waiting for my mother to return so I can finally breathe again and leave."
        scene 71_s28 with dissolve
        mc "Why not just... you know. Sneak out?"
        scene 71_s35 with Dissolve(1.5)
        r "..."
        scene 71_s34 with dissolve
        r "I... I don't know. I guess I'm afraid of being seen. My 'relationship' with the maids and guards isn't exactly... warm."
        r "They tolerate me because they have to. I'm pretty sure half of them would sell me out to my aunt for an extra day off."
        scene 71_s35 with dissolve
        mc "I see. So, where did you used to go? When you did manage to get out. What's your spot?"
        scene 71_s34 with dissolve
        r "There's an old, forgotten garden on the western cliffside. It's all overgrown and wild. The view of the sunset from there... I can't really describe it with words. It wouldn't do it justice."
        scene 71_s29 with dissolve
        r "Why? Are you offering to be my accomplice?"
        scene 71_s28 with dissolve
        mc "Maybe."
        r "..."
        scene 71_s29 with dissolve
        r "If my mother isn't back in the next few days... I don't think I can stand being caged in here any longer. I'll {i}have{/i} to get out."
        r "Anyway, I barely slept a wink last night. I was up thinking about playing Realms and Runes with you."
        scene 71_s28 with dissolve
        mc "The game isn't going anywhere. For now, your royal decree is to take a nap."
        r "Mhm."
        scene 71_s29 with dissolve
        r "You'll... stay with me? Right? Until I fall asleep?"
        r "I'm thinking of sleeping naked today. What do you think~?"
        scene 71_s28 with dissolve
        call screen scene72_choice07 with dissolve
        mc "*chuckles* I'm not going anywhere."
        scene black with Fade(1.0,1.0,1.0)
        stop music fadeout 2.0 
        perception "You lie down on the bed beside Rebecca. The silence between you is comfortable, and you stay, listening to her breathing even out and soften, until you're certain she's asleep."
        jump scene74
        
label scene72:
    $ in_free_roam = True
    $ free_roam_arrows = True
    scene 71_s23 with Dissolve(1.5)
    dm "You and your fellow adventurer materialize on the highest tier of the dungeon. With a thunderous CLANG, the door behind you seals shut, severing your retreat."
    r "What are you doing?"
    scene 71_s24 with dissolve
    stop music fadeout 2.0 
    mc "Imagining it. Continue."
    scene 71_s23 with dissolve
    r "Alright..."
    play music "echoes_of_sorrow.mp3" fadein 2.0 volume 0.5 loop
    scene 72_d2 with Dissolve(1.5)
    dm "*ahem* Before you, a grand gate stands, firmly locked. To your left and right, two identical, dark hallways stretch into the darkness, pulsing with a strange, warm energy. The choice of where to begin... is yours."
    mc "Great voice acting, Becky. You're a natural at this."
    dm "Thank you. Suddenly the air begins vibrating and a deep ancient voice echoes from the stone itself: 'ACTIVATE THE FIVE SHRINES... IF YOU DARE TO ADVANCE FURTHER INTO MY DEPTHS.'"
    scene 72_d3 with Dissolve(1.0)
    mc "Alright, activate the shrines. Sounds simple enough."
    mc "Hmm. What's your read on this, Becky? You're the expert."
    r "I'm not sure. Both hallways look identical on the map. The first move is all yours my brave warrior."
    if persistent.skip_mini:
        "Mini-Game Skipped"
        jump rnr_win
    else:
        call rnr_reset from _call_rnr_reset
    $ in_rnr_1 = True

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen s72_dMAIN with dissolve


label s72_dMAIN_note:
    r "The door is closed, we still have [rnr_shrines_all] shrines to activate."
    call screen s72_dMAIN with dissolve

####################################
####################################
####################################
default rnr_win = False
default rnr_shrines = 0
default rnr_shrines_all = 5
default reb_board_game_lore = False
default reb_board_game_lore2 = False
default reb_board_game_lore_chest = False
default rnr_health = 20
default rnr_bracers = False
default rnr_wand = False
default rnr_defeat_witch = False

default rnr_potion1 = False
default rnr_potion2 = False
default rnr_potion3 = False

default rnr_rune1 = False
default rnr_rune2 = False
default rnr_rune3 = False
default rnr_rune4 = False

default rnr_rune1_used = False
default rnr_rune2_used = False

default rnr_cat_key = False
default rnr_met_cat = False
default rnr_cat_free = False
default rnr_cheese = False

default rnr_met_groblin = False
default rnr_diamond = False

default rnr_met_sphere = False
default rnr_coin = False

default rnr_free_tenta = False
default rnr_shrine_goblin = False
default rnr_shrine_werewolf = False
default rnr_shrine_spider = False

default rnr_in_fight = False
default rnr_secondlife = False
default rnr_wrong_choices = True
####################################
####################################
####################################
#MAP
default in_rnr_1 = False
default in_rnr_2 = False
default in_rnr_3 = False
default in_rnr_4 = False
default in_rnr_5 = False
default in_rnr_6 = False
default in_rnr_7 = False
default in_rnr_8 = False
default in_rnr_9 = False
default in_rnr_10 = False
default in_rnr_11 = False
default in_rnr_12 = False
default in_rnr_13 = False
default in_rnr_14 = False
default in_rnr_15 = False
default in_rnr_16 = False
default in_rnr_17 = False
default in_rnr_18 = False
default in_rnr_19 = False
default in_rnr_20 = False
default in_rnr_21 = False
default in_rnr_22 = False
default in_rnr_23 = False
default in_rnr_24 = False

label rnr_reset:
    $ in_rnr_1 = False
    $ in_rnr_2 = False
    $ in_rnr_3 = False
    $ in_rnr_4 = False
    $ in_rnr_5 = False
    $ in_rnr_6 = False
    $ in_rnr_7 = False
    $ in_rnr_8 = False
    $ in_rnr_9 = False
    $ in_rnr_10 = False
    $ in_rnr_11 = False
    $ in_rnr_12 = False
    $ in_rnr_13 = False
    $ in_rnr_14 = False
    $ in_rnr_15 = False
    $ in_rnr_16 = False
    $ in_rnr_17 = False
    $ in_rnr_18 = False
    $ in_rnr_19 = False
    $ in_rnr_20 = False
    $ in_rnr_21 = False
    $ in_rnr_22 = False
    $ in_rnr_23 = False
    $ in_rnr_24 = False
    return

label s72_dMAIN:
    call rnr_reset from _call_rnr_reset_1
    $ in_rnr_1 = True
    if rnr_shrines == 5:
        scene 72_d30 with dissolve
        dm "You return to the grand chamber where you first began. The massive central shrine, once inert, is now thrumming with power, its eyes blazing with a green light."
        scene black with dissolve
        dm "The stone door behind it lifts, revealing an impenetrable darkness. You step inside. Immediately, a wave of overwhelming magical energy washes over you. Your vision turns to black. Your limbs grow heavy and—"
        stop music fadeout 2.0 
        jump rnr_win
    else:
        scene 72_d3 with dissolve
        call screen s72_dMAIN with dissolve

label s72_dRIGHT:
    call rnr_reset from _call_rnr_reset_2
    $ in_rnr_14 = True
    scene 72_d18 with dissolve
    if not reb_board_game_lore:
        $ reb_board_game_lore = True
        r "Fun fact for you, this dungeon we're crawling through? It's based on a real one."
        mc "You serious?"
        scene 71_s16 with dissolve
        r "Mhm. The 'Silent Sepulcher.' It was discovered centuries ago, carved into the northern mountains. To this day, no one knows who built it, or why."
        scene 71_s17 with dissolve
        mc "Must be some long-gone empire, then. Places like that... they're usually tombs for forgotten kings or temples for dead Gods. Something to do with religion or the afterlife."
        scene 71_s16 with dissolve
        r "Religious reasons? Maybe. But what we're doing right now, is basically retracing the steps of the very first adventurers who mapped it out. We're following their journal entries."
        scene 71_s17 with dissolve
        mc "Huh. So we're reliving history." 
        scene 71_s16 with dissolve
        r "Well... not truly. Let's just say the original explorers didn't report any lewd things or talking statues. The writers took some... creative liberties to make the retelling more interesting."
        scene 71_s17 with dissolve
        scene 72_d18 with Dissolve(1.5)
        call screen s72_dRIGHT with dissolve
    else:
        call screen s72_dRIGHT with dissolve

label s72_dLEFT:
    call rnr_reset from _call_rnr_reset_3
    $ in_rnr_2 = True
    scene 72_d4 with dissolve
    if not reb_board_game_lore:
        $ reb_board_game_lore = True
        r "Fun fact for you, this dungeon we're crawling through? It's based on a real one."
        mc "You serious?"
        scene 71_s16 with dissolve
        r "Mhm. The 'Silent Sepulcher.' It was discovered centuries ago, carved into the northern mountains. To this day, no one knows who built it, or why."
        scene 71_s17 with dissolve
        mc "Must be some long-gone empire, then."
        mc "Places like that... they're usually tombs for kings or temples for dead Gods. Something to do with religion or the afterlife."
        scene 71_s16 with dissolve
        r "Religious reasons? Maybe. But what we're doing right now, is basically retracing the steps of the very first adventurers who mapped it out. We're following their journal entries."
        scene 71_s17 with dissolve
        mc "Huh. So we're reliving history." 
        scene 71_s16 with dissolve
        r "Well... not truly. Let's just say the original explorers didn't report any lewd things or talking statues."
        r "The writers took some... creative liberties to make the retelling more interesting."
        scene 71_s17 with dissolve
        scene 72_d4 with Dissolve(1.5)
        call screen s72_dLEFT with dissolve
    else:
        call screen s72_dLEFT with dissolve

label s72_dLEFT_LEFT:
    call rnr_reset from _call_rnr_reset_4
    $ in_rnr_3 = True
    scene 72_d5 with dissolve
    if not reb_board_game_lore2:
        $ reb_board_game_lore2 = True
        r "There are two chambers here. Should we explore them?"
        call screen s72_dLEFT_LEFT with dissolve
    else:
        call screen s72_dLEFT_LEFT with dissolve

default s72_dLEFT_LEFT_LEFT_chest = True
default s72_dLEFT_LEFT_LEFT_chest_first = True
label s72_dLEFT_LEFT_LEFT:
    call rnr_reset from _call_rnr_reset_5
    $ in_rnr_4 = True
    if s72_dLEFT_LEFT_LEFT_chest:
        scene 72_d6 with dissolve
        if s72_dLEFT_LEFT_LEFT_chest_first:
            $ s72_dLEFT_LEFT_LEFT_chest_first = False
            r "Looks like there's a chest here."
    else:
        scene 72_d7 with dissolve
    call screen s72_dLEFT_LEFT_LEFT with dissolve

label s72_dLEFT_LEFT_LEFT_chest:
    $ s72_dLEFT_LEFT_LEFT_chest = False
    dm "Sitting in the corner is an oak chest. It's covered in a thick layer of dust, and its iron latch appears to be unlocked."
    if not reb_board_game_lore_chest:
        $ reb_board_game_lore_chest = True
        mc "Let's crack it open."
        r "Hold on, brute force isn't always best. I can attempt a minor blessing of fortune on it. It might... persuade the chest to offer up its best treasures."
        mc "You can do that?"
        r "I'm a mage, remember?"
        r "If I roll well, we get better loot. If I fail... the magic could backfire, and we might get nothing. Or worse."
    else:
        r "Should I roll it?"
    call screen scene72_choice01 with dissolve

default dice_number = 0
label scene72_choice01_op1:
    perception "Rebecca rolls the dice..."
    $ dice_number = random.randint(1, 6)
    $ renpy.random.seed()
    perception "The dice lands on [dice_number]!"  
    if dice_number > 3:
        $ rnr_bracers = True
        $ rnr_potion1 = True
        $ rnr_health += 5
        r "Yes! The weave of fortune favors us!"
        dm "A golden light shimmers over the chest. With a gentle, inviting click, the lid rises on its own, as if welcoming you."
        dm "Inside, nestled on velvet, are two items: a small potion of healing and a masturfully crafted bronze bracers. The Warrior's max vitality has increased to 25!"
        scene 72_d7 with dissolve
        mc "Nice work, Becky."
    elif dice_number <= 3:
        r "Oh, no..."
        scene 72_d7 with vpunch
        dm "A sickly green aura envelops the chest. It begins to quiver violently, its wood groaning and splintering before your eyes."
        dm "The entire chest collapses in on itself, disintegrating into a pile of worthless, charred splinters and dust."
        mc "Shit... There goes our loot."
        r "Sorry..."
    call screen s72_dLEFT_LEFT_LEFT with dissolve

label scene72_choice01_op2:
    $ rnr_potion1 = True
    mc "Let's just loot it."
    dm "Inside, nestled on velvet, is a single small potion of healing."
    scene 72_d7 with dissolve
    mc "Alright, this might help us later on."
    call screen s72_dLEFT_LEFT_LEFT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT:
    call rnr_reset from _call_rnr_reset_6
    $ in_rnr_5 = True
    scene 72_d8 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT:
    call rnr_reset from _call_rnr_reset_7
    $ in_rnr_6 = True
    scene 72_d9 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT

default s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest = True

label s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT:
    call rnr_reset from _call_rnr_reset_8
    $ in_rnr_7 = True
    if s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest:
        scene 72_d10 with dissolve
    else:
        scene 72_d11 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest:
    $ s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest = False
    if not reb_board_game_lore_chest:
        $ reb_board_game_lore_chest = True
        mc "A chest! Let's crack it open."
        r "Hold on, brute force isn't always best. I can attempt a minor blessing of fortune on it. It might... persuade the chest to offer up its best treasures."
        mc "You can do that?"
        r "I'm a mage, remember?"
        r "If I roll well, we get better loot. If I fail... the magic could backfire, and we might get nothing. Or worse."
    else:
        dm "You find another wooden chest. This one is made of darker wood, bound with rusted iron."
        mc "Another one!"
        r "Should I try the blessing? Fortune favors the bold, right?"
    call screen scene72_choice02 with dissolve

label scene72_choice02_op1:
    perception "Rebecca rolls the dice..."
    $ dice_number = random.randint(1, 6)
    $ renpy.random.seed()
    perception "The dice lands on [dice_number]!"  
    if dice_number > 3:
        $ rnr_wand = True
        if not rnr_potion1:
            $ rnr_potion1 = True
        else:
            $ rnr_potion2 = True
        $ rnr_health += 5
        r "Success!"
        dm "The chest seems to purr with pleasure. It emits a low, satisfied groan, the lid lifting slowly and sensually to reveal its contents."
        dm "Inside, you find another potion of healing and a slender, elegant wand carved from obsidian."
        mc "A wand? I'd probably just break it. This is all you, mage."
        r "Yay~!"
        if rnr_bracers:
            r "With your new bracers and my wand, our max vitality should be 30!"
        else:
            r "With my new wand, our max vitality should be 25!"
        scene 72_d11 with dissolve
        mc "Nice work, Becky."
        
    elif dice_number <= 3:
        r "...Oh, you have got to be kidding me."
        scene 72_d11 with vpunch
        dm "The magical energy surges uncontrollably! The chest doesn't just collapse. It transforms. The wood warps and reshapes, the iron bindings melting like wax. In a matter of seconds, the chest is gone."
        r "Dammit... Luck isn't on my side today."
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT with dissolve

label scene72_choice02_op2:
    if not rnr_potion1:
        $ rnr_potion1 = True
    else:
        $ rnr_potion2 = True
    mc "Let's just loot it."
    dm "Inside, nestled on velvet, is a single small potion of healing."
    scene 72_d11 with dissolve
    mc "This dungeon is pretty generous."
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP:
    call rnr_reset from _call_rnr_reset_9
    $ in_rnr_8 = True
    scene 72_d12 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT:
    call rnr_reset from _call_rnr_reset_10
    $ in_rnr_9 = True
    scene 72_d13 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve

default s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster = True
label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP:
    call rnr_reset from _call_rnr_reset_11
    $ in_rnr_10 = True
    if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster:
        scene 72_d14_poster with dissolve
    else:
        scene 72_d14 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster:
    $ persistent.alex_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster = False
    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP:
    call rnr_reset from _call_rnr_reset_12
    $ in_rnr_11 = True
    scene 72_d15 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT:
    call rnr_reset from _call_rnr_reset_13
    $ in_rnr_12 = True
    scene 72_d16 with dissolve
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_UP:
    call rnr_reset from _call_rnr_reset_14
    $ in_rnr_13 = True
    scene 72_d17 with dissolve
    mc "Looks like a deadend."
    r "You're right. Should we go back to the main room? We can instantly go there if we jump in the water."
    call screen scene72_choice04 with dissolve

    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_UP with dissolve

default rnr_cat_first = True
label s72_dLEFT_LEFT_cat:
    if not rnr_cat_free:
        scene s72_cat1 with dissolve
        if rnr_cat_first:
            $ rnr_cat_first = False
            dm "You push open the door to the chamber. Hanging from a rusted chain in the center of the room is a sturdy iron cage. Inside, a black and white cat sits perfectly still, its eyes fixed on you with an unnerving, unblinking intensity."
            mc "The hell? What kind of monster cages a cat?!"
            scene s72_cat2 with dissolve
            r "Who knows? Might be there for a reason."
            mc "Seriously? It's a cat, Becky."
            r "...Alright, fine. Maybe you're right."
            if rnr_cat_key:
                $ rnr_cat_free = True
                $ rnr_cheese = True
                mc "Good thing we already have a key. Let's see if this fits."
                scene s72_cat3 with vpunch
                dm "You insert the key into the cage's lock and as soon as the cage opens, the cat bolts. It darts between your legs, and vanishes into the corridor without a backward glance."
                dm "Left behind in the spot where it sat is a small wedge of hard cheese."
                mc "You're welcome, I guess."
                if rnr_met_groblin:
                    r "The cheese! That little Groplin is going to be so excited."
                else:
                    r "...Cheese? We risked a potential demon cat for a snack?"
                    mc "Yeah, not the most glamorous treasure. I'm sure we'll find a use for it. Maybe there's a rat we need to bribe."
                jump s72_dLEFT_LEFT

            else:
                mc "We don't have a key, right?"
                r "Mhm. Let's make a note of this. The poor thing will have to hold on a little longer."
                call screen s72_dLEFT_LEFT_cat with dissolve
        else:
            if rnr_cat_key:
                scene s72_cat2 with dissolve
                $ rnr_cat_free = True
                $ rnr_cheese = True
                mc "We found a key. Let's see if it fits."
                scene s72_cat3 with vpunch
                dm "You insert the key into the cage's lock and as soon as the cage opens, the cat bolts. It darts between your legs, and vanishes into the corridor without a backward glance."
                dm "Left behind in the spot where it sat is a small wedge of hard cheese."
                mc "You're welcome, I guess."
                if rnr_met_groblin:
                    r "The cheese! That little Groplin is going to be so excited."
                else:
                    r "...Cheese? We risked a potential demon cat for a snack?"
                    mc "Yeah, not the most glamorous treasure. I'm sure we'll find a use for it. Maybe there's a rat we need to bribe."
                jump s72_dLEFT_LEFT

            else:
                scene s72_cat2 with dissolve
                r "We're still missing the key..."
                call screen s72_dLEFT_LEFT_cat with dissolve
    else:
        r "We already freed the cat that was there."
        call screen s72_dLEFT_LEFT with dissolve

default s72_dLEFT_LEFT_shrine_first = True
label s72_dLEFT_LEFT_shrine:
    if not rnr_shrine_goblin:
        if s72_dLEFT_LEFT_shrine_first:
            $ s72_dLEFT_LEFT_shrine_first = False
            scene s72_shrine1_1 with dissolve
            dm "A shrine stands before you, but blocking the path is a lone goblin clutching a rusty dagger."
            mc "D-Does the goblin have a penis?"
            r "Uhh... no? Nothing here says that..."
            mc "Great. Just checking."
            r "Ahuh..."
            r "Anyway, we'll need to win this fight to activate the shrine."
            mc "Got it."
        else:
            scene s72_shrine1_1 with dissolve
        call screen s72_dLEFT_LEFT_shrine with dissolve
    else:
        r "We already activated the shrine that was there."
        call screen s72_dLEFT_LEFT with dissolve

default rnr_shrine_fight_info = False
default scene72_rnr_shrine1_op1 = False
default scene72_rnr_shrine1_op2 = False
default scene72_rnr_shrine1_op3 = False
label s72_dLEFT_LEFT_shrine_fight:
    $ rnr_in_fight = True
    play music "battle02.mp3" fadein 2.0 loop
    scene s72_shrine1_2 with vpunch
    dm "The goblin, tired of waiting, lets out a pathetic snarl and charges at you in a wobbly, unsteady run!"
    r "Alright, warrior. What's your move?"
    if not rnr_shrine_fight_info:
        $ rnr_shrine_fight_info = True
        mc "My move?"
        r "You need to predict the correct action that the original adventures made when they fought this monster."
        call screen s72_dLEFT_LEFT_shrine_fight with dissolve
    else:
        call screen s72_dLEFT_LEFT_shrine_fight with dissolve

label scene72_rnr_shrine1_op1:
    $ scene72_rnr_shrine1_op1 = True
    $ rnr_health -= 3
    dm "The Warrior attempt to do a wide theatrical swing but the axe accedintly slips from his fingers. The goblin, untouched, skids to a halt and pokes you in the thigh with its rusty dagger."
    dm "The Warrior's vitality decreases by 3!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dLEFT_LEFT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dLEFT_LEFT_shrine_fight with dissolve

label scene72_rnr_shrine1_op2:
    $ scene72_rnr_shrine1_op2 = True
    $ rnr_health -= 3
    mc "Hold on! I try to reason with it. 'We don't have to do this, little guy! We can get out of here together!'"
    r "You're trying to... negotiate... with a goblin?"
    dm "The goblin seizes the opportunity, leaps forward, and bites you hard on the hand before scrambling away."
    dm "The Warrior's vitality decreases by 3!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dLEFT_LEFT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dLEFT_LEFT_shrine_fight with dissolve

label scene72_rnr_shrine1_op3:
    $ rnr_in_fight = False
    $ rnr_wrong_choices = True
    $ rnr_shrine_goblin = True
    $ rnr_shrines += 1
    $ rnr_shrines_all -= 1
    mc "I plant my feet and bring my axe down in a clean, vertical chop right as he gets in range."
    play sound "sound_effects/unsheathe.mp3"
    scene s72_shrine1_3 with vpunch
    dm "You split the goblin's cranium in half with a single swing. He mutters something about your mother before he dissolves into dust."
    mc "Don't talk about my moms, yo."
    r "Was a bastard to the very end."
    stop music fadeout 2.0 
    play sound "sound_effects/rnr/rnr_activate.mp3"
    scene s72_shrine1_4 with dissolve
    dm "The shrine's eyes turn green, a testament to your victory."
    if rnr_shrines == 5:
        mc "Alright, I think this is it, right? All shrine?"
        r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    else:
        mc "We did it!"
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    jump s72_dLEFT_LEFT

default s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_first = True
label s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine:
    if not rnr_shrine_werewolf:
        if s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_first:
            $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_first = False
            scene s72_shrine2_1 with dissolve
            dm "You push open the door and enter the chamber. Standing between you and the shrine, his massive, fur-covered back to you, is a werewolf. He seems to be gently stroking the shrine's surface, almost... affectionately."
            mc "A werewolf?! Shit... I've had enough of these things for one lifetime."
            r "It hasn't noticed us yet. We could try to sneak away, come back when we're stronger."
        else:
            scene s72_shrine2_1 with dissolve
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine with dissolve
    else:
        r "We already activated the shrine that was there."
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve

label s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight:
    $ rnr_in_fight = True
    scene s72_shrine2_2 with dissolve
    play music "battle02.mp3" fadein 2.0 loop
    dm "The werewolf's head whips around. Yellow eyes lock onto you, and a string of thick saliva drips from his fangs. A low, rumbling voice emerges from his maw."
    werewolf "Ahh... Fresh meat. It's been so long since I've had visitors."
    r "What's our move?"
    if not rnr_shrine_fight_info:
        $ rnr_shrine_fight_info = True
        mc "My move?"
        r "You need to predict the correct action that the original adventures made when they fought this monster."
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight with dissolve

default scene72_rnr_shrine2_op1 = False
default scene72_rnr_shrine2_op2 = False
default scene72_rnr_shrine2_op3 = False

label scene72_rnr_shrine2_op3:
    $ scene72_rnr_shrine2_op3 = True
    $ rnr_health -= 4
    mc "I go for a full-power, spinning slash to its chest!"
    dm "You put everything into a dramatic spin. The werewolf easily ducks under it, and you end up off-balance and dizzy. It swats you into a wall."
    dm "The Warrior's vitality decreases by 4!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight with dissolve

label scene72_rnr_shrine2_op2:
    $ scene72_rnr_shrine2_op2 = True
    $ rnr_health -= 4
    mc "I go low! Try to sweep its legs out from under it!"
    r "Your axe sweeps toward its ankles. The werewolf simply leaps over it, lands on you, and gives you a lick with its slobbery tongue before kicking you away."
    dm "The Warrior's vitality decreases by 4!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight with dissolve

label scene72_rnr_shrine2_op1:
    $ rnr_in_fight = False
    $ rnr_wrong_choices = True
    $ rnr_shrine_werewolf = True
    $ rnr_shrines += 1
    $ rnr_shrines_all -= 1
    mc "Flank him, Becky! I try to keep him busy."
    play sound "sound_effects/slash03.mp3"
    scene s72_shrine2_3 with vpunch
    dm "Your axe bites deep into the werewolf's shoulder, and as it reels back, howling in pain, the Mage seizes the opening. A fireball shoots from her wand, striking the beast in his back."
    play sound "sound_effects/bodydrop.mp3"
    scene s72_shrine2_4 with dissolve
    dm "Its body seizes violently, fur smoking, before it collapses to the stone floor, unmoving."
    mc "Nice work."
    r "Phew... For a second there, I thought we were going to be his next meal."
    play sound "sound_effects/rnr/rnr_activate.mp3"
    stop music fadeout 2.0 
    scene s72_shrine1_4 with dissolve
    dm "As the werewolf's life fades, the shrine behind him flares with a brilliant, emerald green light. A low chime echoes through the room. The trial has been passed."
    if rnr_shrines == 5:
        mc "Alright, I think this is it, right? All shrine?"
        r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    else:
        mc "One down. [rnr_shrines_all] more of these things to go."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT

image s72_tenta_anim1 = Movie(play="images/4_chapter3/scene72/s72_tenta/s72_tenta_anim1.webm", loop=True)
image s72_tenta_anim2 = Movie(play="images/4_chapter3/scene72/s72_tenta/s72_tenta_anim2.webm", loop=True)

default s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta_first = True
default rnr_mc_fell_tenta = False
label s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p6_replay:
        $ persistent.scene3_p6_replay = True
        
    if s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta_first and not rnr_free_tenta:
        stop music fadeout 2.0 
        $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta_first = False
        scene s72_tenta_1 with dissolve
        dm "You push open the door and step into a chamber that is no longer a room of stone, but a living, pulsating cavity. The walls and ceiling are encased in membranous flesh, breathing slowly."
        mc "What the hell is this?!"
        show s72_tenta_anim2 with dissolve
        dm "From the fleshy walls, slick tentacles emerge, each one devoted to a different woman lying in a state of blissful ectacy. The tentacles caress and penetrate whatever hole it finds."
        show s72_tenta_anim1 with dissolve
        hide s72_tenta_anim2
        dm "Your eyes are drawn to one woman in particular. Her belly is swollen tight. With each deep thrust of the tentacle down her throat, a jet of milk spurts from her engorged breasts."
        scene s72_tenta_3 with dissolve
        dm "It is impossible to tell if she is with child or simply filled to bursting with the creature's strange essence."
        scene s72_tenta_5 with dissolve
        mc "Can we... help them?"
        scene s72_tenta_6 with dissolve
        r "The question is, {i}should{/i} we? They look... content. But we can try."
        scene s72_tenta_1 with dissolve
        if not reb_board_game_lore_chest:
            $ reb_board_game_lore_chest = True
            r "Do you want to roll the dice?"
            mc "How does this work?"
            r "It's simple. This is a six sided die. If you roll a three or higher, your action succeeds. If you roll a one or a two... Prepare for consequences."
        else:
            r "Do you want to roll the dice?"
        call screen scene72_choice03 with dissolve
    elif not s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta_first and rnr_free_tenta:
        r "That's the room where these girls were... It's better if we leave them alone. They didn't appreciate your help."
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve
    elif rnr_mc_fell_tenta:
        r "*laughs* Didn't you get embarrassed enough? It's better if we leave them alone."
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve
    else:
        r "That's the room where these girls were... It's better if we leave them alone."
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve

label scene72_choice03_op1:
    perception "You roll the dice..."
    $ dice_number = random.randint(1, 6)
    $ renpy.random.seed()
    perception "The dice lands on [dice_number]!"  
    if dice_number > 3:
        $ rnr_free_tenta = True
        play sound "sound_effects/unsheathe.mp3"
        scene s72_tenta_7 with vpunch
        dm "With a roar of righteous fury, your warrior brings his axe down in a sweeping arc! The blade severs the slick tentacles with clean, wet thwips. They recoil into the walls, which shudder in pain."
        mc "Alright!"
        scene s72_tenta_8 with dissolve
        dm "The women slowly, unsteadily, rise to their feet. Their movements are jerky, like puppets with cut strings. Their faces are not filled with gratitude, but with a vacant, confused loss."
        rnr_girl1 "What... what happened? The music... the warmth... it's gone."
        mc "I saved you. You're free. No need to thank me."
        scene s72_tenta_9 with dissolve
        rnr_girl1 "You... you hurt him?"
        mc "Hurt... him? You mean that... thing?!"
        scene s72_tenta_10 with dissolve
        rnr_girl2 "What do we do now? He was our only comfort in this awful, lonely place..."
        rnr_girl2 "It will be an age before his beautiful tendrils regenerate..."
        scene s72_tenta_11 with dissolve
        rnr_girl1 "Hmm... In the meantime... why don't we... pleasure each other?"
        scene s72_tenta_12 with dissolve
        rnr_girl2 "A good idea! We must fill the silence."
        mc "..."
        scene s72_tenta_9 with dissolve
        rnr_girl1 "Why are you still standing there? You're lucky our grief has made us merciful. Get out! And don't you dare come back!"
        mc "Sheesh... Fine. My bad for helping, I guess."
        $ renpy.end_replay()
        scene 72_d13 with dissolve
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
        dm "As you retreat from the room, the two women fall upon each other in a passionate, frantic kiss, their hands roaming desperately."
        mc "Well... that was... I don't know what that was."
        r "*laughs* This dungeon is seriously messed up. I love it."
        call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve

    elif dice_number <= 3:
        $ rnr_health -= 2
        $ rnr_mc_fell_tenta = True
        play sound "sound_effects/rnr/rnr_splash.mp3"
        scene s72_tenta_13 with vpunch
        dm "You charge forward, axe held high, but your boot slips on the slick floor! Your feet fly out from under you and you land face-first into the soft, yielding flesh of the floor. The entire room jiggles grotesquely."
        scene s72_tenta_14 with dissolve
        dm "The impact jars you to your bones. You lose two vitality points! The tentacles, annoyed by the disturbance, give you a dismissive, slimy slap as you scramble back."
        if rnr_health <= 0:
            $ renpy.end_replay()
            if rnr_rune2 and not rnr_rune2_used:
                $ rnr_rune2_used = True
                $ rnr_health += 10
                r "You ran out of vitality!"
                mc "Shit. So that's it? I lost?"
                r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
                mc "Phew... Alright, let's continue then."
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT
            else:
                jump rnr_loss
        else:
            mc "Ew! That's disgusting!"
            r "*laughs* I told you we shouldn't have helped! You just face-planted into a pleasure monster's living room! That's going into my diary!"
            mc "Let's just... let's just leave before something else happens..."
            $ renpy.end_replay()
            play music "echoes_of_sorrow.mp3" fadein 2.0 loop
            jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT

label scene72_choice03_op2:
    mc "I think you're right. They're probably fine."
    dm "The sound of shilcking and moaning slowly decepate as you leave the room."
    $ renpy.end_replay()
    play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    scene 72_d13 with dissolve
    mc "That was... interesting."
    r "Where to now?" 
    call screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT with dissolve

default s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first = True
default s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done = False
label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine:
    if not s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done:
        if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first:
            $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first = False
            scene s72_shrine3_1 with dissolve
            dm "You push open the door to a chamber. You notice a single, translucent sphere of white light floats aimlessly, drifting in a silent, sorrowful pattern."
            mc "A sphere of light? Just... hovering there? That's creepy."
            r "Oh! I remember this one. This isn't a monster; it's a wandering spirit. The book says it's bound to this dungeon because it yearns for a specific item. Once it gets it, it can move on."
            mc "What kind of item? A key? A rune?"
            r "Let me see..."
            scene s72_shrine3_4 with dissolve
            dm "As you step closer, the sphere stops its drifting. It pulses gently, and a soft, echoing voice, like a whisper from the bottom of a well, fills the room."
            rnr_sphere "Travelers... I sense you. I need a favor."
            rnr_sphere "A coin. I seek a single, special coin, minted in a realm long forgotten. It is the anchor of my regret."
            if not rnr_coin:
                mc "A single coin? What possible use could one coin be in a place like this? It's not like there's a tavern around the corner."
                rnr_sphere "If you wish to activate this shrine, you must bring it to me. Only I can rekindle this shrine's fading embers."
                mc "Hmm. Alright then. We'll be back if we find your coin."
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

            elif rnr_coin:
                $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done = True
                $ rnr_shrines += 1
                $ rnr_shrines_all -= 1
                mc "A coin? You mean this one?"
                rnr_sphere "Yes! After so long...! Please... give it to me."
                play sound "sound_effects/rnr/rnr_light.mp3"
                scene s72_shrine3_2 with dissolve
                dm "Upon contact with the coin, it erupts in a blinding, brilliant white light that floods the entire room, forcing you to shield your eyes."
                scene s72_shrine3_3 with dissolve
                dm "When the light recedes, the sphere is gone. In its place stands the shimmering, translucent form of a man, his features kind and filled with immense relief."
                mc "Woah. It worked."
                rnr_sphere "Hahaha! Thank you, dear adventurers! You have freed my soul from this mortal prison! I am in your eternal debt!"
                play sound "sound_effects/rnr/rnr_activate.mp3"
                scene s72_shrine1_4 with dissolve
                rnr_sphere "As promised, I shall light this fire once more! Farewell! May we meet again in a brighter realm!"
                if rnr_shrines == 5:
                    mc "Alright, I think this is it, right? All shrine?"
                    r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
                    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT
                else:
                    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

        else:
            if not rnr_coin:
                scene s72_shrine3_1 with dissolve
                r "We still don't have the coin it wanted. Let's come back later."
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

            elif rnr_coin:
                $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done = True
                $ rnr_shrines += 1
                $ rnr_shrines_all -= 1
                scene s72_shrine3_1 with dissolve
                mc "Is this the coin you wanted?"
                rnr_sphere "Yes! After so long...! Please... give it to me."
                play sound "sound_effects/rnr/rnr_light.mp3"
                scene s72_shrine3_2 with dissolve
                dm "Upon contact with the coin, it erupts in a blinding, brilliant white light that floods the entire room, forcing you to shield your eyes."
                scene s72_shrine3_3 with dissolve
                dm "When the light recedes, the sphere is gone. In its place stands the shimmering, translucent form of a man, his features kind and filled with immense relief."
                mc "Woah. It worked."
                rnr_sphere "Hahaha! Thank you, dear adventurers! You have freed my soul from this mortal prison! I am in your eternal debt!"
                play sound "sound_effects/rnr/rnr_activate.mp3"
                scene s72_shrine1_4 with dissolve
                rnr_sphere "As promised, I shall light this fire once more! Farewell! May we meet again in a brighter realm!"
                if rnr_shrines == 5:
                    mc "Alright, I think this is it, right? All shrine?"
                    r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
                    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT
                else:
                    jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT
    else:
        r "We already activated this shrine!"
        jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

default s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin_first = True
label s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin:
    if not rnr_diamond:
        if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin_first:
            $ s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin_first = False
            $ rnr_met_groblin = True
            scene s72_groplin1 with dissolve
            dm "You push open the door to the next chamber and find... nothing."
            mc "Nothing? What's the catch?"
            scene s72_groplin2 with dissolve
            dm "Just as you finish speaking, you feel a small tug on the leg of your pants. You look down. Staring up at you with enormous eyes is a Groplin, a creature no taller than your ankle, with greenish skin and oversized pointed ears."
            mc "What in the hell is that?"
            stop music fadeout 2.0 
            scene s72_groplin3 with dissolve
            play music "sillytime.mp3" fadein 2.0 loop
            groplin "Cheese?"
            mc "...Cheese?"
            groplin "You. Cheese? Me."
            mc "I'm no expert, but I'm getting the impression this little guy wants some cheese."
            r "Aren't you just the master of deduction? Yes, it appears the tiny guy has a sophisticated palate."

            if rnr_cheese:
                $ rnr_diamond = True
                mc "Here you go, little man."
                scene s72_groplin5 with dissolve
                dm "The Groplin snatches the cheese with a happy squeak and, unhinges its jaw and devours the entire wedge in one single gulp."
                scene s72_groplin6 with dissolve
                dm "He thanks you with a nod then crawls into a hole in the wall, disappearing from your life as quickly as it entered. Where it once stood, a single, perfectly cut diamond glitters on the stone floor."
                mc "*sniff* Godspeed, you funky little cheese gremlin..."
                r "A... A diamond? Who in their right mind trades a diamond for a piece of cheese? And where did he store it anyway?"
                mc "Don't you dare judge his life choices. I'd have made the same trade."
                play music "echoes_of_sorrow.mp3" fadein 2.0 loop
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

            if not rnr_cheese:
                mc "Sorry, little buddy. No cheese on me."
                scene s72_groplin4 with dissolve
                r "Well, you've broken its heart. I hope you're happy. Let's make a note to come back if we ever find the {i}cheese{/i}."
                play music "echoes_of_sorrow.mp3" fadein 2.0 loop
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

        else:
            if rnr_cheese:
                $ rnr_diamond = True
                stop music fadeout 2.0 
                scene s72_groplin4 with dissolve
                play music "sillytime.mp3" fadein 2.0 loop
                mc "We found you some cheese, little man."
                scene s72_groplin5 with dissolve
                dm "The Groplin snatches the cheese with a happy squeak and, unhinges its jaw and devours the entire wedge in one single gulp."
                scene s72_groplin6 with dissolve
                dm "He thanks you with a nod then crawls into a hole in the wall, disappearing from your life as quickly as it entered. Where it once stood, a single, perfectly cut diamond glitters on the stone floor."
                mc "*sniff* Godspeed, you funky little cheese gremlin..."
                r "A... a diamond? Who in their right mind trades a diamond for a piece of cheese? And where did he store it anyway?"
                mc "Don't you dare judge his life choices. I'd have made the same trade."
                play music "echoes_of_sorrow.mp3" fadein 2.0 loop
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

            if not rnr_cheese:
                scene s72_groplin4 with dissolve
                r "We still don't have the cheese yet..."
                jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT
    else:       
        r "We already got a diamond from the Groplin that was here. Let's go find a use for it."
        jump s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT

label s72_dRIGHT_RIGHT:
    call rnr_reset from _call_rnr_reset_15
    $ in_rnr_15 = True
    scene 72_d19 with dissolve
    call screen s72_dRIGHT_RIGHT with dissolve

default s72_dRIGHT_RIGHT_shrine_lit = False
default s72_dRIGHT_RIGHT_shrine_first = True
default scene72_rnr_shrine4_op1 = False
default scene72_rnr_shrine4_op3 = False

label s72_dRIGHT_RIGHT_shrine:
    if not s72_dRIGHT_RIGHT_shrine_lit:
        scene s72_shrine4_1 with dissolve
        if s72_dRIGHT_RIGHT_shrine_first:
            $ s72_dRIGHT_RIGHT_shrine_first = False
            dm "You enter a shrine room. Guarding the shrine is a lone, reanimated skeleton. It clutches a badly chipped bronze sword, its jaw hanging open in a silent, eternal screech."
            mc "Does it have a flaming skull?"
            r "...No?"
            mc "It does now."
            call screen s72_dRIGHT_RIGHT_shrine with dissolve
        else:
            call screen s72_dRIGHT_RIGHT_shrine with dissolve
    else:
        r "We already activated the shrine that was here."
        jump s72_dRIGHT_RIGHT

label s72_dRIGHT_RIGHT_shrine_fight:
    $ rnr_in_fight = True
    stop music fadeout 2.0 
    scene s72_shrine4_2 with dissolve
    play music "battle02.mp3" fadein 2.0 loop
    r "What's the move?"
    if not rnr_shrine_fight_info:
        $ rnr_shrine_fight_info = True
        mc "My move?"
        r "You need to predict the correct action that the original adventures made when they fought this monster."
    call screen s72_dRIGHT_RIGHT_shrine_fight with dissolve

label scene72_choice04_op1:
    $ scene72_rnr_shrine4_op1 = True
    $ rnr_health -= 2
    mc "I'll knock that sword right out of its hands!"
    dm "You execute a disarming maneuver. The rusty sword clatters to the floor. The skeleton, unbothered, simply lunges at you and starts trying to strangle you with its bony hands."
    dm "The Warrior's vitality decreases by 2!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dRIGHT_RIGHT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dRIGHT_RIGHT_shrine_fight with dissolve
        
label scene72_choice04_op3:
    $ scene72_rnr_shrine4_op3 = True
    $ rnr_health -= 2
    mc "I'll go for a low sweep and shatter one of its legs!"
    dm "Your axe smashes into its femur, which explodes into a cloud of bone chips. The skeleton collapses onto one knee... and then immediately starts crawling toward you, twice as fast, still swinging its sword."
    dm "The Warrior's vitality decreases by 2!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dRIGHT_RIGHT_shrine_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dRIGHT_RIGHT_shrine_fight with dissolve

label scene72_choice04_op2:
    $ rnr_in_fight = False
    $ rnr_wrong_choices = True
    play sound "sound_effects/rnr/rnr_bones.mp3"
    scene s72_shrine4_3 with vpunch
    $ s72_dRIGHT_RIGHT_shrine_lit = True
    $ rnr_shrines += 1
    $ rnr_shrines_all -= 1
    dm "You stride forward and, with a single, powerful swing of your axe, you cleave the skeleton clean in two. It collapses into a clattering pile of bones, the magic animating it instantly extinguished."
    play sound "sound_effects/rnr/rnr_activate.mp3"
    stop music fadeout 2.0 
    scene s72_shrine1_4 with dissolve
    dm "The shrine behind it hums to life, its eyes turning green."
    if rnr_shrines == 5:
        mc "Alright, I think this is it, right? All shrine?"
        r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    else:
        mc "Don't give up, skeleton."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    jump s72_dRIGHT_RIGHT

label s72_dRIGHT_RIGHT_key:
    if not rnr_cat_key:
        $ rnr_cat_key = True
        scene s72_key1 with dissolve
        dm "The door to this chamber swings open with surprising ease. Your eyes are immediately drawn to a scene of past tragedy: a fallen lantern, lies next to the skeletal remains of a forgotten adventurer."
        dm "One bony hand is clenched tightly, and within its grasp, you can see the glint of a tarnished iron key."
        mc "Right. Great. It's gonna wait until we get close, then jumpscare us, isn't it?"
        r "Hmm? Why would it do that? It's just a skeleton, you dummy. It's dead. Deader than dead."
        scene s72_key2 with dissolve
        mc "Alright, the brave and incredibly cautious warrior goes ahead and slowly, very slowly, tries to peel the key from the skeleton's fingers..."
        dm "The Warrior kneels beside the skeleton. He begins to pry the skeletal fingers apart, and that's when—"
        scene s72_key3 with vpunch
        r "BOO!"
        scene s72_key5 with Dissolve(1.0)
        mc "..."
        scene s72_key4 with dissolve
        r "...Seriously? Nothing?"
        scene s72_key5 with dissolve
        mc "Sorry. Was expecting it."
        scene s72_key4 with dissolve
        r "Ugh, whatever... Anyway, you got the key."
        scene s72_key5 with dissolve
        scene 72_d19 with dissolve

        if not rnr_cat_first:
            mc "We can probably use this to free that poor cat from its cage."
            r "Let's give the little thing its freedom."

        if rnr_cat_first:
            mc "A key. Wonderful. And what ancient lock is this meant for?"
            r "I'm sure we'll find something that's feeling particularly locked eventually."
        call screen s72_dRIGHT_RIGHT with dissolve

    else:
        r "We already got the key that was there."
        jump s72_dRIGHT_RIGHT

default s72_dRIGHT_RIGHT_RIGHT_poster = True

label s72_dRIGHT_RIGHT_RIGHT:
    call rnr_reset from _call_rnr_reset_16
    $ in_rnr_16 = True
    if s72_dRIGHT_RIGHT_RIGHT_poster:
        scene 72_d20_poster with dissolve
    else:
        scene 72_d20 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT with dissolve

label s72_dRIGHT_RIGHT_RIGHT_poster:
    $ persistent.alex_render1 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ s72_dRIGHT_RIGHT_RIGHT_poster = False
    jump s72_dRIGHT_RIGHT_RIGHT

label s72_d20_chest:
    dm "In the corner sits a chest, its lid thrown wide open. Inside is bare wood, picked clean."
    mc "It's useless. Someone already got this one."
    jump s72_dRIGHT_RIGHT_RIGHT

label s72_dRIGHT_RIGHT_RIGHT_LEFT:
    call rnr_reset from _call_rnr_reset_17
    $ in_rnr_17 = True
    scene 72_d21 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT with dissolve

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP:
    call rnr_reset from _call_rnr_reset_18
    $ in_rnr_18 = True
    scene 72_d22 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP with dissolve

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT:
    call rnr_reset from _call_rnr_reset_19
    $ in_rnr_19 = True
    scene 72_d23 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT with dissolve

default s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue_first = True

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue:
    if not rnr_coin:
        if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue_first:
            $ s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue_first = False
            scene s72_statue1 with dissolve
            dm "The door creaks open to reveal a statue of a woman illuminated by a single shaft of faint, magical light. She is holding her hand up high."
            mc "This doesn't have the same vibe as the shrine rooms. It feels more like a tomb or a memorial. What's her story?"
            r "Not sure. The notes mention there's more to discover if we inspect her closely."
            mc "Alright, let's inspect her then."
            scene s72_statue2 with dissolve
            dm "On closer inspection, the statue is carved with striking craftsmanship. The woman's body is lifelike in every curve, down to the most intimate details."
            mc "(Guess my world wasn't the only one with artists who enjoyed their work a little too much...)"
            mc "Anything else? Inscriptions? A hidden switch?"
            scene s72_statue3 with dissolve
            dm "Your eyes are drawn to her upraised hand. Clutched in her palm is a empty setting, shaped like a gem. It's clearly designed to hold something specific."
            mc "A jewel? Maybe a rune?"
            r "No, it's designed for a proper gemstone. A large one."

            if rnr_diamond:
                $ rnr_coin = True
                mc "Let's see if our gourmet Groglin friend indirectly solved this puzzle for us."
                scene s72_statue4 with dissolve
                dm "You carefully place the diamond into the empty setting. It fits perfectly. With a deep, grinding rumble, the entire pedestal begins to lower into the floor."
                play sound "sound_effects/rnr/rnr_statue.mp3"
                scene s72_statue5 with dissolve
                dm "As it settles, you hear a faint click from within the statue. The statue's mouth parts slightly, and a single, ancient coin is pushed out."
                scene s72_statue6 with dissolve
                if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first:
                    mc "A coin? What use could this be for in a place like this?"
                    r "Let's find out."
                else:
                    mc "A coin? Wait, this is it! That spirit ball said he needed a 'special coin' to be freed."
                    r "Mhm. Let's get this back to him. His shrine is the last one we need."
                jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT

            else:
                mc "A gem, huh? Hmm... Why don't we try putting {i}you{/i} in there?"
                r "Huh? Are you stu—"
                r "Oh... I see what you did there~ Flattery will get you everywhere, you scoundrel."
                mc "Heh~"
                r "Anyway, Mr. Charming. Let's make a note of this and come back when we find the actual gem that fits."
                jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT
        else:
            scene s72_statue1 with dissolve
            scene s72_statue3 with dissolve
            if rnr_diamond:
                $ rnr_coin = True
                mc "Let's see if our gourmet Groglin friend indirectly solved this puzzle for us."
                scene s72_statue4 with dissolve
                dm "You carefully place the diamond into the empty setting. It fits perfectly. With a deep, grinding rumble, the entire pedestal begins to lower into the floor."
                play sound "sound_effects/rnr/rnr_statue.mp3"
                scene s72_statue5 with dissolve
                dm "As it settles, you hear a faint click from within the statue. The statue's mouth parts slightly, and a single, ancient coin is pushed out."
                scene s72_statue6 with dissolve
                if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first:
                    mc "A coin? What use could this be for in a place like this?"
                    r "Let's find out."
                else:
                    mc "A coin? Wait, this is it! That spirit ball said he needed a 'special coin' to be freed."
                    r "Mhm. Let's get this back to him. His shrine is the last one we need."
                jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT

            else:
                r "We're still missing the gem. Let's come back once we find it."
                jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT
    else:
        r "We already got the coin from the statue."
        jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT

default s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster = True

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT:
    call rnr_reset from _call_rnr_reset_20
    $ in_rnr_20 = True
    if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster:
        scene 72_d24_poster with dissolve
    else:
        scene 72_d24 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT with dissolve

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster:
    $ persistent.reb_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster = False
    jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT:
    call rnr_reset from _call_rnr_reset_21
    $ in_rnr_21 = True
    scene 72_d25 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT with dissolve

default s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest = True
label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT:
    call rnr_reset from _call_rnr_reset_22
    $ in_rnr_22 = True
    if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest:
        scene 72_d26 with dissolve
    else:
        scene 72_d27 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT with dissolve

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest:
    $ s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest = False
    dm "You spot a pristine looking chest set upon a raised platform."
    mc "Raised platform? Suspicious. That's practically begging us to open it."
    r "You think it's a trap?"
    mc "Could be. Does your blessing help sniffing out traps?"
    r "It should, yes."
    call screen scene72_choice06 with dissolve

label scene72_choice06_op1:
    mc "Do it. Better safe than sorry."
    perception "Rebecca rolls the dice..."
    $ dice_number = random.randint(1, 6)
    $ renpy.random.seed()
    perception "The dice lands on [dice_number]!"  
    if dice_number > 3:
        $ rnr_rune2 = True
        r "Got it!"
        dm "The chest shimmers, then creaks open by itself. Inside lies a silver band, glowing faintly. The ring of second heart."
        scene 72_d27 with dissolve
        mc "Ring of second heart?"
        r "Oh! That's rare! It grants a second life, you'll rise once more if you fall in battle."
        mc "Not bad. That's going straight on my finger."

    elif dice_number <= 3:
        r "Shit!"
        scene 72_d27 with vpunch
        dm "The chest trembles, then collapses into a cloud of black dust, vanishing without a trace."
        mc "Black dust? Could've been explosive. I say we dodged a bullet either way."
        r "Maybe... still feels like a waste."
    jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT

label scene72_choice06_op2:
    mc "Ah, to hell with caution. Let's just open it."
    r "[mc], are you sure? This is the most obvious trap I have ever seen in my life!"
    mc "Life's short. Let's live dangerously. Yes."
    play sound "sound_effects/rnr/rnr_explosion.mp3"
    scene 72_d27 with vpunch
    dm "The lid creaks open—then BAM! A violent explosion fills the room. The Warrior staggers back, losing five vitality points."
    r "Dammit! You literally said it was a trap!"
    $ rnr_health -= 5
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT
        else:
            jump rnr_loss
    else:
        mc "Whoops, sorry..."
        r "*sigh* Let's keep moving..."
    jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP:
    call rnr_reset from _call_rnr_reset_23
    $ in_rnr_23 = True
    scene 72_d28 with dissolve
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP with dissolve

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_UP:
    call rnr_reset from _call_rnr_reset_24
    $ in_rnr_24 = True
    scene 72_d29 with dissolve
    mc "Looks like a deadend."
    r "You're right. Should we go back to the main room? We can instantly go there if we jump in the water."
    call screen scene72_choice04 with dissolve

    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_UP with dissolve

default s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch_first = True
image s72_witch_anim = Movie(play="images/4_chapter3/scene72/s72_witch/s72_witch_anim.webm", loop=True)

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p6_replay:
        $ persistent.scene4_p6_replay = True

    if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch_first:
        $ s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch_first = False
        scene s72_witch1 with dissolve
        dm "You push open the door to reveal an empty chamber. At its center, a witch stands alone, chanting softly in the dark."
        mc "A witch, huh?"
        r "You're thinking of {i}that one,{/i} aren't you?"
        mc "Mhm."
        if quest_witch_amelia_alive:
            if quest_witch_amelia_alive_free:
                r "I heard what happened. You let her go, for whatever reason. I just hope you knew what you were doing."
                mc "Don't worry. She won't be hurting anyone anymore."
            else:
                r "I heard what happened. Good work on that, by the way."
                mc "Thank you."
        else:
            r "I heard what happened. You... killed her."
            r "Whatever went down, I'm sure it was a last resort. Right?"
            mc "Yeah."  
        dm "Before either of you can even raise a weapon, the ground quakes with magical energy. It's a trap!"
        stop music fadeout 2.0 
        play sound "sound_effects/rnr/rnr_magic.mp3"
        scene s72_witch2 with vpunch
        dm "A pink wave of magic seeps into you, [mc], clouding your mind with warm, fuzzy static, while a sickly green magic inflicts the Mage sapping the strength from her limbs."
        r "I can't use my spells in this state!"
        scene s72_witch3 with dissolve
        dm "The witch's eyes lock onto you, [mc]. A smile plays on her lips as she glides forward, utterly ignoring the weakened mage."
        mc "W-What is she trying to do?"
        r "She's identified you as male... she doesn't want to kill you, she wants to... harvest you! They use male essence to fuel their power!"
        rnr_witch "So dramatic, little mage. Relax, my strong warrior. Let's make a simple trade. You provide me with a donation... of your vital essence, and I will let you and your friend walk out of here, completely unharmed."
        mc "Uhh... Rebecca, any ideas?"
        r "I'm not allowed to help you. I'm under the influence of a weakness hex."
        show s72_witch_anim with dissolve
        dm "The witch takes off her skirt and begins to sway, a hypnotic dance. Her hips trace slow circles in the air."
        dm "You can feel a heat radiating from her, the scent of her hairy enterance. Your own body betrays you, responding to the charm spell."
        mc "This is weird..."
        r "Just play along!"
        rnr_witch "*ahem* Give in~ It is the only path that spares your friend. Let me have what I desire."
        rnr_witch "Ejaculate for me~"
        call screen scene72_choice05 with dissolve

    else:
        r "No reason to go in there anymore. The witch is gone."
        jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP

label scene72_choice05_op1:
    mc "NO! Get out of my head!"
    perception "You roll the dice..."
    $ dice_number = random.randint(1, 6)
    $ renpy.random.seed()
    perception "The dice lands on [dice_number]!"
    if dice_number > 3:
        $ rnr_defeat_witch = True
        $ rnr_rune1 = True
        play sound "sound_effects/unsheathe.mp3"
        scene s72_witch7 with vpunch
        dm "With a guttural roar, you pick up your axe and cleave her in half. She doesn't even have time to scream."
        dm "Her body dissolves into a pile of dust before it hits the floor."
        play sound "sound_effects/poof.mp3"
        scene s72_witch6 with dissolve
        mc "Phew... You okay?"
        r "The hex lifts the moment she dies. And damn, warrior... that was... incredibly impressive~"
        mc "Did she drop anything?"
        scene s72_witch8 with dissolve
        dm "As the last of the ash settles, something hovers within it: a heavy, obsidian rune etched with a symbol resembling a brain. You slip it on, and shocking clarity floods your mind."
        mc "Uhh... What does it do exactly?"
        r "That's a rune of insight. It's a single-use item. When you're facing a monster and have to choose your move, you can use it. It'll show you the correct action out of the three."
        mc "Nice. Now this is a reward."
        $ renpy.end_replay()
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
        jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP

    elif dice_number <= 3:
        mc "Oh man..."
        jump scene72_choice05_op2

label scene72_choice05_op2:
    $ rnr_health -= 2
    mc "I guess I give in..."
    dm "Your resistance crumbles. The world narrows to a single goal, ejaculating. Your body goes limp, not with weakness, but with anticipation."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene s72_witch4 with vpunch
    dm "You seed spurts out like a torrent, an amount you didn't know your body could hold. You vitality decreases by 2!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            scene s72_witch5 with dissolve
            mc "Alright... You got what you want. Let us go."
            rnr_witch "But of course. A deal is a deal. I am a woman of my word."
            play sound "sound_effects/poof.mp3"
            scene s72_witch6 with dissolve
            dm "With a snap of her fingers, the witch vanishes into the air. Instantly, the strength returns to the Mage's limbs and the fog clears from your mind."
            mc "Damn... Sorry, Becky. I couldn't fight her off."
            $ renpy.end_replay()
            if mc_sub:
                r "*chuckles* I knew you would give in."
                mc "How's that?"
                r "You told me yourself. You're a {i}follower{/i}, remember~?"
                mc "Oh, right..."
                play music "echoes_of_sorrow.mp3" fadein 2.0 loop
            else:
                r "It's fine... Let's just try to avoid witches from now on."
                mc "Right..."
                play music "echoes_of_sorrow.mp3" fadein 2.0 loop
            jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP
        else:
            jump rnr_loss
    else:
        scene s72_witch5 with dissolve
        mc "Alright... You got what you want. Let us go."
        rnr_witch "But of course. A deal is a deal. I am a woman of my word."
        play sound "sound_effects/poof.mp3"
        scene s72_witch6 with dissolve
        dm "With a snap of her fingers, the witch vanishes into the air. Instantly, the strength returns to the Mage's limbs and the fog clears from your mind."
        mc "Damn... Sorry, Becky. I couldn't fight her off."
        $ renpy.end_replay()
        if mc_sub:
            r "*chuckles* I knew you would give in."
            mc "How's that?"
            r "You told me yourself. You're a {i}follower{/i}, remember~?"
            mc "Oh, right..."
            play music "echoes_of_sorrow.mp3" fadein 2.0 loop
        else:
            r "It's fine... Let's just try to avoid witches from now on."
            mc "Right..."
            play music "echoes_of_sorrow.mp3" fadein 2.0 loop
        jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP

default s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_first = True
label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider:
    if not rnr_shrine_spider:
        if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_first:
            $ s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_first = False
            dm "As you push open the next—"
            scene s72_spider2 with vpunch
            r "Ahhhh!"
            mc "Huh? What's wrong?"
            r "Eughh... It's a spider. A giant one. Why did it have to be spiders?"
            mc "*laughs* Ah, I see. Why are you covering your eyes anyway? It's just words."
            r "It's not funny! They drew it! They didn't have to draw it!"
            scene s72_spider1 with dissolve
            dm "*ahem* As you open the door, you find a massive, {i}hairy{/i} Skitter-Maw guarding the shrine. Its eight segmented legs twitch rhythmically."
            mc "Wait, is this a real creature out there in the world?"
            r "Y-Yes. Thankfully, they don't live anywhere near us. They prefer the warmer climates to the south. I heard their webs can ensnare a full grown ogre."
            mc "Thank God for small mercies..."
            r "Anyway, putting my personal feelings aside... Should we engage?"
            call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider with dissolve
        else:
            scene s72_spider1 with dissolve
            call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider with dissolve
    else:
        r "We already defeated the awful spider and activated this shrine."
        jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP

label s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight:
    $ rnr_in_fight = True
    stop music fadeout 2.0 
    scene s72_spider3 with dissolve
    play music "battle02.mp3" fadein 2.0 loop
    dm "The Skitter-Maw's cluster of glistening, red eyes all swivel to focus on your group with unnerving synchronicity."
    r "What's our move?"
    if not rnr_shrine_fight_info:
        $ rnr_shrine_fight_info = True
        mc "Our move?"
        r "You need to predict the correct action that the original adventures made when they fought this monster."
    call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight with dissolve

default scene72_rnr_shrine5_op1 = False
default scene72_rnr_shrine5_op2 = False

label scene72_rnr_shrine5_op1:
    $ scene72_rnr_shrine5_op1 = True
    $ rnr_health -= 5
    dm "You lunge forward, aiming your axe for its mouth. The Skitter-Maw, spits a thick glob of web that pins your weapon to the floor. While you're yanking it free, it skitters sideways and nips you on the shoulder."
    dm "The Warrior's vitality decreases by 5!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight with dissolve

label scene72_rnr_shrine5_op2:
    $ scene72_rnr_shrine5_op2 = True
    $ rnr_health -= 5
    dm "You dive directly under the spider. It's a brilliant idea, until it immediately drops its full weight on you, pinning you to the floor with its bulk."
    dm "The Warrior's vitality decreases by 5!"
    if rnr_health <= 0:
        if rnr_rune2 and not rnr_rune2_used:
            $ rnr_rune2_used = True
            $ rnr_health += 10
            r "You ran out of vitality!"
            mc "Shit. So that's it? I lost?"
            r "Wait, no you don't. You have the ring of second heart, remember? It shatters, and your warrior groggily gets back to his feet."
            mc "Phew... Alright, let's continue then."
            call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight with dissolve
        else:
            jump rnr_loss
    else:
        call screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight with dissolve

label scene72_rnr_shrine5_op3:
    $ rnr_shrines += 1
    $ rnr_shrines_all -= 1
    $ rnr_in_fight = False
    $ rnr_shrine_spider = True
    play sound "sound_effects/slash03.mp3"
    scene s72_spider4 with vpunch
    dm "With a battle cry, the Warrior charges! His axe swings in a devastating arc, shearing through two of the Skitter-Maw's legs with a sickening crunch. The creature collapses, flailing helplessly."
    play sound "sound_effects/rnr/rnr_fireball.mp3"
    scene s72_spider5 with vpunch
    dm "Seizing the opening, the Mage incinerates its shrieking form with a perfectly aimed fireball that leaves behind only the smell of burnt chitin."
    stop music fadeout 2.0 
    play sound "sound_effects/rnr/rnr_activate.mp3"
    scene s72_shrine1_4 with dissolve
    dm "As the last embers fade, the shrine hidden behind the cobwebs, and its stone eyes ignite with a green light."
    if rnr_shrines == 5:
        mc "Alright, I think this is it, right? All shrine?"
        r "Yup! All shrines activated! Let's head back to the main chamber and finish this."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    else:
        r "Good riddance."
        play music "echoes_of_sorrow.mp3" fadein 2.0 loop
    jump s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP

label rnr_win:
    $ in_free_roam = False
    $ rnr_win = True
    scene 71_s16 with dissolve
    r "Alright! And... that's where we'll end the session for today."
    scene 71_s17 with dissolve
    play music "side_event3.mp3" fadein 2.0 loop
    mc "Huh? Wait, what happens? What's in the room? You can't just leave it there!"
    scene 71_s16 with dissolve
    r "We just decend to the second depth of the dungeon."
    scene 71_s17 with dissolve
    mc "Oh, so we're not escaping? We're just going deeper?"
    scene 71_s16 with dissolve
    r "Basically. The ultimate goal is to reach the very bottom. We can continue the campaign later, maybe even rope Maia or someone else in to make a proper party."
    scene 71_s17 with dissolve
    if mc_noprize_bgame:
        mc "Alright, we won. But like I said—"
        scene 71_s16 with dissolve
        r "Right, right. You don't want your prize."
        scene 71_s17 with dissolve
        mc "*chuckles* How about we talk instead? I don't mind spending more time with you."
        scene 71_s16 with dissolve
        r "That sounds nice."
        scene 71_s17 with dissolve
        jump rnr_loss
    else:
        mc "Alright, fair enough. But for now... a win is a win. Which means..."
        scene 71_s18 with dissolve
        r "Yeah, yeah. Don't rub it in. You got lucky."
        scene 71_s19 with dissolve
        mc "Now, remind me. What was the exact wording of my prize again, hmm~?"
        scene 71_s18 with dissolve
        r "*sigh* ...You have a... 'ejaculation permit.' You can finish... wherever you wish... whenever you wish... on my body. For a whole day. Happy?"
        scene 71_s19 with dissolve
        mc "I really love the sound of that."
        mc "And what would my dear princess do about it?"
        scene 71_s18 with dissolve
        r "Nothing. I'd... take it."
        scene 71_s19 with dissolve
        mc "Jokes aside... when does this 'whenever' clock start ticking?"
        scene 71_s16 with dissolve
        r "Like I said. Whenever you want. It's your prize. Just... maybe give a girl a little warning."
        r "Anyway, all that thinking and scheming has worn me out. I'm gonna go... just lay down for a bit."
        stop music fadeout 2.0 
        scene 71_s17 with dissolve
        jump scene73

label rnr_loss:
    $ in_free_roam = False
    if not rnr_win:
        r "You ran out of vitality!"
        mc "Shit. So that's it? I lost?"
        stop music fadeout 2.0 
        scene 71_s16 with dissolve
        r "You did. Completely and utterly."
        play music "side_event2.mp3" fadein 2.0 loop
        scene 71_s17 with dissolve
        mc "Damn... Guess I'm not wining any prize, huh?"
        scene 71_s16 with dissolve
        r "Hold on, we can still... hang out."
        scene 71_s17 with dissolve
        mc "Sure. Better than nothing."
    if rnr_win:
        scene 71_s28 with Fade(1.0,1.0,1.0)
        mc "So, what's the latest gossip? I'm out of the loop."
    else:
        scene 71_s29 with Fade(1.0,1.0,1.0)
        r "You didn't get your prize but you can still talk to me. Isn't that an even better prize?"
        scene 71_s28 with dissolve
        mc "*chuckles* Sure. Whatsup?"

    scene 71_s26 with Dissolve(1.0)
    r "Let's see... A new cook tried a new recipe for lemon tarts. They were so sour Avery's eye twitched for an hour, but she was too polite to say anything. It was hilarious."
    scene 71_s27 with dissolve
    mc "*chuckles* Hopefully this cook still works here."
    scene 71_s29 with Dissolve(1.0)
    r "Okay, your turn. What's something boring that happened to you?"
    scene 71_s28 with dissolve
    mc "Ran into Captain Alice today. She cornered me and asked me to train a new recruit."
    scene 71_s30 with dissolve
    r "{i}You?{/i} Why you? Don't they have seasoned sergeants for that?"
    scene 71_s31 with dissolve
    mc "My thoughts exactly. She said the usual trainers were tied up with other duties."
    scene 71_s29 with dissolve
    r "I doubt that was all there was to it. Alice doesn't do anything without three layers of calculation. She must have chosen you specifically."
    scene 71_s32 with dissolve
    r "Is there something you're not telling me, [mc]?"
    scene 71_s33 with dissolve
    mc "Huh? No, it's not like that... I guess it's just because I've been reliable to your mother a few times now. My name probably came up."
    scene 71_s29 with dissolve
    r "Hmm, maybe. So, what did you say? Don't leave me in suspense."
    scene 71_s28 with dissolve

    if mc_accept_joan:
        mc "I told her I'd do it. Seemed like the right thing to do. I sent the recruit home for the day, though. She looked like a startled deer. No sense in breaking her on the first day."
        scene 71_s30 with dissolve
        r "Well, aren't you a gentle instructor?"
        scene 71_s29 with dissolve
        r "Just remember. That 'startled deer' will be facing monsters. If she dies because you went too easy on her, I doubt you'd sleep well with that on your conscience."
        scene 71_s28 with dissolve
        mc "I get that. It's a heavy responsibility."
        scene 71_s32 with dissolve
        r "And you better not have agreed to train her just because she's a girl."
        scene 71_s33 with dissolve
        mc "Uhh... Of course not."
    else:
        mc "I told her to find someone else. I'm not ready for that kind of responsibility. One wrong move, and it's someone's life on the line."
        scene 71_s28 with dissolve
        r "Hmm... Probably for the best."
        scene 71_s29 with dissolve
        r "If that recruit had gotten hurt due to your inexperience, that's a ghost that would haunt your halls. I doubt you'd sleep well with that on your conscience."
        scene 71_s32 with dissolve
        r "And you better not have agreed to train her just because she's a girl."
        scene 71_s33 with dissolve
        mc "Uhh... Of course not."

    mc "What else is going on with you?"
    scene 71_s29 with dissolve
    r "Not much, really. I haven't set foot outside the castle grounds in a while, if you remember. I'm just... waiting. Waiting for my mother to return so I can finally breathe again and leave."
    scene 71_s28 with dissolve
    mc "Why not just... you know. Sneak out?"
    scene 71_s35 with Dissolve(1.5)
    r "..."
    scene 71_s34 with dissolve
    r "I... I don't know. I guess I'm afraid of being seen. My {i}relationship{/i} with the maids and guards isn't exactly... warm."
    r "They tolerate me because they have to. I'm pretty sure half of them would sell me out to my aunt for an extra day off."
    scene 71_s35 with dissolve
    mc "I see. So, where did you used to go? When you did manage to get out. What's your spot?"
    scene 71_s34 with dissolve
    r "There's an old, forgotten garden on the western cliffside. It's all overgrown and wild. The view of the sunset from there... I can't really describe it with words. It wouldn't do it justice."
    scene 71_s29 with dissolve
    r "Why? Are you offering to be my accomplice?"
    scene 71_s28 with dissolve
    mc "Maybe."
    r "..."
    scene 71_s29 with dissolve
    r "If my mother isn't back in the next few days... I don't think I can stand being caged in here any longer. I'll {i}have{/i} to get out."
    r "Anyway, I barely slept a wink last night. I was up thinking about playing Realms and Runes with you."
    scene 71_s28 with dissolve
    mc "And we had lots of fun. Now, your royal decree is to take a nap."
    r "Mhm."
    scene 71_s29 with dissolve
    r "You'll... stay with me? Right? Until I fall asleep?"
    r "I'm thinking of sleeping naked today. What do you think~?"
    scene 71_s28 with dissolve
    call screen scene72_choice07 with dissolve
    mc "*chuckles* I'm not going anywhere."
    stop music fadeout 2.0 
    scene black with Fade(1.0,1.0,1.0)
    perception "You lie down on the bed beside Rebecca. The silence between you is comfortable, and you stay, listening to her breathing even out and soften, until you're certain she's asleep."
    jump scene74

label scene72_choice07_op2:
    mc "Sorry, Becky. Just remembered I had something to do..."
    scene 71_s32 with dissolve
    r "Oh? What's that?"
    scene 71_s33 with dissolve
    mc "It's a secret. Can't tell you."
    scene 71_s34 with Dissolve(1.5)
    r "*sigh* Fine. Whatever. Just... Just be careful, alright?"
    scene 71_s35 with dissolve
    mc "Of course."
    stop music fadeout 2.0 
    jump scene74

default scene73_choices = 0
default scene73_choice_clothes = False
default scene73_choice_face = False
default scene73_choice_breasts = False
default scene73_choice_belly = False
default scene73_choice_feet = False

label scene73:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene5_p6_replay:
        $ persistent.scene5_p6_replay = True

    scene 73_s71 with Fade(1.0,1.0,1.0)
    play music "fire.mp3" fadein 2.0 volume 0.3 loop
    call screen scene73_choice01 with dissolve

label scene73_choice01_op1:
    stop music fadeout 2.0 
    $ scene73_choice_clothes = True
    $ scene73_choices += 1
    scene 73_s1 with Fade(0.5,0.5,0.5)
    perception "You find Rebecca on her knees, rummaging through a drawer with intense focus. She's muttering to herself about a missing hairpin."
    desire "Oh, she'll find something alright."
    scene 73_s2 with dissolve
    r "[mc]? What are you—"
    r "Oh... Of course."
    r "A-And where, precisely, do you intend to ejaculate anyway?"
    scene 73_s3 with dissolve
    mc "Don't mind me. Just keep searching for whatever it is you're searching for."
    r "..."
    scene 73_s21 with Dissolve(1.5)
    empathy "You can see the tension in her shoulders, the way her breath hitches every time she hears the soft, wet sound of your stroking."
    scene 73_s22 with dissolve
    r "[mc], I would like to let you know that these clothes are very new and clean."
    scene 73_s21 with dissolve
    mc "Okay?"
    scene 73_s22 with dissolve
    r "Just keep it in mind..."
    scene 73_s21 with dissolve
    mc "What are you looking for anyway?"
    scene 73_s22 with dissolve
    r "A hairpin, I remember putting it here along with the board a long time ago."
    scene 73_s21 with dissolve
    call screen scene73_choice04 with dissolve
    mc "Nghn!"
    scene 73_s22 with dissolve
    play sound "se_sfx/blowjob/facial4.mp3" 
    show screen cum
    scene 73_s4 with dissolve
    perception "Thick, hot ropes of cum splatter across the back of her dress, white against the black fabric. The first burst is a surprise, making her jolt, but she remains kneeling, taking it."
    r "Ugh..."
    play sound "se_sfx/blowjob/facial6.mp3" 
    scene 73_s5 with dissolve
    hide screen cum
    perception "You watch, mesmerized, as it soaks through the cotton, creating a wet patch that clings to her skin, marking her as yours."
    scene 73_s6 with dissolve
    r "Are you done ruining my dress?"
    scene 73_s7 with dissolve
    mc "*chuckles* For now."
    scene 73_s6 with dissolve
    r "I can feel it through the dress, it's slowly making my butt wet."
    scene 73_s7 with dissolve
    mc "I told you I'd mark you as mine."
    scene 73_s6 with dissolve
    r "Mark me?! I'm not a beast, you know? You can't just... *sigh* Whatever."
    r "Can't believe I'll have wash it already... It hasn't even been a day."
    scene 73_s7 with dissolve
    jump scene73

label scene73_choice01_op2:
    stop music fadeout 2.0 
    $ scene73_choice_face = True
    $ scene73_choices += 1
    scene 73_s8 with Fade(0.5,0.5,0.5)
    perception "You find Rebecca sitting at her vanity as the soft morning light spills across her skin. She's applying makeup, a brush in her hand dusting powder over her cheeks."
    scene 73_s9 with Dissolve(1.2)
    r "W-What are you doing?"
    scene 73_s10 with dissolve
    mc "Your face is so pretty, It'd be a shame for someone to cover it with something so... sticky and warm."
    scene 73_s9 with dissolve
    r "Ugh! You asshole! Do you have any idea how long and tedious it is to apply this makeup? This isn't fair!"
    scene 73_s10 with dissolve
    mc "It's the rules, princess. A deal's a deal."
    scene 73_s11 with dissolve
    r "*sigh* I guess I can just... do it all over again later."
    scene 73_s12 with dissolve
    mc "No, keep doing your makeup. Don't stop."
    scene 73_s11 with dissolve
    r "Please, [mc]..."
    scene 73_s12 with dissolve
    mc "Keep doing it."
    scene 73_s13 with Dissolve(1.2)
    r "..."
    scene 73_s14 with dissolve
    mc "Good. Can't wait to cover you."
    scene 73_s13 with dissolve
    r "Just don't shoot it in my eye, alright?"
    scene 73_s14 with dissolve
    mc "*chuckles* Your eye? You're giving me ideas."
    scene 73_s13 with dissolve
    r "[mc]..."
    call screen scene73_choice04 with dissolve
    scene 73_s14 with dissolve
    mc "I... I'm!"
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 73_s15 with dissolve
    perception "A hot, sudden splash lands on her cheek, another across her carefully styled hair. The most damning streak lands directly on her eyelid, and she squeezes her eye shut with a sharp gasp."
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene 73_s16 with dissolve
    r "Hah!"
    hide screen cum
    scene 73_s18 with dissolve
    perception "You watch, heart pounding, as your cum drips slowly down her face, ruining her makeup and marking her flawless skin, a beautiful mess of your own making."
    scene 73_s17 with dissolve
    r "Ahnnnn... You ejaculated on my face! It's all ruined now!"
    scene 73_s18 with dissolve
    mc "*laughs* You look a lot more beautiful now, my own little princess."
    scene 73_s17 with dissolve
    r "My eye hurts!"
    r "You little shit. I'll get you back for this, I promise."
    scene 73_s18 with dissolve
    mc "Smile for me."
    scene 73_s17 with dissolve
    r "What?!"
    scene 73_s18 with dissolve
    mc "I want you to look at yourself in the mirror and smile while my cum is all over you face."
    r "..."
    scene 73_s19 with Dissolve(1.3)
    r "Hhnnn... haha..."
    mc "*chuckles* So pretty. Now tell me how much you love being covered in my cum."
    scene 73_s20 with dissolve
    r "T-Thank you for covering me with your seed, [mc]. I-I sure do love it!"
    r "My face is yours to... *gag* ejaculate on whenever you wish!"
    scene 73_s19 with dissolve
    mc "Alright, alright. Go ahead and clean up. I feel like you're about to puke any second."
    scene 73_s18 with dissolve
    r "..."
    jump scene73

label scene73_choice01_op3:
    stop music fadeout 2.0 
    $ scene73_choice_breasts = True
    $ scene73_choices += 1
    scene 73_s23 with Fade(0.5,0.5,0.5)
    perception "You find Rebecca sitting at the table reading a novel. A shaft of sunlight illuminates the page and the gentle curve of her breasts."
    mc "Your posture is terrible. Straighten your back."
    scene 73_s24 with Dissolve(1.0)
    r "Huh? Oh... *sigh* I swear, if you so much as touch my book with your... seed..."
    scene 73_s25 with dissolve
    mc "I can't always help where it might land, sometimes, it's just... out of my control."
    scene 73_s24 with dissolve
    r "Just... Just try not to, alright? I still haven't finished this one."
    scene 73_s26 with Dissolve(0.7)
    mc "Mhm. Anyway, show me your breasts."
    scene 73_s24 with Dissolve(0.7)
    r "W-Why?"
    scene 73_s25 with dissolve
    mc "I've decided on a target. I want to ejaculate on these milk jugs of yours."
    scene 73_s24 with dissolve
    r "Milk jugs?! Don't you think that's a little degrading?"
    scene 73_s25 with dissolve
    mc "Come on, princess."
    r "..."
    scene 73_s24 with dissolve
    r "*sigh* At least it isn't on my book..."
    scene 73_s27 with Dissolve(1.0)
    r "..."
    scene 73_s29 with Dissolve(1.0)
    perception "After a tense moment, she reluctantly sets her book aside. She pulls her dress down, baring her full, soft breasts to you. The cool air makes her nipples peak instantly."
    scene 73_s28 with dissolve
    r "Here. Have fun, you pervert."
    scene 73_s29 with dissolve
    mc "Actually, I want you to talk about them."
    scene 73_s28 with dissolve
    r "W-What do you mean?"
    scene 73_s29 with dissolve
    mc "Tell me how big they are. And how much you want me to finish on them."
    scene 73_s30 with dissolve
    r "That's not part of the deal! You just have to finish anywhere you want, not make me say... stupid, erotic things!"
    r "Actually, I'm not even supposed to get naked for you! This is already me being... kind."
    scene 73_s31 with dissolve
    mc "Oh, please. Don't tell me you don't enjoy this. Just a little. Don't tell me you haven't thought about it."
    scene 73_s33 with dissolve
    r "..."
    scene 73_s32 with dissolve
    r "P-Please, [mc]... Cover my... breasts with your... s-seed."
    scene 73_s34 with dissolve
    mc "Tell me more."
    scene 73_s32 with dissolve
    r "These... these large breasts... were m-made for you... to cover them everyday..."
    r "I... I want to feel your warm, hot seed... trickle down my large, soft breasts and between my cleavage..."
    scene 73_s34 with dissolve
    mc "Fuck... I'm close!"
    call screen scene73_choice04 with dissolve
    mc "Nghn!"
    show screen cum
    play sound "se_sfx/blowjob/facial4.mp3" 
    scene 73_s35 with dissolve
    perception "The first burst lands square on one nipple, making her gasp. The next shots crisscross her soft, pale skin, painting her in streaks of white."
    r "Hnn!"
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 73_s36 with dissolve
    perception "Just as she begged, a thick rivulet pools in the deep valley of her cleavage before slowly, sensually, tracing a path down the smooth skin of her stomach."
    scene 73_s37 with Dissolve(1.0)
    hide screen cum
    r "Oh my..."
    scene 73_s38 with dissolve
    mc "Fuck... that's a lot."
    scene 73_s37 with dissolve
    r "You don't say..."
    scene 73_s39 with dissolve
    r "What the hell do I do now?"
    scene 73_s40 with dissolve
    mc "...Nothing? Just let it sit there."
    scene 73_s39 with dissolve
    r "No way! I'm going straight to the baths."
    scene 73_s40 with dissolve
    mc "Aww, was all that you said a lie then?"
    scene 73_s37 with dissolve
    r "Hnnn... I said it to... make you feel..."
    r "Whatever. I guess I'll let it... stay there for just a bit."
    scene 73_s38 with dissolve
    mc "Good girl."
    scene 73_s40 with dissolve
    r "Hmph..."
    jump scene73

label scene73_choice01_op4:
    stop music fadeout 2.0 
    $ scene73_choice_belly = True
    $ scene73_choices += 1
    scene 73_s41 with Fade(0.5,0.5,0.5)
    perception "You see Rebecca lying on her back, staring at the canopy of her bed with a distant expression. Her hands rest on her stomach, rising and falling with her breath."
    mc "Something on your mind?"
    scene 73_s42 with dissolve
    r "Hmm? No, nothing important. Just... drifting away. What do you want?"
    scene 73_s43 with Dissolve(1.0)
    mc "I've been thinking, too. I want to see my cum glistening on your skin. Right here."
    scene 73_s44 with dissolve
    r "On my... belly? It's such a... mundane place. Why there?"
    scene 73_s43 with dissolve
    mc "Because it's soft. And inviting. I want to mark you here.."
    scene 73_s44 with dissolve
    r "But what's so arousing about that? It's just my stomach."
    scene 73_s43 with dissolve
    mc "Maybe I'm thinking about how it'll look when you're pregnant one day. Swollen with my child. Your breasts heavy and full, leaking milk..."
    scene 73_s45 with dissolve
    r "Hey! You're...! Don't say it like that out of nowhere...!"
    scene 73_s46 with dissolve
    mc "It's what I see when I look at you."
    scene 73_s45 with dissolve
    r "You're so strange... But... alright. I'm yours. Go ahead..."
    r "I'll take off my dress so you can see for yourself how sensual my belly button is. I guess."
    scene 73_s46 with dissolve
    scene 73_s48 with Fade(0.5,0.5,0.5)
    r "*giggles* You're really doing it~"
    scene 73_s47 with dissolve
    mc "Hah... hahh... You have no idea what this does to me."
    scene 73_s48 with dissolve
    r "Heh... Leaking milk, huh? You're making it sound hotter than it should be."
    r "You should count yourself lucky, you know?"
    scene 73_s47 with dissolve
    mc "Lucky?"
    scene 73_s48 with dissolve
    r "Mhm. Not many men get to ejaculate on a princess's body."
    r "Now look at me..."
    r "Look into my eyes... and spill every drop of that seed on my belly, dear husband."
    scene 73_s47 with dissolve
    mc "Fuck... Becky! I'll make sure to cover your whole belly in it!"
    r "Mhm~"
    call screen scene73_choice04 with dissolve
    show screen cum
    play sound "se_sfx/blowjob/facial1.mp3" 
    scene 73_s49 with dissolve
    perception "The sudden, startling seed splashes across her stomach, a stark contrast to her cooler skin. She gasps softly, her muscles tensing for a moment at the sensation."
    play sound "se_sfx/blowjob/facial5.mp3" 
    scene 73_s50 with dissolve
    perception "You watch, as your cum pools in the dip of her navel before slowly tracing a path down the curve of her hip."
    scene 73_s52 with dissolve
    hide screen cum
    mc "Fuck..."
    scene 73_s51 with dissolve
    r "It's... really warm..."
    r "You really must love me, if even a part of me this simple can arouse you so much..."
    scene 73_s52 with dissolve
    mc "You have no idea."
    scene 73_s51 with dissolve
    r "*giggles* Just get me a cloth. It's starting to feel sticky."
    scene 73_s52 with dissolve
    jump scene73

label scene73_choice01_op5:
    stop music fadeout 2.0 
    $ scene73_choice_feet = True
    $ scene73_choices += 1
    scene 73_s53 with Fade(0.5,0.5,0.5)
    perception "Rebecca is lying on her stomach, idly kicking her feet in the air behind her. Her delicate, pale feet are on full display, looking soft and strangely vulnerable."
    r "Hmm? What are you looking at so intently? Do you want to finish on my butt? Is that it?"
    mc "No. Lower. Your feet."

    if mc_kissed_reb_foot or persistent.scene6_p5_replay:
        r "My feet, huh? I had a feeling this would be one of the places you'd pick~"
        r "Well, go on then, my little feet obsessed husband. It's certainly a lot easier to clean than my hair or my clothes."
    else:
        r "My feet? Are you serious?"
        r "Fine. If that's what you want I guess."

    mc "Ahhn! Becky..."
    scene 73_s54 with Dissolve(1.0)
    r "Here, let me help you get a better angle."
    scene 73_s54 with dissolve
    r "Go on. Cover them up~"
    scene 73_s55 with dissolve
    mc "Fuck, Becky... You sure know what I like!"
    scene 73_s54 with dissolve
    r "*giggles* I'm a quick learner."
    call screen scene73_choice04 with dissolve
    show screen cum
    play sound "se_sfx/blowjob/facial6.mp3" 
    scene 73_s56 with dissolve
    perception "Your warm cum lands across the elegant bridge of her foot and her toes. She curls her toes at the sudden, intimate heat."
    play sound "se_sfx/blowjob/facial7.mp3" 
    scene 73_s57 with dissolve
    mc "Aghhn!"
    scene 73_s58 with dissolve
    hide screen cum
    r "Oh? Already done? That was... fast."
    mc "Y-Yeah..."
    if persistent.scene5_p5_replay:
        r "I can't believe it! You finish quicker from my feet than from a proper handjob! What a weird man I've been married to~"
    else:
        r "I can't believe how someone can be so attracted to feet~"
    jump scene73

label scene73_choice01_op6:
    stop music fadeout 2.0 
    scene 73_s59 with Fade(1.5,1.0,1.2)
    mc "Phew... I didn't think my body was even capable of that many times in one day."
    scene 73_s60 with dissolve
    r "Oh, thank the Gods you're finally done... I was beginning to think you were trying to drown me in it. I feel like a glazed pastry."
    scene 73_s59 with dissolve
    mc "*chuckles* You're lucky the well has run dry. I've got nothing left to give."
    scene 73_s60 with dissolve
    r "Yeah, yeah. Don't sound so proud of yourself."
    r "Ugh. I stink. And I'm sticky everywhere."
    r "I'm taking a bath. A long, long, scalding hot bath."
    scene 73_s59 with dissolve
    if not mc_sub:
        call screen scene73_choice02 with dissolve
    else:
        jump scene73_choice02_op2

label scene73_choice02_op1:
    $ mc_reb_dominated = True
    mc "Hold on. I'm not done. I still have something I need to do."
    scene 73_s61 with dissolve
    r "Come on, [mc]! I'm really tired!"
    scene 73_s62 with dissolve
    mc "Take off your clothes. All of them."
    scene 73_s61 with dissolve
    r "M-My clothes, but—"
    scene 73_s62 with dissolve
    mc "No but's. Now."
    r "..."
    scene 73_s64 with Fade(1.0,1.0,1.0)
    r "There. And? What do you possibly want now?"
    scene 73_s63 with dissolve
    mc "I want you to prostrate yourself. Forehead to the floor. Before me."
    scene 73_s64 with dissolve
    r "Oh, screw you. T-That's humiliating!"
    r "Besides, this isn't part of the rules!"
    scene 73_s63 with dissolve
    mc "Screw the rules. I'm asking you this as your husband. As your man."
    r "..."
    scene 73_s64 with dissolve
    r "Prostrate myself, though? Seriously?"
    scene 73_s63 with dissolve
    mc "Yes. It is. I need you to understand who you belong to."
    r "..."
    scene 73_s65 with Dissolve(2.0)
    perception "With reluctance, she gets down on her hands and knees, then lowers her entire body. Her forehead presses against the cold wood. Her back forms a vulnerable curve, and her breasts sway and press against the floor."
    r "..."
    mc "Good girl."
    mc "Now, tell me. Who do you belong to?"
    r "{size=30}...You.{/size}"
    mc "I didn't hear that."
    r "...You!"
    mc "Mhm. And who is your body for?"
    r "I-It's yours! My... my body is yours. To use, my husband."
    mc "Good. I'm glad we've made that clear."
    mc "You may stand up."
    scene 73_s64 with Dissolve(2.0)
    r "*scoff* Happy? Is your ego sufficiently stroked?"
    scene 73_s63 with dissolve
    mc "Very. Now go and get yourself cleaned up, princess."
    scene 73_s64 with dissolve
    r "Y-Yes..."
    scene 73_s63 with dissolve
    scene 73_s66 with Fade(0.5,0.5,0.5)
    call screen scene73_choice03 with dissolve

label scene73_choice02_op2:
    mc "Go ahead. You've earned it."
    $ renpy.end_replay()
    scene 73_s60 with dissolve
    r "Thank you."
    scene 73_s59 with dissolve
    scene 73_s70 with Fade(0.5,0.5,0.5)
    mc "Agh! (Shit... I think I might have actually broken something. My groin hurts...)"
    jump scene74

label scene73_choice03_op1:
    play sound "sound_effects/slap06.mp3"
    scene 73_s67 with vpunch
    r "Ahh!"
    scene 73_s68 with dissolve
    r "Hey! You're getting {i}waaaay{/i} too comfortable with me! I'm supposed to be a princess!"
    scene 73_s69 with Dissolve(1.0)
    mc "And?"
    mc "You got something to say about it?"
    r "..."
    mc "*chuckles* Thought so."
    $ renpy.end_replay()
    jump scene73_choice03_op2

label scene73_choice03_op2:
    $ renpy.end_replay()
    scene 73_s70 with Dissolve(1.0)
    mc "Agh! (Shit... I think I might have actually broken something. My groin hurts...)"
    jump scene74

label scene74:
    scene 74_s1 with Fade(1.5,1.0,2.0)
    play music "nature.mp3" fadein 1.0 loop
    ""
    scene 74_s2 with Fade(0.5,0.5,1.5)
    if mc_maia_left and mc_reb_breakup:
        mc "(Great... Both Maia and Rebecca are now mad at me.)"
        mc "*sigh* (...Guess I can ask Avery for work to take my mind off this mess.)"
        jump scene74_3

    elif mc_reb_breakup:
        mc "(Where the hell did you go, Maia?)"
        mc "(And Rebecca won't even look at me...)"
        mc "*sigh* (...Might as well ask Avery if there's any work.)"
        jump scene74_3

    elif mc_maia_left:
        mc "(Still nothing new from Avery...)"
        mc "(Guess I'll hang out with Becky for now.)"
        jump scene74_2

    else:
        mc "(Where the hell did you go, Maia?)"
        mc "(...Guess I'll hang out with Becky for now.)"
        jump scene74_2

label scene74_2:
    $ mc_reb_told_mc_maia_lost = True
    stop music fadeout 2.0 
    scene 74_s3 with Fade(1.5,1.0,1.0)
    play music "fire.mp3" fadein 2.0 volume 0.3 loop
    mc "Hey. Do you know where Maia's been? Haven't seen her in a while."
    scene 74_s4 with dissolve

    if mc_maia_left:
        r "Why do you care? You two aren't together anymore."
        scene 74_s3 with dissolve
        mc "Still. It was... nice. Seeing her smile in the hallways, or hearing her hum while she worked. She made this place feel more alive."
        scene 74_s4 with dissolve
        r "Well, if you must know, she's been going out to the market district by herself lately."
        r "She told me she wants to be stronger. I told her she's perfectly fine as she is, but she wouldn't listen."
        scene 74_s3 with dissolve
        mc "Hmm... I just hope she's being safe out there."
        mc "It still feels... off. Not like something she'd do on a whim."

    elif not mc_maia_left:
        r "Hmm? Oh, she's started making trips to the market district on her own."
        r "She told me she wants to be stronger. I told her she's perfectly fine as she is, but she wouldn't listen."
        scene 74_s3 with dissolve
        mc "Seriously? Why didn't she tell me? I would have gone with her."
        scene 74_s4 with dissolve
        r "I'm guessing that's the point. She's doing this {i}for{/i} you. She doesn't want to be the helpless girl you have to protect all the time."
        scene 74_s3 with dissolve
        mc "*sigh* Oh, Maia... You don't have to prove anything."
        mc "Hmm... It feels... off. Not like something she'd do on a whim."
        mc "I hope she's being safe."
        
    scene 74_s4 with dissolve
    mc "..."
    r "..."
    scene 74_s3 with dissolve
    mc "For fuck's sake! Why isn't she calling for me! What's the point of having a 'steward' if you never steward anything?!"
    scene 74_s4 with dissolve
    r "What are you on about now? My aunt?"
    scene 74_s5 with dissolve
    mc "Yes, your aunt! I'm not used to just sitting around on my ass all day! I need something to do!"
    r "Then why are you complaining to me? If you're so desperate, go down to her office and ask her yourself."
    mc "You know what? You're right."
    r "When am I ever not~?"
    stop music fadeout 2.0 
    jump scene74_3

label scene74_3:
    stop music fadeout 2.0 
    scene 74_s6 with Fade(1.5,1.0,1.0)
    play music "fire.mp3" fadein 1.0 loop
    avery "What's the situation?"
    scene 74_s7 with dissolve
    guard "Unchanged, my lady. The Mast bandits are still demanding the same ransom for the captured merchants. Our soldiers are trying to negotiate as best they can, but they're stalling."
    scene 74_s6 with dissolve
    mc "(Ransom? A negotiation? Sounds like work.)"
    mc "*ahem* Lady Avery?"
    avery "Keep them talking. We can afford the sum; it's cheaper than losing the trade route over a cartload of cheap weapons. Make it happen."
    scene 74_s8 with dissolve
    guard "On it, my lady."
    scene 74_s9 with Dissolve(1.3)
    avery "Ah, [mc]. Is there something you needed? I'm rather busy."
    scene 74_s10 with dissolve
    mc "I heard. It sounds like something I could help with. Send me."
    scene 74_s9 with dissolve
    avery "That won't be necessary. My guards are handling it. It's a delicate matter."
    scene 74_s10 with dissolve
    mc "Are you sure? I'm completely free. And 'delicate' sometimes just needs a firmer hand."
    scene 74_s9 with dissolve
    avery "I am sure."
    scene 74_s10 with dissolve
    mc "..."

    if mc_play_bgame:
        scene 74_s9 with dissolve
        avery "Listen, if you're here to ask for my permission to enter my niece, the answer is no. My sister was very clear."
        scene 74_s10 with dissolve
        mc "What?! Why would you assume that?"
        scene 74_s9 with dissolve
        if rnr_win:
            if not mc_noprize_bgame:
                avery "The maids. They reported you spent the entirety of yesterday in her room. The entire day, [mc]. It doesn't take a scholar to connect the dots."
                avery "Thankfully, they never heard any moans, so I assume she's still pure."
            elif mc_noprize_bgame:
                avery "The maids. They reported you spent some time in her room yesterday."
                avery "Thankfully, they never heard any moans, so I assume she's still pure."
        else:
            avery "The maids. They reported you spent some time in her room yesterday."
            avery "Thankfully, they never heard any moans, so I assume she's still pure."

        scene 74_s10 with dissolve
        mc "Oh... Right. Nothing escapes them, huh?"
        mc "Well, you're wrong. I'm just here to ask for something to do. I'm going crazy."

    scene 74_s9 with dissolve
    avery "There isn't anything for you right now, [mc]. Just return to your quarters and stay there until I have something that suits you."
    scene 74_s10 with dissolve
    mc "*sigh* Fine."

    if mc_feet_massage_avery_toes:
        mc "And listen, about what happened yesterday morning in the garden..."
        scene 74_s12 with dissolve
        avery "Stop."
        avery "Just... Let's not mention it. Ever again. It was a moment of... profound impropriety. It's best we forget it."
        scene 74_s11 with dissolve
        mc "...Alright. Yeah. Sure."

    if not mc_reb_told_mc_maia_lost:
        $ mc_avery_told_mc_maia_lost = True
        mc "One last thing. Do you know where Maia is? I haven't seen her in a while."
        scene 74_s9 with dissolve
        avery "...I don't."
        scene 74_s10 with dissolve
        mc "You're sure? Shouldn't you know where your staff are? Nothing leaves these walls without being documented."
        scene 74_s9 with dissolve
        avery "I'm really busy, [mc]. I don't have time to keep track of every maid in the castle."
        avery "It would be better if you forgot about her."
        scene 74_s10 with dissolve
        mc "Forget about her? What the hell are you talking about?"
        scene 74_s9 with dissolve
        avery "Watch. Your. Language."
        scene 74_s10 with dissolve
        impulse "How long will you stay dormant like this? A servant to people who don't care about you?"
        mc "*sigh* ...What did you mean?"
        scene 74_s9 with dissolve
        avery "It is nothing. You may leave. Now."
        scene 74_s10 with dissolve
        mc "She better be safe."
        avery "..."
        stop music fadeout 2.0 

    else:
        $ mc_avery_told_mc_maia_lost = True
        mc "One last thing. Did you know that Maia has been leaving the castle on her own?"
        scene 74_s9 with dissolve
        avery "...I didn't."
        scene 74_s10 with dissolve
        mc "You're sure? Shouldn't you know where your staff are? Nothing leaves these walls without being documented."
        scene 74_s9 with dissolve
        avery "I'm really busy, [mc]. I don't have time to keep track of every maid in the castle."
        avery "It would be better if you forgot about her."
        scene 74_s10 with dissolve
        mc "Forget about her? What the hell are you talking about?"
        scene 74_s9 with dissolve
        avery "Watch. Your. Language."
        scene 74_s10 with dissolve
        impulse "How long will you stay dormant like this? A servant to people who don't care about you?"
        mc "*sigh* ...What did you mean?"
        scene 74_s9 with dissolve
        avery "It is nothing. You may leave. Now."
        scene 74_s10 with dissolve
        mc "She better be safe."
        avery "..."
        stop music fadeout 2.0 

    if mc_reb_breakup or mc_rejected_wedding_reb:
        stop music fadeout 2.0 
        jump scene74_4

    scene 74_s13 with Fade(1.0,1.0,1.5)
    r "So? Did you find purpose?"
    scene 74_s14 with dissolve
    mc "I'm back here, aren't I?"
    scene 74_s13 with dissolve
    r "Tch, too bad."
    r "I suppose that means you'll just have to suffer through spending more time with your beautiful, charming wife. How truly awful for you."
    scene 74_s15 with Dissolve(1.0)
    mc "Becky..."
    scene 74_s16 with dissolve
    r "*laughs* Sorry, sorry. I'll stop."
    scene 74_s17 with Dissolve(1.0)
    mc "*sigh*"

    if quest_witch_amelia_alive_free:
        mc "(Did I forget something?)"
        mc "(The witch! I promised to... Shit.)"
        mc "(Hopefully she didn't go back on her word.)"

    scene 74_s18 with Dissolve(1.0)
    r "You're just going to lie there until something comes up?"
    mc "I guess so. Unless you having something in mind?"
    r "...N-Not really."
    scene 74_s19 with Dissolve(1.0)
    r "Mfhnnnn~"
    mc "You said something?"
    scene 74_s20 with vpunch
    r "Huh?! N-No! I didn't... I didn't say anything!"
    scene 74_s21 with dissolve
    r "I... I just remembered. I need to go to the baths. Right now."
    scene 74_s22 with Dissolve(1.0)
    mc "Sure."
    scene 74_s23 with Fade(1.0,1.0,1.0)
    mc "...She's really taking her time."
    scene 74_s24 with Dissolve(1.0)
    mc "Sheesh, you're finally done? I thought you drowned in there."
    r "..."
    scene 75_s1 with Dissolve(1.5)
    perception "Without saying anything, she begins to untie and step out of her dress right in front of you. She doesn't do it seductively, but with a completely casual tone."
    mc "Uhh, Becky? What are you doing?"
    play sound "sound_effects/clothing_rustle.mp3"
    scene 75_s2 with Dissolve(1.0)
    r "What does it look like? This is my room. I can take off my clothes whenever I want." 
    scene 75_s3 with dissolve
    mc "Sure, but..."
    scene 75_s2 with dissolve
    r "A bath didn't help. So, you're going to give me a massage."
    scene 75_s3 with dissolve
    mc "Didn't help with what?"
    scene 75_s4 with Dissolve(0.7)
    r "Come on. On the bed."
    scene 75_s3 with Dissolve(0.7)
    mc "..."
    scene 75_s5 with Fade(0.5,0.5,0.5)
    r "..."
    mc "Hmm. Something tells me you didn't really shower for an hour."
    r "I did. I just... spent most of the time... you know. Thinking. Touching. I couldn't handle it, to be honest."
    scene 75_s16 with Dissolve(1.0)
    r "Hopefully none of the maids heard all the squelching sounds coming from between my legs..."
    scene 75_s17 with dissolve
    mc "*chuckles* I see. For someone who just had a long bath, you look pretty tense."
    scene 75_s16 with dissolve
    r "A little... I found this old comic that I hid a long time ago. And... I kept reading and touching myself while you were laying right there."
    r "Sorry for doing that without telling you. It's hard having you in my room and not think about... doing it."
    scene 75_s17 with dissolve
    mc "Becky..."
    scene 75_s5 with Dissolve(1.0)
    r "Anyway, I think a massage might take things off my mind."
    mc "On the contrary, I believe—"
    r "[mc]..."
    mc "..."
    call screen scene75_choice01 with dissolve
    mc "You should sleep it off instead."
    r "..."
    mc "Trust me. A massage, especially when you're this horny... it won't help. Not a bit."
    r "*sigh* Maybe you're right..."
    mc "I'll leave you to it, then."
    r "Mhm."
    jump scene74_4


label scene74_4:
    stop music fadeout 2.0 
    scene 53_s39 with Fade(1.0,1.0,1.5)
    mc "*sigh* This room feels like a prison with each day."
    if not mc_maia_left:
        mc "(It just doesn't feel right without you, Maia... I hope you come back soon.)"
    scene 76_s14 with Fade(0.5,0.5,0.5)
    ""
    scene 76_s15 with Fade(1.5,0.5,0.5)
    mc "*sigh* (Can't sleep again.)"
    mc "(It feels suffocating. I need to get some air.)"
    scene 76_s18 with Fade(1.0,1.0,1.5)
    ""
    play music "wind_breakup.mp3" fadein 2.0 volume 0.8 loop
    scene 76_s19 with Fade(0.5,0.5,0.5)
    mc "Unf! (So cold...)"
    scene 76_s22 with Fade(0.5,0.5,0.5)
    mc "Hmm?"
    scene 76_s21 with Dissolve(1.0)
    mc "Are those... cigarettes?"
    call screen scene76_choice01 with dissolve

default scene75_first = True
label scene75:
    if scene75_first:
        $ mc_accept_reb_massage = True
        $ scene75_first = False
        play music "relax.mp3" fadein 2.0 loop
        mc "I'll help you out. Just relax."
        r "*giggles* Thank you~"
        if not interact_indicator:
            $ interact_indicator = True
            call screen interact_tutorial with Dissolve(0.3)
        call screen scene75_choice02 with dissolve

    elif not s75_s5_part2:
        scene 75_s5 with dissolve
        call screen scene75_choice02 with dissolve

    elif s75_s5_part2:
        scene 75_s8 with dissolve
        call screen scene75_choice02 with dissolve

label scene75_choice02_op1:
    $ s75_massage_counter += 1
    $ s75_s5_shoulder = True
    scene 75_s6 with Dissolve(1.0)
    sensation "You place your palms on her upper back, gently kneading the muscles around her shoulder blades. Her skin is incredibly soft and warm under your hands."
    r "Hnn~ Mmm... I should make you do this more often. You have strong hands."
    mc "You think?"
    r "*giggles* I always catch myself staring at your hands. Don't really know why."
    if s75_massage_counter == 2:
        r "Go lower now."
        $ s75_s5_part2 = True
    jump scene75

label scene75_choice02_op2:
    $ s75_massage_counter += 1
    $ s75_s5_lback = True
    scene 75_s7 with Dissolve(1.0)
    r "Ahhnm... Just like that~"
    perception "With her arms at her sides, her large breasts spill slightly from her sides."
    r "Mhnnn~"
    mc "Feeling good?"
    r "Mhhmmm!"
    if s75_massage_counter == 2:
        r "Go lower now."
        $ s75_s5_part2 = True
    jump scene75

label scene75_choice02_op3:
    $ s75_massage_counter += 1
    $ s75_s5_butt = True
    scene 75_s9 with Dissolve(1.0)
    r "Ahn~! D-Don't squeeze too hard..."
    perception "You begin to knead the soft, full curves of her ass, her skin molds perfectly to your hands like warm, living clay."
    mc "What a huge ass... What did you eat to get this plump?"
    scene 75_s10 with Dissolve(1.0)
    r "You mean it?"
    mc "Damn right I do."
    r "Hmph. Kiss it then. If you... truly think so."
    mc "...As you wish."
    play sound "se_sfx/blowjob/kiss4.mp3" 
    scene 75_s11 with Dissolve(1.0)
    perception "You lean down, bringing your face close to her skin, which carries the faint, clean scent of her soap. You press a soft kiss to her left cheek."
    r "Hnnm~ ...That's enough."
    jump scene75

label scene75_choice02_op4:
    $ s75_massage_counter += 1
    $ s75_s5_thighs = True
    scene 75_s14 with Dissolve(1.0)
    perception "Her thigh shifts slightly under your touch, her breathing growing heavier as your hands gets closer to her crotch."
    r "Ahh~ you really are devoted, aren't you? I can feel it in your touch..."
    scene 75_s15 with Dissolve(1.0)
    r "Mhnnn~ Yeeesss~!"
    r "Dammit! I can feel my panties getting wet again. I {i}hate{/i} that I'm this sensitive... Or maybe it's just because of you, hm?"
    jump scene75

label scene75_choice02_op5:
    $ s75_massage_counter += 1
    $ s75_s5_feet = True
    scene 75_s12 with Dissolve(1.0)
    r "Oh? Going for my feet, are you?"
    perception "You kneel at the foot of the bed, getting your face as close as possible to her soles. You take one foot in your hands and begin massaging her arch with devotion."
    scene 75_s13 with Dissolve(1.0)
    r "Ahh~ Oh, my... I see you're giving them- Ahn~ extra special attention."
    sensation "The sight of her bare feet, so perfectly and vulnerably presented to you, sends a shiver of arousal straight down your spine. Your cock perks up insistently against your pants."
    if mc_feet_massage_avery_toes:
        impulse "You should shove her toes in your mouth like you did with Avery's."
        mc "..."
    jump scene75


label scene75_2:
    mc "Feeling relaxed yet?"
    scene 75_s16 with Dissolve(1.0)
    r "Hey, [mc]..."
    scene 75_s17 with dissolve
    mc "What's up?"
    scene 75_s16 with dissolve
    r "I... I know we shouldn't. My mother would have your head... but..."
    scene 75_s17 with dissolve
    mc "..."
    scene 75_s16 with dissolve
    r "Give it to me."
    r "I... I can't wait any longer. I need to feel you inside me."
    r "Please."
    scene 75_s17 with dissolve
    call screen scene75_choice03 with dissolve

label scene75_3:
    mc "We really shouldn't, Becky."
    mc "Your mother promised me not to. I can't go back on my word."
    scene 75_s18 with dissolve
    r "..."
    scene 75_s19 with dissolve
    r "Forget it."
    scene 75_s18 with dissolve
    mc "Becky..."
    scene 75_s19 with dissolve
    r "No, I understand. I really do. Just forget I said anything."
    scene 75_s18 with dissolve
    mc "Good. I'll... see you tomorrow. You should sleep it off."
    r "Mhm."
    jump scene74_4

label scene75_4:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene6_p6_replay:
        $ persistent.scene6_p6_replay = True

    $ mc_accept_reb_sex = True
    play sound "se_sfx/blowjob/kiss5.mp3" 
    scene 75_s20 with Dissolve(1.0)
    mc "I love you."
    scene 75_s21 with Dissolve(1.0)
    r "*giggles* I know."
    r "Barely got out of the baths and my panties are already soaked. *chuckles* What the hell are you doing to me?"
    scene 75_s22 with Dissolve(1.0)
    mc "Let's see just how soaked you are for me..."
    perception "As you pull them down, the musky scent of her arousal hits you instantly. Her body is tense with anticipation, a slight, involuntary twitch clenching her anus as it's exposed to the cool air."
    scene 75_s23 with dissolve
    r "C-Can you... kiss it?"
    mc "You want me to kiss your pussy?"
    r "Mhm..."
    call screen scene75_choice04 with dissolve

label scene75_choice04_op1:
    $ mc_kiss_reb_pussy = True
    scene 75_s33 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    perception "Without a second thought, you lean forward and press your mouth firmly against her pussy in a deep, lingering kiss. Her entire body jolts at the contact."
    r "Mhmmmn~!"
    r "Y-Yes! Make out with my pussy! Hnn~!"
    mc "Mmm..."
    play sound "se_sfx/sex/touch3.mp3" 
    scene 75_s34 with dissolve
    r "Ahnnn~ You're too good at this... D-Did you do this to another girl before?"
    mc "Mfhmmm..."
    r "Actually, don't answer that. Just keep licking my slit. Don't stop untill I tell you!"
    play sound "se_sfx/sex/touch4.mp3" 
    scene 75_s35 with dissolve
    sensation "The intoxicating scent and the soft, wet folds pressed against your mouth are overwhelming."
    scene 75_s30 with dissolve
    r "Ahnn~! Yes, that's more like it! Push your tongue deep in my pussy!"
    scene 75_s31 with dissolve
    r "I'm... I'm!"
    play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3" 
    scene 75_s32 with vpunch
    r "AAAHHHHHH!"
    mc "Mghm?!"
    scene 75_s34 with dissolve
    r "Hahh... hah..."
    mc "Mhmm..."
    r "S-Stop... It's... hahh... too sensitive now..."
    jump scene75_5
    
label scene75_choice04_op2:
    $ mc_kiss_reb_anus = True
    scene 75_s24 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    perception "Without a second thought, you lean forward and press your mouth firmly against her puckering anus in a deep, lingering kiss. Her entire body jolts at the contact."
    scene 75_s27 with dissolve
    r "Ahh! What in the—"
    scene 75_s28 with dissolve
    r "My Gods! You... You kissed my asshole! You absolute degenerate!"
    scene 75_s29 with dissolve
    mc "Mmmm..."
    scene 75_s28 with dissolve
    r "Just how depraved are you?! To do it so willingly..."
    scene 75_s30 with dissolve
    r "But... It's somehow... really exciting~ Don't stop. Push your tongue in there! I want you to make out with my butthole!"
    scene 75_s24 with dissolve
    mc "Mhmm..."
    play sound "se_sfx/sex/touch2.mp3" 
    scene 75_s25 with dissolve
    sensation "You obey, your tongue probing past her tight ring. It's soft and warm. Your saliva makes the passage slicker, allowing you to delve deeper with each flick and swirl."
    r "Mghnmm! ...Fuck! It feels so weird, but... I kinda love it!"
    perception "She shudders violently with every stroke of your tongue, her hips pushing back against your face. Her body writhes and jerks uncontrollably."
    scene 75_s31 with dissolve
    r "Mhmm! Why does it feel so good!? What are you doing to me?"
    play sound "se_sfx/sex/touch4.mp3" 
    scene 75_s25 with dissolve
    jump scene75_5

label scene75_5:
    r "I-I can't take it anymore! Stop! Please, stop!"
    scene 75_s37 with Dissolve(1.0)
    mc "Something wrong? Did I hurt you?"
    scene 75_s36 with dissolve
    r "N-No! I need it! I need you inside me, now! {i}Please!{/i}"
    scene 75_s37 with dissolve
    mc "*chuckles* No need for a little more foreplay? I was just getting started."
    scene 75_s36 with dissolve
    r "Can't you tell I'm ready?! I'm soaked! Just... please."
    if mc_kiss_reb_pussy:
        r "Just be... gentle. In case you didn't know, it's my first time."
        scene 75_s37 with dissolve
        mc "I'd never hurt you, Becky. I'll be gentle."
        stop music fadeout 2.0 
        jump s75_vaginal
    elif mc_kiss_reb_anus:
        scene 75_s37 with dissolve
        mc "Alright, alright. But..."
        mc "Where do you want me? You seemed to be enjoying my tongue... elsewhere."
        scene 75_s38 with dissolve
        r "Where? You mean... my...?"
        r "W-Wouldn't that hurt, though? I've read stories..."
        scene 75_s39 with dissolve
        mc "I'll be gentle. I'd never hurt you, Becky. I promise."
        scene 75_s38 with dissolve
        r "Umm... It's called anal, right?"
        scene 75_s39 with dissolve
        mc "Mhm. So, what's your verdict? Do you want to try?"
        scene 75_s38 with dissolve
        r "...Alright. But you have to be gentle!"
        scene 75_s39 with dissolve
        call screen scene75_choice05 with dissolve

label scene75_choice05_op1:
    mc "I'll be gentle."
    stop music fadeout 2.0 
    jump s75_anal

label scene75_choice05_op2:
    mc "Actually, since it's your first time... we should do it properly."
    scene 75_s38 with dissolve
    r "T-That's a good idea..."
    stop music fadeout 2.0 
    jump s75_vaginal

image s75_anim1_p = Movie(play="images/4_chapter3/scene75/75_anim1_p.webm", loop=True)
image s75_anim1_a = Movie(play="images/4_chapter3/scene75/75_anim1_a.webm", loop=True)

image s75_anim2_p = Movie(play="images/4_chapter3/scene75/75_anim2_p.webm", loop=True)
image s75_anim2_a = Movie(play="images/4_chapter3/scene75/75_anim2_a.webm", loop=True)

image s75_anim3_p = Movie(play="images/4_chapter3/scene75/75_anim3_p.webm", loop=True)
image s75_anim3_a = Movie(play="images/4_chapter3/scene75/75_anim3_a.webm", loop=True)

image s75_anim4 = Movie(play="images/4_chapter3/scene75/75_anim4.webm", loop=True)

label s75_anal:
    $ mc_reb_anal = True
    scene 75_s51 with Fade(1.0,0.5,0.5)
    perception "You carefully position yourself, the head of your cock resting lightly against her tight rim. At the first touch, her entire body jolts with a sharp gasp."
    r "C-Careful...!"
    play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
    scene 75_s52 with Dissolve(1.5)
    sensation "You press forward slowly, and with a soft, yielding resistance, you penetrate her. The shocking heat and tightness instantly envelops your shaft, a sensation so intense it steals your breath."
    r "Hnnngg! Ahh! Ahhh! Ahnnn!"
    mc "It's in."
    show s75_anim1_a with dissolve
    r "A-Alright! Just... start moving— Ahn! S-Slowly! Oh, Gods, slowly!"
    sensation "You begin to move in a slow rhythm. With each thrust, her body gradually accepts you, her rectum molding perfectly to your shape."
    r "Ahnn~! Fuck! Dammit! What is this?!"
    mc "Does it hurt?"
    r "N-No! Don't stop! Keep going~! Gods!"
    r "I feel it in my stomach... It's making me feel so... full! Ahh!"
    mc "You're so fucking tight."
    r "Nghn!"
    show s75_anim2_a with dissolve
    hide s75_anim1_a
    perception "You thrust deep into her tight backdoor and a powerful shudder courses through her frame, from her clenched toes to her trembling shoulders."
    mc "Ahhn... How does it feel? Having a cock up your ass?"
    r "It's w-weird~! Your penis is somehow brushing the weak spot in my womb."
    mc "Good. That means you'll learn to love it even more."
    r "Hahhn~!"
    mc "Let's try a different position. I want to see your face."
    r "H-Huh? I don't know if I can move..."
    mc "Come on, turn over. Onto your back."
    r "Ahhn... Alright, just... help me."
    scene 75_s55 with Fade(0.5,0.5,0.5)
    r "L-Like this?"
    mc "You are so fucking beautiful."
    show s75_anim3_a with dissolve
    hide s75_anim2_a
    sensation "You sink into her again. This time, her cry is not of shock, but of pure ecstasy. Her rectum, now accustomed to you, welcomes you easily, a hot, velvety sheath gripping you perfectly."
    r "Ahhnn~! [mc]! You're... you're destroying my butthole!"
    mc "That's right."
    r "Mhnn~! Mghhmm~! You're... so... fucking... deep~! I can feel you in my throat!"
    sensation "Her body begins to spasm around you, losing all control. Her muscles clench intensely with every time you pull out, a rhythmic, milking pressure that seems desperate to keep you buried inside her."
    mc "Come over here!"
    r "Huh?"
    show s75_anim4 with Dissolve(1.0)
    hide s75_anim3_a
    r "Mfhmn!"
    mc "Mhnnnn..."
    r "*slurp* Mhfhnnn~!"
    call screen scene75_choice06 with dissolve

label s75_vaginal:
    $ mc_reb_vaginal = True
    scene 75_s53 with Fade(1.0,0.5,0.5)
    perception "You position yourself at her entrance, the head of your cock resting against her slick, heated folds. She shudders at the contact, a sharp, anticipatory gasp escaping her."
    r "P-Please...!"
    play sound "se_sfx/sex/sex4.mp3" 
    scene 75_s54 with Dissolve(1.5)
    sensation "You press forward slowly, and with one smooth, wet motion, you sink into her. The incredible heat and welcoming tightness envelops your cock completely."
    r "Hnnngg~ Ahh! Ahhh! Ahnnn~"
    mc "You feel... incredible."
    show s75_anim1_p with dissolve
    r "A-Alright! Just... start moving— Ahn! S-Slowly! Oh, Gods, slowly!"
    sensation "You begin to move in a deep, slow rhythm. Her body arches to meet each thrust, her inner walls clenching around you in a perfect, wet embrace."
    mc "Does it feel good?"
    r "Y-Yes! Don't stop! Keep going~! Gods!"
    r "I feel you so deep... It's making me feel so... full. Ahh!"
    mc "God... You're steaming hot in there!"
    r "Hnn~ I-I told you! It's been like that for a while now. I didn't know what to do."
    mc "Hahhn... You're in heat. As your husband, I'll be taking care of it from now on."
    r "Y-Yes~ Please do so~!"
    show s75_anim2_p with dissolve
    hide s75_anim1_p
    perception "You thrust deep into her warm pink pussy and a powerful shudder wracks her frame, from her clenched toes to her trembling shoulders."
    r "Ahhn! Please, please put out this fire in my womb~!"
    mc "Do you want me to go deeper?!"
    r "Yes, yes, yes! {i}Deeeepeer!{/i}"
    r "Mhnng~! I can't think straight anymore."
    mc "Let's try a different position. I want to see your face."
    r "H-Huh? I don't know if I can move..."
    mc "Come on, turn over. Onto your back."
    r "Ahhn... Alright, just... help me."
    scene 75_s56 with Fade(0.5,0.5,0.5)
    r "L-Like this?"
    mc "You are so fucking beautiful."
    show s75_anim3_p with dissolve
    hide s75_anim2_p
    sensation "You sink into her again, face to face. Her cry this time is one of pure ecstasy. Her pussy, now more accustomed to you, moves in perfect rhythm, her warmth gripping you like a velvet glove."
    r "Ahhnn~! [mc]! You're... you're hitting so deep!"
    mc "That's right."
    r "Mhnn~! Mghhmm~!"
    sensation "Her body begins to convulse around you, losing all control. Her inner muscles clench and flutter with every thrust, a rhythmic, milking pressure that seems desperate to pull you even deeper."
    mc "Do you want me to put a baby in your womb?"
    r "Huhh!? N-No..."
    mc "You don't sound sure."
    r "I... I don't... We can't. Not... Hahn~! Yet..."
    mc "Come over here!"
    r "Huh?"
    show s75_anim4 with Dissolve(1.0)
    hide s75_anim3_p
    r "Mfhmn!"
    mc "Mhnnnn..."
    r "*slurp* Mhfhnnn~!"
    call screen scene75_choice06 with dissolve

label scene75_choice06_op1:
    scene black with Dissolve(0.3)
    if mc_reb_vaginal:
        show s75_anim1_p with dissolve
        sensation "Your hand grips her hip as you push into her wet heat, her slickness making the initial glide effortless before her tightness grips you, welcoming you deep inside."
        r "Don't stop... please."
        perception "Her head is bowed, her entire body rocking forward with the force of your thrusts, each one met with a soft, yielding gasp from her."
    elif mc_reb_anal:
        show s75_anim1_a with dissolve
        sensation "Sweat drips from your brow as you press against her tight ring, feeling it slowly yield and stretch to accommodate your throbbing cock with a searing, tight embrace."
        r "Nghnnn~! My ass is on fire!"
    call screen scene75_choice06 with dissolve

label scene75_choice06_op2:
    scene black with Dissolve(0.3)
    if mc_reb_vaginal:
        show s75_anim2_p with dissolve
        perception "Your cock disappears into her, each retreat revealing a glistening, pink glimpse of her pussy before you plunge back into the welcoming, clenching warmth."
        mc "Look at you taking me... Your pussy is making my shirt wet."
        r "Hnn~! I'm sorry!"
    elif mc_reb_anal:
        show s75_anim2_a with dissolve
        r "You're so deep!"
        mc "And you love it, don't you?"
        desire "Her back muscles flex and ripple with each thrust, a beautiful, strained symphony of power and submission playing out just for you."
    call screen scene75_choice06 with dissolve

label scene75_choice06_op3:
    scene black with Dissolve(0.3)
    if mc_reb_vaginal:
        show s75_anim3_p with dissolve
        sensation "Her inner walls squeeze around your cock in a silent, desperate plea."
        r "Hanh~! Hahh~ Gahh~"
        mc "I love seeing you like this, your mind melting from my cock."
    elif mc_reb_anal:
        show s75_anim3_a with dissolve
        sensation "You change the angle as you press into the incredible, tight pressure of her rectum, a slow, burning stretch that makes her tear up in pleasure."
        r "[mc]! HAAhnn! Faauck~!"
    call screen scene75_choice06 with dissolve

label scene75_choice06_op4:
    scene black with Dissolve(0.3)
    if mc_reb_vaginal:
        show s75_anim4 with dissolve
        sensation "With your mouths fused together, you push inside her, the dual sensations of her soft tongue and her wet, clutching pussy creating a dizzying sensation of pure, intimate pleasure."
        r "Hnn... I can't breath~! *slurp* *lick*"
    elif mc_reb_anal:
        show s75_anim4 with dissolve
        sensation "As your tongue explores her mouth, you slowly fill her other forbidden entrance, the intimate kiss masking her sharp intake of breath as her body surrenders to the deep, full feeling."
        r "Ahnnmm~! *slurp* *lick*"
    call screen scene75_choice06 with dissolve

label scene75_choice06_op5:
    mc "Becky! I'm... I'm close!"
    if mc_reb_vaginal:
        r "Faucck! Y-You're going to make me come again~! I can't take it!"
        r "Just don't finish inside me! I-I can't be pregnant now."
    elif mc_reb_anal:
        r "Faucck! Y-You're going too fast~! I can't think!"
        r "You're breaking me apart!"
    call screen scene75_choice07 with dissolve

label scene75_choice07_op1:
    if mc_reb_anal:
        scene 75_s46 with Dissolve(1.0)
        perception "You pull out of her tight rectum in a rush and lift yourself over her face."
        r "W-What are you—"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 75_s47 with dissolve
        mc "Ughn!"
        sensation "You release on her, thick spurts of hot cum splashing across her cheeks and lips until her face is completely covered."
        r "Ah!"
        scene 75_s48 with dissolve
        r "You... you finished on my face."
        mc "Yeah... I wasn't sure if you'd want me to fill your ass with it."
        r "I-It's alright... And my Gods... that's a lot..."
    elif mc_reb_vaginal:
        scene 75_s46 with Dissolve(1.0)
        perception "You pull out of her in a rush and lift yourself over her face."
        r "W-What are you—"
        play sound "se_sfx/blowjob/facial2.mp3" 
        scene 75_s47 with dissolve
        mc "Ughn!"
        sensation "You release on her, thick spurts of hot cum splashing across her cheeks and lips until her face is glistening."
        r "Ah!"
        scene 75_s48 with dissolve
        r "Hahh... My Gods... that's a lot..."
    $ renpy.end_replay()
    jump scene75_6

label scene75_choice07_op2:
    if mc_reb_anal:
        $ reb_total_cum_in_ass += 1
        $ mc_reb_anal_inside = True
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene 75_s45 with vpunch
        sensation "You drive into her one last time, hilt-deep, and release. Thick, hot spurts flood the deepest part of her colon, filling her completely. The feeling of your release triggers a violent, convulsing climax in her."
        r "Gaahhhh~!"
        mc "Ugh! Becky!"
        play sound "se_sfx/sex/sex_cum6.mp3" 
        scene 75_s43 with vpunch
        sensation "Her walls come crashing down on you in a final, intense series of spasms, wringing every last drop from you, urging you to empty yourself completely."
        r "Hahh... hah... Oh, Gods..."
        play sound "se_sfx/sex/touch2.mp3" 
        scene 75_s44 with dissolve
        r "[mc], that was... Ahhnn..."
        r "I can't believe we did that. In my ass..."
        r "Hopefully I don't get addicted to having your cock in my ass... I'll never get anything done."
        mc "*chuckles* Don't count on it. I'll be sure to train this perfect tight hole to my liking."
        r "Hnnn..."
        r "Oh! Your seed... it keeps pooling out. Quick, get me a cloth or something before it drips on the mattress!"
        if bonus_scene1_open:
            call screen bonus_scene1 with dissolve
        mc "I think it's a little too late for that. But alright, Your Highness. Your wish is my command."

    elif mc_reb_vaginal:
        $ reb_total_cum_in_pussy += 1
        $ mc_reb_vaginal_inside = True
        mc "Ugh... Becky... I'm really sorry!"
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene 75_s45 with vpunch
        sensation "You drive into her one last time, as deep as possible, and release. Thick, hot spurts flood her uterus, the intimate warmth triggering a violent, convulsing climax in her that matches your own."
        r "Gaaahhhh~! [mc]!"
        play sound "se_sfx/sex/sex_cum5.mp3" 
        if persistent.xray_mode:
            scene 75_s41_xray1 with vpunch
            sensation "Her walls contract around you in wave after wave of intense spasms, milking every last drop from you, urging you to empty yourself completely within her."
            r "Hahh... hah... Oh, Gods... You finished inside me!?"
            r "Oh no, no, no, no! Pull out!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene 75_s42_xray2 with Dissolve(1.0)
        else:
            scene 75_s41 with vpunch
            sensation "Her walls contract around you in wave after wave of intense spasms, milking every last drop from you, urging you to empty yourself completely within her."
            r "Hahh... hah... Oh, Gods... You finished inside me!?"
            r "Oh no, no, no, no! Pull out!"
            play sound "se_sfx/sex/touch2.mp3" 
            scene 75_s42 with Dissolve(1.0)
        call pregnancy_check_reb from _call_pregnancy_check_reb 
        mc "Hey, hey! Calm down."
        r "W-What are we going to do now?!"
        mc "Just calm down. It's gonna be fine."
        mc "Even if you got pregnant, nothing will show until we're way off into our marriage."
        r "A-Are you sure!?"
        mc "I am. You mother will be here soon, right?"
        r "I... I think so?"
        mc "Then there's nothing to worry about. She'll never find out."
        r "*sigh* Alright. Good..."
        mc "*chuckles* You're leaking."
        r "Oh! Your seed... it keeps pooling out. Quick, get me a cloth or something before it drips on the mattress!"
        if bonus_scene1_open:
            call screen bonus_scene1 with dissolve
        mc "I think it's a little too late for that. But alright, Your Highness. Your wish is my command."
    $ renpy.end_replay()
    jump scene75_6

image bonus_reb_v = Movie(play="images/bonus_scene/reb_bonus1/bonus_reb_v.webm", loop=True)
image bonus_reb_a = Movie(play="images/bonus_scene/reb_bonus1/bonus_reb_a.webm", loop=True)
image bonus_reb2 = Movie(play="images/bonus_scene/reb_bonus1/bonus_reb2.webm", loop=True)
label bonus_scene1:
    mc "Hold on, Becky. I didn't say that I was finished."
    r "S-Sorry?"
    mc "See that? My cock is still rock solid."
    r "Seriously!? After all that...?"
    mc "You do this to me."
    r "...Alright. I'm... I'm feeling too good to stop now."
    r "So... don't stop! I need more~ Please, [mc]."
    mc "*chuckles* Your wish is my command."
    call screen bonus_scene1_sex0 with dissolve

default bonus_scene1_vaginal_first = False
default bonus_scene1_anal_first = False
label bonus_scene1_vaginal:
    $ bonus_scene1_vaginal = True
    $ bonus_scene1_anal = False
    $ bonus_scene1_pov = False
    scene black with Dissolve(0.3)
    show bonus_reb_v with dissolve
    if not bonus_scene1_vaginal_first:
        $ bonus_scene1_vaginal_first = True
        sensation "You thrust back into her steaming hole. Hot, slick, impossibly tight after the first round. Her walls flutter around you instantly, still pulsing from her orgasm."
        r "Hnnmmmnngh~! Y-yes~! So deep... filling me again~"
        r "It's... it's too much... I feel so tired, but I don't want you to stop."
        mc "You're still so tight... like you're trying to keep me inside forever."
        r "I do~! I want you to stay... buried inside me."
        r "Harder... please... I need to feel you everywhere..."
        sensation "Her juices coat you completely, wet sounds filling the room with every thrust. She clenches rhythmically, pulling you deeper."

    else:
        sensation "You slide back in effortlessly, her pussy already soaked and greedy, walls fluttering like they remember exactly how you feel."
        r "Oh Gods~! Yes... right back where you belong~!"
        r "I've been aching for this... dreaming about you stretching me."
        mc "The mattress is basically drenched now. *laughs* I don't think we can sleep on it today."
        r "I don't care anymore! Don't hold back... breed me like you own me... like I'm yours!"
        sensation "She rolls her hips in perfect rhythmm, meeting every thrust, body trembling with need."
    call screen bonus_scene1_sex with dissolve

label bonus_scene1_anal:
    $ bonus_scene1_vaginal = False
    $ bonus_scene1_anal = True
    $ bonus_scene1_pov = False
    scene black with Dissolve(0.3)
    show bonus_reb_a with dissolve
    if not bonus_scene1_anal_first:
        $ bonus_scene1_vaginal_first = True
        sensation "You press against her tight rear entrance. Slow at first, letting her adjust. She gasps sharply as the head pops past the ring, then sinks in inch by inch."
        r "Ahhn~! It's... it's so big... you're stretching me!"
        mc "Relax, you're taking it so well."
        r "It hurts... but... Gods, it feels good too... keep going~"
        r "Deeper! please... I want to feel you in my stomach."
        sensation "Her ass grips you like a vice, hot and tight, fluttering as you push deeper. She whimpers with every inch."

    else:
        sensation "You press in again, this time she relaxes almost instantly, pushing back eagerly, taking you halfway in one smooth motion."
        r "Yesss~! Right back inside my ass~"
        mc "Look how easily your asshole takes my cock."
        mc "Have you been practicing before?"
        r "Nghnn~! No! I never play back there... It's forbidden~!"
        sensation "She rocks back hard, taking you to the hilt, walls clenching rhythmically, already dripping from her pussy onto the mattress."
        r "Ruin my ass harder! Hnngg... please~! I need to feel you come inside."
    call screen bonus_scene1_sex with dissolve

label bonus_scene1_pov:
    $ bonus_scene1_pov = True
    scene black with Dissolve(0.3)
    show bonus_reb2 with dissolve
    sensation "You pull almost all the way out, then sink back in with a single, slow thrust. Her walls flutter and grip you tightly, trying to pull you even deeper."
    mc "Who's inside you right now?"
    perception "Her pupils are blown wide, cheeks flushed deep red. Sweat beads on her forehead, strands of hair clinging to her skin. Her lips part with every shallow breaths."
    r "You... it's you... [mc]..."
    mc "Say it again."
    r "It's you... my [mc]... filling me... owning me..."
    mc "Good girl."
    call screen bonus_scene1_sex with dissolve

label bonus_scene1_cum:
    mc "I'm close, Becky!"
    r "Me too! Please... let's do it together..."
    if bonus_scene1_vaginal:
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene bonus_reb_s4 with vpunch
        sensation "Her walls flutter wildly, clenching, milking, trying to drag you over the edge. The heat, the slickness, the desperate grip of her body is overwhelming."
        r "[mc]! I'm~! I'm coming!"
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene bonus_reb_s5 with vpunch
        mc "Fuck! Take it all!"
        sensation "The release hits like a wave, hot, thick spurts flooding deep inside her. Her body convulses, walls spasming rhythmically around you, drawing out every pulse."
        r "Yes~! Yes! Fill me!"
        sensation "Her body milks you through the final pulses—soft, rhythmic squeezes that prolong the pleasure. Warmth spreads between you and Rebecca, slick and intimate."
        play sound "se_sfx/sex/touch3.mp3" 
        scene bonus_reb_s6 with Dissolve(1.0)
        r "I feel it... so warm... so full..."
        r "You... you came so much the second time..."
        r "I love you... I love this so much. Can we do... this every night, [mc]?"
        mc "*chuckles* No objections."
    else:
        play sound "se_sfx/sex/sex_cum5.mp3" 
        scene bonus_reb_s1 with vpunch
        sensation "Her walls flutter wildly, clenching, milking, trying to drag you over the edge. The heat, the slickness, the desperate grip of her body is overwhelming."
        r "[mc]! I'm~! I'm coming!"
        play sound "se_sfx/sex/sex_cum4.mp3" 
        scene bonus_reb_s2 with vpunch
        mc "Fuck! Take it all!"
        sensation "The release hits like a wave, hot, thick spurts flooding deep inside her. Her body convulses, walls spasming rhythmically around you, drawing out every pulse."
        r "Yes~! Yes! Fill me!"
        sensation "Her body milks you through the final pulses—soft, rhythmic squeezes that prolong the pleasure. Warmth spreads between you and Rebecca, slick and intimate."
        play sound "se_sfx/sex/touch3.mp3" 
        scene bonus_reb_s3 with Dissolve(1.0)
        r "I feel it... so warm... so full..."
        r "You... you came so much the second time..."
        r "I love you... I love this so much. Can we do... this every night, [mc]?"
        mc "*chuckles* No objections."
    $ renpy.end_replay()
    jump scene75_6

label scene75_6:
    scene 75_s49 with Fade(1.0,1.0,1.0)
    r "Hahh... Gods. I'm so tired."
    scene 75_s50 with dissolve
    mc "Me too."
    scene 75_s49 with dissolve
    r "I can't even open my eyes, that was... intense."
    scene 75_s50 with dissolve
    mc "I'm glad that I made you feel good."
    scene 75_s49 with dissolve
    r "Heh. That's an understatement."

    if mc_reb_vaginal:
        r "Well... it's official."
        scene 75_s50 with dissolve
        mc "What is?"
        scene 75_s49 with dissolve
        r "I'm no longer a virgin."
        scene 75_s50 with dissolve
        mc "Oh. Congratu...lation...?"
        scene 75_s49 with dissolve
        r "*chuckles* Shut up..."

        if not mc_reb_vaginal_inside:
            r "And... thank you."
            scene 75_s50 with dissolve
            mc "For what?"
            scene 75_s49 with dissolve
            r "For not finishing inside me. *giggles* Gods know that couldn't have been easy for you."
            scene 75_s50 with dissolve
            mc "*laughs* That's putting it mildly. It was a heroic act of will."
            mc "Come on. Let's get some rest."

        elif mc_reb_vaginal_inside:
            r "*sigh* Hopefully my mother comes back soon..."
            r "I can't have her seeing me with a swollen belly."
            scene 75_s50 with dissolve
            mc "Relax. Like I told you, nothing shows that quickly."
            mc "And that's assuming you're even pregnant in the first place."
            r "Mhm."
            mc "Come on. Let's get some rest."

    if mc_reb_anal:
        r "Hnn! My ass..."
        scene 75_s50 with dissolve
        mc "What's wrong?"
        scene 75_s49 with dissolve
        r "What's {i}wrong!?{/i} You utterly destroyed it, that's what's wrong."
        scene 75_s50 with dissolve
        mc "*chuckles* But you still enjoyed it."
        scene 75_s49 with dissolve
        r "...I did."

        if mc_reb_anal_inside:
            r "*sigh* I can still feel it. There's some of your seed dripping out. You just had to finish inside me, didn't you?"
            scene 75_s50 with dissolve
            mc "You can deal with all that in the morning. Right now, let's just rest."
        else:
            scene 75_s50 with dissolve
            mc "Come on. Let's get some rest."

    scene 75_s49 with dissolve
    r "You'll stay with me, right?"
    scene 75_s50 with dissolve
    mc "I'm not going anywhere. Goodnight, Becky."
    scene 75_s49 with dissolve
    r "Night~"
    scene 75_s50 with dissolve
    jump scene76

label scene76:
    scene 76_s16 with Fade(1.5,1.0,1.5)
    mc "*sigh* (Can't sleep again.)"
    scene 76_s17 with dissolve
    mc "I'm going out to get some air. Sleep tight, Becky."
    r "..."
    scene 76_s18 with Fade(1.0,1.0,1.5)
    ""
    play music "wind_breakup.mp3" fadein 2.0 volume 0.8 loop
    scene 76_s19 with Fade(0.5,0.5,0.5)
    mc "Unf! (So cold...)"
    scene 76_s22 with Fade(0.5,0.5,0.5)
    mc "Hmm?"
    scene 76_s21 with Dissolve(1.0)
    mc "Are those cigarettes?"
    mc "It's been so long..."
    call screen scene76_choice01 with dissolve

label scene76_choice01_op1:
    $ mc_smoked = True
    mc "Why not."
    scene 76_s23 with Dissolve(1.0)
    ""
    scene 76_s24 with Dissolve(1.0)
    play sound "sound_effects/cig_smoke.mp3"
    ""
    scene 76_s20 with Dissolve(1.5)
    mc "*sigh* (I still miss you so much...)"
    mc "(I hope you're doing okay... wherever that world is now.)"
    mc "..."
    jump scene76_2

label scene76_choice01_op2:
    mc "Nah."
    scene 76_s20 with Dissolve(1.5)
    mc "*sigh* (I still miss you so much...)"
    mc "(I hope you're doing okay... wherever that world is now.)"
    mc "..."
    jump scene76_2

label scene76_2:
    if mc_smoked:
        scene 76_s1 with dissolve
    else:
        scene 76_s2 with dissolve
    stop music fadeout 2.0 
    mc "(What the...?)"
    play music "desert.mp3" fadein 2.0 loop
    scene 76_s3 with Dissolve(1.0)
    mc "(Is that... Negumi?)"
    scene 76_s4 with Fade(0.5,0.5,0.5)
    mc "(What the hell is she doing here?!)"
    scene 76_s5 with Fade(0.5,0.5,1.5)
    negumi "Let me go! I need to— I have to find someone!"
    guard "Stop resisting!"
    scene 76_s6 with Dissolve(1.0)
    mc "What's going on here?!"
    scene 76_s7 with dissolve
    guard "Sir [mc]. We caught this one skulking around the outer walls. Looks like a scout or a thief."
    scene 76_s8 with dissolve
    negumi "*pant* I wasn't skulking! You have to listen to me!"
    scene 76_s6 with dissolve
    mc "Let her go. I know her, she's not a thief."
    scene 76_s7 with dissolve
    guard "...As you say, sir."
    scene 76_s6 with dissolve
    scene 76_s9 with Fade(0.5,0.5,0.5)
    negumi "*pant* *pant* ...Thank you."
    mc "Negumi. What's wrong? Why are you here?"
    negumi "Hahh... T-The girl! They... *pant* they took her!"
    mc "Easy. Breathe. Start from the beginning. Who got who?"
    scene 76_s10 with Dissolve(1.0)
    negumi "*gulp* Okay... okay. I was at the market yesterday. And I saw him. Able."
    negumi "He was staring at this girl—she was just buying strawberries. Then he just... grabbed her. She started screaming. The whole market heard it."
    scene 76_s11 with dissolve
    mc "Strawberries...?"
    scene 76_s10 with dissolve
    negumi "Yes! Doesn't matter! He dragged her, kicking and screaming, right into the tavern we visited before. I... I had to know. So I snuck in this night."
    negumi "I found her in a cellar cell. She thought I was with them at first, but I told her I wasn't. When I said that, she just... broke. Started sobbing."
    negumi "She begged me to come to the castle, to find a man named [mc]. She said you were the only one who could help."
    scene 76_s11 with dissolve
    mc "Did she... tell you her name?"
    scene 76_s10 with dissolve
    negumi "Shit... It was all so fast. I didn't stay long... It started with an 'M,' I think..."
    scene 76_s11 with dissolve
    mc "Maia?"
    scene 76_s12 with dissolve
    negumi "That's it! Maia! So you know her? Who is—"
    scene 76_s13 with dissolve
    mc "..."
    negumi "{size=30}Hey... [mc]? Umm... Hello?{/size}"
    negumi "{size=30}Hey! Snap out of it! What's wrong? Who was that girl? Talk to me!{/size}"
    stop music fadeout 1.0 
    scene black

    show expression "chapter1_journey_main" at center with Fade(1.5,1.0,1.0)
    play music "images/custom_gui/global/mainmenu/mainmenu_song.mp3" fadein 2.0 loop
    window hide
    pause 0.5
    window show
    ""

    show chapter3_recap1 with dissolve
    if mc_took_reiner_money:
        "Reiner's gold now sits heavy in your pocket. It was a transaction that earned you a noble's smile, but cost you a glance of disappointment from Alex."
    else:
        "You refused Reiner's coin. A silent, principled stand that did not go unnoticed by Alex."

    show chapter3_recap2 with dissolve
    hide chapter3_recap1
    if mc_queen_choice_coin:
        "The Queen paid you what you asked. A simple transaction, nothing more."
    elif mc_queen_choice_sex:
        "You dared to name the Queen herself as your prize. Instead of offense, your boldness was met with a knowing, intrigued smile."
    elif mc_queen_choice_nothing:
        "You asked for nothing. A move so counter to the court's nature that it might have been the most cunning request of all."

    show chapter3_recap9 with dissolve
    hide chapter3_recap2
    if mc_accept_collector_bribe:
        "The tax collector's bribe was accepted. Easy coin, but it left a faint, unclean stain on your hands."
    else:
        "You turned away the collector's coin. A small victory for integrity, paid for from your own pocket."

    show chapter3_recap3 with dissolve
    hide chapter3_recap9
    if not mc_harem_kat and not mc_execute_kat and not mc_life_kat:
        "You saved Kathrine's life but made it clear you did it for your own reasons."

    elif mc_harem_kat:
        "You spared Kathrine, and in return, she pledged her life to you. Another woman bound to your own by the strange threads of fate."

    elif mc_execute_kat:
        "You gave the order for Kathrine's execution. Was it justice for her crimes, or cruelty to secure your position? The distinction faded with the fall of the axe."
        
    elif mc_life_kat:
        "You condemned Kathrine to a cell for the rest of her days. A fate some would call a mercy, and others a punishment worse than death."

    show chapter3_recap4 with dissolve
    hide chapter3_recap3
    if mc_grope_reb_ass:
        "You let impulse rule you—a daring grope met not with amusement, but with a royal glare."
    else:
        "For once, discipline triumphed over desire. You kept your hands to yourself, and in doing so, kept a princess's volatile temper in check."

    show chapter3_recap10 with dissolve
    hide chapter3_recap4
    if mc_elara_in:
        "Despite her shaky start, you saw a spark of potential in Elara and allowed her entry into the Guild. Her beaming smile was its own reward."
    else:
        "You upheld the Guild's standards and turned Elara away. The disappointment in her eyes was a heavy weight, but a necessary one."

    show chapter3_recap5 with dissolve
    hide chapter3_recap10
    if mc_accept_joan:
        "You accepted Alice's proposal and agreed to train her new recruit. A new task begins."
    else:
        "You refused Alice's offer. Not every opportunity is worth the trouble."
    
    show chapter3_recap6 with dissolve
    hide chapter3_recap5
    if mc_accept_jenny:
        "You gave Jenny the second chance she begged for, and in return, she offered a more... intimate form of payment. A trade she considered more than fair."
    else:
        "You held your ground and denied Jenny's desperate request. Some compromises are too costly, no matter the temptation."

    show chapter3_recap7 with dissolve
    hide chapter3_recap6
    if mc_reb_breakup:
        "You let the silence between you and Rebecca stretch until it snapped. Whatever future you might have had now lies in fragments, its shape uncertain."
    elif mc_rejected_wedding_reb:
        "The Queen offered you Rebecca's hand. You refused without hesitation. Just a flat rejection, and the weight of what you turned away."
    else:
        "The tension with Rebecca remains, a volatile but persistent connection. For now, she is still a presence in your life."

    if not mc_rejected_wedding_reb:
        if not mc_reb_breakup:
            show chapter3_recap8 with dissolve
            hide chapter3_recap6
            if mc_accept_reb_sex:
                if reb_pregnant:
                    "Rebecca gave herself to you, and now she carries your child. Her purity and her future belong to you."
                else:
                    "You succumbed to the heat of the moment with Rebecca. Whatever walls remained between you were torn down in a night that left her innocence a memory."
            else:
                "Rebecca's plea nearly broke you, but you held firm. Some lines weren't meant to be crossed, not yet."

    show chapter1_recap12 with dissolve
    hide chapter2_recap11
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1

    if mc_karma < 1:
        $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    "You have [mc_coin] coins to your name, and your honor stands at [mc_karma] out of 10. Whatever that means."
    window hide
    scene chapter4 with Fade(1.5,0.5,1.5)
    ""
    stop music fadeout 1.5
    scene 76_s36 with Fade(1.0,1.0,1.0)
    pause 1.5
    scene 76_s25 with Fade(1.5,1.0,1.5)
    play music "nature.mp3" fadein 1.0 loop
    olivia "Miss Alex? May I come in?"
    alex "Mhmmm..."
    olivia "I'll take that as a yes."
    scene 76_s26 with Dissolve(1.0)
    olivia "You're still sleeping? Come on, get up. Lord Reiner wants to see you."
    alex "Aggghh... Five more minutes..."
    scene 76_s27 with Dissolve(1.5)
    alex "*yawn*"
    scene 76_s28 with dissolve
    olivia "Ugh! How many times must I tell you not to sleep without clothes?"
    olivia "It's so unladylike!"
    scene 76_s29 with dissolve
    alex "Yeah, yeah. Thank you, Olivia. Could you please leave now?"
    scene 76_s28 with dissolve
    olivia "Do you promise to be up this time?"
    scene 76_s29 with dissolve
    alex "Ahuh."
    scene 76_s28 with dissolve
    play sound "sound_effects/door_close.mp3"
    scene 76_s33 with Dissolve(1.0)
    alex "..."
    if persistent.alex_d:
        scene 76_s32 with Dissolve(1.0)
    elif persistent.alex_p:
        scene 76_s31 with Dissolve(1.0)
    alex "Ngh~! (I can fight it for longer now, but it always... always comes back.)"
    alex "(I could just get it over with and—)"
    alex "(No. No, no, no! I have to stay strong.)"
    alex "(Being alone just makes the cravings worse. I should head out before I lose it again.)"
    scene 76_s34 with Fade(1.0,0.5,0.5)
    alex "*sigh* (Do I really have to wear this stuff again?)"
    scene 76_s35 with Fade(1.0,1.0,1.5)
    jump scene77

label scene77:
    ""
    scene 77_s1 with Fade(1.0,0.5,0.5)
    alex "Who's in there, Olivia? I hear a new voice."
    scene 77_s2 with Dissolve(1.0)
    olivia "Oh, you're actually awake. I'm impressed."
    scene 77_s3 with dissolve
    alex "Mhm."
    scene 77_s4 with dissolve
    olivia "Well, that would be Nueleth. She descended from her spire."
    scene 77_s5 with dissolve
    alex "Nueleth?"
    scene 77_s6 with Dissolve(1.0)
    olivia "Yes! Can you believe it? It's the first time seeing her with my eyes."
    olivia "You know what this is about, don't you?"
    alex "I... don't."
    scene 77_s7 with Dissolve(0.8)
    olivia "Are you sure? It's definitely about that massacre everyone's talking about."
    alex "Maybe."
    scene 77_s43 with Dissolve(1.5)
    olivia "Hmm... Well, don't keep the animals waiting. Good luck."
    stop music fadeout 1.0
    scene 77_s8 with Fade(1.0,0.5,1.0)
    play music "avery2.mp3" fadein 2.0 loop
    reiner "...the yield this season was exceptional. Maybe the best. Really, everyone's talking about it."
    scene 77_s9 with dissolve
    reiner "Ah, there she is. The heroine of the hour."
    scene 77_s10 with dissolve
    reiner "Everyone, this is my daughter, Alexandria. The future of our kingdom."
    amb "You had a daughter?"
    scene 77_s11 with dissolve
    alex "...Pleasure to meet you all."
    scene 77_s12 with Dissolve(1.0) 
    nueleth "She? And what of you, Reiner?"
    scene 77_s13 with dissolve
    reiner "Oh, please. I'm a relic. She possesses a mind and resolve that far surpasses my own. *chuckles* The years have not been kind to me."
    scene 77_s14 with dissolve
    reiner "Now, sit, dear. We were just discussing the tragic events at the manor. Since you were there, your account will finally provide the much needed truth."
    alex "..."
    reiner "Alex?"
    scene 77_s15 with dissolve
    alex "The entire mansion was an inferno. Bodies... were everywhere."
    alex "It was a slaughterhouse."
    scene 77_s16 with dissolve
    amb "We are aware of the outcome, Reiner. We don't need a poetic description."
    scene 77_s53 with dissolve
    reiner "Patience, Ambassador. The details matter. Please, continue, Alex."
    scene 77_s15 with dissolve
    alex "I saw the two responsible. A woman named Kathrine... and Gaius."
    scene 77_s14 with dissolve
    reiner "Gaius? I don't know much about him but he's not a man one sends for diplomacy. And what happened then?"
    scene 77_s15 with dissolve
    if mc_tried_help_alex:
        alex "He... he tried to kill me. I'd be dead if not for a man named [mc]."
    else: 
        alex "He... he tried to kill me."
    scene 77_s18 with dissolve
    amb "Kill you?! First you sabotage our alliance, Reiner, and now you attempt to murder your own blood?!"
    scene 77_s17 with dissolve
    scene 77_s15 with dissolve
    alex "N-No! That's not it! Before he attacked, Gaius whispered to me... something about the Queen sending her regards."
    scene 77_s19 with Dissolve(1.0) 
    amb "..."
    play sound "sound_effects/slam_wood.mp3"
    scene 77_s20 with vpunch
    q "Preposterous!"
    scene 77_s21 with dissolve
    reiner "Your Majesty, why would the victim of an assassination attempt lie? Although faint, the marks from his grip are still on her neck."
    scene 77_s22 with dissolve
    amb "You told me Reiner was responsible!"
    scene 77_s23 with dissolve
    q "Because he is! Use your head, Ambassador! What possible gain would I have in destroying our alliance so brazenly?!"
    scene 77_s24 with dissolve
    q "Alex, your story has a fatal flaw. Gaius doesn't speak. He hasn't spoken a word for years."
    scene 77_s25 with dissolve
    reiner "Doesn't speak? You expect us to believe your personal executioner, a man who helped the royal crown conquer cities, is a mute?"
    reiner "More importantly, why was he even there? Under whose authority?"
    scene 77_s26 with dissolve
    q "Because you—!"
    scene 77_s25 with dissolve
    reiner "Because {i}I{/i} ordered it? But Your Majesty, why would your most loyal hound take commands from me?"
    scene 77_s26 with dissolve
    q "You must have deceived him! He wouldn't... No."
    scene 77_s29 with Dissolve(1.0) 
    nueleth "Can you explain this, Hannah? It's true that Gaius doesn't take commands from anyone who's not in the royal family."
    nueleth "And him 'not speaking' is not something I can take for granted."
    scene 77_s24 with Dissolve(1.0) 
    q "Alex, I beg you, speak the truth. You know what really happened."
    scene 77_s15 with dissolve
    alex "I am."
    scene 77_s27 with Dissolve(1.0) 
    reiner "I believe things are now clear. She orchestrated the massacre to sever our alliance with Nahraya, positioning herself as the sole beneficiary."
    reiner "And when my daughter stumbled upon the truth, she ordered her silenced."
    scene 77_s30 with Dissolve(1.0) 
    q "I see this for what it is now. You venomous snake. Do you truly believe this charade will hold?"
    scene 77_s31 with dissolve
    nueleth "Sit down, Hannah. We are not finished."
    scene 77_s32 with dissolve
    q "You are the wisest of us, Nueleth, and yet he has played you for a fool. I have been here for far too long and there is nothing left to say."
    scene 77_s34 with Dissolve(1.0) 
    reiner "Your Majesty! Do you intend to return today? There's a storm heading our way!"
    scene 77_s27 with Dissolve(0.8) 
    reiner "*sigh* I must apologize for her behavior. The weight of guilt can make even royalty irrational."
    scene 77_s18 with dissolve
    amb "This still feels... convenient. Why does your daughter, whom I didn't even know existed until today, come forward with this now? Why wasn't this presented by you, officially?"
    scene 77_s35 with Dissolve(0.8) 
    reiner "You must understand, Ambassador. Alexandria was undergoing a period of terrible trauma, she couldn't talk, let alone eat. Her... departure is what led her to witness this tragedy."
    reiner "She only confided the full horror of her experience to me last night. I was as horrified as you are."
    scene 77_s36 with dissolve
    amb "*sigh* What of the other woman? You said there were two."
    scene 77_s35 with dissolve
    if not mc_life_kat and not mc_execute_kat:
        reiner "The accomplice? Secured in the dungeons, last I heard. You needn't trouble yourself with her."
    if mc_life_kat:
        reiner "The accomplice? Secured in the dungeons, last I heard. You needn't trouble yourself with her."
    elif mc_execute_kat:
        reiner "The accomplice? She was sentenced to be executed, last I heard. You needn't trouble yourself with her."
    scene 77_s36 with dissolve
    amb "I will be the judge of that. I want to hear her testimony."
    scene 77_s35 with dissolve
    reiner "Ambassador, I assure you, it's unnecessary. Alex's account is more than sufficient."
    scene 77_s37 with Dissolve(1.0) 

    if mc_tried_help_alex:
        nueleth "Alexandria. You mentioned a man named [mc] saved you. Is that correct?"
        scene 77_s38 with dissolve
        alex "Yes."
    else:
        nueleth "Were those two the only people at the scene, Alexandria?"
        scene 77_s38 with dissolve
        alex "...There was a man named [mc] too."

    reiner "Miss Nueleth, with respect—"
    scene 77_s39 with Dissolve(0.8) 
    nueleth "Let her speak."
    scene 77_s37 with Dissolve(0.8) 
    nueleth "What became of him, Alex? Is he available to give his account?"
    scene 77_s38 with dissolve
    alex "I-I don't know... He—"
    scene 77_s40 with dissolve
    alex "..."
    scene 77_s41 with dissolve
    alex "He was killed during the attack. He didn't make it."
    scene 77_s42 with dissolve
    nueleth "Hm. Unfortunate."
    nueleth "It seems we must rely on the other witness, then. Assuming she hasn't been executed."
    reiner "...Of course. We shall arrange it."
    reiner "*ahem* Alex, would you be so kind as to escort Her Majesty? In her current state, I fear her anger may lead her to do something... regrettable. Ensure she returns to her ship safely."
    alex "..."
    reiner "Dear."
    scene 77_s41 with dissolve
    alex "Y-Yes, father."
    scene 77_s42 with dissolve
    stop music fadeout 2.0 
    scene 77_s51 with Fade(1.0,1.0,1.0)
    olivia "What's wrong, Miss? Do you need anything? Water?"
    scene 77_s52 with dissolve
    alex "I just... I need a moment. Thank you."
    play music "wind2.mp3" fadein 3.0 loop
    scene 77_s44 with Fade(1.0,1.5,1.5)
    ""
    scene 77_s45 with dissolve
    king_e "Alex. Is that you?"
    scene 77_s46 with Dissolve(1.0) 
    alex "Y-Your Highness!"
    king_e "*chuckles* Heh. I knew it was you. Your footsteps always give you away, light as a thief's."
    alex "..."
    king_e "*cough* I apologize for my absence in there."
    alex "No, your Highness. It's fine. You don't have to apologize."
    king_e "Good. I hope matters with Irda's queen were resolved amicably. She's a good woman. Stubborn, like her father. I knew him well."
    king_e "He would be heartbroken to see what's become of his daughter's kingdom."
    alex "..."
    king_e "Be careful out there, Alex."
    scene 77_s49 with Dissolve(1.0) 
    alex "Your Highness?"
    scene 77_s50 with dissolve
    king_e "I just hope you know what you're doing."
    scene 77_s48 with Dissolve(1.0) 
    maid_eurina "Your Highness, please! You can't be leaving your room like this! The physicians will have my head!"
    king_e "*chuckles* It seems my jailer has found me."
    king_e "Go on, Alex. God be with you."
    scene 77_s49 with Dissolve(1.0) 
    alex "...You too."
    scene 77_s50 with dissolve
    jump scene78

label scene78:
    stop music fadeout 1.0 
    scene 78_s1 with Fade(1.5,1.0,1.5)
    play music "wind.mp3" fadein 1.0 loop
    ""
    scene 78_s2 with Dissolve(1.5) 
    alex "Ahh... hhah... I-I'm here!"
    scene 78_s3 with Dissolve(1.0) 
    ""
    scene 78_s4 with Dissolve(1.0) 
    alex "Where are my swords?"
    scene 78_s5 with dissolve
    assassin "You only need the dagger."
    scene 78_s6 with dissolve
    eli "Alex!"
    scene 78_s7 with Dissolve(1.0) 
    alex "Eli!? What are you doing here?!"
    scene 78_s8 with Dissolve(1.0) 
    eli "I... Hahh... I saw you running from my room. Where are you going?"
    scene 78_s9 with dissolve
    alex "I'm... I won't be long, don't worry."
    scene 78_s8 with dissolve
    eli "You won't leave me like last time, right?"
    eli "Father was... really scary when you left. Please don't go away!"
    scene 78_s9 with dissolve
    alex "I won't. Never again."
    scene 78_s8 with dissolve
    eli "Do you promise?"
    scene 78_s9 with dissolve
    alex "I promise."
    scene 78_s10 with dissolve
    eli "Good. I'll see you soon. Right?"
    scene 78_s11 with dissolve
    alex "Right."
    scene 78_s12 with dissolve
    eli "Before I leave, I swear I saw someone with you."
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 78_s13 with dissolve
    alex "It's only me. Go on now."
    scene 78_s14 with dissolve
    eli "Unff! *giggles* Alright, alright."
    scene 78_s15 with Dissolve(1.0) 
    alex "..."
    scene 78_s16 with dissolve
    assassin "Dress up and get going."
    stop music fadeout 1.0
    scene 78_s17 with Fade(1.0,1.0,1.5)
    play music "nature.mp3" fadein 1.0 loop
    ""
    play sound "sound_effects/grass.mp3"
    scene 78_s18 with dissolve
    "*rustle* *rustle*"
    guard "Hmm?"
    scene 78_s19 with dissolve
    guard "Who- Uh, Miss Alex? You've got nerve showing your face here, after dragging Her Majesty's name through the mud with your lies."
    guard "Did you come to spin more of your filthy tales?"
    scene 78_s20 with Dissolve(1.0)
    alex "I was ordered to escort Her Majesty to her ship. That's all."
    scene 78_s21 with dissolve
    scene 78_s19 with Dissolve(1.0)
    guard "Escort? There's no need for the likes of you to—"
    scene 78_s18 with dissolve
    q "Let her, Rolf. I would welcome the company."
    scene 78_s22 with Dissolve(1.0)
    guard "A-As you wish."
    stop music fadeout 1.0 
    scene 78_s23 with Fade(1.0,1.0,1.0)
    play sound "sound_effects/horse_cart.mp3" volume 0.5
    play music "nature.mp3" fadein 1.0 volume 0.5 loop
    alex "..."
    q "So. 'Ordered' to escort me, was he? How... thoughtful."
    scene 78_s25 with Dissolve(1.5)
    ""
    stop sound fadeout 2.0
    stop music fadeout 2.0 
    scene 78_s26 with Dissolve(2.0)
    play music "thunder.mp3" fadein 2.0 loop
    ""
    scene 78_s27 with Dissolve(1.0)
    q "Enough time has passed. Are you ready to speak now?"
    scene 78_s28 with dissolve
    alex "About what?"
    scene 78_s27 with dissolve
    q "That you are a poor liar. Your silence screams louder than any confession." 
    q "Did Reiner threaten you? Is it your mother's memory he holds over you? I know how he uses sentiment as a weapon."
    scene 78_s28 with dissolve
    alex "I was telling the truth."
    scene 78_s29 with dissolve
    q "We are past that, girl. Do you have any concept of the war you are lighting the fuse for? The thousands who will suffer and die for this fiction?"
    scene 78_s30 with dissolve
    alex "I didn't start a war. I—"
    scene 78_s29 with dissolve
    q "Is this the legacy you wish to build?"
    scene 78_s30 with dissolve
    alex "...Please. Stop."
    scene 78_s29 with dissolve
    q "Or what? You'll do what you were sent here to do?"
    scene 78_s34 with dissolve
    alex "...What?"
    scene 78_s35 with dissolve
    q "Reiner sent you to kill me. Why else would you be here? I heard rumors he raised you for only one purpose."
    scene 78_s34 with dissolve
    alex "N-No..."
    scene 78_s32 with dissolve
    q "Yet here you are, hesitating. You're no killer, Alex. Not truly. Your mother raised you better than that fiend ever could."
    q "I can see it in your eyes, you still have a conscience."
    scene 78_s31 with dissolve
    alex "You don't know anything about me."
    scene 78_s32 with dissolve
    q "I know enough. The truth always finds its way to the light. Whatever scheme your father has concocted will unravel. I only hope you see your part in it before it's too late."
    q "That woman, Kathrine, confessed to me that the order came from Reiner. There's also [mc] who was present there."
    q "I can only pray both are well when I return to testify."
    scene 78_s36 with dissolve
    alex "..."
    scene 78_s33 with dissolve
    q "As for Gaius... *sigh* How could he listen to Reiner? It makes no sense. He would never... he only ever answers to the Royal Family..."
    scene 78_s37 with dissolve
    q "*gasp* No. No, no, no..."
    q "She wouldn't... No..."
    play sound "sound_effects/horse_neigh.mp3" volume 0.5
    scene 78_s39 with vpunch
    q "Hngh!"
    scene 78_s38 with dissolve
    q "Why are we stopping? Rolf?"
    scene 78_s39 with dissolve
    "..."
    scene 78_s38 with dissolve
    q "What is going on out there!?"
    scene 78_s39 with dissolve
    "..."
    scene 78_s38 with dissolve
    q "No... It can't be. He wouldn't dare make a move so soon!"
    scene 78_s29 with dissolve
    q "Alex, I believe they mean to kill me! Can you fight? I studied barrier magic at the academy, a powerful shield."
    q "I can make us invulnerable long enough to escape if you give me some time to cast it!"
    scene 78_s107 with dissolve
    alex "..."
    scene 78_s40 with dissolve
    q "Look at me, girl! Look at what you are helping him do! This isn't politics, it's butchery!"
    q "My people... your people... they will pay the price in blood. Is that what you want?"
    q "...I see it now. In your eyes. It's not conviction. It's fear. He has you terrified, doesn't he?"
    if mc_tried_help_alex:
        $ mc_save_queen = True
        scene 78_2_s20 with Dissolve(1.0)
        alex "..."
        scene 78_2_s21 with Dissolve(1.0)
        alex "Someone... Someone actually cared about me."
        if not mc_took_reiner_money:
            scene 52_s28 with Dissolve(1.0)
            alex "..."
        scene 78_2_s2 with Dissolve(1.0)
        q "You don't have to do this, Alex."
        q "Just give me the dagger."
        scene 78_2_s1 with dissolve
        alex "What... what should I even do? If I don't finish it, my brother..."
        scene 78_2_s2 with dissolve
        q "You will save your brother from him. But not like this. Do you truly believe your father will let you walk free after this?"
        q "You'll be the perpetrator of a regicide, your tongue the greatest threat to him and Avery. He'll keep your brother alive only as a leash to control you even more."
        scene 78_2_s3 with dissolve
        q "That fiend won't touch your brother while you live. He'll keep him as bait to draw you back."
        scene 78_2_s4 with dissolve
        alex "What do you mean?"
        scene 78_2_s3 with dissolve
        q "You're not an ally to them, you're a loose end. The moment you step out of this carriage, they'll silence you."
        scene 78_2_s1 with dissolve
        alex "Then... what? Will you go back? Expose Avery and my father?"
        scene 78_2_s2 with dissolve
        q "By the time I could return, Avery will have replaced my council, my guards, my very court with her own snakes."
        scene 78_2_s5 with dissolve
        q "And my children... Rebecca and Liam... they would be leashed, used as puppets, or worse..."
        q "If anything, my sudden return after I was presumed dead would certainly trigger a civil war. Many of my people will die for nothing."
        q "No. I must disappear. Let them spin their story. Let them think they have won."
        scene 78_2_s8 with dissolve
        q "When the time is right, when my son and daughter are safe, and the truth can strike with purpose I will return."
        scene 78_2_s7 with dissolve
        alex "Disappear? Where?"
        alex "I think they're planning to place your body and the dead guards back on your ship. They'll set it adrift into the storm."
        scene 78_2_s8 with dissolve
        q "*sigh* I see. That complicates matters. We cannot slip out unnoticed?"
        scene 78_2_s7 with dissolve
        alex "The carriage is surrounded. There's no way."
        scene 78_2_s8 with dissolve
        q "Very well."
        scene 78_2_s7 with dissolve
        alex "Huh? How are you so... composed?"
        scene 78_2_s3 with dissolve
        q "*chuckles* Should I panic? Scream? That is the opposite of helpful now."
        scene 78_2_s4 with dissolve
        alex "..."
        scene 78_2_s9 with Dissolve(1.3)
        q "Hmm... I was never the best at the academy, I had a habit of pushing spells beyond my limits, burning myself out. Almost died once during an incantation."
        scene 78_2_s10 with dissolve
        alex "Where are you going with this?"
        scene 78_2_s9 with dissolve
        q "I will cast two spells. A shield to slow my vital signs, and a calming charm to still my body."
        q "To any but the most thorough examiner, I will appear dead. Once they move me to the ship, I'll sail it not into the storm, but back into a different part of the coast."
        scene 78_2_s10 with dissolve
        alex "What if the spell kills you?"
        scene 78_2_s9 with dissolve
        q "*chuckles* Then Avery wins. But I'd rather die by my own magic than her treachery."
        q "There's a fisherman's family near the shore, the father is Eurinian, a former lieutenant of mine. Loyal to the bone. He'll hide me."
        scene 78_2_s11 with dissolve
        q "Now listen carefully. When you step out, act as if you've done the deed."
        q "The moment they move to silence you, run and don't look back. You're strong, but not against so many trained blades."
        scene 78_2_s12 with dissolve
        alex "I will."
        scene 78_2_s11 with dissolve
        q "Good. Once you're safe, find the man who found you, [mc]. Avery will certainly try to silence him too. He was a witness to all of this."
        scene 78_2_s12 with dissolve
        alex "You want me to save him?"
        scene 78_2_s11 with dissolve
        q "Go to him. Then travel to Nahraya. Find King Hod. Tell him everything, together."
        q "He must summon Nueleth, the only one with the authority and power to call out this treason. Do you understand?"
        scene 78_2_s12 with dissolve
        alex "Find [mc]. Go to Hod. Summon Nueleth."
        scene 78_2_s11 with dissolve
        q "Swear it to me."
        scene 78_2_s12 with dissolve
        alex "I swear."
        scene 78_2_s13 with Dissolve(1.0)
        q "*chuckles* You're a... good girl, Alex."
        q "Once I... Nghn... hear the news of Nueleth coming over, I will make the journey there immediately."
        scene 78_2_s14 with dissolve
        alex "Alright. They must be getting suspicious by now. You should start."
        scene 78_2_s13 with dissolve
        q "I... already was. Leave... the carriage... now."
        scene 78_2_s14 with dissolve
        alex "A-Alright."
        scene 78_2_s13 with dissolve
        stop music fadeout 1.0 
        scene 78_2_s15 with Fade(1.4,1.0,1.0)
        play music "thunder2.mp3" fadein 2.0 loop
        assassin "What took you so long?"
        alex "I had her drink the poison instead. It was the humane way to go about it."
        assassin "Humane? So you do have emotions after all."
        alex "..."
        assassin "Regardless, you did well. Your father will be pleased."
        alex "*sniff* What happens now?"
        scene 78_2_s16 with Dissolve(1.3)
        assassin "Sit tight. We'll clean up this mess and dump the bodies onto their ship."
        scene 78_2_s17 with Dissolve(1.4)
        assassin "It'll sail into the heart of the storm, the sea will claim all evidence. No one will suspect a thing."
        play sound "sound_effects/stab1.mp3"
        scene 78_2_s18 with vpunch
        assassin "Aghhh!"
        scene 78_2_s19 with dissolve
        assassin "You little—! GET HER!"
    else:
        $ mc_save_queen = False
        scene 78_s41 with dissolve
        alex "I... I have to..."
        scene 78_2_s20 with Dissolve(1.0)
        alex "There's not a single soul in this world who cared about me aside from my brother."
        scene 78_s42 with Dissolve(1.0)
        q "No, Alex. I'm sure there are plenty."
        q "Just give me the dag—"
        play sound "sound_effects/stab2.mp3"
        scene 78_s43 with vpunch
        q "Hugh—!"
        scene 78_s46 with Dissolve(1.0)
        ""
        scene 78_s43 with dissolve
        ""
        scene 78_s44 with Dissolve(1.0)
        ""
        play sound "sound_effects/drop_knife.mp3"
        scene 78_s45 with Dissolve(1.0)
        q "Hah... I see."
        q "*cough* So it really was the plan. The little rat {i}did{/i} made you his blade."
        q "So disappointing..."
        scene 78_s47 with Dissolve(1.0)
        alex "Where do you think you're goi—"
        q "Shut it. Let me look at the sky."
        alex "..."
        scene 78_s48 with Dissolve(1.0)
        q "*chuckles* Oh, Avery... it was never that serious..."
        alex "*sniff* I'm sorry..."
        scene 78_s49 with Dissolve(1.0)
        q "Run. *cough* Run away from him, Alex. Now."
        alex "..."
        q "Hahh... You can't possibly believe he'll let you live after this? You're the loose end."
        alex "..."
        q "Listen... The truth... won't die with me. Hod... Nueleth... they... have to know..."
        q "Find... the witness..."
        stop music fadeout 1.0 
        scene 78_s50 with Dissolve(1.5)
        play music "thunder2.mp3" fadein 2.0 loop
        alex "*sniff* It's over. I did it."
        assassin "Good. Your father will be pleased."
        alex "Wh-What happens now?"

        scene 78_s51 with Dissolve(1.0)
        assassin "We load the bodies onto the ship. It will sail into the heart of the storm."
        scene 78_s52 with Dissolve(1.0)
        assassin "The sea will claim all evidence. No one will suspect a thing."
        play sound "sound_effects/stab1.mp3"
        scene 78_s53 with vpunch
        assassin "Aghhh!"
        scene 78_s54 with dissolve
        assassin "You little—! GET HER!"

    scene 78_s55 with dissolve
    alex "Hahh! Hah!"
    play sound "sound_effects/arrow_hit1.mp3"
    scene 78_s56 with vpunch
    alex "AHHHGH! FUCK!"
    assassin2 "Got a hit! She's wounded!"
    scene 78_s57 with dissolve
    alex "Oh, shit! Shit! Shit!"
    play sound "sound_effects/bodydrop2.mp3"
    scene 78_s58 with Dissolve(0.3)
    scene 78_s58 with vpunch
    alex "Ahhng!"
    play sound "sound_effects/watersplash2.mp3"
    scene 78_s59 with Dissolve(0.3)
    scene 78_s59 with vpunch
    ""
    scene 78_s60 with dissolve
    alex "Ahahhn!"
    scene 78_s61 with dissolve
    assassin2 "Got you! She's here!"
    play sound "sound_effects/watersplash3.mp3"
    scene 78_s62 with dissolve
    assassin2 "Oh, no. You're not running away this time."
    assassin2 "I'm going to enjoy choking the life out of you."
    scene 78_s63 with dissolve
    ""
    play sound "sound_effects/stab3.mp3"
    scene 78_s64 with Dissolve(0.3)
    scene 78_s64 with vpunch
    assassin2 "Ghk—!"
    play sound "sound_effects/clothing_rustle.mp3"
    scene 78_s65 with dissolve
    alex "HAHH! AHHH! AHAAHHH!"
    alex "Fuck! Get off me!"
    scene 78_s66 with dissolve
    assassin2 "The voice came from this direction."
    alex "(Give me a break!)"
    scene 78_s67 with dissolve
    alex "*enhale*"
    play sound "sound_effects/waterbloob.mp3"
    scene 78_s68 with Dissolve(1.0)
    assassin2 "I can't find anyone!"
    assassin2 "Head down the mountain. You, get up and look for a vantage point. She couldn't have gone far."
    assassin2 "What about Alric? He's been injured."
    assassin2 "The girl first. His words not mine."
    "..."
    "...."
    "....."
    play sound "sound_effects/watersplash3.mp3"
    scene 78_s69 with Dissolve(0.3)
    scene 78_s69 with vpunch
    alex "HAHH!"
    scene 78_s70 with Fade(1.0,1.0,1.5)
    ""
    scene 78_s71 with Fade(1.0,1.0,1.0)
    slaver2 "We're really goin' out in this shit? I can't feel my bloody fingers no more."
    slaver "That's the point, rookie. Guard ships don't sail in weather like this."
    slaver2 "*groan* Remind me why I signed up for this miserable life."
    slaver "Just pick up the boxes, box picker."
    slaver2 "Aye, captain. {size=30}Asshole...{/size}"
    scene 78_s72 with Fade(1.5,1.0,1.0)
    slaver "All aboard!"
    scene 78_s73 with Dissolve(1.5)
    ""
    scene 78_s74 with Dissolve(1.5)
    ""
    stop music fadeout 2.0 
    scene 78_s76 with Fade(1.5,1.0,1.0)
    play music "ocean.mp3" fadein 1.0 loop
    reham2 "Want some?"
    scene 78_s77 with dissolve
    alex "..."
    scene 78_s76 with dissolve
    reham2 "You should eat. It'll be at least two days before we reach land."
    scene 78_s77 with dissolve
    scene 78_s78 with Dissolve(1.0)
    alex "Thank you."
    reham2 "Mhm."
    scene 78_s79 with dissolve
    alex "Man. This might be the ugliest bread I've ever seen."
    scene 78_s80 with dissolve
    reham2 "*chuckles* Tell me about it."
    scene 78_s75 with Dissolve(2.0)
    ""
    stop music fadeout 1.0 
    scene 78_s81 with Fade(1.0,1.0,1.0)
    play music "ocean2.mp3" fadein 1.0 loop
    slaver "What in Agra's tits!?"
    slaver "You! How the hell did you get down here?"
    alex "Huh...?"
    scene 78_s82 with Fade(1.0,1.0,1.0)
    slaver "How did you get in, huh?!"
    alex "Faaauuuckk... I feel sick... Ugh..."
    scene 78_s83 with dissolve
    rich_man "Gibson, is there a problem?"
    scene 78_s84 with dissolve
    slaver "Found this one in the hull. Must've snuck on at the last port."
    slaver "I'm takin' her topside for the lads."
    scene 78_s83 with dissolve
    rich_man "Hold a moment. Let me see her first."
    scene 78_s84 with dissolve
    slaver "...Aye, sir."
    scene 78_s85 with Dissolve(1.0)
    slaver "Open your mouth, girl."
    scene 78_s86 with Dissolve(1.5)
    alex "Ughhn... Ahhhhhh..."
    slaver "All her teeth, straight and white. Never been in chains before, that's plain. Too well kept for a hold rat."
    alex "Fafer... I don't wan to geh my teesh done... it hurhs..."
    rich_man "What is she babbling about?"
    slaver "Not sure. Delirious, maybe."
    rich_man "Turn her around."
    scene 78_s87 with dissolve
    alex "Huh!? W-Where am I?"
    scene 78_s88 with dissolve
    slaver "Why don't you show us what's under that top, girl?"
    alex "Uhh... Sure thing..."
    scene 78_s89 with Fade(0.5,0.5,0.5)
    slaver "Sheesh... That eager to undress?"
    rich_man "Oh~! Exquisite. Such fair skin."
    rich_man "I want her!"
    slaver "Got a fresh arrow wound on the shoulder. Likely a runaway. Still want the risk, sir?"
    rich_man "More than ever. Means she's got fire in her."
    slaver "She ain't exactly on the list..."
    rich_man "Hang your list! I'm tired of the dark ones you keep dragging in, they break too quickly. This one's different."
    slaver "*ahem* Actually... now that I look closer, she is on the list. Eurinian blood, high grade. She'll cost you dear."
    slaver "Turn back around."
    scene 78_s90 with Dissolve(1.0)
    rich_man "Hold it. Is that..."
    slaver "Hmm? Move your hands."
    scene 78_s91 with dissolve
    rich_man "*laughs* Would you look at that! She's been marked by the Queen of Pleasure!"
    slaver "Not following... Looks like one of them tattoos the brothel whores usually have."
    rich_man "You pig-brained moron. That's no common ink, it's a binding curse. Can't be removed by anyone. Especially now that woman is dead."
    slaver "Right... funny, the list does mention that little detail. That'll be extra. A lot extra."
    rich_man "Worth every coin. You've struck gold this time, Gibson."
    rich_man "Come to my tent. We'll settle terms over wine. Have her bathed, gagged, and delivered by nightfall."
    stop music fadeout 1.0
    scene 78_s92 with Dissolve(1.0)
    slaver "Right behind you, sir. Move, girl."
    play music "angry/anger2.mp3" fadein 1.0 loop
    scene 78_s93 with Dissolve(1.0)
    ""
    scene 78_s94 with dissolve
    slaver "Huh?"
    play sound "sound_effects/stab3.mp3"
    scene 78_s95 with Dissolve(0.3)
    scene 78_s95 with vpunch
    slaver "GURK—!"
    scene 78_s96 with dissolve
    rich_man "Hmm? What was—"
    play sound "sound_effects/stab1.mp3"
    scene 78_s97 with Dissolve(0.3)
    scene 78_s97 with vpunch
    rich_man "AHHN!"
    play sound "sound_effects/bodydrop3.mp3"
    scene 78_s98 with dissolve
    alex "Filth."
    scene 78_s99 with Fade(1.0,1.0,1.0)
    play sound "sound_effects/horse_snort.mp3"
    alex "Woah! Calm down, boy."
    scene 78_s100 with dissolve
    alex "Are you just going to stand there!?"
    scene 78_s101 with dissolve
    alex "Run! Before the rest of them show up!"
    play sound "sound_effects/run.mp3" volume 0.3
    scene 78_s102 with dissolve
    ""
    stop sound fadeout 1.0
    scene 78_s103 with Dissolve(1.0)
    ""
    scene 78_s104 with dissolve
    alex "*sigh*"
    scene 78_s105 with Fade(0.5,0.5,0.5)
    alex "Come on. Give me your hand."
    scene 78_s106 with Dissolve(1.5)
    play sound "sound_effects/horse1.mp3"
    alex "Hyah!"
    stop music fadeout 1.0
    jump scene79

label scene79:
    scene 76_s13 with Fade(1.5,1.0,1.0)
    play music "tense/tention.mp3" fadein 2.0 loop
    ""
    scene 79_s1 with vpunch
    negumi "Huh? [mc]! Where are you going?!"
    scene 79_s2 with Dissolve(1.2)
    guard "Sir? Is something wrong?"
    scene 79_s3 with Dissolve(1.3)
    play sound "sound_effects/doors/door_knock_hard1.mp3"
    guard "Sir! Stand down! What is the meaning of this?"
    play sound "sound_effects/doors/door_knock_hard1.mp3"
    scene 79_s4 with Dissolve(1.0)
    mc "Which room is Avery's?!"
    guard "Sir, I must insist! You cannot address the Lady Regent this—"
    mc "AVERY!"
    scene 79_s5 with Dissolve(1.5)
    avery "What in all the hells is wrong with you? Explain yourself."
    scene 79_s6 with dissolve
    mc "You know exactly why I'm here."
    mc "Where is she?"
    scene 79_s7 with dissolve
    avery "Excuse me?"
    scene 79_s6 with dissolve
    mc "Maia. When were you going to tell me she was taken? Or were you just hoping I'd never find out?"
    scene 79_s8 with dissolve
    r "[mc]? Aunty? What happened?"
    r "I heard your voices all the way up to my chambers."
    scene 79_s9 with dissolve
    avery "It seems your husband is having a fit of hysterics."
    scene 79_s8 with dissolve
    r "[mc]?"
    scene 79_s10 with dissolve
    mc "Don't play with me. You knew Able kidnapped Maia. You knew, and you said nothing."
    scene 79_s11 with dissolve
    avery "..."
    avery "*sigh* Very well. I knew."
    scene 79_s12 with dissolve
    mc "What?"
    scene 79_s13 with dissolve
    avery "But I chose not to tell you for your own good. You are impulsive, [mc]. You rush headlong into danger without considering the consequences."
    avery "I feared what your... reaction would provoke."
    scene 79_s14 with dissolve
    mc "So that's why you told me to 'forget about her'?"
    mc "Doesn't matter. I'm going to get her back. Right now."
    scene 79_s13 with dissolve
    avery "[mc]. Please don't act childish. Maia is a runaway servant. Able has the legal documents to prove it. He is within his rights."
    scene 79_s14 with dissolve
    mc "I don't give a damn about his rights! You're the acting queen. Order her release."
    scene 79_s15 with dissolve
    avery "Order her release!? You dare to command me? To make demands of the crown?"
    avery "Who exactly do you think you're speaking to?"
    scene 79_s16 with dissolve
    mc "I am the Princess's husband and the steward of the castle."
    scene 79_s15 with dissolve
    avery "...Listen to me very carefully, [mc]. Do you know how that woman came to be under our roof? She was a stray, picked up illegally by Rebecca on one of her little... adventures."
    avery "She has lived in the castle's shadow ever since. Of course, Able never thought to look {i}here{/i}. Why would the royal family harbor a common runaway?"
    scene 79_s17 with dissolve
    avery "But once she started venturing beyond these walls... he finally caught his property. It's as simple as that. She is his."
    scene 79_s18 with dissolve
    mc "Is that... Do you honestly believe that explanation would make me calm down?"
    mc "And what do you mean, 'she is his'? I was under the impression slavery was illegal in Irda. Since when can one person {i}own{/i} another?"
    scene 79_s19 with dissolve
    avery "I have explained the situation. If you refuse to accept reality, that isn't my concern."
    scene 79_s20 with Dissolve(1.2)
    r "You know what? Who do {i}you{/i} think you are?"
    scene 79_s21 with dissolve
    avery "I beg your pardon?"
    scene 79_s20 with dissolve
    r "I said, who do you think you are, acting so high and mighty? Have you forgotten your place, {i}Aunt{/i} Avery? You are the Queen's sister, not the Queen."
    scene 79_s21 with dissolve
    avery "Rebecca, do not embarrass yourself. There is no need for this childishness."
    scene 79_s20 with dissolve
    r "There is every need. You've grown far too comfortable on my mother's throne, haven't you?"
    r "Don't think I haven't noticed your little changes in policy. Easing laws on slavery just enough to let filth like Able operate freely?"
    r "Did you think I was too stupid to notice?"
    play sound "sound_effects/slap06.mp3"
    scene 79_s22 with vpunch
    r "Ahh!"
    guard "Lady Avery, please!"
    play sound "sound_effects/bodydrop.mp3"
    scene 79_s23 with dissolve
    avery "You insolent little bitch. Do not {i}ever{/i} speak to me like that again."
    avery "Your mother was always too soft with you. If you were my daughter, I would have broken and remade you into a proper woman, whether you screamed through every second of it or not."
    scene 79_s24 with dissolve
    avery "I'll begin now. Your mother should be thankful."
    scene 79_s25 with vpunch
    avery "Hah!? Unhand me, [mc]!"
    scene 79_s26 with dissolve
    impulse "Pay her back, my liege. Make her feel what Rebecca felt with one good punch to the jaw."
    perception "Her wrist is fragile in your grip, bones shifting, skin paling. Real fear in her eyes, not the usual arrogance. She knows you could break her."
    r "Please, [mc], don't."
    empathy "She's scared. Really scared. Maybe just a slap will do."
    call screen scene79_choice01 with dissolve

label scene79_choice01_op1:
    $ mc_slap_avery = True
    play sound "sound_effects/slap07.mp3"
    scene 79_s27 with vpunch
    avery "AHH!"
    perception "Your palm meets her cheek with a sharp crack. Her head jerks sideways. A mist of spit catches the light before her body follows the motion."
    scene 79_s28 with dissolve
    guard "Lady Avery!"
    scene 79_s29 with Dissolve(1.0)
    avery "Nnnh... ah... S–Stand down...!"
    jump scene79_0

label scene79_choice01_op2:
    scene 79_s32 with dissolve
    empathy "You release her arm. She stumbles back, masking a shaky exhale that slips out anyway."
    avery "Uhhnn..."
    mc "Don't you ever touch her again."
    jump scene79_0

label scene79_0:
    scene 79_s30 with Dissolve(1.3)
    mc "I'm going after her."
    r "Save her, [mc]!"
    avery "Go. But mark my words, [mc]. If you walk out that gate. Do not ever think to come back."
    call screen scene79_choice02 with dissolve

label scene79_2:
    stop music fadeout 3.0
    scene 79_2_s1 with dissolve
    mc "I... I'll stay."
    scene 79_2_s2 with dissolve
    r "W-What!?"
    r "[mc]! You're really going to stay after hearing that!?"
    scene 79_2_s1 with dissolve
    mc "Sorry, Becky. But I had a good thing going here. A life. I'm not about to ruin it all for one... maid."
    scene 79_2_s2 with dissolve
    r "You coward!"
    avery "Don't listen to her, [mc]. You are making the correct choice."
    scene 79_2_s3 with dissolve
    avery "Escort the Princess to her chambers. She is in definite need of... recalibrating her priorities."
    scene 79_2_s4 with dissolve
    guard "...Yes, Lady Avery."
    scene 79_2_s5 with Dissolve(1.3)
    mc "What's... what's happening to her?"
    scene 79_2_s6 with dissolve
    avery "I will break down the rebellious side and reshape her into a woman worthy of the title 'Princess.' It will be painful, but necessary."
    if mc_slap_avery:
        avery "As for you, [mc]. I am willing to forgive you for putting your hand on me."
    else:
        avery "As for you, [mc]. I am willing to forgive your earlier transgressions."
    scene 79_2_s5 with dissolve
    mc "Thank you. But... what would the Queen think? Would she be fine with you doing this to her own daughter?"
    scene 79_2_s6 with dissolve
    avery "You should not concern yourself with that. For now, you look exhausted. Return to your chambers. We will speak more in the morning."
    scene 79_2_s5 with dissolve
    mc "...Alright."

    scene 79_2_s7 with Fade(1.5,1.0,1.0)
    mc "*sigh* (It's for the best. It has to be.)"
    scene 79_2_s8 with Fade(1.5,1.0,1.5)
    play music "nature.mp3" fadein 1.0 volume 0.5 loop
    mc "..."
    mc "(I couldn't sleep... Guess I'll go check on Avery.)"
    stop music fadeout 1.0
    scene 79_2_s9 with Fade(1.5,1.0,1.0)
    play music "tense/lie.mp3" fadein 1.0 volume 0.5 loop
    assassin "...No sign of her, My Lady. The trail ends at the western coast. She has vanished."
    scene 79_2_s10 with dissolve
    avery "You had one job. There will be severe consequences for this failure."
    scene 79_2_s9 with dissolve
    assassin "I understand."
    scene 79_2_s10 with dissolve
    avery "How do you propose we flush her out now? Do you have any conception of how elusive she can be!?"
    assassin "..."
    mc "Lady Avery? Is something wrong?"
    scene 79_2_s11 with dissolve
    avery "Now is {i}NOT{/i} the—"
    scene 79_2_s12 with dissolve
    avery "...Hold on."
    avery "*ahem* [mc]. You do remember Alex, correct? You were the one who found her last time."
    scene 79_2_s13 with dissolve
    mc "Yes, of course. Why? Is she lost again?"
    scene 79_2_s12 with dissolve
    avery "Indeed. And you will help us find her. This will be your new task. A chance to prove your continued value."
    scene 79_2_s13 with dissolve
    mc "I thought I already did that... but alright. I was getting tired of sitting around. Where do I start?"
    scene 79_2_s12 with dissolve
    avery "You'll start by sitting in your room."
    scene 79_2_s13 with dissolve
    mc "What? How am I supposed to help that way?"
    scene 79_2_s12 with dissolve
    avery "Trust me. I have it on good authority that she is trying to get to you. She seeks revenge."
    scene 79_2_s13 with dissolve
    mc "Revenge on me?! For what?"
    scene 79_2_s12 with dissolve
    avery "Who knows what fantasies fester in a traumatized mind, [mc]? Youth and grief make for a volatile concoction."
    avery "We will have time to... question her. We need her alive, after all."
    avery "Now, to your chambers. These gentlemen will ensure you are not hurt."
    scene 79_2_s14 with dissolve
    avery "After him."
    scene 79_2_s15 with dissolve
    assassin "My lady... Are you sure about this? What are the chances she will actually—"
    scene 79_2_s14 with dissolve
    avery "She will be here. She is predictably noble. *chuckles* I assure you."
    scene 79_2_s15 with dissolve
    assassin "As you wish."

    scene 79_2_s16 with Fade(1.0,1.0,1.0)
    mc "So, where are you two from? You don't like regular guards."
    scene 79_2_s54 with dissolve
    guard "..."
    scene 79_2_s16 with dissolve
    mc "I'm talking to you."
    scene 79_2_s17 with dissolve
    guard "Be quiet. Keep walking."
    scene 79_2_s18 with dissolve
    mc "Hey! Who do you think you're talking to?! Don't you know who I am? I'm the Princess's husband!"
    guard "..."
    mc "Tch. That's what I thought."
    stop music fadeout 1.5
    scene 79_2_s19 with Fade(1.0,1.0,1.5)
    mc "This is it. Where will you two stay?"
    scene 79_2_s20 with dissolve
    guard "Do not concern yourself with us. Go about your business as usual."
    scene 79_2_s19 with dissolve
    mc "My business, huh? There's not much of it these days."
    scene 79_2_s33 with dissolve
    scene 79_2_s21 with Fade(1.0,1.0,1.5)
    play music "fire.mp3" fadein 1.0 loop
    env "The moon bids the sun farewell in a hush, and only the crackling fire dares disturb the silence."
    scene 79_2_s22 with dissolve
    mc "*sigh* Hey... You didn't tell me the plan. Shouldn't I be in on it too? What am I supposed to do if she shows up?"
    scene 79_2_s21 with dissolve
    "..."
    perception "A faint scrape at the eastern window. The frame shifts upward, an inch, releasing a small cloud of dust into the air."
    scene 79_2_s23 with dissolve
    mc "Hmm?"
    mc "I think she's here! Hey! What the hell do I do!?"
    "..."
    scene 79_2_s24 with Dissolve(1.2)
    alex "Ahh... Hahh... Fuck. Made it."
    scene 79_2_s25 with Dissolve(1.3)
    alex "[mc]! Thank God you're alive!"
    scene 79_2_s26 with dissolve
    mc "Stay back!"
    scene 79_2_s27 with dissolve
    alex "Why are you backing away? It's me, Alex!"
    scene 79_2_s28 with dissolve
    mc "Why?! You're here to kill me, aren't you? Avery told me!"
    scene 79_2_s55 with dissolve
    alex "Kill you!? What are you—?"
    alex "Look, there's no time! The Queen, she's dead! My father and Av—"
    stop music
    play sound "sound_effects/arrow2.mp3"
    pause(0.28)
    play sound "sound_effects/stab3.mp3"
    scene 79_2_s29 with vpunch
    ""
    play sound "sound_effects/bodydrop3.mp3"
    scene 79_2_s30 with dissolve
    play music "despair.mp3" fadein 1.0 loop
    mc "HAHH!"
    perception "The sentence dies on her lips, replaced by a choked gasp. Her eyes, wide with shock and betrayal, lock onto yours."
    scene 79_2_s31 with dissolve
    mc "W-What... What? Why?"
    mc "Didn't you say you needed her alive!?"
    scene 79_2_s32 with Dissolve(1.0)
    assassin "Confirmed."
    scene 79_2_s34 with Dissolve(1.4)
    assassin "..."
    mc "...H-Hey! Where are you going!?"
    scene 79_2_s35 with Dissolve(1.0)
    mc "Wait!"
    mc "Huh? Why is it closed?!"
    play sound "sound_effects/doors/door_knock_hard2.mp3"
    mc "Open up! I need to talk to Avery! Now!"
    guard "I apologize, sir, but we cannot allow anyone to enter this room. The same goes for leaving it."
    scene 79_2_s36 with dissolve
    mc "Are you fucking kidding me!? Do you expect me to stay in here with a... with a body!?"
    guard "..."
    scene 79_2_s37 with dissolve
    mc "Dammit!"
    scene 79_2_s38 with Dissolve(2.0)
    mc "Hahh... Oh, god..."
    mc "No, no, no, no..."
    scene black with Dissolve(4.0)
    scene 79_2_s39 with Fade(1.0,1.0,1.0)
    avery "Ugh, it reeks in here!"
    assassin "We were awaiting your order, my lady."
    scene 79_2_s40 with dissolve
    avery "And you thought leaving her to rot in here was the best course of action?"
    assassin "..."
    avery "*sigh* Just get this thing out of here. Take it far into the woods and burn it. Leave no trace."
    scene 79_2_s41 with dissolve
    avery "[mc]. I must extend my gratitude. Your presence was the perfect lure. You will be rewarded handsomely for your service."
    avery "I have procured a manor near the castle grounds for you. You will live there from now on. A comfortable retirement, far from the tedious affairs of the castle."
    scene 79_2_s42 with dissolve
    mc "...What happened to the Queen?"
    scene 79_2_s41 with dissolve
    avery "My dear sister tragically died at sea. A storm, they say. A terrible accident. I will assume the role of Queen from now on."
    scene 79_2_s42 with dissolve
    mc "Good for you."
    scene 79_2_s41 with dissolve
    avery "You may leave now, [mc]. Your service is no longer required."
    mc "..."
    avery "I will not repeat myself. Or would you rather my guards escort you?"
    scene 79_2_s42 with dissolve
    mc "I'm leaving."
    scene 79_2_s45 with Fade(1.5,1.0,1.0)
    ""
    scene 79_2_s46 with Dissolve(1.4)
    ""
    scene 79_2_s45 with Dissolve(1.4)
    ""
    scene 79_2_s43 with Dissolve(1.4)
    ""
    scene 79_2_s44 with Dissolve(1.4)
    ""
    scene 79_2_s47 with Dissolve(1.4)
    mc "Rebecca!"
    scene 79_2_s48 with dissolve
    r "..."
    mc "Talk to me! Please..."
    scene 79_2_s49 with dissolve
    r "..."
    scene 79_2_s50 with Fade(1.5,1.0,1.0)
    avery "Farewell, [mc]."
    avery "Now that this is settled, I need groups to sweep the western coast. She might have had allies. I want them rooted out."
    assassin "Yes, Your Majesty."
    impulse "You know will happen when you leave that door. Take her out. A last act to restore some dignity to your pathetic life."
    mc "(I can't...)"
    scene 79_2_s51 with Fade(1.5,1.0,1.0)
    mc "..."
    scene 79_2_s52 with Dissolve(1.4)
    mc "*chuckles* I had a good thing going."
    scene 79_2_s53 with Dissolve(1.4)
    env "The shadow of a once great city sinks deeper into darkness, its last spark of hope extinguished."
    return

label scene79_1:
    $ mc_save_maia = True
    scene 79_s31 with dissolve
    mc "So be it."
    scene 79_s33 with Fade(1.0,1.0,1.0)
    ""
    scene 79_s34 with dissolve
    negumi "Oh, you're back!"
    scene 79_s35 with Dissolve(1.2)
    negumi "So? Are you going after her?"
    mc "Yeah. I am."
    scene 79_s36 with dissolve
    negumi "Good. Let's get out of here. The guards have been giving me the side-eye for ten minutes straight. I think they're still sore about the whole 'trespassing' thing."
    scene 79_s37 with dissolve
    mc "You're coming with me?"
    scene 79_s36 with dissolve
    negumi "Why not? I'm the one who dragged you into this mess. I have to see it through."
    negumi "Besides... it's been way too long since I've had any real action. The great Negumi is getting rusty."
    scene 79_s37 with dissolve
    mc "Thank you, Negumi. Really."
    scene 79_s36 with dissolve
    negumi "*giggles* Hey, don't go getting all sentimental on me. I told you, I'm doing this for myself. Now come on. The damsel's waiting."
    scene 79_s37 with dissolve
    stop music fadeout 1.0
    scene 79_s39 with Fade(1.5,1.0,1.0)
    play music "night.mp3" fadein 1.0 loop
    negumi "You must really love her, going to these lengths."
    mc "It's not about love. Ever since I came to this world... she's the one person I genuinely believe deserves happiness."
    negumi "Came to this world?"
    mc "Let's keep moving."
    scene 79_s40 with Fade(1.0,1.0,1.0)
    negumi "This is the place... but it's way too quiet. Last time I was here, some drunk guys were singing and dancing. Really badly."
    mc "Where's your staff, by the way?"
    negumi "Don't worry about it. I can summon it whenever I want."
    negumi "Place is giving me the creeps... Come on, we can sneak through a window in the back."
    call screen scene79_choice03 with dissolve

label scene79_choice03_op1:
    $ mc_sneak_abel = True
    mc "Show me where that window is."
    negumi "Over here!"
    scene 79_s42 with dissolve
    negumi "Alright... slow at first. Just ease it in."
    mc "Like this?"
    negumi "Yes, just like that... perfect. Don't rush it."
    negumi "Wait! Be more gentle! You're gonna break it!"
    mc "I thought you said use more force—"
    negumi "Not yet! We're not even inside! You have to tease it a little first."
    negumi "Yes, right there! Keep going, keep going... almost... almost...!"
    scene 79_s43 with dissolve
    negumi "Oh Gods, yes! Finally!"
    mc "I can't believe that actually worked..."
    stop music fadeout 2.0
    scene 79_s45 with Fade(0.5,0.5,0.5)
    negumi "Hmm? There really is no one here. I guess we could've just went through the front door..."
    able "*groan* Why did everyone leave all of a sudden?"
    able_girl "N-Not sure, sir. But I heard that all shops in the vicinity should close immediately."
    able "Close? Who gave the order? Certainly wasn't me!"
    able_girl "..."
    mc "Let's rush him."
    negumi "Right behind you."
    play music "angry/anger.mp3" fadein 1.0 loop
    jump scene79_1_2

label scene79_choice03_op2:
    stop music fadeout 1.0
    play sound "sound_effects/doors/door_kick.mp3"
    scene 79_s41 with vpunch
    negumi "...Or we could do that."
    play music "angry/anger.mp3" fadein 1.0 loop
    scene 79_s44 with dissolve
    able_girl "Ahh!"
    able "Huh!? What the—!?"
    jump scene79_1_2

label scene79_1_2:
    play sound "sound_effects/doors/wood_break.mp3"
    scene 79_s46 with vpunch
    pause(0.35)
    stop sound
    mc "Where is she!"
    scene 79_s47 with dissolve
    if mc_sneak_abel:
        able "Gahgh! W-Where did you come from!?"
        able_girl "Ahh!"
    else:
        able "Gahgh! W-What are you talking about!?"
    scene 79_s46 with dissolve
    mc "Maia! Where did you take her!?"
    scene 79_s47 with dissolve
    able "Get—get the hell off me!"
    able "Dammit! Vic! Denovan! Where is everyone!?"
    scene 79_s49 with dissolve
    negumi "That's what I'm wondering too. This place is usually packed, day or night."
    scene 79_s48 with dissolve
    able "Help me you bitch! Get the dagger underneath the counter!"
    scene 79_s49 with dissolve
    able_girl "P-Please don't hurt me!"
    mc "Do I need to beat it out of you!? Where is she!?"
    negumi "I know where the cellar is, [mc]. Don't waste your breath on this filth. Just bring him with us."
    call screen scene79_choice04 with dissolve

label scene79_choice04_op1:
    play sound "sound_effects/punch.mp3"
    scene 79_s50 with vpunch
    perception "Your fist crashes into his face. He drops, stunned for a heartbeat before blinking back to consciousness."
    scene 79_s51 with dissolve
    able "Hahh... Wha-"
    mc "I won't ask again."
    able "F... Fuck you..."
    impulse "He's resilient. I bet another punch will loosen his tongue."
    play sound "sound_effects/punch3.mp3"
    scene 79_s52 with vpunch
    perception "Your knuckles connect even harder. The back of his skull smacks against the solid wood of the bar. His eyes roll back, his body going limp for a moment."
    scene 79_s53 with dissolve
    negumi "Are you finished? Or should I also get a turn?"
    scene 79_s54 with dissolve
    mc "Sorry... Had to let it out on somebody."
    mc "Get up. You're coming with us."
    able "Ahhng... You're dead... you're both fuckin dead..."
    jump scene79_1_3

label scene79_choice04_op2:
    scene 79_s54 with dissolve
    mc "*sigh* Take me to her, Negumi. Quick."
    mc "Get up. You're coming with us."
    able "Ahhng... You're dead... you're both fuckin dead..."
    jump scene79_1_3

label scene79_1_3:
    scene 79_s55 with Fade(1.0,1.0,1.0)
    negumi "Over here! This closet is a fake."
    negumi "Help me push."
    scene 79_s56 with Fade(0.5,0.5,0.5)
    perception "You move the closet and a damp, foul breath of rot and human misery washes over you. This place was never meant to be found."
    scene 79_s57 with dissolve
    mc "Open the gate."
    able "{i}Ptoo{/i}! Fuck you!"
    play sound "sound_effects/doors/iron_door_slam.mp3"
    scene 79_s58 with vpunch
    mc "I said open—!"
    mc "Oh..."
    scene 79_s59 with dissolve
    play sound "sound_effects/body/body_falling.mp3"
    perception "His body tumbles down the stairs like a puppet, limbs flailing, cracking against every corner and step. He hits the bottom with a crunch, his knee folding backward beneath him."
    able "AAAGH—FUCK! My leg! It's fucking backwards!"
    mc "..."
    negumi "Ouch..."
    scene 79_s60 with Dissolve(1.5)
    mc "Holy shit..."
    negumi "Crazy, right? Thankfully, they're all empty. Except for one."
    scene 79_s61 with dissolve
    negumi "Here."
    able "Ahhng... My fucking leg!"
    scene 79_s63 with dissolve
    mc "Maia!"
    m "Hmmnnn..."
    mc "I'll get you out of here."
    scene 79_s62 with dissolve
    m "Is... Is that you... [mc]?"
    scene 79_s63 with dissolve
    mc "It's me. Don't worry, I'm getting you out."
    mc "Goddammit! Where are the keys, Able!?"
    scene 79_s64 with dissolve
    negumi "Move, I got this."
    sensation "Negumi's staff begins to glow with intense heat. The air shimmers around the lock."
    mc "Careful."
    m "I-It hurts... So hot...!"
    negumi "Just a few more seconds. Breathe."
    play sound "sound_effects/metal_clink.mp3"
    scene 79_s65 with dissolve
    negumi "There!"
    perception "The chain clicks open and with Maia having no strength to hold herself up. She crumples to the floor."
    scene 79_s66 with Dissolve(1.5)
    m "Ahhnn..."
    mc "Did he touch you? Are you injured?"
    scene 79_s67 with dissolve
    m "Just... so tired. Haven't eaten... days... I can't feel my legs..."
    scene 79_s66 with dissolve
    negumi "This is great and all, but we really should get out of here. This place is still giving me the creeps."
    mc "Can you walk, Maia?"
    scene 79_s67 with dissolve
    m "Gahhn! I can't... I'm so sorry, [mc]."
    scene 79_s66 with dissolve
    mc "It's fine. I've got you."
    scene 79_s69 with dissolve
    mc "You."
    scene 79_s70 with dissolve
    able "She's mine, [mc]! Legally, I have the papers right—"
    scene 79_s71 with dissolve
    mc "There is no depth low enough for you, is there?"
    scene 79_s70 with dissolve
    able "Please! I can... I can give you whatever you want! What is it? Money? Women? Power? I can make you a king in this city, [mc]! I have the connections!"
    able "Just name it! And it's yours, my friend! You have to let me go!"
    scene 79_s72 with Dissolve(1.5)
    mc "You'll just come after us."
    scene 79_s116 with dissolve
    able "No! I promise I wont! No one will hear a word of what happened today!"
    scene 79_s73 with dissolve
    negumi "He's not worth it, [mc]. Let me burn a shackle to his hand instead. Melt it right into the bone so he never forgets what he is."
    scene 79_s116 with dissolve
    mc "..."
    scene 79_s74 with dissolve
    play sound "sound_effects/unsheathe2.mp3"
    m "—hangh!"
    mc "Wha—!?"
    play sound "sound_effects/bodydrop.mp3"
    stop music fadeout 2.0
    scene 79_s75 with vpunch
    able "W-What is she—? S-Stop her!"
    play sound "sound_effects/stab1.mp3"
    scene 79_s76 with dissolve
    m "AHH! AHH! AHH!"
    play sound "sound_effects/stab3.mp3"
    scene 79_s77 with dissolve
    able "Stop—guhh—stop—!"
    play sound "sound_effects/stab1.mp3"
    scene 79_s76 with dissolve
    negumi "Shit! [mc]!"
    play sound "sound_effects/stab3.mp3"
    scene 79_s78 with dissolve
    scene 79_s79 with dissolve
    empathy "She stabs again. And again. There is no technique, only pure vengeance. Each tearing impact is a word in a silent scream she's held inside for years."
    scene 79_s80 with dissolve
    mc "Stop, Maia! That's enough!"
    mc "He's dead. It's over."
    scene 79_s81 with dissolve
    play music "sad/maia2.mp3" fadein 3.0 loop
    m "Haaaahhhhh!"
    empathy "This isn't the cry of a killer, but of a victim finally breaking her chains. Every sob is a piece of the fear she's lived in for so long."
    scene 79_s82 with Dissolve(2.0)
    mc "Look at me!"
    mc "I've got you. You're safe now."
    mc "He was an awful man. The world is better off without him. You did {i}nothing{/i} wrong."
    scene 79_s83 with dissolve
    m "*sniff* I... I..."
    scene 79_s82 with dissolve
    mc "Come on, I'll clean you up. Let's leave this place. For good."
    stop music fadeout 15.0
    scene 79_s84 with Fade(1.5,1.0,1.0)
    ""
    scene 79_s85 with dissolve
    able_girl "Wait! P-Please! Take me with you! When they find him... they'll blame me! They'll kill me!"
    scene 79_s86 with dissolve
    mc "What?"
    scene 79_s85 with dissolve
    able_girl "H-He's dead right? I know the back alleys! I can lead us out, away from the city walls! We can disappear!"
    scene 79_s86 with dissolve
    mc "Away from the city? Why would we need to leave?"
    scene 79_s85 with dissolve
    able_girl "W-Why?"
    scene 79_s86 with dissolve
    negumi "She's right. You can't just go back to the castle for tea after this. We're basically fugitives now."
    negumi "We have to leave until the heat dies down. And we can't just leave her here. She's a witness."
    call screen scene79_choice05 with dissolve

label scene79_choice05_op1:
    $ mc_accept_ablegirl = True
    mc "Fine. Lead the way. But I swear if you do anything stupid."
    scene 79_s87 with dissolve
    able_girl "Thank you! I won't!"
    scene 79_s88 with Dissolve(1.0)
    able_girl "There's a secret alley behind the tavern. Follow me!"
    scene 79_s117 with dissolve
    play sound "sound_effects/arrow2.mp3"
    pause(0.35)
    play sound "sound_effects/stab3.mp3"
    scene 79_s92 with dissolve
    perception "The moment she steps out, a crossbow bolt thwips through the air, striking her square in the neck. She collapses without a sound."
    play sound "sound_effects/bodydrop.mp3"
    scene 79_s93 with dissolve
    mc "NO!"
    negumi "Oh... fuck..."
    mc "Dammit!"
    jump scene79_1_4

label scene79_choice05_op2:
    mc "No. You stay here. I don't know you, and I don't trust you."
    scene 79_s85 with dissolve
    able_girl "Please, you have to! I was nothing to them! Just a serving girl!"
    scene 79_s86 with dissolve
    mc "My answer is no. I'm not risking our lives on your word. Stay."
    scene 79_s85 with dissolve
    able_girl "Hah... oh Gods... they'll kill me..."
    scene 79_s89 with dissolve
    negumi "Let's go."
    scene 79_s91 with Dissolve(1.0)
    mc "Shit!"
    jump scene79_1_4

label scene79_1_4:
    play music "angry/anger.mp3" fadein 1.0 loop
    scene 79_s94 with dissolve
    if mc_accept_ablegirl:
        d "One more step and you will get the same fate! Put down your weapons and surrender! Now!"
    else:
        d "Not one more step! Put down your weapons and surrender! Now!"
    scene 79_s95 with dissolve
    mc "Darius! Let me explain!"
    scene 79_s94 with dissolve
    d "You can explain everything later, [mc]. For now, I need you to surrender."
    d "Please."
    scene 79_s96 with dissolve
    negumi "*chuckles* Well... this is not how I imagined my morning going."
    mc "What are you laughing for?"
    scene 79_s97 with Dissolve(1.0)
    d "Hmm?"
    scene 79_s98 with dissolve
    d "What?! On whose authority!?"
    scene 79_s99 with dissolve
    guard "Direct from the Lady Regent, sir. Orders are absolute."
    scene 79_s100 with Dissolve(1.0)
    d "Dammit, [mc]! Why!? What did you do to make her issue a kill-on-sight order!?"
    scene 79_s101 with dissolve
    mc "A {i}what!?{/i} What are you talking about!?"
    scene 79_s100 with dissolve
    d "...I'm sorry."
    scene 79_s102 with dissolve
    d "Archers! Loose!"
    scene 79_s103 with dissolve
    mc "Wait!"
    play sound "sound_effects/magic/magic_shield.mp3"
    scene 79_s104 with dissolve
    mc "Huh?"
    #play sound "sound_effects/arrow/arrow_barrage.mp3"
    scene 79_s105 with dissolve
    mc "Negumi?"
    negumi "Heh. You really thought a few pointy sticks could penetrate my shield? Pathetic!"
    guard "Captain! The mage!"
    scene 79_s106 with dissolve
    negumi "Run, [mc]."
    scene 79_s107 with dissolve
    mc "What? No! I'm not leaving you!"
    scene 79_s106 with dissolve
    negumi "You're carrying dead weight and no weapon. You'll die in the first three seconds. Take Maia and go."
    scene 79_s107 with dissolve
    mc "Negumi—"
    scene 79_s106 with dissolve
    negumi "Don't worry about me. I won't fall here. I've been on a leash for years... Today it comes off."
    scene 79_s107 with dissolve
    mc "What are you—?"
    scene 79_s106 with dissolve
    negumi "I apologize Ena, but I have to break my promise to you."
    play sound "sound_effects/magic/magic_fire.mp3" volume 0.5
    scene 79_s108 with Dissolve(1.5)
    perception "She raises her staff and the tip ignites with a blood-red flame. The stone floor at her feet cracks, spider-webbing outward to form an enormous circle of glowing, ancient script. The air shimmers with visible waves of blistering heat."
    mc "Nghn!"
    m "...[mc]! I-I'm burning up!"
    negumi "Goddess of fire, I beseech thee, bring flame..."
    negumi "You have ten seconds. After that, everything around us will be ash."
    scene 79_s109 with Dissolve(1.5)
    mc "I'll... I'll come back for you, Negumi! I Promise!"
    negumi "Sure. Now, scram."
    scene 79_s110 with Dissolve(1.0)
    guard "Captain! What in the Gods' names is that!? Should we charge!?"
    guard "It's getting hotter! I-I feel my armor melting!"
    scene 79_s111 with Dissolve(1.0)
    d "TAKE COVER! GET AWAY FROM THE CIRCLE! FALL BACK!"
    scene 79_s112 with Dissolve(2.0)
    mc "Hahh! Hah!"
    play sound "sound_effects/magic/explosion.mp3"
    scene 79_s113 with vpunch
    sensation "A deafening roar tears through the air, followed by a shockwave that slams into your back, rattling your bones and popping your eardrums. The force nearly sends you stumbling."
    scene 79_s114 with dissolve
    mc "Holy shit! Negumi!"
    stop music fadeout 1.4
label scene80:
    scene 80_s1 with Fade(1.5,1.0,1.0)
    play music "nature.mp3" fadein 1.0 loop
    mc "Hahh... Ahh... (Fuck, I should've went to get [horse].)"
    m "Wha... What is happening, [mc]?"
    scene 80_s2 with dissolve
    mc "Don't worry. I think we're almost out. We just have to—"
    scene 80_s3 with dissolve
    mc "..."
    scene 80_s4 with dissolve
    m "Why did we stop—"
    scene 80_s5 with dissolve
    stop music fadeout 1.0
    shiver "He stares you down. His helmet hides his eyes, but it does nothing to dim the sensation of his gaze."
    play music "fear/creeping_death.mp3" fadein 1.0 loop
    scene 80_s6 with Dissolve(1.0)
    m "[mc]! No! Y-You should run!"
    mc "There's no running from this one, Maia. Stay here."
    scene 80_s7 with Dissolve(1.5)
    mc "So, Avery sent you to finish the job, huh?"
    mc "Is there even someone behind that armor? Are you capable of thinking by yourself?"
    scene 80_s8 with Dissolve(1.0)
    mc "Let's get this over with."
    play sound "sound_effects/sword/sword_swing1.mp3"
    scene 80_s9 with Dissolve(0.3)
    scene 80_s9 with vpunch
    perception "His greatsword sweeps sideways in a silver arc meant to behead you."
    play sound "sound_effects/metal_hit.mp3"
    scene 80_s10 with Dissolve(0.3)
    scene 80_s10 with vpunch
    perception "You drop, feeling the wind of the blade pass over your head, and lunge forward, driving your shoulder into his midsection."
    mc "Hngh! (Damn, he's like a stone!)"
    play sound "sound_effects/punch4.mp3" volume 0.2
    scene 80_s11 with dissolve
    scene 80_s11 with vpunch
    mc "AGHK!"
    scene 80_s12 with dissolve
    mc "...Can't... breathe..."
    play sound "sound_effects/slash03.mp3"
    scene 80_s13 with Dissolve(0.3)
    scene 80_s13 with vpunch
    m "[mc]!"
    scene 80_s14 with dissolve
    mc "(That was close...)"
    scene 80_s15 with dissolve
    mc "(Oh, shit!)"
    scene 80_s16 with dissolve
    ""
    scene 80_s17 with Dissolve(0.3)
    play sound "sound_effects/metal_ting.mp3" volume 0.5
    scene 80_s17 with vpunch
    mc "Hng!"
    logic "The dagger!"
    scene 80_s18 with dissolve
    ""
    play sound "sound_effects/punch2.mp3"
    scene 80_s19 with Dissolve(0.3)
    scene 80_s19 with vpunch
    mc "(Fuck! He caught it!)"
    play sound "sound_effects/metalhit3.mp3" volume 0.5
    scene 80_s20 with vpunch
    sensation "A jolt of pain rockets up your arm, but you feel his grip on your wrist loosen for a fraction of a second."
    mc "(Now's my chance!)"
    scene 80_s21 with dissolve
    perception "As his sword slides off your shoulder, you twist your dagger hand free and thrust upward, aiming for the narrow slit of his helmet."
    mc "GOT YOU NOW, YOU PIECE OF SHIT!"
    play sound "sound_effects/slash03.mp3"
    scene 80_s22 with Dissolve(0.3)
    scene 80_s22 with vpunch
    perception "You see the silver arc of the blade, impossibly fast. There is no pain at first—only a shocking impact that travels up your shoulder."
    scene 80_s23 with dissolve
    mc "Huh...?"
    perception "You watch, detached, as your own left hand falls to the ground."
    scene 80_s24 with dissolve
    mc "Hahh... Ahh— AAAAAGH!"
    m "[mc]!"
    m "Watch out!"
    scene 80_s25 with dissolve
    ""
    play sound "sound_effects/arrow2.mp3"
    pause(0.35)
    play sound "sound_effects/metal_arrow.mp3"
    scene 80_s26 with vpunch
    ""
    stop music fadeout 0.5
    scene 80_s27 with dissolve
    stop music fadeout 0.5
    alex "Back off!"
    play music "battle02.mp3" fadein 1.0 loop
    scene 80_s28 with dissolve
    play sound "sound_effects/metal_hit.mp3"
    scene 80_s28 with vpunch
    alex "Aaagh!"
    scene 80_s29 with Dissolve(0.3)
    scene 80_s29 with vpunch
    ""
    scene 80_s30 with dissolve
    alex "Come on! Before he gets back up!"
    mc "..."
    alex "[mc]!"
    mc "Y-Yeah... hah... alright..."
    scene 80_s31 with Dissolve(1.5)
    alex "You too!"
    scene 80_s32 with Dissolve(1.3)
    alex "Let's go, boy."
    m "[mc], are you alright?"
    mc "..."
    alex "Stay with me, [mc]! Just hold it tight!"
    scene 80_s33 with dissolve
    alex "Is he still after us?"
    mc "What the—!?"
    scene 80_s34 with dissolve
    mc "Alex! Turn right!"
    alex "This fucker doesn't know when to quit."
    scene 80_s35 with dissolve
    mc "Hngh!"
    play sound "sound_effects/woosh1.mp3"
    scene 80_s36 with dissolve
    alex "[mc]?!"
    scene 80_s37 with dissolve
    mc "Hahh... Caught his sword..."
    mc "S-So heavy!"
    alex "Let go of it. You need to hold your wound."
    m "I-I'll do it!"
    scene 80_s38 with dissolve
    mc "Where... hahn... are we going...?"
    alex "Western coast. I found an abandoned shack there when I arrived. We'll hold out there."
    mc "Fuck... I don't... I don't know if I'll..."
    m "[mc]! Please! Don't close your eyes!"
    alex "We'll have to go through the mountain. Hold on."
    stop music fadeout 1.5
    scene 80_s39 with Fade(1.5,1.0,2.0)
    play music "blizzard.mp3" fadein 1.0 loop
    mc "A-Alex... I... hngh... can't... hold on..."
    scene 80_s40 with Dissolve(1.5)
    sensation "You feel your grip slipping away. You're body going more and more limp."
    m "[mc]!"
    play sound "sound_effects/bodydrop3.mp3"
    scene 80_s41 with vpunch
    m "[mc]! [mc]!"
    scene 80_s42 with dissolve
    m "You! Come back! He fell!"
    mc "Maia... look... look for a cave... or... anything..."
    scene 80_s43 with dissolve
    m "Hah...? I— I can't see anything."
    m "Hnn... O-Over there! That dark spot, near the rocks!"
    mc "Let's go... Before... we freeze..."
    scene 80_s44 with Dissolve(1.5)
    m "Hnnnggg!"
    scene 80_s45 with Fade(1.0,0.5,0.5)
    m "Is this good?"
    scene 80_s46 with dissolve
    mc "...Mhm."
    scene 80_s45 with dissolve
    m "It's so cold... I can't feel my toes..."
    scene 80_s46 with dissolve
    mc "Get... close to me. Share... body heat."
    scene 80_s47 with dissolve
    m "Oh, [mc]... What are we going to do now...? There's... there's nowhere left for us."
    mc "..."
    m "[mc]?"
    scene 80_s48 with Dissolve(2.0)
    sensation "Your body has consumed the last dregs of its strength. A deep, unnatural cold is seeping into your core, a cold that has nothing to do with the storm."
    stop music fadeout 4.0
    scene black with Fade(1.0,1.0,1.0)
    sensation "Your eyelids grow heavy, and the darkness at the edges of your vision is swallowing the world."
    play music "breakup.mp3" fadein 10.0 loop
    scene 80_s49 with Fade(1.0,1.0,2.0)
    ex "Isn't it romantic?"
    mc "It's... something."
    scene 80_s50 with Dissolve(1.0)
    ex "Shut up. I see that smile."
    scene 80_s51 with dissolve
    mc "*chuckles* Fine. I like it."
    scene 80_s52 with Dissolve(1.0)
    ex "Brrr—Jesus, it's freezing..."
    scene 80_s54 with Dissolve(1.0)
    mc "Come here."
    scene 80_s53 with dissolve
    ex "Nothing can stop us. Not the cold. Not anything. As long as we're together... right?"
    scene 80_s54 with dissolve
    mc "Right."
    scene 80_s55 with Dissolve(4.0)
    mc "...Liar."
    scene 80_s56 with Dissolve(1.0)
    mc "Huh...? Maia? Maia, wake up."
    mc "UGHN! My hand!"
    stop music fadeout 6.0
    scene 80_s57 with dissolve
    mc "No, no, no... Your temperature! I have to get you warm..."
    scene 80_s58 with Fade(1.0,1.0,1.0)
    play music "wind2.mp3" fadein 1.0 volume 0.5 loop
    mc "Hahh... ahahh... nghn..."
    scene 80_s59 with Dissolve(1.4)
    mc "Just... keep going west... just west..."
    scene 80_s60 with Dissolve(1.4)
    mc "No! Come on! Just a little... further!"
    scene 80_s61 with Dissolve(0.3)
    play sound "sound_effects/bodydrop4.mp3"
    scene 80_s61 with vpunch
    ""
    scene 80_s62 with Dissolve(2.0)
    ""
    stop music fadeout 2.0
image 81_a_d1 = Movie(play="images/chapter4/scene81/81_a_d1.webm", loop=True)
image 81_a_d2 = Movie(play="images/chapter4/scene81/81_a_d2.webm", loop=True)

image 81_a_p1 = Movie(play="images/chapter4/scene81/81_a_p1.webm", loop=True)
image 81_a_p2 = Movie(play="images/chapter4/scene81/81_a_p2.webm", loop=True)

label scene81:
    scene 81_s1 with Fade(2.0,1.0,2.0)
    ""
    play music "fire.mp3" fadein 3.0 volume 0.6 loop
    scene 81_s3 with dissolve
    reham "I found them at the doorstep. He was still holding onto her. The girl... she was barely clinging to life."
    scene 81_s2 with dissolve
    alex "Someone brought them here?!"
    scene 81_s3 with dissolve
    reham "I doubt they meant harm. Why leave them like that on our step?"
    scene 81_s2 with dissolve
    alex "I hope you're right. Thank you, Reham. I lost them in the blizzard. I didn't even realize they'd fallen."
    scene 81_s3 with dissolve
    reham "Of course."
    scene 81_s2 with dissolve
    alex "Will he... live?"
    scene 81_s3 with dissolve
    reham "The cold cauterized the wound and slowed the bleeding. It's the only reason his heart is still beating. The infection is the real battle now."
    scene 81_s4 with Dissolve(1.0)
    alex "*sigh* And the girl?"
    scene 81_s5 with Dissolve(2.0)
    reham "It's not good. Her temperature was dangerously low. I can't just put her too close by the fire, the shock could stop her heart. She has to warm slowly, from the inside out."
    alex "This whole situation... Ugh... It's a tangled mess."
    reham "One thread at a time. You'll unravel it."
    alex "I just need him alive. That's the priority."
    reham "If you don't mind my asking, why is he so important to you?"
    alex "He... was a witness. To the massacre at the manor. It's the reason Avery wants him dead."
    alex "If he can give his testimony... it might change everything."
    reham "Hmm... I see. Well, I'll do everything I can for him. You have my word."
    alex "Thank you."
    scene 81_s6 with dissolve
    alex "I'm gonna go ahead and scout the area. We're still too close to the city for comfort."
    reham "You're not taking the crossbow?"
    alex "No one's going to see me."
    reham "Alright. Be careful."
    stop music fadeout 1.0 
    scene 81_s7 with Fade(1.0,1.0,1.4)
    play music "nature.mp3" fadein 1.0 loop
    ""
    scene 81_s8 with Dissolve(1.0)
    alex "Hmm? Oh—shit."
    scene 81_s9 with Dissolve(1.2)
    guard_stern "...found the market completely destroyed. The blast... it was like a hundred cannons fired at once. That mage, Negumi, they say she did it before she vanished."
    guard_concerned "Fucking hell... How is this not the only thing people are talking about?"
    guard_stern "Same reason you hadn't heard. The Lady Regent is controlling the story. You'd think the Princess conspiring with her husband to murder Able and take control of the market would be the scandal of the decade."
    guard_concerned "I still don't get it. Why would the Princess be involved? What's her angle?"
    guard_stern "She'll have to answer for it when Her Majesty returns."
    guard_concerned "*sigh* Do you actually believe the Princess was in on it? With that outsider? Hell, I didn't even know she was married to begin with."
    guard_stern "That's what the rumors say. But I doubt Lady Avery will do anything without Her Majesty's command. It's too bold, even for her."
    scene 81_s10 with Dissolve(1.0)
    guard "Hey! Enough gossiping like fishwives. Eyes open."
    alex "(The Princess? Of course. Avery, you vicious bitch. You won't leave anyone behind.)"
    scene 81_s11 with dissolve
    alex "Nghn!"
    alex "(No, no, no, no! Not now!)"
    scene 81_s12 with dissolve
    alex "(I can't... take it anymore... I have to~!)"

    if mc_paricipated_festival:
        if mc_masturbated_to_alex:
            jump scene81_alex
        else:
            scene 81_s91 with Dissolve(1.0)
            alex "Nghn...! (I can do this. You held back that day while staring at me like you wanted to devour me, but you stopped yourself...)"
            alex "(You showed restraint... so I will too.)"
            scene 81_s19 with dissolve
            alex "(I'll head back.)"
            jump scene81_alex2
    else:
        scene 81_s94 with Dissolve(1.0)
        alex "Nghn...! (I can do this. You held back that day from joining the stupid breeding festival...)"
        alex "(You showed restraint... so I will too.)"
        scene 81_s19 with dissolve
        alex "(I'll head back.)"
        jump scene81_alex2

label scene81_alex:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene7_p6_replay:
        $ persistent.scene7_p6_replay = True
        
    if persistent.alex_p: 
        scene 81_s92 with Dissolve(1.0)
        alex "(Dammit, [mc]... You just had to use my body like that... stroking yourself while I was right there...)"
        alex "(You really didn't notice me watching? The way your eyes burned into me... like you wanted to pin me down and take what you needed...)"
        alex "(Fuck... why is that image stuck in my head now? Your grip, your breath, the hunger on your face...)"
        scene 81_s12 with dissolve
        alex "(Just... Just a quick one.)"
        show 81_a_p1 with dissolve
        alex "Mhmmnnn... (Already soaked... just from remembering how you looked at me...)"
        alex "(Y-yes... ahhnn~ My clit's throbbing... been aching since I saw you like that~)"
        alex "(Come on... let it build... imagine it's your fingers instead...)"
        alex "(Fuck... I don't know if I would've refused if you asked to fuck me outright.)"
        alex "(You would've taken me right there. Bent me over, pushed inside... my body would've opened for you... begged without words...)"
        alex "Hahn~ Mhmnn~ (God, I'm dripping...)"
        show 81_a_p2 with dissolve
        hide 81_a_p1
        alex "Mhmmnnn... (See what you did?!)"
        alex "Mhmnn~ (Fuck... imagining your big manly hands instead of mine...)"
        alex "(Fuck!) Ngh... (you cursed... piece of shit)"
        alex "(Making me want this... making me ache...)"
        alex "(Right there~!) Hahhn~ Yeeaaass~"
        alex "(God, I want a cock so bad... want it to fill me, ruin me... make me forget everything...)"
        alex "(I'm such a fucking slut! Got so wet from just that. From being treated like furniture.)"
        alex "I'm...! I'mmm...!"

        scene 81_s13 with vpunch
        alex "NGHAAAAA—!"
        scene 81_s14 with Dissolve(1.3)
        alex "Hahh... Ahhnn... fuck..."
        alex "(Faaauck... I got it all over my socks... great.)"
        alex "(No. It's fine. This should make my head clear for a few days.)"
        scene 81_s16 with Dissolve(1.0)
        guard "Did you hear that? Sounds like... moaning. Up there."
        $ renpy.end_replay()

    elif persistent.alex_d:
        scene 81_s93 with Dissolve(1.0)
        alex "(Dammit, [mc]... You just had to use my body like that... stroking yourself while I was right there...)"
        alex "(You didn't even see how hard I got, did you? How my little cock twitched just from your eyes on me...)"
        alex "(Fuck... why is that image stuck in my head now? Your grip, your breath, the hunger on your face...)"
        scene 81_s12 with dissolve
        alex "(Just... Just a quick one.)"
        show 81_a_d1 with dissolve
        alex "Mhmmnn... (So pathetic... getting this hard from being your fantasy...)"
        alex "(Y-Yes... Ahhnn~ Look at me leaking already~ My poor little thing can't help it...)"
        alex "(Fuck... I don't know if I would've refused if you asked to fuck me outright.)"
        alex "(You would've taken me right there. Bent me over. And my body would've let you... even begged for it.)"
        alex "(Come on... Just... Let it all out~!) Hahn~"
        alex "Mhmnn~"
        show 81_a_d2 with dissolve
        hide 81_a_d1
        alex "(My own damn body reacted like a slut. Got hard from just that. From being treated like furniture.)"
        alex "(Fuck!) Ngh... (You cursed... piece of shit.)"
        alex "(Making me need this... making me empty...)"
        alex "(Right there~! Hahhn~ Yes~ Don't stop~)"
        alex "(My cum's useless anyway... can't even breed... just pretty little spurts for you to laugh at...)"
        alex "(Grab my tiny cock and thrust your real one inside me~!)"
        alex "I'm...! I'mmm...!"
        scene 81_s17 with vpunch
        alex "NGHAAAAA—!"
        scene 81_s18 with vpunch
        alex "Ahnn!"
        scene 81_s15 with Dissolve(1.3)
        alex "Hahh... Ahhnn..."
        alex "(Dammit... came like a fountain again...)"
        alex "(No. It's fine. This should make my head clear for a few days.)"
        scene 81_s16 with Dissolve(1.0)
        guard "Did you hear that? Sounds like... moaning. Up there."
        alex "(Shit. Time to move.)"
        $ renpy.end_replay()
    jump scene81_alex2
    
label scene81_alex2:
    stop music fadeout 1.0
    scene 81_s20 with Fade(1.5,1.0,2.0)
    play music "fire.mp3" fadein 3.0 volume 0.6 loop
    ""
    scene 81_s21 with Dissolve(1.0)
    reham "Welcome back."
    scene 81_s22 with Dissolve(1.0)
    alex "Any change?"
    scene 81_s23 with dissolve
    reham "Sorry, no. His body is fighting the infection. Hers is... slowly warming. It will take time."
    scene 81_s95 with Dissolve(1.0)
    alex "..."
    scene 81_s24 with dissolve
    reham "So."
    scene 81_s95 with dissolve
    alex "Hmm?"
    scene 81_s24 with dissolve
    reham "You want to talk about it?"
    scene 81_s25 with dissolve
    alex "About what?"
    scene 81_s24 with dissolve
    reham "The curse inside you. I've been tending wounds long enough to know when one isn't on the skin."
    scene 81_s25 with dissolve
    alex "I don't."
    scene 81_s95 with dissolve
    reham "..."
    scene 81_s26 with dissolve
    alex "It's... It's not good."
    scene 81_s24 with Dissolve(1.0)
    reham "I gathered as much."
    scene 81_s25 with dissolve
    alex "*sigh* And now I'll have to live with it. Forever."
    scene 81_s24 with dissolve
    reham "Why do you say that?"
    scene 81_s25 with dissolve
    alex "The person who cast it is dead. She designed the spell as a personal prison. She was the only key, and that key is broken."
    scene 81_s24 with dissolve
    reham "Did you ever consider visiting the spirit-talkers in my homeland? Might as well pay them a visit since we're going there."
    scene 81_s25 with dissolve
    alex "No. And it wouldn't matter. Your spirit-talkers can't undo a spell they didn't make."
    scene 81_s27 with Dissolve(1.0)
    reham "You won't know until you try. There is a legend... that our founder was cursed with an insatiable thirst. He could drink an entire oasis dry and still feel the desert in his throat."
    stop music fadeout 1.0 
    scene 81_s28 with Dissolve(3.0)
    play music "desert.mp3" fadein 1.0 loop
    reham "He was near death when a wanderer found him. An elf-woman, they say, as old as the dunes themselves. She saw not the curse, but the man suffering beneath it."
    reham "Her ritual took three cycles of the moon. It was so powerful that when the curse finally broke, the land itself recoiled, leaving behind a vast water filled crater in the heart of the desert which became Nahraya."
    stop music fadeout 1.0 
    scene 81_s29 with Dissolve(1.0)
    play music "fire.mp3" fadein 1.0 loop
    alex "*chuckles* A charming story, Reham. But I need a fact, not a fairy tale."
    scene 81_s30 with dissolve
    reham "As I said, you won't know until you try. The sea crater is very real, and all legends have a seed of truth at their core."
    scene 81_s29 with dissolve
    alex "Fine, whatever you say. Get some rest. I'll keep watch."
    scene 81_s30 with dissolve
    stop music fadeout 1.0 

    scene 81_s31 with Fade(1.5,1.0,1.5)
    play music "night.mp3" fadein 1.0 loop
    alex "(Oh, Eli... I hope you're doing well. Your sister will come for you soon.)"
    stop music fadeout 3.0 
    scene 81_s32 with Dissolve(4.0)
    play music "nature.mp3" fadein 4.0 volume 0.5 loop
    ""
    scene 81_s33 with Dissolve(1.0)
    alex "Hmm?"
    scene 81_s34 with Dissolve(1.0)
    alex "Oh, no!"

    scene 81_s35 with Fade(0.5,0.5,0.5)
    
    alex "Reham! Wake up!"
    reham "Hnnn... Alex? What's wrong?"
    alex "A patrol is heading straight for us! We have to leave, now!"
    scene 81_s36 with dissolve
    reham "Leave? In broad daylight? They'll spot us instantly."
    scene 81_s37 with dissolve
    alex "Do you have a better idea!?"
    scene 81_s36 with dissolve
    reham "Yes. We stay. You hide. I will handle them."
    scene 81_s37 with dissolve
    alex "Are you insane!?"
    scene 81_s36 with dissolve
    reham "Trust me."
    scene 81_s38 with dissolve
    alex "Ugh... Where am I supposed to even hide!?"
    "*knock* *knock*"
    reham "Find somewhere. I'll cover Maia up."
    scene 81_s39 with dissolve
    alex "Umm...!"
    reham "Quickly!"
    alex "Sorry, [mc]. Scoot over."
    scene 81_s40 with dissolve
    "*knock* *knock* *knock*"
    reham "Coming!"
    play sound "sound_effects/door.mp3"
    scene 81_s41 with dissolve
    guard "Good day, ma'am. I'm Sergeant Daw of the first Irdan border patrol, and this is my companion, Wilkin."
    scene 81_s96 with dissolve
    reham "Irda? You're a long way from home, Sergeant."
    scene 81_s41 with dissolve
    guard "Special assignment, ma'am. Unfortunate business."
    scene 81_s96 with dissolve
    reham "Alright. Can I help you, Sirs?"
    scene 81_s41 with dissolve
    guard "As a matter of fact, you can. We're investigating the disappearance of several dangerous individuals."
    scene 81_s42 with dissolve
    guard "Have you seen this man?"

    scene 81_s43 with Dissolve(1.0)
    reham "Hmm... Can't say that I have. Nasty-looking fellow."
    scene 81_s44 with dissolve
    guard "What about these two?"

    scene 81_s43 with dissolve
    reham "Sorry, still no. Should I be worried?"
    scene 81_s44 with dissolve
    guard "Do you live here alone, ma'am?"
    scene 81_s45 with dissolve
    reham "I live with my husband. He's out hunting. Why do you ask? Is there a threat nearby?"
    scene 81_s46 with dissolve
    guard "These individuals are extremely dangerous. If you see anything, you are to report it to your nearest outpost immediately."
    scene 81_s45 with dissolve
    reham "I will be sure to do so. Is there anything else?"

    scene 81_s47 with Dissolve(1.0)
    mc "Nghnn..."
    alex "..."
    mc "Wha— A-Alex...?"
    scene 81_s48 with vpunch
    alex "{i}Shhhhhh!{/i}"
    guard "Hmm?"
    scene 81_s45 with Dissolve(1.0)
    reham "{i}I said, is there anything else,{/i} sir? My husband will be back soon from hunting lions, and he doesn't take kindly to strangers loitering."
    scene 81_s46 with dissolve
    guard "L-Lions? Sergeant, are there lions in these parts?"
    guard "I believe not..."
    scene 81_s45 with dissolve
    reham "Ah, forgive me. I meant bears. My mind is still stuck to my country."
    scene 81_s46 with dissolve
    guard "I see. Well, that will be all. Thank you for your time. Stay safe, ma'am."

    scene 81_s48 with Dissolve(1.0)
    mc "..."
    alex "..."
    reham "They're gone."
    alex "..."
    reham "Alex?"
    
    scene 81_s49 with dissolve
    alex "Ah, right..."
    scene 81_s50 with dissolve
    reham "*gasp* He's awake!"
    mc "Nghn... Wha...?"
    scene 81_s51 with dissolve
    alex "[mc]. How do you feel?"
    scene 81_s52 with dissolve
    mc "Where's Maia?"
    scene 81_s51 with dissolve
    alex "Still recovering, but she'll live."
    scene 81_s52 with dissolve
    mc "Good."
    scene 81_s53 with dissolve
    mc "*sigh* Right."
    reham "It's the left one actually."
    mc "Huh?"
    reham "Sorry. I thought I might lighten up the mood a little."

    scene 81_s54 with Fade(0.5,0.5,0.5)
    reham "Hey! You really shouldn't. You'll tear the stitches."
    scene 81_s55 with dissolve
    mc "I'm fine."
    mc "Where are we?"
    scene 81_s54 with dissolve
    alex "The safehouse I told you about. We aren't too far from the mountain we went through."
    scene 81_s55 with dissolve
    mc "How did we get here? I remember collapsing..."
    scene 81_s54 with dissolve
    alex "Someone brought you two here on a sled I think. Do you remember who it was?"
    scene 81_s55 with dissolve
    mc "I don't. Sorry."
    scene 81_s54 with dissolve
    reham "It's impressive you two managed to live through that blizzard. In your condition."
    scene 81_s56 with dissolve
    mc "I... I remember you! Reham?"
    scene 81_s57 with dissolve
    reham "*chuckles* The market. Right?"
    scene 81_s58 with dissolve
    mc "Yeah. How are you here?"
    scene 81_s57 with dissolve
    reham "It's a long story for when you have more strength. But you really should rest. I don't have enough alcohol to disinfect your wounds if you open them up."
    scene 81_s58 with dissolve
    mc "How long has it been? I remember passing out... yesterday?"
    scene 81_s57 with dissolve
    reham "Yesterday? [mc], you've been asleep for almost two weeks."
    scene 81_s56 with vpunch
    mc "Two weeks?! Ughhn!"
    scene 81_s54 with Dissolve(1.0)
    reham "I told you you should rest!"
    scene 81_s55 with dissolve
    mc "Fuck... two weeks... And she still hasn't woken up?"
    scene 81_s54 with dissolve
    reham "..."
    alex "[mc]. We need to talk."
    scene 81_s55 with dissolve
    mc "About what?"
    scene 81_s54 with dissolve
    reham "Is this really the time? He just woke up."
    alex "I can't afford to wait any longer. M-My brother..."
    stop music fadeout 1.0
    scene 81_s61 with Fade(1.0,1.5,1.0)
    play music "sex01.mp3" fadein 1.0 loop
    mc "What is it you wanna talk about? What's this about your brother?"
    
    if mc_tried_help_alex:
        $ mc_save_queen = True

    if mc_save_queen:
        alex "There... there was an attempt at Queen Hannah's life."
        scene 81_s61 with vpunch
        mc "What? How? When?!"
        alex "On the road back from Eurina... She was supposed to die then and there."
        mc "Is... Is it Avery? I knew she was power-hungry, but... trying to kill her own sister?"
        scene 81_s62 with dissolve
        alex "You're right about her. But she didn't act alone. My... father... Reiner... he orchestrated it all. They're in this together."
        scene 81_s63 with dissolve
        mc "Your father? What does he have to gain from the death of Irda's queen? It makes no sense."
        scene 81_s62 with dissolve
        alex "He didn't just orchestrate it, [mc]. He tasked {i}me{/i} with it."
        scene 81_s63 with dissolve
        mc "You... what?"
        scene 81_s62 with dissolve
        alex "I had a dagger to her heart. My father's orders. My brother's life for her death."
        alex "I couldn't do it. She looked at me, not at the blade, at {i}me{/i} and she saw the chain my father had me in."
        scene 81_s63 with dissolve
        mc "Alex..."
        scene 81_s62 with dissolve
        alex "She used her own magic to fake her death. Right now, the world believes she's at the bottom of the sea. But she's hidden. Waiting."
        scene 81_s63 with dissolve
        mc "Waiting for what?"
        scene 81_s62 with dissolve
        alex "For us. For you. She told me to find you."
        alex "She said Avery would try to silence you too since you were a witness to the massacre. You're in as much danger as I am."
        scene 81_s63 with dissolve
        mc "God..."
        scene 81_s64 with dissolve
        alex "I lied to you from the moment we met. I am, by every law, a traitor."
        alex "So go ahead. Look at me. See the traitor. The fool who thought she could save her brother by becoming a monster."
        alex "I dragged you and Maia into this hell. I deserve every bit of your hatred. So hit me. Yell at me. Do whatever you want. I deserve it."
        scene 81_s65 with dissolve
        mc "..."
    
    else:
        alex "The Queen... Queen Hannah... is dead."
        scene 81_s61 with vpunch
        mc "What? How? When?!"
        alex "On the road back from Eurina. The official story will be that her ship sank in the storm."
        mc "Is... Is it Avery? I knew she was power-hungry, but... killing her own sister?"
        scene 81_s62 with dissolve
        alex "You're right about her. But she didn't act alone. My... father... Reiner... he orchestrated it all. They're in this together."
        scene 81_s63 with dissolve
        mc "Your father? What does he have to gain from the death of Irda's queen? It makes no sense."
        scene 81_s62 with dissolve
        alex "He didn't just orchestrate it, [mc]. He tasked {i}me{/i} with it."
        scene 81_s63 with dissolve
        mc "You... what?"
        scene 81_s62 with dissolve
        alex "I had no choice, alright!? He had a knife to my brother's throat!"
        alex "He said he would carve him up piece by piece if I didn't play my part in that damned conference and then on the road home!"
        scene 81_s63 with dissolve
        mc "Alex..."
        scene 81_s62 with dissolve
        alex "He made me lie to everyone! He made me point the finger at an innocent woman, and then... when she was at her most vulnerable... I plunged my dagger into her stomach."
        alex "She knew. In her last moments, she knew it was Avery. And she told me to run. She showed me more mercy than my own blood."
        scene 81_s63 with dissolve
        mc "God..."
        scene 81_s62 with dissolve
        alex "And the punchline? The final, beautiful twist? The assassins he sent to clean up the evidence... their orders were to kill me too."
        alex "I was never supposed to leave that carriage alive. I'm just another loose end."
        scene 81_s64 with dissolve
        alex "So go ahead. Look at me. See the traitor. The Queen killer. The fool who thought she could save her brother by becoming a monster."
        alex "I dragged you and Maia into this hell. I deserve every bit of your hatred. So hit me. Yell at me. Do whatever you want. I deserve it."
        scene 81_s65 with dissolve
        mc "..."
    call screen scene81_choice01 with dissolve

label scene81_choice01_op1:
    $ mc_hug_alex = True
    play sound "sound_effects/clothing_rustle.mp3"
    scene 81_s66 with vpunch
    alex "Huh?"
    mc "I'm sorry you had to go through this."
    scene 81_s67 with dissolve
    alex "Get away from me... I don't deserve this."
    scene 81_s68 with dissolve
    mc "You do. You were used. You acted out of love for your brother, as fucked as it was. I can't put the full blame on you."
    scene 81_s67 with dissolve
    if mc_save_queen:
        alex "*hic* I wish they killed me back there. Then I wouldn't have to live with this... or wonder what he's doing to Eli."
    else:
        alex "*hic* I wish I died back there. Then I wouldn't have to live with this... or wonder what he's doing to Eli."
    scene 81_s68 with dissolve
    mc "Don't say that. You're alive. That means you can still make it right."
    alex "..."
    alex "*sniff* Mhm."
    mc "Tell me. From the very beginning."
    jump scene81_2

label scene81_choice01_op2:
    $ mc_slap_alex = True
    play sound "sound_effects/slap03.mp3"
    scene 81_s69 with vpunch
    alex "Nghn!"
    scene 81_s70 with dissolve
    mc "Get yourself together!"
    alex "*hic* I..."
    mc "Tell me what happened. From the start."
    alex "*sniff* I'm sorry..."
    mc "Alex. Now's not the time to fall apart. You put us in this mess. The least you can do is make me understand the shape of it."
    alex "I'm so sorry..."
    jump scene81_2

label scene81_2:
    scene 81_s71 with Fade(1.0,1.0,2.0)
    alex "I never told you how I got my curse."
    mc "No. You didn't."
    alex "I was trained as an assassin ever since I could barely hold a sword."
    alex "My father... he sent me to Illus. My latest mission was to assassinate the Queen of Pleasure. This was months before you and I ever met."
    alex "It was a quiet night, she didn't have many visitros. I had the perfect oppuritunty."
    alex "I was to be the spark. Her death on Irda's soil, was meant to shatter the fragile truce with Nahraya. I would leave subtle evidence to lead the murder to Irdan soil."
    alex "I spent weeks learning her routines, her habits. When she took her walks in the garden. When she went to bed."
    alex "The night I moved, I disguised myself as a wealthy patron. The entry fee alone cost a small fortune. I was led to her private chamber."
    alex "But when she entered, she didn't look surprised. She just looked... amused."
    alex "She offered me a deal. Abandon my mission, and work for her instead. She promised freedom from my father... but I was too loyal then. A fool. I drew my blade and rushed her."
    alex "She didn't even try to dodge. She just... smiled. And then she spoke a single word. The curse took hold instantly."
    scene 81_s72 with dissolve
    alex "I barely escaped with my life, the heat of her magic still burning me from the inside out."
    scene 81_s73 with dissolve
    mc "So your father's mission was a catastrophic failure."
    scene 81_s72 with dissolve
    alex "A failure that left me permanently branded. After that, I... broke. I couldn't stay in Eurina, not like that. The curse was too much. So I ran."
    alex "I thought if I faced her again, if I killed her, the curse might break. Or maybe I just wanted revenge."
    alex "And that's when I met you."
    scene 81_s73 with dissolve
    mc "*sigh* What have I gotten myself into..."
    scene 81_s72 with dissolve
    alex "I'm sorry, [mc]. Truly. You never should have been caught in this mess."
    if mc_save_queen:
        scene 81_s73 with dissolve
        mc "Can't the Queen just return and depose Avery herself?"
        scene 81_s74 with dissolve
        alex "She fears her sudden return would spark a civil war. The kingdom is already divided."
        alex "And Avery has had time to turn or replace everyone she once trusted... everyone she once relied on."
        alex "But you're involved now. Which means... I need your help."
    else:
        scene 81_s74 with dissolve
        alex "But you're in this now. Which means... I need your help."
    call screen scene81_choice02 with dissolve

label scene81_choice02_op1:
    scene 81_s75 with dissolve
    mc "Alex. How am I supposed to help anyone?"
    mc "My hand is gone. I can't even fight properly anymore. What use am I with one arm?"
    jump scene81_3

label scene81_choice02_op2:
    $ mc_angry_alex = True
    scene 81_s75 with dissolve
    mc "How can you ask for my trust? You lied to me. You lied to the Queen. You've lied to everyone."
    scene 81_s76 with dissolve
    alex "I know. And I will spend the rest of my life earning that trust back. But right now, I am not lying. I swear on my brother's soul, I am telling you the one truth that matters."
    scene 81_s75 with dissolve
    mc "*sigh* It doesn't change anything. I can't even fight properly anymore. What use am I with one arm?"
    jump scene81_3

label scene81_3:
    scene 81_s76 with dissolve
    alex "You're thinking like a soldier who lost his weapon. Stop."
    alex "I don't need your arm. I need your voice."
    scene 81_s84 with dissolve
    mc "My voice?"
    scene 81_s85 with dissolve
    alex "Yes. I need you to testify. To look at Nueleth. Tell her about Avery's conspiracy, about my father's treachery. Tell her the truth."
    scene 81_s84 with dissolve
    mc "Nueleth?"
    scene 81_s85 with dissolve
    alex "She holds the threads of every kingdom on Illus. No one declares war without her counsel. But she won't hear fugitives off the street."
    alex "That's why we go south first, to Nahraya. King Hod despises lies above all else. And... he once loved the Queen. Deeply. If anyone will force a hearing, it's him."
    scene 81_s84 with dissolve
    mc "Let me get this straight..."
    mc "We walk into a foreign king's court, convince him our story is true, and he arranges a meeting with the most powerful woman on the continent... and then what? We tell our tale and everything magically fixes itself?"
    scene 81_s77 with dissolve
    alex "I don't know! But it is the only path that doesn't end with us dead in a ditch! Do you have a better plan? To run? To hide?"
    scene 81_s79 with dissolve
    alex "I have a little brother out there, [mc]. My father's probably keeping him caged like bait to lure me back. I {i}have{/i} to try."
    if mc_save_queen:
        alex "The Queen gave me this mission. Her last act before disappearing was to chart this course."
        alex "This isn't just my atonement, it's her strategy. We're executing the plan to save her kingdom."
    else:
        alex "Her last breath was wasted on telling me to run."
        alex "Going to Nahraya... it's not a plan. It's the only thread of honor I have left to cling to."
    scene 81_s77 with dissolve
    alex "And you. Look at Maia. Do you think you can just live a quiet life now? Avery doesn't just want you dead; she needs you erased."
    alex "To solidify her story, to legitimize her rule, our existence must be painted as a monstrous lie."
    alex "She has connections in every city. The world will become your enemy. There will be no safe haven."
    alex "And when they catch you, they will kill you. But first... they have to catch you."
    alex "But we will not run. We will not hide. We will march straight into the lion's den and speak a truth so powerful it will shatter their throne."
    scene 81_s78 with dissolve
    mc "Can't you just... go back to Eurina yourself? Expose the truth from inside?"
    scene 81_s77 with dissolve
    alex "I wish it were that simple. Yes, I'm niece to the king, but outside the court, almost no one knows my face or name."
    scene 81_s78 with dissolve
    mc "What do you mean?"
    scene 81_s77 with dissolve
    alex "I was raised as a shadow, [mc]. An assassin. My reputation, what little there is, is whispers and fear, not trust. The people never saw me, I made sure of that."
    alex "If I walked into any Eurinian city now, I'd be arrested or knifed before I opened my mouth. He'll have killers waiting on every road and dock."
    alex "And my father's most likely already told something about how I just ran off somewhere since I have a history of doing so."
    scene 81_s78 with dissolve
    mc "*scoff* Your remind me of myself. I doubt many people knew me outside the castle."
    scene 81_s80 with dissolve
    alex "So no easy shortcuts. We don't run. We don't hide."
    alex "They took your arm, [mc]. Don't let them take your future, too."
    alex "What do you say?"
    scene 81_s81 with dissolve
    call screen scene81_choice03 with dissolve

label scene81_choice03_op1:
    $ mc_agree_alex = True
    $ mc_angry_alex = False
    play sound "sound_effects/body/clap.mp3"
    pause(0.2)
    scene 81_s82 with vpunch
    mc "I'm with you."
    mc "Let's do it. Let's break this world"
    scene 81_s83 with dissolve
    alex "Thank you."
    alex "We'll make them regret the day they crossed us."
    jump scene82

label scene81_choice03_op2:
    $ mc_angry_alex = True
    scene 81_s84 with dissolve
    mc "I'll go with you. I'll testify. But I'm doing it because it's the only path I have left, not because I trust you. That, you still have to earn."
    mc "One lie. One half-truth. And we're done. Understood?"
    scene 81_s85 with dissolve
    alex "Understood. I will earn it. I swear."
    jump scene82

label scene81_choice03_op3:
    $ mc_agree_alex = True
    $ mc_angry_alex = False
    $ mc_try_kiss_alex = True
    scene 81_s86 with dissolve
    perception "You lean in, closing the distance between you. For a split second, her eyes widen—not in anger, but in genuine surprise."
    scene 81_s87 with dissolve
    empathy "She jerks her head back, your lips barely brushing her cheek. Her face flushes a deep red, and she looks everywhere but at you."
    scene 81_s88 with dissolve
    alex "Whoa—! I-I, uh..."
    scene 81_s89 with dissolve
    mc "Shit. Sorry. I—I probaly shouldn't have done that."
    scene 81_s88 with dissolve
    alex "...It's okay. I just... wasn't expecting..."
    scene 81_s97 with dissolve
    alex "..."
    mc "..."
    scene 81_s88 with dissolve
    alex "I'm... not really... good at that. At all."
    scene 81_s89 with dissolve
    mc "Yeah, I'm getting that."
    scene 81_s88 with dissolve
    alex "A-Anyway... What do you say?"
    scene 81_s89 with dissolve
    mc "I'm with you. I'm with you for Maia. For the Queen. For everyone they've trampled."
    scene 81_s88 with dissolve
    alex "Good. That's all I needed to hear."
    scene 81_s97 with dissolve
    jump scene82

label scene82:
    stop music fadeout 1.0 
    scene 81_s90 with Fade(1.5,0.5,1.0)
    mc "I need to check on Maia."
    alex "Of course. I'll keep watch."
    scene 82_s1 with Fade(1.0,1.0,1.0)
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    mc "How is she?"
    scene 82_s2 with dissolve
    reham "Her color is better. The fever broke last night. She's no longer dancing with death, just resting deeply."
    mc "Thank you for this, Reham."
    reham "Of course."
    reham "You said her name was Maia, right?"
    mc "Right."
    scene 82_s3 with dissolve
    mc "..."
    reham "[mc]?"
    scene 82_s4 with dissolve
    mc "Sorry! Were you saying something?"
    scene 82_s5 with dissolve
    reham "*chuckles* Is she your lover?"
    scene 82_s4 with dissolve
    
    if not mc_maia_left:
        mc "Yes."
        mc "Why do you ask?"
        scene 82_s5 with dissolve
        reham "Alex mentioned the Princess of Irda is your wife now. I was wondering... how Maia took that news."
        scene 82_s4 with dissolve
        mc "Being married to Rebecca wasn't my choice. The Queen decided it on a whim, right before she sailed for Eurina."
        mc "She entrusted Rebecca to me because she thought I could protect her."
        mc "Though I suspect the real reason was to keep me close. So they could study this... {i}thing{/i} inside me."
        scene 82_s5 with dissolve
        reham "Thing?"
        scene 82_s4 with dissolve
        mc "An elven mage, Ava, examined my mana once. Called it an 'enigma.' No one knows what it is yet, only that it's there."
        scene 82_s5 with dissolve
        reham "Hmm. If it promised to make a kingdom stronger, *chuckles* I'd chain the bearer close too."
        scene 82_s4 with dissolve
        mc "But you asked about Maia for a reason."
        scene 82_s5 with dissolve
        reham "It's not about Maia in particular. I just think most women would be clawing at the walls by now. Jealousy, tears, demands... if their man married a princess."
        reham "But I believe a mere maid like her has no say in her husband's affairs, especially when he's a man of rank. Like you. Or was, I suppose."
        scene 82_s4 with dissolve
        mc "*chuckles* That's fair. But Maia wasn't really against it. The princess is her friend afterall. And besides..."
        if not mc_maia_monogamous_question:
            call screen scene82_choice_maia with dissolve
        else:
            if mc_maia_monogamous:
                mc "I told her she would always be the only one for me."
                scene 82_s5 with dissolve
                reham "And do you mean it?"
                scene 82_s4 with dissolve
                mc "I did when I said it."
                scene 82_s5 with dissolve
                reham "Girls like her don't bend easy on promises of the heart. Break one, and the hurt lingers longer than any wound."
            else:
                mc "I told her upfront, I won't be with only one woman. She accepted it."
                scene 82_s5 with dissolve
                reham "I see. It's for the best that you were honest at least."
            jump scene82_continue
    else:
        mc "No. Not anymore. But I still care for her. More than I should, maybe."
        mc "Why do you ask?"
        scene 82_s5 with dissolve
        reham "Alex mentioned the Princess of Irda is your wife now. I was wondering... how Maia took that news. But if she's no longer your lover... forget I asked."
        scene 82_s4 with dissolve
        mc "Being married to Rebecca wasn't my choice. The Queen decided it on a whim, right before she sailed for Eurina."
        mc "She entrusted Rebecca to me because she thought I could protect her."
        mc "Though I suspect the real reason was to keep me close. So they could study this... {i}thing{/i} inside me."
        scene 82_s5 with dissolve
        reham "Thing?"
        scene 82_s4 with dissolve
        mc "An elven mage, Ava, examined my mana once. Called it an 'enigma.' No one knows what it is yet, only that it's there."
        scene 82_s5 with dissolve
        reham "Hmm. If it promised to make a kingdom stronger, *chuckles* I'd chain the bearer close too."
        scene 82_s4 with dissolve
        mc "But you asked about Maia for a reason."
        scene 82_s5 with dissolve
        reham "It's not about Maia in particular. I just think most women would be clawing at the walls by now. Jealousy, tears, demands... if their man married a princess."
        reham "But I believe a mere maid like her has no say in her husband's affairs, especially when he's a man of rank. Like you. Or was, I suppose."
        scene 82_s4 with dissolve
        mc "*chuckles* I guess that's fair. But I doubt Maia would've been against it. She's too kind and accepting. And besides... The princess is her friend."
        jump scene82_continue

label scene82_choice_maia_op1:
    $ mc_maia_monogamous = False
    mc "I told her upfront, I won't be with only one woman. She accepted it."
    scene 82_s5 with dissolve
    reham "I see. It's for the best that you were honest at least."
    jump scene82_continue
    
label scene82_choice_maia_op2:
    $ mc_maia_monogamous_sure = True
    mc "I told her she would always be the only one for me."
    scene 82_s5 with dissolve
    reham "Then you'd best mean it. Girls like her don't bend easy on promises of the heart. Break one, and the hurt lingers longer than any wound."
    jump scene82_continue

label scene82_choice_maia_op3:
    $ mc_maia_monogamous_unsure = True
    $ mc_maia_monogamous = True
    mc "Actually... we never talked about it."
    scene 82_s5 with dissolve
    reham "Then you've left the door wide open."
    reham "And silence isn't neutrality. Don't be afraid of telling her what you really want, talk about it soon. She might surprise you."
    scene 82_s4 with dissolve
    mc "*sigh* You're right, I probably should have said something."
    jump scene82_continue

label scene82_continue:
    scene 82_s5 with dissolve
    reham "Regardless, I'm sure she's lucky to have a man who would storm the underworld for her."
    scene 82_s4 with dissolve
    mc "I'm not sure 'lucky' is the word."
    scene 82_s5 with dissolve
    reham "It is. Trust me."
    reham "What about Alex, did she tell you the truth?"
    scene 82_s6 with Dissolve(1.5)
    mc "She did. About her father, Avery, the Queen... all of it."
    reham "And what did you decide?"
    mc "I'm going to testify. There's no other path forward except a lifetime of running."
    reham "You made the right choice. A cornered animal only runs. A man with a purpose... he marches."
    scene 82_s4 with dissolve
    mc "Speaking of paths... you never did tell me how you ended up here, Reham."
    scene 82_s7 with Dissolve(1.0)
    reham "*chuckles* Well... As demotivating as it sounds, no one in Irda's market would hire a servant with my... complexion."
    reham "They preferred their maids to look like the snow of the Veilnirn mountains."
    reham "My mentor decided we'd have better luck in Eurina. But before we even reached the city, bandits ambushed our caravan."
    reham "I was taken, to be sold on the block. Caged in the hold of a ship with a few others heading back to Illus. That's where I met Alex."
    reham "She'd snuck aboard, she... made the slavers regret their career choices. Saved us all."
    scene 82_s8 with dissolve
    mc "That's... horrible, Reham. I'm sorry. Though I'm not sure being holed up in a shed with a pair of fugitives is much better."
    scene 82_s7 with dissolve
    reham "Freedom is freedom. And company is company. I'll take this over chains any day."
    scene 82_s8 with dissolve
    reham "..."

    if maia_pregnant:
        scene 82_s2 with Dissolve(1.0)
        reham "She's pregnant, isn't she?"
        mc "I... I believe so. W-Why? Did something happen!? Is the baby—?"
        reham "No, no. Breathe. It's a miracle, but the little spark is still safe. The child is stubborn, like its parents."
        mc "*sigh* Thank God."
        mc "How far along do you think her pregnancy is?"
        reham "Not even two months. It'll be a while before you see your child. But maybe that's for the best."

    scene 82_s4 with dissolve
    mc "Say, Reham..."
    reham "Hmm?"
    mc "If I'd had the coin, if I'd bought your contract back then, would you really have served me?"
    scene 82_s5 with dissolve
    reham "What brought this on all of a sudden?"
    scene 82_s4 with dissolve
    mc "Just answer me."
    scene 82_s5 with dissolve
    reham "*chuckles* Of course I would have. Fair coin for honest work beats most fates by a mile. I'd have served well."
    scene 82_s4 with dissolve
    mc "Do you have a man right now?"
    scene 82_s5 with dissolve
    reham "Why ask? It's not like I can stroll back to working in that field now."
    scene 82_s4 with dissolve
    call screen scene82_choice01 with dissolve

label scene82_choice01_op2:
    mc "It's nothing. Just something that crossed my mind."
    scene 82_s5 with dissolve
    reham "I see."
    reham "Why don't you get some rest? I noticed that you were wincing in pain since you woke up."
    reham "I will wake you up if something happens."
    scene 82_s4 with dissolve
    mc "Yeah, alright. You have a point. My arm's killing me."
    jump scene82_4

label scene82_choice01_op1:
    stop music fadeout 1.0
    mc "I'm asking because I want you."
    play music "side_event2.mp3" fadein 1.0 loop
    scene 82_s90 with dissolve
    perception "Her breath catches, just a fraction. She straightens, but doesn't retreat. A faint flush rises on her warm skin as she struggles to hold your gaze."
    scene 82_s89 with dissolve
    reham "Want me... how, exactly?"
    scene 82_s90 with dissolve
    mc "As mine. My servant. Ever since I saw you standing there in that market, calm and beautiful, I haven't been able to get the thought out of my head."
    scene 82_s89 with dissolve
    if not mc_maia_left:
        reham "[mc]... I think you're only saying this because Maia isn't around to help you."
        scene 82_s90 with dissolve
        mc "I know what I said."
        reham "..."
    else:
        reham "[mc]... I think you're only saying this because you're feeling lonely and distraught after what happened."
        scene 82_s90 with dissolve
        mc "I know what I said."
        reham "..."
    scene 82_s90 with dissolve
    mc "So? Is that a yes?"
    scene 82_s89 with dissolve
    reham "And if I say yes? What then, [mc]?"
    scene 82_s90 with dissolve
    mc "Then you're mine. I protect what's mine. I keep you safe... and close."
    scene 82_s89 with dissolve
    reham "Hm. Back at the market..."
    if mc_inspected_reham:
        reham "You inspected me so thoroughly. You seemed to want... more. And I'm not sure if I would want to serve a master who only looks at my body."
        scene 82_s90 with dissolve  
        mc "I was offered a chance to look at a beautiful woman, how could you expect me to refuse?"
        scene 82_s89 with dissolve
        reham "Still..."
    elif mc_talked_reham:
        reham "You spoke to me. You saw me in this skimpy suit, yet you asked for my name, not just my price. I thought you were different. This... this feels like a more honest transaction than hard labor for a master who doesn't see my worth."
        scene 82_s90 with dissolve  
        mc "*laughs* Glad you see it that way."
    else:
        reham "You walked away. You thought I was being exploited, and your conscience wouldn't allow it. You have a kind heart, [mc]. A master with a kind heart is a rare treasure."
        scene 82_s90 with dissolve  
        mc "*laughs* A kind heart? That might be a stretch."
    scene 82_s92 with Dissolve(2.0)
    reham "Alright. I get it, you're feeling depressed and want someone to look after you. But, before we ink this little contract of ours, what does 'servant' mean to you, [mc]?"
    scene 82_s91 with dissolve
    call screen scene82_choice02 with dissolve
    
label scene82_choice02_op1:
    mc "Just taking basic care of me. Nothing more."
    scene 82_s92 with dissolve
    reham "So, none of the sultry stuff that my mentor suggested?"
    scene 82_s91 with dissolve
    mc "Yes. None of that."
    scene 82_s92 with dissolve
    reham "That makes things easier. But one last thing before we move on. My services aren't free."
    scene 82_s91 with dissolve
    mc "You want me to pay you? I don't think coin means much when we're hiding in a shed."
    scene 82_s92 with dissolve
    reham "Perhaps not today. But I believe we'll survive this and return to a normal life. And when we do, coin will matter again."
    scene 82_s91 with dissolve
    mc "How much are we talking, anyway?"
    scene 82_s92 with dissolve
    if mc_not_interested_slaver:
        reham "We never settled on a price. You walked away, remember?"
        scene 82_s91 with dissolve
        mc "Ah, right..."
        scene 82_s92 with dissolve
        reham "My original asking was five hundred coins."
        scene 82_s91 with vpunch
        mc "Five hundred!? That's five gold, right?"
        scene 82_s92 with dissolve
        reham "*chuckles* Exactly. But no one was interested, so my mentor kept dropping it."
        scene 82_s91 with dissolve
        mc "Oh, come on! You're still quoting the original price?!"
        scene 82_s92 with dissolve
        reham "A girl can dream~ But fine, how about three hundred. Fair?"
        scene 82_s91 with dissolve
        mc "Hmm... Let me see."
        perception "You rummage through your pockets and find [mc_coin] coins."
    else:
        reham "My mentor lowered it for you. If I recall, it was [reham_price] coins."
        reham "Originally? I was five hundred."
        scene 82_s91 with vpunch
        mc "Five hundred!? That's five gold, right?"
        scene 82_s92 with dissolve
        reham "*laughs* Exactly. But no one was interested, so my mentor kept dropping it."
        scene 82_s91 with dissolve
        mc "Hmm... Let me see."
        perception "You rummage through your pockets and find [mc_coin] coins."

    if mc_coin >= reham_price:
        mc "Very well. Consider yourself hired."
        $ mc_harem_reham = True
        $ mc_coin -= reham_price
        mc "Here's your payment."
        scene 82_s102 with Dissolve(1.0)
        perception "You hand her a pouch filled with [reham_price] coins. Her fingers brush yours as she takes it."
        scene 82_s92 with Dissolve(1.0)
        reham "I will serve your faithfully, master."
        scene 82_s91 with dissolve
        mc "Master..."
        reham "Hmm?"
        mc "Say it again..."
        scene 82_s92 with dissolve
        reham "Master~!"
        reham "Before you start ordering me around, master. I have to request that you take some rest."
        reham "You look like death warmed over, and not in a good way. You need proper warmth, deep sleep."
        scene 82_s91 with dissolve
        mc "Yeah, alright. You have a point. My arm's killing me."
        scene 82_s92 with dissolve
        reham "Have a good rest, master!"
        scene 82_s91 with dissolve

    elif mc_coin < reham_price:
        $ mc_harem_reham = False
        $ mc_no_coin_standard_reham = True
        mc "Oh..."
        reham "Hmm?"
        mc "Would it be fine if I pay you later?"
        scene 82_s100 with dissolve
        reham "I'm sorry, [mc]. Coin is coin. Without it up front, I can't bind myself as your servant."
        scene 82_s101 with dissolve
        mc "Really...?"
        scene 82_s100 with dissolve
        reham "But listen, I'll still help. I'll keep this shed running, tend to Maia, watch over Alex, patch you up whenever I can. I'll care for all of us until this situation is over."
        scene 82_s101 with dissolve
        mc "So... basically what you've already been doing?"
        scene 82_s100 with dissolve
        reham "*chuckles* I suppose so. Just without the title."
        scene 82_s101 with dissolve
        mc "*sigh* I get it."
        scene 82_s100 with dissolve
        reham "Please don't be sad. It's not a refusal of you, it's just the terms. I'm still here. Still on your side."
        scene 82_s101 with dissolve
        mc "Thanks anyway, Reham."
        scene 82_s100 with dissolve
        reham "Of course. Always."
        reham "Why don't you go to bed now? You need proper warmth, deep sleep."
        scene 82_s101 with dissolve
        mc "Yeah, alright. You have a point."
        scene 82_s100 with dissolve
        reham "Have a good rest."
        scene 82_s101 with dissolve

    jump scene82_4


default mc_coin_after_reham = 0
default reham_new_price = 0

label scene82_choice02_op2:
    mc "You'll do whatever I ask, whenever I ask."
    perception "Her breath catches audibly. Pupils darken as she searches your face, testing for bluff and finding none."
    scene 82_s92 with dissolve
    if mc_maia_monogamous_sure:
        reham "You just told me Maia is the only one for you. So which is it?"
        scene 82_s91 with dissolve
        mc "She doesn't need to know."
        scene 82_s92 with dissolve
        reham "I'd rather not be the reason that girl's heart breaks, [mc]."
        reham "Sorry. That's a hard no from me."
        scene 82_s91 with dissolve
        mc "...You're right. I don't know why I said that. Forget it."
        scene 82_s92 with dissolve
        reham "Why don't you get some rest? You're clearly not thinking straight from the pain."
        reham "I will wake you up if something happens."
        scene 82_s91 with dissolve
        mc "Yeah... alright. My arm's killing me anyway."
        jump scene82_4

    else:
        if mc_maia_monogamous:
            if mc_maia_monogamous_unsure:
                reham "[mc]... you said Maia doesn't even know where she stands."
                scene 82_s91 with dissolve
                mc "I'll tell her, I promise. Soon."
                scene 82_s92 with dissolve
                reham "*sigh* You'd better. Quickly. Lies by omission cut just as deep."
                reham "And even then..."
            else:
                reham "[mc]... what will Maia think if she knew about this?"
                reham "Shouldn't you have told her that you were interested of having multiple partners from the start?"
                scene 82_s91 with dissolve
                mc "I'll tell her, I promise. Soon."
                scene 82_s92 with dissolve
                reham "*sigh* You'd better. Quickly. Lies by omission cut just as deep."
                reham "And even then..."

        reham "...That's a heavy demand."
        scene 82_s91 with dissolve
        mc "Your mentor {i}did{/i} mention 'fulfilling every need.'"
        scene 82_s92 with dissolve
        reham "Ah, that old hook. Mostly sales talk to reel in the lonely lords."
        scene 82_s91 with dissolve
        mc "So it's not real?"
        scene 82_s92 with dissolve
        reham "Not {i}mostly.{/i} They can have access to my body whenever they wish but only if it was written in the contract."
        reham "It significantly increases the price of us servants, so its mainly reserved to those who are wealthy."
        scene 82_s91 with dissolve
        mc "Did you ever have such a master before?"
        scene 82_s92 with dissolve
        reham "I have had masters. None ever were wealthy enough to earn that particular... dedication."
        scene 82_s91 with dissolve
        mc "You want me to pay you now? I don't think coin means much when we're hiding in a shed."
        scene 82_s92 with dissolve
        reham "Perhaps not today. But I believe we'll survive this and return to a normal life. And when we do, coin will matter again."
        scene 82_s91 with dissolve
        mc "How much are we talking, anyway?"
        scene 82_s92 with dissolve
        if mc_not_interested_slaver:
            reham "We never settled on a price. You walked away, remember?"
            scene 82_s91 with dissolve
            mc "Ah, right..."
            scene 82_s92 with dissolve
            reham "My original asking was five hundred coins."
            scene 82_s91 with vpunch
            mc "Five hundred!? That's five gold, right?"
            scene 82_s92 with dissolve
            reham "*chuckles* Exactly. But no one was interested, so my mentor kept dropping it."
            scene 82_s91 with dissolve
            mc "Oh, come on! You're still quoting the original price?!"
            scene 82_s92 with dissolve
            reham "A girl can dream~ But fine, how about three hundred. Fair?"
            scene 82_s91 with dissolve
            mc "Hmm... Let me see."
            perception "You rummage through your pockets and find [mc_coin] coins."

        else:
            reham "My mentor lowered it for you. If I recall, it was [reham_price] coins."
            reham "Originally? I was five hundred."
            scene 82_s91 with vpunch
            mc "Five hundred!? That's five gold, right?"
            scene 82_s92 with dissolve
            reham "*laughs* Exactly. But no one was interested, so my mentor kept dropping it."
            scene 82_s91 with dissolve
            mc "Hmm... Let me see."
            perception "You rummage through your pockets and find [mc_coin] coins."
            
        if mc_coin >= reham_price:
            $ reham_price += 100
            $ reham_new_price = reham_price
            mc "I have enough... but that's just the basic service, right?"
            scene 82_s92 with dissolve
            reham "Correct. If you want my full dedication then that adds another hundred."
            scene 82_s91 with dissolve
            if mc_coin >= reham_new_price:
                mc "Alright. Even with the upcharge, I've got it covered."
                scene 82_s100 with dissolve
                reham "My... a wealthy man after all. I suppose it makes sense for someone who worked directly under a queen."
                reham "So, do we have a deal?"
                scene 82_s101 with dissolve
                mc "..."
                if not karma_updated:
                    $ karma_updated = True
                    if mc_karma >= 100:
                        $ mc_karma = 10
                    elif mc_karma >= 90:
                        $ mc_karma = 9
                    elif mc_karma >= 80:
                        $ mc_karma = 8
                    elif mc_karma >= 70:
                        $ mc_karma = 7
                    elif mc_karma >= 60:
                        $ mc_karma = 6
                    elif mc_karma >= 50:
                        $ mc_karma = 5
                    elif mc_karma >= 40:
                        $ mc_karma = 4
                    elif mc_karma >= 30:
                        $ mc_karma = 3
                    elif mc_karma >= 20:
                        $ mc_karma = 2
                    elif mc_karma >= 10:
                        $ mc_karma = 1
                    else:
                        $ mc_karma = 1
                if mc_karma > 10:
                    $ mc_karma = 10
                if mc_karma < 1:
                    $ mc_karma = 1
                call screen scene81_choice00 with dissolve

            else:
                mc "Shit. The extra hundred puts me short."
                scene 82_s92 with dissolve
                reham "You can still my basic service."
                scene 82_s91 with dissolve
                mc "*sigh* That's wasn't the point, Reham."
                scene 82_s92 with dissolve
                reham "Well I'm sorry, [mc]. But coin is coin. Without it up front, I can't let you have me like that."
                reham "Standard terms still stand, if you want them."
                scene 82_s91 with dissolve
                if not karma_updated:
                    $ karma_updated = True
                    if mc_karma >= 100:
                        $ mc_karma = 10
                    elif mc_karma >= 90:
                        $ mc_karma = 9
                    elif mc_karma >= 80:
                        $ mc_karma = 8
                    elif mc_karma >= 70:
                        $ mc_karma = 7
                    elif mc_karma >= 60:
                        $ mc_karma = 6
                    elif mc_karma >= 50:
                        $ mc_karma = 5
                    elif mc_karma >= 40:
                        $ mc_karma = 4
                    elif mc_karma >= 30:
                        $ mc_karma = 3
                    elif mc_karma >= 20:
                        $ mc_karma = 2
                    elif mc_karma >= 10:
                        $ mc_karma = 1
                    else:
                        $ mc_karma = 1
                if mc_karma > 10:
                    $ mc_karma = 10
                if mc_karma < 1:
                    $ mc_karma = 1
                call screen scene81_choice000 with dissolve

                mc "Very well. Basic service it is."
                $ mc_harem_reham = True
                $ mc_coin -= reham_price
                mc "Here's your payment."
                scene 82_s102 with Dissolve(1.0)
                perception "You hand her a pouch filled with [reham_price] coins. Her fingers brush yours as she takes it."
                scene 82_s100 with Dissolve(1.0)
                reham "I will serve your faithfully, master."
                scene 82_s101 with dissolve
                mc "Master..."
                reham "Hmm?"
                mc "Say it again..."
                scene 82_s100 with dissolve
                reham "Master~!"
                reham "Before you start ordering me around, master. I have to request that you take some rest."
                reham "You look like death warmed over, and not in a good way. You need proper warmth, deep sleep."
                scene 82_s101 with dissolve
                mc "Yeah, alright. You have a point. My arm's killing me."
                scene 82_s100 with dissolve
                reham "Have a good rest, master!"
                scene 82_s101 with dissolve
                jump scene82_4
        else:
            $ mc_no_coin_dom_reham = True
            $ mc_harem_reham = False
            mc "Dammit. I don't have enough."
            scene 82_s100 with dissolve
            reham "*chuckles* You were bargaining for full service without enough for the basic?"
            scene 82_s101 with dissolve
            mc "Yeah, yeah. Rub it in."
            scene 82_s100 with dissolve
            reham "I'm not mocking you. I'm poor as dirt myself so that makes two of us."
            scene 82_s101 with dissolve
            mc "*sigh* So... nothing?"
            scene 82_s100 with dissolve
            reham "Not as your servant, no. Not without the coin to make it real."
            scene 82_s101 with dissolve
            mc "Really...?"
            scene 82_s100 with dissolve
            reham "Listen, I'll still help. I'll keep this shed running, tend to Maia, watch over Alex, patch you up whenever I can. I'll care for all of us until this situation is over."
            scene 82_s101 with dissolve
            mc "So... basically what you've already been doing?"
            scene 82_s100 with dissolve
            reham "*chuckles* I suppose so. Just without the title."
            scene 82_s101 with dissolve
            mc "*sigh* I get it."
            scene 82_s100 with dissolve
            reham "Please don't be sad. It's not a refusal of you, it's just the terms. I'm still here. Still on your side."
            scene 82_s101 with dissolve
            mc "Thanks anyway, Reham."
            scene 82_s100 with dissolve
            reham "Of course. Always."
            reham "Why don't you go to bed now? You need proper warmth, deep sleep."
            scene 82_s101 with dissolve
            mc "Yeah, alright. You have a point. My arm's killing me."
            scene 82_s100 with dissolve
            reham "Have a good rest."
            scene 82_s101 with dissolve
            jump scene82_4

label scene82_choice04_op2_woah:
    empathy "A flicker of hesitation stirs in your chest. Reham's pride, her careful mannerisms, it's not just about coin. Taking her without paying feels like stealing something she's guarded fiercely."
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1

    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene81_choice00 with dissolve

label scene82_choice04_op2:
    $ mc_harem_reham = True
    $ mc_harem_reham_dom_dom = True
    mc "*grin* Coin's safer in my pocket."
    scene 82_s109 with dissolve
    perception "Her eyes narrow with delighted challenge. Heat rises in her cheeks, but she doesn't pull away—instead, she leans closer, testing."
    scene 82_s110 with dissolve
    reham "Oh? Keeping me in debt already? Bold... and dangerous."
    scene 82_s109 with dissolve
    mc "Dangerous for who? You're the one who'll be begging to pay it off."
    scene 82_s110 with dissolve
    reham "C-Confident words, master... Wha... What if {i}I{/i} make you work for my surrender?"
    scene 82_s109 with dissolve
    mc "Try it. See how long you last before you're on your knees."
    scene 82_s110 with dissolve
    reham "Hnn... It still feels... strange. I've never had a master quite like this."
    reham "I'm not some brothel girl trading flesh for coin..."
    reham "Could you Indulge me one thing?"
    scene 82_s109 with dissolve
    mc "Go on."
    scene 82_s110 with dissolve
    reham "If I'm to truly dedicate myself to you then I need to see more."
    scene 82_s109 with dissolve
    mc "Like what?"
    scene 82_s110 with dissolve
    reham "Safety. Strength. A man who can wrap those arms around me... lift me like I weigh nothing."
    scene 82_s109 with dissolve
    mc "*chuckles* Lift you?"
    scene 82_s110 with dissolve
    reham "Old custom from my hometown. A real man proves he can carry his woman, literally. Sweep her off her feet, hold her steady. Shows he's got the power to protect what's his."
    reham "Think you're up for it, [mc]? Wound and all?"
    scene 82_s109 with dissolve
    scene 82_s93 with Dissolve(1.0)
    reham "Umm, what are you—?"
    reham "[mc]! I was joking! You should not strain that wound!"
    scene 82_s94 with Dissolve(1.0)
    perception "You slide your right arm under her knees. She's warm, curves pressing close as you hoist her effortlessly, her surprised laugh vibrating against your chest."
    reham "*laughs* Oh! Stronger than you look... and that wound didn't even flinch."
    scene 82_s95 with dissolve
    mc "See? Mine to carry. Mine to keep."
    scene 82_s94 with dissolve
    reham "*laughs* Put me down! I'm starting to feel dizzy."
    scene 82_s92 with Fade(0.5,0.5,0.5)
    reham "Alright... Contract signed. Or was it—!?"
    play sound "sound_effects/body/smack.mp3"
    scene 82_s96 with vpunch
    reham "Hmph!"
    perception "She twists suddenly, throwing a quick, jab toward your ribs."
    scene 82_s97 with dissolve
    reham "Impressive reflexes~"
    reham "You... You can let go now."
    scene 82_s98 with dissolve
    call screen scene82_choice03 with dissolve
        
label scene82_choice04_op1:
    $ mc_harem_reham = True
    $ mc_harem_reham_dom = True
    mc "Consider yourself hired."
    $ mc_coin -= reham_new_price
    scene 82_s102 with dissolve
    mc "Here's your payment."
    perception "You pull out a pouch filled with [reham_price] coins."
    scene 82_s103 with dissolve
    mc "But."
    scene 82_s104 with dissolve
    reham "Hmm?"
    mc "You'll earn every piece after today the hard way. Night by night. On your knees, on your back, however I decide."
    jump scene82_2

label scene81_choice00_op3:
    $ mc_harem_reham = False
    $ mc_reham_backoff = True
    mc "You know what? Never mind."
    scene 82_s100 with dissolve
    reham "What's wrong? Are you backing off?"
    scene 82_s101 with dissolve
    mc "Yeah. This isn't going the way I wanted."
    scene 82_s100 with dissolve
    reham "Aww... You're wounding my already fragile ego, [mc]."
    scene 82_s101 with dissolve
    mc "It's not you. I just changed my mind."
    scene 82_s100 with dissolve
    reham "...As you wish."
    reham "*sigh* Why don't you go to bed now? I noticed that you were wincing in pain ever since you woke up."
    scene 82_s101 with dissolve
    mc "Yeah, alright. You have a point. My arm's killing me."
    scene 82_s100 with dissolve
    reham "Have a good rest."
    scene 82_s101 with dissolve
    jump scene82_4

label scene82_2:
    scene 82_s101 with dissolve
    empathy "Her breath stutters, body softening against yours in the same instant it tenses with heat. The playful spark in her eyes shifts into something darker, willing."
    scene 82_s100 with dissolve
    reham "Confident, aren't you? Careful, master... a proud woman can make a man beg just as easily."
    play sound "sound_effects/clothing_rustle.mp3"
    scene 82_s106 with dissolve
    mc "Then we'll see who begs first. But you're already in my arm, Reham. Already caught."
    scene 82_s108 with dissolve
    reham "...So I am."
    scene 82_s106 with dissolve
    mc "Say it. Say you're mine."
    scene 82_s108 with dissolve
    reham "Seriously?"
    scene 82_s106 with dissolve
    mc "Say. It."
    scene 82_s111 with dissolve
    perception "You notice a shift in her attitude whenever you take charge. It's as if she... likes it?"
    reham "..."
    scene 82_s108 with dissolve
    reham "I'm... I-I'm yours, master. Body, service, everything. Claim me however you want."
    scene 82_s106 with dissolve
    mc "Good. Contract sealed."
    scene 82_s108 with dissolve
    reham "It still feels... strange. I've never had a master quite like this."
    reham "I'm not some brothel girl trading flesh for coin..."
    reham "Could you Indulge me one thing?"
    scene 82_s106 with dissolve
    mc "Name it."
    scene 82_s108 with dissolve
    reham "If I'm to truly dedicate myself to you then I need to see more."
    scene 82_s106 with dissolve
    mc "Like what?"
    scene 82_s108 with dissolve
    reham "Safety. Strength. A man who can wrap those arms around me... lift me like I weigh nothing."
    scene 82_s106 with dissolve
    mc "*chuckles* Lift you?"
    scene 82_s108 with dissolve
    reham "Old custom from my hometown. A real man proves he can carry his woman, literally. Sweep her off her feet, hold her steady. Shows he's got the power to protect what's his."
    reham "Think you're up for it, [mc]? Wound and all?"
    scene 82_s93 with Dissolve(1.0)
    reham "Umm, what are you—?"
    reham "[mc]! I was joking! You should not strain that wound!"
    scene 82_s94 with Dissolve(1.0)
    perception "You slide your right arm under her knees. She's warm, curves pressing close as you hoist her effortlessly, her surprised laugh vibrating against your chest."
    reham "*laughs* Oh! Stronger than you look... and that wound didn't even flinch."
    scene 82_s95 with dissolve
    mc "See? Mine to carry. Mine to keep."
    scene 82_s94 with dissolve
    reham "*laughs* Put me down! I'm starting to feel dizzy."
    scene 82_s92 with Fade(0.5,0.5,0.5)
    reham "Alright... Contract signed. Or was it—!?"
    play sound "sound_effects/body/smack.mp3"
    scene 82_s96 with vpunch
    reham "Hmph!"
    perception "She twists suddenly, throwing a quick, jab toward your ribs."
    scene 82_s97 with dissolve
    reham "Impressive reflexes~"
    reham "You... You can let go now."
    scene 82_s98 with dissolve
    call screen scene82_choice03 with dissolve

label scene82_choice03_op1:
    scene 82_s101 with dissolve
    mc "Feel more at ease now?"
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 82_s100 with dissolve
    if mc_harem_reham_dom_dom:
        reham "Yes. Contract sealed, on your terms. Now... how do you want your servant to start serving?"
        hide screen stat_change with easeoutright
        $ karma_more = False
    else:
        reham "Yes. Contract sealed. Now... before you start ordering me around, master. I have to request that you take some rest."
        reham "You look like death warmed over, and not in a good way. You need proper warmth, deep sleep."
        hide screen stat_change with easeoutright
        $ karma_more = False
    scene 82_s101 with dissolve
    call screen scene82_choice05 with dissolve

label scene82_choice03_op2:
    $ mc_squeeze_reham = True
    mc "Not yet."
    scene 82_s99 with dissolve
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    reham "Ah! Alright, alright, alright! I get it!"
    mc "*chuckles* Good enough?"
    hide screen stat_change with easeoutright
    $ karma_less = False
    reham "Ouch... Yes!"
    scene 82_s100 with Dissolve(1.3)
    reham "Message received. You're plenty strong."
    scene 82_s101 with dissolve
    mc "Feel more at ease now?"
    scene 82_s100 with dissolve
    if mc_harem_reham_dom_dom:
        reham "Yes. Contract sealed, on your terms. Now... how do you want your servant to start serving?"
    else:
        reham "Yes. Contract sealed. Now... before you start ordering me around, master. I have to request that you take some rest."
        reham "I noticed that you were wincing in pain ever since you woke up."
    scene 82_s101 with dissolve
    call screen scene82_choice05 with dissolve

label scene82_choice05_op1:
    if mc_harem_reham_dom_dom:
        mc "Take off your clothes. Then come to bed and keep me warm."
        scene 82_s110 with dissolve
        reham "Hngg... What will you do to me, master?"
        scene 82_s109 with dissolve
        mc "Exactly what I want. But tonight? I just want this body pressed against mine. Warming me."
        scene 82_s110 with dissolve
        reham "Ah... Of course."
        reham "A-As you wish, master."
        stop music fadeout 2.0 
        scene 82_s109 with dissolve
        scene 82_s9 with Fade(1.5,1.0,1.5)
        ""
        play sound "sound_effects/body/clothes1.mp3"
        scene 82_s10 with Dissolve(1.0)
        perception "She obeys without hesitation, fingers working ties and buttons, shedding layers until nothing remains but her panties. Candlelight tracing every curve of her body."
        mc "Your body is beautiful. Every inch mine now."
        scene 82_s11 with Dissolve(1.0)
        reham "*giggles* Make room, master."
        
    elif mc_harem_reham_dom:
        mc "Come over to bed with me and keep me warm."
        scene 82_s110 with dissolve
        reham "Oh? Already going to the strong stuff? I told you, I'm not some sultry tavern girl who falls into bed at a snap of fingers..."
        scene 82_s109 with dissolve
        mc "Who said anything about sultry? I just want your warmth. Though if more happens... I won't complain."
        scene 82_s110 with dissolve
        reham "*sigh* Fine... The truth is, master. I've actually been doing it every night for the past two weeks already."
        reham "You kept shivering so violently I feared you'd shake your stitches loose."
        scene 82_s109 with dissolve
        mc "Are you serious?"
        scene 82_s110 with dissolve
        reham "Should I not have? Would you have preferred to succumb to hypothermia? It's a rather unpleasant way to go."
        scene 82_s109 with dissolve
        mc "In that case... I definitely don't mind some warmth tonight too."
        scene 82_s110 with dissolve
        reham "Of course. But as you said, nothing sultry."
        scene 82_s109 with dissolve
        mc "Right."
        scene 82_s110 with dissolve
        reham "Good. Go ahead and lie down. I'll be with you shortly."
        scene 82_s109 with dissolve
        stop music fadeout 2.0 
        scene 82_s9 with Fade(1.0,1.5,1.0)
        mc "Reham? What are you doing?"
        reham "If we're doing this properly... these get in the way of body heat."
        play sound "sound_effects/body/clothes1.mp3"
        scene 82_s10 with Dissolve(1.0)
        mc "I see..."
        reham "Don't worry, I'll still be wearing my panties."
        scene 82_s11 with Dissolve(1.3)
        reham "Make room, master."

    jump scene82_3

label scene82_choice05_op2:
    if mc_harem_reham_dom_dom:
        mc "Nothing for now."
        scene 82_s110 with dissolve
        reham "Are you sure, master?"
        scene 82_s109 with dissolve
        mc "Are you questioning me?"
        scene 82_s110 with dissolve
        reham "I-I apologize..."
        scene 82_s109 with dissolve
        mc "*chuckles* Good. Now stay here and watch over Maia."
        scene 82_s110 with dissolve
        reham "Yes, master."
        scene 82_s109 with dissolve

    elif mc_harem_reham_dom:
        mc "Yeah, alright. You have a point. My arm's killing me."
        scene 82_s100 with dissolve
        reham "Good. Have a good rest, master."
        scene 82_s101 with dissolve
        
    jump scene82_4

label scene82_3:
    play music "fire.mp3" fadein 4.0 volume 0.4 loop
    if mc_harem_reham_dom_dom:
        scene 82_s12 with Fade(1.0,1.0,1.0)
        reham "There... all of me for you."
        scene 82_s13 with dissolve
        mc "Good girl."
        mc "You're really warm. And... soft."
        scene 82_s12 with dissolve
        reham "*giggles* Flatterer."
        scene 82_s13 with dissolve
        sensation "Her body is a living furnace against your cold body, soft and yielding in all the right places. A strange, captivating scent of foreign flowers, spicy and sweet, unlike anything you've ever smelled—emanates from her hair and skin."
        reham "..."
        mc "(Shit...)"
        scene 82_s14 with dissolve
        sensation "As if on cue, your cock begins perking up. The soft, firm pressure of her ass grinding against you as she moves is undeniable. Your body, starved for sensation and finally safe, responds on its own accord."
        reham "Umm... [mc]?"
        mc "Yeah?"
        scene 82_s16 with dissolve
        reham "I feel something poking me rather insistently."
        scene 82_s15 with dissolve
        mc "Can't help it. You're naked and mine."
        scene 82_s16 with dissolve
        reham "*giggles* A healthy sign. Means my master is very much alive... and very demanding."
        scene 82_s15 with dissolve
        mc "Keep teasing and see what happens."
        scene 82_s16 with dissolve
        reham "Is... Is it fully erect?"
        scene 82_s15 with dissolve
        mc "Yes."
        scene 82_s112 with dissolve
        reham "Then let your servant take care of it. You've been without release too long. It's my duty to fix that~"
        reham "It's no good for a strong man, you know? To go so long without relief. It can cause congestion in the prostate, lead to pain, even infection."
        scene 82_s113 with dissolve
        mc "*chuckles* You're acting really differently now."
        scene 82_s112 with dissolve
        reham "Yes, master. Because you own me. Because you refused my coin and made me yours anyway. I want to serve... I want to please the man strong enough to do what he wants."
        reham "That... does something to me. Makes me want to be good for you."
        scene 82_s113 with dissolve
        mc "*chuckles* So... you have a submissive side?"
        scene 82_s112 with dissolve
        reham "Y-Yes..."
        scene 82_s113 with dissolve
        mc "You like it when I take charge."
        scene 82_s112 with dissolve
        reham "I do."
        scene 82_s113 with dissolve
        mc "It's all making sense now. Your old masters tried too hard to be kind, too soft. They never figured out what you really needed."
        scene 82_s112 with dissolve
        reham "*ahem* I-I still expect kindness and respect, master."
        reham "But... yes. When a strong man takes control... it wakes something in me."
        reham "Let me help you, master. It will help you sleep. A tense body cannot heal."
        if not mc_maia_left:
            reham "Maia is in no state to provide you with this kind of care. The duty, for now, falls to me."
        else:
            reham "You have no one else here to provide this for you. So the duty falls to your servant. Let me do my job."
        scene 82_s113 with dissolve

    elif mc_harem_reham_dom:
        scene 82_s12 with Fade(1.0,1.0,1.0)
        reham "There. Now, pull me closer and hug me tight. You need to stop thinking and let your body relax."
        scene 82_s13 with dissolve
        mc "Alright."
        mc "You're really warm. And... soft."
        scene 82_s12 with dissolve
        reham "*giggles* Flatterer."
        scene 82_s13 with dissolve
        sensation "Her body is a living furnace against your cold body, soft and yielding in all the right places. A strange, captivating scent of foreign flowers, spicy and sweet, unlike anything you've ever smelled—emanates from her hair and skin."
        reham "..."
        mc "(Shit...)"
        scene 82_s14 with dissolve
        sensation "As if on cue, your cock begins perking up. The soft, firm pressure of her ass grinding against you as she moves is undeniable. Your body, starved for sensation and finally safe, responds on its own accord."
        reham "Umm... [mc]?"
        mc "Y-Yeah?"
        scene 82_s12 with dissolve
        reham "I feel something poking me rather insistently."
        scene 82_s13 with dissolve
        mc "..."
        scene 82_s16 with dissolve
        reham "*giggles* Are you getting excited? After everything, your body is still so eager for life."
        scene 82_s15 with dissolve
        mc "Sorry. I... I don't really have any control over that. It's just a reaction."
        scene 82_s16 with dissolve
        reham "I know. It's a healthy sign. It means your body is healing. Don't apologize for being alive."
        scene 82_s15 with dissolve
        mc "Uhh... Reham, maybe if you move forward a bit? You're really, {i}really{/i} close."
        scene 82_s16 with dissolve
        reham "It's fine. Body heat works better with full contact. But let me ask... is it fully hard now?"
        scene 82_s15 with dissolve
        mc "Yes... Why?"
        scene 82_s16 with dissolve
        reham "Hmm... I suppose it makes sense. You've been asleep for two weeks, your body trapped in a fight for survival. There was no opportunity for... release."
        reham "It's no good for a man, you know? To go so long without relief. It can cause congestion in the prostate, lead to pain, even infection."
        scene 82_s15 with dissolve
        mc "Reham... you literally just said nothing sultry."
        scene 82_s16 with dissolve
        reham "I did say that. And I meant it... until you started talking to me like you own me."
        reham "It... does something to me. Makes me want to be good for you. Makes me want to please the man who can handle me like that."
        scene 82_s15 with dissolve
        mc "So... you have a submissive side?"
        scene 82_s16 with dissolve
        reham "...N-No?"
        scene 82_s15 with dissolve
        mc "*chuckles* You do. You like it when I take charge."
        reham "..."
        mc "It's all making sense now. Your old masters tried too hard to be kind, too soft. They never figured out what you really needed."
        scene 82_s16 with dissolve
        reham "*ahem* Don't get ahead of yourself. I still expect kindness and respect."
        scene 82_s17 with dissolve
        reham "But... yes. When a strong man takes control... it wakes something in me."
        reham "And I'm still your healer tonight. Your well-being is my responsibility. And right now... relieving this tension will help you heal. Help you sleep."
        reham "Come on. Let me help you, master. It will help you sleep. A tense body cannot heal."
        if not mc_maia_left:
            reham "Maia is in no state to provide you with this kind of care. The duty, for now, falls to me."
        else:
            reham "You have no one else here to provide this for you. So the duty falls to your servant. Let me do my job."
        scene 82_s18 with dissolve
    
    call screen scene82_choice06 with dissolve
    
label scene82_choice06_op2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene8_p6_replay:
        $ persistent.scene8_p6_replay = True

    scene 82_s113 with dissolve
    mc "You want to touch me, huh?"
    scene 82_s112 with dissolve
    reham "Yes..."
    scene 82_s113 with dissolve
    mc "Then ask properly. Beg your master like a good girl."
    scene 82_s112 with dissolve
    reham "P-Please... master. Let me serve you. Let me ease the ache you've been carrying. I need to feel you let go because of me."
    scene 82_s113 with dissolve
    mc "Louder. Convince me."
    scene 82_s112 with dissolve
    reham "Please, [mc]. I want to make you feel good. I want to be the one who takes it all. Use me for your relief..."
    scene 82_s113 with dissolve
    mc "Good girl."
    jump scene85_reham

label scene82_choice06_op1:
    mc "Not today."
    scene 82_s19 with dissolve
    reham "...What?"
    scene 82_s20 with dissolve
    mc "You're right, I need rest. And you need to learn that I decide when you earn the privilege of touching me."
    scene 82_s19 with dissolve
    reham "You're... denying me?"
    scene 82_s20 with dissolve
    mc "Yes. Tonight you just keep me warm. Feel how hard you've made me... and wait. Good girls get rewarded when they're patient."
    scene 82_s19 with dissolve
    reham "...Yes, master."
    scene 82_s20 with dissolve
    mc "Tomorrow, if you're very good... maybe I'll let you beg again."
    scene 82_s19 with dissolve
    reham "I'll be good. I promise."
    scene 82_s20 with dissolve
    jump scene82_4

image 85_tj1 = Movie(play="images/chapter4/scene82/82_tj1.webm", loop=True)
image 85_tj2 = Movie(play="images/chapter4/scene82/82_tj2.webm", loop=True)
image 85_tj2_faster = Movie(play="images/chapter4/scene82/82_tj2_faster.webm", loop=True)

image 85_hj1 = Movie(play="images/chapter4/scene82/82_hj1.webm", loop=True)
image 85_hj2 = Movie(play="images/chapter4/scene82/82_hj2.webm", loop=True)

image 85_hj_feet = Movie(play="images/chapter4/scene82/82_hj_feet.webm", loop=True)
image 85_hj_feet2 = Movie(play="images/chapter4/scene82/82_hj_feet2.webm", loop=True)

image 85_hj_pro = Movie(play="images/chapter4/scene82/82_hj_pro.webm", loop=True)

default scene82_reham1_speed = False

label scene85_reham:
    $ mc_sex_reham = True
    scene 82_s112 with dissolve
    reham "Could you undress your pants for me?"
    scene 82_s113 with dissolve
    scene 82_s21 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/clothing_rustle.mp3"
    reham "Oh, my... I..."
    scene 82_s22 with dissolve
    mc "Something wrong? Is my penis infected or something?"
    scene 82_s21 with dissolve
    reham "*ahem* No, not at all, it's just..." 
    reham "It's just... more impressive than I anticipated."
    reham "Now, relax. Close your eyes if it helps. And... begin thrusting between my thighs."
    scene 82_s22 with dissolve
    show 85_tj1 with dissolve
    mc "Ahhnn..."
    reham "Slow at first. Let the pressure do the work."
    sensation "The soft, warm pressure of her inner thighs is maddening. With every thrust, a slick heat coming from her pussy coaxes you closer to the edge."
    mc "Reham...!"
    reham "Already at the edge?"
    mc "It's been so long!"
    sensation "With every retreat, her muscles contract instinctively, stroking and squeezing your shaft."
    reham "Does it hurt? If you need to focus, just... pretend you're thrusting into a woman who isn't particularly impressed. It can help with control."
    mc "*chuckles* What? How... nghn... is that supposed to help? That's... the opposite of helpful..."
    reham "It's what I always saw whenever I accidentally walked in on my previous master's intimate time with his wife."
    reham "Just focus on the sensation. On the release. Let it build. You're doing very well."
    reham "Go faster. Don't worry about ejaculating on the bed. If you make a mess, I can clean—"
    show 85_tj2 with dissolve
    hide 85_tj1
    reham "—Hah?!"
    perception "You grip her breast hard and start fucking her thighs faster. The force rocks her entire body, her breath catching as her thighs struggle to keep you steady."
    mc "Nghn—!"
    reham "[mc]... *giggles* You're like an animal in heat..."
    mc "I'm... I'm close...!"
    reham "Then finish. Let it go. Your body has held onto this tension for too long."
    call screen scene82_reham1 with dissolve 

default scene82_reham1_fast_first = True
default scene82_reham1_slow_first = True

label scene82_reham1_fast:
    $ scene82_reham1_speed = True
    show 85_tj2_faster with dissolve
    hide 85_tj2
    if scene82_reham1_fast_first:
        $ scene82_reham1_fast_first = False
        reham "Nhnn~!"
        reham "{size=30}This speed... inside me... it would make me pass out...{/size}"
        mc "I can hear you, you know?"
        reham "Ohh—! I..."
        mc "Already imagining me fucking your pussy like this?"
        reham "D-Don't say that... I'm just... helping you here."
        mc "*chuckles* Sure you are."
    else:
        sensation "Her pussy grows slicker with every rapid thrust, the friction turning hot and wet, her body betraying how much the pace excites her."
        reham "Ahnn~! Master!"
        mc "Harder. Squeeze those thighs tighter around me."
        reham "Yes, master... like this?"
    call screen scene82_reham1 with dissolve 

label scene82_reham1_slow:
    show 85_tj2 with dissolve
    hide 85_tj2_faster
    $ scene82_reham1_speed = False
    if scene82_reham1_slow_first:
        $ scene82_reham1_slow_first = False
        reham "Master~... damn it... why am I like this?"
        mc "Like what?"
        reham "I can't help it... the way you spoke to me earlier, the way you claimed me... and now look where we are."
        reham "It happened so quickly... I'm really ashamed of myself."
        mc "Nothing to be ashamed of. You're perfect like this."
        reham "...You're making it very hard to stay professional."
    else:
        sensation "The slower rhythm lets every inch drag against her skin. She shivers, thighs trembling as the teasing friction builds a deeper, aching heat."
        reham "I can feel every... single... vein..."
    call screen scene82_reham1 with dissolve 

label scene82_reham1_cum:
    mc "Ahhng—! I'm gonna cover those fat thighs!"
    perception "Reham braces herself, her hands slipping against your hips as your thrusts grow erratic, desperate—no rhythm left, just raw need driving your body forward."
    scene 82_s23 with Dissolve(0.3)
    play sound "se_sfx/sex/sex_cum4.mp3" 
    scene 82_s23 with vpunch
    perception "Your hips slam forward on instinct, burying yourself between her thighs as thick, hot cum spills out in messy, pulsing ropes."
    reham "Ahn—! Gods!"
    scene 82_s24 with Dissolve(0.3)
    play sound "se_sfx/sex/sex_cum3.mp3" 
    scene 82_s24 with vpunch
    perception "Her breath hitches as your cum splashes across her thighs, even her hand when she instinctively tries to steady you."
    reham "That's it... let it all out. Don't fight it."
    scene 82_s25 with dissolve
    mc "Hahhn... Hahh..."
    scene 82_s26 with dissolve
    reham "Is it... is it over?"
    scene 82_s25 with dissolve
    mc "Yeah..."
    scene 82_s26 with dissolve
    reham "My... That's..."
    scene 82_s25 with dissolve
    mc "I made a mess, huh?"
    scene 82_s26 with dissolve
    reham "N-No it's fine. I can clean it up later."
    reham "[mc]... Your cock. It's still hard."
    scene 82_s25 with dissolve
    mc "Hmm? Oh, right... Guess one time wasn't enough after so long."
    scene 82_s26 with dissolve
    reham "*ahem* Well... I don't mind helping you some more."
    scene 82_s25 with dissolve
    if mc_harem_reham_dom_dom:
        call screen scene82_choice07 with dissolve
    else:
        mc "Seriously? You already helped... A lot."
        scene 82_s26 with dissolve
        reham "I don't mind."
        scene 82_s25 with dissolve
        call screen scene82_choice07 with dissolve

label scene82_choice07_op1:
    mc "Go ahead."
    scene 82_s26 with dissolve
    reham "Mhm. Just keep lying down."
    scene 82_s25 with dissolve
    jump scene82_reham2

label scene82_choice07_op2:
    mc "You already did enough, Reham. I appriciate it but my penis will calm it self down with time."
    scene 82_s26 with dissolve
    reham "Right... Of course. How about we truly rest now?"
    scene 82_s25 with dissolve
    mc "Hahh... Yeah."
    $ renpy.end_replay()
    jump scene82_4

label scene82_reham2:
    scene 82_s114 with Fade(1.0,1.0,1.0)
    reham "There. Just lift your hips and rest it on my thighs."
    show 85_hj1 with dissolve
    sensation "She wets her palm with her tongue before her fingers close around your cock. Her fingers are rough, the slight texture is contrast to the softness of her thighs."
    mc "Ahh..."
    reham "I apologize if my hands aren't the softest you've felt. Being a foreign maid, I was often given labor intensive work. Scrubbing floors, hauling laundry. These hands have seen more soap than silk."
    mc "No, it's... it's fine. It just feels... really sensitive. It's been a while."
    reham "Oh, right. Abstinence will do that. It heightens the sensitivity, especially here..."
    show 85_hj2 with dissolve
    hide 85_hj1
    reham "...at the very tip. I learned during my sexual education class that this is the most sensitive part of the penis."
    reham "Focusing here will help you release faster and more completely."
    sensation "Her fingers tease and rub your sensitive glans, and a violent shiver of pleasure racks your entire body."
    reham "How does this feel? Am I helping?"
    mc "Fuck! Reham!"
    reham "*giggles* Too much? Should I stop?"
    mc "No! Keep going!"
    call screen scene82_reham2 with dissolve

default scene82_reham2_hj1_first = True
default scene82_reham2_hj2_first = True
default scene82_reham2_hj_feet_first = True
default scene82_reham2_hj_pro_first = True

default scene85_reham2_hj = False
default scene85_reham2_feet = False
default scene85_reham2_pro = False

label scene82_reham2_hj1:
    $ scene85_reham2_hj = True
    $ scene85_reham2_feet = False
    $ scene85_reham2_pro = False
    scene black with Dissolve(0.3)
    show 85_hj1 with dissolve
    if scene82_reham2_hj1_first:
        $ scene82_reham2_hj1_first = False
        mc "Nghn~!"
        sensation "She applies more pressure to the tip, the sensation so intensely good it borders on painful. Your precum spills out, and she uses it to slick her movements, creating a wet, looping friction that drives you wild."
        reham "There. There. Just let it happen. Don't fight it, master. Let it {i}all{/i} out."
        reham "You've held onto so much pain... let this be a release from that, too."
    else:
        reham "You're throbbing so much... I can feel how close you are."
        mc "Keep going... just like that."
        reham "As you wish, master."
    call screen scene82_reham2 with dissolve

label scene82_reham2_hj2:
    $ scene85_reham2_hj = True
    $ scene85_reham2_feet = False
    $ scene85_reham2_pro = False
    scene black with Dissolve(0.3)
    show 85_hj2 with dissolve
    if scene82_reham2_hj2_first:
        $ scene82_reham2_hj2_first = False
        reham "So fast already... you're pulsing in my hand."
        mc "Don't slow down."
        reham "I won't... I want to feel you lose control."
        sensation "The pace turns relentless, wet strokes focused on the sensitive head, her grip tightening just enough to make your hips buck."
    else:
        reham "You like it? Hard and fast until you can't hold back?"
        mc "Hnng..."
    call screen scene82_reham2 with dissolve

label scene82_reham2_hj_feet:
    $ scene85_reham2_hj = False
    $ scene85_reham2_feet = True
    $ scene85_reham2_pro = False
    if scene82_reham2_hj_feet_first:
        $ scene82_reham2_hj_feet_first = False
        mc "Reham! Shove your feet on my face! Now!"
        reham "M-My feet? You want... my feet?"
        mc "Yes! Just do it!"
        reham "If the smell of my feet is what pushes you over the edge, then by all means... let it."
        scene black with Dissolve(0.3)
        show 85_hj_feet with dissolve
        perception "She presses her foot firmly against your cheek and mouth. The scent and the relentless motion of her hand, sends a jolt of pure lightning through your spine. More precum leaks out in a steady stream."
        reham "Can you breathe, master?"
        scene black with Dissolve(0.3)
        show 85_hj_feet2 with dissolve
        mc "Mhmm..."
        reham "Ahhn~! You're... licking my toes!"
        mc "Tasty."
        reham "*chuckles* Perverted master... I love it."
    else:
        scene black with Dissolve(0.3)
        show 85_hj_feet with dissolve
        perception "She presses her feet harder this time, toes curling against your lips, knowing exactly how much you crave it."
        reham "You're leaking so much... my feet really do this to you, don't they?"
        scene black with Dissolve(0.3)
        show 85_hj_feet2 with dissolve
        mc "*slurp* *lick*"
    call screen scene82_reham2 with dissolve

label scene82_reham2_hj_pro:
    $ scene85_reham2_hj = False
    $ scene85_reham2_feet = False
    $ scene85_reham2_pro = True
    if scene82_reham2_hj_pro_first:
        $ scene82_reham2_hj_pro_first = False
        mc "Reham! Put your finger in my ass!"
        reham "Huh!?"
        mc "Trust me. Do it."
        reham "Alright... I've heard a man's prostate is... exquisite. I'll be gentle."
        scene black with Dissolve(0.3)
        show 85_hj_pro with dissolve
        perception "She inserts her sweaty finger into your anus slowly and begins moving it in and out."
        sensation "The dual pressure, firm strokes outside, teasing press inside sends lightning up your spine. Precum flows freely, coating her fingers."
        reham "There... feel that? Let it build."
        reham "Do it. Wet my hands with your seed, master."
    else:
        scene black with Dissolve(0.3)
        show 85_hj_pro with dissolve
        sensation "She finds the spot immediately this time, pressing with confident rhythm while her grip tightens."
        reham "I can feel you clenching around my finger. Does it really feel that good?"
        mc "Ahhn! It does."
    call screen scene82_reham2 with dissolve

label scene82_reham2_cum:
    reham "Come for me, [mc]. Now. I want to feel it. Let go."
    mc "Nghn!"
    if scene85_reham2_feet:
        play sound "se_sfx/sex/sex_cum2.mp3" 
        scene 82_s27 with vpunch
        sensation "Your whole body locks as thick ropes of cum surge out painting her palm and wrist while the scent and taste of her feet flood every last shred of your mind."
    elif scene85_reham2_pro:
        play sound "se_sfx/sex/sex_cum3.mp3" 
        scene 82_s39 with vpunch
        sensation "Pleasure detonates behind your eyes. Your hips jerk helplessly as the pressure on your prostate forces an endless release, thick spurts painting her palm and wrist while your vision whites out."
    else:
        play sound "se_sfx/sex/sex_cum7.mp3" 
        scene 82_s27 with vpunch
        sensation "It's not a gentle ejaculation, but an eruption that seems to drain weeks of pain, fear, and tension from your very soul. White hot seed spill on her hands in waves."
    reham "Just... Just let it all out."
    play sound "se_sfx/sex/sex_cum9.mp3" 
    scene 82_s28 with vpunch
    mc "Ahhnn!"
    reham "Oh, my!"
    scene 82_s29 with Dissolve(1.0)
    perception "Her hand stills, her grip gentle now. She brings her cum covered fingers to her nose, inhaling with curiosity."
    reham "*sniff* Ahh... Potent. You could easily impregnate a woman with seed. It speaks well of your health."
    scene 82_s30 with Dissolve(1.0)
    mc "*chuckles* Hah... Thank you?"
    scene 82_s31 with dissolve
    reham "It is a compliment where I'm from. It means the essence of your manhood is strong."
    reham "In my country, you would be highly sought after by women struggling with fertility problems."
    scene 82_s30 with dissolve
    mc "*laughs* You're making me want to go there sooner."
    scene 82_s31 with dissolve
    reham "Do you feel better? The tension is gone?"
    scene 82_s30 with dissolve
    mc "Yeah. I do. Thank you, Reham. It feels like... a weight has been lifted."
    scene 82_s31 with dissolve
    reham "I'm glad to be of service, master."
    scene 82_s30 with dissolve
    scene 82_s33 with Dissolve(1.8)
    mc "Ahn! Reham? You're sitting right on my balls..."
    scene 82_s32 with dissolve
    reham "Am I? I hadn't noticed..."
    scene 82_s33 with dissolve
    perception "She stays there a moment longer, letting the weight and warmth sink in, before finally easing up with a satisfied sigh."
    scene 82_s32 with dissolve
    reham "How about you finally get that much needed rest now, master?"
    scene 82_s33 with dissolve
    $ renpy.end_replay()
    call screen scene82_choice08 with dissolve

label scene82_choice08_op2:
    scene 82_s35 with Dissolve(1.0)
    mc "I have to say... I really like the way you look with my cum all over that pretty face."
    scene 82_s36 with dissolve
    reham "Oh?"
    scene 82_s35 with dissolve
    mc "Yeah. Think we should make it an occasional thing."
    scene 82_s36 with dissolve
    reham "Maybe~"
    scene 82_s35 with dissolve
    jump scene82_4

label scene82_choice08_op1:
    mc "Yeah, alright. I still need you to keep me warm."
    scene 82_s32 with dissolve
    reham "Of course."
    scene 82_s33 with dissolve
    jump scene82_4

label scene82_4:
    stop music fadeout 1.0 
    scene 82_s40 with Fade(1.5,1.0,1.5)
    ""
    scene 82_s41 with dissolve
    reham "[mc]! Wake up!"
    mc "Hmmn?"
    scene 82_s42 with Dissolve(1.0)
    m "*cough* *cough*"
    alex "What wrong? I heard screaming."
    reham "She just spoke! Can you hear me, Maia?"
    play music "sad/maia3.mp3" fadein 4.0 loop
    scene 82_s43 with Dissolve(1.0)
    mc "M-Maia!? Hey, look at me. Can you open your eyes?"
    scene 82_s44 with dissolve
    m "...[mc]? Is that... really you?"
    scene 82_s43 with dissolve
    mc "*sigh* Oh, thank God... Yes, it's me."
    scene 82_s46 with dissolve
    m "W-What's going on? The last thing I remember is... the cold. So cold. Where... Where are we?"
    scene 82_s45 with dissolve
    reham "Shhh, calm down. You're in a safe place. You've been very sick, but the worst is over now."
    scene 82_s47 with dissolve
    m "[mc]... your arm... I'm so sorry... This is because of me..."
    scene 82_s48 with dissolve
    mc "Don't. Don't you dare blame yourself for this."
    reham "You gave us quite a scare. I wasn't sure you'd make it when I first found you."
    scene 82_s46 with dissolve
    m "I'm so sorry... This is all my fault. If I hadn't been so foolish, listening to her and going out on my own..."
    scene 82_s45 with dissolve
    mc "Listening to who?!"
    scene 82_s46 with dissolve
    m "Lady Avery. She... she summoned me. She ordered me to start making trips to the market district. She said it was to make me seem more... normal... to the other maids."
    scene 82_s45 with dissolve
    mc "You weren't going out on your own?"
    scene 82_s46 with dissolve
    m "N-No... I would never be so bold. I was terrified every time."
    scene 82_s45 with dissolve
    alex "*scoff* Of course. Always one step ahead."
    scene 82_s50 with dissolve
    m "I'm really sorry, [mc]! I-I should have told you! B-but she... she gets so angry if anyone questions her..."
    scene 82_s49 with dissolve
    mc "She's a traitor. And we're going to prove it. But first, you need to get your strength back. Just focus on that."
    scene 82_s50 with dissolve
    m "You came for me... even after everything..."
    scene 82_s49 with dissolve
    mc "Always."
    reham "Alright, that's enough. You need to conserve your energy. [mc], let her rest. I'll make some broth."
    scene 82_s51 with dissolve
    alex "She's right. We have work to do, [mc]. I need you."
    scene 82_s52 with dissolve
    mc "Work?"
    scene 82_s51 with dissolve
    alex "Keep watch. I'm going to scout the perimeter and see if I can pick up any news. We're blind out here."
    alex "I need to know what Avery is saying in the city."
    scene 82_s50 with dissolve
    m "[mc]! Why do you have to do this? Shouldn't we just run away!? Far away from here!"
    scene 82_s49 with dissolve
    mc "I can't, Maia. Where would we go? We'd be looking over our shoulders for the rest of our lives."
    mc "And it's not just us anymore. Alex has a brother to save. I can't ignore that."
    m "..."
    scene 82_s53 with Dissolve(1.0)
    m "Be careful."

    stop music fadeout 2.0 
    scene 82_s54 with Fade(1.5,1.0,1.3)
    play music "ambiance/river_water.mp3" fadein 1.0 loop
    alex "Sorry to pull you away, but I can't watch and scout at the same time."
    scene 82_s55 with dissolve
    mc "Alex, you look extremely tired. When's the last time you actually slept?"
    if mc_sex_reham:
        scene 82_s56 with dissolve
        alex "Don't. I'm not in the mood to hear you play concerned after you just spent the last night grunting between Reham's thighs."
        scene 82_s57 with dissolve
        mc "...You were spying on us?"
        scene 82_s56 with dissolve
        alex "I didn't need to spy. Your noises carried. Hers especially."
        scene 82_s57 with dissolve
        call screen scene82_choice09 with dissolve
    else:
        scene 82_s54 with dissolve
        alex "Don't worry about me. I can go for longer."
        scene 82_s55 with dissolve
        mc "If you say so. What do you want me to do?"
        jump scene82_5

label scene82_choice09_op1:
    $ mc_jealous_alex = True
    mc "Wait... are you jealous, Alex?"
    if mc_try_kiss_alex:
        scene 82_s56 with dissolve
        alex "Hah! Jealous? You've got balls asking that after yesterday."
        alex "You leaned in like you meant it, like you saw past the knives and the blood. And I froze because no one's ever looked at me that way."
        alex "Then right after I get a front-row seat to you and Reham. Felt like you decided I wasn't worth the wait."
        scene 82_s57 with dissolve
        mc "I thought you pulling away meant no."
        scene 82_s56 with dissolve
        alex "It meant I'm terrible at this. I don't do soft. I do missions, not... feelings."
        scene 82_s57 with dissolve
        mc "Alex—"
        scene 82_s56 with dissolve
        alex "*sigh* Forget it."
        alex "I just need you be more clear headed from now."
        scene 82_s57 with dissolve
        mc "Fine. What do you want me to do?"
    else:
        scene 82_s56 with dissolve
        alex "Jealous? Of what, exactly? That you found time to fuck while I was trying to keep us from dying?"
        scene 82_s57 with dissolve
        mc "You didn't enjoy the sounds?"
        scene 82_s56 with dissolve
        alex "Keep pushing, [mc]. See how far that gets you when I'm the one keeping watch over your careless ass."
        scene 82_s57 with dissolve
        mc "I just needed... something. For a minute. That's all."
        scene 82_s56 with dissolve
        alex "Well. Next time pick a minute when the world isn't trying to kill us."
        scene 82_s57 with dissolve
        mc "Just tell me what you want from me."
    jump scene82_5

label scene82_choice09_op2:
    $ mc_sowhat_alex = True
    mc "So what? I'm not allowed five damn minutes to feel human?"
    if mc_try_kiss_alex:
        scene 82_s56 with dissolve
        alex "Heh. Human? That's rich coming from the guy who tried to kiss me yesterday and then immediately spent the night with another girl."
        scene 82_s57 with dissolve
        mc "You turned away, Alex. I thought that was your answer."
        scene 82_s56 with dissolve
        alex "It wasn't an answer, it was panic. I freeze when... *sigh*"
        alex "And you just... moved on. Like it didn't matter."
        scene 82_s57 with dissolve
        mc "It mattered. I didn't want to push you when you pulled back."
        scene 82_s56 with dissolve
        alex "Forget it. Whatever that was, it will never work anyway. I know what I am. An assassin. A tool. Not the girl you build a life with."
        scene 82_s57 with dissolve
        mc "Whatever you say. What did you want me to do?"
    else:
        scene 82_s56 with dissolve
        alex "Human? You think sticking your cock in the first warm body you find makes you human? We're running for our lives, [mc]. Maia's half-dead in there and you're busy—"
        scene 82_s57 with dissolve
        mc "Don't lecture me. I carried that girl through a blizzard with a missing hand. I earned a few minutes."
        scene 82_s56 with dissolve
        alex "..."
        mc "Just tell me what you want from me."
    jump scene82_5
    
label scene82_choice09_op3:
    $ mc_apologize_reham_alex = True
    mc "...Fine. I get it. I wasn't thinking about how it looked. Or sounded. I'm sorry."
    if mc_try_kiss_alex:
        alex "..."
        scene 82_s60 with dissolve
        alex "*sigh* No. You don't have to apologize for needing comfort. God knows we all do."
        alex "But yesterday you looked at me like I was more than a blade. And I panicked because I believed it for a second."
        alex "Then I hear you with her and it's like... proof I was right all along. People don't stay for girls like me."
        scene 82_s61 with dissolve
        mc "I thought pulling away was your answer. A clear no. I didn't want to push and make you uncomfortable."
        scene 82_s60 with dissolve
        alex "I... I don't know what I want yet."
        scene 82_s61 with dissolve
        mc "I'm sorry."
        scene 82_s60 with dissolve
        alex "...No. I should be the one apologizing."
        alex "But... ugh. Forget it. Love isn't for me anyway."
        scene 82_s61 with dissolve
        mc "Alex. Don't say that."
        scene 82_s60 with dissolve
        alex "It's true, [mc]. I know what I am. An assassin. A tool. Not the girl you build a life with."
        scene 82_s61 with dissolve
        mc "Alex—"
        scene 82_s56 with dissolve
        alex "Forget it. Just... be more clear headed from now on, alright? We can't afford mistakes. Please."
        scene 82_s57 with dissolve
        mc "I'll try. What do you want me to do?"
    else:
        scene 82_s60 with dissolve
        alex "*sigh* I just need you be more clear headed from now."
        scene 82_s61 with dissolve
        mc "Yes, Ma'am!"
        scene 82_s60 with dissolve
        alex "Don't call me that..."
        scene 82_s61 with dissolve
        mc "What do you want me to do?"
    jump scene82_5

label scene82_5:
    scene 82_s58 with dissolve
    alex "There's a hunter's path near the main road. Patrols sometimes use it as a shortcut. If I can overhear their chatter..."
    alex "The thing is, [mc]. There's a rumor I heard... Avery might be moving to execute Princess Rebecca for treason."
    scene 82_s59 with dissolve
    mc "Treason?! When did you learn this?!"
    scene 82_s58 with dissolve
    alex "A day after Reham found you."
    scene 82_s59 with dissolve
    mc "Why didn't you tell me that!?"
    scene 82_s60 with dissolve
    alex "You were fighting for your life! And the girl for hers! What good would it have done to lay that on you?"
    alex "And it's still just a rumor."
    scene 82_s61 with dissolve
    mc "Dammit, Alex... No more secrets. I'm part of this now, for better or worse. Remember?"
    scene 82_s60 with dissolve
    alex "I'm sorry. You're right."
    scene 82_s61 with dissolve
    scene 82_s62 with Dissolve(1.5)
    mc "*sigh* She really wanted me gone."
    alex "It's not just about eliminating rivals. You're a living witness."
    mc "What about the Queen's son? Shouldn't he be the heir?"
    alex "By all rights, yes. But I'm sure my father and Avery have a plan for him, too. A convenient accident or something."
    mc "I still don't understand... Why go this far? Why this much blood?"
    alex "Power? Greed? *scoff* I can list a hundred things."
    mc "...Well. I'll keep watch for tonight. I still have my voice, like you said. I'll use it."
    alex "Yes. Take care, [mc]. I won't be long."
    alex "Oh, and the person who brought you here also brought Gaius's sword. Use it in case something happens."
    alex "I've hid it under the bed."
    mc "*chuckles* It's a good think I haven't lose my right hand."
    scene 82_s63 with Fade(1.0,1.0,1.0)
    env "A cold wind moves gently through the pines, carrying the soft rush of river water over smooth stones. Sunlight filters through the branches in pale golden bars, warming the garden without urgency, as if the world itself is holding its breath."
    stop music fadeout 2.0
    scene 82_s64 with Dissolve(3.0)
    play music "wind.mp3" fadein 1.0 loop
    ""
    play sound "sound_effects/doors/door_open2.mp3"
    scene 82_s65 with dissolve
    mc "Hmm?"
    scene 82_s66 with Dissolve(1.0)
    reham "Maia, please! Your body is not ready for this! You need to rest!"
    m "Staying on that mattress for one more minute is what's going to kill me! I need to feel the air!"
    scene 82_s67 with Dissolve(1.0)
    if mc_harem_reham:
        reham "Master, please! Reason with her! She can barely stand!"
    else:
        reham "[mc], please! Reason with her! She can barely stand!"
    scene 82_s68 with dissolve
    m "M-May I please have a few minutes outside, [mc]? I really want to breathe a little."
    scene 82_s70 with dissolve
    call screen scene82_choice10 with dissolve

label scene82_choice10_op1:
    mc "Maia, listen to her. She's kept you alive this long."
    scene 82_s68 with dissolve
    m "B-But-"
    scene 82_s70 with dissolve
    mc "No buts. We need you strong, not stubborn."
    m "..."
    scene 82_s69 with dissolve
    reham "Let's get you back inside. I'll keep the window open."
    scene 82_s70 with dissolve
    m "Tch..."
    scene 82_s71 with Fade(1.0,1.0,1.0)
    env "The river water nearby slides over smooth stones with a low, constant murmur, soft and gentle enough to lull even the cruelest beast to sleep."
    mc "(Fuck... I almost went to sleep. Not yet... Have to keep watch.)"
    jump scene82_7

label scene82_choice10_op2:
    $ mc_agree_maia_outside = True
    mc "A few minutes in the open air won't kill her. Let her be."
    scene 82_s68 with dissolve
    m "Thank you!"
    scene 82_s69 with dissolve
    reham "Just don't take too long, alright?"
    scene 82_s72 with Fade(1.3,1.0,1.0)
    perception "You lead Maia to The stone footbridge. River water slides past beneath, dark and glossy. Moonlight breaks on its surface in thin, trembling lines."
    mc "..."
    scene 82_s73 with dissolve
    if mc_harem_reham and not mc_maia_left:
        m "Umm... [mc]?"
        scene 82_s74 with dissolve
        mc "What's up?"
        scene 82_s73 with dissolve
        m "I... don't know if I misheard, but... I think I heard Reham call you 'master.'"
        scene 82_s74 with dissolve
        mc "*chuckles* Ah... yeah. You didn't mishear."
        if mc_maia_monogamous:
            if mc_harem_reham_dom or mc_harem_reham_dom_dom:
                $ mc_maia_mono_after_lie = True
                $ maia_love -= 10
                mc "I hired her. She'll stay with us, take care of things, of me... like that."
                scene 82_s73 with dissolve
                m "Oh... I see."
                m "Does that mean... everything?"
                scene 82_s74 with dissolve
                mc "Everything."
                scene 82_s73 with dissolve
                m "I... I thought maybe something like that might happen."
                m "She's so capable. And beautiful. I understand why you would want her."
                scene 82_s74 with dissolve
                mc "You okay with that?"
                scene 82_s73 with dissolve
                m "M-mhm. It makes me feel... warm. That someone like her wants to serve you too."
                scene 82_s76 with dissolve
                m "I just wish you'd told me earlier..."
                m "I got used to thinking I was... special. The only one."
                scene 82_s75 with dissolve
                empathy "Her voice wavers, not with anger but with the quiet ache of a broken promise. She's trying so hard to be strong for you."
                scene 82_s76 with dissolve
                if mc_maia_no_sex_real:
                    m "I know you told me you wanted to just be friends, but..."
                m "Do you... enjoy it? When she serves you?"
                scene 82_s75 with dissolve
                mc "Maia..."
                scene 82_s73 with dissolve
                m "I want to understand what makes you happy... even if it's not only me anymore."
                m "Just... let me still be yours too. Please."
                scene 82_s74 with dissolve
                mc "Always. You'll always be mine."
                scene 82_s73 with dissolve
                m "Um, I also wanted to ask..."

            else:
                $ maia_love += 10
                if maia_love > 100:
                    $ maia_love == 100
                mc "Don't worry, Maia. I hired her to take care of us. Including you. I promised to never touch her like that."
                scene 82_s73 with dissolve
                m "Really? You're not... with her?"
                scene 82_s74 with dissolve
                mc "No. It's a strictly professional relationship."
                scene 82_s73 with dissolve
                m "I see. I'm glad to know that I'm still your favorite."
                m "Umm, I also wanted to ask..."
        else:
            if mc_harem_reham_dom or mc_harem_reham_dom_dom:
                mc "I hired her. She'll be staying. Helping with... whatever I need."
                scene 82_s73 with dissolve
                m "Oh... alright."
                m "That makes sense. She's good at everything. And you... you deserve someone who can look after you properly."
                scene 82_s74 with dissolve
                mc "You okay with that?"
                scene 82_s73 with dissolve
                m "You told me you might be with others. I... I want to be fine with it. More than fine, even."
                m "Does she... make you feel good?"
                scene 82_s74 with dissolve
                if mc_sex_reham:
                    mc "She does."
                    scene 82_s73 with dissolve
                    m "Good. That's... that's good. I'm glad."
                else:
                    mc "I haven't slept with her yet."
                    scene 82_s73 with dissolve
                    m "I see..."
                m "Maybe one day... I could watch? If you wanted. Just to see you happy. And to know if she's doing it correctly."
                scene 82_s74 with dissolve
                mc "*chuckles* We'll see."
                scene 82_s73 with dissolve
                m "Alright. I'll... I'll look forward to it."
                m "I also wanted to ask..."
            else:
                mc "I hired her to take care of us. Including you. But I promised to never touch her like that."
                scene 82_s73 with dissolve
                m "Is that so?"
                scene 82_s74 with dissolve
                mc "Yes. But like I told you before, I'll still choose to be with other women."
                scene 82_s73 with dissolve
                m "Of course, [mc]. I already accepted that."
                m "You deserve a woman who can service you right."
                scene 82_s74 with dissolve
                mc "*chuckles* Good."
                scene 82_s73 with dissolve
                m "I also wanted to ask..."

    elif mc_harem_reham and mc_maia_left:
        m "Umm... [mc]?"
        scene 82_s74 with dissolve
        mc "What's up?"
        scene 82_s73 with dissolve
        m "I... don't know if I misheard, but... I think I heard Reham call you 'master.'"
        scene 82_s74 with dissolve
        mc "*chuckles* Ah... yeah. You didn't mishear."
        mc "I hired her. She'll stay with me, take care of things, of me... like that."
        scene 82_s73 with dissolve
        m "Oh, I see..."
        m "Did... did you two become... intimate?"
        scene 82_s74 with dissolve
        mc "Why do you ask?"
        scene 82_s73 with dissolve
        m "Just... curious. Old habits, I guess."
        m "I hope she takes good care of you. You deserve someone who knows how to serve you well."
        m "I also wanted to ask..."

    jump scene82_6

label scene82_6:
    scene 82_s73 with dissolve
    m "How have you been, [mc]? Really?"
    scene 82_s74 with dissolve
    mc "Hmm? Oh, you know. Fine. Aside from the whole... hand thing."
    scene 82_s73 with dissolve
    m "*sigh* I'm-"
    scene 82_s74 with dissolve
    mc "Stop. No more apologies. None of this is on you."
    mc "*chuckles* Besides, I'm practically over it now. You should see the cool prosthetic ideas I'm sketching in the dirt. A hook, a crossbow, maybe a built-in cannon..."
    scene 82_s73 with dissolve
    m "D-Does it... hurt?"
    scene 82_s74 with dissolve
    mc "Sometimes. Other times I forget it's gone. I'll try to lean on it or grab something. That's the weird part."
    m "..."
    mc "So, I learned Alex's story. But I still haven't heard yours. At least not the whole of it."
    scene 82_s75 with dissolve
    m "..."

    if maia_love >= 60:
        stop music fadeout 4.0
        $ mc_maia_story = True
        empathy "Her shoulders aren't drawn up to her ears anymore. The wary distance she used to keep has shrunk to nothing. She leans toward the sound of your voice. Whatever walls she had left, they're down."
        empathy "You have succeeded in making Maia trust you."
        play music "sad/maia4.mp3" fadein 8.0 loop
        mc "I can tell that you were a runaway. That Able was your master. But that's just it. I want to know the story."
        scene 82_s77 with Dissolve(2.0)
        m "I was... twelve. My family lived in a small village somewhere far, far away. I don't remember the name of it anymore. There was a raid. Not by soldiers, but by men like Able."
        m "They... they took anyone who could work. My parents... I never saw them again."
        m "Able bought me at a port market. I was cheap and so he bought me. I worked in one of his taverns. Scrubbing floors, washing dishes, carrying barrels twice my size."
        m "I ran away when I was sixteen. I just... ran. I didn't have a plan. I lived off stolen fruit and slept in alleys. I was caught by the guards for stealing."
        m "But then... Princess Rebecca was there. She saw me, crying and that small cell."
        m "She paid my fine and told the guards I was a new maid she'd personally hired, and brought me to the castle."
        mc "She saved you."
        m "Yes. And four years later you did. Again."
        m "I was so scared when I woke up and saw you... like that. I thought I'd lost you. Like my parents."
        mc "You're not going to lose me, Maia. I'm harder to get rid of than that."
        mc "And your past doesn't get to define you anymore. We're writing a new story now. For both of us."
        m "..."
        m "*chuckles* Mhm~"
        mc "Had enough fresh air?"
        m "Y-Yes."
        stop music fadeout 1.0
        mc "Good. Let me get you inside."
        play music "wind.mp3" fadein 1.0 loop
        m "Get me—?"
        scene 82_s78 with Dissolve(1.0)
        m "Hah!"
        m "[mc]... Your arm..."
        scene 82_s79 with dissolve
        mc "You thought I couldn't carry you with one hand?"
        mc "You're too light, you need to eat more."
        scene 82_s78 with dissolve
        m "...Mhm~"
        call screen scene82_choice11 with dissolve

    else:
        empathy "A cold, empathetic clarity hits you: you are still not trusted. The flinch is still in her, waiting. You broke her chains, you kept her alive, but comfort was a bridge too far."
        empathy "You have failed in making Maia trust you."
        scene 82_s76 with dissolve
        m "I-I'm sorry, [mc]... But I'd still rather not talk about it. I want to bury it away for good."
        scene 82_s75 with dissolve
        mc "Sometimes it's relieving to talk about it."
        m "..."
        mc "*sigh* Have it your way."
        mc "Do you want to go back inside now?"
        scene 82_s76 with dissolve
        m "Mhm. Thank you for letting me out, [mc]."
        scene 82_s75 with dissolve
        mc "*chuckles* You're easy to please."
        scene 82_s71 with Fade(1.4,1.0,1.0)
        ""
        stop music fadeout 1.0 
    jump scene82_7

label scene82_choice11_op1:
    play sound "sound_effects/slap03.mp3"
    scene 82_s81 with vpunch
    m "Ahhn!"
    scene 82_s80 with dissolve
    mc "This is for being a big dummy by listening to Avery and not telling me."
    scene 82_s81 with dissolve
    m "*giggles* I'm sorry, [mx]! I won't do it again!"
    scene 82_s80 with dissolve
    mc "Apology... accepted!"
    scene 82_s81 with dissolve
    m "*laughs*"
    scene 82_s71 with Fade(1.0,1.0,1.0)
    ""
    stop music fadeout 1.0 
    jump scene82_7

label scene82_choice11_op2:
    scene 82_s79 with dissolve
    mc "Let's get you inside. I want you to eat a lot and get healthy again."
    scene 82_s78 with dissolve
    m "Alright~"
    scene 82_s71 with Fade(1.0,1.0,1.0)
    ""
    stop music fadeout 1.0 
    jump scene82_7

label scene82_7:
    stop sound fadeout 1.0
    scene 82_s82 with Fade(1.5,1.0,1.4)
    play music "ambiance/river_water.mp3" fadein 1.0 loop
    ""
    scene 82_s83 with dissolve
    alex "[mc]!"
    scene 82_s84 with Dissolve(1.0)
    alex "*cough* I overheard some guards talking about a pair heading over to do another sweep of this area."
    alex "We can ambush them. They might have useful information."
    scene 82_s86 with dissolve
    mc "Take a breath. What's this about?"
    scene 82_s85 with dissolve
    alex "Two guards are coming to check this area. I heard it's only two of them."
    scene 82_s86 with dissolve
    mc "Two guards? That's it?"
    scene 82_s85 with dissolve
    alex "I'm guessing Avery is focusing on other areas at the moment."
    alex "Another large group was already here when you first woke up, so she probably thinks this area is cleared."
    scene 82_s86 with dissolve
    mc "Alright, what's the plan?"
    scene 82_s85 with dissolve
    alex "I'm glad you're onboard. We'll place some fallen trees on the road. When they get off their horses to clear it, we jump them."
    alex "I have my crossbow that I... acquired. They won't see it coming."
    scene 82_s86 with dissolve
    mc "What about me? How am I useful here?"
    scene 82_s85 with dissolve
    alex "You have Gaius's sword, remember? Use it to look... intimidating. It'll be easier for them to surrender if they see more of us."
    scene 82_s86 with dissolve
    mc "*chuckles* I'm guessing you didn't put much effort into this."
    scene 82_s87 with dissolve
    alex "It's the best I could come up with our current resources."
    scene 82_s88 with dissolve
    mc "What happens after we question them?"
    scene 82_s85 with dissolve
    alex "I haven't thought that far ahead... They should arrive soon. We have to hurry, the road isn't far from here."
    scene 82_s86 with dissolve
    mc "What about here? Shouldn't we have someone keep watch?"
    scene 82_s85 with dissolve
    alex "Reham will take care of that. She's knows what to do if someone arrives."
    scene 82_s86 with dissolve
    mc "Hopefully that's enough. Let's go then."

label scene83:
    stop music fadeout 1.0
    scene 83_s1 with Fade(1.5,1.0,1.0)
    play music "wind2.mp3" fadein 1.0 volume 0.55 loop
    mc "It's windy up here."
    alex "This is the place. Help me block the road."
    scene black with Fade(0.5,0.5,0.5)
    play sound "sound_effects/falling_tree.mp3" volume 0.7
    pause(2.0)
    scene 83_s2 with Fade(0.5,0.5,0.5)
    alex "Phew... Alright, this should be good enough. Let's hide in the bushes over there."
    scene 83_s6 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/horse/horse_walk.mp3"
    ""
    scene 83_s3 with Dissolve(1.0)
    guard "What in the...?"
    guard "Did a tree fall over? Great. Just great."
    scene 83_s4 with dissolve
    joan "I-I don't like this, Lewis! Should we head back? This feels like an ambush!"
    scene 83_s5 with dissolve
    lewis "*sigh* Gods... they just had to pair me with you. It's probably just the wind from that storm."
    lewis "Get off and help me clear it out."
    stop music fadeout 1.0
    scene 83_s7 with Dissolve(1.7)
    alex "{size=30}Now!{/size}"
    play music "tense/capture.mp3" fadein 1.0 loop
    scene 83_s8 with vpunch
    alex "Drop your weapons! On the floor now!"
    scene 83_s9 with dissolve
    joan "Ahh! Bandits!"
    scene 83_s10 with dissolve
    lewis "Shit! W-Wait... These are the fugitives! The ones from the posters!"
    scene 83_s8 with dissolve
    alex "One move and I'll put a bolt right between your eyes. I don't miss."
    scene 83_s9 with dissolve
    joan "A-Alright! Alright! Please don't shoot!"
    play sound "sound_effects/bodydrop4.mp3"
    scene 83_s12 with dissolve
    lewis "..."
    scene 83_s11 with dissolve
    joan "P-Please don't kill me! My mother is sick and-"
    alex "Shut up!"
    joan "A-And my father is too old to provide for us, it's the only reason I joined the guar-"
    alex "I said shut up!"
    scene 83_s16 with dissolve
    mc "What's going on in the city? What's Avery planning with the princess?"
    scene 83_s15 with dissolve
    lewis "Screw you! Traitor! We're not talking!"
    scene 83_s13 with dissolve
    mc "Figured it would be too easy. Oh well... guess we'll just have to wait for the next group of guards coming to look for you."
    scene 83_s16 with dissolve
    lewis "..."
    scene 83_s14 with dissolve
    joan "Queen Avery wants to execute the princess! She's holding a private execution in three weeks at dawn! That's what the rumours say, it's all I know! Please!"
    scene 83_s16 with dissolve
    mc "..."
    scene 83_s18 with dissolve
    lewis "You {i}idiot.{/i} Now they have no reason to keep us alive."
    scene 83_s17 with dissolve
    joan "W-W-What?!"
    scene 83_s16 with dissolve
    alex "No. There's still more. What else is she planning? Why the public execution? And what about the Queen's son?"
    scene 83_s15 with dissolve
    lewis "We're not sayi-"
    scene 83_s19 with dissolve
    joan "She's using the execution as a show of power! To prove that the current council is incompetent and that she's the only one who can bring order!"
    joan "She's also saying that the princess was involved with you, [mc], in treasonous plots!"
    scene 83_s21 with dissolve
    mc "And the prince? The Queen's son?"
    scene 83_s19 with dissolve
    joan "P-Prince Liam? She's keeping him under house arrest! She says it's for his safety, but everyone knows she's controlling him!"
    joan "She declared herself queen until he becomes of age, but... I think she might... you know..."
    scene 83_s20 with dissolve
    lewis "Joan, shut your fucking mouth!"
    scene 83_s19 with dissolve
    joan "She's also letting Eurinian soldiers into the city! Hundreds! They answer only to her!"
    scene 83_s21 with dissolve
    mc "This is worse than we thought. She's moving fast."
    alex "What about the patrol routes? How many men are we looking at around the city?"
    scene 83_s19 with dissolve
    joan "They don't tell us that, I swear! Just please, let us go!"
    scene 83_s20 with dissolve
    lewis "If we survive this, Joan, I'm killing you myself."
    scene 83_s16 with dissolve
    alex "This is good. Very good."
    if mc_accept_joan:
        scene 83_s14 with dissolve
        joan "Sir, [mc]! You promised to train me? Remember? You thought I had potential, please!"
        scene 83_s16 with dissolve
        mc "Different times, Joan."
    scene 83_s23 with Dissolve(1.0)
    mc "What do we do with them now? Can we even let them go?"
    mc "Should we... kill them?"
    scene 83_s24 with dissolve
    joan "H-Hahn!?"
    lewis "*gulp*..."
    scene 83_s23 with dissolve
    mc "Calm down. I was joking. Mostly."
    scene 83_s22 with dissolve
    alex "We should have them to join us."
    scene 83_s25 with Dissolve(1.0)
    reham "No. Absolutely not. We are not letting anyone {i}join{/i} us. We're not building an army here."
    scene 83_s26 with Dissolve(1.0)
    alex "R-Reham? What the hell are you doing here?"
    scene 83_s27 with dissolve
    reham "I followed you. I don't want you to do anything we'll all regret."
    scene 83_s26 with dissolve
    mc "You left Maia alone!?"
    scene 83_s28 with dissolve
    reham "She's fine. She's much safer than all of us right now."
    scene 83_s29 with dissolve
    alex "And why exactly should we turn them away?"
    scene 83_s30 with dissolve
    reham "Because the plan is to reach King Hod in Nahraya clean and quiet. If he believes us, he can halt Rebecca's execution with one letter. We don't need soldiers."
    scene 83_s29 with dissolve
    alex "And if he doesn't believe a handful of fugitives walking in off the road? We show up empty-handed, he sends us away, and the princess dies anyway."
    alex "But if we have the Queen's daughter alive at our side, Hod will have to listen. No king ignores a living heir begging for justice."
    scene 83_s30 with dissolve
    reham "So you'd gamble all our lives on a prison break that could fail tomorrow? One letter from Hod could buy her months, time for Nueleth to hear the truth properly."
    scene 83_s29 with dissolve
    alex "*scoff* You're insane if you think we'll reach Nahraya, convince a king, and get that letter sent before the axe falls."
    alex "The journey south is long. Bandits, patrols, the desert itself. More swords could mean we actually get there."
    scene 83_s30 with dissolve
    reham "Every person we add is another tongue that can sell us for a pardon. These two swore oaths to Avery's coin."
    scene 83_s32 with dissolve
    joan "I... I never wanted—"
    scene 83_s31 with dissolve
    reham "Spare me, girl."
    scene 83_s29 with dissolve
    alex "People switch sides all the time. They've seen what happens to loose ends. We can use that."
    scene 83_s30 with dissolve
    reham "Or they wait until we sleep, slit our throats, and ride back for their bounty."
    scene 83_s33 with dissolve
    alex "[mc], think. We have a far better chance with Hod if we bring him Rebecca herself. And a far better chance of surviving the road with numbers."
    if mc_save_queen:
        alex "And try to imagine what the Queen would say if we didn't rescue her daughter."
    scene 83_s34 with Dissolve(1.0)
    if mc_harem_reham:
        reham "Master, listen. Every ally is a risk we can't control. We travel small, we travel fast, we reach king Hod before the execution. One letter, one command from a king can save her without spilling a drop of our blood."
    else:
        reham "[mc], listen. Every ally is a risk we can't control. We travel small, we travel fast, we reach king Hod before the execution. One letter, one command from a king can save her without spilling a drop of our blood."
    reham "Besides, if things go sour with rescuing the princess and many lose their lives because of us, it will hurt our reputation badly."
    if mc_save_queen:
        reham "A Ruler shouldn't think emotionally. The Queen would perfectly understand why we didn't rescue her daughter."
    scene 83_s35 with vpunch
    alex "[mc]!"
    scene 83_s35 with vpunch
    reham "[mc]!"
    scene 83_s36 with dissolve
    mc "Shut up! Both of you."
    scene 83_s37 with Dissolve(1.8)
    call screen scene83_choice01 with dissolve

label scene83_choice01_op2:
    stop music fadeout 1.0
    $ mc_princess_reham = True
    scene 83_s38 with dissolve
    mc "Reham's right. We can rescue the princess without a risky prison break."
    play music "wind.mp3" fadein 1.0 loop
    scene 83_s39 with dissolve
    reham "Thank you, [mc]. That's the smart choice. The only one that keeps us breathing long enough to matter."
    scene 83_s40 with dissolve
    alex "...You're serious. You're just going to miss this opportunity?"
    scene 83_s41 with dissolve
    mc "Alex—"
    alex "Screw this. I'm leaving. Deal with this yourselves."
    scene 83_s42 with dissolve
    reham "Let her go. Anger's loud, but it burns out. She'll come back to her senses eventually."
    scene 83_s43 with dissolve
    mc "...I hope you're right."
    mc "So what now? We can't kill them or more guards will come searching."
    scene 83_s42 with dissolve
    reham "There's a merchant road an hour east, our caravan passed it back when we were heading for Irda. We march them there blind, tie them securely to a tree just off the path."
    reham "Someone will find them. Traders, hunters, patrols even. They'll be questioned, maybe punished for losing us, but alive."
    scene 83_s43 with dissolve
    mc "You're sure the road's busy enough? It's pretty cold out here."
    scene 83_s42 with dissolve
    reham "Someone should stumble on them within a day or two. Long enough for us to think of something, short enough they won't freeze or starve."
    scene 83_s43 with dissolve
    mc "Alright. It's cold, but it's clean. No blood on our hands."
    scene 83_s39 with dissolve
    reham "Exactly. We stay human. That's how we win in the end."
    scene 83_s38 with dissolve
    scene 83_s44 with dissolve
    mc "Hands behind your back. We're going on a journey."
    joan "Thank you, Sir [mc], for not hurting us! We promise not to tell anyone about this!"
    stop music fadeout 1.0
    scene 83_s54 with Fade(1.5,1.2,1.3)
    play music "ambiance/river_water.mp3" fadein 1.0 volume 0.5 loop
    mc "I wanted to ask, Reham. This place doesn't look abandoned. Not at all."
    reham "You're right. Someone kept it up. Roof patched, hearth swept. They're probably just away for the season."
    reham "Actually... I've been wondering if this shed belongs to whoever dragged you and Maia here through the storm."
    mc "You think?"
    reham "It fits. They knew exactly where to bring you. Maybe they're the owner, checking on us from a distance."
    mc "Well... hopefully they don't mind us squatting a little longer."
    stop music fadeout 1.0
    scene black with Fade(1.0,1.2,1.3)
    play sound "sound_effects/doors/door_open2.mp3"
    scene 84_s76 with Fade(0.5,0.5,0.5)
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    m "[mc]? What happened? Reham left in such a hurry and miss Alex is really angry at something."
    scene 84_s77 with dissolve
    mc "We caught a couple of guards and got some news from the capital."
    scene 84_s76 with dissolve
    m "Any good ones?"
    scene 84_s77 with dissolve
    mc "Afraid not. They're... planning to execute the princess. Publicly."
    scene 84_s78 with dissolve
    m "W-What!? No!"
    scene 84_s79 with dissolve
    mc "It's awful. But there's nothing we can do right now, we'll have to ask the king of Nahraya to intervene before it happens."
    scene 84_s78 with dissolve
    m "Oh, princess... She must be so afraid... all alone..."
    scene 84_s79 with dissolve
    mc "*sigh* I know."
    scene 84_s78 with dissolve
    m "Can we really not help her now?"
    scene 84_s79 with dissolve
    alex "We could have—"
    mc "Stop it, Alex. We couldn't. Not without risking everyone here. That's final."
    m "..."
    scene 84_s78 with dissolve
    m "*whimper* ...If you say so, [mc]. I trust your judgment."
    scene 84_s79 with dissolve
    mc "Now that we know what's happening, let's make a real plan."
    scene 84_s80 with dissolve
    reham "I'm listening."
    scene 84_s84 with dissolve
    mc "Reham, you said we can get an audience without Rebecca at our side. How can we do that?"
    scene 84_s80 with dissolve
    reham "I... don't have every detail yet. I spoke in the heat of the moment."
    scene 84_s84 with dissolve
    alex "*scoff* Great."
    scene 84_s80 with dissolve
    reham "But the idea isn't hopeless. King Hod despises falsehood above all else."
    if mc_save_queen:
        reham "And... this is rarely spoken of, out of respect, but after her husband's passing, Queen Hannah and King Hod were once close. His affection for her has endured, even after they parted."
        reham "If we can get word to the Queen, she might be able to send a token or a message that would move him to act."
        reham "But even without that, the truth of Avery's treason and the attack on the Queen and princess should be enough."

    else:
        reham "And... few speak of it now, out of respect, but Queen Hannah was once his lover after her husband died. He carried deep affection for her, even after they parted."
    
    scene 84_s84 with dissolve
    mc "So you think he would act for her sake?"
    scene 84_s80 with dissolve

    if mc_save_queen:
        reham "For her, and for justice. Knowing that Queen Hannah lives, and that her daughter is in peril, would stir him to action."
    else:
        reham "For her memory, and for justice. If we present him with undeniable proof of Avery's treason and the attack on the royal family, he will not remain neutral."

    reham "He could summon Nueleth south under diplomatic seal, or at the very least send a command delaying Rebecca's execution until the truth is examined."
    scene 84_s81 with dissolve
    alex "Or he takes it as a personal insult and starts a war we'll all bleed for."
    reham "...A risk. But calculated. King Hod is cautious with his armies. He'd rather force clarity than fight blindly."
    mc "It's definitely safer than storming the capital with a handful of us."
    mc "Fine. We'll do it your way, Reham. Straight to Nahraya."
    reham "Thank you."
    scene 84_s82 with vpunch
    alex "[mc]!"
    scene 84_s83 with dissolve
    mc "You've been pushing reckless ideas since I woke up. It's starting to feel childish."
    scene 84_s82 with dissolve
    alex "Me? Childish? I'm trying to save the princess before it's too late!"
    scene 84_s83 with dissolve
    mc "And I'm trying to keep us alive long enough to matter. We'll save her, I promise. But we do it smart."
    scene 84_s82 with dissolve
    alex "It's not just about saving her! It's about proof! Marching into Hod's palace with the rightful heir, alive and free? That's not a story, that's irrefutable truth. We win in one move."
    if mc_save_queen:
        alex "There's simply no guarantee that we might be able to reach the Queen in time and have her send a letter to Hod."
    scene 84_s83 with dissolve
    mc "I know what you mean. But the risk is too high right now. Someone or maybe all of us gets caught or killed, and then Rebecca dies anyway. As Reham said."
    mc "And I know you're scared for your brother. But fear doesn't justify throwing lives away. We'll get him back. I swear it."
    alex "..."
    scene 84_s82 with dissolve
    alex "*sigh* ...Fine. For now."
    scene 84_s83 with dissolve
    scene 84_s84 with dissolve
    mc "Good. We're not riding south tomorrow. There are things we need first."
    mc "I've been thinking about Yuuhi, the tailor who helped craft my magic-resistant armor."
    scene 84_s80 with dissolve
    reham "Armor? But we agreed to do this quietly. No fighting. What use would new armor be?"
    scene 84_s84 with dissolve
    mc "No, not armor. A prosthetic for my hand."
    scene 84_s80 with dissolve
    if mc_harem_reham:
        reham "Master... no one here sees you as less because of it. You don't need to hide or compensate."
    else:
        reham "[mc]... no one here sees you as less because of it. You don't need to hide or compensate."
    scene 84_s84 with dissolve
    mc "*chuckles* It's not insecurity. I want something functional. Imagine a prosthetic built by a master smith's daughter. A hidden blade in the wrist. A cannon. A small shield. No one would see it coming."
    scene 84_s76 with dissolve
    m "Is it safe to go back there, [mc]?"
    scene 84_s77 with dissolve
    mc "It's just an idea for now. We'll see."
    scene 84_s83 with dissolve

    if not mc_execute_kat and not mc_life_kat:
        mc "And Alex, Kathrine's still out there, hiding. She saw everything, her testimony could help us a lot."
        mc "That's your task. Find her and bring her to us safely. You know best how to be stealthy."
        scene 84_s82 with dissolve
        alex "...Alright. I can do that."
    else:
        scene 84_s83 with dissolve
        mc "Alex, keep watch over the area. Protect Reham and Maia whenever I'm gone."
        scene 84_s82 with dissolve
        alex "..Understood."

    scene 84_s84 with dissolve
    mc "And since we're blind out here. We need eyes inside the city. There's this woman, Diana. She works at a brothel called the Slick Worm near the capital. Perfect place for rumors."
    scene 84_s80 with dissolve
    reham "A brothel?"
    scene 84_s84 with dissolve
    mc "She could feed us information. Gossip, anything useful."
    if mc_harem_diana or mc_friend_diana:
        mc "She's planning to buy the brothel. If we can help her secure it, we migh have leverage over potentially important clients as they're more likely to visit a regular tavern rather than a brothel."
    scene 84_s80 with dissolve
    if mc_harem_reham:
        reham "I don't know, master... Do you really trust someone like that?"
    else:
        reham "I don't know, [mc]... Do you really trust someone like that?"
    scene 84_s84 with dissolve
    alex "Not a bad idea. Information is worth more than gold right now."
    mc "Alex agrees with me. We'll approach her carefully, nothing guaranteed, but it's a start."
    mc "Finally, Reham. You're our foundation. You keep this place running. Tend to Maia, secure our supplies, and be our lookout."
    mc "You're the reason we're still alive to make this plan."
    scene 84_s80 with dissolve
    reham "I'll hold the line."
    scene 84_s84 with dissolve
    mc "Is everyone re-"
    play sound "sound_effects/Dooropen.mp3"
    pause(0.3)
    scene 84_s85 with dissolve
    mc "Maia?"
    reham "Maia! Where you going?"
    m "Outside."
    scene 84_s86 with Dissolve(1.0)
    mc "*sigh* I'll go see what's wrong."
    $ mc_went_sad_maia = True
    reham "Please."
    jump scene84

label scene83_choice01_op1:
    stop music fadeout 1.0
    mc "..."
    play music "hope/hope.mp3" fadein 2.0 loop
    $ mc_princess_alex = True
    scene 83_s45 with dissolve
    mc "I'll ask you this, and your lives depend on your answer. Who does your loyalty lie with?"
    scene 83_s46 with dissolve
    lewis "Huh?"
    scene 83_s45 with dissolve
    mc "Who does your loyalty belong to? The true crown of Irda or Avery?"
    scene 83_s47 with Dissolve(1.0)
    joan "I... I don't..."
    scene 83_s48 with dissolve
    if mc_save_queen:
        mc "The Queen you swore to protect has been forced into hiding. Her daughter is waiting to be executed. Her son is a prisoner in his own home. Where does your oath lead you now?"
    else:
        mc "The Queen you served is dead. Her daughter is waiting to be executed. Her son is a prisoner in his own home. Where does your oath lead you now?"
    scene 83_s46 with Dissolve(1.0)
    lewis "T-The Queen! Always Her Majesty!"
    scene 83_s47 with dissolve
    joan "Y-Yes! Lady Avery has been... disrespectful. The things she's been saying—"
    scene 83_s48 with dissolve
    mc "What things?"
    scene 83_s47 with dissolve
    joan "That the Queen was weak! That she deserved what happened! But Queen Hannah was good to the people! She cared about the smallfolk!"
    scene 83_s46 with Dissolve(1.0)
    lewis "The execution order for Princess Rebecca... it's wrong. Many of us feel it, but no one dares speak up."
    lewis "Avery's brought in foreign mercenaries who answer only to her. They're watching us as much as they're watching for you."
    scene 83_s45 with dissolve
    mc "Then I'll offer you something Avery can't. A chance to redeem that feeling in your hearts. Prove your loyalty isn't just a memory, but a living fire."
    scene 83_s46 with dissolve
    joan "P-Prove it how?"
    scene 83_s48 with Dissolve(1.0)
    mc "Stand with us. Not as prisoners, but as the first true soldiers of Irda's revolution. Help us take her down."
    scene 83_s49 with Dissolve(1.0)
    reham "[mc], please! Why are you doing this?"
    scene 83_s50 with dissolve
    mc "They have been serving a lie. A good soldier follows orders. A great soldier knows when to question them."
    if mc_save_queen:
        mc "Avery tried to murder her own sister. The 'accident at sea' was a cover for an assassination that failed."
    else:
        mc "Avery lied to you. Queen Hannah didn't die at sea. She was murdered by her own sister."
    scene 83_s47 with Dissolve(1.0)
    if mc_save_queen:
        joan "S-She tried to kill her sister? But how? She didn't leave the city."
    else:
        joan "S-She killed her sister? But how? She didn't leave the city."
    scene 83_s51 with dissolve
    mc "The order came from Avery and Reiner of Eurina. And the blade was meant to be wielded..."
    mc "...by her."
    alex "..."

    if mc_save_queen:
        lewis "She was chosen to do it?"
    else:
        lewis "She did it!? The assassin is right here!?"
    
    if mc_save_queen:
        mc "She was. With her brother's life held hostage. They forced her hand... but when the moment came, she chose mercy. She chose to save the Queen instead."
        mc "Her failure to kill is what gives us this chance."
    else:
        mc "Yes. With a knife at her own brother's throat. Avery and Reiner forced her hand. Now, she wants to atone by exposing the truth."
        mc "Her sin was being a pawn. Ours would be to do nothing."

    scene 83_s46 with Dissolve(1.0)
    lewis "And if we are caught?"
    scene 83_s45 with dissolve
    mc "Then you will die as martyrs for the true Irda, and your names will be remembered for generations."
    mc "Or you can live in shame, watching your kingdom become unrecognizable. This is your moment. Choose what you will be."
    scene 83_s47 with dissolve
    joan "I-I choose to be a soldier for Queen Hannah! For the Princess!"
    lewis "..."
    scene 83_s46 with dissolve
    lewis "*sigh* This... this ends now. My sword is yours."
    scene 83_s51 with dissolve
    if mc_save_queen:
        lewis "And you... It takes more courage to spare a life than to take one. Maybe there's hope for you yet."
    else:
        lewis "But you. I don't think I can ever forgive you."
    alex "..."
    scene 83_s52 with dissolve
    mc "Take my hand. You two will be the spark that will light the fire of revolution."
    mc "We will rescue the Princess. And when the people see their queen's daughter freed by the 'traitors' Avery vilifies, every soul in Irda with a shred of conscience will flock to us."
    scene 83_s53 with Fade(0.5,0.5,0.5)
    reham "[mc]... This isn't a mission to reveal the truth anymore, you might start a war."
    mc "I'm finishing what Avery started."
    reham "..."
    stop music fadeout 2.5
    scene 83_s54 with Fade(1.5,1.0,1.4)
    play music "ambiance/river_water.mp3" fadein 1.0 volume 0.5 loop
    lewis "Wait, is this where you've been holding up? This... shack?"
    mc "We're just starting."
    joan "I like it. Looks cozy."
    lewis "Nobody asked you."
    mc "Actually, I forgot to ask, Alex, this place doesn't look abandoned. Not at all."
    alex "It was rougher when Reham and I found it. But you're right... someone's been keeping it up."
    alex "I assume the owner is just away from some time."
    mc "Hopefully they don't mind us squatting here for a while."
    stop music fadeout 1.0
    scene black with Fade(1.0,1.2,1.3)
    play sound "sound_effects/doors/door_open2.mp3"
    scene 83_s55 with Fade(0.5,0.5,0.5)
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    lewis "Ah, man... is this it? We're just... one, two..."
    lewis "Four women and two men, one of whom is missing a hand? This is the army that's going to rescue the princess?"
    scene 83_s56 with dissolve
    m "Umm... [mc]? Who are these people?"
    scene 83_s57 with dissolve
    joan "Hello. Thank you for having us."
    scene 83_s58 with dissolve
    m "H-Hey..."
    scene 83_s59 with dissolve
    mc "They've sworn to the true crown. They're going to help us get Becky back."
    scene 83_s60 with dissolve
    m "Is the Princess in danger!?"
    scene 83_s61 with dissolve
    reham "*sigh* Since you're all apparently committed to madness... would you like some soup? There's plenty left."
    scene 83_s62 with dissolve
    joan "N-No thanks."
    scene 83_s63 with dissolve
    reham "Maia, you haven't had more than two bites. It's still almost full. I told you to eat more."
    scene 83_s62 with dissolve
    m "It... doesn't taste good..."
    scene 83_s63 with dissolve
    reham "There won't be palace kitchens or royal chefs for a long while. You're going to have to get used to it."
    scene 83_s62 with dissolve
    m "A-Alright."
    scene 83_s64 with dissolve
    lewis "*sigh* How do we even start? We have no weapons, no numbers, no strate—"
    scene 83_s65 with dissolve
    mc "Stop looking at what we're lacking. We're already at the bottom, which means every move we make is up."
    mc "We start now. With a plan."
    mc "Lewis. Joan. You're our connection to the inside. Your first mission: go back to your posts like nothing happened."
    mc "Lewis, you've got the sharper tongue. Your job is to find the guards who grumble about the Nahrayan mercenaries, the ones who loved the Queen. Sound them out. Carefully."
    mc "Joan, your earnestness is your weapon. People trust you. I need you to listen. Eavesdrop on the high ranking guards and learn their routines, their patrol patterns."
    scene 83_s66 with dissolve
    lewis "We can do that."
    scene 83_s67 with dissolve
    joan "I... I won't let you down."
    scene 83_s68 with dissolve
    mc "Alex. You're our shadow. Learn where they plan to execute the princess. Find me a point of entry that isn't watched."
    if not mc_life_kat and not mc_execute_kat:
        mc "And Kathrine, she's still out there, hiding. Avery will hunt her. We'll find Kathrine right after the princess."
    scene 83_s69 with dissolve
    alex "Thanks for not giving me a job that involves babysitting."
    scene 83_s68 with dissolve
    reham "Hey!"
    scene 83_s70 with dissolve
    mc "Reham. You're our foundation. You keep this place running. Tend to Maia, secure our supplies, and be our lookout. You're the reason we're all still alive to make this plan."
    reham "..."
    mc "Please, Reham. We're doing this."
    scene 83_s71 with dissolve
    reham "*sigh* I can't stop a river once it's moving. Just... don't make me regret it."
    if mc_harem_reham:
        reham "You're also my master now so I can't really deny you."
    scene 83_s70 with dissolve
    m "Hmph..."
    scene 83_s72 with dissolve
    mc "Once we learn the patrol routes and a way in—"
    scene 83_s73 with dissolve
    reham "Maia?"
    play sound "sound_effects/Dooropen.mp3"
    pause(0.3)
    scene 83_s74 with dissolve
    reham "Hey! Where are you going?"
    m "...Outside."
    scene 83_s76 with Dissolve(1.0)
    alex "Should I get her?"
    scene 83_s75 with dissolve
    mc "Stay. I'll go see what's wrong."
    $ mc_went_sad_maia = True
    jump scene84

    
label scene83_choice02_op1:
    $ mc_went_sad_maia = True
    mc "Stay. I'll go see what's wrong."
    jump scene84

label scene83_choice02_op2:
    mc "Get her, Alex."
    scene 83_s76 with dissolve
    alex "Alright."
    scene 83_s75 with dissolve
    mc "Don't be too rough on her."
    scene 83_s76 with dissolve
    alex "Sheesh, who do you take me for?"
    scene 83_s75 with dissolve
    scene 83_s72 with dissolve
    mc "Any questions?"
    jump scene84_4

label scene84:
    stop music fadeout 1.0
    scene 84_s1 with Fade(1.4,1.0,1.4)
    play music "ambiance/river_water.mp3" fadein 1.0 volume 0.75 loop
    mc "Maia? Why'd you leave?"
    scene 84_s2 with dissolve
    if mc_princess_reham:
        m "...You gave everyone a role but me."
        m "I don't have anything to do... I'm just a burden."
        m "Alex can fight."
        m "Reham has experiance as a healer and she can cook."
        m "But me... I'm just the weak one who needs to be protected. The one you have to worry about. I can't do anything. I-I'm just... here."
    else:
        m "...You gave everyone a role but me."
        m "I don't have anything to do... I'm just a burden."
        m "The others and Alex can fight."
        m "Reham has experiance as a healer and she can cook."
        m "But me... I'm just the weak one who needs to be protected. The one you have to worry about. I can't do anything. I-I'm just... here."
    scene 84_s1 with dissolve
    call screen scene84_choice01 with dissolve

label scene84_choice01_op1:
    $ mc_console_maia = True
    if maia_sad:
        $ maia_sad = False

    stop music fadeout 1.0
    mc "Stop that."
    play music "hope/rose_of_may.mp3" fadein 1.0
    mc "Listen to me. You are not a burden. You are the reason."
    scene 84_s4 with Dissolve(0.8)
    mc "When you were in that cellar, it wasn't thoughts of vengeance that drove me. It was you."
    mc "When Gaius took my hand and I was bleeding out, it was the memory of your smile that kept me from fainting."
    mc "Everyone else has a job to do. But you... you have a purpose. Your purpose is to be the heart of this. To be the good we're fighting for. To remind me why this is all worth it when the doubt closes in."

    if not mc_maia_left:
        if mc_princess_reham:
            mc "Alex has her crossbow, Reham her herbs. But you... you have my heart. And that is the most important thing I have."
            mc "So don't you ever think you don't have a role. You are the foundation of it all."
            m "..."
        else:
            mc "Alex has her crossbow, Reham her herbs, Lewis and Joan have their swords. But you... you have my heart."
            mc "And that is the most important thing I have. So don't you ever think you don't have a role. You are the foundation of it all."
            m "..."
        jump scene84_2

    elif mc_maia_left:
        m "..."
        mc "So, don't ever tell me you aren't helping. You are. Just by being by my side, you are."
        scene 84_s5 with dissolve
        m "Umm... [mc]. Can I ask you something? About... back then. When the Queen separated us."
        m "Were you fine with it?"
        scene 84_s4 with dissolve
        mc "What do you mean?"
        scene 84_s5 with dissolve
        m "I mean... it felt like everything was just starting. And then it was just... taken away."
        m "Should we... try again? I really want to. I never stopped wanting to."
        scene 84_s4 with dissolve
        call screen scene84_choice02 with dissolve

label scene84_choice02_op2:
    $ maia_love += 10
    if maia_love >= 50:
        if not maia_happy:
            $ maia_happy = True

    $ mc_maia_left_return = True

    mc "That sounds nice, Maia."
    scene 84_s5 with dissolve
    m "R-Really? You mean it?"
    scene 84_s4 with dissolve
    mc "Mhm. Let's try that again."
    mc "And this time, I promise I won't try to take your pet away from you..."
    scene 84_s7 with dissolve
    m "Oh... Crumps. I really hope he's doing well. I miss his cute little face."
    scene 84_s6 with dissolve
    mc "When this is all over, he'll be the first thing we get back. What do you say?"
    scene 84_s4 with dissolve
    m "..."
    if maia_happy:
        jump scene84_2
    else:
        scene 84_s5 with dissolve
        m "Thank you, [mc]. I-I'll hold you to that."
        scene 84_s4 with dissolve
        mc "*chuckles* Alright, should we head back now?"
        scene 84_s5 with dissolve
        m "Yes."
        scene 84_s4 with dissolve
        jump scene84_4

label scene84_choice02_op1:
    $ mc_maia_left_twice = True
    $ maia_happy = False
    mc "Maia... I'm sorry."
    mc "But I prefer things to stay the way they are."
    scene 84_s6 with dissolve
    mc "We didn't fit each other. It wasn't love, it was duty."
    scene 84_s7 with dissolve
    m "I-"
    scene 84_s6 with dissolve
    mc "You are, and will always be precious to me. I will protect you. But as a friend, as family. Not as a lover."
    scene 84_s5 with dissolve
    m "I understand."
    scene 84_s4 with dissolve
    mc "Should we go back inside?"
    scene 84_s5 with dissolve
    m "Yes."
    scene 84_s4 with dissolve
    jump scene84_4

label scene84_choice01_op2:
    mc "Maia, now is not the time for this. We have a princess to save."
    mc "If you need a task, I'll find you one. You can help Reham sort supplies. Or keep watch. There's always something that needs doing."
    mc "But you need to understand that right now, the most useful thing you can do is stay out of the way and get stronger."
    scene 84_s2 with dissolve
    m "...I see. Of course. I'll... I'll go help Reham then."
    scene 84_s1 with dissolve
    scene 84_s3 with Dissolve(1.4)
    m "I won't get in the way."
    jump scene84_4

label scene84_2:
    if mc_maia_mono_after_lie:
        $ mc_maia_mono_after_lie_apologize = True
        $ mc_maia_monogamous = False
        $ maia_love += 20
        scene 84_s5 with dissolve
        m "And?"
        scene 84_s4 with dissolve
        mc "And...?"
        m "..."
        mc "Oh!"
        mc "Maia... I'm so sorry."
        mc "I lied to you. I told you you'd be the only one. And I knew, even then, that I couldn't keep that promise."
        mc "I should have been honest from the start. You deserved the truth, not a pretty lie to make the moment easier."
        m "..."
        mc "I was selfish. I didn't want to see you hurt, so I avoided it and ended up hurting you worse."
        mc "I wanted others... but that's on me. My weakness, my greed. Not yours."
        mc "But I won't lie to you again. Ever. You deserve better than that."
    
    if maia_love >= 50:
        if not maia_happy:
            $ maia_happy = True
            
    scene 84_s8 with Dissolve(0.3)
    play sound "se_sfx/blowjob/kiss5.mp3" 
    scene 84_s8 with vpunch
    mc "M-Maia-?"
    scene 84_s9 with dissolve
    m "*mwah* [mc]... You say these things so earnestly... It makes my heart flutter~ It makes me feel... wanted."
    scene 84_s10 with dissolve
    mc "*chuckles* I'm only telling you the truth."
    if mc_maia_mono_after_lie_apologize:
        scene 84_s12 with dissolve
        m "*giggles* And... apology accepted!"
        m "I realize now that someone like you should have all the happiness in the world!"
        scene 84_s11 with dissolve
        mc "My... Thank you."
    if mc_maia_no_sex_real:
        scene 84_s12 with dissolve
        m "I know you told me we're just... friends. But friends can care for each other like this, too, r-right?"
        scene 84_s11 with dissolve
        call screen scene84_choice03 with dissolve
    else:
        scene 84_s9 with dissolve
        m "I need you... now. Please. I need to feel something other than fear. I want your touch, [mc]."
        scene 84_s10 with dissolve
        call screen scene84_choice03 with dissolve

label scene84_choice03_op1:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p7_replay:
        $ persistent.scene1_p7_replay = True

    stop music fadeout 1.0
    $ scene84_mc_maia_sex = True
    play sound "se_sfx/blowjob/kiss1.mp3" 
    scene 84_s13 with dissolve
    perception "You capture her lips again, this kiss deeper, hungrier, and full of the pent-up fear and passion of the last few weeks. You hold her head as if she were the only solid thing in a crumbling world."
    play music "ambiance/river_water.mp3" fadein 1.0 volume 0.2 loop
    scene 84_s14 with dissolve
    m "[mc]... please~!"
    jump scene84_3

label scene84_choice03_op2:
    mc "Maia... we can't. Not here. Not like this."
    scene 84_s11 with dissolve
    mc "When we're together, I want it to be because we choose each other, not because we're running from everything else."
    mc "We have to be strong for everyone in that shed. I can't lose my focus."
    mc "You deserve more than that."
    scene 84_s12 with dissolve
    m "I understand, [mc]. You know best."
    scene 84_s11 with dissolve
    mc "Good. Let's get inside, the others are waiting."
    jump scene84_4

label scene84_3:
    $ maia_virgin = False
    play sound "sound_effects/bodydrop4.mp3"
    scene 84_s15 with vpunch
    perception "A surge of primal need floods you. Your hand slides down to her waist, and spin her around. She's so light, so fragile against you, her palms flattening against the rough stone with a thud."
    mc "Shit! Sorry... Did I hurt you?"
    m "*giggles* You can be rough with me, [mc]. I don't mind."
    scene 84_s16 with dissolve
    perception "You gather the fabric of her skirt in your fist, drawing it up to her waist. The air shifts, and the intimate musky scent of her pussy hits your face."
    m "Ahhnn~ [mc]..."
    scene 84_s17 with dissolve
    m "Would you... would you taste me there, [mc]? I want to feel your tongue inside me..."
    mc "You've been aching for this, haven't you? Your whole body is trembling."
    
    if maia_pussy_virgin and maia_anus_virgin:
        mc "This will be our first time fucking, isn't it?"
        m "Y-Yes, [mx]. You kept me waiting too long..."
        mc "I'll make it up to you right now."
        m "*giggles* Please do~! I've always wanted to have your babies... ever since I saw you."

    elif maia_pussy_virgin:
        m "[mx]... I hope you know that you still haven't made love to my pussy yet. Only my ass."
        mc "I prefer it that way, Maia."
        m "*giggles* I know. I just wanted to remind you... in case you wanted me to have your babies~"
    
    if maia_anal_sex > maia_pussy_sex:
        m "Y-Yes~! For so long... I need to feel your tongue inside my butt. Please..."
        mc "Your butt, huh?"
        m "Mhm~"
    else:
        m "Y-Yes~! For so long... I need to feel your tongue inside my pussy. Please..."
    call screen scene84_maia with dissolve

image 84_lick_p1 = Movie(play="images/chapter4/scene84/84_lick_p1.webm", loop=True)
image 84_lick_p2 = Movie(play="images/chapter4/scene84/84_lick_p2.webm", loop=True)

image 84_lick_a1 = Movie(play="images/chapter4/scene84/84_lick_a1.webm", loop=True)
image 84_lick_a2 = Movie(play="images/chapter4/scene84/84_lick_a2.webm", loop=True)

image 84_sex_p1 = Movie(play="images/chapter4/scene84/84_sex_p1.webm", loop=True)
image 84_sex_p2 = Movie(play="images/chapter4/scene84/84_sex_p2.webm", loop=True)

image 84_sex_a1 = Movie(play="images/chapter4/scene84/84_sex_a1.webm", loop=True)
image 84_sex_a2 = Movie(play="images/chapter4/scene84/84_sex_a2.webm", loop=True)

image 84_bj = Movie(play="images/chapter4/scene84/84_bj.webm", loop=True)

image 84_sex2_p = Movie(play="images/chapter4/scene84/84_sex2_p.webm", loop=True)
image 84_sex2_a = Movie(play="images/chapter4/scene84/84_sex2_a.webm", loop=True)
image 84_sex2_ap = Movie(play="images/chapter4/scene84/84_sex2_ap.webm", loop=True)

label scene84_maia_op2:
    scene 84_s63 with Dissolve(1.0)
    perception "You hold her hip. With your thumbs, you gently part her, revealing her glistening anus, already clenching around nothing."
    show 84_lick_a1 with dissolve
    perception "You lean in, and your first, slow, flat stroke of your tongue from bottom to top makes her entire body jolt."
    m "AHH! [mc]! Oh, Gods...! So... so warm...!"
    mc "I love your taste."
    sensation "You feast on her ass. Each wet stroke into her tight ring makes her gasp and whimper. You feel her clenching tighter and tighter around the tip of your tongue, her body trying to pull you deeper."
    m "T-There! Right there! Don't stop!"
    mc "You're ass is becoming too sensitive. You really like it in your butt, hm?"
    m "You... you made me this way, [mc]~! I-It's starting to feel... more intense than my pussy..."
    show 84_lick_a2 with Dissolve(1.0)
    hide 84_lick_a1
    mc "*lick* Mhnnmmm... "
    m "[mx]! You're sticking your tongue inside!?"
    mc "*slurp* Mmmm~"
    m "Gah~! Hnnmnmm... I-I can't... take it!"
    m "[mx], I'm... I'm gonna... AHHHHNNN!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 84_s19 with vpunch
    perception "Her climax crashes over her like a wave. A high, keening wail is torn from her throat as her back arches impossibly, her body seizing around your tongue in a series of pulsing convulsions."
    scene 84_s20 with Dissolve(1.0)
    m "Hahh... Ahhn..."
    perception "She collapses forward onto the stone railing gasping, a sheen of sweat on her skin."
    mc "*laughs* Never heard you make that noise before."
    m "I-I'm sorry, I couldn't control it... hopefully no one heard me... Oh, Gods..."
    jump scene84_maia3

label scene84_maia_op1:
    $ scene84_mc_lick_puss = True
    scene 84_s63 with Dissolve(1.0)
    perception "You spread her legs. She's completely bare and open for you. You lean in, blowing a soft stream of air over her glistening, swollen pussy lips, making her shudder."
    m "Mhnn~"
    show 84_lick_p1 with Dissolve(1.0)
    perception "Your first, long, slow lick from her entrance to her throbbing clit makes her entire body jolt."
    m "Ahhn~! [mx]! Y-Your tongue...!"
    mc "You're already dripping for me. How long have you been waiting for this?"
    m "T-Too long~! I need to feel you... I need you inside..."
    show 84_lick_p2 with Dissolve(1.0)
    hide 84_lick_p1
    perception "You focus your tongue on her tiny red clit and sweet nectar flows down from her hole onto your mouth."
    m "Hahn~!"
    perception "Her juices keep gushing out, the taste is intoxicating. You tongue constantly flicking, licking and sucking her bean."
    scene 84_s64 with dissolve
    m "[mc]! Stop! Wait, I-I need to pee!"
    scene 84_s65 with dissolve
    mc "Hmm?"
    scene 84_s64 with dissolve
    m "I'm so sorry! I should've gone before we started... I was just so excited..."
    scene 84_s65 with dissolve
    call screen scene84_maia2 with dissolve

label scene84_maia2_op1:
    mc "Just hold it in."
    scene 84_s64 with dissolve
    m "Mfhnnn... A-Alright... I'll try~! It's just... you're making it so difficult!"
    show 84_lick_p1 with dissolve
    mc "Seeing you squirm like this... it's so fucking hot."
    m "[mc]! You're making it harder to hold it in~"
    show 84_lick_p2 with dissolve
    m "Oh... oh, yes! Like that! Please, don't stop! I can't... I can't hold on... [mc]!"
    scene 84_s19 with vpunch
    m "AHHHNNN~!"
    perception "Her juices leak out in waves with a sharp, strangled cry. Her hips buck as her orgasm coarses through her. Her inner muscles flutter wildly around your tongue."
    scene 84_s20 with dissolve
    m "Hahh... Ahhn..."
    perception "She collapses forward onto the stone railing gasping, a sheen of sweat on her skin."
    m "Sorry, [mc]. I think I peed while I came too..."
    jump scene84_maia3

label scene84_maia2_op2:
    mc "*chuckles* It's fine. Let it out. I want all of you."
    scene 84_s64 with dissolve
    m "A-Are you sure? Right here? Right now?"
    scene 84_s65 with dissolve
    mc "Mhm. Don't mind me. I'm not stopping."
    show 84_lick_p1 with Dissolve(1.0)
    m "Hahh!? [mc]? You're still... unhn~! ...licking me! How can you... ah!"
    mc "Let it go, Maia. I've got you."
    m "A-Alright..."
    scene 84_s21 with Dissolve(1.0)
    play sound "sound_effects/pee.mp3"
    sensation "She lets out a soft, surrendering sigh and relaxes her muscles. A hot, steady stream of pee immediately hits your chin and neck, soaking your shirt and pooling on the ground beneath you."
    m "Unghn!"
    scene 84_s22 with dissolve
    mc "All done?"
    m "Y-Yes. *giggles* [mc]... you really don't mind... me peeing on you~?"
    mc "I love every part of you. Even the dirty, naughty parts."
    show 84_lick_p2 with Dissolve(1.0)
    mc "*lick* You're perfect."
    m "Yes! Like that! Oh, please, don't stop! I can't... I can't hold on... [mx]!"
    play sound "se_sfx/masturbate_female/masturbate_cum2.mp3"
    scene 84_s19 with vpunch
    m "AHHHNNN~!"
    perception "Her juices leak out in waves with a sharp, strangled cry. Her hips buck as her orgasm coarses through her. Her inner muscles flutter wildly around your tongue."
    scene 84_s20 with Dissolve(1.0)
    m "Hahh... Ahhn..."
    perception "She collapses forward onto the stone railing gasping, a sheen of sweat on her skin."
    jump scene84_maia3

label scene84_maia3:
    m "Hahh..."
    mc "Don't think we're done yet."
    m "Aha... O-Of course. You have to relive yourself too, [mx]."

    if scene84_mc_lick_puss:
        m "My pussy is ready for you. It's warm and moist~"
    else:
        m "My butt is ready for you. It's warm and moist~"
    scene 84_s70 with Dissolve(1.0)
    perception "Maia braces herself, her breath already trembling. She spreads her legs, fully presenting her pussy and ass to you."
    m "Don't... don't just stare. Put it inside me."
    call screen scene84_choice05 with dissolve

default s84_maia3_v = False
default s84_maia3_a = False

default s84_maia3_v2 = False
default s84_maia3_a2 = False

default s84_maia3_v_open = False
default s84_maia3_a_open = False

label scene84_choice05_op2:
    $ maia_anus_virgin = False

    $ s84_maia3_a_open = True
    $ s84_maia3_a = True
    scene 84_s69 with dissolve
    perception "You align yourself with her tight entrance. Her whole body tenses when your tip presses against her. The sunlight catches the sweat beading on her lower back."
    show 84_sex_a1 with dissolve
    if scene84_mc_lick_puss:
        m "Hhhn...! You're spreading it~!"
    else:
        m "Hhhn...! You're spreading it~! So much bigger than your tongue..."
    sensation "You push forward. The resistance is intense. Tight, hot, almost sucking you in with each inch. She gasps sharply, fingers clawing at the rough stone."
    m "Aah—hah—hhnn—! Wait, wait... just... give me a moment to adjust..."
    perception "Her raised leg trembles violently. Her toes curl into the dirt. Every thrust makes her body jolt and tighten around your cock."
    mc "Fuck, Maia... you're squeezing me like you're trying to keep me in forever."
    m "I-I can't help it... it just... ngh~ feels so full... so deep...!"
    m "Ah! ah~–ah~ [mc]... you're stretching my butt so wide..."
    mc "That's it... Let me sink in completely."
    sensation "Her hip jerks each time you sink a little deeper, her entire lower body twitches around you, locking down in instinctive, helpless spasms."
    m "It's too deep... I can feel you sitting inside my stomach—!"
    mc "Good. You'll remember this stretch tomorrow."
    call screen scene84_maia3 with dissolve

label scene84_choice05_op1:
    $ maia_pussy_virgin = False

    $ s84_maia3_v_open = True
    $ s84_maia3_v = True
    scene 84_s68 with dissolve
    perception "Your tip glides over her soaked folds, dripping with her arousal. When you press inside her pussy, her entire body melts under you with a relieved sigh."
    show 84_sex_p1 with dissolve
    m "Ahhnnn~...! Finally... I needed this..."
    mc "So wet it's dripping down your thigh... I'm surprised you didn't ask me to breed you the moment you woke up."
    m "N-no—! I... I get wet when you want me. When you use me like this..."
    sensation "The inner heat of her pussy is completely different. Softer, slicker, eagerly welcoming every inch you push in. Her leg rises again instinctively, giving you deep access."
    m "Yes... yes—ahh—! Don't stop, [mc]... keep fucking me! Mess up my insides until I can't think straight!"
    sensation "Her walls flutter rhythmically around your shaft, clenching and releasing like they're begging you to stay buried as deep as you can go."
    mc "How deep am I? Tell me."
    m "You're so deep, [mc]! I can feel you kissing my womb!"
    perception "Her breasts bounce with each thrust, her breath catching every time you bottom out inside her."
    m "Oh Gods! Y-You're hitting... ngh~! ...right there! Again! Please, again! Make me scream!"
    call screen scene84_maia3 with dissolve

label scene84_maia3_pov:
    scene black with Dissolve(0.3)
    if s84_maia3_v:
        if s84_maia3_v2:
            $ s84_maia3_v2 = False
            show 84_sex_p1 with dissolve
            hide 84_sex_p2
            m "Yeeaaass... I'm being bred, [mx]! Make me- Guhnn~! pregnant all the time!"
            if maia_pregnant:
                mc "You're already pregnant, girl."
                m "Again! Again! Next year! After the next year! Foreevvaaarr~!"
            else:
                mc "You want my seed that badly?"
                m "Mhm~! Make me a mother!"
        else:
            $ s84_maia3_v2 = True
            show 84_sex_p2 with dissolve
            hide 84_sex_p1
            m "Are you... Mhghnn~! g-going to come inside me, [mx]?"
            mc "Is that what you want?"
            m "Yeh... Yes! Mhhnnn~!"
    else:
        if s84_maia3_a2:
            $ s84_maia3_a2 = False
            show 84_sex_a1 with dissolve
            hide 84_sex_a2
            mc "Your ass is going to be gaping after I'm done with you."
            m "T-That's so- Hahnng~! embarssing!"
        else:
            $ s84_maia3_a2 = True
            show 84_sex_a2 with dissolve
            hide 84_sex_a1
            m "[mx]... I already- Nmmm~! feel sore!"
            m "You're trying to break me~!"
    call screen scene84_maia3 with dissolve

default scene84_maia3_vag_first = True
default scene84_maia3_anal_first = True
label scene84_maia3_vag:
    $ scene84_maia3_bj = False
    $ s84_maia3_v = True
    $ s84_maia3_a = False

    if s84_maia3_a2:
        $ s84_maia3_v2 = True
    else:
        $ s84_maia3_v2 = False

    if not s84_maia3_v_open:
        $ s84_maia3_v_open = True
        scene 84_s68 with dissolve
        perception "Your tip glides over her soaked folds, dripping with her arousal. When you press inside her pussy, her entire body melts under you with a relieved sigh."
        show 84_sex_p1 with dissolve
        m "Ahhnnn~...! Finally... I needed this..."
        mc "So wet it's dripping down your thigh... Were you getting off on taking me in your ass?"
        m "N-no—! I... I get wet when you want me. When you use me like this..."
        sensation "The inner heat of her pussy is completely different. Softer, slicker, eagerly welcoming every inch you push in. Her leg rises again instinctively, giving you deep access."
        m "Yes... yes—ahh—! Don't stop, [mc]... keep fucking me! Mess up my insides until I can't think straight!"
        sensation "Her walls flutter rhythmically around your shaft, clenching and releasing like they're begging you to stay buried as deep as you can go."
        mc "How deep am I? Tell me."
        m "You're so deep, [mc]! I can feel you touching my womb!"
        perception "Her breasts bounce with each thrust, her breath catching every time you bottom out inside her."
        m "Oh Gods! Y-You're hitting... ngh~! ...right there! Again! Please, again! Make me scream!"
        mc "Good. You'll remember this stretch tomorrow."
        $ s84_maia3_v2 = False
        call screen scene84_maia3 with dissolve

    if scene84_maia3_vag_first:
        $ s84_maia3_v2 = False
        $ scene84_maia3_vag_first = False
        mc "Your pussy is burning up around me. I want to feel that too."
        m "Yes... please~! I want to feel you fill me there too..."
        scene black with Dissolve(0.3)
        show 84_sex_p1 with dissolve
        perception "You pull out slowly from her tight ass. The stretched ring twitches, fluttering open before clenching as if trying to hold you in."
        m "Mghnnnmm~! It's... throbbing..."
        perception "Her pussy easily spreads for you, welcoming you back. The familiar heat almost burns your shaft after the tightness of her ass."
        m "So... so much... you feel even bigger now..."

    else:
        scene black with Dissolve(0.3)
        if s84_maia3_v2:
            show 84_sex_p2 with dissolve
        else:
            show 84_sex_p1 with dissolve
        m "Ah~ Hah~ Mmmnn~ Annh~"
    call screen scene84_maia3 with dissolve

label scene84_maia3_anal:
    $ scene84_maia3_bj = False
    $ s84_maia3_v = False
    $ s84_maia3_a = True

    if s84_maia3_v2:
        $ s84_maia3_a2 = True
    else:
        $ s84_maia3_a2 = False

    if not s84_maia3_a_open:
        $ s84_maia3_a_open = True
        scene 84_s69 with dissolve
        perception "You align yourself with her tight entrance. Her whole body tenses when your tip presses against her. The sunlight catches the sweat beading on her lower back."
        show 84_sex_a1 with dissolve
        m "Hhhn...! You're spreading it~! So much bigger than your tongue..."
        sensation "You push forward. The resistance is intense. Tight, hot, almost sucking you in with each inch. She gasps sharply, fingers clawing at the rough stone."
        m "Aah—hah—hhnn—! Wait, wait... just... give me a moment to adjust..."
        perception "Her raised leg trembles violently. Her toes curl into the dirt. Every thrust makes her body jolt and tighten around your cock."
        mc "Fuck, Maia... you're squeezing me like you're trying to keep me in forever."
        m "I-I can't help it... it just... ngh~ feels so full... so deep...!"
        m "Ah! ah~–ah~ [mc]... you're stretching my butt so wide..."
        mc "That's it... Let me sink in completely."
        sensation "Her hip jerks each time you sink a little deeper, her entire lower body twitches around you, locking down in instinctive, helpless spasms."
        m "It's too deep... I can feel you sitting inside my stomach—!"
        mc "Good. You'll remember this stretch tomorrow."
        $ s84_maia3_a2 = False
        call screen scene84_maia3 with dissolve

    if scene84_maia3_anal_first:
        $ s84_maia3_a2 = False
        $ scene84_maia3_anal_first = False
        mc "Your ass is calling to me again, Maia. Are you clenching like that on purpose?"
        m "Hmm? N-No... it's just... missing you already..."
        mc "You sly fox. Alright, I'll stretch your hungry ass again."
        scene black with Dissolve(0.3)
        show 84_sex_a1 with dissolve
        m "Mhhnnm~ [mc]... Make me cry with how good it feels~! I want to feel you in my deepest places!"
        perception "You press your full shaft against her tight hole, pushing deep into her colon with one thrust."
        m "Hnn! Slow! S-Slow—! It's still so tight!"
        mc "I got you."
        sensation "You push in, eased by her own arousal coating your cock, her walls stretching around you again with familiar resistance."
    else:
        scene black with Dissolve(0.3)
        if s84_maia3_a2:
            show 84_sex_a2 with dissolve
        else:
            show 84_sex_a1 with dissolve
        m "Ahh! Hnn~! Mphnnmm~! Gods... my hole!"
    call screen scene84_maia3 with dissolve

default scene84_maia3_bj_a_first = True
default scene84_maia3_bj_v_first = True

default scene84_maia3_bj = False
label scene84_maia3_bj:
    $ scene84_maia3_bj = True
    if s84_maia3_a:
        $ s84_maia3_a = False
        if scene84_maia3_bj_a_first:
            $ scene84_maia3_bj_a_first = False
            mc "Maia... Turn around and open your mouth for me."
            m "B-But your penis is digging in my butt!"
            perception "She hesitates, nose wrinkling slightly. A faint flush of embarrassment colors her cheeks."
            mc "*chuckles* Don't worry. It's fine."
            m "...Alright. For you."
            scene black with Dissolve(0.3)
            scene 84_s71 with dissolve
            sensation "Her lips close hesitantly around the head, warm and wet but tentative, more gentle licks than full suction. The slight reluctance only makes the heat of her mouth feel more earnest."
            mc "A little quicker than that."
            show 84_bj with dissolve
            m "Hmm-? Guhkk!"
        else:
            mc "Maia... I need your mouth again."
            m "Mmm... yes, [mc]. I didn't think I'd like how I taste on you... but I do."
            show 84_bj with dissolve
            perception "She takes you deep right away, cheeks hollowing with confidence. A soft moan vibrates around you as the familiar flavor coats her tongue."
            sensation "Her mouth is hotter, surer—tongue swirling deliberately, savoring every slide, every drop that beads at the tip."
    else:
        $ s84_maia3_v = False
        if scene84_maia3_bj_v_first:
            $ scene84_maia3_bj_v_first = False
            mc "Maia... Turn around and open your mouth for me."
            m "It'll taste like my pussy, won't it? All over you..."
            scene black with Dissolve(0.3)
            show 84_bj with dissolve
            m "Guhkn! It's... shweeter than ah thoug... *gag*"
        else:
            mc "Turn around, Maia... I want those pretty lips now."
            m "Yes, [mx]~"
            scene black with Dissolve(0.3)
            show 84_bj with dissolve
            perception "She engulfs you eagerly, moaning openly at the familiar flavor coating her tongue. Her hands grip your legs as she works, hungry for every trace of where you've been."
            m "Mmph... *slurp* give me moare... I want *gag* to drink evewything you shaved for meh..."
            sensation "Her mouth is greedy this time, hot, wet suction, tongue swirling to gather every drop of her own juices mixed with you, swallowing with soft, happy sounds."
    call screen scene84_maia3 with dissolve

default s84_maia4_cum_v_again = False
default s84_cum_inside = False
default s84_cum_outside = False
label scene84_maia3_cum:
    if not scene84_maia3_bj:
        call screen scene84_choice06 with dissolve
        if s84_maia3_a and s84_cum_inside:
            show 84_sex_a1 with dissolve
            hide 84_sex_a2
            m "I'm...!"
            perception "Her entire body locks up, every muscle seizing as her orgasm hits like a shockwave. Her lifted leg spasms so hard the crate rattles."
            show 84_sex_a1 with vpunch
            play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3"
            m "Hnn! [mc]! I'm— I'm coming— I'm coming from my ass!"
            play sound "se_sfx/sex/sex_cum5.mp3" 
            scene 84_s27 with vpunch
            sensation "The walls of her ass clamps in violent pulses, squeezing you until the pressure breaks your control."
            mc "Maia—!"
            play sound "se_sfx/sex/sex_cum9.mp3" 
            scene 84_s28 with Dissolve(0.3)
            scene 84_s28 with vpunch
            sensation "You spill deep inside her, cum flooding into her tightest place, filling her until she whimpers from the overwhelming fullness."
            m "N-No more! I'm stuffed... so warm..."
            play sound "se_sfx/sex/sex3.mp3" 
            scene 84_s29 with Dissolve(1.0)
            mc "Hahh... Ahh..."
            m "That was... Ahh... incridble, [mc]..."
            mc "If only you could see what I did to your ass."
            m "D-Don't look! I can't close it... now it will start leaking everywhere all throughout the day."
            mc "You could try taping it with something."
            m "Taping it?"
            mc "Nevermind. I guess you'll just have to keep leaking my semen all over the place."
            m "Aww... *giggles* Poor little semens, you'll never find my womb. Not in there~"
            mc "*laughs* What are you saying?"
            m "Hahhh... I could really use some rest now."
            impulse "No. It's not enough. You have to completely and utterly break her. Make her beg for your cock everytime she sees you. Make her pussy involuntary drip with a single glance."
            mc "..."
            m "[mc]? Why did you go quiet?"

        elif s84_maia3_v and s84_cum_inside:
            $ s84_maia4_cum_v_again = True
            show 84_sex_p1 with dissolve
            hide 84_sex_p2
            perception "Her hips jerk forward as pleasure hits her hard, her leg slipping off the crate before she scrambles to brace herself."
            show 84_sex_p1 with vpunch
            m "Aah! AAH! [mc], you're hitting—! You're hitting my feel good spot!"
            play sound "se_sfx/masturbate_female/6_masturbate_cum1.mp3"
            show 84_sex_p1 with vpunch
            sensation "Her inner walls clamp, ripple, soak you with a rush of wet heat. The squeeze drags your climax out of you."
            mc "Say it!"
            m "F-Fill me with your baby making seed~! M-Make me your woman! Own me! Mark me!"
            m "My pussy is yours to breed forever!"
            play sound "se_sfx/sex/sex_cum5.mp3" 
            if persistent.xray_mode:
                scene 84_s24_xray1 with vpunch
                sensation "You spill deep inside her, cum flooding into her womb, filling her until she whimpers from the overwhelming fullness."
                play sound "se_sfx/sex/sex_cum9.mp3" 
                scene 84_s25_xray2 with Dissolve(0.3)
                scene 84_s25_xray2 with vpunch
                mc "Nghnn!"
                m "I can... I can feel you pouring inside me! Gods!"
                play sound "se_sfx/sex/sex3.mp3" 
                scene 84_s26_xray3 with Dissolve(1.0)
            else:
                scene 84_s24 with vpunch
                sensation "You spill deep inside her, cum flooding into her womb, filling her until she whimpers from the overwhelming fullness."
                play sound "se_sfx/sex/sex_cum9.mp3" 
                scene 84_s25 with Dissolve(0.3)
                scene 84_s25 with vpunch
                mc "Nghnn!"
                m "I can... I can feel you pouring inside me! Gods!"
                play sound "se_sfx/sex/sex3.mp3" 
                scene 84_s26 with Dissolve(1.0)
            mc "Hahh... Ahh..."
            if not maia_pregnant:
                call pregnancy_check_maia from ___call_pregnancy_check_maia
            m "That was... Ahh... incridble, [mc]..."
            m "I can feel your seed leaking from my pussy."
            if maia_pregnant:
                m "*giggles* If I wasn't already pregnant then this will surely do the job~"
            else:
                m "This amount must definitely get me pregnant, [mc]. I really hope I'm not infertile..."
                mc "Hahhn... We'll see."
            m "I could really use some rest now."
            impulse "No. It's not enough. You have to completely and utterly break her. Make her beg for your cock everytime she sees you. Make her pussy involuntary drip with a single glance."
            mc "..."
            m "[mc]? Why did you go quiet?"
            
        else:
            perception "Her back arches sharply, thighs trembling as the wave crashes through her. She pushes back against you one last time, desperate, chasing every last thrust."
            m "Ah—! [mc]—! I'm— I'm coming—! Don't stop—!"
            play sound "se_sfx/sex/sex_cum1.mp3" 
            scene 84_s30 with vpunch
            sensation "Her body shudders hard, inner muscles fluttering wildly around nothing now that you've pulled free. The sudden emptiness makes her whine, but the heat building in your hand is unbearable."
            play sound "se_sfx/blowjob/facial4.mp3" 
            scene 84_s31 with vpunch
            perception "hick ropes streak across the curve of her ass, painting her skin in hot, heavy pulses—some landing high on her lower back, others dripping slowly down between her cheeks."
            m "Mark me... cover me... make me yours on the outside too~"
            scene 84_s32 with Dissolve(1.0)
            m "So warm... I can feel it sliding down my thighs..."
            mc "Hah... god, Maia..."
            m "Look what you did to me, [mc]... all messy and claimed."
            m "That was... ahh... incredible."
            m "Hahhh... I could really use some rest now."
            impulse "No. It's not enough. You have to completely and utterly break her. Make her beg for your cock everytime she sees you. Make her pussy involuntary drip with a single glance."
            mc "..."
            m "[mc]? Why did you go quiet?"
    else:
        perception "She takes you deeper on instinct, eyes watering but fierce, lips sealed tight. Her throat flutters around the head each time she swallows."
        m "Mmmph—!"
        play sound "se_sfx/blowjob/blowjob_cum4.mp3" 
        scene 84_s33 with vpunch
        sensation "The vibration of her moan, the wet heat, the way her tongue presses up underneath—it snaps your control. You spill straight down her throat in heavy, relentless pulses."
        mc "Maia! Swallow it! All of it!"
        play sound "se_sfx/blowjob/blowjob_cum5.mp3" 
        scene 84_s34 with vpunch
        perception "She eagerly gulpes down each wave, cheeks hollowing as she milks you dry. A thin trail escapes the corner of her mouth despite her best effort."
        m "You tashte... sho stwong... sho mush..."
        play sound "se_sfx/blowjob/blowjob1.mp3" 
        scene 84_s35 with Dissolve(1.0)
        m "Ahhhhnn.... Evewy dwop."
        m "Hahh... Such a greedy girl."
        m "Onry foh you~"
        scene 84_s36 with dissolve
        play sound "se_sfx/blowjob/kiss4.mp3" 
        m "*mwah* Thank you for feeding me~"
        scene 84_s37 with Dissolve(1.0)
        m "T-That was... Gods, that was incredible, [mc]..."
        m "I could really use some rest now."
        scene 84_s38 with dissolve
        impulse "No. It's not enough. You have to completely and utterly break her. Make her beg for your cock everytime she sees you. Make her pussy involuntary drip with a single glance."
        mc "..."
        scene 84_s37 with dissolve
        m "[mc]? You're looking at me funny."
        scene 84_s38 with dissolve
    call screen scene84_choice07 with dissolve

label scene84_choice07_op1:
    mc "Yeah... Let's get inside."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    m "Thank you. I can barely stand..."
    m "[mc]! Hold me!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 84_s43 with vpunch
    mc "I got you."
    mc "*chuckles* Come on, the others must be worried by now."
    $ renpy.end_replay()
    jump scene84_maia5

label scene84_choice07_op2:
    $ mc_scene84_second_time = True
    if scene84_maia3_bj:
        mc "Incredible? Maia... I didn't say anything about stopping."
        scene 84_s39 with dissolve
        m "Huh—!? W-Wait, [mc]!"
        scene 84_s40 with dissolve
        m "J-Just... j-just give me a moment— I need to catch my breath—!"
        scene 84_s72 with dissolve
        perception "You hook your hands under her hips and pull. Her feet scramble, her body rising whether she's ready or not. She stumbles into you, palms flattening against your stomach for balance."
        m "H-haah... w-wait— what are you— this angle... this is so open!"
        mc "Up. Higher. Good... right there."
        if s84_maia4_a:
            scene 84_s74 with dissolve
            m "[mc], you're being so rough~ I love it~! It makes me feel... owned... I-I'm yours!"
            show 84_sex2_a with vpunch
            m "HAAH!"
            perception "You slam into her as hard as you can, burying yourself in her ass to the hilt. Her back jerks, her thighs shaking violently at the sheer force. Her breath shatters into broken moans."
        elif s84_maia4_v:
            scene 84_s73 with dissolve
            m "[mc], you're being so rough~ I love it~! It makes me feel... owned... I-I'm yours!"
            show 84_sex2_p with vpunch
            m "HAAH!"
            perception "You slam into her as hard as you can, burying yourself in her pussy to the hilt. A sharp cry leaves her throat while her thighs tremble from the relentless rhythm."
        m "Mmmf! Haa! mmmm... I can't... think..."
        scene black with Dissolve(0.3)
        show 84_sex2_ap with dissolve
        mc "Suck. Let me hear how much you love this."
        m "Mah breashts are... ouh~!"
        mc "Whoops. Reham will sew it back."
        m "Shrow... daw... y-you're... brreakin' meh~!"
        m "I—I'm gnna— faa—!"
        if s84_maia4_a:
            mc "I'll hold you. Just keep tightening that perfect ass around me... Ahhn! Just like that!"
        if s84_maia4_v:
            mc "I've got you. Don't fall. Just keep squeezing me with that tight pussy of yours... nhh— yes— just like that..."
        call screen scene84_maia4 with dissolve

    else:
        mc "Incredible? Maia... I didn't say anything about stopping."
        scene 84_s40 with dissolve
        m "Huh—!? W-Wait, [mc], please!"
        m "J-Just... j-just give me a moment— I need to catch my breath—!"
        scene 84_s72 with dissolve
        perception "You hook your hands under her hips and pull. Her feet scramble, her body rising whether she's ready or not. She stumbles into you, palms flattening against your stomach for balance."
        m "H-haah... w-wait— what are you— this angle... this is so open!"
        mc "Up. Higher. Good... right there."
        if s84_maia4_a:
            scene 84_s74 with dissolve
            m "[mc], you're being so rough~ I love it~! It makes me feel... owned... I-I'm yours!"
            #play sound "se_sfx/sex/sex6.mp3" 
            show 84_sex2_a with vpunch
            m "HAAH!"
            perception "You slam into her as hard as you can, burying yourself in her ass to the hilt. Her back jerks, her thighs shaking violently at the sheer force. Her breath shatters into broken moans."
        elif s84_maia4_v:
            scene 84_s73 with dissolve
            m "[mc], you're being so rough~ I love it~! It makes me feel... owned... I-I'm yours!"
            #play sound "se_sfx/sex/sex6.mp3" 
            show 84_sex2_p with vpunch
            m "HAAH!"
            perception "You slam into her as hard as you can, urying yourself in her pussy to the hilt. A sharp cry leaves her throat while her thighs tremble from the relentless rhythm."
        m "Mmmf! Haa! mmmm... I can't... think..."
        scene black with Dissolve(0.3)
        show 84_sex2_ap with dissolve
        mc "Suck. Let me hear how much you love this."
        m "Mah breashts are... ouh~!"
        mc "Whoops. Reham will sew it back."
        m "Shrow... daw... y-you're... brreakin' meh~!"
        m "I—I'm gnna— faa—!"
        if s84_maia4_a:
            $ s84_maia4_a2 = True
            mc "I'll hold you. Just keep tightening that perfect ass around me... Ahhn! Just like that!"
        if s84_maia4_v:
            $ s84_maia4_v2 = True
            mc "I've got you. Don't fall. Just keep squeezing me with that tight pussy of yours... nhh— yes— just like that..."
        call screen scene84_maia4 with dissolve

default scene84_maia4_a_first = True
default s84_maia4_a2 = False

default scene84_maia4_v_first = True
default s84_maia4_v2 = False

label scene84_maia4_pov:
    scene black with Dissolve(0.3)
    if s84_maia4_v:
        if s84_maia4_v2:
            $ s84_maia4_v2 = False
            show 84_sex2_p with dissolve
            m "Ah! Ah! Yoh digin into mah pussy~!"
        else:
            $ s84_maia4_v2 = True
            show 84_sex2_ap with dissolve
            m "Uwoh~! Ah think am ah... come again!"
    else:
        if s84_maia4_a2:
            $ s84_maia4_a2 = False
            show 84_sex2_a with dissolve
            mc "Your ass is so good at milking my cock."
            m "If shis keeph going ah might pash ouh~"
        else:
            $ s84_maia4_a2 = True
            show 84_sex2_ap with dissolve
            mc "I love seeing you get dumber and dumber from my cock."
            m "Mgghhnnn!"
    call screen scene84_maia4 with dissolve

label scene84_maia4_a:
    $ s84_maia4_a = True
    $ s84_maia4_v = False

    if s84_maia4_v2:
        $ s84_maia4_a2 = True
    else:
        $ s84_maia4_a2 = False

    if scene84_maia4_a_first:
        $ s84_maia4_a2 = False
        $ scene84_maia4_a_first = False
        mc "I'm not done with your ass yet... I'm going to open it so wide you'll be walking funny for days."
        scene black with Dissolve(0.3)
        show 84_sex2_a with dissolve
        m "MFGHMMM—!"
        perception "You thrust into her now loose hole. The wet, obscene sound echoes between you as she cries out uncontrolled sounds that would echo through the whole forest if she weren't biting your finger."
        m "NGH—AAHNN—!"
        sensation "Her tongue swirls desperately around your finger. The lewd, wet sounds mix with her ragged breathing."
        m "Hahh! Hnn~! Aghnmmmn~!"
        mc "You're mine. Every part of you. Your ass will remember my cock long after today is over."
        m "MFGHMMM~!"
    else:
        scene black with Dissolve(0.3)
        if s84_maia4_a2:
            show 84_sex2_ap with dissolve
        else:
            show 84_sex2_a with dissolve
        m "Ehnnnm~!"
    call screen scene84_maia4 with dissolve

label scene84_maia4_v:
    $ s84_maia4_a = False
    $ s84_maia4_v = True

    if s84_maia4_a2:
        $ s84_maia4_v2 = True
    else:
        $ s84_maia4_v2 = False

    if scene84_maia4_a_first:
        $ s84_maia4_v2 = False
        $ scene84_maia4_v_first = False
        mc "Your pussy's not escaping me."
        scene 84_s73 with dissolve
        m "MFGHMM!?"
        perception "You realign and push into her slick front, stretching her open in one smooth thrust. Her cry breaks against your finger, her voice dissolving into pure, helpless sound."
        show 84_sex2_p with vpunch
        m "NGHAANN!"
        sensation "Her tongue tightens around your finger, swirling and trembling as she tries to breathe."
        m "Hahh! Hnn~! Aghnmmmn~!"
        mc "You're mine. You hear that!? Your pussy is mine for whenever I get the urge."
        m "MFGHMMM~!"
    else:
        scene black with Dissolve(0.3)
        if s84_maia4_v2:
            show 84_sex2_ap with dissolve
        else:
            show 84_sex2_p with dissolve
        m "[mc] cock... sho biiiiiggg~"
    call screen scene84_maia4 with dissolve

label scene84_maia4_cum:
    if s84_maia4_a:
        play sound "se_sfx/masturbate_female/masturbate_cum3.mp3"
        show 84_sex2_a with vpunch
        perception "Her whole body tightens, trembling violently as her climax hits, her knees nearly buckling. You hold her steady by wrapping your arm around her neck as she loses control."
        mc "Good girl... let it out! I'm cumming too!"
        play sound "se_sfx/sex/sex_cum6.mp3" 
        scene 84_s41 with vpunch
        sensation "The force of her orgasm triggers your own. Her body convulses around your shaft in waves of blinding pleasure. Her already warm colon grows even hotter as you fill it."
        mc "Maia!"
        play sound "se_sfx/sex/sex_cum1.mp3" 
        scene 84_s41 with vpunch
        sensation "You keep spilling deep inside her, your arm around her neck anchoring her like iron chains while she convulses on you."
        m "Mfhhnnn~!"

    if s84_maia4_v:
        play sound "se_sfx/masturbate_female/masturbate_cum3.mp3"
        show 84_sex2_p with vpunch
        perception "Her thighs clamp together, shaking, her whole body trembling as climax tears through her. You grab her head, keeping her steady as she unravels."
        mc "Good girl... let it out! I'm cumming too!"
        play sound "se_sfx/sex/sex_cum6.mp3" 
        if persistent.xray_mode:
            if s84_maia4_cum_v_again:
                scene 84_s42_xray1 with vpunch
                sensation "Her pussy contracts around your cock, each tight pulse wringing the cum out of you. You fill her fully, your release coating every stretched inch inside her."
                mc "Maia!"
                play sound "se_sfx/sex/sex_cum1.mp3" 
                scene 84_s42_xray2 with vpunch
                sensation "You flood the deepest part of her loose hole, your arm around her neck anchoring her like iron chains while she convulses on you."
            else:
                scene 84_s42_xray3 with vpunch
                sensation "Her pussy contracts around your cock, each tight pulse wringing the cum out of you. You fill her fully, your release coating every stretched inch inside her."
                mc "Maia!"
                play sound "se_sfx/sex/sex_cum1.mp3" 
                scene 84_s42_xray4 with vpunch
                sensation "You flood the deepest part of her loose hole, your arm around her neck anchoring her like iron chains while she convulses on you."
        else:
            scene 84_s42 with vpunch
            sensation "Her pussy contracts around your cock, each tight pulse wringing the cum out of you. You fill her fully, your release coating every stretched inch inside her."
            mc "Maia!"
            play sound "se_sfx/sex/sex_cum1.mp3" 
            scene 84_s42 with vpunch
            sensation "You flood the deepest part of her loose hole, your arm around her neck anchoring her like iron chains while she convulses on you."

        if not maia_pregnant:
            mc "Get pregnant!"
            call pregnancy_check_maia from ____call_pregnancy_check_maia
        m "Mfhhnnn~!"
    
    play sound "sound_effects/body/clothes1.mp3"
    scene 84_s44 with Dissolve(1.0)
    perception "A broken sob escapes her lips as the warm seed drips from her body onto the ground below. Her hole is still steaming hot and leaking with her juices, twitching with aftershocks."
    mc "Look what you do to me..."
    m "..."
    mc "...Maia?"
    m "..."
    mc "..."
    perception "Her body hangs over the stone railing like a discarded piece of clothing. A thin string of drool slides off her lip and drips down to the river. Her eyes are half-lidded, pupils blown wide, stuck in a haze of bliss."
    m "[mc]..."
    mc "I'm here!"
    mc "...Shit. What the hell do I even tell the others?"
    mc "C-Can you walk, Maia?"
    m "Ughhnnmm...."
    mc "Thought so."
    mc "Guess I'm carrying you..."
    $ renpy.end_replay()
    jump scene84_maia5

label scene84_maia5:
    stop music fadeout 1.0
    scene 84_s45 with Fade(1.5,1.0,1.0)
    play music "fire.mp3" fadein 1.0 volume 0.55 loop
    mc "Did I miss anything?"
    scene 84_s46 with dissolve
    alex "Finally! Where the hell were you two?"
    scene 84_s45 with dissolve
    mc "Sorry. We just had an issue. It's been dealt with."
    scene 84_s46 with dissolve
    reham "Maia? Are you alright? You look... winded."
    scene 84_s47 with dissolve
    m "Huh!? I-I'm... Umm... I..."
    scene 84_s48 with dissolve
    mc "She's fine. She tripped over a branch. Gave her a scare is all."
    scene 84_s75 with dissolve
    reham "I see. Well, come over here."
    scene 84_s49 with Dissolve(1.0)
    reham "I'll take a look, make sure nothing's sprained."
    m "T-Thank you, Reham! But, I just need to take a seat! Right here! On this very hard, very normal chair!"
    reham "Are you sure?"
    m "Yes!"
    reham "You're acting weird."
    if mc_sex_reham:
        reham "Hmm? *sniff* *sniff*"
        scene 84_s50 with dissolve
        reham "{size=30}This scent... I-It's your semen, [mc]...{/size}"
        mc "Shhhh..."


    #if mc went for a second time.
    #alex "What the hell, [mc]? Where were you!?"
    #mc "Sorry. Needed to catch up on some things with Maia. Was I gone long?"
    #alex "No shit you were gone long! And what's wrong with—"
    #alex "You know what? No. I don't want to know."
    #reham "Oh dear! Maia, what happened?! Did your fever come back?"
    #mc "She just... fainted. All of a sudden. Must be the exhaustion."
    #mc "Have you been feeding her properly, Reham? She seems... depleted."
    #reham "I–I swear I have! I've been giving her everything she needs! Here. lay her here, gently. I'll heat up the soup."
    #mc "Thank you."
    #reham "Hmm? *sniff* *sniff* {size=30}This scent... I-It's your semen, [mc]...{/size}"
    #mc "Shhhh..."
    alex "*sigh* Unbelievable."
    jump scene84_4

label scene84_4:
    if mc_princess_reham:
        if mc_console_maia:
            stop music fadeout 1.0
            scene 84_s59 with Fade(1.0,1.0,0.5)
            play music "hope/hope.mp3" fadein 1.0 loop
            mc "Alright. Let me ask again, is everyone ready?"
            scene 84_s60 with dissolve
            alex "I guess."
            reham "Yes!"
            scene 84_s59 with dissolve
            mc "Good. As for me..."
            scene 84_s61 with Dissolve(2.0)
            mc "I have a horse that I need to get back first."
            #stop music fadeout 3.0
            scene 84_s62 with Dissolve(1.5)
            jump Update0_4_0_end
        else:
            stop music fadeout 1.0
            scene 83_s59 with Fade(1.0,1.0,0.5)
            play music "hope/hope.mp3" fadein 1.0 loop
            mc "Alright. Let me ask again, is everyone ready?"
            scene 83_s60 with dissolve
            alex "I guess."
            reham "Yes!"
            scene 83_s59 with dissolve
            mc "Good. As for me..."
            scene 84_s61 with Dissolve(2.0)
            mc "I have a horse that I need to get back first."
            #stop music fadeout 3.0
            scene 84_s62 with Dissolve(1.5)
            jump Update0_4_0_end

    else:
        stop music fadeout 1.0
        scene 84_s51 with Fade(1.4,1.0,1.3)
        play music "fire.mp3" fadein 1.0 volume 0.55 loop
        lewis "Uhh... [mc]? I've got a couple questions about what we're doing next."
        lewis "Or should I be calling you 'sir' now? I honestly don't know. We're not exactly a real army."
        scene 84_s66 with dissolve
        call screen scene84_choice04 with dissolve

label scene84_choice04_op1:
    $ mc_name_sir = True
    mc "Sir is fine. We may not have uniforms, but we are an army. And an army needs order."
    mc "But first, proper introductions. I know Joan, and I caught your name as Lewis. That's about it."
    scene 84_s51 with dissolve
    lewis "...Right. Sir."
    lewis "Corporal Lewis Vane of the third Irda border patrol. At your service."
    scene 84_s52 with dissolve
    joan "Private Joan Hill, also third border patrol, sir."
    scene 84_s66 with dissolve
    mc "What are your questions, recruits?"
    jump scene84_5

label scene84_choice04_op2:
    $ mc_name_name = True
    mc "We're all risking our necks equally here. Save the 'sirs' for later. For now, [mc] will do just fine."
    scene 84_s51 with dissolve
    lewis "Alright, [mc]. Makes it easier."
    scene 84_s66 with dissolve
    mc "But first, proper introductions. I know Joan, and I caught your name as Lewis. That's about it."
    scene 84_s51 with dissolve
    lewis "Corporal Lewis Vane of the third Irda border patrol. At your service."
    scene 84_s52 with dissolve
    joan "Private Joan Hill, also third border patrol, sir."
    scene 84_s66 with dissolve
    mc "Pleasure to meet you both. What's on your mind?"
    jump scene84_5

label scene84_choice04_op3:
    $ mc_name_name = True
    mc "How about 'Master'? I don't mind if you and especially Joan call me that."
    scene 84_s53 with dissolve
    joan "S-Sorry, but I'd really rather not!"
    scene 84_s55 with dissolve
    lewis "Master?!"
    scene 84_s54 with dissolve
    mc "Relax, you two. I'm just joking. You can call me whatever you want."
    scene 84_s51 with dissolve
    lewis "Alright, then it's [mc]."
    scene 84_s66 with dissolve
    mc "Before you ask anything, I want proper introductions. I know Joan, and I caught your name as Lewis. That's about it."
    scene 84_s51 with dissolve
    lewis "Corporal Lewis Vane of the third Irda border patrol. At your service."
    scene 84_s52 with dissolve
    joan "Private Joan Hill, also third border patrol, sir."
    scene 84_s66 with dissolve
    mc "Pleasure to meet you both. What are your questions?"
    jump scene84_5

label scene84_5:
    if mc_save_queen:
        scene 84_s51 with dissolve
        lewis "Where is Her Majesty staying? She could return and dismantle Avery's schemes herself."
        scene 84_s66 with dissolve
        mc "Her return now might trigger the civil war she's been trying to avoid."
        mc "And as you said, the castle has changed. It wouldn't be the one she remembers."
        mc "She will come back when the time is right to help us expose the truth."
        scene 84_s51 with dissolve
        lewis "I see... I trust Her Majesty's judgment, and your counsel."
        scene 84_s66 with dissolve
        mc "Do you have any other questions?"
    scene 84_s51 with dissolve
    lewis "So, are there specific people you want us to look for? People who might help us rescue the princess?"
    scene 84_s52 with dissolve
    joan "Yes. Allies, either in the city or outside."
    scene 84_s66 with dissolve
    mc "Hmm..."
    mc "There are a few that come to mind, but I'm not sure they're the fighting type."
    scene 84_s51 with dissolve
    if mc_name_name:
        lewis "Wasn't thinking of fighters, [mc]. Not for this. If we're to pull this off quietly, we need planners. Spies. People who know how to move unseen."
    else:
        lewis "Wasn't thinking of fighters, sir. Not for this. If we're to pull this off quietly, we need planners. Spies. People who know how to move unseen."
    scene 84_s66 with dissolve
    mc "You're right. There's Yuuhi, the tailor who helped make my magic resistant armor. I doubt I would've lived this long without her work."
    scene 84_s52 with dissolve
    joan "I know her! Her father is the prime blacksmith for the Irdan army. His loyalty to the crown, or what's left of it, is absolute."
    joan "Convincing her would be difficult, let alone him."
    scene 84_s66 with dissolve

    if mc_harem_yuuhi:
        mc "We're in a relationship. She'll at least hear me out. She has to."
    scene 84_s51 with dissolve
    lewis "Um, how exatly would the daughter of blacksmith benefit us? Could she act as a spy?"
    scene 84_s66 with dissolve
    mc "I was thinking of reaching out to her... about my hand."
    scene 84_s51 with dissolve
    if mc_name_name:
        lewis "Your hand?"
    else:
        lewis "Your hand, sir?"
    scene 84_s66 with dissolve
    mc "I'm hoping she can convince her father to forge a prosthetic."
    scene 84_s51 with dissolve
    lewis "Hmm... Even the best smithwork would be mostly decorative. Combat worthy prosthetics are rare."
    scene 84_s52 with dissolve
    if mc_name_name:
        joan "Is it safe, [mc]? The market district is crawling with patrols now."
    else:
        joan "Is it safe, sir? The market district is crawling with patrols now."
    scene 84_s66 with dissolve
    mc "We'll see what happens. It's just an idea for now."

    mc "In the case of a spy, there's Diana. She works at a brothel called the Slick Worm somewhat close to the capital."

    if mc_harem_diana or mc_friend_diana:
        mc "She's planning to buy the brothel. If we can help her secure it, we migh have leverage over potentially important clients as they're more likely to visit a regular tavern rather than a brothel."
    scene 84_s51 with dissolve
    lewis "A spy in the pillow house? As long as you trust her, that's a sharp idea."
    scene 84_s52 with dissolve
    joan "Anyone else?"
    scene 84_s66 with dissolve
    mc "What about Eireen? If we can get the support of the guild then we'd be set immediately."
    scene 84_s51 with dissolve
    lewis "*scoff* Not in a hundred moons."
    scene 84_s53 with dissolve
    joan "I never quite liked her ever since she... rejected me from the guild. It's why I opted to join the guards instead."
    scene 84_s54 with dissolve
    mc "I don't know, she seemed understanding and noble... at times. But we'll scratch that for now."
    scene 84_s66 with dissolve
    if not mc_execute_kat or not mc_life_kat:
        mc "There's an elf, Ava. She might be strong. After I helped her friend Kat, she owes me a debt. Or at least, she has a reason to listen."
    else:
        mc "There's an elf, Ava... she's strong. But... I doubt she'll help us now that Kat is gone. She seemed really devestated about it."
        mc "Avery will definitely tell her that I was the one who..."
        scene 84_s52 with dissolve
        joan "The one who what...?"
        scene 84_s66 with dissolve
        mc "Forget it. It was a mistake on my behalf."

    mc "Actually, I have to ask. What happened to Darius? He confronted us when we were leaving Able's tavern."
    scene 84_s56 with dissolve
    lewis "He's... alive. Gravely injured, but he survived."
    scene 84_s57 with dissolve
    joan "Sir Darius was the reason no one was killed during the explosion. He shielded his men."
    scene 84_s67 with dissolve
    mc "Shit..."
    scene 84_s56 with dissolve
    if mc_name_name:
        lewis "[mc], was that the only way? Was there really no other choice?"
    else:
        lewis "Sir, was that the only way? Was there really no other choice?"

    lewis "Some of those guards... they were good people, just following orders."
    scene 84_s67 with dissolve
    mc "I'm not sure, Lewis. In that moment, it felt like the only way."
    scene 84_s57 with dissolve
    joan "Speaking of that... what happened to the mage who cast it? We could definitely use someone with that kind of power."
    scene 84_s67 with dissolve
    mc "I don't know. We went our separate ways before the chaos."
    mc "I severely underestimated her at first, but you're right, Joan. Having her would strengthen us a lot."
    m "She seemed very... unstable to me, [mc]. I don't want her to accidentally hurt the princess."
    scene 84_s52 with dissolve
    joan "Alright. Is there anyone you trust outside the city?"
    scene 84_s66 with dissolve
    mc "I haven't left much, so there aren't many."
    if quest_witch_amelia_alive_free:
        mc "Oh, right! The witch, Amelia."
        scene 84_s51 with dissolve
        if mc_name_name:
            lewis "The witch that was kidnapping men? You can't be serious, [mc]... She's not exactly known for her stability or goodwill."
        else:
            lewis "The witch that was kidnapping men? You can't be serious, sir... She's not exactly known for her stability or goodwill."
        scene 84_s66 with dissolve
        mc "I have... a history with her. We parted on good terms, last I saw her. But that was a long time ago. Who knows where she is now, or if she even remembers me."
    else:
        mc "*sigh* There was a witch, Amelia."
        scene 84_s51 with dissolve
        if quest_witch_amelia_dead:
            lewis "Didn't you... kill her, [mc]? Last I heard, Her Majesty was really angry you did so."
        elif not quest_witch_amelia_alive_free:
            lewis "Last I heard, she was thrown in the dungeon."
            scene 84_s66 with dissolve
            mc "Yeah. Scratch that too."

    scene 84_s52 with dissolve
    joan "Anyone else?"
    scene 84_s58 with Dissolve(1.0)
    mc "The village! Alex, do you remember those villagers we stumbled upon?"
    alex "The isolated ones with the strange customs? Most of them weren't warriors. I doubt they could fight."

    if mc_paricipated_festival:
        mc "We don't need them to fight. We can ask them for supplies. I don't think they can refuse me after I won their festival."
        alex "That festival... I still can't believe you agreed to it. Or that you won."
        mc "And look at us now. That bizarre day might be the reason they agree to help us."
        alex "The village is a couple of days away by horseback. I'm not sure it's worth wasting that time on a maybe."
        mc "It's an option if we're desperate."
    else:
        mc "We can ask them for supplies!"
        alex "Are you sure we can? The last thing I remember was the angry looks they gave us."
        lewis "Why? What happened?"
        mc "I... declined an invitation to join their breeding festival."
        joan "B-Breeding fetival!?"
        mc "Forget it. They won't help."

    scene 84_s66 with Dissolve(1.0)
    mc "That's everyone I can remember who might have a chance of helping."
    mc "For now, just focus on the guards. And maybe Negumi, the mage. I doubt she went far."
    scene 84_s51 with dissolve
    lewis "Understood."
    scene 84_s66 with dissolve
    stop music fadeout 1.0
    scene 84_s59 with Fade(1.0,1.0,1.0)
    play music "hope/hope.mp3" fadein 1.0 loop
    if mc_console_maia:
        mc "Is everyone ready?"
        scene 84_s60 with dissolve
        alex "Yes."
        scene 84_s59 with dissolve
        mc "Good. As for me..."
        scene 84_s61 with Dissolve(2.0)
        mc "I have a horse that I need to get back first."
        scene 84_s62 with Dissolve(4.0)
    else:
        stop music fadeout 1.0
        scene 83_s59 with Fade(1.0,1.0,1.0)
        play music "hope/hope.mp3" fadein 1.0 loop
        mc "Is everyone ready?"
        scene 83_s60 with dissolve
        alex "Yes."
        scene 83_s59 with dissolve
        mc "Good. As for me..."
        scene 84_s61 with Dissolve(2.0)
        mc "I have a horse that I need to get back first."
        #stop music fadeout 3.0
        scene 84_s62 with Dissolve(1.5)
    jump Update0_4_0_end

label Update0_4_0_end:
    ""
    scene 85_s1 with Fade(1.0,1.0,1.0)
    alex "Where is this horse of yours exactly?"

    if mc_tried_help_alex:
        $ mc_save_queen = True

    scene 85_s2 with dissolve
    mc "Stabled outside the city walls, for some reason. Had an awful time finding the place the first time."
    mc "I need to make this quick. Do you still have the horse you rode here on?"
    scene 85_s1 with dissolve
    alex "I do. But... should we reconsider this? Rushing in without proper preparation..."
    scene 85_s2 with dissolve
    scene 85_s3 with Dissolve(1.0)
    mc "What's to reconsider? We can't all fit on one horse. Poor guy will crumble under the weight."

    if mc_princess_alex:
        mc "And every moment counts if we're going to reach the princess in time."

    alex "...You're right. He's nearby, tied to a tree. I'll bring him here."
    stop music fadeout 1.0 
    scene 85_s4 with Dissolve(1.3)
    play music "fire.mp3" fadein 1.0 volume 0.3 loop
    reham "You can't go out there looking like the city's most wanted poster. *laughs* They did a terrible job drawing you, by the way."
    reham "I found some spare clothes in this closet. Something not covered in blood and soot for once. They'll need a dusting off, but they should fit."
    scene 85_s5 with dissolve
    mc "This armor is magic-resistant. It's kept me alive."
    scene 85_s4 with dissolve
    reham "It also shouts your name to every guard within a hundred miles."
    scene 85_s5 with dissolve
    mc "...Fine. Show me."
    scene 85_s6 with Fade(0.5,0.5,0.5)
    reham "There. Lift your hands up a little."
    reham "Those laces are looking crooked, let me fix them quick."
    reham "Why don't you come help me, Maia? I can feel your eyes piercing my back."
    scene 85_s7 with dissolve
    if mc_console_maia:
        m "Yes! I'll help."
        scene 85_s10 with dissolve
        m "Not that tight! He won't be able to breath."
        scene 85_s11 with dissolve
        reham "It'll sag if I don't."
        scene 85_s10 with dissolve
        m "What about the pants?"
        scene 85_s11 with dissolve
        reham "Should be fine, but check again."
        scene 85_s8 with Dissolve(1.0)
        reham "There. How does it feel?"
        scene 85_s9 with dissolve
        mc "It's a lot lighter. It'll take some getting used to."
        scene 85_s12 with dissolve
        reham "The previous owner had good taste. An adventurer, perhaps, or a merchant who valued subtlety. It suits you."
        reham "You're ready. Good luck out there, handsome."
        scene 85_s13 with dissolve
        m "Yes... very handsome."
        scene 85_s29 with dissolve
    else:
        m "Y-You got it. I think [mc] is angry at me."
        scene 85_s6 with dissolve
        reham "Aww... I'm sure he doesn't mean it. He's just worried about you."
        scene 85_s8 with Fade(1.5,0.5,0.5)
        reham "There. How does it feel?"
        scene 85_s9 with dissolve
        mc "It's a lot lighter. It'll take some getting used to."
        scene 85_s8 with dissolve
        scene 85_s15 with Dissolve(1.0)
        reham "The previous owner had good taste. An adventurer, perhaps, or a merchant who valued subtlety. It suits you."
        reham "You're ready. Good luck out there, handsome."
        scene 85_s14 with dissolve
    call screen scene85_choice1 with dissolve


label scene85_choice01_op1:
    mc "Come here, Maia."
    scene 85_s19 with Dissolve(1.0)
    m "Mmmmmnn~"
    perception "She rises on her toes, small hands clutching your shirt as she kisses you passionately—lips urgent, soft and sweet, tongue brushing yours with shy boldness."
    scene 85_s13 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss2.mp3" 
    m "Mmmnn... That will last me for now. So you have to come back."
    m "I'll be counting the minutes!"
    scene 85_s12 with dissolve
    reham "*chuckles* You two are so cute."
    scene 85_s29 with dissolve
    jump scene85

label scene85_choice01_op2:
    mc "Come here, Reham."
    if mc_harem_reham:
        if not mc_harem_reham_dom or not mc_harem_reham_dom_dom:
            scene 85_s16 with Dissolve(1.0)
            reham "M-Master? Our contract... personal contact is..."
            scene 85_s17 with dissolve
            mc "It's just a goodbye for luck. Nothing more."
            scene 85_s16 with dissolve
            reham "W-Well... in that case."
            scene 85_s18 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss4.mp3" 
            reham "Mmmmm~"
            sensation "The kiss is slow and reassuring, soft pressure, faint taste of herbs from her work, her body pressing close with quiet need."
            scene 85_s15 with dissolve
            reham "Don't be long. And I won't lie... I enjoyed that kiss, I'd be very sad if it were the last."
            scene 85_s14 with dissolve
        else:
            scene 85_s15 with dissolve
            reham "Gladly."
            scene 85_s18 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss4.mp3" 
            sensation "The kiss is slow and reassuring, soft pressure, faint taste of herbs from her work, her body pressing close with quiet need."
            scene 85_s15 with dissolve
            reham "Mmmmm~ Don't be long or I'll worry, master."
    else:
        scene 85_s16 with Dissolve(1.0)
        reham "[mc]!? W-What are you doing?"
        scene 85_s17 with dissolve
        mc "What's wrong? I'm trying to get a goodbye kiss."
        scene 85_s16 with dissolve
        reham "I'm... I'm really sorry but... *ahem* How about a simple farewell instead?"
        scene 85_s17 with dissolve
        mc "Are you sure?"
        scene 85_s16 with dissolve
        reham "I am. May you return safely. Good luck out there."

    if mc_console_maia:
        if mc_harem_reham:
            scene 85_s20 with Dissolve(1.0)
            m "What about me!"
            scene 85_s21 with dissolve
            mc "*chuckles* You had plenty of love already."
            scene 85_s20 with dissolve
            m "Fine..."
            scene 85_s21 with dissolve
        else:
            scene 85_s20 with Dissolve(1.0)
            m "I wouldn't mind kissing you!"
            scene 85_s21 with dissolve
            mc "*chuckles* You had plenty of love already."
            scene 85_s20 with dissolve
            m "Fine..."
            scene 85_s21 with dissolve
    jump scene85

label scene85_choice01_op3:
    mc "Come here, you two."
    if mc_harem_reham:
        if mc_harem_reham_dom or mc_harem_reham_dom_dom:
            scene 85_s18 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss4.mp3" 
            perception "You pull Reham in first. She gives you a warm and steady kiss. You sense subtle hesitance from it."
            scene 85_s19 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss2.mp3" 
            perception "You go for Maia's lips next. Her kiss is eager, passionate. You sense her devotion clearly."
            scene 85_s29 with Dissolve(1.0)
            empathy "Reham's kiss is grounding, soft lips, gentle pressure, quiet affection. Maia's is fire, urgent tongue, clutching hands, breath mingling hotly."
            scene 85_s12 with dissolve
            reham "*chuckles* Greedy man."
            scene 85_s13 with dissolve
            m "*giggles* I don't mind sharing... this time."
            scene 85_s29 with dissolve
        else:
            scene 85_s16 with Dissolve(1.0)
            reham "M-Master? Our contract... personal contact is..."
            scene 85_s17 with dissolve
            mc "It's just a goodbye for luck. Nothing more."
            scene 85_s16 with dissolve
            reham "W-Well... in that case."
            scene 85_s18 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss4.mp3" 
            reham "Mmmmm~"
            sensation "The kiss is slow and reassuring, soft pressure, faint taste of herbs from her work, her body pressing close with quiet need."
            scene 85_s19 with Dissolve(1.0)
            play sound "se_sfx/blowjob/kiss2.mp3" 
            perception "You go for Maia's lips next. Her kiss is eager, passionate. You sense her devotion clearly."
            scene 85_s29 with Dissolve(1.0)
            empathy "Reham's kiss is grounding, soft lips, gentle pressure, quiet affection. Maia's is fire, urgent tongue, clutching hands, breath mingling hotly."
            scene 85_s12 with dissolve
            reham "*chuckles* Greedy man."
            scene 85_s13 with dissolve
            m "*giggles* I don't mind sharing... this time."
            scene 85_s29 with dissolve
    else:
        scene 85_s16 with Dissolve(1.0)
        reham "[mc]!? W-What are you doing?"
        scene 85_s17 with dissolve
        mc "What's wrong? I'm trying to get a goodbye kiss."
        scene 85_s16 with dissolve
        reham "I'm... I'm really sorry but... *ahem* How about a simple farewell instead?"
        scene 85_s17 with dissolve
        mc "Are you sure?"
        scene 85_s16 with dissolve
        reham "I am. May you return safely. Good luck out there."
        scene 85_s19 with Dissolve(1.0)
        play sound "se_sfx/blowjob/kiss2.mp3" 
        perception "After being rejected, you go for Maia's lips instead. Her kiss is eager, passionate. You sense her devotion clearly."
        scene 85_s12 with Dissolve(1.0)
        reham "*chuckles* Why not kiss her first?"
        scene 85_s13 with dissolve
        m "*giggles* Yes! I will always accept a kiss from you, [mc]!"
        scene 85_s29 with dissolve
    jump scene85

label scene85_choice01_op4:
    if mc_console_maia:
        mc "Goodbye you two. Stay safe, alright?"
        scene 85_s12 with dissolve
        reham "We will. And we'll be waiting."
        scene 85_s13 with dissolve
        m "Come back soon!"
        scene 85_s29 with dissolve
    else:
        mc "I'll be back soon. Take care of Maia for me, alright?"
        scene 85_s15 with dissolve
        reham "Of course, I won't leave my eyes of her for a second."
        scene 85_s14 with dissolve
    jump scene85

label scene85:
    stop music fadeout 1.0 
    scene 85_s22 with Fade(1.3,1.0,1.2)
    play music "ambiance/river_water.mp3" fadein 1.0 volume 0.5 loop
    m "Be careful out there, [mc]!"
    scene 85_s30 with dissolve
    empathy "Her heart tugs heavy, unquestionable in its unconditional love for you. A love born from nothing."
    scene 85_s23 with dissolve
    mc "Stay close to Reham and follow her lead."
    scene 85_s22 with dissolve
    m "I will."
    scene 85_s30 with dissolve
    scene 85_s24 with dissolve
    alex "Ready?"
    mc "Let's ride."
    if mc_princess_alex:
        scene 85_s27 with Dissolve(1.0)
        lewis "It's time for us to leave as well."
        scene 85_s28 with dissolve
        mc "Remember the plan."
        scene 85_s27 with dissolve
        lewis "We won't let you down."
        scene 85_s28 with dissolve
    
    scene 85_s25 with Fade(0.5,0.5,0.5)
    if maia_love >= 70:
        m "[mc]!"
        mc "Hm?"
        scene 85_s26 with Dissolve(1.0)
        ""

label scene86:
    stop music fadeout 1.0 
    scene 86_s1 with Fade(1.3,1.0,1.3)
    play music "nature.mp3" fadein 1.0 loop
    if mc_try_kiss_alex:
        $ alex_love += 10
    if mc_apologize_reham_alex:
        $ alex_love += 10
    alex "Better to avoid the main roads. I'll take a shortcut through the forest—it's rougher, but safer. You'll need to hold on."
    sensation "As you shift closer, a mix of scents hits you. Warm soup from the hideout meal, faint sweet herbs in her hair... and the unmistakable tang of sweat from days on the run."
    call screen scene86_choice1 with dissolve
    
label scene86_choice01_op1:
    $ alex_love -= 10
    $ alex_stinks = True
    mc "You stink."
    scene 86_s2 with dissolve
    alex "Huh!? D-Do I?"
    scene 86_s3 with dissolve
    mc "Yeah. Whatever you're wearing... it's not quite covering it. You need a bath soon."
    scene 86_s2 with dissolve
    alex "I would've if I could! We've been running nonstop—when exactly was I supposed to find an open bath house out here?"
    alex "Is it... really bad? I told Reham about it and she gave me some herbs to mask the smell. I guess they weren't good enough."
    scene 86_s3 with dissolve
    mc "I've smelled worse."
    scene 86_s2 with dissolve
    alex "*sigh* Dammit... this is so embarrassing..."
    alex "I'll take a bath as soon as we're safe. That river next to the hideout, maybe. It's cold as hell, but it'll do if it's this bad."
    scene 86_s3 with dissolve
    mc "Sounds good."
    scene 86_s2 with dissolve
    alex "Umm... even with the smell... you still need to hold on. Don't fall off and make me drag you."
    scene 86_s3 with dissolve
    scene 86_s1 with dissolve
    call screen scene86_choice2 with dissolve

label scene86_choice01_op2:
    mc "..."
    alex "You'll fall if you don't hold on. Last chance."
    call screen scene86_choice2 with dissolve
    

label scene86_choice02_op1:
    scene 86_s4 with Dissolve(1.0)
    sensation "You place your hand firmly on her shoulder. You can feel the tension in her muscles as she guides the horse. It's surprisingly solid under your touch."
    mc "Like this?"
    scene 86_s5 with dissolve
    alex "Uh... Sure? That works."
    scene 86_s4 with dissolve
    mc "Do you work out?"
    scene 86_s5 with dissolve
    alex "Work out? You mean exercise?"
    scene 86_s4 with dissolve
    mc "Yeah."
    scene 86_s5 with dissolve
    alex "Of course. Physical conditioning was mandatory for assassins. Strength, endurance, agility—can't kill if you're winded after a sprint."
    scene 86_s4 with dissolve
    mc "Shows. These shoulders could carry a man."
    scene 86_s6 with Dissolve(1.0)
    alex "Hey! Stop squeezing so hard."
    scene 86_s7 with dissolve
    mc "I'm just admiring those muscles."
    scene 86_s6 with dissolve
    alex "*chuckles* ...Sure."
    scene 86_s7 with dissolve
    scene 86_s13 with Dissolve(2.0)
    ""
    jump scene86_2

label scene86_choice02_op2:
    $ alex_love += 10
    scene 86_s9 with Dissolve(1.0)
    sensation "Your arms slide around her waist. It's warm and firm, a faint tremble as your hands settle."
    scene 86_s8 with dissolve
    alex "H-hey!"
    alex "You seriously couldn't find a more suitable place to grab?"
    scene 86_s9 with dissolve
    mc "You told me to hold on."
    alex "..."
    if mc_try_kiss_alex:
        scene 86_s8 with dissolve
        alex "What is it with you?"
        scene 86_s9 with dissolve
        mc "What do you mean?"
        scene 86_s8 with dissolve
        alex "First you try to kiss me, and now your hands are around my waist like it's nothing."
        alex "Are you... trying to get close to me?"
        scene 86_s9 with dissolve
        mc "What if I am?"
        scene 86_s8 with dissolve
        alex "...Why?"
        scene 86_s9 with dissolve
        mc "Why? Because I see you, Alex. More than the knives and the missions."
        mc "There's more to you than that and I want to know it."
        scene 86_s12 with Dissolve(1.0)
        alex "..."
        scene 86_s13 with Dissolve(2.0)
        perception "A long, heavy silence stretches between you, broken only by the sounds of the forest."
        empathy "Yet, you sense a shift in her posture. The usual rigid tension has softened slightly."
    else:
        scene 86_s10 with dissolve
        alex "That's... ticklish..."
        scene 86_s11 with dissolve
        mc "Oh?"
        scene 86_s10 with dissolve
        alex "*laughs* S-Stop that! Or I swear I'll kick you off!"
        scene 86_s11 with dissolve
        mc "Sorry, sorry..."
        scene 86_s13 with Dissolve(2.0)
        ""
    jump scene86_2

label scene86_2:
    stop music fadeout 1.0 
    scene 86_s14 with Fade(1.0,1.0,1.5)
    play music "ambiance/forest_path.mp3" fadein 3.0 loop
    alex "We should let him rest and drink."
    scene 86_s16 with Fade(1.0,1.0,1.0)
    mc "You didn't give him a name?"
    scene 86_s15 with dissolve
    alex "There's no reason for it. He'll likely be dead soon anyway."
    alex "[mc]..."
    scene 86_s16 with dissolve
    mc "What's up?"
    scene 86_s15 with dissolve
    alex "Do you really believe we'll pull this off?"
    alex "I... haven't slept more than a couple of hours in weeks. It feels like a weight is pressing down on my chest."
    alex "It's... suffocating."
    alex "We're a handful of nobodies against entire nations. The odds are impossible."
    call screen scene86_choice3 with dissolve

label scene86_choice03_op1:
    $ alex_love += 10
    scene 86_s16 with dissolve
    mc "Yes. I believe it with my whole heart."
    scene 86_s15 with dissolve
    alex "How can you be so sure?"
    scene 86_s16 with dissolve
    mc "Because we're not fighting alone. Because the truth is on our side. And because I've seen what happens when good people do nothing."
    mc "We might be outnumbered, but we're not outmatched."
    jump scene86_3

label scene86_choice03_op2:
    scene 86_s16 with dissolve
    mc "I have to believe, Alex. What's the alternative? Giving up?"
    mc "We can't afford to think like that. It's how we lose before we've even begun."
    jump scene86_3

label scene86_choice03_op3:
    scene 86_s16 with dissolve
    mc "Belief is a luxury. We don't have a choice but to succeed."
    scene 86_s15 with dissolve
    alex "That's what terrifies me... there's no room for a single mistake."
    scene 86_s16 with dissolve
    mc "Then we won't make one. We'll be perfect."
    jump scene86_3

label scene86_3:
    scene 86_s15 with dissolve
    alex "And yet... this weight gets heavier whenever I look at you."
    scene 86_s17 with dissolve
    mc "What are you talking about?"
    scene 86_s18 with dissolve
    alex "I don't know. I can't explain it."
    alex "I just feel... scared when I look at you."
    alex "It's like there's something deeply wrong with you."
    scene 86_s17 with dissolve
    mc "Alex..."
    scene 86_s18 with dissolve
    alex "I'm sorry. I shouldn't have said that."
    scene 86_s17 with dissolve
    mc "Do you still feel it now?"
    scene 86_s18 with dissolve
    alex "I do."
    scene 86_s17 with dissolve
    mc "Maybe what you're feeling isn't that something's wrong with me, but that something {i}could{/i} happen to me."
    scene 86_s18 with dissolve
    alex "It's probably nothing. You're a good person, I shouldn't be feeling this way."
    scene 86_s17 with dissolve
    mc "When did this start?"
    scene 86_s18 with dissolve
    alex "The day I met you."
    scene 86_s17 with dissolve
    mc "I... don't understand, why didn't you tell me before?"
    scene 86_s18 with dissolve
    alex "I-"
    play sound "sound_effects/grass.mp3"
    scene 86_s19 with dissolve
    "*rustle* *rustle*"
    scene 86_s20 with dissolve
    ""
    scene 86_s21 with dissolve
    alex "We should keep moving."
    mc "..."
    stop music fadeout 2.0 
    scene 86_s22 with Fade(1.5,1.0,1.5)
    play music "wind.mp3" fadein 1.0 loop
    alex "This is it. Any closer on horseback and we'll risk being spotted."
    alex "I'll come back for you here at midnight. If you're not back by then—"
    mc "I'll be back long before then. If not... I'll leave you a note or something."
    scene 86_s24 with Fade(0.5,0.5,0.5)
    alex "Watch your back. If someone knew your horse was there, they'd be ready to ambush you."

    if alex_stinks:
        alex "Now's a good time to wear that hood. In the meanwhile, I'll see if I can find a body of water to wash this smell... Maybe sniff around for that Kat girl too."
    else:
        alex "Now's a good time to wear that hood. In the meanwhile, I'll see if I can sniff around for that Kat girl too."

    scene 86_s23 with dissolve
    mc "Good luck with that."

    scene 86_s24 with dissolve
    if mc_try_kiss_alex:
        alex "Please... be careful."
        scene 86_s23 with dissolve
        mc "I will. Thank you, Alex."
        scene 86_s24 with dissolve
        alex "Promise me."
        scene 86_s23 with dissolve
        mc "*chuckle* I promise."
        alex "..."
        empathy "For a moment, it looks like she might say something more. Instead, she simply nods and turns back to the horse."

    
    else:
        if mc_princess_alex:
            alex "And be careful. We can't afford to mount another rescue mission."
        else:
            alex "And be careful. A rescue mission now would cost us more than we can spare."
        scene 86_s23 with dissolve
        mc "I will."

    scene 86_s25 with Dissolve(1.3)
    alex "[mc]... one last thing."
    scene 86_s26 with Dissolve(1.0)
    mc "Hm?"
    alex "I'm sorry. For... everything."
    perception "Before you can respond, she's already fading back into the deep shadows of the forest."

label scene87:
    $ karma_more = False
    $ karma_less = False

    scene 87_s1 with Fade(1.0,1.0,1.0)
    mc "(Doesn't seem to be anyone here.)"
    scene 87_s2 with Dissolve(1.0)
    ""
    play sound "sound_effects/woosh2.mp3" volume 0.5
    scene 87_s3 with vpunch
    ""
    scene 87_s4 with Dissolve(0.3)
    play sound "sound_effects/bodydrop3.mp3"
    scene 87_s4 with vpunch
    mc "Hagh—!"
    scene 87_s5 with Dissolve(0.2)
    play sound "sound_effects/bodydrop4.mp3"
    scene 87_s5 with vpunch
    stop music fadeout 1.0 
    mc "What the—!?"
    play music "side_event7.mp3" fadein 1.0 loop
    lena_ "Hah! You've got some nerve coming back here, [mc]. I love it!"
    lena_ "Thought you'd be ten feet tall with how folk talk about you."
    scene 87_s29 with Dissolve(1.0)
    mc "Nghnn!"
    sensation "You thrash, but her thighs squeeze tighter, solid as iron. Your skull feels like popping open like a watermelon."
    scene 87_s7 with dissolve
    lena_ "Easy, boy. The harder you fight, the worse your headache's gonna be tomorrow."
    scene 87_s6 with dissolve
    mc "Dammit! I should've been more careful!"
    scene 87_s7 with dissolve
    lena_ "Just stay still and listen."
    scene 87_s6 with dissolve
    mc "L-Listen to what? Who are— Ngh! ...you!?"
    scene 87_s7 with dissolve
    lena_ "Calm your shit down. I ain't one of the guards or those shiny new army brats."
    scene 87_s6 with dissolve
    mc "Then let me go!"
    scene 87_s7 with dissolve
    lena_ "I will. When I'm sure you're not gonna to do something stupid, like poke me. Nod if you understand."
    scene 87_s6 with dissolve
    mc "...Fine. I understand."
    scene 87_s7 with dissolve
    lena_ "First question. You're the one they call [mc], right? The one who made Gaius bleed?"
    scene 87_s6 with dissolve
    mc "What's it to you?"
    scene 87_s7 with dissolve
    lena_ "Answer the question."
    scene 87_s30 with Dissolve(1.0)
    perception "She shifts her weight, still pinning you, but now you catch a glimpse of her face: pointed ears, sharp eyes, a smirk."
    mc "Yes. That was me."
    scene 87_s31 with dissolve
    lena_ "And you're back here, skulking around the city stables. Why?"
    scene 87_s30 with dissolve
    mc "I left something I need."
    scene 87_s31 with dissolve
    lena_ "Describe this {i}thing.{/i}"
    scene 87_s30 with dissolve
    mc "It's a black mare. With white hooves."
    scene 87_s31 with dissolve
    lena_ "Well fuck me, it is you... I've been waiting for you."
    scene 87_s30 with dissolve
    mc "Waiting for me? Who are you?"
    scene 87_s31 with dissolve
    lena "The name's Lena. And I'm... well, {i}we{/i} are the reason there's no guard patrol surrounding this whole place right now. I did you a favor. Now we're gonna to talk about you doing one for me."
    scene 87_s30 with dissolve
    mc "I don't do favors for people who try to crack my skull open!"
    scene 87_s31 with dissolve
    lena "Would you have stopped to chat if I'd just stepped out and said hello? A man on the run?"
    scene 87_s30 with dissolve
    mc "...Probably not."
    scene 87_s7 with dissolve
    lena "See? Practical. Now, are you just gonna lie there and keep being squeezed between my thighs, or can we have a real conversation like two adults?"
    scene 87_s29 with dissolve
    call screen scene87_choice1 with dissolve

label scene87_choice01_op1:
    $ mc_likes_thigh_squeeze = True
    scene 87_s6 with dissolve
    mc "I actually don't mind it! In fact, I would go as far as to say that I might want to stay like this a little longer!"
    scene 87_s7 with dissolve
    lena "Don't tell me you're one of those men that get off on this shit? Getting beat up and degraded by a woman and whatnot."
    scene 87_s6 with dissolve
    mc "What if I am!?"
    scene 87_s7 with dissolve
    lena "*laughs* Hell no! I need to get off before you start creaming your panties."
    jump scene87_2

label scene87_choice01_op2:
    scene 87_s6 with dissolve
    mc "You first. Get off."
    jump scene87_2

label scene87_2:
    scene black with dissolve
    play sound "sound_effects/body/clothes1.mp3"
    scene 87_s8 with Fade(0.5,0.5,1.0)
    sensation "You gasp for air as she finally releases you. She then pulls back her hood, revealing a wild face that's all sharp angles and amusement."
    scene 87_s14 with Dissolve(1.0)
    lena "Take a deep breath. Slowly."
    scene 87_s13 with dissolve
    call screen scene87_choice2 with dissolve

label scene87_choice02_op1:
    $ mc_punch_lena = True
    scene 87_s9 with Dissolve(0.8)
    perception "You charge, feinting high with the stump of your missing hand before driving the real strike toward her head."
    lena "Wanna fight? I'll give you a figh—"
    scene 87_s10 with dissolve
    lena "W-Wait, wha—!"
    scene 87_s11 with Dissolve(0.3)
    play sound "sound_effects/punch.mp3"
    scene 87_s11 with vpunch
    lena "Ghah!"
    scene 87_s12 with dissolve
    lena "Ptoo. Fuck me... Haha! I can't believe I fell for that."
    mc "Don't mess with me."
    lena "Alright, alright! I surrender."
    lena "I wasn't trying to hurt you. I promise."
    mc "You're doing a terrible job of showing that."
    lena "Like I said, I only wanted to a conversation. I just needed to make sure you'd actually have it."
    lena "And damn... I'm impressed so far. That punch would've easily knocked me out if you didn't hold back."
    mc "You better start talking."
    scene 87_s14 with Dissolve(1.5)
    lena "*ahem* A girl works here. Serena. You met her. Sweet girl, terrible judge of character. She was sure you'd come back for your horse."
    jump scene87_3

label scene87_choice02_op2:
    mc "*cough* ...You said you were waiting for me. How? Start talking."
    mc "I don't think you're here to arrest me. Otherwise I feel like I'd have been long gone."
    scene 87_s14 with dissolve
    lena "Like I said, I want a conversation. But I needed to make sure you'd actually have it."
    scene 87_s13 with dissolve
    mc "You could've just asked instead of trying to break my neck..."
    scene 87_s14 with dissolve
    lena "Where's the fun in that? Besides—I wanted to see if you were as tough as they say."
    lena "Color me disappointed, but you held out longer than most. That counts for something."
    lena "Anyway, a girl works here. Serena. You met her. Sweet girl, terrible judge of character. She was sure you'd come back for your horse."
    jump scene87_3

label scene87_3:
    lena "She's been hiding it, moving it, falsifying the logs. For you."
    scene 87_s13 with dissolve
    mc "Serena? Why would she do that?"
    scene 87_s14 with dissolve
    lena "Because she's a kind person. A trait that's currently getting her crushed."
    lena "Follow me. Let's get in inside."
    scene 87_s13 with dissolve
    stop music fadeout 1.0 
    scene 87_s15 with Fade(1.5,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    lena "Serena! Come on out, sweetheart. Don't make me yell twice."
    if mc_liked_tits:
        scene 87_s16 with Dissolve(1.0)
    elif mc_liked_ass:
        scene 87_s17 with Dissolve(1.0)
    else:
        scene 87_s16 with Dissolve(1.0)

    if mc_punch_lena:
        selene "Yes, mother? ...Wh-What's with the bruise?"
        lena "This guy's work. It's gonna sting for a while."
    else:
        selene "Yes, mother?"

    selene "[mc]! He's here!"
    mc "..."
    lena "[mc]?"
    scene 87_s32 with vpunch
    mc "Yes, I'm here! ...Wait, did she just call you mother!?"
    scene 87_s19 with dissolve
    lena "*laughs* I know, right? Shocking. I don't look a day over ninety, do I?"
    scene 87_s33 with dissolve
    if mc_likes_thigh_squeeze:
        lena "Well, there he is, hon. He's similar to what you described, except you missed the part where he liked getting crushed between women's thighs."
    else:
        lena "Well, there he is, hon. Tell him your plan."
    scene 87_s32 with dissolve
    mc "...Serena. Your mother has an interesting way of introducing herself."
    scene 87_s18 with dissolve
    selene "I'm so sorry. She's very serious about safety and all that. She means well. Really."
    scene 87_s32 with dissolve
    mc "Serena, you look..."
    scene 87_s19 with dissolve
    lena "Miserable? Right. You're not wrong. Doesn't suit her at all."
    lena "She's usually the most annoyingly cheerful person you'll ever meet. It's honestly exhausting."
    scene 87_s32 with dissolve
    mc "What's gotten her so down? What's going on?"
    scene 87_s21 with dissolve
    stop music fadeout 1.0 
    selene "..."
    play music "tense/tention2.mp3" fadein 1.0 loop
    scene 87_s20 with dissolve
    lena "What's going on is that under Avery's new 'labor reforms,' servants with debt can be bound to their masters. Indefinitely."
    lena "Serena's old contract got burned. Now she belongs to the master of these stables. Can't leave, can't refuse any work, can't even keep a single copper of her own wages."
    scene 87_s21 with dissolve
    mc "That's... horrible. He basically owns her now."
    scene 87_s20 with dissolve
    lena "Call it what it is, then. She's a slave. And I'm getting her out."
    lena "Otherwise, travelling to this city in particular would've been for nothing."
    scene 87_s21 with dissolve
    mc "So what do you need from me?"
    scene 87_s20 with dissolve
    lena "*scoff* Look, [mc]. I ain't gonna sugarcoat it. my plan is straightforward. I find the man who holds her papers. I kill him. Then everything's good again."
    scene 87_s22 with dissolve
    selene "It's not a plan, it's a death wish! Idiot! Idiot! Idiot!"
    selene "You can't come back into my life so suddenly and leave!"
    scene 87_s34 with dissolve
    mc "She's right. I wouldn't call that a plan."
    scene 87_s35 with dissolve
    lena "Ahuh. She ain't too fond of my idea, as you can see. But..."
    lena "She's been clinging to this idea that you might be the alternative. The man who faced down Gaius and walked away. The man who's got Avery's people nervous."
    lena "She basically thinks you have nothing else to loose."
    scene 87_s36 with dissolve
    mc "I have plenty to lose, Serena."
    scene 87_s37 with dissolve
    selene "I'm not asking for a... a murder. I'm asking for a solution. Mother sees everything as a nail because she only has a hammer."
    selene "I hid your horse because I saw that. I thought... maybe you could see a way here, too."
    scene 87_s33 with dissolve
    lena "You hold too much faith in people, hon."
    lena "Let me do it my way. We don't need to ask anyone for help."
    scene 87_s36 with dissolve
    mc "And if you die? She'd be worse off than before. You said you wanted a favor. What, exactly, are you asking me for?"
    scene 87_s38 with dissolve
    lena "I... don't know anymore. I'm at my wits' end. If she hadn't stopped me, I'd already be out there with a sword."
    scene 87_s37 with dissolve
    selene "Please, [mc]. I don't want Mother hurt. She's rough... she left when I was young... but she's still my mother."
    scene 87_s33 with dissolve
    lena "I didn't leave, sweetheart. Elves... time moves different for us. A 'walk' for me was years for you. I thought you'd be safer without a wandering rogue for a mother."
    scene 87_s22 with dissolve
    selene "I don't want to hear anymore of that. Besides... it doesn't matter now. What happened has happened."
    scene 87_s36 with dissolve
    mc "Are you going to tell the guards about me if I don't help?"
    scene 87_s38 with dissolve
    lena "I ain't no filthy snitch. Fuck Avery—I'd burn the city down to see her fall."
    scene 87_s36 with dissolve
    mc "..."
    scene 87_s38 with dissolve
    lena "Doesn't matter to me anyway. I'll gut that pig myself, with or without help. Either I kill him or die trying."
    scene 87_s22 with dissolve
    selene "No! Stop saying that, please! I... I need you."
    scene 87_s34 with dissolve
    call screen scene87_choice3 with dissolve

label scene87_choice03_op1:
    $ mc_want_help_serena = True
    scene 87_s36 with dissolve
    mc "Both of you, just... calm down. I'll think about it."
    mc "What happened to Serena was terrible and unjust but I can't rush into danger with my current circumstances."
    scene 87_s38 with dissolve
    lena "Think about it? This ain't a philosophy debate. It's a yes or no."
    scene 87_s36 with dissolve
    mc "I don't even know where the man lives. If I'm even considering it, I need to know what I'm walking into."
    scene 87_s38 with dissolve
    lena "Fine, ask away."
    scene 87_s36 with dissolve
    call screen scene87_choice4 with dissolve

label scene87_choice04_op1:
    $ scene87_live = True
    mc "Where does he live? Not just the district. The house, the streets around it."
    scene 87_s38 with dissolve
    lena "Greyleaf. Big stone manor with a wrought-iron fence shaped like vines. I never expected someone with that wealth to live in that shithole of a district."
    scene 87_s36 with dissolve
    mc "Security?"
    scene 87_s38 with dissolve
    lena "Two at the front gate, lazy-looking but armed. A patrol walks the perimeter every half-hour. More inside, I'd wager. But the back garden wall... there's barely anyone that goes there."
    scene 87_s36 with dissolve
    mc "How do you know all this?"
    scene 87_s38 with dissolve
    lena "I've been watching. For about a week."
    scene 87_s36 with dissolve
    call screen scene87_choice4 with dissolve

label scene87_choice04_op2:
    $ scene87_describe = True
    mc "Describe him to me."
    scene 87_s38 with dissolve
    lena "He's a bloated tick of a man. With a beard he thinks makes him look dignified. It doesn't."
    lena "Trust me, you'll know him when you see him."
    scene 87_s37 with dissolve
    selene "He always... smiles weirdly at me. It makes my skin crawl."
    scene 87_s32 with dissolve
    call screen scene87_choice4 with dissolve

label scene87_choice04_op3:
    $ scene87_ask_prize = True
    mc "What's in this for me? If I help, what's my prize?"
    scene 87_s19 with dissolve
    lena "Straight to the price tag, huh? I don't blame you. His manor will be full of valuables. You can take your pick after he's dead. Coin, jewels, whatever you can carry."
    scene 87_s22 with dissolve
    selene "Mother!"
    scene 87_s23 with dissolve
    lena "What? He asked. Besides, he gets to be the hero who saved a poor girl from slavery. That's worth something, ain't it?"
    scene 87_s38 with dissolve
    lena "Or does your conscience only speak gold?"
    scene 87_s36 with dissolve
    call screen scene87_choice4 with dissolve
    
label scene87_choice04_op4:
    mc "That's all I need to know for now."
    if not scene87_ask_prize:
        scene 87_s38 with dissolve
        lena "Really? You won't ask about something in return?"
        scene 87_s36 with dissolve
        mc "I won't. Seeing Serena happy again is prize enough."
        scene 87_s38 with dissolve
        lena "Hah! Alright, hero. I'm sorry I judged you terribly before. You really are a good person."
        scene 87_s37 with dissolve
        selene "You're really going to help?"
    else:
        scene 87_s37 with dissolve
        selene "You're really going to help?"

    scene 87_s36 with dissolve
    mc "I'm not promising anything. But I'll try my best."
    mc "For now I need my horse. And I have to be somewhere by midnight."
    scene 87_s38 with dissolve
    lena "You want us to wait?"
    scene 87_s36 with dissolve
    mc "Yes. Can you wait till at least tomorrow or after, Serena?"
    scene 87_s37 with dissolve
    selene "I can!"
    scene 87_s36 with dissolve
    mc "Good. Keep your mother on a leash, she's the one I'm worried about."
    scene 87_s19 with dissolve
    lena "*chuckles* Fine. I'll wait. Your horse is in the last stall on the right. Saddled and ready."
    scene 87_s37 with dissolve
    selene "Thank you, [mc]. Just for listening."
    scene 87_s32 with dissolve
    mc "Don't thank me yet. Get some rest, Serena. You look like you need it."
    mc "If everything goes well, I'll meet you two here tommorrow or after at dawn. Sounds good?"
    scene 87_s19 with dissolve
    lena "Don't make me regret this, [mc]."
    scene 87_s32 with dissolve
    scene 87_s24 with Dissolve(2.0)
    perception "As you turn to leave, you see Serena offer you a small, fragile smile, the first spark of hope you've seen in her eyes today."
    jump scene87_4

label scene87_choice03_op2:
    $ mc_want_help_serena = False
    mc "I can't afford to attract more trouble right now. My plate is already overflowing, and people are depending on me."
    selene "..."
    scene 87_s37 with dissolve
    selene "I... I understand. Thank you for listening, [mc]."
    scene 87_s36 with dissolve
    mc "I'm sorry, Serena. What's happening to you is wrong."
    scene 87_s38 with dissolve
    lena "Sorry doesn't fill a belly or buy freedom. Your horse is in the last stall. Just take it and go."
    scene 87_s36 with dissolve
    mc "You two should think more about it. Especially you, Lena. Don't leave your daughter alone."
    lena "..."
    scene 87_s25 with Dissolve(2.0)
    empathy "As you turn to leave, Lena places a firm but comforting hand on Serena's trembling shoulder. The conversation is over."

    jump scene87_4

label scene87_4:
    stop music fadeout 1.0 
    scene 87_s26 with Fade(0.5,0.5,0.5)
    play music "wind.mp3" fadein 1.0 loop
    mc "Miss me, girl?"
    mc "Let's get you out of here before any guards come wandering in."
    scene black with dissolve
    stop music fadeout 1.0 
    scene 87_s27 with Fade(1.0,1.0,1.5)
    play music "nature.mp3" fadein 1.0 loop
    mc "Stay here. I'll be back for you soon."
    horse "Neigh!"
    mc "Ah, right... I'm sorry for leaving you so long, [horse]. I'll make it up to you, promise."
    scene 87_s28 with Dissolve(1.0)
    mc "Would you look at that... It's still here after all this time."
    mc "I got a brand new sword now so I don't need it. Alex or Reham will make better use of it. Hold on to it a bit longer, alright? I'm supposed to do this quietly afterall."

label scene88:
    stop music fadeout 1.0 
    scene 88_s1 with Fade(1.5,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    mc "(Dammit, of course the gate's going to be crawling with guards. What was I thinking?)"
    mc "(What now?)"
    play sound "sound_effects/horse_cart.mp3"
    scene 88_s2 with Dissolve(1.0)
    mc "(Perfect timing.)"
    stop sound fadeout (1.0)
    play sound "sound_effects/running_grass.mp3"
    scene 88_s3 with Fade(0.5,1.3,0.5)
    mc "(The carriage stopped, now's my chance!)"
    play sound "sound_effects/body/wood_creak.mp3" volume 0.5
    scene 88_s4 with Fade(0.5,3.0,1.0)
    stop sound
    mc "(Phew. I'm getting some flashbacks...)"
    stop sound
    guard "Halt!"
    scene 88_s5 with Dissolve(1.0)
    guard "What's the load?"
    merchant "Grapes and wines galore, sir. And a few barrels of last season's red. A fine vintage, care for a taste?"
    guard "Open that one."
    scene 88_s6 with Dissolve(1.0)
    mc "(Shit!)"
    merchant "All these new rules... pain in the arse, if you'll pardon me saying."
    scene 88_s7 with dissolve
    guard "Clear. Move on."
    scene 88_s6 with dissolve
    merchant "Tch. City's gone mad, I tell ya."
    scene 88_s7 with dissolve
    guard "Move along. Now."

    scene 88_s4 with Dissolve(1.0)
    ""
    stop music fadeout 1.0
    scene 88_s9 with Fade(1.0,1.0,1.0)
    merchant "Delivery for Relis Winery!"
    merchant "Haulers'll be right with you."
    mc "(Far enough. Time to go.)"
    scene 88_s10 with Fade(1.0,1.0,1.5)
    ""
    play music "ambiance/story.mp3" fadein 1.0 loop
    scene 88_s11 with Dissolve(1.0)
    mc "(Hmm? There's a huge crowd gathered here.)"
    scene 88_s15 with Dissolve(1.0)
    storyteller "And there he stood—the wanderer fallen from grace, facing none other than Gaius the Unbroken! Champion of a hundred wars!"
    scene 88_s12 with dissolve
    grumpy_dwarf "*snort* Gaius? {i}The{/i} Gaius? No one messes with him and lives to talk about it. Man's cracked in the head."
    scene 88_s16 with dissolve
    storyteller "Aye, the very same! He towered over the wanderer like an oak over a sapling, his greatsword longer than a man is tall, the sun flashing off his dented armor!"
    scene 88_s17 with dissolve
    storyteller "Gaius charged like thunder, blade whistling death! But the wanderer! Oh, the wanderer danced aside like autumn leaves in a gale! And struck true! First blood staining the flowers, painting them crimson!"
    scene 88_s12 with dissolve
    grumpy_dwarf "First blood? Against Gaius? Stop talking outta your ass."
    scene 88_s18 with dissolve
    storyteller "By my mother's honor! Again and again they clashed! Sparks flying, steel biting steel! Gaius roared, a sound fit to shake the mountains themselves! But the wanderer pressed on, relentless, a storm wearing a man's skin!"
    scene 88_s13 with dissolve
    snarky_dwarf "And then he flew off on a dragon, yeah?"
    scene 88_s14 with dissolve
    perception "Laughter ripples through the crowd. A few people shake their heads as they drift away."
    scene 88_s19 with dissolve
    storyteller "Nay, my lady! With one final slash, the wanderer was driven back... wounded, but alive! And Gaius... Gaius still stands unbroken, his title intact."
    scene 88_s20 with Dissolve(1.0)
    orym "That 'wanderer' is probably rotting in a ditch somewhere. No way he was let go that easily."
    orym "Regardless, with that fool gone, the princess is open for marriage again. Grieving. In desperate need of a man's touch. A {i}real{/i} man."
    scene 88_s21 with dissolve
    snarky_dwarf "*laughs* As if she'd ever look twice at a knife-eared browless fuck like you."
    scene 88_s22 with dissolve
    orym "Shut it, gnome! Watch your tongue or I'll cut it off."
    scene 88_s23 with Dissolve(1.0)
    grumpy_dwarf "Bah! What a load of ogre-piss. Shoulda listened to that lusty lady bard."
    perception "The crowd slowly dissipates until only you and the storyteller remain."
    call screen scene88_choice01 with dissolve

label scene88_choice01_op1:
    play sound "sound_effects/metal_clink.mp3"
    scene 88_s24 with Dissolve(1.0)
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    perception "You toss a copper coin into the small wooden box with a genuine smile."
    scene 88_s25 with Dissolve(1.0)
    storyteller "Ah! A connoisseur of the arts! You, sir, have the soul of a poet!"
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 88_s26 with dissolve
    mc "I enjoyed the story. Don't let them get to you."
    scene 88_s23 with dissolve
    storyteller "But of course. Tis the life of a storyteller. Folks laugh, scoff, walk away—but the stories remain, even when they don't."
    scene 88_s27 with dissolve
    storyteller "May the road be kind to you, sir!"
    scene 88_s28 with dissolve
    jump scene89

label scene88_choice01_op2:
    scene 88_s26 with dissolve
    mc "That's quite a story, how did you hear about it?"
    scene 88_s23 with dissolve
    storyteller "Tales travel, my friend. On the breath of the wind, in the whispers of traders, in the excuses of soldiers trying to explain the inexplicable."
    scene 88_s26 with dissolve
    mc "I couldn't help but notice that some of your details are off."
    scene 88_s27 with dissolve
    storyteller "Of course they are. It is my rule—as a storyteller, nay, as an {i}artist{/i}, to fill the gaps. To give shape where memory falters."
    storyteller "To turn an event into a legend meant to outlive those who witnessed it."
    scene 88_s28 with dissolve
    mc "So it isn't completely true."
    scene 88_s27 with dissolve
    storyteller "Is a river true? It changes with every bend, yet it remains the same river. A man defied a giant and the giant bled. I merely built the cathedral around it."
    scene 88_s28 with dissolve
    mc "I see. I should be going. Good luck to you."
    scene 88_s27 with dissolve
    storyteller "Farewell, sir!"
    scene 88_s28 with dissolve
    jump scene89

label scene88_choice01_op3:
    scene 88_s29 with dissolve
    mc "(At least someone's finding joy in my misery.)"
    scene black with Fade(0.5,0.5,0.5)
    perception "You shake your head, the storyteller's vivid words echoing in your mind as you continue moving through the empty allyways."
    jump scene89

label scene89:
    stop music fadeout 1.0 
    $ yuuhi_love == 0
    scene 89_s1 with Fade(1.5,1.0,1.3)
    play music "wind.mp3" fadein 1.0 loop
    mc "(Good thing it's tucked away like that.)"
    play sound "sound_effects/doors/door_open2.mp3"
    scene 89_s2 with dissolve
    dean "Bring me two iron billets and a sack of charcoal. Be careful with both. They're heavy."
    yuuhi "Would you please stop treating me like I'm still ten? I've got it."
    scene 89_s3 with Dissolve(1.0)
    yuuhi "Execuse me."
    mc "..."
    scene 89_s4 with Dissolve(1.0)
    yuuhi "Two iron billets... and one sack of charcoal."
    call screen scene89_choice01 with dissolve

label scene89_choice01_op1:
    scene 89_s34 with Dissolve(1.4)
    mc "Hey, Yuuhi."
    scene 89_s18 with vpunch
    yuuhi "Ahh!"
    yuuhi "Who—?"
    scene 89_s8 with dissolve
    yuuhi "[mc]! Y-You're... you're alive!"
    play music "side_event6.mp3" fadein 3.0 loop
    if mc_harem_yuuhi:
        scene 89_s10 with Dissolve(0.2)
        play sound "sound_effects/clothing_rustle.mp3"
        scene 89_s10 with vpunch
        sensation "She drops whatever she's holding and throws her arms around you, hugging tight as she kisses you. The warmth of her lips quickly chases the cold from your skin."
        scene 89_s11 with Dissolve(1.0)
        yuuhi "I thought... everyone said you were dead, or captured, or..."
        scene 89_s12 with dissolve
        mc "It would take more than that to keep me down."
        scene 89_s11 with vpunch
        yuuhi "You idiot! Why didn't you send word? I've been worried sick!"
        yuuhi "Don't ever scare me like that again!"
        scene 89_s12 with dissolve
        mc "I'm afraid I'll be giving you lots of scares from now on."
    else:
        yuuhi "I thought... everyone said you were dead, or captured, or..."
        scene 89_s9 with dissolve
        mc "It would take more than that to keep me down."
        scene 89_s8 with dissolve
        yuuhi "You got into some awfully serious trouble. Why are you coming back here? It's not safe."
        yuuhi "D-Don't worry, I won't tell on you. Whatever you did, I'm sure you did it for a good reason. You're not a bad person as the guards say."
        scene 89_s9 with dissolve
    jump scene89_2

label scene89_choice01_op2:
    $ scene89_yuuhi_spank = True
    scene 89_s5 with Dissolve(1.4)
    perception "You move silently, heart racing with mischief. The angle is perfect, her guard down, focused on the crates."
    yuuhi "*whisteling*"
    play sound "sound_effects/slap04.mp3"
    scene 89_s6 with vpunch
    sensation "Your palm connects with a firm smack, sharp sound echoing off the stone wall, her body jolting forward in surprise."
    yuuhi "Ahhn!"
    scene 89_s7 with dissolve
    yuuhi "What the-!?"
    if mc_harem_yuuhi:
        yuuhi "S-Stupid pervert! I will let you know that I already have a boyfriend and he'll beat you up!"
    else:
        yuuhi "S-Stupid pervert! My pops will make short work of you once I call him!"
    scene 89_s8 with dissolve
    yuuhi "You! You... You?"
    yuuhi "[mc]! Y-You're... you're alive!"
    play music "side_event6.mp3" fadein 3.0 loop
    if mc_harem_yuuhi:
        scene 89_s10 with Dissolve(0.2)
        play sound "sound_effects/clothing_rustle.mp3"
        scene 89_s10 with vpunch
        sensation "She drops whatever she's holding and throws her arms around you, hugging tight as she kisses you. The warmth of her lips quickly chases the cold from your skin."
        scene 89_s11 with Dissolve(1.0)
        yuuhi "I thought... everyone said you were dead, or captured, or..."
        scene 89_s12 with dissolve
        mc "It would take more than that to keep me down."
        scene 89_s11 with vpunch
        yuuhi "You idiot! Why didn't you send word? I've been worried sick!"
        yuuhi "And that's how you say hello now? Pervert."
        scene 89_s12 with dissolve
        mc "Missed me that much?"
        scene 89_s11 with dissolve
        yuuhi "Shut up..."
        scene 89_s12 with dissolve
    else:
        yuuhi "I thought... everyone said you were dead, or captured, or..."
        scene 89_s9 with dissolve
        mc "It would take more than that to keep me down."
        scene 89_s8 with dissolve
        yuuhi "You got into some awfuly serious trouble. Why are you coming back here? It's not safe."
        yuuhi "D-Don't worry, I won't tell on you. Whatever you did, I'm sure you did it for a good reason. You're not a bad person as the guards say."
        scene 89_s9 with dissolve
    jump scene89_2

label scene89_2:
    dean "Yuuhi? Everything all right out there?"
    
    if mc_harem_yuuhi:
        scene 89_s13 with dissolve
        if scene89_yuuhi_spank:
            yuuhi "It's fine, Pops! Just... someone that I hold dear. Very, very dearly. And he's being insufferable."
        else:
            yuuhi "It's fine, Pops! Just... someone that I hold dear."
    else:
        scene 89_s35 with dissolve
        yuuhi "It's fine, Pops! Just... an old friend."

    if mc_harem_yuuhi:
        scene 89_s11 with dissolve
        yuuhi "Come on, let's get you inside before someone—"
        scene 89_s14 with dissolve
        yuuhi "Oh... oh my..."
        yuuhi "[mc]... y-your arm..."
        scene 89_s15 with dissolve
        mc "*chuckles* Finally noticed? Yeah, it's been missing for a while."
        scene 89_s14 with dissolve
        yuuhi "Hahh... H-How? When did this happen?"
        scene 89_s15 with dissolve
        mc "During my escape from the city. My farewell wasn't a peaceful one."
        scene 89_s14 with dissolve
        yuuhi "Oh Gods... I'm... I'm so sorry!"
        scene 89_s15 with dissolve
        mc "You have nothing to be sorry for. It's actually part of the reason I'm here."
        scene 89_s14 with dissolve
        yuuhi "You... you want me to help you look for it?"
        scene 89_s15 with dissolve
        mc "No, not that. I've made peace with its absence. I was thinking about what comes next. A prosthetic."
        scene 89_s14 with dissolve
        yuuhi "A prosthetic..."
        scene 89_s15 with dissolve
        mc "You helped make my armor. You understand how these things work, how something needs to move with a body. I thought you'd be the right person to ask."
        scene 89_s11 with dissolve
        yuuhi "*sigh* [mc], I don't know... This isn't a greave or a gauntlet. This is... this is a part of you."
        yuuhi "L-Let's get inside for now. It's too open out here."
        scene 89_s12 with dissolve
        mc "You sure your father will be alright with a fugitive in his smithy? I heard he's a loyal man."
        scene 89_s11 with dissolve
        yuuhi "Loyal to the Crown. To the Queen. Not to Avery and her thugs."
        yuuhi "Pop's been... vocal. I've had to cover his mouth more than once whenever guards passed by. Otherwise he would end up in the dungeon for the things he's been saying."
        scene 89_s12 with dissolve
        mc "*chuckles* He's a good man then."
        scene 89_s11 with dissolve
        yuuhi "He is. Now come on. And try to look like a customer with a very... {i}odd{/i} request."
        scene 89_s12 with dissolve

    else:
        scene 89_s8 with dissolve
        yuuhi "Come on, let's get you inside before someone—"
        scene 89_s17 with dissolve
        yuuhi "Oh... oh my..."
        yuuhi "[mc]... y-your arm..."
        mc "*chuckles* Finally noticed? Yeah, it's been missing for a while."
        yuuhi "Hahh... H-How? When did this happen?"
        mc "During my escape from the city. My farewell wasn't a peaceful one."
        yuuhi "Oh Gods... I'm... I'm so sorry!"
        mc "You have nothing to be sorry for. It's actually part of the reason I'm here."
        scene 89_s18 with dissolve
        yuuhi "You... you want me to help you look for it?"
        scene 89_s19 with dissolve
        mc "No, not that. I've made peace with its absence. I was thinking about what comes next. A prosthetic."
        scene 89_s18 with dissolve
        yuuhi "A prosthetic..."
        scene 89_s19 with dissolve
        mc "You helped make my armor. You understand how these things work, how something needs to move with a body. I thought you'd be the right person to ask."
        scene 89_s18 with dissolve
        yuuhi "*sigh* [mc], I don't know... This isn't a greave or a gauntlet. This is... this is a part of you."
        yuuhi "L-Let's get inside for now. It's too open out here."
        scene 89_s19 with dissolve
        mc "You sure your father will be alright with a fugitive in his smithy? I heard he's a loyal man."
        scene 89_s18 with dissolve
        yuuhi "Loyal to the Crown. To the Queen. Not to Avery and her thugs."
        yuuhi "Pop's been... vocal. I've had to cover his mouth more than once whenever guards passed by. Otherwise he would end up in the dungeon for the things he's been saying."
        scene 89_s19 with dissolve
        mc "*chuckles* He's a good man then."
        scene 89_s18 with dissolve
        yuuhi "He is. Now come on. And try to look like a customer with a very... {i}odd{/i} request."
        scene 89_s19 with dissolve

    stop music fadeout 1.0 
    scene 89_s20 with Fade(1.0,1.0,1.0)
    play music "blacksmith2.mp3" fadein 1.0 loop
    dean "What took you so long? And who's this? Even after I put a sign on that door, customers still find their way here..."
    scene 89_s21 with dissolve
    yuuhi "This isn't a customer, Pops. This is [mc]. You remember? The man you slammed the great club into."
    scene 89_s20 with dissolve
    dean "{i}The{/i} [mc]?"
    scene 89_s22 with Dissolve(1.0)
    mc "In the flesh."
    scene 89_s23 with dissolve
    dean "Son, are you aware the entire garrison is looking for you?"
    scene 89_s22 with dissolve
    mc "I know. Thank you for having me."
    scene 89_s23 with dissolve
    dean "I assume you're not just here to reminisce about the past. And you're not here for standard repairs. Not with half the city watch looking for you."
    scene 89_s22 with dissolve
    mc "I'm not."
    yuuhi "Mhm. Your face is plastered on every notice board."
    scene 89_s23 with dissolve
    dean "And you came to my door. Which means you need something only I and my daughter can provide. And you're desperate enough to walk into the fire to ask for it."
    scene 89_s24 with Dissolve(1.0)
    mc "I need a new hand."
    scene 89_s25 with dissolve
    dean "I see. A simple request. Forged in secrecy, fitted to a fugitive with a bounty in gold over his head."
    dean "Tell me, [mc]. Why should I light my forge for you? Why should I put my daughter, my shop, at risk?"
    scene 89_s24 with dissolve
    mc "Because the person who put the price on my head is the same one who betrayed the Crown. I'm not just running. I'm working to expose Magistrate Avery."
    scene 89_s25 with dissolve
    dean "Expose her for what?"
    scene 89_s24 with dissolve
    mc "For the murder of the Queen."
    scene 89_s26 with dissolve
    yuuhi "Wh-What!?"
    scene 89_s27 with dissolve
    mc "Avery was responsible for the Queen's death. She lied to everyone to the guards, to city, to everyone who loved the Queen."
    if mc_save_queen:
        mc "The Queen didn't die at sea. She was supposed to be assassinated. She escaped."
        mc "Avery and Reiner of Eurina orchestrated the whole plot. Her 'death' was a lie to seize power over Irda and quietly hand it over to Eurina."
    else:
        mc "The Queen didn't die at sea. She was assassinated. The plot was orchestrated by Avery and Reiner of Eurina."
        mc "Her 'tragic loss' was a lie to seize power over Irda and quietly hand it over to Eurina."
    scene 89_s26 with dissolve
    yuuhi "Gods... Her Majesty..."
    scene 89_s23 with dissolve
    dean "That is a staggering accusation. How do I know you're not just spinning a tale to save your skin?"
    scene 89_s22 with dissolve
    mc "If I only wanted to save my skin, I'd be overseas by now. I came back. I'm telling you this so you know what you're risking for. Not just for me."
    scene 89_s29 with dissolve
    dean "Hmm..."

    if mc_take_off_pants_yuuhi or mc_ask_yuuhi_pussy or scene89_yuuhi_spank:
        yuuhi "Father, please. [mc] is a pervert but he's a good person. He's telling the truth. I'm certain of it."
        mc "{size=30}*ahem* Pervert?{/size}"
        if mc_ask_yuuhi_pussy:
            yuuhi "{size=30}You asked me to show you my... genitals when you were barely conscious on the ground.{/size}"
            if mc_ask_yuuhi_pee:
                yuuhi "{size=30}Not to mention that you asked me to pee on you as well.{/size}"      
        elif mc_take_off_pants_yuuhi:
            yuuhi "{size=30}You took off your pants the first time you met me... I'll never forget how embarrassed you made me.{/size}"
        elif scene89_yuuhi_spank:
            yuuhi "*giggles* {size=30}The first thing you did when you came back was to spank my butt.{/size}"
        mc "..."
        
    else:
        yuuhi "Father, please. [mc] is a good person. He's telling the truth. I'm certain of it."

    scene 89_s28 with dissolve
    dean "I had my suspicions about the story. Too neat. Too convenient for Avery's rise."
    dean "But more importantly... my daughter trusts you. Against my better judgment, I will extend that trust as well."
    scene 89_s29 with dissolve
    mc "Thank you. You won't regret it."
    scene 89_s30 with Dissolve(1.0)
    dean "We will see. Now, to the work. There is a problem."
    scene 89_s36 with dissolve
    mc "The materials?"
    scene 89_s30 with dissolve
    dean "Beyond materials. I can forge you a hand of finest steel that will never break. But it will only ever be a tool you strap on. A clever hook."
    scene 89_s36 with dissolve
    mc "Are you saying you can't make a combat-ready prosthetic?"
    scene 89_s30 with dissolve
    dean "I'm saying even if I could, my daughter's magic alone wouldn't be enough to make it yours. To make it feel alive."
    scene 89_s36 with dissolve
    mc "I... don't understand."
    scene 89_s31 with dissolve
    yuuhi "For it to truly be a part of you—to feel, to grip, to move like your real hand, it needs to be woven into your own magic, your nerves."
    yuuhi "That takes a powerful enchantment, melded into the metal itself."
    scene 89_s36 with dissolve
    mc "So I'd need a mage. A really strong one."
    scene 89_s30 with dissolve
    dean "Not just any mage. A sorcerer who specializes in artifice and bodily enchantment. The kind who works for purpose, not payment."
    scene 89_s36 with dissolve
    mc "A poweful sorceror?"
    mc "Hmm..."
    call screen scene89_choice02 with dissolve

label scene89_choice02_op1_2:
    if quest_witch_amelia_dead:
        mc "(I... killed Amelia. I don't even know why I'm still thinking about her. Was it wrong that I did it? It's strange but... it felt really easy at the time.)"
        mc "(God... killing a person... Now that the memories are flooding back, I feel like puking.)"
        scene 89_s31 with dissolve
        yuuhi "Are you alright, [mc]?"
        scene 89_s36 with dissolve
        mc "I'm fine."
    else:
        mc "(I captured Amelia and had her sent to the dungeon. There's no time nor reason to attempt to free her now.)"
    call screen scene89_choice02 with dissolve

label scene89_choice02_op1:
    $ mc_choose_not_amelia = True
    mc "There's a witch I was once sent to capture. I don't know if she's a true sorcerer, but she can definitely cast spells."
    scene 89_s31 with dissolve
    yuuhi "[mc], I don't want to sound rude, but... did you hit your head on the way here?"
    yuuhi "That witch was responsible for a lot of suffering. I wouldn't vouch for her unless it's truly your last resort."
    scene 89_s30 with dissolve
    dean "Indeed. A witch is a broad term. She could specialize in anything—no guarantee it's what you need. She might know curses or potions, not enchantments."
    scene 89_s36 with dissolve
    call screen scene89_choice03 with dissolve

label scene89_choice03_op1:
    $ mc_choose_amelia = True
    mc "I still want to try. I don't see another way."
    scene 89_s30 with dissolve
    dean "You must be at your wit's end if you're counting on a witch's goodwill."
    scene 89_s31 with dissolve
    yuuhi "Are you sure about this? People like that... they don't change easily."
    scene 89_s36 with dissolve
    mc "We parted on... decent terms. She owes me her freedom. That might be enough."
    scene 89_s31 with dissolve
    yuuhi "If you insist... Just promise me you'll be careful."
    scene 89_s36 with dissolve
    mc "I will. It's decided."
    scene 89_s37 with dissolve
    yuuhi "Do you even know where to find her?"
    scene 89_s39 with dissolve
    mc "I can retrace my steps from the city. If she's still in that forest, I'll find her."
    scene 89_s38 with dissolve
    dean "Don't get ahead of yourself. You still need the prosthetic itself to be forged. Unless you plan to drag a witch into the city."
    scene 89_s39 with dissolve
    mc "No, that's too dangerous for you both. I'll wait. How long will the forging take? Can it be done before midnight?"
    scene 89_s38 with dissolve
    dean "Yes. The form will be ready. The enchantment will be up to you and your... witch."
    scene 89_s39 with dissolve
    mc "Thank you, both of you."
    scene 89_s38 with Dissolve(1.0)
    dean "But listen to me carefully, [mc]. Nothing you are asking for comes without consequence."
    dean "The spell you seek does more than attach steel to flesh. It rewrites the way mana flows through a body. Some who undergo it awaken heightened sense, strength, perception, endurance beyond the norm."
    dean "And others... find their mana crippled. Severed. Reduced to a whisper where there was once potential."
    dean "Your body may accept this new limb as its own. Or it may reject it violently."
    scene 89_s39 with dissolve
    mc "I don't have any mana or magic potential to begin with. If anything, that should make this safer."
    scene 89_s38 with dissolve
    dean "Or it may make you unpredictable. Magic abhors empty vessels as much as unstable ones."
    scene 89_s39 with dissolve
    mc "...Even so. I'm willing to take that risk."
    scene 89_s38 with dissolve
    dean "Very well. You're welcome to stay until it is done. As long as you help my daughter with the shop."
    scene 89_s39 with dissolve
    mc "Thank you. But... you want me to help with customers? That's not a good idea. I shouldn't be seen."
    jump scene89_3

label scene89_choice03_op2:
    mc "You're both right, I'll think more about it."
    call screen scene89_choice02 with dissolve

label scene89_choice02_op2:
    $ mc_choose_ava = True
    mc "If it's a powerful sorcer or sorceress, then it I would choose Ava the elf."
    scene 89_s31 with dissolve
    yuuhi "Ava? The Royal Examiner? I've seen her a few times when delivering commissioned work to the castle. She uses her magic to assess the mana of artifacts and people."
    scene 89_s30 with dissolve
    dean "Someone with that title has deep ties to the royal apparatus. Or she had them. That connection is a double-edged sword."
    scene 89_s31 with dissolve
    yuuhi "Our family has ties to the Crown too, Father! It's not the same."
    scene 89_s30 with dissolve
    dean "No, it is not. We are loyalists. She was an official. Her loyalties now, after what happened, are an unanswered question."
    scene 89_s31 with dissolve
    yuuhi "I still think it's the best chance [mc] has. Her specialty sounds perfect."
    scene 89_s36 with dissolve
    mc "Then it's decided. Do you know where I can find her?"
    scene 89_s37 with dissolve
    yuuhi "She had a townhouse near commercial district's market. But after the explosion... I'm not sure if she's still there."
    scene 89_s39 with dissolve
    mc "It's a place to start. Thank you."
    scene 89_s38 with dissolve
    dean "Do not get ahead of yourself. You still require the prosthetic itself. Or do you plan to bring the Royal Examiner to my forge with no work to show her?"
    scene 89_s39 with dissolve
    mc "No, that's too dangerous for you both. I'll wait. How long will the forging take? Can it be done before midnight?"
    scene 89_s38 with dissolve
    dean "Yes. The physical form will be ready. Convincing her to bless it will be your task."
    scene 89_s39 with dissolve
    mc "Thank you, both of you."
    scene 89_s38 with Dissolve(1.0)
    dean "But listen to me carefully, [mc]. Nothing you are asking for comes without consequence."
    dean "The spell you seek does more than attach steel to flesh. It rewrites the way mana flows through a body. Some who undergo it awaken heightened senses... strength, perception, endurance beyond the norm."
    dean "And others... find their mana crippled. Severed. Reduced to a whisper where there was once potential."
    dean "Your body may accept this new limb as its own. Or it may reject it violently."
    scene 89_s39 with dissolve
    mc "I don't have any mana or magic potential to begin with. If anything, that should make this safer."
    scene 89_s38 with dissolve
    dean "Or it may make you unpredictable. Magic abhors empty vessels as much as unstable ones."
    scene 89_s36 with dissolve
    mc "...Even so. I'm willing to take that risk."
    scene 89_s30 with dissolve
    dean "Very well. You're welcome to stay until it is done. As long as you help my daughter with the shop."
    scene 89_s36 with dissolve
    mc "Thank you. But... you want me to help with customers? That's not a good idea. I shouldn't be seen."
    jump scene89_3

label scene89_3:
    scene 89_s31 with dissolve
    yuuhi "Don't worry! I've got a trick up my sleeve. Hehe~"
    scene 89_s36 with dissolve
    mc "What is it? You're not just going to cover my face with a sack, are you?"
    scene 89_s32 with Dissolve(1.0)
    yuuhi "Just come with me!"
    scene 89_s33 with dissolve
    yuuhi "Pops! I'm going to show [mc] the ropes first!"
    dean "Mhm."
    yuuhi "Come on, then~"
    jump scene90

label scene90:
    stop music fadeout 1.0 
    scene 90_s1 with Fade(1.4,1.0,1.2)
    play music "yuuhi.mp3" fadein 1.0 loop
    yuuhi "*sniff* Ahhh... fresh air. Finally."
    yuuhi "I can't stand it over there. All that... nghn... charcoal smell makes it hard to breathe."
    if mc_harem_yuuhi:
        scene 90_s2 with Dissolve(1.0)
        yuuhi "You know what else is breathtaking?"
        scene 90_s4 with dissolve
        yuuhi "...You!"
        scene 90_s3 with Dissolve(1.0)
        mc "*chuckles* I see. So you didn't actually need my help. You wanted something else."
        scene 90_s2 with dissolve
        yuuhi "T-That's not entirely true..."
        if not yuuhi_harem_training_finished:
            yuuhi "We never had the chance to truly make love before."
            if mc_told_yuuhi_maia:
                yuuhi "Is it because of that Maia girl you told me about?"
                scene 90_s3 with dissolve
                mc "...Maybe."
                scene 90_s2 with dissolve
                yuuhi "Heh. Figured. I assume you you're not spending too much time here so we'll make up for it now."
        yuuhi "Just keep it down. I don't want Pops hearing us."
        scene 90_s3 with dissolve
        mc "He wouldn't hear a cannon go off right now. He's in the zone."
        scene 90_s5 with Dissolve(1.5)
        yuuhi "{size=30}Psst! [mc]...{/size}"
        perception "She leans forward over the counter, arching her back. Her hips shift just enough to present her ass, a clear, teasing invitation with a mischievous glance over her shoulder."
        call screen scene90_choice1 with dissolve
    else:
        jump scene90_2

label scene90_2:
    scene 90_s2 with Dissolve(1.0)
    yuuhi "Right! Now to hide your famous face."
    scene 90_s45 with Fade(0.5,0.5,0.5)
    yuuhi "Hold still! I've got the perfect thing somewhere around here!"
    yuuhi "*giggles* I've been dying to use this on someone for ages."
    mc "You said the same thing about that huge club..."
    yuuhi "Don't worry, it isn't a great club this time!"
    scene 90_s46 with Dissolve(1.4)
    mc "A mask?"
    scene 90_s48 with dissolve
    yuuhi "Tsk, tsk, tsk. Not just any mask! This was worn by the legendary Reeves of Irda!"
    scene 90_s46 with dissolve
    mc "Whoa. No idea who that is, but he sounds important."
    scene 90_s47 with dissolve
    yuuhi "He was the first king to rule Irda, almost six hundred years ago."
    yuuhi "It's said he was stricken with an illness that disfigured his face and body. No one knew what he truly looked like, not even his own wife."
    scene 90_s46 with dissolve
    mc "And he wore a mask like this?"
    scene 90_s47 with dissolve
    yuuhi "Exactly! To keep his condition secret, and to not show weakness to his enemies."
    yuuhi "To be fair, outside of history nutjobs like me, he's almost entirely forgotten by now. So, I don't blame you for not knowing."
    scene 90_s46 with dissolve
    mc "How'd you get your hands on something like that?"
    scene 90_s47 with dissolve
    yuuhi "Well... honestly? I doubt it's the real thing. The merchant who sold it to us looked... let's just say, suspicious. Probably a replica. But it'll do the trick!"
    scene 90_s46 with dissolve
    jump scene90_4

label scene90_choice01_op1:
    $ mc_grope_yuuhi = True
    mc "I can't say no when you act like that."
    yuuhi "*giggles* Act like what? I'm just leaning here, totally innocent~"
    yuuhi "I just hope no one takes advantage of the situation~"
    jump scene90_choice01_op1_2

label scene90_choice01_op1_2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene2_p7_replay:
        $ persistent.scene2_p7_replay = True
    stop music fadeout 3.0 
    scene 90_s10 with Dissolve(1.6)
    perception "You step behind her. Her body tenses with anticipation, warm and waiting."
    call screen scene90_choice2 with dissolve

label scene90_choice01_op2:
    $ mc_dont_getit = True
    mc "Huh? What are you doing?"
    perception "She motions again more insistently, wiggling slightly for emphasis. Her eyes dart between you and her rear. Surely it can't get any clearer now..."
    call screen scene90_choice1 with dissolve

label scene90_choice01_op2_2:
    $ mc_grope_yuuhi = True
    mc "I still don't get it..."
    scene 90_s6 with vpunch
    yuuhi "Idiot!"
    yuuhi "I was telling you to touch my butt!"
    scene 90_s7 with dissolve
    mc "Oh..."
    scene 90_s6 with dissolve
    yuuhi "Were you seriously not getting that, or were you just messing with me!?"
    scene 90_s7 with dissolve
    mc "*chuckles* Honestly, it didn't click. Sorry."
    scene 90_s5 with dissolve
    yuuhi "*sigh* Whatever."
    yuuhi "Just... go ahead. Do your thing~"
    jump scene90_choice01_op1_2
    
label scene90_choice01_op3:
    $ mc_refuse_grope_yuuhi = True
    mc "This isn't the time or place, Yuuhi, and you know it."
    scene 90_s8 with dissolve
    yuuhi "Haha... you're right. Pops would probably murder us both if he knew."
    scene 90_s9 with dissolve
    mc "You still haven't told him about us?"
    scene 90_s8 with dissolve
    yuuhi "I wanted to! But with everything that's happened... I don't think he'd let his daughter be with a fugitive, even if it's for a good cause."
    yuuhi "He cares about me. Too much, sometimes."
    scene 90_s9 with dissolve
    mc "I get it. Let's just focus on the shop for now, okay?"
    scene 90_s8 with dissolve
    yuuhi "Alright. Deal."
    scene 90_s9 with dissolve
    jump scene90_2

label scene90_choice02_op1:
    $ scene90_remove_skirt = True
    scene 90_s23 with Dissolve(1.0)
    mc "This is in the way."
    yuuhi "H-hey! You can't just—"
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 90_s24 with Dissolve(1.2)
    perception "Before her fake protest finishes, you grab her skirt and take it off, exposing the soft swell of her thighs and a suprising lack of any underwear. A subtle gleam shines from her anus."
    yuuhi "Someone's bold~ Taking liberties with a poor tailor girl..."
    mc "You love it."
    yuuhi "M-maybe... just a little~"
    scene 90_s25 with Dissolve(1.0)
    sensation "The air in the shop feels cooler against her now-bare skin. She shivers, but remains arched, waiting for what comes next."
    mc "You're wearing a buttplug, huh? I've never met a girl who loves it in the ass as much as you."
    yuuhi "Hnnn~ I... I couldn't help it..."
    yuuhi "Pops is always going on about protecting my 'purity'... no touching down there..."
    yuuhi "It started small... but now I can't go a day without something inside my butt."
    mc "It made things worse if purity was the concern. These rules turned you into a full-fledged butt slut."
    yuuhi "D-Don't say that! It's... it's true, but don't say it!"
    scene 90_s26 with dissolve
    yuuhi "Take it out. I want you to put your finger in my butt~"
    play sound "se_sfx/sex/touch3.mp3" 
    scene 90_s27 with Dissolve(1.3)
    perception "The butt-plug slides out with a soft pop—her hole winking, glistening, already eager."
    yuuhi "Mmmmm~! I love that sensation every time... the emptiness... then the ache for more."
    if yuuh_suck_plug:
        mc "*chuckles* Remember that time when I shoved it in your mouth?"
        yuuhi "Why are you laughing? That was horrible of you!"
        mc "Not willing to try it again?"
        yuuhi "Absolutely not!"
        yuuhi "...Maybe if you say 'please'."
        call screen scene90_choice3 with dissolve
    else:
        scene 90_s22 with Dissolve(1.0)
        call screen scene90_choice2 with dissolve

label scene90_choice03_op1:
    $ yuuh_suck_plug2 = True
    mc "Please!"
    yuuhi "*sigh* ...Really?"
    mc "Pretty please?"
    yuuhi "*sigh* Fine. Give it to me."
    scene 90_s28 with Dissolve(1.0)
    yuuhi "..."
    mc "*chuckles* Come on. Nothing's gonna happen if you wait."
    scene 90_s29 with Dissolve(1.0)
    perception "She puts the buttplug in her mouth, her lips slowly sealing around it. Her expressions is a mix of lust and uneasiness."
    yuuhi "There... you happy?"
    mc "Very. How does your ass taste?"
    yuuhi "Tashtes... fine."
    mc "Good. Always keep it clean for me."
    yuuhi "Mhm..."
    scene 90_s22 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve

label scene90_choice03_op2:
    mc "It's fine. I don't want you to do it."
    yuuhi "Good. I-I wasn't intending on doing it anyway..."
    scene 90_s22 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve

default scene90_choice02_op4_first = False
label scene90_choice02_op4:
    if not scene90_choice02_op4_first:
        $ scene90_choice02_op4_first = True
        play sound "se_sfx/sex/sex4.mp3" 
        scene 90_s31 with Dissolve(1.0)
        perception "Your hand trails lower, fingertips tracing the curve of her cheek until you reach the tight, hidden ring between them. You press a fingertip against it slowly and being moving it in circles, gentle but insistent."
        yuuhi "W-Wait—! Let me relax myself first, your finger is really cold..."
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s32 with Dissolve(1.0)
        sensation "She tenses for a moment, then breathes out, relaxing just enough. You press in slowly—a tight, clutching heat envelops your finger, and her whole body quivers against you."
        yuuhi "Oh Gods~ You're... inside my butthole..."
        mc "This hole has seen much from you, hasn't it?"
        yuuhi "Y-yes! I love it in my butt~ So much."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with Dissolve(1.0)
        mc "Tell me about it."
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s32 with Dissolve(1.0)
        yuuhi "Yesterday... I was alone in my room... Ahhn~! f-fingering my butthole just like this."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with Dissolve(1.0)
        yuuhi "I came so hard~ Imagining it was you... stretching me... filling me there~"
        play sound "se_sfx/sex/touch3.mp3" 
        scene 90_s32 with Dissolve(1.0)
        mc "You're such a slut for anal."
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        yuuhi "It's my favorite... feels so dirty and good at the same time..."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with vpunch
        mc "Like this?"
        perception "You slip your fingers to the base and prod her deepest parts with intensity. She maons loudly before covering her mouth with her hands."
        yuuhi "Ahhn~! Yes~! More... please, [mc]~ I'm your little butt slut!"
        play sound "se_sfx/sex/touch3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        mc "Lower your voice."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with Dissolve(1.0)
        yuuhi "R-Right! Ahnng~! You're making it really hard."
        yuuhi "You're being so rough~ What if someone walks in and sees you fingering me like this?"
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        mc "We'll just pretend we're working on something."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with Dissolve(1.0)
        yuuhi "*giggles* Working on something inside my butt? That doesn't make- Hahhn~! sense."
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        mc "You're so fucking soft... makes me want to do more."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 90_s33 with Dissolve(1.0)
        yuuhi "Ahhn~! Right there... you're so bad~ teasing me like this~"
        yuuhi "M-more... please, I've been thinking about you screwing my ass for so long..."
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        perception "Each squeeze draws a soft, breathy sound from her lips."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with Dissolve(1.0)
        mc "You want me to ruin this hole?"
        play sound "se_sfx/sex/sex3.mp3" 
        scene 90_s31 with Dissolve(1.0)
        yuuhi "Yes! I want to remember you long after you're gone."
    else:
        play sound "se_sfx/sex/sex4.mp3" 
        scene 90_s31 with Dissolve(1.0)
        perception "Your hand trails lower again, fingertips tracing the familiar curve of her cheek until you reach the tight, hidden ring between them. You press your fingertips against it—slow circles."
        yuuhi "Mmm~... you're going right for it again... you remember exactly where I like it."
        yuuhi "It's not enough anymore... your fingers feel so much better..."
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s32 with dissolve
        sensation "She relaxes almost immediately this time—no resistance, just eager heat. You press in slowly—the tight, clutching warmth envelops your finger, her walls fluttering like they recognize you."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with dissolve
        yuuhi "Oh Gods~... you're stretching me just right~"
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s32 with dissolve
        mc "Tell me more about how much you love it."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with dissolve
        yuuhi "Last week I was so horny that I put three fingers deep in my butthole, imagining it was you ruining me... I came so hard I soaked the sheets..."
        play sound "se_sfx/sex/touch3.mp3" 
        scene 90_s32 with dissolve
        yuuhi "But it's never as good as when you do it... you hit places I can't reach..."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with dissolve
        mc "You're such a slut for anal now."
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s32 with dissolve
        yuuhi "Yes~! I'm your little butt slut... only for you."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s31 with dissolve
        yuuhi "Please... go deeper... wreck me~!"
        play sound "se_sfx/sex/touch3.mp3" 
        scene 90_s33 with dissolve
        sensation "You push to the base—her body quivers violently, walls clenching greedily around your fingers. She's dripping down her thighs already."
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s31 with dissolve
        yuuhi "Yes~! Ruin it... stretch it... make it remember your shape."
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with dissolve
        yuuhi "I want to feel you for days... every time I sit, every step... I want to think of you..."
        play sound "se_sfx/sex/sex3.mp3"
        scene 90_s31 with dissolve
        yuuhi "Ahhn~! More... please, [mc]~ I'm your lewd anal girl~!"
        play sound "se_sfx/sex/sex_cum8.mp3" 
        scene 90_s33 with dissolve
        sensation "Her body tenses, walls fluttering wildly around you. She's dripping onto the floor, legs trembling, breath coming in short, ragged bursts."
        play sound "se_sfx/sex/sex3.mp3"
    scene 90_s34 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve

default scene90_choice02_op5_first = False
label scene90_choice02_op5:
    $ mc_finger_yuuhi_pussy = True
    if not scene90_choice02_op5_first:
        $ scene90_choice02_op5_first = True
        if not scene90_choice02_op4_first:
            $ scene90_choice02_op5_first = True
            play sound "se_sfx/masturbate_female/1_masturbate.mp3"
            scene 90_s53 with Dissolve(1.0)
            perception "Your fingers slide forward along her inner thigh, finding her slick enterance. Her hips jerk slightly at the first contact."
            yuuhi "[mc]~! Y-You can't put it there..."
            mc "Your dad won't like his daughter getting pregnant, I know. Especially now I guess..."
            yuuhi "Exactly! So you have to be good..."
            mc "What about just a finger?"
            yuuhi "Umm..."
            yuuhi "J-Just a finger! Promise? And don't go too deep in! I don't want to accidentally lose my virginity... at least not like that."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s37 with Dissolve(1.0)
            sensation "You press one finger inside her, slowly, feeling her tight warmth envelop you. She's dry at first but quickly gets wet, and her hips roll gently against your hand."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s53 with Dissolve(1.0)
            yuuhi "Mmmmn... [mc]... you're finally penetrating my baby-making hole~"
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s37 with Dissolve(1.0)
            mc "Feels good?"
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s53 with Dissolve(1.0)
            yuuhi "Y-yes... so good... don't stop..."
            play sound "se_sfx/sex/sex4.mp3" 
            scene 90_s37 with Dissolve(1.0)
            sensation "Her breath comes in soft, shaky bursts as you move your finger in and out, each stroke drawing a sweet, muffled gasp from her lips."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s53 with Dissolve(1.0)
            mc "Fuck, you're so warm in here. I couldn't begin to imagine how good it would feel inside."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s37 with Dissolve(1.0)
            yuuhi "Mhnnn~! Y-You really think so?"
            play sound "se_sfx/sex/sex4.mp3" 
            scene 90_s53 with Dissolve(1.0)
            mc "Mhm. You're practically burning up my finger. My cock is perking up just thinking about it."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s37 with Dissolve(1.0)
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            yuuhi "*chuckles* I guess that's something I can hold you with~"
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s53 with Dissolve(1.0)
            yuuhi "You'll have to- Ahn~! ...come back if you want to experiance how my pussy feels."
        else:
            play sound "se_sfx/masturbate_female/1_masturbate.mp3"
            scene 90_s35 with Dissolve(1.0)
            perception "Your fingers slide forward along her inner thigh, finding her sensitive clit. Her hips jerk slightly at the first contact."
            yuuhi "[mc]~! Y-You can't put it there..."
            mc "Your dad won't like his daughter getting pregnant, I know. Especially now I guess..."
            yuuhi "Exactly! So you have to be good..."
            mc "What about just a finger?"
            yuuhi "Umm..."
            yuuhi "J-Just a finger! Promise? And don't go too deep in! I don't want to accidentally lose my virginity... at least not like that."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s36 with Dissolve(1.0)
            sensation "You press one finger inside her, slowly, feeling her tight warmth envelop you. She's already dripping, and her hips roll gently against your hand."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s35 with Dissolve(1.0)
            yuuhi "Mmmmn... [mc]... you're finally penetrating my baby-making hole~"
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s36 with Dissolve(1.0)
            mc "Feels good?"
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s35 with Dissolve(1.0)
            yuuhi "Y-Yes... so good... don't stop."
            play sound "se_sfx/sex/sex4.mp3" 
            scene 90_s36 with Dissolve(1.0)
            sensation "Her breath comes in soft, shaky bursts as you move your finger in and out, each stroke drawing a sweet, muffled gasp from her lips."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s35 with Dissolve(1.0)
            mc "Fuck, you're so warm in here. I couldn't begin to imagine how good it would feel inside."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s36 with Dissolve(1.0)
            yuuhi "Mhnnn~! Y-You really think so?"
            play sound "se_sfx/sex/sex4.mp3" 
            scene 90_s35 with Dissolve(1.0)
            mc "Mhm. You're practically burning up my finger. My cock is perking up just thinking about it."
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s36 with Dissolve(1.0)
            yuuhi "*chuckles* I guess that's something I can hold you with now~"
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s35 with Dissolve(1.0)
            yuuhi "You'll have to- Ahn~! ...come back if you want to experiance how my pussy feels."
    else:
        if not scene90_choice02_op4_first:
            play sound "se_sfx/masturbate_female/1_masturbate.mp3"
            scene 90_s53 with Dissolve(1.0)
            yuuhi "Stop, [mc]!"
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s37 with Dissolve(1.0)
            yuuhi "I... ahnn~! ...can't lose my virginty like this. I want it to be by your penis once we're married."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s53 with Dissolve(1.0)
        else:
            play sound "se_sfx/masturbate_female/1_masturbate.mp3"
            scene 90_s35 with Dissolve(1.0)
            yuuhi "Stop, [mc]!"
            play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
            scene 90_s36 with Dissolve(1.0)
            yuuhi "I... ahnn~! ...can't lose my virginty like this. I want it to be by your penis once we're married."
            play sound "se_sfx/masturbate_female/4_masturbate4.mp3"
            scene 90_s35 with Dissolve(1.0)
    
    if not scene90_choice02_op4_first:
        scene 90_s30 with Dissolve(1.0)
    else:
        scene 90_s34 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve

default scene90_choice02_op2_first = False
label scene90_choice02_op2:
    if not scene90_choice02_op2_first:
        $ scene90_choice02_op2_first = True
        scene 90_s11 with Dissolve(1.0)
        yuuhi "H-hey~! That's not my butt..."
        mc "I'd like to check up on these cute breasts first."
        scene 90_s12 with Dissolve(1.0)
        sensation "Her breast is soft and full, fitting perfectly in your palm. Her nipple stiffens under your touch."
        yuuhi "[mc]~... I like it when you squeeze my breasts."
        yuuhi "Please... you're making me... all tingly..."
        scene 90_s13 with Dissolve(1.0)
        yuuhi "Mfhmmm... Yes~! Please tease on my small nipple."
        yuuhi "I can feel it in my... everywhere~"
    else:
        scene 90_s12 with Dissolve(1.0)
        yuuhi "Mmmm~ *giggles* you're focusing too much on my breasts. I think you have a thing for them, aren't you glad I was blessed with big ones~"
        yuuhi "I want you to suckle on them once I become pregnant with our child."
        scene 90_s13 with Dissolve(1.0)
        yuuhi "Ahhn~! My nipples drawing milk with your slightest touch... I can't wait."

    if scene90_remove_skirt:
        scene 90_s22 with Dissolve(1.0)
    else:
        scene 90_s10 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve

default scene90_choice02_op3_first = False
label scene90_choice02_op3:
    if not scene90_choice02_op3_first:
        $ scene90_choice02_op3_first = True
        if not scene90_remove_skirt:
            mc "Let's try something different."
            scene 90_s14 with Dissolve(1.0)
            yuuhi "Different? What do you— ah!"
            scene 90_s15 with Dissolve(1.0)
            perception "You kneel, lifting one foot. You begin removing her work boot, revealing her damp sock."
            mc "Your feet have been working hard all day..."
            yuuhi "W-wait—! My feet are all sweaty and—!"
            scene 90_s18 with Dissolve(1.0)
            mc "Perfect."
            yuuhi "Y-you're serious? That's so embarrassing..."
        else:
            mc "Let's try something different."
            scene 90_s16 with Dissolve(1.0)
            yuuhi "Different? What do you— ah!"
            scene 90_s17 with Dissolve(1.0)
            perception "You kneel, lifting one foot. You begin removing her work boot, revealing her damp sock."
            mc "Your feet have been working hard all day..."
            yuuhi "W-wait—! My feet are all sweaty and—!"
            scene 90_s18 with Dissolve(1.0)
            mc "Perfect."
            yuuhi "Y-you're serious? That's so embarrassing..."
    else:
        if not scene90_remove_skirt:
            mc "I wanna peek at your cute sole again."
            scene 90_s14 with Dissolve(1.0)
            yuuhi "Umm... [mc]? You know you could just keep my shoe and sock off, right? You don't have to keep dressing me up then removing them again."
            scene 90_s15 with Dissolve(1.0)
            mc "No. It's hotter this way. It's like I'm removing your panties for the first time."
            scene 90_s18 with Dissolve(1.0)
            yuuhi "Pervert~"
        else:
            mc "I wanna peek at your cute sole again."
            scene 90_s16 with Dissolve(1.0)
            yuuhi "Umm... [mc]? You know you could just keep my shoe and sock off, right? You don't have to keep dressing and then undressing me..."
            scene 90_s17 with Dissolve(1.0)
            mc "No. It's hotter this way. It's like I'm removing your panties for the first time."
            scene 90_s18 with Dissolve(1.0)
            yuuhi "Pervert~"
    call screen scene90_choice4 with dissolve
    

default scene90_choice4_op1_first = False
label scene90_choice04_op1:
    if not scene90_choice4_op1_first:
        $ scene90_choice4_op1_first = True
        scene 90_s19 with Dissolve(1.0)
        sensation "Your thumb presses into her arch, massaging firmly. Her foot is warm, slightly damp from the day's work."
        yuuhi "Oh~... that feels... really good actually..."
        mc "You carry so much on these little feet all day."
        scene 90_s18 with Dissolve(1.0)
        yuuhi "I didn't know it could feel like this... you're spoiling me~"
        mc "Every part of you deserves attention."
        scene 90_s19 with Dissolve(1.0)
        yuuhi "*giggles* You're making my legs all weak... keep going... please~"
        scene 90_s18 with Dissolve(1.0)
    else:
        scene 90_s19 with Dissolve(1.0)
        sensation "Your thumb digs deeper into her arch this time—confident, knowing exactly where she's tense. Her foot is warmer, softer, already anticipating your touch."
        yuuhi "Ohhh... yes, right there. You remembered..."
        mc "These feet have been aching for me all day, haven't they?"
        scene 90_s18 with Dissolve(1.0)
        yuuhi "Mmm~ You have no idea... I've been carrying crates for Pops since dawn."
        scene 90_s19 with Dissolve(1.0)
        mc "Every part of you deserves this. Especially these pretty little feet."
        yuuhi "I love how strong your hand feels... how you know exactly what I need..."
        scene 90_s18 with Dissolve(1.0)
    call screen scene90_choice4 with dissolve

default scene90_choice4_op2_first = False
label scene90_choice04_op2: 
    if not scene90_choice4_op2_first:
        $ scene90_choice4_op2_first = True
        scene 90_s20 with Dissolve(1.0)
        perception "You bring her foot closer to your face, inhaling slowly—the faint, earthy scent of leather, sweat, and her natural warmth filling your senses."
        yuuhi "[mc]! You're... you're sniffing my foot!?"
        mc "*sniff* Mhm. You smell amazing. Real. Like you."
        yuuhi "Th-that's the sweatiest part of me right now! It's embarrassing~!"
        scene 90_s21 with Dissolve(1.0)
        sensation "Your tongue traces her arch lightly—salty, warm skin. She jolts, toes flexing against your cheek."
        yuuhi "You're making me... all hot and dizzy."
        mc "Mhmm..."
        yuuhi "I'm getting so wet from this... just from you licking my dirty feet..."
    else:
        scene 90_s20 with Dissolve(1.0)
        perception "You lift her foot without hesitation, bringing it straight to your face. The scent is stronger now—sweatier, muskier, more intimate after a full day of work."
        yuuhi "Mmm... you're doing it again..."
        mc "Fuck... even better than last time. Sweaty, warm... all you."
        yuuhi "You really love that smell, don't you? My dirty, sweaty feet..."
        yuuhi "Please lick my foot... taste how much I've been on my feet thinking about you."
        scene 90_s21 with Dissolve(1.0)
        sensation "Your tongue drags slowly along her arch, salty, slick, addictive. She shudders hard, thighs pressing together."
        mc "Like this?"
        yuuhi "Hnmmn~!"
        yuuhi "I'm so wet already... just from you sniffing and licking my sole."
    scene 90_s18 with Dissolve(1.0)
    call screen scene90_choice4 with dissolve

label scene90_choice04_op3:
    if not scene90_remove_skirt:
        scene 90_s10 with Dissolve(1.0)
    else:
        scene 90_s22 with Dissolve(1.0)
    call screen scene90_choice2 with dissolve


label scene90_choice02_op6:
    scene 90_s22 with Dissolve(1.0)
    mc "I can't wait anymore. I want to fuck your ass so hard now!"
    yuuhi "Please make it hurt~!"
    play sound "sound_effects/doors/wood_creak2.mp3"
    scene 90_s38 with dissolve
    yuuhi "W-Wait! The door!"
    #play sound "sound_effects/Dooropen.mp3"
    scene 90_s42 with vpunch
    $ renpy.end_replay()
    perception "Both of you snap upright in a panic—Yuuhi hastly putting back her skirt, you stepping back casually, or as casually as possible with your pulse racing."
    scene 90_s39 with Dissolve(1.0)
    dean "What are you two doing? Aren't you supposed to be helping with the shop, [mc]?"
    scene 90_s40 with dissolve
    mc "Of course, sir. We were just... cleaning up back here first. Making space."
    yuuhi "Y-Yes! Lots of dust! Very... dusty. Hehe..."
    scene 90_s39 with dissolve
    dean "It's clean enough. And you, Yuuhi—don't slack off just because you've got help."
    scene 90_s41 with Dissolve(1.0)
    yuuhi "Yes, sir! I-I mean, Pops!"
    scene 90_s42 with dissolve
    dean "Good. I'm leaving this door open. Don't close it."
    dean "Kids these days..."
    mc "..."
    yuuhi "..."
    scene 90_s43 with Dissolve(1.0)
    yuuhi "*sigh* I'm sorry, [mc]. I shouldn't have egged you on with Pops right there."
    yuuhi "Now I'm all worked up and nowhere to go..."
    scene 90_s44 with Dissolve(1.0)
    mc "*chuckles* You poor thing."
    yuuhi "Don't laugh! It's your fault for leaving me so long."
    mc "Come on, let's open the shop before your dad gets even angrier."
    yuuhi "First I need to wipe myself down. My thighs are... well, you know."
    yuuhi "Your fault too~"
    scene 90_s45 with Fade(1.0,1.0,1.0)
    play music "yuuhi.mp3" fadein 3.0 loop
    yuuhi "Stay right there. I've been dying to use this on someone for ages."
    mc "You said the same thing about that huge club..."
    yuuhi "Don't worry, it isn't a great club this time!"
    scene 90_s46 with Dissolve(1.3)
    mc "A mask?"
    scene 90_s48 with dissolve
    yuuhi "Tsk, tsk, tsk. Not just any mask! This was worn by the legendary Reeves of Irda!"
    scene 90_s46 with dissolve
    mc "Whoa. No idea who that is, but he sounds important."
    scene 90_s47 with dissolve
    yuuhi "He was the first king to rule Irda, almost six hundred years ago."
    yuuhi "It's said he was stricken with an illness that disfigured his face and body. No one knew what he truly looked like, not even his own wife."
    scene 90_s46 with dissolve
    mc "And he wore a mask like this?"
    scene 90_s47 with dissolve
    yuuhi "Exactly! To keep his condition secret, and to not show weakness to his enemies."
    yuuhi "To be fair, outside of history nutjobs like me, he's almost entirely forgotten by now. So, I don't blame you for not knowing."
    scene 90_s46 with dissolve
    mc "How'd you get your hands on something like this?"
    scene 90_s47 with dissolve
    yuuhi "Well... honestly? I doubt it's the real thing. The merchant who sold it to us looked... let's just say, suspicious. Probably a replica. But it'll do the trick!"
    scene 90_s46 with dissolve
    jump scene90_4

label scene90_4:
    scene 90_s49 with Dissolve(1.4)
    perception "Dean's hammer clangs in the background as Yuuhi adjusts the mask, her fingers lingering just a moment longer than necessary."
    scene 90_s50 with Dissolve(1.4)
    yuuhi "*laughs* Mysterious stranger, at your service!"
    mc "You sure this won't scare off customers? I feel like a serial killer."
    yuuhi "Oh, please. It's not as bad as you—"
    scene 90_s51 with vpunch
    yuuhi "Pfft! *laughs* Who am I kidding? You look {i}absolutely{/i} horrifying!"
    dean "Yuuhi!"
    scene 90_s52 with dissolve
    yuuhi "I was just about to open up!"
    yuuhi "Sheesh... calm down..."
    scene 90_s50 with Dissolve(0.8)
    mc "I'm not responsible if anyone runs screaming."
    yuuhi "It'll be fine. Hopefully."
    jump scene91

label scene91:
    stop music fadeout 1.0 
    scene 91_s1 with Fade(1.0,1.0,1.0)
    env "The air is thick with metallic tang and lingering smoke from the forge. Occasional footsteps echo outside, but none turn in."
    mc "It's really quiet."
    scene 91_s2 with dissolve
    yuuhi "*sigh* Welcome to my life."
    yuuhi "Pops mostly works for the army contract now. His standards are brutal, only using the purest ores, perfect tempering, no shortcuts anywhere... etcetera, etcetera..."
    yuuhi "He says if a blade can't survive a battlefield, it has no right to exist at all."
    yuuhi "Even a simple broadsword ends up costing a common family a week's wages. People still come by for repairs, sure—but new commissions? Rare."
    scene 91_s1 with dissolve
    mc "How many customers do you usually get in a day?"
    scene 91_s2 with dissolve
    yuuhi "On a good day? Five. But it's usually three to four."
    yuuhi "Just try to focus on something, anything, really. It makes the waiting feel shorter."
    scene 91_s1 with dissolve
    perception "The hammer clangs on in the back. Outside, footsteps pass again. Closer this time."
    play music "side_event3.mp3" fadein 2.0 loop
    scene 91_s3 with Dissolve(1.5)
    perception "A young woman strides with a confident posture."
    scene 91_s4 with Dissolve(1.0)
    if mc_talked_orym:
        dana "Hello."
    else:
        dana_ "Hello."
    scene 91_s5 with dissolve
    yuuhi "Welcome! How may I help you, miss... Dana, right?"
    scene 91_s4 with dissolve
    dana "Mhm. Is Dean around?"
    scene 91_s5 with dissolve
    yuuhi "He is, but he's in the middle of a complex commission. Is there something I can assist you with?"
    scene 91_s4 with dissolve
    dana "I requested a skinning dagger a while back. I was told it would be ready today."
    scene 91_s5 with dissolve
    yuuhi "Oh, of course! One moment, I'll be right back."
    scene 91_s6 with dissolve
    dana "You're new. I haven't seen you here before."
    dana "What's with the creepy mask? Hiding from an angry wife?"
    scene 91_s7 with dissolve
    mc "*ahem* Just here to help. Yuuhi's showing me the ropes and the mask is to help with all that smoke coming from the forge. My lungs... they aren't what they used to be."
    if mc_talked_orym:
        scene 91_s6 with dissolve
        dana "Hm... Have I met you before?"
        scene 91_s7 with dissolve
        mc "I don't believe so."
        scene 91_s6 with dissolve
        dana "Your voice is familiar. I've got a good memory, comes with being a healer mage. Names, faces, voices... they stick."
        scene 91_s7 with dissolve
        mc "You're probably confusing me with someone else."
    else:
        scene 91_s6 with dissolve
        dana "That so? I'm a healer, I might be able to help. With a fee, of course."
        scene 91_s7 with dissolve
        mc "I'm good."
        scene 91_s6 with dissolve
        dana "Suit yourself."
    scene 91_s8 with Dissolve(1.0)
    yuuhi "Here we are! Freshly sharpened."
    scene 91_s9 with Dissolve(1.3)
    dana "Excellent balance. He does fine work."
    scene 91_s10 with dissolve
    yuuhi "Anything else? We're running a special discount on a great club right now—"
    scene 91_s11 with dissolve
    dana "Actually, yes. I've been considering a new torso piece. This one's... no longer in fashion."
    scene 91_s12 with dissolve
    mc "What did you have in mind?"
    scene 91_s11 with dissolve
    dana "Something light, definitely not heavy plate, I need to move fast. But protective enough for travel. Maybe reinforced leather? Or something with small plates sewn in?"
    dana "Fitted, you know? Not bulky. I like a feminine cut—shows the figure a bit, but practical."
    dana "Color-wise, forest green would be ideal so I blend in the woods. Or deep brown. Nothing shiny. And the shape... curved for... well, you know, comfort."
    dana "Straps should be adjustable, padding on the inside so it doesn't chafe. Maybe some embroidery? Subtle runes if possible, nothing flashy."
    dana "You do custom work, is that correct?"
    scene 91_s13 with dissolve
    yuuhi "Uh... yes, we can do custom..."
    yuuhi "[mc], a little help? My head is spinning..."
    scene 91_s17 with Dissolve(1.0)
    mc "Based on what you described..."
    call screen scene91_choice01 with dissolve

default scene91_wrong = False
default scene91_correct = False
default scene91_partial = False

label scene91_choice01_op1:
    $ scene91_wrong = True
    mc "How about fine chainmail armor? It offers great protection and flexibility, I don't know about dyeing it green though."
    scene 91_s18 with dissolve
    dana "Chainmail? It's too heavy for long wear, and it rustles. I said I needed to move quietly. Also, it's usually front-fastening. Didn't you listen?"
    scene 91_s19 with dissolve
    yuuhi "We could line it with padded cloth to muffle the sound! And tailor the fit so it—"
    scene 91_s18 with dissolve
    dana "No. I'll think on it. Maybe I'll come back when Dean is available."
    scene 91_s20 with Dissolve(1.0)
    ""
    scene 91_s24 with Dissolve(1.0)
    yuuhi "Chainmail... really? *sigh* I don't blame you, I hate it when customers descibe the vaguest things."
    scene 91_s25 with dissolve
    jump scene91_3

label scene91_choice01_op2:
    $ scene91_correct = True
    mc "I'd recommend a hardened leather exterior. It's light, moves with you, and can be dyed in the color you want."
    scene 91_s16 with dissolve
    dana "Hmm, that... actually sounds perfect. You know your gear, new guy."
    scene 91_s17 with dissolve  
    yuuhi "We can have it made to your measurements in about a week!"
    scene 91_s16 with dissolve
    dana "Good. I'll take it."
    jump scene91_2
    
label scene91_choice01_op3:
    $ scene91_partial = True
    mc "How about treated hide armor? It's light, naturally flexible, good against cuts. Can dye it dark and add minimal plating for extra protection."
    scene 91_s16 with dissolve
    dana "Hide... it's light, true, and quiet. Not as strong as I'd like against heavy blows, but it'll do for now."
    dana "Alright. Make it forest green if you can. I'll take it."
    scene 91_s17 with dissolve
    yuuhi "We'll get started right away!"
    jump scene91_2

label scene91_2:
    scene 91_s14 with dissolve
    dana "Hold on, before I commit to this. What's the price?"
    scene 91_s15 with dissolve
    yuuhi "It's a custom piece so naturally the price will be higher... Ten silver."
    scene 91_s14 with vpunch
    dana "Ten?! That's... a bit steep for a traveling healer. Guild tasks have been dry lately so I'm not exactly swimming in coin right now."
    dana "Any chance for a returning customer... perk? I've brought good business before."
    scene 91_s15 with dissolve
    yuuhi "I'm really sorry, miss. We don't do discounts, Father's strict on that. Quality materials cost what they cost."
    scene 91_s14 with dissolve
    dana "Fuck... Orym's going to kill me for doing this, but I wasn't talking about a coin discount."
    scene 91_s15 with dissolve
    yuuhi "Sorry?"
    scene 91_s14 with dissolve
    dana "Come on, you know."
    scene 91_s15 with dissolve
    yuuhi "I... don't?"
    scene 91_s16 with dissolve
    dana "*sigh* What about you, big guy? I'm sure you get my meaning."
    scene 91_s17 with dissolve
    mc "..."
    call screen scene91_choice02 with dissolve

label scene91_choice02_op1:
    $ mc_ask_dana_sex = True
    mc "You want to... have sex with me?"
    scene 91_s18 with vpunch
    dana "Sex!? Gods, no! How did you... you two are so dense!"
    dana "Besides, I already have a man. Orym, he'd have my head if I bartered {i}that{/i}. I was talking about my breasts."
    scene 91_s19 with dissolve
    mc "And he'd be okay with flashing breasts?"
    scene 91_s18 with dissolve
    dana "He... He'd understand. It'll help us both in the long run anyway."
    scene 91_s19 with dissolve
    mc "So... no sex?"
    scene 91_s18 with dissolve
    dana "Definitely not. Just a quick flash—bring it down to seven silver?"
    scene 91_s19 with dissolve
    yuuhi "Wait! that's what you meant!?"
    call screen scene91_choice03 with dissolve

label scene91_choice02_op2:
    $ mc_ask_dana_feet = True
    mc "You want to... show me your feet?"
    scene 91_s18 with dissolve
    dana "My {i}feet{/i}? What kind of disgusting weirdo are you?"
    dana "I could show you my feet for free, and it wouldn't knock a copper off!"
    scene 91_s19 with dissolve
    mc "...Can I?"
    scene 91_s18 with vpunch
    dana "No!"
    dana "*sigh* Feet... Gods, men these days. No, I meant my breasts. A quick flash and you bring it down to seven silver."
    scene 91_s19 with dissolve
    yuuhi "Wait! that's what you meant!?"
    call screen scene91_choice03 with dissolve
    
label scene91_choice02_op3:
    mc "You want to... show me your breasts?"
    scene 91_s16 with dissolve
    dana "Finally! Someone speaks my language."
    scene 91_s17 with dissolve
    yuuhi "That's what you meant!?"
    scene 91_s16 with dissolve
    dana "Look, ten silver is rough. A quick flash and you bring it down to seven. Fair trade for a poor healer."
    scene 91_s17 with dissolve
    call screen scene91_choice03 with dissolve

label scene91_choice03_op1:
    $ mc_accept_dana_breasts = True
    mc "Deal. Show me those breasts."
    play sound "sound_effects/karma_less.mp3" volume 0.2
    if mc_karma > 1:
        $ mc_karma -= 1
    $ karma_less = True
    show screen stat_change with easeinright
    scene 91_s16 with dissolve
    dana "With pleasure~"
    scene 91_s17 with dissolve
    scene 91_s21 with Dissolve(1.3)
    yuuhi "{size=30}[mc]... why did you agree to this?{/size}"
    hide screen stat_change with easeoutright
    $ karma_less = False
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 91_s23 with Dissolve(1.3)
    perception "She loosens her top confidently, revealing natural breasts, soft and slightly flushed from the shop's warmth."
    scene 91_s22 with dissolve
    dana "Satisfied?"
    scene 91_s23 with dissolve
    mc "Mhm. Measurements noted."
    scene 91_s22 with dissolve
    dana "Worth it. Armor better be perfect~"
    scene 91_s23 with dissolve
    scene 91_s20 with Dissolve(1.5)
    dana "Farewell~ And, umm... if you ever meet a man named Orym, don't tell him anything about this."
    scene 91_s24 with Dissolve(1.0)
    yuuhi "*sigh* How am I going to explain to Pops that we sold a ten silver armor piece for seven?"
    scene 91_s25 with dissolve
    mc "You'll figure it out. You're smart, Yuuhi."
    scene 91_s24 with dissolve
    yuuhi "I am smart, and you... you are a pervert. *giggles*"
    scene 91_s25 with dissolve
    if yuuhi_harem_training_finished:
        mc "Don't talk to me about perversion when you've got a plug in all day."
        scene 91_s24 with vpunch
        yuuhi "H-Hey! Shush!"
        scene 91_s25 with dissolve
    jump scene91_3
    
label scene91_choice03_op2:
    mc "No. You'll pay the full price."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 91_s18 with dissolve
    dana "R-Really? You're missing out!"
    scene 91_s19 with dissolve
    mc "I don't think I am. Full price, lady."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 91_s18 with dissolve
    dana "Execue me!? You don't think my breasts are worth a look? You seriously think they're too small for you?!"
    scene 91_s19 with dissolve
    mc "I didn't say any of that..."
    dana "..."
    scene 91_s18 with dissolve
    dana "*sigh* ...Fine! Ten silver, then."
    scene 91_s19 with dissolve
    yuuhi "Thank you for your business. We'll begin the work!"
    scene 91_s20 with Dissolve(1.0)
    dana "See that you do. I'll return in a week for a fitting. Good day. Humph!"
    jump scene91_3

label scene91_3:
    scene 91_s2 with Fade(1.0,1.0,1.0)
    yuuhi "Did you know I'm allergic to cats and dogs? Of course that never stopped me from cuddling them to death. A truly cruel god decided this was my fate..."
    stop music fadeout 1.0 
    play sound "sound_effects/doors/door_kick.mp3"
    scene 91_s29 with vpunch
    perception "The shop door suddenly bangs open and a man stumbles in, one hand braced against the frame. His face is flushed, his eyes are bloodshot, and the stale reek of cheap beer rolls off him."
    play music "side_event1.mp3" fadein 1.0 loop
    scene 91_s30 with Dissolve(1.0)
    yuuhi "Oh! Welcome, sir. Can we... help you?"
    if mc_accept_helped_nadia:
        tom "The fuck else would I be here for? A pint? Yeah, fix my damn sword."
        yuuhi "I... Of course. May I see it?"
        scene 91_s31 with Dissolve(1.0)
        perception "He clumsily drops the sword on the counter with a heavy clang. The blade is notched, rusty, and crusted with dirt."
        mc "Damn... did you dig this out of someone's grave?"
        tom "Nghnn... edge is gone. Like butterin' bread with a rock. Fuckgin' useless."
        yuuhi "This will require significant work, sir. Re-edging, polishing, re-setting the guard... It hasn't been oiled in some time. The price—"
        scene 91_s32 with Dissolve(1.0)
        tom "Don't give me the pretty speech, girl. Just tell me how much and how long."
        scene 91_s33 with dissolve
        yuuhi "For a proper job? At least three silver. And two days."
        scene 91_s32 with vpunch
        tom "Two days?! You takin' a vacation with it? I need it tomorrow!"
        scene 91_s33 with dissolve
        yuuhi "That's impossible! Forging takes time! The steel needs—"
        scene 91_s32 with vpunch
        tom "I don't give a rat's ass about the steel! You think 'cause I've had a drink I don't know my business? I know a swindle when I see one."
        tom "Little girl in a smithy, probably her daddy's place, thinkin' you can fleece a real fighter."
        scene 91_s33 with dissolve
        yuuhi "That's not true! I'm a certified tailor! This is a fair price for the labor!"
        scene 91_s32 with dissolve
        tom "Look, just hammer the edge out or whatever. I don't need it pretty. I need it sharp. Tomorrow. One silver."
        scene 91_s33 with dissolve
        yuuhi "I can't do that. The integrity would be—"
        scene 91_s32 with dissolve
        tom "Fuck integrity! Can you do it or not?"
        scene 91_s33 with dissolve
        yuuhi "..."
    else:
        tom_ "The fuck else would I be here for? A pint? Yeah, fix my damn sword."
        yuuhi "I... Of course. May I see it?"
        scene 91_s31 with Dissolve(1.0)
        perception "He clumsily drops the sword on the counter with a heavy clang. The blade is notched, rusty, and crusted with dirt."
        mc "Damn... did you dig this out of someone's grave?"
        tom_ "Nghnn... edge is gone. Like butterin' bread with a rock. Fuckgin' useless."
        yuuhi "This will require significant work, sir. Re-edging, polishing, re-setting the guard... It hasn't been oiled in some time. The price—"
        scene 91_s32 with Dissolve(1.0)
        tom_ "Don't give me the pretty speech, girl. Just tell me how much and how long."
        scene 91_s33 with dissolve
        yuuhi "For a proper job? At least fifteen silver. And three days."
        scene 91_s32 with vpunch
        tom_ "Three days?! You takin' a vacation with it? I need it tomorrow!"
        scene 91_s33 with dissolve
        yuuhi "That's impossible! Forging takes time! The steel needs—"
        scene 91_s32 with vpunch
        tom_ "I don't give a rat's ass about the steel! You think 'cause I've had a drink I don't know my business? I know a swindle when I see one."
        tom_ "Little girl in a smithy, probably her daddy's place, thinkin' you can fleece a real fighter."
        scene 91_s33 with dissolve
        yuuhi "That's not true! I'm a certified tailor! This is a fair price for the labor!"
        scene 91_s32 with dissolve
        tom_ "Look, just hammer the edge out or whatever. I don't need it pretty. I need it sharp. Tomorrow. Ten silver."
        scene 91_s33 with dissolve
        yuuhi "I can't do that. The integrity would be—"
        scene 91_s32 with dissolve
        tom_ "Fuck integrity! Can you do it or not?"
        scene 91_s33 with dissolve
        yuuhi "..."
    call screen scene91_choice04 with dissolve

label scene91_choice04_op1:
    $ yuuhi_love += 10
    if mc_accept_helped_nadia:
        mc "You heard her. She gave you the terms. You don't like them? The door's right there."
        scene 91_s35 with dissolve
        tom "Who the hell are you? The doorman?"
        scene 91_s34 with dissolve
        mc "Right now, I am. You don't talk to her like that. Not here. Pick up your pig-iron and leave."
        scene 91_s35 with dissolve
        tom "Or what? You gonna make me, masked boy?"
        scene 91_s34 with dissolve
        mc "You have three seconds to be gone before I help you through the door. I won't be gentle."
        tom "..."
        scene 91_s35 with dissolve
        tom "Fine! Shithole smithy. I'll take my business to someone who appreciates it!"
        scene 91_s36 with Dissolve(1.0)
        tom "*sniff* It just had to burn down... where the hell am I ever going to find a job now..."
    else:
        mc "You heard her. She gave you the terms. You don't like them? The door's right there."
        scene 91_s35 with dissolve
        tom_ "Who the hell are you? The doorman?"
        scene 91_s34 with dissolve
        mc "Right now, I am. You don't talk to her like that. Not here. Pick up your pig-iron and leave."
        scene 91_s35 with dissolve
        tom_ "Or what? You gonna make me, masked boy?"
        scene 91_s34 with dissolve
        mc "You have three seconds to be gone before I help you through the door. I won't be gentle."
        tom_ "..."
        scene 91_s35 with dissolve
        tom_ "Fine! Shithole smithy. I'll take my business to someone who appreciates it!"
        scene 91_s36 with Dissolve(1.0)
        tom_ "*sniff* It just had to burn down... where the hell am I ever going to find a job now..."

    scene 91_s24 with Dissolve(1.0)
    yuuhi "*sigh* ...Thank you. He was... awful."
    scene 91_s25 with dissolve
    mc "You don't have to thank me. You were professional and he wasn't a customer."
    scene 91_s24 with dissolve
    yuuhi "I know. But I always feel like I should try... that maybe I'm not being understanding enough. He was clearly in a bad way."
    scene 91_s25 with dissolve
    mc "Being drunk isn't a license to be cruel. Protecting your shop and your peace isn't a failure. It's sense."
    scene 91_s24 with dissolve
    yuuhi "You're right, it is. Thanks again, [mc]."
    scene 91_s25 with dissolve
    if mc_harem_yuuhi:
        mc "I always protect my girl."
        yuuhi "Hehe~"
    jump scene91_4

label scene91_choice04_op2:
    $ mc_helped_tom = True
    if mc_accept_helped_nadia:
        mc "We can have it serviceable by tomorrow. Fifteen silver. Non-negotiable."
        scene 91_s35 with dissolve
        tom "Serviceable? What's that mean?"
        scene 91_s34 with dissolve
        mc "It means sharp, not pretty. It won't be a masterpiece, and it won't hold that edge for long, but it'll cut. That's the deal."
        scene 91_s35 with dissolve
        tom "*scoff* ...Fine, dat's what I wanted anyway. Fifteen. Tomorrow before noon."
    else:
        mc "We can have it serviceable by tomorrow. Fifteen silver. Non-negotiable."
        scene 91_s35 with dissolve
        tom_ "Serviceable? What's that mean?"
        scene 91_s34 with dissolve
        mc "It means sharp, not pretty. It won't be a masterpiece, and it won't hold that edge for long, but it'll cut. That's the deal."
        scene 91_s35 with dissolve
        tom_ "*scoff* ...Fine, dat's I wanted anyway. Fifteen. Tomorrow before noon."

    scene 91_s34 with dissolve
    mc "Agreed. Leave it."
    scene 91_s36 with Dissolve(1.0)
    perception "The man grunts, shoves the sword further across the counter, and fumbles a handful of coins from his purse, dropping them. He turns and leaves without another word."
    scene 91_s24 with Dissolve(1.0)
    yuuhi "*sigh* I'm glad you handled him. But this... it's a butcher's job. It goes against everything Pops works for."
    scene 91_s25 with dissolve
    mc "Not every customer deserves your best work. Just give him a quick fix."
    scene 91_s24 with dissolve
    yuuhi "Y-You're right. I'll tell Pops to get the grinding wheel ready."
    scene 91_s25 with dissolve
    jump scene91_4
    
label scene91_4:
    stop music fadeout 1.0
    scene 91_s2 with Fade(1.3,1.0,1.5)
    yuuhi "Do you read, [mc]? I've been reading this novel... well, more like an illustrated one. It's about a girl blessed with strange powers."
    yuuhi "It's really dark at first because she can't control them, she even accidentally kills her own lover ...wait. I shouldn't have said that. Dammit!"
    play music "fear/slaughter.mp3" fadein 2.0 loop
    scene 91_s37 with Dissolve(1.0)
    perception "The door doesn't so much open as it is dominated. A mountain of a man ducks beneath the frame, then straightens to his full, imposing height, filling the smithy with his presence."
    scene 91_s38 with Dissolve(1.0)
    mc "...Whoa."
    scene 91_s39 with dissolve
    yuuhi "O-Oh! Welcome, sir! Can I help you with something?"
    play music "side_event2.mp3" fadein 1.0 loop
    scene 91_s40 with Dissolve(1.0)
    thulkin "By all the Gods, I hope so! The fellows at the tavern said, 'Thulkin, if you want an edge that'll last, you go to the forge with the intersecting swords on the sign!' So here I am!"
    scene 91_s41 with dissolve
    yuuhi "Th-Then you came to the right place! What can we do for you, Sir Thulkin?"
    scene 91_s44 with Dissolve(1.0)
    thulkin "Take a look at this. The love of my life... wounded."
    scene 91_s45 with dissolve
    perception "He lifts his great-axe with surprising tenderness. A deep, ugly chip mars the blade on the edge, metal torn away as if bitten."
    scene 91_s44 with dissolve
    thulkin "Had a disagreement with an ogre's skull about thirty miles north of here. My swing was true, but his skull was harder than I gave it credit for!"
    scene 91_s45 with dissolve
    yuuhi "A-An ogre!?"
    scene 91_s44 with dissolve
    thulkin "Came charging out of the treeline at dusk, all froth and fury. Thought I'd make a fine supper!"
    scene 91_s40 with Dissolve(1.0)
    thulkin "*laughs* He learned otherwise, but he left his mark on my favorite girl here."
    scene 91_s46 with Dissolve(1.0)
    mc "You travel alone? Through the wilds with ogres?"
    scene 91_s47 with dissolve
    thulkin "Best way to travel! Company slows you down, and you miss all the best conversations! Though that one was more of a listener."
    thulkin "So! Can you fix her? I'd do it myself, but I'm a guest in your fine city."
    scene 91_s41 with Dissolve(1.0)
    yuuhi "This is a severe chip... We'll need to reforge the damaged section, then re-temper the entire blade to keep its balance. Anything less would weaken it."
    yuuhi "It's a full day's work, and it will require a master's hand."
    scene 91_s40 with dissolve
    thulkin "Excellent! I love a craftsman who doesn't mince words. A full day's honest work for a full day's honest pay! What's the damage?"
    scene 91_s41 with dissolve
    yuuhi "Given the quality of the steel... one gold."
    scene 91_s40 with dissolve
    thulkin "*laughs* A fair price for saving my lady! Done!"
    scene 91_s46 with Dissolve(1.0)
    mc "By the accent, I assume you're not from here."
    scene 91_s47 with dissolve
    thulkin "Sharp ears, my one-handed friend! Born and raised in the Valdrun fjords."
    thulkin "I came south with my sister, crossing the snowy mountains nearby. We've been tracking an elusive tribe of goblins who did unspeakable things back home."
    thulkin "But before that... rumors! Lots of them from wandering traders."
    scene 91_s41 with Dissolve(1.0)
    yuuhi "Rumors, sir?"
    scene 91_s40 with dissolve
    thulkin "A queen dies at sea—a tragedy! Her sister takes the throne—politics! Then, boom! An explosion that shakes the very stones, they say big as a dragon's sigh!"
    thulkin "That's a story! And when I hear a story that loud, my feet start moving by themselves. I had to come see the characters and the set-dressing for myself!"
    scene 91_s46 with Dissolve(1.0)
    mc "It's a dangerous story to be part of."
    scene 91_s47 with dissolve
    thulkin "All the best ones are! A safe story is a boring story. So, you're in the thick of it, are you? The quiet man in the smithy. You have the look about you."
    scene 91_s46 with dissolve
    yuuhi "He's, um, our new apprentice!"
    scene 91_s47 with dissolve
    thulkin "Is he now? Well, every story needs a few mysterious fellows. Very well! I'll be back by tommorrow."
    scene 91_s46 with dissolve
    mc "Thank you for your business."
    scene 91_s48 with Dissolve(1.0)
    thulkin "Farewell, friends! Take good care of her."
    scene 91_s24 with Fade(0.5,0.5,0.5)
    yuuhi "Phew..."
    scene 91_s25 with dissolve
    mc "An interesting fellow. He talked like danger was a hobby, sounded a little crazy."
    scene 91_s24 with dissolve
    yuuhi "For sure. On the bright side, maybe Gaius finally found his match."
    scene 91_s25 with dissolve
    mc "You think they'd clash?"
    scene 91_s24 with dissolve
    yuuhi "Probably not, but who knows? Two mountains like that in the same kingdom... bound to rumble eventually."
    scene 91_s25 with dissolve
    call screen scene91_choice05 with dissolve

label scene91_choice05_op1:
    $ mc_wants_fight_gaius = True
    mc "If Gaius falls, it'll be by my blade."
    scene 91_s24 with dissolve
    yuuhi "*giggles* Whoa... listen to you~"
    yuuhi "If only I had half the confidence you do. You say that like it's already written in the stars."
    scene 91_s25 with dissolve
    mc "It's personal."
    scene 91_s24 with dissolve
    yuuhi "Personal, hmm? Gaius took your hand... and you take his life? Sounds like a ballad waiting to happen."
    yuuhi "Just... promise me you won't be so direct about it."
    scene 91_s25 with dissolve
    mc "*chuckles* Promise."
    jump scene91_5
    
label scene91_choice05_op2:
    $ mc_wants_recruit_gaius = True
    mc "I was actually hoping to recruit Gaius."
    scene 91_s24 with dissolve
    yuuhi "You really did hit your head somewhere, didn't you?"
    yuuhi "Gaius has been serving the royal family longer than you and I have been alive. He's loyal as a warhound, probably sleeps with the crown's seal under his pillow."
    scene 91_s25 with dissolve
    mc "Loyalty can change. Men like that... they might appreciate strength more than politics."
    scene 91_s24 with dissolve
    yuuhi "I say go for it. Gaius on your... {i}our{/i} side? *laughs* Avery wouldn't be able to sleep at all!"
    yuuhi "But if he says no... are you going to challenge him to a rematch right there?"
    scene 91_s25 with dissolve
    mc "*chuckles* Maybe."
    scene 91_s24 with dissolve
    yuuhi "I'm betting on you then~"
    scene 91_s25 with dissolve
    jump scene91_5
    
label scene91_choice05_op3:
    $ mc_wants_nothing_gaius = True
    mc "Good. Let them tear each other apart."
    scene 91_s24 with dissolve
    yuuhi "*chuckles* Two monsters fighting? We just sit back and watch the castle burn."
    scene 91_s25 with dissolve
    mc "Mhm. Saves us the trouble."
    scene 91_s24 with dissolve
    yuuhi "Just don't get caught in the crossfire when the big dogs clash."
    scene 91_s25 with dissolve
    jump scene91_5

label scene91_5:
    stop music fadeout 2.0 
    scene 91_s49 with Fade(1.3,1.0,1.3)
    yuuhi "*yawn* I think that's all for today. Time to close up-"
    play sound "sound_effects/Dooropen.mp3"
    scene 91_s51 with Dissolve(1.3)
    perception "The door opens softly. A young woman stands hesitantly in the doorway, a simple but well-cared-for bow slung across her back."
    yuuhi "*sigh* Never mind, I guess..."
    scene 91_s50 with dissolve
    elara "Hello. Is... is the smithy open? I didn't mean to intrude. I can come back tomorrow if it's too late."
    scene 91_s51 with dissolve
    yuuhi "Not at all. Please, come in. How can we help?"

    if mc_elara_in:
        play music "sex01.mp3" fadein 4.0 loop
        scene 91_s52 with Dissolve(1.4)
        elara "Thank you. I was hoping you might fix my bow. The string snapped during... training. Is it possible to repair?"
        scene 91_s53 with dissolve
        yuuhi "Let me see."
        scene 91_s58 with Dissolve(1.0)
        yuuhi "Oh, this is nothing serious. I get adventurers in here with the same issue every week. I can have it good as new for you by tomorrow morning!"
        elara "Thank you. I... I appreciate it. But I wasn't talking about just fixing the string, I could have done it myself, I want the same material."
        scene 91_s59 with Dissolve(1.0)
        mc "How did it snap? That's a sturdy looking bow."
        scene 91_s79 with dissolve
        elara "Too much pressure, I think. I've been pushing myself. Training non-stop since I joined the guild."
        scene 91_s80 with dissolve
        yuuhi "It happens to the best of us. Really, no shame in it."
        scene 91_s81 with dissolve
        elara "It shouldn't have happened at all. They always told me to take care of my gear. That it was the only thing between me and a quick death."
        scene 91_s59 with dissolve
        mc "You seem upset. Did something happen? Is Eireen being too hard on you?"
        scene 91_s79 with dissolve
        elara "No. It's not Eireen. It's... my old party. The one I was with before the guild."
        elara "We had a job lined up. Skitter-Maws in the quarry. Very risky, but the pay... it was life-changing. Eireen found out and immedietly declined me from going."
        elara "She said I wasn't ready. She was... firm. I was furious. I thought she was holding me back."
        scene 91_s59 with dissolve
        mc "And your party... they went without you?"
        scene 91_s79 with dissolve
        elara "Mhm. I found out three days later from the recovery team, they brought them back, or what was left of them. The Skitter-Maws... they don't just kill you. They wrap you up. Leave you for later."
        elara "Eireen saved my life by not allowing me to go. I owe her for that. And I hate her for it a little, too. Because every night, I wonder if I could have made the difference. If I'd been there, maybe..."
        scene 91_s59 with dissolve
        mc "You'd be dead. And you wouldn't be wondering anything."
        scene 91_s79 with dissolve
        elara "*sigh* I know. It just doesn't feel like a victory. It feels like I survived a shipwreck and now I'm just... sitting alone on the shore."
        elara "Sorry... you didn't ask for all that. I just needed the bow fixed."
        scene 91_s80 with dissolve
        yuuhi "It's no trouble at all. I'll take good care of it. It should be ready by tomorrow morning."
        scene 91_s81 with dissolve
        elara "Thank you."
        scene 91_s80 with dissolve  
        scene 91_s24 with Fade(0.5,0.5,0.5)
        yuuhi "...Gods. That's... a horrible way to lose people."
        scene 91_s25 with dissolve
        mc "Eireen was right to stop her."
        scene 91_s24 with dissolve
        yuuhi "She did. But still... all her friends are gone. I can't imagine the weight of that. I hope the guild is looking after her."
        scene 91_s25 with dissolve
        jump scene91_6

    else:
        $ elara_dead = True
        play music "sex01.mp3" fadein 4.0 loop
        scene 91_s52 with Dissolve(1.4)
        elara "Thank you. I was hoping you might sell... elemental arrows. Fire-tipped ones, or even blessed arrows, if you have any."
        scene 91_s53 with dissolve
        yuuhi "I'm really sorry, but we don't carry those."
        yuuhi "Those are specialist items. Usually commissioned through the Alchemists' Guild, or occasionally stocked by the Adventurers' Guild for larger expeditions."
        scene 91_s52 with dissolve
        elara "Oh. I see. Of course."
        scene 91_s55 with dissolve
        mc "That's very specific equipment. What are you hunting?"
        scene 91_s54 with dissolve
        elara "It's... not exactly hunting. It's a task. My party, they... they heard about a job. Clearing out a nest of Skitter-Maws in the old quarry tunnels."
        elara "Somehow a group of them migrated here all the way from the south."
        scene 91_s55 with dissolve
        yuuhi "Skitter-Maws?! But those are very dangerous!"
        mc "You're not even in the guild, why take a such a risky job?"
        scene 91_s54 with dissolve
        elara "Huh?! H-How did you know that I'm in not the guild?"
        scene 91_s55 with dissolve
        mc "...Call it intuition. You have the look of someone waiting for their chance. So why this job?"
        scene 91_s54 with dissolve
        elara "They said... they said we could manage. That it's a quick job. The payout is supposed to be huge. Enough to pay my guild initiation fee three times over."
        elara "It all feels... terrifying. They were supposed to go a few days ago, but they waited for me. Now they're saying I'm holding them back."
        elara "This is my chance to prove I'm not just a liability. If I don't go... I might not have a party anymore."
        elara "I don't know what to do. If I back out now, they'll never trust me again. But if I go..."
        scene 91_s55 with dissolve
        call screen scene91_choice06 with dissolve

label scene91_choice06_op1:
    mc "Don't go. A real team doesn't call you a liability for having sane fears. They listen to them."
    mc "Go to the Adventurers' Guild tomorrow. Speak to Eireen herself and tell her about this 'task'. She'll send better suited people for it."
    mc "She'd also rather have a live applicant than a dead one."
    scene 91_s56 with dissolve
    elara "You sound just like her. Like Eireen. 'Train harder. Wait your turn.' I followed the rules!"
    elara "No one thinks I'm good enough. Not the guild, not my party. And now not you. You all think I'm too scared to make my own choices."
    scene 91_s57 with dissolve
    mc "This isn't about being scared, it's about-"
    scene 91_s56 with dissolve
    elara "I'm done talking. If I wanted advice, I would have asked for it. Goodbye."
    scene 91_s57 with dissolve
    scene 91_s24 with Fade(0.5,0.5,0.5)
    yuuhi "That was... the right thing to say. You tried. If anything happens to her, it isn't your fault."
    scene 91_s25 with dissolve
    mc "I don't know... I was the one who didn't let her into the guild in the first place. Maybe if she were... Eireen could've stopped her."
    scene 91_s24 with dissolve
    yuuhi "Then... I hope she sees reason before it's too late. Sometimes trying is all you can do."
    scene 91_s25 with dissolve
    jump scene91_6

label scene91_choice06_op2:
    mc "Maybe this is your chance. Maybe they're right. Confidence counts for a lot out there."
    mc "If you've trained, if you trust your aim... going might be what seals your place with them. Just be smart. Watch each other's backs."
    scene 91_s54 with dissolve
    elara "You... you really think I can do it?"
    scene 91_s55 with dissolve
    mc "I think the only way to know is to try. Sometimes you have to take the leap."
    scene 91_s54 with dissolve
    elara "You're right. I've trained hard. I can do this. Thank you for the encouragement!"
    scene 91_s55 with dissolve
    scene 91_s24 with Fade(0.5,0.5,0.5)
    yuuhi "Not sure about this, [mc]... she looked terrified. I hope she stays safe."
    scene 91_s25 with dissolve
    mc "I gave her what she asked for: a push. Some lessons have to be learned firsthand."
    scene 91_s24 with dissolve
    yuuhi "I hope that push doesn't send her off a cliff."
    scene 91_s25 with dissolve
    jump scene91_6

label scene91_6:
    stop music fadeout 5.0 
    scene 91_s60 with Fade(1.5,1.0,1.3)
    yuuhi "I doubt anyone else is coming. Hahh... I'm ready to drop."
    scene 91_s61 with dissolve
    mc "The hammering stopped. Your dad must be finished."
    scene 91_s62 with Dissolve(1.0)
    yuuhi "Before we go see, here. This is for you."
    mc "What's this?"
    yuuhi "Your share. For today."
    mc "You're paying me? I was just helping."
    if scene91_correct and mc_helped_tom:
        yuuhi "Helping? You sold that armor to Dana and even agreed to help that rude man. That's more than helping. You earned this."
    elif scene91_partial or scene91_correct or mc_helped_tom:
        yuuhi "Of course I'm paying you. You handled yourself well, even if it wasn't perfect. A fair day's work."
    else:
        yuuhi "You still showed up and tried. That counts for something around here. It's not much, but it's honest."
    call screen scene91_choice07 with dissolve

label scene91_choice07_op1:
    mc "Thank you. I won't pretend it isn't needed."
    scene 91_s60 with Dissolve(1.0)
    if scene91_correct and mc_helped_tom:
        $ mc_coin += 30
        yuuhi "Three silver. Don't spend it all in one place. Unless that place is our smithy. Now, come on. I'm dying to see what he's made!"
    elif scene91_partial or scene91_correct or mc_helped_tom:
        $ mc_coin += 20
        yuuhi "Two silver. It's a start. Now let's go see if Father's work puts ours to shame."
    else:
        $ mc_coin += 10
        yuuhi "One silver. Every journey starts with a single step, right? Let's go see yours."
    scene 91_s61 with dissolve
    jump scene91_7

label scene91_choice07_op2:
    scene 91_s61 with Dissolve(1.0)
    mc "Thank you, Yuuhi. That's kind. But you should keep it."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright
    scene 91_s60 with dissolve
    yuuhi "What? Why? You earned it."
    scene 91_s61 with dissolve
    mc "Get a decent meal for you and your father instead. You've done more for me today than coin can repay."
    hide screen stat_change with easeoutright
    $ karma_more = False
    scene 91_s60 with dissolve
    yuuhi "[mc]... I can't just—"
    scene 91_s61 with dissolve
    mc "You can. Please. Buy yourself something that isn't coal or steel for a change."
    scene 91_s60 with dissolve
    yuuhi "You're a stubborn one, you know that? Fine. But I'm buying you a sweetroll next time you're here. No arguments."
    scene 91_s61 with dissolve
    mc "*chuckles* Deal. Now, let's see this masterpiece."
    jump scene91_7

label scene91_7:
    scene 91_s63 with Fade(1.4,1.0,1.0)
    play music "blacksmith2.mp3" fadein 1.0 loop
    mc "How's the work going?"
    dean "It is done."
    scene 91_s64 with Dissolve(1.5)
    perception "He unfolds the cloth. Beneath it rests the prosthetic, black and silver steel. It doesn't shine; it waits."
    dean "Take it."
    scene 91_s65 with Fade(0.5,0.5,0.5)
    stop music fadeout 3.0 
    sensation "You fit the prosthetic against the stump. It slides into place as if it was always meant to be there. A strange sensation follows, not pain. Not comfort."
    play music "hope/hope2.mp3" fadein 3.0 loop
    desire "Purpose."
    scene 91_s66 with dissolve
    mc "...This is beyond anything I imagined."
    scene 91_s65 with dissolve
    dean "Adamantite core, hardened steel plating. You could block a warhammer with this and not find a dent."
    dean "But as I said, it's just a beautiful paperweight. Its true purpose must be woven into it by another."
    scene 91_s66 with dissolve
    mc "I'll find someone. Thank you. But this... this can't be a gift."
    scene 91_s68 with dissolve
    dean "It isn't. The adamantite alone cost a fortune, it was actually meant for a different commission. A new weapon for Gaius, the Queen's lapdog."
    dean "*chuckles* The idiot lost his sword somehow."
    scene 91_s67 with dissolve
    mc "You used his materials?! For me?"
    scene 91_s68 with dissolve
    dean "The order came from the Magistrate's office. After what you told me? To hell with them. I'd rather see this metal empower a man fighting a tyrant than the tyrant's favorite attack dog."
    scene 91_s67 with dissolve
    yuuhi "Pops... if they find out..."
    scene 91_s68 with dissolve
    dean "They won't. I'll tell them a flaw was found in the smelting, that it shattered under the hammer."
    dean "They'll rage, they'll threaten, but what will they do? Find another smith of my skill overnight? They need me more than I need their guilt-ridden coin."
    scene 91_s69 with dissolve
    mc "You're gambling your entire livelihood."
    scene 91_s70 with dissolve
    dean "I am investing in a principle. One I should have invested in sooner. But make no mistake, this is a debt. Fifty gold pieces."
    sensation "The number settles in your chest like a stone. You don't fully grasp the currency yet, but you understand weight."
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene91_choice08 with dissolve

label scene91_choice08_op2:
    $ mc_debt = True
    scene 91_s67 with dissolve
    mc "Fifty gold. It's a fair price for the risk you took and the craft you put into this. You have my word, it may take time, but you will be paid."
    scene 91_s68 with dissolve
    dean "Good. A man who recognizes a debt is a man who intends to survive long enough to settle it. See that you do. Now, go. The night won't last forever."
    scene 91_s67 with dissolve
    jump scene91_8

label scene91_choice08_op1:
    scene 91_s69 with dissolve
    mc "Fifty gold is a price placed on an object. What you've given me is a tool for a cause."
    mc "I will repay you, Dean, but not with coin. I'll repay you with a city freed, with justice dragged back into the light. Your metal will be part of the hand that tears down Avery's lies. That is the contract I offer."
    scene 91_s68 with dissolve
    dean "...Ha. Bold words. I've little use for grand promises. But I find I've even less use for safe men with quiet hearts."
    dean "Very well. Let your actions be the currency, then. *chuckles* Now get out of my smithy before I change my mind and decide to charge you interest."
    scene 91_s67 with dissolve
    jump scene91_8

label scene91_choice08_op1_2:
    empathy "You hesitate before uttering the words. You know you can't promise such a thing. Not yet, at least."
    call screen scene91_choice08 with dissolve

label scene91_8:
    stop music fadeout 5.0 
    scene 91_s71 with Dissolve(1.0)
    mc "Yuuhi... can I keep the mask? I may need it."
    scene 91_s72 with dissolve
    yuuhi "Of course. Though I should ask how much you're planning to pay for it—"
    yuuhi "...Just kidding. You can have it."
    yuuhi "But promise me one thing. If you ever find out it's the real thing, return it. Something like that belongs in a museum, not lost in an alley or soaked in blood."
    scene 91_s71 with dissolve
    mc "*chuckles* Fair enough."
    if mc_choose_amelia:
        mc "Oh, and before I go, do you have a pen and paper? I'm most likely not making my deadline, so I should leave a note behind."
        mc "I don't want my friend to start frantically looking for me."
        scene 91_s72 with dissolve
        yuuhi "Of course."
        scene 91_s71 with dissolve
    scene 91_s73 with Fade(1.3,1.0,1.5)
    play music "gameplay_night.mp3" fadein 4.0 volume 0.5 loop
    env "Lanternlight spills across the cracked pavement, dull gold against cold stone. Somewhere nearby, a couple sits in silence, shoulder to shoulder, watching the moon as if it might answer something they're afraid to ask."
    scene 91_s74 with Dissolve(1.5)
    yuuhi "So. You're leaving again."
    mc "I am."
    yuuhi "..."
    call screen scene91_choice09 with dissolve

label scene91_choice09_op1:
    $ mc_kiss_yuuhi_leaving = True
    $ yuuhi_love += 30
    scene 91_s76 with Dissolve(1.5)
    ""
    if mc_harem_yuuhi:
        scene 91_s78 with Dissolve(1.3)
        yuuhi "...That's not a goodbye."
        scene 91_s77 with dissolve
        mc "It's not. It's a 'wait for me'."
        scene 91_s78 with dissolve
        yuuhi "I will. I always do."
        yuuhi "*sigh* Now go, before I decide to chain you to the anvil."
        scene 91_s77 with dissolve
        scene black with Fade(1.3,1.0,1.3)
        sensation "You nod then melt back into the shadows of the alley, the weight of the new metal hand heavy."

    else:
        $ mc_kiss_yuuhi_nonharem = True
        scene 91_s78 with Dissolve(1.3)
        yuuhi "...Wha... Why did you..."
        scene 91_s77 with dissolve
        mc "I don't know. Maybe because I might not get another chance to be foolish."
        scene 91_s78 with dissolve
        yuuhi "That was... foolish. ...You don't get to do that and then disappear."
        scene 91_s77 with dissolve
        mc "I know."
        scene 91_s78 with dissolve
        yuuhi "Just don't make it the last thing I remember about you."
        scene 91_s77 with dissolve
        scene black with Fade(1.3,1.0,1.3)
        sensation "You nod then melt back into the shadows of the alley, the weight of the new metal hand heavy."
        
    if mc_choose_amelia:
        jump scene92
    else:
        jump scene96

label scene91_choice09_op2:
    mc "Goodbye, Yuuhi. Thank you. For everything."
    yuuhi "Don't thank me. Just... come back. In one piece. Preferably with both hands this time."
    mc "I'll do my best."
    scene black with Fade(1.3,1.0,1.3)
    sensation "You nod then melt back into the shadows of the alley, the weight of the new metal hand heavy."
    if mc_choose_amelia:
        jump scene92
    else:
        jump scene96


label scene92:
    $ mc_choose_ava_after_amelia = True
    scene 92_s1 with Fade(1.0,1.0,1.1)
    mc "Come on, girl. You've had your rest. Time to move. We can reach the swamp in a few hours if we're quick enough."
    stop music fadeout 2.0 
    scene 92_s2 with Fade(1.5,1.0,1.0)
    play music "night.mp3" fadein 1.0 loop
    mc "(Hopefully she's still here. And damn this place smells worse than I remember.)"
    scene 92_s3 with Fade(1.0,1.0,1.0)
    mc "(Shit. How do I even start this? 'Sorry I ghosted you, need a favor'?)"
    logic "Directness. Apology. Then the request."
    mc "Here goes..."
    scene 92_s4 with dissolve
    amelia "Are you just going to stand there? The door is open."
    mc "(Wha—!? What was that?)"
    mc "(Is she in my head? Right. Of course she is...)"
    stop music fadeout 1.0 
    scene 92_s5 with Fade(0.5,0.5,0.5)
    play sound "sound_effects/door_close.mp3"
    mc "*ahem* Hey, Amelia. Been a while, huh?"
    mc "Seriously, if you knew the kind of shit I've been through."
    mc "And, uh... sorry for not stopping by. For tea. Or anything."
    play sound "sound_effects/rnr/rnr_magic.mp3"
    play music "witch.mp3" fadein 1.0 loop
    scene 92_s6 with vpunch
    amelia "You fool! Do you have any concept of time? Of a promise?"
    play sound "sound_effects/rnr/rnr_magic.mp3"
    scene 92_s8 with Dissolve(1.0)
    sensation "Something unseen closes around your throat, hard and merciless, stealing your breath mid-word."
    mc "Ghhk! Amelia! I need— help!"
    scene 92_s6 with Dissolve(1.0)
    amelia "We had a pact! You would check in. You would be my anchor. In exchange, I spared your precious city folk from my... hungers."
    amelia "Yet you vanished. And now you come back, without your pretty resistant armor, so terribly, terribly vulnerable."
    scene 92_s7 with dissolve
    mc "I know! I'm sorry! Just... let me down! Can't... breathe!"
    scene 92_s9 with dissolve
    amelia "..."
    play sound "sound_effects/bodydrop3.mp3"
    scene 92_s10 with vpunch
    mc "Hahh! Ahhh... *cough* *cough*"
    scene 92_s11 with Dissolve(1.3)
    amelia "*sigh* Forgive the dramatics, darling. But solitude does terrible things to a woman's temperament. This swamp is so very quiet without someone to... talk to."
    mc "*cough* *cough* Right. I can see that."
    scene 92_s12 with Dissolve(1.0)
    amelia "We have catching up to do."
    scene 92_s13 with dissolve
    mc "Yeah... about that."
    scene 92_s12 with dissolve
    amelia "First, pants off."
    scene 92_s13 with dissolve
    mc "Wait! I'm serious. I need your help. Look."
    scene 92_s14 with dissolve
    amelia "Hm?"
    scene 92_s15 with dissolve
    amelia "A new toy? Charming. What of it?"
    scene 92_s14 with dissolve
    mc "*sigh* It's a prosthetic. The smith who forged it said it needs a powerful enchantment to become real. To work like a real hand. You're the strongest sorcerer I know."
    mc "With two hands, things will be easier. I can act faster. I can take down Avery... She's unlawfully—"
    scene 92_s16 with dissolve
    amelia "Do not bore me."
    amelia "I do not care about your crusade against the false queen, or your missing limb. Irrelevant, all of it. I care about our agreement."
    scene 92_s13 with Dissolve(1.0)
    mc "...Alright. That saves me repeating myself."
    scene 92_s12 with dissolve
    amelia "You still have that 'limb' down there, yes?"
    scene 92_s13 with dissolve
    mc "I do. And believe me, it would've been a tragedy to lose {i}that{/i} as well."
    mc "*ahem* No offense, but can you actually do it? Enchanting my prosthetic?"
    scene 92_s17 with Dissolve(1.0)
    amelia "Oh, my sweet fool. I'm not the same person you met last time. I have spent every silent day and starless night studying, consuming, growing. My power would but shatter the mind of the woman you met."
    amelia "My crows told me you were a nobody then. A novice. To be defeated by such a one... it was a lesson. I have learned."
    scene 92_s18 with dissolve
    mc "And you're using this power for... what, exactly?"
    scene 92_s17 with dissolve
    amelia "For whatever I please. Unless, of course, someone were foolish enough to keep me... occupied."
    scene 92_s18 with dissolve
    mc "So, you want to have your way with me in exchange for your help?"
    scene 92_s17 with dissolve
    amelia "Look at you, my sweetling is so, so smart!"
    scene 92_s18 with dissolve
    mc "Will you tie me up to the same device... thingy? I'd rather know what I'm walking into."
    scene 92_s19 with dissolve
    amelia "No. That."
    scene 92_s20 with Dissolve(1.0)
    perception "She gestures towards strange contraption against the wall. The user lies on their waist, limbs secured. Something designed for prolonged extraction."
    mc "You're certainly creative. Did you make this for me?"
    scene 92_s12 with Dissolve(1.0)
    amelia "Mhm. The way your squirmed last time, it inspired me!"
    amelia "Lie down on it~ I've missed this so very much—hearing the whines and cries of a man at my mercy... Ah! It gives me the shivers already."
    scene 92_s13 with dissolve
    mc "How... how long would this take? I'm on the clock here."
    scene 92_s12 with dissolve
    amelia "I suppose I can't keep you forever... for my pleasure alone."
    amelia "Let me look for something."
    scene 92_s13 with dissolve
    scene 92_s21 with Dissolve(2.0)
    amelia "Hmm..."
    mc "..."
    scene 92_s22 with Dissolve(1.0)
    amelia "Aha! How about this? You'll fill this entire chalice with your seed. Not a drop less, until it overflows."
    scene 92_s23 with dissolve
    mc "T-That's huge!"
    scene 92_s22 with dissolve
    amelia "Mhm~ And once you get in, no matter how much you beg, whine, or plead, I won't stop. I'll tease, pleasure, milk you until this chalice is full."
    scene 92_s23 with dissolve
    call screen scene92_choice01 with dissolve

label scene92_choice01_op1:
    $ in_scene93 = True
    $ mc_agree_help_amelia_milking = True
    mc "Do what you wish to me!"
    scene 92_s22 with dissolve
    amelia "*giggles* Oh, wonderful! Let's hope you don't swallow those words later."
    amelia "Wait here like a good boy. I'll just do a quick change to something more... suitable for our game."
    scene 92_s23 with dissolve
    stop music fadeout 1.0 
    scene 93_s1 with Fade(1.0,1.3,1.0)
    play music "ambiance/witch_bubble.mp3" fadein 1.0 volume 0.1 loop
    mc "(I might as well look around until she returns.)"
    $ mc_overview_open = True
    show screen mc_stats with dissolve
    $ in_free_roam = True
    mc "(Hm, it's been a while since I checked my Irda ID card... It's pretty much useless and outdated now.)"
    hide screen mc_stats with dissolve
    $ in_scene93 = False
    $ current_objective = "I don't even know what day it is. Things have been \nso hectic lately that I've barely had time to gather \nmy thoughts. The important thing is that I managed\nto convince Dean, the blacksmith, to forge a new\nhand for me. \n\nNow all it needs is an enchantment to make it real. \nI barely understand how that would even work, but \nI sought out Amelia to see to it. \n\nI hope she knows what she's doing."
    $ second_objective = ""
    $ third_objective = ""
    $ mc_overview_open = False

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene93_free_roam with dissolve

label scene92_choice01_op2:
    mc "Wait... this was a mistake. I changed my mind."
    scene 92_s24 with dissolve
    amelia "You... changed your mind!?"
    amelia "Have you forgotten our pact? I refrain from hunting your precious city folk... as long as you offer yourself to me."
    amelia "Are you truly going back on your word? If so... I'll have no choice but to seek entertainment elsewhere."
    scene 92_s25 with dissolve
    mc "..."
    call screen scene92_choice02 with dissolve
    
label scene92_choice02_op1:
    $ in_scene93 = True
    $ mc_agree_help_amelia_milking = True
    mc "Come on, Amelia... I was joking."
    mc "Of course I'll do it. Haha..."
    scene 92_s22 with dissolve
    amelia "I see. You're not entirely stupid after all."
    amelia "Wait here like a good boy. I'll just do a quick change to something more... suitable for our game."
    scene 92_s23 with dissolve
    stop music fadeout 1.0 
    scene 93_s1 with Fade(1.0,1.3,1.0)
    play music "ambiance/witch_bubble.mp3" fadein 1.0 volume 0.1 loop
    mc "(I might as well look around until she returns.)"
    $ mc_overview_open = True
    show screen mc_stats with dissolve
    $ in_free_roam = True
    mc "(Hm, it's been a while since I checked my Irda ID card... It's pretty much useless and outdated now.)"
    hide screen mc_stats with dissolve
    $ in_scene93 = False
    $ current_objective = "I don't even know what day it is. Things have been \nso hectic lately that I've barely had time to gather \nmy thoughts. The important thing is that I managed\nto convince Dean, the blacksmith, to forge a new\nhand for me. \n\nNow all it needs is an enchantment to make it real. \nI barely understand how that would even work, but \nI sought out Amelia to see to it. \n\nI hope she knows what she's doing."
    $ second_objective = ""
    $ third_objective = ""

    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene93_free_roam with dissolve

label scene92_choice02_op2:
    $ mc_disagree_help_amelia_milking = True
    mc "Find someone else. I'm still leaving."
    scene 92_s24 with dissolve
    amelia "Then consider our pact dissolved. Begone."
    amelia "And never show your face to me again... next time you and I meet, I won't be so merciful."
    scene 92_s25 with dissolve
    stop music fadeout 1.0 
    scene 92_s29 with Fade(1.0,1.0,1.5)
    mc "(Dammit... Almost an entire day wasted.)"
    mc "Hurry up, girl. We can't waste more time."
    jump scene96

label scene92_choice02_op3:
    stop music fadeout 1.0 
    scene 92_s26 with dissolve
    mc "I should've captured you last time!"
    play sound "sound_effects/rnr/rnr_magic.mp3"
    scene 92_s27 with vpunch
    sensation "Before your fist connects, the invisible force clamps your neck again even harder and more vicious this time. You sense intense hatred around you."
    mc "Ghkn!"
    amelia "Tsk, tsk. Wrong move, darling."
    amelia "You see, I never actually removed my spell. It was still there... just hidden."
    sensation "The grip shifts from your neck to your head, twisting sideways with unnatural strength. Bones creak, vision blac—"
    play sound "sound_effects/body/bonecrack.mp3"
    scene 92_s28 with vpunch
    amelia "What a shame. Such potential... wasted."
    return

default in_scene93 = False

label scene93:
    scene 93_s1 with dissolve
    call screen scene93_free_roam with dissolve

label scene93_free_roam_left:
    scene 93_s3 with dissolve
    call screen scene93_free_roam_left with dissolve

default scene93_free_roam_pixie_first = False
label scene93_free_roam_pixie:
    $ scene93_free_roam_pixie_first = True
    mc "What the—? Is someone in there?"
    perception "Suspended among dried herbs and nondescript vials, is a small iron cage. Inside, something faintly luminous lies curled and utterly still."
    mc "H-Hello?"
    scene 93_s4 with dissolve
    perception "As you lean closer, you realize it's not a doll, nor a corpse. Tiny wings, translucent like cracked glass are folded tight against a frail, glowing form."
    mc "...A pixie?"
    mc "Hey. Can you hear me?"
    pixie "Hnnm?"
    scene 93_s6 with Dissolve(1.0)
    perception "The creature stirs, a dim pulse of light rippling weakly through her body. Slowly, she lifts her head, eyes like polished dew fixing on you."
    scene 93_s5 with dissolve
    pixie "Oh. You are... new here."
    scene 93_s6 with dissolve
    mc "Y-You can talk?"
    scene 93_s5 with dissolve
    pixie "Once, I sang."
    pixie "Now I am kept."
    scene 93_s6 with dissolve
    mc "Are you... okay?"
    pixie "Hmm."
    scene 93_s5 with dissolve
    pixie "Great tragedy has befallen you."
    scene 93_s6 with dissolve
    mc "...What?"
    scene 93_s5 with dissolve
    pixie "Something old has brushed against you and found you... suitable."
    scene 93_s6 with dissolve
    mc "I don't know what you're talking about."
    pixie "..."
    mc "Do you want to be free?"
    scene 93_s4 with Dissolve(1.2)
    perception "For a moment, her glow flickers, hesitant, uncertain. Then the light fades, her small form curling in on itself once more."
    scene 93_s3 with Dissolve(1.3)
    call screen scene93_free_roam_left with dissolve
    
label scene93_free_roam_right:
    scene 93_s2 with dissolve
    call screen scene93_free_roam_right with dissolve

label scene93_free_roam_right_device:
    mc "(So that's where I'm meant to lie. Strapped down like an animal...)"
    call screen scene93_free_roam_right with dissolve

label scene93_free_roam_up:
    hide screen s93_hover_areas4
    scene 93_s7 with dissolve
    call screen scene93_free_roam_up with dissolve

label scene93_free_roam_up_door:
    mc "(Amelia went in there to change, as if modesty matters now. I've already seen her naked before.)"
    call screen scene93_free_roam_up with dissolve

default scene93_free_roam_up_right_poster = True
label scene93_free_roam_up_right:
    if scene93_free_roam_up_right_poster:
        scene 93_s8_2 with dissolve
    else:
        scene 93_s8 with dissolve
    call screen scene93_free_roam_up_right with dissolve

label scene93_free_roam_up_right_poster:
    $ persistent.diana_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene93_free_roam_up_right_poster = False
    jump scene93_free_roam_up_right

label scene93_free_roam_up_right_could:
    perception "The liquid inside the cauldron is too thick to be water, too alive to be stew, rising in lazy blisters. Strangely, it carries no scent at all."
    call screen scene93_free_roam_up_right with dissolve
label scene93_free_roam_up_right_skull:
    mc "(That's... real. I wonder if it belonged to one of her previous 'toys'.)"
    call screen scene93_free_roam_up_right with dissolve

label scene93_free_roam_up_left:
    scene 93_s9 with dissolve
    call screen scene93_free_roam_up_left with dissolve

label scene93_free_roam_up_left_ball:
    mc "(A glass sphere. Strange... I can't see my reflection in there.)"
    call screen scene93_free_roam_up_left with dissolve
label scene93_free_roam_up_left_chalice:
    mc "(This is way too big! There's no way I'm filling this whole thing up... right?)"
    call screen scene93_free_roam_up_left with dissolve
label scene93_free_roam_up_left_book:
    $ mc_learned_amelia_death_res = True
    perception "A heavy book rests open on her desk, its script written in a language you don't understand. The margins are crowded with sketches, circles and bodies. It appears to be instructions for pulling something back from the grave."
    mc "(Some of these 'instructions' are crossed out. Was she really trying to bring someone from the dead?)"
    call screen scene93_free_roam_up_left with dissolve

label scene93_free_roam_end:
    call screen scene93_free_roam_end with dissolve
    call screen scene93_free_roam_up with dissolve

image s94_w1 = Movie(play="images/chapter4/scene94/s94_w1.webm", loop=True)
image s94_w2 = Movie(play="images/chapter4/scene94/s94_w2.webm", loop=True)
image s94_w3 = Movie(play="images/chapter4/scene94/s94_w3.webm", loop=True)
image s94_w4 = Movie(play="images/chapter4/scene94/s94_w4.webm", loop=True)
image s94_w5 = Movie(play="images/chapter4/scene94/s94_w5.webm", loop=True)
image s94_w6 = Movie(play="images/chapter4/scene94/s94_w6.webm", loop=True)

label scene94:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene3_p7_replay:
        $ persistent.scene3_p7_replay = True

    $ in_free_roam = False
    scene 94_s1 with Fade(1.5,1.0,1.3)
    amelia "I'm ready. Follow me, darling. And don't forget to bring my contraption with you."
    scene 94_s2 with dissolve
    stop music fadeout 1.0 
    scene 94_s3 with Fade(1.2,1.0,1.0)
    amelia "Assume the position. Let's begin our arrangement~"
    scene 94_s5 with Fade(1.0,1.0,1.0)
    perception "You lower yourself onto the device as instructed. Chest pressed to the smooth wood, arms and legs dangling down the sides in vulnerable exposure."
    scene 94_s4 with dissolve
    amelia "Perfect, darling. Just like that. So obedient already."
    scene 94_s5 with dissolve
    perception "The position leaves you arched slightly, ass raised, completely open, like a bound animal waiting for its owner."
    scene 94_s4 with dissolve
    amelia "Let me secure you properly. Wouldn't want my favorite toy running off mid-play~"
    scene 94_s5 with dissolve
    scene 94_s6 with Dissolve(1.0)
    mc "..."
    mc "(God... what the hell am I doing?)"
    scene 94_s7 with Fade(0.5,0.5,0.5)
    amelia "Mmm... look at you. All mine."
    sensation "Her nails drag lightly down your spine, sending shivers racing through you. Goosebumps rise in their wake."
    amelia "So tense... relax, darling. This is going to be delicious."
    scene 94_s9 with Fade(0.5,0.5,0.5)
    perception "She settles between your spread legs, her presence an overwhelming heat. Her gaze fixed on your cock."
    scene 94_s8 with dissolve
    amelia "It seems your cock is already begging for my attention, already hard and twitching. Should I give it what it wants, I wonder..."
    scene 94_s9 with dissolve
    mc "Y-Yes..."
    scene 94_s8 with dissolve
    amelia "Awww~ I can't deny such an honest request."
    scene 94_s9 with dissolve
    show s94_w1 with Fade(1.0,1.0,1.0)
    sensation "Her hand wraps around your shaft, cool fingers at first, then warming as she strokes slowly, base to tip. A firm squeeze at the head draws a bead of precum."
    amelia "Already leaking for me. Good boy."
    amelia "I'll start gentle... build you up nice and slow."
    sensation "She pumps steadily. Long, twisting strokes that make your hips jerk against the restraints."
    amelia "Mmm~ Feel that? Every stroke pulling more out of you..."
    mc "Amelia... fuck..."
    amelia "That's it... throb for me. I want to feel you swell."
    amelia "Imagine it... that clear glass growing cloudy and warm. All your precious seed, given to me~"
    mc "Hahh! Close... I'm—"
    amelia "Not yet."
    mc "Hngg..."
    amelia "*giggles* No ejaculating without permission."
    amelia "We have all night, darling. I'll bring you to the brink... again and again... until you're desperate."
    mc "Ahhn... I'm getting dizzy again..."
    amelia "Feel them getting heavy? Full for me?"
    mc "(She's too good at this... fuck... I feel like an ocean of my stuff will spill out if she ever lets me.)"
    amelia "Mhhnmmm~ You're dripping so much already... going to fill my chalice beautifully."
    amelia "Your asshole looks delicious~ Perhaps I can milk your prostate too... if you ask nicely, that is."
    mc "..."
    amelia "Go on. Beg for it. Beg your wicked witch to finger your tight hole while I stroke you."
    call screen scene94_choice01 with dissolve


label scene94_choice01_op1:
    $ mc_prostate_amelia = True
    mc "Please... Do it."
    amelia "*chuckles* There's my good boy~"
    scene 94_s25 with Dissolve(1.0)
    sensation "She slicks a finger with her own spit and the steady drip of your precum, then presses them against your entrance. Slow, teasing circles at first."
    show s94_w2 with Dissolve(1.0)
    amelia "Relax for me... let me in..."
    sensation "The first finger slides past the ring with gentle pressure, hot, tight, overwhelming. She curls it immediately, searching."
    amelia "There it is... your sweet spot."
    sensation "She presses firmly against your prostate with slow, rhythmic strokes in time with her hand on your cock. The dual stimulation hits like lightning: pressure inside, stroking outside, pleasure doubling, tripling."
    mc "Fuck! Amelia!"
    amelia "Feel that? That's your special spot, it'll make you come sooner... and harder. *chuckles* You'll be leaking nonstop."
    amelia "So tight... so greedy... clenching around my fingers like you never want me to leave."
    mc "I'm... I'm gonna—"
    amelia "Not yet. Hold it. Let it build until you're sobbing."
    sensation "The pressure is unbearable. Your prostate is throbbing under her finger, cock pulsing in her grip, balls drawn tight. You're dripping constantly, a thin stream pooling on the floor."
    amelia "Beg again. Louder. Tell me you need to ejaculate."
    mc "Please... Amelia... let me cum!"
    amelia "Good boy."
    amelia "Then ejaculate for me. Fill my chalice, now!"
    call screen scene94_choice02 with dissolve

label scene94_choice01_op2:
    mc "No... I don't want that!"
    amelia "Oh? Refusing your sweet witch already?"
    amelia "*tch* Such a pity. I was going to make you come so hard your vision went white."
    amelia "But if you don't want my fingers inside you..."
    mc "Amelia—"
    amelia "Shh. You had your chance."
    amelia "Then we'll do this my way... and you'll regret saying no."
    show s94_w3 with Dissolve(1.0)
    sensation "Her fingertips return, but only to the tip. She circles the sensitive glans with feather-light touches, then suddenly flicks the slit rapidly in quick, sharp, relentless little taps and swirls."
    mc "Fuck! Too much!"
    amelia "*giggles* Too much? Darling, this is nothing."
    amelia "Feel that? Every tiny nerve screaming... but no deeper relief."
    sensation "The stimulation is maddening. She's only focused on the tip, the rest of your cock untouched and aching. Precum wells up constantly, dribbling down her fingers as she spreads it in slippery circles."
    mc "Uhhnn... Amelia... please stroke it properly!"
    amelia "No~ You didn't want my fingers inside. So you get only the tip. Over... and over... and over..."
    amelia "Look how red and swollen it is... *giggles* You're trying so hard to come, aren't you?"
    mc "I can't! It's... it's too sensitive! I need—"
    amelia "Need what? To ejaculate? You can't. Not yet."
    sensation "The pinching sends sharp jolts of pleasure-pain through you. Your cock twitches violently."
    amelia "See how you tremble? How your balls are so tight they hurt? That's what happens when you deny me."
    mc "Please... Amelia... let me cum!"
    amelia "Good boy."
    amelia "Then ejaculate for me. Fill my chalice, now!"
    call screen scene94_choice02 with dissolve
    
label scene94_2:
    mc "I'm!"
    play sound "se_sfx/sex/sex_cum9.mp3" 
    if mc_prostate_amelia:
        scene 94_s10 with vpunch
    else:
        scene 94_s11 with vpunch
    mc "AAAGGHHNN!"
    sensation "Thick, hot ropes shoot into the waiting chalice, each spasm wrenched from you with a force that borders on pain, pleasure so intense it steals the air from your lungs."
    play sound "se_sfx/sex/sex_cum7.mp3" 
    scene 94_s12 with vpunch
    amelia "Yes~! That's it... so much already..."
    amelia "Don't leave a single drop. Let it all out. Good..."
    scene 94_s13 with Dissolve(1.0)
    amelia "Hmm... Not bad but the chalice's barely started."
    mc "Wait! Too much!"
    amelia "No waiting. You'll give me more. All of it."
    mc "It's too sensitive now—"
    show s94_w4 with Dissolve(1.0)
    sensation "Before you can protest further, she bends your cock backward, gentle but firm. She guides the oversensitive head between her warm lips. The sudden wet heat envelops you completely, tongue swirling around the tip."
    amelia "Mhmmmm..."
    mc "Fuck! Amelia!"
    sensation "Her mouth is velvet, hot, slick, relentless. She takes you deeper slowly, lips sealing tight, cheeks hollowing as she sucks."
    amelia "You taste divine... all that seed still lingering. *slurp* I could do this for hours."
    amelia "Mmmph~ So hard again already... my greedy boy. You're thinking of spilling all your seed in my throat?"
    mc "Too much! I can't—"
    amelia "*slurp* *suck* Can't? Or won't? Your cock says otherwise... throbbing so prettily in my mouth."
    amelia "Mhm~ Give me another load... fill my mouth this time..."
    mc "(Her tongue is proding my penis hole! This is too intense!)"
    mc "Stop focusing on that one part only!"
    mc "I-I think I might cum already!"
    amelia "Which part? This?"
    mc "Ahhnn~!"
    amelia "Mmmm~ This is where all the tasty seed will come out from. I must bully and tease it properly."
    amelia "But don't even think of ejaculating just yet. I want you {i}desperate{/i}."
    sensation "She continues the assault on your tip. Her tongue presses hard against the underside, swirling relentlessly while she hums low in her throat."
    amelia "Mmmph~ Throb for me... give me everything..."
    mc "Amelia! Fuck! I can't hold it..."
    mc "Please! I'm—!"
    amelia "*slurp* Mfhhmmm~"
    amelia "Mmmm! You're twitching so hard~ Did my boy reach his limit?"
    mc "Yes!"
    amelia "Very well. Ejaculate in my mouth... fill it with your tasty seed!"
    call screen scene94_choice05 with dissolve
    play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
    scene 94_s28 with vpunch
    mc "Ahnngg!"
    sensation "The pleasure explodes. Hot, thick spurts flood her mouth in waves. She swallows the first instinctively, then seals her lips tight, taking every pulse."
    play sound "se_sfx/blowjob/blowjob_cum2.mp3" 
    scene 94_s29 with vpunch
    amelia "Mfhmm..."
    mc "Hahh... god..."
    play sound "se_sfx/blowjob/blowjob1.mp3" 
    scene 94_s30 with Dissolve(1.0)
    perception "She lets go of your cock with a pop, turning to the chalice on the floor now covered with saliva. Slowly, she parts her lips—letting the thick load spill in a glistening stream into the glass."
    play sound "se_sfx/blowjob/facial2.mp3" 
    scene 94_s31 with Dissolve(1.0)
    amelia "Blaahhnn..."
    scene 94_s32 with Dissolve(1.0)
    amelia "Mmm... second contribution. So much already."
    amelia "But the chalice's still not full, dear. I think just one more try would fill it up."
    amelia "Ready for round three? Or shall I make you beg first?"
    scene 94_s18 with dissolve
    mc "Hnnn... you're insane."
    scene 94_s19 with dissolve
    amelia "What was that? I couldn't hear you."
    scene 94_s18 with dissolve
    mc "Nothing..."
    scene 94_s19 with dissolve
    amelia "Good boy. Learning already."
    jump scene94_3
label scene94_3:
    scene 94_s14 with Fade(1.0,1.0,1.0)
    amelia "Let's do something different this time."
    mc "Hahh... wait, what do you mean?"
    perception "She reaches for a small vial on the table. Inside swirls a viscous, reddish liquid. She uncorks it, letting a single drop fall onto her palm before tipping the rest into her hand."
    mc "W-What are you doing?"
    scene 94_s15 with Dissolve(1.3)
    amelia "Don't worry, darling. It's not dangerous... if used cautiously."
    scene 94_s16 with dissolve
    mc "Huh!? Is that the same liquid you used on me last time?"
    scene 94_s15 with dissolve
    amelia "You'll see~"
    scene 94_s16 with dissolve
    scene 94_s17 with Fade(1.0,1.0,1.0)
    play sound "se_sfx/sex/sex3.mp3" 
    sensation "She brings her palm to your cock and smears the slippery liquid along your length. Suddenly, a violent wave of pleasure crashes through you. Your skin turns hypersensitive, cock throbbing as though it's been edged for hours."
    mc "W-What is this!? I feel... like I'm about to cum already!"
    scene 94_s19 with Dissolve(1.0)
    amelia "Beautiful, isn't it? My latest discovery, a concoction far more potent than my previous little experiment."
    amelia "It heightens the senses to their absolute limit. Every touch... every breath of air against you... will feel like the edge of ecstasy."
    scene 94_s18 with dissolve
    mc "Why didn't you do this before? We could've... finished by now..."
    scene 94_s19 with dissolve
    amelia "Where's the fun in rushing? I want to savor you."
    amelia "Besides... I did cast a spell on you."
    scene 94_s18 with dissolve
    mc "A spell? But I don't feel anything... aside from that liquid."
    scene 94_s19 with dissolve
    amelia "Patience, darling. You'll feel it soon enough. For now, think about my large breasts smothering your cock." 
    show s94_w5 with Dissolve(1.5)
    perception "She shifts closer between your legs. She then presses forward her soft, heavy breasts that envelope your cock completely."
    mc "Ahh... so soft."
    sensation "Silken skin slides against your cock, impossibly soft yet firm. She squeezes them together, trapping you fully as she begins a fast glide."
    amelia "Like that? My breasts were made for this~ Wrapping you up, milking you dry..."
    mc "I'm... I'm already cuming—!"
    amelia "..."
    mc "W-What's happening!? I can't—!"
    amelia "*laughs* There it is. My secret spell, orgasm denial."
    amelia "You'll feel everything... build to the brink... but release? Only when I lift the spell."
    mc "That's so cruel!"
    amelia "Cruel? Or exquisite? You're throbbing so hard between my cleavage... leaking steadily... but stuck forever on the edge."
    sensation "Every glide is pure torture, pleasure mounting impossibly high, balls aching with need, but no relief. Precum flows freely, coating her cleavage in glistening trails."
    scene black with Dissolve(0.3)
    show s94_w6 with Dissolve(1.0)
    mc "Amelia... please... let me come..."
    amelia "Poor darling. So full... so desperate..."
    mc "I-I might go crazy... Hnn... if you keep doing this."
    amelia "*giggles* Feel that? Every nerve screaming for release... but I'm not ready to let you have it."
    sensation "The heightened spell amplifies everything, the velvet slide of her skin, the wet sounds, the ache deep in your core. You're throbbing helplessly, on the brink but forever denied."
    mc "Please... I'll do anything..."
    amelia "Anything? Such pretty words."
    amelia "But I want more than words. I want you broken open... begging like you mean it."
    mc "I am begging—"
    amelia "Not yet. Not enough."
    amelia "Just enjoy the sensation, darling. It's not often you get your cock squished between a pair of breasts like these. And even if you do, I doubt they're as big as mine."
    mc "(I might actually start crying... God!)"
    sensation "Pleasure coils tighter than ever, your vision blurs and your body trembles on the edge of passing out."
    scene black with Dissolve(0.3)
    show s94_w5 with Dissolve(1.0)
    amelia "Hooold~"
    mc "Ahh... hahh... hnn... ghnn."
    amelia "Does my boy want to release his seed now?"
    mc "Yes!"
    amelia "Does he want to spill out between my sweaty warm cleavage and paint them white?"
    mc "God, yes!"
    amelia "Then beg me properly. Let me know that you truly want it. Surrender yourself to me, your new mistress!"
    call screen scene94_choice03 with dissolve

label scene94_choice03_op1:
    $ mc_beg_amelia = True
    mc "Please, Amelia! Mercy! Let me cum! I can't take it anymore! Please!"
    amelia "Yes~! That's it..."
    amelia "Come for me now! Explode!"
    call screen scene94_choice04 with dissolve

label scene94_choice03_op2:
    mc "..."
    scene black with Dissolve(0.3)
    show s94_w6 with Dissolve(1.0)
    amelia "Still fighting? Admirable... but futile."
    amelia "Then we'll go longer... let it hurt so good..."
    amelia "Feel that ache? That's all for me."
    mc "Nghnn..."
    amelia "*chuckles* It feels like you're about to pass out."
    amelia "I'm merciful so I won't let that happen to my dear boy."
    amelia "Fine... come anyway. Give it all."
    call screen scene94_choice04 with dissolve

label scene94_4:
    sensation "The denial spell lifts and pleasure detonates in a blinding wave."
    play sound "se_sfx/sex/sex_cum6.mp3" 
    scene 94_s20 with vpunch
    mc "NGHAAAA—!"
    sensation "Thick ropes erupt between her breasts, endless spurts painting her skin white, overflowing from her cleavage into the chalice below in heavy streams."
    play sound "se_sfx/sex/sex_cum3.mp3" 
    scene 94_s21 with vpunch
    amelia "Yes~! So much... beautiful, darling..."
    amelia "Keep pushing it out, squeeze your core harder~!"
    play sound "se_sfx/sex/sex4.mp3" 
    scene 94_s27 with Dissolve(1.0)
    amelia "Mmmm~ You made such a mess of my breasts. I can barely find a spot that is marked by you~"
    scene 94_s23 with Fade(1.0,1.0,1.0)
    mc "Hahhnn... Faaahh... Agghhnnn..."
    scene 94_s22 with dissolve
    amelia "Hush. I'll let you out now, my poor exhausted boy."
    scene 94_s23 with dissolve
    sensation "The leather straps loosen one by one, cool air rushing over heated skin as the circulation returns to your body."
    scene 94_s24 with Fade(0.5,0.5,0.5)
    amelia "Up you go... slowly now. Let's head up upstairs."
    $ renpy.end_replay()

label scene95:
    scene 95_s1 with Fade(1.3,1.0,1.1)
    play music "ambiance/witch_bubble.mp3" fadein 1.0 volume 0.1 loop
    mc "Hahh... God. I don't think I'll ever forget this feeling."
    scene 95_s2 with dissolve
    amelia "You certainly won't. And we can definitely recreate it, anytime you crave that edge again."
    scene 95_s1 with dissolve
    mc "I'm good. For... a long while."
    scene 95_s2 with dissolve
    amelia "Trust me, darling. You'll return on your own volition."
    amelia "This sensation? The build? The denial? The explosion?! No ordinary woman can give you that. Ever."
    amelia "You'll feel empty every time you finish elsewhere... always chasing what only I can provide."
    scene 95_s1 with dissolve
    mc "Great. You took my seed {i}and{/i} ruined my mind for anyone else."
    scene 95_s2 with dissolve
    amelia "A fair trade, wouldn't you say?"
    scene 95_s1 with dissolve
    mc "You got what you wanted and more. Now hold your end and enchant the prosthetic."
    scene 95_s2 with dissolve
    amelia "Of course. I never go back on my word."
    amelia "Let's step outside. I don't want you knocking over my shelves if things go... awry."
    scene 95_s1 with dissolve
    mc "Awry? Is this not safe?"
    scene 95_s2 with dissolve
    amelia "It's not {i}unsafe{/i}. Just... unpredictable. Enchanting living flesh to metal isn't something I do often."
    scene 95_s1 with dissolve
    mc "Dammit."
    scene 95_s2 with dissolve
    amelia "Calm down, dear. I'm sure everything will be just fine."
    scene 95_s1 with dissolve
    mc "*sigh* I didn't want to ask, but... what are you going to do with that?"
    scene 95_s3 with Dissolve(1.0)
    amelia "Oh, this? I haven't decided yet."
    amelia "Perhaps I'll keep it as a souvenir, a little reminder of how thoroughly I broke you tonight."
    amelia "Or... perhaps I'll use it to impregnate myself."
    scene 95_s4 with dissolve
    mc "Wait— what?"
    scene 95_s3 with dissolve
    amelia "Joking, of course. Carrying your offspring... such a silly idea."
    amelia "Though the thought did cross my mind for a moment. You're quite... potent."
    scene 95_s4 with dissolve
    mc "..."
    call screen scene95_choice01 with dissolve

label scene95_choice01_op1:
    $ mc_wants_impregnate_amelia = True
    mc "Honestly? I'd love to impregnate you myself."
    scene 95_s5 with Dissolve(1.0)
    amelia "E-Excuse me?"
    scene 95_s6 with dissolve
    mc "You're a little... weird. But you're very charming, Amelia."
    mc "Truth is, I had another option for enchanting this prosthetic. But I chose you."
    scene 95_s5 with dissolve
    amelia "Flattery after all that? Are you... stupid?"
    amelia "I'm a witch in case you forgot. I... I'm not exactly someone who you make a life with."
    scene 95_s6 with dissolve
    mc "I'm serious. I would love to be with you. To support you. To be mine."
    amelia "..."
    scene 95_s5 with dissolve
    amelia "I have truly never met a man like you before. You're either too brave or damaged in the head."
    amelia "Perhaps we'll discuss... natural methods... another time."
    scene 95_s6 with dissolve
    mc "Of course, I'll always come back for you."
    scene 95_s5 with dissolve
    amelia "*ahem* L-Let me get you your reward for now."
    amelia "*sigh*{size=30}Am I really falling for a man years younger than me...{/size}"
    scene 95_s6 with dissolve
    jump scene95_2

label scene95_choice01_op2:
    $ mc_wants_sovi_amelia = True
    mc "Keep it as a souvenir. A trophy from tonight."
    scene 95_s3 with dissolve
    amelia "A memento of your surrender. I'll treasure it."
    amelia "Maybe label it: 'From my favorite plaything's milking.'"
    scene 95_s1 with Dissolve(1.0)
    mc "*chuckles* You're twisted."
    scene 95_s2 with dissolve
    amelia "And you love it."
    amelia "*ahem* Enough teasing. Time for your reward."
    scene 95_s1 with dissolve
    jump scene95_2

label scene95_choice01_op3:
    $ mc_never_impregnate_amelia = True
    mc "It's a stupid idea. I'd never want that to happen."
    scene 95_s2 with Dissolve(1.0)
    amelia "Oh? So direct."
    amelia "No feelings for the witch who helped you climax so many times?"
    scene 95_s1 with dissolve
    mc "I appreciate you helping me but that's all there is to it."
    scene 95_s2 with dissolve
    amelia "Very well. It was merely a thought."
    amelia "*ahem* Enough teasing. Time for your reward."
    scene 95_s1 with dissolve
    jump scene95_2

label scene95_2:
    stop music fadeout 1.0 
    scene 95_s7 with Fade(1.3,1.0,1.3)
    play music "ambiance/witch_swamp.mp3" fadein 1.0 loop
    env "The croaking of frogs and the relentless buzz of insects fill the damp, stagnant air. Dead trees stand as silent, skeletal sentinels in the perpetual twilight of the swamp."
    amelia "Focus. On your arm and the prosthetic completely. Do not break concentration for even a second."
    mc "Understood."
    scene 95_s9 with Dissolve(1.0)
    amelia "*sigh*"
    empathy "She lets out a slow sigh. In the faint light, a flicker in her eyes, a tightness around her mouth that hadn't been there before. Hesitation."
    scene 95_s11 with Dissolve(1.0)
    mc "Amelia... Please tell me you actually know what you're doing."
    scene 95_s10 with dissolve
    amelia "If I said yes, I would be lying."
    amelia "You can still run away."
    scene 95_s9 with Dissolve(1.0)
    mc "I came this far. I did everything you asked. There's no turning back now."
    mc "Just... please be careful."
    scene 95_s8 with dissolve
    amelia "I'll try."
    play sound "sound_effects/magic/magic_spell.mp3"
    scene 95_s15 with Dissolve(1.0)
    perception "Her staff began to shimmer, emitting a dark green light that pushes back the gloom, painting your face in a sickly hue. She points the pulsating tip directly at your chest."
    mc "Whoa! Why are you pointing it at me?"
    scene 95_s16 with dissolve
    amelia "Do you want the prosthetic to control you, or the other way around?"
    scene 95_s15 with dissolve
    mc "Ah, right. Continue."
    scene 95_s16 with dissolve
    amelia "Bind this flesh to forgotten brass. Spirit severed and cold, to this vessel, be folded and sold."
    scene 95_s10 with Dissolve(1.0)
    mc "..."
    play sound "sound_effects/magic/magic_beam.mp3"
    scene 95_s12 with vpunch
    sensation "A bolt of violent energy shoots from her staff, a searing lance that punches the air from you lungs before dissolving into a bizarre, gentle warmth."
    scene 95_s14 with dissolve
    mc "I... I feel something."
    scene 95_s13 with Dissolve(1.0)
    amelia "Do NOT break your consentration!"
    mc "..."
    sensation "Vivid, chaotic imagery flood your mind. Memories of touch, of pressure, of flexing fingers that were no longer there, all screaming through the cold steel."
    amelia "Just a little... further."
    amelia "Dammit!"
    scene 95_s14 with dissolve
    mc "W-What?"
    scene 95_s17 with Dissolve(1.0)
    amelia "Focus Amelia!"
    scene 95_s18 with dissolve
    amelia "Nghnnn!"
    scene 95_s14 with Dissolve(1.0)
    mc "Amelia, your head! It looks like it's about to—"
    scene 95_s21 with Dissolve(1.0)
    play sound "sound_effects/magic/magic_stop.mp3"
    amelia "NHGNN!"
    mc "Stop!"
    play sound "sound_effects/bodydrop.mp3"
    scene 95_s19 with Dissolve(0.2)
    scene 95_s19 with vpunch
    perception "The staff flares one last time, then sputters out. Amelia staggers backward as if shoved, collapsing to the ground. The green glow fading from her staff."
    scene 95_s23 with Dissolve(1.0)
    mc "Amelia!"
    scene 95_s20 with Dissolve(1.0)
    amelia "Hahh... ahh... dammit, dammit, dammit!"
    scene 95_s22 with Dissolve(1.0)
    mc "Can you stand up?"
    scene 95_s24 with Fade(0.5,0.5,0.5)
    mc "You're okay?"
    amelia "Of course not! I... I couldn't hold the conduit. The spell fractured. It's gone."
    mc "*sigh* Fuck. At least you're okay."
    scene 95_s25 with Dissolve(1.0)
    amelia "Hnn... This headache. I apologize, [mc]. I was a fool. I should have experimented with a lesser casting first... tested the metaphysical flow. But I was so sure..."
    scene 95_s26 with dissolve
    mc "It's a bit late for regrets now."
    scene 95_s25 with dissolve
    amelia "I can tell you're not pleased. But this wasn't for nothing. You came back and honored our agreement."
    amelia "I swear, I will help you with... whatever mess you're currently in. Whatever you need. Consider my aid pledged, we're even that way."
    scene 95_s26 with dissolve
    mc "I was hoping for a working arm... but I suppose a debt from a witch is a close second."
    mc "Alright. Now for the immediate problem, it took me a long time to get here. I can't afford to waste another on the return."
    scene 95_s25 with dissolve
    amelia "I may be able to expedite your departure. It's the least I can do after my... failure."
    scene 95_s26 with dissolve
    mc "...How?"
    scene 95_s25 with dissolve
    amelia "A teleportation spell. A significant one, mind you. It will drain my mana to the dregs. I'll be useless for a week, maybe more."
    scene 95_s26 with dissolve
    mc "You can do that?"
    scene 95_s27 with dissolve
    amelia "But of course. *chuckles* How do you think I've evaded your city's guards all these years?"
    amelia "Very well, forget my future help. I'll teleport you back to the city now. That will make us even."
    scene 95_s28 with vpunch
    mc "Amelia!"
    scene 95_s27 with dissolve
    amelia "Sorry, sorry. Fine, I'll teleport you {i}and{/i} retain my pledge of assistance. A two-for-one bargain for my failure. Happy?"
    scene 95_s28 with dissolve
    mc "Good. Do it. Send me and my horse straight to an elven girl's house. Her name is Ava."
    scene 95_s27 with dissolve
    amelia "Darling, I do not know of any Ava. {i}You{/i} must know the place you're traveling to. You must hold its image, its essence, in your mind. It's the anchor."
    scene 95_s29 with Dissolve(1.0)
    mc "What happens if I don't know the place well enough?"
    scene 95_s30 with dissolve
    amelia "Oh dear. *laughs* Then you might be deposited into a rather... unpleasant adjacency. A wall. The foundation stones beneath a street. The bottom of a well."
    amelia "You would die, of course, but the real problem would be retrieving your body—or what's left of it. The mere act of—"
    scene 95_s28 with vpunch
    mc "Amelia, please! Just do it."
    scene 95_s27 with dissolve
    amelia "Yes, yes. I'll hurry up."
    play sound "sound_effects/magic/magic_warp.mp3"
    scene 95_s31 with Dissolve(1.0)
    amelia "*ahem* Now, close your eyes. Visualize a place in the city you know. Somewhere you have stood, breathed, and been. Your mind will be the compass."
    mc "..."
    mc "(I can teleport straight to Rebecca's bedroom, but that would be a death sentence. And she might not even be there to begin with... yeah better not.)"
    stop music fadeout 5.0 
    scene 95_s32 with Dissolve(3.0)
    ""
    scene 95_s33 with dissolve
    mc "(Huh? Holy shit, it actually worked! She's definitely useful to have around.)"
    scene 95_s34 with Dissolve(1.0)
    mc "Wait, [horse]? [horse], where are you?!"
    play sound "sound_effects/horse1.mp3"
    scene 95_s35 with Dissolve(1.0)
    horse "Neigh!"
    mc "*laughs* Oh... J-Just stay there, alright? I'll come back soon."
    play sound "sound_effects/running_concrete.mp3"
    scene 95_s36 with Dissolve(1.0)
    mc "(Now, to find her.)"
    jump scene96

label scene96:
    if mc_agree_help_amelia_milking or mc_disagree_help_amelia_milking:
        stop sound fadeout 1.0
        play music "wind.mp3" fadein 1.0 loop
        scene 96_s30 with Fade(1.3,1.0,1.2)
        mc "Hahh... hah... (Shit, where do I even start?)"
        if mc_execute_kat or mc_life_kat:
            shiver "A vision forms in your mind. A place, perfectly clear, as though you've stood there countless times before. A shiver runs through your body."
            scene 96_s31 with Dissolve(1.0)
            mc "(Huh!? Ahnng! My head... what was that? Was that where Ava lives?)"
            mc "(Who's telling me this? Amelia? I guess I have no choice but to trust it.)"
            scene 96_s6 with Fade(1.5,1.0,1.2)
            mc "(A blue door... the same one that appeared in my vision. Could she really be here?)"
            scene 96_s7 with Dissolve(1.0)
            "*knock* *knock* *knock*"
            jump scene100

        shiver "A vision forms in your mind. A place, perfectly clear, as though you've stood there countless times before. A shiver runs through your body."
        scene 96_s31 with Dissolve(1.0)
        mc "(Huh!? Ahnng! My head... what was that? Was that where Ava lives?)"
        mc "(Who's telling me this? Amelia? I guess I have no choice but to trust it.)"
        scene 96_s32 with Fade(1.0,1.0,1.0)
        mc "(Hm? It's her!)"
        mc "Ava!"
        scene 96_s33 with vpunch
        ava "Ahh!"
        ava "[mc]?!"
        scene 96_s35 with Dissolve(1.0)
        mc "Yes, it's me! Please, I need your help. It's urgent."
        scene 96_s34 with dissolve
        ava "What are you doing here? No, scratch that, why should I not scream for the guards this very second?"
        scene 96_s35 with dissolve
        mc "Please, I'll explain everything. Can we go somewhere private? Your house is right here, isn't it?"
        scene 96_s34 with dissolve
        ava "You are {i}not{/i} getting inside my home! Are you insane?"
        scene 96_s35 with dissolve
        mc "I saved Kat, remember? I swear on whatever you hold dear, I mean no harm. I just need to talk."
        ava "..."
        mc "Please! This concerns Kat too. She might be in danger."
        scene 96_s34 with dissolve
        ava "...Dammit! Fine. Follow me, quickly. And I swear to every god, I will regret this."
        scene 96_s35 with dissolve
        scene 96_s36 with Fade(1.0,1.0,1.0)
        ""
        stop music fadeout 1.0 
        scene 96_s37 with Fade(1.0,1.0,1.0)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        ava "There. We're inside. Now talk."
        scene 96_s39 with Dissolve(1.0)
        kat "*yawn* Ava? I heard a man's voice. Don't tell me you actually hired a male whore."
        scene 96_s42 with Dissolve(1.0)
        ava "Don't be ridiculous! This is [mc]. The man who... helped you."
        scene 96_s41 with dissolve
        kat "No fucking way! [mc]?!"
        scene 96_s40 with dissolve
        mc "Hey, Kat. It's... a long story. I was just about to explain why the whole city wants my head."
        scene 96_s37 with Dissolve(1.0)
        ava "And I'm waiting. This had better be the best story I've ever heard."
        scene 96_s38 with dissolve
        mc "First, I came here because I need you to enchant my prosthetic. The smith who forged it said I needed a powerful sorcerer. That's you."
        if mc_agree_help_amelia_milking:
            mc "I tried another... source. A witch. But she couldn't complete the ritual."
        elif mc_disagree_help_amelia_milking:
            mc "I tried another... source. A witch. But I couldn't go through with her terms."
        kat "*chuckles* A witch? Where did you even find one? I'd kill to meet a real—"
        scene 96_s42 with dissolve
        ava "Shut up, Kat."
        scene 96_s37 with dissolve
        ava "You show up at my door, a wanted man, with a tale of witches and enchanted arms, and expect me to just... comply?"
        scene 96_s38 with dissolve
        kat "I'm sure he has his reasons for what happened with Able."
        scene 96_s44 with Dissolve(1.0)
        mc "Able's death wasn't even a fraction of the reason I ran. I ran from the people who {i}used{/i} his death."
        if mc_save_queen:
            mc "Avery and Reiner of Eurina are to blame. They lied to everyone. They intended to assassinate the Queen. Fortunately, it failed. The Queen is in hiding, and Avery has taken power... for now."
        else:
            mc "Avery and Reiner of Eurina are to blame. They lied to everyone. The Queen didn't die at sea. They assassinated her."
        scene 96_s45 with dissolve
        kat "Fucking hell..."
        ava "And you just believe him?"
        kat "I've got no reason not to. Think about it, Ava. It all happened too perfectly, too fast."
        ava "..."
        ava "Do you have proof of this?"
        scene 96_s44 with dissolve
        mc "Not physical proof you can hold. But I know the person chosen to carry out the assassination. She's Reiner's unknown daughter. We intend to expose the truth together."
        mc "Avery is hunting me as we speak. She's targeting innocent people just to bury this. In three weeks, she plans to execute the Princess."
        mc "If anything, she's definitely hunting for Kat too. If you don't trust me now then you will surely do once she goes outside and never comes back. But it will be too late at that point."
        scene 96_s45 with dissolve
        ava "Ugh... This is giving me a headache."
        scene 96_s38 with dissolve
        mc "Will you help me?"
        scene 96_s37 with dissolve
        ava "Just... give me a moment. I need to sit with all of this, turn it over in my head, and decide whether I'm about to make the worst mistake of my life."
        scene 96_s38 with dissolve
        mc "Alright. I can wait. Just don't take too long, I'm on a clock, and it's ticking louder by the minute."
    else:
        stop music fadeout 1.0 
        scene 96_s1 with Fade(1.3,1.0,1.3)
        play music "wind.mp3" fadein 1.0 volume 0.7 loop
        ""
        scene 96_s2 with Dissolve(1.0)
        mc "Excuse me, miss."
        scene 96_s3 with vpunch
        old_woman2 "AHH!"
        scene 96_s4 with Dissolve(1.0)
        old_woman2 "*laughs* Oh, goodness gracious... don't do that to an old woman."
        old_woman2 "Nearly made me empty out my bowels right here on the cobbles."
        scene 96_s5 with dissolve
        mc "..."
        scene 96_s4 with dissolve
        old_woman2 "Something you need, son?"
        scene 96_s5 with dissolve
        mc "I'm looking for a woman—"
        scene 96_s4 with dissolve
        old_woman2 "Who isn't these days?"
        old_woman2 "Hopefully Her new Majesty starts importing ladies from overseas instead of just soldiers."
        old_woman2 "Keep looking, honey. I'm sure you'll find one."
        scene 96_s5 with dissolve
        mc "That's not what I mean... I'm looking for a specific woman. An elvish girl named Ava. Short, blonde hair."
        scene 96_s4 with dissolve
        old_woman2 "Oh! Ava."
        old_woman2 "I know her. Sharp as a tack, that one. Used to be my neighbor before we moved out of the blast zone. Terrible things happening recently. Just terrible."
        old_woman2 "One day you're hanging laundry, the next day half the street is missing and everyone's pretending it's normal."
        scene 96_s5 with dissolve
        mc "...Right. Do you know where she is now?"
        scene 96_s4 with dissolve
        old_woman2 "You can still find her in the same district. Never moved out, brave soul... or stubborn. Hard to tell with elves."
        old_woman2 "Just follow this road to the end, turn left at the broken fountain—bless it, it's been broken since I was a wee girl, and keep going until you find The Thirsty Dinky Inn."
        old_woman2 "Her house is right next to it. Big blue door, looks truly awful. But don't tell her I said that."
        scene 96_s5 with dissolve
        mc "I see. Thank you."
        scene 96_s4 with dissolve
        old_woman2 "Of course, dear. Perhaps next time, you could remove your mask before you talk to folks. People are very skittish these days."
        scene 96_s5 with dissolve
        scene 96_s6 with Fade(1.5,1.0,1.2)
        mc "(Blue door. The old woman's right, it does look out of place.)"
        scene 96_s7 with Dissolve(1.0)
        "*knock* *knock* *knock*"

        if mc_execute_kat or mc_life_kat:
            jump scene100

        kat "Coming!"
        play sound "sound_effects/door.mp3"
        scene 96_s8 with Dissolve(1.3)
        kat "Yes—whoa! Who're you?"
        kat "*laughs* Gods above... You look like you jumped straight outta one of those lurid novels my friend reads."
        scene 96_s9 with dissolve
        ava "Who is it?"
        scene 96_s10 with dissolve
        kat "Dunno! Some guy wearing a full mask. Looks absolutely terrifying."
        scene 96_s9 with dissolve
        ava "A mask?"
        mc "It's me, Kat."
        scene 96_s11 with dissolve
        kat "Hold on... I recognize this voice."
        kat "[mc]?"
        scene 96_s9 with dissolve
        mc "Yes. Can you let me in?"
        scene 96_s11 with dissolve
        kat "Damn right you son of a bitch! Get in here, quick!"
        stop music fadeout 1.0 
        scene 96_s12 with Fade(1.0,0.5,0.5)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        mc "Brrr... finally some warmth."
        scene 96_s13 with Dissolve(1.0)
        ava "You invited a man inside?! I'm practically naked, Kat!"
        scene 96_s14 with dissolve
        kat "This ain't a regular guy, Avy. It's [mc]. {i}The{/i} [mc]."
        scene 96_s15 with dissolve
        ava "By the Gods..."
        ava "W-What are you doing here!?"
        scene 96_s16 with Dissolve(1.0)
        kat "Calm down. He's a good man, and he's definitely here for a good reason."
        kat "Unless he's here to see me~... which is also a perfectly good reason."
        scene 96_s15 with dissolve
        ava "Explain yourself, [mc]. Now. Before I throw you out and call the guards."
        scene 96_s17 with dissolve
        mc "I'm here for help. Your help, Ava."
        scene 96_s46 with dissolve
        ava "What would I possibly give to a fugitive?"
        scene 96_s18 with Dissolve(1.0)
        mc "I need you to enchant my prosthetic. The smith who forged it said I needed a powerful sorcerer. That's you."
        scene 96_s19 with dissolve
        ava "I... I don't understand you. Why would I help you!?"
        scene 96_s20 with Dissolve(1.0)
        kat "For fuck's sake, Ava, listen. He saved me, remember? I'd still be in that cell, or worse, if we hadn't found that loophole."
        kat "I'm sure he has his reasons for what happened with Able."
        scene 96_s21 with Dissolve(1.0)
        mc "Able's death wasn't even a fraction of the reason I ran. I ran from the people who {i}used{/i} his death."
        if mc_save_queen:
            mc "Avery and Reiner of Eurina are to blame. They lied to everyone. They intended to assassinate the Queen. Fortunately, it failed. The Queen is in hiding, and Avery has taken power... for now."
        else:
            mc "Avery and Reiner of Eurina are to blame. They lied to everyone. The Queen didn't die at sea. They assassinated her."
        scene 96_s22 with dissolve
        kat "Fucking hell..."
        ava "And you just believe him?"
        kat "I've got no reason not to. Think about it, Ava. It all happened too perfectly, too fast."
        ava "Do you have proof of this?"
        scene 96_s23 with dissolve
        mc "Not physical proof you can hold. But I know the person chosen to carry out the assassination. She's Reiner's unknown daughter. We intend to expose the truth together."
        mc "Avery is hunting me as we speak. She's targeting innocent people just to bury this. In three weeks, she plans to execute the Princess."
        mc "If anything, she's definitely hunting for Kat too. If you don't trust me now then you will surely do once she goes outside and never comes back. But it will be too late at that point."
        scene 96_s24 with Dissolve(1.0)
        ava "Ugh... This is giving me a headache."
        scene 96_s25 with dissolve
        mc "Will you help me?"
        scene 96_s24 with dissolve
        ava "Just... give me a moment. I need to sit with all of this, turn it over in my head, and decide whether I'm about to make the worst mistake of my life."
        scene 96_s25 with dissolve
        mc "Alright. I can wait. Just don't take too long—I'm on a clock, and it's ticking louder by the minute."
    jump scene96_2


label scene96_2:
    scene 96_s26 with Dissolve(1.2)
    kat "Take a seat or are you one of those types with a worm up their ass? Can't relax unless you're pacing? Because that's basically me."
    scene 96_s27 with dissolve
    mc "(Her breasts are pressing against me...)"
    call screen scene95_choice02 with dissolve

label scene95_choice02_op1:
    $ mc_angry_kat1 = True
    mc "You're too close. Back off."
    scene 96_s28 with dissolve
    kat "Oh, sorry! Haha... didn't notice."
    scene 96_s29 with dissolve
    mc "I'd like to look around if you don't mind. I hate sitting around, like you said."
    scene 96_s28 with dissolve
    kat "Sure, go ahead."
    scene 96_s29 with dissolve
    $ in_free_roam = True
    scene 97_s1 with Fade(1.3,1.0,1.2)
    if mc_choose_ava_after_amelia:
        if mc_agree_help_amelia_milking:
            $ current_objective =  "I went through with what Amelia wanted. I won't \ndeny that I enjoyed it, but... I was hoping to leave \nwith a working arm. Still, I made my way to Ava's \nhouse, guided by a mysterious voice in my head. \n\nThe vision was crystal clear and it shook me to my \ncore. I don't understand it. I'm not sure I want to."
        else:
            $ current_objective = "Amelia was a dead end. Her demands were simply \ntoo much. I suppose I should've seen that coming. \nStill, I made my way to Ava's house, guided by a \nmysterious voice in my head. \n\nThe vision was crystal clear and it shook me to my \ncore. I don't understand it. I'm not sure I want to."
    else:
        $ current_objective = "I don't even know what day it is. Things have been \nso hectic lately that I've barely had time to gather \nmy thoughts. The important thing is that I managed\nto convince Dean, the blacksmith, to forge a new\nhand for me. \n\nNow all it needs is an enchantment to make it real. \nI barely understand how that would even work, but \nI sought out Ava to see to it. \n\nI trust she's competent enough to do it."
    if not mc_agree_help_amelia_milking:
        $ mc_overview_open = True
        $ in_scene93 = True
        show screen mc_stats with dissolve
        mc "(Hm, it's been a while since I checked my Irda ID card... It's pretty much useless and outdated now.)"
        hide screen mc_stats with dissolve
        $ mc_overview_open = False
        $ in_scene93 = False
    
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene97_free_roam with dissolve

label scene95_choice02_op2:
    scene 96_s26 with dissolve
    kat "Like how my tits feel?"
    scene 96_s27 with dissolve
    mc "You're doing it on purpose, aren't you?"
    scene 96_s26 with dissolve
    kat "Maybe~"
    kat "You still have your cock, don't you?"
    scene 96_s27 with dissolve
    mc "I do. Why are you asking about that? Are you not mad about what happened to the Queen, or at least... sad?"
    scene 96_s26 with dissolve
    kat "Eh, shit like that happens all the time in politics. Right, Ava?"
    scene 96_s27 with dissolve
    ava "Not really. Well... kind of."
    scene 96_s26 with dissolve

    if mc_harem_kat:
        kat "I haven't had any action since you freed me, so I'm partilcu... partircul—"
    else:
        kat "And aside from her, I haven't had any action since you freed me, so I'm partilcu... partircul—"
    scene 96_s27 with dissolve
    ava "Particularly."
    scene 96_s26 with dissolve
    kat "—particularly horny."
    scene 96_s27 with dissolve
    mc "I see..."
    scene 96_s26 with dissolve
    kat "Once Ava's finished maybe you and I can have a little fun. It's seriously been too long being cooped up with this girl."
    scene 96_s27 with dissolve
    mc "*chuckles* I'd like to look around if you don't mind. I hate sitting around, like you said."
    scene 96_s26 with dissolve
    kat "Sure, go ahead. You can find my panties in the drawer over there—Ava's are in the one below it."
    scene 96_s27 with dissolve
    ava "No! Don't you dare!"
    scene 96_s26 with dissolve
    kat "He's just looking. Not like he's gonna steal them. Right?"
    scene 96_s27 with dissolve
    mc "..."
    $ in_free_roam = True
    scene 97_s1 with Fade(1.3,1.0,1.2)
    if mc_choose_ava_after_amelia:
        if mc_agree_help_amelia_milking:
            $ current_objective =  "I went through with what Amelia wanted. I won't \ndeny that I enjoyed it, but... I was hoping to leave \nwith a working arm. Still, I made my way to Ava's \nhouse, guided by a mysterious voice in my head. \n\nThe vision was crystal clear and it shook me to my \ncore. I don't understand it. I'm not sure I want to."
        else:
            $ current_objective = "Amelia was a dead end. Her demands were simply \ntoo much. I suppose I should've seen that coming. \nStill, I made my way to Ava's house, guided by a \nmysterious voice in my head. \n\nThe vision was crystal clear and it shook me to my \ncore. I don't understand it. I'm not sure I want to."
    else:
        $ current_objective = "I don't even know what day it is. Things have been \nso hectic lately that I've barely had time to gather \nmy thoughts. The important thing is that I managed\nto convince Dean, the blacksmith, to forge a new\nhand for me. \n\nNow all it needs is an enchantment to make it real. \nI barely understand how that would even work, but \nI sought out Ava to see to it. \n\nI trust she's competent enough to do it."
    if not mc_agree_help_amelia_milking:
        $ mc_overview_open = True
        $ in_scene93 = True
        show screen mc_stats with dissolve
        mc "(Hm, it's been a while since I checked my Irda ID card... It's pretty much useless and outdated now.)"
        hide screen mc_stats with dissolve
        $ mc_overview_open = False
        $ in_scene93 = False
    
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    if mc_karma < 1:
        $ mc_karma = 1
    call screen scene97_free_roam with dissolve

label scene97:
    scene 97_s1 with dissolve
    call screen scene97_free_roam with dissolve

label scene97_free_roam_left:
    scene 97_s2 with dissolve
    call screen scene97_free_roam_left with dissolve

default scene97_free_roam_right_poster = True
label scene97_free_roam_right:
    if scene97_free_roam_right_poster:
        scene 97_s3_2 with dissolve
    else:
        scene 97_s3 with dissolve
    call screen scene97_free_roam_right with dissolve

label scene97_free_roam_right_poster:
    $ persistent.kat_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene97_free_roam_right_poster = False
    jump scene97_free_roam_right

default scene97_drawer_first = False
label scene97_drawer:
    play sound "sound_effects/doors/drawer.mp3"
    scene 97_s5 with dissolve
    $ scene97_drawer_first = True
    perception "You slide open the drawer. Inside, a neat stack of folded undergarments, mostly practical but with a few lacy pieces that look well-worn. A faint scent of clean laundry rises."
    kat "Those are mine. What do you think? Cute, huh?"
    kat "Who'd think such a hardened adventurer like myself would have a soft side?"
    ava "*scoff*"
    kat "What are you scoffing for?!"
    call screen scene97_drawer with dissolve

label scene97_drawer_pantie2:
    call screen scene97_pantie with dissolve
    call screen scene97_drawer with dissolve

default scene97_drawer_pantie2_2_first = False
label scene97_drawer_pantie2_2:
    if not scene97_drawer_pantie2_2_first:
        $ mc_sniff_kat_pantie = True
        $ scene97_drawer_pantie2_2_first = True
        sensation "You inhale deeply, the smell is clean, crisp soap with just a hint of her natural musk underneath. Freshly washed. Disappointing."
        kat "*giggles* Aww, sorry to disappoint. But these are post-wash. You wouldn't have dirty laundry lying around in your drawers, right?"
        ava "Why would he even sniff them in the first place? {i}Disgusting...{/i}"
        kat "*tch* *tch* *tch* You don't understand men, Ava. This is normal for them."
    else:
        mc "(They smell the exact same as before. It's like smelling any laundry... boring.)"
    call screen scene97_drawer with dissolve

default scene97_drawer_pantie1_first = False
label scene97_drawer_pantie1:
    if not scene97_drawer_pantie1_first:
        $ scene97_drawer_pantie1_first = True
        ava "Stop! Those are private!"
        kat "Eh, it's just a bra. *giggles* I wouldn't get too excited, she wears grandma bras afterall."
        kat "And why is that in my drawer anyway?"
        ava "{i}You{/i} took them!"
        kat "Ah... right."
    else:
        ava "Hands off!"
    call screen scene97_drawer with dissolve

label scene97_free_roam_up:
    scene 97_s8 with dissolve
    call screen scene97_free_roam_up with dissolve

label scene97_free_roam_up_left:
    scene 97_s7 with dissolve
    call screen scene97_free_roam_up_left with dissolve

default scene97_free_roam_up_right_poster = True
label scene97_free_roam_up_right:
    if scene97_free_roam_up_right_poster:
        scene 97_s6_2 with dissolve
    else:
        scene 97_s6 with dissolve
    call screen scene97_free_roam_up_right with dissolve

label scene97_free_roam_up_right_poster:
    $ persistent.yuuhi_render2 = True
    play sound "sound_effects/render_unlock.mp3"
    $ renpy.notify("You unlocked a special render!")
    $ scene97_free_roam_up_right_poster = False
    jump scene97_free_roam_up_right

label scene97_feet:
    scene 97_s9 with dissolve
    mc "..."
    jump scene97_free_roam_up

label scene97_kat:
    kat "Will you sit down, please? You're making me anxious with your pitter-pattering."
    call screen scene97_free_roam_up_left with dissolve

label scene97_free_roam_end:
    call screen scene97_free_roam_end with dissolve
    call screen scene97_free_roam_up with dissolve

label scene97_2:
    $ in_free_roam = False
    scene 97_s10 with Fade(1.2,1.0,1.0)
    mc "(I need to make a list of what I should do nex—)"
    play sound "sound_effects/woosh3.mp3"
    pause 0.3
    scene 97_s11 with vpunch
    mc "Ahh!"
    play sound "sound_effects/wood_hit.mp3"
    scene 97_s12 with dissolve
    mc "What the fuck was that for?!"
    scene 97_s15 with Dissolve(1.0)
    kat "*laughs* Just testing your reflexes. Don't worry, I wasn't actually aiming at you."
    scene 97_s16 with dissolve
    mc "It sure as hell looked like it!"
    scene 97_s15 with dissolve
    kat "*giggles* I like that new hand. Fancy. Reinforced steel?"
    scene 97_s16 with dissolve
    mc "Adamntite."
    scene 97_s15 with vpunch
    kat "Get out of here! Adamantite? That shit's rarer than an honest noble."
    kat "Where did you get the coin to pay for something like that?"
    scene 97_s13 with Dissolve(1.0)
    if mc_debt:
        mc "I didn't pay for it yet. It was a debt. Fifty gold coins."
        scene 97_s14 with dissolve
        kat "*laughs* Fifty? Gods... you'll be walking with a cane before you finish paying that off."
        kat "But worth it, right? Look at this thing."
        kat "If I had an adamantite blade, I'd be living in a mansion right now. Forget how efficient it would be, just walking around with metal like that? People would finally take me seriously."
    else:
        mc "The price was saving this city."
        scene 97_s14 with dissolve
        kat "*chuckles* Aren't you the hero."
        kat "Still... damn. If I had an adamantite blade, I'd be living in a mansion right now."
        kat "Forget how efficient it would be—just walking around with metal like that on my hip? People would finally take me seriously."

    scene 97_s16 with Dissolve(1.0)
    mc "Do you want to know how it happened?"
    scene 97_s15 with dissolve
    kat "Let me guess... Gaius, right? Not many can cut cleanly like that. Honestly, it's remarkable you only lost the hand and not your entire arm."
    kat "But don't worry. I've seen more missing limbs than intact ones during my many years of adventuring. You'll blend right in with the city's finest tragedies."
    scene 97_s16 with dissolve
    mc "*chuckles* That's reassuring."
    mc "What about you? Still keeping your head down, avoiding trouble?"
    scene 97_s17 with Dissolve(1.0)
    kat "I've been testing the waters. Going out a bit more."
    kat "Of course, the first time I do, half the market goes up in flames. Right outside Able's tavern, no less."
    kat "Tell me honestly, you had something to do with that, didn't ya?"
    scene 97_s18 with dissolve
    mc "There was a mage. Things got... explosive. She helped me when we were surrounded by guards."
    scene 97_s17 with dissolve
    kat "Fantastic. If you see her again, tell her I've got some very pointed words about burning down my favorite smoked ribs stall."
    scene 97_s18 with dissolve
    mc "Trust me, I'd like to find her too. Wherever she is, she's probably as far from this city as possible."
    scene 97_s17 with dissolve
    kat "So. Fancy new arm, a kingdom that wants you dead, and you're sitting in my house."
    scene 97_s18 with dissolve
    ava "*ahem* {i}My{/i} house."
    scene 97_s17 with dissolve
    stop music fadeout 1.0 
    kat "What's the plan now, wanderer?"
    play music "side_event5.mp3" fadein 2.0 loop
    scene 97_s19 with Dissolve(1.0)
    if mc_princess_alex:
        mc "I'm getting the princess out of the castle."
        scene 97_s20 with dissolve
        kat "*laughs* You're joking."
        mc "..."
        kat "You have to be joking."
        kat "Tell me you're joking..."
        scene 97_s19 with dissolve
        mc "I'm not. Avery's planning to execute her. I won't let that happen."
        scene 97_s20 with dissolve
        kat "Oh man..."
        kat "You know, I keep waiting for the part where you say something sensible for once."
        scene 97_s19 with dissolve
        mc "It won't be a siege. No bloodbath. We'll get in, get her out, and leave before anyone knows she was gone."
        scene 97_s20 with dissolve
        kat "That sounds better. but stil, in practice, you're talking about a fortress crawling with guards, inside and out, trained to kill anything that breathes wrong."
        scene 97_s19 with dissolve
        mc "We'll think something up, I can't let her suffer for longer."
        scene 97_s18 with dissolve
        empathy "She looks at you with endearing eyes, completely captivated by your insane yet beautiful task. It isn't subtle."
        scene 97_s17 with dissolve
        kat "I see. Then count me in."
        scene 97_s18 with dissolve
        mc "R-Really?"
        scene 97_s17 with dissolve
        kat "Really."
        kat "I think I've found the kind of man worth following, even if it gets me killed."
        kat "From now on, I'm your blade! Wherever you step, I'll be there."
        scene 97_s18 with dissolve
        mc "Thank you, Kat. I don't take that lightly."

    else:
        mc "I'll be marching to Nahraya, If we can convince their king to summon Nueleth and tell her the truth, the lie collapses on itself."
        scene 97_s22 with dissolve
        ava "Nueleth? If anyone else heard you say that aloud, they'd call you insane on the spot."
        scene 97_s21 with dissolve
        mc "Maybe. But I don't see another way to force the truth into the light."
        scene 97_s22 with dissolve
        ava "I'm not telling you to stop. In fact, I'd very much like to see someone succeed where everyone else was too afraid to try."
        scene 97_s20 with dissolve
        kat "Insane? Absolutely. But incredible? Even more so."
        kat "Go on, [mc]. When you come back victorious, just remember—I've got a pair of very comfortable thighs waiting for you."
        scene 97_s19 with dissolve
        mc "...I'll keep that in mind."
        scene 97_s20 with dissolve

    scene 97_s22 with Dissolve(1.0)
    ava "*sigh* listen, [mc]. I don't trust you... yet. But I do owe you for helping this stupid girl, and I won't pretend otherwise."
    scene 97_s21 with dissolve
    kat "Hey!"
    mc "You're very understanding. Thank you."
    scene 97_s22 with dissolve
    ava "Once I do this, we're even."
    scene 97_s21 with dissolve
    mc "Of course."
    scene 97_s22 with dissolve
    ava "I'll need time to prepare. This enchantment... it is not like putting a sharp edge on a sword. It is asking metal to become flesh, to converse with a soul it was not born with."
    ava "I tried it once. The subject... did not survive."
    scene 97_s21 with dissolve
    mc "What happened? I've been told that there would be side effects."
    scene 97_s23 with dissolve
    ava "His body fought the new prosthetic like a poison. It was a civil war under his own skin. He lasted three days. I will not be responsible for that again."
    ava "If something goes wrong, your body may accept it partially, just enough for your defenses to recognize it as an intruder."
    ava "At that point, your own system will try to destroy it. Destroying you in the process."
    scene 97_s24 with dissolve
    mc "*sigh* Good to know. I still want to go through with it. I know you can do it."
    scene 97_s22 with dissolve
    ava "You put too much faith on me... I-I need to study the spell more. Could you give me another few minutes? Perhaps an hour?"
    scene 97_s21 with dissolve
    mc "*chuckles* If it's going to help you avoid making a mistake, sure."
    stop music fadeout 1.0 
    kat "Take your sweet time, Ava. As for me..."
    play music "fire.mp3" fadein 1.0 volume 0.5 loop
    scene 97_s25 with Dissolve(1.0)
    perception "She crawls on her hands and knees, closing the distance confidently. Her eyes lock on yours, dark with raw admiration and unmistakable heat."
    mc "(What in the world?)"
    scene 97_s26 with dissolve
    if mc_princess_alex:
        kat "You're a tough one, eh? Sneaking in into a castle and rescuing a princess. Not to mention Gaius."
    else:
        kat "You're a tough one, eh? Going after the Queen and potentially an entire army. Not to mention Gaius."
    scene 97_s27 with dissolve
    mc "*chuckles* Lost my hand becasue of it. But... I'll take the compliment."
    scene 97_s26 with dissolve
    kat "You're insane. Like... impressively insane."
    kat "You wanna know how you look right now?"
    scene 97_s27 with dissolve
    call screen scene97_choice01 with dissolve

label scene97_choice01_op1:
    $ kat_love += 20
    mc "Hot."
    scene 97_s26 with dissolve
    kat "Exactly. Hot as fuck."
    jump scene97_3

label scene97_choice01_op2:
    $ kat_love += 10
    mc "Like an idiot?"
    scene 97_s26 with dissolve
    kat "Not exactly...  Well maybe a sexy, dangerous, beautifully broken hot idiot."
    scene 97_s27 with dissolve
    mc "That's a lot of adjectives."
    scene 97_s26 with dissolve
    kat "You inspire them."
    jump scene97_3

label scene97_choice01_op3:
    mc "Like a freak who did terrible things?"
    scene 97_s28 with dissolve
    kat "What? No! None of that."
    kat "Gods, don't do that. Don't turn yourself into some tragic horror story."
    kat "You look like... Ah shit! I forgot what I was going to say."
    scene 97_s29 with dissolve
    mc "*chuckles* I'm waiting..."
    scene 97_s28 with dissolve
    kat "Shut up, I had something really good."
    scene 97_s29 with dissolve
    mc "Sure you did."
    scene 97_s26 with dissolve
    kat "It was gonna be devastating. Romantic. Probably life-changing!"
    scene 97_s27 with dissolve
    mc "Now we'll never know."
    scene 97_s26 with dissolve
    jump scene97_3

label scene97_3:
    kat "The man who saved my life... is also the strongest I've ever known. It makes me... mad."
    kat "I never got to truly thank you. I owe you everything, you know. My life. My freedom."
    scene 97_s31 with Dissolve(1.0)
    kat "And debts like that... deserve proper repayment."
    scene 97_s30 with dissolve
    ava "Will you two take it elsewhere!? I'm trying to focus here!"
    scene 97_s31 with dissolve
    kat "You heard her. Shall we take our... business to the bedroom? I can't wait any longer."
    scene 97_s30 with dissolve
    ava "Just not on my bed! I swear—"
    scene 97_s21 with dissolve
    kat "You could focus better if you stopped yapping that mouth of yours."
    scene 97_s23 with dissolve
    ava "*sigh* Gods give me strength. Sleeping with a fugitive first thing..."
    scene 97_s26 with dissolve
    kat "Ignore her. She doesn't know what she's missing."
    kat "Let me show you exactly how grateful I am. Show you how good I can worship you. Your call."
    scene 97_s27 with dissolve
    mc "What are you... suggesting?"
    scene 97_s26 with dissolve
    kat "Look~ I'm sure you're busy so how about I suck your cock for now? I want you to fill my mouth with your seed, make me choke on it as I gulp it down."
    if mc_harem_kat:
        kat "Say the word, husband. I'll drop to my knees faster than you can blink."
    kat "Or... would you like to test my loyalty first?"
    scene 97_s27 with dissolve
    call screen scene97_choice02 with dissolve

label scene97_choice02_op1:
    $ mc_refuse_bj_kat = True
    mc "No, Kat. There's a lot on my mind."
    scene 97_s26 with dissolve
    kat "I get it. No pressure."
    kat "Whenever you're ready... whenever you're in need for your cock cleaned. I'm here."
    scene 97_s27 with dissolve
    jump scene99

label scene97_choice02_op2:
    $ mc_told_kat_polygamy = True
    mc "I already have someone, Kat. Do you mind sha-"
    scene 97_s26 with dissolve
    kat "*chuckles* ...Right. Of course you do."
    if mc_harem_kat:
        kat "We're married, legally too. Don't you remember?"
        scene 97_s27 with dissolve
        mc "You can break that contract whenever you want. It was to save you."
        scene 97_s26 with dissolve
        kat "Aww man... I thought we... never mind."
        kat "I get it. You did it to keep me breathing. I'll always be grateful for that. Truly."
        kat "Just so you know... I don't mind being the side girl."
        kat "Whenever your main girl's pussy gets too loose, or she's too tired, or she's just not in the mood... I've got a tight, eager one waiting for you. Always ready. No questions asked."
        scene 97_s27 with dissolve
        mc "...I'll keep that in mind."
        scene 97_s26 with dissolve
        kat "Good. Because I'm not going anywhere. Wife, side piece, whatever you need me to be."
        kat "So, what do you say?"
    else:
        kat "Fair enough. One girl's enough for most men."
        kat "But you should know... gratitude like mine doesn't come with an expiration date."
        kat "Whenever you're feeling generous, or bored, or just need to blow off steam... I'm here. No strings. No drama."
        kat "And I promise you, I'm tighter, wetter, and a hell of a lot more enthusiastic than whatever prim little thing you've got waiting out there."
        scene 97_s27 with dissolve
        mc "...I'll keep that in mind."
        scene 97_s26 with dissolve
        kat "So, what do you say?"
    scene 97_s27 with dissolve
    call screen scene97_choice03 with dissolve

label scene97_choice02_op3:
    mc "I wanna test your loyalty first."
    scene 97_s26 with dissolve
    kat "I'll do whatever you ask of me. Anything."
    scene 97_s27 with dissolve
    call screen scene97_choice04 with dissolve

label scene97_choice03_op1:
    $ mc_breakup_kat = True
    mc "Break that contract. I don't like cheating."
    scene 97_s28 with dissolve
    kat "*sigh* Fine, fine. I won't push you anymore, you clearly love that girl. Whoever she is."
    scene 97_s29 with dissolve
    mc "I'll wait for Ava to finish her studying."
    scene 97_s28 with dissolve
    kat "Of course. I'll stand up, my knees are starting to hurt."
    scene 97_s29 with dissolve
    jump scene99

label scene97_choice03_op2:
    $ mc_breakup_kat = True
    mc "I don't want to cheat, Kat."
    scene 97_s28 with dissolve
    kat "*sigh* Fine, fine. I won't push you anymore, you clearly love that girl."
    scene 97_s29 with dissolve
    mc "I'll wait for Ava to finish her studying."
    scene 97_s28 with dissolve
    kat "Of course. I'll stand up, my knees are starting to hurt."
    scene 97_s29 with dissolve
    jump scene99

label scene97_choice04_op1:
    mc "I want you start barking."
    scene 97_s26 with dissolve
    kat "Ohhh, you're going there~"
    scene 97_s32 with Dissolve(1.0)
    kat "Woof!"
    kat "Woof! Woof!"
    scene 97_s33 with dissolve
    ava "Gods... I never knew you could stoop so low."
    scene 97_s32 with dissolve
    kat "Like this, Master? Or should your bitch bark louder?"
    scene 97_s33 with dissolve
    mc "Louder."
    scene 97_s32 with dissolve
    kat "WOOF! WOOF!"
    kat "Woof... please... use your bitch..."
    scene 97_s33 with dissolve
    mc "That's good. I want you now."
    scene 97_s32 with dissolve
    kat "Hold on, not here. Follow me~"
    scene 97_s33 with dissolve
    scene 97_s36 with Fade(0.5,0.5,0.5)
    ""
    jump scene97_4

label scene97_choice04_op2:
    mc "Kiss my boot."
    scene 97_s26 with dissolve
    kat "Yes, sir."
    scene 97_s34 with Dissolve(1.5)
    play sound "se_sfx/blowjob/kiss4.mp3" 
    kat "*mwah*"
    ava "Kat!? What are you doing!"
    scene 97_s35 with dissolve
    if mc_harem_kat:
        kat "Good enough, Master? Or should your bitch wife polish them until they shine with her spit?"
    else:
        kat "Good enough, Master? Or should your bitch polish them until they shine with her spit?"
    mc "That's good. I want you now."
    kat "Hold on, not here. Follow me~"
    scene 97_s36 with Fade(0.5,0.5,0.5)
    ""
    jump scene97_4

label scene97_choice04_op3:
    mc "Tell me you're nothing without my cock."
    kat "..."
    scene 97_s31 with Dissolve(1.0)
    kat "I'm nothing without your cock."
    kat "I'm just a wet, needy hole waiting to be filled."
    kat "Without it inside me, stretching me, owning me, I'm empty. Worthless."
    kat "Please... remind me what I'm for. Use my mouth. My throat. Anything."
    kat "I live for your seed... for being your obedient little semen-dump."
    scene 97_s30 with dissolve
    mc "That's good. I want you now."
    scene 97_s31 with dissolve
    kat "Hold on, not here. Follow me~"
    scene 97_s30 with dissolve
    scene 97_s36 with Fade(0.5,0.5,0.5)
    ""
    jump scene97_4

label scene97_choice02_op4:
    mc "There's no need. I want your mouth now."
    scene 97_s26 with dissolve
    kat "Hold on, not here. Follow me~"
    scene 97_s36 with Fade(0.5,0.5,0.5)
    ""
    jump scene97_4

label scene97_4:
    scene 97_s37 with Dissolve(2.0)
    if mc_harem_kat:
        kat "Alright, Ava! I'll be in the bedroom sucking off my husband. Keep on studying, babe."
    else:
        kat "Alright, Ava! I'll be in the bedroom sucking off [mc]. Keep on studying, babe."
    scene 97_s38 with dissolve
    ava "You don't need to announce it to the whole house! {size=30}...Slut.{/size}"
    jump scene98

label scene98:
    stop music fadeout 1.1
    scene 98_s1 with Fade(1.3,1.0,1.2)
    mc "Thought you two were together."
    scene 98_s2 with Dissolve(1.3)
    if mc_harem_kat:
        kat "Hmm? Oh, no. We're just close friends."
        kat "She's allowed me to stay with her. *snickers* {i}Rent free{/i} might I add."
        scene 98_s3 with dissolve
        mc "I see. You're never apart, so I just assumed."
        scene 98_s2 with dissolve
        kat "Well... We {i}were{/i} involved in some ways, but I abstained since I thought you wouldn't like it."
    else:
        kat "Hmm? Oh, no. We're friends. Very... close friends."
        kat "Friends who sometimes like to relieve each other. She's good with her tongue—great stress relief."
        scene 98_s3 with dissolve
        mc "I see. You're never apart, so I just assumed."
        scene 98_s2 with dissolve
        kat "Aside from guild tasks, sure. But sucking the juices out of her pussy regularly doesn't make us lovers."
    kat "Honestly? She's been getting on my nerves lately. Subtly hinting I should move out, little comments about 'needing space.'"
    scene 98_s3 with dissolve
    mc "Can you blame her? You're not exactly subtle."
    scene 98_s5 with dissolve
    kat "Hey! You're supposed to be on my side."
    scene 98_s3 with dissolve
    mc "*chuckles* How do you plan on getting back at her? Let's hear this revenge scheme."
    scene 98_s2 with dissolve
    kat "I'm gonna suck you off until you explode... then walk out there with my mouth full of your cum and show her."
    scene 98_s3 with dissolve
    mc "Whoa... that's bold. How's that supposed to get back at her?"
    scene 98_s2 with dissolve
    if mc_harem_kat:
        kat "I dunno... probably piss her off knowing I've got you to play with. A cock that actually fills me up."
    else:
        kat "I dunno... probably piss her off knowing I've got someone else to play with. Someone with a cock that actually fills me up."
    kat "What do you say? Or have something even better in mind?"
    scene 98_s3 with dissolve
    call screen scene98_choice01 with dissolve

label scene98_choice01_op1:
    $ kat_love += 10
    $ mc_kat_show_cum_ava = True
    mc "Let's do it. Make her jealous."
    scene 98_s5 with dissolve
    kat "Fuck yes~ You're so bad."
    kat "Lie down... I'm gonna drain those balls dry."
    scene 98_s4 with dissolve
    jump scene98_2

label scene98_choice01_op2:
    $ kat_love += 20
    $ mc_kat_share_cum_ava = True
    mc "Better idea, share it with her. Make her swallow too."
    scene 98_s6 with Dissolve(1.0)
    kat "*laughs* You crazy son of a bitch! I love it!"
    scene 98_s7 with dissolve
    mc "Think she'd actually do it?"
    scene 98_s6 with dissolve
    if mc_harem_kat:
        kat "She has this habit of always going along with whatever I say. Deep down, I think she's more attached to me than she lets on. But I don't swing that way."
        kat "I enjoy hanging out with her now and then... but I know what I {i}really{/i} prefer. You know?"
        scene 98_s7 with dissolve
        mc "I get what you're saying."
    else:
        kat "She has this habit of always following my commands during sex. Deep down, I think she's in love with me. But I don't swing that way."
        kat "I like some girl fun now and then... but nothing beats a good cock. You know?"
        scene 98_s7 with dissolve
        mc "I... don't know. But I get what you're saying."
    scene 98_s6 with dissolve
    kat "Come on, let's give her a show she can't ignore."
    scene 98_s7 with dissolve
    jump scene98_2

label scene98_choice01_op3:
    $ mc_kat_nothing_cum_ava = True
    mc "No. I'd rather not get on her bad side. She's helping me."
    scene 98_s2 with dissolve
    kat "Pussy. But fair. She's already on edge."
    kat "You're too good sometimes."
    scene 98_s3 with dissolve
    mc "That doesn't mean I'm not fucking your throat silly tonight."
    scene 98_s2 with dissolve
    kat "Of course not. Lie down, I'm draining those balls empty."
    scene 98_s3 with dissolve
    jump scene98_2

image s98_bj1 = Movie(play="images/chapter4/scene98/s98_bj1.webm", loop=True)
image s98_bj2 = Movie(play="images/chapter4/scene98/s98_bj2.webm", loop=True)
image s98_bj3 = Movie(play="images/chapter4/scene98/s98_bj3.webm", loop=True)
image s98_bj4 = Movie(play="images/chapter4/scene98/s98_bj4.webm", loop=True)
label scene98_2:
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene4_p7_replay:
        $ persistent.scene4_p7_replay = True

    scene 98_s8 with Fade(1.0,1.0,1.0)
    ""
    scene 98_s9 with Dissolve(1.0)
    ""
    play sound "sound_effects/clothing_rustle2.mp3"
    scene 98_s10 with Dissolve(1.0)
    ""
    scene 98_s11 with Dissolve(1.0)
    kat "Hehe~"
    scene 98_s12 with Dissolve(1.3)
    kat "I've been told I have a good mouth on me."
    kat "Not only because of what I say... but because of what I can do with it."
    mc "That so?"
    if mc_harem_kat:
        kat "Mhm. Ava can vouch for me. I had her completely amazed once. She couldn't believe it."
        kat "Had her laughing her ass off."
        mc "I don't want to brag, but you may need to open it wide for me."
    else:
        kat "Mhm. Ava can vouch for me. Made her come in under a minute once. She was begging me to stop, her legs shaking and her voice breaking, but I wouldn't let go."
        kat "She came four times in a row that day. Couldn't walk straight after."
        mc "Planning to do that to me too?"
    kat "After tonight? You'll never forget how this mouth feels."
    kat "Your cock's gonna perk up every time I speak. Just thinking about it."
    mc "That's a lot of talk..."
    kat "Don't believe? Let me show~"
    scene 98_s13 with Dissolve(1.0)
    play sound "se_sfx/lick/lick1.mp3" 
    sensation "She captures your lips in a deep, hungry kiss. Her tongue teases yours, hand tangling in your hair. The kiss is fierce, demanding, her body pressing down, heat building fast."
    kat "Mmmmm~"
    scene 98_s14 with Dissolve(1.0)
    mc "Wait, who's bed is this?"
    scene 98_s15 with dissolve
    kat "Ava's."
    scene 98_s14 with dissolve
    mc "*laughs* She just said no fucking on her bed."
    scene 98_s15 with dissolve
    kat "She says that... but she won't mind."
    kat "Besides... she'll hear everything anyway."
    scene 98_s14 with dissolve
    scene 98_s16 with Fade(1.0,0.5,0.5)
    perception "She settles above your face. Her warm thighs framing you, her scent intoxicating. Below, she tugs your pants open with eager hands."
    scene 98_s17 with Dissolve(1.0)
    kat "Hahh! Look at that... you never told me you were hiding a monster down here."
    scene 98_s18 with Dissolve(1.0)
    sensation "Her lips part, tongue flicking the tip, teasing, tasting precum. Then she sinks down, warm, wet mouth taking you inch by inch, throat relaxing to swallow deeper."
    show s98_bj1 with Dissolve(1.0)
    kat "Mmmph~ So big... filling my mouth perfectly..."
    kat "Fuck... I know I'm gonna fall in love with this cock. Thick, veiny, pulsing like it's begging for my throat."
    kat "Going to suck you dry... every last drop. You'll be empty and shaking by the time I'm done."
    mc "Your tongue is insane!"
    kat "*giggles* What did I tell ya? This mouth was made for worshiping your cock."
    kat "Mmm~ I'm gonna make that precum flow like crazy... look at it already leaking for me."
    mc "Can you be a little gentler? That tongue's making me crazy..."
    kat "Gentler? Oh, baby... no chance."
    kat "Don't worry about holding back. I give you full permission to dump your whole load straight into my greedy mouth hole."
    if mc_harem_kat:
        kat "My husband's cum... all for me. I'll show Ava what a real man gives his wife."
    else:
        kat "Your cum... all for me. I'll show Ava what she's missing."
    call screen scene98_kat with dissolve

default scene97_kat_pussy_first = False
default scene98_kat_bj1 = True
default scene98_kat_bj2 = False
default s98_eat_pussy = False
label scene98_kat_pussy:
    $ s98_eat_pussy = True
    scene black with Dissolve(0.3)
    if scene98_kat_bj1:
        show s98_bj2 with Dissolve(1.0)
        if not scene97_kat_pussy_first:
            $ scene97_kat_pussy_first = True
            sensation "Her wet folds press against your lips, hot, slick, swollen with need. The taste of her floods your mouth as she grinds slowly."
            mc "Fuck, you taste amazing..."
            kat "Yes~ Lick me deeper... tongue my clit while I swallow this monster~"
        else:
            mc "Ahhnn... You're sucking just the tip... feels like my cock's gonna melt..."
            kat "Mmmph~ That's the idea. Make you so sensitive you see stars."
            kat "I can see your balls swelling up already~ Heavy and full... I'm gonna make you ejaculate twice. At least."
            kat "My clit's so stiff now, throbbing like crazy. Keep eating me while I drain you."
    else:
        show s98_bj4 with Dissolve(1.0)
        if not scene97_kat_pussy_first:
            $ scene97_kat_pussy_first = True
            mc "Mhpmmnn... I can barely breathe."
            kat "*giggles* Good. Inhale my scent. It'll make you cum faster~"
            mc "Mhnnn..."
            kat "Yes~! Right there~! Slurp my fucking clit, bite it! Uhnnn~"
        else:
            kat "Mffhnn~! [mc], you're sucking my fucking clit! Are you trying to make me gush out in your mouth?"
    call screen scene98_kat with dissolve

default scene97_kat_bj_first = False
default scene97_kat_bj_second = False
default scene97_kat_bj2_first = False
default scene97_kat_bj2_second = False
label scene98_kat_bj1:
    $ s98_eat_pussy = False
    $ scene98_kat_bj1 = True
    $ scene98_kat_bj2 = False
    scene black with Dissolve(0.3)
    show s98_bj1 with Dissolve(1.0)
    if not scene97_kat_bj_first:
        $ scene97_kat_bj_first = True
        kat "Don't worry about me coming first... I won't stop till you start gushing your seed. I'll have you ejaculating streams with just my tongue~"
        sensation "Your hips buckle involuntarily with every deep suck—her throat squeezing, tongue lashing the underside, saliva dripping down your balls."
        kat "Gods, you're throbbing so hard... I can feel you getting close already~"
        mc "Just keep those lips tight around my cock!"
        kat "*suck* *suck* You're struggling hard trying not to ejaculate. I told you, just let it out. I'll greedy mouth will happily accept it all."
        mc "Ahhng!"
    elif not scene97_kat_bj_second:
        $ scene97_kat_bj_second = True
        kat "Look at your face~ In pure bliss."
        mc "You're mine from now on! You're only allowed to suck my cock!"
        kat "*chuckles* Oh~? Keeping me for yourself? Can't blame you."
        kat "It's always good to have a girl like me around. A total cum-slut that would do anything for you."
        if mc_harem_kat:
            kat "As you wish, we're married afterall. Can't refuse my husband's wishes. This cock will satisfy me just fine."
        else:
            kat "But sorry, [mc]. As much as I'm loving this cock. We're not together... yet. I can choose to please whoever I want for now."
    else:
        kat "*slurp* Mffhnnm~ Give it to me..."
    call screen scene98_kat with dissolve

label scene98_kat_bj2:
    $ s98_eat_pussy = False
    $ scene98_kat_bj1 = False
    $ scene98_kat_bj2 = True
    if not scene97_kat_bj2_first:
        $ scene97_kat_bj2_first = True
        scene 98_s24 with Fade(0.5,0.5,0.5)
        perception "She shifts. Her thigh clampes around you like a vice, locking you in place. Her body twists sideways, mouth descending again without mercy."
        scene 98_s23 with Dissolve(1.0)
        kat "Keep eating it, please! I was so close~!"
        show s98_bj3 with Dissolve(1.0)
        sensation "Your senstive cock slides back into warm, slick heat. Her tongue attacking the raw head immediately."
        kat "Mmm~ Feel that? Your balls tightening again already... so full for me..."
        kat "I love how you taste—salty, thick... going to drain you~"
        mc "Hngg! I can't hold it any longer."
        kat "Told you. This mouth is dangerous."
        kat "Just wait till you feel those tits. Or my pussy~ You'll mouth will water just thinking about it~"
    elif not scene97_kat_bj2_second:
        $ scene97_kat_bj2_second = True
        scene black with Dissolve(0.3)
        show s98_bj3 with Dissolve(1.0)
        kat "*suck* *slurp* You're shaking so bad~"
        mc "Uhhh... I-It feels so good!"
        kat "Too bad you're running off somewhere after this."
        kat "If you stay I'll let you fuck my mouth every single day."
        mc "I-I can't stay! Uhnnn... I have lots of people depending on me!"
        kat "*giggles* I know, I was just teasing you. When you come back though... just know that I'll be waiting. On my knees. Mouth hole open, ready for you."
    else:
        scene black with Dissolve(0.3)
        show s98_bj3 with Dissolve(1.0)
        kat "*giggles* Sorry if my bush is covering your face. I never liked shaving it."
        mc "Mmmnn... Never liked or were you just lazy?"
        kat "...I'm not gonna answer that."
    call screen scene98_kat with dissolve

label scene98_kat_bj_cum1:
    mc "I'm filling your throat!"
    kat "Mmmph~ Yes~ Do it... inside. Cover my mouth with your stinky seed~"
    if scene98_kat_bj1:
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene 98_s19 with vpunch
        sensation "The pressure snaps and your cock pulses wildly in her throat, hot spurts flooding her mouth in thick endless waves. She swallows greedily at first, throat working around you, milking every drop."
        play sound "se_sfx/blowjob/blowjob_cum5.mp3" 
        scene 98_s20 with vpunch
        mc "Gahhhn!!"
        kat "Mmm~ Sho much... tashty~"
        perception "She milks you slowly through aftershocks, not stopping until you're completely spent."
        scene 98_s21 with Dissolve(1.0)
        kat "Fuck... mah moush is filled to ah brim. You're incrwdibre."
        mc "Hahh... uhh..."
        mc "God... that was... my cock is numb."
        play sound "se_sfx/blowjob/swallow1.mp3"         
        kat "*gulp* Whoops~ Ahmost shwallowed it all."
    else:
        play sound "se_sfx/blowjob/blowjob_cum1.mp3" 
        scene 98_s25 with vpunch
        sensation "The pressure snaps and your cock pulses wildly in her throat, hot spurts flooding her mouth in thick endless waves. She swallows greedily at first, throat working around you, milking every drop."
        play sound "se_sfx/blowjob/blowjob_cum5.mp3" 
        scene 98_s26 with vpunch
        mc "Gahhhn!!"
        kat "Mmm~ Sho much... tashty~"
        perception "she milks you slowly through aftershocks, not stopping until you're completely spent."
        kat "Fuck... mah moush is filled to ah brim. You're incrwdibre."
        mc "Hahh... uhh..."
    jump scene98_3
    
label scene98_3:
    scene 98_s27 with Fade(1.0,1.0,1.0)
    kat "Look~ It's ahh yours."
    if mc_kat_nothing_cum_ava:
        scene 98_s28 with dissolve
        play sound "se_sfx/blowjob/swallow3.mp3" 
        kat "*gulp* *gulp* It's going down my throat."
        scene 98_s29 with Dissolve(1.0)
        kat "Bleh~"
        kat "Every last drop, right down the hatch."
        scene 98_s31 with dissolve
        mc "You're something else..."
        scene 98_s30 with dissolve
        kat "I'm in heat, [mc]. This pussy's on fire... dripping, aching, begging for the one thing that can put it out."
        kat "Get my meaning... or should I spell it out?"
        scene 98_s31 with dissolve
        mc "I think it's clea—"
        scene 98_s32 with vpunch
        "*knock* *knock*"
        kat "We're in the middle of something, Ava! In fact... we're only getting started~"
        ava "You can do that later! I'm finished preparing."
        kat "Awww... come on. You might've missed something in that book of yours. Let us have a little more time~"
        ava "You'll do whatever you want after I'm done casting the spell. Once I finish, I'll leave the house. You two can... mate afterwards."
        scene 98_s30 with dissolve
        kat "Sounds good! Let's get on with it. I can barely wait to ride you properly."
        scene 98_s31 with dissolve
        $ renpy.end_replay()
        jump scene99
    elif mc_kat_show_cum_ava:
        kat "Come on, let's go show Ava. She'll go crazy~"
        scene 98_s33 with Fade(1.0,1.0,1.0)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        perception "Kat tugs you by the hand out of the bedroom, her cheeks slightly puffed. You follow, pants barely fastened, heart racing from the afterglow."
        scene 98_s34 with Fade(0.5,0.5,0.5)
        ava "Wha—!? Why are you still naked?"
        scene 98_s35 with Dissolve(1.0)
        kat "..."
        scene 98_s36 with dissolve
        ava "Kat? What's... what's going on? What's that white liquid on you lips?"
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene 98_s38 with dissolve
        kat "Ta-da~"
        scene 98_s37 with dissolve
        ava "Gods! Kat! That's— you— in front of me!?"
        ava "Why the hell are you showing me this...?"
        scene 98_s38 with dissolve
        kat "Becaushe ihs impreshive, wight? Rook how mush he gave me~"
        mc "She earned it. Seriously... It's still tingling down there."
        scene 98_s37 with dissolve
        ava "I... I can see that. It's... a lot."
        ava "You two... had fun, huh?"
        scene 98_s38 with dissolve
        kat "The besht. His cock's like nothing I've sheen."
        scene 98_s37 with dissolve
        ava "Right..."
        ava "Not that I needed to see it."
        scene 98_s40 with dissolve
        play sound "se_sfx/blowjob/swallow3.mp3" 
        kat "*gulp* *gulp* Mmmm..."
        scene 98_s39 with dissolve
        ava "Gods... disgusting. You're basically drinking his children, you know that?"
        ava "That liquid is supposed to go inside a woman's womb to make her pregnant, not... be swallowed orally."
        play sound "se_sfx/blowjob/swallow1.mp3" 
        scene 98_s40 with dissolve
        kat "Mmmmm~ *slurp* tashtes like heaven. Won't you give me a wittwe kish?"
        scene 98_s39 with vpunch
        ava "Never! Not until you bursh your teeth ten times in a row!"
        $ renpy.end_replay()
    else:
        kat "Come oh... I want you to wash me share thihs huge road with Ava."
        mc "I'm still not sure if she'll agree to it."
        kat "She'r hate it... but she'r do it."
        scene 98_s33 with Fade(1.0,1.0,1.0)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        perception "Kat tugs you by the hand out of the bedroom, her cheeks slightly puffed. You follow, pants barely fastened, heart racing from the afterglow."
        scene 98_s34 with Fade(0.5,0.5,0.5)
        ava "Wha—!? Why are you still naked?"
        scene 98_s35 with Dissolve(1.0)
        kat "..."
        scene 98_s36 with dissolve
        ava "Kat? What's... what's going on? What's that white liquid on you lips?"
        play sound "se_sfx/blowjob/facial7.mp3" 
        scene 98_s38 with dissolve
        kat "Look at this."
        scene 98_s37 with dissolve
        ava "Kat! Close your mouth! That's... Gods! Disgusting!"
        scene 98_s38 with dissolve
        kat "I was hoping you have a little taste. For me?"
        scene 98_s37 with dissolve
        ava "Absolutely not! That's... that's his... and you... in your mouth! No!"
        ava "I won't even entertain this idea!"
        ava "Why would you even... you know I don't... not like this!"
        scene 98_s38 with dissolve
        kat "Pleeaaaseee~? It's so much... I can't swallow it all alone."
        scene 98_s37 with dissolve
        ava "Kat, stop... this is embarrassing. I don't want—"
        scene 98_s38 with dissolve
        if mc_harem_kat:
            kat "I've seen you taste yourself plenty."
        else:
            kat "You've tasted me plenty. Fair's fair."
        scene 98_s37 with dissolve
        ava "That's different... this is... him. A man. I don't... I don't do that with men."
        scene 98_s38 with dissolve
        kat "Open up~"
        scene 98_s37 with dissolve
        ava "Kat... please..."
        scene 98_s38 with dissolve
        if mc_harem_kat:
            kat "Come on! Just for me. I'll do all of your chores later if you do. You know how much I hate chores~"
        else:
            kat "Come on! Just for me. I'll lick your asshole if you do. I know how much you love that~"
        scene 98_s37 with dissolve
        ava "I... I really hate you sometimes."
        ava "*sigh* Dammit."
        scene 98_s44 with Dissolve(1.3)
        play sound "se_sfx/blowjob/kiss2.mp3" 
        if mc_harem_kat:
            perception "Their lips finally meet. Kat passes the thick load slowly. Ava makes a small, displeased sound."
        else:
            perception "Their lips finally meet. Kat passes the thick load slowly, their tongues tangling. Ava makes a small, displeased sound but doesn't pull away."
        ava "Mmmph..."
        kat "Good girl... now show me that cute tongue."
        play sound "se_sfx/masturbate_female/2_masturbate2.mp3"
        scene 98_s45 with Dissolve(1.0)
        mc "(Fuck... this might be the hottest thing I've seen in my life.)"
        kat "Make sure to savor it~"
        ava "Ahhhnn!"
        scene 98_s47 with Dissolve(1.0)
        ava "*gag* Gods! This tastes awful! I feel like puking."
        scene 98_s46 with dissolve
        kat "Swallow it then~"
        scene 98_s47 with dissolve
        ava "I'm not going to-"
        scene 98_s46 with dissolve
        kat "Quick! Before you make a mess on the floor."
        ava "..."
        scene 98_s48 with Dissolve(1.0)
        play sound "se_sfx/blowjob/swallow3.mp3" 
        ava "*gulp* *gag*"
        scene 98_s49 with dissolve
        ava "Hahh... ahhh... fuck... happy now?! I can't believe you made me swallow a man's seed..."
        scene 98_s50 with dissolve
        kat "Gods, you're so fucking hot when you swallow cum. I never saw this side of you before."
        scene 98_s49 with dissolve
        ava "R-Really?"
        ava "*ahem* Don't answer that. I'll never do anything for you ever again!"
        scene 98_s50 with dissolve
        kat "We'll see about that~"
        scene 98_s51 with Dissolve(1.0)
        ava "You... enjoyed watching that, didn't you?"
        scene 98_s52 with dissolve
        mc "*chuckles* Can't lie."
        scene 98_s51 with dissolve
        ava "Well, don't expect this again. Ever."
        kat "Liar~ I know you liked it a little."
        ava "Shut up..."
        $ renpy.end_replay()

    scene 98_s41 with Dissolve(1.0)
    kat "*laughs* Let's go back to the bedroom, [mc]. This pussy's on fire... dripping, aching, begging for the only one thing that can put it out."
    kat "Get my meaning... or should I spell it out? I need that thick cock buried deep inside me."
    scene 98_s42 with dissolve
    ava "No! I was just about to interrupt you two—I'm done preparing."
    scene 98_s43 with dissolve
    kat "Awww... come on, Ava. Just a little quickie? Don't worry... with this pussy's grip, he won't last long~"
    scene 98_s42 with dissolve
    ava "You'll do whatever you want after I'm done casting the spell. Once I finish, I'll leave the house. You two can... mate afterwards."
    scene 98_s43 with dissolve
    kat "Sounds good! Get on with it then, I'm already soaked thinking about it."
    scene 98_s51 with dissolve
    ava "Just... don't get her pregnant, [mc]. Please?"
    scene 98_s52 with dissolve
    mc "That's a strange request."
    scene 98_s51 with dissolve
    kat "*laughs* What are you on about? Whether he knocks me up or not, mind your own, girl."
    ava "*sigh* ...Forget I said anything."

label scene99:
    if mc_refuse_bj_kat or mc_breakup_kat:
        scene 97_s10 with Fade(1.5,1.0,1.3)
        if maia_love >= 70:
            mc "(I hope Maia is doing well...)"
        scene 97_s23 with Dissolve(1.0)
        ava "Alright, I think I'm ready."
        scene 97_s24 with dissolve
        mc "Are you sure? You don't sound like it."
        scene 97_s23 with dissolve
        ava "*sigh* I'm thinking about what happened last time."
        scene 97_s24 with dissolve
        mc "Then make sure you don't repeat the same mistake."
        scene 97_s22 with dissolve
        ava "I'll try, [mc]."
        scene 97_s21 with dissolve
        mc "How should we start?"
        scene 97_s22 with dissolve
        ava "Stand up and stay over there."
        scene 97_s21 with dissolve
        scene black with Fade(0.5,0.5,0.5)
    else:
        scene 99_s1 with Fade(1.0,1.3,1.0)
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        ava "Stand still. Don't fidget."
    
    scene 99_s2 with dissolve
    mc "I'm trusting you, Ava. Take your time."
    scene 99_s1 with dissolve
    if mc_refuse_bj_kat or mc_breakup_kat:
        ava "Thank you."
    else:
        if mc_kat_show_cum_ava:
            ava "Thank you. But I'd rather get this done as soon as possible so I can leave this house and forget those noises..."
        elif mc_kat_share_cum_ava:
            ava "Thank you. But I'd rather get this done as soon as possible so I can leave this house and forget those noises... and that awful taste. Ugh, I need palate cleanser fast."
    ava "*ahem* Now. You must focus. Not on me, on the ghost of your hand, and on the metal that will become its home. Your mind must bridge the gap. Do you understand?"
    scene 99_s2 with dissolve
    mc "I understand... kinda."
    scene 99_s1 with dissolve
    ava "Move out of the way, Kat."
    stop music fadeout 1.0 
    scene 99_s3 with Dissolve(1.0)
    ""
    play sound "sound_effects/magic/magic_spell.mp3"
    scene 99_s4 with Dissolve(1.0)
    play music "desert.mp3" fadein 3.0 volume 0.7 loop
    perception "A low hum begins to vibrate the air. A circle of intricate harsh light, the color of deep moss appears in the air, painting your skin in sickly hues. The circle starts to spin at speeds your mind can't register."
    scene 99_s5 with Dissolve(1.0)
    ava "Bind this flesh to forged bone. Spirit, severed and adrift, to this vacant harbor, shift. Anchor here, by will and cost, lest both be forever lost."
    scene 99_s6 with dissolve
    mc "'Lest both be forever lost'? I don't like the sound of that..."
    play sound "sound_effects/magic/magic_beam.mp3"
    scene 99_s7 with vpunch
    if mc_agree_help_amelia_milking:
        sensation "A bolt of violent energy erupts from the circle. Bigger. Sharper. Nothing like the witch's. The pain is unbearable, far more noticeable than before."
    else:
        sensation "A bolt of violent energy shoots from the circle, a searing lance that punches the air from you lungs before dissolving into a bizarre, gentle warmth."
    if mc_agree_help_amelia_milking:
        mc "Fuck! Amelia's was nothing compared to this!"
    mc "This light is blinding!"
    ava "I said focus! The connection is thin. Hold it."
    scene 99_s8 with Dissolve(1.0)
    mc "..."
    sensation "Vivid, chaotic imagery flood your mind. Memories of touch, of pressure, of flexing fingers that were no longer there, all screaming through the cold steel."
    scene 99_s9 with Dissolve(1.0)
    ava "Good... It's reaching. It's seeking a shape. Hold steady..."
    mc "... (Nghnn! It hurts!)"
    ava "What in Karla's name is that?"
    scene 99_s10 with dissolve
    mc "What? What's happening?"
    scene 99_s12 with dissolve
    ava "Something's... there's a resonance. It's not in the metal... It's from you."
    ava "Karla's grace, no..."
    scene 99_s13 with dissolve
    kat "Ava, what's wrong?!"
    scene 99_s12 with dissolve
    ava "I have to sever the link! Now!"
    scene 99_s13 with dissolve
    mc "Why? What's happening?!"
    play sound "sound_effects/magic/magic_explosion.mp3" volume 0.5
    scene 99_s14 with vpunch
    sensation "The answer was a flash of pure, annihilating agony. It ripples through every nerve, every cell."
    sensation "Your bones are grinding, the skin is stretching and contracting like a canvas. A strange, foreign force is the only tether keeping you from instantaneous obliteration."
    mc "GAAHAHHHHH!"
    scene 99_s15 with dissolve
    mc "NGHHHH! MAKE IT STOP!"
    kat "Ava!?"
    sensation "The pain is a living thing, tugging at each individual nerve ending. You could feel the very architecture of your body being dismantled."
    mc "Stop! Please!"
    scene 99_s16 with dissolve
    mc "I'm gonna fucking die!"
    kat "She's stopped! The spell is broken!"
    mc "Please... I-I can't take it. Kat, please kill me..."
    kat "Huh!?"
    scene 99_s17 with dissolve
    perception "I screamed my pleas to the hanging herbs, the dusty instruments, the watching skulls on the shelves. No one heard. But I will."
    mc "Hahh... hhhnn... someone help me..."
    sensation "Does it not feel exquisite? A cacophony composed just for me."
    mc "Ahh... god... help... someone..."
    stop music fadeout 5.0 
    jump scene101

label scene100:
    mc "(No answer. The place feels... empty.)"
    scene 100_s1 with Fade(1.0,1.0,1.0)
    mc "Hello? Anyone inside?"
    mc "(Window's unlocked... sorry, Ava. I'm breaking in.)"
    stop music fadeout 1.0 
    scene 100_s2 with Fade(1.0,1.0,1.0)
    play music "desert.mp3" fadein 1.0 loop
    perception "Inside, the room is in chaos. Books spilled, vials overturned, a fine layer of dust over everything."
    mc "(What happened here?)"
    scene 100_s3 with Dissolve(1.0)
    mc "Ava? You here? I'm opening the door!"
    play sound "sound_effects/doors/wood_creak2.mp3"
    scene 100_s5 with Dissolve(1.0)
    perception "You slowly open the door. Ava is curled on the edge of the bed, her face buried. The sound of ragged breathing fills the quiet."
    scene 100_s4 with dissolve
    mc "A-Ava? Are you alright?"
    scene 100_s6 with dissolve
    ava "Who's there?!"
    scene 100_s7 with dissolve
    ava "Tell me why I shouldn't spill the blood from your every orifice right now, thief!"
    scene 100_s9 with dissolve
    mc "Whoa! Just look at me! It's me, [mc]!"
    scene 100_s7 with dissolve
    ava "...You! You bastard!"
    scene 100_s8 with dissolve
    mc "What are you talking about?"
    scene 100_s7 with dissolve
    ava "Don't act stupid. I know what you did, Queen Avery told me."
    ava "You were the one responsible for Kat's death! Queen Avery wanted to spare her but you... you choose otherwise."
    scene 100_s9 with dissolve
    mc "No! You got it wrong! Avery was the one that told me to decide her fate, I swear!"
    scene 100_s10 with dissolve
    ava "Filthy liar! You think I'd believe you over the Magistrate?"
    scene 100_s9 with dissolve
    mc "She's using you! She's using your grief!"
    scene 100_s10 with dissolve
    ava "Goddess of fire, I beseech thee—BRING FLAME!"
    play sound "sound_effects/magic/magic_fire2.mp3"
    stop music fadeout 1.0 
    scene 100_s11 with vpunch
    play music "angry/hard_advent.mp3" fadein 1.0 loop
    perception "A searing globe of fire erupts from her hand. You twist aside as it scorches the door behind you."
    scene 100_s12 with dissolve
    mc "Dammit, Ava! You could've killed me! Stop!"
    scene 100_s13 with dissolve
    ava "Winds of the silent deep, lend me your breath!"
    play sound "sound_effects/magic/magic_wind.mp3"
    scene 100_s14 with vpunch
    sensation "An invisible fist of air slams into your chest, lifting you off the floor and throwing you against the wall."
    mc "AGHH!"
    scene 100_s15 with Dissolve(1.3)
    ava "Oh, no. You don't get to die just yet. Look at me!"
    ava "I want you to stare into your eyes as I burn the skin from your skull. I want to hear your screams of agony."
    play sound "sound_effects/punch3.mp3"
    scene 100_s16 with vpunch
    ava "Ghk!"
    scene 100_s18 with Dissolve(1.0)
    perception "Your punch lands square against her jaw. She staggers back and collapses, hands scrambling against the floor. She can't stand, can't even lift her head. She's completely subdued."
    scene 100_s17 with Dissolve(1.0)
    ava "Goddess of fi—re... I b'see—...!"
    ava "Gobbes of fiaare, I besee..."
    ava "Goddess of fire, I besee—kh—! Tch—!"
    scene 100_s18 with dissolve
    mc "..."
    scene 100_s19 with Dissolve(1.0)
    perception "She tries to continue the spell, but the words come out slurred and broken. Whatever deity she calls to remains silent, deaf to her mangled prayer."
    mc "*laughs*"
    mc "(Wait... why am I laughing at this? This is supposed to be tragic, she lost her... friend? Lover? Whatever it is. ...For some reason I can't help but laugh.)"
    scene 100_s20 with dissolve
    mc "*ahem* That's enough, Ava."
    scene 100_s19 with dissolve
    ava "I gill you...! I swaar... I'll gill you...!"
    scene 100_s20 with dissolve
    mc "No. I need you to calm down."
    scene 100_s19 with dissolve
    perception "Her struggles grow weaker, not from lack of hatred, but from a dawning, crushing exhaustion. The fight bleeds out of her, replaced by tremors."
    scene 100_s20 with dissolve
    mc "I didn't want to hurt her and I don't want to hurt you either."
    scene 100_s19 with dissolve
    ava "You... you should have killed me."
    scene 100_s20 with dissolve
    mc "Listen to me. Avery is lying. She orchestrated the Queen's death. She needed Kat silenced. She used me to make it look lawful. I swear it on my life. On her memory."
    scene 100_s19 with dissolve
    ava "..."
    empathy "Silence, broken only by her hiccupping breaths. A tear traces a clean line through the dust on her cheek."
    ava "...Go. Just get out of my sight."
    scene 100_s20 with dissolve
    mc "I can't. I need your help to make it right."
    scene 100_s19 with dissolve
    ava "Right? Nothing will ever make it right. She's gone."
    scene 100_s20 with dissolve
    mc "Then let me punish the one who took her. Help me. My arm, I need the living steel enchantment. With it, I can tear down Avery's lies. I can give Kat's death meaning."
    scene 100_s21 with Dissolve(1.0)
    ava "*sniff* Heh... You want a spell?"
    ava "Fine. I'll give you your spell."
    play sound "sound_effects/magic/magic_spell.mp3"
    scene 100_s22 with dissolve
    ava "Bind this flesh to forged bone. Spirit, severed and adrift, to this vacant harbor, shift. Anchor here, and let both be forever lost."
    play sound "sound_effects/magic/magic_beam.mp3"
    scene 100_s23 with vpunch
    sensation "A bolt of violent energy shoots from the circle, a searing lance that punches the air from you lungs before dissolving into a bizarre, gentle warmth."
    mc "Careful, Ava. Please..."
    mc "Nghn!"
    sensation "Vivid, chaotic imagery flood your mind. Memories of touch, of pressure, of flexing fingers that were no longer there, all screaming through the cold steel."
    ava "What in Karla's name is that?"
    scene 100_s24 with dissolve
    mc "Ava, what's wrong?!"
    scene 100_s22 with dissolve
    ava "*chuckles* Good. Let her take you to the depths of the void."
    scene 100_s24 with dissolve
    mc "Huh? What's happening?!"
    play sound "sound_effects/magic/magic_explosion.mp3"
    scene 100_s25 with vpunch
    sensation "The answer was a flash of pure, annihilating agony. It ripples through every nerve, every cell."
    sensation "Your bones are grinding, your skin stretching and contracting like a canvas. A strange, foreign force is the only tether keeping you from instantaneous obliteration."
    mc "GAAHAHHHHH!"
    scene 100_s26 with dissolve
    mc "NGHHHH! MAKE IT STOP!"
    sensation "The pain is a living thing, tugging at each individual nerve ending. You could feel the very architecture of your body being dismantled."
    mc "Stop! Please!"
    mc "I'm gonna fucking die!"
    scene 100_s27 with dissolve
    perception "I screamed my pleas to the hanging herbs, the dusty instruments, the watching skulls on the shelves. No one heard. But I will."
    mc "Hahh... hhhnn... someone help me..."
    sensation "Does it not feel exquisite? A cacophony composed just for me."
    mc "Ahh... god... help... someone..."
    stop music fadeout 3.0 
    jump scene101

label scene100_2:
    $ ava_dead = True
    play music "fire.mp3" fadein 3.0 loop
    scene 100_s28 with Fade(1.0,1.0,1.0)
    ""
    scene 100_s29 with Dissolve(1.0)
    mc "..."
    scene 100_s30 with Dissolve(1.0)
    impulse "She tried to kill you. Drive the dagger into her heart. Destroy those who appose you."
    scene 100_s31 with Dissolve(1.0)
    logic "Under the bed. Quick, before the fire consume her anyway."
    call screen scene100_choice01 with dissolve

label scene100_choice01_op1:
    jump scene101_2
    
label scene100_choice01_op2:
    $ mc_kill_ava = True
    if mc_karma > 1:
        $ mc_karma -= 3
    scene 100_s32 with Fade(1.0,1.0,1.0)
    ""
    play sound "sound_effects/stab3.mp3"
    scene 100_s33 with Dissolve(1.0)
    minthra "Excellent. Her soul is potent, she shall strengthen me considerably."
    jump scene101_2

label scene101:
    scene 101_s1 with Dissolve(3.0)
    perception "The world of pain dissolves, not into darkness, but into a silent, star-dusted cosmos. A void of impossible scale, and from its absolute center, a figure stands."
    minthra "Long have I awaited this moment, [mc]."
    play music "ambiance/realms.mp3" fadein 4.0 loop
    scene 101_s2 with Dissolve(1.3)
    minthra "I am the Weaver at the End, the Keeper of Forgotten Seeds. I am Minthra, Goddess of Rebirth."
    perception "She stands before me, a vision of serene, terrifying majesty amid the stars. Her expression carries the weight of countless ends and beginnings."
    scene 101_s3 with Dissolve(1.3)
    minthra "You stand upon the precipice between realms where I had plucked your soul from the torrent. A vessel... fascinatingly resilient. Strong enough to bear a fragment of my will yet weak enough to require it."
    minthra "I have gifted you a second dawn. A chance to act where I, in my current state, cannot."
    minthra "Your rebirth weakened me and so our bond frayed. Yet I have guided you still, my thoughts whispering within your own."
    scene 101_s4 with Dissolve(1.3)
    sensation "A fresh, searing pain lanced through my core as she spoke, not from injury, but from the sheer, oppressive weight of her presence pressing against my mortal shell."
    minthra "That mage's exceptional failure has stirred our connection once more."
    scene 101_s5 with Dissolve(1.3)
    minthra "You have performed poorly thus far. But worry not, this is only the beginning."
    minthra "You will walk the mortal world I cannot yet tread. And where you walk, endings will follow."
    scene 101_s6 with Dissolve(1.3)
    minthra "With each death you deliver to those who would stand against us, with each final breath offered in my name... I grow stronger."
    scene 101_s7 with Dissolve(1.3)
    minthra "Nurture me with their conclusions, and I will reward you beyond the petty imaginings of kings. You will not just rule a kingdom of dirt and stone."
    minthra "You will be my consort. We shall rule this realm together."
    scene 101_s8 with dissolve
    call screen scene101_choice01 with dissolve

label scene101_choice01_op1:
    $ mc_agree_minthra = True
    $ minthra_love += 10
    $ mc_karma -= 1
    perception "You have no strength for words, only for truth. Your body, a broken instrument, gives the only answer it can. You let your head fall forward in a slow, infinitesimal nod."
    scene 101_s7 with dissolve
    minthra "The pain will recede soon. My will shall be your guide. Sleep now, my champion. When you wake, our work begins."
    minthra "Do not fail me."
    scene 101_s8 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    stop music fadeout 6.0 
    perception "The cosmos gently folds in around you, not with violence, but with the absolute finality of a tomb door sealing shut."
    if mc_execute_kat or mc_life_kat:
        jump scene100_2
    jump scene101_2

label scene101_choice01_op2:
    perception "You lock your screaming muscles, forcing your body to absolute stillness. You do not nod. You do not blink. You hold the shattered remnant of your will in your gaze and meet her star-filled eyes with a silent, stubborn refusal."
    scene 101_s7 with dissolve
    minthra "Ah. You mistake this for a request, vessel. This was {i}not{/i} a request. It is the fundamental command of your new existence."
    scene 101_s9 with Dissolve(1.0)
    minthra "Refuse and I banish you here with me. A place with no end. No beginning. Just this perfect, silent awareness, fused forever with the agony of your unraveling."
    minthra "You will be a monument to futility, gazing at the unreachable cosmos for an eternity that has only just begun."
    scene 101_s8 with Dissolve(1.0)
    sensation "Your soul shrieks at the thought of this now becoming your always. The present pain, unbearable as it is, becomes a coveted memory compared to the infinite, frozen moment she describes."
    scene 101_s7 with dissolve
    minthra "Do no fail me."
    scene 101_s8 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    stop music fadeout 6.0 
    perception "The cosmos gently folds in around you, not with violence, but with the absolute finality of a tomb door sealing shut."
    if mc_execute_kat or mc_life_kat:
        jump scene100_2
    jump scene101_2

label scene101_2:
    if mc_execute_kat or mc_life_kat:
        pause(0.1)
    else:
        scene 99_s18 with Dissolve(1.5)
        kat "Ava wake up! Please!"
        play music "fire.mp3" fadein 1.0 volume 0.5 loop
        kat "[mc]? You just... vanished. Where did you go?"
        mc "..."
        scene 99_s19 with Dissolve(1.0)
        kat "Ava's alive, but she's out cold. Her pulse is there, but it's... slow. Like she's dreaming."
        kat "We need to bring her to a healer quick!"
        scene 99_s21 with Dissolve(1.0)
        mc "..."
        scene 99_s20 with Dissolve(1.0)
        kat "Say something!"
        kat "Where are you going?! I need help here!"
        stop music fadeout 1.0 
        scene 99_s22 with dissolve
        kat "[mc]!"
    
    if mc_agree_help_amelia_milking:
        scene 99_s23 with Fade(1.0,1.0,1.0)
        ""
    stop music fadeout 1.0 
    scene 99_s24 with Fade(1.0,1.0,1.0)
    ""
    scene 101_s10 with Fade(1.0,1.0,1.0)
    #play music "river.mp3" fadein 1.0 volume 0.6 loop
    m "Go find him! Now!"
    scene 101_s11 with dissolve
    if mc_choose_amelia:
        alex "Will you calm your shit down? The letter said he'd be taking longer than expected. Have some faith in him."
    else:
        alex "Will you calm your shit down? It's barely dawn yet. Have some faith in him."
    scene 101_s10 with dissolve
    m "If no one else is going, then I—"
    scene 101_s12 with dissolve
    reham "Wait... It's him!"
    scene 101_s13 with dissolve
    m "Oh, thank the Gods! [mc]!"
    alex "See? I told you... *sigh* Thank god."
    scene 101_s14 with dissolve
    alex "You... you actually convinced them to make you one. How does it feel?" 
    mc "..."
    reham "A-Are you alright, [mc]? You're... you're pale."
    scene 101_s16 with Dissolve(1.0)
    alex "I feel it again. That strange sensation... the cold, wrong presence I told you about. Only... it's a thousand times stronger."
    play music "hope/mountain_mist.mp3" fadein 4.0 loop
    play sound "sound_effects/clothing_rustle.mp3"
    scene 101_s18 with dissolve
    m "It's fine, everything is going to be fine. We're together now. You're safe." 
    scene 101_s17 with dissolve
    alex "Maia, you don't understand what I'm saying."
    mc "I saw what I have to do."
    m "Hm?"
    mc "I can end it. All of it."
    scene 101_s18 with dissolve
    m "Then... do what you must."
    scene 101_s17 with dissolve
    mc "Can I... destroy them?"
    reham "What are you saying?"
    alex "Destroy who? Avery? My father? Or... everyone?"
    scene 101_s18 with dissolve
    m "If that's what it takes... then yes."
    scene 101_s19 with Dissolve(1.0)
    m "They took everything from us. From you. If destruction is the only way forward... then destroy them. Burn it all down."
    m "But you come back to me. No matter what. Promise me that."
    mc "..."
    stop music fadeout 5.0 
    scene black with Fade(1.5,0.2,0.2)
    scene black
    if maia_pregnant:
        $ pregnancies += 1
    if reb_pregnant:
        $ pregnancies += 1
    if diana_pregnant:
        $ pregnancies += 1
    if mc_paricipated_festival:
        if not mc_date_adaroza_fail:
            if mc_date_adaroza_final:
                $ pregnancies += 1
        if not mc_date_sigrun_points < 3:
            if mc_date_sigrun_final:
                $ pregnancies += 1

        $ pregnancies += 1 #ANN

    if mc_nadia_pregnant:
        $ pregnancies += 1
    
    show expression "chapter1_journey_main" at center with Fade(1.5,1.0,1.0)
    window hide
    pause 0.5
    play music "images/custom_gui/global/mainmenu/mainmenu_song.mp3" fadein 2.0 loop
    window show
    ""

    if mc_save_queen:
        show chapter4_recap1_life with dissolve
        "In her darkest moment, she remembered your kindness. She stepped back from the edge. The Queen breathes another day because of you."
    else:
        show chapter4_recap1_death with dissolve
        "Alone. That's how she felt when she made her choice. Her brother's life, traded for a life. Now the Queen is no more. Alex got what she wanted. But sometimes, she wonders if she's lost more than she gained."

    if mc_slap_avery:
        show chapter4_recap2_slap with dissolve
        hide chapter4_recap1_life
        hide chapter4_recap1_death
        "Kings or queens. Your hands know no title. When she stood before you, arrogance dripping from every word, you reminded her that crowns don't stop fists. But Rebecca... Rebecca may wear the punishment intended for you."
    else:
        show chapter4_recap2_noslap with dissolve
        hide chapter4_recap1_life
        hide chapter4_recap1_death
        "In the moment of white-hot rage, you chose stillness. Perhaps it was fear for Rebecca. Perhaps it was wisdom. Either way, your restraint might have saved her from severe punishment."

    show chapter4_recap3 with dissolve
    hide chapter4_recap2_slap
    hide chapter4_recap2_noslap
    if mc_accept_ablegirl:
        "Compassion. Or foolishness. It ended in tragedy, her blood on ground that didn't care, her story unfinished. Does her death matter? In the vast scheme of life, probably not."
    else:
        "Her words fell on deaf ears. You left her to face destiny alone, as we all must. You don't know what became of her. You tell yourself you don't want to."


    if mc_hug_alex:
        show chapter4_recap4_hug with dissolve
        hide chapter4_recap3
        "Alex told you everything. The weight she carried, the choices that haunt her. You didn't answer with words. You answered with your arms. It might be the only thing she needed in that moment."
    elif mc_slap_alex:
        show chapter4_recap4_slap with dissolve
        hide chapter4_recap3
        "The slap echoed louder than words. She recoiled, but something in her eyes shifted. Pain, yes. But also... recognition? You've drawn a line between you now. Whether it's a boundary or a battle line remains to be seen."


    if mc_try_kiss_alex:
        show chapter4_recap5_kiss with dissolve
        hide chapter4_recap4_slap
        hide chapter4_recap4_hug
        "Alex laid out her plans to tear down Avery and her father. And in that moment you leaned in. She pulled back, startled. But her solitude, the walls she's built for years, they're showing cracks. You're getting through."
    elif mc_agree_alex:
        show chapter4_recap5_accept with dissolve
        hide chapter4_recap4_slap
        hide chapter4_recap4_hug
        "Her plans, your support. Simple as that. She looked at you and saw someone who believed in her without reservation. Trust like that doesn't come easy for Alex. She's given it to you now. Don't waste it."
    else:
        show chapter4_recap5_angry with dissolve
        hide chapter4_recap4_slap
        hide chapter4_recap4_hug
        "You'll help her. Yes. But not for her. For yourself. For your own grudges, your own ambitions. She sees it in your eyes—the distance, the calculation. She'll use you anyway. That's what survivors do."


    show chapter4_recap6 with dissolve
    hide chapter4_recap5_kiss
    hide chapter4_recap5_accept
    hide chapter4_recap5_angry
    if mc_harem_reham_dom_dom:
        "You told her you wanted her—heart, body, and soul. Three things to give, three things to take. Surprisingly, she agreed. Perhaps she was always waiting for someone to ask for all of her. She's yours now, as completely as the word allows."
    elif mc_harem_reham_dom:
        "You told her you wanted her, heart and body. It's enough. For now."
    elif mc_harem_reham:
        "You told her she would serve you. Nothing more. She agreed without hesitation. A transaction, clean and cold. She'll do her duty. Whether she'll do more is up to you."
    else:
        "Reham is not your servant. She moves through her days as she always has, unclaimed, unspoken for."


    if mc_agree_maia_outside:
        show chapter4_recap7_out with dissolve
        hide chapter4_recap6
        if mc_maia_story:
            "You gave her the world outside, under your watch, your protection. And she rewarded you with the story she'd buried for years. Your love cracked her open, and she let you see the rot inside. Now you can heal it. Together."
        else:
            "Fresh air. But her story stayed locked away. She's not ready. Maybe she never will be. Your love hasn't won her complete trust yet. Patience, or loss. The choice remains yours."
    else:
        show chapter4_recap7_in with dissolve
        hide chapter4_recap6
        "You agreed with Reham. Maia stays inside. It's for her benefit, you tell yourself. Safety over freedom. Protection over trust. She doesn't argue. But she doesn't thank you either."

    show chapter4_recap8 with dissolve
    hide chapter4_recap7_in
    hide chapter4_recap7_out
    if mc_princess_alex:
        "You accepted Alex's proposal. The castle, the guards, the executioner's clock ticking. You're going to pull a princess from the lion's den. Madness, perhaps. But madness with purpose."
    else:
        "The princess will have to wait, or die waiting. You've made your choice. Trade one duty for another. The road east promises different dangers, different rewards."
    

    if mc_console_maia:
        show chapter4_recap9_happy with dissolve
        hide chapter4_recap8
        if mc_maia_left_return:
            "In her moment of absolute fracture, you held her together. And she asked, terrified—if you could try again. You said yes. It might be the happiest moment of her life."
        elif mc_maia_left_twice:
            "In her moment of absolute fracture, you held her together. She crawled back, offering her heart again. You'd already broken it once. Twice now. She won't ask a third time."
        else:
            "In her moment of absolute fracture, you held her together. She kissed you. And in that kiss, a promise of lifelong servitude, or partnership, depending on how you see it."
    else:
        show chapter4_recap9_sad with dissolve
        hide chapter4_recap8
        "You came to her broken, and then brushed her aside. Her heart was already in pieces. It doesn't matter now, you tell yourself. But the way she looks at you when you're not watching suggests otherwise."

    show chapter4_recap10 with dissolve
    hide chapter4_recap9_happy
    hide chapter4_recap9_sad
    if mc_want_help_serena:
        "She told you everything. What happened to her daughter, the cruelty dressed as law. You couldn't stand still. You won't stand still. Serena has someone in her corner now. "
    else:
        "Another tragedy. Another name to forget. Serena's mother spoke, and you listened, and then you left. Serena has lost hope in the world. She's not wrong to."

    show chapter4_recap14 with dissolve
    hide chapter4_recap13_kiss
    hide chapter4_recap13_leave
    if mc_choose_amelia:
        if mc_agree_help_amelia_milking:
            "Dean told you to find a sorcerer. You choose a witch in a swamp. She had... unconventional demands. You met them. If only you'd known her incompetence before she laid hands on you."
            if mc_wants_impregnate_amelia:
                show chapter4_recap14_2 with dissolve
                hide chapter4_recap14
                "Once Amelia was satisfied, you told her that you want to... impregnate her. Whether you truly wanted her to be yours, or you simply wanted to have fun, she fell for you."
        else:
            "Dean told you to find a sorcerer. You choose a witch in a swamp. You also found your senses and refused her terms."
    else:
        "Dean told you to find a sorcerer. You choose Ava, the elven woman who once assessed your mana, a choice much more sound than a witch."
        
    show chapter4_recap11 with dissolve
    hide chapter4_recap10
    if elara_dead:
        "Skitter-Maws. A nest of them. She went with her friends, her bow, her hope. You have a feeling, cold and certain that you won't see her again."
    else:
        "Perhaps you saved her by bringing her into the guild. Perhaps you merely delayed the inevitable. The cost of her survival remains to be calculated."

    show chapter4_recap12 with dissolve
    hide chapter4_recap11
    if mc_debt:
        "Dean asked for fifty gold coins as payment for your new hand. You told him later, maybe never."
    else:
        "Dean asked for fifty gold coins as payment for your new hand. You told him that restoring the city would be payment enough. He laughed, but beneath the laughter, he saw something in your eyes. Fire. Purpose. He'll wait. He's curious now."
    
    if mc_kiss_yuuhi_leaving:
        show chapter4_recap13_kiss with dissolve
        hide chapter4_recap12
        if mc_kiss_yuuhi_nonharem:
            "You kissed her. A gentle press of lips that said what words couldn't. She didn't flinch, didn't pull away in shock, as if she'd been expecting this moment for longer than either of you knew. Perhaps she had feelings all along."
        else:
            "You pulled her close, gently. Your lips met hers in a soft kiss. When you pulled back, her eyes were filled with quiet sadness. She'll wait for you now. She always has."

    else:
        show chapter4_recap13_leave with dissolve
        hide chapter4_recap12
        "You spoke your gratitude, turned, and walked away. It's better this way. Cleaner. Safer. Attachment is a chain, and she deserves to be free of yours."

    if mc_execute_kat or mc_life_kat:
        show chapter4_recap15 with dissolve
        hide chapter4_recap14
        hide chapter4_recap14_2
        if mc_kill_ava:
            "You woke in a cold sweat. The dagger hidden across the room. It found her heart. She never woke. Her unconscious body gave no resistance, no final words. Just silence and spreading red."
        else:
            "You woke in a cold sweat. The dagger hidden across the room. And you chose not to kill. To let her live. She lies there now, amidst the fire you didn't start, her body likely charred beyond recognition. But you'll know. You'll always know she was alive when you left."
    else:
        show chapter4_recap16 with dissolve
        hide chapter4_recap14
        hide chapter4_recap14_2
        hide chapter4_recap15
        if mc_breakup_kat:
            "Her heat got the better of her. She told you what she wanted, how she wanted to please you. And you cut it off, clean and cold. No future here. She understood."
        elif mc_told_kat_polygamy:
            "You told her about your other relationships. She didn't mind. In fact, she seemed more eager. Kat has never been one for convention. Why start now?"
        elif mc_refuse_bj_kat:
            "She offered to please you. You declined—not forever, just for now. Wrong moment, wrong place. She nodded, accepting."
        else:
            "You took what she offered. Pleasure, brief and bright. But Ava's look from across the room followed you out the door. Perhaps you should keep your distance."
    
    show chapter4_recap17 with dissolve
    hide chapter4_recap16
    hide chapter4_recap15
    if mc_agree_minthra:
        "In the presence of something beyond your understanding, you bowed your head. Was it surrender? Was it strategy? Was it simply the desire for the pain to end? You nodded."
    else:
        "A mortal before a god. You didn't bow. You didn't break. You stood, silent and unmoving, and met her gaze with whatever shred of yourself remained. She could destroy you. She didn't."
        
    hide chapter4_recap13_leave
    hide chapter4_recap17 with dissolve

    show chapter4_recap18 with dissolve
    if pregnancies == 7:
        "[pregnancies] out of 7 available women are now expecting. Looks like you're single-handedly repopulating the city..."
    elif pregnancies >= 4:
        "You've knocked up [pregnancies] of the 7 available lovely ladies. Leave some for the rest of us, stud!"
    elif pregnancies >= 1:
        "[pregnancies] out of 7 available women are carrying your child. Someone's been a busy bee, haven't they?"
    else:
        "You haven't impregnated a single woman so far. Are you feeling okay? Or just... responsible?"
    
    show chapter1_recap12 with dissolve
    hide chapter2_recap11
    if not karma_updated:
        $ karma_updated = True
        if mc_karma >= 100:
            $ mc_karma = 10
        elif mc_karma >= 90:
            $ mc_karma = 9
        elif mc_karma >= 80:
            $ mc_karma = 8
        elif mc_karma >= 70:
            $ mc_karma = 7
        elif mc_karma >= 60:
            $ mc_karma = 6
        elif mc_karma >= 50:
            $ mc_karma = 5
        elif mc_karma >= 40:
            $ mc_karma = 4
        elif mc_karma >= 30:
            $ mc_karma = 3
        elif mc_karma >= 20:
            $ mc_karma = 2
        elif mc_karma >= 10:
            $ mc_karma = 1
        else:
            $ mc_karma = 1

    if mc_karma < 1:
        $ mc_karma = 1
    if mc_karma > 10:
        $ mc_karma = 10
    "You have [mc_coin] coins to your name, and your honor stands at [mc_karma] out of 10. Whatever that means."
    window hide
    scene chapter5 with Fade(1.5,0.5,1.5)
    ""
    stop music fadeout 1.5
    jump scene102

label scene102:
    scene 102_s1 with Fade(1.0,1.0,1.0)
    ""
    jump scene102_2


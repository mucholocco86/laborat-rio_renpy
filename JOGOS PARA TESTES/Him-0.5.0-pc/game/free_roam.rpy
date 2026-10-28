default free_roam_tutorial5_first = False
label free_roam_main_label:
    stop music fadeout 1.0

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

    if in_scene18:
        jump scene18_free_roam_up2
    elif in_scene30:
        if not mc_armor_timer == 0:
            $ current_objective = "Main Quest: I visited the blacksmith today and met \nYuuhi. A shy and nerdy girl. Kind of a weirdo too. \nShe took my measurements and said it'll take about \nthree days before my new armor's ready. Can't wait!!\n"
        else:
            $ current_objective = "Main Quest: My armor should be ready. \nI should visit Yuuhi and see.\n"
        if mc_market_first:
            $ second_objective = "Main Quest: When I first arrived in this city, the \nmarket instantly caught my attention. So many \nthings being sold, some I can't even recognize! \nI swear I even saw a stall selling green looking meat. \nGotta check it out.\n"
        else:
            $ second_objective = ""
        if mc_accept_helped_nadia and not (mc_friend_nadia or mc_harem_nadia):
            $ third_objective = "Side Quest: Oh, Nadia. I promised to help her! \nBetter get to it too."
        else:
            $ third_objective = ""
        if mc_armor_timer == 3:
            scene 29_s5 with fade
            call screen free_roam_choices with dissolve
        elif mc_armor_timer == 2:
            scene 29_s5 with fade
            if not free_roam_tutorial5_first:
                $ free_roam_tutorial5_first = True
                call screen free_roam_tutorial5 with dissolve
            call screen free_roam_choices with dissolve
        elif mc_armor_timer == 1:
            scene 32_s1 with fade
            mc "(One days left for the armor. Might as well do something.)"
            call screen free_roam_choices with dissolve
        elif mc_armor_timer == 0:
            scene 32_s2 with fade
            mc "(The armor should be ready by now, I should go to the blacksmith.)"
            call screen free_roam_choices with dissolve
    elif in_scene32:
        $ current_objective = "Main Quest: Wait for your armor."
        scene 29_s5 with fade
        mc "(Now that I've got my armor, I should talk to Eireen.)"
        call screen free_roam_choices with dissolve
    elif in_scene34:
        scene 30_s16 with fade
        $ current_objective = "Main Quest: The witch has been dealt with. \nI think I've earned some rest.\n"
        if mc_harem_yuuhi and not yuuhi_harem_training_finished:
            $ second_objective = "Side Quest: Me and Yuuhi are a thing now. She kind \nof reminds me of Maia, both too easy to please and \ntoo trusting for their own good. \nI guess it's better they ended up with me than some \nother asshole... right? Anyway, I promised I'd come \nback every now and then to check on her. Maybe \neven have a little fun while I'm at it.\n"
        else:
            $ second_objective = ""

        if mc_harem_nadia and not mc_harem_talk_nadia:
            $ third_objective = "Side Quest: I made a move on Nadia and she just... \nran away. I honestly thought, being older, she'd just \ngive me a straight answer but I guess not. I'll have \nto stop by the market again and see if she's ready to \ntalk."
        else:
            $ third_objective = ""

        if mc_harem_nadia and not mc_harem_talk_nadia:
            mc "(I should check out Nadia. Hopefully she has an answer now.)"
        else:
            mc "(I can take it easy today.)"
        call screen free_roam_choices with dissolve
    elif in_scene35:
        $ current_objective = "Main Quest: The Queen told me to meet with Eireen \nat the guild to start my next task. This time, I'll try \nnot to not get caught off guard like I did with the \nwitch...\n"
        if mc_harem_yuuhi and not yuuhi_harem_training_finished:
            $ second_objective = "Side Quest: Me and Yuuhi are a thing now. She kind \nof reminds me of Maia, both too easy to please and \ntoo trusting for their own good. \nI guess it's better they ended up with me than some \nother asshole... right? Anyway, I promised I'd come \nback every now and then to check on her. Maybe \neven have a little fun while I'm at it.\n"
        else:
            $ second_objective = ""
        
        if not mc_friend_reb:
            if "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it." not in (second_objective, third_objective):
                if second_objective == "":
                    $ second_objective = "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it."
                else:
                    $ third_objective = "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it."
        elif second_objective == third_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
            $ third_objective = ""
            
        else:
            if second_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
                $ second_objective = ""
            elif third_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
                $ third_objective = ""
            
        scene 30_s16 with fade
        if not mc_friend_reb:
            if mc_reb_works_for_me:
                mc "(Rebecca told me she'll handle it with her mother. Can I really trust her?)"
            else:
                mc "(I'll try to befriend Rebecca before heading to Eireen.)"
        else:
            mc "(Now that Rebecca accepts me, I should head over to Eireen.)"
        call screen free_roam_choices with dissolve
    elif in_scene35_2:
        $ current_objective = "Main Quest: I told Eireen I'd take a few days to get \nready. I need to clear my head before jumping into \nwhatever's next."
        if mc_harem_yuuhi and not yuuhi_harem_training_finished:
            $ second_objective = "Side Quest: Me and Yuuhi are a thing now. She kind \nof reminds me of Maia, both too easy to please and \ntoo trusting for their own good. \nI guess it's better they ended up with me than some \nother asshole... right? Anyway, I promised I'd come \nback every now and then to check on her. Maybe \neven have a little fun while I'm at it.\n"
        else:
            $ second_objective = ""
        
        if not mc_friend_reb:
            if "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it." not in (second_objective, third_objective):
                if second_objective == "":
                    $ second_objective = "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it."
                else:
                    $ third_objective = "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it."
        elif second_objective == third_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
            $ third_objective = ""

        else:
            if second_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
                $ second_objective = ""
            elif third_objective == "Side Quest: The Queen said the I should befriend \nher daughter, Rebecca. Yeah, befriend. She must \nreally think highly of me if she wants me to cozy \nup to her daughter. But something tells me Rebecca \nwon't be thrilled about it.":
                $ third_objective = ""
                
        scene 30_s16 with fade
        if in_scene35_2_timer == 3:
            mc "(Three days until my mission begins.)"
        elif in_scene35_2_timer == 2:
            mc "(Two days until my mission begins.)"
        elif in_scene35_2_timer == 1:
            mc "(One day until my mission begins.)"
        else:
            mc "(Today's the day.)"
        call screen free_roam_choices with dissolve
    elif in_scene64:
        scene 30_s16 with fade
        $ current_objective = "Main Quest: I've done my tasks. Gotta say, being a \nsteward isn't half bad, I get to meet all kinds of \npeople. Wouldn't mind if Avery gave me a few more \njobs, actually. \nFor now though, I think I've earned a break.\n"
        if not yuuhi_harem_training_finished and mc_harem_yuuhi:
            $ second_objective = "Side Quest: Me and Yuuhi are a thing now. She kind \nof reminds me of Maia, both too easy to please and \ntoo trusting for their own good. \nI guess it's better they ended up with me than some \nother asshole... right? Anyway, I promised I'd come \nback every now and then to check on her. Maybe \neven have a little fun while I'm at it.\n"
        else:
            $ second_objective = ""
        $ third_objective = ""
        call screen free_roam_choices with dissolve

default in_scene64_maia_reb_talk = False
default maia_first_time_talk = True
label free_roam_maia:
    play music "maia.mp3" fadein 3.0 loop
    $ maia_sex_tab_regular = False
    $ all_options = True
    scene 18_s6 with Fade(0.5,0.5,0.5)
    mc "Hey, Maia!"
    $ mc_maia_no_sex = False

    if maia_first_time_talk:
        $ maia_first_time_talk = False
        scene 18_s8 with dissolve
        m "Good morning, [mx]! I'm sorry I was still sleeping when you arrived yesterday."
        scene 18_s7 with dissolve
        mc "Don't worry about it. Never let anyone get between you and your sleep, that's my motto."
        scene 18_s8 with dissolve
        m "*chuckles* As you wish, [mx]."
        scene 18_s7 with dissolve
        call screen is_maia with dissolve
    if not mc_didnt_accept_crumps and maia_love >= 30:
        if maia_know_wed_reb and not mc_told_maia_nadia_sex and not mc_talked_maia_wed_reb:
            jump free_roam_maia_reb_wed
        elif in_scene64 and not in_scene64_maia_reb_talk:
            jump in_scene64_maia_reb_talk
        else:
            jump free_roam_maia_main
        
    else:
        jump free_roam_maia_sad

label free_roam_maia_main:
    #play music "maia.mp3" fadein 2.0 loop
    $ maia_sex_tab_regular = False
    $ all_options = True
    scene 18_s8 with dissolve
    if speech_cycle == 0:
        m "Hello, [mx]."
    elif speech_cycle == 1:
        m "Good morning, [mx]. Did you sleep well? I... I hope you did."  
    elif speech_cycle == 2:
        m "I wonder when your birthday is, [mx]... I already have a gift in mind~"  
    elif speech_cycle == 3:
        m "Last night, I woke up and heard you talking in your sleep... I think you were singing? It was... kind of cute."
    elif speech_cycle == 4:
        m "Good morning, my love~"
    elif speech_cycle == 5:
        m "We should visit the beach someday, [mx]... Just the two of us, under the warm sun... Doesn't that sound nice?"
    elif speech_cycle == 6:
        m "I had a dream about you last night... but it's too embarrassing to say." 
    elif speech_cycle == 7:
        m "You know, [mx]... sometimes I think about how different things could have been if we had met earlier... but I wouldn't change a thing now."
    elif speech_cycle == 8:
        m "I tried baking something with Ren today... It didn't turn out very well. I think I made a new type of rock. *chuckles*"   
    elif speech_cycle == 9:
        m "I saw a really big bug earlier. I was going to call for you, but then I thought—what if you're scared of bugs too? That would have been a disaster!"  
    elif speech_cycle == 10:
        m "Sometimes, when I see you, my heart beats so fast... I wonder if you notice."
    elif speech_cycle == 11:
        m "I saw a cat today! It somehow snuck past the guards, they wouldn't let me pet it before taking it outside..."
    elif speech_cycle == 12:
        m "I accidentally tripped back when you first came to the castle... I hope you didn't see me, [mx]." 
    scene 18_s7 with dissolve
    if mc_has_strawberries and not mc_refused_strawberries_maia:
        mc "(I have the strawberries she asked for.)"
        call screen mc_has_strawberries
        $ mc_refused_strawberries_maia = True
    call screen is_maia with dissolve

default mc_refused_strawberries_maia = False
default mc_refused_strawberries_yuuhi = False

screen mc_has_strawberries():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("maia_gift")
    text "Give her the strawberries":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Keep it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen mc_has_strawberries_yuuhi():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("yuuhi_gift")
    text "Give her the strawberries":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Keep it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label free_roam_maia_sad:
    if maia_love <= 30:
        $ maia_sad = True
        $ maia_happy = False
    scene 18_s16 with dissolve
    m "Yes, [mx]."
    scene 18_s15 with dissolve
    mc "You're still sad about that? It's just a cat."
    m "..."
    call screen is_maia with dissolve
     
label maia_sex_end:
    play music "maia.mp3" fadein 3.0 loop
    scene 18_s8 with Fade(0.5,0.5,0.5)
    if maia_hj:
        $ maia_hj = False
        m "Is your cock calm now, [mx]? I can... give you a-another handjob if not~"
    elif maia_tj:
        $ maia_tj = False
        m "My breasts feel so sweaty after that... you really like them, [mx]~"
    elif maia_bj:
        $ maia_bj = False
        m "Did my mouth feel good, [mx]? You can use it whenever to feed me your delicious semen~"
    elif maia_sex:
        $ maia_sex = False
        m "You ejaculated so much, [mx]... I can still feel some of it inside me~"
    elif maia_fj:
        $ maia_fj = False
        m "You seemed to have lots of fun covering my feet, [mx]~"
    scene 18_s7 with dissolve
    call screen is_maia with dissolve

default update0_3_1_tasks_armor_fin_talk = False
default free_roam_yuuhi_first = True
default yuuhi_armor_speech = True
default mc_armor_timer2 = True
default mc_armor_timer1 = True

label free_roam_yuuhi:
    $ all_options = True
    $ yuuhi_sex_tab_regular = False
    scene irda_blacksmith with Fade(1.0,1.0,1.0)
    play music "yuuhi.mp3" fadein 2.0 loop
    ""
    if update0_3_1_tasks_armor_fin and not update0_3_1_tasks_armor_fin_talk:
        $ update0_3_1_tasks_armor_fin_talk = True
        $ free_roam_yuuhi_first = False
        scene 31_s19 with dissolve
        yuuhi "[mc]! How are you?"
        yuuhi "Does it still hurt?"
        scene 31_s20 with dissolve
        mc "I'm fine. But thanks for asking."
        scene 31_s19 with dissolve
        yuuhi "I'm really sorry... I didn't know that he would go all out like that..."
        scene 31_s20 with dissolve
        mc "It's all good. I'm glad you got to test it out. You seemed really fond of that club."
        scene 31_s1 with dissolve
        yuuhi "Thank you, [mc]. You're so strong~"
        scene 31_s2 with dissolve
        if mc_has_strawberries and not mc_refused_strawberries_yuuhi:
            mc "(Maia asked for these straberries, but I can give them to Yuuhi instead. She might love them. All girls love strawberries, right?)"
            call screen mc_has_strawberries_yuuhi
            $ mc_refused_strawberries_yuuhi = True
        call screen is_yuuhi with dissolve
    elif free_roam_yuuhi_first and mc_got_armor:
        scene 31_s1 with dissolve
        yuuhi "Welcome back, [mc]! I missed you."
        scene 31_s2 with dissolve
        mc "How are you doing, Yuuhi? Is that guy still bothering you?"
        scene 31_s1 with dissolve
        if mc_punch_orym:
            yuuhi "Haven't seen him since you kicked is ass!"
        else:
            yuuhi "Haven't seen him since. I think you scared him off."
        scene 31_s2 with dissolve
        mc "*laughs* Good."
        $ free_roam_yuuhi_first = False
        if mc_has_strawberries and not mc_refused_strawberries_yuuhi:
            mc "(I have the strawberries that Maia asked for, but I can give them to Yuuhi instead. She might love them. All girls love strawberries, right?)"
            call screen mc_has_strawberries_yuuhi
            $ mc_refused_strawberries_yuuhi = True
        call screen is_yuuhi with dissolve
    if mc_armor_timer == 2 and mc_armor_timer2:
        $ mc_armor_timer2 = False
        scene 31_s1 with dissolve
        if mc_harem_yuuhi:
            yuuhi "Hello, boyfriend! Hehe~"
        else:
            yuuhi "Hello, [mc]!"
        scene 31_s2 with dissolve
        mc "Hey, Yuuhi. What are you up to?"
        scene 31_s1 with dissolve
        yuuhi "Just hammering away, same as yesterday, same as tomorrow."
        scene 31_s2 with dissolve
        mc "Any strange customers lately?"
        scene 31_s1 with dissolve
        yuuhi "Strange? {i}Every{/i} adventurer that walks through that door is strange."
        scene 31_s2 with dissolve
        mc "Oh yeah?"
        scene 31_s17 with dissolve
        yuuhi "Half of them ask me for armor that'll make them invincible! Like I can just wave a hammer and—poof!—they're immortal."
        scene 31_s18 with dissolve
        mc "*laughs* Guess that means they really trust your work."
        scene 31_s15 with dissolve
        yuuhi "I suppose..."
        scene 31_s1 with dissolve
        yuuhi "Still, I can't complain. The crazier the adventurers, the better the business."
        scene 31_s2 with dissolve
        if mc_has_strawberries and not mc_refused_strawberries_yuuhi:
            mc "(I have the strawberries that Maia asked for, but I can give them to Yuuhi instead. She might love them. All girls love strawberries, right?)"
            call screen mc_has_strawberries_yuuhi
            $ mc_refused_strawberries_yuuhi = True
        call screen is_yuuhi with dissolve
    if mc_armor_timer == 1 and mc_armor_timer1:
        $ mc_armor_timer1 = False
        scene 31_s1 with dissolve
        yuuhi "[mc]! Good news—I think I can finish your armor tomorrow!"
        yuuhi "Excited?"
        scene 31_s2 with dissolve
        mc "I am. Not so much for what comes after, though."
        scene 31_s19 with dissolve
        yuuhi "The witch..."
        scene 31_s20 with dissolve
        mc "Yeah."
        scene 31_s1 with dissolve
        yuuhi "Don't worry, [mc]. My armor will give you decent protection against attack magic. Fireballs, lightning strikes, that sort of thing."
        scene 31_s2 with dissolve
        mc "Decent protection?"
        scene 31_s1 with dissolve
        yuuhi "Sorry. I make armor, not miracles. It won't block everything, but it'll keep you alive."
        scene 31_s2 with dissolve
        mc "Alive's good enough, I guess. What about other kinds of magic?"
        scene 31_s1 with dissolve
        yuuhi "...Not great. If she messes with your mind, or curses you, the armor can't really help with that."
        scene 31_s2 with dissolve
        mc "Comforting."
        scene 31_s17 with dissolve
        yuuhi "Hey! It's the best I can do..."
        scene 31_s18 with dissolve
        mc "I know, I know. Didn't mean to say it like that."
        yuuhi "Hmph!"
        if mc_has_strawberries and not mc_refused_strawberries_yuuhi:
            mc "(I have the strawberries that Maia asked for, but I can give them to Yuuhi instead. She might love them. All girls love strawberries, right?)"
            call screen mc_has_strawberries_yuuhi
            $ mc_refused_strawberries_yuuhi = True
        call screen is_yuuhi with dissolve
    else:
        scene 31_s1 with dissolve
        if speech_cycle == 0:
            if mc_harem_yuuhi:
                yuuhi "Welcome back, [mc]! *winks*"
            else:
                yuuhi "Welcome back, [mc]!"
        elif speech_cycle == 1:
            yuuhi "Do you like dogs, [mc]? I have always wanted one as a pet."
        elif speech_cycle == 2:
            yuuhi "Are you more of a winter or summer person, [mc]? I love winter—mostly because I get to stay in and be lazy all day, hehe~"
        elif speech_cycle == 3:
            yuuhi "Ugh, I'm {i}sooo{/i} bored, [mc]... Maybe I should grab a deck of cards and we can play something?"
        elif speech_cycle == 4:
            yuuhi "Is it just me, or are you getting more muscular by the day?"
        elif speech_cycle == 5:
            if mc_harem_yuuhi:
                yuuhi "What kind of house do you think we'll have? I know your situation isn't great, [mc], so I wouldn't mind staying at my Pops's place for a while."
            else:
                yuuhi "Hello, [mc]! The weather's great today."
        elif speech_cycle == 6:
            yuuhi "Not a single sale yesterday... I don't really mind slacking off, honestly, but my Pops? Yeah, he's not gonna be happy about it."
        elif speech_cycle == 7:
            if mc_harem_yuuhi:
                yuuhi "Are they making you do dangerous jobs at the guild, [mc]? Please take care of yourself... I don't know what I'd do if something happened to you."
            else:
                yuuhi "Are they making you do dangerous jobs at the guild, [mc]? Please take care of yourself. I don't want to lose a customer."
        elif speech_cycle == 8:
            yuuhi "{i}It is I, gaze upon me and kneel.{/i} That's what Gavlan the Archer said when his cavalry reclaimed the Highwall from the Nahrayan forces. Are you any good with history, [mc]? I only seem to remember the cool parts."
        elif speech_cycle == 9:
            yuuhi "Do you think I'd make a good adventurer? I mean, I can sew my own clothes and I can run pretty fast! ...Okay, maybe not."
        elif speech_cycle == 10:
            yuuhi "I think I might have made my Pops mad... again. But in my defense, who even needs that many pairs of tongs?!"
        
        scene 31_s2 with dissolve
        if mc_has_strawberries and not mc_refused_strawberries_yuuhi:
            mc "(I have the strawberries that Maia asked for, but I can just give them to Yuuhi instead. She might love them. All girls love strawberries, right?)"
            call screen mc_has_strawberries
            $ mc_refused_strawberries_yuuhi = True
        call screen is_yuuhi with dissolve

default yuuhi_asex_times = 1
label yuuhi_sex_end:
    play music "yuuhi.mp3" fadein 3.0 loop
    if not yuuhi_harem_training_finished:
        if yuuhi_harem_training_hj_second:
            scene 31_s13 with Fade(0.5,0.5,0.5) 
            yuuhi "How was that? The softest hands in Irda~"
            scene 31_s14 with dissolve
        elif yuuhi_harem_training_bj_first:
            scene 31_s13 with Fade(0.5,0.5,0.5) 
            yuuhi "I think I'm slowly getting the hang of this... Will you come train me again soon?"
            scene 31_s14 with dissolve
        elif yuuhi_harem_training_bj_second:
            scene 31_s16 with Fade(0.5,0.5,0.5) 
            yuuhi "..."
            mc "Yuuhi?"
            scene 31_s15 with dissolve
            yuuhi "I'm fine!"
            scene 31_s16 with dissolve
            impulse "Her womb's begging to be colonized."
        elif yuuhi_harem_training_asex_first:
            scene 31_s13 with Fade(0.5,0.5,0.5) 
            yuuhi "Sorry for running off like that... again. You really know how to make me embarrassed."
            scene 31_s14 with dissolve
            mc "{i}I'm{/i} embarrassing you? You've got a knack for doing that to yourself, you know."
            yuuhi "..."
        elif not yuuhi_harem_training_asex_first:
            scene 31_s1 with Fade(0.5,0.5,0.5) 
            yuuhi "[mc]... Can you keep coming over? I... can't get enough of you~"
            scene 31_s2 with dissolve
            $ yuuhi_harem_training_finished = True
    else:
        if yuuhi_hj:
            scene 31_s7 with dissolve
            $ yuuhi_hj = False
            yuuhi "My hand smells like you now... Did you enjoy my handy, [mc]?"
            scene 31_s8 with dissolve
        elif yuuhi_bj:
            scene 31_s7 with dissolve
            $ yuuhi_bj = False
            yuuhi "*cough* Sorry, I just had something really big in my throat recently~"
            scene 31_s8 with dissolve
        elif yuuhi_asex:
            if yuuhi_asex_times == 1:
                scene 31_s7 with dissolve
                yuuhi "My butt is sore because of you, [mc]~"
                scene 31_s8 with dissolve
            elif yuuhi_asex_times == 2:
                scene 31_s7 with dissolve
                yuuhi "You must really like the feeling of my butt, [mc]~"
                scene 31_s8 with dissolve
            elif yuuhi_asex_times == 3:
                scene 31_s15 with dissolve
                yuuhi "[mc]... All this anal sex is starting to {i}really{/i} take a toll on my butt..."
                scene 31_s16 with dissolve
            else:
                scene 31_s15 with dissolve
                yuuhi "M-Maybe we should try something else now? I can barely stand, [mc]..."
                scene 31_s16 with dissolve
            $ yuuhi_asex_times += 1
            $ yuuhi_asex = False
        elif yuuhi_fj:
            scene 31_s7 with dissolve
            $ yuuhi_fj = False
            yuuhi "My toes feel sticky now... I hope you had fun, [mc]~"
            scene 31_s8 with dissolve
    call screen is_yuuhi with dissolve

default diana_in_scene64_talk = False
label free_roam_diana:
    $ all_options = True
    $ diana_sex_tab_regular = False
    scene irda_brothel with Fade(1.0,1.0,1.0)
    play music "diana.mp3" fadein 2.0 loop
    ""
    if mc_harem_diana_chance and mc_visit_diana >= 3:
        jump diana_harem_chance
    if in_scene64 and not diana_in_scene64_talk:
        $ diana_in_scene64_talk = True
        $ is_diana_first_time_talk = False
        if mc_harem_diana:
            scene 7_s26 with dissolve
            di "[mc]! Oh, gods... you're back! You're actually here!"
            scene 7_s27 with dissolve
            mc "Diana? Whoa, what's wrong? What happened?"
            scene 7_s52 with dissolve
            di "You idiot! Where in the seven hells have you been?! Do you have any idea how long it's been? I thought—!"
            scene 7_s51 with dissolve
            mc "...I'm sorry. I was on another mission by the queen."
            scene 7_s26 with dissolve
            di "*sigh* I-I'm sorry... I should have known it was something like that. I just... my nerves got the better of me. It's not easy, you know? Waiting."
            scene 7_s27 with dissolve
            mc "*chuckles* You were really that worried about me? You really do care, huh?"
            scene 7_s52 with dissolve
            di "What kind of question is that? Of course I care, you bastard! You're my lover, dammit!"
            scene 7_s51 with dissolve
            mc "I know, I know. You're right. I'm sorry for vanishing. I'll try to tell you in advance next time."
            scene 7_s26 with dissolve
            di "It's fine... I suppose it's part of your work."
            scene 7_s27 with dissolve
            mc "I love you, Diana."
            scene 7_s26 with dissolve
            di "[mc]..."
            scene 7_s24 with dissolve
            di "I love you too~"
            di "I'm so glad you're back, honey."
            scene 7_s25 with dissolve
        else:
            scene 7_s22 with dissolve
            di "There you are~ Couldn't resist my charm, could you?"
            scene 7_s23 with dissolve
            mc "Hey, Diana. It's been a while."
            scene 7_s22 with dissolve
            di "Where've you been, if you don't mind me asking?"
            scene 7_s23 with dissolve
            mc "It's a long story. But basically... I helped retrieve a noble's daughter who turned out to be royalty from Eurina."
            scene 7_s22 with dissolve
            di "Well, isn't that something. You started out a nobody, and now you've got leverage over some pretty powerful people."
            scene 7_s23 with dissolve
            mc "...Wait. How do you know where I came from? I never told you."
            scene 7_s24 with dissolve
            di "Sweetheart, it's our job to collect whispers and spread a little gossip now and then. Comes with the territory."
            scene 7_s25 with dissolve
            mc "Right..."
            scene 7_s22 with dissolve
            di "Anyway~ I'm glad you're back."
            scene 7_s23 with dissolve
        call screen is_diana with Dissolve(0.5)
    if is_diana_first_time_talk:
        scene 7_s22 with dissolve
        di "Oh? Look who's back~"
        scene 7_s23 with dissolve
        mc "Hey. Anything new around here?"
        scene 7_s22 with dissolve
        di "Same old, same old. But what I'm really curious about... is what brings our brave hero back here."
        scene 7_s23 with dissolve
        mc "Uh... Well—"
        scene 7_s22 with dissolve
        di "Come on, sweetpea. There's only one reason a man walks into a brothel."
        scene 7_s23 with dissolve
        mc "What if I only wanted a drink?"
        scene 7_s22 with dissolve
        di "Then you visit a tavern."
        scene 7_s23 with dissolve
        mc "..."
        scene 7_s22 with dissolve
        di "No need to play shy, darling."
        di "I'm always here if you make up your mind~"
        scene 7_s25 with dissolve
        $ is_diana_first_time_talk = False
        call screen is_diana with Dissolve(0.5)
    else:
        scene 7_s22 with dissolve
        if speech_cycle == 0:
            if mc_harem_diana:
                di "How may I service my lover today? *psst* {size=30}It's free if you don't have any coin~{/size}"
            else:
                di "How may I service our brave hero today?"
        elif speech_cycle == 1:
            di "I hope you didn't forget about me, [mc]~ A woman like me needs constant attention, you know." 
        elif speech_cycle == 2:
            di "Mmm, you look tense... Should I help you relax, or would you rather {i}tire{/i} yourself out first?"
        elif speech_cycle == 3:
            di "What wicked thing is going through your mind right now, [mc]?"  
        elif speech_cycle == 4:
            di "Are you here for business, pleasure, or both?" 
        elif speech_cycle == 5:
            di "I had a dream about you last night, [mc]... Should I tell you about it, or would you rather {i}act{/i} it out?"
        elif speech_cycle == 6:
            di "There you are, I was wondering where you went."
        elif speech_cycle == 7:
            di "Did you sleep well yesterday, [mc]?" 
        elif speech_cycle == 8:
            di "Welcome back, [mc]~"  
        scene 7_s23 with dissolve
        call screen is_diana with dissolve

default diana_tj = False
default diana_bj = False
default diana_vsex = False
default diana_asex = False

label diana_sex_end:
    if diana_game_start_end:
        $ diana_game_start_end = False
        scene 7_s30 with Fade(0.5,0.5,0.5)
        di "Thank you for yesterday, [mc]... I slept like a log in your arms."
        scene 7_s31 with dissolve
        mc "*chuckles* Happy to help. See you, Diana."
        scene 7_s29 with dissolve
        di "Wait..."
        scene 7_s28 with dissolve
        mc "Hmm?"
        scene 7_s26 with dissolve
        di "Will you... come back soon?"
        scene 7_s27 with dissolve
        mc "I will."
        scene black with Fade(1.0,1.0,1.0)
        $ diana_sex_tab_regular = False
        $ all_options = True
        jump free_roam_main_label
    if in_scene05:
        jump after_diana_sex
    else:
        scene 7_s22 with Fade(0.5,0.5,0.5)
        if diana_tj:
            $ diana_tj = False
            di "My tits are yours to use whenever, come back soon, baby~"
        elif diana_bj:
            $ diana_bj = False
            di "Did you enjoy using my mouth? I can still taste your cock~"
        elif diana_vsex:
            $ diana_vsex = False
            if diana_pregnant:
                di "I'll be counting on you, [mc]. Our child needs a father figure, so no running away!"
                scene 7_s23 with dissolve
                mc "Why do you have so little trust in me?"
                scene 7_s29 with dissolve
                di "N-No... I didn't mean it that way. It's just that my father... forget it. Just please don't leave me."
                di "Please..."
                scene 7_s28 with dissolve
                call screen is_diana with dissolve
            else:
                di "You came {i}so{/i} hard, I'm willing to bet that cock will remember how my pussy feels for a long time~"
        elif diana_asex:
            $ diana_asex = False
            di "My ass will be gaping for a while thanks to your cock. I would be lying if I said I didn't enjoy though~"
        scene 7_s23 with dissolve
        call screen is_diana with dissolve


default free_roam_reb_first = True
label free_roam_reb:
    if free_roam_reb_first:
        jump free_roam_reb_first
    elif not mc_friend_reb:
        scene irda_roof with Fade(0.5,0.5,0.5)
        play music "wind.mp3" fadein 2.0 loop
        ""
        scene 35_s22 with dissolve
        r "What? I told you I'll take care of it. Now leave."
        scene 35_s21 with dissolve
        call screen scene35_choice02 with dissolve
    elif not mc_reb_first_talk_:
        jump free_roam_reb_first
    elif mc_roam_reb_break:
        mc "(I should leave her alone for now. I'll talk to her some other time.)"
        call screen free_roam_choices with dissolve
    elif mc_rejected_reb_friend_date:
        mc "(I refused to marry Rebecca. I don't think she would appreciate me stroming into her room all of a sudden.)"
        call screen free_roam_choices with dissolve
    else:
        jump free_roam_reb_main

default reb_speech_cycle = 0
default mc_rejected_reb_first_talk = False
label free_roam_reb_main:
    play music "reb.mp3" fadein 3.0 loop
    $ reb_sex_tab_regular = False
    $ all_options = True
    if mc_rejected_reb_first and not mc_rejected_reb_first_talk:
        $ mc_rejected_reb_first_talk = True
        scene 63_s4 with Fade(1.0,1.0,1.0)
        r "Hmph!"
        mc "What's wrong?"
        scene 63_s3 with dissolve
        r "You left me... I slept on my own!"
        scene 63_s4 with dissolve
        mc "I'm sorry but like I said, we were drunk. Remember?"
        scene 63_s3 with dissolve
        r "S-Still..."
        scene 63_s4 with dissolve
        mc "Oh? Now you want me to sleep on your bed? You made me sleep on the couch last time."
        scene 63_s3 with dissolve
        r "Look. I really regretted that afterwards, alright? You looked really uncomfortable there..."
        r "I'm sorry."
        scene 63_s4 with dissolve
        mc "Apology accepted."
        scene 63_s3 with dissolve
        r "Whatever... Just don't leave me out like that again."
        scene 63_s4 with dissolve
        call screen is_reb with dissolve
    scene 63_s1 with Fade(1.0,1.0,1.0) 
    if reb_speech_cycle == 0:
        r "Morning, [mc]. Don't you have work to do?"
    elif reb_speech_cycle == 1:
        r "Good morning, husband~ Or should I say... my favorite headache."
    elif reb_speech_cycle == 2:
        r "Hello, [mc]. Came to annoy me again?" 
    elif reb_speech_cycle == 3:
        r "*yawn* I barely caught any sleep yesterday from all the food I ate..."
    elif reb_speech_cycle == 4:
        r "Good morning, husband. Still surprised you get to call me yours?"
    elif reb_speech_cycle == 5:
        r "I was thinking... do I need a reason to buy you a gift, or can I spoil you just because?"
    elif reb_speech_cycle == 6:
        r "Morning, [mx]. You snore. Loudly. But I guess I'm getting used to it."
    elif reb_speech_cycle == 7:
        r "Oh, look who's finally awake. Did I tire you out that much yesterday?"
    elif reb_speech_cycle == 8:
        r "You were mumbling in your sleep again. Something about 'conquering the world'... Should I be worried? Just joking..."  
    elif reb_speech_cycle == 9:
        r "Next time, I want to take you to the river. No guards, no lectures, just... you and me."
    elif reb_speech_cycle == 10:
        r "Sometimes, when I see you, my heart beats so fast... I wonder if you notice."
    elif reb_speech_cycle == 11:
        r "[mc]! I saw a spider crawling across my book this morning. I considered burning the entire room."
    elif reb_speech_cycle == 12:
        r "Good morning, husband. That's right, I called you that. Don't start blushing on me now~" 

    scene 63_s2 with dissolve
    call screen is_reb with dissolve


label reb_sex_end:
    play music "reb.mp3" fadein 3.0 loop
    scene 63_s1 with Fade(0.5,0.5,0.5)
    if reb_hj:
        $ reb_hj = False
        r "You ejaculated so much... I only used my hand, you know? I wonder how much would you release if you used my... Nevermind."
    elif reb_tj:
        $ reb_tj = False
        r "My breasts feel so sweaty after that... you really like them, [mx]~"
    elif reb_bj:
        $ reb_bj = False
        r "Did my mouth feel good, [mx]? You can use it whenever to feed me your delicious semen~"
    elif reb_sex:
        $ reb_sex = False
        r "You ejaculated so much, [mx]... I can still feel some of it inside me~"
    elif reb_fj:
        $ reb_fj = False
        r "I can't believe you wanted me to do that... You seem enjoy my feet a lot. What a weirdo~"
    scene 63_s2 with dissolve
    call screen is_reb with dissolve

label free_roam_before_sleep:
    play music "gameplay_night.mp3" fadein 2.0 loop
    scene 29_1_s52 with Fade(1.0,1.0,1.0)
    call screen scene_maia_sleep1 with dissolve

default speech_cycle = 0
label free_roam_sleep:
    $ days_passed += 1
    $ mc_masturbated = False
    $ yuuhi_asex_times = 1
    if mc_harem_yuuhi:
        if not yuuhi_harem_training_finished:
            $ yuuhi_sex_times = 2
        elif yuuhi_harem_training_finished:
            $ yuuhi_sex_times = 6
    
    if maia_pregnant:
        $ maia_pregnancy_timer += 1
    if diana_pregnant:
        $ diana_pregnancy_timer += 1
    if yuuhi_pregnant:
        $ yuuhi_pregnancy_timer += 1
    
    if cycle >= 3:
        $ cycle = random.randint(0, 3)
    else:
        $ cycle += 1

    $ speech_cycle += 1

    if in_scene29:
        jump scene30
    elif in_scene30:
        if not mc_armor_timer == 0:
            $ mc_armor_timer -= 1
        jump free_roam_main_label
    elif in_scene34:
        jump scene35
    elif in_scene35_2:
        if not in_scene35_2 == 0:
            $ in_scene35_2_timer -= 1
        jump free_roam_main_label

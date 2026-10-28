init python:
    import random

init:
    $ renpy.music.register_channel("music1", "music", loop=True)
    $ renpy.music.register_channel("music2", "music", loop=True)
    $ renpy.music.register_channel("music3", "music", loop=True)
    $ renpy.music.register_channel("music4", "music", loop=True)
label irda_bedroom:
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music3"
    stop music fadeout 2.0 channel "music4"
    if time_of_day == "morning":
        if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
            play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    else:
        if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
            play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    
    $ maia_sex_tab_regular = False
    $ maia_sex_tab_slave = False
    $ maia_sex_tab_clothes = False
    $ map_screen_open = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_blacksmith = False
    $ in_guild = False
    $ in_brothel = False

    if time_of_day == "morning":
        if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
            # Pregnant versions
            if is_maia_wearing_all == False:
                if cycle == 0 or cycle == 3:
                    scene irda_bedroom_rall_preg with dissolve
                elif cycle == 1:
                    scene irda_bedroom2_rall_preg with dissolve
                elif cycle == 2:
                    scene irda_bedroom3_rall_preg with dissolve
            elif is_maia_wearing_top:
                if cycle == 0 or cycle == 3:
                    scene irda_bedroom_preg with dissolve
                elif cycle == 1:
                    scene irda_bedroom2_preg with dissolve
                elif cycle == 2:
                    scene irda_bedroom3_preg with dissolve
            else:
                if cycle == 0 or cycle == 3:
                    scene irda_bedroom_rtop_preg with dissolve
                elif cycle == 1:
                    scene irda_bedroom2_rtop_preg with dissolve
                elif cycle == 2:
                    scene irda_bedroom3_rtop_preg with dissolve
        else:
            # Non-pregnant versions
            if is_maia_wearing_all == False:
                if cycle == 0:
                    scene irda_bedroom_rall with dissolve
                elif cycle == 1:
                    scene irda_bedroom2_rall with dissolve
                elif cycle == 2:
                    scene irda_bedroom3_rall with dissolve
                elif cycle == 3:
                    scene irda_bedroom4_rall with dissolve
            elif is_maia_wearing_top:
                if cycle == 0:
                    scene irda_bedroom with dissolve
                elif cycle == 1:
                    scene irda_bedroom2 with dissolve
                elif cycle == 2:
                    scene irda_bedroom3 with dissolve
                elif cycle == 3:
                    scene irda_bedroom4 with dissolve
            else:
                if cycle == 0:
                    scene irda_bedroom_rtop with dissolve
                elif cycle == 1:
                    scene irda_bedroom2_rtop with dissolve
                elif cycle == 2:
                    scene irda_bedroom3_rtop with dissolve
                elif cycle == 3:
                    scene irda_bedroom4_rtop with dissolve
                
    elif time_of_day == "night":
        if cycle == 0:
            scene irda_bedroom_night1 with dissolve
        elif cycle == 1:
            scene irda_bedroom_night2 with dissolve
        elif cycle == 2:
            scene irda_bedroom_night3 with dissolve
        elif cycle == 3:
            scene irda_bedroom_night1 with dissolve
    
    if diana_pregnant: 
        if diana_pregnancy_timer == pregnancy_time: 
            $ diana_pregnant = False 
            $ is_diana_gave_birth = True
            $ diana_births += 1
            $ total_births += 1
            $ diana_pregnancy_timer = 0 
            jump diana_birth_scene

    if maia_pregnant: 
        if maia_pregnancy_timer == pregnancy_time: 
            $ maia_pregnant = False 
            $ is_maia_gave_birth = True
            $ maia_births += 1
            $ total_births += 1
            $ maia_pregnancy_timer = 0 
            jump maia_birth_scene

    call screen gameplay with dissolve
       

label irda_throne:
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music3"
    stop music fadeout 2.0 channel "music4"
    if time_of_day == "morning":
        if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
            play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    else:
        if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
            play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_blacksmith = False
    $ in_guild = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_throne with dissolve
    elif time_of_day == "night":    
        scene irda_throne_night with dissolve
    call screen gameplay with dissolve

label irda_kitchen:
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music3"
    stop music fadeout 2.0 channel "music4"
    if time_of_day == "morning":
        if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
            play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    else:
        if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
            play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_roof = False
    $ in_blacksmith = False
    $ in_guild = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_kitchen with dissolve
    elif time_of_day == "night":    
        scene irda_kitchen_night with dissolve
    call screen gameplay with dissolve

label irda_roof:
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music3"
    stop music fadeout 2.0 channel "music4"
    if time_of_day == "morning":
        if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
            play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    else:
        if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
            play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_blacksmith = False
    $ in_guild = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_roof with dissolve
    elif time_of_day == "night":
        play music "roof_night.mp3" fadein 2.0 volume 0.1 loop    
        scene irda_roof_night with dissolve
    call screen gameplay with dissolve

label irda_blacksmith:
    $ all_options = True
    $ yuuhi_sex_tab_regular = False
    stop music fadeout 2.0 channel "music1"
    stop music fadeout 2.0 channel "music3"
    stop music fadeout 2.0 channel "music4"
    if renpy.music.get_playing(channel='music2') != "yuuhi.mp3":
        play music "yuuhi.mp3" fadein 2.0 volume 0.1 loop channel "music2"
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_guild = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_blacksmith with dissolve
    elif time_of_day == "night":
        scene irda_blacksmith_night with dissolve
    call screen gameplay with dissolve

label irda_guild:
    stop music fadeout 2.0 channel "music1"
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music4"
    if renpy.music.get_playing(channel='music3') != "guild.mp3":
        play music "guild.mp3" fadein 2.0 volume 0.1 loop channel "music3"
        
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_blacksmith = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_guild with dissolve
    elif time_of_day == "night":
        scene irda_guild_night with dissolve
    call screen gameplay with dissolve

label irda_brothel:
    $ all_options = True
    $ diana_sex_tab = False
    $ diana_sex_tab_regular = False
    $ diana_sex_tab_clothing = False
    stop music fadeout 2.0 channel "music1"
    stop music fadeout 2.0 channel "music2"
    stop music fadeout 2.0 channel "music3"
    if renpy.music.get_playing(channel='music4') != "diana.mp3":
        play music "diana.mp3" fadein 2.0 volume 0.1 loop channel "music4"
    
    #if renpy.music.get_playing(channel='music3') != "guild.mp3":
        #play music "guild.mp3" fadein 2.0 volume 0.1 loop channel "music3"
        
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_blacksmith = False
    $ in_guild = False
    $ in_brothel = True
    if time_of_day == "morning":
        if diana_pregnant and diana_pregnancy_timer >= pregnancy_time // 2:
            # Pregnant versions
            if is_diana_wearing_all == False:
                scene irda_brothel_rall_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_rall_preg_cum with dissolve
            elif is_diana_wearing_top:
                scene irda_brothel_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_preg_cum with dissolve
            else:
                scene irda_brothel_rtop_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_rtop_preg_cum with dissolve
        else:
            # Non-pregnant versions
            if is_diana_wearing_all == False:
                scene irda_brothel_rall with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_rall_cum with dissolve
            elif is_diana_wearing_top:
                scene irda_brothel with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_cum with dissolve
            else:
                scene irda_brothel_rtop with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_rtop_cum with dissolve

    elif time_of_day == "night":
        if diana_pregnant and diana_pregnancy_timer >= pregnancy_time // 2:
            # Pregnant versions
            if is_diana_wearing_all == False:
                scene irda_brothel_night_rall_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_rall_preg_cum with dissolve
            elif is_diana_wearing_top:
                scene irda_brothel_night_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_preg_cum with dissolve
            else:
                scene irda_brothel_night_rtop_preg with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_rtop_preg_cum with dissolve
        else:
            # Non-pregnant versions
            if is_diana_wearing_all == False:
                scene irda_brothel_night_rall with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_rall_cum with dissolve
            elif is_diana_wearing_top:
                scene irda_brothel_night with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_cum with dissolve
            else:
                scene irda_brothel_night_rtop with dissolve
                if is_diana_face_cum:
                    scene irda_brothel_night_rtop_cum with dissolve
    call screen gameplay with dissolve

label irda_barn:
    $ map_screen_open = False
    $ in_bedroom = False
    $ in_throne = False
    $ in_kitchen = False
    $ in_roof = False
    $ in_guild = False
    $ in_blacksmith = False
    $ in_brothel = False
    if time_of_day == "morning":
        scene irda_barn with dissolve
    elif time_of_day == "night":
        scene irda_barn_night with dissolve
    call screen gameplay with dissolve

label maia_call:
    if time_of_day == "morning":
        if is_maia_gave_birth:
            show maia outfit natural1 with dissolve
            m "Oh... [mc]... I-It really happened... Our child is here..."
            show maia outfit sad1 with dissolve
            m "I-I was so scared... I thought I wouldn't make it through... but then I heard the baby cry, and..."
            show maia outfit natural1 with dissolve
            m "It's strange... My belly feels so empty now..."
            m "I-I know it's selfish, but... I miss the feeling of carrying your child..."
            m "D-Do you... w-want to try again? I... I'd love to feel you inside me again..."
            show maia outfit natural2 with dissolve
            mc "Already begging to be bred?"
            show maia outfit natural1 with dissolve
            m "I-I mean, only if you want to! I just... I really l-liked it..."
            show maia outfit natural2 with dissolve
            $ is_maia_gave_birth = False
            $ is_maia_gave_birth2 = True
            call screen is_maia with Dissolve(0.5)
        if is_maia_gave_birth2:
            show maia outfit natural1 with dissolve
            m "D-Don't worry about [baby_name]... The Queen's caretakers will look after them." 
            show maia outfit sad1 with dissolve
            if baby_gender == "male":
                m "I-I just hope he grows up strong... M-Maybe even like you..."
            else:
                m "I hope she has a good life... and maybe, someday, she'll understand everything..."
            show maia outfit sad2 with dissolve
            mc "What's gotton you sad all of a sudden?"
            show maia outfit sad1 with dissolve
            m "It's... They're not letting me see my baby..."
            show maia outfit sad2 with dissolve
            mc "Oh... Well, I'm sure they're taking good care of [baby_name] so don't worry."
            m "..."
            $ is_maia_gave_birth2 = False
            call screen is_maia with Dissolve(0.5)

        if maia_fear >= 70 or maia_love <= 30:
            show maia fear2 with dissolve
            m "..."
        elif maia_fear <= 50 and maia_love >= 70:
            if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
                show maia outfit natural1 with dissolve
                if cycle == 0:
                    m "I keep having these strange cravings..."
                elif cycle == 1:
                    m "I... I feel so heavy lately. It's strange... but I think I can feel our baby moving sometimes."
                elif cycle == 2:
                    m "Here... C-Can you feel it? It's your child... I-I mean, it's growing inside me, so it's only natural you'd want to, right?"
                elif cycle == 3:
                    m "My body is... changing. I, um, know that it's normal, but it's still embarrassing..." 
                show maia outfit natural2 with dissolve
            elif maia_pregnant:
                show maia outfit natural1 with dissolve
                if cycle == 0:
                    m "M-My chest feels so sore lately... I-Is that normal?"
                elif cycle == 1:
                    m "I keep feeling nauseous in the mornings... I-I don't regret anything! It's just... a little difficult..."
                elif cycle == 2:
                    m "Some of the Queen's slaves have been whispering about me lately... I-I hope they're not saying anything bad..."
                elif cycle == 3:
                    m "I keep catching myself rubbing my breasts when I'm alone... I-It's kind of comforting..."
                show maia outfit natural2 with dissolve
            else:
                show maia outfit natural1 with dissolve
                if cycle == 0:
                    m "Oh, [mx]! I missed you!"
                if cycle == 1:
                    m "Did I tell you how much I love you today, [mx]?"
                if cycle == 2:
                    m "Good morning, love!"
                if cycle == 3:
                    m "I'm writing a poem for you, [mx]!"
                show maia outfit natural2 with dissolve
        else:
            if maia_pregnant and maia_pregnancy_timer >= pregnancy_time // 2:
                show maia outfit natural1 with dissolve
                if cycle == 0:
                    m "I keep having these strange cravings..."
                elif cycle == 1:
                    m "I... I feel so heavy lately. It's strange... but I think I can feel our baby moving sometimes."
                elif cycle == 2:
                    m "Here... C-Can you feel it? It's your child... I-I mean, it's growing inside me, so it's only natural you'd want to, right?"
                elif cycle == 3:
                    m "My body is... changing. I, um, know that it's normal, but it's still embarrassing..." 
                show maia outfit natural2 with dissolve
            elif maia_pregnant:
                show maia outfit natural1 with dissolve
                if cycle == 0:
                    m "M-My chest feels so sore lately... I-Is that normal?"
                elif cycle == 1:
                    m "I keep feeling nauseous in the mornings... I-I don't regret anything! It's just... a little difficult..."
                elif cycle == 2:
                    m "Some of the Queen's slaves have been whispering about me lately... I-I hope they're not saying anything bad..."
                elif cycle == 3:
                    m "I keep catching myself rubbing my breasts when I'm alone... I-It's kind of comforting..."
                show maia outfit natural2 with dissolve
            else:
                show maia natural1 with dissolve
                if cycle == 0:
                    m "Yes, [mx]?"
                if cycle == 1:
                    m "What can I do for you, [mx]?"
                if cycle == 2:
                    m "Good morning, [mx]."
                if cycle == 3:
                    m "What are we doing today, [mx]?"
                show maia natural2 with dissolve
        call screen is_maia with Dissolve(0.5)
    else:
        scene m_sleep1_1 with fade
        mc "(She's sleeping.)"
        call screen scene_maia_sleep1 with dissolve


default maia_talk_choice1 = False
default maia_talk_choice2 = False
default maia_talk_choice3 = False
default maia_talk_choice4 = False
default maia_talk_choice5 = False

label is_maia_talk:
    if maia_talk_choice1:
        if maia_happy:
            if maia_love >= 70:
                mc "How are you doing?"
                scene 18_s8 with dissolve
                m "I'm always better when you're around me~"
                m "Please stay with me forever and ever and ever, [mx]~!"
                scene 18_s7 with dissolve
                call screen is_maia with dissolve
            else:
                mc "How are you doing?"
                scene 18_s8 with dissolve
                m "M-Me? I'm doing fine. Thank you for asking, [mx]~"
                scene 18_s7 with dissolve
                call screen is_maia with dissolve

        else:
            mc "How are you doing?"
            scene 18_s16 with dissolve
            m "I-I'm... I'm..."
            scene 18_s15 with dissolve
            mc "What is it?"
            scene 18_s16 with dissolve
            m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
            scene 18_s15 with dissolve
            call screen is_maia with dissolve

    elif maia_talk_choice2:
        if maia_happy:
            mc "Tell me about yourself. I'd like to know more about you."
            scene 18_s10 with dissolve
            m "Umm... I... M-My name is Maia..."
            scene 18_s9 with dissolve
            mc "I already know that much."
            scene 18_s10 with dissolve
            m "Oh! Then... I was born here in Irda a long time ago."
            scene 18_s9 with dissolve
            mc "Did you spend all your time here?"
            scene 18_s10 with dissolve
            m "Yes!"
            scene 18_s9 with dissolve
            mc "What else? I want to know how you got here."
            scene 18_s11 with dissolve
            m "Um... I don't... I don't... No..."
            scene 18_s12 with dissolve
            mc "Hey! Are you okay?!"
            mc "(Must be a tough subject for her. I shouldn't push her right now.)"
            mc "Alright, that's enough. You don't have to say anything if you don't want to."
            scene 18_s11 with dissolve
            m "T-Thank you."
            scene 18_s12 with dissolve
            "Maia doesn't fully trust you yet. Increase her trust by doing favorable actions towards her."
            call screen is_maia with dissolve
        else:
            mc "Tell me about yourself. I'd like to know more about you."
            scene 18_s16 with dissolve
            m "I'm... I'm, Maia."
            scene 18_s15 with dissolve
            mc "...And?"
            m "..."
            mc "Not in the mood to talk?"
            call screen is_maia with dissolve

    elif maia_talk_choice3:
        if maia_happy:
            if mc_friend_reb:
                mc "How are they treating you here? Is the princess still being kind to you?"
                scene 18_s13 with dissolve
                m "Yes, [mx]. She talks about you sometimes."
                scene 18_s14 with dissolve
                mc "R-Really? What does she say?"
                scene 18_s13 with dissolve
                m "T-That you're a pain in her... you know."
                scene 18_s7 with dissolve
                mc "Oh..."
                scene 18_s8 with dissolve
                m "But she also told me that she's starting to like you, [mx]."
                scene 18_s7 with dissolve
                mc "That's good to know."
            else:
                mc "How are they treating you here? Are they nice to you?"
                scene 18_s13 with dissolve
                m "O-Of course! Princess Rebecca... She always takes care of me."
                scene 18_s14 with dissolve
                mc "She's the last person I would've expected to do that."
                scene 18_s13 with dissolve
                m "She's very nice, master! You should talk to her."
                scene 18_s7 with dissolve
                mc "I'll try, I doubt she'll let me though."
            call screen is_maia with dissolve
        else:
            mc "How are they treating you here? Are they nice to you?"
            scene 18_s16 with dissolve
            m "Y-Yes..."
            scene 18_s15 with dissolve
            call screen is_maia with dissolve

    elif maia_talk_choice4:
        mc "What do you think about me? And be honest. I won't do anything to you."
        if mc_apologized_maia or mc_punished_maia_little:
            scene 18_s10 with dissolve
            m "Y-You're... sometimes cruel... but you apologized, so it's okay..."
            scene 18_s9 with dissolve
            mc "Oh, you're talking about the punishment? I hope you know I was just playing around. I never meant to harm you."
            scene 18_s8 with dissolve
            m "T-That's a relief, [mx]."
            scene 18_s7 with dissolve
            call screen is_maia with dissolve

        elif maia_love >= 70:
            scene 18_s13 with dissolve
            m "I... I really love you, [mx]!"
            scene 18_s14 with dissolve
            mc "*chuckles* I love you too."
            scene 18_s13 with dissolve
            m "You're the best ever! I-I'm so lucky to have someone so kind as my husband."
            scene 18_s14 with dissolve
            mc "Thank you."
            if mc_gave_strawberries_maia:
                scene 18_s13 with dissolve
                m "Umm... those strawberries you gave me were so delicious~"
                scene 18_s14 with dissolve
                mc "I guess I'll have to buy you more then."
                m "Hehe~"
            call screen is_maia with dissolve

        elif maia_love <= 40:
            if mc_didnt_accept_crumps and not in_scene18:
                scene 18_s16 with dissolve
                m "Y-You're... you're..."
                scene 18_s15 with dissolve
                mc "Come on, say it."
                scene 18_s16 with dissolve
                m "You're... cruel, [mx]... Y-you didn't let me keep Crumps when I asked you..."
                scene 18_s15 with dissolve
            else:
                scene 18_s16 with dissolve
                m "Y-You're... you're..."
                scene 18_s15 with dissolve
                mc "Come on, say it."
                scene 18_s16 with dissolve
                m "You're... cruel, [mx]... I hope y-you don't make me sad anymore..."
                scene 18_s15 with dissolve
            call screen is_maia with dissolve
        elif maia_love > 40:
            if not mc_didnt_accept_crumps:
                scene 18_s13 with dissolve
                m "Y-You're really kind, [mx]!"
                scene 18_s14 with dissolve
                mc "Am I?"
                scene 18_s13 with dissolve
                m "Yes, you are! I-I can feel it in my heart! You're a good person and you're always nice to me!"
                scene 18_s14 with dissolve
                mc "Thank you."
            else:
                scene 18_s13 with dissolve
                m "Y-You're really kind, [mx]!"
                scene 18_s14 with dissolve
                mc "Am I?"
                scene 18_s13 with dissolve
                m "Yes, you are! I-I can feel it in my heart! You're a good person."
                scene 18_s14 with dissolve
                mc "Thank you."
            call screen is_maia with dissolve

    elif maia_talk_choice5:
        call screen is_maia with dissolve

label is_maia_talk_pregnant:
    mc "How is your pregnancy going?"
    if maia_happy:
        if maia_pregnant:
            scene 18_s8 with dissolve
            if maia_pregnancy_timer <= 10:
                if maia_love >= 70:
                    m "I love you, [mx]!"
                    scene 18_s7 with dissolve
                    mc "Hmm? I love you too, but that wasn't what I asked."
                    scene 18_s8 with dissolve
                    m "M-Must be my hormones... they're making me mishear things..."
                    scene 18_s7 with dissolve
                    mc "*chuckles* You sly fox."
                else:
                    m "It's still too early. But thank you for asking, [mx]!"
            elif maia_pregnancy_timer <= 20:
                m "I feel a little dizzy sometimes and I'm starting to eat a lot of... weird things. Thank you for asking, [mx]."
            elif maia_pregnancy_timer <= 30:
                m "I can feel our child kicking sometimes, I think it will happen soon, [mx]! I'm so excited~"
            scene 18_s7 with dissolve
            call screen is_maia with dissolve
        else:
            scene 18_s8 with dissolve
            m "Hmm? I don't think I'm pregnant. Do you... want to make me pregnant, [mx]?"
            scene 18_s7 with dissolve
            call screen is_maia with dissolve
    else:
        scene 18_s16 with dissolve
        m "I'm not pregnant, [mx]."
        scene 18_s15 with dissolve
        call screen is_maia with dissolve

label is_reb_talk_pregnant:
    mc "How is your pregnancy going?"
    if reb_pregnant:
        ""
    else:
        scene 63_s3 with dissolve
        r "Pregnancy?!"
        scene 63_s4 with dissolve
        mc "I don't know why I said that..."
        scene 63_s3 with dissolve
        r "Do I look pregnant to you?!"
        scene 63_s4 with dissolve
        mc "Not at all. You look... healthy. Beautiful. Glowing, even."
        scene 63_s3 with dissolve
        r "...Idiot."
        scene 63_s4 with dissolve
    call screen is_reb with dissolve

label pregnancy_check_maia:
    if not maia_pregnant: 
        if persistent.super_sprem:
            $ maia_pregnant = True
            $ maia_pregnancy_timer = 0
            preg "Maia has a 100%% chance of getting pregnant..."
            preg "Success: Maia is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ maia_pregnant = True
                $ maia_pregnancy_timer = 0
                preg "Maia has a 25%% chance of getting pregnant..."
                preg "Success: Maia is now pregnant!"  
            else:
                preg "Maia has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_diana:
    if not diana_pregnant: 
        if persistent.super_sprem:
            $ diana_pregnant = True
            $ diana_pregnancy_timer = 0  
            preg "Diana has a 100%% chance of getting pregnant..."
            preg "Success: Diana is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ diana_pregnant = True
                $ diana_pregnancy_timer = 0  
                preg "Diana has a 25%% chance of getting pregnant..."
                preg "Success: Diana is now pregnant!"  
            else:
                preg "Diana has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_nadia:
    if not mc_nadia_pregnant: 
        if persistent.super_sprem:
            $ mc_nadia_pregnant = True
            preg "Nadia has a 100%% chance of getting pregnant..."
            preg "Success: Nadia is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ mc_nadia_pregnant = True
                preg "Nadia has a 25%% chance of getting pregnant..."
                preg "Success: Nadia is now pregnant!"  
            else:
                preg "Nadia has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_reb:
    if not reb_pregnant: 
        if persistent.super_sprem:
            $ reb_pregnant = True
            $ reb_pregnancy_timer = 0
            preg "Rebecca has a 100%% chance of getting pregnant..."
            preg "Success: Rebecca is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ reb_pregnant = True
                $ reb_pregnancy_timer = 0
                preg "Rebecca has a 25%% chance of getting pregnant..."
                preg "Success: Rebecca is now pregnant!"  
            else:
                preg "Rebecca has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_reham:
    if not reham_pregnant: 
        if persistent.super_sprem:
            $ reham_pregnant = True
            $ reham_pregnancy_timer = 0
            preg "Reham has a 100%% chance of getting pregnant..."
            preg "Success: Reham is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ reham_pregnant = True
                $ reham_pregnancy_timer = 0
                preg "Reham has a 25%% chance of getting pregnant..."
                preg "Success: Reham is now pregnant!"  
            else:
                preg "Reham has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_lena:
    if not lena_pregnant: 
        if persistent.super_sprem:
            $ lena_pregnant = True
            preg "Lena has a 100%% chance of getting pregnant..."
            preg "Success: Lena is now pregnant!" 
        else:
            if random.randint(1, 100) <= pregnancy_chance_lena:
                $ lena_pregnant = True
                preg "Lena has a 10%% chance of getting pregnant..."
                preg "Success: Lena is now pregnant!"  
            else:
                preg "Lena has a 10%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label pregnancy_check_jenny:
    if not jenny_pregnant: 
        if persistent.super_sprem:
            $ jenny_pregnant = True
            preg "Jenny has a 100%% chance of getting pregnant..."
            preg "Success: Jenny is now pregnant!"  
        else:
            if random.randint(1, 100) <= pregnancy_chance:
                $ jenny_pregnant = True
                preg "Jenny has a 25%% chance of getting pregnant..."
                preg "Success: Jenny is now pregnant!"  
            else:
                preg "Jenny has a 25%% chance of getting pregnant..."
                preg "Failed: Sorry, better luck next time!" 
    return

label maia_mc_rename:
    if maia_sad:
        $ mx = renpy.input("What should she call me? (default: Master)", length=32)
        $ mx = mx.strip()
            
        if mx == "":
            $ mx = "Master"
            
            # Capitalize the first letter and letters after a period '.'
        $ mx = '. '.join(sentence.capitalize() for sentence in mx.split('. '))
        m "..."
        call screen is_maia with dissolve

    else:
        $ mx = renpy.input("What should she call me? (default: Master)", length=32)
        $ mx = mx.strip()
            
        if mx == "":
            $ mx = "Master"
            
            # Capitalize the first letter and letters after a period '.'
        $ mx = '. '.join(sentence.capitalize() for sentence in mx.split('. '))
        scene 18_s8 with dissolve
        m "As you wish, [mx]."
        scene 18_s7 with dissolve
        call screen is_maia with dissolve


label queen_call:
    if quest1_queen_talkq_speakToDarius:
        show queen natural1 with dissolve
        q "Hero, speak with Darius once you're ready. He will guide you to the guild."
        show queen natural2 with dissolve
    elif quest2_noarmor:
        show queen natural1 with dissolve
        q "Hero, what's the news?"
        show queen natural2 with dissolve
        mc "I'm still waiting on my armor."
        mc "Thanks for that by the way."
        show queen natural1 with dissolve
        q "Think nothing of it. I expect a lot from you."
        show queen natural2 with dissolve
    else:
        show queen natural1 with dissolve
        q "Did you do what Eireen asked you of?"
        show queen natural2 with dissolve
    call screen is_queen with Dissolve(0.5)

label is_queen_talk:
    if queen_talk_choice1:
        #if queen_fear >= 70 or queen_love <= 30:
            #mc "How are you doing?"
            #m "I-I'm... I'm..."
            #mc "What is it?"
            #m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
            #call screen is_queen with dissolve
        #elif queen_fear <= 50 and queen_love >= 70:
            #mc "How are you doing?"
            #m "I'm doing wonderful, [mx]! Thank you for asking!"
            #call screen is_queen with dissolve
        #else:
        mc "How are you doing?"
        show queen natural1 with dissolve
        q "I'm doing well, hero. But tell me... shouldn't you be occupied with something more important right now?"
        show queen natural2 with dissolve
        call screen is_queen with dissolve
    elif queen_talk_choice2:
        #if queen_fear >= 70 or queen_love <= 30:
            #mc "Do you need something?"
            #m "N-no, I don't..."
            #call screen is_queen with dissolve
        #else:
        mc "Do you need something?"
        show queen happy1 with dissolve
        q "Not at the moment, no. Unless you count your unwavering loyalty, which I already have... Do I not?"
        show queen happy2 with dissolve
        call screen is_queen with dissolve
    elif queen_talk_choice3:
        #if queen_fear >= 70 or queen_love <= 30:
            #mc "Do you want to go on a date?"
            #m "..."
            #mc "I'll... I'll take that as a no."
            #call screen is_queen with dissolve
        #else:
        mc "Do you want to go on a date?"
        show queen happy1 with dissolve
        q "A date? How intriguing... Where would you take your Queen, brave hero?"
        show queen happy2 with dissolve
        mc "Uhh... Sorry, I didn't think this far ahead..."
        call screen is_queen with dissolve
    elif queen_talk_choice4:
        mc "How's your pregnancy?"
        #if queen_pregnant:
            #m "It's going fine, [mx]. I feel a bit more tired lately, and... I've been feeling hungrier..."
            #mc "That's normal. Be sure to eat well and get plenty of rest, okay?"
            #m "Yes, [mx]~ I will..."
            #call screen is_queen with dissolve
        #else:
        show queen shock1 with dissolve
        q "Pregnancy? I'm not pregnant..."
        q "Hold on... Could it be? No... No, that's impossible..."
        show queen shock2 with dissolve
        call screen is_queen with dissolve
    elif queen_talk_choice5:
        call screen is_queen with dissolve


default reb_first_talk = True
label reb_call:
    if reb_first_talk:
        show reb natural1 with dissolve
        r "You've got some nerve showing your face around me."
        show reb natural2 with dissolve
        mc "Hey, I think we got off on the wrong foot..."
        show reb natural1 with dissolve
        r "Fuck off."
        show reb natural2 with dissolve
        mc "Come on now, is that really the kind of language a princess should use?"
        show reb angry1 with dissolve
        r "Oh, I'm sorry! Should I be throwing flowers at your feet instead?"
        show reb angry2 with dissolve
        mc "Look, How about I do something for you. Prove my strength or my worth or whatever you want..."
        show reb smug1 with dissolve
        r "Oh, I've got something for you."
        show reb smug2 with dissolve
        mc "See! We can work this out."
        show reb smug1 with dissolve
        r "How about you march out there, find the biggest ogre you can, yank his dick off, and sit on it?"
        show reb smug2 with dissolve
        mc "..."
        show reb smug1 with dissolve
        r "Good luck."
        hide reb smug1 with dissolve
        $ reb_first_talk = False
        call screen gameplay with dissolve
    else:
        if quest1_queen_talkq_speakToDarius:
            show reb angry2 with dissolve
            r "..."
            hide reb angry2 with dissolve
            call screen gameplay with dissolve
        else:
            show reb natural1 with dissolve
            r "What?"
            show reb natural2 with dissolve
            mc "Can I not hang out here?"
            r "..."
            call screen is_reb with Dissolve(0.5)

label is_reb_talk:
    if reb_talk_choice1:
        mc "How are you doing?"
        scene 63_s1 with dissolve
        r "Fine. Why do you ask?"
        scene 63_s2 with dissolve
        mc "Just checking in on my favorite princess."
        scene 63_s3 with dissolve
        r "H-Huh?"
        scene 63_s4 with dissolve
        r "..."
        scene 63_s1 with dissolve
        r "Thanks..."
        scene 63_s2 with dissolve
        call screen is_reb with Dissolve(0.5)
    elif reb_talk_choice2:
        mc "Tell me about yourself. I'd like to know more."
        scene 63_s1 with dissolve
        r "It's boring. I promise."
        scene 63_s2 with dissolve
        mc "Try me."
        scene 63_s1 with dissolve
        r "Alright. I was raised inside stone walls, learned swordplay, court manners, and how to fake a smile before I was even allowed to ride a horse."
        scene 63_s2 with dissolve
        mc "Sounds strict."
        scene 63_s5 with dissolve
        r "It was. My mother wanted a strong woman. My father wanted a strong warrior."
        r "So I learned to act strong. Loud, sharp, untouchable. But sometimes I wonder what I'd be if I weren't born into this life."
        scene 63_s6 with dissolve
        mc "You'd still be you."
        scene 63_s5 with dissolve
        r "That's sweet. But I think I'd be a librarian. I'd open a tiny library out in the countryside... read all day, maybe fall asleep next to my husband."
        r "*sigh* But that's just a fantasy."
        scene 63_s6 with dissolve
        mc "It doesn't have to be. You don't have to carry all of that alone."
        mc "I'll help you from now on. You can rest by my side."
        scene 63_s4 with dissolve
        r "..."
        scene 63_s3 with dissolve
        r "...Stop saying things like that, idiot~"
        scene 63_s4 with dissolve
        call screen is_reb with dissolve
    elif reb_talk_choice3:
        
        ""

    elif reb_talk_choice4:
        mc "What do you think about me?"
        scene 63_s3 with dissolve
        r "Ugh... Do you enjoy asking questions you know will embarrass me?"
        scene 63_s4 with dissolve
        mc "Yes."
        scene 63_s3 with dissolve
        r "Fine... At first, I thought you were a parasite. Some opportunist looking for a way to climb."
        scene 63_s4 with dissolve
        mc "Ouch. I mean, you're not totally wrong..."
        scene 63_s5 with dissolve
        r "But then you surprised me. You aren't afraid to speak your mind. Even in front of my mother."
        scene 63_s6 with dissolve
        mc "So I'm... not a parasite anymore?"
        scene 63_s5 with dissolve
        r "You're still a pest. But a good one. Like a very charming cockroach."
        scene 63_s6 with dissolve
        mc "I'll take that as a compliment."
        scene 63_s3 with dissolve
        r "Don't. I'm already regretting saying anything nice."
        scene 63_s4 with dissolve
        call screen is_reb with dissolve

    elif reb_talk_choice5:
        call screen is_reb with dissolve


label is_reb_sex_first:
    $ is_reb_sex_first = False
    mc "Hey, Rebecca..."
    scene 63_s1 with dissolve
    r "Yes? You're not usually this shy."
    r "Ah, I see. You're frustrated, aren't you?"
    scene 63_s2 with dissolve
    mc "You got me. All this work lately is really getting to me."
    scene 63_s1 with dissolve
    r "Is that your excuse?"
    scene 63_s2 with dissolve
    mc "..."
    scene 63_s1 with dissolve
    r "You can't go inside me yet. She told you that, right?"
    scene 63_s2 with dissolve
    mc "I know. But love isn't just about that."
    scene 63_s1 with dissolve
    r "You mean like... jerking off?"
    scene 63_s2 with dissolve
    mc "Yes. And please stop calling it that..."
    mc "So? What do you say?"
    scene 63_s1 with dissolve
    r "Hmm... I'm torn. Should I make you beg first?"
    scene 63_s2 with dissolve
    mc "Please?"
    scene 63_s1 with dissolve
    r "*sigh* I suppose a wife should take care of her husband's needs."
    scene 63_s2 with dissolve
    $ all_options = False
    $ reb_sex_tab_regular = True
    call screen is_reb with dissolve

label ren_call:
    if quest3_ren_talkq_help:
        if time_of_day == "morning":
            show ren_natural1 with dissolve
            ren "Anything you need, [rx]?"
            show ren_natural2 with dissolve
            call screen is_ren with Dissolve(0.5)
        elif time_of_day == "night":
            scene ren_natural1_night with dissolve
            ren "You're up late, [rx]."
            scene ren_natural2_night with dissolve
            call screen is_ren with Dissolve(0.5)
    else:
        if time_of_day == "morning":
            show ren_natural1_ear with dissolve
            ren "Anything you need, [rx]?"
            show ren_natural2_ear  with dissolve
            call screen is_ren with Dissolve(0.5)
        elif time_of_day == "night":
            scene ren_natural1_night_ear  with dissolve
            ren "You're up late, [rx]."
            scene ren_natural2_night_ear  with dissolve
            call screen is_ren with Dissolve(0.5)

label is_ren_talk:
    if quest3_ren_talkq_help:
        if time_of_day == "morning":
            if ren_talk_choice1:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "How are you doing?"
                    #m "I-I'm... I'm..."
                    #mc "What is it?"
                    #m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
                    #call screen is_ren with dissolve
                #elif ren_fear <= 50 and ren_love >= 70:
                    #mc "How are you doing?"
                    #m "I'm doing wonderful, [mx]! Thank you for asking!"
                    #call screen is_ren with dissolve
                #else:
                mc "How are you doing?"
                scene ren_natural1_ear with dissolve
                ren "I'm doing well, [rx]. Thank you for asking. What about you? Are you eating well?"
                scene ren_natural2_ear with dissolve
                mc "Yup! Thanks to all the good food you've been making."
                scene ren_natural1_ear with dissolve
                ren "I'm glad to hear."
                scene ren_natural2_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice2:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you need something?"
                    #m "N-no, I don't..."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you need something?"
                scene ren_happy1_ear with dissolve
                ren "Hmm... Maybe a little rabbit? Haha, just kidding."
                scene ren_happy2_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice3:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you want to go on a date?"
                    #m "..."
                    #mc "I'll... I'll take that as a no."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you want to go on a date?"
                scene ren_sad1_ear with dissolve
                ren "A-a date? Oh, [rx]... I don't know..."
                scene ren_sad2_ear with dissolve
                mc "No pressure. Just thought I'd ask."
                scene ren_sad1_ear with dissolve
                ren "Besides, [rx]. I don't think... dating beastfolk would be good for your image."
                scene ren_sad2_ear with dissolve
                mc "Huh..."
                call screen is_ren with dissolve
            elif ren_talk_choice4:
                mc "How's your pregnancy?"
                #if ren_pregnant:
                    #m "It's going fine, [mx]. I feel a bit more tired lately, and... I've been feeling hungrier..."
                    #mc "That's normal. Be sure to eat well and get plenty of rest, okay?"
                    #m "Yes, [mx]~ I will..."
                    #call screen is_ren with dissolve
                #else:
                scene ren_sad3_ear with dissolve
                ren "My... pregnancy? [rx], I'm not pregnant..."
                scene ren_sad4_ear with dissolve
                mc "Oh, uh, right. My mistake. Haha..."
                scene ren_sad3_ear with dissolve
                ren "It's okay, [rx]. Just please don't go spreading any strange rumors about me."
                scene ren_sad4_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice5:
                call screen is_ren with dissolve
        elif time_of_day == "night":
            if ren_talk_choice1:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "How are you doing?"
                    #m "I-I'm... I'm..."
                    #mc "What is it?"
                    #m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
                    #call screen is_ren with dissolve
                #elif ren_fear <= 50 and ren_love >= 70:
                    #mc "How are you doing?"
                    #m "I'm doing wonderful, [mx]! Thank you for asking!"
                    #call screen is_ren with dissolve
                #else:
                mc "How are you doing?"
                scene ren_natural1_night_ear with dissolve
                ren "I'm doing well, [rx]. Thank you for asking. What about you? Are you eating well?"
                scene ren_natural2_night_ear with dissolve
                mc "Yup! Thanks to all the good food you've been making."
                scene ren_natural1_night_ear with dissolve
                ren "I'm glad to hear."
                scene ren_natural2_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice2:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you need something?"
                    #m "N-no, I don't..."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you need something?"
                scene ren_happy1_night_ear with dissolve
                ren "Hmm... Maybe a little rabbit? Haha, just kidding."
                scene ren_happy2_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice3:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you want to go on a date?"
                    #m "..."
                    #mc "I'll... I'll take that as a no."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you want to go on a date?"
                scene ren_sad1_night_ear with dissolve
                ren "A-a date? Oh, [rx]... I don't know..."
                scene ren_sad2_night_ear with dissolve
                mc "No pressure. Just thought I'd ask."
                scene ren_sad1_night_ear with dissolve
                ren "Besides, [rx]. I don't think... dating beastfolk would be good for your image."
                scene ren_sad2_night_ear with dissolve
                mc "Huh..."
                call screen is_ren with dissolve
            elif ren_talk_choice4:
                mc "How's your pregnancy?"
                #if ren_pregnant:
                    #m "It's going fine, [mx]. I feel a bit more tired lately, and... I've been feeling hungrier..."
                    #mc "That's normal. Be sure to eat well and get plenty of rest, okay?"
                    #m "Yes, [mx]~ I will..."
                    #call screen is_ren with dissolve
                #else:
                scene ren_sad3_night_ear with dissolve
                ren "My... pregnancy? [rx], I'm not pregnant..."
                scene ren_sad4_night_ear with dissolve
                mc "Oh, uh, right. My mistake. Haha..."
                scene ren_sad3_night_ear with dissolve
                ren "It's okay, [rx]. Just please don't go spreading any strange rumors about me."
                scene ren_sad4_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice5:
                call screen is_ren with dissolve
    else:
        if time_of_day == "morning":
            if ren_talk_choice1:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "How are you doing?"
                    #m "I-I'm... I'm..."
                    #mc "What is it?"
                    #m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
                    #call screen is_ren with dissolve
                #elif ren_fear <= 50 and ren_love >= 70:
                    #mc "How are you doing?"
                    #m "I'm doing wonderful, [mx]! Thank you for asking!"
                    #call screen is_ren with dissolve
                #else:
                mc "How are you doing?"
                scene ren_natural1_ear with dissolve
                ren "I'm doing well, [rx]. Thank you for asking. What about you? Are you eating well?"
                scene ren_natural2_ear with dissolve
                mc "Yup! Thanks to all the good food you've been making."
                scene ren_natural1_ear with dissolve
                ren "I'm glad to hear."
                scene ren_natural2_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice2:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you need something?"
                    #m "N-no, I don't..."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you need something?"
                scene ren_happy1_ear with dissolve
                ren "Hmm... Maybe a little rabbit? Haha, just kidding."
                scene ren_happy2_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice3:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you want to go on a date?"
                    #m "..."
                    #mc "I'll... I'll take that as a no."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you want to go on a date?"
                scene ren_sad1_ear with dissolve
                ren "A-a date? Oh, [rx]... I don't know..."
                scene ren_sad2_ear with dissolve
                mc "No pressure. Just thought I'd ask."
                scene ren_sad1_ear with dissolve
                ren "Besides, [rx]. I don't think... dating beastfolk would be good for your image."
                scene ren_sad2_ear with dissolve
                mc "Huh..."
                call screen is_ren with dissolve
            elif ren_talk_choice4:
                mc "How's your pregnancy?"
                #if ren_pregnant:
                    #m "It's going fine, [mx]. I feel a bit more tired lately, and... I've been feeling hungrier..."
                    #mc "That's normal. Be sure to eat well and get plenty of rest, okay?"
                    #m "Yes, [mx]~ I will..."
                    #call screen is_ren with dissolve
                #else:
                scene ren_sad3_ear with dissolve
                ren "My... pregnancy? [rx], I'm not pregnant..."
                scene ren_sad4_ear with dissolve
                mc "Oh, uh, right. My mistake. Haha..."
                scene ren_sad3_ear with dissolve
                ren "It's okay, [rx]. Just please don't go spreading any strange rumors about me."
                scene ren_sad4_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice5:
                call screen is_ren with dissolve
        elif time_of_day == "night":
            if ren_talk_choice1:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "How are you doing?"
                    #m "I-I'm... I'm..."
                    #mc "What is it?"
                    #m "I'm s-scared of you, [mx]... You're... You're not very kind to me... I... I don't know how to handle it."
                    #call screen is_ren with dissolve
                #elif ren_fear <= 50 and ren_love >= 70:
                    #mc "How are you doing?"
                    #m "I'm doing wonderful, [mx]! Thank you for asking!"
                    #call screen is_ren with dissolve
                #else:
                mc "How are you doing?"
                scene ren_natural1_night_ear with dissolve
                ren "I'm doing well, [rx]. Thank you for asking. What about you? Are you eating well?"
                scene ren_natural2_night_ear with dissolve
                mc "Yup! Thanks to all the good food you've been making."
                scene ren_natural1_night_ear with dissolve
                ren "I'm glad to hear."
                scene ren_natural2_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice2:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you need something?"
                    #m "N-no, I don't..."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you need something?"
                scene ren_happy1_night_ear with dissolve
                ren "Hmm... Maybe a little rabbit? Haha, just kidding."
                scene ren_happy2_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice3:
                #if ren_fear >= 70 or ren_love <= 30:
                    #mc "Do you want to go on a date?"
                    #m "..."
                    #mc "I'll... I'll take that as a no."
                    #call screen is_ren with dissolve
                #else:
                mc "Do you want to go on a date?"
                scene ren_sad1_night_ear with dissolve
                ren "A-a date? Oh, [rx]... I don't know..."
                scene ren_sad2_night_ear with dissolve
                mc "No pressure. Just thought I'd ask."
                scene ren_sad1_night_ear with dissolve
                ren "Besides, [rx]. I don't think... dating beastfolk would be good for your image."
                scene ren_sad2_night_ear with dissolve
                mc "Huh..."
                call screen is_ren with dissolve
            elif ren_talk_choice4:
                mc "How's your pregnancy?"
                #if ren_pregnant:
                    #m "It's going fine, [mx]. I feel a bit more tired lately, and... I've been feeling hungrier..."
                    #mc "That's normal. Be sure to eat well and get plenty of rest, okay?"
                    #m "Yes, [mx]~ I will..."
                    #call screen is_ren with dissolve
                #else:
                scene ren_sad3_night_ear with dissolve
                ren "My... pregnancy? [rx], I'm not pregnant..."
                scene ren_sad4_night_ear with dissolve
                mc "Oh, uh, right. My mistake. Haha..."
                scene ren_sad3_night_ear with dissolve
                ren "It's okay, [rx]. Just please don't go spreading any strange rumors about me."
                scene ren_sad4_night_ear with dissolve
                call screen is_ren with dissolve
            elif ren_talk_choice5:
                call screen is_ren with dissolve

default yuuhi_talk_choice1 = False
default yuuhi_talk_choice2 = False
default yuuhi_talk_choice3 = False
default yuuhi_talk_choice4 = False
default yuuhi_talk_choice5 = False
default yuuhi_talk_choice3_first = True
label yuuhi_call:
    if time_of_day == "morning":
        if yuuhi_harem:
            show yuuhi happy1 with dissolve
            if cycle == 0:
                yuuhi "I can't wait to get married to you... Please don't take too long, okay?"
            elif cycle == 1:
                yuuhi "Once we get married, I want you to... um... Never mind!"
            elif cycle == 2:
                yuuhi "Do you think you can beat my dad at arm wrestling? He's really strong!"
            elif cycle == 3:
                yuuhi "I get a strange feeling in my stomach every time I see you..."
            show yuuhi happy2 with dissolve
        else:
            show yuuhi natural1 with dissolve
            if cycle == 0:
                yuuhi "Hello, Sir. How can I help you?"
            elif cycle == 1:
                yuuhi "{i}*Humming softly...*{/i}"
                yuuhi "Oh! Sorry... I got lost in thought again, haha."
            elif cycle == 2:
                yuuhi "I'm still not sure if I want to follow my Pops's work... It just doesn't feel like me, you know?"
            elif cycle == 3:
                yuuhi "Eventuallyyyyy haahaahaha Eventuallyyyyy~ Oh! Did you hear that? That song has been stuck in my head all day!"
            show yuuhi natural2 with dissolve
        call screen is_yuuhi with Dissolve(0.5)
    elif time_of_day == "night":
        if yuuhi_harem:
            show yuuhi happy1 with dissolve
            if cycle == 0: 
                yuuhi "It's late... Do you want to sleep next to me tonight? Just kidding... I doubt my dad would agree to that yet..."
            elif cycle == 1:
                yuuhi "Sometimes I dream about you, but for some reason it always ends with you... Forget it."
            elif cycle == 2:
                yuuhi "Mmm... Oh! Hey!"
            elif cycle == 3:
                yuuhi "If I sleep in your arms, I wonder if these nightmares will go?"
            show yuuhi happy2 with dissolve
        else:
            show yuuhi natural1 with dissolve
            if cycle == 0:
                yuuhi "*yawn* Oh! Hello, sir... Did you need something?"
            elif cycle == 1:
                yuuhi "I-I'm awake! I wasn't sleeping! Oh... it's just you."
            elif cycle == 2:
                yuuhi "I like the sound of the crickets at night. It makes everything feel... peaceful."
            elif cycle == 3:
                yuuhi "What do you think the future will look?" 
            show yuuhi natural2 with dissolve
        call screen is_yuuhi with Dissolve(0.5)

label is_yuuhi_talk:
    if yuuhi_talk_choice1:
        mc "How are you doing?"
        if mc_harem_yuuhi:
            scene 31_s1 with dissolve
            yuuhi "A-Are you worried about me, [mc]?"
            scene 31_s2 with dissolve
            mc "It's just a simple question..."
            scene 31_s1 with dissolve
            yuuhi "Hehe~ Well, I'm a little tired, but thanks for asking~"
            scene 31_s2 with dissolve
            perception "She gives you a wink... or at least, she tries. One eye shuts too slow, the other flutters for a second like she's reconsidering halfway through."
            mc "Tired? From what? I haven't seen any customers here."
            scene 31_s15 with dissolve
            yuuhi "Uh... You know... Standing around all day gets exhausting too..."
            scene 31_s16 with dissolve
            mc "Right."
        else:
            scene 31_s1 with dissolve
            yuuhi "I'm doing fine, thank you for asking, [mc]."
            scene 31_s2 with dissolve
        call screen is_yuuhi with dissolve
    elif yuuhi_talk_choice2:
        mc "I want to know more about you."
        if mc_harem_yuuhi:
            scene 31_s15 with dissolve
            yuuhi "Me? Trust me, there's not much to tell..."
            scene 31_s16 with dissolve
            mc "Come on, do you really want us to be a couple without me knowing anything about you?"
            scene 31_s1 with dissolve
            yuuhi "When you put it that way... *ahem* I was born in Kaerat—"
            scene 31_s2 with dissolve
            mc "Kaerat? Is that nearby?"
            scene 31_s1 with dissolve
            yuuhi "No, it isn't on Illus, another continent up north named Veilnirn. It's where Elves originated from!"
            scene 31_s2 with dissolve
            mc "Mhm. And? What about your family? If you're okay sharing."
            scene 31_s1 with dissolve
            yuuhi "It's fine... I was told my mother died giving birth to me. As for my father... I don't really know."
            scene 31_s2 with dissolve
            mc "You don't?"
            scene 31_s1 with dissolve
            yuuhi "No. Maybe he left because of my mother's death. Maybe he was never there to begin with. I have no way of knowing."
            scene 31_s2 with dissolve
            mc "...I'm sorry, Yuuhi. I probably shouldn't have brought it up."
            scene 31_s15 with dissolve
            yuuhi "It's fine, really."
            empathy "She means it. The pain faded long ago—what's left is just a story she's told too many times to count."
            scene 31_s1 with dissolve
            yuuhi "Afterward, I was raised in an orphanage... until my stepfather adopted me."
            scene 31_s2 with dissolve
            mc "That's good, right? How was he?"
            scene 31_s1 with dissolve
            yuuhi "...He wasn't the kind to show it much. His emotions I mean."
            yuuhi "But... I think deep down, he cared."
            yuuhi "We came here eleven years ago and lived together ever since. That's pretty much my whole story."
            scene 31_s2 with dissolve
            mc "Thanks for telling me."
            scene 31_s15 with dissolve
            yuuhi "H-Huh? Why are you thanking me?"
            scene 31_s16 with dissolve
            mc "Because it means something that you'd share it with me."
            scene 31_s13 with dissolve
            yuuhi "O-Oh... well... you're welcome, I guess~"
            scene 31_s14 with dissolve
        else:
            scene 31_s15 with dissolve
            yuuhi "M-Me? What for, [mc]?"
            scene 31_s16 with dissolve
            mc "I'd just like to. You look interesting."
            scene 31_s15 with dissolve
            yuuhi "Sorry, but I'd rather not talk about private stuff with customers."
            yuuhi "Is there anything else I can help you with?"
            scene 31_s16 with dissolve
        call screen is_yuuhi with dissolve
    elif yuuhi_talk_choice3:
        if mc_harem_yuuhi:
            if not mc_maia_left:
                if yuuhi_talk_choice3_first:
                    $ yuuhi_talk_choice3_first = False
                    if mc_told_yuuhi_maia:
                        mc "I have a wife. I think I've told you before."
                        scene 31_s19 with dissolve
                        yuuhi "Yeah... you did, [mc]..."
                        scene 31_s20 with dissolve
                        mc "You don't sound to happy about that."
                    elif not mc_told_yuuhi_maia:
                        $ mc_told_yuuhi_maia = True
                        mc "I need to tell you something. I have a wife."
                        scene 31_s19 with vpunch
                        yuuhi "What!? But... but you look so young?"
                        scene 31_s20 with dissolve
                        mc "I'm sorry. I should have told you earlier. Will that change anything between us?"
                        scene 31_s19 with dissolve
                        yuuhi "N-no... I think it's fine... My Pops has two wives too."
                        scene 31_s20 with dissolve
                        mc "Good to know."
                    scene 31_s19 with dissolve
                    yuuhi "Can you tell me about her?"
                    scene 31_s20 with dissolve
                    call screen yuuhi_talk_maia_choice with dissolve
                else:
                    mc "So about Maia—"
                    scene 31_s17 with dissolve
                    yuuhi "[mc]... Can we please not mention her anymore? At least not for now."
                    scene 31_s18 with dissolve
                    mc "Alright."
                    if mc_told_yuuhi_love_maia:
                        empathy "Her tone is soft but firm, a quiet plea for distance. She doesn't want to compete, not now."
            else:
                mc "(There's no reason to tell her about my divorce with Maia. The past should stay in the past.)"
        else:
            mc "(There's no reason to tell her about Maia. We aren't in a relationship afterall.)"
        call screen is_yuuhi with dissolve

    elif yuuhi_talk_choice4:
        mc "How's your pregnancy?"
        if mc_harem_yuuhi:
            #if yuuhi_pregnant:
                #if cycle == 0:
                    #show yuuhi natural1 with dissolve
                    #yuuhi "It's strange... knowing there's a life growing inside me. Our child."
                    #show yuuhi natural2 with dissolve
                #elif cycle == 1:
                    #show yuuhi natural1 with dissolve
                    #yuuhi "I feel... different. My body's changing in ways I didn't expect. But I love knowing this baby is yours."
                    #show yuuhi natural2 with dissolve
                #elif cycle == 2:
                    #show yuuhi happy1 with dissolve
                    #yuuhi "You know... pregnant women get extra needy... Would you like to help with that?"
                    #show yuuhi happy22 with dissolve
                #elif cycle == 3:
                    #show yuuhi angry1 with dissolve
                    #yuuhi "Ugh... my back hurts, my feet are swollen, and I swear, if I crave pickles and honey one more time, I'm going to lose it."
                    #show yuuhi angry2 with dissolve
            #else:
            scene 31_s13 with dissolve
            yuuhi "Are you implying something?"
            scene 31_s14 with dissolve
            mc "Maybe I am."
            scene 31_s13 with dissolve
            yuuhi "Hehe~"
            scene 31_s14 with dissolve
        else:
            scene 31_s15 with dissolve
            yuuhi "...What?"
            scene 31_s16 with dissolve
            mc "Sorry... that probably sounded really weird."
            scene 31_s15 with dissolve
            yuuhi "A little..."
            scene 31_s16 with dissolve
        call screen is_yuuhi with dissolve
    elif yuuhi_talk_choice5:
        call screen is_yuuhi with dissolve

label is_yuuhi_talk_op4:
    mc "What do you think about me?"
    if mc_harem_yuuhi:
        scene 31_s15 with dissolve
        yuuhi "Huh? Come on! Don't put me on the spot like that!"
        scene 31_s16 with dissolve
        mc "Sorry, I just really want to know."
        scene 31_s15 with dissolve
        yuuhi "Umm... well..."
        if mc_screamed_yuuhi:
            yuuhi "You did scream at me that time when we first met..."
            scene 31_s16 with dissolve
            mc "Oh, that? Yeah... sorry about that. I wasn't really in the mood for jokes."
            scene 31_s15 with dissolve
            yuuhi "I'm sorry too. I shouldn't have said things like that to someone I didn't know..."
            scene 31_s16 with dissolve
            mc "Well, I guess that makes us even?"
            scene 31_s12 with dissolve
            yuuhi "Mhmm~"
            $ mc_screamed_yuuhi = False
            call screen is_yuuhi with dissolve
        else:
            scene 31_s1 with dissolve
            yuuhi "You've been really nice to me so far."
            scene 31_s2 with dissolve
            mc "Nice?"
            scene 31_s1 with dissolve
            yuuhi "Umm... well, you did accept my proposal~"
            scene 31_s2 with dissolve
            mc "*sigh* That wasn't... okay, fine. What else?"
            scene 31_s1 with dissolve
            yuuhi "Umm... you also don't hit me."
            scene 31_s2 with dissolve
            mc "What the hell? Why would I hit you?"
            scene 31_s1 with dissolve
            yuuhi "I don't know... my Pops used to hit my stepmom. Maybe when we get married, you will?"
            scene 31_s2 with dissolve
            mc "What?! No!"
            impulse "What if she wants it? Cold dinner after a long day, the kids screaming, the ale's all but piss, tsk, tsk. Gotta teach her somehow, right? It's for her own good in the end."
            scene 31_s1 with dissolve
            yuuhi "But... why not?"
            scene 31_s2 with dissolve
            mc "Alright, we're done here. I'm not hitting you. Not now, not ever."
            scene 31_s13 with dissolve
            yuuhi "Ohhh~ So you're saying I can get away with anything~?"
            scene 31_s14 with dissolve
            mc "No. I'm saying I'm not a psychopath."
            call screen is_yuuhi with dissolve
    else:
        scene 31_s1 with dissolve
        yuuhi "W-What do you mean?"
        scene 31_s2 with dissolve
        mc "Just in general, what do you think about me?"
        scene 31_s1 with dissolve
        yuuhi "Oh... well... you're really strong. You're also really handsome and—"
        scene 31_s15 with dissolve
        yuuhi "Uhh! I mean!"
        scene 31_s16 with dissolve
        mc "*chuckles* Alright then."
        yuuhi "..."
        empathy "She's avoiding eye contact so hard she might tunnel through the floor."
        call screen is_yuuhi with dissolve

label yuuhi_sex_not_harem:
    mc "(I probably shouldn't go around asking {i}that{/i} of girls who barely know me. I don't want to be labeled a pervert...)"
    call screen is_yuuhi with dissolve

    show yuuhi angry1 with dissolve
    yuuhi "S-s-sex?!... Sir!"
    show yuuhi angry2 with dissolve
    mc "What? Did you forget what happened last time I was here?"
    show yuuhi nervous1 with dissolve
    yuuhi "T-that was...! I mean...! {i}*sigh*{/i}"
    yuuhi "I-I'm sorry, but I can't. I shouldn't. Not with someone who isn't my future husband..."
    yuuhi "{i}*sigh*{/i} {size=30}My step dad's going to kill me if he knew..."
    show yuuhi nervous2 with dissolve
    "Check failed: Yuuhi isn't a part of your harem!"
    jump irda_blacksmith

label yuuhi_sex_not_yet:
    show yuuhi nervous1 with dissolve
    yuuhi "S-s-sex?!... Umm..."
    yuuhi "C-could you wait until my step dad isn't in the shop at least..."
    show yuuhi nervous2 with dissolve
    mc "Do I come back later?"
    yuuhi "Mhmm."
    mc "Got it."
    jump irda_blacksmith

label diana_call:
        if is_diana_first_time_talk:
            show diana outfit natural1 with dissolve
            di "Oh? Look who's back. Our very own hero~"
            show diana outfit natural2 with dissolve
            mc "Hey. Anything new around here?"
            show diana outfit natural1 with dissolve
            di "Same old, same old. But what I'm really curious about... is what brings our brave hero back here."
            show diana outfit natural2 with dissolve
            mc "Uh... Well—"
            show diana outfit flirt1 with dissolve
            di "Come on, sweetpea. There's only one reason a man walks into a brothel."
            show diana outfit natural2 with dissolve
            mc "You got me..."
            show diana outfit natural1 with dissolve
            di "No need to play shy, darling. And since you took care of that nasty ogre... you've earned yourself a little reward."
            show diana outfit natural2 with dissolve
            mc "What is it?"
            show diana outfit flirt1 with dissolve
            di "You can fuck my tits whenever you like... No charge."
            show diana outfit flirt2 with dissolve
            mc "For... free?"
            show diana outfit flirt1 with dissolve
            di "{i}For. Free~{/i}"
            show diana outfit flirt2 with dissolve
            $ is_diana_first_time_talk = False
            call screen is_diana with Dissolve(0.5)
        if is_diana_gave_birth:
            show diana outfit natural1 with dissolve
            di "Oh [mc]... look what you did to me~ Your seed finally blossomed..."
            show diana outfit nervous1 with dissolve
            di "That labor was torture... but nothing compared to how you stretch me when we fuck."
            show diana outfit natural1 with dissolve
            di "But you know what's strange? This empty womb feels... lonely now."
            show diana outfit flirt1 with dissolve
            di "Why don't you come claim it again? I want to feel that thick cock planting another baby deep inside me..."
            di "What do you say, daddy? Ready to knock up your favorite broodmare one more time?"
            show diana outfit flirt2 with dissolve
            $ is_diana_gave_birth = False
            $ is_diana_gave_birth2 = True
            call screen is_diana with Dissolve(0.5)

        if is_diana_gave_birth2:
            show diana outfit natural1 with dissolve
            di "Don't worry your pretty little head about [baby_name]..." 
            if baby_gender == "male":
                di "The Queen's experts will take care of him." 
                di "Though I suspect he'll inherit his father's... appetites..." 
            else:
                di "The Queen's handlers will mold her into a proper young lady..." 
            $ is_diana_gave_birth2 = False
            show diana outfit natural2 with dissolve
            call screen is_diana with Dissolve(0.5)

        if diana_pregnant and diana_pregnancy_timer >= pregnancy_time // 2:
            if is_diana_mouth_cum:
                show diana outfit mouth1 with dissolve
                jump is_diana_mouth_cum
            if is_diana_wearing_all:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "Ugh, my belly's getting too big for some of the weird shit customers keep asking for... Not that I mind, but I do have my limits."
                elif cycle == 1:
                    di "I swear, every time I think about that huge cock of yours, my tits start leaking... You really did a number on me, didn't you?"
                elif cycle == 2:
                    di "Come here. Feel this... It's your child, after all. Doesn't it make you a little excited, knowing I'm carrying your seed?"
                elif cycle == 3:
                    di "Lately, I can't stop craving the taste of semen. Think it's just a pregnancy thing, or am I really just a cum-hungry whore?"
                show diana outfit natural2 with dissolve
            else:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "I was just cleaning a table when some old guy smacked my ass out of nowhere. Can you believe that? I mean, at least buy me a drink first."
                elif cycle == 1:
                    di "I love watching the reaction of the people when I walk outside like this, the guards don't seem too happy though..."
                elif cycle == 2:
                    di "Every time I walk past a table, someone's fingers end up inside me... I swear, my legs are about to give out."
                elif cycle == 3:
                    di "So... someone paid me to 'buttchug' today. Didn't even know what it was till now... Let's just say I'll never look at alcohol the same way again."
                show diana outfit natural2 with dissolve
        elif diana_pregnant:
            if is_diana_wearing_all:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "Ugh, my tits feel like they're full of rocks... your baby's already making me ache in the best ways~"
                elif cycle == 1:
                    di "Been puking all morning... but somehow still hungry for your cock. Pregnancy does weird things~"
                elif cycle == 2:
                    di "Can you believe some guys pay extra now that I'm knocked up? Perverts want to 'feel the baby move' while they fuck me..."
                elif cycle == 3:
                    di "My cunt's been dripping nonstop since the conception... your brat's making me even hornier than usual~"
                show diana outfit natural2 with dissolve
            else:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "See that little swell? That's your seed taking root... want to celebrate with a creampie?"
                elif cycle == 1:
                    di "My nipples are so sensitive now... customers keep making me cum just by sucking them~"
                elif cycle == 2:
                    di "The Queen says pregnant women get twenty percent more salary... I sure do love her sometimes."
                elif cycle == 3:
                    di "I've been rubbing my belly between customers... imagining how much bigger it'll get with your next load~"
        else:
            if is_diana_mouth_cum:
                show diana outfit mouth1 with dissolve
                jump is_diana_mouth_cum
            if is_diana_wearing_all:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "Welcome back, sir. How may I service you?"
                elif cycle == 1:
                    di "No one's been asking to use my ass lately... Think I should drop the price? Or maybe they just don't know what they're missing~"
                elif cycle == 2:
                    di "My throat's feeling a little {i}empty{/i}. Wanna help with that?"
                elif cycle == 3:
                    di "I swear, if one more guy ejaculates on my hair, I'm going to scream. Do you {i}know{/i} how long it takes to wash that out?"
                show diana outfit natural2 with dissolve
            else:
                show diana outfit natural1 with dissolve
                if cycle == 0:
                    di "I was just mopping the floor, minding my business, and some guy just {i}ejaculated{/i} all over my back... Some people, huh?"
                elif cycle == 1:
                    di "Had a guy pay me for a quick handjob under the table... while his wife was {i}right there{/i}. He didn't even try to hide it."
                elif cycle == 2:
                    di "The way they keep staring at me... it's making me {i}ache{/i}. Wanna do something about it?"
                elif cycle == 3:
                    di "*cough* Ugh, sorry. The last guy had me deepthroating a giant cucumber for ages... and the bastard didn't even fuck me."
                show diana outfit natural2 with dissolve
        call screen is_diana with Dissolve(0.5)
        
label is_diana_talk:
    if diana_talk_choice1:
        mc "How are you doing?"
        scene 7_s22 with dissolve
        if mc_harem_diana or mc_friend_diana:
            di "I feel much safer with you around, [mc]~"
            if diana_pregnant:
                di "And don't worry, no pregnancy sickness yet."
        else:
            di "I'm doing well. Thank you for asking, darling."
        scene 7_s23 with dissolve
        call screen is_diana with dissolve
    elif diana_talk_choice2:
        mc "Do you need something?"
        scene 7_s22 with dissolve
        di "Is that a normal question, or are you implying something more... sexual?"
        scene 7_s23 with dissolve
        mc "It's normal, a normal question..."
        scene 7_s22 with dissolve
        di "Oh, well... maybe a new handbag or dress. Have you seen what they're selling at Mara's?"
        scene 7_s23 with dissolve
        mc "Can't say I have."
        scene 7_s22 with dissolve
        di "Ah! It's {i}soo{/i} lovely."  
        scene 7_s26 with dissolve
        di "Those wedding dresses..."
        scene 7_s28 with dissolve
        di "..."
        if mc_harem_diana:
            mc "Don't look too down. One day, I'll be the one to dress you in one." 
            scene 7_s26 with dissolve
            di "[mc]..."
            scene 7_s30 with dissolve
            di "Thank you. You have no idea how happy that makes me."  
            scene 7_s31 with dissolve
            mc "Always."
        elif mc_friend_diana:
            mc "Don't look too sad. Someday, someone will be lucky enough to dress you in one."  
            scene 7_s26 with dissolve
            di "*sigh* But I'm so tired of waiting, [mc]..."  
            scene 7_s28 with dissolve
            mc "Don't give up, Skeleton."
            scene 7_s30 with dissolve
            di "*laughs* What's that supposed to mean?"  
            scene 7_s31 with dissolve
            mc "Don't worry about it."
        else:
            scene 7_s26 with dissolve
            di "...Do you think I'll ever find a man who truly accepts me?"
            scene 7_s27 with dissolve
            mc "...What?"
            scene 7_s26 with dissolve
            di "Forget it."
            scene 7_s28 with dissolve
            empathy "Whatever she meant, she doesn't want to talk about it."
        call screen is_diana with dissolve

    elif diana_talk_choice3:
        mc "Do you want to go on a date?"
        scene 7_s27 with dissolve
        di "..."
        mc "Diana?"
        scene 7_s26 with dissolve
        di "*sigh* Sweetheart, my idea of romance is bent over a table while you split me open. Save the poetry."
        scene 7_s27 with dissolve
        empathy "Her voice is hollow, like she's reciting something rehearsed—something meant to push you away."
        mc "Are you sure? You sound conflicted. You can forget your work for a bit, just go out and have fun."
        di "..."
        scene 7_s26 with dissolve
        di "I'm good, but thank you, [mc]."
        scene 7_s28 with dissolve
        call screen is_diana with dissolve

    elif diana_talk_choice4:
        mc "How's your pregnancy?"
        if diana_pregnant:
            if cycle == 0:
                show diana outfit natural1 with dissolve
                di "Your brat's making me crave cock more than ever... fuck me gently?"
                show diana outfit natural2 with dissolve
            elif cycle == 1:
                show diana outfit natural1 with dissolve
                di "Think he'll have your size? I'll need new holes to wreck if he does~"
                show diana outfit natural2 with dissolve
                mc "Well, we don't know if it's a {i}he{/i} yet. Also please don't say that..."
            elif cycle == 2:
                show diana outfit flirt1 with dissolve
                di "Your seed's making my tits swell... care to test if they've made milk yet?"
                show diana outfit flirt2 with dissolve
            elif cycle == 3:
                show diana outfit natural1 with dissolve
                di "I can feel him moving around when I cum... your baby loves watching mommy get railed."
                show diana outfit natural2 with dissolve
        else:
            if cycle == 0:
                show diana outfit flirt1 with dissolve
                di "This belly's empty and my womb's hungry... plant that thick cock where it belongs."
                show diana outfit flirt2 with dissolve
            elif cycle == 1:
                show diana outfit natural1 with dissolve
                di "I'm not pregnant... but I dream of waddling around town full of your spawn."
                show diana outfit natural2 with dissolve
            elif cycle == 2:
                show diana outfit natural1 with dissolve
                di "Pregnant? Maybe you're not as potent anymore? Let's test that~"
                show diana outfit natural2 with dissolve
            elif cycle == 3:
                show diana outfit natural1 with dissolve
                di "My belly's empty... maybe you should tie me down and pump me full."
                show diana outfit natural2 with dissolve
        call screen is_diana with dissolve
    elif diana_talk_choice5:
        call screen is_diana with dissolve

label yuuhi_talk_quest2_yuuhi_talkq_getArmor_notready:
    show yuuhi natural1 with dissolve
    yuuhi "You're armor isn't ready yet, sir."
    show yuuhi natural2 with dissolve
    call screen is_yuuhi with Dissolve(0.5)

default eireen_talk_choice1 = False
default eireen_talk_choice2 = False
default eireen_talk_choice3 = False
default eireen_talk_choice4 = False
default eireen_talk_choice5 = False

label eireen_call:
    show eireen natural1 with dissolve
    eireen "Take a look at the quests available, [mc]."
    show eireen natural2 with dissolve
    call screen is_eireen with Dissolve(0.5)

label is_eireen_talk:
    if eireen_talk_choice1:
        mc "How are you doing?"
        if cycle == 0:
            show eireen natural1 with dissolve
            eireen "I'm fine. No need to worry about me."
            show eireen natural2 with dissolve
        elif cycle == 1:
            show eireen frown1 with dissolve
            eireen "Anywhere but here would be nice."
            show eireen frown2 with dissolve
        elif cycle == 2:
            show eireen frown1 with dissolve
            eireen "Between the paperwork and reckless adventurers? Take a wild guess."
            show eireen frown2 with dissolve
        elif cycle == 3:
            show eireen natural1 with dissolve
            eireen "Tired, overworked, and underpaid. The usual."
            show eireen natural2 with dissolve

        call screen is_eireen with dissolve
    elif eireen_talk_choice2:
        mc "Do you need something?"
        if cycle == 0:
            show eireen frown1 with dissolve
            eireen "A barrel of mead and a week of silence. Think you can manage that?"
            show eireen frown2 with dissolve
        elif cycle == 1:
            show eireen natural1 with dissolve
            eireen "Shouldn't I be asking {i}you{/i} that?"
            show eireen natural2 with dissolve
        elif cycle == 2:
            show eireen frown1 with dissolve
            eireen "Let's see... A million gold coins, a house on a hill, and a... {i}*sigh*{/i} forget it..."
            show eireen frown2 with dissolve
        elif cycle == 3:
            show eireen natural1 with dissolve
            eireen "No, but I appreciate the offer."
            show eireen natural2 with dissolve
        call screen is_eireen with dissolve
    elif eireen_talk_choice3:
        mc "Do you want to go on a date?"
        show eireen frown1 with dissolve
        eireen "A... date?"
        show eireen frown2 with dissolve
        mc "Yeah."
        show eireen frown1 with dissolve
        eireen "Do you have any idea how ridiculous you sound right now?"
        show eireen frown2 with dissolve
        mc "..."
        call screen is_eireen with dissolve
    elif eireen_talk_choice4:
        mc "How's your pregnancy?"
        show eireen frown1 with dissolve
        eireen "Pregnancy? Did you hit your head, [mc]?"
        show eireen frown2 with dissolve
        call screen is_eireen with dissolve
    elif eireen_talk_choice5:
        call screen is_eireen with dissolve

label eireen_talk_quest2_yuuhi_talkq_getArmor:
    show eireen natural1 with dissolve
    eireen "[mc], Did you get your armor?"
    show eireen natural2 with dissolve
    mc "Still waiting on it."
    call screen is_eireen with Dissolve(0.5)

label eireen_quest_quest2_yuuhi_talkq_getArmor:
    show eireen frown1 with dissolve
    eireen "Where do you think you're going without proper protection?"
    show eireen frown2 with dissolve
    mc "Right, right..."
    call screen is_eireen with Dissolve(0.5)

label null_map:
    "You don't have access to the map yet."
    $ screen_tooltip = ""  
    call screen gameplay

label ren_mc_rename:
    $ rx = renpy.input("What should she call me? (default: Sir)", length=32)
    $ rx = rx.strip()
        
    if rx == "":
        $ rx = "Sir"
        
        # Capitalize the first letter and letters after a period '.'
    $ rx = '. '.join(sentence.capitalize() for sentence in rx.split('. '))
    scene ren_natural1 with dissolve
    m "Of course, [rx]."
    jump irda_kitchen
    call screen is_ren with dissolve

label timeskip_null:
    mc "(I should probably talk to the Queen before she gets angry.)"
    $ screen_tooltip = ""  
    call screen gameplay with dissolve
label timeskip:
    #a button that the player can press will call this label
    $ quest_screen_open = False
    $ map_screen_open = False
    $ mc_stats_overview = False
    if time_of_day == "morning":
        $ random_event = random.randint(0, 25)
        $ time_of_day = "night"

        if in_bedroom:
            if time_of_day == "morning":
                if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
                    play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            else:
                if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
                    play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            jump irda_bedroom

        elif in_throne:
            if time_of_day == "morning":
                if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
                    play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            else:
                if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
                    play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            scene irda_throne_night with dissolve
        elif in_kitchen:
            if time_of_day == "morning":
                if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
                    play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            else:
                if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
                    play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            scene irda_kitchen_night with dissolve
        elif in_roof:
            if time_of_day == "morning":
                if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
                    play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            else:
                if renpy.music.get_playing(channel='music1') != "gameplay_night.mp3":
                    play music "gameplay_night.mp3" fadein 2.0 volume 0.1 loop channel "music1"
            scene irda_roof_night with dissolve  
        elif in_guild:
            scene irda_guild_night with dissolve 
        elif in_blacksmith:
            scene irda_blacksmith_night with dissolve
        elif in_brothel:
            jump irda_brothel
        elif in_barn:
            scene irda_barn_night with dissolve 
        
        if random_event == 0:
            "You spend some time reading. You learn that female elves are more likely to get pregnant from a human rather than an elf male."
        elif random_event == 1:
            "You find a rat while walking the halls of the castle."
        elif random_event == 2:
            "You found a silver coin!"
            $ coin += 10
        elif random_event == 3:
            "While walking in the main floor of the castle, you find a door reinforced with several steel locks. What could this door lead to?"
        elif random_event == 4:
            "You hear a scream for help while staring out the window of your room... or maybe you just imagined that?"
        elif random_event == 5:
            "A bird flies into your room, flapping wildly before escaping. It drops a feather on the floor."
        elif random_event == 6:
            "You overhear two guards whispering about a hidden treasure somewhere in the castle."
        elif random_event == 7:
            "You trip over a loose floorboard and find a hidden compartment underneath containing an old map of some unknown city."
        elif random_event == 8:
            "You find a strange glowing shard in the castle garden. It hums faintly when touched."
        elif random_event == 9:
            "A merchant passing through the castle courtyard offers the Queen a foot massage, she declines."
        elif random_event == 10:
            "You decide to search the cabinets of your room. Nothing of value was found however you find a statue of some creature you've never seen before."
        elif random_event == 11:
            "A maid rushes past you, muttering something about a 'haunted mirror' in one of the guest rooms."
        elif random_event == 12:
            "You find a stray dog wandering near the castle gates. It wags its tail as it looks up at you."
        elif random_event == 13:
            "While walking through the library, a random book falls from a high shelf, landing open to a page about forbidden magic."
        elif random_event == 14:
            "You hear faint music coming from a distant part of the castle, though no one seems to be playing."
        elif random_event == 15:
            "A gust of wind blows through the window, it's nostalgic smell brings back memories of your world."   
        elif random_event == 16:
            "You find a broken necklace near the well. There's an engraving that reads 'For my love.'" 
        elif random_event == 17:
            "A cat follows you through the courtyard, meowing persistently before darting away."
        elif random_event == 18:
            "You catch sight of a shadowy figure at the end of the corridor, but it vanishes before you can approach."        
        elif random_event == 19:
            "A guard stops you and asks if you've seen someone suspicious wandering the halls."
        elif random_event == 21:
            "A sudden draft makes you shiver, and you notice a crack in the wall blowing cold air."
        elif random_event == 22:
            "You find a broken sword buried in the garden, its blade etched with words you can't understand."
        elif random_event == 23:
            "Ren offers you a bowl of stew and says it was left unclaimed in the kitchen."
        elif random_event == 24:
            "A loud thud echoes through the halls. You turn to find an old guard has accidentally dropped his sword."
        elif random_event == 25:
            "You find a strange drawing on the floor of your room of a mother and a child. They weren't there before."

        call screen gameplay with dissolve

    elif time_of_day == "night":
        mc "(I should head to bed...)"
        call screen gameplay with dissolve
    
label sleep:
    $ days_passed += 1
    $ update_date()
    
    if renpy.music.get_playing(channel='music1') != "gameplay.mp3":
        play music "gameplay.mp3" fadein 2.0 volume 0.1 loop channel "music1"

    if is_maia_face_cum:
        $ is_maia_face_cum = False

    $ is_yuuhi_sex_limit = 1
    $ is_diana_sex_limit = 2
    if not is_diana_wearing_top:
        $ is_diana_wearing_top = True
    if not is_diana_wearing_all:
        $ is_diana_wearing_all = True
    if is_diana_face_cum:
        $ is_diana_face_cum = False

    if maia_pregnant:
        $ maia_pregnancy_timer += 1

    if diana_pregnant:
        $ diana_pregnancy_timer += 1

    if quest2_yuuhi_talkq_getArmor:
        $ quest2_yuuhi_talkq_getArmor_timer -= 1
        if quest2_yuuhi_talkq_getArmor_timer == 0:
            $ yuuhi_talk_quest2_yuuhi_talkq_getArmor_notready = False
            $ quest2_yuuhi_talkq_getArmor_timer_finished = True
            $ current_objective = "Current Objective: Retrieve your armor from the blacksmith."

    if cycle == 3:
        $ cycle = random.randint(0, 3)
    else:
        $ cycle += 1
    $ time_of_day = "morning"

    jump irda_bedroom
    call screen gameplay with dissolve

default has_reb_item = False
label reb_gift:
    if has_reb_item:
        mc "(What should I give her?)"
    else:
        mc "(I don't have anything to give her...)" 
        call screen is_reb with Dissolve(0.5)

label maia_gift:
    mc "I got you something."
    if maia_happy:
        scene 18_s8 with dissolve
        m "W-What is it?"
        scene 18_s7 with dissolve
        mc "Here you go, some fresh strawberries."
        scene 30_s10 with dissolve
        m "F-For me?! Thank you, thank you, thank you, [mx]!"
        play sound "sound_effects/karma_more.mp3" volume 0.2
        if mc_karma < 10:
            $ mc_karma += 1
        $ karma_more = True
        show screen stat_change with easeinright 
        scene 30_s11 with dissolve
        mc "Come on, don't act surprised, you asked for them."
        scene 30_s10 with dissolve
        m "Ehehe~"
        hide screen stat_change with easeoutright
        $ karma_more = False
        scene 30_s11 with dissolve
        $ maia_love += 10
        $ mc_gave_strawberries_maia = True
        $ mc_has_strawberries = False
        call screen is_maia with Dissolve(0.5)

    if maia_sad:
        m "..."
        mc "Are you not going to ask what it is?"
        scene 18_s16 with dissolve
        m "W-What is it...?"
        scene 18_s15 with dissolve
        mc "Here you go, some fresh strawberries."
        scene 18_s16 with dissolve
        m "...Thank you, [mx]."
        scene 18_s15 with dissolve
        perception "She reaches out slowly, her fingers trembling, flinching as though she expects a strike instead of a gift."
        empathy "A small bag of strawberries won't erase what's been broken. It'll take much more than that for her to trust you again."
        m "..."
        call screen is_maia with Dissolve(0.5)

label yuuhi_gift:
    $ mc_has_strawberries = False
    mc "Yuuhi? Do you like strawberries?"
    scene 31_s1 with dissolve
    yuuhi "Yes! I love them! Why do you ask?"
    scene 31_s2 with dissolve
    mc "I got you some."
    scene 31_s15 with dissolve
    yuuhi "W-What? But... I didn't ask for it."
    scene 31_s16 with dissolve
    mc "Don't worry, it's on me."
    play sound "sound_effects/karma_more.mp3" volume 0.2
    if mc_karma < 10:
        $ mc_karma += 1
    $ karma_more = True
    show screen stat_change with easeinright 
    scene 31_s15 with dissolve
    yuuhi "T-Thank you~ This was unexpected, but welcome nonetheless."
    scene 31_s16 with dissolve
    hide screen stat_change with easeoutright
    $ karma_more = False
    $ yuuhi_love += 10
    call screen is_yuuhi with Dissolve(0.5)

label diana_gift:
    if has_item:
        mc "(What should I give her?)"
    else:
        mc "(I don't have anything to give her...)"
        call screen is_diana with Dissolve(0.5)

label queen_sex:
    show queen natural1 with dissolve
    q "Not now, hero. I have far too many matters to attend to."
    show queen happy1 with dissolve
    q "But worry not—when the time is right, I'll gladly indulge in that big cock of yours once more."
    show queen happy2 with dissolve
    call screen is_queen with Dissolve(0.5)

label diana_birth_scene:
    mc "(Diana should be due anytime now... Should I go see her?)"
    call screen diana_birth_scene with dissolve
    call screen gameplay with dissolve

label diana_birth_scene2:
    scene diana_birth1 with Fade(1.0,0.5,0.5)
    di "{i}Haaaaaaa!!!{/i} Fuck..."
    scene diana_birth2 with dissolve
    midwife "Keep pushing, darling! You're almost there."
    di "I am pushing, you old bitch! {i}Anghhhh!{/i} Next time, you carry a baby after taking his monster cock!"
    scene diana_birth3 with dissolve
    di "{i}Mfhhmmmmmmm!!{/i} I swear... if you knock me up again... nghhh!"
    scene birth4 with vpunch
    di "Fuck! Feels like he's tearing me open... just like his father!"
    "The room fills with the sound of a baby's cry—and Diana's breathless laughter."
    $ baby_gender = random.choice(["male", "female"])
    if baby_gender == "male":
        "Congratulations, it's a boy!"
        "The Queen takes the baby from the midwife and hands him to you."
        $ baby_name = renpy.input("What should I name him?", length=12).strip()
        if not baby_name:
            $ baby_name = "Jack"
    else:
        "Congratulations, it's a girl!" 
        "The Queen takes the baby from the midwife and hands her to you."
        $ baby_name = renpy.input("What should I name her?", length=12).strip()
        if not baby_name:
            $ baby_name = "Luna"

    scene birth5 with dissolve
    q "Good job, hero. Your contributions to the city's population will be rewarded."
    scene birth6 with dissolve
    "You received 5 silver coins."
    mc "Woah, what's this for?"
    scene birth5 with dissolve
    q "Consider it an incentive. Keep breeding our women. The more swollen bellies you leave behind, the greater the... benefits."
    q "And who knows? If you fill enough wombs, maybe you'll earn a... {i}special{/i} reward~"
    scene birth6 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump irda_bedroom

label is_diana_talk_pregnant:
    if diana_pregnant:
        mc "How is our little one faring?"
        scene 7_s22 with dissolve
        di "*giggles* He's barely even a droplet at this point. It'll be a while before we can feel any kicks or get real news."
        scene 7_s23 with dissolve
        mc "{i}He?{/i} *chuckles* So you've already decided it's going to be a boy?"
        scene 7_s22 with dissolve
        di "Mhm~ He's going to be the strongest, kindest boy in the whole city."
        di "He'll always help his mother... and he'll be good to everyone. Even to kids who didn't grow up with a father around."
        scene 7_s23 with dissolve
        mc "That sounds really lovely."
        mc "I'm glad you're taking all of this so well, Diana."
        scene 7_s22 with dissolve
        di "Well... I have to, don't I? Someone has to be excited for the both of us."
        scene 7_s23 with dissolve
        call screen is_diana with dissolve
    else:
        mc "How is your pregnancy going?"
        scene 7_s22 with dissolve
        if mc_harem_diana:
            if not mc_convince_diana_pregnancy:
                $ mc_convince_diana_pregnancy = True
                di "Pregnancy? Ohh~ I think I understand what you're hinting at..."  
                di "Are you really willing to take responsibility if that happens?"
                scene 7_s23 with dissolve
                mc "Yes. I am."
                scene 7_s30 with dissolve
                di "...You were supposed to say no, you know."
                di "A-Are you actually serious right now?"
                scene 7_s31 with dissolve
                mc "I'm serious. Nothing would make me happier than seeing you pregnant with my child."
                di "..."
                scene 7_s26 with dissolve
                di "You really mean that..."
                scene 7_s27 with dissolve
                empathy "Her usual smutty expression softens. She looks almost vulnerable for a moment."
                scene 7_s29 with dissolve
                di "I... I don't know what to say. We've only just started dating and you're already talking about getting me pregnant?"
                di "Please tell me... you didn't just want me for that."
                scene 7_s28 with dissolve
                mc "It's not like that. I promise."
                scene 7_s26 with dissolve
                di "*sigh* Most men just say whatever they think I want to hear... but you actually sound like you want it."
                scene 7_s30 with dissolve
                di "Fine then..."
                di "Then let's do it. Let's make a baby and help fix this city's pathetic birth rates together. Maybe that way I can contribute something with my terrible life."
                di "But you better not regret this later, [mc]. And I'm obviously counting on you financially. There's no way I can support a growing child with the meager pay I receive here."
                scene 7_s31 with dissolve
                mc "You don't have to worry about that. I work directly for the Queen now. I've got it."
                scene 7_s30 with dissolve
                di "Just know that once I start showing... you're not allowed to run away. You're stuck with me and that unattractive belly, alright, darling?"
                scene 7_s31 with dissolve
                mc "{i}Unattractive?{/i} Nonsense!"
                scene 7_s24 with dissolve
                di "*giggles* Just... take care of me, alright? If this actually happens... I don't want to go through it alone."
                scene 7_s25 with dissolve
                mc "I'll be there. Always."
            else:
                di "I already agreed to it, darling. It's up to you now to make it happen."
        else:
            di "Last time I checked, I wasn't pregnant, [mc]. Why do you ask~?"
        scene 7_s23 with dissolve
        call screen is_diana with dissolve

label maia_birth_scene:
    mc "(Maia should be due anytime now... Should I go see her?)"
    call screen maia_birth_scene with dissolve
    call screen gameplay with dissolve

label maia_birth_scene2:
    scene maia_birth1 with Fade(1.0,0.5,0.5)
    m "{i}Hnnngh!!!{/i}"
    scene maia_birth2 with dissolve
    midwife "You're doing great, dear. Just a little more!"
    m "I-It hurts!"
    scene maia_birth3 with dissolve
    m "{i}Haaaaaaa!!{/i} I-I can't— I can't do this!"
    scene birth4 with vpunch
    m "{i}HNNHAAAAAAAHH!!!{/i}"
    "The room fills with the sound of a baby's cry."
    $ baby_gender = random.choice(["male", "female"])
    if baby_gender == "male":
        "Congratulations, it's a boy!"
        "The Queen takes the baby from the midwife and hands him to you."
        $ baby_name = renpy.input("What should I name him?", length=12).strip()
        if not baby_name:
            $ baby_name = "Jack"
    else:
        "Congratulations, it's a girl!" 
        "The Queen takes the baby from the midwife and hands her to you."
        $ baby_name = renpy.input("What should I name her?", length=12).strip()
        if not baby_name:
            $ baby_name = "Luna"

    scene birth5 with dissolve
    q "Well done, hero. Another life born into our city... and all thanks to you."
    scene birth6 with dissolve
    "You received 5 silver coins."
    mc "Woah, what's this for?"
    scene birth5 with dissolve
    q "A token of appreciation. Consider it an encouragement... keep filling our wombs, and the rewards will only grow."
    q "Who knows? Breed enough of our women, and perhaps the greatest prize of all will be yours~"
    scene birth6 with dissolve
    scene black with Fade(1.0,0.5,0.5)
    jump irda_bedroom

label maia_no_sex:
    scene 18_s16 with dissolve
    m "N-No!"
    scene 18_s15 with dissolve
    mc "What?"
    scene 18_s16 with dissolve
    m "I... I can't... I just can't... [mx]."
    scene 18_s15 with dissolve
    mc "..."
    empathy "Maia shrinks away, trembling. She's too afraid of you to even consider it."
    call screen is_maia with dissolve

label eurina_temp:
    mc "(Another city on the map... I haven't heard anything about this one yet. I wonder what kind of place it is.)"
    call screen gameplay with dissolve

label nahraya_temp:
    mc "(Darius mentioned that the Queen traveled to Nahraya to ease tensions. Whatever's happening there must be serious...)" 
    call screen gameplay with dissolve

label witch_house_temp:
    mc "(No need to go there yet. If the witch needs me, I'm sure she'll send for me.)"
    call screen gameplay with dissolve


label is_maia_sex_notyet:
    mc "(As tempting as this is, sex will take too long... The Queen is waiting, and I doubt she'd appreciate me showing up late and exhausted.)"
    mc "(Maybe I should go for something quicker instead...)"
    call screen is_maia with dissolve

label free_roam_maia_yuuhi:
    $ mc_told_maia_yuuhi = True
    #if mc met yuuhi
    m "Good morning, [mx]! I hope you had a good sleep."
    mc "Thank you! By the way, I went to the blacksmith."
    m "The blacksmith? Did you buy something cool?"
    mc "I did... kinda? It was a gift from the Queen."
    m "How geneorus of her Majesty. What did he give you? The blacksmith i mean."
    mc "It wasn't a he, it was a she. The blacksmiths daughter, her name's yuuhi."
    m "Oh... W-What was she like?"
    mc "I could tell she wasn't from around here. She looked different."
    m "You mean from another city?"
    mc "Yeah, but she was kinda like you, shy and timid."

label free_roam_maia_nadia:
    $ mc_maia_monogamous_question = True
    $ mc_told_maia_nadia = True
    mc "Maia... what do you think about me being with other women?"  
    scene 30_s2 with dissolve
    perception "Her eyes widen with startled surprise. Her hands grip each other harder, even more so than usual."
    scene 30_s1 with dissolve
    m "[mx]... That's... a sudden question."  
    scene 30_s2 with dissolve
    mc "I want you to be honest with me."  
    scene 30_s1 with dissolve
    m "I... I don't know what to think. My head says one thing, my heart... another."
    m "I thought you'd only want me... but part of me also thinks... someone like you should be desired."
    scene 30_s2 with dissolve
    mc "Isn't it normal for a man to be with more than one woman in this period? And especially now that the birth rates are plummeting in the city."  
    scene 30_s4 with dissolve
    m "I know... I've heard. But it's different when it's {i}you.{/i}"  
    m "When I try to imagine it... my chest feels tight. But... not just bad tight. It's scary, but... not entirely bad? I don't understand it myself."
    m "It's... warm too. As in... I'm proud someone else would wants my husband."
    scene 30_s2 with dissolve
    mc "*chuckles* You don't have to understand it all now."
    scene 18_s10 with dissolve
    m "It's confusing! I still want to be special to you..."
    scene 18_s9 with dissolve
    mc "You are. Always."
    scene 18_s10 with dissolve
    m "You're making me say embarrassing things..."
    scene 18_s9 with dissolve
    empathy "The idea unsettles her, but her love for you is stronger than the worry. She's choosing to meet you with openness instead of fear."
    scene 18_s10 with dissolve
    m "But... if that's what you want... I think... I think I want you to be happy. Even if it means sharing."
    m "When princess Rebecca brought me here, I thought I'd be wed to a guardsman. Or a baker. Someone kind, maybe, but... ordinary. I never dreamed I'd be with someone important like you."
    m "So it's not my place to forbid you anything, [mx]. It's yours to choose. I'll be here. Always yours."
    scene 18_s9 with dissolve
    call screen free_roam_maia_talk_harem with dissolve

label free_roam_maia_talk_harem_op1:
    $ mc_maia_monogamous = True
    $ mc_told_maia_nadia_sex = False
    mc "Don't worry, Maia. It was just a question."
    mc "You're the only woman I'll ever need."  
    scene 30_s1 with dissolve
    m "O-Oh..."
    m "I... I wasn't worried. Just... thinking."
    scene 30_s2 with dissolve
    mc "If you say so."
    scene 30_s6 with vpunch
    m "I was!"
    scene 30_s7 with dissolve
    mc "Woah..."
    m "..."
    scene 18_s11 with dissolve
    m "I... I'm sorry, [mx]! I-I-I didn't mean to! I swear!"
    scene 18_s12 with dissolve
    mc "It's fine. Honestly, I kind of like seeing you flustered. Finally, something different than [mx] this, [mx] that."
    scene 18_s10 with dissolve
    m "[mx]... you're terrible."
    scene 18_s9 with dissolve
    mc "Anyway, let's change the subject."  
    scene 18_s10 with dissolve
    m "Y-Yes..."
    scene 18_s9 with dissolve
    "You can now talk to Maia whenever you encounter interesting people or discover noteworthy things. She will share her thoughts on these topics. Talking to Maia will help her open up to you."
    call screen is_maia with dissolve

label free_roam_maia_talk_harem_op2:
    $ mc_maia_monogamous = False
    $ mc_told_maia_nadia_sex = True
    mc "Yes, Maia. I don't want to lie to you and hurt you later." 
    scene 30_s5 with dissolve
    m "..."
    empathy "A gentle breeze rustles the pages of a nearby book. The sun breaks through the clouds, illuminating her face. Her expression intensely focused, as if solving a riddle about herself."
    scene 30_s4 with dissolve
    m "O-Of course..."
    m "Someone like you... should be shared. It... it makes sense. The thought of it... it's scary, but..."
    m "If that makes you happy... I'll try to be happy for you."
    scene 18_s10 with dissolve
    m "Just... tell me about it sometimes? So I know you're safe..."
    scene 18_s9 with dissolve
    mc "Oh?"
    scene 18_s10 with dissolve
    m "I-I mean! Forget I said that!"
    scene 18_s9 with dissolve
    mc "*chuckles* Thank you for being so understanding."
    scene 18_s10 with dissolve
    m "Just... promise you'll always come back to me? That I'll still be... special?"
    scene 18_s7 with dissolve
    mc "Always, Maia. You're irreplaceable."
    "You can now talk to Maia whenever you encounter interesting people or discover noteworthy things. She will share her thoughts on these topics. Talking to Maia will help her open up to you."
    call screen is_maia with dissolve

label free_roam_maia_talk_slaver:
        $ mc_told_maia_slaver = True
        mc "Listen to this! I met this merchant in the market, he was flaunting this girl with him. Said it's from his homeland."
        scene 30_s1 with dissolve
        m "A girl?"
        scene 30_s2 with dissolve
        mc "Yeah. Beautiful, honestly. Dark skin, long hair. But she barely said a single word. Just stood there, eyes down, completely silent."
        scene 30_s1 with dissolve
        m "Very still..."
        scene 30_s2 with dissolve
        mc "Maia?"
        scene 18_s8 with dissolve
        m "Sorry, [mx]. It's nothing, please continue."
        scene 18_s7 with dissolve
        mc "Like I said, she was eerily quiet, it creeped me out a little."
        scene 18_s8 with dissolve
        m "What... what did the merchant look like?"
        scene 18_s7 with dissolve
        mc "What he looked like? Foreign clothes... flowing robes and weird patterns. Dark skin, bald head. Why?"
        scene 30_s1 with dissolve
        m "*sigh* ...Thank the gods."
        scene 30_s2 with dissolve
        mc "Hmm? What's wrong, Maia?"
        scene 18_s10 with dissolve
        m "I-It's nothing!"
        scene 18_s9 with dissolve
        mc "Hey. That sigh wasn't 'nothing.' What's going on?"
        scene 18_s10 with dissolve
        m "I-it's really nothing! I just... for a second I thought..."
        scene 18_s9 with dissolve
        mc "Thought what?"
        scene 18_s10 with dissolve
        m "I thought... maybe it was someone else. Someone bad. From before."
        scene 18_s9 with dissolve
        mc "Someone who scared you?"
        scene 18_s10 with dissolve
        m "Yes. But it wasn't him. The man you described... he's not the one."
        scene 18_s9 with dissolve
        mc "You don't have to tell me everything. But if you ever want to..."
        scene 18_s8 with dissolve
        m "I know. Thank you, [mx]."
        scene 18_s7 with dissolve
        call screen is_maia with dissolve

label free_roam_maia_talk_guild:
    $ mc_told_maia_guild = True
    mc "I went to the guild the other day."
    scene 18_s8 with dissolve
    m "Oh! What did you see there?"
    scene 18_s7 with dissolve
    mc "Honestly... not much. There was this elven guy with his group and this big scary armored guy."
    mc "And these two girls, Kat and Ava."
    mc "I felt kinda out of place there, to tell you the truth."
    scene 18_s8 with dissolve
    m "Out of place? Why, [mx]?"
    scene 18_s7 with dissolve
    mc "I just didn't have the crazy armor they were all wearing... or a weapon at the time."
    scene 30_s1 with dissolve
    m "But does that really matter?"
    scene 30_s2 with dissolve
    mc "It kind of does. They looked like they belonged there. I didn't."
    scene 30_s1 with dissolve
    m "M-Maybe not yet..."
    m "But they'll see."
    scene 30_s2 with dissolve
    mc "See what?"
    scene 30_s1 with dissolve
    m "That you don't need heavy armor or a big sword to be someone important."
    m "That even without all that... you're still above them."
    scene 30_s2 with dissolve
    mc "...Huh?"
    scene 30_s1 with dissolve
    m "One day, your name will be written in history. People will whisper it in the dark, and cry it in the streets."
    impulse "God damn right."
    m "Some will love you. Some will hate you."
    m "But all of them will kneel when they hear it."
    m "It doesn't matter how you get there... only that you do."
    m "And I'll always be right behind you."
    scene 18_s8 with dissolve
    m "I believe in you, [mx]. More than anyone."
    scene 18_s7 with dissolve
    mc "..."
    mc "Thank you, Maia. This was really encouraging."
    m "Mhmm~"
    call screen is_maia with dissolve 

label free_roam_maia_talk_ogre:
    $ mc_told_maia_ogre = True
    mc "Do you wanna talk about the ogre?"
    if mc_lied:
        scene 18_s8 with dissolve
        m "The ogre? You killed it, [mx]. Right?"
        scene 18_s7 with dissolve
        call screen free_roam_maia_talk_ogre with dissolve
    else:
        $ mc_told_maia_ogre_truth = True
        scene 18_s8 with dissolve
        m "The ogre? I remember her Majesty saying something about how it was an accident."
        scene 18_s7 with dissolve
        mc "Yeah. A cage was hanging above a tree. I think when the ogre swung his axe at me, he shook the tree and it fell on him."
        scene 30_s1 with dissolve
        m "I see... that must have been terrifying, [mx]. You weren't hurt, were you?"
        scene 30_s2 with dissolve
        mc "You... you actually believe me?"
        scene 30_s1 with dissolve
        m "Yes? Why wouldn't I, [mx]?"
        scene 30_s2 with dissolve
        mc "I don't know... nobody seems to take me seriously when I tell them the truth."
        scene 30_s1 with dissolve
        m "Maybe... it's because they see something in you, [mx]."
        scene 30_s2 with dissolve
        mc "Something?"
        scene 18_s13 with dissolve
        m "Potential."
        scene 18_s14 with dissolve
        mc "Maybe. Or maybe they just want to use me."
        scene 18_s13 with dissolve
        m "...Then make sure they do."
        scene 18_s14 with dissolve
        mc "What do you mean?"
        scene 18_s13 with dissolve
        m "If they want to use you, make them need you."
        m "That way... no one can ever cast you aside."
        scene 18_s14 with dissolve
        mc "Thank you, Maia."
        scene 18_s13 with dissolve
        m "I'm always here for you... [mc]."
        scene 18_s14 with dissolve
        call screen is_maia with dissolve

label free_roam_maia_talk_witch:
    $ mc_told_maia_witch = True
    mc "I finally got done with the witch."
    scene 30_s1 with dissolve
    m "I hope you weren't hurt, [mx]?"
    scene 30_s2 with dissolve
    mc "I'm fine, thank you for asking. It wasn't what I expected to be honest. And I still can't believe the Queen ordered me to hunt a witch as a first task."
    scene 18_s10 with dissolve
    m "Her Magesty can be..."
    scene 18_s9 with dissolve
    mc "Come on, say it. It's not like she's listening to us through the walls."
    scene 18_s10 with dissolve
    m "S-she's really stubborn... If she wants something done then it {i}has{/i} to be done."
    scene 18_s9 with dissolve
    mc "Yeah, I got that impression in the little time I spent with her."
    scene 18_s8 with dissolve
    m "What happened to the witch, [mx]? If you don't mind me asking."
    scene 18_s7 with dissolve
    if quest_witch_amelia_dead:
        mc "The witch is dead."
        scene 30_s1 with dissolve
        m "Oh... I see."
        scene 30_s2 with dissolve
        mc "She was too dangerous. I did what I had to do."
        scene 30_s1 with dissolve
        m "I understand, [mx]. If that was your decision, then I won't question it."
        scene 30_s2 with dissolve
        mc "You sound uncertain."
        scene 30_s1 with dissolve
        m "It's not that... I just—"  
        m "Please, just promise me you won't become numb to these things. I... I know the world can be cruel, but I don't want it to change you."
        scene 30_s2 with dissolve
        mc "I'll be fine, Maia."  
        scene 30_s1 with dissolve
        m "I hope so, [mx]... I really do." 
        scene 30_s2 with dissolve
    elif not quest_witch_amelia_alive_free:
        mc "I caught her and brought her back. She should be locked up in the dungeon by now."
        scene 18_s8 with dissolve
        m "I see. Good job, [mx]!"
        scene 18_s7 with dissolve
        mc "Thank you, Maia."
        scene 18_s8 with dissolve
        m "I hope you don't mind me saying this, but... please don't let the success get to your head. Always be careful when you're out there."
        scene 18_s7 with dissolve
        mc "Got it."
    elif quest_witch_amelia_alive_free:
        mc "I'll tell you the truth, but promise me you'll keep it between us."
        scene 30_s1 with dissolve
        m "Of course, [mx]! As your wife, I vow to keep your secrets safe."
        scene 30_s2 with dissolve
        mc "I let her go."
        scene 30_s1 with dissolve
        m "I see... If that's the choice you made, I trust it was the right one. You must have had your reasons."
        scene 30_s2 with dissolve
        mc "Thank you, Maia."
        scene 18_s8 with dissolve
        m "I'm always happy to hear you talk, [mx]."
        scene 18_s7 with dissolve
    call screen is_maia with dissolve

label free_roam_maia_talk_ogre_op1:
        mc "Yes, it was an intense battle."
        scene 30_s1 with dissolve
        m "I hope you weren't hurt, [mx]?"
        scene 30_s2 with dissolve
        mc "I wasn't. The ogre was no match for me."
        scene 18_s8 with dissolve
        m "Hehe~ Will you protect me if an ogre attacked me, [mx]?"
        scene 18_s7 with dissolve
        mc "Uh... of course! You'll be the princess that I always rescue."
        scene 30_s10 with dissolve
        m "Princess?!"
        scene 30_s11 with dissolve
        mc "Mhm. I'll protect you, always."
        scene 30_s10 with dissolve
        m "T-Thank you, [mx]!"
        scene 30_s11 with dissolve
        call screen is_maia with dissolve

label free_roam_maia_talk_ogre_op2:
        $ mc_told_maia_ogre_truth = True
        mc "Actually... that story isn't... true."
        scene 18_s8 with dissolve
        m "Huh? What do you mean, [mx]?"
        scene 18_s7 with dissolve
        mc "I lied. I lied to Darius and the Queen."
        scene 30_s1 with dissolve
        m "But... why, [mx]? I-If you don't mind me asking..."
        scene 30_s2 with dissolve
        mc "I guess I just wanted to be recognized... or get some kind of reward for it."
        empathy "Her fingers fidget slightly, but her expression doesn't change. Then, she smiles—small and soft, as if she never doubted you at all."
        scene 18_s8 with dissolve
        m "You don't need to slay an ogre to be great, [mx]."
        scene 18_s7 with dissolve
        mc "...What?"
        scene 18_s8 with dissolve
        m "Even if you didn't kill it this time... you still can."
        m "And even if you never do... what matters is that they believe you did."
        scene 18_s7 with dissolve
        mc "You really think so?"
        scene 18_s8 with dissolve
        m "Yes! Everyone will know your name, one way or another."
        scene 18_s7 with dissolve
        mc "Thank you, Maia."
        call screen is_maia with dissolve

label in_scene64_maia_reb_talk:
    $ in_scene64_maia_reb_talk = True
    if mc_told_maia_nadia_sex:
        if mc_rejected_wedding_reb:
            scene 30_s1 with Dissolve(1.0)
            m "Is it... true, [mx]?"
            scene 30_s2 with dissolve
            mc "About what?"
            scene 30_s1 with dissolve
            m "The princess... she's getting married to you now, right?"
            scene 30_s2 with dissolve
            mc "No. I refused to marry her."
            scene 30_s1 with dissolve
            m "H-Huh? You... you refused to marry the princess?"
            scene 30_s2 with dissolve
            mc "I did. And before you ask—yes, I'm sure. No, I haven't lost my mind. And no, I don't regret it."
            scene 30_s8 with dissolve
            m "But... but why?"
            scene 30_s9 with dissolve
            mc "{i}Why?{/i} I just didn't want to. Why is that such a hard thing to understand here?"
            mc "I barely know the woman."
            scene 30_s1 with dissolve
            m "S-Sorry, [mx]. I didn't mean to question your choices. It's just... surprising. I thought most people would salivate at the chance of marrying a princess."
            scene 30_s2 with dissolve
            mc "*chuckles* Well, I'm not 'most people'."
            scene 30_s10 with dissolve
            m "*giggles* I guess not~"
            scene 30_s11 with dissolve
            call screen is_maia with dissolve
        else:
            scene 18_s8 with Dissolve(1.0)
            m "[mx]! Hello."
            scene 18_s7 with dissolve
            mc "You heard? I'm getting married to Princess Rebecca."
            scene 18_s8 with dissolve
            m "O-Oh... I see. Congratulations, [mx]. I'm happy for you."
            scene 18_s7 with dissolve
            mc "Thank you, Maia."
            scene 18_s8 with dissolve
            m "It's strange... I never thought I'd be sharing you with the princess."
            m "But... it makes me feel proud, too. That you're wanted by someone like her."
            scene 18_s7 with dissolve
            mc "I'll take good care of you both."
            scene 18_s8 with dissolve
            m "Mhm~ I know you will."
            scene 18_s7 with dissolve
            mc "Maybe we could all... share the same bed one day."
            scene 18_s10 with dissolve
            m "Th-the same bed? With... the princess?"
            scene 18_s9 with dissolve
            mc "*laughs* Getting flustered?"
            scene 18_s10 with dissolve
            m "I-I've never seen Princess Rebecca naked... I'd be so nervous..."
            m "But... if that's what you want... I'll try to be good for you both."
            scene 18_s9 with dissolve
            mc "We'll take it slow. You don't have to worry."
            scene 18_s8 with dissolve
            m "As you wish, [mx]."
            scene 18_s7 with dissolve
            call screen is_maia with dissolve
    else:
        scene 30_s1 with Dissolve(1.0)
        m "Is it... true, [mx]?"
        scene 30_s2 with dissolve
        mc "About what?"
        scene 30_s1 with dissolve
        m "The princess... she's getting married to you now, right?"
        scene 30_s2 with dissolve
        if not mc_rejected_wedding_reb:
            mc "That's right. News travels fast, huh?"
            scene 30_s1 with dissolve
            m "I see."
            scene 30_s2 with dissolve
            mc "It was the Queen's wish, Maia. This will protect us, you included. I couldn't exactly refuse a queen."
            scene 30_s4 with dissolve
            m "I know you carry many burdens, [mx]... and I want to be strong for you."
            m "I... I will accept it. If this is your path, then I will walk it too, as long as I may stay by your side."
            scene 30_s5 with dissolve
            mc "You will, Maia. You're precious to me. Nothing changes that."
            scene 18_s10 with dissolve
            m "Just... Just promise me that I'll in your number one spot!"
            scene 18_s9 with dissolve
            mc "*laughs* Deal."
            scene 18_s10 with dissolve
            m "Does this also mean... you'll be with others as well from now on?"
            m "I know some men have... more than one. I just never thought... well, I never thought I'd marry someone important enough for it to matter."
            scene 18_s9 with dissolve
            $ mc_maia_monogamous_question = True
            call screen scene18_choice_maia with dissolve
        else:
            mc "No. I refused to marry her."
            scene 30_s1 with dissolve
            m "H-Huh? You... you refused to marry the princess?"
            scene 30_s2 with dissolve
            mc "I did. And before you ask—yes, I'm sure. No, I haven't lost my mind. And no, I don't regret it."
            scene 30_s8 with dissolve
            m "But... but why?"
            scene 30_s9 with dissolve
            mc "{i}Why?{/i} I just didn't want to. Why is that such a hard thing to understand here?"
            mc "I barely know the woman."
            scene 30_s1 with dissolve
            m "S-Sorry, [mx]. I didn't mean to question your choices. It's just... surprising. I thought most people would salivate at the chance of marrying a princess."
            scene 30_s2 with dissolve
            mc "*chuckles* Well, I'm not 'most people'."
            scene 30_s10 with dissolve
            m "*giggles* I guess not~"
            scene 30_s11 with dissolve
            call screen is_maia with dissolve

label scene18_choice_maia_op1:
    $ mc_maia_monogamous = True
    $ mc_told_maia_nadia_sex = False
    mc "No, Maia. Marrying Rebecca wasn't my choice. The Queen decided it on a whim to keep me close."
    mc "If I'd had any say, I wouldn't have. You're the only one I want. The only one I need."
    scene 18_s7 with dissolve
    empathy "Her shoulders relax, the tension melting from her face. A fragile, radiant smile blooms."
    scene 18_s8 with dissolve
    m "Thank you, [mc]. Truly... from the bottom of my heart."
    m "But... please don't feel pressured to do this for me. I want you to be happy first and foremost."
    scene 30_s11 with dissolve
    mc "I'm saying it because I mean it."
    call screen is_maia with dissolve

label scene18_choice_maia_op2:
    $ mc_maia_monogamous = False
    $ mc_told_maia_nadia_sex = True
    mc "Yes, Maia. I won't lie to you and break your heart later with the truth."
    m "..."
    scene 30_s4 with dissolve
    m "It's... exciting to know someone as important as the princess wants you too..."
    scene 30_s5 with dissolve
    mc "*chuckles* Maia...?"
    scene 18_s10 with dissolve
    m "D-don't tease! I'm trying to be understanding!"
    scene 18_s9 with dissolve
    call screen is_maia with dissolve

label yuuhi_talk_maia_choice_love:
    $ mc_told_yuuhi_love_maia = True
    mc "I love her a lot. I think we fit each other really well."
    yuuhi "..."
    mc "Yuuhi?"
    scene 31_s19 with dissolve
    yuuhi "Ngh... I'm having really weird feelings..."
    scene 31_s20 with dissolve
    empathy "Telling a woman who loves you that you love another woman is a bad idea ninety nine percent of time."
    mc "I love her, but I also love you, Yuuhi. Both of you."
    scene 31_s15 with dissolve
    yuuhi "I... You really know how to get me..."
    scene 31_s16 with dissolve
    mc "Thank you. Maybe one day you two will meet."
    scene 31_s17 with dissolve
    yuuhi "Yeah, I don't think so."
    scene 31_s18 with dissolve
    perception "Her voice shifts—suddenly firmer, more serious."
    mc "Why not?"
    scene 31_s17 with dissolve
    yuuhi "She can have you in {i}her{/i} house, for a limited time. But {i}our{/i} place will be separate."
    scene 31_s18 with dissolve
    mc "You're quite serious about this, aren't you?"
    scene 31_s17 with dissolve
    yuuhi "I am."
    scene 31_s18 with dissolve
    call screen is_yuuhi with dissolve

label yuuhi_talk_maia_choice_hate:
    $ mc_told_yuuhi_hate_maia = True
    mc "This marriage was forced on me. I don't love her. I try my best to avoid her."
    scene 31_s19 with dissolve
    yuuhi "[mc]..."
    scene 31_s20 with dissolve
    mc "What's wrong?"
    scene 31_s19 with dissolve
    yuuhi "Did you ever think about how she feels? What if she was forced into it too?"
    yuuhi "You should talk to her... maybe get divorced or something."
    scene 31_s20 with dissolve
    mc "*sigh* It isn't that simple."
    scene 31_s15 with dissolve
    yuuhi "So... d-does that mean you only love me?"
    scene 31_s16 with dissolve
    mc "Yes. Only you."
    yuuhi "Mhmm~"
    call screen is_yuuhi with dissolve

label free_roam_yuuhi_nope:
    mc "(I guess I could check on her... Wait, didn't I tell her I wasn't interested in her? Probably shouldn't go there until my armor's ready, anyway.)"
    call screen free_roam_choices with dissolve

label free_roam_maia_left:
    $ mc_maia_left_talk = True
    perception "You instinctively look right to where Maia would usually be, standing and staring through that window with a dazzled look on her face."
    perception "However, this time, no one's there."
    call screen free_roam_choices with dissolve

label scene35_choice03_op2_2:
    mc "I'm still not going to do that."
    scene 35_s22 with dissolve
    r "Then why the hell are you here?"
    scene 35_s21 with dissolve
    mc "What if I just wanted some fresh air? Ease off..."
    scene 35_s30 with dissolve
    r "Do {i}not{/i} talk to me like that. Know your place."
    scene 35_s31 with dissolve
    mc "*sigh*"
    jump free_roam_main_label

default mc_reb_first_talk_ = False
label free_roam_reb_first:
    if free_roam_reb_first:
        $ free_roam_reb_first = False
        $ mc_roam_reb_break = True
        stop music fadeout 2.0
        scene irda_roof with Fade(0.5,0.5,1.5)
        play music "wind.mp3" fadein 2.0 loop
        sensation "The air hits as soon as you step out—gentle and breezy. For a brief moment, the scent takes you back to simpler days."
        scene 35_s20 with fade
        mc "Princess."
        r "..."
        scene 35_s21 with dissolve
        mc "Princess?"
        r "..."
        call screen scene35_choice01 with dissolve

    $ mc_reb_first_talk_ = True
    scene irda_roof with Fade(0.5,0.5,1.5)
    ""
    play music "wind.mp3" fadein 2.0 loop
    scene 35_s22 with dissolve
    r "What do you want? I'm busy here. Talk to my mom if you want your next task or whatever."
    scene 35_s21 with dissolve
    mc "What are you reading?"
    scene 35_s22 with dissolve
    r "None of your business."
    scene 35_s21 with dissolve
    mc "Why are you always so mean?"
    scene 35_s22 with dissolve
    r "*sigh* It's a story about a man and a woman falling in love."
    scene 35_s21 with dissolve
    mc "Sounds... bland. There has to be more to this story, right?"
    scene 35_s22 with dissolve
    r "Ugh, you really want to know? Fine. The man's a mercenary leader who came to the city to aid the king in battle."
    r "While he's talking with the king, he spots the princess. She's all shy and timid."
    scene 35_s21 with dissolve
    mc "Wait, he's a mercenary leader?"
    scene 35_s22 with dissolve
    r "Mhm. One day, while walking back to his band, he sees her walking toward him... thing is, she falls for him almost instantly."
    r "He, on the other hand, is all broody and mysterious—of course—but she sees past it, and they end up getting really close."
    scene 35_s21 with dissolve
    mc "Hold on, this sounds like it's got more than just a 'falling in love' part. What happens next?"
    scene 35_s22 with dissolve
    r "Well, she really has to trust him because it's dangerous. There's a conspiracy to take the throne, and they go through a lot of stuff together, but they don't give up."
    scene 35_s21 with dissolve
    mc "That doesn't sound so bland now..."
    scene 35_s28 with dissolve
    r "I told you! It's not just the plot, it's the way they care for each other. It's... real. Not like the fake stuff people think love is. They trust each other even when everything is falling apart."
    scene 35_s29 with dissolve
    mc "So, you really believe in this kind of love?"
    scene 35_s60 with dissolve
    r "I... I think it's real. At least in books. I guess, with all the things I've seen... it's hard to believe love like that exists outside of stories."
    scene 35_s61 with dissolve
    perception "Her voice becomes softer, almost hushed."
    mc "You've never really seen it in real life?"
    scene 35_s60 with dissolve
    r "No. Not like this. People always want something from each other, or... they hide what they really feel. It's... rare to see someone actually trust another like that."
    scene 35_s61 with dissolve
    mc "I get that. But, you know, it's not impossible. Some things aren't as fake as you think."
    scene 35_s60 with dissolve
    r "Maybe..."
    scene 35_s58 with dissolve
    r "Hey... [mc]."
    scene 35_s59 with dissolve
    mc "What's up?"
    scene 35_s58 with dissolve
    r "You're... not too bad."
    scene 35_s59 with dissolve
    mc "*chuckles* Thank you."
    scene 35_s58 with dissolve
    r "Now if you don't mind, [mc], I would really love to be alone."
    r "But... thank you for listening."
    scene 35_s59 with dissolve
    mc "I'm always here, princess."
    jump free_roam_main_label
    
label free_roam_maia_reb_wed:
    $ mc_talked_maia_wed_reb = True
    scene 30_s1 with dissolve
    m "[mx]... So you really want to marry princess rebecca..."
    scene 30_s2 with dissolve
    mc "Yes. I'm sorry I didn't tell you earlier, Maia."
    scene 30_s4 with dissolve
    m "I-I see."
    scene 30_s5 with dissolve
    mc "Are you okay?"
    scene 30_s4 with dissolve
    m "Yes."
    scene 30_s5 with dissolve
    mc "Maia, you don't have to pretend—"
    scene 30_s4 with dissolve
    m "I'm not pretending, [mx]. I understand. I really do."
    scene 30_s5 with dissolve
    mc "Listen, if it makes you feel any better... I still love you. This doesn't change anything."
    m "..."
    scene 30_s4 with dissolve
    m "It's fine. I will get used to it, [mx]."
    scene 30_s5 with dissolve
    call screen is_maia with dissolve

label free_roam_reb_talk_maia:
    $ mc_told_reb_maia = True
    mc "Hey, about Maia."
    if not mc_maia_left:
        scene 63_s5 with dissolve
        r "What about her?"
        scene 63_s6 with dissolve
        mc "You told me to let you know if I took another wife... before you, you know—killed me."
        scene 63_s5 with dissolve
        r "I already know about her, dummy."
        scene 63_s6 with dissolve
        mc "Alright, good."
        scene 63_s5 with dissolve
        r "You better be treating her right."
        scene 63_s6 with dissolve
        mc "I am. You seem fond of her."
        scene 63_s5 with dissolve
        r "Of course I am. She's my favorite. That's why I was so against handing her over to you in the first place."
        scene 63_s6 with dissolve
        mc "How long have you two known each other?"
        scene 63_s5 with dissolve
        r "Couple of years, give or take. No matter how much training she gets, she's still the same shy little thing."
        scene 63_s6 with dissolve
        mc "I've noticed... she keeps to herself a lot."
        scene 63_s5 with dissolve
        r "She probably had it rough. I never asked. I don't think she'd tell you either, if you're expecting some tragic confession."
        scene 63_s6 with dissolve
        mc "She hasn't said anything. I wish she would. Maybe I could help."
        scene 63_s5 with dissolve
        r "Some things... can't be helped, [mc]. Sometimes forgetting is kinder."
        scene 63_s6 with dissolve
        mc "I don't know if I agree with that."
        scene 63_s5 with dissolve
        r "Of course you don't. You're soft underneath it all."
        scene 63_s6 with dissolve
        mc "Says the woman who threatened to murder me the other day."
        scene 63_s1 with dissolve
        r "*laughs* And I still might. But until then... just keep taking care of her."
        scene 63_s2 with dissolve
        mc "I will."
    else:
        scene 63_s1 with dissolve
        r "What about her?"
        scene 63_s2 with dissolve
        mc "You told me to let you know if I took another wife... before you, you know—killed me."
        scene 63_s1 with dissolve
        r "Didn't she already leave you?"
        scene 63_s3 with dissolve
        r "Why was that by the way?"
        scene 63_s4 with dissolve
        mc "We just... didn't fit each other well."
        scene 63_s3 with dissolve
        r "I see. She's really sensitive you know?"
        r "You better have not broken her heart."
        scene 63_s4 with dissolve
        mc "I'm not sure. I think she's doing better now."
        r "Hmm..."
    call screen is_reb with dissolve

label free_roam_reb_talk_yuuhi:
    $ mc_told_reb_yuuhi = True
    mc "There's another girl I'm considering marrying."
    scene 63_s5 with dissolve
    r "Oh? Who is she?"
    scene 63_s6 with dissolve
    mc "Her name's Yuuhi. She works at the blacksmith—she's a tailor."
    scene 63_s5 with dissolve
    r "Ah. Alright."
    scene 63_s6 with dissolve
    mc "..."
    mc "That's it?"
    scene 63_s1 with dissolve
    r "What?"
    scene 63_s2 with dissolve
    mc "I thought you'd be... a little jealous."
    scene 63_s1 with dissolve
    r "Oh-ho~ Don't mistake my composure. I'm ready to explode any minute now. But it's expected for royalty to have multiple wives or mistresses, isn't it?"
    scene 63_s2 with dissolve
    mc "I see... Well, if anything, she's really sweet. And weird. You might actually like her."
    scene 63_s1 with dissolve
    r "Sure."
    scene 63_s2 with dissolve
    mc "She's also—"
    scene 63_s3 with dissolve
    r "{i}Dear husband.{/i} Let's change the subject."
    scene 63_s4 with dissolve
    mc "...Got it."
    call screen is_reb with dissolve

label free_roam_reb_talk_diana:
    $ mc_told_reb_diana = True
    mc "There's a girl I... did the dirty with."
    scene 63_s3 with dissolve
    r "Great. I just {i}love{/i} hearing that."
    scene 63_s4 with dissolve
    mc "Don't get sassy. You told me to be upfront about these things."
    scene 63_s3 with dissolve
    r "*sigh* Fine. Who is she?"
    scene 63_s4 with dissolve
    mc "Diana. The brothel worker."
    scene 63_s3 with vpunch
    r "Her?! Of all people? Really?!"
    scene 63_s4 with dissolve
    mc "What's wrong?"
    scene 63_s3 with dissolve
    r "I just thought... it was above you to go around sleeping with {i}whores.{/i}"
    scene 63_s4 with dissolve
    mc "Well... sometimes, anyone will do."
    scene 63_s3 with dissolve
    r "You know what kind of reputation that brings, right?"
    scene 63_s4 with dissolve
    mc "I don't really care about that."
    r "..."
    scene 63_s3 with dissolve
    r "*sigh* Gods... listen to me. I sound just like my mother..."
    r "...Whatever. Thanks for telling me, I guess."
    scene 63_s4 with dissolve
    call screen is_reb with dissolve

label free_roam_market2:
    if mc_coin >= reham_price and mc_inspected_reham:
        mc "(I have enough to buy that servant now. I should go out and see her sometime later.)"
    else:
        mc "(No reason to go there for now.)"
    call screen free_roam_choices with dissolve

default diana_harem_chance_talk_pepo = False

label diana_harem_chance:
    $ is_diana_first_time_talk = False
    $ diana_harem_chance_talk_pepo = True
    scene 7_s31 with dissolve
    mc "Hey, Diana. How are you doing?"
    scene 7_s30 with dissolve
    di "[mc]! You're back."
    scene 7_s31 with dissolve
    mc "Yeah. Why wouldn't I be? I've been here almost everyday now."
    scene 7_s30 with dissolve
    di "I... wasn't sure if you'd want to see me again."
    scene 7_s31 with dissolve
    mc "Why wouldn't I? Did I leave such a bad impression?"
    scene 7_s30 with dissolve
    di "No! Not bad. Just... intense. I've been replaying it in my head ever since."
    scene 7_s31 with dissolve
    mc "Is that so? Sounds like I left more of a mark than I thought."
    scene 7_s30 with dissolve
    di "[mc]... can I ask you something?"
    scene 7_s31 with dissolve
    mc "Go ahead."
    scene 7_s30 with dissolve
    di "I know I shouldn't. As a brothel worker, it's... not really my place to ask customers things like this. It's supposed to just be my job."
    di "But like I told you before between us, there was never any customers."
    di "And I know we barely know each other, but that night... when you touched me, when you said those things to me... it felt like it meant something more. And now I can't stop wondering..."
    scene 7_s29 with dissolve
    di "What are we, [mc]?"
    scene 7_s28 with dissolve
    mc "..."
    call screen scene07_choice01 with dissolve

label scene07_choice01_op1:
    $ mc_harem_diana = True
    mc "Lovers."
    di "..."
    mc "Diana? Did I say something wrong?"
    scene 7_s26 with dissolve
    di "Do you... do you really mean it? You're not just saying it because you think I want to hear it?"
    scene 7_s27 with dissolve
    mc "I do. I wouldn't say it if I didn't."
    scene 7_s26 with dissolve
    di "Gods... I wasn't sure if you would. When you left, I kept telling myself it was just a night. That I was just... convenient."
    scene 7_s27 with dissolve
    mc "You weren't."
    scene 7_s26 with dissolve
    di "Then... we're truly lovers? Not just by flesh, but... in heart?"
    scene 7_s27 with dissolve
    mc "In heart. In flesh. In whatever way matters. You and me."
    scene 7_s30 with dissolve
    di "*laughs* You don't know how much I needed to hear that. I've been waiting for someone to say those words to me for years."
    scene 7_s31 with dissolve
    mc "I'll say it to you everyday."
    scene 7_s30 with dissolve
    di "Fool... you'll spoil me if you keep saying things like that."
    scene 7_s31 with dissolve
    mc "Maybe I want to spoil you. You've been working yourself to the bone, taking care of everyone except yourself. Let someone take care of you for a change."
    scene 7_s30 with dissolve
    di "Then promise me, [mc]... you won't cast me aside."
    scene 7_s31 with dissolve
    mc "I promise."
    scene 7_s22 with dissolve
    di "*sigh* Good... then let me tell you something else. Something I've been dreaming about for a long time."
    scene 7_s23 with dissolve
    mc "What is it?"
    scene 7_s32 with Dissolve(1.0)
    di "I've been thinking a lot about my life here. I don't want to stay a working girl forever. Especially now that I have you." 
    di "I want to buy this brothel from Vera someday and turn it into a regular tavern."
    scene 7_s33 with dissolve
    mc "That's... ambitious."
    scene 7_s32 with dissolve
    di "*laughs* Isn't it? Right now I can barely afford three meals a day."
    di "I've been saving coppers in a jar under my bed, but at this rate, I'll be sixty before I have enough. But... that's where you come in."
    scene 7_s33 with dissolve
    mc "Me?"
    scene 7_s32 with dissolve
    di "I want you to keep choosing me. Keep asking for me."
    di "The coin goes toward my savings—Vera takes her cut, but I get a percentage. And if I'm the one you always request, that percentage grows."
    scene 7_s33 with dissolve
    mc "Wouldn't it be easier if I just gave you the coin outright?"
    scene 7_s32 with dissolve
    di "D-Do you have the coin?!"
    scene 7_s33 with dissolve
    mc "Not yet. But I'll get there eventually."
    mc "How much is Vera asking for this place?"
    scene 7_s22 with dissolve
    di "Twenty gold coins."
    scene 7_s23 with dissolve
    mc "Twenty!? That's... that's a fortune!"
    scene 7_s24 with dissolve
    di "*giggles* Hey! Don't lose hope yet. Dreams don't come true overnight."
    scene 7_s25 with dissolve
    mc "Right... I guess I'll just have to keep 'ordering services' until then."
    scene 7_s24 with dissolve
    di "Services? That sounds so cold. Let's call it what it really is... making love."
    scene 7_s25 with dissolve
    mc "Making love it is. But what about the others?"
    scene 7_s24 with dissolve
    di "Don't worry. No other man will touch me from now on. Not if you're truly mine. And... I doubt I'll get requested anyway."
    di "This body belongs to you, [mc]... only you. Every curve and every scar."
    scene 7_s25 with dissolve
    mc "Good. I wouldn't have it any other way."
    scene 7_s24 with dissolve
    di "Then... care to make love now, darling~?"
    scene 7_s25 with dissolve
    jump diana_harem_chance2

label scene07_choice01_op2:
    $ mc_friend_diana = True
    mc "Friends."
    scene 7_s29 with dissolve
    di "Right..."
    scene 7_s28 with dissolve
    mc "Diana—"
    scene 7_s29 with dissolve
    di "No, it's fine. Truly. I suppose I expected too much after so little."
    scene 7_s28 with dissolve
    mc "It wasn't meaningless. What we shared... I meant it in that moment. But if I called us lovers, it wouldn't be honest."
    scene 7_s26 with dissolve
    di "You've a cruel way of being kind, you know that?"
    scene 7_s27 with dissolve
    mc "I'd rather be cruel in truth than tell lies."
    scene 7_s30 with dissolve
    di "Hah... then at least I know you're not the sort of man to play with me."
    scene 7_s31 with dissolve
    mc "Never. If friendship is what you'll allow me, then I'll take it gladly. Better that than nothing at all."
    scene 7_s30 with dissolve
    di "Then friends we are. Nothing more, nothing less."
    scene 7_s31 with dissolve
    mc "That doesn't mean I don't care about you, Diana."
    scene 7_s30 with dissolve
    di "I know..."
    scene 7_s31 with dissolve
    empathy "The air is heavy; she forces a small laugh, as though to lighten it, but the silence that follows lingers long after."
    scene 7_s22 with dissolve
    di "*sigh* I want to ask you something else."
    scene 7_s23 with dissolve
    mc "What is it?"
    scene 7_s32 with dissolve
    di "I've been thinking a lot about my life here. I don't want to stay a working girl forever. Especially now that I have you." 
    di "I want to buy this brothel from Vera someday and turn it into a regular tavern."
    scene 7_s33 with dissolve
    mc "That's... ambitious."
    scene 7_s32 with dissolve
    di "*laughs* Isn't it? Right now I can barely afford three meals a day."
    di "I've been saving coppers in a jar under my bed, but at this rate, I'll be sixty before I have enough. But... that's where you come in."
    scene 7_s33 with dissolve
    mc "Me?"
    scene 7_s32 with dissolve
    di "I want you to keep choosing me. Keep asking for me."
    di "The coin goes toward my savings—Vera takes her cut, but I get a percentage. And if I'm the one you always request, that percentage grows."
    scene 7_s33 with dissolve
    mc "Wouldn't it be easier if I just gave you the coin outright?"
    scene 7_s32 with dissolve
    di "D-Do you have the coin?"
    scene 7_s33 with dissolve
    mc "Not yet. But I'll get there eventually."
    mc "How much is Vera asking for this place?"
    scene 7_s22 with dissolve
    di "Twenty gold coins."
    scene 7_s23 with dissolve
    mc "Twenty!? That's... that's a fortune!"
    scene 7_s22 with dissolve
    di "*giggles* Hey! Don't lose hope yet. Dreams don't come true overnight."
    scene 7_s23 with dissolve
    mc "Right... I guess I'll just have to keep 'ordering services' until then."
    scene 7_s22 with dissolve
    di "Will you help me atchive my grand ambition?"
    scene 7_s23 with dissolve
    mc "We'll see. I won't promise anything."
    scene 7_s24 with dissolve
    di "Of course. Just anytime you're free, come visit for a quickie~"
    scene 7_s25 with dissolve
    jump diana_harem_chance2

label scene07_choice01_op3:
    mc "We? There's no we, Diana."
    di "..."
    scene 7_s29 with dissolve
    di "Of course. I was stupid for thinking otherwise."
    scene 7_s30 with dissolve
    di "*sigh* I apologize for that, [mc]. What'll it be for today?"
    scene 7_s31 with dissolve
    $ mc_harem_diana_chance = False
    call screen is_diana

label diana_harem_chance2:
    $ mc_harem_diana_chance = False
    evrart_ "Over my dead body!"
    scene 7_s26 with dissolve
    di "Oh, dear..."
    scene 7_s27 with dissolve
    scene 7_s35 with Dissolve(1.0)
    di "Please, Evrart... This time it isn't like that!"  
    scene 7_s36 with dissolve
    evrart "You don't know nothin', sweetheart. These men are here for only one thing!"
    evrart "They sweet-talk you, they promise you the moon, and then they're gone before sunrise, leaving you with nothing but a broken heart!"
    scene 7_s35 with dissolve
    di "He isn't like that! And besides, I'm not a child anymore. You can stop with this overprotective guardian act."  
    di "It was charming when I was sixteen. Now it's just... exhausting."
    scene 7_s36 with dissolve
    if mc_harem_diana:
        evrart "Tch! Children always say that right before they get swindled. And what kind of man says 'lover' and then hops in bed before proving his worth?"  
    else:
        evrart "Tch! Children always say that right before they get swindled. And what kind of man says 'friend' and then hops in bed before proving his worth?"  
    scene 7_s35 with dissolve
    mc "Wait—"  
    scene 7_s36 with dissolve
    evrart "Shut it! If you're serious about Diana, then you'll prove it the proper way. The old way."
    scene 7_s35 with dissolve
    mc "Proper way? What are you talking about?"  
    scene 7_s36 with dissolve
    evrart "Arm wrestling."  
    scene 7_s35 with dissolve
    mc "....Arm wrestling? That's your test of character? {i}Arm wrestling?{/i}"  
    scene 7_s37 with dissolve
    evrart "That's right. Two men. One table. One winner. And if you lose, you walk away from the girl forever!"  
    scene 7_s35 with dissolve
    di "Evrart, you can't just—this isn't some tavern brawl! He's a hero!"  
    scene 7_s36 with dissolve
    evrart "Hush, princess! This is tradition. The ancient art of deciding manliness!"
    scene 7_s35 with dissolve
    mc "Pretty sure that's just called insecurity. And also, I think you're making up that tradition."
    scene 7_s36 with dissolve
    evrart "And I'm pretty sure you're about to get your hand crushed."  
    evrart "Sit down, boy. Let's see what those hands are made of."
    if mc_got_armor:
        scene 7_s39 with Dissolve(1.0)
    else:
        scene 7_s38 with Dissolve(1.0)
    di "{size=30}[mc], don't be fooled by his age. Evrart was a seasoned knight. He served under Queen Hannah's father.{/size}"
    di "{size=30}No one was ever able to defeat him at arm wrestling during his prime.{/size}"
    mc "{size=30}Seriously!?{/size}"  
    di "{size=30}Mhm. Don't go easy on him. Well... Don't go too hard either. He's still an old man afterall.{/size}"  
    evrart "What's wrong, boy? Too scared to show your girly hands?"  
    scene 7_s35 with dissolve
    mc "Fine, but just so you know—if I win, you'll stop treating me like some scoundrel."  
    scene 7_s36 with dissolve
    evrart "{i}If{/i} you win, boy, I'll start treatin' you like a man. Until then, you're just a stray dog sniffin' after scraps." 
    scene 7_s35 with dissolve
    if mc_got_armor:
        scene 7_s41 with Fade(1.0,1.0,1.0)
    else:
        scene 7_s40 with Fade(1.0,1.0,1.0)
    di "This is ridiculous... but go, go [mc]!"  
    evrart "Count it down, sweatbee."  
    di "Three... Two... One... Go!"
    scene 7_s44 with vpunch
    evrart "Hnnngh! Not bad... you've got some strength in ya. More than I expected from a pretty boy."  
    scene 7_s43 with dissolve
    mc "You're not bad yourself... for a fossil!"  
    scene 7_s44 with dissolve
    evrart "Fossil?! Boy, I was breaking backs before you were even born! I wrestled a cave troll once!"  
    scene 7_s43 with dissolve
    mc "Yeah? Well, you're about to break your wrist!"
    evrart "..."
    sensation "His grip begins to weaken. Sweat forming on his brow."
    scene 7_s44 with dissolve
    evrart "Nghhh! Impossible! How are you... this strong!?"  
    play sound "sound_effects/slam_wood.mp3"
    if mc_got_armor:
        scene 7_s46 with vpunch
    else:
        scene 7_s45 with vpunch
    mc "HAH! Victory!"  
    evrart "Ghh... damn it all..." 
    scene 7_s36 with Fade(1.0,1.0,1.0)
    evrart "Fine... you've got guts. Maybe you ain't just another bastard after all." 
    scene 7_s35 with dissolve
    mc "So you'll finally accept me?"
    scene 7_s36 with dissolve
    evrart "...I'll think about it."  
    scene 7_s35 with dissolve
    mc "Good enough."
    scene 7_s36 with dissolve
    evrart "Still don't like the way you look at her... too much hunger in those eyes."  
    evrart "Diana, you keep an eye on this one. If he ever breaks your heart, you come find me."
    scene 7_s35 with dissolve
    scene 7_s48 with Dissolve(1.0)
    di "Good job, [mc]! You're really strong~"
    if mc_harem_diana:  
        scene 7_s47 with dissolve    
        mc "Thank you—"
        play sound "se_sfx/blowjob/kiss1.mp3" 
        if mc_got_armor:
            scene 7_s50 with Dissolve(1.0)
        else:
            scene 7_s49 with Dissolve(1.0)
        di "Mmm~"
        evrart "Eghhh..."  
    if mc_harem_diana:
        scene 7_s48 with Dissolve(1.0)
        di "Heh~ I guess it's official now."
        di "I was dreading bringing this up to Evrart..."
        scene 7_s47 with dissolve
        mc "No man is keeping me away from you."
        scene 7_s48 with dissolve
        di "*giggles* I guess not~"
    elif mc_friend_diana:
        di "Heh~ I guess our friendship is official now."
        di "I was dreading bringing this up to Evrart..."
        scene 7_s47 with dissolve
        mc "No man is keeping me away from you."
        scene 7_s48 with dissolve
        di "*giggles* I guess not~"
    scene 7_s47 with dissolve
    scene 7_s24 with Fade(1.0,1.0,1.0)
    di "Shall we~?"
    scene 7_s25 with dissolve
    call screen is_diana with dissolve

label scene31_nope:
    mc "(I should check out the market first before heading out.)"
    call screen free_roam_choices with dissolve

default brothel_coin_new = 2000

default brothel_coin = 2000
default brothel_offer_coin = 0
default brothel_first_offer = True
label is_diana_buy_brothel:
    if not brothel_coin_new <= 0:
        mc "(Coin needed to purchase the brothel is [brothel_coin_new])"
        mc "(Should I give her some coin?)"

        if mc_coin <= 0: 
            mc "(Wait... I don't have any coin to offer her anyway.)"
        else:
            $ offer = renpy.input("How much should I give her? (Enter 0 to cancel)")
            $ offer = int(offer) if offer.isdigit() else 0
            
            if offer > mc_coin:
                mc "(I don't have that much coin!)"
            elif offer < 0:
                mc "(Yup, great. I'll just give her negative coins. That'll surely help her...)"
            elif offer == 0:
                mc "(Nevermind.)"
            else:
                $ brothel_offer_coin += offer
                $ mc_coin -= offer
                $ brothel_coin_new -= offer
                mc "(I gave her [offer] coin. The remaining cost should be [brothel_coin_new])"
                mc "Here you go, Diana."
                if brothel_first_offer:
                    $ brothel_first_offer = False
                    scene 7_s26 with dissolve
                    di "[mc]! Thank you but... I suddenly feel terrible for having you do this for me."
                    scene 7_s27 with dissolve
                    mc "Don't worry about it. I'm happy to help."
                    scene 7_s30 with dissolve
                    di "Thank you."
                    scene 7_s31 with dissolve
                else:
                    scene 7_s30 with dissolve
                    di "Thank you, [mc]! A-Are you sure this isn't a liability to you?"
                    scene 7_s31 with dissolve
                    mc "It's fine. I promise."
                if brothel_coin_new <= 0:
                    "Cheater!"
                    "Regardless if you cheated or not. This part of the game isn't implemented yet. :)"
            call screen is_diana with dissolve
    else:
        "Nope."
        call screen is_diana with dissolve

label mc_harem_talk_nadia_no:
    mc "(I should go to the market and speak with Nadia first.)"
    call screen free_roam_choices

label mc_harem_talk_nadia:
    $ mc_harem_talk_nadia = True
    play music "market2.mp3" fadein 2.0 loop
    scene 29_1_s1 with Fade(1.0,1.0,1.0)
    mc "Hey, Nadia. How's business?"  
    scene 29_1_s3_2 with Dissolve(1.0)
    ml "Oh, [mc]... It's going well, thanks to you. I've sold more milk yesterday than I did all last month."  
    ml "Word got around that Viktor's men stopped harassing me, and suddenly everyone wants to buy from the milkmaid again. Funny how that works."
    scene 29_1_s3 with dissolve
    mc "Glad to hear it. And uh... you're still wearing this outfit."
    scene 29_1_s3_2 with dissolve
    ml "Only for now. I plan to change into something less... revealing, once I've built a steady customer base."  
    scene 29_1_s3 with dissolve
    mc "You'll still look great in whatever you choose. Just maybe with fewer people staring."
    scene 29_1_s9 with dissolve
    ml "[mc]... I'm sorry for walking away last time, when you told me how you felt. I just... panicked. And I've been thinking about it ever since."
    scene 29_1_s10 with dissolve
    mc "You needed space. I get it. I threw a lot at you all at once."  
    scene 29_1_s9 with dissolve
    ml "The truth is... I've never had anyone confess to me before. Not like that. Not with real feeling behind it."  
    scene 29_1_s3_2 with dissolve
    ml "But... I've thought about it. And I accept you, [mc]! I want to be with you! I don't want to let fear push away the best thing that's ever happened to me."  
    scene 29_1_s3 with dissolve
    mc "Really? You mean it? *chuckles* You're not going to run off this time?"
    scene 29_1_s3_2 with dissolve
    ml "Yes. At first, I hesitated because you seem... a little younger than me. But I can't let this chance slip away."  
    scene 29_1_s3 with dissolve
    mc "Younger? How much younger are we talking?"  
    scene 29_1_s3_2 with dissolve
    ml "Just one more month before I reach thirty-four. Haha... Time sure flies, huh?"
    scene 29_1_s3 with dissolve
    mc "Seriously? You don't look any older than me."  
    scene 29_1_s3_2 with dissolve
    ml "*chuckles* Thank you. I suppose I'm just worried... about getting too old before I have children."
    scene 29_1_s3 with dissolve
    mc "Hey, you still have plenty of time."
    mc "Women usually begin menopause around... I actually don't know."
    scene 29_1_s3_2 with dissolve
    ml "Around fifty, last I heard from the clerks."
    scene 29_1_s11 with Dissolve(1.0)
    ml "Umm... [mc]. Would you like to come with me?"  
    scene 29_1_s12 with dissolve
    mc "To your house?"  
    scene 29_1_s11 with dissolve
    ml "*laughs* Yes! Why not start now? I want children, and we're both here. So... what are we waiting for?"  
    scene 29_1_s12 with dissolve
    mc "You mean... start making children now?! Right now? Today?" 
    scene 29_1_s11 with dissolve
    ml "Mhm. Forgive me if I'm rushing, but missing my chance... it's the kind of thought that keeps me awake at night."  
    ml "I lie in bed and stare at the ceiling and think about all the years I've spent alone. All the years I might still spend alone if I don't act."
    scene 29_1_s12 with dissolve
    mc "You seriously want to do it now? No dinner first?"
    scene 29_1_s11 with dissolve
    ml "Yes. I even considered joining the arranged marriage matches her majesty sponsors... but I won't be needing that anymore, now that you're here."
    ml "So... will you come over to my home? I can close early today."  
    scene 29_1_s12 with dissolve  
    call screen scene29_choice000000 with dissolve

label scene29_choice000000_op2:
    mc "Maybe another time, Nadia."  
    scene 29_1_s9 with dissolve
    ml "Aww... are you busy right now?"  
    scene 29_1_s10 with dissolve
    mc "Yeah, there's a lot I still need to take care of."  
    scene 29_1_s9 with dissolve
    ml "Hmph... I suppose I'll forgive you. But don't keep me waiting too long, alright?"  
    scene 29_1_s10 with dissolve
    mc "Got it."
    mc "I'll see you soon, Nadia."
    scene 29_1_s3_2 with dissolve
    ml "*winks* See you~"
    scene 29_1_s3 with dissolve
    scene black with Fade(1.0,1.0,1.0)
    jump free_roam_main_label

label scene29_choice000000_op1: 
    #if mc accepts
    $ mcname = persistent.name
    if persistent.name == "None" or mcname == "None":
        while mcname == "None" or mcname == "":
            $ mcname = renpy.input("There was an issue with your name. Please rewrite your name:", length=32)
        $ persistent.name = mcname
    if not persistent.scene1_p2_replay:
        $ persistent.scene1_p2_replay = True
    $ mc_fucked_nadia = True
    scene 29_1_s12 with dissolve
    mc "Of course! Do you really think I'd pass up a chance like this?"  
    scene 29_1_s3_2 with dissolve
    ml "Easy now... I'm not exactly experienced. Don't want you to break me."
    scene 29_1_s3 with dissolve
    mc "That so? I'll be gentle."
    scene 29_1_s3_2 with dissolve  
    ml "*giggles* Come here."  
    scene 29_1_s3 with dissolve
    scene 29_1_s13 with Fade(0.5,0.5,0.5)
    perception "Her fingers wrap around your hand, tugging you toward her with surprising strength. It's obvious she's been longing for this more than she dared to admit."      
    stop music fadeout 3.0
    scene 29_1_s15 with Fade(1.0,1.0,2.0)
    ml "Hah... hahh..."
    scene 29_1_s14 with dissolve
    mc "Wow... You really want this, huh? You're practically trembling."  
    scene 29_1_s15 with dissolve
    ml "Sorry if I tugged on you too tightly but yes... I've always dreamt of having children, [mc]."  
    scene 29_1_s14 with dissolve
    mc "That much?"  
    scene 29_1_s22 with dissolve
    ml "More than I can put into words."  
    ml "My whole life, I've been surrounded by people chasing wealth, chasing power... but all I ever wanted was something simple. A family of my own."  
    scene 29_1_s23 with dissolve
    mc "..."  
    scene 29_1_s19 with dissolve
    ml "*laughs* I know it sounds silly. But when I see mothers with their children, I feel this... ache inside me. Like I was meant for it too."  
    scene 29_1_s18 with dissolve
    mc "That doesn't sound silly at all."  
    scene 29_1_s19 with dissolve
    ml "Maybe not. But it scares me, wanting something so badly... and not knowing if I'll ever have it."  
    scene 29_1_s18 with dissolve
    mc "Then let's make it happen."
    scene 29_1_s19 with dissolve
    ml "Y-Yes!"  
    scene 29_1_s17 with dissolve
    ml "..."
    scene 29_1_s19 with dissolve
    ml "You can... start now. I'm ready."  
    scene 29_1_s17 with dissolve
    mc "Uh..."  
    scene 29_1_s22 with dissolve
    ml "What are you waiting for?"  
    ml "Just put it in me and... do what men do."  
    scene 29_1_s23 with dissolve
    mc "*chuckles* That's... one way to put it. 'Do what men do', very romantic..."  
    scene 29_1_s15 with dissolve
    ml "Ah! Maybe this position isn't ideal then. I knew I should have consulted more than just the medical texts." 
    scene 29_1_s14 with dissolve 
    scene black with Fade(0.5,0.5,0.5)
    perception "She slips off her bra and panties before bending over, spreading her legs as she steadies herself against the table."
    scene 29_1_s25 with dissolve
    ml "If you stand here, and I lean just a little... your seed might, um, travel deeper inside."  
    scene 29_1_s61 with dissolve
    perception "She sounds like she's reciting from a half-remembered book, but the flush on her cheeks betrays her eagerness." 
    if mc_liked_tits:
        sensation "The sight of her bare breasts sends a rush of heat through you, stirring your arousal."
    elif mc_liked_ass:
        sensation "The curve of her ass, perfectly framed in this position, is all it takes to make your cock harden."
    elif mc_liked_feet:
        sensation "Forget tits or ass—it's the outline of her feet in those tights that really gets you going."
    elif mc_liked_personality:
        sensation "It's not her body that does it for you... No, of course not. It's her beautiful personality. Right?"
    call screen scene29_choice08 with dissolve

label scene29_choice08_op2:
    mc "Let's begin."
    ml "Mhm."
    jump mc_harem_talk_nadia2

label scene29_choice08_op1:
    mc "You really think I'd begin without kissing you first?"  
    scene 29_1_s25 with dissolve
    ml "H-Huh? O-Oh! Right, of course. A proper man always... always kisses the woman first..."  
    ml "Gods above, I really am hopeless at this..." 
    scene 29_1_s61 with dissolve
    scene 29_1_s55 with Fade(0.5,0.5,1.0)
    perception "You lift her and place her on the table, her legs dangling just above the floor."  
    scene 29_1_s56 with dissolve
    ml "Oh my... *chuckles* You're really strong, [mc]."
    scene 29_1_s55 with dissolve
    mc "Nah, you're just light."
    mc "Now, where's my kiss?"
    scene 29_1_s56 with dissolve
    ml "R-Right..." 
    scene 29_1_s55 with dissolve
    scene 29_1_s57 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss3.mp3" 
    perception "Her lips tremble before they meet yours, a brief, clumsy brush, almost shy." 
    scene 29_1_s55 with Dissolve(1.0)
    mc "That was a kiss? Felt more like you were testing the waters."  
    scene 29_1_s56 with dissolve
    ml "*laughs* I told you, I don't have much practice..."  
    scene 29_1_s55 with dissolve
    mc "Then let's fix that."  
    scene 29_1_s58 with Dissolve(1.0)
    play sound "se_sfx/blowjob/kiss4.mp3" 
    perception "You pull her closer. Her lips part slightly, and the stiffness in her shoulders slowly melts away."  
    ml "Mmh... oh..."  
    perception "Her hand clutch your shoulder as if afraid you might pull away too soon."
    scene 29_1_s60 with Dissolve(1.0)
    mc "That's more like it."  
    scene 29_1_s59 with dissolve
    ml "My heart... it feels like it's going to burst out of my chest."  
    scene 29_1_s60 with dissolve
    mc "That just means you're doing it right."  
    scene 29_1_s59 with dissolve
    ml "You really do know how to make a woman blush, don't you?" 
    scene 29_1_s60 with dissolve
    mc "Shall we?"
    scene 29_1_s59 with dissolve
    ml "Yes. I feel more at ease now~" 
    scene 29_1_s60 with dissolve
    jump mc_harem_talk_nadia2

label maia_no_sex_happy:
    mc "(I made it clear to Maia that we're just friends. I'll stick to that.)"
    call screen is_maia with dissolve
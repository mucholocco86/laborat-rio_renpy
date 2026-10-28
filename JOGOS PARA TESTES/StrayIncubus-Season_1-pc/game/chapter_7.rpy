label chapter_7:
    $ chapter = 7
    $ clair_met = 1
    if invited_misty == 1:
        $ misty_met = 2
    define cat = Character("Cat", color="#6e6e6e")
    define margot = Character("Margot", color = "cf4442")
    image v7m1 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m1.webm", loop=True)
    image v7m2 = Movie(size = (1920,1080), channel="movie", play="0.7/video/FlynnTest1.webm", loop=True)
    image v7m3 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m3.webm", loop=True)
    image v7m4 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m4.webm", loop=True)
    image v7m5 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m5.webm", loop=True)
    image v7m6 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m6.webm", loop=True)
    image v7m7 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m7.webm", loop=True)
    image v7m8 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m8.webm", loop=True)
    image v7m9 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m9.webm", loop=True)
    image v7m10 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m10.webm", loop=True)
    image v7m11 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m11.webm", loop=True)
    image v7m12 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m12.webm", loop=True)
    image v7m13 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m13.webm", loop=True)
    image v7m14 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m14.webm", loop=True)
    image v7m15 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m15.webm", loop=True)
    image v7m16 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m16.webm", loop=True)
    image v7m17 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m17.webm", loop=True)
    image v7m18 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m18.webm", loop=True)
    image v7m19 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m19.webm", loop=True)
    image v7m20 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m20.webm", loop=True)
    #image v7m21 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m21.webm", loop=True)
    image v7m22 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m22.webm", loop=True)
    image v7m23 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m23.webm", loop=True)
    image v7m24 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m24.webm", loop=True)
    #image v7m25 = Movie(size = (1920,1080), channel="movie", play="0.7/video/v7m25.webm", loop=True)
    define choice_variable_ch7_1 = 0
    define choice_variable_ch7_2 = 0
    define choice_variable_ch7_3 = 0
    define choice_variable_ch7_4 = 0
    define choice_variable_ch7_5 = 0
    define choice_variable_ch7_6 = 0
    define choice_variable_ch7_8 = 0
    define choice_variable_ch7_9 = 0
    define choice_variable_ch7_10 = 0
    define choice_variable_ch7_11 = 0
    define choice_variable_ch7_12 = 0
    define choice_variable_ch7_13 = 0
    define choice_variable_ch7_14 = 0
    define choice_variable_ch7_15 = 0
    define choice_variable_ch7_16 = 0
    define choice_variable_ch7_17 = 0
    define choice_variable_ch7_18 = 0
    define choice_variable_ch7_19 = 0
    define choice_variable_ch7_20 = 0
    define choice_variable_ch7_21 = 0
    define choice_variable_ch7_22 = 0
    define choice_variable_ch7_23 = 0
    define choice_variable_ch7_24 = 0
    define choice_variable_ch7_25 = 0
    define choice_variable_ch7_26 = 0
    define choice_variable_ch7_27 = 0
    define choice_variable_ch7_28 = 0
    define choice_variable_ch7_29 = 0
    define choice_variable_ch7_30 = 0
    define choice_variable_ch7_31 = 0
    define choice_variable_ch7_32 = 0
    define choice_variable_ch7_33 = 0
    define choice_variable_ch7_34 = 0
    define choice_variable_ch7_35 = 0
    define persistent.g_22_unlock = 0
    define persistent.g_23_unlock = 0
    define persistent.g_24_unlock = 0
    define persistent.g_25_unlock = 0
    define persistent.g_26_unlock = 0
    pause(3)
    play music "audio/ch7_dream.mp3" volume 0.2 fadeout 1.0 fadein 1.0
    scene v71 with Dissolve(5)
    pause(1.5)
    z "..."
    scene black with Fade(1.5,1.5,1.5)
    scene v71_1 with dissolve
    pause(1.5)
    z "(Where...)"
    scene black with Fade(1.5,1.5,1.5)
    scene v71 with dissolve
    pause(1.5)
    z "(And who's that...)"
    scene black with Fade(1.5,1.5,1.5)
    scene v71_1 with dissolve
    pause(1.5)
    z "..."
    scene black with Fade(1.5,1.5,0)
    play sound "audio/Effect1.wav"
    stop music
    scene v72
    $ renpy.pause(0.1, hard=True)
    scene white with Dissolve(1.5)
    pause(1.5)
    #Fade to elnor in the tower.
    #Next scene jumps to Elnor holding the orb.
    #Disappears quickly
    #In the dungeon.
    scene v73 with Dissolve(1.5)
    play music "audio/ch7_dream.mp3" volume 0.5 fadeout 1.0 fadein 1.0
    z "(What was that...)"
    z "(And who was that man...)"
    z "(Wait... I know this place...)"
    scene v74 with dissolve #Sees Seira's legs.
    z "..."
    scene v75 with dissolve #Looks up (Out of focus).
    z "(Is that...)"
    z "(Seira?)"
    z "(But who's that next to her...)"
    #She's standing in front of him (protecting him from Theseus).
    Character("Man with blonde hair", color = "ffe9c2") "Hah! Don't you dare lecture me, boy! You say all that but here you are committing war crimes at the orders of the gods right besides me."
    z "(And who's that talking? What is he talking about? Is he talking to me?!)"
    z "(Why can't I move?! My vision is very blurry and I feel so cold...)"
    z "(And I'm... scared?)"
    z "(Is this me? Or am I feeling someone else's emotions like the time at the faceless god's town?)"
    Character("Man with dark hair", color = "000000") "You..."
    scene v76 with dissolve
    Character("Man with dark hair", color = "000000") "You shan't lay a hand on this child." #Lefts his lance
    Character("Man with blonde hair", color = "ffe9c2") "..."
    s "..."
    scene v77 with dissolve
    Character("Man with blonde hair", color = "ffe9c2") "You shall regret this, son of Helios."
    Character("Man with dark hair", color = "000000") "..."
    scene v78 with dissolve
    #Theseus leaves.
    s "..."
    scene v79 with dissolve
    s "Thank you..." #looking a sirius
    pause(1.5)
    scene black with Fade(1.5,0,0)
    stop music fadeout 1.0
    pause(1.5)
    play background_s "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v710 with Fade(0,0,1.5)
    pause(1.5)
    #Fades out and z wakes up
    scene v711 with dissolve
    z "..."
    z "(A dream?)"
    z "(It's similar to those I used to have in the cave... It's been a while since I had one, though...)"
    #Seira isn't there when z wakes up.
    #If slept next to S, Z wonders where she went. And why no one woke him up for practice.
    #Outside, Z sees Candy and Torr sitting on the edge next to stream. Z asks why no one woke him up for morning practice. They tell him that Stephanie isn't around, so classes are cancelled.
    #Z asks how they're doing. They talk a bit.
    #They tell Z that they're all summoned to the Keres's hut at noon.
    #Z tells them he's going to walk around a bit, they say goodbye.
    if s_aff >= 6 or hugged_s == 1: #if slept next to seira.
        scene v713 with dissolve
        z "(Seira already left...)"
    if s_aff >= 6 or hugged_s == 1:
        scene v716 with dissolve
    else:
        scene v717 with dissolve
    z "(Seems I slept in... How come no one woke me up for morning practice...)"
    if s_aff >= 6 or hugged_s == 1:
        scene v719 with dissolve
    else:
        scene v718 with dissolve
    pause(1)
    #Gets up and leaves the room.
    #Cndy and tr are sitting where tamara and hailey used to sit.
    #Yumi's cat is sitting in cndy's lap. He seems to hate torr.
    scene black with Fade(1.5,0,0)
    stop music fadeout 1.0
    pause(1.5)
    play background_s "audio/Ambient_ninja_village.mp3" volume 1 fadeout 1.0 fadein 1.0 loop
    scene v720 with Fade(0,0,1.5)
    pause(1.7)
    scene v721 with dissolve
    tr "..."
    play audio "audio/cat_hiss.wav"
    scene v722 with vpunch
    #Torr tries to pet him but he scratches her.
    cat "Hsss!" (multiple=2)
    tr "Aww!" (multiple=2)
    play audio "audio/meow.wav"
    scene v723 with dissolve
    tr "Mmmm... I fuhing hathhe thith cathh!" (multiple=2)
    cndy "Ahahah..." (multiple=2)
    scene v724 with dissolve
    pause(1.3)
    z "Morning, guys."
    scene v725 with dissolve
    pause(1.1)
    scene v726 with dissolve
    tr "Hey." (multiple=2) #Would be cool to make both their names appear.
    cndy "Hi, [mc_name]." (multiple=2)
    play music "audio/ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0
    scene v727 with dissolve
    z "Err... Shouldn't you guys be at morning practice?"
    scene v728 with dissolve
    cndy "Nah... Stephanie isn't around. She and Hailey left on a mission a few days ago."
    scene v727 with dissolve
    z "Ohh..."
    z "Wait! Don't tell me Tamara is going to give us classes again!"
    scene v729 with dissolve
    tr "No. She also left with Venus and the new ginger girl with the big tities... Uhm... What was her name..."
    scene v727 with dissolve
    z "..."
    z "Err... Gabbie?"
    scene v730 with dissolve
    tr "Yep. That's the one. They left on a mission to a nearby village, I think."
    scene v727 with dissolve
    z "..."
    z "So, who's even left around here aside from us?"
    scene v731 with dissolve
    cndy "I mean... Helena is here. And Yumi is around somewhere. Centoria too, I guess..."
    if invited_misty >= 1:
        scene v732 with dissolve
        cndy "And there's Misty, right? They're going to assign her to a role in the village at the meeting."
    scene v730 with dissolve
    tr "Which reminds me. All three of us are supposed to attend the meeting in the Keres's hut at noon."
    scene v733 with dissolve
    tr "They're going to evaluate the missions we took and reward us with dozens of points!" #Excited
    tr "I bet we'll get to reach purple belt like Centoria!"
    scene v727 with dissolve
    z "Oh? Centoria got to purple?"
    scene v728 with dissolve
    cndy "Yeah. After her last mission with Tamara."
    define cnt_prpl = 0
    $ cnt_prpl = 1
    #Change centoria's belt in stats.
    scene v734 with dissolve
    cndy "Let's not get too excited, though, Torr. We don't know if we're going to reach purple. You and I barely did anything during those mission..."
    scene v735 with dissolve
    tr "..."
    scene v736 with dissolve
    tr "Rrrright..." #Disappointed.
    scene v737 with dissolve
    z "I'm not sure how points work yet. But I'm sure you guys earned plenty of points... Come on!"
    scene v738 with dissolve
    tr "I hope so... You're definitely going to make it to purple, though..."
    scene v739 with dissolve
    z "Huh? Me?"
    scene v740 with dissolve
    cndy "I mean... It's almost guaranteed that you will..."
    if v4_obeyed_athena == 0:
        cndy "You killed a fury, right?"
    else:
        cndy "You stood up to a fury, right?"
    scene v741 with dissolve
    tr "And you almost killed the butcher by yourself. You're probably stronger than Yumi..."
    scene v727 with dissolve
    z "Err... I wouldn't say I'm stronger than Yumi..."
    z "(I can't be, right? That's ridiculous! She's a blue belt. Half a dozen ranks higher than I am or something...)"
    z "Changing the subject... Have you guys seen Seira?"
    scene v741 with dissolve
    tr "Oh. Your mom? Yeah. She went to the bath, I think."
    scene v742 with dissolve
    cndy "She's not his mom, Torr!" #Half closed eyes.
    scene v743 with dissolve
    tr "Oh? She's not?"
    scene v744 with dissolve
    if told_tr_n_cndy == 1:
        z "Ehhh... No. Not really. I told you my story before, remember?"
    else:
        z "Ehhh... No. Not really."
    scene v745 with dissolve
    tr "Rrrrright... I thought it was weird how you guys looked nothing alike..."
    scene v746 with dissolve
    z "... (Not the sharpest tool in the shed, are you, Torr?)"
    z "I guess I'll walk around a bit. See you, guys!"
    scene v747 with dissolve
    tr "Bye!" (multiple=2)
    cndy "See you!" (multiple=2)

    #z is walking around.
    #Sees centoria in front of a building.
    scene v748 with Fade(0.5,1.5,0.5)
    z "(Oh. Is that Centoria? She's wearing the purple belt and everything...)"
    scene v749 with dissolve
    z "Hey there, Centoria."
    scene v750 with dissolve
    cnt "Hm?"
    scene v751 with dissolve
    cnt "Oh. [mc_name]! Welcome back."
    scene v752 with dissolve
    z "Congrats on your new belt."
    scene v751 with dissolve
    cnt "Thank you."
    scene v752 with dissolve
    z "..."
    cnt "..."
    z "(She doesn't talk much, does she...)"
    z "So... Err... What does this door lead to? I've never been in there, I think."
    scene v753 with dissolve
    cnt "Hm? This?"
    cnt "It's just the old bathhouse."
    scene v754 with dissolve
    z "The old bathhouse? How come I never heard of it?"
    scene v755 with dissolve
    cnt "I believe it was closed. Tamara and I were tasked with cleaning it, so they can reopen it."
    cnt "But then Tamara left on a mission and I had to do it all on my own."
    scene v754 with dissolve
    z "Oh..."
    z "So, is it open now?"
    scene v755 with dissolve
    cnt "Yes. I finished cleaning yesterday."
    scene v754 with dissolve
    z "Cool."
    scene v755 with dissolve
    cnt "The older Keres lady went in there a few minutes ago."
    scene v754 with dissolve
    z "Seira?"
    scene v755 with dissolve
    cnt "Yes."
    scene v754 with dissolve
    if s_aff >= 6 or hugged_s == 1:
        z "Hmmm..."
        menu:
            "[ModGreen]Join Seira. (Seira Lust +2)":
                $ choice_variable_ch7_1 = 1
                z "(I guess I'll join her...)"
                z "I think I'm going to take a bath too."
                scene v755 with dissolve
                cnt "Okay."
                scene v754 with dissolve
                z "See you around, Centoria."
                scene v756 with dissolve
                cnt "See you around!" #waves bye at him
                scene v757 with dissolve
                pause(1)
                #Goes in
                label G22:
                    $ persistent.g_22_unlock = 1
                scene black with Fade(0.5,0,0)
                pause(1.5)
                stop sound fadeout 1.0
                stop music fadeout 1.0
                play background_s "audio/bath.mp3" fadein 1.0 loop
                scene v758 with Fade(0,0,0.5)
                pause(1.5)
                scene v759 with dissolve
                s "Lalala la..."
                play audio "audio/Door close.mp3"
                pause(1.0)
                z "Room for one more?"
                scene v760 with dissolve
                s "Hm? [mc_name]?"
                scene v761 with dissolve
                s "Sure. Come on in, honey."
                scene v762 with dissolve
                pause(0.7)
                #gets into tup.
                #s is sitting across from him.
                scene v763 with Fade(0.5,1.5,0.5)
                pause(1.3)
                scene v764 with dissolve
                s "Why are you sitting so far away? Come over here, I won't bite."
                scene v763 with dissolve
                z "Right."
                #They're sitting so she's hugging him from behind.
                scene v765 with dissolve
                play audio "audio/splash.wav"
                z "..."
                scene v766 with dissolve
                s "So... Sleep well?"
                scene v767 with dissolve
                z "Reasonably."
                scene v766 with dissolve
                s "'Reasonably'? You were sleeping like a baby when I left this morning!"
                if choice_variable_ch6_47 == 1:
                    scene v768 with dissolve
                    s "Guessing last night helped you blow off some steam..." #Seductive look
                    scene v769 with dissolve
                    z "Heh. You could say that."
                #Looks down.
                scene v770 with dissolve
                s "..."
                scene v771 with dissolve
                pause(0.7)
                scene v772 with dissolve
                s "My! Full of energy already?"
                z "Errr..."
                scene v773 with dissolve
                s "Say, how come stuff like this didn't happen when we bathed before?"
                scene v774 with dissolve
                z "It used to sometimes. But I used to hide it..."
                scene v775 with dissolve
                s "..."
                scene v776 with dissolve
                s "Well, you don't need to hide this kind of thing from me anymore, okay?" #Grabs it. Serious look
                stop music fadeout 1.0
                play music "audio/Jazz.mp3" volume 0.1 fadein 1.0 fadeout 1.0
                scene v777 with dissolve
                s "I'll help you with it, whenever you need."
                z "(Whoa... That sounds awesome...)"
                scene v779 with dissolve
                z "Yeah."
                $ Mod1 = False
                menu:
                    "Let her 'help' you. [ModGreen](Seira HJ)":
                        label label_Mod11:
                        $ choice_variable_ch7_2 = 1
                        z "I'd love some... 'help'."
                        scene v778 with dissolve
                        s "Okay... Let's see..."
                        show v7m1 with dissolve
                        #Hj while hugging him from behind.
                        s "Hmmm... So stiff..."
                        s "Must be really difficult to keep it tucked in your pants when it gets like this..."
                        z "Err... Kinda"
                        s "Does this feel good?"
                        z "Yeah... It's great..."
                        scene v780 with dissolve
                        s "Do you maybe feel a bit weird about me doing this for you?"
                        hide v7m1
                        show v7m1 with dissolve
                        z "..."
                        menu:
                            "Not really.":
                                $ choice_variable_ch7_3 = 1
                                z "Huh? No. Why?"
                                scene v780 with dissolve
                                s "I don't know... It's just."
                                s "You know what? Never mind. Just focus on feeling good."
                            "A bit.":
                                $ choice_variable_ch7_4 = 1
                                z "A bit, I guess."
                                scene v780 with dissolve
                                s "Think maybe we should stop doin-"
                                scene v782 with vpunch
                                z "NO!"
                                scene v783 with dissolve
                                s "Gods... Someone is excited. Okay..."
                        hide v7m1
                        show v7m1 with dissolve #Speeds up
                        s "How's that?"
                        z "Awesome... I'm close..."
                        s "(Gods... I never got to do this stuff when I was young... It feels so exciting...)"
                        s "(Who knew pleasuring someone could feel so satisfying...)"
                        s "(Maybe it's because it's [mc_name] I feel good about this...)"
                        z "Hahh... Seira... I'm..."
                        s "It's okay, honey. Do it."
                        s "Let it out..."
                        scene v785 with vpunch
                        z "Hahhh..." #Cums
                        if Mod1 == True:
                            jump label_Mod12
                    "'Help' her instead. [ModGreen](suck Seira boobs)":
                        label label_Mod12:
                        $ choice_variable_ch7_5 = 1
                        scene v786 with dissolve
                        z "Actually... I have a better idea."
                        s "?"
                        play audio "audio/splash.wav"
                        scene v787 with vpunch #Turns around grabbing her boob.
                        s "Ahh..."
                        scene v788 with dissolve
                        z "I was thinking I could help you, this time around."
                        scene v789 with dissolve
                        s "Ehhh... But you're the one who looks like he's about to dry-hump the lockers..."
                        scene v790 with dissolve
                        z "Trust me. I'd rather do this."
                        s "Hmm..."
                        scene v789 with dissolve
                        s "Well... Okay, then."
                        s "What exactly do you-"
                        show v7m3 with dissolve #Lowers his hand to her pussy while sucking her boob.
                        s "Ohhh... Ahhh... [mc_name]..."
                        s "This is... Ahhh... I'm..."
                        if choice_variable_ch6_43 == 1:
                            s "What's... Ahh... with you and sucking my... ah... nipples..."
                            z "Hmm..."
                            s "We're going to... Ahhh... Have to look for a cure..."
                            s "Ohhh... For this obsession of yours... Ahhhh... Ohhh..."
                            z "Hmmm... Maybe the cure lies in sucking on them..."
                            s "Ahhh... That's... Absurd..."
                        s "Ohhh... Wait... [mc_name]... Ahhhh..."
                        s "(Gods... I never got to do this stuff when I was young... It feels so exciting...)"
                        s "(Who knew it felt so good to have someone do this to me...)"
                        s "(Maybe it's because it's [mc_name] I feel this good...)"
                        s "Ahhh... [mc_name]... You're... That's... Ahhh..."
                        s "I'm going to... I can feel it... Ahhh..."
                        s "Wait... I... Ahhh..."
                        scene v791 with vpunch
                        s "Ohhhhhhh!" #Cums.
                        scene v792 with dissolve
                        s "Hahhhh..."
                        if Mod1 == True:
                            jump label_Mod13
                    "[ModGreen]MOD: Both. (Seira HJ and suck Seira boobs)":
                        $ Mod1 = True
                        jump label_Mod11
                label label_Mod13:
                pause(1)
                scene black with fade
                stop music fadeout 1.0
                $ renpy.end_replay()
                if came_from_gallery == 1:
                    $ came_from_gallery = 0
                    jump gallery_3
                pause(1.5)
                #Cuddling after.
                scene v793 with dissolve
                if came_from_gallery == 0:
                    $ s_lst += 3
                play sound "audio/stats.wav"
                show screen button_lst with dissolve
                hide screen button_lst with dissolve
                s "..."
                scene v794 with dissolve
                s "Comfortable?"
                scene v795 with dissolve
                z "Very."
                scene v796 with dissolve
                s "Teh."
                scene v797 with dissolve
                s "So... Are you getting similar action elsewhere?"
                scene v798 with dissolve
                z "H-Huh?! What do you mean?!"
                scene v799 with dissolve
                if cndy_lst >= 6 and cndy_aff >= 10 and tr_lst >= 4 and tr_aff >= 12:
                    s "Don't play dumb with me! Candy and Torr! I can tell these two were all over you!"
                elif cndy_lst >= 6 and cndy_aff >= 10:
                    s "Don't play dumb with me! I can tell Candy was all over you!"
                elif tr_lst >= 4 and tr_aff >= 12:
                    s "Don't play dumb with me! I can tell Torr was all over you!"
                else:
                    s "Hm? Playing all innocent, are we? Fine. I'll pretend I believe you."
                scene v798 with dissolve
                if cndy_lst >= 6 and cndy_aff >= 10 and tr_lst >= 4 and tr_aff >= 12:
                    z "What?! They were?!"
                    scene v7100 with dissolve
                    s "Ahahah... Oh... Honey. You're so cute, sometimes..."
                elif tr_lst >= 4 and tr_aff >= 12:
                    z "What?! She was?!"
                    scene v7100 with dissolve
                    s "Ahahah... Oh... Honey. You're so cute, sometimes..."
                elif tr_lst >= 4 and tr_aff >= 12:
                    z "What?! She was?!"
                    scene v7100 with dissolve
                    s "Ahahah... Oh... Honey. You're so cute, sometimes..."
                z "..."
                if a_aff >= 2:
                    scene v799 with dissolve
                    s "I feel like you have a chance with Anabelle too."
                    scene v798 with dissolve
                    z "A-Anabelle? Do I?"
                    scene v799 with dissolve
                    s "Yep. I can tell she likes you. I mean who can blame her. You're such a handsome young man."
                    scene v798 with dissolve
                    z "No way... She's totally out of my league, Seira."
                    scene v7100 with dissolve
                    s "Heh. If you say so."
                scene v799 with dissolve
                s "Actually. Don't you have practice or something?"
                scene v798 with dissolve
                z "No. Stephanie isn't around, so my classes are cancelled."
                scene v799 with dissolve
                s "Right..."
                scene v7103 with dissolve
                z "..."
                scene v7102 with dissolve
                z "Seira..."
                scene v7101 with dissolve
                s "Yeah?"
                scene v7102 with dissolve
                z "Do you remember those dreams I told you about?"
                scene v7101 with dissolve
                s "The ones from back in the cave?"
                scene v7102 with dissolve
                z "Well, yes."
                scene v7101 with dissolve
                s "Did you have one?"
                scene v7102 with dissolve
                z "I think so..."
                z "There was a weird bit at the beginning. I can't remember clearly but I was in a room. And there was a man there."
                z "I think he gave me something... Something shiny..."
                scene v7101 with dissolve
                s "Shiny?"
                scene v7102 with dissolve
                z "Yeah. It was like a ball. But glowing and I could feel it's warmth."
                scene v7101 with dissolve
                s "Maybe it was a spell?"
                scene v7102 with dissolve
                z "A spell? Yeah. Maybe..."
                z "But then, I went back to the usual dream. Sort of..."
                z "I usually just see you standing there. Looking at me while I cry in the corner."
                z "And then, Theseus shows up telling you that I should die..."
                z "But this time, I was looking through my own eyes. I think."
                z "And I saw you. This time, you were turning your back to me. And there was a man standing next to you."
                z "I think he had black hair. And he was wearing a ponytail... I'm not sure. It wasn't very clear."
                scene v7104 with dissolve
                s "Oh..."
                scene v7106 with dissolve
                z "Theseus called him 'son of Helios'."
                z "I think he defended me from Theseus. You thanked him at the end."
                scene v7105 with dissolve
                s "..."
                scene v7106 with dissolve
                z "Did this happen, or..."
                scene v7104 with dissolve
                s "Yeah. It happened."
                scene v7107 with dissolve
                s "Theseus was my mentor. He was extremely powerful. I doubt I could've held my own against him that day."
                $ theseus_met = 1
                scene v7105 with dissolve
                s "..."
                scene v7107 with dissolve
                s "The man you saw. The one who defended you. That was Sirius. Anabelle and Yumi's brother."
                scene v7105 with dissolve
                z "..." #Surprised
                scene v7106 with dissolve
                z "Tell me more..."
                scene v7107 with dissolve
                s "That was it, basically. I took you and we left."
                scene v7106 with dissolve
                z "But why would Sirius support you and disobey the gods all of the sudden?!"
                scene v7104 with dissolve
                s "I don't know exactly what it was. Maybe he simply thought killing a child was wrong. At that day this sort of thing wasn't very unusual, [mc_name]."
                scene v7107 with dissolve
                s "Dozens of warriors defected that day. They were told they're heading into a battle, not slaughtering defenseless civilians."
                s "I didn't really know Sirius. He was famous amongst the demi gods and the Keres. Many claimed he'd be the strongest demi-god in living memory. But I think that was the first time I talked to him."
                scene v7106 with dissolve
                z "Yeah. Anabelle mentioned him defecting and joining the ninjas after that."
                scene v7108 with dissolve
                s "Well. No matter what he did after, I'm grateful to him."
                s "Thanks to him, I got you, after all."
                scene v7109 with dissolve
                s "*Kisses you."
                #Kisses him.
                scene v7110 with dissolve
                z "..."
                scene v7111 with vpunch
                play audio "audio/splash.wav"
                s "Now, chop-chop! We can't just hang around here the whole day. Time to get up."
                z "Yeah, yeah. I'm getting up! Stop pushing!"
                pause(1)
            "Don't.":
                $ choice_variable_ch7_7 = 1
                z "Well, I guess I'll just walk around some more, then."
                scene v755 with dissolve
                cnt "Okay."
                scene v754 with dissolve
                z "See you around, Centoria."
                scene v756 with dissolve
                cnt "See you around!" #waves bye at him
                scene v757 with dissolve
                pause(1)
    else:
        z "Oh..."
        z "I guess I'll walk around some more, then."
        scene v755 with dissolve
        cnt "Okay."
        scene v754 with dissolve
        z "See you around, Centoria."
        scene v756 with dissolve
        cnt "See you around!" #waves bye at him
        scene v757 with dissolve
        pause(1)
    scene black with fade
    stop sound fadeout 1.0
    play background_s "audio/Ambient_ninja_village.mp3" fadein 1.0 loop
    #Later
    init python:
        renpy.music.register_channel("effects", "sfx")
        renpy.music.register_channel("background_s", "sfx")
        renpy.music.register_channel("background_s2", "sfx")
    pause(2.5)
    scene v7112 with dissolve
    pause(1) #Z is walking.
    scene v7113 with dissolve
    play effects "audio/Sparing.wav" fadein 1.0 loop volume 0.05
    "*Fighting sounds."
    scene v7114 with dissolve
    z "Hm?"
    stop effects fadeout 1.0
    stop background_s fadeout 1
    play background_s "audio/Ambient_ninja_village.mp3" fadein 1 volume 0.6 loop
    scene v7115 with Fade(0.5,0.5,0.5) #Enters the builing.
    z "..."
    z "(Is that... Are they sparring?)"
    z "(This should be interesting...)"
    play audio "audio/bamboo_sword_clash.mp3"
    scene v7117 with vpunch
    a "Haah!" #Slashes at yumi.
    play audio "audio/slash.flac"
    scene v7118
    z "(So fast... I barely saw her sword moving...)"
    play audio "audio/slash.flac"
    scene v7119 with vpunch
    z "(Yumi can do nothing but block and evade. There's no window to attack...)"
    scene v7120 with dissolve
    z "(But it's still pretty impressive... Can I even block something like that?)"
    play audio "audio/bamboo_sword_clash.mp3"
    scene v7121 with vpunch
    #Repeated fast slashes from a, which ymi is able to block with difficulty.
    z "(Holy fuck! Are they trying to kill each other?!)" #When anabelle slams the ground.
    scene v7122 with dissolve
    ymi "*Heavily breating."
    scene v7123 with dissolve
    a "Not bad, Yumi. Not bad at all."
    scene v7124 with dissolve
    ymi "Hufh... Hah... Hahh..."
    scene v7125 with dissolve
    a "..."
    scene v7126 with dissolve
    a "But enough warm up. Let's get serious, shall we?"
    scene v7127 with dissolve
    z "(Err... What...)"
    scene v7128 with dissolve
    ymi "Y-Yeah..."
    scene v7129 with dissolve
    z "..."
    scene v7130 with dissolve
    a "..."
    scene v7131 with dissolve
    ymi "..."
    scene v7132 with dissolve
    z "(Could I have evaded and blocked like Yumi did just now?)"
    z "(I feel...)"
    z "(I feel like I could... Somehow...)"
    z "(Damn... I want to try...)"
    z "(Or, do I...)"
    #Standing and staring at each other.
    scene v7133 with Dissolve(0.1)
    play audio "audio/Punch.wav"
    pause(0.3)
    scene v7134 with vpunch
    a "HAAAAH!"
    ymi "Ugh!"
    #Kicks her.
    #Lands at z's feet.
    play audio "audio/Falling.mp3"
    scene v7135 with vpunch
    pause(0.5)
    a "Gods, Yumi! How many times have I told you to pay attention to your opponent's legs?!"
    ymi "Awww..."
    scene v7136 with dissolve
    ymi "?" #Looks up.
    z "Errr... Sup!"
    scene v7137 with dissolve
    ymi "[mc_name]?! How long have you been standing here?!"
    scene v7138 with dissolve
    z "Well, I-"
    scene v7139 with dissolve
    a "Yeah... I didn't notice you at all, to be honest. Have you been practicing to conceal your presence? I thought it was too early for that." #Anabelle approaches them.
    scene v7140 with dissolve
    z "Not really. I guess it's a talent of mine..."
    scene v7141 with dissolve
    a "Hmm..."
    z "How are you doing Yumi? It's been a while."
    scene v7142 with dissolve
    ymi "Yeah... I'm fine, thank you for asking."
    scene v7143 with dissolve
    ymi "Aside from having my ass kicked here, of course." #Smiles at a
    scene v7144 with dissolve
    z "Heh..."
    scene v7145 with dissolve
    ymi "How are YOU doing, though? Annie tells me you basically defeated the butcher on your own..."
    scene v7146 with dissolve
    z "Well... I wouldn't go that far."
    scene v7147 with dissolve
    a "Come on! Stop being so humble! He was totally chopped up when I got there!"
    scene v7148 with dissolve
    z "..."
    z "I guess he was kinda... chopped up..."
    scene v7149 with dissolve
    ymi "Which means you defeated an opponent I couldn't defeat, this is 1-0 for you."
    ymi "I'll get you back for this, though!"
    scene v7150 with dissolve
    z "I guess we'll see about that, Yumi."
    scene v7149 with dissolve
    ymi "It's a promise. I've been practicing and sparring with others every day ever since I came back."
    scene v7151 with dissolve
    a "You're doing great, Yumi. Just don't forget to practice your basics too."
    scene v7152 with dissolve
    ymi "I won't."
    scene v7153 with dissolve
    a "Now that I think about it. You and I have never sparred before, have we?"
    scene v7154 with dissolve
    z "Who? Me?"
    if a_aff >= 2:
        scene v7153 with dissolve
        a "No. I'm talking to the pillar behind you."
        scene v7154 with dissolve
        z "*Chuckles. No. I don't believe we have."
    else:
        scene v7153 with dissolve
        a "Yup."
        scene v7154 with dissolve
        z "Ahm... No. I don't believe we have."
    scene v7155 with dissolve
    a "Wanna try?"
    scene v7156 with dissolve
    z "I mean... Can I really spar against you?"
    scene v7157 with dissolve
    a "Why? Are you underestimating yourself. You're quite strong, you know..."
    a "Besides, you spar against Keres Seira all the time, don't you?"
    scene v7158 with dissolve
    z "Yeah. I guess..."
    scene v7159 with dissolve
    a "I'd say Seira is actually stronger than I am. So you should be fine."
    scene v7160 with dissolve
    ymi "Wait. Really?"
    scene v7161 with dissolve
    a "I think so. She's a demi-god, after all..."
    scene v7162 with dissolve
    z "Hmm... (Wow... I always knew that Seira is very strong, but...)"
    scene v7163 with dissolve
    a "So? What do you say?"
    scene v7164 with dissolve
    menu:
        "Spar with Anabelle. [ModGreen](Posible Anabelle Lust point)":
            $ choice_variable_ch7_8 = 1
            z "Yeah. I'd love to spar with you."
            scene v7165 with dissolve
            a "Cool! Let's do it, then."
            scene v7166 with dissolve
            ymi "Nice! This should be fun to watch." #Walks closer.
            scene v7167 with dissolve
            a "Errr... Where do you thing you're going?" #Stops Yumi with her hand on Yumi's face
            a "You still haven't finished your morning push-ups. We agreed you'd do them once we're done here."
            scene v7168 with dissolve
            ymi "Awww... Fine."
            scene v7169 with dissolve
            ymi "*Defeated Yumi leaves."
            scene v7170 with dissolve
            z "Err... How come I don't have to do morning push-ups?"
            scene v7171 with dissolve
            a "Well, it's really up to your instructor to decide what kind of exercise you have to do."
            a "And Yumi asked me to be her instructor while Hailey is gone."
            scene v7172 with dissolve
            z "Ohh... I see."
            scene v7171 with dissolve
            a "Okay, let's start by you showing me your stance."
            scene v7172 with dissolve
            z "Right."
            pause(0.7)
            #Go on the mat.
            #Shows her.
            scene black with fade
            stop music fadeout 3.0
            stop sound fadeout 3.0
            pause(1.0)
            scene v7173 with dissolve
            pause(1.0)
            scene v7174 with dissolve
            pause(1.0)
            scene v7175 with dissolve
            a "Hmmm..."
            scene v7176 with dissolve
            a "Not bad. Not bad at all..."
            play music "audio/fight.mp3" volume 0.2 fadein 3.0 fadeout 1.5
            scene v7177 with dissolve
            a "Okay. Here I come, [mc_name]."
            scene v7178 with dissolve
            z "..."
            scene v7179 with dissolve
            z "(Fuck me... She looks a bit... scary...)"
            z "(But kinda really cute at the same time... I don't know what it is... But something about this girl is really charming...)"
            #If bathed with Seira and told you that you have a chance with a_lst
            z "(Gods... Could it really be that I have a chance with this girl... I feel like a kid next to her...)"
            #If fucked serena or seira.
            if choice_variable_ch7_1 == 1 or choice_variable_ch6_47 == 1:
                z "(I know I did some stuff with older women, and even with Seira... But it's just different with her...)"
            else:
                z "(I know I did some stuff with older women, but it's just different with her...)"
            scene v7178 with dissolve
            z "(Okay. I have to focus here! I can't look pathetic now! Even if I can't win, I have to put up a good show in front of her!)"
            play audio "audio/Punch.wav"
            pause(0.2)
            scene v7180 with vpunch #Anabelle slashes at him a bit.
            z "(Holy fuck! So fast!)"
            #Z is only barely able to block.
            scene v7181 with dissolve
            pause(0.3)
            play audio "audio/Punch.wav"
            pause(0.4)
            scene v7182 with vpunch
            pause(0.3)
            play audio "audio/Punch.wav"
            pause(0.4)
            scene v7183 with vpunch
            pause(0.5)
            scene v7184 with dissolve
            z "(I can't even blink, yet she's just swinging effortlessly...)"
            z "(I really can't tell whether she's stronger or weaker than Seira... I feel just as helpless against her as against Seira...)"
            z "(I guess this means I still have a long way to go...)"
            z "(Although... I do feel way stronger whenever I activate my powers during a fight...)"
            z "(Should I try it now? It could give me an edge here... But I also don't want to somehow accidentally hurt her...)"
            z "(Well... It's Anabelle. She should be fine even if I go all out... It's not like I actually lose control either... Right?)"
            menu:
                "Use your powers. [ModGreen](Anabelle Lust +1)":
                    $ choice_variable_ch7_9 = 1
                    scene v7192 with dissolve
                    z "Hmmm..."
                    scene v7193 with dissolve
                    pause(0.5)
                    scene v7194 with Dissolve(2)
                    pause(1)
                    scene v7195 with dissolve
                    a "?!"
                    #Focus on his eye.
                    #Opens suddenly, he's transformed.
                    play audio "audio/slash.flac"
                    scene v7196
                    a "HAAA!" #Slashes into the dark cloud.
                    scene v7197 with dissolve
                    pause(0.5)
                    scene v7198 with dissolve
                    a "Whoa... You-"
                    play audio "audio/Punch.wav"
                    pause(0.2)
                    scene v7199 with vpunch
                    #Attacks her from behind.
                    a "Hnn!" #Blocks with difficulty.
                    #Swings at each other.
                    play audio "audio/Punch.wav"
                    pause(0.2)
                    scene v7200 with vpunch
                    a "HAA!" #Make both char names appear.
                    z "Hngh!"
                    #Pushes the swords towards her.
                    play audio "audio/Punch.wav"
                    pause(0.2)
                    scene v7201 with vpunch
                    a "Hn!"
                    scene v7202 with dissolve
                    a "Hngh..."
                    scene v7203 with dissolve
                    a "Y-You..."
                    #Struggling to push back
                    scene v7204 with dissolve
                    pause(1)
                    play audio "audio/Punch.wav"
                    pause(0.3)
                    scene v7205 with vpunch
                    pause(0.5)
                    play audio "audio/Falling.mp3"
                    stop music fadeout 2.0
                    scene v7206 with vpunch #Kicks his feet and he falls.
                    z "Ugh!"
                    scene v7207 with dissolve
                    z "Ughnn..."
                    #Sits on him holding his arms.
                    #She's visibly sweaty.
                    scene v7208 with dissolve
                    play music "audio/Jazz.mp3" volume 0.1 fadein 1.0 fadeout 1.0
                    a "Hufh... I got you now, big boy."
                    scene v7209 with dissolve
                    z "..."
                    scene v7210 with dissolve
                    z "Yeah... Fair. You got me."
                    scene v7212 with dissolve
                    a "By the way, you're not supposed to use magic during sword sparring..."
                    scene v7211 with dissolve
                    z "Magic? I didn't use magic!"
                    scene v7213 with dissolve
                    a "What?! You disappeared just now in the black smoke!"
                    scene v7214 with dissolve
                    z "I... That wasn't magic... I don't think..."
                    scene v7213 with dissolve
                    a "Huh?!"
                    a "You mean you could actually move this fast?!"
                    scene v7214 with dissolve
                    z "Yeah... But it's only when I transform and for a split second."
                    scene v7213 with dissolve
                    a "What about that dark cloud you left?"
                    scene v7214 with dissolve
                    z "It's just left over aura, I guess... It comes out on its own, but it works very well to mask my movement."
                    a "..."
                    scene v7215 with dissolve
                    a "Whoa... That's a pretty useful ability to escape a difficult situation..."
                    scene v7216 with dissolve
                    z "Err... Speaking of difficult situations..."
                    a "Hm?"
                    scene v7217 with dissolve
                    z "(She's literally sitting on my...)"
                    z "(Doesn't she know what she's doing? She seems pretty clueless about it...)"
                    z "(I guess she really doesn't see me as a man after all... Damn...)"
                    scene v7218 with dissolve
                    z "(Gods... Her boobs are so close to my face... I can almost feel the warmth coming out of them...)"
                    scene v7217 with dissolve
                    z "(Great! I'm getting a boner...)"
                    scene v7219 with dissolve
                    z "(Fuck...)"
                    scene v7216 with dissolve
                    a "..." #looking at z
                    scene v7220 with dissolve
                    a "Err..." #Notices sth
                    a "Stay still. Something was poking me... Do you have something in your pocket? I hope it didn't get broken when I knocked you down or-" #Turns around
                    play audio "audio/rustle.mp3"
                    scene v7221 with dissolve
                    z "W-Wait!"
                    scene v7222 with dissolve
                    z "(Gods...)" #Her ass is in his face.
                    scene v7223 with dissolve
                    #Looking at it.
                    a "..."
                    scene v7224 with dissolve
                    a "What's th-"
                    pause(1)
                    scene v7225 with dissolve
                    a "..." #Surprised
                    $ a_lst += 1
                    play sound "audio/stats.wav"
                    show screen button_lst with dissolve
                    hide screen button_lst with dissolve
                    play audio "audio/rustle.mp3"
                    scene v7226 with vpunch
                    a "Ahh! Sorry!" #Jumps off.
                    z "(Gods... She definitely thinks I'm a huge-ass pervert now...)"
                    #After standing up, a is embarrassed.
                    play audio "audio/rustle.mp3"
                    scene v7227 with dissolve
                    z "Err... Sorry... It just happens sometimes... It's not intentional or anything..."
                    scene v7228 with dissolve
                    a "No, no. I'm not a child. I know. It's my fault, after all. I should've been more considerate."
                    scene v7229 with dissolve
                    a "Listen. Let's just forget about it and put it behind us, okay?"
                    scene v7230 with dissolve
                    z "Yeah... Sounds good."
                    scene v7229 with dissolve
                    a "Cool..."
                    scene v7231 with dissolve
                    a "Anyway, though. I have to get going. I want to talk a bit with Helena before the meeting. We'll pick this up some other time, okay?"
                    scene v7232 with dissolve #Pauses.
                    pause(1)
                    scene v7233 with vpunch
                    a "The sparring, I mean!" #Vpunch
                    scene v7234 with dissolve
                    z "Err... Yeah. Sure. See you."
                    scene v7235 with dissolve
                    a "*Runs away."
                    z "..."
                    z "(I hope I didn't fuck things up...)"
                "Don't.":
                    $ choice_variable_ch7_10 = 1
                    scene v7185 with dissolve
                    z "(Anabelle or not. It's too dangerous to casually use a power I don't fully understand...)"
                    z "(I think I'll just try to hold my own as is. Maybe I can somehow force an opening and st-)"
                    scene v7186
                    play audio "audio/slash.flac"
                    z "!" #Anabelle's sword stops before it hits his face. She has won.
                    scene v7187 with dissolve
                    z "..."
                    scene v7188 with dissolve
                    z "(Heh. How delusional of me...)"
                    scene v7189 with dissolve
                    z "You got me."
                    a "Hmmm..."
                    scene v7190 with dissolve
                    a "Not bad, [mc_name]. Not bad at all. You're more or less as good as Yumi."
                    scene v7189 with dissolve
                    z "Really? I mean I did tie against her once. But I thought it might've just been a fluke..."
                    z "And she held her own longer against you, didn't she?"
                    scene v7190 with dissolve
                    a "Nope. You're excellent at this. It's not only about how long you can hold your own."
                    a "When it comes to sword skill, you're at least green belt level."
                    scene v7189 with dissolve
                    z "You really think so?" #Smiling.
                    scene v7190 with dissolve
                    a "Definitely."
                    scene v7191 with dissolve
                    a "Sorry, though. I have to get going. I want to talk a bit with Helena before the meeting. We'll pick this up some other time, okay?"
                    scene v7189 with dissolve
                    z "Yeah. See you."
        "Don't.":
            $ choice_variable_ch7_11 = 1
            z "I'm not sure, Anabelle... I don't want to embarrass myself... Maybe in a few weeks? When I've had more training?"
            scene v7163 with dissolve
            a "Oh? Well. If that's what you prefer."
            a "I guess I'll go talk a bit with Helena before the meeting. See you in a bit."
            scene v7164 with dissolve
            z "Yeah. See you."
    stop music fadeout 1.0
    pause(1.0)
    scene black with fade
    #Later
    pause(2.5)
    if invited_misty == 0:
        jump meeting_ch7
    play background_s "audio/Ambient_ninja_village.mp3" fadeout 1.0 fadein 1.0 loop
    #Give her the white belt in stats. Maybe also change her pic?
    #Comment how they made a custom for her. (She makes a sissors gesture saying she cuts holes in them herself.)
    #Go together to the meeting.
    #Only if she's at village.
    #She looks lost.
    #She's where z first met stephanie.
    #She's wearing a white belt uniform.
    scene v7236 with dissolve
    pause(1)
    z "(Is that...)"
    z "(Misty!)"
    pause(1)
    scene v7237 with dissolve #Approaches her.
    z "Hi, Misty!"
    scene v7238 with dissolve
    misty "Hm?"
    scene v7239 with dissolve
    misty "[mc_name]!"
    scene v7240 with dissolve
    play music "audio/ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    z "You look nice."
    scene v7241 with dissolve
    misty "Th-Thanks..." #Timidly looks away.
    scene v7242 with dissolve
    define misty_rank_change = 0
    define z_rank_change = 0
    define cndy_rank_change = 0
    define tr_rank_change = 0
    $ misty_rank_change = 1
    $ renpy.notify("Misty's rank is now white belt.")
    pause(1.0)
    #Give her the white belt in stats. Maybe also change her pic?
    #Maybe a notification about it?
    #Ask her questions menu: Animation with blinking <----------------------------------------------------
    label ask_misty_ch7:
    show v7m4 with dissolve
    define ask_misty_ch7_1 = 0
    define ask_misty_ch7_2 = 0
    define ask_misty_ch7_3 = 0
    define ask_misty_ch7_4 = 0
    menu:
        "Ask about the four-arm-holed uniform." if ask_misty_ch7_1 == 0:
            $ ask_misty_ch7_1 = 1
            z "Wait... How did you find a uniform with four arm holes?"
            misty "Hmm?"
            scene v7243 with dissolve
            misty "Oh. This?"
            scene v7244 with dissolve
            misty "I just cut holes in my clothes with sissors."
            misty "I was pretty bad at making these and damaged some shirts at first, but with time, I got better."
            misty "I kinda got help from Torr and Candy too..."
            scene v7245 with dissolve
            z "I see..."
            pause(0.7)
            jump ask_misty_ch7
        "Ask about her tattoo." if ask_misty_ch7_2 == 0:
            $ ask_misty_ch7_2 = 1
            z "Can I ask about your tattoo?"
            scene v7246 with dissolve
            misty "My tattoo?"
            scene v7247 with dissolve
            misty "You mean the mark on my back?"
            scene v7248 with dissolve
            z "Yeah."
            scene v7249 with dissolve
            misty "Well... My father drew it for me... Back when he was... You know..."
            scene v7250 with dissolve
            z "Ohhh..."
            scene v7251 with dissolve
            misty "He spent three weeks doing it. It's a special type of ink, so it doesn't wash off."
            misty "Most beasts do something similar to their children, from what I hear."
            misty "He said it should always remind me of who I am... That I wasn't a human... And that no one would ever really accept me as one..."
            scene v7252 with dissolve
            z "..."
            z "(Well done, [mc_name]. You reminded her of some painful memories...)"
            z "I'm really sorry, Mi-"
            scene v7253 with dissolve
            misty "No, no! Don't be!"
            scene v7251 with dissolve
            misty "It's not like he was totally right. I was hardly ever treated harshly for being a demi-human."
            misty "I mean... Maybe I was occasionally..."
            misty "But then again, there were plenty of kind people like you in my life. My parents, Frankie, Mrs.Schwartz... others I forgot... And I was very lucky to meet all of them."
            scene v7254 with dissolve
            misty "You were the first to help me this much, though. The thing with my father... Then you gave me a new start... I don't think I'll ever forget you."
            scene v7255 with dissolve
            z "..."
            z "I... don't know what to say..."
            scene v7256 with dissolve
            misty "You don't need to say anything, silly! Just acknowledge my gratitude in silence. *Giggles."
            scene v7257 with dissolve
            z "*Chuckles. I could do that."
            pause(0.7)
            jump ask_misty_ch7
        "Ask how she finds it here." if ask_misty_ch7_3 == 0:
            $ ask_misty_ch7_3 = 1
            z "So... I know you've only been here for a very short while, but..."
            z "What's your initial impression of the place?"
            scene v7258 with dissolve
            misty "Oh. The village looks super nice... And It's warmer than it was in Esyl too."
            misty "And the girls are all nice to me. Being a shop owner, I'm used to rougher treatment from people. Not all customers were as polite as you guys..."
            scene v7259 with dissolve
            misty "So... This kinda reminds me of home... Maybe it's a bit early to be saying stuff like that..."
            misty "But it's just... With my parents and at home... That was where I'm used to being treated with such kindness..."
            scene v7260 with dissolve
            misty "A-Am I making sense? Or d-does it sound like some weird nonsense?" #Shy
            scene v7261 with dissolve
            z "Yup. I get what you're saying."
            z "I think it's great that you feel that way."
            z "I think I mentioned this to you before. But I've only been here for a week or so..."
            z "I might've spent more time out on missions than in the village."
            z "But I really feel like I'm at home here. I think Seira being here is helping with that too."
            scene v7262 with dissolve
            misty "The older Keres lady? I thought Keres didn't get married or have children... You also mentioned being an orphan..."
            scene v7263 with dissolve
            z "Huh? No. Seira is not my mother!"
            scene v7262 with dissolve
            misty "Oh..."
            misty "So... Like... She's..."
            scene v7263 with dissolve
            z "She took care of me for as long as I can remember. And like I said I don't remember my real parents."
            scene v7262 with dissolve
            misty "Ohhhhhhh...."
            misty "Yeah. It all makes sense now..."
            scene v7260 with dissolve
            misty "Sorry. I didn't mean to press or anything." #Pointy fingers with awekward smile
            scene v7261 with dissolve
            z "Don't worry. I don't really mind talking about this stuff."
            z "And it's not like I haven't been poking around asking you all kind of stuff about yourself. You're a very interesting person, you know."
            scene v7264 with dissolve
            misty "..." #Embarressed while doing the pointy finger thing.
            scene v7265 with dissolve
            misty "Th-Thanks... I don't mind telling you about stuff like that either. You can ask whatever you want..."
            pause(0.7)
            jump ask_misty_ch7
        "Ask about her extra eyes." if ask_misty_ch7_4 == 0:
            $ ask_misty_ch7_4 = 1
            z "So... I have a very... curious question."
            scene v7259 with dissolve
            misty "Shoot."
            scene v7263 with dissolve
            z "Your four bottom eyes. I noticed they don't blink..."
            scene v7266 with dissolve
            misty "Oh, those?"
            scene v7267 with dissolve
            misty "Yeah. They don't actually work. I can't see anything with them."
            misty "I hear it's very common for hybrid creatures to have parts that don't function properly."
            scene v7268 with dissolve
            z "Really..."
            scene v7269 with dissolve
            misty "But all my arms work just fine. See?" #Lefts them all up.
            scene v7270 with dissolve
            z "Yeah. I noticed that much."
            pause(0.7)
            jump ask_misty_ch7
        "Enough questions." if ask_misty_ch7_1 == 0 or ask_misty_ch7_2 == 0 or ask_misty_ch7_3 == 0 or ask_misty_ch7_4 == 0:
            z "Well... Are you looking for something, or..."
    scene v7258 with dissolve
    misty "Oh. Yeah! I'm actually supposed to attend a meeting at the Keres's hut. But I don't remember how to get there..."
    scene v7252 with dissolve
    z "Oh? I'm going there too. Come on, I'll show you."
    pause(1)
    stop music fadeout 1.0
    stop background_s fadeout 1.0
    scene black with fade
    #Later
    pause(2.5)
    label meeting_ch7:
    #5) Meeting at the keres's hut. {@100%@100%R@0%W}
    #If misty is invited, mention that she recieved the white belt and is working at the cafeteria.
    #S talks with A about how disobeying Athena might anger Ares. (Who commands the kereses.)
    #Torr and Candy are here.
    #Z should learn here that Helena is Stephanie's mother.
    #Helena should break down the missions and their ranking system. And says he was supposed to learn this in class, but it was too early for that. This is taught directly before they start taking missions and they weren't supposed to take any missions yet.
    #(Maybe with some illustrations. Shadowed figures of characters.)
    #Anabelle meets w/ Seira and Helena. They reavaluate the two missions:
    #Anabelle says that the butcher was basically defeated by Z before she even got there. She says he's basically the one who took him down.
    #Helena admits that was reluctant to let z joing. But both her daughter and Anabelle praised him a lot, and she says that she officially accepts z and apologises for being cold to him.
    #z is polite to her.
    #z then asks what she meant with her daughter. She says it's Stephanie. Z is surprised.
    #Faceless god mission and butcher missions, both rank B.
    #Z is awarded 40 points for his work. Torr and Candy each 15. All are promoted to purple belts. And so was Centoria.
    #+ S respect.
    #Torr and Candy are so happy. The hug Z.
    #Change their belt in stats screen.
    #Helena says that there's a pressing matter they should also talk about.
    #Tamara follows Gbrla and Vns after they don't report in 5 days. She doesn't come back either.
    #Stfny and Hly are sent on another mission by the time Z comes back.
    #Ymi is the only one dispatchable for the mission to look for them.
    #Anabelle doesn't want yumi to go alone. She says she'll go too.
    #Helena says that she's leaving to the southern village very soon and that Anabelle's duty is to protect the village.
    #Z remembers Tmra's resolve to keep working after coming back from a mission and wants to go w/ Yumi.
    #The mission's level is too high for Centoria, cndy, and Tr. Z says he wants to go, and Anabelle says he can handle himself and vouches for him.
    #Helena agrees to let him go.
    #The mission is rating is increased to B because they didn't come back, Seira goes with them.
    #Anabelle doesn't like sending Yumi, but feels better about it, since Z and S are going w/ her. (Mentions this).
    #Anabelle must stay to protect the village.
    #Helena is needed at souther village and is leaving soon.
    play background_s "audio/Ambient_ninja_village.mp3" volume 0.5 fadeout 1.0 fadein 1.0 loop
    scene v7272 with dissolve
    pause(1)
    z "(Hm... Yumi and Centoria are here, as well. Seems that everyone present at the village is attending... Must be an important meeting.)"
    scene v7273 with dissolve
    pause(1)
    scene v7274 with dissolve
    hlna "..."
    scene v7275 with dissolve
    hlna "Good. Everyone is here."
    pause(1)
    scene black with fade
    pause(1)
    if invited_misty >= 1:
        scene v7276 with dissolve
        hlna "I hope you slept well, dear?"
        scene v7277 with dissolve
        misty "Me?"
        scene v7278 with dissolve
        misty "Yeah. I slept great. Thank you."
        scene v7276 with dissolve
        hlna "Any issues with the uniform?"
        scene v7279 with dissolve
        misty "Ahmm... No. None. It's pretty comfy."
        scene v7280 with dissolve
        hlna "You only have to wear it while taking classes, practicing, or working."
        hlna "Since you're running the cafeteria now, you don't have to attend any classes or practice."
        hlna "But you're still welcome to do so if you'd like."
        scene v7281 with dissolve
        misty "Oh? I see."
        scene v7280 with dissolve
        hlna "Any questions before we jump to the next subject?"
        scene v7282 with dissolve
        misty "Hmmm..."
        scene v7283 with dissolve
        misty "Actually, yeah I have one!"
        scene v7284 with dissolve
        misty "Will I be sent on missions like the others?"
        scene v7276 with dissolve
        hlna "You might. But it depends on the type of expertise the mission requires."
        hlna "Of course, you won't be sent on a combat mission without recieving the proper training or being escorted by a combat-ready ninja. So don't worry."
        scene v7284 with dissolve
        misty "Yeah. It's just that... I'm not really a good fighter... So, I was wondering if that's a problem."
        scene v7280 with dissolve
        hlna "No. You're not a combat ninja. So, it's no problem."
        scene v7285 with dissolve
        misty "That's good..."
        scene v7286 with dissolve
        hlna "Now that that's settled..."
    scene v7287 with dissolve
    hlna "Before we begin discussing the white belt team's missions, I have something to say..." #Looking at the floor.
    scene v7288 with dissolve
    hlna "[mc_name]."
    scene v7289 with dissolve
    z "Hm?"
    scene v7288 with dissolve
    hlna "I..."
    hlna "You probably don't know this, but... I was reluctant to let you join at first..."
    scene v7289 with dissolve
    z "I know."
    scene v7290 with dissolve
    hlna "?!" #Looks at him
    scene v7287 with dissolve
    hlna "Well... We've never had someone from the dark races as a ninja... I hope you can understand where I was coming from..."
    scene v7291 with dissolve
    hlna "However, both Keres Anabelle and my daughter Stephanie, your direct instructor, have spoken very highly of you."
    scene v7292 with dissolve
    z "..." #Looking at a
    scene v7293 with dissolve
    z "(Wait... Her daughter Stephanie?! This is Stephanie's mom?!)"
    scene v7294 with dissolve
    hlna "And they believe you're a very good addition to the village."
    scene v7293 with dissolve
    z "(Gods... That's really nice to hear...)"
    scene v7295 with dissolve
    hlna "So, I apologise if I was harsh towards you." #Bows slightly.
    scene v7296 with dissolve
    hlna "And I'd like to say that I accept you." #Rests her hand on her chest while bowing.
    #Cndy and Torr smiling back at z
    scene v7298 with dissolve
    z "..."
    z "I..."
    z "Thank you, Helena. You honour me."
    scene v7297 with dissolve
    hlna "..." #Smiles.
    scene v7294 with dissolve
    hlna "Now, then. To conclude..."
    scene v7299 with dissolve
    hlna "Torr, Candy, and [mc_name]."
    hlna "You three were initially tasked with a single E-rank mission a few days back."
    hlna "However, your mission faced unforseen and quite unfortunate complications."
    hlna "While this is not uncommon for missions with higher ranks, E-rank missions are usually relatively straightforward."
    scene v7294 with dissolve
    hlna "I understand the belt and mission-ranking system was not yet explained to you in detail."
    hlna "So, I'll break it down for you."
    #Make small sample ninja with various belts and small corresponding monsters and threats.
    hlna "There are seven ranks for missions in term of difficulty."
    play music "audio/Explaining_missions.mp3" volume 0.15 fadeout 4.0 fadein 4.0 loop
    scene v7300_e with dissolve
    hlna "The first and the easiest is rank E."
    scene v7301 with dissolve
    hlna "This is the only rank which white belt ninjas are allowed to take."
    scene v7302 with dissolve
    hlna "It mostly involves simple escort missions and helping around villages and towns. And doesn't involve any risks."
    scene v7300_d with dissolve
    hlna "The second rank is D."
    scene v7303 with dissolve
    hlna "Only red belts and above are allowed to take missions with this rank."
    scene v7304 with dissolve
    hlna "More complex escort missions which involve little risk are usaully ranked D."
    scene v7300_c with dissolve
    hlna "Then, there's rank C."
    scene v7305 with dissolve
    hlna "Yellow belt and above only."
    scene v7306 with dissolve
    hlna "More tricky situations, like resolving public disputes and killing pests are usually missions ranked C."
    scene v7300_b with dissolve
    hlna "Rank B."
    scene v7307 with dissolve
    hlna "Minimum belt: Green."
    scene v7308 with dissolve
    hlna "These types of missions are quite dangerous. Escorting targeted people, dealing with bandits and killers, killing dangerous magical beings... This all falls in this rank."
    scene v7300_a with dissolve
    hlna "Rank A."
    scene v7309 with dissolve
    hlna "No ninja with a belt lower than blue is allowed to take such missions."
    scene v7310 with dissolve
    hlna "Very risky. I've known very skilled ninjas who died carrying out A-ranked missions. The nature of the missions is similar to that in rank B, but the danger is increased greatly."
    stop music fadeout 3.0
    scene v7300_s with dissolve
    hlna "Rank S."
    scene v7311 with dissolve
    hlna "These missions are rare, and only issued to black belts. And usaully, more than one ninja is sent."
    scene v7312 with dissolve
    hlna "Most of those who take such missions... don't come back... Kunoichi in paticular..."
    scene v7313 with dissolve
    z "..."
    scene v7314 with dissolve
    hlna "They usually involve, assassinations, killing very powerful beings, and wars..."
    scene v7300_x with dissolve
    hlna "And finally, rank X."
    z "(There's more?!)"
    scene v7315 with dissolve
    hlna "Very rare. I've yet to witness one being issued. Several black belt ninjas are sent to deal with such missions."
    scene v7316 with dissolve
    hlna "I'm not even sure what type of threat is dealt with here, to tell you the truth..."
    scene v7317 with dissolve
    z "..."
    scene v7318 with dissolve
    hlna "Of course, on the field, several ninjas varying in belt ranks are usually sent on each mission."
    hlna "And in dire situations, the belt requirements can be overridden if need be."
    scene v7319 with dissolve
    hlna "Now, regarding your own mission..."
    hlna "We decided to treat your entire trip not as one, but as three seperate missions."
    scene v7320 with dissolve
    tr "Really? That's great news! There's no way we're not getting promoted now!"
    scene v7321 with dissolve
    hlna "Now, now, Torr. Let's not get too excited."
    scene v7322 with dissolve
    hlna "In order of completion, the first mission was escaping the town of the faceless god."
    scene v7323 with dissolve
    hlna "For Candy and Torr, the mission rank is C."
    scene v7324 with dissolve
    cndy "For us? What about [mc_name]?"
    scene v7323 with dissolve
    hlna "[mc_name] had to face Athena and a fury, the Keres was by his side. But that still counts."
    hlna "The mission rank for [mc_name] is B."
    scene v7325 with dissolve
    z "..." #Surprised while cndy and tr are looking at him.
    scene v7326 with dissolve
    hlna "The three objectives to which you three will be judged are as follows:"
    scene v7327 with dissolve
    z "(I didn't expect this to be this official...)"
    scene v7328 with dissolve
    hlna "One: protecting the person you are escorting."
    scene v7329 with dissolve
    hlna "Two: protecting your team members."
    scene v7330 with dissolve
    hlna "And three: leaving the town as quickly as possible to carry on with your escort mission to Esyl."
    scene v7331 with dissolve
    hlna "You achieved the first and third objectives almost perfectly, so each of you recieves 8 points."
    scene v7332 with dissolve
    tr "Sweet!"
    scene v7334 with dissolve
    hlna "As for the second objective, [mc_name] recieves 5 extra points for being directly responsible for saving Torr's life."
    if v4_obeyed_athena == 0:
        hlna "And additional 15 points for killing the Fury. That's no ordinary feat."
    else:
        hlna "And additional 15 points for your choice, which helped your team slip out a very difficult situation."
    scene v7335 with dissolve
    z "(Whoa... That's a lot... Right?)"
    scene v7336 with dissolve
    hlna "It should be noted, though. Torr, if your rank were higher, you'd have lost points for that mistake which endangered you and indirectly endangered your teammates. But I won't subtract anything from you since you're a white belt..."
    scene v7337 with dissolve
    tr "..."
    scene v7338 with dissolve
    tr "S-Sorry..."
    scene v7333 with dissolve
    hlna "Now for the second mission. Escorting Karolina to Esyl."
    scene v7334 with dissolve
    hlna "The mission was completed with little to no problems, considering the obstacles you had to face."
    hlna "You each receive 8 points."
    scene v7339 with dissolve
    tr "Whoa! So many points!"
    scene v7340 with dissolve
    tr "Wait... How many do I have now?" #Starts counting with her fingers.
    scene v7323 with dissolve
    hlna "And finally. Dealing with the butcher."
    hlna "If the Keres's plan worked, the mission rank would be D."
    hlna "However, since you three had to face him directly, the mission rank is increased to A."
    scene v7341 with dissolve
    tr "!" (multiple=2)
    cndy "!" (multiple=2)
    scene v7342 with dissolve
    cndy "You mean..."
    scene v7343 with dissolve
    tr "We completed an A-ranked mission?!"
    scene v7344 with dissolve
    hlna "Yes. But each of you will be judged based on thier performance, and awarded points accordingly."
    tr "..."
    scene v7345 with dissolve
    tr "Awww..."
    scene v7346 with dissolve
    hlna "Torr. You did your task of guarding the mansion from the inside until the butcher attacked."
    hlna "You were injured very early and couldn't fight. But you weren't expected to be able to fight the butcher. So it's okay."
    hlna "You'll receive 10 points."
    scene v7347 with dissolve
    tr "Oh! Not bad!"
    scene v7348 with dissolve
    hlna "Candy. Like Torr, you did your guarding task. But you couldn't fight the butcher either."
    hlna "You took care of Torr. And let her rest her injured head on your lap, which was good."
    scene v7349 with dissolve
    hlna "But... you should've dragged her carefully inside, or at least away from the fight."
    scene v7350 with dissolve
    cndy "Oh..."
    scene v7351 with dissolve
    hlna "You receive 12 points."
    cndy "..."
    scene v7352 with dissolve #Tr grabs her shoulder.
    tr "Not bad, not bad." #Cndy smiles at her.
    scene v7348 with dissolve
    hlna "Now... [mc_name]."
    scene v7293 with dissolve
    z "Yeah."
    scene v7336 with dissolve
    hlna "You were the first to notice the butcher's illusion."
    hlna "Not only that, but you made the right decision to rush to your teammates, who were being attacked."
    hlna "And you saved Candy's life."
    hlna "I can't believe I'm saying this... But you also defeated the butcher... practically..."
    scene v7334 with dissolve
    hlna "You receive 25 points."
    scene v7354 with dissolve
    z "25?!"
    scene v7355 with dissolve
    tr "Wait... You only need thirty to get to purple..." #Counting with her fingers while grabing cndy's shoulder.
    tr "How many does [mc_name] have in total? It's more than 30, right?"
    scene v7356 with dissolve
    tr "And I have..."
    tr "Errr... I..."
    scene v7357 with dissolve
    hlna "All three of you are promoted to purple belt."
    tr "..."
    tr "We... We..."
    play audio "audio/rustle.mp3"
    scene v7358 with vpunch
    tr "CANDY! I DID IT! I'M PURPLE BELT!" #Hugs cndy. (Climbs on her)
    cndy "Heheheheh."
    $ z_rank_change = 1
    $ cndy_rank_change = 1
    $ tr_rank_change = 1
    $ renpy.notify("Torr, Candy's rank is now purple belt.")
    scene v7359 with dissolve
    #Pause Looking at each other.
    tr "..." (multiple=2)
    cndy "..." (multiple=2) #They look at z
    scene v7360 with dissolve
    tr "..." (multiple=2)
    cndy "..." (multiple=2)
    #They both hug him.
    #Change their belt in stats.
    play audio "audio/rustle.mp3"
    scene v7361 with vpunch
    z "!"
    scene v7362 with dissolve
    z "*Chuckles. Congrats, guys!" #Both looking at him smiling.
    scene v7363 with dissolve
    $ cndy_res += 5
    $ tr_res += 5
    $ s_res += 3
    $ cndy_trst += 5
    $ tr_trst += 5
    $ cndy_aff += 5
    $ tr_aff += 5
    #Buttons!
    play sound "audio/stats.wav"
    show screen button_aff with dissolve
    hide screen button_aff with dissolve
    play sound "audio/stats.wav"
    show screen button_trst with dissolve
    hide screen button_trst with dissolve
    play sound "audio/stats.wav"
    show screen button_res with dissolve
    hide screen button_res with dissolve
    scene v7365 with dissolve
    hlna "Well done, you three. You should be proud."
    scene v7366 with dissolve
    #All three looking at helena while z is hugging them.
    #If I can make more than one daiglogue box appear with one for each.
    Character("All") "Thanks!"
    scene v7367 with dissolve
    hlna "Unfortunately, there's another less pleasant matter at hand."
    hlna "A day after the white belt team left on their mission, another group of ninjas left on a mission in a nearby village."
    scene v7368 with dissolve
    hlna "The ninjas were: Gabriella, white belt, Tamara, purple belt, and Venus, brown belt."
    scene v7369 with dissolve
    z "But why did Tamara go? I thought the mission had to do with an illness... And it was assigned to Venus and Gabbie, if I recall."
    scene v7368 with dissolve
    hlna "Yes. But she insisted on going. She was probably worried about Venus, who wasn't fully recovered. And Gabriella is an amateur. So, I welcomed Tamara's suggestion to go with them."
    scene v7369 with dissolve
    z "Hmm... (That girl is more mature and caring than she lets on, huh?)"
    scene v7368 with dissolve
    hlna "Anyway, like [mc_name] said, the mission involved a fever that has been spreading amongst the villagers there."
    hlna "Their medic came down with it too, so we sent them ours. It was supposed to be simple enough."
    scene v7370 with dissolve
    hlna "However, we haven't recieved word from them since."
    scene v7289 with dissolve
    z "What?"
    scene v7371 with dissolve
    hlna "Yes. I'm just as surprised as you are, [mc_name]. And honestly, quite worried..."
    hlna "Unfortunately, I have to leave tomorrow to the southern village. So I can't go myself."
    hlna "The mission to follow the medic team is to be treated as a B-rank mission."
    hlna "Seeing how all the brown belts are already dispatched, the only option at the moment is to send Yumi."
    scene v7372 with dissolve
    ymi "..." #Surprised.
    scene v7373 with dissolve
    ymi "Me?"
    scene v7374 with dissolve
    a "Just a moment, Helena! Yumi hasn't fully recovered yet!"
    scene v7375 with dissolve
    ymi "Yes, I am. I'm fine! I can go!"
    scene v7376 with dissolve
    a "But..."
    scene v7377 with dissolve
    a "Fine. I'll go too."
    scene v7371 with dissolve
    hlna "No. Keres. You can't. I'm leaving tomorrow. A Keres or a black belt must always be present at the village to protect it. You could go with the white-belt team last time because I was here..."
    scene v7378 with dissolve
    s "Well... I know I'm not officially affiliated to the village. But I can stay if you need help here."
    scene v7379 with dissolve
    hlna "That's very generous of you, Keres Seira. But there must always be at least one black belt ninja or the assigned Keres at each village. Those are the rules."
    scene v7380 with dissolve
    z "..."
    scene v7381 with dissolve
    z "How about I go with Yumi?"
    scene v7382 with dissolve
    hlna "[mc_name]? You only just got to purple belt. A B-rank mission requires green belts and higher, I just explained this."
    scene v7381 with dissolve
    z "But you also said the minimum belt ranks can be overridden if the need arises."
    hlna "..."
    scene v7383 with dissolve
    hlna "Well... At least someone has been paying close attention."
    scene v7382 with dissolve
    hlna "But I can't allow you to go."
    scene v7381 with dissolve
    z "Just hear me out. We are obviously undermanned here. And I think it's better if more than one person went."
    z "If the situation is really bad, one of us could stay to help, while the other runs back here to report or call for more help."
    scene v7383 with dissolve
    hlna "Hmmm... Good point there..."
    scene v7384 with dissolve
    a "Yeah. He has a talent for that. His insight on difficult situations is very good."
    scene v7386 with dissolve
    a "And he's also very capable, Helena. I've seen it first hand."
    scene v7385 with dissolve
    a "And..."
    scene v7384 with dissolve
    a "If I'm really honest here... I'd feel a lot better knowing that [mc_name] is going with my little sister."
    scene v7387 with dissolve
    hlna "..."
    scene v7388 with dissolve
    hlna "But-"
    scene v7378 with dissolve
    s "How about I go too?"
    s "I may not be able to fill in for one of you here, but there are no rules against me helping them on their mission, right?"
    scene v7389 with dissolve
    hlna "Well... Yes. You're quite right."
    scene v7390 with dissolve
    hlna "Actually, that's..."
    scene v7391 with dissolve
    hlna "Yeah... Let's do that."
    scene v7389 with dissolve
    hlna "Thank you, Keres Seira."
    scene v7391 with dissolve
    hlna "Very well. [mc_name], Keres Seira, and Yumi will go."
    scene v7392 with dissolve
    hlna "Remember: your objective is to help but also to report the situation to us as quickly as possible."
    scene v7393 with dissolve
    ymi "Yeah. Understood."
    scene v7391 with dissolve
    hlna "You three will leave tomorrow at first light. So, take the rest of the day off, and prepare."
    scene v7394 with dissolve
    z "Got it."
    pause(1)
    #Z is walking out.
    #After, Seira is taking to a outside about disobaying or obaying Athena.
    scene v7395 with Fade(0.5,1,0.5)
    pause(0.7)
    a "You think so?"
    scene v7396 with dissolve
    s "I'm not sure..."
    z "?"
    s "Athena is his sister after all, and they're both olympians..."
    scene v7397 with dissolve
    s "!" #Notices z
    scene v7398 with dissolve
    z "Errr... Didn't mean to eavesdrop..."
    scene v7399 with dissolve
    s "You're not."
    scene v7400 with dissolve
    s "*Sighs."
    if v4_obeyed_athena == 0:
        scene v7401 with dissolve
        s "We were just talking about how the conflict with Athena could cause issues with my father as well."
        scene v7402 with dissolve
        z "Your father?"
        scene v7401 with dissolve
        s "Yes. Ares."
        s "You see. The order of the Keres is ultimately loyal to Ares."
        s "Unlike most the olympians, he doesn't usually concern himself with what mortals do."
        s "But if a Keres should gain Athena's wrath... This could lead to problems between Ares and Athena."
        scene v7402 with dissolve
        z "I see..."
        z "So... I could've gotten Anabelle in trouble?"
        scene v7403 with dissolve
        a "No! I alone am responsible for my actions, [mc_name]."
        scene v7404 with dissolve
        a "Also... We're just talking, you know."
        a "Athena has other things to do. She probably forgot about the whole encounter by now."
        scene v7405 with dissolve
        z "Hm..."
    else:
        scene v7401 with dissolve
        s "We were just talking about how obaying Athena was probably for the best, after all."
        s "Any conflict with her might have caused problems with my father..."
        scene v7402 with dissolve
        z "Your father?"
        scene v7401 with dissolve
        s "Yes. Ares."
        s "You see. The order of the Keres is ultimately loyal to Ares."
        s "Unlike most the olympians, he doesn't usually concern himself with what mortals do."
        s "But if a Keres should gain Athena's wrath... This could lead to problems between Ares and Athena."
        scene v7402 with dissolve
        z "I see..."
        z "So... We probably did the right thing, after all?"
        scene v7404 with dissolve
        a "I suppose..."
        a "But, well... We're just talking, you know."
        a "Olympians tend to be busy. Athena probably forgot about the whole encounter by now."
        scene v7405 with dissolve
        z "Hm..."
    scene v7404 with dissolve
    a "Honestly, don't go worrying about this stuff."
    a "You have a big mission tomorrow, you need to rest properly."
    scene v7405 with dissolve
    z "Yeah. You're right."
    #Turns.
    scene v7406 with dissolve
    pause(1.5)
    a "Oh, and [mc_name]."
    scene v7407 with dissolve
    z "Hm?"
    scene v7408 with dissolve
    a "Thank you... for offering to go with Yumi..."
    scene v7409 with dissolve
    z "Don't mention it, Anabelle."
    scene v7410 with dissolve
    a "You too, Seira. I'm so glad you guys are going with her."
    scene v7411 with dissolve
    s "Hmm..."
    pause(1)
    stop sound fadeout 1.0
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    scene black with fade
    #Later
    pause(2.5)
    #6) Torr and Candy in their room: {@100%@100%R@0%W}
    #Torr remarks how ever since Z showed up, good things happened to them. And that she has been trying to get to purple belt for months, and now she got it thanks to him. "At least, partly thanks to him..."
    #Tr and cndy sitting in their room eating snacks.
    #Close up shot to tr.
    #ONLY IF AFF WITH TORR IS HIGH!!!!!!!!!!!!!!!!!!!
    if tr_aff >= 16:
        scene v7412 with dissolve
        pause(1)
        scene v7413 with dissolve
        tr "Say..."
        scene v7414 with dissolve
        cndy "Hmmm?" #Eating
        scene v7415 with dissolve
        play sound "audio/crunch.wav"
        tr "Can you believe we got to purple belt? It feels we've been stuck at white belt for ages..."
        scene v7416 with dissolve
        cndy "I mean... We only started a few weeks ago... I don't think it's even been two months for me... And you joined even later..."
        scene v7417 with dissolve
        tr "I know. That's not..."
        scene v7418 with dissolve
        tr "You notice how ever since [mc_name] got here, things... like... changed?"
        scene v7419 with dissolve
        cndy "..." #Looking at tr
        scene v7420 with dissolve
        play sound "audio/crunch.wav"
        tr "Like... Things were stuck... And he set them in motion or something..."
        scene v7421 with dissolve
        cndy "..." #Looking at tr
        scene v7422 with dissolve
        tr "..." #Looking at cndy
        scene v7423 with dissolve
        tr "Look; just because I'm an elf, doesn't mean I'm a poet, okay? I'm just saying... Good things have happened ever since he... like... came along and stuff..."
        scene v7424 with dissolve
        play sound "audio/crunch.wav"
        tr "..." #Looking in the distance
        if choice_variable_ch7_1 == 1:
            scene v7425 with dissolve
            tr "You notice how he also kinda smells good when you hug him?"
            scene v7426 with dissolve
            tr "Like... not like we smell. Like... manly... kinda in a good way..."
            scene v7427 with dissolve
            tr "..." #Looking in the distance
        scene v7428 with dissolve
        cndy "Oooohhh... Someone is in looooooooooovvvveeee!" #Gets closer
        play sound "audio/Slap.mp3" volume 0.2
        scene v7429 with vpunch
        tr "H-Huh?!" #Pushes candy away.
        scene v7430 with dissolve
        tr "Th-The fuck are you t-talking about?!"
        scene v7431 with dissolve
        tr "I don't fucking like him or anything! It's just that..."
        tr "I'm just saying, that... like..."
        scene v7432 with dissolve
        cndy "..." (multiple=2) #Playfull smile
        tr "..." (multiple=2) #Looking at candy surprised
        play sound "audio/Slap.mp3" volume 0.2
        scene v7433 with vpunch
        tr "F-Fuck off!" #Pushing her further annoyed.
        pause(1)
        scene black with fade
        #Later
        pause(2.5)
    #7) Next morning.  {@100%@100%R@0%W}
    #Next day...
    #ymi feeding the cat.
    #Z is wearing purple belt!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Cat leaves food and rubs himself on z's leg
    play background_s "audio/Ambient_ninja_village.mp3" fadeout 1.0 fadein 1.0 loop
    scene v7434 with dissolve
    pause(2.5)
    play sound "audio/sliding door.mp3"
    scene v7435 with dissolve
    pause(1.5)
    play sound "audio/meow.wav"
    scene v7436 with dissolve
    cat "Meow."
    play sound "audio/purring.mp3" volume 0.5 loop
    scene v7437 with dissolve
    z "Oh. Hey there, little guy."
    scene v7438 with dissolve
    stop sound fadeout 1.0
    z "Hey, Yumi."
    scene v7439 with dissolve
    ymi "Morning."
    ymi "What exactly did you do to make him like you this much?"
    scene v7438 with dissolve
    z "I didn't do anything. I guess he's just friendly."
    scene v7439 with dissolve
    ymi "*Giggles. No he's not! Aside from me, he only likes Candy. And now you, I guess."
    scene v7440 with dissolve
    ymi "Apparently, he likes you more than food. Which says a lot."
    scene v7441 with dissolve
    z "Heh."
    scene v7442 with dissolve
    z "So... Does he have a name?"
    scene v7443 with dissolve
    ymi "Eh? Name?"
    ymi "I never really thought of that..."
    scene v7444 with dissolve
    z "Hmmm... I think he should have one."
    scene v7445 with dissolve
    ymi "We could just call him 'the cat', like we always do."
    scene v7446 with dissolve
    z "I guess..."
    z "But would you like it if we started calling you 'the girl'?"
    scene v7447 with dissolve
    ymi "Whaaaat? There are like ten girls around here aside from me. But he's the only cat around."
    scene v7448 with dissolve
    z "How about... 'the girl with blue eyes and black hair' then?"
    scene v7447 with dissolve
    ymi "That's too long, though. Aren't things named out of convenience?"
    scene v7448 with dissolve
    z "..."
    z "Errr... Good point..."
    z "I'll get back to you when I think of a counter argument, okay?"
    scene v7447 with dissolve
    ymi "I'll be waiting."
    scene v7448 with dissolve
    z "So? Are you ready?"
    scene v7449 with dissolve
    ymi "Yep."
    ymi "You?"
    scene v7450 with dissolve
    z "Yeah."
    scene v7451 with dissolve
    ymi "Are you sure you're up to this? You only returned two days ago... And your last mission wasn't exactly simple, [mc_name]."
    scene v7452 with dissolve
    z "Honestly, I'm fine. A whole day's rest is more than enough for me. Besides, I wasn't injured or anything."
    ymi "Hmmm..."
    scene v7453 with dissolve
    ymi "About that... Did anyone figure out how you can heal so quickly?"
    scene v7452 with dissolve
    z "Nahh... It remains a mystery, I guess..."
    scene v7451 with dissolve
    ymi "Doesn't it bother you?"
    ymi "That there are some things about yourself you don't know yet?"
    scene v7453 with dissolve
    ymi "I heard you don't remember anything from your past before you met Seira, not even your parents... Is it true?"
    scene v7452 with dissolve
    z "..."
    z "I remember glimpses here and there... but... Yeah... I don't remember my parents."
    z "And it does bother me a little, I suppose..."
    z "But I know I was very lucky to have Seira."
    scene v7453 with dissolve
    ymi "I see..."
    ymi "But if Elnor is really your father, and your mother is Demeter..."
    scene v7451 with dissolve
    ymi "Don't you want to meet her?"
    scene v7452 with dissolve
    z "..."
    menu:
        "No. Seira is all I need. [ModGreen](Seira Love +5)":
            $ choice_variable_ch7_12 = 1
            z "Not really. As far as I'm concerned, Seira is all I need."
            $ s_aff += 5
            #Button
            play sound "audio/stats.wav"
            show screen button_aff with dissolve
            hide screen button_aff with dissolve
            scene v7454 with dissolve
            ymi "Hmmm... I like your answer... Kinda."
            scene v7455 with dissolve
            z "You do? Thanks, I guess..."
            z "Besides, from my limited expertise with the gods, they're mostly assholes..."
            scene v7456 with dissolve
            ymi "Ahahahahah... True!"
            scene v7457 with dissolve
            pause(1)
        "I suppose...":
            $ choice_variable_ch7_13 = 1
            z "Maybe... I'd like to get to know my real mother one day..."
            scene v7453 with dissolve
            ymi "Hmmm... I see..."
    scene v7458 with dissolve
    ymi "I'm sorry. I was just curious. You're quite interesting, you know. Even Annie thinks so. And you sort of remind me of my brother. Before he..."
    scene v7459 with dissolve
    z "Hm?"
    scene v7460 with dissolve
    ymi "The point is... Sorry for poking into this stuff."
    scene v7461 with dissolve
    z "No. It's fine, Yumi. And thanks for finding me interesting... *Chuckles."
    scene v7462 with dissolve
    s "What are you two conspiring about?"
    scene v7463 with vpunch
    ymi "Nothing!" (multiple=2)
    z "Nothing!" (multiple=2)
    scene v7464 with dissolve
    z "How long have you been listening?!"
    scene v7465 with dissolve
    s "Oh... You know... I just got here..."
    scene v7466 with dissolve
    s "So... Apparently it's a four-hours trip to the village. You two should eat something before we leave."
    scene v7467 with dissolve
    ymi "Oh. I already ate."
    scene v7468 with dissolve
    z "I didn't..."
    scene v7469 with dissolve
    s "Go get something to eat, then. We're leaving soon."
    scene v7468 with dissolve
    z "Yeah... Okay."
    pause(1)
    scene black with fade
    #Later
    pause(2.5)

    #8) Cafeteria {@100%@100%R@0%W}
    #GIVE TORR A HAIRCUT WITH MOVABLE HAIR!!!!!!!!!!!!!!!!!!!!!!!!!!! <------------------------------------------------------------------
    #They're wearing casual clothes. or purple belts.
    if invited_misty >= 1:
        scene v7470 with dissolve
        pause(1)
        scene v7471 with dissolve
        misty "Sorry for the wait, guys." #Brings them food.
        scene v7472 with dissolve
        play audio "audio/pouring.mp3"
        misty "Congratulations on the new belts, by the way!" #misty giving them food (Different) and says:
        scene v7473 with dissolve
        tr "Thanks, Misty." (multiple=2) #Together.
        cndy "Thanks!" (multiple=2) #Together.
        scene v7474 with dissolve
        misty "Enjoy!"
        scene v7475 with dissolve
        misty "Hm?" #Looks at z.
        scene v7477 with dissolve
        z "Hey, Misty."
        scene v7476 with dissolve
        misty "Good morning, [mc_name]!"
        scene v7477 with dissolve
        z "I-"
        scene v7478 with vpunch
        tr "Hey! How come Misty gets a 'hey' but we don't?"
        scene v7479 with dissolve
        z "I literally see you two everyday... But I was gonna say 'hey' to you guys in a second..."
        tr "Hmmm..." #Not convinced.
        scene v7480 with dissolve
        z "I see there's some new... ehm... dishes! ...on the menu!"
        scene v7481 with dissolve
        misty "Yeah. I didn't know what I was supposed to make. Apparently there's a girl called Hailey who was supposed to show me the ropes, but she's not around right now."
        scene v7482 with dissolve
        misty "So, I had to get a little creative."
        scene v7483 with dissolve
        z "Oh. Interesting. I think we could use some creativity with food around here."
        scene v7484 with dissolve
        misty "Would you like to try some?"
        scene v7485 with dissolve
        cndy "It's really good. Even better that the potato chips. You definitely should try it."
        scene v7486 with dissolve
        z "Oh, okay. Then I'll have some, please. I was supposed to eat something before we leave."
        if went_w_hailey == 1:
            pause(1)
            z "By the way..."
            z "This doesn't contain meat by any chance... does it?"
            scene v7487 with dissolve
            misty "Err... Yeah. It does. I didn't know you didn't eat meat."
            scene v7488 with dissolve
            z "Hmmm... Not really about meat in general... it's just..."
            scene v7489 with dissolve
            misty "Oh! Is it because you don't want to eat that giant rat creature?"
            z "(How did she...)"
            scene v7490 with dissolve
            misty "Don't worry. It's just bird meat. I caught them today, too. So the meat is very fresh."
            scene v7491 with dissolve
            z "You..."
            z "You went to the woods to hunt birds today?!"
            scene v7487 with dissolve
            misty "Hunted? Woods?"
            scene v7488 with dissolve
            z "What?"
            scene v7487 with dissolve
            misty "What?"
            misty "I just caught them in my web."
            scene v7488 with dissolve
            z "..."
            z "......"
            z "Did you just say you caught them in your web?"
            scene v7487 with dissolve
            misty "Yep."
            scene v7492 with dissolve
            misty "Here! I'll show you." #Starts walking signaling z to follow her.
            pause(1)
            scene v7493 with Fade(0.5,1,0.5)
            pause(0.7)
            misty "See?"
            z "..."
            scene v7494 with dissolve #Huge spider web with a few birds caught in it.
            z "..."
            scene v7495 with vpunch
            z "YOU COULD DO THAT?!"
            z "That's so..."
            menu:
                "[ModGreen]...cool! (Misty Love +2)":
                    $ choice_variable_ch7_14 = 1
                    z "...cool! Probably one of the most amazing abilities I've ever seen!"
                    scene v7496 with dissolve
                    misty "!" #Surprised.
                    scene v7497 with dissolve
                    misty "*Giggles. Th-Thanks!" #Looks away timidly
                    $ misty_aff += 2
                    play sound "audio/stats.wav"
                    show screen button_aff with dissolve
                    hide screen button_aff with dissolve
                    scene v7498 with dissolve
                    z "How does it work? Do you-"
                    scene v7499 with vpunch
                    misty "No! Th-They don't come out of my b-butt!"
                    scene v7500 with dissolve
                    z "..."
                    misty "..."
                    z "Errr... I wasn't gonna say that..."
                    scene v7501 with dissolve
                    misty "You weren't?"
                    scene v7502 with dissolve
                    misty "*Clears her throat. Anyway I can shoot them from my hands."
                    scene v7503 with dissolve
                    misty "It takes a while to build a whole net, though. But it's a lot easier because I've got four hands..."
                    scene v7504 with dissolve
                    z "I see..."
                    scene v7505 with dissolve
                    misty "Come on. Let's go back. I'll make you some food, okay?"
                    scene v7506 with dissolve
                    z "Yeah. Sounds good."
                "...weird.":
                    $ choice_variable_ch7_15 = 1
                    z "Err... A bit weird... to be honest."
                    scene v7507 with dissolve
                    misty "Oh..."
                    scene v7508 with dissolve
                    z "I guess it's really 'handy', though."
                    z "Pun intended."
                    scene v7509 with dissolve
                    misty "Ahahah. Yeah."
                    scene v7505 with dissolve
                    misty "I didn't want to cook that rat thing. So I though this would be better."
                    misty "Let's go back. I'll make you some food, okay?"
                    scene v7506 with dissolve
                    z "Yeah. Sounds good."
            pause(1)
        else:
            scene v7510 with dissolve
            misty "Sure. Just a second!" #Goes to the kitchen.
        scene v7511 with Fade(0.5,1,0.5)
        pause(1)
        z "..." #Sits down.
        scene v7512 with dissolve
        tr "So... You're leaving now?"
        scene v7513 with dissolve
        z "In an hour or so. Yeah."
        scene v7514 with dissolve
        tr "You planning to make it to black belt in a month or what?"
        scene v7515 with dissolve
        z "Huh? It's not really about the belt ranking, Torr."
        z "Actually... this may sound a bit sudden. But I'm curious..."
        z "Why do you want to reach the black belt this much? Is there a particular reason, or..."
        if tr_trst >= 10:
            scene v7516 with dissolve
            tr "..."
            scene v7517 with dissolve
            tr "I guess we're like... friends now... So, I don't mind telling you..."
            scene v7518 with dissolve
            tr "So... I never actually told this to anyone except for Candy..."
            scene v7519 with dissolve
            play music "audio/ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0
            tr "Back home, my father's family was famously blessed from the god of fire, Hephaestus."
            tr "Some say we all descended from a demi-god who was his son."
            scene v7520 with dissolve
            tr "You know how Anabelle and Yumi are blessed from Helios because of their brother?"
            tr "It would've been something like that."
            scene v7519 with dissolve
            tr "Others say our family never had a demi-god, but simply devoted itself to maintain Hephaestus's temple for generations."
            tr "But... Well... The point is..."
            scene v7521 with dissolve
            tr "We were supposed to be great fighters because of this, you know."
            tr "We all have good fire magic and all. But that aside, no one in my family was ever considered a good fighter."
            tr "My father, my uncles, even my cousins... they all couldn't even make it to soldiers in the city."
            scene v7519 with dissolve
            tr "And I tried too. I tried my luck at the try-outs to become a soldier. But I didn't make it either."
            tr "I don't have any brothers. Just a little sister. And everone was hoping that at least I could make it."
            tr "You see... I have more than one blessing. While my father's side is blessed from Hephaestus, my mother's is said to be similarly blessed from Demeter."
            scene v7522 with dissolve
            tr "Which is why I have this mark on my forehead, and why I have a connection to trees." #Points at the mark (maybe moving her hair aside?)
            scene v7519 with dissolve
            tr "Anyway... After I failed, I tried to join a group called the hunters of Artemis. They only accepted women, apparently. So I thought I should try there... That I could prove myself there..."
            tr "But I could never find them... I searched for weeks."
            tr "So, I lastly decided to come here to try and join the ninja village."
            tr "And it was great that I was accepted. But it still wasn't enough to prove that I could be a great fighter..."
            scene v7520 with dissolve
            tr "Apparently, almost anyone could make it to white belt. Right?"
            scene v7523 with dissolve
            z "So you want to get to black to prove that you can be a great fighter?"
            scene v7519 with dissolve
            tr "Do you think it's silly?"
            scene v7523 with dissolve
            z "No. I didn't say that."
            scene v7519 with dissolve
            tr "But?"
            scene v7523 with dissolve
            menu:
                "Why do you even need to prove that?":
                    $ choice_variable_ch7_16 = 1
                    z "I mean... Why do you need to prove that? And to whom?"
                    scene v7521 with dissolve
                    tr "I want my family and myself to be respected amongst the elves!"
                    scene v7519 with dissolve
                    tr "And I want to make my parents and my little sister proud!"
                    scene v7523 with dissolve
                    z "Hmmm..."
                    z "Well... Why not... It's a fine goal."
                    z "It's nothing obsessive or self-destructive."
                    z "If anything, pursuing it will be benificial to you after all."
                    scene v7524 with dissolve
                    tr "Hmmm..."
                    scene v7525 with dissolve
                    tr "I'm glad you think so."
                "No buts. I think it's a solid goal to pursue.":
                    $ choice_variable_ch7_17 = 1
                    z "No buts, really. I think it's a fine goal."
                    z "It's nothing obsessive or self-destructive."
                    z "If anything, pursuing it will be benificial to you after all."
                    scene v7524 with dissolve
                    tr "Hmmm..."
                    scene v7525 with dissolve
                    tr "I'm glad you think so."
        else:
            scene v7516 with dissolve
            tr "..."
            scene v7526 with dissolve
            tr "Er... Me?"
            tr "It's nothing particular. No. I just think it'd be... cool and stuff."
            scene v7527 with dissolve
            tr "Yeah. You?"
            scene v7528 with dissolve
            z "Hm? Me? I'm not really bothered how quickly I reach it."
            scene v7529 with dissolve
            tr "Oh... Cool."
            scene v7530 with dissolve
            z "(Seems there's more to it, but... she doesn't want to talk about it. Let's not push her.)"
        scene v7531 with dissolve
        play sound "audio/plate.mp3"
        stop music fadeout 1.0
        misty "And, here's your food!"
        scene v7532 with dissolve
        z "Thanks, Misty."
    else: #(Misty isn't here.)
        #Tr and Cndy are simply standing at the cafeteria's door.
        scene v7533 with dissolve
        pause(1)
        scene v7534 with dissolve
        z "Morning."
        scene v7535 with dissolve
        tr "Oh, hey, [mc_name]."
        scene v7536 with dissolve
        cndy "Errr... Are you here for breakfast?" #Worried look
        scene v7534 with dissolve
        z "Yeah. Something wrong?"
        scene v7536 with dissolve
        cndy "Well..."
        #Cnt leans out of the cafeteria.
        scene v7537 with dissolve
        cnt "Hm?"
        scene v7538 with dissolve
        cnt "Morning, [mc_name]."
        scene v7539 with dissolve
        z "Err... Morning, Centoria."
        z "What are you doing in there?"
        scene v7538 with dissolve
        cnt "There's no one to run the cafeteria while Hailey is away. So, I was assigned here today."
        cnt "Shall I make you some food, as well?"
        scene v7539 with dissolve
        z "Hmm... Well, yes, please."
        #Smoke starts coming out
        scene v7540 with dissolve
        play sound "audio/fire_in_kitchen.mp3" volume 0.5
        pause(1.2)
        z "Err..."
        z "I think something is burning inside..."
        scene v7541 with dissolve
        cnt "Eh? Where?" #Turns around
        scene v7542 with dissolve
        cnt "OH, NO!"
        pause(1.0)
        stop sound fadeout 1
        scene v7543 with Fade(0.5,1,0.5)
        pause(1.0) #They're sitting down with burned food. (Use scat?)
        play sound "audio/slime.mp3"
        scene v7544 with dissolve
        cndy "Hmmm..." #Tries touching it with her finger.
        scene v7545 with dissolve
        cndy "Mmm..." #Licks it
        scene v7546 with dissolve
        pause(1.0)
        scene v7547 with dissolve
        cndy "!" #Makes a funny expression.
        scene v7548 with dissolve
        cndy "Ugh!" #Spits it.
        scene v7549 with dissolve
        tr "Sheeesh... Was it that bad?" #Cndy is wiping her mouth
        scene v7550 with dissolve
        cndy "You're welcome to try it..."
        scene v7551 with dissolve
        tr "..."
        scene v7552 with dissolve
        tr "Nah... I'm good."
        scene v7553 with dissolve
        z "Damn... I was supposed to eat something before I leave..."
        scene v7558 with dissolve
        tr "You're leaving now?"
        scene v7553 with dissolve
        z "In an hour or so. Yeah."
        scene v7554 with dissolve
        tr "You planning to make it to black belt in a month or what?"
        scene v7553 with dissolve
        z "Huh? It's not really about the belt ranking, Torr."
        z "Actually... this may sound a bit sudden. But I'm curious..."
        z "Why do you want to reach the black belt this much? Is there a particular reason, or..."
        if tr_trst >= 10:
            scene v7555 with dissolve
            tr "..."
            scene v7556 with dissolve
            tr "I guess we're like... friends now... So, I don't mind telling you..."
            scene v7557 with dissolve
            tr "So... I never told this to anyone except for Candy..."
            scene v7558 with dissolve
            play music "audio/ninja_village.mp3" volume 0.2 fadeout 1.0 fadein 1.0
            tr "Back home, my father's family was famously blessed from the god of fire, Hephaestus."
            scene v7556 with dissolve
            tr "Some say we all descended from a demi-god who was his son."
            scene v7558 with dissolve
            tr "You know how Anabelle and Yumi are blessed from Helios because of their brother?"
            scene v7554 with dissolve
            tr "It would've been something like that."
            scene v7558 with dissolve
            tr "Others say our family never had a demi-god, but simply devoted itself to maintain Hephaestus's temple for generations."
            tr "But... Well... The point is..."
            scene v7556 with dissolve
            tr "We were supposed to be great fighters because of this, you know."
            scene v7558 with dissolve
            tr "We all have good fire magic and all. But that aside, no one in my family was ever considered a good fighter."
            tr "My father, my uncles, even my cousins... they all couldn't even make it to soldiers in the city."
            scene v7556 with dissolve
            tr "And I tried too. I tried my luck at the try-outs to become a soldier. But I didn't make it either."
            scene v7558 with dissolve
            tr "I don't have any brothers. Just a little sister. And everone was hoping that at least I could make it."
            tr "You see... I have more than one blessing. While my father's side is blessed from Hephaestus, my mother's is said to be similarly blessed from Demeter."
            scene v7559 with dissolve
            tr "Which is why I have this mark on my forehead, and why I have a connection to trees." #Points at the mark (maybe moving her hair aside?)
            scene v7558 with dissolve
            tr "Anyway... After I failed, I tried to join a group called the hunters of Artemis. They only accepted women, apparently. So I thought I should try there... That I could prove myself there..."
            tr "But I could never find them... I searched for weeks."
            tr "So, I lastly decided to come here to try and join the ninja village."
            tr "And it was great that I was accepted. But it still wasn't enough to prove that I could be a great fighter..."
            scene v7554 with dissolve
            tr "Apparently, almost anyone could make it to white belt. Right?"
            scene v7553 with dissolve
            z "So you want to get to black to prove that you can be a great fighter?"
            scene v7558 with dissolve
            tr "Do you think it's silly?"
            scene v7553 with dissolve
            z "No. I didn't say that."
            scene v7558 with dissolve
            tr "But?"
            scene v7553 with dissolve
            menu:
                "Why do you even need to prove that?":
                    $ choice_variable_ch7_16 = 1
                    z "I mean... Why do you need to prove that? And to whom?"
                    scene v7554 with dissolve
                    tr "I want my family and myself to be respected amongst the elves!"
                    scene v7556 with dissolve
                    tr "And I want to make my parents and my little sister proud..."
                    scene v7553 with dissolve
                    z "Hmmm..."
                    z "Well... Why not... It's a fine goal."
                    z "It's nothing obsessive or self-destructive."
                    z "If anything, pursuing it will be benificial to you after all."
                    scene v7560 with dissolve
                    tr "Hmmm..."
                    scene v7561 with dissolve
                    tr "I'm glad you think so."
                "No buts. I think it's a solid goal to pursue.":
                    $ choice_variable_ch7_17 = 1
                    z "No buts, really. I think it's a fine goal."
                    z "It's nothing obsessive or self-destructive."
                    z "If anything, pursuing it will be benificial to you after all."
                    scene v7560 with dissolve
                    tr "Hmmm..."
                    scene v7561 with dissolve
                    tr "I'm glad you think so."
        else:
            scene v7555 with dissolve
            tr "..."
            scene v7562 with dissolve
            tr "Er... Me?"
            tr "It's nothing particular. No. I just think it'd be... cool and stuff."
            scene v7563 with dissolve
            tr "Yeah. You?"
            scene v7564 with dissolve
            z "Hm? Me? I'm not really bothered how quickly I reach it."
            scene v7565 with dissolve
            tr "Oh... Cool."
            scene v7566 with dissolve
            z "(Seems there's more to it, but... she doesn't want to talk about it. Let's not push her.)"
        scene v7553 with dissolve
        stop music fadeout 1.0
        z "Well, guys. I'd love to sit and chat a bit more, but I have to get ready..."
        scene v7567 with dissolve #IF I can make both names appear on screen.
        cndy "Yeah. Take care." (multiple=2)
        tr "Bye, [mc_name]." (multiple=2)
        scene v7568 with dissolve
        pause(1.0)
    #9) Just before they leave. @100%@100%R@0%W}
    #Anabelle headpating Yumi before they leave telling her to be careful. Head pats Z too after he looks at them (If enough points).
    #Z says it's embarrassing. A tells him to let her do it. He's already becoming a man, if she doesn't do it now, it might be too late to do this sort of thing later.
    #While pating both their heads, she tells them to take care of each other.
    #Goes to gate.
    #Seira, Anabelle, and Yumi is there.
    scene black with fade
    #Later
    pause(2.5)
    scene v7569 with dissolve
    pause(1)
    z "(Everyone is here already... Is that Anabelle?)"
    scene v7570 with dissolve #Approaches
    a "And don't cause the Keres any trouble."
    scene v7571 with dissolve
    ymi "Annie! I'm not going to cause anyone trouble!"
    scene v7572 with dissolve
    a "And don't forget to-" #Ymi notices z.
    play audio "audio/slight_hit.mp3"
    scene v7573 with dissolve
    ymi "Okay! I got it!" #Removes anabelles' hand while blushing.
    scene v7574 with dissolve
    a "Hm?"
    scene v7575 with dissolve
    a "Oh. [mc_name]."
    scene v7576 with dissolve
    z "(A new look? She looks nice.)"
    a "..."
    if a_aff >= 2:
        play audio "audio/rustle.mp3"
        scene v7578 with Dissolve(2.0)
        #Head pats him with Ymi.
        z "!"
        scene v7579 with dissolve
        z "Errr... Anabelle? This is a bit... embarrassing..."
        scene v7580 with dissolve
        a "Now, now. You're already twice as big as I am. You'll be a fully grown man in no time... If I don't do this now, it might be too late later."
        scene v7581 with dissolve
        z "..."
        scene v7582 with dissolve
        a "Take care of each other, okay?"
        scene v7583 with dissolve
        ymi "Okay..." #Super embarrassed
        scene v7584 with dissolve
        z "Yeah..." #Looking at her face
        scene v7585 with dissolve
        z "..." #Gaze drift down to her cleavage uncontously
        scene v7586 with dissolve
        a "..." #Notices.
        scene v7587 with dissolve
        z "(Shit! Did she catch me staring?)"
        scene v7588 with dissolve
        a "Oh? Is it the look?"
        a "Sorry! I didn't have time to dress up. I was really busy, stayed up all night with piles of paper work because of my long absence and I lost track of time..."
        scene v7589 with dissolve
        z "H-Huh?! Are you really okay?!"
        z "(Thank the gods...)"
        scene v7590 with dissolve
        a "Don't worry! It's not the first time I've done this. It's really efficient. The only downside is that I end up looking like a dead specter..."
        scene v7589 with dissolve
        z "Nonsense! You always look great!"
        scene v7591 with dissolve
        a "..." #A bit surprised.
        z "(Woops! That slipped out! Why is interacting with this girl so fucking difficult...)"
        scene v7592 with dissolve
        pause(1)
        play audio "audio/flick.mp3"
        scene v7593 with vpunch
        #with vpunch
        a "Flirt!" (multiple=2) #flicks his nose and smiles
        z "Aww!" (multiple=2) #At the same time.
        $ a_lst += 1
        $ a_aff += 1
        play sound "audio/stats.wav"
        show screen button_aff with dissolve
        hide screen button_aff with dissolve
        play sound "audio/stats.wav"
        show screen button_lst with dissolve
        hide screen button_lst with dissolve
        scene v7594 with dissolve
        pause(1)
        # S behind them giving z thumps up.
    else:
        #Simply stops headpating ymi.
        scene v7577 with dissolve
        a "Take care, okay?"
        scene v7576 with dissolve
        z "Yeah. I will."
    scene v7595 with dissolve
    s "Okay, guys. Time to go. I want to make it there before nightfall."
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    #Later
    play background_s "audio/rain.mp3" fadeout 1.0 fadein 1.0 loop
    pause(2.5)
    #Rainy at the village.
    #The party reaches the village.
    #From a higher position, Z looks at the village and says:
    show v7m5 with dissolve
    pause(1)
    z "(So quiet and peaceful...)"
    z "(Yet I'm having this eerie feeling...)"
    z "(And it seems, everytime I get a bad feeling, something bad happens...)"
    z "(I guess Irena had a point about this... succubus instinct...)"
    z "(Or did she...)"
    z "(I had a really bad feeling about the butcher, and it turned out fine. Didn't it?)"
    if invited_misty == 0:
        z "(Or maybe it's just because I'm really hungry...)"
    scene v7597 with dissolve
    ymi "Something wrong, [mc_name]?"
    scene v7598 with dissolve
    z "..."
    scene v7599 with dissolve
    pause(1)
    scene v7600 with dissolve
    z "Nah... Let's keep going."
    scene v7601 with dissolve
    $ renpy.pause(1, hard=True)
    hide screen button_1 with dissolve
    show v7m6 with Dissolve(2.5)
    $ renpy.pause(9.5, hard=True)
    play sound "audio/mirror.mp3" volume 0.4
    $ renpy.pause(1.5, hard=True)
    show v7m7 with dissolve
    $ renpy.pause(5, hard=True)
    hide v7m6
    show mirror with Dissolve(2.0)
    $ renpy.pause(5, hard=True)
    scene black
    $ renpy.pause(3, hard=True)
    #Video with chapter name here !!!! <--------------------------------
    scene v7602 with Dissolve(2.0)
    show screen button_1 with dissolve
    play music "audio/die_zwei_geschwister.mp3" volume 0.7 fadeout 1.0 fadein 1.0
    pause(2)
    scene v7603 with dissolve
    pause(2)
    scene v7604 with dissolve
    pause(2)
    scene v7605 with dissolve
    pause(2)
    scene v7606 with dissolve
    pause(2)
    #They reach the village (Inside)
    #There's no one walking in the streets.
    s "Hmm... Why is there no one around?"
    scene v7607 with dissolve
    ymi "This can't be a good sign... Right?"
    scene v7608 with dissolve
    s "..." #Looks at ymi
    scene v7609 with dissolve
    z "Is there some kind of... town hall or something where we can probably find some people... You know, ask around, maybe."
    scene v7610 with dissolve
    ymi "There probably is one around here somewhere..."
    scene v7611 with dissolve
    s "Let's split up and try to find it. Regroup back here in five minutes if we can't find anything."
    scene v7612 with dissolve
    z "Sounds good."
    scene v7613 with dissolve
    ymi "Err... Okay..."
    scene v7614 with dissolve
    pause(1)
    #Split up.
    scene black with fade
    #Later
    pause(1)
    scene v7615 with dissolve
    pause(1)
    z "..."
    scene v7616 with dissolve
    z "..." #Walking around
    scene v7617 with dissolve
    z "(There really is no one around...)"
    pause(0.7)
    #Rustling sounds.
    play audio "audio/rustle 2.mp3"
    pause(0.7)
    scene v7618
    z "Hm?!"
    scene v7619 with dissolve
    z "Hello?!"
    z "(What was that?!)"
    z "(Or did I imagine it...)"
    z "(Or maybe it's a cat or something... Don't get spooked now, [mc_name]. You've been through tougher shit already.)"
    #Walking some more.
    scene v7620 with dissolve
    z "(It feels like the whole place has been abandoned or something...)"
    pause(1.5)
    scene v7621 with dissolve
    z "(Are all those buildings empty? Where did everyone go?)"
    scene v7622 with dissolve
    pause(0.7)
    scene v7623 with dissolve
    z "(Seems like there's no one home...)"
    pause(1.7)
    #Sound <---------------------------------
    scene v7624
    stop music
    play audio "audio/Venus_on_glass.mp3"
    pause(0.8)
    #Venus looks out of the window, or her eye looks through the keyhole. (She's wearing a mask and one of her earings is missing.)
    play audio "audio/Falling.mp3"
    scene v7625 with vpunch
    z "AHH!" #Falls on the ground.
    pause(1.2)
    play audio "audio/creaky door.mp3"
    scene v7626 with dissolve
    #Opens the door.
    pause(0.8)
    z "Venus?! Is that you?!"
    vns "..."
    scene v7627 with dissolve
    vns "Hm?" #Lowers her mask.
    scene v7628 with dissolve
    ymi "[mc_name]?! Are you okay?! I heard you shout just now!" #Comes running.
    scene v7629 with dissolve
    z "Yumi? I'm fine, I'm fine. Venus just scared the shit out of me."
    scene v7630 with dissolve
    z "Again..."
    scene v7631 with dissolve
    vns "Oh. [mc_name]. It's just you..."
    scene v7632 with dissolve #Stands up.
    vns "What are you doing creeping around the village and looking through the window like that?"
    scene v7633 with dissolve
    z "Oh. Well-"
    scene v7634 with dissolve
    ymi "Venus?! Are you guys okay?"
    scene v7635 with dissolve
    vns "Hm? What do you mean?"
    scene v7636 with dissolve
    ymi "We came because you guys didn't come back to the village! You didn't even send a message!"
    ymi "So... What's going on?! Also, why is no one walking around the village?"
    scene v7637 with dissolve
    vns "Well... Gabbie and I told them to stay at their homes. So that the illness doesn't spread quickly. It spreads easily through the air from the looks of it, which is why I was wearing a mask..."
    vns "And, yeah... I'm fine. Tamara caught it, though... She's sleeping right now."
    scene v7638 with dissolve
    ymi "Tamara?! Gods, is she..."
    vns "Hm?"
    scene v7639 with dissolve
    vns "What? No. She's probably going to be fine... I got it too and recovered. I'm totally fine now."
    scene v7640 with dissolve
    ymi "Oh..."
    scene v7641 with dissolve
    z "What about Gabbie?"
    scene v7642 with dissolve
    vns "Well, Gabbie never actually developed any symptoms. I guess she's immune or something."
    scene v7643 with dissolve
    ymi "So..."
    ymi "If you and Gabbie are doing fine, why didn't you report back to the village, or at least send someone to bring us the info?"
    scene v7644 with dissolve
    vns "Hmmmm..."
    scene v7645 with dissolve
    vns "Well... Did I have to do that? I didn't think it was necessary..."
    scene v7646 with dissolve
    ymi "..."
    scene v7647 with dissolve
    ymi "How did you even become a brown belt ninja..." #facepalms
    scene v7648 with dissolve #Seira comes running.
    s "You guys okay?! I heard shouting a minute ago!"
    scene v7649 with dissolve
    z "We're fine, Seira! We found Venus!"
    scene v7650 with dissolve
    z "So... Is this where you and Gabbie treat the sick people?"
    scene v7651 with dissolve
    vns "Yeah. I asked them to clear this house for that. I didn't want them spreading it to the others."
    scene v7652 with dissolve
    z "And how serious is it? The illness?"
    scene v7651 with dissolve
    vns "It can give you a strong fever, which is really hard to bring down. But so long as you have someone like me to care for you, you should be fine."
    vns "Most of those who got it are mostly healed right now. Gabbie took care of me when I had it. She said I only needed a day to recover from most of the symptoms."
    vns "And thankfully, no one died so far."
    scene v7652 with dissolve
    z "I see... That doesn't sound too bad."
    scene v7651 with dissolve
    vns "Gabbie and her mom are still working on a treatment, though. Should help people recover faster. Some people have been here for almost a week."
    vns "I guess not everyone recovers as quickly as I do."
    scene v7652 with dissolve
    z "Oh."
    z "Wait..."
    z "She's working with..."
    z "HER MOTHER?!" with vpunch
    scene v7651 with dissolve
    vns "Err... Yeah?"
    scene v7652 with dissolve
    z "She went back to her mother's house in the mountain?"
    scene v7651 with dissolve
    vns "What? No. Her mother lives here."
    scene v7652 with dissolve
    z "What? No, she doesn't."
    scene v7651 with dissolve
    vns "She totally does."
    scene v7652 with dissolve
    z "Trust me. She doesn't. They were basically our neighbors back in the day. I'm one hundred percent certain tha-"
    play audio "audio/creaky door.mp3"
    scene v7653 with dissolve #Gabbie opens the door to the house next to them
    gbrla "Yes, mother! Right away!"
    z "..."
    scene v7654 with dissolve
    frnsska "And bring some petals from that purple flower with the small leaves!"
    scene v7655 with dissolve
    jnfr "Mother! Don't shout! The sick people are sleeping in the house next to us!"
    scene v7656 with dissolve
    z "..."
    scene v7657 with dissolve
    jnfr "..." #Looks at z
    scene v7658 with dissolve
    jnfr "[mc_name]?"
    if jnfr_trst >= 1:
        scene v7659 with dissolve
        z "(Oh! Jenny is here too! I hope thing aren't awkward after last time...)"
        pause(1)
    else:
        scene v7659 with dissolve
        z "(Oh! Jenny is here too!)"
        pause(1)
    #Jumps and hugs him
    play audio "audio/rustle.mp3"
    scene v7660 with vpunch
    jnfr "[mc_name]!"
    if jnfr_trst >= 1:
        z "(Guess not.)"
    scene v7661 with dissolve
    jnfr "What are you doing here?! Did you come to visit us in our new house?"
    scene v7662 with dissolve
    z "Err... I'm actually here on a mission. I didn't know you guys moved... But I'm certainly happy to see all of you guys!"
    scene v7663 with dissolve
    jamie "Darling? Did you see my gold watch? I can't find it!"
    scene v7664 with dissolve
    z "Hmm... Maybe most of you..."
    scene v7665 with dissolve
    jnfr "Ahahah! Stop it!"
    scene v7666 with dissolve
    jnfr "It's probably somewhere in the room you took as your closet, Jamie!"
    scene v7667 with dissolve
    jamie "It's not-"
    scene v7668 with dissolve
    jamie "Hm?"
    scene v7669 with dissolve
    jamie "Darling? Who's this elf with blonde hair? We've met before..."
    scene v7670 with dissolve
    z "Yeah. We have. I'm-"
    scene v7671 with dissolve
    jamie "Right! You're the mailman!"
    scene v7672 with dissolve
    z "Huh?!"
    scene v7673 with dissolve
    jamie "I actually had a very important letter for Lord Ax-"
    scene v7674 with dissolve
    jnfr "He's not the damn mailman, Jamie! Gods!"
    scene v7675 with dissolve
    jamie "He's not?"
    scene v7674 with dissolve
    jnfr "No! Would you please start paying more attention to regular people! I'm friends with some of them, you know!"
    scene v7676 with dissolve
    jamie "Hmmm..."
    scene v7677 with dissolve
    play audio "audio/Door close.mp3"
    jamie "*Goes back inside."
    scene v7678 with dissolve
    jnfr "..."
    scene v7679 with dissolve
    z "(Gods... I can't help but fucking hate this dude...)"
    #Seira in the background talking to fransiska.
    scene v7680 with dissolve
    jnfr "Err... Sorry about him, [mc_name]. He can be a bit of an... ass sometimes..."
    define jxj = 10
    scene v7681 with dissolve
    pause(1)
    menu:
        "[ModGreen]Why are you even with this prick? (Jeniffer Love +2)":
            $ choice_variable_ch7_18 = 1
            z "*Sighs. Why are you even dating him?"
            $ jxj -= 1
            scene v7682 with dissolve
            jnfr "Well... We're not 'dating'. We're betrothed. It's different. I don't think I'd date someone like him normally..."
            scene v7680 with dissolve
            jnfr "But... I don't know. It's complicated. And he's not so bad. We just... don't really know each other... or do anything together, basically."
            scene v7683 with dissolve
            jnfr "Anyway. You don't need to hear my complaining! I bet you have enough on your plate already. You're on a ninja mission, right?"
            scene v7684 with dissolve
            z "Hey, now. You know I always have time for you, Jenny!" #Puts his hand on her shoulder
            scene v7685 with dissolve
            jnfr "..."
            $ jnfr_aff += 2
            play sound "audio/stats.wav"
            show screen button_aff with dissolve
            hide screen button_aff with dissolve
            z "And I didn't mean to pry into your affairs or anything, I ju-"
            scene v7686 with dissolve
            jnfr "Nah, dude. It's cool. I get what you mean."
            scene v7687 with dissolve
            jnfr "I should probably go help him find his watch, though. He's going to turn our room on its head if I don't."
            scene v7683 with dissolve
            jnfr "See you around. Come visit us while you're here, okay?"
            scene v7684 with dissolve
            z "I will."
            #leaves.
        "Don't worry about it.":
            $ choice_variable_ch7_19 = 1
            z "Yeah. No. Don't worry about it, Jenny."
            scene v7687 with dissolve
            jnfr "Sorry. I should probably go help him find his watch. He's going to turn our room on it's head if I don't."
            scene v7683 with dissolve
            jnfr "See you later, though. Come visit us while you're here, okay?"
            scene v7684 with dissolve
            z "I will."
    #Turns around.
    pause(1)
    scene v7688 with dissolve
    z "Hm? (Where did everyone go?)"
    scene v7689 with dissolve
    s "I think they went inside the town hall to talk."
    scene v7690 with dissolve
    z "Oh."
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    play background_s "audio/rain_inside.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    #Later
    pause(2.5)
    #Inside the hall:
    #Yumi is sitting with Venus and the man who issued the quest from chapter 4
    scene v7691 with dissolve
    pause(0.8)
    ymi "What about the village's medic? Has he not recovered yet?"
    scene v7692 with dissolve
    vns "I'm afraid not... We isolated him and his family with the other sick people in an empty house about a week ago. I've been working there ever since."
    scene v7693 with dissolve
    ymi "Hmmm..."
    scene v7694 with dissolve
    play music "audio/mysterious_and_mystic.mp3" volume 0.5 fadeout 1.0 fadein 2.0
    ymi "So... This doctor you mentioned... Where did she go?"
    scene v7695 with dissolve
    Character("Man") "We don't know. She stayed at the medic's cottage for a few days after she arrived, since it was empty at the time. But one day, she didn't show up to help Venus. We went to the cottage. It was a mess."
    scene v7694 with dissolve
    ymi "A mess? As in..."
    scene v7695 with dissolve
    Character("Man") "Books, bottles, tools, even furniture thrown around everywhere."
    scene v7696 with dissolve
    z "Sorry. I just got here. Whom are we talking about?"
    scene v7697 with dissolve
    ymi "A traveling doctor who visited the village to help with the fever situation. She was helping Venus and Gabbie with the sick, until she went missing a few days back."
    scene v7698 with dissolve
    z "Hmm..."
    scene v7696 with dissolve
    z "And you said her place was a mess?"
    scene v7699 with dissolve
    Character("Man") "The place she was staying in. Yes."
    scene v7697 with dissolve
    ymi "What are you thinking?"
    scene v7698 with dissolve
    z "Well. I'd say that usually means whoever was the reason for her disappearance must've searched her house for something, causing the mess..."
    z "But maybe I'm overreaching here... I'm just back from the butcher's investigation, after all..."
    scene v7700 with dissolve
    s "Yeah. But you still have a point. This does sound suspicious..."
    scene v7701 with dissolve
    z "Think we should take a look around the place?"
    scene v7702 with dissolve
    vns "Err... I already searched the house. Also, I thought you guys came to help with the sickness situation?"
    scene v7698 with dissolve
    z "I mean... Yes. But you said the sickness isn't that worrying, right?"
    z "Besides, maybe this would even provide further insight into this whole situation... Like help us get the full picture of what's going on, you know?"
    scene v7704 with dissolve
    vns "Hmmm... I guess."
    scene v7703 with dissolve
    vns "Okay. Maybe I missed something. I'll help you investigate."
    scene v7705 with dissolve
    pause(0.8)
    #tries to stand up and falls.
    play audio "audio/chair.mp3"
    scene v7706 with dissolve
    vns "Ah!" (multiple=2)
    ymi "!" (multiple=2)
    play audio "audio/Falling.mp3"
    scene v7707 with vpunch
    stop music fadeout 2.0
    pause(1.2)
    scene v7708 with dissolve
    vns "Aww..."
    z "Venus? Are you okay?"
    scene v7709 with dissolve
    vns "Yeah, yeah. Don't worry. I'm fine."
    scene v7710 with dissolve
    ymi "Think you should take it easy? You've probably been overworking yourself... Since we three are here now, we should split tasks. Just tell us what to do."
    scene v7711 with dissolve
    vns "No, no. Honestly, it's nothing like that! I'm fine. I just randomly fell. I promise."
    scene v7712 with dissolve
    ymi "..."
    scene v7713 with dissolve
    vns "Come on, [mc_name]. I'll take you there."
    scene v7714 with dissolve
    vns "Yumi, I just need you to make sure you give the sick people water if they're thirsty."
    scene v7715 with dissolve
    ymi "Okay, I got it. I'll have a look at them too if that's okay. I know a thing or two about healing."
    scene v7716 with dissolve
    vns "Yeah. Sure. Go ahead."
    pause(1.0)
    scene black with fade
    #Later
    stop background_s fadeout 1.0
    play background_s "audio/rain.mp3" fadeout 1.0 fadein 1.0 loop
    pause(2.5)
    #11) medic's cottage. {@100%@100%R@0%W}
    #On the way to the cottage:
    scene v7717 with dissolve
    pause(1.0)
    z "So... This doctor. You met her, right?"
    scene v7718 with dissolve
    vns "Yeah. She got here two days before we did, apparently."
    scene v7719 with dissolve
    vns "I worked with her for three days, I think..."
    scene v7720 with dissolve
    vns "And on the fourth day, she wasn't there..."
    scene v7721 with dissolve
    vns "She usually got to the sick house before I woke up. She used to wake me most of the time."
    scene v7722 with dissolve
    z "Hmmm... Wait... You sleep at the sick house?"
    scene v7723 with dissolve
    vns "Well, yeah. Just to make sure everyone gets what they need."
    scene v7724 with dissolve
    z "(She's pretty dedicated, huh? Seems to be the case for almost every ninja I've met so far...)"
    scene v7725 with dissolve
    z "..."
    z "(The morale also seems quite high in the ninja village... And everyone is friendly and kind...)"
    scene v7726 with dissolve
    z "(Well, almost everyone...)"
    scene v7727 with dissolve
    vns "Something on your mind?"
    scene v7728 with Dissolve(2.0)
    z "!" #Mutiple
    z "H-Huh? No! Nothing!"
    vns "..."
    z "Errr... So, where do the others sleep?"
    scene v7729 with dissolve
    vns "Well, Gabbie is staying at her mother's. They let Tamara stay there too, but then she got sick and we had to move her to the sick house."
    scene v7728 with dissolve
    z "I-Is that so... (Why is she so close...)"
    scene v7730 with dissolve
    vns "We're here."
    z "Hm?"
    play music "audio/Eerie.mp3" volume 0.7 fadeout 1.0 fadein 1.0
    scene v7731 with Dissolve(2.0) #Looks at house. It looks super creepy.
    z "..."
    scene v7732 with dissolve
    z "*Gulps."
    scene v7733 with dissolve
    z "And you said you searched it already?"
    scene v7734 with dissolve
    vns "Yeah. Just the day the doctor disappeared."
    scene v7735 with dissolve
    z "All on your own, huh?"
    scene v7734 with dissolve
    vns "Why do you ask?"
    scene v7735 with dissolve
    z "Nothing. No reason. Nope."
    z "(Well, if Venus came her and took a look inside alone, I can't act like a coward here...)"
    z "Shall we go in?"
    vns "..."
    scene v7734 with dissolve
    vns "Yeah. Let's."
    pause(1)
    stop background_s fadeout 1.0
    scene black with fade
    play background_s "audio/rain_inside.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    pause(1) #Go in.
    #Messed up inside. (The place is big, it's a house). (Can be similar to Frnsska's house).
    scene v7736 with dissolve
    z "..."
    scene v7737 with dissolve
    z "(It really is a mess...)"
    scene v7738 with dissolve
    vns "Let's split up. You search the upper floor and I'll search here."
    scene v7739 with dissolve
    z "Split up?"
    z "(Is that really such a good idea...)"
    vns "..."
    pause(0.7)
    scene v7740 with Dissolve(2)
    vns "You're not scared, are you?" #Teasing him.
    scene v7741 with dissolve
    z "Ah..."
    scene v7742 with dissolve
    z "H-Huh?! I have no idea what you're talking about..."
    scene v7740 with dissolve
    vns "You sure?" #Teasing him.
    scene v7743 with dissolve
    z "Yup! Positive."
    vns "Hmmmm..."
    z "Tell you what, I'll search the upper floor and you search here, like you suggested. Once we're done, we'll switch to make sure the other one didn't miss anything. Sound good?"
    vns "..."
    scene v7738 with dissolve
    vns "Sure."
    scene v7744 with dissolve
    vns "Here. Take this." #Gives him a candle.
    scene v7745 with dissolve
    z "A candle?"
    scene v7744 with dissolve
    vns "Yeah. The house is really dark. It'll come in handy."
    scene v7739 with dissolve
    z "Thanks. I'm heading upstairs, then."
    pause(1)
    scene black with fade
    pause(1)
    play audio "audio/creak.mp3"
    scene v7747 with dissolve
    pause(1)
    #Goes upstairs. (Creepy hallway.)
    #Image buttons on doors would be cooler. <-------------------------------------
    #############VN MODE!!!!!!!!!!!!!!!!!################################ <------------------------------------------------
    #Button and variable definintion:
    screen ch7_upstars_room1_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.30
            ypos 0.4
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/arrow_button_h.webp"
            action Jump("ch7_upstars_room1")
    screen ch7_upstars_room2_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.59
            ypos 0.28
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/arrow_button_h.webp"
            action Jump("ch7_upstars_room2")
    screen ch7_upstars_room1_seen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.30
            ypos 0.4
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/ch7_upstars_room1_seen_button_h.webp"
            action Jump("ch7_upstars_room1_seen")
    screen ch7_upstars_room2_seen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.59
            ypos 0.28
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/ch7_upstars_room2_seen_button_h.webp"
            action Jump("ch7_upstars_room2_seen")
    screen ch7_upstars_back_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.52
            ypos 0.82
            idle "images/0.7/other/back_arrow_m.webp"
            hover "images/0.7/other/back_arrow_m_h.webp"
            action Call ("cant_go_back_yet") #Change to : z "(I have to search the rooms first...)"
    screen ch7_upstars_back_seen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.52
            ypos 0.82
            idle "images/0.7/other/back_arrow_m.webp"
            hover "images/0.7/other/back_arrow_m_h.webp"
            action Jump("ch7_go_downstars")

    screen button_vn_mode2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.04
            ypos 0.05
            idle "images/Buttons/vnmode.png"
            hover "images/Buttons/vnmode_h.png"
            action Jump("ch7_vn_mode")

    define ch7_upstars_room1_done = 0
    define ch7_upstars_room2_done = 0
    define ch7_upstars_jumpscare = 0
    label ch7_upstars:
        call hide_all_ch7 from _call_hide_all_ch7
        scene v7747 with dissolve
        pause(1)
        #Goes upstairs. (Creepy hallway.)
        if ch7_upstars_room1_done == 0 and ch7_upstars_room2_done == 0:
            z "..." #Hallway is dark.
            z "(Holy fuck... So dark...)"
            #Lights up candle.
            play audio "audio/match.mp3"
            pause(0.6) #Match sound <----------------------
        if ch7_upstars_room1_done == 1 and ch7_upstars_room2_done == 0 and ch7_upstars_jumpscare == 0:
            play audio "audio/giggle.mp3"
            scene v7751 #Show jumpscare image
            pause(0.7)
        elif ch7_upstars_room1_done == 0 and ch7_upstars_room2_done == 1 and ch7_upstars_jumpscare == 0:
            play audio "audio/giggle.mp3"
            scene v7751 #Show jumpscare image
            pause(0.7)
        if ch7_upstars_jumpscare == 2:
            scene v7752 with dissolve
            z "Venus?!"
        scene v7748 with dissolve
        if ch7_upstars_room1_done == 0 and ch7_upstars_room2_done == 0:
            z "(Okay... That's better...)"
            z "(Looks like there are two rooms here. One with a door, and one without... for some reason.)"
            dev "Please note that the next section was designed to be played with very simple sandbox mechanics. However, I understand that some people
            may prefer to stick to the VN approach."
            show screen button_vn_mode2 with dissolve #Make button appear here <--------------------
            dev "So, this button will override the sandbox mode and change the section to a VN-based one. Feel free to use it if you get stuck at any point or simply prefer to play that way."
        if ch7_upstars_room1_done == 1 and ch7_upstars_room2_done == 0 and ch7_upstars_jumpscare == 0:
            $ ch7_upstars_jumpscare = 1
            z "HUH?!"
            z "HEY!"
            z "Venus?! Is that you?!"
            z "Venus!"
            z "..."
            z "(The fuck was that... Am I seeing thing...)"
        elif ch7_upstars_room1_done == 0 and ch7_upstars_room2_done == 1 and ch7_upstars_jumpscare == 0:
            $ ch7_upstars_jumpscare = 1
            z "HUH?!"
            z "HEY!"
            z "Venus?! Is that you?!"
            z "Venus!"
            z "..."
            z "(The fuck was that... Am I seeing thing...)"
        if ch7_upstars_jumpscare == 2:
            z "(Fuck...)"
            $ ch7_upstars_jumpscare = 3
        pause(0.7)
    if ch7_upstars_room1_done == 0:
        show screen ch7_upstars_room1_button
    else:
        show screen ch7_upstars_room1_seen_button
    if ch7_upstars_room2_done == 0:
        show screen ch7_upstars_room2_button
    else:
        show screen ch7_upstars_room2_seen_button
    if ch7_upstars_room2_done == 0 or ch7_upstars_room1_done == 0:
        call screen ch7_upstars_back_button
    else:
        call screen ch7_upstars_back_seen_button
    #Room labels:
    label cant_go_back_yet:
        z "(I have to search the rooms first...)"
        if ch7_upstars_room2_done == 0 or ch7_upstars_room1_done == 0:
            call screen ch7_upstars_back_button
        else:
            call screen ch7_upstars_back_seen_button
        return
    label ch7_upstars_room1:
        call hide_all_ch7 from _call_hide_all_ch7_1
        $ ch7_upstars_room1_done = 1
        scene v7749 with dissolve #Creepy kid's room.
        pause(1)
        z "(A child's room?)"
        z "(Looks somewhat out of place here...)"
        z "(Wait... Why isn't it a mess like the rest of the house?!)"
        scene v7750 with dissolve
        z "(Even though the door was apparently broken down...)"
        z "..."
        scene v7749 with dissolve
        z "(Weird...)"
        z "(I don't think I'll find anything useful here, though... Right?)"
        pause(0.7)
        if ch7_upstars_room2_done == 1:
            $ ch7_upstars_jumpscare = 2
            play audio "audio/glass_breaking.mp3"
            pause(1.0)
            #Breaking glass sound. <------------------
            z "Huh?!"
            pause(0.7)
            jump ch7_upstars #Goes back out to the hall way.
        jump ch7_upstars
        #Leaves.
    label ch7_upstars_room1_seen:
        call hide_all_ch7 from _call_hide_all_ch7_2
        scene v7749 with dissolve
        pause(1)
        z "(The kid's room. I don't think I'll find anything useful here...)"
        pause(0.7)
        jump ch7_upstars
    label ch7_upstars_room2:
        call hide_all_ch7 from _call_hide_all_ch7_3
        $ ch7_upstars_room2_done = 1
        #Next room is a bathroom.
        play audio "audio/creaky door.mp3"
        scene v7754 with dissolve
        pause(1)
        z "..."
        z "(Looks like it's a bathroom... An old one...)"
        z "(Not much to see here.)"
        pause(0.7)
        if ch7_upstars_room1_done == 1:
            $ ch7_upstars_jumpscare = 2
            play audio "audio/glass_breaking.mp3"
            pause(1.0)
            #Broking glass sound. <------------------
            z "Huh?!"
            pause(0.7)
            jump ch7_upstars #Goes back out to the hall way.
        jump ch7_upstars
    label ch7_upstars_room2_seen:
        call hide_all_ch7 from _call_hide_all_ch7_4
        play audio "audio/creaky door.mp3"
        scene v7754 with dissolve
        pause(1)
        z "(I don't think searching the old and dirty bathroom will help... Not that I want to...)"
        pause(0.7)
        jump ch7_upstars
    label ch7_go_downstars:
        call hide_all_ch7 from _call_hide_all_ch7_5
    #Go back towards the stairs.
    scene v7755 with dissolve
    z "Venus?"
    play audio "audio/creaky stairs.mp3"
    scene v7756 with dissolve
    z "..."
    scene v7757 with dissolve
    z "VENUS!"
    play sound "audio/footsteps.mp3"
    pause(1.7)
    "*Footstep sounds behind you."
    z "..."
    menu:
        "Turn around.":
            stop sound
            pause(0.5)
    play audio "audio/jump_scare_very_light.mp3"
    scene v7758
    pause(0.7)
    #Jumpscare venus.
    #Sound <------------------------
    scene v7759 with vpunch
    z "Fuck!"
    scene v7760 with dissolve
    vns "What?!"
    scene v7761 with dissolve
    z "..."
    z "How the fuck did you even get behind me?!"
    scene v7762 with dissolve
    vns "Errr... I was standing here when you came down."
    scene v7763 with dissolve
    z "So why didn't you say anything?!"
    scene v7764 with dissolve
    vns "I don't know. Should I have?"
    scene v7765 with dissolve
    z "..."
    z "Nevermind..."
    z "I heard some glass break just a minute ago. Was that you?"
    scene v7766 with dissolve
    vns "Eh? Glass? No. I didn't hear anything like that."
    scene v7765 with dissolve
    z "Hm... (Weird...)"
    z "Well... I'm done upstairs. Are you done here?"
    scene v7764 with dissolve
    vns "Errr... Sure. I've already looked around here a few days ago anyway."
    scene v7765 with dissolve
    z "Okay. Let's switch then."
    scene v7767 with dissolve
    pause(1)
    #Vns leaves.
    scene v7768 with dissolve
    z "(Okay. Which room should I investigate first?)"
    #Image buttons on doors would be cooler. <-------------------------------------
    #Button and variable definintion:
    screen ch7_first_floor_kitchen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1
            ypos 0.8
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/arrow_button_h.webp"
            action Jump("ch7_first_floor_kitchen")
    screen ch7_first_floor_masterbedrroom_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.346
            ypos 0.19
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/arrow_button_h.webp"
            action Jump("ch7_first_floor_masterbedrroom")
    screen ch7_first_floor_doctorbedrroom_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.62
            ypos 0.22
            idle "images/0.7/other/arrow_button_db.webp"
            hover "images/0.7/other/arrow_button_db_h.webp"
            action Jump("ch7_first_floor_doctorbedrroom")
    screen ch7_first_floor_kitchen_seen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 1
            ypos 0.8
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/ch7_first_floor_kitchen_seen_button_h.webp"
            action Jump("ch7_first_floor_kitchen")
    screen ch7_first_floor_masterbedrroom_seen_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.346
            ypos 0.19
            idle "images/0.7/other/arrow_button.webp"
            hover "images/0.7/other/ch7_first_floor_masterbedrroom_seen_button_h.webp"
            action Jump("ch7_first_floor_masterbedrroom")
    screen ch7_first_floor_back_button:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.79
            idle "images/0.7/other/back_arrow.webp"
            hover "images/0.7/other/back_arrow_h.webp"
            action Jump("first_floor_ch7")
    define ch7_first_floor_kitchen_done = 0
    define ch7_first_floor_masterbedrroom_done = 0
    define ch7_first_floor_doctorbedrroom_done = 0

    label first_floor_ch7:
        call hide_all_ch7 from _call_hide_all_ch7_6
        scene v7768 with dissolve
        if ch7_first_floor_masterbedrroom_done == 1 and ch7_first_floor_kitchen_done == 1:
            z "Hm? (There seems to be one more room I haven't checked out yet...)"
            show screen ch7_first_floor_kitchen_seen_button
            show screen ch7_first_floor_masterbedrroom_seen_button
            call screen ch7_first_floor_doctorbedrroom_button
        else:
            if ch7_first_floor_kitchen_done == 0:
                show screen ch7_first_floor_kitchen_button
            else:
                show screen ch7_first_floor_kitchen_seen_button
            if ch7_first_floor_masterbedrroom_done == 0:
                call screen ch7_first_floor_masterbedrroom_button
            else:
                call screen ch7_first_floor_masterbedrroom_seen_button

    #Room labels:
    label ch7_first_floor_kitchen:
        call hide_all_ch7 from _call_hide_all_ch7_7
        scene v7769 with dissolve
        pause(1)
        $ ch7_first_floor_kitchen_done = 1
        if ch7_first_floor_kitchen_Knife_done == 0 and ch7_first_floor_kitchen_Food_done == 0 and ch7_first_floor_kitchen_Vials_done == 0:
            z "(Quite a few things were going on here from the looks of it...)"
        if ch7_first_floor_kitchen_Knife_done == 1 and ch7_first_floor_kitchen_Food_done == 1 and ch7_first_floor_kitchen_Vials_done == 1:
            z "(Hmm... I doubt I'll find anything else in the kitchen...)"
        show screen ch7_first_floor_kitchen_Knife_button
        show screen ch7_first_floor_kitchen_Food_button
        show screen ch7_first_floor_kitchen_Vials_button
        call screen ch7_first_floor_back_button

        #kitchen exploration buttons and variables:
        screen ch7_first_floor_kitchen_Knife_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.575
                ypos 0.20
                idle "images/0.7/other/ch7_first_floor_kitchen_Knife_button.webp"
                hover "images/0.7/other/ch7_first_floor_kitchen_Knife_button_h.webp"
                action Jump("ch7_first_floor_kitchen_Knife")
        screen ch7_first_floor_kitchen_Food_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.71
                ypos 0.83
                idle "images/0.7/other/ch7_first_floor_kitchen_Food_button.webp"
                hover "images/0.7/other/ch7_first_floor_kitchen_Food_button_h.webp"
                action Jump("ch7_first_floor_kitchen_Food")
        screen ch7_first_floor_kitchen_Vials_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.875
                ypos 0.5
                idle "images/0.7/other/ch7_first_floor_kitchen_Vials_button.webp"
                hover "images/0.7/other/ch7_first_floor_kitchen_Vials_button_h.webp"
                action Jump("ch7_first_floor_kitchen_Vials")
        define ch7_first_floor_kitchen_Knife_done = 0
        define ch7_first_floor_kitchen_Food_done = 0
        define ch7_first_floor_kitchen_Vials_done = 0

        #kitchen exploration labels:
        label ch7_first_floor_kitchen_Knife:
            call hide_all_ch7 from _call_hide_all_ch7_8
            scene v7773 with dissolve
            #Gets closer.
            if ch7_first_floor_kitchen_Knife_done == 1:
                z "(Maybe someone used the knife to hang something on the wall? Like a paper or a note of some sort...)"
                z "(But if that were the case, the note is long gone...)"
                pause(0.7)
                jump ch7_first_floor_kitchen
            else:
                $ ch7_first_floor_kitchen_Knife_done = 1
                z "(What's this? Why is knife sticking out of the wall like this?)"
                z "(No real signs of a fight or anything... I mean, sure it's a mess. But that's the case everywhere.)"
                z "(The mess is more likely to be due to someone searching the house rather than a fight all around the house.)"
                z "Hmm..."
                z "(Maybe someone used the knife to hang something on the wall? Like a paper or a note of some sort...)"
                z "(But if that were the case, the note is long gone...)"
                pause(0.7)
                jump ch7_first_floor_kitchen
        label ch7_first_floor_kitchen_Food:
            call hide_all_ch7 from _call_hide_all_ch7_9
            scene v7770 with dissolve
            #Gets closer.
            if ch7_first_floor_kitchen_Food_done == 1:
                z "(The food was probably put here by the traveling doctor...)"
                z "(The cup still has something in it... Either whoever made it didn't get to finish it, or forgot it.)"
                z "(But assuming it was the doctor who left the cup. The first option seems more likely...)"
                pause(0.7)
                jump ch7_first_floor_kitchen
            else:
                $ ch7_first_floor_kitchen_Food_done = 1
                z "(Seems it has been here for a few days, but it hasn't started to rot yet.)"
                z "(The medic's family got sick and were taken out of the house over a week ago. I don't think this stuff has been here for that long...)"
                z "(So, that was probably put here by the traveling doctor...)"
                z "(The cup still has something in it... Either whoever made it didn't get to finish it, or forgot it.)"
                z "(But assuming it was the doctor who left the cup. The first option seems more likely...)"
                pause(0.7)
                jump ch7_first_floor_kitchen
        label ch7_first_floor_kitchen_Vials:
            call hide_all_ch7 from _call_hide_all_ch7_10
            scene v7771 with dissolve
            #Gets closer.
            #Alchemy stuff. pistle and mortor.
            if ch7_first_floor_kitchen_Vials_done == 1:
                z "(Alchemy isn't really my area. Venus must've seen this and decided if there was anything useful here already.)"
                pause(0.7)
                jump ch7_first_floor_kitchen
            else:
                $ ch7_first_floor_kitchen_Vials_done = 1
                z "(Looks like someone was trying to make a cure, I guess...)"
                scene v7772 with dissolve
                z "(The books in the bottom shelf look like someone has gone through them. Not very delicately at that...)"
                scene v7771 with dissolve
                z "(I really can't tell whether this was the work of the doctor or the medic...)"
                z "(It's not really my area. Venus must've seen this and decided if there was anything useful here already.)"
                pause(0.7)
                jump ch7_first_floor_kitchen
    label ch7_first_floor_masterbedrroom:
        call hide_all_ch7 from _call_hide_all_ch7_11
        scene v7774 with dissolve
        pause(1)
        if ch7_first_floor_masterbedrroom_done == 1:
            z "(Probably the master bedroom. I doubt I'll find anything useful here. I'm looking for stuff left behind by the doctor...)"
            pause(0.7)
            jump first_floor_ch7
        else:
            $ ch7_first_floor_masterbedrroom_done = 1
            z "(Hmmm... This is probably the master bedroom.)"
            z "(From the looks of it, whoever searched the house must've looked in here too. But I doubt I can find anything useful here. I'm looking for stuff left behind by the doctor...)"
            pause(0.7)
            jump first_floor_ch7
    label ch7_first_floor_doctorbedrroom:
        call hide_all_ch7 from _call_hide_all_ch7_12
        scene v7775 with dissolve
        pause(1)
        if ch7_first_floor_doctorbedrroom_bedside_done == 0 and ch7_first_floor_doctorbedrroom_desk_done == 0:
            z "(Another bedroom... Could be a guest bedroom. Maybe the doctor slept here?)"
            z "(If so, this room is definitely worth searching thoroughly.)"
        #Drawers next to bed.

        if ch7_first_floor_doctorbedrroom_desk_done == 0 or ch7_first_floor_doctorbedrroom_bedside_done == 0:
            show screen ch7_first_floor_doctorbedrroom_desk_button
            call screen ch7_first_floor_doctorbedrroom_bedside_button
        else:
            z "(Maybe I can find something on the bed itself...)"
            show screen ch7_first_floor_doctorbedrroom_desk_button
            show screen ch7_first_floor_doctorbedrroom_bedside_button
            call screen ch7_first_floor_doctorbedrroom_bed_button

        #doctorbedrroom exploration buttons and variables:
        screen ch7_first_floor_doctorbedrroom_desk_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.25
                ypos 0.38
                idle "images/0.7/other/ch7_first_floor_doctorbedrroom_desk_button.webp"
                hover "images/0.7/other/ch7_first_floor_doctorbedrroom_desk_button_h.webp"
                action Jump("ch7_first_floor_doctorbedrroom_desk")
        screen ch7_first_floor_doctorbedrroom_bedside_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.475
                ypos 0.28
                idle "images/0.7/other/ch7_first_floor_doctorbedrroom_bedside_button.webp"
                hover "images/0.7/other/ch7_first_floor_doctorbedrroom_bedside_button_h.webp"
                action Jump("ch7_first_floor_doctorbedrroom_bedside")
        screen ch7_first_floor_doctorbedrroom_bed_button:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.87
                ypos 0.34
                idle "images/0.7/other/ch7_first_floor_doctorbedrroom_bed_button.webp"
                hover "images/0.7/other/ch7_first_floor_doctorbedrroom_bed_button_h.webp"
                action Jump("ch7_first_floor_doctorbedrroom_bed")
        screen button_diary_next:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.93
                ypos 0.5
                idle "images/Buttons/next_smol_u.png"
                hover "images/Buttons/next_smol_h.png"
                action Jump("diary_page_2")
        screen button_diary_back:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.07
                ypos 0.5
                idle "images/Buttons/back_smol_u.png"
                hover "images/Buttons/back_smol_h.png"
                action Jump("diary_page_1")
        screen button_diary_out:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.85
                idle "images/Buttons/down_smol_u.png"
                hover "images/Buttons/down_smol_h.png"
                action Jump("diary_out")
        define ch7_first_floor_doctorbedrroom_desk_done = 0
        define ch7_first_floor_doctorbedrroom_bedside_done = 0
        define ch7_first_floor_doctorbedrroom_bed_done = 0

        #doctorbedrroom exploration labels:
        label ch7_first_floor_doctorbedrroom_desk:
            call hide_all_ch7 from _call_hide_all_ch7_13
            scene v7776 with dissolve
            #Gets closer.
            if ch7_first_floor_doctorbedrroom_desk_done == 1:
                z "(Whoever searched the place before us must've taken the papers with stuff written on them.)"
                pause(0.7)
                jump ch7_first_floor_doctorbedrroom
            else:
                $ ch7_first_floor_doctorbedrroom_desk_done = 1
                z "(A Quill and some ink?)"
                scene v7777 with dissolve
                z "(Some papers on the table and others scattered on the ground. Nothing is written on them, though...)"
                scene v7776 with dissolve
                z "(Maybe whoever searched the place before us took those with stuff written on them.)"
                pause(0.7)
                jump ch7_first_floor_doctorbedrroom
        label ch7_first_floor_doctorbedrroom_bedside:
            call hide_all_ch7 from _call_hide_all_ch7_14
            scene v7778 with dissolve
            #Gets closer.
            if ch7_first_floor_doctorbedrroom_bedside_done == 1:
                #There's a comb, a mascara, and some lipstick in there.
                z "(Some make up stuff, but it feels like something is missing here...)"
                pause(0.7)
                jump ch7_first_floor_doctorbedrroom
            else:
                $ ch7_first_floor_doctorbedrroom_bedside_done = 1
                #There's a comb, a mascara, and some lipstick in there.
                z "..."
                z "(Some make up stuff, I guess...)"
                z "(But it feels like something is missing here... Right?)"
                pause(0.7)
                jump ch7_first_floor_doctorbedrroom
        label ch7_first_floor_doctorbedrroom_bed:
            call hide_all_ch7 from _call_hide_all_ch7_15
            hide screen button_vn_mode2 #Hide VN mode button here <--------------------
            scene v7779 with dissolve
            #A bottel of liquid is poured on it
            z "(Hmmm... Some bottle has been poured all over it... But that aside, nothing too weird going on with the bed...)"
            pause(0.7)
            play audio "audio/glass_shards.mp3" #Glass sounds
            pause(1)
            z "Hm?"
            #Looks down, glass shards seem to be under the bed.
            #Takes a look under the bed.
            scene v7780 with dissolve
            z "(Shards? Where did they come from...)"
            scene v7781 with dissolve
            z "(Wait...)"
            #Pulls out a broken mirror.
            z "(Is this... a mirror?)"
            scene v7782 with dissolve
            z "(Wait... There's something else.)"
            scene v7783 with dissolve
            pause(1)
            #Pulls out the mask.
            play audio "audio/rustle.mp3"
            scene v7784 with Dissolve(2)
            z "(What is that? A mask?)"
            scene v7785 with dissolve
            z "(Why is it so bizarre-looking... Almost creepy...)"
            z "(There's a bunch of broken and scattered stuff all around here, so it isn't exactly unusual to find things randomly placed...)"
            z "(But why were they under the bed? Almost as if they were hidden...)"
            z "Hmm..."
            scene v7786 #Scary reflection for a second.
            play audio "audio/jumpscare_long.mp3"
            z "!"
            pause(0.5)
            menu:
                "Turn around.":
                    $ dummy += 1
            pause(0.5)
            #Turns around, nothing is there.
            scene v7787
            pause(1.0)
            z "..."
            z "V-Venus?! Is that you?!"
            z "Venus!"
            scene v7788 with dissolve
            z "..."
            z "(The fuck was that...)"
            scene v7789 with dissolve
            z "(Something is definitely off here...)"
            #Goes to the window.
            #Zoom in on the window. Can see the village outside.
            scene v7790 with dissolve
            z "(Was it someone outside?)"
            z "..."
            z "Hmm... (This room has a good view on almost the whole village...)"
            scene v7791 with dissolve
            z "(Let's just call it a day, I don't know if I'm seeing things because I'm tired, but I don't want to stay in this creepy place one more second than I need to.)"
            #Notices something now that leads him to the diary, but a liquid was poured on it when Venus made the mess, so not all pages are salvagable.
            #Subtle sewing marks on the futon.
            scene v7792 with dissolve
            z "(Wait...)"
            #Zoom in.
            scene v7793 with dissolve
            z "(Are those sewing marks?)"
            scene v7794 with dissolve
            z "..."
            pause(1)
            play audio "audio/Rip.mp3"
            #Tearing sound. <----------------
            #Cuts it open and finds the diary.
            scene v7795 with Dissolve(2.5)
            z "(A diary of some sort?)"
            scene v7796 with dissolve
            z "(But why was it so well hidden inside the mattress itself...)"
            #Z sits on the bed with the diary but is interupted:
            z "(Did the doctor hide this? If so, why would she? What does it even contai-)"
            scene v7797 with dissolve
            vns "[mc_name]? Where are you?"
            scene v7798 with dissolve
            z "Venus! I'm over here! Come over! I found something!"
            scene v7799 with dissolve
            vns "Huh? What did you find?" #Comes into the room
            scene v7800 with dissolve
            z "Looks like a diary of some sort. The doctor must have left it."
            z "It was well hidden too. So I'm guessing she didn't want it found..."
            scene v7801 with dissolve
            vns "What? Why?"
            scene v7802 with dissolve
            z "I'm not sure... Maybe someone was onto her..."
            scene v7803 with dissolve
            vns "Onto her?"
            scene v7802 with dissolve
            z "I mean... She did go missing, didn't she?"
            scene v7803 with dissolve
            vns "You really think someone hurt her?"
            scene v7802 with dissolve
            z "Could very well be. Would explain the hidden diary and the fact that someone searched the house and made a mess."
            vns "Hmmm..."
            scene v7804 with dissolve
            vns "Okay, let's have a look at what you found."
            play sound "audio/open book.mp3"
            scene v7805 with Dissolve(1.5)
            pause(1)
            label diary_page_1:
                play sound "audio/page turn.mp3"
            show dairy_1 with dissolve
            hide dairy_2 with dissolve
            hide screen button_diary_back
            hide screen button_diary_out
            call screen button_diary_next
            label diary_page_2:
                play sound "audio/page turn.mp3"
            show dairy_2 with dissolve
            hide dairy_1 with dissolve
            hide screen button_diary_next
            show screen button_diary_back
            call screen button_diary_out
            label diary_out:
                hide dairy_1 with dissolve
                hide screen button_diary_next
                hide dairy_2 with dissolve
                hide screen button_diary_back
                hide screen button_diary_out
            #Put notebook here and make it available in stats menü. <--------
            #After reading.
            pause(1)
            z "..." (multiple=2)
            vns "..." (multiple=2)
            scene v7806 with Dissolve(1.5)
            pause(1)
            z "..." (multiple=2) #(Looking at each other.)
            vns "..." (multiple=2) #(Looking at each other.)
            pause(1)
            jump after_medics_cottage

    label ch7_vn_mode:
        hide screen button_vn_mode2
        call hide_all_ch7 from _call_hide_all_ch7_16
        #Hide VN mode button here
        scene v7748 with dissolve
        z "(Okay. Let's explore the rooms...)"
        scene v7749 with dissolve #Creepy kid's room.
        pause(1)
        z "(A child's room?)"
        z "(Looks somewhat out of place here...)"
        z "(Wait... Why isn't it a mess like the rest of the house?!)"
        scene v7750 with dissolve
        z "(Even though the door was apparently broken down...)"
        z "..."
        scene v7749 with dissolve
        z "(Weird...)"
        z "(I don't think I'll find anything useful here, though... Right?)"
        pause(0.7)
        scene v7747 with dissolve
        pause(1)
        play audio "audio/giggle.mp3"
        scene v7751 with dissolve #Show jumpscare image
        #Jumpscare sound <------------
        pause(0.7)
        scene v7748 with dissolve
        z "HUH?!"
        z "HEY!"
        z "Venus?! Is that you?!"
        z "Venus!"
        z "..."
        z "(The fuck was that... Am I seeing thing...)"
        pause(0.7)
        z "(Let's just check the other room...)"
        play audio "audio/creaky door.mp3"
        scene v7754 with dissolve
        pause(1)
        z "..."
        z "(Looks like it's a bathroom... An old one...)"
        z "(Not much to see here.)"
        pause(0.7)
        play audio "audio/glass_breaking.mp3"
        pause(1.0)
        #Broking glass sound. <------------------
        z "Huh?!"
        pause(0.7)
        scene v7752 with dissolve
        z "Venus?!"
        scene v7748 with dissolve
        z "(Fuck...)"
        z "(I'm done here.... I think I'll just switch with Venus. The faster we're out of here the better...)"
        #Go back towards the stairs.
        scene v7755 with dissolve
        z "Venus?"
        play audio "audio/creaky stairs.mp3"
        scene v7756 with dissolve
        z "..."
        scene v7757 with dissolve
        z "VENUS!"
        play sound "audio/footsteps.mp3"
        pause(1.7)
        "*Footstep sounds behind you."
        z "..."
        menu:
            "Turn around.":
                stop sound
                pause(0.5)
        play audio "audio/jump_scare_very_light.mp3"
        scene v7758
        pause(0.7)
        #Jumpscare venus.
        #Sound <------------------------
        scene v7759 with vpunch
        z "Fuck!"
        scene v7760 with dissolve
        vns "What?!"
        scene v7761 with dissolve
        z "..."
        z "How the fuck did you even get behind me?!"
        scene v7762 with dissolve
        vns "Errr... I was standing here when you came down."
        scene v7763 with dissolve
        z "So why didn't you say anything?!"
        scene v7764 with dissolve
        vns "I don't know. Should I have?"
        scene v7765 with dissolve
        z "..."
        z "Nevermind..."
        z "I heard some glass break just a minute ago. Was that you?"
        scene v7766 with dissolve
        vns "Eh? Glass? No. I didn't hear anything like that."
        scene v7765 with dissolve
        z "Hm... (Weird...)"
        z "Well... I'm done upstairs. Are you done here?"
        scene v7764 with dissolve
        vns "Errr... Sure. I've already looked around here a few days ago anyway."
        scene v7765 with dissolve
        z "Okay. Let's switch then."
        scene v7767 with dissolve
        pause(1.5)
        #Vns leaves.
        scene v7768 with dissolve
        z "(Okay. Let's start investigating the rooms.)"
        scene v7769 with dissolve
        pause(1)
        z "(A kitchen? Quite a few things were going on here from the looks of it...)"
        pause(1)
        scene v7773 with dissolve
        z "(What's this? Why is knife sticking out of the wall like this?)"
        z "(No real signs of a fight or anything... I mean, sure it's a mess. But that's the case everywhere.)"
        z "(The mess is more likely to be due to someone searching the house rather than a fight all around the house.)"
        z "Hmm..."
        z "(Maybe someone used the knife to hang something on the wall? Like a paper or a note of some sort...)"
        z "(But if that were the case, the note is long gone...)"
        pause(0.7)
        scene v7770 with dissolve
        z "(Seems it has been here for a few days, but it hasn't started to rot yet.)"
        z "(The medic's family got sick and were taken out of the house over a week ago. I don't think this stuff has been here for that long...)"
        z "(So, that was probably put here by the traveling doctor...)"
        z "(The cup still has something in it... Either whoever made it didn't get to finish it, or forgot it.)"
        z "(But assuming it was the doctor who left the cup. The first option seems more likely...)"
        pause(0.7)
        scene v7771 with dissolve
        z "(Looks like someone was trying to make a cure, I guess...)"
        scene v7772 with dissolve
        z "(The books in the bottom shelf look like someone has gone through them. Not very delicately at that...)"
        scene v7771 with dissolve
        z "(I really can't tell whether this was the work of the doctor or the medic...)"
        z "(It's not really my area. Venus must've seen this and decided if there was anything useful here already.)"
        pause(0.7)
        scene v7769 with dissolve
        z "(I think I'm done in the kitchen. Let's check some other room.)"
        scene v7774 with dissolve
        z "(Hmmm... This is probably the master bedroom.)"
        z "(From the looks of it, whoever searched the house must've looked in here too. But I doubt I can find anything useful here. I'm looking for stuff left behind by the doctor...)"
        pause(0.7)
        scene v7775 with dissolve
        z "(Another bedroom... Could be a guest bedroom. Maybe the doctor slept here?)"
        z "(If so, this room is definitely worth searching thoroughly.)"
        scene v7776 with dissolve
        z "(A Quill and some ink?)"
        scene v7777 with dissolve
        z "(Some papers on the table and others scattered on the ground. Nothing is written on them, though...)"
        scene v7776 with dissolve
        z "(Maybe whoever searched the place before us took those with stuff written on them.)"
        pause(0.7)
        scene v7778 with dissolve
        z "..."
        z "(Some make up stuff, I guess...)"
        z "(But it feels like something is missing here... Right?)"
        pause(0.7)
        scene v7779 with dissolve
        z "(Maybe I can find something on the bed itself...)"
        #A bottel of liquid is poured on it
        z "(Hmmm... Some bottle has been poured all over it... But that aside, nothing too weird going on with the bed...)"
        pause(0.7)
        play audio "audio/glass_shards.mp3" #Glass sounds
        pause(1)
        z "Hm?"
        #Looks down, glass shards seem to be under the bed.
        #Takes a look under the bed.
        scene v7780 with dissolve
        z "(Shards? Where did they come from...)"
        scene v7781 with dissolve
        z "(Wait...)"
        #Pulls out a broken mirror.
        z "(Is this... a mirror?)"
        scene v7782 with dissolve
        z "(Wait... There's something else.)"
        scene v7783 with dissolve
        pause(1)
        #Pulls out the mask.
        play audio "audio/rustle.mp3"
        scene v7784 with Dissolve(2)
        z "(What is that? A mask?)"
        scene v7785 with dissolve
        z "(Why is it so bizarre-looking... Almost creepy...)"
        z "(There's a bunch of broken and scattered stuff all around here, so it isn't exactly unusual to find things randomly placed...)"
        z "(But why were they under the bed? Almost as if they were hidden...)"
        z "Hmm..."
        scene v7786 #Scary reflection for a second.
        play audio "audio/jumpscare_long.mp3"
        z "!"
        pause(0.5)
        menu:
            "Turn around.":
                $ dummy += 1
        pause(0.5)
        #Turns around, nothing is there.
        scene v7787
        pause(1.0)
        z "..."
        z "V-Venus?! Is that you?!"
        z "Venus!"
        scene v7788 with dissolve
        z "..."
        z "(The fuck was that...)"
        scene v7789 with dissolve
        z "(Something is definitely off here...)"
        #Goes to the window.
        #Zoom in on the window. Can see the village outside.
        scene v7790 with dissolve
        z "(Was it someone outside?)"
        z "..."
        z "Hmm... (This room has a good view on almost the whole village...)"
        scene v7791 with dissolve
        z "(Let's just call it a day, I don't know if I'm seeing things because I'm tired, but I don't want to stay in this creepy place one more second than I need to.)"
        #Notices something now that leads him to the diary, but a liquid was poured on it when Venus made the mess, so not all pages are salvagable.
        #Subtle sewing marks on the futon.
        scene v7792 with dissolve
        z "(Wait...)"
        #Zoom in.
        scene v7793 with dissolve
        z "(Are those sewing marks?)"
        scene v7794 with dissolve
        z "..."
        pause(1)
        play audio "audio/Rip.mp3"
        #Tearing sound. <----------------
        #Cuts it open and finds the diary.
        scene v7795 with Dissolve(2.5)
        z "(A diary of some sort?)"
        scene v7796 with dissolve
        z "(But why was it so well hidden inside the mattress itself...)"
        #Z sits on the bed with the diary but is interupted:
        z "(Did the doctor hide this? If so, why would she? What does it even contai-)"
        scene v7797 with dissolve
        vns "[mc_name]? Where are you?"
        scene v7798 with dissolve
        z "Venus! I'm over here! Come over! I found something!"
        scene v7799 with dissolve
        vns "Huh? What did you find?" #Comes into the room
        scene v7800 with dissolve
        z "Looks like a diary of some sort. The doctor must have left it."
        z "It was well hidden too. So I'm guessing she didn't want it found..."
        scene v7801 with dissolve
        vns "What? Why?"
        scene v7802 with dissolve
        z "I'm not sure... Maybe someone was onto her..."
        scene v7803 with dissolve
        vns "Onto her?"
        scene v7802 with dissolve
        z "I mean... She did go missing, didn't she?"
        scene v7803 with dissolve
        vns "You really think someone hurt her?"
        scene v7802 with dissolve
        z "Could very well be. Would explain the hidden diary and the fact that someone searched the house and made a mess."
        vns "Hmmm..."
        scene v7804 with dissolve
        vns "Okay, let's have a look at what you found."
        play sound "audio/open book.mp3"
        scene v7805 with Dissolve(1.5)
        pause(1)
        play sound "audio/page turn.mp3"
        show dairy_1 with dissolve
        call screen button_diary_next
        #Reading.
        #Put notebook here and make it available in stats menü.  <--------
        #After reading.
        pause(1)
        z "..." (multiple=2)
        vns "..." (multiple=2)
        scene v7806 with Dissolve(1.5)
        pause(1)
        z "..." (multiple=2) #(Looking at each other.)
        vns "..." (multiple=2) #(Looking at each other.)
        pause(1)
        jump after_medics_cottage

    #Living room, kitchen, master bedroom, and guest room are here.
    #in the kitchen, there's a knife stuck in the wall. Suggesting that there was a paper suspended on it.

    #Maybe make some sandbox dynamics here?
    #One of the rooms downstairs (Guest room) was evedently occupied by the doctor. (After searching downstairs.)
    #There are viles and doctor equipment in the room.
    #Broken mirror shard hidden under the bed in the room.
    #Investigate the room to find the diary well hidden there.
    #Z comes back from the medic's cottage.
    #Is about to open the door.
    #S comes out of frnsska's house
    define saw_diary = 0
    label after_medics_cottage:
        $ saw_diary = 1
        scene black with fade
        stop background_s fadeout 1.0
        stop music fadeout 1.0
        play background_s "audio/rain.mp3" fadeout 1.0 fadein 1.0 loop
        #Later
        pause(2.5)
    scene v7807 with dissolve
    $ renpy.notify("The doctor's diary is now accessible in the stats screen.")
    pause(1)
    scene v7808 with dissolve
    pause(1)
    s "[mc_name]!"
    scene v7809 with dissolve
    z "Seira?"
    pause(0.7)
    scene v7810 with dissolve
    z "Where are the others? I found out some important stuff!"
    scene v7811 with dissolve
    s "Oh?"
    scene v7812 with dissolve
    s "Well... Yumi already left to report back to the village."
    scene v7813 with dissolve
    z "This late?! And she barely even sat down..."
    scene v7815 with dissolve
    s "She'll be fine, don't worry. She's a tough girl."
    scene v7816 with dissolve
    z "..."
    z "Wait, when did you change clothes?"
    scene v7814 with dissolve
    s "Oh. I was soaked from the rain, so Fransisca gave these to me. They're a bit small... But they'll do for now."
    if s_lst >= 5:
        scene v7816 with dissolve
        z "I'm not gonna complain either..."
        scene v7817 with dissolve
        s "Ahahah! I bet you won't, you naughty boy!"
        $ s_lst += 1
        play sound "audio/stats.wav"
        show screen button_lst with dissolve
        hide screen button_lst with dissolve
    else:
        scene v7816 with dissolve
        z "(Well... I'm not complaining...)"
    #end if
    scene v7815 with dissolve
    s "Anyway, she also said we're welcome to stay at their house while we're here."
    scene v7816 with dissolve
    z "Oh..."
    scene v7815 with dissolve
    s "Come on, let's talk inside."
    scene v7816 with dissolve
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    #Later
    pause(1)
    #They go inside.
    play sound "audio/creaky door.mp3"
    #Door creaking sound <-------------
    play background_s "audio/fireplace.mp3" fadeout 1.0 fadein 1.0 loop
    #%%% Wood burning sound. <------------------
    #gbrla is sitting the table
    scene v7818 with dissolve
    pause(1)
    scene v7819 with dissolve
    gbrla "?"
    scene v7820 with dissolve
    gbrla "[mc_name]! Hey!"
    scene v7821 with dissolve
    z "Hey, Gabbie!"
    scene v7820 with dissolve
    gbrla "Come on in! Jenny and I made supper."
    #Jny comes in carrying food.
    scene v7822 with dissolve
    jnfr "Gabbie! I told you to make some space! This thing is super heavy."
    scene v7823 with dissolve
    s "Guess we'll talk after supper."
    scene v7825 with dissolve
    s "Hang on, girls. I'll help you set the table." #Goes to them.
    scene v7826 with dissolve
    z "..."
    z "(Guess I'll go help too...)"
    pause(1)
    scene black with fade
    pause(1) #At the table.
    scene v7827 with dissolve
    z "Honestly, guys. Thank you. But you shouldn't have done all of this..."
    scene v7828 with dissolve
    jnfr "Oh, It's nothing, really."
    scene v7829 with dissolve
    jamie "Now, now, darling. No need to be so modest."
    scene v7830 with dissolve
    jamie "You're quite welcome, err..."
    scene v7831 with dissolve
    z "[mc_name]. And I wasn't thanking you. You didn't do anything."
    scene v7832 with dissolve
    jamie "..." #Surprised.
    play sound "audio/table_slam.mp3"
    scene v7833 with vpunch
    play music "audio/comedy.mp3" volume 0.2 fadeout 1.0 fadein 1.0
    jamie "How dare you!" #Slams table with his hands.
    scene v7834 with dissolve
    jnfr "Sit down, Jamie. You really didn't do anything all day aside from looking for that watch of yours."
    scene v7835 with vpunch
    jamie "Huh?! You're taking the elf's side?!"
    play sound "audio/table_slam.mp3"
    scene v7836 with vpunch
    z "I'm not a fucking elf!"
    scene v7837 with vpunch
    jnfr "I'm not taking anyone's side, okay?! I'm just sayi-"
    play sound "audio/Door big.mp3"
    stop music fadeout 1.0
    scene v7838 with dissolve
    pause(1.8)
    #Door opens.
    #Stop music <----------------------
    #It's Frnsska.
    scene v7839 with Dissolve(2)
    pause(1.5)
    scene v7840 with dissolve
    frnsska "Good evening."
    frnsska "I feel like I've heard a commotion a minute ago..."
    frnsska "It must've been outside..."
    scene v7841 with dissolve
    frnsska "...Right?"
    #All frozen stiff.
    scene v7842 with dissolve
    jamie "..."
    scene v7843 with dissolve
    jamie "Y-Yes, ma'am... I believe it was..."
    scene v7839 with dissolve
    frnsska "..."
    scene v7844 with dissolve
    frnsska "Awww... Aren't you such a polite young man! I'm really glad my daughter is marrying you!"
    scene v7845 with dissolve
    jamie "Th-Thank you very much, ma'am."
    scene v7846 with dissolve
    z "(What is going on with this dynamic...)"
    z "(This family is fucking weird...)"
    pause(0.8)
    play sound "audio/chair.mp3"
    scene v7847 with dissolve
    frnsska "I apologise for the delay. I hope you didn't wait long."
    scene v7848 with dissolve
    s "No. Not at all."
    scene v7847 with dissolve
    frnsska "Splendid."
    scene v7849 with dissolve
    z "..." #Z is looknig at the food.
    scene v7850 with dissolve
    Character("Girl with glasses") "Smells good, am I right?"
    scene v7851 with dissolve
    z "Yeah."
    scene v7852 with dissolve
    z "..."
    z "Wait! Who are you?! How did you get here?!"
    scene v7853 with dissolve
    Character("Girl with glasses") "Huh? What are you on about? I've been sitting here the whole time!"
    scene v7852 with dissolve
    z "What?! No you weren't!"
    scene v7853 with dissolve
    Character("Girl with glasses") "Yeah, I was."
    scene v7852 with dissolve
    z "..."
    scene v7854 with dissolve
    jnfr "Oh. [mc_name], I don't believe you met Margot. She's mother's new apprentice."
    scene v7852 with dissolve
    z "..."
    z "Errr... Nice to meet yo-"
    play sound "audio/rustle.mp3"
    scene v7855 with vpunch #Jumps in his lap.
    $ margot_met = 1
    margot "Nice to meet you too!"
    scene v7856 with dissolve
    margot "..." (multiple=2)
    z "..." (multiple=2)
    scene v7857 with dissolve
    z "Errr... I don't think I can eat like this..."
    scene v7858 with dissolve
    margot "Oh? Want me to feed you? How lewd!"
    scene v7859 with dissolve
    pause(0.5)
    #Bring food from the table.
    scene v7860 with dissolve
    margot "Here! Aaaaaaa..."
    scene v7861 with dissolve
    jnfr "Margot! Stop weirding him out, please!"
    scene v7862 with dissolve
    margot "..." #Looking at jenny
    scene v7863 with dissolve
    margot "Aaaaaaaa..." #While still looking at jenny
    scene v7864 with dissolve
    frnsska "Go back to your chair, Margot."
    #Goes back to her chair.
    play sound "audio/rustle.mp3"
    scene v7865 with dissolve
    margot "Yes, ma'am." #Military pose.
    scene v7866 with dissolve
    z "(Holy fuck! And I thought Venus was weird!)"
    #They eat dinner uneventfully.
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    pause(1)
    play background_s "audio/rain_inside.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    #At the corrodor.
    scene v7868 with dissolve
    pause(0.7)
    scene v7867 with dissolve
    s "Well, Fransisca said the guest's bath is ready for me. Said you could use it after I'm done."
    if s_lst >= 5:
        scene v7869 with dissolve
        s "But I'm thinking we could go in together? Save some water for them?" #Seductive look.
        scene v7870 with dissolve
        z "Yup. That's most considerate of you! I agree!"
        z "(Is this gonna become a regular thing now? Awesome!)"
        z "Gabbie said she left me some clean clothes in our room, I'll go fetch them and be right back, okay?"
        scene v7869 with dissolve
        s "Sounds good. Don't get lost, though. The house is pretty big."
        scene v7870 with dissolve
        z "Got it."
        pause(1)
        scene black with fade
        pause(1)
        #Goes to bring his clothes.
        play sound "audio/creaky door.mp3"
        scene v7871 with dissolve
        pause(0.7)
        z "(Okay. Here they are. Let's grab them and run to the bath.)"
    else:
        scene v7868 with dissolve
        z "Yeah. Sounds good."
        z "Gabbie said she left me some clean clothes in our room, I'll go find them..."
        scene v7867 with dissolve
        s "Sounds good. Don't get lost, though. The house is pretty big."
        scene v7868 with dissolve
        z "Got it."
        pause(1)
        scene black with fade
        pause(1)
        #Goes to bring his clothes.
        play sound "audio/creaky door.mp3"
        scene v7871 with dissolve
        pause(0.7)
        #Goes to bring his clothes.
        z "(Okay. Here they are. Let's grab them and check if Seira's done.)"
    #Goes out to the hall way.
    pause(1)
    scene v7872 with dissolve
    z "..."
    z "Err... (Where is the bath...)"
    pause(1)
    scene black with fade
    z "(How is the house even this big...)"
    z "(Damn...)"
    pause(1)
    #After a while of looking.
    scene v7873 with dissolve
    #Sound <-------------------------------------------------------------------------------------------
    play sound "audio/water.mp3"
    "*Water sounds from behind the door."
    pause(1)
    z "(That must be it!)"
    #Goes in.
    pause(0.7) #Door sound <-----------
    label G23:
        $ persistent.g_23_unlock = 1
    stop background_s fadeout 1.0
    scene v7874 with Dissolve(1.0)
    play background_s "audio/bath.mp3" fadeout 1.0 fadein 1.0 loop
    play sound "audio/Door close.mp3"
    z "Seira? Are you in here?"
    scene v7875 with Dissolve(2.5)
    pause(1)
    #Jny comes out of the water.
    play sound "audio/splash.wav"
    scene v7876 with dissolve
    jnfr "Hm?"
    z "Huh?! Jenny?! I'm sorry! I thought..."
    scene v7877 with dissolve
    jnfr "..." #Embarressed.
    z "I'm out of here! I was looking for the guest's bath and I got lost! The house is so damn big!"
    if jnfr_aff < 4 and came_from_gallery == 0:
        #leaves.
        scene v7873 with dissolve
        play sound "audio/Door close.mp3"
        play background_s "audio/rain_inside.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
        z "(Gods... That was embarrassing...)"
        if s_lst >= 5:
            z "(Let's just call it a night... I'll tell Seira I couldn't find the bath. I don't want to do something like that again...)"
        else:
            z "(Let's just call it a night... I don't want to do something like that again...)"
    else:
        scene v7878 with dissolve
        jnfr "H-Hold on! Did you just call Seira?"
        scene v7879 with dissolve
        jnfr "You guys take baths together?"
        scene v7880 with dissolve
        z "I mean... Sometimes..."
        z "Is that weird?"
        jnfr "..."
        scene v7881 with dissolve
        jnfr "I guess not... I take baths with Gabbie sometimes too."
        scene v7882 with dissolve
        jnfr "..."
        scene v7883 with dissolve
        jnfr "Say..."
        scene v7884 with dissolve
        jnfr "You behave yourself when you bathe with Seira, right?"
        scene v7885 with dissolve
        z "Behave myself?"
        if s_lst >= 5:
            z "I m-mean... Err... Of course..."
        else:
            z "I mean... Of course. What are you trying to say?"
        scene v7886 with dissolve
        jnfr "Hmmm..."
        scene v7883 with dissolve
        jnfr "W-Well. You can take one with me too, you know."
        scene v7879 with dissolve
        jnfr "I-If you like."
        scene v7887 with dissolve
        jnfr "I used to give you baths when you were little. So.. It's not weird or anything, right?"
        scene v7888 with dissolve
        jnfr "Unless YOU think it's weird, of course!"
        scene v7889 with dissolve
        z "..."
        menu:
            "[ModGreen]Tell her it's not weird. (Jeniffer Lust +2) (More content later)":
                $ choice_variable_ch7_20 = 1
                z "Who? Me? O-Of course not! Why would it be weird?"
                scene v7890 with dissolve
                jnfr "Exactly..."
                scene v7891 with dissolve
                jnfr "So... Come on in! Come on in!"
                scene v7892 with dissolve
                pause(0.7)
                #Sits on the chair outside the bath and begins washing himself.
                scene v7893 with Fade(0.5,0.5,0.5)
                z "..."
                jnfr "..." #Observing him from the edge.
                scene v7894 with dissolve
                jnfr "Want me to wash your hair?" #Heartfull smile.
                scene v7895 with dissolve
                z "..."
                scene v7896 with dissolve
                z "Yeah. I'd like that."
                play sound "audio/splash.wav"
                scene v7897 with dissolve
                jnfr "Just a second."
                #Starts to get out of the water
                #Z starts to turn.
                scene v7898 with vpunch
                jnfr "Hey, now. No peeking!" #Turns his head with her hand.
                scene v7899 with Fade(0.5,0.5,0.5)
                pause(0.7)
                scene v7900 with dissolve
                jnfr "Remember when I used to wash your hair when you were younger?"
                scene v7901 with dissolve
                z "Of course I remember! That shit was horrifying!"
                scene v7902 with dissolve
                jnfr "Whaaaaat?! What part of that was horrifying?!"
                scene v7903 with dissolve
                z "You used to get soap in my eyes every time and that hurt a lot!"
                scene v7904 with dissolve
                jnfr "Bullshit! I never got any soap in your eyes."
                scene v7905 with dissolve
                z "You did!"
                scene v7904 with dissolve
                jnfr "Did not!"
                scene v7905 with dissolve
                z "One time, my right eye got so red, that your mother made me a potion. I had to put three drops of it in my eye for a week. Remember?"
                scene v7906 with dissolve
                jnfr "..."
                scene v7907 with dissolve
                jnfr "That..."
                scene v7908 with dissolve
                jnfr "Well, that was only because you kept moving while I washed you!"
                scene v7909 with dissolve
                z "Of course! I was trying to run! You washing me was really scary!"
                scene v7910 with dissolve
                jnfr "..."
                scene v7911 with vpunch #Hugs him from behind and puts her arms around him. Her boobs touching his back
                z "!"
                scene v7912 with Dissolve(2)
                play music "audio/Jazz.mp3" volume 0.1 fadein 1.0 fadeout 1.0
                jnfr "Do you still think me washing you is scary?" #Seductive look.
                scene v7913 with dissolve
                z "..."
                scene v7914 with dissolve
                z "Nope. It's getting more pleasant by the minute."
                scene v7915 with dissolve
                jnfr "..."
                scene v7916 with dissolve
                jnfr "So I can see..."
                scene v7917 with dissolve
                z "..."
                scene v7918 with dissolve
                z "I..."
                scene v7919 with dissolve
                jnfr "It's all good, [mc_name]. I'm not one of those timid girls who get scared when they see a dick. I know it's normal."
                scene v7920 with dissolve
                z "Oh? You seemed pretty scared last time, though."
                scene v7921 with dissolve
                jnfr "No, I wasn't! I was just surprised!"
                jnfr "I went inside that closet to find sweet little [mc_name] who I remember barely reaching my waist, but instead I find something the size of my forearm pointing at me."
                scene v7922 with dissolve
                z "Hmmm..."
                scene v7921 with dissolve
                jnfr "Besides, if I were scared, would I do..."
                scene v7923 with vpunch
                jnfr "...THIS?!" (multiple=2) #(grabs it)
                z "!" (multiple=2)
                show v7m8 with dissolve #Starts slowly sliding her hand up and down while rubbing his hair.
                z "Hahh... Jenny... You're..."
                jnfr "Hm? I'm... what?"
                jnfr "Something wrong? I'm just cleaning your hair..."
                jnfr "You've really 'grown' since last time I did this, though..."
                z "Well, you grew up too, you know. Especially in certain regions... All the good ones too... Guess it runs in your family."
                jnfr "Why, thank you."
                jnfr "And you've been inspecting that growth in my sister and my mom too, huh?"
                scene v7924 with dissolve
                jnfr "You pervert..." #Wispers it in his ear seductively
                hide v7m8
                show v7m8 with dissolve
                z "I mean... It's hard to miss..."
                jnfr "Hmm..."
                z "Ahh... (Heh... I always knew Jenny had this playful side to her, but...)"
                if s_lst >= 5:
                    scene v7925 with Dissolve(2)
                    pause(1)
                    scene v7926 with dissolve
                    s "(I guess [mc_name] must've gotten lost...)"
                    scene v7927 with dissolve
                    s "(Oh, well. There's always tomorrow...)"
                    hide v7m8
                    show v7m8 with Dissolve(2)
                z "(It feels amazing... The way she's embracing me... Her boobs are pressing agains my back...)"
                z "(If only she'd go faster..)"
                z "Jenny... Could you-"
                scene v7928 with dissolve #Stands up.
                stop music fadeout 1.0
                jnfr "Aaaand... That's enough. Your hair is as clean as it gets." (multiple=2)
                z "!" (multiple=2)
                scene v7929 with dissolve
                z "W-What?!"
                z "You're going to leave me like this?!"
                scene v7930 with dissolve
                jnfr "Like what, dude?! I'm totally done cleaning your hair!"
                scene v7931 with dissolve
                z "..." #Half closed eyes.
                scene v7932 with dissolve
                jnfr "I trust you can do the rest yourself. Right?"
                scene v7931 with dissolve
                z "..." #Half closed eyes.
                scene v7933 with dissolve
                jnfr "I'm going to bed. Good night, [mc_name]."
                if came_from_gallery == 0:
                    $ jnfr_lst += 2
                play sound "audio/stats.wav"
                show screen button_lst with dissolve
                hide screen button_lst with dissolve
                scene v7934 with dissolve
                pause(0.7)
                scene v7935 with dissolve
                z "..." #Leaves.
                scene v7936 with dissolve
                z "(Fuck...)"
                pause(1)
            "Tell her it's weird.":
                $ choice_variable_ch7_21 = 1
                z "Yeah... I'm not sure it's a very good idea, Jenny."
                scene v7881 with dissolve
                jnfr "Huh?! Oh yeah. Totally."
                jnfr "You're right bad idea."
                scene v7882 with dissolve
                z "Good night."
                scene v7883 with dissolve
                jnfr "N-Night..."
                scene v7877 with dissolve
                pause(1)
                #Disappointed after he leaves.
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_3
    if s_lst >= 5:
        scene black with fade
        stop background_s fadeout 1.0
        #Later
        pause(2.5)
        play background_s "audio/rain_inside.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
        # Later at their room:
        scene v7937 with dissolve
        s "..."
        z "..."
        scene v7938 with dissolve
        s "You got lost, didn't you?" #Sly smile
        scene v7937 with dissolve
        z "Yeah... Sorry about that..."
        scene v7938 with dissolve
        s "It's fine."
        scene v7939 with dissolve
        s "Let's just get some sleep, okay? We'll discuss what you and Venus found at the medic's cottage tomorrow. Hopefully, Yumi will be back by then."
        scene v7940 with dissolve
        z "..."
        z "Sure... Good night."
        scene v7939 with dissolve
        s "Good night, honey."
        scene v7940 with dissolve
        #They sleep.

    pause(1.0)
    label G24:
        $ persistent.g_24_unlock = 1
    scene black with fade
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    #Later
    pause(2.5)
    play background_s "audio/Ambient_ninja_village.mp3" volume 0.3 fadeout 1.0 fadein 1.0 loop
    pause(0.7)
    z "..."
    scene v7941 with Dissolve(2)
    pause(1)
    z "(What's with this weird feeling...)"
    scene black with Dissolve(2)
    pause(1)
    z "(It feels really...)"
    scene v7941 with Dissolve(2)
    pause(1)
    z "(...good.)" #Opens eyes slightly.
    scene v7942 with Dissolve(2)
    scene v7943 with Dissolve(2)
    pause(1)
    z "..."
    scene v7944 with dissolve #Margot giving him hj, while looking at his dick.
    z "..."
    play sound "audio/rustle.mp3"
    scene v7945 with vpunch
    z "The fuck?!" #Gets up
    scene v7946 with dissolve
    margot "Oh! You're up, huh?"
    play music "audio/jazz.mp3" volume 0.1 fadeout 1.0 fadein 1.0
    show v7m9 with dissolve
    margot "I hope you'll pardon my..."
    margot "...experimenting with your reproductive organ..."
    margot "It's quite fascinating."
    z "(What.)"
    z "(The.)"
    z "(Fuck.)"
    margot "I've been studying alchemy for a few years now. My specific field was the study of alchemical ingredients, those extracted from living being, to be more precise..."
    margot "Did you know sperm can be used as an ingredient to brew over a hundred potions? And not all them are aphrodisiac-related."
    z "(Am I still dreaming or is this girl I just met yesterday actually giving me a handjob while casually making conversation...)"
    margot "Of course, the potency and thickness of the sperm is usually what plays a role in determining the overall quality of such potions."
    play sound "audio/open book.mp3"
    scene v7947 with dissolve #Grabs a notebook.
    margot "Now, tell me; do all elves have such massive dicks? Cuz humans certainly don't..."
    margot "And approximately, how much of an ounce of semen do you usually produce per ejaculation?"
    z "I..."
    z "Huh?! Wha-"
    play sound "audio/slight_hit.mp3"
    scene v7948 with vpunch
    z "HMM!" #Shuts his mouth with her hand.
    show v7m10 with dissolve
    margot "Actually, don't tell me! I prefer to learn from experimenting!"
    #HJ animation while covering his mouth.
    margot "Hmmm... Very stiff. Almost dangerously so..."
    margot "You ever fuck a woman with that thing?"
    scene v7949 with dissolve
    z "..." #Looking with angry eyes.
    hide v7m10
    show v7m10 with dissolve
    margot "Oh, right. I'm covering your mouth, so you can't talk..."
    margot "Just nod if you did."
    menu:
        "[ModGreen]Nod.":
            $ choice_variable_ch7_22 = 1
            scene v7951 with dissolve
            pause(0.6)
            scene v7950 with dissolve
            pause(0.25)
            scene v7951 with dissolve
            pause(0.6)
            hide v7m10
            show v7m10 with dissolve
            margot "Oh?! Is it more than one?"
            #Depending on choices nods or shakes his head.
            if affair_w_serena == 1 or choice_variable_ch6_35 == 1:
                scene v7951 with dissolve
                pause(0.6)
                scene v7950 with dissolve
                pause(0.25)
                scene v7951 with dissolve
                pause(0.6)
                hide v7m10
                show v7m10 with dissolve
                margot "And they all survived no problem?"
                z "(Well, you're the apprentice of one of them...)"
            else:
                scene v7951 with dissolve
                pause(0.6)
                scene v7953 with dissolve
                pause(0.25)
                scene v7952 with dissolve
                pause(0.25)
                scene v7951 with dissolve
                pause(0.6)
                hide v7m10
                show v7m10 with dissolve
                margot "Oh... But that one you fucked, she survived no problem?"
                z "(Well, you're her apprentice, so...)"
            margot "Hmmm..."
            margot "Can I try?"
            z "..."
            menu:
                "[ModGreen]Nod.":
                    $ choice_variable_ch7_23 = 1
                    scene v7951 with dissolve
                    pause(0.6)
                    scene v7950 with dissolve
                    pause(0.25)
                    scene v7951 with dissolve
                    pause(0.6)
                    #Nods.
                    hide v7m10
                    show v7m10 with dissolve
                    margot "Excellent!"
                    play sound "audio/rustle.mp3"
                    scene v7954 with vpunch #Climbs on top of him grabbing his arms.
                    pause(1)
                    scene v7955 with dissolve
                    z "Oh..."
                    scene v7956 with dissolve
                    margot "Hmmm..."
                    scene v7957 with dissolve
                    margot "Let the experiment 'Fucking an Elf' begin!"
                    scene v7958 with dissolve
                    pause(0.8)
                    scene v7959 with vpunch #Inserts it.
                    margot "OHHHH!"
                    scene v7m11 with dissolve
                    z "(So sudden... Not to mention loud... Someone will definitely hear her...)"
                    margot "Ahhh... It's reaching some spots I didn't know were there! And it's not even all the way in!"
                    margot "And this shape... It's perfectly shaped to reach deeper inside..."
                    margot "Oooohhh... Tip feels unbelievably.... Ahhhh... good when it hits the inner walls..."
                    margot "And the shaft is... Haaahhhhh... impressively stimulating the clitoris... Ahhh... by rubbing against it with every thrust..."
                    play sound "audio/open book.mp3"
                    scene v7962 with dissolve
                    margot "Very interesting..." #Takes notes.
                    z "..."
                    menu:
                        "Let her take her notes.":
                            $ choice_variable_ch7_24 = 1
                            #Finishes.
                            pause(1)
                            play sound "audio/writing.mp3"
                            scene v7963 with dissolve
                            margot "Now... Where were we?"
                            scene v7964 with vpunch
                            margot "Riiiiight... Fucking an elf..."
                            scene v7965 with dissolve
                            z "I'm not an e-"
                            show v7m11 with dissolve
                            #Starts fucking rapidly him while grabbing his arms
                            margot "OOOHHHH!"
                            margot "Ahhhh! Ohhhhh... Ahhhh!"
                            z "Keep it down! The others will hea-"
                            play sound "audio/slight_hit.mp3"
                            scene v7966 with vpunch
                            z "Mmm!" #Shoves the notebook in his mouth.
                            show v7m12 with dissolve
                            margot "Ahhhh... Haaahhhh... Ohhhhh..."
                            z "Mmmm..."
                            margot "Ohhhh... This dick... Ahhh..."
                            z "Hmmm..."
                            margot "Ohhh... wait... you're... cumming? Ahhh..."
                            scene v7967 with dissolve #Takes his dick outside and makes him finish in a vial.
                            pause(1)
                            scene v7968 with dissolve
                            margot "Haahh... So much semen... about a whole ounce..."
                            stop music fadeout 1.0
                            scene v7969 with dissolve #Grabs a ruler.
                            margot "And the flaccid length... Hahhh... About 24cm..."
                            margot "Erect length was about 29cm... Hmmm..."
                            scene v7970 with dissolve
                            z "Wait! When did you even measure that?!"
                            scene v7971 with dissolve
                            margot "Why, while you were sleeping, of course!"
                            z "..."
                            play sound "audio/rustle.mp3"
                            scene v7972 with dissolve
                            margot "Aaaand, experiment complete!"
                            scene v7973 with dissolve
                            margot "See you later, sweety."
                            scene v7974 with dissolve
                            margot "You can find me in the lab if you need anything."
                            play sound "audio/kiss.mp3"
                            scene v7975 with dissolve #kiss
                            margot "Bye!" #wink and kiss in the air.
                            scene v7976 with dissolve
                            play sound "audio/Door close.mp3"
                            margot "*Leaves."
                            z "Wait! Your cloth-"
                            #Leaves.
                            z "..."
                            z "(What a fucking crazy woman...)"
                        "Interrupt her. [ModGreen](More content)":
                            $ choice_variable_ch7_25 = 1
                            pause(1)
                            play audio "audio/slight_hit.mp3"
                            scene v7981 with vpunch
                            margot "Eh?!" #Grabs her hands.
                            #Pushes her down.
                            #Throws pen and note book.
                            play sound "audio/rustle.mp3"
                            scene v7982 with vpunch
                            margot "OOOHHHH!"
                            show v7m13 with dissolve
                            #mating press? fast fucking animation
                            margot "Waihhht! I... Ohhhhh! Didn't finishhhhhh.... wrihhhhting... Ahhhhh!"
                            z "Never mind that. I bet you'll remember every little detail of this anyway."
                            margot "Ohhh... But I... Ohhhhh!"
                            margot "Ahhhh! Ohhhhh... Ahhhh!"
                            z "Keep it down! The others will hear you." #(shoves one of the pen and note book in her mouth.)
                            margot "Oooooohhhh... Aaaaahhh... Haaaaaahhhh..."
                            scene v7983 with dissolve
                            z "Hmmm..." #Grabs notebook.
                            scene v7984 with dissolve
                            margot "Oooooohhhh..." #Looks at her while holding it.
                            play sound "audio/slight_hit.mp3"
                            scene v7985 with vpunch
                            margot "Hhhhmmmm! Mmmmmmmm!" #(shoves one of the pen and note book in her mouth.)
                            show v7m14 with dissolve
                            margot "Mmmmmmm... Ohhhmmmmmm!"
                            z "How's that, you crazy bitch?"
                            margot "Hmmmm..."
                            z "You love being treated like this, don't you?"
                            margot "Hmmmm! Mmmmm!"
                            z "What? I didn't get that..."
                            margot "Mmmmm!"
                            show v7m15 with dissolve
                            z "I wish you'd see your face right now... It's priceless how dumb you look..."
                            margot "Hmmm..."
                            z "Did you maybe feel like you were in control of the situation for a few seconds?"
                            z "I bet you weren't expecting to end up like this when you decided to come into my room this morning."
                            hide v7m14
                            show v7m14 with dissolve
                            margot "Mmmmmm... Ohhhmmmm..."
                            z "(I'm cumming...)"
                            define came_in_margot = 0
                            menu:
                                "Fill her up.":
                                    $ choice_variable_ch7_26 = 1
                                    $ came_in_margot = 1
                                    pause(1)
                                    scene v7987 with vpunch
                                    margot "Gaaaah!" #Spits the book out.
                                    show v7m17 with dissolve
                                    margot "Haahh... So much semen... Probably over an ounce..."
                                "Pull out.":
                                    $ choice_variable_ch7_27 = 1
                                    pause(1)
                                    scene v7988 with dissolve
                                    margot "Hmmm..."
                                    show v7m16 with dissolve
                                    margot "Haahh... So much semen... Probably over an ounce..."
                            #Grabs a ruler.
                            stop music fadeout 1.0
                            pause(2)
                            scene v7990 with dissolve #missing render
                            z "Hahhh... That was good..."
                            scene v7969 with dissolve #Grabs a ruler.
                            margot "And the flaccid length... Hahhh... About 24cm..."
                            margot "Erect length was about 29cm... Hmmm..."
                            scene v7970 with dissolve
                            z "Wait! When did you even measure that?!"
                            scene v7971 with dissolve
                            margot "Why, while you were sleeping, of course!"
                            z "..."
                            play sound "audio/rustle.mp3"
                            scene v7972 with dissolve
                            margot "Aaaand, experiment complete!"
                            scene v7973 with dissolve
                            margot "See you later, sweety. You can find me in the lab if you need anything."
                            if came_in_margot == 1:
                                scene v7974 with dissolve
                                margot "By the way, don't worry about me getting pregnant, I'm gonna take a potion for that."
                            play sound "audio/kiss.mp3"
                            scene v7975 with dissolve #kiss
                            margot "Bye!" #wink and kiss in the air.
                            scene v7976 with dissolve
                            play sound "audio/Door close.mp3"
                            margot "*Leaves."
                            z "Wait! Your cloth-"
                            #Leaves.
                            z "..."
                            z "(What a fucking crazy woman...)"
                "Shake your head.":
                    $ choice_variable_ch7_28 = 1
                    stop music fadeout 1.0
                    scene v7951 with dissolve
                    pause(0.6)
                    scene v7953 with dissolve
                    pause(0.25)
                    scene v7952 with dissolve
                    pause(0.25)
                    scene v7951 with dissolve
                    pause(0.6)
                    #Shakes his head.
                    z "(I think I've got more than enough craziness in my life right now...)"
                    play sound "audio/rustle.mp3"
                    scene v7977 with dissolve
                    margot "Eeeeeeeeeeeeeeeeeeh..."
                    margot "You're so mean, man..."
                    scene v7978 with dissolve
                    margot "And you're standing in the way of discovery!" #Crazy excited pose
                    scene v7979 with dissolve
                    margot "..." #Looks at him
                    scene v7980 with dissolve
                    margot "Yeah, yeah. I'm leaving."
                    play sound "audio/kiss.mp3"
                    scene v7975 with dissolve
                    margot "Bye, honey! Come find me if you find the mood." #wink and kiss in the air.
                    scene v7976 with dissolve
                    play sound "audio/Door close.mp3"
                    margot "*Leaves."
                    z "Wait! Your cloth-"
                    #Leaves.
                    z "..."
                    z "(What a fucking crazy woman...)"
        "Kick her out of the room.":
            $ choice_variable_ch7_29 = 1
            stop music fadeout 1.0
            #Grabs her hand.
            #Missing renders here!!!!!!!!!!!!! <-------------------------
            play audio "audio/slight_hit.mp3"
            scene v7991 with vpunch
            margot "Eh?!"
            play sound "audio/Punch.wav"
            scene v7992 with vpunch
            z "You're an absolute nutjob, aren't you?!"
            play sound "audio/Falling.mp3"
            scene v7993 with vpunch
            #Kicks her with his foot.
            z "Get the fuck out. I'm not in the mood for this."
            margot "Eeeeeeeh?"
            play sound "audio/rustle.mp3"
            scene v7977 with dissolve
            margot "Eeeeeeeeeeeeeeeeeeh..."
            margot "You're so mean, man..."
            scene v7978 with dissolve
            margot "And you're standing in the way of discovery!" #Crazy excited pose
            scene v7979 with dissolve
            margot "..." #Looks at him
            scene v7980 with dissolve
            margot "Yeah, yeah. I'm leaving."
            play sound "audio/kiss.mp3"
            scene v7975 with dissolve
            margot "Come find me if you find the mood." #wink and kiss in the air.
            scene v7976 with dissolve
            play sound "audio/Door close.mp3"
            margot "*Leaves."
            #Leaves.
            z "..."
            z "(What a fucking crazy woman...)"
    pause(1.0)
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_3
    scene black with fade
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    #Later
    pause(2.5)
    play audio "audio/creaky door.mp3"
    scene v7994 with dissolve
    pause(1)
    z "Hey, Venus."
    z "..." #Venus isn't there.
    play music "audio/die_zwei_geschwister.mp3" volume 0.7 fadeout 1.0 fadein 1.0
    scene v7995 with dissolve
    z "Venus?"
    z "(I guess she's not around...)"
    tmra "Hmmm..."
    scene v7996 with dissolve
    z "Hm? (Tamara? Did I wake her up?)"
    scene v7997 with dissolve #Goes to her.
    pause(1)
    #Wears a mask first! (IMPORTANT)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    play audio "audio/curtain.wav"
    scene v7998 with dissolve
    tmra "..."
    scene v7999 with dissolve
    tmra "[mc_name]..."
    scene v7998 with dissolve
    z "Hey, Tamara."
    tmra "..."
    scene v71000 with dissolve
    tmra "[mc_name]?! No! What are you doing here?!"
    scene v71001 with dissolve
    #z says they're here to help. It's good to see her fever has gone down.
    z "Well, we came here to help you guys."
    z "Seems your fever has gone down a bit. That's goo-"
    play audio "audio/light thud.mp3"
    scene v71002 with vpunch
    tmra "No! You don't understand! You're a demi-god, right? She's definitely going to want you! You have to-" #Grabs him
    scene v71003 with dissolve
    tmra "... to..."
    scene v71004 with dissolve
    z "Hm?"
    play audio "audio/light thud.mp3"
    scene v71005 with vpunch
    z "!"
    tmra "..." #and passes out again.
    z "Tamara?"
    scene v71006 with dissolve
    z "... (She's out cold...)"
    pause(1)
    play audio "audio/rustle.mp3"
    scene v71007 with dissolve
    z "(There... Let's go look for Ven-)"
    scene v71008
    play audio "audio/jump_scare_very_light.mp3"
    pause(0.7)
    #turns around.
    scene v71009 with vpunch
    z "Fuck!" #Strattled by venus
    z "Dude! What's with you and fucking scaring the shit out of people?!"
    scene v71010 with dissolve
    vns "What?! This is literally my work station here..." #Half closed eyes.
    scene v71011 with dissolve
    z "Rrrright..."
    z "Err... Where's your mask?"
    scene v71012 with dissolve
    vns "My mask?"
    scene v71013 with dissolve
    vns "Oh. Right. Thanks for reminding me."
    scene v71014 with dissolve
    pause(1.2)
    play audio "audio/put on mask.mp3"
    scene v71015 with dissolve
    z "(Is Venus always this clumsy...)"
    scene v71016 with dissolve #Puts her mask on.
    z "So, did you hear Tamara?"
    scene v71017 with dissolve
    vns "Kinda..."
    scene v71016 with dissolve
    z "She said some weird stuff about how I shouldn't have come. And that someone would want me or something..."
    z "Isn't this kind of similar to what that doctor was saying?"
    scene v71020 with dissolve
    vns "You think so?"
    scene v71019 with dissolve
    z "Hmm... I'm not sure..."
    scene v71018 with dissolve
    vns "Honestly, I get where you're coming from, [mc_name]. But I've been working as a medic for a while. People tend to talk nonsense when they have a fever."
    vns "And two people having a similar illness in a similar environment, can have similar hallucinations."
    scene v71019 with dissolve
    z "Hmm..."
    scene v71020 with dissolve
    vns "By the way, I was supposed to tell you. Yumi is back. And we're meeting up at the hall in thirty minutes to talk about the stuff we found yesterday."
    scene v71019 with dissolve
    z "Oh. That's good."
    scene v71020 with dissolve
    vns "Do you still have the diary?"
    scene v71019 with dissolve
    z "Yeah. It's in my pocket. Let me check real qui-"
    play audio "audio/mirror shard.mp3"
    #Glass sound.
    pause(1)
    z "Hm?"
    scene v71021 with dissolve
    #Pulls out a mirror shard.
    vns "What's that?"
    z "Oh... It's one of the mirror shards. I must've grabbed it along with the dia-"
    stop music
    play audio "audio/jump_scare_very_light.mp3" volume 0.2
    scene v71022
    pause(0.5)
    z "!"
    scene v71023 with vpunch
    z "The fuck?!"
    vns "Hm?!"
    scene v71024 with dissolve
    vns "What?!"
    z "Her reflection! Look!"
    scene v71025 with dissolve
    vns "..."
    scene v71026 with dissolve
    vns "!"
    scene v71027 with dissolve
    z "What the hell is this?! Venus?!"
    vns "I-I don't know!"
    z "..."
    scene v71028 with dissolve
    pause(1)
    play audio "audio/curtain.wav" #Curtain sound.
    pause(1)
    z "Look! It's the same for the others!"
    #Goes and checks someone else.
    scene v71029 with dissolve
    pause(1)
    vns "I-It really is..."
    z "..."
    pause(1)
    scene v71030 with dissolve
    z "Listen. We have to tell the others about all of this. Something weird is going on here!"
    scene v71031 with dissolve
    vns "Y-Yeah... You're right..."
    scene v71032 with dissolve
    z "Let's just head straight to the meeting."
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    #Later
    pause(2.5)
    #Later at meeting.
    #Dairy is open in the middle.
    play background_s "audio/fireplace.mp3" volume 0.4 fadeout 1.0 fadein 1.0 loop
    scene v71052 with dissolve
    z "To be honest, I'm not sure what I saw back there..."
    play music "audio/mysterious_and_mystic.mp3" volume 0.4 fadeout 1.0 fadein 1.0
    scene v71053 with dissolve
    z "And an entry in the diary seems to be talking about a sick girl who saw something, when she looked in the water."
    scene v71054 with dissolve
    z "But the words 'white dress' and 'black hair' are mentioned. I think that was what I saw too."
    z "In the entry of the day, in which the doctor was last seen, she said someone was following her. And that she was going to confront them..."
    scene v71053 with dissolve
    z "Tamara also said something a bit similar... She said someone will want me because I'm a demi-god... But Venus thinks they're just hallucinating because of the fever."
    z "That was when we noticed the weird reflections on a mirror shard from the alchemist's house. All the sick people were like that."
    scene v71054 with dissolve
    z "I think I'm going to start carrying the shard around..."
    scene v71040 with dissolve
    s "Hmmm..." #Looks tired.
    z "You okay, Seira? You look a bit tired. Didn't get enough sleep?"
    scene v71041 with dissolve
    s "Oh. I'm fine, [mc_name]. Don't worry."
    scene v71040 with dissolve
    z "Could it be that you caught it too?"
    scene v71041 with dissolve
    s "Maybe... I'm not sure..."
    scene v71040 with dissolve
    z "Hmmm... just try to take it easy for now, okay?"
    scene v71041 with dissolve
    s "I will."
    scene v71040 with dissolve
    z "(Now that I think about it... I kinda feel a slight soreness in my joints...)"
    z "(I hope it's nothing after all...)"
    z "(Let's not worry anyone for now, though.)"
    scene v71048 with dissolve
    vns "Just make sure to let me know if it starts getting worse, Keres Seira."
    scene v71042 with dissolve
    s "Yeah. Will do."
    scene v71041 with dissolve
    s "I actually have an idea to what it might be. Considering everything we know."
    scene v71040 with dissolve
    z "You do?"
    scene v71043 with dissolve
    s "Yes. I faced a similar situation many years ago. It was a plague specter."
    scene v71040 with dissolve
    z "Errr... A what?"
    scene v71041 with dissolve
    s "They're a dark race. They have the ability to possess other beings, but they need their prey to be weakened."
    scene v71043 with dissolve
    s "So, they evolved another ability. They can spread an illness which serves to weaken the potential host, if I recall."
    scene v71033 with dissolve
    ymi "Oh. Sirius once told me a similar story..."
    scene v71036 with dissolve
    ymi "I didn't know it was true, though."
    scene v71037 with dissolve
    gbrla "That's scary..."
    scene v71040 with dissolve
    z "Hold up! Is this really true?!"
    scene v71041 with dissolve
    s "Yes. I've seen it before."
    scene v71048 with dissolve
    vns "But what makes you think this is the case here? Can't this be... some strange illness we simply haven't seen before?"
    scene v71049 with dissolve
    z "It's the fact that someone did something to stop that doctor, Venus."
    scene v71053 with dissolve
    z "She said someone was watching her. She was speaking of a person, or an entity."
    z "Something weird is going on. There's obviously more to it than an illness."
    scene v71041 with dissolve
    s "I'm not entirely sure, but maybe the strange reflections have something to do with the creature too..."
    scene v71040 with dissolve
    z "Hmmm..."
    z "So... How do we go about handling this?"
    scene v71043 with dissolve
    s "I don't know. We definitely need help here."
    scene v71040 with dissolve
    z "Help? You mean send back to the ninja village?"
    scene v71041 with dissolve
    s "No. That's not it."
    scene v71043 with dissolve
    s "I know someone who could help us..."
    s "She's an old friend. A member of Artemis's hunting group."
    scene v71033 with dissolve
    ymi "Artemis's hunting group?"
    scene v71047 with dissolve
    vns "Is this really a good idea? I've heard they're not really good people."
    scene v71050 with dissolve
    vns "They sometimes capture men and... you know..."
    scene v71051 with dissolve
    s "Well, you're not entirely wrong... I've heard similar stories."
    scene v71042 with dissolve
    s "But my old friend is nothing like that. She's a very kind person, I promise."
    scene v71051 with dissolve
    vns "Hmmm..."
    scene v71041 with dissolve
    s "I'll go look for her in the mountains. She used to hunt there back in the day. Hopefully, I'll find her there..."
    scene v71040 with dissolve
    z "I'll go with you."
    scene v71041 with dissolve
    s "No. She'll be able to tell you're an incubus and might not show up."
    scene v71040 with dissolve
    z "But..."
    z "You're already tired... Are you sure you're up to this? At least take someone with you."
    scene v71038 with dissolve
    gbrla "Ahmm... I'd like to go with miss Seira."
    scene v71039 with dissolve
    gbrla "Maybe I could learn from the girl you mentioned how to make a potion to cure the illness."
    scene v71043 with dissolve
    s "Sure. I think that's a good idea."
    scene v71044 with dissolve
    s "See? I'm not going alone, after all."
    scene v71045 with dissolve
    z "..."
    z "Yeah. Okay..."
    pause(1)
    label G25:
        $ persistent.g_25_unlock = 1
    scene black with fade
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    #Later
    pause(2.5)
    #Goes back and sits down on the sofa at Fransisca's house.
    #Gabbie comes
    #Z asks her if they're leaving. Says in an hour and that she finished packing a small bag.
    #and asks if she can sit down with him.

    scene v71055 with Dissolve(2)
    play background_s "audio/fireplace.mp3" fadeout 1.0 fadein 1.0 loop
    play background_s2 "audio/rain_inside.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    pause(1.5)
    scene v71056 with Dissolve(1.5)
    z "..." #Looking at diary chilling on the couch.
    scene v71057 with dissolve
    z "..." #Looks at window
    scene v71058 with dissolve
    z "(It's raining outside again.)"
    scene v71057 with dissolve
    z "(The weather here is surprisingly totally different from that at the ninja village. Even though they're not far from each other.)"
    scene v71059 with dissolve
    gbrla "Hey. Done with the bath already?"
    scene v71060 with dissolve
    z "Hm?" #looks up.
    scene v71061 with dissolve
    z "Oh. Hey, Gabbie."
    z "Yeah. I thought you guys left already."
    scene v71062 with dissolve
    gbrla "Not yet. Miss Seira is still packing."
    scene v71061 with dissolve
    z "Oh."
    scene v71063 with dissolve
    gbrla "Can I sit down?"
    scene v71061 with dissolve
    z "Well... It's your house, Gabbie."
    scene v71064 with dissolve
    gbrla "It's mother's house, now. I no longer live with her, remember?"
    scene v71065 with dissolve
    z "Right."
    if gbrla_lst >= 2 or came_from_gallery == 1:
        play sound "audio/leather.wav"
        scene v71066 with dissolve
        gbrla "And I was kinda asking if I can sit with you." #Sits down leaning onto him.
        scene v71067 with dissolve
        z "(So cute...)"
        scene v71068 with dissolve
        z "Rude... I was about to say no."
        scene v71069 with dissolve
        gbrla "*Giggles. No you weren't!"
        scene v71070 with dissolve
        z "Say..."
        scene v71071 with dissolve
        gbrla "Hm?"
        scene v71070 with dissolve
        z "Not that we're doing anything weird, but wouldn't it be an issue if your mother saw us sitting like this?"
        scene v71073 with dissolve
        gbrla "Oh. Mother is always busy working on a potion for Jamie. She has been spending the whole day in her lab ever since I came here."
        scene v71074 with dissolve
        z "A potion for Jamie, you say..."
        z "(I wonder what kind of potion that asshole would want...)"
        scene v71075 with dissolve
        z "(Now that I think about it I never knew what exactly he was smuggling to Es-)"
        scene v71076 with dissolve #Gbrla puts her palm on his cheek.
        z "?"
        scene v71077 with dissolve
        pause(1)
        scene v71078 with dissolve
        z "Gabbie?"
        scene v71079 with dissolve
        gbrla "Ah." #Pulls it back embarrassed.
        scene v71080 with dissolve
        z "..."
        scene v71081 with dissolve
        z "Did I have something on my cheek, or..."
        scene v71082 with dissolve
        gbrla "Y-Yeah..."
        scene v71081 with dissolve
        z "Oh... Weird. I haven't eaten yet and-"
        scene v71083 with dissolve
        gbrla "No!"
        scene v71084 with dissolve
        z "?"
        scene v71083 with dissolve
        gbrla "It wasn't something on your cheek..." #Looking away.
        scene v71084 with dissolve
        gbrla "..." #Looking away.
        scene v71085 with dissolve
        gbrla "..." #Looks at z.
        scene v71086 with dissolve
        #Puts her hand on his cheek again.
        gbrla "Can I... Uhm..."
        scene v71087 with dissolve
        gbrla "I-Is it okay, if I..."
        gbrla "I..."
        menu:
            "[ModGreen]Kiss her. (Gabriella Love +2 Lust +2)":
                $ choice_variable_ch7_30 = 1
                #Puts his hand on her cheek.
                scene v71092 with dissolve
                gbrla "!" #Surprised.
                pause(1)
                play sound "audio/Falling.mp3"
                play sound "audio/kiss.mp3"
                scene v71093 with vpunch
                gbrla "Hm!" #Kisses her.
                scene v71094 with dissolve
                gbrla "Hmmmm..." #Heart aura.
                scene v71095 with dissolve
                z "(Was that aura just now? I feel like something like this happened a few times when I did this kind of thing...)"
                gbrla "Hm..."
                scene v71096 with dissolve
                gbrla "That was..."
                scene v71097 with dissolve
                play music "audio/Jazz.mp3" volume 0.1 fadeout 1.0 fadein 1.0
                gbrla "Nice..."
                show v7m18 with dissolve
                if came_from_gallery == 0:
                    $ gbrla_lst += 2
                    $ gbrla_aff += 2
                play sound "audio/stats.wav"
                show screen button_aff with dissolve
                hide screen button_aff with dissolve
                play sound "audio/stats.wav"
                show screen button_lst with dissolve
                hide screen button_lst with dissolve
                gbrla "..." #Looking at z with puppy eyes. (Animated?)
                z "Heh. What's with this look?"
                gbrla "..." #puppy mode.
                z "Wanna kiss some more?"
                pause(1)
                scene v71098 with dissolve
                pause(0.1)
                scene v71099 with dissolve
                pause(0.1)
                scene v71098 with dissolve
                pause(0.1)
                scene v71099 with dissolve
                pause(1)
                hide v7m18
                show v7m18 with dissolve
                pause(1)
                menu:
                    "Kiss her some more.":
                        $ dummy += 1
                #Nods in puppy mode.
                #kissing her while carrasing animation (Maybe play with her boob.)
                pause(1)
                play sound "audio/kiss.mp3"
                show v7m19 with dissolve
                hide v7m18
                gbrla "Mmmmm..."
                gbrla "Mhmmmh... Ahhmmm... Mmmmhhmm..."
                z "(She smells so good...)"
                gbrla "Mmhh..."
                z "(I want more...)"
                scene v71101 with dissolve
                z "(I can't hold back anymore...)"
                z "(I'm going to fuck you, Gabbie. I hope you're ready fo-)" #His hand starts moving to undress her.
                play sound "audio/Door slam.mp3"
                stop music
                scene v71102 with vpunch
                jnfr "Mother! Jamie is asking where his white coat is!" #Slams door up behind them.
                scene v71103 with dissolve
                jnfr "..." #Not looking at them.
                scene v71104 with dissolve
                jnfr "?" #Gaze shifts to them.
                #They're in an innocent position.
                scene v71105 with dissolve
                pause(2.5)
                scene v71106 with dissolve
                jnfr "Oh, Gabbie. You're still here?" #Looks at them.
                scene v71107 with dissolve
                jnfr "Did you see Jamie's white coat?" #Comes closer.
                scene v71109 with dissolve
                gbrla "N-No! I haven't. I was..." (multiple=2)
                z "(Fucking Jamie...)" (multiple=2) #Angry.
                scene v71110 with dissolve
                gbrla "Ahhm..."
                gbrla "I was... just..." (multiple=2)
                jnfr "Hm?" (multiple=2)
                scene v71111 with dissolve
                frnsska "Girls? Did one of you call me just now?" #Comes in
                scene v71112 with dissolve
                z "..."
                scene v71113 with dissolve
                jnfr "Yeah. I wanted to know if you knew where Jamie's white coat is."
                scene v71114 with dissolve
                frnsska "White coat, you say..."
                scene v71115 with dissolve
                jamie "Did someone say something about my white coat? Did you find it?"
                scene v71116 with dissolve
                jnfr "No, Jamie. I'm still looking. I was just asking around if anyone saw it." (multiple=2)
                z "(Wow... The whole household is here now...)" (multiple=2)
                scene v71117 with dissolve
                s "Gabbie? Are you in here?"
                scene v71118 with dissolve
                z "(All hope is lost...)"
                scene v71119 with dissolve
                gbrla "Yes! Here!"
                scene v71120 with dissolve
                s "Are you ready?"
                scene v71121 with dissolve
                gbrla "Errr... Yeah!"
                scene v71120 with dissolve
                s "Shall we, then?"
                scene v71122 with dissolve
                gbrla "..." #Looks at z.
                scene v71123 with dissolve
                z "(Guess we'll pick it up later, Gabbie... Damn...)"
                scene v71121 with dissolve
                gbrla "Yeah. Let's go."
                pause(1)
                scene v71124 with dissolve
                play sound "audio/creaky door.mp3"
                pause(3.3)
                #Leave. Door sound.
                scene v71125 with dissolve
                margot "Ehhh... Ma'am? I don't think this is my lab coat..." #Margot comes in wearing an oversized white coat with dirty spots on it.
                scene v71126 with dissolve
                jamie "..." #Looks at her surprised.
                pause(1)
                play sound "audio/Falling.mp3"
                scene v71127 with vpunch
                jamie "NOOOOOOOOOO! MY COAT!"
                #Falls to his knees.
            "Ask what she means.":
                $ choice_variable_ch7_31 = 1
                scene v71078 with dissolve
                z "Hm? Is it okay if you what?"
                scene v71077 with dissolve
                gbrla "..."
                #Cute angry face (emploded cheeks?)
                scene v71088 with dissolve
                gbrla "N-Nevermind..."
                scene v71089 with dissolve
                z "(Err... She's angry?!)"
                play sound "audio/Door slam.mp3"
                scene v71091 with vpunch
                jnfr "Mother! Jamie is asking where his white coat is!" #Shows up behind them.
                scene v71104 with dissolve
                jnfr "..." #Turns to them.
                scene v71106 with dissolve
                jnfr "Oh, Gabbie. You're still here?" #Looks at them.
                jnfr "Did you see Jamie's white coat?" #Comes closer.
                scene v71133 with dissolve
                gbrla "Uhm... I haven't..." (multiple=2)
                z "(This Jamie really can't keep track of his shit, can he...)" (multiple=2)
                scene v71134 with dissolve
                jnfr "Hmm..."
                scene v71135 with dissolve
                frnsska "Girls? Did one of you call me just now?" #Comes in
                scene v71136 with dissolve
                jnfr "Yeah. I wanted to know if you knew where Jamie's white coat is."
                scene v71114 with dissolve
                frnsska "White coat, you say..."
                scene v71115 with dissolve
                jamie "Did someone say something about my white coat? Did you find it?"
                scene v71116 with dissolve
                jnfr "No, Jamie. I'm still looking. I was just asking around if anyone saw it."
                scene v71117 with dissolve
                s "Gabbie? Are you in here?"
                scene v71119 with dissolve
                gbrla "Yes! Here!"
                scene v71120 with dissolve
                s "Are you ready?"
                scene v71121 with dissolve
                gbrla "Errr... Yeah!"
                scene v71120 with dissolve
                s "Shall we, then?"
                scene v71121 with dissolve
                gbrla "Yeah. Let's go."
                scene v71137 with dissolve
                gbrla "Bye, [mc_name]."
                scene v71138 with dissolve
                z "Take care, Gabbie."
                pause(1)
                scene v71124 with dissolve
                play sound "audio/creaky door.mp3"
                pause(3.3)
                #Leave. Door sound.
                scene v71125 with dissolve
                margot "Ehhh... Ma'am? I don't think this is my lab coat..." #Margot comes in wearing an oversized white coat with dirty spots on it.
                scene v71126 with dissolve
                jamie "..." #Looks at her surprised.
                pause(1)
                play sound "audio/Falling.mp3"
                scene v71127 with vpunch
                jamie "NOOOOOOOOOO! MY COAT!"
                #Falls to his knees.
    else:
        play sound "audio/leather.wav"
        scene v71128 with dissolve
        gbrla "And I was kinda asking if I can sit with you." #Sits next to him.
        scene v71129 with dissolve
        z "Rude... I was about to say no."
        scene v71129_1 with dissolve
        gbrla "*Giggles. No you weren't!" #MISSING RENDER!!!!! <-------------------
        show v7m20 with dissolve
        z "Say..."
        gbrla "Hm?"
        z "Were's everyone? I thought I'd find most of you sitting here at this time..."
        scene v71130 with dissolve
        gbrla "Oh. I'm not sure where Jenny went. She was here a minute ago."
        gbrla "And mother is busy working on a potion for Jamie. She's been spending the whole day in her lab ever since I came here."
        hide v7m20
        show v7m20 with dissolve
        z "A potion for Jamie, you say..."
        z "(I wonder what kind of potion that asshole would want...)"
        z "(Now that I think about it I never knew what exactly he was smuggling to Es-)"
        play sound "audio/Door slam.mp3"
        scene v71132 with vpunch
        jnfr "Mother! Jamie is asking where his white coat is!" #Shows up behind them.
        scene v71104 with dissolve
        jnfr "..." #Turns to them.
        scene v71106 with dissolve
        jnfr "Oh, Gabbie. You're still here?" #Looks at them.
        jnfr "Did you see Jamie's white coat?" #Comes closer.
        scene v71133 with dissolve
        gbrla "Uhm... I haven't..." (multiple=2)
        z "(This Jamie really can't keep track of his shit, can he...)" (multiple=2)
        scene v71134 with dissolve
        jnfr "Hmm..."
        scene v71135 with dissolve
        frnsska "Girls? Did one of you call me just now?" #Comes in
        scene v71136 with dissolve
        jnfr "Yeah. I wanted to know if you knew where Jamie's white coat is."
        scene v71114 with dissolve
        frnsska "White coat, you say..."
        scene v71115 with dissolve
        jamie "Did someone say something about my white coat? Did you find it?"
        scene v71116 with dissolve
        jnfr "No, Jamie. I'm still looking. I was just asking around if anyone saw it."
        scene v71117 with dissolve
        s "Gabbie? Are you in here?"
        scene v71119 with dissolve
        gbrla "Yes! Here!"
        scene v71120 with dissolve
        s "Are you ready?"
        scene v71121 with dissolve
        gbrla "Errr... Yeah!"
        scene v71120 with dissolve
        s "Shall we, then?"
        scene v71121 with dissolve
        gbrla "Yeah. Let's go."
        scene v71137 with dissolve
        gbrla "Bye, [mc_name]."
        scene v71138 with dissolve
        z "Take care, Gabbie."
        pause(1)
        scene v71124 with dissolve
        play sound "audio/creaky door.mp3"
        pause(3.3)
        #Leave. Door sound.
        scene v71125 with dissolve
        margot "Ehhh... Ma'am? I don't think this is my lab coat..." #Margot comes in wearing an oversized white coat with dirty spots on it.
        scene v71126 with dissolve
        jamie "..." #Looks at her surprised.
        pause(1)
        play sound "audio/Falling.mp3"
        scene v71127 with vpunch
        jamie "NOOOOOOOOOO! MY COAT!"
        #Falls to his knees.
    pause(1)
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_4
    label G26:
        $ persistent.g_26_unlock = 1
    scene black with fade
    stop background_s fadeout 1.0
    stop background_s2 fadeout 1.0
    stop music fadeout 1.0
    #Later
    pause(2.5)
    #Walking around in the house looking at diary.
    #Explosion sound from a door next to him.
    #Hpunch and sound
    scene v71167 with dissolve
    play background_s "audio/rain_inside.mp3" volume 0.1 fadeout 1.0 fadein 1.0 loop
    pause(2)
    #explosion sound <---
    play sound "audio/explosion.mp3"
    with hpunch
    pause(1.2)
    scene v71168 with dissolve
    z "Huh?!"
    play sound "audio/creaky door.mp3"
    scene v71169 with dissolve
    #Slams door open. sound <--
    z "What was that?! Is everyone okay?"
    scene v71170 with Dissolve(2)
    play background_s "audio/rain_inside.mp3" volume 0.25 fadeout 1.0 fadein 1.0 loop
    scene v71171 with Dissolve(2)
    margot "..." (multiple=2)
    frnsska "..." (multiple=2) #their clothes are torn and are standing to an explosion site of a pot.
    scene v71172 with dissolve
    margot "..."
    scene v71173 with dissolve
    margot "Oh. Hey there, cutie!" #Waves at him.
    margot "Did you come to visit me in the lab after all?"
    scene v71174 with dissolve
    frnsska "Go toss the failed mixture away, Margot."
    scene v71175 with dissolve
    margot "Yes, ma'am!"
    pause(0.8)
    scene v71176 with dissolve
    play sound "audio/Door slam.mp3" #Leaves door sound <--
    frnsska "And change your clothes while you're at it!"
    scene v71177 with dissolve
    frnsska "..." #Looks at her own clothes.
    scene v71178 with dissolve
    frnsska "Do you need something, [mc_name]?"
    scene v71179 with dissolve
    z "Not really. I just heard an explosion and you know..."
    frnsska "Hmm..."
    scene v71178 with dissolve
    frnsska "I better go clean myself up from this mess."
    scene v71180 with dissolve
    #Walking towards the door.
    menu:
        "[ModGreen]Stop her. (Fransisca Lust +3)":
            $ choice_variable_ch7_32 = 1
            pause(0.7)
            scene v71181 with dissolve
            z "Now, now. What are you in such a hurry for?"
            #Blocks her way with his arm.
            scene v71182 with dissolve
            frnsska "Hm?" #Raises one eyebrow
            scene v71183 with dissolve
            frnsska "What exactly do you think you're doing?"
            scene v71184 with dissolve
            z "Actually, I think you look fine the way you are."
            frnsska "..."
            scene v71185 with dissolve
            frnsska "What?"
            scene v71184 with dissolve
            z "You heard me."
            frnsska "..."
            scene v71186 with dissolve
            frnsska "Oh, I see."
            frnsska "Did you think just because you and Gabriella made a passable potion last time and you managed to take advantage of that, you can order me around?"
            scene v71187 with dissolve
            frnsska "Is that it?" #Grin
            play sound "audio/slight_hit.mp3"
            scene v71188 with vpunch #sound <--
            frnsska "Out of my way, boy!" #Moves his hand forcefully.
            play sound "audio/slight_hit.mp3"
            scene v71189 with vpunch
            frnsska "AH!" #Grabs her hand.
            play sound "audio/Falling.mp3"
            scene v71190 with vpunch
            frnsska "OHF!" #Pushes her against the wall.
            play music "audio/Jazz.mp3" volume 0.1 fadein 1.0 fadeout 1.0
            scene v71191 with dissolve
            z "You know... I'm sick of your bitchy behaviour, Fransisca."
            z "You may have that idiot Jamie fooled by the fearsome highly respected lady act, but not me."
            z "Did you think I forgot about cock craving slut you were last time?"
            frnsska "..."
            scene v71192 with dissolve
            frnsska "Y-You..."
            scene v71193 with dissolve
            frnsska "You dar-"
            play sound "audio/kiss.mp3"
            scene v71194 with dissolve
            frnsska "HMMM!" #Kisses her.
            scene v71195 with dissolve
            frnsska "Hmmmmm..." #Heart aura.
            z "(There it is again...)"
            play sound "audio/rustle.mp3"
            scene v71196 with dissolve
            frnsska "Hahhh... Ahhh..." #Falls to her knees.
            scene v71197 with dissolve
            z "Heh... You were saying?"
            scene v71198 with dissolve
            frnsska "Hahhhhhh..." #Looks up at him
            scene v71199 with dissolve
            z "Hmm... Let's move to the chair, shall we."
            pause(1)
            scene v71200 with Fade(0.5,0.5,0.5)
            pause(1)
            scene v71201 with dissolve
            #Frnsska giving him bj in a humilating position.
            frnsska "Hmmm..."
            scene v71202 with dissolve
            z "Come on. Start sucking already."
            scene v71203 with dissolve
            frnsska "Hmm..." #Kissing his dick annoyed.
            scene v71204 with dissolve
            frnsska "Ghk?" #Struggling to insert it in her mouth.
            scene v71205 with dissolve
            frnsska "Mmm..."
            scene v71211 with dissolve
            z "Hey, not bad. Not bad at all. You reached so deep without any help from me."
            show v7m22 with dissolve
            frnsska "Mmmm... Hmmm... Mmm..."
            z "Who knew a highly regarded woman like you had talents in this area."
            frnsska "Hmmmmm..." #Annoyed
            z "You ever consider changing your career path? You just might make more doing this than you're making with your high and mighty alchemist thing."
            frnsska "Mmmmmmmm..." #Annoyed
            z "..."
            scene v71207 with dissolve
            z "You're sucking it even better now..."
            z "Fransisca..."
            scene v71211 with dissolve
            z "Could it be that being insulted while shamelessly sucking my dick is turning you on?"
            scene v71209 with dissolve
            frnsska "HM!" #Surprised.
            scene v71210 with dissolve
            z "..."
            scene v71211 with dissolve
            z "Damn... I hit a jackpot, didn't I?"
            hide v7m22
            show v7m22 with dissolve
            frnsska "Mhmhm!"
            z "You keep making those angry faces, but you didn't even bother to take my dick out of your mouth to object."
            scene v71209 with dissolve
            frnsska "Hmmmm?" #Surprised looking at his dick.
            scene v71211 with dissolve
            z "If anything, you started to suck it even harder."
            hide v7m22
            show v7m23 with dissolve
            frnsska "Hmmmm..."
            z "You know... I think there's something I can do to make this even more enjoyable for you..."
            scene v71212 with dissolve
            frnsska "Hmm?" #Looking up on him.
            scene v71228 with dissolve
            pause(0.8)
            #Grabs her head and pushes it deeper.
            scene v71229 with vpunch
            frnsska "HMMM!"
            show v7m24 with dissolve
            frnsska "Ghk... Khmm... Gahkm..."
            z "Hm... I know I said this already, but man... you're such a natural at this."
            frnsska "Mgkhmm... Ghkm..."
            z "You're enjoying this aren't you?"
            frnsska "Ghm... Noohm... Ihm... Nothhh..."
            z "Come on, be honest with yourself..."
            frnsska "Ghkhm... youhm... mehkin... ghkm... meeee... dooohhh... thith..."
            z "Really? Are you sure that's the only reason?"
            frnsska "Khm... Gahmm..."
            z "We could stop if you hate this so much..."
            frnsska "Hmm..."
            frnsska "Gkhm... Thuth... uph... anth... cuhm... alrreadeeeey..."
            z "Now, now. Don't push me. I can't do it if I'm under pressure, you know."
            frnsska "Khm..."
            z "(Seriously though, this feels too good... I'm about to cum...)"
            menu:
                "Shoot it down her throat.":
                    $ choice_variable_ch7_33 = 1
                    pause(0.5)
                    scene v71230 with vpunch
                    frnsska "Khkgkkgmkgmkg!" #Surprised explosion cum
                    scene v71231 with dissolve
                    frnsska "Gaaah..." #Heart aura.
                "Pull out and cum on her face.":
                    $ choice_variable_ch7_34 = 1
                    pause(0.5)
                    scene v71232 with dissolve
                    z "Here. Take it, you like the cock-craving slut you are." #Surprised explosion cum
                    scene v71233 with dissolve
                    frnsska "Aaah..."
            pause(1.5)
            stop music fadeout 1.0
            #Z and Fransisca scene she's resting her head on his thigh after the bj.
            scene v71234 with Fade(0.5,0.5,0.5)
            pause(1)
            scene v71235 with dissolve
            z "Man... That was really good... I'm spent..."
            scene v71236 with dissolve
            frnsska "Haaahh..."
            #Wipes her face if came on it.
            z "Say..."
            z "If you're such a good alchemist how come you didn't come up with a medicine for the fever already?"
            scene v71237 with dissolve
            frnsska "..."
            scene v71238 with dissolve
            frnsska "Why you insolent..."
            scene v71239 with dissolve
            frnsska "..." #looks at him.
            scene v71240 with dissolve
            frnsska "*Sighs. How did I even end up like this..."
            scene v71241 with dissolve
            frnsska "If it weren't for that damn cock of yours..."
            scene v71242 with dissolve
            z "..."
            scene v71243 with dissolve
            frnsska "Anyway, to answer your question..."
            frnsska "Gabriella tried quite a few potions for the fever-ridden people."
            frnsska "But their fever wouldn't go down."
            frnsska "It wouldn't go up, either. Which I found very unusual."
            scene v71244 with dissolve
            z "Unusual?"
            scene v71243 with dissolve
            frnsska "Yes."
            frnsska "I've never seen such a consistant fever before. The temperature of a sick person normally varies throughout the day."
            scene v71244 with dissolve
            z "Is that so... Do you have lots of experience treating sick people?"
            scene v71243 with dissolve
            frnsska "You could say that. I've worked as a medical alchemist for a few years."
            scene v71244 with dissolve
            z "I see."
            z "So, even cooling the sick people with water doesn't work here?"
            scene v71243 with dissolve
            frnsska "No. Not in this case."
            frnsska "Their fever is strong enough to keep them idle and too tired to do anything. But it's too weak to kill them."
            frnsska "That's why no one died so far. Or recovered for that matter. Except for that white-haired girl."
            scene v71244 with dissolve
            z "..."
            z "Venus was the only one that recovered?!"
            scene v71243 with dissolve
            frnsska "As far as I know. Yes."
            scene v71244 with dissolve
            z "Interesting..."
            z "And Gabbie never got it, right?"
            scene v71243 with dissolve
            frnsska "No. No one in our family got it."
            scene v71244 with dissolve
            z "Hmm..."
            z "Even though Tamara got it while she was staying with you guys."
            scene v71243 with dissolve
            frnsska "Oh. Tamara. Have you seen her? How's she doing?"
            scene v71244 with dissolve
            z "Eh... She's... just sleeping, mostly."
            z "She did wake up and talk to me for a few seconds, but then she passed out again a few seconds later."
            scene v71243 with dissolve
            frnsska "Ah. That's to be expected."
            frnsska "A stable on-going fever will tire out the mind. Make one feel tired and dizzy all the time."
            scene v71244 with dissolve
            z "Tire out the mind, you say..."
            scene v71243 with dissolve
            frnsska "Yes. Through fever dreams."
            scene v71244 with dissolve
            z "Fever dreams?"
            scene v71243 with dissolve
            frnsska "The dreams one has when they're having a fever. They're mostly bad dreams."
            scene v71244 with dissolve
            z "Hmmm..."
            z "Does the fever also usually cause hallucinations in your experience?"
            scene v71243 with dissolve
            frnsska "Sure. That too."
            scene v71244 with dissolve
            z "And are those hallucinations usually similar?"
            scene v71243 with dissolve
            frnsska "Similar? In what way?"
            scene v71244 with dissolve
            z "As in, they see the same... ghost, for example. They all describe it in a similar way."
            scene v71243 with dissolve
            frnsska "Hmmm... I don't believe so. No."
            scene v71244 with dissolve
            z "Really?"
            z "..."
            scene v71245 with dissolve
            z "Wait..."
            play sound "audio/Falling.mp3"
            scene v71246 with vpunch
            #sound <--
            z "I have an idea!" (multiple=2) #Gets up.
            frnsska "Ohf..." (multiple=2)
            scene v71247 with dissolve
            z "Sorry! I gotta go. See you later, okay?" (multiple=2)
            frnsska "Ah!" (multiple=2)
            scene v71248 with dissolve
            play sound "audio/Door slam.mp3"
            pause(1)
            #Slams door on his way out. sound <--
            scene v71249 with dissolve
            frnsska "..."
            if came_from_gallery == 0:
                $ frnsska_lst += 3
            play sound "audio/stats.wav"
            show screen button_lst with dissolve
            hide screen button_lst with dissolve
        "Don't.":
            $ choice_variable_ch7_35 = 1
            pause(0.7)
            play sound "audio/slight_hit.mp3"
            scene v71213 with vpunch
            pause(0.25)
            #Pumbs into him on her way out.
            #Sound. <--
            scene v71214 with dissolve
            frnsska "*Pumbs into you."
            scene v71215 with dissolve
            z "Say..."
            scene v71216 with dissolve
            frnsska "Hm?"
            z "If you're such a good alchemist how come you didn't come up with a medicine for the fever already?"
            pause(1) #Pause.
            scene v71217 with dissolve
            frnsska "Why you insolent little..."
            scene v71218 with dissolve
            frnsska "..." #looks at him.
            scene v71219 with dissolve
            frnsska "*Sighs."
            scene v71220 with dissolve
            frnsska "Listen well, brat. I'm only going to explain it once."
            frnsska "And only because I believe the alchemy shouldn't be insulted by a clueless incompetent kid like you."
            scene v71221 with dissolve
            frnsska "It's not treatable with potions."
            frnsska "Gabriella tried quite a few of them for the fever-ridden people."
            frnsska "But their fever wouldn't go down."
            frnsska "It wouldn't go up, either. Which I found very unusual."
            scene v71222 with dissolve
            z "Unusual?"
            scene v71221 with dissolve
            frnsska "Yes."
            frnsska "I've never seen such a consistant fever before. The temperature of a sick person normally varies throughout the day."
            scene v71222 with dissolve
            z "Is that so... Do you have lots of experience treating sick people?"
            scene v71221 with dissolve
            frnsska "You could say that. I've worked as a medical alchemist for a few years."
            scene v71222 with dissolve
            z "I see."
            z "So, even cooling the sick people with water doesn't work here?"
            scene v71221 with dissolve
            frnsska "No. Not in this case."
            frnsska "Their fever is strong enough to keep them idle and too tired to do anything. But it's too weak to kill them."
            frnsska "That's why no one died so far. Or recovered for that matter. Except for that white-haired girl."
            scene v71222 with dissolve
            z "..."
            z "Venus was the only one that recovered?!"
            scene v71221 with dissolve
            frnsska "As far as I know. Yes."
            scene v71222 with dissolve
            z "Interesting..."
            z "And Gabbie never got it, right?"
            scene v71221 with dissolve
            frnsska "No. No one in our family got."
            scene v71222 with dissolve
            z "Hmm..."
            z "Even though Tamara got it while she was staying with you guys."
            scene v71221 with dissolve
            frnsska "Surprisingly prescriptive of you. Yes."
            scene v71222 with dissolve
            z "..."
            scene v71221 with dissolve
            frnsska "Speaking of Tamara. Have you seen her? How's she doing?"
            scene v71222 with dissolve
            z "Eh... She's... just sleeping, mostly."
            z "She did wake up and talk to me for a few seconds, but then she passed out again a few seconds later."
            scene v71221 with dissolve
            frnsska "Ah. That's to be expected."
            frnsska "A stable on-going fever will tire out the mind. Make one feel tired and dizzy all the time."
            scene v71222 with dissolve
            z "Tire out the mind, you say..."
            scene v71221 with dissolve
            frnsska "Yes. Through fever dreams."
            scene v71222 with dissolve
            z "Fever dreams?"
            scene v71221 with dissolve
            frnsska "The dreams one has when they're having a fever. They're mostly bad dreams."
            scene v71222 with dissolve
            z "Hmmm..."
            z "Does the fever also usually cause hallucinations in your experience?"
            scene v71221 with dissolve
            frnsska "Sure. That too."
            scene v71222 with dissolve
            z "And are those hallucinations usually similar?"
            scene v71221 with dissolve
            frnsska "Similar? In what way?"
            scene v71222 with dissolve
            z "As in, they see the same... ghost, for example. They all describe it in a similar way."
            scene v71221 with dissolve
            frnsska "Hmmm... I don't believe so. No."
            scene v71222 with dissolve
            z "Really?"
            z "..."
            z "Wait..."
            z "I have an idea!"
            scene v71223 with dissolve
            z "Gotta run. See you later!"
            play sound "audio/slight_hit.mp3"
            scene v71224 with vpunch
            frnsska "Ohf..." #Pumbs into her on his way out.
            scene v71225 with dissolve
            #Slams door on his way out. sound <--
            play sound "audio/Door slam.mp3"
            frnsska "..."
            scene v71226 with dissolve
            frnsska "Damn brat..."
            scene v71227 with dissolve
    pause(1)
    scene black with fade
    stop background_s fadeout 1.0
    stop music fadeout 1.0
    $ renpy.end_replay()
    if came_from_gallery == 1:
        $ came_from_gallery = 0
        jump gallery_4
    #Later
    pause(2.5)
    #18) Suggest to Ymi and Vns to go into Tamara's mind to see what they can find. {@100%@100%R@0%W}
    #Z is talking to Yumi and Venus at the sick house:
    scene v71139 with dissolve
    pause(1)
    play background_s "audio/rain_inside.mp3" volume 0.2 fadeout 1.0 fadein 1.0 loop
    z "So... I had this idea."
    z "Let me know if it's crazy."
    scene v71140 with dissolve
    ymi "..." (multiple=2) #looking at each other
    vns "..." (multiple=2)
    scene v71141 with dissolve
    play music "audio/die_zwei_geschwister.mp3" volume 0.7 fadeout 1.0 fadein 1.0
    ymi "Okay. Shoot."
    scene v71142 with dissolve
    z "So, many of the sick people said they've seen weird things, right?"
    scene v71143 with dissolve
    vns "Yeah?"
    vns "I told you it's probably just h-"
    scene v71142 with dissolve
    z "Hallucinations. I know, I know."
    z "But you know how to create an illusion and enter someone's mind, right?"
    z "Like Axius did that time when he entered yours?"
    vns "..." (multiple=2)
    ymi "..." (multiple=2)
    scene v71144 with dissolve
    ymi "..." (multiple=2) #Looks at venus.
    vns "..." (multiple=2) #Looks at yumi.
    scene v71145 with dissolve
    vns "Me? Well... Yeah."
    scene v71146 with dissolve
    vns "Why?"
    scene v71147 with dissolve
    z "So... You're basically just hanging around until Seira finds her friend."
    z "And I was thinking we-"
    scene v71148 with dissolve
    ymi "You want to go into one of the sick people's mind?"
    scene v71142 with dissolve
    z "Exactly. Let's say... Tamara."
    scene v71149 with dissolve
    vns "Eh? But what is that supposed to accomplish?" (multiple=2)
    ymi "Hmm..." (multiple=2)
    scene v71150 with dissolve
    z "Well, we could get an insight on why their having similar hallucinations, right?"
    z "Honestly, I think it's worth a shot to try an see exactly what she's going through."
    scene v71149 with dissolve
    vns "Hmmm... But-"
    play sound "audio/chair.mp3"
    scene v71151 with dissolve
    ymi "I think that just might be a good idea."
    scene v71152 with dissolve
    vns "Wait. Really?"
    scene v71151 with dissolve
    ymi "Yeah. Maybe we could learn something here."
    scene v71153 with dissolve
    vns "Hmmm..."
    if a_trst >= 3:
        scene v71154 with dissolve
        ymi "Plus, Annie told me to trust what [mc_name] says. Said he had a really good insight and judgement."
        scene v71155 with dissolve
        z "..."
    scene v71152 with dissolve
    vns "Okay. I'm sold. Let's do it."
    scene v71156 with dissolve
    vns "Just give me a few minutes to prepare." #Sounds of her doing stuff.
    scene v71157 with dissolve
    pause(2.5)
    play sound "audio/chair squeak.mp3"
    scene v71158 with dissolve
    #Sitting sound <--
    #Z goes to sit down next to sleeping tamara.
    z "..."
    scene v71159 with dissolve
    $ renpy.pause(1, hard=True)
    scene v71160 with dissolve
    $ renpy.pause(0.7, hard=True)
    #Pulls out the mirror but drops it.
    play sound "audio/dropping mirror.mp3"
    scene v71161 with dissolve
    z "Woops..."
    scene v71162 with dissolve
    z "Where did it even go..." #Searching under the bed.
    pause(2)
    scene v71163 with dissolve
    z "There!"
    stop music fadeout 2.0
    stop background_s fadeout 2.0
    pause(1)
    z "(Is that...)"
    #Picks it up.
    scene v71164 with Dissolve(2)
    z "V-Venus?!"
    play sound "audio/tension-build.mp3"
    $ renpy.pause(3, hard=True)
    scene v71165 with Dissolve(4.2)
    $ renpy.pause(3, hard=True) #Hard pause
    scene v71166 with Dissolve(4.2)
    $ renpy.pause(0.6, hard=True)
    scene black
    $ renpy.pause(4, hard=True)
    play sound "audio/mirror.mp3" volume 0.4
    $ renpy.pause(7, hard=True)
    show mirror with Dissolve(2.0)
    $ renpy.pause(5, hard=True)
    #Venus's reflection.
    #Turns around, slow dissolve and hard puase. (Both the image in the mirror and z turning around are visible!!!) <------------
    #END OF UPDATE.
    jump chapter_8

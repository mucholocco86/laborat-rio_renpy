label ep9_others_branch_label:
play music "music/ep9/halloween_again.mp3"
scene ep9_others_branch1 with dissolve
de "[mc_de_up]! Come! Sit down and join us!"
label ep9_others_branch_label_wt:
play music "music/ep9/halloween_again.mp3"
scene ep9_others_branch2 with dissolve
mc "Who's this?"
de "I have no clue, but she was thirsty."
scene ep9_others_branch3 with dissolve
uk "Yeah, I'm just a thirsty ghoul."
mc "With the bluest eyes I've ever seen. Wow!"
uk "Haha! Thanks."
scene ep9_others_branch4 with dissolve
de "Are you single?"
scene ep9_others_branch9 with dissolve
uk "Yeah?"
de "Are you interested in my friend here? He's single too."
scene ep9_others_branch5 with dissolve
mc "What are you doing?"
scene ep9_others_branch6 with dissolve
de "What? You're the one who started hitting on her."
scene ep9_others_branch5 with dissolve
mc "Uh, I wasn't."
scene ep9_others_branch6 with dissolve
de "I'm helping you out, pal."
scene ep9_others_branch5 with dissolve
mc "Thanks, but I'm good."
scene ep9_others_branch6 with dissolve
de "What's the matter? Did you quit the dating game?"
scene ep9_others_branch7 with dissolve
mc "No, I didn't quit it. But I've been doing a lot of thinking lately."
if ep8_jill_rejected_you:
    mc "I've been kinda bummed out after getting rejected by Jill, but I'm trying to move on."
    mc "And I wake up feeling a bit hopeful about being single, but when I go to bed, I feel like I'm not enjoying it at all."
else:
    mc "It's both bummed me out and made me hopeful, but it comes and goes."
    mc "Like, I wake up feeling happy about being single, but then I go to bed feeling like I'm missing out on something."
scene ep9_others_branch8 with dissolve
uk "I can relate to that. Cheers to being lonesome!"
scene ep9_others_branch3 with dissolve
if ep8_jill_rejected_you:
    uk "If you're dealing with heartbreak, you need to get back up on the horse. Don't give up on dating because some past relationship didn't work out."
    uk "You'll find the right one for you eventually."
else:
    uk "You need to get back up on the horse. Don't give up on dating because you haven't found the right one yet."
    uk "It will happen eventually."
mc "Those are some wise words."
stop music fadeout 3
scene ep9_others_branch6 with dissolve
de "So, who are you dating right now?"
if not ep8_nora_number and not envyLikesYou and jade_state != 1 and not ep8_quinn_lewd and not ep7_lily_lewd and not (ep7_rica_lewd or ep7_riona_lewd or ep5_fuckedRiona):
    jump ep9_after_chat_label
hide screen new_phone_screen
play music "music/ep9/passing_time.mp3"
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
scene anim_rain_ep9 with wipeleft
pause
$ guideSuggestedPage = 59
scene ep9_others_branch11 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=3)
$ ep9_others_texted = [False,False,False,False,False,False]
label ep9_others_text_loop_label:
$ renpy.block_rollback()
scene ep9_others_branch12 with dissolve
menu:
    "Text Nora (Got Nora's number)" if ep8_nora_number and not ep9_others_texted[0]:
        $ ep9_others_texted[0] = True

        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"It's really pouring tonight.",False])
        $ text_message_screen_list.append(["Nora","Lovely, isn't it? I turned off my TV and cracked open a window to listen. But it's almost stopped raining here.",True])
        $ text_message_screen_list.append(["%s" % name,"How nice. Here it's still going. I'm sitting here watching my window, drinking a beer.",False])
        $ text_message_screen_list.append(["Nora","That sounds awfully sad. Are you all right?",True])
        show screen text_message_screen
        $ renpy.pause()
        $ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
        scene anim_rain_ep9 with dissolve
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch17 with dissolve
        $ renpy.music.stop(channel="sfx1", fadeout=3)
        $ tmpInt += 1
        $ renpy.pause()
        scene anim_nora_idle_ep9 with dissolve
        $ tmpInt += 1
        $ renpy.pause()

        menu:
            "Yeah, I'm fine":
                hide screen text_message_screen
                $ tmpInt2 = 4
                $ text_message_screen_list.append(["%s" % name,"Yeah, I'm fine. I didn't realize it sounded sad. I'm not just drinking; I'm eating crackers too. mphone_emoji_smile",False])
                $ text_message_screen_list.append(["Nora","I was picturing you in black and white, staring out your window with a beer in one hand and the phone in the other, deciding to text me to keep up your morale.",True])
                $ text_message_screen_list.append(["%s" % name,"I'm not sad or in black and white, but you're not far off. That's what I look like right now.",False])
                $ text_message_screen_list.append(["%s" % name,"What about you? What do you look like now?",False])
                $ tmpInt += 1
                scene ep9_others_branch19 with dissolve
                show screen text_message_screen
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt2 = len(text_message_screen_list)
                hide screen text_message_screen
                scene ep9_others_branch22 with dissolve

                $ text_message_screen_list.append(["Nora","I'm unwinding on my couch in comfortable clothes.",True])
                $ text_message_screen_list.append(["%s" % name,"Comfortable clothes? Sounds hot.",False])
                $ text_message_screen_list.append(["Nora","Not particularly. Well...? I'm not wearing a bra, so there's that.",True])
                $ text_message_screen_list.append(["%s" % name,"Sorry, I was gonna say something, but I completely lost my train of thought.",False])
                $ text_message_screen_list.append(["Nora","Haha! I won't mention my bra again, then. I wouldn't want you to stop talking to me. mphone_emoji_smile",True])
                $ tmpInt += 1
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
                $ tmpInt2 = len(text_message_screen_list)
            "I've felt better":

                hide screen text_message_screen
                $ tmpInt2 = 4
                $ text_message_screen_list.append(["%s" % name,"I've felt better.",False])
                $ text_message_screen_list.append(["Nora","Oh, dear. What's got you feeling down?",True])
                $ text_message_screen_list.append(["%s" % name,"Honestly, I don't know. I guess I've felt kind of lonely lately.",False])
                $ text_message_screen_list.append(["Nora","In my experience, loneliness means you don't enjoy your own company. Work on being comfortable with yourself, and you won't feel as lonely when you're alone.",True])
                $ tmpInt += 1
                show screen text_message_screen
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                scene ep9_others_branch21 with dissolve
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                scene ep9_others_branch20 with dissolve
                $ tmpInt2 = 8
                hide screen text_message_screen
                $ text_message_screen_list.append(["%s" % name,"Aha, is that something you've done?",False])
                $ text_message_screen_list.append(["Nora","I've always been a blast to be around. I do love my own company.",True])
                $ text_message_screen_list.append(["%s" % name,"I'm sure I'd love it too.",False])
                $ text_message_screen_list.append(["Nora","Such a charmer. mphone_emoji_smile",True])
                $ tmpInt += 1
                show screen text_message_screen
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt2 = len(text_message_screen_list)

        hide screen text_message_screen
        $ text_message_screen_list.append(["%s" % name,"Will I see you at the gym next week?",False])
        $ text_message_screen_list.append(["Nora","Next week will be a bit hectic, but I'll try to squeeze in some workout. However, I can't say when.",True])
        $ text_message_screen_list.append(["%s" % name,"Hopefully, I'll run into you then.",False])
        $ text_message_screen_list.append(["Nora","We'll see what chance brings us. If nothing, then at least we can talk like this.",True])
        $ text_message_screen_list.append(["%s" % name,"Absolutely. Or maybe we can meet up someplace else? If you're interested, that is.",False])
        $ tmpInt += 1

        scene ep9_others_branch22 with dissolve
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
        scene ep9_others_branch23 with dissolve
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Nora","Maybe I am.",True])
        $ text_message_screen_list.append(["Nora","Enjoy your evening, [name]. Thanks for the pleasant distraction.",True])
        $ text_message_screen_list.append(["%s" % name,"You too.",False])
        $ tmpInt += 1
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_others_branch24 with dissolve
        no "Ugh... What am I doing...?"

        $ mphone_scene_to_chat("Nora",text_message_screen_list)
        $ tmpInt = 0
        $ text_message_screen_list = []

        jump ep9_others_text_loop_label
    "Text Nicole (Nicole likes you)" if envyLikesYou and not ep9_others_texted[1]:
        $ ep9_others_texted[1] = True

        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"How are you?",False])
        $ text_message_screen_list.append(["Nicole","[name]! I'm fine, but super tired. I just got off work and am about to head home.",True])
        $ text_message_screen_list.append(["%s" % name,"I hope you brought an umbrella.",False])
        $ text_message_screen_list.append(["Nicole","No! Is it raining?",True])
        $ text_message_screen_list.append(["%s" % name,"It is here. You might get wet.",False])

        scene ep9_others_branch13 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch25 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_others_branch26 with dissolve

        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Nicole","Thanks for the heads up. I'll check if there's an umbrella in the lost and found.",True])
        $ text_message_screen_list.append(["Nicole","Gotta go! Talk another time, sweetie. Mwah!",True])
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Nicole",text_message_screen_list)
        jump ep9_others_text_loop_label
    "Text Jade (Ongoing affair)" if jade_state == 1 and not ep9_others_texted[2]:
        $ ep9_others_texted[2] = True

        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"Good evening...",False])
        $ text_message_screen_list.append(["Jade","Not the best time.",True])
        $ text_message_screen_list.append(["%s" % name,"Got it.",False])
        $ text_message_screen_list.append(["Jade","Did you want something?",True])
        $ text_message_screen_list.append(["%s" % name,"No. Well...",False])
        $ text_message_screen_list.append(["Jade","Spit it out.",True])

        scene ep9_others_branch13 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch27 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_others_branch28 with dissolve
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"I wanted to talk to you. And check that everything is good after last time.",False])
        $ text_message_screen_list.append(["Jade","Yes. We're in the clear. But let's never meet like that again.",True])
        $ text_message_screen_list.append(["%s" % name,"I'll try my best to stay clear of it. When will I see you again?",False])
        $ text_message_screen_list.append(["Jade","I'll talk to you at school, ok? Ironically, it's much safer to flirt with a student there than at home. mphone_emoji_kiss",True])
        $ text_message_screen_list.append(["%s" % name,"Haha! Deal. mphone_emoji_kiss",False])
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch29 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ mphone_scene_to_chat("Jade",text_message_screen_list)
        hide screen text_message_screen
        jump ep9_others_text_loop_label
    "Text Quinn (Quinn likes you)" if ep8_quinn_lewd and not ep9_others_texted[3]:
        $ ep9_others_texted[3] = True

        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []

        $ text_message_screen_list.append(["%s" % name,"I got my outfit ready for the party.",False])
        $ text_message_screen_list.append(["Quinn","Let me guess. Gimp suit?",True])
        $ text_message_screen_list.append(["%s" % name,"Almost. Spartan warrior.",False])
        $ text_message_screen_list.append(["Quinn","Ah! You're going as the quintessential college douchebag. Gotcha.",True])
        $ text_message_screen_list.append(["%s" % name,"Come on, it's not. Is it?",False])
        $ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
        scene anim_rain_ep9 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch30 with dissolve
        $ renpy.music.stop(channel="sfx1", fadeout=3)
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Quinn","I never saw someone wear it who didn't do it for scoring pussy.",True])
        $ text_message_screen_list.append(["%s" % name,"Sounds to me like I chose the perfect costume.",False])
        $ text_message_screen_list.append(["Quinn","Pff.",True])
        $ text_message_screen_list.append(["%s" % name,"What about you?",False])
        $ text_message_screen_list.append(["Quinn","My costume will make you cum in your pants faster than you ever have before.",True])
        scene ep9_others_branch31 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch32 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"Sounds sexy. I'm in.",False])
        $ text_message_screen_list.append(["Quinn","Earn it.",True])
        $ text_message_screen_list.append(["%s" % name,"How?",False])
        $ text_message_screen_list.append(["Quinn","Keep your dick in your pants during the party, and I'll take you home to my lair.",True])
        $ text_message_screen_list.append(["%s" % name,"Is that some kind of a challenge?",False])
        $ text_message_screen_list.append(["Quinn","I don't think you can do it.",True])
        scene ep9_others_branch33 with dissolve
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
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch34 with dissolve
        menu:
            "For you, I can":
                hide screen text_message_screen
                $ tmpInt += 1
                $ tmpInt2 = len(text_message_screen_list)
                $ text_message_screen_list.append(["%s" % name,"If you're the prize, I can.",False])
                $ text_message_screen_list.append(["Quinn","Doubt it.",True])
                $ text_message_screen_list.append(["%s" % name,"Besides, I'm wearing some kind of a skirt, so it's technically not pants I'd be cumming in.",False])
                $ text_message_screen_list.append(["Quinn","You've already lost.",True])
                $ text_message_screen_list.append(["%s" % name,"Haha! Nah. You'll see.",False])

                scene ep9_others_branch35 with dissolve
                show screen text_message_screen
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                scene ep9_others_branch36 with dissolve
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
            "You're right. I can't":
                hide screen text_message_screen
                $ tmpInt += 1
                $ tmpInt2 = len(text_message_screen_list)
                $ text_message_screen_list.append(["%s" % name,"You're right. I can't. Especially not when I'm dressed as a sexy Spartan warrior.",False])
                $ text_message_screen_list.append(["Quinn","Then you have already lost. Shame.",True])
                $ text_message_screen_list.append(["%s" % name,"Well, your costume would have to be really worth it.",False])
                $ text_message_screen_list.append(["Quinn","It is.",True])

                scene ep9_others_branch37 with dissolve
                show screen text_message_screen
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
                $ tmpInt += 1
                $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Quinn",text_message_screen_list)
        scene ep9_others_branch38 with dissolve
        $ renpy.pause()

        jump ep9_others_text_loop_label
    "Text Lily (Lily likes you)" if ep7_lily_lewd and not ep9_others_texted[4]:
        $ ep9_others_texted[4] = True
        label ep9_lily_lewd_label:
        if _in_replay:
            hide screen new_phone_screen
            if persistent.name == None:
                $ name = "MC"
            else:
                $ name = persistent.name
            $ ep3_lilyHatesYou = False
            play music "music/ep9/passing_time.mp3"
            $ currentEpisode = 9
            $ mphones_emotes = []
            $ mphones_emotes.append(["mphone_emoji_evil",False])
        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []

        $ text_message_screen_list.append(["%s" % name,"Are you free?",False])
        $ text_message_screen_list.append(["Lily","For you, I'll make time. What's up?",True])
        $ text_message_screen_list.append(["%s" % name,"Not much. I'm kind of bored. I've been browsing Rooster and whatnot.",False])
        $ text_message_screen_list.append(["Lily","Dude, if you're bored, just call me. I can...entertain you.",True])


        scene ep9_others_branch13 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        scene ep9_others_branch39 with dissolve
        $ renpy.pause()
        scene ep9_others_branch40 with dissolve
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"Oh yeah? Doing what?",False])
        $ text_message_screen_list.append(["Lily","You know what. mphone_emoji_evil",True])
        $ text_message_screen_list.append(["%s" % name,"Haha!",False])
        show screen text_message_screen
        $ renpy.pause()
        scene ep9_others_branch41 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()


        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Lily","I've been meaning to ask you... You don't post a lot on Rooster. What's up with that?",True])
        $ text_message_screen_list.append(["%s" % name,"I don't know. I prefer to browse and comment on others' clucks.",False])
        $ text_message_screen_list.append(["Lily","Post more.",True])
        $ text_message_screen_list.append(["%s" % name,"Like what?",False])
        $ text_message_screen_list.append(["Lily","Like a picture of yourself or something. It doesn't have to be much.",True])

        scene ep9_others_branch42 with dissolve
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
        scene ep9_others_branch43 with dissolve
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Lily","Wait, I found a picture of you. Yeah... This one will work.",True])
        $ text_message_screen_list.append(["%s" % name,"Work for what?",False])
        $ text_message_screen_list.append(["Lily","Hey, you're not here with me, and I'm in the mood.",True])
        $ text_message_screen_list.append(["%s" % name,"Don't tell me you're using my picture for it.",False])


        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch44 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        scene ep9_others_branch45 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_others_branch44 with dissolve
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Lily","Hot, huh? I'm looking at it right now as I touch myself.",True])
        $ text_message_screen_list.append(["%s" % name,"I don't believe you.",False])
        show screen text_message_screen
        $ renpy.pause()
        scene ep9_others_branch45 with dissolve
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        if not _in_replay:
            $ mphone_scene_to_chat("Lily",text_message_screen_list)

        play sound "sound_effects/cellphone.mp3"
        scene ep9_others_branch16 with dissolve
        "*{i}Cellphone rings{/i}*"
        scene ep9_others_branch46 with dissolve
        ly "Ah, that's better than that old picture of you."
        mc "You weren't kidding."
        scene ep9_others_branch47 with dissolve
        ly "Why would I joke about it? Haven't you gotten it yet, [name]?"
        ly "I want you."
        mc "You want me?"
        scene ep9_others_branch49 with dissolve
        ly "Grr! Well, you know what I want. And someday, you'll wake up and know you want it too."
        ly "Until then... Wanna watch me?"
        scene ep9_others_branch48 with dissolve
        mc "Yeah... Go on."
        scene ep9_others_branch50 with dissolve
        ly "You like it when I touch myself to you, [name]?"
        scene ep9_others_branch51 with dissolve
        ly "You look stunned. You're horny too. I can tell."
        ly "Help a girl out here, [name]. Show it to me."
        scene ep9_others_branch52 with dissolve
        ly "Haha, I knew it... Damn, that thing looks even bigger on the phone. It's probably the wide-angle lens."
        scene anim_lily_idle_ep9 with dissolve
        menu:
            "Finger your pussy":
                mc "Finger your pussy for me..."
                scene ep9_others_branch54 with dissolve
                ly "You want this, huh?"
                ly "Let me fix my phone so that we can watch each other."
                scene anim_lily_finger_ep9 with dissolve
            "Finger your ass":
                mc "Finger your ass for me..."
                scene ep9_others_branch55 with dissolve
                if ep3_lilyHatesYou:
                    ly "Haha! What is it with you and sticking fingers in my ass?"
                else:
                    ly "Mmm... You like it kinky, huh?"
                ly "Hold on. Let me fix my phone so that we can watch each other."
                scene anim_lily_finger_ass_ep9 with dissolve

        mc "Yeah... That's so hot."
        ly "Stroke it for me, [name]. I wanna watch you beat it while I finger myself thinking about you entering me."
        pause
        scene ep9_others_branch56 with dissolve
        ly "Since you're not here, I'll have to settle for the next best thing..."
        ly "I named him [name] Junior."
        scene ep9_others_branch57 with dissolve
        ly "Now, where should I put it?"
        menu:
            "Pussy":
                mc "Put it in your pussy."
                $ renpy.sound.play("sound_effects/season2/vibrator.mp3", channel="sfx3", loop=True)
                scene anim_lily_dildo_ep9 with dissolve
                ly "Hngh..."
                mc "That's so hot!"
                pause
                ly "[name]... I'm gonna cum..."
                scene ep9_others_branch58 with hpunch
                ly "Ahhhhh..."
            "Asshole":
                mc "Put it in your asshole."
                $ renpy.sound.play("sound_effects/season2/vibrator.mp3", channel="sfx3", loop=True)
                scene anim_lily_dildo_ass_ep9 with dissolve
                ly "Oh, fuck!"
                mc "Yes, keep doing that!"
                pause
                ly "[name]... I'm gonna cum..."
                scene ep9_others_branch58b with hpunch
                ly "Ahhhhh..."
        scene ep9_others_branch59 with dissolve
        $ renpy.music.stop(channel="sfx3", fadeout=3)
        el "Lily, what are you... Oh!"
        ly "Haha! Oh, shit! Hey!"
        ly "Say hi to [name]!"
        scene ep9_others_branch60 with dissolve
        el "Oh, fuck! Wow! Um..."
        mc "Jesus! Sorry, Elena!"
        el "No! I'm sorry, [name]. Uh... Nice cock! It seems like the legend is true."
        scene ep9_others_branch61 with dissolve
        ly "Hahaha!"
        ly "Call me another time. I gotta go do some damage control."
        scene ep9_others_branch62 with dissolve
        mc "Fuck! That was... Wow..."
        $ renpy.end_replay()
        $ persistent.ep9_lewd_lily = True
        $ calcScenes()
        $ new_bio("Lily", "I texted Lily and ended up having some kind of phone sex with her. Elena walked in on her before we could finish.")
        $ new_bio("Elena", "Elena walked in on Lily having phone sex with me.")
        $ mphone_stats_add_girl_s3("lily","You had phone sex with Lily in episode 9.")
        jump ep9_others_text_loop_label
    "Text Riona (Riona likes you)" if (ep7_rica_lewd or ep7_riona_lewd or ep5_fuckedRiona) and not ep9_others_texted[5]:
        $ ep9_others_texted[5] = True

        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["%s" % name,"What are you up to?",False])
        $ text_message_screen_list.append(["Riona","Not much. Listening to some music and annoying Cammy with my off-pitch singing. You?",True])
        $ text_message_screen_list.append(["%s" % name,"I'm fiddling with my phone. I'm pretty bored, actually. And it's too late to do something fun.",False])

        if ep7_riona_help:
            scene ep9_others_branch63 with dissolve
        else:
            scene ep9_others_branch63b with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_others_branch64 with dissolve
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Riona","Feels nice to have some time off between midterms and new classes, huh?",True])
        $ text_message_screen_list.append(["%s" % name,"Yeah. With the Halloween planning and some drama put aside, my stress levels are way lower after the midterms.",False])
        if not ep7_riona_help:
            $ text_message_screen_list.append(["Riona","Good for you.",True])
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

        if ep7_riona_help:
            hide screen text_message_screen
            $ tmpInt += 1
            $ tmpInt2 = len(text_message_screen_list)

            $ text_message_screen_list.append(["Riona","Same here, but mostly thanks to your help with my paranoia.",True])
            $ text_message_screen_list.append(["%s" % name,"It wasn't paranoia. You were right.",False])
            $ text_message_screen_list.append(["Riona","Yeah. It's so fucking creepy. I get chills thinking about it still.",True])
            $ text_message_screen_list.append(["%s" % name,"Let me know if that dude bothers you again.",False])
            $ text_message_screen_list.append(["Riona","You'd be the first one I'd call. mphone_emoji_kiss",True])
            scene ep9_others_branch65 with dissolve
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
        else:
            scene ep9_others_branch65b with dissolve
            $ tmpInt += 1
            $ renpy.pause()

        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"Say hi to Cammy for me.",False])
        show screen text_message_screen
        $ renpy.pause()
        hide screen text_message_screen

        scene ep9_others_branch66 with dissolve
        ri "[name] says hi."
        scene ep9_others_branch68 with dissolve
        cam "Tell him swiggity swooty. He knows what it means."
        scene ep9_others_branch67 with dissolve
        ri "What?"
        scene ep9_others_branch69 with dissolve
        cam "Swiggity swooty. Just tell him."

        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Riona","She said \"swiggity swooty\" to you.",True])
        $ text_message_screen_list.append(["%s" % name,"Huh? What does that mean?",False])
        scene ep9_others_branch15 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        scene ep9_others_branch72 with dissolve
        $ tmpInt += 1
        $ renpy.pause()

        hide screen text_message_screen
        scene ep9_others_branch71 with dissolve
        ri "Cammy!"
        scene ep9_others_branch70 with dissolve
        cam "Hahaha! You actually typed that?"

        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Riona","Nothing. She's being an ass. Haha!",True])
        $ text_message_screen_list.append(["Riona","Anyway, have a good one!",True])
        scene ep9_others_branch73 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

        hide screen text_message_screen
        $ mphone_scene_to_chat("Riona",text_message_screen_list)
        play sound "sound_effects/shove.mp3"
        scene ep9_others_branch74 with hpunch
        ri "Why did you have to embarrass me like that?"
        cam "Haha! What!?"
        jump ep9_others_text_loop_label
    "Stop texting" if not (ep8_quinn_lewd and not ep9_others_texted[3]):
        stop music fadeout 3
        if True in ep9_others_texted:
            scene ep9_others_branch13 with dissolve
            mc "(That made me feel a bit better...)"
        else:
            scene ep9_others_branch14 with dissolve
            mc "(Nah... I don't feel like texting anyone.)"
$ disabled_contacts_list = []
show screen new_phone_screen
play music "music/ep9/halloween_again.mp3"

label ep9_after_chat_label:
scene ep9_others_branch7 with dissolve
if ep8_nora_number or ep7_lily_lewd or ep6_envy_lewd or envyLikesYou or ep8_quinn_lewd or jade_state == 1:
    mc "I'm not exactly dating anyone, but I see the potential."
else:
    mc "No one... I literally have nothing going on for me."
scene ep9_others_branch9 with dissolve
if ep8_nora_number or ep7_lily_lewd or ep6_envy_lewd or envyLikesYou or ep8_quinn_lewd or jade_state == 1:
    de "Snatch him up while he's on the meat market."
else:
    de "While he sounds like a sad fuck, I can guarantee you that you'd be missing out on something great if you don't snatch him up while he's on the meat market."
uk "Haha! He's pretty cute, but I don't know... He came dressed as a Spartan. Maybe he's the violent type?"
menu:
    "You got me there":
        $ ep9_dangerous = True
        scene ep9_others_branch3 with dissolve
        mc "Yeah, you got me there."
        mc "Unless you like trouble, you'd better stay away from me. I'm dangerous."
        uk "Haha! Mr. Danger, huh? You're funny."
    "Not really":
        $ ep9_dangerous = False
        mc "No, I'm not that violent."
        de "He's as huggable as a teddy bear. That's what I think."
        scene ep9_others_branch5 with dissolve
        mc "How is this helping me, Derek?"
        scene ep9_others_branch3 with dissolve
        uk "Hahaha! Well, it's nice meeting you, Mr. Teddy Bear."

    
if wt_ep9_branch_numbers > 1 and branchIsabella:
    mc "(I need to get back to my room...)"
    mc "I need to check on something real quick."
    jump ep9_bella_branch_label
scene ep9_others_branch10 with dissolve
stop music fadeout 3
"The HOTs! The HOTs! They're finally here!"
de "Fuck yes! Let's go check it out!"
jump ep9_wave2_label

label ep9_lily_nicole_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep4_smoked_weed = True
    $ envyLikesYou = True
    $ affinity = "DIK"
    $ ep7_lily_lewd = True

play music "music/ep6/licensed_music/track37.mp3"
queue music ["music/ep6/licensed_music/track37.mp3","music/ep7/licensed_music/track55.mp3","music/ep6/licensed_music/track42.mp3"]

scene ep9_lily_nicole_lewd1 with dissolve
nic "Hahaha!"
mc "What's so funny?"
scene ep9_lily_nicole_lewd2 with dissolve
nic "Lily said it's funny how we're waiting for a guy to get his coat. Get it?"
scene ep9_lily_nicole_lewd3 with dissolve
mc "I can't argue with that. I was wearing a skirt, too."
scene ep9_lily_nicole_lewd2 with dissolve
nic "Haha! Sure were!"
scene ep9_lily_nicole_lewd4 with dissolve
ly "It's not that cold."
scene ep9_lily_nicole_lewd3 with dissolve
mc "True. But it feels good wearing normal clothes."
scene ep9_lily_nicole_lewd4 with dissolve
ly "Gotta cover up those tits, huh?"
scene ep9_lily_nicole_lewd3 with dissolve
mc "Haha! Yeah, I don't know how girls do it."
scene ep9_lily_nicole_lewd5 with dissolve
nic "We don't go topless this time of year, [name]."

if not _in_replay and len(wt_ep9_scenes) < 2:
    $ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
    $ renpy.sound.play("sound_effects/season3/bus.mp3", channel="sfx2", loop=False)
    scene ep9_ending18 with dissolve
    $ renpy.pause()
    scene ep9_ending20 with dissolve
    $ renpy.pause()
    scene ep9_ending19 with dissolve
    $ renpy.pause()
    $ renpy.music.stop(channel="sfx1", fadeout=3)
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep9_ending21 with dissolve
    $ renpy.pause()
scene ep9_lily_nicole_lewd7 with fade
ly "This walk is taking ages. Let's smoke over there."
scene ep9_lily_nicole_lewd8 with dissolve
nic "Come on; we're not that far away."
scene ep9_lily_nicole_lewd9 with dissolve
ly "Too late."
scene ep9_lily_nicole_lewd10 with dissolve
nic "Lily, don't be stupid."
scene ep9_lily_nicole_lewd11 with dissolve
ly "It's like 4 a.m. or something; there's no one around. Do you hear that?"
ly "Not even the fucking birds are awake."
scene ep9_lily_nicole_lewd12 with dissolve
nic "Let's go over there, at least."
scene ep9_lily_nicole_lewd13 with dissolve
ly "[name]? Want a hit?"
scene ep9_lily_nicole_lewd14 with dissolve
if ep4_smoked_weed:
    mc "Yeah, ok..."
else:
    mc "Uh... I shouldn't."
scene ep9_lily_nicole_lewd15 with dissolve
if ep4_smoked_weed:
    ly "Don't worry; it's not that strong."
else:
    ly "Don't worry; it's not that strong. Just have a hit."
scene ep9_lily_nicole_lewd16 with dissolve
mc "I doubt I'd feel much of it. I'm still a bit drunk."
scene ep9_lily_nicole_lewd17 with dissolve
nic "You guys had so much beer and liquor at that party. That must have cost a fortune."
scene ep9_lily_nicole_lewd18 with dissolve
mc "We charged the guests, and the DIKs and the HOTs split the rest of the cost."
mc "I don't think it was too bad, but what do I know? I'm not in charge of the money; I only helped plan the party."
scene ep9_lily_nicole_lewd19 with dissolve
ly "Don't sell yourself short. People loved that party. You did amazing."
scene ep9_lily_nicole_lewd20 with dissolve
mc "Thanks. I think it was very fun too."
scene ep9_lily_nicole_lewd21 with dissolve
nic "Totally. Although I gotta say I was a bit surprised..."
mc "About what?"
nic "I thought there would be people hooking up and fucking. I couldn't spot a single couple going at it."
scene ep9_lily_nicole_lewd22 with dissolve
ly "Maybe because you were more focused on doing shots than looking?"
ly "There were a few. I could totally tell."
scene ep9_lily_nicole_lewd23 with dissolve
mc "Really? Who did you see?"
scene ep9_lily_nicole_lewd24 with dissolve
ly "I'm not gonna snitch on people. At least one of them cheated on someone."
scene ep9_lily_nicole_lewd23 with dissolve
mc "Sounds like it was Tommy."
scene ep9_lily_nicole_lewd25 with dissolve
nic "Didn't you hook up with anyone tonight, [name]?"
if affinity == "DIK":
    scene ep9_lily_nicole_lewd26 with dissolve
    mc "What the fuck do you think I'm doing here?"
    scene ep9_lily_nicole_lewd29 with dissolve
    ly "Hahaha!"
    scene ep9_lily_nicole_lewd28 with dissolve
    nic "HAHA! Oh my God!"
    if ep7_lily_lewd:
        scene ep9_lily_nicole_lewd29 with dissolve
        ly "He's so hilarious. I fucking love it!"
        scene ep9_lily_nicole_lewd24 with dissolve
    else:
        scene ep9_lily_nicole_lewd24 with dissolve
else:
    scene ep9_lily_nicole_lewd26 with dissolve
    mc "Well, there's you two. How many more is enough for a night, according to you?"
    scene ep9_lily_nicole_lewd25 with dissolve
    nic "Well, you do know what I do for a living, so take a guess."
    scene ep9_lily_nicole_lewd26 with dissolve
    mc "Oh, right..."
    if envyLikesYou:
        scene ep9_lily_nicole_lewd27 with dissolve
        nic "This is why I like this guy, Lily."
        nic "He never sees me as just what I do for work."
        scene ep9_lily_nicole_lewd24 with dissolve
        ly "Yeah, you got a point there."
    else:
        scene ep9_lily_nicole_lewd24 with dissolve

ly "It would be pretty crazy if we fucked out here, right?"
scene ep9_lily_nicole_lewd30 with dissolve
nic "Out here? Lily, there's a comfortable bed a 10-minute walk that way."
scene ep9_lily_nicole_lewd33 with dissolve
ly "You're the one who wanted to experience college life. College students fuck everywhere."
ly "Tell her, [name]."
scene ep9_lily_nicole_lewd27b with dissolve
mc "Yeah, of course. Everywhere. It doesn't have to be in a bed."
scene ep9_lily_nicole_lewd33 with dissolve
ly "See? College students don't need mattresses with lumbar support or whatever when they wanna get freaky."
scene ep9_lily_nicole_lewd31 with dissolve
nic "Mattresses don't have that; pillows and chairs do."
scene ep9_lily_nicole_lewd33 with dissolve
ly "You're only proving my point by knowing that."
scene ep9_lily_nicole_lewd32 with dissolve
nic "Haha! Shut up! I don't need lumbar support. You know how flexible I am."
scene ep9_lily_nicole_lewd33 with dissolve
ly "If it were up to Nicole, we'd have ankle warmers and reclining chairs at work."
scene ep9_lily_nicole_lewd32 with dissolve
nic "HAHA! Fuck you!"
scene ep9_lily_nicole_lewd34 with dissolve
ly "Hahaha!"
scene ep9_lily_nicole_lewd31 with dissolve
nic "Look! A bed is more comfortable than the table of a gazebo; are you denying that?"
scene ep9_lily_nicole_lewd33 with dissolve
ly "I don't have that frame of reference yet. But if the sex is hot and steamy, it doesn't matter where you have it."
scene ep9_lily_nicole_lewd35 with dissolve
ly "Oh-la-la! What about the bed?"
nic "I look forward to telling you \"I told you so\" when you're pulling splinters out of your asscheeks."
scene ep9_lily_nicole_lewd36 with dissolve
nic "*{i}Smack{/i}*"
scene ep9_lily_nicole_lewd37 with dissolve
nic "Ok. Hop up."
scene ep9_lily_nicole_lewd38 with dissolve
ly "Watch out for splinters, [name]."
scene ep9_lily_nicole_lewd39 with dissolve
mc "It's worth it."
hide screen new_phone_screen
scene anim_ln_bj_ep9 with dissolve
ly "That looks like an ergonomic blowjob, Nic."
ly "Hahaha!"
pause
scene anim_ln_bj2_ep9 with dissolve
nic "*{i}Suck lick{/i}*"
pause
scene ep9_lily_nicole_lewd40 with dissolve
nic "Planning to join, or are you just gonna get high?"
scene ep9_lily_nicole_lewd41 with dissolve
ly "I was just giving you a {b}head{/b} start before I swoop in and steal the show."
scene anim_ln_bj3_ep9 with dissolve
ly "*{i}Suck suck smack{/i}*"
nic "Feels good?"
mc "Yeah..."
pause
scene anim_ln_bj4_ep9 with dissolve
pause

scene ep9_lily_nicole_lewd42 with dissolve
ly "Are you only gonna pull up your skirt? Can't you flash him your tits, or is it too cold?"
scene ep9_lily_nicole_lewd43 with dissolve
nic "Says you! I don't see you taking anything off."
scene ep9_lily_nicole_lewd44 with dissolve
ly "Oh yeah?"
scene ep9_lily_nicole_lewd45 with dissolve
$ renpy.pause()
scene ep9_lily_nicole_lewd46 with dissolve
ly "Your move."
scene ep9_lily_nicole_lewd47 with dissolve
nic "Note to self: Never challenge Lily."
nic "It's chilly..."
scene ep9_lily_nicole_lewd48 with dissolve
ly "Yeah, but you couldn't tell from the size of his cock."
scene ep9_lily_nicole_lewd49 with dissolve
nic "Oh, fuck!"
scene anim_ln_miss1_ep9 with dissolve
ly "Fuck her, [name]. Fuck her good."
pause
scene anim_ln_miss2_ep9 with dissolve
nic "*{i}Moans{/i}*"
mc "This feels..."
ly "Good? Weird? What?"
pause

scene bg anim_ln_hit_ep9 movie with dissolve
mc "Whoa..."
scene ep9_lily_nicole_lewd62 with dissolve
ly "Did it hit?"
scene ep9_lily_nicole_lewd63 with dissolve
nic "Looks like it did. Take it slow, [name]."
scene anim_ln_miss2_ep9 with dissolve
pause

$ tmpInt = 0
label ep9_lily_nicole_lewd_loop_label:
menu:
    "Fuck Lily":
        menu:
            "Missionary":
                $ tmpInt += 1
                scene anim_ln_miss3_ep9 with dissolve
                ly "*{i}Lick lick{/i}*"
                nic "Hngn... Yeah, get in there."
                pause
                scene anim_ln_miss4_ep9 with dissolve
                ly "*{i}Moans{/i}* Fuck me, [name]."
                pause

                scene ep9_lily_nicole_lewd64 with dissolve
                nic "*{i}Moans{/i}* Damn... Lily... Your tongue."
                scene ep9_lily_nicole_lewd65 with dissolve
                ly "*{i}Lick lick{/i}* Yeah? I bet you like that."

                jump ep9_lily_nicole_lewd_loop_label
            "Cowgirl":
                $ tmpInt += 1
                scene anim_ln_ride1_ep9 with dissolve
                ly "How about that table, Nic?"
                pause
                scene ep9_lily_nicole_lewd66 with dissolve
                nic "*{i}Moans{/i}* Ahhh..."
                scene ep9_lily_nicole_lewd67 with dissolve
                ly "I knew you'd like it."
                scene ep9_lily_nicole_lewd68 with dissolve
                nic "It's way too good."
                scene anim_ln_ride2_ep9 with dissolve
                ly "I know exactly what you mean. Hngn..."
                pause
                scene anim_ln_ride3_ep9 with dissolve
                pause
                jump ep9_lily_nicole_lewd_loop_label
            "Doggystyle":
                $ tmpInt += 1
                scene anim_ln_doggy_ep9 with dissolve
                mc "I'm feeling...dizzy."
                nic "Take a deep breath."
                pause
                scene ep9_lily_nicole_lewd69 with dissolve
                nic "Fuck her, [name]. I got you. Just focus on thrusting your cock into her."
                scene ep9_lily_nicole_lewd70 with dissolve
                ly "*{i}Moans{/i}* Don't stop, [name]. You won't pass out, trust me."
                scene anim_ln_doggy2_ep9 with dissolve
                pause
                jump ep9_lily_nicole_lewd_loop_label
    "Fuck Nicole":
        menu:
            "Missionary":
                $ tmpInt += 1
                scene anim_ln_miss1_ep9 with dissolve
                pause
                scene ep9_lily_nicole_lewd71 with dissolve
                nic "*{i}Moans{/i}*"
                scene anim_ln_miss2_ep9 with dissolve
                ly "That looks so good. He's making you feel all of it, isn't he?"
                nic "Mhm..."
                pause
                jump ep9_lily_nicole_lewd_loop_label
            "Sideways":
                $ tmpInt += 1
                scene anim_ln_side1_ep9 with dissolve
                ly "Fuck her, [name]. Go deep inside her."
                pause
                scene ep9_lily_nicole_lewd72 with dissolve
                ly "*{i}Moans{/i}*"
                nic "Enjoying the show, Lily?"
                scene ep9_lily_nicole_lewd73 with dissolve
                ly "Yup. I don't need the dick inside me to enjoy this."
                scene anim_ln_side2_ep9 with dissolve
                ly "But seriously... Is it my turn soon or...?"
                nic "*{i}Moans{/i}* Not yet..."
                pause
                jump ep9_lily_nicole_lewd_loop_label
            "Doggystyle":
                $ tmpInt += 1
                scene anim_ln_doggy3_ep9 with dissolve
                pause
                scene ep9_lily_nicole_lewd74 with dissolve
                ly "Mmm... *{i}Smack{/i}*"
                scene anim_ln_doggy4_ep9 with dissolve
                nic "[name]... Deeper... Please?"
                pause
                jump ep9_lily_nicole_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna cum..."
        menu:
            "Lily's face":
                scene anim_ln_bj5_ep9 with dissolve
                ly "Do it, [name]. Cum all over my pretty face."
                pause
                scene ep9_lily_nicole_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd50 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd50 at vpunch, cum2
                $ renpy.pause()
                scene ep9_lily_nicole_lewd51 with dissolve
                nic "No way! Did she get all of it?"
                scene ep9_lily_nicole_lewd51b with dissolve
                ly "*{i}Smack{/i}* Come, share it."
                nic "*{i}Smack{/i}*"
                scene ep9_lily_nicole_lewd51c with dissolve
                ly "Hey, you did great."
                scene ep9_lily_nicole_lewd51d with dissolve
                nic "Gee! Thanks! Pff!"
                nic "I'm more impressed with you. His dick isn't bleeding after getting blown with those fangs."
                scene ep9_lily_nicole_lewd51c with dissolve
                ly "You underestimate my head game, Nic."
            "Nicole's ass":
                scene anim_ln_bj5_ep9 with dissolve
                nic "I want it, [name]. Cum all over my ass!"
                scene ep9_lily_nicole_lewd52 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd52 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd52 at vpunch, cum2
                $ renpy.pause()
                scene ep9_lily_nicole_lewd53 with dissolve
                ly "How's your back, Nic?"
                nic "Obviously, great; he chose to cum all over it."
                ly "Haha!"
            "Lily's tits":
                scene anim_ln_cum_ep9 with dissolve
                ly "Cum on my tits, [name]."
                nic "Yeah, do it, [name]. Cover her chest with it."
                pause
                scene ep9_lily_nicole_lewd54 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd54 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd54 at vpunch, cum2
                $ renpy.pause()
                scene ep9_lily_nicole_lewd55 with dissolve
                ly "There you go..."
                scene ep9_lily_nicole_lewd56 with dissolve
                nic "*{i}Lick lick{/i}* Mmm..."
            "Creampie Nicole":
                scene anim_ln_doggy4_ep9 with dissolve
                nic "Cum inside of me, [name]."
                ly "*{i}Smack{/i}* Mmpff... If you're not gonna share that with me, you can fill her up, and I'll lick whatever drips out of her pussy."
                ly "Cum, [name]!"
                scene ep9_lily_nicole_lewd57 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd57 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd57 at vpunch, cum1
                $ renpy.pause()
                scene ep9_lily_nicole_lewd58 with dissolve
                $ renpy.pause()
                scene ep9_lily_nicole_lewd59 with dissolve
                ly "*{i}Lick lick{/i}*"
            "Creampie Lily":
                scene anim_ln_doggy2_ep9 with dissolve
                nic "Look at her ass. She's practically begging for it."
                nic "Shoot your load inside of her."
                ly "Cum, [name]!"
                scene ep9_lily_nicole_lewd60 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd60 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_lily_nicole_lewd60 at vpunch, cum1
                $ renpy.pause()
                scene ep9_lily_nicole_lewd61 with dissolve
                nic "That is so hot!"
scene ep9_lily_nicole_lewd75 with dissolve
nic "Damn... *{i}Phew{/i}* So, this is the college experience."
scene ep9_lily_nicole_lewd76 with dissolve
ly "The table does feel like a futon, doesn't it?"
scene ep9_lily_nicole_lewd75 with dissolve
nic "It wasn't that bad. Once he started fucking me, I let it all go."
nic "Fuck, that was good..."
scene ep9_lily_nicole_lewd76 with dissolve
ly "What a way to end the night, eh? Right, [name]?"
scene ep9_lily_nicole_lewd77 with dissolve
ly "[name]?"
scene ep9_lily_nicole_lewd78 with dissolve
mc "*{i}Snores{/i}*"
ly "Ok, we have to do something about that."
scene ep9_lily_nicole_lewd79 with dissolve
nic "[name]? [name]? Wake up."
nic "Haha! Imagine if we left the poor thing here like this."
scene ep9_lily_nicole_lewd80 with dissolve
ly "That would be so cruel."
scene ep9_lily_nicole_lewd79 with dissolve
nic "Hey, don't sleep. We're not home yet."
scene ep9_lily_nicole_lewd80 with dissolve
ly "My ass is freezing, and I wanna sleep."
scene ep9_lily_nicole_lewd79 with dissolve
nic "The faster we dress him, the faster we can get back home."

$ renpy.end_replay()
$ persistent.ep9_lewd_ln = True
$ calcScenes()
$ new_bio("Lily", "I smoked pot and fucked Lily and Nicole after the Halloween party.")
$ new_bio("Envy", "I smoked pot and fucked Lily and Nicole after the Halloween party.")
$ mphone_stats_add_girl_s3("envy","You had a threesome with Nicole and Lily after the Halloween party in episode 9.")
$ mphone_stats_add_girl_s3("lily","You had a threesome with Nicole and Lily after the Halloween party in episode 9.")
stop music fadeout 3
if not persistent.ep9_card20:
    $ persistent.ep9_card20 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    
if "Lily" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Lily")

if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          "Josy & Maya" if branchMayaJosy and "Josy" not in wt_ep9_scenes:
            if "Josy" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Josy")
            jump ep9_jm_committing_label
          "Jill" if branchJill and "Jill" not in wt_ep9_scenes:
            if "Jill" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Jill")
            jump ep9_jill_lewd2_label
          "Sage" if branchSage and "Sage" not in wt_ep9_scenes:
                if "Sage" not in wt_ep9_scenes:
                   $wt_ep9_scenes.append("Sage")
                jump ep9_sage_hunt_label
          "Isabella" if branchIsabella and "Bella" not in wt_ep9_scenes:
                if "Bella" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Bella")
                jump ep9_bella_lewd2_label
          "Quinn" if branchAlone and ep8_quinn_lewd and "Quinn" not in wt_ep9_scenes:
                
                $ep9_quinn_lewd=True
                
                if "Quinn" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Quinn")
                jump ep9_quinn_lewd_label
          "Melanie & Sarah" if branchAlone and (ep6_sarah_lewd or ep8_sarah_lewd or ep8_melanie_lewd or ep4_fuckedMelanie) and "Sarah" not in wt_ep9_scenes:
                
                $ep9_sarah_melanie_lewd=True
                if "Sarah" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Sarah")
                jump ep9_sm_lewd_label
          "Continue the game":
              pass
              
if wt_ep9_branch_numbers != 1:
    "End the night with?"
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if envyLikesYou:
                            $mod_choices[6]="[m_c1](Progress Nicole path)"
    
    menu:
         "Josy & Maya" if "Josy" in wt_ep9_scenes:
            $wt_ep9_end_pick="Maya"
         "Jill"  if "Jill" in wt_ep9_scenes:
            $wt_ep9_end_pick="Jill"
         "Sage"  if "Sage" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sage"
         "Isabella" if "Bella" in wt_ep9_scenes:
            $wt_ep9_end_pick="Bella"
         "Quinn" if "Quinn" in wt_ep9_scenes:
            $wt_ep9_end_pick="Quinn"
         "Lily & Nicole [mod_choices[6]]" if "Lily" in wt_ep9_scenes:
            $wt_ep9_end_pick="Lily"
         "Melanie & Sarah" if "Sarah" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sarah"
         "Tara & Tiffani & Gina":
            $ep9_tiffani_gina_tara=True
            $wt_ep9_end_pick="Other"
    

jump ep9_ending_label

label ep9_ending_nicole_lily_label:
scene ep9_ending_nicole_lily1 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily2 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily3 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily4 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily5 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily6 with dissolve
$ renpy.pause()
scene ep9_ending_nicole_lily7 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Better for Nicole path)","(+Maya)","(-DIK)","(+DIK)","(Better for Lily path)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Spoon Nicole" if envyLikesYou:
        $ ep9_spoon_nicole = True
        scene ep9_ending_nicole_lily10 with dissolve
        $ renpy.pause()
        if affinity == "CHICK":
            scene ep9_ending_nicole_lily11 with dissolve
            mc "*{i}Smack{/i}*"
            scene ep9_ending_nicole_lily12 with dissolve
            nic "Hm? Hey, you..."
        else:
            scene ep9_ending_nicole_lily24 with dissolve
            mc "Damn..."
            scene ep9_ending_nicole_lily25 with dissolve
            nic "Um? Hey, you..."
        scene ep9_ending_nicole_lily13 with dissolve
        mc "It's morning..."
        scene ep9_ending_nicole_lily14 with dissolve
        nic "Morning? No... I don't even wanna know what it is. Haha."
        scene ep9_ending_nicole_lily15 with dissolve
        nic "I had a good time with you last night."
        mc "It was the best."
        nic "I feel we should do something together sometime."
        scene ep9_ending_nicole_lily16 with dissolve
        mc "All three of us?"
        scene ep9_ending_nicole_lily17 with dissolve
        $ renpy.pause()
        scene ep9_ending_nicole_lily18 with dissolve
        nic "No. I was talking about you and me. Are you interested?"
        scene ep9_ending_nicole_lily19 with dissolve
        mc "Well... Why do you think I'm spooning you and not her?"
        nic "Haha..."
        scene ep9_ending_nicole_lily20 with dissolve
        nic "You make me laugh. I like laughing."
        scene ep9_ending_nicole_lily21 with dissolve
        nic "*{i}Smack{/i}*"
        scene ep9_ending_nicole_lily22 with dissolve
        nic "[name]... Who are you?"
        nic "I really wanna know."
        scene ep9_ending_nicole_lily23 with dissolve
        $ renpy.pause()
        $ new_bio("Envy", "I spooned Nicole instead of Lily. Nicole wants to know more about me.")
    "Spoon Lily" if ep7_lily_lewd:
        $ ep9_spoon_lily = True
        scene ep9_ending_nicole_lily26 with dissolve
        $ renpy.pause()
        scene ep9_ending_nicole_lily27 with dissolve
        ly "*{i}Slow deep breath{/i}*"
        scene ep9_ending_nicole_lily28 with dissolve
        $ renpy.pause()
        scene ep9_ending_nicole_lily29 with dissolve
        ly "It looks like I got you hooked. Took me a while."
        scene ep9_ending_nicole_lily30 with dissolve
        mc "Haha... I don't know."
        scene ep9_ending_nicole_lily29 with dissolve
        ly "I think I did."
        scene ep9_ending_nicole_lily30 with dissolve
        mc "Well... I am spooning you right now."
        scene ep9_ending_nicole_lily31 with dissolve
        ly "When I said we should roll together..."
        ly "Just so you know... {b}This{/b} is not what I'm looking for."
        scene ep9_ending_nicole_lily32 with dissolve
        ly "Don't fall in love with me, [name]."
        scene ep9_ending_nicole_lily33 with dissolve
        mc "Huh? Why is that? I mean, I'm not, but...why?"
        scene ep9_ending_nicole_lily32 with dissolve
        ly "I'm just telling you. Don't fall in love with me."
        scene ep9_ending_nicole_lily33 with dissolve
        mc "Ok..."
        scene ep9_ending_nicole_lily34 with dissolve
        $ renpy.pause()
        $ new_bio("Lily", "I spooned Lily instead of Nicole. Lily doesn't want me to fall in love with her.")
        if not persistent.ep9_card19:
            $ persistent.ep9_card19 = True
            $ persistent.rew_2d_unlocked += 1
            $ persistent.chat_new_rewards = True
            $ calcRenders()
            show screen srmsg
            $ renpy.pause(3)
    "Don't spoon":
        scene ep9_ending_nicole_lily8 with dissolve
        mc "(What a night...)"
        scene ep9_ending_nicole_lily9 with dissolve
        $ renpy.pause()

jump ep9_ending2_label

label ep9_quinn_lewd_label:
if _in_replay:
    hide screen new_phone_screen
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
scene ep9_quinn_lewd1 with fade
play music "music/ep9/licensed_music/track127.mp3"
queue music (["music/ep9/licensed_music/track130.mp3","music/ep9/licensed_music/track133.mp3","music/ep9/licensed_music/track127.mp3"])
mc "It's a shame I couldn't vote for you in the costume competition."
scene ep9_quinn_lewd2 with dissolve
qu "What are you doing? I already brought you back home; there's no need for this."
scene ep9_quinn_lewd3 with dissolve
mc "You had the sexiest costume tonight; that's all I'm saying."
scene ep9_quinn_lewd4 with dissolve
qu "Oh, please. You've been strutting around showing off the goods all night."
scene ep9_quinn_lewd5 with dissolve
mc "So, you finally admit it's sexy."
scene ep9_quinn_lewd6 with dissolve
qu "You knew very well why you put that costume on in the first place."
qu "You just wanted to show off your abs and arms, and that costume was perfect for it."
scene ep9_quinn_lewd7 with dissolve
mc "Uh-huh? What about you? Putting on a robe, walking around, and teasing with your amazing ass."
scene ep9_quinn_lewd8 with dissolve
qu "What? This little thing?"
scene ep9_quinn_lewd9 with dissolve
mc "Yeah..."
mc "I'd say you're the one who knew what you were doing with that outfit."
scene ep9_quinn_lewd10 with dissolve
qu "It got me what I wanted, didn't it?"
scene ep9_quinn_lewd11 with dissolve
mc "Well..."
scene ep9_quinn_lewd12 with dissolve
qu "Fuck you! You're not what I meant."
scene ep9_quinn_lewd13 with dissolve
mc "Are you sure about that?"
scene ep9_quinn_lewd14 with dissolve
qu "Eww. Is that supposed to be sexy? If I had a boner, it wouldn't be erect; it would be inside of me right now."
scene ep9_quinn_lewd15 with dissolve
mc "You can have my boner inside of you right now if you want."
scene ep9_quinn_lewd16 with dissolve
qu "Remove that fuckboy costume already."
hide screen new_phone_screen
scene ep9_quinn_lewd17 with dissolve
qu "So much fake metal crap you put on for tonight."
mc "I know; it was like a workout session getting it on."
qu "...and off."
scene ep9_quinn_lewd18 with dissolve
mc "You're keeping your costume on, right?"
scene ep9_quinn_lewd19 with dissolve
qu "You have no idea what you're in for."
scene ep9_quinn_lewd21 with dissolve
qu "Can you handle me wearing this?"
scene ep9_quinn_lewd20 with dissolve
mc "I'll show you."
label ep9_quinn_lewd_loop_label:
menu:
    "Spank her ass":
        scene bg anim_quinn_spank_ep9 movie with dissolve
        qu "Mmm..."
        pause
        scene bg anim_quinn_spank2_ep9 movie with dissolve
        qu "Damn, [mc_quinn]."
        mc "What?"
        qu "You're slapping my ass like it owes you money."
        mc "Haha! Do you want me to stop?"
        qu "Nah, I feel empowered knowing you can't quit it."
        pause
        scene bg anim_quinn_spank3_ep9 movie with dissolve
        mc "I can quit... But just a few more slaps before I do."
        qu "Haha!"
        pause
        jump ep9_quinn_lewd_loop_label
    "Finger her pussy":
        scene ep9_quinn_lewd20c with dissolve
        mc "Show me what you got here..."
        qu "Feel for yourself..."
        scene ep9_quinn_lewd20b with dissolve
        qu "*{i}Moans{/i}*"
        scene anim_quinn_finger_ep9 with dissolve
        mc "You're so tight around my finger..."
        qu "Imagine that feeling around your cock."
        mc "Oh, I am."
        pause
        scene anim_quinn_finger2_ep9 with dissolve
        qu "*{i}Moans{/i}* Give it to me, [mc_quinn]..."
        pause
        scene ep9_quinn_lewd20c2 with dissolve
        mc "Mmm... You're all nice and wet..."
        jump ep9_quinn_lewd_loop_label
    "Finger her ass":
        scene ep9_quinn_lewd20d with dissolve
        qu "Where are you going with those fingers, [mc_quinn]?"
        mc "Oh, you'll see..."
        scene ep9_quinn_lewd20e with dissolve
        qu "*{i}Moans{/i}* I knew it..."
        scene anim_quinn_finger_anal_ep9 with dissolve
        qu "Go slow..."
        mc "I will. I wanna enjoy the view for a long time."
        pause
        scene anim_quinn_finger2_ep9 with dissolve
        qu "I bet you're enjoying it. *{i}Moan{/i}*"
        mc "I hear your moaning. We're both enjoying it."
        pause
        jump ep9_quinn_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep9_quinn_lewd22 with dissolve
qu "Hey... You're taking control... I'm not sure I like that."
qu "It's the succubus who should dominate."
scene ep9_quinn_lewd23 with dissolve
mc "Can't we take turns?"
qu "It's a special night for you, so sure..."
qu "Question is... Do you want to cum when you're dominant or when I'm in control?"
$ tmpBool3 = False
$ tmpStr = "Continue"
menu:
    "Cum when she's in control":
        $ tmpBool3 = True
        mc "I want you to drain my balls when I'm close."
        scene ep9_quinn_lewd23 with dissolve
        qu "Then I'll let you have your fun, to begin with."
        scene ep9_quinn_lewd24 with dissolve
        mc "Awesome... I've always wanted to tame a succubus."
        scene ep9_quinn_lewd25 with dissolve
        qu "Bitch, you can't tame me."
        scene ep9_quinn_lewd26 with dissolve
        mc "Wanna bet?"
        scene ep9_quinn_lewd27 with dissolve
        $ renpy.pause()
        scene ep9_quinn_lewd28 with dissolve
        mc "Bend over."
        scene ep9_quinn_lewd29 with dissolve
        qu "A mortal warrior wants to fuck the succubus?"
        qu "Show me what you got."

        scene ep9_quinn_lewd30 with dissolve
        menu:
            "Vaginal":
                scene ep9_quinn_lewd30b with dissolve
                qu "*{i}Moans{/i}*"
                scene ep9_quinn_lewd30b2 with dissolve
                $ renpy.pause()
                jump ep9_quinn_lewd_vag_label
            "Anal":
                scene ep9_quinn_lewd30c with dissolve
                qu "Hngn..."
                scene ep9_quinn_lewd30c2 with dissolve
                $ renpy.pause()
                jump ep9_quinn_lewd_anal_label
        label ep9_quinn_lewd_loop2_label:
        menu:
            "Prone bone (Anal)":
                scene ep9_quinn_lewd30c with dissolve
                qu "Hngn..."
                scene ep9_quinn_lewd30c2 with dissolve
                $ renpy.pause()
                label ep9_quinn_lewd_anal_label:
                scene anim_quinn_doggy_anal_ep9 with dissolve
                qu "Yes! Fuck my ass, [mc_quinn]!"
                mc "Shut your mouth."
                pause
                scene anim_quinn_doggy_anal2_ep9 with dissolve
                qu "Hngn..."
                qu "Fuck..."
                mc "Yeah, you love this, don't you?"
                qu "I can barely feel anything."
                pause
                mc "Then I'll go all the way in."
                qu "Wait-"
                scene anim_quinn_doggy_anal3_ep9 with vpunch
                qu "Ahh!! FUCK!"
                mc "Yeah, that's more like it. Feel the entire length of it."
                pause
                scene ep9_quinn_lewd30d with dissolve
                qu "You're fucking crazy..."
                jump ep9_quinn_lewd_loop2_label
            "Prone bone (Vaginal)":
                scene ep9_quinn_lewd30b with dissolve
                qu "*{i}Moans{/i}*"
                scene ep9_quinn_lewd30b2 with dissolve
                $ renpy.pause()
                label ep9_quinn_lewd_vag_label:
                scene anim_quinn_doggy_ep9 with dissolve
                mc "Take it, [quinn]."
                qu "Yes... Yes! Fuck me, [mc_quinn]!"
                pause
                scene anim_quinn_doggy2_ep9 with dissolve
                qu "*{i}Moans{/i}* Are you enjoying my tight demonic holes, [mc_quinn]?"
                mc "You're squeezing it extra, aren't you?"
                qu "I'm in control, and you know it."
                mc "Keep telling yourself that, but you know you aren't."
                pause
                jump ep9_quinn_lewd_loop2_label
            "Missionary (Anal)":
                scene ep9_quinn_lewd30e with dissolve
                mc "Come here. I'm not done with your ass."
                scene anim_quinn_miss_anal_ep9 with dissolve
                qu "You won't last long like this. My ass feels too good for you. Admit it!"
                pause
                scene anim_quinn_miss_anal2_ep9 with dissolve
                mc "I've got great endurance tonight. You'll wish I was done with you, but I will keep going."
                qu "*{i}Moans{/i}*"
                pause
                scene anim_quinn_miss_anal3_ep9 with dissolve
                qu "Fuck...[mc_quinn]... I can keep at this all night. Hngn..."
                qu "But for you, it'll be over as soon as you look into my eyes."
                qu "Focus on them and fuck me. I swear you'll cum in an instant."
                mc "(Fuck... She's right... Must not look...)"
                qu "You're avoiding eye contact... Haha... I knew it. I'm in control, bitch."
                pause
                jump ep9_quinn_lewd_loop2_label
            "Missionary (Vaginal)":
                scene ep9_quinn_lewd30f with hpunch
                mc "Don't try to get away from me..."
                scene anim_quinn_miss_ep9 with dissolve
                qu "Oh, I wouldn't want to get away from you."
                qu "I'm gonna let you run out of steam before I finish you."
                pause
                scene anim_quinn_miss2_ep9 with hpunch
                qu "*{i}Moans{/i}* Hngn..."
                mc "Are you sure about that? It looks like I will finish you first."
                qu "Fat chance!"
                pause
                scene anim_quinn_miss3_ep9 with dissolve
                mc "You can't fool me. Your words say one thing, but your face is begging for more."
                qu "My pleasure comes from watching you pound away, thinking you have a chance of making me cum."
                pause
                jump ep9_quinn_lewd_loop2_label
            "Standing (Anal)":
                scene ep9_quinn_lewd30g with dissolve
                qu "Fuck! *{i}Moans{/i}*"
                mc "You love it when I enter your ass, don't you?"
                scene anim_quinn_stand_anal_ep9 with dissolve
                qu "No."
                mc "Admit it."
                qu "Fuck you."
                pause
                scene anim_quinn_stand_anal2_ep9 with dissolve
                mc "Fuck, you're so tight."
                qu "You're gonna cum, aren't you?"
                pause
                jump ep9_quinn_lewd_loop2_label
            "Lift her (Vaginal)":
                scene ep9_quinn_lewd30g2 with vpunch
                qu "Whoa!"
                mc "You look scared."
                scene ep9_quinn_lewd30i with dissolve
                qu "I didn't think you were strong enough to lift me, that's all."
                mc "Don't worry; you don't weigh that much."
                scene anim_quinn_stand_ep9 with dissolve
                qu "*{i}Moans{/i}* You're going pretty slow... Is this your idea of dominating someone?"
                mc "I thought about it. You seem to like it slow."
                mc "Fucking you fast feels good, but I think you enjoy this way more."
                pause
                scene anim_quinn_stand2_ep9 with vpunch
                qu "I'm- Hngn... Not enjoying it. Fast is way better."
                qu "Save this slow shit for some bitch who can't take it and wants romantic sex."
                pause
                scene ep9_quinn_lewd30i2 with dissolve
                qu "*{i}Moans{/i}*"
                scene anim_quinn_stand3_ep9 with dissolve
                mc "This is a good way to dominate you. You'd never fuck me slowly unless I were in control."
                qu "Uh-huh..."
                pause
                jump ep9_quinn_lewd_loop2_label
            "[tmpStr]":
                if not tmpBool3:
                    menu:
                        "In mouth":
                            scene anim_quinn_bj_ep9 with dissolve
                            qu "*{i}Glug glug suck{/i}*"
                            mc "Choke on it, [quinn]."
                            mc "I'm close... I'm gonna fill your mouth with it."
                            pause
                            scene ep9_quinn_lewd31 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd31 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd31 at vpunch, cum1
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd32 with dissolve
                            qu "*{i}Pants{/i}* Wow... I didn't think you had it in you."
                            scene ep9_quinn_lewd32b with dissolve
                            qu "Mmm... *{i}Gulp{/i}*"
                            scene ep9_quinn_lewd32c with dissolve
                            mc "Now, that's a hot sight..."
                        "Facial":
                            scene anim_quinn_bj_ep9 with dissolve
                            qu "*{i}Glug glug suck{/i}*"
                            mc "Choke on it, [quinn]."
                            mc "I'm close... I'm gonna spray your mouth with all of it."
                            pause
                            scene ep9_quinn_lewd33 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd33 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd33 at vpunch, cum2
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd34 with dissolve
                            mc "What a pretty sight..."
                            scene ep9_quinn_lewd34b with dissolve
                            qu "*{i}Pants{/i}* Wow... I didn't think you had it in you."
                        "On ass (Anal)":
                            scene anim_quinn_doggy_anal_ep9 with dissolve
                            mc "I'm close... I'm gonna spray your ass with all of it."
                            qu "Do it, [mc_quinn]..."
                            pause
                            scene ep9_quinn_lewd35 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd35 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd35 at vpunch, cum2
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd36 with dissolve
                            qu "*{i}Phew{/i}* That's hot..."
                        "On back (Vaginal)":
                            scene anim_quinn_doggy_ep9 with dissolve
                            mc "I'm close... I'm gonna spray your back with all of it."
                            qu "Do it, [mc_quinn]..."
                            pause
                            scene ep9_quinn_lewd37 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd37 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd37 at vpunch, cum2
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd38 with dissolve
                            qu "*{i}Phew{/i}* That's hot..."
                        "Creampie (Anal)":
                            scene anim_quinn_miss_anal_ep9 with dissolve
                            mc "I'm close... I'm gonna fill your ass with cum."
                            qu "Do it, pussy! Fill me!"
                            pause
                            scene ep9_quinn_lewd39 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd39 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd39 at vpunch, cum1
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd40 with dissolve
                            qu "Oh, fuck! That's hot..."
                        "Creampie (Vaginal)":
                            scene anim_quinn_miss_ep9 with dissolve
                            mc "I'm close... I'm gonna fill your pussy with cum."
                            qu "Do it, [mc_quinn]! Fill me!"
                            pause
                            scene ep9_quinn_lewd41 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd41 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd41 at vpunch, cum1
                            mc "Ahhh... Fuck!!!"
                            scene ep9_quinn_lewd42 with dissolve
                            qu "Completely drained...aren't you?"
                    scene ep9_quinn_lewd55 with dissolve
                    mc "Did I tame you?"
                    scene ep9_quinn_lewd57 with vpunch
                    mc "OUCH! FUCK!"
                    scene ep9_quinn_lewd58 with dissolve
                    qu "Hahaha! Such a pussy!"
                    qu "You cannot tame me. You didn't even make me cum."
                    scene ep9_quinn_lewd58b with dissolve
                    mc "Stop lying; I know you came. You tried to hide it, but I could tell."
                    scene ep9_quinn_lewd58 with dissolve
                    qu "Pff. I went easy on you this time. Next time, I'll eat you alive."
                else:
                    $ tmpStr = "Cum"
                    qu "*{i}Yawns{/i}* Are you done yet?"
                    mc "You're getting tired?"
                    qu "More like bored."
                    scene ep9_quinn_lewd58c with vpunch
                    mc "*{i}Gulp{/i}*"
                    qu "Ok, bitch. You're done trying to prove something. It's my turn... I'm gonna eat you alive."
                    qu "You'll see what you get when you fuck with a succubus."
                    jump ep9_quinn_lewd_loop3_label
    "Cum as dominant":
        $ tmpBool3 = False
        mc "I wanna fuck you into submission."
        qu "Is that what you want?"
        scene ep9_quinn_lewd24 with dissolve
        mc "Fuck yes."
        scene ep9_quinn_lewd25 with dissolve
        qu "You can try... But your cock will be my toy before you get the chance."
        scene ep9_quinn_lewd24 with dissolve
        mc "Is that-"
        scene ep9_quinn_lewd25b with vpunch
        mc "*{i}Gulp{/i}*"
        qu "Shut up, mortal! You'll see what you get when you fuck with a succubus."
        label ep9_quinn_lewd_loop3_label:
        menu:
            "Cowgirl (Anal)":
                scene ep9_quinn_lewd25c with dissolve
                qu "Get in there..."
                scene anim_quinn_ride_anal_ep9 with dissolve
                mc "Oh, fuck..."
                qu "Yeah, enter my ass, [mc_quinn]."
                pause
                scene anim_quinn_ride2_anal_ep9 with dissolve
                qu "Feel all of it."
                qu "You're such a fuckboy. Walking around all night showing skin."
                pause
                scene anim_quinn_ride3_anal_ep9 with dissolve
                qu "Trying to entice girls with that skimpy outfit."
                mc "I think we both had the same idea."
                qu "Yeah, right."
                pause
                jump ep9_quinn_lewd_loop3_label
            "Cowgirl (Vaginal)":
                scene ep9_quinn_lewd25d with dissolve
                qu "Now you're mine!"
                scene anim_quinn_ride_ep9 with dissolve
                mc "You want me to be yours, huh?"
                qu "You wish. All I want of you is your seed."
                qu "You're gonna fill up my succubus pussy, [mc_quinn]."
                pause
                scene anim_quinn_ride2_ep9 with dissolve
                mc "That's hot."
                qu "*{i}Moans{/i}* Yes... Just lie there while I pump your dick."
                pause
                scene anim_quinn_ride3_ep9 with dissolve
                qu "Feel how my ass slaps against you as I ride your cock. Take it, bitch."
                pause
                jump ep9_quinn_lewd_loop3_label
            "From behind (Anal)":
                scene ep9_quinn_lewd25e with dissolve
                qu "Enter me, but don't move."
                scene ep9_quinn_lewd25f with dissolve
                mc "How do you expect me to stay still when you're this inviting?"
                qu "You'll find a way to stay still, or I'll use my claws on your cock."
                scene anim_quinn_behind_anal_ep9 with dissolve
                qu "I bet you didn't think you'd be submissive from on top, did you?"
                qu "That's right... *{i}Moans{/i}* I fucking own you and your cock."
                pause
                scene anim_quinn_behind_anal2_ep9 with dissolve
                mc "Shit... It's so good."
                qu "I know. You can't resist me."
                pause
                jump ep9_quinn_lewd_loop3_label
            "From behind (Vaginal)":
                scene ep9_quinn_lewd25g with dissolve
                qu "Right there. Don't move!"
                scene anim_quinn_behind_ep9 with dissolve
                qu "*{i}Moans{/i}*"
                pause
                scene anim_quinn_behind2_ep9 with dissolve
                mc "That's looking real good, [quinn]..."
                qu "Enjoy that view while you're lucky enough to see it."
                pause
                jump ep9_quinn_lewd_loop3_label
            "Standing (Anal)":
                scene ep9_quinn_lewd25h with dissolve
                qu "Don't you dare move your hips."
                mc "Why? It feels better if I do."
                scene anim_quinn_stand_sub_anal_ep9 with dissolve
                qu "Because I said so. Watch me bounce all over your cock."
                qu "Can you feel how my asshole envelops you?"
                pause
                scene anim_quinn_stand_sub_anal2_ep9 with hpunch
                qu "*{i}Moans{/i}* Fuck..."
                mc "Keep going."
                qu "Don't tell me what to do. We're done when I say we're done."
                pause
                jump ep9_quinn_lewd_loop3_label
            "Missionary (Vaginal)":
                scene ep9_quinn_lewd25i with dissolve
                qu "Come over here..."
                scene ep9_quinn_lewd25j with dissolve
                mc "Is it my turn?"
                scene anim_quinn_miss_sub_ep9 with dissolve
                qu "No. You follow my pace. Not too slow now."
                pause
                scene anim_quinn_miss_sub2_ep9 with dissolve
                qu "Yes... Fuck me, [mc_quinn]."
                qu "Right there..."
                pause
                jump ep9_quinn_lewd_loop3_label
            "[tmpStr]":
                if tmpBool3:
                    menu:
                        "In mouth":
                            scene anim_quinn_bj_sub_ep9 with dissolve
                            qu "*{i}Suck suck{/i}* It's time, [mc_quinn]."
                            qu "*{i}Suck glug{/i}* Cum in my mouth. Give me what's mine."
                            pause
                            scene ep9_quinn_lewd43 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd43 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd43 at vpunch, cum1
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd44 with dissolve
                            $ renpy.pause()
                            scene ep9_quinn_lewd44b with dissolve
                            qu "Mmm... *{i}Gulp{/i}*"
                            scene ep9_quinn_lewd44c with dissolve
                            qu "Ahh..."
                        "Facial":
                            scene anim_quinn_bj_sub_ep9 with dissolve
                            qu "*{i}Suck suck{/i}* It's time, [mc_quinn]."
                            qu "*{i}Suck glug{/i}* Spray me! Give me what's mine."
                            pause
                            scene ep9_quinn_lewd45 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd45 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd45 at vpunch, cum2
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd46 with dissolve
                            qu "There you go... You did good..."
                        "Creampie (Anal)":
                            scene anim_quinn_ride_anal_ep9 with dissolve
                            qu "It's time, [mc_quinn]."
                            qu "Fill my ass with your cum. Give me what's mine."
                            pause
                            scene ep9_quinn_lewd47 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd47 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd47 at vpunch, cum1
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd48 with dissolve
                            qu "Mmm... *{i}Moans{/i}* I can feel the warmth of it."
                        "Creampie (Vaginal)":
                            scene anim_quinn_ride_ep9 with dissolve
                            qu "It's time, [mc_quinn]."
                            qu "Fill me with your cum. Give me what's mine."
                            pause
                            scene ep9_quinn_lewd49 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd49 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd49 at vpunch, cum1
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd50 with dissolve
                            qu "Mmm... *{i}Moans{/i}* I can feel the warmth of it."
                        "On ass (Anal)":
                            scene anim_quinn_behind_anal_ep9 with dissolve
                            qu "Here's your chance, [mc_quinn]."
                            qu "Spray my ass with your cum! Give me what's mine."
                            pause
                            scene ep9_quinn_lewd51 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd51 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd51 at vpunch, cum2
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd52 with dissolve
                            qu "Is that all you got?"
                            mc "Haha, yeah. But that's a lot."
                            qu "Pathetic."
                        "On ass (Vaginal)":
                            scene anim_quinn_behind_ep9 with dissolve
                            qu "Here's your chance, [mc_quinn]."
                            qu "Spray my ass with your cum! Give me what's mine."
                            pause
                            scene ep9_quinn_lewd53 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd53 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep9_quinn_lewd53 at vpunch, cum2
                            mc "Fuck!!! Ahhh!"
                            scene ep9_quinn_lewd54 with dissolve
                            qu "Is that all you got?"
                            mc "Haha, yeah. But that's a lot."
                            qu "Pathetic."
                    scene ep9_quinn_lewd56 with dissolve
                    qu "I'm surprised you're still alive after that."
                    scene ep9_quinn_lewd55 with dissolve
                    mc "How are you still full of energy after moving that much? I thought you'd be relaxed by now."
                    scene ep9_quinn_lewd56 with dissolve
                    qu "Pff. Relaxed? You didn't even make me cum."
                    scene ep9_quinn_lewd55b with dissolve
                    mc "Stop lying; I know you came. You tried to hide it, but I could tell."
                    scene ep9_quinn_lewd55 with dissolve
                    mc "So... Weren't you gonna eat me alive or something?"
                    scene ep9_quinn_lewd57 with dissolve
                    mc "OUCH! FUCK!"
                    scene ep9_quinn_lewd58 with dissolve
                    qu "Hahaha! Such a pussy!"
                    qu "Maybe I'll keep you as a chewing toy instead."
                else:
                    $ tmpStr = "Cum"
                    mc "Ok, you've had your fun. Now I'm gonna show you what I got."
                    jump ep9_quinn_lewd_loop2_label
scene ep9_quinn_lewd59 with dissolve
mc "Damn... Maybe I should leave after all..."
scene ep9_quinn_lewd60 with dissolve
qu "I'm gonna go wash up. If you're still here when I get back..."
scene ep9_quinn_lewd60b with dissolve
mc "Yeah, I know..."
scene ep9_quinn_lewd60 with dissolve
qu "It wouldn't be the worst way to end the night."
scene ep9_quinn_lewd61 with dissolve
mc "Oh?"
qu "Plus, people are probably fucking on your bed now anyway."

stop music fadeout 10
scene ep9_quinn_lewd62 with dissolve
mc "(That was quite a drunken workout...)"
scene ep9_quinn_lewd63 with dissolve
play sound "sound_effects/interlude/zoey_message.mp3"
"*{i}Phone message{/i}*"
scene ep9_quinn_lewd64 with dissolve
$ renpy.pause()
scene ep9_quinn_lewd65 with dissolve
mc "(What's that about?)"
scene ep9_quinn_lewd66 with dissolve
play music "music/ep9/relaxed.mp3"
$ renpy.pause()
scene ep9_quinn_lewd67 with dissolve
qu "I thought you'd have passed out by now, for sure."
scene ep9_quinn_lewd68 with dissolve
mc "Almost. But I didn't want to fall asleep before you got back."
scene ep9_quinn_lewd69 with dissolve
qu "An FYI. I got zero problems with you telling people we fuck, but if you even mention this to anyone, I'll cut your dick off."
scene ep9_quinn_lewd68 with dissolve
mc "Whoa. Are you serious?"
scene ep9_quinn_lewd69 with dissolve
qu "You don't wanna find out."
scene ep9_quinn_lewd70 with dissolve
mc "You really don't know how to do sleepovers."
qu "..."
scene ep9_quinn_lewd71 with dissolve
qu "Fall the fuck asleep already so I can pretend this doesn't suck."
scene ep9_quinn_lewd72 with dissolve
$ renpy.pause()
scene ep9_quinn_lewd73 with fade
$ renpy.pause()
scene ep9_quinn_lewd74 with dissolve
$ renpy.pause()
scene ep9_quinn_lewd75 with dissolve
$ renpy.pause()
scene ep9_quinn_lewd76 with dissolve
mc "*{i}Smack{/i}*"
scene ep9_quinn_lewd77 with dissolve
$ renpy.pause()
scene ep9_quinn_lewd78 with dissolve
qu "*{i}Smack{/i}*"
scene ep9_quinn_lewd79 with dissolve
qu "Mmm..."
scene ep9_quinn_lewd80 with dissolve
mc "Are you still drunk?"
scene ep9_quinn_lewd81 with dissolve
qu "That must be it."
stop music fadeout 3
scene ep9_quinn_lewd79 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep9_lewd_quinn = True
$ calcScenes()
$ new_bio("Quinn", "After the Halloween party, I had sex with Quinn in her room and spent the night.")
$ mphone_stats_add_girl_s3("quinn","You had sex with Quinn after the Halloween party in episode 9.")


if "Quinn" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Quinn")

if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          "Josy & Maya" if branchMayaJosy and "Josy" not in wt_ep9_scenes:
            if "Josy" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Josy")
            jump ep9_jm_committing_label
          "Jill" if branchJill and "Jill" not in wt_ep9_scenes:
            if "Jill" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Jill")
            jump ep9_jill_lewd2_label
          "Sage" if branchSage and "Sage" not in wt_ep9_scenes:
                if "Sage" not in wt_ep9_scenes:
                   $wt_ep9_scenes.append("Sage")
                jump ep9_sage_hunt_label
          "Isabella" if branchIsabella and "Bella" not in wt_ep9_scenes:
                if "Bella" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Bella")
                jump ep9_bella_lewd2_label
          
          "Lily & Nicole" if branchAlone and (envyLikesYou or ep7_lily_lewd) and "Lily" not in wt_ep9_scenes:
                $ep9_lily_nicole_lewd=True
                
                if "Lily" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Lily")
                jump ep9_lily_nicole_lewd_label
          "Melanie & Sarah" if branchAlone and (ep6_sarah_lewd or ep8_sarah_lewd or ep8_melanie_lewd or ep4_fuckedMelanie) and "Sarah" not in wt_ep9_scenes:
                
                $ep9_sarah_melanie_lewd=True
                if "Sarah" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Sarah")
                jump ep9_sm_lewd_label
          "Continue the game":
              pass
              
if wt_ep9_branch_numbers != 1:
    "End the night with?"
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if envyLikesYou:
                            $mod_choices[6]="[m_c1](Progress Nicole path)"
    
    menu:
         "Josy & Maya" if "Josy" in wt_ep9_scenes:
            $wt_ep9_end_pick="Maya"
         "Jill"  if "Jill" in wt_ep9_scenes:
            $wt_ep9_end_pick="Jill"
         "Sage"  if "Sage" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sage"
         "Isabella" if "Bella" in wt_ep9_scenes:
            $wt_ep9_end_pick="Bella"
         "Quinn" if "Quinn" in wt_ep9_scenes:
            $wt_ep9_end_pick="Quinn"
         "Lily & Nicole [mod_choices[6]]" if "Lily" in wt_ep9_scenes:
            $wt_ep9_end_pick="Lily"
         "Melanie & Sarah" if "Sarah" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sarah"
         "Tara & Tiffani & Gina":
            $ep9_tiffani_gina_tara=True
            $wt_ep9_end_pick="Other"

jump ep9_ending_label

label ep9_ending_quinn_label:
scene ep9_ending_quinn1 with dissolve
$ renpy.pause()
scene ep9_ending_quinn2 with dissolve
mc "You did it."
scene ep9_ending_quinn3 with dissolve
qu "Hm?"
scene ep9_ending_quinn2 with dissolve
mc "Your first sleepover. How was it?"
scene ep9_ending_quinn4 with dissolve
qu "I hated it."
scene ep9_ending_quinn2 with dissolve
mc "Sure you did."
scene ep9_ending_quinn5 with dissolve
$ renpy.pause()
scene ep9_ending_quinn2 with dissolve
mc "Don't give me that look. This is the only time you'd have me sleep over. I'm taking advantage here."
scene ep9_ending_quinn4 with dissolve
qu "Well, the night's over, and so is this."
scene ep9_ending_quinn2 with dissolve
mc "..."
scene ep9_ending_quinn6 with dissolve
qu "Leave whenever and however. Out the window, preferably; the back door's an option too."
scene ep9_ending_quinn7 with dissolve
$ renpy.pause()

jump ep9_ending2_label

label ep9_ending_others_label:
scene ep9_ending_others1 with dissolve
my "[name]!"
js "Hey!"
scene ep9_jm_committing5 with dissolve
mc "Are you still here? I thought you left."
scene ep9_ending_others2 with dissolve
js "We've been drinking with Derek for a while. He's been pretty upset about Ashley, so we felt he needed some support."
scene ep9_ending_others3 with dissolve
mc "That's nice of you. He didn't take it well that she didn't show up."
scene ep9_ending_others4 with dissolve
my "It feels like people are leaving. Or is it just me?"
scene ep9_jm_committing5 with dissolve
mc "No, people have been dropping out for the last few hours. It's getting very late, so I don't blame anyone for wanting to go to bed by now."
scene ep9_ending_others2 with dissolve
js "I think that's our cue too."
scene ep9_ending_others5 with dissolve
my "*{i}Yawns{/i}* Yeah, definitely."
scene ep9_ending_others4 with dissolve
my "Thanks for an amazing party!"
scene ep9_ending_others2 with dissolve
js "Yeah, it was so much fun! You did a great job with it."
scene ep9_jm_committing5 with dissolve
mc "Thanks for showing up!"
if branchSage and wt_ep9_end_pick=="Sage":
    jump ep9_sage_hunt_label
elif branchJill and wt_ep9_end_pick=="Jill":
    jump ep9_jill_lewd2_label
elif branchIsabella and wt_ep9_end_pick=="Bella":
    jump ep9_bella_lewd2_label
mc "Have a nice end to the night; I'm gonna head to bed too."
if len(wt_ep9_scenes) < 2:
    $ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
    $ renpy.sound.play("sound_effects/season3/bus.mp3", channel="sfx2", loop=False)
    scene ep9_ending18 with dissolve
    $ renpy.pause()
    scene ep9_ending20 with dissolve
    $ renpy.pause()
    scene ep9_ending19 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    $ renpy.music.stop(channel="sfx1", fadeout=3)
    $ renpy.music.stop(channel="sfx2", fadeout=3)
    scene ep9_ending21 with dissolve
    $ renpy.pause()
scene ep9_ending_others6 with dissolve
mc "*{i}Yawns{/i}* (What a crazy night.)"
mc "(I don't look forward to tomorrow's hangover.)"
scene ep9_ending_others7 with dissolve
mc "Uh... Hello?"
scene ep9_ending_others8 with dissolve
mc "(Are they passed out...?)"
mc "Girls? You're in my bed."
mc "Girls?"
scene ep9_ending_others9 with dissolve
ti "Tara... It's for you."
scene ep9_ending_others11 with dissolve
ta "*{i}Mumbles{/i}* Is it Oscar?"
scene ep9_ending_others9 with dissolve
ti "Are you Oscar?"
scene ep9_ending_others10 with dissolve
if name == "Oscar":
    mc "Well, yeah. But probably not the Oscar you're referring to."
else:
    mc "No, I'm [name]."
scene ep9_ending_others9 with dissolve
ti "Gina... There's a guy here for you."
scene ep9_ending_others12 with dissolve
gi "Ok..."
scene ep9_ending_others13 with dissolve
mc "You're in my bed. I'm going to sleep."
scene ep9_ending_others14 with dissolve
if ep9_josy_choice != "CHICK":
    gi "*{i}Mumbles{/i}* Oh... It's this guy..."
else:
    gi "*{i}Mumbles{/i}* I don't wanna go home."
ti "Can we stay the night?"
ta "Please?"
scene ep9_ending_others13 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["()","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "[mod_gr]Join them":
        $ ep9_tiffani_gina_tara = True
        mc "That's up to you. But I'm sleeping in my bed."
        scene ep9_ending_others15 with dissolve
        ti "Gina... There's a naked guy here for you."
        scene ep9_ending_others16 with dissolve
        gi "*{i}Mumbles{/i}* Is it Oscar?"
        scene ep9_ending_others17 with dissolve
        ta "My Oscar?"
        scene ep9_ending_others18 with dissolve
        ti "No."
        scene ep9_ending_others16 with dissolve
        gi "*{i}Mumbles{/i}* Doesn't matter. Send him over."
        scene ep9_ending_others19 with dissolve
        mc "(Is this how life's gonna be from now on?)"
        mc "(Going to bed with strangers after parties?)"
        if affinity == "DIK":
            scene ep9_ending_others20 with dissolve
            mc "(Fucking awesome.)"
        else:
            mc "(I don't know how I feel about it...)"
        scene ep9_ending_others21 with dissolve
        ta "You smell good."
        scene ep9_ending_others22 with dissolve
        ti "It's too hot in here."
        scene ep9_ending_others23 with dissolve
        ta "Right?"
        ti "Remove your top, then."
        scene ep9_ending_others24 with dissolve
        mc "Sure... Make yourselves comfortable."
        mc "(Damn...)"
        scene ep9_ending_others25 with dissolve
        mc "(Yep... No one will believe me tomorrow.)"
        scene ep9_ending_others26 with dissolve
        mc "What was your name again?"
        scene ep9_ending_others27 with dissolve
        ti "Tiffani. That's Tara and Gina."
        scene ep9_ending_others26 with dissolve
        mc "Right."
        scene ep9_ending_others28 with dissolve
        mc "(All right... I can do this. Just close your eyes and drift away.)"
        if affinity == "DIK":
            scene ep9_ending_others29 with dissolve
            mc "(Or...?)"
            scene ep9_ending_others30 with dissolve
            mc "So...um... Are you girls up for doing something or...?"
            scene ep9_ending_others31 with dissolve
            if ep9_tara_kiss:
                ta "I already told you I can't. I have a boyfriend."
            else:
                ta "I can't. I have a boyfriend."
            scene ep9_ending_others30 with dissolve
            mc "Right, sure... I can feel your tits against me, by the way."
            scene ep9_ending_others29 with dissolve
            ti "*{i}Snores{/i}*"
        else:
            scene ep9_ending_others29 with dissolve
        mc "(It's gonna be a long night...)"
        $ new_bio("You", "I chose to sleep in my bed with the girls who were crashing in it.")
    "Take the couch":
        $ ep9_tiffani_gina_tara = False
        mc "Yeah. Stay. I'm gonna take the couch."
        scene ep9_ending_others34 with dissolve
        mc "(Ugh... I hope I don't end up breaking anything in my sleep.)"
        scene ep9_ending_others35 with dissolve
        mc "(Next party, I'm locking my door before the party ends.)"
        $ new_bio("You", "I chose to sleep on my couch instead of my bed with the girls who were crashing in it.")
stop music fadeout 3
jump ep9_ending_label

label ep9_ending2_others_label:
if ep9_tiffani_gina_tara:
    scene ep9_ending_others40 with dissolve
    $ renpy.pause()
    scene ep9_ending_others41 with dissolve
    dikcs "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the walk!"
    dikcs "*{i}Sings{/i}* What walk!?"
    scene ep9_ending_others42 with dissolve
    $ renpy.pause()
else:
    scene ep9_ending_others36 with dissolve
    $ renpy.pause()
    scene ep9_ending_others37 with dissolve
    $ renpy.pause()
    scene ep9_ending_others38 with dissolve
    dikcs "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the walk!"
    dikcs "*{i}Sings{/i}* What walk!?"
    scene ep9_ending_others39 with dissolve
    $ renpy.pause()

jump ep9_ending2_label

label ep9_sm_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep4_smoked_weed = True
    $ ep9_top_pick = " "
$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track131.mp3"])
scene ep9_sm_lewd1 with wipeleft
ml "I fucking love burgers!"
scene ep9_sm_lewd2 with dissolve
sar "Tell me about it. I loooove this burger."
scene ep9_sm_lewd4 with dissolve
ml "I'd let this burger fuck me."
scene ep9_sm_lewd3 with dissolve
sar "It wouldn't be the worst thing you've stuck up there."
play sound "sound_effects/hand.mp3"
scene ep9_sm_lewd5 with hpunch
sar "Haha! What!?"
scene ep9_sm_lewd6 with dissolve
sar "Don't throw your burger at me, bitch."
ml "Give it back."
scene ep9_sm_lewd7 with dissolve
mc "You're that hungry, huh?"
scene ep9_sm_lewd8 with dissolve
sar "It's the weed, dude. It always makes you hungry."
scene ep9_sm_lewd7 with dissolve
if ep4_smoked_weed:
    mc "I don't recall it doing that when I smoked."
    scene ep9_sm_lewd8 with dissolve
    sar "Think about food the next time you do, and I guarantee it will."
else:
    mc "Why is that?"
    scene ep9_sm_lewd8 with dissolve
    sar "I don't know. It's just one of those things."
scene ep9_sm_lewd9 with dissolve
ml "I'm full."
scene ep9_sm_lewd10 with dissolve
sar "Good, because that was the last one."
if ep9_top_pick == "Sarah":
    scene ep9_sm_lewd11 with dissolve
    ml "So, what did Sarah promise to do to you?"
    scene ep9_sm_lewd11b with dissolve
    mc "She promised something?"
    scene ep9_sm_lewd12 with dissolve
    ml "She must have. Otherwise, there's no way she'd get picked as one of the top three costumes."
    scene ep9_sm_lewd13 with dissolve
    sar "Girl, you're saltier than a fucking french fry! Just accept it. I'm the better bunny."
    scene ep9_sm_lewd14 with dissolve
    ml "You lost, though."
    scene ep9_sm_lewd13 with dissolve
    sar "You didn't even get picked."
    scene ep9_sm_lewd14 with dissolve
    ml "Pff!"
elif ep9_top_pick == "Melanie":
    scene ep9_sm_lewd11 with dissolve
    ml "Tell me, was it you who picked me for the competition or what?"
    scene ep9_sm_lewd11b with dissolve
    mc "Of course, it was."
    scene ep9_sm_lewd11 with dissolve
    ml "I knew it."
    scene ep9_sm_lewd13 with dissolve
    sar "You didn't win."
    scene ep9_sm_lewd14 with dissolve
    ml "Neither did you, so shut it."
else:
    scene ep9_sm_lewd11 with dissolve
    ml "I can't believe you didn't pick me for the competition, [name]. What the hell?"
    scene ep9_sm_lewd11b with dissolve
    mc "Sorry, but I had to pick someone, and it was pretty hard."
    scene ep9_sm_lewd15 with dissolve
    sar "It should have been me up there."
    scene ep9_sm_lewd14 with dissolve
    ml "As if!"
scene ep9_sm_lewd11b with dissolve
mc "Did you have fun tonight?"
scene ep9_sm_lewd16 with dissolve
ml "Yeah, sure."
scene ep9_sm_lewd17 with dissolve
sar "It was all right."
scene ep9_sm_lewd18 with dissolve
mc "Was it that bad?"
scene ep9_sm_lewd15 with dissolve
sar "Did we hurt your feelings or something? It was a fun party."
scene ep9_sm_lewd18 with dissolve
mc "It was the first party I had ever planned, so I wanted to make sure it was perfect."
scene ep9_sm_lewd16 with dissolve
ml "The parties tend to blend into each other when you party as much as we do."
scene ep9_sm_lewd17 with dissolve
sar "Yeah, they all feel the same at some point. That doesn't mean they're bad, but it doesn't make them amazing."
scene ep9_sm_lewd18 with dissolve
mc "Then, what would make a party amazing for you?"
scene ep9_sm_lewd16 with dissolve
ml "Maybe something unexpected?"
scene ep9_sm_lewd17 with dissolve
sar "Yeah. That or something out of the ordinary. Like, a change of venue or something."
sar "Lately, it's always been at our place, or your place, in the dorms..."
scene ep9_sm_lewd16 with dissolve
ml "At the alphas..."
scene ep9_sm_lewd17 with dissolve
sar "The preps' party was different, but it sucked for another reason."
scene ep9_sm_lewd18 with dissolve
mc "It sounds hard to please you."
scene ep9_sm_lewd11 with dissolve
ml "He's totally upset now."
scene ep9_sm_lewd15 with dissolve
sar "Yeah, come on, [name]..."
scene ep9_sm_lewd18 with dissolve
mc "Haha! I'm not upset. I swear."
scene ep9_sm_lewd20 with dissolve
ml "You did a great job!"
scene ep9_sm_lewd21 with dissolve
sar "Totally! Such a good job!"
scene ep9_sm_lewd19 with dissolve
mc "Stop that. You don't have to reassure me. I know I did my best."
ml "Hahaha!"
sar "Haha! We're just messing with you."
mc "I know."
scene ep9_sm_lewd18 with dissolve
mc "Thanks for the burger. I guess I should be heading back."
scene ep9_sm_lewd20 with dissolve
ml "To what? An empty party?"
scene ep9_sm_lewd18 with dissolve
mc "That, and back home to my bed."
scene ep9_sm_lewd22 with dissolve
sar "So, you didn't come back here with us for a reason?"
scene ep9_sm_lewd23 with dissolve
mc "I...wanted a burger."
scene ep9_sm_lewd20 with dissolve
ml "As if I'm gonna believe this guy didn't smoke tonight after saying that."
scene ep9_sm_lewd21 with dissolve
sar "Yeah, I don't believe him, either."
scene ep9_sm_lewd20 with dissolve
ml "Tell it like it is, [name]."
scene ep9_sm_lewd18 with dissolve
mc "I knew I was getting at least a burger coming here, but sure..."
mc "...can I stay the night?"
scene ep9_sm_lewd22 with dissolve
sar "So, a burger and a place to sleep? That's it?"
scene ep9_sm_lewd24 with dissolve
ml "Why won't he admit it?"
scene ep9_sm_lewd25 with dissolve
mc "*{i}Sigh{/i}* Ok..."
mc "Both of you look insanely hot tonight."
mc "I tried to keep my cool, but your asses are fucking amazing in those tight outfits."
scene ep9_sm_lewd26 with dissolve
mc "I jumped at the chance to come back here with you because I hoped it would lead to more than a burger."
scene ep9_sm_lewd21 with dissolve
sar "He's still not saying it."
scene ep9_sm_lewd25 with dissolve
menu:
    "I wanna fuck you":
        $ ep9_sm_anal = False
        mc "I wanna fuck you. Both of you."
        scene ep9_sm_lewd29 with dissolve
        mc "I wanna fuck you hard against that weird cushion thingy."
        scene ep9_sm_lewd25 with dissolve
        mc "I wanna fuck you on the beds. Top bunk, lower bunk, I don't give a shit."
    "I wanna fuck your asses":
        $ ep9_sm_anal = True
        mc "I wanna fuck your asses. Both of them."
        scene ep9_sm_lewd29 with dissolve
        mc "I wanna fuck them hard against that weird cushion thingy."
        scene ep9_sm_lewd25 with dissolve
        mc "I wanna fuck them on the beds. Top bunk, lower bunk, I don't give a shit."
mc "All I know is that I'm not skipping a chance to get with the two sexiest girls at our Halloween party tonight."
mc "There, I said it."
scene ep9_sm_lewd27 with dissolve
ml "See!? If you had said that two hours ago, we'd all three be in bed sleeping already."
scene ep9_sm_lewd28 with dissolve
sar "Yeah, about time, [name]. You've gotta learn to be more upfront with us."
scene ep9_sm_lewd25 with dissolve
mc "I'm not gonna be upfront with you; I'm gonna be at your back now."
scene ep9_sm_lewd27 with dissolve
ml "That's what I like to hear."
hide screen new_phone_screen
scene ep9_sm_lewd30 with dissolve
mc "Give me..."
scene ep9_sm_lewd31 with dissolve
sar "I knew we looked irresistible in these."
ml "Mhm..."
scene ep9_sm_lewd32 with dissolve
mc "You'll look irresistible without them too."
scene ep9_sm_lewd33 with dissolve
mc "Yeah, I was right..."
scene ep9_sm_lewd34 with dissolve
mc "Damn... I don't know where to begin..."
ml "With me, obviously. Why settle for the lesser ass?"
sar "You're so clueless. Petite is where it's at, right, [name]?"
menu:
    "Eat pussy (Melanie)":
        scene ep9_sm_lewd35 with dissolve
        ml "Yes! Haha! I win!"
        sar "[name] must be drunk to choose you over me."
        ml "Hngnnn... His tongue certainly works. That's what I care about."
        scene ep9_sm_lewd38 with dissolve
        ml "*{i}Moans{/i}*"
        sar "Are you gonna share or what?"
        ml "Chill, girl... Just a bit more."
        scene ep9_sm_lewd39 with dissolve
        sar "My turn!"
        ml "Hey! I wasn't done."
        sar "I don't care!"
    "Eat ass (Melanie)":
        scene ep9_sm_lewd36 with dissolve
        ml "Yes! Haha! I win!"
        sar "[name] must be drunk to choose you over me."
        ml "Hngnnn... His tongue certainly works. That's what I care about."
        scene ep9_sm_lewd37 with dissolve
        ml "*{i}Moans{/i}*"
        sar "Are you gonna share or what?"
        ml "Chill, girl... Just a bit more."
        scene ep9_sm_lewd40 with dissolve
        sar "My turn!"
        ml "Hey! I wasn't done."
        sar "Eating your fat ass would take ages anyway."
    "Eat pussy (Sarah)":
        scene ep9_sm_lewd39 with dissolve
        sar "I knew [name] understood what I meant. He's very smart."
        ml "He just needs to warm his tongue up on something before he gets to me. Consider yourself lucky he didn't choose the rest of my burger."
        sar "Bitch!"
        scene ep9_sm_lewd35 with dissolve
        ml "Yes, give it to me..."
        sar "He's good, huh?"
        scene ep9_sm_lewd38 with dissolve
        ml "*{i}Moans{/i}* Very..."
    "Eat ass (Sarah)":
        scene ep9_sm_lewd40 with dissolve
        sar "I knew [name] understood what I meant. He's very smart."
        ml "He just needs to warm his tongue up on something before he gets to me. Consider yourself lucky he didn't choose the rest of my burger."
        sar "Bitch!"
        scene ep9_sm_lewd36 with dissolve
        ml "Yes, give it to me..."
        sar "He's good, huh?"
        scene ep9_sm_lewd37 with dissolve
        ml "*{i}Moans{/i}* Very..."

scene ep9_sm_lewd41 with dissolve
ml "*{i}Smack{/i}* Let us return the favor..."
sar "Ever gotten a rimjob, [name]?"
scene ep9_sm_lewd42 with dissolve
mc "No. I've licked stuff myself but never gotten licked."
scene ep9_sm_lewd43 with dissolve
sar "Then you should definitely try it... Who do you want at the front?"
scene ep9_sm_lewd42 with dissolve
menu:
    "Blowjob from Sarah":
        mc "Sarah... Do you wanna?"
        scene ep9_sm_lewd43 with dissolve
        sar "Do I wanna what?"
        scene ep9_sm_lewd42 with dissolve
        mc "Suck my dick."
        scene ep9_sm_lewd44 with dissolve
        $ renpy.pause()
        scene ep9_sm_lewd45 with dissolve
        ml "Strap in for this, [name]."
        scene anim_sm_bj1_ep9 with dissolve
        mc "Whoa! Hey!"
        mc "That's... Uh..."
        pause
        scene anim_sm_bj2_ep9 with dissolve
        sar "*{i}Suck suck{/i}*"
        ml "*{i}Lick lick{/i}* Do you like it?"
        menu:
            "Yes":
                $ ep9_sm_like_rim = True
                mc "Oh... Wow... That... Why does that feel so good? Damn..."
                ml "Haha, good..."
            "Not for me":
                $ ep9_sm_like_rim = False
                mc "I don't think that's for me... But it's cool to try new stuff."
        pause
    "Blowjob from Melanie":
        scene ep9_sm_lewd46 with dissolve
        mc "Mel? Do you wanna?"
        scene ep9_sm_lewd45 with dissolve
        ml "Still with the half-sentence questions... Come on, [name]."
        scene ep9_sm_lewd46 with dissolve
        mc "Suck my dick, Mel."
        scene ep9_sm_lewd45 with dissolve
        ml "You know what that means, Sarah."
        scene ep9_sm_lewd43 with dissolve
        sar "I'm not complaining."
        scene anim_sm_bj3_ep9 with dissolve
        mc "Whoa! Hey!"
        pause
        scene anim_sm_bj4_ep9 with dissolve
        sar "*{i}Suck suck{/i}*"
        ml "*{i}Lick lick{/i}* Do you like it?"
        menu:
            "Yes":
                $ ep9_sm_like_rim = True
                mc "Oh... Wow... That... Why does that feel so good? Damn..."
                ml "Haha, good..."
            "Not for me":
                $ ep9_sm_like_rim = False
                mc "I don't think that's for me... But it's cool to try new stuff."
        pause

scene ep9_sm_lewd47 with dissolve
sar "Against the cushion, you said?"
if ep9_sm_anal:
    sar "Lube that dick up and let's go."
scene ep9_sm_lewd48 with dissolve
sar "Don't go giving Mel the dick first now."
ml "Don't listen to her, [name]. Use my hole first, will you?"
menu:
    "Fuck Sarah":
        if ep9_sm_anal:
            scene ep9_sm_lewd49 with dissolve
        else:
            scene ep9_sm_lewd52 with dissolve
        sar "Excellent choice. There's no point in saving the best for last. Right, [name]?"
        if ep9_sm_anal:
            scene ep9_sm_lewd50 with dissolve
        sar "Fuck! Damn..."
        ml "It's too big for you."
        sar "Shut up; it's not!"
        if ep9_sm_anal:
            scene anim_sarah_anal_doggy1_ep9 with dissolve
        else:
            scene anim_sarah_doggy1_ep9 with dissolve
        sar "Fuck... Hngnn..."
        ml "You can't handle him."
        pause
        if ep9_sm_anal:
            scene anim_sarah_anal_doggy2_ep9 with dissolve
        else:
            scene anim_sarah_doggy2_ep9 with dissolve
        sar "I can handle him fine. You've probably not even felt the full size of him."
        sar "And I can't blame you; he wouldn't get this hard from fucking your sloppy holes."
        pause
        scene ep9_sm_lewd51 with dissolve
        ml "Oh, fuck you!"
        ml "[name], give it to me."
        if ep9_sm_anal:
            scene ep9_sm_lewd53 with dissolve
        else:
            scene ep9_sm_lewd54 with dissolve
        mc "Hey, easy! Don't fight."
        ml "Hngn..."
        if ep9_sm_anal:
            scene anim_melanie_anal_doggy1_ep9 with dissolve
        else:
            scene anim_melanie_doggy1_ep9 with dissolve
        ml "See that? What do you say about that?"
        sar "I say that I warmed him up for you."
        pause
        if ep9_sm_anal:
            scene anim_melanie_anal_doggy2_ep9 with dissolve
        else:
            scene anim_melanie_doggy2_ep9 with dissolve
        mc "Fuck, this feels great..."
        sar "*{i}Cough{/i}*"
        mc "Oh, you felt amazing too, Sarah."
        ml "But not as good as me."
        pause
    "Fuck Melanie":
        if ep9_sm_anal:
            scene ep9_sm_lewd53 with dissolve
            ml "I win- Hngnnn!!!"
        else:
            scene ep9_sm_lewd54 with dissolve
            ml "I win!"
        sar "Enjoy it... Just like you have to finish your meal before dessert, he's clearly saving the best for last."
        if ep9_sm_anal:
            scene anim_melanie_anal_doggy1_ep9 with dissolve
            ml "Fuck, [name]... God! *{i}Moans{/i}*"
        else:
            scene anim_melanie_doggy1_ep9 with dissolve
            ml "Fuck, [name]..."
        sar "If you're wondering how [name] looks as he's fucking you, I'd describe it as mildly bored."
        pause
        if ep9_sm_anal:
            scene anim_melanie_anal_doggy2_ep9 with dissolve
        else:
            scene anim_melanie_doggy2_ep9 with dissolve
        mc "Huh? No way! I'm having the best time right now."
        ml "HAHA! Hear that? The BEST time."
        pause
        if ep9_sm_anal:
            scene ep9_sm_lewd49 with dissolve
        else:
            scene ep9_sm_lewd52 with dissolve
        sar "Give it to me. You wouldn't know what \"the best time\" is until you've enjoyed my hole."
        if ep9_sm_anal:
            scene anim_sarah_anal_doggy1_ep9 with dissolve
        else:
            scene anim_sarah_doggy1_ep9 with dissolve
        mc "Damn..."
        sar "*{i}Moans{/i}* I'll take that as him agreeing with me."
        pause
        if ep9_sm_anal:
            scene anim_sarah_anal_doggy2_ep9 with dissolve
        else:
            scene anim_sarah_doggy2_ep9 with dissolve
        ml "And I'll take it as \"damn, what a shame I had to share my cock with her\"."
        sar "If \"her\" means you, then he couldn't be more right."
        pause
mc "Girls, stop fighting. Teamwork is way more fun."
mc "What if you, Sarah, get on top of Mel and I'll take care of both of you?"
scene ep9_sm_lewd55 with dissolve
ml "How many burgers did you eat? Bitch, you're heavy."
scene ep9_sm_lewd57 with dissolve
sar "I'm not heavy; I'm petite. I think you're just weak. Maybe you should hit the gym more often."
scene ep9_sm_lewd57b with dissolve
ml "Yeah? And you should-"
scene ep9_sm_lewd56 with hpunch
ml "Oh, fuck!"
scene anim_mel_anal_doggy3_ep9 with dissolve
ml "*{i}Moans{/i}*"
sar "That good?"
ml "Yeah... It's that good..."
pause
if ep9_sm_anal:
    scene anim_mel_doggy3b_ep9 with dissolve
else:
    scene anim_mel_doggy3_ep9 with dissolve
pause
sar "[name]? Are you gonna share that with me?"
menu:
    "Beg me for it":
        mc "Beg me for it."
        scene ep9_sm_lewd58 with dissolve
        sar "Please, [name]? Fuck me..."
    "Shove it in her":
        $ renpy.pause(0.5)

if ep9_sm_anal:
    scene ep9_sm_lewd60 with dissolve
else:
    scene ep9_sm_lewd61 with dissolve
$ renpy.pause()
scene ep9_sm_lewd59 with hpunch
sar "Oh, fuck!!!"
if ep9_sm_anal:
    scene anim_sarah_anal_doggy3_ep9 with dissolve
else:
    scene anim_sarah_doggy3_ep9 with dissolve
ml "Told you it was good."
sar "Way better than the burgers."
ml "Hahaha!"
pause
menu:
    "Reverse cowgirl (Sarah)":
        if ep9_sm_anal:
            scene anim_sarah_anal_rev_ep9 with dissolve
        else:
            scene anim_sarah_rev_ep9 with dissolve
        ml "Fuck her..."
        mc "Oh, I am."
        sar "You know the saying \"fuck like bunnies\"?"
        ml "Isn't it rabbits?"
        sar "Same shit. And that's what I'll be doing with [name]."
        ml "You and me both."
        sar "*{i}Moans{/i}*"
        pause
    "Reverse cowgirl (Melanie)":
        if ep9_sm_anal:
            scene anim_mel_anal_rev_ep9 with dissolve
        else:
            scene anim_mel_rev_ep9 with dissolve
        ml "Deeper, [name]!"
        sar "Deeper? Holy shit! All of it?"
        ml "You did it too."
        sar "It looks scarier seeing it from here than getting fucked with it."
        ml "*{i}Moans{/i}* Haha, you just need more practice with it."
        sar "Pff! I bet it's because I'm more used to getting it than watching someone get it."
        ml "Keep telling yourself that. *{i}Moans{/i}*"
        pause

label ep9_sm_lewd_loop_label:
    menu:
        "Doggystyle (Sarah)":
            if ep9_sm_anal:
                scene anim_sarah_anal_doggy1_ep9 with dissolve
            else:
                scene anim_sarah_doggy1_ep9 with dissolve
            pause
            if ep9_sm_anal:
                scene anim_sarah_anal_doggy2_ep9 with dissolve
            else:
                scene anim_sarah_doggy2_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Doggystyle (Melanie)":
            if ep9_sm_anal:
                scene anim_melanie_anal_doggy1_ep9 with dissolve
            else:
                scene anim_melanie_doggy1_ep9 with dissolve
            pause
            if ep9_sm_anal:
                scene anim_melanie_anal_doggy2_ep9 with dissolve
            else:
                scene anim_melanie_doggy2_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Stacked (Sarah)":
            if ep9_sm_anal:
                scene anim_sarah_anal_doggy3_ep9 with dissolve
            else:
                scene anim_sarah_doggy3_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Stacked (Melanie)":
            scene anim_mel_anal_doggy3_ep9 with dissolve
            pause
            if ep9_sm_anal:
                scene anim_mel_doggy3b_ep9 with dissolve
            else:
                scene anim_mel_doggy3_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Reverse cowgirl (Sarah)":
            if ep9_sm_anal:
                scene anim_sarah_anal_rev_ep9 with dissolve
            else:
                scene anim_sarah_rev_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Reverse cowgirl (Melanie)":
            if ep9_sm_anal:
                scene anim_mel_anal_rev_ep9 with dissolve
            else:
                scene anim_mel_rev_ep9 with dissolve
            pause
            jump ep9_sm_lewd_loop_label
        "Cum":
            menu:
                "Creampie (Sarah)":
                    if ep9_sm_anal:
                        scene anim_sarah_anal_doggy3_ep9 with dissolve
                    else:
                        scene anim_sarah_doggy3_ep9 with dissolve
                    mc "I'm gonna cum..."
                    sar "Cum inside me, [name]. There's no need to share with her."
                    ml "Hey, what the fuck!?"
                    pause
                    if ep9_sm_anal:
                        scene ep9_sm_lewd64 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd64 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd64 at hpunch, cum1
                        mc "Ahh!!!"
                        scene ep9_sm_lewd65 with dissolve
                    else:
                        scene ep9_sm_lewd62 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd62 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd62 at hpunch, cum1
                        mc "Ahh!!!"
                        scene ep9_sm_lewd63 with dissolve
                    pause
                "Creampie (Melanie)":
                    if ep9_sm_anal:
                        scene anim_mel_doggy3b_ep9 with dissolve
                    else:
                        scene anim_mel_doggy3_ep9 with dissolve
                    mc "I'm gonna cum..."
                    ml "Yes, give it to me! Fill me!"
                    sar "You're such a dumpster!"
                    ml "Shut up!"
                    pause
                    if ep9_sm_anal:
                        scene ep9_sm_lewd66 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd66 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd66 at hpunch, cum1
                        mc "Ahh!!!"
                        scene ep9_sm_lewd67 with dissolve
                    else:
                        scene ep9_sm_lewd68 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd68 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sm_lewd68 at hpunch, cum1
                        mc "Ahh!!!"
                        scene ep9_sm_lewd69 with dissolve
                    pause
                "On asses":
                    scene anim_cum1_ep9 with dissolve
                    mc "Get ready... I'm cumming."
                    ml "Mmm... Give it to us, [name]."
                    sar "Cum on our tight asses, [name]..."
                    pause
                    scene ep9_sm_lewd70 at hpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep9_sm_lewd70 at hpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep9_sm_lewd70 at hpunch, cum2
                    mc "Ahh!!!"
                    scene ep9_sm_lewd71 with dissolve
                    pause
                "Facial":
                    scene anim_cum2_ep9 with dissolve
                    mc "Get ready... I'm cumming."
                    ml "Mmm... Give it to us, [name]."
                    sar "Cum on our slutty faces, [name]..."
                    pause
                    scene ep9_sm_lewd72 at hpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep9_sm_lewd72 at hpunch, cum2
                    $ renpy.pause(0.5)
                    scene ep9_sm_lewd72 at hpunch, cum2
                    mc "Ahh!!!"
                    scene ep9_sm_lewd73 with dissolve
                    sar "Mmm..."
                    ml "You didn't hold anything back..."

scene ep9_sm_lewd74 with dissolve
ml "*{i}Phew{/i}*"
mc "Damn..."
sar "My thoughts exactly..."
scene ep9_sm_lewd76 with dissolve
sar "[name]?"
scene ep9_sm_lewd77 with dissolve
mc "Yeah?"
scene ep9_sm_lewd76 with dissolve
sar "Best party ever."
scene ep9_sm_lewd78 with dissolve
ml "Yep. Nothing can top it."
scene ep9_sm_lewd75 with dissolve
mc "Stop fucking with me."
sar "Hahaha!"
ml "Haha! It's too fucking funny!"
$ renpy.end_replay()
$ persistent.ep9_lewd_sm = True
$ calcScenes()
$ new_bio("Sarah", "I had a threesome with Sarah and Melanie after the Halloween party.")
$ new_bio("Melanie", "I had a threesome with Sarah and Melanie after the Halloween party.")
$ mphone_stats_add_girl_s3("sarah","You had a threesome with Sarah and Melanie after the Halloween party in episode 9.")
$ mphone_stats_add_girl_s3("melanie","You had a threesome with Sarah and Melanie after the Halloween party in episode 9.")
stop music fadeout 3

if "Sarah" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Sarah")

if wt_ep9_branch_numbers != 1:
    "See other scenes?"
    menu:
          "Josy & Maya" if branchMayaJosy and "Josy" not in wt_ep9_scenes:
            if "Josy" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Josy")
            jump ep9_jm_committing_label
          "Jill" if branchJill and "Jill" not in wt_ep9_scenes:
            if "Jill" not in wt_ep9_scenes:
                $wt_ep9_scenes.append("Jill")
            jump ep9_jill_lewd2_label
          "Sage" if branchSage and "Sage" not in wt_ep9_scenes:
                if "Sage" not in wt_ep9_scenes:
                   $wt_ep9_scenes.append("Sage")
                jump ep9_sage_hunt_label
          "Isabella" if branchIsabella and "Bella" not in wt_ep9_scenes:
                if "Bella" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Bella")
                jump ep9_bella_lewd2_label
          "Quinn" if branchAlone and ep8_quinn_lewd and "Quinn" not in wt_ep9_scenes:
                
                $ep9_quinn_lewd=True
                
                if "Quinn" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Quinn")
                jump ep9_quinn_lewd_label
          "Lily & Nicole" if branchAlone and (envyLikesYou or ep7_lily_lewd) and "Lily" not in wt_ep9_scenes:
                $ep9_lily_nicole_lewd=True
                
                if "Lily" not in wt_ep9_scenes:
                    $wt_ep9_scenes.append("Lily")
                jump ep9_lily_nicole_lewd_label
          
          "Continue the game":
              pass
              
if wt_ep9_branch_numbers != 1:
    "End the night with?"
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        if envyLikesYou:
                            $mod_choices[6]="[m_c1](Progress Nicole path)"
    
    menu:
         "Josy & Maya" if "Josy" in wt_ep9_scenes:
            $wt_ep9_end_pick="Maya"
         "Jill"  if "Jill" in wt_ep9_scenes:
            $wt_ep9_end_pick="Jill"
         "Sage"  if "Sage" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sage"
         "Isabella" if "Bella" in wt_ep9_scenes:
            $wt_ep9_end_pick="Bella"
         "Quinn" if "Quinn" in wt_ep9_scenes:
            $wt_ep9_end_pick="Quinn"
         "Lily & Nicole [mod_choices[6]]" if "Lily" in wt_ep9_scenes:
            $wt_ep9_end_pick="Lily"
         "Melanie & Sarah" if "Sarah" in wt_ep9_scenes:
            $wt_ep9_end_pick="Sarah"
         "Tara & Tiffani & Gina":
            $ep9_tiffani_gina_tara=True
            $wt_ep9_end_pick="Other"


jump ep9_ending_label

label ep9_sm_ending_label:
scene ep9_sm_ending1 with dissolve
$ renpy.pause()
scene ep9_sm_ending2 with dissolve
$ renpy.pause()
scene ep9_sm_ending3 with dissolve
$ renpy.pause()
scene ep9_sm_ending4 with dissolve
mc "Morning..."
ml "Shh..."
scene ep9_sm_ending5 with dissolve
$ renpy.pause()
scene ep9_sm_ending6 with dissolve
mc "Oh, wow..."
scene bg anim_sm_ending_ep9 movie with dissolve
$ renpy.pause()
jump ep9_ending2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

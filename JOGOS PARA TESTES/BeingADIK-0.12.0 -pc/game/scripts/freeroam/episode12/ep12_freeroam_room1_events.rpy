label ep12_freeroam_room1_label:
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep9/relaxed.mp3"])
show screen new_phone_screen
scene ep12_freeroam1_room0 with wipeleft
$ renpy.pause()
if (branchZoey and not wt_ep11_zoey_kiss_others) and not branchAlone:
    scene ep12_freeroam1_room1 with dissolve
    mc "(I have to do it... I need to rip the band-aid...)"
    scene ep12_freeroam1_room2 with dissolve
    if branchMayaJosy:
        mc "(No... It can't be a phone call or text. I owe them more than that.)"
    else:
        mc "(No... It can't be a phone call or text. I owe her more than that.)"
        if branchIsabella:
            mc "(She knows it's coming, but even so... It will suck telling her.)"
    scene ep12_freeroam1_room3 with dissolve
    if branchMayaJosy:
        mc "(It will hurt them...)"
    else:
        mc "(It will hurt her...)"
    mc "(But I'm in love with Zoey... It will be worth it.)"
    if branchSage and jade_state > 0:
        $ ep12_break_or_tell = "break"
        mc "(And I hate to admit it, but Derek was right about my situation with Jade and Sage...)"
        mc "(At least I get to spare their relationship.)"
    elif not branchSage and jade_state > 0:
        scene ep12_freeroam1_room4 with dissolve
        mc "(And then there's Sage...)"
        mc "(And I hate to admit it, but Derek was right about my situation with Jade and Sage...)"
        mc "(The guilt won't go away, and I can't tell her what I did...)"
        mc "(I'm going to have to try and be less of a friend to Sage from now on...)"
elif branchSage and jade_state > 0 and wt_ep9_branch_numbers == 1:
    scene ep12_freeroam1_room1 with dissolve
    mc "(No matter how many times I think about it, it stays the same...)"
    mc "(The guilt I feel about Jade and Sage won't go away.)"
    scene ep12_freeroam1_room3 with dissolve
    mc "(I can't base our relationship on this lie... And like Derek, I don't see any chance that Sage will forgive me...)"
    menu:
        "Break up with Sage":
            $ ep12_break_or_tell = "break"
            mc "(I'd rather spare her relationship with her mom than tell her what I did... Derek was right.)"
        "Tell Sage about Jade":
            $ ep12_break_or_tell = "tell"
            mc "(Even if I ruin her mom for her, I need to come clean about it. It's the only way I can feel good about myself.)"
elif not branchSage and jade_state > 0 and wt_ep9_branch_numbers == 1:
    scene ep12_freeroam1_room1 with dissolve
    mc "(I hate to admit it, but Derek was right about my situation with Jade and Sage...)"
    mc "(The guilt won't go away, but I can't tell her what I did...)"
    mc "(I'm going to have to try and be less of a friend to Sage from now on...)"
else:
    scene ep12_freeroam1_room1 with dissolve
    mc "(Yesterday was rough. I wonder how everyone's feeling today.)"
if ((branchZoey and not wt_ep11_zoey_kiss_others) and not branchAlone) or (branchSage and jade_state > 0  and wt_ep9_branch_numbers == 1):
    scene ep12_freeroam1_room2 with dissolve
    mc "(Fuck! I hate myself...)"
jump ep12_fr_room1_setup_label

label ep12_fr_sage_call_label:
scene ep12_fr_sage_call2 with dissolve
mc "Hey, it's me. Are you free?"
scene ep12_fr_sage_call1 with dissolve
sa "Sadly, not... It's hectic before winter break."
sa "And right now, I'm busy studying. At least it will be my last finals..."
sa "At last, the name lives up to it. Haha!"
sa "Did you want something important?"
scene ep12_fr_sage_call3 with dissolve
mc "Oh, sorry. Um... Yeah, it's important but not urgent."
scene ep12_fr_sage_call1 with dissolve
sa "I'm free tomorrow afternoon. Does that work for you?"
scene ep12_fr_sage_call2 with dissolve
mc "Tomorrow works."
scene ep12_fr_sage_call1 with dissolve
sa "Can't wait to see you."
scene ep12_fr_sage_call4 with dissolve
mc "(Tomorrow then...)"
mc "(That gives me some time to prepare...)"
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_fr_bia_chat_label:
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Bianca","Hey, it's Bianca.",True])
if branchZoey and not wt_ep11_zoey_kiss_others:
    $ text_message_screen_list.append(["%s" % name,"Hey, I changed my mind about this. I'm out. You should delete my number. I won't tell anyone what happened.",False])
    $ text_message_screen_list.append(["Bianca","Weird, but ok.",True])
else:
    $ text_message_screen_list.append(["%s" % name,"I was wondering when you'd shoot me a message.",False])
    $ text_message_screen_list.append(["Bianca","It's been on my mind since the party. I went back and forth about whether to send one. How about you?",True])
    $ text_message_screen_list.append(["%s" % name,"I'm the same as you. We're bad...",False])
    $ text_message_screen_list.append(["Bianca","Yep. So bad...",True])
hide screen new_phone_screen
play sound "sound_effects/interlude/zoey_message.mp3"
scene ep12_fr_bia_chat1 with dissolve
show screen text_message_screen
$ renpy.pause()
if branchZoey and not wt_ep11_zoey_kiss_others:
    scene ep12_fr_bia_chat2 with dissolve
    mc "(Oh, fuck... That's right, I started flirting with Bianca...)"
    if branchJill:
        mc "(Another sign that I wasn't happy with Jill...)"
    else:
        mc "(Another sign that I wasn't happy with Bella...)"
    mc "(I'm such a mess... Zoey doesn't even have a clue what she's in for...)"
    mc "(I have to end whatever this flirt is with Bianca immediately.)"
    scene ep12_fr_bia_chat3 with dissolve
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    mc "(No. It's not weird at all. I see things clearly now.)"
    $ new_bio("Bianca", "I ended my flirt with Bianca.")
    hide screen text_message_screen
    $ mphone_contact_list.insert(0,["Bianca","NONE",False])
    $ mphone_chat_history_list.insert(0,["Bianca",0,[],[]," ",0])
    $ mphone_scene_to_chat("Bianca",text_message_screen_list)
else:
    scene ep12_fr_bia_chat4 with dissolve
    mc "(I've been waiting for her to reach out. Looks like she didn't get cold feet after sobering up.)"
    mc "(Fuck, it's risky to continue this with her...)"
    if branchJill and wt_ep9_branch_numbers == 1:
        mc "(I'd be betraying Jill... Again...)"
    elif branchIsabella  and wt_ep9_branch_numbers == 1:
        mc "(I'd be betraying Bella... Again...)"
    scene ep12_fr_bia_chat5 with dissolve
    mc "(But like Bianca said... There's this shameless side of me that enjoys it, too...)"
    mc "(Fuck, I get horny thinking about doing stuff to her.)"
    $ tmpInt += 1
    mc "(I'm going for it.)"
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat6 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"At least we're bad together. So, what are we going to do about it? mphone_emoji_tongue",False])
    $ text_message_screen_list.append(["Bianca","What do you want to do about it?",True])
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    menu:
        "I asked you first":
            $ text_message_screen_list.append(["%s" % name,"I asked you first. I wanna see how daring you'd get.",False])
            $ text_message_screen_list.append(["Bianca","I thought that instead of me touching myself while thinking about you... How about you touch yourself thinking about me?",True])
        "I know what I want to do":
            $ text_message_screen_list.append(["%s" % name,"I know what I want to do... I get hard thinking about you.",False])
            $ text_message_screen_list.append(["Bianca","Do you touch yourself when you think about me?",True])
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat7 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"I would do that, but my imagination sucks. I have a difficult time picturing your face and body. Can you help me out?",False])
    $ text_message_screen_list.append(["Bianca","Tell me how.",True])
    $ text_message_screen_list.append(["%s" % name,"Send me some sexy pictures. That would get me going.",False])
    $ text_message_screen_list.append(["Bianca","I'll do it if you do it too.",True])
    $ text_message_screen_list.append(["%s" % name,"Deal.",False])
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
    scene ep12_fr_bia_chat8 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["Bianca","chat_bianca_pic1_ep12_thumb",True])
    $ text_message_screen_list.append(["Bianca","chat_bianca_pic2_ep12_thumb",True])
    $ text_message_screen_list.append(["Bianca","How about that?",True])
    $ text_message_screen_list.append(["%s" % name,"Wow! That was way more than I thought you'd send. You're so sexy! That will do the trick.",False])
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat9 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"chat_bianca_pic3_ep12_thumb",False])
    $ text_message_screen_list.append(["%s" % name,"This one is for you.",False])
    $ text_message_screen_list.append(["Bianca","Fuck. It looks delicious. I want to put that in my mouth.",True])
    $ text_message_screen_list.append(["%s" % name,"I'm stroking it to you now.",False])
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat10 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["Bianca","Mmm... I wish I were there. I'm rubbing myself to you.",True])
    $ text_message_screen_list.append(["%s" % name,"What would you do if you were here with me?",False])
    $ text_message_screen_list.append(["Bianca","I'd tell myself to take it slow with you, but honestly, I'd sit on you and let you penetrate me hard.",True])
    $ text_message_screen_list.append(["Bianca","I'd bounce up and down on you and push your face into my tits.",True])

    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat11 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"Fuck! You're gonna make me cum talking like that. Go on.",False])
    $ text_message_screen_list.append(["Bianca","My tight pussy could barely handle your big cock, and I'd moan loudly from having it inside.",True])
    $ text_message_screen_list.append(["Bianca","You'd bend me over on your bed and take me from behind. I would push my ass toward you forcefully until you came inside me.",True])

    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    scene ep12_fr_bia_chat12 at vpunch, cum2
    $ renpy.pause(0.5)
    scene ep12_fr_bia_chat12 at vpunch, cum2
    $ renpy.pause(0.5)
    scene ep12_fr_bia_chat12 at vpunch, cum2
    $ renpy.pause()

    hide screen text_message_screen
    scene ep12_fr_bia_chat13 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["%s" % name,"Look at what you made me do...",False])
    $ text_message_screen_list.append(["%s" % name,"chat_bianca_pic4_ep12_thumb",False])
    $ text_message_screen_list.append(["Bianca","Mmm... I like the look of that. I want to clean that up with my tongue...",True])
    $ text_message_screen_list.append(["%s" % name,"I wish you did.",False])

    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    scene ep12_fr_bia_chat14 with dissolve
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)
    $ text_message_screen_list.append(["Bianca","Do you have time to meet me soon? It has to be discreet.",True])
    $ text_message_screen_list.append(["%s" % name,"How about during winter break? Most will leave and go back home to their families. I bet I can get the place to myself. At least, there will be fewer prying eyes.",False])
    if not ep9_told_jill:
        $ text_message_screen_list.append(["Bianca","Let me know when. But I'll need a heads up.",True])
    else:
        $ text_message_screen_list.append(["Bianca","Let me know when. Even if it's on short notice.",True])
    $ text_message_screen_list.append(["%s" % name,"You got it. Thanks for the pictures. I'll put them to good use until we meet.",False])
    $ text_message_screen_list.append(["Bianca","mphone_emoji_kiss",True])

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
    $ mphone_contact_list.insert(0,["Bianca","NONE",False])
    $ mphone_chat_history_list.insert(0,["Bianca",0,[],[]," ",0])
    $ mphone_scene_to_chat("Bianca",text_message_screen_list)
    $ mgallery_add_photo("chat_bianca_pic1_ep12_zoomed")
    $ mgallery_add_photo("chat_bianca_pic2_ep12_zoomed")

    scene ep12_fr_bia_chat15 with dissolve
    mc "(She wants to do it too... And I need to have her... There's no turning back now.)"
    mc "(Fuck, that was hot.)"
    $ new_bio("Bianca", "I continued my flirt with Bianca. We shared some lewd pictures with each other.")
    $ ep12_bianca_lewd = True

$ task_list[1] = ""
$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep12_fr_jill_call_label:
scene ep12_fr_sage_call2 with dissolve
mc "Hi, Jill..."
scene ep12_fr_sage_call1 with dissolve
ji "Oh? What's wrong?"
scene ep12_fr_sage_call3 with dissolve
mc "Can I drop by? We need to talk."
scene ep12_fr_sage_call1 with dissolve
ji "I'm not at home right now, but I can come to you after I get back."
scene ep12_fr_sage_call2 with dissolve
mc "Yeah, drop by when you can. It's...important."
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_fr_jill_call2_label:
scene ep12_fr_jill_call1 with dissolve
mc "Hi, Jill."
scene ep12_fr_jill_call2 with dissolve
ji "Hi, you! What's up?"
scene ep12_fr_jill_call1 with dissolve
mc "I felt like hearing your voice."
scene ep12_fr_jill_call2 with dissolve
ji "Aw. I'm not at home right now. "
scene ep12_fr_jill_call1 with dissolve
mc "What are you up to?"
scene ep12_fr_jill_call2 with dissolve
ji "It's a secret..."
scene ep12_fr_jill_call4 with dissolve
mc "A secret? Now you've got me curious."
scene ep12_fr_jill_call3 with dissolve
ji "Can I drop by after I get back?"
scene ep12_fr_jill_call4 with dissolve
mc "I'd love that."
scene ep12_fr_jill_call3 with dissolve
ji "I'll hurry."
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_fr1_music_label:
scene ep12_fr1_music1 with dissolve
mc "(20 minutes worth of songs for the faculty's party... That's longer than it sounds.)"
mc "(Since it's a Christmas party, I should play some Christmas-themed songs.)"
stop music fadeout 3
mc "(But I should be smart and choose some songs I already know by heart since I don't have too much time to practice.)"
play music "music/ep12/licensed_music/track196.mp3"
scene ep12_fr1_music2 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_fr1_music3 with dissolve
mc "(That sounded good.)"
mc "(If I practice some every day, I should be able to make it work.)"
$ mphone_next_song()
$ task_list[3] = ""
$ updateTaskList()
jump endEvent

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

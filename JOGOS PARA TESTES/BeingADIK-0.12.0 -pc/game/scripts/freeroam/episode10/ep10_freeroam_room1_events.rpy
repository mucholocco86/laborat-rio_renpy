label ep10_fr2_desk_event_label:
scene ep10_fr2_desk_event1 with dissolve
mc "(Nick told me we need to put sick fish in quarantine in a separate bowl. I guess that's my responsibility now.)"
mc "(Not that I mind it, but I need to make sure I don't forget to take care of the fish.)"

$ specialMessage = "{size=-%d}You can now take care of the aquarium from your desk.{/size}" % (5 * persistent.scale_factor)
show screen specialmsglong
pause
hide screen specialmsglong
$ task_list[4] = ""
$ optional_task_list[0] = "Take care of your fish"
$ updateTaskList()
jump endEvent

label ep10_fr2_sage_event_label:
scene ep10_fr2_sage_event1 with dissolve
$ renpy.pause()
scene ep10_fr2_sage_event2 with dissolve
mc "Whoa..."
scene ep10_fr2_sage_event3 with dissolve
sa "What?"
scene ep10_fr2_sage_event4 with dissolve
mc "That's a lot of cinnamon you put on your oatmeal."
scene ep10_fr2_sage_event5 with dissolve
sa "No, it's not."
scene ep10_fr2_sage_event4 with dissolve
mc "It's not? There's like this brown desert sand cloud of cinnamon surrounding your bowl."
scene ep10_fr2_sage_event5 with dissolve
sa "Don't you like cinnamon?"
scene ep10_fr2_sage_event4 with dissolve
mc "It's alright, but I don't like doing the cinnamon challenge for breakfast."
scene ep10_fr2_sage_event6 with dissolve
sa "Funny guy."
scene ep10_fr2_sage_event4 with dissolve
mc "Were you always this messy?"
scene ep10_fr2_sage_event5 with dissolve
sa "How am I messy?"
scene ep10_fr2_sage_event7 with dissolve
$ renpy.pause()
scene ep10_fr2_sage_event8 with dissolve
sa "Meh! Relax, I'll clean it up after."
sa "Any other \"compliments\" you'd like to give me?"
scene ep10_fr2_sage_event9 with dissolve
mc "Yes, and a real one at that. It's nice to see that you're comfortable around me like this."
mc "And I like waking up next to you and starting my day with you."
scene ep10_fr2_sage_event10 with dissolve
sa "Ok, those compliments saved your butt from a spanking."

$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep10_bella_phone_call_label:
scene ep10_bella_phone_call1 with fade
$ renpy.pause()
play sound "sound_effects/door_slam.mp3"
scene ep10_bella_phone_call2 with hpunch
$ renpy.pause()
play sound "sound_effects/season2/vibrate.mp3"
scene ep10_bella_phone_call3 with dissolve
"*{i}Phone vibrates{/i}*"
scene ep10_bella_phone_call4 with dissolve
isa "Hello?"
if branchIsabella:
    scene ep10_bella_phone_call5 with dissolve
    mc "I'm finally up and about. Sorry if I kept you waiting."
    scene ep10_bella_phone_call4 with dissolve
    isa "I assumed you had classes."
    scene ep10_bella_phone_call5 with dissolve
    mc "Nope. I have a study day today, and I slept in."
    scene ep10_bella_phone_call6 with dissolve
    isa "That doesn't sound like a study day."
    scene ep10_bella_phone_call7 with dissolve
    mc "It's called \"study day\", not \"study morning\". And I will study."
    mc "Maybe I'll drop by the library later and let you watch me."
    scene ep10_bella_phone_call6 with dissolve
    isa "Haha... Please, do."
    scene ep10_bella_phone_call7 with dissolve
    mc "What did you want?"
else:
    scene ep10_bella_phone_call5 with dissolve
    mc "Hey, Bella. What's wrong?"
    scene ep10_bella_phone_call4 with dissolve
    isa "Why would something be wrong?"
    scene ep10_bella_phone_call5 with dissolve
    mc "You texted me, asking me to call you. It sounded like something was wrong."
    scene ep10_bella_phone_call6 with dissolve
    isa "Well, surprise, surprise. I wanted to be friendly."
    scene ep10_bella_phone_call7 with dissolve
    mc "Oh? Sorry. What's up?"

scene ep10_bella_phone_call6 with dissolve
if branchIsabella:
    isa "Tomorrow, the gym is having a free classes day, and I wanted to invite you to do yoga with me."
else:
    isa "Tomorrow, the gym is having a free classes day, and I wanted to invite you to do yoga with Jill and me."
scene ep10_bella_phone_call7 with dissolve
mc "Do you want me in your yoga class?"
scene ep10_bella_phone_call8 with dissolve
isa "I thought it would be fun for you. You've shown moderate interest in it before, and now is a perfect opportunity to broaden your horizons."
scene ep10_bella_phone_call9 with dissolve
if branchIsabella:
    mc "While I'd love to hang out with you more, I'm afraid I will feel out of place."
else:
    if affinity == "DIK":
        mc "I like that you want to do stuff with me and all..."
    else:
        mc "I gotta say that I'm flattered that you invited me. It makes me happy to hear..."
    mc "...but a yoga class. I will feel out of place."
    if not branchJill:
        mc "And I'm not sure if Jill would want me there. We had a pretty weird discussion the last time I saw her."
scene ep10_bella_phone_call8 with dissolve
if branchIsabella or branchJill:
    isa "It doesn't hurt to feel out of place. Venturing outside of your comfort zone is good for you."
else:
    isa "I asked her, and she didn't mind."
    isa "Also, it doesn't hurt to feel out of place. Venturing outside of your comfort zone is good for you."
scene ep10_bella_phone_call9 with dissolve
mc "Like you did, showing up at our Halloween party, huh?"
scene ep10_bella_phone_call8 with dissolve
isa "Exactly."
scene ep10_bella_phone_call9 with dissolve
mc "All right. I'll come, but don't set your expectations too high."
scene ep10_bella_phone_call6 with dissolve
isa "I've known you long enough to know where my expectations should be."
scene ep10_bella_phone_call7 with dissolve
mc "I'm not sure if that's a compliment or an insult. But thanks for inviting me."
scene ep10_bella_phone_call8 with dissolve
if branchIsabella:
    isa "See you later today, then. Whenever you get dressed and ready to study."
    scene ep10_bella_phone_call9 with dissolve
    mc "I'll drop by soon. I know how much you miss me."
    scene ep10_bella_phone_call10 with dissolve
    $ renpy.pause()
else:
    isa "Have a nice \"study day\", [name]."
    scene ep10_bella_phone_call9 with dissolve
    mc "Sure! Good luck with \"work\"."
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep10_derek_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
scene ep10_derek_shop1 with dissolve
de "What's up, [mc_de]? Do you need something?"
scene ep10_derek_shop2 with dissolve
show screen newmoneymsg
call screen shop_derek_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
scene ep10_derek_shop1 with dissolve
de "Later, bro!"
jump endEvent

label ep10_magnar_shop:
$ renpy.block_rollback()
$ phone_call_enabled = False
scene ep10_magnar_shop1 with dissolve
mg "Top of the morning to you, [name]. What can I do for you?"
scene ep10_magnar_shop2 with dissolve
show screen newmoneymsg
call screen shop_magnar_screen
$ renpy.pause(0.5)
hide screen newmoneymsg
scene ep10_magnar_shop1 with dissolve
mg "Have a good one, [name]!"
jump endEvent

label ep10_jm_plan_label:
if branchSage:
    scene ep10_jm_plan4 with dissolve
    mc "What are you up to this weekend? Wanna do something?"
    scene ep10_jm_plan5 with dissolve
    sa "Friday, I'm busy, but I'm free on Saturday."
    scene ep10_jm_plan4 with dissolve
    mc "Great! Let's hang out."

if branchMayaJosy:
    scene ep10_jm_plan1 with dissolve
    mc "(It's almost the weekend again. And I have nothing planned on Friday.)"
    mc "(I wanna be with Josy and Maya, but I'm not sure if we should spend time together as it is right now...)"
    mc "(With the lie and all, maybe it's best to lay low?)"
    mc "(That doesn't mean I can't spend some time with one of them, right?)"
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Maya scene)","(Josy scene)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Mod: Both":
            $ ep10_jm_solo = "Maya Josy"
            hide screen new_phone_screen
            $ tmpInt = 0
            $ tmpInt2 = 0
            $ text_message_screen_list = []
            $ text_message_screen_list.append(["%s" % name,"How does you and me on Friday sound like?",False])
            $ text_message_screen_list.append(["Maya","Like the best Friday imaginable. Is Josy coming?",True])
            $ text_message_screen_list.append(["%s" % name,"I thought we could spend some alone time together if you don't mind. And with the whole relationship excuse and all, maybe it's best if we don't hang out together here this weekend? Also, Tommy's still pissed off at me.",False])
            $ text_message_screen_list.append(["Maya","Understandable. It's a date. mphone_emoji_heart",True])

            scene ep10_jm_plan2 with dissolve
            show screen text_message_screen
            $ renpy.pause()
            play sound "sound_effects/interlude/zoey_message.mp3"
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            scene ep10_jm_plan3 with dissolve
            stop music fadeout 3
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            $ mphone_scene_to_chat("Maya",text_message_screen_list)
            show screen new_phone_screen
            hide screen new_phone_screen
            $ tmpInt = 0
            $ tmpInt2 = 0
            $ text_message_screen_list = []
            $ text_message_screen_list.append(["%s" % name,"Are you free on Friday night? I'd like to spend it with you.",False])
            $ text_message_screen_list.append(["Josy","Free as a bird. Your place?",True])
            $ text_message_screen_list.append(["%s" % name,"Tommy's still pissed at me. Can we do your place?",False])
            $ text_message_screen_list.append(["Josy","I'll check with Heather if she'll be here or not. Either way, we'll make it work. mphone_emoji_kiss",True])
            scene ep10_jm_plan2 with dissolve
            show screen text_message_screen
            $ renpy.pause()
            play sound "sound_effects/interlude/zoey_message.mp3"
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            scene ep10_jm_plan3 with dissolve
            stop music fadeout 3
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            $ mphone_scene_to_chat("Josy",text_message_screen_list)
            show screen new_phone_screen
        "Spend Friday with Maya [m_c1][mod_choices[0]]":
            $ ep10_jm_solo = "Maya"
            mc "(I'm sure Josy will understand.)"
            hide screen new_phone_screen
            $ tmpInt = 0
            $ tmpInt2 = 0
            $ text_message_screen_list = []
            $ text_message_screen_list.append(["%s" % name,"How does you and me on Friday sound?",False])
            $ text_message_screen_list.append(["Maya","Like the best Friday imaginable. Is Josy coming?",True])
            $ text_message_screen_list.append(["%s" % name,"I thought we could spend some time alone together if you don't mind. And with the whole relationship excuse and all, maybe it's best if we don't hang out together here this weekend? Also, Tommy's still pissed off at me.",False])
            $ text_message_screen_list.append(["Maya","Understandable. It's a date. mphone_emoji_heart",True])

            scene ep10_jm_plan2 with dissolve
            show screen text_message_screen
            $ renpy.pause()
            play sound "sound_effects/interlude/zoey_message.mp3"
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            scene ep10_jm_plan3 with dissolve
            stop music fadeout 3
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            $ mphone_scene_to_chat("Maya",text_message_screen_list)
            show screen new_phone_screen
        "Spend Friday with Josy [m_c2][mod_choices[1]]":
            $ ep10_jm_solo = "Josy"
            mc "(I'm sure Maya will understand.)"
            hide screen new_phone_screen
            $ tmpInt = 0
            $ tmpInt2 = 0
            $ text_message_screen_list = []
            $ text_message_screen_list.append(["%s" % name,"Are you free on Friday night? I'd like to spend it with you.",False])
            $ text_message_screen_list.append(["Josy","Free as a bird. Your place?",True])
            $ text_message_screen_list.append(["%s" % name,"Tommy's still pissed at me. Can we do your place?",False])
            $ text_message_screen_list.append(["Josy","I'll check with Heather if she'll be here or not. Either way, we'll make it work. mphone_emoji_kiss",True])
            scene ep10_jm_plan2 with dissolve
            show screen text_message_screen
            $ renpy.pause()
            play sound "sound_effects/interlude/zoey_message.mp3"
            $ tmpInt += 1
            $ renpy.pause()
            $ tmpInt += 1
            $ renpy.pause()
            scene ep10_jm_plan3 with dissolve
            stop music fadeout 3
            $ tmpInt += 1
            $ renpy.pause()
            hide screen text_message_screen
            $ mphone_scene_to_chat("Josy",text_message_screen_list)
            show screen new_phone_screen
else:
    if branchSage:
        scene ep10_jm_plan1b with dissolve
        mc "(Hm... But what about Friday? If Sage is busy, what am I gonna do?)"
    else:
        scene ep10_jm_plan1 with dissolve
        mc "(It's almost the weekend again. And I have nothing planned on Friday.)"
    if ep9_jm_sad:
        $ ep10_jm_solo = "Maya"
        mc "(Maybe I could spend some time with Maya and see how she's feeling and all...?)"
        mc "(I don't dare to ask Josy. She'd probably not even answer.)"
    else:
        if ep5_feelingsForMaya:
            $ ep10_jm_solo = "Maya"
            mc "(It's been a while since I hung out with Maya... I should ask her if she's free.)"
        if ep5_feelingsForJosy:
            $ ep10_jm_solo = "Josy"
            mc "(It's been a while since I hung out with Josy... I should ask her if she's free.)"
        
        menu:
                "Spend Friday with Maya":
                    $ ep10_jm_solo = "Maya"
                    mc "(It's been a while since I hung out with Maya... I should ask her if she's free.)"
                "Spend Friday with Josy":
                    $ ep10_jm_solo = "Josy"
                    mc "(It's been a while since I hung out with Josy... I should ask her if she's free.)"
    if ep10_jm_solo == "Maya":
        hide screen new_phone_screen
        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        if ep9_jm_sad:
            $ text_message_screen_list.append(["%s" % name,"Hi, Maya! I hope it's not inappropriate, but I'd like to spend Friday night with you if you're up for it.",False])
            $ text_message_screen_list.append(["Maya","You wanna talk, huh?",True])
            $ text_message_screen_list.append(["%s" % name,"I miss hanging out with you, and I feel like we should get together. I hope you agree.",False])
            $ text_message_screen_list.append(["Maya","I miss you too. I'll drop by, and we'll take it from there. Ok?",True])
        else:
            $ text_message_screen_list.append(["%s" % name,"Hi, Maya! Can we hang out on Friday? I'd love to catch up with you. It's been a while.",False])
            $ text_message_screen_list.append(["Maya","It sure has. I'd love to. What do you wanna do?",True])
            $ text_message_screen_list.append(["%s" % name,"We'll figure something out. My place or yours?",False])
            $ text_message_screen_list.append(["Maya","I need to clean my room, and I'm not feeling up for it. Let's do yours. mphone_emoji_laugh",True])

        if branchSage:
            scene ep10_jm_plan2b with dissolve
        else:
            scene ep10_jm_plan2 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        if branchSage:
            scene ep10_jm_plan3b with dissolve
        else:
            scene ep10_jm_plan3 with dissolve
        stop music fadeout 3
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Maya",text_message_screen_list)
        show screen new_phone_screen
    else:
        hide screen new_phone_screen
        $ tmpInt = 0
        $ tmpInt2 = 0
        $ text_message_screen_list = []

        $ text_message_screen_list.append(["%s" % name,"Wanna spend some quality time with me on Friday? It's been a while since we hung out, just the two of us.",False])
        $ text_message_screen_list.append(["Josy","I'd love to. My place or yours? mphone_emoji_smile",True])
        $ text_message_screen_list.append(["%s" % name,"Yours, please. I need a change of scenery after studying all day in my room. mphone_emoji_smile",False])
        $ text_message_screen_list.append(["Josy","Haha! Ok, I'll check with Heather if it's ok. mphone_emoji_laugh",True])

        if branchSage:
            scene ep10_jm_plan2b with dissolve
        else:
            scene ep10_jm_plan2 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ tmpInt += 1
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        if branchSage:
            scene ep10_jm_plan3b with dissolve
        else:
            scene ep10_jm_plan3 with dissolve
        stop music fadeout 3
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Josy",text_message_screen_list)
        show screen new_phone_screen
jump ep10_tq_label

label ep10_dad_phone_call_label:
scene ep10_dad_phone_call4 with dissolve
dad "Morning, Son."
scene ep10_dad_phone_call5 with dissolve
mc "Morning. Is this a good time?"
scene ep10_dad_phone_call4b with dissolve
dad "Yes, I can talk. How was your weekend and that big party of yours?"
if branchSage:
    scene ep10_dad_phone_call3b with dissolve
else:
    scene ep10_dad_phone_call3 with dissolve
mc "The party was great, mostly. The place was packed, and we had a blast."
if branchSage:
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "That's nice. Did everything go according to plan?"
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
mc "More or less. There were a couple of incidents. Nothing major."
mc "Oh, I wanted to ask you something. I know you're not an electrician, but since you know things and people..."
mc "Our power went out during the party, and we don't know what caused it."
if branchSage:
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "Did you get it back up and running?"
if branchSage:
    scene ep10_dad_phone_call3b with dissolve
else:
    scene ep10_dad_phone_call3 with dissolve
if affinity == "DIK":
    mc "No, we partied all night in the dark. Haha, of course we did."
else:
    mc "Yeah, of course."
scene ep10_dad_phone_call6 with dissolve
dad "It could be that a circuit breaker was overloaded. It should be flipped off automatically if it's a modern fuse box."
scene ep10_dad_phone_call5 with dissolve
mc "When we went to look, it all looked the same in there. We fixed it by pulling this big lever next to the fuse box."
scene ep10_dad_phone_call6 with dissolve
dad "Oh? Was it the main breaker?"
scene ep10_dad_phone_call5 with dissolve
mc "I guess. The power came back on after we did it."
scene ep10_dad_phone_call6 with dissolve
dad "The main breaker would rarely shut off like that unless there's a power failure."
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
mc "Do you think someone might have shut it off manually?"
if branchSage:
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "That would certainly kill the power, and it's a more plausible explanation."
dad "If there was a major power failure, you couldn't turn everything back on just like that without the breaker blowing again."
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
mc "Thanks... I had a hunch because something didn't feel right about it."
if branchSage:
    scene ep10_dad_phone_call1b2 with dissolve
    sa "Snow!? Already? Shut up, weather bitch! It's November!"
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "People shouldn't play around with fuse boxes. Those are dangerous."
if branchSage:
    scene ep10_dad_phone_call3b with dissolve
else:
    scene ep10_dad_phone_call3 with dissolve
mc "I know. Thanks for the help."
if branchSage:
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "Don't mention it."
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
mc "Another thing... About Thanksgiving..."
scene ep10_dad_phone_call4b with dissolve
dad "I look forward to having you."
scene ep10_dad_phone_call5 with dissolve
mc "Would it be ok if we celebrated it on the Friday instead? I made a promise to help a friend in need."
scene ep10_dad_phone_call4b with dissolve
dad "It's just you and me. It's not a problem to postpone it if you're busy. All I wish is to see you sometime that weekend."
scene ep10_dad_phone_call5 with dissolve
mc "Yeah, I wanna come back home too. But, like I said, a friend needs me."
scene ep10_dad_phone_call6 with dissolve
dad "Did something bad happen?"
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
mc "I can tell you at Thanksgiving. It's a longer discussion than a phone call, but don't worry about it."
if branchSage:
    scene ep10_dad_phone_call2b with dissolve
else:
    scene ep10_dad_phone_call2 with dissolve
dad "Ok. Well, take care of your friend. You have a big heart, Son."
dad "And everything else...? Is it good?"
if branchSage:
    scene ep10_dad_phone_call1b with dissolve
else:
    scene ep10_dad_phone_call1 with dissolve
if affinity == "DIK":
    mc "Yeah, everything else is good. Talk soon."
else:
    mc "Yeah, everything else is good. Thanks, Dad. I'll talk to you soon. Love you."
    if branchSage:
        scene ep10_dad_phone_call2b with dissolve
    else:
        scene ep10_dad_phone_call2 with dissolve
    dad "Love you, Son."

    if branchSage:
        scene ep10_dad_phone_call2b2 with dissolve
        sa "Aw... You tell your dad you love him when you hang up?"
        scene ep10_dad_phone_call2b3 with dissolve
        mc "Yeah, so what?"
        scene ep10_dad_phone_call2b2 with dissolve
        sa "I find that incredibly cute."

$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep10_madame_label_shop:
stop music fadeout 3
scene black with fade
$ renpy.pause(2)
scene ep7_madame_1 with dissolve
play music "music/ep7/licensed_music/track53.mp3"
queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]
md "If it isn't [name]..."
scene ep7_madame_2 with dissolve
md "Welcome back, love. How can [madame] satisfy you?"
if "Visit Madame Rose" in optional_task_list:
    $ optional_task_list.remove("Visit Madame Rose")
    $ updateTaskList()
jump ep10_madame_label

label ep10_madame_label:
$ currentEvent = "ep10_madame_label"
scene anim_madame_main_ep7 with dissolve
label ep10_madame_loop_label:
show screen newmoneymsg
menu:
    "Dances":
        menu:
            "Exotic dance #1":
                hide screen newmoneymsg
                jump ep7_madame_dance1_label
            "Back":
                jump ep10_madame_loop_label
    "Teasing":
        menu:
            "[ep7_madame_options_list[1][0]]" if (ep7_madame_options_list[1][0] == "Groping {color=#36ca2b}${/color}" and money > 0) or ep7_madame_options_list[1][0] != "Groping {color=#36ca2b}${/color}":
                if ep7_madame_options_list[1][0] == "Groping {color=#36ca2b}${/color}":
                    jump ep7_madame_buy_groping_label
                hide screen newmoneymsg
                jump ep7_madame_groping_label
            "[ep7_madame_options_list[1][1]]" if (ep7_madame_options_list[1][1] == "Suck tits {color=#36ca2b}$$${/color}" and money > 2) or ep7_madame_options_list[1][1] != "Suck tits {color=#36ca2b}$$${/color}":
                if ep7_madame_options_list[1][1] == "Suck tits {color=#36ca2b}$$${/color}":
                    jump ep7_madame_buy_suck_tits_label
                hide screen newmoneymsg
                jump ep7_madame_suck_tits_label
            "[ep7_madame_options_list[1][2]]" if (ep7_madame_options_list[1][2] == "Lick pussy {color=#36ca2b}$$${/color}" and money > 2) or ep7_madame_options_list[1][2] != "Lick pussy {color=#36ca2b}$$${/color}":
                if ep7_madame_options_list[1][2] == "Lick pussy {color=#36ca2b}$$${/color}":
                    jump ep8_madame_buy_pussylick_label
                hide screen newmoneymsg
                jump ep8_madame_pussylick_label
            "Back":
                jump ep10_madame_loop_label
    "Lewd scenes":
        menu:
            "[ep7_madame_options_list[2][0]]" if (ep7_madame_options_list[2][0] == "Blowjob {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][0] != "Blowjob {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][0] == "Blowjob {color=#36ca2b}$$$${/color}":
                    jump ep7_madame_buy_bj_label
                hide screen newmoneymsg
                jump ep7_madame_bj_label
            "[ep7_madame_options_list[2][1]]" if (ep7_madame_options_list[2][1] == "Assjob {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][1] != "Assjob {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][1] == "Assjob {color=#36ca2b}$$$${/color}":
                    jump ep8_madame_buy_assjob_label
                hide screen newmoneymsg
                jump ep8_madame_assjob_label
            "[ep7_madame_options_list[2][2]]" if (ep7_madame_options_list[2][2] == "Footjob {color=#36ca2b}${/color}" and money > 0) or ep7_madame_options_list[2][2] != "Footjob {color=#36ca2b}${/color}":
                if ep7_madame_options_list[2][2] == "Footjob {color=#36ca2b}${/color}":
                    jump ep10_madame_footjob_buy_label
                hide screen newmoneymsg
                jump ep10_madame_footjob_lewd_label
            "[ep7_madame_options_list[2][3]]" if (ep7_madame_options_list[2][3] == "Boobjob {color=#36ca2b}$${/color}" and money > 1) or ep7_madame_options_list[2][3] != "Boobjob {color=#36ca2b}$${/color}":
                if ep7_madame_options_list[2][3] == "Boobjob {color=#36ca2b}$${/color}":
                    jump ep10_madame_boobjob_buy_label
                hide screen newmoneymsg
                jump ep10_madame_boobjob_lewd_label
            "[ep7_madame_options_list[2][4]]" if (ep7_madame_options_list[2][4] == "Vaginal sex {color=#36ca2b}$$$${/color}" and money > 3) or ep7_madame_options_list[2][4] != "Vaginal sex {color=#36ca2b}$$$${/color}":
                if ep7_madame_options_list[2][4] == "Vaginal sex {color=#36ca2b}$$$${/color}":
                    jump ep10_madame_fuck_buy_label
                hide screen newmoneymsg
                jump ep10_madame_fuck_lewd_label
            "Back":
                jump ep10_madame_loop_label
    "Done":
        hide screen newmoneymsg
        stop music fadeout 3
        mc "I think I better be going."
        scene ep7_madame_16 with dissolve
        md "It's sad to see you go, but I look forward to your next visit."
        $ mphone_next_song()
        jump endEvent

label ep10_madame_footjob_buy_label:
$ renpy.block_rollback()
$ mny(-1)
$ ep7_madame_options_list[2][2] = "Footjob"
hide screen newmoneymsg
mc "Would it be ok if I fucked your feet? Or is that too weird?"
scene ep7_madame_16 with dissolve
md "It's not the weirdest request I've gotten."
md "Let's say {color=#36ca2b}${/color} for that. A special price for my special guy."
jump ep10_madame_footjob_lewd_label

label ep10_madame_boobjob_buy_label:
$ renpy.block_rollback()
$ mny(-2)
$ ep7_madame_options_list[2][3] = "Boobjob"
hide screen newmoneymsg
mc "I'd love to fuck your tits..."
scene ep7_madame_16 with dissolve
md "I think I can take care of that request for you."
md "For {color=#36ca2b}$${/color}, I'll let you feel how soft they are against your cock."
jump ep10_madame_boobjob_lewd_label

label ep10_madame_fuck_buy_label:
$ renpy.block_rollback()
$ mny(-4)
$ ep7_madame_options_list[2][4] = "Vaginal sex"
hide screen newmoneymsg
mc "Out of curiosity... How much would it be to fuck you?"
scene ep7_madame_16 with dissolve
md "{color=#36ca2b}$$$${/color}. It's expensive, but you won't regret it."
scene anim_madame_main_ep7 with dissolve
mc "Ok... I wanna do it."
scene ep7_madame_16 with dissolve
md "Anal is not included in that price."
jump ep10_madame_fuck_lewd_label


label ep10_madame_boobjob_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ madame = "Madame"
    play music "music/ep7/licensed_music/track53.mp3"
    queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]

scene ep10_madame_boobjob4 with dissolve
$ renpy.pause()
scene ep10_madame_boobjob3 with dissolve
md "Sit back and spread your legs, love."
scene ep10_madame_boobjob1 with dissolve
md "There we go. My lubed-up breasts envelop your thick cock..."
scene anim_madame_boobjob1_ep10 with dissolve
md "Is that tight enough for you?"
mc "Yeah, [madame]. I love how big they are. They even make my cock look small."
pause
scene anim_madame_boobjob2_ep10 with dissolve
md "Haha, they don't. Your member is the biggest one I've felt between my breasts."
md "Your size is making my job simple. I can slip and slide all over your cock with ease."
md "Up and down. Slowly but surely, milking the cum from your balls."
pause
scene anim_madame_boobjob3_ep10 with dissolve
mc "I'm getting close..."
md "That's good, love. I want you to shoot your seed all over my big breasts."
md "Cover my chest in cum."
pause
scene anim_madame_boobjob_cum_ep10 with vpunch
mc "Ahhh!!!"
md "That's it... Cum for [madame]."
pause
scene ep10_madame_boobjob2 with dissolve
md "Mmm... You looked drained, [name]. I take it I satisfied you."
mc "You definitely did... Wow..."

$ renpy.end_replay()
$ persistent.ep10_lewd_madame1 = True
$ calcScenes()
$ renpy.jump(currentEvent)

label ep10_madame_footjob_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ madame = "Madame"
    play music "music/ep7/licensed_music/track53.mp3"
    queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]

scene ep10_madame_footjob4 with dissolve
md "You want to feel [madame]'s feet against your cock. Is that it?"
scene ep10_madame_footjob5 with dissolve
mc "Yeah... Could you jack me off using them?"
md "It's not my first footjob, love."
scene ep10_madame_footjob6 with dissolve
md "I know what my customers like. Let me show you what I've learned."
scene ep10_madame_footjob1 with dissolve
md "They go crazy for this position... Hold my feet to adjust the pressure to your liking."
scene anim_madame_footjob1_ep10 with dissolve
mc "Fuck... Yeah. This is what I wanted for sure."
md "Mhm... Enjoy it, dear."
pause
scene anim_madame_footjob2_ep10 with dissolve
mc "You have such a hot ass, [madame]."
md "I figured you'd enjoy the view."
pause
scene anim_madame_footjob3_ep10 with dissolve
md "Tell me, [name]. How do my soft stockings and feet feel against your throbbing cock? Does it feel like you can cum all over them?"
mc "Yeah... I feel like I could bust any second from this."
md "Don't let me stop you, [name]. They're yours to cum all over. Do it, [name]."
pause
scene ep10_madame_footjob2 at vpunch, cum2
$ renpy.pause(0.5)
scene ep10_madame_footjob2 at vpunch, cum2
$ renpy.pause(0.5)
scene ep10_madame_footjob2 at vpunch, cum2
mc "Ahhh..."
scene ep10_madame_footjob3 with dissolve
md "My feet got warm all of a sudden. I can feel that load's size without looking over my shoulder."
mc "Haha, yeah. I completely covered them."
md "Good that you fully enjoyed yourself, [name]. That's what it's all about."

$ renpy.end_replay()
$ persistent.ep10_lewd_madame2 = True
$ calcScenes()
$ renpy.jump(currentEvent)

label ep10_madame_fuck_lewd_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ madame = "Madame"
    play music "music/ep7/licensed_music/track53.mp3"
    queue music ["music/ep7/licensed_music/track53.mp3","music/ep6/licensed_music/track34.mp3"]

scene ep10_madame_fuck_lewd17 with dissolve
md "Let me get rid of some clothes."
scene ep10_madame_fuck_lewd16 with dissolve
mc "You're keeping the mask on, right?"
scene ep10_madame_fuck_lewd15 with dissolve
md "I always do."
scene ep10_madame_fuck_lewd14 with dissolve
$ renpy.pause()
scene ep10_madame_fuck_lewd13 with dissolve
md "There we go."
scene ep10_madame_fuck_lewd11 with dissolve
md "Now, the question is... How do you want me? Do you want to be on top or not?"
scene ep10_madame_fuck_lewd12 with dissolve
menu:
    "Madame on top":
        mc "To start with... I'd love to have you ride my cock."
        scene ep10_madame_fuck_lewd6 with dissolve
        md "Lie down, [name]. [madame]'s got you..."
        scene ep10_madame_fuck_lewd7 with dissolve
        md "*{i}Moans{/i}*"
        md "Wow... It feels even bigger than it looks. That's quite a feat."
        jump ep10_madame_fuck_top_label
    "You on top":

        mc "To start with... I'd love to be on top."
        scene ep10_madame_fuck_lewd5 with dissolve
        md "Slide your fat cock inside my hole, [name]."
        scene ep10_madame_fuck_lewd1 with dissolve
        md "*{i}Moans{/i}*"
        scene ep10_madame_fuck_lewd2 with dissolve
        md "Wow... It feels even bigger than it looks. That's quite a feat."
        jump ep10_madame_fuck_miss_label

label ep10_madame_fuck_miss_label:
scene anim_madame_miss1_ep10 with dissolve
md "I knew you desired to fuck me the moment I met you."
md "Fuck me hard, [name]."
pause
scene anim_madame_miss2_ep10 with dissolve
mc "Damn... It's such a hot sight..."
mc "(I can't believe I'm doing this.)"
md "Mmm... Go deep, [name]. I can handle it."
pause
scene anim_madame_miss3_ep10 with dissolve
md "Yes, fuck my pussy. Fill it with your big, hard cock."
pause

menu:
    "Let her ride you":
        mc "Can you ride me?"
        scene ep10_madame_fuck_lewd6 with dissolve
        md "Lie down, [name]. [madame]'s got you..."
        scene ep10_madame_fuck_lewd7 with dissolve
        md "*{i}Moans{/i}*"
        jump ep10_madame_fuck_top_label
    "Cum":
        mc "I'm ready to cum..."
        md "Shoot your cum over my pussy, [name]."
        scene ep10_madame_fuck_lewd3 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep10_madame_fuck_lewd3 at vpunch, cum3
        $ renpy.pause(0.5)
        scene ep10_madame_fuck_lewd4 at vpunch, cum3
        mc "Fuck! Ahhh!!!"
        md "There you go..."
        mc "That felt amazing..."
        jump ep10_madame_fuck_after_label


label ep10_madame_fuck_top_label:
scene anim_madame_ride1_ep10 with dissolve
md "Let [madame] take care of you."
md "If you wish, I'll ride your cock until you cum and go soft inside me."
pause
scene anim_madame_ride2_ep10 with dissolve
md "Feel my wet pussy sloshing and slapping against your pelvis as we thrust against each other."
pause
scene anim_madame_ride3_ep10 with dissolve
md "*{i}Moans{/i}* You're fucking me so good, [name]."
pause

menu:
    "Fuck her from the top":
        mc "Can I fuck you for a while?"
        scene ep10_madame_fuck_lewd5 with dissolve
        md "Slide your fat cock inside my hole, [name]."
        scene ep10_madame_fuck_lewd1 with dissolve
        md "*{i}Moans{/i}*"
        scene ep10_madame_fuck_lewd2 with dissolve
        $ renpy.pause()
        jump ep10_madame_fuck_miss_label
    "Cum":
        mc "I'm ready to cum..."
        md "Fill my pussy with your cum, [name]."
        scene ep10_madame_fuck_lewd8 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep10_madame_fuck_lewd8 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep10_madame_fuck_lewd9 at vpunch, cum1
        mc "Fuck! Ahhh!!!"
        scene ep10_madame_fuck_lewd10 with dissolve
        md "There you go..."
        mc "That felt amazing..."
        jump ep10_madame_fuck_after_label

label ep10_madame_fuck_after_label:
$ renpy.end_replay()
$ persistent.ep10_lewd_madame3 = True
$ calcScenes()
$ renpy.jump(currentEvent)

label ep8_madame_buy_assjob_label:
$ renpy.block_rollback()
$ mny(-4)
$ ep7_madame_options_list[2][1] = "Assjob"
hide screen newmoneymsg
mc "If I wanted an assjob, how much would that be?"
scene ep7_madame_16 with dissolve
md "For that, I think {color=#36ca2b}$4{/color} is enough."
scene anim_madame_main_ep7 with dissolve
mc "Ok. Let's do that."
jump ep8_madame_assjob_label
label ep8_madame_assjob_label:
scene anim_madame_assjob3_ep8 with dissolve
md "Here we go, love."
md "Mhm... That's it... Nice and slow."
pause
scene anim_madame_assjob4_ep8 with dissolve
md "Up and down against that hard rod of yours."
pause

label ep8_madame_assjob_loop2_label:
menu:
    "Standing up":
        scene anim_madame_assjob3_ep8 with dissolve
        md "Here we go, love."
        md "Mhm... That's it... Nice and slow."
        pause
        scene anim_madame_assjob4_ep8 with dissolve
        md "Up and down against that hard rod of yours."
        pause
        jump ep8_madame_assjob_loop2_label
    "Lying down":
        scene anim_madame_assjob2_ep8 with dissolve
        md "Lie down and feel my ass go up and down... I hope I'm not pressing it too hard against you."
        mc "No, it's hard enough to feel amazing..."
        pause
        scene anim_madame_assjob1_ep8 with dissolve
        md "I like to mix it up by going like this. I know how you'd like this, [name]."
        pause
        jump ep8_madame_assjob_loop2_label
    "Prone":
        scene anim_madame_assjob5_ep8 with dissolve
        md "Mmm, yes... Use my ass cheeks for your pleasure, love."
        md "I can tell that you're planning on getting your money's worth. That makes me very happy."
        pause
        scene anim_madame_assjob5b_ep8 with dissolve
        md "What's that I feel? You're not about to cum yet, are you?"
        pause
        jump ep8_madame_assjob_loop2_label
    "Cum":

        mc "(Fuck, I'm gonna cum...)"
        menu:
            "Standing up":
                scene anim_madame_assjob4_ep8 with dissolve
                mc "(Can't...hold...it...back...)"
                scene ep8_madame_assjob1 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob1 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob2 at vpunch, cum3
            "Lying down":
                scene anim_madame_assjob2_ep8 with dissolve
                mc "(Can't...hold...it...back...)"
                scene ep8_madame_assjob3 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob3 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob3 at vpunch, cum3
            "Prone":
                scene anim_madame_assjob5b_ep8 with dissolve
                mc "(Can't...hold...it...back...)"
                scene ep8_madame_assjob4 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob4 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep8_madame_assjob5 at vpunch, cum3
        mc "Ahhh!"
        md "Oh, what's that I feel against my back? Mmm, [name]... You didn't..."
        md "Naughty, naughty..."
$ renpy.jump(currentEvent)

label ep8_madame_buy_pussylick_label:
$ renpy.block_rollback()
$ mny(-3)
$ ep7_madame_options_list[1][2] = "Lick pussy"
hide screen newmoneymsg
mc "Can I lick your pussy?"
scene ep7_madame_16 with dissolve
md "Oh, my. How does {color=#36ca2b}$3{/color} sound?"
scene anim_madame_main_ep7 with dissolve
mc "All right."
jump ep8_madame_pussylick_label
label ep8_madame_pussylick_label:
label ep8_madame_pussylick_loop_label:
menu:
    "Doggy (Pussy)":
        scene anim_madame_pussylick1_ep8 with dissolve
        pause
        scene anim_madame_pussylick2_ep8 with dissolve
        pause
        scene anim_madame_pussylick3_ep8 with dissolve
        pause
        jump ep8_madame_pussylick_loop_label
    "Missionary":
        scene anim_madame_pussylick4b_ep8 with dissolve
        pause
        scene anim_madame_pussylick5b_ep8 with dissolve
        pause
        jump ep8_madame_pussylick_loop_label
    "Doggy (Ass)":
        scene anim_madame_asslick1_ep8 with dissolve
        md "Hey, now... That's not my pussy..."
        mc "*{i}Lick lick{/i}*"
        md "Haha... Ok. Anything for a valued customer. Go ahead, dear."
        pause
        scene anim_madame_pussylick3_ep8 with dissolve
        pause
        scene anim_madame_asslick2_ep8 with dissolve
        md "Mmm... Do you like sticking your tongue in my asshole?"
        pause
        jump ep8_madame_pussylick_loop_label
    "Missionary (Finger ass)":
        scene anim_madame_pussylick4_ep8 with dissolve
        md "You're such a dirty boy... Sticking your finger in my asshole like that."
        pause
        scene anim_madame_pussylick5_ep8 with dissolve
        pause
        jump ep8_madame_pussylick_loop_label
    "Continue":
        md "Thank you, dear. I enjoyed your tongue; we'll have to do that again sometime."
$ renpy.jump(currentEvent)

label ep7_madame_dance1_label:
mc "Can you dance for me?"
scene ep7_madame_dance1 with dissolve
$ renpy.pause(13)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
$ renpy.jump(currentEvent)

label ep7_madame_buy_groping_label:
$ renpy.block_rollback()
$ mny(-1)
$ ep7_madame_options_list[1][0] = "Groping"
hide screen newmoneymsg
mc "If I wanted to touch you, how much would that be?"
scene ep7_madame_16 with dissolve
md "It depends on what you mean by touching, love."
scene anim_madame_main_ep7 with dissolve
mc "You know, to squeeze your tits a bit."
scene ep7_madame_16 with dissolve
md "For that, I think {color=#36ca2b}${/color} is enough."
scene anim_madame_main_ep7 with dissolve
mc "Ok. Let's do that."
jump ep7_madame_groping_label
label ep7_madame_groping_label:
scene ep8_madame_groping with dissolve
md "Some oil will make this better..."
scene ep7_madame_groping1 with dissolve
md "There we go. Enjoy it, love."
scene ep7_madame_grope with dissolve
md "Mmm..."
scene anim_madame_grope1_ep8 with dissolve
mc "(They're so big! I can't even fit them in my hands.)"
mc "(I'm no expert...but I think they're real, too.)"
pause
scene ep8_madame_grope2 with dissolve
mc "(Shiiit...)"
scene anim_madame_grope2_ep7 with dissolve
mc "(I'm getting hard... I like how she's grinding me at the same time...)"
pause
scene ep8_madame_groping2 with dissolve
md "Perhaps you'd like to see what you're feeling?"
scene anim_madame_grope3_ep8 with dissolve
md "Do you like them, honey?"
mc "Yeah, I was thinking how great they are."
md "Aren't you sweet? You don't have to keep those thoughts to yourself."
md "Share with me when you get a dirty thought, and I think this will be even more enjoyable for you."
mc "Ok."
pause
scene anim_madame_grope4_ep7 with dissolve
mc "I think these are the biggest ones I've felt."
pause
scene anim_madame_grope5_ep7 with dissolve
md "*{i}Gasp{/i}* Oh, my... You're playful... I like this."
mc "I won't be too rough with you."
md "Don't worry, honey. I'm usually the one who sets those limits."
md "I think you got your money's worth."
pause
scene ep8_madame_groping3 with dissolve
md "Oh, I thought we were done..."
scene anim_madame_grope6_ep7 with dissolve
md "Ok, touch it a little bit."
pause
$ renpy.jump(currentEvent)

label ep7_madame_buy_suck_tits_label:
$ renpy.block_rollback()
$ mny(-3)
$ ep7_madame_options_list[1][1] = "Suck tits"
hide screen newmoneymsg
mc "I'd love to suck on your tits."
scene ep7_madame_16 with dissolve
md "Of course, love. I think {color=#36ca2b}$$${/color} is a reasonable price for that."
jump ep7_madame_suck_tits_label
label ep7_madame_suck_tits_label:
scene ep8_madame_buy_suck_tits with dissolve
md "There we go... Nice and oily for you."
md "Now, let [madame] feel your lips around her nipples."
scene anim_madame_tits_ep8 with dissolve
md "Yes... Like that. How gentle you are with [madame]."
pause
scene anim_madame_tits2_ep8 with dissolve
mc "*{i}Suck suck{/i}*"
md "You seem to be enjoying yourself. That's good. Take your time with it."
pause
scene anim_madame_tits3_ep8 with dissolve
md "Mmm..."
md "You can lick them if you want, love."
pause
scene anim_madame_tits4_ep8 with dissolve
mc "*{i}Lick lick{/i}*"
md "That's such a hot look, and it's nice to see that you know how to use your tongue."
pause
scene anim_madame_tits5_ep8 with dissolve
pause
$ renpy.jump(currentEvent)

label ep7_madame_buy_bj_label:
$ renpy.block_rollback()
$ mny(-4)
$ ep7_madame_options_list[2][0] = "Blowjob"
hide screen newmoneymsg
mc "Can I buy a blowjob from you?"
scene ep7_madame_16 with dissolve
md "I think you should. It's almost as if my lips were made for sucking on your dick, [name]."
md "I'll give you special treatment for {color=#36ca2b}$$$${/color}."
md "Don't be deterred by the price. I assure you that you'll get an unforgettable experience."
jump ep7_madame_bj_label
label ep7_madame_bj_label:
scene ep7_madame_bj with dissolve
$ renpy.pause()
scene ep7_madame_bj2 with dissolve
$ renpy.pause()
scene ep7_madame_bj3 with dissolve
md "Come here."
scene ep7_madame_bj4 with dissolve
md "Go ahead, honey."
scene ep7_madame_bj5 with dissolve
mc "You want me to pull it out?"
scene ep7_madame_bj4 with dissolve
md "Oh, yes. Remove your clothes."
scene ep7_madame_bj6 with dissolve
md "[madame] is hungry..."
scene anim_madame_bj1_ep8 with dissolve
md "*{i}Glug glug{/i}*"
pause
scene anim_madame_bj2_ep7 with dissolve
mc "Wow... It feels great. I'm amazed you can hold that position for so long."
pause
scene anim_madame_bj3_ep7 with dissolve
md "*{i}Suck schlurp{/i}*"
pause
scene ep7_madame_bj4 with dissolve
md "*{i}Phew{/i}* Ok... I think that's it for the pole."
scene ep7_madame_bj7 with dissolve
md "But don't fool yourself; I'm not done. That was just the start."
md "Lie down here, honey. It's time to show you my special technique."
scene anim_madame_lick_ep7 with dissolve
md "*{i}Lick lick{/i}* [madame]'s mouth will make you lose control."
mc "I'm sure it will..."
pause
scene anim_madame_bj4_ep7 with dissolve
md "*{i}Suck suck{/i}*"
mc "Mmm... You know how to do that, for sure..."
pause
scene ep7_madame_bj8 with dissolve
md "Here we go, love... Enjoy this..."
scene anim_madame_bj5_ep7 with dissolve
md "*{i}Suck glug{/i}*"
pause
scene anim_madame_bj6_ep7 with dissolve
mc "I'm getting close..."
md "*{i}Suck suck{/i}* Mpfhh..."
mc "Shit... Do you want me to cum inside or not?"
md "*{i}Glug glug{/i}*"
pause
mc "Ok... I'm fucking cumming, [madame]!"
menu:
    "Cum in mouth":
        scene ep7_madame_bj9 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep7_madame_bj9 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep7_madame_bj9 at vpunch, cum1
        mc "Ah... Shit, I can't stop!"
        scene ep7_madame_bj9 at vpunch, cum1
        $ renpy.pause(0.5)
        scene ep7_madame_bj9 at vpunch, cum1
        mc "Wow! That kept going..."
        scene ep7_madame_bj10 with dissolve
        md "You did good, honey."
        scene ep7_madame_bj11 with dissolve
    "Cum on face":
        scene ep7_madame_bj12 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep7_madame_bj12 at vpunch, cum2
        $ renpy.pause(0.5)
        scene ep7_madame_bj12 at vpunch, cum2
        $ renpy.pause()
        scene ep7_madame_bj13 with dissolve
        md "Haha, I'll need to replace my mask, I think. You did good, honey."
        scene ep7_madame_bj14 with dissolve
mc "Me? You're the one who did good. No, not good... Great! I loved it."
$ renpy.jump(currentEvent)

image anim_madame_assjob1_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob1_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob1_ep8_start", channel = "sex1")
image anim_madame_assjob2_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob2_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob2_ep8_start", channel = "sex2")
image anim_madame_assjob3_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob3_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob3_ep8_start", channel = "sex3")
image anim_madame_assjob4_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob4_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob4_ep8_start", channel = "sex4")
image anim_madame_assjob5_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob5_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob5_ep8_start", channel = "sex5")
image anim_madame_assjob5b_ep8 = Movie(play="%s/movies/ep8/anim_madame_assjob5b_ep8.webm" % persistent.img_dir, start_image="anim_madame_assjob5b_ep8_start", channel = "sex6")
image anim_madame_bj1_ep8 = Movie(play="%s/movies/ep8/anim_madame_bj1_ep8.webm" % persistent.img_dir, start_image="anim_madame_bj1_ep8_start", channel = "sex7")
image anim_madame_grope1_ep8 = Movie(play="%s/movies/ep8/anim_madame_grope1_ep8.webm" % persistent.img_dir, start_image="anim_madame_grope1_ep8_start", channel = "sex8")
image anim_madame_grope3_ep8 = Movie(play="%s/movies/ep8/anim_madame_grope3_ep8.webm" % persistent.img_dir, start_image="anim_madame_grope3_ep8_start", channel = "sex9")
image anim_madame_tits_ep8 = Movie(play="%s/movies/ep8/anim_madame_tits_ep8.webm" % persistent.img_dir, start_image="anim_madame_tits_ep8_start", channel = "sex10")
image anim_madame_tits2_ep8 = Movie(play="%s/movies/ep8/anim_madame_tits2_ep8.webm" % persistent.img_dir, start_image="anim_madame_tits2_ep8_start", channel = "sex11")
image anim_madame_tits3_ep8 = Movie(play="%s/movies/ep8/anim_madame_tits3_ep8.webm" % persistent.img_dir, start_image="anim_madame_tits3_ep8_start", channel = "sex12")
image anim_madame_tits4_ep8 = Movie(play="%s/movies/ep8/anim_madame_tits4_ep8.webm" % persistent.img_dir, start_image="anim_madame_tits4_ep8_start", channel = "sex13")
image anim_madame_tits5_ep8 = Movie(play="%s/movies/ep8/anim_madame_tits5_ep8.webm" % persistent.img_dir, start_image="anim_madame_tits5_ep8_start", channel = "sex14")
image anim_madame_pussylick1_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick1_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick1_ep8_start", channel = "sex15")
image anim_madame_pussylick2_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick2_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick2_ep8_start", channel = "sex16")
image anim_madame_pussylick3_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick3_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick3_ep8_start", channel = "sex17")
image anim_madame_pussylick4_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick4_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick4_ep8_start", channel = "sex18")
image anim_madame_pussylick5_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick5_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick5_ep8_start", channel = "sex19")
image anim_madame_pussylick4b_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick4b_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick4b_ep8_start", channel = "sex20")
image anim_madame_pussylick5b_ep8 = Movie(play="%s/movies/ep8/anim_madame_pussylick5b_ep8.webm" % persistent.img_dir, start_image="anim_madame_pussylick5b_ep8_start", channel = "sex1")
image anim_madame_asslick1_ep8 = Movie(play="%s/movies/ep8/anim_madame_asslick1_ep8.webm" % persistent.img_dir, start_image="anim_madame_asslick1_ep8_start", channel = "sex2")
image anim_madame_asslick2_ep8 = Movie(play="%s/movies/ep8/anim_madame_asslick2_ep8.webm" % persistent.img_dir, start_image="anim_madame_asslick2_ep8_start", channel = "sex3")
image anim_madame_main_ep7 = Movie(play="%s/movies/ep7/anim_madame_main_ep7.webm" % persistent.img_dir,start_image="ep7_madame_main_start", channel = "sex4")
image anim_madame_bj2_ep7 = Movie(play="%s/movies/ep7/anim_madame_bj2_ep7.webm" % persistent.img_dir, start_image="anim_madame_bj2_ep7_start", channel = "sex5")
image anim_madame_bj3_ep7 = Movie(play="%s/movies/ep7/anim_madame_bj3_ep7.webm" % persistent.img_dir, start_image="anim_madame_bj3_ep7_start", channel = "sex6")
image anim_madame_bj4_ep7 = Movie(play="%s/movies/ep7/anim_madame_bj4_ep7.webm" % persistent.img_dir, start_image="anim_madame_bj4_ep7_start", channel = "sex7")
image anim_madame_bj5_ep7 = Movie(play="%s/movies/ep7/anim_madame_bj5_ep7.webm" % persistent.img_dir, start_image="anim_madame_bj5_ep7_start", channel = "sex8")
image anim_madame_bj6_ep7 = Movie(play="%s/movies/ep7/anim_madame_bj6_ep7.webm" % persistent.img_dir, start_image="anim_madame_bj6_ep7_start", channel = "sex9")
image anim_madame_lick_ep7 = Movie(play="%s/movies/ep7/anim_madame_lick_ep7.webm" % persistent.img_dir, start_image="anim_madame_lick_ep7_start", channel = "sex10")
image anim_madame_grope2_ep7 = Movie(play="%s/movies/ep7/anim_madame_grope2_ep7.webm" % persistent.img_dir, start_image="anim_madame_grope2_ep7_start", channel = "sex11")
image anim_madame_grope4_ep7 = Movie(play="%s/movies/ep7/anim_madame_grope4_ep7.webm" % persistent.img_dir, start_image="anim_madame_grope4_ep7_start", channel = "sex12")
image anim_madame_grope5_ep7 = Movie(play="%s/movies/ep7/anim_madame_grope5_ep7.webm" % persistent.img_dir, start_image="anim_madame_grope5_ep7_start", channel = "sex13")
image anim_madame_grope6_ep7 = Movie(play="%s/movies/ep7/anim_madame_grope6_ep7.webm" % persistent.img_dir, start_image="anim_madame_grope6_ep7_start", channel = "sex14")


image ep7_madame_dance1:
    "ep7_madame_dance1_fr1" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr2" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr3" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr4" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr5" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr6" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr7" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr8" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr9" with Dissolve(0.2, alpha=True)
    pause 5
    "ep7_madame_dance1_fr10" with Dissolve(0.2, alpha=True)
    pause 5
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label ep12_freeroam_room2_label:
play music "music/ep7/licensed_music/track50.mp3"
show screen new_phone_screen
if branchJill:
    scene ep12_mc_rio_room1j with dissolve
else:
    scene ep12_mc_rio_room1 with dissolve
$ renpy.pause()
scene ep12_mc_rio_room2 with dissolve
$ renpy.pause()
scene ep12_mc_rio_room3 with dissolve
$ renpy.pause()
scene ep12_mc_rio_room4 with dissolve
$ renpy.pause()
scene ep12_mc_rio_room5 with dissolve
mc "Does it hurt?"
scene ep12_mc_rio_room6 with dissolve
ri "It used to hurt, but it reached a point where it looks worse than it feels."
ri "How bad does it look to you?"
scene ep12_mc_rio_room5 with dissolve
menu:
    "It doesn't look great":
        mc "It doesn't look great. I can tell you've been through some trauma."
        scene ep12_mc_rio_room6 with dissolve
        ri "Yeah. It's tough hiding it from people. There's only so much I can cover up with my hair."
    "You're still pretty":
        mc "You're still pretty."
        scene ep12_mc_rio_room6 with dissolve
        ri "There's no need to lie, [name]."
scene ep12_mc_rio_room5 with dissolve
mc "What happened to you?"
if ep10_quinn_help:
    scene ep12_mc_rio_room7 with dissolve
    ri "I thought Quinn already told you everything."
    scene ep12_mc_rio_room8 with dissolve
    mc "I heard her side of the story. Now, I want to hear it from you."
scene ep12_mc_rio_room7 with dissolve
ri "It's been hell."
ri "I keep having nightmares about that night."
scene ep12_mc_rio_room9 with dissolve
ri "How they abducted me. Forced me to tell everything about Quinn."
ri "And even after I did..."
scene ep12_mc_rio_room10 with dissolve
ri "They wanted to make sure I wasn't lying."
scene ep12_mc_rio_room11 with dissolve
ri "Buddy had a pair of pliers. And he..."
ri "He ripped the piercings out. One by one."
scene ep12_mc_rio_room12 with dissolve
ri "The septum piercing hurt like hell."
ri "I'm thankful he didn't spot my tongue piercing."
scene bg anim_rio_tongue_ep12 movie with dissolve
ri "I removed it after I got back to Mom's place."
pause
scene ep12_mc_rio_room5 with dissolve
mc "Rio... I can't imagine what you went through."
scene ep12_mc_rio_room13 with dissolve
$ renpy.pause()
scene ep12_mc_rio_room5 with dissolve
mc "Why didn't you go to the police?"
scene ep12_mc_rio_room14 with dissolve
ri "And say what? \"The drug dealers whose drugs I've been selling roughed me up.\""
ri "It would have made things worse for me. And that's why I didn't even go to the hospital."
scene ep12_mc_rio_room15 with dissolve
ri "I've been scared about what they would do to Mom if they found out I told anyone. They threatened her, too."
ri "This is all Quinn's fault."
scene ep12_mc_rio_room16 with dissolve
ri "I want to make her pay so fucking bad for what she's done to me, but I don't know how."
scene ep12_mc_rio_room17 with dissolve
mc "What was her part in this?"
scene ep12_mc_rio_room18 with dissolve
ri "We sold the drugs Buddy provided at a higher price and pocketed the profit."
ri "It was Quinn's idea, and she reassured me that I was safe."
scene ep12_mc_rio_room14 with dissolve
ri "She told me they didn't even know about me, but she was wrong. "
ri "They were watching me, and I got to pay the price that was hers to pay."
scene ep12_mc_rio_room15 with dissolve
ri "She has lied to me so many times that I've lost count."
ri "She thought she had it all under control and refused to listen to me when I told her we should calm down and not take risks."
scene ep12_mc_rio_room16 with dissolve
ri "If she only had stopped thinking about money for one fucking minute..."
scene ep12_mc_rio_room19 with dissolve
ri "I don't know what to do now, [name]."
scene ep12_mc_rio_room20 with dissolve
mc "Rio... I wish I could help you."
scene ep12_mc_rio_room19 with dissolve
ri "I'm waiting things out now. Waiting for the scars to heal so I can show my face again."
ri "I asked the dean for another shot at the finals because I didn't study for them, and I can't show up looking like this."
scene ep12_mc_rio_room21 with dissolve
ri "He will arrange for me to take the tests in January. But I don't think that's enough time to fully heal."
ri "I will have to face my friends looking like this. And I won't be able to answer their questions without lying."
scene ep12_mc_rio_room19 with dissolve
ri "What would the lie even be? I..."
scene ep12_mc_rio_room20 with dissolve
mc "They will be concerned, but what happened to you is private if you want it to be."
scene ep12_mc_rio_room21 with dissolve
ri "You won't tell anyone about this, right?"
scene ep12_mc_rio_room22 with dissolve
mc "I can keep this a secret if that's what you're asking."
scene ep12_mc_rio_room23 with dissolve
ri "Thank you, [name]."
if ep10_quinn_help:
    ri "Did Quinn tell you anything else?"
    scene ep12_mc_rio_room22 with dissolve
    mc "She seemed remorseful."
else:
    ri "Have you talked to Quinn?"
    scene ep12_mc_rio_room22 with dissolve
    if branchAlone:
        mc "Not about this. She has seemed distant lately. Now I get why."
    else:
        mc "We don't talk that much, but she's seemed distant lately."
mc "Have you talked to her?"
scene ep12_mc_rio_room24 with dissolve
ri "She showed up at my mom's place after it happened and tried to apologize, but I punched her in her stupid face."
ri "And I told her I didn't want to see her again. That was the last time I saw her."
scene ep12_mc_rio_room25 with dissolve
mc "Do you think you'll eventually talk it out with her?"
scene ep12_mc_rio_room24 with dissolve
ri "Well, I can't fucking avoid her, can I?"
ri "She lives in the same house as me."
scene ep12_mc_rio_room26 with dissolve
ri "And I can't do anything about it, because I'll be in trouble if I do."
ri "My hands are tied..."
if branchJill:
    scene ep12_mc_rio_room27j with dissolve
else:
    scene ep12_mc_rio_room27 with dissolve
ri "My only two options are to suck it up or drop out of college."
ri "But I don't want to drop out. I want to stay here."
scene ep12_mc_rio_room28 with dissolve
ri "But I don't want to stay near her!"
scene ep12_mc_rio_room29 with dissolve
mc "What if you got yourself a dorm?"
scene ep12_mc_rio_room30 with dissolve
ri "I feel like that would start drama. What do you think I should do?"
scene ep12_mc_rio_room29 with dissolve
if ep10_quinn_help:
    if not wt_ep11_quinn_riona_question_fix:
        "scrappy" "In episode 11 the result of a dialogue option weren't yet known but one leads to Quinn path and the other is a possible Riona path. So here's a quick fix check for it."
        menu:
           "Answer for Quinn's path":
              $ ep11_quinn_question[1] =True
           "Answer for possible Riona's path":
              $ ep11_quinn_question[1]=False
           "Both":
              $ wt_ep11_quinn_riona_question=True
    if ep11_quinn_question[1]:
        mc "I think you should talk to Quinn again. Even though she's done you wrong, I don't think it was intentional."
        scene ep12_mc_rio_room31 with dissolve
        ri "Did she tell you to say that?"
        scene ep12_mc_rio_room37 with dissolve
        mc "No. I think she's self-sabotaging because of the life she's lived. But I saw something in her..."
        mc "I think she deeply regrets what she did to you, but doesn't know how to change."
        scene ep12_mc_rio_room32 with dissolve
        mc "Maybe if you helped her, she'd have an easier time with it."
        label ep12_freeroam_room2c_label:
        $ ep12_riona_side = "Quinn"
        scene ep12_mc_rio_room33 with dissolve
        ri "You can't be serious, [name]! Look at what she's done to me."
        ri "There's no chance in hell that I'll patch things up with her after this."
        ri "Stop trying to defend her."
        scene ep12_mc_rio_room32 with dissolve
        mc "I'm sorry, Rio. I didn't mean to upset you."
        scene ep12_mc_rio_room34 with dissolve
        ri "*{i}Sigh{/i}*"
        ri "Sometimes you have to draw a line and stick to it. I should have done that a long time ago, but I kept cutting her slack."
        ri "I won't let it happen again."
        scene ep12_mc_rio_room32 with dissolve
        mc "I hear you."
        scene ep12_mc_rio_room35 with dissolve
        $ renpy.pause()
        scene ep12_mc_rio_room36 with dissolve
        ri "I'm gonna head out."
        scene ep12_mc_rio_room37 with dissolve
        mc "Right... You know how to find me. Call, text, visit...whenever you need it."
        stop music fadeout 3
        scene ep12_mc_rio_room38 with dissolve
        $ renpy.pause()
    else:
        mc "I think you should do what you feel is right. I will support whatever you choose, regardless."
        scene ep12_mc_rio_room37 with dissolve
        mc "Like I told Quinn, I can't defend her actions."
        mc "It made me sick hearing what she put you through."
        if branchJill:
            scene ep12_mc_rio_room39j with dissolve
        else:
            scene ep12_mc_rio_room39 with dissolve
        mc "And I think you're better off without her."
        label ep12_freeroam_room2b_label:
        $ ep12_riona_side = "Riona"
        if branchJill:
            scene ep12_mc_rio_room40j with dissolve
        else:
            scene ep12_mc_rio_room40 with dissolve
        ri "So, I'm not crazy for thinking that."
        ri "*{i}Sigh{/i}* Thank you, [name]."
        scene ep12_mc_rio_room41 with dissolve
        $ renpy.pause()
        scene ep12_mc_rio_room42 with dissolve
        mc "Wanna stay for a while? I'll help you take your mind off things."
        scene ep12_mc_rio_room43 with dissolve
        ri "All I've done lately is stay in bed all day."
        ri "I could use some normality."
        stop music fadeout 3
        scene ep12_mc_rio_room44 with dissolve
        mc "You got it. Stay for as long as you'd like."
else:
    menu:
        "Patch it up with Quinn":
            mc "I think you should try to patch it up with Quinn."
            scene ep12_mc_rio_room31 with dissolve
            ri "Did she tell you to say that?"
            scene ep12_mc_rio_room37 with dissolve
            mc "No. But I have a hard time believing she did this on purpose."
            mc "You said she tried to apologize. Maybe you could hear her out."
            jump ep12_freeroam_room2c_label
        "[m_c1]Stay away from Quinn":
            if branchJill:
                scene ep12_mc_rio_room39j with dissolve
            else:
                scene ep12_mc_rio_room39 with dissolve
            mc "I think you're better off without Quinn in your life."
            jump ep12_freeroam_room2b_label
if ep12_riona_side == "Quinn":
    $ new_bio("Riona", "Riona told me what happened to her, and I tried to nudge her toward patching things up with Quinn. She didn't like that.")
else:
    $ new_bio("Riona", "Riona told me what happened to her, and I told her she should stay away from Quinn. Riona was relieved that I saw it her way.")
jump ep12_fr_room2_setup_label

label ep12_fr2_rio_talk_label:
scene ep12_fr2_rio_talk1 with dissolve
mc "Can I get you anything?"
scene ep12_fr2_rio_talk3 with dissolve
ri "No, I feel like lying on your couch for a while."
scene ep12_fr2_rio_talk4 with dissolve
mc "Are you tired? I can get you a blanket."
scene ep12_fr2_rio_talk3 with dissolve
ri "Tired? I'm exhausted, but I can't get more than a few hours of sleep every night."
scene ep12_fr2_rio_talk5 with dissolve
ri "But I feel relaxed here."
ri "I think I've been worrying too much at Mom's place. Like, will they come back for me?"
scene ep12_fr2_rio_talk4 with dissolve
mc "Try not to think about that now. You're safe here."
scene ep12_fr2_rio_talk3 with dissolve
ri "Maybe I'll close my eyes for a second."
scene ep12_fr2_rio_talk1 with dissolve
mc "The bed is yours if you want it."
scene ep12_fr2_rio_talk2 with dissolve
ri "No, no... The couch is fine."
scene ep12_fr2_rio_talk1 with dissolve
$ renpy.pause()
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep12_fr2_td_label:
scene ep12_fr2_td1 with dissolve
mc "(So, Josy got contacted by TheDiane? Who even is that?)"
scene ep12_fr2_td3 with dissolve
mc "(Oh, ok... She seems like a big deal.)"
mc "(She's pretty hot.)"
mc "(I can see why Josy is excited about that.)"
mc "(Hm... A lingerie photoshoot?)"
mc "(It looks like this Diane chick is selling pictures of herself, too.)"
show screen newmoneymsg
menu:
    "Buy her photos {color=#36ca2b}$${/color}" if money > 1:
        scene ep12_fr2_td2 with dissolve
        hide screen newmoneymsg
        $ mny(-2)
        $ ep12_diane_pics = True
        mc "(It feels kind of creepy, but I wanna see her photos...)"
        $ mgallery_add_photo("ep12_diane1")
        $ mgallery_add_photo("ep12_diane2")
        $ mgallery_add_photo("ep12_diane3")
        $ mgallery_add_photo("ep12_diane4")
        $ mgallery_add_photo("ep12_diane5")
        $ mgallery_add_photo("ep12_diane6")
        $ mgallery_add_photo("ep12_diane7")
        $ specialMessage = "Photos added to your phone gallery!"
        show screen specialmsg
        pause
        hide screen specialmsg
        $ new_bio("Josy", "Josy was contacted by a famous blogger called TheDiane. I bought her lingerie photos.")
    "Don't do it":
        scene ep12_fr2_td2 with dissolve
        hide screen newmoneymsg
        mc "(But there's no way I would pay to see her in lingerie.)"
        $ new_bio("Josy", "Josy was contacted by a famous blogger called TheDiane. I didn't buy her lingerie photos.")

if branchMayaJosy and not breakup:
    jump ep12_fr_josy_chat_label
else:
    $ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep12_fr_josy_chat_label:
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
scene ep12_fr_josy_chat1 with dissolve
mc "(I wanna check up on Josy...)"

menu:
    "Remember me when you're famous":
        $ text_message_screen_list.append(["%s" % name,"Will you remember me when you're famous?",False])
        $ text_message_screen_list.append(["Josy","HAHA! I guess you saw the news. It's huge, isn't it?",True])
    "Congratulate her":
        $ text_message_screen_list.append(["%s" % name,"Congrats, Josy. I saw the big news! mphone_emoji_smile",False])
        $ text_message_screen_list.append(["Josy","THANKS!!! I'm so excited!!! It's friggin' huge!",True])

$ text_message_screen_list.append(["%s" % name,"I have to admit, I didn't know who TheDiane was, but I checked her page and she had a crazy number of followers.",False])
$ text_message_screen_list.append(["Josy","Have you and Maya lived under the same rock? She's like number one in the blogosphere. I mean, I guess it depends on what blogs you read, but she's number one on CB!",True])

hide screen new_phone_screen
play sound "sound_effects/interlude/zoey_message.mp3"
show screen text_message_screen
$ renpy.pause()

$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()

menu:
    "I don't read blogs":
        $ tmpInt2 = len(text_message_screen_list)
        hide screen text_message_screen
        $ text_message_screen_list.append(["%s" % name,"I don't read blogs, Josy. I barely read my DMs on Rooster. Anything that takes longer than a couple of sentences to say online is a waste of time.",False])
        $ text_message_screen_list.append(["Josy","Bah!!! I'm gonna show you some of TheDiane's posts. You'll see how much impact she has.",True])
    "Maya and I are rock people":
        $ tmpInt2 = len(text_message_screen_list)
        hide screen text_message_screen
        $ text_message_screen_list.append(["%s" % name,"Yep. Maya and I are rock people. She's indie rock, and I'm hard rock.",False])
        $ text_message_screen_list.append(["Josy","I'm gonna show you some of TheDiane's posts. You'll see how much impact she has.",True])

$ text_message_screen_list.append(["%s" % name,"I don't doubt it. You wrote she was going to feature you. What does that mean?",False])
$ tmpInt += 1
show screen text_message_screen
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()

if ep11_josy_solo or wt_ep11_maya_josy:
    $ text_message_screen_list.append(["Josy","Remember the winter photos you helped me shoot? She will use those in her blog.",True])
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)

    $ text_message_screen_list.append(["%s" % name,"Wow! That means I'm famous too.",False])
    $ text_message_screen_list.append(["Josy","HAHA! I guess it does!",True])
    $ text_message_screen_list.append(["%s" % name,"So, where do I send the invoice?",False])
    $ text_message_screen_list.append(["Josy","I'm not getting paid for this. If I were, I would give you a cut.",True])
    $ text_message_screen_list.append(["%s" % name,"I was joking anyway. Why isn't she paying you?",False])
    scene ep12_fr_josy_chat2 with dissolve
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
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)

    $ text_message_screen_list.append(["Josy","I'm getting paid in notoriety. You can't put a price on that.",True])
    $ text_message_screen_list.append(["%s" % name,"So, I was free labor all along...",False])
    $ text_message_screen_list.append(["Josy","You and Maya. She's helping me take pictures now.",True])
    $ text_message_screen_list.append(["%s" % name,"I work for free and I get fired? I suck.",False])
    $ text_message_screen_list.append(["Josy","No you don't suck. You did great! You can still take photos of me if you want. I didn't realize you wanted to.",True])


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
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)

    $ text_message_screen_list.append(["%s" % name,"It's cool. I'll always help you if you want my assistance, but I'm sure Maya will do a great job at it, too. Anyway, I hope the feature brings you success! mphone_emoji_heart",False])
    $ text_message_screen_list.append(["Josy","You're the best! mphone_emoji_heart",True])

    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
else:
    $ text_message_screen_list.append(["Josy","I took some photos of myself by the lake for my blog, and she will repost those on her page along with some other creators who're getting the same deal.",True])
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)

    $ text_message_screen_list.append(["Josy","She'll credit me and link my page. If people like what they see, they'll sign up for my blog and that will bring me both traffic and money.",True])
    $ text_message_screen_list.append(["%s" % name,"Hey, that's awesome! From just one post of TheDiane you could end up with an even bigger following.",False])
    $ text_message_screen_list.append(["Josy","I know! Isn't it great? mphone_emoji_laugh",True])
    $ text_message_screen_list.append(["%s" % name,"You're worth it! You should take some more photos for your blog then. To prepare for the influx of new subscribers.",False])
    scene ep12_fr_josy_chat2 with dissolve
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    hide screen text_message_screen
    $ tmpInt += 1
    $ tmpInt2 = len(text_message_screen_list)

    $ text_message_screen_list.append(["Josy","I'm already on it. Or, Maya is already on it, I should say. She's helping me take pictures now.",True])
    $ text_message_screen_list.append(["%s" % name,"I'm sure Maya will do a great job at it. Anyway, I hope the feature brings you success! mphone_emoji_heart",False])
    $ text_message_screen_list.append(["Josy","You're the best! mphone_emoji_heart",True])

    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
hide screen text_message_screen
hide screen text_message_screen
$ mphone_scene_to_chat("Josy",text_message_screen_list)

scene ep12_fr_josy_chat3 with dissolve
mc "(Good on Josy.)"
$ new_bio("Josy", "Josy told me about her collaboration with TheDiane. It seemed like a big deal for her.")

$ task_list[2] = ""
$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep12_fr2_cube_event_label:
scene ep12_fr2_cube_event1 with dissolve
mc "(Gah... I give up. This puzzle box was too hard.)"
mc "(Maybe someone can help me with it...)"
$ task_list[1] = ""
$ updateTaskList()
jump ep12_fr2_dlj_event_label

label ep12_fr2_dlj_event_label:
scene ep12_fr2_dlj_event6 with dissolve
mc "Hey, guys."
if not pb_completed:
    $ pb_derek_completed = True
    scene ep12_fr2_dlj_event7 with dissolve
    mc "Has anyone seen a box like this before? It's a puzzle box or something, but I can't open it."
    scene ep12_fr2_dlj_event8 with dissolve
    de "Gimme."
    scene ep12_fr2_dlj_event9 with dissolve
    mc "Do you think you can solve it?"
    scene ep12_fr2_dlj_event8 with dissolve
    de "I was a cuber when I was younger. I'll give it a crack."
scene ep12_fr2_dlj_event10 with dissolve
mc "What are you watching?"
scene ep12_fr2_dlj_event11 with dissolve
le "Some stupid movie. We're trying to unwind from today's exam."
scene ep12_fr2_dlj_event10 with dissolve
mc "How did it go?"
scene ep12_fr2_dlj_event12 with dissolve
jm "I'll probably have to retake it. Calculus kicked our asses."
scene bg anim_swype_ep12 movie with dissolve
le "Yeah, I'd be surprised if I passed it."
mc "That sucks to hear."
le "Your tests are on Friday, yeah?"

scene ep12_fr2_dlj_event13 with dissolve
mc "Yep. I feel like I'm done studying for them. I'm not gonna get better than this."
mc "It's been a rough week..."
if breakup or ep4_toldDerekAboutJade:
    mc "For many reasons."
scene ep12_fr2_dlj_event14 with dissolve
le "Wanna have some fun with us?"
scene ep12_fr2_dlj_event15 with dissolve
mc "Fun how?"
scene ep12_fr2_dlj_event14 with dissolve
le "Let's head to the Pink Rose tonight."
scene ep12_fr2_dlj_event16 with dissolve
jm "That's an awesome idea. I could go for a couple of tits in my face right about now."
if ep12_riona_side == "Riona":
    mc "(Hm... I gotta check with Rio about that.)"
if not pb_completed:
    scene ep12_fr2_dlj_event17 with dissolve
else:
    scene ep12_fr2_dlj_event17b with dissolve
le "Derek? Are you coming?"
if not pb_completed:
    scene ep12_fr2_dlj_event18 with dissolve
else:
    scene ep12_fr2_dlj_event18b with dissolve
de "Sure. I'm always up for it."
if pb_completed:
    if ep12_riona_side != "Riona":
        stop music fadeout 3
scene ep12_fr2_dlj_event13 with dissolve
mc "If you're all going... Fine, but let me get changed first."
if not pb_completed:
    play sound "sound_effects/season3/pb_open.mp3"
    scene ep12_fr2_dlj_event19 with dissolve
    de "[mc_de_up]. Catch."
    play sound "sound_effects/season3/pb_catch.mp3"
    scene ep12_fr2_dlj_event20
    mc "You solved it..."
    scene ep12_fr2_dlj_event21 with dissolve
    de "Yeah. It wasn't that hard."
    de "The box is empty, by the way."
    if ep12_riona_side != "Riona":
        stop music fadeout 3
    scene ep12_fr2_dlj_event20 with dissolve
    mc "There's nothing inside? What a waste..."

if ep12_riona_side == "Riona" or wt_ep11_quinn_riona_question:
    if branchJill:
        scene ep12_fr2_dlj_event5j with dissolve
    else:
        scene ep12_fr2_dlj_event5 with dissolve
    mc "Rio?"
    scene ep12_fr2_dlj_event1 with dissolve
    $ renpy.pause()
    scene ep12_fr2_dlj_event2 with dissolve
    mc "(All that stress she's been under must have taken its toll.)"
    scene ep12_fr2_dlj_event3 with dissolve
    $ renpy.pause()
    play sound "sound_effects/switch.mp3"
    stop music fadeout 3
    scene ep12_fr2_dlj_event4 with dissolve
    mc "Rest up, Rio."
jump ep12_pinkrose_label

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

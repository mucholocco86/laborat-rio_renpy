label ep10_fr1_jacob_event_label:
scene ep10_fr1_jacob_event1 with dissolve
jac "Cleaning blows..."
jac "Why did we have to go crazy with the spiderwebs?"
scene ep10_fr1_jacob_event2 with dissolve
mc "I'll take the spiderwebs if you clean the puke in the bathroom."
scene ep10_fr1_jacob_event1 with dissolve
jac "On second thought, I'm fine with cleaning the spiderwebs."
scene ep10_fr1_jacob_event7 with dissolve
le "Is Heather here?"
if not "ep10_fr1_josy_event_label" in event_list and ep9_jm_sad:
    scene ep10_fr1_jacob_event6b with dissolve
    sar "Nope. She's hungover like crazy today."
    scene ep10_fr1_jacob_event7b with dissolve
    le "I found this in my room. It's hers, right?"
    scene ep10_fr1_jacob_event3 with dissolve
    jac "Yeah, that's hers."
    scene ep10_fr1_jacob_event6b with dissolve
    sar "Leave it somewhere. She can pick it up later."
else:
    scene ep10_fr1_jacob_event4 with dissolve
    js "No, she came back home earlier this morning and went straight to bed. She didn't feel well."
    scene ep10_fr1_jacob_event7 with dissolve
    le "I found this in my room. It's hers, right?"
    scene ep10_fr1_jacob_event3 with dissolve
    jac "Yeah, that's hers."
    scene ep10_fr1_jacob_event4 with dissolve
    js "I can bring it back with me."
    scene ep10_fr1_jacob_event6 with dissolve
    sar "Is she not helping out at all with this? That's unfair as fuck."
    if "ep10_fr1_sage_event_label" in event_list:
        scene ep10_fr1_jacob_event5 with dissolve
        sa "Don't complain. I'll make sure that the HOTs who don't help out get to clean our house extra."
$ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_sarah_event_label:
scene ep10_fr1_sarah_event1 with dissolve
mc "Thanks for last night."
scene ep10_fr1_sarah_event2 with dissolve
sar "You would have thanked me for this morning too if it weren't for Mel."
scene ep10_fr1_sarah_event1 with dissolve
mc "What can I say? Early bird gets the worm."
scene ep10_fr1_sarah_event2 with dissolve
sar "Haha! Worm? More like snake."
scene ep10_fr1_sarah_event3 with dissolve
mc "Maybe next time you'll get it."
scene ep10_fr1_sarah_event4 with dissolve
sar "I'm not inviting Mel for it. That's for sure."
$ optional_task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_flower_event_label:
$ ep8_flower_water_level = 2
$ optional_task_list[6] = ""
scene ep10_fr1_flower_event1 with dissolve
mc "(Look at that! They're blossoming.)"
play sound "sound_effects/watering.mp3"
scene ep10_fr1_flower_event2 with dissolve
mc "(The soil is getting dry. They need some more water.)"
jump endEvent

label ep10_fr1_flower_dead_event_label:
$ optional_task_list[6] = ""
scene ep10_fr1_flower_dead_event1 with dissolve
mc "(Damn... I forgot about my flower...)"
mc "(It looks pretty dead to me. Sorry, Jamie... I don't have green fingers.)"
jump endEvent

label ep10_fr1_tommy_event_label:
scene ep10_fr1_tommy_event1 with dissolve
tm "Get the fuck out of here, you sisterfucker!"
mc "Ok..."
jump endEvent

label ep10_fr1_tommy_event2_label:
scene ep10_fr1_tommy_event2 with dissolve
menu:
    "Tell him to help":
        mc "Are you taking a break while everyone else is working?"
        scene ep10_fr1_tommy_event3 with dissolve
        tm "I'm making sure people paid for the party, asshole. "
        scene ep10_fr1_tommy_event2 with dissolve
        mc "Oh... Sorry."
    "Ignore him":
        $ renpy.pause(0.5)

jump endEvent

label ep10_fr1_josy_event_label:
$ guideSuggestedPage = 100
if ep9_jm_sad:
    scene ep10_fr1_josy_event1 with dissolve
    $ renpy.pause()
    scene ep10_fr1_josy_event2 with dissolve
    mc "Josy?"
    mc "I'm so sorry-"
    scene ep10_fr1_josy_event3 with dissolve
    js "Don't."
    scene ep10_fr1_josy_event4 with dissolve
    mc "I never wanted to hurt you. And this hurts me, too. You should know that."
    scene ep10_fr1_josy_event5 with dissolve
    js "It...doesn't help. Not one bit."
    scene ep10_fr1_josy_event4 with dissolve
    mc "I don't want to lose you as a friend."
    scene ep10_fr1_josy_event3 with dissolve
    js "You're unbelievable."
    if branchSage:
        js "You dumped us to be with Sage without talking to us, without any notice or discussion whatsoever."
    elif branchJill:
        js "You dumped us to be with Jill without talking to us, without any notice or discussion whatsoever."
    else:
        js "You dumped us without talking to us, without any notice or discussion whatsoever."
    scene ep10_fr1_josy_event5 with dissolve
    js "And now you expect me to stay friends with you?"
    scene ep10_fr1_josy_event4 with dissolve
    mc "I tried to wait for a good moment to bring it up, but the longer I waited, I realized there wasn't one... And we said no strings attached, remember?"
    scene ep10_fr1_josy_event3 with dissolve
    js "It was Maya who said that. I never liked that idea, but you two seemed ok with it."
    js "Just because she was unsure and dating a guy was new to her, it didn't mean I felt the same about it."
    scene ep10_fr1_josy_event4 with dissolve
    mc "Why didn't you tell us that back then?"
    scene ep10_fr1_josy_event5 with dissolve
    js "For the same reason I went along with other things you said."
    js "I didn't want to upset you two, and I didn't think compromising would lead to...this."
    js "I thought it meant that Maya's emotions would be kept at bay until she felt ready."
    js "And for me, I already knew what I wanted... I..."
    scene ep10_fr1_josy_event6 with dissolve
    js "I wanted us."
    js "And you better fucking believe it... I wanted you."
    js "I want you so much it hurts."
    scene ep10_fr1_josy_event7 with dissolve
    js "*{i}Phew{/i}*"
    scene ep10_fr1_josy_event6 with dissolve
    js "And to go from being with you to having you as a friend..."
    if branchSage:
        js "Seeing you be happy with Sage..."
    elif branchJill:
        js "Seeing you be happy with Jill..."
    else:
        js "Seeing you be happy with someone else..."
    js "I do not want that."
    scene ep10_fr1_josy_event5 with dissolve
    js "And you thinking I'd be ok with it shows how clueless you are about me and my feelings."
    scene ep10_fr1_josy_event4 with dissolve
    menu:
        "Walk away":
            scene ep10_fr1_josy_event9 with dissolve
            mc "..."
        "Console her":
            scene ep10_fr1_josy_event8 with dissolve
            mc "Josy..."
            js "Don't."
            scene ep10_fr1_josy_event9 with dissolve
            $ renpy.pause()

    scene ep10_fr1_josy_event10 with dissolve
    el "Are you ok?"
    scene ep10_fr1_josy_event11 with dissolve
    js "I'm fine."
    scene ep10_fr1_josy_event12 with dissolve
    el "Come. Let's grab some fresh air together."
    el "The alcohol stench hurts my head."
    js "Ok..."
    $ new_bio("Josy", "Josy told me I was delusional for thinking she'd want to remain my friend after breaking up with her.")
elif branchMayaJosy:
    scene ep10_fr1_josy_event13 with dissolve
    mc "Are you still here?"
    scene ep10_fr1_josy_event14 with dissolve
    js "No. I went back to my room, but it was just in time to return here to clean."
    js "I can't skip it, can I?"
    scene ep10_fr1_josy_event13 with dissolve
    mc "I wouldn't blame you if you did. I've been looking over my shoulder for Tommy."
    scene ep10_fr1_josy_event15 with dissolve
    el "Aw."
    scene ep10_fr1_josy_event16 with dissolve
    mc "What's aw?"
    scene ep10_fr1_josy_event15 with dissolve
    el "I just wanted to tell you congratulations. I heard the news."
    scene ep10_fr1_josy_event17 with dissolve
    js "That didn't take long..."
    scene ep10_fr1_josy_event18 with dissolve
    el "Two girls, huh? What a stud."
    scene ep10_fr1_josy_event19 with dissolve
    mc "It's not that simple."
    scene ep10_fr1_josy_event20 with dissolve
    js "What can I say? We just had to have him."
    scene ep10_fr1_josy_event21 with dissolve
    el "More power to you."
    scene ep10_fr1_josy_event22 with dissolve
    js "Look. It's spreading already. You can't undo this by telling them it's not simple and such."
    js "You either have to own what you said or say that you lied and that it was just about sex."
    scene ep10_fr1_josy_event23 with dissolve
    mc "I'm sorry. I wasn't thinking clearly when I said we were in a relationship."
    if "ep10_fr1_jb_event_label" in event_list:
        mc "I thought the DIK secret code would be stronger than that..."
    else:
        mc "I thought the DIK secret code would be stronger than that... Apparently, it doesn't mean shit to Tommy."
    mc "I thought telling them about us would shift the focus from you two having sex to me being with two girls."
    scene ep10_fr1_josy_event24 with dissolve
    js "It did. It definitely did."
    js "But that doesn't make things perfect because it's not the entire truth."
    scene ep10_fr1_josy_event23 with dissolve
    mc "But we can't tell the truth; we have to lie about it."
    mc "At least this way, we don't have to sneak around in public."
    scene ep10_fr1_josy_event24 with dissolve
    js "It makes Maya and me look bad, though. Don't you think?"
    scene ep10_fr1_josy_event23 with dissolve
    mc "How?"
    scene ep10_fr1_josy_event24 with dissolve
    js "It's like we don't have integrity. We just \"had to have you\"."
    scene ep10_fr1_josy_event23 with dissolve
    mc "That's what {b}you{/b} told Elena."
    scene ep10_fr1_josy_event25 with dissolve
    js "Because that's what it looks like. That's the only way it can look without people knowing about Maya and me. Don't you get it?"
    scene ep10_fr1_josy_event23 with dissolve
    mc "*{i}Sigh{/i}* Yes..."
    scene ep10_fr1_josy_event24 with dissolve
    js "And that's one of the reasons it doesn't feel good for Maya in particular."
    js "She's also afraid that her dad will find out. I told her she didn't have to fear that."
    js "I mean, how would he figure it out? He doesn't know or talk to anyone on campus aside from Maya and Derek."
    scene ep10_fr1_josy_event23 with dissolve
    mc "I feel bad now."
    scene ep10_fr1_josy_event24 with dissolve
    js "You should talk to her about this."
    scene ep10_fr1_josy_event23 with dissolve
    mc "I will."
    scene ep10_fr1_josy_event26 with dissolve
    js "But don't feel too bad. It's scary that people know about it, but it's kinda good too."
    js "If it works out, we won't have to sneak around that much anymore."
    scene ep10_fr1_josy_event27 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Only with a few people":
            mc "You're right. We'd only have to be careful around a few people - like Tommy and Maya's dad."
            scene ep10_fr1_josy_event26 with dissolve
            js "Right."
        "Kiss her [m_c1][mod_choices[1]]":
            $ RPjosy += 1
            mc "Yeah. And I could do this in public, too."
            scene ep10_fr1_josy_event29 with dissolve
            mc "*{i}Smack{/i}*"
            scene ep10_fr1_josy_event28 with dissolve
            js "..."
    $ new_bio("Josy", "Josy tried to explain Maya's concerns about me telling everyone about our relationship. I felt stupid for not realizing it myself, but when I told Tommy and the rest about us, it felt like the smart solution to our problem.")
else:
    $ guideSuggestedPage = 101
    scene ep10_fr1_josy_event13 with dissolve
    mc "And I already miss it."
    scene ep10_fr1_josy_event14 with dissolve
    js "Miss what?"
    scene ep10_fr1_josy_event13 with dissolve
    mc "Your hair let loose."
    scene ep10_fr1_josy_event14 with dissolve
    js "When I woke up today, I looked like a big mess. I had to put it in a ponytail."
    scene ep10_fr1_josy_event30 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Pull it [m_c1][mod_choices[3]][m_c2][mod_choices[1]]":
            $ dk(1)
            $ RPjosy += 1
            mc "It's not bad; it means I can do this."
            scene bg anim_josy_pull_ep10 movie with dissolve
            js "Hey!"
            $ renpy.pause()
            scene ep10_fr1_josy_event32 with dissolve
            js "Damn you."
            scene ep10_fr1_josy_event33 with dissolve
            mc "Haha, sorry."
        "Don't pull it":
            mc "Well, you look great with that, too."
            scene ep10_fr1_josy_event31 with dissolve
            js "Thanks, [name]. But today, no one is looking great."
            js "We all look like we haven't slept for more than two hours."
    scene ep10_fr1_josy_event34 with dissolve
    mc "Thirsty?"
    scene ep10_fr1_josy_event35 with dissolve
    js "I can't even look at that without wanting to puke."
    js "I drank too many weird drinks yesterday."
    scene ep10_fr1_josy_event36 with dissolve
    mc "I'm amazed we still have some alcohol left, with how much people were drinking."
    scene ep10_fr1_josy_event37 with dissolve
    js "Leftover beer is good. You can save it for another one of your parties."
    scene ep10_fr1_josy_event36 with dissolve
    if affinity == "DIK":
        mc "Yeah, whenever that will happen."
        mc "Tomorrow, I have to get back into college mode..."
    else:
        mc "I don't want to think about planning another party yet."
        mc "Tomorrow, I'm back into college mode."
    scene ep10_fr1_josy_event37 with dissolve
    js "I'm starting to miss classes. Is that weird?"
    scene ep10_fr1_josy_event36 with dissolve
    mc "I'll tell you something I don't miss... Gender Studies."
    scene ep10_fr1_josy_event37 with dissolve
    js "Haha!"

$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_nick_event_label:
scene ep10_fr1_nick_event1 with dissolve
ni "Fuck..."
scene ep10_fr1_nick_event2 with dissolve
mc "What's wrong?"
scene ep10_fr1_nick_event3 with dissolve
ni "Some of the bottles leaked onto the tank, but hopefully not into it."
scene ep10_fr1_nick_event8 with dissolve
mc "Those fish don't look drunk to me."
scene ep10_fr1_nick_event3 with dissolve
ni "They would be dead, not drunk."
scene ep10_fr1_nick_event4 with dissolve
mc "From a little bit of beer?"
scene ep10_fr1_nick_event5 with dissolve
ni "I don't intend to find out how much beer will kill them. I'm trying to keep them alive."
if ep8_help_nick:
    ni "I remember you said you wanted to help out with it. Are you still interested?"
    scene ep10_fr1_nick_event4 with dissolve
    mc "Of course! What do you need me to do?"
    jump ep10_fish_intro_label
else:
    ni "I know you don't want to help out with it, but I could use a hand from someone... Can I change your mind somehow?"
    scene ep10_fr1_nick_event4 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-DIKs)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "[mod_gr]Help out":
            $ ep8_help_nick = True
            mc "I mean...if you really need someone to help, I'll do it. But I thought you'd be able to take care of it by yourself."
            scene ep10_fr1_nick_event6 with dissolve
            ni "I thought I could, too, but it's a lot of work. And I don't think the fish are feeling well."
            scene ep10_fr1_nick_event4 with dissolve
            mc "What do you need me to do?"
            label ep10_fish_intro_label:
            scene ep10_fr1_nick_event6 with dissolve
            ni "I'm kind of a rookie when it comes to this. I thought it would be cool to have fish when I saw this tank among the stuff your dad brought us."
            ni "But I'm worried I don't have what it takes to take care of it."
            scene ep10_fr1_nick_event4 with dissolve
            mc "I thought you knew how to do it."
            scene ep10_fr1_nick_event6 with dissolve
            ni "Me and my sis had a smaller tank when I was younger and lived back home. But this one is next level."
            ni "It looks empty without any stuff in it. And I haven't bought an air pump yet."
            ni "The water looks kind of murky, too, and I think I've put too many fish in it."
            scene ep10_fr1_nick_event4 with dissolve
            mc "So, they'll die unless we do something about it?"
            scene ep10_fr1_nick_event6 with dissolve
            ni "Probably. It would be a horror show, so I want to do something about it before it's too late."
            ni "I read they can get diseases, too, unless they are taken care of properly."
            scene ep10_fr1_nick_event4 with dissolve
            mc "That sounds bad. How should we do it?"
            if minigames:
                $ quick_menu = False
                $ renpy.block_rollback()
                call screen fish_tank_screen
                $ renpy.pause(0.5)
                $ quick_menu = True
                $ renpy.block_rollback()
                scene ep10_fr1_nick_event5 with dissolve
                ni "Ok. Maybe that's good enough? I don't know. Check up on them whenever you want. You know where to find them."
                scene ep10_fr1_nick_event4 with dissolve
                mc "Great, I'll do that."
            else:
                $ ft_init_nm()
                $ ft_nm_new_round()
                scene ep10_fr1_nick_event5 with dissolve
                ni "How about this? If you help me feed them once or twice daily and help out with the expenses for equipment and stuff..."
                ni "And maybe help me clean the tank once in a while, then I'll fix the rest."

                $ renpy.block_rollback()
                scene ep10_fr1_nick_event8 with dissolve
                $ jumpLabel = "ep10_ft_nm_return1_label"
                jump ep10_ft_nm_label
                label ep10_ft_nm_return1_label:

                scene ep10_fr1_nick_event4 with dissolve
                mc "That sounds good to me. I'll make sure to check up on them and talk to you about what needs to be done."
                scene ep10_fr1_nick_event5 with dissolve
                ni "Thanks, bro."
        "Don't help out [m_c1][mod_choices[0]]":
            $ RPdiks -= 1
            $ ep8_help_nick = False
            mc "Sorry, but you should ask someone else. I wouldn't be of much help taking care of them."
            mc "Maybe Derek can help you? His room is right next to it anyway."
            scene ep10_fr1_nick_event6 with dissolve
            ni "Ok... I'll ask him instead."

if branchIsabella:
    scene ep10_fr1_nick_event7 with dissolve
    mc "By the way... Thanks for...um...that thing with Bella."
    scene ep10_fr1_nick_event5 with dissolve
    ni "With who?"
    scene ep10_fr1_nick_event4 with dissolve
    mc "Bella, you know, from my room earlier."
    scene ep10_fr1_nick_event5 with dissolve
    ni "Yeah, I know. I meant, \"with who?\" Get it?"
    scene ep10_fr1_nick_event7 with dissolve
    mc "Oh. Thanks. It means a lot."

if branchIsabella:
    mc "Oh, yeah... Another thing."
else:
    scene ep10_fr1_nick_event7 with dissolve
    mc "By the way..."
mc "Vinny was here last night."
scene ep10_fr1_nick_event6 with dissolve
ni "Yeah, I heard it from Tommy. I must have missed him."
scene ep10_fr1_nick_event7 with dissolve
mc "Oh. I thought it was you who invited him."
scene ep10_fr1_nick_event6 with dissolve
ni "No, it wasn't me. I was actually surprised that he showed up."
ni "He must have patched things up with Tommy when Tommy...uh..."
scene ep10_fr1_nick_event4 with dissolve
mc "When Tommy what?"
scene ep10_fr1_nick_event3 with dissolve
ni "Don't talk about this with people, but Tommy's buying weed from Vinny."
ni "Not that long ago, Tommy asked me to reach out to him about it."
scene ep10_fr1_nick_event6 with dissolve
ni "I guess that's why he showed up."
scene ep10_fr1_nick_event7 with dissolve
mc "I gotta say, I didn't think you'd be friends with someone like Vinny."
mc "I pictured him being different, but he's a real dick."
scene ep10_fr1_nick_event6 with dissolve
ni "Did something happen?"
scene ep10_fr1_nick_event4 with dissolve
mc "He provoked me, and we had an altercation."
scene ep10_fr1_nick_event3 with dissolve
ni "Oh... He does have a short fuse."
scene ep10_fr1_nick_event4 with dissolve
mc "You can say that again. He was being a complete asshole to me for no reason."
scene ep10_fr1_nick_event6 with dissolve
ni "That sucks to hear. Vinny's always been difficult, but he's changed a lot for the worse lately."
ni "But I don't think you have to worry about him being around much."
ni "Even if he patched things up with Tommy, he's got another life going for him these days, and even I rarely see him."
scene ep10_fr1_nick_event7 with dissolve
mc "Right. Anyway, thanks for the talk."

$ new_bio("Nick", "I talked to Nick about Vinny being at our Halloween party, but he didn't know he'd been there until Tommy had mentioned it.")
$ mphone_stats_unlocked_state = 2
$ task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_sage_event_label:
$ guideSuggestedPage = 101
scene ep10_fr1_sage_event1 with dissolve
sa "And here we are... In the aftermath of a bitching party."
sa "You can tell how fun it was by all the crap we have to clean."
scene ep10_fr1_sage_event2 with dissolve
mc "I'm happy you girls are here helping out."
scene ep10_fr1_sage_event1 with dissolve
sa "Of course, dude."
if branchSage:
    scene ep10_fr1_sage_event3 with dissolve
    sa "What are you up to later?"
    scene ep10_fr1_sage_event4 with dissolve
    mc "Today? Nothing. Nothing at all. I think I'm gonna rest after this."
    scene ep10_fr1_sage_event3 with dissolve
    sa "If you wanna rest together, you can join me."
    sa "How about some slow music and lying on the bed together?"
    scene ep10_fr1_sage_event4 with dissolve
    mc "That sounds like a great evening."
    scene ep10_fr1_sage_event5 with dissolve
    $ renpy.pause()
    if ep9_jm_sad:
        scene ep10_fr1_sage_event6 with dissolve
        $ renpy.pause()
        scene ep10_fr1_sage_event7 with dissolve
        $ renpy.pause()
    else:
        scene ep10_fr1_sage_event6 with dissolve
        $ renpy.pause()
stop music fadeout 3
scene ep10_fr1_sage_event8 with dissolve
jac "Um... [name]!"
scene ep10_fr1_sage_event9 with dissolve
play music "music/ep5/licensed_music/track12.mp3"
if affinity == "DIK":
    mc "Who the fuck let you guys in?"
else:
    mc "What are you doing here?"
mc "Jacob, get the bros."
scene ep10_fr1_sage_event10 with dissolve
dw "We're gonna talk about what happened yesterday. We are PISSED OFF!"
scene ep10_fr1_sage_event11 with dissolve
sa "Don't start anything! We will talk, but not all of us. You know what this will lead to."
scene ep10_fr1_sage_event12 with dissolve
tm "Get the fuck out of here!"
scene ep10_fr1_sage_event13 with dissolve
sa "Everyone, relax!"
sa "Vice presidents and presidents only. The rest of you leave and tell Quinn to get her ass in here."
scene ep10_fr1_sage_event14 with dissolve
rs "We don't want these guys in here at all. We're not letting them trash our home again."
scene ep10_fr1_sage_event17 with dissolve
dw "I don't know what you're talking about. It wasn't a tri-alpha who did it."
scene ep10_fr1_sage_event15 with dissolve
tm "Wipe that smug fucking look off your face. We know it was you."
scene ep10_fr1_sage_event17 with dissolve
dw "I dare you to accuse Caleb of it. He's not a tri-alpha or bound by our rules."
scene ep10_fr1_sage_event15 with dissolve
tm "Aha, so that's how you're gonna do it? That shit might fly with the counselors, but it's not gonna work on us."
scene ep10_fr1_sage_event16 with dissolve
sa "Pipe down. Let's sit down and have a talk somewhere. Rusty? A little help?"
scene ep10_fr1_sage_event14 with dissolve
rs "Let's be civil, for once. We can talk in my room."

show ep10_fr1_alphas_event1
if not persistent.ep10_cardzo3:
    show screen ep10_render_screen("zo3")
with dissolve
dw "Are you gonna tell us what's up, or will you lie to our faces again?"
show ep10_fr1_alphas_event2
hide screen ep10_render_screen
with dissolve
sa "No one is lying to you. Yes, we had a Halloween party here yesterday, and for obvious reasons, you weren't invited."
scene ep10_fr1_alphas_event11 with dissolve
dw "And you tricked us into going on Arieth's road trip to get rid of us. Admit it."
scene ep10_fr1_alphas_event3 with dissolve
sa "Quinn?"
scene ep10_fr1_alphas_event4 with dissolve
qu "If you are stupid enough to fall for it, you deserve it."
scene ep10_fr1_alphas_event5 with dissolve
sa "Quinn!"
scene ep10_fr1_alphas_event11 with dissolve
dw "I knew it!"
scene ep10_fr1_alphas_event4 with dissolve
qu "I don't get why we're tiptoeing around this at this point. You know we party with the DIKs."
scene ep10_fr1_alphas_event11 with dissolve
dw "There are traditions between the tri-alphas and the HOTs that you can't shit on like that!"
dw "The HOTs have always been our sorority. End of story!"
scene ep10_fr1_alphas_event8 with dissolve
tm "And now they aren't. Fucking deal with it!"
scene ep10_fr1_alphas_event13 with dissolve
dw "I'm gonna deal with your face!"
scene ep10_fr1_alphas_event2 with dissolve
sa "Calm down!"
sa "We wanted to do this in a civil manner, didn't we?"
sa "Civil. As in no more fights. No more ruined properties and removed presidents. Right?"
scene ep10_fr1_alphas_event11 with dissolve
dw "You girls are breaking the rules we have."
scene ep10_fr1_alphas_event4 with dissolve
qu "There are no fucking rules about this. Get real!"
scene ep10_fr1_alphas_event11 with dissolve
dw "Alumni would tell you differently! Some rules are unwritten."
scene ep10_fr1_alphas_event2 with dissolve
sa "We need to settle this once and for all. Look, we can't keep doing this crap you guys are doing."
sa "We all have to agree that sometimes we party with each other and other times we don't."
scene ep10_fr1_alphas_event11 with dissolve
dw "And who decides that?"
dw "I bet you wouldn't be partying with the DIKs if you put it to a vote."
scene ep10_fr1_alphas_event8 with dissolve
tm "That's not the first thing you're wrong about."
scene ep10_fr1_alphas_event13 with dissolve
dw "We want the HOTs! And that's that."
dw "If you try to take them from us, you better be prepared because we will take this fight up another notch."
scene ep10_fr1_alphas_event8 with dissolve
tm "And I'll shove my fist so far up your ass that you'd probably enjoy it!"
scene ep10_fr1_alphas_event6 with dissolve
sa "GUYS! ENOUGH!"
scene ep10_fr1_alphas_event7 with dissolve
sa "The HOTs have a say in this, too. This is not the tri-alphas' call or the DIKs' call; it's our joint call."
sa "We will respect our traditions because that's our duty as presidents."
scene ep10_fr1_alphas_event12 with dissolve
dw "You're goddamned right about that."
scene ep10_fr1_alphas_event2 with dissolve
sa "But! We will also make new traditions for the future by partying with the DIKs."
sa "And the HOTs will decide how to do it. Not you."
scene ep10_fr1_alphas_event9 with dissolve
tm "That's not good enough."
scene ep10_fr1_alphas_event11 with dissolve
dw "Yeah, that sucks balls!"
scene ep10_fr1_alphas_event9 with dissolve
tm "We should get the HOTs more than these guys. Everyone knows our parties are the shit."
scene ep10_fr1_alphas_event13 with dissolve
dw "There's no way we would agree to that. No chance in hell!"
dw "And our parties are the bomb! There are beers and chicks everywhere!"
dw "You wouldn't know anything about it because you'd never be invited to one."
scene ep10_fr1_alphas_event7 with dissolve
sa "I have a proposition. And I think it will make everyone happy."
scene ep10_fr1_alphas_event2 with dissolve
sa "The DIKs will party more with the HOTs than the tri-alphas..."
scene ep10_fr1_alphas_event8 with dissolve
tm "Damn straight."
scene ep10_fr1_alphas_event11 with dissolve
dw "Fuck no. No way."
scene ep10_fr1_alphas_event7 with dissolve
sa "And in return..."
sa "I'll get you Chad back."
scene ep10_fr1_alphas_event14 with dissolve
dw "..."
scene ep10_fr1_alphas_event2 with dissolve
sa "You know you want him. Hell, you know you need him."
sa "How are you going to win that title next year without him?"
scene ep10_fr1_alphas_event15 with dissolve
an "Dawe. We have Caleb now. I think we stand a good chance. If he becomes one of us, I mean."
scene ep10_fr1_alphas_event16 with dissolve
dw "But with both of them, we would be unstoppable. Last year was close, but now... That trophy would be ours."
scene ep10_fr1_alphas_event7 with dissolve
sa "Given what he did, I don't think I can get him back as president, but I'll make sure he can be one of you guys again."
scene ep10_fr1_alphas_event11 with dissolve
dw "Chad told us you were gonna try in the past. How come you couldn't make it happen back then?"
scene ep10_fr1_alphas_event7 with dissolve
sa "Because I never gave it a shot. And he's got himself to blame for that."
sa "This time, however, I will make it happen."
scene ep10_fr1_alphas_event11 with dissolve
dw "You better not be bullshitting us."
scene ep10_fr1_alphas_event7 with dissolve
sa "There's no bullshit. You'll get Chad back, and the DIKs will get more of the HOTs than you."
sa "Everybody wins. Do we have a deal?"
scene ep10_fr1_alphas_event12 with dissolve
dw "Deal!"
dw "And none of you better not fuck us over again! Or this deal is off!"
scene ep10_fr1_alphas_event18 with dissolve
sa "Rusty? Tommy? Do we have a deal?"
scene ep10_fr1_alphas_event10 with dissolve
rs "We can work with that. And neither of us trashes each other's homes again. Including Caleb or any other guy you'd use for it."
scene ep10_fr1_alphas_event17 with dissolve
an "Deal."
scene ep10_fr1_alphas_event16 with dissolve
dw "You don't get to say deal; it's me who says deal."
scene ep10_fr1_alphas_event15 with dissolve
an "Then say it."
scene ep10_fr1_alphas_event13 with dissolve
dw "Deal!"
scene ep10_fr1_alphas_event2 with dissolve
sa "Good! Everyone's happy."
sa "Now, unless you intend to help us clean up here, I suggest you leave."
scene ep10_fr1_alphas_event19 with dissolve
rs "It's better than nothing."
scene ep10_fr1_alphas_event20 with dissolve
tm "It's a shit deal, and you know it. We went from having the HOTs whenever we wanted to agreeing to share them."
scene ep10_fr1_alphas_event21 with dissolve
sa "You won't even notice it. We'll make this work for everyone, ok? We have to."
scene ep10_fr1_alphas_event22 with dissolve
qu "It sucks."
scene ep10_fr1_alphas_event23 with dissolve
sa "And don't get me started on you. This is practically your fault."
sa "We'll have this conversation later."
stop music fadeout 3
sa "First, I need to call Dad and find a way to bring Chad back, or this deal will be for nothing...ugh..."

$ new_bio("Dawe", "The jocks were pissed that Quinn fooled them at Halloween, and the DIKs agreed to share the HOTs with them to get an end to the constant fighting between the frats.")

if branchSage:
    jump ep10_sage_chill_label
else:
    jump ep10_ip_label

label ep10_fr1_rusty_event_label:
$ guideSuggestedPage = 98
scene ep10_fr1_rusty_event1 with dissolve
if affinity == "DIK":
    mc "You look like you're in shit shape today."
else:
    mc "You don't look too good, Rusty. How are you feeling?"
scene ep10_fr1_rusty_event2 with dissolve
rs "Well, I'm feeling last night today. Everything from Micha to the bottle of pure vodka..."
scene ep10_fr1_rusty_event1 with dissolve
mc "I bet you are. Any sober thoughts on her?"
scene ep10_fr1_rusty_event2 with dissolve
rs "I feel ashamed for putting myself out there like that."
rs "And I feel a lot of regret about even going for her in the first place."
rs "Fuck... I thought she was single and interested in me."
scene ep10_fr1_rusty_event1 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-DIKs)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Sympathize [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I totally get you. It's good to process your emotions like this, but don't be too hard on yourself."
        mc "Let's do something fun another day when we feel better."
        scene ep10_fr1_rusty_event2 with dissolve
        rs "Thanks, [name]. I'll get over her."
    "It's her fault [m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep10_fr1_rusty_event1 with dissolve
        mc "You shouldn't feel ashamed of that. If there's anyone who should feel ashamed, it's Micha. It's all her fault, really."
        scene ep10_fr1_rusty_event2 with dissolve
        rs "*{i}Sigh{/i}* I'll get over her."
scene ep10_fr1_rusty_event3 with dissolve
mc "Yeah, you will. Take the time you need."

$ new_bio("Rusty", "Rusty felt bad about Micha, and I tried my best to be there for him.")
$ optional_task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_derek_event_label:
scene ep10_fr1_derek_event1 with dissolve
mc "How's it going?"
scene ep10_fr1_derek_event2 with dissolve
de "Good, I guess. I'm checking this room thoroughly."
scene ep10_fr1_derek_event1 with dissolve
mc "This room? Why do you care about it?"
scene ep10_fr1_derek_event3 with dissolve
de "I...uh...may have used the home theater for something."
scene ep10_fr1_derek_event1 with dissolve
mc "You watched porn in here, didn't you?"
scene ep10_fr1_derek_event4 with dissolve
de "Have you ever seen a 150-inch pussy, [mc_de]? You can't go back to fapping to your phone after you have."
scene ep10_fr1_derek_event6 with dissolve
mc "I can see why you wouldn't want someone to record that."
scene ep10_fr1_derek_event7 with dissolve
de "Exactly."
scene ep10_fr1_derek_event8 with dissolve
de "Also, do yourself a favor. Never sit on that spot."
de "Trust me on this."
scene ep10_fr1_derek_event2 with dissolve
de "This is going to take a while... I need to check every room."
scene ep10_fr1_derek_event1 with dissolve
mc "Wait... For the sake of it or because you jacked off in them?"
scene ep10_fr1_derek_event4 with dissolve
de "I don't feel like I have to explain myself to you."
scene ep10_fr1_derek_event1 with dissolve
mc "Is that why you wanted to check my room?"
if branchMayaJosy:
    scene ep10_fr1_derek_event4 with dissolve
    de "I don't want any sex tapes of you and my sis to leak. *{i}Mumbles{/i}* Among other things."
    scene ep10_fr1_derek_event1 with dissolve
    mc "What was that last part?"
    mc "Wait. Don't tell me. I don't wanna know."
else:
    scene ep10_fr1_derek_event5 with dissolve
    de "..."
    mc "Don't tell me. I don't wanna know."

if "ep10_fr1_derek_event2_label" in event_list:
    scene ep10_fr1_derek_event2 with dissolve
    de "How's it going on your end?"
    $ event_list.remove("ep10_fr1_derek_event2_label")
    jump ep10_fr1_derek_event2_label
jump endEvent

label ep10_fr1_camera1_event_label:
if "ep10_fr1_clean7_event_label" in event_list:
    scene ep10_fr1_camera1_event1 with dissolve
else:
    scene ep10_fr1_camera1_event1b with dissolve
mc "(Putting a hidden camera in the bathroom would be creepy. Let's hope no one did...)"
play sound "sound_effects/switch.mp3"
if "ep10_fr1_clean7_event_label" in event_list:
    scene ep10_fr1_camera1_event2
else:
    scene ep10_fr1_camera1_event2b
$ renpy.pause()
scene ep10_fr1_camera1_event3 with dissolve
mc "(I don't see any red flashes in here. That's good. This room is clean.)"

$ ep10_cameras += 5
if ep10_cameras < 5:
    $ task_list[6] = "Check rooms for hidden cameras %d/5" % ep10_cameras
else:
    $ task_list[6] = "Talk to Derek again"
    mc "(Ok. I've checked where I can. I should let Derek know.)"
    $ event_list.append("ep10_fr1_derek_event2_label")
$ updateTaskList()
play sound "sound_effects/switch.mp3"
jump endEvent

label ep10_fr1_camera2_event_label:
mc "(Ok, no one's here. Let's check if there are any cameras in here.)"
play sound "sound_effects/switch.mp3"
scene ep10_fr1_camera2_event2
mc "(Hm... I think we're good. There's nothing I can spot, at least.)"

$ ep10_cameras += 5
if ep10_cameras < 5:
    $ task_list[6] = "Check rooms for hidden cameras %d/5" % ep10_cameras
else:
    $ task_list[6] = "Talk to Derek again"
    mc "(Ok. I've checked where I can. I should let Derek know.)"
    $ event_list.append("ep10_fr1_derek_event2_label")
$ updateTaskList()
play sound "sound_effects/switch.mp3"
jump endEvent

label ep10_fr1_camera3_event_label:
scene ep10_fr1_camera3_event1 with dissolve
mc "(It would be weird if there were cameras in here, but let's check.)"
play sound "sound_effects/switch.mp3"
scene ep10_fr1_camera3_event2
mc "(Nope, there's nothing in here. That's good.)"

$ ep10_cameras += 5
if ep10_cameras < 5:
    $ task_list[6] = "Check rooms for hidden cameras %d/5" % ep10_cameras
else:
    $ task_list[6] = "Talk to Derek again"
    mc "(Ok. I've checked where I can. I should let Derek know.)"
    $ event_list.append("ep10_fr1_derek_event2_label")
$ updateTaskList()
play sound "sound_effects/switch.mp3"
jump endEvent

label ep10_fr1_camera4_event_label:
mc "(Please, let there be no cameras in here...)"
play sound "sound_effects/switch.mp3"
if "ep10_fr1_clean6_event_label" in event_list:
    scene ep10_fr1_camera4_event1
else:
    scene ep10_fr1_camera4_event1b
mc "(*{i}Phew{/i}* Nothing.)"

$ ep10_cameras += 5
if ep10_cameras < 5:
    $ task_list[6] = "Check rooms for hidden cameras %d/5" % ep10_cameras
else:
    $ task_list[6] = "Talk to Derek again"
    mc "(Ok. I've checked where I can. I should let Derek know.)"
    $ event_list.append("ep10_fr1_derek_event2_label")
$ updateTaskList()
play sound "sound_effects/switch.mp3"
jump endEvent

label ep10_fr1_camera5_event_label:
mc "(Let's check this room...)"
play sound "sound_effects/switch.mp3"
if "ep10_fr1_clean8_event_label" in event_list:
    scene ep10_fr1_camera5_event1
else:
    scene ep10_fr1_camera5_event1b
mc "(This room is clean.)"

$ ep10_cameras += 5
if ep10_cameras < 5:
    $ task_list[6] = "Check rooms for hidden cameras %d/5" % ep10_cameras
else:
    $ task_list[6] = "Talk to Derek again"
    mc "(Ok. I've checked where I can. I should let Derek know.)"
    $ event_list.append("ep10_fr1_derek_event2_label")
play sound "sound_effects/switch.mp3"
jump endEvent

label ep10_fr1_derek_event2_label:
scene ep10_fr1_derek_event1 with dissolve
mc "I've checked a few rooms, and I couldn't find anything. No red flashes. Nothing."
scene ep10_fr1_derek_event2 with dissolve
de "Good."
scene ep10_fr1_derek_event1 with dissolve
mc "Do you think it's only in your room?"
scene ep10_fr1_derek_event2 with dissolve
de "That might be the case... And that makes me wonder why."
de "Someone is targeting me... But who?"
scene ep10_fr1_derek_event1 with dissolve
mc "Can you be sure about that? What if the camera was there before you moved in?"
scene ep10_fr1_derek_event4 with dissolve
de "But why?"
scene ep10_fr1_derek_event1 with dissolve
if ep2_fuckHOT:
    mc "I don't know... But if that's the case, it caught me fucking Sarah in there..."
else:
    mc "I don't know..."
mc "What's next?"
scene ep10_fr1_derek_event2 with dissolve
de "I'm gonna check more before I decide what to do. And I need to sort out a few things that are bothering me."
de "I don't feel like I can trust anyone else right now."
scene ep10_fr1_derek_event1 with dissolve
mc "Let me know when you need my help."
$ new_bio("Derek", "I helped Derek search the DIKs' mansion for hidden cameras, but I couldn't find any.")
$ task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_leon_event_label:
$ guideSuggestedPage = 100
scene ep10_fr1_leon_event1 with dissolve
if affinity == "DIK":
    mc "Hey, Lily! I didn't recognize you without a skirt and stockings."
    scene ep10_fr1_leon_event2 with dissolve
    le "Ha-ha. Not."
else:
    mc "Hey, Leon. How's it going?"
    scene ep10_fr1_leon_event2 with dissolve
le "What was I thinking with all this spiderweb? I should have skipped the decorations and locked my room during the party."
scene ep10_fr1_leon_event3 with dissolve
mc "Use the vacuum cleaner on it. I think it's effective."
scene ep10_fr1_leon_event4 with dissolve
le "Oh, nice idea!"
scene ep10_fr1_leon_event3 with dissolve
mc "Did you have fun yesterday?"
if not branchJill and ((ep8_leons_side and not ep9_leons_side) or (not ep8_leons_side and ep9_leons_side)):
    scene ep10_fr1_leon_event4 with dissolve
    le "The night ended great. Jamie and I made up."
    scene ep10_fr1_leon_event3 with dissolve
    if affinity == "DIK":
        mc "Yeah, I saw it on Rooster. Unfortunately..."
    else:
        mc "Yeah, I saw it on Rooster."
    scene ep10_fr1_leon_event4 with dissolve
    le "Damn... I forgot about that cluck. We were hammered when we posted it."
    le "Does it look good?"
    scene ep10_fr1_leon_event3 with dissolve
    if affinity == "DIK":
        mc "No. It does not. It made me want to claw my eyes out."
    else:
        mc "Eh... You should be the judge of that."
else:
    if (minigames and pp_current_party_happiness[4] > 2) or (not minigames and pp_current_party_happiness[4] == 1):
        scene ep10_fr1_leon_event4 with dissolve
        le "It was an awesome party, dude. I don't know how you did it."
    elif (minigames and pp_current_party_happiness[4] > 1) or (not minigames and pp_current_party_happiness[4] == 0):
        scene ep10_fr1_leon_event4 with dissolve
        le "I did, yeah. It was fun."
    else:
        scene ep10_fr1_leon_event2 with dissolve
        le "Not that much. The party kinda sucked for me."
    scene ep10_fr1_leon_event3 with dissolve
if not ep10_others_intro:
    if affinity == "DIK":
        mc "I'm guessing you struck out with that costume."
    else:
        mc "Did you strike out with that costume, or...?"
    scene ep10_fr1_leon_event2 with dissolve
    le "Big time. But I'll make up for it at the next party, for sure."
    le "I have to do some damage control first, though. Some girls I like cringed at me last night."
    scene ep10_fr1_leon_event3 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-DIKs)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "Make him feel better [m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "You're a guy who's not afraid to make fun of himself. Girls like that, I think."
            scene ep10_fr1_leon_event4 with dissolve
            le "Thanks, [name]."
        "Make fun of him [m_c1][mod_choices[3]]":
            $ dk(1)
            mc "Many guys did, too."
            scene ep10_fr1_leon_event2 with dissolve
            le "Ugh..."

$ optional_task_list[0] = ""
jump endEvent

label ep10_fr1_jb_event_label:
scene ep10_fr1_jb_event1 with dissolve
mc "Are there any leftovers from yesterday?"
scene ep10_fr1_jb_event2 with dissolve
jb "Way less than I thought there would be. Some people went hard on the cakes."
scene ep10_fr1_jb_event3 with dissolve
mc "That's a big compliment."
scene ep10_fr1_jb_event2 with dissolve
jb "Yeah, it sure is."
scene ep10_fr1_jb_event3 with dissolve
mc "Need any help in here?"
scene ep10_fr1_jb_event2 with dissolve
jb "No, I've got this. I'm kinda pedantic when it comes to the kitchen."
scene ep10_fr1_jb_event3 with dissolve
mc "Make it sparkle, then."
scene ep10_fr1_jb_event4 with dissolve
jb "Hey, uh... I need to ask you about something. If it's cool?"
scene ep10_fr1_jb_event5 with dissolve
mc "What's up?"
scene ep10_fr1_jb_event6 with dissolve
jb "It's kind of a sensitive question..."
scene ep10_fr1_jb_event5 with dissolve
if affinity == "DIK":
    mc "I'll be gentle, haha."
elif affinity == "CHICK":
    mc "I can be a sensitive guy."
else:
    mc "Whatever you ask will stay between us."
scene ep10_fr1_jb_event6 with dissolve
jb "I knew I could count on you..."
jb "So, I woke up in my bed early, and I think I saw something that I shouldn't have seen."
jb "And if I saw what I think I saw...um..."
scene ep10_fr1_jb_event5 with dissolve
mc "What was it?"
scene ep10_fr1_jb_event8 with dissolve
jb "I might be paranoid, but..."
jb "I heard a door close in the hallway upstairs."
scene ep10_fr1_jb_event5 with dissolve
mc "To Jacob's or Nick's room?"
scene ep10_fr1_jb_event6 with dissolve
jb "Yeah, it was one of them, for sure."
jb "And when I opened my eyes, I saw Heather walking down the stairs."
scene ep10_fr1_jb_event5 with dissolve
mc "Uh, ok? That's kinda weird or...?"
scene ep10_fr1_jb_event7 with dissolve
jb "I don't know, is it?"
scene ep10_fr1_jb_event5 with dissolve
mc "Do you think she was checking up on them?"
scene ep10_fr1_jb_event6 with dissolve
jb "The thing is... Leon and woke up Tommy for the walk of shame."
jb "It didn't look like someone else had been sleeping next to him."
scene ep10_fr1_jb_event7 with dissolve
jb "Do you think she might have...you know...cheated on Tommy?"
scene ep10_fr1_jb_event5 with dissolve
mc "You didn't see her do it, right? So, you can't know for sure."
scene ep10_fr1_jb_event6 with dissolve
jb "You're right about that. It's just a gut feeling."
scene ep10_fr1_jb_event5 with dissolve
$ guideSuggestedPage = 98
if ep9_heather_lewd == 2:
    menu:
        "Tell him some of what you know":
            jump ep10_fr1_jb1_label
        "Don't tell him":
            jump ep10_fr1_jb2_label

menu:
    "Tell him what you know":
        label ep10_fr1_jb1_label:
        $ ep10_told_jb_about_heather = True
        mc "Last night, I talked to her, and she seemed upset about Tommy wanting to fuck Christie."
        mc "And it seemed to me like she was thinking about doing the same to him with someone."
        scene ep10_fr1_jb_event9 with dissolve
        jb "Did she tell you she wanted to fuck other dudes?"
        scene ep10_fr1_jb_event5 with dissolve
        mc "Pretty much."
        scene ep10_fr1_jb_event9 with dissolve
        jb "Then what happened?"
        scene ep10_fr1_jb_event5 with dissolve
        if ep9_heather_lewd == 2:
            mc "(Fuck, I can't tell him what I did...)"
        mc "I don't know, but she seemed determined to do it."
        scene ep10_fr1_jb_event7 with dissolve
        jb "Are you saying Heather did that? With Jacob or Nick?"
        scene ep10_fr1_jb_event5 with dissolve
        mc "I'm not saying she did anything, but that's what she told me."
        scene ep10_fr1_jb_event7 with dissolve
        jb "Damn... What do you think I should do?"
        jb "I mean, fucking another bro's girl behind their back is like a cardinal sin."
        if ep9_heather_lewd == 2:
            scene ep10_fr1_jb_event5 with dissolve
            mc "Uh... I don't know. I mean, it's Heather. Considering what Tommy does to her, I don't think it's that bad if someone did."
            scene ep10_fr1_jb_event7 with dissolve
            jb "Unless Tommy is cool with it, I think it is."
    "Don't tell him":
        label ep10_fr1_jb2_label:
        $ ep10_told_jb_about_heather = False
        mc "I don't know. I think you should be careful of accusing her of that."
        mc "I mean, you didn't see her do it, right?"
        scene ep10_fr1_jb_event6 with dissolve
        jb "Exactly, I didn't. But she was still wearing her costume, so..."
        jb "What do you think I should do?"
scene ep10_fr1_jb_event5 with dissolve
mc "If I were you, I'd probably stay out of it. But that's me."
mc "Tommy and Heather's relationship isn't a normal one. I'd let them sort their issues out without getting involved."
if ep10_told_jb_about_heather:
    mc "I mean, Tommy fucks girls without Heather's approval like it's nothing. Who's to say she can't too, you know?"
mc "I wouldn't make too big of a deal out of this."
scene ep10_fr1_jb_event6 with dissolve
if ep10_told_jb_about_heather:
    jb "Maybe you're right... I don't get how their vetoes work. Heather always seemed ok with everything Tommy did."
    jb "And I wasn't sure who to talk to about this. Since Elena is Heather's friend, it didn't feel good to mention this to her."
else:
    jb "Maybe you're right..."
    jb "I wasn't sure who to talk to about this. Since Elena is Heather's friend, it didn't feel good to mention this to her."
scene ep10_fr1_jb_event5 with dissolve
mc "I get you."
scene ep10_fr1_jb_event10 with dissolve
jb "Thanks for easing my mind, [name]. It's good to have people you can trust with these things."
if branchMayaJosy:
    scene ep10_fr1_jb_event6 with dissolve
    jb "Oh, by the way. Heads up... Tommy was ranting to me about you, Maya, and Josy in front of some of the HOTs... It might spread."
    scene ep10_fr1_jb_event5 with dissolve
    mc "So much for the DIK secret code..."

if ep10_told_jb_about_heather:
    $ new_bio("John Boy", "John Boy told me he saw Heather exit Jacob's or Nick's room, thinking she spent the night with one of them. I shared what I knew about Heather with him.")
else:
    $ new_bio("John Boy", "John Boy told me he saw Heather exit Jacob's or Nick's room, thinking she spent the night with one of them. I didn't share what I knew about Heather with him.")
$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_jamie_event_label:
scene ep10_fr1_jamie_event1 with dissolve
ri "This floor is nasty. It doesn't look anything like it did last night."
scene ep10_fr1_jamie_event2 with dissolve
jm "This isn't even the worst I've seen this floor. I can mop it up if you want."
scene ep10_fr1_jamie_event1 with dissolve
ri "No, I've got this. It can't always be fun and parties, can it?"
scene ep10_fr1_jamie_event4 with dissolve
mc "Cleaning the dance floor, huh? Want some party music while you're at it?"
scene ep10_fr1_jamie_event2 with dissolve
jm "No way, that would make my head explode."
scene ep10_fr1_jamie_event5 with dissolve
ri "How did it go with Dany last night?"
scene ep10_fr1_jamie_event2 with dissolve
jm "What do you mean?"
scene ep10_fr1_jamie_event5 with dissolve
ri "She looked like she was gonna murder you when you were performing magic. And she gave me the stink eye."
scene ep10_fr1_jamie_event3 with dissolve
jm "Uh... It went all right. She...uh...They..."
jm "Fuck it. She doesn't like our crowd that much, but I think she had fun."
scene ep10_fr1_jamie_event5 with dissolve
ri "How do you know?"
scene ep10_fr1_jamie_event2 with dissolve
jm "Ok, she didn't have fun. She hated the party."
jm "But she did it for me, and that should count for something."
scene ep10_fr1_jamie_event6 with dissolve
ri "I don't know what you see in her. I really don't."
scene ep10_fr1_jamie_event3 with dissolve
jm "You don't see what I see. That's fine."
scene ep10_fr1_jamie_event6 with dissolve
ri "I thought you were done with her."
scene ep10_fr1_jamie_event3 with dissolve
jm "I was, but things changed for me."
scene ep10_fr1_jamie_event5 with dissolve
ri "You deserve better, dude."
scene ep10_fr1_jamie_event3 with dissolve
jm "I do?"
scene ep10_fr1_jamie_event5 with dissolve
ri "Cheating on her put aside, you're one of the good guys."
scene ep10_fr1_jamie_event3 with dissolve
jm "Thanks, I guess."

if ep9_riona_choice == "DIK" or ep9_riona_choice == "NEUTRAL":
    scene ep10_fr1_jamie_event7 with dissolve
    $ renpy.pause()
    scene ep10_fr1_jamie_event8 with dissolve
    ri "There aren't many good guys out there."
    scene ep10_fr1_jamie_event2 with dissolve
    jm "I'd have to take your word on that."
    scene ep10_fr1_jamie_event8 with dissolve
    ri "Yeah, some guys only want one thing from you."
    ri "But not you, Jamie."
    scene ep10_fr1_jamie_event3 with dissolve
    jm "Uh... I don't?"
    scene ep10_fr1_jamie_event8 with dissolve
    ri "No."
    ri "I'm happy to be around you."
    scene ep10_fr1_jamie_event9 with dissolve
    mc "(Is she flirting with him?)"
    $ new_bio("Riona", "Riona flirted with Jamie in front of me.")
$ task_list[11] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_arieth_event_label:
scene ep10_fr1_arieth_event1 with dissolve
ar "Yes, gimme!"
scene ep10_fr1_arieth_event2 with dissolve
el "Arieth... Maybe you shouldn't drink alcohol."
scene ep10_fr1_arieth_event4 with dissolve
ar "I know it's early, but I didn't even get to party yesterday. I'm gonna make up for it today."
scene ep10_fr1_arieth_event5 with dissolve
ar "WOOOO!!!"
scene ep10_fr1_arieth_event2 with dissolve
el "It's not that it's early; I was thinking more about your...um...situation."
scene ep10_fr1_arieth_event6 with dissolve
ar "Oh..."
scene ep10_fr1_arieth_event7 with dissolve
ar "It's so unfair! You had this super-duper-awesome party, and we didn't even get one."
scene ep10_fr1_arieth_event3 with dissolve
el "I know."
scene ep10_fr1_arieth_event7 with dissolve
ar "This is all Dawe's fault."
scene ep10_fr1_arieth_event3 with dissolve
el "What do you mean?"
scene ep10_fr1_arieth_event7 with dissolve
ar "If he hadn't put a baby in me, I wouldn't feel like my life is slipping away."
ar "I've been stressed out every day since I found out about it."
ar "Not knowing what to do. Not knowing how to feel. Am I even the mother? My mind is running a mile per hour, and everything is just bleh!"
scene ep10_fr1_arieth_event3 with dissolve
el "About that... Are you going to keep it?"
scene ep10_fr1_arieth_event8 with dissolve
ar "I have to! It's growing inside of me. I can feel it."
ar "And I hate it! And I love it!"
scene ep10_fr1_arieth_event7 with dissolve
ar "In God knows how many months from now, I'll have a bald boy with a micropenis shooting out of me."
scene ep10_fr1_arieth_event3 with dissolve
el "How do you know it's a boy?"
scene ep10_fr1_arieth_event4 with dissolve
ar "It runs in the family."
$ optional_task_list[3] = ""
jump endEvent

label ep10_fr1_elena_event_label:
$ guideSuggestedPage = 97
scene ep10_fr1_elena_event1 with dissolve
$ renpy.pause()
play sound "sound_effects/slap.mp3"
scene ep10_fr1_elena_event2 with vpunch
mc "Hey?"
scene ep10_fr1_elena_event3 with dissolve
el "Haha, I couldn't resist."
scene ep10_fr1_elena_event4 with dissolve
$ tmpBool3 = False
menu:
    "That's sexist":
        $ tmpBool3 = True
        mc "You're so sexist, I swear."
        scene ep10_fr1_elena_event3 with dissolve
        el "Here! You get one free slap. Make it count."
    "I'm irresistible":
        mc "I know I'm irresistible, but you have to try to keep your hands to yourself, Elena."
        scene ep10_fr1_elena_event3 with dissolve
        el "As if you would be able to resist if I bent over in front of you."
scene ep10_fr1_elena_event5 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Slap her [m_c1][mod_choices[3]]":
        $ dk(1)
        if affinity == "DIK":
            if tmpBool3:
                mc "I'll make it count, alright."
            else:
                mc "You're goddamned right I can't resist it."
        play sound "sound_effects/slap.mp3"
        if affinity == "DIK":
            scene ep10_fr1_elena_event7 with vpunch
            el "OUCH! HOLY FUCK!"
            scene ep10_fr1_elena_event8 with dissolve
            mc "Hahaha! Now we're even."
            scene ep10_fr1_elena_event9 with dissolve
            el "Hahaha! Even? That was way too hard, dude! It's gonna leave a mark!"
        else:
            scene ep10_fr1_elena_event6 with vpunch
            el "Ouch!"
            mc "All right. Now we're even."
        scene ep10_fr1_elena_event10 with dissolve
        if affinity == "CHICK":
            mc "It didn't hurt, did it?"
        else:
            mc "That's a firm ass."
        scene ep10_fr1_elena_event11 with dissolve
        if affinity == "CHICK":
            el "You have a good slap. I hope you're putting it to use in bed."
            scene ep10_fr1_elena_event10 with dissolve
            menu:
                "That's private [m_c1][mod_choices[2]]":
                    $ dk(-1)
                    mc "Sorry, but that's private."
                    scene ep10_fr1_elena_event11 with dissolve
                "Maybe":
                    mc "Haha, maybe."
                    scene ep10_fr1_elena_event11 with dissolve
                "Joke [m_c1][mod_choices[3]]":
                    $ dk(1)
                    mc "Of course. I slap everything I can slap, even my own ass."
                    scene ep10_fr1_elena_event11 with dissolve
                    el "Haha, you're so weird."
        else:
            el "Haha, you're so weird."
            el "And you have a firm ass too. I can tell that you work out."
    "Don't slap her [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Nah, I'm good."
        el "Tsk."
        scene ep10_fr1_elena_event11 with dissolve
el "On a scale between 1 and 10, how hungover are you?"
scene ep10_fr1_elena_event10 with dissolve
mc "A 5 or so. It's not too bad. You?"
scene ep10_fr1_elena_event12 with dissolve
el "6 or 7. I should have loaded my gun with cider like Jacob did."
scene ep10_fr1_elena_event13 with dissolve
mc "Do you want some coffee? I can get you some."
scene ep10_fr1_elena_event11 with dissolve
el "Thanks, but I already drank enough for today."
scene ep10_fr1_elena_event13 with dissolve
mc "Same here."
scene ep10_fr1_elena_event12 with dissolve
el "Scouring the place for drinks, are you?"
scene ep10_fr1_elena_event13 with dissolve
mc "I think the others would puke if they had to smell the alcohol stench today, so I volunteered."
scene ep10_fr1_elena_event11 with dissolve
el "That's nice of you. I'll help out when I finish my tasks."
scene ep10_fr1_elena_event10 with dissolve
mc "Thanks, but don't stress it."

$ optional_task_list[4] = ""
jump endEvent

label ep10_fr1_maya_event_label:
$ guideSuggestedPage = 100
if branchMayaJosy:
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_fr1_maya_event1 with dissolve
    else:
        scene ep10_fr1_maya_event1b with dissolve
    mc "You came back."
    scene ep10_fr1_maya_event2 with dissolve
    my "I have to help out, but I'm feeling weird about this."
    scene ep10_fr1_maya_event3 with dissolve
    mc "I'm sorry, Maya..."
    scene ep10_fr1_maya_event2 with dissolve
    my "What's done is done. I hope it doesn't spread, though."
    scene ep10_fr1_maya_event13 with dissolve
    ml "Aren't you two cute? So, it's true, huh?"
    scene ep10_fr1_maya_event15 with dissolve
    my "What?"
    scene ep10_fr1_maya_event13 with dissolve
    ml "I heard from Sarah that you're in a three-way relationship."
    scene ep10_fr1_maya_event18 with dissolve
    my "Oh, God... It's started already."
    scene ep10_fr1_maya_event13 with dissolve
    ml "It's fucking cool, Maya. I didn't think you'd be into that."
    scene ep10_fr1_maya_event16 with dissolve
    my "Mhm. Sure."
    scene ep10_fr1_maya_event14 with dissolve
    ml "I'm not being sarcastic. I used to date a guy in high school together with a friend."
    ml "It was pretty laid back since it didn't feel that serious, with feelings and whatnot."
    ml "So, I get why you'd do it. It's a great way to have fun without having to worry about that commitment crap."
    scene ep10_fr1_maya_event15 with dissolve
    my "Really? How did that go?"
    scene ep10_fr1_maya_event14 with dissolve
    ml "I ended up leaving them. Michelle - my friend - is still with the guy, I think. We don't talk much these days."
    ml "But I got what I wanted, and then I got out before it was too late."
    scene ep10_fr1_maya_event13 with dissolve
    ml "Enjoy it while it lasts. It's a blast."
    scene ep10_fr1_maya_event10 with dissolve
    my "That's not like us, right?"
    scene ep10_fr1_maya_event11 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(-Maya)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "It sounds like it [m_c1][mod_choices[1]]":
            $ RPmaya -= 1
            mc "It sounds a lot like us, to be honest. We're having a lot of fun together."
            scene ep10_fr1_maya_event10 with dissolve
            my "But what about the feelings? Can you relate to that?"
            scene ep10_fr1_maya_event11 with dissolve
            mc "There are feelings between us, but it hasn't felt too serious yet."
        "Not necessarily [m_c1][mod_choices[0]]":
            $ RPmaya += 1
            mc "No, not necessarily. I mean, we have a lot of fun together..."
            mc "...but I want the feelings, too."
            scene ep10_fr1_maya_event12 with dissolve
            my "Exactly."
            scene ep10_fr1_maya_event11 with dissolve
            mc "But we don't have to let people know about that. The less they know, the better. That's what I think."
            scene ep10_fr1_maya_event10 with dissolve
            my "Yeah... Maybe I can work with that."
    $ new_bio("Maya", "Maya felt weird about letting people know about our relationship, even if the lie I told about us protected her and Josy somewhat.")
elif ep9_jm_sad:
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_fr1_maya_event1 with dissolve
    else:
        scene ep10_fr1_maya_event1b with dissolve
    mc "Hey, Maya..."
    scene ep10_fr1_maya_event2 with dissolve
    my "Hi."
    scene ep10_fr1_maya_event3 with dissolve
    mc "How are you today?"
    scene ep10_fr1_maya_event2 with dissolve
    my "You know...?"
    scene ep10_fr1_maya_event3 with dissolve
    mc "I do. Me too."
    scene ep10_fr1_maya_event4 with dissolve
    my "It sucks. Big time."
    scene ep10_fr1_maya_event3 with dissolve
    mc "Do you think we'll be able to move past it?"
    scene ep10_fr1_maya_event5 with dissolve
    my "I don't know, [name]. But it's not like we have a choice, do we?"
    my "I mean, I'll be seeing you daily for at least the rest of this semester."
    if not "ep10_fr1_josy_event_label" in event_list:
        scene ep10_fr1_maya_event6 with dissolve
        mc "You seem to be taking it better than Josy... She doesn't want to talk to me."
        scene ep10_fr1_maya_event5 with dissolve
        my "Don't be mistaken... I'm hurting a lot too."
        my "I guess we have different ways of showing it."
        my "And if the choice I have to make is to keep seeing you or not..."
        scene ep10_fr1_maya_event7 with dissolve
        my "I know what I'd choose."
    else:
        scene ep10_fr1_maya_event7 with dissolve
    my "You mean a lot to me in many ways."
    my "Fuck, I don't wanna cry right now. Can you go someplace else?"
    scene ep10_fr1_maya_event6 with dissolve
    mc "Yeah. But for the record..."
    mc "I feel the same way. It's just..."
    scene ep10_fr1_maya_event7 with dissolve
    my "I already know, [name]. Please leave."
else:
    if "ep10_fr1_clean2_event_label" in event_list:
        scene ep10_fr1_maya_event1 with dissolve
    else:
        scene ep10_fr1_maya_event1b with dissolve
    mc "Thanks for helping out."
    scene ep10_fr1_maya_event8 with dissolve
    my "Of course. And it's not just because I'm a HOT now, either."
    scene ep10_fr1_maya_event9 with dissolve
    mc "You are? For real this time?"
    scene ep10_fr1_maya_event8 with dissolve
    my "Sure am."
    scene ep10_fr1_maya_event13 with dissolve
    ml "You are!? That's awesome, Maya."
    scene ep10_fr1_maya_event17 with dissolve
    my "You think?"
    scene ep10_fr1_maya_event13 with dissolve
    ml "The more the merrier, right?"
    scene ep10_fr1_maya_event17 with dissolve
    my "Yeah."
    scene ep10_fr1_maya_event9 with dissolve
    mc "Are you moving in with them now?"
    scene ep10_fr1_maya_event8 with dissolve
    my "I haven't decided on that yet. I see upsides and downsides either way."
    scene ep10_fr1_maya_event9 with dissolve
    mc "Take your time to think it through. I'm happy for you."
    scene ep10_fr1_maya_event8 with dissolve
    my "Thanks, [name]."

$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_mel_event_label:
scene ep10_fr1_mel_event1 with dissolve
ml "Ugh... People are gross."
scene ep10_fr1_mel_event6 with dissolve
my "How so?"
scene ep10_fr1_mel_event1 with dissolve
ml "Someone puked behind the sofa."
scene ep10_fr1_mel_event7 with dissolve
my "Oh... Is that what smells?"
scene ep10_fr1_mel_event2 with dissolve
ml "Ugh... I can't do this."
scene ep10_fr1_mel_event6 with dissolve
my "Do you want me to clean it?"
scene ep10_fr1_mel_event2 with dissolve
ml "Would you?"
scene ep10_fr1_mel_event6 with dissolve
my "Yeah, leave it, and I'll get a mop later."
scene ep10_fr1_mel_event3 with dissolve
ml "Thanks. You don't know how much I appreciate that."
scene ep10_fr1_mel_event6 with dissolve
my "It's not a problem."
scene ep10_fr1_mel_event4 with dissolve
ml "[name]? Where do the decorations go?"
scene ep10_fr1_mel_event5 with dissolve
mc "Put them in Nick's room. I'm not quite sure what's ours and what we rented."
scene ep10_fr1_mel_event4 with dissolve
ml "Got it."

$ optional_task_list[5] = ""
jump endEvent

label ep10_fr1_lily_event_label:
$ guideSuggestedPage = 98
if ep10_rolling:
    scene ep10_fr1_lily_event4 with dissolve
    ly "There he is."
    scene ep10_fr1_lily_event5 with dissolve
    mc "Here I am."
    label ep10_fr1_lily_event_label2:
    scene ep10_fr1_lily_event6 with dissolve
    ly "I haven't decided what I wanna call you yet."
    scene ep10_fr1_lily_event7 with dissolve
    mc "What's wrong with my name?"
    scene ep10_fr1_lily_event6 with dissolve
    ly "Nah, I want something else for you. To brand you."
    scene ep10_fr1_lily_event7 with dissolve
    mc "I'm not a cow, Lily."
    scene ep10_fr1_lily_event8 with dissolve
    ly "Haha!"
    scene ep10_fr1_lily_event6 with dissolve
    ly "Tell me... What do you think about king and queen?"
    scene ep10_fr1_lily_event7 with dissolve
    if affinity == "DIK":
        mc "If I'm the king, I like it. If not, fuck you."
    else:
        mc "Hm... I like it!"
    scene ep10_fr1_lily_event6 with dissolve
    ly "Hell yeah. You're my king, huh?"
    scene ep10_fr1_lily_event7 with dissolve
    mc "Queen Lily. It has a nice ring to it."
    scene ep10_fr1_lily_event9 with dissolve
    ly "Sit down on the throne, king."
    mc "This is a weird throne."
    ly "Haha! Just do it."
    scene ep10_fr1_lily_event10 with dissolve
    mc "Yeah, this isn't fit for a king."
    scene ep10_fr1_lily_event11 with dissolve
    ly "How about now?"
    scene ep10_fr1_lily_event12 with dissolve
    mc "Much better."
    scene bg anim_wheelchair_ep10 movie with dissolve
    mc "Wheee!!! We rollin', Lily!"
    scene ep10_fr1_lily_event13 with dissolve
    ly "Hahaha!"
    mc "Such a low-budget throne, though."
    scene ep10_fr1_lily_event14 with dissolve
    ly "We'll have to find you something better, for sure."
    scene ep10_fr1_lily_event15 with dissolve
    if ep9_lily_nicole_lewd:
        mc "What do the rules of rolling say about kissing?"
    else:
        mc "By the way... I'm unfamiliar with the rules of...this."
        scene ep10_fr1_lily_event14 with dissolve
        ly "We can make any rules we want, king."
        scene ep10_fr1_lily_event15 with dissolve
        mc "What do the rules say about kissing?"
    scene ep10_fr1_lily_event14 with dissolve
    ly "During sex, sure."
    scene ep10_fr1_lily_event15 with dissolve
    mc "How about now? Or at other times?"
    scene ep10_fr1_lily_event16 with dissolve
    ly "Why do you wanna do it so much?"
    scene ep10_fr1_lily_event15 with dissolve
    mc "It's hot and feels nice."
    scene ep10_fr1_lily_event16 with dissolve
    ly "If it's used to assert dominance, to flex, or to make people feel uncomfortable...yes."
    ly "But if it's got something to do with feelings - hell no. Ok?"
    scene ep10_fr1_lily_event15 with dissolve
    mc "I can work with that."
    mc "Is right now off the table?"
    scene ep10_fr1_lily_event14 with dissolve
    ly "You got it."
    scene ep10_fr1_lily_event19 with dissolve
    sar "Lily? Sage's asking for you. You can do your weird wheelchair fetishes with [name] later."
    scene ep10_fr1_lily_event17 with dissolve
    ly "*{i}Whispers{/i}* Gimme your tongue."
    scene anim_lily_kiss_ep10 with dissolve
    ly "*{i}Smack{/i}* Mmm..."
    pause
    scene ep10_fr1_lily_event18 with dissolve
    ly "Tell her to come find me. The queen's busy getting freaky with her king."
    scene ep10_fr1_lily_event19 with dissolve
    if ep9_sarah_melanie_lewd:
        sar "Whatever. Enjoy the scraps me and Mel left you. His balls should be drained today."
    else:
        sar "Whatever."
    scene ep10_fr1_lily_event14 with dissolve
    if ep9_sarah_melanie_lewd:
        ly "This is where a girlfriend would freak out and slap you, but not me."
        scene ep10_fr1_lily_event15 with dissolve
        mc "Are you really cool with it?"
        scene ep10_fr1_lily_event14 with dissolve
        ly "It's not talk, [name]. I am."
        ly "And now I better find Sage before Sarah rats me out."
    else:
        ly "And that's how you do it."
        scene ep10_fr1_lily_event13 with dissolve
        mc "I've never had a boner in a wheelchair before."
        ly "Haha! It's called a throne-bone, king."
        scene ep10_fr1_lily_event14 with dissolve
        ly "I better find Sage."
else:
    scene ep10_fr1_lily_event1 with dissolve
    ly "Fuck my life, [name]."
    scene ep10_fr1_lily_event2 with dissolve
    mc "It's one of those days, huh?"
    scene ep10_fr1_lily_event1 with dissolve
    ly "This is not what I feel like doing today. Plus, I gotta work tonight."
    scene ep10_fr1_lily_event2 with dissolve
    
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(-Maya)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    
    menu:
        "I can cover for you [m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "Damn, that sucks. Go ahead and leave if you want. I can cover for you."
            scene ep10_fr1_lily_event3 with dissolve
            ly "Nah. Sage would notice, and I'd be punished like Heather will be for skipping this."
            ly "I have to push through."
            scene ep10_fr1_lily_event2 with dissolve
            mc "All right. The faster we clean, the faster we're done."
        "We all have to help out [m_c1][mod_choices[3]]":
            $ dk(1)
            mc "It is what it is. We all have to help out."
            scene ep10_fr1_lily_event3 with dissolve
            ly "I know. I know."
            scene ep10_fr1_lily_event2 with dissolve
            mc "The faster we clean, the faster we're done."
    scene ep10_fr1_lily_event1 with dissolve
    ly "Ugh."
    if ep7_lily_lewd and branchAlone:
        scene ep10_fr1_lily_event4 with dissolve
        ly "I gotta admit, [name], you're teasing me too much these days."
        scene ep10_fr1_lily_event5 with dissolve
        mc "In what way?"
        scene ep10_fr1_lily_event4 with dissolve
        ly "We flirt and all, but it doesn't seem like you want to take it further than that."
        ly "Look at me, [name]. I'm standing here, ready to have fun with you, but you seem unsure about it."
        if dtype > 0:
            scene ep10_fr1_lily_event5 with dissolve
            mc "You don't look like you're ready for anything right now."
            scene ep10_fr1_lily_event4 with dissolve
            ly "Tsk. You know what I mean."
        scene ep10_fr1_lily_event5 with dissolve
        mc "Is this about rolling together?"
        scene ep10_fr1_lily_event6 with dissolve
        ly "I'm giving you a final chance before I go find someone else for it."
        ly "Are you in or out?"
        scene ep10_fr1_lily_event7 with dissolve
        if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Lily path)","(-Maya)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
        
        menu:
            "We can roll [m_c1][mod_choices[0]]":
                $ ep10_rolling = True
                mc "I know I haven't been decisive when it comes to that, but I don't want to get locked up."
                scene ep10_fr1_lily_event6 with dissolve
                ly "And I'm telling you, that's not what it will be like."
                scene ep10_fr1_lily_event6b with dissolve
                ly "Rolling is a state of mind, dude."
                ly "We hang, we fuck, we cover each other's asses."
                scene ep10_fr1_lily_event6 with dissolve
                ly "I don't care about what you do with someone else, and neither do you."
                ly "But if you need me or I need you, no questions will be asked, and we always prioritize each other's needs."
                scene ep10_fr1_lily_event6c with dissolve
                ly "We're in sync, we understand each other, and we're fucking partners in crime."
                ly "That's what I'm offering."
                scene ep10_fr1_lily_event7 with dissolve
                mc "All right. I'm in."
                scene ep10_fr1_lily_event6 with dissolve
                ly "You're not just saying that, are you? Because if you are, don't bother."
                scene ep10_fr1_lily_event7 with dissolve
                mc "No, I mean it. I like what you said. Let's try it."
                scene ep10_fr1_lily_event6c with dissolve
                ly "Fuck yes, [name]..."
                ly "Hm..."
                $ new_bio("Lily", "I told her that we could roll, and she was very excited about it. I wasn't sure what that meant, but she seemed to have it figured out.")
                jump ep10_fr1_lily_event_label2
            "We can fuck":
                $ ep10_rolling = False
                mc "Lily, I won't say no to having sex with you, but I'm not looking for something more than that."
                scene ep10_fr1_lily_event6 with dissolve
                ly "Alright, I'm not gonna force you."
                scene ep10_fr1_lily_event7 with dissolve
                mc "It feels like a commitment."
                scene ep10_fr1_lily_event6b with dissolve
                ly "It's not a fucking relationship, but yeah, it takes commitment."
                ly "And I get it. It's not for everyone."
                scene ep10_fr1_lily_event6d with dissolve
                ly "At least I got a clear answer now. Thanks for that."
                $ new_bio("Lily", "I told her that I wasn't interested in rolling with her but still wanted to fuck her.")

$ task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep10_fr1_qc_event_label:
scene ep10_fr1_qc_event1 with dissolve
cam "Ugh. The soggy pumpkin smell makes me feel sick."
scene ep10_fr1_qc_event3 with dissolve
qu "Want a smoke?"
scene ep10_fr1_qc_event2 with dissolve
cam "That would make me throw up."
scene ep10_fr1_qc_event4 with dissolve
qu "Suit yourself."
scene ep10_fr1_qc_event2 with dissolve
cam "Did we really need to have all these pumpkins for the party?"
scene ep10_fr1_qc_event4 with dissolve
qu "Quit your bitching. Think of it as cardio. Chop chop!"
scene ep10_fr1_qc_event5 with dissolve
mc "Are you guys taking care of the pumpkins?"
scene ep10_fr1_qc_event6 with dissolve
qu "Something like that."
scene ep10_fr1_qc_event7 with dissolve
mc "Cool. I'm collecting cups, cans, and bottles. Have you seen any around here?"
scene ep10_fr1_qc_event6 with dissolve
qu "There should be shitloads on the roof."
scene ep10_fr1_qc_event7 with dissolve
if not "ep10_fr1_clean9_event_label" in event_list:
    mc "Thanks. I got those already."
else:
    mc "Thanks. I'll get to them later."

if ep9_quinn_lewd:
    scene ep10_fr1_qc_event7 with dissolve
    mc "About earlier... I know you don't like talking about feelings and PDA. I'm sorry if I pushed you."
    mc "I guess we're at different places when it comes to...well, us. I'm not saying there is an \"us\", but if there is...you know?"
    mc "I'm not gonna rush it if it's moving too fast for you. But let me just say last night with you was amazing."
    scene ep10_fr1_qc_event6 with dissolve
    qu "I didn't want to talk about this back there, and I don't want to talk about it now. Can we forget it happened?"
    scene ep10_fr1_qc_event7 with dissolve
    mc "No, we can't. But I'll shut up until you feel more comfortable talking about it."
    scene ep10_fr1_qc_event6 with dissolve
    qu "Shut up forever, then."
    scene ep10_fr1_qc_event7 with dissolve
if dtype > 0:
    mc "I can't believe that Halloween is over. It came and went fast as fuck."
else:
    mc "I can't believe that Halloween is over. All that planning and preparation and it's gone in an instant."
scene ep10_fr1_qc_event8 with dissolve
qu "There will be more parties soon."
scene ep10_fr1_qc_event7 with dissolve
mc "Yeah? Like what? Christmas?"
scene ep10_fr1_qc_event6 with dissolve
qu "You can throw a party any day of the week if you want. It doesn't have to be during holidays. You get that, right?"
scene ep10_fr1_qc_event8 with dissolve
qu "But Thanksgiving is coming up, and you guys have that DIKs' Thanksgiving party."
scene ep10_fr1_qc_event7 with dissolve
mc "What's that?"
scene ep10_fr1_qc_event8 with dissolve
qu "The one where the latest maggots thank their DIK elders by throwing them a dinner party or something."
qu "You'd have to ask Tommy about it; I don't know the details."

if not ep9_quinn_ask and branchAlone and ep8_quinn_lewd:
    scene ep10_fr1_qc_event6 with dissolve
    qu "You're good at fighting, right?"
    scene ep10_fr1_qc_event7 with dissolve
    mc "I'm pretty good at it. Why?"
    scene ep10_fr1_qc_event8 with dissolve
    qu "Just checking."
    qu "If you're free sometime next week, I'd like to borrow you."
    qu "I've got something to do downtown and could use some company."
    scene ep10_fr1_qc_event7 with dissolve
    mc "Sure. What are we doing?"
    scene ep10_fr1_qc_event8 with dissolve
    qu "Hanging out and such."
    scene ep10_fr1_qc_event7 with dissolve
    mc "Alright, I'm game."
    scene ep10_fr1_qc_event6 with dissolve
    qu "Awesome."

scene ep10_fr1_qc_event9 with dissolve
cam "Quinn? A little help?"
scene ep10_fr1_qc_event10 with dissolve
qu "*{i}Sigh{/i}* You two can't do anything, can you?"

$ event_list.append("ep10_fr1_sage_event_label")
$ task_list[4] = ""
$ updateTaskList()
jump endEvent

style clean_text_custom:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
    outlines [(6, "#000000", 0, 0)]

label ep10_fr1_clean1_event_label:
$ tmpList = ["a","b","c","d"]
$ tmpInt = 0
$ renpy.block_rollback()
show ep10_fr1_clean1_event
show ep10_fr1_clean1_event1_idle
show ep10_fr1_clean1_event2_idle
show ep10_fr1_clean1_event3_idle
show ep10_fr1_clean1_event4_idle
label ep10_fr1_clean1_event_nofx:
if tmpList == ["","","",""]:
    hide text "Clean up [tmpInt]/4"
    $ ep10_clean += 5
    if ep10_clean >= 5:
        $ task_list[0] = ""
    else:
        $ task_list[0] = "Clean the mansion [ep10_clean]/5"
    $ updateTaskList()
    jump endEvent
show text "{=clean_text_custom}Clean up [tmpInt]/4{/=clean_text_custom}" at top

if "a" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean1_event1_idle", "ep10_fr1_clean1_event1_idle", clicked=ui.returns("a"), xpos=0, ypos=0, focus_mask=True)
if "b" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean1_event2_idle", "ep10_fr1_clean1_event2_idle", clicked=ui.returns("b"), xpos=0, ypos=0, focus_mask=True)
if "c" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean1_event3_idle", "ep10_fr1_clean1_event3_idle", clicked=ui.returns("c"), xpos=0, ypos=0, focus_mask=True)
if "d" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean1_event4_idle", "ep10_fr1_clean1_event4_idle", clicked=ui.returns("d"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "a":
    $ tmpInt += 1
    $ tmpList[0] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean1_event1_idle
    jump ep10_fr1_clean1_event_nofx
elif result == "b":
    $ tmpInt += 1
    $ tmpList[1] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean1_event2_idle
    jump ep10_fr1_clean1_event_nofx
elif result == "c":
    $ tmpInt += 1
    $ tmpList[2] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean1_event3_idle
    jump ep10_fr1_clean1_event_nofx
elif result == "d":
    $ tmpInt += 1
    $ tmpList[3] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean1_event4_idle
    jump ep10_fr1_clean1_event_nofx

label ep10_fr1_clean2_event_label:
$ tmpList = ["a","b","c","d"]
$ tmpInt = 0
$ renpy.block_rollback()
show ep10_fr1_clean2_event
show ep10_fr1_clean2_event1_idle
show ep10_fr1_clean2_event2_idle
show ep10_fr1_clean2_event3_idle
show ep10_fr1_clean2_event4_idle
label ep10_fr1_clean2_event_nofx:
if tmpList == ["","","",""]:
    hide text "Clean up [tmpInt]/4"
    $ ep10_clean += 5
    if ep10_clean >= 5:
        $ task_list[0] = ""
    else:
        $ task_list[0] = "Clean the mansion [ep10_clean]/5"
    $ updateTaskList()
    jump endEvent
show text "{=clean_text_custom}Clean up [tmpInt]/4{/=clean_text_custom}" at top

if "a" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean2_event1_idle", "ep10_fr1_clean2_event1_idle", clicked=ui.returns("a"), xpos=0, ypos=0, focus_mask=True)
if "b" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean2_event2_idle", "ep10_fr1_clean2_event2_idle", clicked=ui.returns("b"), xpos=0, ypos=0, focus_mask=True)
if "c" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean2_event3_idle", "ep10_fr1_clean2_event3_idle", clicked=ui.returns("c"), xpos=0, ypos=0, focus_mask=True)
if "d" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean2_event4_idle", "ep10_fr1_clean2_event4_idle", clicked=ui.returns("d"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "a":
    $ tmpInt += 1
    $ tmpList[0] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean2_event1_idle
    jump ep10_fr1_clean2_event_nofx
elif result == "b":
    $ tmpInt += 1
    $ tmpList[1] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean2_event2_idle
    jump ep10_fr1_clean2_event_nofx
elif result == "c":
    $ tmpInt += 1
    $ tmpList[2] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean2_event3_idle
    jump ep10_fr1_clean2_event_nofx
elif result == "d":
    $ tmpInt += 1
    $ tmpList[3] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean2_event4_idle
    jump ep10_fr1_clean2_event_nofx

label ep10_fr1_clean3_event_label:
$ ep10_clean += 5
if ep10_clean >= 5:
    $ task_list[0] = ""
else:
    $ task_list[0] = "Clean the mansion [ep10_clean]/5"
$ updateTaskList()
play sound "sound_effects/bottle_clink.mp3"
scene ep10_fr1_clean3_event1 with dissolve
mc "(The floor. What an excellent place to put drinks...)"
jump endEvent

label ep10_fr1_clean4_event_label:
$ tmpList = ["a","b","c","d"]
$ tmpInt = 0
$ renpy.block_rollback()
show ep10_fr1_clean4_event
show ep10_fr1_clean4_event1_idle
show ep10_fr1_clean4_event2_idle
show ep10_fr1_clean4_event3_idle
show ep10_fr1_clean4_event4_idle
label ep10_fr1_clean4_event_nofx:
if tmpList == ["","","",""]:
    hide text "Clean up [tmpInt]/4"
    $ ep10_clean += 5
    if ep10_clean >= 5:
        $ task_list[0] = ""
    else:
        $ task_list[0] = "Clean the mansion [ep10_clean]/5"
    $ updateTaskList()
    jump endEvent
show text "{=clean_text_custom}Clean up [tmpInt]/4{/=clean_text_custom}" at top

if "a" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean4_event1_idle", "ep10_fr1_clean4_event1_idle", clicked=ui.returns("a"), xpos=0, ypos=0, focus_mask=True)
if "b" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean4_event2_idle", "ep10_fr1_clean4_event2_idle", clicked=ui.returns("b"), xpos=0, ypos=0, focus_mask=True)
if "c" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean4_event3_idle", "ep10_fr1_clean4_event3_idle", clicked=ui.returns("c"), xpos=0, ypos=0, focus_mask=True)
if "d" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean4_event4_idle", "ep10_fr1_clean4_event4_idle", clicked=ui.returns("d"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "a":
    $ tmpInt += 1
    $ tmpList[0] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean4_event1_idle
    jump ep10_fr1_clean4_event_nofx
elif result == "b":
    $ tmpInt += 1
    $ tmpList[1] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean4_event2_idle
    jump ep10_fr1_clean4_event_nofx
elif result == "c":
    $ tmpInt += 1
    $ tmpList[2] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean4_event3_idle
    jump ep10_fr1_clean4_event_nofx
elif result == "d":
    $ tmpInt += 1
    $ tmpList[3] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean4_event4_idle
    jump ep10_fr1_clean4_event_nofx

label ep10_fr1_clean5_event_label:
$ tmpList = ["a","b","c","d","e"]
$ tmpInt = 0
$ renpy.block_rollback()
show ep10_fr1_clean5_event
show ep10_fr1_clean5_event1_idle
show ep10_fr1_clean5_event2_idle
show ep10_fr1_clean5_event3_idle
show ep10_fr1_clean5_event4_idle
show ep10_fr1_clean5_event5_idle
label ep10_fr1_clean5_event_nofx:
if tmpList == ["","","","",""]:
    hide text "Clean up [tmpInt]/5"
    $ ep10_clean += 5
    if ep10_clean >= 5:
        $ task_list[0] = ""
    else:
        $ task_list[0] = "Clean the mansion [ep10_clean]/5"
    $ updateTaskList()
    jump endEvent
show text "{=clean_text_custom}Clean up [tmpInt]/5{/=clean_text_custom}" at top

if "a" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean5_event1_idle", "ep10_fr1_clean5_event1_idle", clicked=ui.returns("a"), xpos=0, ypos=0, focus_mask=True)
if "b" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean5_event2_idle", "ep10_fr1_clean5_event2_idle", clicked=ui.returns("b"), xpos=0, ypos=0, focus_mask=True)
if "c" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean5_event3_idle", "ep10_fr1_clean5_event3_idle", clicked=ui.returns("c"), xpos=0, ypos=0, focus_mask=True)
if "d" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean5_event4_idle", "ep10_fr1_clean5_event4_idle", clicked=ui.returns("d"), xpos=0, ypos=0, focus_mask=True)
if "e" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean5_event5_idle", "ep10_fr1_clean5_event5_idle", clicked=ui.returns("e"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "a":
    $ tmpInt += 1
    $ tmpList[0] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean5_event1_idle
    jump ep10_fr1_clean5_event_nofx
elif result == "b":
    $ tmpInt += 1
    $ tmpList[1] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean5_event2_idle
    jump ep10_fr1_clean5_event_nofx
elif result == "c":
    $ tmpInt += 1
    $ tmpList[2] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean5_event3_idle
    jump ep10_fr1_clean5_event_nofx
elif result == "d":
    $ tmpInt += 1
    $ tmpList[3] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean5_event4_idle
    jump ep10_fr1_clean5_event_nofx
elif result == "e":
    $ tmpInt += 1
    $ tmpList[4] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean5_event5_idle
    jump ep10_fr1_clean5_event_nofx

label ep10_fr1_clean6_event_label:
$ ep10_clean += 5
if ep10_clean >= 5:
    $ task_list[0] = ""
else:
    $ task_list[0] = "Clean the mansion [ep10_clean]/5"
$ updateTaskList()
play sound "sound_effects/bottle_clink.mp3"
scene ep10_fr1_clean6_event1 with dissolve
mc "(Yuck... I wonder who'll volunteer to clean the puke.)"
jump endEvent

label ep10_fr1_clean8_event_label:
$ ep10_clean += 5
if ep10_clean >= 5:
    $ task_list[0] = ""
else:
    $ task_list[0] = "Clean the mansion [ep10_clean]/5"
$ updateTaskList()
play sound "sound_effects/bottle_clink.mp3"
scene ep10_fr1_clean8_event1 with dissolve
mc "(With this many bottles and cups, we will probably find bottles long after cleaning.)"
jump endEvent

label ep10_fr1_clean9_event_label:
$ ep10_clean += 5
if ep10_clean >= 5:
    $ task_list[0] = ""
else:
    $ task_list[0] = "Clean the mansion [ep10_clean]/5"
$ updateTaskList()
mc "(Ah, some more bottles.)"
play sound "sound_effects/bottle_clink.mp3"
jump endEvent

label ep10_fr1_clean10_event_label:
$ ep10_clean += 5
if ep10_clean >= 5:
    $ task_list[0] = ""
else:
    $ task_list[0] = "Clean the mansion [ep10_clean]/5"
$ updateTaskList()
play sound "sound_effects/season2/stick.mp3"
scene ep10_fr1_clean10_event1 with dissolve
mc "(Good thing I checked outside too.)"
jump endEvent

label ep10_fr1_clean7_event_label:
$ tmpList = ["a","b","c"]
$ tmpInt = 0
$ renpy.block_rollback()
show ep10_fr1_clean7_event
show ep10_fr1_clean7_event1_idle
show ep10_fr1_clean7_event2_idle
show ep10_fr1_clean7_event3_idle
label ep10_fr1_clean7_event_nofx:
if tmpList == ["","",""]:
    hide text "Clean up [tmpInt]/3"
    $ ep10_clean += 5
    if ep10_clean >= 5:
        $ task_list[0] = ""
    else:
        $ task_list[0] = "Clean the mansion [ep10_clean]/5"
    $ updateTaskList()
    jump endEvent
show text "{=clean_text_custom}Clean up [tmpInt]/3{/=clean_text_custom}" at top

if "a" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean7_event1_idle", "ep10_fr1_clean7_event1_idle", clicked=ui.returns("a"), xpos=0, ypos=0, focus_mask=True)
if "b" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean7_event2_idle", "ep10_fr1_clean7_event2_idle", clicked=ui.returns("b"), xpos=0, ypos=0, focus_mask=True)
if "c" in tmpList:
    $ ui.imagebutton("ep10_fr1_clean7_event3_idle", "ep10_fr1_clean7_event3_idle", clicked=ui.returns("c"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "a":
    $ tmpInt += 1
    $ tmpList[0] = ""
    play sound "sound_effects/season2/stick.mp3"
    hide ep10_fr1_clean7_event1_idle
    jump ep10_fr1_clean7_event_nofx
elif result == "b":
    $ tmpInt += 1
    $ tmpList[1] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean7_event2_idle
    jump ep10_fr1_clean7_event_nofx
elif result == "c":
    $ tmpInt += 1
    $ tmpList[2] = ""
    play sound "sound_effects/bottle_clink.mp3"
    hide ep10_fr1_clean7_event3_idle
    jump ep10_fr1_clean7_event_nofx

label ep10_fr1_desk_event_label:

scene ep10_fr1_desk_event1 with dissolve
mc "(Oh, yeah. This ugly mask... I'm gonna throw it out. I don't wanna be reminded of what happened with Vinny.)"
play sound "sound_effects/shove.mp3"
scene ep10_fr1_desk_event2 with hpunch
$ renpy.pause()
$ renpy.sound.play("sound_effects/season3/pb_open.mp3",channel="sfx2", loop=False)
scene ep10_fr1_desk_event3 with dissolve
mc "(Shit... Did I break it?)"
scene ep10_fr1_desk_event4 with dissolve
mc "(Huh? One of the sides opened up.)"

show screen puzzle_box_screen_ep10_fake
mc "(This is some kind of puzzle! I knew it.)"
mc "(I've got some time now... Let's see if I can crack this open.)"
hide screen puzzle_box_screen_ep10_fake
$ task_list[9] = ""
$ updateTaskList()
show screen puzzle_box_help
call screen puzzle_box_screen_ep10
hide screen puzzle_box_help
hide screen puzzle_box_wt_help
$ renpy.pause(0.5)
if pb_3_lid_open[0]:
    mc "(Hm... I made some progress, but this was harder than I thought it would be... I'll play more with this box later.)"
else:
    mc "(This was harder than I thought it would be... I'll play more with this box later.)"
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

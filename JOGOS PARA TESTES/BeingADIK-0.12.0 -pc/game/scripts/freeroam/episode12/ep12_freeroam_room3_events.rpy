label ep12_freeroam_room3_label:
show screen new_phone_screen
if roadMaya or roadJosy:
    $ roadAlone = False
if roadZoey:
    scene ep12_fr3_room25 with dissolve
    zo "Just a few more weeks and then I know for sure."
    scene ep12_fr3_room26 with dissolve
    mc "I'm hoping for the best."
    scene ep12_fr3_room25 with dissolve
    zo "Should we prepare for the worst?"
    scene ep12_fr3_room27 with dissolve
    mc "That you don't get in?"
    scene ep12_fr3_room28 with dissolve
    zo "Yeah."
    scene ep12_fr3_room27 with dissolve
    mc "I don't want to think that way."
    scene ep12_fr3_room28 with dissolve
    zo "I wanna be closer to you. If I don't get in, that's gonna be an issue, I feel."
    scene ep12_fr3_room27 with dissolve
    mc "It won't be an issue."
    scene ep12_fr3_room29 with dissolve
    zo "I'd have to keep working. Maybe I could find a job closer to here."
    mc "Where would you live?"
    scene ep12_fr3_room30 with dissolve
    zo "With you?"
    scene ep12_fr3_room31 with dissolve
    mc "Are we talking about moving in already?"
    scene ep12_fr3_room30 with dissolve
    zo "I could crash here once in a while, at least."
    scene ep12_fr3_room31 with dissolve
    mc "Well, yeah. But you can't live here permanently. We're not allowed to do that."
    scene ep12_fr3_room32 with dissolve
    zo "*{i}Sigh{/i}* I know. I wish we could skip forward two weeks and know for sure."
    scene ep12_fr3_room31 with dissolve
    mc "We'll survive, whatever the outcome is."
    scene ep12_fr3_room30 with dissolve
    zo "I love that you're so confident about it."
    scene ep12_fr3_room32 with dissolve
    zo "It feels weird to wear this dress today."
    scene ep12_fr3_room33 with dissolve
    mc "You could have borrowed my clothes."
    scene ep12_fr3_room32 with dissolve
    zo "Nah, I should get back home at some point."
    scene ep12_fr3_room31 with dissolve
    mc "Working tomorrow?"
    scene ep12_fr3_room25 with dissolve
    zo "Yep. And what about you? You'll be free until classes start, or what?"
    scene ep12_fr3_room26 with dissolve
    mc "We'll see. I'll take it day by day."
    scene ep12_fr3_room34 with dissolve
    zo "*{i}Smack{/i}* I'll call you later tonight."
    scene ep12_fr3_room26 with dissolve
    mc "Get back home safely."
elif roadJill:
    scene ep12_fr3_room24 with dissolve
    mc "*{i}Yawns{/i}*"
    mc "(I can't wait to get out of these clothes. I need a shower.)"
    scene ep12_fr3_room23 with dissolve
    mc "(Ah... As good as new.)"
elif roadSage:
    scene ep12_fr3_room1 with dissolve
    sa "*{i}Groans{/i}* It's too damn bright already."
    scene ep12_fr3_room2 with dissolve
    mc "That's usually the case with...noon."
    scene ep12_fr3_room3 with dissolve
    sa "Why are you dressed and so chipper? Shouldn't you be sleeping too?"
    scene ep12_fr3_room4 with dissolve
    mc "I slept in. And I'm feeling good today."
    scene ep12_fr3_room6 with dissolve
    sa "You didn't drink enough."
    scene ep12_fr3_room5 with dissolve
    mc "Maybe that was it."
    scene ep12_fr3_room6 with dissolve
    sa "Ugh..."
    scene ep12_fr3_room7 with dissolve
    mc "I know you're hungover, but I gotta say I love waking up next to you."
    scene ep12_fr3_room8 with dissolve
    sa "Less talking, more fetching me coffee."
    scene ep12_fr3_room7 with dissolve
    mc "Haha! I'll get right on it."
elif roadQuinn:
    $ roadAlone = False
    scene ep12_fr3_room9 with dissolve
    mc "Morning."
    scene ep12_fr3_room10 with dissolve
    qu "Don't shout."
    scene ep12_fr3_room11 with dissolve
    mc "I wasn't. Hungover?"
    scene ep12_fr3_room10 with dissolve
    qu "The question is, why aren't you?"
    scene ep12_fr3_room11 with dissolve
    mc "I think it was the food. I rarely get hungover after eating a lot."
    scene ep12_fr3_room12 with dissolve
    qu "Lucky you."
    scene ep12_fr3_room13 with dissolve
    mc "Can I get you something for the hangover? Coffee?"
    scene ep12_fr3_room12 with dissolve
    qu "A shot."
    scene ep12_fr3_room13 with dissolve
    mc "Really?"
    scene ep12_fr3_room14 with dissolve
    qu "It's far more effective."
    scene ep12_fr3_room15 with dissolve
    mc "I'm not sure if we have any. We brought most of our liquor to the party."
    scene ep12_fr3_room14 with dissolve
    qu "It's fine. I'll head home for one."
    scene ep12_fr3_room16 with dissolve
    mc "Not staying for breakfast?"
    qu "Nah..."
    scene ep12_fr3_room17 with dissolve
    mc "Are you sure? I can even bring it to you."
    scene ep12_fr3_room18 with dissolve
    qu "I stayed the night, didn't I? Take the fucking win."
    scene ep12_fr3_room19 with dissolve
    qu "*{i}Smack{/i}*"
    scene ep12_fr3_room20 with dissolve
    mc "Talk later then."
else:
    if breakup:
        $ roadAlone = True
    scene ep12_fr3_room22 with dissolve
    $ renpy.pause()
    if roadAlone:
        scene ep12_fr3_room21 with dissolve
    else:
        scene ep12_fr3_room21b with dissolve
    mc "(Yep... It's already decided. I'm not doing shit today.)"
jump ep12_fr_room3_setup_label

label ep12_fr_sage_event_label:
scene ep12_fr_sage_event1 with dissolve
mc "Feeling better?"
scene ep12_fr_sage_event2 with dissolve
sa "Just slightly."
scene ep12_fr_sage_event3 with dissolve
mc "No sweat. It's not like we have something better to do today. Clean-up can wait, yeah?"
scene ep12_fr_sage_event2 with dissolve
sa "Yeah."
scene ep12_fr_sage_event1 with dissolve
mc "So, what do you want to talk about?"
scene ep12_fr_sage_event2 with dissolve
sa "I'm more of a listener today, if you don't mind."
if ep12_brawler_comp_won:
    scene ep12_fr_sage_event4 with dissolve
    mc "If that's the case, I have something I'd like to talk about."
    mc "After I won the fight, I was approached by a scout. She offered me her services and a partnership."
    scene ep12_fr_sage_event5 with dissolve
    sa "For what? Like, fighting professionally?"
    scene ep12_fr_sage_event4 with dissolve
    mc "Yeah. It's a stepping stone, for sure."
    mc "The guys in the club couldn't believe it. Apparently, it's not that common."
    scene ep12_fr_sage_event6 with dissolve
    mc "But the thing is, I'm unsure if I want to do this for a living."
    scene ep12_fr_sage_event7 with dissolve
    sa "Could you stay here while doing that?"
    scene ep12_fr_sage_event9 with dissolve
    mc "Yeah. I think so."
    mc "I told the scout that I'm in college and such, and she said that wasn't a problem."
    scene ep12_fr_sage_event10 with dissolve
    mc "I could still study and maybe even get a job without it affecting the deal much."
    mc "As long as I fight, I guess, it's ok to do other things too."
    scene ep12_fr_sage_event11 with dissolve
    mc "I've been looking at her card every day since I got it."
    mc "A part of me thinks it's too much for me. That I'm not cut out for that life."
    mc "And there's another part saying I'm stupid for wasting this opportunity."
    mc "What do you think?"
    scene ep12_fr_sage_event8 with dissolve
    sa "I think you already know the answer without me telling you."
    sa "You're checking that card daily. That doesn't sound like someone who doesn't want to go through with something."
    sa "It sounds like you're hesitant to pull the trigger."
    scene ep12_fr_sage_event9 with dissolve
    mc "It is scary... Because it might be binding..."
    scene ep12_fr_sage_event8 with dissolve
    sa "Call her and find out."
    scene ep12_fr_sage_event13 with dissolve
    mc "Thanks. I'm gonna."
elif ep11_music:
    scene ep12_fr_sage_event4 with dissolve
    mc "If that's the case, I have something I'd like to talk about."
    mc "This guy at the faculty party asked me if I wanted a summer job at his company."
    scene ep12_fr_sage_event5 with dissolve
    sa "Oh? Who and what company?"
    scene ep12_fr_sage_event4 with dissolve
    mc "His name is David Cerus Baxter."
    scene ep12_fr_sage_event5 with dissolve
    sa "Wow, you remembered his full name."
    scene ep12_fr_sage_event12 with dissolve
    mc "I got his business card. He's the CEO of BaxTec. It's a MedTech company."
    scene ep12_fr_sage_event15 with dissolve
    sa "Flashy. He just offered you a job like that?"
    scene ep12_fr_sage_event16 with dissolve
    mc "Yeah. He liked my vibe."
    scene ep12_fr_sage_event17 with dissolve
    sa "Maybe that's not all he liked."
    scene ep12_fr_sage_event16 with dissolve
    mc "I know I'm hot, but no, that wasn't the vibe I got, ok?"
    scene ep12_fr_sage_event15 with dissolve
    sa "[name] got a new boyfriend."
    if ep8_told_sage_chad_troy:
        sa "Damn... I sure know how to pick 'em. That's two for two."
    scene ep12_fr_sage_event16 with dissolve
    mc "Shut up. I thought you were gonna listen."
    scene ep12_fr_sage_event18 with dissolve
    sa "Haha!"
    scene ep12_fr_sage_event9 with dissolve
    mc "So, what do you think?"
    scene ep12_fr_sage_event8 with dissolve
    sa "It's great that you landed a summer job."
    scene ep12_fr_sage_event10 with dissolve
    mc "I haven't contacted him about that yet."
    scene ep12_fr_sage_event8 with dissolve
    sa "But you're gonna, right?"
    scene ep12_fr_sage_event9 with dissolve
    mc "I think so, yeah."
    mc "But it's silly..."
    scene ep12_fr_sage_event8 with dissolve
    sa "What is?"
    scene ep12_fr_sage_event6 with dissolve
    mc "A part of me thought I'd be going back home to Dad this summer and maybe work at the minimart again or something like that."
    scene ep12_fr_sage_event8 with dissolve
    sa "It sounds like someone needs to step out of his comfort zone, if you ask me."
    scene ep12_fr_sage_event19 with dissolve
    mc "You think that's playing it too safe?"
    scene ep12_fr_sage_event8 with dissolve
    sa "You got an opportunity for a job in a field you're studying for. What do you think?"
    sa "Why waste that on going back to doing something you already did in the past? What's the point of even going to college if you're gonna regress?"
    scene ep12_fr_sage_event19 with dissolve
    mc "When you put it like that, you make me feel stupid."
    scene ep12_fr_sage_event15 with dissolve
    sa "Good. Don't be a fool. Call your boyfriend already."
    scene ep12_fr_sage_event14 with dissolve
    mc "Bah... I'm gonna."
    scene ep12_fr_sage_event18 with dissolve
    sa "Haha! You even got tired of denying it."
else:
    scene ep12_fr_sage_event3 with dissolve
    mc "That's alright. I don't have much to talk about, anyway."
    scene ep12_fr_sage_event2 with dissolve
    sa "That works for me too."

$ task_list[1] = ""
if ep11_music:
    $ task_list[1] = "Call David Cerus Baxter"
    $ event_list.append("ep12_fr_dav_event_label")
if ep12_brawler_comp_won:
    $ task_list[1] = "Call Jen Byson"
    $ event_list.append("ep12_fr_jen_event_label")
$ event_list.append("trigger_active")
$ updateTaskList()
jump endEvent

label ep12_fr_sage_leave_label:
scene ep12_fr_sage_leave1 with dissolve
sa "I'm gonna head back home, grab a shower, and put on some fresh clothes."
scene ep12_fr_sage_leave2 with dissolve
mc "Why? You look great wearing mine."
scene ep12_fr_sage_leave3 with dissolve
sa "I do like the jacket. Can I borrow it?"
scene ep12_fr_sage_leave2 with dissolve
mc "Sure. And remember, if you want to pledge the DIKs, it's almost time."
scene ep12_fr_sage_leave1 with dissolve
sa "Ugh... Don't remind me. We have to accept more HOTs again."
sa "Talk later. Thanks for everything."
scene ep12_fr_sage_leave4 with dissolve
sa "Love you."
stop music fadeout 3
scene ep12_fr_sage_leave5 with dissolve
mc "Me too."
jump ep12_sally_end_label

label ep12_fr_dav_event_label:
scene ep12_fr_dav_event7 with dissolve
$ renpy.pause()
scene ep12_fr_dav_event8 with dissolve
mc "(I'm doing it.)"
scene ep12_fr_jen_event3 with dissolve
dav "*{i}Hoarse voice{/i}* Yeah, it's David."
scene ep12_fr_jen_event4 with dissolve
mc "David! Hi! It's...uh...[name]. From the Christmas party."
scene ep12_fr_jen_event3 with dissolve
dav "Oh. Excuse me, one second."
scene ep12_fr_dav_event9 with dissolve
$ renpy.pause()
scene ep12_fr_dav_event10 with dissolve
dav "I'm back. Sorry about that. I'm a bit hungover from yesterday."
scene ep12_fr_dav_event11 with dissolve
mc "Oh... I hope I didn't wake you up."
scene ep12_fr_dav_event10 with dissolve
dav "Don't worry, I should get out of bed anyway."
scene ep12_fr_dav_event11 with dissolve
mc "I wanted to tell you that I'm interested in that summer job, if the offer is still on the table."
scene ep12_fr_dav_event9 with dissolve
dav "Yeah, yeah. I'm glad to hear that. Haha, you could have sent me an e-mail like I asked, though."
scene ep12_fr_dav_event11 with dissolve
mc "Oh, right. I'm sorry about that. I thought I'd make a better impression by giving you a call, but - haha - I clearly did not."
scene ep12_fr_dav_event10 with dissolve
dav "Haha. No sweat. It's me who should have given you a better impression."
dav "How about we forget this phone call, and you send me an e-mail with your info? Then I'll set up a meeting later this year regarding the job."
scene ep12_fr_dav_event12 with dissolve
mc "Yes. That sounds perfect! I'll do that."
mc "Uh... Thanks again for this opportunity! Oh! And Happy New Year!"
scene ep12_fr_dav_event13 with dissolve
dav "You too, [name]."
scene ep12_fr_dav_event14 with dissolve
$ renpy.pause()

if roadSage:
    scene ep12_fr_dav_event1 with dissolve
    sa "What did he say?"
    scene ep12_fr_dav_event2 with dissolve
    mc "He said he was hungover from last year's party..."
    mc "I should have waited to call him. Fuck..."
    scene ep12_fr_dav_event1 with dissolve
    sa "That's how it is with dating. You don't call the guy immediately; you have to wait at least a week, or you'll look too clingy."
    scene ep12_fr_dav_event3 with dissolve
    mc "Well, he still offered me the job, but told me to send my info over email."
    mc "I'll get called to an interview sometime later this year."
    scene ep12_fr_dav_event4 with dissolve
    sa "Congratulations."
    scene ep12_fr_dav_event3 with dissolve
    mc "Thanks... It feels good!"
$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep12_fr_jen_event_label:
scene ep12_fr_jen_event1 with dissolve
$ renpy.pause()
scene ep12_fr_jen_event2 with dissolve
mc "(I'm doing it.)"
scene ep12_fr_jen_event3 with dissolve
jen "Byson."
scene ep12_fr_jen_event4 with dissolve
mc "Um... Hi! It's [name]. [name] [lname]. I don't know if you remember me..."
scene ep12_fr_jen_event5 with dissolve
jen "Of course, I remember you, [name]. Happy New Year!"
scene ep12_fr_jen_event6 with dissolve
mc "Oh! Happy New Year! Did you have a nice time yesterday?"
scene ep12_fr_jen_event5 with dissolve
jen "I went to a party with my friends. We had a great time, thanks for asking. And you?"
scene ep12_fr_jen_event6 with dissolve
mc "My frat co-hosted a party. We also had a nice end to the year."
scene ep12_fr_jen_event5 with dissolve
jen "Sounds lovely. So, [name], are you calling me with good or bad news?"
scene ep12_fr_jen_event4 with dissolve
mc "I'm calling to ask you a question."
scene ep12_fr_jen_event3 with dissolve
jen "Shoot."
scene ep12_fr_jen_event7 with dissolve
mc "If I accept your representation... Is it binding?"
scene ep12_fr_jen_event9 with dissolve
jen "The terms depend on the fighter. My agency has signed contracts binding fighters from one year to five years."
jen "Sometimes, we even base the contracts on a set number of fights."
jen "And many contracts can be renewed with updated terms."
scene ep12_fr_jen_event10 with dissolve
jen "We would rather sign long-term contracts, as it's a big investment on our end and we might not see a return for quite some time."
jen "That's why I would recommend that we sign a three-year contract, or 15 fights."
scene ep12_fr_jen_event9 with dissolve
jen "It is binding, yes. And we will get exclusive rights to you as a fighter. But we can get into every clause, should you wish to sign."
scene ep12_fr_jen_event7 with dissolve
mc "I see..."
scene ep12_fr_jen_event9 with dissolve
jen "Is that what worries you - that it is binding?"
scene ep12_fr_jen_event8 with dissolve
mc "I'm worried about what would happen if I regret it, that's all."
scene ep12_fr_jen_event10 with dissolve
jen "Given that you're new to all of this, I understand your trepidation."
jen "We could do a trial period, and if you still feel the same after that, you'll get an out."
scene ep12_fr_jen_event8 with dissolve
mc "Hm... Ok..."
scene ep12_fr_jen_event9 with dissolve
jen "Let's set up a meeting next week. I'll have our lawyer present to explain the contract in depth."
scene ep12_fr_jen_event8 with dissolve
mc "*{i}Exhales{/i}* This is more scary than the fight, haha."
scene ep12_fr_jen_event10 with dissolve
jen "Aw, aren't you sweet? I know it can be intimidating. But, trust me, this is a great opportunity for you and potentially even for us."
menu:
    "Accept":
        $ ep12_accepted_jen = True
        scene ep12_fr_jen_event11 with dissolve
        mc "I'll do it. I want to sign with you."
        scene ep12_fr_jen_event12 with dissolve
        jen "Haha! I still think we should have a meeting, but I love your answer."
        scene ep12_fr_jen_event11 with dissolve
        mc "Yes. Let's have a meeting. *{i}Phew{/i}*"
        mc "I'm looking forward to this."
        scene ep12_fr_jen_event12 with dissolve
        jen "[name]. I'm looking forward to it too."
        jen "I'll send you the details when I get back to my office tomorrow or the day after that."
        scene ep12_fr_jen_event13 with dissolve
        mc "Talk soon, then. Bye!"
        scene ep12_fr_jen_event14 with dissolve
        jen "Haha. Bye, [name]."
        scene ep12_fr_jen_event15 with dissolve
        $ renpy.pause()
        play sound "sound_effects/whoosh.mp3"
        scene ep12_fr_jen_event17 with vpunch
        mc "Yes!!!"
        if roadSage:
            scene ep12_fr_dav_event1 with dissolve
            sa "What happened?"
            scene ep12_fr_dav_event3 with dissolve
            mc "I'm doing it! I'm going through with it!"
            scene ep12_fr_dav_event4 with dissolve
            sa "For real? What did she say?"
            scene ep12_fr_dav_event3 with dissolve
            mc "We're gonna meet next week and talk about it. Most likely, we're talking about a three-year contract with a trial period."
            scene ep12_fr_dav_event4 with dissolve
            sa "Congratulations!"
            scene ep12_fr_dav_event3 with dissolve
            mc "Thanks! Wow... I don't know why, but it's like a weight came off my shoulders."
            scene ep12_fr_dav_event5 with dissolve
            sa "See! You knew you wanted this."
        $ new_bio("You", "I accepted Jen's offer to represent me as a fighter.")
    "Decline":
        $ ep12_accepted_jen = False
        scene ep12_fr_jen_event8 with dissolve
        mc "You know what? I will have to think some more about this."
        scene ep12_fr_jen_event9 with dissolve
        jen "Are you sure, [name]?"
        scene ep12_fr_jen_event7 with dissolve
        mc "No, you're right... I already know that I can't do this. Sorry for wasting your time."
        mc "I have to decline."
        scene ep12_fr_jen_event9 with dissolve
        jen "That saddens me, [name]. But thank you for entertaining the idea."
        jen "Best of luck to you."
        scene ep12_fr_jen_event8 with dissolve
        mc "Thanks... Bye."
        scene ep12_fr_jen_event16 with dissolve
        mc "Fuck!"
        if roadSage:
            scene ep12_fr_dav_event1 with dissolve
            sa "What happened?"
            scene ep12_fr_dav_event2 with dissolve
            mc "I couldn't go through with it."
            scene ep12_fr_dav_event1 with dissolve
            sa "You turned her down?"
            scene ep12_fr_dav_event6 with dissolve
            mc "It's not what I want to do. She wanted to lock me up for three years."
            mc "After hearing that, I knew that I didn't want it that much."
            scene ep12_fr_dav_event1 with dissolve
            sa "Aw... That sucks. But hey, at least you know for sure what you want."
            scene ep12_fr_dav_event6 with dissolve
            mc "Yeah... Dwyane's not gonna like hearing that I turned her down."
            scene ep12_fr_dav_event1 with dissolve
            sa "It's your life and your call."
        $ new_bio("You", "I declined Jen's offer to represent me as a fighter.")

$ task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep12_fr_remove_label:
if "Sage" in breakup:
    scene ep12_fr_remove2 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove1 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season3/crumble.mp3"
    scene ep12_fr_remove3 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove4 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove5 with dissolve
    mc "(What's that stupid saying? New year, new me.)"
    if ep8_current_second_painting == 9 or ep8_current_second_painting == 10 or ep8_current_second_painting == 16:
        $ ep8_current_second_painting = 0
    if ep7_current_desk_painting == 13:
        $ ep7_current_desk_painting = 0
elif "Jill" in breakup:
    scene ep12_fr_remove6 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove7 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove5 with dissolve
    mc "(What's that stupid saying? New year, new me.)"
    mc "(This has to go.)"
    if ep8_current_second_painting == 4 or ep8_current_second_painting == 3 or ep8_current_second_painting == 12:
        $ ep8_current_second_painting = 0
    if ep7_current_desk_painting == 6:
        $ ep7_current_desk_painting = 0
elif "Josy" in breakup and "Maya" in breakup:
    scene ep12_fr_remove10 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove11 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove5 with dissolve
    mc "(What's that stupid saying? New year, new me.)"
    mc "(This has to go.)"
    if ep8_current_second_painting == 5 or ep8_current_second_painting == 6 or ep8_current_second_painting == 7 or ep8_current_second_painting == 8 or ep8_current_second_painting == 13 or ep8_current_second_painting == 14:
        $ ep8_current_second_painting = 0
    if ep7_current_desk_painting == 7:
        $ ep7_current_desk_painting = 0
    if ep7_current_desk_painting == 9:
        $ ep7_current_desk_painting = 0
elif "Isabella" in breakup:
    scene ep12_fr_remove8 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove9 with dissolve
    $ renpy.pause()
    scene ep12_fr_remove5 with dissolve
    mc "(What's that stupid saying? New year, new me.)"
    mc "(This has to go.)"
    if ep8_current_second_painting == 1 or ep8_current_second_painting == 2 or ep8_current_second_painting == 11:
        $ ep8_current_second_painting = 0
    if ep7_current_desk_painting == 4:
        $ ep7_current_desk_painting = 0

$ task_list[0] = ""
$ updateTaskList()
jump endEvent

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

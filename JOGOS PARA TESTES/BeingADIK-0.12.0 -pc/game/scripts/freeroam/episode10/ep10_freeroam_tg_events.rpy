label ep10_tg_pills_event_label:
mc "(Someone's notepad.)"
menu:
    "Read it":
        $ ep10_read_notepad = True
    "Leave it alone":
        mc "(No, I'm not going to pry.)"
        jump endEvent

scene ep10_tg_pills_event1 with dissolve
mc "(Hm... A schedule for meds. And... Uh...)"
scene ep10_tg_pills_event3 with dissolve
$ renpy.pause()
scene ep10_tg_pills_event2 with dissolve
mc "(Why the fuck did I have to read that? I feel sick.)"
jump endEvent

label ep10_tg_mp_label:
if ep8_told_josy_chad:
    scene ep10_tg_mp1 with dissolve
    pa "A boyfriend?"
    scene ep10_tg_mp7 with dissolve
    my "Yes. It's the truth."
    scene ep10_tg_mp2 with dissolve
    pa "I'm having a hard time believing you."
    scene ep10_tg_mp8 with dissolve
    my "I didn't bring him here for you to be convinced. I brought him here because I wanted him to meet my family."
    my "I thought you'd be thrilled."
    scene ep10_tg_mp3 with dissolve
    pa "..."
    scene ep10_tg_mp4 with dissolve
    pa "I'm sorry."
    scene ep10_tg_mp9 with dissolve
    my "You're sorry?"
    scene ep10_tg_mp4 with dissolve
    pa "It will make your mom happy."
    if ep7_patrick_score < 0:
        scene ep10_tg_mp5 with dissolve
        pa "I can't say that I've gotten a good first impression of [name], but maybe time will take care of that."
        scene ep10_tg_mp4 with dissolve
    else:
        pa "And you seem to have found yourself a sensible guy, too."
    pa "I look forward to getting to know him."
    scene ep10_tg_mp10 with dissolve
    my "Ok..."
else:
    scene ep10_tg_mp1 with dissolve
    pa "So, you got a single dorm now?"
    scene ep10_tg_mp7 with dissolve
    my "Yeah, and I don't think there will be another roommate for at least my first year of college."
    scene ep10_tg_mp2 with dissolve
    pa "I assumed that the spot would get taken instantly by another student."
    pa "Isn't there a shortage of accommodation at B&R?"
    scene ep10_tg_mp7 with dissolve
    my "It's in the middle of the semester, Dad. Many have quit college already."
    my "I know several who left for different reasons."
    scene ep10_tg_mp2 with dissolve
    pa "Aha."
    scene ep10_tg_mp8 with dissolve
    my "Don't you believe me?"
    scene ep10_tg_mp2 with dissolve
    pa "It sounds too convenient, that's all."
    scene ep10_tg_mp8 with dissolve
    my "I'm sorry that the truth is too convenient for you."
    scene ep10_tg_mp6 with dissolve
    pa "Do not start. Think about your mother. This night means a lot to her."

if "ep10_tg2_mp_label" in event_list:
    $ event_list.remove("ep10_tg2_mp_label")
    jump ep10_tg2_mp_label
jump endEvent

label ep10_tg2_mp_label:
scene ep10_tg2_mp1 with dissolve
mc "Maya? Your mom needs her meds."
scene ep10_tg_mp4 with dissolve
pa "It's time for her morphine, yes. It's on her walker."
scene ep10_tg2_mp2 with dissolve
my "I'll get it."

scene ep10_tg2_mp3 with dissolve
mc "Hey..."
if ep8_told_josy_chad:
    if branchMayaJosy:
        mc "I overheard you talking to your dad... How did that feel?"
    else:
        mc "I overheard you talking to your dad... How did that feel? It seems like he bought it."
    scene ep10_tg2_mp5 with dissolve
    my "I'm stunned, [name]."
    my "This is what it should feel like when you tell your parents about your partner."
    scene ep10_tg2_mp4 with dissolve
    my "It makes me mad that he has that in him but only shows it when I'm \"straight\"."
    my "It doesn't feel good at all. Him accepting you just like that makes me feel worse."
    scene ep10_tg2_mp6 with dissolve
    mc "I'm sorry..."
    scene ep10_tg2_mp5 with dissolve
    my "Tonight is not about that. Any luck with the contract yet?"
else:
    mc "I overheard you talking to your dad... How are you holding up?"
    scene ep10_tg2_mp5 with dissolve
    my "*{i}Sigh{/i}*"
    my "This will be a long night."
    scene ep10_tg2_mp4 with dissolve
    my "Even when I mix the truth into my stories, he sees right through my lies."
    scene ep10_tg2_mp3 with dissolve
    mc "Maybe he's choosing to distrust you regardless of what you say."
    scene ep10_tg2_mp6 with dissolve
    my "..."
    scene ep10_tg2_mp4 with dissolve
    my "Any luck with the contract yet?"
scene ep10_tg2_mp3 with dissolve
if "ep10_tg_d_label" in event_list:
    mc "No, not yet."
else:
    mc "No, not yet. The door is locked."
scene ep10_tg2_mp4 with dissolve
my "Ok. I believe in you. I'm gonna give Mom her morphine."
$ event_list.append("tg_part1b")
if not "ep10_tg_d_label" in event_list:
    $ event_list.append("ep10_tg_dinner_label")
jump endEvent

label ep10_tg_helen_label:
scene ep10_tg_helen1 with dissolve
de "Hey, Mom. How are you feeling?"
scene ep10_tg_helen3 with dissolve
hl "Aw, my boy! You're finally back home."
hl "I've missed you so much."
scene ep10_tg_helen4 with dissolve
hl "Look at you. You look so nice with that sweater on."
scene ep10_tg_helen1 with dissolve
de "It's the one you and Dad bought me for Christmas."
scene ep10_tg_helen3 with dissolve
hl "Yes, I remember. You're so handsome and strong. Did you work out more?"
scene ep10_tg_helen1 with dissolve
de "Oh, Mom. Stop it. Haha..."
if ep8_told_josy_chad:
    de "We brought a couple of guests for tonight. I hope that's still fine with you."
else:
    de "I brought a close friend here for tonight. I hope that's still fine with you."
scene ep10_tg_helen4 with dissolve
hl "Of course, it is. Your friends are always welcome here."
scene ep10_tg_helen5 with dissolve
hl "*{i}Grunts{/i}*"
scene ep10_tg_helen2 with dissolve
de "Can I do something for you?"
scene ep10_tg_helen3 with dissolve
hl "No, it's almost time for my meds. I'll have to endure."
hl "I had to wake up at 5 a.m. to get ready for today."
scene ep10_tg_helen1 with dissolve
de "You look beautiful."
scene ep10_tg_helen6 with dissolve
de "[name]! Come in."
if affinity == "CHICK":
    mc "Are you sure? I can come back later."
scene ep10_tg_helen7 with dissolve
if affinity == "CHICK":
    de "It's fine."
de "Mom, I'd like you to meet my best friend. This is [name]."
de "[name], this is my mom, Helen."
scene ep10_tg_helen8 with dissolve
mc "Hello. It's nice to meet you."
scene ep10_tg_helen10 with dissolve
hl "Hi, dear. Welcome. It's nice to finally meet you. I've heard a lot about you from Derek."
scene ep10_tg_helen8 with dissolve
mc "Oh, really? Only good things, I hope."
scene ep10_tg_helen10 with dissolve
hl "Yes, of course. He's told me all about your college adventures."
hl "What your first week at college was like and how you two stuck together since the beginning of it."
scene ep10_tg_helen8 with dissolve
mc "Our college adventures? Like, when we...?"
scene anim_derek_tg_ep10 with dissolve
pause
scene ep10_tg_helen8 with dissolve
mc "When we...uh...discovered campus together?"
scene ep10_tg_helen7 with dissolve
de "No, I didn't tell her about that one. But it's a fun story! Maybe there'll be time for it later."
scene ep10_tg_helen11 with dissolve
hl "I would love to hear it. Sweetie, can you get me my pill box?"
scene ep10_tg_helen7 with dissolve
de "[mc_de_up]- [name]! Can you tell Maya that Mom needs her meds?"
scene ep10_tg_helen9 with dissolve
mc "Yes, of course."
scene ep10_tg_helen10 with dissolve
hl "Thank you, dear."
$ event_list.append("ep10_tg2_mp_label")
jump endEvent

label ep10_tg_hall_derek_label:
scene ep10_tg_hall_derek1 with dissolve
de "He'll be busy with dessert for a while. Now's your shot. I'll keep an eye on him."
scene ep10_tg_hall_derek2 with dissolve
mc "Are you sure?"
scene ep10_tg_hall_derek1 with dissolve
de "Trust the dildo, [mc_de]."

jump endEvent

label ep10_tg_d_label:
$ guideSuggestedPage = 141
if ep8_told_josy_chad:
    scene ep10_tg_d1 with dissolve
    sa "*{i}Psst{/i}* [name]..."
    scene ep10_tg_d2 with dissolve
    mc "Is this the door?"
    scene ep10_tg_d3 with dissolve
    sa "Yeah. But it's locked."
    play sound "sound_effects/door_lock.mp3"
    scene ep10_tg_d4 with dissolve
    mc "Yeah, it's locked."
    scene ep10_tg_d5 with dissolve
    sa "Why did you have to check? I told you it was locked."
    scene ep10_tg_d6 with dissolve
    mc "Uh... So, where's the key?"
    scene ep10_tg_d7 with dissolve
    sa "If it was me, I'd put it on my keychain or in a bowl by the front door."
    scene ep10_tg_d6 with dissolve
    mc "All right... Maybe Derek or Maya know where it is."
    scene ep10_tg_d7 with dissolve
    sa "I'm gonna take \"the house tour\" and look for it. I suggest you do the same."
    scene ep10_tg_d6 with dissolve
    mc "Good call."
    scene ep10_tg_d8 with dissolve
    sa "..."
    mc "(There's something up with Sage...)"
    menu:
        "How are you?":
            mc "Sage... How are you?"
            scene ep10_tg_d7 with dissolve
            sa "Huh? I'm...fine."
            scene ep10_tg_d6 with dissolve
            mc "Are you sure? You seem a bit off."
            scene ep10_tg_d9 with dissolve
            sa "Not here. Ok?"
            scene ep10_tg_d8 with dissolve
            mc "Ok. I understand. When you're ok with it, then."
            scene ep10_tg_d9 with dissolve
            sa "Yeah."
        "Leave it for later":
            mc "(It can wait.)"
else:
    scene ep10_tg_d10 with dissolve
    mc "(Hm... Could this be the door?)"
    play sound "sound_effects/door_lock.mp3"
    scene ep10_tg_d10 with hpunch
    mc "(Locked...)"
    scene ep10_tg_d12 with dissolve
    mc "(It's dark, but there's light shining through the windows.)"
    mc "(A desk. A computer. A shelf of binders. Bingo!)"
    scene ep10_tg_d11 with dissolve
    mc "(Ok. Now I know where to look. But I have to find the key first. Maybe Derek or Maya know where it is.)"

if "tg_part1b" in event_list:
    $ event_list.append("ep10_tg_dinner_label")
jump endEvent

label ep10_tg_keys_label:
scene ep10_tg_keys1 with dissolve
mc "(This must be where the keys are.)"
scene ep10_tg_keys2 with dissolve
mc "(The code to the padlock... 0505, was it?)"
mc "(Yes... It's open.)"
scene ep10_tg_keys3 with dissolve
mc "(Which key is it!?)"
$ currentFreeRoamLabel = "ep10_fr_tg_garage_keys_label_nofx"
jump endEvent


label ep10_tg_hide_event_label:
scene ep10_fr_tg_end7 with dissolve
play sound "sound_effects/key_jiggle.mp3"
play music "music/ep9/licensed_music/track116.mp3"
mc "(Please be the right set of keys... Please...)"
mc "(Nope, that's not it... What about this one?)"
play sound "sound_effects/season3/vibrate_single.mp3"
scene ep10_tg_hide_event1 with vpunch
"*{i}Vibration{/i}*"
mc "(Fuck! I need to hide!)"
$ guideSuggestedPage = 147
scene ep10_tg_hide_event2 with dissolve
menu:
    "Maya's room":
        jump ep10_tg_hide_mroom_label
    "Derek's room":
        jump ep10_tg_hide_droom_label


label ep10_tg_hide_mroom_label:
scene ep10_tg_hide_mroom1 with dissolve
mc "(Maya's room... Where the fuck do I hide?)"
menu:
    "[mod_gr]Under the bed":
        $ renpy.block_rollback()
        scene ep10_tg_hide_mroom5 with dissolve
        mc "(If he spots me, I won't be talking my way out of this easily...)"
        $ renpy.sound.play("sound_effects/season3/door_squeek.mp3", channel="sfx2", loop=False)
        $ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
        scene ep10_tg_hide_mroom8 with dissolve
        $ renpy.pause()
        scene ep10_tg_hide_mroom6 with dissolve
        $ renpy.pause()
        play sound "sound_effects/door_close.mp3"
        $ renpy.music.stop(channel="sfx1", fadeout=1)
        scene ep10_tg_hide_mroom7 with dissolve
        $ renpy.pause()
        mc "(Fuck, that was too close... I should have gone with the bathroom.)"
        mc "(Don't panic...)"
        play sound "sound_effects/season2/vibrate.mp3"
        scene ep10_tg_hide_mroom9 with hpunch
        "*{i}Vibrations{/i}*"
        mc "(Ok, time to move. Man, I can't believe a dildo is keeping me safe.)"
    "In the corner":
        $ renpy.block_rollback()
        scene ep10_tg_hide_mroom2 with dissolve
        mc "(I hope this will be enough... At least I can talk my way out of standing here.)"
        scene ep10_tg_hide_mroom3 with dissolve
        pa "[name]? What are you doing in here?"
        mc "(Fuck!)"
        scene ep10_tg_hide_mroom4 with dissolve
        mc "I got lost looking for the bathroom and ended up in here."
        scene ep10_tg_hide_mroom3 with dissolve
        pa "This is Maya's room. Didn't she show you it?"
        scene ep10_tg_hide_mroom4 with dissolve
        mc "No, we didn't find the time for a house tour."
        scene ep10_tg_hide_mroom3 with dissolve
        pa "Ah..."
        jump ep10_tg_failed_hideb_label

jump ep10_tg_after_hide_label

label ep10_tg_failed_hide_label:
pa "There you are. Did you get lost?"
mc "Yeah, I was looking for the bathroom. It's a big house."
scene ep10_tg_failed_hide2 with dissolve
pa "Not really."
label ep10_tg_failed_hideb_label:
$ ep10_patrick_penalty += 3
scene ep10_tg_failed_hide3 with dissolve
pa "Wait a moment."
pa "The bathroom is in here. Go ahead. I need to use it, too."
mc "Oh?"
mc "(Fuck...)"
play sound "sound_effects/season2/flush.mp3"
scene ep10_tg_after_hide5 with fade
pa "Dessert is shortly. We'll be waiting for you."
scene ep10_tg_after_hide6 with dissolve
stop music fadeout 3
mc "(This backfired... I can't stay upstairs now, or he'll notice I'm snooping around.)"
play music "music/ep9/relaxed.mp3"
queue music ["music/ep7/morning_routine.mp3","music/ep9/passing_time.mp3","music/ep1/fresh_air.mp3","music/ep9/getting_closure.mp3","music/ep9/relaxed.mp3"]
jump ep10_tg_after_hide2_label

label ep10_tg_after_hide_label:
scene ep10_tg_after_hide1 with dissolve
mc "(I made it!)"
play sound "sound_effects/key_jiggle.mp3"
scene ep10_fr_tg_end7 with dissolve
mc "(Which key is it?)"
mc "(Not that one...)"
mc "(Not that one either... Fucking hurry!)"
$ renpy.sound.play("sound_effects/season3/door_squeek.mp3", channel="sfx2", loop=False)
scene ep10_tg_after_hide2 with dissolve
mc "(Yes! This is the one. It's open!)"
play sound "sound_effects/season3/vibrate_single.mp3"
scene ep10_tg_after_hide3 with vpunch
"*{i}Vibration{/i}*"
mc "(No! Not now!)"
mc "(If he notices the door is unlocked, it's over...)"
play sound "sound_effects/key_jiggle.mp3"
scene ep10_fr_tg_end7 with dissolve
mc "(Fuck! Stop shaking!)"
scene ep10_tg_after_hide4 with dissolve
mc "(Hurry! The bathroom was this one, right?)"
play sound "sound_effects/door_close.mp3"
scene ep10_tg_after_hide7 with dissolve
mc "*{i}Phew{/i}*"
stop music fadeout 3
mc "(At least he won't question me going to the bathroom.)"
scene ep10_tg_after_hide8 with wipeleft
play music "music/ep9/relaxed.mp3"
queue music ["music/ep7/morning_routine.mp3","music/ep9/passing_time.mp3","music/ep1/fresh_air.mp3","music/ep9/getting_closure.mp3","music/ep9/relaxed.mp3"]
mc "(Is he still out there?)"
mc "(Derek hasn't sent me another signal yet, so he must be.)"
mc "(Ok, I gotta do something. Pretend to flush and exit...)"
play sound "sound_effects/season2/flush.mp3"
scene ep10_tg_after_hide5 with dissolve
pa "There you are. You almost made me use the bathroom downstairs."
pa "Dessert is shortly. I'll be a minute."
scene ep10_tg_after_hide6 with dissolve
mc "(Fuck... I should have trusted my gut and waited...)"
mc "(I can't stay upstairs now, or he'll notice I'm snooping around.)"
jump ep10_tg_after_hide2_label

label ep10_tg_hide_droom_label:
scene ep10_tg_hide_droom1 with dissolve
mc "(There's nowhere to hide in here! Fuck!!!)"
menu:
    "Run into Maya's room":
        $ renpy.block_rollback()
        mc "(There's still time to hide someplace else, right?)"
        scene ep10_tg_failed_hide1 with dissolve
        jump ep10_tg_failed_hide_label
    "[mod_gr]Try to hide in the corner":
        $ renpy.block_rollback()
        scene ep10_tg_hide_droom2 with dissolve
        mc "(Please, don't come in here... Please?)"
        scene ep10_tg_hide_droom3 with dissolve
        $ renpy.pause()
        scene ep10_tg_hide_droom2 with dissolve
        $ renpy.pause()
        scene ep10_tg_hide_droom4 with dissolve
        mc "(Did he leave?)"
        scene ep10_tg_hide_droom2 with dissolve
        menu:
            "Go outside":
                $ renpy.block_rollback()
                scene ep10_tg_failed_hide1 with dissolve
                jump ep10_tg_failed_hide_label
            "[mod_gr]Stay":
                $ renpy.block_rollback()
                mc "(Not yet. Gotta wait for Derek's signal.)"
                scene ep10_tg_hide_droom4 with dissolve
                mc "(Fuck, I should have gone with the bathroom.)"
                mc "(Don't panic...)"
                play sound "sound_effects/season2/vibrate.mp3"
                scene ep10_tg_hide_droom5 with hpunch
                "*{i}Vibrations{/i}*"
                mc "(Ok. Time to move. Man, I can't believe a dildo is keeping me safe.)"
jump ep10_tg_after_hide_label

label ep10_tg_dinner_label:
if ep8_told_josy_chad:
    scene ep10_tg_dinner1b with dissolve
else:
    scene ep10_tg_dinner1 with dissolve
pa "[name], sit down. It's time to eat."

if ep8_told_josy_chad:
    scene ep10_tg_dinner2 with dissolve
    sa "I had no luck finding the key."
    scene ep10_tg_dinner3 with dissolve
    mc "Me neither."
    scene ep10_tg_dinner4 with dissolve
    de "The office key?"
    scene ep10_tg_dinner5 with dissolve
    mc "Yeah, the office door is locked."
else:
    scene ep10_tg_dinner5 with dissolve
    mc "Derek..."
    scene ep10_tg_dinner4 with dissolve
    de "What's up?"
    scene ep10_tg_dinner5 with dissolve
    mc "The office door is locked. Where the hell is the key?"
scene ep10_tg_dinner6 with dissolve
de "He has a keychain with keys to the house."
de "It should have a tag that says \"house keys\" on it. It's one of those."
scene ep10_tg_dinner5 with dissolve
mc "Ok. And where is it?"
scene ep10_tg_dinner6 with dissolve
de "Most likely in the garage. There's a combination lock on a locker on the wall. The code is 0505 - our birthday."
scene ep10_tg_dinner5 with dissolve
mc "Got it."
scene ep10_tg_dinner7 with dissolve
hl "Dinner smells delicious!"
hl "Your father has outdone himself again."
scene ep10_tg_dinner8 with dissolve
my "Yeah, he sure has."
scene ep10_tg_dinner9 with dissolve
pa "*{i}Smack{/i}* Everything for you, love."
scene ep10_tg_dinner10 with dissolve
hl "Who won?"
scene ep10_tg_dinner11 with dissolve
pa "I haven't watched the game yet. I put it on pause to prepare the feast."
scene ep10_tg_dinner10 with dissolve
hl "But you love watching the game on Thanksgiving."
scene ep10_tg_dinner11 with dissolve
pa "I'll watch it later tonight."
pa "If anyone knows who won, spare me the spoilers. Haha!"
if ep8_told_josy_chad:
    scene ep10_tg_dinner12 with dissolve
    hl "Oh! Another fresh face. Who is this?"
    scene ep10_tg_dinner33 with dissolve
    de "Mom, this is my - ugh - close friend, Sage."
    scene ep10_tg_dinner36 with dissolve
    sa "Hi! Helen, is it? You have a lovely home."
    scene ep10_tg_dinner12 with dissolve
    hl "Sage, what a pretty name. Almost as pretty as you."
    scene ep10_tg_dinner35 with dissolve
    sa "Oh. Thanks..."
    scene ep10_tg_dinner22 with dissolve

pa "Love? Do you want to say the prayers?"
scene ep10_tg_dinner13 with dissolve
hl "I don't do that anymore. You know that."
scene ep10_tg_dinner22 with dissolve
pa "Still, I wanted to check. Do you mind if I say them?"
scene ep10_tg_dinner21 with dissolve
$ renpy.pause()
scene ep10_tg_dinner24 with dissolve
pa "Our Heavenly Father."
pa "We are thankful for our food and drink."
pa "And we're especially thankful for this on this day, which we may share in the company of family and friends."
pa "Thank you."
scene ep10_tg_dinner25 with dissolve
pa "Please, everyone. Dig in."
scene ep10_tg_dinner49 with dissolve
hl "The food looks delicious!"
hl "Your father has spent most of today ensuring we have this great meal."
scene ep10_tg_dinner16 with dissolve
hl "I remember when we were young, and he struggled so hard in the kitchen. Haha!"
hl "He once made fish sticks using the bread toaster. Do you remember that, Maya?"
scene ep10_tg_dinner37 with dissolve
my "Yes, I do. They came out all burnt."
scene ep10_tg_dinner16 with dissolve
hl "Haha! All burnt! We had to open the windows because it smelled so bad."
hl "It also set off the fire alarms, and the neighbors came running."
scene ep10_tg_dinner22 with dissolve
pa "You've always been the cook in the family. Everything I've learned comes from you."
scene ep10_tg_dinner14 with dissolve
hl "You're doing great, love."
hl "Your father is so good these days. He cooks, cleans, and works."
hl "I do the laundry, of course. That's my job, haha."
scene ep10_tg_dinner22 with dissolve
pa "And I don't dare touch it."
scene ep10_tg_dinner14 with dissolve
hl "Haha! No, you better not."
$ guideSuggestedPage = 141
scene ep10_tg_dinner41 with dissolve
my "*{i}Whispers{/i}* I'm sorry about Mom. She gets amped up after she takes morphine."
my "*{i}Whispers{/i}* It's hard to get a word in."
scene ep10_tg_dinner42 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(+Maya)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Reassure Maya [m_c1][mod_choices[0]]":
        $ RPmaya += 2
        mc "*{i}Whispers{/i}* She's sweet, though. I can see where you get it from."
        if branchMayaJosy:
            scene ep10_tg_dinner44 with dissolve
            $ renpy.pause()
            if ep8_told_josy_chad:
                scene ep10_tg_dinner45 with dissolve
                $ renpy.pause()
            else:
                scene ep10_tg_dinner46 with dissolve
                $ renpy.pause()
        else:
            scene ep10_tg_dinner43 with dissolve
            $ renpy.pause()
    "I understand":
        mc "*{i}Whispers{/i}* I understand. It must be tough to try and stay herself with her illness."
        scene ep10_tg_dinner43 with dissolve
        $ renpy.pause()

scene ep10_tg_dinner47 with dissolve
pa "Honey? Don't forget to eat."
scene ep10_tg_dinner48 with dissolve
hl "Oh, right! Eat. I need to eat when I've taken my medication, or I get sick."
hl "It's the weirdest thing."
scene ep10_tg_dinner26 with dissolve
pa "I have an idea. How about we go around the table and say what we are thankful for?"
pa "That's a nice tradition, right? I can start."
scene ep10_tg_dinner27 with dissolve
pa "I am thankful for my family. How we stick together through thick and thin."
pa "And how we always care about each other."
scene ep10_tg_dinner22 with dissolve
pa "I am thankful for you, Helen. Every day is a struggle for you, but you always manage, and it amazes me."
pa "You are the strongest person I'm blessed to know, and I don't know how you do it."
pa "I love you."
scene ep10_tg_dinner14 with dissolve
hl "Oh, dear. That was so beautiful."

scene ep10_tg_dinner50 with dissolve
mc "(That was so unexpected... It felt genuine.)"
mc "(If he means those words, why is he treating Maya like shit?)"
scene ep10_tg_dinner22 with dissolve
pa "What are you thankful for, love?"
scene ep10_tg_dinner14 with dissolve
hl "I, too, am thankful for my beautiful family."
hl "Having you home is the highlight of my day, week, or month. It's what I live for."
scene ep10_tg_dinner16 with dissolve
hl "What are you thankful for, pumpkin?"
scene ep10_tg_dinner38b with dissolve
my "Uh... I don't know."
scene ep10_tg_dinner28 with dissolve
pa "Surely you're thankful for something."
scene ep10_tg_dinner39 with dissolve
my "I'm thankful for my friends."
scene ep10_tg_dinner28c with dissolve
$ renpy.pause()
scene ep10_tg_dinner40 with dissolve
my "And my family, of course."
scene ep10_tg_dinner34 with dissolve
de "Me too. And I'm thankful for this dinner."
if ep8_told_josy_chad:
    scene ep10_tg_dinner12 with dissolve
    hl "What about you two?"
    hl "You make a lovely couple, I might add."
    if branchMayaJosy:
        scene ep10_tg_dinner38 with dissolve
    else:
        scene ep10_tg_dinner38b with dissolve
    my "Actually... [name] is my boyfriend, Mom."
    scene ep10_tg_dinner17 with dissolve
    hl "Your boyfriend!? Is it true?"
    scene ep10_tg_dinner51 with dissolve
    mc "Yeah, it is."
    scene ep10_tg_dinner15 with dissolve
    hl "Patrick, did you hear what your daughter just shared with us? Isn't it wonderful!?"
    scene ep10_tg_dinner23 with dissolve
    pa "It is certainly something out of the ordinary."
    if not branchMayaJosy:
        scene ep10_tg_dinner15b with dissolve
        my "(Lying to Mom like this doesn't feel good...)"
    scene ep10_tg_dinner15 with dissolve
    hl "Such a wonderful surprise! Now, I have something else to be thankful for."
    scene ep10_tg_dinner18 with dissolve
    hl "But oh! How embarrassing. I must apologize to you for my comment!"
    scene ep10_tg_dinner57 with dissolve
    sa "It's fine, haha. Uh..."
    sa "*{i}Sigh{/i}* I'm not sure about what I'm thankful for today."
    scene ep10_tg_dinner29 with dissolve
    pa "It can be anything that comes to mind. Your family, or maybe something happened this last year that you are thankful for?"
    scene ep10_tg_dinner58 with dissolve
    sa "..."
    scene ep10_tg_dinner59 with dissolve
    sa "Ok... I'm thankful for finding new, true friends and being able to open up to them."
    if branchSage:
        scene ep10_tg_dinner60 with dissolve
        sa "And I'm thankful for someone special, too."
        scene ep10_tg_dinner61 with dissolve
        $ renpy.pause()
    else:
        scene ep10_tg_dinner60 with dissolve
        sa "It's meant a lot."
    scene ep10_tg_dinner12 with dissolve
    hl "Aw, how nice!"
    scene ep10_tg_dinner52 with dissolve
    mc "I guess it's my turn..."
else:
    scene ep10_tg_dinner19 with dissolve
    hl "What about you?"
    scene ep10_tg_dinner52 with dissolve
    mc "Me? Um..."

mc "I'm thankful for the ones closest to me."
mc "And I'm thankful for my dad..."
scene ep10_tg_dinner53 with dissolve
mc "He's guided and supported me throughout my life."
mc "I wouldn't be who I am today without him."
menu:
    "He lets me be me":
        $ ep10_patrick_penalty += 1
        scene ep10_tg_dinner56 with dissolve
        mc "And most importantly, he lets me be me. He lets me make my own mistakes, and he accepts my flaws."
        mc "He doesn't impose his standards or wishes on me."
        scene ep10_tg_dinner54 with dissolve
        mc "That's what a parent should be like."
        scene ep10_tg_dinner30 with dissolve
        $ renpy.pause()
        scene ep10_tg_dinner19 with dissolve
        hl "Your father must be proud. He sounds like a beautiful person."
        scene ep10_tg_dinner55 with dissolve
        mc "Thank you. He is."
        scene ep10_tg_dinner31 with dissolve
        pa "Isn't your father lonely, spending Thanksgiving without you?"
        scene ep10_tg_dinner13 with dissolve
        hl "Patrick!"
        scene ep10_tg_dinner23 with dissolve
        pa "It was merely a question."
        $ guideSuggestedPage = 142
        scene ep10_tg_dinner54 with dissolve
        if ep8_told_josy_chad:
            mc "I will celebrate it this weekend with him instead. He understood when I said I wanted to spend it with my girlfriend and meet her family."
        else:
            mc "I will celebrate it this weekend with him instead. He understood when I said I wanted to spend it with my friends and meet their family."
        menu:
            "Rub it in":
                $ ep10_patrick_penalty += 1
                $ dk(1)
                scene ep10_tg_dinner32 with dissolve
                mc "Like I said, he's very supportive of my choices."
            "End it there":
                mc "And, once again, thanks for having me."
    "[mod_gr]End it there":
        scene ep10_tg_dinner19 with dissolve
        hl "Your father sounds like a beautiful person."
        scene ep10_tg_dinner20 with dissolve
        mc "Oh, he is."

if ep8_told_josy_chad:
    scene ep10_tg_dinner62 with wipeleft
else:
    scene ep10_tg_dinner62b with wipeleft
$ renpy.pause()
scene ep10_tg_dinner34 with dissolve
de "I am full... What a great dinner."
scene ep10_tg_dinner63 with dissolve
pa "I'm glad you enjoyed it. Please take some leftovers with you when you leave."
scene ep10_tg_dinner64 with dissolve
mc "Thanks for the dinner. I need to use the restroom."
if ep8_told_josy_chad:
    scene ep10_tg_dinner65b with dissolve
else:
    scene ep10_tg_dinner65 with dissolve
play sound "sound_effects/season2/vibrate.mp3"
"*{i}Vibrations{/i}*"
mc "(Garage, here I come.)"

$ event_list.append("tg_part2")
$ event_list.append("ep10_tg_hall_derek_label")
$ event_list.append("ep10_tg_keys_label")
$ event_list.append("no_keys")

jump endEvent

label ep10_tg_after_hide2_label:
scene ep10_tg_dinner66 with dissolve
my "*{i}Whispers{/i}* Did he catch you?"
scene ep10_tg_dinner67 with dissolve
mc "*{i}Whispers{/i}* Yeah, but it's fine. I got the keys."
mc "*{i}Whispers{/i}* The next time I get an opportunity, I'll go for it."
mc "*{i}Whispers{/i}* But the bad news is that I no longer have the bathroom to use as a cover."
scene ep10_tg_dinner66 with dissolve
my "*{i}Whispers{/i}* Damn... That's bad. I'm getting nervous, [name]... Maybe we should call it off."
scene ep10_tg_dinner67 with dissolve
mc "*{i}Whispers{/i}* We can't call it off now, Maya. We're this close."
scene ep10_tg_dinner69 with dissolve
$ renpy.pause()
scene ep10_tg_dinner67 with dissolve
mc "*{i}Whispers{/i}* Hey, what's up with your mom?"
scene ep10_tg_dinner66 with dissolve
my "*{i}Whispers{/i}* [name], I'm sorry in advance. The effect of her meds is starting to subside. And it will be a few more hours until she can have more."
my "*{i}Whispers{/i}* She might get angry... But it's not her; it's her illness."
scene ep10_tg_dinner67 with dissolve
mc "*{i}Whispers{/i}* Maya... I'm so sorry."
scene ep10_tg_dinner68 with dissolve
my "*{i}Whispers{/i}* Don't be. I've lived like this my entire life. You get used to it."
my "*{i}Whispers{/i}* I feel helpless when it comes to Mom. There's nothing I can say or do to make it better for her."
my "*{i}Whispers{/i}* To you, it might seem as if I'm acting cold, brushing it off easily... *{i}Sigh{/i}*"
scene ep10_tg_dinner66 with dissolve
my "*{i}Whispers{/i}* But the truth is that I have to do it. Because it's the only way I can live a somewhat happy life."
scene ep10_tg_dinner67 with dissolve
menu:
    "Hug her [m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep10_tg_dinner70 with dissolve
        mc "*{i}Whispers{/i}* You're so fucking strong... Wow..."
    "Sympathize":
        mc "*{i}Whispers{/i}* I think I understand."

if ep8_told_josy_chad:
    scene ep10_tg_dinner71 with dissolve
else:
    scene ep10_tg_dinner71b with dissolve
pa "I hope you still have some room left for dessert."
scene ep10_tg_dinner72 with dissolve
pa "Honey?"
scene ep10_tg_dinner73 with dissolve
hl "No. I don't want any dessert. I'm feeling queasy. You should know that."
scene ep10_tg_dinner75 with dissolve
pa "That's fine. Have some water."
scene ep10_tg_dinner73 with dissolve
hl "No, I don't want water. Let me breathe for a moment, will you?"
if ep8_told_josy_chad:
    scene ep10_tg_dinner86 with dissolve
    sa "Helen? Are you ok?"
    scene ep10_tg_dinner74 with dissolve
    hl "I'll be fine, dear. It's my illness. It has its ups and downs."
else:
    scene ep10_tg_dinner74 with dissolve
hl "Please, everyone. Have cake."
scene ep10_tg_dinner76 with dissolve
pa "Yes, let's have some cake. And maybe after that, it's time to call it a night."
scene ep10_tg_dinner78 with dissolve
if ep8_told_josy_chad:
    de "About that, Dad... Can I borrow your car after dinner? I'd like to drive my friends back home."
else:
    de "About that, Dad... Can I borrow your car after dinner? I'd like to drive my friend back home."
scene ep10_tg_dinner77 with dissolve
pa "Yes, that's fine. I don't need it until Monday. You know where the car keys are."
scene ep10_tg_dinner78 with dissolve
stop music fadeout 3
de "Thanks. Hey, that's another thing to be thankful for."
scene ep10_tg_dinner79 with dissolve
play music "music/ep10/licensed_music/track149.mp3"
hl "It's good that everyone has things to be thankful for."
hl "I'd be thankful for a day without meds."
scene ep10_tg_dinner82 with dissolve
pa "Helen."
scene ep10_tg_dinner80 with dissolve
hl "I haven't left the house in three months! I have no life! I have nothing!"
hl "Being locked inside these four walls. In half a home I cannot use because I can't walk up the stairs."
hl "It's my prison, Patrick! Don't you get that?"
scene ep10_tg_dinner82 with dissolve
pa "Helen..."
scene ep10_tg_dinner81 with dissolve
hl "And my body is my prison!"
hl "And I'm sweating again. *{i}Exhales{/i}*"
scene ep10_tg_dinner82 with dissolve
pa "Maybe you should get some rest?"
scene ep10_tg_dinner81 with dissolve
hl "Yes. More rest. Every day. It's all I do."
hl "I sleep, I eat, I rest. *{i}Exhales{/i}*"
scene ep10_tg_dinner83 with dissolve
pa "Come, I'll help you get to bed. Do you want the wheelchair?"
scene ep10_tg_dinner84 with dissolve
hl "I will walk! Let me end the night with a single bit of dignity."
scene ep10_tg_dinner85 with dissolve
$ renpy.pause()
if ep8_told_josy_chad:
    scene ep10_tg_dinner87 with dissolve
    $ renpy.pause()
    scene ep10_tg_dinner89 with dissolve
    mc "Are you ok?"
    scene ep10_tg_dinner88 with dissolve
    sa "Maya, Derek... I'm so sorry."
    scene ep10_tg_dinner90 with dissolve
    my "It's fine."
else:
    scene ep10_tg_dinner89 with dissolve
    mc "Maya, are you ok?"
    scene ep10_tg_dinner90 with dissolve
    my "It's fine. I told you..."

scene ep10_tg_dinner91 with dissolve
my "This is why I don't talk to Mom about my problems."
my "I don't want to burden her more. And besides, she can't help me..."
scene ep10_tg_dinner92 with dissolve
my "All she could do is get mad at Dad. And that wouldn't help either of them."
my "Mom needs Dad to survive. And Dad needs Mom, or he'd collapse."
scene ep10_tg_dinner91 with dissolve
my "I told you this wasn't easy..."
scene ep10_tg_dinner90 with dissolve
my "I'm gonna check on Mom. She verbally attacks Dad but usually holds it together when it's me or Derek."
scene ep10_tg_dinner89 with dissolve
mc "What about the contract? Should I go for it?"
scene ep10_tg_dinner93 with dissolve
de "Mom usually forces him to leave her alone."
de "He'll be back soon."
if ep8_told_josy_chad:
    play sound "sound_effects/season3/keys.mp3"
    scene ep10_tg_dinner96 with dissolve
    sa "Give me the keys. I'm doing it."
    scene ep10_tg_dinner95 with dissolve
    de "Sage, no!"
    stop music fadeout 3
    scene ep10_tg_dinner94 with dissolve
    mc "We gotta do it now."
else:
    scene ep10_tg_dinner94 with dissolve
    stop music fadeout 3
    mc "But you heard what he said before. We need to leave after dinner."
    mc "We gotta do it now."
"*{i}Indistinct yelling{/i}*"
play music "music/ep10/licensed_music/track150.mp3"
if ep8_told_josy_chad:
    scene ep10_tg_dinner97 with dissolve
else:
    scene ep10_tg_dinner97b with dissolve
mc "That's Maya..."
de "Fuck... Not like this."

scene ep10_tg_dinner98 with hpunch
my "You're making it worse when you tell her to calm down. Don't you get that?"
scene ep10_tg_dinner99 with hpunch
pa "Do you think I want to argue in front of everyone? Do you think I enjoy this?"
scene ep10_tg_dinner98 with hpunch
my "Dad, let go! You're hurting me!"
scene ep10_tg_dinner100 with dissolve
mc "Hey, what's going on?"
scene ep10_tg_dinner101 with dissolve
my "[name]..."
my "It's fine, [name]..."
my "[name]... Do you see?"
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
scene ep10_tg_dinner102 with dissolve
mc "(Do I see?)"
scene ep10_tg_dinner103 with dissolve
mc "(Do I see...?)"
if ep2_choseMayaOverParty:
    play sound "sound_effects/whoosh_2.mp3"
    scene ep10_mayamovienight35
    my "This was taken the day of my graduation."
    my "I graduated Magna Cum Laude."
    scene ep10_mayamovienight35b with dissolve
    my "Do you see?"
hide screen freeroam_help
play sound "sound_effects/whoosh_2.mp3"
scene ep10_maya_wede
mc "Say, who was that man leaving our dorm?"
scene ep10_maya_wedd with dissolve
my "That was my dad, you see?"

play sound "sound_effects/whoosh_2.mp3"
scene ep7_mj_dorm47
mc "He has a {b}key{/b}...to {b}your{/b} dorm?"
scene ep7_mj_dorm46 with dissolve
my "I know."
scene ep7_mj_dorm47 with dissolve
mc "What the hell, Maya..."
scene ep7_mj_dorm46 with dissolve
my "Do you see it now?"
$ guideSuggestedPage = 148
scene ep10_tg_dinner105 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
                    if ep10_patrick_penalty > 3:
                        $mod_choices[6]="Don't find contracts"
                    if ep10_patrick_penalty > 5:
                        $mod_choices[7]="Don't find contracts"

$ mc_info = ["Punch him\n[m_c2][mod_choices[6]]","ep10_tg_punch_label","Confront him\n[m_c2][mod_choices[7]]","ep10_tg_confront_label","Rescue Maya","ep10_tg_rescue_label",(ep2FoughtJocks or ep5_agitatedCaleb or ep6_foughtTommy)]
show screen major_choice_screen
$ renpy.pause()

label ep10_tg_punch_label:
$ ep10_patrick_choice = "DIK"
$ renpy.music.stop(channel="sfx1", fadeout=1)
$ ep10_patrick_penalty += 5
scene ep10_tg_dinner111 with dissolve
$ renpy.pause()
play sound "sound_effects/hit.mp3"
scene ep10_tg_dinner112 with hpunch
my "[name]! No!"
scene ep10_tg_dinner113 with dissolve
my "Dad!? Dad!?"
scene ep10_tg_dinner113b with dissolve
pa "*{i}Groans{/i}*"
scene ep10_tg_dinner114 with dissolve
pa "You! You are not welcome in this house. You're leaving now!"
$ new_bio("You", "I punched Patrick when I saw him abusing Maya.")
$ new_bio("Patrick", "I punched Patrick when I saw him abusing Maya.")
jump ep10_tg_confrontb_label

label ep10_tg_confront_label:
$ ep10_patrick_choice = "NEUTRAL"
$ renpy.music.stop(channel="sfx1", fadeout=1)
$ ep10_patrick_penalty += 3
scene ep10_tg_dinner115 with dissolve
mc "You don't put your fucking hands on her! What the hell are you doing?"
$ new_bio("You", "I confronted Patrick when I saw him abusing Maya.")
$ new_bio("Patrick", "I confronted Patrick when I saw him abusing Maya.")

label ep10_tg_confrontb_label:
scene ep10_tg_dinner105 with dissolve
mc "You're abusing your child. What the fuck is wrong with you?"
scene ep10_tg_dinner106 with dissolve
pa "I'm not abusing my daughter. This is a family matter, and it doesn't concern you!"
scene ep10_tg_dinner105 with dissolve
mc "I'm not stupid. I know what I saw. You gripped her arm hard, and she told you that you were hurting her."
if affinity == "DIK":
    mc "That's abuse, you fucking moron!"
else:
    mc "That's abuse!"
scene ep10_tg_dinner106 with dissolve
pa "You don't get to judge me!"
if ep10_patrick_choice == "DIK":
    pa "I told you already. It's time to leave!"
else:
    pa "You are not welcome in this house. You're leaving now!"
scene ep10_tg_dinner110 with dissolve
mc "I'm not leaving without Maya."
mc "Come, Maya. Let's leave this abusive asshole."
jump ep10_tg_car_label

label ep10_tg_rescue_label:
$ ep10_patrick_choice = "CHICK"
$ renpy.music.stop(channel="sfx1", fadeout=1)
scene ep10_tg_dinner102 with dissolve
mc "I see it, Maya... I'm sorry I didn't see it before...but I see it now."
scene ep10_tg_dinner103b with dissolve
my "..."
scene ep10_tg_dinner105 with dissolve
mc "Patrick, let's calm down. We don't have to resort to violence."
scene ep10_tg_dinner107 with dissolve
pa "*{i}Sigh{/i}* She agitated me."
pa "Maya, I'm sorry."
scene ep10_tg_dinner104 with dissolve
my "It's ok, Dad..."
scene ep10_tg_dinner109 with dissolve
mc "We're going to leave."
mc "Take care of your wife. She needs you."
scene ep10_tg_dinner108 with dissolve
pa "..."
$ new_bio("You", "I defused the situation with Patrick when I saw him abusing Maya.")
$ new_bio("Patrick", "I defused the situation with Patrick when I saw him abusing Maya.")

label ep10_tg_car_label:

if ep8_told_josy_chad:
    scene ep10_tg_car1 with dissolve
    sa "What's happening?"
    scene ep10_tg_car2 with dissolve
    mc "We're leaving."
    mc "Patrick's hitting Maya."
else:
    scene ep10_tg_car3 with dissolve
    de "[name]?"
    mc "We're leaving. Your dad is hitting your sister."
scene ep10_tg_car6 with dissolve
my "[name], he doesn't...hit me."
scene ep10_tg_car4 with dissolve
de "Fuck... Fuck..."
scene ep10_tg_car5 with dissolve
mc "You knew about this?"

if ep10_patrick_choice == "CHICK":
    scene ep10_tg_car6 with dissolve
    my "We gotta go..."
    if ep8_told_josy_chad:
        scene ep10_tg_car7 with dissolve
        sa "[name], there's no way I could find the contract. There are too many binders in there."
else:
    if ep8_told_josy_chad:
        scene ep10_tg_car7 with dissolve
        sa "[name], there's no way I could find the contract. There are too many binders in there."

scene ep10_tg_car8 with dissolve
if ep10_patrick_choice == "CHICK":
    if ep8_told_josy_chad:
        pa "Thanksgiving is over. Derek, leave with your friends."
    else:
        pa "Thanksgiving is over. Derek, leave with your friend."
else:
    if ep8_told_josy_chad:
        pa "Thanksgiving is over. Derek, remove your friends from our home."
    else:
        pa "Thanksgiving is over. Derek, remove your friend from our home. He's not welcome here."

if ep7_patrick_score < -3:
    $ ep10_patrick_penalty += 3
elif ep7_patrick_score < 0:
    $ ep10_patrick_penalty += 2
elif ep7_patrick_score < 4:
    $ ep10_patrick_penalty += 1
else:
    $ ep10_patrick_penalty += 0

if not ep8_told_josy_chad:
    $ ep10_patrick_penalty += 1


if ep10_patrick_penalty > 6:
    $ ep10_got_contracts = False
else:
    $ ep10_got_contracts = True

if not ep10_got_contracts:
    scene ep10_tg_sus1 with dissolve
    $ renpy.pause()
    scene ep10_tg_sus2 with dissolve
    $ renpy.pause()
    scene ep10_tg_sus3 with dissolve
    $ renpy.pause()
    scene ep10_tg_sus4 with dissolve
    $ renpy.pause()

    if ep8_told_josy_chad:
        scene ep10_tg_sus5 with dissolve
    else:
        scene ep10_tg_sus5b with dissolve
    pa "Where are the house keys? They're missing."
    if ep8_told_josy_chad:
        scene ep10_tg_sus6b with dissolve
        de "Oh, the house keys? Um... Anyone?"
    else:
        scene ep10_tg_sus6 with dissolve
        de "Oh, the house keys? Um... [name]?"

    if ep8_told_josy_chad:
        scene ep10_tg_sus7 with dissolve
        sa "Here."
    else:
        scene ep10_tg_sus7b with dissolve
        mc "..."
    scene ep10_tg_sus8 with dissolve
    pa "I don't know what the hell you are up to; you guys whisper and act weird."
    pa "But you don't borrow keys without asking first!"
    scene ep10_tg_sus9 with dissolve
    if ep8_told_josy_chad:
        de "It's my fault, Dad. I gave them to her."
    else:
        de "It's my fault, Dad. I gave them to him."
    de "We used them to open the garage."
    scene ep10_tg_sus10 with dissolve
    my "Dad..."

if ep8_told_josy_chad:
    scene ep10_tg_car9 with dissolve
else:
    scene ep10_tg_car9b with dissolve
my "It doesn't have to be this way. Mom wouldn't want this."
scene ep10_tg_car10 with dissolve
pa "Your mother needs peace and quiet. Can you at least give her that?"
scene ep10_tg_car11 with dissolve
my "Please, calm down. For Mom's sake."
stop music fadeout 3
pa "*{i}Sigh{/i}*"
scene ep10_tg_car12 with dissolve
$ renpy.pause()

play music "music/ep10/licensed_music/track149.mp3"
if ep8_told_josy_chad:
    scene ep10_tg_car18 with dissolve
else:
    scene ep10_tg_car18b with dissolve
$ renpy.pause()

if ep8_told_josy_chad:
    scene ep10_tg_car19b with dissolve
else:
    scene ep10_tg_car19 with dissolve
$ renpy.pause()

if ep10_got_contracts:
    if branchJill:
        scene ep10_jill_solo33b2 with dissolve
        ji "I don't want you to end up doing something you will regret. That's all."
    if branchIsabella:
        scene ep10_pre_tgb7b with dissolve
        isa "Promise me you'll be safe today. And don't do something stupid or...something you'd probably do."
    if (ep10_jm_solo == "Maya" or ep10_jm_solo=="Maya Josy"):
        scene ep10_maya_solo25b with dissolve
        my "Whatever happens... I trust you."
    else:
        scene ep10_josy_solo70b with dissolve
        js "Do whatever it takes...for her. Ok?"
else:
    if ep8_told_josy_chad:
        scene ep10_tg_sus11 with dissolve
    else:
        scene ep10_tg_sus11b with dissolve
    mc "I blew it..."
    scene ep10_tg_car22 with dissolve
    my "You didn't blow it, [name]. You tried your best."
    if ep8_told_josy_chad:
        scene ep10_tg_sus11 with dissolve
    else:
        scene ep10_tg_sus11b with dissolve
    mc "We were right there... If I'd just had some more time, I could have..."
    scene ep10_tg_car22 with dissolve
    my "It's ok, [name]."
    my "It's ok."
    scene ep10_tg_car23 with dissolve
    mc "Maya... Nothing about tonight was ok. It was horrible."
    scene ep10_tg_car24 with dissolve
    mc "Seeing how ill your mom is... Seeing how Patrick treats you."
    stop music fadeout 10
    if ep8_told_josy_chad:
        scene ep10_tg_sus11 with dissolve
    else:
        scene ep10_tg_sus11b with dissolve
    mc "I mean... What now? Can we find a way to try again? We have to, right?"
    $ phone_clear_jump_label = "ep10_fr_tg_end_bella_label"
    jump end_freeroam

if ep8_told_josy_chad:
    scene ep10_tg_car20 with dissolve
else:
    scene ep10_tg_car20b with dissolve
mc "Wait... Stop the car."
if ep8_told_josy_chad:
    scene ep10_tg_car21 with dissolve
    mc "Sage? The keys."
    play sound "sound_effects/season3/keys.mp3"
scene ep10_tg_car22 with dissolve
my "What are you doing?"
scene ep10_tg_car23 with dissolve
mc "I'm not leaving until we get what we came here for."
scene ep10_tg_car22 with dissolve
my "He will stop you dead in your tracks."
scene ep10_tg_car23 with dissolve
mc "No, he won't notice I'm still in there."
mc "Wait for me around the block."
play sound "sound_effects/season3/car_door.mp3"
scene ep10_tg_car22 with dissolve
my "This plan is a disaster..."

scene ep10_tg_car13 with dissolve
de "[mc_de_up]... You're not doing this alone. I'll help you."
scene ep10_tg_car14 with dissolve
de "If he spots you... Promise me you'll just get out. Ok?"
scene ep10_tg_car15 with dissolve
mc "Yeah."
scene ep10_tg_car16 with dissolve
de "Dad's in the living room. I'm gonna call him and get his attention. Do you still have the vibrator in your pocket?"
mc "Keep a lookout."
scene ep10_tg_car14 with dissolve
de "Wait..."
scene ep10_tg_car15 with dissolve
mc "What?"
scene ep10_tg_car14 with dissolve
de "Unless he changed it, the binder should be white."
scene ep10_tg_car15 with dissolve
mc "Got it."
scene ep10_tg_car17 with dissolve
$ renpy.pause()

label ep10_tg_contract_label:
scene ep10_tg_contract1 with dissolve
$ renpy.pause()
scene ep10_tg_contract2 with dissolve
$ renpy.pause()
scene ep10_tg_contract3 with dissolve
pa "This is not what I wanted for today, either."
pa "Your mother has worsened these last few months and didn't want us to cancel the plans when you were coming back home."
scene ep10_tg_contract4 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/floor_creak.mp3"
scene ep10_tg_contract5 with dissolve
$ renpy.pause()
scene ep10_tg_contract6 with dissolve
$ renpy.pause()
play sound "sound_effects/key_jiggle.mp3"
scene ep10_fr_tg_end7 with dissolve
$ renpy.pause()

scene ep10_tg_contract8 with dissolve
if ep8_told_josy_chad:
    mc "(Sage couldn't find it... I hope that I can.)"
else:
    mc "(I hope I can find it...)"

$ currentEvent = "ep10_fr_tg_office_label"
jump startEvent

label ep10_fr_tg_end_label:
scene ep10_fr_tg_end1 with dissolve
mc "(Loans...)"
mc "(Mortgage seems paid in full.)"
scene ep10_fr_tg_end2 with dissolve
mc "(A loan for a caravan. Payments for it... Paid in full.)"
scene ep10_fr_tg_end3 with dissolve
mc "(Finnman Banking? Some kind of loan... Uh... Nah, this doesn't look like it.)"
scene ep10_fr_tg_end5 with dissolve
mc "(Medical bills for Helen... Insurance... Ugh... I feel like such a scummy asshole going through these.)"
mc "(It's for Maya... Come on... Push those feelings away.)"
scene ep10_fr_tg_end4 with dissolve
mc "(Oh! This one has Maya's signature on it! And Patrick's, too! This is it!)"
mc "(\"The funds lent by Finnman Banking...\" Finnman Banking? Wait, I saw that one in here.)"
scene ep10_fr_tg_end6 with dissolve
mc "(I'll grab these too.)"
play sound "sound_effects/key_jiggle.mp3"
scene ep10_fr_tg_end7 with dissolve
mc "(I can't forget to lock the door and to put the keys back in the box.)"
mc "(The longer the time we have reading these papers without him knowing about it, the better.)"
scene ep10_fr_tg_end8 with dissolve
pa "*{i}Sobs{/i}*"
scene ep10_fr_tg_end9 with dissolve
mc "(Is he...crying?)"
scene ep10_fr_tg_end10 with dissolve
mc "..."

scene ep10_fr_tg_end11 with dissolve
$ renpy.pause()
scene ep10_fr_tg_end12 with dissolve
mc "Derek? Are you out there?"
scene ep10_fr_tg_end13 with dissolve
de "[mc_de_up]?"
scene ep10_fr_tg_end14 with dissolve
mc "I got it! Open the door."
scene ep10_fr_tg_end13 with dissolve
de "Hold on."

if ep8_told_josy_chad:
    scene ep10_fr_tg_end15 with dissolve
    my "This couldn't have gone any worse."
    scene ep10_fr_tg_end16 with dissolve
    sa "We were so close to getting it earlier. With just some more time to search, I'm sure [name] will find it."
    scene ep10_fr_tg_end15 with dissolve
    my "I don't know what we were thinking when we came up with this."
    scene ep10_fr_tg_end16 with dissolve
    sa "It will be fine, Maya."
    scene ep10_fr_tg_end15 with dissolve
    my "I'm afraid I caused problems for Mom. If she gets mad at Dad..."
    my "Sometimes, she says these horrible things to him in front of us."
    scene ep10_fr_tg_end17 with dissolve
    my "Like, how she doesn't love him anymore. And how he wasn't her first love."
    my "I think it's her illness talking, but I can't help but wonder if she'd ever leave him."
    scene ep10_fr_tg_end18 with dissolve
    sa "..."
    scene ep10_fr_tg_end19 with dissolve
    sa "It's not the end of the world if they split up. Many parents...divorce."
    scene ep10_fr_tg_end17 with dissolve
    my "For them, it's everything. Mom depends on him."
    scene ep10_fr_tg_end20 with dissolve
    sa "Don't jump ahead, Maya. Your dad might cool down tomorrow, and you can talk to him."
    sa "And if the boys are lucky...everything we did tonight will be worth it."

stop music fadeout 3
play sound "sound_effects/season3/car_door.mp3"
if ep8_told_josy_chad:
    scene ep10_fr_tg_end21 with dissolve
else:
    scene ep10_fr_tg_end21b with dissolve
mc "I did it! Maya, I did it!"
if ep8_told_josy_chad:
    sa "No way!"
scene ep10_fr_tg_end22 with dissolve
my "You got the contract?"
scene ep10_fr_tg_end23 with dissolve
mc "The papers are right here! Here you go!"
scene ep10_fr_tg_end24 with dissolve
my "Are you for real?"
play sound "sound_effects/burnout.mp3"
scene ep10_fr_tg_end25 with dissolve
de "Let's go! Haha!"

scene ep10_fr_tg_end26 with dissolve
my "I can't believe you got them... They're here. They're really here!"

scene ep10_fr_tg_end27 with dissolve
de "We fucking did it!"
scene ep10_fr_tg_end29 with dissolve
if ep8_told_josy_chad:
    mc "So, what now? Should we read them?"
    scene ep10_fr_tg_end30 with dissolve
    sa "I don't want to be responsible for interpreting the contracts on my own. Let's wait until we're at Bella's."
else:
    mc "I can't wait until we get to Bella's."
scene ep10_fr_tg_end28 with dissolve
play sound "sound_effects/switch.mp3"
$ renpy.pause(0.5)
play music "music/ep10/licensed_music/track135.mp3"
de "Hey! This calls for a celebration! How about some music?"
if ep8_told_josy_chad:
    scene ep10_fr_tg_end31 with dissolve
    sa "What the fuck is this music?"
else:
    mc "Um... Weird tunes."
scene ep10_fr_tg_end32 with dissolve
my "Hahaha! This is the radio station Dad listens to."
my "SET US FREE!"
scene ep10_fr_tg_end33 with dissolve
mc "SET US FREE!"
if ep8_told_josy_chad:
    scene ep10_fr_tg_end34 with dissolve
    sa "Hahaha!"
else:
    scene ep10_fr_tg_end34b with dissolve
de "SET US FREE!"
my "PREACH IT, BROTHER!"
scene ep10_fr_tg_end35 with dissolve
$ renpy.pause()

stop music fadeout 10

label ep10_fr_tg_end_bella_label:
if ep10_got_contracts:
    $ new_bio("Maya", "I managed to steal Maya's contract from Patrick at Thanksgiving.")
else:
    $ new_bio("Maya", "I failed to steal Maya's contract from Patrick at Thanksgiving.")
if ep8_told_josy_chad:
    scene ep10_fr_tg_end36 with Fade(2,2,2)
else:
    scene ep10_fr_tg_end36b with Fade(2,2,2)
de "Is this the place?"
mc "Yeah, we're here."
if ep10_got_contracts:
    my "*{i}Phew{/i}* Let's go. They're waiting for us."
else:
    my "Let's go... They'll want to hear what happened."
$ guideSuggestedPage = 149
if ep8_told_josy_chad:
    scene ep10_fr_tg_end37 with dissolve
else:
    scene ep10_fr_tg_end37b with dissolve
de "Go ahead, you guys. I need a minute."
play music "music/ep10/licensed_music/track151.mp3"
scene ep10_fr_tg_end38 with dissolve
mc "Are you ok?"


if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

if ep10_got_contracts:
    scene ep10_fr_tg_end39 with dissolve
    de "I can't believe we did it... Well, {b}you{/b} did it."
    scene ep10_fr_tg_end40 with dissolve
    menu:
        "We're not done yet":
            mc "We're not out of the woods yet."
            scene ep10_fr_tg_end39 with dissolve
            de "It still feels like a victory... It's about time."
            scene ep10_fr_tg_end40 with dissolve
            mc "Yeah... It kind of does."
        "You helped me do it \n{size=-4}[m_c1][mod_choices[2]][m_c2][mod_choices[4]]":
            $ dk(-1)
            $ RPderek += 1
            mc "I couldn't have done it without you."
            scene ep10_fr_tg_end39 with dissolve
            de "I was about to give up when we drove away."
            scene ep10_fr_tg_end40 with dissolve
            mc "But we both changed our minds and powered through. That's what matters."
else:
    scene ep10_fr_tg_end39 with dissolve
    de "I will be. I have to."
    scene ep10_fr_tg_end40 with dissolve
    menu:
        "We'll find another way":
            mc "We'll find another way to help her."
            scene ep10_fr_tg_end39 with dissolve
            de "I don't want to be a downer, but I don't think we will."
        "You're not giving up, right?":
            mc "You're not giving up, right?"
            scene ep10_fr_tg_end39 with dissolve
            de "Truth be told, I didn't believe this play would work in the first place."
    scene ep10_fr_tg_end40 with dissolve
    mc "Have some faith..."
    scene ep10_fr_tg_end39 with dissolve
    de "My dad had faith. Look what it got him."
    de "It's fine, [name]."

scene ep10_fr_tg_end41 with dissolve
de "[name]... About before... I should have told you about Dad, but...it was too hard."
scene ep10_fr_tg_end42 with dissolve
mc "You should have told me that your dad is abusing Maya. And maybe you too?"
scene ep10_fr_tg_end43 with dissolve
de "It's not like that."
de "Dad's gotten a bit rough with us in the past, but he doesn't hit us."
scene ep10_fr_tg_end42 with dissolve
mc "What I saw him do to Maya is still abuse, dude..."
mc "Not to mention the whole psychological abuse."
scene ep10_fr_tg_end43 with dissolve
de "I don't expect you to understand this, but it's not been easy for him."
de "He basically raised us on his own. Mom did what she could, but Dad's been carrying this heavy burden all my life."
scene ep10_fr_tg_end44 with dissolve
de "Having to provide for us, taking care of Mom and us... He's pushing himself daily for his family."
de "His beaker is almost always full, and at times, it overflows."
scene ep10_fr_tg_end43 with dissolve
de "I know it doesn't justify his actions...but...he's still our dad."
de "And all I could do about it was to be there for Maya. Always and ever..."
de "That's why I'm here today, [name]."
scene ep10_fr_tg_end42 with dissolve
mc "What do you mean?"
scene ep10_fr_tg_end39 with dissolve
de "I mean, that's why I'm in college. It's been cool to party and try to hook up with girls and all..."
de "But I'm really doing it for Maya. Wherever she goes, I will follow."
scene ep10_fr_tg_end40 with dissolve
$ renpy.pause()
scene ep10_fr_tg_end39 with dissolve
de "She doesn't know that's the reason, and it's fine. I think it's best if she doesn't know it. But it's what I want to do."
scene ep10_fr_tg_end45 with dissolve
de "I owe it to Mom. And I owe it to Dad, too."
de "Even if Dad doesn't see it our way, I'm doing it for my family."
de "Maybe someday he will realize he's been wrong with how he treats Maya."
scene ep10_fr_tg_end46 with dissolve
mc "Derek..."
de "No, no... Don't touch me. I'm a slight graze away from bursting."
de "And I'm not talking about my dick. Haha..."
scene ep10_fr_tg_end47 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(-Sage)","(+Josy)","(-DIK)","(+DIK)","(+Derek)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Hug him [m_c1][mod_choices[4]]":
        $ RPderek += 1
        scene ep10_fr_tg_end50 with dissolve
        if dtype > 0:
            mc "Fuck you. I'm still doing it."
        else:
            mc "I'm still doing it."
        de "*{i}Sobs{/i}*"
        scene ep10_fr_tg_end51 with dissolve
        $ renpy.pause()
        mc "Derek. You should do something for yourself, too. If college isn't what you wanna do with your life, you shouldn't do it."
        mc "You can still be there for Maya."
        de "And do what? I have no clue what I wanna do with my life."
    "Let him recover":
        scene ep10_fr_tg_end48 with dissolve
        $ renpy.pause()
        scene ep10_fr_tg_end49 with dissolve
        $ renpy.pause()
        scene ep10_fr_tg_end42 with dissolve
        mc "Derek. You should do something for yourself, too. If college isn't what you wanna do with your life, you shouldn't do it."
        mc "You can still be there for Maya."
        scene ep10_fr_tg_end39 with dissolve
        de "And do what? I have no clue what I wanna do with my life."
scene ep10_fr_tg_end40 with dissolve
mc "You have to figure that one out for yourself."
mc "But I don't think Maya would want you to live your life just for her."
mc "And I think you know that too. Or else you would have told her about this."
scene ep10_fr_tg_end39 with dissolve
de "I just wanted her to be safe first."
scene ep10_fr_tg_end52
show screen ep10_snow_screen
with dissolve
$ renpy.pause()
if ep10_got_contracts:
    scene ep10_fr_tg_end53 with dissolve
    mc "Let's make sure she can be safe, then."
else:
    scene ep10_fr_tg_end53 with dissolve
    mc "Then don't give up on her now. She needs you."
    mc "Let's make sure she can be safe together."
scene ep10_fr_tg_end54 with dissolve
$ renpy.pause()
if RPderek > 5:
    scene ep10_fr_tg_end55 with dissolve
    if not ep9_derek_better_friend:
        de "[mc_de_up]... I know I'm not your best friend, but you're mine."
        de "I love you."
    else:
        de "I love you, [mc_de]."
    scene ep10_fr_tg_end56 with dissolve
    mc "I love you, too."
scene ep10_fr_tg_end57 with dissolve
$ new_bio("Derek", "Derek opened his heart to me and told me about his family and why he's in college.")
jump ep10_ending_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

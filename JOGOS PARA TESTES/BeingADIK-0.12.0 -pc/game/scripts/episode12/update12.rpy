label startUpdate12:
    

jump header_ep12_label
label previousEp12Label:


   

$ guideSuggestedPage = 227
play music "music/patched/track_previous2.mp3"
scene black
$ renpy.pause(2)
hide screen new_phone_screen
$ previousEpLabel = "startUpdate12b"
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen
show ep11_jparty8 with wipeleft
dw "You girls broke our agreement."
scene ep11_jparty6
sa "We're at your Christmas party tonight, as agreed upon."
scene ep11_jparty8
dw "Yeah, but you went to the DIKs yesterday!"
scene ep11_jparty9
al "Where do we draw the line with this?"
scene ep11_jparty11
dw "There's zero chance the DIKs are getting the New Year's party now."

scene ep11_lab10 with wiperight
no "Sally, you're with [name]."
scene ep11_lab16
sy "[name]? That's even worse!"
scene ep11_sally10
mc "You don't have to feel ashamed. I think some stuff is hard, too."
scene ep11_sally40
sy "Wanna study some before class? Like, later this week or whenever?"
if ep11_sally_kiss:
    scene anim_sally_kiss_ep11 with dissolve
    pause

scene ep11_nerds12 with wipeleft
mg "The tri-alphas, the alpha nu omegas, the delta iota kappas... Finally, they will all get what's coming to them."
scene ep11_prep15
mg "When we're done, the only frat worth its salt on campus is ours."
scene ep11_jocks_end13
dw "The DIKs put the condom in my shaker!? I drank their cum!?"

if ep11_fighter:
    scene ep11_gym3 with wiperight
    chao "Are you entering the December tournament?"
    scene ep11_gym9
    mc "Ok. I wanna do it."
    scene ep11_gym10
    dwy "That's my boy."
if ep11_music:
    scene ep11_math90 with wiperight
    mc "Do you want me to perform for the faculty?"
    scene ep11_math94
    ph "I'm thinking a smaller performance of 20 minutes or so should suffice."
    scene ep11_math93
    mc "Ok, I'll do it. It sounds fun!"

if branchSage:
    scene ep11_shome26 with wipeleft
    sa "You're dropping by your ex-girlfriend tomorrow?"
    scene ep11_shome27
    mc "I'm dropping by my friend tomorrow."
    scene ep11_shome26
    sa "Your friend who you used to fuck."

scene ep11_pp_zoey_end38 with wipeleft
zo "I love you."
if branchZoey:
    scene anim_zoey_kiss_ep11 with dissolve
    mc "Do you love me?"
    mc "Since...when?"
    zo "For years."
else:
    scene ep11_pp_zoey_end92
    mc "No... I can't. It's... Way too late."
    scene ep11_pp_zoey_end94
    zo "So, you're saying...? Never?"

scene ep11_md21 with wiperight
pa "I promised myself that I wouldn't turn out like my father."
scene ep11_md23
pa "*{i}Sobs{/i}* I'm sorry. It wasn't supposed to turn out this way. Nothing was."
scene ep11_md33
my "I...forgive you."

scene ep11_quinn104 with wipeleft
qu "..."
qu "Rio... What have they done to you?"
scene ep11_quinn106
ri "You said you were protecting me from them."
scene bg anim_pliers_ep11 movie with dissolve
ri "You fucking lied to me... You lied to me."
qu "I'll make them pay for what they did to you."
scene bg anim_quinn_end_ep11b movie with dissolve
qu "We do anything to survive, yeah? Maybe the ermine learned one of the tricks from the rat?"

if branchMayaJosy and not branchZoey:
    scene ep11_jmc3 with wiperight
    mc "I told Dad about you girls and us. But I felt like he didn't understand what we were doing together."
    scene ep11_jmc9
    my "At times, we don't even understand what this is ourselves. How can we expect our parents to understand?"
    scene ep11_jmc12
    js "I couldn't bring both of you back home either."
    if ep11_josy_solo:
        scene ep11_jsolo122
        js "Don't take this the wrong way, but I like it when it's just us."
        js "I feel like our talks are deeper when we're alone."
        if ep11_josy_love == 2:
            scene ep11_jsolo127
            mc "I love you."
            scene ep11_jsolo129
            js "I love you, too."
        elif ep11_josy_love == 1:
            scene ep11_jsolo127
            mc "I love you."
            scene ep11_jsolo128
            js "I... I'm not sure what to say..."
    elif ep11_maya_solo:
        scene ep11_msolo6
        mc "So, why didn't Josy come with us?"
        scene ep11_msolo8
        my "Is it just me, or has she been withdrawn lately?"
        if ep11_maya_love > 0:
            scene ep11_msolo43
            my "Do you love me?"
            if ep11_maya_love == 2:
                scene ep11_msolo48
                mc "I can feel it... I do."
                scene ep11_msolo50
                my "I love you too."
            elif ep11_maya_love == 1:
                my "You shouldn't."
                scene ep11_msolo44
                mc "But I do."
    scene ep11_josy_hobby3
    js "I've started a blog on CB, ok?"
    js "It's nothing much yet, but I've gained a few hundred followers in a short time."

if branchSage and not branchZoey:
    scene ep11_sage_party9 with wiperight
    sa "I went back home today."
    sa "And I got caught in the middle of a fight."

    scene ep11_sage_party19
    sa "My father... My so-called role model never wanted to be my dad."

    scene ep11_ssolo122
    ja "Of course, it hurts. The truth always hurts. Stephen is hurtful!"
    ja "But you deserve to hear it."
    scene ep11_ssolo125
    sa "Do I deserve to hear it? Do I deserve to hear that I'm unwanted?"

    if jade_state > 0:
        scene ep11_ssolo50
        mc "How is your relationship with your mom? How...important is it to you?"
        scene ep11_ssolo51
        sa "What do you mean? She's my mom. It's very important to me."

    scene ep11_ssolo65
    sa "What do you see when you close your eyes and imagine your future family? Try it."
    if ep11_sage_questions[0]:
        scene ep11_ssolo68
    else:
        scene ep11_ssolo69
    mc "There's a girl next to me. It could be my wife."
    if ep11_sage_questions[0]:
        mc "It could be you."
    else:
        mc "I don't see her face."
    if ep4_toldDerekAboutJade:
        scene ep11_ssolo99
        sb "You fucked my wife and now you're dating my daughter..."
        sb "You've got some serious nerve, kid. Or perhaps it's brain damage?"

if branchJill and not branchZoey:
    scene ep10_jill_fam19 with wiperight
    ge "And who is this lad?"
    scene ep10_jill_fam21
    mc "(Whoa! Is that alcohol I smell...?)"
    scene ep10_jill_fam67
    ji "This is not how I wanted today to go."
    scene ep10_jill_fam65
    mc "It's the next step in our relationship and I'm happy to take it."

    scene ep10_jill_fam75
    mc "This room is totally different from all the other rooms."
    scene ep10_jill_fam72
    ji "Yes. It's a sanctuary for Lana now."
    scene ep10_jill_fam87
    mc "You look so much alike."

if branchIsabella and not branchZoey:
    scene ep10_bbq_isabella_end22 with wiperight
    isa "Why don't you ask me about him?"
    mc "I've tried in the past. But I know it's not something you want to discuss, or you would have brought it up."
    scene ep10_bbq_isabella_end34
    isa "I feel like I've been constantly drowning, [name]."
    scene ep10_bbq_isabella_end36
    isa "And when I met you, I realized I was drowning less with time."
    scene ep10_bbq_isabella_end34
    isa "Please... Stay with me."

if ep11_bianca_path and not branchZoey:
    scene ep11_pp_bia_event24 with wipeleft
    mc "I can't stop flirting with you."
    play sound "sound_effects/slap.mp3"
    scene ep11_pp_bia_event41 with hpunch
    bia "I've touched myself thinking about you. How's that for an answer?"

if ep11_rolling:
    scene anim_lily_kiss_ep11 with wiperight
    if ep11_lily_want_more:
        mc "(There's tension between us... I'm not imagining it.)"
    else:
        mc "(Fuck... I'm not imagining it... She's feeling different about me for some reason.)"
    scene ep11_lily_lewd53
    mc "That was so good..."
    scene ep11_lily_lewd55
    mc "Where are you going?"

scene ep5_morning7_blink0 with wipeleft
mc "It might sound stupid, but what's in her locked room?"
scene ep5_morning8
ji "What locked room?"
scene ep5_morning7_blink0
mc "The one next to her bathroom..."
scene ep5_morning18
ji "Cut her some slack and let her have some privacy, ok?"

play sound "sound_effects/table_slam.mp3"
$ renpy.sound.play("sound_effects/glass.mp3", channel="sfx2", loop=False)
$ renpy.sound.play("sound_effects/season2/bottle_smash.mp3", channel="sfx3", loop=False)
scene ep11_ending22 with vpunch
de "AHHHHH!!!"
scene ep11_ending29
my "Where are the towels!?"
scene ep11_ending32
mc "..."
scene ep11_ending33
$ renpy.pause()

label startUpdate12b:
if steamConfig or nonPatreonConfig:
    if branchIsabella:
        $ state = "ep12_steam_isabella"
    elif branchSage:
        $ state = "ep12_steam_sage"
    elif branchMayaJosy:
        if ep11_josy_solo:
            $ state = "ep12_steam_jm"
        else:
            $ state = "ep12_steam_jm2"
    elif branchJill:
        $ state = "ep12_steam_jill"
    else:
        if branchZoey:
            $ state = "ep12_steam_others"
        elif ep11_quinn_question[0] and ep11_quinn_question[1]:
            $ state = "ep12_steam_others2"
        elif ep11_nicole_dating:
            $ state = "ep12_steam_others3"
        elif ep11_rolling:
            $ state = "ep12_steam_others4"
        else:
            $ state = "ep12_steam_others5"
else:
    if branchIsabella:
        $ state = "ep12_isabella"
    elif branchSage:
        $ state = "ep12_sage"
    elif branchMayaJosy:
        if ep11_josy_solo:
            $ state = "ep12_jm"
        else:
            $ state = "ep12_jm2"
    elif branchJill:
        $ state = "ep12_jill"
    else:
        if branchZoey:
            $ state = "ep12_others"
        elif ep11_quinn_question[0] and ep11_quinn_question[1]:
            $ state = "ep12_others2"
        elif ep11_nicole_dating:
            $ state = "ep12_others3"
        elif ep11_rolling:
            $ state = "ep12_others4"
        else:
            $ state = "ep12_others5"
call rpc from _call_rpc_4
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black
$ renpy.pause(0.5)

label ep12_intro_label:
play sound "sound_effects/season2/tick_tock.mp3"
scene bg anim_intro_ep12 movie with fade
if persistent.seen_cutscene_ep12[0]:
    $ renpy.pause(4)
    play music "music/ep12/licensed_music/track192.mp3"
    $ renpy.pause(44)
else:
    #$ _skipping = False
    $ renpy.pause(4, hard=True)
    play music "music/ep12/licensed_music/track192.mp3"
    $ renpy.pause(44, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep12[0] = True

scene ep12_intro1 with dissolve
$ renpy.pause()
scene ep12_intro2 with dissolve
$ renpy.pause()
scene ep12_intro3 with dissolve
$ renpy.pause()
scene ep12_intro4 with dissolve
$ renpy.pause()
scene ep12_intro5 with dissolve
jam "What are you thinking?"
scene ep12_intro6 with dissolve
isa "The house feels empty without them."
#if not steamConfig and not nonPatreonConfig and persistent.mod_wtenabled != None:
#    $ renpy.quit()
scene ep12_intro7 with dissolve
jam "..."
scene ep12_intro6 with dissolve
isa "Yet... I can still feel like they're here. It has their scent..."
isa "It's as if their souls remained here. Maybe that sounds weird."
scene ep12_intro5 with dissolve
jam "It doesn't sound weird. This was their home. This is what you associate them with. This is where you grew up."
jam "Of course, you can still feel them here."
scene ep12_intro8 with dissolve
isa "There used to be a wall here, and we had a small reading area in its corner."
show ep12_intro9
if not persistent.ep12_cardcam1:
    show screen ep12_render_screen("cam1")
with dissolve
isa "After I moved out, they removed the wall to make this spacious room. And they moved the reading area into my old room."
isa "I had to tell them that I didn't need my old room so many times before they went through with it."
isa "But they wanted to keep my room as it was..."
show ep12_intro10
hide screen ep12_render_screen
with dissolve
isa "They said they couldn't believe that I had grown up and moved out. And leaving my room untouched made it feel like I never had left."
isa "At the time, I didn't understand what they meant by that. I'd still come to visit..."
isa "And just like I wanted my life to enter that new phase of college and independence..."
scene ep12_intro11 with dissolve
isa "I wanted them to have something new to look forward to."
isa "A life where we weren't just Mom, Dad, and Daughter. But a life where we were also best friends and could talk to each other as such."
scene ep12_intro12 with dissolve
isa "*{i}Sobs{/i}*"
scene ep12_intro13 with dissolve
$ renpy.pause()
scene ep12_intro15 with dissolve
isa "I don't know how to do this without them."
isa "I don't know how to do this without you either."
scene ep12_intro16 with dissolve
jam "You're not without me. I'm right here."
jam "We'll get through this together. We'll grow stronger for it."
scene ep12_intro14 with dissolve
$ renpy.pause()
scene ep12_intro16 with dissolve
jam "Let's grab some air."
scene ep12_intro17 with dissolve
$ renpy.pause()
scene ep12_intro18 with dissolve
jam "Did you grow up with this pool?"
scene ep12_intro19 with dissolve
isa "No. This entire area used to be grass and a couple of trees."
scene ep12_intro20 with dissolve
isa "The same goes for the garage. It was all grass and gravel used as a parking space."
isa "I remember Dad had the hardest time getting the permit to build the garage."
scene ep12_intro21 with dissolve
isa "He told me how much he hated the rules and regulations of this city."
isa "And he told me that the only way to get a timely permit was to act upset and annoyed with the building authority."
scene ep12_intro22 with dissolve
isa "You'd think being rude would have the opposite effect, but they were swamped with granting permits and would process the annoying people faster to get rid of them."
isa "Haha... It wasn't until he scolded them that he finally got it approved."
isa "Dad didn't like himself for doing that, but it worked just as people advised him."
scene ep12_intro23 with dissolve
isa "When they built the pool, I didn't think they would want to go through that entire process again."
isa "Apparently, it was much simpler with the pool than with the garage."
isa "They built the pool after I had left for college, and Dad said they had me to thank for it."
isa "I had told them to move on and do something for their own enjoyment, and this pool was it."
scene ep12_intro24 with dissolve
isa "I'm proud that they did this for themselves, but I wish they could have grown old in this house."
isa "And now... I have to decide the fate of their home... It's too sudden."
isa "It's way too sudden!"
scene ep12_intro25 with dissolve
jam "I know how hard this must be. Let me offer you my thoughts."
scene ep12_intro26 with dissolve
jam "You obviously have a lot of memories here, in this house that defined your childhood."
jam "This is the house that connects you to your parents."
jam "I could never ask you to sell it."
scene ep12_intro27 with dissolve
isa "But James... We don't live here. This is not our city."
scene ep12_intro28 with dissolve
jam "But it can be our future."
scene ep12_intro29 with dissolve
jam "You know me; I'm somewhat flexible with where I live. And you can always get a job here. There are libraries here, aren't there?"
jam "With the inheritance, we can make this change for ourselves."
scene ep12_intro30 with dissolve
jam "I know we shouldn't make rash and big decisions right now, but time is a luxury we don't have."
jam "And I'm telling you if this house is where you see your future, and if it brings you happiness to live here again..."
jam "I'm with you all the way."
scene ep12_intro31 with dissolve
$ renpy.pause()

scene ep12_intro32 with Dissolve(2)
$ renpy.pause()
scene ep12_intro33 with dissolve
jam "It was the right call to hire movers."
scene ep12_intro34 with dissolve
isa "We'll get sweaty enough from unpacking."
scene ep12_intro35 with dissolve
jam "What do you want to do with their furniture?"
scene ep12_intro36 with dissolve
isa "I want to keep some of it."
isa "These specific memories pop into my head when I look at them."
scene ep12_intro37 with dissolve
isa "But at the same time, their taste was different from mine. Lots of it has to go..."
jam "Then, I'll leave those decisions up to you."
scene ep12_intro38 with dissolve
wo2 "Is this the bedroom you want it in?"
scene ep12_intro39 with dissolve
isa "Oh! No! Nothing goes in there! You can put it in the big room upstairs."
scene ep12_intro40 with dissolve
isa "I'm sorry about the stairs."
scene ep12_intro41 with dissolve
wo2 "Don't be; it's our job."
scene ep12_intro42 with dissolve
isa "..."
scene ep12_intro43 with dissolve
$ renpy.pause()
scene ep12_intro44 with dissolve
$ renpy.pause()
scene ep12_intro45 with dissolve
$ renpy.pause()
scene ep12_intro46 with dissolve
isa "..."
scene ep12_intro47 with dissolve
isa "I don't want to sleep here."
scene ep12_intro48 with dissolve
jam "I wouldn't either. We don't have to make it our bedroom."
scene ep12_intro49 with dissolve
isa "Then what will it be?"
scene ep12_intro48 with dissolve
jam "It can be anything you want."
scene ep12_intro50 with dissolve
jam "We could turn it into a guest room..."
jam "Or a study..."
scene ep12_intro51 with dissolve
jam "Or... We can leave it as it is."
jam "It's your call."
scene ep12_intro52 with dissolve
$ renpy.pause()
scene ep12_intro48 with dissolve
jam "Take the time you need. I'll check on the movers."
scene ep12_intro53 with dissolve
isa "James."
scene ep12_intro55 with dissolve
jam "Yes?"
scene ep12_intro54 with dissolve
isa "I love you."
scene ep12_intro55 with dissolve
jam "I love you too."

scene bg anim_intro2_ep12 movie with dissolve
if persistent.seen_cutscene_ep12[1]:
    $ renpy.pause(35)
    stop music fadeout 5
    $ renpy.sound.play("music/ep7/musicbox.mp3", channel="sfx1", fadein=5)
    $ renpy.pause(18.33)
else:
    #$ _skipping = False
    $ renpy.pause(35, hard=True)
    stop music fadeout 5
    $ renpy.sound.play("music/ep7/musicbox.mp3", channel="sfx1", fadein=5)
    $ renpy.pause(18.33, hard=True)
    $ _skipping = True
    $ persistent.seen_cutscene_ep12[1] = True

$ renpy.music.stop(channel="sfx1", fadeout=5)

scene 2d_jacob_screen_main with dissolve
show screen episode_title_screen
$ renpy.pause(5)
$ renpy.block_rollback()

label ep12_hospital_label:
play music "music/ep12/licensed_music/track190.mp3"
show screen new_phone_screen
scene ep12_hospital1 with fade
$ renpy.pause()
scene ep12_hospital2 with dissolve
$ renpy.pause()
scene ep12_hospital4 with dissolve
$ renpy.pause()
scene ep12_hospital3 with dissolve
$ renpy.pause()
scene ep12_hospital5 with dissolve
$ renpy.pause()
scene ep12_hospital6 with dissolve
$ renpy.pause()
scene ep12_hospital7 with dissolve
$ renpy.pause()
scene ep12_hospital10 with dissolve
js "What did the doctor say?"
scene ep12_hospital8 with dissolve
my "They rushed Derek to surgery. They will stitch him up, but they don't reattach fingertips unless they are thumbs."
my "And with the way he cut it off and how the fingertip looked, they concluded it was better not to reattach it."
scene ep12_hospital11 with dissolve
sa "They won't reattach it!? Will he have to live without the finger?"
scene ep12_hospital9 with dissolve
my "He lost slightly more than the tip. He should regain the function of what's left of the index finger... But yeah...."
scene ep12_hospital11 with dissolve
sa "How long will surgery take?"
scene ep12_hospital9 with dissolve
my "It won't take long, since they're just stitching him back up - maybe an hour or two."
scene ep12_hospital10 with dissolve
js "We can wait here until he wakes up."
scene ep12_hospital8 with dissolve
my "He is awake. They are giving him local anesthetics."
my "And yeah, I'm not leaving until I get to see him again."
scene ep12_hospital12 with dissolve
sa "We will all wait for him."
scene ep12_hospital13 with dissolve
$ renpy.pause()
scene ep12_hospital14 with dissolve
ji "I'm still shaking..."
scene ep12_hospital15 with dissolve
js "He'll be alright."
scene ep12_hospital16 with dissolve
$ renpy.pause()
scene ep12_hospital20 with dissolve
$ renpy.pause()
scene ep12_hospital19 with dissolve
sa "[name]? How are you?"
scene ep12_hospital18 with dissolve
mc "I think the adrenaline has worn off. I feel sick."
mc "About Derek... And..."
scene ep12_hospital17 with dissolve
mc "Bella? How are you doing?"
scene ep12_hospital21 with dissolve
$ renpy.pause()
scene ep12_hospital22 with dissolve
ji "*{i}Sniffles{/i}* Bella?"
scene ep12_hospital20 with dissolve
$ renpy.pause()
scene ep12_hospital17 with dissolve
mc "Bella... I'm...confused."
mc "What is that room?"
scene ep12_hospital23 with dissolve
ji "[name]..."
scene ep12_hospital24 with dissolve
mc "We all saw it. It turned my stomach to see what was in there."
scene ep12_hospital23 with dissolve
ji "But don't push her on it."
scene ep12_hospital25 with dissolve
isa "It's ok, Jill."
scene ep12_hospital27 with dissolve
isa "I hoped that I'd never have to tell you about this because it's too hard for me to talk about."
isa "But you all saw it... And..."
scene ep12_hospital22 with dissolve
ji "Bella, you don't have to explain yourself."
scene ep12_hospital25 with dissolve
isa "If I don't, it will loom over me like a dark cloud."
scene ep12_hospital26 with dissolve
$ renpy.pause()
stop music fadeout 5
scene ep12_hospital25 with dissolve
isa "I met my husband, James, back in my second year of college."
isa "He was taking single classes and learning different languages."

play music "music/ep12/licensed_music/track191.mp3"
show ep12_hospital28
if not persistent.ep12_cardcam2:
    show screen ep12_render_screen("cam2")
with dissolve
isa "We often ran into each other while studying at the campus library, and we took a liking to each other."
show ep12_hospital29
hide screen ep12_render_screen
with dissolve
$ renpy.pause()
scene ep12_hospital31 with dissolve
$ renpy.pause()
scene ep12_hospital30 with dissolve
isa "It didn't take long for us to fall in love, but I didn't realize whom I had fallen in love with."
scene ep12_hospital32 with dissolve
isa "James was three years older than me, and he served in the Special Forces."
scene ep12_hospital33 with dissolve
isa "He was taking classes between missions, and when I realized that he was going away on an intermittent basis, I thought that was it for us."
scene ep12_hospital34 with dissolve
isa "But when he returned home, he hadn't forgotten about me."
isa "And my love for him was...still as big as before he left."
scene ep12_hospital35 with dissolve
isa "We both felt it. It was true love."
scene ep12_hospital36 with dissolve
isa "After I graduated from college, we moved in together."
isa "I got used to him being away for long periods. It wasn't the best for our relationship, but it made the time we spent together invaluable."
scene ep12_hospital37 with dissolve
isa "When I was 26 years old, my parents died suddenly."
isa "They lost their lives in a freak car accident after getting T-boned by a truck."
scene ep12_hospital38 with dissolve
isa "At that time, it was the toughest crisis of my life. Luckily, I had James by my side."
isa "He was granted permission to stay off work for a while, and we decided to move into my parents' home - my house."
isa "It was hard, but we started a new life together here."
scene ep12_hospital39 with dissolve
isa "After a few years, we got married."
scene ep12_hospital40 with dissolve
isa "We talked about having a child, but it wasn't feasible with his work."
isa "He would be away on up to year-long missions, and I'd only hear from him a couple of times per month at best."
scene ep12_hospital41 with dissolve
isa "I felt so alone when he was away, but life became a routine."
scene ep12_hospital42 with dissolve
isa "After I had turned 30, I told him I wanted a child and that I wouldn't be able to wait much longer."
isa "We were both getting older, and it felt like time kept passing us by."
scene ep12_hospital43 with dissolve
isa "He wanted us to try to get pregnant, but I feared it would be too hard for me to take care of a child on my own when he's away at work."
isa "He said he was planning his retirement, but that it wasn't possible yet."
scene ep12_hospital44 with dissolve
isa "Even so...we started trying."
scene ep12_hospital45 with dissolve
isa "We tried... And we tried..."
isa "I was naive. I thought getting pregnant would be easy."
isa "I thought having unprotected sex once or twice was enough."
scene ep12_hospital46 with dissolve
isa "But the older you get, the harder it gets."
isa "And it didn't help that James left for work while we were trying."
scene ep12_hospital47 with dissolve
isa "But then, one day, he returned from a mission and said what I had waited to hear."
isa "\"I'm retiring.\""
scene ep12_hospital48 with dissolve
isa "I couldn't believe my ears."
isa "He said he would go on one final mission in four months and then return as a free man. And that our future could be anything that I wanted."
scene ep12_hospital49 with dissolve
isa "I was overjoyed to hear that, and it was as if something changed inside of me."
scene ep12_hospital50 with dissolve
isa "We both cried when we learned that I was pregnant."
isa "For me, they were happy tears, but for him... the tears were twofold."
scene ep12_hospital51 with dissolve
isa "Although he was happy about the baby, he was also sad that he had to leave me again during pregnancy."
isa "For the first time, I truly felt that he didn't want to leave."
scene ep12_hospital52 with dissolve
isa "I didn't want him to leave either. I begged him to stay."
isa "He told me he was sorry and wished he could get out of it, but he couldn't."
scene ep12_hospital53 with Dissolve(2)
isa "I saw the remorse in his eyes as he left."
isa "It hurt to see him leave, but it was supposed to be the final time he left me like that..."
stop music fadeout 5
scene ep12_hospital54 with dissolve
isa "And it was..."
isa "But in a different way than I had imagined."
play music "music/ep12/licensed_music/track190.mp3"
scene ep12_hospital55 with dissolve
isa "One night, I received a phone call."
isa "It was an officer calling me to tell me that James was M.I.A."
js "M.I.A.?"
scene ep12_hospital56 with dissolve
isa "Missing in action."
isa "The officer couldn't tell me any details but said there was a chance that James was still alive."
isa "However, they presumed that he was either dead or abducted."
scene ep12_hospital57 with dissolve
isa "I dropped the phone and screamed out loud as I received the news."
isa "It felt like a nightmare. Everything was spinning, and I felt helpless."
scene ep12_hospital58 with dissolve
isa "During the emotional time that followed, my stomach started hurting."
scene ep12_hospital59 with dissolve
isa "I had a miscarriage..."
scene ep12_hospital60 with dissolve
isa "I prayed that James still would return, but if he were alive, I wouldn't know how to tell him that our daughter was dead."
scene ep12_hospital61 with dissolve
isa "And I felt that I had to leave the nursery I prepared for her that way until he had returned..."

scene ep12_hospital62 with dissolve
$ renpy.pause()
scene ep12_hospital63 with dissolve
$ renpy.pause()
scene ep12_hospital64 with dissolve
$ renpy.pause()
scene ep12_hospital65 with dissolve
isa "I forgot to lock it..."
isa "If I had locked it... You wouldn't have known."
scene ep12_hospital66 with dissolve
ji "You have nothing to be ashamed of, Bella."
scene ep12_hospital65 with dissolve
isa "I need to get some air."
scene ep12_hospital67 with dissolve
$ renpy.pause()
scene ep12_hospital68 with dissolve
mc "..."
scene ep12_hospital69 with dissolve
mc "What do I do? Can I follow?"
scene ep12_hospital70 with dissolve
my "Yes. Go with them."
scene ep12_hospital69 with dissolve
mc "But... But... What do I say?"
scene ep12_hospital70 with dissolve
my "Just be there for her."

scene ep12_hospital71 with dissolve
$ renpy.pause()
scene ep12_hospital72 with dissolve
isa "*{i}Shudders{/i}*"
scene ep12_hospital73 with dissolve
ji "Bella, it's too cold outside."
scene ep12_hospital74 with dissolve
isa "I can't go back in there."
scene ep12_hospital75 with dissolve
ji "Everyone understands. They will support you. Right, [name]?"
scene ep12_hospital76 with dissolve
mc "Uh... Yeah."
scene ep12_hospital73 with dissolve
ji "If you can't go back inside, at least let's sit in the car for a while."

play sound "sound_effects/season3/car_door.mp3"
scene ep12_hospital77 with dissolve
$ renpy.pause()
scene ep12_hospital80 with dissolve
$ renpy.pause()
scene ep12_hospital78 with dissolve
$ renpy.pause()
scene ep12_hospital79 with dissolve
isa "After I had miscarried... I was lost."
scene ep12_hospital87 with dissolve
isa "I stayed at home from work for a while."
scene ep12_hospital88 with dissolve
isa "And they gave me antidepressants to manage the sorrow."
isa "But no amount of pills could make it better."
scene ep12_hospital89 with dissolve
isa "I had lost everything of importance to me."
isa "I tried my best to survive the hell I was living in, but I couldn't..."
ji "*{i}Sobs{/i}*"

show ep12_hospital90
if not persistent.ep12_cardcam3:
    show screen ep12_render_screen("cam3")
with dissolve
isa "I went back to work and tried to return to daily life."
show ep12_hospital91
hide screen ep12_render_screen
with dissolve
isa "I started to see James everywhere."
isa "He talked to me as if he were there with me. And I talked to him."
scene ep12_hospital92 with dissolve
isa "But it was all in my head."
scene ep12_hospital93 with dissolve
isa "I wasn't ready to return to work, and they made me leave again."
isa "And as they were laying off personnel, I was laid off too."
scene ep12_hospital94 with dissolve
isa "With nowhere to go and no one by my side, I stopped caring about it all..."
isa "I didn't want to live anymore."
scene ep12_hospital95 with dissolve
isa "So, I grabbed a bottle of sleeping pills they had given me and..."
scene ep12_hospital96 with dissolve
mc "Oh my God..."

scene ep12_hospital97 with dissolve
isa "Luckily... My old neighbor spotted me as I collapsed on the kitchen floor."
scene ep12_hospital98 with dissolve
isa "I woke up alone in a hospital bed."
isa "It was as if something or someone didn't want me to go that way."
scene ep12_hospital99 with dissolve
isa "I was given a second chance, and the hospital coerced me into getting help."
scene ep12_hospital81 with dissolve
$ renpy.pause()
scene ep12_hospital84 with dissolve
$ renpy.pause()
scene ep12_hospital82 with dissolve
mc "(I can't believe this... Fuck...)"
mc "(How is she doing now? Can I even ask her?)"
scene ep12_hospital85 with dissolve
$ renpy.pause()
scene ep12_hospital83 with dissolve
mc "I'm going to head back inside..."
play sound "sound_effects/season3/car_door.mp3"
scene ep12_hospital86 with dissolve
ji "[name]?"

scene ep12_hospital100 with dissolve
$ renpy.pause()
scene ep12_hospital101 with dissolve
my "He is getting stitched up. We'll get out of here soon."
my "No, you don't have to come here. We're all here with him; stay at home with Mom."
scene ep12_hospital102 with dissolve
my "Yeah, I can do that. If you insist..."
my "I'll let you know."
scene ep12_hospital103 with dissolve
my "Uh... Wow. Bye."
scene ep12_hospital104 with dissolve
js "What's wrong?"
scene ep12_hospital105 with dissolve
my "Dad said he loved me. I think he was in shock."
scene ep12_hospital106 with dissolve
my "He wanted to come here, but I told him not to."
my "But he insisted on seeing Derek, so I promised to let him know when we're leaving."
scene ep12_hospital107 with dissolve
js "[name]? How is Bella?"
scene ep12_hospital108 with dissolve
mc "I feel queasy."
scene ep12_hospital109 with dissolve
sa "What's the matter?"
scene ep12_hospital110 with dissolve
mc "It's Bella... I..."
mc "I can't handle this."
scene ep12_hospital109 with dissolve
sa "There isn't a perfect way of doing it. All you can do is sympathize and listen."
scene ep12_hospital110 with dissolve
mc "She told me she attempted suicide."
scene ep12_hospital111 with dissolve
js "What?"
scene ep12_hospital112 with dissolve
mc "Help me. What do I even say to that?"
mc "I... I..."
scene ep12_hospital113 with dissolve
$ renpy.pause()
scene ep12_hospital114 with dissolve
$ renpy.pause()
show ep12_hospital115
if not persistent.ep12_cardcam4:
    show screen ep12_render_screen("cam4")
with dissolve
$ renpy.pause()
show ep12_hospital116
hide screen ep12_render_screen
with dissolve
sa "Bella's car is gone. They left."
scene ep12_hospital117 with dissolve
js "Jill is with her, right?"
scene ep12_hospital118 with dissolve
my "Maybe they went back home."
my "Let them have some space. If Jill is with Bella, I'm sure they are all right."
stop music fadeout 3
scene ep12_hospital119 with dissolve
$ renpy.pause()

$ new_bio("Isabella", "Isabella attempted suicide after James went M.I.A. and she had lost her child.")

label ep12_prep_label:
hide screen new_phone_screen
play music "music/ep2/freedom.mp3"
scene ep12_prep1 with wipeleft
ty "Everybody, get in the meeting room! NOW!!!"
scene ep12_prep2 with dissolve
tr "Why are you shouting?"
scene ep12_prep3 with dissolve
ty "Because it hurts to walk downstairs."
ty "Bring everyone! That's an order from your president."
scene ep12_prep4 with dissolve
tr "You heard him."
scene ep12_prep5 with dissolve
go "Aw... A meeting now? But it's our free time."
scene ep12_prep6 with dissolve
tr "There better be a good reason to call a meeting at this hour."
scene ep12_prep7 with dissolve
ty "They've surely done it this time. It's outrageous!"
scene ep12_prep17 with dissolve
rich "Who has done what?"
scene ep12_prep8 with dissolve
ty "Those dirty fraternity slobs! The Delta Iota Kappas!"
scene ep12_prep9 with dissolve
ty "I suppose none of you know anything about this."
scene ep12_prep18 with dissolve
cr "Is that a letter?"
scene ep12_prep9 with dissolve
ty "Aha! So, you do know about it! What do you know?"
scene ep12_prep18 with dissolve
cr "Nothing. I saw it in your hand and guessed it was a letter."
scene ep12_prep10 with dissolve
ty "Well, my first guess was that it was a telegram, but it was not."
scene ep12_prep11 with dissolve
ty "What are you wearing!?"
scene ep12_prep19 with dissolve
lu "..."
scene ep12_prep11 with dissolve
ty "That is MY suit! Are you stealing my look?"
scene ep12_prep25 with dissolve
cr "I warned you..."
scene ep12_prep11 with dissolve
ty "You cannot wear that. Take it off! It's an order."
scene ep12_prep20 with dissolve
lu "Come on! It's a suit. I bought it for myself."
scene ep12_prep26 with dissolve
rich "Seriously... That's a low-class move, Lucas."
scene ep12_prep11 with dissolve
ty "Do you think it's funny? Do you see anyone laughing?"
ty "You and I need to have a serious discussion about your future here if this is the kind of antics that you get your jollies from."
scene ep12_prep27 with dissolve
tr "Can't this argument wait? Rich needs to return to writing his essay, and I had a long day."
tr "Get to the point about the letter."
scene ep12_prep12 with dissolve
$ renpy.pause()
scene ep12_prep13 with dissolve
ty "As I was saying..."
ty "Someone put this telegram-looking letter by my door. This is what it reads..."
play sound "sound_effects/season3/paperbag.mp3"
scene ep12_prep14 with dissolve
ty "\"The DIKs\"-"
scene ep12_prep15 with dissolve
ty "That's colloquial for Delta Iota Kappas, if you're not following."
scene ep12_prep14 with dissolve
ty "\"The DIKs are a threat that needs to be dealt with once and for all. The time is now.\""
ty "\"The proof in this letter should tell you all you need to know.\""
ty "\"The DIKs have wronged many. But together we are strong. Together we are Legion.\""
scene ep12_prep21 with dissolve
lu "That sounds so cringe."
scene ep12_prep25 with dissolve
cr "Shh..."
scene ep12_prep14 with dissolve
ty "\"Let's bring the battle to their doorstep. Fight with all your might.\""
ty "\"If you're still not convinced. Look at the material using this link.\""
ty "And then it ends with a link to a website."
scene ep12_prep17 with dissolve
rich "What's on it?"
scene ep12_prep16 with dissolve
ty "I haven't got the foggiest idea. All I had to see were the atrocious images in the envelope to know that this was the real deal."
ty "Take a look at them! Pass them around!"
if ep2_tybaltPhotoMc:
    scene ep12_prep28 with dissolve
else:
    scene ep12_prep28b with dissolve
go "What are we looking at?"
scene ep12_prep24 with dissolve
lu "I saw some of these on campus already. Didn't you?"
lu "Mine has someone voiding their bladder on Tybalt's bed."
scene ep12_prep29 with dissolve
ty "Do you find this amusing!?"
scene ep12_prep23 with dissolve
cr "No, I'm sure he doesn't. Right?"
scene ep12_prep22 with dissolve
lu "No..."
scene ep12_prep30 with dissolve
$ renpy.pause()
scene ep12_prep32 with dissolve
rich "Oh! That's your family's heirloom!"
scene ep12_prep31 with dissolve
ty "It is! And there they are, posing with it as if it's theirs."
scene ep12_prep33 with dissolve
cr "And that's my cane and top hat. They stole those, too, and I'm missing a suit."
scene ep12_prep34 with dissolve
tr "These are pictures from your room... So, the DIKs were the burglars all along?"
scene ep12_prep31 with dissolve
ty "Theft and pranks! That's what they are all about."
ty "And from the sound of it, many more have been affected by the Delta Iota Kappas' antics."
scene ep12_prep35 with dissolve
go "I can't stand them either. On top of this, they stole Beth from me."
scene ep12_prep36 with dissolve
rich "Who's Beth?"
scene ep12_prep33 with dissolve
cr "It's a girl he likes. She made out with a DIK at their Halloween party."
scene ep12_prep31 with dissolve
ty "They love taking what's not theirs to take - including our women."
scene ep12_prep36 with dissolve
rich "Show us the website. I have to see what that one is about. What else did they do?"
play sound "sound_effects/season3/type1.mp3"
show ep12_prep37
if not persistent.ep12_cardcam5:
    show screen ep12_render_screen("cam5")
with dissolve
ty "Nothing will surprise me at this stage. I'm sure there will be more material of this nature."
show ep12_prep38
hide screen ep12_render_screen
with dissolve
go "What's that?"
scene ep12_prep39 with dissolve
cr "It looks like drone footage of our mansion."
scene ep12_prep40 with dissolve
tr "That's during our alumni party. Look... You guys are on it."
rich "They spied on us?"
scene ep12_prep41 with dissolve
ty "Reconnaissance... Classic thieves."
ty "Don't forget how they ruined that party for us. And how they humiliated our esteemed guests."
ty "This proves that it was premeditated."
scene ep12_prep27 with dissolve
tr "That's subpar behavior, but what are we going to do?"
scene ep12_prep43 with dissolve
ty "And that's the spirit! What are we going to do!?"
if ep4_toldDerekAboutJade:
    scene ep12_prep46
    ja "{i}I'm gonna fuck your brains out, [name]!{/i}"
    scene ep12_prep45 with dissolve
    mc "{i}Ride me, Jade!{/i}"
    rich "Isn't that...?"
    stop music fadeout 3
    scene ep12_prep42 with dissolve
    ty "NOOOOOOOOOOOOOOOOO!!! MOMMY!!!"
else:
    stop music fadeout 3
    scene ep12_prep44 with dissolve
    $ renpy.pause()

label ep12_bellas_label:
show screen new_phone_screen
play music "music/ep7/licensed_music/track48.mp3"
scene ep12_bellas1 with wiperight
$ renpy.pause()
play sound "sound_effects/door_knock.mp3"
scene ep12_bellas2 with dissolve
"*{i}Door knock{/i}*"
pa "Hello? Derek! Maya!"
play sound "sound_effects/season3/door_open.mp3"
scene ep12_bellas3 with dissolve
$ renpy.pause()
scene ep12_bellas4 with dissolve
pa "Hello? The door was unlocked. I'm Patrick. I'm Derek and Maya's Dad."
scene ep12_bellas5 with dissolve
pa "Hello? Is anyone at home?"
scene ep12_bellas6 with dissolve
$ renpy.pause()
scene ep12_bellas7 with dissolve
$ renpy.pause()
scene ep12_bellas8 with dissolve
$ renpy.pause()
scene ep12_bellas9 with dissolve
$ renpy.pause()
scene ep12_bellas10 with dissolve
de "Dad?"
scene ep12_bellas11 with dissolve
pa "Derek!"
pa "What have you done to yourself?"
scene ep12_bellas12 with dissolve
de "My finger came off. It's the weirdest thing."
scene ep12_bellas13 with dissolve
pa "Dear Lord... How are you feeling?"
scene ep12_bellas14 with dissolve
de "They gave me some painkillers and antibiotics... Haha... I'm doing fine..."
scene ep12_bellas15 with dissolve
de "The doctor said they couldn't put the fingertip back. So it will be shorter from now on."
de "It's going to be weird not having a nail..."
scene ep12_bellas13 with dissolve
pa "I was worried sick... Helen was too. She wanted to come, but I had to stop her."
scene ep12_bellas16 with dissolve
de "I'm fine. My friends helped me get to the hospital and back."
de "I'm gonna call Mom and calm her down."
scene ep12_bellas17 with dissolve
$ renpy.pause()
scene ep12_bellas18 with dissolve
pa "Maya..."

scene ep12_bellas20 with dissolve
my "I thought you wouldn't come... How did you even know where Bella lived?"
scene ep12_bellas19 with dissolve
pa "I know, I know. But I had to see you. I checked the car app for recent trip data."
pa "Are you ok?"
scene ep12_bellas20 with dissolve
my "I'm fine, Dad. But it was scary there for a moment."

scene ep12_bellas19 with dissolve
pa "I'm lucky that you were there with him."
scene ep12_bellas21 with dissolve
sa "You should have seen her; she did great. She didn't even hesitate after it happened."
scene ep12_bellas22 with dissolve
$ renpy.pause()
scene ep12_bellas24 with dissolve
pa "Josy... I wasn't expecting to meet you here."
scene ep12_bellas23 with dissolve
js "Hello... It's...um...been a while."
if not ep10_got_contracts:
    scene ep12_bellas25 with dissolve
    my "She's just my friend, Dad."
    scene ep12_bellas26 with dissolve
    $ renpy.pause()
else:
    scene ep12_bellas25 with dissolve
    my "Please, don't make a big deal of this, Dad."
scene ep12_bellas27 with dissolve
pa "Thank you all for being there for my son. I wanted to see for myself that he was ok."
pa "And while I have you here, I'd also like to apologize for my behavior during Thanksgiving."
scene ep12_bellas28 with dissolve
pa "I'll leave and let you all recover. Again... Thank you for helping my son get to the hospital."
scene ep12_bellas31 with dissolve
my "Dad, you can take the car. We'll manage without it."
scene ep12_bellas29 with dissolve
pa "Are you sure?"
scene ep12_bellas31 with dissolve
my "Mhm. The keys are in my jacket pocket."
scene ep12_bellas30 with dissolve
$ renpy.pause()
scene ep12_bellas32 with dissolve
sa "That was something..."
scene ep12_bellas34 with dissolve
my "I haven't had a chance to tell you yet, but we had a good moment together earlier today when we went to borrow the car."
my "I think there might be hope for him..."
scene ep12_bellas33 with dissolve
sa "That's amazing..."
if not ep10_got_contracts:
    scene ep12_bellas35 with dissolve
    js "*{i}Mumbles{/i}* Friend..."


scene ep12_bellas36 with dissolve
mc "Since Bella and Jill aren't here, should we try their phones?"
stop music fadeout 3
scene ep12_bellas37 with dissolve
sa "I'll do it."
play music "music/ep12/licensed_music/track194.mp3"
scene ep12_bellas38 with dissolve
$ renpy.pause()
scene ep12_bellas39 with dissolve
$ renpy.pause()
scene ep12_bellas40 with dissolve
$ renpy.pause()
scene ep12_bellas41 with dissolve
$ renpy.pause()
scene ep12_bellas42 with dissolve
$ renpy.pause()
scene ep12_bellas43 with dissolve
js "[name]? How are you feeling?"
scene ep12_bellas44 with dissolve
mc "I'm worried I fucked it up..."
scene ep12_bellas43 with dissolve
js "Fucked what up?"
scene ep12_bellas44 with dissolve
mc "Back at the hospital and in the car with Bella..."
mc "I panicked..."
scene ep12_bellas45 with dissolve
mc "I was at a loss for words..."
mc "You think you know someone..."
scene ep12_bellas46 with dissolve
mc "Not in a million guesses would I have guessed that this is what she kept in here."
scene ep12_bellas47 with dissolve
mc "I'm worried I made it worse for her. I forced it out of her, but at the same time, I couldn't handle hearing about it."
scene ep12_bellas48 with dissolve
$ renpy.pause()
scene ep12_bellas49 with dissolve
js "We all react in different ways."
js "Like me, when Derek cut his finger... I just stood there."
scene ep12_bellas50 with dissolve
js "Everyone else was running around trying to help, but I froze."
js "It took me a while to be helpful... Maybe that's what happened to you, too, with Bella."
scene ep12_bellas51 with dissolve
sa "[name]! Josy! They're here."
scene ep12_bellas52 with dissolve
$ renpy.pause()
scene ep12_bellas53 with dissolve
mc "Bella..."
scene ep12_bellas55 with dissolve
isa "I'm sorry. But I had to leave."
scene ep12_bellas54 with dissolve
js "Are you ok?"
scene ep12_bellas55 with dissolve
isa "I feel stupid and ashamed. This is not how I wanted to tell anyone about this."
isa "And definitely not when Derek was badly hurt."
scene ep12_bellas56 with dissolve
isa "Derek, how are you doing?"
scene ep12_bellas58 with dissolve
de "Nine and a half out of ten. Haha!"
scene ep12_bellas60 with dissolve
my "He's on painkillers, but he'll be fine."
my "Maybe we should end the night."
scene ep12_bellas57 with dissolve
isa "No. Please... That wouldn't make me feel better."
isa "Please, stay. Let's talk and eat. I bet you're all hungry."
isa "If Derek is ok with it, of course."
scene ep12_bellas59 with dissolve
de "I'm fine. No Champagne though!"
scene ep12_bellas60 with dissolve
my "The food is all ruined..."
stop music fadeout 3
scene ep12_bellas61 with dissolve
sa "Let's clean up and order pizza."

$ new_bio("Derek", "Derek lost the tip of his finger after playing with a sword.")
$ new_bio("Patrick", "Patrick showed up at Bella's place to check in on Derek after the accident.")

play music "music/ep12/licensed_music/track195.mp3"
scene ep12_bellas63 with wipeleft
$ renpy.pause()
scene ep12_bellas62 with dissolve
$ renpy.pause()
scene ep12_bellas64 with dissolve
$ renpy.pause()
scene ep12_bellas65 with dissolve
$ renpy.pause()
scene ep12_bellas66 with dissolve
isa "I'm so sorry, guys."
scene ep12_bellas70 with dissolve
de "If there's anyone who should feel sorry, it's me. I ruined our night, didn't I?"
scene ep12_bellas71 with dissolve
my "You guys don't have to keep apologizing. None of us blames you for anything that happened tonight."
scene ep12_bellas66 with dissolve
isa "I can sense that you are worried about me, and I don't want you to feel on edge around me."
isa "There will never be a good time to talk about this, but I don't want to end the story without telling you more."
scene ep12_bellas72 with dissolve
sa "You don't have to continue for our sake."
scene ep12_bellas67 with dissolve
isa "But I want to because it gets better."
scene ep12_bellas68 with dissolve
stop music fadeout 5
isa "As I told [name] in the car... After I had attempted to end my life, the hospital talked me into seeking help."
scene ep12_bellas69 with dissolve
$ renpy.pause()

play music "music/ep10/pineapple_pizza.mp3"
scene ep12_bellas73 with Dissolve(3)
$ renpy.pause()
scene ep12_bellas74 with dissolve
$ renpy.pause()
scene ep12_bellas75 with dissolve
wom "My son's addiction eventually got the upper hand of him."
wom "He couldn't shake the demon inside, and he ended up taking his life...b-by..."
wom "...by jumping off a building."
scene ep12_bellas76 with dissolve
wom "*{i}Sobs{/i}* If I had only seen the signs earlier, I would have been able to help him."
scene ep12_bellas77 with dissolve
than "I hear that you're blaming yourself for your son's death."
scene ep12_bellas75 with dissolve
wom "I do."
scene ep12_bellas78 with dissolve
than "That's the demon inside {b}you{/b} speaking."
than "This might be triggering for some of you, but I will say it."
scene ep12_bellas79 with dissolve
than "When someone who wants to commit suicide does it, and they don't let you know in any way, shape, or form..."
than "They aren't crying for help. They made a decision, and they went through with it."
scene ep12_bellas80 with dissolve
than "If you see the signs, or if they try to tell you about it, that's them calling out for help."
than "I've seen this pattern with many people in my group over the years."
than "And regardless of whether there was a cry for help, those who remain tend to blame themselves."
scene ep12_bellas78 with dissolve
than "As you know, even I blamed myself for the loss of a loved one."
scene ep12_bellas81 with dissolve
than "You might think it was your fault, it might have been your fault, or you found another way to blame yourself for it..."
than "Regardless of why you blame yourself... You have to find a way to forgive yourself."
scene ep12_bellas78 with dissolve
than "And that's the beauty of everyone here today. Together we can do that."
than "And the healing starts with sharing."
than "Does anyone else have a story they'd like to share?"
scene ep12_bellas82 with dissolve
$ renpy.pause()
scene ep12_bellas83 with dissolve
than "You don't have to share anything until you feel ready."
than "If no one else wants to share today, I'd like to introduce you to someone special..."
scene ep12_bellas84 with dissolve
than "Remember my story about Lana? This here is her younger sister, Jill."
scene ep12_bellas85 with dissolve
ji "Hi, everyone."
scene ep12_bellas86 with dissolve
than "Jill has lived through the same story as I told you last week, but from a different perspective."
than "Occasionally, she joins us to share her story and to listen to yours."
than "She's also a survivor like all of you."
scene ep12_bellas84 with dissolve
than "Jill? Would you like to tell us about your sister?"
scene ep12_bellas87 with dissolve
$ renpy.pause()
scene ep12_bellas88 with dissolve
ji "I've done this many times, but I always find it hard to start talking."
ji "Yet I feel that putting my feelings into words has helped me cope."
scene ep12_bellas89 with dissolve
ji "Today, it's easier for me to say that Lana is dead than it was before coming here."
ji "I used to choke up saying those words - well, sometimes I still do - but it has gotten easier with time."
scene ep12_bellas90 with dissolve
ji "Losing my sister... It has shaped my life."
scene ep12_bellas91 with dissolve
$ renpy.pause()
scene ep12_bellas92 with Dissolve(2)
$ renpy.pause()
scene ep12_bellas93 with dissolve
ji "Hi. I know I introduced myself to the group, but I'm Jill."
scene ep12_bellas96 with dissolve
isa "I'm sorry for your loss."
scene ep12_bellas94 with dissolve
ji "Thank you. And you are?"
scene ep12_bellas96 with dissolve
isa "Isabella."
scene ep12_bellas94 with dissolve
ji "Thank you, Isabella. And how are you doing? Is the group working out for you?"
scene ep12_bellas97 with dissolve
isa "I... I haven't opened up yet."
scene ep12_bellas95 with dissolve
ji "It's hard, isn't it?"
ji "What's the hardest part about it for you? For me, it was talking to strangers about someone I love."
ji "But after I had done it once, it felt liberating. Especially when I knew they all had similar stories."
scene ep12_bellas97 with dissolve
isa "I think it's like how you described it... Saying the words, that's the hardest part for me."
isa "And to admit what harm I have done to myself."
scene ep12_bellas98 with dissolve
$ renpy.pause()
scene ep12_bellas99 with dissolve
ji "If you feel that it's too hard for you to say those words, you don't have to feel pressured to do it."
ji "Take it at your own pace. They'll come out of you eventually."
ji "And trust me... It gets easier. Take it from someone who was inconsolable."
scene ep12_bellas101 with dissolve
ji "I'm glad that you're still here today, Isabella."
ji "And if you feel that it's easier to tell me in private, or someone else for that matter..."
ji "You can say so. I'm sure there are many here who would want to listen to you."
stop music fadeout 3
scene ep12_bellas100 with dissolve
$ renpy.pause()

play music "music/ep12/licensed_music/track195.mp3"
scene ep12_bellas102 with Dissolve(2)
$ renpy.pause()
scene ep12_bellas103 with dissolve
isa "And that's how Jill and I met."
scene ep12_bellas104 with dissolve
isa "Jill's help has been life-changing to me."
isa "It was thanks to Jill that I managed to turn everything around."
scene ep12_bellas105 with dissolve
ji "You have helped me, too, I hope you know. In so many ways."
scene ep12_bellas106 with dissolve
isa "It still hurts, but the sorrow is different today."
isa "I want to move on and not feel alone anymore. I think that's what James would have wanted too."
if branchIsabella:
    scene ep12_bellas107 with dissolve
    isa "But taking those steps has felt tremendously hard for me, even though I've gotten help with that from someone special at this table."
    scene ep12_bellas108 with dissolve
    if ep11_zoey_kiss != 2 and ep11_mg_party:
        sa "So, that's what has been going on between you two?"
    else:
        sa "So, have you two been together all this time?"
    scene ep12_bellas109 with dissolve
    mc "I...uh..."
    scene ep12_bellas107 with dissolve
    isa "It's hard to explain it. But also liberating to tell you all."
    isa "What [name] and I share is not something we flaunt or want out there - for many reasons."
    scene ep12_bellas111 with dissolve
    isa "But it's also something special. And I want you all to know that."
    isa "Maybe it doesn't make any sense from the outside, but for us it does."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_bellas109 with dissolve
        mc "(Fuck...)"
    scene ep12_bellas112 with dissolve
    my "That's the most important part, isn't it? That it makes sense to you."
    scene ep12_bellas113 with dissolve
    sa "Yeah. Screw what everyone else thinks."
scene ep12_bellas112 with dissolve
my "Thank you so much for sharing this with us. It couldn't have been easy."
scene ep12_bellas114 with dissolve
js "You're so strong, Bella. I can't even imagine what you've been through."
scene ep12_bellas115 with dissolve
$ renpy.pause()
scene ep12_bellas116 with dissolve
de "Well..."
de "We sure know how to throw a party."
scene ep12_bellas117 with dissolve
"*{i}Laughter{/i}*"
scene ep12_bellas118 with dissolve
isa "Thank you for still being here with me."
scene ep12_bellas119 with dissolve
sa "Of course. You're not alone, Bella."
scene ep12_bellas110 with dissolve
mc "Bella. I feel bad. I didn't know... Sorry if I pushed you to..."
scene ep12_bellas111 with dissolve
isa "You couldn't have known."

scene ep12_bellas118 with dissolve
isa "It's been a long evening..."
isa "How about opening some gifts and trying to laugh more?"
if not 1 in ep11_gift_list and not 2 in ep11_gift_list:
    scene ep12_bellas120 with dissolve
    mc "I didn't bring any gifts... I'm sorry. I've been short on money."
    scene ep12_bellas121 with dissolve
    sa "It's fine, [name]. It's not what's important, especially not after tonight."
    scene ep12_bellas122 with dissolve
    ji "We understand, [name]. Don't worry about it."
elif 0 in ep11_gift_list:
    scene ep12_bellas120 with dissolve
    mc "I feel bad... I didn't bring gifts for everyone..."
    mc "I'm sorry. I've been short on money, and I couldn't stretch the budget."
    scene ep12_bellas121 with dissolve
    sa "It's fine, [name]. It's not what's important. Especially not after tonight."
    scene ep12_bellas122 with dissolve
    ji "We understand, [name]. Don't worry about it."

scene ep12_bellas124 with dissolve
de "Hey, wanna laugh more?"
scene anim_derek_thumb_ep12 with dissolve
de "Look at what I can do."
scene ep12_bellas123 with dissolve
my "Derek... That's not funny."
stop music fadeout 3
scene anim_derek_thumb_ep12 with dissolve
de "I'm sure it won't be tomorrow, but for now it is."

$ new_bio("Isabella", "Isabella shared how she met Jill. Jill has helped Bella heal after the trauma.")
$ new_bio("Jill", "Jill attended group meetings hosted by Jonathan, where she met Bella.")

play music "music/ep11/oholynight.mp3"
queue music ["music/ep11/silent_night.mp3","music/ep11/oholynight.mp3"]
scene ep12_bellas125 with dissolve
$ renpy.pause()
scene ep12_bellas126 with dissolve
my "Oh, no..."
scene ep12_bellas127 with dissolve
de "What?"
scene ep12_bellas126 with dissolve
my "I just remembered what I got you. It's no longer appropriate..."
scene ep12_bellas128 with dissolve
de "Thanks, Sis. I could use a new pair."
scene ep12_bellas130 with dissolve
my "I'm sorry. Maybe I could cut off the finger and sew it back together, making it shorter."
scene ep12_bellas129 with dissolve
de "Don't worry about that. I could use some extra space in there."
de "The finger will be swollen and sore for a while."
scene ep12_bellas131 with dissolve
$ renpy.pause()

if ep11_gift_list[3] == 2:
    scene ep12_bellas132 with dissolve
    js "A gift card for my favorite clothing store? How did you know?"
    scene ep12_bellas133 with dissolve
    mc "I heard you mention it and saw some clothes I've seen you wear while window shopping."
    scene ep12_bellas132 with dissolve
    js "Thank you so much. I'll put it to good use, I swear."
elif ep11_gift_list[3] == 1:
    scene ep12_bellas132 with dissolve
    js "A gift card for makeup?"
    scene ep12_bellas133 with dissolve
    mc "I stink at buying the actual makeup and figured you would know what to get."
    scene ep12_bellas132 with dissolve
    js "Thank you so much. I'll make sure to get something special with this."
else:
    if branchMayaJosy:
        if 1 in ep11_gift_list or 2 in ep11_gift_list:
            scene ep12_bellas134 with dissolve
            mc "I'm sorry. I didn't get you anything."
            if ep11_josy_love > 0:
                scene ep12_bellas135 with dissolve
                js "Don't be sorry. I know how much you care."
            else:
                $ RPjosy -= 2
                scene ep12_bellas136 with dissolve
                js "It's ok..."

scene ep12_bellas137 with dissolve
js "Here you go."
scene ep12_bellas138 with dissolve
if ep9_jm_sad:
    mc "You got me something?"
    js "I did."
else:
    mc "For me?"
    js "Go ahead. Open it."
scene ep12_bellas139 with dissolve
mc "A necklace?"
js "You should wear more accessories. It's your style, but you don't know it."
mc "Thank you so much."
if (not branchZoey or wt_ep11_zoey_kiss_others) and branchMayaJosy:
    scene ep12_bellas140 with dissolve
    js "*{i}Smack{/i}*"
else:
    scene ep12_bellas141 with dissolve
    $ renpy.pause()

scene ep12_bellas142 with dissolve
de "[mc_de_up]. I got you something."

if ep11_gift_list[0] == 2:
    scene ep12_bellas143 with dissolve
    mc "Thanks! Here's one for you, too."
    scene ep12_bellas144 with dissolve
    de "Wow, that's a big one."
    scene ep12_bellas143 with dissolve
    mc "You deserve it."
    scene ep12_bellas144 with dissolve
    de "Now you're making me feel bad about mine, haha. It's not much. I saw it and thought about you."
elif ep11_gift_list[0] == 1:
    scene ep12_bellas145 with dissolve
    mc "Thanks! Here's one for you too."
    scene ep12_bellas146 with dissolve
    de "Thanks! Be prepared, though, mine is an inside joke. I saw it and thought about you."
else:
    scene ep12_bellas147 with dissolve
    mc "Thanks! You shouldn't have... I didn't get you anything."
    scene ep12_bellas148 with dissolve
    de "It's not much, so don't feel bad. I saw this one and thought about you."

scene ep12_bellas149 with dissolve
if ep11_gift_list[0] == 1:
    mc "Dude... Haha! No way!"
    scene ep12_bellas150 with dissolve
    de "Hahaha! No way!!!"
    de "HELLO!!!"
    mc "HAHA! HELLO!!!"
    scene ep12_bellas149 with dissolve
    mc "I love it!"
else:
    mc "Haha! HELLO!"
    mc "I love it!"
    if ep11_gift_list[0] == 2:
        scene ep12_bellas151 with dissolve
        de "Wow! A moose! This is amazing!"
        scene ep12_bellas152 with dissolve
        mc "It's not a-"
        mc "Ah... Fuck it. I thought it would fit somewhere in your room."
        scene ep12_bellas151 with dissolve
        de "No kidding. It will look so good on the wall! I love it!"

scene ep12_bellas153 with dissolve
de "Check the box. There's more in there."
if branchMayaJosy:
    scene ep12_bellas154 with dissolve
    mc "Really?"
    scene ep12_bellas155 with dissolve
    de "You should read it."
    scene ep12_bellas154 with dissolve
    mc "Hilarious..."
else:
    scene ep12_bellas156 with dissolve
    mc "Really? Granny porn?"
    scene ep12_bellas155 with dissolve
    de "I had to guess what kind of porn you liked."
    scene ep12_bellas157 with dissolve
    mc "To clue you in... This isn't it."

scene ep12_bellas155 with dissolve
de "Merry Christmas, [mc_de]."
scene ep12_bellas158 with dissolve
mc "Merry Christmas, bro."

scene ep12_bellas159 with dissolve
sa "[name]. This one is for you."
scene ep12_bellas160 with dissolve
mc "Oh? Thank you."
scene ep12_bellas159 with dissolve
sa "Haha, you should open it before you thank me."
if branchSage:
    scene ep12_bellas169 with dissolve
    mc "What's this? A calendar? Hey! That's you!"
    scene ep12_bellas165 with dissolve
    sa "It's a homemade calendar. Keep this one to yourself, ok?"
    scene ep12_bellas170 with dissolve
    mc "Wow..."
    sa "I know... The summer pictures are going to make you cum, haha."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_bellas168 with dissolve
        mc "..."
        scene ep12_bellas166 with dissolve
        sa "Are you ok?"
        scene ep12_bellas167 with dissolve
        mc "I'm sorry... I..."
        scene ep12_bellas166 with dissolve
        sa "Hey. I get it. It's a rough night for all of us."
        sa "Tomorrow will be better."
    else:
        scene ep12_bellas164 with dissolve
        mc "I can't find the words for this gift. It's amazing..."
        mc "You put so much effort into it."
        scene ep12_bellas165 with dissolve
        sa "Merry Christmas."
else:
    scene ep12_bellas161 with dissolve
    mc "Is this what I think it is?"
    sa "It's cologne! Smell it. I think it's you."
    scene ep12_bellas162 with dissolve
    mc "*{i}Sniffs{/i}* That's such a nice smell. Oh... Nice!"
    scene ep12_bellas163 with dissolve
    sa "*{i}Sniffs{/i}* Yep, that's totally you."
    scene ep12_bellas164 with dissolve
    mc "Thank you! I promise to use this one a lot."
    scene ep12_bellas165 with dissolve
    sa "Merry Christmas."

if ep11_gift_list[4] == 2:
    if (branchZoey and not wt_ep11_zoey_kiss_others) or not branchSage:
        scene ep12_bellas171 with dissolve
        mc "I had to ask Rusty for some help to get this one, but I hope you'll like it."
        scene ep12_bellas172 with dissolve
        sa "Single malt. Haha! Yep, you sure know me. I love, love, love this one."
        if branchSage:
            scene ep12_bellas174 with dissolve
        else:
            scene ep12_bellas175 with dissolve
        sa "*{i}Smack{/i}* Thank you!"
    else:
        scene ep12_bellas177 with dissolve
        mc "Here you go. I hope you'll like it."
        scene ep12_bellas178 with dissolve
        sa "Like it...?"
        sa "[name], I love this. It's a leaf..."
        scene ep12_bellas179 with dissolve
        mc "I figured you'd get what it meant."
        scene ep12_bellas176 with dissolve
        sa "*{i}Smack{/i}*"
        scene ep12_bellas180 with dissolve
        sa "Thank you! It's such a romantic gift..."
        scene ep12_bellas179 with dissolve
        mc "Merry Christmas, Sage."
elif ep11_gift_list[4] == 1:
    if (branchZoey and not wt_ep11_zoey_kiss_others) or not branchSage:
        scene ep12_bellas171 with dissolve
        mc "I had to ask Rusty for some help to get this one, but I hope you'll like it."
        scene ep12_bellas173 with dissolve
        sa "I will never say no to a bottle of whisky. Thank you, [name]."
        if branchSage:
            scene ep12_bellas174 with dissolve
        else:
            scene ep12_bellas175 with dissolve
        sa "*{i}Smack{/i}*"
    else:
        scene ep12_bellas177 with dissolve
        mc "Here you go. I hope you'll like it."
        scene ep12_bellas181 with dissolve
        sa "Wait... Are those guitar picks?"
        mc "And that's your own personal case of them. I thought they looked pretty, and I hope they make you want to play more."
        scene ep12_bellas176 with dissolve
        sa "*{i}Smack{/i}*"
        scene ep12_bellas182 with dissolve
        sa "Thank you! It will be fun playing with these."
        scene ep12_bellas183 with dissolve
        mc "Merry Christmas, Sage."
else:

    if branchSage:
        if 1 in ep11_gift_list or 2 in ep11_gift_list:
            scene ep12_bellas185 with dissolve
            mc "I'm sorry. I didn't get you anything."
            if ep11_sage_love > 0:
                scene ep12_bellas184 with dissolve
                sa "You didn't have to. You already give me so much daily."
            else:
                $ RPsage -= 2
                scene ep12_bellas186 with dissolve
                sa "It's ok. It's not like you promised that you would."
                $ new_bio("Sage", "Sage seemed disappointed that I didn't give her anything for Christmas.")


scene ep12_bellas187 with dissolve
my "For me!? You didn't have to get me anything."
scene ep12_bellas188 with dissolve
ji "Merry Christmas, Maya. I wish you a better next year."
scene ep12_bellas187 with dissolve
my "Merry Christmas."

scene ep12_bellas189 with dissolve
isa "How are you doing?"
scene ep12_bellas190 with dissolve
mc "Tonight has been...uh... Both terrible and nice. I'm not quite feeling myself."
scene ep12_bellas191 with dissolve
isa "Can I do something for you?"
scene ep12_bellas190 with dissolve
mc "I feel like I should ask you that."
scene ep12_bellas191 with dissolve
isa "I know what I told you tonight scared you."
scene ep12_bellas192 with dissolve
mc "Scared me? I..."
scene ep12_bellas193 with dissolve
isa "I can tell that it did."
scene ep12_bellas192 with dissolve
mc "If I had known this earlier... I would have acted differently around you."
mc "Like... Um... Being forward with you."
mc "I've been analyzing whether I said inappropriate things to you in the past."
scene ep12_bellas194 with dissolve
isa "[name], I want you to be yourself around me."
isa "You've said and done things that I know you wouldn't have if you had known about my past..."
scene ep12_bellas193 with dissolve
isa "But I'd hate it if you started walking on eggshells around me."
isa "So, keep being yourself. That's what you can do for me."
scene ep12_bellas192 with dissolve
mc "I still feel bad."
mc "Sure, I've gone through things, but I've never had to deal with this kind of pain in my life."
scene ep12_bellas194 with dissolve
isa "Neither had I when I was your age. There will be days in your life when you realize there's no guide to follow."
isa "You will feel lost and clueless."
scene ep12_bellas193 with dissolve
isa "Learning how to deal with it and to move on from there is a journey we all have to make at some point. Some face it sooner in life than others."
scene ep12_bellas195 with dissolve
isa "And I've made many mistakes on my journey. But I believe I'm finally heading in the right direction again."
scene ep12_bellas196 with dissolve
isa "Give me a hug."
scene ep12_bellas197 with dissolve
$ renpy.pause()
scene ep12_bellas198 with dissolve
$ renpy.pause()
scene ep12_bellas199 with dissolve
isa "I'm sorry for making you feel this way."
scene ep12_bellas198 with dissolve
mc "I'm sorry too."
if (branchZoey and not wt_ep11_zoey_kiss_others) and branchIsabella:
    mc "For a lot of things..."
else:
    mc "For everything you've had to go through."
if branchIsabella:
    scene ep12_bellas199 with dissolve
    isa "I know this has affected you..."
    isa "Does it change anything between us?"
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_bellas198 with dissolve
        mc "I'm in a bad spot, right now..."
        scene ep12_bellas200 with dissolve
        isa "So, it does..."
        scene ep12_bellas201 with dissolve
        mc "No, it doesn't. But there's something else that does..."
        mc "And I didn't want to bring that up tonight, and after hearing what you said, it was even harder to bring it up..."
        isa "..."
        scene ep12_bellas200 with dissolve
        isa "Then, let's not ruin this night further."
        scene ep12_bellas202 with dissolve
        mc "..."
    else:
        scene ep12_bellas198 with dissolve
        mc "I need time to digest it."
        scene ep12_bellas199 with dissolve
        isa "Of course. I understand."

scene ep12_bellas203 with dissolve
isa "Here... Merry Christmas, [name]."
if ep11_gift_list[1] == 0:
    scene ep12_bellas204 with dissolve
else:
    scene ep12_bellas205 with dissolve
mc "Merry Christmas to you too..."
scene ep12_bellas206 with dissolve
isa "I thought that brand would suit you. I hope I got the size right."
scene ep12_bellas207 with dissolve
mc "Yeah, you did. It's perfect."
mc "It's so soft... What a nice quality..."
scene ep12_bellas208 with dissolve
isa "I'm happy you like it."

if ep11_gift_list[1] == 2:
    scene ep12_bellas209 with dissolve
    isa "Oh, my... [name]... You shouldn't have."
    scene ep12_bellas210 with dissolve
    mc "Do you like them?"
    scene ep12_bellas209 with dissolve
    isa "You're not going to believe this, but I was going to buy these come spring."
    scene ep12_bellas210 with dissolve
    mc "You were?"
    scene ep12_bellas211 with dissolve
    isa "I wanted a new pair for summer. You've got great taste."
    scene ep12_bellas212 with dissolve
    mc "I'm happy you'll use them. They suit you!"
    scene ep12_bellas211 with dissolve
    isa "Thank you, [name]."
elif ep11_gift_list[1] == 1:
    scene ep12_bellas213 with dissolve
    isa "My favorite student, huh?"
    scene ep12_bellas214 with dissolve
    mc "And I mean that."
    scene ep12_bellas213 with dissolve
    if branchIsabella:
        isa "Haha... Thank you."
    else:
        isa "Haha... Not even close, but thank you."
    scene ep12_bellas214 with dissolve
    if branchIsabella:
        mc "I thought you might need one for work."
    else:
        mc "Ouch... Well, I thought you might need one for work."
    scene ep12_bellas213 with dissolve
    isa "How thoughtful."
    isa "It will bring a smile to my face daily."

show ep12_bellas215
if not persistent.ep12_cardcam6:
    show screen ep12_render_screen("cam6")
with dissolve
my "Merry Christmas, [name]."

if branchMayaJosy:
    show ep12_bellas216
    hide screen ep12_render_screen
    with dissolve
    mc "Um... Stockings?"
    scene ep12_bellas218 with dissolve
    my "Feel away, [name]. Feel away."
    scene ep12_bellas216 with dissolve
    mc "Funny..."
    scene ep12_bellas218 with dissolve
    my "Haha! I intend to wear those for you, in case you hadn't guessed."
    if not branchZoey or wt_ep11_zoey_kiss_others:
        scene ep12_bellas217 with dissolve
        mc "Feel away, [name]. Feel away."
    scene ep12_bellas219 with dissolve
    my "Look. There's more in the box."

show ep12_bellas220
hide screen ep12_render_screen
with dissolve
$ renpy.pause()
scene ep12_bellas219 with dissolve
if ep10_got_contracts:
    my "How do I thank someone who's given me everything?"
    my "I couldn't think of a way, so... I bought you some candy."
else:
    my "I didn't know how to thank you for everything you've done."
    my "So, I bought you some candy."
my "And I hope you can use the box for something special too."
scene ep12_bellas221 with dissolve
mc "Thank you, Maya. They look delicious."

if ep11_gift_list[4] == 2:
    scene ep12_bellas222 with dissolve
    mc "Merry Christmas."
    scene ep12_bellas223 with dissolve
    my "Aw! My favorite drink...and two movie tickets!?"
    scene ep12_bellas224 with dissolve
    mc "For any movie of your choice."
    scene ep12_bellas223 with dissolve
    my "Thank you, [name]. Now I can go to the movies twice."
    scene ep12_bellas224 with dissolve
    mc "Haha, or you could invite someone."
    scene ep12_bellas225 with dissolve
    my "Haha, I was joking."
elif ep11_gift_list[4] == 1:
    scene ep12_bellas222 with dissolve
    mc "Merry Christmas."
    scene ep12_bellas226 with dissolve
    mc "That coupon can be used to stream a movie of your choice."
    scene ep12_bellas227 with dissolve
    my "Thank you, [name]."
else:
    if branchMayaJosy:
        if 1 in ep11_gift_list or 2 in ep11_gift_list:
            scene ep12_bellas228 with dissolve
            mc "I don't have anything for you... I'm sorry."
            scene ep12_bellas229 with dissolve
            if ep10_got_contracts:
                my "As I said, you've already given me everything. I don't need any gifts."
            else:
                my "You've done so much for me, [name]. I don't need any gifts."
scene ep12_bellas230 with dissolve
$ renpy.pause()

scene ep12_bellas231 with dissolve
$ renpy.pause()
scene ep12_bellas232 with dissolve
ji "Merry Christmas, [name]. This one is for you."
if branchJill:
    ji "Now, this is part one of the gift. You'll have to wait for part two."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_bellas233 with dissolve
        mc "You shouldn't have..."
    else:
        scene ep12_bellas233 with dissolve
        mc "Two gifts? You're spoiling me."
    scene ep12_bellas234 with dissolve
    mc "Wait... This is..."
    ji "It's Lana's poster. I saw the glow in your eyes when you spotted it."
    ji "I figured you'd enjoy having it on your wall."
    scene ep12_bellas235 with dissolve
    mc "You have no idea..."
    scene ep12_bellas236 with dissolve
    ji "It's not much, but remember, there's a part two to this."
    scene ep12_bellas235 with dissolve
    mc "This was already too much. These are hard to come by today; they stopped printing them."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        mc "And it was your sister's poster too... It's too much..."
    else:
        mc "And it was your sister's poster too... This means a lot..."
else:
    scene ep12_bellas237 with dissolve
    mc "Acoustic guitar strings?"
    ji "I wasn't sure of what brand you usually get, but these are supposed to be high-quality."
    scene ep12_bellas238 with dissolve
    mc "Yeah, these are top-of-the-line. I've never bought this brand because they are too expensive."
    mc "Thank you so much!"
    scene ep12_bellas239 with dissolve
    ji "Enjoy them."
    scene ep12_bellas238 with dissolve
    mc "Oh, I will!"

if ep11_gift_list[2] == 2:
    mc "Hold on a second. I have something for you."
    scene ep12_bellas243 with dissolve
    mc "Merry Christmas, Jill."
    scene ep12_bellas244 with dissolve
    mc "I'm clueless when it comes to jewelry, but I saw this necklace and thought of you."
    ji "This is so sweet... It's beautiful."
    scene ep12_bellas245 with dissolve
    if branchJill:
        ji "I've never gotten jewelry from a guy before, and to get one from my boyfriend..."
        ji "It means a lot to me."
    else:
        ji "I've never gotten jewelry from a guy before."
    ji "Thank you, [name]."
    scene ep12_bellas246 with dissolve
    mc "You're welcome."
elif ep11_gift_list[2] == 1:
    mc "Hold on a second. I have something for you."
    scene ep12_bellas243 with dissolve
    mc "Merry Christmas, Jill."
    if branchJill:
        scene ep12_bellas249 with dissolve
        mc "It's for your camera. I figured you could use some more film for it."
        scene ep12_bellas248 with dissolve
        ji "That's so thoughtful. Thank you, [name]."
        scene ep12_bellas247 with dissolve
        ji "(I don't have the heart to tell him it's the wrong kind...)"
    else:
        scene ep12_bellas252 with dissolve
        mc "I hope you like chocolate truffles."
        scene ep12_bellas251 with dissolve
        ji "I do! Thank you, [name]. I'll make sure to enjoy these with some sparkling wine."
        scene ep12_bellas250 with dissolve
        mc "You're welcome."
else:
    if 1 in ep11_gift_list or 2 in ep11_gift_list:
        scene ep12_bellas240 with dissolve
        mc "Merry Christmas, Jill... I'm sorry, but I didn't get you anything."
        if branchJill:
            $ RPjill -= 3
            scene ep12_bellas242 with dissolve
            $ new_bio("Jill", "Jill seemed disappointed that I didn't prioritize getting her something for Christmas.")
        else:
            scene ep12_bellas241 with dissolve
        ji "It's ok, [name]. Don't feel bad."

play sound "sound_effects/bottle_clink.mp3"
scene ep12_bellas253 with dissolve
js "Thanks, everyone, for the gifts. Merry Christmas!"
scene ep12_bellas254 with dissolve
"Merry Christmas!"
mc "{i}And that was our weird family's Christmas.{/i}"
scene ep12_bellas255 with dissolve
stop music fadeout 3
if (branchZoey and not wt_ep11_zoey_kiss_others) and not branchAlone or ep4_toldDerekAboutJade:
    mc "{i}Derek said Christmas was all about traditions, but I don't think there will be another Christmas like this one.{/i}"
else:
    mc "{i}Dismemberment and dark revelations put aside... We had a nice time together.{/i}"

label ep12_war_label:
$ guideSuggestedPage = 228
hide screen new_phone_screen
play music "music/ep10/licensed_music/track149.mp3"
play sound "sound_effects/season3/police_radio.mp3"
scene ep12_war1 with fade
$ renpy.pause()
scene ep12_war2 with dissolve
$ renpy.pause()
scene ep12_war3 with dissolve
$ renpy.pause()
scene ep12_war4 with dissolve
cop1 "Alright, I checked with central... The caller said they saw people peddling drugs at this address."
scene ep12_war5 with dissolve
con "Who made the call?"
scene ep12_war6 with dissolve
cop1 "It was an anonymous tip from a concerned citizen."
scene ep12_war5 with dissolve
con "What else can you tell me about the call?"
scene ep12_war6 with dissolve
cop1 "Not much. It was a female - a young voice."
scene ep12_war7 with dissolve
con "A kid?"
scene ep12_war6 with dissolve
cop1 "A woman. You'll have to listen to the call; that's all I know about it."
scene ep12_war8 with dissolve
con "This isn't a busy street, especially not at this time."
con "And that place back there is hidden from the view of what little public there is."
scene ep12_war9 with dissolve
cop1 "What are you getting at?"
scene ep12_war8 with dissolve
con "Can you spot that something is going on back there from where you're standing?"
scene ep12_war10 with dissolve
$ renpy.pause()
scene ep12_war11 with dissolve
cop1 "No."
scene ep12_war12 with dissolve
con "And what does that tell you?"
scene ep12_war13 with dissolve
cop1 "You're the detective."
scene ep12_war12 with dissolve
con "Well, with a specific address and all... It tells me the caller knows more about it than they let on."
scene ep12_war13 with dissolve
cop1 "A squeaker?"
scene ep12_war12 with dissolve
con "Possibly."
play sound "sound_effects/interlude/bark.mp3"
scene ep12_war14 with dissolve
"*{i}Dog barking{/i}*"
scene ep12_war15 with dissolve
fc "Detective Conti. We're done in there. It's all yours."
scene ep12_war17 with dissolve
con "That was fast work."
scene ep12_war15 with dissolve
fc "More like pointless work. Sully got one whiff of the place and went crazy."
fc "The tip seems accurate. My best bet is that the safe is used to store the drugs, but it's most likely airtight because Sully didn't react to it."
scene ep12_war17 with dissolve
con "The locksmith is working on it."
con "What about the other rooms?"
scene ep12_war16 with dissolve
fc "Search them too. As I said, Sully wouldn't stop barking in there."
scene ep12_war18 with dissolve
$ renpy.pause()
scene ep12_war19 with dissolve
$ renpy.pause()
scene ep12_war20 with dissolve
cop2 "Detective. Take a look at what I found."
scene ep12_war21 with dissolve
con "Let me guess. It's the ledger."
scene ep12_war22 with dissolve
cop2 "Yeah, but it's written in code."
scene ep12_war23 with dissolve
con "Code? These are drug dealers, not World War 2 Germans."
scene ep12_war22 with dissolve
cop2 "Well, it is code. But I think I cracked it."
scene ep12_war24 with dissolve
cop2 "Look here..."
cop2 "Those letters are short for what drugs they sold, and that's the quantity."
scene ep12_war25 with dissolve
cop2 "And those nicknames: Fox, Wolf, Eagle, Ermine, Bulldog, Tiger..."
cop2 "They are the customers."
scene ep12_war26 with dissolve
con "..."
scene ep12_war27 with dissolve
con "No. That's not what it is."
scene ep12_war28 with dissolve
cop2 "I'm sorry, detective. But you're mistaken. Look..."
cop2 "The nicknames are recurring. Page after page. Wolf, Ermine, Tiger, Bulldog..."
scene ep12_war29 with dissolve
con "How many years have you been on the force?"
scene ep12_war30 with dissolve
cop2 "I'm closing in on four years."
scene ep12_war31 with dissolve
con "Then, I take it you've seen your fair share of drug dens."
scene ep12_war30 with dissolve
cop2 "Of course, sir. I've worked as a first responder on a couple of occasions."
scene ep12_war31 with dissolve
con "With your experience in mind..."
con "Tell me which kind of customer buys that amount every other week."
scene ep12_war32 with dissolve
$ renpy.pause()
scene ep12_war31 with dissolve
con "It would be a dead customer."
scene ep12_war33 with dissolve
cop2 "That's too much drugs for personal use... You're right."
scene ep12_war31 with dissolve
con "I tend to be."
scene ep12_war34 with dissolve
con "The names in that ledger are henchmen. And the guy we arrested is their boss."
scene ep12_war35 with dissolve
con "And that safe holds the motherlode."
con "And based on that ledger, it should be a sight to behold."
scene ep12_war36 with dissolve
cop2 "You're not saying they stored all their money and drugs in that safe, are you?"
cop2 "You can see it as soon as you walk inside."
show ep12_war37
if not persistent.ep12_cardcam7:
    show screen ep12_render_screen("cam7")
with dissolve
con "Look at how disgusting this place is. How do you live like this?"
con "Like I said, they are mere drug dealers. There's nothing genius about this. However, the nicknames are a cute touch."
play sound "sound_effects/season3/safe.mp3"
$ renpy.sound.play("sound_effects/season3/safe_door.mp3", channel="sfx2")
scene ep12_war38 with dissolve
lc "And Bob's your uncle."
show ep12_war39
hide screen ep12_render_screen
with dissolve
cop2 "Is that it? How anti-climactic..."
scene ep12_war40 with dissolve
con "Hm..."
scene ep12_war41 with dissolve
cop2 "What did you call it again? The motherlode?"
scene ep12_war42 with dissolve
con "Alright there, Enigma machine... I never said we arrested a kingpin. As it appears, we simply arrested a middleman."
con "If those packages contain what I suspect, it's enough for a conviction."
con "And maybe we can find out who the big fish is."
scene ep12_war43 with dissolve
cop2 "*{i}Mumbles{/i}* Mr. Right, huh?"
scene ep12_war44 with dissolve
cop2 "Detective? What about this?"
scene ep12_war45 with dissolve
con "That's evidence. Bag it and leave it for the interrogation. And don't touch any more evidence without wearing gloves."
con "*{i}Mumbles{/i}* Four years on the force..."
scene ep12_war46 with dissolve
$ renpy.pause()
scene ep12_war52 with Dissolve(3)
$ renpy.pause()
scene ep12_war53 with dissolve
$ renpy.pause()
scene ep12_war47 with dissolve
$ renpy.pause()
scene ep12_war85 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/car_pass2.mp3"
scene ep12_war86 with dissolve
$ renpy.pause()
scene ep12_war48 with dissolve
$ renpy.pause()
scene ep12_war87 with dissolve
$ renpy.pause()
scene ep12_war49 with dissolve
$ renpy.pause()
scene ep12_war54 with dissolve
$ renpy.pause()
if ep11_quinn_question[0] and ep11_quinn_question[1]:
    scene ep12_war55 with dissolve
    $ renpy.pause()
    scene ep12_war58 with dissolve
    $ renpy.pause()
    scene ep12_war59 with dissolve
    mc "Quinn?"
    scene ep12_war60 with dissolve
    qu "Did I wake you up?"
    scene ep12_war59 with dissolve
    mc "Yeah, but it's fine. What's wrong?"
    scene ep12_war60 with dissolve
    qu "Nothing is wrong. I...needed to hear your voice."
    scene ep12_war61 with dissolve
    mc "I'm right here."
    scene ep12_war62 with dissolve
    qu "How was your night?"
    scene ep12_war61 with dissolve
    mc "Um... I was at a Christmas party with my friends."
    mc "It was...an eventful evening. Derek chopped a part of his finger off with a sword."
    scene ep12_war63 with dissolve
    qu "Whoa... Is he ok?"
    scene ep12_war64 with dissolve
    mc "After the trip to the hospital, yeah. They closed the wound, but he lost his fingertip for good."
    scene ep12_war63 with dissolve
    qu "Shit. That must suck."
    scene ep12_war64 with dissolve
    mc "Yeah. He was high on painkillers for the rest of the night. We'll see how he feels tomorrow."
    scene ep12_war65 with dissolve
    qu "I haven't talked to him much, but he's a good guy."
    qu "I remember how mad he got at me during Hell Week, when we pranked him."
    scene ep12_war61 with dissolve
    mc "Which prank?"
    scene ep12_war62 with dissolve
    qu "The same one we pulled on you. Tommy sent him to get underwear from us, and we made him strip nude before we threw his ass out on the streets."
    scene ep12_war61 with dissolve
    mc "Oh, that one. Yeah... Honestly, he's still not over it. Haha..."
    scene ep12_war62 with dissolve
    qu "I guess it rubbed him the wrong way."
    scene ep12_war61 with dissolve
    mc "Kinda. But he doesn't talk badly about you."
    scene ep12_war65 with dissolve
    qu "Wouldn't be anything I haven't heard before."
    scene ep12_war61 with dissolve
    mc "Are you sure you're all right?"
    scene ep12_war62 with dissolve
    qu "I feel better now."
    scene ep12_war66 with dissolve
    mc "Listen, I thought about our last talk..."
    scene ep12_war65 with dissolve
    qu "Yeah?"
    scene ep12_war66 with dissolve
    mc "I suppose there's nothing I can say to make you change your mind..."
    mc "About the revenge and everything... Maybe there's another way to go."
    scene ep12_war67 with dissolve
    qu "You're a little late for that."
    scene ep12_war66 with dissolve
    mc "What do you mean? Did you do something?"
    scene ep12_war67 with dissolve
    qu "Doing something. Tonight."
    scene ep12_war66 with dissolve
    mc "Did you call because you needed me? I'll come."
    scene ep12_war68 with dissolve
    qu "No. Like I said, I needed to hear your voice."
    scene ep12_war66 with dissolve
    mc "I won't be able to sleep now. Where are you?"
    scene ep12_war67 with dissolve
    qu "Don't worry, [name]. It won't be dangerous. I'm cautious."
    scene ep12_war69 with dissolve
    mc "Can you at least tell me what you're up to?"
    scene ep12_war70 with dissolve
    qu "Not over the phone."
    scene ep12_war69 with dissolve
    mc "Can you call me when you're done, or give me a time frame when I should start worrying?"
    scene ep12_war70 with dissolve
    qu "Usually, I can't stand it when someone treats me like this."
    qu "The whole coddling shit and feeling the need to protect me... I hate it."
    scene ep12_war61 with dissolve
    mc "I can't help it. That's how I am."
    scene ep12_war71 with dissolve
    qu "I said usually..."
    qu "I hate to admit it, but... It does feel nice coming from you."
    scene ep12_war61 with dissolve
    mc "I do care."
    scene ep12_war71 with dissolve
    qu "I know. And for a long time, I didn't want you to."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_war61 with dissolve
        mc "Fuck... Quinn..."
        scene ep12_war63 with dissolve
        qu "What?"
        scene ep12_war66 with dissolve
        mc "There's something I have to tell you..."
        mc "I'm getting back together with my ex."
        scene ep12_war72 with dissolve
        $ renpy.pause()
        scene ep12_war73 with dissolve
        mc "We recently reconnected, and I have unresolved feelings for her."
        mc "I didn't want to tell you like this, and after our last talk, it didn't feel like I would have to."
        scene ep12_war74 with dissolve
        mc "I felt you trusted me and all, but lately you haven't around much, and that put me off."
        mc "I'm sorry."
        scene ep12_war72 with dissolve
        $ renpy.pause()
        scene ep12_war73 with dissolve
        mc "Quinn? Are you still there?"
        scene ep12_war75 with dissolve
        qu "I'm sorry for treating you like that."
        scene ep12_war72 with dissolve
        mc "I know you have your reasons."
        scene ep12_war75 with dissolve
        qu "It's for the best anyway."
        qu "I'd only get you into trouble."
        scene ep12_war73 with dissolve
        mc "I'm not cut out for that, yeah?"
        scene ep12_war75 with dissolve
        qu "You're not."
        scene ep12_war74 with dissolve
        $ renpy.pause()
        scene ep12_war75 with dissolve
        qu "You should go back to sleep."
        scene ep12_war73 with dissolve
        mc "Stay safe..."
        scene ep12_war75 with dissolve
        qu "I will. Good night."
        scene ep12_war76 with dissolve
        $ renpy.pause()
        $ new_bio("Quinn", "Quinn called me late at night because she needed to hear my voice. I told her about getting back together with Zoey. It felt like she was hurt from hearing that.")
    else:
        scene ep12_war61 with dissolve
        mc "But now you do."
        scene ep12_war62 with dissolve
        qu "Don't push it."
        scene ep12_war61 with dissolve
        mc "If you were at home right now, I'd come over and kiss you."
        scene ep12_war62 with dissolve
        qu "Well, I'm not. I'll be back tomorrow."
        scene ep12_war77 with dissolve
        mc "I've missed you."
        scene ep12_war78 with dissolve
        qu "Fucking broccoli, dude."
        scene ep12_war77 with dissolve
        mc "It's not in public. Hell, it's not even face-to-face."
        scene ep12_war78 with dissolve
        qu "I'm not saying it back."
        scene ep12_war77 with dissolve
        mc "But you did too... Didn't you?"
        scene ep12_war78 with dissolve
        qu "What do you think?"
        scene ep12_war79 with dissolve
        mc "I knew it."
        scene ep12_war80 with dissolve
        qu "You should go back to sleep."
        scene ep12_war81 with dissolve
        mc "Send me something after you're done with whatever you're doing."
        scene ep12_war80 with dissolve
        qu "I will. Good night."
        scene ep12_war82 with dissolve
        $ renpy.pause()
        $ new_bio("Quinn", "Quinn called me late at night because she needed to hear my voice. She admitted that she missed me in her own way.")
scene ep12_war57 with dissolve
$ renpy.pause()
scene ep12_war84 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/timer.mp3"
scene ep12_war83 with dissolve
"*{i}Alarm beeps{/i}*"

scene ep12_war50 with dissolve
$ renpy.pause()
scene ep12_war88 with dissolve
$ renpy.pause()
scene ep12_war51 with dissolve
$ renpy.pause()

scene ep12_war89 with dissolve
$ renpy.pause()
scene ep12_war90 with dissolve
$ renpy.pause()
scene ep12_war91 with dissolve
$ renpy.pause()
scene ep12_war92 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/crowbar.mp3"
scene ep12_war93 with dissolve
$ renpy.pause()
scene ep12_war94 with dissolve
$ renpy.pause()
scene ep12_war95 with dissolve
$ renpy.pause()
play sound "sound_effects/switch.mp3"
scene ep12_war96 with dissolve
$ renpy.pause()
scene ep12_war97 with dissolve
$ renpy.pause()
scene ep12_war98 with dissolve
$ renpy.pause()
scene ep12_war99 with dissolve
rx "{i}I outsmarted you. By dangling something obvious and valuable in front of you...{/i}"
rx "{i}...you didn't see what I tried to hide.{/i}"
scene ep12_war100 with dissolve
rx "{i}You've seen Daddy's safe, right? I wanna show you something.{/i}"
rx "{i}And not a word to your mom, ok?{/i}"
scene ep12_war101 with dissolve
$ renpy.pause()
scene ep12_war102 with dissolve
$ renpy.pause()
scene ep12_war103 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/cardboard_kick.mp3"
scene ep12_war104 with hpunch
$ renpy.pause()
play sound "sound_effects/season3/rug.mp3"
scene ep12_war105 with dissolve
$ renpy.pause()
scene ep12_war106 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/door_squeek.mp3"
scene ep12_war107 with dissolve
$ renpy.pause()
scene ep12_war108 with dissolve
rx "{i}Remember when you were born. Easy, huh?{/i}"
scene ep12_war109 with dissolve
rx "{i}My precious is guarding what's precious to me.{/i}"
scene ep12_war110 with dissolve
$ renpy.pause()
scene ep12_war111 with dissolve
$ renpy.pause()
scene ep12_war112 with dissolve
$ renpy.pause()
scene ep12_war113 with dissolve
$ renpy.pause()
scene ep12_war114 with dissolve
$ renpy.pause()
scene ep12_war115 with dissolve
dl1 "Yeah, they got the decoy safe."
scene ep12_war116 with dissolve
dl1 "Well, it was supposed to be a decoy safe, but Buddy got lazy at times. Beats me how much drugs and money he kept in it."
dl1 "Yeah, they probably got the ledger too."
dl1 "Shit, I don't know! I think he kept it in there when he wasn't using it."
scene ep12_war117 with dissolve
dl1 "My money is on a snitch."
dl1 "I have my suspicions."
scene ep12_war118 with dissolve
dl1 "It could be one of the dealers getting revenge."
scene ep12_war119 with dissolve
dl1 "Well, one fucker overcharged and pocketed the money, and that's because the other one started it and passed the idea on."
dl1 "We straightened him out, but the dude holds grudges."
scene ep12_war120 with dissolve
dl1 "And get this... He ratted the other one out for doing the same thing he did. Snitching is his style."
dl1 "It wouldn't surprise me if he snitched on Buddy, too. Buddy cut his face up with a kitchen knife."
scene ep12_war121 with dissolve
dl1 "I'll look into it."
dl1 "Yeah. Hold on. I'll check the main safe."
scene ep12_war122 with dissolve
$ renpy.pause()
scene ep12_war123 with dissolve
dl1 "Fuck! They got this one, too."
scene ep12_war124 with dissolve
dl1 "It's cleaned out. They searched everywhere. Fucking pigs!"
dl1 "Yeah. Buddy is in real trouble now. He could be a liability, but I don't think he would talk. Well, maybe he would, if he wanted to save his ass."
dl1 "No, no! Fuck him! I ain't loyal to him."
dl1 "What do you want me to do? Name it."
scene ep12_war125 with dissolve
dl1 "Yeah. Got it. I'll let you know what I find out."
dl1 "What are you gonna do about Buddy?"
dl1 "Hello?"
scene ep12_war126 with dissolve
dl1 "Fuck..."
scene ep12_war127 with dissolve
$ renpy.pause()
scene ep12_war128 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_war129 with dissolve
$ renpy.pause()

jump ep12_freeroam_room1_label
label ep12_fr1_end_label:
if (branchZoey and not wt_ep11_zoey_kiss_others) and branchJill:
    jump ep12_jill_break_label
if branchMayaJosy:
    if branchZoey and not wt_ep11_zoey_kiss_others:
        jump ep12_jm_break_label
    else:
        jump ep12_jm_z_label
elif branchJill:
    jump ep12_jill_room_label
label ep12_bd_label:
hide screen new_phone_screen
play music "music/ep12/licensed_music/track198.mp3"
play sound "sound_effects/door_lock.mp3"
scene ep12_bd1 with wiperight
$ renpy.pause()
play sound "sound_effects/season3/door_open.mp3"
scene ep12_bd2 with dissolve
$ renpy.pause()
play sound "sound_effects/door_close.mp3"
scene ep12_bd3 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/chair_move.mp3"
scene ep12_bd4 with dissolve
$ renpy.pause()
scene ep12_bd5 with dissolve
con "Good morning. I'm Detective Conti. Can you state your name for the record, please?"
scene ep12_bd6 with dissolve
bd "..."
scene ep12_bd7 with dissolve
bd "Buddy."
scene ep12_bd8 with dissolve
con "I meant your full legal name."
scene ep12_bd6 with dissolve
bd "..."
scene ep12_bd8 with dissolve
con "Don't be difficult with me. I've had a long night."
con "Besides, I already know most things about you."
play sound "sound_effects/interlude/page_turn.mp3"
scene ep12_bd9 with dissolve
con "Robert Dabbs. Also known as Robert Bobby Dabbs and Buddy."
con "Born in Minnesota. Spent 3 years in juvie due to substance abuse."
con "During your time in juvie, you were accused of poisoning a fellow offender with fentanyl, but didn't face any charges because of a lack of evidence."
scene ep12_bd10 with dissolve
con "A couple of misdemeanors along the road and a big blank space on your record since."
con "Hell, your last known address is still in Minnesota, and now you resurface here."
scene ep12_bd11 with dissolve
con "Tell me, Robert. What have you been up to lately?"
scene ep12_bd12 with dissolve
bd "You seem to be the man with all the answers. You tell me."
scene ep12_bd11 with dissolve
con "So, you're living on Easy Street these days?"
scene ep12_bd12 with dissolve
bd "I hang out there."
scene ep12_bd13 with dissolve
con "Come on. You do more than hang out there."
scene ep12_bd14 with dissolve
bd "You lost me."
scene ep12_bd13 with dissolve
con "We found your fingerprints all over the place."
scene ep12_bd14 with dissolve
bd "What can I tell you?"
play sound "sound_effects/interlude/page_turn.mp3"
scene ep12_bd15 with dissolve
con "You can tell me about the drugs we found in the safe. They have your fingerprints on them, too."
con "Or the illegal firearm. Or the money. There was a lot of cash in that safe."
scene ep12_bd16 with dissolve
$ renpy.pause()
scene ep12_bd17 with dissolve
$ renpy.pause()
play sound "sound_effects/interlude/page_turn.mp3"
scene ep12_bd18 with dissolve
con "Or this. This is yours, too, yeah?"
scene ep12_bd19 with dissolve
con "Bulldog. Fox. Tiger. Ermine. Eagle..."
con "I'm trying to figure out what these scribbles mean. Care to enlighten me?"
scene ep12_bd20 with dissolve
bd "I'm an animal lover."
scene ep12_bd21 with dissolve
con "Haha! You're a funny guy."
scene ep12_bd22 with dissolve
con "I wonder, will you be the funny guy in prison, too?"
con "You have to be really funny to survive in there."
scene ep12_bd23 with dissolve
con "We both know what this ledger is. And we can link you to everything we found."
scene ep12_bd22 with dissolve
con "You're going away, Robert, for a long time."
con "And prison isn't like juvie either."
scene ep12_bd23 with dissolve
con "If you keep being difficult with me, it will be reflected in your sentence."
con "But if you cooperate and tell me where you got the drugs from, maybe we can work something out."
con "It's all up to you."
scene ep12_bd24 with dissolve
bd "I want a lawyer."
stop music fadeout 3
scene ep12_bd22 with dissolve
con "Now, that's the first smart thing you've said so far."

if branchAlone and (ep11_nicole_dating or ep11_rolling):
    jump ep12_prl_label
else:
    jump ep12_qm_label
label ep12_prl_label:
play music "music/ep12/licensed_music/track201.mp3"
scene ep12_prl1 with wipeleft
tan "See you on Thursday!"
scene ep12_prl2 with dissolve
nic "Bye, Tania."
if ep11_nicole_dating:
    if ep11_nicole_over_lily and not ep11_rolling:
        scene ep12_prl3 with dissolve
        $ renpy.pause()
        scene ep12_prl10 with dissolve
        nic "Are you doing ok?"
        scene ep12_prl4 with dissolve
        ly "Yeah."
        scene ep12_prl10 with dissolve
        nic "Are you sure? You seem off tonight."
        scene ep12_prl4 with dissolve
        ly "Why are you overly concerned? I said I was fine."
        scene ep12_prl10 with dissolve
        nic "I'm just making sure, considering..."
        scene ep12_prl5 with dissolve
        ly "Give it a rest. [name] and I had fun together; there was nothing more to it."
        ly "If you think that he's boyfriend material...you should go for it."
        scene ep12_prl11 with dissolve
        nic "I'm trying to find out if he is boyfriend material, but I couldn't do that if you two were together."
        scene ep12_prl5 with dissolve
        ly "We weren't together. We were having sex, it's not the same thing."
        scene ep12_prl11 with dissolve
        nic "Yeah, but I don't want there to be any bad blood between us."
        scene ep12_prl6 with dissolve
        ly "Look. What I think doesn't even matter. He chose you, didn't he?"
        scene ep12_prl11 with dissolve
        nic "It still matters how you feel."
        scene ep12_prl6 with dissolve
        ly "Nah, it doesn't. In fact, you did me a favor."
        scene ep12_prl12 with dissolve
        nic "What's that supposed to mean?"
        scene ep12_prl7 with dissolve
        ly "You took him off my hands before he got clingy."
        ly "I never wanted to date him because I couldn't date someone and work here."
        ly "But obviously, you can."
        scene ep12_prl11 with dissolve
        nic "Work is work. What you do in private is a different thing."
        scene ep12_prl7 with dissolve
        ly "Well, I don't think I can grind on horny dudes and like [name] at the same time. That's not me."
        scene ep12_prl13 with dissolve
        nic "Do you like him? \"Like him\", like him?"
        scene ep12_prl7 with dissolve
        ly "I'm not in love with him, if that's where you're getting at."
        ly "I enjoyed his company."
        scene ep12_prl14 with dissolve
        $ renpy.pause()
        scene ep12_prl7 with dissolve
        ly "Don't feel bad."
        stop music fadeout 3
        scene ep12_prl8 with dissolve
        $ renpy.pause()
    else:
        scene ep12_prl22 with dissolve
        nic "I need a vacation..."
        scene ep12_prl16 with dissolve
        ly "Yeah? Where are we going?"
        scene ep12_prl23 with dissolve
        nic "If I could choose, I'd stay in bed at home for a week and catch up on some sleep."
        scene ep12_prl17 with dissolve
        ly "That's not a vacation; that's just sad. Is this what life after 30 has to offer?"
        scene ep12_prl23 with dissolve
        nic "It's what life after having a child offers."
        scene ep12_prl17 with dissolve
        ly "Good thing I'm not doing that."
        scene ep12_prl24 with dissolve
        nic "Ever?"
        scene ep12_prl18 with dissolve
        ly "Eh... It's not high on my to-do list; let's leave it at that."
        ly "Besides, fat strippers aren't popular."
        ly "And you're one of the lucky few who managed a pregnancy without having it ruin you."
        scene ep12_prl24 with dissolve
        nic "What a shallow take."
        scene ep12_prl18 with dissolve
        ly "Yeah, see? I'm way too immature to be a mom."
        scene ep12_prl23 with dissolve
        nic "That's what I thought when I was your age, too - just saying."
        scene ep12_prl19 with dissolve
        ly "What's your holiday going to be like this year?"
        scene ep12_prl23 with dissolve
        nic "I got Marvin for Christmas, and I hope to find free time to spend with [name] on top of that."
        scene ep12_prl19 with dissolve
        ly "Has [name] met your kid?"
        scene ep12_prl25 with dissolve
        nic "No, he hasn't."
        scene ep12_prl19 with dissolve
        ly "Will he?"
        scene ep12_prl24 with dissolve
        nic "We'll see. I think it would scare him away."
        scene ep12_prl20 with dissolve
        ly "Because of his age?"
        scene ep12_prl25 with dissolve
        nic "The age gap isn't that big of an issue to me."
        scene ep12_prl20 with dissolve
        ly "It's not? Because without thinking, I can't tell if [name]'s age is closer to yours or Marvin's."
        scene ep12_prl26 with dissolve
        nic "Don't put it like that. Stop it!"
        scene ep12_prl20 with dissolve
        ly "So... It is an issue after all."
        scene ep12_prl24 with dissolve
        nic "Not when we get older."
        scene ep12_prl19 with dissolve
        ly "Yeah, but what about now?"
        scene ep12_prl23 with dissolve
        nic "I feel [name] is mature for his age."
        scene ep12_prl18 with dissolve
        ly "The guy who passed out naked in the park from a blunt is mature?"
        scene ep12_prl23 with dissolve
        nic "We were high and naked in the park, too."
        scene ep12_prl18 with dissolve
        ly "Yeah, and as we already established, I'm not that mature."
        scene ep12_prl23 with dissolve
        nic "Still, I feel he is mature. On our date, we had a long and deep talk."
        nic "Sure, he's a frat guy and goofs off at parties, but that's his playful side."
        nic "There's another side to him that I've seen."
        scene ep12_prl21 with dissolve
        ly "Hey, you're the one dating him. You don't have to convince me."
        ly "But you might have to convince Luke that you haven't lost it."
        scene ep12_prl24 with dissolve
        nic "Because I'm dating [name]?"
        scene ep12_prl21 with dissolve
        ly "All I'm saying is, hold off on introducing [name] to Marvin and you'll be good."
        stop music fadeout 3
        scene ep12_prl25 with dissolve
        $ renpy.pause()
if ep11_rolling:
    scene ep12_prl3 with dissolve
    $ renpy.pause()
    scene ep12_prl10 with dissolve
    nic "Bad night?"
    scene ep12_prl4 with dissolve
    ly "It was alright."
    scene ep12_prl10 with dissolve
    nic "Then why the sad face?"
    scene ep12_prl4 with dissolve
    ly "Blame [name]... Everything is his fault."
    if ep10_date_nicole and not ep10_cancel_date_nicole:
        scene ep12_prl10 with dissolve
        nic "This doesn't have anything to do with me, right?"
        scene ep12_prl4 with dissolve
        ly "Hm? No. It's not because of you."
        scene ep12_prl11 with dissolve
        nic "Then what did he do?"
    else:
        scene ep12_prl11 with dissolve
        nic "What did he do?"
    scene ep12_prl7 with dissolve
    ly "He got into my head."
    scene ep12_prl11 with dissolve
    nic "How?"
    scene ep12_prl7 with dissolve
    ly "For the first time since I started working here and met you girls, I felt I was doing something wrong tonight."
    ly "You know that feeling, yeah?"
    scene ep12_prl15 with dissolve
    nic "Sure do. I hated looking at my face in these mirrors for a long time."
    nic "What did [name] say? Did he slam you for stripping?"
    scene ep12_prl9 with dissolve
    ly "He hasn't said a thing about it."
    scene ep12_prl15 with dissolve
    nic "Then what did he say?"
    scene ep12_prl9 with dissolve
    ly "It's not a single thing he said. It's more..."
    ly "It doesn't feel like we are rolling anymore. It feels like we're dating."
    scene ep12_prl13 with dissolve
    nic "And you don't want that."
    scene ep12_prl7 with dissolve
    ly "I can't date him and work here. I can't do it."
    scene ep12_prl11 with dissolve
    nic "Why not? This is just a job. You have your work life and your private life. If [name] is cool with it and you want to date him, go for it."
    scene ep12_prl7 with dissolve
    ly "Honestly, I think it's more than dating. And it snuck up on me from nowhere."
    scene ep12_prl13 with dissolve
    nic "From his or your side?"
    if ep11_lily_want_more and ep11_follow_quinn and not ep10_lily_english:
        scene ep12_prl7 with dissolve
        ly "Mostly his. There's tension between us."
    elif ep11_lily_want_more:
        scene ep12_prl9 with dissolve
        ly "Both. There's tension between us."
    else:
        scene ep12_prl9 with dissolve
        ly "Maybe just mine... It's not a lot, but there's tension between us."
    scene ep12_prl13 with dissolve
    if ep10_date_nicole and not ep10_cancel_date_nicole:
        nic "He told me he didn't want to stop being with you. I think he's into you."
    nic "Is it something you want to explore?"
    scene ep12_prl9 with dissolve
    ly "Like, I said... I can't work here and do that."
    scene ep12_prl11 with dissolve
    nic "Is it one or the other with you? There's no way to try it?"
    scene ep12_prl7 with dissolve
    ly "I can't do both."
    scene ep12_prl13 with dissolve
    nic "Then what will you do?"
    stop music fadeout 3
    scene ep12_prl8 with dissolve
    $ renpy.pause()

label ep12_qm_label:
play music "music/ep12/licensed_music/track193.mp3"
scene ep12_qm1 with wipeleft
$ renpy.pause()
scene ep12_qm2 with dissolve
$ renpy.pause()
scene ep12_qm3 with dissolve
$ renpy.pause()
scene ep12_qm4 with dissolve
qu "*{i}Sigh{/i}*"
scene ep12_qm5 with dissolve
qu "Mick? It's me. What the hell is going on?"
qu "I went to Buddy's, and there was police tape by the entrance. I'm freaking out here."
scene ep12_qm6 with dissolve
qu "I got rid of it as fast as I could. If the cops had his phone, they'd have my number and yours, too."
scene ep12_qm7 with dissolve
qu "What about Buddy? Did he get out ok?"
qu "In jail? No fucking way..."
scene ep12_qm6 with dissolve
qu "And what about the drop off? I've got customers waiting."
qu "What the fuck!? No, I know nothing about it."
scene ep12_qm5 with dissolve
qu "What the hell are you accusing me of?"
qu "Dude, why would I self-snitch? I gave all my money to Buddy; I have to make it back. I'm fucking broke here..."
scene ep12_qm8 with dissolve
qu "I heard that Vinny threatened one of my customers again. Have you asked him?"
qu "Yeah, it was recently. He forced her to buy from him again at a higher price."
qu "She said he looked like shit, with a scar and bruises. Did you do that to him?"
scene ep12_qm9 with dissolve
qu "Mick!? What about the drop off?"
qu "You're not doing this to me! I need that money! Mick!?"
stop music fadeout 3
scene ep12_qm10 with dissolve
$ renpy.pause()
scene ep12_qm11 with dissolve
$ renpy.pause()

label ep12_djocks_label:
play music "music/ep1/food_chain_short.mp3"
play sound "sound_effects/shove.mp3"
scene ep12_djocks1 with hpunch
an "AARGH!"
de "Hey! What the hell!? Get off me!"
play sound "sound_effects/hit.mp3"
scene ep12_djocks2 with hpunch
an "Do you think you can fuck my girlfriend and get away with it!?"
scene ep12_djocks3 with dissolve
ash "Anthony!!! No!"
play sound "sound_effects/hit.mp3"
scene ep12_djocks4 with hpunch
an "I'll fucking kill you!!!"
de "AH! My hand!"
play sound "sound_effects/shove.mp3"
scene ep12_djocks5 with hpunch
sec "Break this off!"
ph "What are you two doing? Come to your senses."
scene ep12_djocks6 with dissolve
ash "Derek? Are you ok? What happened to your hand? It's bleeding."
scene ep12_djocks7 with dissolve
de "What's going on? Anthony just jumped me."
scene ep12_djocks8 with dissolve
an "Oh, shut up! You know what you did!"
an "You fucked my girl! And I have the pictures to show it!"
scene ep12_djocks9 with dissolve
ph "If you don't calm down, Anthony, you'll face expulsion."
ph "Whatever the dispute is, settle it with words."
scene ep12_djocks8 with dissolve
an "But he-!"
scene ep12_djocks9 with dissolve
ph "Walk it off, Anthony. I will report this to the disciplinary committee. You're treading dangerous waters."
stop music fadeout 3
scene ep12_djocks10 with dissolve
ph "Move along, everyone. Go to your classes."
play music "music/ep9/getting_closure.mp3"
scene ep12_djocks11 with dissolve
ph "Are you hurt? Do you need medical attention? You appear to be bleeding."
scene ep12_djocks12 with dissolve
de "I got stitches yesterday, after I cut the tip of my finger off."
scene ep12_djocks14 with dissolve
ash "Oh my God... Derek..."
scene ep12_djocks15 with dissolve
de "I'll be fine. I need to check on it."
scene ep12_djocks11 with dissolve
ph "Are you sure?"
scene ep12_djocks12 with dissolve
de "Yeah."
scene ep12_djocks11 with dissolve
ph "After I talk to the committee, you'll be summoned to a meeting about this."
scene ep12_djocks13 with dissolve
ash "He didn't do anything! Anthony started whaling on him."
scene ep12_djocks11 with dissolve
ph "I saw, but they will still want to hear what happened from him."
scene ep12_djocks12 with dissolve
de "I have to go to the bathroom."
scene ep12_djocks16 with dissolve
ash "Derek, wait. Let me help you."
scene ep12_djocks17 with dissolve
ash "Did you really cut off a part of your finger?"
scene ep12_djocks19 with dissolve
de "*{i}Sigh{/i}*"
de "What did you tell Anthony?"
scene ep12_djocks18 with dissolve
ash "I didn't tell him anything! I swear."
if ep7_hot_ashley_phase == 4:
    ash "It must have been that sex tape..."
else:
    ash "It must have been those sex tapes..."
ash "But how did he know? Someone must have shown him."
scene ep12_djocks19 with dissolve
de "It could have been Nick..."
scene ep12_djocks18 with dissolve
ash "Nick!?"
scene ep12_djocks19 with dissolve
de "It's...whatever..."
scene ep12_djocks17 with dissolve
ash "How's the finger?"
scene ep12_djocks19 with dissolve
de "The stitches are still there. It's just some blood."
scene ep12_djocks20 with dissolve
ash "Thank God! And how's your face?"
scene ep12_djocks23 with dissolve
de "It doesn't hurt as much as the finger. And that's with painkillers, too."
scene ep12_djocks21 with dissolve
ash "Derek... I'm so sorry."
scene ep12_djocks23 with dissolve
de "I...don't want to do this anymore, Ash."
scene ep12_djocks20 with dissolve
ash "Do what?"
scene ep12_djocks23 with dissolve
de "Pretend that we're friends and that everything is fine."
de "I'm in love with you."
scene ep12_djocks22 with dissolve
de "And you're probably in love with Anthony, or whatever, but something has to change."
scene ep12_djocks24 with dissolve
$ renpy.pause()
scene ep12_djocks25 with dissolve
ash "*{i}Smack{/i}*"
scene ep12_djocks26 with dissolve
stu "Guys? Guys? I've been holding on to a fart for like 5 minutes out of courtesy. Can you do this elsewhere?"
stop music fadeout 3
scene ep12_djocks27 with dissolve
$ renpy.pause()

label ep12_sally_label:
$ guideSuggestedPage = 230
show screen new_phone_screen
play music "music/ep8/licensed_music/track67.mp3"
scene ep12_sally1 with wipeleft
$ renpy.pause()
scene ep12_sally2 with dissolve
$ renpy.pause()
show ep12_sally8
if not persistent.ep12_cardcam8:
    show screen ep12_render_screen("cam8")
with dissolve
$ renpy.pause()
show ep12_sally3
hide screen ep12_render_screen
with dissolve
$ renpy.pause()
scene ep12_sally4 with dissolve
sy "Do you want something?"
scene ep12_sally9 with dissolve
$ renpy.pause()
scene ep12_sally6 with dissolve
$ renpy.pause()
scene ep12_sally7 with dissolve
$ renpy.pause()
scene ep12_sally5 with dissolve
$ renpy.pause()
scene ep12_sally10 with dissolve
mc "I'm here. Have you been waiting long?"
scene ep12_sally11 with dissolve
sy "I've been at it for an hour or so."
scene ep12_sally12 with dissolve
mc "What are you studying?"
scene ep12_sally13 with dissolve
sy "Linear algebra. It sucks donkey dick."
scene ep12_sally12 with dissolve
mc "Haha! That bad?"
scene ep12_sally13 with dissolve
sy "Ugh... Trust me. You'll hate it too."
scene ep12_sally12 with dissolve
mc "Is it on your finals?"
scene ep12_sally14 with dissolve
sy "Among other tests. This is the one I struggle with the most."
scene ep12_sally12 with dissolve
mc "I don't think I can help you with that."
scene ep12_sally15 with dissolve
sy "I don't need your help with it."
sy "I didn't mind your company today. That's all."
scene ep12_sally12 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
menu:
    "Tease her \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Aw. You didn't want to study alone?"
        scene ep12_sally14 with dissolve
        sy "What's wrong with that?"
        scene ep12_sally12 with dissolve
        mc "Nothing. I think it's cool that you asked me."
    "I'll keep you company \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "I'll happily keep you company."
scene ep12_sally17 with dissolve
mc "Although, why aren't you studying with your friends?"
scene ep12_sally15 with dissolve
sy "I don't want to get into it."
scene ep12_sally16 with dissolve
mc "Forget I asked."
scene ep12_sally18 with dissolve
mc "Are the finals like midterms?"
scene ep12_sally19 with dissolve
sy "Sort of. But the tests usually cover the entire curriculum."
sy "And that makes it so much harder."
scene ep12_sally22 with dissolve
sy "For instance, you might have a limited understanding of one area, and if there's a hard question on it, you're screwed."
scene ep12_sally20 with dissolve
mc "Well, I don't plan to ace the test. Because I don't think I will."
scene ep12_sally21 with dissolve
sy "Not with that attitude."
scene ep12_sally20 with dissolve
mc "Is it important to you to ace them?"
scene ep12_sally21 with dissolve
sy "A high grade says a lot about a person."
sy "Sure, it's enough if you have a high enough grade for it to count toward your major."
sy "However, if you show that you can go above and beyond, you can use it to your advantage and get great opportunities."
scene ep12_sally20 with dissolve
mc "I see..."
scene ep12_sally19 with dissolve
sy "What kind of person are you?"
scene ep12_sally20 with dissolve
mc "What do you mean?"
scene ep12_sally19 with dissolve
sy "Are you an overachiever like me, or do you settle for a passing grade?"
if minigames:
    $ ep12_class_performance = get_class_performance()
else:
    if affinity == "DIK":
        $ ep12_class_performance = 2
    elif affinity == "NEUTRAL":
        $ ep12_class_performance = 1
    else:
        $ ep12_class_performance = 0
scene ep12_sally20 with dissolve
if ep12_class_performance == 0:
    mc "I wouldn't describe myself as an overachiever, but I have gotten great grades on all tests here so far."
    scene ep12_sally19 with dissolve
    sy "There's no shame in being an overachiever. Take pride in it."
    scene ep12_sally23 with dissolve
    mc "Haha, alright. I'm proud to be a nerd, then."
elif ep12_class_performance == 1:
    mc "I'm not an overachiever, but I have passed all tests here so far."
    scene ep12_sally19 with dissolve
    sy "That's good. Then you have it in you to do even better."
    scene ep12_sally20 with dissolve
    mc "I'll try, but it's not the most important thing for me."
elif ep12_class_performance == 2:
    mc "I'd take a passing grade any day. I'm doing alright in college, so far."
    scene ep12_sally21 with dissolve
    sy "I don't think we'll see eye to eye on this."
else:
    mc "I'd take a passing grade any day... But college is challenging for me."
    mc "I'm trying my best, but the tests are harder than I thought they would be."
    scene ep12_sally21 with dissolve
    sy "Hm... You'd better get your shit together fast, then."
    sy "If you fall behind this early on, you won't make it. And that's the hard truth."

scene ep12_sally19 with dissolve
sy "Do you want me to show you what you should focus extra on?"
scene ep12_sally20 with dissolve
mc "In math and English?"
scene ep12_sally19 with dissolve
sy "Yeah. I know those tests by heart."
scene ep12_sally20 with dissolve
mc "If you know something I don't, go ahead."
scene ep12_sally24 with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

scene ep12_sally25 with dissolve
be "*{i}Whispers{/i}*"
scene ep12_sally26 with dissolve
mg "Well, talk to her about it."
scene ep12_sally27 with dissolve
be "Now?"
scene ep12_sally26 with dissolve
mg "When she's alone, of course."

scene ep12_sally28 with dissolve
sy "To sum up, that's often a common question on the test. Make sure you know all the steps to set up that equation."
scene ep12_sally29 with dissolve
mc "I'm impressed. How do you remember all of this?"
scene ep12_sally28 with dissolve
sy "You'll have to trust me. This will be on your test."
scene ep12_sally29 with dissolve
mc "I trust you. You seem to know what you're talking about."
mc "I'm getting hungry."
scene ep12_sally30 with dissolve
sy "Did you bring any lunch?"
scene ep12_sally31 with dissolve
mc "No, I'm heading home to eat."
scene ep12_sally30 with dissolve
sy "Then, let's continue this after lunch."
scene ep12_sally31 with dissolve
if affinity == "DIK":
    mc "Ugh... Nah, I think I'm gonna call it a day."
    scene ep12_sally32 with dissolve
    sy "Poor choice, [name]."
    scene ep12_sally31 with dissolve
    mc "I know, but thanks for the help."
else:
    mc "I think that's it for me today, but thank you for helping me. I appreciate it."
    scene ep12_sally30 with dissolve
    sy "It wasn't hard. I enjoyed it."
scene ep12_sally33 with dissolve
$ renpy.pause()

scene ep12_sally34 with dissolve
$ renpy.pause()
scene ep12_sally37 with dissolve
sy "What do you want?"
scene ep12_sally36 with dissolve
be "A word with you."
scene ep12_sally37 with dissolve
sy "Spill it."
scene ep12_sally36 with dissolve
be "Over here."
scene ep12_sally38 with dissolve
be "I hope you're not helping [name] too much."
scene ep12_sally39 with dissolve
sy "What is it to you?"
scene ep12_sally44 with dissolve
be "You're asking for trouble."
scene ep12_sally39 with dissolve
sy "Psch! I can study with whomever I want."
scene ep12_sally38 with dissolve
be "Listen. It would be in your best interest not to befriend [name] now - or any other DIK for that matter."
scene ep12_sally39 with dissolve
sy "Is this advice coming from you or Magnar?"
scene ep12_sally44 with dissolve
be "You know me... If it were up to me, things would be different."
be "After our vendetta is done, I will do everything I can to help you."
scene ep12_sally38 with dissolve
be "Who knows? With time, maybe things can go back to how they were."
scene ep12_sally40 with dissolve
sy "Things will never be the same between us again. Magnar made sure of it."
scene ep12_sally44 with dissolve
be "Maybe not between you and Magnar, but between the rest of us."
be "Magnar finally found Excalibus."
scene ep12_sally41 with dissolve
sy "I know."
scene ep12_sally45 with dissolve
be "You do?"
scene ep12_sally41 with dissolve
sy "Yeah, I saw it with my own eyes. Did he forget to tell you?"
scene ep12_sally44 with dissolve
be "He must have let that detail slip. Either way, he doesn't want to stop there."
scene ep12_sally42 with dissolve
sy "What do you mean?"
scene ep12_sally46 with dissolve
be "The vendetta. All the frats are going to pay for it. And we are starting with the DIKs."
be "And once they are dealt with, we'll deal with the others."
scene ep12_sally43 with dissolve
be "Please, Sally... Don't get caught in the crossfire."
scene ep12_sally47 with dissolve
$ renpy.pause()
scene ep12_sally48 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_sally49 with dissolve
$ renpy.pause()
$ new_bio("Sally", "I had a nice time studying together with Sally in the library. She taught me what she knew about the finals.")

label ep12_jocks_label:
hide screen new_phone_screen
play music "music/ep8/licensed_music/track78.mp3"
scene ep12_jocks1 with wiperight
dw "No... You're kidding!"
scene ep12_jocks2 with dissolve
an "He's banging my girl! I'm no cuck; I had to punch him!"
scene ep12_jocks7 with dissolve
dw "I get it, but I thought we agreed on waiting until after the competition to fight them."
scene ep12_jocks3 with dissolve
an "I saw him in the corridors and I snapped. I don't have it in me, Dawe."
an "I'm a passionate guy. I feel things! And he's porking my Ashley!"
scene ep12_jocks4 with dissolve
al "If you ask me, he didn't punch him hard enough. I'd kick him in his nuts, too."
scene ep12_jocks7 with dissolve
dw "We all want to punch them and shit on their faces! But this is what happens when we do it without thinking."
dw "They're sending Ant to the counselors. Do I have to remind you of what happened to Chad?"
scene ep12_jocks5 with dissolve
al "You drank their cum. How are you this calm about it?"
scene ep12_jocks8 with dissolve
dw "Protein is protein!"
scene ep12_jocks5 with dissolve
al "You're lying to yourself, dude."
scene ep12_jocks7 with dissolve
dw "My point is, if we fight them out in the open, we're gambling with the competition, guys..."
dw "We need everyone for it. We can't afford to lose a brother."
scene ep12_jocks8 with dissolve
dw "Yes. I swallowed their cum. But I also swallowed my pride, because that's how much I want us to win."
dw "I'm asking you guys to make the same kind of sacrifice."
scene ep12_jocks7 with dissolve
dw "Prank them, fuck with them, antagonize them... But don't do anything that can get you guys expelled or kicked out of the frat."
dw "Come on! We're so close to the competition now!"
scene ep12_jocks3 with dissolve
an "I'm sorry, guys..."
scene ep12_jocks7 with dissolve
dw "No one blames you. But you have to do better than this."
dw "Look at me! And look at Chad. Be more like us. Right, Chad?"
scene ep12_jocks11 with dissolve
ch "We can't go soft on them."
scene ep12_jocks9 with dissolve
dw "What?"
scene ep12_jocks11 with dissolve
ch "Anthony had the right idea. They deserve to get punched and screwed with."
scene ep12_jocks9 with dissolve
dw "But the competition..."
scene ep12_jocks12 with dissolve
ch "I know. We just gotta do something. To show them and everyone else we're not cool with them."
ch "If we let them fuck with us unpunished, people are going to think we've gone soft. We can't allow that to happen."
scene ep12_jocks6 with dissolve
al "Ha! I knew you were pissed at the DIKs, too. I fucking called it!"
al "What was in your letter?"
scene ep12_jocks11 with dissolve
ch "You guys were right about it. There were pictures of Sage in it."
scene ep12_jocks6 with dissolve
al "Nude pics of Sage? Has she been whoring around? Hook a brother up, will you?"
scene ep12_jocks11 with dissolve
ch "I'm not showing them to you."
ch "But the DIKs have it coming. I'm with whatever you guys want to do about it. And doing nothing is not the answer."
scene ep12_jocks10 with dissolve
dw "Well, I'm the President now. And I'm putting my foot down!"
stop music fadeout 3
dw "We're not fighting them until we win our competition. And that's final!"

label ep12_dprep_label:
show screen new_phone_screen
play music "music/ep2/freedom.mp3"
scene ep12_dprep1 with wipeleft
ty "What about not extending their lease? Or if you do what you did to the beta beta betas, and increase their rent?"
scene ep12_dprep2 with dissolve
rich "We can't. The DIKs aren't our tenants."
rich "Didn't I tell you that Dad sold the property off to Mr. Burgmeister? We don't have that power over them."
scene ep12_dprep3 with dissolve
ty "*{i}Groans{/i}*"
scene ep12_dprep4 with dissolve
rich "Take a breath. We'll get your heirloom back to you."
scene ep12_dprep3 with dissolve
ty "It's not enough. I want them to suffer."
scene ep12_dprep4 with dissolve
rich "Hold on with the threats until we see how they respond."
rich "If you can't contain your emotions, let me be the mediator."
scene ep12_dprep3 with dissolve
ty "Bah! Let you mediate? I don't believe I will."
ty "I know perfectly well how to be civil."
play sound "sound_effects/door_bang.mp3"
$ renpy.play("sound_effects/bell.mp3", "sfx3")
scene ep12_dprep5 with dissolve
"*{i}Door knock and doorbell{/i}*"
ty "Open up, you hoodlums!!!"
scene ep12_dprep6 with dissolve
rich "Hey? What happened to a civil approach?"
scene ep12_dprep7 with dissolve
ty "Be quiet and don't test me."
scene ep12_dprep8 with dissolve
rs "Yes?"
scene ep12_dprep11 with dissolve
ty "Russell! I demand that you bring me what's mine."
scene ep12_dprep9 with dissolve
rs "What is he talking about?"
play sound "sound_effects/season3/finger_snaps.mp3"
scene ep12_dprep12 with dissolve
"*{i}Fingers snapping{/i}*"
ty "Hey! Hey! You're talking to me, not him. Eyes over here."
scene ep12_dprep8 with dissolve
rs "What do you want?"
scene ep12_dprep11 with dissolve
ty "My family heirloom, that's been in my family for generations. The heirloom that my father passed on to me!"
scene ep12_dprep10 with dissolve
rs "You lost me."
scene ep12_dprep11 with dissolve
ty "Give me the mounted deer head that you stole, or I will call the police!"
scene ep12_dprep13 with dissolve
mc "Hey, what's the commotion?"
scene ep12_dprep14 with dissolve
rs "Tybalt wants the deer head back."
scene ep12_dprep16 with dissolve
rich "And Christian's suit, cane, and top hat. We know you stole those as well."
scene ep12_dprep17 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(+5 Maya)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]

menu:
    "Get lost \n{size=-4}[m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep12_dprep13 with dissolve
        mc "Get lost."
        scene ep12_dprep18 with dissolve
        ty "If you do not bring us what's ours, we will return with the police."
        ty "And who knows what else they will find?"
        scene ep12_dprep13 with dissolve
        mc "I don't respond well to threats."
        scene ep12_dprep18 with dissolve
        ty "If you think it's worth the risk, go ahead. I'll have them arrest your friend for larceny while they are at it!"
        scene ep12_dprep14 with dissolve
        rs "[name]... It's not worth it."
        scene ep12_dprep15 with dissolve
        mc "*{i}Sigh{/i}* Wait here..."
    "I'll get them \n{size=-4}[m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep12_dprep15 with dissolve
        mc "Wait here..."
scene ep12_dprep18 with dissolve
ty "Pronto!"
show ep12_dprep27
if not persistent.ep12_cardcam9:
    show screen ep12_render_screen("cam9")
with dissolve
mc "Derek?"
mc "Whoa! What happened to you?"
scene ep12_dprep28 with dissolve
de "Don't worry about it."
show ep12_dprep29
hide screen ep12_render_screen
with dissolve
mc "Who punched you?"
scene ep12_dprep30 with dissolve
de "Anthony."
scene ep12_dprep29 with dissolve
mc "Why did he punch you?"
scene ep12_dprep30 with dissolve
de "He found out about Ashley and me..."
scene ep12_dprep29 with dissolve
mc "Are you kidding? Did she tell him?"
scene ep12_dprep31 with dissolve
de "No... I think he saw the footage from the hidden camera."
de "I'm sorry to say it, but I'm getting more convinced Nick was behind this after all."
if affinity == "DIK":
    scene ep12_dprep32 with dissolve
    mc "I'm gonna beat the shit out of Anthony."
    scene ep12_dprep33 with dissolve
    de "Don't do that. Professor Hoff witnessed it and sent Anthony to the disciplinary committee."
    de "Don't get involved in this."
    scene ep12_dprep29 with dissolve
    mc "Bro, he punched you."
    scene ep12_dprep30 with dissolve
    de "I've got bigger problems than a scratch on my face. Don't worry about this."
else:
    scene ep12_dprep29 with dissolve
    mc "Are you ok?"
    scene ep12_dprep30 with dissolve
    de "Yeah. It looks worse than it is."
    de "Besides, I've got bigger problems than a scratch on my face."
    scene ep12_dprep29 with dissolve
    mc "I know, buddy... If you need something, say the word."
    scene ep12_dprep30 with dissolve
de "So, what's up?"
scene ep12_dprep32 with dissolve
mc "We have a situation at our doorstep. Tybalt wants the deer head back."
scene ep12_dprep33 with dissolve
de "But that's my family heirloom..."
scene ep12_dprep34 with dissolve
mc "I'm sorry, bro. We have to return it."
mc "..."
mc "Not in that state, though."
de "But... But..."
scene ep12_dprep32 with dissolve
mc "And the cane, top hat, and suit that you stole... They want those too."
scene ep12_dprep19 with dissolve
mc "Here."
scene ep12_dprep20 with dissolve
ty "You thieves."
scene ep12_dprep21 with dissolve
mc "Are we done here?"
if ep4_toldDerekAboutJade:
    scene ep12_dprep20 with dissolve
    ty "You will all get what's coming to you. Mark my words."
    ty "And I do not appreciate what you did to my mother."
    scene ep12_dprep24 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    scene ep12_dprep21 with dissolve
    mc "What...do you mean by that?"
    scene ep12_dprep22 with dissolve
    $ renpy.pause()
    play music "music/ep10/licensed_music/track149.mp3"
    scene ep12_dprep23 with dissolve
    ty "You know exactly what I mean by it."
    ty "Have you talked to my sister lately? Because I have."
    scene ep12_dprep24 with dissolve
    $ renpy.pause()
    play sound "sound_effects/season3/running2.mp3"
    scene ep12_dprep25 with dissolve
    $ renpy.pause()
    scene ep12_dprep26 with dissolve
    rich "What did you do?"
    $ new_bio("Tybalt", "Tybalt found out about what I had done with Jade, and he ratted me out to Sage.")
else:
    stop music fadeout 3
    scene ep12_dprep20 with dissolve
    ty "Hmpf... You will all get what's coming to you. Mark my words."

$ new_bio("Tybalt", "Somehow, Tybalt found out that Derek had stolen his mounted deer head, and he demanded to have it back.")
$ new_bio("Derek", "Derek got punched in the face by Anthony because he found out about Derek and Ashley.")
$ new_bio("Anthony", "Anthony punched Derek in the face after finding out about Derek and Ashley.")

jump ep12_smc_label

label ep12_mv_label:
hide screen new_phone_screen
play music "music/ep12/licensed_music/track199.mp3"
scene ep12_mv33 with wipeleft
$ renpy.pause()
scene ep12_mv34 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/gun_cock.mp3"
scene ep12_mv35 with dissolve
dl1 "Get inside - no sudden movements."
scene ep12_mv36 with dissolve
vi "Whoa! Relax. Don't do anything stupid..."
vi "Is it drugs you want? Money?"
play sound "sound_effects/door_close.mp3"
scene ep12_mv1 with dissolve
$ renpy.pause()
scene ep12_mv2 with dissolve
dl1 "Sit down."
scene ep12_mv3 with dissolve
vi "Mick!? Shit, you scared me."
vi "What's going on? Put the gun down."
play sound "sound_effects/hit.mp3"
scene ep12_mv4 with vpunch
dl1 "Shut the fuck up and do what I say!"
scene ep12_mv5 with dissolve
vi "Ah!!! Fuck! That hurts."
vi "What do you want!? I have already told you everything."
scene ep12_mv6 with dissolve
dl1 "Arms raised. Sit down."
scene ep12_mv7 with dissolve
dl1 "Hand over your phone."
scene ep12_mv8 with dissolve
vi "It's in my pocket."
scene ep12_mv9 with dissolve
dl1 "Reach for it and unlock it. Slowly."
scene ep12_mv10 with dissolve
$ renpy.pause()
scene ep12_mv11 with dissolve
$ renpy.pause()
scene ep12_mv12 with dissolve
$ renpy.pause()
scene ep12_mv14 with dissolve
$ renpy.pause()
scene ep12_mv13 with dissolve
$ renpy.pause()
scene ep12_mv14 with dissolve
$ renpy.pause()
scene ep12_mv16 with dissolve
dl1 "Give me your burner phone."
scene ep12_mv15 with dissolve
vi "It's over there in the cupboard."
scene ep12_mv16 with dissolve
dl1 "Get it. Slowly."
scene ep12_mv17 with dissolve
$ renpy.pause()
scene ep12_mv18 with dissolve
$ renpy.pause()
scene ep12_mv19 with dissolve
vi "Mick? What do you want from me? Can we fucking talk?"
scene ep12_mv20 with dissolve
dl1 "The phone."
scene ep12_mv21 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/thud.mp3"
scene ep12_mv22 with dissolve
dl1 "Back up."
scene ep12_mv23 with dissolve
vi "This is fucking bullshit, Mick! Why are you treating me like this?"
vi "Tell me what you're looking for. I can help you find it."
scene ep12_mv24 with dissolve
dl1 "Shut up."
scene ep12_mv25 with dissolve
$ renpy.pause()
scene ep12_mv28 with dissolve
$ renpy.pause()
scene ep12_mv26 with dissolve
$ renpy.pause()
scene ep12_mv29 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/thud.mp3"
scene ep12_mv30 with dissolve
$ renpy.pause()
scene ep12_mv31 with dissolve
$ renpy.pause()
scene ep12_mv32 with dissolve
dl1 "I'm with him, and I've searched his phones."
dl1 "Mhm."
scene ep12_mv27 with dissolve
dl1 "No, but he can't be trusted. I found out he threatened one of his customers to make them buy from him again."
dl1 "We tried to set him straight, but he went off to do the same shit behind our backs again with the same fucking customer."
scene ep12_mv32 with dissolve
dl1 "What do you want me to do with him?"
stop music fadeout 3
dl1 "Consider it done."
scene ep12_mv37 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/gunshot.mp3"
scene ep12_mv38 with vpunch
$ renpy.pause()

if not branchSage and not branchJill and not ep4_toldDerekAboutJade:
    jump ep12_lclass_label

label ep12_js_label:
if branchSage or (not branchJill):
    if "Sage" in breakup or ep4_toldDerekAboutJade:
        play music "music/ep7/licensed_music/track48.mp3"
        scene ep12_js1 with wipeleft
        if branchSage:
            ji "You guys broke up? Didn't you just enter a relationship?"
        else:
            ji "What are you saying?"
        if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
            if ep3_acceptedJade and not ep4_fuckedJade:
                scene ep12_js2 with dissolve
                sa "He got a handjob from my mother in class."
                scene ep12_js4 with dissolve
                ji "He what!?"
                scene ep12_js3 with dissolve
                sa "He was in her class, and she came on to him. And she gave him a handjob."
                scene ep12_js5 with dissolve
                ji "I can't believe what I'm hearing. [name] did that?"
                ji "You think you know someone and..."
                scene ep12_js2 with dissolve
                sa "He claims he didn't know who she was before doing it."
                scene ep12_js5 with dissolve
                ji "But still... She was his teacher. That's...so gross."
            elif ep12_break_or_tell == "tell":
                scene ep12_js2 with dissolve
                sa "He had sex with my mother."
                scene ep12_js4 with dissolve
                ji "He what!?"
                scene ep12_js3 with dissolve
                sa "He was in her class, and she came on to him. And, eventually, they ended up in bed together."
                scene ep12_js5 with dissolve
                ji "I can't believe what I'm hearing. [name] did that?"
                ji "You think you know someone and..."
                scene ep12_js2 with dissolve
                sa "He claims he didn't know who she was before doing it."
                scene ep12_js5 with dissolve
                ji "But still... She was his teacher. That's...so gross."
            else:
                scene ep12_js2 with dissolve
                sa "He had sex with my mother."
                scene ep12_js4 with dissolve
                ji "He what!?"
                scene ep12_js3 with dissolve
                sa "He had sex with her, recorded it on his phone, and used it for Hell Week to score points with his brothers."
                scene ep12_js5 with dissolve
                ji "I can't believe what I'm hearing. [name] did that?"
                ji "That's gross! You think you know someone and..."
                scene ep12_js2 with dissolve
                sa "He claims he didn't know who she was before doing it."
                scene ep12_js5 with dissolve
                ji "Bah! As if that makes it excusable."
            scene ep12_js6 with dissolve
            ji "Sage... I'm so sorry. What can I do for you?"
            scene ep12_js9 with dissolve
            if ep4_toldDerekAboutJade:
                sa "It might not be avoidable at this point, but don't spread it any further."
            else:
                sa "Just don't spread it any further."
            scene ep12_js6 with dissolve
            ji "I would never. So... Who knows about it?"
            scene ep12_js9 with dissolve
            if ep12_break_or_tell == "tell" and not ep4_toldDerekAboutJade:
                sa "As far as I know, just you."
            else:
                sa "As far as I know, just my brother and you. But I'm not sure."
            scene ep12_js10 with dissolve
            $ renpy.pause()
            scene ep12_js11 with dissolve
            sa "I'm gonna have to tell people about this, right?"
            scene ep12_js6 with dissolve
            ji "You don't have to tell anyone about it. This is your private matter."
            ji "Although I do appreciate that you put your trust in me like this."
            scene ep12_js9 with dissolve
            sa "What about Josy, Maya, and Bella? They will wonder what happened between me and [name]."
            if branchIsabella:
                sa "And since Bella is dating him..."
            scene ep12_js7 with dissolve
            ji "Look, you haven't done anything wrong. You don't owe anyone any explanation unless you want to."
            scene ep12_js9 with dissolve
            sa "I feel like I have to tell them, at least."
            scene ep12_js8 with dissolve
            if branchIsabella:
                ji "You're right. Bella needs to know."
                scene ep12_js11 with dissolve
                sa "Yeah... And Josy and Maya are my support. I need you now."
            else:
                ji "Because you're close?"
                scene ep12_js11 with dissolve
                sa "I mean, you girls are my support. I need you now."
            scene ep12_js7 with dissolve
            ji "I'll be there for you. And I'm sure they will too."
            scene ep12_js11 with dissolve
            sa "I will tell them."
            stop music fadeout 3
            scene ep12_js10 with dissolve
            $ renpy.pause()
        elif branchZoey:
            scene ep12_js2 with dissolve
            sa "He's still in love with his ex-girlfriend."
            scene ep12_js4 with dissolve
            ji "No way! He's in love with Zoey?"
            scene ep12_js3 with dissolve
            sa "I was right all along. They were more than friends."
            sa "I'm so fucking mad at him that I can't find the words to express it."
            scene ep12_js6 with dissolve
            ji "What happened?"
            scene ep12_js2 with dissolve
            sa "He broke up with me, just like that."
            sa "He gaslit me into thinking she was his friend, all the while they rekindled their relationship."
            scene ep12_js6 with dissolve
            ji "Did he cheat on you with her?"
            scene ep12_js3 with dissolve
            sa "Yes. They made out with each other."
            scene ep12_js5 with dissolve
            ji "I can't believe what I'm hearing."
            ji "You think you know someone and..."
            scene ep12_js10 with dissolve
            $ renpy.pause()
            scene ep12_js6 with dissolve
            ji "Sage... I'm so sorry. What can I do for you?"
            scene ep12_js11 with dissolve
            sa "Nothing. I needed someone's support; that's why I told you."
            scene ep12_js6 with dissolve
            ji "Well, you have it. I'm here for you."
            ji "There aren't any excuses for what [name] did to you."
            scene ep12_js11 with dissolve
            sa "How do you think the rest will react?"
            scene ep12_js6 with dissolve
            ji "Who?"
            scene ep12_js3 with dissolve
            sa "I know Derek will side with [name], but what about Josy, Maya, and Bella?"
            sa "I don't want to lose them."
            scene ep12_js7 with dissolve
            ji "You won't. You should talk to them about this."
            ji "They are sensible. They will understand."
            scene ep12_js6 with dissolve
            ji "You haven't done anything wrong."
            scene ep12_js11 with dissolve
            sa "Wrong or right, I don't care. I can't believe he'd do that to me."
            stop music fadeout 3
            scene ep12_js10 with dissolve
            $ renpy.pause()
        elif branchSage and ep12_break_or_tell == "break":
            scene ep12_js2 with dissolve
            sa "Yeah. Out of the blue he tells me that he wants to break up."
            scene ep12_js6 with dissolve
            ji "What for?"
            scene ep12_js11 with dissolve
            sa "He didn't give me any reason other than that he didn't want to be with me."
            sa "I thought he'd say that there was someone else, but he swore that there wasn't."
            scene ep12_js12 with dissolve
            sa "It hurts so much."
            scene ep12_js6 with dissolve
            ji "You liked him a lot, didn't you?"
            scene ep12_js2 with dissolve
            if RPsage >= 22:
                sa "I did both as a friend and girlfriend."
            else:
                sa "As a friend, yeah. But I'm not sure if there was more to it than that."
            sa "But I wasn't ready for it to end like that. It took me by surprise."
            scene ep12_js6 with dissolve
            ji "Sage... I'm so sorry. What can I do for you?"
            scene ep12_js2 with dissolve
            sa "I just need your support."
            scene ep12_js7 with dissolve
            ji "And you got it. I'm here for you."
            scene ep12_js10 with dissolve
            $ renpy.pause()
            scene ep12_js11 with dissolve
            sa "I'm gonna have to tell people about this, right?"
            scene ep12_js7 with dissolve
            ji "Take it at your own pace. This is your personal life."
            ji "I appreciate that you trusted me enough to tell me like this."
            scene ep12_js2 with dissolve
            sa "What about Josy, Maya and Bella? They will wonder what happened between me and [name]."
            sa "I feel like I have to tell them, at least."
            scene ep12_js7 with dissolve
            ji "If you want to, you should. I'm sure they will be there for you, too."
            scene ep12_js11 with dissolve
            sa "I will tell them."
            stop music fadeout 3
            scene ep12_js10 with dissolve
            $ renpy.pause()
    else:
        play music "music/ep5/licensed_music/track10.mp3"
        scene ep12_js13 with wipeleft
        sa "What do you think?"
        scene ep12_js14 with dissolve
        ji "I agree with you. He shouldn't still be friends with Zoey after this."
        scene ep12_js18 with dissolve
        sa "So, what I said wasn't uncalled for, right?"
        scene ep12_js14 with dissolve
        ji "I think your situation would make any girlfriend feel uncomfortable."
        ji "But it sounded like you gave [name] an ultimatum."
        scene ep12_js18 with dissolve
        sa "I didn't say he had to choose between her and me."
        scene ep12_js14 with dissolve
        ji "No, but if what you told me is the same as what you told him, it could be construed as you choosing for him."
        ji "And that if he didn't choose the way you wanted, it implied that you wouldn't be ok with it."
        scene ep12_js19 with dissolve
        sa "It's the only way he can choose, isn't it?"
        scene ep12_js14 with dissolve
        ji "You may feel that, but it has got to be up to him."
        scene ep12_js20 with dissolve
        sa "*{i}Sigh{/i}* I get what you're saying, but it scares me that he would do something stupid. Like picking the other option and trying to work it out with her."
        scene ep12_js15 with dissolve
        ji "And what if he did? How would you react?"
        scene ep12_js22 with dissolve
        sa "..."
        scene ep12_js15 with dissolve
        ji "Would you stop trusting him? Would you...break up with him?"
        scene ep12_js20 with dissolve
        sa "I'd feel so uncomfortable. Like, constantly."
        sa "Even if I'd trust him, there would still be lingering doubt."
        scene ep12_js21 with dissolve
        sa "I wouldn't feel good. And if I can't feel good when I'm in a relationship..."
        sa "Then what's the point of that relationship?"
        scene ep12_js16 with dissolve
        ji "How important is he to you?"
        if ep11_sage_love == 2:
            scene ep12_js23 with dissolve
            sa "I love him."
            scene ep12_js16 with dissolve
        elif RPsage >= 22:
            scene ep12_js24 with dissolve
            sa "Very... I never felt like this for someone before."
            scene ep12_js16 with dissolve
        else:
            scene ep12_js21 with dissolve
            sa "I'm not quite sure..."
            scene ep12_js15 with dissolve
        ji "And how does he feel about you?"
        if ep11_sage_love == 2:
            scene ep12_js23 with dissolve
            sa "It's mutual."
        elif ep11_sage_love == 1:
            scene ep12_js21 with dissolve
            sa "He told me he loves me, but I couldn't say it back."
        else:
            scene ep12_js21 with dissolve
            sa "He cares a lot about me. But I'm unsure how he truly feels."
        sa "I feel it would suck if his ex ruined everything."
        scene ep12_js16 with dissolve
        ji "Be patient with him. I'm sure he'll make the right decision."
        scene ep12_js24 with dissolve
        sa "Thanks... I needed someone else's opinion on it."
        scene ep12_js16 with dissolve
        ji "Anytime."
        scene ep12_js24 with dissolve
        sa "What about you? Any problems I can help you with?"
        scene ep12_js15 with dissolve
        ji "There's nothing new under the sun."
        label ep12_js2_label:
        if ep8_recital_failed:
            ji "I'm expected to perform at the faculty's Christmas party. It's stressing me out."
        else:
            ji "Oh! I'll be performing at the faculty's Christmas party. It's stressing me out a little."
        if ep11_music:
            scene ep12_js24 with dissolve
            sa "Oh! With [name], yes?"
            scene ep12_js16 with dissolve
            ji "We'll perform separately, but yes, he was also asked to play."
        scene ep12_js25 with dissolve
        sa "If I can make you feel better, my brother's performing at that party too."
        scene ep12_js17 with dissolve
        ji "Haha, I know. Have you heard him play yet?"
        scene ep12_js25 with dissolve
        sa "No, but he picked up that instrument a few months ago. How good can he have gotten?"
        scene ep12_js18b with dissolve
        ji "I don't think there has been much progress. He even stopped playing it at the mansion."
        scene ep12_js26 with dissolve
        sa "What the hell is he thinking? He's going to make a fool of himself."
        scene ep12_js18b with dissolve
        ji "I...kind of want to see that."
        scene ep12_js27 with dissolve
        sa "Hahaha! You're bad!"
        scene ep12_js17 with dissolve
        ji "I'm sorry! But I do."
        ji "He's put me through a lot this year. I think it's only fair that he embarrasses himself."
        scene ep12_js27 with dissolve
        sa "I'd so want to see that."
        scene ep12_js17 with dissolve
        ji "You should come."
        scene ep12_js25 with dissolve
        sa "Isn't it just for the faculty?"
        scene ep12_js16 with dissolve
        ji "Yes, but I can take care of it."
        scene ep12_js25 with dissolve
        if ep11_fighter and branchSage and (ep11_sage_love == 2 or RPsage >= 22):
            sa "Well... [name] is participating in a fighting competition that day. I want to be there for him."
            scene ep12_js30 with dissolve
            ji "The party is in the evening. When is the competition done?"
            scene ep12_js25 with dissolve
            sa "I'm not sure. But maybe I can make it to both."
            sa "Yeah, what the hell. Sign me up."
        elif ep11_music:
            sa "Sign me up. I want to watch you and [name] play."
        else:
            sa "Yeah, what the hell. Sign me up."
        scene ep12_js30 with dissolve
        ji "Then it's settled."
        scene ep12_js28 with dissolve
        sa "I'm sure you'll do great. Don't overthink it when you play."
        scene ep12_js30 with dissolve
        if not branchJill:
            if ep9_jill_mood != 1:
                stop music fadeout 3
        ji "I'll try."
        if branchJill:
            jump ep12_js2b_label
        if ep9_jill_mood == 1:
            scene ep12_js29 with dissolve
            sa "Hey... Um..."
            sa "Does it feel weird to you when I talk about my problems with [name]?"
            scene ep12_js31 with dissolve
            ji "Weird how?"
            scene ep12_js29 with dissolve
            sa "[name] told me you two dated."
            scene ep12_js34 with dissolve
            ji "..."
            scene ep12_js31 with dissolve
            ji "I wasn't sure if you were aware of that."
            scene ep12_js36 with dissolve
            sa "He told me about it. Well, not in great detail or anything. But it came up."
            scene ep12_js31 with dissolve
            ji "Maybe I should have let you know earlier..."
            ji "Considering your situation with Zoey and him... Do you feel weird around me, too?"
            scene ep12_js37 with dissolve
            sa "As I gather, you didn't...progress with [name]. Right?"
            scene ep12_js32 with dissolve
            ji "I'm not sure what you are getting at."
            scene ep12_js37 with dissolve
            sa "[name] told me you two never slept together."
            scene ep12_js32 with dissolve
            ji "We slept in the same bed, but we weren't intimate..."
            ji "I mean, I suppose it depends on what you mean by intimate."
            scene ep12_js38 with dissolve
            sa "Oh?"
            scene ep12_js32 with dissolve
            ji "We never had sex, if that's what you're asking."
            scene ep12_js38 with dissolve
            sa "How come?"
            scene ep12_js33 with dissolve
            ji "Now it feels weird."
            scene ep12_js39 with dissolve
            sa "I think it would feel weirder for me if we didn't finish this conversation."
            scene ep12_js33 with dissolve
            ji "It was because of me."
            ji "I haven't done that before-"
            scene ep12_js38 with dissolve
            sa "What? Never?"
            scene ep12_js33 with dissolve
            ji "No."
            scene ep12_js38 with dissolve
            sa "Jill..."
            scene ep12_js32 with dissolve
            ji "It just never happened."
            ji "I had strong feelings for him... It would have happened eventually, but I needed more time."
            scene ep12_js33 with dissolve
            ji "He ended it with me before Halloween because he had stronger feelings for you."
            scene ep12_js40 with dissolve
            sa "..."
            scene ep12_js39 with dissolve
            sa "Now I feel horrible..."
            scene ep12_js32 with dissolve
            ji "Sage... Don't."
            scene ep12_js39 with dissolve
            sa "I've been bitching about my problems to you. Talking your ears off about everything he's done and our relationship..."
            sa "How could you sit through that? Why didn't you stop me?"
            scene ep12_js35 with dissolve
            ji "I'm still his friend, and I want to be yours."
            ji "My feelings for him are different now."
            scene ep12_js39 with dissolve
            sa "Are you sure?"
            scene ep12_js33 with dissolve
            ji "It still hurts from time to time, but..."
            ji "It's not going to stop me from spending time with you guys."
            scene ep12_js41 with dissolve
            sa "Wow... You're a lot stronger than I am."
            scene ep12_js35 with dissolve
            ji "Oh? Did I make you feel weird about our friendship now?"
            scene ep12_js39 with dissolve
            sa "No. I pictured myself in your shoes. I don't see myself handling it as well as you."
            stop music fadeout 3
            scene ep12_js42 with dissolve
            $ renpy.pause()
elif branchJill:
    if "Jill" in breakup:
        play music "music/ep7/licensed_music/track48.mp3"
        scene ep12_js43 with wipeleft
        sa "What an absolute ass."
        scene ep12_js45 with dissolve
        ji "I thought I meant something more to him than that."
        ji "He never told me about his feelings for his ex-girlfriend. But they must have been there all along."
        ji "To think that he told me there was nothing left between them, and then he does that to me."
        scene ep12_js44 with dissolve
        sa "Yeah, it's wrong. He gaslit you."
        sa "I can't believe [name] would do that."
        scene ep12_js45 with dissolve
        ji "There wasn't even a discussion about it. He just dropped that bombshell on me."
        ji "I feel so stupid for trusting him and giving him the benefit of the doubt."
        scene ep12_js6 with dissolve
        ji "How could I have been so blind!? I even tried to defend his actions to you."
        ji "I should have listened to you. You knew what it was from the moment you heard about it."
        scene ep12_js49 with dissolve
        sa "Yeah, but I don't think you could have stopped this. Reacting differently would only have saved you some of the heartache."
        sa "I think [name] made up his mind the moment he started hanging out with Zoey. He allowed himself to feel for her, and he relapsed."
        scene ep12_js46 with dissolve
        ji "I'm so disappointed in him."
        scene ep12_js44 with dissolve
        sa "Disappointed? You should be fucking furious."
        sa "He's not worthy of you."
        if ep4_toldDerekAboutJade:
            scene ep12_js3 with dissolve
            sa "If you guys hadn't already broken up, I would have given you another reason for it."
            sa "[name] had sex with my mother."
            scene ep12_js4 with dissolve
            ji "He what!?"
            scene ep12_js44 with dissolve
            sa "He had sex with her, recorded it, and used it for Hell Week to score points with his brothers."
            scene ep12_js5 with dissolve
            ji "I can't believe what I'm hearing. [name] did that?"
            ji "That's gross! You think you know someone and..."
            scene ep12_js2 with dissolve
            sa "He claims he didn't know who she was before doing it."
            scene ep12_js5 with dissolve
            ji "Bah! As if that makes it excusable."
            scene ep12_js44 with dissolve
            sa "And after hearing what he did to you... Ugh..."
            sa "It makes me sick."
        else:
            scene ep12_js49 with dissolve
            sa "He threw away your relationship for what?"
            sa "Trust me. Their relationship won't last, and he'll come begging for you to have him back."
        scene ep12_js46 with dissolve
        ji "I'm so done with him."
        scene ep12_js50 with dissolve
        sa "You don't need him. You have our friends and me."
        scene ep12_js46 with dissolve
        ji "I don't want him anywhere near me."
        scene ep12_js50 with dissolve
        if ep4_toldDerekAboutJade:
            sa "You don't have to convince me. I'm with you."
        sa "So much for our joint circle of friends..."
        scene ep12_js47 with dissolve
        ji "I have to tell Josy and Maya about this."
        scene ep12_js51 with dissolve
        sa "What about Bella?"
        scene ep12_js47 with dissolve
        ji "I called her the moment after he broke up with me."
        scene ep12_js51 with dissolve
        sa "Let's tell them."
        scene ep12_js48 with dissolve
        ji "Now?"
        stop music fadeout 3
        scene ep12_js51 with dissolve
        sa "Trust me. You'll feel better having their support."
    else:
        if ep4_toldDerekAboutJade:
            $ guideSuggestedPage = 231
            $ breakup.append("Jill")
            play music "music/ep6/licensed_music/track21.mp3"
            scene ep12_js13 with wipeleft
            sa "How do I tell you this...?"
            scene ep12_js52 with dissolve
            ji "You can tell me anything. What did [name] do?"
            scene ep12_js55 with dissolve
            sa "He had sex with my mother."
            scene ep12_js4 with dissolve
            ji "He what!?"
            scene ep12_js3 with dissolve
            sa "He had sex with her, recorded it and used it for Hell Week to score points with his brothers."
            scene ep12_js53 with dissolve
            ji "..."
            scene ep12_js55 with dissolve
            sa "I know. It came as a shock to me, too."
            scene ep12_js54 with dissolve
            ji "Are you completely sure?"
            scene ep12_js55 with dissolve
            sa "My brother showed me the recording. There's no doubt about it, and [name] even admitted to it."
            scene ep12_js5 with dissolve
            ji "I can't believe what I'm hearing. That's... That's..."
            ji "That's so gross!"
            scene ep12_js54 with dissolve
            ji "I..."
            scene ep12_js56 with dissolve
            sa "Take it easy."
            scene ep12_js59 with dissolve
            ji "How can I take it easy? I'm disgusted."
            ji "Why would he do something like that?"
            scene ep12_js56 with dissolve
            sa "I knew the DIKs had some weird tasks that they do during Hell Week, but to think that [name] would do that..."
            sa "Even if I put aside that it was with my mother, it's still so fucking nasty to do that to someone."
            sa "To have sex with someone to score points with his frat, and to record it..."
            scene ep12_js61 with dissolve
            $ renpy.pause()
            scene ep12_js57 with dissolve
            sa "Are you ok?"
            scene ep12_js59 with dissolve
            ji "How can I ever be ok now?"
            ji "My boyfriend did that. It's so wrong."
            ji "What he did goes against every moral fiber of my being."
            scene ep12_js57 with dissolve
            sa "So, what do we do?"
            scene ep12_js59 with dissolve
            ji "How can I possibly be with someone who would do that?"
            scene ep12_js58 with dissolve
            sa "Jill... I'm so sorry."
            scene ep12_js60 with dissolve
            ji "If you hadn't told me, maybe I would never have known."
            ji "[name]... Why did you do this?"
            scene ep12_js57 with dissolve
            sa "I'm gonna have to tell people about this, right?"
            scene ep12_js60 with dissolve
            ji "Oh my God... I didn't even think about that. What will we even say? People will have questions."
            scene ep12_js58 with dissolve
            sa "Yeah. Josy, Maya, and Bella will wonder what happened between us. They deserve the truth."
            sa "I feel like I have to tell them, at least."
            scene ep12_js60 with dissolve
            ji "Well, I need to talk to him right now."
            scene ep12_js62 with wipeleft
            mc "It was a stupid mistake. I was new here and wanted to fit in."
            mc "Everyone tried to push us to do these tasks, and I didn't want to let them down."
            scene ep12_js64 with dissolve
            ji "That doesn't even begin to explain why you would do such a thing."
            scene ep12_js65 with dissolve
            ji "You recorded a teacher having sex with you for the sake of impressing your friends."
            ji "Can't you hear how disgusting that sounds!?"
            scene ep12_js66 with dissolve
            mc "I know it sounds bad, but I was single, and she didn't mind being recorded..."
            mc "The video was never meant to spread like that."
            scene ep12_js64 with dissolve
            ji "You seem to believe that the only thing wrong about this is that the video spread."
            ji "Answer me this, if you had gotten away with it and no one would have known about it..."
            ji "...would you ever have told me? Would that have made it all better?"
            scene ep12_js66 with dissolve
            mc "We all have private lives and a past. I don't blame you for your past choices. I think you should cut me some slack for mine."
            scene ep12_js67 with dissolve
            ji "Oh my God! I cannot believe you."
            ji "Who are you?"
            scene ep12_js63 with dissolve
            mc "I made a mistake, Jill. I'm not proud of what I did, but I can't undo it."
            scene ep12_js66 with dissolve
            ji "..."
            scene ep12_js67 with dissolve
            ji "No. That doesn't make it any better."
            ji "I think this is it for us."
            scene ep12_js66 with dissolve
            mc "Are you breaking up with me because of a mistake? It had nothing to do with you."
            scene ep12_js65 with dissolve
            ji "It's not something as simple as a mistake, [name]."
            ji "Our relationship was built during that time. It's in our foundation."
            ji "Someone whom I'd want to be with long-term wouldn't have chosen to do those things to begin with."
            ji "It speaks to who you are as a person. And you crossed a line with me."
            stop music fadeout 3
            scene ep12_js68 with dissolve
            $ renpy.pause()
        else:
            play music "music/ep5/licensed_music/track10.mp3"
            scene ep12_js69 with wipeleft
            sa "What's new with you?"
            scene ep12_js70 with dissolve
            jump ep12_js2_label
            label ep12_js2b_label:
            scene ep12_js76 with dissolve
            sa "And how is your relationship treating you?"
            scene ep12_js71 with dissolve
            ji "It's going...well."
            scene ep12_js77 with dissolve
            sa "What was that smile?"
            scene ep12_js71 with dissolve
            ji "I'm just happy."
            scene ep12_js77 with dissolve
            sa "Elaborate."
            scene ep12_js72 with dissolve
            ji "I shouldn't... It's private."
            scene ep12_js76 with dissolve
            sa "That's code for sex talk, and that's the fun stuff to share."
            scene ep12_js72 with dissolve
            ji "I'm not used to sharing intimate details."
            scene ep12_js77 with dissolve
            sa "You don't have to be specific. That smile of yours tells me things are good in bed."
            scene ep12_js73 with dissolve
            ji "Oh, God."
            scene ep12_js78 with dissolve
            sa "That good?"
            scene ep12_js72 with dissolve
            ji "He's very good. But..."
            ji "He's also a lot more experienced than I am."
            scene ep12_js77 with dissolve
            sa "He's a slut, huh?"
            scene ep12_js72 with dissolve
            ji "*{i}Scoffs{/i}* No. But comparatively..."
            scene ep12_js76 with dissolve
            sa "He's been with more than you."
            scene ep12_js74 with dissolve
            ji "Given that he was my first, obviously."
            scene ep12_js79 with dissolve
            sa "Oh? You lost your V-card to him?"
            scene ep12_js74 with dissolve
            ji "Yes."
            scene ep12_js79 with dissolve
            sa "I see."
            scene ep12_js74 with dissolve
            ji "At first, I felt...um...inadequate. But he always encourages me and takes the pressure off."
            ji "And I started to feel more comfortable, but I'm still unsure if I'm doing enough and where to go from here."
            scene ep12_js76 with dissolve
            sa "Doing enough, how?"
            scene ep12_js72 with dissolve
            ji "He has all these ideas about how, when, and where... He's taking the lead when it comes to sex."
            scene ep12_js76 with dissolve
            sa "Don't you like that he's taking charge?"
            scene ep12_js72 with dissolve
            ji "I do. But I want to show him that I know how to do things too, and lead him."
            scene ep12_js77 with dissolve
            sa "Then do it."
            scene ep12_js74 with dissolve
            ji "I would. Only that... I'm unsure how to do things or how to lead."
            ji "Pretty much everything I know, I only know because [name] taught me."
            scene ep12_js77 with dissolve
            sa "Ah, so you have the ambition, but you ain't got the moves."
            scene ep12_js72 with dissolve
            ji "That's another way of putting it. There aren't any ways you can learn these things."
            scene ep12_js76 with dissolve
            sa "Are you joking? You can learn about sex from everywhere."
            sa "Surf porn on your phone and you'll pick up a lot of tricks."
            scene ep12_js75 with dissolve
            ji "Oh, I don't do that."
            scene ep12_js78 with dissolve
            sa "Don't you watch porn?"
            scene ep12_js75 with dissolve
            ji "Now, I'm uncomfortable again."
            scene ep12_js77 with dissolve
            sa "Well, what do you want to know? How to drive [name] wild in bed? Is that it?"
            scene ep12_js74 with dissolve
            ji "It would be nice to know how to do that without him taking command."
            scene ep12_js77 with dissolve
            sa "I can give you a few pointers if you'd like."
            scene ep12_js74 with dissolve
            ji "What kind of pointers?"
            scene ep12_js76 with dissolve
            sa "Show me how you do doggy."
            scene ep12_js75 with dissolve
            ji "You...want me to show you?"
            scene ep12_js76 with dissolve
            sa "I can tell you how to improve it."
            scene ep12_js74 with dissolve
            ji "I don't think so."
            scene ep12_js77 with dissolve
            sa "Didn't you take yoga classes? This isn't anything different."
            scene ep12_js74 with dissolve
            ji "I strongly disagree on that one. Yoga is as far away from sex as you can get."
            scene ep12_js77 with dissolve
            sa "Aw, bless you... Fine. Let me show you then."
            sa "Watch and learn."
            scene ep12_js80 with dissolve
            sa "You start on all fours, yeah? And isn't that like yoga?"
            scene ep12_js81 with dissolve
            ji "Yes, but..."
            scene ep12_js82 with dissolve
            sa "Looks like I'm right, after all."
            sa "Now, when girls start out doing doggy, I imagine most of them going like this."
            scene ep12_js84 with dissolve
            ji "Isn't that how it's supposed to look?"
            scene ep12_js83 with dissolve
            sa "Well, yeah. It's nice, it's classic, but not something guys will write home about."
            sa "There are levels to it. And by making a few tweaks, you will drive him nuts."
            scene ep12_js85 with dissolve
            ji "..."
            scene ep12_js86 with dissolve
            ji "Tell me more."
            scene ep12_js87 with dissolve
            sa "The next level, which makes it better for him, is simply dropping down on your elbows like this."
            scene ep12_js88 with dissolve
            $ renpy.pause()
            scene ep12_js89 with dissolve
            ji "I can do that."
            scene ep12_js90 with dissolve
            sa "And to make it even better. Separate your legs wide like this."
            scene ep12_js91 with dissolve
            ji "Elbows dropped and separated legs."
            scene ep12_js90 with dissolve
            sa "And finally... For the ultimate position, drop your arms down like you're resting on a pillow."
            scene ep12_js92 with dissolve
            sa "Trust me. If you drop into this position, he will go nuts for you. That's all there is to it."
            scene ep12_js93 with dissolve
            sa "He will think you're amazing in bed, and all you did was take doggy to another level with some simple tweaks."
            scene anim_js1_ep12 with dissolve
            sa "Also, don't be still when you're down here getting busy."
            sa "Thrust back. Moan. Tell him sexy things."
            pause
            scene anim_js2_ep12 with dissolve
            ji "I can see that working. I think that's not far off from what I've been doing... Maybe..."
            pause
            scene ep12_js80 with dissolve
            sa "Oh, yeah? Show me! It's your turn."
            scene ep12_js94 with dissolve
            ji "..."
            scene ep12_js80 with dissolve
            sa "You're making me uncomfortable by not doing it."
            scene ep12_js95 with dissolve
            sa "All fours."
            scene ep12_js96 with dissolve
            sa "Elbows dropped."
            scene ep12_js97 with dissolve
            sa "Awesome."
            scene ep12_js98 with dissolve
            sa "Legs spread. And arms resting."
            scene ep12_js99 with dissolve
            sa "Yep, just like that."
            scene anim_js3_ep12 with dissolve
            sa "Remember, thrust back and forth and help him out back there..."
            pause
            scene anim_js4_ep12 with dissolve
            sa "Wow! That looks hot. I knew you could do it. You're a natural!"
            pause
            scene ep12_js100 with dissolve
            sa "That was a piece of cake for you. I wonder why."
            scene ep12_js101 with dissolve
            ji "Haha. Just because it's due to yoga doesn't mean it is yoga."
            ji "But thank you for showing me."
            scene ep12_js105 with dissolve
            sa "Any time."
            sa "Oh! And something else you can do to spice it up: have sex with him in a place where he doesn't expect you to do it."
            sa "Like, in the car or in a bathroom somewhere."
            scene ep12_js102 with dissolve
            ji "How does the dressing room of a clothing store sound?"
            scene ep12_js105 with dissolve
            sa "Risky as hell. I wouldn't do that as a first, but you're on to something."
            scene ep12_js102 with dissolve
            ji "I ask because we did that one already."
            scene ep12_js106 with dissolve
            sa "What? No way!!!"
            scene ep12_js101 with dissolve
            ji "We did! When we went shopping for Christmas gifts."
            scene ep12_js106 with dissolve
            sa "You should give yourself more credit. That's wild!"
            scene ep12_js103 with dissolve
            ji "Does... Um... Does anal sex hurt?"
            scene ep12_js107 with dissolve
            sa "..."
            scene ep12_js108 with dissolve
            sa "I did not think I'd be talking about that with you today."
            stop music fadeout 3
            scene ep12_js104 with dissolve
            $ renpy.pause()

label ep12_lclass_label:
show screen new_phone_screen
play music "music/ep5/licensed_music/track11.mp3"
scene ep12_lclass1 with wipeleft
$ renpy.pause()
if branchZoey:
    scene ep12_lclass2 with dissolve
    de "I know you two have history, but it's gonna be weird to see you together with Zoey."
    if breakup or branchIsabella:
        scene ep12_lclass3 with dissolve
        mc "I wish I could be 100%% happy about it, but at the moment it feels like shit..."
    else:
        scene ep12_lclass4 with dissolve
        mc "No kidding. It will feel weird for me too..."
    scene ep12_lclass5 with dissolve
    de "Why? Don't you want to be with Zoey?"
    scene ep12_lclass6 with dissolve
    if breakup or (branchIsabella and not wt_ep11_zoey_kiss_others):
        if branchIsabella and not wt_ep11_zoey_kiss_others:
            mc "Oh, I do! But I meant I felt weird because I need to break up with Bella."
        else:
            mc "Oh, I do! But I meant I felt weird because of the breakup."
        scene ep12_lclass7 with dissolve
        if "Sage" in breakup:
            de "How did Sage take it?"
            scene ep12_lclass6 with dissolve
            mc "*{i}Groans{/i}*"
            scene ep12_lclass7 with dissolve
            de "That bad?"
            scene ep12_lclass6 with dissolve
            if ep4_toldDerekAboutJade:
                label ep12_lclass_b_label:
                if "Sage" in breakup or "Jill" in breakup:
                    mc "Actually, she was the one who broke up with me."
                mc "Somehow, Tybalt saw the video of me fucking Jade... And he told Sage about it."
                if "Jill" in breakup:
                    mc "Then Sage told Jill, and she ended it with me."
                scene ep12_lclass8 with dissolve
                de "Bro... No."
                scene ep12_lclass9 with dissolve
                if "Sage" in breakup or "Jill" in breakup and branchZoey:
                    mc "Yep... I didn't even have to tell her about Zoey. It was already over."
                else:
                    mc "Yep... There was no way to explain it to her. She wouldn't listen to me."
                scene ep12_lclass8 with dissolve
                de "How the fuck did Tybalt get a hold of that recording?"
                scene ep12_lclass9 with dissolve
                mc "Someone must have sent it to him recently, or he would have confronted me about it earlier..."
                if "Jill" in breakup:
                    mc "I think both Jill and Sage hate my guts..."
                else:
                    if "Sage" in breakup:
                        mc "I think Sage hates my guts... It was a bad breakup."
                    else:
                        mc "I think Sage hates my guts..."
            else:
                mc "Yeah... It wasn't pretty."
            scene ep12_lclass6 with dissolve
        elif "Josy" in breakup or "Maya" in breakup:
            de "How did they take it?"
            scene ep12_lclass6 with dissolve
            if ep12_josy_hurt:
                mc "Josy was hurt... She doesn't want to stay friends with me."
            else:
                mc "Josy didn't think I tried enough with them."
                mc "She wasn't as hurt as I feared she'd be, but she still found it difficult to stay friends after."
            scene ep12_lclass7 with dissolve
            de "And what about my sis?"
            scene ep12_lclass9 with dissolve
            if ep12_maya_hurt:
                mc "She was hurt, but mature about it. It was easier to tell her than Josy."
                mc "But I think that's because it's always been a tad easier talking to Maya."
            else:
                mc "She understood. She even said that she hadn't felt us click."
                mc "She said she loved me as a friend, and I'm with her on that one."
                mc "Even though I told them at the same time, it was easier to tell Maya about Zoey than Josy."
            mc "Josy is more...emotionally driven, whereas Maya can handle hearing bad news."
            scene ep12_lclass7 with dissolve
            de "Ah... Shit... This is going to affect us, isn't it?"
            scene ep12_lclass6 with dissolve
        elif branchIsabella:
            de "Haven't you done it yet?"
            scene ep12_lclass6 with dissolve
            mc "I almost mentioned it to her when we celebrated Christmas, but I feel like I need to have a real talk with her about it."
            mc "I felt like I was bringing it up at a particularly bad time."
            scene ep12_lclass3 with dissolve
            mc "But I can't control the timing... I made that decision about Zoey during our Christmas party."
            mc "Then Bella dropped that bombshell..."
            scene ep12_lclass7 with dissolve
            de "Ugh... I wouldn't wanna be in your spot. But I think you're doing the right things."
            de "Maybe it doesn't feel that way now, but in the greater scheme of things, you were honest and up front about it."
            scene ep12_lclass6 with dissolve
            mc "*{i}Groans{/i}* I did kiss Zoey while I was with Bella."
            if tc > 3:
                mc "And I've been tempted before, too..."
            scene ep12_lclass5 with dissolve
            de "Aight... I feel you..."
            scene ep12_lclass6 with dissolve
        elif "Jill" in breakup:
            de "How did Jill take it?"
            scene ep12_lclass6 with dissolve
            mc "She was mad, sad, and disappointed..."
            mc "She said I didn't care about her and that I broke her heart."
            mc "She felt humiliated... But I only told her that I loved Zoey, not that Jill didn't mean something."
            scene ep12_lclass7 with dissolve
            de "Jill must have been into you a lot. I'm not surprised that she took it badly."
            scene ep12_lclass6 with dissolve
            mc "It hurt to see her react that way. I never wanted to be the reason she was upset like that."
            scene ep12_lclass7 with dissolve
            de "It's shit, but it had to be done."
            scene ep12_lclass6 with dissolve
            mc "It's true... But now that I've upset her..."

        mc "I'm not sure if we'll hang out together as a group again."
        scene ep12_lclass5 with dissolve
        if ep4_toldDerekAboutJade and not "Jill" in breakup and not "Sage" in breakup:
            de "Give it time, [mc_de]. It's a fresh wound..."
        else:
            de "Breakups are always hard. Give it time, [mc_de]."
    else:
        mc "Oh, I do! But that doesn't stop it from feeling weird."
        mc "It will be the first time we know that's what we're doing together."
        scene ep12_lclass3 with dissolve
        mc "She put her heart on the line, and I knew it then and there..."
        mc "I felt the same as her."
        scene ep12_lclass6 with dissolve
        mc "Maybe that's why it feels weird. It feels real this time."
        mc "I can't wait to tell her that... But at the same time, I need to sort my thoughts out completely."
        scene ep12_lclass5 with dissolve
        de "Going from single to a relationship is quite the leap."
        de "I think you'll get used to it, and I'll get used to seeing you with Zoey."
    scene ep12_lclass6 with dissolve
    mc "And what about you?"
    scene ep12_lclass11 with dissolve
    de "Hm?"
    scene ep12_lclass6 with dissolve
elif "Sage" in breakup or "Jill" in breakup or ep4_toldDerekAboutJade:
    scene ep12_lclass5 with dissolve
    de "How are you feeling?"
    scene ep12_lclass6 with dissolve
    if "Jill" in breakup:
        mc "Not that good. Jill and I just broke up..."
    elif "Sage" in breakup:
        mc "Not that good. Sage and I broke up..."
    else:
        mc "Not that good. Sage and I had a huge fight."
    scene ep12_lclass7 with dissolve
    if "Jill" in breakup or "Sage" in breakup:
        de "Oh... That explains it."
    else:
        de "Oh... That explains it. What was the fight about?"
    scene ep12_lclass6 with dissolve
    if ep4_toldDerekAboutJade:
        jump ep12_lclass_b_label
    else:
        mc "Yeah... It wasn't pretty."
        scene ep12_lclass7 with dissolve
        de "How did you do it?"
        scene ep12_lclass6 with dissolve
        if ep12_break_or_tell == "break":
            mc "I decided not to let her know about Jade."
            mc "She didn't understand why I wanted to break up with her."
            scene ep12_lclass7 with dissolve
            de "What reason did you give her?"
            scene ep12_lclass6 with dissolve
            mc "I told her I wasn't feeling it, but she didn't buy it."
            mc "She sensed that I was lying about why I broke up with her, but it didn't matter."
            scene ep12_lclass3 with dissolve
            mc "I feel somewhat relieved that it's done..."
            mc "But at the same time... I didn't want to do it."
            scene ep12_lclass10 with dissolve
            if ep11_sage_stance == 1:
                de "I know, buddy. You sacrificed something for her."
                de "She doesn't know it, and she never will, but you know it."
                de "Try to find comfort in that."
                scene ep12_lclass6 with dissolve
                mc "*{i}Sigh{/i}* I wish I could rewind time."
                scene ep12_lclass5 with dissolve
                de "Life would be perfect if you could. Take the time you need to move on. There's no rush."
                scene ep12_lclass6 with dissolve
                mc "Yeah... I will."
            elif ep11_sage_stance == 2:
                de "When we talked earlier about this, you thought your relationship with Sage would be short-term."
                scene ep12_lclass6 with dissolve
                mc "Yeah, but not this short. I feel like I'm wrong about things all the time."
                mc "Maybe I was wrong about this, too."
                scene ep12_lclass5 with dissolve
                de "I think you did a good thing."
                de "There was no good choice for you. You did what you could."
                scene ep12_lclass6 with dissolve
                mc "Thanks."
            else:
                de "When we talked earlier about this, you didn't know what you wanted to be with Sage."
                de "That doesn't sound like it was love."
                scene ep12_lclass6 with dissolve
                mc "Even so... It's going to take some time to recover from this."
                scene ep12_lclass5 with dissolve
                de "Take all the time you need. There was no good choice for you. You did what you could."
                scene ep12_lclass6 with dissolve
                mc "Thanks."
            mc "But I'm not sure if we'll hang out together as a group again."
        else:
            mc "I decided to tell her about Jade."
            scene ep12_lclass7 with dissolve
            de "Oh..."
            scene ep12_lclass6 with dissolve
            mc "If there were the tiniest chance that she'd forgive me, I wanted to try."
            mc "But she freaked out... I got to explain myself, but in the end, it didn't matter."
            scene ep12_lclass3 with dissolve
            mc "It crushed her. She was mad at me, and I think she was mad at her mom, too, but I took the blame."
            mc "I owned up to my mistake... That's all I could do."
            scene ep12_lclass6 with dissolve
            mc "And I told her that I didn't want our relationship to end, and that there must be a way for her to forgive me."
            mc "But... She started hitting me as she broke up with me."
            scene ep12_lclass5 with dissolve
            de "There was no good choice in your situation. You did what you could."
            de "I respect that you wanted to be honest with her, even though I would have taken a different approach to the situation."
            scene ep12_lclass6 with dissolve
            mc "Thanks..."
            mc "I'm not sure if we'll hang out together as a group again."
        scene ep12_lclass5 with dissolve
        de "I see what you mean..."
    scene ep12_lclass6 with dissolve
    mc "And what about you?"
    scene ep12_lclass11 with dissolve
    de "Hm?"
    scene ep12_lclass6 with dissolve
else:
    scene ep12_lclass6 with dissolve
    mc "So..."
mc "You and Ashley, huh?"
scene ep12_lclass12 with dissolve
de "I...think so."
scene ep12_lclass13 with dissolve
mc "You two made out. Trust me; she wants you."
scene ep12_lclass12 with dissolve
de "We've had sex before. A few kisses don't mean anything."
de "She was caught up in the moment."
scene ep12_lclass13 with dissolve
mc "Do you want to be with her?"
scene ep12_lclass14 with dissolve
de "More than I want my fingertip back."
scene ep12_lclass13 with dissolve
mc "Then go for it."
scene ep12_lclass12 with dissolve
de "I did. That's why we kissed."
de "But I've yet to see her break up with Anthony. Until that happens, I'm not going to assume anything."
$ guideSuggestedPage = 231
if ep11_girl_leaving:
    scene ep12_lclass15 with dissolve
    $ renpy.pause()
    scene ep12_lclass17 with dissolve
    $ renpy.pause()
    scene ep12_lclass16 with dissolve
    $ renpy.pause()
    scene ep12_lclass18 with dissolve
    $ renpy.pause()
    scene ep12_lclass19 with dissolve
    if breakup:
        if branchZoey and not wt_ep11_zoey_kiss_others:
            label ep12_lclass_c_label:
            de "Don't get any ideas now."
            scene ep12_lclass20 with dissolve
            mc "Just because a girl smiles at me? You don't have to worry about that."
            mc "I'm gonna talk to Sally."
        else:
            de "Normally, I'd recommend you get back on the horse, but I think you should wait a bit."
            scene ep12_lclass20 with dissolve
            
            if persistent.mod_wtenabled: 
                        $mod_choices = ["(Possible path)","(-5 Maya)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
                        
                        
                        
                        

            
            menu:
                "Heed Derek's advice":
                    mc "I know. I wasn't going to talk to her."
                    scene ep12_lclass22 with dissolve
                    de "Good call. Nikita is hot, though."
                    scene ep12_lclass21 with dissolve
                    mc "That's her name?"
                    scene ep12_lclass22 with dissolve
                    de "Yeah. She left a bag in my room on Halloween."
                    scene ep12_lclass21 with dissolve
                    mc "I see."
                    mc "I'm gonna talk to Sally."
                "Talk to her \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep12_nikita = True
                    mc "Just because a girl smiles at me?"
                    mc "I need time, but talking to girls isn't getting back on any horse."
                    scene ep12_lclass22 with dissolve
                    de "Well... Nikita is hot."
                    scene ep12_lclass21 with dissolve
                    mc "That's her name?"
                    scene ep12_lclass22 with dissolve
                    de "Yeah. She left a bag in my room on Halloween."
                    scene ep12_lclass21 with dissolve
                    mc "Thanks for the info."
    elif branchZoey and not wt_ep11_zoey_kiss_others:
        jump ep12_lclass_c_label
    elif not branchAlone:
        jump ep12_lclass_c_label
    else:
        $ ep12_nikita = True
        de "Go for it, dude."
        scene ep12_lclass20 with dissolve
        mc "Go for what?"
        scene ep12_lclass22 with dissolve
        de "For Nikita. She was smiling at you."
        scene ep12_lclass21 with dissolve
        mc "Is that her name?"
        scene ep12_lclass22 with dissolve
        de "Yeah. She left a bag in my room on Halloween."
        scene ep12_lclass21 with dissolve
        mc "Thanks for the info."
    if ep12_nikita:
        scene ep12_lclass23 with dissolve
        mc "So... We-"
        play sound "sound_effects/shove.mp3"
        scene ep12_lclass24 with vpunch
        nik "Are you ok?"
        scene ep12_lclass25 with dissolve
        mc "I tripped on my shoe. Let me try that again."
        scene ep12_lclass26 with dissolve
        nik "Haha! Sure."
        scene ep12_lclass27 with dissolve
        mc "*{i}Clears throat{/i}* So... We meet again."
        scene ep12_lclass28 with dissolve
        nik "Hahaha!"
        scene ep12_lclass30 with dissolve
        nik "*{i}Breathes out{/i}*"
        scene ep12_lclass31 with dissolve
        nik "Hm? And you are?"
        nik "Oh, wait! It's you! Sorry, but I didn't recognize you in your clothes."
        scene ep12_lclass29 with dissolve
        mc "Good one."
        scene ep12_lclass33 with dissolve
        nik "Haha! Hi, [name]."
        scene ep12_lclass29 with dissolve
        mc "Hi, to you... Nikita."
        scene ep12_lclass31 with dissolve
        nik "I'm impressed. You cared enough to find out my name."
        nik "But it's also a tad concerning..."
        scene ep12_lclass29 with dissolve
        mc "Trust me; I'm not a stalker. My friend Derek knew it."
        scene ep12_lclass32 with dissolve
        nik "Aw... And the mystery is gone. I thought it was more enigmatic than that."
        scene ep12_lclass29 with dissolve
        mc "I'm sorry to ruin the mystery, but I was going to find out your name somehow."
        mc "It's not often someone keeps you from learning it. What other secrets are you hiding?"
        scene ep12_lclass31 with dissolve
        nik "It's not a chase without a good bit of fun."
        scene ep12_lclass34 with dissolve
        mc "So, you were putting me up to it."
        scene ep12_lclass33 with dissolve
        nik "Not intentionally, but you made me want to."
        scene ep12_lclass29 with dissolve
        mc "Why is that?"
        scene ep12_lclass31 with dissolve
        nik "Imagine if I just told you."
        scene ep12_lclass29 with dissolve
        mc "Well, the chase ends here."
        scene ep12_lclass32 with dissolve
        nik "It does? I mean, you were down on your knee a minute ago."
        scene ep12_lclass34 with dissolve
        mc "I think it's your turn to chase me for a change."
        scene ep12_lclass33 with dissolve
        nik "My turn? Hm... I don't know. Are you worth chasing?"
        scene ep12_lclass34 with dissolve
        mc "Yep. I'm a catch."
        scene ep12_lclass35 with dissolve
        $ renpy.pause()

        $ tmpInt = 52
        python:
            for x in range(0,len(mphone_bios_chars_list)):
                if mphone_bios_chars_list[x][0] == "Nick":
                    tmpInt = x + 1
        $ mphone_bios_chars_list.insert(tmpInt,["Nikita",[1],bios_txt_nikita,mbios_history_nikita,0])
        $ new_bio("Nikita", "I approached Nikita in class after learning her name from Derek. She seems to enjoy the attention she gets from me.")
else:
    scene ep12_lclass21 with dissolve
    mc "Yeah... Hang in there."
    mc "Sec, I'm gonna have a word with Sally."
scene ep12_lclass36 with dissolve
mc "No need to look bored. Class hasn't started yet."
scene ep12_lclass38 with dissolve
sy "*{i}Groans{/i}* That's the problem! I want the day to end so I can get the hell out of here."
sy "First class and then lab... It's finals week! Have they gone mad, or do they hate their students?"
scene ep12_lclass37 with dissolve
mc "Yeah, I know. It stinks. But what are you gonna do?"
mc "I'll pull some extra weight during lab class, if you want."
scene ep12_lclass39 with dissolve
$ renpy.pause()
scene ep12_lclass40 with dissolve
sy "Did you even have time to prepare for it?"
scene ep12_lclass39 with dissolve
mc "Not a lot."
scene ep12_lclass40 with dissolve
sy "I'm sure we'll figure it out together."
scene ep12_lclass41 with dissolve
mc "Awesome! That's the spirit."
scene ep12_lclass42 with dissolve
sy "What are you doing?"
scene ep12_lclass41 with dissolve
mc "Never did a fist bump before?"
play sound "sound_effects/season2/fistbump.mp3"
scene ep12_lclass43 with vpunch
mc "Yeah! There you go."
scene ep12_lclass39 with dissolve
mc "How about sitting in the back with Derek and me?"
scene ep12_lclass40 with dissolve
sy "Why all the way in the back?"
scene ep12_lclass39 with dissolve
mc "It beats sitting alone and up front."
scene ep12_lclass40 with dissolve
sy "Thanks for the offer, but I'm already settled in. Maybe next time."

scene ep12_lclass46 with dissolve
te5 "Good afternoon, class. I hope we are in good spirits for the final class before winter break."
if ep12_nikita:
    scene ep12_lclass44b with dissolve
else:
    scene ep12_lclass44 with dissolve
li "Professor? Did you talk to Dr. Jenkins about my banishment yet?"
scene ep12_lclass47 with dissolve
te5 "Let's have this conversation after class, ok?"
if ep12_nikita:
    scene ep12_lclass45b with dissolve
else:
    scene ep12_lclass45 with dissolve
li "What she's doing is called power abuse."
scene ep12_lclass47 with dissolve
te5 "Leave it for after class, Linda."
scene ep12_lclass48 with dissolve
de "*{i}Yawns{/i}* Wake me up when he's done."
if not (ep10_cathy_lewd and ep11_jade_lewd):
    stop music fadeout 3
scene ep12_lclass49 with dissolve
mc "*{i}Yawns{/i}* Stop yawning; it's contagious."

if ep10_cathy_lewd and ep11_jade_lewd:
    hide screen new_phone_screen
    $ mphone_contact_list.insert(1,["Cathy","NONE",False])
    $ mphone_chat_history_list.insert(1,["Cathy",0,[],[]," ",0])
    play sound "sound_effects/season2/vibrate.mp3"
    scene ep12_lclass50 with dissolve
    "*{i}Phone vibrates{/i}*"
    $ tmpInt = 0
    $ tmpInt2 = 0
    $ text_message_screen_list = []
    $ text_message_screen_list.append(["Cathy","Hi, [name]. This is Cathy.",True])
    $ text_message_screen_list.append(["%s" % name,"Hi! This was a surprise.",False])
    $ text_message_screen_list.append(["Cathy","I hope my text didn't alarm you. I talked to Jade, and I wanted to reach out.",True])
    $ text_message_screen_list.append(["%s" % name,"How so?",False])
    $ text_message_screen_list.append(["Cathy","It's a conversation I'd rather have in person. Are you free later tonight? mphone_emoji_kiss",True])
    scene ep12_lclass51 with dissolve
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    scene ep12_lclass50 with dissolve
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()

    $ tmpInt2 = len(text_message_screen_list)
    hide screen text_message_screen
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_lclass52 with dissolve
        mc "(Hm... I think I know what this is about.)"
        $ text_message_screen_list.append(["%s" % name,"I hope this isn't too direct or presumptuous, but I'm sort of in a relationship now. If the meeting is of that nature, I can't come.",False])
        $ text_message_screen_list.append(["Cathy","Oh? Jade didn't mention that. I'm sorry.",True])
        $ text_message_screen_list.append(["%s" % name,"Don't worry about it. It's recent, but yeah, I'm no longer available.",False])
        $ text_message_screen_list.append(["Cathy","Thanks for the honest answer, [name].",True])
    else:
        $ text_message_screen_list.append(["%s" % name,"I'm in town for science class all afternoon. I'm free after 6 p.m., maybe earlier.",False])
        $ text_message_screen_list.append(["Cathy","In town, you say. How about if you drop by my office after? It should be close by.",True])
        scene ep12_lclass51 with dissolve
        $ text_message_screen_list.append(["%s" % name,"Sure! I'll call you when I get out of class.",False])
        $ text_message_screen_list.append(["Cathy","Splendid. I'll send you the address.",True])
    $ tmpInt += 1
    show screen text_message_screen
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    $ tmpInt += 1
    $ renpy.pause()
    hide screen text_message_screen
    $ mphone_scene_to_chat("Cathy",text_message_screen_list)
    if branchZoey and not wt_ep11_zoey_kiss_others:
        stop music fadeout 3
        scene ep12_lclass53 with dissolve
        mc "(I'm in a relationship... I haven't even said those words to Zoey yet, but that's how I feel. It feels nice...)"
    else:
        scene ep12_lclass54 with dissolve
        mc "(Hm... Her office. Maybe this isn't about sex after all.)"
        stop music fadeout 3
        mc "(This is going to be a long afternoon...)"
    show screen new_phone_screen

label ep12_lab_label:
play music "music/ep6/licensed_music/track20.mp3"
scene ep12_lab1 with wipeleft
de "To cut a long story and finger short, I'm gonna need you to do most of the work today."
scene ep12_lab4 with dissolve
$ renpy.pause()
scene ep12_lab2 with dissolve
de "Don't give me that look. Have you seen this?"
de "If it were a fake excuse, I would have told you my dog ate my homework or something far-fetched."
scene ep12_lab5 with dissolve
no "Far-fetched? You cut your fingertip off with a sword. A sword!"
scene ep12_lab2 with dissolve
de "Why is that so hard to believe?"
de "Every hour in this country, there are like five people amputating a finger."
de "During this very class that's like 20 people!"
scene ep12_lab3 with dissolve
de "Or 15, if you work fast enough."
scene ep12_lab6 with dissolve
$ renpy.pause()
scene ep12_lab7 with dissolve
no "You can work with Mr. Anderson's group today. Do as much as you can without using your left hand."
if lname == "Anderson":
    scene ep12_lab8 with dissolve
    de "With [name]?"
else:
    scene ep12_lab9 with dissolve
    de "With who!?"
scene ep12_lab10 with dissolve
olv "She means me."

if ep12_nikita:
    scene ep12_lab11 with dissolve
    $ renpy.pause()
    scene ep12_lab12 with dissolve
    $ renpy.pause()
    scene ep12_lab13 with dissolve
    mc "Here you go."
    scene ep12_lab14 with dissolve
    nik "Thank you."
    scene ep12_lab15 with dissolve
    $ renpy.pause()
    scene ep12_lab16 with dissolve
    nik "So..."
    nik "What's your last name?"
    scene ep12_lab21 with dissolve
    $ renpy.pause()
    scene ep12_lab17 with dissolve
    mc "It's [lname]."
    scene ep12_lab18 with dissolve
    nik "Wow. You gave that up easily."
    scene ep12_lab17 with dissolve
    mc "You should try it."
    scene ep12_lab19 with dissolve
    nik "Yeah. Maybe next time."
    scene ep12_lab17 with dissolve
    mc "Great. In that case..."
    mc "What's your phone number?"
    scene ep12_lab20 with dissolve
    nik "Haha!"
    scene ep12_lab22 with dissolve
    $ renpy.pause()
    scene ep12_lab23 with dissolve
    sy "Um... Earth to [name]. Hello?"
    scene ep12_lab24 with dissolve
    mc "What?"
    scene ep12_lab25 with dissolve
    sy "You can ogle girls after class. Some of us need to get the hell out of here."
    scene ep12_lab26 with dissolve
    mc "Jealous much?"
    scene ep12_lab27 with dissolve
    sy "Yeah, I am so jealous. Please, [name]! Look at my ass."
    if affinity == "DIK":
        scene ep12_lab29 with dissolve
        sy "Stop looking at my ass."
        scene ep12_lab28 with dissolve
        mc "You're sending me mixed signals here, Sally."
    else:
        scene ep12_lab28 with dissolve
        if affinity == "CHICK":
            mc "I don't think you mean that."
        else:
            mc "You can't see much with the lab coat on anyway."
    scene ep12_lab30 with dissolve
    sy "Can we do this or what?"
    scene ep12_lab26 with dissolve
    mc "Sure. I've got the chemicals right here."
else:
    scene ep12_lab30 with dissolve
    sy "Hey, [name]? Can we get started already?"
    scene ep12_lab26 with dissolve
    mc "Sure. I've got the chemicals right here."

if minigames:
    $ sm_init_mg(3)
    $ qM = quick_menu
    $ quick_menu = 0
    $ renpy.block_rollback()
    hide screen new_phone_screen
    $ science_jump_label = "science_game_end_ep12_label"
    scene science_minigame_neutral with dissolve
    jump sm_setup_experiment_ep12_label

    label science_game_end_ep12_label:
    $ renpy.block_rollback()
    $ quick_menu = qM
    show screen new_phone_screen
    hide screen science_screen
    $ sm_play_stirrer_stop()
    scene ep12_after_lab1 with dissolve
    hide screen wt_science_cheat3
else:
    scene ep12_after_lab1 with wipeleft
sy "Is that it? Are we done?"
scene ep12_after_lab2 with dissolve
mc "Unless there's another page of the experiment, this is our product."
scene ep12_after_lab3 with dissolve
sy "Finally! Let's assess the purity."
scene ep12_after_lab4 with dissolve
no "Do you need my assistance?"
scene ep12_after_lab5 with dissolve
sy "No, we know how to do it."
play sound "sound_effects/season3/bn_click.mp3"
scene ep12_after_lab6 with dissolve
sy "Please, be good... I don't need more stress in my life."
scene ep12_after_lab7 with dissolve
mc "Me neither."
scene ep12_after_lab8 with dissolve
sy "I have an exam tomorrow, how about you?"
scene ep12_after_lab7 with dissolve
mc "Both my tests are on Friday."
scene ep12_after_lab9 with dissolve
sy "On a Friday? And both? That's sadistic!"
scene ep12_after_lab7 with dissolve
mc "It's not always going to be like that, right?"
scene ep12_after_lab8 with dissolve
sy "It shouldn't even be like that in the first place. Most of the tests I've had were on different days."
play sound "sound_effects/season2/beep.mp3"
scene ep12_after_lab10 with dissolve
"*{i}Machine beeps{/i}*"

if not minigames and affinity != "DIK":
    $ ep11_chem_status += 4
if (minigames and sm_purity == 0) or (not minigames and affinity == "DIK"):
    scene ep12_after_lab11 with dissolve
    sy "What the hell, [name]!? This is shit."
    scene ep12_after_lab12 with dissolve
    mc "Oof... Yeah. We suck."
else:
    if minigames:
        if sm_purity <= 50:
            scene ep12_after_lab13 with dissolve
            sy "[sm_purity]%%? That's so bad."
            scene ep12_after_lab12 with dissolve
            mc "Oof... Yeah. It could be better."
        else:
            if sm_purity < 75:
                $ ep11_chem_status += 1
                scene ep12_after_lab13 with dissolve
                sy "[sm_purity]%%? Eh... I'll take it."
                scene ep12_after_lab14 with dissolve
                mc "Yeah, I consider that a win."
            else:
                scene ep12_after_lab16 with dissolve
                sy "[sm_purity]%% pure! We did it!"
                scene ep12_after_lab17 with dissolve
                mc "Awesome work, Sally. The report on this is going to write itself."
                scene ep12_after_lab15 with dissolve
                sy "Yeah, at least we won't have to figure out what went wrong."
                $ ep11_chem_status += 2
                if steamAchievements and not config.console and not config.developer:
                    if ep11_chem_status == 6 and sm_hard_mode:
                        $ achievement.grant("IDS3_17")
                        init:
                            $ achievement.register("IDS3_17")
                        $ achievement.Sync()
                if not persistent.ep12_cardisa9:
                    $ persistent.chat_new_rewards = True
                    $ persistent.rew_isa_unlocked += 1
                    $ persistent.ep12_cardisa9 = True
                    $ calcRenders()
                    show screen srmsg
                    $ renpy.pause(3)
                    hide screen srmsg
    else:
        scene ep12_after_lab15 with dissolve
        sy "This is a decent result. I'll take it."
        scene ep12_after_lab14 with dissolve
        mc "Yeah, I consider that a win."

if minigames and sm_purity <= 50:
    scene ep12_after_lab13 with dissolve
    sy "Well, I don't have time to figure out what went wrong today. I need to leave now to study."
    scene ep12_after_lab12 with dissolve
    mc "Make a note of it, and we'll deal with it another day."

scene ep12_after_lab18 with dissolve
sy "Dr. Jenkins? When is the report due?"
scene ep12_after_lab19 with dissolve
no "The first week after winter break is fine."
scene ep12_after_lab21 with dissolve
if sm_purity <= 50:
    sy "At least there's some good news today."
else:
    sy "I can work with that."
sy "Let's pack up and leave."
scene ep12_after_lab20 with dissolve
mc "Hey, you seem to be in a rush. I can clean up after us this time."
scene ep12_after_lab21 with dissolve
sy "Great! I owe you one."
if not ep11_scientist:
    stop music fadeout 3
scene ep12_after_lab20 with dissolve
mc "Good luck with your test tomorrow!"
if not ep11_scientist:
    jump ep12_pre_cathy_label

label ep12_nora_label:
scene ep12_nora21 with dissolve
no "How did it go today, [name]?"
scene ep12_nora22 with dissolve
if (minigames and sm_purity == 0) or (not minigames and affinity == "DIK"):
    mc "Sadly, not too good. It's one of those days..."
    mc "I think finals week is messing with my head."
    scene ep12_nora23 with dissolve
    no "I'm sorry to hear that."
    scene ep12_nora25 with dissolve
else:
    if minigames:
        if sm_purity <= 50:
            mc "It wasn't the best today."
            mc "I think finals week is messing with my head."
            scene ep12_nora23 with dissolve
            no "I'm sorry to hear that."
            scene ep12_nora25 with dissolve
        else:
            if sm_purity < 75:
                mc "We did alright. But I was hoping for a higher purity than [sm_purity]%%."
                scene ep12_nora24 with dissolve
                no "It takes practice and patience to stay consistent in the lab."
                scene ep12_nora25 with dissolve
            else:
                mc "We did great today. We had [sm_purity]%% purity."
                scene ep12_nora25 with dissolve
                no "Impressive. But I'm not surprised. I saw how diligent you were."
    else:
        mc "We did well today, but I think we rushed some steps. Sally was in a hurry because of finals week."
        scene ep12_nora24 with dissolve
        no "It takes practice and patience to stay consistent in the lab."
        scene ep12_nora25 with dissolve

no "Since everyone is done with the experiment early today, I've got some time to show you my lab."
scene ep12_nora26 with dissolve
mc "Your lab?"
scene ep12_nora25 with dissolve
no "That is, if you're still interested in seeing what it's like to work here."
scene ep12_nora26 with dissolve
mc "I am. That would be cool."
stop music fadeout 3
scene ep12_nora27 with dissolve
no "I'll have to make sure everyone leaves class first."
play music "music/ep5/licensed_music/track4.mp3"
scene ep12_nora1 with wipeleft
mc "Is this lab all yours?"
scene ep12_nora2 with dissolve
no "I call it mine because it's where I prepare my samples, but I share it with a couple of fellow scientists."
scene ep12_nora3 with dissolve
no "I use a plethora of instruments, all spread out in different labs, but this is my primary lab - or main hub, as I like to call it."
no "I have responsibilities to keep it tidy and to ensure the equipment is calibrated and functioning."
scene ep12_nora4 with dissolve
mc "There are many new tools for me in here."
scene ep12_nora5 with dissolve
mc "That is a scale, right?"
scene ep12_nora6 with dissolve
no "Correct. It's used when you handle small amounts and need accuracy."
no "You open the lids to add chemicals and then close them during measurements."
scene ep12_nora7 with dissolve
mc "Why don't we use these during our experiments?"
scene ep12_nora2 with dissolve
no "They are more expensive and, in your class, that level of accuracy isn't that important."
no "After students feel more comfortable working in a lab, we let them handle the expensive equipment."
scene ep12_nora8 with dissolve
mc "Oh, cool. Automatic pipettes."
no "Did you ever handle one?"
mc "No, but I've seen them before."
scene ep12_nora2 with dissolve
no "They are also expensive and only used for pipetting small volumes. Smaller than the ones you handle in class."
scene ep12_nora7 with dissolve
mc "How small?"
scene ep12_nora2 with dissolve
no "Microliter to milliliter."
scene ep12_nora7 with dissolve
mc "Wow."
scene ep12_nora9 with dissolve
no "Remember the tubes I told you about last time?"
scene ep12_nora10 with dissolve
mc "The ones with filters in them?"
no "Yes. They can look like this."
no "You fill the inner tube with your sample and put it in a big centrifuge."
scene ep12_nora11 with dissolve
no "Then you centrifuge according to the instructions, and anything larger than the filter's pore size won't pass through."
scene ep12_nora12 with dissolve
mc "That's smart..."
mc "So, what are you working on right now?"
if ep10_dating_nora:
    scene ep12_nora13 with dissolve
    no "During our date, I believe I told you about it..."
scene ep12_nora14 with dissolve
no "I'm working on improving chromatography methods."
no "I use different separation methods and analyze how to improve them."
scene ep12_nora15 with dissolve
no "I employ a wide array of instruments in my studies. Lately, I've been working plenty with gas chromatography, HPLC, and capillary electrophoresis."
no "The plan is to publish three different papers on my findings."
scene ep12_nora16 with dissolve
mc "I wish I could understand what you're talking about."
scene ep12_nora14 with dissolve
no "You will, if you're interested and choose to study more chemistry."
no "I understand that you're confused. I was, too, when I started college."
scene ep12_nora15 with dissolve
no "It sounds harder than it is."
no "Let me explain the basics."
scene ep12_nora17 with dissolve
no "Take this tube, for example. Pretend it contains a sample with different molecules."
no "Be it a perfume, a chemical compound, some drug, or any other mixture you want to analyze."
no "How would you analyze it?"
scene ep12_nora18 with dissolve
mc "I wouldn't know where to begin."
scene ep12_nora17 with dissolve
no "Well, the answer depends on your goal."
no "Do you want to quantify the constituents of the sample, isolate them, or merely identify them?"
scene ep12_nora18 with dissolve
mc "Haha... Still, I don't know."
scene ep12_nora15 with dissolve
no "It was a rhetorical question."
no "The thing is, with chromatography, we can separate the molecules in this sample and study them."
no "Depending on the method we choose, we can purify, identify, and quantify them."
scene ep12_nora14 with dissolve
no "And we do this by exploiting their intrinsic properties."
scene ep12_nora16 with dissolve
mc "And...what does that mean?"
scene ep12_nora15 with dissolve
no "Again, it can mean different things. For instance, molecules can be separated by size, polarity, and charge."
scene ep12_nora16 with dissolve
mc "What's chromatography used for?"
scene ep12_nora19 with dissolve
no "Crime labs, for one, use these methods to pinpoint where drugs come from."
no "If you analyze drug samples, you can compare the results and determine whether the drugs come from the same batch or lab."
no "Even toilet water can be analyzed for traces of drugs."
scene ep12_nora20 with dissolve
no "As you've seen in my class, we can separate compounds to get a higher purity of the desired chemical."
no "This is employed in chemistry and biology."
no "In biology, for instance, you can purify proteins, analyze them at the molecular level, and design drugs to combat disease."
scene ep12_nora15 with dissolve
no "In the food industry, chromatography is a crucial part. It enables analysis of nutrients."
no "I could go on, if you'd like."
scene ep12_nora16 with dissolve
mc "You don't have to do that. I think I understand its importance."
scene ep12_nora14 with dissolve
no "My friends rarely understand what I'm talking about, but I think it's such an exciting field."
scene ep12_nora16 with dissolve
if ep10_dating_nora:
    mc "I was right the first time about you."
    scene ep12_nora15 with dissolve
    no "What do you mean?"
    scene ep12_nora16 with dissolve
    mc "You're passionate about this."
else:
    mc "You seem passionate about this."
scene ep12_nora14 with dissolve
no "I am. And thank you for showing me your interest."
scene ep12_nora16 with dissolve
mc "I'm not gonna lie, this seems like hard work. Like, you have to be really smart to work with this."
mc "But at the same time... It is intriguing. Thanks for showing me this."
$ guideSuggestedPage = 232
if ep10_dating_nora and (not branchZoey or wt_ep11_zoey_kiss_others) and ep10_nora_encourage and ep10_nora_kids:
    label ep12_nora_lewd_label:
    if _in_replay:
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        play music "music/ep5/licensed_music/track4.mp3"
    hide screen new_phone_screen
    scene ep12_nora_lewd1 with dissolve
    $ renpy.pause()
    scene ep12_nora_lewd2 with dissolve
    $ renpy.pause()
    scene ep12_nora_lewd3 with dissolve
    $ renpy.pause()
    scene ep12_nora_lewd10 with dissolve
    no "*{i}Smack{/i}*"
    scene ep12_nora_lewd4 with dissolve
    no "I'm sorry. I shouldn't have done that."
    no "This is not why I brought you here."
    scene ep12_nora_lewd3 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Nora scene)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if ep10_cathy_lewd and ep11_jade_lewd and (not branchZoey or wt_ep11_zoey_kiss_others):
                           $ mod_choices[4]="(Skips Cathy scene)"
    
    menu:
        "Mod: Nora and Cathy scenes" if ep10_cathy_lewd and ep11_jade_lewd and (not branchZoey or wt_ep11_zoey_kiss_others):
            $ wt_ep12_nora_cathy=True
            jump wt_ep12_nora_scene
        "Kiss her \n{size=-4}[m_c1][mod_choices[0]][m_c2][mod_choices[4]]" :
            label wt_ep12_nora_scene:
            $ ep12_nora_state = 2
            stop music fadeout 3
            scene ep12_nora_lewd5 with dissolve
            mc "It's not why I followed either."
            mc "But that doesn't mean I don't want it..."
            play music "music/ep6/licensed_music/track34.mp3"
            scene anim_nora_kiss_ep12 with dissolve
            mc "*{i}Smack{/i}*"
            no "*{i}Smack{/i}* Mmm... [name]."
            pause
            scene ep12_nora_lewd11 with dissolve
            no "Wait... Wait."
            scene ep12_nora_lewd12 with dissolve
            mc "*{i}Smack{/i}* What?"
            scene ep12_nora_lewd11 with dissolve
            no "I can't do this. I can't date a student."
            scene ep12_nora_lewd12 with dissolve
            mc "You don't have to date me. Let us have this moment together."
            scene ep12_nora_lewd13 with dissolve
            no "Will you be able to leave it at that?"
            scene ep12_nora_lewd14 with dissolve
            mc "It's up to you. You're the one who didn't want me."
            scene ep12_nora_lewd13 with dissolve
            no "[name]. I never said I didn't want you. I said I wasn't willing to risk my job."
            no "And here I am... Fooling around with you at my workplace."
            scene ep12_nora_lewd14 with dissolve
            mc "I get it, and I respect it if you ask me to, but it doesn't change anything for me."
            scene ep12_nora_lewd13 with dissolve
            no "Maybe... Just one more moment together."
            scene anim_nora_kiss_ep12 with dissolve
            pause
            scene ep12_nora_lewd15 with dissolve
            $ renpy.pause()
            play sound "sound_effects/clothes.mp3"
            scene ep12_nora_lewd16 with dissolve
            mc "What abour your coworkers?"
            scene ep12_nora_lewd17 with dissolve
            no "No one will show up at this time."
            no "They are busy working on a paper, and they won't use the lab until they're done with that."
            scene ep12_nora_lewd18 with dissolve
            no "But no loud moans. People could be walking in the corridors."
            scene ep12_nora_lewd19 with dissolve
            mc "Roger that."
            scene ep12_nora_lewd20 with dissolve
            $ renpy.pause()
            scene ep12_nora_lewd21 with dissolve
            mc "Fuck, I've missed your big and beautiful tits."
            scene ep12_nora_lewd22 with dissolve
            no "They have missed you, too."
            scene ep12_nora_lewd23 with dissolve
            menu:
                "Fondle them":
                    label ep12_nora_lewd_tits_label:
                    scene anim_nora_tits_ep12 with dissolve
                    pause
                    scene anim_nora_titsb_ep12 with dissolve
                    pause
                    menu:
                        "Lick them":
                            jump ep12_nora_lewd_tits2_label
                        "Continue":
                            jump ep12_nora_lewd_tits3_label
                "Lick them":
                    label ep12_nora_lewd_tits2_label:
                    scene anim_nora_tits2_ep12 with dissolve
                    pause
                    menu:
                        "Fondle them":
                            jump ep12_nora_lewd_tits_label
                        "Continue":
                            jump ep12_nora_lewd_tits3_label
            label ep12_nora_lewd_tits3_label:
            scene ep12_nora_lewd24 with dissolve
            mc "Have you ever done it in here before?"
            scene ep12_nora_lewd25 with dissolve
            no "*{i}Suck suck{/i}* No. Never."
            scene ep12_nora_lewd24 with dissolve
            mc "Is it safe to do it in here?"
            scene ep12_nora_lewd26 with dissolve
            no "*{i}Moans{/i}* I already told you no one will show up."
            mc "I didn't mean it that way."
            no "Fuck... Hngn..."
            scene ep12_nora_lewd27 with dissolve
            no "Oh, you're talking about lab safety. I always clean the lab before and after use."
            no "Even so, we should be somewhat careful."
            scene ep12_nora_lewd28 with dissolve
            mc "*{i}Smack{/i}*"
            no "Let's avoid surfaces with lab equipment on them."
            scene ep12_nora_lewd29 with dissolve
            mc "Is this chair ok?"
            scene ep12_nora_lewd30 with dissolve
            no "Mhm..."
            scene ep12_nora_lewd31 with dissolve
            no "And there it is... Exactly how I remembered it."
            scene ep12_nora_lewd32 with dissolve
            no "*{i}Smack{/i}*"
            scene anim_nora_bj1_ep12 with dissolve
            mc "There you go... Put your lips around it."
            no "*{i}Suck suck glug glug{/i}*"
            pause
            scene ep12_nora_lewd33 with dissolve
            mc "You're so good at that."
            scene anim_nora_bj2_ep12 with dissolve
            mc "(Fuck, she's sucking on it so hard with a perfect rhythm.)"
            no "*{i}Suck suck{/i}*"
            pause
            scene ep12_nora_lewd34 with dissolve
            no "Fuck, [name]. Come over here... I want you inside me."
            no "I want you to penetrate me hard, and I want it now."
            scene ep12_nora_lewd35 with dissolve
            no "Mmm... Give that cock to me."
            scene ep12_nora_lewd36 with dissolve
            no "Yes! Give it..."
            scene bg anim_nora_insert_ep12 movie with dissolve
            no "*{i}Moans{/i}* Yes! Go slow, [name]..."
            pause
            scene anim_nora_miss1_ep12 with dissolve
            mc "Your pussy is so wet that it slid right in there."
            no "*{i}Moans{/i}* Fuck me, [name]. Fuck me good."
            pause
            scene anim_nora_miss2_ep12 with dissolve
            pause
            scene anim_nora_miss3_ep12 with dissolve
            pause

            $ tmpInt = 0
            $ tmpBool3 = False
            label ep11_nora_lewd_loop_label:
            menu:
                "Facing on chair":
                    $ tmpInt += 1
                    scene anim_nora_miss1_ep12 with dissolve
                    no "Give me that dick, [name]."
                    mc "How much do you want it?"
                    no "Against my better judgment, I'm fucking you in here. That should tell you how much I want it."
                    pause
                    scene anim_nora_miss2_ep12 with dissolve
                    mc "Fuck, you feel so good."
                    pause
                    scene anim_nora_miss3_ep12 with dissolve
                    no "*{i}Moans{/i}*"
                    pause
                    jump ep11_nora_lewd_loop_label
                "Doggystyle":
                    $ tmpInt += 1
                    scene anim_nora_doggy1_ep12 with dissolve
                    no "Take me from behind, [name]. Pound me."
                    mc "Damn... Your ass slapping against me like that makes it hard to hold it back."
                    pause
                    scene anim_nora_doggy2_ep12 with dissolve
                    no "Please, not yet. Try not to cum. I want more."
                    mc "You're making it hard, Nora."
                    pause
                    scene anim_nora_doggy3_ep12 with dissolve
                    pause
                    jump ep11_nora_lewd_loop_label
                "From behind":
                    $ tmpInt += 1
                    scene anim_nora_stand1_ep12 with dissolve
                    if not tmpBool3:
                        no "Ahh... I'm so close."
                        mc "Are you gonna cum from this?"
                        no "Mhm.. I think I am. Fuck me harder, [name]."
                    else:
                        no "Fuck me harder, [name]."
                    pause
                    scene anim_nora_stand2_ep12 with dissolve
                    if not tmpBool3:
                        $ tmpBool3 = True
                        no "Hnnn... Ahhh..."
                        scene ep12_nora_lewd37 with vpunch
                        no "*{i}Moans{/i}* Ahhh!"
                        scene ep12_nora_lewd38 with vpunch
                        no "*{i}Moans{/i}* Oh, [name]..."
                        scene ep12_nora_lewd39 with vpunch
                        no "Fuck! *{i}Exhales{/i}*"
                        scene ep12_nora_lewd38 with dissolve
                        no "I'm trembling... Wow..."
                    else:
                        pause
                    jump ep11_nora_lewd_loop_label
                "Cowgirl":
                    $ tmpInt += 1
                    scene anim_nora_ride1_ep12 with dissolve
                    mc "Ride me, Nora. It's so fucking hot being ridden by my sexy teacher."
                    no "Mmm... You're talking too dirty, [name]."
                    mc "Do you want me to dial it back?"
                    no "No... Tell me more."
                    pause
                    scene anim_nora_ride2_ep12 with dissolve
                    mc "You're so fucking naughty doing this with your student."
                    mc "20 minutes ago you were in class as my teacher, and now you're bouncing up and down on my cock like this..."
                    no "Yes, I am naughty. And I'm horny for you, [name]."
                    no "You're making me want to break all kinds of rules."
                    pause
                    jump ep11_nora_lewd_loop_label
                "Reverse cowgirl":
                    $ tmpInt += 1
                    scene anim_nora_rev1_ep12 with dissolve
                    mc "There's that hot ass again... I fucking love it."
                    no "*{i}Moans{/i}*"
                    pause
                    scene anim_nora_rev2_ep12 with dissolve
                    no "I love riding your hard cock. It fills me up so good."
                    pause
                    jump ep11_nora_lewd_loop_label
                "Titty fuck":
                    $ tmpInt += 1
                    scene anim_nora_tf1_ep12 with dissolve
                    mc "I love your big, soft tits."
                    no "Fuck them, [name]."
                    pause
                    scene anim_nora_tf2_ep12 with dissolve
                    no "Yes... Don't hold anything back. Please yourself with my breasts."
                    no "Fuck them... They're yours."
                    pause
                    jump ep11_nora_lewd_loop_label
                "Cum" if tmpInt > 2:
                    mc "I'm so close. I don't think I can hold it back any longer."
                    menu:
                        "Creampie":
                            scene anim_nora_rev2_ep12 with dissolve
                            no "Then cum inside me, [name]. I want your seed."
                            pause
                            scene ep12_nora_lewd42 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd42 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd42 at vpunch, cum1
                            mc "Fuck... I'm cumming. Ah..."
                            scene ep12_nora_lewd43 with dissolve
                            $ renpy.pause()
                            scene ep12_nora_lewd44 with dissolve
                            $ renpy.pause()
                        "On pussy and belly":
                            scene anim_nora_miss2_ep12 with dissolve
                            no "Cum all over my pussy, [name]. Unload on me."
                            pause
                            scene ep12_nora_lewd45 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd45 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd45 at vpunch, cum2
                            mc "Hnnn... Fuck!"
                            scene ep12_nora_lewd46 with dissolve
                            $ renpy.pause()
                        "On tits":
                            scene anim_nora_tf2_ep12 with dissolve
                            no "Shoot it all over my tits, [name]. Cover my breasts with your cum."
                            scene ep12_nora_lewd40 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd40 at vpunch, cum2
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd40 at vpunch, cum2
                            mc "Hnnn... Fuck!"
                            scene ep12_nora_lewd41 with dissolve
                            $ renpy.pause()
                        "In mouth":
                            scene anim_nora_ff_ep12 with dissolve
                            no "*{i}Suck suck glug glug{/i}*"
                            mc "I'm cumming!"
                            scene ep12_nora_lewd47 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd47 at vpunch, cum1
                            $ renpy.pause(0.5)
                            scene ep12_nora_lewd47 at vpunch, cum1
                            mc "Hnnn... Fuck!"
                            scene ep12_nora_lewd48 with dissolve
                            no "*{i}Gasps{/i}* Wow... Mmm..."

                    scene ep12_nora_lewd49 with Dissolve(3)
                    $ renpy.pause()
                    scene ep12_nora_lewd50 with dissolve
                    $ renpy.pause()
                    scene ep12_nora_lewd51 with dissolve
                    mc "All good?"
                    scene ep12_nora_lewd52 with dissolve
                    no "Affirmative. You?"
                    scene ep12_nora_lewd51 with dissolve
                    mc "Yep."
                    scene ep12_nora_lewd52 with dissolve
                    no "I'll be walking this way."
                    scene ep12_nora_lewd51 with dissolve
                    mc "I'll see you after winter break, Dr. Jenkins."
                    stop music fadeout 3
                    scene ep12_nora_lewd53 with dissolve
                    no "..."
                    $ renpy.end_replay()
                    $ persistent.ep12_lewd_nora = True
                    $ calcScenes()
                    $ new_bio("Nora", "Nora showed me her lab. What started out as a genuine interest in her work ended up with her on top of me.")
                    $ mphone_stats_add_girl_s3("nora","You had sex with Nora in her lab in episode 12.")
        "Reject Nora" if not _in_replay:
            $ ep12_nora_state = 1
            scene ep12_nora_lewd5 with dissolve
            mc "It's fine. You got caught up in the moment."
            mc "You were right about everything you said in our phone call."
            scene ep12_nora_lewd6 with dissolve
            mc "We shouldn't get involved more. It's too complicated."
            scene ep12_nora_lewd9 with dissolve
            no "You're right. Please, forget I did that."
            scene ep12_nora_lewd7 with dissolve
            mc "Already forgotten."
            mc "Thanks for showing me your lab."
            stop music fadeout 3
            scene ep12_nora_lewd8 with dissolve
            no "You're welcome."
            $ new_bio("Nora", "Nora showed me her lab. She tried to rekindle something between us, but I shut it down.")
            show screen new_phone_screen
else:
    stop music fadeout 3
    scene ep12_nora19 with dissolve
    no "You're welcome. Perhaps there's a future for you waiting in a lab somewhere."
    $ new_bio("Nora", "Nora showed me her lab. I was genuinely interested in learning what it was like to work in a lab environment.")

label ep12_pre_cathy_label:
if ep10_cathy_lewd and ep11_jade_lewd and (not branchZoey or wt_ep11_zoey_kiss_others):
    if ep12_nora_state == 2 and not wt_ep12_nora_cathy:
        scene ep12_nora_lewd54 with dissolve
        mc "(Oh... I've got a couple of missed phone calls from Cathy...)"
        mc "(And texts too...)"
        hide screen new_phone_screen

        $ tmpInt = 2
        $ tmpInt2 = 0
        $ text_message_screen_list = []
        $ text_message_screen_list.append(["Cathy","Was there a change of plans?",True])
        $ text_message_screen_list.append(["Cathy","[name]? Hello?",True])
        $ text_message_screen_list.append(["Cathy","I'm guessing you got held up. I'm heading back home. Let's reschedule.",True])
        $ text_message_screen_list.append(["%s" % name,"Hi. Yeah, something else came up. I'm sorry, but I missed your calls.",False])
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ mphone_scene_to_chat("Cathy",text_message_screen_list)
        show screen new_phone_screen
        scene ep12_nora_lewd55 with dissolve
        mc "(Oh, well... It was worth it.)"
        $ new_bio("Cathy", "I chose to have sex with Nora instead of going to visit Cathy.")
        jump ep12_jblog_label
    else:
        show screen new_phone_screen
        jump ep12_cathy_label
else:
    jump ep12_jblog_label

label ep12_cathy_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_cathy == None:
        $ mc_cathy = name
    else:
        $ mc_cathy = persistent.mc_cathy
    if persistent.cathy == None:
        $ cathy = "Cathy"
    else:
        $ cathy = persistent.cathy
    if persistent.mc_jade == None:
        $ mc_jade = name
    else:
        $ mc_jade = persistent.mc_jade
    if persistent.jade == None:
        $ jade = "Jade"
    else:
        $ jade = persistent.jade
hide screen new_phone_screen
$ guideSuggestedPage = 232
play music "music/ep7/good_old_days.mp3"
scene ep12_cathy1 with wipeleft
ca "Ah, [name]. Welcome. Did you find the place ok?"
scene ep12_cathy2 with dissolve
mc "I did. So, this is where you work?"
scene ep12_cathy3 with dissolve
ca "Yes and no. I have my office on this floor, but I have to work out of the office too."
scene ep12_cathy4 with dissolve
mc "Yeah? Do you get to travel?"
scene ep12_cathy3 with dissolve
ca "Not yet, but I see it in my future. Lately, I've been working with local businesses, so I wouldn't call it traveling."
ca "It's more or less like commuting."
ca "Many meetings and assignments are digital too."
scene ep12_cathy5 with dissolve
ca "Come, let me show you my office."
scene ep12_cathy6 with dissolve
ca "Oh! Most have already left for the day, but if anyone asks... You're a potential junior-level candidate."
scene ep12_cathy7 with dissolve
mc "Uh... Sure. Whatever that means."
scene ep12_cathy6 with dissolve
ca "Leave the talking to me and nod along."
label ep12_cathy_lewd_label:
scene ep12_cathy_lewd1 with wiperight
mc "Nice view!"
scene ep12_cathy_lewd2 with dissolve
ca "It's quite something, isn't it?"
scene ep12_cathy_lewd3 with dissolve
mc "I wouldn't mind having an office like this. That's for sure."
scene ep12_cathy_lewd4 with dissolve
mc "So, how are you?"
scene ep12_cathy_lewd5 with dissolve
ca "*{i}Sigh{/i}* I'm happy you showed up. It's been a long day of meetings."
scene ep12_cathy_lewd7 with dissolve
mc "I was curious about what you wanted, and it's always nice to catch up."
scene ep12_cathy_lewd6 with dissolve
ca "Can I get you some coffee?"
scene ep12_cathy_lewd7 with dissolve
mc "No, thanks."
scene ep12_cathy_lewd5 with dissolve
ca "Well... Where do I start?"
scene ep12_cathy_lewd8 with dissolve
mc "You tell me. What's on your mind?"
scene ep12_cathy_lewd9 with dissolve
ca "I'm trying to think of a way to put this eloquently, but I'm drawing a blank."
scene ep12_cathy_lewd10 with dissolve
mc "Then say it. I'm not that eloquent myself."
scene ep12_cathy_lewd11 with dissolve
ca "That's fair."
ca "I've talked to Jade and learned more about her situation."
ca "Among the details she shared, I learned things about you."
scene ep12_cathy_lewd12 with dissolve
ca "Apparently... Jade and I had a mutual interest, if you catch my drift."
scene ep12_cathy_lewd13 with dissolve
mc "Yeah, I think I do. What can I say? Things have happened."
scene ep12_cathy_lewd12 with dissolve
ca "And as I gather, the \"things\" are still ongoing. Correct?"
scene ep12_cathy_lewd13 with dissolve
mc "Well... I'm not sure."
scene ep12_cathy_lewd14 with dissolve
ca "Then what would you call this?"
scene ep12_cathy_lewd15 with dissolve
mc "She sent you that picture?"
scene ep12_cathy_lewd16 with dissolve
ca "She was teasing me with it."
ca "And admittedly, it worked. I was thoroughly teased."
scene ep12_cathy_lewd15 with dissolve
mc "I didn't realize you two had that close of a relationship."
scene ep12_cathy_lewd17 with dissolve
ca "Jade and I talk about everything."
scene ep12_cathy_lewd18 with dissolve
mc "Everything?"
scene ep12_cathy_lewd17 with dissolve
ca "I believe so."
scene ep12_cathy_lewd18 with dissolve
mc "Then, she knows what you and I did, too?"
scene ep12_cathy_lewd17 with dissolve
ca "Yes, she does."
scene ep12_cathy_lewd18 with dissolve
mc "Did she take it the wrong way?"
scene ep12_cathy_lewd19 with dissolve
ca "No. In fact, we bonded over it, and it led to that picture."
scene ep12_cathy_lewd18 with dissolve
mc "Oh? I'm happy there weren't any bad feelings then."
scene ep12_cathy_lewd19 with dissolve
ca "What would you say to teasing Jade back?"
scene ep12_cathy_lewd18 with dissolve
mc "Why?"
scene ep12_cathy_lewd19 with dissolve
ca "I think she'd enjoy it."
scene ep12_cathy_lewd18 with dissolve

if persistent.mod_wtenabled: 
                        $mod_choices = ["(Cathy scene)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if ep10_cathy_lewd and ep11_jade_lewd and not branchZoey:
                           $ mod_choices[4]="(Skips Cathy scene)"

menu:
    "Accept offer \n{size=-4}[m_c1][mod_choices[0]]":
        $ ep12_cathy_lewd = True
        stop music fadeout 3
    "Decline offer" if not _in_replay:
        scene ep12_cathy_lewd23 with dissolve
        mc "I see where this is going... But I'm gonna have to say no."
        scene ep12_cathy_lewd20 with dissolve
        ca "Aw, [name]. How disappointing."
        scene ep12_cathy_lewd21 with dissolve
        mc "I didn't intend to come in between friends - or whatever this is. I think it's for the best that I don't participate."
        mc "Also, I don't want to jeopardize your job by doing something in here."
        mc "No hard feelings."
        scene ep12_cathy_lewd22 with dissolve
        ca "Of course, [name]. No hard feelings."
        scene ep12_cathy_lewd20 with dissolve
        ca "*{i}Sigh{/i}*"
        ca "Well, then all that's left is to ask you to keep this conversation to yourself."
        scene ep12_cathy_lewd21 with dissolve
        mc "You got it. My lips are sealed. I'll see myself out."
        stop music fadeout 3
        scene ep12_cathy_lewd24 with dissolve
        $ renpy.pause()
        $ new_bio("Cathy", "I rejected Cathy's advances at her office.")
        jump ep12_jblog_label

mc "And how would we do that?"
play music "music/ep3/dc_love_go_go.mp3"
scene ep12_cathy_lewd25 with dissolve
ca "Are you up to taking some pictures?"
scene ep12_cathy_lewd26 with dissolve
mc "Possibly. But... Do you mean in here?"
scene ep12_cathy_lewd25 with dissolve
ca "Thrilling, isn't it?"
scene ep12_cathy_lewd26 with dissolve
mc "What about the windows?"
scene ep12_cathy_lewd27 with dissolve
ca "Those are one-way windows. You can't see in here from the outside."
scene ep12_cathy_lewd23 with dissolve
mc "Uh... And what about the door?"
scene ep12_cathy_lewd28 with dissolve
ca "I can push a button to indicate I'm in a meeting..."
ca "And no one will disturb us."
scene ep12_cathy_lewd27 with dissolve
ca "You can lock the door if you're still nervous."
scene ep12_cathy_lewd29 with dissolve
mc "It's hot seeing you take charge and be confident like this, but yeah, I think I will lock it."
scene ep12_cathy_lewd30 with dissolve
mc "What kind of photos did you have in mind?"
scene ep12_cathy_lewd31 with dissolve
ca "I've been thinking all afternoon about what I want from you."
ca "I'd love to take a picture of you going down on me behind this desk."
scene ep12_cathy_lewd32 with dissolve
ca "Are you up for it?"
scene ep12_cathy_lewd33 with dissolve
mc "Try to stop me."
scene ep12_cathy_lewd34 with dissolve
mc "Show me that sexy underwear..."
scene ep12_cathy_lewd35 with dissolve
mc "Fuck, that's hot!"
scene ep12_cathy_lewd36 with dissolve
$ renpy.pause()
scene ep12_cathy_lewd37 with dissolve
mc "*{i}Lick lick{/i}*"
ca "*{i}Moans{/i}* I want to feel that tongue directly against my pussy."
scene ep12_cathy_lewd38 with dissolve
mc "*{i}Lick lick{/i}* Now you know how I feel about condoms."
scene ep12_cathy_lewd39 with dissolve
ca "Newsflash: Women feel that way, too."
scene ep12_cathy_lewd40 with dissolve
mc "There it is... That looks delicious."
scene ep12_cathy_lewd41 with dissolve
ca "Are you going to eat it?"
scene ep12_cathy_lewd42 with dissolve
mc "Oh, I've got this. You worry about that camera."
scene anim_cathy_lick_ep12 with dissolve
mc "*{i}Lick lick{/i}*"
ca "*{i}Moans{/i}*"
pause
scene anim_cathy_lick3_ep12 with dissolve
mc "Are you shooting?"
ca "Yes, I figured I'd record it."
mc "Whatever works. *{i}Lick lick{/i}*"
pause
scene ep12_cathy_lewd43 with dissolve
ca "(Let's see how she likes this...)"
scene anim_cathy_lick2_ep12 with dissolve
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Jade","No way. You didn't!",False])
$ text_message_screen_list.append(["Cathy","We're still doing it. His tongue feels amazing swirling around my clit. mphone_emoji_tongue",True])
$ text_message_screen_list.append(["Jade","Video chat?",False])
$ text_message_screen_list.append(["Cathy","If you're in private.",True])
pause
show screen text_message_screen
play sound "sound_effects/interlude/zoey_message.mp3"
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
play sound "sound_effects/cellphone.mp3"
scene ep12_cathy_lewd44 with dissolve
"*{i}Phone rings{/i}*"
ca "Jade invited me to a video chat. She wants to see you do it. Is that ok?"
scene ep12_cathy_lewd45 with dissolve
mc "Uh... How do I respond to that? Do you think it's ok?"
scene ep12_cathy_lewd44 with dissolve
ca "I wouldn't have asked you if I didn't."
scene ep12_cathy_lewd45 with dissolve
mc "Then go ahead."
scene ep12_cathy_lewd46 with dissolve
ja "{i}Are you two for real?{/i}"
scene ep12_cathy_lewd47 with dissolve
ca "I believe we are."
scene ep12_cathy_lewd46 with dissolve
ja "{i}I'm happy I caught you two going at it. I wouldn't want to miss this.{/i}"
ja "{i}Switch cameras and show him doing it.{/i}"
scene anim_cathy_lick2_ep12 with dissolve
ca "Can you see him?"
ja "{i}Oh, yes. There he is... That naughty, naughty boy...{/i}"
ca "*{i}Moans{/i}*"
ja "{i}Aren't you going to say hi to me, [mc_jade]?{/i}"
scene ep12_cathy_lewd48 with dissolve
mc "Hi, [jade]..."
scene anim_cathy_lick2_ep12 with dissolve
ja "{i}Don't let me interrupt. Show me how you handle him.{/i}"
ca "What do you want to see?"
ja "{i}Show me how you suck his cock. And make it sloppy.{/i}"
scene ep12_cathy_lewd49 with dissolve
ca "Here. Hold this."
scene anim_cathy_bj1_ep12 with dissolve
ca "*{i}Suck suck{/i}*"
ja "{i}Yes, that's what I want to see. Mmm...{/i}"
pause
scene ep12_cathy_lewd49b with dissolve
ja "{i}Here's some visual stimuli for you, [mc_jade]...{/i}"
scene anim_cathy_bj2_ep12 with dissolve
mc "Fuck me... This is too hot."
ca "*{i}Suck glug{/i}* What is she up to?"
mc "She's showing me her tits. It's like we're having a digital threesome ."
ja "{i}Mmm... I like the sound of that. I've never had a digital threesome before.{/i}"
ja "{i}Show me how you penetrate her. Let me see her beg for your cock.{/i}"
pause
scene ep12_cathy_lewd50 with dissolve
ca "How do you want us to show you?"
scene ep12_cathy_lewd51 with dissolve
ja "{i}Rig the camera so I can see him fuck you from behind.{/i}"
scene ep12_cathy_lewd52 with dissolve
ja "{i}Perfect. Let me see you fuck her good.{/i}"
scene anim_cathy_doggy1_ep12 with dissolve
ca "*{i}Moans{/i}*"
ja "{i}There you go... That's just what I want to see.{/i}"
ja "{i}Give her the full length of that big and sexy cock of yours, [mc_jade].{/i}"
ja "{i}Shove it into her pussy.{/i}"
pause
scene anim_cathy_doggy2_ep12 with dissolve
ja "{i}You're such a naughty slut, Cathy.{/i}"
ca "Yes, I'm a slut. I'm his slut."
mc "Damn, that's sexy."
pause
$ tmpInt = 0
$ tmpBool3 = False
label ep12_cathy_lewd_loop_label:
menu:
    "Doggystyle":
        $ tmpInt += 1
        scene anim_cathy_doggy1_ep12 with dissolve
        pause
        scene anim_cathy_doggy2_ep12 with dissolve
        pause
        jump ep12_cathy_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_cathy_miss1_ep12 with dissolve
        ca "Yes! Enter me! Give it to me."
        ja "{i}Fuck her brains out.{/i}"
        mc "Fuck... I'm trying so hard not to cum... Your sexy talk isn't helping."
        pause
        scene anim_cathy_miss2_ep12 with dissolve
        ja "{i}Oh, I will enjoy you covering her in cum. This is so much better than watching porn.{/i}"
        ca "*{i}Moans{/i}* I feel so dirty doing this."
        ja "{i}You are dirty. A dirty, little slut.{/i}"
        pause
        jump ep12_cathy_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_cathy_ride1_ep12 with dissolve
        ja "{i}Ride that cock.{/i}"
        ja "{i}Yes... You're really going at it. Mmm...{/i}"
        pause
        scene anim_cathy_ride2_ep12 with dissolve
        ja "{i}Ahh... I'm gonna cum from watching you ride him like that... Hngn...{/i}"
        ca "*{i}Moans{/i}* Me...too..."
        pause
        scene anim_cathy_ride3_ep12 with vpunch
        ca "Ahhh... Yes! Yes!"
        scene ep12_cathy_lewd53 with vpunch
        ca "Hnnnn!"
        scene anim_cathy_ride3_ep12 with dissolve
        ja "{i}You love that, you slut.{/i}"
        ca "You're the one to talk."
        pause
        jump ep12_cathy_lewd_loop_label
    "Try anal" if not tmpBool3:
        $ tmpBool3 = True
        scene ep12_cathy_lewd54 with dissolve
        ja "{i}Put it in her asshole.{/i}"
        scene ep12_cathy_lewd55 with dissolve
        ca "Oh, no. Nothing is going up there today."
        scene ep12_cathy_lewd54 with dissolve
        ja "{i}Can't you take it?{/i}"
        scene ep12_cathy_lewd55 with dissolve
        ca "Even if I could, I wouldn't try it here."
        scene ep12_cathy_lewd54 with dissolve
        ja "{i}It looks like you have things to learn, Cathy.{/i}"
        ja "{i}What a bummer... But maybe I'll show you one day how it's done.{/i}"
        jump ep12_cathy_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene ep12_cathy_lewd56 with dissolve
        ja "{i}Lift her and fuck her like the slut she is.{/i}"
        ca "Whoa!"
        scene anim_cathy_stand1_ep12 with dissolve
        ja "{i}Yes, that's how you do it. Fuck her hard, [mc_jade].{/i}"
        ca "Hngn! Fuck! Oh, [mc_cathy]!"
        pause
        scene anim_cathy_stand2_ep12 with dissolve
        mc "Do you like it?"
        ca "Yes! Give it to me. Hard!"
        pause
        jump ep12_cathy_lewd_loop_label
    "Cum" if tmpInt > 2 and tmpBool3:
        mc "I'm gonna cum soon..."
        menu:
            "Creampie":
                scene anim_cathy_miss1_ep12 with dissolve
                ja "{i}I want to see it up close. Show me how you fill that slut up with cum.{/i}"
                ja "{i}Fill her up to the brim and let me watch it ooze out of her.{/i}"
                scene ep12_cathy_lewd57 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_cathy_lewd57 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_cathy_lewd57 at vpunch, cum1
                mc "Ahh!!!"
                ca "*{i}Moans{/i}* Fuck!"
                scene ep12_cathy_lewd58 with dissolve
                ja "{i}Yes, show me that cum...{/i}"
                scene ep12_cathy_lewd59 with dissolve
                ja "{i}Beautiful... That's such a sexy sight.{/i}"
            "On tits":
                scene anim_cathy_tits_ep12 with dissolve
                ja "{i}Cover her tits with your sperm. Let me watch it spray all over her.{/i}"
                pause
                scene ep12_cathy_lewd60 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_cathy_lewd60 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_cathy_lewd61 at vpunch, cum2
                mc "Ahh!!!"
                ca "*{i}Gasps{/i}*"
                scene ep12_cathy_lewd62 with dissolve
                ja "{i}Yes, show me that cum...{/i}"
                ja "{i}Beautiful... That's such a sexy sight.{/i}"

scene ep12_cathy_lewd63 with dissolve
ca "*{i}Phew{/i}* Did you enjoy the show?"
scene ep12_cathy_lewd64 with dissolve
ja "{i}You made me want to crawl through the phone... You sly slut.{/i}"
scene ep12_cathy_lewd63 with dissolve
ca "Hahaha! That's what you get for sending me pictures of him kissing your breasts while I was in a meeting."
scene ep12_cathy_lewd64 with dissolve
ja "{i}[name], you fucked her good. But I'm going to punish you for this later.{/i}"
ja "{i}Sneaking around with my best friend like that... You're so naughty.{/i}"
scene ep12_cathy_lewd65 with dissolve
mc "I couldn't help myself."
stop music fadeout 3
scene ep12_cathy_lewd64 with dissolve
ja "{i}You'll get yours. Now go clean up.{/i}"
scene ep12_cathy_lewd66 with dissolve
play music "music/ep7/good_old_days.mp3"
ca "Wow... That was a hot experience. How did it feel for you?"
scene ep12_cathy_lewd67 with dissolve
mc "I was speechless... I loved being bossed around by her, and it was arousing knowing she watched us have sex."
mc "Are you two into this? I would never have guessed."
scene ep12_cathy_lewd68 with dissolve
ca "That makes two of us. It's not something we've done before."
ca "As it turned out, we had no problem sharing the experience we had with you in the past."
ca "And, evidently, we had no problem sharing this experience either."
scene ep12_cathy_lewd67 with dissolve
mc "Have you ever shared someone?"
scene ep12_cathy_lewd68 with dissolve
ca "Oh, no. We never went there before."
ca "I've always felt sexual, and I've had desires I didn't know how to sate..."
ca "But I haven't discussed those with Jade prior to her divorce."
scene ep12_cathy_lewd69 with dissolve
ca "So... How long has your fling with Jade been going on?"
scene ep12_cathy_lewd70 with dissolve
mc "Since the start of the semester. She came on to me during class, and we had some meaningful conversations and hot moments."
scene ep12_cathy_lewd69 with dissolve
ca "Oh, so she has confided in you, too? That's news to me."
scene ep12_cathy_lewd70 with dissolve
mc "Yeah, she has. We both were keeping our affair a secret from everyone else..."
mc "...and it felt natural to share more than just sex with each other. So, we have talked plenty."
scene ep12_cathy_lewd71 with dissolve
mc "..."
scene ep12_cathy_lewd72 with dissolve
mc "About that... Can I ask you something?"
scene ep12_cathy_lewd73 with dissolve
ca "Anything."
scene ep12_cathy_lewd74 with dissolve
mc "I mean, without you telling Jade about it."
scene ep12_cathy_lewd73 with dissolve
ca "Oh? Uh... I believe so."
scene ep12_cathy_lewd74 with dissolve
mc "Did you and Stephen ever...? You know?"
scene ep12_cathy_lewd73 with dissolve
ca "Ever do what?"
scene ep12_cathy_lewd75 with dissolve
ca "*{i}Gasps{/i}* Oh! Oh, God no! With Stephen?"
ca "Why would you ask me that?"
scene ep12_cathy_lewd76 with dissolve
mc "I shouldn't say."
scene ep12_cathy_lewd75 with dissolve
ca "Did Jade put that thought into your head?"
scene ep12_cathy_lewd76 with dissolve
mc "I feel bad about telling you this, but it's been one of her biggest fears that something was going on between you and Stephen."
mc "But she valued your friendship so highly that she'd never ask you about it."
mc "In fear that the answer would be yes, she'd rather keep you as a friend and pretend the answer was no."
scene ep12_cathy_lewd77 with dissolve
ca "Well, it is a no. I would never betray her like that."
ca "I can't believe she even thought that low of me."
scene ep12_cathy_lewd76 with dissolve
mc "She didn't. She thought that low of Stephen."
mc "He once said things that made her believe that something was going on."
scene ep12_cathy_lewd77 with dissolve
ca "*{i}Sigh{/i}* That piece of shit. He put those thoughts in her head?"
ca "Poor Jade..."
scene ep12_cathy_lewd78 with dissolve
mc "She'd be happy to learn that it never happened..."
mc "But also... Maybe she'd be pissed that I asked you that."
scene ep12_cathy_lewd79 with dissolve
ca "I understand. But what you did just now was a good thing."
ca "Let me handle my friend. I will reassure her that I did nothing of the sort."
scene ep12_cathy_lewd78 with dissolve
mc "I'm going to trust you on this."
scene ep12_cathy_lewd80 with dissolve
ca "Thank you. You already put your trust in me by telling me this."
ca "I will take care of it, and I'll be delicate about it."
stop music fadeout 3
scene ep12_cathy_lewd81 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep12_lewd_cathy = True
$ calcScenes()
$ mphone_stats_add_girl_s3("cathy","You had sex with Cathy at her office while Jade was on a video call with her in episode 12.")
$ mphone_stats_add_girl_s3("jade","You had sex with Cathy at her office while Jade was on a video call with her in episode 12.")
$ new_bio("Cathy", "I had sex with Cathy at her office as Jade was on a video call with her. It was like a virtual threesome.")
$ new_bio("Jade", "I had sex with Cathy at her office as Jade was on a video call with her. It was like a virtual threesome.")

label ep12_jblog_label:
hide screen new_phone_screen
$ guideSuggestedPage = 232
play music "music/ep5/licensed_music/track14.mp3"
show ep12_jblog1
if not persistent.ep12_cardcam10:
    show screen ep12_render_screen("cam10")
with wipeleft
$ renpy.pause()
if "Josy" in breakup:
    show ep12_jblog2
    hide screen ep12_render_screen
    with dissolve
    my "Is it just me, or is it hard to focus on the finals today?"
    scene ep12_jblog8 with dissolve
    js "..."
    scene ep12_jblog3 with dissolve
    my "Josy? Are you listening to me?"
    scene ep12_jblog9 with dissolve
    js "Sorry, I drifted off. What was that?"
    scene ep12_jblog2 with dissolve
    my "Never mind, I got the answer."
    scene ep12_jblog9 with dissolve
    js "I was thinking about [name] and going over everything he's said to me."
    scene ep12_jblog3 with dissolve
    my "How come?"
    scene ep12_jblog10 with dissolve
    js "I'm wracking my head for a sign or something he said that makes sense of it all."
    scene ep12_jblog2 with dissolve
    my "Does it matter? The outcome won't change."
    if ep12_josy_hurt:
        scene ep12_jblog10 with dissolve
        js "I'm trying to figure out if he knew for longer than he let on. Like, since Halloween or something."
        js "I doubt what happened between him and Zoey happened overnight."
        scene ep12_jblog3 with dissolve
        my "I think you'd have to go further back than that. And you can't see that far back because it happened years before we were even in the picture."
        my "That's what I think."
        scene ep12_jblog11 with dissolve
        js "I get sick when I think about seeing him with Zoey. I can't be his friend anymore, Maya... I can't."
    else:
        scene ep12_jblog11 with dissolve
        js "I'm looking for a reason to stay friends."
        js "I'm entertaining the thought, but I get mad at the thought of seeing him with Zoey."
    scene ep12_jblog4 with dissolve
    my "I don't think I have it in me either."
    if not ep12_josy_hurt:
        scene ep12_jblog9 with dissolve
        js "Have what in you?"
        scene ep12_jblog4 with dissolve
        my "To be his close friend after this."
    scene ep12_jblog5 with dissolve
    if ep12_maya_hurt:
        my "I wanted so much more than that. It will be too hard to settle for a friendship and see him with Zoey, like you said."
    else:
        my "How do I explain it...?"
        my "I think it will be hard to revert to friends after all that we've been through."
    scene ep12_jblog6 with dissolve
    my "I'll always be thankful for what he's done for me and us, but hanging out with him and acting like nothing happened between us..."
    my "I know I don't have that in me."
    scene ep12_jblog13 with dissolve
    js "Are you never going to talk to him again?"
    scene ep12_jblog6 with dissolve
    my "I didn't say that. I said I couldn't be his close friend."
    my "There are levels to it."
    scene ep12_jblog13 with dissolve
    js "I can't do any level of it."
    scene ep12_jblog6 with dissolve
    my "Maybe you can eventually."
    scene ep12_jblog12 with dissolve
    if ep12_josy_hurt:
        js "I feel like I don't need someone like him in my life."
        js "He is someone who hurt and betrayed me. I can't forgive or forget that."
    else:
        js "Honestly, what's the point of it? I feel like he betrayed my trust."
        js "I don't respect him anymore."
    scene ep12_jblog4 with dissolve
    my "It's a fresh wound, but I understand how you feel."
else:
    show ep12_jblog2
    hide screen ep12_render_screen
    with dissolve
    my "My head feels full. I don't want to study more today."
    scene ep12_jblog9 with dissolve
    js "I stopped studying an hour ago."

    if "Jill" in breakup:
        scene ep12_jblog3 with dissolve
        my "I'm still thinking about what Sage and Jill told us..."
        if ep4_toldDerekAboutJade:
            scene ep12_jblog11 with dissolve
            js "It's disgusting. I can't believe [name] did that."
            scene ep12_jblog3 with dissolve
            my "Which thing?"
            scene ep12_jblog11 with dissolve
            js "Well, both. But fucking Sage's mom and recording it... Eww!"
            scene ep12_jblog7 with dissolve
            my "Yeah... That's icky."
        elif branchZoey:
            scene ep12_jblog11 with dissolve
            js "I can't believe [name] did that to Jill."
            scene ep12_jblog7 with dissolve
            my "We haven't heard his side of the story, but yeah..."
            my "It sounded bad."
        scene ep12_jblog10 with dissolve
        if ep4_toldDerekAboutJade:
            js "Poor Sage... And poor Jill... She seemed heartbroken."
        else:
            js "Poor Jill... She seemed heartbroken."
    elif "Sage" in breakup:
        scene ep12_jblog3 with dissolve
        my "I'm still thinking about what Sage told us..."
        if ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
            scene ep12_jblog11 with dissolve
            js "It's disgusting. I can't believe [name] did that."
            if ep4_fuckedJade:
                js "Having sex with Sage's mom... Eww!"
            scene ep12_jblog7 with dissolve
            my "Yeah... That's icky."
        elif branchZoey:
            scene ep12_jblog11 with dissolve
            js "I can't believe [name] did that to Sage."
            scene ep12_jblog7 with dissolve
            my "We haven't heard his side of the story, but yeah..."
            my "It sounded bad."
        else:
            scene ep12_jblog10 with dissolve
            js "It sounded too weird that he'd break up with her without a reason."
            scene ep12_jblog3 with dissolve
            my "I agree. I'm sure there is a reason."
            my "I think he's trying to spare her feelings but doesn't know how."
            scene ep12_jblog10 with dissolve
            js "Spare her feelings from what? He broke up with her."
            scene ep12_jblog3 with dissolve
            my "Maybe he wasn't that into her?"
            scene ep12_jblog12 with dissolve
            js "That's not a big enough reason to withhold from her. He could just have said that."
            scene ep12_jblog6 with dissolve
            my "I know. I'm just trying to make sense of it."
        scene ep12_jblog10 with dissolve
        js "Poor Sage... She seemed heartbroken."
    elif ep4_toldDerekAboutJade:
        scene ep12_jblog3 with dissolve
        my "I'm still thinking about what Sage and Jill told us..."
        scene ep12_jblog11 with dissolve
        js "It's disgusting. I can't believe [name] did that."
        js "Having sex with Sage's mom... Eww!"
        scene ep12_jblog7 with dissolve
        my "Yeah... That's icky."
        scene ep12_jblog10 with dissolve
        if branchIsabella:
            js "Poor Sage... And poor Bella..."
        else:
            js "Poor Sage..."
    if "Jill" in breakup or "Sage" in breakup or ep4_toldDerekAboutJade:
        scene ep12_jblog3 with dissolve
        my "I know. It's going to be tricky to navigate this..."
        scene ep12_jblog9 with dissolve
        js "How do you mean?"
        scene ep12_jblog4 with dissolve
        if ep12_break_or_tell == "break" and not ep4_toldDerekAboutJade:
            my "How do we stay friends with both of them? Are we supposed to pick sides?"
        else:
            my "How do we stay friends with [name]? Are we supposed to pick sides?"
        scene ep12_jblog10 with dissolve
        js "Honestly, I think it's best not to get in the middle of it."
        if ep12_break_or_tell != "break":
            js "But if he asks me, I'll tell him my two cents."
        scene ep12_jblog4 with dissolve
        my "I don't know what to do. I feel bad."
        scene ep12_jblog10 with dissolve
        js "Same here. Can we talk about something else? I don't want to think about it."

scene ep12_jblog3 with dissolve
my "So... What are you doing on your laptop?"
scene ep12_jblog14 with dissolve
js "I'm checking my blog."
scene ep12_jblog15 with dissolve
my "Do you have a blog?"
scene ep12_jblog16 with dissolve
js "I've been meaning to show it to you. Take a look."
scene ep12_jblog19 with dissolve
my "1500 followers!?"
scene ep12_jblog18 with dissolve
js "They're not 1500."
scene ep12_jblog19 with dissolve
my "You're right. 1496. That's not even close, is it?"
scene ep12_jblog20 with dissolve
my "1497. I stand corrected."
scene ep12_jblog18 with dissolve
js "It's a lot, isn't it?"
scene ep12_jblog19 with dissolve
my "More people than I know."
scene ep12_jblog18 with dissolve
js "I don't know most of them. But the majority seems nice."
js "They like my content."
scene ep12_jblog21 with dissolve
my "What is your content?"
scene ep12_jblog22 with dissolve
js "I'm trying to inspire women."
scene ep12_jblog21 with dissolve
my "Into doing what? Giving you money?"
scene ep12_jblog23 with dissolve
js "Hey! The donations are optional. Most of my posts are free posts."
scene ep12_jblog24 with dissolve
my "But you charge people for some of them."
scene ep12_jblog25 with dissolve
js "Well, yeah. That's how you turn it into a business."
js "How else could I afford the clothes for my weekly fashion segments?"
scene ep12_jblog26 with dissolve
my "..."
scene ep12_jblog27 with dissolve
js "You should be supportive."
scene ep12_jblog28 with dissolve
my "I'm trying to understand it all."
scene ep12_jblog27 with dissolve
js "It's not that difficult to understand."
js "I blog about everyday life as a normal girl. I talk about topics people can relate to and interact with my fans."
scene ep12_jblog28 with dissolve
my "Have you got fans now?"
scene ep12_jblog27 with dissolve
js "Followers and fans are the same thing."
scene ep12_jblog29 with dissolve
my "Can I read some of it?"
scene ep12_jblog30 with dissolve
js "Yeah, go ahead."
scene ep12_jblog31 with dissolve
$ renpy.pause()
scene ep12_jblog32 with dissolve
js "See? It's not bad, is it?"
scene ep12_jblog33 with dissolve
my "I do like your writing. You have a way with your words."
scene ep12_jblog35 with dissolve
js "Really!? Do you think so?"
scene ep12_jblog34 with dissolve
my "I wouldn't have guessed from talking to you."
scene ep12_jblog36 with dissolve
js "Hey!"
scene ep12_jblog33 with dissolve
my "It was a joke. You're very good. I like how you paint a picture with your words."
scene ep12_jblog35 with dissolve
js "I've been nervous to tell you about it. I wasn't sure of what you'd think."
scene ep12_jblog33 with dissolve
my "You convinced me. I'll be follower 1498."
scene ep12_jblog37 with dissolve
js "Oh! Look! 1500!"
scene ep12_jblog38 with dissolve
my "Or something after that."
scene ep12_jblog39 with dissolve
my "That's a lot of unread messages and notifications. Don't you have to read all of those?"
js "I did at first, but it was hard to keep up."
scene ep12_jblog40 with dissolve
js "Huh!? I've got a message."
scene ep12_jblog41 with dissolve
my "Not just one. You have 99+ messages."
scene ep12_jblog42 with dissolve
js "It's from TheDiane."
scene ep12_jblog41 with dissolve
my "Who's that?"
scene ep12_jblog42 with dissolve
js "Who's that!? TheDiane - or Diane Reed - is one of the notorious independent fashion bloggers on CB."
scene ep12_jblog39b with dissolve
js "Look! This is her page."
scene ep12_jblog39c with dissolve
$ renpy.pause()
scene ep12_jblog39b with dissolve
my "582,000 followers!? That's like a small country of fans."
js "I know! She's huge! Have you really never heard of her?"
my "Nope. I never even saw her before."
js "Then you're out of the loop. She's fearless and such an inspiration. Check this out!"
scene ep12_jblog39d with dissolve
$ renpy.pause()
scene ep12_jblog39b2 with dissolve
js "She covers fashion, pop culture, and a fair deal of gossip."
js "She also does some amateur modeling, as you can see in these pictures."
scene ep12_jblog39e with dissolve
$ renpy.pause()
scene ep12_jblog39f with dissolve
js "She's gorgeous!"
my "Well, what does she want?"
scene ep12_jblog42 with dissolve
js "She says she likes my blog! Oh my God! I can't believe it!"
js "She said she loved the winter fashion photo set I posted."
scene ep12_jblog41 with dissolve
my "What's that?"
scene ep12_jblog43 with dissolve
if ep11_josy_solo:
    js "[name] and I went out to the lake with my camera and tripod to snap fashion pictures."
else:
    js "I went out to the lake with my camera and tripod to snap fashion pictures."
js "Then I wrote a post about it and included some of the photos. "
scene ep12_jblog44 with dissolve
my "So, she reads your blog?"
scene ep12_jblog43 with dissolve
js "She probably noticed me liking and commenting on her posts."
scene ep12_jblog45 with dissolve
js "She wants to use my photos in her upcoming post on the same topic."
scene ep12_jblog46 with dissolve
my "She wants to repost your content?"
scene ep12_jblog45 with dissolve
js "She says she'll credit me and link my CB page to her followers as compensation."
js "That is huge!"
scene ep12_jblog46 with dissolve
my "582,000 people will see your pictures!?"
scene ep12_jblog45 with dissolve
js "And maybe they'll join my page after! This is a huge opportunity, Maya!"
js "I have to do it! Right?"
scene ep12_jblog47 with dissolve
my "I wouldn't want that many people to scrutinize what I wear. Are you sure about this?"
scene ep12_jblog48 with dissolve
js "Don't you see the potential?"
scene ep12_jblog47 with dissolve
my "I do. I'm just asking if this is what you want."
my "I can't imagine having that many people read my thoughts and follow my advice."
my "Who am I to give advice? And for what? Uh... No. Just no."
my "Do you want that exposure? Is that the goal of your blog?"
scene ep12_jblog49 with dissolve
js "Maya... For the first time in my life, I feel like I've found something that I'm actually good at."
js "Can't you see how many people already like my blog?"
scene ep12_jblog50 with dissolve
my "Which is it that you like? Being good at something or getting validation for it?"
scene ep12_jblog49 with dissolve
js "What is there not to like about either? I have found my creative outlet, and people enjoy my content."
js "It's a win-win! And now with Diane's offer of publicity, it's a win-win-win! It's a triple win, Maya!"
scene ep12_jblog50 with dissolve
my "It sounds like you're sure about this."
scene ep12_jblog51 with dissolve
play sound "sound_effects/season3/type1.mp3"
js "I'm going for it."
js "Haha, wow! My fingers are trembling as I type. How unreal is this?"
scene ep12_jblog52 with dissolve
js "Question... Do you know how to use a camera?"
scene ep12_jblog53 with dissolve
play sound "sound_effects/season3/type2.mp3"
my "Pointing and pressing a button? I'm familiar with the concept."
scene ep12_jblog52 with dissolve
js "I have a job for you, if you want it."
js "How would you like to help me with my fashion photography?"
scene ep12_jblog53 with dissolve
my "As long as you don't make me famous for it, I can take a picture or two of you."
scene ep12_jblog52 with dissolve
js "Trust me; you'll enjoy it. It's something fun we can do together!"
stop music fadeout 3
scene ep12_jblog54 with dissolve
$ renpy.pause()

label ep12_than_label:
play music "music/ep5/rustic_ballad.mp3"
scene ep12_than1 with wipeleft
$ renpy.pause()
scene ep12_than2 with dissolve
than "Ah! There she is."
scene ep12_than3 with dissolve
ji "I'm so sorry I'm late. Have you been waiting long?"
scene ep12_than2 with dissolve
than "For about ten minutes or so. It's fine."
play sound "sound_effects/season2/chair_move.mp3"
if "Jill" in breakup or ep4_toldDerekAboutJade:
    scene ep12_than4 with dissolve
    ji "I've had a horrible day..."
    ji "Of course, I should have expected the traffic to be this bad on top of it."
    scene ep12_than10 with dissolve
    than "Oh? What happened?"
    scene ep12_than4 with dissolve
    if "Jill" in breakup:
        if branchZoey:
            ji "My boyfriend broke up with me, and I'm a mess right now."
        else:
            ji "I broke up with my boyfriend today because I found out some nasty truths about him. I'm a big mess right now."
    else:
        ji "I learned something terrible about someone close today, and it's weighing on my mind."
    scene ep12_than6 with dissolve
    ji "But I'm here now. I'll try my best to be present."
    ji "I know how valuable your time is."
    scene ep12_than11 with dissolve
    than "It's not more valuable than yours. I'm sad to hear you're going through a rough time. If you feel like talking..."
    scene ep12_than6 with dissolve
    ji "Thank you, but no. I don't want my problems to affect our meeting."
    ji "Believe me, he's not worth it."
    scene ep12_than11 with dissolve
    if "Jill" in breakup:
        than "I hear you."
    else:
        than "Guy problems, huh? I hear you."
    scene ep12_than7 with dissolve
    $ renpy.pause()
else:
    scene ep12_than5 with dissolve
    ji "I didn't expect the traffic to be this bad already."
    scene ep12_than12 with dissolve
    than "Blame it on the holidays. I'm happy you arrived safe and sound."
scene ep12_than8 with dissolve
ji "How have you been?"
scene ep12_than12 with dissolve
than "Lately, I've been good. I have traveled a lot around the country."
scene ep12_than8 with dissolve
ji "Giving lectures?"
scene ep12_than13 with dissolve
than "And promoting my new book."
scene ep12_than9 with dissolve
ji "Oh, of course! Is it out yet?"
scene ep12_than13 with dissolve
than "Two weeks ago. Just in time for Christmas shopping."
than "Not that people will buy my book as a gift, but..."
scene ep12_than9 with dissolve
ji "Don't sell yourself short like that. I'm sure many would consider it an excellent gift. I, for one, would!"
scene ep12_than13 with dissolve
than "I'm so happy you said that."
scene ep12_than15 with dissolve
than "Merry Christmas."
than "It's the first print edition."
ji "I'm honored."
scene ep12_than16 with dissolve
ji "And you signed it, too."
ji "\"To Jill. Thank you for being a beacon of light in a world of darkness. Without your forgiveness, I doubt this book would have seen the light of day. Jonathan.\""
scene ep12_than17 with dissolve
ji "Jonathan... I'm touched."
if "Jill" in breakup:
    scene ep12_than19 with dissolve
    than "No matter what that ex-boyfriend of yours did, he didn't deserve you."
    scene ep12_than18 with dissolve
    $ renpy.pause()
else:
    scene ep12_than19 with dissolve
    than "I meant every word."
scene ep12_than20 with dissolve
bari "Hi! What can I get you?"
scene ep12_than21 with dissolve
ji "A latte, please."
scene ep12_than20 with dissolve
bari "Coming right up."
scene ep12_than22 with dissolve
than "This extra copy is for Isabella. I take it you're still as close as ever."
scene ep12_than23 with dissolve
if branchIsabella or branchJill:
    ji "We've had some rough patches, but yes. I'd say we are closer than ever."
else:
    ji "Even closer, I'd say."
ji "Bella has made a lot of progress over the last year. You'd be surprised."
scene ep12_than30 with dissolve
than "Oh? Tell me more."
scene ep12_than23 with dissolve
ji "She's opened up, and not just to me. She's let others into her life, too."
scene ep12_than30 with dissolve
than "She was always tough to get close to. It's because of you she managed to open up in the first place."
scene ep12_than24 with dissolve
ji "She has not had it easy."
scene ep12_than30 with dissolve
than "I'm happy that you're still there for her."
scene ep12_than23 with dissolve
ji "She's here for me, too."
scene ep12_than31 with dissolve
$ renpy.pause()
scene ep12_than30 with dissolve
than "Now... About Lana and your campaign..."
scene ep12_than25 with dissolve
ji "Yes?"
scene ep12_than32 with dissolve
than "Tell me what you've come up with. I'm dying to hear it."
scene ep12_than25 with dissolve
ji "So, my idea right now is this..."
ji "I will start a foundation in memory of my sister, and any funds that I'd receive I'd use to help people in similar situations."
scene ep12_than32 with dissolve
than "A foundation is great. It's a solid idea, but the funding is a huge problem."
than "You'll need sponsors to make it work, and we're not talking small sponsors at that."
than "If you're looking to make a difference, you'll need more than $1 million to set it up."
scene ep12_than26 with dissolve
ji "I'm aware that I need funding for it..."
ji "I have money that I could use, but it would be smarter to contact potential sponsors early on to gauge interest."
scene ep12_than32 with dissolve
than "And I assume that asking Amelia and Geoff is still out of the picture."
scene ep12_than26 with dissolve
ji "I can see that going two ways, and I like neither."
ji "They will either be disappointed in me for getting your help and react poorly to the idea because of it..."
scene ep12_than27 with dissolve
ji "...or they will love the idea and try to make it their own because Lana was their daughter."
ji "And I don't want them to take this away from me."
scene ep12_than26 with dissolve
ji "I plan on telling them about it after it's been set up, but asking them to be sponsors at this stage..."
ji "I don't want to risk it."
scene ep12_than33 with dissolve
than "Geoff and Amelia may not like me, but I don't think they will dislike your idea at all."
than "And sure, they can be controlling, but I can't see them making your idea theirs."
scene ep12_than26 with dissolve
ji "How can you be sure?"
scene ep12_than33 with dissolve
than "They know how much your sister loved you."
than "Without you, Lana wouldn't have come back home as much as she did."
scene ep12_than34 with dissolve
than "If they saw that you started a foundation in her name, I think they would be proud of you."
than "For all these years, they didn't do anything like it. And they are smart people, your parents."
than "I'm sure it must have crossed their minds sometime."
scene ep12_than27 with dissolve
ji "I think Dad needs this."
scene ep12_than33 with dissolve
than "What do you mean?"
scene ep12_than27 with dissolve
ji "He's been more down than usual lately. It's always around Lana's birthday, but his drinking has gotten worse, and he's working way less, too."
ji "I think he needs to see that Lana's memory still lives on and that her time on this earth inspired something greater than herself."
ji "That's another reason why I think this foundation is the way to go."
scene ep12_than33 with dissolve
than "See... The way you realize that doesn't align with Geoff or Amelia wanting to overtake your foundation."
than "And you know, if you think that me being a part of it will deter them, I have no problem staying out of it."
than "My name doesn't have to be involved in any paperwork. And the donations I'd make could be anonymous."
scene ep12_than26 with dissolve
ji "What donations?"
scene ep12_than30 with dissolve
than "You didn't count me out as a sponsor, did you?"
scene ep12_than28 with dissolve
$ renpy.pause()
scene ep12_than30 with dissolve
than "Let's hope that the book sales take off first. Haha."
scene ep12_than29 with dissolve
ji "Jonathan... Thank you."
scene ep12_than25 with dissolve
ji "Now I want to hear your thoughts and ideas."
scene ep12_than34 with dissolve
than "Well, I've been thinking too. Most of the ideas I came up with, I thought of during my tour."
than "Haha... Tour sounds so pretentious."
scene ep12_than25 with dissolve
ji "It was a tour."
scene ep12_than30 with dissolve
than "Yeah, I'm quite the rockstar. I'm amazed we aren't swamped by fans just sitting here."
scene ep12_than29 with dissolve
ji "Haha!"
scene ep12_than34 with dissolve
than "Speaking at universities, hospitals, and clinics has done amazing things for me."
than "I've felt so...fulfilled. And I get the feeling that I have reached people in a way I couldn't before."
scene ep12_than33 with dissolve
than "Sure, it's not a weekly group meeting where you get to know someone and dig into the problems, but I still feel like I'm out there doing well by people."
scene ep12_than34 with dissolve
than "What I thought about for you, if you're interested, is having your own seminars."
than "You could start with local high schools and share your experience, and reach out to young adults who might not feel so well."
scene ep12_than25 with dissolve
ji "That sounds like something that would be possible."
scene ep12_than34 with dissolve
than "But if you don't want to invest time in the hands-on approach, I'm sure the foundation would keep you busy enough."
scene ep12_than26 with dissolve
ji "I'd like the foundation to have a meaning beyond a name and money being handed out."
ji "I want it to help and inspire."
ji "Seminars would be a good start to do that. And what better way than to reach out to students at that age?"
scene ep12_than30 with dissolve
than "That's what I thought too."
stop music fadeout 3
scene ep12_than35 with dissolve
$ renpy.pause()

label ep12_lib_label:
$ guideSuggestedPage = 233
show screen new_phone_screen
if branchIsabella:
    jump ep12_bella_lib_label
play music "music/ep2/journey_of_hope.mp3"
scene ep12_lib1 with wiperight
$ renpy.pause()
label ep12_libb_label:
if branchIsabella:
    scene ep12_lib6 with dissolve
    mc "(I wonder where Bella went...)"
    if ep4_toldDerekAboutJade:
        scene ep12_lib3 with dissolve
        mc "(How much space does she want me to give her? I wish I knew...)"
scene ep12_lib2 with dissolve
if minigames:
    menu:
        "Study Math":
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Study English":
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
mc "(Ugh... I can't wait until the finals are over and done with.)"
mc "(The finals are weird...)"
scene ep12_lib4 with dissolve
mc "(They want us to know everything about the class at once.)"
mc "(Which forces us to study it all at once.)"
scene ep12_lib5 with dissolve
mc "(But I can already tell you most of this won't stick in my head for another week.)"
mc "(So, have I truly learned something? Or am I only displaying that I know how to retain information for a week?)"
if branchAlone and ep11_rolling and (not ep11_nicole_dating or ep11_nicole_dating):
    scene ep12_lib7 with dissolve
    ly "Found you."
    scene ep12_lib8 with dissolve
    mc "Were you looking for me?"
    scene ep12_lib9 with dissolve
    ly "Check your phone."
    scene ep12_lib8 with dissolve
    mc "Oh, I had it on silent mode. I've been trying to focus on my studies with minimal distractions."
    mc "Don't tell me you walked around campus looking for me."
    scene ep12_lib9 with dissolve
    ly "Jacob told me where you were. Can we talk or...?"
    scene ep12_lib8 with dissolve
    mc "I've earned myself a break. What's up?"
    scene ep12_lib10 with dissolve
    ly "We need to talk about what happened at the party."
    scene ep12_lib11 with dissolve
    mc "Yeah, maybe we do."
    scene ep12_lib10 with dissolve
    ly "Yesterday at work was hard for me."
    ly "I had to dance for strangers the entire night, but all I could think about was you."
    scene ep12_lib11 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Cathy scene)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        #if ep10_cathy_lewd and ep11_jade_lewd and not branchZoey:
                        #   $ mod_choices[4]="(Skips Cathy scene)"
    
    menu:
        "That's sweet":
            mc "That's sweet."
            scene ep12_lib12 with dissolve
            ly "That's not sweet at all, [name]. It distracted me."
        "I've thought about you, too \n{size=-4}[m_c1][mod_choices[2]]":
            $ dk(-1)
            mc "I've thought about you, too."
            scene ep12_lib12 with dissolve
            ly "Not in that kind of way, [name]. It distracted me."
        "So? \n{size=-4}[m_c1][mod_choices[3]]":
            $ dk(1)
            mc "So?"
            scene ep12_lib12 with dissolve
            ly "What do you mean by \"So\"? It distracted me."
    ly "It stopped me from doing my job."
    scene ep12_lib13 with dissolve
    ly "It doesn't feel like we're rolling anymore. It feels like we're dating."
    if branchZoey and not wt_ep11_zoey_kiss_others:
        scene ep12_lib11 with dissolve
        mc "Lily, we're not dating."
        scene ep12_lib12 with dissolve
        ly "That's how it feels."
        scene ep12_lib11 with dissolve
        mc "I'm gonna stop you right there."
        mc "Lily... We're not dating. We've been rolling."
        mc "And while that's been fun... We need to stop doing that."
        scene ep12_lib15 with dissolve
        ly "Because it's affecting my job?"
        scene ep12_lib11 with dissolve
        mc "That is a good reason to stop... But also, I'm getting back together with my ex."
        scene ep12_lib15 with dissolve
        ly "What?"
        scene ep12_lib16 with dissolve
        mc "Zoey. I'm getting back together with her."
        mc "After you left the party... Things happened between us."
        scene ep12_lib17 with dissolve
        ly "Huh?"
        ly "We have sex, I leave, and you get back together with your ex? All in one night?"
        scene ep12_lib16 with dissolve
        mc "It didn't happen all in one night. It's been happening since about Halloween."
        scene ep12_lib17 with dissolve
        ly "What the fuck?"
        scene ep12_lib16 with dissolve
        mc "You and I weren't dating, so..."
        mc "And, hey... That's good news for you, yeah?"
        mc "You don't have to feel bad about doing your job anymore."
        scene ep12_lib18 with dissolve
        ly "I guess not..."
        scene ep12_lib19 with dissolve
        mc "I had fun with you. I hope we can still stay friends."
        mc "The terms of rolling together weren't clear on that..."
        scene ep12_lib17 with dissolve
        ly "Yeah... Whatever. Friends."
        scene ep12_lib16 with dissolve
        mc "All good?"
        scene ep12_lib17 with dissolve
        ly "Peachy."
        scene ep12_lib28 with dissolve
        $ renpy.pause()
        stop music fadeout 3
        scene ep12_lib29 with dissolve
        mc "(Great... Now she's sour. It feels like there wasn't any winning with her.)"
        $ new_bio("Lily", "Lily wanted to stop rolling with me as it affected her job. I told her I was fine with it since I entered a relationship with Zoey.")
    elif ep11_lily_want_more:
        scene ep12_lib11 with dissolve
        mc "We're not dating. We're rolling."
        scene ep12_lib12 with dissolve
        ly "You say that, but I don't think you mean it."
        ly "Tell me what you really feel, [name]."
        scene ep12_lib11 with dissolve
        mc "We're not dating, but...what would be so wrong about that?"
        if (ep11_follow_quinn and not wt_ep11_quinn_lilly) and not ep10_lily_english:
            scene ep12_lib13 with dissolve
            ly "It doesn't feel good for me, [name]."
            ly "Look... I think we should stop rolling."
            scene ep12_lib11 with dissolve
            mc "Why?"
            scene ep12_lib12 with dissolve
            ly "You're too much of a risk for me. I can't quit my job and date you."
            ly "And I can't do my job if I'm with you."
            $ ep12_rolling = False
            scene ep12_lib11 with dissolve
            menu:
                "I feel something for you":
                    mc "I feel something for you, Lily."
                    mc "I know that rolling with you didn't turn out like you planned, but I think it turned out for the better."
                    mc "Well... Until now."
                    scene ep12_lib20 with dissolve
                    mc "I'm not going to ask you to stop working if that's what you need to do."
                    mc "And I won't blame you if you choose to follow your plan."
                    mc "But if you choose differently... I'm here for it."
                    scene ep12_lib13 with dissolve
                    ly "I'm sorry, [name]. It has to end."
                    scene ep12_lib14 with dissolve
                    mc "I hear you... Let's be friends instead."
                    scene ep12_lib28 with dissolve
                    $ renpy.pause()
                    stop music fadeout 3
                    scene ep12_lib29 with dissolve
                    $ renpy.pause()
                "Respect her choice":
                    mc "If that's what you want, I'm ok with it."
                    scene ep12_lib12 with dissolve
                    ly "Are you sure?"
                    scene ep12_lib14 with dissolve
                    mc "If what we're doing together affects you negatively... We should stop doing it."
                    mc "That's not what it was supposed to be like. Remember?"
                    mc "It was about having a good time together and having each other's backs."
                    scene ep12_lib21 with dissolve
                    mc "Let me have your back one final time. Let's be friends instead."
                    scene ep12_lib22 with dissolve
                    ly "Thanks, [name]. I'm happy you understand me."
                    scene ep12_lib28 with dissolve
                    $ renpy.pause()
                    stop music fadeout 3
                    scene ep12_lib29 with dissolve
                    mc "(I can't lie... I'm going to miss it...)"
            $ new_bio("Lily", "Lily wanted to stop rolling with me as it affected her job.")
        else:
            scene ep12_lib12 with dissolve
            ly "Don't you remember what I told you on the jetty?"
            scene ep10_bbq_lily_jetty_event14 with Dissolve(2)
            ly "[name]..."
            ly "I can only do what I do {b}because{/b} I haven't fallen for anyone."
            ly "Do you get it?"
            scene ep12_lib11 with dissolve
            mc "You've got feelings for me."
            scene ep12_lib13 with dissolve
            ly "I don't know what it is, but I don't like it."
            ly "[name], the problem is..."
            ly "How can I choose between a job that makes me financially secure and a weird feeling in my gut?"
            scene ep12_lib12 with dissolve
            ly "Even though you never asked me to stop stripping, my conscience tells me I can't do this to you."
            ly "I know what I am, and I know what I'm not."
            ly "I'm a stripper, but I'm not a cheater."
            scene ep12_lib11 with dissolve
            mc "So, what do you want to do?"
            scene ep12_lib12 with dissolve
            ly "You're gonna have to help me out here."
            scene ep12_lib11 with dissolve
            
            if persistent.mod_wtenabled: 
                        $mod_choices = ["(Lily path)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        #if ep10_cathy_lewd and ep11_jade_lewd and not branchZoey:
                        #   $ mod_choices[4]="(Skips Cathy scene)"
            
            menu:
                "I feel something for you \n{size=-4}[m_c1][mod_choices[0]]":
                    $ ep12_rolling = True
                    mc "I'm not sure if this will help you, but I feel something for you, too."
                    mc "I know that rolling with you didn't turn out like you planned, but I think it turned out for the better."
                    scene ep12_lib14 with dissolve
                    mc "Well... Until now."
                    mc "I'm not going to ask you to stop working if that's what you need to do."
                    mc "But I'm not gonna lie... A part of me is happy that you feel something, too."
                    scene ep12_lib20 with dissolve
                    mc "Because it reinforces the good feelings I feel about you."
                    mc "I don't think I can or want to help you with this problem because I'd hate it if I chose for you and it didn't turn out well."
                    mc "This needs to be your choice, Lily."
                    scene ep12_lib11 with dissolve
                    mc "I won't blame you if you choose to follow your plan."
                    mc "But if you choose differently... I'm here for it."
                    scene ep12_lib27 with dissolve
                    ly "That didn't help me at all..."
                    scene ep12_lib25 with dissolve
                    mc "It's the best I can do."
                    scene ep12_lib26 with dissolve
                    ly "*{i}Sigh{/i}* Dammit, [name]."
                    scene ep12_lib28 with dissolve
                    $ renpy.pause()
                    stop music fadeout 3
                    scene ep12_lib29 with dissolve
                    $ renpy.pause()
                    $ new_bio("Lily", "Lily wanted to stop rolling with me as it affected her job. I told her I had feelings for her.")
                "Break it off":
                    $ ep12_rolling = False
                    mc "I think you should stick to your plan."
                    scene ep12_lib15 with dissolve
                    ly "You do?"
                    scene ep12_lib20 with dissolve
                    mc "I could be selfish and say something else, but you told me where you're coming from."
                    mc "I know you have a goal, and I don't want to keep you from reaching that goal."
                    scene ep12_lib14 with dissolve
                    mc "And if what we're doing together affects you negatively... We should stop doing it."
                    mc "That's not what it was supposed to be like. Remember?"
                    mc "It was about having a good time together and having each other's backs."
                    scene ep12_lib25 with dissolve
                    mc "Let me have your back one final time. Let's be friends instead."
                    ly "..."
                    scene ep12_lib26 with dissolve
                    ly "You're the best."
                    scene ep12_lib28 with dissolve
                    $ renpy.pause()
                    stop music fadeout 3
                    scene ep12_lib29 with dissolve
                    mc "(I can't lie... I'm going to miss it...)"
                    $ new_bio("Lily", "Lily wanted to stop rolling with me as it affected her job. I told her she should stick to her plan.")
    else:
        scene ep12_lib11 with dissolve
        mc "To you maybe... But not to me."
        scene ep12_lib12 with dissolve
        ly "For real?"
        scene ep12_lib11 with dissolve
        mc "100%%."
        mc "I like rolling, but I'm not looking to start a relationship with you."
        mc "I went in this not knowing what to make out of it, but you made it clear it wasn't dating."
        scene ep12_lib14 with dissolve
        mc "That may have changed for you, but it hasn't changed for me."
        scene ep12_lib12 with dissolve
        ly "It feels way different, and I can't say why."
        scene ep12_lib11 with dissolve
        mc "I blame myself. I'm simply too attractive and charming. I'm not cut out for rolling with someone."
        scene ep12_lib22 with dissolve
        ly "Not funny."
        scene ep12_lib21 with dissolve
        mc "Listen... I don't want you to change your plans. You told me why you do what you do."
        mc "If I'm the reason you can't reach your goals, then screw me. Figuratively."
        mc "Put yourself first, Lily."
        scene ep12_lib22 with dissolve
        ly "Thank you, [name]... That helps."
        scene ep12_lib21 with dissolve
        mc "Can we still be friends?"
        scene ep12_lib22 with dissolve
        ly "Friends."
        scene ep12_lib23 with dissolve
        mc "With benefits?"
        scene ep12_lib24 with dissolve
        ly "Why do you mock me?"
        scene ep12_lib21 with dissolve
        mc "Ironically, to make you feel better."
        scene ep12_lib22 with dissolve
        ly "It worked... You're the best."
        scene ep12_lib28 with dissolve
        $ renpy.pause()
        stop music fadeout 3
        scene ep12_lib30 with dissolve
        $ renpy.pause()
        $ new_bio("Lily", "Lily wanted to stop rolling with me as it affected her job. I told her I was fine with it since I didn't have any feelings for her.")
else:
    stop music fadeout 3
    scene ep12_lib2 with dissolve
    mc "(Screw this... It's late. Let's head back home.)"

label ep12_campus_label:
play music "music/ep8/licensed_music/track65.mp3"
scene ep12_campus1 with wipeleft
ni "[name]... Got a second?"
if ep11_nick_attitude > 2:
    scene ep12_campus2 with dissolve
    mc "What the fuck do you want?"
elif ep11_nick_attitude > 0:
    scene ep12_campus2 with dissolve
    mc "What?"
else:
    scene ep12_campus3 with dissolve
    mc "Hey... What's up?"
scene ep12_campus4 with dissolve
ni "The other day, in the library, I overheard something you should know."
if ep11_nick_attitude > 2:
    scene ep12_campus5 with dissolve
    mc "Yeah? Tell it to someone who cares."
    scene ep12_campus6 with dissolve
    ni "It concerns the DIKs, dude. Stop being an ass."
    scene ep12_campus5 with dissolve
    mc "Are you calling me an ass? Look in a fucking mirror."
    scene ep12_campus4 with dissolve
    ni "Yeah, I get it. You're mad at me. But at least listen to what I have to say."
elif ep11_nick_attitude > 0:
    scene ep12_campus5 with dissolve
    mc "I'm not interested in hearing more of your accusations."
    scene ep12_campus4 with dissolve
    ni "It's nothing like that. It concerns the DIKs."
else:
    scene ep12_campus5 with dissolve
    mc "About what?"
    scene ep12_campus4 with dissolve
    ni "It concerns the DIKs."
$ guideSuggestedPage = 234
ni "Something is going on with the tri-betas. I overheard them talking about us."
scene ep12_campus5 with dissolve
if ep11_nick_attitude > 2:
    mc "Us, huh?"
else:
    mc "I'm listening."
scene ep12_campus7 with dissolve
ni "They said something about getting revenge on the frats, and that they are starting with the DIKs."
scene ep12_campus5 with dissolve
mc "Revenge for what?"
scene ep12_campus7 with dissolve
ni "It sounded serious. They called it a vendetta."
if ep11_nick_attitude > 2:
    scene ep12_campus5 with dissolve
    mc "That's it? What am I supposed to do with that?"
    scene ep12_campus8 with dissolve
    ni "*{i}Sigh{/i}* I don't know either."
scene ep12_campus5 with dissolve
mc "We haven't done anything to them. It's far-fetched that they would hold a grudge against us."
scene ep12_campus4 with dissolve
ni "That's not entirely true. We've picked on them a lot during Hell Week, and they weren't happy when the DIKs were formed and moved into the mansion."
ni "There's history between the frats, for sure."
ni "And I'm thinking... What if they had something to do with everything that's going on, too?"
scene ep12_campus9 with dissolve
mc "With what?"
scene ep12_campus8 with dissolve
ni "With the laptop, maybe."
scene ep12_campus5 with dissolve
mc "Wasn't that your doing?"
scene ep12_campus10 with dissolve
ni "No! Not the cluck or the pictures. I tried telling you guys that, but you wouldn't listen."
scene ep12_campus9 with dissolve
mc "So, you're saying the tri-betas somehow got hold of the laptop while you were using it and posted the cluck?"
scene ep12_campus8 with dissolve
ni "I know how it sounds, but I wasn't with the laptop all the time."
scene ep12_campus9 with dissolve
mc "What? You said you were."
scene ep12_campus11 with dissolve
ni "No, not really. I was watching...porn on it, and I got caught doing that and left the laptop alone for a while."
ni "And when I realized what had happened, I panicked and tried to find the laptop."
ni "I think I left it unlocked... So, part of it was my fault."
scene ep12_campus5 with dissolve
if ep11_nick_attitude > 2:
    mc "This story sounds like bullshit. I don't believe you."
else:
    mc "Nick... I'm sorry, but this sounds like bullshit."
scene ep12_campus6 with dissolve
ni "I'm not a liar, [name]. And even if you don't believe anything else I've said, believe this..."
ni "The tri-betas are up to something. Watch your backs."
$ new_bio("Nick", "Nick tried to convince me that the tri-betas were plotting behind the DIKs' backs.")
show ep12_campus12
if not persistent.ep12_cardcam11:
    show screen ep12_render_screen("cam11")
with dissolve
$ renpy.pause()
show ep12_campus13
hide screen ep12_render_screen
with dissolve
mc "(Hey... Isn't that...?)"
scene ep12_campus14 with dissolve
mc "Rio?"
scene ep12_campus15 with dissolve
mc "Hey, Rio?"
scene ep12_campus16 with dissolve
mc "Riona? Wait."
scene ep12_campus17 with dissolve
mc "Come on, Rio. I know that's you..."
ri "[name]. Please, don't look at me."
ri "I only came to talk to the dean. I didn't want to run into someone I knew."
scene ep12_campus18 with dissolve
if ep10_quinn_help:
    mc "Let me see your face. I know what happened. It's ok. It's me..."
    scene ep12_campus19 with dissolve
    mc "Rio... I knew it was bad, but..."
else:
    mc "What's wrong?"
    ri "Don't freak out."
    scene ep12_campus19 with dissolve
    mc "Oh my God. What happened to you?"
scene ep12_campus20 with dissolve
ri "..."
scene ep12_campus21 with dissolve
ri "I..."
ri "I don't feel comfortable talking about it here."
scene ep12_campus20 with dissolve
mc "Follow me back to my room. We can talk in private there."
scene ep12_campus21 with dissolve
ri "I can't. I don't want anyone to see me like this."
scene ep12_campus19 with dissolve
mc "It's fine. I'll sneak you in from my window. Come on..."
stop music fadeout 3
scene ep12_campus22 with dissolve
$ renpy.pause()
jump ep12_freeroam_room2_label

label ep12_pinkrose_label:
play music "music/ep12/licensed_music/track201.mp3"
queue music ["music/ep12/licensed_music/track200.mp3","music/ep12/licensed_music/track201.mp3"]
scene ep12_pinkrose1
show screen dance_filter_screen
with wipeleft
mc "Guess who approached me today?"
scene ep12_pinkrose2 with dissolve
le "Like, which one of the strippers?"
scene ep12_pinkrose3 with dissolve
mc "On campus."
scene ep12_pinkrose4 with dissolve
jm "A stripper approached you on campus?"
scene ep12_pinkrose3 with dissolve
mc "Never mind this guessing game. It was Nick."
scene ep12_pinkrose4 with dissolve
jm "Nick approached you?"
scene ep12_pinkrose3 with dissolve
mc "Did you guys talk to him lately?"
scene ep12_pinkrose5 with dissolve
le "I haven't said a single word to him since he almost fucked up my friendship with Jamie."
scene ep12_pinkrose6 with dissolve
jm "Yeah, we don't need Nick to do that. We're good at doing it ourselves."
play sound "sound_effects/bottle_clink.mp3"
scene ep12_pinkrose7 with dissolve
le "We both said things we weren't proud of behind each other's backs. Let's call it even."
scene ep12_pinkrose4 with dissolve
jm "What did Nick say?"
scene ep12_pinkrose3 with dissolve
mc "He told me that he overheard the tri-betas plotting."
mc "He said that they were looking for revenge on all frats and that the DIKs were their first target."
scene ep12_pinkrose4 with dissolve
jm "Revenge for what?"
scene ep12_pinkrose8 with dissolve
mc "Nick thought it had something to do with our Hell Week pranks."
mc "And he said it might go back even further than that - back when the DIKs were formed."
mc "Do you understand what he meant by that?"
scene ep12_pinkrose2 with dissolve
le "We wedgied the hell out of them. I'm not surprised if they hate us for that."
scene ep12_pinkrose9 with dissolve
jm "Haha, yeah! Their revenge would be something tame like egging our house or calling the cops when we have a party."
scene ep12_pinkrose3 with dissolve
mc "Hm... Someone snitched to Professor Hoff about our Christmas party."
scene ep12_pinkrose10 with dissolve
le "For real?"
scene ep12_pinkrose8 with dissolve
mc "Yeah, he showed up wanting to check it out, but I talked my way out of it."
scene ep12_pinkrose9 with dissolve
jm "See! I wouldn't worry about those nerds."
scene ep12_pinkrose2 with dissolve
le "Yeah, I would worry more about sharing the HOTs with the jocks at the New Year's Eve party. Like... What is up with that!?"
scene ep12_pinkrose3 with dissolve
mc "Yeah... That wasn't news I expected today either."

play sound "sound_effects/shove.mp3"
scene ep12_pinkrose11 with vpunch
sn "[name]!!! You're here?"
scene ep12_pinkrose12 with dissolve
mc "Oh, Sandy? Hey... Yeah, I came with the boys."
mc "We needed something to take our minds off finals week."
scene ep12_pinkrose13 with dissolve
sn "Say no more... I know exactly what you need."
$ guideSuggestedPage = 236
if branchAlone:
    if ep9_sandy_accept:
        jump ep12_pinkrose_sandy_label
    elif in_bios("Sandy wanted to fuck me, but I declined."):
        sn "Are you in the mood for it tonight?"
        jump ep12_pinkrose_sandy2_label
    else:
        jump ep12_pinkrose_sandy_label
else:
    if ep9_sandy_club:
        label ep12_pinkrose_sandy_label:
        sn "I finally got you here in the club to myself."
        label ep12_pinkrose_sandy2_label:
        scene ep12_pinkrose14 with dissolve
        menu:
            "[m_c1]What are you thinking?":
                mc "What are you thinking?"
                scene ep12_pinkrose15 with dissolve
                sn "Dirty, nasty, and kinky stuff. How about you?"
                scene ep12_pinkrose14 with dissolve
                
                if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sandy/Tania scene)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        if not ep12_nicole_path:
                           $ mod_choices[4]="(Sandy/Tania scene)"
                        else:
                            $ mod_choices[4]="(Sandy/Tania scene)"
                            $ mod_choices[5]="(Ends Nicole path)"
                
                if branchZoey and not wt_ep11_zoey_kiss_others:
                    jump ep12_pinkrose_sandy2b_label
                elif (not breakup and not branchAlone) and wt_ep9_branch_numbers == 1:
                    if (ep11_sage_love > 0 or ep11_maya_love > 0 or ep11_josy_love > 0) and wt_ep9_branch_numbers == 1:
                        jump ep12_pinkrose_sandy2b_label
                    elif tc < 5 and not persistent.no_cheater:
                        jump ep12_pinkrose_sandy2b_label
                menu:
                    "Sandy/Tania (Keep Nicole path open)" if ep12_nicole_path:
                       $ wt_ep12_sandy_nicole=True
                       jump wt_ep12_sandy_tania_label
                    "I want to do those things to you \n{size=-4}[m_c1][mod_choices[4]][m_c2][mod_choices[5]]":
                        label wt_ep12_sandy_tania_label:
                        mc "I want to do those things to you."
                        scene ep12_pinkrose16 with dissolve
                        tan "[name]!"
                        scene ep12_pinkrose19 with dissolve
                        sn "Back off, Tania. I saw him first. I'm sure there are other customers you can satisfy."
                        if ep12_nicole_path and not wt_ep12_sandy_nicole:
                            scene ep12_pinkrose18 with dissolve
                            tan "Actually, I think Nicole saw him first. I heard they are dating...or was it fucking?"
                            scene ep12_pinkrose20 with dissolve
                            sn "You're dating Nicole!?"
                            scene ep12_pinkrose21 with dissolve
                            
                            if persistent.mod_wtenabled: 
                                $mod_choices = ["(Sandy/Tania scene)","(-5 Maya)","(-DIK)","(+DIK)","","","","","","","","" ]
                                #[mod_gr][mod_choices[0]]
                                #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                                if not ep12_nicole_path:
                                   $ mod_choices[4]="(Sandy/Tania scene)"
                            
                            menu:
                                "Yeah, we're dating":
                                    $ ep12_nicole_dating = 1
                                    mc "Yeah, we're dating. It hasn't been going on long, but we've gone on one date so far."
                                    scene ep12_pinkrose20 with dissolve
                                    sn "Then, you're a bad boy! Bad, bad, bad..."
                                    sn "I can't do the things I planned if you're dating Nic."
                                    sn "What a shame."
                                    $ new_bio("Sandy", "I told Sandy that Nicole and I were dating when she wanted to have some fun with me.")
                                    jump ep12_pinkrose_sandy3_label
                                "No, we're just fucking \n{size=-4}[m_c1][mod_choices[0]]":
                                    $ ep12_nicole_dating = 2
                                    mc "Dating? No, we're just fucking."
                                    scene ep12_pinkrose22 with dissolve
                                    sn "Then, that's a different story. Let's go."
                                    $ new_bio("Sandy", "I told Sandy that Nicole and I were just fucking when she wanted to have some fun with me.")
                        else:
                            scene ep12_pinkrose16 with dissolve
                            tan "No, it's a slow night. Everyone's busy getting ready for Christmas instead of coming here."
                            tan "Men need to get their priorities straight. Am I right, [name]?"
                            scene ep12_pinkrose17 with dissolve
                            mc "Haha, sure."
                            scene ep12_pinkrose22 with dissolve
                            sn "Let's not waste any more time talking. Let's go."
                        scene ep12_pinkrose18 with dissolve
                        tan "Where are we going?"
                        scene ep12_pinkrose19 with dissolve
                        sn "[name] and I are going to a private room. And you're going nowhere."
                        scene ep12_pinkrose18 with dissolve
                        tan "I'll tag along for some fun."
                        scene ep12_pinkrose23 with dissolve
                        sn "*{i}Whispers{/i}*"
                        scene ep12_pinkrose24 with dissolve
                        tan "Oh? {b}That{/b} kind of fun?"
                        scene ep12_pinkrose25 with dissolve
                        tan "Let's go, [name]!"
                        sn "Haha!"
                        jump ep12_ts_lewd_label
                    "I don't want to do that":
                        label ep12_pinkrose_sandy2b_label:
                        mc "Oh... I don't want to do that. I'm just here to watch tonight."
                        $ new_bio("Sandy", "Sandy wanted to take me to a private room for some fun, but I declined.")
                        scene ep12_pinkrose15 with dissolve
            "I'm just here to watch":
                mc "Sorry, Sandy. I'm just here to watch tonight."
                scene ep12_pinkrose15 with dissolve
                $ new_bio("Sandy", "Sandy wanted to have some fun, but I declined.")
        sn "*{i}Groans{/i}*"
        sn "I thought you were up for some fun..."
    elif in_bios("Sandy wanted to fuck me, but I told her I couldn't do stuff like that with her anymore."):
        $ guideSuggestedPage = 237
        sn "Oh, fuck... I forgot you were taken. Right?"
        scene ep12_pinkrose14 with dissolve
        menu:
            "A dance is fine":
                if breakup:
                    mc "It's complicated. But a dance is fine."
                else:
                    mc "Yeah, but a dance is fine."
            "I don't need a dance":
                mc "It's fine; I don't need a dance. I'm happy to watch you girls in the cages."
        scene ep12_pinkrose15 with dissolve
        sn "*{i}Whispers{/i}* I wasn't talking about a dance."
        sn "What a shame."
        $ new_bio("Sandy", "Sandy wanted to have some fun, but remembered that I didn't want to do that with her anymore.")
    else:
        scene ep12_pinkrose14 with dissolve
        mc "It's fine; I don't need a dance. I'm happy to watch you girls in the cages."
        scene ep12_pinkrose15 with dissolve
        sn "*{i}Whispers{/i}* I wasn't talking about a dance."
        sn "Oh, well... What a shame."
        $ new_bio("Sandy", "Sandy wanted to have some fun, but I declined.")
label ep12_pinkrose_sandy3_label:
scene ep12_pinkrose26 with dissolve
le "I'd give both my nuts to bang Sandy."
scene ep12_pinkrose27 with dissolve
mc "Gonna be a weird orgasm for you."
scene ep12_pinkrose28 with dissolve
le "Um... Wouldn't I still be able to cum?"
scene ep12_pinkrose29 with dissolve
jm "Without balls? No way."
scene ep12_pinkrose28 with dissolve
le "But what about dudes who get vasectomies? They can still cum."
scene ep12_pinkrose29 with dissolve
jm "Now that's a thinker..."
jump ep12_pinkrose_sandy4_label

label ep12_ts_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ money = 5
    play music "music/ep12/licensed_music/track201.mp3"
    queue music ["music/ep12/licensed_music/track200.mp3","music/ep12/licensed_music/track201.mp3"]
hide screen new_phone_screen
$ ep12_ts_lewd = True
scene ep12_ts_lewd1
show screen dance_filter_screen
with dissolve
tan "The problem is, we'd better come back with some money, or the boss will get suspicious."
scene ep12_ts_lewd2 with dissolve
sn "Why do you have to be the voice of reason now, of all times?"
scene ep12_ts_lewd3 with dissolve
tan "I'm just looking out for us."
scene ep12_ts_lewd4 with dissolve
show screen newmoneymsg
menu:
    "[m_c1]Pay them {color=#36ca2b}$$${/color}" if money > 2 or _in_replay:
        $ ep12_full_service = True
        hide screen newmoneymsg
        if not _in_replay:
            $ mny(-3)
        scene ep12_ts_lewd9 with dissolve
        mc "Will this do?"
        scene ep12_ts_lewd10 with dissolve
        sn "See! [name] got us covered."
        scene ep12_ts_lewd11 with dissolve
        tan "That will buy us the time we need. Haha!"
        scene ep12_ts_lewd8 with dissolve
        sn "It's time to get naked!"
    "Don't pay them":
        $ ep12_full_service = False
        hide screen newmoneymsg
        scene ep12_ts_lewd5 with dissolve
        mc "I wish I had money on me to cover for you, but I don't."
        scene ep12_ts_lewd6 with dissolve
        sn "And I hate to admit that Tania's right..."
        sn "It's not gonna stop us, but we can't savor it for too long."
        scene ep12_ts_lewd7 with dissolve
        tan "Sorry..."
        scene ep12_ts_lewd8 with dissolve
        sn "Don't be sorry; be naked."
scene ep12_ts_lewd12 with dissolve
tan "I think he's the one who should get naked."
scene ep12_ts_lewd13 with dissolve
mc "Whoa, whoa... Easy there, ladies."
scene ep12_ts_lewd14 with dissolve
tan "Nuh-uh."
if ep12_full_service:
    scene ep12_ts_lewd15 with dissolve
    sn "*{i}Lick lick{/i}*"
    scene ep12_ts_lewd16 with dissolve
    tan "*{i}Smack{/i}*"
    scene ep12_ts_lewd17 with dissolve
    mc "Tongues and kisses... You're spoiling me."
    scene ep12_ts_lewd18 with dissolve
    $ renpy.pause()
    scene ep12_ts_lewd19 with dissolve
    $ renpy.pause()
scene ep12_ts_lewd20 with dissolve
sn "Do your job, Tania. Dance for him."
scene ep12_ts_lewd21 with dissolve
tan "And what is your job?"
scene ep12_ts_lewd22 with dissolve
sn "A blowjob."
scene ep12_ts_lewd23 with dissolve
tan "Aha... I see how it is."
scene ep12_ts_lewd24 with dissolve
$ renpy.pause()
scene anim_ts_bj1_ep12 with dissolve
mc "Oh, fuck..."
sn "*{i}Suck suck{/i}*"
mc "Yeah... Suck my cock, Sandy."
mc "Damn... You sure know how to do that... Wow..."
sn "Mmmppfff!"
pause
if ep12_full_service:
    jump ep12_ts_lewd_loop1b_label
    label ep12_ts_lewd_loop1_label:
    scene anim_ts_bj1_ep12 with dissolve
    label ep12_ts_lewd_loop1b_label:
    menu:
        "Watch Tania dance":
            scene anim_ts_bj2_ep12 with dissolve
            pause
            jump ep12_ts_lewd_loop1_label
        "Boobjob":
            scene anim_ts_boobjob1_ep12 with dissolve
            sn "Wanna feel my tits around your cock, [name]?"
            mc "I can feel them already...and yes. Keep going."
            sn "I bet I could milk every drop of your cum with my tits."
            mc "You could. That's why I'm focusing on not cumming early."
            sn "Haha... Good, [name]. I've got more plans for you."
            pause
            jump ep12_ts_lewd_loop1b_label
        "Switch to Tania":
            scene ep12_ts_lewd25 with dissolve
            mc "You're so good at that, Sandy..."
            mc "How about letting Tania in on the action?"
            scene ep12_ts_lewd26 with dissolve
            tan "Mmm... Yes. Give it here..."
            scene anim_ts_bj3_ep12 with dissolve
            tan "*{i}Suck suck glug glug{/i}*"
            mc "Yes... You like that, don't you?"
            label ep12_ts_lewd_loop2_label:
            pause
            menu:
                "Watch Sandy dance":
                    scene anim_ts_bj4_ep12 with dissolve
                    pause
                    scene anim_ts_bj3_ep12 with dissolve
                    jump ep12_ts_lewd_loop2_label
                "Footjob":
                    scene anim_ts_foot1_ep12 with dissolve
                    tan "Let's see how kinky you are..."
                    mc "Shit... You sure like to tease me."
                    $ renpy.pause()
                    scene anim_ts_foot2_ep12 with dissolve
                    tan "Your cock is so big and hard already..."
                    mc "I had a semi the moment you two dragged me in here."
                    $ renpy.pause()
                    jump ep12_ts_lewd_loop2_label
                "Switch to Sandy":
                    scene ep12_ts_lewd27 with dissolve
                    mc "Sandy! Get back here and show her how it's done."
                    jump ep12_ts_lewd_loop1_label
                "Continue":
                    jump ep12_ts_lewd_loop3_label
        "Continue":
            jump ep12_ts_lewd_loop3_label
else:
    scene anim_ts_bj2_ep12 with dissolve
    pause
label ep12_ts_lewd_loop3_label:
scene ep12_ts_lewd28 with dissolve
sn "I think you've had enough warm-up. Here comes mommy..."
scene ep12_ts_lewd29 with dissolve
tan "You're going first, huh? Jealous..."
scene ep12_ts_lewd30 with dissolve
mc "You'll get your turn."
sn "That is, if he can handle me."
scene anim_ts_ride1_ep12 with dissolve
sn "*{i}Moans{/i}* Ahh! Fuck!"
mc "Shiiit. That's a lot to handle."
sn "I'm putting you to the test."
pause
scene anim_ts_ride2_ep12 with dissolve
tan "*{i}Smack{/i}* Mmm..."
pause
scene anim_ts_ride3_ep12 with dissolve
tan "*{i}Smack{/i}* Wow, he's balls deep. If he had a normal-sized cock, it wouldn't be as surprising."
sn "And I love every inch of it! *{i}Moans{/i}*"
pause
scene ep12_ts_lewd32 with dissolve
tan "Hngn... Seriously... How big is that thing?"
scene ep12_ts_lewd31 with dissolve
mc "I haven't measured it."
scene ep12_ts_lewd33 with dissolve
sn "Let's see if you can take it."
scene ep12_ts_lewd34 with dissolve
tan "Hngn... I'm sure I can. Fuck!"
scene anim_ts_doggy1_ep12 with dissolve
mc "That's such a sexy ass."
if ep12_full_service:
    tan "I bet you'd want to fuck it too."
    tan "Give me a heads-up before you do."
else:
    tan "*{i}Moans{/i}* Don't get too carried away now. We can't be in here for that long."
pause
scene anim_ts_doggy2_ep12 with dissolve
tan "Hngnn! God damn! It's as thick as it's long!"
sn "Don't I know it? Take it, slut."
tan "*{i}Moans{/i}*"
pause
$ tmpInt = 0
$ tmpBool3 = False
label ep12_ts_lewd_loop4_label:
menu:
    "Cowgirl (Sandy)":
        $ tmpInt += 1
        scene anim_ts_ride1_ep12 with dissolve
        tan "*{i}Smack{/i}*"
        sn "Hnhn... Fuck! Give me that dick, [name]."
        pause
        scene anim_ts_ride2_ep12 with dissolve
        tan "*{i}Smack{/i}*"
        pause
        scene anim_ts_ride3_ep12 with dissolve
        pause
        jump ep12_ts_lewd_loop4_label
    "Cowgirl (Tania)":
        $ tmpInt += 1
        scene anim_ts_ride4_ep12 with dissolve
        tan "*{i}Moans{/i}* Fuck..."
        sn "Isn't his cock the best?"
        pause
        scene anim_ts_ride5_ep12 with dissolve
        tan "It's so good."
        pause
        jump ep12_ts_lewd_loop4_label
    "Doggystyle (Tania)":
        $ tmpInt += 1
        scene anim_ts_doggy1_ep12 with dissolve
        sn "Fuck her, [name]. She's loves getting railed like that."
        pause
        scene anim_ts_doggy2_ep12 with dissolve
        tan "Yes! Fuck me! Fuck me!"
        pause
        jump ep12_ts_lewd_loop4_label
    "Doggystyle (Anal)" if ep12_full_service:
        $ tmpInt += 1
        if not tmpBool3:
            $ tmpBool3 = True
            scene ep12_ts_lewd35 with dissolve
            sn "Hey, let's try anal over here. I have an idea."
            scene ep12_ts_lewd36 with dissolve
            mc "That looks delicious..."
            scene ep12_ts_lewd37 with dissolve
            sn "Come, now. Don't be shy."
        menu:
            "Fuck Sandy":
                label ep12_ts_lewd_loop4b_label:
                scene anim_ts_chair1_ep12 with dissolve
                sn "*{i}Moans{/i}* That's right. Push it in. Push it all in..."
                pause
                scene anim_ts_chair2_ep12 with dissolve
                sn "How does that ass feel?"
                mc "It's tight and amazing..."
                pause
                scene anim_ts_chair3_ep12 with dissolve
                sn "Are you gonna give Tania a piece of it too?"
                pause
                menu:
                    "Fuck Tania":
                        jump ep12_ts_lewd_loop4c_label
                    "Continue":
                        jump ep12_ts_lewd_loop4_label
            "Fuck Tania":
                label ep12_ts_lewd_loop4c_label:
                scene anim_ts_chair4_ep12 with dissolve
                tan "Ahhh... Fuck! *{i}Moans{/i}*"
                sn "You love it, don't you?"
                tan "Yes... Yes!"
                pause
                scene anim_ts_chair5_ep12 with dissolve
                pause
                menu:
                    "Fuck Sandy":
                        jump ep12_ts_lewd_loop4b_label
                    "Continue":
                        jump ep12_ts_lewd_loop4_label
    "Doggystyle (Sandy)":
        $ tmpInt += 1
        scene anim_ts_doggy4_ep12 with dissolve
        tan "Give it to her, [name]. In and out... Do it faster!"
        sn "*{i}Moans{/i}*"
        pause
        scene anim_ts_doggy5_ep12 with dissolve
        tan "Yes... That's so hot!"
        sn "You're getting off to it, aren't you?"
        pause
        scene anim_ts_doggy6_ep12 with hpunch
        tan "*{i}Moans{/i}* Hngn... Yes... He looks so hot fucking you."
        pause
        jump ep12_ts_lewd_loop4_label
    "Missionary":
        $ tmpInt += 1
        scene anim_ts_miss1_ep12 with dissolve
        sn "That's it, [name]. Fuck her. Give it to her good."
        sn "Look at that slut taking your cock with ease."
        tan "*{i}Moans{/i}*"
        pause
        scene anim_ts_miss2_ep12 with dissolve
        sn "You just know she wants it."
        tan "Yes! Yes! I want it."
        pause
        scene anim_ts_miss3_ep12 with dissolve
        sn "Don't stop fucking her, [name]."
        pause
        jump ep12_ts_lewd_loop4_label
    "Missionary (Anal)" if ep12_full_service:
        $ tmpInt += 1
        scene anim_ts_miss1_anal_ep12 with dissolve
        sn "Fuck! Yes! Mmm..."
        mc "Is it too fast?"
        pause
        scene anim_ts_miss2_anal_ep12 with dissolve
        sn "No, I love it up my ass. Give it to me!"
        pause
        scene anim_ts_miss3_anal_ep12 with dissolve
        sn "There you go... There you go. Fuck me, [name]!"
        pause
        jump ep12_ts_lewd_loop4_label
    "Cum" if tmpInt > 3:
        menu:
            "In mouth":
                scene anim_ts_bj5_ep12 with dissolve
                sn "Mhm... Are you going to cum, [name]? It looks like you are."
                mc "Yeah... I'm close."
                sn "Let Tania suck that cum out."
                mc "I'm gonna bust..."
                pause
                scene ep12_ts_lewd38 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_ts_lewd38 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_ts_lewd38 at vpunch, cum1
                mc "Ahhh!!!"
                scene ep12_ts_lewd39 with dissolve
                tan "Mmm..."
            "On ass":
                scene anim_ts_doggy5_ep12 with dissolve
                sn "Mhm... Are you going to cum, [name]? It feels like you are."
                mc "Yeah... I'm close."
                sn "Shoot it all over my ass!"
                mc "I'm gonna bust..."
                pause
                scene ep12_ts_lewd40 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_ts_lewd40 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_ts_lewd40 at vpunch, cum2
                mc "Ahhh!!!"
                scene ep12_ts_lewd41 with dissolve
                mc "Fuck..."
            "On pussy":
                scene anim_ts_miss2_ep12 with dissolve
                sn "Mhm... Are you going to cum, [name]? It looks like you are."
                mc "Yeah... I'm close."
                tan "Give me that cum, [name]!"
                mc "I'm gonna bust..."
                pause
                scene ep12_ts_lewd42 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_ts_lewd42 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_ts_lewd42 at vpunch, cum2
                mc "Ahhh!!!"
                scene ep12_ts_lewd43 with dissolve
                mc "Fuck..."

scene ep12_ts_lewd44 with dissolve
mc "Girls... That was amazing and just what I needed."
scene ep12_ts_lewd45 with dissolve
sn "You should drop by more often, [name]."
scene ep12_ts_lewd46 with dissolve
tan "Oh! We'll see you for the party on New Year's Eve, right?"
scene ep12_ts_lewd44 with dissolve
mc "Let me guess, Tommy already sent you an invite."
scene ep12_ts_lewd46 with dissolve
tan "Earlier today, yeah."
scene ep12_ts_lewd44 with dissolve
mc "I hope he extended it to all of you."
scene ep12_ts_lewd45 with dissolve
sn "We'll be there."

$ renpy.end_replay()
$ persistent.ep12_lewd_ts = True
$ calcScenes()
$ new_bio("Sandy", "I had a threesome with Sandy and Tania in a private room at The Pink Rose.")
$ mphone_stats_add_girl_s3("sandy","You had a threesome with Sandy and Tania in a private room at the Pink Rose in episode 12.")
$ mphone_stats_add_girl_s3("tania","You had a threesome with Sandy and Tania in a private room at the Pink Rose in episode 12.")
show screen new_phone_screen

label ep12_pinkrose_sandy4_label:
scene ep12_pinkrose30 with dissolve
if ep12_ts_lewd:
    mc "Hey... I'm back. How's it hanging?"
else:
    mc "How's it hanging? You seem low."
scene ep12_pinkrose31 with dissolve
de "Something is wrong with me tonight. This isn't doing anything for me."
scene ep12_pinkrose32 with dissolve
mc "I think I know what it is. It's about Ashley, yeah?"
scene ep12_pinkrose31 with dissolve
de "You might be right about that."
scene ep12_pinkrose32 with dissolve
mc "What happened after you two kissed?"
scene ep12_pinkrose31 with dissolve
de "I took it as she wanted to be with me. But she felt bad about ending it with Anthony."
scene ep12_pinkrose33 with dissolve
de "Part of me wants to fight harder for her, but I feel like I already put all my cards on the table."
de "Do you think I should give her space?"
scene ep12_pinkrose34 with dissolve
mc "The ball is in her court. You've shown her what you want, and she seemed to want it too."
mc "If that's the case, she'll come to you."
scene ep12_pinkrose35 with dissolve
de "Space it is."
de "But I'm telling you... Watching these tits does nothing for me."
scene ep12_pinkrose37 with dissolve
stri "That's so rude!"
scene ep12_pinkrose36 with dissolve
mc "Don't mind him; he's going through some stuff. Your boobs are delightful."
stop music fadeout 3
scene ep12_pinkrose38 with dissolve
$ renpy.pause()

label ep12_sjade_label:
if not ep4_toldDerekAboutJade and ep12_break_or_tell != "tell":
    jump ep12_pre_diary_label
hide screen new_phone_screen
play music "music/ep3/black_box.mp3"
scene ep12_sjade1
hide screen dance_filter_screen
with wiperight
ja "Your father and I had a relationship crisis, and it culminated in divorce."
scene ep12_sjade6 with dissolve
if ep3_acceptedJade and not ep4_fuckedJade:
    if branchSage:
        sa "And how does a relationship crisis lead to you giving my boyfriend a handjob!?"
    else:
        sa "And how does a relationship crisis lead to you giving my friend a handjob!?"
else:
    if branchSage:
        sa "And how does a relationship crisis lead to you having sex with my boyfriend!?"
    else:
        sa "And how does a relationship crisis lead to you having sex with my friend!?"
scene ep12_sjade2 with dissolve
ja "I know! I did a horrible thing! I didn't tell you because I wanted to spare you from the truth."
if branchSage:
    ja "He was just a student when I met him. I didn't do that with him when I learned he was your boyfriend."
else:
    ja "He was just a student when I met him. I didn't do that with him when I learned he was your friend."
scene ep12_sjade6 with dissolve
sa "Are you even listening to your words? He was a student! Why on earth did you even do it to begin with!?"
scene ep12_sjade3 with dissolve
ja "It's all because of your father."
scene ep12_sjade8 with dissolve
sa "My father? Yeah, of course, you will jump at a chance to blame him for your mistakes."
scene ep12_sjade2 with dissolve
ja "Listen to me. I wanted to spare the details and avoid hurting you, but if you leave me no choice, I will tell you the ugly truth."
scene ep12_sjade7 with dissolve
sa "At this point, you fucking better!"
scene ep12_sjade3 with dissolve
ja "I always had a hunch that your father was a cheater."
ja "And I found out that your father cheated on me with not just one student, but three."
scene ep12_sjade9 with dissolve
sa "Dad had sex with three students?"
scene ep12_sjade3 with dissolve
ja "He admitted it."
scene ep12_sjade10 with dissolve
sa "..."
scene ep12_sjade2 with dissolve
ja "I was furious with him. He made me feel worthless as a wife and woman."
ja "And I wanted to hurt him in the same way he hurt me."
scene ep12_sjade4 with dissolve
ja "[name] attended my class, and I came on to him. I flirted with him and pushed his limits."
ja "He responded to my advances, and you seem to know the rest."
scene ep12_sjade11 with dissolve
sa "You came on to him first?"
scene ep12_sjade4 with dissolve
ja "I did. I took advantage of my position as his teacher, and I'm ashamed of it."
scene ep12_sjade8 with dissolve
sa "How did it feel, Mom? Did it feel good?"
sa "Did you get your sweet revenge on Dad?"
sa "Was he angry at you? Did he love you more for it?"

if ep4_toldDerekAboutJade:
    scene ep12_sjade2 with dissolve
    ja "Your father threatened to use that recording and ruin my career. He used it as leverage in our divorce to make me settle for less money."
    ja "And even after I submitted to his demands and signed the papers to protect my family from this..."
    scene ep12_sjade3 with dissolve
    ja "That recording is out there."
    ja "I will have to resign to get away from it."
else:
    scene ep12_sjade2 with dissolve
    ja "I never used it against him. And he was the one who asked for a divorce without even knowing about what I did."
scene ep12_sjade5 with dissolve
ja "He's the one who betrayed me and ruined our family."

scene ep12_sjade12 with dissolve
if branchSage:
    sa "I lost my boyfriend because of you."
else:
    sa "I lost my close friend because of you."
sa "And all I hear is you saying how sorry you are for yourself."
sa "Do you understand how this affects me? Do you even care?"
scene ep12_sjade13 with dissolve
ja "Of course, I care. It was never my intention to hurt you."
ja "If I could take it all back, I would."
scene ep12_sjade15 with dissolve
sa "I don't believe you."
scene ep12_sjade14 with dissolve
ja "I'm telling you the truth."
scene ep12_sjade15 with dissolve
sa "But I don't believe it."
stop music fadeout 3
scene ep12_sjade16 with dissolve
$ renpy.pause()

label ep12_pre_diary_label:
show screen new_phone_screen
play music "music/ep10/licensed_music/track139.mp3"
scene ep12_pre_diary1
hide screen dance_filter_screen
with fade
$ renpy.pause()
scene ep12_pre_diary2 with dissolve
mc "(Study... Study... Study...)"
mc "(Tomorrow is the big day. I feel as ready as I can be for it.)"
mc "(Rusty told me he always takes the day before an exam off, but that feels risky.)"
scene ep12_pre_diary3 with dissolve
mc "(What if I missed some information and finally understood it today?)"
mc "(Yet, I can't come up with what that would be. I feel uninspired to read more.)"
mc "(Maybe I should follow Rusty's advice.)"
scene ep12_pre_diary4 with dissolve
mc "(Oh, I know. I could start planning the New Year's Eve party.)"
mc "(Sharing a party with the jocks is going to be something different. I have a feeling there will be too many people to please.)"
mc "(I'll focus on the DIKs and our guests as normal and leave some room for discussion.)"
scene ep12_pre_diary5 with dissolve
mc "Rusty. I'm gonna start planning the New Year's Eve party today. Is there any news on that front I need to know?"
scene ep12_pre_diary7 with dissolve
rs "Oh, great! I'm not at home right now, but I can swing by your room soon to help out."
scene ep12_pre_diary5 with dissolve
mc "Sounds great."
scene ep12_pre_diary7 with dissolve
rs "But if you want to get started before that, I checked the guest list last night. Between the jocks, the HOTs, and us, the guest list is bigger than usual."
scene ep12_pre_diary5 with dissolve
mc "How do you want to handle it?"
scene ep12_pre_diary8 with dissolve
rs "We talked about splitting the dining rooms, and I think that will be the case. Sage managed to book a venue on campus that is perfect for it."
scene ep12_pre_diary9 with dissolve
mc "Oh, awesome! That makes my job a lot easier. What's the venue?"
scene ep12_pre_diary8 with dissolve
rs "There's an old building on the north end of campus. It's not that far off from the examination hall."
rs "Sage also found a caterer for the event - if we want one that is. We have to decide on the menu and how much we want to spend on food and drinks."
rs "I can fix the alcohol."
scene ep12_pre_diary5 with dissolve
mc "What do you need me to do?"
scene ep12_pre_diary7 with dissolve
rs "Check the budget for our end of the party. Calculate the costs based on 100-150 guests."
scene ep12_pre_diary6 with dissolve
mc "That many, huh?"
scene ep12_pre_diary7 with dissolve
rs "Yeah. Many are interested."
rs "Oh, and we'll need fireworks! The jocks will buy some, but we should chip in."
scene ep12_pre_diary5 with dissolve
mc "So, the party will pretty much be: dining, dancing, drinking, and topping it off with some fireworks."
scene ep12_pre_diary7 with dissolve
rs "Yeah. Sounds about right. If you can come up with something else, go for it. I bet the others have ideas too."
rs "Talk to you in a bit."
scene ep12_pre_diary5 with dissolve
mc "See you soon."
scene ep12_pre_diary10 with dissolve
mc "(That was helpful. Let me do some math here...)"
$ guideSuggestedPage = 237
$ pp_activity_choices = [2,1,2]
if not minigames:

    $ pp_nm_party_preference = [[1,0,0],[2,0,2],[1,1,1],[0,0,-1],[-1,-1,-1],[1,0,-1],[2,-1,0],[-1,1,2]]
    $ pp_nm_activity_description = [["Fancy Buffet","Decent Buffet","Don't care","Not Cheap Buffet"],["Card Game","Don't care"],["Fireworks","Some Fireworks","Don't care","Anything"]]
    $ currentActivity = 0
    $ pp_money = 20
else:
    $ pp_money = 20

scene ep12_pre_diary11 with dissolve
if not minigames:
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "For that many guests... It comes down to this... Hm... How much do we wanna spend on food?"
menu:
    "Fancy Buffet ($4)" if minigames or pp_money > 3:
        $ pp_money -= 4
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 0
        mc "Probably a lot. New Year's Eve should have a feast to remember."
    "Decent Buffet ($2)" if minigames or pp_money > 1:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_money -=2
        $ pp_activity_choices[0] = 1
        mc "A nice dinner. Nothing over the top. That will keep the entry fee down, too."
    "Cheap Buffet":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[0] = 2
        mc "Eh... We'll choose the cheapest options. Food isn't that important."

scene ep12_pre_diary12 with dissolve
if not minigames:
    $ currentActivity = 1
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "(Dancing and drinking are the way to go. I know we usually have games and such, but now that we're planning this together with the HOTs and the jocks...)"
mc "(Maybe I'll leave those decisions up to them. But if things get boring, we could have a cheap backup plan.)"
menu:
    "Card Game ($4)" if minigames or pp_money > 3:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 0
        $ pp_money -= 4
        mc "(Let's play some kind of party game. There are cheap card games that would be fun and easy to break out if needed.)"
    "Nothing":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[1] = 1
        mc "(Nah... I don't think we need any extra activities for this party. If the others disagree, then that's their problem to solve.)"

scene ep12_pre_diary11 with dissolve
if not minigames:
    $ currentActivity = 2
    show screen pp_dik_preferences_screen
else:
    show screen pp_dik_budget_screen
mc "What about fireworks...?"
menu:
    "Fireworks ($4)" if minigames or pp_money > 3:
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 0
        $ pp_money -= 4
        mc "This is worth spending money on. Let's put on a spectacular show. I don't trust the jocks with this."
    "Some Fireworks ($2)":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 1
        $ pp_money -= 2
        mc "Since the jocks will buy fireworks, we can contribute to the show with some of our own."
    "No Fireworks":
        hide screen pp_dik_preferences_screen
        hide screen pp_dik_budget_screen
        $ pp_activity_choices[2] = 2
        mc "We can save money here. We have the same venue as the jocks, and they will buy fireworks. We'll mooch off of them."

if minigames:
    hide screen new_phone_screen
    stop music fadeout 3
    mc "Alright... What's next?"
    $ tmpMenu = quick_menu
    $ quick_menu = 0
    play music "music/ep12/licensed_music/track211.mp3"
    queue music ["music/ep11/licensed_music/track182.mp3","music/ep10/licensed_music/track147.mp3","music/ep12/licensed_music/track211.mp3"]
    show screen pp_intro_screen
    pause
    label ep12_play_label:
    $ tmp_list = [-1,-1]
    $ pp_tut_state = 0
    show screen pp_bg_screen_ep12

    $ pp_round = 4
    $ pp_continue_label = "ep12_pp_cont_label"
    $ renpy.block_rollback()
    jump party_planner_setup_round_label
    label ep12_pp_cont_label:
    hide screen pp_bg_screen_ep12
    $ quick_menu = tmpMenu
    stop music fadeout 3
    show screen new_phone_screen
    mc "(Let's go with this.)"
    play music "music/ep10/licensed_music/track139.mp3"
else:
    label ep12_lock_in_label:
    $ pp_nm_tmp_happiness = [0,0,0,0,0,0,0,0]
    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][0] == -1 and pp_activity_choices[0] != 2:
                pp_nm_tmp_happiness[i] += 1
            elif pp_nm_party_preference[i][0] == pp_activity_choices[0] and pp_activity_choices[0] != 2:
                pp_nm_tmp_happiness[i] += 1
    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][1] == pp_activity_choices[1] and pp_activity_choices[1] == 0:
                pp_nm_tmp_happiness[i] += 1

    python:
        for i in range(0,8):
            if pp_nm_party_preference[i][2] == -1 and pp_activity_choices[2] != 2:
                pp_nm_tmp_happiness[i] += 1
            elif pp_nm_party_preference[i][2] == pp_activity_choices[2] and pp_activity_choices[2] != 2:
                pp_nm_tmp_happiness[i] += 1

    python:
        for i in range(0,8):
            if pp_nm_tmp_happiness[i] > 1:
                pp_nm_tmp_happiness[i] = 1
                pp_current_party_happiness[i] = 1
            elif pp_nm_tmp_happiness[i] == 1:
                pp_nm_tmp_happiness[i] = 0
                pp_current_party_happiness[i] = 0
            else:
                pp_nm_tmp_happiness[i] = -1
                pp_current_party_happiness[i] = -1
    python:
        for i in range(0,8):
            pp_nm_tmp_happiness[i] += pp_nm_dik_happiness[i]
            if pp_nm_tmp_happiness[i] < 0:
                pp_nm_tmp_happiness[i] = 0
            elif pp_nm_tmp_happiness[i] > 3:
                pp_nm_tmp_happiness[i] = 3

    show screen pp_nm_happiness_screen
    menu:
        "{i}Are you done planning the activities?{/i}"
        "Done":
            $ renpy.block_rollback()
            hide screen pp_nm_happiness_screen
            python:
                for i in range(0,8):
                    pp_nm_dik_happiness[i] = pp_nm_tmp_happiness[i]
            mc "All done."
        "Start over":
            hide screen pp_nm_happiness_screen
            $ currentActivity = 0
            $ pp_money = 10
            show screen pp_dik_preferences_screen
            menu:
                "Fancy Buffet ($4)" if pp_money > 3:
                    $ pp_money -= 4
                    $ pp_activity_choices[0] = 0
                "Decent Buffet ($2)" if minigames or pp_money > 1:
                    $ pp_money -=2
                    $ pp_activity_choices[0] = 1
                "Cheap Buffet":
                    $ pp_activity_choices[0] = 2
            $ currentActivity = 1
            menu:
                "Card Game ($4)" if pp_money > 3:
                    $ pp_activity_choices[1] = 0
                    $ pp_money -= 4
                "Nothing":
                    $ pp_activity_choices[1] = 1
            $ currentActivity = 2
            menu:
                "Fireworks ($4)" if pp_money > 3:
                    $ pp_activity_choices[2] = 0
                    $ pp_money -= 4
                "Some Fireworks ($2)" if pp_money > 1:
                    $ pp_activity_choices[2] = 1
                    $ pp_money -= 2
                "No Fireworks":
                    $ pp_activity_choices[2] = 2
            hide screen pp_dik_preferences_screen
            jump ep12_lock_in_label


$ ep12_pp_food = pp_activity_choices[0]
$ ep12_pp_game = pp_activity_choices[1]
$ ep12_pp_fireworks = pp_activity_choices[2]
if minigames:
    python:
        for x in range(0,len(pp_needs_met)):
            tmpInt = 0
            for y in pp_needs_met[x]:
                if y:
                    tmpInt += 1
            pp_current_party_happiness[x] = tmpInt

scene ep12_pre_diary12 with dissolve
mc "(Looks good... I'll wait for Rusty to plan the rest.)"
scene ep12_pre_diary13 with dissolve
mc "(Now what...?)"
scene ep12_pre_diary14 with dissolve
mc "(I'm not gonna study...)"
mc "(But I will read something while I wait for Rusty.)"
stop music fadeout 3
scene ep12_pre_diary15 with dissolve
mc "(Please, Mom... No more detailed sex escapades.)"
$ guideSuggestedPage = 241
label ep12_diary_label:
hide screen new_phone_screen
play music "music/ep12/licensed_music/track206.mp3"
scene ep11_diary93 with dissolve
ln "My first time with Neil was wonderful."
mc "(Mom... I get it! Stop! Derek didn't flip the fucking page!)"
scene ep12_diary4 with dissolve
ln "Dear diary. I'm sorry for not writing in you much lately. I've been rather busy..."
scene ep12_diary5 with dissolve
ln "With Neil."
scene ep12_diary6 with dissolve
ln "I don't intend to brag, but since that first time, we snuck away almost daily to do it again."
scene ep12_diary7 with dissolve
ln "Before work..."
scene ep12_diary8 with dissolve
$ renpy.pause()
scene ep12_diary9 with dissolve
ln "During his lunch breaks..."
scene ep12_diary10 with dissolve
ln "After work..."
ln "And aside from the hot sex, he treats me so well..."
ln "Maybe it's fast, but I believe I'm falling in love with him."
scene ep12_diary11 with dissolve
ln "However... I have a huge dilemma!"
ln "Mom found out about it. And as we didn't tell her about us, you can probably guess in what way she found out."
ln "It was horrible."
scene ep12_diary12 with dissolve
ln "I confessed to her what I'd been doing with Neil, and she lectured me on why I'd done something wrong."
ln "But to me, the only thing that I did wrong was getting caught by her."
scene ep12_diary13 with dissolve
ln "She still sees me as a little girl. But I'm an adult now, Mom."
ln "I'm allowed to make my own \"bad\" choices."
ln "Mom told me to break it off with Neil, or she would have to tell Dad."
scene ep12_diary14 with dissolve
ln "Dad will be furious if he learns about Neil."
ln "But I don't want to break it off with Neil. Should I lie to Mom?"

scene ep12_diary15 with dissolve
dad "You shouldn't have to lie to your mom. And I don't care if your dad finds out about us."
scene ep12_diary17 with dissolve
ln "How can you say that?"
scene ep12_diary16 with dissolve
dad "Because eventually he would. What we're doing together means more than sex and hanging out to me."
dad "We could last beyond the time I have left here."
scene ep12_diary17 with dissolve
ln "Left here? Are you leaving?"
scene ep12_diary15 with dissolve
dad "Not right now. But I'm only here to help finish building the hotel. After that, who knows where work takes me."
scene ep12_diary18 with dissolve
ln "I don't want you to leave. I want you to stay."
scene ep12_diary16 with dissolve
dad "Do you feel it too? There's something special between us."
scene ep12_diary18 with dissolve
ln "I do."
ln "But when Mom doesn't accept it, how can I expect Dad to?"
scene ep12_diary19 with dissolve
ln "And I was right. Mom told Dad, and he didn't accept it."

show ep12_diary20
if not persistent.ep12_cardcam12:
    show screen ep12_render_screen("cam12")
with dissolve
dad3 "I am paying you to work here, not to defile my daughter!"
show ep12_diary21
hide screen ep12_render_screen
with dissolve
dad3 "You've taken advantage of your position as a worker and of our generosity."
dad3 "You were never allowed to walk about our premises for any purpose other than what was necessary to do your job. You've been trespassing!"
scene ep12_diary22 with dissolve
dad3 "This is a gross violation of your contract, and I will sue you for this. Not just your company; I will hold you personally liable for your transgressions."
dad3 "It does not matter that she's an adult! You have crossed lines that should not have been crossed."
dad3 "You're fired!"
play sound "sound_effects/hit.mp3"
scene ep12_diary23 with hpunch
dad3 "OW!"
play sound "sound_effects/hit.mp3"
scene ep12_diary23 with hpunch
dad3 "STOP IT!"
play sound "sound_effects/hit.mp3"
scene ep12_diary23 with hpunch
$ renpy.pause()
play sound "sound_effects/door_slam.mp3"
scene ep12_diary24 with dissolve
dad3 "GET THE HELL OFF MY PROPERTY!"
scene ep12_diary25 with dissolve
dad3 "GET THE HELL OUT!!!"
ln "Dad! Please, don't... I love him."
scene ep12_diary26 with dissolve
dad3 "That boy is trash! Do you hear me?"
dad3 "He is trash. And no daughter of mine will be associated with the likes of him."
show screen new_phone_screen
stop music fadeout 5
scene ep12_diary1 with dissolve
mc "(Huh? What?)"
mc "(Dad assaulted grandpa? And he was fired for it? He never told me that.)"
scene ep12_diary2 with dissolve
mc "(I knew my grandpa didn't like him, but he never mentioned that he threatened him with a lawsuit...)"
mc "(What the hell?)"
scene ep12_diary3 with vpunch
play sound "sound_effects/thud.mp3"
mc "(What was that? It came from the bathroom.)"

$ new_bio("Dad", "According to Mom's diary, Dad punched my grandpa when he was fired from his job.")
$ new_bio("Lynette", "Mom was told to stop dating Dad, but she wouldn't.")

label ep12_tommy_label:
play music "music/ep5/suspense5.mp3"
scene ep12_tommy1 with dissolve
play sound "sound_effects/door_knock.mp3"
"*Door knocking*"
mc "Everything alright in there? I heard a thud."
scene ep12_tommy3 with dissolve
tm "H-help."
scene ep12_tommy2 with dissolve
mc "What's that?"
scene ep12_tommy3 with dissolve
tm "Help!"
play sound "sound_effects/door_lock.mp3"
scene ep12_tommy4 with dissolve
mc "The door is locked. Hold on."
scene ep12_tommy5 with dissolve
$ renpy.pause()
play sound "sound_effects/door_lock.mp3"
scene ep12_tommy6 with dissolve
$ renpy.pause()
scene ep12_tommy10 with dissolve
mc "Tommy!? Tommy!? Did you fall?"
scene ep12_tommy11 with dissolve
tm "Get me the bag from my fridge."
scene ep12_tommy12 with dissolve
mc "The bag!? What bag!?"
scene ep12_tommy11 with dissolve
tm "Behind the bar."
scene ep12_tommy7 with dissolve
rs "Hey? What's the rush?"
scene ep12_tommy8 with dissolve
mc "Something is wrong with Tommy! He needs some kind of a bag."
scene ep12_tommy9 with dissolve
rs "Oh, shit! It's in his fridge."
scene ep12_tommy13 with dissolve
rs "Tommy? Do you need us to call for paramedics?"
scene ep12_tommy14 with dissolve
tm "Give it to me."
scene ep12_tommy15 with dissolve
$ renpy.pause()
scene ep12_tommy16 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_tommy17 with dissolve
$ renpy.pause()
scene ep12_tommy18 with dissolve
mc "What now?"
play music "music/ep7/licensed_music/track58.mp3"
scene ep12_tommy19 with dissolve
rs "He'll be fine."
scene ep12_tommy18 with dissolve
mc "How can you be sure?"
scene ep12_tommy19 with dissolve
rs "It's not the first time this has happened. He needed a glucagon shot."
scene ep12_tommy18 with dissolve
mc "A glucagon shot?"

play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg43
mc "Dad taught me everything I know. He knows all kinds of stuff."
scene ep10_pre_tg44 with dissolve
tm "That's fucking cool."
play sound "sound_effects/whoosh_2.mp3"
scene ep10_pre_tg45
mc "Why don't you like me?"
scene ep10_pre_tg46 with dissolve
tm "I do! We're bonding here, aren't we?"
scene ep10_pre_tg45 with dissolve
mc "You're drunk! Where are the shots?"
play sound "sound_effects/whoosh_2.mp3"
scene ep12_tommy20
tm "Alright, since you're sharing, I'm gonna let you in on something personal, too."
tm "But don't fucking tell anyone, it's a DIK secret."
scene ep12_tommy21 with dissolve
mc "Hand on my balls, I won't tell anyone."
scene ep12_tommy20 with dissolve
tm "I've got diabetes. That's why I can't do too many of those shots with you."
scene ep12_tommy21
mc "Don't worry! I can handle them all by myself!"
play sound "sound_effects/whoosh_2.mp3"

scene ep12_tommy23
mc "He's got diabetes."
scene ep12_tommy22 with dissolve
mc "The needles..."
scene ep12_tommy26 with dissolve
rs "He called the DIKs' secret code for this. That's how it became a thing."
scene ep12_tommy24 with dissolve
tm "My blood sugar levels were too low."
tm "I had a stressful day yesterday and woke up without realizing it had affected me..."
scene ep12_tommy25 with dissolve
tm "Thanks for bursting in here. If you hadn't... I..."
scene ep12_tommy27 with dissolve
$ renpy.pause()

scene ep12_tommy28 with dissolve
$ renpy.pause()
scene ep12_tommy29 with dissolve
mc "How do you feel now?"
scene ep12_tommy30 with dissolve
tm "Drained."
tm "I usually take good care of myself, but some days it sneaks up on me. When that happens, I can't help it."
scene ep12_tommy31 with dissolve
tm "You might have noticed that I sometimes behave weirdly."
scene ep12_tommy34 with dissolve
mc "I think you're gonna have to be more specific."
scene ep12_tommy31 with dissolve
tm "It happens that I snap, get sweaty, or delirious."
scene ep12_tommy34 with dissolve
mc "I saw that happen, maybe once or twice. I didn't think much of it. I thought you were hungover or pissed off."
scene ep12_tommy30 with dissolve
tm "Nah. It happens when my blood sugar levels are off. I try to hide it as best as I can by eating alone and taking my shots when no one's around."
tm "Haven't you noticed that I don't always sit with you guys at dinner or show up late?"
scene ep12_tommy34 with dissolve
mc "Yeah. But I figured that's how you are."
mc "Honestly, I had forgotten that you told me about it once at the Pink Rose."
scene ep12_tommy30 with dissolve
tm "When I was young, I almost died from it. I was too young to remember, but in a short time I lost a lot of weight."
scene ep12_tommy31 with dissolve
tm "One day, I couldn't stop drinking soda. It was like my thirst couldn't be quenched."
tm "I downed a big-ass bottle in minutes but kept wanting more."
scene ep12_tommy32 with dissolve
tm "I collapsed on the floor, and Mom got crazy scared. She took me to the hospital, and after some tests, they found out the problem."
tm "Type 1 diabetes. My body couldn't take up any nutrients from the food without the insulin."
scene ep12_tommy30 with dissolve
tm "I had to learn how to self-medicate, but I fucking hated the needles. I still do."
tm "I remember crying like a bitch daily when I had to do it myself."
tm "And back then, I had to do it with every meal. And that meant doing it at school."
scene ep12_tommy31 with dissolve
tm "I was bullied mercilessly for it. They'd take my bag of insulin and throw it to each other over my head."
tm "One time, they broke the insulin vial, and Mom had to bring me a new one."
scene ep12_tommy35 with dissolve
mc "Tommy... That's horrible."
scene ep12_tommy32 with dissolve
tm "Those events stuck with me. I get so fucking mad thinking about it still."
scene ep12_tommy33 with dissolve
tm "That fucking Evan!"
scene ep12_tommy34 with dissolve
mc "Who?"
scene ep12_tommy32 with dissolve
tm "The asshole who kept calling me Tummy Tommy throughout junior high because he saw me stick the needle in my stomach for the insulin."
tm "Well, that short fuckface didn't grow up to be big, and I got to beat his ass in high school every time he even glanced in my direction."
scene ep12_tommy33 with dissolve
tm "Still... I fucking hate him."
scene ep12_tommy34 with dissolve
mc "I was bullied in school too... I know how much it hurts."
scene ep12_tommy30 with dissolve
tm "I don't medicate in front of people, and I don't want people to know about it."
tm "In the early days of the DIKs, Vinny started poking fun at it. I snapped as if it were Evan in front of me, and we got into a fight."
tm "This disease already controls my life. I didn't want the bad shit I left in high school to follow me in college."
scene ep12_tommy31 with dissolve
tm "After the fight with Vinny, we came up with the DIKs' secret code, and I used mine for my diabetes."
tm "I don't like people talking about it."
scene ep12_tommy35 with dissolve
mc "It's good to have those closest to you know about it, though. In cases like today."
scene ep12_tommy34 with dissolve
mc "I always thought your needles were heavy drugs or something."
mc "I saw one or two lying around."
scene ep12_tommy30 with dissolve
tm "It would have been a hell of a lot cooler if they were."
scene ep12_tommy34 with dissolve
mc "Nah. It wouldn't."
scene ep12_tommy36 with dissolve
$ renpy.pause()

if ep9_heather_lewd == 2:
    scene ep12_tommy34 with dissolve
    mc "I know things haven't been great between us lately..."
    mc "I want to apologize again for what I did to Heather."
    scene ep12_tommy31 with dissolve
    tm "I don't want to hear about it."
    scene ep12_tommy35 with dissolve
    mc "It was stupid."
    scene ep12_tommy31 with dissolve
    tm "I've done worse things than that. Let it go."

scene ep12_tommy30 with dissolve
tm "I'm gonna lie down for a while."
tm "Help yourself to a beer if you want one."
scene ep12_tommy34 with dissolve
mc "I'll check up on you later."
scene ep12_tommy37 with dissolve
tm "What are you? My nurse? There's no need to check up on me; I'm all good now."
scene ep12_tommy38 with dissolve
mc "Yeah, there's the Tommy I know."
scene ep12_tommy39 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_tommy40 with dissolve
$ renpy.pause()
$ new_bio("Tommy", "I helped Tommy when he had a medical emergency. He told me about his diabetes, and it explained a lot.")
$ new_bio("Rusty", "Rusty told me that Tommy started the DIKs' secret code as a way to not have people mock him for his diabetes.")

label ep12_mains_label:
hide screen new_phone_screen
if not ep4_toldDerekAboutJade and ep12_break_or_tell == "break" and branchSage and breakup and not branchZoey:
    play music "music/ep12/licensed_music/track217.mp3"
    scene ep12_mains1 with dissolve
    js "Are you sure he didn't give you a reason?"
    scene ep12_mains36 with dissolve
    sa "I begged him for one, but he just wanted our relationship to end."
    sa "It was so out of the blue."
    scene ep12_mains7 with dissolve
    my "It does sound odd... Do you think he was lying?"
    scene ep12_mains36 with dissolve
    sa "I thought there was someone else, and I asked him about that. But he said there weren't."
    sa "I don't know what to think."
    scene ep12_mains37 with dissolve
    sa "Why would he break up with me without a reason?"
    scene ep12_mains38 with dissolve
    isa "I can't speak for him, but maybe he didn't have deep enough feelings for you and wanted to spare you from heartbreak."
    scene ep12_mains36 with dissolve
    sa "He said he didn't feel something, but I called him out on that, too. I don't believe him."
    scene ep12_mains38 with dissolve
    isa "I know it must feel hard to accept that he doesn't feel the same about you, but if that's what he says... Maybe that was his reason."
    scene ep12_mains36 with dissolve
    sa "But it doesn't line up with how it's been between us."
    sa "There were no signs of a breakup. Sure, we had some stupid fights here and there, but we were on good terms."
    scene ep12_mains17 with dissolve
    sa "I don't get it."
    sa "And I feel like I have ruined him for you guys now, too."
    scene ep12_mains7 with dissolve
    my "It's a hard situation for all of us - especially you."
    scene ep12_mains8 with dissolve
    my "It's tough for us to be caught in the middle of it."
    my "I sympathize with you, but I'm also his friend. And trying to defend him makes me feel like I'm upsetting you."
    scene ep12_mains29 with dissolve
    isa "That goes for all of us. But we are adults, and we understand that this is complicated."
    isa "I don't think Sage expects us to choose sides. She needs our support, and she has it."
    scene ep12_mains15 with dissolve
    sa "Yeah, I'm not stupid. I know you're his friend. If you still want to be that, don't let me stop you."
    sa "But I don't think I can be around him when you are. *{i}Sigh{/i}*"
    stop music fadeout 3
    scene ep12_mains35 with dissolve
    $ renpy.pause()
elif ep4_toldDerekAboutJade or ep12_break_or_tell == "tell":
    play music "music/ep12/licensed_music/track217.mp3"
    scene ep12_mains1 with dissolve
    js "No. I'm sorry, but that does not excuse her."
    scene ep12_mains2 with dissolve
    if ep3_acceptedJade and not ep4_fuckedJade:
        js "I get that she felt hurt, but doing that with a student to retaliate..."
    else:
        js "I get that she felt hurt, but sleeping with a student just because your dad did it..."
    js "It's a plain weird and wrong response."
    scene ep12_mains7 with dissolve
    my "So, she used [name] to feel better? Did I get that right?"
    scene ep12_mains15 with dissolve
    sa "She tried to justify it, but in the same breath, she admitted she was wrong and blamed Dad for everything."
    sa "I mean, fuck! Pick a lane, will you?"
    scene ep12_mains7 with dissolve
    if ep3_acceptedJade and not ep4_fuckedJade:
        my "It seems like it was more complex than just the act. And it validates what [name] said, too."
    else:
        my "It seems like it was more complex than just sex. And it validates what [name] said, too."
    scene ep12_mains16 with dissolve
    sa "What?"
    scene ep12_mains7 with dissolve
    my "They were both oblivious to how it would affect you."
    scene ep12_mains15 with dissolve
    sa "Let's say that I buy into that [name] wouldn't have done it, if he knew that she was my mother."
    sa "Does that make it any better?"
    scene ep12_mains3 with dissolve
    js "Not by much, no."
    scene ep12_mains8 with dissolve
    my "It's hard to say. I still want to believe that [name] is better than this."
    scene ep12_mains19 with dissolve
    sa "What do you two think?"
    scene ep12_mains22 with dissolve
    ji "You know what I think. I haven't changed my mind since you first told me."
    if branchJill:
        ji "There's no excuse for what either of them did. And I can't be with someone who would do something like that."
        scene ep12_mains5 with dissolve
        js "What did he say when you broke up with him?"
        scene ep12_mains23 with dissolve
        ji "He said it was a mistake and that it had nothing to do with me."
        ji "And since it didn't involve me, he didn't get why I would break up with him over it."
        ji "He doesn't understand that it speaks to his character. To me, it revealed everything I needed to know about him."
    else:
        ji "There's no excuse for what either of them did. Period."
    if branchIsabella:
        scene ep12_mains24 with dissolve
        ji "But... How do you feel, Bella?"
        scene ep12_mains27 with dissolve
        isa "It was a rude awakening. How else can I put it?"
        isa "After the initial shock subsided, I reflected on how [name] and I started our relationship."
        isa "And with that in mind, I look at what he did with Jade with more understanding."
        scene ep12_mains21 with dissolve
        sa "You understand him?"
        scene ep12_mains29 with dissolve
        isa "I understand how it could have happened, but that doesn't mean that I accept it."
        if ep4_toldDerekAboutJade:
            isa "And I accept it much less, considering that he recorded the act to show his friends for Hell Week."
            scene ep12_mains27 with dissolve
            isa "Hell Week or not, you don't do that to someone."
            scene ep12_mains15 with dissolve
            sa "Exactly... It's humiliating."
        else:
            scene ep12_mains15 with dissolve
            sa "Exactly... It's unacceptable behavior."
        scene ep12_mains24 with dissolve
        ji "Did you break up with him?"
        if branchZoey:
            scene ep12_mains28 with dissolve
            isa "Yes, but for a different reason altogether. He wanted to get back together with his ex-girlfriend Zoey."
            scene ep12_mains24 with dissolve
            ji "Are you kidding me?"
            scene ep12_mains28 with dissolve
            isa "I'm not."
            isa "In one fell swoop, he managed to change the way I looked at him."
        else:
            scene ep12_mains28 with dissolve
            isa "I was on the verge of doing it, but I asked him for some time to think."
            isa "Does this one bad thing he did negate every other good thing he did?"
            isa "Is it unforgivable? Can I look past it?"
        scene ep12_mains27 with dissolve
        isa "And after talking to you tonight..."
        isa "I fear there's no going back to how it was."
    else:
        scene ep12_mains29 with dissolve
        isa "I don't think you're out of line to have this reaction."
        isa "If I put myself in your shoes, I'd feel hurt and betrayed too."
        scene ep12_mains27 with dissolve
        isa "Regardless of intent, it doesn't change what they did together."
        isa "Truthfully, I would have a hard time forgiving either of them."
    scene ep12_mains28 with dissolve
    isa "Looking around the room, I can see how divided you are. Will you be able to call him a friend after this?"
    scene ep12_mains15 with dissolve
    sa "I know I won't."
    if branchSage:
        sa "I feel disgusted with myself for having been his girlfriend. I'll never wash this dirty feeling off..."
    else:
        sa "He may have good sides, but there are things you don't do."
        sa "And I think that's why it hurts this much. It would have been so much easier if he were pure evil, but he's not."
    stop music fadeout 3
    scene ep12_mains35 with dissolve
    $ renpy.pause()
elif branchZoey and breakup:
    play music "music/ep12/licensed_music/track217.mp3"
    if branchSage:
        scene ep12_mains15 with dissolve
        sa "He told me she was his friend. And I expressed my concerns about that to him."
        sa "I was 100%% right about her. And [name] not caring about my feelings makes me think he knew he was still in love with her the moment she returned from San Diego."
        scene ep12_mains3 with dissolve
        js "I'm so sorry to hear that."
        scene ep12_mains7 with dissolve
        my "So, he lied about his feelings to you?"
        scene ep12_mains17 with dissolve
        sa "That's what I think, yeah. I asked him if he cheated on me, but he didn't consider making out with Zoey cheating."
        scene ep12_mains22 with dissolve
        ji "That's not right. He can't justify that to make himself look better."
        scene ep12_mains2 with dissolve
        js "Yeah. Kissing someone else while you're in a relationship is cheating. He should have owned that."
        scene ep12_mains19 with dissolve
        sa "Why did he even want me to be his girlfriend while building something up with Zoey?"
        sa "I feel like I don't know him."
        scene ep12_mains17 with dissolve
        sa "And I feel like I have ruined him for you guys now, too."
        scene ep12_mains7 with dissolve
        my "It's a hard situation for us all - especially you."
        my "I don't like how [name] handled it. The moment he felt something for Zoey, he should have been up front with you."
        my "The way he wasn't makes it hard for me to defend him."
        scene ep12_mains8 with dissolve
        my "And it's also hard because we're caught in the middle of it."
        my "I sympathize with you, but I'm also his friend. And trying to defend him makes me feel like I'm upsetting you."
        scene ep12_mains29 with dissolve
        isa "That goes for all of us. But we are adults and we understand that this is complicated."
        isa "I don't think Sage expects us to choose sides. She needs our support, and she has it."
        scene ep12_mains27 with dissolve
        isa "I think we all agree that [name] could have handled it better and that he hurt Sage by cheating on her. She didn't deserve that."
        scene ep12_mains15 with dissolve
        sa "Yeah, I'm not stupid. I know you're his friend. If you still want to be that, do whatever you want."
        sa "But I won't be around him when you are. And I definitely won't be around Zoey."
        scene ep12_mains25 with dissolve
        ji "No one is asking you to do that."
        scene ep12_mains3 with dissolve
        js "This is so sad. *{i}Sigh{/i}*"
    elif branchMayaJosy:
        scene ep12_mains1 with dissolve
        if ep12_josy_hurt:
            js "Everything we built together he was willing to throw away for Zoey. I feel so fooled."
        else:
            js "In hindsight, I'm not surprised. We had some great times, but it was always going to be complicated between us."
            scene ep12_mains3 with dissolve
            js "I can't fault him for getting together with Zoey, but I can't stay friends with him."
        scene ep12_mains19 with dissolve
        sa "I'm sorry it happened like that."
        sa "It feels scummy for him to get into a relationship with her and to break up with you over it."
        sa "It would have been easier to digest if he had broken it off because he wasn't into you."
        scene ep12_mains3 with dissolve
        js "I think he was into us at one point. But when Zoey returned to his life, he realized we weren't his true love."
        scene ep12_mains26 with dissolve
        ji "How do you feel, Maya?"
        if ep12_maya_hurt:
            scene ep12_mains9 with dissolve
            my "It's been hard. I love him."
            my "And now, all of a sudden, I'm not supposed to do that anymore."
            scene ep12_mains10 with dissolve
            my "I'm having difficulties wrapping my head around that."
            my "I'm glad that he's happy, but I wish he were happy with me."
            scene ep12_mains32 with dissolve
            isa "..."
        else:
            scene ep12_mains10 with dissolve
            my "[name] means a lot to me, but like I told him..."
            my "It's not that kind of love."
            scene ep12_mains9 with dissolve
            my "Maybe I would have felt that way at some point - I was attracted to him in many ways, after all..."
            my "But I can't know for sure."
            scene ep12_mains11 with dissolve
            my "And he seemed sure about his love for Zoey."
            my "So... In the big picture, it doesn't matter how I feel."
            scene ep12_mains31 with dissolve
            isa "Of course, it matters how you feel."
            isa "Just because [name] feels different, it doesn't mean your feelings aren't worth something."
            scene ep12_mains13 with dissolve
            my "I feel some relief. I don't have to push myself to find out if I love him that way."
            my "Maybe movies are wrong about it, but I want to believe that love is supposed to be easy. And this wasn't. So..."
        scene ep12_mains14 with dissolve
        my "You probably feel awful about this situation, too."
        my "Bad parts aside, we've had some nice times together as a group lately."
        my "I'm unsure if that will happen again."
        scene ep12_mains18 with dissolve
        sa "We're together now, aren't we?"
        scene ep12_mains14 with dissolve
        my "Yeah, but [name] was a big part of it."
        scene ep12_mains26 with dissolve
        ji "Even if it's different, we're still here for both of you."
        ji "As for [name]... Time will tell."
    elif branchJill:
        scene ep12_mains6 with dissolve
        js "He told you that there wasn't anything going on between him and Zoey?"
        scene ep12_mains23 with dissolve
        ji "He reassured me of it. He lied to my face. *{i}Sigh{/i}*"
        scene ep12_mains9 with dissolve
        my "Is there any chance he didn't know he felt that way?"
        scene ep12_mains26 with dissolve
        ji "I don't see it. He spent time with her on several occasions and invited her to parties."
        ji "What was his intention in doing that?"
        scene ep12_mains23 with dissolve
        ji "I feel naive for trusting his word after I felt a hunch that something was wrong."
        scene ep12_mains28 with dissolve
        isa "Ask yourself what you could have done differently."
        scene ep12_mains24 with dissolve
        ji "Like how?"
        scene ep12_mains28 with dissolve
        isa "Let's say you forbade him from spending time with Zoey. Would that have made it better?"
        scene ep12_mains24 with dissolve
        ji "I don't think posing an ultimatum is healthy for a relationship."
        scene ep12_mains27 with dissolve
        isa "You're right. It's not."
        isa "You did the right thing. You communicated with him and trusted his words."
        scene ep12_mains23 with dissolve
        ji "I withheld how I truly felt. I didn't tell him how much it scared me."
        scene ep12_mains19 with dissolve
        sa "But that's not why it fell apart, Jill."
        sa "In my opinion, nothing you could have said would have changed it."
        scene ep12_mains20 with dissolve
        sa "He kept putting himself in a position where his feelings for her grew."
        sa "And since she was his first girlfriend, it should have been obvious to him how he felt about her."
        scene ep12_mains19 with dissolve
        sa "I don't know if he cheated on you physically, but he sure as hell cheated on you emotionally."
        sa "Feelings aren't just turned on and off in an instant."
        scene ep12_mains5 with dissolve
        js "I don't buy that he wasn't aware of his feelings either."
        js "You trusted him and treated him in a way he didn't deserve. You're way too good for him."
        scene ep12_mains23 with dissolve
        ji "I wish I could let it go. I hate that he makes me feel this way."
        scene ep12_mains12 with dissolve
        my "We're here for you."
    else:
        scene ep12_mains33 with dissolve
        ji "It wasn't because of your past?"
        scene ep12_mains27 with dissolve
        isa "No. He felt guilty because the timing of the breakup was horrible."
        isa "I believe he was worried about my mental health, but I assured him that I could handle it."
        scene ep12_mains21 with dissolve
        sa "You are alright, aren't you?"
        scene ep12_mains29 with dissolve
        isa "You don't have to worry about me either."
        scene ep12_mains13 with dissolve
        my "Of course, we worry about you. That's what friends do."
        scene ep12_mains27 with dissolve
        isa "I appreciate it, but really, I'll be fine."
        isa "I've been to hell and back. I'm determined to stay here now."
        scene ep12_mains4 with dissolve
        js "So, he broke up with you because of Zoey? Was that the real reason?"
        scene ep12_mains30 with dissolve
        isa "Yes. Apparently, he is still in love with her."
        isa "And honestly, our relationship has been difficult since the beginning."
        isa "We couldn't even tell our friends about it. It jeopardized my friendship with Jill, and it was unethical in several ways."
        scene ep12_mains27 with dissolve
        isa "Maybe it was for the better that it ended."
        scene ep12_mains21 with dissolve
        sa "Does that make you feel better, that there's a convenient reason for it to end?"
        sa "You and [name] seem to have connected since you first met. It doesn't seem like it was a shallow deal."
        scene ep12_mains29 with dissolve
        isa "You're right. Convenience is the only positive side to it."
        isa "I did enjoy our relationship, and he made me feel loved again - a feeling I've missed dearly."
        scene ep12_mains27 with dissolve
        isa "*{i}Sigh{/i}* But this is how relationships go. Some last, some don't."
        isa "For me, I think it was important to take this step with him. If anything, it has shown me that I am moving in the right direction."
        scene ep12_mains24 with dissolve
        ji "I wish he had treated you better than this."
        scene ep12_mains28 with dissolve
        isa "He treated me well, Jill."
        scene ep12_mains24 with dissolve
        ji "It makes me mad that he risked our friendship for your relationship, and then threw it away to be with his ex-girlfriend."
        ji "That's a bitter pill for me to swallow."
        scene ep12_mains27 with dissolve
        isa "It's ok to feel angry or sad about that. I'm sad too."
        scene ep12_mains13 with dissolve
        my "We'll be here for you if you need anything."
        scene ep12_mains27 with dissolve
        isa "I can see that. Your friendship will help me get through this."
    stop music fadeout 3
    scene ep12_mains34 with dissolve
    $ renpy.pause()

label ep12_qv_label:
hide screen new_phone_screen
play music "music/ep6/licensed_music/track33.mp3"
scene ep12_qv13 with wipeleft
$ renpy.pause()
play sound "sound_effects/cellphone.mp3"
scene ep12_qv14 with dissolve
"*{i}Phone rings{/i}*"
scene ep12_qv15 with dissolve
qu "Yeah?"
scene ep12_qv16 with dissolve
uk "They're coming for us."
scene ep12_qv17 with dissolve
qu "Who is this?"
scene ep12_qv1 with dissolve
vi "It's over, Quinn. Buddy has it out for us."
scene ep12_qv17 with dissolve
qu "Vinny...? What do you mean?"
scene ep12_qv2 with dissolve
vi "He's not done with us. He's out to get us, and I'm not sticking around for it."
scene ep12_qv17 with dissolve
qu "Slow down! What happened?"
scene ep12_qv3 with dissolve
vi "I thought we had worked it out - Buddy and I..."
vi "But he sent Mick to snuff me. That's what I'm saying."
scene ep12_qv18 with dissolve
qu "What the fuck? Are you serious?"
scene ep12_qv3 with dissolve
vi "I shot him."
scene ep12_qv19 with dissolve
qu "..."
scene ep12_qv18 with dissolve
qu "You shot Mick?"
scene ep12_qv4 with dissolve
vi "He had to go. It was either gonna be him or me."
scene ep12_qv19 with dissolve
qu "Is he dead?"
scene ep12_qv3 with dissolve
vi "Yeah, he's gone."
scene ep12_qv5 with dissolve
vi "This is all because that fucking stripper cunt couldn't keep her mouth shut."
scene ep12_qv20 with dissolve
qu "I'm not following."
scene ep12_qv4 with dissolve
vi "Lily. She fucked me over by snitching to Mick."
vi "Take whatever cash you have left and get the fuck out while you can."
scene ep12_qv22 with dissolve
qu "Why would I trust you? You ratted me out and hurt my friend."
scene ep12_qv3 with dissolve
vi "No, no. That's not all true."
scene ep12_qv22 with dissolve
qu "That's bullshit! I know you did. I heard Rio recognize you over the phone when you grabbed her."
scene ep12_qv3 with dissolve
vi "Yeah, I did that with Mick, but I didn't touch her after. That was all them."
vi "I thought they'd threaten her, not beat her up."
scene ep12_qv23 with dissolve
qu "Beat her up!? They ripped the piercings off her fucking face, Vinny!"
scene ep12_qv4 with dissolve
vi "It's not my fault they went apeshit on her!"
vi "Look! You fucking stole my customers, and it pissed me off. Something had to be done!"
scene ep12_qv23 with dissolve
qu "What you did was way worse. You snitched on me."
scene ep12_qv5 with dissolve
vi "And you snitched back. And Buddy cut my fucking face up!"
scene ep12_qv22 with dissolve
qu "So why would I trust you?"
scene ep12_qv6 with dissolve
vi "Because we're in the same boat and it's sinking. I'm jumping ship."
vi "I'll only warn you once more. Stay away from Buddy's place. Don't go back there. He'll be waiting for you."
scene ep12_qv20 with dissolve
qu "What? Buddy...will be waiting for me at his place?"
scene ep12_qv6 with dissolve
vi "Are you deaf? That's what I've been saying this whole time."
vi "Buddy changed his mind. He wanted me gone for what I did."
vi "And I think you're next. Especially now that Mick's dead..."
scene ep12_qv21 with dissolve
qu "(He doesn't know Buddy is in jail...)"
scene ep12_qv3 with dissolve
vi "Consider us even. Don't go back there."
scene ep12_qv20 with dissolve
qu "Is that what this is about? You want to make things right?"
scene ep12_qv3 with dissolve
vi "Somewhere along the road, we drifted apart, you and I."
vi "I never wanted us to be enemies, but the competition got to me, and lines were blurred. Consider this as my parting gift to you for the trouble I got both of us into."
scene ep12_qv15 with dissolve
qu "Where are you going?"
scene ep12_qv2 with dissolve
vi "Far from here. I'm already gone."
vi "I never called you."
scene ep12_qv7 with dissolve
$ renpy.pause()
scene ep12_qv8 with dissolve
$ renpy.pause()
scene ep12_qv6 with dissolve
vi "Hi. I have an anonymous tip. Who do I talk to?"
scene ep12_qv9 with dissolve
vi "There's this strip club in the city..."
vi "Well, they say it's a strip club, but it's also a brothel."
scene ep12_qv10 with dissolve
vi "Yeah, yeah. Some of the girls there sell sex in the back rooms, and I've seen them use drugs."
vi "Yeah, most of the girls working there use it. And lots of it."
vi "And I heard from a buddy of mine that they let in underage guys, too."
scene ep12_qv11 with dissolve
vi "The Pink Rose."
vi "That's what I know. Yeah."
vi "Yeah... That's the one."
stop music fadeout 3
scene ep12_qv12 with dissolve
$ renpy.pause()

label ep12_finals_label:
play music "music/ep12/licensed_music/track207.mp3"
hide screen new_phone_screen
scene ep12_finals1 with wipeleft
$ renpy.pause()
scene ep12_finals2 with dissolve
mc "Hey, Arieth. What are you doing here?"
scene ep12_finals3 with dissolve
ar "I'm here for the math test, dummy."
ar "The Professor said if I passed the finals, I'd get a passing grade."
scene ep12_finals4 with dissolve
mc "Oh. Are you retaking it? You weren't in our class this semester."
scene ep12_finals5 with dissolve
ar "Well, I missed the exam last spring because I mixed up the dates..."
ar "...and the time before that, my score wasn't the best."
scene ep12_finals4 with dissolve
mc "Good luck to you today, then."
scene ep12_finals3 with dissolve
ar "No luck needed. It's just math."
ar "And that's what I like about it. There are no wrong answers."
scene ep12_finals6 with dissolve
$ renpy.pause()

scene ep12_finals7 with dissolve
de "One more math test, then we're free from this class..."
scene ep12_finals8 with dissolve
mc "There's a math class next semester, too, dude. And I doubt it will be easier."
scene ep12_finals9 with dissolve
de "Son of a bitch! I forgot about that."
de "Hey, what classes did you register for?"
scene ep12_finals8 with dissolve
mc "Well, we still have the Applied Chemistry class..."
mc "Then, I registered for Introduction to College Research, Mathematical Statistics, and Engineering Economics."
scene ep12_finals9 with dissolve
de "Economics? Why did you choose that?"
scene ep12_finals8 with dissolve
mc "I figured it would be useful. What about you?"
scene ep12_finals10 with dissolve
de "I just clicked on the recommended classes. So, we should be the same."
scene ep12_finals8 with dissolve
mc "The econ class isn't mandatory. You had to choose one class as an extra."
scene ep12_finals11 with dissolve
de "But... I clicked the recommended ones..."
scene ep12_finals12 with dissolve
mc "Uh... They base that list on what you've already studied, along with suggested follow-up courses and such."
scene ep12_finals11 with dissolve
de "Dear God... No..."
scene ep12_finals13 with dissolve
de "*{i}Phew{/i}* Oh, thank you! I went with something cool."
de "I clicked on Masculinity Studies. You got me worried there."
scene ep12_finals19 with dissolve
mc "What's that?"
scene ep12_finals13 with dissolve
de "Let me see..."
de "The class focuses on a critical examination of manhood..."
scene ep12_finals14 with dissolve
de "...from a feminist perspective-"
scene ep12_finals15 with dissolve
de "NO!!! FUCK!"
scene ep12_finals17 with dissolve
de "[mc_de_up]! It's a social studies class!"
scene ep12_finals18 with dissolve
mc "You should read before you click on things..."
scene ep12_finals16 with dissolve
de "The class will deconstruct manhood and focus on the damaging effects men's ideals have on men and social life."
de "What's wrong with being manly!? Is there anything they won't pick a fight with?"
de "Why don't they make a class about womanhood and how to lose weight and dress sexier instead?"
scene ep12_finals17 with dissolve
de "I'm going to kill myself!"
de "Why would they give a feminist class a cool name like that!?"
de "They fooled me!"
scene ep12_finals18 with dissolve
mc "Stop it. You didn't even know what you signed up for."
scene ep12_finals17 with dissolve
de "I'm not going! I'm not."
scene ep12_finals18 with dissolve
mc "Registration ended in November. It's too late to change it."
scene ep12_finals13 with dissolve
de "The class is held by Dr. Jade Burke..."
scene ep12_finals20 with dissolve
mc "At least you don't have to kill yourself. She'll do it for you."
scene ep12_finals21 with dissolve
de "Can this day get any worse?"
scene ep12_finals22 with dissolve
ph "Hehe. Hold on to that thought; the test hasn't begun yet."
ph "Your phone, please."

scene ep12_finals23 with dissolve
ph "Good morning, everyone."
ph "Well, this is it. The day you've all been studying hard for."
scene ep12_finals24 with dissolve
ph "You have four hours at your disposal. The test covers the entire curriculum, and it consists of 12 in-depth problems for you to solve."
ph "A word of advice: make sure that you provide every step needed to reach your solution."
ph "You will not gain full points for incomplete solutions."
scene ep12_finals26 with dissolve
ph "That said, you may also earn points for partial solutions."
ph "So, even if you feel the question is too hard and you can't quite solve it..."
ph "Do your best, and maybe you'll get some extra points for your effort."
scene ep12_finals25 with dissolve
ph "Remember... It's always better to try than not to write anything at all."
scene ep12_finals24 with dissolve
ph "Before you begin, make sure that you write your student ID at the top of each paper along with the other information."
ph "Papers with incomplete information at the top won't be graded."
scene ep12_finals23 with dissolve
ph "Please, respect your neighbors during the test."
ph "Good luck! You may begin when you receive the test."
scene ep12_finals27 with dissolve
mc "(Here we go... This is what I have studied for.)"

if minigames:
    play music "music/ep3/sing_along_with_jim.mp3"
    $ renpy.block_rollback()
    $ qM = quick_menu
    $ quick_menu = 0
    $ math_jump_label = "after_math_setup_ep12_label"
    jump math_setup_ep12_label
    label after_math_setup_ep12_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_ep12_label"
    show screen math_screen
    $ renpy.pause()

    label after_math_ep12_label:
    $ renpy.block_rollback()
    $ math_jump_label = "after_math_result_ep12_label"
    $ quick_menu = qM
    hide screen math_screen
    hide screen math_tool_tip_screen
    show screen math_result_screen
    $ renpy.pause()
    label after_math_result_ep12_label:
    $ renpy.block_rollback()
    hide screen math_result_screen
    stop music fadeout 3

if minigames:
    if steamAchievements and not config.console and not config.developer:
        if maxedMathS3 == 3:
            $ achievement.grant("IDS3_16")
            init:
                $ achievement.register("IDS3_16")
            $ achievement.Sync()
    scene ep12_finals28 with wipeleft
    play music "music/ep11/licensed_music/track172.mp3"
else:
    scene ep12_finals28 with fade
mc "(That's it... I can't come up with better solutions than these.)"
scene ep12_finals29 with dissolve
mc "(Many have already left... I guess it's my turn.)"
if ep8_midterms_cheated == "DIK":
    scene ep12_finals30 with dissolve
    mc "(Hoff watched me with eagle eyes...)"
    mc "(But I'm happy I sat in the front rows. That way I could prove that I wasn't up to something.)"
else:
    scene ep12_finals31 with dissolve
    $ renpy.pause()
if ep8_midterms_cheated == "DIK":
    scene ep12_finals34 with dissolve
    ph "How did it go?"
    scene ep12_finals33 with dissolve
    mc "I tried my best."
    scene ep12_finals32 with dissolve
    ph "You looked focused. That's good. Keep it up."
    $ new_bio("Philip", "Professor Hoff watched me closely during the finals.")
else:
    scene ep12_finals32 with dissolve
    ph "Well done, [name]."
    scene ep12_finals33 with dissolve
    mc "We'll see."
$ guideSuggestedPage = 251
$ new_bio("Derek", "Derek accidentally registered for another gender studies class.")
show screen new_phone_screen
if ep12_nicole_path:
    scene ep12_finals35 with wiperight
    "*{i}Phone rings{/i}*"
    scene ep12_finals36 with dissolve
    mc "Hey, Nicole. What's up?"
    $ guideSuggestedPage = 252
    if ep12_nicole_dating > 0:
        scene ep12_finals37 with dissolve
        nic "I talked to Sandy, and she told me what you said."
        scene ep12_finals38 with dissolve
        mc "Whoa... What's wrong? What did I say?"
        scene ep12_finals37 with dissolve
        nic "What's wrong? Really?"
        $ ep12_nicole_breakup = True
        if ep12_nicole_dating == 2:
            nic "You told her we were just fucking...not dating."
            scene ep12_finals39 with dissolve
            nic "But you know that's not the truth. You know how we talked about calling and seeing each other more."
            scene ep12_finals40 with dissolve
            mc "I didn't feel like it was her business to know about what you and I do."
            scene ep12_finals39 with dissolve
            nic "Oh, stop it! You went into a private room, and had sex with her and Tania."
            menu:
                "It was just sex":
                    scene ep12_finals38 with dissolve
                    mc "It was just sex. It didn't mean anything."
                    scene ep12_finals37 with dissolve
                    nic "I think that's the problem. Nothing seems to mean anything to you."
                    scene ep12_finals40 with dissolve
                    mc "That's harsh."
                    scene ep12_finals37 with dissolve
                    nic "No, it's not. Honestly, I'm going too easy on you."
                "I'm single":
                    scene ep12_finals38 with dissolve
                    mc "So? I'm single."
                    scene ep12_finals37 with dissolve
                    nic "You are, and I get the feeling that's how you like it."
        else:
            scene ep12_finals39 with dissolve
            nic "You told her we were dating but still wanted to do dirty things to her."
            menu:
                "We didn't do anything":
                    scene ep12_finals38 with dissolve
                    mc "We didn't do anything."
                    scene ep12_finals37 with dissolve
                    nic "Because Sandy put a stop to it."
                    nic "There's something called \"intent\", [name]."
                    scene ep12_finals38 with dissolve
                    mc "You and I are dating, but we're not a couple. Sex doesn't have to mean something."
                    scene ep12_finals37 with dissolve
                    nic "I think that's the problem. Nothing seems to mean anything to you."
                    scene ep12_finals40 with dissolve
                    mc "That's harsh."
                    scene ep12_finals37 with dissolve
                    nic "No, it's not. Honestly, I'm going too easy on you."
                "Dating isn't a relationship":
                    scene ep12_finals38 with dissolve
                    mc "So? I'm single. Dating isn't a relationship."
                    scene ep12_finals37 with dissolve
                    nic "Are you for real, [name]? Is this who you are?"

        nic "You know what? Never mind."
        scene ep12_finals39 with dissolve
        nic "I'm happy you're enjoying yourself, but I can't date someone like you anymore."
        if ep12_nicole_dating == 2:
            nic "Sorry... I meant \"fuck you\" anymore. Bye."
        scene ep12_finals41 with dissolve
        mc "*{i}Sigh{/i}* Come on..."
        mc "Ah... Fuck!"
        $ new_bio("Envy", "Nicole dumped me after talking to Sandy about my recent visit to The Pink Rose.")
    else:
        scene ep12_finals42 with dissolve
        nic "I figured I'd call and catch you during lunch. Are you free to talk?"
        scene ep12_finals36 with dissolve
        mc "I'm between tests, but yeah, I can talk for a while."
        scene ep12_finals42 with dissolve
        nic "Tests? Oh, is it exam day?"
        scene ep12_finals36 with dissolve
        mc "It's finals day."
        scene ep12_finals43 with dissolve
        nic "How is it going?"
        scene ep12_finals44 with dissolve
        mc "I just sat through a tricky math test. The professor didn't hold anything back, and neither did I."
        mc "After lunch, I'm taking an English test, and then I'm free!"
        scene ep12_finals43 with dissolve
        nic "Well, you know how to speak English. I'm sure you will pass."
        scene ep12_finals44 with dissolve
        mc "Haha! It isn't that kind of English test."
        scene ep12_finals43 with dissolve
        nic "Say, are you free tonight? Because I am."
        nic "Since it's going to be tricky to find time for it during the holidays... How about a date night? Dinner and drinks at my place?"
        if branchZoey and not wt_ep11_zoey_kiss_others:
            $ ep12_nicole_breakup = True
            scene ep12_finals45 with dissolve
            mc "Nicole... I can't..."
            scene ep12_finals46 with dissolve
            nic "Oh, you've got plans?"
            scene ep12_finals45 with dissolve
            mc "No, I don't. But..."
            mc "I'm getting back together with my ex."
            scene ep12_finals46 with dissolve
            nic "Excuse me?"
            scene ep12_finals45 with dissolve
            mc "I was going to tell you, but I haven't had much spare time this week, and it's fresh."
            scene ep12_finals46 with dissolve
            nic "It has to be, considering we made plans to see each other more at the party. What was that about?"
            scene ep12_finals48 with dissolve
            mc "I know. I feel bad for leading you on, but I didn't know it at the time."
            scene ep12_finals47 with dissolve
            nic "You got your feelings back for your ex in less than a week?"
            scene ep12_finals48 with dissolve
            mc "*{i}Sigh{/i}* No. I think I've had them all this time, but I just learned that she reciprocated."
            scene ep12_finals47 with dissolve
            nic "Wow. That's great to hear, [name]. Really great."
            scene ep12_finals48 with dissolve
            mc "Nicole... I'm sorry."
            scene ep12_finals47 with dissolve
            nic "You could have told me you were in love with her."
            scene ep12_finals45 with dissolve
            mc "I've tried to get over her. I swear."
            mc "How am I supposed to do that without dating?"
            mc "I never meant to hurt you. You're a great girl."
            scene ep12_finals46 with dissolve
            nic "*{i}Sigh{/i}* Whatever, [name]. It is what it is."
            scene ep12_finals49 with dissolve
            $ renpy.pause()
            $ new_bio("Envy", "I told Nicole about Zoey, and she was upset that I hadn't told her sooner.")
        else:
            scene ep12_finals44 with dissolve
            mc "I'm free and want to unwind tonight. That sounds fun!"
            scene ep12_finals42 with dissolve
            nic "I'll help you relax, and you can tell me all about how the finals went."
            scene ep12_finals36 with dissolve
            mc "It's a date. How does 7 p.m. sound?"
            scene ep12_finals42 with dissolve
            nic "Sounds perfect. I can't wait! Good luck on your test."
            scene ep12_finals36 with dissolve
            mc "Thanks! See you later."
            $ new_bio("Envy", "Nicole asked me out for a date after the finals.")
elif breakup or ep4_toldDerekAboutJade:
    scene ep12_finals35 with wiperight
    $ renpy.pause()
    scene ep12_finals50 with dissolve
    $ renpy.pause()
    scene ep12_finals53 with dissolve
    $ renpy.pause()
    scene ep12_finals54 with dissolve
    $ renpy.pause()
    scene ep12_finals55 with dissolve
    $ renpy.pause()
    scene ep12_finals51 with dissolve
    $ renpy.pause()
    scene ep12_finals52 with dissolve
    $ renpy.pause()
    $ new_bio("Maya", "The girls started distancing themselves from me. Maya at least acknowledged me.")
    $ new_bio("Josy", "The girls started distancing themselves from me.")
    $ new_bio("Sage", "The girls started distancing themselves from me.")
    $ new_bio("Isabella", "The girls started distancing themselves from me.")
else:
    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals56 with wiperight
    else:
        scene ep12_finals57 with wiperight
    js "Could that test have been any harder? What the hell was question number 11?"
    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals58 with dissolve
    else:
        scene ep12_finals59 with dissolve
    my "I skipped that one. I felt like I knew about half of the test. Hopefully, my answers were enough to score some extra points."
    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals60 with dissolve
        sa "It sounds like it was a hard one. The first finals in college are usually the worst. That's when you learn where the bar is."
        scene ep12_finals61 with dissolve
        my "I sure hope so because the bar was set high."
    scene ep12_finals63 with dissolve
    js "How did it go for you, [name]?"
    scene ep12_finals64 with dissolve
    mc "We'll see. I hope they publish the answers before Christmas. I'll try to remember what I wrote to cross-check."
    scene ep12_finals65 with dissolve
    js "Ugh. That test was so long... My neck is sore from looking down for four hours."

    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals62 with dissolve
    else:
        scene ep12_finals66 with dissolve
        mc "Let me help you."
        scene ep12_finals67 with dissolve
        js "Aw... Yes. That feels good."
        scene ep12_finals68 with dissolve
    my "For me, it's my hand that hurts from writing."
    my "What's worse is that we have four more hours of it coming."
    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals63 with dissolve
    else:
        scene ep12_finals67 with dissolve
    js "I feel like I'm more prepared for the English test. Maybe I can finish it faster."
    if branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_finals61 with dissolve
    else:
        scene ep12_finals68 with dissolve
    my "If there are plenty of multiple choice questions, we might."

    if branchMayaJosy:
        scene ep12_finals67b with dissolve
        mc "Josy... You know that Tommy has diabetes, yeah?"
        scene ep12_finals67 with dissolve
        js "Why wouldn't I? I've lived together with him."
        scene ep12_finals67b with dissolve
        mc "I was just curious why you never mentioned it to me."
        scene ep12_finals67c with dissolve
        js "His diabetes is not really my business, and besides, he hates it when people bring it up."
        js "Why are you talking about it all of a sudden?"
        scene ep12_finals67b with dissolve
        mc "He...um... Don't tell him I told you this, but he collapsed on the bathroom floor yesterday."
        scene ep12_finals67c with dissolve
        js "Oh! Is he ok?"
        scene ep12_finals67d with dissolve
        mc "Yeah. I heard him fall and helped him together with Rusty."
        scene ep12_finals67c with dissolve
        js "Did you give him his shot?"
        scene ep12_finals67d with dissolve
        mc "Yeah. And after he came to, we had a talk about it. He shared plenty about his disease and growing up with it."
        scene ep12_finals67c with dissolve
        js "Wow... You got him to open up about his diabetes?"
        scene ep12_finals67b with dissolve
        mc "Yeah. I was wondering, though... He seemed pretty chill after it happened, but isn't it life-threatening if he doesn't get that shot?"
        scene ep12_finals67e with dissolve
        js "Potentially, yeah. I saw it happen a few times. He wasn't always the best at taking care of himself."
        js "But I do believe he's gotten better at it."
        scene ep12_finals67b with dissolve
        mc "Should I keep an eye out for him? The reason I'm asking you is that he said I wasn't his nurse when I showed concern."
        scene ep12_finals67e with dissolve
        js "*{i}Scoffs{/i}* Tommy would never ask someone to look out for him. He'd hate it if he knew that you were."
        js "But yeah... I'd appreciate it if you did. And I know Monica would too."
        scene ep12_finals67 with dissolve
        js "But you know, in secret?"
        scene ep12_finals67f with dissolve
        mc "Thanks. I'll be more attentive then."
        scene ep12_finals67g with dissolve
        my "It must have felt scary for you to experience that with him."
        scene ep12_finals67h with dissolve
        mc "Yeah, it shook me. Luckily Rusty showed up and knew what to get from his fridge."
        scene ep12_finals67e with dissolve
        js "I would have told you about his diabetes if I knew that he hadn't."
        scene ep12_finals67f with dissolve
        mc "He told me once, but at that time I was too drunk to remember."
        if branchMayaJosy and check_mlove():
            scene ep12_finals67i with dissolve
            mc "..."
            mc "Oh..."
            mc "I think I remember something else about that night now."
            scene ep12_finals67g with dissolve
            my "What is it?"
            scene ep12_finals67h with dissolve
            mc "Um... Nothing."
            scene ep12_finals67i with dissolve
            mc "(Fuck... Poor Maya.)"

hide screen new_phone_screen
scene ep12_finals69 with wipeleft
$ renpy.pause()
if ep8_midterms_cheated == "DIK":
    scene ep12_finals70 with dissolve
    $ renpy.pause()
    scene ep12_finals71 with dissolve
    $ renpy.pause()
    scene ep12_finals72 with dissolve
    $ renpy.pause()
    scene ep12_finals73 with dissolve
    $ renpy.pause()
    scene ep12_finals74 with dissolve
    $ renpy.pause()
    scene ep12_finals75 with dissolve
    $ renpy.pause()
scene ep12_finals76 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 252
scene ep12_finals77 with dissolve
isa "Alright, listen up. I'm aware many of you had a rough morning with another exam..."
isa "...but I hope you still have some energy left for this one."
scene ep12_finals78 with dissolve
isa "This is your final exam for my class, and it will count for 30%% of your grade."
isa "As always, write your student ID at the top of the papers and fill in the remaining fields too."
scene ep12_finals79 with dissolve
isa "When the test starts, I ask you to remain silent until you're done. If you have any questions during the test, come to my desk."
scene ep12_finals80 with dissolve
mc "(*{i}Phew{/i}* Here we go... One test, and it's 30%% of my grade...)"
if minigames:
    stop music fadeout 3
mc "(One final test, then we're home free.)"

if minigames:
    play music "music/ep3/sing_along_with_jim.mp3"
    $ qM = quick_menu
    $ quick_menu = 0
    $ renpy.block_rollback()
    jump init_eng_test_ep12_label

label after_eng_test_ep12_label:
hide screen word_cheat
if minigames:
    $ renpy.block_rollback()
    $ quick_menu = qM
    play music "music/ep11/licensed_music/track172.mp3"
    if steamAchievements and not config.console and not config.developer:
        if maxedEnglishS3 == 3:
            $ achievement.grant("IDS3_15")
            init:
                $ achievement.register("IDS3_15")
            $ achievement.Sync()
        if maxedEnglishS3 == 3 and maxedMathS3 == 3 and maxedScienceS3 == 3:
            $ achievement.grant("IDS3_14")
            init:
                $ achievement.register("IDS3_14")
            $ achievement.Sync()
    scene ep12_finals81 with wiperight
else:
    scene ep12_finals81 with fade
mc "(Ugh! Focusing like this made me feel like I'm drunk. But that's it... I'm done!)"
mc "(Sweet winter break, here I come.)"

if "Isabella" in breakup or (ep4_toldDerekAboutJade and not branchIsabella) or ep12_break_or_tell == "tell":
    scene ep12_finals82 with dissolve
    isa "Thank you."
    scene ep12_finals87 with dissolve
    mc "Have a nice Christmas, Bella."
    scene ep12_finals88 with dissolve
    isa "You too."
    $ new_bio("Isabella", "Isabella wasn't very chatty with me after the finals.")
else:
    if ep4_toldDerekAboutJade:
        scene ep12_finals82 with dissolve
        isa "Are you off to spend your holiday tonight? Or can I drop by later?"
        scene ep12_finals87 with dissolve
        mc "Sure, I'm not going home for a few more days."
        scene ep12_finals88 with dissolve
        isa "See you soon then."
    else:
        scene ep12_finals83 with dissolve
        isa "Went well?"
        scene ep12_finals84 with dissolve
        mc "I hope I did enough for the 70%% of my grade that wasn't on this test."
        if branchIsabella and not breakup:
            scene ep12_finals85 with dissolve
            isa "I'm sure you did."
            isa "Are you off to spend your holiday tonight?"
            scene ep12_finals84 with dissolve
            mc "No, not for a few days."
            scene ep12_finals86 with dissolve
            isa "Let's talk later tonight, then. If you're free..."
            scene ep12_finals84 with dissolve
            mc "Sure."
            scene ep12_finals86 with dissolve
            isa "I'll drop by."
        else:
            scene ep12_finals85 with dissolve
            isa "I'm sure you did."
            isa "Off to enjoy your holiday, [name]. I wish you a nice one."
            scene ep12_finals84 with dissolve
            mc "You too."
stop music fadeout 3
scene ep12_finals89 with dissolve
$ renpy.pause()
show screen new_phone_screen
if ep11_quinn_question[0] and ep11_quinn_question[1] and (not branchZoey or wt_ep11_zoey_kiss_others):
    $ guideSuggestedPage = 253
    jump ep12_qmc_label
elif (not branchZoey or wt_ep11_zoey_kiss_others) and ep12_nicole_path and not ep12_nicole_breakup:
    $ guideSuggestedPage = 253
    jump ep12_nic_date_label
elif (not branchZoey or wt_ep11_zoey_kiss_others) and branchJill and not breakup:
    jump ep12_jill_solo_label
elif (not branchZoey or wt_ep11_zoey_kiss_others)  and branchIsabella and not breakup:
    $ guideSuggestedPage = 253
    jump ep12_bella_solo_label
elif ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
    $ guideSuggestedPage = 254
    jump ep12_sage_solo_label
else:
    jump ep12_dikmas_label

label ep12_nic_date_label:
play music "music/ep2/by_your_side.mp3"
scene ep12_nic_date1 with wipeleft
nic "How were the finals?"
scene ep12_nic_date2 with dissolve
mc "I had two exams today... They could have spread it out over the week, but they didn't."
mc "As a result, my head feels...full and empty at the same time."
scene ep12_nic_date3 with dissolve
mc "I don't want to see another math exercise until January."
scene ep12_nic_date4 with dissolve
nic "Aw, you poor thing."
nic "It's good that you came here. We'll have a relaxed night together."
scene ep12_nic_date2 with dissolve
mc "Thanks! I need it."
mc "And how about you? How have you been?"
scene ep12_nic_date4 with dissolve
nic "There's not much excitement in my life at the moment, but there is plenty of stress to go around."
nic "That's holidays for you."
scene ep12_nic_date2 with dissolve
mc "Oh, yeah. You're having your kid over Christmas, right?"
scene ep12_nic_date4 with dissolve
nic "Yes. I've been re-shopping for Christmas gifts this week."
scene ep12_nic_date2 with dissolve
mc "What do you mean by that?"
scene ep12_nic_date5 with dissolve
nic "Well, I already bought him what he wanted, but apparently Luke got him the same toy, so one of us had to replace the gift."
nic "And, like always, I caved."
scene ep12_nic_date8 with dissolve
mc "It sounds like you're too nice."
scene ep12_nic_date6 with dissolve
nic "Don't I know it... Holidays are rough, [name]."
scene ep12_nic_date9 with dissolve
mc "Is it hard to get along with Luke?"
scene ep12_nic_date5 with dissolve
nic "With both him and his family."
nic "When Marvin was younger, we tried to have joint celebrations for his sake."
nic "We thought it would mean a lot to Marvin if he got to see his mom and dad get along together, but it made me feel like the third wheel."
scene ep12_nic_date6 with dissolve
nic "His relatives didn't want to talk to me, and when they did, they loved giving me a hard time."
nic "Mostly, I suffered through dinner in silence."
nic "After bringing up how I felt with Luke, we decided to have separate celebrations."
scene ep12_nic_date8 with dissolve
mc "That sucks... But is it working better now or...?"
scene ep12_nic_date5 with dissolve
nic "Yes, and no."
nic "I was supposed to have Marvin for New Year's Eve this year, but Luke's parents invited Marvin to their party."
nic "Marvin got all excited and practically begged me to let him celebrate with them..."
scene ep12_nic_date7 with dissolve
nic "So, I'm free for New Year's Eve..."
scene ep12_nic_date9 with dissolve
mc "You caved again?"
scene ep12_nic_date6 with dissolve
nic "They knew exactly what they were doing when they asked Marvin directly, rather than me or Luke."
nic "If I had said no, it would have put me in a bad light, and Marvin would have blamed me."
scene ep12_nic_date5 with dissolve
nic "Maybe it was wrong of me to fall for their trick, but I felt it was the best way to go..."
stop music fadeout 3
nic "I can't say that I would throw a better New Year's celebration for Marvin."
play music "music/ep12/licensed_music/track218.mp3"
play sound "sound_effects/season3/lighter.mp3"
scene ep12_nic_date10 with dissolve
$ renpy.pause()
scene ep12_nic_date11 with dissolve
$ renpy.pause()
scene ep12_nic_date12 with dissolve
mc "If you're free, you're welcome to celebrate New Year's Eve with us."
scene ep12_nic_date13 with dissolve
nic "Would you like that?"
scene ep12_nic_date15 with dissolve
mc "Of course. We planned on inviting you, girls."
scene ep12_nic_date16 with dissolve
nic "Actually, Tommy already invited us. But I'm happy you want us there too."
nic "Here. Have some."
scene ep12_nic_date17 with dissolve
nic "Fair warning, it's strong."
scene ep12_nic_date18 with dissolve
mc "*{i}Coughs{/i}*"
nic "Told you."
scene ep12_nic_date19 with dissolve
mc "My lungs sting..."
scene ep12_nic_date20 with dissolve
nic "You'll get better at it. Have some more."
scene ep12_nic_date19 with dissolve
mc "Are you trying to get me fucked up?"
scene ep12_nic_date20 with dissolve
nic "I figured you'd need it too."
scene ep12_nic_date21 with dissolve
$ renpy.pause()
scene ep12_nic_date12 with dissolve
mc "I'm sorry things are rough for you with Marvin and all..."
mc "Don't let them walk right over you."
scene ep12_nic_date14 with dissolve
nic "I choose my battles. It's better that way."
scene ep12_nic_date13 with dissolve
nic "Enough about me... What are you doing for your holidays?"
scene ep12_nic_date15 with dissolve
mc "A calm and quiet Christmas with Dad. That's about it."
mc "We eat and give each other gifts."
scene ep12_nic_date22 with dissolve
mc "I think I'll stay with him for a couple of days before coming back here."
mc "Even though it's winter break, I feel like I want to spend it at the DIKs."
scene ep12_nic_date23 with dissolve
nic "Doing what? Aren't your brothers at home for the break too?"
scene ep12_nic_date24 with dissolve
if ep11_fighter:
    mc "I bet they are. But I want to work out more and prepare for a competition."
    scene ep12_nic_date25 with dissolve
    nic "What competition?"
    scene ep12_nic_date27 with dissolve
    mc "A fighting one. I train with some guys at the gym, and they invited me to join a competition on the 29th."
    mc "I'll be fighting someone. It's my first fight like that ever."
    scene ep12_nic_date25 with dissolve
    nic "Can I watch you fight?"
    scene ep12_nic_date27 with dissolve
    mc "Yeah, if you want. Are you free that day?"
    scene ep12_nic_date25 with dissolve
    nic "I should be, but I'll double-check."
    scene ep12_nic_date27 with dissolve
    mc "I would love to have you there."
    mc "Damn... Now I hope I don't lose."
    scene ep12_nic_date26 with dissolve
    nic "You won't. I'll cheer you on as much as I can."
    scene ep12_nic_date27 with dissolve
    mc "Haha."
elif ep11_music:
    mc "I bet they are. But I want to work out more, and I need to practice for a performance."
    scene ep12_nic_date25 with dissolve
    nic "What performance?"
    scene ep12_nic_date27 with dissolve
    mc "I'm playing guitar at the faculty's Christmas party on the 29th."
    scene ep12_nic_date25 with dissolve
    nic "A Christmas party after Christmas?"
    scene ep12_nic_date27 with dissolve
    mc "The faculty is off for winter break, too. According to my Professor, it's one of the highlights of the year for them."
    mc "He asked me to play guitar for them, and I need to put together a performance."
    scene ep12_nic_date25 with dissolve
    nic "Then it's good you'll have some time for it after Christmas. I wish I could hear you play."
    scene ep12_nic_date27 with dissolve
    mc "I'll play for you sometime if you want."
    scene ep12_nic_date26 with dissolve
    nic "I'd love it."
else:
    mc "I bet they are. But I want to work out more and relax."
    scene ep12_nic_date25 with dissolve
    nic "I get it. Alone time is nice. You need to recuperate after the finals."
    scene ep12_nic_date27 with dissolve
    mc "Yeah... Before I know it, next semester is here, and it's back to studying."

label ep12_nic_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    play music "music/ep12/licensed_music/track218.mp3"
hide screen new_phone_screen
scene ep12_nic_lewd1
show screen ep12_drugs_screen
with dissolve
mc "Oh..."
scene ep12_nic_lewd2 with dissolve
nic "Yeah... You can feel it too, can't you?"
scene ep12_nic_lewd3 with dissolve
$ renpy.pause()
scene ep12_nic_lewd4 with dissolve
nic "Haha... I'll stop talking. Enjoy the feeling together with me."
scene ep12_nic_lewd5 with dissolve
$ renpy.pause()
scene ep12_nic_lewd6 with dissolve
$ renpy.pause()
scene ep12_nic_lewd7 with dissolve
mc "How strong was that blunt?"
scene ep12_nic_lewd8 with dissolve
nic "The feel-good kind of strong."
scene ep12_nic_lewd7 with dissolve
mc "I can't feel my face."
scene ep12_nic_lewd9 with dissolve
nic "Can you feel this?"
scene ep12_nic_lewd10 with dissolve
mc "Yes. That feels good."
scene ep12_nic_lewd9 with dissolve
nic "Relax and enjoy this, [name]."
nic "There are few better feelings than this in the world."
scene ep12_nic_lewd11 with dissolve
$ renpy.pause()
scene ep12_nic_lewd12 with dissolve
mc "You're so warm and soft."
scene ep12_nic_lewd13 with dissolve
$ renpy.pause()
scene ep12_nic_lewd14 with dissolve
nic "Do you know what else is warm and soft?"
play sound "sound_effects/clothes.mp3"
scene ep12_nic_lewd15 with dissolve
$ renpy.pause()
scene ep12_nic_lewd16 with dissolve
mc "Yes... That's lovely."
scene ep12_nic_lewd17 with dissolve
nic "Hahaha!"
nic "You're lovely."
scene ep12_nic_lewd18 with dissolve
$ renpy.pause()
scene ep12_nic_lewd19 with dissolve
nic "Mmm..."
scene ep12_nic_lewd20 with dissolve
nic "*{i}Smack{/i}*"
scene ep12_nic_lewd21 with dissolve
nic "Wanna have sex?"
scene ep12_nic_lewd22 with dissolve
mc "Yes, but I'm not sure if I can."
mc "I feel like I'm too out of myself."
scene ep12_nic_lewd21 with dissolve
nic "That's why I think you'll enjoy sex right now."
scene ep12_nic_lewd20 with dissolve
nic "*{i}Smack{/i}*"
scene ep12_nic_lewd23 with dissolve
$ renpy.pause()
play sound "sound_effects/clothes.mp3"
scene ep12_nic_lewd24 with dissolve
$ renpy.pause()
scene ep12_nic_lewd25 with dissolve
$ renpy.pause()
scene ep12_nic_lewd26 with dissolve
nic "Mmm..."
scene anim_nicole_bj1_ep12 with dissolve
nic "*{i}Suck suck glug glug{/i}*"
pause
scene anim_nicole_bj2_ep12 with dissolve
pause
scene ep12_nic_lewd27 with dissolve
nic "Looks like getting it up wasn't a problem."
$ tmpInt = 0
$ tmpBool3 = False
label ep12_nic_lewd_loop_label:
menu:
    "Blowjob":
        $ tmpInt += 1
        scene anim_nicole_bj1_ep12 with dissolve
        nic "*{i}Suck suck glug glug{/i}*"
        pause
        scene anim_nicole_bj2_ep12 with dissolve
        pause
        jump ep12_nic_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_nicole_ride1_ep12 with dissolve
        nic "Mmm... Yes, [name]. Nice and slow now. Don't ruin your buzz."
        pause
        scene anim_nicole_ride2_ep12 with dissolve
        mc "Haha, I can't even feel if I'm going fast or slow."
        nic "It's perfect, [name]. Keep going just like that. Mmm..."
        pause
        jump ep12_nic_lewd_loop_label
    "Cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_nicole_ride1_anal_ep12 with dissolve
        nic "*{i}Moans{/i}* Fuck! Ahh!!!"
        pause
        scene anim_nicole_ride2_anal_ep12 with dissolve
        mc "Hm... Is it me or is your pussy tighter than usual?"
        nic "You're fucking my ass, [name]."
        mc "Oh... Wow..."
        pause
        scene anim_nicole_ride3_anal_ep12 with dissolve
        nic "*{i}Moans{/i}*"
        pause
        jump ep12_nic_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_nicole_doggy1_ep12 with dissolve
        nic "*{i}Moans{/i}* Yes! Slow but hard. Just what I want right now."
        pause
        scene anim_nicole_doggy2_ep12 with dissolve
        nic "Fuck me, [name]. Don't stop."
        mc "I couldn't stop even if I wanted. My hips are moving on their own."
        pause
        scene anim_nicole_doggy3_ep12 with dissolve
        pause
        jump ep12_nic_lewd_loop_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_nicole_doggy1_anal_ep12 with dissolve
        nic "Fuck! You're so deep inside me. It's like we're one."
        pause
        scene anim_nicole_doggy2_anal_ep12 with dissolve
        nic "*{i}Moans{/i}* [name]? Are you feeling good?"
        mc "Hm? Oh... I must have zoned out."
        pause
        scene anim_nicole_doggy3_anal_ep12 with dissolve
        nic "Does it feel good?"
        mc "Yeah... It feels like I'm not here right now."
        nic "Haha, I don't even know what that means. *{i}Moans{/i}*"
        mc "Haha... Me neither."
        pause
        jump ep12_nic_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_nicole_stand1_ep12 with dissolve
        nic "Be still. I've got this."
        mc "Mmm... Fuck, Nicole. It's so good."
        pause
        scene anim_nicole_stand2_ep12 with dissolve
        nic "Yes... Yes... God, I love your cock!"
        pause
        jump ep12_nic_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_nicole_miss1_ep12 with dissolve
        nic "Yes! Yes! Right there... Hngn!"
        pause
        scene anim_nicole_miss2_ep12 with dissolve
        nic "*{i}Moans{/i}*"
        pause
        if not tmpBool3:
            $ tmpBool3 = True
            scene ep12_nic_lewd29 with hpunch
            nic "Ahh!!! I'm cumming!"
            scene ep12_nic_lewd28 with hpunch
            nic "Yes!!!"
            scene ep12_nic_lewd30 with hpunch
            nic "[name]... Fuck... You're so good..."
        jump ep12_nic_lewd_loop_label
    "Prone (Anal)":
        $ tmpInt += 1
        scene anim_nicole_prone1_ep12 with dissolve
        nic "Getting close yet?"
        mc "I'm as close as I can get to you."
        nic "I mean, are you cumming soon?"
        pause
        scene anim_nicole_prone2_ep12 with dissolve
        mc "Coming? I'm right here. Shh... Don't worry."
        pause
        jump ep12_nic_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "Whoa... Something's building up inside me."
        nic "That's it... You're about to cum."
        menu:
            "Creampie":
                scene anim_nicole_doggy3_ep12 with dissolve
                nic "Cum for me, [name]. Cum inside me..."
                pause
                scene ep12_nic_lewd37 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_nic_lewd37 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_nic_lewd37 at vpunch, cum1
                mc "Ahhh!!!"
                scene anim_nicole_doggy3b_ep12 with dissolve
                mc "Fuck... Nicole... I don't wanna stop..."
                pause
                scene ep12_nic_lewd38 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_nicole_ride2_anal_ep12 with dissolve
                nic "Cum for me, [name]."
                pause
                scene ep12_nic_lewd31 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_nic_lewd31 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_nic_lewd31 at vpunch, cum1
                mc "Ahhh!!!"
                scene anim_nicole_ride2b_anal_ep12 with dissolve
                mc "Fuck... Nicole..."
                pause
                scene ep12_nic_lewd32 with dissolve
                $ renpy.pause()
            "On belly":
                scene anim_nicole_miss1_ep12 with dissolve
                nic "Cum for me, [name]."
                pause
                scene ep12_nic_lewd33 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_nic_lewd33 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_nic_lewd33 at vpunch, cum2
                mc "Hngnnn... Fuck!"
                scene ep12_nic_lewd34 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_nicole_bj2_ep12 with dissolve
                nic "*{i}Suck suck glug{/i}* Cum, [name]..."
                pause
                scene ep12_nic_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_nic_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_nic_lewd35 at vpunch, cum2
                mc "Hngnn... Fuck!"
                scene ep12_nic_lewd36 with dissolve
                $ renpy.pause()

$ renpy.pause()
scene ep12_nic_lewd39 with dissolve
$ renpy.pause()
scene ep12_nic_lewd41 with dissolve
nic "How are you feeling?"
scene ep12_nic_lewd44 with dissolve
mc "What happened?"
scene ep12_nic_lewd42 with dissolve
nic "Haha, you came."
if tmpBool3:
    nic "I came too."
scene ep12_nic_lewd43 with dissolve
$ renpy.pause()
scene ep12_nic_lewd45 with dissolve
mc "Everything is spinning."
scene ep12_nic_lewd41 with dissolve
nic "Stay on the couch with me, [name]. It will be alright soon. You'll see."
scene ep12_nic_lewd44 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_nic_lewd40 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep12_lewd_nicole = True
$ calcScenes()
$ mphone_stats_add_girl_s3("envy","You had sex with Nicole in episode 12.")
$ new_bio("Envy", "I got high together with Nicole during our date. We ended up having sex on her couch.")
show screen new_phone_screen
hide screen ep12_drugs_screen
if (not branchZoey or wt_ep11_zoey_kiss_others) and branchJill and not breakup:
    jump ep12_jill_solo_label
elif (not branchZoey or wt_ep11_zoey_kiss_others)  and branchIsabella and not breakup:
    $ guideSuggestedPage = 253
    jump ep12_bella_solo_label
elif ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
    $ guideSuggestedPage = 254
    jump ep12_sage_solo_label
else:
    jump ep12_dikmas_label

jump ep12_dikmas_label

label ep12_qmc_label:
play music "music/ep12/licensed_music/track219.mp3"
queue music ["music/ep10/licensed_music/track142.mp3","music/ep12/licensed_music/track219.mp3"]
scene ep12_qmc1 with dissolve
le "Hey, congrats! You made it through your first semester! How did the finals go?"
scene ep12_qmc2 with dissolve
mc "Thanks! It was a long day..."
scene ep12_qmc3 with dissolve
le "You should rest up tonight. You have a visitor, by the way."
scene ep12_qmc2 with dissolve
mc "Who?"
scene ep12_qmc3 with dissolve
le "Quinn. I told her she could hang out in your room until you returned."
scene ep12_qmc4 with dissolve
mc "(I hope this means good news...)"

label ep12_quinn_lewd_label:
if _in_replay:
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
    $ ep12_nicole_path = False
    $ ep12_nicole_breakup = True
    play music "music/ep12/licensed_music/track219.mp3"
    queue music ["music/ep10/licensed_music/track142.mp3","music/ep12/licensed_music/track219.mp3"]
hide screen new_phone_screen
scene ep12_quinn_lewd1 with dissolve
mc "Quinn? I heard you were here."
scene ep12_quinn_lewd2 with dissolve
mc "Holy..."
scene ep12_quinn_lewd3 with dissolve
qu "What took you so long?"
scene ep12_quinn_lewd4 with dissolve
mc "I had my finals. Wow, you look amazing."
scene ep12_quinn_lewd5 with dissolve
qu "That's an understatement."
scene ep12_quinn_lewd3 with dissolve
qu "So... Finals, huh? Do you need a celebratory fuck or a pity one?"
if ep12_nicole_path and not ep12_nicole_breakup:
    scene ep12_quinn_lewd6 with dissolve
    mc "(If I do this, I have a feeling I won't make it to dinner with Nicole...)"
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Nicole path)","(Quinn path)","(-DIK)","(+DIK)","(+5 Josy)","(-5 Josy)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
                        #\n{size=-4}[m_c1][mod_choices[1]][m_c2][mod_choices[4]]
                        
    
    menu:
        "Mod: Both":
            $ wt_ep12_quinn_nicole=True
            jump wt_ep12_quinn_nicole_label
        "Ditch Nicole \n{size=-4}[m_c1][mod_choices[1]]":
            $ ep12_nicole_ditch = True
            label wt_ep12_quinn_nicole_label:
            mc "(But I'd rather spend the night with Quinn.)"
            if not wt_ep12_quinn_nicole:
                $ new_bio("Envy", "I ditched Nicole to spend the night together with Quinn.")
        "Ditch Quinn \n{size=-4}[m_c2][mod_choices[0]]":           
            $ ep12_quinn_ditch = True
            scene ep12_quinn_lewd8 with dissolve
            mc "I wish you had called... I already made plans for tonight."
            scene ep12_quinn_lewd7 with dissolve
            qu "Cancel them."
            scene ep12_quinn_lewd8 with dissolve
            mc "I can't."
            scene ep12_quinn_lewd7 with dissolve
            qu "Somebody better be dying. What plans are more important than this?"
            scene ep12_quinn_lewd8 with dissolve
            mc "I have a date with Nicole."
            scene ep12_quinn_lewd9 with dissolve
            qu "You gotta be shitting me. You're gonna pick her over me?"
            scene ep12_quinn_lewd10 with dissolve
            mc "*{i}Sigh{/i}* Sorry, but I will."
            scene ep12_quinn_lewd9 with dissolve
            qu "What the fuck? You said you were into me."
            scene ep12_quinn_lewd10 with dissolve
            mc "Yeah, I am... But I'm into her too."
            scene ep12_quinn_lewd11 with dissolve
            qu "I don't get you."
            scene ep12_quinn_lewd10 with dissolve
            mc "I'm sorry, Quinn. You put me on the spot, and this is how I feel."
            mc "I'm not canceling my date."
            stop music fadeout 3
            scene ep12_quinn_lewd12 with dissolve
            $ renpy.pause()
            $ new_bio("Quinn", "I ditched Quinn to spend the night together with Nicole.")
            show screen new_phone_screen
            jump ep12_nic_date_label

scene ep12_quinn_lewd13 with dissolve
mc "Haha... How about an \"I've missed you terribly\" one?"
scene ep12_quinn_lewd14 with dissolve
qu "I can do that one."
scene ep12_quinn_lewd15 with dissolve
$ renpy.pause()
scene ep12_quinn_lewd16 with dissolve
qu "*{i}Smack{/i}*"
scene ep12_quinn_lewd17 with dissolve
$ renpy.pause()
scene ep12_quinn_lewd18 with dissolve
$ renpy.pause()
scene ep12_quinn_lewd19 with dissolve
$ renpy.pause()
scene ep12_quinn_lewd20 with dissolve
mc "How are things?"
scene ep12_quinn_lewd21 with dissolve
qu "Things are good, [name]. Real good."
scene ep12_quinn_lewd20 with dissolve
mc "I'm relieved to hear that."
scene ep12_quinn_lewd19 with dissolve
qu "*{i}Smack{/i}*"
scene ep12_quinn_lewd20 with dissolve
mc "I have like a million questions for you."
scene ep12_quinn_lewd21 with dissolve
qu "We can talk after. Right now, I need you inside me."
qu "Because I did miss you terribly."
scene ep12_quinn_lewd22 with dissolve
mc "You know your lines."
scene ep12_quinn_lewd21 with dissolve
qu "It's not a line."
scene bg anim_quinn_strip_ep12 movie with dissolve
pause
scene ep12_quinn_lewd23 with dissolve
mc "Fuck, you're so beautiful."
qu "Beautiful? Are you high? Call me sexy or something less cringe."
mc "You are sexy too."
label ep12_quinn_lewd_loop_label:
menu:
    "Fondle tits":
        scene anim_quinn_tits_ep12 with dissolve
        mc "I've missed these."
        qu "That's better. Objectify me."
        pause
        jump ep12_quinn_lewd_loop_label
    "Suck on nipple":
        scene anim_quinn_nipple_ep12 with dissolve
        mc "*{i}Suck suck{/i}*"
        pause
        jump ep12_quinn_lewd_loop_label
    "Fondle ass":
        scene anim_quinn_ass_ep12 with dissolve
        mc "It feels like ages ago..."
        qu "Haha, it's not ages ago. But yeah, it's been too long since last time."
        pause
        jump ep12_quinn_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep12_quinn_lewd24 with dissolve
mc "I love that lingerie on you."
scene ep12_quinn_lewd25 with dissolve
qu "Good. Because I wasn't planning on taking it off."
scene ep12_quinn_lewd26 with dissolve
mc "This part needs to come off, though."
qu "Dude, you're still fully dressed. Get naked for me, and I'll show you what's underneath."
scene ep12_quinn_lewd27 with dissolve
mc "There it is... How I missed it."
scene ep12_quinn_lewd28 with dissolve
qu "Yeah? Care to show it?"
scene ep12_quinn_lewd29 with dissolve

$ tmpInt = 0
label ep12_quinn_lewd_loop2_label:
menu:
    "Eat pussy":
        $ tmpInt += 1
        scene anim_quinn_cunn1_ep12 with dissolve
        qu "*{i}Moans{/i}* Yes! Fuck!"
        pause
        scene anim_quinn_cunn2_ep12 with dissolve
        mc "*{i}Lick lick{/i}*"
        qu "*{i}Moans{/i}* Mmm... Yes, [mc_quinn]. Eat my pussy."
        pause
        jump ep12_quinn_lewd_loop2_label
    "Eat ass":
        $ tmpInt += 1
        scene anim_quinn_ass2_ep12 with dissolve
        mc "*{i}Lick lick{/i}*"
        qu "Mmm... Aha, so that's what you want to do to me."
        pause
        scene anim_quinn_ass3_ep12 with dissolve
        pause
        jump ep12_quinn_lewd_loop2_label
    "Handjob":
        $ tmpInt += 1
        scene anim_quinn_hj_ep12 with dissolve
        qu "I almost forgot how big it was."
        mc "You didn't forget how to handle it, though... Keep going."
        pause
        scene anim_quinn_hj2_ep12 with dissolve
        qu "Dude, you're twitching already. You're not getting close, are you?"
        mc "Haha! Fuck... I don't know what it is about you today. But yeah, take it easy with me."
        pause
        jump ep12_quinn_lewd_loop2_label
    "Blowjob":
        $ tmpInt += 1
        scene anim_quinn_bj_ep12 with dissolve
        qu "*{i}Suck suck glug glug{/i}*"
        pause
        scene anim_quinn_bj2_ep12 with dissolve
        mc "That's such a hot sight. Fuck..."
        pause
        jump ep12_quinn_lewd_loop2_label
    "Footjob":
        $ tmpInt += 1
        scene anim_quinn_foot_ep12 with dissolve
        qu "My little pervert... I'll take good care of you."
        mc "Haha, I'm the pervert? I didn't even ask for this."
        pause
        scene anim_quinn_foot2_ep12 with dissolve
        qu "Oh, so you want me to stop?"
        mc "I didn't say that..."
        qu "See. I wouldn't have done it if I thought you didn't want it."
        pause
        jump ep12_quinn_lewd_loop2_label
    "Tease cock":
        $ tmpInt += 1
        scene anim_quinn_tease_ep12 with dissolve
        mc "I wanna fuck you so bad..."
        qu "Mhm..."
        pause
        scene anim_quinn_tease2_ep12 with dissolve
        pause
        jump ep12_quinn_lewd_loop2_label
    "Continue" if tmpInt > 2:
        scene ep12_quinn_lewd31 with dissolve
        qu "I want you to own this pussy, [mc_quinn]... Make it yours."
        scene ep12_quinn_lewd30 with dissolve
        qu "Take me in all the ways that you want to."

$ tmpInt = 0
label ep12_quinn_lewd_loop3_label:
menu:
    "Cowgirl":
        $ tmpInt += 1
        scene anim_quinn_ride1_ep12 with dissolve
        qu "Mmm... Is this what you want?"
        mc "Fuck, yes... Ride me, [quinn]."
        pause
        scene anim_quinn_ride2_ep12 with dissolve
        qu "You love it, don't you?"
        mc "Mhm..."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_quinn_doggy1_ep12 with dissolve
        qu "*{i}Moans{/i}* Ahh!"
        mc "Take it."
        qu "More! Harder!"
        pause
        scene anim_quinn_doggy2_ep12 with dissolve
        mc "Your ass is so sexy. I wanna cum all over it."
        qu "Not yet... Hold it."
        pause
        scene anim_quinn_doggy3_ep12 with dissolve
        mc "I'm gonna try my best."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Missionary":
        $ tmpInt += 1
        scene anim_quinn_miss1_ep12 with dissolve
        qu "*{i}Moans{/i}* Take me, [mc_quinn]."
        pause
        scene anim_quinn_miss2_ep12 with dissolve
        mc "Are you clenching?"
        qu "Can you feel it?"
        mc "Yeah, if feels like you're gripping my cock."
        qu "Mmm... Good."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Standing":
        $ tmpInt += 1
        scene anim_quinn_stand1_ep12 with dissolve
        qu "*{i}Moans{/i}* Fuck me! Fuck me!"
        pause
        scene anim_quinn_stand2_ep12 with dissolve
        qu "Mmm... You've still got the moves."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Sideways (Anal)":
        $ tmpInt += 1
        scene anim_quinn_side1_ep12 with dissolve
        qu "*{i}Moans{/i}* Ahh!"
        mc "Too rough?"
        qu "No. Keep going. *{i}Moans{/i}*"
        pause
        scene anim_quinn_side2_ep12 with dissolve
        qu "Yes... Yes... I love it in the ass. Fuck me, [mc_quinn]."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Doggystyle (Anal)":
        $ tmpInt += 1
        scene anim_quinn_doggy4_ep12 with dissolve
        mc "Fuck, you're tight."
        qu "Switch holes if you can't take it."
        pause
        scene anim_quinn_doggy5_ep12 with dissolve
        mc "If {b}I{/b} can't take it? Haha, what about you?"
        qu "*{i}Moans{/i}* I'm loving every second of it."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Reverse cowgirl (Anal)":
        $ tmpInt += 1
        scene anim_quinn_rev1_ep12 with dissolve
        qu "Ahh! Ahh!!!"
        pause
        scene anim_quinn_rev2_ep12 with dissolve
        mc "Fuck, I'm not gonna be able to hold it for much longer."
        pause
        jump ep12_quinn_lewd_loop3_label
    "Cum" if tmpInt > 2:
        mc "Quinn... I'm cumming."
        menu:
            "On ass":
                scene anim_quinn_stand2_ep12 with dissolve
                pause
                scene ep12_quinn_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd35 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd35 at vpunch, cum2
                mc "Ahh!!!"
                scene ep12_quinn_lewd36 with dissolve
                $ renpy.pause()
            "Facial":
                scene anim_quinn_bj_ep12 with dissolve
                mc "Yes... Yes. A bit more."
                qu "*{i}Suck suck{/i}*"
                scene ep12_quinn_lewd40 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd40 at vpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd40 at vpunch, cum3
                mc "Ahh!!!"
                scene ep12_quinn_lewd41 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_quinn_miss2_ep12 with dissolve
                mc "I'm so close..."
                qu "Cum inside me, [mc_quinn]. Give me your cum."
                scene ep12_quinn_lewd37 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd37 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd37 at vpunch, cum1
                mc "Ahh!!!"
                scene ep12_quinn_lewd38 with dissolve
                $ renpy.pause()
                scene ep12_quinn_lewd39 with dissolve
                $ renpy.pause()
            "Creampie (Anal)":
                scene anim_quinn_doggy5_ep12 with dissolve
                mc "I'm so close..."
                qu "Cum inside me, [mc_quinn]. Give me your cum."
                scene ep12_quinn_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd32 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep12_quinn_lewd32 at vpunch, cum1
                mc "Ahh!!!"
                scene ep12_quinn_lewd33 with dissolve
                $ renpy.pause()
                scene ep12_quinn_lewd34 with dissolve
                $ renpy.pause()

$ renpy.end_replay()
$ persistent.ep12_lewd_quinn = True
$ calcScenes()
$ mphone_stats_add_girl_s3("quinn","You had sex with Quinn in your room in episode 12.")
stop music fadeout 3
show screen new_phone_screen
scene ep12_qmc5 with dissolve
mc "Fuck, I've missed that..."
play music "music/ep11/licensed_music/track153.mp3"
scene ep12_qmc6 with dissolve
qu "You still got it."
scene ep12_qmc5 with dissolve
mc "This was the best way I could kick off winter break."
scene ep12_qmc6 with dissolve
qu "Yeah..."
scene ep12_qmc7 with dissolve
mc "Now... How are you really?"
scene ep12_qmc8 with dissolve
qu "Full answer?"
scene ep12_qmc7 with dissolve
mc "Yeah. Let me hear it."
scene ep12_qmc8 with dissolve
qu "You might not want to hear the details."
scene ep12_qmc7 with dissolve
mc "You don't have to protect me. I want to know what you've gotten yourself into."
scene ep12_qmc9 with dissolve
qu "Well... I got my revenge."
scene ep12_qmc10 with dissolve
mc "Are you in danger?"
scene ep12_qmc9 with dissolve
qu "Usually. But my plan worked."
scene ep12_qmc11 with dissolve
mc "What was your plan?"
scene ep12_qmc12 with dissolve
qu "I called in a tip to the cops about Buddy's drug den. I told them I had spotted someone with a gun selling drugs at his address."
qu "The cops showed up and arrested him. I watched it all unfold from a hotel room on the other side of the street."
scene ep12_qmc13 with dissolve
qu "And after the cops had left, I snuck inside the den and got what is now mine."
scene ep12_qmc10 with dissolve
mc "And what was that?"
scene ep12_qmc12 with dissolve
qu "Dad had a hidden safe installed under the floorboards in my childhood room."
qu "He hoped that no one would search for it, especially since there already was a big safe in plain sight from where you enter the place."
scene ep12_qmc9 with dissolve
qu "And he was right, the cops missed it."
qu "I was worried they would find it when they brought in the dog, but they didn't."
scene ep12_qmc12 with dissolve
qu "I opened the safe and got away with the money and the drugs in it. I had to be careful and make multiple trips, but I managed."
qu "I fooled Mick, Buddy's right hand, into thinking that I didn't know anything about the arrest, and he confronted Vinny about it."
scene ep12_qmc13 with dissolve
qu "Then Vinny called me... He had left town."
scene ep12_qmc10 with dissolve
mc "Is Vinny gone?"
scene ep12_qmc12 with dissolve
qu "He had to leave because the confrontation with Mick didn't go well for him."
qu "Either way, there's no threat out there. Buddy is in jail, and I don't think he'll get out anytime soon."
scene ep12_qmc10 with dissolve
mc "What if he finds out that it was you who called the cops?"
scene ep12_qmc9 with dissolve
qu "I distorted my voice during the call, covered my tracks well, and shifted the blame onto Vinny."
scene ep12_qmc11 with dissolve
mc "If you say you're safe, I trust you. So, what now?"
scene ep12_qmc9 with dissolve
qu "I'll lie low for a while, but I also need to sell the drugs I brought with me. I have too much of it."
scene ep12_qmc10 with dissolve
mc "Maybe you shouldn't have taken it all with you."
scene ep12_qmc14 with dissolve
qu "I got greedy when I saw what was inside the safe."
qu "[name], there was so much money in it. It will solve all my problems."
qu "I've secured my future! I'm set for life."
scene ep12_qmc10 with dissolve
mc "Still... I'm worried. You've involved the cops and pissed off some dangerous people."
scene ep12_qmc12 with dissolve
qu "That's why I'm being extra careful right now."
scene ep12_qmc10 with dissolve
mc "Hoarding money and drugs is careful?"
scene ep12_qmc9 with dissolve
qu "Don't worry. I've got a good hiding spot."
scene ep12_qmc11 with dissolve
mc "I'm happy that you're safe, but I don't know how I feel about the rest."
scene ep12_qmc14 with dissolve
qu "Let me worry about that. I don't want to make my problems yours."
stop music fadeout 3
scene ep12_qmc15 with dissolve
$ renpy.pause()
$ new_bio("Quinn", "Quinn surprised me in my room. After having sex, she shared what she had been up to. She reassured me that she was safe, but what she told me bothered me.")
$ mgallery_add_photo("ep12_quinn_pic1")

if (not branchZoey or wt_ep11_zoey_kiss_others) and ep12_nicole_path and not ep12_nicole_breakup and wt_ep12_quinn_nicole:
    $ guideSuggestedPage = 253
    jump ep12_nic_date_label
elif (not branchZoey or wt_ep11_zoey_kiss_others) and branchJill and not breakup:
    jump ep12_jill_solo_label
elif (not branchZoey or wt_ep11_zoey_kiss_others)  and branchIsabella and not breakup:
    $ guideSuggestedPage = 253
    jump ep12_bella_solo_label
elif ((not branchZoey or wt_ep11_zoey_kiss_others) and branchSage) and (ep11_sage_love == 2 or RPsage >= 22) and not breakup:
    $ guideSuggestedPage = 254
    jump ep12_sage_solo_label
else:
    jump ep12_dikmas_label

jump ep12_dikmas_label

label ep12_dikmas_label:
$ guideSuggestedPage = 254
play music "music/ep11/licensed_music/track160.mp3"
queue music ["music/ep11/licensed_music/track167.mp3","music/ep11/licensed_music/track160.mp3"]
scene ep12_dikmas1
hide screen ep12_drugs_screen
with wipeleft
rs "Alright, guys! I know you're all excited about the holidays and heading home, but I'm excited about tonight."
rs "No more tests, a somewhat empty calendar, and a night with the boys."
scene ep12_dikmas2 with dissolve
jm "I don't know about you guys, but I'm not having a kinky sleepover with Rusty."
scene ep12_dikmas3 with dissolve
"*{i}Laughter{/i}*"
rs "Hilarious."
scene ep12_dikmas4 with dissolve
rs "I wanted to take this opportunity to wish you guys Merry Christmas."
rs "We'll see each other again around New Year's Eve. But hopefully a few days earlier than that, so we can finish the preparations for the epic party."
scene ep12_dikmas5 with dissolve
le "How epic can it get with the jocks being there?"
le "And are we just gonna forget that Anthony punched Derek?"
scene ep12_dikmas6 with dissolve
rs "I know. It's not the best outlook for a party, but many others will be there too. We'll make it work, ok?"
scene ep12_dikmas7 with dissolve
rs "Anyway, this speech is losing its momentum. Merry DIKmas, everyone!"
"*{i}Cheers{/i}*"
scene ep12_dikmas8 with dissolve
jac "Hey. I got you something for Christmas."
scene ep12_dikmas9 with dissolve
jb "I thought we all agreed on not getting each other gifts."
scene ep12_dikmas8 with dissolve
jac "I know. But I had this one planned for quite some time, and it wasn't ready for your birthday."
scene ep12_dikmas10 with dissolve
jb "Oh my God! You're joking... You made this for me?"
scene ep12_dikmas11 with dissolve
jac "Merry Christmas. Don't let it hang on the wall all year, though."
jb "I love it! Dude, thank you so much."
scene ep12_dikmas12 with dissolve
play sound "sound_effects/camera_shutter.mp3"
"*{i}Camera shutter{/i}*"
le "Wow! That's an awesome gift. Good job, Jacob."
if not persistent.ep12_card19:
    $ persistent.ep12_card19 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
scene ep12_dikmas13 with dissolve
jac "I'm sorry, I didn't get you a gift."
scene ep12_dikmas14 with dissolve
le "Don't be; I didn't get you anything either. And besides, after what Tommy got me, I don't want any more gifts."
scene ep12_dikmas47
$ renpy.pause()
scene ep12_dikmas15
tm "Merry Christmas."
scene ep12_dikmas16 with dissolve
mc "For me? Why?"
scene ep12_dikmas15 with dissolve
tm "You deserve this one."
scene ep12_dikmas16 with dissolve
mc "Oh boy... If it's anything like what Leon got..."
scene ep12_dikmas15 with dissolve
tm "Haha! It's not."
scene ep12_dikmas17 with dissolve
mc "A shirt?"
scene ep12_dikmas18 with dissolve
tm "For the New Year's Eve party, or whatever. I remember you don't have a lot of good clothes."
scene ep12_dikmas17 with dissolve
mc "That's both thoughtful and insulting. Even so, I like it!"
mc "I hope you're not doing this because you feel like you owe me something."
scene ep12_dikmas18 with dissolve
tm "Eh... It's a way of saying thanks, but also sorry for coming across as a bitch with you at times this semester."
tm "I know I'm not the easiest guy to deal with... And I'll only say this once..."
scene ep12_dikmas21 with dissolve
tm "I appreciate you."
play sound "sound_effects/season2/fistbump.mp3"
scene ep12_dikmas22 with hpunch
mc "Tommy..."
scene ep12_dikmas19 with dissolve
tm "Now, let's never talk about this again. Ok, fuckhead?"
scene ep12_dikmas20 with dissolve
mc "Haha! Got it."
scene ep12_dikmas19 with dissolve
tm "Tell me how you ruined the New Year's Eve party. Rusty mentioned something about it."
scene ep12_dikmas20 with dissolve
mc "That I ruined it?"
scene ep12_dikmas24 with dissolve
tm "Nah. It was ruined from the start. That's why I haven't cared much about it so far."
scene ep12_dikmas23 with dissolve
mc "There's still time to fix it if you don't like what we did."
if ep12_pp_fireworks == 0:
    mc "We're getting a bunch of fireworks to outshine the jocks..."
elif ep12_pp_fireworks == 1:
    mc "The jocks and DIKs are both getting some fireworks for a joint show..."
else:
    mc "We're saving money by mooching off the jocks' fireworks..."
if ep12_pp_food == 0:
    mc "...and we're spending a lot of money on a fancy buffet."
elif ep12_pp_food == 1:
    mc "...and we're spending some money on a decent buffet."
else:
    mc "...and we're not spending a lot of money on the decent buffet. We're keeping it simple."
mc "The biggest expense will be alcohol..."
if ep12_pp_game == 0:
    mc "...and while we probably won't need it, I'm bringing some party games people can play if they get bored."
else:
    mc "...and we're not doing any activities for this one."
scene ep12_dikmas24 with dissolve
if (minigames and pp_current_party_happiness[7] > 2) or (not minigames and pp_current_party_happiness[7] == 1):
    tm "It sounds like you didn't need me at all. I couldn't have planned it better."
else:
    tm "It works. The party was doomed from the start anyway."
tm "People will dance, drink, and talk for this one. And with the jocks there, I think it's fair that we don't treat them to any of our special games that night."
scene ep12_dikmas23 with dissolve
mc "So, you agree with me?"
scene ep12_dikmas25 with dissolve
tm "I think you got it covered, but I'll help you out after Christmas."
scene ep12_dikmas23 with dissolve
mc "Cool."

if branchMayaJosy and (not branchZoey or wt_ep11_zoey_kiss_others):
    if check_jlove():
        $ ep12_jsolo = True
        play sound "sound_effects/bell.mp3"
        scene ep12_dikmas26 with dissolve
        "*{i}Doorbell{/i}*"
        mc "I'll get it."
        scene ep12_dikmas53 with dissolve
        mc "Josy? What a nice surprise."
        scene ep12_dikmas48 with dissolve
        js "Hi! I hope I'm not interrupting your night with the boys."
        scene ep12_dikmas49 with dissolve
        mc "Nah, don't worry about it. It's laid back."
        scene ep12_dikmas48 with dissolve
        js "That sounds nice! I hope you're having a wonderful night."
        js "I stopped by to tell you that I'm going home tomorrow morning."
        scene ep12_dikmas49 with dissolve
        mc "Maybe I'll see you at home, then."
        scene ep12_dikmas50 with dissolve
        js "Not that home. I'm going to Mom's place for Christmas."
        scene ep12_dikmas49 with dissolve
        if ep11_josy_solo:
            mc "Oh, that's right."
        else:
            mc "I see."
        scene ep12_dikmas48 with dissolve
        js "But I wanted to ask if you'd like to visit and meet Mom."
        scene ep12_dikmas50 with dissolve
        js "You know how hard it is for us to meet family..."
        scene ep12_dikmas51 with dissolve
        mc "I'd love to... But..."
        scene ep12_dikmas52 with dissolve
        js "Maya. I know."
        js "[name], I don't know how to deal with this. So, I've decided to look at it in another way."
        scene ep12_dikmas50 with dissolve
        js "Instead of focusing on the negatives, I'm trying to see the positives."
        js "And the positive thing, right now, is that there's an opportunity for you to meet Mom. That is, if you're up for it."
        scene ep12_dikmas49 with dissolve
        if tc > 4 or persistent.no_cheater:
            mc "Hm... Meeting parents... I don't know."
            scene ep12_dikmas50 with dissolve
            js "She's not that scary. Come on... I want you to meet her."
            scene ep12_dikmas49 with dissolve
            mc "Ok, then..."
        else:
            mc "I'd love to meet her. I am up for it."
        scene ep12_dikmas48 with dissolve
        js "Then how about you visit on the 26th? And then we'll return home together on the 27th?"
        js "I'm celebrating with Dad and Monica that night."
        scene ep12_dikmas49 with dissolve
        if ep11_fighter:
            mc "I'll likely return to campus on the 27th. I have that competition on the 29th, remember?"
        elif ep11_music:
            mc "I'll likely return to campus on the 27th. I have that performance on the 29th, remember?"
        else:
            mc "I'll likely return to campus on the 27th. I want to help out with the New Year's Eve party preparations."
        scene ep12_dikmas48 with dissolve
        js "Of course. That's fine too."
        js "I'll book a bus ticket for you. It's the same bus I always take when I'm at Dad's."
        scene ep12_dikmas49 with dissolve
        if tc > 4 or persistent.no_cheater:
            mc "Thanks, but I can book it myself."
        else:
            mc "Thanks, but I can book it myself. And I can't wait to meet your mom."
        mc "Have a great Christmas."
        scene ep12_dikmas54 with dissolve
        js "Merry Christmas, [name]."
        scene ep12_dikmas55 with dissolve
        js "*{i}Smack{/i}*"

show ep12_dikmas27
if not persistent.ep12_cardcam13:
    show screen ep12_render_screen("cam13")
with dissolve
rs "Hey, everyone! To simplify for us when the spring semester starts..."
rs "I'd like to hear you guys make the case for any new initiates. Are we recruiting next semester or not?"
show ep12_dikmas30
hide ep12_dikmas27
hide screen ep12_render_screen
with dissolve
jac "Cool! Are we talking Hell Week tonight?"
show ep12_dikmas27
if not persistent.ep12_cardcam13:
    show screen ep12_render_screen("cam13")
with dissolve
rs "If you guys don't mind. There's a dilemma we need to solve next year."
show ep12_dikmas33
hide screen ep12_render_screen
with dissolve
jm "What's been bothering you?"
scene ep12_dikmas28 with dissolve
rs "Well, aside from the loss of Vinny and Nick... We're still a growing fraternity."
rs "And while this mansion is big, it's getting crowded."
rs "Tommy and I still have one and a half years left until graduation."
scene ep12_dikmas35 with dissolve
tm "Ugh... At least."
scene ep12_dikmas28 with dissolve
rs "Yeah, depending on how things pan out, of course."
rs "But the problem remains. How many can we accept come spring, and where would they stay?"
scene ep12_dikmas35 with dissolve
tm "Nick is gone. That's one room."
scene ep12_dikmas36 with dissolve
de "[name] has space for at least another DIK in his room."
scene ep12_dikmas38 with dissolve
mc "Whoa! Where the hell did that come from?"
scene ep12_dikmas39 with dissolve
de "It wasn't a slam on you, but hey... [mc_de_up], I live in a closet."
de "With the square feet you've got going for you, you could fit at least one more brother in there."
scene ep12_dikmas29 with dissolve
rs "And Tommy's room is even bigger. We're not splitting rooms until we absolutely have to."
scene ep12_dikmas35 with dissolve
tm "Damn straight."
scene ep12_dikmas33 with dissolve
jm "What does that leave us with? The home theater and Nick's room?"
scene ep12_dikmas34 with dissolve
le "We can't get rid of the home theater, guys... That's like my favorite room here."
scene ep12_dikmas31 with dissolve
jac "Yeah, and we host some DIK nights in there - like the evaluation for one."
jac "Crazy idea, but what about the attic?"
scene ep12_dikmas32 with dissolve
jb "Oh, yeah! We could fit at least four more DIKs up there, can't we?"
scene ep12_dikmas28 with dissolve
rs "We would have to put up some walls, but the attic is a possibility."
scene ep12_dikmas40 with dissolve
mc "Do they have to live here with us?"
mc "I mean, if we want to accept lots of DIKs, maybe they could live in dorms and join us for parties and such."
scene ep12_dikmas35 with dissolve
tm "Nah. We're not the tri-betas. We take care of our own."
scene ep12_dikmas33 with dissolve
jm "I'd offer to remove my pots and plants from the porch, but it gets cold out there during winter."
scene ep12_dikmas29 with dissolve
rs "I think Jacob had the right idea. Let's do some work on the attic and fit the guys up there."
rs "So, we have capacity for roughly five more DIKs before we need to talk about our living arrangements."
scene ep12_dikmas35 with dissolve
tm "It shouldn't be all five this semester. Six months fly by, and before we know it, we have a fall batch of freshies knocking on our door."
scene ep12_dikmas32 with dissolve
jb "There are more ways to fix that. I'm not against putting another bed in my room."
scene ep12_dikmas33 with dissolve
jm "Yeah, fuck it. I can do a bunk bed, too. Don't let it stop us from accepting new guys into the frat."
jm "What good is a dick if it doesn't grow?"
$ guideSuggestedPage = 255
scene ep12_dikmas29 with dissolve
rs "Hm... It would be nice if we grew to be the biggest frat on campus. If you guys are up to sharing rooms and whatnot, let's explore that option more."
rs "Also, it could take us a while to make the attic inhabitable."
scene ep12_dikmas41 with dissolve
$ mc_info = ["{size=-%d}Stick to your guns{/size}" % persistent.scale_factor,"ep12_dikmas_dik_choice_label","{size=-%d}Stay out of it{/size}" % persistent.scale_factor,"ep12_dikmas_neutral_choice_label","{size=-%d}Offer a part of your room{/size}" % persistent.scale_factor,"ep12_dikmas_chick_choice_label",not ep8_share_room]
show screen major_choice_screen
$ renpy.pause()

label ep12_dikmas_dik_choice_label:
$ ep12_offered_room = "DIK"
scene ep12_dikmas42 with dissolve
mc "I'm sorry, guys, but I'm not gonna offer my room like that."
scene ep12_dikmas45 with dissolve
mc "I worked my ass off making it inhabitable. I don't want to share it now."
scene ep12_dikmas29 with dissolve
rs "Again, sharing rooms is not our first solution. But it's good that some of us are volunteering."
rs "If we want the frat to grow even bigger, we will need room for beds and personal space."
jump ep12_dikmas_after_choice_label

label ep12_dikmas_neutral_choice_label:
$ ep12_offered_room = "NEUTRAL"
mc "(I'm not that happy about this idea... But if I speak up, I'll look like a selfish ass.)"
if ep8_share_room:
    mc "(Let's hope it doesn't come to this, but I might have to give up a part of my room eventually.)"
else:
    mc "(Let's hope it doesn't come to this, and I'll fight this fight when I have to.)"
jump ep12_dikmas_after_choice_label

label ep12_dikmas_chick_choice_label:
$ ep12_offered_room = "CHICK"
scene ep12_dikmas40 with dissolve
mc "Fine. If it comes to it, I'll think about sharing my room with someone."
scene ep12_dikmas43 with dissolve
mc "We could install another door and extend the wall to create two rooms."
scene ep12_dikmas44 with dissolve
mc "I love my room so much, but family comes first."
jump ep12_dikmas_after_choice_label

label ep12_dikmas_after_choice_label:
scene ep12_dikmas35 with dissolve
tm "I hope we don't get some total losers for this next batch."
scene ep12_dikmas37 with dissolve
de "Hey! [name] and I fucking slayed, and you know it!"
stop music fadeout 3
scene ep12_dikmas46 with dissolve
$ renpy.pause()

$ new_bio("Tommy", "Tommy gave me a shirt for Christmas and told me he appreciated me. It was the nicest thing he ever did for me.")
if ep12_offered_room == "DIK":
    $ new_bio("You", "I told the DIKs that I didn't want to share my room with new DIKs.")
elif ep12_offered_room == "NEUTRAL":
    $ new_bio("You", "I stayed out of the conversation when the DIKs talked about sharing rooms with new DIKs.")
else:
    $ new_bio("You", "I offered to share a part of my room with a new DIK if it was needed.")
if ep12_jsolo:
    $ new_bio("Josy", "Josy invited me to her mom's place during winter break. She wanted me to meet her mom, even though it felt weird that Maya couldn't come with us.")

label ep12_holidays_label:
play music "music/ep11/licensed_music/track165.mp3"
scene ep12_holidays1 with fade
$ renpy.pause()

if breakup or ep4_toldDerekAboutJade:
    scene ep12_holidays3 with dissolve
    if breakup:
        dad "I'm sad to hear that. Breakups are hard."
    else:
        dad "I'm sad to hear that. Losing friends can be difficult."
    if branchMayaJosy:
        dad "I'm sorry I wasn't more supportive of your relationship. It was a situation I couldn't relate to."
    scene ep12_holidays2 with dissolve
    mc "Yeah... I'll try my best to get over it, but it's wearing me down."
    scene ep12_holidays3 with dissolve
    if breakup:
        dad "How come you broke up?"
    else:
        dad "What was the reason for it?"
    scene ep12_holidays2 with dissolve
    if branchZoey:
        if ep4_toldDerekAboutJade:
            if breakup:
                mc "I was going to break up with her because of Zoey."
                scene ep12_holidays4 with dissolve
                dad "Was it about Zoey?"
                scene ep12_holidays5 with dissolve
                mc "Part of it was, but I did a horrible thing with Sage's mom."
            else:
                mc "I did a horrible thing with Sage's mom."
            scene ep12_holidays4 with dissolve
            if branchSage:
                dad "With...her mom?"
            else:
                dad "With...Sage's mom?"
            scene ep12_holidays5 with dissolve
            mc "You probably don't want to hear it. But yeah, I did something bad, and that led to this. So..."
            scene ep12_holidays3 with dissolve
            dad "Do you regret it?"
            scene ep12_holidays2 with dissolve
            mc "I do."
            scene ep12_holidays8 with dissolve
            dad "Then use that as a life lesson."
            scene ep12_holidays5 with dissolve
            mc "Yeah... I learned my lesson, but I wish I hadn't had to."
            if breakup:
                mc "And about Zoey... We love each other, and we just got back together."
                scene ep12_holidays7 with dissolve
                dad "It might not help you feel better about your breakup, but I'm happy for you and Zoey."
                scene ep12_holidays5 with dissolve
                mc "Thanks. It's not the perfect way to get back together, but it's what we both want."
                scene ep12_holidays7 with dissolve
            else:
                mc "But there's some good news too regarding Zoey... We love each other, and we just got back together."
                scene ep12_holidays7 with dissolve
                dad "It might not help you feel better about Sage, but I'm happy for you and Zoey."
            dad "I can't say I'm surprised. I know how hard it was for you to get over her. It appears you never did."
            scene ep12_holidays5 with dissolve
            mc "Yeah. I was fooling myself..."
        else:
            mc "It was because of Zoey."
            scene ep12_holidays4 with dissolve
            dad "It was about Zoey?"
            scene ep12_holidays5 with dissolve
            mc "Yeah, but it's also good. We love each other, and we just got back together."
            scene ep12_holidays7 with dissolve
            dad "It might not help you feel better about your breakup, but I'm happy for you and Zoey."
            scene ep12_holidays5 with dissolve
            mc "Thanks. It's not the perfect way to get back together, but it's what we both want."
            scene ep12_holidays7 with dissolve
            dad "I can't say I'm surprised. I know how hard it was for you to get over her. It appears you never did."
            scene ep12_holidays5 with dissolve
            mc "Yeah. I was fooling myself..."
    elif ep4_toldDerekAboutJade or ep12_break_or_tell == "break" or ep12_break_or_tell == "tell":
        mc "I did a horrible thing with Sage's mom."
        scene ep12_holidays4 with dissolve
        if branchSage:
            dad "With...her mom?"
        else:
            dad "With...Sage's mom?"
        scene ep12_holidays5 with dissolve
        mc "You probably don't want to hear it. But yeah, I did something bad and that led to this. So..."
        scene ep12_holidays3 with dissolve
        dad "Do you regret it?"
        scene ep12_holidays2 with dissolve
        mc "I do."
        scene ep12_holidays8 with dissolve
        dad "Then use it as a life lesson."
        scene ep12_holidays5 with dissolve
        mc "Yeah... I learned my lesson, but I wish I didn't have to learn it."
    else:
        mc "It was my fault. I wasn't ready for a relationship. I wanted to stay single."
        mc "It's either that or the relationship didn't make me feel like it was enough for me. It's hard to put a finger on it."
        scene ep12_holidays3 with dissolve
        dad "You'll likely experience more heartbreaks in your life."
        scene ep12_holidays5 with dissolve
        mc "Thanks, Dad..."
        scene ep12_holidays3 with dissolve
        dad "It's not what I wish, of course. But that's life for you."
        scene ep12_holidays5 with dissolve
        mc "Yeah..."
if branchZoey:
    scene ep12_holidays9 with dissolve
    dad "That makes me happy to hear!"
    scene ep12_holidays6 with dissolve
    mc "It does?"
    scene ep12_holidays10 with dissolve
    dad "Why wouldn't it?"
    scene ep12_holidays6 with dissolve
    mc "Well, I was worried you'd think it was a bad idea."
    scene ep12_holidays10 with dissolve
    dad "She may have broken your heart, but you two finding a way back together confirms suspicions."
    scene ep12_holidays6 with dissolve
    mc "What suspicions?"
    scene ep12_holidays10 with dissolve
    dad "That it wasn't because she didn't love you that she left. It was because of personal reasons."
    scene ep12_holidays6 with dissolve
    mc "It didn't feel that way when she stopped caring about me, and we lost touch."
    mc "I don't think she realized what her feelings were for me back then, but she does now."
    scene ep12_holidays9 with dissolve
    dad "Whatever the reason is, I'm overjoyed. You two share a special bond."
    scene ep12_holidays6 with dissolve
    mc "Thank you, Dad."
if branchIsabella:
    scene ep12_holidays9 with dissolve
    dad "When will she get here?"
    scene ep12_holidays6 with dissolve
    mc "Tomorrow. If that's ok with you."
    scene ep12_holidays3 with dissolve
    dad "Tomorrow? Doesn't she have family to celebrate with?"
    scene ep12_holidays5 with dissolve
    mc "She doesn't."
    scene ep12_holidays7 with dissolve
    dad "Oh my... Well, why didn't you tell me earlier? She could have come here today."
    scene ep12_holidays5 with dissolve
    mc "I needed this alone time with you. You see, there's something I left out about her."
    mc "She's older than me."
    scene ep12_holidays7 with dissolve
    dad "There's nothing wrong with an age gap, son. It's just a number, and the older you get, the less the gap matters."
    scene ep12_holidays5 with dissolve
    mc "She's 36 years old."
    scene ep12_holidays9 with dissolve
    dad "Well, there you have it. She's thirty..."
    scene ep12_holidays8 with dissolve
    dad "36?"
    scene ep12_holidays5 with dissolve
    mc "Yeah."
    scene ep12_holidays3 with dissolve
    dad "Didn't you say she was in your class?"
    scene ep12_holidays5 with dissolve
    mc "About that... I wasn't technically lying, but..."
    mc "She's been my teacher in one of my classes."
    scene ep12_holidays14 with dissolve
    dad "Oh no..."
    scene ep12_holidays15 with dissolve
    mc "But it's nothing like that, Dad. Trust me."
    mc "We met in the library where she works as a librarian."
    mc "And after we got together, she became my teacher because my first teacher, Cathy, quit."
    scene ep12_holidays5 with dissolve
    mc "It wasn't a teacher-student kind of relationship at first. But then it became one..."
    mc "And, as you've already figured out, it's a problem for us."
    scene ep12_holidays3 with dissolve
    dad "Are you going to be on the news for this?"
    scene ep12_holidays5 with dissolve
    mc "I hope not... We've kept it a secret all semester."
    scene ep12_holidays3 with dissolve
    dad "*{i}Sigh{/i}* I'm worried about this."
    scene ep12_holidays5 with dissolve
    mc "Yeah, I'm worried too. But I love her."
    scene ep12_holidays4 with dissolve
    dad "You love her?"
    scene ep12_holidays5 with dissolve
    mc "Yeah... I know you know how that's like."
    mc "To be into someone you shouldn't be."
    scene ep12_holidays7 with dissolve
    dad "Yes... I remember that feeling."
    dad "I'm happy you found love. But I will always be a parent first when it comes to you."
    scene ep12_holidays6 with dissolve
    mc "I know. And I'm happy that you are looking out for me."
    mc "Do you still want to meet her?"
    scene ep12_holidays9 with dissolve
    dad "I do."
    scene ep12_holidays6 with dissolve
    mc "Tomorrow then."
    scene ep12_holidays9 with dissolve
    dad "Tomorrow."

scene ep12_holidays10 with dissolve
dad "How was the food?"
scene ep12_holidays11 with dissolve
mc "Delicious, Dad. I've missed your cooking."
scene ep12_holidays10 with dissolve
dad "It feels great to have you home. Even though I know it's just for a little while."
scene ep12_holidays6 with dissolve
mc "Yeah, I wish I could stay for the duration of the break, but I have plans."
if ep11_fighter:
    mc "I've been meaning to tell you, I've entered into a fighting competition."
    scene ep12_holidays12 with dissolve
    dad "A competition? Wow! With your fighting club?"
    scene ep12_holidays6 with dissolve
    mc "Yes. I'm fighting at my gym on the 29th. My trainer wanted me to join, and so I did."
    mc "I'm nervous about it."
    scene ep12_holidays12 with dissolve
    dad "I would be too. It's a big step. Can I watch?"
    scene ep12_holidays6 with dissolve
    mc "Dad... With you there, I'd get even more nervous."
    mc "Would it be ok if you don't show up for this one? If it's something I want to continue doing, I'll let you come for the next one."
    scene ep12_holidays13 with dissolve
    dad "Hehe. Are you ashamed of me?"
    scene ep12_holidays6 with dissolve
    mc "No, it's not that."
elif ep11_music:
    mc "I've been meaning to tell you, I've been asked to perform at the faculty's Christmas party."
    scene ep12_holidays12 with dissolve
    dad "Wow! You have?"
    scene ep12_holidays6 with dissolve
    mc "Yeah. Professor Hoff liked my performance at the recital, and he asked me to play at the party."
    mc "He says it's a way to network with people, but I also get paid some."
    scene ep12_holidays10 with dissolve
    dad "And you get to share your music."
    scene ep12_holidays6 with dissolve
    mc "Yeah, I will play 20 minutes worth of Christmas songs."
    scene ep12_holidays10 with dissolve
    dad "Then I understand you'll need some time to practice before that."
    scene ep12_holidays6 with dissolve
    mc "I haven't had too many opportunities to practice because of my finals."
else:
    mc "There's this big New Year's Eve party we're hosting, and I need to help out."

scene ep12_holidays13 with dissolve
dad "Well, if you're leaving for campus again soon, I won't hold back on being sappy this Christmas."
dad "You'll have to endure listening to my stories from your childhood."
scene ep12_holidays11 with dissolve
mc "You'll hear no complaints from me. I love being home, but I also love to be independent."
mc "Do you remember that feeling? Of moving out?"
scene ep12_holidays14 with dissolve
dad "Back then, life was different."
dad "I ran away from home when I was 15. And I didn't do it because of college or anything fancy..."
dad "I did it because I had to get away from Mom."
scene ep12_holidays15 with dissolve
mc "Right... It's not the same."
scene ep12_holidays14 with dissolve
dad "The first few months were the hardest. But my uncle took me under his wing as an apprentice, and it's because of him that I ended up working in construction."
scene ep12_holidays15 with dissolve
mc "Did you ever return home?"
scene ep12_holidays16 with dissolve
dad "I came to visit. And I know that Mom talked to Uncle Hank behind my back - well, because Hank told me."
dad "That's what I always liked about him. He didn't keep any secrets, but I was lying left and right."
scene ep12_holidays17 with dissolve
dad "That's how it was growing up. I often had to lie to Mom to avoid beatings."
dad "But Hank treated me well. He had a twisted sense of humor, too."
dad "He once sent me to the depot to purchase a list of materials for a contract we were working on."
scene ep12_holidays18 with dissolve
dad "And I had to ask the clerk where to find the wooden BU-tt plugs."
dad "And the clerk laughed at me, said someone was joking with me, and that they didn't sell any buttplugs."
scene ep12_holidays20 with dissolve
dad "I didn't fully understand the joke at the time, but that was Uncle Hank for you."
scene ep12_holidays19 with dissolve
mc "Hahaha! That's a good one!"
scene ep12_holidays20 with dissolve
dad "Ahh... Uncle Hank. May God rest his soul."
scene ep12_holidays21 with dissolve
mc "Was it because of Hank that you got work with Kovak's Carpentry?"
scene ep12_holidays20 with dissolve
dad "It was. After I finished my apprenticeship, Hank recommended me for the job."
dad "Hank was getting old, and he couldn't afford to keep me on. He thought it was the best move for me."
dad "He always looked out for me. He was like the parent I never had."
scene ep12_holidays22 with dissolve
mc "I've read more of Mom's diary, Dad. And...uh..."
mc "There's something I need to talk to you about."
scene ep12_holidays23 with dissolve
dad "*{i}Sigh{/i}* I've been expecting it."
scene ep12_holidays24 with dissolve
mc "It's been great to learn about Mom, and I got to read her stories about how you two met."
mc "It's been graphic at times. Um... I didn't need to read the details about her sex life."
scene ep12_holidays22 with dissolve
mc "But then I came across this entry she wrote that left me stunned."
scene ep12_holidays25 with dissolve
dad "..."
scene ep12_holidays22 with dissolve
mc "She wrote that her mom told her dad about the two of you. And that they didn't want you to be together."
scene ep12_holidays23 with dissolve
dad "It's true."
scene ep12_holidays22 with dissolve
mc "I know. You've told me that, but you never told me he fired you and threatened to sue you. And that you assaulted him..."
mc "Mom loved you, but the way she described it shocked me."
scene ep12_holidays25 with dissolve
mc "I felt like I didn't recognize you through her words."
mc "Did you really hit grandpa?"
scene ep12_holidays26 with dissolve
dad "He fired me for what I had done. And it's true, I didn't react well to hearing that."
dad "And I hit him repeatedly."
scene ep12_holidays25 with dissolve
mc "Because you loved Mom?"
scene ep12_holidays26 with dissolve
dad "That, and he wanted to take away what I had worked hard for - my job."
dad "It was all I had. And in that moment, he took it away from me."
dad "It was a knee-jerk reaction, and I even scared myself for letting it happen."
scene ep12_holidays27 with dissolve
dad "Later, he sued me for assault."
scene ep12_holidays28 with dissolve
mc "He sued you for the assault? Not because you trespassed?"
scene ep12_holidays27 with dissolve
dad "He couldn't hold me liable for that. Kovak's Carpentry had insurance to cover such disputes."
dad "But he pressed charges against me because I broke his nose, and I ended up settling in court to avoid prison."
scene ep12_holidays29 with dissolve
dad "*{i}Sniffles{/i}*"
mc "Dad..."
scene ep12_holidays30 with dissolve
dad "But Mr. Kovak understood my side of the story and didn't fire me, despite the lawsuit."
dad "He let me work on minor contracts while they finished the work on the hotel."
scene ep12_holidays31 with dissolve
dad "There's so much I've wanted to tell you, but I couldn't."
dad "That's why I let the diary do it for me."
scene ep12_holidays32 with dissolve
mc "What? The diary didn't come from Mom? I thought it was my inheritance."
scene ep12_holidays30 with dissolve
dad "It's her diary, but I'm the one who gave it to you."
scene ep12_holidays32 with dissolve
mc "Do you know what's in it?"
scene ep12_holidays31 with dissolve
dad "Yes. Life with Lynette has been the hardest journey I've made."
dad "I have protected you in the way I thought was best. But I've realized I didn't do you any favors in doing so."
scene ep12_holidays33 with dissolve
dad "Now, I wanted the diary to tell you the truth."
dad "It's because I love you, and don't have the capacity to tell you myself."
scene ep12_holidays34 with dissolve
mc "Why?"
scene ep12_holidays33 with dissolve
dad "Because I'm scared you won't forgive me."
scene ep12_holidays34 with dissolve
mc "Forgive you for what?"
scene ep12_holidays33 with dissolve
dad "For lying and sheltering you from the harsh reality in a way that I shouldn't have."
scene ep12_holidays35 with dissolve
mc "Dad... Stop."
mc "You've been the best Dad all my life. If you're worried that I will look at you in another way because you did bad things when you were young, guess what...?"
mc "It's not gonna happen."
scene ep12_holidays34 with dissolve
mc "I'm not perfect either. I've made many mistakes and bad calls."
mc "And I refuse to let anyone, or anything, change the way I look at you."
scene ep12_holidays35 with dissolve
mc "If this diary is going to tell me that you're anything but great..."
mc "To hell with it! I won't read another word from it."
mc "I already know who you are. I don't need to hear about your sins and mistakes. I only need you."
scene ep12_holidays36 with dissolve
dad "I love you, son."
scene ep12_holidays37 with dissolve
mc "I know you do. And I love you."
scene ep12_holidays36 with dissolve
dad "I'm so proud of who you have become. Never forget that."
scene ep12_holidays37 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep12_holidays38 with dissolve
mc "{i}Dad...{/i}"
scene black with dissolve
mc "{i}What have you done?{/i}"

if branchIsabella and not breakup:
    $ new_bio("Dad", "I told Dad about Bella and our relationship. He was surprised to learn that she was my teacher, but agreed to meet her.")
$ new_bio("Dad", "Dad told me he gave me Mom's diary so I could learn the truth he couldn't tell me. I was upset that the diary showed him in a bad light and didn't want to read it anymore.")

label ep12_zoey_label:
play music "music/ep11/licensed_music/track183.mp3"
scene ep12_zoey1 with wipeleft
$ renpy.pause()
show ep12_zoey2
if not persistent.ep12_cardcam14:
    show screen ep12_render_screen("cam14")
with dissolve
zmom "Zoey. I thought I heard footsteps out in the garden, and there was a man out there looking for you."
show ep12_zoey4
hide screen ep12_render_screen
with dissolve
zo "I stopped believing in Santa when I was five, Mom."
scene ep12_zoey3 with dissolve
zmom "Haha! I wasn't talking about Santa."
if branchZoey:
    scene ep12_zoey5 with dissolve
else:
    scene ep12_zoey6 with dissolve
mc "Merry Christmas, everyone."
if branchZoey:
    scene ep12_zoey10 with dissolve
else:
    scene ep12_zoey7 with dissolve
zo "[name]? You're here."
if branchZoey:
    scene ep12_zoey9 with dissolve
else:
    scene ep12_zoey8 with dissolve
mc "I'm celebrating with Dad as always. I thought I'd drop by."
mc "I hope I'm not interrupting any tradition."
scene ep12_zoey11 with dissolve
zmom "You're always welcome here, [name]. Merry Christmas to you, too."
scene ep12_zoey12 with dissolve
flo "Merry Christmas, [name]. It's been a while."
scene ep12_zoey13 with dissolve
mc "Yeah. How have you been?"
scene ep12_zoey12 with dissolve
flo "Can't complain."
flo "Come. Have a drink with us."
if branchZoey:
    scene ep12_zoey10 with dissolve
else:
    scene ep12_zoey7 with dissolve
zo "I want to talk to him before you guys do that."
if branchZoey:
    scene ep12_zoey9 with dissolve
else:
    scene ep12_zoey8 with dissolve
mc "Your room?"
scene ep12_zoey12 with dissolve
flo "The drink will wait for you."
if branchZoey:
    scene ep12_zoey18 with dissolve
    mc "How has your Christmas been so far?"
    scene ep12_zoey20 with dissolve
    zo "It's been nice. Everyone has been getting along. It's weird."
    scene ep12_zoey29 with dissolve
    mc "Even you and Floyd?"
    scene ep12_zoey30 with dissolve
    zo "Yeah. It's hella weird... Maybe Mom told him to behave, but that never worked before."
    scene ep12_zoey29 with dissolve
    mc "That must be a nice feeling for Alison - to see you two get along."
    scene ep12_zoey31 with dissolve
    zo "Maybe it was his Christmas gift to her or something. Or maybe it was because he thinks I'm going away again soon."
    scene ep12_zoey29 with dissolve
    mc "To B&R? Did you get in?"
    scene ep12_zoey31 with dissolve
    zo "I'm on the waiting list."
    scene ep12_zoey29 with dissolve
    mc "At what spot?"
    scene ep12_zoey31 with dissolve
    zo "8. It sucks..."
    scene ep12_zoey32 with dissolve
    mc "No, no. 8 isn't bad. 8 is good."
    scene ep12_zoey33 with dissolve
    zo "Really? Do you think it's doable?"
    scene ep12_zoey32 with dissolve
    mc "Someone I know was 14th in line, and she got in."
    scene ep12_zoey30 with dissolve
    zo "That makes me feel better."
    scene ep12_zoey29 with dissolve
    mc "Just stay positive. It's not over because you're on that list."
    scene ep12_zoey34 with dissolve
    zo "What about you? How have you been?"
    scene ep12_zoey35 with dissolve
    mc "I had my finals week. It was stressful."
    scene ep12_zoey36 with dissolve
    zo "How did it go?"
    scene ep12_zoey35 with dissolve
    if minigames:
        if (englishResult + bonusPercentageEnglish >= 70 - (englishBoost*5)) or (mathResult + bonusPercentageMath >= 80 - (mathBoost*10)):
            mc "I had a good feeling from it, but we'll see after Christmas."
        else:
            mc "I don't think I did very well. I'll need a Christmas miracle to pass my tests."
    else:
        mc "I had a good feeling from it, but we'll see after Christmas."
    mc "I try to put it out of my mind until I know for sure."
    scene ep12_zoey37 with dissolve
    zo "Here's hoping."
    scene ep12_zoey29 with dissolve
    mc "Aside from the tests, I've been celebrating with my friends and such..."
    mc "Things are going on that weigh on my mind, but it's been ok."
    mc "I've been thinking a lot about you."
    scene ep12_zoey38 with dissolve
    zo "Same. Like...fucking daily."
    if breakup:
        scene ep12_zoey40 with dissolve
        if "Josy" in breakup:
            mc "I broke up with my girlfriends."
        else:
            mc "I broke up with my girlfriend."
        scene ep12_zoey41 with dissolve
        zo "You did?"
        scene ep12_zoey40 with dissolve
        if ep4_toldDerekAboutJade:
            mc "Well, she broke up with me. And it wasn't even because of you."
        else:
            mc "Yeah... It was horrible. I felt like a piece of shit doing it."
            mc "But I had to do it."
        scene ep12_zoey41 with dissolve
        zo "I don't want to read too much into that, but does that mean...?"
    else:
        scene ep12_zoey39 with dissolve
        mc "Yeah. Me too."
        scene ep12_zoey38 with dissolve
        zo "So... What does that mean?"
    scene ep12_zoey42 with dissolve
    mc "I have a lot to say to you, but I don't know where to begin."
    scene ep12_zoey43 with dissolve
    zo "Start somewhere. Let the words come to you."
    scene ep12_zoey44 with dissolve
    mc "You told me that you love me, but I'm not sure if you do."
    scene ep12_zoey45 with dissolve
    zo "But I'm sure... I do."
    scene ep12_zoey46 with dissolve
    zo "What makes you unsure?"
    scene ep12_zoey44 with dissolve
    mc "I'm not the same guy I was when you left for San Diego."
    mc "Maybe it's that guy you love and not me."
    scene ep12_zoey46 with dissolve
    zo "Try me. How are you different?"
    scene ep12_zoey44 with dissolve
    mc "Take a look at what I've done during my first semester of college."
    $ ep12_zworries = 0
    scene ep12_zoey47 with dissolve
    if ep4_smoked_weed or ep9_lily_nicole_lewd or ep10_shroom_choice == "DIK":
        $ ep12_zworries += 1
        mc "I've tried drugs, gotten into fights, partied a lot, and gone to strip clubs..."
    else:
        mc "I've partied a lot, gotten into fights, and gone to strip clubs..."
    if len(mphone_stats_girl_list) > 10:
        $ ep12_zworries += 1
        mc "I've had sex with a lot of girls. I've lost count."
    elif len(mphone_stats_girl_list) > 5:
        mc "I've had sex with several girls."
    if quinn_shop_special_lvl > 0 or quinn_shop_japanese_lvl > 0 or quinn_shop_spicy_lvl > 0 or ep3_envyLewd == 1 or ep3_envyLewd == 2 or ep4_roseLewd or ep7_accept_madame:
        $ ep12_zworries += 1
        mc "I've even paid for sex."
    if ep4_fuckedJade:
        $ ep12_zworries += 1
        if branchSage:
            mc "I fucked my girlfriend's mom, who used to be my teacher. I didn't know it was her mom, but I did it."
        else:
            mc "I fucked my friend's mom, who used to be my teacher. I didn't know it was her mom, but I did it."
        if ep4_toldDerekAboutJade:
            mc "There's even a sex tape of it floating around out there somewhere that I'm responsible for."
            if "Sage" in breakup:
                mc "That's why Sage broke up with me, if you hadn't guessed."
            elif breakup:
                mc "That's why my girlfriend broke up with me, if you hadn't guessed."
    elif ep3_acceptedJade:
        $ ep12_zworries += 1
        if branchSage:
            mc "I got a handjob from my girlfriend's mom in class, when she was my teacher. I didn't know she was my girlfriend's mom, but I did it."
        else:
            mc "I got a handjob from my friend's mom in class, when she was my teacher. I didn't know she was my friend's mom, but I did it."

    if ep2FoughtJocks:
        mc "And about the fights... It wasn't just self-defense. I could have avoided fighting, but I did it."
        mc "I broke the code that Dad taught me."
        if ep5_agitatedCaleb:
            mc "And I even provoked a fight."
    scene ep12_zoey53 with dissolve
    mc "During Hell Week, I broke into the preps' mansion. I streaked at the mall and got chased by a cop."
    if ep8_midterms_cheated == "DIK":
        $ ep12_zworries += 1
        mc "I cheated on my midterm by looking at the answers I found in the bathroom."
    scene ep12_zoey47 with dissolve
    mc "All of this is a result of what happened between us and what happened to me after you left."
    mc "I don't blame you for my actions. I made those choices, and I stand by them - mistakes or not."
    scene ep12_zoey53 with dissolve
    mc "I could go on and tell you in detail about everything I did. But I think you can hear it from these words..."
    mc "I'm not the same guy that you used to know."
    mc "Can you still say that you love me after hearing all this?"
    scene ep12_zoey48 with dissolve
    $ renpy.pause()
    scene ep12_zoey49 with dissolve
    zo "[name]. I know you're not the same person anymore."
    zo "I'm not the same girl I was, either."
    scene ep12_zoey50 with dissolve
    zo "But I know that underneath all of this... There's still the guy I grew up with."
    zo "And there's still the guy I fell in love with."
    scene ep12_zoey51 with dissolve
    zo "You can tell me about everything you did. Every girl you fucked. Every guy you punched."
    zo "But don't focus on the negatives because I know you've done great things too. Your brothers have told me all about it."
    scene ep12_zoey49 with dissolve
    zo "You're focusing on the negatives because you think they will scare me away."
    zo "But they won't. We all do bad shit."
    scene ep12_zoey51 with dissolve
    zo "I want to slam the big fat reset button with us, and that goes for whatever you did, too."
    zo "To me, the real question isn't if I'm ok with what you did. The question is, can you forgive me for what I have done?"
    scene ep12_zoey54 with dissolve
    mc "I want to. And I think that I can forgive you in time."
    scene ep12_zoey52 with dissolve
    mc "It only hurt so much because you meant the world to me."
    mc "And what's that if not love?"
    scene ep12_zoey55 with dissolve
    $ renpy.pause()
    scene ep12_zoey56 with dissolve
    mc "I love you, Zoey. I fucking love you."
    scene anim_zoey_kiss_ep12 with dissolve
    pause
    scene ep12_zoey57 with dissolve
    $ renpy.pause()
    scene ep12_zoey58 with dissolve
    zo "Then let's do this. Together."
    zo "I'm not scared of whatever challenges or drama we have to face."
    scene ep12_zoey59 with dissolve
    mc "Neither am I."
    scene ep12_zoey60 with dissolve
    $ renpy.pause()
    scene ep12_zoey61 with dissolve
    zmom "Zoey? [name]? There's cocoa down here if you want it."
    scene ep12_zoey62 with dissolve
    zo "Wanna tell them the news?"
    scene ep12_zoey63 with dissolve
    mc "Yes."
    mc "And I don't know why, but I want to have that drink with Floyd."
    scene ep12_zoey64 with dissolve
    zo "Haha! What's wrong with you?"
    scene ep12_zoey63 with dissolve
    mc "I told you I changed. Is THIS the thing that made you react?"
    scene ep12_zoey64 with dissolve
    zo "Give me time, and I'll be ok with it."
    scene ep12_zoey14 with Dissolve(2)
    $ renpy.pause(10)
    show screen click_to_continue_screen with dissolve
    $ renpy.pause(2)
    hide screen click_to_continue_screen with dissolve
    $ renpy.pause()
    scene ep12_zoey15 with Dissolve(2)
    $ renpy.pause()
    scene ep12_zoey16 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    scene ep12_zoey17 with dissolve
    $ renpy.pause()
    $ new_bio("Zoey", "I told Zoey what I had been up to since starting college. I didn't want to keep anything from her. She took the news well, and it didn't turn her away.")
else:
    scene ep12_zoey18 with dissolve
    mc "How has your Christmas been so far?"
    scene ep12_zoey19 with dissolve
    zo "[name]... You should have called."
    scene ep12_zoey21 with dissolve
    mc "I wasn't sure if you'd pick up. You haven't been vocal with me since our Christmas party."
    scene ep12_zoey22 with dissolve
    zo "Well duh! It's because I feel stupid."
    zo "I put myself out there, thinking you'd feel the same. And you flat-out shut me down."
    scene ep12_zoey23 with dissolve
    zo "I can't unsay those words to you."
    scene ep12_zoey21 with dissolve
    mc "I know how you're feeling."
    scene ep12_zoey23 with dissolve
    zo "No, you don't."
    scene ep12_zoey21 with dissolve
    mc "When you left for San Diego, how do you think I felt?"
    mc "I had feelings for you, but I couldn't share them because you weren't here."
    mc "I had to process all of that alone. It was one of the hardest things I've done."
    mc "And I felt stupid for not telling you how I felt."
    scene ep12_zoey25 with dissolve
    mc "But I went through the emotions, and this is me on the other side."
    mc "When I told you it was too late for us... It's because I've mourned us already."
    mc "I've processed our breakup. And while I feel nostalgic around you, I can't force myself to go back and feel that way about you again."
    scene ep12_zoey22 with dissolve
    zo "Because it hurts?"
    scene ep12_zoey21 with dissolve
    if not branchAlone:
        if not breakup:
            if tc < 5:
                mc "It's one of the reasons, yeah. But also, I'm past feeling that way about you. I'm in a happy relationship now."
            else:
                mc "It's one of the reasons, yeah. But also, I'm past feeling that way about you."
        else:
            mc "It's one of the reasons, yeah. But also, I'm past feeling that way about you."
    else:
        mc "It's one of the reasons, yeah. But also, I'm past feeling that way about you."
    scene ep12_zoey25 with dissolve
    mc "I have moved on, Zoey. And you should, too."
    scene ep12_zoey22 with dissolve
    zo "But... If we both move on, can we even stay friends?"
    scene ep12_zoey21 with dissolve
    if not branchAlone and not breakup:
        mc "Co-exist on campus when you come to B&R, sure. But friends... I... I don't know."
        if branchSage:
            scene ep12_zoey25 with dissolve
            mc "Truth be told, my girlfriend doesn't think it's a good idea."
            mc "She thinks you don't see me as a friend anymore, and that makes her uncomfortable."
        elif branchMayaJosy:
            scene ep12_zoey25 with dissolve
            mc "Truth be told, my girlfriends had some opinions on that."
            mc "They understood our situation, but I could sense that they didn't like the idea of me being close to you."
    else:
        mc "Co-exist on campus when you come to B&R, sure. But friends... I... I don't know."
    scene ep12_zoey22 with dissolve
    zo "So, we can't hang out anymore?"
    scene ep12_zoey26 with dissolve
    mc "I'm not sure."
    scene ep12_zoey23 with dissolve
    zo "Then why are you even here? I don't get it."
    scene ep12_zoey26 with dissolve
    mc "*{i}Sigh{/i}* I was worried about you."
    mc "Do you think it's possible to stay friends? Is that something you'd want?"
    scene ep12_zoey23 with dissolve
    zo "How would I know when you don't?"
    if not ep9_mad_at_zoey:
        zo "I thought we got along great ever since I came back from San Diego."
    else:
        zo "I thought we got along great lately."
    scene ep12_zoey21 with dissolve
    if not ep9_mad_at_zoey:
        mc "We did."
    else:
        mc "We did. Um... Somewhat, at least."
    zo "..."
    scene ep12_zoey22 with dissolve
    zo "So, neither of us knows if we want to stay friends after this."
    zo "How do we find out for sure?"
    scene ep12_zoey21 with dissolve
    mc "We just have to decide..."
    mc "You're coming to B&R next semester. Ignoring this won't make it go away or make us feel better."
    scene ep12_zoey24 with dissolve
    zo "If I even get in."
    scene ep12_zoey27 with dissolve
    zmom "Zoey? [name]? There's cocoa down here if you want it."
    scene ep12_zoey26 with dissolve
    mc "Maybe I should get going."
    scene ep12_zoey24 with dissolve
    zo "Yeah. Next time, use the phone if this is how it's going to be."
    stop music fadeout 3
    scene ep12_zoey28 with dissolve
    $ renpy.pause()
    $ new_bio("Zoey", "I went to check up on Zoey during Christmas, and it didn't go well. We need to figure out whether we can stay friends or if we need to move on permanently.")

label ep12_nerds_label:
hide screen new_phone_screen
play sound "sound_effects/season3/game_over.mp3"
scene ep12_nerds1 with dissolve
$ renpy.pause()
mg "You do one wrong thing, and it's game over like that!?"
mg "Aargh! Fucking shit game!"
play music "music/ep11/licensed_music/track153.mp3"
scene ep12_nerds2 with dissolve
be "It's just a game."
scene ep12_nerds3 with dissolve
mg "Well, I hate it!"
show ep12_nerds4
if not persistent.ep12_cardcam15:
    show screen ep12_render_screen("cam15")
with dissolve
rn "Why the rage? Didn't get the toys you wished for Christmas?"
show ep12_nerds9
hide screen ep12_render_screen
with dissolve
mg "Do you know what I didn't get for Christmas?"
mg "Retribution."
scene ep12_nerds5 with dissolve
rn "*{i}Sigh{/i}* It's coming. But it will take longer than we thought."
scene ep12_nerds9 with dissolve
mg "It's not coming fast enough. Give them another semester, and they'll grow even bigger!"
mg "We have to hit them while they're small and insignificant."
scene ep12_nerds12 with dissolve
be "So, the letters we sent out achieved nothing?"
scene ep12_nerds7 with dissolve
rn "They had an effect, alright. Anthony beat up Derek because of it."
scene ep12_nerds13 with dissolve
be "Oh, good. Derek had it coming."
be "The guy would fart when I was in the dorm with him. Unapologetic rancid farts!"
scene ep12_nerds8 with dissolve
rn "Hahaha!"
scene ep12_nerds13 with dissolve
be "It was NOT funny! His poo particles went into my nose."
scene ep12_nerds9 with dissolve
mg "A mere beating isn't enough."
scene ep12_nerds5 with dissolve
rn "He did it in front of everyone! Security even got involved. There will be disciplinary actions, I'm sure."
scene ep12_nerds9 with dissolve
mg "For Anthony, maybe. But what about the rest of them!? Why aren't they raging mad right now? We gave them all the ammo!"
mg "The Alpha Nu Omegas aren't doing anything! And I thought they would be the ones to seal the deal."
scene ep12_nerds5 with dissolve
rn "I told you the letters were too vague. The jocks need things to be pointed out to them, and the preps might need extra motivation."
scene ep12_nerds10 with dissolve
mg "What are you suggesting?"
scene ep12_nerds5 with dissolve
rn "Let's do plan B already. Let's bring them all together."
scene ep12_nerds14 with dissolve
be "The jocks and the preps in the same room as us?"
scene ep12_nerds6 with dissolve
rn "Yeah. Let's try the honest approach to speed things along."
rn "Let's call the VPs and Ps to a meeting and make the case for a joint complaint to the counselors. That ought to get rid of the DIKs in no time."
scene ep12_nerds10 with dissolve
mg "We have operated in the shadows for so long. Sticking out our necks like that now... Is it too soon?"
scene ep12_nerds5 with dissolve
rn "If it works, then why worry about it?"
scene ep12_nerds12 with dissolve
be "If we got their attention with the letters, it's an easy in."
scene ep12_nerds6 with dissolve
rn "Yeah, we can say we got letters too or something. They don't have to know we were behind it all."
scene ep12_nerds11 with dissolve
mg "The Trojan Horse. It's not a bad idea."
stop music fadeout 3
scene ep12_nerds15 with dissolve
rn "Alright. It's my turn; pass the controller."
if roadIsabella:
    show screen new_phone_screen
    jump ep12_bhome_label

label ep12_jsolo_label:
if ep12_jsolo:
    show screen new_phone_screen
else:
    hide screen new_phone_screen
$ renpy.sound.play("sound_effects/season3/fireplace.mp3", channel="sfx2", loop=True)
play music "music/ep11/christmas_jazz.mp3"
if ep12_jsolo:
    scene ep12_jsolo1b with wipeleft
    js "The finals were hard, but I think we both managed."
    scene ep12_jsolo2 with dissolve
    mc "Honestly, I'm not that sure about it. I'm second-guessing my answers now that I think about them."
    mc "We'll have to wait until after Christmas break to know for sure."
else:
    scene ep12_jsolo1 with wipeleft
    js "The finals were hard, but I think I managed."
if ep12_jsolo:
    scene ep12_jsolo3 with dissolve
else:
    scene ep12_jsolo3b with dissolve
ir "If you're having issues this early on in college, you should consider private tutoring."
ir "It will only get harder from here on in, I hope you realize."
if ep12_jsolo:
    scene ep12_jsolo7 with dissolve
else:
    scene ep12_jsolo7b with dissolve
js "I'm not worried. It has gotten easier over the course of the semester."
js "It's just that math got harder faster than I thought it would."
scene ep12_jsolo6 with dissolve
cli "Isn't economics all about numbers? How will you manage if you're struggling with math?"
if ep12_jsolo:
    menu:
        "[m_c1]Defend Josy":
            $ ep12_josy_defend_count += 1
            scene ep12_jsolo9 with dissolve
            mc "Didn't you go to school when you were young? I bet you struggled with something too."
            scene ep12_jsolo11 with dissolve
            cli "Sorry?"
            scene ep12_jsolo12 with dissolve
            mc "It's not uncommon for some subjects to be hard, especially in college."
            mc "And it's college math, too. Most of us won't even have a daily use for it beyond college."
            scene ep12_jsolo10 with dissolve
            $ renpy.pause()
            scene ep12_jsolo4b with dissolve
        "Say nothing":
            scene ep12_jsolo8b with dissolve
            js "Like everyone else, no one knows what they are being taught when they start a class."
            js "If they did, they wouldn't have to be there."
            scene ep12_jsolo4b with dissolve
            ir "An excellent point, Josephine."
else:
    scene ep12_jsolo8 with dissolve
    js "Like everyone else. No one knows what they are being taught when they start a class."
    js "If they did, they wouldn't have to be there."
    scene ep12_jsolo4 with dissolve
    ir "An excellent point, Josephine."
ir "Now, I've been waiting for you to tell me all about that blog of yours."
ir "Have you registered it as a business yet?"
if ep12_jsolo:
    scene ep12_jsolo7 with dissolve
else:
    scene ep12_jsolo7b with dissolve
js "As a matter of fact, I have."
js "Because I started accepting donations from subscribers and didn't want to end up with lots of problems later."
if ep12_jsolo:
    scene ep12_jsolo5 with dissolve
else:
    scene ep12_jsolo5b with dissolve
ir "Who's managing your bookkeeping?"
if ep12_jsolo:
    scene ep12_jsolo7 with dissolve
else:
    scene ep12_jsolo7b with dissolve
js "You're looking at her."
if ep12_jsolo:
    scene ep12_jsolo5 with dissolve
else:
    scene ep12_jsolo5b with dissolve
ir "Are you doing that by yourself?"
if ep12_jsolo:
    scene ep12_jsolo14 with dissolve
    mc "Wow, that's amazing. Can you do that?"
    scene ep12_jsolo15 with dissolve
else:
    scene ep12_jsolo15b with dissolve
js "It's not that hard."
scene ep12_jsolo16 with dissolve
ir "It doesn't surprise me that you found it simple."
ir "But I was surprised you'd waste your time on something that doesn't bring value to your company."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "It keeps me out of trouble with the IRS. I consider that value."
scene ep12_jsolo16 with dissolve
ir "What I mean is that your time is what brings value to your company and product."
ir "Simple tasks that others can handle shouldn't be your concern."
scene ep12_jsolo17 with dissolve
ir "It's not expensive to hire a bookkeeper for a small-scale company. I will refer you to one."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "I want to handle it by myself, thanks."
$ guideSuggestedPage = 256
scene ep12_jsolo6 with dissolve
cli "You don't have to be snarky when Iris offers you advice. She only means well."
if ep12_jsolo:
    menu:
        "[m_c1]Defend Josy":
            $ ep12_josy_defend_count += 1
            scene ep12_jsolo9 with dissolve
            mc "She's not snarky. Josy is passionate about doing it on her own."
            mc "If anything, calling it simple is putting her down. I couldn't do what she's doing."
        "Say nothing":
            scene ep12_jsolo13 with dissolve
            mc "(I want to say something, but I should stay out of it...)"
            scene ep12_jsolo8b with dissolve
            js "I don't need her help. I like doing things on my own. That's the point I'm trying to make."
else:
    scene ep12_jsolo8 with dissolve
    js "I don't need her help. I like doing things on my own. That's the point I'm trying to make."
scene ep12_jsolo16 with dissolve
ir "I didn't realize you wanted to stand completely on your own legs."
ir "That's admirable."
if ep12_jsolo:
    scene ep12_jsolo7 with dissolve
else:
    scene ep12_jsolo7b with dissolve
js "Thank you... If I wanted advice, I'd ask you."
if ep12_jsolo:
    scene ep12_jsolo4b with dissolve
else:
    scene ep12_jsolo4 with dissolve
ir "Other than the boring aspects of running a business, tell me about the rest."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "Nothing is boring about it. I find everything fun."
if ep12_jsolo:
    scene ep12_jsolo4b with dissolve
else:
    scene ep12_jsolo4 with dissolve
ir "Yes, yes. But what about your actual product? Tell me more about it."
if ep12_jsolo:
    scene ep12_jsolo21 with dissolve
else:
    scene ep12_jsolo21b with dissolve
js "Well, I have some exciting news. One of the bigger bloggers on the platform contacted me the other week and asked for my permission to repost my photos."
js "She posted a collection of winter fashion, and I was in it."
scene ep12_jsolo18 with dissolve
js "She credited me for my pictures, and I saw more than a 300%% increase in followers in two days."
scene ep12_jsolo19 with dissolve
ir "Now that's a smart move."
if ep12_jsolo:
    scene ep12_jsolo21 with dissolve
else:
    scene ep12_jsolo21b with dissolve
js "Thank you."
scene ep12_jsolo19 with dissolve
ir "I meant by the other blogger."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "Come again?"
scene ep12_jsolo19 with dissolve
ir "She obviously got your content for free, dear. That's minimal effort on her end."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "But I got publicity. She didn't shaft me, if that's what you're saying."
scene ep12_jsolo16 with dissolve
ir "No, no. That wasn't what I was saying. I was making the point that it was a smart move for her to utilize her power position."
ir "Of course, smaller bloggers will jump at the chance to get a splash of her notoriety."
scene ep12_jsolo17 with dissolve
ir "Meanwhile, her business thrives on unique content for free."
ir "And that's how she will continue to stay ahead. She gets it."
if ep12_jsolo:
    scene ep12_jsolo20 with dissolve
else:
    scene ep12_jsolo20b with dissolve
js "It still sounds like you're saying that she used me."
if ep12_jsolo:
    scene ep12_jsolo23 with dissolve
else:
    scene ep12_jsolo23b with dissolve
ir "No, I'm saying she got the better end of that deal. But, of course, you have to start somewhere."
ir "In your position, it was a good choice too."
if ep12_jsolo:
    scene ep12_jsolo22 with dissolve
else:
    stop music fadeout 3
    scene ep12_jsolo22b with dissolve
$ renpy.pause()
if not ep12_jsolo:
    $ renpy.music.stop(channel="sfx2", fadeout=3)
if ep12_jsolo:
    jump ep12_jsolo_cont_label

label ep12_ret_label:
if not breakup and branchMayaJosy and check_mlove():
    jump ep12_pre_ret_label
else:
    show screen new_phone_screen
    play music "music/ep11/licensed_music/track172.mp3"
label ep12_ret2_label:
scene ep12_ret1 with wipeleft
rs "This is the place."
scene ep12_ret2 with dissolve
mc "Hm... Are we all gonna fit in here? It will get cramped."
scene ep12_ret3 with dissolve
rs "There's another room like this one down the hall. They are the dining halls."
rs "Tommy came up with the idea of splitting the dining rooms and keeping the frats separate."
scene ep12_ret4 with dissolve
mc "Is everyone ok with that?"
scene ep12_ret5 with dissolve
rs "The jocks loved the idea. Sage was the only one who put up a little bit of a fight."
scene ep12_ret6 with dissolve
menu:
    "Why didn't Sage like it?":
        mc "Why didn't Sage like it?"
        scene ep12_ret7 with dissolve
        rs "She didn't want us to act like kids in a divorced family and suggested we all could share the dining rooms."
        rs "But the votes were two frats against one sorority, so..."
        scene ep12_ret6 with dissolve
        mc "Yeah, so we'll split the party. No big deal. It sounds like a good approach to me."
    "I'm surprised they liked it":
        mc "I'm surprised they liked it."
        scene ep12_ret7 with dissolve
        rs "Yeah, it was weird seeing them agree with Tommy."
        scene ep12_ret6 with dissolve
        mc "But it sounds like a good approach. I think it will make the party more relaxed."
scene ep12_ret8 with dissolve
rs "Come."
scene ep12_ret9 with dissolve
rs "This is where we'll drink and dance the night away."
scene ep12_ret10 with dissolve
mc "What is this place? You've got a gymnasium here and conference rooms over there."
scene ep12_ret11 with dissolve
rs "It's an old building from before the campus gym was built. Nowadays, it's mostly used for conferences."
rs "I believe they use this gym for some local sports competitions, but that's about it."
rs "So, what do you think?"
scene ep12_ret12 with dissolve
mc "It will work. It's not like we have any better options."
scene ep12_ret11 with dissolve
rs "I'll be here helping out every day until New Year's Eve. If you're free, you're welcome to join me."
scene ep12_ret12 with dissolve
if ep11_fighter:
    mc "I'll help out as much as I can, but I have a fighting competition on the 29th. It will take all day."
    scene ep12_ret13 with dissolve
    rs "Any time you can spare is appreciated."
elif ep11_music:
    mc "I'll help out as much as I can, but I'm off on the 29th. I'm performing at the faculty's Christmas party."
    scene ep12_ret13 with dissolve
    rs "Any time you can spare is appreciated."
else:
    mc "I have a clean slate. I'll be here."
    scene ep12_ret13 with dissolve
    rs "I appreciate it."
scene ep12_ret12 with dissolve
mc "What about the rest of the DIKs?"
scene ep12_ret13 with dissolve
rs "Tommy and Leon should be back tomorrow. The rest, I don't know for sure."
rs "The jocks are already helping out, and several HOTs, too."
if "Sage" in breakup or ep4_toldDerekAboutJade:
    scene ep12_ret14 with dissolve
    rs "I hope you don't mind me asking, but is everything ok between you and Sage?"
    scene ep12_ret15 with dissolve
    if "Sage" in breakup:
        mc "No. We broke up recently."
        scene ep12_ret14 with dissolve
        rs "Oh, so that's why..."
    else:
        mc "No. Something happened, but I don't want to get into it."
        scene ep12_ret14 with dissolve
    rs "I noticed her being short with me when I mentioned you."
    scene ep12_ret15 with dissolve
    mc "Yeah. It's not the best situation to plan a party together with someone who doesn't want to be around you..."
    scene ep12_ret16 with dissolve
    rs "If that's the case, leave the rest of the planning to me. You did a great job with it as it is."

scene ep12_ret17 with dissolve
mc "Thanks for showing me the place. It's gonna be awesome! I'm off to the gym."
scene ep12_ret18 with dissolve
rs "Burning off that Christmas food?"
scene ep12_ret17 with dissolve
mc "Hah! Something like it."
if ep12_bianca_lewd:
    scene ep12_ret19 with dissolve
    $ renpy.pause()
    scene ep12_ret21 with dissolve
    mc "Hey, it's me."
    scene ep12_ret22 with dissolve
    bia "I've waited for your call."
    scene ep12_ret21 with dissolve
    mc "Sorry for keeping you waiting. I'm back on campus."
    scene ep12_ret22 with dissolve
    bia "Uh huh."
    scene ep12_ret21 with dissolve
    mc "And I was thinking... Wanna come over?"
    scene ep12_ret23 with dissolve
    bia "Tonight?"
    scene ep12_ret24 with dissolve
    mc "If you're free."

    scene ep12_ret23 with dissolve
    bia "Are you sure you want to do this?"
    if branchIsabella and wt_ep9_branch_numbers == 1:
        scene ep12_ret24 with dissolve
        mc "I am. But also, you should know that I broke up with Bella."
        scene ep12_ret23 with dissolve
        bia "You did?"
        scene ep12_ret24 with dissolve
        mc "Yep."
        scene ep12_ret25 with dissolve
        bia "That changes things for you, but for me it's still... You know?"
        scene ep12_ret26 with dissolve
        mc "I know. I haven't stopped thinking about you."
    else:
        if "Jill" in breakup:
            scene ep12_ret24 with dissolve
            mc "I am. But also, you should know that I broke up with Jill."
            scene ep12_ret23 with dissolve
            bia "Actually, I heard. But Jill never told me why."
            bia "I didn't inquire because I was scared it had something to do with me."
            scene ep12_ret24 with dissolve
            mc "No, it was about something I did in the past. We can leave it at that."
            scene ep12_ret25 with dissolve
            bia "That changes things for you, but for me it's still... You know?"
            scene ep12_ret26 with dissolve
            mc "I know. I haven't stopped thinking about you. I gotta have you."
        else:
            scene ep12_ret24 with dissolve
            mc "I haven't stopped thinking about you. I gotta have you."

    scene ep12_ret25 with dissolve
    bia "Haha... I get a kick from hearing that."
    scene ep12_ret26 with dissolve
    mc "My blood is pumping now, too. I'm thinking about everything I want to do with you."
    scene ep12_ret25 with dissolve
    bia "Mmm... Sounds hot. Tonight then."
    scene ep12_ret27 with dissolve
    mc "You can enter from my window. Wear something sexy."
    scene ep12_ret28 with dissolve
    bia "I think I have something."

label ep12_gym_label:
scene ep12_gym3 with wiperight
dwy "Sure, I'll show. How big of a party are we talking about?"
scene ep12_gym1 with dissolve
mc "The guest list isn't final, but we're around 100 guests, if not more."
scene ep12_gym3 with dissolve
dwy "Is it cool if I invite some more people?"
scene ep12_gym4 with dissolve
mc "Like who?"
scene ep12_gym3 with dissolve
dwy "I'd bring my girl, and maybe Chao wants to come too. I heard he didn't have any plans."
scene ep12_gym1 with dissolve
mc "The more the merrier. I'll give you Sage's number, and you can shoot her the details."
mc "But please do it soon. There's some planning involved with the food and such."
scene ep12_gym5 with dissolve
dwy "Is she in charge of the guest list?"
scene ep12_gym6 with dissolve
mc "Yeah."
scene ep12_gym5 with dissolve
dwy "What type of party is it?"
scene ep12_gym6 with dissolve
mc "Dinner, dancing, and drinking. There's a dress code, too."
scene ep12_gym5 with dissolve
dwy "Dress to impress and move to the groove. Gotcha. I appreciate the invite."
scene ep12_gym1 with dissolve
mc "Haha! It's going to be weird to see you without gym clothes."
scene ep12_gym7 with dissolve
dwy "Tell me about it. I wear this more than I wear casual clothes."
dwy "When clients see me outside of the gym, they get shocked."
scene ep12_gym2 with dissolve
mc "Do you dress that poorly?"
scene ep12_gym3 with dissolve
dwy "HAH! Big mouth on you. Focus more on your reps, boy."
if ep11_fighter:
    dwy "Oh, and don't forget to show up early for the competition."
    scene ep12_gym2 with dissolve
    mc "I'm aware. I'll help out."
    scene ep12_gym3 with dissolve
    dwy "Awesome."
scene ep12_gym8 with dissolve
$ renpy.pause(0.5)
scene ep12_gym9 with dissolve
$ renpy.pause(0.5)
scene ep12_gym8 with dissolve
$ renpy.pause(0.5)
scene ep12_gym9 with dissolve
$ renpy.pause(0.5)
play sound "sound_effects/clang.mp3"
scene ep12_gym10 with hpunch
if ep10_troy_mad:
    troy "Got a sec?"
    scene ep12_gym11 with dissolve
    mc "I'm between sets here."
    scene ep12_gym12 with dissolve
    troy "It won't take long."
    scene ep12_gym11 with dissolve
    mc "What is it?"
else:
    troy "Looking strong."
    scene ep12_gym14 with dissolve
    mc "Feeling strong too. I don't know what it is."
    scene ep12_gym13 with dissolve
    troy "It's most likely the rest you've gotten from the winter break."
    scene ep12_gym14 with dissolve
    mc "I have slept in more than usual. How about you?"
    scene ep12_gym13 with dissolve
    troy "I'm doing ok. I'm getting nervous about the competition, though."
    scene ep12_gym14 with dissolve
    if ep11_fighter:
        mc "I feel the same."
    else:
        mc "Good luck with that."
scene ep12_gym15 with dissolve
troy "I talked to Chad..."
scene ep12_gym16 with dissolve
mc "Yeah?"
scene ep12_gym15 with dissolve
troy "He told me that you reached out."
troy "I wanted to thank you for not spreading it further. Um... Our relationship."
scene ep12_gym16 with dissolve
mc "It wasn't any of my business."
scene ep12_gym17 with dissolve
troy "Yeah, but still. It could have done a lot of damage to Chad if you had spread it."
scene ep12_gym16 with dissolve
mc "How do you mean?"
scene ep12_gym17 with dissolve
troy "Well, it's the reason why I'm not a jock anymore."
troy "Chad has big goals in life. He doesn't want his sexuality to hold him back."
scene ep12_gym16 with dissolve
mc "The jocks kicked you out because you're gay?"
scene ep12_gym18 with dissolve
troy "It's not that simple."
troy "I lashed out at Dawe after he bullied me for it."
troy "I don't want to get into it. I'm trying to leave it all behind me."
if ep10_troy_mad:
    scene ep12_gym15 with dissolve
    troy "I know you and I aren't seeing eye to eye on much, but anyway..."
    troy "I wanted to say thanks."
    scene ep12_gym16 with dissolve
    mc "Alright."
else:
    scene ep12_gym16 with dissolve
    mc "Dawe is a dick."
    scene ep12_gym19 with dissolve
    troy "Haha! Which is funny because he lacks one."
    scene ep12_gym20 with dissolve
    mc "Hm?"
    scene ep12_gym19 with dissolve
    troy "He's got a micropenis."
    scene ep12_gym20 with dissolve
    mc "That explains a lot."
    scene ep12_gym15 with dissolve
    troy "Anyway... Thanks."
    scene ep12_gym16 with dissolve
    mc "Hey... Do you wanna come to our New Year's Eve party?"
    scene ep12_gym19 with dissolve
    troy "That would be awesome."
    scene ep12_gym20 with dissolve
    mc "Tell Dwyane you'll come. He knows how to fix an invite."
$ new_bio("Troy", "Troy thanked me for not spreading information on his and Chad's relationship further.")
stop music fadeout 3
scene ep12_gym8 with dissolve
$ renpy.pause(0.5)
scene ep12_gym9 with dissolve
$ renpy.pause(0.5)
scene ep12_gym8 with dissolve
$ renpy.pause(0.5)
scene ep12_gym9 with dissolve
$ renpy.pause(0.5)

if ep12_bianca_lewd:
    jump ep12_bianca_lewd_label
elif not breakup and branchMayaJosy and check_mlove():
    jump ep12_msolo_label
jump ep12_zbret_label

label ep12_bianca_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ branchJill = True
    $ branchIsabella = False
    $ breakup = []
$ guideSuggestedPage = 257
hide screen new_phone_screen
play music "music/ep2/jingle.mp3"
scene ep12_bianca_lewd1 with wipeleft
$ renpy.pause()
scene ep12_bianca_lewd2 with dissolve
$ renpy.pause(1)
play sound "sound_effects/season3/glass_knock.mp3"
scene ep12_bianca_lewd3 with dissolve
"*{i}Knock knock{/i}*"
play sound "sound_effects/season3/door_slide.mp3"
scene ep12_bianca_lewd4 with dissolve
mc "Come on in."
scene ep12_bianca_lewd5 with dissolve
bia "Sorry about making the floor wet."
scene ep12_bianca_lewd6 with dissolve
mc "Don't worry about it; I'll get it. Just put your shoes and clothes anywhere."
scene ep12_bianca_lewd7 with dissolve
bia "There we go... Hey."
scene ep12_bianca_lewd8 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd10 with dissolve
bia "Are you alone here?"
scene ep12_bianca_lewd9 with dissolve
mc "No. A few of the boys are back, but I've locked the door. They won't bother us."
scene ep12_bianca_lewd11 with dissolve
mc "How are you feeling?"
scene ep12_bianca_lewd12 with dissolve
bia "My heart has been racing ever since I left home."
bia "I can't believe we're doing this."
if branchJill and not "Jill" in breakup:
    scene ep12_bianca_lewd11 with dissolve
    mc "Did you change your mind?"
    scene ep12_bianca_lewd12 with dissolve
    bia "Not even once. Did you?"
    scene ep12_bianca_lewd13 with dissolve
    mc "I'm not gonna lie; I second-guessed myself several times."
    scene ep12_bianca_lewd14 with dissolve
    bia "Oh?"
    scene ep12_bianca_lewd13 with dissolve
    mc "But every time I did, the answer was the same. I want to do this."
else:
    scene ep12_bianca_lewd11 with dissolve
    mc "Did you change your mind?"
    scene ep12_bianca_lewd12 with dissolve
    bia "Not even once."
scene ep12_bianca_lewd15 with dissolve
mc "*{i}Smack{/i}*"
scene ep12_bianca_lewd16 with dissolve
mc "I haven't been able to get you out of my head."
scene ep12_bianca_lewd17 with dissolve
bia "Me neither. I've read our chat like a million times. Only wanting more and more..."
scene ep12_bianca_lewd16 with dissolve
mc "So have I."
scene ep12_bianca_lewd15 with dissolve
bia "Mmm..."
scene ep12_bianca_lewd18 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd19 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd20 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd21 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd22 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd23 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd24 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd25 with dissolve
bia "*{i}Smack{/i}*"
play sound "sound_effects/shove.mp3"
scene ep12_bianca_lewd26 with vpunch
$ renpy.pause()
scene ep12_bianca_lewd27 with dissolve
bia "Mmm..."
scene ep12_bianca_lewd28 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd29 with dissolve
bia "*{i}Moans{/i}*"
scene ep12_bianca_lewd30 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd31 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd32 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd33 with dissolve
$ renpy.pause()
scene anim_bianca_cunn1_ep12 with dissolve
bia "*{i}Gasps{/i}*"
mc "*{i}Suck lick lick{/i}*"
pause
scene anim_bianca_cunn2_ep12 with dissolve
pause
scene ep12_bianca_lewd34 with dissolve
bia "A little bit more..."
scene ep12_bianca_lewd35 with dissolve
bia "Yes... Yes! Yes! YES!!!"
scene ep12_bianca_lewd36 with hpunch
bia "*{i}Moans{/i}* I'm cumming!"
scene ep12_bianca_lewd37 with hpunch
bia "Ahh!"
scene ep12_bianca_lewd38 with hpunch
bia "*{i}Moans{/i}* Oh, [name]..."
scene ep12_bianca_lewd39 with dissolve
bia "Wow... Are you for real?"
scene ep12_bianca_lewd40 with dissolve
bia "*{i}Smack{/i}*"
scene ep12_bianca_lewd41 with dissolve
bia "I want to reciprocate."
scene ep12_bianca_lewd42 with dissolve
mc "How do you want it?"
scene ep12_bianca_lewd41 with dissolve
bia "I need that big cock in my mouth, [name]."
scene ep12_bianca_lewd43 with dissolve
mc "How about this?"
scene ep12_bianca_lewd44 with dissolve
bia "I want to suck you dry."
scene anim_bianca_bj1_ep12 with dissolve
bia "*{i}Suck suck{/i}*"
mc "Fuck... I appreciate the effort, but don't make me cum from this..."
pause
scene anim_bianca_bj2_ep12 with dissolve
bia "Mmm..."
pause
scene anim_bianca_bj3_ep12 with dissolve
pause
scene anim_bianca_bj4_ep12 with dissolve
mc "I want to fuck you hard, Bianca... You're so goddamned sexy."
pause
scene ep12_bianca_lewd45 with dissolve
bia "I'm going to do it as I wrote you..."
scene ep12_bianca_lewd46 with dissolve
bia "I'm gonna sit on you and let you penetrate me hard..."
scene ep12_bianca_lewd47 with dissolve
bia "*{i}Moans{/i}* Ah... Fuck!"
scene ep12_bianca_lewd48 with dissolve
bia "Ahhh!!! It's so big!"
scene ep12_bianca_lewd49 with dissolve
bia "Fuck!"
mc "Is it too deep?"
scene ep12_bianca_lewd50 with dissolve
bia "Yes, but it feels so unbelievably good."
scene anim_bianca_ride1_ep12 with dissolve
bia "Mmm... Fuck... Yes! Oh, [name]... Yes!"
pause
scene anim_bianca_ride2_ep12 with dissolve
mc "You feel so damn good, Bianca."
bia "We're so bad... Aren't we?"
mc "Yeah... You're such a hot slut..."
pause
scene anim_bianca_ride3_ep12 with dissolve
bia "Mmm... I'm a slut now? Haha... No one has ever called me that before."
mc "Was it too much?"
bia "No... I kinda liked it. Call me a slut again."
mc "You're so slutty, Bianca. I'm gonna fuck you in a way you deserve."
bia "*{i}Moans{/i}* Yes!"
pause
$ tmpInt = 0
label ep12_bianca_lewd_loop_label:
menu:
    "Blowjob":
        $ tmpInt += 1
        scene anim_bianca_bj1_ep12 with dissolve
        bia "*{i}Suck suck glug glug{/i}*"
        pause
        scene anim_bianca_bj2_ep12 with dissolve
        mc "Suck my cock, you slut. Take it all."
        pause
        scene anim_bianca_bj3_ep12 with dissolve
        bia "Mmmpfff... Mmm..."
        pause
        scene anim_bianca_bj4_ep12 with dissolve
        pause
        jump ep12_bianca_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_bianca_ride1_ep12 with dissolve
        mc "Ride me... Ride me hard."
        pause
        scene anim_bianca_ride2_ep12 with dissolve
        bia "I want your cock, [name]. I fucking crave it!"
        mc "Take it... It's yours."
        pause
        scene anim_bianca_ride3_ep12 with dissolve
        pause
        jump ep12_bianca_lewd_loop_label
    "Piledriver":
        $ tmpInt += 1
        scene anim_bianca_pile1_ep12 with dissolve
        mc "Fuck... Those eyes..."
        bia "Hm?"
        mc "Those sexy bedroom eyes could make me cum right now."
        bia "Cum if you're close, [name]."
        pause
        scene anim_bianca_pile2_ep12 with dissolve
        mc "Fuck no. I'm not done with you yet."
        pause
        scene anim_bianca_pile3_ep12 with dissolve
        mc "I'm gonna fuck you as much as I've fucked you in my fantasies."
        bia "*{i}Moans{/i}* If I did that, we would be here all night if not longer."
        pause
        scene anim_bianca_pile4_ep12 with dissolve
        mc "Your pussy feels so good."
        pause
        jump ep12_bianca_lewd_loop_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_bianca_doggy1_ep12 with dissolve
        bia "*{i}Moans{/i}* Yes... Give it to me, [name]. Fuck your slut."
        pause
        scene anim_bianca_doggy2_ep12 with dissolve
        mc "Fuck!!! You sure know how to do doggy. I'm getting harder with each thrust."
        pause
        scene anim_bianca_doggy3_ep12 with dissolve
        bia "*{i}Moans{/i}* Fuck me, [name]. Fuck me!"
        pause
        jump ep12_bianca_lewd_loop_label
    "Missionary":
        $ tmpInt += 1
        scene anim_bianca_miss1_ep12 with dissolve
        pause
        scene anim_bianca_miss2_ep12 with dissolve
        pause
        scene anim_bianca_miss3_ep12 with dissolve
        pause
        jump ep12_bianca_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_bianca_rev1_ep12 with dissolve
        bia "Ahh!!! Ah!!! Yes! Keep going!"
        mc "Take it, you little slut."
        pause
        scene anim_bianca_rev2_ep12 with dissolve
        bia "*{i}Moans and whimpers{/i}*"
        pause
        jump ep12_bianca_lewd_loop_label
    "Cum" if tmpInt > 2:
        mc "I'm gonna cum..."
        menu:
            "Creampie":
                scene anim_bianca_pile2_ep12 with dissolve
                mc "I'm gonna fill you the fuck up."
                bia "Yes! Give it to me! Give it!"
                pause
                scene anim_bianca_pile5_ep12 with hpunch
                mc "Fuck!"
                bia "*{i}Moans{/i}* Ahh!!! I'm cumming!!!"
                pause
                scene ep12_bianca_lewd51 with dissolve
                bia "Fuck, [name]... You made me cum again!"
            "Facial":
                scene anim_bianca_cum_ep12 with dissolve
                bia "*{i}Suck suck{/i}*"
                mc "I'm gonna shoot it all over your slutty face."
                bia "{i}Suck suck{/i} Yes! Give it to me! Give it!"
                pause
                scene ep12_bianca_lewd54 at hpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_bianca_lewd54 at hpunch, cum3
                $ renpy.pause(0.5)
                scene ep12_bianca_lewd54 at hpunch, cum3
                mc "Fuck!"
                scene ep12_bianca_lewd55 with dissolve
                mc "Damn... That's so hot."
            "On ass":
                scene anim_bianca_doggy3_ep12 with dissolve
                mc "I'm gonna shoot it all over your slutty ass."
                bia "Yes! Give it to me! Give it!"
                pause
                scene ep12_bianca_lewd52 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bianca_lewd52 at hpunch, cum2
                $ renpy.pause(0.5)
                scene ep12_bianca_lewd52 at hpunch, cum2
                mc "Fuck!"
                scene ep12_bianca_lewd53 with dissolve
                $ renpy.pause()

scene ep12_bianca_lewd56 with dissolve
bia "Mmm..."
mc "Fuck... Bianca..."
scene ep12_bianca_lewd58 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd57 with dissolve
$ renpy.pause()
scene ep12_bianca_lewd59 with dissolve
bia "I haven't orgasmed like that ever."
scene ep12_bianca_lewd60 with dissolve
mc "Mine was so intense too."
scene ep12_bianca_lewd59 with dissolve
bia "Damn, your smoldering look is so sexy. It makes me want to go for a second round."
scene ep12_bianca_lewd60 with dissolve
mc "Stay for longer, and we'll do it."
scene ep12_bianca_lewd59 with dissolve
bia "I can stay here all night."
scene ep12_bianca_lewd61 with dissolve
bia "*{i}Smack{/i}*"
scene ep12_bianca_lewd62 with dissolve
mc "{i}And that she did.{/i}"
mc "{i}We fucked four times that night. We were exhausted, but after each time we finished...we were still horny for each other.{/i}"
if branchIsabella or "Jill" in breakup:
    if "Jill" in breakup:
        mc "{i}Even though Jill and I had broken up, it felt like it was wrong to have sex with Bianca.{/i}"
        scene ep12_bianca_lewd63 with dissolve
        mc "{i}Probably because we initiated it back when I was with Jill...{/i}"
    else:
        mc "{i}Even though Bella and I had broken up, it felt like it was wrong to have sex with Bianca.{/i}"
        scene ep12_bianca_lewd63 with dissolve
        mc "{i}Probably because we initiated it back when I was with Bella...{/i}"
    mc "{i}But weirdly, it also felt right.{/i}"
    scene ep12_bianca_lewd64 with dissolve
    stop music fadeout 3
    mc "{i}I chose to focus on that feeling.{/i}"
else:
    mc "{i}We took that step together. We both did something wrong. But how can something wrong feel so right?{/i}"
    scene ep12_bianca_lewd63 with dissolve
    mc "{i}I remember thinking about what Josy said to me during our first date.{/i}"
    mc "{i}About how cheating can be ok if you end up with someone who makes you happy.{/i}"
    scene ep12_bianca_lewd64 with dissolve
    mc "{i}Having done that to Jill with Bianca...{/i}"
    stop music fadeout 3
    mc "{i}Josy's way of looking at it seemed true at that moment.{/i}"
$ renpy.end_replay()
$ persistent.ep12_lewd_bianca = True
$ calcScenes()
$ mphone_stats_add_girl_s3("bianca","You had sex with Bianca in your room in episode 12.")
$ new_bio("Bianca", "We did it. We went all the way. It felt wrong, but also right.")
if branchJill and not "Jill" in breakup:
    $ new_bio("Jill", "I cheated on Jill with Bianca.")
if not breakup and branchMayaJosy and check_mlove():
    jump ep12_msolo_label
jump ep12_zbret_label

label ep12_zbret_label:
play music "music/ep_interlude/licensed_music/track108.mp3"
hide screen new_phone_screen
if branchZoey:
    scene ep12_zbret1 with wipeleft
    bre "No way."
    scene ep12_zbret2 with dissolve
    zo "Skeptical, much? Believe it or not, but he loves me back."
    scene ep12_zbret1 with dissolve
    bre "Of course, he loves you back. Who wouldn't? I'm stunned that he said it, that's all."
    scene ep12_zbret3 with dissolve
    zo "He told me how he felt, and also some not-so-nice things to hear."
    zo "He wanted me to know about what he's been up to and make sure that I was ok with it."
    scene ep12_zbret4 with dissolve
    bre "Like what?"
    scene ep12_zbret3 with dissolve
    zo "That's between him and me."
    scene ep12_zbret4 with dissolve
    bre "Was he trying to scare you away or...?"
    scene ep12_zbret6 with dissolve
    zo "I think it's the opposite. He was honest because he didn't want those things to become an issue for us down the road."
    scene ep12_zbret5 with dissolve
    bre "Whoa. Sounds like he did some bad things."
    scene ep12_zbret6 with dissolve
    if ep12_zworries > 0:
        zo "I'm still not telling you... But yeah... Some of it was hard to swallow, but I don't care. I know who he is deep down inside."
    else:
        zo "It wasn't anything that bad."
    zo "Everyone makes mistakes, yeah?"
    scene ep12_zbret5 with dissolve
    bre "I'm perfect."
    scene ep12_zbret7 with dissolve
    zo "Haha! The hell you ain't!"
    scene ep12_zbret8 with dissolve
    bre "You got me. I've been young and stupid too."
    if breakup:
        scene ep12_zbret9 with dissolve
        if branchMayaJosy:
            zo "Can you believe that he broke up with his girlfriends for me?"
            scene ep12_zbret10 with dissolve
            bre "Girlfriend{b}s{/b}!? Who is this guy?"
            scene ep12_zbret9 with dissolve
            zo "I don't know what kind of a relationship that was."
            zo "I haven't asked him questions about it because I didn't want to know."
            scene ep12_zbret10 with dissolve
            bre "Is that gonna be a problem?"
        else:
            if ep4_toldDerekAboutJade:
                zo "Can you believe that he got dumped by his girlfriend and that it wasn't my fault?"
                scene ep12_zbret10 with dissolve
                bre "Hm... Sounds odd. But hey, if she's gone, she's gone. Or is it gonna be a problem?"
            else:
                zo "Can you believe that he broke up with his girlfriend for me?"
                scene ep12_zbret10 with dissolve
                bre "That sucks for her, but it had to happen. Is that gonna be a problem?"
        scene ep12_zbret9 with dissolve
        zo "Who knows?"
        scene ep12_zbret10 with dissolve
        if branchMayaJosy:
            bre "I can't imagine them being happy with you. Be careful."
        else:
            if ep4_toldDerekAboutJade:
                bre "Still, I can't imagine her being happy with you. Be careful."
            else:
                bre "I can't imagine her being happy with you. Be careful."
        if not zoey_dik:
            scene ep12_zbret11 with dissolve
            if branchMayaJosy:
                zo "I'm not going to start something with them. It blows that I had to get between them and [name], but I'd do it again no matter what."
            else:
                zo "I'm not going to start something. It blows that I had to get between her and [name], but I'd do it again no matter what."
                if ep4_toldDerekAboutJade:
                    zo "Not like that mattered anyway, since he got dumped."
        else:
            scene ep12_zbret7 with dissolve
            if branchMayaJosy:
                zo "Hey. They are the ones who should watch out, not me."
            else:
                zo "Hey. She's the one who should watch out, not me."
            scene ep12_zbret8 with dissolve
            bre "Haha! Good one."
            scene ep12_zbret11 with dissolve
            if branchMayaJosy:
                zo "It blows that I had to get between them and [name], but I'd do it again no matter what."
            else:
                zo "It blows that I had to get between her and [name], but I'd do it again no matter what."
    scene ep12_zbret5 with dissolve
    bre "It sounds like all the pieces are falling into place for you. That makes me happy."
    scene ep12_zbret11 with dissolve
    zo "Don't say that yet. I'm still on that waiting list."
    scene ep12_zbret12 with dissolve
    bre "You'll get in."
    scene ep12_zbret13 with dissolve
    zo "What if I don't?"
    zo "I'm not gonna be as close to [name] as I want if I have to stay here."
    scene ep12_zbret11 with dissolve
    zo "I know he can't commute to see me every day. And if I need to work, I won't be able to do that daily either."
    scene ep12_zbret12 with dissolve
    bre "Who says you have to see each other daily? You're feeling like this now because your relationship is fresh."
    scene ep12_zbret13 with dissolve
    zo "Well, I wanna see him every day. Sue me."
    scene ep12_zbret12 with dissolve
    bre "Have some faith. You'll get in. Don't make other plans until you know for sure."
    stop music fadeout 3
    scene ep12_zbret14 with dissolve
    zo "Can it be January already? I hate December."
else:
    scene ep12_zbret15 with wipeleft
    zo "And now he expects me to figure out if we could remain friends."
    scene ep12_zbret5 with dissolve
    bre "But he doesn't know if he wants it?"
    scene ep12_zbret15 with dissolve
    zo "Yeah. Basically, he thinks we'll manage being on the same campus, but we need to decide whether we can still hang out."
    scene ep12_zbret5 with dissolve
    bre "Isn't that what you've been doing since you returned? How's that an issue for him now?"
    scene ep12_zbret16 with dissolve
    if branchSage and not breakup:
        zo "It could have something to do with his girlfriend. He mentioned she didn't like that he hung out with me or something like that."
        scene ep12_zbret17 with dissolve
        bre "Aha. That makes sense. Some girlfriends get jealous of the slightest thing."
        scene ep12_zbret16 with dissolve
        zo "I told her boyfriend that I loved him... I don't care about her, but in her defense, I think her jealousy is justified."
    elif branchMayaJosy and not breakup:
        zo "It could have something to do with his girlfriends. They weren't too happy about me hanging out with him."
        scene ep12_zbret17 with dissolve
        bre "Girlfriend{b}s{/b}!? Who is this guy?"
        scene ep12_zbret16 with dissolve
        zo "I don't know what kind of a relationship that is. I haven't asked him questions about it because I didn't want to know."
    else:
        zo "I think everything changed when I told him I loved him. It's as if he's looking for a reason to get away from all of that."
        zo "Maybe he doesn't want to be reminded of me daily. Maybe he still has some regrets."
        if not breakup and (branchIsabella or branchJill):
            zo "Also, he's in some relationship now, too. That could be it."
    scene ep12_zbret17 with dissolve
    bre "If you ask me, the answer is simple."
    bre "I know you love him and all, but when push comes to shove, he sounds like a wishy-washy tool."
    scene ep12_zbret5 with dissolve
    bre "He wants your friendship when you return, but now he has issues with it because you told him you love him."
    bre "And he comes to your home at Christmas to talk about it, but he doesn't have much to say."
    scene ep12_zbret18 with dissolve
    bre "He doesn't even know what he wants for himself. Is he expecting you to solve everything for him?"
    bre "Is he waiting for you to make a choice and to go along with it, or is he trying to string you along?"
    bre "What do you make of a guy like this?"
    scene ep12_zbret19 with dissolve
    zo "I think he's conflicted because of our past."
    zo "If we hadn't grown up together, he wouldn't even have considered a friendship now."
    scene ep12_zbret18 with dissolve
    bre "How do you know?"
    scene ep12_zbret19 with dissolve
    zo "Because that's how I feel about it."
    zo "What normal person wants to be around someone they got rejected by unless there's a strong bond between them?"
    scene ep12_zbret20 with dissolve
    zo "It's a self-destructive behavior."
    scene ep12_zbret18 with dissolve
    bre "And the bond makes the difference, huh?"
    scene ep12_zbret20 with dissolve
    zo "That's what I'm trying to decide."
    zo "I mean... Look at you and Emma."
    scene ep12_zbret5 with dissolve
    bre "Listen... I don't want you to do something stupid."
    bre "Whatever the choice you make.... Be selfish about this."
    stop music fadeout 3
    scene ep12_zbret21 with dissolve
    $ renpy.pause()

if ep11_fighter:
    jump ep12_fcomp_label
elif ep11_music:
    jump ep12_fparty_label
else:
    jump ep12_no_fparty_label

label ep12_fcomp_label:
$ guideSuggestedPage = 257
play music "music/ep_interlude/licensed_music/track105.mp3"
play sound "sound_effects/season2/punching_bag_punch.mp3"
$ renpy.play("sound_effects/season3/audience_gasp.mp3", "sfx2")
show screen new_phone_screen
scene ep12_fcomp1 with hpunch
aud "*{i}Gasps{/i}*"
play sound "sound_effects/bell.mp3"
scene ep12_fcomp2 with dissolve
play sound "sound_effects/season3/dj/dj_audience1.mp3"
ann "And that's it! The ref called it! Chao wins on TKO!"
scene ep12_fcomp3 with dissolve
aud "*{i}Cheers{/i}*"
scene ep12_fcomp4 with dissolve
$ renpy.pause()
scene ep12_fcomp5 with dissolve
mc "You can do this. You can do this..."
scene ep12_fcomp6 with dissolve
tate "Hey, [name]! You missed it!"
scene ep12_fcomp7 with dissolve
mc "I missed my fight!?"
scene ep12_fcomp8 with dissolve
tate "What? No! Chao won on TKO!"
tate "He sure showed the City Fighters who they're up against. We're one up!"
scene ep12_fcomp12 with dissolve
mc "That's awesome. Great!"
scene ep12_fcomp8 with dissolve
tate "How are you doing? You look pale."
scene ep12_fcomp12 with dissolve
mc "I think it's the nerves. I've never fought in front of an audience before. You know, with a referee, an announcer and all."
mc "I didn't think this competition would be at this level. I thought it was something...a bit less of everything, you know?"
scene ep12_fcomp9 with dissolve
tate "I whimped out during my first fight, too."
tate "Don't pay too much attention to the people around you. The announcer is there to make things more fun for the audience."
tate "And you gotta have a referee, don't you?"
scene ep12_fcomp10 with dissolve
mc "I know. It just hit me now how much I want this. Like... I want to give it my all."
scene ep12_fcomp9 with dissolve
tate "That's the spirit! Hold on to that!"
scene ep12_fcomp10 with dissolve
mc "But what if I'm not good enough?"
scene ep12_fcomp11 with dissolve
tate "And the spirit is gone..."
tate "Everyone doubts themselves at some point. And those who say they don't, they're lying."
scene ep12_fcomp9 with dissolve
tate "Win or lose, it doesn't matter today. You can still give it your all."
play sound "sound_effects/season2/puke.mp3"
scene ep12_fcomp13 with dissolve
mc "*{i}Pukes{/i}*"
tate "Bro..."
scene ep12_fcomp14 with dissolve
mc "I'll make it."
scene ep12_fcomp15 with dissolve
dwy "[name]. You're up. Wrapped up and ready?"
scene ep12_fcomp16 with dissolve
mc "Yeah... I'm ready."
scene ep12_fcomp15 with dissolve
dwy "I need to talk to you. Walk with me."

scene ep12_fcomp17 with dissolve
dwy "You're gonna do great today. Keep your mind on your goal."
scene ep12_fcomp18 with dissolve
mc "My goal, yeah..."
if brawler_attitude > 0:
    mc "Knock the fucker out."
    scene ep12_fcomp17 with dissolve
    dwy "That's the attitude. But you know... Be respectful too."
else:
    mc "Do my best, keep it clean, and try to win."
    scene ep12_fcomp17 with dissolve
    dwy "Sound goods. You could do with more attitude, though."
dwy "Rumor has it, there's a scout in the audience."
scene ep12_fcomp19 with dissolve
mc "A scout?"
scene ep12_fcomp20 with dissolve
dwy "Yeah. Someone is keeping an eye out for promising talent."
dwy "I don't know who he is or who he works for, but scouts mean sponsors and sponsors mean money."
dwy "Aim to impress."
play sound "sound_effects/season3/dj/dj_audience2.mp3"
if not ep10_troy_mad:
    scene ep12_fcomp21 with dissolve
    troy "[name], you got this. We're rooting for you."
else:
    scene ep12_fcomp22 with dissolve
    chao "Let's go, [name]!"
scene ep12_fcomp23 with dissolve
mc "This is a bigger audience than I expected."
scene ep12_fcomp24 with dissolve
dwy "I know, I know. Zone that shit out. They don't matter during your fight."
dwy "They're just noise, trying to distract you."
scene ep12_fcomp25 with dissolve
dwy "I have vetted your opponent. He's undefeated with 7-0. He likes to keep it technical and wait for clean shots."
dwy "He's not a risk-taker, and his fists are what you need to look out for."
scene ep12_fcomp26 with dissolve
mc "What about his leg game?"
scene ep12_fcomp25 with dissolve
dwy "He'll likely throw in a low kick here and there to wear you out and open you up."
dwy "Don't fall for it. Keep your guard up until you're within range, and then unleash multiple attacks when you commit."
dwy "Chain your moves together. Overwhelm his defense, and you'll have the upper hand."
stop music fadeout 3
scene ep12_fcomp27 with dissolve
dwy "Trust your instincts. I'm in your corner."
play music "music/ep12/licensed_music/track205.mp3"
scene ep12_fcomp28 with dissolve
ann "In the blue corner: he's a 6'1\" fighter, weighing in at 182 pounds. He's a first-time fighter, fighting for the Burgmeister & Royce campus gym."
scene ep12_fcomp29 with dissolve
play sound "sound_effects/season3/dj/dj_audience3.mp3"
ann "Give it up for... [name] [lname]!"
aud "*{i}Cheers{/i}*"
if not breakup and (branchMayaJosy or (branchSage and (ep11_sage_love == 2 or RPsage >= 22))):
    scene ep12_fcomp38 with dissolve
    js "Yes! Go [name]!!!"
    my "WOOO!!!"
    sa "WHOOP! WHOOP!"
elif branchZoey:
    scene ep12_fcomp39 with dissolve
    zo "*{i}Cheers{/i}* [name]!!!"
elif not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
    scene ep12_fcomp40 with dissolve
    nic "Let's go!!! [name]!!!"
scene ep12_fcomp41 with dissolve
$ renpy.pause()
scene ep12_fcomp30 with dissolve
$ renpy.pause()
scene ep12_fcomp28 with dissolve
ann "In the red corner: he's a 5'10\" fighter, weighing in at 183 pounds. He stands at 7 wins and 0 losses, fighting for the City Fighters gym."
scene ep12_fcomp31 with dissolve
play sound "sound_effects/season3/dj/dj_audience1.mp3"
if name == "Johnny" and lname == "Stevens":
    ann "Give it up for - well, I'll be damned - Johnny Stevens!"
else:
    ann "Give it up for Johnny Stevens!"
scene ep12_fcomp32 with dissolve
aud "*{i}Cheers{/i}*"
aud "GO, JOHNNY!!!"
scene ep12_fcomp30 with dissolve
mc "(I can take this guy.)"
scene ep12_fcomp33 with dissolve
ref "Ok, guys. I want to see a clean fight. Follow my instructions at all times."
ref "Touch gloves if you want. Let's do this."
scene ep12_fcomp34 with dissolve
$ renpy.pause()
if brawler_attitude > 0:
    scene ep12_fcomp36 with dissolve
    ann "Touching gloves is a sign of respect for the sport and your opponent, but [name] doesn't want to do it."
    ann "Maybe he's trying to get into his opponent's head."
else:
    scene ep12_fcomp35 with dissolve
    ann "And the fighters touch gloves and make their way back to their corners for the fight."
scene ep12_fcomp37 with dissolve
ref "FIGHT!"
ann "And the fight is on!"

$ renpy.block_rollback()
$ _game_menu_screen = None
hide screen new_phone_screen
$ phone_opened = True
$ renpy.pause(0.5)
$ renpy.block_rollback()
if minigames:
    $ bn_history_list.append(1)
    $ bn_story_fight = True
    $ bn_story_fight_round = 1
    $ bn_init_opponents()

    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Johnny":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_johnny_fight_nomg_label

label ep12_fcomp_round1_end_label:
$ phone_opened = False
hide screen brawler_menu_screen
hide screen brawler_result_screen
$ _game_menu_screen = "save"
if bn_mc_won:
    $ ep12_brawler_round_win = 1
    play sound "sound_effects/season3/kick_slap.mp3"
    scene ep12_fcomp42 with hpunch
    ann "[name] with a heel kick!"
    ann "It connects!"
    scene ep12_fcomp45 with dissolve
    ann "That has got to rattle his opponent."
else:
    play sound "sound_effects/whoosh.mp3"
    scene ep12_fcomp43 with hpunch
    ann "[name] with a heel kick!"
    ann "He dodged that one."
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp44 with hpunch
    ann "And he counters with a clean shot to the head."
play sound "sound_effects/season3/kick_body.mp3"
scene ep12_fcomp46 with hpunch
ann "Whoa! A hard kick to the body. Johnny is switching things up late in the first."
play sound "sound_effects/bell.mp3"
scene ep12_fcomp47 with dissolve
play sound "sound_effects/season3/dj/dj_audience2.mp3"
"*{i}Bell rings{/i}*"
ann "And there's the bell. Fighters go back to their corners."
scene ep12_fcomp48 with dissolve
aud "*{i}Cheers{/i}*"
dwy "Sit down."
if ep12_brawler_round_win == 1:
    scene ep12_fcomp49 with dissolve
    dwy "You're doing amazing. Don't let that leg kick bother you."
    dwy "He'll try to surprise you in the second round too. It's all that he's got."
    scene ep12_fcomp50 with dissolve
    dwy "Keep at it. Don't let him stay out of your reach; push forward when he retreats."
    dwy "You're tiring him out. Be relentless when you choose to assault."
    scene ep12_fcomp51 with dissolve
    $ renpy.pause()
    scene ep12_fcomp52 with dissolve
    dwy "I love the focus, [name]. Come on, second round. Put him to sleep."
else:
    scene ep12_fcomp53 with dissolve
    dwy "Breathe, [name]. Breathe."
    scene ep12_fcomp54 with dissolve
    mc "He can read my every move."
    scene ep12_fcomp50 with dissolve
    dwy "It's because you're hesitating. Don't televise your punches or fake him out with one."
    dwy "You have to keep him guessing, or you won't connect."
    scene ep12_fcomp55 with dissolve
    dwy "He's just as tired as you are. He'll be slower in the second round."
    dwy "You lost the first round. You have to bring it all in the second."
    scene ep12_fcomp52 with dissolve
    dwy "You've got this, [name]. I know you can do it."
    dwy "Show him who's boss."
dwy "If there's one time to show all your power, it's now."
play sound "sound_effects/season3/dj/dj_audience1.mp3"
scene ep12_fcomp56 with dissolve
ann "And the second round is on!"

$ renpy.block_rollback()
$ _game_menu_screen = None
hide screen new_phone_screen
$ phone_opened = True
$ renpy.pause(0.5)
$ renpy.block_rollback()
if minigames:
    $ bn_history_list[5] = 2
    $ bn_story_fight_round = 2
    $ bn_init_opponents()

    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Johnny":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_johnny_fight2_nomg_label

label ep12_fcomp_round2_end_label:
$ phone_opened = False
hide screen brawler_menu_screen
hide screen brawler_result_screen
$ _game_menu_screen = "save"
if bn_mc_won:
    play sound "sound_effects/season3/dj/dj_audience3.mp3"
    $ ep12_brawler_round_win += 1
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp57 with hpunch
    ann "[name] is going hard on his opponent! He's not letting him breathe!"
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp58 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp59 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season3/kick_slap2.mp3"
    scene ep12_fcomp60 with hpunch
    $ renpy.pause()
    play sound "sound_effects/bell.mp3"
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    scene ep12_fcomp61 with dissolve
    "*{i}Bell rings{/i}*"
    ann "Talk about being saved by the bell! It's not looking good for Johnny."
else:
    play sound "sound_effects/season3/dj/dj_audience3.mp3"
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp62 with hpunch
    ann "Uh-oh! [name] is having a hard time blocking Johnny's punches."
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp63 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp64 with hpunch
    $ renpy.pause()
    play sound "sound_effects/bell.mp3"
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    scene ep12_fcomp65 with dissolve
    "*{i}Bell rings{/i}*"
    ann "Talk about being saved by the bell! The blue corner needed that break."

scene ep12_fcomp66 with dissolve
if ep12_brawler_round_win == 2:
    ann "We're going to a third round. And I don't know what you guys in the audience think, but to me, this looks like the blue corner is 2-0 for rounds."
elif ep12_brawler_round_win == 1:
    ann "We're going to a third round. And I don't know what you guys in the audience think, but to me, this looks like they have won one round each."
else:
    ann "We're going to a third round. And I don't know what you guys in the audience think, but to me, this looks like the red corner is 2-0 for rounds."
ann "It all will be decided in the third and final round."

scene ep12_fcomp67 with dissolve
if ep12_brawler_round_win == 2:
    dwy "You're ahead, but he's not out of this one yet."
    dwy "He will go for the knockout in the third. A knockout or TKO is the only way he can win."
    scene ep12_fcomp68 with dissolve
    dwy "Don't give him that chance. Finish him! This is your fight, [name]."
elif ep12_brawler_round_win == 1:
    if bn_mc_won:
        dwy "Good! You won that round, and you've built the momentum. It's time to finish him in the third."
    else:
        dwy "[name], listen to me. He won that round. I need you to bring back the energy from the first round, ok?"
    dwy "He'll try to stay technical in the third to lock in the win. Don't give him that chance!"
    scene ep12_fcomp68 with dissolve
    dwy "Dial up the intensity and finish this fight in the best way you can. Give it all! This is the final round."
else:
    dwy "[name], listen to me. You have to knock him out!"
    dwy "You can't play the third round safely."
    scene ep12_fcomp68 with dissolve
    dwy "Remember everything we've practiced. Dial the intensity up even more."
    dwy "Go all out in this one, or you'll lose. Do you understand?"

play sound "sound_effects/season3/dj/dj_audience2.mp3"
if not breakup and (branchMayaJosy or (branchSage and (ep11_sage_love == 2 or RPsage >= 22))):
    scene ep12_fcomp69 with dissolve
    my "I'm so nervous. My chest is pounding."
    scene ep12_fcomp70 with dissolve
    js "I didn't think I'd enjoy watching him fight, but all I want to see right now is him winning."
    scene ep12_fcomp71 with dissolve
    if ep12_brawler_round_win > 0:
        sa "He's winning, right?"
        scene ep12_fcomp70 with dissolve
        js "Don't jinx it."
    else:
        sa "It's not looking good, is it?"
        scene ep12_fcomp70 with dissolve
        js "Don't say that. He can still win... I think."
if branchZoey:
    scene ep12_fcomp72 with dissolve
    zo "[name]! [name]! [name]!"
    aud "[name]! [name]! [name]!"
    scene ep12_fcomp66 with dissolve
    ann "The audience is now chanting for [name]."
    if name == "Johnny":
        ann "But it's hard to tell which corner they are rooting for."
if not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
    scene ep12_fcomp73 with dissolve
    nic "Come on, [name]!!!"

stop music fadeout 3
scene ep12_fcomp74 with dissolve
aud "Get him!!!"
play sound "sound_effects/whoosh_2.mp3"
scene ep12_fcomp233 with dissolve
kid "Get him!!!"
play sound "sound_effects/season2/punching_bag_punch.mp3"
scene ep12_fcomp234 with hpunch
kid "Haha! [name] doesn't have a mother! [name] doesn't have a mother!"
play sound "sound_effects/whoosh_2.mp3"
scene ep12_fcomp75
$ renpy.pause()
play music "music/ep_interlude/licensed_music/track95.mp3"
play sound "sound_effects/season3/dj/dj_audience1.mp3"
scene ep12_fcomp76 with dissolve
ann "The third and final round! Here we go!"

$ renpy.block_rollback()
$ _game_menu_screen = None
hide screen new_phone_screen
$ phone_opened = True
$ renpy.pause(0.5)
$ renpy.block_rollback()
if minigames:
    $ bn_history_list[5] = 3
    $ bn_story_fight_round = 3
    $ bn_init_opponents()

    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Johnny":
                bn_init_fight(i)
    pause
else:
    jump brawler_story_johnny_fight3_nomg_label

label ep12_fcomp_round3_end_label:
$ phone_opened = False
hide screen brawler_menu_screen
hide screen brawler_result_screen
$ _game_menu_screen = "save"
$ bn_story_fight = False

if bn_mc_won:
    $ ep12_brawler_round_win += 1
    $ ep12_brawler_comp_won = True
    $ renpy.play("sound_effects/season3/dj/dj_audience2.mp3", "sfx3")
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp77 with hpunch
    ann "Look at that! [name] is on the prowl, and he has found his prey!"
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp78 with hpunch
    ann "Johnny is absorbing hit after hit."
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp79 with hpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp80 with hpunch
    $ renpy.pause()
    scene ep12_fcomp81 with dissolve
    mc "(Look low...)"
    scene ep12_fcomp82 with dissolve
    mc "(...aim high.)"
    scene bg anim_ko_ep12 movie with dissolve
    $ renpy.play("sound_effects/season3/audience_gasp.mp3", "sfx2")
    ann "WOW!"
    aud "*{i}Gasps{/i}*"
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    if brawler_attitude > 0:
        play sound "sound_effects/shove.mp3"
        scene ep12_fcomp83 with vpunch
        mc "AAARGH!!!"
        ann "That kick put him to sleep, and the ref has to get in there to stop the fight!"
        scene ep12_fcomp84 with dissolve
        ann "The ref has called it! [name] wins!"
    else:
        scene ep12_fcomp86 with dissolve
        ann "Even his opponent knows he's had enough."
        scene ep12_fcomp85 with dissolve
        ann "The ref is calling it! [name] wins!"
    if minigames:
        if steamAchievements and not config.console and not config.developer:
            $ achievement.grant("IDS3_34")
            init:
                $ achievement.register("IDS3_34")
            $ achievement.Sync()

    scene ep12_fcomp87 with dissolve
    mc "*{i}Screams{/i}*"
    if not breakup and (branchMayaJosy or (branchSage and (ep11_sage_love == 2 or RPsage >= 22))):
        scene ep12_fcomp88 with dissolve
        my "Yes!!!"
        js "He did it!"
        sa "YES!!! Go [name]!!!"
    elif branchZoey:
        scene ep12_fcomp88a with dissolve
        zo "YES!!! [name]!!!"
    elif not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
        scene ep12_fcomp88b with dissolve
        nic "WOHO!!! YES!!!"
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    scene ep12_fcomp89 with dissolve
    aud "*{i}Cheers{/i}*"
    ann "There was an audible silence when [name] landed that finishing blow. And what a remarkable finish at that!"
    ann "[name] showcased his talents in this one."
    scene ep12_fcomp90 with dissolve
    dwy "Yes! You fucking did it!"
    ann "[name] strung together techniques in a flawless way."
    scene ep12_fcomp91 with dissolve
    ann "The referee has put a stop to this fight in the third round. Declaring the winner by knockout..."
    scene ep12_fcomp92 with dissolve
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    play sound "sound_effects/season3/audience_cheer.mp3"
    ann "[name] [lname]!"
    aud "*{i}Cheers{/i}*"
    if not persistent.ep12_cardisa15:
        $ persistent.ep12_cardisa15 = True
        $ persistent.rew_isa_unlocked += 1
        $ persistent.chat_new_rewards = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
    scene ep12_fcomp93 with dissolve
    $ renpy.pause()
    stop music fadeout 3
    scene ep12_fcomp28 with dissolve
    ann "The next fight will start in 15 minutes."
    show screen new_phone_screen
    play music "music/ep_interlude/licensed_music/track94.mp3"
    scene ep12_fcomp94 with dissolve
    mc "I won, Dwyane. I won!"
    play sound "sound_effects/season2/fistbump.mp3"
    scene ep12_fcomp95 with hpunch
    dwy "Dude, you didn't just win. You fucking made a statement to all those City Fighters today."
    dwy "Enjoy the moment, [name]. Not everyone wins their first real fight."
    scene ep12_fcomp94 with dissolve
    mc "Thanks. I'm so excited!"

    if not breakup and branchMayaJosy:
        scene ep12_fcomp96 with dissolve
        js "[name]! You won!"
        mc "Haha! I did!"
        my "You were amazing!"
        scene ep12_fcomp97 with dissolve
        mc "Thank you so much for coming here to watch me fight."
        scene ep12_fcomp98 with dissolve
        sa "It was fun! How does it feel?"
        scene ep12_fcomp97 with dissolve
        mc "Oh, wow. Where do I even start? The adrenaline high was crazy!"
        mc "The moment the fight started, I got tunnel vision."
        scene ep12_fcomp99 with dissolve
        mc "All I could see and think about was him in front of me and how I could beat him."
        scene ep12_fcomp97 with dissolve
        mc "When he landed the first hits, I knew he was the real deal and that I had to focus."
        mc "I'm disappointed it took me three rounds to beat him, but I think I would have been disappointed if the fight had ended early, too."
        scene ep12_fcomp99 with dissolve
        mc "I didn't want the fight to end, but I wanted to win!"
        scene ep12_fcomp100 with dissolve
        js "It sounds like you enjoyed it a lot."
        scene ep12_fcomp99 with dissolve
        mc "Oh, I did. Wow... If I had known how this felt earlier, I would have started fighting years ago."
        scene ep12_fcomp100 with dissolve
        js "Do you mind if I post your picture on my blog? I wanna write about this and show it to my followers."
        scene ep12_fcomp102 with dissolve
        my "Is it a \"Men's fashion in the fight club\" weekly section?"
        scene ep12_fcomp103 with dissolve
        js "Are you making fun of it?"
        scene ep12_fcomp102 with dissolve
        my "It was a joke. But it didn't land as well as [name]'s punches."
        scene ep12_fcomp99 with dissolve
        mc "Yeah, you can write about it if you want. I don't mind."
        if not (not breakup and branchSage and (ep11_sage_love == 2 or RPsage >= 22)):
            scene ep12_fcomp101 with dissolve
            sa "I have to leave now. What about you guys?"
            scene ep12_fcomp98 with dissolve
            mc "I'll stay and watch the others fight. I wanna support Dwyane and Tate, and after that, I need to help out with cleaning and such."
            mc "If you girls want to head out, go ahead. I'm happy you came here for me."
            scene ep12_fcomp96 with dissolve
            my "You deserve this!"
            js "Enjoy the rest, and we'll talk later."
    if not breakup and branchSage and (ep11_sage_love == 2 or RPsage >= 22):
        play sound "sound_effects/shove.mp3"
        scene ep12_fcomp104 with hpunch
        sa "Yes! You won!"
        scene ep12_fcomp105 with dissolve
        mc "I'm so happy you got to see it."
        scene ep12_fcomp104 with dissolve
        sa "What the hell was that at the end, [name]? Where did that come from?"
        scene ep12_fcomp106 with dissolve
        mc "I just went for it. Feeling how I connected with each punch kept fueling me."
        mc "And then I wanted to try something special, so I tricked him with a kick, and he couldn't block or dodge it."
        scene ep12_fcomp109 with dissolve
        my "You were amazing!"
        scene ep12_fcomp110 with dissolve
        js "Yeah! Everyone around us was completely shocked. Did you even hear the gasps!?"
        scene ep12_fcomp111 with dissolve
        mc "Haha! No, I was in the zone. I couldn't hear or think about anything else but the guy in front of me."
        mc "But now, I'm starting to take it all in."
        scene ep12_fcomp106 with dissolve
        mc "I was so nervous before the fight. I even threw up in the locker room."
        scene ep12_fcomp108 with dissolve
        sa "You did? I couldn't tell that you were nervous up there."
        sa "You looked so confident. It was such a turn on!"
        scene ep12_fcomp106 with dissolve
        mc "Haha! Something changed when I stepped into the ring."
        mc "But before that, it was a different story."
        scene ep12_fcomp107 with dissolve
        sa "You did it, [name]. You can relax and enjoy yourself now."
        sa "I have to leave. There's a party I'm heading to later, and I need to get ready."
        scene ep12_fcomp106 with dissolve
        mc "A party? What party?"
        scene ep12_fcomp107 with dissolve
        sa "It's a party for the faculty. Jill invited me. She's playing the piano, and my brother will be there playing the cello."
        sa "Basically, I wanna support Jill and mock Tybalt. That's what I'm doing tonight."
        scene ep12_fcomp106 with dissolve
        mc "Haha, I see. Support Jill from me, too. I will stay here and watch the rest of the fights and help out afterward."
        mc "Thanks so much for coming!"
        scene ep12_fcomp112 with dissolve
        sa "*{i}Smack{/i}*"
    if branchZoey:
        play sound "sound_effects/shove.mp3"
        scene ep12_fcomp113 with hpunch
        zo "Whoa! You absolutely smashed that!"
        scene ep12_fcomp114 with dissolve
        mc "Surprised?"
        scene ep12_fcomp115 with dissolve
        zo "I'm blown away!"
        zo "Everyone in the audience started chanting your name. And I was like..."
        zo "That's my guy they're chanting for. That's [name] up there."
        scene ep12_fcomp114 with dissolve
        mc "Aw..."
        scene ep12_fcomp116 with dissolve
        zo "How do you feel? Are you hurt?"
        scene ep12_fcomp117 with dissolve
        mc "No, I'm not hurt at all. I'm exhausted, though."
        mc "I gave it everything I had."
        scene ep12_fcomp116 with dissolve
        zo "I could tell. It must be draining to go at it for three rounds."
        scene ep12_fcomp117 with dissolve
        mc "Yeah. I thought I was prepared for it, but it's a completely different thing from sparring."
        mc "But I feel great! I won, Zoey... I won."
        scene ep12_fcomp116 with dissolve
        zo "You sure did."
        zo "Are you going to watch the other fights?"
        scene ep12_fcomp118 with dissolve
        mc "Yeah. Dwyane - the guy who was in my corner - and Tate have fights coming up."
        mc "I wanna cheer them on, and then I need to help clean up the place after the competition."
        mc "Do you need to leave, or?"
        scene ep12_fcomp119 with dissolve
        zo "No way! I'll stay and watch the fights with you."
        scene ep12_fcomp120 with dissolve
        $ renpy.pause()
    if not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
        scene ep12_fcomp121 with dissolve
        nic "Seeing you fight like that was such a turn-on."
        scene ep12_fcomp122 with dissolve
        mc "Really? I'm happy I won then."
        scene ep12_fcomp123 with dissolve
        nic "*{i}Smack{/i}*"
        scene ep12_fcomp124 with dissolve
        nic "I didn't know you were this good at fighting. I'm in awe."
        scene ep12_fcomp125 with dissolve
        mc "I trained a lot with Dad when I was younger, but this was the first time I competed."
        scene ep12_fcomp124 with dissolve
        nic "And I'm guessing it's not the last time either."
        scene ep12_fcomp125 with dissolve
        mc "Oh, it won't be! I want to do it again."
        scene ep12_fcomp124 with dissolve
        nic "When's your next fight? I have to clear my schedule."
        scene ep12_fcomp126 with dissolve
        mc "Haha! We'll see. For now, I want to enjoy the victory and root for my pals when they fight."
    scene ep12_fcomp127 with dissolve
    le "Awesome fight, [name]!!!"
    scene ep12_fcomp128 with dissolve
    mc "Hey! You guys came? I didn't even see you."
    scene ep12_fcomp129 with dissolve
    tm "Derek told us about it, and we had to see you win."
    scene ep12_fcomp131 with dissolve
    de "Man, I wish I could fight like you."
    scene ep12_fcomp130 with dissolve
    mc "It's not too late to learn."
    scene ep12_fcomp128 with dissolve
    mc "I need to talk to some of my buddies over there. I'll catch up with you for the other fights!"
    scene ep12_fcomp132 with dissolve
    if ep12_brawler_round_win == 3:
        chao "Congratulations, [name]. That performance was flawless!"
    elif ep12_brawler_round_win > 1:
        chao "Congratulations, [name]. That performance was almost flawless."
    else:
        chao "Congratulations, [name]. That performance was something else."
    scene ep12_fcomp133 with dissolve
    mc "Thanks! I'm so sorry I missed your fight. I was busy freaking out and throwing up in the locker room."
    scene ep12_fcomp134 with dissolve
    chao "Haha! That's good. I usually throw up after."
    scene ep12_fcomp135 with dissolve
    mc "Dad? You came!?"
    scene ep12_fcomp136 with dissolve
    dad "I know you didn't want me to, but I had to see this."
    scene ep12_fcomp137 with dissolve
    mc "You're missing work for this..."
    scene ep12_fcomp138 with dissolve
    dad "Don't worry about it."
    dad "I'm proud of you, son."
    scene ep12_fcomp139 with dissolve
    $ renpy.pause()
else:
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp140 with hpunch
    ann "Oof! He felt that one."
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp142 with vpunch
    ann "Johnny has found his groove."
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp143 with vpunch
    $ renpy.pause()
    play sound "sound_effects/season2/punching_bag_punch.mp3"
    scene ep12_fcomp144 with hpunch
    ann "[name] isn't even fighting back."
    $ renpy.play("sound_effects/season3/dj/dj_audience1.mp3", "sfx3")
    scene ep12_fcomp145 with hpunch
    ann "And that's it! The referee calls it! Johnny wins!"
    if not breakup and (branchMayaJosy or (branchSage and (ep11_sage_love == 2 or RPsage >= 22))):
        scene ep12_fcomp146 with dissolve
        my "Oh no..."
        sa "Dammit..."
        scene ep12_fcomp147 with dissolve
        js "Poor [name]..."
    if branchZoey:
        scene ep12_fcomp148 with dissolve
        zo "..."
    if not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
        scene ep12_fcomp149 with dissolve
        nic "Aw..."
    scene ep12_fcomp28 with dissolve
    ann "Johnny wore [name] down until he was all out of energy."
    ann "A solid performance from Johnny, who proved that playing to your strengths will win matches."
    scene ep12_fcomp150 with dissolve
    dwy "It's alright, [name]. We all lose some."
    scene ep12_fcomp151 with dissolve
    mc "I was overwhelmed."
    scene ep12_fcomp150 with dissolve
    dwy "You'll have to do more cardio. We'll come up with a plan for you."
    scene ep12_fcomp152 with dissolve
    ann "The referee has put a stop to this fight in the third round. Declaring the winner by TKO..."
    scene ep12_fcomp153 with dissolve
    play sound "sound_effects/season3/dj/dj_audience1.mp3"
    ann "Johnny Stevens!"
    aud "*{i}Cheers{/i}*"
    stop music fadeout 3
    scene ep12_fcomp28 with dissolve
    ann "The next fight will start in 15 minutes."
    show screen new_phone_screen
    play music "music/ep_interlude/licensed_music/track108.mp3"
    scene ep12_fcomp154 with dissolve
    mc "..."
    scene ep12_fcomp155 with dissolve
    dwy "Chin up. There's always next time."
    scene ep12_fcomp154 with dissolve
    mc "Yeah..."
    if not breakup and branchMayaJosy:
        scene ep12_fcomp156 with dissolve
        js "Hey, [name]..."
        my "You did so well."
        scene ep12_fcomp157 with dissolve
        mc "No. I sucked... He was a better fighter than I was."
        scene ep12_fcomp158 with dissolve
        sa "Don't beat yourself up. It was your first fight."
        scene ep12_fcomp157 with dissolve
        mc "I know, but I wanted to win... Damn... I'm so disappointed in myself."
        scene ep12_fcomp159 with dissolve
        js "You shouldn't be. It takes courage to do what you did."
        js "And someone has to lose."
        scene ep12_fcomp160 with dissolve
        my "You fought against someone with more experience than you."
        my "You were at a disadvantage. But next fight, you'll be even better at it!"
        scene ep12_fcomp157 with dissolve
        mc "Thanks for the support... I can't accept what you're saying, but I still appreciate it."
    if not breakup and (branchMayaJosy or (branchSage and (ep11_sage_love == 2 or RPsage >= 22))):
        scene ep12_fcomp161 with dissolve
        sa "I'm so sorry, [name]..."
        scene ep12_fcomp162 with dissolve
        mc "It's not your fault I suck."
        scene ep12_fcomp161 with dissolve
        sa "Don't talk about yourself like that. You didn't suck."
        sa "You went three rounds against him. That's hardcore."
        scene ep12_fcomp164 with dissolve
        my "Yeah! You did so well."
        scene ep12_fcomp163 with dissolve
        mc "I ran out of energy in the third round. I wanted it, but I couldn't give more than that..."
        scene ep12_fcomp165 with dissolve
        sa "I think you did great. You put on a great show."
        sa "The audience loved the fight."
        scene ep12_fcomp163 with dissolve
        mc "If I had only won..."
        scene ep12_fcomp165 with dissolve
        sa "You'll win at some point. Don't stop believing in yourself."
        sa "We believe in you."
        scene ep12_fcomp163 with dissolve
        mc "Thanks..."
        scene ep12_fcomp165 with dissolve
        sa "I have to leave. There's this party I'm heading to later and I need to get ready for it."
        scene ep12_fcomp166 with dissolve
        mc "A party? What party?"
        scene ep12_fcomp167 with dissolve
        sa "It's a party for the faculty. Jill invited me. She's playing the piano and my brother will be there playing the cello."
        sa "Basically, I wanna support Jill and mock Tybalt. That's what I'm doing tonight."
        scene ep12_fcomp166 with dissolve
        mc "I see. Support Jill from me, too. I will stay here and watch the rest of the fights and help out afterward."
        scene ep12_fcomp112 with dissolve
        sa "*{i}Smack{/i}*"
    if branchZoey:
        scene ep12_fcomp168 with dissolve
        zo "You did well, [name]."
        scene ep12_fcomp169 with dissolve
        mc "Not good enough..."
        scene ep12_fcomp168 with dissolve
        zo "That dude was a pro. Cut yourself some slack."
        zo "He was boring to watch, too. He just kept blocking and dodging while you tried to land shots."
        scene ep12_fcomp170 with dissolve
        mc "Well, his strategy worked. I was gassed out in the third..."
        mc "I suck."
        scene ep12_fcomp171 with dissolve
        zo "Stop that. It doesn't mean you're a bad fighter."
        zo "You'll fight again and keep improving. This was your first fight, dude."
        scene ep12_fcomp170 with dissolve
        mc "Fuck... I wanted to win."
        scene ep12_fcomp172 with dissolve
        zo "I know."
        scene ep12_fcomp173 with dissolve
        $ renpy.pause()
    if not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
        scene ep12_fcomp174 with dissolve
        nic "You were so close... I thought you had him."
        scene ep12_fcomp175 with dissolve
        mc "Nah, I wasn't close. He was the better fighter."
        scene ep12_fcomp174 with dissolve
        nic "Don't put too much weight into winning or losing."
        nic "You entertained everyone. I enjoyed the fight even though you lost."
        scene ep12_fcomp176 with dissolve
        mc "If I don't fight to win, why do I fight at all?"
        scene ep12_fcomp177 with dissolve
        nic "Didn't you have fun? It looked like you did."
        scene ep12_fcomp176 with dissolve
        mc "Yeah, it was fun. But I wanted to win..."
        scene ep12_fcomp178 with dissolve
        nic "You're a winner in my book."
        scene ep12_fcomp175 with dissolve
        $ renpy.pause()
    scene ep12_fcomp179 with dissolve
    le "That was so close, [name]."
    scene ep12_fcomp180 with dissolve
    mc "Hey... I didn't know you guys were coming. I didn't even see you."
    scene ep12_fcomp181 with dissolve
    tm "Derek told us about it, and we had to see you fight."
    scene ep12_fcomp182 with dissolve
    de "Who put you up against someone with a record like that for your first fight? That's fucked up, [mc_de]."
    scene ep12_fcomp183 with dissolve
    mc "Yeah, he was better than me."
    scene ep12_fcomp179 with dissolve
    le "I was still impressed."
    scene ep12_fcomp181 with dissolve
    tm "Get some ice on that face. You should be proud."
    scene ep12_fcomp180 with dissolve
    mc "Thanks. I need to talk to some of my buddies over there. I'll catch up with you for the other fights."
    scene ep12_fcomp184 with dissolve
    chao "Welcome to the club, [name]."
    scene ep12_fcomp185 with dissolve
    mc "Was it five consecutive matches you lost before winning one?"
    scene ep12_fcomp184 with dissolve
    chao "Yeah. Losing is part of the journey, [name]. You've just started it."
    scene ep12_fcomp185 with dissolve
    mc "Yeah... I'm so sorry I missed your fight. I was busy freaking out and throwing up in the locker room."
    scene ep12_fcomp186 with dissolve
    chao "Haha! That's good. I usually throw up after."
    scene ep12_fcomp187 with dissolve
    mc "Dad? You came!?"
    scene ep12_fcomp188 with dissolve
    dad "I know you didn't want me to, but I had to see this."
    scene ep12_fcomp189 with dissolve
    mc "You're missing work for this..."
    scene ep12_fcomp190 with dissolve
    dad "Don't worry about it."
    scene ep12_fcomp189 with dissolve
    mc "I'm sorry I didn't win."
    scene ep12_fcomp190 with dissolve
    dad "I'm proud of you, son. You looked great up there."
    scene ep12_fcomp191 with dissolve
    $ renpy.pause()

if ep12_brawler_comp_won:
    scene ep12_fcomp192 with fade
    $ renpy.pause()
else:
    scene ep12_fcomp192b with fade
    $ renpy.pause()
scene ep12_fcomp193 with dissolve
dwy "It happens, bro."
scene ep12_fcomp194 with dissolve
tate "It shouldn't have happened."
scene ep12_fcomp195 with dissolve
dwy "You'll get him next time."
scene ep12_fcomp194 with dissolve
tate "Easy for you to say. When was the last time you lost a fight?"
if ep12_brawler_comp_won:
    scene ep12_fcomp196 with dissolve
    $ renpy.pause()
    scene ep12_fcomp197 with dissolve
    mc "Let him be. I don't think there's anything we can say right now to make him feel better."
    scene ep12_fcomp198 with dissolve
    dwy "But he fought like a champion. He just got caught. All it takes is one bad decision, and a good fight is lost."
    scene ep12_fcomp199 with dissolve
    jen "Excuse me. [name] [lname]?"
    scene ep12_fcomp200 with dissolve
    mc "Yes?"
    scene ep12_fcomp199 with dissolve
    jen "I'm Jen Byson. My job is to keep an eye out for new talent, and I'd like a word with you."
    scene ep12_fcomp201 with dissolve
    dwy "My man."
    scene ep12_fcomp202 with dissolve
    jen "Congratulations on your win. I found it hard to believe that it was your first fight."
    scene ep12_fcomp203 with dissolve
    mc "Heh... Thanks! But it was."
    scene ep12_fcomp202 with dissolve
    jen "Have you been practicing for long?"
    scene ep12_fcomp203 with dissolve
    mc "It depends on how you look at it. I'm fairly new to the club, but I've practiced fighting for many years."
    scene ep12_fcomp204 with dissolve
    jen "It's not often I see someone with raw talent for the sport, and when I do, my interest is instantly piqued."
    jen "I came here today to scout Johnny Stevens of the City Fighters club. Rumors had it that he showed promise for the next step of his career..."
    scene ep12_fcomp205 with dissolve
    jen "But I have to say, with the display you put up today, my eyes weren't on Johnny at all. They were on you."
    jen "And it wasn't because Johnny didn't try to win. I could tell that he wanted the win."
    jen "But you were confident, talented, and - most of all - entertaining to watch."
    scene ep12_fcomp207 with dissolve
    mc "I'm honored... Thanks so much."
    scene ep12_fcomp206 with dissolve
    jen "It would be highly unusual to promote someone with one fight on their record."
    jen "But I'm in this business because I have a talent on my own."
    jen "I have a sixth sense for spotting promising athletes."
    scene ep12_fcomp205 with dissolve
    jen "If you're serious about martial arts, I can sense a long-term professional career for you. And I'd like to get on that train early."
    jen "So, are you serious about it?"
    scene ep12_fcomp207 with dissolve
    mc "I loved being in the ring today. I enjoyed every moment of it. I wanna do it again, for sure."
    mc "But I'm in college. This is more of a hobby for me and a way to stay in shape."
    scene ep12_fcomp204 with dissolve
    jen "That's not a problem. Most athletes need a profession while they are up and coming."
    jen "It takes hard work to make it in this business, and most don't get paid enough to make it their living."
    jen "What I can offer you is my representation, should you wish."
    scene ep12_fcomp207 with dissolve
    mc "What does that mean?"
    scene ep12_fcomp205 with dissolve
    jen "It means I'll manage your fights and everything related to your fighting career. I'll set you up with a trainer and a dedicated club."
    jen "I'll sign you up for fights and take care of the details."
    scene ep12_fcomp204 with dissolve
    jen "I'll also help you look for sponsorship deals by introducing you to sponsors."
    jen "Until you get paid for fights, you'll earn income through sponsors."
    scene ep12_fcomp207 with dissolve
    mc "It all sounds good, but... it also sounds expensive, and I don't have a lot of money."
    mc "I can't pay for a trainer or your services. I could barely afford to fight today."
    scene ep12_fcomp206 with dissolve
    jen "I know it takes funding to get started. This is an investment on my end, and it would all be part of our agreement."
    jen "In return, my fee is 40%% of what you'd make from any fights or deals while I represent you."
    scene ep12_fcomp205 with dissolve
    jen "What I require from you is your commitment and dedication to the sport. And it would help if you'd put yourself out there on social media, showcasing your fights and training."
    jen "You need to build yourself a fan base and make a name for yourself."
    jen "I will help you with that as well."
    scene ep12_fcomp207 with dissolve
    mc "Oh?"
    scene ep12_fcomp206 with dissolve
    jen "We can talk numbers and details if it comes to it."
    scene ep12_fcomp208 with dissolve
    jen "Here's my card. Take your time to consider my offer."
    jen "If you're up for it, give me a call, and I'll put it in writing."
    scene ep12_fcomp209 with dissolve
    mc "I will think about it... Thanks for this opportunity."
    scene ep12_fcomp206 with dissolve
    jen "I'm sure it sounds intimidating to you right now, but don't worry. We could accomplish something great together."
    jen "If your fighting today is the standard of intensity and entertainment you'd bring to the sport, you will make it far."
    scene ep12_fcomp210 with dissolve
    jen "Again, congratulations on your win. You were spectacular."
    scene ep12_fcomp211 with dissolve
    $ renpy.pause()
    scene ep12_fcomp212 with dissolve
    dwy "Bro... What the hell? That was the scout! What did she say?"
    scene ep12_fcomp213 with dissolve
    mc "She offered me her representation."
    scene ep12_fcomp214 with dissolve
    dwy "Did she miss me? I was standing right next to you."
    scene ep12_fcomp213 with dissolve
    mc "She said she was scouting Johnny, but that I stole the show."
    scene ep12_fcomp214 with dissolve
    dwy "She noticed you during your first fight. Do you have any clue how lucky you are?"
    dwy "We've been scrapping for years and never got scouted."
    scene ep12_fcomp215 with dissolve
    chao "Someone got scouted?"
    scene ep12_fcomp216 with dissolve
    dwy "[name] got scouted!"
    scene ep12_fcomp217 with dissolve
    chao "Congrats... Man, I'm jealous."
    scene ep12_fcomp218 with dissolve
    mc "Relax... I haven't signed a deal or something. It was just an offer."
    scene ep12_fcomp217 with dissolve
    chao "What was the offer?"
    scene ep12_fcomp218 with dissolve
    mc "She said she could set me up with a trainer and club and manage my fighting career."
    mc "She'd help me find sponsors and make a name for myself on social media and such."
    mc "But she wants 40%% of the money I make as a fighter. That's a lot, isn't it?"
    scene ep12_fcomp219 with dissolve
    dwy "That's what those agencies do. They discover talent and profit from them."
    dwy "Sure, you could say they are predatory by doing that. 40%% is a high price to pay for not doing the dirty work..."
    scene ep12_fcomp220 with dissolve
    dwy "But bro... Without a manager, it will take a hell of a lot more luck to get somewhere. These people know the business better than anybody."
    scene ep12_fcomp217 with dissolve
    chao "I'm with Dwyane. This is a great opportunity for you. She must be sitting on all kinds of contacts."
    chao "Make sure that you can exit the deal scot-free somehow."
    chao "If you make it, you won't need her anymore."
    scene ep12_fcomp218 with dissolve
    mc "I'm not gonna make it, guys. I've had one fight."
    mc "And now it's a lot of pressure being put on my shoulders."
    mc "I'm not sure if I should do this... Maybe I'll keep fighting for fun, and that's it."
    scene ep12_fcomp220 with dissolve
    dwy "I can't believe what I'm hearing..."
    dwy "Don't throw away this opportunity... She's right about you."
    scene ep12_fcomp219 with dissolve
    dwy "I was in your corner the entire fight, yeah?"
    dwy "All I could think about when I saw you fight was how shitty the other guy must feel going up against you."
    scene ep12_fcomp221 with dissolve
    dwy "The dude had a flawless record, but in his eighth fight, he was dominated by a newcomer."
    dwy "And he put up a hell of a fight, too."
    scene ep12_fcomp218 with dissolve
    mc "Man... I don't know..."
    scene ep12_fcomp219 with dissolve
    dwy "Can you at least think about it?"
    dwy "I'm not one for begging. But if you feel like you owe me something, this is it."
    scene ep12_fcomp218 with dissolve
    mc "Oh, I will think about it. I'm sure it will keep me up at night."
    stop music fadeout 3
    scene ep12_fcomp222 with dissolve
    $ renpy.pause()
else:
    scene ep12_fcomp223 with dissolve
    mc "Just let us feel like shit."
    scene ep12_fcomp224 with dissolve
    dwy "Learning how to take a loss is part of the sport."
    scene ep12_fcomp223 with dissolve
    mc "Yeah, but this soon after the loss... It hurts even more."
    scene ep12_fcomp225 with dissolve
    $ renpy.pause()
    scene ep12_fcomp226 with dissolve
    tate "Thanks, [name]."
    tate "How are you feeling?"
    scene ep12_fcomp227 with dissolve
    mc "Probably the same as you."
    scene ep12_fcomp226 with dissolve
    tate "Yeah? I'm going over the fight in my head... Over and over."
    tate "I dodged into his fist... Why did I choose to go right instead of left?"
    scene ep12_fcomp227 with dissolve
    mc "You made a guess. It was wrong, and you got punished for it."
    scene ep12_fcomp226 with dissolve
    tate "Yeah... I suppose."
    scene ep12_fcomp228 with dissolve
    mc "I'd take a bad guess over not being in good enough shape."
    scene ep12_fcomp229 with dissolve
    tate "It's not about you being in bad shape, because you're not."
    tate "You didn't conserve the energy when you needed to."
    scene ep12_fcomp226 with dissolve
    tate "I saw it... You ended up playing his game, not yours."
    scene ep12_fcomp227 with dissolve
    mc "What do you mean?"
    scene ep12_fcomp226 with dissolve
    tate "Every time you threw a punch, he backed away, and you kept chasing."
    tate "He didn't lose as much energy from that as you did, throwing all those punches."
    scene ep12_fcomp227 with dissolve
    mc "Well, what should I have done? Waited for him to attack me?"
    scene ep12_fcomp229 with dissolve
    tate "You could have waited for him to take a step forward before you went at him again - small things like that."
    scene ep12_fcomp228 with dissolve
    mc "I wanted it too much..."
    scene ep12_fcomp229 with dissolve
    tate "You fought against someone with more experience than you."
    tate "If you're not scared of catching a punch, you can keep your calm in the ring and develop a strategy."
    scene ep12_fcomp230 with dissolve
    tate "You'll win at some point. It might not be your next fight, or the one after that, but you're a good fighter."
    tate "I'm not just saying that."
    scene ep12_fcomp231 with dissolve
    mc "Thanks, Tate."
    stop music fadeout 3
    scene ep12_fcomp232 with dissolve
    $ renpy.pause()

if ep12_brawler_comp_won:
    $ new_bio("You", "I fought in the fighting competition and won! It felt amazing to win in front of an audience, and a scout named Jen Byson approached me after to make a deal.")
else:
    $ new_bio("You", "I fought in the fighting competition, but I lost. It was tough to accept defeat, but in the end, I wasn't good enough.")

jump ep12_no_fparty_label

label ep12_fparty_label:
$ guideSuggestedPage = 257
play music "music/ep11/licensed_music/track161.mp3"
show screen new_phone_screen
scene ep12_fparty1 with wipeleft
$ renpy.pause()
scene ep12_fparty2 with dissolve
$ renpy.pause()
scene ep12_fparty3 with dissolve
de "This party blows."
scene ep12_fparty4 with dissolve
mc "I told you there would be mostly faculty and non-students."
mc "Why did you insist on coming?"
scene ep12_fparty5 with dissolve
de "What do you mean by \"Why\"? I wanna hear you play."
de "And also, it's a party. I'm not passing up on a party if I'm invited."
scene ep12_fparty6 with dissolve
mc "But you weren't invited. You tagged along anyway."
scene ep12_fparty7 with dissolve
de "Semantics."
de "When do you get the show going?"
scene ep12_fparty6 with dissolve
mc "It will be a while. Right now, there's a flutist playing."
mc "Then there's some dude named Muriel playing the trumpet."
scene ep12_fparty8 with dissolve
de "Muriel? What the hell kinda name is Muriel?"
scene ep12_fparty9 with dissolve
mc "Haha, I know. It's odd. I think it was Muriel Storch."
scene ep12_fparty7 with dissolve
de "Man, that dude's parents must have hated him. Sheesh. Who names a kid that?"
scene ep12_fparty6 with dissolve
mc "After him, there will be a speech by a professor, I think."
mc "After that, Jill will play. Then I will play."
scene ep12_fparty7 with dissolve
de "Sounds like a long night..."
scene ep12_fparty6 with dissolve
mc "If you stick around after that, Tybalt will play too."
scene ep12_fparty10 with dissolve
de "Huh? What does he play?"
scene ep12_fparty6 with dissolve
mc "The cello, apparently. And it says on the program that he even brought a band. Can you believe that?"
scene ep12_fparty11 with dissolve
de "Ugh! I'm not sticking around to watch that. Let's bounce after you're done."
scene ep12_fparty12 with dissolve
mc "You don't have to stay after, but I will. I get paid to be here."
scene ep12_fparty13 with dissolve
de "Are you paid to party? Are you stripping for the guests or something?"
scene ep12_fparty12 with dissolve
mc "They pay me to play the guitar."
scene ep12_fparty14 with dissolve
de "How much are they paying you?"
scene ep12_fparty12 with dissolve
mc "$100 and a free meal."
scene ep12_fparty13 with dissolve
de "What? Isn't the meal free?"
scene ep12_fparty12 with dissolve
mc "But Professor Hoff said the real reward is to network with the guests."
mc "There are some esteemed ones at the party."
scene ep12_fparty14 with dissolve
de "Meh. And say what? I bet we have nothing in common with them."
scene ep12_fparty15 with dissolve
mc "Well, we gotta do something while we wait."
scene ep12_fparty16 with dissolve
de "Go ahead and mingle with them if you want. I'm gonna get myself a free meal too."

scene ep12_fparty17 with dissolve
$ renpy.pause()
scene ep12_fparty18 with dissolve
ty "Haha, can you believe he got in dressed like that?"
scene ep12_fparty19 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 258
if (branchJill or branchSage) and not breakup:
    if branchJill and not breakup:
        scene ep12_fparty20 with dissolve
        ji "Guess who?"
        scene ep12_fparty21 with dissolve
        menu:
            "Jill":
                mc "Jill?"
                scene ep12_fparty22 with dissolve
                ji "Haha, you guessed it."
            "Joke":
                mc "Professor Hoff?"
                scene ep12_fparty22 with dissolve
                ji "No. It's me."
                scene ep12_fparty23 with dissolve
                mc "Oh, good! That would have been creepy."
                scene ep12_fparty24 with dissolve
                ji "Hahaha!"
        if tc > 4 and not persistent.no_cheater:
            scene ep12_fparty26 with dissolve
            ji "*{i}Smack{/i}*"
            scene ep12_fparty27 with dissolve
            ji "Are you ok?"
            scene ep12_fparty28 with dissolve
            mc "Uh... Big night. How about you?"
        else:
            scene ep12_fparty25 with dissolve
            ji "*{i}Smack{/i}*"
            scene ep12_fparty29 with dissolve
            mc "Wow. You look lovely."
            scene ep12_fparty30 with dissolve
            ji "Aw, thank you. As do you."
            scene ep12_fparty31 with dissolve
            mc "You think? I feel like I don't fit in among all the suits and fancy dresses."
            scene ep12_fparty32 with dissolve
            ji "You're perfect the way you are."
            scene ep12_fparty31 with dissolve
            mc "How are you feeling? It's a big night."
        scene ep12_fparty33 with dissolve
        ji "It is. I'm doing great. I'm looking forward to playing tonight."
        scene ep12_fparty34 with dissolve
        ji "Look at the stage. It's not that intimidating."
        ji "In fact, it's not even a stage. It's a space with instruments."
        scene ep12_fparty33 with dissolve
        ji "And everyone here won't pay attention to us. They will mingle and talk while we play."
        ji "It's nothing like the auditorium."
        ji "That thought calms my nerves."
        scene ep12_fparty35 with dissolve
        ji "I'm happy I get to do this with you... Again. Haha!"
        scene ep12_fparty36 with dissolve
        sa "Don't mind me. Third wheel checking in."
        scene ep12_fparty37 with dissolve
        mc "Hey, Sage. What are you doing here?"
    if branchSage and not breakup:
        scene ep12_fparty41 with dissolve
        sa "Somebody call security. There's a party crasher here."
        ji "Haha."
        scene ep12_fparty37 with dissolve
        mc "Sage? Jill?"
        scene ep12_fparty42 with dissolve
        ji "Hi, [name]."
        scene ep12_fparty43 with dissolve
        mc "You look...wow."
        scene ep12_fparty44 with dissolve
        sa "Yep. We both do."
        scene ep12_fparty43 with dissolve
        mc "For sure."
        mc "I know why Jill is here, but why are you?"
    scene ep12_fparty38 with dissolve
    sa "Didn't Jill tell you? I'm the closing act."
    scene ep12_fparty37 with dissolve
    mc "The closing act?"
    scene ep12_fparty38 with dissolve
    sa "Yeah, I'm gonna juggle."
    scene ep12_fparty37 with dissolve
    mc "Juggle?"
    scene ep12_fparty39 with dissolve
    ji "Hahaha!"
    sa "Gullible much?"
    sa "Jill invited me. I want to watch you perform."
    scene ep12_fparty38 with dissolve
    sa "Thanks for not inviting me, by the way."
    scene ep12_fparty37 with dissolve
    mc "I didn't realize we could invite people."
    scene ep12_fparty40 with dissolve
    sa "Yeah? Isn't that Derek over there stuffing his face with food?"
    scene ep12_fparty45 with dissolve
    mc "Derek invited himself."
    mc "Besides, it's not our kind of party."
    scene ep12_fparty46 with dissolve
    sa "It does reek of an adult party, at which we will sit at the kids' table."
    scene ep12_fparty47 with dissolve
    mc "At least the kids' table has Champagne."
    scene ep12_fparty48 with dissolve
    sa "But no glasses... I doubt there will be a body shot competition."
    scene ep12_fparty49 with dissolve
    mc "If there is, I call dibs on you two."
    scene ep12_fparty50 with dissolve
    ji "[name]... Our parents are here. Mine are at the next table."
    scene ep12_fparty49 with dissolve
    mc "I'm not doing body shots with them."
elif breakup or ep4_toldDerekAboutJade:
    scene ep12_fparty51 with dissolve
    mc "(Why is Sage here? Jill must have invited her...)"
    scene ep12_fparty52 with dissolve
    $ renpy.pause()
    if branchZoey and breakup:
        if branchSage or branchJill:
            scene ep12_fparty53 with dissolve
            mc "(They've gotten close... I can't blame them for not wanting to talk to me.)"
            scene ep12_fparty54 with dissolve
            mc "(But fuck... It hurts being ignored by them.)"
        else:
            scene ep12_fparty53b with dissolve
            mc "(It seems like the news about Zoey has reached them...)"
            scene ep12_fparty54 with dissolve
            mc "(Fuck... Not that long ago, we were close friends, and now they're ignoring me...)"
            if branchMayaJosy:
                mc "(I can't blame them for siding with Josy and Maya...)"
                mc "(Even I blame myself for hurting them.)"
            else:
                mc "(I can't blame them for siding with Bella...)"
                mc "(Even I blame myself for hurting her.)"
    else:
        if branchJill:
            scene ep12_fparty53 with dissolve
            mc "(They both hate me now...)"
            scene ep12_fparty54 with dissolve
            mc "(We used to be so close, and now they're ignoring me.)"
        else:
            if ep12_break_or_tell == "break":
                scene ep12_fparty53b with dissolve
                mc "(They've gotten close...)"
                mc "(Jill is supporting Sage after our breakup.)"
                scene ep12_fparty54 with dissolve
                mc "(I wish she were here for me, too, but at least she's helping Sage get through it.)"
                mc "(It hurts to be ignored...)"
            else:
                if not branchIsabella or ep4_toldDerekAboutJade:
                    scene ep12_fparty53 with dissolve
                    mc "(Sage must have told Jill what I did...)"
                else:
                    scene ep12_fparty53b with dissolve
                    mc "(I have a feeling Bella told them what I did...)"
                scene ep12_fparty54 with dissolve
                mc "(We used to be so close and now they're ignoring me.)"
else:
    scene ep12_fparty41 with dissolve
    sa "Look who we have here."
    scene ep12_fparty37 with dissolve
    mc "Jill! Sage? Why are you here?"
    scene ep12_fparty38 with dissolve
    sa "You don't sound happy to see me."
    scene ep12_fparty37 with dissolve
    mc "I meant, {b}why{/b} are you here? Why did you choose to come to this party?"
    scene ep12_fparty38 with dissolve
    sa "Jill invited me. I want to watch you perform."
    sa "Thanks for not inviting me, by the way."
    scene ep12_fparty37 with dissolve
    mc "I didn't realize we could invite people."
    scene ep12_fparty40 with dissolve
    sa "Yeah? Isn't that Derek over there stuffing his face with food?"
    scene ep12_fparty45 with dissolve
    mc "Derek invited himself."
    mc "Besides, it's not our kind of party."
    scene ep12_fparty46 with dissolve
    sa "It does reek of an adult party, at which we will sit at the kids' table."
    scene ep12_fparty55 with dissolve
    mc "Is that because your parents are here?"
    scene ep12_fparty56 with dissolve
    sa "Kinda. At least they are keeping their distance from each other."
    sa "It's scary how important appearances are to them."
    scene ep12_fparty57 with dissolve
    mc "So, Jill... How are you feeling about performing?"
    scene ep12_fparty58 with dissolve
    ji "I'm feeling good. I'm looking forward to playing tonight."
    scene ep12_fparty34 with dissolve
    ji "Look at the stage. It's not that intimidating."
    ji "In fact, it's not even a stage. It's a space with instruments."
    scene ep12_fparty58 with dissolve
    ji "And everyone here won't pay attention to us. They will mingle and talk while we play."
    ji "It's nothing like the auditorium."
    ji "That thought calms my nerves."
    scene ep12_fparty59 with dissolve
    sa "You'll both do fine."
    sa "Did you see any booze we could yoink? This party could use some."

label ep12_no_fparty_label:
if not ep11_music:
    hide screen new_phone_screen
    play music "music/ep11/licensed_music/track161.mp3"
    scene ep12_fparty64a with wipeleft
    $ renpy.pause()
scene ep12_fparty64 with dissolve
sb "Bella. You came."
scene ep12_fparty60 with dissolve
isa "Were you under the assumption that I wouldn't come?"
scene ep12_fparty64 with dissolve
sb "You never know with these events. Sometimes Christmas plans interfere."
sb "How was your Christmas? A big family gathering?"
scene ep12_fparty60 with dissolve
isa "I celebrated it with friends."
scene ep12_fparty65 with dissolve
sb "Mine wasn't with family either. It was lonely."
sb "I'm not sure if you heard the news..."
scene ep12_fparty67 with dissolve
sb "Jade and I have separated."
scene ep12_fparty62 with dissolve
isa "I'm sorry to hear that."
scene ep12_fparty61 with dissolve
sb "I couldn't help but notice that you're not wearing your wedding band either."
scene ep12_fparty65 with dissolve
sb "I don't want to appear nosey, but... Is everything ok at home?"
scene ep12_fparty62 with dissolve
isa "Everything is fine, thanks."
scene ep12_fparty64 with dissolve
sb "No ring... Celebrating Christmas with friends..."
sb "If you need to talk to someone about it, I'm always available."
scene ep12_fparty63 with dissolve
isa "I celebrated Christmas with friends because that's what I wanted."
isa "We had a wonderful Christmas together, and just because I'm not wearing a ring doesn't give you an invitation to pry."
scene ep12_fparty66 with dissolve
$ renpy.pause()
if not ep11_music:
    jump ep12_no_fparty2_label

scene ep12_fparty68 with dissolve
de "How hard can it be to play the trumpet? It has three buttons."
scene ep12_fparty72 with dissolve
mu "*{i}Snorts{/i}* It has three {b}valves{/b}. And despite that, it's a hard instrument to master."
scene ep12_fparty69 with dissolve
de "I bet I could play it. Can I try it?"
scene ep12_fparty72 with dissolve
mu "Do not touch my trumpet, or any of the brass instruments lying around."
scene ep12_fparty69 with dissolve
de "Come on. Let me hold it for a minute."
scene ep12_fparty73 with dissolve
mu "This trumpet costs $3000. Could you imagine if I let some slob with greasy pork fingers touch my beloved?"
scene ep12_fparty71 with dissolve
de "Your beloved? Really?"
scene ep12_fparty70 with dissolve
mu "Begone! I must focus on my upcoming solo."
scene ep12_fparty76 with dissolve
ph "Muriel! I've been looking for you."
scene ep12_fparty74 with dissolve
mu "Is it time for my solo already?"
scene ep12_fparty76 with dissolve
ph "No, not yet. You have ample time. But I conversed with Mr. Langley about you earlier."
scene ep12_fparty75 with dissolve
mu "Mr. Langley? Are you joshing me?"
scene ep12_fparty76 with dissolve
ph "No. He was keen on talking to you."
ph "I mentioned that you and I have fought many battles on the checkered board together. And as it turns out, he's a chess player too."
scene ep12_fparty75 with dissolve
mu "Can you introduce me? I'd love to pick his brain about his recent paper on neural networks."
scene ep12_fparty77 with dissolve
$ renpy.pause()
scene ep12_fparty78 with dissolve
$ renpy.pause()
scene ep12_fparty79 with dissolve
$ renpy.pause()

label ep12_no_fparty2_label:
if not ep11_music:
    scene ep12_fparty80a with dissolve
    isa "Excuse me..."
scene ep12_fparty80 with dissolve
isa "I am so happy you're here tonight."
scene ep12_fparty81 with dissolve
ji "Why? Are you not feeling the Christmas party?"
scene ep12_fparty82 with dissolve
isa "I don't feel like explaining why I don't have a ring on my finger to Professor Burke."
isa "He's getting more blatant."
scene ep12_fparty83 with dissolve
sa "What did my dad say?"
scene ep12_fparty84 with dissolve
isa "Oh... I..."
scene ep12_fparty83 with dissolve
sa "What?"
scene ep12_fparty84 with dissolve
isa "..."
scene ep12_fparty83 with dissolve
sa "What did he do?"
scene ep12_fparty85 with dissolve
isa "He hasn't done anything. But..."
isa "He flirts with me."
scene ep12_fparty88 with dissolve
sa "He flirts with you?"
scene ep12_fparty86 with dissolve
isa "You shouldn't have to hear this about your father."
scene ep12_fparty88 with dissolve
sa "How long has he flirted with you?"
scene ep12_fparty87 with dissolve
isa "Eh..."
scene ep12_fparty89 with dissolve
sa "You said he was getting more blatant."
sa "Bella?"
scene ep12_fparty86 with dissolve
isa "It's been going on for a while. He used to be subtle about it, but not so much lately."
isa "I'm sorry."
scene ep12_fparty90 with dissolve
sa "He's not with Mom anymore, and I know they've had issues for a long time, but yeah, it's not something nice to hear."
sa "You don't have to feel sorry. You haven't done anything wrong."
scene ep12_fparty89 with dissolve
sa "I'm sorry he's hitting on you. I'll talk to him if you want."
scene ep12_fparty87 with dissolve
isa "No. Don't do that. I'd be embarrassed."
scene ep12_fparty89 with dissolve
if ep4_toldDerekAboutJade:
    sa "I'm embarrassed, too. By both my parents..."
else:
    sa "I'm embarrassed, too."
scene ep12_fparty85 with dissolve
isa "Is your mom here tonight?"
scene ep12_fparty90 with dissolve
if ep4_toldDerekAboutJade:
    sa "Yes, but I'm ignoring her. She's doing her best to save face from the divorce."
    scene ep12_fparty93 with dissolve
    ji "Have you talked to her again?"
    scene ep12_fparty91 with dissolve
    sa "We tried to get together for Christmas, but we realized it was pointless to celebrate anything this year."
    scene ep12_fparty94 with dissolve
    isa "What did you end up doing?"
    scene ep12_fparty91 with dissolve
    sa "Pretty much nothing. But I'm fine with it."
else:
    sa "Yes. She's doing her best to save face from the divorce."
    scene ep12_fparty94 with dissolve
    ji "How was your Christmas together with her?"
    scene ep12_fparty91 with dissolve
    sa "We had dinner, but it wasn't merry."
scene ep12_fparty92 with dissolve
sa "At least I got to celebrate Christmas with you guys."
if not ep11_music:
    jump ep12_no_fparty3_label
if not breakup and not ep4_toldDerekAboutJade:
    scene ep12_fparty95 with dissolve
    isa "Is [name] around here somewhere? I wanted to wish him good luck."
    scene ep12_fparty96 with dissolve
    ji "He needed to visit the restroom."
    ji "Also, you shouldn't wish him good luck - that's inviting bad luck. You should tell him to break a leg."
    scene ep12_fparty95 with dissolve
    isa "Yes, of course."
    isa "And I want you to break a leg too."
    scene ep12_fparty96 with dissolve
    ji "Haha, I'll try."

scene ep12_fparty97 with dissolve
de "[name]. Come here."
scene ep12_fparty99 with dissolve
mc "What now?"
scene ep12_fparty98 with dissolve
de "Check out Muriel. He's about to perform."
scene ep12_fparty99 with dissolve
mc "Since when are you into brass music?"
scene ep12_fparty98 with dissolve
de "I have a feeling I will love it."
scene ep12_fparty99 with dissolve
mc "That's nice, I guess."
scene ep12_fparty98 with dissolve
de "And not only because I did unspeakable things to his beloved."
scene ep12_fparty100 with dissolve
mc "What?"
scene ep12_fparty103 with dissolve
de "I stuck his trumpet up my butthole."
scene ep12_fparty104 with dissolve
mc "..."
scene ep12_fparty101 with dissolve
mc "Y-you... What?"
scene ep12_fparty102 with dissolve
de "He told me I had greasy pork fingers."
scene ep12_fparty101 with dissolve
mc "And your instincts told you to do that to him?"
play sound "sound_effects/season3/trumpet.mp3"
scene ep12_fparty108 with dissolve
"{i}Vrmmmp bvaroomf!{/i}"
scene ep12_fparty105 with dissolve
de "HAHAHA!"
scene ep12_fparty109 with dissolve
mu "Oh, dear God!!! What is this!?"
scene ep12_fparty110 with dissolve
ph "Muriel?"
scene ep12_fparty106 with dissolve
de "Brass music. More like ass music, am I right?"
scene ep12_fparty107 with dissolve
mc "What is it with you and shoving things up your ass?"

scene ep12_fparty111 with dissolve
ph "Ahem. We have a slight change in the program."
label ep12_no_fparty3_label:
if ep11_music:
    scene ep12_fparty112 with dissolve
else:
    scene ep12_fparty112b with dissolve
ph "Up next, we'll have the first speaker of the night, who wishes to say a few welcoming words to all of you."
ph "Everyone... Professor Stephen Burke."
play sound "sound_effects/season2/applause2.mp3"
if ep11_music:
    scene ep12_fparty113 with dissolve
else:
    scene ep12_fparty113b with dissolve
"*{i}Smatter of applause{/i}*"
if ep11_music:
    scene ep12_fparty114 with dissolve
else:
    scene ep12_fparty114b with dissolve
sb "Thank you, Professor Hoff."
if ep11_music:
    scene ep12_fparty115 with dissolve
else:
    scene ep12_fparty115b with dissolve
sb "I want to start my speech by giving my sincere thanks to the party committee, who have arranged tonight's entertainment for you."
sb "Professor Hoff has been a part of the committee this year, and they have decided to go with college musicians."
if ep11_music:
    scene ep12_fparty116 with dissolve
else:
    scene ep12_fparty116b with dissolve
sb "And I know what you're thinking..."
sb "No, they weren't forced to be here. It won't reflect on their grades."
sb "And yes, their parents know where they are."
scene ep12_fparty118 with dissolve
"*{i}Laughter{/i}*"
if ep11_music:
    scene ep12_fparty115 with dissolve
else:
    scene ep12_fparty115b with dissolve
sb "My son is performing tonight, so I can attest to that."
if ep11_music:
    scene ep12_fparty117 with dissolve
else:
    scene ep12_fparty117b with dissolve
sb "Welcome, everyone, to our annual Christmas party."
sb "I hope everyone in the dining room can hear me as well. And I also hope that you're enjoying the fantastic buffet."
if ep11_music:
    scene ep12_fparty114 with dissolve
else:
    scene ep12_fparty114b with dissolve
sb "I look forward to this party every year, not only because it is in the middle of a mini-vacation..."
sb "...but also because I get to spend it with you."
if ep11_music:
    scene ep12_fparty116 with dissolve
else:
    scene ep12_fparty116b with dissolve
sb "We have some notorious sponsors with us tonight. And I'd like to go around the room and introduce them..."
sb "First... Mr. Lyle Wallace!"

if not breakup and not ep4_toldDerekAboutJade and ep11_music:
    scene ep12_fparty123 with dissolve
    isa "There you are."
    scene ep12_fparty124 with dissolve
    mc "Hey, you're here."
    if branchIsabella:
        scene ep12_fparty125 with dissolve
        isa "In my mind, I'm giving you a kiss and a hug."
        scene ep12_fparty124 with dissolve
        mc "It sucks that we can't do that now..."
        mc "You look beautiful tonight."
        scene ep12_fparty125 with dissolve
        isa "Likewise, nice shirt!"
        isa "Good luck with your performance tonight."
        scene ep12_fparty132 with dissolve
        ji "*{i}Whispers{/i}* Break a leg."
        scene ep12_fparty125 with dissolve
        isa "I meant, break a leg."
        scene ep12_fparty124 with dissolve
        mc "Thanks! I'm getting excited."
        scene ep12_fparty127 with dissolve
        mc "Oh! FYI... Derek snuck in with me."
        scene ep12_fparty128 with dissolve
        isa "He didn't bring his sword, did he?"
        scene ep12_fparty127 with dissolve
        mc "No, I hope he learned that lesson."
        mc "But it took him like thirty minutes before he had to shove a trumpet up his ass."
        scene ep12_fparty129 with dissolve
        isa "Is that a euphemism?"
        scene ep12_fparty130 with dissolve
        mc "Ask Muriel Storch."
        scene ep12_fparty129 with dissolve
        isa "Who?"
        scene ep12_fparty130 with dissolve
        mc "The brass musician who didn't play his set."
        scene ep12_fparty131 with dissolve
        $ renpy.pause()
    else:
        scene ep12_fparty125 with dissolve
        isa "Good luck on your performance tonight."
        scene ep12_fparty132 with dissolve
        ji "*{i}Whispers{/i}* Break a leg."
        scene ep12_fparty125 with dissolve
        isa "I meant, break a leg."
        scene ep12_fparty124 with dissolve
        mc "Thank you. I will do my best. I'm getting excited."
        mc "Although I don't think most out there are paying attention to the music."
        scene ep12_fparty126 with dissolve
        isa "Some are. It's playing in the dining room too while people are eating."
        isa "I, for one, will listen the whole time. And I'm sure Sage will too."
        scene ep12_fparty133 with dissolve
        sa "Sure, I will. It's the only reason I came here."
    scene ep12_fparty134 with dissolve
    ji "I'm up next... I wish he would stop talking already."
    scene ep12_fparty135 with dissolve
    sa "We all do. He tends to ramble."
    scene ep12_fparty134 with dissolve
    ji "The waiting is what kills me..."
    scene ep12_fparty137 with dissolve
    isa "You'll do fine. Tell us about the songs you'll play."
    scene ep12_fparty136 with dissolve
    ji "I'm going to play a few Christmas songs, but I'll start with a song I wrote for my sister."
    ji "I wanted to surprise my parents. They always loved it when I played it for them."
    scene ep12_fparty137 with dissolve
    isa "They'll be proud of you for honoring her tonight."
    scene ep12_fparty136 with dissolve
    ji "I hope."
else:
    scene ep12_fparty119 with dissolve
    ji "I'm up next... I wish he would stop talking already."
    scene ep12_fparty120 with dissolve
    sa "We all do. Dad can go on for a long time unless he's stopped."
    scene ep12_fparty119 with dissolve
    ji "The waiting is what kills me..."
    scene ep12_fparty121 with dissolve
    isa "You'll do fine. Tell us about the songs you'll play."
    scene ep12_fparty122 with dissolve
    ji "I'm going to play a few Christmas songs, but I'll start with a song I wrote for my sister."
    ji "I wanted to surprise my parents with it. They always loved it when I played it for them."
    scene ep12_fparty121 with dissolve
    isa "They'll be proud of you for honoring her tonight."
    scene ep12_fparty119 with dissolve
    ji "I hope."

if ep11_music:
    scene ep12_fparty114 with dissolve
else:
    scene ep12_fparty114b with dissolve
sb "Thank you all for coming. Enjoy the food, drinks, and entertainment."
sb "Happy Holidays, and have a wonderful end to the year!"
play sound "sound_effects/season2/applause2.mp3"
"*{i}Smatter of applause{/i}*"

if branchJill and not breakup and ep11_music and (tc < 5 or persistent.no_cheater):
    scene ep12_fparty140 with dissolve
    mc "Amelia. Geoff. Hi!"
    scene ep12_fparty138 with dissolve
    ge "I swear, the faculty gets younger and younger every year. Haha!"
    ge "It's good to see you, [name]!"
    scene ep12_fparty139 with dissolve
    jim "I take it you came to listen to Jill play."
    scene ep12_fparty140 with dissolve
    mc "Partly. I'm here to perform, too."
    scene ep12_fparty141 with dissolve
    ge "Ah, of course. You have a talent, [name]. I remember your last performance at the recital."
    ge "Or was it your last? Maybe you've played more in between."
    scene ep12_fparty142 with dissolve
    mc "No, you're right. That was my last performance, and also why I was invited here."
    scene ep12_fparty143 with dissolve
    mc "I wanted to thank you for the Christmas gift Jill gave me."
    mc "I feel honored to play on Lana's guitar."
    scene ep12_fparty144 with dissolve
    jim "Jill insisted on giving it to you. It's nothing against you, but it was hard for us to part with it."
    scene ep12_fparty143 with dissolve
    mc "I understand. I promise to take good care of it."
    scene ep12_fparty144 with dissolve
    jim "You've made an impression on our daughter. She's fond of you."
    scene ep12_fparty143 with dissolve
    mc "I'm fond of her too. Jill is amazing."
    scene ep12_fparty145 with dissolve
    $ renpy.pause()
    scene ep12_fparty143 with dissolve
    mc "I'll let you enjoy her music. It was nice seeing you."
    scene ep12_fparty146 with dissolve
    jim "Well... He is polite."
    scene ep12_fparty147 with dissolve
    ge "Jonathan was smart and polite, too."

scene ep12_fparty148 with dissolve
$ renpy.pause()
if ep8_recital_failed:
    scene ep12_fparty149 with dissolve
else:
    scene ep12_fparty150 with dissolve
$ renpy.pause()
stop music fadeout 3
if ep11_music and not breakup and not ep4_toldDerekAboutJade:
    if branchSage and (ep11_sage_love == 1 or RPsage < 22):
        scene ep12_fparty151b with dissolve
    else:
        scene ep12_fparty151 with dissolve
else:
    scene ep12_fparty152 with dissolve
$ renpy.pause()
play music "music/ep2/reaching_the_sky.mp3"
if ep11_music:
    scene ep12_fparty153 with dissolve
else:
    scene ep12_fparty153b with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

scene ep12_fparty154 with dissolve
jim "Geoff, do you hear what song your daughter is playing?"
stop music fadeout 3
scene ep12_fparty155 with dissolve
$ renpy.pause()
play music "music/ep11/licensed_music/track179.mp3"
if not ep11_music:
    jump ep12_no_fparty4_label
scene ep12_fparty156 with dissolve
mu "What did you do to my trumpet!?"
scene ep12_fparty157 with dissolve
de "I didn't do nothing."
scene ep12_fparty156 with dissolve
mu "Didn't do nothing...? A double negative! So you {b}did{/b} do something?"
scene ep12_fparty157 with dissolve
de "Hey... You told me not to play it, and I didn't play it."
scene ep12_fparty158 with dissolve
ph "Gentlemen... Please, tone it down. Remember where you are tonight."
scene ep12_fparty159 with dissolve
mu "Bah!"
scene ep12_fparty160 with dissolve
ph "One of my roles on the party committee was to reach out to and invite the students who will perform here tonight."
ph "But I don't remember extending the invite to you, Mr. Bailey."
scene ep12_fparty168 with dissolve
de "Erm... I... Some cheesecake?"
scene ep12_fparty161 with dissolve
ph "I snuck into parties when I was your age, too."
ph "But it never crossed my mind to sneak into a faculty party. Haha."
scene ep12_fparty169 with dissolve
de "I came to see my friend play."
scene ep12_fparty160 with dissolve
ph "Mhm. I see."
ph "I talked to the committee the other day. You should expect to be summoned in January."
ph "How are things between you and Anthony since the altercation?"
scene ep12_fparty171 with dissolve
de "We haven't crossed each other's paths more than during the finals."
de "But it went ok."
scene ep12_fparty162 with dissolve
ph "What was it all about, if I may ask?"
scene ep12_fparty170 with dissolve
de "I thought the meeting was in January."
scene ep12_fparty162 with dissolve
ph "This is just between you and me. We're at a party, aren't we?"
scene ep12_fparty171 with dissolve
de "Well... I'm in love with his girlfriend."
scene ep12_fparty163 with dissolve
ph "A lovers' quarrel, you say."
scene ep12_fparty170 with dissolve
de "You can call it that."
scene ep12_fparty163 with dissolve
ph "Ahh... To be young and experience heartbreak again."
scene ep12_fparty169 with dissolve
de "Yeah? Were you a ladies' man?"
scene ep12_fparty164 with dissolve
ph "Haha. Not as much as I wish."
ph "But I, too, was in love with someone who got away from me."
scene ep12_fparty165 with dissolve
ph "*{i}Sigh{/i}*"
scene ep12_fparty164 with dissolve
ph "Are you a smoker, Bailey?"
scene ep12_fparty172 with dissolve
de "Nah."
scene ep12_fparty166 with dissolve
ph "Me neither. Except for a cigar here and there."
ph "Care to join me for one? Bad habits like company."
scene ep12_fparty169 with dissolve
de "Is there a drink that comes with it?"
scene ep12_fparty167 with dissolve
ph "Haha! I'll look the other way if you want to grab yourself a whisky. I'll show you where it is."
scene ep12_fparty173 with dissolve
ph "Now, what did you really do to Muriel's trumpet?"
scene ep12_fparty175 with dissolve
de "I may have shoved it up my butt."
scene ep12_fparty174 with dissolve
ph "BAHAHA! You're quite a joker, Bailey."
scene ep12_fparty173 with dissolve
ph "If there's any truth to that, I don't want to know."
ph "Muriel is a great chess player, but he's a sore loser. He gets on my nerves, too."

label ep12_no_fparty5_label:
if not ep11_music:
    scene ep12_fparty176b with dissolve
else:
    scene ep12_fparty176 with dissolve
$ renpy.pause()
play sound "sound_effects/season2/applause2.mp3"
if not ep11_music:
    scene ep12_fparty177b with dissolve
else:
    scene ep12_fparty177 with dissolve
"*{i}Applause{/i}*"
scene ep12_fparty178 with dissolve
jim "That was beautiful. Well done."
scene ep12_fparty179 with dissolve
ge "I'm proud of you. Superbly played."
scene ep12_fparty180 with dissolve
ji "Thank you so much. I hope you liked my surprise."
scene ep12_fparty178 with dissolve
jim "It's been a long time since we heard you play her song. It made us happy that you remembered it."

scene ep12_fparty181 with dissolve
ji "*{i}Excited noises{/i}*"
scene ep12_fparty183 with dissolve
isa "You did it!"
scene ep12_fparty181 with dissolve
ji "I did it!"
scene ep12_fparty184 with dissolve
sa "You didn't have to be nervous about that at all. You nailed it."
scene ep12_fparty182 with dissolve
ji "*{i}Sigh{/i}* I feel so relieved."
if not ep11_music:
    jump ep12_no_fparty5b_label
if not breakup and not ep4_toldDerekAboutJade and branchJill and (tc < 5 or persistent.no_cheater):
    scene ep12_fparty189 with dissolve
    mc "*{i}Smack{/i}*"
    scene ep12_fparty190 with dissolve
    mc "You played it so well."
    scene ep12_fparty191 with dissolve
    ji "What are you still doing here? You're supposed to go up after me."
    scene ep12_fparty190 with dissolve
    mc "I can't follow you without an intermission! The audience will laugh at me."
    scene ep12_fparty191 with dissolve
    ji "Oh, stop it."
    scene ep12_fparty192 with dissolve
    mc "I'm heading up there. You were amazing!"
elif not breakup and not ep4_toldDerekAboutJade:
    scene ep12_fparty193 with dissolve
    mc "You were amazing, Jill. You'll be a tough act to follow, but I'm heading up there."
    scene ep12_fparty194 with dissolve
    isa "Good luck!"
    scene ep12_fparty195 with dissolve
    ji "Break a leg."
    scene ep12_fparty196 with dissolve
    isa "Dammit."
elif breakup or ep4_toldDerekAboutJade:
    scene ep12_fparty185 with dissolve
    if branchIsabella:
        isa "[name] is next... I don't feel like watching this."
    else:
        isa "[name] is next."
    if branchJill:
        scene ep12_fparty187 with dissolve
        ji "Can we go somewhere else?"
        scene ep12_fparty188 with dissolve
        $ renpy.pause()
    if branchMayaJosy:
        scene ep12_fparty187 with dissolve
        ji "I feel bad..."
        scene ep12_fparty186 with dissolve
        sa "I do too, but what about Josy and Maya? How do you think they feel?"
        scene ep12_fparty185 with dissolve
        isa "We can still show him some support."
        scene ep12_fparty186 with dissolve
        sa "No... I can't do this."
        scene ep12_fparty188 with dissolve
        $ renpy.pause()
    else:
        scene ep12_fparty186 with dissolve
        if branchIsabella:
            sa "Let's leave."
        else:
            sa "Can we leave? I don't want to watch this."
        scene ep12_fparty188 with dissolve
        $ renpy.pause()

scene ep12_fparty197 with dissolve
mc "(I'll do what the others did. I'll just start playing.)"
stop music fadeout 3
scene ep12_fparty198 with dissolve
mc "(No talk... Just music.)"

play music "music/ep12/licensed_music/track196.mp3"
if not breakup and not ep4_toldDerekAboutJade:
    scene ep12_fparty199 with dissolve
else:
    scene ep12_fparty199b with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()

label ep12_no_fparty4_label:
scene ep12_fparty200 with dissolve
sb "Mr. Wallace. Are you enjoying the evening?"
scene ep12_fparty204 with dissolve
wl "Stephen! We were talking about you."
wl "Did you say hi to Mr. Dahl yet?"
scene ep12_fparty209 with dissolve
sb "We spoke earlier tonight together with Mr. Finch."
scene ep12_fparty204 with dissolve
wl "Excellent."
wl "We were debating who contributed the most this year, haha."
scene ep12_fparty210 with dissolve
dh "Yes, Stephen. Help us settle the argument."
scene ep12_fparty200 with dissolve
sb "I'm sure both of you know how much you donated to B&R."
scene ep12_fparty210 with dissolve
dh "Well, I don't. But Mr. Wallace seems to suggest that not knowing the exact figure is equal to peanuts."
scene ep12_fparty205 with dissolve
wl "Hahaha!"
scene ep12_fparty209 with dissolve
sb "It wasn't peanuts. I can assure you."
sb "Tell me, did you find any prospects among the candidates?"
scene ep12_fparty210 with dissolve
dh "Yes. Yes. A couple of them caught my attention."
dh "Mr. Syles! He shows promise. I take it you will put in a good word for me."
scene ep12_fparty203 with dissolve
sb "I can be very convincing."
scene ep12_fparty206 with dissolve
wl "As long as the top candidates reach out to me, I take no issue with that."
scene ep12_fparty200 with dissolve
sb "The candidates are always handpicked and tailored to your business. There won't be any conflict of interest or shady acts."
scene ep12_fparty211 with dissolve
dh "Right. But the news said you dealt in quid pro quo."
scene ep12_fparty203 with dissolve
sb "I don't know who told them that. But you have my word that it will stay a rumor - a forgotten one at that."
sb "It will not affect you or reflect on your donations in any negative way."
scene ep12_fparty207 with dissolve
wl "Stephen."
scene ep12_fparty201 with dissolve
sb "Yes?"
scene ep12_fparty207 with dissolve
wl "I'm going to hold you to that."
scene ep12_fparty202 with dissolve
$ renpy.pause()
scene ep12_fparty208 with dissolve
$ renpy.pause()
if not ep11_music:
    jump ep12_no_fparty5_label
stop music fadeout 3
play sound "sound_effects/season2/applause2.mp3"
scene ep12_fparty212 with dissolve
"*{i}Applause{/i}*"
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("IDS3_33")
    init:
        $ achievement.register("IDS3_33")
    $ achievement.Sync()
if not persistent.ep12_cardisa16:
    $ persistent.ep12_cardisa16 = True
    $ persistent.rew_isa_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
play music "music/ep11/christmas_jazz.mp3"
mc "(That's it... Phew... I made it through. And barely any mistakes at that.)"
scene ep12_fparty213 with dissolve
de "That was awesome, [mc_de]. Top-tier stuff!"
scene ep12_fparty214 with dissolve
mc "You're drinking and smoking? You should be careful around these people."
scene ep12_fparty215 with dissolve
de "Don't worry. Professor Hoff gave me the cigar and told me I could swipe some whisky."
scene ep12_fparty216 with dissolve
mc "I can't with your lies, right now."
scene ep12_fparty217 with dissolve
bru "Wow! You are talented. Your performance blew us away."
scene ep12_fparty218 with dissolve
mc "Oh, thank you..."
scene ep12_fparty217 with dissolve
bru "You can call me Bruce. And this is my wife, Ursula."
scene ep12_fparty219 with dissolve
urs "You sure brought the Christmas spirit with that."
scene ep12_fparty218 with dissolve
mc "Thank you very much! That's what I tried to do."
scene ep12_fparty217 with dissolve
bru "We were discussing when you played..."
bru "We both swore we knew you from somewhere."
bru "Tell us, did you perchance play Pachelbel's Canon in D in a video online?"
scene ep12_fparty218 with dissolve
mc "I played that song at a recital here at B&R, and someone put it online."
scene ep12_fparty220 with dissolve
urs "I told you it was him!"
scene ep12_fparty217 with dissolve
bru "Our daughter showed us that video. She would be thrilled to learn that we met you."
scene ep12_fparty219 with dissolve
urs "She went on and on about how this cute guy played our wedding song on the guitar."
scene ep12_fparty218 with dissolve
mc "Oh, you got married to it?"
scene ep12_fparty217 with dissolve
bru "Oh, like 17 years ago, when she was a child. But our daughter saw the video from it and loved that song."
scene ep12_fparty219 with dissolve
urs "Would you mind taking a picture with us? We'd love to show it to her."
scene ep12_fparty218 with dissolve
mc "Sure, I don't mind."
play sound "sound_effects/camera_shutter.mp3"
scene ep12_fparty221 with dissolve
$ renpy.pause()
scene ep12_fparty219 with dissolve
urs "Thank you so much."
scene ep12_fparty222 with dissolve
de "This guy sure can play, yeah?"
scene ep12_fparty223 with dissolve
bru "Haha, yes. He sure can."
bru "Is he a friend of yours?"
scene ep12_fparty227 with dissolve
de "Friends? Uh... We are MORE than just friends."
scene ep12_fparty226 with dissolve
urs "Oh..."
scene ep12_fparty228 with dissolve
mc "What are you saying? We are not more than friends."
scene ep12_fparty230 with dissolve
if ep9_derek_better_friend:
    de "I'm saying we're best friends."
else:
    de "I'm saying we're very close friends."
scene ep12_fparty229 with dissolve
mc "That's not how that came out."
scene ep12_fparty224 with dissolve
urs "Haha..."
scene ep12_fparty225 with dissolve
bru "Excuse us. And thank you for the music."
scene ep12_fparty231 with dissolve
mc "Why did you have to say that?"
scene ep12_fparty232 with dissolve
mc "And stop smoking indoors."

if ep11_jade_lewd:
    scene ep12_fparty233 with dissolve
    ja "Well played, [name]."
    scene ep12_fparty234 with dissolve
    mc "Thank you, Dr. Burke."
    mc "Um... Is it still Burke, by the way?"
    scene ep12_fparty235 with dissolve
    ja "Yes. We're both keeping it. It makes life in academia simpler."
    scene ep12_fparty236 with dissolve
    mc "Oh, how so?"
    scene ep12_fparty235 with dissolve
    ja "For notoriety reasons. It appears more coherent when you publish works, papers, communications, books, etc."
    scene ep12_fparty234 with dissolve
    mc "How's the party for you? I can't imagine that it's any fun having to endure Stephen being in the spotlight."
    scene ep12_fparty235 with dissolve
    ja "I didn't enjoy it when we were married either. I've gotten good at ignoring it."
    ja "As for the party, it's the same old."
    scene ep12_fparty237 with dissolve
    ja "I miss Cathy, though. We used to have a good time together at these parties."
    if ep12_cathy_lewd:
        scene ep12_fparty238 with dissolve
        ja "Speaking of Cathy..."
        scene ep12_fparty234 with dissolve
        mc "We shouldn't talk about her here..."
        scene ep12_fparty238 with dissolve
        ja "Oh, I know. You don't have to worry. I'll choose my words carefully."
        ja "I was thinking that next time, maybe we could reverse the roles."
        scene ep12_fparty234 with dissolve
        mc "I think I get what you mean. But even if I don't, I'm game."
        scene ep12_fparty238 with dissolve
        ja "Haha... You would say yes to anything. Wouldn't you?"
        scene ep12_fparty239 with dissolve
        mc "I like to party."
        scene ep12_fparty238 with dissolve
        ja "Then party we shall."
    else:
        scene ep12_fparty234 with dissolve
        mc "I miss her too."
    if branchZoey or wt_ep11_zoey_kiss_others:
        scene ep12_fparty236 with dissolve
        mc "By the way, there's something I need to talk to you about. But this isn't the place for it."
        scene ep12_fparty235 with dissolve
        ja "Leave it for another time, [name]."
    scene ep12_fparty233 with dissolve
    ja "I should continue to mingle. Have a nice evening."

if branchJill and not breakup:
    scene ep12_fparty240 with dissolve
    ji "Unsurprisingly, you were great."
    scene ep12_fparty243 with dissolve
    sa "That was so good, [name]."
    scene ep12_fparty244 with dissolve
    isa "Yes. Well done."
    scene ep12_fparty241 with dissolve
    ji "It's so easy to tell that you enjoy being on stage."
    scene ep12_fparty193 with dissolve
    mc "Yeah, I had a good time tonight. This made me want to play more."
    scene ep12_fparty241 with dissolve
    ji "You should. Share your beautiful music with others."
    scene ep12_fparty193 with dissolve
    mc "So should you."
    mc "That song you wrote for Lana... I've heard you play it before."
    scene ep12_fparty242 with dissolve
    ji "It's a special song that I wrote for her after she passed away."
    ji "I wanted to play it tonight because my parents are here. They love that song."
    scene ep12_fparty193 with dissolve
    mc "What a nice gesture."
if branchSage and not breakup:
    if (ep11_sage_love == 2 or RPsage >= 22):
        scene ep12_fparty247 with dissolve
        sa "You're the best. How do you feel?"
        scene ep12_fparty248 with dissolve
        mc "I enjoyed it. It wasn't scary at all. I can see myself doing this again."
        scene ep12_fparty247 with dissolve
        sa "You should. It felt like you belonged up there on stage."
        scene ep12_fparty248 with dissolve
        mc "I don't know about that."
    scene ep12_fparty246 with dissolve
    ji "Beautifully played, [name]."
    scene ep12_fparty244 with dissolve
    isa "It was music to my ears."
    scene ep12_fparty245 with dissolve
    mc "Haha, funny."
if branchIsabella and not breakup:
    scene ep12_fparty244 with dissolve
    isa "Simply divine."
    scene ep12_fparty246 with dissolve
    ji "Beautifully played, [name]."
    scene ep12_fparty243 with dissolve
    sa "Yeah, that was so good."
    scene ep12_fparty245 with dissolve
    mc "Aw, thank you."

if not breakup and not ep4_toldDerekAboutJade:
    scene ep12_fparty249 with dissolve
    mc "Isn't it Tybalt's turn to play next?"
    scene ep12_fparty250 with dissolve
    sa "Oh, I want to record this trainwreck."
else:
    label ep12_no_fparty5b_label:
    if not ep11_music:
        scene ep12_fparty185 with dissolve
    else:
        scene ep12_fparty251 with dissolve
    isa "I believe your brother is up next."
    if not ep11_music:
        scene ep12_fparty252b with dissolve
    else:
        scene ep12_fparty252 with dissolve
    sa "Oh, I want to record this trainwreck."

if not ep11_music:
    scene ep12_fparty257d with dissolve
else:
    scene ep12_fparty257c with dissolve
$ renpy.pause()

scene ep12_fparty253 with dissolve
isa "He brought a band?"
scene ep12_fparty254 with dissolve
sa "Lose the \"r\". I haven't seen the guy before, but I think I recognize the girl."
scene ep12_fparty253 with dissolve
isa "Oh. Do you think he hired them to play?"
scene ep12_fparty254 with dissolve
sa "Well, I doubt they are his friends."

if not ep11_music:
    scene ep12_fparty257b with dissolve
else:
    scene ep12_fparty257 with dissolve
ty "Good evening. I hope you're enjoying the Christmas party."
ty "I'm Tybalt Burke, and I'm here to bless you with a song."
ty "You'll only get one song from me tonight."
scene ep12_fparty254 with dissolve
sa "Tch. Because he could only learn one. Am I right?"
if not ep11_music:
    scene ep12_fparty257b with dissolve
else:
    scene ep12_fparty257 with dissolve
ty "But it's a special song."
ty "It's called \"To be a winner\", and I wrote it myself."
stop music fadeout 3
scene ep12_fparty258 with dissolve
nik "*{i}Whispers{/i}* Didn't you write it?"
scene ep12_fparty259 with dissolve
$ renpy.pause()
play music "music/ep12/to_be_a_winner.mp3"

if not ep11_music:
    scene ep12_fparty260b with dissolve
else:
    scene ep12_fparty260 with dissolve
$ renpy.pause()
scene ep12_fparty255 with dissolve
sa "What the fuck!? He's good!?"
scene ep12_fparty256 with dissolve
ji "When did that happen?"
ji "I'm telling you, the last time I heard him play was like listening to a bag of cats being beaten with rocks."
scene ep12_fparty255 with dissolve
sa "I'm not gonna record this."
if not ep11_music:
    scene ep12_fparty261b with dissolve
else:
    scene ep12_fparty261 with dissolve
$ renpy.pause()
scene ep12_fparty262 with dissolve
$ renpy.pause()
if not ep11_music:
    scene ep12_fparty263b with dissolve
else:
    scene ep12_fparty263 with dissolve
if ep12_nikita and ep11_music:
    mc "(Nikita?)"
    scene ep12_fparty264 with dissolve
    mc "(She plays the bass...)"
    mc "(That's so hot...)"
    scene ep12_fparty265 with dissolve
    mc "(But she's playing it with Tybalt...)"
    mc "(Why would she do that?)"
else:
    $ renpy.pause()

if not ep11_music:
    scene ep12_fparty265b with dissolve
else:
    scene ep12_fparty265a with dissolve
$ renpy.pause(10)
show screen click_to_continue_screen with dissolve
$ renpy.pause(2)
hide screen click_to_continue_screen with dissolve
$ renpy.pause()
stop music fadeout 3
play sound "sound_effects/season2/applause2.mp3"
if not ep11_music:
    scene ep12_fparty266b with dissolve
else:
    scene ep12_fparty266 with dissolve
"*{i}Applause{/i}*"
play music "music/ep11/silent_night.mp3"
if not ep11_music:
    scene ep12_fparty267b with dissolve
else:
    scene ep12_fparty267 with dissolve
ty "Thank you, everyone. Thanks for being here tonight."
ty "I want to give an extra thanks to the people I couldn't have done this without..."
scene ep12_fparty269 with dissolve
$ renpy.pause()
if not ep11_music:
    scene ep12_fparty268b with dissolve
else:
    scene ep12_fparty268 with dissolve
ty "The donors, who keep B&R well-funded and, with that, students well-educated. I applaud you."
if not ep11_music:
    scene ep12_fparty270b with dissolve
else:
    scene ep12_fparty270 with dissolve
ty "And of course, another thanks to someone who's been motivating me daily to do this..."
if not ep11_music:
    scene ep12_fparty271b with dissolve
else:
    scene ep12_fparty271 with dissolve
ty "My girlfriend Paula."
scene ep12_fparty272 with dissolve
$ renpy.pause()

scene ep12_fparty273 with dissolve
ji "*{i}Sigh{/i}* I need a drink..."
scene ep12_fparty274 with dissolve
sa "Ditto."
scene ep12_fparty275 with dissolve
isa "You go ahead. Sadly, I should mingle more tonight."
if not ep11_music:
    jump ep12_no_fparty6_label
if ep12_nikita:
    scene ep12_fparty276 with dissolve
    mc "That was something else."
    scene ep12_fparty279 with dissolve
    nik "Ditto. I watched you play before we got on."
    nik "Of course, it had to be you who played before us."
    scene ep12_fparty280 with dissolve
    nik "I started to suspect that you were following me..."
    nik "...but tonight I followed you in a sense. So, I'm torn."
    scene ep12_fparty277 with dissolve
    mc "So, you play the bass."
    scene ep12_fparty279 with dissolve
    nik "And you play the guitar."
    scene ep12_fparty277 with dissolve
    mc "Marry me."
    scene ep12_fparty281 with dissolve
    nik "Hahaha!"
    scene ep12_fparty278 with dissolve
    mc "I have to ask..."
    mc "Why do you play with...him?"
    scene ep12_fparty282 with dissolve
    nik "With Tybalt Burke?"
    nik "Well, my older brother Tim works as a music teacher, and Tybalt hired him to teach him how to play better."
    scene ep12_fparty283 with dissolve
    nik "He paid quite a handsome sum for Tim to write him a piece and to perform it here."
    nik "Tim asked me to help him out, and of course, I'll help my brother."
    scene ep12_fparty277 with dissolve
    mc "Oh, good... I thought you were friends with Tybalt or something."
    scene ep12_fparty282 with dissolve
    nik "Friends? Oh, no. Actually, we're lovers."
    scene ep12_fparty277 with dissolve
    mc "What?"
    scene ep12_fparty280 with dissolve
    nik "Or we're not lovers, and I can tell you don't like him for some reason."
    scene ep12_fparty278 with dissolve
    mc "Hahaha... You got me."
    mc "Yeah... There are reasons."
    play sound "sound_effects/season3/finger_snaps.mp3"
    scene ep12_fparty284 with dissolve
    ty "Hey. *{i}Snaps fingers{/i}* Hey, blondie!"
    ty "I paid for the entire evening."
    scene ep12_fparty282 with dissolve
    nik "I can probably guess what they are."
    nik "I'd better go before I get Tim into trouble."
    scene ep12_fparty285 with dissolve
    mc "I...um..."
    scene ep12_fparty286 with dissolve
    de "You almost had her..."
    scene ep12_fparty287 with dissolve
    mc "Were you eavesdropping?"
    scene ep12_fparty286 with dissolve
    de "What else am I gonna do here? The party sucks."
    de "You could have closed the deal with her. It's not hard."
    scene ep12_fparty288 with dissolve
    de "\"We should get together and play something.\""
    de "\"How about we meet up after?\""
    scene ep12_fparty287 with dissolve
    mc "I got tongue-tied, ok?"
    scene ep12_fparty286 with dissolve
    de "Want me to ask her?"
    scene ep12_fparty287 with dissolve
    mc "No... I'm gonna ruin this one on my own."
    $ new_bio("Nikita", "Nikita played bass at the faculty's Christmas party. She and her brother Tim were hired to perform together with Tybalt.")

scene ep12_fparty289 with dissolve
$ renpy.pause()
scene ep12_fparty290 with dissolve
dav "These Christmas parties are always the same."
scene ep12_fparty291 with dissolve
mc "I wouldn't know; it's my first. I'm a student here."
scene ep12_fparty292 with dissolve
dav "I know. I didn't mistake you for a faculty member. I watched you play before."
dav "You're talented. It was an impeccable performance you put on."
scene ep12_fparty291 with dissolve
mc "Thank you, sir."
scene ep12_fparty292 with dissolve
dav "No sirs needed. Call me David."
scene ep12_fparty291 with dissolve
if name == "David":
    mc "I'm David, too."
else:
    mc "I'm [name]."
scene ep12_fparty293 with dissolve
if name == "David":
    dav "That's easy to remember."
dav "I used to play the guitar when I was your age."
dav "The Stratocaster. That one was my favorite."
scene ep12_fparty295 with dissolve
mc "Good taste. That's a nice guitar."
mc "Are you still playing?"
scene ep12_fparty293 with dissolve
dav "I still jam, from time to time. But work has a habit of keeping me from it."
scene ep12_fparty295 with dissolve
mc "That's a shame. You should make more time for it."
mc "What line of work are you in?"
scene ep12_fparty294 with dissolve
dav "I'm in the Medtech sector."
scene ep12_fparty295 with dissolve
mc "That's interesting! I'm studying science. I think I'm going to pursue an engineering degree."
mc "Either that or a bachelor's degree. I haven't made up my mind yet."
scene ep12_fparty293 with dissolve
dav "Oh, really? That's a breath of fresh air."
dav "Most people I've talked to at this party are interested in finance."
scene ep12_fparty294 with dissolve
dav "Do you perform as well in school as you do with that guitar?"
scene ep12_fparty295 with dissolve
if (not minigames and affinity != "DIK")or (passedEnglish + passedMath + passedGender + passedEnglishS3 + passedMathS3 + passedScienceS3 > failedEnglish + failedMath + failedGender + failedEnglishS3 + failedMathS3 + failedScienceS3):
    mc "I think I'm doing well."
else:
    mc "It's tough, but I'm trying..."
scene ep12_fparty293 with dissolve
dav "Modesty is admirable. You got invited tonight. That alone speaks volumes to me."
scene ep12_fparty298 with dissolve
dav "I hated college. They made it harder than it had to be."
dav "All these redundant classes you needed to pass..."
scene ep12_fparty294 with dissolve
dav "Today, I know you should look at the person, not just the grades."
dav "If you get a good feeling from someone, follow that instinct."
dav "That's how we hire our employees. We let the gut lead."
scene ep12_fparty295 with dissolve
mc "Sounds healthy to me. When I'm applying for a job, I'd want the recruiter to be like that, for sure."
mc "And hey, that makes sense for you. Using chemistry in other aspects of your work, too."
scene ep12_fparty293 with dissolve
dav "Haha! Clever! Do you have any summer jobs lined up yet?"
scene ep12_fparty295 with dissolve
mc "Summer? It's December. All that's on my mind right now is whether I passed the finals."
scene ep12_fparty294 with dissolve
dav "I take that as a no."
dav "Well, if you're interested in Medtech, I might have something for you."
scene ep12_fparty295 with dissolve
mc "Seriously? I don't have any experience with that."
scene ep12_fparty294 with dissolve
dav "Companies want you to have 10 years of work experience when you graduate from college. It's absurd."
dav "Sometimes in life, you've got to catch a break. And I believe in passing things forward."
scene ep12_fparty295 with dissolve
mc "I'm interested, sure."
scene ep12_fparty297 with dissolve
dav "You don't even know what the job would be, but you're already interested. Haha!"
dav "That's the good feeling I was talking about."
scene ep12_fparty296 with dissolve
mc "The good feeling goes both ways."
scene ep12_fparty293 with dissolve
dav "Haha! I like it."
scene ep12_fparty299 with dissolve
dav "Well, it's a summer job. But who knows? It could lead to a career."
dav "Here. Take my card."
dav "Send me an e-mail when you get the chance, and I'll take care of it."
scene ep12_fparty295 with dissolve
mc "Can you do that?"
scene ep12_fparty297 with dissolve
dav "I own the company. I sure hope I can."
scene ep12_fparty300 with dissolve
dav "Nice to meet you, [name]."
scene ep12_fparty301 with dissolve
mc "You too, David."
scene ep12_fparty302 with dissolve
$ renpy.pause()

$ new_bio("You", "I played at the faculty's Christmas party, and it went well. After my performance, I was approached by David Cerus Baxter, who offered me a summer job at his company.")
$ new_bio("Derek", "Derek shoved Muriel Storch's trumpet up his asshole.")
$ new_bio("Tybalt", "Tybalt performed at the Christmas party, and he didn't make a fool of himself. He introduced everyone to his new girlfriend, Paula.")

label ep12_no_fparty6_label:
hide screen new_phone_screen
scene ep12_fparty303 with dissolve
ji "Thanks for coming tonight."
scene ep12_fparty304 with dissolve
sa "All things considered, it was worth it."
scene ep12_fparty312 with dissolve
ji "I'm sorry that your brother didn't suck."
scene ep12_fparty304 with dissolve
sa "Me too."
sa "He's not even walking funny anymore. He didn't embarrass himself at all tonight..."
scene ep12_fparty313 with dissolve
ji "Did he tell you how that happened to him?"
scene ep12_fparty305 with dissolve
sa "How he got injured?"
scene ep12_fparty313 with dissolve
ji "Yes... Because I'm the reason why he tore his scrotum."
scene ep12_fparty305 with dissolve
sa "Come again?"
scene ep12_fparty313 with dissolve
ji "It was me. I kicked him between his legs."
scene ep12_fparty306 with dissolve
sa "You're the hoodlum he got into a fight with?"
scene ep12_fparty314 with dissolve
ji "*{i}Sigh{/i}* It appears so."
scene ep12_fparty305 with dissolve
sa "Why did you do that to him?"
scene ep12_fparty313 with dissolve
ji "I'm not sure if you want to know why."
scene ep12_fparty305 with dissolve
sa "Well, without a reason, I don't know what to think about it."
sa "He's been hurting a lot."
scene ep12_fparty315 with dissolve
ji "He stole my underwear. And I caught him...um..."
ji "I'm going to ruin watermelons for you."
scene ep12_fparty306 with dissolve
sa "Watermelons? What's going on?"
scene ep12_fparty315 with dissolve
ji "He dressed up a watermelon with my underwear, a picture of me, and what I believe was a lock of my hair..."
ji "And I caught him pleasuring himself with it."
scene ep12_fparty307 with dissolve
sa "You're joking."
scene ep12_fparty315 with dissolve
ji "I wish. Trent was there with me."
scene ep12_fparty316 with dissolve
ji "When I saw it... I reacted to it..."
ji "And my reaction was to kick him between the legs."
scene ep12_fparty307 with dissolve
sa "I can't believe he would do that... That is so creepy."
sa "Yeah, I would have kicked him in the balls, too."
scene ep12_fparty317 with dissolve
ji "Your brother has been in love with me."
ji "He even proposed to me."
scene ep12_fparty306 with dissolve
sa "He proposed to you!?"
scene ep12_fparty315 with dissolve
ji "How do you treat someone like him?"
ji "I tried to be nice, but he kept pushing it."
ji "He told me I couldn't see [name], and he forced me to date him."
scene ep12_fparty307 with dissolve
sa "I didn't know he put you through all of that. That's disgusting."
sa "Did you tell someone about it? I'm sure it could get him into big trouble."
scene ep12_fparty316 with dissolve
ji "I told Bella and [name]."
if ep10_tybalt_mercy:
    ji "[name] told me to show him mercy."
    scene ep12_fparty308 with dissolve
    sa "[name] told you that?"
    scene ep12_fparty317 with dissolve
    ji "I believe he wanted me to take the high road."
    scene ep12_fparty308 with dissolve
    sa "I appreciate that..."
    sa "What Tybalt did was a scumbag thing to do, but..."
    scene ep12_fparty317 with dissolve
    ji "Don't you think he deserves to be punished, either?"
else:
    ji "[name] encouraged me to punish Tybalt."
    ji "I considered bringing it up to the disciplinary committee."
    scene ep12_fparty309 with dissolve
    sa "You could ruin his future..."
    scene ep12_fparty316 with dissolve
    ji "I'm aware."
    scene ep12_fparty309 with dissolve
    sa "What he did was a scumbag thing to do, but..."
    scene ep12_fparty317 with dissolve
    ji "Don't you think he deserves to be punished?"
scene ep12_fparty309 with dissolve
sa "Don't get me wrong... I hate him."
sa "But he's my brother. I get to do that."
scene ep12_fparty310 with dissolve
sa "And my family isn't strong right now."
sa "We could use less drama surrounding us..."
scene ep12_fparty317 with dissolve
ji "I understand."
scene ep12_fparty310 with dissolve
sa "Is Tybalt still being a pain in your ass?"
scene ep12_fparty317 with dissolve
ji "Not since I caught him with my fruity alter ego."
ji "He's going out of his way to ignore me now."
scene ep12_fparty311 with dissolve
sa "Well, that's better. And now that he has a girlfriend, he might leave you alone."
sa "He gloated a lot about Paula over Christmas."
scene ep12_fparty316 with dissolve
ji "I hope he has moved on then."
scene ep12_fparty311 with dissolve
sa "Thanks for confiding in me. It couldn't have been easy."
scene ep12_fparty318 with dissolve
ji "You make it easy. You're so outspoken and unafraid to say what you think."
ji "I wish I were the same."
scene ep12_fparty319 with dissolve
sa "You have qualities that I could use as well."
scene ep12_fparty318 with dissolve
ji "Like what?"
scene ep12_fparty319 with dissolve
sa "You're level-headed and so fucking nice."
scene ep12_fparty318 with dissolve
ji "You're nice too."
if branchSage and not breakup and (ep11_sage_love == 1 or RPsage < 22):
    scene ep12_fparty308 with dissolve
    sa "Thanks..."
    scene ep12_fparty310 with dissolve
    sa "Um... There's something I'd like to run by you, too. I could use some advice."
    scene ep12_fparty312 with dissolve
    ji "What about?"
    scene ep12_fparty309 with dissolve
    sa "It's about [name]."
    scene ep12_fparty313 with dissolve
    ji "Oh? Is something wrong?"
    stop music fadeout 3
    scene ep12_fparty321 with dissolve
    $ renpy.pause()
else:
    stop music fadeout 3
    scene ep12_fparty320 with dissolve
    $ renpy.pause()

label ep12_stephen_label:
$ guideSuggestedPage = 258
play music "music/ep8/licensed_music/track63.mp3"
scene ep12_stephen1 with fade
sb "Wallace! It's been years since I heard your voice. How have you been?"
scene ep12_stephen2 with dissolve
sb "Oh, haha! You saw that?"
sb "Yeah, what can I tell you? Journalists... They always fixate on something you said in passing."
scene ep12_stephen3 with dissolve
sb "No, it is true. I am indeed a big part of that process, but it's not going nearly as well as they worded it."
sb "Securing funds is hard work, and there is always a need for more."
scene ep12_stephen4 with dissolve
sb "He did? Yes, I kept Levenson in my social network, but I can assure you, there's no conflict of interest or anything."
show ep12_stephen5
if not persistent.ep12_cardcam16:
    show screen ep12_render_screen("cam16")
with dissolve
sb "Good, I didn't want you to think that I'm competing for your clients. I've got my own thing going on here."
sb "There's nothing fishy about it. I never did those things; I'm sure you remember."
show ep12_stephen6
hide screen ep12_render_screen
with dissolve
sb "Well, Levenson's had a great year and needed a write-off."
sb "The donation is for a good cause, and he wanted to thank me for what I did for him in the past."
scene ep12_stephen7 with dissolve
sb "Haha! Yes! Symbiosis. You remembered."
scene ep12_stephen6 with dissolve
sb "Oh, right. I believe they wrote that in the newspaper."
scene ep12_stephen3 with dissolve
sb "Yeah, I heard. It took some time, but that trade I suggested to Levenson came through. I made a killing on it myself."
sb "If you only had trusted my analysis, haha..."
scene ep12_stephen4 with dissolve
sb "Sure, I'd be thrilled to have lunch with you. But let me say this up front, you're not getting me back."
sb "I'm done with that life, and I'd like to keep whatever hair I have left rather than lose it to stress."
scene ep12_stephen2 with dissolve
sb "Haha! Great! Tomorrow then."

scene ep12_stephen84 with fade
sb "Time's out. Pencils down."
sb "Turn in your papers before you leave."
scene ep12_stephen85 with dissolve
pris "You put some tough questions in there, professor."
scene ep12_stephen86 with dissolve
sb "I don't make the questions. Blame it on B&R's test system."
scene ep12_stephen87 with dissolve
pris "Hopefully, I'll pass."
scene ep12_stephen88 with dissolve
sb "..."
scene ep12_stephen8 with dissolve
ca "Another year, but it feels like the same old students."
scene ep12_stephen9 with dissolve
sb "Having a couple of retakes?"
scene ep12_stephen11 with dissolve
ca "Mhm... Several."
scene ep12_stephen10 with dissolve
sb "Maybe they keep coming back because they like you as a teacher so much?"
scene ep12_stephen12 with dissolve
ca "Haha! Good one!"
ca "I'll see you on Monday. Don't stay too late correcting tests."
scene ep12_stephen13 with dissolve
$ renpy.pause()
play sound "sound_effects/cellphone.mp3"
scene ep12_stephen14 with dissolve
"*{i}Phone rings{/i}*"
scene ep12_stephen15 with dissolve
sb "Wallace... Thanks again for lunch the other day."
scene ep12_stephen16 with dissolve
sb "I thought about your offer, but I have to decline."
sb "I think you know why, but if you need me to enlighten you..."
scene ep12_stephen17 with dissolve
sb "Frankly, I don't believe for a second that the money you'd donate is fair game. We both know how you operate."
scene ep12_stephen18 with dissolve
sb "I believe you'd use B&R as a funnel, putting in dirty money and getting white write-offs."
sb "Furthermore, it sounded like you wanted me to scout for talented students and introduce them to your firm, which would create a potential quid pro quo."
scene ep12_stephen17 with dissolve
sb "Tell me how close I was with that assessment?"
sb "I realize I would look good procuring that sizeable donation, but I'm doing fine without it."
scene ep12_stephen16 with dissolve
sb "Yes, I did say that we need more money for scholarships, but-"
sb "You can tell me to think about it all you want, but I won't change my mind on this."
scene ep12_stephen15 with dissolve
sb "Have a good evening, Mr. Wallace."
scene ep12_stephen19 with dissolve
$ renpy.pause()

play sound "sound_effects/door_knock.mp3"
scene ep12_stephen20 with dissolve
"*{i}Door knock{/i}*"
scene ep12_stephen21 with dissolve
sb "Yes? Come on in."
scene ep12_stephen22 with dissolve
pris "Hi, Professor."
scene ep12_stephen24 with dissolve
sb "Priscilla... Why are you still here? It's Friday. Off and enjoy your weekend."
scene ep12_stephen23 with dissolve
pris "Says you. Do you always work this late?"
scene ep12_stephen24 with dissolve
sb "When work calls for it, I have to find time to correct the tests, and I don't like to procrastinate."
scene ep12_stephen26 with dissolve
pris "Oh, right... The tests..."
scene ep12_stephen25 with dissolve
$ renpy.pause()
scene ep12_stephen27 with dissolve
$ renpy.pause()
scene ep12_stephen28 with dissolve
sb "Uh... Priscilla. What can I do for you?"
scene ep12_stephen29 with dissolve
pris "Look, I'm going to level with you."
scene ep12_stephen30 with dissolve
pris "That test today... I flunked it. Hard."
scene ep12_stephen31 with dissolve
sb "Maybe you did, maybe you didn't? I haven't corrected your test yet, but you never know-"
scene ep12_stephen32 with dissolve
pris "Exactly! You never know, right?"
scene ep12_stephen33 with dissolve
pris "Thing is...I didn't even answer any of the questions. I doodled on my papers because I didn't know any of the answers."
scene ep12_stephen34 with dissolve
sb "Ah. That's a different story, then."
scene ep12_stephen35 with dissolve
pris "But...you never know... Right?"
scene ep12_stephen36 with dissolve
sb "Priscilla, did you want something?"
scene ep12_stephen37 with dissolve
pris "I talked to my friends about how they get out of these situations, and they say professors are often nice to them..."
pris "They offer them these extracurricular activities and whatnot to boost their grades."
scene ep12_stephen38 with dissolve
sb "Did you come here looking to get a bump on your grade?"
scene ep12_stephen37 with dissolve
pris "You're smart. I bet that's why you are a professor, haha."
scene ep12_stephen38 with dissolve
sb "I can't bump your grade if you're not passing to begin with."
sb "The extracurricular activities you mentioned are for students who are close to earning a different grade."
scene ep12_stephen39 with dissolve
sb "They aren't used as a Hail Mary to get out of a failing grade. You need to put in effort, too."
scene ep12_stephen40 with dissolve
pris "I put in effort."
scene ep12_stephen42 with dissolve
$ renpy.pause()
scene ep12_stephen41 with dissolve
sb "Priscilla... What are you doing?"
scene ep12_stephen43 with dissolve
pris "Putting in the effort."
scene ep12_stephen44 with dissolve
pris "I've noticed how you watch me in class."
scene ep12_stephen45 with dissolve
sb "I'm your teacher; I watch all of my students."
scene ep12_stephen46 with dissolve
pris "Not in the way you've been watching me. Your eyes wander all over my body. Undressing me with your gaze."
scene ep12_stephen47 with dissolve
pris "Looking up my skirt when I sit at my desk..."
scene ep12_stephen48 with dissolve
pris "All I'm asking for is a passing grade. It's not much... Surely, you can do that?"
pris "And in return..."
scene ep12_stephen49 with dissolve
pris "I'll let you fuck me right now."
pris "I'll let you do every naughty thing that enters your head in class while watching me."
scene ep12_stephen50 with dissolve
pris "Ever did it with a college student, professor?"
scene ep12_stephen51 with dissolve
pris "Pull down your pants and let's have some fun."
play sound "sound_effects/zipper.mp3"
scene ep12_stephen52 with dissolve
$ renpy.pause()
scene ep12_stephen53 with dissolve
pris "*{i}Moans{/i}*"
scene ep12_stephen54 with dissolve
$ renpy.pause()
scene ep12_stephen55 with dissolve
$ renpy.pause()

scene ep12_stephen79 with dissolve
sb "Hello."
scene ep12_stephen80 with dissolve
ja "You missed dinner."
scene ep12_stephen81 with dissolve
sb "Sorry, I fell asleep correcting tests."
scene ep12_stephen80 with dissolve
ja "You went out drinking, didn't you?"
scene ep12_stephen81 with dissolve
sb "Yeah, you got me."
scene ep12_stephen82 with dissolve
sb "Shit..."
stop music fadeout 3
scene ep12_stephen83 with dissolve
$ renpy.pause()

play music "music/ep11/licensed_music/track155.mp3"
scene ep12_stephen56 with fade
pris "Professor Burke?"
scene ep12_stephen57 with dissolve
sb "What do you want?"
scene ep12_stephen59 with dissolve
pris "I wanted to say thank you for the nice grade."
pris "B plus, huh? You went the extra mile."
scene ep12_stephen58 with dissolve
sb "You earned it. Your test result was good."
scene ep12_stephen59 with dissolve
pris "I sent you an e-mail. I think you should read it."
scene ep12_stephen57 with dissolve
sb "Ok...?"
scene ep12_stephen60 with dissolve
pris "*{i}Moans{/i}* Professor Burke! Fuck me!"
play sound "sound_effects/season3/bn_click.mp3"
sb "Priscilla! What the hell!?"
scene ep12_stephen61 with dissolve
pris "I've been a bad girl, Professor."
scene ep12_stephen62 with dissolve
sb "What is this?"
scene ep12_stephen61 with dissolve
pris "The title of my sextape? Oh... I've dubbed it \"Priscilla's free ride through college\"."
scene ep12_stephen62 with dissolve
sb "Your free ride through college?"
scene ep12_stephen61 with dissolve
pris "Do you like it?"
scene ep12_stephen63 with dissolve
sb "What the hell are you up to?"
scene ep12_stephen64 with dissolve
pris "Thanks for the grade and all, but I think you can do me one better."
scene ep12_stephen63 with dissolve
sb "Are you blackmailing me?"
scene ep12_stephen64 with dissolve
pris "Me? No, I'm the poor student victim who had to fuck her professor to pass his class."
pris "I didn't do well at all on my tests, and he forced me to do unspeakable things."
scene ep12_stephen65 with dissolve
sb "What do you want from me? I can't change any other grades for you."
sb "You're not in any of my other classes; I don't have that power."
scene ep12_stephen66 with dissolve
pris "That's not the free ride I had in mind."
pris "I saw the great work you do for B&R in the newspaper."
scene ep12_stephen67 with dissolve
pris "You provide scholarships to all kinds of students. Impressive stuff..."
pris "Perhaps if you look hard enough, you'll find one suitable for me?"
scene ep12_stephen68 with dissolve
sb "It doesn't work like that. You need funding and planning, and-"
scene ep12_stephen69 with dissolve
pris "Oh, I think it does work like that. You'll make it work like that."
pris "Or that sextape of ours will find its way to another e-mail address."
scene ep12_stephen70 with dissolve
pris "Off the top of my head, I'm thinking the student mailing list."
pris "For starters. But I doubt I'd need to send it to someone else after I do that."
scene ep12_stephen68 with dissolve
sb "Priscilla, you can't do this to me."
sb "And you shouldn't do this to yourself either. Think about your future."
scene ep12_stephen70 with dissolve
pris "I am thinking about my future. How do you like {b}this{/b} for effort?"
scene ep12_stephen69 with dissolve
pris "You should have thought about your future before you fucked an innocent student in exchange for a grade bump."
pris "Let me know when you've made your decision. Sooner, rather than later."
scene ep12_stephen71 with dissolve
$ renpy.pause()

scene ep12_stephen72 with dissolve
sb "That fucking... That fucking bitch!"
scene ep12_stephen73 with dissolve
$ renpy.pause()
scene ep12_stephen74 with dissolve
$ renpy.pause()
scene ep12_stephen75 with dissolve
$ renpy.pause()
scene ep12_stephen76 with dissolve
$ renpy.pause()
scene ep12_stephen77 with dissolve
sb "Wallace... Haha! It's me."
scene ep12_stephen78 with dissolve
sb "You were right... I've thought some more about your offer and reached clarity."
stop music fadeout 3
sb "I'll do it. But I have some conditions of my own."

jump ep12_freeroam_np_label

label ep12_evaluation_label:
if not minigames:
    stop music fadeout 3
scene black with fade
if not minigames:
    $ renpy.pause(2)
else:
    $ renpy.pause(0.5)
hide screen new_phone_screen

if minigames:
    $ renpy.block_rollback()
    $ pp_continue_label = "ep12_pp_cont2_label"

    if ep12_pp_food == 0:
        $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
        $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
        $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
        $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
        $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
        $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Fancy Buffet{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    elif ep12_pp_food == 1:
        $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
        $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
        $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}Decent Buffet{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Decent Buffet{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Decent Buffet{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    else:
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-2,0)
        $ pp_happiness_level[1] = max(pp_happiness_level[1]-2,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-2,0)
        $ pp_happiness_level[3] = max(pp_happiness_level[3]-2,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-2,0)
        $ pp_happiness_level[5] = max(pp_happiness_level[5]-2,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-2,0)
        $ pp_happiness_level[7] = max(pp_happiness_level[7]-2,0)

        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Derek's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Jacob's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Jamie's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased John Boy's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Leon's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased [name]'s happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Rusty's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Cheap Buffet{/color} activity decreased Tommy's happiness by {color=ff0000}-2%{/color}.")

    if ep12_pp_game == 0:
        $ pp_happiness_level[0] = min(pp_happiness_level[0]+2,100)
        $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
        $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
        $ pp_happiness_level[6] = min(pp_happiness_level[6]+2,100)
        $ mphone_pp_history_list.append("• The {color=ffed00}Card Game{/color} activity increased Derek's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Card Game{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Card Game{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}Card Game{/color} activity increased Rusty's happiness by {color=00ff00}+2%{/color}.")
    else:
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-2,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-2,0)
        $ pp_happiness_level[5] = max(pp_happiness_level[5]-2,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-2,0)
        $ mphone_pp_history_list.append("• No {color=ffed00}Card Game{/color} activity decreased Derek's happiness by {color=00ff00}-2%{/color}.")
        $ mphone_pp_history_list.append("• No {color=ffed00}Card Game{/color} activity decreased Jamie's happiness by {color=00ff00}-2%{/color}.")
        $ mphone_pp_history_list.append("• No {color=ffed00}Card Game{/color} activity decreased [name]'s happiness by {color=00ff00}-2%{/color}.")
        $ mphone_pp_history_list.append("• No {color=ffed00}Card Game{/color} activity decreased Rusty's happiness by {color=00ff00}-2%{/color}.")

    if ep12_pp_fireworks != 2:
        if ep12_pp_fireworks == 0:
            $ pp_happiness_level[0] = min(pp_happiness_level[0]+3,100)
            $ pp_happiness_level[1] = min(pp_happiness_level[1]+3,100)
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+3,100)
            $ pp_happiness_level[3] = min(pp_happiness_level[3]+3,100)
            $ pp_happiness_level[4] = min(pp_happiness_level[4]+3,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+3,100)
            $ pp_happiness_level[6] = min(pp_happiness_level[6]+3,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+3,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Derek's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Jacob's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Jamie's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased John Boy's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Leon's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased [name]'s happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Rusty's happiness by {color=00ff00}+3%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Fireworks{/color} activity increased Tommy's happiness by {color=00ff00}+3%{/color}.")
        elif ep12_pp_fireworks == 1:
            $ pp_happiness_level[2] = min(pp_happiness_level[2]+2,100)
            $ pp_happiness_level[3] = min(pp_happiness_level[3]+2,100)
            $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
            $ pp_happiness_level[5] = min(pp_happiness_level[5]+2,100)
            $ mphone_pp_history_list.append("• The {color=ffed00}Some Fireworks{/color} activity increased Jamie's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Some Fireworks{/color} activity increased John Boy's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Some Fireworks{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}Some Fireworks{/color} activity increased [name]'s happiness by {color=00ff00}+2%{/color}.")
    else:
        $ pp_happiness_level[0] = max(pp_happiness_level[0]-2,0)
        $ pp_happiness_level[1] = max(pp_happiness_level[1]-2,0)
        $ pp_happiness_level[2] = max(pp_happiness_level[2]-2,0)
        $ pp_happiness_level[3] = max(pp_happiness_level[3]-2,0)
        $ pp_happiness_level[4] = max(pp_happiness_level[4]-2,0)
        $ pp_happiness_level[5] = max(pp_happiness_level[5]-2,0)
        $ pp_happiness_level[6] = max(pp_happiness_level[6]-2,0)
        $ pp_happiness_level[7] = max(pp_happiness_level[7]-2,0)

        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Derek's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Jacob's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Jamie's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased John Boy's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Leon's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased [name]'s happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Rusty's happiness by {color=ff0000}-2%{/color}.")
        $ mphone_pp_history_list.append("• The {color=ffed00}No Fireworks{/color} activity decreased Tommy's happiness by {color=ff0000}-2%{/color}.")

    $ specialMessage = "DIKs' happiness changed!"
    $ pp_update_happiness_icons()
    show screen specialmsg
    $ renpy.pause(2)
    hide screen specialmsg
    jump party_planner_setup_evaluation_label
    label ep12_pp_cont2_label:
    $ renpy.block_rollback()

    $ tmpStr = ""
    if ep12_pp_food == 2:
        $ tmpStr += "• Cheap buffet "
    elif ep12_pp_food == 1:
        $ tmpStr += "• Decent buffet "
    else:
        $ tmpStr += "• Fancy buffet "
    if ep12_pp_game == 0:
        $ tmpStr += "• Card game "
    if ep12_pp_fireworks == 2:
        $ tmpStr += "• No fireworks"
    elif ep12_pp_fireworks == 1:
        $ tmpStr += "• Some fireworks"
    else:
        $ tmpStr += "• Fireworks"

    $ mphone_pp_history_list.append("DIKs' New Year's Eve party\n{color=fe9416}Activities:{/color} %s\n{color=fe9416}Total Party Score:{/color} {color=ffed00}%d{/color}\n{color=fe9416}Total Score:{/color} {color=ffed00}%d{/color}\n{color=e51475}Multiplier: [pp_multiplier]x{/color}\n{color=fe9416}Rank:{/color} {color=ffed00}%s{/color}" % (tmpStr,pp_round_score,pp_score,pp_party_rank[3][1]))
    $ mphone_pp_history_list.append("\n")
    $ mphone_pp_history_list.append("\n")

    if steamAchievements:
        if pp_party_rank[3][0]==12 and pp_party_rank[3][1]=="S":
            $ achievement.grant("IDS3_23")
            init:
                $ achievement.register("IDS3_23")
            $ achievement.Sync()
    if steamAchievements:
        if pp_party_rank[0][1] == "S" and pp_party_rank[1][1] == "S" and pp_party_rank[2][1] == "S" and pp_party_rank[3][1] == "S":
            $ achievement.grant("IDS3_24")
            init:
                $ achievement.register("IDS3_24")
            $ achievement.Sync()
else:
    $ party_planner_get_nm_rank(pp_current_party_happiness)
    $ party_planner_get_nm_score(pp_nm_dik_happiness)
if minigames:
    stop music fadeout 3
    scene black with fade
    $ renpy.pause(2)
show screen new_phone_screen
$ mphone_music_genre = 3
$ mphone_play_songs(["music/ep12/licensed_music/track216.mp3"])
scene ep12_end_party1 with dissolve
if breakup or roadMayaJosy:
    mc "{i}Happy New Year...{/i}"
else:
    mc "{i}Happy New Year.{/i}"
mc "{i}January 1st has got to be the weirdest day of the year.{/i}"
mc "{i}A new year has begun, and with all the resolutions promising big changes, many start the year off by feeling like shit.{/i}"
scene ep12_end_party2 with dissolve
mc "{i}It's like we're telling ourselves to have one more day before the new year truly begins...{/i}"
mc "{i}Let's celebrate the new year by throwing up and sleeping until afternoon.{/i}"
scene ep12_end_party3 with dissolve
le "Fuck..."
if ep10_nora_lewd:
    scene ep12_end_party5 with dissolve
    mc "{i}For different reasons.{/i}"
    scene ep12_end_party4 with dissolve
    $ renpy.pause()
label ep12_rio_end_label:
hide screen new_phone_screen
scene ep12_rio_end1 with dissolve
$ renpy.pause()
scene ep12_rio_end2 with dissolve
cam "*{i}Yawns{/i}*"
scene ep12_rio_end3 with dissolve
cam "Rio?"
scene ep12_rio_end4 with dissolve
ri "Hey..."
scene ep12_rio_end3 with dissolve
cam "You're back."
scene ep12_rio_end4 with dissolve
ri "For now."
scene ep12_rio_end3 with dissolve
cam "Huh? What's that supposed to mean?"
scene ep12_rio_end5 with dissolve
$ renpy.pause()
scene ep12_rio_end6 with dissolve
cam "Rio... What happened to you?"
scene ep12_rio_end7 with dissolve
ri "I take it the makeup fooled you last night."
scene ep12_rio_end8 with dissolve
cam "Who did this to you?"
scene ep12_rio_end11 with dissolve
ri "Quinn by proxy."
scene ep12_rio_end8 with dissolve
cam "What!?"
scene ep12_rio_end11 with dissolve
ri "Cammy... Quinn is dangerous."
ri "I can't let this happen to you or anyone else involved with her... It's gone too far."
scene ep12_rio_end12 with dissolve
ri "I'm here because I need to ask you a big favor."
scene ep12_rio_end9 with dissolve
cam "Anything."
scene ep12_rio_end12 with dissolve
ri "I need your help."
scene ep12_rio_end9 with dissolve
cam "With what?"
scene ep12_rio_end13 with dissolve
ri "To give Quinn what she deserves."
scene ep12_rio_end10 with dissolve
cam "..."
scene ep12_rio_end9 with dissolve
cam "Tell me everything."
scene ep12_rio_end14 with dissolve
$ renpy.pause()
jump ep12_freeroam_room3_label

label ep12_sally_end_label:
$ guideSuggestedPage = 274
scene ep12_sally_end100 with dissolve
$ renpy.pause()
scene ep12_sally_end101 with dissolve
if ep12_sally_lewd:
    mc "Sally? What a nice surprise. Thanks for last night."
else:
    mc "Sally? What are you doing here?"
scene ep12_sally_end102 with dissolve
sy "You're in deep shit, [name]."
scene ep12_sally_end103 with dissolve
mc "What did I do now?"
scene ep12_sally_end102 with dissolve
sy "Not you. Your entire frat is in deep shit."
scene ep12_sally_end103 with dissolve
mc "What's going on?"
scene ep12_sally_end104 with dissolve
sy "I'm not supposed to tell you this... I didn't think I'd ever do it either, but...but..."
scene ep12_sally_end105 with dissolve
mc "Sally... Slow down. Tell me what's wrong."
scene ep12_sally_end106 with dissolve
sy "You're going to hate me."
scene ep12_sally_end105 with dissolve
mc "Look, you and I started things out rough, but it's been going well lately."
mc "I don't hate you. I like you."
scene ep12_sally_end106 with dissolve
sy "And that's why this sucks. I like you too."
sy "It's been ingrained in me not to like you or any of the DIKs, but... I can't do this anymore."
scene ep12_sally_end107 with dissolve
mc "What are you talking about?"
scene ep12_sally_end109 with dissolve
sy "The tri-betas have been plotting behind your back, and now they're out to get you."
scene ep12_sally_end107 with dissolve
mc "The tri-betas?"
scene ep12_sally_end109 with dissolve
sy "They are bringing the other frats together now as we speak. They are going to report you to the counselors and get you banned."
scene ep12_sally_end107 with dissolve
mc "What!? What did we do?"
scene ep12_sally_end108 with dissolve
sy "I don't know where to start."
scene ep12_sally_end107 with dissolve
mc "Start from the beginning."
scene ep12_sally_end108 with dissolve
sy "It's a long story."
scene ep12_sally_end107 with dissolve
mc "Tell me what you know."
scene ep12_sally_end109 with dissolve
sy "It all started before I came here."
sy "Back when this mansion belonged to the tri-betas."
scene ep12_sally_end107 with dissolve
mc "This mansion!?"
play music "music/ep12/licensed_music/track213.mp3"
scene ep12_sally_end1 with dissolve
sy "The tri-betas had been renting it for years, but the property owner increased the rent to ludicrous levels."
sy "And when the tri-betas struggled to make payments, all of a sudden, the property owner decided to sell it."
sy "Naturally, the fraternity didn't have the money to acquire it. They tried to deal with the owner to extend the lease, but they couldn't change his mind."
scene ep12_sally_end18 with dissolve
sy "Do you know Richard Syles?"
mc "I don't think I do."
scene ep12_sally_end19 with dissolve
sy "He's the vice president of Alpha Nu Omega."
mc "Oh! Rich? That blonde guy?"
show ep12_sally_end16
if not persistent.ep12_cardcam18:
    show screen ep12_render_screen("cam18")
with dissolve
sy "Yes. His father owned this mansion."
sy "The tri-betas tried to plead to Rich for help, but the Alpha Nu Omegas laughed in their faces."
show ep12_sally_end17
hide screen ep12_render_screen
with dissolve
sy "They couldn't care less about what happened to the tri-betas."
scene ep12_sally_end20 with dissolve
sy "And then you guys came. Rusty's dad bought the mansion. And just like that, the tri-betas were vacated on short notice."
sy "They were ordered to leave, and everything inside the mansion was included in the purchase."
scene ep12_sally_end21 with dissolve
sy "They were livid about it. They saw it as being kicked out by both the Alpha Nu Omegas and the DIKs."
scene ep12_sally_end22 with dissolve
sy "And now they were forced to live in dorms like commoners. What kind of a fraternity lives in dorms!?"
sy "But that was merely the start of their problems."
sy "And here comes the big one... And I swore to them that I'd never tell anyone about it."
scene ep12_sally_end110 with dissolve
sy "But they have treated me like disposable waste, and now that you have shown me you guys aren't as bad as I thought..."
sy "I have to tell you."
scene ep12_sally_end109 with dissolve
sy "But you have to promise me this stays between us. I'd be in so much trouble if it doesn't."
sy "And not just me... The tri-betas, too."
scene ep12_sally_end107 with dissolve
mc "You're trusting me with a secret because you see me as a friend."
mc "I'm not going to betray your trust. I'll put your best interest first, since that's what you're doing with the DIKs and me now."
scene ep12_sally_end111 with dissolve
sy "Thank you..."
scene ep12_sally_end112 with dissolve
sy "It's all because of what's on your desk."
scene ep12_sally_end113 with dissolve
mc "My desk?"
scene ep12_sally_end114 with dissolve
$ renpy.pause()
scene ep12_sally_end115 with dissolve
sy "It's because of this."
scene ep12_sally_end116 with dissolve
sy "The Pandora's box that caused all of it."
sy "Where did you find it?"
scene ep12_sally_end117 with dissolve
mc "That box? I found it in here when I was cleaning up to make the room inhabitable."
mc "I put it aside because it struck me as something special. But I didn't think much more about it until later."
if pb_completed:
    mc "And not that long ago, I opened it. But there's nothing inside of it, Sally. It's empty."
else:
    mc "And not that long ago, Derek opened it. But there's nothing inside of it, Sally. It's empty."
scene ep12_sally_end120 with dissolve
$ renpy.pause()
scene ep12_sally_end119 with dissolve
sy "This is the tri-betas' best-kept secret. Not everyone of the tri-betas even knows of its existence."
scene ep12_sally_end118 with dissolve
sy "This box belonged to Duke, the tri-beta president before Magnar."
sy "And in it, he kept something so valuable and illegal that he feared the consequences if someone else found out about it."
stop music fadeout 3
scene ep12_sally_end117 with dissolve
mc "What was in it?"
scene ep12_sally_end118 with dissolve
sy "That's the next part of the story..."
play music "music/ep12/licensed_music/track214.mp3"
scene ep12_sally_end2 with dissolve
sy "Duke wasn't like the other tri-betas. And he wasn't like any of the fraternity presidents you'd ever seen."
sy "He was this short and skinny guy, but still managed to rule the tri-betas with an iron hand."
sy "And how?"
scene ep12_sally_end3 with dissolve
sy "Because he was the smartest tri-beta you'd ever seen."
sy "And the other tri-betas admired Duke for his brilliance."
scene ep12_sally_end4 with dissolve
sy "And Magnar was his biggest admirer and suck-up."
scene ep12_sally_end5 with dissolve
sy "Duke would cockily describe himself as a big party guy. And whenever the tri-betas hosted a party, he'd be the first one trying to get laid."
sy "I have heard others describe him as a nerd with a filthy mind who could only get with girls because of his presidential title."
scene ep12_sally_end6 with dissolve
sy "But mostly, Duke was known for his computer and technical skills."
scene ep12_sally_end6b with dissolve
sy "Today, he's working as a lead programmer at a billion-dollar company in Silicon Valley."
scene ep12_sally_end7 with dissolve
sy "Duke graduated with the highest possible grades from B&R... but you wouldn't guess why."
scene ep12_sally_end7b with dissolve
$ renpy.pause()
scene bg anim_box_ep12 movie with dissolve
sy "By the time Duke graduated, Magnar had earned Duke's trust and friendship."
sy "Duke passed the presidential title and the puzzle box onto Magnar."
sy "Magnar was told to keep the box to himself and never to disclose its content or where he got it from to anyone."
scene bg anim_box2_ep12 movie with dissolve
sy "Duke's one mistake during his time at B&R was thinking that Magnar would honor his wish."
sy "After Magnar found out what was in the box, he saw the power he could wield."
sy "As if being the president of the fraternity wasn't good enough, he wanted to ensure that his fratmates would be completely loyal to him."
sy "To accomplish this, Magnar chose to let his closest friends in on it."
scene ep12_sally_end24 with dissolve
sy "And when I got together with him, he let me in on its secrets, too."
scene ep12_sally_end25 with dissolve
sy "But there was a big problem..."
sy "He had lost that box in this mansion."
scene ep12_sally_end10 with dissolve
sy "He used to keep it in this room, on a bookshelf behind books."
scene ep12_sally_end11 with dissolve
sy "Magnar was paranoid that someone would find it or that someone who knew about its existence would steal it, so he'd frequently change the hiding spot."
sy "Never finding a perfect place for it."
scene ep12_sally_end12 with dissolve
sy "The day the tri-betas were evicted, they packed their belongings and left."
sy "But Magnar - that idiot - forgot to bring the box with him."
scene ep12_sally_end14 with dissolve
sy "When he realized his mistake, he needed to get back inside the mansion to get it."
sy "But the DIKs had already moved in and wouldn't let him enter."
scene ep12_sally_end15 with dissolve
sy "He pleaded to Rusty and Tommy to let him in for a minute or two, but they didn't trust his intentions and refused."
scene bg anim_box4_ep12 movie with dissolve
sy "He thought he had lost the box, and he had to make peace with it."
pause
scene ep12_sally_end13 with dissolve
mc "You have to tell me... What was in the box?"
scene bg anim_box3_ep12 movie with dissolve
sy "A USB stick."
mc "A USB stick? That's it?"
sy "A golden USB stick with the entire database that B&R uses to generate their tests and exams."
sy "It has the answers and questions to all the tests."
scene ep12_sally_end8 with dissolve
sy "And I don't know if you're aware, but B&R barely updates those databases."
sy "Why waste time and money on changing perfect questions and answers to classes that have the same curriculum?"
sy "They can reuse everything and create new tests from a new mix of questions and answers. It saves them both time and money."
sy "And that USB stick held the key to getting perfect scores on every test. You could graduate as an A student with ease."
scene ep12_sally_end9 with dissolve
sy "Just like Duke."
sy "Duke managed to access the B&R database and downloaded everything onto that USB stick."
scene ep12_sally_end121 with dissolve
mc "Holy shit... You weren't kidding. That's huge..."
scene ep12_sally_end122 with dissolve
sy "I know!"
sy "So much for Duke's brilliant mind."
sy "And Magnar followed in Duke's footsteps, relying on the USB stick for his college classes."
scene ep12_sally_end23 with dissolve
sy "Magnar had printed out questions and answers to the classes he was taking at the time he lost the USB stick."
sy "But after he passed those classes, he couldn't get the answers for his next semester because he didn't have the box."
scene ep12_sally_end26 with dissolve
sy "And that's when reality hit him. Magnar wasn't an A student. He wasn't THAT smart."
sy "He needed that database to excel, and he felt the pressure."
scene ep12_sally_end23 with dissolve
sy "Magnar has tried to rebuild the knowledge of the USB stick by buying old tests and notes from students."
sy "He also did that to stay in charge and keep his fratmates' trust."
sy "But whatever he could get from students would never measure up to the B&R database."
scene ep12_sally_end27 with dissolve
sy "Magnar reached out to Duke, but he wouldn't help him retrieve the database. And the USB stick had the only copy of it."
scene ep12_sally_end28 with dissolve
sy "Enter me..."
sy "Magnar gave me what he had printed for my first semester here. And I, too, aced my classes."
scene ep12_sally_end28b with dissolve
sy "And I know he's helped new fratmates pass their tests in the same way, too."
sy "He has enticed them with perfect grades in exchange for loyalty - all to keep ruling the tri-betas the way he wants."
sy "If he has dirt on everyone in the frat, they must obey him. He only accepted new pledges if he sensed that a member could be manipulated."
scene ep12_sally_end29 with dissolve
sy "Magnar got the idea to use me to get the box back."
scene ep12_sally_end30 with dissolve
sy "I started partying with the DIKs, and for the first time since they left the mansion, the tri-betas had someone on the inside of it again."
scene ep12_sally_end32 with dissolve
sy "Imagine my surprise when I walked into this room and saw heavy bookshelves on the floor and an inhabitable mess."
scene ep12_sally_end31 with dissolve
sy "The room reeked of piss, and trash littered every corner."
mc "Yeah, I remember how it looked."
scene ep12_sally_end33 with dissolve
sy "I couldn't find the damned box in here, and I wasn't strong enough to move shelves around."
sy "And the bookshelves that were still standing had so many books in them that it would have taken me hours to scour through them without drawing suspicion."
scene ep12_sally_end34 with dissolve
sy "I attempted it multiple times without luck."
sy "Magnar started suspecting that you guys had already found the box..."
scene ep12_sally_end35 with dissolve
sy "And that's when he wanted access to any computer you had to check for himself."
sy "A tall order... But after some digging, I found out that you guys had a laptop and were sharing and synchronizing files on your phones."
scene ep12_sally_end36 with dissolve
sy "Magnar told me to get hold of a phone by any means necessary."
scene ep12_sally_end37 with dissolve
sy "And I did..."
if ep2_danceSage:
    scene ep12_sally_end38 with dissolve
else:
    scene ep12_sally_end38b with dissolve
sy "At the start of this semester, you guys had a party, and I hooked up with Jamie."
sy "He was wasted. He was the perfect target."
scene ep12_sally_end39 with dissolve
sy "I saw him fiddle with his phone and figured out how he opened it."
sy "4321. Bah! What an original passcode."
scene ep12_sally_end40 with dissolve
sy "After he had passed out, I left with his phone."
scene ep12_sally_end41 with dissolve
sy "When I told Magnar what I had done to get the phone, he was furious."
scene ep12_sally_end42 with dissolve
sy "He called me a cheater and a whore. But he had told me to do anything it took, and I had."
scene ep12_sally_end43 with dissolve
sy "Magnar browsed Jamie's phone and extracted all the files he could access from the DIKs' PinkCloud account."
sy "And he kept monitoring it for any activity, too. But he never found a trace of the database."
scene ep12_sally_end44 with dissolve
sy "He told me I had to retrieve the laptop, too. But I could sense it on him..."
sy "He detested me for what I had done with Jamie."
scene ep12_sally_end45 with dissolve
sy "And little did I know... He used what he found on Jamie's phone to get back at you guys."
scene ep12_sally_end46 with dissolve
sy "He sent the tri-alphas pictures of DIKs having sex with one of their girls."
scene ep12_sally_end47 with dissolve
sy "And along with those, he also sent pictures Ron had snapped of an unexposed gay jock couple as a threat."
scene ep12_sally_end48 with dissolve
sy "Together with the DIKs' photos, he hoped that it would further pin the blame on you guys."
scene ep12_sally_end121 with dissolve
mc "It was Magnar who was behind those letters!? You can't be serious?"
mc "I've been trying to find out who the hell it was."
scene ep12_sally_end122 with dissolve
sy "I know. And it wasn't just Magnar, by the way. He had help from Bert and Ron."
sy "Bert and Ron were also privy to Pandora's box. And they were just as motivated as Magnar to get it back. Anyone loyal to Magnar would be."
scene ep12_sally_end50 with dissolve
sy "Ron had been sneaking around the gym and taking pictures."
sy "At first, it was for his own perverted reasons, but he later figured out he could use them to blackmail the DIKs."
sy "He hoped to snap a picture of some naked girl and blame the DIKs, but he ended up getting something much better."
scene ep12_sally_end49 with dissolve
mc "Cathy?"
sy "Yes."
sy "I wasn't in on the blackmailing. I want to make that clear..."
scene ep12_sally_end121 with dissolve
mc "So it was Magnar, Ron, and Bert?"
scene ep12_sally_end122 with dissolve
sy "They were all ok with it."
scene ep12_sally_end53 with dissolve
sy "During one of your Hell Week parties, I finally got the opportunity we had been waiting for."
sy "I found the laptop in Rusty's room."
scene ep12_sally_end51 with dissolve
sy "I walked in there, and I saw Nick using it."
scene ep12_sally_end52 with dissolve
mc "Nick was using it!?"
sy "Yeah. He was watching a homemade sextape of Heather and Tommy, and he got flustered when I caught him."
scene ep12_sally_end54 with dissolve
sy "He closed the video, but before he could shut down the laptop, I told him I didn't feel comfortable knowing he did that."
sy "I told him that Heather was upstairs and that I would talk to her."
scene ep12_sally_end62 with dissolve
sy "He pulled me aside into the kitchen, explained he had accidentally viewed the video, and begged me not to tell Heather."
sy "Nick's face was pale... I knew I had something good on him, but I didn't want to take it too far."
scene ep12_sally_end63 with dissolve
sy "I calmed him down, said I wouldn't tell anyone about it, and he thanked me before going up to his room."
sy "Walking with a hardon, I figured he was going to finish himself off."
scene ep12_sally_end55 with dissolve
sy "I saw the opportunity, and I seized it."
scene ep12_sally_end56 with dissolve
sy "I texted Magnar to meet me outside the library, and I went there with the laptop that I had put in a bag."
scene ep12_sally_end64 with dissolve
sy "I let Magnar in, and while I guarded the door, he did his thing."
scene ep12_sally_end65 with dissolve
sy "But he still couldn't find any trace of the database."
scene ep12_sally_end67 with dissolve
sy "Frantically, he started looking around the room for the box."
sy "He commanded me to help him find it, but I was getting nervous that someone would show up."
scene ep12_sally_end66 with dissolve
sy "Yet again... No box was found. But before Magnar left, he wanted to leave the DIKs with a surprise."
sy "He transferred the picture of Cathy to the laptop and posted it on Rooster using your frat account."
scene ep12_sally_end68 with dissolve
sy "Then he left me there with the laptop!"
sy "I was stunned when I saw what he had posted, and I started to panic."
scene ep12_sally_end57 with dissolve
sy "I exited the library and put the bag down. I don't even remember what I was doing when trying to cover everything up."
sy "It was too risky to return anything now."
scene ep12_sally_end58 with dissolve
sy "I saw people around me react to the cluck, so I locked myself inside the bathroom to hide."
scene ep12_sally_end61 with dissolve
sy "It wasn't the best move. But what choice did I have?"
sy "I could hear people through the door, talking about the cluck. I heard Rusty run around and tell people to help him look for the laptop."
scene ep12_sally_end59 with dissolve
sy "I figured I'd ride the storm out in the bathroom."
sy "But people outside needed to use the bathroom too."
scene ep12_sally_end60 with dissolve
sy "Eventually, I left the bathroom. I told the girls waiting in line that I was feeling ill."
sy "And then I quietly left the party..."
scene ep12_sally_end69 with dissolve
sy "Magnar had betrayed me by doing what he did."
scene ep12_sally_end70 with dissolve
sy "I confronted him about it, but he tried to justify it."
scene ep12_sally_end71 with dissolve
sy "Our relationship took a turn for the worse."
sy "We tried to move past everything, but it didn't feel the same as before, and we fought more than usual."
scene ep12_sally_end72 with dissolve
sy "I thought that was it for the box. I thought that he had given up on it."
sy "But then something happened to you guys."
scene ep12_sally_end73 with dissolve
sy "The tri-alphas broke into your home and ruined it."
scene ep12_sally_end77 with dissolve
sy "After Magnar got wind of it, he watched you guys closely. He watched you empty the mansion of ruined furniture."
sy "And maybe even...ruined bookshelves..."
scene ep12_sally_end74 with dissolve
sy "At night, he came here to rummage through the trash and the container you put behind the mansion."
scene ep12_sally_end75 with dissolve
sy "He thought that he could enter through the broken glass, but you had already moved into the room."
scene ep12_sally_end76 with dissolve
sy "He didn't find the box outside among the debris..."
scene ep12_sally_end78 with dissolve
sy "After you got the windows fixed, he looked inside and saw how neat the room was."
sy "If you hadn't already thrown the box in the dumpster he had scoured, it had to be in your room."
sy "You must have found it by now, and who would throw away such a mesmerizing box?"
sy "He got new hope for it..."
scene ep12_sally_end79 with dissolve
sy "He asked me to help him again, but I refused. I didn't want him to use me like that anymore."
scene ep12_sally_end81 with dissolve
sy "I almost got caught last time, and I would have been blamed for everything..."
scene ep12_sally_end80 with dissolve
sy "After he failed to convince me... He broke up with me."
sy "That was what I was to him... The means to an end."
sy "And when the tool is broken, you discard it and get a new one."
scene ep12_sally_end82 with dissolve
sy "Without my help, I thought he wouldn't try it again."
sy "But I didn't give him enough credit."
scene ep12_sally_end83 with dissolve
sy "Halloween provided the perfect opportunity."
if not branchIsabella:
    if branchJill:
        scene ep12_sally_end90 with dissolve
    else:
        scene ep12_sally_end90b with dissolve
sy "With the costumes, no one would question why Ron and Magnar were at your party."
scene ep12_sally_end84 with dissolve
sy "But your party was too crowded... Getting into your room without anyone noticing proved hard..."
scene ep12_sally_end85 with dissolve
sy "Especially since people came and went to have their pictures taken."
scene ep12_sally_end88 with dissolve
sy "I recognized Magnar's and Ron's costumes from LARPing together with them, and I confronted them."
scene ep12_sally_end89 with dissolve
sy "Magnar told Ron to hit the lights, and I tried talking Magnar out of doing something stupid."
if ep9_scary_stories or ep9_haunted_mansion:
    scene ep12_sally_end91 with dissolve
else:
    scene ep12_sally_end91b with dissolve
sy "But Ron, he went for it."
show ep12_sally_end86
if not persistent.ep12_cardcam19:
    show screen ep12_render_screen("cam19")
with dissolve
sy "Magnar couldn't be reasoned with."
stop music fadeout 3
sy "The moment the lights went out..."
show ep12_sally_end87
hide screen ep12_render_screen
with dissolve
play music "music/ep12/licensed_music/track215.mp3"
sy "He went into your room to search for the box."
scene ep12_sally_end92 with dissolve
sy "I went after him, trying to stop him as he rummaged around."
scene ep12_sally_end93 with dissolve
sy "But he was obsessed... Almost failing at the midterms got to him. He needed that box!"
scene ep12_sally_end94 with dissolve
sy "And he found it..."
sy "...proudly displayed on your desk. It was like a gift waiting to be unwrapped."
scene ep12_sally_end95 with dissolve
sy "I couldn't believe my eyes. I had heard him talk about that box for so long that I thought it was a myth."
sy "But he opened it... And there it was."
scene ep12_sally_end96 with dissolve
sy "The golden USB stick. Excalibus, as Magnar likes to call it."
mc "Do you mean Excalibur? Like the legendary sword?"
scene ep12_sally_end97 with dissolve
sy "No. Excalibus, as in a play on the word Excalibur and the word bus in USB. It's a nerd thing..."
scene ep12_sally_end98 with dissolve
sy "Magnar put the box back and left with Ron and the USB stick before the lights came back on."
scene ep12_sally_end99 with dissolve
sy "And me... I was too drunk to do anything about it."
scene ep12_sally_end123 with dissolve
sy "They are back to using the USB stick again. And they wouldn't let me have any of the answers."
sy "They shut me out completely."
sy "I bet they passed the finals with flying colors... But not me."
scene ep12_sally_end124 with dissolve
sy "They couldn't even throw me some scraps after what I did for them."
sy "Bert was the only one I could almost reason with."
sy "He said he understood me, but that his hands were tied."
scene ep12_sally_end125 with dissolve
sy "And Bert told me that after the other frats all got what's coming to them, he'd try to get Magnar to help me again."
sy "And that's when I realized that the blackmailing wouldn't stop, even though they got Excalibus back."
scene ep12_sally_end126 with dissolve
sy "Magnar didn't only want Excalibus. He wanted revenge."
scene ep12_sally_end127 with dissolve
sy "Revenge against the Alpha Nu Omegas for kicking the tri-betas out of their home..."
scene ep12_sally_end128 with dissolve
sy "Revenge against the tri-alphas for the bullying throughout the years..."
scene ep12_sally_end129 with dissolve
sy "And revenge against the DIKs for buying their home, keeping the box from him, the bullying, and for what Jamie did with me."
sy "And they are starting with the DIKs because they know how to get the jocks and the preps to turn on you..."
stop music fadeout 3
scene ep12_sally_end130 with dissolve
$ renpy.pause()
$ new_bio("Sally", "Sally told me the truth about what the tri-betas had been up to.")
$ new_bio("Nick", "Nick watched porn on the DIKs' laptop, which led to Sally being able to swipe it.")
$ new_bio("Jamie", "Jamie's lost phone was stolen by Sally. Magnar used it to find incriminating photos from the DIKs' PinkCloud account.")
$ new_bio("Magnar", "Magnar has been cheating on tests with the help of Excalibus, and he's used that USB stick to rule the tri-betas the way he wants.")
$ new_bio("Bert", "Ron, Magnar, and Bert were responsible for posting the cluck of Cathy.")
$ new_bio("Ron", "Ron, Magnar, and Bert were responsible for posting the cluck of Cathy.")
$ new_bio("Magnar", "Ron, Magnar, and Bert were responsible for posting the cluck of Cathy.")
$ new_bio("Magnar", "Magnar and Ron caused the Halloween blackout.")
$ new_bio("Ron", "Magnar and Ron caused the Halloween blackout.")
$ new_bio("Rich", "Rich's father sold the DIKs' mansion to them. In doing so, the tri-betas were evicted.")
$ new_bio("You", "The box on my desk has been the reason why the DIKs have been involved in so much drama.")

label ep12_qend_label:
play music "music/ep2/acoustic.mp3"
scene ep12_qend1 with dissolve
$ renpy.pause()
scene ep12_qend2 with dissolve
qu "I did it, Dad."
scene ep12_qend3 with dissolve
qu "Buddy is in jail..."
scene ep12_qend4 with dissolve
qu "Mick is dead..."
scene ep12_qend5 with dissolve
qu "Vinny is gone..."
scene ep12_qend6 with dissolve
qu "I've got the drugs..."
scene ep12_qend7 with dissolve
qu "I've got the money..."
scene ep12_qend8 with dissolve
$ renpy.pause()
scene ep12_qend9 with dissolve
qu "Checkmate."
scene ep12_qend10 with dissolve
$ renpy.pause()
scene ep12_qend11 with dissolve
$ renpy.pause()
scene ep12_qend12 with dissolve
qu "Ahh..."
scene ep12_qend13 with dissolve
$ renpy.pause()
scene ep12_qend14 with dissolve
qu "Have you made up your mind?"
scene ep2_intro0 with Dissolve(2)
$ renpy.pause()
qu "I can see it in your eyes..."
scene ep2_intro5 with dissolve
qu "You need this. We all do."
qu "Don't think of this as an easy escape."
qu "Think of it as liberation."
scene ep2_intro6 with dissolve
qu "With just a single prick..."
qu "...all of our troubles go-"
scene ep2_intro7
qu "Poof!"
scene ep2_intro8 with dissolve
qu "I promise you...it's not addictive..."
qu "Look, we'll do it together."
qu "I'll take half and you'll take the rest. Here!"
scene ep2_intro9 with dissolve
qu "There...Mmmm..."
qu "Just...do...it..."
scene ep2_intro9b with dissolve
qu "Join me..."
scene ep2_intro1300 with dissolve
$ renpy.pause()
scene ep2_intro13 with dissolve
$ renpy.pause()
scene bg anim_qend_ep12 movie with dissolve
pause
hide screen new_phone_screen
scene black
stop music fadeout 10
$ renpy.pause(2)
jump ep12_save_here_label

label ep12_save_here_label:
hide screen new_phone_screen
scene black
$ renpy.pause(1)
$ persistent.ep12_completed = True
$ updateDikScore()

if minigames:
    if steamAchievements:
        if ep8_help_nick and ((not ft_failed and minigames) or (not minigames and ft_fish_nm > 0)):
            $ achievement.grant("IDS3_19")
            init:
                $ achievement.register("IDS3_19")
            $ achievement.Sync()

if steamAchievements:
    $ achievement.grant("IDS3_05")
    init:
        $ achievement.register("IDS3_05")
    $ achievement.Sync()
    call check_steam_achievements_label from _call_check_steam_achievements_label_4

if steamAchievements:
    if roadJill:
        $ achievement.grant("IDS3_36")
        init:
            $ achievement.register("IDS3_36")
        $ achievement.Sync()
    if roadIsabella:
        $ achievement.grant("IDS3_37")
        init:
            $ achievement.register("IDS3_37")
        $ achievement.Sync()
    if roadJosy or roadMaya or roadMayaJosy:
        $ achievement.grant("IDS3_38")
        init:
            $ achievement.register("IDS3_38")
        $ achievement.Sync()
    if roadSage:
        $ achievement.grant("IDS3_39")
        init:
            $ achievement.register("IDS3_39")
        $ achievement.Sync()
    if roadAlone:
        $ achievement.grant("IDS3_40")
        init:
            $ achievement.register("IDS3_40")
        $ achievement.Sync()
    if roadZoey:
        $ achievement.grant("IDS3_41")
        init:
            $ achievement.register("IDS3_41")
        $ achievement.Sync()
    if roadQuinn:
        $ achievement.grant("IDS3_48")
        init:
            $ achievement.register("IDS3_48")
        $ achievement.Sync()
scene ep12_episode_end
$ renpy.pause()

$ mp_slot = -1
$ mp_slot_hover = -1
$ mps3slotname = ""
$ qM = quick_menu
$ quick_menu = 0
jump check_mps3_vars_label
label after_mps3_vars_label:
if save_name.strip() != "":
    $ mps3slotname = save_name
label after_mps3_save_label:
show screen mps3_save_screen
pause

scene black
show screen scoremsg
$ renpy.pause(2)
hide screen scoremsg

$ episodeIsEnding = True
show screen endingScreen
$ renpy.pause()
$ episodeIsEnding = False
hide screen endingScreen


jump ep12_generate_report_text_label
$ renpy.pause()
label ep12EndLabel:
stop music fadeout 2
$ renpy.pause(2)
jump game_credits

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch

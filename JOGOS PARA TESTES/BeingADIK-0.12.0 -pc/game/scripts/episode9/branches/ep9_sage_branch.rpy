label ep9_sage_branch_label:
$ guideSuggestedPage = 59
play music "music/ep9/halloween_again.mp3"
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"Are you still getting ready?",False])
$ text_message_screen_list.append(["Sage","Put your dick back inside your pants; we're coming.",True])
scene ep9_jill_branch1 with dissolve
de "[mc_de_up]! Come sit down! Want something to drink?"
scene ep9_jill_branch2 with dissolve
mc "Sure! Pour me one, bro."
hide screen new_phone_screen
scene ep9_sage_branch33 with dissolve
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
menu:
    "How did you know?":
        $ text_message_screen_list.append(["%s" % name,"How did you know?",False])
        $ text_message_screen_list.append(["Sage","I took a course in probability and stochastics; it was the most likely guess.",True])
        $ text_message_screen_list.append(["%s" % name,"Can't wait to see you.",False])
    "I'm not wearing pants":
        $ text_message_screen_list.append(["%s" % name,"I'm not wearing pants; I'm kinda wearing a skirt.",False])
        $ text_message_screen_list.append(["Sage","Should I be concerned?",True])
        $ text_message_screen_list.append(["%s" % name,"Haha! Maybe? Come here and find out.",False])
$ tmpInt += 1
$ renpy.pause()
scene ep9_sage_branch34 with dissolve
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ mphone_scene_to_chat("Sage",text_message_screen_list)
show screen new_phone_screen
scene ep9_jill_branch5 with dissolve
de "Who are you texting?"
scene ep9_jill_branch6 with dissolve
mc "Sage."
scene ep9_jill_branch7 with dissolve
de "You've sure been spending a lot of time with her lately."
scene ep9_jill_branch6 with dissolve
mc "Yeah, you know. Party planning takes time."
scene ep9_jill_branch7 with dissolve
de "Party planning. Is that what you call it?"
scene ep9_jill_branch8 with dissolve
mc "What?"
de "When are you gonna tell me what's really going on between you two?"
scene ep9_jill_branch17 with dissolve
de "When you told me about the dinner with her family..."
de "That wasn't the whole story, was it?"
scene ep9_jill_branch9 with dissolve
mc "Sage and I are...getting close."
if ep4_toldDerekAboutJade:
    scene ep9_jill_branch10 with dissolve
    de "And is that smart...? You know...? Considering that her mom is-"
    scene ep9_jill_branch14 with dissolve
    mc "Secret code."
    scene ep9_jill_branch13 with dissolve
    de "I know! I just want to talk to you about it."
    scene ep9_jill_branch12 with dissolve
    mc "Well, don't. You can't say anything that I haven't thought of myself since I found out."
    scene ep9_jill_branch13 with dissolve
    de "If you had a baby with Jade and married Sage, your kid would be your sister- or brother-in-law."
    scene ep9_jill_branch14 with dissolve
    mc "Apparently, I was wrong."
    scene ep9_jill_branch17 with dissolve
    de "Anyway... Congrats!"
else:
    scene ep9_jill_branch17 with dissolve
    de "I knew it! Congrats!"

scene ep9_jill_branch18 with dissolve
if not ep4_toldDerekAboutJade:
    mc "Thanks, bro. It's feeling pretty good, even though her family is...Tybalt."
else:
    mc "Thanks... And you know it's not only Jade; Sage's family is...Tybalt."

if pathMayaJosy and wt_ep9_branch_numbers < 2:
    scene ep9_jill_branch11 with dissolve
    de "I gotta ask..."
    de "What about my sis and Josy?"
    mc "..."
    scene ep9_jill_branch12 with dissolve
    mc "I feel horrible about it... I haven't found the perfect moment to tell them yet."
    scene ep9_jill_branch13 with dissolve
    de "[name]..."
    scene ep9_jill_branch9 with dissolve
    mc "Wow... You're calling me by my name."
    scene ep9_jill_branch13 with dissolve
    de "You've gotta tell them."
    scene ep9_jill_branch14 with dissolve
    mc "I know I have to, but you know what Maya is going through."
    mc "I can't just blurt it out, can I?"
    scene ep9_jill_branch13 with dissolve
    de "To me, you should. The longer you wait, the more it will hurt."
    scene ep9_jill_branch12 with dissolve
    if ep9_jill_mood == 1:
        mc "I know... It fucking sucks. And I already broke Jill's heart telling her about it."
        scene ep9_jill_branch13 with dissolve
        de "I feel you... But you have to."
    else:
        mc "I know... It fucking sucks."
    scene ep9_jill_branch16 with dissolve
    de "As for Tybalt, you can't choose her family. So, you'll have to suck it up if you wanna be with her."
elif ep5_feelingsForJosy or ep5_feelingsForMaya:
    de "I gotta ask..."
    scene ep9_jill_branch16 with dissolve
    if ep5_feelingsForJosy:
        de "What about your feelings for Josy?"
    else:
        de "What about your feelings for my sis?"
    scene ep9_jill_branch12 with dissolve
    mc "It's not been easy, but I'm with Sage now."
    scene ep9_jill_branch11 with dissolve
    de "Do you have feelings for Sage?"
    scene ep9_jill_branch10 with dissolve
    $ renpy.pause()
    scene ep9_jill_branch12 with dissolve
    mc "I do."
    scene ep9_jill_branch17 with dissolve
    de "That's great."
    scene ep9_jill_branch16 with dissolve
    de "As for Tybalt, you can't choose her family. So, you'll have to suck it up if you wanna be with her."
else:
    scene ep9_jill_branch16 with dissolve
    de "You can't choose her family. So, you'll have to suck it up if you wanna be with her."

scene ep9_jill_branch9 with dissolve
mc "I know. But it's funny how she's nothing like him."
mc "She's so different from her entire family..."
stop music fadeout 3
mc "But she's also different from me... I'm not sure if it's good or bad at times."
mc "Like the other day..."
hide screen new_phone_screen
label ep9_sage_lewd1_label:


if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_sage == None:
        $ mc_sage = name
    else:
        $ mc_sage = persistent.mc_sage
    if persistent.sage == None:
        $ sage = "Sage"
    else:
        $ sage = persistent.sage
    if persistent.mc_jade == None:
        $ mc_jade = name
    else:
        $ mc_jade = persistent.mc_jade
    if persistent.jade == None:
        $ jade = "Jade"
    else:
        $ jade = persistent.jade
    $ jade_state = 1
    $ totalDikChoices = 0
    $ ep4_fuckedJade = True

play music "music/ep3/black_box.mp3"
scene anim_sage_lap_ep9 with dissolve
sa "God! Yes! Deep, [mc_sage]... All the way."
sa "I want all of you."
pause
scene anim_sage_lap2_ep9 with dissolve
sa "Feel how my asscheeks are slapping against your thighs."
sa "I've been bad, [mc_sage]... Call me a name..."
mc "A name?"
pause
scene anim_sage_lap3_ep9 with dissolve
sa "Yeah. Call me something nasty."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Jade scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Sexy":
        mc "Fuck me, sexy."
        sa "That's not nasty. Call me a slut!"
        mc "A slut? Really?"
        sa "Yeah, it's hot."
        mc "Ok, uh... Fuck me...slut."
    "Whore [mod_gr][mod_choices[3]]":
        $ dk(1)
        mc "Fuck me, whore."
        sa "Whoa! Not that nasty. Jesus!"
        mc "Sorry... Uh... What do you want then?"
        sa "Call me a slut."
        mc "Ok, uh... Fuck me...slut."
    "Slut":
        mc "Fuck me, slut."
sa "Yes! I'm your little fuck slut, aren't I?"
pause


scene anim_sage_branch_miss_ep9 with dissolve
sa "Give me your cock, [mc_sage]. Your slut needs it."
sa "Ahhh! Yes! Fuck me! Harder!"
pause
scene anim_sage_branch_miss2_ep9 with dissolve
sa "Fuck my tight, slutty pussy, [mc_sage]. It's all yours."
sa "Do you like how I - *{i}Moans{/i}* - make it tighter for you?"
pause
scene anim_sage_branch_miss3_ep9 with dissolve
mc "Yeah."
sa "You're making me go crazy here, [mc_sage]. Call me a slut again."
mc "Take it...slut."
sa "Are you ok?"
mc "Yeah. I'm gonna fuck you hard."
pause

scene ep9_sage_lewd1c with dissolve
sa "No. I'm gonna fuck you hard!"
scene anim_sage_branch_ride4_ep9 with dissolve
sa "Your little fuck slut wants it bad, [mc_sage]."
sa "I'm craving your cock. I'm so fucking thirsty for it."
pause
scene anim_sage_branch_ride1_ep9 with dissolve
sa "Your cock is such a perfect fit inside my tight and wet pussy, [mc_sage]."
sa "I wanna ride it for hours. Hngnnn..."
pause
scene anim_sage_branch_ride3_ep9 with dissolve
sa "Are you with me? Come on, fuck me."
scene anim_sage_branch_ride2_ep9 with dissolve
sa "Yes... That's it! Fuck me!"

if not ep4_fuckedJade:
    scene ep9_sage_branch1 with dissolve
    $ renpy.pause()
else:
    scene anim_jade_ride_ep9 with dissolve
    ja "I'm gonna fuck your brains out, [mc_jade]!"
    mc "Ride me, [jade]!"
    scene ep9_sage_branch2 with dissolve
    $ renpy.pause()

scene ep9_sage_branch3 with dissolve
sa "Ok. Stop. What the hell is wrong with you?"
scene ep9_sage_branch4 with dissolve
mc "Uh... I'm... Nothing's wrong."
scene ep9_sage_branch3 with dissolve
sa "It's like humping a sex doll. You're just lying there and not making a sound. What's up with that?"
scene ep9_sage_branch4 with dissolve
mc "I'm thinking about your brother."
sa "..."
scene ep9_sage_branch3 with dissolve
sa "Whatever works for you..."
scene ep9_sage_branch5 with dissolve
mc "Not like that! I...uh..."
mc "I'm thinking about your family too. And Maya."
scene ep9_sage_branch6 with dissolve
sa "Super-kinky..."
scene ep9_sage_branch7 with dissolve
mc "Sage."
scene ep9_sage_branch6 with dissolve
sa "I can't joke, but you can say those things while you're inside me?"
stop music fadeout 3
scene ep9_sage_branch8 with dissolve
$ renpy.pause()
scene ep9_sage_branch9 with dissolve
mc "Sorry..."

$ renpy.end_replay()
$ persistent.ep9_lewd_sage1 = True
$ calcScenes()
$ new_bio("Sage", "I had sex with Sage, but I couldn't stop thinking about her family.")
$ mphone_stats_add_girl_s3("sage","You had sex with Sage on her bed in episode 9.")
play music "music/ep9/relaxed.mp3"
scene ep9_sage_branch10 with dissolve
sa "What's going on?"
scene ep9_sage_branch11 with dissolve
mc "I'm still a bit shocked about who your family is."
scene ep9_sage_branch12 with dissolve
sa "So? I'm still the same I always was."
scene ep9_sage_branch11 with dissolve
mc "I can't help but look at you a bit differently now."
scene ep9_sage_branch13 with dissolve
sa "Talk to me... What's on your mind?"
$ tmpList = [False,False,False,False]
label ep9_sage_q_label:
scene anim_sage_talk_ep9 with dissolve
menu:
    "Your last name" if not tmpList[0]:
        $ tmpList[0] = True
        mc "What's up with your last name? Why don't you go by Burke like your brother?"
        scene ep9_sage_branch14 with dissolve
        sa "..."
        scene ep9_sage_branch15 with dissolve
        if tmpList[1]:
            sa "Morgan is my given name. When Mom and Dad adopted my brother and me, they let us keep our last names and added Burke to them."
        else:
            sa "Morgan is my given name. When Mom and Dad adopted my brother and me-"
            scene ep9_sage_branch17 with dissolve
            mc "He's adopted too?"
            scene ep9_sage_branch18 with dissolve
            sa "Yes. We come from the same foster home."
            sa "My parents couldn't have kids, so they chose to adopt."
            sa "My dad wanted a son, and my mom wanted a daughter; they adopted both of us."
            scene ep9_sage_branch15 with dissolve
            sa "They let us keep our last names and added Burke to them."
        scene ep9_sage_branch17 with dissolve
        mc "Why did they do that?"
        scene ep9_sage_branch18 with dissolve
        sa "Because adoption is a loaded subject to talk to your kids about."
        sa "Keeping our last names made it easier for them to discuss it with us."
        scene ep9_sage_branch19 with dissolve
        sa "When we got older, we talked about the adoption, and they asked us if we wanted to change our last names."
        sa "My brother chose to remove his and only keep Burke, but I chose to keep mine."
        scene ep9_sage_branch17 with dissolve
        mc "Why did you keep yours?"
        scene ep9_sage_branch15 with dissolve
        sa "Even though I'm grateful for what Mom and Dad have done for me, \"Morgan\" is the only thing that connects me to my birth mom and dad."
        scene ep9_sage_branch18 with dissolve
        sa "And choosing to use \"Morgan\" is easier for me too."
        sa "Most people know who I am and about my family, but even so, it distances me from our well-known name."
        scene ep9_sage_branch15 with dissolve
        sa "It gives me an identity, and I feel like I'm independent, you know?"
        sa "I'm not abusing the Burke name to get ahead like my brother."
        scene ep9_sage_branch18 with dissolve
        sa "Does that answer your question?"
        scene ep9_sage_branch20 with dissolve
        mc "It does... Thank you."
        if False in tmpList:
            scene ep9_sage_branch21 with dissolve
            sa "Is anything else on your mind?"
            jump ep9_sage_q_label
    "Your brother" if not tmpList[1]:
        $ tmpList[1] = True
        mc "I can't wrap my head around that Tybalt is your brother."
        scene ep9_sage_branch18 with dissolve
        sa "We're not blood-related if it makes you feel any better."
        sa "And my feelings for him shouldn't be of any surprise to you."
        scene ep9_sage_branch23 with dissolve
        mc "I can't stand your brother."
        scene ep9_sage_branch24 with dissolve
        sa "Me neither! Fuck him. Sometimes I wish Mom and Dad had never adopted both of us."
        sa "But if they hadn't, maybe I would have turned out like him. So, there's that."
        if not tmpList[0]:
            scene ep9_sage_branch17 with dissolve
            mc "He's adopted too?"
            scene ep9_sage_branch18 with dissolve
            sa "Yes. We come from the same foster home."
            sa "My parents couldn't have kids, so they chose to adopt."
            sa "My dad wanted a son, and my mom wanted a daughter; they adopted both of us."
        scene ep9_sage_branch21 with dissolve
        sa "I know you don't get along with Tybalt, but you don't have to worry about him. Trust me."
        if False in tmpList:
            jump ep9_sage_q_label
    "Your mom" if not tmpList[2]:
        $ tmpList[2] = True
        mc "So... Your mom's been my teacher."
        scene ep9_sage_branch18 with dissolve
        sa "Yeah. Why were you taking Gender Studies?"
        scene anim_sage_talk_ep9 with dissolve
        mc "It was a mistake. Maya told me it was easy credits and would look good on my resume."
        scene ep9_sage_branch18 with dissolve
        sa "She's not wrong about that last part, you know."
        scene anim_sage_talk_ep9 with dissolve
        mc "I was getting at that she's different from you in many ways."
        scene ep9_sage_branch18 with dissolve
        sa "She is stern, but she has softer sides too. Sadly, as a female professor, you have to be strict to get respect."
        scene ep9_sage_branch20 with dissolve
        mc "(I wanna ask more about her, but I probably shouldn't...)"
        if False in tmpList:
            jump ep9_sage_q_label
    "Your dad" if not tmpList[3]:
        $ tmpList[3] = True
        mc "Tell me more about your dad."
        scene ep9_sage_branch18 with dissolve
        sa "Um... Ok? He's an honorary professor of the economics department."
        sa "He teaches several classes, too. He's a student counselor and, as you now know, a major cog in granting scholarships."
        sa "He used to be a successful investment banker, but he got fired for some bullshit reason."
        scene ep9_sage_branch19 with dissolve
        sa "It didn't matter, though. He had already made bank before he left."
        sa "He's got plenty of contacts, which he uses today to procure funding and donations for the school."
        sa "B&R loves him for it."
        scene ep9_sage_branch17 with dissolve
        mc "That's quite a list of accomplishments... How is he as a dad?"
        scene ep9_sage_branch19 with dissolve
        sa "Um... He's smart, and he's taught me a lot in life. He's my role model and the reason why I'm studying economics."
        scene ep9_sage_branch14 with dissolve
        mc "And as a dad...?"
        scene ep9_sage_branch15 with dissolve
        sa "Look. He's there for me in his own way. No parent is perfect."
        sa "He's not exactly the most...um..."
        scene ep9_sage_branch16 with dissolve
        sa "As I told you in the past, we're not good at talking about emotions."
        sa "I wish it were different, but it is what it is."
        if False in tmpList:
            jump ep9_sage_q_label
scene ep9_sage_branch21 with dissolve
sa "Was that everything you wanted to know?"
scene anim_sage_talk_ep9 with dissolve
mc "Your answers helped a lot, yeah."
scene ep9_sage_branch22 with dissolve
sa "It's nice that you want to get to know me better. I want to tell you about myself, but you know it's tough for me to open up about these things."
scene anim_sage_talk_ep9 with dissolve
mc "I know..."
scene ep9_sage_branch21 with dissolve
sa "But I don't like how you had to ask me during sex."
scene ep9_sage_branch20 with dissolve
mc "Sorry... It's been stuck in my mind lately. I couldn't focus."
scene ep9_sage_branch21 with dissolve
sa "Are you good?"
scene anim_sage_talk_ep9 with dissolve
mc "Yeah, I am. Actually, it's kind of nice..."
scene ep9_sage_branch25 with dissolve
mc "There's one thing that we have in common. Neither of us knew our mother."
scene ep9_sage_branch26 with dissolve
sa "I guess that's right."
scene ep9_sage_branch25 with dissolve
mc "I've been reading my mom's diary to get to know her, and it's pretty insightful..."
mc "I've learned a lot about her even though I never met her."
mc "Did you ever look into who your mom was?"
scene bg anim_sage_talk2_ep9 movie with dissolve
sa "..."
mc "Huh?"
scene ep9_sage_branch28 with dissolve
sa "Put your clothes on; I'm not horny anymore."
scene ep9_sage_branch27 with dissolve
mc "What's wrong? Was it something I said?"
scene ep9_sage_branch29 with dissolve
sa "Uh! What's wrong? You're asking me all these serious questions as if they don't mean anything."
scene ep9_sage_branch30 with dissolve
mc "I'm sorry. I'm only trying to bond and understand you better."
stop music fadeout 3
scene ep9_sage_branch31 with dissolve
sa "Talking about my family during sex. God, you're such a boner-killer!"
scene ep9_sage_branch32 with dissolve
mc "..."

play music "music/ep9/halloween_again.mp3"
scene ep9_jill_branch12 with dissolve
show screen new_phone_screen
mc "Sometimes it feels like I'm traversing a minefield when I ask her stuff."
scene ep9_jill_branch16 with dissolve
de "She hits you?"
scene ep9_jill_branch15 with dissolve
mc "No, but she is quick to anger, mostly when I ask her private questions."
mc "She calms down fast, though."
scene ep9_jill_branch16 with dissolve
de "Maybe she doesn't like you prying?"
scene ep9_jill_branch15 with dissolve
mc "It's not prying; it's called getting to know each other."
mc "She doesn't have an easy time talking about feelings, and it's something I don't mind doing."
mc "I always thought women had an easier time talking about feelings, but with Sage, now it's two for two..."
scene ep9_jill_branch16 with dissolve
de "You'll have to go easy on her, then."
scene ep9_jill_branch12 with dissolve
mc "I thought I was, but yeah... It's my fault. I shouldn't have asked her about her family as I was fucking her."
scene ep9_sage_branch18b with dissolve
de "You did what?"
$ new_bio("Sage", "Sage got upset when I asked her about her birth mom.")


    
if wt_ep9_branch_numbers > 1 and branchAlone:
    jump ep9_others_branch_label
    
if wt_ep9_branch_numbers > 1 and branchIsabella:
    mc "(I need to get back to my room...)"
    mc "I need to check on something real quick."
    jump ep9_bella_branch_label

scene ep9_jill_branch19 with dissolve
"The HOTs! The HOTs! They're finally here!"
stop music fadeout 3
scene ep9_jill_branch18 with dissolve
mc "Nothing. Let's go greet the HOTs."


jump ep9_wave2_label

label ep9_sage_drink_label:
scene ep9_sage_drink1 with dissolve
sa "[name]! Finally! Sit down with me!"
scene ep9_sage_drink2 with dissolve
sa "How the fuck are you doing tonight? Excited about your first party as a party planner?"
scene ep9_sage_drink3 with dissolve
mc "I've been stressing a lot. Tommy's been...counterproductive."
mc "It feels like everything has fallen on my shoulders up until now."
scene ep9_sage_drink5 with dissolve
sa "He's testing you. It's only natural that he'd get territorial about it."
sa "But he couldn't put aside his issues with Quinn to plan the party, so..."
scene ep9_sage_drink4 with dissolve
mc "I gotta give that to him; he hasn't been complaining about it that much."
mc "And it's not been all bad. He has taught me a lot, but he's difficult to deal with at times."
scene ep9_sage_drink6 with dissolve
sa "He's got a strong will. You have to pick your battles with people like him."
sa "The place looks great! Especially when people are here."
sa "I was a bit worried that we didn't get enough decorations, but I think it's spot on."
scene ep9_sage_drink4 with dissolve
mc "Yeah, it's more than enough. I think people are enjoying it."
scene ep9_sage_drink6 with dissolve
sa "So, everything's under control?"
scene ep9_sage_drink4 with dissolve
mc "Huh? Yeah!"
mc "I think all that's left is to enjoy the party."
scene ep9_sage_drink7 with dissolve
sa "So, why aren't you?"
scene ep9_sage_drink8 with dissolve
mc "What do you mean? I am."
scene ep9_sage_drink7 with dissolve
sa "You're not even drinking. You're in total control mode."
scene ep9_sage_drink8 with dissolve
mc "I am drinking. But I'm taking it slow."
scene ep9_sage_drink9 with dissolve
sa "Yeah, maybe you should. I heard you passed out at the dorm party."
scene ep9_sage_drink10 with dissolve
mc "You did? How did you hear about that?"
scene ep9_sage_drink9 with dissolve
sa "The same way as always, people talk. They talk a lot."
scene ep9_sage_drink11 with dissolve
sa "Come on. Drink some."
scene ep9_sage_drink12 with dissolve
mc "Are you gonna nurse me?"
scene ep9_sage_drink11 with dissolve
sa "If you're gonna be Mr. Stiff at the party, I will."
sa "Let's get you good and drunk."
scene ep9_sage_drink13 with dissolve
mc "Haha! Wait!"
scene ep9_sage_drink14 with dissolve
sa "There you go! Refuel that party juice!"
scene ep9_sage_drink15 with dissolve
$ renpy.pause()
scene ep9_sage_drink16 with dissolve
sa "What?"
scene ep9_sage_drink15 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+Sage)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "I really like you [mod_gr][mod_choices[0]]":
        $ RPsage += 2
        mc "I really like you."
        scene ep9_sage_drink17 with dissolve
        sa "Saying those things, perhaps you are drunk enough."
        scene ep9_sage_drink18 with dissolve
        mc "No, I'm not even halfway where I'm going tonight."
        scene ep9_sage_drink17 with dissolve
        sa "Is the destination snoring on Becky's sofa?"
        scene ep9_sage_drink19 with dissolve
        mc "You know way too much."
        sa "Hahaha!"
    "Thanks for the drink":
        mc "Thanks for the drink, but I think I got most of it on me, not in me."
scene ep9_sage_drink20 with dissolve
sa "Meet me later on the dance floor, ok?"
sa "We're gonna shake our butts together!"

if branchJill:
    jump ep9_jill_banana_event_label

jump ep9_freeroam_diks_ph2_label

label ep9_sage_hunt_label:
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

if notifications:
    play sound mphone_notifications[current_notification_sound][1]
scene ep9_sage_hunt1 with fade
"*{i}Text message{/i}*"
play music "music/ep9/diks_spooky_halloween.mp3"
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["Sage","Guess where I am...",True])
$ text_message_screen_list.append(["Sage","chat_sage_pic1_ep9_thumb",True])
$ text_message_screen_list.append(["%s" % name,"What are you up to?",False])
$ text_message_screen_list.append(["Sage","You said you would be able to find me no matter what. I'm putting it to the test.",True])

hide screen new_phone_screen
scene ep9_sage_hunt2 with dissolve
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()

menu:
    "Bathroom downstairs":
        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"I recognize those tiles. You're in the downstairs bathroom.",False])
        $ text_message_screen_list.append(["Sage","Hm... Am I?",True])
        scene ep9_sage_hunt3 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)

        scene ep9_sage_hunt6 with dissolve
        mc "Got you!"
        mc "Dammit..."

        $ text_message_screen_list.append(["%s" % name,"Ok, where are you, really?",False])
        $ text_message_screen_list.append(["Sage","I'm not in the bathroom anymore; I can tell you that much. Maybe this will help you find me?",True])
        scene ep9_sage_hunt7 with dissolve
    "Bathroom upstairs":

        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["%s" % name,"I recognize those tiles. You're in the upstairs bathroom.",False])
        $ text_message_screen_list.append(["Sage","Hm... Am I?",True])
        scene ep9_sage_hunt3 with dissolve
        show screen text_message_screen
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)

        scene ep9_sage_hunt4 with dissolve
        mc "Got you!"
        mc "Dammit..."
        $ text_message_screen_list.append(["%s" % name,"Ok. You're not here. Where are you?",False])
        $ text_message_screen_list.append(["Sage","Wrong bathroom. Besides, I'm not there anymore. Maybe this will help you find me?",True])
        scene ep9_sage_hunt5 with dissolve

$ text_message_screen_list.append(["Sage","chat_sage_pic2_ep9_thumb",True])
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
menu:
    "Upstairs hallway":
        $ text_message_screen_list.append(["%s" % name,"Hah! I got you now.",False])
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_sage_hunt9 with dissolve
        mc "(Dammit...)"
        scene ep9_sage_hunt10 with dissolve
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Sage","You must be completely off because I waited and couldn't even spot you.",True])
        $ text_message_screen_list.append(["Sage","Final clue. If you don't get this, I'll question your sanity.",True])
        show screen text_message_screen
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()
    "Dining room":

        $ text_message_screen_list.append(["%s" % name,"Hah! I got you now.",False])
        $ tmpInt += 1
        $ renpy.pause()
        hide screen text_message_screen
        scene ep9_sage_hunt8 with dissolve
        mc "(Dammit...)"
        $ tmpInt += 1
        $ tmpInt2 = len(text_message_screen_list)
        $ text_message_screen_list.append(["Sage","Haha! Close! But you just missed me.",True])
        $ text_message_screen_list.append(["Sage","Final clue.",True])
        show screen text_message_screen
        play sound "sound_effects/interlude/zoey_message.mp3"
        $ renpy.pause()
        $ tmpInt += 1
        $ renpy.pause()

$ text_message_screen_list.append(["Sage","chat_sage_pic3_ep9_thumb",True])
$ tmpInt += 1
$ renpy.pause()
stop music fadeout 3
mc "(I know where this is...)"
hide screen text_message_screen
$ mphone_scene_to_chat("Sage",text_message_screen_list)

label ep9_sage_lewd3_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.sage == None:
        $ sage = "Sage"
    else:
        $ sage = persistent.sage
    if persistent.mc_sage == None:
        $ mc_sage = name
    else:
        $ mc_sage = persistent.mc_sage
    $ ep9_haunted_mansion = False
    $ jade_state = 0
    $ ep8_sq_lewd = True
    $ ep4_fuckedJade = False
    $ affinity = "DIK"
hide screen new_phone_screen
play music "music/ep9/licensed_music/track131.mp3"
queue music ["music/ep9/licensed_music/track130.mp3","music/ep9/licensed_music/track132.mp3","music/ep9/licensed_music/track131.mp3"]
scene ep9_sage_lewd1 with dissolve
mc "Found you... Damn..."
scene ep9_sage_lewd3 with dissolve
sa "You finally caught up to me. It took you a while."
scene ep9_sage_lewd2 with dissolve
mc "You didn't make it easy for me."
if ep9_jm_sad:
    scene ep9_sage_lewd4b with dissolve
    mc "(This isn't the moment to tell her about Josy and Maya, right? She'd call me a boner-killer again.)"
    mc "(She seems happy now... I can wait to bum her out...)"
scene ep9_sage_lewd3 with dissolve
sa "So, did you run around the mansion with a boner or what?"
scene ep9_sage_lewd4 with dissolve
if ep9_jm_sad:
    mc "Um... Pretty much. You teased me good. But I told you I'd always find you."
else:
    mc "Pretty much. You teased me good. But I told you I'd always find you."
scene ep9_sage_lewd5 with dissolve
sa "I thought we could have some fun together. Maybe a party of our own?"
scene ep9_sage_lewd6 with dissolve
if ep9_haunted_mansion:
    mc "Wasn't the basement sex enough for you?"
    scene ep9_sage_lewd5 with dissolve
    sa "It was hot but barely enough."
else:
    mc "What kind of party do you have in mind?"
    scene ep9_sage_lewd5 with dissolve
sa "Something a bit raunchier than what's going on out there..."
scene ep9_sage_lewd6 with dissolve
mc "I like the sound of that."

scene bg anim_sage_lewd_plug_ep9 movie with dissolve
sa "Good. Because I've been preparing..."
mc "You want me to...?"
sa "Fuck my ass. Yes."
scene ep9_sage_lewd7 with dissolve
mc "Oh..."
scene ep9_sage_lewd8 with dissolve
sa "There's just one rule."
scene ep9_sage_lewd7 with dissolve
mc "You name it..."
scene ep9_sage_lewd8 with dissolve
sa "No boner-killing family talk tonight. Ok?"
if not ep4_fuckedJade:
    scene ep9_sage_lewd7 with dissolve
    mc "No, I learned my lesson."
else:
    scene ep9_sage_lewd7 with dissolve
    mc "..."
    mc "Ok..."
    mc "(Put it out of your mind...)"

scene anim_sage_lewd_plug2_ep9 with dissolve
sa "Good..."
pause
scene bg anim_sage_lewd_plug3_ep9 movie with dissolve
sa "Hngn..."
pause

scene anim_anal_sage_mast_ep9 with dissolve
mc "You are something else, do you know that?"
sa "I'm well aware. It's you who shouldn't forget it."
mc "Believe me; I couldn't even if I tried."
pause
scene anim_anal_sage_mast2_ep9 with dissolve
pause

scene ep9_sage_lewd9 with dissolve
sa "No-no. You're not putting that one in right off the bat."
sa "Who do you think you are? Microdick Dawe?"
scene ep9_sage_lewd11 with dissolve
mc "Did he get to do that?"
scene ep9_sage_lewd10 with dissolve
sa "Shut up! You know what I meant."
sa "You're gonna have to warm me up before you slam me with that."
scene ep9_sage_lewd12 with dissolve
sa "Use your fingers on me."
scene ep9_sage_lewd13 with dissolve
label ep9_sage_lewd_loop_label:
menu:
    "Spank ass":
        scene bg anim_anal_sage_spank1_ep9 movie with dissolve
        sa "Hnnn... Hey..."
        sa "Have I been that bad?"
        scene bg anim_anal_sage_spank2_ep9 movie with dissolve
        mc "Yeah, you made me run around the mansion looking for you."
        mc "That deserves some punishment."
        pause
        jump ep9_sage_lewd_loop_label
    "Finger her":
        scene anim_anal_sage_finger1_ep9 with dissolve
        sa "Yeah, like that... Slowly, now. Don't go too fast and hard on me."
        mc "You are tighter than I thought you'd be."
        sa "Dude, that sounds like such an insult."
        mc "No, I didn't mean it like that. You're tight!"
        pause
        scene anim_anal_sage_finger2_ep9 with dissolve
        sa "I have toys for it. But what can I say? I have a tight ass. Sue me."
        pause
        scene anim_anal_sage_finger3_ep9 with dissolve
        sa "Hngn... Your finger is thick..."
        mc "Do you like it?"
        sa "Yeah... Fuck."
        pause
        jump ep9_sage_lewd_loop_label
    "Blowjob":
        scene anim_anal_sage_bj_ep9 with dissolve
        sa "*{i}Suck suck{/i}*"
        mc "Fuck... You're so hot in that outfit."
        sa "Mhm. You like *{i}Glug{/i}* it?"
        mc "Yeah. I like how you put on stockings with it, just like last time."
        pause
        jump ep9_sage_lewd_loop_label
    "Continue":
        $ renpy.pause(0.5)

scene ep9_sage_lewd14 with dissolve
sa "Mmm... The thought of you entering my asshole is driving me crazy."
scene ep9_sage_lewd15 with dissolve
mc "Same..."

scene anim_anal_sage_rub_ep9 with dissolve
pause

scene ep9_sage_lewd16 with dissolve
mc "I'm gonna add the lube."
sa "Take it easy with that, or it's gonna be like a slip-and-slide."
mc "Hey, we can do it without if you'd rather."
scene ep9_sage_lewd17 with dissolve
sa "Haha! Good one."
sa "Just be careful with how much you use; I want some friction, dude."
scene anim_anal_sage_tease_ep9 with dissolve
mc "Do you want it?"
sa "Mhm. Enter me, [mc_sage]. *{i}Moans{/i}*"
sa "Fuck me, [mc_sage]. Slowly."
mc "Does it hurt?"
sa "I feel I need a bigger toy to handle this."
mc "I'll stop if it hurts."
sa "Hell no. Are you crazy? You're not stopping until I'm done with you."
pause

scene ep9_sage_lewd18 with dissolve
sa "Ok. *{i}Phew{/i}* Now I know I can take you."
scene ep9_sage_lewd19 with dissolve
mc "Were you worried that you couldn't?"
scene ep9_sage_lewd20 with dissolve
sa "That's such a stupid question. Have you seen yourself?"
scene ep9_sage_lewd18 with dissolve
sa "Let's go, [mc_sage]! I'm ready. How do you want me?"
$ tmpInt = 0

label ep9_sage_lewd_loop2_label:
menu:
    "Sideways":
        $ tmpInt += 1
        scene anim_anal_sage_side1_ep9 with dissolve
        sa "Fuck my ass, [mc_sage]. Take care of it."
        pause
        scene anim_anal_sage_side2_ep9 with dissolve
        mc "It's squeezing my cock so hard, [sage]."
        sa "Hnnnn! No shit! Damn!"
        pause
        scene anim_anal_sage_side3_ep9 with dissolve
        if tmpInt > 2:
            sa "I bet you're close to cumming now."
        else:
            sa "Don't cum too early now, [mc_sage]."
        pause
        jump ep9_sage_lewd_loop2_label
    "Cowgirl":
        $ tmpInt += 1
        scene ep9_sage_lewd21 with dissolve
        mc "Ride me, [sage]."
        scene ep9_sage_lewd22 with dissolve
        sa "Mmm. Keep talking to me, [mc_sage]."
        sa "I get an adrenaline kick out of it when you do."
        scene anim_anal_sage_cg1_ep9 with dissolve
        sa "*{i}Moans{/i}*"
        mc "Fuck me!"
        sa "Yes! Yes!"
        pause
        scene anim_anal_sage_cg2_ep9 with dissolve
        mc "Do you want more lube?"
        sa "No, it's perfect. You?"
        mc "I love it. Seeing you ride me like this is so hot."
        pause
        scene anim_anal_sage_cg3_ep9 with dissolve
        pause
        jump ep9_sage_lewd_loop2_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_anal_sage_rev1_ep9 with dissolve
        sa "Do you love the view, or what?"
        mc "Haha! Totally."
        sa "I figured you did. You went quiet on me all of a sudden."
        mc "Yeah, I'm trying to think of things so I don't cum too fast."
        pause
        scene anim_anal_sage_rev2_ep9 with dissolve
        sa "*{i}Moans{/i}* Why would you? Just enjoy it. Cum if you're gonna."
        mc "Easy for girls to say. You have no idea what we guys endure. One orgasm and it's over."
        sa "Haha! Sucks to be you!"
        pause
        jump ep9_sage_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene ep9_sage_lewd25 with dissolve
        sa "Go harder on me!"
        scene ep9_sage_lewd24 with dissolve
        mc "Are you sure?"
        scene ep9_sage_lewd23 with dissolve
        sa "Yeah. I wanna feel it."
        scene anim_anal_sage_doggy1_ep9 with dissolve
        sa "*{i}Moans{/i}* FUCK!"
        sa "[mc_sage]! Yes! FASTER! Hngn..."
        pause
        scene anim_anal_sage_doggy2_ep9 with dissolve
        sa "AHHH!!! KEEP GOING!"
        pause
        jump ep9_sage_lewd_loop2_label
    "Choking ({color=#ffffff}{size=-[persistent.scale_factor]}{font=fonts/collegiate.ttf}DIK{/font}{/size} affinity{/color})" if affinity == "DIK":
        $ tmpInt += 1
        scene ep9_sage_lewd27 with dissolve
        sa "Are you gonna choke me?"
        mc "Can I?"
        scene ep9_sage_lewd26 with dissolve
        sa "Don't go too hard."
        scene anim_anal_sage_rev3_ep9 with dissolve
        sa "Y-yes! Hngn!"
        pause
        scene anim_anal_sage_rev4_ep9 with dissolve
        sa "Mmpfhh..."
        pause
        scene anim_anal_sage_rev5_ep9 with dissolve
        pause
        scene ep9_sage_lewd27b with dissolve
        sa "*{i}Heavy breathing{/i}* Wow..."
        mc "Are you good?"
        sa "That was so fucking hot, [mc_sage]!"
        jump ep9_sage_lewd_loop2_label
    "Riding":
        $ tmpInt += 1
        scene anim_anal_sage_ride1_ep9 with dissolve
        sa "That look on your face, dude... Are you gonna burst?"
        if tmpInt > 2:
            mc "I can feel it getting closer... But I got some left in me."
        else:
            mc "Not yet..."
        pause
        scene anim_anal_sage_ride2_ep9 with dissolve
        sa "Open your eyes and you will."
        mc "Fuck, [sage]... You're trying to make me cum fast, aren't you?"
        sa "Haha! I don't know what it is, but teasing you is so entertaining for me."
        pause
        jump ep9_sage_lewd_loop2_label
    "Standing":
        $ tmpInt += 1
        scene anim_anal_sage_stand1_ep9 with dissolve
        sa "Yes, [mc_sage]! Punish me! Fuck my ass until you're ready to fill me up."
        pause
        scene anim_anal_sage_stand2_ep9 with dissolve
        sa "God! It feels so good! Ahhh!!!"
        pause
        scene anim_anal_sage_stand3_ep9 with dissolve
        pause
        jump ep9_sage_lewd_loop2_label
    "Cum" if tmpInt > 2:
        mc "I'm so close... It's almost time..."
        menu:
            "Standing":
                scene anim_anal_sage_stand1_ep9 with dissolve
                sa "Fill my asshole, [mc_sage]! Give it to me!"
                scene bg anim_anal_sage_cum_ep9 movie with dissolve
                sa "*{i}Moans{/i}* FUCK!!! AAHHH!!"
                mc "Ah!!! FUCK!"
                pause
                scene ep9_sage_lewd28 with dissolve
                sa "That was unbelievably hot, [mc_sage]..."
                mc "It really was..."
            "Cowgirl":
                scene anim_anal_sage_cg2_ep9 with dissolve
                mc "I'm gonna bust..."
                sa "Cum inside of my ass, [mc_sage]! Let everything go and cum!"
                scene ep9_sage_lewd35 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_sage_lewd35 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_sage_lewd35 at vpunch, cum1
                mc "Ahhh!!!"
                scene ep9_sage_lewd36 with dissolve
                sa "Damn, [mc_sage]!"
                mc "Damn yourself... Wow..."
            "Riding":
                scene anim_anal_sage_ride2_ep9 with dissolve
                sa "Cum inside of my ass, [mc_sage]! Let everything go and cum!"
                scene ep9_sage_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_sage_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep9_sage_lewd29 at vpunch, cum1
                mc "Ahhh!!!"
                scene ep9_sage_lewd30 with dissolve
                sa "Damn, [mc_sage]!"
                mc "Damn yourself... Wow..."
            "Doggystyle":
                scene anim_anal_sage_doggy2_ep9 with dissolve
                sa "Are you gonna fill me up, [mc_sage]?"
                menu:
                    "Creampie":
                        mc "Yeah, I'm so close."
                        sa "Cum in my tight asshole, [mc_sage]!"
                        scene ep9_sage_lewd31 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sage_lewd31 at vpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_sage_lewd31 at vpunch, cum1
                        mc "Ahhh!!!"
                        scene ep9_sage_lewd32 with dissolve
                        sa "Incredible... Just... Wow..."
                    "On ass":
                        mc "I wanna cum all over your ass, [sage]."
                        sa "Do it! Cum on me, [mc_sage]!"
                        scene ep9_sage_lewd34 at vpunch, cum2
                        $ renpy.pause(0.5)
                        scene ep9_sage_lewd34 at vpunch, cum2
                        $ renpy.pause(0.5)
                        scene ep9_sage_lewd34 at vpunch, cum2
                        mc "Ahhh!!!"
                        scene ep9_sage_lewd33 with dissolve
                        sa "Wow..."
$ guideSuggestedPage = 88
scene ep9_sage_lewd37 with dissolve
sa "How good was that!?"
menu:
    "5 out of 5":
        scene ep9_sage_lewd38 with dissolve
        mc "Totally a 5 out of 5!"
        scene ep9_sage_lewd39 with dissolve
        sa "Nah, not that good. 4 out of 5!"
        scene ep9_sage_lewd38 with dissolve
        mc "I'm never getting that 5, am I?"
        scene ep9_sage_lewd40 with dissolve
        sa "Hahaha!"
    "4 out of 5":
        scene ep9_sage_lewd38 with dissolve
        mc "Definitely a 4 out of 5."
        scene ep9_sage_lewd39 with dissolve
        sa "I couldn't agree more!"
        scene ep9_sage_lewd38 with dissolve
        mc "Really? It wasn't better than that?"
        scene ep9_sage_lewd39 with dissolve
        sa "4 out of 5 sounds right, don't you think?"
scene ep9_sage_lewd41 with dissolve
$ renpy.pause()
scene ep9_sage_lewd42 with dissolve
sa "I'll probably feel it tomorrow. You went all the way in."
scene ep9_sage_lewd43 with dissolve
mc "You wanted it."
scene ep9_sage_lewd42 with dissolve
sa "Yeah, but it doesn't mean I won't feel it."
sa "I like that you're into these things. Like, you're not scared of trying things with me."
if not ep8_sq_lewd:
    scene ep9_sage_lewd44 with dissolve
    sa "But I wish we could do threesomes."
    mc "I'm not against them."
    sa "Good to know..."
else:
    scene ep9_sage_lewd44 with dissolve
    sa "And it's hot that you're into threesomes too."
    mc "Who isn't?"
    sa "Some aren't. And while some might be, they couldn't handle more than one at the same time."
    sa "You, however, can."
scene ep9_sage_lewd45 with dissolve
sa "I wanna do more things with you... I have some stuff I wanna try."
scene ep9_sage_lewd46 with dissolve
mc "Like what?"
scene ep9_sage_lewd45 with dissolve
sa "I'm embarrassed to say..."
scene ep9_sage_lewd46 with dissolve
mc "You can tell me."
scene ep9_sage_lewd45 with dissolve
sa "I mean, it's nothing too crazy, but..."
scene ep9_sage_lewd46 with dissolve
mc "But what? Tell me!"
scene ep9_sage_lewd47 with dissolve
sa "Look who's eager... I think you're getting a kick out of this."
sa "I'll let you know...eventually...maybe."
scene ep9_sage_lewd48 with dissolve
mc "Stop teasing me."
scene ep9_sage_lewd47 with dissolve
sa "You'd be on board for everything I'd suggest, wouldn't you?"
scene ep9_sage_lewd48 with dissolve
menu:
    "[mod_gr]Likely":
        $ ep9_sage_vanilla = False
        mc "Not everything, but probably most of it."
        scene ep9_sage_lewd47 with dissolve
        sa "I like it... So, you wouldn't take offense if I surprised you?"
    "I prefer vanilla":
        $ ep9_sage_vanilla = True
        mc "Honestly, I'm not sure if I would. I prefer normal sex."
        scene ep9_sage_lewd49 with dissolve
        sa "Hm... Ok. So, you wouldn't like it if I surprised you?"
scene ep9_sage_lewd48 with dissolve
mc "You could give me a heads-up, no?"
scene ep9_sage_lewd50 with dissolve
if ep9_sage_vanilla:
    sa "That takes the fun out of it, but I don't want you to be uncomfortable. Can you trust me?"
else:
    sa "No. You're either in or out. You'll just have to trust me."
scene ep9_sage_lewd51 with dissolve
if ep9_sage_vanilla:
    mc "Yeah, I trust you."
else:
    mc "Ok, I'm in..."
sa "*{i}Suck{/i}* Awesome!"

$ renpy.end_replay()
$ persistent.ep9_lewd_sage3 = True
$ calcScenes()
$ new_bio("Sage", "I had anal sex with Sage after the Halloween party.")
$ mphone_stats_add_girl_s3("sage","You had anal sex with Sage after the Halloween party in episode 9.")

if ep4_fuckedJade:
    scene ep9_sage_lewd52 with dissolve
    mc "(...)"
    mc "(And here comes the guilt again...)"
    scene ep9_sage_lewd53 with dissolve
    mc "(I feel sick.)"
    mc "(She's happy when she's with me, and I feel like shit because of what I unknowingly did to her.)"
    scene ep9_sage_lewd54 with dissolve
    mc "(How would she react if I told her that I slipped up?)"
    mc "(She'd probably be mad as hell... Anger seems to be her gut response when she gets upset.)"
    mc "(But what about after that? Maybe she'd understand me if I explained how I didn't do it on purpose?)"
    scene ep9_sage_lewd53 with dissolve
    mc "(And how her mom and dad don't get along and cheat on each other... Yeah, right...)"
    mc "(You fucking idiot! I can't tell her... I fucking can't...)"
    mc "(Even if my conscience were to get cleared, I'd ruin so much more in her life than just our relationship.)"
    scene ep9_sage_lewd54 with dissolve
    mc "(I'd ruin her family... Her second family...)"
    mc "(Push that reset button for her... It didn't happen...)"
    mc "(It didn't happen...)"
    mc "(...)"
    scene ep9_sage_lewd52 with dissolve
    mc "(I don't wanna give her up. I'll have to learn how to live with this secret...)"
stop music fadeout 3


if "Sage" not in wt_ep9_scenes:
    $wt_ep9_scenes.append("Sage")

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

label ep9_ending_sage_label:
scene anim_sage_wakeup_ep9 with dissolve
sa "[name]...?"
mc "Yeah?"
sa "Wake up..."
mc "Do I have to? I'm hungover..."
scene ep9_ending_sage2 with dissolve
sa "You ended up drinking too much, didn't you?"
mc "I didn't. But I still managed to get one."
scene ep9_ending_sage3 with dissolve
mc "Oh... But this is a great way to start the day..."
scene ep9_ending_sage4 with dissolve
sa "I figured you needed it, considering we'll be cleaning up all day."
scene ep9_ending_sage5 with dissolve
mc "Ugh... I forgot about that part."
scene ep9_ending_sage6 with dissolve
sa "Don't worry. I made sure the HOTs will help out. It's only fair after this kickass party."
scene ep9_ending_sage7 with dissolve
mc "You're amazing."
scene ep9_ending_sage6 with dissolve
sa "So... I was gonna do the walk. Are you ok with that?"
scene ep9_ending_sage7 with dissolve
mc "The walk?"
scene ep9_ending_sage6 with dissolve
sa "Of shame. I heard them singing just now."
scene ep9_ending_sage8 with dissolve
mc "Why would you wanna do that if you can avoid it? Exit through my window instead."
scene ep9_ending_sage9 with dissolve
sa "I have a feeling I'd have to do it eventually, and I'm in a good mood for it."
scene ep9_ending_sage8 with dissolve
mc "If you want to, go ahead, but I wouldn't recommend it."
mc "I can talk to them if you want."
scene ep9_ending_sage9 with dissolve
sa "No. I've got this."
scene ep9_ending_sage10 with dissolve
sa "*{i}Smack{/i}* See you later, my Greek god."
scene ep9_ending_sage11 with dissolve
$ renpy.pause()
scene ep9_ending_sage12 with dissolve
tm "*{i}Sings{/i}* She fucked a DIK! He came real quick! And now she does the waaaalk!"
scene ep9_ending_sage19
le "*{i}Sings{/i}* What walk?"
scene ep9_ending_sage18 with dissolve
dikcs "*{i}Sings{/i}* The walk of shaaaame! The walk of shaaaame!"
dikcs "*{i}Sings{/i}* Our DIK brother, he's got game!"
scene ep9_ending_sage13 with dissolve
sa "Damn, you guys are out of tune. You need singing lessons."
scene ep9_ending_sage20 with dissolve
le "At least we got to finish the entire song this time."
scene ep9_ending_sage13 with dissolve
sa "Yeah, you did. This time. And there won't be a next time."
scene ep9_ending_sage21 with dissolve
tm "Jacob's that bad in bed, huh? Sucks to be you."
scene ep9_ending_sage14 with dissolve
sa "Haha! Jacob? You better get your facts straight. I've been with [name] all night."
sa "And you better get used to seeing me walk out of his room because it's far from the last time."
scene ep9_ending_sage22 with dissolve
sa "Aaaand sometimes I'll probably be accompanied by other girls too."
scene ep9_ending_sage15 with dissolve
sa "So, please do me a favor and save your tunes for the other girls."
sa "Either that or I'll pull some strings with the HOTs to get revenge."
sa "It's your call, cuties. We can get nasty."
scene ep9_ending_sage16 with dissolve
sa "Oh, and [name] convinced me to fetch the HOTs to help clean your mess today, but..."
sa "I think I'll go tell them to stay in bed instead."
scene ep9_ending_sage17 with dissolve
sa "Have fun! Toodles!"
if not ep4_toldDerekAboutJade:
    scene ep9_ending_sage23 with dissolve
    le "Dude... You fucking blew it."
    scene ep9_ending_sage24 with dissolve
    tm "Me? You woke me up for this!"
else:
    scene ep9_ending_sage25 with dissolve
    jb "Bros... We shouldn't talk about it, but..."
    jb "If she means what I think she said...um..."
    scene ep9_ending_sage26 with dissolve
    le "The dude's been banging both his girl and her mother..."
    scene ep9_ending_sage27 with dissolve
    tm "That is so..."
    tm "...cool."
jump ep9_ending2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

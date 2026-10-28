label ep9_diks_ph3_qv_event_label:
if "ep9_diks_ph3_riona_event_label" not in event_list and "ep9_diks_ph3_dz_event_label" not in event_list and "ep9_diks_ph3_zoey2_event_label" not in event_list and "ep9_diks_ph3_prg_event_label" not in event_list and "ep9_diks_ph3_lily_event_label" not in event_list and "ep9_diks_ph3_rusty_event_label" not in event_list and "ep9_diks_ph3_cumpetition_event_label" not in event_list:
    $ task_list[1] = "Check the porch"
    $ event_list.append("ep9_diks_ph3_sage_event_label")
scene ep9_diks_ph3_qv_event1 with dissolve
uk "Look what the cat dragged in."
scene ep9_diks_ph3_qv_event2 with dissolve
qu "Vinny...?"
qu "Is that your way of announcing yourself?"
scene ep9_diks_ph3_qv_event3 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qv_event4 with dissolve
qu "What are you doing here? I thought you were too cool for college these days."
scene ep9_diks_ph3_qv_event3 with dissolve
vi "I heard there was a bitching Halloween party here. I thought I'd check in on it."
scene ep9_diks_ph3_qv_event5 with dissolve
qu "And you came dressed like an ass too. Good for you."
scene ep9_diks_ph3_qv_event6 with dissolve
vi "Damn. Why so feisty? I bet a part or hole of you misses me."
scene ep9_diks_ph3_qv_event7 with dissolve
qu "Not one bit. Also, you know what we agreed to. B&R is mine."
scene ep9_diks_ph3_qv_event8 with dissolve
vi "I remember. Question is how your memory is?"
scene ep9_diks_ph3_qv_event9 with dissolve
qu "Crystal."
scene ep9_diks_ph3_qv_event8 with dissolve
vi "Crystal? Right..."
vi "So, is it a coincidence that I found the bitches I used to sell to at a party with you?"
scene ep9_diks_ph3_qv_event9 with dissolve
qu "You've been a DIK. Them partying here is hardly something new."
scene ep9_diks_ph3_qv_event8 with dissolve
vi "Then enlighten me, how come they stopped buying from me but are still blazing somehow?"
vi "I mean, Tania's out there smoking until she's dropping. It doesn't check out."
scene ep9_diks_ph3_qv_event10 with dissolve
ly "You already know why. We told you."
scene ep9_diks_ph3_qv_event11 with dissolve
ly "We're quitting, but Tania's having a harder time than others. So, we shared whatever we had left with her."
ly "Don't come here acting like we're fucking you over after we bought shitloads from you."
ly "You should be thanking us. Is that why you came to the party? If it's not, you coming here is what doesn't check out."
scene ep9_diks_ph3_qv_event12 with dissolve
vi "I guess I'll have a little chat with Tania. You know, to extend my hand in case she needs something to help her \"phase out\" what she's clearly loving."
scene ep9_diks_ph3_qv_event13 with dissolve
ly "Are you good?"
scene ep9_diks_ph3_qv_event14 with dissolve
qu "Yeah... Thanks."
scene ep9_diks_ph3_qv_event15 with dissolve
ly "Open your eyes. I got your back, sister."
scene ep9_diks_ph3_qv_event16 with dissolve
ly "I didn't bring my stick with me for nothing."

scene ep9_diks_ph3_qv_event17 with dissolve
$ renpy.pause()
$ task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_zoey2_event_label:
if "ep9_diks_ph3_riona_event_label" not in event_list and "ep9_diks_ph3_qv_event_label" not in event_list and "ep9_diks_ph3_lily_event_label" not in event_list and "ep9_diks_ph3_rusty_event_label" not in event_list and "ep9_diks_ph3_cumpetition_event_label" not in event_list:
    $ task_list[1] = "Check the porch"
    $ event_list.append("ep9_diks_ph3_sage_event_label")
scene ep9_diks_ph3_zoey2_event1 with dissolve
mc "What are you drinking?"
scene ep9_diks_ph3_zoey2_event2 with dissolve
zo "Tommy made me a drink."
scene ep9_diks_ph3_zoey2_event1 with dissolve
mc "Tommy?"
scene ep9_diks_ph3_zoey2_event2 with dissolve
zo "Yeah, I told him about my recipes and he wanted to try them."
scene ep9_diks_ph3_zoey2_event3 with dissolve
mc "Which one? You made many."
scene ep9_diks_ph3_zoey2_event4 with dissolve
zo "My Gin and Juice. What else?"
scene ep9_diks_ph3_zoey2_event3 with dissolve
mc "*{i}Shudder{/i}* Ugh. I thought about your half-and-half coke beer."
scene ep9_diks_ph3_zoey2_event4 with dissolve
zo "Haha! Don't remind me."
scene ep9_diks_ph3_zoey2_event5 with dissolve
zo "Want some? For old times' sake?"
if ep9_mad_at_zoey:
    scene ep9_diks_ph3_zoey2_event6 with dissolve
    mc "..."
    mc "No, I'm good."
    scene ep9_diks_ph3_zoey2_event5 with dissolve
    zo "Come on, just have a sip."
    scene ep9_diks_ph3_zoey2_event7 with dissolve
    mc "I said, I'm good."
    zo "..."
    mc "Sorry, I..."
    scene ep9_diks_ph3_zoey2_event8 with dissolve
    zo "This is hard for you. I get it."
    zo "Maybe this is moving too fast?"
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "Maybe it is... I don't know."
    scene ep9_diks_ph3_zoey2_event8 with dissolve
    zo "You didn't have to invite me here tonight."
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "I wanted to."
    mc "And I hoped that I would feel better about us after our talk."
    scene ep9_diks_ph3_zoey2_event8 with dissolve
    zo "But you're not."
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "I still have things to say to you and thoughts to process."
    scene ep9_diks_ph3_zoey2_event8 with dissolve
    zo "So, say them."
    scene ep9_diks_ph3_zoey2_event10 with dissolve
    zo "I'd rather hear you spew shit in my face than be mad and silent."
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "I can't tonight."
    scene ep9_diks_ph3_zoey2_event11 with dissolve
    zo "Gotcha. Next time, then."
    scene ep9_diks_ph3_zoey2_event10 with dissolve
    zo "Do you want me to leave?"
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "No. But I need more time."
    scene ep9_diks_ph3_zoey2_event10 with dissolve
    zo "You got it. All the time you need. Remember?"
    scene ep9_diks_ph3_zoey2_event9 with dissolve
    mc "Sorry."
    scene ep9_diks_ph3_zoey2_event11 with dissolve
    zo "Stop apologizing. It's cool."
    zo "We're gonna talk about this and work on it."
    scene ep9_diks_ph3_zoey2_event13 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_zoey2_event12 with dissolve
    $ renpy.pause()
else:
    scene ep9_diks_ph3_zoey2_event14 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_zoey2_event15 with dissolve
    mc "Yep. It's just like I remember it."
    mc "Did you dance yet?"
    scene ep9_diks_ph3_zoey2_event16 with dissolve
    zo "A bit before. But people were making out left and right up there. It felt kinda weird dancing next to them."
    scene ep9_diks_ph3_zoey2_event17 with dissolve
    mc "Haha, I bet."
    scene ep9_diks_ph3_zoey2_event18 with dissolve
    zo "And then there was this firefighter douche, trying to stick his tongue down my throat."
    scene ep9_diks_ph3_zoey2_event17 with dissolve
    mc "For real?"
    if zoey_dik:
        scene ep9_diks_ph3_zoey2_event18 with dissolve
        zo "A knee to the nads, and he went off to do some maintenance on his hose."
        if affinity == "DIK":
            scene ep9_diks_ph3_zoey2_event19 with dissolve
            mc "Hahaha! No way!?"
            zo "Hell yeah!"
        else:
            scene ep9_diks_ph3_zoey2_event17 with dissolve
            mc "Yikes... That hurts a lot, you know?"
            scene ep9_diks_ph3_zoey2_event18 with dissolve
            zo "He deserved it."
    else:
        scene ep9_diks_ph3_zoey2_event18 with dissolve
        zo "Some dudes see signals when there are none, or maybe he was just shooting his shot at random."
        zo "Either way, that's how I ended up here drinking."
        if affinity == "DIK":
            scene ep9_diks_ph3_zoey2_event19 with dissolve
            mc "You should have punched him."
            scene ep9_diks_ph3_zoey2_event18 with dissolve
            if ep9_josy_choice == "DIK":
                zo "That's your solution, not mine."
            else:
                zo "That wouldn't have made anything better."
        else:
            scene ep9_diks_ph3_zoey2_event17 with dissolve
            mc "Drunk people can get obnoxious."
            scene ep9_diks_ph3_zoey2_event18 with dissolve
            zo "Truth."
    scene ep9_diks_ph3_zoey2_event16 with dissolve
    zo "If you're gonna steal my drink, I might as well make you one."
    scene ep9_diks_ph3_zoey2_event15 with dissolve
    mc "It's pretty good..."
    scene ep9_diks_ph3_zoey2_event16 with dissolve
    zo "Keep it. I'll make a new one later."
    scene ep9_diks_ph3_zoey2_event15 with dissolve
    mc "Thanks! I think I gotta go find Sage. There's a costume contest starting soon, I think."
    scene ep9_diks_ph3_zoey2_event16 with dissolve
    zo "Meet you up there."
$ task_list[14] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_vinny_event_label:
if branchIsabella:
    scene ep9_diks_ph3_vinny_event1 with dissolve
else:
    scene ep9_diks_ph3_vinny_event1b with dissolve
$ renpy.pause()
scene ep9_diks_ph3_vinny_event2 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_vinny_event3 with dissolve
de "No, I swear! It works. Just dip a tampon in vodka and stick it up there."
scene ep9_diks_ph3_vinny_event4 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_vinny_event5 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_vinny_event6 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/safe.mp3"
scene ep9_diks_ph3_vinny_event7 with dissolve
$ renpy.pause()
play sound "sound_effects/door_lock.mp3"
scene ep9_diks_ph3_vinny_event8 with vpunch
$ renpy.pause()
scene ep9_diks_ph3_vinny_event9 with dissolve
$ renpy.pause()

if "" in event_list:
    $ event_list.remove("")
$ event_list.append("ep9_diks_ph3_jamie_event_label")
$ event_list.append("ep9_diks_ph3_zoey_event_label")

if (branchSage or branchJill or branchIsabella):
    $ event_list.append("ep9_vinny_label")
    $ task_list[2] = "Check your room"
    $ task_list[4] = ""
if branchMayaJosy or branchAlone:
    $ event_list.append("ep9_diks_ph3_mj_event_label")
    if persistent.mod_wtenabled:
        $ task_list[4] = "Find Josy & Maya (Rusty's room)"
    else:
        $ task_list[4] = "Find Josy & Maya"

if persistent.mod_wtenabled:
    $ task_list[3] = "Say goodbye to Zoey (Main party room)"
else:
    $ task_list[3] = "Say goodbye to Zoey"
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_lily_event_label:
$ guideSuggestedPage = 74
scene ep9_diks_ph3_lily_event1 with dissolve
if ep7_lily_lewd:
    mc "Lily! You're finally here."
else:
    mc "Lily. I didn't see you yet. Did you just show up?"
scene ep9_diks_ph3_lily_event2 with dissolve
if ep7_lily_lewd:
    ly "I finally am."
else:
    ly "Hey! Yeah, I came with my girls tonight."
scene ep9_diks_ph3_lily_event3 with dissolve
nic "[name]! Looking hot!"
scene ep9_diks_ph3_lily_event4 with dissolve
menu:
    "Thanks":
        mc "Thanks! I tried my best, but I can't go outside for too long or I get cold wearing this."
    "You too":
        scene ep9_diks_ph3_lily_event5 with dissolve
        mc "Thanks! I was gonna say the same about the two of you."
mc "What are you chatting about?"
scene ep9_diks_ph3_lily_event6 with dissolve
nic "I'm trying to make Lily drink more. She's several drinks behind me."
scene ep9_diks_ph3_lily_event7 with dissolve
ly "Maybe you should drink less?"
$ guideSuggestedPage = 75
scene ep9_diks_ph3_lily_event8 with dissolve
nic "No way! I'm at a college party! I'm gonna act the part! Woooo!!!"
if envyLikesYou:
    scene ep9_diks_ph3_lily_event9 with dissolve
    nic "I'm so happy we came!"
    scene ep9_diks_ph3_lily_event10 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone  or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "Grab ass [mod_gr][mod_choices[3]]{color=#E6F653}[mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            $ dk(1)
            scene ep9_diks_ph3_lily_event11 with dissolve
            $ renpy.pause()
        "Don't grab ass [mod_gr][mod_choices[2]]":
            $ dk(-1)
            scene ep9_diks_ph3_lily_event12 with dissolve
            $ renpy.pause()
    scene ep9_diks_ph3_lily_event13 with dissolve
    nic "Lily! You should know [name] is such a great fucking guy, I swear!"
    nic "If I had met him when I was younger, there's no telling what I would have done to him."
    scene ep9_diks_ph3_lily_event14 with dissolve
    ly "What's stopping you now?"
    scene ep9_diks_ph3_lily_event15 with dissolve
    nic "Who's to say anything is? Haha!"
else:
    scene ep9_diks_ph3_lily_event16 with dissolve
    nic "[name]! I can't get over how good you look in that costume. Are those your abs?"
    scene ep9_diks_ph3_lily_event10 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone  or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "Grab ass [mod_gr][mod_choices[3]]{color=#E6F653}[mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            $ dk(1)
            scene ep9_diks_ph3_lily_event11 with dissolve
            $ renpy.pause()
        "Don't grab ass [mod_gr][mod_choices[2]]":
            $ dk(-1)
            scene ep9_diks_ph3_lily_event12 with dissolve
            $ renpy.pause()
if ep7_lily_lewd:
    scene ep9_diks_ph3_lily_event18 with dissolve
    ly "Girl, get in line. I've been trying to get with him since like forever."
    scene ep9_diks_ph3_lily_event19 with dissolve
    ly "But apparently, he's immune to all my tricks."
    scene ep9_diks_ph3_lily_event20 with dissolve
    ly "Yep, completely immune..."
    ly "I don't think he likes his girls bad."
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone  or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "I like them bad [mod_gr][mod_choices[3]]{color=#E6F653}[mod_choices[10]]":
            if not branchAlone:
                $ tc += 1
            $ dk(1)
            scene ep9_diks_ph3_lily_event21 with dissolve
            if branchAlone:
                mc "I like my girls bad, for sure."
            else:
                mc "Trust me... I'm not immune, but I wish I was... I do like my girls bad."
            scene ep9_diks_ph3_lily_event22 with dissolve
            ly "Oh, he's starting to cave. Haha!"
        "Talk about something else [mod_gr][mod_choices[2]]":
            $ dk(-1)
            mc "So... What else is new?"
            scene ep9_diks_ph3_lily_event22 with dissolve
            ly "See?"
            nic "Haha!"
elif not envyLikesYou:
    scene ep9_diks_ph3_lily_event17 with dissolve
    ly "You're drooling over him; what's wrong with you?"
    scene ep9_diks_ph3_lily_event16 with dissolve
    nic "I never noticed that before. It's always me taking my clothes off around him."
    if name[0].lower() == 'a' or name[0].lower() == 'e' or name[0].lower() == 'u' or name[0].lower() == 'i' or name[0].lower() == 'o':
        nic "You know, when he's not pulling an [name]. Haha!"
    else:
        nic "You know, when he's not pulling a [name]. Haha!"

scene ep9_diks_ph3_lily_event23 with dissolve
mc "Are you having fun tonight?"
scene ep9_diks_ph3_lily_event24 with dissolve
nic "Very much so! I feel like I'm in college."
scene ep9_diks_ph3_lily_event23 with dissolve
menu:
    "Dressed as a teacher?":
        mc "Is that why you came dressed as a teacher?"
        scene ep9_diks_ph3_lily_event25 with dissolve
        nic "Come on... Damn it."
        ly "Haha! Told you!"
        scene ep9_diks_ph3_lily_event26 with dissolve
        mc "What did I say?"
        scene ep9_diks_ph3_lily_event27 with dissolve
        nic "Lily said I looked more like a teacher than a schoolgirl! And now you did too."
        scene ep9_diks_ph3_lily_event26 with dissolve
        mc "It's still a nice costume."
    "Dressed as a schoolgirl?":
        mc "Is that why you came dressed as a schoolgirl?"
        scene ep9_diks_ph3_lily_event28 with dissolve
        nic "Haha! See!? [name] got it!"
        ly "Dammit!"
        scene ep9_diks_ph3_lily_event30 with dissolve
        mc "What did I say?"
        scene ep9_diks_ph3_lily_event29 with dissolve
        nic "Lily said I looked more like a teacher than a schoolgirl! I knew people would get it!"

$ event_list.append("ep9_diks_ph3_cumpetition_event_label")
if ep9_cumpetition:
    scene ep9_diks_ph3_lily_event31 with dissolve
    nic "Picked a girl for the CUM-petition yet?"
    scene ep9_diks_ph3_lily_event33 with dissolve
    if branchAlone:
        mc "I didn't know I was supposed to. Besides, I'm not sure I'm gonna join."
    else:
        mc "Oh, I won't be doing that tonight."
    scene ep9_diks_ph3_lily_event32 with dissolve
    nic "What!? No! You have to!"
    scene ep9_diks_ph3_lily_event34 with dissolve
    ly "You're gonna miss a chance to get a free dance?"
    scene ep9_diks_ph3_lily_event33 with dissolve
    if branchAlone:
        if ep2_wonCumpetition:
            mc "I don't know; I didn't think about it. Besides, I don't wanna eat a condom."
        else:
            mc "I don't know; I didn't think about it. Besides, I don't wanna eat another condom."
        scene ep9_diks_ph3_lily_event35 with dissolve
        nic "Uh, what the hell does that have to do with anything?"
        scene ep9_diks_ph3_lily_event36 with dissolve
        mc "You know, the loser of the CUM-petition has to eat a condom."
        scene ep9_diks_ph3_lily_event37 with dissolve
        ly "That's only during Hell Week, silly. Tonight, it's about fun times."
        ly "I'll be your partner for it."
        scene ep9_diks_ph3_lily_event38 with dissolve
        nic "Hey, I was gonna offer first!"
        scene ep9_diks_ph3_lily_event39 with dissolve
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Nicole,Lily scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
        menu:
            "Join CUM-petition":
                $ ep9_cumpetition_join = True
                mc "Girls, don't fight. You can both dance for me."
                scene ep9_diks_ph3_lily_event41 with dissolve
                nic "Haha! Nice!"
                ly "Oh, poor you, [name]. You really had to compromise there, didn't you?"
                scene ep9_diks_ph3_lily_event42 with dissolve
                mc "What can I say? Sometimes you have to put others in front of yourself."
                scene ep9_diks_ph3_lily_event43 with dissolve
                nic "Yeah, you'll be on a chair, and we'll be in front of you."
                scene ep9_diks_ph3_lily_event44 with dissolve
                ly "Let us know when it starts, ok?"
                ly "I have a feeling we'll make you lose."
                scene ep9_diks_ph3_lily_event42 with dissolve
                mc "Bring it."
                $ task_list[5] = "Talk to Tommy"
                $ updateTaskList()
                jump endEvent
            "Skip it":
                $ ep9_cumpetition_join = False
                mc "Girls, it's fine. I'm not gonna cum in my pants tonight, regardless. Haha."
                scene ep9_diks_ph3_lily_event40 with dissolve
                ly "You're gonna miss out."
                scene ep9_diks_ph3_lily_event39 with dissolve
                mc "Maybe next time."
                $ task_list[5] = "Talk to Tommy"
                $ updateTaskList()
                jump endEvent
    else:
        mc "I think it's for the best if I skip it, yeah."
        jump ep9_diks_ph3_lily2_event_label
else:
    scene ep9_diks_ph3_lily_event31 with dissolve
    nic "[name]! Tommy said he was having a small CUM-petition later. Are you in on it?"
    scene ep9_diks_ph3_lily_event33 with dissolve
    mc "No, he insisted we should have it, but the calls are his since he's paying for it."
    scene ep9_diks_ph3_lily_event31 with dissolve
    nic "You should totally come anyway!"
    if branchAlone:
        scene ep9_diks_ph3_lily_event33 with dissolve
        mc "Sorry, I have other things to take care of."
        scene ep9_diks_ph3_lily_event45 with dissolve
        if ep7_lily_lewd:
            ly "What he's doing right now is playing hard to get. And I'm telling you, you gotta try hard with this one."
        else:
            ly "You're playing hard to get, aren't you?"
        scene ep9_diks_ph3_lily_event44 with dissolve
        nic "He totally is."
        ly "If you only knew what you're missing out on, [name]."
        $ task_list[5] = "Talk to Tommy"
        $ updateTaskList()
        jump endEvent
    else:
        scene ep9_diks_ph3_lily_event39 with dissolve
        mc "I think it's best if I skip it. Maybe next time."
        jump ep9_diks_ph3_lily2_event_label

label ep9_diks_ph3_tara_event_label:
scene ep9_diks_ph3_tara_event1 with dissolve
ta "Hey, can you hold my costume for a moment? I need to pee."
if affinity == "DIK":
    mc "Why don't you put it on the floor or somewhere?"
    scene ep9_diks_ph3_tara_event2 with dissolve
    ta "I don't want someone to ruin it and the floor is sticky."
    mc "Yeah, it would be a shame if this amazing costume got ruined."
    ta "Thanks for understanding."
    scene ep9_diks_ph3_tara_event3 with dissolve
    mc "..."
else:
    mc "Sure."

play sound "sound_effects/cloth.mp3"
scene ep9_diks_ph3_tara_event4 with dissolve
ta "Thanks!"
scene ep9_diks_ph3_tara_event5 with dissolve
mc "(I gotta try this on.)"
scene ep9_diks_ph3_tara_event6 with dissolve
mc "(Wow... I can barely see anything in it)"
scene ep9_diks_ph3_tara_event7 with vpunch
mc "BOOOOOH!!!!"
gi "Damn! Tara! Don't do that."
scene ep9_diks_ph3_tara_event8 with dissolve
mc "Haha..."

scene ep9_diks_ph3_tara_event9 with dissolve
av "Tara. We got something good. I swear!"
mc "Hm?"
av "Trust me. It's gonna be perfect. I'll show you later."
scene ep9_diks_ph3_tara_event10 with dissolve
mc "(What the fuck was that about?)"
if branchIsabella:
    scene ep9_diks_ph3_tara_event11 with vpunch
    mc "BOOOOOOH!!!"
    scene ep9_diks_ph3_tara_event12 with dissolve
    isa "..."
    mc "Don't be scared. It's me."
    scene ep9_diks_ph3_tara_event13 with dissolve
    isa "Are you changing costumes?"
    scene ep9_diks_ph3_tara_event12 with dissolve
    mc "Nah, I'm just hanging on to this while she's in the bathroom."
    scene ep9_diks_ph3_tara_event14 with dissolve
    isa "I should have gone with that costume too. It would have been smarter."
    scene ep9_diks_ph3_tara_event15 with dissolve
    mc "I like yours way more."
    scene ep9_diks_ph3_tara_event12 with dissolve
    isa "I have to give it to you. You were right."
    isa "Aside from Sage and Jill, no one recognized me tonight."
    scene ep9_diks_ph3_tara_event15 with dissolve
    mc "That's very good!"
    play sound "sound_effects/cloth.mp3"
    scene ep9_diks_ph3_tara_event16 with vpunch
    $ renpy.pause()
    scene ep9_diks_ph3_tara_event17 with dissolve
    isa "What's this?"
    scene ep9_diks_ph3_tara_event18 with dissolve
    mc "Some makeshift cover while I kiss you."
    scene ep9_diks_ph3_tara_event19 with dissolve
    isa "It's true that it wouldn't be a college party without making out."
    scene ep9_diks_ph3_tara_event20 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_tara_event21 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_tara_event22 with vpunch
    play sound "sound_effects/cloth.mp3"
    ta "I'm back!"
    scene ep9_diks_ph3_tara_event23 with dissolve
    ta "Oh! Sorry. I thought it was just you."
    mc "That's fine."
    scene ep9_diks_ph3_tara_event24 with dissolve
    mc "It could have been worse."
    scene ep9_diks_ph3_tara_event25 with dissolve
    isa "Yeah..."
    scene ep9_diks_ph3_tara_event26 with dissolve
    mc "You don't seem too freaked out. That's good."
    scene ep9_diks_ph3_tara_event25 with dissolve
    isa "I'm having a very good time."
    scene ep9_diks_ph3_tara_event26 with dissolve
    mc "That makes me glad to hear. I was worried you wouldn't."
    scene ep9_diks_ph3_tara_event25 with dissolve
    isa "Me too."
    $ event_list.append("ep9_bsolo_label")
else:
    scene ep9_diks_ph3_tara_event27 with vpunch
    play sound "sound_effects/cloth.mp3"
    ta "I'm back!"
    ta "You just had to try it, huh?"
    scene ep9_diks_ph3_tara_event28 with dissolve
    ta "*{i}Mwah{/i}* Thanks!"
    if branchAlone:
        menu:
            "[mod_gr]Kiss her":
                $ ep9_tara_kiss = True
                scene ep9_diks_ph3_tara_event29 with dissolve
                ta "Mmpff... Mmm..."
                scene ep9_diks_ph3_tara_event30 with dissolve
                ta "Mmm..."
                scene ep9_diks_ph3_tara_event30b with dissolve
                ta "*{i}Smack{/i}*"
                scene ep9_diks_ph3_tara_event31 with dissolve
                ta "Dude... Wait. I can't do this. I'm with Oscar."
                scene ep9_diks_ph3_tara_event32 with dissolve
                if name == "Oscar":
                    mc "I'm Oscar too, you know."
                else:
                    mc "Who?"
                scene ep9_diks_ph3_tara_event31 with dissolve
                if name == "Oscar":
                    ta "You're not my Oscar. He'd get mad if he found out about this."
                else:
                    ta "Oscar! He'd get mad if he found out about this."
                if affinity == "DIK":
                    scene ep9_diks_ph3_tara_event32 with dissolve
                    mc "Forget about that guy. It's a party; no one will know you did this."
                    scene ep9_diks_ph3_tara_event33 with dissolve
                    ta "..."
                    scene ep9_diks_ph3_tara_event30b with dissolve
                    ta "*{i}Smack{/i}*"
                    scene ep9_diks_ph3_tara_event30c with dissolve
                    ta "Mmm... God... No..."
                else:
                    scene ep9_diks_ph3_tara_event32 with dissolve
                    mc "Sorry, I thought you were single."
                scene ep9_diks_ph3_tara_event31 with dissolve
                ta "I gotta go before I do something I'd regret."
                if affinity == "DIK":
                    scene ep9_diks_ph3_tara_event35 with dissolve
                    mc "That sheet is big enough for both of us. And if we ruin it, I can show you the sheet I have in my bed."
                    scene ep9_diks_ph3_tara_event36 with dissolve
                    $ renpy.pause()
                    scene ep9_diks_ph3_tara_event37 with dissolve
                    mc "Hahaha."
                else:
                    scene ep9_diks_ph3_tara_event34 with dissolve
                    mc "Damn..."
                $ new_bio("Tara", "I kissed Tara at the Halloween party, but she felt a bit iffy about it since she's dating Oscar.")
            "Let her go":
                $ dk(-1)
                mc "Any time."

if branchIsabella:
    if persistent.mod_wtenabled:
        $ task_list[6] = "Talk to Bella (Main Party room)"
        if branchJill and "ep9_diks_ph3_bm_event_label" in event_list:
           $task_list[6]=task_list[6]+"\n Check Rusty's room"
        elif branchJill and "ep9_diks_ph3_bj_event_label" in event_list:
          $task_list[6]=task_list[6]+"\n Talk to Jill & Bianca (Upper Main Room)"
    else:
        $ task_list[6] = "Talk to Bella"
        
        if branchJill and "ep9_diks_ph3_bm_event_label" in event_list:
           $task_list[6]=task_list[6]+"\n Check Rusty's room"
        elif branchJill and "ep9_diks_ph3_bj_event_label" in event_list:
          $task_list[6]=task_list[6]+"\n Talk to Jill & Bianca"
else:
    $ optional_task_list[1] = ""
$ updateTaskList()
jump endEvent

label ep9_bsolo_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_isabella == None:
        $ mc_isabella = name
    else:
        $ mc_isabella = persistent.mc_isabella
    if persistent.isabella == None:
        $ isabella = "Isabella"
    else:
        $ isabella = persistent.isabella
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track131.mp3"])
scene ep9_bsolo1 with dissolve
$ renpy.pause()
scene ep9_bsolo2 with dissolve
mc "*{i}Whispers{/i}* Wanna sneak away with me?"
scene ep9_bsolo3 with dissolve
isa "Where to?"
scene ep9_bsolo2 with dissolve
mc "I was thinking...someplace where we can make out a bit."
scene ep9_bsolo3 with dissolve
isa "Make out?"
scene ep9_bsolo2 with dissolve
mc "Or talk?"
scene ep9_bsolo3 with dissolve
isa "Your room?"
scene ep9_bsolo2 with dissolve
mc "Yeah, that will do."
scene ep9_bsolo4 with dissolve
mc "Or it won't..."
isa "Has that line of girls received the same offer?"
scene ep9_bsolo5 with dissolve
mc "Yeah, just stand at the end of it and I'll meet you in there in an hour."
isa "Somehow, it's less funny when you have good comebacks."
scene ep9_bsolo6 with dissolve
mc "So, we don't have a good place for privacy, it seems."
isa "We can go for a walk."
stop music fadeout 3
mc "I'll get your bag from the bathroom."
scene ep9_bsolo7 with wipeleft
play music "music/ep9/diks_spooky_halloween.mp3"
mc "So, how much does this party feel like the ones you had in college?"
scene ep9_bsolo8 with dissolve
isa "It does take me back. It's somewhat nostalgic being here tonight."
isa "I remember details of the Halloween parties we threw that I didn't realize I still remembered."
scene ep9_bsolo7 with dissolve
mc "Anything good?"
scene ep9_bsolo8 with dissolve
isa "No, just small details. Like odd pieces of decoration and the music we played."
isa "And for some reason, I remember how I spilled wine on my friend's costume."
scene ep9_bsolo9 with dissolve
mc "You drank wine at a Halloween party?"
scene ep9_bsolo10 with dissolve
isa "It wasn't wine. It was fermented human blood."
mc "Haha! Nice."
scene ep9_bsolo11 with dissolve
isa "But yes, we had carafes of wine on a silver platter. And next to them, we had spiderwebs and plastic bats."
isa "We weren't quite as inventive with the decoration compared to you. So, kudos to you for that."
scene ep9_bsolo12 with dissolve
mc "It's going to be a bitch to clean tomorrow..."
scene ep9_bsolo11 with dissolve
isa "It always is. But the party is well worth it."
scene ep9_bsolo13 with dissolve
mc "So, where are we headed?"
scene ep9_bsolo14 with dissolve
isa "This place is good enough for a private talk but not so much for making out."
scene ep9_bsolo15 with dissolve
mc "Yeah. Any suggestions?"
isa "I have the keys to the library on me."
mc "We're gonna make out in the library?"
scene ep9_bsolo16 with dissolve
isa "No, we're going to talk in the library."
scene ep9_bsolo17 with wipeleft
mc "This brings me back..."
isa "In what way?"
scene ep9_bsolo18 with dissolve
mc "The first time we talked, for real, was at night in this spot."
scene ep9_bsolo19 with dissolve
isa "Yes. That's right."
scene ep9_bsolo21 with dissolve
mc "But this time, it's you who are walking around campus butt-naked."
scene ep9_bsolo20 with dissolve
isa "..."
mc "Haha! Funny how that turned out, eh?"
scene ep9_bsolo22 with dissolve
stop music fadeout 3
mc "Want me to find you something to wear from the lost and found?"
scene ep9_bsolo23 with dissolve
isa "..."
mc "Haha! Say something. If you're silent, this just feels mean."
hide screen new_phone_screen
play music "music/ep9/licensed_music/track123.mp3"
scene ep9_bsolo24 with dissolve
isa "*{i}Smack{/i}*"
scene ep9_bsolo26 with dissolve
mc "I thought you didn't want to make out here."
scene ep9_bsolo27 with dissolve
isa "It's not like we didn't do it before."
scene ep9_bsolo26 with dissolve
mc "Oh... Yeah... That time."
scene ep9_bsolo28 with dissolve
isa "..."
scene ep9_bsolo27 with dissolve
isa "Not this time."
scene ep9_bsolo25 with dissolve
isa "*{i}Smack{/i}*"
scene anim_bella_kiss_ep9 with dissolve
pause
scene anim_bella_kiss2_ep9 with dissolve
pause
scene anim_bella_kiss3_ep9 with dissolve
pause

scene ep9_bsolo29 with dissolve
mc "Ok, that's what I call making out."
scene ep9_bsolo30 with dissolve
isa "Surely, this is grounds for termination."
scene ep9_bsolo29 with dissolve
mc "Hey, there are no cameras in here...right?"
scene ep9_bsolo31 with dissolve
isa "While I understand why you didn't think ahead, you give me too little credit."
scene ep9_bsolo32 with dissolve
mc "Could just have said no, but ok."
scene ep9_bsolo33 with dissolve
mc "This room feels different tonight."
mc "I usually sit here and study."
scene ep9_bsolo34 with dissolve
isa "I know. I always glance in your direction when I walk into this room."
scene ep9_bsolo32 with dissolve
mc "You do? That's sweet."
scene ep9_bsolo31 with dissolve
isa "We should be getting back to the party."
scene ep9_bsolo32 with dissolve
mc "Yeah? You thirsty or something?"
scene ep9_bsolo31 with dissolve
isa "No, but I believe it needs you. Don't you have some competition or something to attend to?"
scene ep9_bsolo32 with dissolve
mc "Yeah..."
scene anim_bella_kiss3_ep9 with dissolve
pause
scene ep9_bsolo32 with dissolve
mc "Can we sneak back here later?"
scene ep9_bsolo31 with dissolve
isa "If the never-ending line of girls to your room won't go away, let's sleep in my office."
stop music fadeout 3
scene ep9_bsolo32 with dissolve
mc "Haha, deal!"
$ mphone_next_song()

$ renpy.end_replay()
$ persistent.ep9_lewd_isabella = True
$ calcScenes()
$ new_bio("Isabella", "Bella and I snuck away from the party to make out in the college's library.")
$ task_list[6] = ""

if branchJill and "ep9_diks_ph3_bm_event_label" in event_list:
           $task_list[6]="Check Rusty's room"
elif branchJill and "ep9_diks_ph3_bj_event_label" in event_list:
          $task_list[6]="Talk to Jill & Bianca"
          if persistent.mod_wtenabled:
            $task_list[6]="Talk to Jill & Bianca (Upper Main Room)"

$ updateTaskList()
show screen new_phone_screen
jump endEvent

label ep9_diks_ph3_elena_event_label:
scene ep9_diks_ph3_elena_event1 with dissolve
mc "Oh, sorry! The door was unlocked."
scene ep9_diks_ph3_elena_event2 with dissolve
el "Well, well, well... If it isn't my archenemy [name], the demigod..."
el "This bathroom isn't big enough for both of us."
scene ep9_diks_ph3_elena_event3 with dissolve
$ renpy.pause()
if ep8_elena_shot:
    scene ep9_diks_ph3_elena_event4 with dissolve
    mc "Well, well, well, indeed. If it isn't Cowgirl Elena McTitty..."
    scene ep9_diks_ph3_elena_event5 with dissolve
    el "Haha! McTitty?"
    scene ep9_diks_ph3_elena_event6 with dissolve
    el "Oh, right! Staying in character."
scene ep9_diks_ph3_elena_event7 with vpunch
play sound "sound_effects/season3/squirt.mp3"
el "Draw!!!"
"*{i}Squirt{/i}*"
mc "Pff!!! Hey!"
scene ep9_diks_ph3_elena_event8 with dissolve
el "Hahah!"
mc "What is that?"
scene ep9_diks_ph3_elena_event9 with dissolve
el "Vodka!"
scene ep9_diks_ph3_elena_event10 with dissolve
mc "So, that's why it burns?"
scene ep9_diks_ph3_elena_event11 with dissolve
el "Shit! Sorry. I was aiming for your mouth."
el "Ugh. Listen to me. I sounded like a guy there, didn't I?"
scene ep9_diks_ph3_elena_event10 with dissolve
mc "Haha! What?"
scene ep9_diks_ph3_elena_event9 with dissolve
el "Don't mind me. I'm drunk as hell tonight."
scene ep9_diks_ph3_elena_event10 with dissolve
mc "That's good. It's what the party is for. Nice costume, by the way."
mc "But um... You're not fully covered."
scene ep9_diks_ph3_elena_event12 with dissolve
mc "But looking at your face, you knew that already."
scene ep9_diks_ph3_elena_event9 with dissolve
el "Your tits are showing too."
scene ep9_diks_ph3_elena_event10 with dissolve
mc "Yeah, but... You know. I'm a guy."
if ep8_elena_shot:
    scene ep9_diks_ph3_elena_event9 with dissolve
    el "Wanna know why, though?"
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Do I?"
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "I consider you my friend, so yeah. See it as something I don't tell everyone."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Oh? Then lay it on me."
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "You might have noticed how me and John Boy are..."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Always partying naked?"
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "We're not naked, but yeah, you know what I mean."
    el "John Boy gets a kick of it, and I do too."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Of being almost naked?"
    scene ep9_diks_ph3_elena_event13 with dissolve
    el "Yeah, but also from seeing each other being almost naked among people."
    el "He likes it when guys check me out, haha!"
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "What about you? Do you like it?"
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "Which of it? Being checked out or seeing him get checked out?"
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Both, I guess."
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "Girls rarely check him out, but I like it when they do. And I don't mind guys drooling over me because I know how much John Boy likes it."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "You have an interesting relationship, to say the least."
    scene ep9_diks_ph3_elena_event9 with dissolve
    el "I hope I wasn't oversharing."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "Not at all. It's cool that you're this open about this stuff. Maybe I'll be the same with you someday soon?"
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "I've heard stories about you; I would love to know if they're true."
    el "But other than that... How are you tonight?"
else:
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "How are you tonight?"
scene ep9_diks_ph3_elena_event10 with dissolve
mc "I'm doing fine."
if ep9_others_texted[4]:
    scene ep9_diks_ph3_elena_event11 with dissolve
    el "I meant to say sorry for walking in on you and Lily."
    el "It's tough when you have a roomie. I can't tell you how many times Lily walked in on me and John Boy."
    scene ep9_diks_ph3_elena_event10 with dissolve
    mc "It's ok. I hope I didn't embarrass you."
    scene ep9_diks_ph3_elena_event9 with dissolve
    if ep8_elena_shot:
        el "After what I just told you, it should be clear I'm hard to embarrass. Haha!"
    else:
        el "Please. It's gonna take a hell of a lot more to embarrass me."
scene ep9_diks_ph3_elena_event11 with dissolve
el "Did you take a lot of pictures tonight?"
scene ep9_diks_ph3_elena_event10 with dissolve
mc "Some. And I think people have been using the camera all night."
mc "I'm sure there will be some fun photos on that camera."
scene ep9_diks_ph3_elena_event9 with dissolve
el "Awesome!"
el "Oh, yeah. Don't you have to pee?"
scene ep9_diks_ph3_elena_event10 with dissolve
mc "I really do."
scene ep9_diks_ph3_elena_event9 with dissolve
el "I'll let you get to it."
scene ep9_diks_ph3_elena_event10 with dissolve
mc "Thanks! Tell John Boy I checked you out."
scene ep9_diks_ph3_elena_event9 with dissolve
el "Haha! Will do."
scene ep9_diks_ph3_elena_event14 with dissolve
el "And don't come to my town again, or I'll shoot you."
if ep9_vinny_choice != "":
    mc "(Everyone wants to shoot me tonight...heh...)"
$ optional_task_list[2] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_bm_event_label:
scene ep9_diks_ph3_bm_event1 with dissolve
oli "Mmm..."
scene ep9_diks_ph3_bm_event2 with dissolve
oli "We can't keep sneaking around like this. It's too risky."
scene ep9_diks_ph3_bm_event3 with dissolve
mat "I can't help it. Whenever I see you... I go crazy."
mat "I want you!"
scene ep9_diks_ph3_bm_event1 with dissolve
oli "Mmm... *{i}Smack{/i}*"
scene ep9_diks_ph3_bm_event4 with dissolve
mat "Hey!! Uh... Great party! Just great!"
oli "..."
scene ep9_diks_ph3_bm_event5 with dissolve
if branchJill:
    $ ep9_saw_matthew = True
    mc "What's going on here?"
    scene ep9_diks_ph3_bm_event6 with dissolve
    mat "Nothing. I was just telling Liv a secret."
    mat "Great seeing you again, by the way. Fun party!"
    scene ep9_diks_ph3_bm_event7 with dissolve
    mc "Do you think I'm stupid?"
    scene ep9_diks_ph3_bm_event8 with dissolve
    mat "You didn't see anything. Hear me?"
    scene ep9_diks_ph3_bm_event9 with dissolve
    mc "(Fuck... Why did I have to see that? Poor Bianca...)"
    if persistent.mod_wtenabled:
        $ task_list[6] = "Talk to Jill & Bianca (Upper Main Room)"
        if (branchIsabella or branchAlone) and "ep9_diks_ph3_tara_event_label" in event_list:
            $ task_list[6] = "Talk to Jill & Bianca (Upper Main Room)\n Talk to the ghost (Right Hallway)"
    else:
        $ task_list[6] = "Talk to Jill & Bianca"
        if (branchIsabella or branchAlone) and "ep9_diks_ph3_tara_event_label" in event_list:
            $ task_list[6] = "Talk to Jill & Bianca\n Talk to the ghost"
        
    $ new_bio("Jill", "I caught Jill's friends, Matthew and Olivia, making out in Rusty's room at the Halloween party.")
    $ new_bio("Bianca", "I caught Bianca's boyfriend, Matthew, making out with Olivia in Rusty's room at the Halloween party.")
else:
    if affinity == "DIK":
        mc "Don't fuck in Rusty's bed. Ok?"
        scene ep9_diks_ph3_bm_event6 with dissolve
        mat "No, no. That's not what this is!"
        scene ep9_diks_ph3_bm_event5 with dissolve
        mc "Sure, buddy."
    else:
        mc "Thanks. You should probably return to the party out there."
        scene ep9_diks_ph3_bm_event6 with dissolve
        mat "Yeah, yeah. Of course."
    if ep8_jill_state == 1:
        $ ep9_saw_matthew = True
        scene ep9_diks_ph3_bm_event9 with dissolve
        mc "(Matthew and Olivia... Poor Bianca... Well... It sucks, but that's none of my business.)"
        $ new_bio("Jill", "I caught Jill's friends, Matthew and Olivia, making out in Rusty's room at the Halloween party.")
        $ new_bio("Bianca", "I caught Bianca's boyfriend, Matthew, making out with Olivia in Rusty's room at the Halloween party.")
    else:
        scene ep9_diks_ph3_bm_event10 with dissolve
        mc "(People are getting horny. Can't blame them.)"

    $ optional_task_list[0] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_sm_event_label:
scene ep9_diks_ph3_sm_event1 with dissolve
sar "Only muffins and cakes? No pizza?"
ml "I couldn't find any."
scene ep9_diks_ph3_sm_event2 with dissolve
mc "Are you raiding our fridge?"
scene ep9_diks_ph3_sm_event3 with dissolve
sar "We wouldn't do it unless we had to."
scene ep9_diks_ph3_sm_event4 with dissolve
mc "Are you hungry?"
scene ep9_diks_ph3_sm_event5 with dissolve
ml "Starving! We skipped dinner for the party, thinking there would be food. But all we find are cakes, chips and popcorn."
scene ep9_diks_ph3_sm_event6 with dissolve
mc "We don't have any food in there; we needed the space for the party."
scene ep9_diks_ph3_sm_event7 with dissolve
sar "Dammit. "
ml "Wanna leave and order some burgers?"
sar "Yeah, let's do that."
scene ep9_diks_ph3_sm_event8 with dissolve
mc "Sounds like a good plan. It's getting late anyway."
if branchAlone and (ep6_sarah_lewd or ep8_sarah_lewd or ep8_melanie_lewd or ep4_fuckedMelanie):
    scene ep9_diks_ph3_sm_event9 with dissolve
    ml "Yeah? Wanna join us?"
    label ep9_diks_ph3_sm_eventb_label:
    scene ep9_diks_ph3_sm_event10 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sarah,Melanie scene)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone:
                             $mod_choices[10]="(Heather path open/+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "End the night with Sarah & Melanie [mod_gr][mod_choices[0]]":
            $ ep9_sarah_melanie_lewd = True
            $ ep9_ended_night_with = "Sarah & Melanie"
            $ wt_ep9_end_pick="Sarah"
            mc "Order a burger for me too. I'm joining."
            scene ep9_diks_ph3_sm_event11 with dissolve
            ml "I'm gonna get one with bacon."
            scene ep9_diks_ph3_sm_event12 with dissolve
            mc "That sounds perfect. Bacon rocks."
            $ phone_clear_jump_label = "ep9_sm_lewd_label"
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
            jump end_freeroam
        "Not yet":
            mc "Can you give me a second? I need to check something first."
            $ event_list.append("ep9_diks_ph3_sm_eventb_label")
            jump endEvent
        "End the night in a different way":
            mc "Thanks, but I'm not hungry and I need to stay here."
scene ep9_diks_ph3_sm_event13 with dissolve
sar "Mel. Let's go. I'm feeling up for a bacon burger."
ml "That sounds so good... My mouth is watering."
$ optional_task_list[8] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_sage_event_label:
$ guideSuggestedPage = 77
scene ep9_diks_ph3_sage_event0 with dissolve
$ renpy.pause()
play music "music/ep7/licensed_music/track48.mp3"
scene ep9_diks_ph3_sage_event1 with dissolve
sa "Did you see Leon tonight? Poor thing."
ri "Jamie mentioned Leon's mad at him for ditching his theme costume and leaving Leon looking like that."
scene ep9_diks_ph3_sage_event2 with dissolve
sa "He did? That's not cool."
scene ep9_diks_ph3_sage_event3 with dissolve
mc "Hate to be that guy, but Jamie doesn't want people in here during the party."
scene ep9_diks_ph3_sage_event4 with dissolve
ri "It's cool. He unlocked it for us."
scene ep9_diks_ph3_sage_event5 with dissolve
mc "Oh. But why?"
scene ep9_diks_ph3_sage_event6 with dissolve
sa "Because the mansion's crowded and we wanted someplace to chat without screaming."
scene ep9_diks_ph3_sage_event7 with dissolve
mc "It is lively out there, yeah."
scene ep9_diks_ph3_sage_event4 with dissolve
ri "The party's a real banger."
scene ep9_diks_ph3_sage_event8 with dissolve
mc "You ok there, Camila?"
scene ep9_diks_ph3_sage_event9 with dissolve
cam "Hm? Yeah. My head's spinning a bit. This helps."
scene ep9_diks_ph3_sage_event10 with dissolve
sa "How much did you drink?"
scene ep9_diks_ph3_sage_event9 with dissolve
cam "All of it? Haha!"
scene ep9_diks_ph3_sage_event11 with dissolve
play sound "sound_effects/interlude/zoey_message.mp3"
"*{i}Text message{/i}*"
ri "Oof. I just got a text from Alex. Looks like the alphas aren't having the best time on their end."
$ renpy.sound.set_volume(0,channel='music')
$ renpy.music.play("music/ep4/fluffing_a_duck.mp3", channel="music2")
scene ep9_bus_trip1
ar "*{i}Sobs{/i}* I'm sorry for caring!"
ar "I thought trick-or-treating where I grew up would be a fun thing to do!"
scene ep9_bus_trip2 with dissolve
ar "I even got my parents to put up a party tent and everything!"
ar "There's gonna be finger food and - *{i}Snotty sob{/i}* - karaoke!"
scene ep9_bus_trip3 with dissolve
ash "Arieth... It's not that it's bad; it's just not what they expected."
scene ep9_bus_trip2 with dissolve
ar "I'm sorry!!! I guess I'm extra emotional because of this pregnancy thing."
scene ep9_bus_trip4 with dissolve
an "The what?"
scene ep9_bus_trip6 with dissolve
ar "I'm pregnant!!! Ok!?"
scene ep9_bus_trip7 with dissolve
ar "Oh, yeah."
ar "Dawe? You're gonna be a father."
scene ep9_bus_trip5 with dissolve
$ renpy.pause()
$ renpy.music.stop(channel="music2", fadeout=0)
$ renpy.sound.set_volume(1.0,channel='music')
scene ep9_diks_ph3_sage_event11
ri "This isn't gonna bite us in the ass, right?"
scene ep9_diks_ph3_sage_event12 with dissolve
sa "It better not. Quinn set it up."
scene ep9_diks_ph3_sage_event13 with dissolve
mc "Seems like she fooled them good."
scene ep9_diks_ph3_sage_event11 with dissolve
ri "Alex sounds pissed about it, and I doubt he's the only one."
scene ep9_diks_ph3_sage_event13 with dissolve
mc "Ugh..."
scene ep9_diks_ph3_sage_event14 with dissolve
ri "What?"
scene ep9_diks_ph3_sage_event15 with dissolve
mc "I'm so tired of the fights between jocks and DIKs."
mc "When we're not fighting each other, we're fighting over you girls."
scene ep9_diks_ph3_sage_event16 with dissolve
sa "We've started breaking traditions..."
scene ep9_diks_ph3_sage_event17 with dissolve
ri "Do you think they care about traditions? They care about \"pussy\", and you know it."
scene ep9_diks_ph3_sage_event18 with dissolve
cam "We should all just get along and be happy."
scene ep9_diks_ph3_sage_event19 with dissolve
ri "Damn, Cammy. You {b}are{/b} drunk."
scene ep9_diks_ph3_sage_event18 with dissolve
cam "Hahaha!"
scene ep9_diks_ph3_sage_event20 with dissolve
sa "The thought is nice, but could you imagine a party with DIKs and alphas?"
sa "And I don't mean like our party with just [name] and Jacob; I mean a full-scale party with everyone."
scene ep9_diks_ph3_sage_event21 with dissolve
ri "That would be a disaster! They're hardwired to hate each other."
scene ep9_diks_ph3_sage_event22 with dissolve
mc "Yeah. Even if one or two of us might get along, there are too many of us that never would."
mc "Like, imagine if Dawe and Tommy had to party with each other. I'd give that party two minutes before it went south."
scene ep9_diks_ph3_sage_event23 with dissolve
sa "I think you're being too narrow-minded on that one. Imagine if the party was huge, bigger than this one. "
sa "Do you think it wouldn't work when there are that many guests? The DIKs and the alphas wouldn't even have to talk."
scene ep9_diks_ph3_sage_event22 with dissolve
mc "Maybe at first, but you know how alcohol brings out the worst in some? I just don't see it happening."
scene ep9_diks_ph3_sage_event23 with dissolve
sa "Well, you'll have to think about something. I doubt we'll be able to fool the alphas easily after this."
scene ep9_diks_ph3_sage_event24 with dissolve
cam "Whoa..."
scene ep9_diks_ph3_sage_event25 with dissolve
ri "Did you get an idea, Cammy?"
scene ep9_diks_ph3_sage_event24 with dissolve
cam "No, I sat up too fast."
scene ep9_diks_ph3_sage_event26 with dissolve
sa "Don't drink more for a while. You don't wanna pass out before the best costume contest."
sa "Speaking of it, we should do it soon. Are you ready for it, [name]?"
scene ep9_diks_ph3_sage_event27 with dissolve
mc "What do I need to do?"
scene ep9_diks_ph3_sage_event28 with dissolve
sa "Have you made your picks for the best costume yet?"
scene ep9_diks_ph3_sage_event27 with dissolve
mc "No?"
scene ep9_diks_ph3_sage_event28 with dissolve
sa "It's fine; you still have time."
sa "Check guests' costumes one final time and pick three entries for the contest."
scene ep9_diks_ph3_sage_event27 with dissolve
mc "So, I'm deciding who wins?"
scene ep9_diks_ph3_sage_event28 with dissolve
sa "Quinn and I will choose three each. Then we will talk about a final top three together and let the guests decide the winner based on that."
scene ep9_diks_ph3_sage_event27 with dissolve
mc "Ok, that sounds good. Is there anyone I can't pick?"
scene ep9_diks_ph3_sage_event26 with dissolve
sa "Well, obviously not yourself, me or Quinn. Other than that, pick whoever you want."
stop music fadeout 3
sa "Let me know when you're ready to start the competition."
$ event_list.append("ep9_diks_ph3_sage2_event_label")
$ event_list.append("ep9_diks_ph3_costume_riona_event_label")
$ event_list.append("ep9_diks_ph3_costume_camila_event_label")
$ event_list.append("ep9_diks_ph3_costume_sm_event_label")
$ event_list.append("ep9_diks_ph3_costume_nl_event_label")
if not ep9_mad_at_zoey:
    $ event_list.append("ep9_diks_ph3_costume_zoey_event_label")
$ event_list.append("ep9_diks_ph3_costume_derek_event_label")
if branchJill:
    $ event_list.append("ep9_diks_ph3_costume_jill_event_label")
$ event_list.append("ep9_diks_ph3_costume_elena_event_label")
$ event_list.append("ep9_diks_ph3_costume_leon_event_label")
if not (pathMayaJosy and not branchMayaJosy):
    $ event_list.append("ep9_diks_ph3_costume_jm_event_label")
if branchIsabella:
    $ event_list.append("ep9_diks_ph3_costume_bella_event_label")

if "ep9_diks_ph3_room_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph3_room_event_label")

$ task_list[1] = "Pick top three costumes"
$ updateTaskList()
$ mphone_next_song()
jump ep9_diks_ph3_qt_event_label

label ep9_diks_ph3_sage2_event_label:
scene ep9_diks_ph3_sage2_event1 with dissolve
sa "Are you ready for the contest?"
scene ep9_diks_ph3_sage2_event2 with dissolve
if "" in ep9_top_three:
    jump ep9_diks_ph3_sage2b_event_label
menu:
    "Let's do it":
        if "ep9_diks_ph3_costume_riona_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_riona_event_label")
        if "ep9_diks_ph3_costume_camila_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_camila_event_label")
        if "ep9_diks_ph3_costume_sm_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_sm_event_label")
        if "ep9_diks_ph3_costume_nl_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_nl_event_label")
        if "ep9_diks_ph3_costume_zoey_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_zoey_event_label")
        if "ep9_diks_ph3_costume_derek_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_derek_event_label")
        if "ep9_diks_ph3_costume_jill_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_jill_event_label")
        if "ep9_diks_ph3_costume_elena_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_elena_event_label")
        if "ep9_diks_ph3_costume_leon_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_leon_event_label")
        if "ep9_diks_ph3_costume_jm_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_jm_event_label")
        if "ep9_diks_ph3_costume_bella_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_bella_event_label")
        if "ep9_diks_ph3_costume_riona_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_riona_eventb_label")
        if "ep9_diks_ph3_costume_sm_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_sm_eventb_label")
        if "ep9_diks_ph3_costume_nl_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_nl_eventb_label")
        if "ep9_diks_ph3_costume_zoey_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_zoey_eventb_label")
        if "ep9_diks_ph3_costume_derek_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_derek_eventb_label")
        if "ep9_diks_ph3_costume_jill_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_jill_eventb_label")
        if "ep9_diks_ph3_costume_elena_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_elena_eventb_label")
        if "ep9_diks_ph3_costume_leon_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_leon_eventb_label")
        if "ep9_diks_ph3_costume_jm_eventb_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_costume_jm_eventb_label")

        if "ep9_diks_ph3_becky_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_becky_event_label")
        if "ep9_diks_ph3_jacob_event_label" in event_list:
            $ event_list.remove("ep9_diks_ph3_jacob_event_label")

        $ task_list[7] = ""
        $ task_list[1] = ""
        $ updateTaskList()
        mc "Yeah, I have my picks. Let's do it."
        stop music fadeout 3
        scene ep9_diks_ph3_sage2_event1 with dissolve
        sa "Let's get Quinn first to come up with the best picks."
    "Not yet":
        label ep9_diks_ph3_sage2b_event_label:
        mc "Not yet. I need more time."
        scene ep9_diks_ph3_sage2_event1 with dissolve
        sa "Hurry up. We should do it soon."
        $ event_list.append("ep9_diks_ph3_sage2_event_label")
        jump endEvent

play music "music/ep9/halloween_again.mp3"
scene ep9_diks_ph3_sage2_event3 with wipeleft
qu "It's time already?"
scene ep9_diks_ph3_sage2_event4 with dissolve
sa "Yeah, time flies tonight. Do you have your picks?"
scene ep9_diks_ph3_sage2_event3 with dissolve
qu "I can come up with three, sure. You?"
scene ep9_diks_ph3_sage2_event4 with dissolve
sa "Yeah, I've seen enough to know who my favorites are."
scene ep9_diks_ph3_sage2_event5 with dissolve
mc "So, how do we do this?"
scene ep9_diks_ph3_sage2_event6 with dissolve
sa "Let's present our picks and see if we can agree on something. You can go first, [name]."
scene ep9_diks_ph3_sage2_event7 with dissolve
mc "Ok. I couldn't find everyone, but I looked at as many as possible and my picks in no specific order..."
if "Riona" in ep9_top_three:
    mc "I like Riona's cat costume. It's cute, hot, and funny."
    scene ep9_diks_ph3_sage2_event8 with dissolve
    sa "She spent a long time on that makeup. So, she cares a lot about the party."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Camila" in ep9_top_three:
    mc "Camila is one of my picks. I think her costume looks great on her."
    scene ep9_diks_ph3_sage2_event14 with dissolve
    qu "Aha, you're picking with your dick tonight."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Sarah" in ep9_top_three:
    mc "Sarah. Her bunny costume is great."
    scene ep9_diks_ph3_sage2_event9 with dissolve
    sa "She does look great in it. But what about Melanie? She's dressed the same."
    scene ep9_diks_ph3_sage2_event10 with dissolve
    if "Melanie" in ep9_top_three:
        mc "She's also one of my picks. I know they are wearing the same costume, but they are equally good to me."
    else:
        mc "I think Sarah looks better in it."
        scene ep9_diks_ph3_sage2_event14 with dissolve
        qu "Translation: [name] would rather fuck Sarah than Melanie."
    scene ep9_diks_ph3_sage2_event7 with dissolve
elif "Melanie" in ep9_top_three:
    mc "Melanie is rocking that bunny outfit. She's one of my picks."
    scene ep9_diks_ph3_sage2_event9 with dissolve
    sa "What about Sarah? She's wearing the same costume."
    scene ep9_diks_ph3_sage2_event10 with dissolve
    mc "I prefer Melanie, though. She wears it better."
    scene ep9_diks_ph3_sage2_event14 with dissolve
    qu "Translation: [name] would rather fuck Melanie than Sarah."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Nicole" in ep9_top_three:
    mc "Nicole's costume is great. I pick her."
    scene ep9_diks_ph3_sage2_event9 with dissolve
    sa "Nicole? Who's that again?"
    scene ep9_diks_ph3_sage2_event12 with dissolve
    qu "A stripper from The Pink Rose."
    sa "Oh. Ok."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Lily" in ep9_top_three:
    mc "Lily's costume is so good. I have to pick her."
    scene ep9_diks_ph3_sage2_event8 with dissolve
    sa "It is good. I agree."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Jill" in ep9_top_three:
    mc "Jill is one of my picks."
    scene ep9_diks_ph3_sage2_event15 with dissolve
    qu "That banana costume is shit."
    scene ep9_diks_ph3_sage2_event12 with dissolve
    sa "[name] can choose whomever he wishes."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Josy" in ep9_top_three:
    mc "Josy's fairy costume is amazing."
    scene ep9_diks_ph3_sage2_event9 with dissolve
    sa "Maya's wearing a similar costume. What about her?"
    scene ep9_diks_ph3_sage2_event10 with dissolve
    if "Maya" in ep9_top_three:
        mc "She's also my pick. I find them equally good and Maya's hair looks great."
        scene ep9_diks_ph3_sage2_event15 with dissolve
        qu "Gay."
    else:
        mc "I think Josy's costume is better."
    scene ep9_diks_ph3_sage2_event7 with dissolve
elif "Maya" in ep9_top_three:
    mc "Maya's fairy costume is amazing."
    scene ep9_diks_ph3_sage2_event9 with dissolve
    sa "What about Josy? She's wearing a similar costume."
    scene ep9_diks_ph3_sage2_event10 with dissolve
    mc "I think Maya's better. Her hair looks amazing too."
    scene ep9_diks_ph3_sage2_event15 with dissolve
    qu "Gay."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Derek" in ep9_top_three:
    mc "Derek's costume is one of the best at the party."
    scene ep9_diks_ph3_sage2_event8 with dissolve
    sa "It is a funny one."
    scene ep9_diks_ph3_sage2_event15 with dissolve
    qu "You're gonna vote for your best friend?"
    scene ep9_diks_ph3_sage2_event16 with dissolve
    mc "You're goddamned right."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "John Boy" in ep9_top_three:
    mc "John Boy's cowboy outfit is a good one."
    scene ep9_diks_ph3_sage2_event14 with dissolve
    qu "It's lame if you ask me."
    scene ep9_diks_ph3_sage2_event12 with dissolve
    sa "Let [name] pick whatever he wants."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Elena" in ep9_top_three:
    mc "I like Elena's cowgirl outfit."
    scene ep9_diks_ph3_sage2_event11 with dissolve
    sa "She and Derek had the same idea with the pants."
    scene ep9_diks_ph3_sage2_event14 with dissolve
    qu "Yeah, but she had the decency to not let her ass hang out like his."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Leon" in ep9_top_three:
    mc "I can't pick the best costumes without seriously considering Leon's costume. The dude has been dressed like a chick for the entire party."
    scene ep9_diks_ph3_sage2_event14 with dissolve
    qu "Haha, it's dedication, for sure."
    scene ep9_diks_ph3_sage2_event7 with dissolve
if "Zoey" in ep9_top_three:
    mc "And my final pick is Zoey."
    scene ep9_diks_ph3_sage2_event15 with dissolve
    qu "Who?"
    if branchSage:
        scene ep9_diks_ph3_sage2_event13 with dissolve
        sa "His ex-girlfriend...right?"
    else:
        scene ep9_diks_ph3_sage2_event12 with dissolve
        sa "His ex-girlfriend, right?"
    scene ep9_diks_ph3_sage2_event15 with dissolve
    qu "Your ex is here? And you're picking her for the contest?"
    scene ep9_diks_ph3_sage2_event16 with dissolve
    mc "That's not the full story. Zoey is my final pick."
    scene ep9_diks_ph3_sage2_event7 with dissolve
mc "What about you two?"
scene ep9_diks_ph3_sage2_event12 with dissolve
sa "Ok. Those are some good picks. Quinn?"
scene ep9_diks_ph3_sage2_event17 with dissolve
qu "Easy."
qu "Kylie, because I wanna watch Becky lose her shit."
qu "Leon, because I don't think he's been humiliated enough."
scene ep9_diks_ph3_sage2_event18 with dissolve
if branchIsabella:
    qu "And whoever is wearing that slutty mummy outfit. Half of her ass is showing and I have no fucking clue who it is."
    mc "(Fuck!)"
else:
    qu "And Sally, because she had the balls to wear basically a blanket without underwear."
    qu "Plus, I made her tits show in it and I wanna see that on stage."
scene ep9_diks_ph3_sage2_event19 with dissolve
sa "Ok. Interesting..."
sa "My picks would be..."
sa "Nick. Because his clown costume is fucking scary!"
scene ep9_diks_ph3_sage2_event20 with dissolve
sa "Penny. Her makeup must have taken ages. It looks amazing!"
sa "And I agree with you, Quinn, but for different reasons. Leon's had a rough night. He should get something for his effort."
scene ep9_diks_ph3_sage2_event21 with dissolve
mc "Ok, so from the looks of it. We do not agree on a lot."
scene ep9_diks_ph3_sage2_event22 with dissolve
sa "Yeah, but Leon seems to be a majority vote."
scene ep9_diks_ph3_sage2_event23 with dissolve
qu "Yeah, he's one of the top three."
scene ep9_diks_ph3_sage2_event22 with dissolve
sa "Let's do it this way. You two pick one each and that will be that."
scene ep9_diks_ph3_sage2_event23 with dissolve
if branchIsabella:
    qu "All right. The mummy."
    scene ep9_diks_ph3_sage2_event24 with dissolve
    mc "Really? The mummy? Can't we agree on Kylie?"
    scene ep9_diks_ph3_sage2_event25 with dissolve
    mc "Sage?"
    scene ep9_diks_ph3_sage2_event26 with dissolve
    sa "Uh...yeah. Maybe Kylie's a better choice?"
    scene ep9_diks_ph3_sage2_event27 with dissolve
    qu "Nah, fuck Kylie. It's about the best costume. Unless you have a better reason why I can't pick the mummy?"
    scene ep9_diks_ph3_sage2_event26 with dissolve
    sa "No. Not really."
    mc "(Fuck fuck fuck.)"
else:
    qu "All right. Kylie's my pick."
scene ep9_diks_ph3_sage2_event22 with dissolve
sa "[name]? The final choice is yours."
scene ep9_diks_ph3_sage2_event21 with dissolve
menu:
    "[ep9_top_three[0]]" if "Leon" != ep9_top_three[0]:
        $ ep9_top_pick = ep9_top_three[0]
        mc "Ok. I choose [ep9_top_three[0]]."
    "[ep9_top_three[1]]" if "Leon" != ep9_top_three[1]:
        $ ep9_top_pick = ep9_top_three[1]
        mc "Ok. I choose [ep9_top_three[1]]."
    "[ep9_top_three[2]]" if "Leon" != ep9_top_three[2]:
        $ ep9_top_pick = ep9_top_three[2]
        mc "Ok. I choose [ep9_top_three[2]]."
if not branchIsabella:
    stop music fadeout 3
scene ep9_diks_ph3_sage2_event22 with dissolve
sa "Great. It's settled then. Let's start the competition."
if branchIsabella:
    scene ep9_diks_ph3_sage2_event28 with dissolve
    mc "*{i}Whispers{/i}* Um... The mummy."
    stop music fadeout 3
    sa "*{i}Whispers{/i}* Trust me. I've got this."
jump ep9_diks_ph3_costume_event_label

label ep9_diks_ph3_becky_event_label:
scene ep9_diks_ph3_becky_event1 with dissolve
mc "Becky?"
scene ep9_diks_ph3_becky_event2 with vpunch
bc "Hey!!! What the hell are you doing here!?"
scene ep9_diks_ph3_becky_event3 with dissolve
mc "I saw some puddles leading in here and I had to check what it was. I'm guessing Jacob's coming soon."
scene ep9_diks_ph3_becky_event4 with dissolve
bc "He fucking better be! He told me to wipe off and wait for him here."
scene ep9_diks_ph3_becky_event3 with dissolve
mc "What happened?"
scene ep9_diks_ph3_becky_event4 with dissolve
bc "Can you like turn around when we talk!?"
if affinity == "DIK":
    scene ep9_diks_ph3_becky_event3 with dissolve
    mc "No. What happened?"
else:
    scene ep9_diks_ph3_becky_event6 with dissolve
    mc "*{i}Sigh{/i}* What happened?"

scene ep9_diks_ph3_becky_event4 with dissolve
bc "I fell into your stupid bathtub when the lights went out. I fucking hate you guys for that!"
scene ep9_diks_ph3_becky_event3 with dissolve
mc "It's just water and coloring."
scene ep9_diks_ph3_becky_event4 with dissolve
bc "It ruined my costume!"
if "DIK" == affinity:
    scene ep9_diks_ph3_becky_event5 with dissolve
    mc "I'd say it got you into an even better costume, but that's just me."
    scene ep9_diks_ph3_becky_event4 with dissolve
    bc "Fuck you!"
bc "Are you gonna help me or what?"
scene ep9_diks_ph3_becky_event3 with dissolve
mc "I don't think Jacob's coming any time soon; he's on the dance floor."
scene ep9_diks_ph3_becky_event7 with dissolve
bc "Screw this!"
mc "I don't think he'll let you borrow that one."
bc "Screw him too."
scene ep9_diks_ph3_becky_event8 with dissolve
mc "(I should probably tell Jacob about this.)"
$ event_list.append("ep9_diks_ph3_jacob_event_label")
if persistent.mod_wtenabled:
    $ task_list[7] = "Warn Jacob (Tommy's room)"
else:
    $ task_list[7] = "Warn Jacob"
$ updateTaskList()
$ new_bio("Becky", "Becky fell into the bathtub and ruined her costume at the Halloween party. She was mad and stormed off with Jacob's DIK jacket.")
jump endEvent

label ep9_diks_ph3_riona_event_label:
if "ep9_diks_ph3_rusty_event_label" not in event_list and "ep9_diks_ph3_dz_event_label" not in event_list and "ep9_diks_ph3_zoey2_event_label" not in event_list and "ep9_diks_ph3_prg_event_label" not in event_list and "ep9_diks_ph3_lily_event_label" not in event_list and "ep9_diks_ph3_cumpetition_event_label" not in event_list and "ep9_diks_ph3_qv_event_label" not in event_list:
    $ task_list[1] = "Check the porch"
    $ event_list.append("ep9_diks_ph3_sage_event_label")
$ guideSuggestedPage = 74
scene ep9_diks_ph3_riona_event1 with dissolve
ri "[name]?"
scene ep9_diks_ph3_riona_event3 with dissolve
mc "Yeah? What's up?"
scene ep9_diks_ph3_riona_event2 with dissolve
ri "Come with me for a second."
scene ep9_diks_ph3_riona_event4 with dissolve
mc "In here?"
scene ep9_diks_ph3_riona_event5 with dissolve
mc "What's on your mind?"
scene ep9_diks_ph3_riona_event6 with dissolve
mc "What are you up to?"

scene ep9_diks_ph3_riona_event7 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Riona path)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
if branchAlone:
    menu:
        "Make out [mod_gr][mod_choices[0]]{color=#E6F653}[mod_choices[10]]":
            jump ep9_riona_makeout_label
        "Refuse her":
            jump ep9_riona_refuse_label
else:
    $ mc_info = ["Make out [mod_gr][mod_choices[11]]","ep9_riona_makeout_label","{size=-%d}Tell her about your situation{/size}" % (3 * persistent.scale_factor),"ep9_riona_talk_label","Refuse her","ep9_riona_refuse_label",ep7_riona_lewd or ep5_fuckedRiona or ep7_rica_lewd]
    show screen major_choice_screen
    $ renpy.pause()

label ep9_riona_makeout_label:
$ ep9_riona_choice = "DIK"
if not branchAlone:
    $ tc += 2
scene ep9_diks_ph3_riona_event8 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event9 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event10 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event11 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event12 with dissolve
mc "Hey..."
scene ep9_diks_ph3_riona_event11 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event10 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event13 with dissolve
ri "I like making out with you."
if branchAlone:
    scene ep9_diks_ph3_riona_event12 with dissolve
    mc "You're not worried about me messing up your makeup?"
    scene ep9_diks_ph3_riona_event14 with dissolve
    ri "Well, not until you just said it."
    scene ep9_diks_ph3_riona_event12 with dissolve
    mc "Don't worry, haha. It still looks fine."
    scene ep9_diks_ph3_riona_event15 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_riona_event16 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_riona_event17 with dissolve
    ri "This is why I like you. You're like me..."
    scene ep9_diks_ph3_riona_event18 with dissolve
    mc "In what way?"
    scene ep9_diks_ph3_riona_event17 with dissolve
    ri "You like having fun with people."
    scene ep9_diks_ph3_riona_event18 with dissolve
    mc "I like having fun with you."
    scene ep9_diks_ph3_riona_event17 with dissolve
    ri "Yeah, but what I mean is that you don't make a big deal out of it."
    ri "With some guys, you know all they want is to fuck. And then they treat you like shit after."
    scene ep9_diks_ph3_riona_event20 with dissolve
    ri "You come off as more...genuine, somehow."
    scene ep9_diks_ph3_riona_event21 with dissolve
    mc "I like having fun, but I haven't ruled out looking for a relationship either."
    mc "But right now, I'm kinda playing the field a bit. Seeing if I can find something worth pursuing."
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "You? In a relationship? I don't see it."
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "Is it that hard to believe?"
    scene ep9_diks_ph3_riona_event24 with dissolve
    ri "..."
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "I mean, if you were looking for one, I'd say the girl you chose would be lucky to have you."
    ri "But I don't get that vibe from you."
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "What about you?"
    scene ep9_diks_ph3_riona_event25 with dissolve
    ri "Me in a relationship...? I don't think so."
    scene ep9_diks_ph3_riona_event26 with dissolve
    ri "..."
    scene ep9_diks_ph3_riona_event25 with dissolve
    ri "Maybe someday?"
    ri "It would be kinda nice when I think about it. But I don't know."
    ri "It's so damned hard to trust guys, you know?"
    ri "I haven't met anyone who cared about me that way. They only seem to want one thing from me."
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "Well, if you keep giving it to them, then maybe that's all there will be?"
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "Aha, you think I should play hard to get?"
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "No, I mean. If you're looking for something real, maybe your mindset should be to try to find it rather than dudes to hook up with."
    scene ep9_diks_ph3_riona_event24 with dissolve
    ri "..."
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "You realize that if I did, I wouldn't be doing this with you tonight."
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "I do. And maybe I would shape up, knowing that you looked for something real?"
    scene ep9_diks_ph3_riona_event24 with dissolve
    ri "..."
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "Ok, I've changed my mind about you."
    ri "Maybe you are a relationship kinda guy after all."
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "Just like that?"
    scene ep9_diks_ph3_riona_event22 with dissolve
    ri "There's something about the way you talk to me."
    ri "I think I want to believe it."
    ri "Maybe I'll change my ways?"
    scene ep9_diks_ph3_riona_event23 with dissolve
    mc "Well, I'm not sure if I will change mine."
    mc "But can I get one last kiss before you do?"
    scene ep9_diks_ph3_riona_event27 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_riona_event47 with dissolve
    ri "Happy?"
    scene ep9_diks_ph3_riona_event48 with dissolve
    mc "And...um...maybe we could...you know? Have some more fun tonight too?"
    scene ep9_diks_ph3_riona_event47 with dissolve
    ri "Haha... Nope."
    scene ep9_diks_ph3_riona_event28 with dissolve
    mc "Wait, I didn't mean what I said."
    scene ep9_diks_ph3_riona_event31 with dissolve
    ri "No, I think you did."
    if ep9_kissed_rio:
        scene ep9_diks_ph3_riona_event32 with dissolve
        mc "Rio! Don't leave me with a boner again."
        scene ep9_diks_ph3_riona_event34 with dissolve
        mc "..."
        scene ep9_diks_ph3_riona_event35 with dissolve
        mc "Like you are perfect? At least I'm honest about it!"
    else:
        mc "Rio!"
    scene ep9_diks_ph3_riona_event33 with dissolve
    mc "(Me and my stupid mouth.)"
else:
    scene ep9_diks_ph3_riona_event36 with dissolve
    mc "Fuck.. I can't do this..."
    scene ep9_diks_ph3_riona_event37 with dissolve
    ri "I hate to break it to you, but you are doing it."
    scene ep9_diks_ph3_riona_event36 with dissolve
    mc "Rio... I'm getting involved with someone."
    scene ep9_diks_ph3_riona_event37 with dissolve
    ri "Yeah, right. So am I."
    scene ep9_diks_ph3_riona_event36 with dissolve
    mc "I'm not joking. I am."
    scene ep9_diks_ph3_riona_event38 with dissolve
    mc "It's new to me...but I'm in a relationship. And I'm trying to stay faithful."
    scene ep9_diks_ph3_riona_event39 with dissolve
    ri "Dude... You obviously suck at it."
    scene ep9_diks_ph3_riona_event38 with dissolve
    mc "Yeah, with you I do. I like you a lot."
    scene ep9_diks_ph3_riona_event40 with dissolve
    ri "You gotta make up your mind about it, [name]."
    ri "You can have me tonight if you want."
    scene ep9_diks_ph3_riona_event41 with dissolve
    mc "Fuck... Don't do this to me."
    mc "If I wasn't in a relationship, I'd never be able to refuse you saying that."
    scene ep9_diks_ph3_riona_event40 with dissolve
    ri "*{i}Sigh{/i}* All right, then I'll do it for you."
    ri "[name]. I'm cutting you off until you make your mind up."
    scene ep9_diks_ph3_riona_event41 with dissolve
    mc "God..."
    scene ep9_diks_ph3_riona_event42 with dissolve
    ri "I think we're alike. We both love having fun."
    ri "I don't think you're a relationship kinda guy. This just proves it."
    scene ep9_diks_ph3_riona_event41 with dissolve
    mc "But I want to be."
    scene ep9_diks_ph3_riona_event42 with dissolve
    ri "Do you?"
    scene ep9_diks_ph3_riona_event41 with dissolve
    mc "I think so. But like I said, I like you. It's hard to resist you."
    scene ep9_diks_ph3_riona_event42 with dissolve
    ri "You'll figure it out."
    scene ep9_diks_ph3_riona_event29 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_riona_event33 with dissolve
    $ renpy.pause()

$ tmpBool = False
if not persistent.ep9_card17:
    $ tmpBool = True
    $ persistent.ep9_card17 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
if not persistent.ep9_card18:
    $ tmpBool = True
    $ persistent.ep9_card18 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
if tmpBool:
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
$ new_bio("You", "I made out with Riona at the Halloween party.")
$ new_bio("Riona", "I made out with Riona at the Halloween party.")
$ task_list[15] = ""
$ updateTaskList()
jump endEvent

label ep9_riona_talk_label:
$ ep9_riona_choice = "NEUTRAL"

scene ep9_diks_ph3_riona_event43 with dissolve
mc "Hey... Whoa... I'm flattered, but I can't do this with you."
scene ep9_diks_ph3_riona_event45 with dissolve
if ep7_riona_lewd or ep5_fuckedRiona or ep7_rica_lewd:
    ri "Huh? Why not? You're not the kinda guy to refuse me."
else:
    ri "Huh? Why not?"
scene ep9_diks_ph3_riona_event43 with dissolve
mc "I'm getting involved with someone."
scene ep9_diks_ph3_riona_event45 with dissolve
ri "You are?"
scene ep9_diks_ph3_riona_event44 with dissolve
mc "Yeah, it's pretty new, but this wouldn't sit right with me."
scene ep9_diks_ph3_riona_event45 with dissolve
ri "You're serious. Wow..."
ri "Forgive me, but I never saw you as that kinda guy."
scene ep9_diks_ph3_riona_event44 with dissolve
mc "What kind?"
scene ep9_diks_ph3_riona_event45 with dissolve
ri "The relationship kind. I thought you were a bit like me. You know? Having fun with people and such."
scene ep9_diks_ph3_riona_event44 with dissolve
mc "I haven't been in a real relationship before, but now I wanna try it."
mc "I'm not sure if it's for me, but if I don't give it a shot I'll never know."
scene ep9_diks_ph3_riona_event47 with dissolve
ri "Well, obviously. Go for it, dude."
ri "It sucks, though. I kinda liked knowing you were available."
scene ep9_diks_ph3_riona_event48 with dissolve
mc "I mean, it's not like you and I would ever be in a relationship. Right?"
scene ep9_diks_ph3_riona_event47 with dissolve
ri "Me in a relationship? Haha... I don't think so."
ri "I mean..."
scene ep9_diks_ph3_riona_event50 with dissolve
ri "..."
scene ep9_diks_ph3_riona_event47 with dissolve
ri "Maybe someday?"
ri "It would be kinda nice when I think about it. But I don't know."
ri "It's so damned hard to trust guys, you know?"
scene ep9_diks_ph3_riona_event49 with dissolve
ri "I haven't met anyone who cared about me that way. They only seem to want one thing from me."
scene ep9_diks_ph3_riona_event48 with dissolve
mc "Well, if you keep giving it to them, then maybe that's all there will be?"
scene ep9_diks_ph3_riona_event47 with dissolve
ri "Aha, you think I should play hard to get?"
scene ep9_diks_ph3_riona_event48 with dissolve
mc "No, I mean. If you're looking for something real, maybe your mindset should be to try to find it rather than dudes to hook up with."
scene ep9_diks_ph3_riona_event50 with dissolve
ri "..."
scene ep9_diks_ph3_riona_event47 with dissolve
ri "Ok, I've changed my mind about you."
ri "Maybe you are a relationship kinda guy after all."
scene ep9_diks_ph3_riona_event48 with dissolve
mc "Just like that?"
scene ep9_diks_ph3_riona_event47 with dissolve
ri "There's something about the way you talk to me."
ri "Such a shame, though..."
scene ep9_diks_ph3_riona_event48 with dissolve
mc "What is?"
scene ep9_diks_ph3_riona_event47 with dissolve
ri "I'm not gonna root for your relationship to last, that's all."
scene ep9_diks_ph3_riona_event29 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_riona_event33 with dissolve
mc "(Ah... Rio... Don't do that to me.)"

$ new_bio("You", "I told Riona that I was in a relationship at the Halloween party.")
$ new_bio("Riona", "I told Riona that I was in a relationship at the Halloween party.")
$ task_list[15] = ""
$ updateTaskList()
jump endEvent

label ep9_riona_refuse_label:
$ ep9_riona_choice = "CHICK"
if branchAlone:
    scene ep9_diks_ph3_riona_event43 with dissolve
    mc "Hey... Whoa... I'm flattered. Really, but I don't wanna do this."
    scene ep9_diks_ph3_riona_event45 with dissolve
    if ep9_kissed_rio:
        ri "Huh? What's wrong? You wanted to make out earlier."
    elif ep7_riona_lewd or ep5_fuckedRiona or ep7_rica_lewd:
        ri "Huh? What's wrong? You're not the kinda guy to refuse me."
    else:
        ri "Huh? What's wrong?"
    scene ep9_diks_ph3_riona_event44 with dissolve
    mc "I think you're great, but I'm not feeling it right now."
    scene ep9_diks_ph3_riona_event46 with dissolve
    ri "..."
    scene ep9_diks_ph3_riona_event45 with dissolve
    ri "Ok."
    scene ep9_diks_ph3_riona_event29 with dissolve
    $ renpy.pause()
else:
    scene ep9_diks_ph3_riona_event43 with dissolve
    mc "Oh... Sorry, but I can't do this."
    scene ep9_diks_ph3_riona_event45 with dissolve
    ri "I think the answer you're looking for is \"Yes, gimme\"."
    scene ep9_diks_ph3_riona_event43 with dissolve
    mc "Don't..."
    mc "It's tempting, but I can't."
    scene ep9_diks_ph3_riona_event45 with dissolve
    ri "All right..."
    scene ep9_diks_ph3_riona_event30 with dissolve
    $ renpy.pause()
$ new_bio("You", "I rejected Riona's advances at the Halloween party.")
$ new_bio("Riona", "I rejected Riona's advances at the Halloween party.")
$ task_list[15] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_sally_event_label:
$ guideSuggestedPage = 81
scene ep9_diks_ph3_sally_event1 with dissolve
sy "Psst! [name]."
scene ep9_diks_ph3_sally_event2 with dissolve
mc "Yeah?"
scene ep9_diks_ph3_sally_event1 with dissolve
sy "Can you help me?"
scene ep9_diks_ph3_sally_event2 with dissolve
mc "In the bathroom...? Nope."
scene ep9_diks_ph3_sally_event3 with dissolve
sy "Wait, wait! Don't leave."
sy "Something bad happened."
sy "My costume got compromised...and it...and it ripped!"
scene ep9_diks_ph3_sally_event4 with dissolve
mc "Where is it now?"
scene ep9_diks_ph3_sally_event5 with dissolve
sy "I have it, but it's ruined. I can't wear it anymore. I just can't!"
scene ep9_diks_ph3_sally_event4 with dissolve
mc "That's quite a predicament."
scene ep9_diks_ph3_sally_event5 with dissolve
sy "Stop being an ass! Help me!"
scene ep9_diks_ph3_sally_event6 with dissolve
mc "Let me see what the problem is."
sy "Hey!"
scene ep9_diks_ph3_sally_event7 with dissolve
mc "Oh. You're not wearing anything underneath?"
scene ep9_diks_ph3_sally_event8 with dissolve
sy "No shit? A round of applause for Captain Obvious."
if affinity == "DIK":
    scene ep9_diks_ph3_sally_event9 with dissolve
    mc "I'm waiting. Please clap your hands for me."
    scene ep9_diks_ph3_sally_event8 with dissolve
sy "I wanted my costume to be somewhat historically accurate! Hello?"
scene ep9_diks_ph3_sally_event9 with dissolve
mc "Ah. Like your glasses and wristwatch?"
scene ep9_diks_ph3_sally_event8 with dissolve
sy "Shut up!"
scene ep9_diks_ph3_sally_event9 with dissolve
mc "Hahaha!"
scene ep9_diks_ph3_sally_event10 with dissolve
sy "Help me out here. Get me something to wear."
scene ep9_diks_ph3_sally_event7 with dissolve
mc "Why don't you try to put it back on? There must be some way to wear it."
scene ep9_diks_ph3_sally_event8 with dissolve
sy "Don't you think I've tried that? And why are there no fucking towels in here!?"
scene ep9_diks_ph3_sally_event7 with dissolve
mc "No clue..."
menu:
    "[mod_gr]Offer your clothes":
        $ currentFreeRoamLabel = "ep9_diks_ph3_toilet_2nd_label"
        $ ep9_helped_sally = True
        mc "Let me get you some of my clothes, so you don't have to walk home with nothing. Ok?"
        scene ep9_diks_ph3_sally_event11 with dissolve
        sy "Thank you."
    "Leave her hanging":
        $ ep9_helped_sally = False
        mc "I think we ran out of options. Good luck with it."
        scene ep9_diks_ph3_sally_event12 with dissolve
        sy "[name]!?"
        $ optional_task_list[9] =""
        $ updateTaskList()
        $ new_bio("Sally", "Sally's costume ripped, and I didn't help her with it.")
        $ event_list.append("ep9_diks_ph3_sally_eventb_label")
        jump endEvent
scene ep9_diks_ph3_sally_event13 with fade
mc "Here you go. I'm gonna need these back, though."
scene ep9_diks_ph3_sally_event14 with dissolve
sy "Yes, of course."
scene ep9_diks_ph3_sally_event15 with dissolve
sy "Thanks... You're less of an ass than I thought you were."
if affinity == "DIK":
    scene ep9_diks_ph3_sally_event16 with dissolve
    mc "And you have less of an ass than your clothes usually suggest."
    scene ep9_diks_ph3_sally_event19 with dissolve
    mc "Haha! Have a good one, Sally!"
else:
    scene ep9_diks_ph3_sally_event17 with dissolve
    mc "Wanna try that again without making it sound like an insult?"
    scene ep9_diks_ph3_sally_event18 with dissolve
    sy "No. That's the best you'll get from me."
    scene ep9_diks_ph3_sally_event17 with dissolve
    mc "All right... Return my clothes whenever, then."
$ optional_task_list[9] = ""
$ updateTaskList()
$ event_list.append("ep9_diks_ph3_sally_gone_event_label")
$ new_bio("Sally", "Sally's costume ripped, but I helped her by lending her some of my clothes.")
jump endEvent

label ep9_diks_ph3_heather_event_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ affinity = "DIK"
    $ ep7_told_heather_tommy_cheated = True
    $ branchAlone = True
    $ branchJill = False
    $ branchIsabella = False
    $ assman = True
    $ branchSage = True
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track133.mp3"])
$ guideSuggestedPage = 77
scene ep9_diks_ph3_heather_event1 with dissolve
he "[name]!"
scene ep9_diks_ph3_heather_event2 with dissolve
if affinity == "DIK":
    mc "Hey, Heather! Run in slow motion for me."
    scene ep9_diks_ph3_heather_event1 with dissolve
    he "What? Listen..."
else:
    mc "Heather! What's up?"
    scene ep9_diks_ph3_heather_event1 with dissolve
he "Have you seen Tommy?"
scene anim_heather_idle_ep9 with dissolve
mc "Let me think... Hm... It's been a while. I don't know where he is."
mc "Did you check the dance floor?"
menu:
    "Check her tits":
        if not _in_replay:
            $ dk(1)
        scene anim_heather_idle2_ep9 with dissolve
    "Focus on eyes":
        if not _in_replay:
            $ dk(-1)
        scene ep9_diks_ph3_heather_event5 with dissolve
he "I did, but I couldn't find him. Someone told me they saw him with Christie."
scene anim_heather_idle_ep9 with dissolve
mc "I saw him with Christie earlier, but it's been a while since."
scene ep9_diks_ph3_heather_event5 with dissolve
he "I knew it. He's gonna try to get with her tonight, I swear."
scene anim_heather_idle_ep9 with dissolve
mc "What makes you say that?"
scene ep9_diks_ph3_heather_event5 with dissolve
he "Aside from the fact that he told me she would be his next plus one, whenever that happened..."
he "Well, I don't need anything more than that to know."
scene anim_heather_idle_ep9 with dissolve
mc "Did you tell him no, or...?"
scene ep9_diks_ph3_heather_event5 with dissolve
if ep7_told_heather_tommy_cheated:
    he "I told him it's not gonna happen while he's already plus three."
else:
    he "I told him it's not gonna happen while he's already plus two."
scene anim_heather_idle_ep9 with dissolve
mc "That should do it, then..."
scene ep9_diks_ph3_heather_event6 with dissolve
he "Why the fuck are you being sarcastic?"
scene anim_heather_idle_ep9 with dissolve
mc "Look, Tommy's clearly doing what he feels like. He thinks it's easier to ask for forgiveness than permission."
mc "Unless you put your foot down with him, this is gonna continue happening to you."
mc "Maybe he's off doing something right now with Christie; maybe he's not. Whichever it is, you're still being stressed out and paranoid about it."
mc "That doesn't sound healthy to me."
play sound "sound_effects/clank.mp3"
scene ep9_diks_ph3_heather_event10 with hpunch
he "You're right!"
scene ep9_diks_ph3_heather_event6 with dissolve
he "I should do the same to him."
scene ep9_diks_ph3_heather_event7 with dissolve
mc "What?"
scene ep9_diks_ph3_heather_event6 with dissolve
he "I mean, he doesn't ask for permission to be with others; why should I?"
scene anim_heather_idle_ep9 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Heather scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "That wasn't what I meant" if not _in_replay:
        mc "That wasn't what I meant, Heather. Talk to him about this. Tell him you're not as ok with it as he thinks you are."
        scene ep9_diks_ph3_heather_event5 with dissolve
        he "No, you got the other part right. Thanks, [name]!"
        scene ep9_diks_ph3_heather_event8 with dissolve
        mc "That wasn't what I meant! Heather!?"
        scene ep9_diks_ph3_heather_event9 with dissolve
        if affinity == "DIK":
            mc "(Oh, well.)"
        else:
            mc "(Uh... Fuck...)"
        $ task_list[9] = ""
        $ updateTaskList()
        $ new_bio("Heather", "Heather was drunk and mad at Tommy. She suspected that he was fucking Christie at the Halloween party.")
        jump endEvent
    "[mod_gr]You're not wrong":
        mc "That wasn't what I meant, but technically you're not wrong."
        mc "Why should the rules be different for you?"
        scene ep9_diks_ph3_heather_event11 with dissolve
        he "Exactly! Maybe it's my turn to be on the plus side, so he can see how it feels?"
        scene ep9_diks_ph3_heather_event12 with dissolve
        mc "Oh? With me? I..."
        scene ep9_diks_ph3_heather_event13 with dissolve
        he "Yeah, you'll get me on my way there."
        scene ep9_diks_ph3_heather_event12 with dissolve
        if branchAlone:
            if affinity == "DIK":
                mc "I mean, I'm a DIK and it's Tommy-"
            else:
                mc "Heather, we shouldn't-"
        else:
            mc "Oh! Heather, I can't-"
        scene ep9_diks_ph3_heather_event14 with dissolve
        he "Shut up, it's just a blowjob. I'm using you."
        scene ep9_diks_ph3_heather_event15 with dissolve
        if _in_replay:
            jump ep9_heather_lewd_label
        if persistent.mod_wtenabled: 
                        $mod_choices = ["(Heather scene/-2 DIKS)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if not branchAlone  or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="({color=#E6F653}+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
        if not branchAlone:
            menu:
                "Maybe in the future? \n[mod_gr][mod_choices[10]]":
                    jump ep9_heather_maybe_label
                "Refuse":
                    jump ep9_heather_no_label

        $ mc_info = ["Let her use you{size=-4}[mod_gr][mod_choices[0]]","ep9_heather_lewd_label","Maybe in the future?\n[mod_gr][mod_choices[10]] ","ep9_heather_maybe_label","Refuse","ep9_heather_no_label",False]
        show screen major_choice_screen
        $ renpy.pause()

        label ep9_heather_no_label:
        $ ep9_heather_lewd = 0
        scene ep9_diks_ph3_heather_event16 with dissolve
        mc "Heather! No!"
        scene ep9_diks_ph3_heather_event17 with dissolve
        he "Huh? What's wrong?"
        scene ep9_diks_ph3_heather_event16 with dissolve
        mc "We can't do this."
        scene ep9_diks_ph3_heather_event17 with dissolve
        he "You just said I could!"
        scene ep9_diks_ph3_heather_event16 with dissolve
        if branchAlone:
            mc "Not with me. I can't do that to Tommy. We don't see eye to eye on many things, but he's my brother."
        else:
            mc "Not with me. I'm not available and I can't do that to Tommy."
        scene ep9_diks_ph3_heather_event8b with dissolve
        he "Ugh! Fine!"
        scene ep9_diks_ph3_heather_event9 with dissolve
        mc "(Wow... I gave her some truthful advice, but she almost seems vindictive now.)"
        $ task_list[9] = ""
        $ updateTaskList()
        $ new_bio("Heather", "Heather was drunk and mad at Tommy. She suspected that he was fucking Christie at the Halloween party.")
        $ new_bio("You", "I refused Heather's advances at the Halloween party.")
        $ new_bio("Heather", "I refused Heather's advances at the Halloween party.")
        jump endEvent

        label ep9_heather_maybe_label:
        $ ep9_heather_lewd = 1
        if not branchAlone:
            $ tc += 1
        scene ep9_diks_ph3_heather_event16 with dissolve
        mc "Heather! No!"
        scene ep9_diks_ph3_heather_event17 with dissolve
        he "Huh? What's wrong?"
        scene ep9_diks_ph3_heather_event16 with dissolve
        mc "We can't do this."
        scene ep9_diks_ph3_heather_event17 with dissolve
        he "You just said I could!"
        scene ep9_diks_ph3_heather_event16 with dissolve
        mc "It's not that I don't want to, but I can't right now."
        mc "I mean, maybe in the future, if things are different for me? But not now."
        scene ep9_diks_ph3_heather_event8b with dissolve
        he "Ugh! Fine!"
        scene ep9_diks_ph3_heather_event9 with dissolve
        mc "(Wow... I gave her some truthful advice, but she almost seems vindictive now.)"
        $ task_list[9] = ""
        $ updateTaskList()
        $ new_bio("Heather", "Heather was drunk and mad at Tommy. She suspected that he was fucking Christie at the Halloween party.")
        $ new_bio("Heather", "I refused Heather's advances and told her that I'd maybe do it in the future if things were different for me.")
        $ new_bio("You", "I refused Heather's advances and told her that I'd maybe do it in the future if things were different for me.")
        jump endEvent

        label ep9_heather_lewd_label:
        $ ep9_heather_lewd = 2
        hide screen new_phone_screen
        scene ep9_diks_ph3_heather_event18 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph3_heather_event19 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph3_heather_event20 with dissolve
        mc "God... Oh fuck..."
        scene ep9_diks_ph3_heather_event21 with dissolve
        mc "Tommy will kill me for this..."
        scene ep9_diks_ph3_heather_event23 with dissolve
        he "*{i}Suck suck{/i}* He won't! He fucked my friends; I fuck his!"
        scene ep9_diks_ph3_heather_event22 with dissolve
        mc "Oh, fuck! You can suck."
        mc "Damn, your lips are so tight around my cock."
        scene ep9_diks_ph3_heather_event23 with dissolve
        he "*{i}Suck suck{/i}*"
        scene anim_heather_bj_ep9 with dissolve
        mc "(Is this really happening?)"
        he "*{i}Schlurp suck{/i}*"
        pause
        scene anim_heather_bj2_ep9 with dissolve
        pause
        scene anim_heather_bj3_ep9 with dissolve
        mc "Go deeper..."
        he "*{i}Suck suck{/i}* You sound just like Tommy!"
        he "Mmphff! I can't go deeper. I'll start gagging like crazy."
        mc "I have an idea."
        pause
        scene ep9_diks_ph3_heather_event25 with dissolve
        mc "Hold those bars for me. And don't let go, ok?"
        scene ep9_diks_ph3_heather_event26 with dissolve
        mc "Yeah... Like that... Here we go."
        scene ep9_diks_ph3_heather_event27 with dissolve
        he "*{i}Suck gag{/i}* I can't go further!"
        scene anim_heather_bj4_ep9 with dissolve
        mc "It's good enough. Keep going."
        pause
        scene anim_heather_bj5_ep9 with dissolve
        he "Mmppfhh!!!"
        mc "(She wasn't kidding. She's gagging from this.)"
        pause
        scene ep9_diks_ph3_heather_event28 with dissolve
        he "Are you seriously drinking now?"
        scene ep9_diks_ph3_heather_event29 with dissolve
        mc "I need to numb myself a bit. This is too crazy, Heather."
        scene ep9_diks_ph3_heather_event30 with dissolve
        he "Oh, please. I've seen you look at me before. Don't tell me you never wanted me."
        scene ep9_diks_ph3_heather_event31 with dissolve
        mc "Well, obviously..."
        scene ep9_diks_ph3_heather_event32 with dissolve
        if assman:
            he "You're always looking at my tits, which is ironic since they call you ass man."
            scene ep9_diks_ph3_heather_event33 with dissolve
            mc "Is it a crime to like both?"
        else:
            he "You're always looking at my tits."
            scene ep9_diks_ph3_heather_event33 with dissolve
            mc "Can you blame me?"
        scene ep9_diks_ph3_heather_event34 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph3_heather_event35 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph3_heather_event36 with dissolve
        $ renpy.pause()
        scene anim_heather_boobjob_ep9 with dissolve
        he "Tommy likes it when I do this."
        mc "Stop talking about him, ok?"
        pause
        scene anim_heather_boobjob2_ep9 with dissolve
        he "I can't believe he's fucking Christie right now! She's probably deepthroating him too."
        pause
        scene anim_heather_boobjob3_ep9 with dissolve
        he "I bet she's riding his cock too. She's such a slut!"
        mc "Damn, your tits are soft..."
        he "Huh? Yeah! You like that?"
        mc "Push them together for me."
        pause
        scene anim_heather_boobjob4_ep9 with dissolve
        pause
        scene anim_heather_bj6_ep9 with dissolve
        he "Gimme!"
        he "*{i}Suck suck{/i}*"
        mc "Yeah... Work it..."
        he "*{i}Glug glug{/i}*"
        pause
        scene anim_heather_bj7_ep9 with dissolve
        mc "Fuck!!!"
        he "*Suck gag*"
        pause

        label ep9_heather_lewd_loop_label:
        menu:
            "Blowjob (Floor)":
                scene anim_heather_bj_ep9 with dissolve
                pause
                scene anim_heather_bj2_ep9 with dissolve
                pause
                scene anim_heather_bj3_ep9 with dissolve
                pause
                scene anim_heather_bj4_ep9 with dissolve
                pause
                scene anim_heather_bj5_ep9 with dissolve
                pause
                jump ep9_heather_lewd_loop_label
            "Blowjob (Chair)":
                scene anim_heather_bj6_ep9 with dissolve
                pause
                scene anim_heather_bj7_ep9 with dissolve
                pause
                jump ep9_heather_lewd_loop_label
            "Boobjob":
                scene anim_heather_boobjob_ep9 with dissolve
                pause
                scene anim_heather_boobjob2_ep9 with dissolve
                pause
                scene anim_heather_boobjob3_ep9 with dissolve
                pause
                scene anim_heather_boobjob4_ep9 with dissolve
                pause
                jump ep9_heather_lewd_loop_label
            "Cum":
                menu:
                    "On tits":
                        scene anim_heather_boobjob_ep9 with dissolve
                        mc "I'm getting close."
                        he "Cum all over my tits. Make this worth my time."
                        pause
                        scene anim_heather_boobjob5_ep9 with hpunch
                        mc "Ahh!!! Fuck!!!"
                        scene ep9_diks_ph3_heather_event39 with dissolve
                        he "Damn, you came a lot!"
                        mc "Haha, I sure did."
                    "On face":
                        scene anim_heather_bj4_ep9 with dissolve
                        mc "Heather, I'm getting close."
                        pause
                        scene ep9_diks_ph3_heather_event40 at hpunch, cum2
                        $ renpy.pause(0.5)
                        scene ep9_diks_ph3_heather_event40 at hpunch, cum2
                        $ renpy.pause(0.5)
                        scene ep9_diks_ph3_heather_event40 at hpunch, cum2
                        he "Give it to me!"
                        scene ep9_diks_ph3_heather_event42 with dissolve
                        mc "Damn... That's gonna take some time to clean up."
                    "In mouth":
                        scene anim_heather_bj6_ep9 with dissolve
                        mc "Heather, I'm getting close."
                        pause
                        scene ep9_diks_ph3_heather_event41 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_diks_ph3_heather_event41 at hpunch, cum1
                        $ renpy.pause(0.5)
                        scene ep9_diks_ph3_heather_event41 at hpunch, cum1
                        he "Hngnnn!!!! *{i}Gag gulp{/i}*"
                        scene ep9_diks_ph3_heather_event38 with dissolve
                        he "Mmppff."
                        scene ep9_diks_ph3_heather_event37 with dissolve
                        he "Fuck! How much is that? My mouth is overflowing!"
                        scene ep9_diks_ph3_heather_event38 with dissolve
                        mc "You drained me."
        scene ep9_diks_ph3_heather_event43 with dissolve
        mc "..."
        mc "Are you good?"
        scene ep9_diks_ph3_heather_event44 with dissolve
        he "Yeah."
        he "Thanks, [name]..."
        scene ep9_diks_ph3_heather_event45 with dissolve
        mc "..."
        scene ep9_diks_ph3_heather_event46 with dissolve
        mc "(I don't know what I was expecting. She wanted to use me.)"
        mc "(It still felt weird...)"
        mc "(Tommy's gonna kill me if he finds out, but she told me she wouldn't tell him, so there's that.)"
        mc "(Well, it's done now... There's no way to undo it.)"
        $ renpy.end_replay()
        $ persistent.ep9_lewd_heather = True
        $ calcScenes()
        $ new_bio("Heather", "Heather was drunk and mad at Tommy. She suspected that he was fucking Christie at the Halloween party.")
        $ new_bio("Heather", "I got a blowjob and boobjob from Heather in Leon's room.")
        $ new_bio("You", "I got a blowjob and boobjob from Heather in Leon's room.")
        $ mphone_stats_add_girl_s3("heather","You got a boobjob and a blowjob from Heather at the Halloween party in episode 9.")
        show screen new_phone_screen
$ task_list[9] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_mj_event_label:
$ guideSuggestedPage = 80
scene ep9_diks_ph3_mj_event1 with dissolve
my "He was shot!"
scene ep9_diks_ph3_mj_event3 with dissolve
js "How can you be sure?"
scene ep9_diks_ph3_mj_event2 with dissolve
my "Because of the gun shell casing."
scene ep9_diks_ph3_mj_event3 with dissolve
js "Maybe the victim shot the murderer?"
scene ep9_diks_ph3_mj_event2 with dissolve
my "If he did, the gun wouldn't be stuck behind the couch. And there would be traces of blood."
scene ep9_diks_ph3_mj_event4 with dissolve
js "Maybe he missed and scared him off? And then put it there after shooting? Then went to drink some of his drink, and he was poisoned."
js "Aaaand..."
scene ep9_diks_ph3_mj_event5 with dissolve
js "He walked toward the bathroom or kitchen to get help or something, but collapsed right here."
scene ep9_diks_ph3_mj_event6 with dissolve
my "Aha, I see what you're getting at, but if that's the case...explain the blood."
scene ep9_diks_ph3_mj_event7 with dissolve
js "He coughed blood and died in the puddle, of course!"
scene ep9_diks_ph3_mj_event8 with dissolve
my "You think that's what happened?"
scene ep9_diks_ph3_mj_event7 with dissolve
js "Well, if you're going with the whole he-got-shot theory, why isn't there blood splatter on the walls?"
scene ep9_diks_ph3_mj_event9 with dissolve
js "Who lies down like that when they get shot?"
scene ep9_diks_ph3_mj_event8 with dissolve
my "Interesting theory... There's just one contradiction."
scene ep9_diks_ph3_mj_event10 with dissolve
my "There is lipstick on the wine glass, and I'm gonna make the fair assumption it's not his."
js "Maybe it's not his glass?"
my "Aha. What would make you say that?"
scene ep9_diks_ph3_mj_event11 with dissolve
js "We can't find a second glass. Maybe the murderer took it with them to cover up the evidence?"
scene ep9_diks_ph3_mj_event12 with dissolve
my "But you said he got scared off with a gunshot."
my "And what a stupid murderer that would have been, leaving behind their DNA on the glass."
scene ep9_diks_ph3_mj_event13 with dissolve
js "More things don't add up, though. That wine bottle wasn't even opened, and there was liquid in that glass."
scene ep9_diks_ph3_mj_event14 with dissolve
mc "Are you two detectives now?"
scene ep9_diks_ph3_mj_event15 with dissolve
my "Haha! Yes! We can't make any sense of this murder mystery!"
scene ep9_diks_ph3_mj_event16 with dissolve
js "But the fairy detectives are on it."
scene ep9_diks_ph3_mj_event17 with dissolve
mc "It's easy. He got shot."
scene ep9_diks_ph3_mj_event15 with dissolve
my "We believe it's not that simple."
scene ep9_diks_ph3_mj_event17 with dissolve
mc "Well, I believe that Tommy didn't put that much thought into this when he made it."
mc "I think he just wanted a dude with a big penis on the floor and improvised the rest."
scene ep9_diks_ph3_mj_event15 with dissolve
my "This rookie detective is no good. Right, Josy?"
scene ep9_diks_ph3_mj_event16 with dissolve
js "Yeah, I agree. Horrible detective work. No wonder there is a killer out there."
scene ep9_diks_ph3_mj_event17 with dissolve
mc "Yeah, yeah. At least you're having fun with it."
scene ep9_diks_ph3_mj_event18 with dissolve
my "Haha! That game we played before; how fun was that!?"
scene ep9_diks_ph3_mj_event19 with dissolve
js "Yeah! I can't believe that Bella is that much fun."
scene ep9_diks_ph3_mj_event20 with dissolve
my "Yeah, how awkward will it be next week in class!? Haha!"
scene ep9_diks_ph3_mj_event21 with dissolve
mc "There's nothing wrong with being friends with your teacher."
scene ep9_diks_ph3_mj_event22 with dissolve
js "It is a bit odd."
scene ep9_diks_ph3_mj_event21 with dissolve
mc "Yeah, it's likely not the usual case. But Bella isn't a usual teacher either."
if not branchMayaJosy:
    mc "I'll let you get back to solving the murder mystery."
    scene ep9_diks_ph3_mj_event23 with dissolve
    my "Maybe there's a clue we're missing?"
    js "Yes! Maybe the forensic team missed something? Let's not narrow the search down to this room. What about the hallway?"
    if "ep9_vinny_label" not in event_list:
        $ event_list.append("ep9_vinny_label")
    $ task_list[2] = "Check your room"
    $ task_list[4] = ""
    jump endEvent
scene ep9_diks_ph3_mj_event24 with dissolve
js "So, about the question you didn't answer..."
scene ep9_diks_ph3_mj_event25 with dissolve
mc "Do I still have the option to drink?"
scene ep9_diks_ph3_mj_event26 with dissolve
my "All drinking does is answer the question for you."
scene ep9_diks_ph3_mj_event24 with dissolve
js "So, she's really here?"
scene ep9_diks_ph3_mj_event27 with dissolve
mc "It's complicated, but yeah. I invited her."
mc "She's been living on the West Coast for like a year, and we recently connected again."
scene ep9_diks_ph3_mj_event28 with dissolve
mc "But it's not what you might think."
mc "Zoey's important to me. She's been my best friend for many years."
scene ep9_diks_ph3_mj_event29 with dissolve
js "And your girlfriend for how long?"
scene ep9_diks_ph3_mj_event30 with dissolve
mc "We were never official. I mean... We did things that you do as a couple, I guess. But we never said the words."
scene ep9_diks_ph3_mj_event31 with dissolve
my "The \"I love you\" words?"
scene ep9_diks_ph3_mj_event30 with dissolve
mc "No, the girlfriend, boyfriend words."
scene ep9_diks_ph3_mj_event29 with dissolve
js "Why did you break up?"
scene ep9_diks_ph3_mj_event32 with dissolve
mc "Hey, I feel like I've answered my fair share of that question already."
scene ep9_diks_ph3_mj_event33 with dissolve
my "We won't force an answer. We weren't playing the game; we were just talking now."
scene ep9_diks_ph3_mj_event30 with dissolve
mc "Personal things happened and she moved away. We lost touch, and that's about it."
scene ep9_diks_ph3_mj_event34 with dissolve
js "Thank you for letting us know."
scene ep9_diks_ph3_mj_event32 with dissolve
mc "Maybe I should have done that earlier?"
scene ep9_diks_ph3_mj_event33 with dissolve
my "You didn't lie about it, like, you know...we did about each other."
my "I believe you've earned every bit of slack you need."
scene ep9_diks_ph3_mj_event32 with dissolve
mc "Did I just kill your detective mood with this?"
scene ep9_diks_ph3_mj_event35 with dissolve
js "We're in game mode now, anyway. It's your turn with the question."
scene ep9_diks_ph3_mj_event36 with dissolve
mc "We don't have any drinks."
mc "Well, there is that wine bottle on the table, but it might be poisoned."
scene ep9_diks_ph3_mj_event37 with dissolve
js "Precisely!"
my "Haha!"
scene ep9_diks_ph3_mj_event36 with dissolve
mc "Let me get a bottle and some cups for us."
scene ep9_diks_ph3_mj_event38 with dissolve
my "No. You've already done so much tonight. Let me get it."
scene ep9_diks_ph3_mj_event35 with dissolve
js "No, I can do it."
scene ep9_diks_ph3_mj_event36 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(Heather scene)","(+Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]]
menu:
    "Alone time with Josy":
        $ ep9_alone_josy = True
        mc "Maya can fetch it for us."
        scene ep9_diks_ph3_mj_event39 with dissolve
        my "I'll grab something special from Derek's bar."
        jump ep9_diks_ph3_mj_event_josy_label
    "Alone time with Maya":
        $ ep9_alone_maya = True
        mc "Josy can fetch it for us."
        scene ep9_diks_ph3_mj_event38 with dissolve
        my "Derek had some interesting ones in his bar!"
        scene ep9_diks_ph3_mj_event40 with dissolve
        js "I'm on it! And who knows..."
        js "Maybe I find a clue on the way?"
        jump ep9_diks_ph3_mj_event_maya_label

label ep9_diks_ph3_mj_event_josy_label:
scene ep9_diks_ph3_mj_event41 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_mj_event42 with dissolve
js "What's with you tonight?"
scene ep9_diks_ph3_mj_event43 with dissolve
mc "What?"
scene ep9_diks_ph3_mj_event42 with dissolve
js "You're up to something."
scene ep9_diks_ph3_mj_event43 with dissolve
mc "What makes you say that?"
scene ep9_diks_ph3_mj_event44 with dissolve
js "You've been looking weirdly at us and smiling a lot."
scene ep9_diks_ph3_mj_event45 with dissolve
mc "I'm always happy to see you two."
scene ep9_diks_ph3_mj_event44 with dissolve
js "Hm... My detective sense tells me there's something more."
scene ep9_diks_ph3_mj_event45 with dissolve
mc "Maybe the drinking game will provide some answers."
scene ep9_diks_ph3_mj_event44 with dissolve
js "Yeah, right. You'll likely drink instead of answering."
scene ep9_diks_ph3_mj_event46 with dissolve
mc "You know me quite well. I'm impressed."
scene ep9_diks_ph3_mj_event47 with dissolve
js "Wanna know something I've been thinking about all night?"
scene ep9_diks_ph3_mj_event48 with dissolve
mc "This murder mystery?"
scene ep9_diks_ph3_mj_event47 with dissolve
js "Haha, no!"
js "I've been thinking about you."
js "And how each drink I drink makes me wanna do stuff to you."
scene ep9_diks_ph3_mj_event49 with dissolve
js "At first, I only wanted to sneak a kiss or two..."
js "Then after a couple of drinks, I wanted to lick your body."
scene ep9_diks_ph3_mj_event48 with dissolve
mc "Wow, how many drinks have you had?"
scene ep9_diks_ph3_mj_event47 with dissolve
js "I'm up to the point where I wanna wear your helmet as you fuck me on the dance floor."
scene ep9_diks_ph3_mj_event48 with dissolve
mc "That many drinks? You're an alcoholic."
scene ep9_diks_ph3_mj_event50 with dissolve
js "Hahaha!"
scene ep9_diks_ph3_mj_event51 with dissolve
js "I swear I'm just horny as hell tonight."
scene ep9_diks_ph3_mj_event52 with dissolve
mc "I promise I'll take care of that before the night is over. Deal?"
scene ep9_diks_ph3_mj_event53 with dissolve
js "Pinky swear?"
scene ep9_diks_ph3_mj_event54 with dissolve
mc "Fuck the pinky; come over here."
scene ep9_diks_ph3_mj_event55 with dissolve
js "*{i}Smack{/i}*"

scene ep9_diks_ph3_mj_event56 with dissolve
my "I'm back... Aaaand you're two minutes away from wearing birthday suits."
scene ep9_diks_ph3_mj_event57 with dissolve
js "Haha, shut up! We're not."
scene ep9_diks_ph3_mj_event58 with dissolve
my "Sure, you've been horny all night."
my "She grabbed my ass and boobs on the dance floor, [name]."
scene ep9_diks_ph3_mj_event59 with dissolve
mc "Without wearing my helmet?"
my "What?"
js "Haha!"
scene ep9_diks_ph3_mj_event58 with dissolve
my "I got us a bottle and three cups! Let's get to it!"

jump ep9_diks_ph3_mj_event2_label

label ep9_diks_ph3_mj_event_maya_label:
scene ep9_diks_ph3_mj_event60 with dissolve
my "So... I am a HOT now."
scene ep9_diks_ph3_mj_event61 with dissolve
mc "It's official?"
scene ep9_diks_ph3_mj_event62 with dissolve
my "I told Sage I'll join, but I don't know if the others know about it yet."
scene ep9_diks_ph3_mj_event61 with dissolve
mc "That's great, Maya. Congrats!"
scene ep9_diks_ph3_mj_event62 with dissolve
my "Thanks! It feels pretty good. A bit scary, but good scary."
scene ep9_diks_ph3_mj_event63 with dissolve
mc "I felt the same with the DIKs, and now I wouldn't have it any other way."
scene ep9_diks_ph3_mj_event64 with dissolve
my "If there's one thing I've seen lately is how the HOTs are much nicer than I gave them credit for."
scene ep9_diks_ph3_mj_event65 with dissolve
mc "I remember when we first met. You described them as sluts."
scene ep9_diks_ph3_mj_event66 with dissolve
my "Yeah, I remember. I feel pretty bad about that now."
my "I should have known better than to label them like that, but that's what I heard about them in high school and it stuck with me."
scene ep9_diks_ph3_mj_event65 with dissolve
mc "At least you're admitting you were wrong."
scene ep9_diks_ph3_mj_event67 with dissolve
my "I was. I like most of them. There's just one bad apple that spoiled the bunch."
my "Camila and Ashley are great. Arieth is very nice, and Riona and Sarah, too."
scene ep9_diks_ph3_mj_event68 with dissolve
my "I believe Melanie is nice, but I haven't talked to her much. And Heather is so nice to Josy that it makes me wanna like her."
my "Elena is so much fun and carefree. I'm not sure about Lily yet, though."
scene ep9_diks_ph3_mj_event69 with dissolve
mc "And Sage?"
scene ep9_diks_ph3_mj_event70 with dissolve
my "She's amazing! And it's not just because she's helping me, she actually cares about people."
my "It's so awesome to see. And she is hilarious! And interesting to talk to."
scene ep9_diks_ph3_mj_event69 with dissolve
mc "Wow, you've got a lot of good things to say about her."
scene ep9_diks_ph3_mj_event71 with dissolve
my "Yeah, so?"
scene ep9_diks_ph3_mj_event69 with dissolve
mc "It's cool that you like her that much."
scene ep9_diks_ph3_mj_event71 with dissolve
my "It feels like you're insinuating something."
scene ep9_diks_ph3_mj_event72 with dissolve
mc "You like girls. Do you never think about other girls in that way? You can't tell me it's only Josy you're attracted to."
scene ep9_diks_ph3_mj_event73 with dissolve
my "I'm attracted to you."
scene ep9_diks_ph3_mj_event75 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_mj_event74 with dissolve
mc "Thanks for that, and also, nice try. I said girls."
scene ep9_diks_ph3_mj_event73 with dissolve
my "*{i}Sigh{/i}* You wanna know if I find the HOTs hot? Is that it?"
scene ep9_diks_ph3_mj_event74 with dissolve
mc "Yeah, why not?"
scene ep9_diks_ph3_mj_event73 with dissolve
my "It sounds like guy talk."
scene ep9_diks_ph3_mj_event72 with dissolve
mc "Please, like girls don't do that too. Maybe it's a bit different than how we do it, but don't lie to me and say you never discuss who's the hottest guy or girl or whatever."
scene ep9_diks_ph3_mj_event68 with dissolve
my "Well, they all have their qualities."
scene ep9_diks_ph3_mj_event69 with dissolve
mc "Qualities? Like tits?"
scene ep9_diks_ph3_mj_event76 with dissolve
js "What on earth are you talking about?"
scene ep9_diks_ph3_mj_event77 with dissolve
my "You don't wanna know."
scene ep9_diks_ph3_mj_event78 with dissolve
js "I do! Tell me."
scene ep9_diks_ph3_mj_event77 with dissolve
my "I don't think so. Besides, that question should probably be in the drinking game."
scene ep9_diks_ph3_mj_event78 with dissolve
js "Perfect timing then, I brought us a bottle."
scene ep9_diks_ph3_mj_event79 with dissolve
mc "Thank you for getting it. Let's play..."

label ep9_diks_ph3_mj_event2_label:
if _in_replay:
    hide screen new_phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.josy == None:
        $ josy = "Josy"
    else:
        $ josy = persistent.josy
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.mc_josy == None:
        $ mc_josy = name
    else:
        $ mc_josy = persistent.mc_josy
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya
    $ RPmaya = 0
    $ RPjosy = 0
    $ ep9_alone_josy = False
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track132.mp3","music/ep9/licensed_music/track125.mp3","music/ep9/licensed_music/track124.mp3","music/ep9/licensed_music/track127.mp3"])
scene ep9_diks_ph3_mj_event80 with dissolve
my "[name], I believe it's your turn."
scene ep9_diks_ph3_mj_event81 with dissolve
mc "All right. But for fun...can't we do truth, dare or drink?"
scene ep9_diks_ph3_mj_event82 with dissolve
if ep9_alone_josy:
    my "Yeah? You're as horny as Josy tonight, too, huh?"
else:
    my "Sounds like you'll get support from Josy with that suggestion. She's been horny all night."
scene ep9_diks_ph3_mj_event98 with dissolve
js "I'm gonna pick dare every time. I wanna grab stuff."
scene ep9_diks_ph3_mj_event83 with dissolve
my "Hahaha! You're unbelievable."
scene ep9_diks_ph3_mj_event94 with dissolve
js "Shouldn't it be truth or dare, or drink? I can't just pick drink, can I?"
scene ep9_diks_ph3_mj_event93 with dissolve
mc "Truth or dare? Drink gets you out of the question or dare."

$ tmp_list = []
$ tmp_list = [[[False, False],[False, False]],[False,False],[False,False]]
label ep9_tdd_loop_label:
if not False in tmp_list[1] and not False in tmp_list[2]:
    if _in_replay:
        jump ep9_tdd_cont_label
    if ep9_maya_cluck > 0 or ep9_josy_cluck > 0:
        $ roosterState = "ep9_5"
        $ rooster_jump_label = "ep9_tdd_cont_label"
        jump initRoosterLabel
    else:
        jump ep9_tdd_cont_label
scene ep9_diks_ph3_mj_event81 with dissolve
menu:
    "Ask Maya" if False in tmp_list[1]:
        scene ep9_diks_ph3_mj_event84 with dissolve
        mc "Maya! Truth or dare?"
        if not tmp_list[1][0]:
            $ tmp_list[1][0] = True
            scene ep9_diks_ph3_mj_event82 with dissolve
            my "Truth."
            scene ep9_diks_ph3_mj_event84 with dissolve
            menu:
                "Which HOT is the hottest?":
                    mc "Which HOT is the hottest?"
                    mc "And before you cheat, you can't pick yourself or Josy."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "You've played this game before, I hear."
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "She's gonna drink to that one."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "Oh, yeah?"
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "You're not?"
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "If you promise you won't tell anyone, I won't drink."
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "Oh, fuck yes. Tell us!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "It depends on a lot of things. Like, you could say this one or that one has the best so and so."
                    my "But if I can only say one girl, based on everything I see and know right now..."
                    scene ep9_diks_ph3_mj_event88 with dissolve
                    my "Ok, maybe I should drink."
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "No! Come on, say it!"
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "It would be Sage, of course."
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "Sage!!? HAHA! No way!"
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "Oh, this is better than I thought it would be. Why?"
                    scene ep9_diks_ph3_mj_event88 with dissolve
                    my "She's so nice."
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "Ugh. Personality? That's why you're picking her?"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "I didn't say it was personality, did I?"
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "And things are good again. Go on."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "What else is there to say? She's hot, ok?"
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "You know, looks-wise, she's my polar opposite. Tall and...you know...big everything."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "That doesn't mean I don't find you hot. You know I do."
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "I get it. It's like ice cream; just because you enjoy vanilla doesn't mean you hate chocolate."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "Exactly, you can desire to put both in your mouth."
                    scene ep9_diks_ph3_mj_event95 with dissolve
                    js "Hahaha!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "Ok, now that I exposed myself, it's my turn."
                "Who is hotter? Me or Josy?":
                    mc "Who is the hotter one? Me or Josy?"
                    scene ep9_diks_ph3_mj_event99 with dissolve
                    js "Ooof! What a mean question."
                    scene ep9_diks_ph3_mj_event111 with dissolve
                    my "I'll drink to that one! Cheers!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                "Tits or ass? Which is better?":
                    mc "Tits or ass? Which is better?"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "Ass! Not even a question."
        else:
            $ tmp_list[1][1] = True
            scene ep9_diks_ph3_mj_event82 with dissolve
            my "Dare!"
            js "Yay!"
            scene ep9_diks_ph3_mj_event86 with dissolve
            my "Haha! Shut up."
            scene ep9_diks_ph3_mj_event84 with dissolve

            menu:
                mc "Big mistake... I want you to..."
                "...post an embarrassing cluck.":
                    mc "...post an embarrassing cluck."
                    scene ep9_diks_ph3_mj_event101 with dissolve
                    js "Oh, that's a good one!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "What kind of a cluck?"
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "A picture of your feet saying, \"Look at my soft and smooth feet. Aren't they pretty? #ILoveFeet\"."
                    scene ep9_diks_ph3_mj_event83 with dissolve
                    my "Hahaha! No fucking way!!!"
                    scene ep9_diks_ph3_mj_event84 with dissolve
                    mc "That's the dare."
                    scene ep9_diks_ph3_mj_event112 with dissolve
                    my "This is so ridiculous."
                    js "You're gonna do it?"
                    scene ep9_diks_ph3_mj_event113 with dissolve
                    my "I'm not scared. [name] is the one who should be the next time I ask him something."
                    scene white
                    play sound "sound_effects/camera_shutter.mp3"
                    $ renpy.pause(0.5)
                    scene ep9_diks_ph3_mj_event114 with dissolve
                    my "And post! There!"
                    mc "Hahaha! Well done!"
                    $ ep9_maya_cluck = 1
                "...stick a finger in your pussy.":
                    mc "...stick a finger in your pussy and show it to us."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "Whoa! Is this what alcohol does to you two?"
                    scene ep9_diks_ph3_mj_event102 with dissolve
                    js "I'm having the best time right now."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "I bet you think I'd drink to that, but I won't."
                    scene ep9_diks_ph3_mj_event116 with dissolve
                    $ renpy.pause()
                    scene ep9_diks_ph3_mj_event115 with dissolve
                    $ renpy.pause()
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "That looks delicious..."
                    scene ep9_diks_ph3_mj_event117 with dissolve
                    my "Yeah? Here."
                    js "Mmm..."
                    my "Haha!"
                "...send a nude to a stranger.":
                    mc "...send a nude picture to a complete stranger."
                    scene ep9_diks_ph3_mj_event111 with dissolve
                    my "Nope, I'm not doing that. No, sir."
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "She's drinking!"
            scene ep9_diks_ph3_mj_event82 with dissolve
        my "[name]! Truth or dare?"
        scene ep9_diks_ph3_mj_event84 with dissolve
        menu:
            "Truth" if not tmp_list[0][0][0]:
                $ tmp_list[0][0][0] = True
                mc "Truth."
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "How many girls have you been with?"
                scene ep9_diks_ph3_mj_event84 with dissolve
                mc "Been with how?"
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "Sexually. In any way."
                scene ep9_diks_ph3_mj_event84 with dissolve
                $ tmpInt = 3
                if not _in_replay:
                    if ep1_lewd_camila_quinn or ep3_fuckedCamilaAndMona or ep5_fuckedCamila or ep7_camila_lewd or quinn_shop_spicy_lvl>0:
                                    $ tmpInt += 1
                    if ep3_fuckedRionaQuinn or ep4_quinn_lewd or ep1_lewd_camila_quinn or ep6_quinn_lewd:
                                    $ tmpInt += 1
                    if ep3_fuckedRionaQuinn or ep2_fuckHOT or ep5_fuckedRiona or ep7_riona_lewd or quinn_shop_japanese_lvl > 0:
                                    $ tmpInt += 1
                    if ep5_cathy_lewd:
                                    $ tmpInt += 1
                    if ep4_bella_lewd or ep5_bella_lewd:
                                    $ tmpInt += 1
                    if ep4_fuckedMelanie or ep2_fuckHOT or ep5_hot_lewd or ep8_melanie_lewd:
                                    $ tmpInt += 1
                    if ep7_becky_lewd:
                                    $ tmpInt += 1
                    if ep3_fuckedCamilaAndMona:
                                    $ tmpInt += 1
                    if ep2_fuckHOT or ep5_hot_lewd or ep6_sarah_lewd or ep8_sarah_lewd:
                                    $ tmpInt += 1
                    if ep8_sarah_lewd:
                                    $ tmpInt += 2
                    if ep3_envyLewd > 0 or ep6_envy_lewd or ep8_envy_lewd:
                                    $ tmpInt += 1
                    if ep6_nora_lewd:
                                    $ tmpInt += 1
                    if ep6_envy_lewd or ep8_sandy_lewd:
                                    $ tmpInt += 1
                    if ep4_lickedAshley:
                                    $ tmpInt += 1
                    if ep4_grindedLily or ep5_lily_lewd or ep7_lily_lewd or ep8_lily_lewd:
                                    $ tmpInt += 1
                    if ep3_acceptedJade:
                                    $ tmpInt += 1
                    if ep4_roseLewd:
                                    $ tmpInt += 1
                    if ep2QuinnSawYouAndSage or ep4_fuckedSage or ep5_fuckedSage or ep7_sage_lewd:
                                    $ tmpInt += 1
                    if ep7_accept_madame:
                                    $ tmpInt += 1

                    if ep9_heather_lewd == 2:
                                    $ tmpInt += 1
                
                if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(-2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        if tmpInt >= 10:
                             $mod_choices[0]="(-3 Maya/Josy)"
                        elif tmpInt > 5:
                             $mod_choices[0]=""
                        elif tmpInt == 4:
                             $mod_choices[0]="(+1 Maya/Josy)"
                        elif tmpInt == 3:
                             $mod_choices[0]="(+3 Maya/Josy)"
                        if not branchAlone:
                             $mod_choices[10]="(Heather path open/+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
                menu:
                    "Truth [mod_gr][mod_choices[0]]":
                        mc "Well, there's you two... My ex..."
                        scene ep9_diks_ph3_mj_event94 with dissolve
                        js "Why do I have the feeling it won't end there?"
                        
                        
                            

                        if tmpInt >= 10:
                            $ RPjosy -= 3
                            $ RPmaya -= 3
                            scene ep9_diks_ph3_mj_event84 with dissolve
                            mc "Honestly... I don't keep count. But it's probably more than 10."
                            scene ep9_diks_ph3_mj_event89 with dissolve
                            my "That many? No way!"
                            scene ep9_diks_ph3_mj_event99 with dissolve
                            js "More than 10!?"
                            scene ep9_diks_ph3_mj_event100 with dissolve
                            mc "Yeah."
                            scene ep9_diks_ph3_mj_event99 with dissolve
                            js "Who?"
                            scene ep9_diks_ph3_mj_event100 with dissolve
                            mc "That wasn't part of the question."
                            scene ep9_diks_ph3_mj_event99 with dissolve
                            js "Wow... That's...a lot!"
                            scene ep9_diks_ph3_mj_event89 with dissolve
                            my "Yeah."
                        elif tmpInt > 5:
                            scene ep9_diks_ph3_mj_event84 with dissolve
                            mc "It's just a few more."
                            scene ep9_diks_ph3_mj_event94 with dissolve
                            js "Less than 10?"
                            scene ep9_diks_ph3_mj_event93 with dissolve
                            mc "Yeah, definitely. Please."
                            scene ep9_diks_ph3_mj_event92 with dissolve
                            my "Interesting..."
                        elif tmpInt == 4:
                            $ RPjosy += 1
                            $ RPmaya += 1
                            scene ep9_diks_ph3_mj_event84 with dissolve
                            mc "Maybe one more or two, but that's about it."
                            scene ep9_diks_ph3_mj_event94 with dissolve
                            js "Who?"
                            scene ep9_diks_ph3_mj_event93 with dissolve
                            mc "That wasn't part of the question."
                            scene ep9_diks_ph3_mj_event82 with dissolve
                            my "I didn't expect it to be that few. That's amazing."
                        elif tmpInt == 3:
                            $ RPjosy += 3
                            $ RPmaya += 3
                            scene ep9_diks_ph3_mj_event84 with dissolve
                            mc "It does."
                            scene ep9_diks_ph3_mj_event103 with dissolve
                            js "No way."
                            scene ep9_diks_ph3_mj_event104 with dissolve
                            mc "Way."
                            scene ep9_diks_ph3_mj_event82 with dissolve
                            my "That's incredibly sweet."
                            scene ep9_diks_ph3_mj_event103 with dissolve
                            js "It is. Wow..."
                    "Drink [mod_gr][mod_choices[1]]":
                        $ RPjosy -= 2
                        $ RPmaya -= 2
                        scene ep9_diks_ph3_mj_event97 with dissolve
                        js "You got him."
                        scene ep9_diks_ph3_mj_event92 with dissolve
                        my "Yep, [name] is a slut. Confirmed!"
                        scene ep9_diks_ph3_mj_event90 with dissolve
                        mc "I'm not a slut. I was thirsty."
                        scene ep9_diks_ph3_mj_event92 with dissolve
                        my "Yep. You sure are thirsty."
                        scene ep9_diks_ph3_mj_event94 with dissolve
                        js "Thirsty, thirsty. Haha!"
            "Dare" if not tmp_list[0][0][1]:
                $ tmp_list[0][0][1] = True
                mc "Dare."
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "Now you're in for it..."
                scene ep9_diks_ph3_mj_event84 with dissolve
                mc "What's with that evil smile?"
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "I wanna see if you're brave enough to do this..."
                my "We're in Rusty's room, that door isn't locked and anyone could walk in on us, really."
                scene ep9_diks_ph3_mj_event84 with dissolve
                mc "What do I have to do with my cock?"
                scene ep9_diks_ph3_mj_event83 with dissolve
                my "Haha! Why did you assume it was something about your dick?"
                scene ep9_diks_ph3_mj_event84 with dissolve
                mc "It is, isn't it?"
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "Of course, it is."
                scene ep9_diks_ph3_mj_event84 with dissolve
                mc "See?"
                scene ep9_diks_ph3_mj_event101 with dissolve
                js "Haha! Yay!"
                scene ep9_diks_ph3_mj_event82 with dissolve
                my "Stand up and let Josy make out with your cock for one minute."
                scene ep9_diks_ph3_mj_event96 with dissolve
                js "Hey, this isn't my dare, is it?"
                scene ep9_diks_ph3_mj_event85 with dissolve
                my "It's a dare for both of you."
                scene ep9_diks_ph3_mj_event118 with dissolve
                mc "One minute?"
                my "My heart just started racing. You're doing it?"
                scene ep9_diks_ph3_mj_event119 with dissolve
                mc "It depends on this girl."
                scene ep9_diks_ph3_mj_event120 with dissolve
                js "Well, this girl says whip it out."
                scene anim_josy_suck_ep9 with dissolve
                my "You guys are crazy!"
                mc "It was your dare."
                scene ep9_diks_ph3_mj_event121 with dissolve
                js "Just like his cock, the minute is up."
                scene ep9_diks_ph3_mj_event122 with dissolve
                mc "That was a minute?"
                my "Yeah... Good job, you two."
        jump ep9_tdd_loop_label
    "Ask Josy" if False in tmp_list[2]:
        scene ep9_diks_ph3_mj_event93 with dissolve
        mc "Josy! Truth or dare?"
        if not tmp_list[2][1]:
            $ tmp_list[2][1] = True
            scene ep9_diks_ph3_mj_event101 with dissolve
            js "Dare, all the way!"
            scene ep9_diks_ph3_mj_event86 with dissolve
            my "Haha, are you for real?"
            scene ep9_diks_ph3_mj_event94 with dissolve
            js "I don't think [name] will be too mean. Right?"
            scene ep9_diks_ph3_mj_event93 with dissolve
            menu:
                "Squeeze Maya's ass":
                    mc "Squeeze and fondle Maya's ass."
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "I think I'm gonna drink."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "Why? If someone catches us, we can say we're playing this game."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "He's not wrong. I mean, unless you're scared."
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "No way, I told you I wanted to grab stuff."
                    scene ep9_diks_ph3_mj_event86 with dissolve
                    my "Haha, then do it!"
                    scene anim_josy_squeeze_ep9 with dissolve
                    js "For how long should I do it?"
                    mc "Just a little more..."
                    my "He is so getting off to this."
                    pause
                    mc "Ok, you can stop. Very nice!"
                "Shake your butt":
                    mc "Pull down your pants and panties, and shake your butt for us."
                    scene ep9_diks_ph3_mj_event101 with dissolve
                    js "That's what you wanna see? My butt?"
                    scene ep9_diks_ph3_mj_event86 with dissolve
                    my "Haha, I'm with [name] on this one. Woooo! Show us that ass!"
                    scene ep9_diks_ph3_mj_event96 with dissolve
                    js "Hey, not so loud! It would be my luck if someone entered now."
                    scene anim_josy_shake_ep9 with dissolve
                    mc "Shake it!"
                    my "Yeah!!!"
                    js "Haha! Shh!!!"
                    my "Up and down and all around!"
                    pause
                    scene ep9_diks_ph3_mj_event123 with dissolve
                    js "That's all you get from me."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "I'm very pleased."
                "Let us post a cluck for you":
                    mc "Let us use your phone and post a cluck for you."
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "Nah, come on. Not happening."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "Let's do this. Maya and I say out loud what it will be, and if you decide it's too bad, you drink."
                    scene ep9_diks_ph3_mj_event124 with dissolve
                    js "Knowing you two, it's gonna be bad."
                    scene ep9_diks_ph3_mj_event125 with dissolve
                    mc "Give me a frown for the camera."
                    scene white
                    play sound "sound_effects/camera_shutter.mp3"
                    $ renpy.pause(0.5)
                    scene ep9_diks_ph3_mj_event126 with dissolve
                    mc "Haha! Perfect!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "Let's see, I'll start and you fill in, [name]..."

                    menu:
                        my "\"The DIKs' party is awesome, but I'm a bit sad I...\""
                        "...didn't bring more condoms.":
                            $ ep9_josy_cluck = 1
                            scene ep9_diks_ph3_mj_event100 with dissolve
                            mc "...didn't bring more condoms. #TooManyHotGuys"
                            scene ep9_diks_ph3_mj_event83 with dissolve
                            my "Haha! Oh my God! Yes! And then that picture of her frowning!"
                            scene ep9_diks_ph3_mj_event96 with dissolve
                            js "Haha! No way! Do you know how much damage that would do? People wouldn't let me hear the end of it."
                        "...came dressed as a fairy, when...":
                            $ ep9_josy_cluck = 2
                            scene ep9_diks_ph3_mj_event84 with dissolve
                            mc "...came dressed as a fairy, when..."
                            scene ep9_diks_ph3_mj_event83 with dissolve
                            my "...I wanted to come as a baby with a diaper. #MeLikeyDiapers"
                            my "And then that picture of her frowning!"
                            scene ep9_diks_ph3_mj_event96 with dissolve
                            js "Haha! No way! I'd look like the biggest creep posting that!"
                    scene ep9_diks_ph3_mj_event100 with dissolve
                    mc "You could play it off as a joke."
                    scene ep9_diks_ph3_mj_event99 with dissolve
                    js "If you post that, I'm gonna blame you!"
                    scene ep9_diks_ph3_mj_event100 with dissolve
                    menu:
                        "Post it":
                            mc "I'm gonna post it, and you can't defend yourself for an hour. Ok?"
                            scene ep9_diks_ph3_mj_event101 with dissolve
                            js "Damn you two. But I'm not a chicken. Do it!"
                            scene ep9_diks_ph3_mj_event83 with dissolve
                            my "Haha! I can't wait to read the comment section!"
                        "Don't post it":
                            $ ep9_josy_cluck = 0
                            mc "You can always drink."
                            scene ep9_diks_ph3_mj_event109 with dissolve
                            mc "And she does it..."
                            scene ep9_diks_ph3_mj_event83 with dissolve
                            my "Haha, aw... So close!"
        else:
            $ tmp_list[2][0] = True
            scene ep9_diks_ph3_mj_event94 with dissolve
            js "Hit me with some truth this time."
            scene ep9_diks_ph3_mj_event93 with dissolve
            mc "Ok... Let's see..."
            menu:
                "Dream foursome":
                    mc "If you could add anyone to a foursome with me and Maya, who would it be and why?"
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "It would probably be a celebrity."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "No, it's gotta be someone we know, and someone you think would be hot or interesting to have join."
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "I'm not sure if she's gonna pick a guy or a girl."
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "Oh, it would definitely be a girl."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "Why?"
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "That's more fun for all of us. But I can't choose who."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "Are you sure? I bet a few names popped up in your head just now."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "Yeah, you said it would be a girl pretty quickly."
                    scene ep9_diks_ph3_mj_event108 with dissolve
                    js "No, I can't answer this. It's too embarrassing."
                    scene ep9_diks_ph3_mj_event109 with dissolve
                    mc "No, don't drink! Come on!"
                    scene ep9_diks_ph3_mj_event82 with dissolve
                    my "She's blushing, haha! She definitely knows."
                    scene ep9_diks_ph3_mj_event109 with dissolve
                    mc "I'm disappointed."
                    scene ep9_diks_ph3_mj_event110 with dissolve
                    js "*{i}Sigh{/i}* Fine! It would either be Jill, Sage or Lily."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "Three girls!? Wow! You're serious."
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "Yeah, yeah. Whatever! Is it my turn already?"
                "Isabella, Jade or Cathy?":
                    mc "If you had to sleep with a teacher, who would it be? You can pick between Isabella, Jade or Cathy."
                    scene ep9_diks_ph3_mj_event99 with dissolve
                    js "What? That's such a weird question."
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "Not really. They are all pretty."
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "Yeah? Who would you pick?"
                    scene ep9_diks_ph3_mj_event85 with dissolve
                    my "It's not my question to answer. You're up."
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "I don't feel like answering that one. It's too weird."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "That's a shame."
                    scene ep9_diks_ph3_mj_event94 with dissolve
                    js "They're all pretty, but I don't have the desire to sleep with any of them."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "It wasn't about desire; the question was if you had to do it."
                    scene ep9_diks_ph3_mj_event101 with dissolve
                    js "Then probably Cathy. She scares me the least."
                    scene ep9_diks_ph3_mj_event86 with dissolve
                    my "Haha! That's a good one."
                "Wildest thing":
                    mc "If there were no consequences to your actions, what's the wildest thing you would do?"
                    scene ep9_diks_ph3_mj_event97 with dissolve
                    js "That one is easy for me. I wouldn't hide you two from anyone."
                    scene ep9_diks_ph3_mj_event105 with dissolve
                    js "I'd be making out with you both in public, walking through school, holding your hands and talking openly about how I feel about you."
                    scene ep9_diks_ph3_mj_event87 with dissolve
                    my "While that doesn't sound wild, it is wild to me."
                    scene ep9_diks_ph3_mj_event93 with dissolve
                    mc "That's a great answer. A very sweet one."
        scene ep9_diks_ph3_mj_event94 with dissolve
        js "Truth or dare, [name]?"
        scene ep9_diks_ph3_mj_event93 with dissolve
        menu:
            "Truth" if not tmp_list[0][1][0]:
                $ tmp_list[0][1][0] = True
                mc "I'll go with truth."
                scene ep9_diks_ph3_mj_event94 with dissolve
                js "What would have been different for you today if your ex-girlfriend had never left town?"
                scene ep9_diks_ph3_mj_event106 with dissolve
                mc "..."
                menu:
                    "Truth":
                        mc "I'd probably not be here today. I think I would have gone with her wherever she wanted if she had waited for me."
                        mc "We talked about moving to Miami for beaches and college. But who knows?"
                        scene ep9_diks_ph3_mj_event107 with dissolve
                        js "So, you still think you would have been together with her?"
                        scene ep9_diks_ph3_mj_event106 with dissolve
                        mc "Uh... It's hard to say."
                        mc "All I know is that if she didn't leave, I couldn't say why it wouldn't have lasted longer. We were very close."
                        if persistent.mod_wtenabled: 
                            $mod_choices = ["(Jade scene)","(-Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                            #[mod_gr][mod_choices[0]]
                        menu:
                            "I wish I knew [mod_gr][mod_choices[1]]":
                                $ RPmaya -= 1
                                $ RPjosy -= 1
                                mc "But I wish I knew for sure."
                            "It's for the best":
                                mc "But it's probably for the best."
                        mc "One thing is sure, I wouldn't have met you two or sat here playing this game."
                        mc "And that would have sucked."
                        scene ep9_diks_ph3_mj_event94 with dissolve
                        js "Thanks for your honest answer. I wouldn't have blamed you if you drank to that one."
                        scene ep9_diks_ph3_mj_event91 with dissolve
                        my "Are you ok?"
                        scene ep9_diks_ph3_mj_event84 with dissolve
                        mc "Yeah. Of course, I am. It's my turn to ask you stuff."
                    "Drink":
                        mc "Sorry, but that one is a bit too tough to answer for me."
                        scene ep9_diks_ph3_mj_event99 with dissolve
                        js "That bad?"
                        scene ep9_diks_ph3_mj_event100 with dissolve
                        mc "I don't wanna speculate. Things would have been different; that's all I know."
            "Dare" if not tmp_list[0][1][1]:
                $ tmp_list[0][1][1] = True
                mc "Dare me something."
                scene ep9_diks_ph3_mj_event101 with dissolve
                js "I dare you to..."
                js "...lick..."
                js "...Maya's panties for one minute."
                scene ep9_diks_ph3_mj_event93 with dissolve
                if persistent.mod_wtenabled: 
                            $mod_choices = ["(Jade scene)","(-2 Maya)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                            #[mod_gr][mod_choices[0]]
                menu:
                    "[mod_gr]Do it":
                        mc "I'm gonna have to remove my helmet for this one."
                        scene ep9_diks_ph3_mj_event85 with dissolve
                        my "I've gotta stand up for this?"
                        scene anim_maya_panties_lick_ep9 with dissolve
                        my "*{i}Moans{/i}*"
                        js "Haha... This game... Is it just me or has it gotten out of hand?"
                        my "Then don't tell us to do these things, haha..."
                        js "How's that tongue?"
                        my "Warm and wet... My panties do nothing to stop me from feeling all of it..."
                        scene ep9_diks_ph3_mj_event127 with dissolve
                        my "*{i}Phew{/i}* Are you done?"
                        mc "Sadly, it was just for one minute."
                    "Drink [mod_gr][mod_choices[1]]":
                        $ RPmaya -= 2
                        mc "No, I'm gonna have myself a drink instead."
                        scene ep9_diks_ph3_mj_event89 with dissolve
                        my "What the hell?"
                        scene ep9_diks_ph3_mj_event90 with dissolve
                        mc "You wanted me to do it?"
                        scene ep9_diks_ph3_mj_event89 with dissolve
                        my "I didn't expect you to jump on the drink."
        jump ep9_tdd_loop_label

label ep9_tdd_cont_label:
scene ep9_diks_ph3_mj_event81 with dissolve
mc "I'm gonna dare both of you right now..."
scene ep9_diks_ph3_mj_event94 with dissolve
js "Are you changing the rules?"
scene ep9_diks_ph3_mj_event93 with dissolve
mc "Yeah, it's the dare game now."
scene ep9_diks_ph3_mj_event101 with dissolve
js "The dare game? I like that name."
scene ep9_diks_ph3_mj_event89 with dissolve
my "Wait. Just dares? No drinks?"
scene ep9_diks_ph3_mj_event81 with dissolve
mc "Nope. You're either in or out; that's the rule of the dare game. Here's the dare..."
mc "I dare you two to remove your tops; whoever keeps it off the longest wins."
scene ep9_diks_ph3_mj_event101 with dissolve
js "What? Like some kind of a chicken race?"
scene ep9_diks_ph3_mj_event93 with dissolve
mc "Yeah! A titty chicken race."
scene ep9_diks_ph3_mj_event83 with dissolve
my "Hahaha! You've completely lost it."
scene ep9_diks_ph3_mj_event81 with dissolve
mc "It's not that bad. Look at me, I'm already topless. And don't act like we haven't done worse stuff together."
scene ep9_diks_ph3_mj_event128 with dissolve
my "No way! You're doing it?"
scene ep9_diks_ph3_mj_event129 with dissolve
js "I am! Because I'm not the chicken. You are!"
scene ep9_diks_ph3_mj_event130 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_mj_event131 with dissolve
my "Game on!"
scene ep9_diks_ph3_mj_event132 with dissolve
js "Come on... Put it back on so I win, already."
scene ep9_diks_ph3_mj_event131 with dissolve
my "Nope. You do it!"
scene ep9_diks_ph3_mj_event132 with dissolve
js "I can stay like this forever."
scene ep9_diks_ph3_mj_event131 with dissolve
my "Oh, yeah? Then why didn't you come to the party like that?"
scene ep9_diks_ph3_mj_event132 with dissolve
js "You're gonna choke. You don't have it in you."
scene ep9_diks_ph3_mj_event133 with dissolve
mc "I have to give it to both of you... I didn't think either would last this long or even do it."
scene ep9_diks_ph3_mj_event132 with dissolve
js "I'm telling you, I'm gonna go all night."
scene ep9_diks_ph3_mj_event131 with dissolve
my "You're such a liar right now!"
scene ep9_diks_ph3_mj_event134 with dissolve
my "Haha! Don't try to act casual on me."
my "I'm the casual one."
scene ep9_diks_ph3_mj_event135 with dissolve
my "In fact, I think I'm gonna continue my investigation."
scene ep9_diks_ph3_mj_event136 with dissolve
js "You're already way behind. I think I saw a clue out in the hallway."
scene ep9_diks_ph3_mj_event137 with dissolve
my "N-no, you didn't."
scene ep9_diks_ph3_mj_event136 with dissolve
js "I think I did."
scene ep9_diks_ph3_mj_event138 with vpunch
le "Yeah, the good liquor is over here."
js "Ah!"
my "Holy..."
scene ep9_diks_ph3_mj_event139 with dissolve
le "[name]... Nice."
scene ep9_diks_ph3_mj_event140 with dissolve
mc "It's just a drinking game..."
scene ep9_diks_ph3_mj_event139 with dissolve
le "Yeah, yeah. Over here, guys."
scene ep9_diks_ph3_mj_event141 with dissolve
my "Josy... Look."
scene ep9_diks_ph3_mj_event142 with dissolve
js "Hahaha!"
my "Hahaha!"
scene ep9_diks_ph3_mj_event143 with dissolve
mc "You girls just proved me wrong."
js "I think we both won that dare."
my "Haha! We sure did."
scene ep9_diks_ph3_mj_event144 with dissolve
js "Perhaps we should get out of here before something worse happens?"
scene ep9_diks_ph3_mj_event143 with dissolve
mc "Yeah, I think that was our cue to leave."
$ renpy.end_replay()
$ persistent.ep9_lewd_jm2 = True
$ calcScenes()
$ new_bio("Josy", "Josy, Maya, and I coined \"The Dare Game\" and dared each other to do lewd things.")
$ new_bio("Maya", "Josy, Maya, and I coined \"The Dare Game\" and dared each other to do lewd things.")
if "ep9_vinny_label" not in event_list:
    $ event_list.append("ep9_vinny_label")
$ task_list[2] = "Check your room"
$ task_list[4] = ""
jump endEvent

label ep9_diks_ph3_qt2_event_label:
play music "music/ep9/licensed_music/track128.mp3"
scene ep9_diks_ph3_qt2_event1 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qt2_event2 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qt2_event3 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qt2_event3b with dissolve
$ renpy.pause()
scene ep9_rox1 with dissolve
$ renpy.pause()
scene ep9_rox2 with dissolve
rx "Mhm..."
scene ep9_rox3 with dissolve
$ renpy.pause()
scene ep9_rox4 with dissolve
rx "What are you gonna do now, Q?"
scene ep9_rox6 with dissolve
rx "Not that one."
scene ep9_rox5 with dissolve
$ renpy.pause()
scene ep9_rox6 with dissolve
rx "You're still going with it? All right..."
scene ep9_rox7 with dissolve
rx "Don't say I didn't warn you."
scene ep9_rox8 with dissolve
rx "Checkmate."
rx "See? I warned ya."
scene ep9_rox9 with dissolve
rx "Never make a move without planning for your next one."
rx "Now. Spot how to fix your mistake."
scene ep9_rox10 with dissolve
rx "Yeah, that's my girl."
scene ep9_rox11 with dissolve
rx "I outsmarted you. By dangling something obvious and valuable in front of you..."
scene ep9_rox12 with dissolve
rx "...you didn't see what I tried to hide."
scene ep9_rox13 with dissolve
rx "Always think one step ahead. It's not just a lesson in chess, baby girl."
rx "You can't trust anyone in life..."
rx "...except for your dad, you hear?"
scene ep9_rox14 with dissolve
rx "And even if you're forced to trust someone else..."
rx "Keep them at arm's length without letting them know about it."
scene ep9_rox15 with dissolve
rx "Because trust can be taken away instantly."
rx "Just like your king trusted the pawns around him to keep him safe, but instead they trapped him and became the end of him."
scene ep9_rox16 with dissolve
bd "Ey."
rx "Whaddya want?"
scene ep9_rox17 with dissolve
bd "Eli was short."
rx "Then no pay, this time."
bd "None?"
scene ep9_rox18 with dissolve
rx "None. Tell him to get his shit together or I'll dump him off where we found him."
scene ep9_rox19 with dissolve
$ renpy.pause()
scene ep9_rox20 with dissolve
rx "Case in point. You can't trust anyone. Not your pawns. No one."
rx "Only your dad."
rx "And Buddy too. At arm's length. Remember?"
scene ep9_rox21 with dissolve
rx "..."
scene ep9_rox20 with dissolve
rx "*{i}Sigh{/i}* Look at you..."
rx "You're old enough to play chess... Are you old enough to keep a secret?"
scene ep9_rox21 with dissolve
rx "..."
scene ep9_rox20 with dissolve
rx "You've seen Daddy's safe, right? I wanna show you something."
rx "And not a word to your mom, ok?"

scene ep9_diks_ph3_qt2_event4 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qt2_event5 with dissolve
tm "Vinny left."
scene ep9_diks_ph3_qt2_event6b with dissolve
qu "Just like that?"
scene ep9_diks_ph3_qt2_event5 with dissolve
tm "Not really. He..."
tm "He threatened [name] with a gun."
scene ep9_diks_ph3_qt2_event6 with dissolve
qu "..."
scene ep9_diks_ph3_qt2_event7 with dissolve
qu "What the fuck happened in there?"
scene ep9_diks_ph3_qt2_event8 with dissolve
tm "People heard some arguing and told me about it. I went to check and there he was..."
tm "In his old room, squaring off with [name]."
scene ep9_diks_ph3_qt2_event9 with dissolve
if ep9_vinny_choice == "DIK":
    tm "Looked like [name] tried to beat the shit out of him too."
else:
    tm "They didn't fight, but it didn't stop Vinny."
scene ep9_diks_ph3_qt2_event8 with dissolve
tm "He flashed a gun and told [name] to back off. And called him a dog to his face."
scene ep9_diks_ph3_qt2_event7 with dissolve
qu "How did [name] handle it?"
scene ep9_diks_ph3_qt2_event8 with dissolve
tm "He was shaken up."
tm "I calmed Vinny down, asked him to leave and he did."
scene ep9_diks_ph3_qt2_event7 with dissolve
qu "Was [name] freaking out?"
scene ep9_diks_ph3_qt2_event8 with dissolve
tm "Yeah, he wanted to call the cops, but I calmed him down too. I told him it was the prop gun from Rusty's room that Vinny fucked around with."
scene ep9_diks_ph3_qt2_event10 with dissolve
tm "This one."
scene ep9_diks_ph3_qt2_event11 with dissolve
tm "[name] cannot know it was a real one."
scene ep9_diks_ph3_qt2_event12 with dissolve
qu "Tommy..."
scene ep9_diks_ph3_qt2_event15 with dissolve
tm "This is all my fault. If I hadn't bought from Vinny, he wouldn't have shown up."
scene ep9_diks_ph3_qt2_event13 with dissolve
qu "..."
scene ep9_diks_ph3_qt2_event14 with dissolve
qu "No."
qu "This is my fault."
scene ep9_diks_ph3_qt2_event16 with dissolve
qu "If I hadn't been so fucking stubborn and told you I was sorry, we wouldn't even be in this spot."
scene ep9_diks_ph3_qt2_event17 with dissolve
tm "Well, you weren't sorry, so..."
scene ep9_diks_ph3_qt2_event18 with dissolve
qu "I was."
qu "But it's a weakness to say it."
scene ep9_diks_ph3_qt2_event17 with dissolve
tm "It's not a weakness to own your mistakes. It's the fucking opposite."
scene ep9_diks_ph3_qt2_event18 with dissolve
qu "I'm sorry. I fucked up."
scene ep9_diks_ph3_qt2_event17 with dissolve
tm "I forgive you."
scene ep9_diks_ph3_qt2_event19 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_qt2_event20 with dissolve
qu "I stole Vinny's customers."
qu "That's why I didn't want him back snooping around."
scene ep9_diks_ph3_qt2_event21 with dissolve
tm "I know. Tania told me."
scene ep9_diks_ph3_qt2_event20 with dissolve
qu "I think Vinny figured it out."
scene ep9_diks_ph3_qt2_event21 with dissolve
tm "I told Tania to shut up about it. And it looks like Lily told the others to do the same."
scene ep9_diks_ph3_qt2_event22 with dissolve
qu "I don't know..."
qu "Vinny's smarter than you give him credit for."
scene ep9_diks_ph3_qt2_event21 with dissolve
tm "He's been overcharging them for everything."
scene ep9_diks_ph3_qt2_event20 with dissolve
qu "That's Vinny for you."
qu "So, what are we gonna do?"
scene ep9_diks_ph3_qt2_event21 with dissolve
tm "I guess I'm back to buying from you."
scene ep9_diks_ph3_qt2_event22 with dissolve
qu "That won't make him stay away."
scene ep9_diks_ph3_qt2_event23 with dissolve
tm "It's a start."
scene ep9_diks_ph3_qt2_event22 with dissolve
qu "It is."
qu "Party's awesome, by the way."
scene ep9_diks_ph3_qt2_event24 with dissolve
if (minigames and pp_current_party_happiness[7] > 1) or (not minigames and pp_current_party_happiness[7] == 1):
    tm "Best Halloween party we had, that's for sure."
else:
    tm "Most seem to love it."
stop music fadeout 3
if ep8_mansion_won:
    tm "Sometimes I hate [name] for being good at everything. It's fucking annoying."
else:
    tm "It's fucking annoying how [name] is learning shit faster than we did around here. I hate it."

if branchAlone and ep8_quinn_lewd:
    $ event_list.append("ep9_diks_ph3_quinn_event_label")
    if persistent.mod_wtenabled:
        $ optional_task_list[5] = "Talk to Quinn (Main party room)"
    else:
        $ optional_task_list[5] = "Talk to Quinn"
    $ updateTaskList()
$ mphone_next_song()
jump endEvent

label ep9_diks_ph3_dz_event_label:
scene ep9_diks_ph3_dz_event1 with dissolve
de "Saying that doesn't prove that you're his best friend, you know."
if ep8_revenge == "DIK":
    de "Did you ever let him make out with your twin sister, streak through the mall, throw piss balloons at someone with him or comfort him while being naked?"
else:
    de "Did you ever let him make out with your twin sister, streak through the mall, or comfort him while being naked?"
scene ep9_diks_ph3_dz_event4 with dissolve
zo "Dude, you've got issues."
scene ep9_diks_ph3_dz_event1 with dissolve
de "I know... And I'm drunk."
scene ep9_diks_ph3_dz_event4 with dissolve
zo "I couldn't tell."
scene ep9_diks_ph3_dz_event3 with dissolve
de "I hide it well."
de "Answer my question."
scene ep9_diks_ph3_dz_event2 with dissolve
zo "It's a party. You should be thrashing, not asking me bullshit questions!"
scene ep9_diks_ph3_dz_event1 with dissolve
de "Yeah! I should!"
scene ep9_diks_ph3_dz_event2 with dissolve
zo "Hell yeah, dude. Do some moonwalking, stick a flag into something or ride a rocket."
scene ep9_diks_ph3_dz_event5 with dissolve
de "You just gave me the idea of the century."
if ep9_josy_choice == "DIK":
    scene ep9_diks_ph3_dz_event6 with dissolve
    zo "Look who it is... Mr. On-a-mission-to-get-expelled-guy."
    scene ep9_diks_ph3_dz_event8 with dissolve
    mc "Sorry, you had to see that."
    scene ep9_diks_ph3_dz_event9 with dissolve
    zo "Since when do you punch people?"
    scene ep9_diks_ph3_dz_event8 with dissolve
    mc "Don't knock it. That's why we met."
    scene ep9_diks_ph3_dz_event9 with dissolve
    if emma_calm:
        zo "[name]... You're better than that."
        scene ep9_diks_ph3_dz_event8 with dissolve
        mc "It's the alcohol and he was rude to Josy."
        scene ep9_diks_ph3_dz_event9 with dissolve
        zo "If you're gonna punch every asshat you meet, it won't end well."
        scene ep9_diks_ph3_dz_event8 with dissolve
        mc "He got to me. Ok?"
        scene ep9_diks_ph3_dz_event10 with dissolve
        $ renpy.pause()
        scene ep9_diks_ph3_dz_event8 with dissolve
    else:
        zo "I get it; sometimes you're pushed to your limits. Just be careful with that, ok?"
        scene ep9_diks_ph3_dz_event8 with dissolve
        mc "Yeah. It's the alcohol, and he was rude to Josy."
else:
    scene ep9_diks_ph3_dz_event7 with dissolve
mc "Was Derek bothering you?"
scene ep9_diks_ph3_dz_event9 with dissolve
zo "Meh, he's harmless. That's your best friend?"
scene ep9_diks_ph3_dz_event11 with dissolve
mc "We are close, yeah. He was my maggot brother when we pledged the DIKs."
scene ep9_diks_ph3_dz_event12 with dissolve
zo "What's a maggot brother?"
scene ep9_diks_ph3_dz_event11 with dissolve
mc "It's someone you have to stick by and pass Hell Week together with. It's a long story; I'll tell you about it sometime."
scene ep9_diks_ph3_dz_event12 with dissolve
zo "I've heard a lot about your adventures tonight."
scene ep9_diks_ph3_dz_event11 with dissolve
mc "Yeah? Are people talking about me?"
scene ep9_diks_ph3_dz_event13 with dissolve
zo "Some are. I can tell they like you a lot. You seem to have made your mark here."
scene ep9_diks_ph3_dz_event11 with dissolve
mc "Yeah, maybe I have."
scene ep9_diks_ph3_dz_event14 with dissolve
zo "And, somehow, your dick has been the subject of conversation more than once tonight."
scene ep9_diks_ph3_dz_event15 with dissolve
mc "My dick?"
scene ep9_diks_ph3_dz_event16 with dissolve
zo "Dude, people here are weird. Like super-weird."
scene ep9_diks_ph3_dz_event17 with dissolve
mc "I guess some are."
scene ep9_diks_ph3_dz_event16 with dissolve
zo "But it's cool; I prefer weird over normal."
scene ep9_diks_ph3_dz_event17 with dissolve
mc "You managed to catch us on a wild night."
scene ep9_diks_ph3_dz_event16 with dissolve
zo "No shit. I saw some girl flashing her tits to people."
scene ep9_diks_ph3_dz_event17 with dissolve
mc "That's probably one of the strippers..."
scene ep9_diks_ph3_dz_event18 with dissolve
zo "You hired strippers for Halloween?"
scene ep9_diks_ph3_dz_event17 with dissolve
mc "Kinda."
scene ep9_diks_ph3_dz_event12 with dissolve
zo "Party planner, much?"
scene ep9_diks_ph3_dz_event11 with dissolve
mc "Look, they're friends of the DIKs too. And they are pretty cool people, profession put aside."
scene ep9_diks_ph3_dz_event12 with dissolve
zo "Hey, I'm not judging."
zo "And it's good too, you know. Now people won't be weirded out when I flash them mine."
scene ep9_diks_ph3_dz_event19 with dissolve
mc "Funny."
scene ep9_diks_ph3_dz_event20 with dissolve
zo "Who's joking?"
scene ep9_diks_ph3_dz_event19 with dissolve
mc "You, I hope."
$ event_list.append("ep9_diks_ph3_zoey2_event_label")
if persistent.mod_wtenabled:
    $ task_list[14] = "Find Zoey (Tommy's room)"
else:
    $ task_list[14] = "Find Zoey"
$ task_list[10] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_zoey_event_label:
scene ep9_diks_ph3_costume_zoey_event1 with dissolve
zo "Why are you walking around staring at people's asses?"
scene ep9_diks_ph3_costume_zoey_event2 with dissolve
if affinity == "DIK":
    mc "It's an added benefit of being a judge for the costume contest."
    scene ep9_diks_ph3_costume_zoey_event3 with dissolve
    zo "Tsk."
else:
    mc "I'm not. I'm checking everyone's costumes for the contest."
    scene ep9_diks_ph3_costume_zoey_event3 with dissolve
    zo "Uh-huh."
scene ep9_diks_ph3_costume_zoey_event4 with dissolve
mc "I need to check yours too."
scene ep9_diks_ph3_costume_zoey_event5 with dissolve
zo "It's not much of a costume. I bought something off-the-rack."
scene ep9_diks_ph3_costume_zoey_event4 with dissolve
mc "Most did that and it doesn't matter. A good costume is a good costume."
label ep9_diks_ph3_costume_zoey_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_zoey_eventb_label")
scene ep9_diks_ph3_costume_zoey_event5 with dissolve
zo "So, what about mine? Is it good enough for the contest?"
scene ep9_diks_ph3_costume_zoey_event6 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_costume_zoey_event7 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_costume_zoey_event4 with dissolve
menu:
    "Put Zoey in your top three":
        if not "Zoey" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Zoey"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Zoey"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Zoey"
            else:
                menu:
                    "{i}Choose who to replace with Zoey{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Zoey"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Zoey"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Zoey"
                    "Don't put Zoey in top three":
                        $ renpy.pause(0.5)
        mc "Yeah. It's a good one."
    "Haven't decided yet":
        mc "It's not bad. But I haven't decided yet."

if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_riona_event_label:
scene ep9_diks_ph3_costume_riona_event1 with dissolve
ri "Are you checking me out because of what Sage said or for another reason?"
scene ep9_diks_ph3_costume_riona_event2 with dissolve
mc "Wouldn't you like to know?"
label ep9_diks_ph3_costume_riona_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_riona_eventb_label")
scene ep9_diks_ph3_costume_riona_event1 with dissolve
ri "Am I in your top three for the contest, [name]?"
scene ep9_diks_ph3_costume_riona_event2 with dissolve
menu:
    "Put Riona in your top three":
        if not "Riona" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Riona"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Riona"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Riona"
            else:
                menu:
                    "{i}Choose who to replace with Riona{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Riona"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Riona"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Riona"
                    "Don't put Riona in top three":
                        $ renpy.pause(0.5)
        mc "Maybe you are, maybe you aren't. We'll see."
    "Haven't decided yet":
        mc "I haven't decided yet."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_camila_event_label:
$ event_list.append("ep9_diks_ph3_costume_camila_event_label")
scene ep9_diks_ph3_costume_camila_event1 with dissolve
cam "[name]. Look at me."
cam "Top three. Am I right?"
scene ep9_diks_ph3_costume_camila_event2 with dissolve
menu:
    "Put Camila in your top three":
        if not "Camila" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Camila"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Camila"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Camila"
            else:
                menu:
                    "{i}Choose who to replace with Camila{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Camila"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Camila"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Camila"
                    "Don't put Camila in top three":
                        $ renpy.pause(0.5)
        mc "You make a strong case for it."
    "Haven't decided yet":
        mc "I'm not sure... You might be."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_nl_event_label:
scene ep9_diks_ph3_costume_nl_event1 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_costume_nl_event2 with dissolve
ly "Look at [name] not being shy."
mc "Huh?"
scene ep9_diks_ph3_costume_nl_event3 with dissolve
nic "Haha! What the hell are you up to?"
scene ep9_diks_ph3_costume_nl_event4 with dissolve
mc "I'm a judge for the best costume competition and I need to pick three entries for it."
scene ep9_diks_ph3_costume_nl_event3 with dissolve
nic "There's a competition? Damn, what's the prize?"
scene ep9_diks_ph3_costume_nl_event4 with dissolve
mc "Um... A trophy of sorts."
scene ep9_diks_ph3_costume_nl_event5 with dissolve
ly "Who are your picks?"
scene ep9_diks_ph3_costume_nl_event4 with dissolve
mc "I'm still undecided."
scene ep9_diks_ph3_costume_nl_event6 with dissolve
ly "Well, look at Nic. Look how hot she is tonight."
ly "She clearly made an effort for this party. Tight clothes and very stylish, right?"
scene ep9_diks_ph3_costume_nl_event7 with dissolve
nic "What about you? [name]! Look at that makeup. It might look sloppy, but that's not easy to pull off, let me tell you."
scene ep9_diks_ph3_costume_nl_event8 with dissolve
nic "And that's no outfit she normally wears; she got it for this party. Lily's just as serious about Halloween as I am."
scene ep9_diks_ph3_costume_nl_event4 with dissolve
mc "You both make good cases. Thanks!"

label ep9_diks_ph3_costume_nl_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_nl_eventb_label")
scene ep9_diks_ph3_costume_nl_event5 with dissolve
ly "So? What about it? Are we in the top three for the competition?"
scene ep9_diks_ph3_costume_nl_event4 with dissolve
menu:
    "Put Lily in your top three":
        if not "Lily" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Lily"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Lily"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Lily"
            else:
                menu:
                    "{i}Choose who to replace with Lily{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Lily"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Lily"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Lily"
                    "Don't put Lily in top three":
                        $ renpy.pause(0.5)
        mc "I can't spoil that, sorry."
    "Put Nicole in your top three":
        if not "Nicole" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Nicole"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Nicole"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Nicole"
            else:
                menu:
                    "{i}Choose who to replace with Nicole{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Nicole"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Nicole"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Nicole"
                    "Don't put Nicole in top three":
                        $ renpy.pause(0.5)
        mc "I can't spoil that, sorry."
    "Put both in your top three":
        if not "Lily" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Lily"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Lily"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Lily"
            else:
                menu:
                    "{i}Choose who to replace with Lily{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Lily"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Lily"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Lily"
                    "Don't put Lily in top three":
                        $ renpy.pause(0.5)
        if not "Nicole" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Nicole"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Nicole"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Nicole"
            else:
                menu:
                    "{i}Choose who to replace with Nicole{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Nicole"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Nicole"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Nicole"
                    "Don't put Nicole in top three":
                        $ renpy.pause(0.5)
        mc "I think I might have to pick both of you... But I'm not the only judge."
    "Haven't decided yet":
        mc "I still need time to decide. So, we'll have to wait and see."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_sm_event_label:
scene ep9_diks_ph3_costume_sm_event1 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_costume_sm_event2 with dissolve
sar "What are you up to, [name]?"
scene ep9_diks_ph3_costume_sm_event3 with dissolve
mc "I'm checking up on stuff. What about you?"
scene ep9_diks_ph3_costume_sm_event4 with dissolve
ml "We heard from Quinn about your booze stash, haha!"
scene ep9_diks_ph3_costume_sm_event3 with dissolve
mc "Ah, so you figured you'd help yourselves?"
scene ep9_diks_ph3_costume_sm_event2 with dissolve
sar "We can, can't we?"
scene ep9_diks_ph3_costume_sm_event3 with dissolve
mc "Haha, of course. You're paying for half of it anyway."
scene ep9_diks_ph3_costume_sm_event4 with dissolve
ml "Score!"
scene ep9_diks_ph3_costume_sm_event3 with dissolve
mc "As for me, I'm taking a final look at costumes for the contest."
scene ep9_diks_ph3_costume_sm_event5 with dissolve
ml "Look no further. Here's your answer."
scene ep9_diks_ph3_costume_sm_event6 with dissolve
sar "Haha! You're joking, right? Why would he pick the lesser bunny when number one is available?"
scene ep9_diks_ph3_costume_sm_event5 with dissolve
ml "Because [name] is a sexy, smart and fair judge."
scene ep9_diks_ph3_costume_sm_event2 with dissolve
sar "How about it, [name]? Will you break the news to her that I'm the better-looking bunny?"
scene ep9_diks_ph3_costume_sm_event7 with dissolve
sar "[name]. [name]... Look."
scene ep9_diks_ph3_costume_sm_event8 with dissolve
sar "Best bunny, right here. Ok?"
scene ep9_diks_ph3_costume_sm_event9 with dissolve
ml "Yeah! Look! Perky ones are better than saggy ones, huh?"
sar "Fuck you!"

scene ep9_diks_ph3_costume_sm_event10 with dissolve
ml "Wanna touch them? Check for yourself."
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(Heather path open/+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"

menu:
    "Touch their tits [mod_gr][mod_choices[11]]":
        if not branchAlone:
            $ tc += 2
        mc "Maybe for a little while..."
        scene anim_mel_sarah_squeeze1_ep9 with dissolve
        mc "Yeah... These are great."
        sar "[name]! [name]! Mine too."
        scene anim_mel_sarah_squeeze2_ep9 with dissolve
        mc "I'm not done here yet."
        scene anim_mel_sarah_squeeze3_ep9 with dissolve
        mc "Ok... Here we go."
        sar "See!? They're not saggy, right?"
        scene anim_mel_sarah_squeeze4_ep9 with dissolve
        mc "They're definitely not saggy."
        sar "Hah!"
        if affinity == "DIK":
            mc "But Mel's are perkier."
            ml "HAH!"
            sar "Fuck you!"
    "Don't touch them":
        if affinity == "DIK":
            mc "Thanks, but I can see they're great from here."
        else:
            mc "Easy, girls..."

label ep9_diks_ph3_costume_sm_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_sm_eventb_label")

scene ep9_diks_ph3_costume_sm_event2 with dissolve
sar "Come on, [name]. Tell us already! Am I in the top three?"
scene ep9_diks_ph3_costume_sm_event3 with dissolve
menu:
    "Put Sarah in your top three":
        if not "Sarah" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Sarah"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Sarah"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Sarah"
            else:
                menu:
                    "{i}Choose who to replace with Sarah{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Sarah"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Sarah"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Sarah"
                    "Don't put in top three":
                        $ renpy.pause(0.5)
        mc "I'm a judge; I can't spoil that for you."
    "Put Melanie in your top three":
        if not "Melanie" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Melanie"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Melanie"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Melanie"
            else:
                menu:
                    "{i}Choose who to replace with Melanie{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Melanie"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Melanie"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Melanie"
                    "Don't put Melanie in top three":
                        $ renpy.pause(0.5)
        mc "I'm a judge; I can't spoil that for you."
    "Put both in your top three":
        if not "Sarah" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Sarah"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Sarah"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Sarah"
            else:
                menu:
                    "{i}Choose who to replace with Sarah{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Sarah"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Sarah"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Sarah"
                    "Don't put Sarah in top three":
                        $ renpy.pause(0.5)
        if not "Melanie" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Melanie"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Melanie"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Melanie"
            else:
                menu:
                    "{i}Choose who to replace with Melanie{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Melanie"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Melanie"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Melanie"
                    "Don't put Melanie in top three":
                        $ renpy.pause(0.5)
        mc "I'd pick both of you. But I guess we'll find out at the competition what Sage and Quinn think."
    "Haven't decided yet":
        mc "I'm a judge; I can't spoil that for you."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_elena_event_label:
scene ep9_diks_ph3_costume_elena_event1 with dissolve
jb "Is it time for the contest yet?"
scene ep9_diks_ph3_costume_elena_event2 with dissolve
mc "Almost. I'm picking my entries for it."
scene ep9_diks_ph3_costume_elena_event1 with dissolve
jb "Cool. If you're gonna pick a cowboy costume, pick Elena. I'm not too comfortable with the spotlight."
scene ep9_diks_ph3_costume_elena_event2 with dissolve
mc "What are you talking about? You're frequently almost-nude."
scene ep9_diks_ph3_costume_elena_event1 with dissolve
jb "In the background, yeah. But not on stages."
scene ep9_diks_ph3_costume_elena_event3 with dissolve
el "Aw, baby. It's fine. You'd do good on stage."
label ep9_diks_ph3_costume_elena_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_elena_eventb_label")
scene ep9_diks_ph3_costume_elena_event1 with dissolve
jb "You're not picking me, right?"
scene ep9_diks_ph3_costume_elena_event2 with dissolve
menu:
    "Put John Boy in your top three":
        if not "John Boy" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "John Boy"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "John Boy"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "John Boy"
            else:
                menu:
                    "{i}Choose who to replace with John Boy{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "John Boy"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "John Boy"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "John Boy"
                    "Don't put John Boy in top three":
                        $ renpy.pause(0.5)
    "Put Elena in your top three":
        if not "Elena" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Elena"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Elena"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Elena"
            else:
                menu:
                    "{i}Choose who to replace with Elena{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Elena"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Elena"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Elena"
                    "Don't put Elena in top three":
                        $ renpy.pause(0.5)
    "Put both in your top three":
        if not "John Boy" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "John Boy"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "John Boy"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "John Boy"
            else:
                menu:
                    "{i}Choose who to replace with John Boy{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "John Boy"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "John Boy"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "John Boy"
                    "Don't put John Boy in top three":
                        $ renpy.pause(0.5)
        if not "Elena" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Elena"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Elena"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Elena"
            else:
                menu:
                    "{i}Choose who to replace with Elena{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Elena"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Elena"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Elena"
                    "Don't put Elena in top three":
                        $ renpy.pause(0.5)
    "Haven't decided yet":
        $ renpy.pause(0.5)
mc "Drink some more if you're scared of the stage. Anything can happen tonight."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_jill_event_label:
scene ep9_diks_ph3_costume_jill_event1 with dissolve
mc "Question... Is it bad if you're a judge in a contest and you choose your girlfriend as the winner?"
scene ep9_diks_ph3_costume_jill_event2 with dissolve
ji "Yes, that doesn't sound very fair to me."
scene ep9_diks_ph3_costume_jill_event3 with dissolve
bia "Yeah, that's a bit unfair."
scene ep9_diks_ph3_costume_jill_event1 with dissolve
mc "But what about if she deserved to win?"
scene ep9_diks_ph3_costume_jill_event2 with dissolve
ji "Hm. I still think it's in poor taste. Why are you asking?"
scene ep9_diks_ph3_costume_jill_event1 with dissolve
mc "I'm judging a best costume contest and was considering you."
scene ep9_diks_ph3_costume_jill_event4 with dissolve
ji "Then I'm gonna add to my answer..."
ji "Don't do that."
scene ep9_diks_ph3_costume_jill_event5 with dissolve
bia "Haha! And I'm gonna change my answer. It sounds super-fair if you ask me!"
ji "Bianca!"
scene ep9_diks_ph3_costume_jill_event1 with dissolve
mc "Haha, why don't you want it?"
scene ep9_diks_ph3_costume_jill_event2 with dissolve
ji "Because I'm dressed as a banana, [name]. I'd be embarrassed."

label ep9_diks_ph3_costume_jill_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_jill_eventb_label")
scene ep9_diks_ph3_costume_jill_event1 with dissolve
menu:
    "Put Jill in your top three":
        if not "Jill" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Jill"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Jill"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Jill"
            else:
                menu:
                    "{i}Choose who to replace with Jill{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Jill"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Jill"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Jill"
                    "Don't put Jill in top three":
                        $ renpy.pause(0.5)
    "Haven't decided yet":
        $ renpy.pause(0.5)
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_lily2_event_label:
mc "I'm getting involved with someone, so..."
if ep7_lily_lewd:
    scene ep9_diks_ph3_lily_event46 with dissolve
    ly "For real?"

if envyLikesYou:
    scene ep9_diks_ph3_lily_event47 with dissolve
    nic "Really? Wow... That's such a bummer... Fuck."
    nic "I thought we were gonna date more."
    scene ep9_diks_ph3_lily_event52 with dissolve
    ly "You're dating him?"
    nic "Just a bit, but not really. We only had some fun in the past, but this sucks."
    scene ep9_diks_ph3_lily_event48 with dissolve
    nic "Lucky her, [name]."
    scene ep9_diks_ph3_lily_event49 with dissolve
    mc "Thanks. And I'm sorry."
    scene ep9_diks_ph3_lily_event48 with dissolve
    nic "*{i}Sigh{/i}* Don't be. Story of my life."
    $ new_bio("Envy", "Nicole was disappointed when I told her that I was getting involved with someone.")
else:
    scene ep9_diks_ph3_lily_event50 with dissolve
    nic "You are? Good for you! Someone bagged a hottie."
    scene ep9_diks_ph3_lily_event51 with dissolve
    mc "Yeah, haha. I did."
    scene ep9_diks_ph3_lily_event50 with dissolve
    nic "No, I meant the girl did."
    scene ep9_diks_ph3_lily_event51 with dissolve
    mc "Thanks! It feels pretty good."
$ task_list[5] = "Talk to Tommy"
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_derek_event_label:
scene ep9_diks_ph3_costume_derek_event1 with dissolve
mc "Bro? You alive?"
scene ep9_diks_ph3_costume_derek_event2 with dissolve
de "I think I drank too much."
scene ep9_diks_ph3_costume_derek_event1 with dissolve
mc "You think?"
scene ep9_diks_ph3_costume_derek_event2 with dissolve
de "I'll be...fine. Give me a minute."
scene ep9_diks_ph3_costume_derek_event1 with dissolve
mc "I'm not gonna pick you for best costume if you can't walk."
label ep9_diks_ph3_costume_derek_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_derek_eventb_label")
scene ep9_diks_ph3_costume_derek_event3 with dissolve
de "I'm winning best costume?"
scene ep9_diks_ph3_costume_derek_event4 with dissolve
menu:
    "Put Derek in your top three":
        if not "Derek" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Derek"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Derek"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Derek"
            else:
                menu:
                    "{i}Choose who to replace with Derek{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Derek"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Derek"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Derek"
                    "Don't put Derek in top three":
                        $ renpy.pause(0.5)
        mc "Maybe. Try to sober up a bit, though."
    "Haven't decided yet":
        mc "Not if you can't walk."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_prepsg_event_label:
scene ep9_diks_ph3_prepsg_event1 with dissolve
$ renpy.pause()
if ep9_prep_truce:
    scene ep9_diks_ph3_prepsg_event2 with dissolve
    go "Beth?"
    scene ep9_diks_ph3_prepsg_event4 with dissolve
    beth "Gordon? What are you doing here?"
    scene ep9_diks_ph3_prepsg_event3 with dissolve
    go "I can't believe this! You're making out with another one now!?"
    go "What about...us!?"
    scene ep9_diks_ph3_prepsg_event5 with dissolve
    $ renpy.pause()
    $ task_list[11] = ""
    $ updateTaskList()
else:
    scene ep9_diks_ph3_prepsg_event6 with dissolve
    lu "It's open. Let's go."
    scene ep9_diks_ph3_prepsg_event7 with dissolve
    cr "Perfect. Let's split up and blend in."
    scene ep9_diks_ph3_prepsg_event8 with dissolve
    go "Beth!?"
    scene ep9_diks_ph3_prepsg_event9 with dissolve
    beth "Gordon? What are you doing here?"
    scene ep9_diks_ph3_prepsg_event10 with dissolve
    go "I can't believe this! You're making out with another one now!?"
    scene ep9_diks_ph3_prepsg_event11 with dissolve
    lu "Gogo? Where are you going?"
    scene ep9_diks_ph3_prepsg_event12 with dissolve
    go "I'm going back to the REAL party!"
    scene ep9_diks_ph3_prepsg_event13 with dissolve
    cr "*{i}Whispers{/i}* That's the girl he was talking about."
    scene ep9_diks_ph3_prepsg_event14 with dissolve
    lu "Oh, no... Do we have to follow him back?"
    scene ep9_diks_ph3_prepsg_event13 with dissolve
    cr "It feels like we should, but..."
    scene ep9_diks_ph3_prepsg_event14 with dissolve
    lu "Let's stay for a little while. Please? We made it inside."
    scene ep9_diks_ph3_prepsg_event13 with dissolve
    cr "Yeah. Let's split up and look around."
    if persistent.mod_wtenabled:
        $ task_list[11] = "Kick out the preps(Left hallway,Tommy's room)"
    else:
        $ task_list[11] = "Kick out the preps"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_preps_event_label:
$ guideSuggestedPage = 75
scene ep9_diks_ph3_preps_event1 with dissolve
jb "[name]. We need some backup at the front door."
scene ep9_diks_ph3_preps_event2 with dissolve
mc "What's the problem?"
scene ep9_diks_ph3_preps_event3 with dissolve
jb "Preps are showing up."
scene ep9_diks_ph3_preps_event2 with dissolve
mc "Preps? Dammit. Not tonight..."
scene ep9_diks_ph3_preps_event4 with dissolve
cr "We won't cause you any problems."
scene ep9_diks_ph3_preps_event5 with dissolve
mc "Hey. What's going on?"
ni "See for yourself."
if ep8_prep_truce:
    scene ep9_diks_ph3_preps_event6 with dissolve
    go "Hey, it's this guy! He's all right."
else:
    scene ep9_diks_ph3_preps_event7 with dissolve
    go "Ugh... Not this guy..."
scene ep9_diks_ph3_preps_event8 with dissolve
lu "Can we join your party? We really wanna go."
scene ep9_diks_ph3_preps_event9 with dissolve
jb "Don't you guys have your own party tonight?"
ni "Yeah, they do."
scene ep9_diks_ph3_preps_event8 with dissolve
lu "It's not a party. It's..."
lu "Halloween is supposed to be fun and we heard you guys are it tonight."
if ep8_prep_truce:
    scene ep9_diks_ph3_preps_event9 with dissolve
    
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(-DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
    
    menu:
        "Let them in [mod_gr][mod_choices[0]]":
            $ ep9_prep_truce = True
            $ event_list.append("ep9_diks_ph3_prepsg_event_label")
            scene ep9_diks_ph3_preps_event9 with dissolve
            mc "I wish I could, but you're preps and we're DIKs. You know what I'm getting at?"
            scene ep9_diks_ph3_preps_event10 with dissolve
            cr "These frat wars are so stupid. Can't we call another truce?"
            scene ep9_diks_ph3_preps_event9 with dissolve
            ni "What do you mean by another truce?"
            mc "Derek and I were cool with them at the dorm party."
            scene ep9_diks_ph3_preps_event11 with dissolve
            go "Exactly! And look how well that went. We didn't fight and we all had a great night."
            go "Let's do that again. Think of it like diplomacy."
            scene ep9_diks_ph3_preps_event9 with dissolve
            mc "(Fuck... Tommy told me to kick preps out if they showed up...)"
            scene ep9_diks_ph3_preps_event10 with dissolve
            cr "Be a pal and let us in."
            scene ep9_diks_ph3_preps_event9 with dissolve
            mc "I'm going against my better judgment on this..."
            ni "Are you sure?"
            jb "Yeah, I don't know about this one."
            mc "Ok. Get in here. But if anything happens..."
            scene ep9_diks_ph3_preps_event10 with dissolve
            cr "It's on us!"
            scene ep9_diks_ph3_preps_event12 with dissolve
            lu "Super!"
            go "Much obliged!"
            $ new_bio("Christian", "I let the preps into our Halloween party.")
            $ new_bio("Lucas", "I let the preps into our Halloween party.")
            $ new_bio("Gordon", "I let the preps into our Halloween party.")
            $ task_list[11] = "Check the theater"
            $ updateTaskList()
        "Turn them away":
            label ep9_turn_away_label:
            $ ep9_prep_truce = False
            $ event_list.append("ep9_diks_ph3_prepsl_event_label")
            $ event_list.append("ep9_diks_ph3_prepsc_event_label")
            scene ep9_diks_ph3_preps_event13 with dissolve
            if affinity == "DIK" and not ep8_prep_truce:
                mc "Hell no. Fuck off!"
                play sound "sound_effects/door_slam.mp3"
                scene ep9_diks_ph3_preps_event14 with hpunch
            else:
                mc "Look. You already have a party to go to. Stick to your party and leave ours alone."
                mc "We're full tonight."
                scene ep9_diks_ph3_preps_event14 with dissolve
            jb "Good call."
            ni "Yeah. I'm with you on this one."
            scene ep9_diks_ph3_preps_event15 with dissolve
            if ep8_prep_truce:
                lu "What an asshole! Is this the guy you said was cool? Him? Really?"
            else:
                lu "What an asshole!"
            scene ep9_diks_ph3_preps_event16 with dissolve
            if ep8_prep_truce:
                go "He's probably acting tough around his chums."
            else:
                go "Major ass."
            scene ep9_diks_ph3_preps_event17 with dissolve
            cr "I'm not giving up that easily. They snuck into our party; let's find a way to sneak into theirs."
            $ new_bio("Christian", "I didn't let the preps into our Halloween party.")
            $ new_bio("Lucas", "I didn't let the preps into our Halloween party.")
            $ new_bio("Gordon", "I didn't let the preps into our Halloween party.")
            jump ep9_diks_ph3_prepsg_event_label
else:
    jump ep9_turn_away_label
jump endEvent

label ep9_diks_ph3_penny_event_label:
scene ep9_diks_ph3_penny_event1 with dissolve
py "*{i}Moans{/i}* Yes, like that..."
play sound "sound_effects/slap.mp3"
scene ep9_diks_ph3_penny_event2 with vpunch
mc "What the fuck did I walk in on?"
py "Ah!! Shit!"
scene ep9_diks_ph3_penny_event3 with dissolve
py "What are you doing in here!?"
scene ep9_diks_ph3_penny_event4 with dissolve
if branchSage and ep9_haunted_mansion:
    mc "Great, now we're even for the basement. I don't have to apologize to you, and you don't have to apologize to me."
else:
    mc "Unless it's Jamie who turned himself into a scuba diver, I could ask you the same thing."
    mc "This door is supposed to stay unlocked. Anyway... Have fun!"
if affinity == "DIK":
    scene ep9_diks_ph3_penny_event5 with dissolve
    mc "Penny! I'm loving the body paint. Now, that's dedication!"
    $ currentFreeRoamLabel = "ep9_diks_ph3_jamie_label"

$ optional_task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_jm_breakup_label:
$ ep9_jm_sad = True
scene ep9_jm_breakup1 with dissolve
js "[name]?"
mc "Huh?"
scene ep9_jm_breakup2 with dissolve
my "Hi!"
scene ep9_jm_breakup3 with dissolve
mc "Hey..."
scene ep9_jm_breakup2 with dissolve
my "You've been very busy tonight. Did you even have time to enjoy the party?"
scene ep9_jm_breakup3 with dissolve
mc "Yeah, I've had...fun."
scene ep9_jm_breakup2 with dissolve
my "So... Were you planning on talking to us tonight or...?"
my "It feels like you've been avoiding us."
scene ep9_jm_breakup3 with dissolve
mc "Can you two follow me?"
scene ep9_jm_breakup4 with dissolve
play music "music/ep7/licensed_music/track44.mp3"
my "What's wrong, [name]? Are you not feeling well?"
scene ep9_jm_breakup5 with dissolve
mc "..."
scene ep9_jm_breakup6 with dissolve
mc "No, I'm not."
mc "Recently, I haven't been there for you. I know you've felt it too."
scene ep9_jm_breakup7 with dissolve
my "You've been busy, no?"
scene ep9_jm_breakup6 with dissolve
mc "Yes, but also, no..."
mc "I've waited for the dust to settle since we went to the Burkes and for the right moment to tell you two something..."
mc "...and the longer I waited, the worse I felt. Which made me stay away from you, so I didn't feel bad."
scene ep9_jm_breakup10 with dissolve
js "What's going on? You're scaring me."
scene ep9_jm_breakup8 with dissolve
mc "There's no good way to tell you this. But I have to..."
scene ep9_jm_breakup11 with dissolve
my "He's breaking up with us..."
scene ep9_jm_breakup10 with dissolve
js "What!? No!"
scene ep9_jm_breakup9 with dissolve
mc "Let me explain."
mc "Remember how we said that we wouldn't have any strings attached when we talked about us three?"
if branchJill:
    mc "I didn't stop dating Jill, and with time we..."
    mc "She's my girlfriend."
if branchSage:
    mc "Sage and I have gotten very close. Ever since I got here, we've been hanging out."
    mc "And now it's turned into something real for me."
if branchIsabella:
    mc "I didn't stop dating, and I think I found something I want to pursue..."
    mc "It's still early, but my heart has already decided on it."
scene ep9_jm_breakup12 with dissolve
mc "I can't see you anymore. I mean, I still want to be friends, but this thing we started together..."
mc "It has to end. And I didn't know how to tell you this..."
scene ep9_jm_breakup13 with dissolve
$ renpy.pause()
scene ep9_jm_breakup14 with dissolve
mc "Josy, please, don't go..."
scene ep9_jm_breakup15 with dissolve
mc "Josy!?"
scene ep9_jm_breakup16 with dissolve
my "..."
scene ep9_jm_breakup17 with dissolve
mc "Maya... Please... I hope you can forgive me."
scene ep9_jm_breakup18 with dissolve
$ renpy.pause()
scene ep9_jm_breakup19 with dissolve
$ renpy.pause()
if ep8_maya_lewd or ep7_solo_maya or ep5_fucked_maya or ep3_mayaLewd:
    scene ep9_jm_breakup20 with dissolve
    if ep8_maya_lewd or ep7_solo_maya or ep5_fucked_maya:
        my "You made me feel things I had never felt before. *{i}Exhales{/i}*"
    my "You opened my eyes to something new."
    my "I can't believe it's over, just like that."
    scene ep9_jm_breakup19 with dissolve
    mc "I'm so sorry."
    if affinity == "CHICK":
        mc "*{i}Sobs{/i}* It hurts so much."
    else:
        mc "It's not been easy for me."
    scene ep9_jm_breakup21 with dissolve
    $ renpy.pause()
    scene ep9_jm_breakup20 with dissolve
    my "[name]... It hurts, but it's ok. We said no strings attached."
else:
    scene ep9_jm_breakup20 with dissolve
    my "[name]... It hurts, but it's ok. We said no strings attached."
    my "I loved the three of us together. So, it's sad that it has to end like this."
    my "But don't feel bad, ok?"

scene ep9_jm_breakup22 with dissolve
my "No one can force you to feel different."
my "You can't control your feelings, and suppressing them... Believe me, you don't want to go down that road like me."
scene ep9_jm_breakup23 with dissolve
$ renpy.pause()
scene ep9_jm_breakup22 with dissolve
my "I have to go find Josy."
scene ep9_jm_breakup23 with dissolve
mc "I can't end it like this with her. I must find her too."
scene ep9_jm_breakup22 with dissolve
my "No, please don't. Not tonight. Trust me on this."
scene ep9_jm_breakup24 with dissolve
$ renpy.pause()
scene ep9_jm_breakup25 with dissolve
mc "(Why does this hurt so fucking much?)"
mc "(This can't be a mistake, can it?)"
stop music fadeout 3
scene ep9_jm_breakup26 with dissolve
mc "(No. It hurts because I care about them.)"
$ new_bio("Josy", "I broke up with Josy and Maya at the end of the Halloween party. It sucked, but it had to be done.")
$ new_bio("Maya", "I broke up with Josy and Maya at the end of the Halloween party. It sucked, but it had to be done.")
if branchJill and wt_ep9_end_pick=="Jill":
    mc "(But Jill is the one I want to be with.)"
    scene ep9_jm_breakup27 with dissolve
    ji "Hey! Careful, so you don't slip on me."
    scene ep9_jm_breakup28 with dissolve
    $ renpy.pause()
    scene ep9_jm_breakup29 with dissolve
    ji "What? I thought that was funny."
    scene ep9_jm_breakup30 with dissolve
    mc "It was, I'm just..."
    mc "I broke it off with two girls I've been dating."
    scene ep9_jm_breakup31 with dissolve
    ji "Two!?"
    scene ep9_jm_breakup30 with dissolve
    mc "Yeah, I'm done now. I can be completely yours."
    scene ep9_jm_breakup32 with dissolve
    ji "You look sad."
    scene ep9_jm_breakup33 with dissolve
    mc "I am. I hurt them."
    mc "I didn't want this to hang over my shoulder when we are official."
    scene ep9_jm_breakup32 with dissolve
    ji "I don't know how to respond."
    scene ep9_jm_breakup33 with dissolve
    mc "You don't have to say anything about it. I just wanted you to know."
    mc "To let you know that I'm serious about us."
    scene ep9_jm_breakup34 with dissolve
    ji "That's...wonderful to know."
    scene ep9_jm_breakup35 with vpunch
    ji "Gah!"
    scene ep9_jm_breakup36 with dissolve
    ji "Sorry... I'm feeling so stupid wearing this now. I'm beginning to think I couldn't have picked a worse costume."
    scene ep9_jm_breakup37 with dissolve
    mc "I love that costume. It makes me smile."
    scene ep9_jm_breakup38 with dissolve
    ji "Wanna grab some air?"
    scene ep9_jm_breakup37 with dissolve
    mc "Let's..."
    jump ep9_jill_lewd2_label
elif branchSage and wt_ep9_end_pick=="Sage":
    mc "(But I want to be with Sage.)"
    jump ep9_sage_hunt_label
elif True and wt_ep9_end_pick=="Bella":
    mc "(But my feelings for Bella are stronger.)"
    jump ep9_bella_lewd2_label

label ep9_diks_ph3_rusty_event_label:
if "ep9_diks_ph3_riona_event_label" not in event_list and "ep9_diks_ph3_dz_event_label" not in event_list and "ep9_diks_ph3_zoey2_event_label" not in event_list and "ep9_diks_ph3_prg_event_label" not in event_list and "ep9_diks_ph3_lily_event_label" not in event_list and "ep9_diks_ph3_cumpetition_event_label" not in event_list and "ep9_diks_ph3_qv_event_label" not in event_list:
    $ task_list[1] = "Check the porch"
    $ event_list.append("ep9_diks_ph3_sage_event_label")
scene ep9_diks_ph3_rusty_event1b with dissolve
tan "Haha! Lily? Really?"
scene ep9_diks_ph3_rusty_event5b with dissolve
sn "Yeah! I kinda see it."
scene ep9_diks_ph3_rusty_event4b with dissolve
le "It would have been better if Jamie wore his costume too. I feel stupid wearing this."
scene ep9_diks_ph3_rusty_event2b with dissolve
tan "Aw! Don't feel stupid. You look...good!"
scene ep9_diks_ph3_rusty_event6b with dissolve
sn "Did anyone see Rusty or is he in too good of a costume to notice?"
scene ep9_diks_ph3_rusty_event3b with dissolve
tan "I just came back from a smoke and saw him on the rooftop. He seemed a bit off or drunk."
scene ep9_diks_ph3_rusty_event4b with dissolve
stop music fadeout 3
mc "(Huh? I should check that out.)"
scene ep9_diks_ph3_rusty_event1
hide screen dance_filter_screen
with wipeleft
$ renpy.pause()
play music "music/ep9/relaxed.mp3"
scene ep9_diks_ph3_rusty_event2 with dissolve
mc "Rusty?"
mc "There you are. What are you doing up here by yourself?"
scene ep9_diks_ph3_rusty_event3 with dissolve
rs "Did you know that flirting is harmless?"
scene ep9_diks_ph3_rusty_event4 with dissolve
mc "That kind of depends..."
scene ep9_diks_ph3_rusty_event3 with dissolve
rs "It doesn't feel harmless."
scene ep9_diks_ph3_rusty_event5 with dissolve
mc "What happened?"
scene ep9_diks_ph3_rusty_event6 with dissolve
rs "Micha's got a boyfriend."
mc "..."
scene ep9_diks_ph3_rusty_event5 with dissolve
mc "That's a shit feeling."
mc "Was she hiding that from you?"
scene ep9_diks_ph3_rusty_event6 with dissolve
rs "Yes. No... She just got back together with him."
scene ep9_diks_ph3_rusty_event5 with dissolve
mc "She wasn't completely honest?"
scene ep9_diks_ph3_rusty_event7 with dissolve
rs "..."
scene ep9_diks_ph3_rusty_event8 with dissolve
mc "Do you like her a lot?"
scene ep9_diks_ph3_rusty_event9 with dissolve
rs "I guess I did like her more than I thought I did."
rs "I've had it rough with relationships in the past."
rs "I never looked for one, but I wasn't dismissing the idea of it altogether."
scene ep9_diks_ph3_rusty_event10 with dissolve
rs "But I've been pretty shallow. I fucked around a lot."
rs "Micha's one of the girls I felt that it could be more than that."
rs "Those feelings are rare. They stick with you."
scene ep9_diks_ph3_rusty_event11 with dissolve
mc "I can relate to that more than you know."
scene ep9_diks_ph3_rusty_event10 with dissolve
rs "Yeah? Ever dated someone who had a boyfriend?"
scene ep9_diks_ph3_rusty_event11 with dissolve
mc "Sort of. I mean... Yeah, I've dated a taken girl."
mc "It made me feel like what I'm assuming you feel right now."
scene ep9_diks_ph3_rusty_event8 with dissolve
mc "It got me sad, it got me angry, and it made me realize a lot about myself."
scene ep9_diks_ph3_rusty_event9 with dissolve
rs "How did you get over it?"
scene ep9_diks_ph3_rusty_event11 with dissolve
if branchMayaJosy:
    mc "I didn't get over it. But it's too complicated to explain."
elif ep5_feelingsForJosy:
    mc "I didn't. It still hurts thinking about it too much, but I've been trying to move on."
else:
    mc "By trying to talk to other girls and get back into the dating game."
scene ep9_diks_ph3_rusty_event9 with dissolve
rs "Guess I'm not making anyone do the walk of shame tomorrow."
scene ep9_diks_ph3_rusty_event12 with dissolve
mc "Haha! Dude, you're like the saddest joker ever."
scene ep9_diks_ph3_rusty_event13 with dissolve
rs "Haha!"
if (minigames and pp_current_party_happiness[6] > 2) or (not minigames and pp_current_party_happiness[6] == 1):
    rs "And you throw great parties."
    scene ep9_diks_ph3_rusty_event12 with dissolve
    mc "You think so?"
    scene ep9_diks_ph3_rusty_event13 with dissolve
    rs "Absolutely do."
elif (minigames and pp_current_party_happiness[6] > 1) or (not minigames and pp_current_party_happiness[6] == 0):
    rs "And you throw mediocre parties."
    scene ep9_diks_ph3_rusty_event12 with dissolve
    mc "Damn... That's below the belt."
    scene ep9_diks_ph3_rusty_event13 with dissolve
    rs "It's a decent party, [name]. I'd probably enjoy it more if it weren't for Micha."
else:
    rs "And you're like the worst party planner ever."
    scene ep9_diks_ph3_rusty_event12 with dissolve
    mc "Shit. You didn't like the party because of me?"
    scene ep9_diks_ph3_rusty_event13 with dissolve
    rs "Micha made it fun. I know you're trying. Keep at it, though."

if ep8_mansion_won:
    scene ep9_diks_ph3_rusty_event14 with dissolve
    rs "Wanna know something crazy?"
    scene ep9_diks_ph3_rusty_event15 with dissolve
    mc "Always."
    scene ep9_diks_ph3_rusty_event14 with dissolve
    rs "Before you and I checked if we could afford to replace the windows, I was going to sell my car."
    scene ep9_diks_ph3_rusty_event15 with dissolve
    mc "To cover the expenses?"
    scene ep9_diks_ph3_rusty_event14 with dissolve
    rs "Yeah. I even went online to get a rough estimate and everything."
    scene ep9_diks_ph3_rusty_event15 with dissolve
    mc "Good thing you didn't. It's a sweet ride."
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "I love that car."
    rs "But I love the DIKs more."
    scene ep9_diks_ph3_rusty_event17 with dissolve
    mc "Your heart is in the right place, Rusty."
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "So is yours."
    rs "I can't believe I feel more connected to a freshman than to people I've known here for years."
    scene ep9_diks_ph3_rusty_event17 with dissolve
    mc "That means a lot to me. I'm happy I can talk to you like this. I haven't got a lot of people for it."
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "If you ever wanna borrow the car, I'll keep the keys in the safe for you."
    scene ep9_diks_ph3_rusty_event17 with dissolve
    mc "You'd let me ride it?"
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "Without your help around here, none of us would ride it."
    rs "Use it whenever you want."
    scene ep9_diks_ph3_rusty_event18 with dissolve
    rs "If you scratch it, I'll kill you."
    mc "Hahaha!"
    scene ep9_diks_ph3_rusty_event14 with dissolve
else:
    scene ep9_diks_ph3_rusty_event20 with dissolve
    rs "About before... You asked me about how we could afford everything now."
    scene ep9_diks_ph3_rusty_event21 with dissolve
    mc "Yeah?"
    scene ep9_diks_ph3_rusty_event20 with dissolve
    rs "You know my car?"
    scene ep9_diks_ph3_rusty_event21 with dissolve
    mc "Yes. It's a sweet ride."
    scene ep9_diks_ph3_rusty_event20 with dissolve
    rs "I sold it."
    scene ep9_diks_ph3_rusty_event22 with dissolve
    mc "You what?"
    scene ep9_diks_ph3_rusty_event23 with dissolve
    rs "It was the only way I could cover the expenses without crawling back to Dad."
    rs "I had to take responsibility and this was within my power."
    rs "I loved that car."
    rs "But I love the DIKs more. Ultimately, it wasn't a hard decision."
    scene ep9_diks_ph3_rusty_event22 with dissolve
    mc "It's still sad... But wow..."
    mc "Your heart is in the right place, Rusty."
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "So is yours."
    rs "I can't believe I feel more connected to a freshman than to people I've known here for years."
    scene ep9_diks_ph3_rusty_event17 with dissolve
    mc "Thanks. That means a lot to me."
    scene ep9_diks_ph3_rusty_event16 with dissolve
    rs "Don't mention it."
rs "Wanna head back inside?"
scene ep9_diks_ph3_rusty_event15 with dissolve
mc "Yeah, this costume wasn't made for rooftop hangouts."
scene ep9_diks_ph3_rusty_event14 with dissolve
rs "No kidding. The strippers here have more clothes than you tonight."
scene ep9_diks_ph3_rusty_event15 with dissolve
mc "Haha! That one was funny. Maybe you are a joker after all."
stop music fadeout 3
scene ep9_diks_ph3_rusty_event19 with dissolve
rs "I'm definitely some kind of a joke tonight."
$ task_list[12] = ""
$ updateTaskList()
$ mphone_next_song()
if not ep8_mansion_won:
    $ new_bio("Rusty", "Rusty had to sell his car to pay for fixing the mansion.")
$ new_bio("Rusty", "I had a heart-to-heart with Rusty about Micha. Apparently, she's got a boyfriend and led Rusty on.")
$ new_bio("Micha", "Apparently, she's got a boyfriend and led Rusty on.")
jump endEvent

label ep9_diks_ph3_jacob_event_label:
scene ep9_diks_ph3_jacob_event1 with dissolve
mc "Heads up. Becky is taking off with your jacket."
scene ep9_diks_ph3_jacob_event2 with dissolve
jac "She's what?"
scene ep9_diks_ph3_jacob_event1 with dissolve
mc "She was naked in your room waiting for you..."
scene ep9_diks_ph3_jacob_event2 with dissolve
jac "Shit! I forgot about her."
scene ep9_diks_ph3_jacob_event1 with dissolve
if affinity == "DIK":
    mc "Are you gonna bang her, or what?"
else:
    mc "Don't tell me you and Becky are gonna..."
scene ep9_diks_ph3_jacob_event2 with dissolve
jac "Not again, no."
scene ep9_diks_ph3_jacob_event1 with dissolve
mc "Oh, you already did, huh?"
scene ep9_diks_ph3_jacob_event3 with dissolve
jac "She's a lousy fuck. She just lies there."
jac "And she's no Arieth, but she gets around. Especially if she thinks you're popular enough."
jac "I think it was Tommy who dicked her last."
if ep7_becky_lewd:
    scene ep9_diks_ph3_jacob_event1 with dissolve
    mc "I got a blowjob from her not that long ago."
    scene ep9_diks_ph3_jacob_event4 with dissolve
    jac "Nice."
scene ep9_diks_ph3_jacob_event5 with dissolve
jac "I'm gonna get my jacket back. Thanks, bro!"
$ task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_leon_event_label:
scene ep9_diks_ph3_costume_leon_event1 with dissolve
le "Dude, why are you checking me out?"
scene ep9_diks_ph3_costume_leon_event2 with dissolve
mc "No reason."
scene ep9_diks_ph3_costume_leon_event1 with dissolve
le "Well... Stop it."
label ep9_diks_ph3_costume_leon_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_leon_eventb_label")
scene ep9_diks_ph3_costume_leon_event2 with dissolve
menu:
    "Put Leon in your top three":
        if not "Leon" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Leon"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Leon"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Leon"
            else:
                menu:
                    "{i}Choose who to replace with Leon{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Leon"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Leon"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Leon"
                    "Don't put Leon in top three":
                        $ renpy.pause(0.5)
    "Haven't decided yet":
        $ renpy.pause(0.5)
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3b_jamie_event_label:
show screen dance_filter_screen
if ep9_winner == "Leon":
    scene ep9_dik3b_jamie_event1b with dissolve
else:
    scene ep9_dik3b_jamie_event1 with dissolve
$ renpy.pause()
scene ep9_dik3b_jamie_event5 with dissolve
jm "Hey..."
scene ep9_dik3b_jamie_event2 with dissolve
le "You..."
le "You're wearing it!"
scene ep9_dik3b_jamie_event6 with dissolve
jm "*{i}British accent{/i}* Sorry for being late to the party, Lily."
jm "*{i}British accent{/i}* And I'm sorry for being an ass to you before."
scene ep9_dik3b_jamie_event2 with dissolve
le "Haha! Why are you talking like that?"
scene ep9_dik3b_jamie_event8 with dissolve
jm "I suck at mimicking a girl's voice."
scene ep9_dik3b_jamie_event3 with dissolve
le "*{i}High voice{/i}* You have to go high like this, Envy!"
scene ep9_dik3b_jamie_event6 with dissolve
jm "*{i}High voice{/i}* Oh, is that how you do it, Lily?"
scene ep9_dik3b_jamie_event3 with dissolve
le "*{i}High voice{/i}* Haha! Yes! Let's go grind some cocks!"
scene ep9_dik3b_jamie_event7 with dissolve
jm "..."
scene ep9_dik3b_jamie_event4 with dissolve
le "I mean... Let's go grab some dicks. Drinks!"
scene ep9_dik3b_jamie_event8 with dissolve
jm "I won't say no to that."
scene ep9_dik3b_jamie_event9 with dissolve
jm "Question. Are your balls squeezed by the panties?"
le "Soooo squeezed."
jm "Right!? It's like they're being cradled by this lingerie."
$ task_list[13] = ""
$ updateTaskList()
hide screen dance_filter_screen
jump endEvent

label ep9_diks_ph3_prepsl_event_label:
scene ep9_diks_ph3_prepsl_event1 with dissolve
if "ep9_diks_ph3_prepsc_event_label" in event_list:
    mc "(That's a prep. They snuck in!)"
else:
    mc "(That's another prep.)"
scene ep9_diks_ph3_prepsl_event2 with dissolve
$ renpy.pause()

hide screen dance_filter_screen
play sound "sound_effects/door_slam.mp3"
scene ep9_diks_ph3_prepsl_event3 with vpunch
lu "Hey!!!"
scene ep9_diks_ph3_prepsl_event4 with dissolve
lu "Whatever! I don't wanna go to your pretentious party anyway!"
$ new_bio("Lucas", "I threw Lucas out of the Halloween party after he snuck in.")
if not "ep9_diks_ph3_prepsc_event_label" in event_list:
    $ task_list[11] = ""
    $ updateTaskList()
else:
   if persistent.mod_wtenabled:
      $ task_list[11] = "Kick out the preps(Left hallway)"
jump endEvent

label ep9_diks_ph3_prepsc_event_label:
if branchIsabella:
    scene ep9_diks_ph3_prepsc_event3 with dissolve
else:
    scene ep9_diks_ph3_prepsc_event3b with dissolve
if "ep9_diks_ph3_prepsl_event_label" in event_list:
    mc "(That's a prep. They snuck in!)"
else:
    mc "(That's another prep.)"
scene ep9_diks_ph3_prepsc_event4 with dissolve
mc "Party's over."
cr "Please?"
play sound "sound_effects/door_slam.mp3"
scene ep9_diks_ph3_prepsc_event1 with vpunch
cr "Watch it! My attire is expensive!"
scene ep9_diks_ph3_prepsc_event2 with dissolve
cr "This is bullshit. Elitist assholes!"
$ new_bio("Christian", "I threw Christian out of the Halloween party after he snuck in.")
if not "ep9_diks_ph3_prepsl_event_label" in event_list:
    $ task_list[11] = ""
    $ updateTaskList()
else:
   if persistent.mod_wtenabled:
      $ task_list[11] = "Kick out the preps(Tommy's room)"
jump endEvent

label ep9_diks_ph3_qt_event_label:
play sound "sound_effects/shower_curtain.mp3"
scene ep9_diks_ph3_qt_event1 with hpunch
chr "Hey!"
scene ep9_diks_ph3_qt_event2 with dissolve
qu "Get out, bitch."
scene ep9_diks_ph3_qt_event3 with dissolve
chr "Tommy?"
scene ep9_diks_ph3_qt_event4 with dissolve
tm "Leave."
scene ep9_diks_ph3_qt_event3 with dissolve
chr "I can't believe this."
scene ep9_diks_ph3_qt_event2 with dissolve
qu "You're fucking Tommy; what did you expect?"
scene ep9_diks_ph3_qt_event5 with dissolve
tm "What do you want?"
scene ep9_diks_ph3_qt_event9 with dissolve
qu "You invited Vinny!? Are you insane?"
scene ep9_diks_ph3_qt_event6 with dissolve
tm "No, I didn't. He's here?"
scene ep9_diks_ph3_qt_event9 with dissolve
qu "Yeah, he's upstairs snooping around and trying to stir shit up."
scene ep9_diks_ph3_qt_event6 with dissolve
tm "I'll handle it."
scene ep9_diks_ph3_qt_event10 with dissolve
qu "Really? You're calm about this? Last time I checked, you couldn't stand the guy."
qu "What the hell did you do?"
scene ep9_diks_ph3_qt_event7 with dissolve
qu "Of fucking course. You're buying from him."
scene ep9_diks_ph3_qt_event8 with dissolve
tm "What fucking choice did you leave me?"
scene ep9_diks_ph3_qt_event11 with dissolve
qu "Are you still salty about that? Fuck, Tommy! Grow up!"
scene ep9_diks_ph3_qt_event10 with dissolve
qu "Since Vinny left, it's been perfect for us."
scene ep9_diks_ph3_qt_event8 with dissolve
tm "You mean perfect for you."
scene ep9_diks_ph3_qt_event9 with dissolve
qu "The hell I don't! You've enjoyed it too."
scene ep9_diks_ph3_qt_event8 with dissolve
tm "I'll ask him to leave."
scene ep9_diks_ph3_qt_event10 with dissolve
qu "And you think that will work? You don't think he's got leverage now that you're buying from him?"
scene ep9_diks_ph3_qt_event8 with dissolve
tm "Just let me fucking handle it."
jump endEvent

label ep9_diks_ph3_prg_event_label:
scene ep9_diks_ph3_prg_event1 with dissolve
$ renpy.pause()
scene ep9_diks_ph3_prg_event5 with dissolve
js "Um. Those girls look a bit too old to be college students."
if branchIsabella:
    scene ep9_diks_ph3_prg_event12 with dissolve
else:
    scene ep9_diks_ph3_prg_event12b with dissolve
js "No offense to you, of course."
isa "None taken, and I agree. I've never seen them before. Odds are they aren't students."
scene ep9_diks_ph3_prg_event1 with dissolve
my "Guys seem to like them."
scene ep9_diks_ph3_prg_event5 with dissolve
js "I wonder why...?"
if branchIsabella:
    scene ep9_diks_ph3_prg_event13 with dissolve
else:
    scene ep9_diks_ph3_prg_event12b with dissolve
isa "Jealousy is unbecoming of you."
scene ep9_diks_ph3_prg_event6 with dissolve
js "I'm not jealous; I'm just noticing it."
if branchIsabella:
    scene ep9_diks_ph3_prg_event13 with dissolve
else:
    scene ep9_diks_ph3_prg_event12b with dissolve
isa "College boys are chock-full of hormones. This behavior isn't novel or surprising."
scene ep9_diks_ph3_prg_event7 with dissolve
my "Every guy isn't like that."
if branchIsabella:
    scene ep9_diks_ph3_prg_event13 with dissolve
else:
    scene ep9_diks_ph3_prg_event12b with dissolve
isa "True. Some know how and when to behave. But don't believe them if they say that they have zero interest in it."
isa "Desires are natural. For both men and women."
scene ep9_diks_ph3_prg_event8 with dissolve
my "*{i}Whispers{/i}* She's not wrong."
scene ep9_diks_ph3_prg_event10 with dissolve
js "*{i}Whispers{/i}* Oh, yeah? Do you like what you see over there?"
scene ep9_diks_ph3_prg_event9 with dissolve
my "*{i}Whispers{/i}* I mean... I wouldn't seriously date someone looking like that, but...kinda?"
if branchIsabella:
    scene ep9_diks_ph3_prg_event14 with dissolve
else:
    scene ep9_diks_ph3_prg_event14b with dissolve
sa "Drooling over the strippers, are we?"
scene ep9_diks_ph3_prg_event11 with dissolve
js "Strippers?"
if branchIsabella:
    scene ep9_diks_ph3_prg_event15 with dissolve
else:
    scene ep9_diks_ph3_prg_event15b with dissolve
sa "Those are Lily's colleagues, but also the girls the DIKs frequent."
scene ep9_diks_ph3_prg_event11 with dissolve
js "Oh?"
if branchIsabella:
    scene ep9_diks_ph3_prg_event15 with dissolve
else:
    scene ep9_diks_ph3_prg_event15b with dissolve
sa "Yup. What are you gonna do?"
scene ep9_diks_ph3_prg_event2 with dissolve
de "Tits! Tits! Tits!"
if branchIsabella:
    scene ep9_diks_ph3_prg_event17 with dissolve
else:
    scene ep9_diks_ph3_prg_event17b with dissolve
my "Derek! Stop being obnoxious."
if affinity != "CHICK":
    scene ep9_diks_ph3_prg_event3 with hpunch
    mc "Tits! Tits! Tits!"
    scene ep9_diks_ph3_prg_event4 with dissolve
    mc "..."
    if branchIsabella:
        scene ep9_diks_ph3_prg_event16 with dissolve
    else:
        scene ep9_diks_ph3_prg_event16b with dissolve
    isa "Boys will be boys."

$ event_list.append("ep9_diks_ph3_dz_event_label")
if persistent.mod_wtenabled:
    $ task_list[10] = "Talk to Zoey (Upper main room)"
else:
    $ task_list[10] = "Talk to Zoey"
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_costume_bella_event_label:
scene ep9_diks_ph3_costume_bella_event1 with dissolve
mc "I'm so tempted right now."
scene ep9_diks_ph3_costume_bella_event2 with dissolve
isa "Behave."
scene ep9_diks_ph3_costume_bella_event3 with dissolve
mc "Not that. Well...that too, but I was talking about the best costume competition."
scene ep9_diks_ph3_costume_bella_event4 with dissolve
isa "You're {b}not{/b} putting me on stage wearing this."
scene ep9_diks_ph3_costume_bella_event5 with dissolve
mc "I know that I probably shouldn't, but also...maybe I should?"
scene ep9_diks_ph3_costume_bella_event4 with dissolve
isa "And when they bring me on stage and ask me who I am in front of everyone. Tell me, what would your plan be by then?"
scene ep9_diks_ph3_costume_bella_event5 with dissolve
mc "Yeah. You're right. I can't do it."
scene ep9_diks_ph3_costume_bella_event6 with dissolve
isa "Good. Pick someone else. There are many good ones."
scene ep9_diks_ph3_costume_bella_event7 with dissolve
mc "Yeah? Who's your favorite so far?"
scene ep9_diks_ph3_costume_bella_event6 with dissolve
isa "Probably the rabbit and the magician."
scene ep9_diks_ph3_costume_bella_event7 with dissolve
mc "Jamie and Dany? Them?"
scene ep9_diks_ph3_costume_bella_event6 with dissolve
isa "I think it's cute and inventive. He pulled a rabbit out of a hat."
scene ep9_diks_ph3_costume_bella_event7 with dissolve
mc "What I wouldn't give to look at those two with your eyes."
scene ep9_diks_ph3_costume_bella_event6 with dissolve
isa "What do you mean?"
scene ep9_diks_ph3_costume_bella_event7 with dissolve
mc "Without going into details, there's plenty of drama surrounding them and their relationship."
scene ep9_diks_ph3_costume_bella_event8 with dissolve
isa "And you're jealous because you like to be the drama queen?"
scene ep9_diks_ph3_costume_bella_event7 with dissolve
mc "Where did that come from?"
scene ep9_diks_ph3_costume_bella_event8 with dissolve
isa "From nowhere. You're a walk in the park."
scene ep9_diks_ph3_costume_bella_event9 with dissolve
isa "*{i}Cough{/i}* Tybalt. *{i}Cough{/i}* Fights. *{i}Cough{/i}* Streaking."
scene ep9_diks_ph3_costume_bella_event10 with dissolve
mc "I better go look for some medicine. That cough sounds nasty."
jump endEvent

label ep9_diks_ph3_costume_jm_event_label:
scene ep9_diks_ph3_costume_jm_event1 with dissolve
my "What are you looking for?"
scene ep9_diks_ph3_costume_jm_event2 with dissolve
mc "The best costume of the party for the competition."
scene ep9_diks_ph3_costume_jm_event3 with dissolve
js "Are you looking at us for that?"
scene ep9_diks_ph3_costume_jm_event2 with dissolve
mc "I'm looking at everyone. I have to."
scene ep9_diks_ph3_costume_jm_event1 with dissolve
my "Would you tell us if you're gonna pick us?"
scene ep9_diks_ph3_costume_jm_event2 with dissolve
mc "Nope. I have to respect the integrity of the competition."
scene ep9_diks_ph3_costume_jm_event3 with dissolve
js "There are so many good costumes at this party."
label ep9_diks_ph3_costume_jm_eventb_label:
$ event_list.append("ep9_diks_ph3_costume_jm_eventb_label")
scene ep9_diks_ph3_costume_jm_event2 with dissolve
menu:
    "Put Josy in your top three":
        if not "Josy" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Josy"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Josy"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Josy"
            else:
                menu:
                    "{i}Choose who to replace with Josy{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Josy"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Josy"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Josy"
                    "Don't put Josy in top three":
                        $ renpy.pause(0.5)
    "Put Maya in your top three":
        if not "Maya" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Maya"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Maya"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Maya"
            else:
                menu:
                    "{i}Choose who to replace with Maya{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Maya"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Maya"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Maya"
                    "Don't put Maya in top three":
                        $ renpy.pause(0.5)
    "Put both in your top three":
        if not "Josy" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Josy"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Josy"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Josy"
            else:
                menu:
                    "{i}Choose who to replace with Josy{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Josy"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Josy"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Josy"
                    "Don't put Josy in top three":
                        $ renpy.pause(0.5)
        if not "Maya" in ep9_top_three:
            if ep9_top_three[0] == "":
                $ ep9_top_three[0] = "Maya"
            elif ep9_top_three[1] == "":
                $ ep9_top_three[1] = "Maya"
            elif ep9_top_three[2] == "":
                $ ep9_top_three[2] = "Maya"
            else:
                menu:
                    "{i}Choose who to replace with Maya{/i}"
                    "[ep9_top_three[0]]":
                        $ ep9_top_three[0] = "Maya"
                    "[ep9_top_three[1]]":
                        $ ep9_top_three[1] = "Maya"
                    "[ep9_top_three[2]]":
                        $ ep9_top_three[2] = "Maya"
                    "Don't put Maya in top three":
                        $ renpy.pause(0.5)
    "Haven't decided yet":
        mc "Yeah, there are so many good ones."
if not "" in ep9_top_three:
    $ task_list[1] = "Talk to Sage"
    $ updateTaskList()
jump endEvent

label ep9_diks_ph3_jt_event_label:
scene ep9_diks_ph3_jt_event1 with dissolve
dn "Decks of cards are misogynistic. They clearly show men are worth more than females and also how males outnumber females."
scene ep9_diks_ph3_jt_event2 with dissolve
tm "Ugh."
scene ep9_diks_ph3_jt_event3 with dissolve
jm "Tommy!"
jm "Pick a card. Any card."
play sound "sound_effects/slap.mp3"
scene ep9_diks_ph3_jt_event4 with hpunch
$ renpy.pause()
scene ep9_diks_ph3_jt_event5 with dissolve
dn "What the fuck!?"
dn "Are you ok?"
jm "Yeah, he's just not into magic, I guess."
jump endEvent

label ep9_diks_ph3_cumpetition_event_label:
if "ep9_diks_ph3_riona_event_label" not in event_list and "ep9_diks_ph3_dz_event_label" not in event_list and "ep9_diks_ph3_zoey2_event_label" not in event_list and "ep9_diks_ph3_prg_event_label" not in event_list and "ep9_diks_ph3_rusty_event_label" not in event_list and "ep9_diks_ph3_qv_event_label" not in event_list:
    $ task_list[1] = "Check the porch"
    $ event_list.append("ep9_diks_ph3_sage_event_label")
scene ep9_diks_ph3_cumpetition_event53 with dissolve
if ep9_cumpetition:
    ro "It's your party. Just tell us when and where."
    scene ep9_diks_ph3_cumpetition_event54 with dissolve
    tm "It's time for it right now. Let's head to my room."
    scene ep9_diks_ph3_cumpetition_event55 with dissolve
    br "So, who's competing aside from you?"
    scene ep9_diks_ph3_cumpetition_event56 with dissolve
    tm "Leon? Did you check with people?"
    scene ep9_diks_ph3_cumpetition_event57 with dissolve
    le "I checked with some, but they don't wanna join."
    le "Jamie's being a bitch, John Boy's not in the mood, Jacob's talking to some chick, and I don't know where the rest are."
    scene ep9_diks_ph3_cumpetition_event58 with dissolve
    tm "[name]! Did you make up your mind?"
    scene ep9_diks_ph3_cumpetition_event59 with dissolve
    if ep9_cumpetition_join:
        mc "Yeah, Nicole and Lily wanted me to come. So, they'll be dancing for me."
        scene ep9_diks_ph3_cumpetition_event60 with dissolve
        tm "Hah! Bullshit. Get a load of this guy."
        scene ep9_diks_ph3_cumpetition_event59 with dissolve
        mc "It's not bullshit; ask them yourself."
        scene ep9_diks_ph3_cumpetition_event61 with dissolve
        tm "If he's getting two, so are we. Dibs on Tania and Rose."
        le "No way! I want Tania!"
        scene ep9_diks_ph3_cumpetition_event62 with dissolve
        tm "I'll flip you for it. Bee or stag?"
        scene bg anim_coin_flip_ep9 movie with dissolve
        le "Bee."
        tm "Stag! Hah! Fuck you! Tania is mine."
    else:
        mc "I did. Have fun! I'm not joining."
        if minigames:
            scene ep9_diks_ph3_cumpetition_event63 with dissolve
            $ specialMessage = "DIKs' happiness increased!"
            $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
            $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
            $ pp_update_happiness_icons()
            $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
            $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
            show screen specialmsg
            pause
            hide screen specialmsg
        $ task_list[5] = ""
        $ updateTaskList()
        jump endEvent
else:
    ro "You want us to entertain you and Leon?"
    scene ep9_diks_ph3_cumpetition_event54 with dissolve
    tm "Yeah, nothing big. It's a small, friendly CUM-petition."
    scene ep9_diks_ph3_cumpetition_event55 with dissolve
    br "This again? Last year, you lost."
    scene ep9_diks_ph3_cumpetition_event54 with dissolve
    tm "On purpose. When there's no condom-swallowing involved, every contestant is a winner."
    tm "But... Hm...we should have some kind of punishment for the loser."
    scene ep9_diks_ph3_cumpetition_event53 with dissolve
    ro "Ok, sure. So, are we gonna gather people somewhere for it, or...?"
    scene ep9_diks_ph3_cumpetition_event54 with dissolve
    tm "No, it's just Leon and me. We'll pay you for it."
    tm "Let's go to my room."
    $ task_list[5] = ""
    $ updateTaskList()
    jump endEvent

label ep9_diks_ph3_cumpetition_event2_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    $ ep6_envy_lewd = True
    $ ep7_lily_lewd = True
    $ ep8_sandy_lewd = True
    $ mphone_music_genre = 2
    $ mphone_play_songs(["music/ep9/licensed_music/track115.mp3"])
hide screen new_phone_screen
scene ep9_diks_ph3_cumpetition_event1
show screen dance_filter_screen
with wipeleft
tm "All right, now it's a party! What are we playing for?"
scene ep9_diks_ph3_cumpetition_event2 with dissolve
le "Bragging rights? I don't have a lot of money right now."
scene ep9_diks_ph3_cumpetition_event3 with dissolve
tm "The first loser gets shamed too."
scene ep9_diks_ph3_cumpetition_event4 with dissolve
mc "Shamed how?"
scene ep9_diks_ph3_cumpetition_event2 with dissolve
le "A picture on the DIK wall?"
scene ep9_diks_ph3_cumpetition_event3 with dissolve
tm "Yes! A pic with cum in your underwear and the girls making the loser sign next to you!"
scene ep9_diks_ph3_cumpetition_event4 with dissolve
mc "Those are some high stakes."
scene ep9_diks_ph3_cumpetition_event5 with dissolve
tm "There's gotta be an incentive to not cum, or else it's not different from another night out."
stop music fadeout 3
scene ep9_diks_ph3_cumpetition_event1 with dissolve
tm "All right, girls... You know the rules. Last man cumming! Go!"

$ mphone_music_genre = 2
$ mphone_play_songs(["music/ep9/licensed_music/track122.mp3","music/ep9/the_friendly_monster_shop.mp3","music/ep9/halloween_again.mp3","music/ep9/licensed_music/track122.mp3"])

scene ep9_diks_ph3_cumpetition_event6 with dissolve
ly "Girl, get to it."
scene ep9_diks_ph3_cumpetition_event7 with dissolve
ly "Do you think he wants to win or lose?"
scene ep9_diks_ph3_cumpetition_event8 with dissolve
nic "I'm not sure, but I'm pretty sure he doesn't wanna be in that picture Tommy talked about."
scene ep9_diks_ph3_cumpetition_event9 with dissolve
mc "Yeah, I'd rather not."
scene ep9_diks_ph3_cumpetition_event10 with dissolve
ly "Haha, it would be kinda fun if he was. Don't you think?"
scene ep9_diks_ph3_cumpetition_event11 with dissolve
nic "Hahaha! He's definitely rock-hard, so who knows?"
scene ep9_diks_ph3_cumpetition_event12 with dissolve
mc "Come on, be nice to me."
scene ep9_diks_ph3_cumpetition_event13 with dissolve
nic "No can do. I'm working right now, and the customer didn't order a lousy dance - they wanted the premium shit."
scene anim_cumpetition_1_ep9 with dissolve
ly "You're not gonna cum over Nicole, are you?"
mc "I'm not planning on it. No."
nic "Look at his face. He's concentrating so hard, right now."
mc "There's a dot in the ceiling."
scene ep9_diks_ph3_cumpetition_event14 with dissolve
ly "Shut up and watch her grind your cock."
scene anim_cumpetition_1_ep9 with dissolve
pause
scene ep9_diks_ph3_cumpetition_event15 with dissolve
ly "*{i}Lick{/i}* I bet you've been hard since the moment she sat in your lap."
if ep7_lily_lewd:
    scene ep9_diks_ph3_cumpetition_event16 with dissolve
    ly "You know, [name]... If you and I were together, you'd call this moment Monday."
mc "Hngnn..."
scene ep9_diks_ph3_cumpetition_event17 with dissolve
tm "How's it going, brothers? Cumsies yet?"
scene ep9_diks_ph3_cumpetition_event18 with dissolve
le "I'm good! Fuck!"
br "He's not good, haha! He's struggling hard over here!"
scene ep9_diks_ph3_cumpetition_event26 with dissolve
nic "I got him warmed up for you."
ly "We need to move this into a higher gear if we're gonna have pretty boy's face on that wall."
scene anim_cumpetition_2_ep9 with dissolve
nic "[name], let me tell you about Lily. She's got some of the best moves you've seen."
nic "She even made me cum once from grinding her ass in my lap when we practiced dance moves together."
nic "I can't imagine the amount of blood in your dick right now."
nic "It's throbbing against her, isn't it?"
pause
scene ep9_diks_ph3_cumpetition_event27 with dissolve
ly "Damn right it is, girl. He picked a bad costume for a CUM-petition."
ly "The layers are so thin... I think..."
scene ep9_diks_ph3_cumpetition_event28 with dissolve
ly "Oh no... They are starting to slip off him."
scene ep9_diks_ph3_cumpetition_event29 with dissolve
nic "Oh no... He's naked now? That's unfortunate."
scene ep9_diks_ph3_cumpetition_event30 with dissolve
ly "Yeah, for those four drooling girls. Well, five if you count Leon."
scene ep9_diks_ph3_cumpetition_event25 with dissolve
tan "WOW! Is that thing real!?"
scene ep9_diks_ph3_cumpetition_event31 with dissolve
nic "Haha! Focus on your guy, Tania. Even though we have enough dick to last for everyone, we're not sharing."
scene ep9_diks_ph3_cumpetition_event19 with dissolve
br "Did you know he was that big all this time?"
if ep6_envy_lewd or ep8_sandy_lewd:
    scene ep9_diks_ph3_cumpetition_event20 with dissolve
    sn "Yeah, but if I told you what that dick of his can do to you, you'd be my competition for it."
    if ep6_envy_lewd:
        sn "He's my little lamb chop..."
else:
    scene ep9_diks_ph3_cumpetition_event21 with dissolve
    sn "Fuck! If I did, I would have jumped him the moment I met him."

scene ep9_diks_ph3_cumpetition_event32 with dissolve
ly "Oh, no. Nicole... [name] is gonna cum all over me. I can feel it."
scene anim_cumpetition_3_ep9 with dissolve
mc "Hngn... Hey! That's cheating."
nic "Nothing is cheating in the CUM-petition. It's all about the limits the girl in your lap sets."
nic "And these girls are feeling extra frisky tonight, haha! We've never been with a Spartan before."
nic "[name]... Please, don't cum over my friend. Her small mouth can't handle it."
ly "*{i}Suck suck{/i}*"
nic "I know her mouth feels good, [name]. But you shouldn't cum inside it..."
scene ep9_diks_ph3_cumpetition_event33 with dissolve
nic "[name]? Open your mouth for me. Did you ever taste my tits?"
mc "*{i}Muffled{/i}* HELP ME! SOMEONE!"
scene ep9_diks_ph3_cumpetition_event34 with dissolve
nic "Hahaha!"
nic "No one is coming to help you, baby."
scene anim_cumpetition_4_ep9 with dissolve
ly "Nicole's insatiable. She will keep going until you cum for her."
ly "Why don't you swirl your tongue around her nipples a bit? They feel so good that way. I promise."
nic "That's it. Suck on my nipple. Enjoy this, [name]."
pause
scene ep9_diks_ph3_cumpetition_event35 with dissolve
ly "Got any room for mine? I bet you can fit both in your mouth."
scene ep9_diks_ph3_cumpetition_event36 with dissolve
ly "There you go..."
scene ep9_diks_ph3_cumpetition_event22 at vpunch, cum1
le "NOOO!!!"
br "We have a loser over here, haha!"
scene ep9_diks_ph3_cumpetition_event23 with dissolve
tm "Hahaha! Yes!!!"
tm "Take the picture with him!"
scene ep9_diks_ph3_cumpetition_event24 with dissolve
tm "Fuck, that feels good. Now I can enjoy this thoroughly!"
scene ep9_diks_ph3_cumpetition_event37 with dissolve
nic "You're not dozing off, are you?"
scene ep9_diks_ph3_cumpetition_event39 with dissolve
mc "No. Like Tommy said, I can finally relax."
scene ep9_diks_ph3_cumpetition_event37 with dissolve
ly "How close are you, really?"
scene ep9_diks_ph3_cumpetition_event39 with dissolve
mc "I was very close; I can't lie. Now I got a second wind."
nic "You're gonna need it if you wanna beat Tommy."
scene ep9_diks_ph3_cumpetition_event40 with dissolve
ly "Obviously, we're going too easy on him. Do something, Nicole."
scene ep9_diks_ph3_cumpetition_event41 with dissolve
nic "Give me some room and I'll finish him."
scene anim_cumpetition_5_ep9 with dissolve
ly "Perfect. Keep it up."
tm "It feels weird rooting for a girl to make a dude cum, but go Envy! Haha!"
le "And I came in my underwear from rubbing with layers on..."
ly "Damn, [name]. Your dick rubbing against her like that... How lucky are you?"
pause
nic "Fuck..."
scene ep9_diks_ph3_cumpetition_event42 with dissolve
ly "Huh, what's that?"
scene anim_cumpetition_5_ep9 with dissolve
nic "Hngn... Nothing, I..."
scene ep9_diks_ph3_cumpetition_event43 with vpunch
nic "FUCK! Ahh!!"
scene ep9_diks_ph3_cumpetition_event44 with vpunch
nic "AHHH!!!"
ly "Hahaha! No way! Nicole lost! That has got to be a first for the CUM-petition!"
nic "Shit..."
scene ep9_diks_ph3_cumpetition_event49 at vpunch, cum1
tm "Ahh!!!"
tan "We got another loser over here!"
scene ep9_diks_ph3_cumpetition_event45 with dissolve
mc "I won?"
scene ep9_diks_ph3_cumpetition_event46 with dissolve
ly "I think you won in two ways tonight."
scene ep9_diks_ph3_cumpetition_event50 with dissolve
tm "Fuck! I couldn't hold it longer."
scene ep9_diks_ph3_cumpetition_event51 with dissolve
tm "But at least I'm not gonna be immortalized on the wall as a femboy like Leon! HAHAHA!"
scene ep9_diks_ph3_cumpetition_event52 with dissolve
le "Fuck you, dude... It's Halloween."
scene ep9_diks_ph3_cumpetition_event47 with dissolve
mc "I guess the dance is over then."
scene ep9_diks_ph3_cumpetition_event48 with dissolve
nic "Well... At least you won."
scene ep9_diks_ph3_cumpetition_event47 with dissolve
mc "True."
mc "You two did amazing, though."
$ renpy.end_replay()
$ persistent.ep9_lewd_cumpetition = True
$ calcScenes()
$ new_bio("You", "I won the CUM-petition, but Lily and Nicole made it very hard for me.")
$ new_bio("Lily", "I won the CUM-petition, but Lily and Nicole made it very hard for me.")
$ new_bio("Envy", "I won the CUM-petition, but Lily and Nicole made it very hard for me.")
$ new_bio("Leon", "Leon lost the CUM-petition. Poor guy... I wouldn't want to be him. That punishment didn't sound too good to me.")
$ mphone_stats_add_girl_s3("envy","Lily and Nicole entertained you during the CUM-petition at the Halloween party in episode 9.")
$ mphone_stats_add_girl_s3("lily","Lily and Nicole entertained you during the CUM-petition at the Halloween party in episode 9.")
if minigames:
    scene ep9_diks_ph3_cumpetition_event63 with dissolve
    $ specialMessage = "DIKs' happiness increased!"
    $ pp_happiness_level[4] = min(pp_happiness_level[4]+2,100)
    $ pp_happiness_level[7] = min(pp_happiness_level[7]+2,100)
    $ pp_update_happiness_icons()
    $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Leon's happiness by {color=00ff00}+2%{/color}.")
    $ mphone_pp_history_list.append("• The {color=ffed00}CUM-petition{/color} activity increased Tommy's happiness by {color=00ff00}+2%{/color}.")
    show screen specialmsg
    pause
    hide screen specialmsg
$ task_list[5] = ""
$ updateTaskList()
hide screen dance_filter_screen with dissolve
show screen new_phone_screen
jump endEvent

label ep9_diks_ph3_jamie_event_label:
scene ep9_dik3_jamie_event1b with dissolve
sn "WOOO!!"
ro "Work it, girl! Yeah!!!"
scene ep9_dik3_jamie_event1 with dissolve
ti "HAHA!"
scene ep9_dik3_jamie_event2 with dissolve
dn "This party is now below my standards for humanity. We're leaving."
jm "People are just having fun."
dn "It's not for Franz and me. Are you coming?"
if (ep8_leons_side and not ep9_leons_side) or (not ep8_leons_side and ep9_leons_side):
    scene ep9_dik3_jamie_event5 with dissolve
    jm "No, I think I'll stay. The guys might need my help later."
    scene ep9_dik3_jamie_event4 with dissolve
    dn "Call me."
    scene ep9_dik3_jamie_event6 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event7 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event8 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event9 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event10 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event12 with dissolve
    $ renpy.pause()
    scene ep9_dik3_jamie_event11 with dissolve
    $ renpy.pause()
    jump ep9_diks_ph3b_jamie_event_label
else:
    scene ep9_dik3_jamie_event3 with dissolve
    jm "Can we have sex?"
    scene ep9_dik3_jamie_event4 with dissolve
    dn "I think Linda's at home."
    scene ep9_dik3_jamie_event3 with dissolve
    jm "Can we make her leave...or watch?"
    scene ep9_dik3_jamie_event4b with dissolve
    dn "Watch...? You'd be into that?"
    scene ep9_dik3_jamie_event5 with dissolve
    jm "Uh..."
    scene ep9_dik3_jamie_event4b with dissolve
    dn "I'll see what I can do."
$ task_list[13] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_zoey_event_label:
$ guideSuggestedPage = 79
scene ep9_diks_ph3_zoey_event1 with dissolve
zo "I had a great fucking time, but I need to take off."
scene ep9_diks_ph3_zoey_event2 with dissolve
mc "Already?"
scene ep9_diks_ph3_zoey_event3 with dissolve
zo "This late is \"already\" to you now, huh?"
scene ep9_diks_ph3_zoey_event2 with dissolve
mc "Well..."
scene ep9_diks_ph3_zoey_event3 with dissolve
zo "I would stay if I could, but I'm gonna miss the last train ride home."
scene ep9_diks_ph3_zoey_event2 with dissolve
if branchAlone and not ep9_mad_at_zoey:
    if persistent.mod_wtenabled: 
                            $mod_choices = ["(Jade scene)","(-Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                            #[mod_gr][mod_choices[0]]
    menu:
        "[mod_gr]Crash in your room":
            $ ep9_zoey_crash = True
            if ep9_zoey_photo:
                mc "Are you sure? You can crash in my room. You saw how big it is."
            else:
                mc "Are you sure? You can crash in my room. You saw how big it is, right?"
            scene ep9_diks_ph3_zoey_event4 with dissolve
            zo "I didn't bring any other clothes, and I'm naked under this, so..."
            zo "Plus, I'd rather ride the train back home looking like this tonight than tomorrow."
            scene ep9_diks_ph3_zoey_event2 with dissolve
            mc "Yeah, I get it. Less questions."
            scene ep9_diks_ph3_zoey_event4 with dissolve
            zo "Not that I mind being the freak, but yeah."
            scene ep9_diks_ph3_zoey_event3 with dissolve
            zo "Thanks for the offer, though. Maybe next time?"
            $ new_bio("Zoey", "I offered Zoey to crash on my couch.")
            jump ep9_diks_ph3b_zoey_event2_label
        "Say goodbye":
            jump ep9_diks_ph3b_zoey_event_label
else:
    label ep9_diks_ph3b_zoey_event_label:
    mc "Yeah, I get it. So, um..."
    label ep9_diks_ph3b_zoey_event2_label:
    scene ep9_diks_ph3_zoey_event5 with dissolve
    zo "Thanks for inviting me. Really. This party was the bomb."
    scene ep9_diks_ph3_zoey_event6 with dissolve
    mc "You think so?"
    scene ep9_diks_ph3_zoey_event7 with dissolve
    zo "Party planner, huh?"
    scene ep9_diks_ph3_zoey_event6 with dissolve
    mc "Yeah. Seems so."
    scene ep9_diks_ph3_zoey_event8 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_zoey_event7 with dissolve
    zo "I can't believe you're in college..."
    zo "It fits you."
    scene ep9_diks_ph3_zoey_event9 with dissolve
    zo "I'll call you."
    scene ep9_diks_ph3_zoey_event10 with dissolve
    $ renpy.pause()
    scene ep9_diks_ph3_zoey_event11 with dissolve
    $ renpy.pause()
$ task_list[3] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_ln_leaving_event_label:
scene ep9_diks_ph3_ln_leaving_event1 with dissolve
ly "[name]? Nicole and I are gonna head out for a smoke and back to her place."
scene ep9_diks_ph3_ln_leaving_event2 with dissolve
mc "I can't blame you; it's getting pretty late."
mc "Why back to her place?"
scene ep9_diks_ph3_ln_leaving_event1 with dissolve
ly "Elena's been talking about fucking John Boy tonight and I'm not in the mood to catch their live show, so I'm coming with her."
scene ep9_diks_ph3_ln_leaving_event2 with dissolve
mc "Ok. Well, thanks for tonight; it was-"
scene ep9_diks_ph3_ln_leaving_event3 with dissolve
nic "Wanna come with?"
scene ep9_diks_ph3_ln_leaving_event2 with dissolve
mc "Back to your place?"
scene ep9_diks_ph3_ln_leaving_event3 with dissolve
if ep9_cumpetition_join:
    nic "Yeah. We feel bad for not letting you finish earlier, so..."
else:
    if envyLikesYou:
        nic "Yeah. I figured we could return some hospitality for your efforts with the party."
    else:
        nic "Lily's been raving about your libido. She said you'd be up for some fun."
scene ep9_diks_ph3_ln_leaving_event1 with dissolve
ly "Catch her drift?"
scene ep9_diks_ph3_ln_leaving_event2 with dissolve
label ep9_diks_ph3_ln_leaving_event2b_label:
if persistent.mod_wtenabled: 
                        $mod_choices = ["\n{size=-5}(Sex scene){color=#E6F653}(Progress Nicole path)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone:
                             $mod_choices[10]="(Heather path open/+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
menu:
    "End the night with Lily & Nicole [mod_gr][mod_choices[0]]":
        $ ep9_lily_nicole_lewd = True
        $ ep9_ended_night_with = "Lily & Nicole"
        mc "I'm game. Let me just grab some clothes, so I don't freeze."
        scene ep9_diks_ph3_ln_leaving_event3 with dissolve
        nic "We'll wait for you outside."
        stop music fadeout 3
        scene ep9_diks_ph3_ln_leaving_event2 with dissolve
        $ renpy.pause(0.5)
        $ wt_ep9_end_pick="Lily"
        $ phone_clear_jump_label = "ep9_lily_nicole_lewd_label"
        jump end_freeroam
    "Not yet":
        mc "Can you wait for a little while longer? I need to check some things first."
        $ event_list.append("ep9_diks_ph3_ln_leaving_event2_label")
        jump endEvent
    "End the night in a different way":
        mc "It sounds good, but I can't leave."
        scene ep9_diks_ph3_ln_leaving_event4 with dissolve
        ly "Damn..."
        nic "Worth a shot. Thanks for the party."
        scene ep9_diks_ph3_ln_leaving_event5 with dissolve
        if ep7_lily_lewd:
            ly "Damn, you are hard to catch."
        else:
            ly "Tsk tsk. Passing on a once-in-a-lifetime offer."
        $ optional_task_list[4] = ""
        $ updateTaskList()
jump endEvent

label ep9_diks_ph3_ln_leaving_event2_label:
scene ep9_diks_ph3_ln_leaving_event2 with dissolve
mc "Sorry about that..."
jump ep9_diks_ph3_ln_leaving_event2b_label

label ep9_diks_ph3_quinn_event_label:
$ ep9_quinn_ask = True
play sound "sound_effects/shove.mp3"
scene ep9_diks_ph3_quinn_event1 with vpunch
mc "*{i}Sigh{/i}* Ahhh..."
scene ep9_diks_ph3_quinn_event2 with dissolve
qu "What's wrong?"
scene ep9_diks_ph3_quinn_event3 with dissolve
mc "Nothing is wrong, but I realized I'm done for the night. No more obligations."
scene ep9_diks_ph3_quinn_event2 with dissolve
qu "Why are you looking at it as a job?"
scene ep9_diks_ph3_quinn_event3 with dissolve
mc "I guess I cared a lot about the party."
mc "I didn't even drink that much tonight."
scene ep9_diks_ph3_quinn_event4 with dissolve
qu "Drink."
scene ep9_diks_ph3_quinn_event5 with dissolve
mc "Thanks. How was your night? We didn't get a lot of chances to talk."
scene ep9_diks_ph3_quinn_event6 with dissolve
qu "Meh."
scene ep9_diks_ph3_quinn_event5 with dissolve
mc "Wanna talk about it?"
scene ep9_diks_ph3_quinn_event6 with dissolve
qu "Not really."
scene ep9_diks_ph3_quinn_event7 with dissolve
qu "What about you? How did the challenge go?"
scene ep9_diks_ph3_quinn_event5 with dissolve
if ep9_camila_lewd or ep9_heather_lewd == 2 or ep9_cumpetition_join:
    mc "Not that well. You were right, I couldn't keep my dick in my pants."
    scene ep9_diks_ph3_quinn_event8 with dissolve
    qu "Called it."
    scene ep9_diks_ph3_quinn_event9 with dissolve
    mc "Guess I won't be coming back to your place."
    scene ep9_diks_ph3_quinn_event6 with dissolve
    qu "I've got no use for you if your balls are drained."
    scene ep9_diks_ph3_quinn_event5 with dissolve
    mc "They aren't drained."
    qu "..."
    menu:
        "[mod_gr]Convince her":
            $ event_list.append("ep9_diks_ph3_quinn3_event_label")
            mc "Are you gonna make me beg for it?"
            mc "Those other girls were the warmup."
            scene ep9_diks_ph3_quinn_event10 with dissolve
            qu "Girls? Plural?"
            scene ep9_diks_ph3_quinn_event5 with dissolve
            mc "I don't keep track. Maybe it was just one?"
            mc "Come on, it's Halloween. You'll never get to fuck a Spartan if you don't do it now."
            scene ep9_diks_ph3_quinn_event11 with dissolve
            $ renpy.pause()
        "I'll find someone else":
            mc "All right, I'll find someone then."
            scene ep9_diks_ph3_quinn_event8 with dissolve
            qu "Good luck with that..."
else:
    mc "Oh, that. Yeah, I kept my dick in my pants."
    scene ep9_diks_ph3_quinn_event12 with dissolve
    qu "No fucking way."
    scene ep9_diks_ph3_quinn_event13 with dissolve
    mc "I did."
    scene ep9_diks_ph3_quinn_event7 with dissolve
    qu "You're probably the only dude to not get laid in that outfit at a Halloween party."
    scene ep9_diks_ph3_quinn_event5 with dissolve
    menu:
        "[mod_gr]Saved myself for you":
            $ event_list.append("ep9_diks_ph3_quinn3_event_label")
            mc "You're joking, right? I could have gotten laid if I wanted to, but I wanted to come back to your place tonight."
            scene ep9_diks_ph3_quinn_event14 with dissolve
            qu "I don't do sleepovers."
            scene ep9_diks_ph3_quinn_event15 with dissolve
            mc "Broccoli, huh?"
            scene ep9_diks_ph3_quinn_event14 with dissolve
            qu "Totally."
            scene ep9_diks_ph3_quinn_event16 with dissolve
            $ renpy.pause()
            scene ep9_diks_ph3_quinn_event17 with dissolve
            qu "I can...try it once. Sometime..."
            scene ep9_diks_ph3_quinn_event18 with dissolve
            $ renpy.pause()
            scene ep9_diks_ph3_quinn_event19 with dissolve
            qu "Hey, quit it. No fucking PDA. There are too many people watching."
            scene ep9_diks_ph3_quinn_event20 with dissolve
            mc "..."
            scene ep9_diks_ph3_quinn_event5 with dissolve
            mc "You're that shy, huh?"
            scene ep9_diks_ph3_quinn_event8 with dissolve
            qu "I'll suck your cock here if I want to, but I'm not doing this."
            scene ep9_diks_ph3_quinn_event9 with dissolve
            mc "Haha."
        "I'll find someone":
            mc "The night's not over. I'll find someone."
            scene ep9_diks_ph3_quinn_event8 with dissolve
            qu "Good luck with that..."

scene ep9_diks_ph3_quinn_event21 with dissolve
if ep9_vinny_choice == "DIK":
    mc "I got into a fight tonight."
else:
    mc "I almost got into a fight tonight."
scene ep9_diks_ph3_quinn_event22 with dissolve
mc "With this former DIK... Vinny."
scene ep9_diks_ph3_quinn_event23 with dissolve
qu "How come?"
scene ep9_diks_ph3_quinn_event22 with dissolve
mc "I found him in my room, trashing it and I confronted him about it."
mc "Then he flashed a prop gun."
scene ep9_diks_ph3_quinn_event24 with dissolve
qu "..."
scene ep9_diks_ph3_quinn_event22 with dissolve
mc "Tommy intervened and made him leave."
mc "Even though the gun wasn't real, it felt intimidating as hell."
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "You should stay away from that guy."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Yeah?"
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "Trust me, you don't want anything to do with him."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "All right, but if he gets into my face again..."
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "How good are you at fighting, really?"
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Pretty good, I think. But I only use it to protect myself."
if ep2FoughtJocks or ep5_agitatedCaleb or ep6_foughtTommy or ep9_josy_choice == "DIK":
    mc "Well... Most of the time."
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "Are you free sometime next week?"
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Possibly. I haven't got a lot planned."
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "Can I borrow you one night? I've got something to do downtown and could use some company."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Sure. What are we doing?"
scene ep9_diks_ph3_quinn_event25 with dissolve
qu "Nothing much. Just, you know, hanging out."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "A date, huh?"
scene ep9_diks_ph3_quinn_event27 with dissolve
qu "Forget I asked."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Come on."
scene ep9_diks_ph3_quinn_event27 with dissolve
qu "Broccoli."
scene ep9_diks_ph3_quinn_event26 with dissolve
mc "Haha! Is that our safe word or something?"

if "ep9_diks_ph3_quinn3_event_label" in event_list:
    scene ep9_diks_ph3_quinn_event28 with dissolve
    qu "It should be. Wanna head back to my lair?"
    label ep9_diks_ph3_quinn2b_event_label:
    scene ep9_diks_ph3_quinn_event26 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Quinn scene/path)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone:
                             $mod_choices[10]="(Heather path open/+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "End free roam [mod_gr][mod_choices[0]]":
            $ ep9_quinn_lewd = True
            $ wt_ep9_end_pick="Quinn"
            stop music fadeout 3
            mc "Let's go."
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
            $ phone_clear_jump_label = "ep9_quinn_lewd_label"
            jump end_freeroam
        "Not yet":
            mc "Maybe, but not yet. I need to check something really quickly."
            scene ep9_diks_ph3_quinn_event25 with dissolve
            qu "Come find me when you're ready."
            qu "But don't drag your ass for too long, or I'll leave."
            $ event_list.append("ep9_diks_ph3_quinn2_event_label")
            jump endEvent
else:
    mc "Anyway... I'm gonna go check on some things."
    scene ep9_diks_ph3_quinn_event25 with dissolve
    qu "Sure."
$ optional_task_list[5] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_quinn2_event_label:
scene ep9_diks_ph3_quinn_event28 with dissolve
qu "Wanna head back to my place?"
jump ep9_diks_ph3_quinn2b_event_label

label ep9_diks_ph3_cari_event_label:
scene ep9_diks_ph3_cari_event1 with dissolve
cam "Haha! You look like a cat!"
scene ep9_diks_ph3_cari_event2 with dissolve
ri "Did it take you this long to notice?"
scene ep9_diks_ph3_cari_event3 with dissolve
cam "Meow!"
scene ep9_diks_ph3_cari_event4 with dissolve
mc "Need a hand?"
scene ep9_diks_ph3_cari_event5 with dissolve
ri "Thanks, but I got her."
ri "I think it's time for us to leave."
scene ep9_diks_ph3_cari_event7 with dissolve
cam "No! One more drink, Rio... Please?"
scene ep9_diks_ph3_cari_event8 with dissolve
ri "Yes, let's have one more drink back at our place, ok?"
ri "I'll fix you up with a cold glass of water. That's the perfect drink to end the night with."
scene ep9_diks_ph3_cari_event6 with dissolve
menu:
    "Say goodbye":
        mc "It was great seeing you two tonight. Sleep well!"
        scene ep9_diks_ph3_cari_event5 with dissolve
        ri "You too, [name]."
    "Flatter Riona":
        if affinity == "DIK":
            mc "Both hot and sweet. You're the complete package, aren't you?"
            scene ep9_diks_ph3_cari_event9 with dissolve
            ri "Haha! I do what I can, I guess."
        else:
            mc "You're very sweet for helping your friend like this."
            scene ep9_diks_ph3_cari_event9 with dissolve
            ri "Well, she's a sweet friend... Those are hard to come by these days."
        if ep9_riona_choice == "DIK" and branchAlone:
            ri "Talk soon, [name]. We should continue our conversation, don't you think?"
        else:
            ri "Talk soon, [name]. Ok?"
        scene ep9_diks_ph3_cari_event6 with dissolve
        if ep9_riona_choice == "DIK" and branchAlone:
            mc "I absolutely do."
        mc "Good night, girls."
scene ep9_diks_ph3_cari_event8 with dissolve
ri "Now, let's get you home and out of those clothes."
$ optional_task_list[6] = ""
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_sandy_event_label:
$ guideSuggestedPage = 79
play sound "sound_effects/shove.mp3"
scene ep9_diks_ph3_sandy_event1 with hpunch
if ep6_envy_lewd:
    sn "Lamb chop!"
else:
    sn "There you are!"
scene ep9_diks_ph3_sandy_event2 with dissolve
sn "I've been looking all over for you."
scene ep9_diks_ph3_sandy_event3 with dissolve
mc "For me?"
scene ep9_diks_ph3_sandy_event2 with dissolve
sn "Mhm. I've waited all night to pounce on you."
scene ep9_diks_ph3_sandy_event3 with dissolve
if branchAlone and wt_ep9_branch_numbers < 2:
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(Sandy path open)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone:
                             $mod_choices[10]="(Sandy path open/{color=#E6F653}+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "Accept [mod_gr][mod_choices[0]]":
            $ ep9_sandy_accept = True
            mc "I'm here for it, baby."
            scene ep9_diks_ph3_sandy_event6 with dissolve
            sn "Grr!"
            mc "Ahh!! Don't bite!"
            sn "I'll do more than bite."
            mc "There's only one problem."
            scene ep9_diks_ph3_sandy_event4 with dissolve
            sn "Oh no... Dick problems? Sometimes guys go soft if they drink too much."
            scene ep9_diks_ph3_sandy_event5 with dissolve
            mc "No, it's not a dick problem. It's more of a privacy problem."
            mc "I mean, we can't fuck here, right?"
            scene ep9_diks_ph3_sandy_event7 with dissolve
            sn "Meh! Who needs a bed? Fuck me against the railing."
            mc "Um... No, I don't think so. It's too...public."
            scene ep9_diks_ph3_sandy_event8 with dissolve
            sn "Ugh, I knew it. I lost my mojo from all of this talking."
            sn "I need a hit."
            scene ep9_diks_ph3_sandy_event9 with dissolve
            mc "Huh? Sandy?"
            scene ep9_diks_ph3_sandy_event10 with dissolve
            ka "..."
            mc "I wasn't gonna do it, Karen."
            scene ep9_diks_ph3_sandy_event11 with dissolve
            mc "Dammit..."
            $ new_bio("Sandy", "Sandy wanted me to fuck her against the railing in the hallway.")
        "Decline":
            $ ep9_sandy_accept = False
            mc "Really? Wow, that's nice, but I-"
            scene ep9_diks_ph3_sandy_event6 with dissolve
            sn "Grr!"
            mc "Ahh!! Don't bite!"
            sn "I'll do more than bite."
            mc "Sandy, I can't do this tonight. Sorry..."
            scene ep9_diks_ph3_sandy_event4 with dissolve
            sn "Dick problems? Sometimes guys go soft if they drink too much."
            scene ep9_diks_ph3_sandy_event5 with dissolve
            mc "Ah... Not the case with me, but I'll keep that in mind."
            scene ep9_diks_ph3_sandy_event4 with dissolve
            sn "Damn... Who am I gonna do tonight?"
            scene ep9_diks_ph3_sandy_event5 with dissolve
            mc "I'm sure you'll find someone. Now, if you'll excuse me..."
            $ new_bio("Sandy", "Sandy wanted to fuck me, but I declined.")
else:
    mc "Wow, um... While I think that sounds great, I've gotta tell you..."
    mc "I'm sort of in a relationship right now."
    scene ep9_diks_ph3_sandy_event2 with dissolve
    sn "Cool! Bring her with you."
    scene ep9_diks_ph3_sandy_event3 with dissolve
    mc "I don't think that is the best idea."
    scene ep9_diks_ph3_sandy_event4 with dissolve
    if ep6_envy_lewd:
        sn "What are you trying to say, lamb chop?"
    else:
        sn "What are you trying to say?"
    scene ep9_diks_ph3_sandy_event5 with dissolve
    if ep6_envy_lewd:
        mc "I can't be your lamb chop anymore, Sandy. I'm sorry..."
    else:
        mc "I'm not available anymore, Sandy. I'm sorry..."
    scene ep9_diks_ph3_sandy_event4 with dissolve
    sn "Not at all? Like, not even at the club?"
    scene ep9_diks_ph3_sandy_event5 with dissolve
    if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone or wt_ep9_branch_numbers > 1:
                             $mod_choices[10]="(Sandy path open/{color=#E6F653}+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
    menu:
        "Not even at the club":
            $ ep9_sandy_club = False
            mc "Exactly. Not even at the club."
            scene ep9_diks_ph3_sandy_event4 with dissolve
            sn "Oh!? Damn!"
            sn "Who am I gonna do tonight?"
            $ new_bio("Sandy", "Sandy wanted to fuck me, but I told her I couldn't do stuff like that with her anymore.")
        "Maybe at the club [mod_gr][mod_choices[10]]":
            $ ep9_sandy_club = True
            $ tc += 1
            mc "I mean...maybe a bit at the club. Like dances and such. Maybe?"
            scene ep9_diks_ph3_sandy_event2 with dissolve
            sn "Got it! At the club it is."
            scene ep9_diks_ph3_sandy_event4 with dissolve
            sn "But damn... Who am I gonna do tonight?"
            $ new_bio("Sandy", "Sandy wanted to fuck me, but I told her I could only have fun with her at The Pink Rose.")
    scene ep9_diks_ph3_sandy_event5 with dissolve
    mc "I'm sure you'll find someone. Now, if you'll excuse me..."
$ optional_task_list[7] = ""
$ updateTaskList()
jump endEvent

label ep9_vinny_label:
stop music fadeout 3
$ guideSuggestedPage = 81
scene ep9_vinny1 with dissolve
mc "Hey! What are you doing in here?"
play music "music/ep_interlude/licensed_music/track96.mp3"
scene ep9_vinny2 with dissolve
vi "Don't worry about it."
scene ep9_vinny3 with dissolve
mc "It's my room, dude. What the fuck have you done to it?"
scene ep9_vinny4 with dissolve
$ renpy.pause()
scene ep9_vinny5 with dissolve
vi "This place went downhill after I left. I don't even recognize the room anymore."
scene ep9_vinny6 with dissolve
mc "Huh? Who the hell are you?"
scene ep9_vinny5 with dissolve
vi "I'd watch that tone if I were you. You're looking at the founder. I'm the OG DIK."
scene ep9_vinny6 with dissolve
mc "Vinny...?"
scene ep9_vinny7 with dissolve
vi "Ah, so you do know your history."
scene ep9_vinny6 with dissolve
if persistent.mod_wtenabled: 
                        $mod_choices = ["(+DIKs)","(- 2 Maya/Josy)","(-DIK)","(+DIK)","(Sandy scene)","(Sarah scene)","","","","","","" ]
                        #[mod_gr][mod_choices[0]] #{color=#E6F653}
                        
                        if not branchAlone:
                             $mod_choices[10]="(+Cheater)"
                             $mod_choices[11]="(+2 Cheater)"
menu:
    "Rude [mod_gr][mod_choices[3]]":
        $ dk(1)
        scene ep9_vinny8 with dissolve
        mc "You're the dude who couldn't handle the pressure and bailed. That legacy sticks with you."
        scene ep9_vinny7 with dissolve
        vi "You got that maggot attitude, kid. I'll give you that."
    "Non-confrontational [mod_gr][mod_choices[2]]":
        $ dk(-1)
        mc "The name's come up."
scene ep9_vinny9 with dissolve
vi "This used to be my room, you know."
vi "A lot of memories were made in here."
scene ep9_vinny8 with dissolve
if affinity == "DIK":
    mc "Yeah, but it's my place now. So, stop trashing it, and fuck off."
else:
    mc "Yeah, but it's my place now. So, stop trashing it, and show some respect."
scene ep9_vinny10 with dissolve
$ renpy.pause()
play sound "sound_effects/shove.mp3"
scene ep9_vinny11 with hpunch
$ renpy.pause()
scene ep9_vinny12 with dissolve
vi "Or you'll what?"

scene ep9_vinny13 with dissolve
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
$ mc_info = ["Punch him","ep9_vinny_fight_label","Tell him off","ep9_vinny_confront_label","Defuse the situation","ep9_vinny_ask_label",(ep5_agitatedCaleb and ep6_foughtTommy)]
show screen major_choice_screen
$ renpy.pause()

label ep9_vinny_fight_label:
if minigames:
    hide screen new_phone_screen
$ renpy.block_rollback()
$ ep9_vinny_choice = "DIK"
$ renpy.music.stop(channel="sfx1", fadeout=1)
play sound "sound_effects/hit.mp3"
scene ep9_vinny37 with hpunch
$ renpy.pause()
scene ep9_vinny38 with dissolve
vi "You motherfucker."
scene ep9_vinny39 with dissolve
mc "Don't act like you didn't start it!"
mc "Come on, fight me! I'll fucking floor you!"
if minigames:
    $ cpu_name = "Vinny"
    $ cpu_color = "#FF9C43"
    $ renpy.block_rollback()
    jump sports101_start_pov_fight_faux
label pov_mc_missed_label_faux:
scene ep9_vinny17 with dissolve
vi "You need to learn your place."
scene ep9_vinny17b with dissolve
stop music fadeout 3
if minigames:
    hide screen pov_health_screen
    show screen new_phone_screen
vi "Back up, bitch."
play sound "sound_effects/hit.mp3"
scene ep9_vinny17c with hpunch
$ renpy.pause()
scene ep9_vinny17d with dissolve
$ renpy.pause()
$ new_bio("You", "I punched Vinny when he shoved me in my room.")
$ new_bio("Vinny", "I punched Vinny when he shoved me in my room.")
jump ep9_vinny_gun_leave2_label

label ep9_vinny_confront_label:
$ renpy.block_rollback()
$ ep9_vinny_choice = "NEUTRAL"
$ renpy.music.stop(channel="sfx1", fadeout=1)
scene ep9_vinny14 with dissolve
mc "Dude... What the fuck are you doing!?"
mc "You know you're asking for trouble now, right? Just...leave. Ok?"
scene ep9_vinny15 with dissolve
vi "Easy there, boy. You're gonna hurt my feelings."
scene ep9_vinny16 with dissolve
mc "Believe me, I'm gonna hurt a lot more than your feelings if you keep pushing. Don't fucking test me."
$ new_bio("You", "I told Vinny off when he shoved me in my room.")
$ new_bio("Vinny", "I told Vinny off when he shoved me in my room.")
jump ep9_vinny_gun_leave_label

label ep9_vinny_ask_label:
$ renpy.block_rollback()
$ ep9_vinny_choice = "CHICK"
$ renpy.music.stop(channel="sfx1", fadeout=1)
scene ep9_vinny14 with dissolve
mc "Vinny... What the fuck? Relax! I'm just asking you to leave."
mc "Trust me, you don't want to fight me, so don't start one."
scene ep9_vinny15 with dissolve
vi "Don't start a fight? Haha!"
vi "Life doesn't work that way."

$ new_bio("You", "I tried to act friendly with Vinny and defuse the situation when he shoved me in my room.")
$ new_bio("Vinny", "I tried to act friendly with Vinny and defuse the situation when he shoved me in my room.")

label ep9_vinny_gun_leave_label:
stop music fadeout 3
scene ep9_vinny17 with dissolve
vi "You need to learn your place."
label ep9_vinny_gun_leave2_label:
if ep9_vinny_choice == "DIK":
    scene ep9_vinny18b with dissolve
else:
    scene ep9_vinny18 with dissolve

play music "music/ep5/suspense5.mp3"
vi "Good boy. Listening to commands, much like a dog."
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
if ep9_vinny_choice == "DIK":
    scene ep9_vinny19b with dissolve
    vi "Dog's got a nasty bite. You're a rabid pooch, aren't you?"
    vi "Rabid dogs get put down."
elif ep9_vinny_choice == "NEUTRAL":
    scene ep9_vinny19 with dissolve
    vi "Dog's got a bark, but no bite."
    vi "You have to teach barking dogs to be obedient."
else:
    scene ep9_vinny19 with dissolve
    vi "This sissy has his tail between his legs. You're a fucking puppy, aren't you?"
    vi "Dogs that got no bark or teeth to flash don't get to call the shots."

if affinity != "CHICK":
    scene ep9_vinny19c with dissolve
    $ renpy.pause()
scene ep9_vinny20 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=1)
tm "Vinny...? What are you doing?"
if ep9_vinny_choice == "DIK":
    scene ep9_vinny21 with dissolve
else:
    scene ep9_vinny21b with dissolve
vi "Housebreaking your pet. He's got an attitude."
scene ep9_vinny20 with dissolve
tm "Vinny... It's time to leave. The party's over. I'll show you out."
if ep9_vinny_choice == "DIK":
    scene ep9_vinny22 with dissolve
else:
    scene ep9_vinny22b with dissolve
vi "See, dog? That's how you should behave. Polite and submissive."
vi "Be a good dog now."
scene ep9_vinny23 with dissolve
$ renpy.pause()
scene ep9_vinny24 with dissolve
$ renpy.pause()
scene ep9_vinny25 with dissolve
mc "Tommy...? What the fuck?"
scene ep9_vinny26 with dissolve
tm "You ok?"
scene ep9_vinny25 with dissolve
mc "I...feel sick. Should we call the cops?"
scene ep9_vinny26 with dissolve
tm "What? No. Not the cops. Leave this one to me."
scene ep9_vinny25 with dissolve
mc "He had a fucking gun on him!"
scene ep9_vinny27 with dissolve
tm "Dude, chill. It's not a real gun; it's just a bad joke. It's the prop gun from Rusty's room."
tm "You know the one. I rigged that murder scene with it."
scene ep9_vinny28 with dissolve
mc "Still... Does that even matter?"
tm "He must have felt threatened by you. Take it as a compliment."
scene ep9_vinny29 with dissolve
tm "Look. I'm gonna level with you."
tm "He sold me some weed. If you call the cops for this, you're only gonna drag the DIKs and me into some deep shit."
scene ep9_vinny30 with dissolve
tm "Just let it go, and let me handle him."
tm "This won't happen again, I swear. He's not coming back here."
scene ep9_vinny31 with dissolve
mc "I feel like I'm gonna throw up."
scene ep9_vinny30 with dissolve
tm "It's the adrenaline; go grab some fresh air or something."
scene ep9_vinny32 with dissolve
mc "Don't. Just go."
tm "..."
scene ep9_vinny33 with dissolve
$ renpy.pause()

stop music fadeout 5
scene ep9_vinny34 with dissolve
mc "(What a fucking mess he made in here.)"
scene ep9_vinny35 with dissolve
mc "(Such an asshole!)"
if ep9_vinny_choice == "DIK":
    mc "(I shouldn't have gone easy on him. But next time, I won't...)"
    mc "(Fuck... My mouth hurts... That prop gun packed a punch.)"
else:
    mc "(I should have kicked his fucking ass! Try to threaten me like that... Fuck him!)"
scene ep9_vinny36 with fade
mc "(*{i}Sigh{/i}* There...)"
mc "(Ok... Snap out of it. Back to the party...or what's left of it.)"
$ event_list.append("ep9_diks_ph3_sally_event_label")
if persistent.mod_wtenabled:
    $ optional_task_list[8] = "Talk to Sarah & Melanie (Kitchen)"
else:
    $ optional_task_list[8] = "Talk to Sarah & Melanie"
if persistent.mod_wtenabled:
    $ optional_task_list[9] = "Find Sally (Upstairs bathroom)"
else:
    $ optional_task_list[9] = "Find Sally"
if branchAlone and (envyLikesYou or ep7_lily_lewd):
    $ event_list.append("ep9_diks_ph3_ln_leaving_event_label")
    if persistent.mod_wtenabled:
    
        $ optional_task_list[4] = "Talk to Lily & Nicole (Main Party room)"
    else:
        $ optional_task_list[4] = "Talk to Lily & Nicole"
$ task_list[2] = ""
$ updateTaskList()
$ new_bio("Vinny", "Vinny threatened me with a prop gun at the Halloween party.")
jump ep9_diks_ph3_qt2_event_label

label ep9_diks_ph3_room_event_label:
scene ep9_diks_ph3_room_event1 with dissolve
el "One at a time! If anyone wants a group shot, let me know."
mc "(Yikes... I'll come back later. There are too many people in here.)"
jump endEvent

label ep9_diks_ph3_costume_event_label:
$ mphone_play_songs(["music/ep9/licensed_music/track126.mp3","music/ep9/the_friendly_monster_shop.mp3"])
if branchIsabella:
    scene ep9_diks_ph3_costume_event1c with dissolve
else:
    if branchJill:
        scene ep9_diks_ph3_costume_event1b with dissolve
    else:
        scene ep9_diks_ph3_costume_event1 with dissolve
sa "Is everyone having a good time?"
"*{i}Cheers{/i}*"
sa "It's cool to see so many of you in here. I wasn't sure if people would be able to walk by now or not."
scene ep9_diks_ph3_costume_event2 with dissolve
sa "But it's all good! Help us drink all the beer and booze, don't be shy tonight."
sa "Can we give a round of applause for the DIKs? Haven't they been great hosts tonight?"
play sound "sound_effects/season2/applause_audience2.mp3"
"*{i}Applause{/i}*"
scene ep9_diks_ph3_costume_event3 with dissolve
sa "And another applause for the HOTs being a big part of the evening as well."
play sound "sound_effects/season2/applause_audience.mp3"
"*{i}Applause{/i}*"
scene ep9_diks_ph3_costume_event2 with dissolve
sa "Before everyone goes off on their end-of-the-night adventures, we're gonna have a little competition."
sa "We have been checking you out during the night, trying to decide who's wearing the best costume out of the lot."
scene ep9_diks_ph3_costume_event4 with dissolve
sa "And by we, I mean the judges of this competition. Aside from myself, give a round of applause for Quinn."
play sound "sound_effects/season2/applause_audience2.mp3"
"*{i}Applause{/i}*"
scene ep9_diks_ph3_costume_event5 with dissolve
sa "And representing the DIKs, we have [name]. He's been planning this party together with us and Tommy, I might add."
play sound "sound_effects/season2/applause2.mp3"
"*{i}Applause{/i}*"
if swyper_rejected_by_ida:
    scene ep9_diks_ph3_costume_event6 with dissolve
    uk "BOOOH!!! HATER!!!"
    mc "What?"
    scene ep9_diks_ph3_costume_event18 with dissolve
    uk "Hater!!!"
    scene ep9_diks_ph3_costume_event8 with dissolve
    qu "It looks like [name] has been naughty this year. No Christmas gifts for you."
    scene ep9_diks_ph3_costume_event7 with dissolve
    mc "I'm not a hater."
    scene ep9_diks_ph3_costume_event19 with dissolve
    ida "You ARE a HATER! I remember you from Swyper! You were horrible to me!"
    scene ep9_diks_ph3_costume_event8 with dissolve
    qu "Dude... You tried to get with that thing?"
    scene ep9_diks_ph3_costume_event9 with dissolve
    mc "No. She was using her friend's picture in her profile to catfish guys."
    scene ep9_diks_ph3_costume_event8 with dissolve
    qu "Ah, the catfish. Or, in this case, fatfish."
    scene ep9_diks_ph3_costume_event19 with dissolve
    ida "I heard that! Bullies!!!"
    ida "You have no idea how hard it is to find a quadruple XL-size Halloween costume!"
    scene ep9_diks_ph3_costume_event20 with dissolve
    mic "Ida. Calm down."
    scene ep9_diks_ph3_costume_event10 with dissolve
    sa "So, um... Where were we? Right - the jury."

scene ep9_diks_ph3_costume_event2 with dissolve
sa "It's been very difficult to crown a winner since you're all looking fabulous tonight."
sa "And I'm sure you all have your opinion on who's dressed the best."
scene ep9_diks_ph3_costume_event21 with dissolve
de "Opinions are like balls! We all got them."
scene ep9_diks_ph3_costume_event3 with dissolve
sa "So, we have narrowed it down to three guests."
scene ep9_diks_ph3_costume_event11 with dissolve
sa "One of which will go home with the DIKs' Halloween award."
sa "This is Willy! Willy's custom-made for this competition."
"*{i}Laughter{/i}*"
scene ep9_diks_ph3_costume_event2 with dissolve
sa "Can the following three guests please come up on stage?"
sa "Leon dressed as Lily!"
scene ep9_diks_ph3_costume_event37 with dissolve
le "No!"
scene ep9_diks_ph3_costume_event12 with dissolve
qu "Hahaha!"
sa "Come on, Leon. We're being sincere here. It's an amazing costume."
sa "Give it up for Leon, everyone."
scene ep9_diks_ph3_costume_event38 with dissolve
tm "No, thank you!"
"Hahaha!"
if branchIsabella:
    scene ep9_diks_ph3_costume_event13 with dissolve
    sa "I'm sure you've all noticed one of the scarier-looking costumes at the party."
    scene ep9_diks_ph3_costume_event32 with dissolve
    sa "There's a mysterious mummy among us..."
    uk "Who is that?"
    scene ep9_diks_ph3_costume_event14 with dissolve
    sa "Yes, over there in the back. Come up on stage."
    play sound "sound_effects/season2/applause_audience2.mp3"
    "*{i}Applause{/i}*"
else:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "Kylie with her hot nurse outfit!"
    scene ep9_diks_ph3_costume_event25 with dissolve
    ky "Did Becky leave? Make sure you get a picture of this."

scene ep9_diks_ph3_costume_event2 with dissolve
sa "And finally..."
if "Derek" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "Derek, the astronaut."
    scene ep9_diks_ph3_costume_event22 with dissolve
    de "I won!"
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "Well, that's not decided yet. But come on down here."
elif "Riona" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "The cutest cat at the party! Riona!"
    if branchIsabella:
        scene ep9_diks_ph3_costume_event24 with dissolve
    else:
        scene ep9_diks_ph3_costume_event24b with dissolve
    ri "I bet this is because of [name]."
elif "Camila" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "The sexy student, Camila!"
    scene ep9_diks_ph3_costume_event23 with dissolve
    cam "Haha! No way!"
elif "Sarah" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "This party has several bunnies, but there can be only one... Sarah!"
    scene ep9_diks_ph3_costume_event26 with dissolve
    sar "Hah! Suck it, Mel!"
    ml "Aw! I thought [name] would pick me."
elif "Melanie" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event16 with dissolve
    sa "This party has several bunnies, but there can be only one... Melanie!"
    scene ep9_diks_ph3_costume_event27 with dissolve
    ml "Haha! Told you!"
    sar "Such a pity vote, I swear! Just like Leon."
elif "Nicole" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "The sexy teacher, Nicole!"
    scene ep9_diks_ph3_costume_event29 with dissolve
    nic "Teacher? No... I'm a student."
    ly "Haha, just roll with it."
elif "Lily" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "The sexy vampire villain, Lily!"
    scene ep9_diks_ph3_costume_event30 with dissolve
    ly "Haha! Awesome!"
    scene ep9_diks_ph3_costume_event38 with dissolve
    tm "Haha! Fucking hilarious! Leon and Lily are on the same stage."
    if branchIsabella:
        scene ep9_diks_ph3_costume_event39b with dissolve
    else:
        scene ep9_diks_ph3_costume_event39 with dissolve
    le "Sup..."
    ly "How is that me...?"
elif "Jill" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event17 with dissolve
    sa "Jill, dressed as a banana."
    scene ep9_diks_ph3_costume_event28 with dissolve
    ji "[name]..."
    bia "HAHA! Jill!!!"
    isa "Haha. You have to go up there."
elif "Josy" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "The petite fairy, Josy!"
    scene ep9_diks_ph3_costume_event36 with dissolve
    js "Oh?"
    my "You deserve it."
    js "Maybe it's because I'm tiny..."
    my "*{i}Whispers{/i}* No, it's because you're beautiful."
elif "Maya" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "The magical fairy, Maya!"
    scene ep9_diks_ph3_costume_event35 with dissolve
    my "Huh? Me? Why?"
    js "Yes! Go up there!"
elif "John Boy" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "Our hot little cowboy, John Boy!"
    scene ep9_diks_ph3_costume_event33 with dissolve
    jb "I told him I didn't want this."
    el "Haha! You can do it, baby."
elif "Elena" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "The pantsless cowgirl! Elena!"
    scene ep9_diks_ph3_costume_event34 with dissolve
    el "Yee haw!"
elif "Zoey" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event15 with dissolve
    sa "Zoey!"
    scene ep9_diks_ph3_costume_event31 with dissolve
    zo "Ok...?"

if branchIsabella:
    scene ep9_diks_ph3_costume_event40 with dissolve
    mc "*{i}Whispers{/i}* Don't freak out. Trust Sage."
    scene ep9_diks_ph3_costume_event41 with dissolve
    $ renpy.pause()

if branchIsabella:
    scene ep9_diks_ph3_costume_event74b with dissolve
else:
    scene ep9_diks_ph3_costume_event74 with dissolve
sa "These are the top three contestants! And now it's up to you to cheer for the costume you like the most."

scene ep9_diks_ph3_costume_event109 with dissolve
"*{i}Cheers{/i}*"
scene ep9_diks_ph3_costume_event105 with dissolve
if branchIsabella:
    uk "Big-titted girl!!! WOOO!!!"
else:
    uk "Slutty nurse, for the win!!!"
if branchIsabella:
    scene ep9_diks_ph3_costume_event75b with dissolve
else:
    scene ep9_diks_ph3_costume_event75 with dissolve
sa "Haha! Wait! Not all at once!"
sa "On my signal, give it up for Leon."
scene ep9_diks_ph3_costume_event43 with dissolve
sa "Now!"
scene ep9_diks_ph3_costume_event110 with dissolve
"*{i}Cheers{/i}*"
scene ep9_diks_ph3_costume_event38 with dissolve
tm "Flattest tits at the party award!"
if branchIsabella:
    scene ep9_diks_ph3_costume_event74b with dissolve
else:
    scene ep9_diks_ph3_costume_event74 with dissolve
sa "Interesting! We have the benchmark."
if branchIsabella:
    scene ep9_diks_ph3_costume_event41 with dissolve
    sa "Next up. Give it up for the scary mummy!"
else:
    scene ep9_diks_ph3_costume_event42 with dissolve
    sa "Next up. Give it up for Kylie!"
scene ep9_diks_ph3_costume_event111 with dissolve
"*{i}Cheers{/i}*"
if branchIsabella:
    scene ep9_diks_ph3_costume_event76b with dissolve
else:
    scene ep9_diks_ph3_costume_event76 with dissolve
sa "That's a loud cheer! Was it the loudest? We'll see."
if branchIsabella:
    scene ep9_diks_ph3_costume_event74b with dissolve
else:
    scene ep9_diks_ph3_costume_event74 with dissolve
sa "And please give your final cheer for..."
if "Derek" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event47 with dissolve
    sa "Derek!"
elif "Riona" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event54 with dissolve
    sa "Riona!"
elif "Camila" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event57 with dissolve
    sa "Camila!"
    cam "WOOOOO!!! YEAH!!!"
elif "Sarah" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event48 with dissolve
    sa "Sarah!"
elif "Melanie" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event49 with dissolve
    sa "Melanie!"
elif "Nicole" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event61 with dissolve
    sa "Nicole!"
elif "Lily" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event44 with dissolve
    sa "Lily!"
elif "Jill" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event62 with dissolve
    sa "Jill!"
elif "Josy" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event65 with dissolve
    sa "Josy!"
elif "Maya" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event68 with dissolve
    sa "Maya!"
elif "John Boy" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event50 with dissolve
    sa "John Boy!"
elif "Elena" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event51 with dissolve
    sa "Elena!"
elif "Zoey" == ep9_top_pick:
    scene ep9_diks_ph3_costume_event71 with dissolve
    sa "Zoey!"
"*{i}Cheers{/i}*"

scene ep9_diks_ph3_costume_event106 with dissolve
if branchIsabella:
    uk "Big tits definitely won!"
else:
    uk "Slutty nurse definitely won!"
scene ep9_diks_ph3_costume_event107 with dissolve
uk "..."
play sound "sound_effects/season2/puke.mp3"
scene ep9_diks_ph3_costume_event108 with dissolve
uk "*{i}Pukes{/i}*"

if branchIsabella:
    scene ep9_diks_ph3_costume_event76b with dissolve
else:
    scene ep9_diks_ph3_costume_event76 with dissolve
sa "Well done, everybody. I believe we have a clear winner of the costume contest!"
sa "The receiver of the \"Best Costume\" award..."
sa "Congratulations to..."
if branchIsabella:
    $ ep9_winner = "Isabella"
    scene ep9_diks_ph3_costume_event77 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "The scary mummy!"
    "*{i}Cheers{/i}*"
    scene ep9_diks_ph3_costume_event78 with dissolve
    isa "Uh... Thank you. I... I'm honored."
    $ new_bio("Isabella", "Bella won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Derek" or ep9_top_pick == "Sarah" or ep9_top_pick == "Melanie" or ep9_top_pick == "John Boy" or ep9_top_pick == "Elena" or ep9_top_pick == "Nicole":
    $ ep9_winner = "Leon"
    scene ep9_diks_ph3_costume_event52 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Leon!"
    scene ep9_diks_ph3_costume_event53 with dissolve
    le "No! Stop this! I'm not touching that fucking thing!"
    "*{i}Laughter{/i}*"
    scene ep9_diks_ph3_costume_event38 with dissolve
    tm "Treasure it, Leon!"
    $ new_bio("Leon", "Leon won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Jill":
    $ ep9_winner = "Jill"
    scene ep9_diks_ph3_costume_event63 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Banana Jill."
    scene ep9_diks_ph3_costume_event64 with dissolve
    ji "Um..."
    sa "No words for the crowd?"
    ji "Thank you for the...trophy."
    $ new_bio("Jill", "Jill won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Maya":
    $ ep9_winner = "Maya"
    scene ep9_diks_ph3_costume_event69 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Maya!"
    scene ep9_diks_ph3_costume_event70 with dissolve
    my "Did you guys make this one? Haha! It's so good!"
    my "Thanks, everyone! This party is...amazing!"
    $ new_bio("Maya", "Maya won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Josy":
    $ ep9_winner = "Josy"
    scene ep9_diks_ph3_costume_event66 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Josy!"
    scene ep9_diks_ph3_costume_event67 with dissolve
    js "Hahaha! This trophy is ridiculous! I'm loving the mustache!"
    $ new_bio("Josy", "Josy won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Riona":
    $ ep9_winner = "Riona"
    scene ep9_diks_ph3_costume_event55 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Riona!"
    scene ep9_diks_ph3_costume_event56 with dissolve
    ri "I don't know what to say. Damn! Thanks, everyone, for the big...cock, I guess."
    ri "And sorry, Leon. I know you probably wanted this one."
    "*{i}Laughter{/i}*"
    scene ep9_diks_ph3_costume_event38 with dissolve
    tm "Don't worry, Leon! You can probably borrow it!"
    $ new_bio("Riona", "Riona won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Camila":
    $ ep9_winner = "Camila"
    scene ep9_diks_ph3_costume_event58 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Camila!"
    cam "Really? Yay!"
    scene ep9_diks_ph3_costume_event59 with dissolve
    cam "Thanks! Oh my God! Wow! Uhh..."
    cam "Whatever you do in life...for whatever reason...always don't forget to..."
    scene ep9_diks_ph3_costume_event60 with dissolve
    cam "[name]? What was I saying?"
    mc "Uh... I don't know."
    scene ep9_diks_ph3_costume_event59 with dissolve
    cam "Don't drink or drive! WOO!!!"
    $ new_bio("Camila", "Camila won the best costume contest at our Halloween party.")
elif ep9_top_pick == "Lily":
    $ ep9_winner = "Lily"
    scene ep9_diks_ph3_costume_event45 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Lily!"
    scene ep9_diks_ph3_costume_event46 with dissolve
    ly "Wow! Speech?"
    ly "Um... If this isn't proof of reaching the top, what is?"
    $ new_bio("Lily", "Lily won the best costume contest at our Halloween party.")
else:
    $ ep9_winner = "Zoey"
    scene ep9_diks_ph3_costume_event72 with dissolve
    play sound "sound_effects/season2/applause_audience2.mp3"
    sa "Zoey!"
    scene ep9_diks_ph3_costume_event73 with dissolve
    zo "But...why? Uh... Thanks?"
    $ new_bio("Zoey", "Zoey won the best costume contest at our Halloween party.")

if branchIsabella:
    scene ep9_diks_ph3_costume_event79 with dissolve
else:
    scene ep9_diks_ph3_costume_event79b with dissolve
play sound "sound_effects/season2/applause_audience2.mp3"
sa "Give it up for all contestants and yourselves! Thank you all for coming tonight! Let's party until we drop!"
"*{i}Cheers{/i}*"

if ep9_winner == "Maya":
    scene ep9_diks_ph3_costume_event97 with dissolve
    my "This is your doing, isn't it?"
    scene ep9_diks_ph3_costume_event98 with dissolve
    mc "Blame the audience."
    scene ep9_diks_ph3_costume_event97 with dissolve
    my "You're unbelievable."
    scene ep9_diks_ph3_costume_event98 with dissolve
    mc "You don't have to keep that thing."
    scene ep9_diks_ph3_costume_event99 with dissolve
    my "Haha! I'm gonna! Is it weird that this is the nicest award I've ever gotten?"
    mc "Haha!"
elif ep9_winner == "Josy":
    scene ep9_diks_ph3_costume_event100 with dissolve
    mc "You so deserve that penis."
    scene ep9_diks_ph3_costume_event101 with dissolve
    js "You're so dead."
    mc "Haha!"
elif ep9_winner == "Isabella":
    scene ep9_diks_ph3_costume_event80 with dissolve
    mc "See how great that went?"
    isa "I can't believe you did that to me."
    mc "I swear, it wasn't me. And you could trust Sage, couldn't you?"
    scene ep9_diks_ph3_costume_event81 with dissolve
    sa "Sorry for that. It was Quinn's idea. She genuinely liked your costume."
    scene ep9_diks_ph3_costume_event82 with dissolve
    isa "Clearly, I haven't had enough to drink to get through this night."
    scene ep9_diks_ph3_costume_event81 with dissolve
    sa "Come! Let's get another shot!"
elif ep9_winner == "Zoey":
    scene ep9_diks_ph3_costume_event102 with dissolve
    zo "How many strings did you pull for this to happen?"
    scene ep9_diks_ph3_costume_event103 with dissolve
    mc "None."
    mc "Ok, maybe one. But it was the audience who made the final call."
    scene ep9_diks_ph3_costume_event104 with dissolve
    zo "Whoever made this award has some sick imagination."
    scene ep9_diks_ph3_costume_event103 with dissolve
    mc "You should see the helmet we had to wear for Hell Week."
    scene ep9_diks_ph3_costume_event102 with dissolve
    zo "Let me guess. Another dick?"
    scene ep9_diks_ph3_costume_event103 with dissolve
    mc "Right on the forehead."
    zo "Haha!"
elif ep9_winner == "Lily":
    scene ep9_diks_ph3_costume_event95 with dissolve
    ly "Haha! Thanks, [name]. But if you wanted me to get a dick, all you had to do was ask."
    scene ep9_diks_ph3_costume_event96 with dissolve
    mc "Your costume is great, Lily. No lie."
elif ep9_winner == "Leon":
    if affinity == "DIK":
        scene ep9_diks_ph3_costume_event83 with dissolve
        mc "Congrats, Leon!"
        qu "Deserved!"
        scene ep9_diks_ph3_costume_event84 with dissolve
        le "Go fuck yourselves."
        mc "Hahaha!"
    else:
        scene ep9_diks_ph3_costume_event85 with dissolve
        mc "Chin up, Leon."
        scene ep9_diks_ph3_costume_event86 with dissolve
        le "This night now sucks for another reason."
elif ep9_winner == "Jill":
    scene ep9_diks_ph3_costume_event87 with dissolve
    ji "[name]. I'm so embarrassed."
    scene ep9_diks_ph3_costume_event88 with dissolve
    mc "Don't be! You won the competition."
    scene ep9_diks_ph3_costume_event87 with dissolve
    ji "What am I going to do with this? I can't keep it."
    scene ep9_diks_ph3_costume_event89 with dissolve
    mc "Haha! Why not? You won it, fair and square."
    scene ep9_diks_ph3_costume_event90 with dissolve
    ji "Oh my God... Hahaha!"
elif ep9_winner == "Camila":
    scene ep9_diks_ph3_costume_event91 with dissolve
    cam "Thanks for voting for me, [name]."
    scene ep9_diks_ph3_costume_event92 with dissolve
    mc "How do you know it was me?"
    scene ep9_diks_ph3_costume_event91 with dissolve
    cam "I'm pretty sure the HOTs wouldn't vote for their own."
    scene ep9_diks_ph3_costume_event92 with dissolve
    mc "Haha, right... You deserved it!"
    scene ep9_diks_ph3_costume_event91 with dissolve
    cam "Haha! Thanks!"
else:
    scene ep9_diks_ph3_costume_event93 with dissolve
    ri "Looks like the cat costume paid off."
    scene ep9_diks_ph3_costume_event94 with dissolve
    mc "Big time! Enjoy that award."
    scene ep9_diks_ph3_costume_event93 with dissolve
    ri "Haha! Sick!"

if "early_freeroam_mutex" in event_list:
    $ event_list.remove("early_freeroam_mutex")

$ mphone_rooster_clear()

if "ep9_diks_ph3_penny_event_label" in event_list:
    $ event_list.remove("ep9_diks_ph3_penny_event_label")
    $ optional_task_list[3] = ""

$ optional_task_list[2] = "Check downstairs bathroom"
if persistent.mod_wtenabled:
    $ optional_task_list[6] = "Say goodbye to Rio & Cammy (Right hallway)"
else:
    $ optional_task_list[6] = "Say goodbye to Rio & Cammy"
if ep6_envy_lewd or ep8_sandy_lewd:
    if persistent.mod_wtenabled:
        $ optional_task_list[7] = "Find Sandy (Left hallway)"
    else:
        $ optional_task_list[7] = "Find Sandy"
if persistent.mod_wtenabled:
    $ task_list[13] = "Find Jamie (Main Party room)"
else:
    $ task_list[13] = "Find Jamie"
$ updateTaskList()
jump ep9_diks_ph3_vinny_event_label

label ep9_diks_ph3_bj_event_label:
scene ep9_diks_ph3_bj_event1 with dissolve
bia "Maybe I should be leaving too?"
scene ep9_diks_ph3_bj_event2 with dissolve
ji "Are you sure?"
scene ep9_diks_ph3_bj_event1 with dissolve
bia "Yeah, I mean, poor Liv."
scene ep9_diks_ph3_bj_event3 with dissolve
mc "Who's leaving?"
scene ep9_diks_ph3_bj_event5 with dissolve
bia "I might."
scene ep9_diks_ph3_bj_event4 with dissolve
mc "Bianca? No... Why this early?"
scene ep9_diks_ph3_bj_event5 with dissolve
bia "Liv was feeling sick and Matty is driving her home."
scene ep9_diks_ph3_bj_event4 with dissolve
mc "Is he now?"
scene ep9_diks_ph3_bj_event5 with dissolve
bia "Yeah. He'll be back after making sure she's ok, and then I might leave with him."
bia "He was feeling a bit bummed out by all of it. It's such a sad end to a fun night."
scene ep9_diks_ph3_bj_event2 with dissolve
ji "Yeah, it is."
scene ep9_diks_ph3_bj_event6 with dissolve
mc "You should stay a while longer. The party isn't over yet."
scene ep9_diks_ph3_bj_event7 with dissolve
bia "Yeah, but I feel bad for Liv."
scene ep9_diks_ph3_bj_event9 with dissolve
ji "Andy's at home; I'm sure he'll take good care of her."
scene ep9_diks_ph3_bj_event10 with dissolve
bia "Well, I feel bad for Matty too."
scene ep9_diks_ph3_bj_event9 with dissolve
ji "Aw, he's such a great guy to take care of her."
ji "We'll try to convince him to keep going when he returns."
scene ep9_diks_ph3_bj_event11 with dissolve
bia "You know what? When he calls, I'm gonna tell him I'll take a cab back home."
bia "That way, we can keep going."
scene ep9_diks_ph3_bj_event9 with dissolve
ji "Yes! That's the spirit!"
ji "Isn't that great, [name]?"
scene ep9_diks_ph3_bj_event6 with dissolve
mc "Yeah, it is..."
mc "How...long have you and Matthew been together?"
scene ep9_diks_ph3_bj_event8 with dissolve
bia "We're closing in on our two-year anniversary."
scene ep9_diks_ph3_bj_event9 with dissolve
ji "Is it already?"
scene ep9_diks_ph3_bj_event11 with dissolve
bia "Time moves so fast that it's crazy!"
scene ep9_diks_ph3_bj_event6 with dissolve
mc "Oh, only two years? To me, it felt like it would be longer."
scene ep9_diks_ph3_bj_event7 with dissolve
bia "We've known each other for longer than that. So, things moved rather quickly once we got together as a couple."
bia "We moved in together after six months. It just felt right."
scene ep9_diks_ph3_bj_event9 with dissolve
ji "You're such a great couple. Everybody thinks so."
scene ep9_diks_ph3_bj_event12 with dissolve
mc "(Oh, man... Why did this have to happen tonight?)"
scene ep9_diks_ph3_bj_event16 with dissolve
isa "Jill, there you are."
scene ep9_diks_ph3_bj_event13 with dissolve
ji "Hey! Where have you been off to? I thought you left."
scene ep9_diks_ph3_bj_event16 with dissolve
isa "No, I've been talking to some students of mine."
isa "They will be the reason for tomorrow's hangover."
scene ep9_diks_ph3_bj_event13 with dissolve
ji "Haha! And you said you were staying for one drink."
scene ep9_diks_ph3_bj_event15 with dissolve
mc "Haha, you know, you don't have to drink. You can say no."
scene ep9_diks_ph3_bj_event17 with dissolve
isa "Am I getting lectured by {b}you{/b}?"
scene ep9_diks_ph3_bj_event15 with dissolve
mc "Hey, I'll take the chances I get. You can't blame me for this."
scene ep9_diks_ph3_bj_event16 with dissolve
isa "No, I blame the banana over there."
scene ep9_diks_ph3_bj_event13 with dissolve
ji "Me? I only got you the first drink. It's not my fault you ended up drinking shots. Haha!"
scene ep9_diks_ph3_bj_event14 with dissolve
bia "You're like the coolest teacher ever."
scene ep9_diks_ph3_bj_event18 with dissolve
isa "It ends now. No more drinks."
isa "If they come to ask for me, I'm not here."
scene ep9_diks_ph3_bj_event19 with dissolve
sa "Haha! Look! There she is!"
scene ep9_diks_ph3_bj_event18 with dissolve
isa "Dammit."
scene ep9_diks_ph3_bj_event20 with dissolve
my "We didn't finish our drinking game yet!"

$ task_list[6] = ""
if branchIsabella or branchAlone:
    if "ep9_diks_ph3_tara_event_label" in event_list:
        if persistent.mod_wtenabled:
            $ task_list[6] = "Talk to the ghost (Right Hallway)"
        else:
            $ task_list[6] = "Talk to the ghost"
    elif "ep9_bsolo_label" in event_list:
        if persistent.mod_wtenabled:
            $ task_list[6] = "Talk to Bella (Main Party room)"
        else:
            $ task_list[6] = "Talk to Bella"
    
$ updateTaskList()
jump endEvent

label ep9_diks_ph3_db_event_label:
scene ep9_diks_ph3_db_event1 with dissolve
de "And when they have their backs turned, it's a good opportunity to change the video or fiddle with the phone."
scene ep9_diks_ph3_db_event2 with dissolve
isa "I see."
scene ep9_diks_ph3_db_event1 with dissolve
de "I'm not boring you with this, am I?"
scene ep9_diks_ph3_db_event2 with dissolve
isa "Not at all. I'd love to hear about all the tricks you use in class."
scene ep9_diks_ph3_db_event3 with dissolve
mc "Derek. Maybe you should leave it at that?"
scene ep9_diks_ph3_db_event5 with dissolve
de "[mc_de_up]... I think I'm gonna score tonight."
scene ep9_diks_ph3_db_event4 with dissolve
mc "*{i}Whispers{/i}* I hate to break it to you, but you won't score with this one."
scene ep9_diks_ph3_db_event5 with dissolve
de "Well, I think I might."
scene ep9_diks_ph3_db_event6 with dissolve
isa "*{i}Whispers{/i}* You won't."
de "Oh..."
jump endEvent
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

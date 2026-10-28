default heraoutcome = False
default heraslap = False
default moonlollipop = False
#default emmaroute= False
default lewdemma = False
#default emmasolo = False
#default aineroute = False

label ep7:
    scene ep6e
    with dissolve
    pause
    scene ep7
    with dissolve
    pause
    play music 'audio/EventualBloom.mp3'
    scene ep5_500
    with dissolve
    scene ep5_544
    with dissolve
    scene ep5_595
    with dissolve
    scene ep7_1
    with dissolve
    pause
    scene ep7_2
    with dissolve
    mc "So you were there..."
    scene ep7_3
    with dissolve
    mc "Right at the moment I made the stupidest choice in my life..."
    scene ep7_4
    with dissolve
    mc "Ahaa..."
    scene ep7_5
    with dissolve
    mc "AHAHAHAHAAA!"
    stop music fadeout 2
    scene black
    with dissolve
    pause
    play sound cinematicimpact
    show ep7_46
    pause 0.2
    play sound cinematicimpact
    show ep7_41
    pause 0.2
    play sound cinematicimpact
    show ep7_38
    pause 0.2
    play sound cinematicimpact
    show ep7_34
    pause 0.2
    play sound cinematicimpact
    show ep7_28
    pause 0.2
    play sound cinematicimpact
    show ep7_27
    pause 0.2
    play sound cinematicimpact
    show ep7_20
    pause 0.2
    play sound cinematicimpact
    show ep7_13
    pause 0.2
    play sound cinematicimpact
    show ep7_9
    pause 0.2
    play sound cinematicimpact
    scene black
    pause
    show ep7_6
    with Dissolve(2.0)
    play music 'audio/EventualBloom.mp3' fadein 6
    e "Hey, why are you crying?"
    mc "H-huh? What-"
    play sound chair
    show ep7_7
    with hpunch
    mc "Wait, what happened? Why am I in my room now?"
    scene ep7_8
    with dissolve
    mc "Don't tell me you..."
    e "Yes, I brought you back here. I'm also the one who dressed you."
    mc "T-then you saw... everything?"
    e "Why are you acting so flustered? You were already half-naked when you entered the bathroom."
    e "But you saw me and I saw you. Let's call it even."
    mc "So you're fine with it?"
    e "What's the point of dragging it out further?"
    e "Anyways, I'm sorry. That must have hurt..."
    scene ep7_9
    mc "Of course, it hurt!"
    e "Then you should get the door lock fixed, I think it's cursed."
    image emcmtmcr:
        "ep7_10.jpg"
        pause 3.0
        "ep7_11.jpg"
        pause .2
        repeat
    show emcmtmcr
    with dissolve
    e "That other day, you walked in while Aine was in there, right?"
    mc "How did you..."
    e "She told me, of course."
    mc "Ugh..."
    mc "Just for the record, I didn't mean to do that to either of you."
    e "...Who's next?"
    mc "......"
    yt "Here we are just having a casual conversation..."
    yt "Does she even..."
    yt "No... The real question right now is if she's actually Emy."
    scene ep7_12
    with dissolve
    mc "Hey... Uhh... Emma?"
    scene ep7_13
    with dissolve
    e "Hm?"
    mc "Did we... by any chance... meet when we were kids?"
    stop music fadeout 3
    scene ep7_14
    with dissolve
    e "!!!"
    scene ep7_15
    play sound opendoor
    e "...I don't have much time to talk, sorry. I have to go now."
    mc "H-hey, wait!"
    play sound closedoor
    scene ep7_16
    "*door closes*"
    play sound opendoor
    scene ep7_17
    "*door opens*"
    mc "Emma?!"
    a "[mc]?"
    a "Are you looking for Emma? She left just now."
    yt "That's so fucking fast!"
    scene ep7_18
    with dissolve
    mc "Yeah, I know that. She just left my room."
    a "Huh..."
    scene ep7_19
    with dissolve
    a "Why was she in your room, hm? Did you do something to her?"
    mc "Well... something happened, yeah..."
    mc "I entered the bathroom while she was in there and I paid a steep price..."
    scene ep7_20
    with dissolve
    a "Y-you!"
    mc "I did not mean to do it, I promise!"
    mc "Maybe she's right, that door lock is cursed or something!"
    a "Hrrmmmnn..."
    a "Cursed he says..."
    mc "*sighs* I have a lot on my mind right now, okay? Please... don't make it worse, I beg you."
    scene ep7_19
    with dissolve
    a "A-alright... I'll just... take a bath and then we can... talk..."
    scene ep7_21
    with dissolve
    mc "......"
    a "N-nevermind..."
    scene ep7_22
    with dissolve
    play sound closedoor
    "*door closes*"
    if ainepoint == 11:
        a "{i}He really looks so stressed. I wonder what happened between him and Emma."
        a "......"
    scene ep7_23
    with dissolve
    yt "I should just get myself ready for work."
    yt "......"
    scene ep7_24
    with dissolve
    pause
    play sound opendoorsilent
    scene ep7_25
    with dissolve
    play music shower2
    pause
    play sound closedoor
    scene ep7_26
    with dissolve
    yt "......"
    scene ep7_27
    with dissolve
    pause
    stop music fadeout 1
    scene ep7_28
    with dissolve
    e "......"
    play music 'audio/LinkYourArms.mp3'
    scene ep7_29
    with dissolve
    pause
    scene ep7_30
    with dissolve
    e "{i}No, no, no! Please, not the picture! Anything, but that!"
    show ep7_31
    with dissolve
    pause 0.3
    hide ep7_31
    show emmastrugglerun
    with dissolve
    pause 7.5
    play sound emmafall
    show ep7_32
    pause 0.2
    show ep7_33
    with dissolve
    pause 0.5
    show ep7_34
    with dissolve
    pause 0.5
    play sound closedoor
    show emmastrugglestairs
    with dissolve
    pause 2.2
    show ep7_35
    with dissolve
    pause 0.2
    play sound doorslam
    show ep7_36
    a "No way..." #crying
    scene ep7_37
    with dissolve
    a "You were Emma's..."
    play sound thud
    show ep7_38
    with hpunch
    "*thud*"
    a "*hics*"
    a "I'm so... sorry... I did not know..."
    scene ep7_39
    with dissolve
    e "Wait, what are you talking about?"
    scene ep7_40
    with dissolve
    e "......"
    scene ep7_41
    with dissolve
    e "[mc]?"
    scene ep7_42
    with dissolve
    mc "......"
    mc "So you were there..."
    mc "Right at the moment when I made the stupidest choice in my life..."
    scene ep7_43
    with dissolve
    mc "Ahaa..."
    scene ep7_44
    with dissolve
    mc "AHAHAHAHAAA!"
    mc "No, you were with me all this time, isn't that right?"
    scene ep7_45
    with dissolve
    mc "...Emy?"
    e "[mc] I..."
    play sound running
    scene ep7_46
    pause 0.5
    play sound cloth
    show ep7_47
    with hpunch
    e "Ahh..."
    scene ep7_48
    with dissolve
    e "......"
    e "[mc]..."
    mc "Mhm."
    scene ep7_49
    with dissolve
    e "*hics* [mc]~"
    mc "Mhm!"
    e "[mc]... I'm sorry, I..."
    mc "You did not tell me anything because you couldn't, right?"
    mc "I know, Emy... I know... I understand now."
    scene ep7_50
    with dissolve
    mc "If only I'd come back a little bit earlier, then none of this would've happened."
    mc "Not only you or Aine, or even Gwen did anything wrong here."
    mc "I made my own mistake. And I shamelessly did it in front of you."
    e "No, I-"
    mc "Your side must have come later."
    mc "For now, there is something I would like to end once and for all. We won't be able to properly move on if it stays like this."
    mc "Yeah, I kept saying that I already did... but this circumstance proved me wrong."
    scene ep7_51
    with dissolve
    mc "*clench*"
    mc "Aine, this is your mess too."
    mc "Stop crying and stand up."
    mc "I'm not in the right mood to sugarcoat my words, but I'm going to use you, so prepare yourself."
    scene ep7_52
    with dissolve
    a "*sniff*"
    scene ep7_53
    with dissolve
    a "You don't have to force me, I plan to do it myself."
    scene ep7_54
    with dissolve
    e "Hold on, what are you planning to do?"
    a "It feels so nice to see you being yourself, Emma. So I'm going to make sure it stays that way, no matter what it takes."
    a "We are going to finish where this all started, and you... are going to stay here."
    scene ep7_55
    with dissolve
    a "Do you understand?"
    mc "......"
    yt "This is the first time I've seen her act this way..."
    yt "Sure, she was like this in high school, but somehow it feels odd that I can almost say she is intimidating me even though I'm not the one she's addressing."
    yt "Looks like I'm about to witness a real shitshow."
    scene ep7_56
    with dissolve
    a "Don't stare at me, let's go."
    mc "*nods*"
    play sound closedoor
    scene ep7_57
    with dissolve
    g "Huh?"
    e "No, don't go there, please! She'll kill you two! That's why I couldn't tell you anything because I knew this would happen!"
    e "I don't care if it's me, but not you two!"
    scene ep7_58
    with dissolve
    e "Please reconsi-"
    a "And then what?!" with hpunch
    a "Stay like this and cower in fear of her forever?! No! I refuse, Emma!"
    a "I see everyone trying to blame themselves!"
    a "Because I did this, because I did that...!"
    a "Honestly, I'm sick of it! Why are we blaming ourselves because someone tried to play with our fates and naiveté?!"
    a "I know my mother better than any of you, but if I die in the process, then so be it!"
    a "If I don't come back... then call me an {b}idiot{/b}!"
    scene ep7_59
    with dissolve
    e "Aine!"
    yt "Shit, I've got shivers down my spine..."
    scene ep7_60
    with dissolve
    e "[mc]?"
    mc "I'm ready to accept anything at this point, Emy. If it's my time, it's my time."
    mc "But, relax... I won't let anything happen. Thanks to you, I now have a plan."
    a "[mc]! Let's stop wasting time!"
    mc "You have a lot to tell me later, right?"
    scene ep7_61
    with dissolve
    e "*hics* Yes... Yes, I do!"
    mc "Then hold on to that."
    scene ep7_62
    with dissolve
    mc "Watch her for me."
    g "Uhm... Okay."
    play sound thud
    show ep7_63
    with hpunch
    e "*thud*"
    g "Dude, hey! What's happening? It's so early in the morning and I'm so confused!"
    g "Why is everyone so dead-ass, and why the hell are you crying?"
    show ep7_64
    with hpunch
    e "*sobs* Gweeeeen~!"
    g "Whoa, whoa, whoa! Hold the phone!"
    g "Who are you?! Where's Emma?!"
    e "It's me~!"
    scene ep7_65
    with dissolve
    g "Then what's happening?! I'm getting creeped out, you know?"
    e "......"

    scene black
    with dissolve
    with fadeq

    scene ep7_66
    with dissolve
    e "Am I horrible for making such decisions?"
    e "Am I stupid for wanting something better?"
    scene ep7_67
    with dissolve
    g "Why... didn't you tell me anything before?"
    scene ep7_68
    with dissolve
    g "No... you didn't tell anyone... right?"
    g "That's why those two lost it when they realized what's happening."
    scene ep7_66
    with dissolve
    e "I couldn't... Not until earlier..."
    e "I was so afraid of what might happen if I did..."
    show ep7_69
    with dissolve
    e "I'm so afraid of losing anybody I care about because of me..."
    show ep7_70
    with dissolve
    e "I'm so afraid that my decision will lead us into the worst possible scenario..."
    show ep7_71
    with dissolve
    e "Just call me a cowa-"
    play sound slap
    show ep7_72
    with hpunch
    g "*slaps*"
    e "Ahh..."
    show ep7_73
    with hpunch
    g "*hugs*"
    g "Shut up..."
    g "Just fucking shut up..."
    g "You've lost everything multiple times, and yet... here you are..."
    g "Never... ever... call yourself a coward."
    g "Because If I were in your place, I don't know if I would still have the will to live..."
    g "You are the most strong-willed woman... I have ever known, Emma."
    g "To be honest with you, I really hate drama like this, that's why I ran away from my mother's beliefs in the first place..."
    g "Not a single tear came from my eyes for a long, long time after that..."
    show ep7_74
    with dissolve
    g "However, you... for fuck's sake... are making me tear up like shit..."
    g "You know, Em... There are things that we cannot control no matter how hard we try."
    g "But those two are stupid. And sometimes, being stupid is what it takes to have the courage to do a lot of things others cannot."
    g "All we can do... is have faith and trust that everything will be alright."
    g "Just believe in them."
    g "...For now, cry your heart out. I'll be here for you."
    scene ep7_75
    with dissolve
    e "*hics*"
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play music traffic
    scene ep7_76
    with dissolve
    "........"
    ".............."
    a "Who are you calling? You know I can just-"
    scene ep7_77
    with dissolve
    mc "Shhhhh..."
    mc "It's who I hope will be my secret weapon... who also happens to be your aunt."
    scene ep7_78
    with dissolve
    a "Pardon?"
    mc "I learned about this through Emma, I'll explain later."
    a "But why are you calling my... {b}aunt{/b}? If that's really true. I don't have one as far as I know."
    scene ep7_79
    with dissolve
    mc "......"
    a "Why do you always look like that when you find me stupid? I'm just telling you!"
    image aimctpark:
        "ep7_80.jpg"
        pause 3.0
        "ep7_81.jpg"
        pause .2
        repeat
    show aimctpark
    with dissolve
    mc "You and your family are waaay too much for me, Aine."
    a "...Aren't you nervous?"
    mc "Uhh... Why should I be? Is there anything I should be nervous about?"
    a "Excuse you..."
    a "You're meeting my mother — Hera."
    a "Owner of several companies in this city."
    a "The current leader of Agnor Family Mafia."
    mc "Wait, what?!"
    mc "Mafia?!"
    a "Uh-huh?"
    mc "Why didn't you tell me that beforehand?!"
    a "Well, because you never asked!"
    a "Why do you think the other students were afraid of me back then?"
    a "Why do you think the school officials could never touch me?"
    j "Excuse me, lovebirds. You shouldn't be fighting this early in the morning."
    scene ep7_82
    with dissolve
    mc "Oh, hey, uhh... Sorry, we were just arguing about something."
    j "Yes, that's what I just said, [mc]."
    mc "Did you hear everything?"
    j "Just from the moment she mentioned Agnor Family."
    j "{b}My{/b} family."
    j "But I suppose I shouldn't say that."
    mc "So you are a member of this Mafia thing, huh?"
    j "I may carry the last name, but I am, in fact, not a part of it."
    j "*chuckles* I'm way too far ahead of them."
    stop music fadeout 2
    mc "That chuckle tells me everything."
    play music 'audio/EventualBloom.mp3'
    scene ep7_83
    with dissolve
    j "And your lack of reaction tells me that you don't seem to believe anything."
    mc "Well, yeah. I have too many doubts about this, thus I have a question for you, Miss Jess."
    mc "No... Jess."
    j "... Now that's the way my employees should address me."
    j "You seem... not like yourself today. What's up?"
    mc "......"
    mc "... Are you guys using me?"
    scene ep7_84
    with dissolve
    j "*chuckles* And where did you get that idea?"
    mc "I don't have an informant, but I'm not that stupid, Jess."
    mc "These girls coming here was way too much of a coincidence for Emma to pick."
    mc "Agreeing for me to meet your sister was way too easy."
    mc "You meeting me before wasn't a simple stroke of luck either, no?"
    mc "And now, why do I feel that you have been waiting for this chance? I can hear the eagerness in your voice."
    j "Well, well... Aren't you a sharp one."
    j "Well, it looks like it's time for you to know."
    j "About you... and your real identity."
    j "But before that..."
    j "Go ahead and finish what you guys started."
    mc "So I was right, you were waiting for this to happen."
    scene ep7_85
    with dissolve
    j "Not quite. I was simply going with the flow, and of course, a huge part of it was a gamble."
    j "I know this is confusing. That's why I am inviting you to come to our hideout after you are done with your business."
    j "I bet you and Klara, might want to have a good talk as well."
    mc "I know, I have a lot of questions for her."
    mc "......"
    mc "And since you seem to be using me, I'm going to ask you to return the favor, Jess."
    scene ep7_86
    with dissolve
    j "*chuckles* I told you, I am not."
    j "Although, you sound exactly like someone I know. You're not dropping your guard that easily, I like it."
    j "... Very well."
    j "How can I serve you, boss?"
    mc "I know this won't go that easy {b}if{/b} this so-called Mafia actually exists. So I need men to protect us while we are in there."
    scene ep7_87
    with dissolve
    j "Alright, I'm sending two of my people to go with you."
    mc "Just two?"
    scene ep7_88
    with dissolve
    j "Believe me when I say that the two of them are more than enough."
    j "You're still in your house, right?"
    mc "We're not that far away."
    j "Good, wait for them."
    mc "Alright."
    j "And [mc]?"
    mc "Yes?"
    scene ep7_89
    with dissolve
    j "I'll just clarify that I am {b}not{/b} your enemy. I never was, and I never will be."
    j "And you... are not under anybody's control."
    j "Whether or not you take my word for it, is totally up to you."
    j "As for the rest, we'll talk later together with some people you might want to meet."
    mc "I'm looking forward to that."
    scene ep7_90
    with dissolve
    j "Go easy on her, will you?"
    mc "That is something I can't promise."
    scene ep7_91
    with dissolve
    j "Well? I hope you are ready for this, Klara. It came sooner than I expected."
    k "I'm nervous, of course. A lot of possible scenarios are running through my mind right now."
    j "And the same goes for him as well."
    j "Remember, I am just your tool, your weapon, whatever you want to call me. I can never help you if it is between you two."
    scene ep7_92
    with dissolve
    k "I know my responsibility."
    j "Good."
    scene ep7_93
    with dissolve
    k "Aside from that, I'm really worried about their confrontation."
    k "Can I go there too? I can't let anything happen to him, Jess."
    j "Considering your history with my sister, your presence might make her rage more."
    j "I will go there in your stead. I will bring the kids back safe and sound: you have my word."
    j "Furthermore, I'm also worried about what will happen to Freya after this. I don't want her to get caught in the conflict."
    play sound cloth
    scene ep7_94
    with dissolve
    k "......"
    j "Hey, chin up."
    j "Once this is over, why don't you go back home for a while? Spend some time with them and get rid of all your stubbornness."
    scene ep7_95
    with dissolve
    k "... I still don't fully understand why are you so eager to help us with our situation, Jess."
    k "Do you mind telling me the truth?"
    j "I simply want to mend both sides, Klara."
    j "Hera is still my sister no matter how horrible she became."
    j "You and Sky... are Georgia's collateral descendants that I swore to protect at her graveside."
    j "All of you are blinded by your pasts. And my boy is caught in the middle of it. So, my role is to bring light to your eyes."
    j "Wasn't that your goal in the first place?"
    k "...Yes."
    j "*chuckles* Unlike us, you are quite lucky that this is all you have to face."
    k "What do you mean?"
    j "You're about to see."
    scene ep7_96
    with dissolve
    "........"
    "............."
    un "Uhh... Hello?"
    j "Intelligence encrypted call, relax."
    un "Oh, hey, Jessy! What's up?"
    j "Tell them to come to Fang's hideout please, Eliza."
    un "Right away!"
    j "*click*"
    scene ep7_95
    with dissolve
    j "I'll be back."
    k "Mhm."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/RiverRunsDeep.mp3' fadein 3
    play sound jesscarroar
    scene ep7_97
    with dissolve
    pause
    scene ep7_98
    with dissolve
    pause
    play sound cardoorclose
    scene ep7_99
    with dissolve
    "*car door closes*"
    scene ep7_100
    with dissolve
    cl "You must be [mc] and Lady Aine."
    cl "It's nice to meet you two. We will be your bodyguards today."
    if gwenroute:
        scene ep7_101
        with dissolve
        yt "Wait, isn't she that girl from last time?"
        yt "She looks hella nice in that hair, though."
        scene ep7_102
        with dissolve
        scene ep7_101
        with dissolve
        yt "Oh boy..."
    scene ep7_103
    with dissolve
    a "Please don't address me like that, I'm nothing but an ordinary person."
    cl "I insist. We all know that you are not, Lady Aine."
    scene ep7_104
    with dissolve
    a "Tch! So be it, I'm not in the mood for this."
    yt "Hooo... She's really intimidating me, I should be careful not to annoy her from now on."
    scene ep7_105
    play sound cardoorclose
    "*car door closes*"
    cl "*chuckles* Like mother, like daughter..."
    image mccltoutt:
        "ep7_106.jpg"
        pause 3.0
        "ep7_107.jpg"
        pause .2
        repeat
    show mccltoutt
    with dissolve
    cl "Now before this all starts, remember this, kid..."
    cl "Whatever your problems are, I'm not someone you want to command to do things for you."
    cl "I follow who I should follow, and those are the people who can control me at my worst."
    cl "Do you understand?"
    mc "I'm not sure what you're trying to say, but I'll go with it for now."
    scene ep7_108
    with dissolve
    cl "......"
    image mccltoutt2:
        "ep7_109.jpg"
        pause 3.0
        "ep7_110.jpg"
        pause .2
        repeat
    show mccltoutt2
    with dissolve
    cl "Hm, I expected a different reaction."
    cl "Fear... is an insignificant value to you."
    cl "I guess we both see things eye to eye, after all."
    cl "But to be fair, you're different from all of them, and that is not an insult."
    mc "Why are you speaking like you've known me for a long time?"
    cl "I can fully assess a person just by looking at them."
    cl "They say that you don't judge a book by its cover, but it's a different story when I'm the judge."
    yt "...Who is this woman?"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music cardriveinterior fadein 2
    scene ep7_111
    with dissolve
    cl "Boss, we're near the compound."
    j "Good. We're hacking the gate's passcode. You should be able to enter without any trouble."
    j "There should be only a few guards on patrol at the moment, take them out."
    j "Remember, avoid spilling blood as much as possible. We don't need to go that far."
    cl "Copy."
    scene ep7_112
    with dissolve
    a "Just who are you people?"
    mc "I have the same question, to be honest."
    cl "We don't have the authority to tell you anything, so save that question for later."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play music 'audio/Reload.mp3'
    scene ep7_113
    with dissolve
    "*muffled shouting*"
    cl "No guns, huh? This place has become a daycare center."
    cl "Stay here."
    scene ep7_114
    play sound cardoorclose
    with dissolve
    "*car door closes*"
    play sound shockandawe
    show ep7_115
    cl "HAHAAA~!"
    play sound kick_heavy
    show ep7_116
    pause 0.2
    play sound kick_heavy
    show ep7_117
    pause 0.2
    play sound kick_heavy
    show ep7_118
    pause 0.2
    play sound kick_heavy
    show ep7_119
    with hpunch
    pause
    scene ep7_120
    play sound slurp
    with dissolve
    cl "*slurps*"
    scene ep7_121
    play sound whistle2
    m "*whistles*"
    m "Granny, chill..."
    scene ep7_122
    cl "Oops..."
    scene ep7_123
    with dissolve
    m "......"
    scene ep7_124
    with dissolve
    m "You two might wanna pick your jaws back up."
    scene ep7_125
    with dissolve
    scene ep7_126
    with dissolve
    m "......"
    scene ep7_127
    with dissolve
    m "Huh... This is a Mafia compound, right? Why are there so few guards?"
    a "No, the main hideout is far from here, this is just my mother's safehouse. But this isn't how it usually is, something is off here."
    mc "Did we just step into a trap or something?"
    scene ep7_128
    with dissolve
    a "No, that's not it."
    a "Mother is a very straightforward person: if she wants to do it, she will do it in the most textbook way possible."
    a "She's not the type to set traps."
    a "There is no way the guards would abandon their posts just like that, either."
    scene ep7_129
    with dissolve
    m "Well, remember what you came here for, this is no time to theorize."
    m "If this is a rabbit hole, then leave that problem to us, there's a reason why Jess chose us to assist you."
    menu:
        "Alright":
            mc "Alright."
        "Thanks":
            $ moonpoint += 1
            $ renpy.notify(moonnotif)
            mc "Thanks."
            m "That's unnecessary, go!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    show ep7_130
    with dissolve
    h "Ahh... We finally m-"
    play sound running
    play sound2 woosh2
    show ep7_130c
    pause 0.2
    hide ep7_130c
    show ep7_130a
    pause 0.1
    show ep7_130b
    pause 0.2
    show ep7_130c
    pause 0.6
    stop sound
    play sound slap
    show ep7_131
    with hpunch
    pause
    play sound slap
    show ep7_132
    with hpunch
    pause
    play sound slap
    show ep7_133
    with hpunch
    pause
    play sound thud
    show ep7_134
    with hpunch
    play music 'audio/EventualBloom.mp3' fadein 6
    "*thud*"
    scene ep7_135
    play sound chair
    with dissolve
    cl "We searched the whole area, you two are clear."
    mc "*nods*"
    scene ep7_136
    with dissolve
    h "Ughh..."
    cl "*chuckles* What a sorry state you are in, woman."
    h "Like you're one to talk."
    scene ep7_137
    play sound cloth
    with dissolve
    mc "Yes, it is nice to finally meet you, Hera."
    mc "So, how does it feel to have your own daughter used against you?"
    h "Bastard!" with hpunch
    h "You assassin clan members are nothing but a goddamn annoyance!"
    yt "Assassin clan members?"
    scene ep7_138
    with dissolve
    yt "Is she talking about those two? Or..."
    scene ep7_139
    a "Where are Emma's papers? Give them to me."
    h "Is that how you ask your mother for a favor? It's such a pity seeing what this guy turned you into, my dear daughter."
    a "I never once asked you for a favor, I'm telling you to do it."
    a "And no, you are wrong..."
    a "It is {b}you{/b} who turned me into this, mother."
    a "I should've done this long ago, but despite what you did, I still had a little respect for you because you are the one who gave birth to me."
    scene ep7_140
    with dissolve
    a "I was hoping that one day... you'd change, because I've always missed the old you."
    a "You would always pat my head every time I did something good."
    a "They might have been {b}nothing{/b} to you, but I deeply cherished those moments."
    a "But after I learned that you are the one playing with our fates..."
    a "I lost it, mother..."
    a "No... you are not my mother. She is already long gone."
    scene ep7_141
    with dissolve
    f "Hm? What's with all the commotion out there?"
    f "Wait, isn't that sis?!"
    scene ep7_142
    play sound doorknock
    with dissolve
    "*knocks*"
    f "Uhm... Yes?"
    j "Freya, dear. It's me."
    f "Jess?! What are you doing here? I mean, come in!"
    scene ep7_143
    play sound closedoor
    with dissolve
    j "Come with me. You have to know something."

    scene black
    with dissolve
    with fadeq

    scene ep7_144
    with dissolve
    f "*gasps*"
    f "Sis?! [mc]?! What in the hell are you all doing here?! What's happening?!"
    scene ep7_145
    with dissolve
    m "'Sup. Do you guys have some popcorn? I forgot to bring some lollipops."
    cl "Fang, quiet."
    scene ep7_146
    with dissolve
    h "*chuckles*"
    play sound heralaugh
    show ep7_147
    h "AHAHAHAHAHAHAHAAA!!"
    show ep7_148
    h "AAAHAHAHAHAHAHAHAHAHAHAHAHAAAA~!!"
    h "Yes! You are right, the old me is long gone!"
    h "I lost everything from the day I lost this family's hopes, Aine!"
    a "......."
    scene ep7_149
    with dissolve
    h "You know, boy..."
    h "Klara and I used to be close friends."
    h "... No, we were {b}best friends{/b}."
    scene ep7_150
    with dissolve
    h "(I chose to be a lone wolf thinking that nobody would have the guts to get close to me because of my name, but I was wrong.)"
    scene ep7_151
    with dissolve
    k "Hey, you're that Mafia gal everyone is talking about, yes?"
    k "Damn, girl, you are pretty!"
    k "By the way, is this seat taken?"
    h "Uhh... No."
    scene ep7_152
    with dissolve
    k "Phew~! I thought I was going to be late."
    h "(I used to stare at her wondering why she was not afraid of me.)"
    h "(Hell, no one even wanted to sit in the same row with me, but she was different.)"
    h "(Things like status or names don't matter to her.)"
    scene ep7_153
    with dissolve
    h "(And so I accepted her into my life.)"
    scene ep7_154
    with dissolve
    k "What?! Did you forget what the professor said yesterday?!"
    k "Girl, you are mentally challenged!"
    h "Excuse me?! I'm taking notes, you bitch! There is no way I'm wrong!"
    k "You took the wrong notes then!"
    h "(We used to fight often. However, that did not stop our friendship — rather, it brought us even closer.)"
    scene ep7_155
    with dissolve
    h "(...Until we fell in love with the same guy... Jovian.)"
    h "(Jovian was my personal bodyguard who treated me with the utmost respect.)"
    h "(Not long after he got appointed, I came to fall in love with him.)"
    h "(My feelings for him made me ignore the reality...)"
    h "(But I learned that it's not always going to be about you...)"
    h "(That there is always someone better than you out there...)"
    h "(Years later, after we graduated from college... it finally came down to it.)"
    scene ep7_156
    with dissolve
    jov "I'm really sorry, Hera..."
    jov "I'm going to quit my job, so this might be the last day we'll see each other."
    jov "I already asked your father about it."
    h "After everything I did for you, this is a sorry excuse, Jovian."
    scene ep7_157
    play sound shoedown
    with dissolve
    h "Honestly, it wasn't hard for me to let go. I wasn't so heartless as to not understand the situation."
    scene ep7_158
    with dissolve
    h "And so, I let them have the life they wanted."
    scene ep7_159
    with dissolve
    h "A few months later, I eventually found the man that completed my missing piece — Richard, Aine and Freya's father."
    h "We were happy with what we had and couldn't have asked for anything more..."
    h "Now, you two listen carefully."
    scene ep7_160
    with dissolve
    h "In our family, bearing a male offspring is considered our hope — the next heir of the group."
    h "However, it also carries great danger."
    h "After finding out that I was pregnant with a boy, your father and I decided and told you that we would temporarily live away."
    h "For you... and your brother's safety."
    scene black
    with dissolve
    h "But..."
    scene ep7_161
    with dissolve
    ri "......"
    scene ep7_162
    with dissolve
    h "Don't stare at him like that, or he'll melt."
    ri "He's so lovely..."
    ri "Too bad, seems he got everything from you. He doesn't even have my nose."
    h "Well, he's got your hair color, at least. And I reckon he got his personality from you."
    scene ep7_163
    with dissolve
    ri "Heeh... How can you tell?"
    h "Never underestimate a mother's instinct, Richard."
    ri "Alright, alright. I'll give it to you."
    scene ep7_164
    with dissolve
    h "I can't wait to show him to his sisters. Aine was so excited when I told her that we're finally coming home."
    ri "They will love him for sure."
    ri "After my time, he'll be the one to lead the group, no?"
    h "Exactly..."
    h "Father may still be alive, but when it's our time, we'll change the group into something better."
    h "Something that will help our people achieve their dreams."
    scene ep7_165
    with dissolve
    ri "Oof... That will be a challenge considering the current state of the group."
    h "Don't worry, you have me."
    scene ep7_164
    with dissolve
    ri "...Yeah... For Simon."
    ri "I'm sure he'll be the greatest leader among us."
    h "I never thought that you would be this kind of dreamer, Richard."
    ri "Well, even though I was just a simple man without any knowledge of your family, your father accepted me for who I am."
    ri "So in return, I'll be a good son-in-law and a father to his grandchildren."
    scene ep7_166
    with dissolve
    h "Mmm..."
    h "But don't think about it for now."
    ri "Although... There was a time where I thought of taking you all away from this kind of living and just having a simple life like any other family out there..."
    h "I thought we already talked about that?"
    h "Even if we hide, you know that my father will always find us no matter how far we go."
    h "As long as he's alive, we can never fully break away from his grasp."
    h "Don't worry, Richard. We'll be fine, trust me."
    ri "Yeah..."
    scene ep7_167
    with dissolve
    ri "*chuckles* Jovian once told me about his son."
    ri "I'm sure that someday, we will have a time where we can have fun together..."
    scene ep7_168
    with dissolve
    h "Just his son, huh?"
    h "So it's just all you boys?"
    ri "W-well... Ahaha!"
    ri "Of course, you're going to be with us. From time to time maybe?"
    h "I'm going to kill you if one of our kids turns out to be like you!"
    ri "I'm just kidding, just kidding!"
    ri "You'll be with me wherever I go, Hera. You and the girls."
    scene ep7_169
    with dissolve
    h "And of course, our handsome little Simon."
    scene ep7_170
    with dissolve
    h "I love you, Richard."
    ri "I love you too, Hera."
    h "Time to go home?"
    ri "Yeah, let's go."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play music cardriveinterior
    scene ep7_171
    with dissolve
    ri "Jeez... I'm so excited. I can't wait to show him to the girls."
    h "Yes, me either. It's been more than a year since we last saw them too."
    ri "I'm sure they will be losing their minds. Haha!"
    h "Hmhmm... I know."
    scene ep7_172
    with dissolve
    ri "Hera, let's-"
    stop music
    play sound carcrash
    show ep7_173
    pause 0.6
    show black
    pause
    scene ep7_174
    with Dissolve(4.0)
    ri "Uugh... Shit...!"
    ri "What..."
    stop sound fadeout 3
    ri "What just... happened...?"
    play music 'audio/InPieces.mp3'
    play sound babycry loop
    scene ep7_175
    with Dissolve(2.0)
    ri "Hera!" with hpunch
    ri "No, no, no, no!"
    ri "Hera, are you alright?!"
    ri "*coughs* Simon... Thank god he's fine."
    scene ep7_176
    with dissolve
    h "Ri..."
    h "Richard..."
    h "Take..."
    h "Take Simon..."
    h "This car might..."
    ri "Hera!"
    ri "Hold on! I'll get yo-"
    ri "Ack!!" with hpunch
    ri "M-my legs! T-they're stuck!"
    h "Take our son... outside, Richard..."
    scene ep7_177
    with dissolve
    ri "I think... I can... pull my feet out of my shoes!"
    ri "*breathes intensely*"
    show ep7_178
    with hpunch
    ri "*grunts* ACK!!"
    scene ep7_179
    with dissolve
    ri "Simon..."
    ri "I'm sorry..."
    ri "It's all daddy's fault. I'm sorry..."
    scene ep7_180
    with dissolve
    ri "Hera, wait for me... I'll be back."
    h "...Never mind me..."
    h "G...go...!"
    stop sound fadeout 2

    scene black
    with dissolve
    with fadeq

    play sound thud
    show ep7_181
    with hpunch
    play sound babycry loop
    ri "Ack! Shit, I broke my right leg!"
    scene ep7_182
    with dissolve
    ri "*dragging his leg* Hush... hush..."
    ri "Everything's okay, Simon... Dad is here."
    play sound2 rain loop fadein 2
    scene ep7_183
    with dissolve
    ri "Oh no, it's raining!"
    scene ep7_184
    with dissolve
    ri "Help! Somebody, we need help!"
    ri "My wife is-"
    scene ep7_185
    with dissolve
    ri "Huh?"
    ri "Who's..."
    ri "J...Jovian?!"
    scene ep7_186
    with dissolve
    jov "......"
    ri "You bastard! So it was you! How could-"
    scene ep7_187
    with dissolve
    pause 0.4
    play sound3 gunshot_muffled
    show ep7_188
    pause 0.2
    scene ep7_187
    with dissolve
    play sound3 thud
    "*thud*"
    scene ep7_189
    with dissolve
    jov "......"
    play sound3 gunshot_muffled
    stop sound
    show ep7_190
    pause 0.2
    scene ep7_189
    with dissolve
    pause
    scene ep7_191
    with dissolve
    h "......"
    scene ep7_192
    with dissolve
    pause
    scene ep7_193
    with dissolve
    pause
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade

    play sound rain loop fadein 2
    scene ep7_194
    with dissolve
    scene ep7_195
    with Dissolve(2.0)
    h "..."
    scene ep7_196
    with dissolve
    h "......"
    play sound2 cough_female
    show ep7_197
    h "*coughing*"
    scene ep7_198
    with dissolve
    h "Richard..."
    h "Simon..."
    scene ep7_199
    with dissolve
    pause
    scene ep7_200
    with dissolve
    pause
    play sound2 thud
    show ep7_201
    with hpunch
    "*thud*"
    h "Ri-"
    scene ep7_202
    with dissolve
    pause
    scene ep7_203
    with Dissolve(5.0)
    pause
    scene ep7_204
    with Dissolve(2.0)
    pause
    play sound2 herascream
    show ep7_205
    h "AAAAAAAAAAAAAAAAHHHH!!!!!"
    scene ep7_206
    with dissolve
    scene black
    with Dissolve(5.0)
    stop sound fadeout 2

    scene ep7_207
    with dissolve
    h "I swore to myself that I would kill him because of what he did, but he was nowhere to be found no matter how much I tried to look for him."
    h "So you... took the brunt of his sins."
    h "He took my son from me, but instead of killing you in return, making you suffer was the best choice."
    scene ep7_208
    with dissolve
    h "But even after that, he still won't show his face! He's nothing but a coward!"
    scene ep7_209
    with dissolve
    a "So... it was the man who took you in?"
    scene ep7_210
    with dissolve
    mc "*clench*"
    mc "*breathes heavily*"
    yt "This... can't be true..."
    yt "There's no way he could do that..."
    yt "Compose yourself, [mc]... Compose yourself, don't let your feelings take over your actions..."
    yt "Not this time!"
    scene ep7_211
    with dissolve
    a "But why didn't you tell us anything about that?! We are your daughters — your family! Why did you keep it a secret from us?!"
    h "From the moment you were born... I knew you would follow in your father's footsteps. Kindness was always the answer."
    h "Now that you know, if I asked you to do the same thing to him right now — would you?"
    scene ep7_212
    with dissolve
    a "......"
    a "..........."
    scene ep7_213
    with dissolve
    a "No."
    h "Exactly."
    scene ep7_214
    with dissolve
    mc "Somehow, it all... makes sense..."
    mc "We waited for you for a decade because you said you would just follow us there..."
    mc "So this was what you were doing, huh?"
    mc "I lost someone important to me because of you..."
    mc "My life became hell because of you..."
    scene ep7_215
    with dissolve
    mc "Wherever you are..."
    mc "I'm going to find you, and you're not running away this time..."
    mc "If this is all true, then you are going to eat my fists... Jovian."
    scene ep7_216
    with dissolve
    mc "As for you..."
    menu:
        "Harsh answer":
            $ heraoutcome = False
            scene ep7_217
            with dissolve
            mc "...If you believe that I deserve to be punished because of what Jovian did to you, then so be it."
            mc "But Jovian's sins are not my own. What you were doing to us was simply just an act of selfishness and obsession."
            mc "We were {b}innocent{/b} kids, Hera. But you decided to make us part of your story that we had nothing to do with."
            mc "I want to kill you for toying with our lives..."
            mc "But, no..."
            mc "I don't have the right to take your life."
            mc "However... I will make you suffer more than what you did to us."
            mc "I'm stupid, and I may be nothing, but this nobody will bring you down. I will take everything that you have and I don't care who you are."
            scene ep7_220
            with dissolve
            h "{i}... *chuckles* Damn..."
        "Think logically":
            $ heraoutcome = True
            scene ep7_217
            with dissolve
            mc "...If you believe that I deserve to be punished because of what Jovian did to you, then so be it."
            mc "I understand that Jovian is the one in the wrong here. But that is no reason for you to control our lives."
            mc "You did not lose everything. Come on, you still have your {b}daughters{/b}. Why would you think that it's all over?"
            scene ep7_218
            with dissolve
            yt "However, what's mind-boggling in all of this is that he was able to kill someone, and a newborn child at that."
            yt "Our time together was short, but all those years were enough for me to get to know the real him."
            yt "And knowing him, there is no way in hell that he would do something like that..."
            yt "Hearing Hera's story, he might have turned out to be a coward. But he doesn't seem to have any grudge with them."
            yt "The last part was a sudden turn of events."
            yt "......"
            yt "Is there..."
            yt "......"
            yt "No, that's ridiculous considering what this old hag can do..."
            yt "Asking her would probably lead to denial either way."
            yt "Let's play this safe for now."
            scene ep7_219
            with dissolve
            mc "Hey, old hag."
            h "Don't call me that, or I'll break your neck."
            m "Yeah, do that and it will be yours next. Don't forget that we're here, old woman."
            mc "Why did you put a stop to all the bullying?"
            h "......"
            mc "Yeah, I know that you purposely stopped it. I have been wondering about that all this time."
            mc "Klara might have tried and asked, but she doesn't have any power to do it on her own considering what kind of person she was up against."
            mc "You could've made Aine follow me to the same college, but you didn't."
            mc "You could've even killed me if you wanted to end it, but there was nothing after high school."
            h "I don't have anything to say about that, just thank Klara. She did that all by herself."
            mc "... Are you telling me the truth?"
            h "*chuckles* Figure it out yourself, boy."
            scene ep7_218
            with dissolve
            yt "Yeah, I'm not buying it."
            yt "Fine, let's end it with this..."
            scene ep7_219
            with dissolve
            mc "Look, I don't care about what you did to me anymore, but what you've done to Emy and Aine is unconscionable."
            mc "Someone will have to make you pay for everything, and I will be the judge of that."
            scene ep7_220
            with dissolve
            h "{i}... *chuckles* Damn..."
    stop music fadeout 2

    scene ep7_221
    with dissolve
    mc "We're done talking here."
    mc "Now, where are Emy's papers?"
    play music 'audio/BinaryMotion.mp3' fadein 3
    scene ep7_222
    with dissolve
    h "Hnn..."
    scene ep7_223
    with dissolve
    h "Ahh..."
    h "You know, boy?"
    h "It's been a while..."
    play sound woosh2
    show ep7_224
    menu:
        "Let her slap you":
            $ heraslap = True
            play sound slap
            show ep7_225
            with hpunch
            pause
            show ep7_226
            a "You! You dare to hit my-"
            mc "I let her slap me on purpose, just let her be."
            scene ep7_227
            with dissolve
            mc "Well? Was that enough for a payment?"
            h "*chuckles* Sure."
        "Catch her hand":
            $ heraslap = False
            play sound punch
            show ep7_228
            with hpunch
            mc "Mn... Nope, not gonna happen."
            mc "I at least know how to protect myself, you know?"
            h "Nice catch."
            mc "Give it to us already."

    play sound drawer
    scene ep7_229
    with dissolve
    h "Don't worry, if her freedom is what you came here for, then you can have it."
    scene ep7_230
    with dissolve
    h "Here. I always keep hers separate from the others."
    h "These are her records in the Mafia. If you want to throw them out or burn them, I'll leave it to you."
    h "But remember, the change was official, so her name and everything in her birth certificate will remain the same."
    scene ep7_231
    with dissolve
    h "And you, boy... It's your responsibility to give this to her."
    mc "What's this?"
    h "The second letter that Daisy wrote for her before she died."
    mc "......"
    scene ep7_232
    with dissolve
    h "Also tell her to remember what I told her before."
    mc "That's it?"
    h "That's it. What do you want from me? I can't offer you my body, boy."
    mc "No, not that."
    mc "She was worried sick that you would kill us if we came here."
    h "She knows me well."
    mc "So she was being serious?!"
    h "Of course, if you came here alone, you'd already be dead now."
    scene ep7_233
    with dissolve
    h "But what can my guards do against those monsters?"
    h "Even if I had more, it wouldn't change anything."
    h "What you have here are a deranged assassin and an eccentric ex-mili-"
    show ep7_234
    m "Shut your trap or I'll gouge your eyeballs out, old woman. Do I look like a joke to you?"
    h "I'd like to see you try."
    scene ep7_235
    with dissolve
    m "It will be my pleasure."
    cl "Fang... control yourself."
    scene ep7_236
    with dissolve
    m "Tell that to your stupid ol' bloodlust, Owl!"
    cl "Yes, yes, okay. I don't want to fight you here."
    mc "Who... are you two?"
    scene ep7_237
    with dissolve
    h "So, is my sister your pawn now?"
    j "I guess you can say that, yes. I was a tad too late, but I must maintain his well-being."
    scene ep7_238
    with dissolve
    f "Wait, then you're my aunt?!"
    j "Mmm. I have been looking after you as well, my dear niece."
    f "So that's the reason why you're always so nice to me."
    j "Mhm."
    scene ep7_239
    with dissolve
    j "I will be taking her with me. Now that you're on your knees, I'm concerned about what will happen to her."
    scene ep7_240
    with dissolve
    h "Fine."
    h "But don't forget that you two are still my daughters..."
    h "...no matter what you do."
    scene ep7_241
    with dissolve
    j "Let's go."
    j "*whispers* Don't worry, just give her some time by herself."
    f "Mom?"
    scene ep7_242
    with dissolve
    h "Tch! Go!"
    scene ep7_243
    with dissolve
    mc "Let's go, Aine."
    a "Mhm..."
    stop music fadeout 3
    scene ep7_244
    with dissolve
    pause
    play sound phonevibrate
    "*phone vibrates*"
    stop sound
    scene ep7_245
    with dissolve
    h "What?"
    un "I heard everything."
    un "Hurry up, or I'm going to do it myself."
    "*click*"
    scene ep7_246
    with dissolve
    h "......"
    play sound woosh2
    show ep7_247
    with hpunch
    h "Raaahh!" #throws her phone

    scene black
    with dissolve
    with fade

    play music 'audio/TheFatFrog.mp3'
    scene ep7_248
    with dissolve
    mc "Uhm... Where are we heading now?"
    play sound woosh
    show ep7_249
    with hpunch
    mc "And why the hell are you undressing?!"
    m "Just be quiet for a moment, your questions will be answered soon."
    play sound cloth
    scene ep7_250
    with dissolve
    m "...I guess?"
    play sound cloth
    scene ep7_251
    with dissolve
    m "And I'm going on a patrol later before I go to the academy."
    mc "Huh... Patrol for what?"
    play sound cloth
    scene ep7_252
    with dissolve
    m "Your name is [mc], isn't it?"
    if gwenroute:
        mc "Yes? We already met before."
        m "Right..."
    else:
        mc "Yes?"
    scene ep7_253
    with dissolve
    m "From this moment on, I will be your servant."
    mc "Excuse me?! Who decided that?"
    scene ep7_254
    with dissolve
    m "I did."
    m "It was an order from Jess, but I had my doubts."
    m "However, after seeing you — a nobody, stand up to that woman, you proved that you are worthy enough for me to offer you my life."
    m "You also smell quite nice so that's a huge plus."
    m "Does that makes sense?"
    mc "No, not really."
    m "And if what Jess told me was right, then you have no idea how valuable your life is."
    mc "How... valuable my life is?"
    m "So you really have no idea, after all?"
    mc "Well... No?"
    m "That's the best decision Klara ever made, I think."
    m "You don't want to be out there telling everybody that you are that kind of person."
    mc "You are just making me a loooot more confused."
    mc "And again, just who are you? I don't know if I should actually trust you."
    m "You don't have to, but trust me when I say that you'll need me sooner or later. You can consider me your Swiss army knife."
    scene ep7_255
    with dissolve
    m "Like her, I'm also just a piece of trash salvaged by someone."
    scene ep7_256
    with dissolve
    m "I have nothing else to do with my life aside from getting a college degree and serving those who I consider worthy."
    m "Now, here I am. I will be in your care from now on... {b}Commander{/b}."
    scene ep7_257
    with dissolve
    m "*winks*"
    scene ep7_258
    with dissolve
    yt "Oof... I hope she doesn't mean what I think..."
    if ainepoint == 11:
        scene ep7_259
        with dissolve
        a "......"
        mc "......"
        scene ep7_260
        with dissolve
        a "What?"
        show ep7_261
        mc "Hey, you're the one staring at me like you're about to kill me."
        menu:
            "Are you jealous?":
                scene ep7_262
                with dissolve
                mc "Wait, are you jealous?!"
                $ ainepoint += 1
                $ renpy.notify(ainenotif)
                play sound woosh
                show ep7_263
                with hpunch
                a "!!!"
                a "W-w-why would I be jealous?!"
                mc "Hmmmm..."
                mc "Are you sure?"
                a "Yes! I am sure!"
                yt "I don't think so... You're just getting obvious at this point."
                scene ep7_264
                with dissolve
                mc "Anyway..."
                mc "Are you... angry?"
                a "About what?"
                mc "You know what I mean, Aine."
            "Are you angry?":
                scene ep7_264
                with dissolve
                mc "Are you... angry?"
                a "About what?"
                mc "You know what I mean, Aine."
        a "Of course, I don't feel so good, but it's not because of you."
        a "It's because of Jovian and how we got dragged into this. It's not your fault."
        mc "......"
        mc "I'm sorry about what he did..."
        mc "I didn't know..."
        a "You already made your point, you don't need to feel sorry about it."
        a "As long as you don't follow his footsteps, then there is no reason for me to resent you."
        mc "Well, if there is someone who would know my personality by now, that would be you."
        a "Right."
        scene ep7_265
        with dissolve
        mc "Hey..."
        a "Hm?"
        scene ep7_266
        with dissolve
        mc "*pats*"
        a "Mnhh..."
        mc "Thank you, and good job."
        scene ep7_267
        with dissolve
        cl "Ahhh... Youth."
        play sound woosh
        show ep7_268
        with hpunch
        a "......"
        mc "*whistle* *whistle*"
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play music cardriveinterior
    scene ep7_269
    with dissolve
    j "You don't have to go to work today, Lily. [mc] and Freya won't be able to come today either."
    l "Oh, did something happen?"
    j "Nothing important, just take time off for now, alright?"
    l "...Alright, if you say so, Miss Jess."
    stop music fadeout 2
    scene ep7_270
    with dissolve
    l "I wonder what actually happened..."
    play sound chair
    scene ep7_271
    with dissolve
    l "*removing her shoes* Well, it's not so bad, I guess. More study time for me."
    scene ep7_272
    with dissolve
    pause
    scene ep7_273
    with dissolve
    pause
    play music stadiumcrowd fadein 2
    scene ep7_274
    with flash
    l "......"
    scene ep7_275
    with dissolve
    an "Hey!"
    l "Yeah?"
    scene ep7_276
    with dissolve
    an "*tap* *tap*"
    an "Relax and breath."
    stop music fadeout 2
    scene ep7_273
    with flash
    pause
    scene ep7_277
    with dissolve
    l "{i}Well, I guess completing this shoe collection is nothing but an unreachable dream now."
    scene ep7_278
    with dissolve
    l "......"
    show ep7_279
    with dissolve
    pause 0.5
    play sound step
    scene ep7_278
    pause 0.1
    scene ep7_279
    with dissolve
    pause 0.5
    play sound step
    scene ep7_278
    pause 0.1
    scene ep7_279
    with dissolve
    pause 0.5
    play sound step
    scene ep7_278
    pause 0.1
    show ep7_280
    with hpunch
    l "Urk~!"
    l "{i}Why does it still hurt this bad even after so long?!"

    scene black
    with dissolve
    with fade

    play music cityalley
    play sound cardoorclose
    scene ep7_281
    with dissolve
    mc "......"
    mc "I know this place. Isn't it plagued by addicts and drug dealers?"
    f "Is it? It looks peaceful to me though."
    scene ep7_282
    with dissolve
    m "It {b}was{/b}."
    m "Until I came here."
    mc "Huh?"
    m "I am nothing if not the sheriff in these parts."
    scene ep7_283
    with dissolve
    m "So while you're here, I suggest you refrain from making any stupid moves and do just what I say."
    m "My turf, my rules."
    mc "What?! How can you be a sheriff while you're in college?!"
    scene ep7_284
    with dissolve
    j "It's not official, but the residents here like to call her that since she brought peace and order to this place."
    j "I don't need to tell you, but you'd better behave yourselves."
    scene ep7_285
    with dissolve
    mc "Huh... She's... weird..."
    j "She's a bit eccentric, but you'll get used to it, especially with the way she talks sometimes."
    scene ep7_286
    with dissolve
    mc "So you assigned her to be my servant? What for? And I don't get why..."
    mc "Not that I'm complaining though..."
    j "You'll need her. Use her to your heart's content in addition to what you have right now."
    mc "O...kay...?"
    scene ep7_283
    with dissolve
    m "Hurry up and get inside, I don't want you people standing there in broad daylight."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play sound closedoor
    scene ep7_287
    with dissolve
    j "Take her to her room, please, Fang. Thank you."
    scene ep7_288
    with dissolve
    m "Follow me."
    play music 'audio/Menacing.mp3' fadein 3
    scene ep7_289
    with dissolve
    a "We'll talk later, Frey."
    f "Alright, I'll call you?"
    a "Sure!"
    j "......"
    scene ep7_290
    with dissolve
    j "Let me introduce to you..."
    mc "Hm?"
    scene ep7_291
    with dissolve
    j "My people..."
    j "My team..."
    j "My friends..."
    j "And the members of our Clan..."
    j "{b}Your{/b} Clan."
    mc "Klara?"
    play sound cloth2
    show ep7_292
    with hpunch
    pause
    k "I'm sorry you have to go through this."
    k "No, I'm the one who put you into this situation."
    scene ep7_293
    with dissolve
    mc "You intentionally made them live with me... right? Tell me the truth."
    k "Yes, it wasn't Emma's plan, but mine."
    scene ep7_294
    with dissolve
    k "I fully understood that you'd finally moved on, but I needed you to learn something."
    k "Something that would allow you to open your eyes."
    k "But still, I think I do owe you an apology."
    mc "......"
    mc "And I did realize something..."
    mc "But honestly, I'm conflicted..."
    mc "A part of me wants to blame you for messing with my peace, but you are the reason I could meet Emy once more."
    mc "I couldn't have asked for a more perfect gift than that."
    mc "You gave me a chance to correct my mistakes."
    scene ep7_295
    with dissolve
    k "All you young ones' mistakes, not just yours."
    mc "Right..."
    mc "However, I won't thank you just yet. We'll have our conversation at a proper time."
    mc "I'm not going to let my emotions control my actions."
    scene ep7_296
    with dissolve
    k "Of course."
    scene ep7_297
    with dissolve
    mc "Right now, there is something I want to know."
    mc "Could you please enlighten me..."
    mc "Jess?"
    yt "Wait, when did that woman enter here? I did not see her after she left the car."
    scene ep7_298
    with dissolve
    j "Don't force yourself, [mc]. Just call me directly by my name, I have been telling you that since day one."
    mc "Right, since day one. Let's start from that."
    j "Before we start..."
    scene ep7_299
    with dissolve
    j "......"
    yt "Ah, shit. Here we go again."
    play sound bodykick
    show ep7_300
    with hpunch
    pause
    scene ep7_301
    with dissolve
    mc "As I said, I know how to protect myself."
    mc "I at least know how to dodge and block, you know? That was already the fifth time you did that since we met."
    j "I know, I just needed to reaffirm something."
    scene ep7_302
    with dissolve
    j "Well? Was that enough to prove it to you?"
    un "*chuckles* Yes. Go ahead."
    scene ep7_301
    with dissolve
    j "Sorry about that."
    mc "Hmph. I've gotten used to your games by now. Just cut to the chase—what do I need to know?"
    scene ep7_303
    with dissolve
    j "Like I told Klara..."
    j "She and Sky are descendants of Georgia—her blood runs through them. I swore to protect them the day I stood at Georgia's grave."
    j "But you, you're different."
    j "You weren't part of her bloodline, but you came from the same clan—cut from the same legacy, just not directly bound to it."
    j "Jovian found you first. And when I learned who you really were... I brought you into one of my networks."
    j "Not to give you a job, but to keep you under the radar until I could be sure the threat was gone."
    mc "But... why me? I've always thought I was just some average guy."
    j "As far as you know, sure."
    j "But Klara did one hell of a job keeping you hidden. She made sure you never knew just how close the fire really was."
    scene ep7_304
    with dissolve
    mc "You knew all this?"
    k "Yes, dear. Every word of it."
    k "Georgia and I were daughters of a man who wasn't just a killer, but was one of the most dangerous intelligence operatives our world has ever known."
    k "She followed in his footsteps. I chose another path."
    k "I walked away. Gave up everything—status, power, legacy—just for a chance at a normal life."
    k "And keeping you and Sky in the dark was the only way to protect that life."
    k "If I hadn't broken free when I did... I'd be dead. And you—none of this would exist for you now."
    scene ep7_305
    with dissolve
    mc "I see... Assassins, huh...?"
    mc "I couldn't imagine those kinds of people actually exist."
    scene ep7_306
    with dissolve
    j "We've got a few in this room who can confirm it to you."
    mc "What?! These people are your team, right? Then you're..."
    scene ep7_307
    with dissolve
    y "Oh boy... You are too innocent for this."
    scene ep7_308
    cl "Heeh~! Since when did you get so talkative?"
    scene ep7_309
    with dissolve
    y "Don't talk to me, bitch. I'm still watching you, just so you know."
    scene ep7_310
    cl "Urmph! God, I would love to hear that voice scream my name~!"
    y "Shut up!"
    scene ep7_311
    with dissolve
    li "Oh please... cut this out before it gets too noisy."
    scene ep7_312
    with dissolve
    ka "Like you are one to talk, Lisa."
    li "Huh?!"
    scene ep7_313
    with dissolve
    un "That's enough, let the new guy have his moment, will you?"
    j "And there's your answer."
    scene ep7_312
    with dissolve
    mc "Kana?! You're also one of them?!"
    play sound woosh
    show ep7_314
    ka "Uh-huh? I'm Georgia's daughter, you know?"
    scene ep7_304
    with dissolve
    mc "You knew about this too?!"
    k "Not until they arrived here and introduced themselves to me, no."
    k "I was shocked to learn about this too. I didn't have a single clue that Georgia's Clan was still thriving."
    scene ep7_315
    with dissolve
    k "Does that mean there is still something happening in this City?"
    j "......"
    scene ep7_316
    with dissolve
    j "Would you like to explain this yourself before you go?"
    un "Well, sure, why not?"
    scene ep7_317
    with dissolve
    mc "Whoa... What's with the eyepatch, buddy?"
    scene ep7_318
    with dissolve
    un "......"
    scene ep7_319
    with dissolve
    pause
    scene ep7_320
    with dissolve
    pause
    scene ep7_321
    with dissolve
    pause
    scene ep7_322
    with dissolve
    un "Nothing but a small price paid to untie a hitch."
    scene ep7_323
    with dissolve
    un "To answer your question..."
    un "A lot of blood was spilled, but everything was over two years ago."
    un "Right now, we are just trying to live the lives we all wanted."
    un "Or... well... to help Jess with her businesses."
    un "I haven't held a knife for a long time myself, unless it's in the kitchen, of course."
    scene ep7_324
    with dissolve
    un "As for you..."
    un "Jess might have told you about risks or whatnot, but all of those are in the past."
    image mcmcmctalk:
        "ep7_325.jpg"
        pause 3.0
        "ep7_326.jpg"
        pause .2
        repeat
    show mcmcmctalk
    with dissolve
    un "We simply took precautionary actions to keep you people safe, not to use or control you."
    un "You are still really a part of my Clan, after all."
    un "Now that you know everything there is to know about yourself, don't go and brag about it out there, will you?"
    un "Just a piece of advice from me."
    un "Also just to clarify, this is your story now..."
    un "You may be under my Clan, but we won't be moving just because you need us to."
    un "We're just here to let you know about your identity."
    un "That is selfish of me, I know. But this is to prevent you from getting drunk on your newfound power."
    un "I hope you understand what I'm trying to say."
    mc "I get it, I'm not that kind of person."
    un "Good, I'm glad to hear that."
    scene ep7_327
    with dissolve
    un "And I guess... he already has everything he needs?"
    j "I think so, but only he can say for sure."
    scene ep7_328
    with dissolve
    mc "......."
    scene ep7_329
    with dissolve
    mc "*chuckles* Yeah... I already have that."
    un "I like that smile."
    scene ep7_330
    with dissolve
    un "Now that we got our part settled, it is time for us to go."
    un "We'll leave you guys to discuss your personal matters."
    mc "Oh... Alright."
    un "Don't worry, this isn't the last time. We'll definitely see each other again at some point."
    mc "I'm looking forward to knowing more about you, then."
    un "I'll be glad to tell you my story when the time comes."
    un "And..."
    scene ep7_331
    with dissolve
    un "*whispers* Gotta get them all, don't you think?"
    scene ep7_332
    j "Pff..."
    scene ep7_333
    with dissolve
    mc "Oh man... What are you?"
    un "Ahaha!"
    scene ep7_334
    with dissolve
    un "Anyway, good luck."
    mc "Thanks."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    if ainepoint == 12:
        scene ep7_335
        with dissolve
        a "H-Hello, Miss Klara."
        a "I'm Aine, [mc]'s g-g-girl..."
        a "I mean..."
        a "N-no, never mind that."
        k "Ah, so you are that girl, hm?"
        k "I can see why [mc] was so into you."
        a "H-huh?"
    play music 'audio/UnderCanopies.mp3'
    scene ep7_336
    with dissolve
    j "......"
    mc "......"
    a "{i}The atmosphere suddenly got so tense... It's scary."
    k "Well? What happened back there? You've been silent since they left."
    scene ep7_337
    with dissolve
    mc "You have to know something about Jovian, Klara."
    k "My... Please don't bring up Jovian like that, dear. He's-"
    mc "No, he's responsible for us being in this situation."
    k "But he's dead, [mc]. How can he..."
    mc "He's not dead, he made us look like fools standing on his motherfucking grave."
    mc "He's still somewhere out there, hiding. Or at least, as far as we know."
    mc "There's no certainty if he's actually still alive."
    scene ep7_338
    with dissolve
    k "...!!!"
    mc "Listen..."

    scene black
    with dissolve
    with fade

    play sound chair
    scene ep7_339
    with dissolve
    k "......"
    k ".........."
    play sound chair
    scene ep7_340
    with dissolve
    yt "Yeah, that's the reaction I expected from her."
    yt "She has this inner tomboy that can come out and seem rude towards others when she is stressed or angry."
    yt "It's been a while..."
    yt "Honestly, I don't want to get on this side of her too much, it's dangerous."
    scene ep7_341
    with dissolve
    mc "So, does everything... make sense to you? Because it does to me."
    scene ep7_342
    with dissolve
    cl "She wasn't lying either, just to let you know."
    cl "Her emotions were real: there wasn't any hesitation with the way she told you the story."
    cl "I can vouch that she was telling the truth."
    scene ep7_343
    with dissolve
    k "...If that is true, then I don't understand why Hera would use our rivalry as an excuse to get to me."
    k "Why does she have to bring it up if she let us be in the first place?"
    scene ep7_344
    with dissolve
    mc "We can consider four reasons for that..."
    mc "One, to put up a strong face."
    mc "Two, she's lying."
    mc "Those two are bullshit, by the way."
    scene ep7_345
    with dissolve
    a "Language, [mc]!"
    scene ep7_346
    with dissolve
    j "You two make a good couple, you know that?"
    scene ep7_347
    with dissolve
    mc "Three... like her daughter here..."
    mc "She has become someone else's puppet..."
    mc "Or four... All of the above."
    a "Huh?!"
    a "There's no way she would-"
    mc "Calm down, it's just a hypothesis."
    mc "But did she ever tell you to do anything after we graduated from high school?"
    a "No, she didn't. That was the time when I slowly started to move out."
    mc "And she let you do it without saying anything?"
    scene ep7_348
    with dissolve
    h "Do whatever you want, I don't need you anymore."
    scene ep7_349
    with dissolve
    a "That's... what she said."
    scene ep7_350
    with dissolve
    mc "See?"
    mc "She could've made you follow me to the same college to start more shit if she really wanted to get to me."
    mc "Now the question is... Why?"
    mc "Why did she stop?"
    mc "She got bored or something?"
    mc "I don't think so..."
    scene ep7_351
    with dissolve
    j "I suggest you all give it a rest for now. Let it sink in and think about what you want to do next."
    j "Especially you, [mc]."
    scene ep7_352
    with dissolve
    k "Yes, I..."
    k "This is a bit too much for me... I don't even know what to say."
    k "I just can't believe that... Jovian..."
    mc "That's enough for now."
    mc "It is what it is, this is where we are now."
    mc "Do we make a move, or let it be? That's the question."
    scene ep7_353
    with dissolve
    j "Only you can answer that. The rest will be up to you from now on."
    j "I'm pretty much done with what I have to do, all that's left for me is to help Klara with her company."
    j "Whatever you want to do, stand up for it like a man."
    yt "......"
    yt "Emy..."
    scene ep7_354
    with dissolve
    mc "So you want me to stay here with you?"
    k "Oh, no, no. You still have something to do, don't you?"
    k "I'm coming home in a day or two, don't worry. Then... we can talk alone."
    k "But please, don't tell Sky anything about this for now."
    k "I already know how she will react, so I want to be the one to tell her."
    k "Just... give me some time to collect myself..."
    mc "Alright, if that's what you want."
    mc "We'll be waiting then."
    scene ep7_355
    with dissolve
    j "You might want to talk to Fang before you leave, maybe to clarify things?"
    mc "Oh yeah, I will do that."
    scene ep7_356
    with dissolve
    a "Since I have the time, can I talk to Freya too?"
    j "Sure, she's upstairs in the room to the right."
    a "Uhm, wait..."
    a "You're... my aunt, right?"
    j "Mhm."
    j "Your mother's only sister. My name is Jess, it's nice to see you all grown up now, Aine."
    j "Though our ages aren't that-"
    play sound cloth2
    show ep7_357
    with hpunch
    a "*hugs*"
    j "......"
    a "Thank you for looking after Freya."
    scene ep7_358
    with dissolve
    j "You're welcome."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep7_358a
    with dissolve
    pause
    play music hellfire
    scene ep7_359
    with flash
    un "*burning* Aaack!"
    un "Hurry, Fang! Hurry!"
    un "*burning* AAAAAACK!"
    scene ep7_360
    with dissolve
    m "I'm sorry..."
    play sound gunshot
    show black
    stop music
    pause 3.0

    play music 'audio/Folklore.mp3' fadein 2
    scene ep7_361
    with dissolve
    pause
    scene ep7_362
    with dissolve
    un "Aren't you too young to be in this war, kid? What are you even doing here?"
    scene ep7_363
    with dissolve
    m "Mnh... Nothing... I'm just here to take people's lives... A tool for war, that's what they call me."
    m "How about you? You must be a new recruit if you're asking me that. Everybody in the squadron knows me. Well... except you."
    un "Let's just say... I'm visiting my old hometown. I can't even remember how long I've been away."
    m "Hmm... Were you assigned overseas?"
    un "Haha. Well, I guess you can say that. Somewhere very far away from here, yes."
    scene ep7_364
    with dissolve
    m "I see..."
    m "What is it like outside? I mean... outside of this hell. It must be nice..."
    scene ep7_365
    with dissolve
    un "I can't say it's peaceful, but many are doing fine, thanks to you people."
    m "......"
    m "What's your name?"
    un "My real name?"
    m "Yes."
    scene ep7_366
    with dissolve
    un "Maya."
    ma "Maya Asmethana Cyraeni."
    m "That's a long name."
    ma "Is it?"
    m "Mhm."
    ma "Well, there's nothing I can do about that."
    scene ep7_367
    with dissolve
    ma "However... I can definitely do something for you."
    m "Hm?"
    ma "I can get you out of here."
    scene ep7_368
    with dissolve
    m "That's impossible, I've already tried so many times and ended up getting confined. No water nor food for several days, I can't do it anymore."
    ma "Then try me."
    ma "And in exchange for your freedom, promise me you'll find your true purpose in your life. You don't belong here, kid."
    scene ep7_369
    with dissolve
    m "A purpose... in my life?"
    m "I... don't know if I could ever do that..."
    stop music fadeout 2

    scene ep7_370
    with dissolve
    mc "Hey..."
    m "......"
    mc "Hey!"
    m "......"
    play music 'audio/TheFatFrog.mp3' fadein 2
    scene ep7_371
    with dissolve
    m "Oh..."
    m "'Sup. I was sleeping."
    mc "Who sleeps like that?"
    mc "Anyway, aren't you coming with me, since you're my servant and all?"
    image mmcsertup:
        "ep7_372.jpg"
        pause 3.0
        "ep7_373.jpg"
        pause .2
        repeat
    play sound chair
    show mmcsertup
    with dissolve
    m "Right..."
    m "But don't get it wrong, I am your servant, but I won't stick around you like what you think."
    m "I have a responsibility in this place and I can't leave just like that."
    scene ep7_374
    with dissolve
    m "Give me your phone."
    scene ep7_375
    with dissolve
    m "......"
    scene ep7_376
    with dissolve
    m "There's my number, call me when you need me."
    scene ep7_377
    with dissolve
    m "Although I will come by your house from time to time, show me around, okay?"
    m "I've only been in this city the last year or so, actually, so I still don't know a lot about it yet."
    mc "Oh... Alright."
    scene ep7_378
    with dissolve
    mc "I'm off th-"
    m "You want some?"
    scene ep7_379
    with dissolve
    mc "What's that?"
    m "A lollipop, of course."
    menu:
        "Take it":
            $ moonlollipop = True
            scene ep7_380
            with dissolve
            mc "Thanks."
            m "Mmmmm..."
            scene ep7_381
            with dissolve
            m "How does it taste?"
            mc "Hm, well... It's mint."
            m "Oh?"
            scene ep7_382
            pause
            scene ep7_383
            with dissolve
            m "Yeah, it's mint indeed."
            scene ep7_384
            with dissolve
            m "*winks*"
            yt "Man... She's dirty!"
            scene ep7_385
            with dissolve
            m "Let me walk you guys out."
            $ moonpoint += 1
            $ renpy.notify(moonnotif)
            yt "I'm speechless..."
            stop music fadeout 2

            scene black
            with Dissolve(2.0)
            label moonpause2:
            if _in_replay:
                $ name = persistent.gallery_name
            scene moonpause2
            with dissolve
            $ renpy.pause()
            $ renpy.end_replay()
            play sound 'audio/gamepause.mp3'
            show title at move_slide
            with flash
            $ renpy.notify(imageunlock)
            $ renpy.pause()
        "Reject it":
            $ moonlollipop = False
            mc "Nah... I'm good, thanks."
            m "Alright."
            scene ep7_385
            with dissolve
            m "Let me walk you guys out."
    stop music fadeout 2

    if ainepoint == 12:
        scene black
        with dissolve
        with fade

        play music 'audio/DifLove.mp3'
        scene ep7_663
        with dissolve
        a "......"
        mc "......"
        yt "She may look okay, but I know that she's deeply affected by what happened earlier."
        yt "Even though it was a huge shock to me, I have to compose myself no matter what to avoid making rash decisions."
        scene ep7_664
        with dissolve
        cl "......"
        mc "...Can you give us-"
        show ep7_665
        cl "Understood."
        cl "Call me when you are ready."
        yt "How the hell do you know what I'm about to tell you?!"
        scene ep7_666
        with dissolve
        mc "Come here for a moment. There's something I want to talk to you about for a bit."
        a "Hm?"
        scene ep7_667
        with dissolve
        yt "Let's start the conversation somewhere. I think asking about Freya will be a good start since I'm also concerned about her."
        scene ep7_668
        with dissolve
        mc "How's Freya, by the way?"
        scene ep7_669
        with dissolve
        a "Oh... well..."
        a "She's fine, I think."
        a "After all, she wanted to get out of there. Although for some reason, she was hesitant at the last moment."
        a "But I know that she will be fine."
        yt "I noticed that..."
        scene ep7_670
        with dissolve
        mc "Knowing her so far, I think so too. She's the type that can stand up on her own no matter what the obstacle or the challenge is."
        a "*giggles* Did you know that she got her personality from mother?"
        mc "Seriously?"
        a "Mhm."
        a "That might be one of the factors why she was hesitant to leave her. She's closer to her than I was."
        a "At least, when we were kids where everything was still fine."
        scene ep7_671
        with dissolve
        mc "...To be honest with you, she supported me when I initially planned to talk to your mother alone."
        mc "I was just waiting for the right time to come..."
        show ep7_672
        with hpunch
        a "Are you for real?!"
        scene ep7_673
        with dissolve
        mc "Yeah, I was dead serious about it. But that was just out of curiosity, everything was so different not so long ago..."
        mc "The moment I saw Emma's letters and our photo back then, something clicked and a lot of memories came rushing into my brain, then all the dots were connected."
        mc "I felt that I had to do something right away and did not even think about the risks."
        mc "Was it out of anger? I'm not sure..."
        mc "All I know is that I have to get something done somehow..."
        scene ep7_674
        with dissolve
        mc "Thank you for going along with me, Aine."
        mc "Thank you for standing up for me."
        scene ep7_675
        with dissolve
        mc "That slap was pretty darn cool, by the way. Haha!"
        scene ep7_676
        with dissolve
        a "......"
        a "{i}Urrhh... What am I getting so flustered for?"
        a "{i}Why am I like this towards him every single time? I don't understand!"
        yt "......"
        yt "Trying to hide your face, eh? I can still see you, you know?"
        scene ep7_677
        with dissolve
        mc "Hey... I've always wondered, did you ever wonder what would've happened if we had known each other under different circumstances?"
        mc "Let's say, none of this happened and both of us had lived a peaceful life..."
        mc "Would you have accepted me back then?"
        a "Huh?"
        a "W-where did that come from? Why are you asking that all of a sudden?"
        mc "I was serious with my feelings for you, you know that, right?"
        scene ep7_678
        with dissolve
        a "...!!!"
        mc "I still couldn't forget that one week before our final year in high school started, Aine."
        scene ep7_626a
        with flash
        pause
        scene ep7_626b
        with dissolve
        pause
        scene ep7_679
        with flash
        yt "Although, I may have treated her as an escape rope from my past... I guess we can call it even, huh?"
        yt "*chuckles* Fuck, now I'm certain I have an evil within me."
        a "......"
        scene ep7_680
        with dissolve
        a "I don't know... Maybe?"
        a "I haven't... given it a thought..."
        mc "......"
        a "But I'm certain that I did not want to hurt you."
        scene ep7_681
        with dissolve
        mc "...Then you don't have to answer now."
        mc "I know that it was Hera's orders, but I want you to recall that week and tell me what your heart says."
        a "......"
        scene ep7_682
        with dissolve
        yt "I want to know what you think of me, Aine."
        yt "Having found Emma again, I've already filled a big hole in my heart."
        scene ep7_683
        with dissolve
        yt "You're the other remnant from my past that keeps me wondering... So I want to hear it from your lips."
        yt "Though I won't stop trying to make you admit it."
        scene ep7_684
        with dissolve
        mc "Let's go home, for now. Emma is waiting for us to come back."
        a "Mhm."
        scene ep7_685
        with dissolve
        mc "Now where the hell is that cuckoo? She keeps on disappearing out of my sight."
        a "*whispers* Hey, don't call her that! You saw what she can do, right?!"
        stop music
        show ep7_686
        mc "Oops..."

    scene black
    with dissolve
    with fade

    play music cityalley
    scene ep7_386
    with dissolve
    mc "Thanks."
    cl "It's my pleasure."
    play sound cardriveaway
    scene ep7_387
    with dissolve
    mc "Jesus, I will never get used to seeing people bow down to me."
    mc "I've never gotten so much respect in my lifetime."
    a "Hm?"
    scene ep7_388
    with dissolve
    a "Welcome to my life then. That's what I saw every day when I was still with mother."
    mc "Sheeesh... You're bragging, aren't you?"
    a "*giggles* No... In fact, I hated it. I just wanted to be normal, that's all."
    scene ep7_389
    with dissolve
    a "And here, take this."
    scene ep7_390
    with dissolve
    a "I wanted to talk with Emma about it myself, but..."
    a "I think it should be you."
    a "I'm going to stay outside for a while."
    a "Go set her free, [mc]. Please tell her to not make the same mistake again."
    a "And that I'm fine on my own."
    mc "......"
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play music 'audio/TheBlame.mp3' fadein 2
    scene ep7_391
    with dissolve
    g "Hmm... Oddly enough, that fits you really well."
    scene ep7_392
    with dissolve
    mc "......"
    mc "What in the goddamn..."
    scene ep7_393
    with dissolve
    shu "[mc], buddy...? Help...?"
    mc "Pfff..."
    mc "AHAHAHAHAHA!"
    mc "What the fuck, Shu! That looks good on you, man!"
    play sound woosh
    show ep7_394
    shu "No, it doesn't!"
    scene ep7_395
    with dissolve
    g "You're back, where's Aine?"
    mc "She's on the veranda."
    mc "You... might wanna talk to her. She doesn't feel so good."
    play sound woosh
    show ep7_396
    g "Come, let's slap someone back to her senses."
    shu "Nooooo~!"
    if gwenroute:
        scene ep7_397
        with dissolve
        g "I did my best to temporarily get her mind off of you two."
        g "I understand what's going on..."
        g "Whatever it is, I'll be waiting for an answer."
        mc "Of course."
    play sound woosh
    show ep7_398
    shu "[mc]~!!" #being dragged by Gwen
    mc "May God bless your soul."
    stop music fadeout 4
    scene ep7_399
    with dissolve
    mc "Well? Don't just stand there..." #refering to Emma
    mc "Come here, I'm going to show you something."

    scene black
    with dissolve
    with fadeq

    play music 'audio/RhapsodicSprout.mp3' fadein 2
    scene ep7_400
    with dissolve
    mc "Before anything else, mind explaining your side to me?"
    e "Even if I do, it won't change anything. You already know that I'm-"
    mc "Shhh..."
    mc "Go on, tell me. There's nothing to hide now, trust me."
    scene ep7_401
    with dissolve
    e "......"

    scene black
    with dissolve
    with fadeq

    scene ep7_402
    with dissolve
    e "I wanted to see you, I wanted to know how you were doing."
    e "However, I needed a reason to do that."
    mc "So you used Aine's issue as an excuse to come here?"
    e "Mhm..."
    image emamcconfess:
        "ep7_403.jpg"
        pause 3.0
        "ep7_404.jpg"
        pause .2
        repeat
    show emamcconfess
    with dissolve
    e "Gwen was right..."
    e "I lost myself a lot of times and made stupid decisions."
    mc "Well, what else could you have done?"
    e "I came here not just for Aine, but for my own selfish wishes as well."
    e "Either way, we wouldn't have been able to if it wasn't for Miss Klara. She was the one who permitted us to come here."
    mc "She knew about you and me?"
    e "No, but she figured something out when I was constantly checking on you back then."
    e "Although she has no idea what we really are to each other."
    yt "Yeah, this is what she meant by 'something that would open my eyes'..."
    yt "You never stop educating me even at this age, goddamn it..."
    image emamcconfess2:
        "ep7_405.jpg"
        pause 3.0
        "ep7_406.jpg"
        pause .2
        repeat
    show emamcconfess2
    with dissolve
    e "I wouldn't have become a detective if I knew that I was so easy to read."
    mc "Hey, your job is different from this, don't compare it to your personal problems."
    e "But in the end, I couldn't do anything..."
    mc "That old woman threatened you that she would kill us if you did, am I right?"
    e "Mhm..."
    e "I was in a corner, I couldn't make a move. I was afraid that I would lose you two if I did."
    scene ep7_407
    with dissolve
    mc "I see..."
    mc "Well, hiding the truth from me was not the best, but I guess you did the right thing by hiding it as much as you could."
    mc "Because I would've stormed in there all by myself if I knew about it sooner."
    show ep7_408
    with hpunch
    e "I knew it!"
    e "And you still did, you stupid! I was telling you not to!"
    scene ep7_409
    with dissolve
    e "Hrrmmnnnn!"
    yt "Cute..."
    mc "What? I'm alive, aren't I?"
    image emamcconfess3:
        "ep7_410.jpg"
        pause 3.0
        "ep7_411.jpg"
        pause .2
        repeat
    show emamcconfess3
    with dissolve
    e "But... how? What did you do?"
    mc "Well, that's thanks to Jess."
    e "Jess?"
    mc "*sighs* Yeah... It's a long explanation but it was because of her that we could make it out alive."
    mc "Let's just say that she was watching over us this whole time, so I kind of used her."
    e "Huh?"
    mc "Ah, it doesn't matter how as long as we're alive."
    scene ep7_412
    with dissolve
    mc "Anyway, these are your records in the Mafia."
    e "H...How did you get that...?"
    play sound woosh2
    show ep7_413
    pause
    scene ep7_414
    with dissolve
    pause
    play sound firewood fadein 2 loop
    scene ep7_415
    with dissolve
    pause
    scene ep7_416
    with dissolve
    e "......"
    mc "You're free, Emy."
    mc "But your new name is actually official, so I guess calling you Emma now is not that bad either."
    mc "One last thing..."
    mc "Please don't make the same mistake again. From now on, be honest with me, okay?"
    scene ep7_417
    with dissolve
    pause
    if emmapoint == 5:
        play sound2 cloth2
        show ep7_424
        mc "......"
        e "Mnnhh~"
        mc "........."
        yt "Shit... My heart is pounding so fast..."
        yt "I'm about to cry for fuck's sake..."
        yt "Not until just now did I realize that... I absolutely fucking missed her..."
        menu:
            with Dissolve(1.0)
            "Take her to your room":
                $ emmaroute = True
                stop sound fadeout 2
                scene ep7_425
                with dissolve
                pause

                scene black
                with dissolve
                with fadeq

                label emmaxmcfirst:
                if _in_replay:
                    $ name = persistent.gallery_name
                play sound closedoor
                scene ep7_426
                with dissolve
                e "Mnnhhhh~"
                yt "Now that she's here with me... there is no way..."
                yt "...I'm going to lose her once more..."
                scene ep7_427
                with dissolve
                e "[mc]?"
                mc "Yeah?"
                e "If I can live my life however I want from now on... then..."
                e "I..."
                e "I want to spend the rest of it with you..."
                scene ep7_428
                with dissolve
                mc "!!!"
                scene ep7_429
                with dissolve
                mc "Damn it..."
                scene ep7_430
                with dissolve
                e "No, no... Don't cry, please." #wipes mc tears
                e "Now that it's over, thanks to you..."
                e "I'm all yours..."
                e "I wanted to be with you without any consequences, and you've granted me that wish."
                e "I can never ask for more, [mc]."
                scene ep7_431
                with dissolve
                mc "*chuckles* You making me stop crying has always been effective."
                e "*giggles* Go on, please, do me a favor."
                play sound cloth
                scene ep7_432
                with dissolve
                mc "Let's move these out of the way."
                stop music fadeout 2

                scene black
                with dissolve
                with fadeq

                play music 'audio/OneNight.mp3'
                scene ep7_433
                with Dissolve(2.0)
                e "Uhm..."
                e "This is a bit embarrassing..."
                play sound cloth
                mc "*chuckles* I'll make it even."
                scene ep7_434
                with dissolve
                e "Ohh... That's..."
                scene ep7_435
                with dissolve
                e "*deeply exhales*"
                scene ep7_436
                with Dissolve(2.0)
                pause
                mc "Wow, Emma, you're so... beautiful."
                scene ep7_437
                with dissolve
                e "You already saw me like this, you know?"
                mc "That's true, but it's different when it is the real you, especially when you want to show me all of you."
                scene ep7_438
                with dissolve
                e "Come!"
                e "We've let each other wait long enough..."
                mc "Well then..."
                show ep7_439
                with hpunch
                mc "Hup!"
                show ep7_440
                e "Ohhh!"
                scene ep7_441
                with dissolve
                e "[mc], your thing is rubbing against my-"
                show emma1
                with dissolve
                pause
                mc "Relax and let go. I'll show you what you've been missing all this time."
                e "This sensation is making me... lose my mind..."
                yt "She's getting wet fast. We've both been waiting for this to happen, huh?"
                yt "I can tell that she wants this. If so, then I won't hold back."
                pause
                scene ep7_442
                with dissolve
                e "*licks*"
                show emma2
                with dissolve
                pause
                mc "Yeah, that's it—don't hold it back, Emma. Let it out."
                e "*licks*"
                yt "*chuckles* I didn't know she could be this horny."
                yt "I thought that I would have to do everything on my own, but she's really into it."
                yt "Let's give it to her then."
                pause
                play sound woodhit
                show ep7_443
                with hpunch
                e "Oh!"
                e "Hey, we could damage your computer!"
                mc "If we do, then I don't care, it's worth it."
                scene ep7_444
                with dissolve
                e "W-what are you going to do now?"
                mc "Let me just..."
                scene ep7_445
                with dissolve
                mc "There."
                show emma3
                with dissolve
                pause
                mc "Is that better?"
                e "Uhm... It's..."
                e "Ohhh~! [mc]!"
                mc "I'll take that as a yes."
                yt "She's ready at this point, but let's see how far I can take her."
                pause
                show emma4
                with dissolve
                pause
                e "Uhm, [mc]?"
                mc "Yes?"
                e "I'm..."
                e "I..."
                e "Mnnnhh~!"
                menu:
                    "Tell her to say it":
                        $ lewdemma = True
                        mc "Say it. I told you, don't hold back."
                        e "I'm... I'm..."
                        e "I'm cumming!"
                        mc "And where did you learn that word?"
                        e "I... when I was touching myself."
                        mc "Hmm... While thinking of me?"
                        e "Yes!"
                        mc "You naughty little... At least you're all honest now."
                        mc "Then cum for me, Emma."
                        show ep7_446
                        with hpunch
                        e "HNNGGG~!!"
                        play sound chair
                        show ep7_447
                        with hpunch
                        mc "Come here."
                        e "Wait, wait, I'm still..."
                        scene ep7_448
                        with dissolve
                        mc "*smooch*"
                        show ep7_449
                        with hpunch
                        e "OHH~!"
                        show emma5
                        with dissolve
                        pause
                        mc "Damn, you're dripping wet. You really did enjoy that, huh?"
                        e "Yes, yes I did!"
                        e "Emy has been such a bad girl, please punish her little pussy like what she deserves!"
                        mc "Fucking hell, Emma. So you swing like that?"
                        mc "Damn, girl! Alright!"
                        e "N-no! I don't know what I'm..."
                        yt "Well, shit. So she's into that kind of stuff, huh?"
                        yt "That's such a surprise in contrast to her personality."
                        yt "She submits quite easily too."
                        pause
                        show ep7_450
                        with hpunch
                        e "MNNNNHHH~!!"
                        show ep7_451
                        with hpunch
                        "*thud*"
                        e "*huff* *huff*"
                    "Don't force her":
                        $ lewdemma = False
                        e "I'm... I'm..."
                        show ep7_446
                        with hpunch
                        e "HNNGGG~!!"
                        play sound chair
                        show ep7_447
                        with hpunch
                        mc "Come here."
                        e "Wait, wait, I'm still..."
                        scene ep7_448
                        with dissolve
                        mc "*smooch*"
                        show ep7_449
                        with hpunch
                        e "OHH~!"
                        show emma5
                        with dissolve
                        pause
                        mc "Damn, you're dripping wet. You really did enjoy that, huh?"
                        e "N-no! I don't know what I'm-"
                        pause
                        show ep7_450
                        with hpunch
                        e "MNNNNHHH~!!"
                        show ep7_451
                        "*thud*"
                        e "*huff* *huff*"
                play sound chair
                scene ep7_452
                with dissolve
                mc "You already came twice, but we haven't even started yet."
                scene ep7_453
                with dissolve
                e "Let's go on, [mc]..."
                e "I think I'm ready."
                mc "...I don't know what it is with you, Em. But you saying my name has become the most satisfying thing to hear."
                scene ep7_452
                with dissolve
                e "*blushes* D...Don't call me that. It's a bit awkward when you use my nickname..."
                mc "You better get used to it then."
                e "I'll... try."
                mc "Do you trust me?"
                scene ep7_454
                with dissolve
                e "I'm giving you everything, [mc]."
                e "Trust is an understatement at this point."
                mc "*about to cry*"
                scene ep7_455
                with dissolve
                e "Hmmnn... I told you, don't cry."
                mc "God... I love you, Em."
                scene ep7_456
                with dissolve
                e "I love you too, [mc]."
                e "Take me, let's be happy like how we were in those times..."
                scene ep7_457
                with dissolve
                mc "Yeah, I think you are ready. You're still soaking after all that talk."
                if lewdemma:
                    e "*giggles* Sorry, but... I'm not as innocent as you think I am."
                else:
                    e "Well..."
                scene ep7_458
                with dissolve
                mc "I'm going to slowly put it in, Em. Tell me if it hurts."
                scene ep7_459
                with dissolve
                e "Ahhh~!"
                mc "I can already feel you, one more push and I'll-"
                scene ep7_460
                with dissolve
                e "Then take it, it's all yours, [mc]."
                scene ep7_461
                with dissolve
                e "MNNNHHHH~!"
                show emma6
                with dissolve
                e "Haah~! Ahhh~! Ahhhh~!"
                mc "How's that for you?"
                if lewdemma:
                    e "More, [mc]! Punish little Emy's pussy more!"
                    mc "Alright, if that's what you want."
                    show emma7
                    with dissolve
                    mc "Then cum your brains out, Em!"
                    e "Yes, keep talking to me like that!"
                    pause
                    e "Oh, [mc]~!"
                    e "I'm cumming again!"
                    pause
                    show ep7_462
                    with hpunch
                    e "HAAAAHH~!"
                    show ep7_463
                    e "*huff* *huff*"
                    play sound chair
                    show ep7_464
                    with hpunch
                    e "Oh!"
                    mc "Move your hips a little bit for me."
                    mc "This time, please yourself to your heart's content."
                    show emma8
                    with dissolve
                    pause
                    e "Oh my god..."
                    e "[mc]! [mc]~!"
                    mc "Let me guess..."
                    mc "You've played with your tits before, right?"
                    e "Yes, a lot, yes!"
                    mc "Tell me more about it."
                    e "I... I was thinking..."
                    e "How would it feel like if [mc] would touch them!"
                    e "I wondered if it would feel good!"
                    e "I wanted [mc] to punish and harass me so bad!"
                    mc "Yeah, you are definitely a bad girl, Em."
                    show emma9
                    with dissolve
                    e "Hnng~!"
                    mc "That's it, faster!"
                else:
                    e "It... It feels so satisfying!"
                    mc "Yeah, just relax and enjoy it. This is your first time, after all. Let me handle everything."
                    show emma7
                    with dissolve
                    pause
                    e "Oh, [mc]~!"
                    e "I'm about to..."
                    pause
                    show ep7_462
                    with hpunch
                    e "HAAAAHH~!"
                    show ep7_463
                    e "*huff* *huff*"
                    show ep7_464
                    e "Oh!"
                    mc "Move your hips a little bit for me."
                    mc "This time, let's do it together."
                    show emma8
                    with dissolve
                    pause
                    e "Oh my god..."
                    e "[mc]! [mc]~!"
                    pause
                    show emma9
                    with dissolve

                e "[mc], I'm almost..."
                mc "I'm gonna go too, Em."
                pause
                menu:
                    "Cum outside":
                        e "[mc]! [mc]~! [mc]~!"
                        show ep7_465
                        with hpunch
                        e "AAHHHHH~!"
                        show ep7_466
                        with hpunch
                        mc "Urrghh!"
                        play sound chair
                        show ep7_469
                        with hpunch
                        "*thud*"
                        e "*huff* *huff*"
                    "Cum inside":
                        e "[mc]! [mc]~! [mc]~!"
                        scene ep7_465
                        with hpunch
                        e "AAHHHHH~!"
                        show ep7_467
                        with hpunch
                        mc "Urrghh!"
                        scene ep7_468
                        with dissolve
                        pause
                        play sound chair
                        show ep7_469
                        with hpunch
                        "*thud*"
                        e "*huff* *huff*"
                stop music fadeout 2
                $ renpy.end_replay()

                scene black
                with dissolve
                with fadeq

                play music 'audio/RhapsodicSprout.mp3' fadein 2
                with dissolve
                scene ep7_470
                with dissolve
                mc "......"
                e "Hm?"
                e "What's on your mind?"
                scene ep7_471
                with dissolve
                mc "...I'm thinking about you."
                mc "No, about us..."
                e "I'm sorry... I put too much on your shoulders..."
                e "I had no one else to go to but you."
                mc "That's not it. Things have become more than just us two, Em."
                e "What do you mean?"
                scene ep7_472
                with dissolve
                yt "I'm actually not sure which path I should take from here."
                yt "I want to pursue the promise I made to her."
                yt "Yet on the other hand, I don't want to leave everything."
                yt "If I choose her, I'm going to take her away from here and abandon everyone."
                yt "But I'm already tied to something..."
                if gwenroute:
                    yt "Gwen..."
                if skyroute:
                    yt "Sky..."
                if (gwenroute & skyroute):
                    yt "I can't just abandon those two..."
                yt "Shit, what should I choose here?"
                label emmarevert:
                menu:
                    with dissolve
                    "Pursue your promise":
                        $ emmasolo = True
                        jump emmasoloending
                    "Stand for the current situation":
                        $ emmasolo = False
                        scene ep7_473
                        with dissolve
                        mc "Look, Em..."
                        mc "I know I made a promise to you, and I really want to keep it now that I have an opportunity and I don't care what the circumstances are."
                        mc "I want to run away with you. Runaway from all this."
                        mc "But..."
                        mc "There is something that I must do now."
                        mc "I'm going to find Jovian."
                        image emamcaftsexconf:
                            "ep7_474.jpg"
                            pause 3.0
                            "ep7_475.jpg"
                            pause .2
                            repeat
                        show emamcaftsexconf
                        with dissolve
                        mc "He's... the one who started this mess."
                        mc "Everything that happened in the past was because of him."
                        mc "Me, Klara, Aine, Hera, and you became victims of his actions."
                        e "Huh? W-what did he do?"
                        mc "He killed Aine's father and..."
                        mc "Agh!"
                        mc "Her little brother."
                        show ep7_476
                        with hpunch
                        e "*gasps*!"
                        e "So that was why Hera..."
                        mc "Yes, she changed because of that."
                        e "I... never knew about it."
                        scene ep7_477
                        with dissolve
                        mc "Well, because the old woman decided to keep it to herself."
                        mc "That's also the reason she tormented me."
                        mc "Half of it was for revenge, and the rest was in hopes of bringing Jovian out of hiding."
                        e "......"
                        mc "That's why I must find him and make him finish what he started."
                        scene ep7_478
                        with dissolve
                        e "It's going to be a challenge, [mc]. You don't have any clue on his whereabouts, right?"
                        mc "I don't, but that's not going to stop me from doing it."
                        if (gwenroute & skyroute):
                            scene ep7_479
                            with dissolve
                            mc "Also, Em..."
                            mc "I want you to listen..."
                            mc "I don't want to lie to you, so I'm going to confess."
                            e "A confession?"
                            mc "Mhm."
                            mc "......"
                            mc "Gwen and I are already dating."
                            show ep7_480
                            with Dissolve(2.0)
                            e "!!!"
                            e "Just when did you two..."
                            mc "Well, something already happened to us even before you came here — during high school to be exact."
                            mc "And when you all came here, it triggered our feelings for each other once more."
                            mc "Which... I never expected to happen."
                            mc "Then, there's Sky..."
                            scene ep7_481
                            with dissolve
                            e "Huh?"
                            mc "It's a very long story to tell."
                            scene ep7_482
                            with dissolve
                            mc "It's weird, I know... But a lot happened to both of us after high school ended."
                            mc "And now, you're here as well. I can't choose, Em."
                            mc "All of you have been an indispensable part of my life already. Leaving anyone aside will be devastating for me."
                            scene ep7_483
                            with dissolve
                            e "......"
                            e "It..."
                            e "It hurts, [mc]..."
                            mc "Emma..."
                            scene ep7_484
                            with dissolve
                            e "*sniffs*"
                            yt "A sniff..."
                            scene ep7_485
                            with dissolve
                            e "*deeply exhales*"
                            yt "She exhaled?"
                            scene ep7_486
                            with dissolve
                            e "But, no..."
                            e "It was my choice to come here not knowing what was going to hit me."
                            e "I'm going to stand with it."
                            e "If this is what it takes for me to be with you, then I'm going to accept that fact."
                            e "Even if it hurts..."
                            e "Just promise that you won't leave me again."
                            scene ep7_487
                            with dissolve
                            pause
                            play sound chair
                            show ep7_488
                            with hpunch
                            mc "Em!"
                            e "Ow, ow, ow!"
                            scene ep7_489
                            with dissolve
                            e "H-Hey..."
                            e "Y-You're... suffocating me..."
                            play sound gasp_female2
                            show ep7_490
                            e "*gasping for air*"
                            mc "Oh, sorry!"
                            play sound cough_female
                            e "*cough* *cough*"
                            play sound cloth
                            scene ep7_491
                            with dissolve
                            mc "I wonder though..."
                            mc "Aren't these huge jugs of yours suffocating you in the first place?"
                            stop music
                            play sound punch
                            show ep7_492
                            with hpunch
                            e "Stupid~!" #hits him in the head
                            mc "Ow!"
                        elif gwenroute:
                            scene ep7_479
                            with dissolve
                            mc "Also, Em..."
                            mc "I want you to listen..."
                            mc "I don't want to lie to you, so I'm going to confess."
                            e "A confession?"
                            mc "Mhm."
                            mc "......"
                            mc "Gwen and I are already dating."
                            scene ep7_480
                            with Dissolve(2.0)
                            e "!!!"
                            e "Just when did you two..."
                            mc "Well, something already happened to us even before you came here — during high school to be exact."
                            mc "And when you all came here, it triggered our feelings for each other once more."
                            mc "Which... I never expected to happen."
                            scene ep7_482
                            with dissolve
                            mc "And now, you're here as well. I can't choose, Em."
                            mc "Both of you have become a crucial part of my life already. Leaving anyone aside will be devastating for me."
                            scene ep7_483
                            with dissolve
                            e "......"
                            e "It..."
                            e "It hurts, [mc]..."
                            mc "Emma..."
                            scene ep7_484
                            with dissolve
                            e "*sniffs*"
                            yt "A sniff..."
                            scene ep7_485
                            with dissolve
                            e "*deeply exhales*"
                            yt "She exhaled?"
                            scene ep7_486
                            with dissolve
                            e "No..."
                            e "It was my choice to come here not knowing what was going to hit me."
                            e "I'm going to stand with it."
                            e "If this is what it takes for me to be with you, then I'm going to accept that fact."
                            e "Even if it hurts..."
                            scene ep7_487
                            with dissolve
                            pause
                            play sound chair
                            show ep7_488
                            with hpunch
                            mc "Em!"
                            e "Ow, ow, ow!"
                            scene ep7_489
                            with dissolve
                            e "H-Hey..."
                            e "Y-You're... suffocating me..."
                            play sound gasp_female2
                            show ep7_490
                            e "*gasping for air*"
                            mc "Oh, sorry!"
                            play sound cough_female
                            e "*cough* *cough*"
                            scene ep7_491
                            with dissolve
                            mc "I wonder though..."
                            mc "Aren't these huge jugs of yours suffocating you in the first place?"
                            stop music
                            play sound punch
                            show ep7_492
                            with hpunch
                            e "Stupid~!"
                            mc "Ow!"
                        elif skyroute:
                            scene ep7_479
                            with dissolve
                            mc "Also, Em..."
                            mc "I want you to listen..."
                            mc "I don't want to lie to you, so I'm going to confess."
                            e "A confession?"
                            mc "Mhm."
                            mc "Sky and I have something going on..."
                            scene ep7_480
                            with dissolve
                            e "H-Huh?"
                            e "But aren't you two..."
                            mc "It's a very long story to tell."
                            scene ep7_482
                            with dissolve
                            mc "It's weird, I know... But a lot happened to us both after high school ended."
                            mc "And now, you're here as well. I can't choose, Em."
                            mc "Both of you have become a crucial part of my life already. Leaving anyone aside will be devastating for me."
                            scene ep7_483
                            with dissolve
                            e "......"
                            e "It..."
                            e "It hurts, [mc]..."
                            mc "Emma..."
                            scene ep7_484
                            with dissolve
                            e "*sniffs*"
                            yt "A sniff..."
                            scene ep7_485
                            with dissolve
                            e "*deeply exhales*"
                            yt "She exhaled?"
                            scene ep7_486
                            with dissolve
                            e "No..."
                            e "It was my choice to come here not knowing what was going to hit me."
                            e "I'm going to stand with that."
                            e "If this is what it takes for me to be with you, then I'm going to accept that fact."
                            e "Even if it hurts..."
                            scene ep7_487
                            with dissolve
                            pause
                            show ep7_488
                            with hpunch
                            mc "Em!"
                            e "Ow, ow, ow!"
                            scene ep7_489
                            with dissolve
                            e "H-Hey..."
                            e "Y-You're... suffocating me..."
                            play sound gasp_female2
                            show ep7_490
                            e "*gasping for air*"
                            mc "Oh, sorry!"
                            play sound cough_female
                            e "*cough* *cough*"
                            play sound cloth
                            scene ep7_491
                            with dissolve
                            mc "I wonder though..."
                            mc "Aren't these huge jugs of yours suffocating you in the first place?"
                            stop music
                            play sound punch
                            show ep7_492
                            with hpunch
                            e "Stupid~!"
                            mc "Ow!"
                        else:
                            scene ep7_479
                            with dissolve
                            mc "I hope you understand me, Em."
                            scene ep7_481
                            with dissolve
                            e "No, I understand, [mc]. If that's what you want to do, then I have no say in it."
                            e "It was my choice to come here not knowing what was going to hit me."
                            e "I'm going to stand with that."
                            mc "Thanks for understanding, Em."
                            stop music fadeout 2

            "End it here":
                $ emmaroute = False
                yt "But... this is more than just us now..."
                yt "I can't let my feelings decide what I should do..."
                mc "Uhm... Emma, I..."
                scene ep7_419
                with dissolve
                e "No, I know..."
                e "I just wanted to say thank you..."
                e "Thank you, [mc]..."
                mc "No... Don't cry again, you've already cried a lot of tears since we were kids."
                mc "You're free now. Be happy and live your life however you want to, you got me?"
                scene ep7_420
                with dissolve
                e "Mhm!"
                mc "Good."
                scene ep7_421
                with dissolve
                mc "And here..."
                mc "Hera wanted you to have this."
                e "It... looks familiar..."
                mc "Well, she told me that it's from your mom, so..."
                e "Really?"
                mc "Yeah."
                scene ep7_422
                with dissolve
                mc "She also said that you should remember what she told you before."
                e "......"
                mc "You might also want to check on Aine."
                mc "I just... want to go to my room right now and get my mind as clear as I can..."
                scene ep7_423
                with dissolve
                e "I understand."
    else:
        $ emmaroute = False
        show ep7_418
        e "*hugs*"
        e "Thank you..."
        e "Thank you!"
        mc "No... Don't cry again, you've already cried a lot of tears since we were kids."
        scene ep7_419
        with dissolve
        mc "You're free now. Be happy and live your life however you want to, you got me?"
        e "*sniffs*"
        scene ep7_420
        with dissolve
        e "Mhm!"
        mc "Good."
        scene ep7_421
        with dissolve
        mc "And here..."
        mc "Hera wanted you to have this."
        e "It... looks familiar..."
        mc "Well, she told me that it's from your mom, so..."
        e "Really?"
        mc "Yeah."
        scene ep7_422
        with dissolve
        mc "She also said that you should remember what she told you before."
        e "......"
        mc "You might also want to check on Aine."
        mc "I just... want to go to my room right now and get my mind as clear as I can..."
        scene ep7_423
        with dissolve
        e "I understand."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "At night..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/SlowEvening.mp3'
    scene ep7_493
    with dissolve
    yt "*sighs*"
    yt "Now that's one thing off of my chest."
    yt "Honestly, I couldn't have asked for a better outcome than that."
    yt "And who would've thought that I'm from some kind of a secret organization all around the city?"
    yt "Well, probably a handful of people, but still..."
    yt "I don't know if it will matter in the end. I'm still just an average person in my eyes."
    yt "Learning about my identity was nothing but a momentary shock."
    scene ep7_494
    with dissolve
    yt "Meeting those people was still cool as fuck though..."
    yt "Man... I can only imagine!"
    scene ep7_495
    with dissolve
    yt "But enough thinking of my shit."
    yt "I may have closed one major case, but why do I still feel so uneasy about this?"
    yt "The way Hera acted earlier really bugs me for some reason."
    yt "I can say that her emotion was definitely not faked, and I could somehow feel her pain when she was telling her story."
    yt "But why do I feel that she was trying to tell me something as if she was passing on an encoded message?"
    yt "There was barely any resistance from her at all."
    yt "She like... just sat down in a corner and told us her side, nothing more."
    yt "I get that I brought some backup with me, but still... Isn't she the leader of a Mafia?"
    yt "What the hell are you trying to tell me, old woman?"
    scene ep7_496
    with dissolve
    yt "......"
    yt ".........."
    yt "I want to hear about Emma's plan once more..."
    if (emmaroute & gwenskyharem & skyroute):
        scene ep7_497
        with dissolve
        yt "But before that..."
        yt "I can't leave her hanging for too long."
        yt "If there's someone whose reaction I'm genuinely afraid of, it's gonna be her."
        yt "But I've pretty much dug my own grave. Whatever the outcome is, I still have to tell her about it."

        scene black
        with dissolve
        with fadeq

        scene ep7_498
        play sound doorknock
        with dissolve
        mc "*knocks*"
        g "Come in!"
        scene ep7_499
        play sound closedoor
        with dissolve
        play sound chairdrag
        mc "Hey, Gwen..."
        g "*tap* *tap*"
        yt "So she's really expecting this, huh?"
        yt "Well, what am I thinking? She is the one that I'm actually dating."
        play sound chair
        scene ep7_500
        with dissolve
        g "Listen, from now on if we have something we want to talk about — especially if it's something between us two, let's do it this way."
        g "No talks over the phone nor messages, you got me?"
        g "It's not for us to fight about any topic, but rather for us to create a mutual understanding that calls or messages can not."
        mc "Mhm, I understand, Gwen."
        yt "Damn..."
        yt "We're still in the midst of dating, yet she already feels like my wife or something."
        yt "But that just shows how much she wants to stabilize and strengthen our relationship."
        yt "Gwen definitely knows what she's doing."
        scene ep7_501
        with dissolve
        g "So..."
        g "You got something to tell me, right?"
        mc "Mhm."
        g "Go on, I'm all ears."
        scene ep7_502
        with dissolve
        mc "We got ourselves finally settled..."
        g "And...?"
        mc "I couldn't lie, so I told her that we were already dating."
        mc "But even if it will hurt her, she's ready to accept that fact just to be with me."
        mc "Now I know you are going to-"
        stop music
        play sound scratch
        show ep7_503
        with hpunch
        play music 'audio/NomadsDance.mp3'
        g "Mnn! Good!"
        g "*slurps*"
        mc "W-w-w-wait, wait, wait!"
        mc "Whaaat?!"
        mc "You're not angry?!"
        scene ep7_504
        with dissolve
        g "Dude... If anything, I'm friggin' pumped about it!"
        scene ep7_505
        with dissolve
        g "The idea just gets my juices dripping!"
        mc "Really?!"
        scene ep7_506
        with dissolve
        g "Mhm, mhm, mhm!"
        yt "Well, shit..."
        yt "I'm drawing out the playful version of her — I'm getting on her wild side!"
        yt "Where the heck did this woman come from?!"
        scene ep7_507
        with dissolve
        mc "Damn, Gwen... That is not the reaction I expected from you!"
        mc "I was so fucking nervous when I came in here, too!"
        scene ep7_508
        with dissolve
        g "Well then, let me tell you something."
        g "Remember that second time when I took you to the school rooftop?"
        mc "Uh-huh?"
        g "I was so envious of Aine that I thought about stealing you from her."
        g "However, then it occurred to me..."
        g "What if somehow, something happened and we could both have you at the same time? That would be really interesting!"
        g "Oh, boy... You can consider this a dream come true for me, you know that?"
        mc "You, my lady... are friggin' crazy."
        scene ep7_509
        g "Am I now?"
        show ep7_510
        g "Well, I'll gladly accept it if I am!"
        show ep7_511
        g "AHAHAHA!"
        play sound cloth2
        show ep7_512
        with hpunch
        mc "*hugs*"
        g "Whoa~!"
        scene ep7_513
        with dissolve
        g "......"
        mc "I honestly didn't want to choose..."
        mc "You don't know... how happy I am right now, Gwen."
        scene ep7_514
        with dissolve
        g "You know how much I love you."
        g "Aside from that mystifying dream, it's my feelings for you that I hold most dear."
        g "If that's what you truly want, then I'd be more than delighted to take this adventure with you, [mc]."
        scene ep7_515
        with dissolve
        mc "But what about us? What's going to happen then?"
        g "It's simple, the loser will be a loser. It's up to her if she wants to get left behind."
        g "You got nothing to lose on me, you know?"
        scene ep7_516
        with dissolve
        mc "Uhm... Correction..."
        g "Hm?"
        mc "That should be 'them'."
        g "Excuse me? I don't get it."
        mc "Sky is... also..."
        scene ep7_517
        with dissolve
        g "Well shit, [mc]..."
        scene ep7_518
        with dissolve
        mc "Yeah... I know..."
        mc "But like what I said to Emma, it's going to be a long story to tell."
        mc "It wasn't at the snap of a finger or an accident, we simply fell in love with each other."
        scene ep7_517
        with dissolve
        g "My only question is, since when?"
        mc "It went on for a long time, but the way we looked at each other changed after high school."
        g "Damn..."
        g "You guys are fucked up, you know that?"
        scene ep7_518
        with dissolve
        mc "......"
        scene ep7_519
        with dissolve
        g "Pfft!"
        scene ep7_520
        with dissolve
        g "Would you look at that! My man's one hell of a hotshot!"
        g "AHAHAHAHA!"
        mc "*chuckles* Damn it, you're still making fun of me."
        scene ep7_521
        with dissolve
        g "Duh..."
        g "It may be strange, but it's happening out there, you know?"
        g "So what about her? Does she know?"
        scene ep7_522
        with dissolve
        mc "That's the problem, she does..."
        g "And she did not like it, I assume?"
        mc "She might have discovered about us the worst way possible."
        mc "That last morning when we did it, she was acting strange..."
        g "She heard us, I guessed as much."
        g "Did you try and talk to her already?"
        mc "That's the thing, I want to give her some space first before I try."
        mc "I know her, she's... extremely soft at heart and that's kind of a double-edged sword."
        mc "We won't get anywhere if she'll be ignoring me anyway."
        scene ep7_523
        with dissolve
        g "Huh..."
        g "If that's the case, then she is also my responsibility."
        g "I can definitely talk to her, but you have to do your part first, [mc]."
        image gwenmctalkharem:
            "ep7_524.jpg"
            pause 3.0
            "ep7_525.jpg"
            pause .2
            repeat
        show gwenmctalkharem
        with dissolve
        g "Don't get used to the space."
        g "Because if you allow yourself not to talk for a day, you will get used to that."
        g "You'll get used to not talking for three days."
        g "You will fight and then not speak to each other for a month."
        g "And then one of you will eventually say, 'I fell out of love'."
        g "I believe that love is a choice more than an emotion, more than anything."
        g "And that is why we have to work on it."
        g "It's a choice to make it work."
        mc "...It's a choice to love your partner."
        g "Exactly. That's something I learned from my parents' issues."
        g "So whenever you find a chance, grab it and don't let go."
        g "If you have to force her, then do it, so she can understand and until she does."
        g "Do you get what I'm trying to say?"
        mc "Yeah..."
        mc "In fact, that was a slap in my face."
        scene ep7_526
        with dissolve
        g "Just like how you once slapped me back to reality."
        g "It's a simple give and take."
        mc "*chuckles*"
        mc "Thanks, Gwen."
        scene ep7_527
        with dissolve
        g "No, thank you for being honest with me. You thought it would be hard, but you still confessed to me."
        g "Your love and honesty are all that matters to me."
        show ep7_528
        with hpunch
        mc "Enough said."
        scene ep7_529
        with dissolve
        g "Mnnhh~"
        scene ep7_530
        with dissolve
        g "*licks*"
        scene ep7_531
        with dissolve
        g "Haah..."
        scene ep7_532
        with dissolve
        mc "I'm gonna go and have a word with Emma now."
        g "Damn it, [mc]. Now I want you again, but... sure thing!"
        scene ep7_533
        with dissolve
        mc "......"
        scene ep7_534
        with dissolve
        mc "Did she somehow tell you everything?"
        mc "I mean, her reason why you came here in the first place?"
        g "Enough for me to know what's going on."
        g "She said there's no reason for her to hide it now that you know about her."
        mc "I see..."
        mc "Well then... You're going to like this."
        scene ep7_535
        with dissolve
        g "Oh..."
        scene ep7_536
        with dissolve
        g "Ooooohhhhh~!"
        show ep7_537
        g "Bring 'em all in, [mc]! The more, the merrier!"
        mc "We'll see."
        scene ep7_538
        play sound closedoor
        with dissolve
        "*door closes*"
        play sound chair
        show ep7_539
        with hpunch
        pause
        show ep7_540
        g "HNNNNNN~!"
        scene ep7_541
        play sound chair
        with dissolve
        g "{i}Oh, man... This is getting interesting!"
        scene ep7_542
        with dissolve
        g "{i}Come and get me, you losers!"
        g "{i}AHAHAHAHAHA!"
        stop music fadeout 2

        scene black
        with Dissolve(2.0)
        label gwenpause3:
        if _in_replay:
            $ name = persistent.gallery_name
        scene gwenpause3
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()
    elif (emmaroute & gwenskyharem):
        scene ep7_497
        with dissolve
        yt "But before that..."
        yt "I can't leave her hanging for too long."
        yt "If there's someone whose reaction I'm genuinely afraid of, it's gonna be her."
        yt "But I've pretty much dug my own grave. Whatever the outcome is, I still must tell her about it."

        scene black
        with dissolve
        with fadeq

        scene ep7_498
        play sound doorknock
        with dissolve
        mc "*knocks*"
        g "Come in!"
        scene ep7_499
        play sound closedoor
        with dissolve
        play sound chairdrag
        mc "Hey, Gwen..."
        #gwen taps on her piano chair
        yt "So she's really expecting this, huh?"
        yt "Well, what am I thinking? She is the one that I'm actually dating."
        play sound chair
        scene ep7_500
        with dissolve
        g "Listen, from now on if we have something we want to talk about — especially if it's something between us two, let's do it this way."
        g "No talks over the phone nor messages, you got me?"
        g "It's not for us to fight about the topic, it's for us to create a mutual understanding that calls or messages can not."
        mc "Mhm, I understand, Gwen."
        yt "Damn..."
        yt "We're still in the midst of dating, yet she already feels like my wife or something."
        yt "But that just shows how much she wants to stabilize and strengthen our relationship."
        yt "Gwen definitely knows what she's doing."
        scene ep7_501
        with dissolve
        g "So..."
        g "You got something to tell me, right?"
        mc "Mhm."
        g "Go on, I'm all ears."
        scene ep7_502
        with dissolve
        mc "We got ourselves finally settled..."
        g "And...?"
        mc "I couldn't lie so I told her that we were already dating."
        mc "But even if it will hurt her, she's ready to accept that fact just to be with me."
        mc "Now I know you are going to-"
        stop music
        play sound scratch
        show ep7_503
        with hpunch
        play music 'audio/NomadsDance.mp3'
        g "Mnnn!"
        g "*slurps*"
        mc "W-w-w-wait, wait, wait!"
        mc "Whaaat?!"
        mc "You're not angry?!"
        scene ep7_504
        with dissolve
        g "Dude... If anything, I'm friggin' pumped!"
        scene ep7_505
        with dissolve
        g "The idea just gets my juices dripping!"
        mc "Really?!"
        scene ep7_506
        with dissolve
        g "Mhm, mhm, mhm!"
        yt "Well, shit..."
        yt "I'm drawing out the playful version of her — I'm getting on her wild side!"
        yt "Where the heck did this woman come from?!"
        scene ep7_507
        with dissolve
        mc "Damn, Gwen... That is not the reaction I expected from you!"
        mc "I was so fucking nervous when I entered here too!"
        scene ep7_508
        with dissolve
        g "Well then let me tell you something."
        g "Remember that second time when I took you to the school rooftop?"
        mc "Uh-huh?"
        g "I was so envious of Aine that I thought about stealing you from her."
        g "However, then it occurred to me..."
        g "What if somehow, something happened and we could both have you at the same time? That would be very interesting!"
        g "Oh, boy... You can consider this a dream come true for me, you know that?"
        mc "You, my lady... are friggin' crazy."
        show ep7_509
        g "Am I now?"
        show ep7_510
        g "Well, I'll gladly accept it if I am!"
        show ep7_511
        g "AHAHAHA!"
        play sound cloth2
        show ep7_512
        with hpunch
        mc "*hugs*"
        g "Whoa~!"
        scene ep7_513
        with dissolve
        g "......"
        mc "I honestly didn't want to choose..."
        mc "You don't know... how happy I am right now, Gwen."
        scene ep7_514
        with dissolve
        g "You know how much I love you."
        g "Aside from that mystifying dream, it's my feelings for you that I hold dear the most."
        g "If that's what you truly want, then I'd be more than delighted to take this adventure with you, [mc]."
        scene ep7_515
        with dissolve
        mc "But what about us? What's going to happen then?"
        g "It's simple, the loser will be a loser. It's up to her if she wants to get left behind."
        g "You got nothing to lose on me, you know?"
        mc "......"
        scene ep7_519
        with dissolve
        g "Pfft!"
        scene ep7_520
        with dissolve
        g "Would you look at that! My man's one hell of a hotshot!"
        g "AHAHAHAHA!"
        mc "*chuckles* Damn it, you're still making fun of me."
        g "I always do! What do you expect from me?"
        mc "Alright, alright... Anyway, thanks, Gwen."
        scene ep7_527
        with dissolve
        g "No, thank you for being honest with me. You thought it would be hard, but you still confessed to me."
        g "That's all I can ask."
        show ep7_528
        with hpunch
        mc "Enough said."
        scene ep7_529
        with dissolve
        g "Mnnhh~"
        scene ep7_530
        with dissolve
        g "*licks*"
        scene ep7_531
        with dissolve
        g "Haah..."
        scene ep7_532
        with dissolve
        mc "I'm gonna go and have a word with Emma now."
        g "Damn it, [mc]. Now I want you again, but... sure thing!"
        scene ep7_533
        with dissolve
        mc "......"
        scene ep7_534
        with dissolve
        mc "Did she somehow tell you everything?"
        mc "I mean, her reason why you came here in the first place?"
        g "Enough for me to know what's going on."
        g "She said there's no reason for her to hide it now that you know about her."
        mc "I see..."
        mc "Well then... You're going to like this."
        scene ep7_535
        with dissolve
        g "Oh..."
        scene ep7_536
        with dissolve
        g "Ooooohhhhh~!"
        show ep7_537
        g "Bring 'em all in, [mc]! The more, the merrier!"
        mc "We'll see."
        scene ep7_538
        play sound closedoor
        with dissolve
        "*door closes*"
        play sound chair
        show ep7_539
        with hpunch
        pause
        show ep7_540
        g "HNNNNNN~!"
        scene ep7_541
        play sound chair
        with dissolve
        g "{i}Oh, man... This is getting interesting!"
        scene ep7_542
        with dissolve
        g "{i}Come and get me, you suckers!"
        g "{i}AHAHAHAHAHA!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/YoungDetective.mp3' fadein 2
    scene ep7_543
    play sound doorknock
    with dissolve
    mc "*knocks*"
    mc "......"
    play sound opendoor
    scene ep7_544
    with dissolve
    "*door opens*"
    e "Oh, [mc]-"
    mc "Shhhh..."
    scene ep7_545
    with dissolve
    mc "......"
    mc "Good, she's asleep."
    e "She often sleeps early, why?"
    scene ep7_544
    with dissolve
    mc "Do you have a moment? I have a couple of things to discuss with you."
    e "Of course."
    mc "Nice, come with me."

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    scene ep7_546
    with dissolve
    e "Hmm..."
    e "Then you can just get me as your private investigator."
    mc "Wait, is that allowed? You applied as a detective last time, no?"
    image emamcfainves:
        "ep7_547.jpg"
        pause 3.0
        "ep7_548.jpg"
        pause .2
        repeat
    show emamcfainves
    with dissolve
    e "Not literally a Private Investigator, but there are only three of us allowed to handle a single case at a time in our division."
    e "Especially if it's a complicated case that's been unsolved for a while."
    e "It's a relatively new system that was established a few years ago, just so you know."
    mc "Oh..."
    mc "I didn't know about that."
    e "And you are lucky, I don't have any cases in hand at the moment."
    e "If you want, I can write this up tomorrow, and when you are ready, come to my office so we can talk about it."
    e "From what I understand about Jovian's case, he clearly committed first-degree murder."
    e "If he is proven guilty of committing this felony offense, he could be punished with lifetime imprisonment, or worse..."
    e "A death sentence..."
    e "I hope you are ready when that time comes, [mc]."
    mc "If he's guilty, then so be it."
    mc "All I need are his words to prove Hera's story."
    e "Then it's settled."
    e "Don't forget to come to my office. The sooner we can get it done, the better."
    mc "Copy."
    mc "But, jeez..."
    mc "You're really very serious when it comes to your job. I thought it was just your pseudo-personality talking to me."
    e "It is a no-nonsense line of work, so I take it seriously."
    mc "...That makes sense."
    scene ep7_549
    with dissolve
    mc "And one more thing..."
    e "Yes?"
    scene ep7_550
    with dissolve
    mc "Can you tell me about that plan of yours again?"
    mc "Your {b}real{/b} plan this time."
    scene ep7_551
    with dissolve
    mc "Hey, Jess."
    j "You kids should be sleeping at this time."
    j "Anyway, how can I help you?"
    mc "I want you to listen as we try and discuss something."
    j "It'd better be interesting."
    mc "I'm sure it will pique your interest, at the very least."
    j "*chuckles* Alright, I'm listening."

    scene black
    with dissolve
    with fade

    scene ep7_552
    with dissolve
    mc "So the plan is to take over the Mafia by having me married to Aine?"
    mc "Where did all the {b}hiding{/b} stuff go?"
    e "That's half of it."
    e "By having you two married, we can keep her secured from the guy who's entitled to be her husband."
    yt "I have a bad feeling about this guy..."
    mc "Is this the Arranged Marriage you were talking about?"
    e "Mhm."
    e "Not only can we secure her, but we can also put a stop to Hera's plans for her."
    e "But taking over the Mafia won't happen unless we are holding some of their assets."
    e "Right now, Hera only owns a handful of companies in this city and that's about it."
    e "Still, it won't be that easy."
    e "We have to take them all, or at least most of them."
    e "That is the hardest part."
    mc "Do you... have some kind of plan for it?"
    e "Yes, it recently came to my mind, but we can use Miss Klara's-"
    scene ep7_553
    with dissolve
    j "You can leave that to us."
    j "We plan to kick-start Klara's company and use it against Hera."
    j "That's why she wants to build one in the first place, for your future."
    mc "I had already guessed that much considering what's happening so far."
    j "However, we will need a few more brains at work, so your help will be appreciated."
    mc "Understood."
    scene ep7_554
    with dissolve
    e "Although you might see Aine as the only person that will benefit from this, it will be for us at the same time."
    e "You can gain the power to keep everyone safe when it's needed."
    scene ep7_555
    with dissolve
    mc "You're right..."
    mc "I have to think on a larger scale, rather than just thinking about myself."
    mc "The future is uncertain, there is a possibility that this could lead to a brawl and I surely don't want that to happen."
    mc "I'm sure that's what Klara thinks too."
    mc "I can plan ahead and keep everyone safe as much as I can."
    mc "What I need is just a bit of power."
    mc "And if the only way is for me to have Aine as a wife..."
    mc "Then..."
    mc "But what exactly is the power that I can get from it."
    scene ep7_556
    with dissolve
    e "A lot."
    e "The Mafia can never be led by a woman. That's their first and foremost rule."
    scene ep7_557
    with dissolve
    j "I was right, you dug into their old documents."
    e "Yes, I did."
    scene ep7_558
    with dissolve
    mc "Okay, I think I get it."
    mc "So, I have to make a name of my own using Aine, right?"
    e "Exactly, and that will come when we start taking over their assets, their people will slowly know and acknowledge you."
    e "And they will follow the ones they find more suitable to lead them."
    mc "Wow..."
    mc "That's kinda dreamy..."
    scene ep7_559
    with dissolve
    j "The Mafia as it is now, is nothing like they used to be since Hera temporarily led it."
    j "However, you still got very lucky earlier. If not for us, you would have ended up dead."
    show ep7_560
    e "See?! What did I tell you?!"
    scene ep7_561
    with dissolve
    j "That is the extent of what I could do to help you, [mc]."
    j "From now on, the rest will be all on you."
    mc "......"
    scene ep7_562
    with dissolve
    j "Before you two start moving, there is one piece of misinformation you got there, Emma."
    scene ep7_563
    with dissolve
    e "Huh?"
    j "You don't need to get them married..."
    j "Having them engaged is already more than enough to hit your goals."
    j "You just need a witness from the Mafia's main family and I can be that person."
    scene ep7_564
    with dissolve
    mc "......"
    e "......"
    scene ep7_565
    with dissolve
    mc "You thinking what I'm thinking?"
    e "Mhm."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "Friday, early morning..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Swayed.mp3' fadein 2
    scene ep7_566
    play sound closedoor
    with dissolve
    "*door closes*"
    play sound woosh
    show ep7_567
    a "Hm?"
    show ep7_568
    with hpunch
    a "Ahh!"

    scene black
    with dissolve
    with fade

    scene ep7_569
    with dissolve
    e "Good morning."
    a "Urrhh..."
    a "You two didn't have to do me like that!"
    a "What are we doing here again, anyway?"
    scene ep7_570
    with dissolve
    j "Welcome back."
    j "Are you both ready?"
    a "Uhm... Ready for...?"
    scene ep7_571
    with dissolve
    mc "She still has no idea what's going on."
    play sound woosh
    show ep7_572
    k "Oh my god... I'm going to cry."
    j "Jesus..."
    a "What's... happening?"
    scene ep7_573
    with dissolve
    j "Well, you two are about to get engaged, right now."
    scene ep7_574
    with dissolve
    a "......"
    mc "......"
    play sound punch
    show ep7_575
    with hpunch
    a "WHAAAAAAAAAAAAAAT?!"
    a "B-b-b-b-but why?! Why with him?! Why here?!"
    a "What is this for?!"
    j "There has to be a witness from one of the Mafia heads to make it official."
    j "I may not consider myself as one, but I'm still technically one of them."
    j "As for the rest, I'll leave the explanation to you two. This is your plan after all."

    scene black
    with dissolve
    with fade

    play sound smallbell
    show ep7_576
    pause
    scene ep7_577
    with dissolve
    pause
    play sound pop
    show ep7_578
    a "MNNNN~!"
    a "What do I do now~?"
    j "I'd say live with him, much closer than before."
    scene ep7_579
    with dissolve
    a "You mean like... sleep in his room?"
    j "Exactly."
    j "Get used to it. It'll eventually take the embarrassment away, but that's up to you."
    show ep7_580
    a "Huuun~!"
    a "*sniffs*"
    scene ep7_581
    with dissolve
    j "You all should take your time and relax for now. We will have to wait until Klara's company is fully established."
    j "Now, I know you want to find Jovian, but take it easy, and don't forget that you are all still young."
    show ep7_582
    k "Is that true, [mc]?"
    mc "Yes, I'm going to find him. We are already set on that."
    scene ep7_583
    with dissolve
    k "......"
    scene ep7_582
    with dissolve
    k "Alright, then you have my support. Go find him and make him pay for what he's done."
    mc "Mhm."
    scene ep7_584
    with dissolve
    j "Don't forget that you are still my employee, [mc]."
    j "It's Friday, you know that you have work today, right?"
    mc "Oh..."
    j "Freya was already on her way before you came here."
    mc "Oh, shit! Alright!"
    scene ep7_585
    with dissolve
    mc "Come, let's go home for now!"
    a "Waaaaait~!"
    scene ep7_586
    with dissolve
    a "Huuun~!"

    scene black
    with dissolve
    with fadeq

    "At night..."

    scene black
    with dissolve
    with fadeq

    play sound pop
    show ep7_587
    pause
    play sound pop
    show ep7_588
    pause
    play sound pop
    show ep7_589
    pause
    play sound pop
    show ep7_590
    pause
    play sound pop
    show ep7_591
    pause
    show ep7_592
    with dissolve
    mc "Hey, could you please relax?"
    mc "You've been like that since I got back. It's been like what? Three hours now?"
    scene ep7_593
    with dissolve
    a "Huuun~!"
    play sound woosh
    show ep7_594
    a "That's because I don't know what to do, I never had a boyfriend before, okay?!"
    a "And now you're my... my..."
    scene ep7_595
    with dissolve
    a "What's it called?"
    mc "Fiancé."
    show ep7_596
    a "Yes! My..."
    a "F-f-f-fiancé!"
    scene ep7_597
    with dissolve
    mc "*sighs*"
    scene ep7_598
    with dissolve
    mc "Listen, you don't have to force it. It's only temporary until this is all over."
    mc "Just temporary!"
    show ep7_599
    mc "Tem-po-ra-ry!"
    scene ep7_600
    with flash
    mc "Give me... that fucking hand!"
    mc "I spent almost all my savings on this ring! Don't you dare take it off your finger!"
    a "Nooooo~! Emmaaaa~!"
    e "Just accept it, it's for your own good."
    scene ep7_601
    with flash
    a "*sniffs*"
    scene ep7_602
    with dissolve
    a "Whaat~?"
    a "But once we are engaged to each other, we can never break up unless one of us dies...!"
    a "Especially if there was a witness...!"
    a "That's one of my family's rules...!"
    a "You knew that, didn't you?"
    stop music
    play sound smallbell
    show ep7_603
    mc "Eh?"
    scene ep7_604
    a "Eh?"
    mc "Are you serious?"
    a "Uh-huh?"
    scene ep7_605
    with dissolve
    mc "Urrhh..."
    show ep7_606
    with hpunch
    mc "Raaaaaaaahh!"
    play sound sneeze_female
    show ep7_607
    with hpunch
    j "Achoooo~!"
    play sound sniff
    show ep7_608
    j "*sniffs*"
    j "I think I might have forgotten to tell them something, but I can't think what it is..."
    k "Huh?"
    scene ep7_609
    with dissolve
    mc "*sighs*..."
    play music 'audio/TimeTraveling.mp3' fadein 2
    mc "Well, whatever... As long as it will benefit us both, I don't care about those rules."
    mc "Once we take over the Mafia, I'm sure I can change that rule or whatever it is."
    mc "I can, right?"
    a "As long as you are the leader, everyone will follow what you say. That includes changing the rules."
    mc "See?"
    mc "There's nothing to worry about."
    mc "I was serious, Aine. You don't have to force yourself."
    mc "Once I reach my goals, then we can call it over."
    if ainepoint == 12:
        play sound chair
        scene ep7_610
        with dissolve
        a "......"
        scene ep7_611
        with dissolve
        a "You know?"
        a "That's the reason why I never had a boyfriend before."
        a "Because once things go deeper, it becomes very risky and you don't know what might happen..."
        a "I don't mean anything life-threatening, but I'm afraid that I might end up with a broken heart."
        a "If my partner broke up with me, my only choices would be to endure it, or kill him to free myself from our vow."
        mc "*gulps*"
        a "It is uncommon, but we still follow that custom now."
        scene ep7_612
        with dissolve
        a "However, I cannot do that."
        a "So I made a promise to myself that if I ever loved someone, I wanted that person to be the last."
        yt "Now she's making me feel bad..."
        mc "I'm sorry I had to force it on you... I just-"
        scene ep7_613
        with dissolve
        a "Mmh..."
        scene ep7_614
        with dissolve
        a "It's not that bad."
        a "At the end of the day, we freed Emma, and we're both also safe from my mother now."
        a "Especially me, as long as we stick together, that is."
        mc "......"
        menu:
            "Make it officially \"official\"":
                $ aineroute = True
                label ainethumbsuck:
                if _in_replay:
                    $ name = persistent.gallery_name
                yt "Well? I can't just leave her hanging, can I?"
                yt "This is also a chance for me to push her a little bit and test her out."
                play sound chair
                show ep7_619
                with hpunch
                a "Ahh..."
                a "[mc]?"
                mc "I mean, you have a point."
                mc "But do you know what I like the most about this?"
                a "Uhm... What?"
                mc "Is that I have a beautiful fiancée in front of me... {b}You{/b}."
                scene ep7_620
                with dissolve
                a "*blushes* H-Huh?"
                scene ep7_621
                with dissolve
                a "Uhm... [mc], you're getting too close!"
                mc "We never had a chance before, so why don't we..."
                mc "...Make it official?"
                mc "Right here..."
                mc "Right now..."
                scene ep7_622
                with dissolve
                mc "*licks*"
                a "Mmmp~!"
                scene ep7_623
                with Dissolve(1.0)
                mc "*licks*"
                a "Mnnhhh..."
                scene ep7_624
                with Dissolve(2.0)
                pause
                show aine1
                with dissolve
                a "*sucks* *sucks*"
                yt "I haven't noticed it until now, but she smells so fucking nice!"
                yt "It's that smell that could entice any man she's with."
                yt "Goddamn, I don't want to push her too much but she's making me want to go all the way!"
                yt "I did not expect her to suck my finger on her own too!"
                mc "Aine?"
                a "*sucks* *sucks*"
                yt "Yeah, she's lost to the pleasure..."
                yt "Let's see if I can..."
                pause
                play sound chair
                scene ep7_625
                with dissolve
                mc "Your beauty is really like no other, Aine..."
                mc "You are the most alluring woman I've ever met in my life, do you know that?"
                scene ep7_626
                with Dissolve(1.0)
                yt "I can feel her breath from here. I can tell that she's nervous but..."
                yt "Let's do it."
                scene ep7_627
                with dissolve
                mc "*smooch*"
                a "......"
                a "........."
                stop music
                play sound gasp
                show ep7_628
                with hpunch
                a "*gasps*!!"
                play sound opendoor
                show ep7_629
                pause
                play sound doorslam
                show ep7_630
                with hpunch
                pause
                scene ep7_631
                with dissolve
                mc "*chuckles*"
                yt "Yeah, she has something for me."
                yt "She could've pushed me away, but she unconsciously took it in."
                yt "Now I can't wait for her answer..."
                $ renpy.end_replay()
            "Just let her be":
                $ aineroute = False
                a "I will still try and stay here because that's what I want to do."
                a "This ring still means something to me, and I will be your fiancée until my last breath."
                mc "If that's what you want..."
                mc "Alright, I'll accept it."
    else:
        $ aineroute = False
        scene ep7_615
        with dissolve
        a "......"
        scene ep7_616
        with dissolve
        a "Fine, but I will still try and stay here because that's what I want to do."
        a "This ring still means something to me, and I will be your fiancée until my last breath."
        scene ep7_617
        with dissolve
        a "I guess, it's not half-bad. *giggles*"
        scene ep7_618
        with dissolve
        mc "If that's what you want..."
        mc "Alright, I'll accept it."
    stop music fadeout 2

    if aineroute:
        play music 'audio/DontShoot.mp3'
        scene ep7_632
        with wipeleft
        a "Come on, come on, come on..."
        a "Pick up the phone, please!"
        scene ep7_633
        with dissolve
        "........"
        "............."
        f "Yow! What's up, sis?"
        play sound woosh
        show ep7_634
        a "Freeeeeey~!"
        f "Wait, whoa, hold up before you scream at me!"
        f "What the hell happened to you?!"
        scene ep7_635
        with dissolve
        a "W-well... I've got a ring on my finger, and I'm engaged!"
        f "Uh, don't joke like that, sis."
        play sound woosh
        show ep7_634
        a "I'm serious, Frey!"
        f "Eh, what the hell?"
        f "But to whom?"
        f "Don't tell me it's that guy mom was trying to-"
        a "No, I'm engaged to [mc]!"
        f "Pfff!"
        f "AHAHAHAHAHAHAHAHAHAHAHA!"
        show ep7_636
        with hpunch
        a "Don't just laugh at me! I don't know what to do~!"
        f "Excuse me?"
        f "How the hell do you not know? You're such a noob, it's pretty simple!"
        f "Just show him your panties and suck his dick or something! Use your brain, sis!"
        a "I'm seriously freaking out here, Frey! You're not helpful at all!"
        f "Hey, you're the one who called me! I'm just telling you what I got from a reliable source!"
        show ep7_637
        a "And where would that be?!"
        f "Where else? The internet, of course!"
        a "You can't just believe everything you see on the net, Freya!"
        f "I'm on the internet every day, sis! What can I do?!"
        stop music fadeout 3
        scene ep7_638
        with dissolve
        f "If you seriously want help, then fine! Just give me a sec!"
        "............"
        "................."
        scene ep7_639
        with dissolve
        a "Uhm, Frey? Where did you-"
        f "Lo and behold!"
        play music 'audio/Nocturne.mp3' fadein 2
        scene ep7_640
        with dissolve
        k "Hello, dear?"
        a "M-Miss Klara?"
        k "Yes, it's me."
        k "Did [mc] already give you a hard time?"
        a "Uhm... No, that's not it."
        a "I never had a boyfriend before and I honestly don't know what to do."
        k "Hm..."
        scene ep7_641
        with dissolve
        k "I understand, dear."
        k "But I have a question."
        k "Why do you want to make it work?"
        a "Why do I..."
        a "No, I just-"
        k "You don't have to hide it from me, dear, I can tell. I'm a grown-up woman, after all."
        k "Do you like him?"
        a "Uhm..."
        a "I... don't know, Miss Klara."
        scene ep7_642
        with dissolve
        k "Ask these questions to yourself."
        k "How do you feel when he is beside you?"
        k "And how do you feel when he is not?"
        scene ep7_643
        with dissolve
        a "......"
        scene ep7_644
        with dissolve
        a "All I know is that he gives me a lot of comfort."
        a "So there were times when I was searching for it."
        a "I... always get flustered when he does something to me... then my heart beats faster than usual."
        k "Then there's your answer, dear. But it's only you who can know what it is."
        scene ep7_645
        with dissolve
        a "......"
        k "My, my..."
        k "I did not expect you to be this innocent."
        k "If you want some advice, I cannot tell you anything. You'll have to figure it out on your own."
        k "We each have our ways; you'll just have to find yours."
        k "But if I can tell you something: just be {b}you{/b} and don't be afraid to be proactive and ask him anything."
        a "......"
        scene ep7_644
        with dissolve
        a "Alright. Thanks, Miss Klara."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/NomadsDance.mp3'
    scene ep7_646
    with dissolve
    yt "*sighs*"
    yt "After some time, it's finally progressing, although the results are a bit bittersweet."
    yt "Nevertheless, I'm locked and loaded and ready to move."
    scene ep7_647
    with dissolve
    yt "......"
    yt "I might wanna talk to Shu about that place. I can still relax for a bit, right? Haha!"
    yt "I can already imagine the astonishing {b}views{/b}."
    show ep7_648
    yt "Hee ehehee..."
    scene ep7_647
    with dissolve
    yt "It's my day off tomorrow, perfect timing."
    yt "I should sleep and wake up early tomorrow, then find that twat."
    if aineroute:
        play sound opendoor
        scene ep7_649
        with dissolve
        "*door opens*"
        a "{i}Yeah, I'll just try and see how it goes from here."
        play sound chair
        scene ep7_650
        with dissolve
        yt "Is that Aine?"
        yt "Now that it's happening, it really is awkward."
        play sound chair
        scene ep7_651
        with dissolve
        pause
        play sound woosh
        show ep7_652
        pause
        play sound chair
        scene ep7_653
        with dissolve
        pause 0.5
        play sound woosh
        show ep7_654
        mc "Hey, can we talk-"
        play sound gasp
        show ep7_655
        with hpunch
        a "*gasps*"
        scene ep7_627
        with flash
        pause
        show ep7_655
        with flash
        pause
        play sound pop
        show ep7_656
        a "*faints*"
        mc "Huh?"
        play sound chair
        scene ep7_657
        with dissolve
        mc "Aine?"
        mc "Hey, Aine!"
        scene ep7_657a
        with dissolve
        a "......"
        scene ep7_658
        with dissolve
        mc "......"
        scene ep7_659
        with dissolve
        mc "*chuckles* Again, thank you."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music riftstable fadein 2
    play sound eternityclock loop fadein 2
    scene ep7_660
    with Dissolve(3.0)
    mc "And that's how it started."
    mc "Ridiculous, isn't it?"
    scene ep7_661
    with dissolve
    un "I sayeth destiny leadeth thee to such circumstance. Nothing risible about it."
    un "Hast thou regreteth aught?"
    scene ep7_660
    with dissolve
    mc "I still have no idea how the hell am I able to understand you."
    mc "But if you're asking if I regret anything, then..."
    stop sound fadeout 2
    stop music fadeout 2
    scene black
    with Dissolve(2.0)
    pause
    show ep7end
    with dissolve
    pause
    scene black
    with dissolve
    pause

    play music cityalley fadein 2
    scene ep7_662
    with Dissolve(3.0)
    pause
    k "*deeply exhales*"
    k "Welcome home..."
    k "Let's get this over with, shall we?"
    scene black
    stop music
    pause


    jump ch1ep1

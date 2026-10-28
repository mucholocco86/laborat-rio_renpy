label ch1ep4:
    show screen day_sunday with dissolve
    play music 'audio/NorthernLights.mp3'
    $ renpy.sound.set_volume(0.3, 1.0)
    scene ch1ep4_1
    with dissolve
    pause
    play sound doorslam
    scene ch1ep4_2
    with hpunch
    f "[mc]~!!"
    $ renpy.sound.set_volume(1.0, 1.0)
    m "Hm?"
    play sound closedoor
    scene ch1ep4_3
    with Dissolve(0.1)
    f "[mc]!"
    mc "Freya? I thought you were..."
    scene ch1ep4_4
    with dissolve
    f "Forget about that! L...look at this!"
    mc "A letter? Who's it from?"
    f "It's from mom!"
    play sound closedoor
    scene ch1ep4_5
    with dissolve
    m "What's happening here?"
    scene ch1ep4_6
    with dissolve
    f "I woke up just before you left and saw the gift... I thought it was only a dress, but then..."
    f "I found that letter at the bottom."
    f "What do you think?"
    mc "..."
    scene ch1ep4_7
    with dissolve
    mc "We need to discuss this immediately. Let's gather everyone, now."
    mc "Wake everybody up and have them meet in the living room."
    f "Got it!"
    scene ch1ep4_8
    with dissolve
    mc "..."
    m "Is everything alright?"
    scene ch1ep4_9
    with dissolve
    pause
    scene ch1ep4_10
    with dissolve
    mc "Yeah, I'm going to be fine."
    mc "But first, let's bring this to everyone's attention."
    scene ch1ep4_11
    with dissolve
    m "..."
    m "{i}I thought I wasn't afraid of anything in this world, but that smile just now... is making me nervous."
    m "{i}What's on your mind, Commander? I thought we had a plan?"
    call hide_days from _call_hide_days_19
    with dissolve
    stop music fadeout 2
    scene ch1ep3e
    with dissolve
    pause
    scene ch1ep4s
    with dissolve
    pause
    scene warn2
    with dissolve
    pause

    scene black
    with dissolve
    with fade

    show screen day_sunday with dissolve
    play music 'audio/NorthernLights.mp3'
    scene ch1ep4_12
    with dissolve
    mc "Sorry, I know it's late. I hope I'm not bothering you too much."
    scene ch1ep4_13
    with dissolve
    g "Don't worry about it, [mc]. This is a pressing matter; sleep can come later."
    scene ch1ep4_14
    with dissolve
    pause
    yt "Klara..."
    scene ch1ep4_15
    with dissolve
    k "Alright, let's hear it. Whatever she has to say."
    scene ch1ep4_16
    with dissolve
    mc "..."
    scene ch1ep4_17
    with dissolve
    h "{i}To those I have wronged, especially Aine and [mc]..."
    h "{i}As I pen this letter, I find myself at a crossroads, one paved with decisions that have irrevocably altered the course of our lives."
    h "{i}My actions, born from a place of desperation, blindness, and control, have cast long shadows over us all."
    h "{i}I stand before you, not as a figure of authority or power, but as someone who has been brought to her knees by the weight of her own choices."
    scene ch1ep4_18
    with dissolve
    h "{i}I am ensnared, my options dwindling, my freedom a mere illusion. The path I chose was one I believed necessary, yet I recognize now the pain it has inflicted."
    h "{i}For the hurt I have caused, particularly to Aine and [mc], words of apology may seem hollow."
    h "{i}But know that my intent now is to mend what has been broken in the only way I know how."
    scene ch1ep4_19
    with dissolve
    h "{i}This is not a plea for absolution, nor do I write this seeking redemption in your eyes."
    h "{i}Rather, it is an acknowledgment of the web I have woven and a step towards untangling it, if such a thing is still possible."
    scene ch1ep4_20
    with dissolve
    h "{i}Now, on a less formal note..."
    h "{i}About Jovian... I have some information that could be useful, but unfortunately, nothing earth-shattering."
    h "{i}I believe I had mentioned that I conducted a search in hopes of finding him. My last solid lead was the old Winters' place, out of town."
    scene ch1ep4_21
    with dissolve
    h "{i}Someone among you knows exactly where it is."
    h "{i}After that, nothing: Jovian might as well have disappeared off the face of the earth. If you're clueless about his vanishing, I understand from firsthand experience."
    scene ch1ep4_22
    with dissolve
    h "{i}My hands were and are still tied. I don't have the reach or power to dig deeper."
    h "{i}Bonheur has taken a significant portion of the Mafia's power and resources. He has more pull than I do."
    h "{i}What he's planning with that kind of power, I can't say. But him having control over part of the Mafia means trouble for me. For everyone entangled in this mess."
    scene ch1ep4_23
    with dissolve
    h "{i}Lastly, I'd like to request something big of you, Aine. I know it might be too much."
    h "{i}I'm hoping you'll consider taking my place in the Mafia as soon as possible."
    h "{i}Not to keep things the same, but to change them for the better."
    h "{i}You may not know, but some people in the group are looking to build a brighter future. Those people need someone to hold them together."
    h "{i}Use this to your advantage, or whatever you decide. It's all up to you two; I will not stop you."
    scene ch1ep4_24
    with dissolve
    h "{i}Although, I suggest..."
    h "{i}Why don't you two get married already? What are you waiting for, Christmas?"
    h "{i}Yes, I know what you have been planning. Jess is watching over you, and I was informed of this before writing this letter."
    h "{i}[mc] has shown he's strong enough for this. With the two of you, I believe you can make things better."
    h "{i}I've been a thorn in your side for too long. So, on [mc]'s advice, I'm stepping back. This way, you can move forward without me in the way."
    h "{i}I never planned to get you involved like this, but now I see the mess I've made. I'm ready to give up everything if it means you can have the life you deserve."
    h "{i}Use what I've left behind to create something new. It's your stage now, not mine."
    scene ch1ep4_25
    with dissolve
    h "{i}To my daughters, you mean everything to me. Despite all the messiness of these past few years, my love for you has never changed."
    h "{i}I hope you can find it in your hearts to move past the chaos I've caused. Be happy."
    h "{i}With love, Hera."
    scene ch1ep4_26
    with Dissolve(1.0)
    pause
    scene ch1ep4_27
    with dissolve
    pause
    scene ch1ep4_28
    with dissolve
    pause
    scene ch1ep4_29
    with dissolve
    m "..."
    scene ch1ep4_30
    with dissolve
    m "{i}Yet again, everyone around me is in pain..."
    scene ch1ep4_31
    with dissolve
    m "{i}Why...?"
    m "{i}Why does it have to be always like this...?"
    call hide_days from _call_hide_days_20
    stop music fadeout 3
    play sound woosh5
    scene black
    with Dissolve(0.1)
    pause 1.5
    play sound2 tinnitus fadein 2 loop
    scene ch1ep4_32
    with Dissolve(5.0)
    play sound war fadein 10 loop
    un "{size=-15}Four!"
    scene ch1ep4_33
    with Dissolve(2.0)
    un "{size=-9}Four! You alright there, buddy?!"
    m "H...huh?"
    stop sound2 fadeout 6
    scene ch1ep4_34
    with Dissolve(2.0)
    un "Are you alright?!"
    $ renpy.music.set_volume(1.0, 1.0)
    play music 'audio/ArmedAndReady.mp3'
    play sound4 headshot
    show ch1ep4_35
    with hpunch
    play sound3 ak74
    pause
    $ renpy.music.set_volume(0.6, 1.0)
    scene ch1ep4_36
    with Dissolve(0.2)
    play sound4 m4
    si "Fuck, they really brought the calvary down on us this time. That RPG would've taken us out if it weren't for your reflexes, Five."
    scene ch1ep4_37
    with Dissolve(0.2)
    play sound3 pkp
    eg "Way too close... Is Four alright?"
    si "Eight! Targets, 3 o'clock! They're trying to flank us!"
    scene ch1ep4_38
    with Dissolve(0.2)
    fi "Four?"
    scene ch1ep4_39
    with Dissolve(0.2)
    m "I am fine. Nothing to worry about."
    si "Five, bring yourself here! We need support, NOW!"
    scene ch1ep4_40
    with Dissolve(0.2)
    m "Maybe I can..."
    fi "Negative, I need you to do something first."
    scene ch1ep4_41
    with Dissolve(0.2)
    fi "Listen, we won't be able to hold them off forever. I need you to call for an evac first while we return fire. Give them our coordinates."
    eg "Five! It's getting a bit crowded here!"
    scene ch1ep4_42
    with Dissolve(0.2)
    fi "Got it?"
    scene ch1ep4_43
    with Dissolve(0.2)
    play sound2 casepickup2
    m "Got it."
    fi "Don't lose it again, will you? Our guns will never be able to replace it."
    m "Sorry."
    scene ch1ep4_44
    with Dissolve(0.2)
    fi "*nods*"
    play sound2 running loop
    scene ch1ep4_45
    with Dissolve(0.2)
    pause 0.6
    stop sound2 fadeout 3
    scene ch1ep4_46
    with Dissolve(0.2)
    pause
    play sound3 casepickup2
    scene ch1ep4_47
    with Dissolve(0.2)
    play sound4 radiostatic
    m "Command, this is Replace Element, callsign Four. How copy? Over."
    play sound4 radiostatic
    comms "Four, this is HQ. Comms are five by five. Report status. Over."
    play sound4 radiostatic
    m "Encountering heavy enemy resistance, surprise assault compromizing our perimeter. Risk of encirclement imminent, over."
    play sound4 radiostatic
    m "Requesting immediate extraction to avoid entrapment. Awaiting instructions. Over."
    play sound4 radiostatic
    comms "... Running request to command, hold the line. Over."
    scene ch1ep4_48
    with dissolve
    pause
    scene ch1ep4_49
    with dissolve
    pause
    scene ch1ep4_50
    with dissolve
    pause
    scene ch1ep4_51
    with dissolve
    play sound4 radiostatic
    comms "Four, this is HQ. Are you still there? Over."
    scene ch1ep4_52
    with dissolve
    play sound4 radiostatic
    m "Solid copy, still here. Was the request for exfil granted? Over."
    play sound4 radiostatic
    comms "... Confirm completion of primary directives? Over."
    play sound4 radiostatic
    m "Affirmative, HQ. HVT neutralized, sensitive materials destroyed. Over."
    play sound4 radiostatic
    comms "Excellent. Request for exfil granted, relay your current grid. Over."
    play sound4 radiostatic
    m "Current grid is Point Kilo One-Two, how copy? Over."
    play sound4 radiostatic
    comms "Solid copy, Four. Extraction bird's inbound, ETA five mikes. Maintain position and prepare for immediate exfil. Out."
    play sound2 m4
    scene ch1ep4_53
    with Dissolve(0.2)
    pause
    play sound3 g17_multiple
    scene ch1ep4_54
    with Dissolve(0.2)
    eg "Took you long enough. What did command say?"
    play sound2 m4
    m "They asked us if we completed the mission and then agreed to extract us. Helo will be here in 5."
    si "Typical. If we hadn't, then they would have left us to rot. I'm sure of it."
    play sound2 m4
    scene ch1ep4_55
    with Dissolve(0.2)
    play sound3 g17_multiple
    fi "Does it really matter now, Six? What matters is that we did it and are all getting out of here in 5 minutes. We just need to hold on a bit longer."
    play sound3 g17_multiple
    eg "You Odd Numbers are always so optimistic, so forgiving. If you weren't, Seven would still be here."
    play sound2 m4
    fi "Ack, I'm not having this discussion with you again, Eight. We decided to move past it."
    play sound3 m4
    scene ch1ep4_56
    with Dissolve(0.2)
    si "That's enough! Let's just get this done, okay?"
    fi "Everyone, focus! We are all going home together, you hear me?"
    eg "Far easier said than done, man! But I ain't ready to die here! Let's do it!"
    fi "That's more like it."
    play sound2 m4
    scene ch1ep4_57
    with Dissolve(0.2)
    play sound3 g17_multiple
    fi "Four, while you were gone, some hostiles managed to sneak around on our right flank. They're probably going through the ruined buildings to surprise us."
    fi "Mind giving them a warm welcome?"
    m "Sure."
    si "Atta girl. Don't be late, though!"
    m "*nods*"
    scene black
    with dissolve
    pause 1.0
    scene ch1ep4_58
    with dissolve
    pause
    scene ch1ep4_59
    with Dissolve(0.2)
    sol1 "Gunshots are getting louder. We are getting close. Those insects won't even know what hit 'em."
    scene ch1ep4_60
    with Dissolve(0.2)
    sol2 "I don't know man, I have a bad feeling about this. It's only four of them, but they still managed to take out dozens of us."
    scene ch1ep4_61
    with Dissolve(0.2)
    sol3 "They even got Jernandez, and god knows how tough that dude was."
    scene ch1ep4_62
    with Dissolve(0.2)
    sol1 "Exactly why we'll make sure those whores pay for what they did."
    scene ch1ep4_63
    with Dissolve(0.2)
    sol2 "Hehe, dibs on the least blown-up one."
    sol2 "What about you, Ray?"
    sol3 "Honestly, I just wanna..."
    $ renpy.music.set_volume(0.3, 1.0)
    $ renpy.sound.set_volume(0.5, 1.0)
    play sound2 woosh4
    scene ch1ep4_64
    sol1 "Shit! It's one of th-"
    play sound3 headsplat
    scene ch1ep4_65
    with hpunch
    pause
    play sound2 gravelslide
    scene ch1ep4_66
    with dissolve
    pause
    play sound3 katana_impact
    show ch1ep4_67
    with flashq
    pause 1.0
    play sound5 gore_large_07
    play sound4 katanasheath
    scene ch1ep4_68
    with Dissolve(0.1)
    pause
    play sound3 bodyfall
    play sound2 bodyfall2
    scene ch1ep4_69
    with dissolve
    m "Amen..."
    $ renpy.music.set_volume(0.5, 1.0)
    $ renpy.sound.set_volume(1.0, 1.0)
    play sound3 running loop
    scene ch1ep4_70
    with Dissolve(0.2)
    eg "I'm black on ammo!"
    si "Same, last mag here."
    fi "Don't give in! Use your sidearm if you have to!"
    play sound3 gravelslide
    scene ch1ep4_71
    with Dissolve(0.2)
    si "Hey, Four's back!"
    eg "Perfect timing. Give us a hand, Four!"
    play sound2 ak74
    scene ch1ep4_72
    with Dissolve(0.2)
    pause
    scene ch1ep4_73
    with Dissolve(0.2)
    m "Six, throw a flashbang."
    si "Copy that, it's my last one."
    play sound3 woosh2
    scene ch1ep4_74
    si "Flash out!"
    $ renpy.music.set_volume(0.3, 1.0)
    $ renpy.sound.set_volume(0.5, 1.0)
    play sound4 flash_detonate
    show ch1ep4_75
    with hpunch
    pause 0.2
    scene ch1ep4_76
    with Dissolve(0.2)
    pause 0.3
    play sound5 katana_open
    play sound3 running loop
    scene ch1ep4_77
    with Dissolve(0.1)
    pause
    play sound2 katana_slash
    show ch1ep4_78
    pause 0.2
    play sound3 katana_slash2
    show ch1ep4_79
    pause 0.2
    play sound4 katana_slash3
    show ch1ep4_80
    pause 0.2
    play sound5 katana_slash4
    show ch1ep4_81
    pause 0.3
    play sound2 katana_slash_multiple
    show ch1ep4_82
    pause 1.1
    play sound3 katana_impact
    play sound4 gore_large_07
    show ch1ep4_83
    pause
    $ renpy.music.set_volume(0.5, 1.0)
    $ renpy.sound.set_volume(1.0, 1.0)
    play sound5 hellfire loop
    scene ch1ep4_84
    with Dissolve(2.0)
    pause
    $ renpy.sound.set_volume(0.5, 1.0)
    stop sound5 fadeout 6
    play sound2 helicopter_outside fadein 3 loop
    scene ch1ep4_85
    with dissolve
    pause
    scene ch1ep4_86
    with dissolve
    pil "To Replace Element, this is Silverbird 1. We have arrived."
    pil "LZ is hot, I repeat LZ is hot. Get in immediately!"
    pil "We're leaving in 1 mike. Out."
    scene ch1ep4_87
    with dissolve
    fi "Let's go everyone! Pop smokes to cover our retreat."
    play sound3 woosh2
    scene ch1ep4_88
    eg "Copy! Smokes out!"
    scene ch1ep4_89
    with Dissolve(2.0)
    pause
    scene ch1ep4_90
    with Dissolve(0.2)
    sol4 "FOR MOTHER SHA CREA!!!"
    play sound3 g17_multiple
    scene ch1ep4_91
    play sound4 headshot
    play sound5 rpg_fire
    pause
    scene ch1ep4_92
    with Dissolve(0.1)
    m "RPG!"
    scene ch1ep4_93
    with Dissolve(0.2)
    pause
    play sound3 fistbump
    scene ch1ep4_94
    with hpunch
    pause 0.3
    play sound4 bodyfall
    scene ch1ep4_95
    with hpunch
    pause 0.4
    play sound5 rpg_explosion
    scene ch1ep4_96
    with hpunch
    pause 0.6
    play sound3 bodyfall
    scene ch1ep4_97
    with hpunch
    pause
    scene ch1ep4_98
    with Dissolve(0.2)
    si "NO!! FIVE!!"
    scene ch1ep4_99
    with dissolve
    pause
    play sound3 pkp loop
    scene ch1ep4_100
    with Dissolve(0.2)
    eg "SHIT! MORE SOLDIERS COMING!"
    eg "Four! Grab Five and get to the chopper already!"
    m "O-okay!"
    scene ch1ep4_101
    with dissolve
    m "It's gonna be okay, Five! We're almost there, just... a little further!"
    scene ch1ep4_102
    with dissolve
    pause
    stop sound3
    scene ch1ep4_103
    with Dissolve(0.2)
    eg "We're all here! Go, go, go!"
    stop music fadeout 4
    stop sound fadeout 4
    stop sound2 fadeout 4
    play sound5 helicopter_inside loop fadein 2
    play sound4 dyinggasps loop
    $ renpy.music.set_volume(1.0, 1.0)
    $ renpy.sound.set_volume(1.0, 1.0)
    scene ch1ep4_104
    with dissolve
    pil "All elements on board. Silverbird 1 departing. RTB."
    scene ch1ep4_105
    with dissolve
    si "Five, you hear that? Everything's gonna be okay-we're going home!"
    scene ch1ep4_106
    with dissolve
    pause
    stop sound4 fadeout 2
    scene ch1ep4_107
    with Dissolve(2.0)
    pause
    scene ch1ep4_108
    with Dissolve(0.2)
    si "No, no, no! Don't you dare, Five! You can't leave us like that!"
    si "You can't leave me!"
    scene ch1ep4_109
    with dissolve
    si "Hng! Hng! Hng! Come on, Five!"
    scene ch1ep4_110
    with dissolve
    pause
    scene ch1ep4_111
    with dissolve
    eg "*shaking her head*"
    scene ch1ep4_112
    with dissolve
    eg "Six, he's..."
    si "NO! He's gonna be okay, you'll see!"
    play sound bodyfall2
    scene ch1ep4_113
    eg "Six! He's dead! Your cries will not bring him back! It's over!"
    eg "We prepared ourselves for moments like this! You need to accept it! You need to accept it NOW!"
    scene ch1ep4_114
    with dissolve
    si "*hics* He said... we would all go home together, Eight...! He said it...!"
    scene ch1ep4_113
    with dissolve
    eg "I know that, Six. But it was either you or him. He made his choice, so don't waste it."
    scene ch1ep4_115
    with Dissolve(1.0)
    pause
    scene ch1ep4_116
    with dissolve
    pause
    scene ch1ep4_117
    with Dissolve(1.0)
    pause
    play sound tinnitus fadein 3 loop
    stop sound5 fadeout 3
    scene ch1ep4_118
    with Dissolve(4.0)
    pause 1.0
    stop sound fadeout 4
    scene black
    with Dissolve(1.0)
    un "{size=-10}Moon."
    show screen day_sunday with dissolve
    scene ch1ep4_119
    with Dissolve(0.2)
    mc "Moon!"
    scene ch1ep4_120
    with Dissolve(0.2)
    m "Hm? Huh?"
    mc "Everything alright? You zoned out there for a bit."
    m "Ah, yeah, I'm fine. Just lost in thought for a moment."
    play music 'audio/NorthernLights.mp3'
    scene ch1ep4_121
    with dissolve
    a "Hold up, are you two coordinating this somehow?"
    a "Why does everything seem like it's unfolding exactly as you planned?"
    mc "Well, with the lack of direct communication, Hera's silence was a giveaway. It hinted she was concealing something crucial: something she couldn't share."
    mc "That led me to believe there's more to her past actions than meets the eye."
    mc "I've been anticipating this moment. She really took her sweet time."
    mc "Raiding her safe house? If I wanted revenge, I would've had bigger aspirations than that."
    mc "I'm checking off this part of our plan. With her backed into a corner, I knew she'd eventually spill the beans."
    scene ch1ep4_122
    with dissolve
    a "..."
    a "I see... Now that I think of it, it makes sense..."
    a "Having her power cut doesn't make her totally powerless. She could have done so much more..."
    scene ch1ep4_123
    with dissolve
    mc "On to our next move."
    mc "Em?"
    e "Mhm. It's about time you revisit your roots, Aine."
    a "..."
    scene ch1ep4_124
    with dissolve
    mc "Think you're up for it?"
    a "I'm the least of your worries, [mc]. The real question is, are you prepared? What's your plan from here?"
    mc "More prepared than ever. Nothing but to push forward and track down Jovian, for real this time."
    play sound closedoor
    scene ch1ep4_125
    with dissolve
    shu "Who's joining the expedition? Need any help? Just say the word."
    mc "Definitely need you on board, buddy. Especially since I'm not sure how long this will take."
    mc "Given your connections, you should reach out to Jess. Ask her to arrange for someone to watch over everyone here. Do it now if you can."
    shu "You got it, boss! I'll be back in a bit."
    play sound closedoor
    scene ch1ep4_126
    with dissolve
    mc "As for the team-"
    scene ch1ep4_127
    with Dissolve(0.2)
    k "Count me in."
    scene ch1ep4_128
    with dissolve
    k "Emma, how long will it take for you to obtain a search warrant?"
    e "Thankfully, this case has been open for a while already. If I have the necessary information, I can have the warrant authorized by tomorrow."
    k "Good. After this, come to my room. I have a few things to discuss with you."
    scene ch1ep4_129
    with dissolve
    mc "Klara, you sure about this?"
    k "No question, [mc]. I've been on the sidelines too long. It's about time I step up."
    k "Needless to say, I'm the only one who knows where that place Hera mentioned is."
    mc "I see... She mentioned that one of us knows the location. So it's you."
    k "Yes. It's where Jovian and I temporarily stayed long ago."
    k "You asked me to lay low, but I can't sit idly when it comes to Jovian. If he's out there, I want first dibs to acquaint my palm with his face."
    mc "*sighs*"
    mc "I doubt a confrontation will solve everything, but I'll make sure you'll get that chance."
    scene ch1ep4_130
    with dissolve
    mc "And for the others, I think it's pretty clear."
    mc "Moon..."
    mc "And Emma..."
    mc "You're with me."
    e "Of course."
    m "Absolutely."
    mc "Gwen, Aine, I'll leave you in charge of everything and everyone else for the time being."
    g "You got it."
    scene ch1ep4_131
    with dissolve
    mc "Alright, we should head out-"
    scene ch1ep4_132
    with Dissolve(0.2)
    m "Wait, [mc]."
    mc "Moon?"
    m "I think we should wait until tomorrow to head out, no? We all need a good night's rest."
    mc "... You read my mind or something?"
    m "Not exactly. But I know we've all been preparing for this. However, facing what's ahead requires us at our best, which means being well-rested."
    mc "I..."
    scene ch1ep4_133
    with dissolve
    mc "... Yeah, you're right. It's a lot to process for all of us."
    m "Exactly. Let's give ourselves the best chance by starting fresh tomorrow. We've waited this long; one more night won't hurt."
    mc "Thanks, Moon."
    scene ch1ep4_134
    with dissolve
    mc "Okay, everyone, let's rest up. Tomorrow, we move."
    scene ch1ep4_135
    with dissolve
    s "..."
    stop music fadeout 2

    if allornothingroute:
        scene black
        with dissolve
        with fade

        play sound chair
        scene ch1ep4_163
        with hpunch
        mc "Ah, fuck... I can't sleep..."
        scene ch1ep4_164
        with dissolve
        mc "What time is it?"
        mc "..."
        play sound cloth
        scene ch1ep4_165
        with dissolve
        mc "Man... already midnight."
        mc "I told myself I was ready, but the pressure is too much."
        mc "So many questions, and the answers are within my reach. I can't stop thinking."
        mc "How—no, I have to stop spiraling. For everyone's sake."
        scene ch1ep4_166
        with dissolve
        mc "*sighs* Alright, calm down, [mc]. Clear your mind and remember what Lily taught you."
        mc "... Which was what again?"
        play sound closedoor
        scene ch1ep4_168
        with dissolve
        s "..."
        scene ch1ep4_167
        with dissolve
        s "I knew he would have trouble sleeping..."
        play sound doorknock
        scene ch1ep4_169
        with dissolve
        mc "... Hm?"
        yt "Who could it be at this hour?"
        s "[mc], are you still awake in there?"
        yt "Sky, of course. She always seems to sense when I'm under stress."
        mc "Sky? Why are you awake right now?"
        s "I had to use the bathroom and heard you after I was done."
        s "But enough about me. Are you okay?"
        mc "Yeah, don't worry about me. Just having a bit of trouble falling asleep is all."
        s "Are you sure? You know I'm always here for you if you need someone to talk to."
        mc "I appreciate that, Sky. But it's really nothing to worry about."
        mc "I'll be fine on my own. You can go back to bed."
        play sound opendoor
        scene ch1ep4_170
        with dissolve
        s "Are you sure about that? Because you sound like your thoughts are running wild with worries. Maybe talking about things will help ease your mind."
        mc "*sighs* I don't want to burden you with my problems, Sky. As much as I'd love ask for help, I can't get you involved in this."
        play sound chair
        scene ch1ep4_171
        with dissolve
        s "{i}Your{/i} problem? No, [mc]. I know I haven't said much about Dad, but that's because I trust you."
        s "Any problem related to us is my problem too, you know?"
        scene ch1ep4_172
        with dissolve
        s "I will never be as strong as Moon, as quick-witted as Aine, or as smart as Emma. I hate to say it, but... comforting you is all I can do."
        s "So don't take this away from me, please? Let me be here for you."
        mc "..."
        scene ch1ep4_173
        with dissolve
        mc "Alright... I guess it wouldn't hurt to get some things off my chest."
        label skystressrelief:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ch1ep4_174
        with Dissolve(0.2)
        s "Pff...! I already know what's bothering you, stupid. There's no need to tell me."
        play music 'audio/HoneySky.mp3' fadein 2
        scene ch1ep4_175
        with dissolve
        s "However, sharing a more {i}intimate{/i} moment with someone can also help alleviate stress."
        s "And since we haven't done anything in a while..."
        mc "Ahh, of course. I know what you're getting at."
        scene ch1ep4_176
        with dissolve
        s "*giggles* Do you? Well, of course you do."
        s "It could be a fun and pleasurable way to help you relax. Emphasis on {i}pleasurable{/i}."
        s "Plus, I must admit I've been craving your attention too. It's been a long time, after all."
        s "{size=-10}Four updates without even a sniff of [mc]'s meat... What kind of torture-loving developer does that?"
        mc "Sorry, I didn't catch the last part. What was that?"
        s "Hmm? Oh, nothing. Just wanted to know if you were on board with the idea."
        scene ch1ep4_177
        with dissolve
        mc "I see... Are you sure about this? I mean, I don't want you to feel like you have to do it just because I'm going through a rough patch."
        s "[mc], I wouldn't have suggested it if I didn't want it too. Trust me, it would be mutually beneficial for both of us."
        s "You get some stress relief and something to tire you out, and I get my sausage—I mean a stronger connection with you."
        s "So, what do you say? Want to take me up on this exclusive offer?"
        menu:
            "Relieve your stress with Sky":
                mc "You know what? That sounds absolutely perfect right now."
                mc "But everyone's sleeping, so we'll have to stay quiet and make it quick."
                play sound cloth
                scene ch1ep4_178
                with dissolve
                s "Don't worry, [mc]..."
                "As always, Sky seems to anticipate what you were thinking perfectly."
                s "I'm way ahead of you."
                "And as always, she's very eager to get things started."
                mc "Glad to see we're still always on the same page."
                scene ch1ep4_179
                with dissolve
                "You strip off your sleepwear, then grab her waist."
                s "Eep!"
                "Sky lets out a small yelp, equal parts surprise and excitement, as you pull her towards you."
                scene ch1ep4_180
                with dissolve
                "You kiss her deeply: your way of apologizing for neglecting her for so long."
                "However, though she briefly reciprocates the kiss, she just as quickly pushes you back."
                scene ch1ep4_181
                with dissolve
                s "[mc]... As much as I'd love to go through all the fancy foreplay, that wouldn't exactly make things quick, would it?"
                mc "Oops... yeah, you're right. My bad."
                mc "It's just that this body makes it so easy for me to get carried away..."
                scene ch1ep4_182
                with dissolve
                "You trace your hands along her body, starting from the curves of her bosom and down her sides, before resting them on her plump butt."
                mc "But since you're clearly better at staying focused than I am, what do you propose we do next?"
                s "Well, I've always wanted to know how a certain position felt..."
                mc "Mm? What kind of position?"
                s "Nu-uh. I'm not going to give you the answer that easily. You can't just expect me to do all the work here!"
                "Intrigued, you raise your eyebrow and give her a curious smirk."
                mc "Okay, but at least give me a hint, will you?"
                "Sky rolls her eyes at you, but she can't hide the excitement and playfulness in her smile."
                s "Fine. Looks like the thick {i}walls{/i} of your skull can't figure out what I'm {i}pushing{/i} for."
                mc "Say no more."
                play sound chair
                scene ch1ep4_183
                with dissolve
                "You pick Sky up and walk towards the wall."
                mc "Can't have you do all the work, right, my little ragdoll?"
                s "*giggles* Ragdoll? That's a new one."
                mc "What? You don't like it?"
                scene ch1ep4_184
                with dissolve
                "You place her down once you feel your hands brush against the cool wall."
                s "I never said that. Perhaps I like being your personal sex doll, [mc]..."
                "Maybe it shouldn't be the case, but hearing those words makes your dick even hungrier to \"relieve your stress\" with Sky."
                mc "I will keep that in mind..."
                scene ch1ep4_185
                with dissolve
                "Sky giggles at your response, but then adopts a serious, inquisitive expression."
                s "You're on the right track, but standing against this wall isn't what I had in mind."
                mc "You don't say?"
                s "Mhm."
                mc "Then maybe I should raise another question."
                scene ch1ep4_186
                with dissolve
                "You lift her leg, pressing your firm cock against her abdomen."
                "Your balls brush against her shaven mound, causing your dick to throb in anticipation."
                mc "Am I getting {i}warmer{/i}?"
                "You feel Sky's nipples rise against your skin as her arousal begins to build."
                s "Definitely... but only halfway there?"
                mc "Oh, only halfway? Really?"
                "You can't hide your astonishment at what her words imply. Does this girl really want to be fucked completely off the ground?"
                scene ch1ep4_187
                with dissolve
                s "I didn't stutter, [mc]. All that working out should mean that it won't be too difficult for a big, strong man like you to hold little old me up, right?"
                mc "I—no, it won't be, but what will you use to support yourself?"
                "Sky chuckles at your utter disbelief."
                s "[mc], don't you remember I did gymnastics for basically my entire childhood? Balancing myself against this wall will be a piece of cake compared to my practices."
                s "And I read that this position lets you reach deeper, so I figured it was worth a try."
                mc "So you've been researching sex this whole time? Sky, how would Klara feel if she found out?"
                s "Hey, guys aren't the only ones who are curious about sex! Besides, I had to do something to relieve the stress that grading all those exams brought on..."
                mc "Is that how you knew that this would help me with my worries?"
                scene ch1ep4_186
                with dissolve
                s "Maybe... but again, you're talking too much!"
                s "Lift me up, stick it in there, and let's get this show on the road!"
                mc "Just like that? Are you sure it won't hurt?"
                s "[mc]. It's not the first time we've done it with each other. Also, it's not like I'm an older woman like Mom who requires a lot of warmups."
                mc "I don't think it's a good idea to talk about Klara during a time like this..."
                s "Do you want to worry about her, or do you want stress relief?"
                "Perhaps you're overthinking things. Perhaps everyone would be happier if you just give the lady what she wants."
                mc "I want the stress relief."
                show sky32
                with dissolve
                "Without further ado, you pick both of Sky's legs up and push yourself in."
                s "Yeeesss!! F-finally!"
                "Sky's dampened pussy takes you in with ease, welcoming your member back with a warm embrace."
                "You begin to move your pelvis back and forth against hers, building up a steady rhythm."
                s "Ngh~~"
                "True to her words, Sky shows no signs of discomfort."
                "In fact, whether due to the no-cock dry spell or her own youthful libido, she almost immediately begins to emit sounds of pleasure."
                s "Ngh... that feels... amazing..."
                s "It really feels like... you're going so deep!"
                "You look down, and sure enough, you're burrowing your cock inside of her vagina almost down to the base."
                mc "I can't lie... it feels good for me too."
                s "*giggles* I'm s-sure it does, [mc]."
                "You continue grinding against her, amazed at how she's able to hold the position while having a piston driven in between her legs every second."
                "Despite all your movement, she keeps her upper body and torso almost perfectly still."
                "Almost as if she is doing everything in her power to stay in the perfect receiving position for your cock."
                s "Mmh... aahhhh...!"
                "Even as her pleasure increases, she holds steady, her vagina remaining in the prime location to receive your full length."
                "It seems she's content to let you do the dirty work, but you're not complaining."
                "In fact, the arousal is building quickly for you as well."
                s "Mmh... faster, [mc]!"
                mc "Faster? But won't w-we make too much n-noise then? Your moans are practically screams already!"
                s "Nghh... hmmm...!"
                "In between moans, Sky seemingly pauses to think."
                s "Okay! Then mmgh~... c-cover my mouth!"
                mc "C-cover your mouth? B-but I'm already h-holding up your legs!"
                s "Just g-go for it! I'll w-wrap my legs around you!"
                s "B-brace your other hand a-against the w-wall if you need to!"
                show sky33
                with dissolve
                hide sky32
                "Despite your doubts, you now know better than to question Sky's capabilities."
                "You let go of her legs, clasping your right hand over her mouth."
                "You push your left hand against the wall, using it as a counterbalance."
                "Sure enough, Sky stays upright, this time encircling her thighs around your pelvic girdle."
                "She locks her ankles behind your back, forming a vice grip around your hips."
                "You start to move again, this time with more gusto."
                mc "F-fuck!"
                "You shout at the sudden surge of pleasure coming from your dick."
                s "Ngh~! Shhh! Q-quier, rumhmbrr?"
                "Sky scolds you through your hand, making you catch your slip-up."
                mc "S-sorry! Quick and quiet, right."
                "Quiet being a relative term, of course. The noise of her wet pussy gushing against your cock, and the sound of your hips slamming against her, echo in your room."
                "If anyone was standing outside your door, they would know exactly what was happening right now."
                "But thankfully, it's just you two on this floor. Well, you two and Gwen, but she's totally cool with this."
                "But back to the task at hand: stress relief with Sky."
                s "Mmhhh!! Nghhh!!"
                yt "Damn, even through my fingers, Sky's moans sound just like they normally do."
                yt "It makes me wonder how they'd sound like unmuffled... but I'm not stupid enough to find out."
                yt "Maybe next time. For now, just gonna enjoy Sky's amazing idea to relieve some anxiety."
                "As the pleasure continues growing, you find yourself biting your lip to keep from making too much noise yourself."
                "Also, it turns out that Sky's research was wrong: this position is the deepest you could possibly drive yourself into her."
                "When you look down, you see your penis fully disappear in between her labia, only to emerge re-coated with her fluids over and over again."
                s "Ghmmm!!! Hngghh!!!"
                "Sky's eyes begin to roll back, a sign that she's closing in on her climax."
                "The pleasure is mounting for you as well, your balls preparing to fill Sky up to the brim."
                play sound bodyfall2
                scene ch1ep4_188
                with hpunch
                s "HMMMM!!!"
                "With a final muffled scream, Sky's pussy twitches against your cock while it is buried fully inside."
                "Your dick receives a full-body massage, courtesy of the smooth muscle cells of her vaginal walls."
                "Her legs squeeze around your waist, drawing you closer to her than you thought was humanly possible."
                "With that, your hips involuntarily spasm forward, helping you shoot your load deep into her pussy as you orgasm with her."
                mc "Hrrmmhh!!"
                "You continue to bury your cum into the deepest parts of her womanhood, soon causing the overflow to drip onto your lap as you both finish climaxing."
                scene ch1ep4_189
                with dissolve
                "You pull out your dick, now flaccid and covered in mixed cum."
                mc "That... that was... something else, Sky."
                s "I... I had a feeling... it would be... *laughs*..."
                scene ch1ep4_190
                with dissolve
                "Sky puts her hand on your shoulder, bracing herself as she lowers her legs back onto the ground." 
                s "W-wow..."
                "She grimaces slightly, still holding your shoulder as she tries to regain her balance."
                mc "What's wrong?"
                s "Normally I can't... feel my legs... when we finish... but this..."
                s "This is... a new level... of jelly legs..."
                scene ch1ep4_191
                with dissolve
                mc "Guess no amount of gymnastics training could've prepared you for that, right?"
                "You laugh as you carry her over to the bed, laying her down gently."
                play sound cloth
                scene ch1ep4_192
                with dissolve
                "As she smiles sincerely at you, you smile back and plant a kiss on her forehead."
                image skmcsbms:
                    "ch1ep4_193.jpg"
                    pause 3.0
                    "ch1ep4_194.jpg"
                    pause .2
                    repeat
                show skmcsbms
                with dissolve
                mc "Thank you, Sky. This was exactly what I needed."
                s "Thank you for going along with it, [mc]."
                mc "Really, I mean it. You always seem to know exactly how to make my worries go away."
                mc "Whether it's a soothing melody, a comforting embrace, or something more... mature, you've saved me from myself more times than I can remember."
                mc "So even though you might not feel you're as quick-witted, smart, or strong as the others, that doesn't mean you're any less precious to me."
                mc "The bond we have is special, something that I can never have with any of the other girls."
                "Despite her fatigue, Sky gives you a loving smile, with tears beginning to dot the corners of her eyes."
                s "Thank you, [mc]. I needed to hear that."
                mc "It's all true. You know, maybe I should be stressed in the middle of the night more often so we can continue having moments like that."
                s "*giggles* Maybe..."
                mc "So thank you again, Sky. You'll always have a place in my heart."
                s "And you will always have one in mine."
                s "Mind if I stay here for the night? I'd love to be with you for a little longer. And on top of that, my legs are in no condition to walk."
                yt "Thank god Aine isn't sleeping here tonight..."
                mc "*chuckles* I'd like that."
                s "Great! Now, come here so we can cuddle just like old times."
                mc "In a minute. I need to clean myself up first."
                s "Fine, fine."
                stop music fadeout 4
                play sound opendoor
                scene ch1ep4_195
                with dissolve
                pause
                yt "Yeah, no, abort! Abort!"
                play sound closedoor
                scene ch1ep4_196
                with dissolve
                s "What's wrong, [mc]?"
                mc "Klara's coming up the stairs! Get dressed, quick!"
                play sound opendoor
                scene ch1ep4_197
                with dissolve
                pause
                scene ch1ep4_198
                with dissolve
                k "Oh... I guess Sky went to comfort him. What was all that thudding I heard, then?"
                play sound closedoor
                scene ch1ep4_199
                with dissolve
                s "Is she gone?"
                mc "Yeah, we're good."
                scene ch1ep4_200
                with dissolve
                yt "*sighs* How do we even start to tell her about all this?"
                yt "It's not just about Sky: I've been fucking every single woman in this house!"
                yt "Well... except for her..."
                mc "..."
                scene ch1ep4_201
                with dissolve
                yt "Huh?! You deranged asshole, don't even think about it!"
            "Try to fall asleep on your own":
                mc "As tempting as that sounds, I'm just not really feeling it right now, Sky. I'm sorry."
                scene ch1ep4_202
                with dissolve
                s "Oh... well, it's okay, I understand."
                mc "It's not that I don't want to, it's just not the right time."
                s "Don't worry, [mc]. I know you're dealing with a lot right now."
                scene ch1ep4_177
                with dissolve
                s "But don't think I'm letting you off the hook that easily!"
                s "{size=-10}Next time, you'll have to fuck me twice as hard."
                mc "Say that again?"
                s "I said next time, you'll have to take me somewhere nice where it's just the two of us!"
                mc "*chuckles* Fine, you have a deal!"
                s "Good night, [mc]. Promise me you'll try not to worry too much?"
                mc "I'll do my very best. Good night, Sky."
        $ renpy.end_replay()
    stop music fadeout 4
    call hide_days from _call_hide_days_21
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_monday with dissolve
    play sound cityalley loop
    scene ch1ep4_136
    with dissolve
    y "... Are you sure?"
    nic "Well, yeah. Pantyhose with sneakers aren't my taste, but that looks good on you."
    play sound2 closedoor
    scene ch1ep4_137
    with dissolve
    mc "Who-?"
    scene ch1ep4_138
    with dissolve
    mc "Oh, it's you guys... from before."
    nic "Hey there! We did run into each other previously but never got around to proper introductions."
    scene ch1ep4_139
    with dissolve
    nic "I'm Nicole, Nicole Fitzcharles."
    nic "And this is Yuna."
    stop sound fadeout 6
    play music 'audio/CrystalGloom.mp3'
    scene ch1ep4_140
    with dissolve
    mc "Fitzcharles?"
    mc "Wait, you're that-!"
    nic "Yep, that's me. But let's keep that under wraps for now, okay?"
    nic "Carrying that name comes with its burdens. We'd really appreciate being treated like anyone else, if you don't mind."
    scene ch1ep4_141
    with dissolve
    mc "Got it, no problem at all. I was just a bit surprised is all."
    mc "So, you're here to look after everyone while we're away?"
    nic "Exactly, Jess sent us. I'm part of the Intelligence Department, and Yuna here is one of our best mercenaries."
    nic "You can count on us to keep everyone safe while you handle your business."
    scene ch1ep4_142
    with dissolve
    yt "Their actual roles in this city are still a mystery to me..."
    scene ch1ep4_143
    with dissolve
    yt "But... I can confirm that these two are actual monsters..."
    yt "Treat them like just anybody else? How can I do that if I feel like they could slit my throat at any moment?"
    scene ch1ep4_144
    with dissolve
    yt "I can ignore the one with the hatchet and short sword, but this silver-haired woman..."
    yt "For someone hiding her identity, that introduction was intentional... An intimidation display, or so they say."
    yt "I know we've been looking at each other all this time, but her gaze has always been below mine..."
    yt "Do people around her notice this at all? Such intense pressure..."
    stop music fadeout 4
    play sound cityalley fadein 4 loop
    scene ch1ep4_145
    with dissolve
    mc "Anyway, I'm [mc]. I appreciate you two stepping in to help."
    nic "Happy to. Just a heads-up, though."
    scene ch1ep4_146
    with dissolve
    mc "Hm?"
    nic "This is a paid gig for us. Jess will be deducting it from your salary."
    mc "*sighs* Should've seen that coming."
    nic "*laughs* Don't sweat it; we're not charging an arm and a leg."
    nic "Jess might be a friend, but she's all business at the end of the day. Some things never change."
    mc "Sounds about right."
    play sound2 closedoor
    scene ch1ep4_147
    with dissolve
    nic "Oh, hey there, Fang!"
    m "'Sup."
    scene ch1ep4_148
    with dissolve
    y "..."
    scene ch1ep4_149
    with dissolve
    m "..."
    nic "Oh?"
    scene ch1ep4_150
    with dissolve
    y "Are you happy?"
    scene ch1ep4_151
    with dissolve
    m "Yes."
    scene ch1ep4_150
    with dissolve
    y "Good."
    scene ch1ep4_152
    with dissolve
    nic "You two might just set a world record for the least words used in a conversation."
    nic "It's been a while, why not loosen up a bit?"
    y "That's unnecessary. A warrior's silence speaks louder than words..."
    m "... For each action carves fate, while unnecessary words are but whispers lost to the wind."
    y "Glad that's still your mantra."
    m "Always."
    play sound2 closedoor
    scene ch1ep4_153
    with dissolve
    k "Are these our guests?"
    nic "Good morning, Miss Hahn."
    y "Good morning."
    mc "They're going to keep an eye on things while we're gone."
    scene ch1ep4_154
    with dissolve
    k "Thanks. I trust you'll keep everyone safe."
    nic "Absolutely, Miss Hahn. We never fail to deliver."
    scene ch1ep4_155
    with dissolve
    k "I noticed you've been on your feet for a while. Please, feel free to come in for refreshments."
    nic "We appreciate it, but we'll stay on guard out here for as long as needed."
    scene ch1ep4_156
    with dissolve
    mc "Ready to get going?"
    k "*taking a deep breath*"
    scene ch1ep4_157
    with dissolve
    k "Yes, let's go."
    scene ch1ep4_158
    with dissolve
    mc "..."
    m "..."
    scene ch1ep4_159
    with dissolve
    pause
    scene ch1ep4_160
    with dissolve
    m "... Just so you know, if even one person gets hurt, that's enough reason for me to kill you."
    nic "Feel free to if that happens. But trust us, it won't come to that."
    play sound2 waterphone
    show ch1ep4_161
    nic "If anything... who do you take us for, Ha-Jeong Lee?"
    m "Your blood doesn't scare me, Fitzcharles. You're just a weak and sane version of Owl."
    scene ch1ep4_162
    with Dissolve(0.2)
    nic "Am I not that intimidating anymore? Have I lost my edge?"
    y "... I don't know, I just got here."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound carmoving loop
    scene ch1ep4_203
    with dissolve
    pause
    stop sound fadeout 2
    play sound2 cardriveinterior fadein 2 loop
    scene ch1ep4_204
    with dissolve
    mc "So, what's with the outfit?"
    k "..."
    mc "Klara?"
    scene ch1ep4_205
    with dissolve
    k "Oh, uhh..."
    k "Well... I just wanted to feel more like myself today."
    mc "And what's been stopping you lately?"
    scene ch1ep4_206
    with dissolve
    k "Aside from acting like my age, I feel like I should present myself in a certain way, as someone respectable in everyone's eyes."
    menu:
        "Understandable":
            mc "That's totally understandable."
        "It's not an issue":
            $ klarapoint += 1
            $ renpy.notify(klaranotif)
            mc "Honestly, it's not every day that I see you in that kind of clothing, but I don't see it being an issue."
            mc "You look great, and it really suits you."
            scene ch1ep4_207
            with dissolve
            mc "Right, Em?"
            e "Yeah, it does make you look younger, Miss Klara."
            k "*laughs* Thanks, you two. I appreciate it."
    
    play music 'audio/ParticleEmission.mp3' fadein 2
    scene ch1ep4_208
    with dissolve
    mc "Speaking of someone with clothing issues, how's she doing?"
    e "She's fine, but she knocked out ten minutes after we hit the road."
    scene ch1ep4_209
    with dissolve
    mc "Seems I wasn't the only one struggling to sleep last night. It's nice to see you two bonding, though."
    e "It's not like I've warmed up to her."
    scene ch1ep4_210
    with dissolve
    k "You're not still at odds, are you?"
    e "No, it's not that. She's just unpredictable in ways that I can't understand."
    e "Not only her actions, but especially with the way she talks and address matters."
    e "It feels like she's incomplete as a person, but at the same time, she's whole, more than any other person I've met."
    e "... I don't get it, I can't read her, and it bothers me."
    scene ch1ep4_211
    with dissolve
    mc "Can't blame you. She has been acting odd lately."
    e "In what way?"
    mc "There's this unexplainable connection between us. It's hard to describe."
    k "Can you elaborate on that?"
    scene ch1ep4_212
    with dissolve
    mc "Imagine you're walking on a straight path, eyes wide open. Then suddenly, you're walking with your eyes shut."
    e "That analogy doesn't really hold up..."
    mc "Just go with it for a second. What would you do? How would you feel?"
    scene ch1ep4_213
    with dissolve
    k "Well, I'd keep walking since I know the path, but closing my eyes would make me uneasy."
    mc "What if now, you can open your eyes?"
    k "In that case, I will feel a tremendous amount of relief knowing that I can see again."
    mc "Exactly my point."
    mc "You know you've been living your whole life, all well and all things considered. But then, a huge part of you opened up, something you didn't know existed."
    mc "That's the kind of unsettling feeling I get around her."
    e "Sounds like basic human instinct to me..."
    scene ch1ep4_214
    with dissolve
    mc "It might be, but for two people who've only recently met, it's odd to establish such a connection so quickly."
    mc "I just wish I could figure out what it means."
    k "Maybe it's not something to puzzle over, but to be grateful for. It might be exactly what you both need."
    mc "Hope you're right. It's been perplexing, to say the least."
    stop music fadeout 2
    if allornothingroute:
        scene ch1ep4_215
        with dissolve
        e "..."
        yt "Uh-oh... Looks like I hit a nerve. Forgot she's the type to get jealous."

    scene ch1ep4_216
    with dissolve
    mc "Changing topics, how did you come to know about this place?"
    k "Jovian and I lived there briefly before we settled in Golden City. It's owned by the Winters, a married couple."
    k "They'd better remember me. I've been there a couple of times, and got denied every single time."
    k "Now, it makes sense they're hiding something from me."
    scene ch1ep4_217
    with dissolve
    mc "Point us in the right direction, then."
    k "It's still a few hours' drive from here. Are you sure you want to keep on the wheels?"
    mc "Absolutely. I got this."
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade
    
    play sound curtain
    scene ch1ep4_218
    with dissolve
    ew "Love, they're here again."
    tw "Who?"
    ew "His family."
    tw "I see..."
    play music 'audio/DevilsDoorstep.mp3'
    scene ch1ep4_219
    with dissolve
    e "Let me handle this. Don't do anything unless I say so."
    play sound doorbell
    scene ch1ep4_220
    with dissolve
    pause
    play sound2 opendoor
    scene ch1ep4_221
    with dissolve
    ew "Yes?"
    scene ch1ep4_222
    with Dissolve(0.2)
    k "Good morning, Mrs. Winters. It's been a while."
    scene ch1ep4_223
    with dissolve
    ew "*laughs* Oh, Klara? Y-yes, it has been a while!"
    scene ch1ep4_224
    with Dissolve(0.2)
    e "Good morning. Are you Eudora Winters?"
    ew "Yes, that's me. And who are you?"
    play sound cloth
    scene ch1ep4_225
    with Dissolve(0.2)
    e "I'm Detective Meyer. I'm here for an ongoing investigation."
    e "I have a search warrant authorized by the court to search your house."
    scene ch1ep4_226
    with dissolve
    e "Here's the paperwork."
    ew "..."
    scene ch1ep4_227
    with dissolve
    ew "I see. Well, if it's all correct, then... you have the right. May I ask what you're looking for?"
    e "I can't share the investigation details right now, but we'll be quick and try not to disturb too much. Thank you for cooperating."
    play sound shotgun_rechamber
    scene ch1ep4_228 # shotgun sfx
    with Dissolve(0.2)
    pause
    scene ch1ep4_229
    with Dissolve(0.2)
    m "Shotgun. A military hand sign? How does she..."
    scene ch1ep4_230
    with dissolve
    k "You're not very good at {i}hiding{/i} that you're {i}hiding{/i} something, are you, Eudora?"
    ew "What do you mean-"
    scene ch1ep4_231
    tw "We're ending this curse right now!"
    play sound cloth2
    show ch1ep4_232
    mc "Em!"
    play sound2 bodyfall
    play sound3 bodyfall2
    play sound shotgun_shoot
    show ch1ep4_233
    with hpunch
    pause 0.8
    scene ch1ep4_234
    with Dissolve(0.1)
    e "Hold the wife down!"
    m "On it."
    play sound2 woosh2
    play sound running loop
    scene ch1ep4_235
    pause 0.5
    play sound shotgun_shoot
    scene ch1ep4_236
    with hpunch
    pause 0.5
    play sound2 cloth3
    scene ch1ep4_237
    pause 0.8
    play sound3 handcuff
    scene ch1ep4_238
    pause 0.7
    play sound bodyfall
    scene ch1ep4_239
    with hpunch
    pause 0.9
    play sound2 cloth2
    play sound3 handcuff
    scene ch1ep4_240
    e "You move, I shoot. Up to you."
    scene ch1ep4_241
    with dissolve
    m "Please don't move. I don't want to hurt you."
    scene ch1ep4_242
    with dissolve
    mc "W...well... that's one way to say \"welcome\"..."
    scene ch1ep4_243
    with dissolve
    tw "You cursed people! You're not welcome here! Leave our house, now!"
    ew "L-let my husband go! You have my cooperation, I promise you! Just don't hurt him!"
    scene ch1ep4_244
    with dissolve
    k "We came in peace, Eudora. But it seems that sentiment isn't mutual after what your husband did."
    k "You know why we're here, right?"
    ew "I don't know what you're talking about-"
    k "Denying it will just make things harder for you."
    scene ch1ep4_245
    with dissolve
    k "If we've caused you trouble, I'm truly sorry. But you're not the only one who's suffered because of him."
    k "So, please... I'm asking you. Tell us where he is."
    scene ch1ep4_246
    with dissolve
    ew "..."
    tw "Don't tell them anything, Love! We promised him!" with hpunch
    scene ch1ep4_247
    with dissolve
    ew "Enough, Thaddeus..."
    ew "It's time. We've hidden this for too long."
    ew "We deserve peace, and so do they."
    scene ch1ep4_248
    with dissolve
    k "That's right."
    ew "Help me up. I have something to show you."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound closedoor
    play music 'audio/Introspection.mp3'
    scene ch1ep4_249
    with dissolve
    k "This is... the house where we both stayed back then..."
    scene ch1ep4_250
    with dissolve
    k "And he's here?"
    ew "..."
    k "Eudora?"
    scene ch1ep4_251
    with dissolve
    ew "All your questions will be answered soon."
    mc "This isn't a trap, is it?"
    ew "I understand your concerns, but my husband's actions were solely in our defense."
    mc "To defend you from what? He was the one who made things worse, not us."
    scene ch1ep4_252
    with dissolve
    ew "Please, follow me."
    scene black
    with dissolve
    scene ch1ep4_253
    with dissolve
    ew "This is the room where he used to stay."
    k "Used to?"
    scene ch1ep4_254
    with dissolve
    pause
    scene ch1ep4_255
    with dissolve
    e "Open this."
    ew "Good instincts, Detective. But you don't have to tell me."
    play sound safedial
    scene ch1ep4_256
    with dissolve
    pause
    scene ch1ep4_257
    with dissolve
    m "Commander, this place makes me uncomfortable."
    mc "Yeah, something's seemed off since we got here. Glad it's not just me feeling it."
    play sound camcorder_movement
    scene ch1ep4_258
    with dissolve
    ew "Here."
    k "This is..."
    mc "Should this look familiar to me?"
    k "I'm not sure I'm ready for what's inside..."
    scene ch1ep4_259
    with dissolve
    k "[mc], would you please?"
    scene ch1ep4_260
    with dissolve
    mc "..."
    scene ch1ep4_261
    with dissolve
    mc "Yeah... let's see what's in it."
    ew "Let's head to the living room."

    scene black
    with dissolve
    with fadeq

    play sound chair
    scene ch1ep4_262
    with dissolve
    mc "You sure you don't want to watch this?"
    k "... You go ahead. I'll still be able to hear it from here."
    mc "..."
    stop music fadeout 2
    play sound camcorder_movement
    play sound2 camcorder_fastforward loop
    scene ch1ep4_263
    with dissolve
    pause
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_264
    k "Really? You actually went and got it?"
    scene ch1ep4_265
    with dissolve
    play music 'audio/Hopefully.mp3'
    jov "Hey, don't give me a hard time. You know I've been wanting one."
    play sound woodhit
    show ch1ep4_266
    with hpunch
    k "Ah, [mc]! Don't do that!"
    scene ch1ep4_267
    with dissolve
    jov "So, I got this camcorder... and, uh..."
    jov "... I'm not really sure why I'm doing this..."
    scene ch1ep4_268
    with dissolve
    jov "I'm thinking about capturing all the moments that matter to us. The everyday stuff, the laughs, the trips out."
    jov "Maybe someday, someone will find these videos and see a bit of our lives."
    jov "Today, it's just enjoying the little things—like how much [mc] means to us. Even if he's not our son."
    scene ch1ep4_269
    with dissolve
    k "That was a few months after you came into our lives."
    k "Jovian finally got his camcorder and started recording. Well, at least he tried to."
    mc "I see..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_270
    jov "Wha-ohh, woops..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_271
    jov "It's been a while since I last touched this thing. Life's been... well, a bit of a whirlwind—work and everything else."
    jov "Oh, right! Klara finally gave birth to Sky."
    jov "She's been with us for a year now, and she's always trailing behind [mc]. Those two are practically inseparable. It's the sweetest thing."
    play sound doorslam2
    scene ch1ep4_272
    k "Can you put the camera down for a bit? You've been staring at that thing all day!"
    k "Sky needs you, and I need help in the kitchen, too!"
    jov "Okay, okay, just a sec!"
    scene ch1ep4_273
    with dissolve
    jov "Guess I need to wrap this up. I'll record more later, promise."
    play sound thud2
    show ch1ep4_274
    with hpunch
    jov "Oh, [mc], no, don't touch that!"
    jov "Oops, duty calls!"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_275
    k "Awww! Aren't they adorable?"
    jov "Here we are, [mc] trying to teach Sky to walk. He's barely got it down himself, but he's so eager to help her."
    jov "Their laughter, their games are full of love."
    scene ch1ep4_276
    with dissolve
    jov "Watching [mc] help Sky, and her looking up to him like he's a superhero—it's perfect."
    jov "Capturing these moments feels like I'm keeping something precious forever."
    jov "I just hope we can keep these good times going..."
    stop music fadeout 4
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_277
    play music2 'audio/Rosee.mp3' fadein 4
    jov "This entry's hard... [mc]'s been feeling sick... a lot..."
    jov "The coughing doesn't stop, and it's not just a regular cold..."
    jov "He's also been clumsy, tripping over nothing, which isn't like him..."
    jov "And he looks pale, even though we've been outside a lot. It's got to be something more..."
    jov "You can tell, he's not his usual self..."
    scene ch1ep4_278
    with dissolve
    jov "It's hard seeing him try to keep up with Sky but get tired so quickly..."
    jov "He's frustrated because he can't keep going like she does..."
    jov "The nights are tougher. His coughing keeps us all up..."
    jov "I stay with him, holding his hand, until he falls asleep..."
    jov "Even in his sleep, he's restless..."
    jov "I keep hoping it'll get better, but deep down, I'm worried..."
    jov "We've got doctor appointments lined up. I'm trying to be strong for Klara and Sky, but I'm scared. What if..."
    jov "*sighs* I need to stop here..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_279
    jov "Everything has been nonstop, but we're most worried about [mc]'s health."
    jov "It's been a constant worry in the back of our minds."
    jov "Sky, being younger, is so energetic, always dragging [mc] into her adventures."
    jov "It's beautiful to see her trying to cheer him up, even if she doesn't fully understand. Their bond is the bright spot in all this."
    jov "On good days, [mc] is almost like his old self, laughing and playing with Sky."
    jov "But on bad days, he can't even get out of bed. Those days are tough on everyone."
    scene ch1ep4_280
    with dissolve
    jov "Explaining to Sky why [mc] can't play is heartbreaking."
    jov "But focusing on [mc] and Sky keeps us going. They remind us of what matters most."
    jov "We take it one day at a time, cherishing the good and staying strong through the bad."
    jov "It won't be easy, but with [mc] and Sky's light, we keep hope alive."
    jov "Yes, there's still hope in all this. I won't give up."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_281
    jov "The last few weeks have been hard. [mc]'s laughter, which used to fill our home, has gone quiet."
    jov "His energy is now constantly drained from fighting the disease."
    jov "He has been such a brave little soldier, but you can clearly see the toll that his fight has taken on him."
    scene ch1ep4_282
    with dissolve
    jov "On all of us, to be honest."
    jov "Sky tries to help in her own sweet way, comforting [mc] by using her little hands to stroke his back."
    jov "And Klara's been so strong for us, but I can see it's wearing on her."
    jov "If only I could find something, anything, to help [mc]..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_283
    jov "Jovian. Entry for April 6th, XXXX."
    jov "In my search for answers, I've explored every option, reaching out to old colleagues, even those whose research has ventured into... unconventional territories."
    jov "I've heard about new treatments, stuff that sounds almost too good to be true."
    jov "It's a long shot, but I'm willing to try anything."
    stop music2 fadeout 2
    scene ch1ep4_284
    with dissolve
    mc "{i}Unconventional territories{/i}...? What are you getting into?"
    scene ch1ep4_285
    with dissolve
    m "..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_286
    play music 'audio/DarkMind.mp3'
    jov "Entry for April 9th, XXXX. Seeing [mc] struggle to sleep tonight hit me hard."
    scene ch1ep4_287
    with dissolve
    jov "This isn't just fighting an illness anymore; it's a fight for our future. For [mc]'s future."
    jov "I'm ready to do anything, even make a deal with the devil himself, if it means giving him a chance."
    jov "Tomorrow, I'll meet up with Bonheur and his connections. He says he has something big, something that will make all of [mc]'s ailments go away."
    scene ch1ep4_288
    with dissolve
    jov "It's risky, but what choice do I have?"
    jov "I wish I could talk to Klara about it, but I can't. She'd stop me."
    jov "But I can't just watch [mc] suffer. I can't..."
    jov "What kind of man would I be if I just let [mc] die this slow, painful d-"
    jov "No, I can't think like that. I can't..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_289
    jov "Entry for April 10th, XXXX. Bonheur's offer is hanging over me, full of promise yet riddled with risk."
    jov "He talks about a \"universal cure\": something that would fix everything. But there's a catch."
    scene ch1ep4_290
    with dissolve
    jov "Be that as it may, we've run out of options. We've admitted [mc] to the hospital."
    jov "If only these doctors were the least bit competent... but they're proving useless day after day."
    jov "Looking into [mc]'s eyes, I know I have to be ready for whatever comes next."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep3p2_865
    jov "This is Jovian. Entry for April 12th, XXXX. It's [mc]'s second day in the hospital."
    scene ch1ep3p2_866
    with dissolve
    jov "The doctors... they've confirmed it. [mc], my little boy, just three years old, he's got a terminal brain tumor."
    jov "I couldn't... I couldn't just sit there and do nothing. So, I sought out Bonheur, a trusted friend, a brilliant mind, once known as a leading scientist."
    scene ch1ep3p2_867
    with dissolve
    jov "I pleaded with him, desperate for any cure, anything that could save [mc] from his cruel fate."
    scene ch1ep3p2_868
    with dissolve
    jov "And Bonheur... had something. A miracle drug, he called it. Claimed it could cure any illness."
    jov "But the cost... is being in debt to him, possibly for the rest of my life."
    jov "But what is debt compared to [mc]'s life? Even if he's not my blood, it doesn't matter. I love him like my own son."
    jov "I didn't hesitate, not for a second. I accepted it, all for [mc], to save him."
    scene ch1ep3p2_869
    with Dissolve(1.5)
    jov "This... this right here... is called the {i}\"Chimera Genesis Serum\"{/i}."
    jov "It seems this serum is... the future of warfare between the Glabia and Sha Crea territories."
    jov "In their longstanding conflict, Glabia plans to use it as a covert weapon."
    scene ch1ep4_291
    with dissolve
    jov "There, it's known by a rather cryptic name:"
    jov "... The {i}\"Numbers Serum\"{/i}." with Dissolve(2.0)
    scene ch1ep4_292
    with Dissolve(1.0)
    m "All the others were always created in pairs, like One and Two. My friends, Five and Six, then Seven and Eight."
    m "It always made me wonder... why was I the only one created alone? Why just me?"
    m "[mc]...you're...how..."
    scene ch1ep4_293
    with dissolve
    mc "I was too young to remember, and given my weak memory, I haven't a single clue... I guess we're about to find out."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_294
    jov "The hospital's too quiet at night: eerie, almost."
    jov "It's just me here, listening to the faint beeps of the machines, and [mc]'s breathing too lightly for comfort."
    jov "Here I am, holding what they call a miracle in a vial. My hands are shaking as I prep the syringe."
    jov "Never thought I'd find myself in a hero's shoes, especially like this."
    scene ch1ep4_295
    with dissolve
    jov "I keep looking over my shoulder, making sure we're still alone. This has to stay under wraps; the doctors can't find out."
    jov "I must do this, I must do this, I must do this... It's going to be okay..."
    jov "*taking a deep breath* I need to stay calm..."
    scene ch1ep4_296
    with dissolve
    jov "Now, injecting the serum..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_297
    jov "..."
    jov "...."
    scene ch1ep4_298
    with dissolve
    jov "Time check: it's eleven at night, [mc] is still unresponsive. I guess this is a waiting game."
    jov "I'm hoping for that miracle or bracing for the fallout of my choice."
    jov "Sinking back into my chair, I'll keep my eyes on [mc] as the night continues. No matter what happens next, I stand by my decision."
    jov "For better... or for worse..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_299
    jov "A few days after that night, [mc] woke up, seemingly out of nowhere."
    jov "Just like that, it was as if he had never been sick in the first place. It was a complete 180."
    jov "One minute we're steeling ourselves for the worst, and the next, he's sitting up in bed, wondering what's for breakfast like it was any normal day."
    jov "The doctors were stumped. They're throwing around the word \"miracle\" like it's going out of style. They don't have the faintest clue about what I did..."
    scene ch1ep4_300
    with dissolve
    jov "They wanted to run some tests on [mc], but I refused and had him discharged immediately."
    jov "There's no way I would let those imbeciles discover this ground-breaker."
    scene ch1ep4_301
    with dissolve
    jov "... Watching [mc] now, all energy and smiles, you'd never know how close we were to saying goodbye."
    jov "It feels like we've been given a second shot, though I'm still trying to wrap my head around the price."
    jov "But right now, seeing him running around, all that worry and uncertainty just melts away."
    jov "I'm under no illusions about this serum or what I agreed to with Bonheur. There's gonna be a price to pay, no doubt about it."
    jov "But for now, I'm just soaking in the gratitude."
    jov "Fully grateful for [mc]'s laughter echoing through the house, for his bright eyes smiling back at me."
    scene ch1ep4_302
    with dissolve
    jov "I didn't record this as some sort of confession. It's just proof of how far I'm willing to go for him."
    jov "Someday, I might find the guts to lay all this out for [mc] and explain the whole story."
    jov "But that's a worry for another day. For now, I will sit back and watch this play out."
    jov "Although... I feel like I need to come clean to Klara about everything. But seeing her smile... maybe it's better if I just keep my mouth shut."
    jov "And lastly, before I shut this whole thing down, I'm going to be honest. This is no longer just some vlog anymore. It turned into a whole documentary of secrets."
    jov "So yeah, I've decided to stop it here, to keep this \"documentary\" under wraps."
    jov "I just want to take this second chance and make it work with them. [mc], Sky, Klara are all my beacons of hope."
    jov "So long..."
    stop sound2
    stop music
    play sound camcorder_glitch
    scene black
    pause
    play music 'audio/Rosee.mp3'
    scene ch1ep4_303
    with Dissolve(2.0)
    mc "*takes a deep breath*..."
    mc "... What have you done to me?"
    scene ch1ep4_304
    with dissolve
    k "I... don't know what to say. [mc], I'm so sorry, I..."
    mc "No, it's not on you. You heard what he said..."
    k "Oh my god...!"
    play sound cloth
    scene ch1ep4_305
    with dissolve
    mc "I'm thankful to be alive because of him. But why didn't anyone tell me about my illness? It's something I should know, wouldn't you say?"
    scene ch1ep4_306
    with dissolve
    k "You always wanted to know every little detail, and I was scared I wouldn't be able to answer your questions."
    k "I knew Jovian had some shady connections from his past job, but I never knew exactly what he was up to. He kept things to himself during those last days..."
    k "Seeing you get better truly was a miracle: one I was scared to question."
    k "You getting better was the only good thing we had at that time, and I feared that asking too many questions would ruin that."
    k "I thought not knowing was worth it if it meant you were healthy and we were happy."
    k "But you're right. You deserved to know. I just didn't have the answers."
    k "And maybe I was too scared to look for them, scared of what it might mean for us. I'm truly sorry."
    k "I wish I could give you the closure you're looking for. I can only say that Jovian did it all because he loved you."
    scene ch1ep4_307
    with dissolve
    mc "..."
    scene ch1ep4_308
    with dissolve
    e "So... what exactly is going on here? I still can't wrap my head around all this."
    scene ch1ep4_309
    with dissolve
    mc "Or, the real question... what does that make us? Looking at you, I don't feel so different from anyone else."
    m "I don't know all the details about the serum, but I have an idea of why we feel connected."
    m "They called us the \"Numbers\". There were two groups of us."
    m "We, the first ten subjects, were the \"Early Stages\". Then came the \"Mass Productions\"..."
    m "I don't know the reasoning, but the first ten were supposed to be in pairs, but I ended up being made alone."
    m "That's all I understand. The only one who really knows about the serum is its creator."
    scene ch1ep4_310
    with dissolve
    mc "Which means Bonheur..."
    scene ch1ep4_311
    with dissolve
    mc "..."
    k "[mc], what are you thinking? You surely can't be considering..."
    scene ch1ep4_312
    with dissolve
    mc "It's nothing. I'm just thinking about what he did, and how our destinies became intertwined. Seems like we're being played with."
    scene ch1ep4_313
    with dissolve
    mc "So, where is he now?"
    ew "The answer is in the next folder."
    scene ch1ep4_314
    with Dissolve(0.1)
    k "[mc], maybe we should-"
    scene ch1ep4_315
    with Dissolve(0.1)
    mc "We've waited long enough. It's time to finish this, right?"
    scene ch1ep4_316
    with dissolve
    k "..."
    scene ch1ep4_317
    with dissolve
    k "Yes..." #
    stop music fadeout 2
    play sound camcorder_movement
    play sound2 camcorder_fastforward loop
    scene ch1ep4_318
    with dissolve
    pause
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_319
    play music 'audio/HearingAid.mp3' fadein 2
    jov "*takes a deep breath*"
    jov "It's been several years, and I never thought I'd turn this thing on again..."
    jov "So much has changed, especially me... I started to work for Bonheur."
    scene ch1ep4_320
    with dissolve
    jov "Once, I counted time in milestones: [mc]'s first steps, Sky's first word. Now, it's measured in jobs completed."
    jov "The serum kept [mc] alive, yes, but at what cost?"
    scene ch1ep4_321
    with dissolve
    jov "Klara doesn't ask anything. But I see it in her eyes... there's a hint of suspicion."
    jov "\"It's honest work\", I lied, and my voice sounded as hollow as I felt. I can't even speak like myself anymore..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_322
    jov "Completed my first... questionable job for Bonheur. The details... better left unsaid."
    jov "Each task takes a piece of me, but the thought of [mc] and Sky, healthy and laughing, keeps me going."
    jov "Although... my hands are shaking. Not from fear, but from... disgust. What have I become?"
    jov "Klara's having trouble looking me in the eyes. Is it pity, worry, or does she know?"
    jov "Can she sense the change in me, the stench of it clinging to my skin?"
    jov "Sky wants to play. Wants to build a castle, she says. As if my world isn't crumbling to sand around me. How can her eyes still shine so brightly?"
    jov "[mc] smiles at me. I smile back, but inside, I scream. Do I have it in me to finally tell him?"
    jov "No, I don't have the strength..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_323
    jov "Klara finally noticed the changes, the late nights, the silence. Worry clearly clouds her eyes, especially when she looks at me."
    jov "She hasn't asked outright... yet. But the questions hang heavy in the silence between us."
    jov "\"Where do you go?\", \"Why are you always so tired?\". If only she knew."
    jov "Mealtimes are the worst. Their laughter feels so far away. Klara watches me push food around my plate."
    jov "Even Sky hugs me tighter these days. The guilt is starting to suffocate me."
    jov "\"Are you okay?\", Sky typically asks, as her little brow furrows. I can only force a smile. \"Just peachy, sweetheart.\"."
    jov "Liar. Monster. That's what I am."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_324
    jov "The more I do for Bonheur, the further I drift from the man I was. The line between right and wrong blurs."
    jov "My hands once held the kids. Now... I can't bear to look at them."
    jov "Klara's plan was a lifeline tossed to me, and I let it slip through my fingers."
    jov "\"We can work together from now on, Jovian. We'll leave, then we can start fresh for the kids.\"... She believed in me, even when I'd stopped believing in myself."
    jov "Why did I tell them to go first? Fear? Pride?"
    jov "Or did some twisted part of me know I'd never be able to follow?"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_325
    play sound3 plane_pass
    jov "The plane took off without me. And soon, the photos started arriving... [mc] on a beach, laughing."
    jov "Sky makes sandcastles, her eyes filled with wonder."
    jov "Klara smiles in the pictures, but her eyes are distant."
    jov "It was a good decision to stay behind. My hands aren't fit to touch them anymore."
    jov "Bonheur's tasks wring tighter, like a noose around my neck. Yet... what choice do I have?"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_326
    jov "Bonheur's latest demand is unthinkable... Eliminate Hera's husband and son?"
    jov "How did it come to this? The very thought threatens to tear me apart."
    jov "My hands shake once again, and not from the usual fear. This is a different poison, seeping deep into my gut."
    jov "A monster, that's what Bonheur calls Hera. But who's the true monster here? The one fighting to survive, or the one with the power to crush her under his heel?"
    jov "Is this the end of the line? The point where even I can't justify the price anymore?"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_327
    jov "To refuse Bonheur is to sign a death warrant. To comply is to lose myself."
    jov "Yet again, I asked... What choice do I have? The serum's miracle... at what cost?"
    play sound3 woodhit
    scene ch1ep4_328
    with hpunch
    jov "No, I can't let this go on any further. I've made my decision. There's a line I cannot cross, even for [mc]'s life."
    jov "Some prices are too high. I'm going to confront Bonheur and negotiate... or end this charade."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_329
    jov "I'm cornered, with no way out."
    jov "Bonheur's resorted to blackmail. If I defy him, he's threatened to target my loved ones, not me."
    jov "My defiance died the moment he held up that photo. Sky's smile, Klara's trusting eyes... my world reduced to a bargaining chip in Bonheur's cruel game."
    jov "\"A soul for a soul\", is what he said. I'm left with no option but to comply."
    jov "It's not just [mc]'s life on the line anymore. They are all bound to this twisted fate I've woven for them."
    jov "Every smile, every carefree moment, it's all an illusion I can no longer sustain."
    jov "I must do it... for the sake of keeping them safe."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_330
    jov "I... I've done it... I took the lives of Hera's family..."
    jov "Hera's son, just a newborn infant. I... I could hear his cries as I took its life."
    jov "It's like it was pleading with me, to forgive him for the sins it has never committed."
    jov "If there is still any good in the world, I hope I can be forgiven for what I've done."
    jov "I need to run away. Hide away from the world Bonheur represents, from everything. But to protect Klara, [mc], and Sky... there was no other choice."
    scene ch1ep4_331
    with dissolve
    jov "This may be my last entry..."
    jov "Klara, if you're watching this, know that I did everything for you, for [mc], for Sky. Please forgive me..."
    scene ch1ep4_332
    with dissolve
    ew "The next clips are from several years after he moved back..."
    ew "The house had been listed for sale, but he seemed so desperate, we just had to take him in..."
    ew "He was okay for a few years. We loved him, treated him like our own son, but the change of pace didn't really help his situation..."
    scene ch1ep4_333
    with Dissolve(0.1)
    k "*sobs* I can't... I'm sorry, I just can't watch this anymore...!"
    yt "Klara..."
    stop music fadeout 3
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_334
    play music2 'audio/BeyondTheHills.mp3' fadein 3
    jov "Forgive me..."
    play sound3 waterphone
    scene ch1ep4_335
    jov "Years passed, and I still keep saying the words, as if repetition will make them come true!"
    jov "It won't bring back that child! It won't absolve me of my sin!"
    jov "They say time heals all wounds... LIES!"
    jov "Every night, the cries of that child echo! No escape, not even in sleep! They haunt my dreams, my waking hours!"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_336
    jov "I...I'm not alone anymore. T-t-there's always someone watching... In the corner of the room, a flicker in the mirror... that child's f-face... condemning me..."
    jov "Its whispers startle me awake at night... Just the creaking of the old house, or...  No, a voice... Though tiny, the whimper turns into a wail..."
    jov "It's the child!"
    scene ch1ep4_337
    jov "I cover my ears, but it's voice inside my head now. Won't stop."
    scene ch1ep4_338
    jov "Won't STOP!"
    scene ch1ep4_339
    with hpunch
    jov "STOPPPP!!"
    scene ch1ep4_340
    jov "I-I didn't m-m-mean to do it, I PROMISE!"
    jov "But does it hear me...?"
    jov "Does it even need to?! It knows! It glares into the black pit where my soul used to be! There's no hiding from that stare, no running from what I am!"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_341
    jov "T-they'll find me! Bonheur knows I've failed!"
    jov "No, it's her — Hera! Blood on her hands, yes! But it's my blood staining them red!"
    jov "T-t-the child screaming, begging...! Wait, it wasn't me who did that, it was... someone else. Wasn't it?"
    jov "No, no, no, no... Can't be me, it can't be me... I can't be the monster... That other one, the one Bonheur created."
    jov "It must be... it has to be him...!"
    jov "He wears my face, uses my hands, but... he's not me!"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_342
    jov "Sky drew a picture today. Stick figures. Her, Klara, [mc], and me... but there's another one... smaller, lying down."
    jov "Did she see? Does she KNOW what I did?"
    jov "Her eyes were so proud when she showed me... \"It's us!\"."
    jov "Does she sense the blood on my hands, even when I've tried so hard to hide it?"
    jov "The picture... it's still on the fridge. That tiny figure haunts me. A child's way of saying, \"I know what kind of monster you are.\"."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_343
    jov "H-huh...? What's this camera doing in front of me...?"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_344
    jov "There... in the bathtub. Water turns red, I swear it does. A tiny hand reaching up, splashing, then gone..."
    jov "Not real... not real... but the water is cold even though the tap never runs... How's that possible...?"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_345
    jov "The pills... they quiet the cries for a while. Not enough. Need something sharper."
    jov "The knives in the kitchen drawer... they shine. A quick cut, maybe that'll wash the stain away..."
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_346
    jov "Sky's laughter echoes from downstairs. [mc]'s shouting something about his game."
    jov "I can hear them, I can hear them all!"
    play sound camcorder_glitch
    scene black
    pause 0.1
    scene ch1ep4_347
    jov "C-cold steel against my temple... A coolness, a sign of relief..."
    jov "One finger on the trigger... Huh, it's lighter than it should be..."
    scene ch1ep4_348
    k "No... No, no, no!"
    scene ch1ep4_349
    jov "This is wrong, all of it, but... there's no other way..."
    jov "No, this is right, this is the only way out! I must find my way out!"
    jov "Just a single breath..."
    jov "One final breath..."
    scene ch1ep4_350
    k "NO!"
    scene ch1ep4_351
    jov "In..."
    jov "... Out..."
    jov "And then..."
    play sound3 woosh2
    scene ch1ep4_352
    k "Wait, Jov-!"
    play sound3 doorbang
    show ch1ep4_353
    with hpunch
    pause
    stop sound2 fadeout 5
    scene ch1ep4_354
    k "*gasps*"
    play sound3 cloth2
    play sound4 thud3
    show ch1ep4_355
    with hpunch
    pause
    scene ch1ep4_356
    with dissolve
    k "*wailing*"
    m "..."
    scene ch1ep4_357
    with dissolve
    m "... I may not be in the right place to say this, but he did what he believed was necessary."
    m "It's heart-wrenching to witness the lengths he went to, I understand."
    m "But his actions, as difficult as they are to come to terms with, were done for [mc], for you, and for Sky."
    m "He aimed to protect, to offer a second chance for a life that seemed to be fading."
    k "*sobs* I... I just didn't realize how deep his despair went, the weight he's been carrying all those years...!"
    k "We were supposed to share that burden...!"
    m "None of us truly understood, not until today. The decisions he made, the paths he chose were all for a future he deeply believed in."
    m "He was prepared to take on all the burdens, to pay any price."
    scene ch1ep4_358
    with dissolve
    m "On a personal note, I'm thankful. Without him, I would never have met [mc]. I wouldn't have felt the warmth of belonging that all of you have shown me."
    m "And if it weren't for him, we wouldn't have been here to witness his final moments, no matter how grim."
    m "I've experienced loss myself..."
    m "Every choice carried the weight of life or death: not just for me, but for those whom I was responsible."
    m "There are times, burdened by the consequences of those choices, that haunt me."
    m "Instances when I had to decide who could be saved and who couldn't. It's a burden that alters you, molds you."
    scene ch1ep4_359
    with dissolve
    m "Understanding his choices now... I relate to them more than I'd like. He waged his own battles, using every resource at his disposal, for your futures."
    m "In the military, we speak a lot about sacrifice and duty. Jovian lived those values, not on a faraway battlefield, but in the silent struggles he faced for [mc]."
    m "Your pain is a testament to the love you all shared. And it's natural to feel adrift in it, to mourn the sacrifices made."
    m "It doesn't ease the pain, but it's important to come to terms with it."
    scene ch1ep4_360
    with dissolve
    m "Now, let me ask you..."
    m "In the end, what does all your sorrow achieve? The tears, your cries?"
    m "Can any of it bring him back?"
    k "..."
    scene ch1ep4_361
    with dissolve
    k "No..."
    m "Exactly. So, stand up, not for us, not for others, but for yourself. I'm certain the Jovian you loved, and who loved you, wouldn't have wanted to see you like this."
    play sound cloth
    scene ch1ep4_362
    with dissolve
    k "Thank you."
    m "Mhm."
    stop music2 fadeout 5
    play sound2 ceilingfan_low loop fadein 4
    scene ch1ep4_363
    with dissolve
    yt "I couldn't have articulated it better—actually, I doubt I'd have found the right words to reach her."
    yt "She doesn't easily trust others' words, so gaining her full confidence takes time."
    yt "But... Moon managed to make her listen amidst her grief."
    yt "This came from someone who I thought barely understood life."
    yt "I can't fault Emma for saying Moon is unpredictable. Her wisdom is not readily visible; it lies deep within her core."
    scene ch1ep4_364
    with dissolve
    play sound heartbeat_single
    pause
    yt "... What's this? My heart's racing, but not out of affection... From something else? Why does it call your name?"
    yt "Wait, how did I even know that...? What the hell is happening to me?"
    scene ch1ep4_365
    with dissolve
    e "[mc], are you alright?"
    mc "Yeah... I'm fine..."
    scene ch1ep4_366
    with dissolve
    k "... You know what I'm going to ask, right?"
    ew "Come with me."
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade

    play sound parkwind loop
    scene ch1ep4_368
    with dissolve
    pause
    scene ch1ep4_367
    with dissolve
    m "Dear Lord..."
    m "As I kneel in reverence before this hallowed ground, I humbly ask you to grant eternal solace to the soul of my confidant's cherished loved one."
    m "Though our paths never crossed, I know he was a pillar of strength and a wellspring of love for those who were blessed to know him."
    m "May his memory forever be a guiding star, illuminating the lives of his loved ones and inspiring them to walk in the footsteps of his wisdom and compassion."
    m "Grant them the fortitude to carry on his legacy, to find joy in the moments he shared, and to feel his presence in the whispers of the wind."
    m "Watch over them, oh Lord, and envelop them in your boundless grace, so that they may find peace in the knowledge that he rests eternally in your celestial embrace."
    m "Amen..."
    scene ch1ep4_369
    with dissolve
    ew "He chose this..."
    ew "Before he lost himself, he made us promise that whatever happens in this house, stays in this house."
    ew "He was a good man, and we came to love him like our own son."
    ew "We're prepared to accept any punishment from you or the law. But we'll never regret protecting him from the world."
    scene ch1ep4_370
    with dissolve
    mc "... What's your plan about him?"
    k "..."
    scene ch1ep4_371
    with dissolve
    k "I will not do anything..."
    mc "Huh?"
    k "He chose this path... and knowing him, he wouldn't have wanted me to interfere. I'll let him rest here in peace."
    scene ch1ep4_372
    with dissolve
    mc "..."
    k "Wherever you are, I hope you've found freedom from your suffering... Thank you for sacrificing yourself for us."
    scene ch1ep4_373
    with dissolve
    yt "Her words are cold..."
    yt "She understands, but she's barely holding herself together..."
    yt "I... myself..."
    scene ch1ep4_374
    with dissolve
    yt "Thank you for giving me this second chance at life... I won't waste it."
    yt "I will finish this, mark my words."
    play sound2 phonevibrate loop
    scene ch1ep4_375
    with dissolve
    pause
    play sound2 phoneclick
    scene ch1ep4_376
    with dissolve
    mc "Aine?"
    "......."
    "..........."
    scene ch1ep4_377
    with dissolve
    mc "Huh?"
    "........"
    mc "Ah, yeah, well... we're heading home now. We've finished here..."
    "....."
    mc "We'll discuss it when we're all back together. It's better to talk about it with everyone present..."
    "........"
    scene ch1ep4_378
    with dissolve
    mc "My voice? Oh, no, I'm fine. We'll be home in a few hours."
    "...."
    mc "Okay, we will."
    play sound2 phoneclick
    play sound3 cloth
    scene ch1ep4_379
    with dissolve
    k "Who was that?"
    mc "Aine. She said our {i}friends{/i} are waiting and told me to hurry home."
    k "I see..."
    mc "Should we go?"
    k "There's nothing left for us here. Let's head back... let everything sink in..."
    play sound2 camcorder_movement
    scene ch1ep4_380
    with dissolve
    ew "You should have this."
    ew "He never said what to do with it, but since you're interested in photos, I believe he'd want {i}you{/i} to have it."
    scene ch1ep4_381
    with dissolve
    mc "How did you know that?"
    ew "He talked about you a lot, and had mentioned your interest in photos several times."
    mc "..."
    scene ch1ep4_382
    with dissolve
    mc "I have a question."
    ew "Yes?"
    mc "Why did your husband call us cursed?"
    scene ch1ep4_383
    with dissolve
    ew "Thaddeus is superstitious. After Jovian's death, misfortune followed us, and he blamed you all. He said you were a curse on our lives."
    ew "While I don't share that belief, I can't say he was entirely mistaken."
    ew "But that's behind us now. We've lived long enough, seen too much. Peace of mind is all we want."
    scene ch1ep4_384
    with dissolve
    ew "I just hope... there's a reason for all this..."
    ew "Good luck with whatever you aim to achieve."
    mc "..."
    scene ch1ep4_385
    with dissolve
    ew "Let's get this done, Detective Meyer. We're ready to cooperate."
    e "Yes."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound2 exhale_female_reverb
    m "{i}Little did I know..."
    play music 'audio/DaytimeMoon.mp3'
    play sound closedoor
    scene ch1ep4_386
    with dissolve
    pause
    scene ch1ep4_387
    with dissolve
    j "How was it?"
    m "Not a big deal, just a gang trying to mug an old man. I took care of it quickly."
    j "I see."
    scene ch1ep4_388
    with dissolve
    j "..."
    m "... What?"
    scene ch1ep4_389
    with Dissolve(0.1)
    play sound bookdrop
    j "I'm not going sugarcoat it, Fang: do you really find fulfillment living this way?"
    m "You were the one who put me in this position. Why are you now questioning how I'm living?"
    scene ch1ep4_390
    with dissolve
    j "I know, but it's not my intention to trap you in this life. I'm not my sister."
    j "You refused to join our cause despite accepting our deal, so this is a place I provided for you to find a purpose."
    j "You might have been an exceptional soldier, but you are also human, Fang."
    j "Stop confining yourself to following orders. Don't you want to find your calling?"
    m "Yes."
    j "So, are you sure this is what you want?"
    m "No. I don't even know what I want..."
    scene ch1ep4_391
    with dissolve
    j "Out of all my charity cases, you're proving to be the most challenging."
    m "... What do you suggest I do, then?"
    scene ch1ep4_392
    with dissolve
    j "Leave this place and do something meaningful. Not for us, not for others, but for yourself."
    m "And how am I supposed to find that \"something meaningful\"?"
    j "I think I know someone who might be able to help you—No, I have this feeling you might just help each other."
    j "Under our agency, try taking on the role as his aid, and see where that leads."
    m "If you're giving me orders again, how is that any different?"
    j "It's not an order... this time, it's your choice."
    j "Like I said, I'm not here to control you. You're always welcome to return if it doesn't work out."
    scene ch1ep4_393
    with dissolve
    m "..."
    scene ch1ep4_394
    with dissolve
    m "Who is it?"
    j "His name is [mc]. But we'll need to wait for the right moment. I can't just hand you over to him out of the blue."
    j "Well... No matter what I say, I'm sure it will sound like that."
    scene ch1ep4_395
    with dissolve
    m "{i}Little did I realize that fate was pulling us {b}back together{/b}..."
    scene ch1ep4_396
    with dissolve
    m "{i}Oddly enough, it wasn't a comforting sensation, so I tried to put up a brave face every time our eyes met."
    m "{i}Yet, despite the ominous weight in my chest, seeing you brought an unexpected sense of relief, even without knowing your true identity."
    scene ch1ep4_397
    with dissolve
    m "{i}Without hesitation..."
    m "{i}... I embraced the role of being your bodyguard; it was a responsibility I found unexpectedly fulfilling."
    scene ch1ep4_398
    with dissolve
    m "{i}What is this feeling...? Whenever I'm near you, this indescribable sense of happiness washes over me... What exactly are we to each other?"
    scene ch1ep4_399
    with dissolve
    m "{i}You're unlike anyone I've ever met. Your eyes often carry a hint of pity."
    m "{i}I don't desire it, yet I find comfort knowing you're here to watch over me, just as I'm determined to protect you-"
    stop music fadeout 5
    scene black
    with dissolve
    m "{i}-My Lord..."
    m "{i}My... Lord...? Who am I referring to-"
    play sound parkwind loop
    scene ch1ep4_400
    with Dissolve(2.0)
    mc "Moon..."
    scene ch1ep4_401
    with dissolve
    mc "We're home."
    scene ch1ep4_402
    with dissolve
    m "... Sorry, I was resting my eyes."
    mc "No, no, it's okay. Come on, they're here."
    play sound2 cardoorclose
    scene ch1ep4_403
    with dissolve
    pause
    scene ch1ep4_404
    with dissolve
    mc "It's you guys again."
    scene ch1ep4_405
    with dissolve
    mc "You look different from before. What's up with that?"
    un "Well, not only me, but..."
    scene ch1ep4_406
    with dissolve
    un "... A certain guy didn't like my usual look, that's all."
    mc "Huh?"
    scene ch1ep4_407
    with dissolve
    m "What did you do?"
    cl "Don't worry about it."
    scene ch1ep4_408
    with dissolve
    mc "Wait, what's your name? I don't think you've mentioned it."
    la "My real name would be an inconvenience, so let's just go with \"Lance\"."
    scene ch1ep4_409
    with dissolve
    m "What are you all doing here?"
    la "We came to talk with your... friend."
    m "He's more than just a friend."
    la "I see, my mistake."
    la "Nevertheless, we may know something he doesn't, and we thought we could share it with him."
    la "You might find it interesting too, Fang."
    m "..."
    scene ch1ep4_410
    with dissolve
    j "I believe you found something?"
    play sound2 camcorder_movement
    scene ch1ep4_411
    with dissolve
    mc "This..."
    j "Interesting..."
    play sound2 closedoor
    scene ch1ep4_412
    with Dissolve(0.2)
    s "[mc], Mom! You're back-"
    scene ch1ep4_413
    with dissolve
    pause
    scene ch1ep4_414
    with Dissolve(1.0)
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound firewood loop
    scene ch1ep4_415
    with dissolve
    la "Is this all of you?"
    mc "Emma has to take care of the Winters."
    mc "Klara is trying to explain everything to Sky upstairs. Honestly, it's better for her not to see it at all."
    mc "Freya and Shu... I have no idea where those two went."
    scene ch1ep4_416
    with dissolve
    a "Shu told me that Freya is coming with her—I mean him."
    a "God, I'm still so confused about that guy."
    scene ch1ep4_417
    with dissolve
    a "But, yeah... He mentioned he was looking for a place or something. He didn't elaborate further."
    scene ch1ep4_418
    with dissolve
    la "I see. Then, if everyone else is here, we should start."
    scene ch1ep4_419
    with dissolve
    mc "Wait!"
    j "[mc]?"
    mc "I think it's better if only you guys watch it. The rest should just listen."
    j "... We understand."
    scene ch1ep4_420
    with dissolve
    a "*whispers* He's so intimidating."
    g "*whispers* I know, right? Something's off about his presence."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound firewood loop
    play sound2 doorbang
    show ch1ep4_421
    with hpunch
    play music 'audio/HidingDNA.mp3'
    pause
    scene ch1ep4_422
    with dissolve
    pause
    scene ch1ep4_423
    with dissolve
    g "Did he... just..."
    mc "Yeah, you guys heard it right..."
    a "Oh... my god..."
    scene ch1ep4_424
    with dissolve
    la "I'm terribly sorry for your loss, [mc]."
    mc "He did what he had to..."
    play sound2 camcorder_movement
    scene ch1ep4_425
    with dissolve
    la "No... What others may say doesn't matter. In our eyes, Jovian is a true hero."
    la "We'll visit him as soon as we can. Pay him our full respects."
    scene ch1ep4_426
    with dissolve
    mc "Thank you."
    scene ch1ep4_427
    with dissolve
    la "Now then, as for the rest of what Jovian revealed..."
    la "You were right."
    j "Yes, just as I thought..."
    mc "Huh? Right about what?"
    scene ch1ep4_428
    with dissolve
    j "I still can't believe it, but you, [mc], have the last serum we sought."
    mc "So you guys knew about this?"
    scene ch1ep4_429
    with dissolve
    la "I did say we have information that you don't. We only needed confirmation in order to share this confidential detail."
    la "And with that, there's no doubt about it."
    j "For the past two years, we have been scouring every corner of the globe to find it. Who would've thought it was right under our noses this whole time?"
    scene ch1ep4_430
    with dissolve
    a "Is it the thing... that was injected into [mc]?"
    la "That's right, Miss Agnor. We will explain what we know in a moment. But these serums are far too dangerous for anyone to possess."
    scene ch1ep4_431
    with dissolve
    la "For a long time, we've been searching for every last one of them, including those that... have used them."
    la "That's how we found Fang, or Moon, as you would call her now."
    la "And the last possessor... is you, [mc]."
    mc "Just... how dangerous are these things?"
    scene ch1ep4_432
    with dissolve
    la "Fang has been with you for some time, so I'm guessing you know her capabilities by now."
    la "Imagine dozens of her—No, we're talking about hundreds."
    la "If we were to let these people roam free without supervision, just think of what they could do."
    la "I'm talking about those who turned to crime, those who joined wicked causes to exploit what they possess."
    scene ch1ep4_433
    with dissolve
    mc "So you kill them?"
    la "These serums eventually corrupt the possessor. However, that's not always the case."
    la "Observing Fang for several years, we can safely say that the Early Stages don't suffer such a fate."
    la "But those Mass Produced... are the problem. They are made to be disposable, and if they can no longer be saved, we have no choice but to eliminate them."
    mc "I see..."
    scene ch1ep4_434
    with dissolve
    mc "Moon and I are from the Early Stages, is that right?"
    la "That is correct."
    mc "Then... how come I don't feel that different from any normal person?"
    la "This is only a theory, but we may know why."
    scene ch1ep4_435
    with dissolve
    la "Shall I? It's better if he explains it himself."
    mc "He?"
    j "Feel free to. But expect a chain reaction from a few people in this room."
    stop music fadeout 4
    play music2 'audio/Impasse.mp3' fadein 2
    play sound2 alter_woosh
    scene ch1ep4_436
    with Dissolve(0.2)
    la "{size=-10}Switch with me. You only have a few minutes..." with dissolve
    play sound2 cloth2
    show ch1ep4_437
    with hpunch
    pause 0.3
    play sound2 gravelslide
    scene ch1ep4_438
    pause 1.0
    play sound3 shortgiggle
    scene ch1ep4_439
    cl "Heheee!"
    play sound2 cloth2
    show ch1ep4_440
    cl "Oh, oops... She slipped out. My bad."
    j "*sighs*"
    scene ch1ep4_441
    with dissolve
    g "What the hell is going on here? Should we be worried?"
    mc "What... what just happened?"
    scene ch1ep4_442
    with dissolve
    ala "Be at ease, young ones. Allow me to introduce myself properly."
    scene ch1ep4_443
    with dissolve
    ala "I am Lucien, Lance's alter ego."
    ala "And the foolish one residing within her is my twin sister, Aveline."
    ala "We are very pleased to meet you, people of the new era."
    cl "Oh, I'm not sure if she feels the same way..."
    mc "Wait, wait, wait! Huh?! I'm so fucking confused!"
    ala "Permit me to elucidate from the beginning."
    scene ch1ep4_444
    with dissolve
    ala "Most individuals who are aware of the Numbers' origin only know of two groups or batches that were created."
    ala "However, that is not entirely accurate."
    scene ch1ep4_445
    with Dissolve(2.0)
    ala "Before you, there was us... the \"Experimental Test Subjects\". Or, simply, the failed iterations of the serum."
    ala "We were referred to as the \"Zeroes\"."
    ala "I shall not delve deeper into the specifics of our creation, but that is the fundamental concept."
    scene ch1ep4_446
    with dissolve
    ala "The core principle behind the serum is the combination of DNA from two individuals: the living and the exhumed."
    ala "The living, of course, refers to you, the Test Subjects. And the exhumed are us, the ones bestowing upon you your strength and capabilities."
    scene ch1ep4_447
    with dissolve
    a "E-exhumed...? Does that mean..."
    scene ch1ep4_448
    with dissolve
    ala "Indeed. Aveline and I are deceased mercenaries from a bygone era. The creator managed to locate our remains and utilized them for their experiments."
    ala "And no, this is not derived from some fantastical tale; it is a reality. Made possible by what you people refer to as Science."
    cl "To think that someone would be capable of reviving the dead..."
    g "So that means... [mc] and Moon are also... you know, dead people?"
    ala "Do not misunderstand, young one. I am only referring to us, the Zeroes."
    ala "The Numbers are... not entirely identical to us."
    ala "The Zeroes retain the consciousness of both the living and the exhumed, creating an unstable mental state in the Test Subjects. Hence, we were deemed \"Failed\"."
    scene ch1ep4_449
    with dissolve
    ala "Utilizing the same concept, the successful subjects actually amalgamate both DNAs and manage to exist as a single entity, if that makes sense."
    ala "Unlike the Zeroes, the Numbers do not trigger any alter ego and retain only the consciousness of the Test Subjects while still maintaining the capabilities of the exhumed."
    scene ch1ep4_450
    with dissolve
    mc "Then what about me?"
    ala "You, on the other hand, are quite an enigma..."
    ala "However, I postulate that it is because you did not undergo what they referred to as the Incubation stage, which only applies to the Early Stages."
    mc "Incu...bation stage?"
    scene ch1ep4_451
    with dissolve
    m "It's a process designed to awaken the serum within the Early Stages. This specific process was removed when Mass Production started."
    scene ch1ep4_452
    with dissolve
    ala "Precisely. Aside from combining DNAs, it is indeed true that the serum also possesses incredible healing capabilities."
    ala "I hypothesize that this healing process prepares you for the Incubation stage. However, none of us knows how the Incubation stage is conducted."
    ala "It is a process that remains a mystery to us to this day."
    mc "I see..."
    scene ch1ep4_453
    with dissolve
    ala "{size=-10}I have concluded my explanation..."
    ala "{size=-10}No, grant me a moment..."
    scene ch1ep4_454
    with dissolve
    ala "Is there something you wish to convey to me... Aveline?"
    scene ch1ep4_455
    with dissolve
    cl "..."
    scene ch1ep4_456
    with dissolve
    cl "... She won't come out."
    ala "Oh... well... It's not as if you've vanished entirely. Let us spar again in the near future."
    scene ch1ep4_457
    with dissolve
    av "..."
    scene ch1ep4_458
    with dissolve
    av "Yes, brother... I would be more than inclined..."
    scene ch1ep4_459
    with dissolve
    pause
    stop music2 fadeout 4
    play sound2 alter_woosh
    scene ch1ep4_460
    with Dissolve(0.2)
    ala "{size=-10}Let us switch back..." with dissolve
    scene ch1ep4_461
    with dissolve
    la "*takes a deep breath*..."
    scene ch1ep4_462
    with dissolve
    a "I can't believe this... I'm having a hard time trying to process what I'm seeing..."
    g "So it's possible for two consciousnesses to exist within one body? Well damn, that's... wild!"
    play music 'audio/HidingDNA.mp3' fadein 2
    scene ch1ep4_463
    with dissolve
    la "As incredible and advantageous as that sounds, there are serious repercussions."
    la "It's tougher for us Zeroes, but everyone with the serum faces problems."
    la "And they're not just any simple repercussions. They affect one's vital organs, weakening them."
    la "Since the exhumed are meant to be stronger than normal people, it's like using a truck engine in a moped."
    la "But if you know how to care for your body, you can easily manage the side effects."
    la "Although, there's one thing that happens to all of us..."
    scene ch1ep4_464
    with dissolve
    m "Our eyes."
    la "Exactly. Eventually, it harms our eyes, causing us to cry blood. And there are no countermeasures for it."
    la "It might not harm our health directly, but it's... quite painful."
    scene ch1ep4_465
    with dissolve
    mc "..."
    la "I know this is a lot to take in, but it's better for us to lay it all out for you now. You have another question, right?"
    scene ch1ep4_466
    with dissolve
    mc "Yeah, it's about us."
    m "Commander?"
    mc "Lucien mentioned something about the exhumed..."
    mc "Moon and I... who the hell do we have inside us?"
    la "Do you really want to know-?"
    la "Ah, silly question. Of course, you deserve to know."
    scene ch1ep4_467
    with dissolve
    la "Claire?"
    cl "On it."
    scene ch1ep4_468
    with dissolve
    cl "Checking on our data from your past expeditions..."
    cl "Moon is linked with #4, and [mc] is connected to #3..."
    cl "..."
    scene ch1ep4_469
    with dissolve
    cl "This is... interesting... No, this shouldn't even be possible..."
    la "Well, we're delighted to hear about it, Ms. Secretary."
    scene ch1ep4_470
    with dissolve
    cl "These two are... Do you know anything about Suehara?"
    j "Oh, wow... Out of all the possibilities..."
    j "That data has been nothing but accurate. The fact that it's there means that it's true."
    stop music fadeout 5
    scene ch1ep4_471
    with dissolve
    mc "What's it about?"
    cl "Let me tell you the story..."
    stop sound fadeout 2
    show kaitosora1
    with flashl
    play music 'audio/OrigamiVoyage.mp3'
    cl "In the ancient times of Suehara, there existed an empire where the sun never dared to set without first kissing the golden spires of its capital, Tsukizaki."
    cl "At the heart of this majestic empire ruled Emperor Kaito, a sovereign of unparalleled wisdom and valor, whose reign brought about an era of prosperity and peace."
    show kaitosora2
    with dissolve
    hide kaitosora1
    cl "By his side, not as a mere servant but as his most trusted confidant, was Lady Sora..."
    cl "A woman whose beauty was matched only by her intelligence and fierce loyalty to the emperor and the empire."
    show kaitosora3
    with dissolve
    hide kaitosora2
    cl "Their story began in the quiet corridors of the imperial palace, where whispers of their affections first took flight."
    cl "It was an uncommon bond, transcending the rigid hierarchies of royalty and service."
    show kaitosora4
    with dissolve
    hide kaitosora3
    cl "Emperor Kaito, a widower whose heart had been closed to love, found in Sora a kindred spirit, a woman whose presence illuminated the darkest corners of his world."
    cl "Sora, who had served at the palace since her youth, found in the emperor not just a ruler, but a man of deep compassion and understanding."
    cl "Their love, though forbidden by tradition and the court's expectations, bloomed in secret, nurtured by stolen moments and silent glances."
    show kaitosora5
    with dissolve
    hide kaitosora4
    cl "In time, their love could no longer be concealed, and Kaito, with the courage that had defined his reign, declared his intent to marry Sora."
    cl "The empire, accustomed to his unorthodox ways, celebrated the union, for the happiness of their beloved emperor ensured the prosperity of Suehara."
    cl "The wedding was a spectacle of joy and grandeur, a testament to a love that defied norms and expectations."
    stop music fadeout 4
    show kaitosora6
    with Dissolve(1.0)
    pause 3.0
    show black
    hide kaitosora5
    cl "However, their happiness was not to last..."
    play music2 'audio/CherryBlossomFall.mp3'
    play sound hellfire loop
    show kaitosora7
    with dissolve
    hide kaitosora6
    cl "A neighboring kingdom, envious of Suehara's prosperity and peace, launched a surprise attack. The empire, caught off guard, faced unprecedented peril."
    cl "Kaito, ever the protector of his people and his love, led the charge to defend the empire."
    stop sound fadeout 2
    show kaitosora8
    with dissolve
    pause 6.5
    show ch1ep4_471a
    hide kaitosora7
    cl "In the heat of battle, as the emperor fought valiantly, a deadly arrow aimed at Sora was intercepted by Kaito."
    cl "The emperor fell, mortally wounded. With the last of his strength, he uttered his last words declaring his eternal love for Sora and his empire."
    cl "Though the war against the enemy had been won, the empire could not celebrate its Pyrrhic victory."
    cl "The loss of Emperor Kaito plunged the empire into mourning, but none grieved more deeply than Sora."
    cl "The world they had dreamed of building together, a world of enduring peace and love, had crumbled before her eyes, shattered by the tip of an arrow."
    cl "In her heart, she believed that her existence without Kaito was a life devoid of purpose, a flame without its warmth."
    show kaitosora9
    with dissolve
    pause 1.8
    show ch1ep4_471b
    hide kaitosora8
    cl "With a heart drowned in grief, Sora chose to follow her beloved into death, committing Jigai in the imperial garden where Kaito had first declared his love for her."
    cl "It was her final act of love and loyalty, a testament to their undying bond."
    stop music2 fadeout 5
    play music 'audio/JapaneseDawn.mp3' fadein 4
    show kaitosora2
    with dissolve
    hide kaitosora9
    cl "The tale of Emperor Kaito and Lady Sora became a legend, a true reminder of the power of love and the sacrifices it entails."
    cl "Their story, echoing through the ages, inspired generations, teaching that true love knows no bounds, not even in the face of death itself."
    cl "And so, in the heart of Suehara, amidst the whispering winds and beneath the eternal sky, the love of Kaito and Sora endures, a beacon of light in a world of shadows."
    play sound firewood loop
    scene ch1ep4_472
    with dissolve
    a "Whoa...! What a beautiful story..."
    g "Yeah..."
    g "Wait, so that means...!"
    scene ch1ep4_473
    with dissolve
    cl "Mhm. Emperor Kaito's DNA was used for serum #3, and Lady Sora's for #4."
    scene ch1ep4_474
    with dissolve
    m "So, technically speaking..."
    stop music
    play sound2 woosh
    show ch1ep4_475
    mc "She's my wife?" (multiple=2)
    m "He's my husband?" (multiple=2)
    scene ch1ep4_476
    with dissolve
    mc "..." (multiple=2)
    m "..." (multiple=2)
    play sound2 woodhit
    play music 'audio/ChuckInTheBox.mp3'
    show ch1ep4_477
    with hpunch
    a "NO WAY!!!!" (multiple=2)
    g "REALLY??!!" (multiple=2)
    play sound2 smallbell
    show ch1ep4_478
    mc "Hey, don't freeze up. It's already getting weird in here."
    if moonroute:
        m "I-I-I-I'm not... ready for this! Please give me some time!"
        mc "Where did that playful side of you go...?"
    if allornothingroute:
        scene ch1ep4_479
        with Dissolve(0.2)
        a "*whimpers*"
        g "Heh...!"
        scene ch1ep4_480
        with dissolve
        a "What's the point of living anymore...? What's the point...?"
        g "Serves you right."
    scene ch1ep4_481
    with dissolve
    mc "So... is that why we've felt this weird connection?"
    m "It... it has to be. There's no other explanation."
    scene ch1ep4_482
    with dissolve
    la "Correct. The essences within you two are reaching out to each other."
    la "It may not be the same, but Lucien and Aveline have a certain connection between them, too. I'm sure that also goes for the rest of the Early Stages."
    mc "So... what do we do now? This is a lot to process..."
    play sound2 woosh
    show ch1ep4_483
    g "You fuck? Like a real husband and wife do?"
    scene ch1ep4_484
    a "Hey!"
    g "What?! I'm just saying!"
    scene ch1ep4_485
    with dissolve
    la "It's your choice. Maybe talk it over. But... take some time to think for now."
    la "You've been through a lot today. It's a good idea to take some time off."
    mc "Yeah, we'll do that."
    la "Alright, we'll leave you to it. Contact Jess if you need anything."
    mc "Guess I'm footing the bill, but yeah... thanks for coming."
    play sound2 woosh
    show ch1ep4_486
    la "You charged him for Nicole and Yuna's service?! Seriously?!"
    j "What are you talking about? You're the one who started our agency in the first place!"
    j "nO oNe GeTs A fReE sErViCe, blah, blah, blah...!"
    play sound2 bodyfall2
    show ch1ep4_487
    with hpunch
    cl "Okay, okay. I'm not going to be your referee, so let's just get out."
    scene ch1ep4_488
    with dissolve
    cl "See you later... [mc]."
    mc "T-take care..."
    scene ch1ep4_489
    with dissolve
    yt "What's with that mischievous grin...?"
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/SheWont.mp3'
    scene ch1ep4_490
    with dissolve
    mc "..."
    m "..."
    scene ch1ep4_491
    with dissolve
    mc "Well... this is awkward..."
    m "Hm? Why? I don't feel that awkward."
    mc "Yeah, says the one who was blushing like a tomato moments ago."
    play sound woosh
    scene ch1ep4_492
    m "!!!"
    mc "See what I mean? Do you always freeze up like that when you're flustered?"
    scene ch1ep4_493
    with dissolve
    m "I'm not sure. This time, I just don't know how to react or what to make of how I feel."
    mc "*sighs*"
    m "This is a first for me..."
    m "My heart is racing, but... it feels really nice. Is this what love is supposed to feel like?"
    menu:
        "I can't say":
            scene ch1ep4_494
            with dissolve
            mc "I can't say for sure."
            m "I see..."
        "I think so":
            scene ch1ep4_494
            with dissolve
            mc "I think so."
            mc "But what do you really feel towards me?"
            m "I'm not sure... but I know I want to stay by your side."
            $ moonpoint += 1
            $ renpy.notify(moonnotif)
    
    scene ch1ep4_495
    with dissolve
    mc "It's crazy that you have such a deep understanding of concepts but haven't experienced them yourself. Why is that?"
    m "I learned through observing others. Over time, I accepted those observations as truths."
    mc "I see... It's still strange to me."
    scene ch1ep4_496
    with dissolve
    m "Uh... Commander?"
    mc "Yeah?"
    m "Are you really my husband?"
    mc "If the history records and the details about the serum are correct, then technically, yes..."
    m "And I'm your wife?"
    mc "Yep."
    m "Then what do we do now? I have no idea what to make of it."
    mc "We can't just ignore the fact, nor do I want us to."
    mc "It's a confusing situation, but it's something very special to us."
    mc "That said, do you simply want us to forget about it?"
    show moonshakehead
    pause 1.5
    show ch1ep4_497
    with dissolve
    scene ch1ep4_498
    with Dissolve(0.1)
    m "No, I don't wanna!"
    yt "*laughs* She sounded so childlike just now. Another rare Moon mannerism: I'll add it to my list."
    scene ch1ep4_499
    with dissolve
    mc "Then we'll have to accept it. Maybe not right away, but let it come naturally, gradually. I don't want to force you into this."
    m "I suppose that's all we can do."
    scene ch1ep4_500
    with dissolve
    mc "I still can't believe something like this is possible."
    mc "With our current technology, it shouldn't be. But here we are."
    mc "Why was this kept a secret? It could save millions of lives."
    mc "But then again, knowing the risks, maybe it's better if it stays hidden."
    scene ch1ep4_501
    with dissolve
    m "Yes, there are many factors to consider. It's safer in the right hands. That's what Jess and her crew fought for."
    mc "Oh man... this is still a lot to take in. Giving it a rest was a good idea..."
    stop music fadeout 3
    play music2 'audio/HidingDNA.mp3' fadein 3
    scene ch1ep4_502
    with dissolve
    m "..."
    scene ch1ep4_503
    with dissolve
    m "I need to tell you something."
    mc "What's up?"
    m "Aside from us, one more serum user is still alive."
    mc "Really? Who?"
    m "Subject Number Two."
    if moonroute:
        mc "Wait, are they..."
        m "The one who killed my friends when we tried to escape from the military."
    else:
        m "She killed my friends during our escape attempt from the military."
    scene ch1ep4_504
    with dissolve
    mc "So she's still out there?"
    m "Mhm..."
    m "Her real name is {i}Aoife{/i}."
    scene ch1ep4_505
    with dissolve
    mc "E-Eefa?"
    m "Ee...fuh... Eefuh. It's spelled A-O-I-F-E, but that's how you pronounce it."
    mc "Okay..."
    scene ch1ep4_506
    with dissolve
    m "Jess and her crew have been aware that Aoife's still alive, but they've never been able to catch her."
    m "If only I could..."
    m "..."
    mc "What will you do once you find her?"
    m "I..."
    mc "You seem conflicted. Why?"
    image mmkamtpast:
        "ch1ep4_507.jpg"
        pause 3.0
        "ch1ep4_508.jpg"
        pause .2
        repeat
    show mmkamtpast
    with dissolve
    m "... Back then, the soldiers split into two groups over their beliefs."
    m "The Loyalists supported the military's power. Many joined them, including One and Two."
    m "Six, Eight, and I were part of the Activists, trying to initiate change from within. Because we saw ourselves as prisoners, not soldiers, fighting someone else's war."
    m "But as the Loyalists had military backing, our numbers decreased day after day. Soon, only a few of us remained."
    m "One day, we were tasked with eliminating the Loyalists' leader, Subject Number Two."
    mc "I take it that you failed?"
    m "Not completely..."
    m "Informed by a spy, we planted a bomb in a Loyalist hideout where One and Two often stayed."
    m "Two survived the blast."
    mc "And One?"
    m "He died trying to save Two from the fire caused by the explosion."
    mc "So that's why she's after you."
    m "Mhm."
    yt "It's not a battle for justice, but a fight for revenge with no clear right side... I see..."
    menu:
        "Push your beliefs on her":
            $ aoifelives = True
            scene ch1ep4_509
            with dissolve
            mc "Listen, Moon: I know you're hurting over this, but going after Aoife won't solve anything."
            mc "Even if you get your revenge, it won't bring your friends back or undo the past."
            mc "You said the same to Klara, so I know you get that, right?"
            m "Yes..."
            mc "Moving forward means letting go of that resentment."
            mc "Hanging onto that anger will just eat away at you. It's not going to bring you any peace."
            mc "How long are you going to endure it?"
            m "I... I'm not sure I can let it go, Commander. It's totally different from Klara. Their deaths aren't something I can just forget."
            mc "I'm not saying you have to forgive her. But if there's a chance to stop the fighting, don't let it pass by."
            mc "You have me now, Moon. Just think about that."
        "Let her decide on her own":
            $ aoifelives = False
            scene ch1ep4_509
            with dissolve
            mc "I promised I wouldn't dictate your choices, right?"
            mc "And I'm not about to start now, pretending I've got all the answers. This decision is yours to make."
            mc "Just know that whatever you decide, I'm with you."
            mc "Whether you go after Aoife or choose to let go and move forward, there's no wrong choice here. Focus on what {i}you{/i} believe you should do."
            mc "You have me now, Moon. That's all that matters."

    scene ch1ep4_510
    with dissolve
    m "..."
    play sound firewood fadein 2 loop
    scene ch1ep4_511
    with Dissolve(2.0)
    pause
    scene ch1ep4_512
    with dissolve
    bo "Hm?"
    scene ch1ep4_513
    with dissolve
    fr "I've gathered enough resources, father."
    fr "Everything is in place; we're ready to make our move."
    scene ch1ep4_514
    with dissolve
    bo "And these {i}resources{/i} include her?"
    fr "Yes. I heeded your warning about {i}that{/i} soldier."
    fr "If everything we know about her is accurate, then we'll need a stronger soldier to counter her."
    scene ch1ep4_515
    with dissolve
    bo "..."
    scene ch1ep4_516
    with dissolve
    bo "Subject Number Two, reborn from a marksman renowned in history, set against a Legend-class like Sora? Dubious... but intriguing."
    bo "*chuckles* Fascinating."
    bo "End her life. Now that she has discovered her Odd, she ceases to intrigue me."
    ao "..."
    scene ch1ep4_517
    with dissolve
    fr "Speak up. Father is commanding you."
    bo "She will obey, but speaking is not her forte."
    scene ch1ep4_518
    with dissolve
    bo "You have my full backing. I am eager to witness the fruits of your strategy."
    bo "Do entertain me, Francis."
    fr "We have everything we need. Plus, I have my own reasons for targeting him first. He's as good as dead."
    bo "Personal vendettas can sharpen one's determination or cloud one's judgment. Tread carefully with the double-edged sword you've unsheathed, Francis."
    fr "It's not mere anger, father. Believe me, he won't know what hit him."
    bo "So be it."
    scene ch1ep4_517
    with dissolve
    fr "Let's go."
    scene ch1ep4_519
    with dissolve
    bo "..."
    scene ch1ep4_520
    with dissolve
    bo "Perhaps my experiments weren't my biggest mistake, but you, Francis..."
    call hide_days from _call_hide_days_22
    with dissolve
    stop music2 fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    show screen day_tuesday with dissolve
    play sound traffic fadein 2 loop
    scene ch1ep4_521
    with dissolve
    f "... So that's what happened..."
    mc "Yeah... we found him, but at the same time we lost him again."
    mc "It's always like this. We solve one problem, but then another one pops up."
    mc "When will we finally achieve something truly beneficial?"
    scene ch1ep4_522
    with dissolve
    f "... I still wonder where Mom went. She said she'd step back, so she probably went somewhere far."
    yt "I should change the topic. I don't want her to worry too much."
    scene ch1ep4_523
    with dissolve
    mc "Anyway, where did you and Shu go yesterday?"
    f "Well... he asked me to keep it a secret, but we were looking for... a venue to prepare for something."
    mc "A venue?"
    scene ch1ep4_524
    with dissolve
    f "Yeah! It was beautiful!"
    mc "What for?"
    f "That, I don't know. He didn't tell me. Likely for an event of some sort, that's for sure."
    mc "That guy..."
    $ renpy.sound.set_volume(0.3, 1.0)
    play music 'audio/KingsRansom.mp3'
    scene ch1ep4_525
    with dissolve
    pause
    scene ch1ep4_526
    with dissolve
    f "Who's that? A customer?"
    scene ch1ep4_527
    with dissolve
    mc "Hey, can we help you with something? We're opening in thirty minutes if you're here to eat."
    play sound2 cloth
    scene ch1ep4_528
    with dissolve
    ao "..."
    mc "..."
    scene ch1ep4_529
    with dissolve
    mc "Have we met before?"
    ao "..."
    scene ch1ep4_530
    with dissolve
    f "Not much for talking, huh?"
    ao "..."
    scene ch1ep4_531
    with dissolve
    pause
    scene ch1ep4_532
    with dissolve
    f "She's an odd one."
    yt "... I don't know what those bioluminescent eyes were telling me. Could she be..."
    yt "What are the chances, right?"
    scene ch1ep4_533
    with dissolve
    mc "... I see."
    f "Hm?"
    stop music fadeout 2
    stop sound fadeout 2
    $ renpy.sound.set_volume(1.0, 1.0)
    play sound2 festivalcrowd loop fadein 2
    play sound3 traffic loop fadein 2 
    scene black
    with dissolve
    scene ch1ep4_534
    with dissolve
    pause
    scene ch1ep4_535
    with dissolve
    pause
    scene ch1ep4_536
    with dissolve
    m "..."
    stop sound2 fadeout 2
    stop sound3 fadeout 2
    scene ch1ep3p2_791
    with flash
    mc "Well, why not start by exploring what you like? There must be things you're interested in."
    m "I guess... I haven't really thought about it. I've always been focused on things specifically assigned to me."
    mc "Look, Moon, you've got skills, not just bodyguard-ing. There's more to you than just that."
    mc "I know you're committed to your duty, but isn't it time to explore what else life has for you? You've been at a crossroads since graduation, haven't you?"
    play sound2 festivalcrowd loop fadein 2
    play sound3 traffic loop fadein 2 
    scene ch1ep4_536
    with flash
    m "..."
    scene ch1ep4_537
    with dissolve
    m "*taking a deep breath*"
    stop sound2 fadeout 2
    stop sound3 fadeout 2
    
    scene black
    with dissolve
    with fadeq
    
    play music 'audio/Maskros.mp3'
    scene ch1ep4_538
    with dissolve
    au "While I'm aware of your connection to Jess, I must emphasize that it doesn't influence our hiring process. Everyone is evaluated on the same criteria here."
    au "Currently, we don't have openings that match your skill set. However, if you're interested in a janitorial position, we can immediately offer that opportunity."
    scene ch1ep4_539
    with dissolve
    m "..."
    au "Is this your first job application?"
    scene ch1ep4_540
    with dissolve
    m "Yes. I just graduated."
    au "I see. The job market is broad; there are many opportunities out there."
    au "I can provide you with some recommendations for where to apply next. That's the best assistance I can offer at the moment."
    m "Thank you."
    au "Oh. On the less professional side, please give my regards to Jess."
    m "I will."

    scene black
    with dissolve
    with fadeq

    scene ch1ep4_541
    with dissolve
    m "I'm a hardworking individual with a passion for learning and growing. I believe my skills would be a great fit for any role."
    sophia "I appreciate your enthusiasm, but I'm afraid your qualifications don't quite match what we're looking for at the moment."
    m "Then what are you looking for?"
    sophia "Keep working on your skills, and feel free to apply again in the future!"
    m "Hm?"

    scene black
    with dissolve
    with fadeq

    scene ch1ep4_542
    with dissolve
    claire "Good morning, Moon. I've reviewed your application. Can you elaborate on your experience in this field?"
    m "Well, I may not have extensive experience, but I'm a quick learner and always eager to take on new challenges."
    claire "While we value your willingness to learn, this position requires a certain level of expertise."
    claire "I'm sorry, but we'll have to pass on your application this time."

    scene black
    with dissolve
    with fadeq

    scene ch1ep4_543
    with dissolve
    jane "Hello, Moon. Thank you for showing interest in our law firm. I've taken the time to review your application and résumé thoroughly."
    m "Oh, uhm, thank you so much for considering my application. I'm really grateful for the opportunity."
    jane "I want to be transparent with you from the start."
    jane "You have a commendable background, but it seems you lack direct experience in a legal environment."
    scene ch1ep4_544
    with dissolve
    m "Yes, I'm aware of that. I... Is there something I can do to fit in?"
    jane "Unfortunately, I don't think there is anything for you here."
    jane "The role we're filling demands a robust understanding of legal practices and firsthand experience."
    jane "Our firm is committed to upholding the utmost level of professionalism and legal acumen."
    scene ch1ep4_545
    with dissolve
    m "I see. It makes sense..." #
    jane "I recommend exploring opportunities to further your education in law or seek out positions that can provide practical experience."
    jane "It could significantly enhance your profile for future applications."
    jane "Please, Moon, don't let this setback deter you."
    jane "Continue to pursue your professional ambitions, and I'm confident you'll discover an opportunity that perfectly matches your skills and goals."

    scene black
    with dissolve
    with fadeq

    scene ch1ep4_546
    with dissolve
    mall "..."
    m "..."
    scene ch1ep4_547
    with dissolve
    mall "You have no idea what you've gotten into, do you?"
    m "Um... where am I?"
    mall "Although we have vacancies, this is an Adult Company you're applying to."
    m "Adult... Company?"
    scene ch1ep4_548
    with dissolve
    mall "The pornography industry, to put it simply. I can't fit you in here unless you want to become an adult video actress."
    mall "You have a lot of potential. You look cute and have just the right curves to appeal to a mass audience. I'm sure I can pair you up with someone."
    mall "So, how about it?"
    scene ch1ep4_549
    with dissolve
    m "I can't. My husband will get mad at me."
    mall "You're married?"
    m "... Technically."
    mall "Technically?"
    scene ch1ep4_550
    with dissolve
    m "Yes. But thank you for the offer."
    scene ch1ep4_551
    with dissolve
    pause
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound gymcrowd loop
    play sound2 closedoor2
    play music 'audio/LookInto.mp3'
    scene ch1ep4_552
    with dissolve
    pause
    scene ch1ep4_553
    with dissolve
    pause
    scene ch1ep4_554
    with dissolve
    m "Excuse me."
    kai "Oh hey, a new fitness enthusiast?"
    m "No, I'm-{w=0.5}{nw}"
    scene ch1ep4_555
    kai "Millie! We have someone interested in signing up!"
    scene ch1ep4_556
    kai "Where is she?"
    nik "Она в туалете."
    kai "Tell her to hurry up. There's no one at the front desk."
    nik "Хорошо."
    scene ch1ep4_557
    with dissolve
    m "Actually, I'm here to apply for a job, not to sign up for a membership."
    kai "Oh? A job, you say? Right, we do have an opening."
    m "I heard there's an opening for a hand-to-hand combat instructor. I have years of experience and believe I'm a good fit for the job."
    scene ch1ep4_558
    kai "Ha! That may be true, but you seem a bit on the slim side. This job requires someone who can hold their own in a fight."
    m "My size isn't a drawback. In a real fight, skill is what counts."
    kai "Yeah? Alright then, how about this? Prove to me you can handle the job."
    kai "Show me what you've got, then I'll think about it."
    m "Okay."
    stop sound fadeout 2
    scene black
    with dissolve
    pause 1.0
    play sound2 cloth
    scene ch1ep4_559
    with dissolve
    m "Are you sure about this? I wouldn't want to hurt you."
    kai "Don't worry about me. I can take it."
    scene ch1ep4_560
    with dissolve
    pause
    scene ch1ep4_561
    with dissolve
    m "..."
    kai "Why the wait? Let's-{w=0.7}{nw}"
    play sound2 woodcrash
    show ch1ep4_562
    with hpunch
    kai "Hhrrkk...! I... can't... breathe! L-let up!"
    m "Like I said, size isn't everything. Underestimating others is what kills you on the battlefield."
    kai "Okay, okay, you've proved your point! Let me go!"
    play sound closedoor
    scene ch1ep4_563
    with Dissolve(0.2)
    mill "What's going on here?"
    nik "Эта девушка подает заявление на работу."
    mill "Applying for a job? But..."
    scene ch1ep4_564
    with dissolve
    m "So, am I hired?"
    kai "*coughing* Yeah, I think you're good enough..."
    m "Thank-{w=0.5}{nw}"
    scene ch1ep4_565
    mill "Hold on!"
    m "Hm?"
    scene ch1ep4_566
    with dissolve
    mill "Hi there, miss. I'm Millie, the gym manager."
    mill "You're applying for the combat instructor role, right? Unfortunately, we just filled that position yesterday."
    m "I see... That's disappointing..."
    scene ch1ep4_567
    kai "Filled? But you haven't closed the job posting yet!"
    mill "Well... my fault..."
    kai "It was a guy, wasn't it?"
    mill "Yes."
    kai "Come on, Millie! She just showed she's more than qualified! Kick him out, I don't like him already! We need more women in here!"
    mill "*sighs* You know I can't just do that..."
    scene ch1ep4_568
    with dissolve
    mill "However, the new hire is only on a five-month contract. It's not permanent."
    m "So there's a possibility it'll open up again?"
    mill "Exactly. And given what I've just seen, I'd be very interested in having you join us then."
    scene ch1ep4_567
    kai "Seriously, Millie, consider making a switch now! Nikolay, tell her!"
    nik "Нет."
    mill "Kai, as much as I share your enthusiasm, we need to honor our commitments."
    scene ch1ep4_568
    with dissolve
    mill "But... what was your name?"
    m "Moon. Moon Chi."
    scene ch1ep4_569
    with dissolve
    mill "Moon, please consider coming back once the position reopens. With your skills, you'd be an excellent addition."
    m "..."
    m "... Alright, I'll consider it."
    scene ch1ep4_567
    kai "You're making a big mistake, Millie!"
    mill "Let it go, Kai. Let's be professional."
    scene ch1ep4_569
    with dissolve
    mill "I'll be sure to reach out as soon as there's an opening, Moon. It was a pleasure meeting you. Sorry for any confusion today."
    m "It's okay."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound2 festivalcrowd loop fadein 2
    play sound3 traffic loop fadein 2
    scene ch1ep4_570
    with dissolve
    m "..."
    play sound sniperrechamber2
    play music 'audio/SniperInSight.mp3'
    scene ch1ep4_571
    with Dissolve(0.1)
    pause
    scene ch1ep4_572
    pause
    scene ch1ep4_573
    with Dissolve(0.1)
    pause
    play sound5 cloth2
    play sound sniperfire
    scene ch1ep4_574
    with hpunch
    pause 0.5
    play sound4 bodyfall2
    stop sound2 fadeout 1
    play sound crowd_chaos loop fadein 1
    scene ch1ep4_575
    with hpunch
    pause
    $ renpy.sound.set_volume(0.3, 1.0)
    show twosniperscope
    with dissolve
    pause 7.0
    play sound2 sniperrechamber2
    scene ch1ep4_576
    pause 0.2
    scene ch1ep4_577
    pause 0.2
    scene ch1ep4_578
    pause 0.5
    scene ch1ep4_579
    with Dissolve(0.2)
    pause
    scene ch1ep4_580
    with hpunch
    m "{size=+10}{b}AOIFEEEEEEEEE!!!"
    stop sound3 fadeout 2
    stop sound fadeout 2
    scene black
    with Dissolve(0.2)
    $ renpy.sound.set_volume(1.0, 1.0)
    scene ch1ep4_581
    with dissolve
    mc "Frey, are you done yet? Let's hurry! It's getting late!"
    f "Hold your horses! I'm almost ready!"
    play sound carpark
    scene ch1ep4_582
    with dissolve
    pause
    play sound2 cardoorclose
    scene ch1ep4_583
    with dissolve
    mc "..."
    yt "So, the circus is in town. Just as I predicted..."
    yt "And look who's playing ringmaster..."
    yt "Frey, I swear, if you jump out now..."
    scene ch1ep4_584
    with dissolve
    f "..."
    play sound bodyfall2
    scene ch1ep4_585
    with hpunch
    f "*gasps*"
    scene ch1ep4_586
    with dissolve
    mc "Ah, if it isn't Mr. Pretzel-Octopus himself. Can't stay away from me, huh?"
    mc "What's the matter? Run out of people to annoy, so you brought your fan club here to impress me?"
    scene ch1ep4_587
    with dissolve
    mc "Really, I'm dying to know—what kind of stick got wedged up your ass this time? What do you want from me now?"
    fr "Ugh, your sarcasm is like nails on a chalkboard!"
    scene ch1ep4_588
    with dissolve
    fr "What do I want? Revenge, my dear simpleton!"
    fr "Did you think I'd forget how you made a fool out of me? I'm here to make you regret it, tenfold!"
    scene ch1ep4_589
    fr "Seize him!"
    play sound punch
    scene ch1ep4_590
    with hpunch
    fr "Ack!{w=0.5}{nw}"
    play sound bodyfall2
    scene ch1ep4_591
    with hpunch
    pause
    scene ch1ep4_592
    with Dissolve(0.1)
    fr "M-m-my face! My precious, priceless face!!"
    fr "Do you have any idea how much my beauty routine costs?!"
    scene ch1ep4_593
    with dissolve
    mc "Oh, look at little Pretzel-O-Pus Junior..."
    mc "Gonna cry?"
    fr "What are you imbeciles waiting for? Get him!"
    scene ch1ep4_594
    with Dissolve(0.1)
    yt "Moon..."
    yt "... I'm sorry."
    play sound punch
    scene black
    with hpunch
    pause
    scene ch1ep4_595
    with dissolve
    pause
    fr "*nervous chuckle*"
    fr "HAHAHAHAHA!!"
    fr "Let's see if you can crack jokes now, wise guy!"
    fr "Drag him in!"
    play sound cardriveaway
    scene ch1ep4_596
    with dissolve
    pause
    scene ch1ep4_597
    with dissolve
    f "Did they..."
    f "No..."
    scene ch1ep4_598
    with Dissolve(0.2)
    f "No, no, no, NO!"
    scene black
    with Dissolve(0.2)
    pause 0.5
    play sound sniperfire
    scene ch1ep4_599
    with hpunch
    pause 0.5
    play sound2 gravelslide
    scene ch1ep4_600
    with hpunch
    m "Her aim is just as sharp as it was. Did she intentionally miss that second shot, or..."
    m "... What is she plotting now?"
    scene ch1ep2_88
    with flash
    pause 1.0
    scene ch1ep4_600
    with flash
    m "This feels just like back then."
    m "Once she has you in her sights, there's no escaping."
    play sound cloth
    scene ch1ep4_601
    with Dissolve(0.1)
    m "Her only weakness is close combat. I need to find a way to get close-"
    scene ch1ep4_602
    with Dissolve(0.1)
    m "Ugh!"
    scene ch1ep4_603
    with Dissolve(0.1)
    m "How are you still alive, Aoife?! After all these years, why show your face to me now?!"
    ao "..."
    m "... You're still mouthless, I see. Why did I even bother asking?"
    play sound running loop
    scene ch1ep4_604
    with Dissolve(0.1)
    pause
    stop sound
    scene ch1ep4_605
    with Dissolve(0.1)
    m "Tsk!"

    scene black
    with dissolve
    with fade

    scene ch1ep4_606
    with dissolve
    pause
    play sound gateclose
    scene ch1ep4_607
    with dissolve
    fr "Well, well, well. Not so cocky now, are we?"
    fr "I do hope you're enjoying our deluxe accommodations. Only the best for my esteemed guest!"
    mc "Francis, you spineless worm. If you're going to bore me to death, just get it over with already."
    fr "Oh no, no, no! We have far more things in store for you."
    scene ch1ep4_608
    with dissolve
    fr "Allow me to introduce you to my associate here."
    fr "This is Malice. He's positively brilliant at extracting information. But we won't need that from you."
    fr "I'm looking forward to your screams. Lots of delightful screams."
    scene ch1ep4_609
    with dissolve
    mal "Hello, [mc]. We're going to become very... intimately acquainted."
    mal "I can't tell you how eager I am to take care of you."
    scene ch1ep4_610
    with dissolve
    mal "Shall we begin? I have so many wonderful toys to show you."
    mc "..."
    fr "Not so chatty anymore, hm? No matter. You'll be singing soon enough."
    fr "I'll leave you two to get better familiarized."
    scene ch1ep4_611
    with dissolve
    fr "Remember, my friend - make it hurt."
    mal "With pleasure. This one seems like he'll last a while. The tough ones are always the most fun to break."
    play sound gateclose
    scene ch1ep4_612
    with dissolve
    mal "*chuckles* Now then. Let's put a lovely smile on that face, shall we?"
    mc "You look absolute shit, by the way. Has anyone ever told you that?"
    mal "Oh yeah? Let's see how long you can keep that attitude up."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound windgrass loop
    scene ch1ep4_613
    with dissolve
    pause
    play sound2 heartbeat_single
    scene ch1ep4_614
    with Dissolve(0.1)
    m "!!!"
    scene ch1ep4_615
    with dissolve
    pause
    scene ch1ep4_616
    with dissolve
    pause
    scene ch1ep4_617
    with Dissolve(2.0)
    pause
    scene ch1ep4_618
    with Dissolve(0.1)
    pause
    play sound2 running loop
    scene ch1ep4_619
    with Dissolve(0.1)
    m "Please be in there, please be in there...!"
    stop sound2 fadeout 2
    scene black
    with dissolve
    pause 0.5
    play sound closedoor
    play music 'audio/AbsintheMinded.mp3'
    scene ch1ep4_620
    with dissolve
    shu "Shit, shit, shit!"
    e "No, this won't do, I'm going to find him myself!"
    g "Without any leads or clues? Surely you're not the type to charge ahead without plans, Em!"
    e "Then what do you propose I should do?!"
    g "I don't know, okay? Just stay put and wait for them to arrive!"
    s "*crying* [mc]...!"
    k "Huh? C-can you say that again? I couldn't hear you."
    scene ch1ep4_621
    with Dissolve(0.2)
    a "Ugh..."
    play sound woodhit
    show ch1ep4_622
    with hpunch
    a "EVERYBODY, SHUT THE FUCK UP! YOUR CRIES ARE NOT HELPING!"
    k "... Thank you, dear."
    scene ch1ep4_623
    with Dissolve(0.2)
    k "Yes, I'm sorry about that..."
    "....."
    k "Yes, yes! We're all safe! Please hurry!"
    "........"
    k "You're almost here? Okay, I understand!"
    scene ch1ep4_624
    with Dissolve(0.2)
    f "I'm so sorry, I couldn't do anything~!"
    g "It wasn't your fault, Freya. We're just thankful you didn't get involved too. It could've been much worse."
    scene ch1ep4_625
    with dissolve
    pause 0.7
    play sound teardrop
    scene ch1ep4_626
    with Dissolve(0.2)
    pause 0.5
    play sound2 teardrop
    scene ch1ep4_627
    with Dissolve(0.2)
    pause
    scene ch1ep4_628
    with dissolve
    pause
    scene ch1ep4_629
    with Dissolve(0.1)
    a "You! Where the hell have you-!"
    scene ch1ep4_630
    with Dissolve(1.0)
    a "..."
    scene ch1ep4_631
    with Dissolve(1.0)
    pause
    scene ch1ep4_632
    with Dissolve(2.0)
    pause 0.5
    e "Moon..."
    scene ch1ep4_633
    with dissolve
    m "Where is he?"
    scene ch1ep4_634
    with dissolve
    a "..."
    scene ch1ep4_635
    with dissolve
    f "... That Francis guy! They took him...!"
    f "*sobs* I'm sorry, Moon! I was with him, but I couldn't do anything!"
    play sound bodyfall2
    scene ch1ep4_636
    with hpunch
    pause
    scene ch1ep4_637
    with Dissolve(1.0)
    m "*wailing* HHNNK~! AAAHK~!"
    scene ch1ep4_638
    with Dissolve(0.2)
    m "Why does this hurt so bad...?"
    m "Why?! I don't get it! This shouldn't be happening to me...!"
    play sound closedoor
    scene ch1ep4_639
    with dissolve
    pause
    scene ch1ep4_638
    with Dissolve(0.2)
    m "These feelings aren't mine; they're from the one inside me. But..."
    m "But... deep down, in my own heart... I'm desperately yearning for him..."
    m "No, I can't bear the thought of losing him~! I need to be by his side~!"
    scene ch1ep4_640
    with dissolve
    el "I've... never seen her break down like that..."
    j "I bet no one ever has... Even herself."
    cl "Aveline and Lucien have a different kind of relationship, so I can't say I completely relate to her."
    cl "But if there's one more thing that's common in all serum users, it's their conflicting emotions."
    cl "It's an intensely complicated feeling where you experience multiple emotions simultaneously."
    cl "Aveline tends to push her emotions towards me, making them mine. At the same time, my own emotion triggers along with it, fighting Aveline's back."
    cl "However, in Fang's case, her and Lady Sora's emotions aren't colliding..."
    cl "Her bond with [mc] eventually made her feelings align with Lady Sora's, which means Fang feels twice the intensity when it triggers."
    cl "And I believe this is a first for her..."
    play sound cloth
    scene ch1ep4_641
    with dissolve
    j "Don't worry. We haven't lost him just yet."
    j "Thanks to Freya's swift actions, we were alerted immediately."
    scene ch1ep4_642
    with dissolve
    el "Come on, Fang. I'll show you something."
    scene ch1ep4_643
    with dissolve
    el "Uh, if I may."
    play sound keyboardtype_fast loop
    scene ch1ep4_644
    with dissolve
    el "Take a look at this..."
    el "By leveraging my comprehensive integration with the urban closed-circuit television network architecture, I methodically derived the vehicular trajectory employing advanced tracking algorithms."
    stop sound
    scene ch1ep4_645
    with Dissolve(0.1)
    j "English, please, Eliza."
    el "Oh, sorry."
    scene ch1ep4_644
    with dissolve
    el "Well, I tapped into the city's CCTV network and managed to track their van."
    el "Based on their last known location, he's here."
    scene ch1ep4_646
    with dissolve
    shu "So you're a hacker."
    el "Yeah!"
    shu "And the government doesn't know this?"
    el "Nope!"
    scene ch1ep4_647
    with dissolve
    m "Where is that?"
    j "It's an unmarked site in our records. Likely one of Mentzelopoutous' hideouts as we had no information about them."
    el "That area lacks CCTV coverage, but there's only one way in and out given the layout. They must have taken him there."
    el "I'm currently monitoring all nearby cameras, so if they move, we'll catch it."
    stop music fadeout 2
    play music2 'audio/Impasse.mp3' fadein 2
    scene ch1ep4_648
    with Dissolve(0.3)
    cl "And where do you think you're heading?"
    m "This is my responsibility, Owl. I failed to do my job. I will fix this alone."
    scene ch1ep4_649
    with dissolve
    cl "That's not happening, Fang. At a time like this, we should be working together."
    play sound cloth2
    scene ch1ep4_650
    j "Stand back."
    scene ch1ep4_651
    with Dissolve(0.2)
    m "Since when did \"teamwork\" become part of your lexicon?"
    m "I said it's my burden to bear. Besides, what the hell could you possibly do to help?"
    cl "Are you mocking me?"
    m "Yes."
    play sound casepickup2
    scene ch1ep4_652
    av "Really now?"
    m "Stand down, Aveline..."
    av "Stand down? This isn't the military, Fang."
    play sound woosh4
    scene ch1ep4_653
    pause 0.7
    play sound2 woodcrash
    scene ch1ep4_654
    pause 0.8
    play sound3 bodyfall
    play sound gravelslide
    scene ch1ep4_655
    pause
    cl "Lance's strength? No, even stronger..."
    cl "Tch... Damn you, Yuna..."
    play sound closedoor
    play sound2 cloth2
    scene ch1ep4_656
    with Dissolve(0.1)
    j "No, let them be."
    j "Once they clash, no one can stop them. Not even us in the Agency."
    k "But, I can't just..."
    j "Don't worry. It takes a beast to tame another."
    scene ch1ep4_657
    with dissolve
    m "Now tell me again, what can you do?"
    cl "*chuckles* Even Aveline would shake at that...?"
    cl "I see... So this is why Lance picked you."
    cl "Fine, I'll back off. Arguing with you is pointless, as always."
    m "That's right... You're weak."
    scene ch1ep4_658
    with Dissolve(0.1)
    m "You're all weak. Always relying on others to solve your problems. You can't do anything on your own."
    scene ch1ep4_659
    with Dissolve(0.1)
    m "But I'm different. I'm stronger. Stronger than all of you."
    m "So go ahead, sit here and bawl your eyes out. I'll handle this myself."
    play sound fistbump
    scene ch1ep4_660
    with hpunch
    m "Get your hands off me."
    scene ch1ep4_661
    with dissolve
    a "Is she serious?! Doing it on her own?!"
    j "To protect you all."
    a "I mean, I get it, but still...!"
    scene ch1ep4_662
    with dissolve
    j "Fang is not one to mock other people's capabilities. I think, in her own way, it's her means of coping with the pressure."
    j "She's always been uncertain of what she wants to do. But for once, she's making a choice on her own."
    j "Let her go. We can only hope for the best."
    a "..."
    scene ch1ep4_663
    with dissolve
    a "... No, I can't just sit by. Regardless of her strength, she's still human. And this is [mc]'s life at stake."
    scene ch1ep4_664
    with dissolve
    a "Em, are you coming with me?"
    e "Anywhere."
    a "Get ready, we're leaving."
    scene ch1ep4_665
    with dissolve
    j "Where are you going?"
    a "Back to where I came from."
    j "I understand. Do what you think is best. I entrust them to you."
    scene ch1ep4_666
    with dissolve
    k "I hate my powerlessness, but, Aine, please... bring them back safely."
    a "I will. You have my word."
    stop music2 fadeout 2
    $ renpy.music.set_volume(1.0, 1.0)
    $ renpy.sound.set_volume(1.0, 1.0)

    scene black
    with dissolve
    with fade

    mal "Wakey, wakey!"
    play music 'audio/Symphony7.mp3'
    play sound waterpour_bucket
    show ch1ep4_667
    pause 0.6
    play sound2 sizzle
    play sound3 agony
    scene ch1ep4_668
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    play sound dyinggasps loop
    scene ch1ep4_669
    with dissolve
    mc "*huff* *huff*"
    show keivisionshake
    with Dissolve(1.0)
    yt "Huh...? How long have I been stuck here...?"
    yt "Is this the price I have to pay for wanting to uncover the truth...?"
    yt "I just wanted answers, to understand why the world could be so cruel and unfair..."
    yt "But now, here I am, caught in this bad dream, hurting more than I ever thought possible..."
    yt "Why does wanting to know more and find peace end up like this...?"
    yt "My body's giving up, and it's hard to keep hoping, but I can't stop wanting to know..."
    yt "I have to find out the truth, to make sense of all this. Even if it hurts..."
    yt "But every new pain makes me wonder if it's worth it..."
    yt "Is this what happens to people who dare to question...? To those who look for a little bit of light...?"
    yt "Or am I just another casualty of the cruelty and injustice that pervades this world...?"
    yt "I don't know how much more I can handle, but I can't give up. I have to believe there's a reason for all this pain..."
    yt "... I wonder how Moon is doing without me..."
    yt "*chuckles* She's been like a baby... seeking for my presence all the time..."
    scene ch1ep4_670
    with dissolve
    hide keivisionshake
    mal "Ah, there you are! Back from a little dream world, are we?"
    mal "You know, you're quite a fascinating case. Most people would have broken by now, but not you."
    mal "It's almost like you enjoy the pain, like you're clinging to it as some twisted lifeline."
    mal "But I can see it in your eyes: desperation and fear. You're wondering how long you can hold out. Isn't that so?"
    scene ch1ep4_671
    with dissolve
    mal "Well, let me tell you a little secret..."
    mal "I'm just getting started. We've got plenty of time to explore the depths of your suffering."
    mal "And I've got a very {i}special{/i} treat for you..."
    mal "You see, I've been thinking about how to make this even more exquisite for you."
    mal "So, I've decided to let the room cool down a bit."
    mal "The chill will seep into your bones, making every cut, every burn, every broken piece of you scream in agony."
    mal "It's a delightful contrast, don't you think? The searing heat of pain against the icy grip of despair."
    scene ch1ep4_672
    with dissolve
    mal "And just when you think you can't take anymore, when you're ready to beg for mercy, I'll bring you back from the brink, only to start all over again."
    mal "Because you can't give up just yet, [mc]. We've got so much more playtime ahead of us. And I intend to savor every moment of your suffering."
    mal "So, go ahead. Cling to your precious truth, your pathetic hopes. They'll only make your fall that much sweeter."
    scene ch1ep4_673
    with dissolve
    mal "Now, let's see how long you can last in the cold embrace of my affection, yeah?"
    play sound2 gateclose
    play sound3 powerdown
    scene ch1ep4_674
    with Dissolve(2.0)
    pause
    yt "Everyone... I'm sorry... I don't know if I can make it back to you..."
    stop sound fadeout 2
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    play sound closedoor
    play music 'audio/Imperium.mp3'
    scene ch1ep4_675
    with dissolve
    pause
    play sound caseopen
    scene ch1ep4_676
    with dissolve
    pause
    scene ch1ep4_677
    with dissolve
    pause
    scene ch1ep4_678
    with dissolve
    pause
    play sound casepickup2
    scene ch1ep4_679
    with dissolve
    pause
    play sound2 katana_open
    scene ch1ep4_680
    with Dissolve(0.2)
    m "..."
    play sound chime_bell
    scene ch1ep4_681
    with Dissolve(0.1)
    pause 0.5
    av "You can run as far as you like, but escaping who you are is impossible. You've taken thousands of lives."
    av "Struggle as you might to distance yourself from your past, it won't change a thing."
    av "You can try to be a bodyguard... {w}a savior..."
    av "... {b}A lover{/b}."
    play sound2 katanasheath
    scene ch1ep4_682
    with Dissolve(0.2)
    m "..."
    av "Yet there is a truth that clings to you, one that you cannot simply forget..."
    av "Despite your efforts, you cannot erase the fact that you are..."
    scene ch1ep4_683
    with dissolve
    av "A monster..."
    scene ch1ep4_684
    with dissolve
    m "I know what I've done, Aveline. I live with the weight of my actions every single day."
    av "Please, save the dramatics. You forfeited the right to sympathy the moment you walked onto your path."
    av "And now, [mc] is in peril because of your mistake, the one soul who managed to look beyond the monster that you are..."
    m "I never wanted any of this. I'll risk everything to protect him, even if it's the last thing I do."
    av "You'd better. Should death come to him, you'll find yourself drowning in blame."
    play sound cloth
    scene ch1ep4_685
    with dissolve
    m "I don't need your words, Aveline..."
    m "After all, you're not any different than me."
    play sound closedoor
    scene ch1ep4_686
    with dissolve
    av "*chuckles*"
    scene black
    with dissolve
    scene ch1ep4_687
    with dissolve
    pause
    $ renpy.music.set_volume(0.7, 1.0)
    play sound snowfall loop
    scene ch1ep4_688
    with Dissolve(2.0)
    pause
    scene ch1ep4_689
    with Dissolve(1.0)
    pause
    scene ch1ep4_690
    with dissolve
    pause
    scene ch1ep4_691
    with dissolve
    j "Good luck."
    scene ch1ep4_692
    with dissolve
    m "After everything's settled, I want to be [mc]'s full-time aide."
    j "Is that a lifeline to grasp at, or a duty you feel compelled to take?"
    play sound2 cloth
    scene ch1ep4_693
    with Dissolve(2.0)
    m "Neither..."
    m "It's a decision I've made because it is what I want."
    j "..."
    scene ch1ep4_694
    with dissolve
    j "Seriously, waking up now of all times."
    j "I understand, but... it's unnecessary. The call wasn't mine to make in the first place."
    j "Ultimately, Lance chose you to lead the clan..."
    stop music fadeout 2
    stop sound fadeout 2
    $ renpy.music.set_volume(1.0, 1.0)

    scene black
    with dissolve
    with fade

    play music2 'audio/CreepyCockroachINST.mp3'
    scene ch1ep4_696
    with dissolve
    pause
    scene ch1ep4_695
    with Dissolve(1.0)
    pause
    scene ch1ep4_697
    with Dissolve(2.0)
    m "Beneath the suffocating grip of twilight's gloom..."
    m "I stand, a sentinel in fate's unyielding tomb."
    m "Moon aloft, a silent witness to my plight..."
    m "Through shadows' menace, in darkness I ignite."
    scene ch1ep4_698
    with dissolve
    m "As a huntsman revels in the chase's bloody wake..."
    m "I offer thanks for the power thou dost make."
    m "For foes laid waste and victories hard-won..."
    m "A feast of carnage, when the hunt is done."
    scene ch1ep4_699
    with dissolve
    m "In this eerie calm, before the tempest's roar..."
    m "I am the stalker, and the night's grim core."
    m "Bless the steel I bear, merciless and cold..."
    m "Let my strike be lethal, my resolve untold."
    scene ch1ep4_700
    with dissolve
    m "For the lives I reap, like the harvest moon's blight..."
    m "I pray their end be brutal, devoid of light."
    m "Grant me dominion as I tip the scales..."
    m "In the dance of blades, where terror prevails."
    scene ch1ep4_701
    with dissolve
    m "I thank thee for the curse, the savage might I bear..."
    m "In this waltz of ruin, upon the field of despair."
    m "May the wailing night choke on their final breath..."
    stop music2 fadeout 4
    scene ch1ep4_702
    with dissolve
    m "As I embrace my fate, the harbinger of death."
    play music 'audio/CreepyCockroach.mp3' fadein 2
    play sound gravelslide
    scene ch1ep4_703
    with dissolve
    play sound2 katana_open
    pause 2.0
    play sound katana_impact
    scene ch1ep4_704
    with flashq
    pause 1.0
    play sound2 woosh2
    play sound3 bodyfall
    scene ch1ep4_705
    with Dissolve(0.1)
    pause 1.0
    play sound katana_stab
    scene ch1ep4_706
    pause 1.0
    play sound3 bodyfall2
    play sound2 woosh2
    scene ch1ep4_707
    with Dissolve(0.1)
    pause 1.0
    play sound katana_stab2
    scene ch1ep4_708
    pause 1.0
    play sound3 bodyfall
    play sound2 katanasheath2
    scene ch1ep4_709
    with Dissolve(0.1)
    pause 1.0
    $ renpy.music.set_volume(0.5, 1.0)
    play sound moonmassacre
    scene ch1ep4_710
    with Dissolve(0.2)
    pause 13.0
    $ renpy.music.set_volume(1.0, 1.0)
    play sound running loop
    scene ch1ep4_711
    with Dissolve(0.1)
    pause 1.0
    stop sound
    $ renpy.music.set_volume(0.5, 1.0)
    show moonslashes
    pause 2.0
    scene black
    with dissolve
    pause 0.2
    $ renpy.music.set_volume(1.0, 1.0)
    play sound2 katana_impact
    scene ch1ep4_712
    with flashq
    pause
    play sound bodyfall
    play sound2 bodyfall2
    scene ch1ep4_713
    with dissolve
    pause
    scene ch1ep4_714
    with dissolve
    m "I'm confused. Why not shoot? I'm right here."
    play sound running loop
    scene ch1ep4_715
    with Dissolve(0.1)
    pause 1.0
    stop sound
    play sound2 katana_impact
    scene ch1ep4_716
    pause
    play sound bodyfall
    scene ch1ep4_717
    with dissolve
    m "*huff*... *huff*..."
    stop music fadeout 10
    scene ch1ep4_718
    with dissolve
    m "..."
    scene black
    with dissolve
    scene ch1ep4_719
    with dissolve
    pause
    scene ch1ep4_720
    with dissolve
    m "..."
    play music2 'audio/Impasse.mp3'
    play sound closedoor2
    scene ch1ep4_721
    with dissolve
    pause
    scene ch1ep4_722
    with dissolve
    pause
    scene ch1ep4_723
    with Dissolve(2.0)
    pause
    scene ch1ep4_724
    with dissolve
    pause
    scene ch1ep4_725
    with dissolve
    pause
    scene ch1ep4_726
    with dissolve
    m "{i}We're in close quarters. She should be at a disadvantage. But why do I feel..."
    m "{i}No, now is not the time to underestimate anybody."
    m "{i}Her real strength was always her endurance and patience... A quality of a real marksman."
    m "{i}I wonder, how will she-"
    scene ch1ep4_727
    with Dissolve(0.1)
    ao "I remember the time when we were friends, Four... You, me, Six, and Eight..."
    ao "I've always wondered: Why does it have to be like this...? Why couldn't you simply join my side...?"
    scene ch1ep4_728
    m "!!!"
    scene ch1ep4_729
    with Dissolve(0.2)
    ao "Yes, I can speak..."
    ao "Back then, only One ever heard my voice... He loved it..."
    ao "Seeing his smile after hearing me felt like déjà vu... I thought I recognized that smile..."
    ao "And I was right..."
    ao "You weren't the only person searching for answers, Four..."
    ao "One... was my little brother..."
    m "..."
    scene ch1ep4_730
    with Dissolve(0.1)
    ao "And you took him away from me..."
    scene ch1ep4_731
    with Dissolve(0.2)
    m "We both chose our paths, Aoife. His fate was sealed the moment we picked sides."
    ao "I could say the same about your friends..."
    m "{b}{i}Your{/i}{/b} friends."
    ao "They were no longer mine when they chose to follow you..."
    m "Aoife...!"
    scene ch1ep4_732
    with Dissolve(0.2)
    ao "But enough of the past... I'm not here to cram years of backstory in a few sentences..."
    ao "I know you're here for your... friend..."
    m "He's not just a friend! He's my husband!"
    ao "Oh... Well... I guess you already know..."
    m "Where is he?!"
    ao "Right now, he's being tortured for nothing... But that's all I can tell you..."
    scene ch1ep4_733
    with Dissolve(0.1)
    m "[mc]!"
    play sound sniperfire
    scene ch1ep4_734
    play sound3 bullet_whiz
    with hpunch
    pause 0.2
    play sound2 gravelslide
    scene ch1ep4_735
    m "Tsk!"
    scene ch1ep4_736
    with Dissolve(0.2)
    ao "I'm afraid I can't let you do that... Four..."
    m "What do you want from us?! Why join them?!" with hpunch
    ao "I wasn't choosing sides or anything... I joined them because of you..."
    ao "When I heard you were still alive, I took every chance I could get just to look for you..."
    ao "And now, here we are..."
    ao "I have no interest in him, or in any benefits from the creator's organization..."
    ao "My focus is solely on you... and ending your life..."
    scene ch1ep4_737
    with Dissolve(0.2)
    m "... Then let's settle it here."
    ao "Our pasts no longer matter... Right now, this is a fight of vengeance..."
    m "You sure talk too much for a mouthless bitch."
    ao "Only when I choose to open up... But you know, I really {i}hate{/i} that word..."
    m "See if I care."
    stop music2 fadeout 5
    play sound windgrass loop
    scene ch1ep4_738
    with Dissolve(2.0)
    ao "..."
    scene ch1ep4_739
    with Dissolve(2.0)
    m "..."
    stop sound fadeout 2
    play music 'audio/OumaNoHyakki.mp3' fadein 2
    play sound2 gravelslide
    scene ch1ep4_740
    with Dissolve(0.2)
    pause
    play sound3 katana_open
    scene ch1ep4_741
    pause 0.5
    play sound bodyhit
    scene ch1ep4_742
    pause 0.5
    play sound2 swordscrape
    scene ch1ep4_743
    pause 0.5
    play sound whiz_bladeclash
    scene ch1ep4_744
    with hpunch
    pause 0.8
    play sound2 katana_slash2
    scene ch1ep4_745
    pause 0.5
    play sound3 katanasheath2
    play sound gravelslide
    scene ch1ep4_746
    with Dissolve(0.1)
    pause 0.8
    play sound2 gravelslide
    scene ch1ep4_747
    with Dissolve(0.1)
    pause 0.5
    play sound sniperfire
    scene ch1ep4_748
    with hpunch
    pause 0.8
    play sound2 kick_heavy
    scene ch1ep4_749
    with hpunch
    pause 0.3
    play sound3 gravelslide
    scene ch1ep4_750
    with Dissolve(0.1)
    pause
    scene ch1ep4_751
    with dissolve
    m "Tsk!"
    m "{i}I shouldn't have done that!"
    m "{i}All I did was give her the distance she wanted. But if I hadn't, her knife would've pierced my neck."
    m "{i}So she trained herself with knives to counter close-quarters combat. She doesn't have an opening now..."
    m "{i}Regardless, I have no way to counter her bullets at a distance. My best chance is still up close. I have to keep the distance tight."
    m "{i}But my Iaido uses a little distance to emphasize power. I can't rely on it. I need to switch to Kendo."
    scene ch1ep4_752
    with Dissolve(0.2)
    ao "Hearing your tongue clicks is still so satisfying... just like old times..."
    ao "We were created with specific abilities, but that doesn't mean we can't learn new ones, Four..."
    stop music fadeout 3
    play music2 'audio/OniMusashi.mp3' fadein 3
    play sound katanasheath2
    scene ch1ep4_753
    with Dissolve(0.1)
    m "You're right, and I don't have time for you. I'm ending this now..."
    play sound2 katana_open
    scene ch1ep4_754
    with Dissolve(0.1)
    m "So let's see how this goes."
    ao "..."
    scene ch1ep4_755
    with Dissolve(0.2)
    ao "Trying something new, huh? Throwing away your only defense against me..."
    ao "I take that as an insult..."
    scene ch1ep4_756
    with Dissolve(0.2)
    m "What defense?"
    play sound whiz
    play sound2 gravelslide
    scene ch1ep4_757
    pause
    scene ch1ep4_758
    with dissolve
    ao "{i}She didn't lose her speed; in fact, she's..."
    scene ch1ep4_759
    with dissolve
    ao "{i}Much faster...!"
    show moonslashes2
    pause 2.7
    play sound running loop
    scene ch1ep4_760
    with Dissolve(0.1)
    pause 0.8
    stop sound
    play sound2 woosh2
    scene ch1ep4_761
    with Dissolve(0.1)
    pause 0.5
    play sound sniperfire
    scene ch1ep4_762
    with hpunch
    pause 0.3
    play sound2 bullet_whiz
    scene ch1ep4_763
    pause 0.5
    play sound bodyfall2
    scene ch1ep4_764
    with Dissolve(0.1)
    pause 0.1
    scene ch1ep4_765
    with Dissolve(0.1)
    pause 0.1
    play sound3 gravelslide
    scene ch1ep4_766
    with Dissolve(0.1)
    pause 0.5
    play sound whiz_bladeclash
    scene ch1ep4_767
    with hpunch
    pause 1.0
    scene ch1ep4_768
    with Dissolve(0.1)
    m "You can't keep avoiding me, Aoife!"
    ao "I don't have to. I just need one clear shot..."
    play sound katana_stab2
    scene ch1ep4_769
    with hpunch
    pause 0.5
    play sound2 gravelslide
    scene ch1ep4_770
    m "Ngh! Is that all you've got?!"
    play sound katana_impact
    scene ch1ep4_771
    with hpunch
    pause 0.5
    play sound2 running loop
    scene ch1ep4_772
    with Dissolve(0.1)
    pause 0.5
    stop sound2
    show moonslashes3
    pause 3.8
    scene ch1ep4_773
    with Dissolve(0.1)
    ao "Agh...! Damn you, Four...!"
    play sound woosh4
    scene ch1ep4_774
    pause 0.5
    play sound2 kick_heavy
    scene ch1ep4_775
    with hpunch
    pause 0.5
    play sound3 bodyfall
    scene ch1ep4_776
    with hpunch
    pause 0.8
    play sound whiz_bladeclash
    scene ch1ep4_777
    with hpunch
    pause
    scene ch1ep4_778
    with Dissolve(0.1)
    if aoifelives:
        m "It's over, Aoife! Yield!"
        ao "Never...!"
    else:
        m "It's over, Aoife!"
        ao "Not yet...!"
    ao "I will dictate my own fate...!"
    play sound katana_slash2
    scene ch1ep4_779
    pause 0.5
    play sound2 kick_light
    scene ch1ep4_780
    with hpunch
    pause 0.5
    play sound3 kick_heavy
    scene ch1ep4_781
    with hpunch
    pause 0.5
    play sound bodyfall2
    play sound2 running loop
    scene ch1ep4_782
    with hpunch
    pause 0.8
    play sound3 casepickup2
    scene ch1ep4_783
    with Dissolve(0.1)
    pause 0.2
    play sound4 casepickup2
    scene ch1ep4_784
    with Dissolve(0.1)
    pause 0.2
    play sound katana_open
    play sound2 gravelslide
    scene ch1ep4_785
    with Dissolve(0.2)
    pause 0.5
    play sound3 woosh2
    play sound4 gravelslide
    scene ch1ep4_786
    with Dissolve(0.2)
    pause 0.5
    scene ch1ep4_787
    with dissolve
    ao "Goodbye, Moon..."
    play sound windgrass loop
    stop music2 fadeout 2
    scene black
    with Dissolve(0.2)
    un "Aoife."
    un "Her name should be Aoife."
    scene ch1ep4_788
    with Dissolve(0.1)
    ao "Khhhkkk!"
    play sound2 woosh4
    show moondash
    pause 0.5
    play sound3 katana_impact
    scene ch1ep4_789
    with hpunch
    pause
    scene ch1ep4_790
    with dissolve
    m "No... Goodbye, Aoife..."
    play sound2 bagdrop
    play sound3 metaldrop
    scene ch1ep4_791
    with dissolve
    ao "... You win, Four... Finish it..."
    m "Any last words?"
    scene ch1ep4_792
    with Dissolve(1.0)
    ao "Not much left to say, but... I'll say the words I couldn't tell you back then..."
    ao "... Thank you... for giving me my name..." with Dissolve(2.0)
    scene ch1ep4_793
    with Dissolve(0.3)
    m "!!!"
    call hide_days from _call_hide_days_23
    with dissolve
    stop sound fadeout 2
    scene ch1ep4_794
    with flash
    play music2 'audio/FadingAway.mp3'
    eg "Huh? Give each other names? Where did you get that idea?"
    si "Hey, it's not my fault we woke up without names! The others did it too, you know?"
    scene ch1ep4_795
    with dissolve
    m "We do have names."
    si "Yeah, but... didn't they erase our past identities?"
    si "Besides, I don't really want to call you guys by your numbers outside the battlefield!"
    scene ch1ep4_796
    with dissolve
    eg "It makes sense, but I don't want anyone giving me names. I'll choose my own."
    eg "Starting today, I'll go by \"Enigma\"!"
    scene ch1ep4_797
    with Dissolve(0.2)
    si "... Are you crazy?"
    eg "What? You don't like it?"
    scene ch1ep4_798
    with dissolve
    si "Come on, be serious! At least give yourself a proper name!"
    er "... How about \"Erma\"? It's pretty close to Enigma."
    si "There you go! Was that so hard?"
    scene ch1ep4_799
    with Dissolve(0.2)
    er "Are you calling me dumb?!"
    scene ch1ep4_800
    si "Hey, nice to meet you, Erma."
    scene ch1ep4_801
    with dissolve
    er "..."
    scene ch1ep4_802
    with dissolve
    er "... Nice to meet you too."
    scene ch1ep4_803
    with dissolve
    si "Hmm, how about me, though? I've been thinking about it, but couldn't come up with one."
    scene ch1ep4_804
    with dissolve
    er "How about \"Lumi\"? It is derived from the word \"lumen\", which means light."
    er "You're not the calm, tranquil type, but your presence always brings everyone smiles."
    scene ch1ep4_805
    with Dissolve(0.2)
    lu "*gasps* So you do love me~?"
    play sound fistbump
    scene ch1ep4_806
    with hpunch
    er "Get out of my face!"
    lu "Whoops!"
    scene ch1ep4_807
    with dissolve
    two "..."
    m "Hm?"
    scene ch1ep4_808
    with Dissolve(0.1)
    lu "Now it's your turn to be reborn!"
    m "Me?"
    lu "Yeah! Want to choose a name for yourself, Four?"
    m "I don't know. I'm not sure I want one."
    scene ch1ep4_809
    with dissolve
    lu "..."
    scene ch1ep4_810
    with dissolve
    lu "..."
    scene ch1ep4_811
    with dissolve
    lu "... Moon."
    m "Moon? Why?"
    lu "Because you don't have an Odd."
    er "Hey!"
    lu "I'm not insulting her!"
    scene ch1ep4_812
    with dissolve
    lu "But you know, the moon is a solitary sentinel, always hangs alone in the night sky."
    lu "Independent of the twinkling stars that keep it company."
    lu "Right now, you're a lightless moon, but one day, you will eventually find your sun that will make you shine. I really believe that."
    scene ch1ep4_813
    with dissolve
    m "..."
    scene ch1ep4_814
    with dissolve
    m "Okay. I like it."
    scene ch1ep4_815
    with Dissolve(0.2)
    lu "Hm-hmmm!"
    er "I'll never understand your sense of pride, woman."
    scene ch1ep4_816
    with dissolve
    lu "And lastly, Two-{w=1.0}{nw}"
    scene ch1ep4_817
    m "Aoife."
    ao "!!!"
    lu "Huh?"
    m "Her name should be Aoife."
    er "Care to explain?"
    scene ch1ep4_818
    with dissolve
    m "Just because she's beautiful. More so than any of us."
    lu "Well, that's true! Shame she doesn't talk, though."
    m "Do you like it?"
    scene ch1ep4_819
    with dissolve
    ao "*nods*"
    m "I'm glad."
    scene ch1ep4_820
    with dissolve
    m "Ah..."
    eg "She really liked it, huh?"
    lu "I guess that's her way of saying thank you."
    scene ch1ep4_821
    with dissolve
    pause
    stop music2 fadeout 4
    play music 'audio/InPieces.mp3'
    show hesitationisdefeat
    with flash
    show screen day_tuesday with dissolve
    m "Hnngkk...! Khhhkkk...!"
    show hesitationisdefeat2
    with dissolve
    hide hesitationisdefeat
    ao "... You're tired of fighting, aren't you...?"
    m "*cracking voice* Y...Yes!"
    scene ch1ep4_822
    with dissolve
    hide hesitationisdefeat2
    pause
    scene ch1ep4_823
    with dissolve
    ao "Don't be afraid..."
    ao "When this is over, you'll have avenged Lumi and Erma, saved your partner... and I'll finally be reunited with One..."
    ao "This is the end of the line for me, Moon... I don't have the will to live on, but I couldn't bring myself to end it..."
    m "So that's why you..."
    m "... You never intended to kill me..."
    ao "I'm... all tired of this, too... Moon..."
    ao "If I'm to die, I'd rather it be by your hand..."
    if aoifelives:
        scene ch1ep4_509
        with flash
        mc "I'm not saying you have to forgive her. But if there's a chance to stop the fighting, don't let it pass by."
        mc "You have me now, Moon. Just think about that."
        play sound swordimpact
        scene ch1ep4_831
        m "No."
        scene ch1ep4_832
        with dissolve
        ao "Why...?"
        m "Sometimes, I wonder if this is really what Lumi, Erma, or even One would have wanted—us fighting over what's left of their memories. Over their long-lifeless bodies."
        m "If I were to kill you, would they be proud and commend me for doing the right thing? If you killed me, are you sure One would appreciate it?"
        scene ch1ep4_833
        with dissolve
        ao "..."
        m "Every year, we mourn their deaths, the pain comes back."
        m "Will it matter in the end? We are the ones still alive, not them. The choice is ours to make, not theirs."
        m "And if they could see us now, I'm sure Lumi and Erma would do everything to stop us."
        scene ch1ep4_834
        with dissolve
        m "Right now, I'm devoted to one person and intend to be his and his alone."
        m "I refuse to be chained by grievances or forced to do something against my will anymore. It's time to choose for myself."
        m "And I choose to stop the fighting."
        play sound cloth
        scene ch1ep4_835
        with dissolve
        ao "You just can't help but bring up your husband, can you...?"
        m "He's all that matters to me now, Aoife. I don't care about anything else."
        ao "He's #3, right...?"
        m "Yes."
        ao "I see... I won't ask how that came to be..."
        scene ch1ep4_836
        with dissolve
        m "In exchange for letting you live, find a person named Jess Agnor."
        m "I was lost once, and she helped me find my footing again. If you have questions, she's the one you want to talk to."
        m "You said you get to dictate your fate, but I disagree."
        m "The fact that you're still alive means there's still something you can and must do."
        m "Find another purpose and live, just like I did. It's not the end yet, Aoife."
        ao "You really are... such a kind girl..."
        ao "How can you be so...-"
        ao "No, never mind that... What's your plan from here...?"
        m "Rescue my husband. I need any information you can give me."
        scene ch1ep4_837
        with dissolve
        ao "Honestly, I don't know anything... But the creator is in his office..."
        scene ch1ep4_838
        with dissolve
        ao "When you reach the second floor, turn right... It should be the only room in that corridor..."
        ao "And... watch out for that Francis guy..."
        m "Why?"
        ao "I'm not sure, but... he's got major issues..."
        m "I'll keep that in mind."
        ao "Good luck..."
        scene ch1ep4_839
        with dissolve
        ao "Moon...!"
        m  "Yes?"
        ao "Let's talk about the past properly... the next time we meet again..."
        ao "No guns, no blades. Just our hearts."
        ao "I'll look forward to that day."
    else:
        scene ch1ep4_824
        with dissolve
        m "Khhhkkk...! C...close your eyes, Aoife..."
        scene ch1ep4_825
        with dissolve
        ao "Thank you..."
        ao "You really are... such a kind girl..."
        scene ch1ep4_826
        with dissolve
        m "AAAAAAAHHHHH!!"
        play sound katana_impact
        scene ch1ep4_827
        with Dissolve(2.0)
        pause
        play sound2 bodyfall2
        scene ch1ep4_828
        with dissolve
        pause
        play sound cloth2
        scene ch1ep4_829
        with Dissolve(0.1)
        pause
        play sound2 moonscream
        scene ch1ep4_830
        with Dissolve(0.1)
        m "AAAAAAAAAAAAHHHHHHHHHH!!!"
    stop music fadeout 2
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade

    play sound2 closedoor
    play music 'audio/HidingDNA.mp3'
    play sound claps
    scene ch1ep4_840
    with dissolve
    bo "A splendid fight. I must say, I'm thoroughly entertained. I'm glad to be alive to see my strongest creations clash."
    scene ch1ep4_841
    with dissolve
    m "... Entertainment. Is that all we are to you? Us Numbers and the people around you?"
    bo "Not entirely."
    bo "The Chimera Genesis Project began with noble intentions, albeit for my own benefit."
    scene ch1ep4_842
    with dissolve
    bo "When the war between Sha Crea and Glabia erupted, my family was among those poor souls who did not survive."
    bo "I was young and couldn't face the reality, so I sought knowledge that was beyond anyone's imagination."
    bo "Reviving the dead seemed like an impossible dream. Yet, I never ceased in my pursuit."
    bo "Perhaps I reached a point where I was willing to give up everything, even my soul, to acquire the power to reverse fate."
    bo "And so, I did..."
    scene ch1ep4_843
    with dissolve
    m "So your goal really was to revive the dead."
    scene ch1ep4_844
    with dissolve
    bo "With the power of science, I brought my family back. But they were no longer the people I once loved."
    bo "I thought they could harness another's consciousness as their own, but their minds were unstable, and I couldn't control them."
    bo "I had no choice but to end their lives once more."
    m "..."
    scene ch1ep4_845
    with dissolve
    bo "However, the potential of my discovery was undeniable."
    bo "The power to grant strength, heal the wounded, cure any disease, to perform miracles... Do you know what we call that?"
    scene ch1ep4_846
    with dissolve
    bo "A god."
    scene ch1ep4_847
    with dissolve
    bo "I joined the military of Glabia, offering them this power, which they eagerly accepted."
    bo "With their backing and financial assistance, I searched every corner of the world for individuals with remarkable histories."
    bo "And so, I made those individuals fight my battles... That's how you \"Numbers\" came to be."
    m "... Why did you separate me from my Odd?"
    scene ch1ep4_848
    with dissolve
    bo "Ahh... Emperor Kaito and Lady Sora. A truly fascinating piece of history."
    bo "Not just any history, but a love story that marked the world for generations."
    bo "Out of all my experiments, you two are the pinnacle. So much so that I'd say..."
    bo "... You are my masterpieces. With your love for each other, nothing could ever tear you apart."
    bo "But on the battlefield, your connection could have become a liability."
    bo "Considering how Kaito protected Sora, I knew Sora would never allow that to happen again, disrupting the patterns of your creation."
    m "Patterns?"
    scene ch1ep4_849
    with dissolve
    bo "I designed the Odds to protect the Evens. It's their destiny to die for this cause."
    bo "That's how they were created, and that's the purpose of their existence."
    bo "In sacrificing his life, One saved Two from the fire you caused."
    bo "Five and Seven did the same for Six and Eight. All to protect them."
    scene ch1ep4_850
    with dissolve
    bo "[mc] deliberately planned this and made Francis dance in his palm. All to discover our location."
    bo "To end this once and for all."
    bo "I commend his strong will to pull this off, but he will die for you in exchange for all this information, Moon Chi. There's no escaping that fate."
    scene ch1ep4_851
    with dissolve
    m "All this... just for..."
    m "{i}I knew your plan was too convenient for me to believe. So, all that was just to put our minds at ease?"
    scene ch1ep4_10
    with flash
    mc "Yeah, I'm going to be fine."
    scene ch1ep4_851
    with flash
    m "{i}Tsk! You're a liar, Commander..."
    play sound woosh4
    scene ch1ep4_852
    bo "Now then, what will you do? Should you entertain me-{w=2.0}{nw}"
    play sound2 kick_heavy
    scene ch1ep4_853
    pause 0.3
    play sound3 bodyfall2
    scene ch1ep4_854
    with hpunch
    pause 0.3
    scene ch1ep4_855
    with Dissolve(0.2)
    m "I couldn't care less about you and your damn sob story."
    m "What you've told me isn't enough, and killing you would be an act of mercy. Instead, I'm going to take you into Sicae's custody."
    bo "You think you can—{w=1.0}{nw}"
    play sound woodcrash
    play sound2 bonebreak
    scene ch1ep4_856
    with hpunch
    pause 0.5
    play sound3 katana_stab2
    play sound4 swordimpact
    scene ch1ep4_857
    with hpunch
    bo "GAAAAAAAHHKKK!!!"
    scene ch1ep4_858
    with dissolve
    m "These hands have toyed with our fates, our lives..."
    m "What's left is your brain, but I see no way to strip all that knowledge from you without killing you."
    m "However, I'll make sure you lose the remnants of your sanity."
    m "And don't worry, you'll find it far more enjoyable than anything the depths of hell could offer you."
    scene ch1ep4_859
    with dissolve
    bo "*pained chuckle* You'll never be his savior, Moon Chi—no, Lady Sora!"
    m "I never intended to be."
    m "[mc] is the one who forgives, and I thought I'd be the one to bear his sins."
    m "But that will change today, now that you made him experience what true hell is like."
    scene ch1ep4_860
    with hpunch
    bo "You...! Lady Soraaaaaa!"
    scene ch1ep4_861
    with dissolve
    m "Puny god."
    bo "Khhkk!"
    play sound heartbeat_single
    scene ch1ep4_862
    m "!!!"
    m "C...Commander?!"
    bo "*pained chuckle* It's finally happened. He should be dead by now! I told you, there's no escaping his fate!"
    play sound running loop
    scene ch1ep4_863
    with Dissolve(0.2)
    pause
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fade

    scene ch1ep4_864
    with dissolve
    mc "*huff*... *huff*..."
    play sound gateclose
    scene ch1ep4_865
    with dissolve
    mal "Ah, [mc]. Looking rather worse for wear, I see."
    mal "But cheer up, I have news that will... pique your interest."
    scene ch1ep4_866
    with dissolve
    mc "*huff*... *huff*..."
    mal "You see, it seems your precious little girlfriend has decided to play the heroine."
    mal "She's fighting her way through Bonheur's men as we speak, trying to save you."
    mc "Moon..."
    play sound cloth2
    scene ch1ep4_867
    mal "It's quite the spectacle. Her futile efforts, all for you, knowing well it's all in vain."
    mc "You bastard... if you lay a hand on her, I'll..."
    mal "You'll what? You can barely keep yourself conscious, let alone fight back."
    mal "Worry not. I don't plan to harm her... not immediately, anyway."
    mal "In fact, I've got special plans for when we capture her."
    scene ch1ep4_868
    with dissolve
    mal "I'll take my time with her, make her scream in ways you never could. And you'll have a front-row seat to the whole show."
    play sound woodhit
    scene ch1ep4_869
    with hpunch
    mc "No...! Moon...! I won't let you touch her!"
    scene ch1ep4_870
    with dissolve
    mal "Ah, there's that spirit! That fire, that anger! I was wondering if I'd see any left in you."
    mal "But it's pointless, [mc]. You can't save her, much less yourself."
    mal "All you can do is sit there and watch as I break her, piece by piece."
    mc "I'll kill you... I swear, I'll rip you apart with my bare hands..."
    scene ch1ep4_871
    with dissolve
    mal "Big words from a man who can't even stand. But by all means, keep struggling. It makes victory that much sweeter."
    mal "And when she's finally broken, she'll know just how much of a failure you were."
    mal "How you couldn't protect her, couldn't save her from what awaits her."
    mc "..."
    scene ch1ep4_872
    with dissolve
    mal "She's a virgin, isn't she? I could tell from a glance."
    mal "*laughs* Oh ho ho... I'm going to enjoy my time with her!"
    mal "And you... will watch every single second of me exploring her depths!"
    stop music fadeout 4
    play sound chair2
    scene ch1ep4_873
    with dissolve
    pause
    play music2 'audio/AwakenYourPower.mp3'
    scene ch1ep4_874
    with dissolve
    mc "Hey..."
    mal "Hm? Wanna say your last words, eh? Okay, I'm listening."
    mc "For someone who's supposed to be interrogating me... you talk too much..."
    mc "You... and everyone in this goddamned organization... are all idiots..."
    play sound woosh5
    scene ch1ep4_875
    with dissolve
    mc "You forgot one thing... my legs aren't tied."
    scene ch1ep4_876
    with dissolve
    mal "Huh?"
    play sound kick_heavy
    scene ch1ep4_877
    with hpunch
    pause 0.3
    play sound2 bodyfall
    scene ch1ep4_878
    with Dissolve(0.1)
    pause
    scene black
    with dissolve
    pause 1.0
    play sound woodcrash
    scene ch1ep4_879
    with hpunch
    pause 0.3
    play sound2 bodyfall2
    scene ch1ep4_880
    with hpunch
    pause
    scene ch1ep4_881
    with dissolve
    mal "W-what are you?!"
    mc "What am I? Sounds like something I could answer..."
    scene ch1ep4_882
    with dissolve
    mal "W-wait! Hold on! Let's talk about this!"
    mc "Talk? You want to talk now, you piece of shit...?"
    mal "P-please! I was just following orders! None of it was personal!"
    scene ch1ep4_883
    with dissolve
    mc "Not personal? You threatened to assault my wife, now you're pleading for your life...?"
    mc "We were sailing smoothly back there, but you know, I don't take any threats to my girls so kindly..."
    mal "I-I'm sorry! I won't touch her, I swear! Just let me go!"
    mc "Let you go...? After everything you've done...? After all the pain you've given me...?"
    mal "I'll do anything! I'll tell you where Bonheur is! I'll help you save her!"
    mc "Save her? No, you don't get to save anyone else after this..."
    scene ch1ep4_884
    with dissolve
    mal "No, wait! Please! I'm begging you!"
    mc "Beg all you want... It won't change a thing..."
    mal "No... no, please... don't..."
    scene ch1ep4_885
    with dissolve
    pause
    play sound swordimpact
    scene ch1ep4_886
    mc "I've been through hell and back for the truth..."
    mc "Seeking answers, wanting to know why the world is so filled with pain and injustice..."
    mc "But instead, I've endured more agony than I thought possible..."
    mc "I've questioned whether it was worth it... whether all this suffering was the price of my curiosity..."
    scene ch1ep4_887
    with dissolve
    mc "But I've come to realize... I'm not the only casualty of this world's cruelty..."
    mal "W-what are you talking about...?"
    mc "You're... about to become one of those casualties..."
    mc "That... is the price {b}you{/b} will have to pay..."
    mc "I told you, didn't I? I'll rip you apart with my..."
    mc "Bare..."
    play sound running loop
    scene ch1ep4_888
    mal "SOMEONE SAVE MEEEEEE!!!"
    mc "{b}Hands{/b}."
    stop sound
    play sound2 headsplat
    scene ch1ep4_889
    with hpunch
    pause
    play sound3 bodyfall
    scene ch1ep4_890
    with dissolve
    mc "..."
    mal "I... enough... plea-{w=0.5}{nw}"
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    mal "I-{w=0.5}{nw}"
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    mal "Plea-{w=0.5}{nw}"
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_891
    with hpunch
    pause 0.5
    play sound kick_heavy
    scene ch1ep4_892
    with hpunch
    pause 0.8
    stop music2 fadeout 3
    scene ch1ep4_893
    with dissolve
    mc "*huff*... *huff*... *huff*..."
    scene ch1ep4_894
    with Dissolve(0.1)
    m "[mc]!"
    scene ch1ep4_895
    with dissolve
    pause 0.5
    play sound chime_bell
    play music 'audio/DesertLife.mp3'
    scene ch1ep4_896
    with flash
    pause 0.5
    scene ch1ep4_897
    with flash
    pause 0.5
    scene ch1ep4_898
    with flash
    pause 0.5
    scene ch1ep4_899
    with flash
    pause 0.5
    scene ch1ep4_900
    with flash
    m "What... did I just..."
    scene ch1ep4_901
    with dissolve
    pause 0.5
    play sound bodyfall2
    scene ch1ep4_902
    with hpunch
    m "[mc]?"
    scene black
    with dissolve
    m "[mc]!"

    scene black
    with dissolve
    with fade

    play sound windgrass loop
    scene ch1ep4_903
    with dissolve
    m "Hnngkk! I... I need... to get you to the hospital... quick! Just... hang in there!"
    mc "..."
    scene ch1ep4_904
    with dissolve
    m "[mc]! Stay with me, okay? Don't you dare leave me now!"
    mc "..."
    scene ch1ep4_905
    with dissolve
    m "I know it hurts, I know you're tired, but you have to stay alive!"
    m "Remember what we talked about at the dinner table? I'm going to accept it!"
    scene ch1ep4_906
    with dissolve
    m "We're going to get properly married...! Start a family...! Grow old together...!"
    m "I-I'll even cook your meals! I'll burn a few at first, but I'll keep trying until I get it right...!"
    mc "..."
    scene ch1ep4_907
    with dissolve
    m "And we'll return to the beach...!"
    m "I know I dressed a bit conservatively last time, so I'll wear whatever you like!"
    mc "..."
    m "No? Then... I'll go naked! If it's for you, I wouldn't mind!"
    mc "..."
    scene ch1ep4_908
    with dissolve
    m "[mc]...?"
    scene ch1ep4_909
    with dissolve
    pause
    scene ch1ep4_910
    with Dissolve(0.1)
    m "!!!"
    play sound2 cloth
    scene ch1ep4_911
    with Dissolve(0.2)
    m "[mc]!"
    scene ch1ep4_912
    with dissolve
    m "Hnn! Hnng! Hnnh!"
    scene ch1ep4_913
    with dissolve
    pause
    scene ch1ep4_912
    with dissolve
    m "Hnn! Hnng! Hnnh! Hnnh!"
    scene ch1ep4_913
    with dissolve
    pause
    scene ch1ep4_912
    with dissolve
    m "Hnn! Hnng! Hnnh! Hnnh! Hnnh!"
    scene ch1ep4_913
    with dissolve
    pause
    scene ch1ep4_914
    with dissolve
    m "Hnn! Hnng! Hnnh! Come on, Commander! Come on!"
    mc "..."
    scene ch1ep4_915
    with dissolve
    m "*sobs*"
    scene ch1ep4_916
    with Dissolve(0.2)
    m "No... I'm not letting you go this time! Not again!"
    play sound2 cap_off
    scene ch1ep4_917
    with Dissolve(0.2)
    m "I took one of these back in the war. It may hurt, so if you can somehow hear me, please brace yourself!"
    play sound2 punch
    scene ch1ep4_918
    pause 0.8
    play sound3 gasp_male
    scene ch1ep4_919
    mc "*GASPS*"
    m "Commander!"
    mc "..."
    $ renpy.music.set_volume(0.3, 1.0)
    play sound2 heartbeat_fast loop fadein 2
    scene ch1ep4_920
    with dissolve
    pause
    stop sound2 fadeout 2
    $ renpy.music.set_volume(1.0, 1.0)
    scene ch1ep4_921
    with dissolve
    pause
    play sound3 jesscarroar
    scene ch1ep4_922
    with dissolve
    pause
    scene ch1ep4_923
    with Dissolve(0.2)
    a "Spread out and search the entire place! Find Bonheur and his son!"
    a "I want all the dead bodies cleared! Leave no evidence of tonight's events!"
    gru "YES, MADAM!"
    scene ch1ep4_924
    with dissolve
    a "{i}What on earth happened here...?"
    a "{i}She did this... all by herself?!"
    scene ch1ep4_925
    with dissolve
    pause 0.8
    play sound2 cloth2
    scene ch1ep4_926
    with hpunch
    pause
    scene ch1ep4_927
    with dissolve
    a "..."
    scene ch1ep4_928
    with dissolve
    pause
    scene ch1ep4_929
    with dissolve
    a "... Thank you. You can rest now. I'll take care of the rest."
    scene ch1ep4_930
    with dissolve
    a "Someone assist me with getting these two to the hospital, NOW!"
    call hide_days from _call_hide_days_24
    with dissolve
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    show screen day_wednesday with dissolve
    play music 'audio/SleepingGiant.mp3'
    scene ch1ep4_931
    with dissolve
    mar "I apologize, but she didn't mention anything about her destination."
    a "*sighs* Where the hell did she go...?"
    scene ch1ep4_932
    with dissolve
    a "It's okay. I should be fine here. You can go home now."
    mar "Understood. Is there anything else you'd like me to do?"
    a "... Actually, I'll put you in charge of what's left of the group for the time being. Make sure everyone has food and receives equal treatment."
    mar "I shall do as instructed. I'll be off now."
    play sound closedoor2
    scene ch1ep4_933
    with dissolve
    a "..."
    scene ch1ep4_934
    with dissolve
    a "... I was told she reformed the mafia as a charity. I had no idea things were that... dire."
    scene ch1ep4_935
    with dissolve
    j "Yes, your mother had good intentions. She had no desire for power."
    j "She saw potential in such a corrupt group and aimed to transform it into a force for good. To give back to those who served her."
    j "She made progress, but with the mafia's influence halved, her dream became unattainable."
    scene ch1ep4_936
    with dissolve
    a "Why didn't you guys help her then? You and your crew are more than capable of taking on her problems."
    scene ch1ep4_937
    with dissolve
    j "I once harbored a vendetta against the group."
    j "And now, working under the government's oversight, a mafia... remains a mafia."
    j "No matter how you dress it up, it is still a shady organization that operates beyond the government's gaze."
    scene ch1ep4_938
    with dissolve
    a "Then why are you helping us, given your stance?"
    j "Let's just say... it serves a mutual interest."
    j "We get to address unfinished business, and you gain more chances to secure the peace you wanted."
    scene ch1ep4_939
    with dissolve
    j "Besides, I couldn't simply disregard [mc] or Georgia's last wishes."
    j "Aside from my crew, you're the only people I have left... I've lost too many already..."
    j "That being said, I can only offer limited personal support. I can't officially work on your behalf."
    j "But with Bonheur now under our thumb, the remainder of the mafia should naturally realign with you."
    j "Like what Hera told you, what you choose to do with that power is entirely up to you."
    scene ch1ep4_940
    with dissolve
    a "..."
    scene ch1ep4_941
    with dissolve
    a "I understand, but..."
    a "That decision will not come from me, but from him, now that he's tied to my blood."
    j "That's right."
    a "I know it was his and Emma's idea. I believe it's the right course of action..."
    a "I thought it would only be a game of cat and mouse; I never expected things to become this heavy... but he did..."
    a "Now that this all happened, I realize he anticipated things all along."
    scene ch1ep2_4
    with flash
    mc "If my intuition is right, I'm sure what we did at Hera's safe house alerted whoever is pulling the strings behind her back."
    mc "If so, they'll move sooner than we think. We must be prepared if that happens."
    scene ch1ep2_5
    with dissolve
    mc "I still don't know what they want or their true goal, but I won't let that affect our lives."
    mc "We have people with the right skillsets to do this. I need you to trust me and let me be your brains."
    scene ch1ep4_941
    with flash
    a "... I thought you said we were all in this together, [mc]..."
    scene ch1ep4_942
    with dissolve
    k "After watching Jovian's documentary, I had a feeling he might pull something like this..."
    k "I knew that silence was saying more than his words could..."
    k "What he did wasn't all for naught, but it was a suicide mission..."
    j "Well... we can call it braveness, stubbornness, or even foolishness, but can we really blame him for his desires?"
    j "Thanks to him, those simple dreams you had are now within reach."
    k "They may be simple dreams... but at what cost? I nearly lost him too..."
    j "Everything comes with a price, Klara. That's part of what we've learned."
    k "I know... I've been with the Dietrich Clan long enough to understand that..."
    a "..."
    scene ch1ep4_943
    with dissolve
    a "How's he doing?"
    j "*sighs* Not to throw everything at you, but there's both good and bad news."
    a "Just tell us."
    scene ch1ep4_944
    with dissolve
    j "The good news is he's starting to recover, especially impressive considering it's only been a day since he was injured."
    k "Is that because of..."
    j "Yes, the serum. It's the same with Fang, Lance, and Claire. They always heal a bit faster than normal people."
    a "And the bad news?"
    j "His wounds and burns will heal, but the damage is irreversible. And I'm not just talking about external injuries."
    j "Some of his internal organs have suffered significant damage due to his sudden... awakening."
    j "Thanks to Bonheur's intel, we now understand how the serum is activated."
    j "The Incubation stage involves applying mild, consistent pain to the body, gradually activating the serum."
    j "But... we were a bit too late. [mc] really is an anomaly among serum users."
    scene ch1ep4_945
    with dissolve
    k "How... How is this all possible? The serum, its wonders, risks... How can such a thing even exist?"
    j "I used to ask the same question."
    j "With today's technology, it {i}could{/i} be possible to create something like it, especially since a certain gaming company is now making neural implants for their upcoming game."
    j "But the serum predates our current tech by decades, when technology was far less advanced."
    j "Yet, we've seen it work. We know it exists."
    j "Going back to [mc]'s case... He's healing, but all we can do is wait, and hope for the best."
    scene ch1ep4_946
    with dissolve
    a "..."
    scene ch1ep4_947
    with dissolve
    a "How about Moon?"
    j "Ah, you shouldn't worry about her. She's built to last."
    j "She may be tired, but she'll be fine."
    scene ch1ep4_948
    with dissolve
    j "There's something I need to ask of all of you, though."
    k "What's that?"
    j "Now that we know who they are, let's allow them to keep their pasts to themselves, if possible."
    j "I don't know how they will process that fact, so let's not preempt their reactions."
    j "Whether they come to terms with it or not, it's a sensitive matter that only they can truly understand."
    j "Just remember, despite what we've learned, [mc] remains [mc], and Moon is still Moon."
    k "That's true... I'll make sure the others know."
    j "Thank you."
    stop music fadeout 2
    
    scene black
    with dissolve
    with fade

    play music 'audio/ShineLikeUs.mp3'
    play sound closedoor2
    scene ch1ep4_949
    with dissolve
    a "I'm back. Sorry, I had to send them off."
    scene ch1ep4_950
    with dissolve
    a "I can't believe you did that, [mc]. What were you thinking, going in there by yourself?"
    a "*sigh* Honestly, what am I going to do with you? I can't even get mad."
    a "You know this ring would be meaningless without you, right?"
    a "I have so much to tell you, [mc]. So you'd better wake up soon."
    scene ch1ep4_951
    with dissolve
    a "The others are hesitating to visit because they can't bear to see you like this, especially Sky. But I'll try to persuade them again."
    a "... No, I'll make sure everyone comes to see you."
    scene ch1ep4_952
    with dissolve
    a "But forget about that for now. Hasn't your hair... gotten a bit longer?"
    a "That's odd..."
    a "Not that it makes you any less handsome, anyway."
    call hide_days from _call_hide_days_25
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_thursday with dissolve
    play music 'audio/Carefree.mp3'
    play sound closedoor2
    scene ch1ep4_953
    with hpunch
    shu "EEEEY! WAZZUP!"
    shu "The name's Shu, but you can call me the highlight of your day!"
    shu "I'm the guy who walks into a room and boom, it lights up—no spotlight needed, though I surely deserve one!"
    play sound woosh
    scene ch1ep4_954
    shu "When it comes to making an entrance, consider me a pro!"
    shu "Style, charisma, and a dash of modesty, all wrapped up in one irresistible package!"
    shu "If you don't know me, WHY?"
    play sound woosh
    scene ch1ep4_955
    shu "..."
    scene ch1ep4_956
    with dissolve
    shu "Oh... you're still dead, huh?"
    scene ch1ep4_957
    with dissolve
    shu "Anyway, got you some clothes I think you'll like."
    shu "Heard you're a badass now, so I picked out something edgy for when you're up and about."
    shu "... I've prepared a lot for you, so try not to keep me waiting for too long."
    scene ch1ep4_958
    with dissolve
    shu "Catch you later, dude..."
    play sound woosh
    scene ch1ep4_959
    shu "*wheeze* Actually, scratch that! I still have a few hours here, so you're stuck with me and my magnificence!!"
    shu "That's right! Yours truly will be by your side, using my eloquent words to nurse you back to health!"
    shu "Well, until they kick me out... but anyway, where were we?"
    call hide_days from _call_hide_days_26
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_friday with dissolve
    stop music fadeout 3 
    play music2 'audio/ShineLikeUs.mp3' fadein 3
    play sound closedoor2
    scene ch1ep4_960
    with dissolve
    pause
    if gwenroute:
        play sound cloth
        scene ch1ep4_961
        with dissolve
        pause
    scene ch1ep4_962
    with dissolve
    g "Hey, I know you're worried about us. Rest easy; we're all fine."
    g "But [mc]..."
    g "You never forced us to be with you; it was our choice. Our lives were never your cross to bear."
    g "Still, thank you for trying to protect us."
    g "It's over now-you did it."
    g "So please, don't ever do anything like that again, okay?"
    scene ch1ep4_963
    with dissolve
    g "Emma's done with the Winters' case, so she'll be able to visit you tomorrow."
    g "And Aine's a little busy, so it's my turn to watch over you for the entire day."
    scene ch1ep4_964
    with dissolve
    g "*laughs* No alcohol nor tobacco breaks, I promise."
    call hide_days from _call_hide_days_27
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_saturday with dissolve
    play sound closedoor2
    scene ch1ep4_965
    with dissolve
    pause
    scene ch1ep4_966
    with dissolve
    e "Sorry it took me a while to get here. I was taking care of the Winters."
    e "But that's exactly what you would've told me to do, right?"
    e "\"Prioritize what matters, Emma.\". That's always been your way, putting everyone else before yourself."
    scene ch1ep4_967
    with dissolve
    e "Thank you, [mc]..."
    e "Thank you for every sacrifice, especially for all the times you've been there for me."
    e "You never needed to prove yourself as a hero, [mc]. In my eyes, you've always been one."
    scene ch1ep4_968
    with dissolve
    e "Without you, I can't even imagine where I'd be right now."
    e "Yes, our journey to get to where we are today has been filled with tears, with both of us giving up so much."
    e "But don't forget that I'm by your side just as much as you've been by mine."
    e "I'll be waiting for you, [mc]."
    call hide_days from _call_hide_days_28
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_sunday with dissolve
    play sound closedoor2
    scene ch1ep4_969
    with dissolve
    s "..."
    k "Sky, honey, come on now, you can do it."
    scene ch1ep4_970
    with dissolve
    s "But... he looks so..."
    k "Sky, he's not gone. He's fighting, stronger than ever."
    scene ch1ep4_971
    with dissolve
    s "..."
    scene ch1ep4_972
    with Dissolve(0.2)
    s "*hics*"
    s "I'm sorry, I just... can't look at him like this."
    s "We lost Dad, now [mc]'s like this..."
    s "I'm scared, Mom... What if he doesn't wake up?"
    k "Don't say that, Sky. He'll wake up, he has to."
    k "But right now, we've got to hold onto hope."
    call hide_days from _call_hide_days_29
    with dissolve
    
    scene black
    with dissolve
    with fade

    show screen day_monday with dissolve
    scene ch1ep4_973
    with dissolve
    n "[mc], I legged it over as soon as I heard about what happened."
    n "I still can't wrap my head around why you did that, but bloody hell, I admire your guts."
    n "Once you've set your sights on somethin', no one's changin' yer mind, huh? That, we both have in common."
    scene ch1ep4_974
    with dissolve
    mc "..."
    n "... Honestly, I'm a bit lost for words here. It's rough seein' ya like this, but I'm stoked you're still with us."
    n "But I'll tell ya what... hearing the news nearly knocked the wind outta me."
    n "We might not have hung out much, but it turns out we're tighter than I thought we'd get."
    scene ch1ep4_975
    with dissolve
    n "I mean, what are the odds that I'd get close with you?"
    if naomiroute:
        n "... And what's the chance of that same bloke makin' me reckon I might be worthy of loving again?"
    n "What I'm tryin' t'say is... when you pull through, I'll have a cold one waiting for ya."
    n "'Cause if there's one thing I'm sure of, it's that you'll get past this. That's just who you are."
    n "Just don't leave us waitin' for too long, alright?"
    call hide_days from _call_hide_days_30
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_tuesday with dissolve
    play sound closedoor2
    scene ch1ep4_976
    with dissolve
    f "Well, well, well... Look who's trying to be a hero."
    play sound cloth
    scene ch1ep4_977
    with dissolve
    f "But seriously, [mc], that was one heck of a stunt you pulled."
    f "I didn't know what to do when Francis grabbed you that night. All I knew was I needed to get help and fast."
    f "You had me scared shit out of my mind, do you know that?"
    scene ch1ep4_978
    with dissolve
    f "But... I'm relieved you're okay now."
    f "You better get well soon. It's not fun working alone, you know...? I need my partner in crime back."
    scene ch1ep4_979
    with dissolve
    f "Oh, and guess what? I finally got Moon to come visit."
    f "Yeah, she's fine, but she's been a bit hesitant to see you. Can't figure out why, though..."
    scene ch1ep4_980
    with dissolve
    f "Seeing her tears filled with blood like that, man, I was speechless. I've never seen anything like it."
    call hide_days from _call_hide_days_31
    with dissolve
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade
    
    show screen day_wednesday with dissolve
    play music 'audio/LinesIdCross.mp3'
    play sound closedoor2
    scene ch1ep4_981
    with Dissolve(1.0)
    pause
    play sound cloth
    scene ch1ep4_982
    with Dissolve(1.0)
    pause
    scene ch1ep4_983
    with dissolve
    m "That night I saw you, something strange happened. Memories began flashing in my head, and suddenly, I remembered everything."
    m "Lady Sora's memories and emotions merged with mine, making it feel like I had lived her life, not just inherited her memories."
    m "I experienced her heartache over losing Emperor Kaito firsthand. It makes me wonder... have you seen Kaito's memories too?"
    scene ch1ep4_984
    with dissolve
    m "It's strange, isn't it? It feels like history repeats itself, as if caught in a loop."
    m "But it also feels like Sora and Kaito are trying to bring us back together, to break that cycle and change our destiny."
    mc "..."
    scene ch1ep4_985
    with dissolve
    m "[mc], it's been nearly two weeks since I've been living without you."
    m "Lying there, unconscious, I know you can't respond, but I have to tell you... I have to let out these feelings that aren't only Lady Sora's, but mine as well."
    m "In these memories, I feel Sora's love for Kaito. It's so deep that it transcends time itself."
    scene ch1ep4_986
    with dissolve
    m "And standing by your side, I understand that love because I feel it too."
    m "It's not only because of the memories or the feelings passed down to me: it's because of who you are, and the time we've spent together."
    scene ch1ep4_987
    with Dissolve(1.0)
    m "[mc], I love you..." with Dissolve(1.0)
    m "Even though you're not aware of it right now, I need you to know that my feelings are real, a blend of the past and present, something uniquely ours."
    m "I can't see what the future holds, nor can I dictate the course of history."
    m "But one thing I'm certain of is my feelings for you. They're as strong as Sora's for Kaito, yet they're my own."
    m "I promise, when you wake up, I'll be here to tell you all of this myself, to make our memories, and maybe, in our way, to continue their story."
    scene ch1ep4_988
    with dissolve
    m "So please, [mc], find your way back to me. That's all I'm asking. I'll be waiting, no matter how long it takes."
    scene ch1ep4_989
    with Dissolve(0.2)
    m "Because without you... I..."
    m "*sobs* I... I can't do it..."
    play sound clench
    scene ch1ep4_990
    with Dissolve(0.2)
    pause
    scene ch1ep4_991
    with dissolve
    if moonroute:
        mc "... I told you not to cry, didn't I?"
    else:
        mc "... Hey..."
    scene ch1ep4_992
    with Dissolve(0.2)
    m "*hics*"
    scene ch1ep4_993
    with dissolve
    mc "Mmh...!"
    mc "Experiencing it myself, I know how much it hurts... So, no more tears, okay?"
    m "Okay..."
    scene ch1ep4_994
    with dissolve
    m "Wait, did you... did you hear everything I said?"
    mc "Yeah... everything, from the second you walked in... I was waiting for you, Moon..."
    scene ch1ep4_995
    with dissolve
    m "!!!!"
    mc "*chuckles* There you go again, freezing up... It really does make things a bit awkward, you know...?"
    mc "Seriously, you've changed a little since we discovered what we are to each other..."
    scene ch1ep4_996
    with dissolve
    mc "But it's not just you... I heard everyone's messages..."
    mc "I was conscious, but couldn't move or even open my eyes..."
    mc "Felt like I was floating in darkness... It was a weird experience..."
    play sound cloth
    scene ch1ep4_997
    with dissolve
    mc "I... I need to thank everyone for looking out for me..."
    m "That time will come. For now, you should rest."
    scene ch1ep4_998
    with dissolve
    mc "I've been asleep for more than a week already..."
    m "It doesn't matter, [mc]. Our bodies still function like those of normal people."
    m "Not only that, but you also unconventionally activated your serum, using up almost everything you've got."
    m "Trust me, as long as you can't move properly, you should stay lying down."
    play sound chair
    scene ch1ep4_999
    with dissolve
    mc "Now that I think about it... So that's how it gets activated..."
    m "Now that we have you as proof, I'm sure of it."
    mc "Everything felt... normal. Nothing changed, yet I knew I could do things I couldn't do before..."
    scene ch1ep4_1000
    with dissolve
    m "That's how it is for all of us. But once it's activated, something does change within us, [mc]. I hope you're prepared for that."
    mc "Just like how I felt nothing after killing that guy..."
    m "Yes..."
    mc "For some reason, I don't feel any remorse."
    scene ch1ep4_1001
    with dissolve
    m "Welcome to my world, Commander. A cruel place where everything fades into insignificance, except for what we truly hold dear."
    mc "*sighs* That's... a cool way to baptize me, alright..."
    scene ch1ep4_1002
    with dissolve
    m "Just remember, we aren't immortal. We age and will eventually die. Don't let your abilities get to your head, and you'll be fine."
    mc "Yeah, I understand... I'll take Lance's and Jess' warning seriously."
    mc "But... just like that... it's all over..."
    m "You almost died, [mc]. It wasn't a \"just like that\" situation."
    mc "Well... you're right... I know it was reckless of me, so I owe everyone an apology..."
    m "I'm going to call Jess and inform everyone about you."
    if moonroute:
        scene ch1ep4_1003
        with dissolve
        mc "Hey... we'll talk later, okay?"
        scene ch1ep4_1004
        with dissolve
        m "Mhm, I expect us to."
    else:
        scene ch1ep4_1003
        with dissolve
        mc "Moon?"
        m "Yes, Commander?"
        mc "Thank you."
        scene ch1ep4_1004
        with dissolve
        m "It's my duty."
    stop music fadeout 2
    call hide_days from _call_hide_days_32
    with dissolve

    scene black
    with dissolve
    with fadeq

    "A week later..."

    scene black
    with dissolve
    with fadeq

    show screen day_friday with dissolve
    play music 'audio/Inspiration.mp3'
    scene ch1ep4_1005
    with dissolve
    pause
    play sound closedoor2
    scene ch1ep4_1006
    with dissolve
    shu "Dude, you ready? Our new home sweet home is waiting!"
    mc "New? What happened while I was out?"
    scene ch1ep4_1007
    with dissolve
    k "It might not be necessary anymore, but for extra security and peace of mind, Jess offered us their old place."
    k "I've been there before. It's actually in a nice neighborhood. In fact, some of them are still living there."
    mc "Oh, really?"
    scene ch1ep4_1008
    with dissolve
    a "And by a wild coincidence, one of your old friends lives there too."
    mc "An old friend, huh? Other than Shu, I did have quite a few friends in college. I wonder who it could be."
    scene ch1ep4_1009
    with dissolve
    shu "Someone you know pretty well, dude."
    mc "... Please don't tell me it's Bite Size."
    shu "Yep!"
    mc "Ah, shit... here we go again..."
    mc "It's been a long time. Did you two get along?"
    shu "Nah, I'm good. It was actually nice to see her again."
    shu "So come on! I'll drive us there!"

    scene black
    with dissolve
    with fade

    play sound2 cityalley loop
    play sound cardoorclose
    scene ch1ep4_1010
    with dissolve
    mc "Isn't this..."
    scene ch1ep4_1011
    with dissolve
    mc "... Almost exactly like our old neighborhood?"
    shu "Exactly!"
    mc "So are we just going to leave our old place behind?"
    mc "We have so many memories in that house. This feels so sudden."
    scene ch1ep4_1012
    with dissolve
    k "With Naomi's help, everything has been moved here. But that doesn't mean we can't visit our old home, sweetheart."
    k "It will always hold a special place in our hearts."
    play sound closedoor
    scene ch1ep4_1013
    with dissolve
    pause
    play sound cloth2
    scene ch1ep4_1014
    with hpunch
    s "*crying* [mc]!"
    scene ch1ep4_1015
    with dissolve
    mc "Sky..."
    mc "There, there. I'm here now."
    s "You had us all worried!"
    scene ch1ep4_1016
    with dissolve
    mc "I know, that's why I owe everyone an apology."
    scene ch1ep4_1017
    with dissolve
    g "Yes, it was risky, and we could've lost you, but you did what you thought was best with what you had, [mc]."
    g "You had my full trust. You don't owe me an apology at all."
    e "I agree with Gwen. I'm just glad to have you back. That's all that matters."
    mc "Thanks, guys."
    if (moonroute and moonpoint == 6):
        scene ch1ep4_1018
        with dissolve
        a "Though, if there's someone who truly deserves an apology, it's her."
        a "Even if it was her duty, she was the one who risked her life to get you out of there, not us."
        scene ch1ep4_1019
        with Dissolve(0.2)
        f "*whispers* So... did you confess?"
        play sound woosh
        scene ch1ep4_1020
        m "!!!"
        scene ch1ep4_1021
        with Dissolve(0.2)
        a "Frey, what did I tell you?"
        f "Ugh, bummer..."
        scene ch1ep4_1022
        with dissolve
        mc "Give us some time. I know we have a lot to sort out in the aftermath, but right now, she's my priority."
        scene ch1ep4_1023
        with dissolve
        g "..."
        stop music fadeout 2
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fade

        label kaitosorareunion:
        if _in_replay:
            $ name = persistent.gallery_name
        play sound ceilingfan_low loop
        scene ch1ep4_1072
        with dissolve
        pause
        scene ch1ep4_1073
        with dissolve
        pause
        scene ch1ep4_1074
        with dissolve
        yt "This feels a little awkward given it's not my first rodeo in these situations."
        yt "The atmosphere is quite different here than at the hospital, despite me being barely conscious pretty much the whole time there..."
        scene ch1ep4_1075
        with Dissolve(0.2)
        m "... Comm-{w=0.5}{nw}"
        scene ch1ep4_1076
        "Moon catches herself almost immediately, softly clearing her throat."
        scene ch1ep4_1077
        with dissolve
        m "Umm, [mc]...?"
        "You crane your neck, looking down towards Moon with a smile."
        m "Umm, I'm feeling a little... hot..."
        "You notice Moon more flushed than usual and turn to face her."
        yt "Wow... she's usually more composed with herself than this."
        yt "Even when I picked her up at school, she didn't show a hint of bashfulness."
        yt "But now, it feels like she's afraid of saying or doing a single thing wrong."
        yt "... Is it because we're in my room... on my bed... alone... and coming to terms with how we truly feel about each other?"
        "Trying to ease her tension, you crack a joke."
        scene ch1ep4_1078
        with dissolve
        mc "You didn't catch anything while we were at the hospital, did you?"
        m "No, being that we're numbers infused with the serum... we have disease resistance and tolerance."
        m "If we can't reduce pathogens in our system, we can at least keep them in place until they die out naturally... leaving us unaffected."
        yt "Noted... though, I should have realized that given it cured my disease back then."
        yt "In any case, it seems like that didn't lighten the mood much. Maybe I can switch tactics."
        play sound2 cloth
        scene ch1ep4_1079
        with dissolve
        "You place your hands on her shoulders, feeling her immediately stiffen at your touch."
        mc "Well, be that as it may... let's check to make sure. Lean forward a bit."
        scene ch1ep4_1080
        with dissolve
        "Moon's cheeks grow a deeper crimson as she leans into you, closing her eyes."
        "Ever so slightly, she pushes out her lips."
        yt "So adorable-wait, does she want me to kiss her?"
        yt "... Let's tease her a little more first..."
        mc "Let's check your temperature using the method people use with their loved ones."
        mc "Klara used to do this with Sky and me whenever we felt sick."
        play sound2 cloth
        scene ch1ep4_1081
        with dissolve
        "Moon's eyes snap open as she feels your forehead bump against hers, but she doesn't move."
        "Her heat radiates against your forehead, a pulsating warmth that builds with her every breath."
        "You're not sure if Moon's reaction is because of the intimate skin-to-skin contact or because you mentioned \"loved ones\"."
        scene ch1ep4_1082
        with dissolve
        m "S-so, d-do I have a fever...?"
        mc "I don't know actually. This is my first time doing this, and I'm not even sure what a fever feels like."
        m "Oh..."
        "Moon looks into your eyes, unsure what to do next."
        "The long, tense stare continues for some time, each of you wondering what the other's next move will be."
        "Since you're in no rush, you just focus on the sight before you."
        scene ch1ep4_1083
        with dissolve
        yt "God, she's so beautiful... I want to wrap her up and hold her for all eternity."
        yt "But for whatever reason, I just can't move beyond this, as if a force is preventing me from moving."
        yt "A feeling of want, need, desire... to remain like this, drinking in her beauty."
        yt "Is it Kaito? Are the feelings of the emperor moving within me?"
        stop sound fadeout 2
        play sound2 closedoor
        scene ch1ep4_1084
        with dissolve
        "Some rustling outside the window can be heard, bringing you both out of your reverie."
        play sound chair3
        play sound2 exhale_female
        scene ch1ep4_1085
        with Dissolve(1.0)
        pause
        play music 'audio/PerfectShadows.mp3'
        scene ch1ep4_1086
        with Dissolve(8.0)
        pause 2.0
        scene ch1ep4_1087
        with dissolve
        g "When I go, to reach out and to roam...{w=4.5}{nw}"
        scene ch1ep4_1088
        with dissolve
        g "There is no perception of a home...{w=5.0}{nw}"
        scene ch1ep4_1089
        with dissolve
        g "For when it's all been said and done, I know...{w=5.0}{nw}"
        $ renpy.music.set_volume(0.5, 1.0)
        scene ch1ep4_1090
        with dissolve
        mc "..."
        m "..."
        scene ch1ep4_1091
        with dissolve
        yt "*chuckles* Nice assist, Gwen."
        yt "Wait, did she do this on purpose knowing that we're...?"
        yt "Well, either way, it doesn't matter as I now feel like I can continue."
        scene ch1ep4_1092
        with dissolve
        m "Is that... Gwen? Her voice is beautiful..."
        menu:
            "There's nothing more beautiful...":
                scene ch1ep4_1093
                with dissolve
                mc "There's nothing more beautiful than the one right before me."
                scene ch1ep4_1094
                with dissolve
                "Moon covers her deepening blush; however, she can't hide her smile."
                yt "God, as cheesy as that line was, her reaction is just too cute. Worth it!"
                yt "I can't take this anymore. My heart feels as though it's about to burst for her!"
                m "You do have a way with words-"
                scene ch1ep4_1095
                with dissolve
                "Moon's words are cut off as you pull her shoulders towards you, drawing her face to yours, pressing your lips together."
            "I agree...":
                scene ch1ep4_1093
                with dissolve
                mc "Yeah, I agree."
                "Moon stares longingly at you with an anticipating look."
                yt "I can't take this anymore; my heart can't take much more of this!"
                scene ch1ep4_1095
                with dissolve
                "You pull Moon's shoulders towards you, drawing her face to yours, pressing your lips together."
        scene ch1ep4_1096
        with dissolve
        "You can feel the tension in Moon's shoulders disappear as if they're saying, \"Finally, he kissed me...\""
        scene ch1ep4_1097
        with dissolve
        "You pull away from her, revealing an amusing sight of her with pursed lips... like a fish out of water, seeking your lips to meet hers again."
        scene ch1ep4_1098
        with dissolve
        mc "Moon, ever since we found out about our connection, we've always begged the question of whether or not our feelings are our own or fabricated by some past life."
        mc "But after the time we've spent, after everything we've gone through together, at the school and what we shared at the hospital..."
        scene ch1ep4_1099
        with dissolve
        yt "She's remembering what we did together at the school. How cute..."
        scene ch1ep4_1100
        with dissolve
        mc "I realize that our connection isn't based on some mind-altering serum."
        mc "Instead, it's from the connection between our hearts."
        m "You mean the jolt... the ache in my chest?"
        mc "Yes, exactly... it's our feelings resonating with each other."
        mc "We already have something special, an unparalleled love we've fostered ourselves."
        mc "The connection we have from the serum has only elevated it due to the Emperor and Sora's passion for each other."
        scene ch1ep4_1101
        with dissolve
        m "You're right. The time we shared had me wondering if my hidden desires were being solely pushed by Sora's."
        m "But, looking back, I've always enjoyed our times together. I loved how you carried yourself from the first moment we met."
        m "And despite knowing full well I'd be guarding you, protecting you..."
        m "I, myself, felt safe by your side."
        "You chuckle softly at the idea of Moon also having developed feelings from the very beginning."
        scene ch1ep4_1102
        with dissolve
        m "A-are you laughing at me?"
        mc "Not at all. I find it amusing that I even felt some connection upon first seeing you... Your beauty blew me away."
        mc "And this happened well before I unlocked any memories or feelings of the Emperor."
        mc "And hearing you lay out your feelings to me at the hospital cemented mine that much more."
        mc "I can't, and I won't let you go. You'll never have to feel lost anymore."
        scene ch1ep4_1103
        with dissolve
        yt "I've reached her! She confessed her feelings at the hospital, and I confessed mine here; our feelings have connected and now have become a single entity."
        mc "I love you, Moon... with every fiber of my being!"
        mc "My love is immeasurable: the very universe can't contain it..."
        scene ch1ep4_1104
        with dissolve
        yt "Crap, my own emotions might have come on a little too strong..."
        yt "Oh, the hell with it."
        scene ch1ep4_1105
        with dissolve
        "You bring her back into a kiss, cradling the back of her head to pull her in further."
        yt "God, why did that sound like such a wedding vow?"
        scene ch1ep4_1106
        with dissolve
        "When you both pull away, you can see that her blushed expression still hasn't disappeared."
        "If anything, you're shocked her cheeks haven't caught fire with how hot and red they've been."
        m "Y-you know, that sounded almost like wedding vows."
        stop music fadeout 4
        scene ch1ep4_1107
        with dissolve
        "You're taken aback by how your thoughts are in sync even now."
        mc "You're amazing, you know that? We're such a perfect match for each other, it's unbelievable!"
        $ renpy.music.set_volume(1.0, 1.0)
        play music 'audio/DevilDisguised.mp3'
        play sound cloth
        scene ch1ep4_1108
        with Dissolve(2.0)
        "Once again, you lock lips with Moon as you both battle for control over each other's mouths."
        "As your lips wrestle with hers for control, your hands synchronize with hers in a dance to remove each other's clothes."
        "First your bottoms... then your tops..."
        play sound2 belt
        play sound cloth
        scene ch1ep4_1109
        with dissolve
        "Then your underwear... then hers..."
        "Until finally, you both have nothing to hide."
        scene ch1ep4_1110
        with dissolve
        m "I have found myself on many battlefields throughout my life... some more brutal than others..."
        m "As brutal as they were, they hardened me... made me stronger."
        m "However, this is a battlefield like no other... a new experience for me."
        scene ch1ep4_1111
        with dissolve
        "You reach out with your hand and caress Moon's cheek."
        mc "Moon, this isn't a battlefield... this is a sanctuary, one where we both share an equal footing."
        mc "Here, no one will hurt you, nor me... we are the masters of this domain."
        m "Then, I am in your care, my love."
        play sound chair
        scene ch1ep4_1112
        with Dissolve(2.0)
        "You see Moon lean back, flopping herself onto your bed, head resting on your pillow.  Her entirety is exposed before you."
        "Stupefied at her naked sight, you can barely move while staring passionately at her."
        yt "Undoubtedly one of the most beautiful displays of the human body I have ever witnessed lays before me."
        yt "How can I {i}not{/i} admire it in all its full glory?"
        scene ch1ep4_1113
        with dissolve
        m "Once again, a full moon shines before you... what do you plan to do, besides taking mental pictures?"
        mc "I plan to land on it, of course. Fully explore it, every inch of it, for the glory of [mc]-kind!"
        mc "As the moon rises, so shall I to meet her!"
        m "... Then what are you waiting for?"
        scene ch1ep4_1114
        with dissolve
        "You shift yourself, sliding Moon's legs off of your thighs."
        "Spreading her legs, you position yourself onto your knees to rest parallel with her center."
        "You start by touching the inside of Moon's shins, almost caressingly, as you move up her legs."
        "Moon breathes in deeply at your faint touch, holding it in as you continue your ascent."
        "As you move down her inner thighs and approach her crotch, you immediately pass over it and glide onto her stomach, fingers spread outward."
        m "Mmmhh..."
        "She finally exhales, but was that because she couldn't hold her breath anymore?"
        "Or was it because your bypassing move abated her anticipation of your approach to her nethers?"
        scene ch1ep4_1115
        with dissolve
        yt "It's incredible just how soft and smooth Moon is naturally... yet taut when I apply any pressure."
        yt "She has certainly honed her muscles to the extreme and through the most extraordinary of ways."
        yt "She's like the perfect union of a princess and a warrior."
        scene ch1ep4_1116
        with dissolve
        "You move your hands forward until your fingers wrap around the perky tits that lay atop Moon's chest."
        "Once again, you feel Moon inhale deeply as your fingers tighten their grip."
        scene ch1ep4_1117
        with dissolve
        "Massaging her breasts with both hands, you lean forward and place your face in between."
        m "Nhhh..."
        "You elicit a moan from Moon as you continue to play with her tits, kneading them against either side of your face."
        "You inhale through your nose, taking in Moon's perfect scent."
        "You exhale through your mouth, blowing warm air onto Moon's sternum."
        "As the air cools against her skin while you relentlessly palpate her chest, her nipples harden in response."
        m "Mghhh..."
        "All the while, you feel your arousal growing to meet hers."
        scene ch1ep4_1118
        with dissolve
        "From here, you slide your lips down, kissing along the centerline of her body while using your fingers to pinch and tug at her nipples."
        m "Hhhh!"
        "Upon reaching her navel, you give it a light tickle with the tip of your tongue."
        "You lift up slightly to puff a breath of cool air against her abdomen, continuing to overload her senses with different sensations."
        m "Oohhh..."
        yt "Heh, can you image how she'd feel if I had an ice cube right now...?"
        yt "Another time, maybe. For now, let's keep the momentum going."
        scene ch1ep4_1119
        with dissolve
        "Moving on from her midriff, you slide your fingers down her feminine form as you move your face lower."
        "Soon, you come face to face with her vulva."
        "You can feel the heat emanating from her in waves: a clear sign she can't wait any longer."
        show moon7
        with dissolve
        pause
        "Just like Moon, you can't wait either."
        "As if driven by instinct, your tongue finds her clitoris."
        "In one deft motion, it pushes the skin of her hood back, exposing the swollen bud underneath."
        "You encircle her clit with your tongue, flicking it back and forth with quick twitches of the muscle."
        m "Gyhh!"
        "Moon's reaction clearly indicates she wants you to keep going."
        "Moving quickly, you run the skin of your tongue along her inner labia, mixing your saliva with her vaginal secretions."
        "The taste is absolutely divine. Each lick sends waves of pleasure through both your bodies."
        yt "Wow... why is this so much better than when we were at the school...?"
        yt "Is it because we've grown stronger with our feelings, where even her taste has become elevated?"
        "You can't help but descend deeper into her, finding new places to brush your tongue against. Moon shudders with pleasure in response."
        m "Mmm.. AAH... there! Right there!!"
        yt "Is she close already? Did the teasing really have that much of an effect?"
        yt "I can't let her reach climax first... not when there's still so much to experience together."
        scene ch1ep4_1120
        with dissolve
        hide moon7
        "You stop abruptly and prop yourself up, placing your hands on the outside of her knees."
        m "Nhhh, why did you-"
        play sound chair
        scene ch1ep4_1121
        with hpunch
        "Not letting her get even a word in, you lift her knees, causing her to slide off your pillow."
        "This causes her butt to slide in between your thighs as you let go, her upper thighs resting on yours."
        "Of course, this also has the serendipitous effect of letting your cock loom above her wet and exposed pussy, begging to be fed."
        yt "Let's see if we can slow it down while still building up the pleasure."
        scene ch1ep4_1122
        "You slap your engorged cock down upon her mound with a wet thud."
        m "Mmmm... denying me, and now bullying me?"
        "You see her pout; as adorable as it is, you don't want her to think you're ignoring her feelings."
        mc "Never... but wouldn't it be better if we both felt the peak of pleasure together at the same time?"
        scene ch1ep4_1123
        with dissolve
        "Moon covers her mouth with both hands, hiding her slight shock."
        m "*whispers* Y-yes..."
        mc "Do you trust me?"
        m "*whispers* Yes...?"
        mc "You don't sound too sure."
        scene ch1ep4_1124
        with dissolve
        m "Yes! Yes, I do."
        "You smile as you look down at your cock, still resting on top of her pussy."
        scene ch1ep4_1125
        with dissolve
        "Grabbing your dick, you pull back as you place your mushroom stamp of approval right onto her folds."
        "You can feel the heat and wetness of her pussy as your glans presses against her. Still, you don't push into her yet."
        "You guide the tip of your dick over her clit, rubbing your tip against it."
        "You then slide your head down her labia until it reaches the base of her cunt."
        m "..."
        "Moon doesn't say anything, but her expression betrays her feelings." 
        yt "Oh yeah, she must feel the pressure now."
        scene ch1ep4_1126
        with dissolve
        "Repeating this process, you coat the head of your dick in your latent saliva and Moon's juices left over from your prior treatment of her pussy."
        "Moon is panting at this point, stuck between the realization of you pushing yourself inside or rubbing up against her clit."
        yt "I don't think she can wait much longer; teasing her more could cause her to orgasm at any moment."
        scene ch1ep4_1127
        with dissolve
        "You place your hands on either side of Moon's hips."
        yt "Let's surprise her to halt that growing release..."
        "Sliding the head of your dick back up Moon's pussy, instead of rubbing your head onto her labia, you push gently between her folds."
        play sound chair
        scene ch1ep4_1128
        with hpunch
        m "Hghh!"
        "Moon slams her hands down onto yours, startling you, as she gasps deeply for air."
        "The sudden reaction stops you from pushing any further, the head of your dick engulfed by her pussy."
        scene ch1ep4_1129
        with dissolve
        m "Wow... you tricked me..."
        "Moon bites her lower lip, feeling the pressure of the tip of your manhood inside her."
        mc "Just keeping you on your toes, love..."
        m "Mmm... I like the way that sounds."
        mc "As do I."
        mc "Alright, I'll start pushing it in further."
        scene ch1ep4_1130
        with dissolve
        "You take her hands and interlock her fingers with yours."
        m "I'm ready... take me."
        m "All of me."
        show moon8
        with dissolve
        pause
        "You start sliding your dick into her, only to be met with some resistance." 
        m "Fffff... so big."
        "Pausing, you slowly back out a little before sliding forward again."
        yt "I don't want to hurt her, so best not to just jam myself in."
        yt "As tough as she is, I don't think she would appreciate that painful sensation."
        "You slowly start edging in, only to pull back slightly before again sliding forward."
        "You can see Moon taking in short breaths: a good sign that she's not uncomfortable as you work your way in."
        m "Mmh..."
        yt "Good girl, Moon. We'll keep going like this until you're ready."
        "Gauging it's her first time, you commend her for taking it in stride while experiencing this new, temporarily uncomfortable feeling."
        show moon9
        with dissolve
        hide moon8
        "Finally, what little resistance you felt gives way... like the last defensive wall breaking down."
        "Moon also begins breathing with a sense of pleasure as your thrusts seek deeper refuge inside her."
        "You eventually find the base of your cock touching her pussy lips."
        m "OH yes... y-you're so deep, I can feel all of you inside me."
        "You slide out from deep inside her and thrust inwards, seating her once again at the base of your dick, but with greater force."
        mc "Tell me, Moon, tell me how it feels!"
        "Each thrust you push into her, you can feel her hands grip yours tighter before releasing every time you pull out."
        m "Amazing... I-I'm feeling... everything, so full..."
        yt "She can barely get any words in as I pump away at her. It's... empowering."
        mc "Your pussy walls... you feel beyond amazing too, Moon."
        scene ch1ep4_1131
        with dissolve
        hide moon9
        m "Em-Embrace me!"
        play sound chair
        show moon10
        with dissolve
        "Not wanting to disappoint her in your quest for skinship, you let yourself lean into her arms as they fold around you."
        "Resting your head on the side of hers, you begin nibbling on her skin ever so slightly."
        "Moon gasps as you introduce yet another sensation to her."
        "She begins tightening up in her nethers, a telltale sign her orgasm is imminent."
        m "*whispers* [mc], I-I'm close... so close."
        "Her whispers into your ear, and the tightening of her insides as she closes in on her orgasm causes your eruption to begin its journey."
        mc "Yes, I'm right there as well Moon-"
        m "CLOSE, I SAID!!! Don't stop!!!"
        "As loud as she was in your ear, it didn't matter... you continue to thrust in and out."
        "In! And out!"
        pause
        play sound chair
        scene ch1ep4_1132
        with hpunch
        hide moon10
        m "AaaaaaaaaaaaaaAGH!!!!"
        "You can feel the pressure of her womanhood clamp hard as she reaches the height of pleasure."
        "Her vaginal walls flex tightly around your cock as you thrust one final time, balls deep within her."
        scene ch1ep4_1133
        with hpunch
        mc "MmmmmmmmuuHHH!!!"
        "Your orgasm shoots forward, painting Moon's insides as if it were a blank canvas on its way to becoming a masterpiece."
        scene ch1ep4_1134
        with dissolve
        m "I-I can FEEL it! FEEL you deep inside me!!!"
        scene ch1ep4_1135
        with hpunch
        "You're not done yet. The pressure of Moon's insides hasn't yet abated... causing more ropes of your ejaculate to pump into her."
        "It was as if Moon's pussy was sucking you dry."
        "Finally finished, you lie on top of Moon. Both of you are left breathing heavily."
        scene ch1ep4_1136
        with dissolve
        "You gently push off the lovely Moon, still buried within her."
        "Lovingly, but still breathlessly, you look down at her and begin settling down."
        mc "S-so... how did that feel?"
        scene ch1ep4_1137
        with dissolve
        "With her hands over her heart, Moon's chest rises and falls as she regulates her breathing back to normal."
        scene ch1ep4_1138
        with dissolve
        "She opens her eyes and looks up at you, blushing profusely."
        m "I... I never would have thought it would feel this amazing."
        m "Is this... will it be like this every time?"
        mc "Well, I cannot say it'll be like this every time..."
        m "Oh... I see."
        mc "... As there could be times of even greater intensities."
        scene ch1ep4_1139
        with dissolve
        "Moon smiles excitedly up at you, looking more mischievous than normal."
        m "More intense, you say?"
        mc "Of course. If you want to, we can try again tomor-"
        play sound chair
        scene ch1ep4_1140
        with hpunch
        "In one quick movement, Moon uses her strong core to sit up, gripping your shoulders and pinning your arms to the side."
        "Her unexpected actions and the force of her motion causes you to fall backwards."
        "Moon pauses, inches from your face, still sporting her mischievous smile."
        scene ch1ep4_1141
        with dissolve
        m "Why put off till tomorrow when we can continue today?"
        m "As numbers, we're gifted with extraordinary stamina... so why neglect it?"
        m "It may have only been a week since you've awakened in the hospital..."
        m "And as much as I would like you to rest, I know by now that you've got more stamina to continue."
        m "Isn't that right, {i}My King{/i}?"
        "Her goading causes you to elicit your own wry smile."
        mc "I will always have the stamina I need to continue to show you how much I love you, {i}My Queen{/i}."
        scene ch1ep4_1142
        with dissolve
        "And that was all she needed to hear."
        "This time, Moon grabs the initiative and kisses you first."
        "You can hear her moan from her kiss, seemingly acknowledging her proclivities."
        scene ch1ep4_1143
        with dissolve
        pause
        scene ch1ep4_1144
        with dissolve
        "You watch as she moves down your body, placing her kisses along your centerline until coming face to face with your cock."
        "She stares contently at your still-hard member."
        scene ch1ep4_1145
        with dissolve
        m "Well, it seems you're always ready to go."
        mc "It's not hard when I'm in the presence of such beauty, with whom I'm also deeply in love."
        m "... Since when did you have such a way with words?"
        scene ch1ep4_1146
        with dissolve
        pause
        scene ch1ep4_1147
        with dissolve
        mc "I meant given the situation, not my cock... which IS obviously hard."
        m "... and there he is again."
        scene ch1ep4_1148
        with dissolve
        "Moon giggles before reaching out and grabbing your aforementioned hardness with her hand."
        m "Obviously, indeed, and I don't mind if I help myself with it."
        m "Just like you helped yourself with me."
        show moon11
        with dissolve
        "Moon sucks the tip of your dick into her mouth, slipping her pursed lips just over your glans."
        "Due to the sensitivity of your cock and the rapt blissful nature you were in, it takes everything you have to not just thrust your hips upward into Moon's mouth."
        "She further descends on your shaft as the wet heat from the inside of her mouth reduces the intensity, but just barely."
        "However, she only reaches halfway down your cock before lifting off of it, resting your tip just inside her mouth."
        "Snaking her tongue out under your cockhead, she starts to move it back and forth, massaging the underside of your glans."
        "You gasp sharply at her newfound ability."
        mc "M-Moon... where... where did you learn that?!"
        scene ch1ep4_1149
        with dissolve
        hide moon11
        "She pops the head of your dick out of her mouth, licking her lips."
        scene ch1ep4_1150
        with dissolve
        m "Ever since that time at school, I wanted to make sure my skills rivaled my Commander's the next time we found ourselves in a similar situation."
        m "So, of {i}course{/i}, I'm going to gather intel on how to formulate a well-thought-out strategy."
        show moon12
        with dissolve
        "Not wasting any time, she pops your cock back into her mouth and quickly sucks, causing her cheeks to collapse inward."
        "This causes you to throw your head back, lifting your chest up slightly due to the bed behind you."
        mc "Mmmmmmm, you were definitely... vigilant in your findings."
        "Moon continues to slide her mouth down your cock, massaging your balls and sucking extra hard every time she ascends back up your shaft."
        "The sensation soon begins to reach epic levels."
        mc "Mmmm, yes... I'm almost-"
        play sound chair
        scene ch1ep4_1151
        with hpunch
        hide moon12
        "Your eyes shoot open as the sensation of elation escapes you."
        "You catch Moon sliding off your cock and looking down at you, smirking."
        mc "W-what... why did you?"
        scene ch1ep4_1152
        with dissolve
        "Realization dawns on you, as she {i}did{/i} say that she was going to help you in the {b}same manner{/b} you did to her."
        "You look up at her sporting a wry smile once again."
        scene ch1ep4_1153
        with dissolve
        mc "A sneaky little revenge plan, I see."
        m "No. Revenge would be to leave you in this state."
        m "That's a situation I would never let happen."
        "Moon clambers on top of you. You feel the heat from her sex radiate into your lower abdomen."
        m "As you said earlier, this is a sanctuary where we stand on equal footing."
        "You feel her slide down till her pussy idles just above your cock."
        m "I intended to perform in the same manner as my loving partner performed for me."
        show moon13
        with dissolve
        pause
        "Moon begins shifting her hips forward, then instantly dragging them back as she travels the full length of your dick."
        mc "Oooh, god, that feels good."
        "You feel your nuts start to constrict; the sensation of Moon's grind brings you to a rapid conclusion."
        pause
        play sound chair
        scene ch1ep4_1154
        with hpunch
        hide moon13
        "Moon senses you're at your wit's end and, in esteemed fashion, pops the head of your dick into her pussy on her last slide backwards."
        mc "Oooh, FUCK!!!" with hpunch
        "The warm sensation of Moon's cunt swallowing up your head causes you to blow your load immediately."
        "Moon's grinning expression turns to surprise as she senses another round of hot blasts dumping into her."
        scene ch1ep4_1155
        with dissolve
        m "Wait... what? How did that not cause you to \"suck it back in\" like it did with me?"
        "You chuckle while gathering your breath."
        mc "We're, well... designed a little differently, Moon."
        mc "Once it starts, you can't stop what's to come... literally."
        scene ch1ep4_1156
        with dissolve
        "Moon pouts, looking down at you petulantly while crossing her arms."
        m "That's not fair..."
        mc "Welp, it's science..."
        m "I guess thinking on my feet during our sexual escapades is still going to need more work."
        "Moon places her hands on her hips, showing full well she's not very pleased with how things went."
        m "Now I feel so-"
        play sound bodyhit
        show moon14
        with hpunch
        pause
        "Sensing her sexual frustration, you grab her hips and push her back hard while simultaneously trusting your hips."
        "Your scrotum flies up and slaps her perineum."
        "Moon's soulful look vanishes as an aroused one takes its place."
        "Her mouth hangs agape as her eyes roll towards the back of her head."
        m "Aohhhh!!"
        m "Oohhh yes!! YES!!!!"
        "Egged on by Moan's--er, Moon's cries, you use the springiness of your mattress to pump away at her."
        yt "Situational awareness and fully utilizing your environment, check."
        "Unrelentingly, you continue to jackhammer away at Moon's fully engorged vagina."
        m "Nghaahahhss...!"
        "Her words are becoming more unintelligible with each thrust."
        "Simultaneously, Moon's typically precise, controlled movements give way to involuntary twitches and wild flops."
        "Now, the swordmaster's movements resemble a wet noodle's."
        "Well, a wet noodle that can't get enough of being pounded mercilessly."
        pause
        show moon15
        with dissolve
        hide moon14
        pause
        play sound chair
        scene ch1ep4_1157
        with hpunch
        hide moon15
        "Eventually, Moon regains her composure and slams her hands down on your waist, causing you to stop thrusting."
        "You can see her breathing heavily with an elated expression on her face."
        m "Oh, I see what you did there... but you're not taking over {i}that{/i} easily."
        m "My turn!"
        play sound chair
        show moon16
        with hpunch
        pause
        "Once again, she goes to grind on you; this time, with you buried inside her pussy."
        "You shudder as you feel the head of your cock scrape along the insides of her vaginal wall."
        m "MMmmmmm..."
        "Moon also noticeably moans as she feels the head of your cock glide against her most sensitive of areas."
        "An area you surmise to be her actual G-spot... you mentally take notice of the exact location, as if mapping out the insides of her pussy."
        yt "More intel to use for later..."
        "Once again, you can sense the inside of Moon's pussy start to spasm and clamp down on your dick."
        m "YES!!! OH GOD, this...!!!"
        play sound chair
        scene ch1ep4_1158
        with hpunch
        "She slides back {b}hard{/b}, ingesting your cock deep within, all the way down to its base."
        m "Oh GOD, YES!!!"
        "Once again, Moon's face contorts into a pleasurable display of beauty and elation, and her eyes roll upwards in bliss."
        mc "Oooh, FFFfffuck...!"
        "Your pleasure climaxes as you release the very last of the ejaculate stored in your testes."
        play sound chair
        scene ch1ep4_1159
        with hpunch
        "Filled to the brim, Moon finally slumps on top of you, placing her head on your chest."
        "She presses her ear to your sternum, listening to your quickened heartbeat due to recent events."
        scene ch1ep4_1160
        with dissolve
        m "[mc]..."
        mc "... Yeah?"
        m "I agree with you fully..."
        "She pauses to gather her breath before she continues."
        scene ch1ep4_1161
        with dissolve
        m "That was far, {i}far{/i} more intense than the last one."
        scene ch1ep4_1162
        with dissolve
        "You reach up and pet the top of Moon's head."
        mc "Continuing despite having already had a release, while being already sensitive, can certainly elevate the sexual experience to greater heights."
        m "That's good to know."
        m "And spoken like a true nympho."
        mc "Maybe I just can't help myself when I'm with you."
        m "Watch your words, Commander. I might just have to enter the sanctuary for another round."
        play sound cloth
        scene ch1ep4_1163
        with Dissolve(1.0)
        "Smiling, Moon rolls off and snuggles alongside you."
        m "This was incredible; I've never experienced that kind of pleasure before, even when I tried to... well, do it myself."
        mc "It's obvious as to why."
        "Moon looks at you, intrigued."
        m "Oh, you've already figured it out?"
        mc "Yes. It's because we've bared our souls to one another, exposing our love in the most intimate ways."
        m "Mmmm, yes... you're right."
        scene ch1ep4_1164
        with dissolve
        "Moon settles into your side, and you place your arm around her to pull her close."
        "As time passes, you can't help but stay still."
        "With Moon next to you, how could you not feel totally content with life?"
        "Your thoughts are interrupted by a steady rhythm of breathing coming from Moon."
        "Perhaps she has dozed off. That wouldn't be surprising considering the energy you both expended."
        scene ch1ep4_1165
        with dissolve
        "But to your mild surprise, Moon speaks."
        m "[mc]...?"
        mc "Hmmm?"
        m "Do you not like it when I call you Commander?"
        mc "Well, I figured we've moved past that, given our relationship is much more intimate now."
        mc "You can just call me by my name."
        scene ch1ep4_1166
        with dissolve
        m "Right..."
        "There is a long pause."
        scene ch1ep4_1167
        with dissolve
        m "Can I also call you by something else?"
        "You chuckle slightly at her innocent question."
        mc "Again, Moon, my name is fine... but sure, what were you thinking?"
        scene ch1ep4_1168
        with dissolve
        m "*whispers* My purpose..." with Dissolve(2.0)
        mc "What was that?"
        scene ch1ep4_1169
        with dissolve
        m "My purpose."
        "You smile at hearing this, knowing full well the implications you've gathered from Moon's talks."
        m "Now that I finally have it, I will never let you go either, my husband."
        "Moon hugs you tightly, almost possessively."
        mc "Aye, and we will continue to be inseparable for all eternity, my wife."
        stop music fadeout 2
        $ renpy.end_replay()

    call hide_days from _call_hide_days_33
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_saturday with dissolve
    play music 'audio/KingsRansom.mp3'
    play sound closedoor
    scene ch1ep4_1024
    with dissolve
    mc "Aine."
    scene ch1ep4_1025
    with dissolve
    a "[mc], we need to talk."
    mc "Yeah, I was about to look for you."
    a "Let's head downstairs, then."

    scene black
    with dissolve
    with fadeq

    scene ch1ep4_1026
    with dissolve
    mc "I see, so you already took over..."
    mc "Sorry, I kind of pushed you into it."
    scene ch1ep4_1027
    with dissolve
    a "No, don't be. I did hesitate, yes. But I couldn't leave it hanging after learning about the group's state. It was such a mess."
    mc "How did her men take it?"
    a "Well... they welcomed me with open arms."
    a "She left them just like that; it's not like they had any choice, anyway."
    scene ch1ep4_1028
    with dissolve
    a "[mc], we eventually must decide what to do about it. You, especially. We can no longer take this lightly."
    mc "I know, it's just... there's something I don't get about your mother's ideology..."
    mc "Why reform a mafia group into a charity?"
    mc "Because she wants to give back to those who work for her? Because that's what she and her husband wanted? Because she's a good person behind the facade?"
    mc "I don't think that's all there is to it."
    a "I know the real reason... and that is where the {i}real{/i} problem comes from."
    a "While you were asleep, I got to talk to Bonheur."
    scene ch1ep4_1029
    with flash
    bo "*chuckles* That's where you're mistaken, Miss Agnor."
    bo "I didn't plan to control you and your friends; you all simply got caught in my... let's say, skirmish."
    bo "Hera saw through my intentions and tried to counter the possible future by reforming the mafia."
    bo "So, I attempted to stop her by arranging for either me or my son to marry you, thus taking full control of the throne."
    scene ch1ep4_1030
    with dissolve
    a "Keep dreaming."
    bo "Certainly, it is all but a dream now, isn't it?"
    a "And what was your goal after sitting on the throne?"
    bo "It was quite simple: not to waste the Agnor Mafia's potential."
    bo "Its resources could easily revive my past project, which sadly shut down after the war between Glabia and Sha Crea concluded."
    a "And you failed."
    scene ch1ep4_1031
    with dissolve
    bo "*laughs* Failed? No, not at all, Miss Agnor."
    scene ch1ep4_1032
    with dissolve
    bo "Do whatever you wish to me. After all, the die is cast."
    bo "Do you think a lowly human being like me can do the work of the Gods?"
    bo "In the far future, something far more significant will come..."
    bo "In the grand scheme of things, and the future of this world, I am... but a mere observer."
    scene ch1ep4_1033
    with dissolve
    a "What... the hell are you up to?"
    bo "My tongue is tied; I am forbidden to talk. In any case, I'll be kind enough to give you a warning..."
    bo "Be careful about Francis."
    bo "Now that there's no one to control him, who knows what he'll do."
    a "Don't tell me he's a Number, too?"
    scene ch1ep4_1034
    with dissolve
    bo "No, he is not. My project was long gone before I even found him."
    bo "He's... not what you think he is."
    a "Tell me what he's up to."
    bo "I don't know that either."
    scene ch1ep4_1035
    with dissolve
    bo "All his charades to get Olivia back, his so-called sister... are all in his head."
    bo "This Olivia person does not exist." with Dissolve(1.0)
    scene ch1ep4_1036
    with flash
    mc "..."
    scene ch1ep4_1037
    with dissolve
    mc "Did he say anything else after that?"
    a "No, he refused to talk no matter how much we pushed him."
    a "Unfortunately, we couldn't find Francis in that mansion. He ran with his tail tucked between his legs."
    mc "To be expected. I'm pretty sure I told his father the same thing before."
    mc "Let's arrange a search for Francis. Before we decide what to do with the mafia, let's make use of it."
    a "Good call. We can't let him roam free in the streets. There's really no telling what he'll do."
    play sound casepickup
    scene ch1ep4_1038
    with dissolve
    a "Hey, we found this though..."
    a "I'm not sure if she wants it back, but I'll leave it to you to return it to her."
    mc "..."
    play sound casepickup2
    scene ch1ep4_1039
    with dissolve
    mc "Just... how many lives did this thing take?"
    scene ch1ep4_1040
    with dissolve
    a "... Moon can be so cruel, but she's also the most gentle soul I've ever met. I'm glad to have her as my friend, [mc]."
    mc "Yeah, I know that more than anyone."
    a "When I arrived to get you two out of there, I saw someone in so much pain kneeling before you. Not on the outside, but on the inside."
    a "I want to protect her, as much as she wants to protect us. I don't... want to see her in that state again, [mc]."
    scene ch1ep4_1041
    with dissolve
    mc "..."
    stop music fadeout 2
    
    scene black
    with dissolve
    with fade
    
    play sound windgrass loop
    scene ch1ep4_1042
    with dissolve
    pause
    yt "Everything... is done, right? This is peace."
    yt "Then... why do I feel like I've lost something? Something important within me."
    yt "... I'm not... the same as I was before..."
    yt "Everything isn't the same as before..."
    play music 'audio/LinesIdCross.mp3'
    scene ch1ep4_1043
    with dissolve
    m "[mc]?"
    yt "... But I'm not alone..."
    mc "*chuckles* I can't express how it feels not being called \"Commander\" the first thing you say every time you see me."
    scene ch1ep4_1044
    with dissolve
    m "Then how about I call you \"My Lord\" instead? As I rightfully should."
    mc "That's even worse."
    mc "No need for those titles anymore, Moon. We're way past those times already. Just call me by my name. That's more than enough."
    m "Alright."
    scene ch1ep4_1045
    with dissolve
    mc "Anyway, here. Aine found it when she got us out."
    m "..."
    scene ch1ep4_1046
    with dissolve
    m "You keep it."
    mc "Why?"
    m "I already have you; I don't need it anymore, [mc]. And..."
    m "It was yours to begin with."
    mc "That's right..."
    scene ch1ep4_1047
    with dissolve
    m "It's about time I fully let go of the past."
    m "No, {i}we{/i} will let go of the past."
    scene ch1ep4_1048
    with dissolve
    m "What happened to me during the war, or to us hundreds of years ago, no longer matters. What matters now is the two of us today."
    m "Whether you're my husband or not, whether I'm your bodyguard or not..."
    scene ch1ep4_1049
    with Dissolve(1.0)
    m "I will still love you from the bottom of my heart." with Dissolve(1.0)
    m "I don't want to just stay by your side, [mc]. I will walk with you until the end of time."
    m "After all, in heart and spirit, we... are a singular fate."
    m "That is the answer I found."
    scene ch1ep4_496
    with flash
    m "Uh... Commander?"
    mc "Yeah?"
    m "Are you really my husband?"
    mc "If the history records and the details about the serum are correct, then technically, yes..."
    m "And I'm your wife?"
    mc "Yep."
    m "Then what do we do now? I have no idea what to make of it."
    scene ch1ep4_1050
    with flash
    mc "..."
    scene ch1ep4_1051
    with dissolve
    mc "Jesus... Just how many times do you want this man's heart to flutter?"
    m "As many times as you want me to express what I feel for you."
    mc "*chuckles* I'll hold you to that."
    stop music fadeout 4
    scene ch1ep4_1052
    with dissolve
    shu "Hey, hey, hey!"
    mc "Of course, you always have a knack for showing up at the perfect time."
    scene ch1ep4_1053
    with dissolve
    shu "Sorry, did I interrupt something?"
    mc "No, don't worry about it."
    play sound2 closedoor
    scene ch1ep4_1060
    with dissolve
    a "Uh, guys...? Dinner is ready!"
    a "If you don't come in soon, Klara will... Well, you know what will happen."
    stop music fadeout 5
    scene ch1ep4_1061
    with dissolve
    mc "Let's go."
    yt "What do I do with this thing inside me...?"
    yt "I don't know..."
    yt "But if there's a God, a Deity, or whatever brought me to this fate... please let me use it for something good."
    play sound2 heartbeat_fast loop fadein 2
    scene ch1ep4_1062
    with dissolve
    pause
    scene ch1ep4_1063
    with dissolve
    m "..."
    stop sound
    stop sound2
    scene black
    pause

    call hide_days from _call_hide_days_34
    with dissolve
    show ch1ep4end
    with dissolve
    pause 183.5
    scene black
    with dissolve
    pause

    play sound2 windgrass loop
    play sound chime_bell
    scene ch1ep4_1064
    with Dissolve(0.2)
    pause
    play sound3 teleport
    scene ch1ep4_1065
    pause
    am "Have you secured the place?"
    ee "Yes. It seems she's not around."
    ee "I also summoned 7th to watch the perimeters, just to make sure."
    am "That's good to know."
    scene ch1ep4_1066
    with dissolve
    ee "Mistress, may I ask something?"
    am "Yes?"
    ee "Why are we watching over these people? Why are you so fond of their stories?"
    am "For a lot of reasons."
    am "You know the most important one. And the rest is a little... personal."
    scene ch1ep4_1067
    with dissolve
    am "I've lived since this world's first sunrise, E..."
    am "... They are the only ones who remind me of what being human is like. Of what it feels like not being bound to this eternal curse."
    am "I will not allow her to tamper with their fates, especially [mc]'s."
    scene ch1ep4_1068
    with dissolve
    ee "... Perhaps I will never understand what that means, but I will carry out your will without question."
    scene ch1ep4_1067
    with dissolve
    am "You have a lot to work on, E..."
    am "A time will eventually come when someone changes who you are. Only then will you finally open your eyes."
    scene ch1ep4_1068
    with dissolve
    ee "But... I won't be able to see either way."
    am "*sighs* That's not what I meant..."
    am "Anyway, we're done here. Call off Maya and Jinn. We'll return for the time being."
    ee "Right away."
    stop sound2 fadeout 2
    scene continued
    with dissolve
    call hide_days from _call_hide_days_35
    with dissolve
    pause

    play music 'audio/NeeTheme.mp3'
    scene ch1ep4_1069
    with dissolve
    nee "Hey, you made it this far! You've finally reached the end of Chapter 1!"
    nee "That means you really like the game despite its shortcomings, and that means a lot to us."
    scene ch1ep4_1070
    with dissolve
    show screen patreonpagepop with dissolve
    nee "If you enjoyed it, please consider supporting {b}NiiChan{/b} on his Patreon page."
    nee "Every bit of support helps and goes a long way!"
    hide screen patreonpagepop with dissolve
    scene ch1ep4_1071
    with dissolve
    nee "{b}My Bully is My Lover{/b} will soon continue with Chapter 2, its final chapter.\n{i}(Will contain an estimate of 6-7 Episodes){/i}"
    nee "I can't wait to see you guys there!"
    nee "Thank you for playing and for your amazing support!"
    stop music fadeout 2
    scene black
    with dissolve
    pause


    jump ch2ep1
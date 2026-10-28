label ep10_ln_intro_label:
$ guideSuggestedPage = 92
scene ep10_ln_intro1 with fade
$ renpy.pause()
scene ep10_ln_intro2 with dissolve
nic "More coffee?"
scene ep10_ln_intro3 with dissolve
ly "Pour it on my face."
play sound "sound_effects/season2/pour.mp3"
scene ep10_ln_intro4 with dissolve
nic "Is the hangover that bad?"
scene ep10_ln_intro3 with dissolve
ly "Like a sledgehammer to the head. You?"
scene ep10_ln_intro5 with dissolve
nic "Surprisingly, I feel fine. Not too shabby for little-old-me, huh?"
scene ep10_ln_intro6 with dissolve
ly "I don't get it. You should feel like shit today. You kept pushing me to drink more all night."
scene ep10_ln_intro7 with dissolve
nic "It's karma for you making all those jokes about me yesterday."
scene ep10_ln_intro8 with dissolve
ly "What about you, [name]? Did you get visited by the hangover fairy, too?"
scene ep10_ln_intro9 with dissolve
mc "No, I think she visited you two times. I'm tired, but I feel fine."
mc "Thanks for the fun last night. What a way to end the night it was."
scene ep10_ln_intro10 with dissolve
nic "I also blame Lily for that one."
scene ep10_ln_intro6 with dissolve
ly "Yeah, yeah. Blame me for everything."
ly "I wanted to have a good time with you two, and I got it."
scene ep10_ln_intro10 with dissolve
nic "I think we all got it."
scene ep10_ln_intro8 with dissolve
ly "Ugh... I can't believe I have to work tonight..."
scene ep10_ln_intro9 with dissolve
mc "Is there no way to get out of it?"
scene ep10_ln_intro6 with dissolve
ly "Only if I can find someone to cover my shift."
scene ep10_ln_intro7 with dissolve
nic "Don't look at me. Luke is dropping off Marvin in a few hours from now."
scene ep10_ln_intro12 with dissolve
mc "Who?"
scene ep10_ln_intro11 with dissolve
nic "Marvin's my son and Luke is his dad."
scene ep10_ln_intro12 with dissolve
mc "Ah, got it."
scene ep10_ln_intro11 with dissolve
nic "And I hate to be like this, but you two should leave soon."
nic "I don't want him to come home to see this."
scene ep10_ln_intro8 with dissolve
ly "We should leave, anyway. Sage hammered it in that we should help you guys clean."
ly "So, I guess I'll be working double shifts today. Yippee..."
scene ep10_ln_intro13 with dissolve
ly "I better get ready."
scene ep10_ln_intro14 with dissolve
nic "Sorry for kicking you out like this."
scene ep10_ln_intro15 with dissolve
mc "Don't be. I get it."
if envyLikesYou:
    if ep9_spoon_nicole:
        scene ep10_ln_intro16 with dissolve
        nic "But I guess I'll see you soon."
        scene ep10_ln_intro17 with dissolve
        mc "You will?"
        scene ep10_ln_intro16 with dissolve
        nic "I think I will. And I'm not talking about at The Pink Rose."
    else:
        scene ep10_ln_intro16 with dissolve
        nic "But I was thinking... Would you like to get together sometime soon?"
        scene ep10_ln_intro17 with dissolve
        mc "Together, like how?"
        scene ep10_ln_intro16 with dissolve
        nic "How about a date?"

    scene ep10_ln_intro17 with dissolve
    if ep9_spoon_nicole:
        mc "I'd love to go out on a date. When?"
        jump ep10_date_nic_label
    if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Reject Nicole)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]
    menu:
        "Date her":
            mc "I'd love to date you. When?"
            label ep10_date_nic_label:
            $ ep10_date_nicole = True
            $ ep10_rejected_nicole = False
            scene ep10_ln_intro16 with dissolve
            nic "Well, I got Marvin this week. Would next Saturday work for you?"
            scene ep10_ln_intro17 with dissolve
            mc "Next Saturday sounds great."
            scene ep10_ln_intro23 with dissolve
            nic "*{i}Smack{/i}*"
            scene ep10_ln_intro24 with dissolve
            $ renpy.pause()
            $ new_bio("Envy", "I told Nicole that I wanted to date her.")
        "Don't date her [m_c1][mod_choices[0]]":
            $ ep10_date_nicole = False
            $ ep10_rejected_nicole = True
            mc "I've thought about it..."
            mc "And listen... You have a kid."
            scene ep10_ln_intro18 with dissolve
            nic "Is that a problem?"
            scene ep10_ln_intro19 with dissolve
            mc "I'm 19, Nicole... I'm not ready for that kind of commitment, I think."
            scene ep10_ln_intro20 with dissolve
            nic "Yeah... I can't deny that I haven't thought about it. But I wanted to give it a shot anyway."
            scene ep10_ln_intro21 with dissolve
            mc "It's not that you're not great, because I think you are."
            mc "You're an amazing girl, and I like a lot about you. It's just me and where I'm at in life..."
            scene ep10_ln_intro22 with dissolve
            nic "This is probably the first time I believe the \"It's not you, it's me\" speech."
            nic "It's fine, [name]. We don't have to date."
            nic "I still like you, though."
            scene ep10_ln_intro25 with dissolve
            nic "*{i}Smack{/i}*"
            scene ep10_ln_intro26 with dissolve
            nic "..."
            $ new_bio("Envy", "I told Nicole that I didn't want to date her because I wasn't ready to commit to someone with a kid.")
else:
    scene ep10_ln_intro14 with dissolve
    nic "Thanks, [name]."
$ guideSuggestedPage = 93
if not ep7_lily_lewd:
    jump ep10_dik_intro_label
scene ep10_ln_intro27 with wipeleft
mc "Did we walk this way yesterday?"
scene ep10_ln_intro29 with dissolve
ly "Don't you remember it?"
scene ep10_ln_intro28 with dissolve
mc "No, not at all..."
scene ep10_ln_intro29 with dissolve
ly "I can't say I'm surprised. We almost had to carry you back with us."
scene ep10_ln_intro30 with dissolve
ly "Over there is where we fucked."
mc "Oh, yeah! Now I remember."
menu:
    "What were we thinking?":
        mc "Looking at it in daylight... What were we thinking?"
        scene ep10_ln_intro31 with dissolve
        ly "What the hell! That's something you say when you wake up with an ugly fuck in your bed."
        scene ep10_ln_intro32 with dissolve
        mc "I wasn't talking about you and Nicole. I was talking about fucking in public like that."
        mc "But I don't regret doing it."
    "What a night":
        mc "What a night it was."
        scene ep10_ln_intro31 with dissolve
        ly "Haha! It was an awesome night, for sure."
        scene ep10_ln_intro32 with dissolve
        mc "The party was great, but fucking you two was the highlight of the night."
scene ep10_ln_intro31 with dissolve
ly "It was hot, wasn't it?"
scene ep10_ln_intro32 with dissolve
mc "Yeah, you can say that again."
scene ep10_ln_intro33 with dissolve
ly "Which begs the question..."
ly "Are we finally rolling now, or what?"
scene ep10_ln_intro34 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Lily path)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "We're rolling [m_c1][mod_choices[0]]":
        $ ep10_rolling = True
        mc "Yeah. We're rolling."
        scene ep10_ln_intro37 with dissolve
        ly "It's about time."
        scene ep10_ln_intro38 with dissolve
        mc "I made you wait long enough."
        scene ep10_ln_intro37 with dissolve
        ly "You sure took your sweet time to make up your mind, but someone worth rolling with would make me wait."
        scene ep10_ln_intro39 with dissolve
        mc "How do you roll with someone?"
        scene ep10_ln_intro40 with dissolve
        ly "It's a state of mind, dude."
        ly "We hang, we fuck, we cover each other's asses."
        scene ep10_ln_intro42 with dissolve
        menu:
            "Just you and me, huh? [m_c1][mod_choices[2]]":
                $ dk(-1)
                mc "Just you and me, huh?"
                scene ep10_ln_intro41 with dissolve
                ly "Hold up. Don't take it that far. It's not a relationship."
            "Can I date others?":
                mc "Can I date others or do you expect us to stay exclusive?"
                scene ep10_ln_intro41 with dissolve
                ly "It's fine by me, but maybe it won't be fine by them."
            "Can I sleep around? [m_c1][mod_choices[3]]":
                $ dk(1)
                if affinity == "DIK":
                    mc "Can I still fuck others?"
                    scene ep10_ln_intro41 with dissolve
                    ly "Yeah, why wouldn't you? Bang away!"
                else:
                    mc "If I wanted to...can I sleep around or do you expect me to stay faithful?"
                    scene ep10_ln_intro41 with dissolve
                    ly "Faithful? It's not a relationship. Go ahead and bang away."
        ly "I don't care about what you do with someone else, nor do you."
        ly "But if you need me or if I need you, no questions will be asked, and we always prioritize each other's needs."
        ly "We're in sync, we understand each other, and we're fucking partners in crime."
        scene ep10_ln_intro42 with dissolve
        if affinity == "DIK":
            mc "Those sound like my kind of rules."
        else:
            mc "That sounds...cool."
        scene ep10_ln_intro41 with dissolve
        ly "Cool."
        if ep9_spoon_lily:
            scene ep10_ln_intro43 with dissolve
            ly "And to make it clear, no spooning and stuff, ok?"
            scene ep10_ln_intro42 with dissolve
            menu:
                "Spooning feels good":
                    mc "Why not? Spooning doesn't mean you're in a relationship, if that's what you think. It feels good."
                    scene ep10_ln_intro41 with dissolve
                    ly "*{i}Sigh{/i}* No spooning. Ok?"
                    scene ep10_ln_intro42 with dissolve
                    mc "I mean, if that's where you draw the line, no spooning."
                "Define stuff":
                    mc "You'll have to define \"stuff\" for me."
                    scene ep10_ln_intro41 with dissolve
                    ly "We'll get there."
        play sound "sound_effects/shove.mp3"
        scene ep10_ln_intro44 with hpunch
        ly "Excited about it?"
        scene ep10_ln_intro45 with dissolve
        if affinity == "DIK":
            mc "Fuck yeah!"
        else:
            mc "I think I am."
        $ new_bio("Lily", "I told her that we could roll, and she was very excited about it. I wasn't sure what that meant, but she seemed to have it figured out.")
    "We're just fucking":
        $ ep10_rolling = False
        mc "No, we're just fucking."
        scene ep10_ln_intro35 with dissolve
        ly "It's almost the same thing, but fine."
        ly "If you don't wanna roll, you don't want to."
        ly "I'm not gonna force you or anything."
        scene ep10_ln_intro36 with dissolve
        mc "It feels like a commitment. I'm not there yet."
        scene ep10_ln_intro35 with dissolve
        ly "It's not a fucking relationship, but yeah, it takes commitment."
        ly "And I get it. It's not for everyone."
        $ new_bio("Lily", "I told her that I wasn't interested in rolling with her but still wanted to fuck her.")
scene ep10_ln_intro46 with dissolve
if ep10_rolling:
    if affinity == "DIK":
        mc "Can I grab your ass in public?"
        ly "Haha! I don't see why you couldn't."
        mc "Awesome."
    else:
        mc "But to others, it will look like we're in a relationship, won't it?"
        ly "It will confuse the hell out of them and that's part of the fun."
else:
    $ renpy.pause()
jump ep10_dik_intro_label

label ep10_smq_intro_label:
$ guideSuggestedPage = 93
scene ep10_sqm_intro1 with fade
$ renpy.pause()
scene ep10_sqm_intro2 with dissolve
el "Morning, [name]. You're here, huh?"
scene ep10_sqm_intro3 with dissolve
mc "Well, you know?"
scene ep10_sqm_intro4 with dissolve
el "I can guess."
scene ep10_sqm_intro3 with dissolve
mc "Fun night last night."
scene ep10_sqm_intro5 with dissolve
el "You can say that again."
scene ep10_sqm_intro6 with dissolve
js "Morning, [name]... You're here early."
scene ep10_sqm_intro7 with dissolve
mc "Yeah, you could say that."
scene ep10_sqm_intro8 with dissolve
js "Oh... I think I got it."
scene ep10_sqm_intro9 with dissolve
el "No, I think someone else got it. Haha."
scene ep10_sqm_intro10 with dissolve
js "Right... See you later."
scene ep10_sqm_intro11 with dissolve
el "She did not like that joke."
scene ep10_sqm_intro12 with dissolve
mc "Yeah, well, we have some...history."
scene ep10_sqm_intro13 with dissolve
el "Fuck... That's right. Was that insensitive of me?"
scene ep10_sqm_intro12 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Lily path)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "A bit [m_c1][mod_choices[2]]":
        $ dk(-1)
        if affinity == "DIK":
            mc "Yeah, a bit. But it doesn't matter."
        else:
            mc "Yeah, a bit."
        scene ep10_sqm_intro13 with dissolve
        el "I should apologize to her later. And sorry to you, too."
        scene ep10_sqm_intro12 with dissolve
        mc "No apology is needed. I'm single. I can do what I want."
        play sound "sound_effects/season2/pour.mp3"
        scene ep10_sqm_intro14 with dissolve
        el "How's that going for you?"
    "No [m_c1][mod_choices[3]]":
        $ dk(1)
        if affinity == "DIK":
            mc "Nope, it was a fun joke. And she knows I'm single."
        else:
            mc "No. Not at all. I'm single, after all."
        play sound "sound_effects/season2/pour.mp3"
        scene ep10_sqm_intro14 with dissolve
        el "Yeah, you are. How's that going for you?"
$ guideSuggestedPage = 94
scene ep10_sqm_intro15 with dissolve
mc "I can't complain."
scene ep10_sqm_intro16 with dissolve
el "So, who did you spend the night with?"
scene ep10_sqm_intro17 with dissolve
mc "Wouldn't you like to know?"
scene ep10_sqm_intro16 with dissolve
el "Hence the question."
scene ep10_sqm_intro17 with dissolve
menu:
    "Tell her":
        if ep9_quinn_lewd:
            mc "She'd kill me if I told you."
            scene ep10_sqm_intro18 with dissolve
            el "Quinn, huh?"
            scene ep10_sqm_intro17 with dissolve
            mc "Was it that easy to guess?"
            scene ep10_sqm_intro18 with dissolve
            el "I can't see anyone else having a problem with it."
            el "Well, unless it was Heather or Ashley, maybe. But I don't see that happening."
            scene ep10_sqm_intro16 with dissolve
            el "So, what's going on between you and Quinn? Just sex or?"
            scene ep10_sqm_intro17 with dissolve
            menu:
                "Yeah":
                    mc "Yeah, that's what she'd call it."
                    scene ep10_sqm_intro18 with dissolve
                    el "Would you call it something else?"
                    scene ep10_sqm_intro17 with dissolve
                    mc "It's not the first time we've fucked, and if you ask me, I'd like there to be many more times."
                    scene ep10_sqm_intro19 with dissolve
                    el "Wow... With Quinn? You surprise me, [name]."
                    scene ep10_sqm_intro17 with dissolve
                    mc "Is it that hard to imagine?"
                    scene ep10_sqm_intro19 with dissolve
                    el "Not based on what I've seen and heard, but still... It's hard to believe there's potential for something between you two."
                "I don't know":
                    mc "I don't know. There might be something more between us, but she'd never admit it."
                    scene ep10_sqm_intro20 with dissolve
                    el "I'm not surprised by that. I've never heard her talk about relationships, and I have a hard time imagining she'd be in one."
                    scene ep10_sqm_intro17 with dissolve
                    mc "She isn't open to talking about it and she hates when I try to do stuff to her."
                    scene ep10_sqm_intro20 with dissolve
                    el "Stuff, like what?"
                    scene ep10_sqm_intro17 with dissolve
                    mc "PDA is a big turn-off for her."
                    scene ep10_sqm_intro19 with dissolve
                    el "Aw...[name]."
                    scene ep10_sqm_intro17 with dissolve
                    mc "Haha, I'm fine. I think I have figured her out."
                    scene ep10_sqm_intro20 with dissolve
            el "I hope it works out for you."
            scene ep10_sqm_intro17 with dissolve
            mc "Thanks. Me too."
        else:
            mc "I'm not sure if they'd mind me sharing it."
            scene ep10_sqm_intro20 with dissolve
            el "They!?"
            el "Did you hook up with two HOTs or is your pronoun game that strong?"
            scene ep10_sqm_intro17 with dissolve
            mc "Haha, yeah. Sarah and Mel."
            scene ep10_sqm_intro19 with dissolve
            el "Oh! Of course. Yeah, that makes sense."
            scene ep10_sqm_intro17 with dissolve
            mc "It makes sense?"
            scene ep10_sqm_intro21 with dissolve
            el "I don't know the nicest way to tell you this, but..."
            el "Maybe I shouldn't tell you."
            scene ep10_sqm_intro17 with dissolve
            mc "Hey, we're friends, right? Tell me."
            scene ep10_sqm_intro21 with dissolve
            el "Don't get sad, but they do this a lot."
            scene ep10_sqm_intro17 with dissolve
            mc "I had a feeling."
            scene ep10_sqm_intro20 with dissolve
            el "That doesn't mean you might not be special, but I don't want to get your hopes up."
            scene ep10_sqm_intro17 with dissolve
            mc "I understand. Besides, it was just sex anyway."
            mc "It's not like I'm going for a relationship with either of them."
            scene ep10_sqm_intro22 with dissolve
            el "Congrats to the threesome, then."
            scene ep10_sqm_intro17 with dissolve
            mc "Thanks!"
            mc "You won't spread this, right?"
            scene ep10_sqm_intro20 with dissolve
            el "I would never! But I can't promise that it won't spread. Those girls talk a lot."
            el "Know that if it spreads, it's not coming from me."
            scene ep10_sqm_intro17 with dissolve
            mc "Thanks."
    "Don't tell her":
        mc "Sorry, but that's a secret."
        scene ep10_sqm_intro18 with dissolve
        el "Aw, I thought we were friends."
        scene ep10_sqm_intro17 with dissolve
        mc "Are you using the friendship angle to make me say it?"
        scene ep10_sqm_intro16 with dissolve
        el "No, it's fine. I'm sure I'll find out somehow anyway. I just thought you'd be cool with sharing."
        scene ep10_sqm_intro17 with dissolve
        mc "Maybe another time."
        scene ep10_sqm_intro16 with dissolve
        el "I hear you."
        scene ep10_sqm_intro17 with dissolve

if ep9_quinn_lewd:
    scene ep10_sqm_intro23 with dissolve
    qu "What the fuck are you still doing here?"
    scene ep10_sqm_intro24 with dissolve
    el "Aha... And that's my cue to leave. See you, [name]."
    scene ep10_sqm_intro25 with dissolve
    qu "What part of \"exit through my window or the back door\" was unclear to you?"
    scene ep10_sqm_intro26 with dissolve
    mc "I was hungry, so I made myself some breakfast."
    scene ep10_sqm_intro27 with dissolve
    qu "..."
    mc "Do you wanna talk about why that makes you mad?"
    scene ep10_sqm_intro28 with dissolve
    qu "No. You've had your breakfast. It's time to leave."
    scene ep10_sqm_intro27 with dissolve
    mc "Wait a fucking minute! You bring me back here to fuck and then you make out with me during the night..."
    mc "And, come morning, you act as if last night didn't mean anything."
    mc "That kind of pisses me off."
    scene ep10_sqm_intro28 with dissolve
    qu "It pisses {i}you{/i} off?"
    scene ep10_sqm_intro27 with dissolve
    mc "It does."
    scene ep10_sqm_intro28 with dissolve
    qu "Dude, I'm hungover here. I don't wanna discuss this."
    qu "I wanted sex last night, and I got it. Why does it have to be more than that?"
    qu "If I knew I'd wake up to your drama queen bullshit, I wouldn't have fucked you."
    scene ep10_sqm_intro27 with dissolve
    mc "I think it scares you to admit that you like me."
    scene ep10_sqm_intro29 with dissolve
    qu "..."
    scene ep10_sqm_intro28 with dissolve
    qu "You couldn't be more wrong."
    scene ep10_sqm_intro27 with dissolve
    mc "Well, I like you. I'm not scared to admit that."
    scene ep10_sqm_intro30 with dissolve
    $ renpy.pause()
    play sound "sound_effects/shove.mp3"
    scene ep10_sqm_intro31 with hpunch
    mc "Hey! I was eating that!"
    scene ep10_sqm_intro32 with dissolve
    mc "*{i}Sigh{/i}*"
    $ new_bio("Quinn", "She got mad at me for staying at the HOTs and eating breakfast despite her telling me to leave.")
else:
    mc "I'm heading back to the mansion before they think I skipped cleaning day."
    scene ep10_sqm_intro20 with dissolve
    el "I'll meet you there later after my coffee injection and breakfast."
    scene ep10_sqm_intro17 with dissolve
    mc "Sounds perfect."
jump ep10_dik_intro_label

label ep10_others_intro_label:
$ ep10_others_intro = True
if ep9_tiffani_gina_tara:
    scene ep10_others_intro1 with fade
else:
    scene ep10_others_intro1b with fade
$ renpy.pause()

scene ep10_others_intro2 with dissolve
ta "Has anyone seen my sheet?"
scene ep10_others_intro3 with dissolve
ti "It's by the foot of the bed."
if ep9_tiffani_gina_tara:
    scene ep10_others_intro4 with dissolve
else:
    scene ep10_others_intro4b with dissolve
gi "Ugh. I stink; I need a shower."
scene ep10_others_intro5 with dissolve
ti "Tell me about it; my mouth tastes horrible."

scene ep10_others_intro6 with dissolve
ti "Why are you putting that sheet back on?"
scene ep10_others_intro7 with dissolve
ta "I'm not walking out showing my face. Haven't you heard what they do to girls like that?"
scene ep10_others_intro6 with dissolve
ti "Who cares?"
ti "And don't you think they'll know it's you - sheet or no sheet?"
scene ep10_others_intro7 with dissolve
ta "I don't think so. I didn't show my face to them."
if ep9_tiffani_gina_tara:
    scene ep10_others_intro8 with dissolve
else:
    scene ep10_others_intro8b with dissolve
gi "Let's leave."
if ep9_tiffani_gina_tara:
    scene ep10_others_intro9 with dissolve
else:
    scene ep9_ending_others34 with dissolve
$ renpy.pause()
if ep9_tiffani_gina_tara:
    scene ep10_others_intro10 with dissolve
else:
    scene ep10_others_intro23 with dissolve
dikcs "She fucked a DIK! He came real quick! And now she does the walk!"

scene ep10_others_intro11 with dissolve
tm "THREE GIRLS!?"
if ep9_tiffani_gina_tara:
    scene ep10_others_intro12 with dissolve
else:
    scene ep10_others_intro23 with dissolve
mc "Huh?"
if ep9_tiffani_gina_tara:
    le "Bro! Details!"
    mc "Oh, that. Nothing happened."
    scene ep10_others_intro13 with dissolve
    tm "Nothing happened, my ass. This is Tiffani's."
    scene ep10_others_intro14 with dissolve
    mc "I swear, I just slept next to them."
    scene ep10_others_intro15 with dissolve
    tm "Who has a foursome and lies about it?"
    tm "I feel like I... I don't even know you."
    scene ep10_others_intro16 with dissolve
    mc "Believe what you want, but I didn't fuck them."
    scene ep10_others_intro17 with dissolve
    le "Tell me about it later."
    scene ep10_others_intro18 with dissolve
    mc "There's nothing to tell you. I came in here and they were in my bed and I got in it with them."
    scene ep10_others_intro19 with dissolve
    le "You didn't try to fuck them?"
    scene ep10_others_intro18 with dissolve
    if affinity == "DIK":
        mc "Of course, I tried. But they were half-asleep and Tara went on about her boyfriend when I asked."
        scene ep10_others_intro19 with dissolve
        le "Yeah, Tara does that a lot. It sucks because I feel like I could bang her and I was this close to it at that dorm party."
        le "I had to settle for someone else that night."
        scene ep10_others_intro18 with dissolve
        mc "What a shame."
        scene ep10_others_intro20 with dissolve
        le "Maybe someday, right?"
    else:
        mc "No. I just wanted to sleep. They slept topless next to me, if that's something you want to hear."
        scene ep10_others_intro20 with dissolve
        le "Oh, damn! That's hot."
        scene ep10_others_intro18 with dissolve
        mc "Yeah, it was."
        scene ep10_others_intro20 with dissolve
        le "But hey, maybe next time, right?"
    scene ep10_others_intro18 with dissolve
    mc "Maybe. What about you? Did that costume work out for you?"
    scene ep10_others_intro21 with dissolve
    le "What do you think?"
    scene ep10_others_intro22 with dissolve
    mc "Haha, sorry."
    scene ep10_others_intro21 with dissolve
    le "Next party, I'll make up for it."
    scene ep10_others_intro22 with dissolve
    mc "That's the spirit."
else:
    tm "He's not even in here. Check the bathroom."
    scene ep10_others_intro24 with dissolve
    mc "What's going on?"
    scene ep10_others_intro25 with dissolve
    tm "Bro... What were you doing back there?"
    scene ep10_others_intro26 with dissolve
    mc "I was sleeping."
    scene ep10_others_intro25 with dissolve
    tm "You didn't fuck those girls?"
    scene ep10_others_intro26 with dissolve
    mc "Oh, them? No. They were in my bed when I went to sleep, so I had to take the couch."
    scene ep10_others_intro27 with dissolve
    tm "False alarm, bros. [name] didn't get pussy, he is one."
    scene ep10_others_intro28 with dissolve
    le "That sucks, we thought you got lucky."
    scene ep10_others_intro29 with dissolve
    mc "With three girls? Come on, who does that?"
    scene ep10_others_intro30 with dissolve
    le "A man can dream..."
    le "But I should have known you didn't when I saw Tara leave with them."
    le "Gina and Tiffani - sure, I could believe you banged them, but Tara, she's a whole other story."
    scene ep10_others_intro29 with dissolve
    mc "I take it you've tried to get with her."
    scene ep10_others_intro30 with dissolve
    le "At the dorm party, I tried. But she went on about Oscar. Blah!"
    le "I had to settle for someone else that night."
    scene ep10_others_intro29 with dissolve
    mc "What a shame."
    scene ep10_others_intro30 with dissolve
    le "Maybe someday, right?"
    scene ep10_others_intro29 with dissolve
    mc "Maybe. What about you? Did that costume work out for you?"
    scene ep10_others_intro32 with dissolve
    le "What do you think?"
    scene ep10_others_intro31 with dissolve
    mc "Haha, sorry."
    scene ep10_others_intro30 with dissolve
    le "Next party, I'll make up for it."
    scene ep10_others_intro29 with dissolve
    mc "That's the spirit."
jump ep10_dik_intro_label

label ep10_nicole_date_label:
$ renpy.sound.play("sound_effects/rain_outside.mp3", channel="sfx2", loop=True)
play sound "sound_effects/camera_shutter.mp3"
scene white
$ renpy.pause(0.5)
play music "music/ep10/date_night.mp3"
scene ep10_nicole_date0 with dissolve
$ renpy.pause()
scene ep10_nicole_date0b with dissolve
nic "What was that for?"
scene ep10_nicole_date0c with dissolve
mc "I just wanted a picture to remember tonight."
mc "(And also to prove something to Jacob.)"

$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
$ text_message_screen_list.append(["%s" % name,"Nicole says hi.",False])
$ text_message_screen_list.append(["%s" % name,"chat_jacob_pic1_ep10_thumb",False])
$ text_message_screen_list.append(["Jacob","NO FUCKING WAY! YOU'RE NOT LYING!?",True])
$ text_message_screen_list.append(["%s" % name,"Never was. mphone_emoji_cool",False])
$ mgallery_add_photo("chat_jacob_pic1_ep10_zoomed")
hide screen new_phone_screen
show screen text_message_screen
$ tmpInt += 1
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ mphone_scene_to_chat("Jacob",text_message_screen_list)
show screen new_phone_screen
scene ep10_nicole_date1 with dissolve
mc "I wanted to ask you something. Are you from here?"
scene ep10_nicole_date2 with dissolve
nic "I am. I moved away once, but I gravitated back home."
scene ep10_nicole_date3 with dissolve
mc "What made you come back?"
scene ep10_nicole_date4 with dissolve
nic "I wish I knew. I think it was that feeling of home."
nic "But my family doesn't live here anymore, so it feels like it's my town now."
scene ep10_nicole_date5 with dissolve
nic "I've thought about moving again, but I feel settled in and it would be hard to move too far away because of Marvin."
scene ep10_nicole_date6 with dissolve
mc "I can only imagine."
mc "How old is he?"
scene ep10_nicole_date5 with dissolve
nic "He turns ten next year."
scene ep10_nicole_date6 with dissolve
mc "Ten!? That's older than I thought he'd be."
scene ep10_nicole_date7 with dissolve
nic "I was young and stupid when we had him."
nic "Luke and I tried our best but eventually realized we were better off without each other."
scene ep10_nicole_date8 with dissolve
nic "Raising a kid when you're young... It's hard."
scene ep10_nicole_date9 with dissolve
mc "I just pictured myself getting some girl pregnant now and that would be me in your shoes next year."
scene ep10_nicole_date7 with dissolve
nic "And how does that make you feel to think about?"
scene ep10_nicole_date9 with dissolve
mc "I'm so not there yet. Like... No way."
mc "I just moved out. I'm not ready to raise a kid. I need to get myself some education and a job first."
mc "And even then, I'd have to think if I want one."
scene ep10_nicole_date7 with dissolve
nic "The money problem is hard to solve. We relied on Luke's parents a lot during the first few years."
scene ep10_nicole_date9 with dissolve
mc "That must have been tough."
scene ep10_nicole_date7 with dissolve
nic "Yes, but the toughest part was when Luke and I finally split up."
nic "I had to find a way to provide for me and Marvin, and I had no one to rely on."
scene ep10_nicole_date10 with dissolve
mc "No parents?"
scene ep10_nicole_date7 with dissolve
nic "I wish, but I don't have the best relationship with them. I couldn't ask them for money or help with him."
scene ep10_nicole_date9 with dissolve
mc "So, what did you end up doing?"
scene ep10_nicole_date4 with dissolve
nic "You know what I ended up doing."
scene ep10_nicole_date11 with dissolve
mc "Oh..."
scene ep10_nicole_date12 with dissolve
nic "I felt ashamed about it for a long time."
nic "But you tell me how an uneducated 23-year-old single mom can get a well-paying job because I couldn't figure it out."
scene ep10_nicole_date11 with dissolve
mc "..."
mc "But do you like doing it?"
scene ep10_nicole_date12 with dissolve
nic "At first, I hated it. But I had to because it was my best option."
nic "Then, after a while, you get used to it. It becomes like any other job, I guess."
scene ep10_nicole_date13 with dissolve
nic "You grow thick skin fast because you have to. It's the only way to survive in that business."
nic "Horny and drunk men can be ruthless."
nic "I went to bed crying many nights..."
scene ep10_nicole_date14 with dissolve
nic "Sorry, this is getting heavy-handed for a first date."
scene ep10_nicole_date15 with dissolve
mc "I don't mind at all. I enjoy talking about feelings. I always did."
scene ep10_nicole_date16 with dissolve
$ renpy.pause()
scene ep10_nicole_date17 with dissolve
nic "I got into fights with Luke over it, too. At one point, he told me he wanted full custody and that I wasn't a fit mother."
nic "That really hurt. I was only trying my best to survive and provide, but he didn't see it."
nic "As long as Marvin doesn't know and can stay protected from it...we'll be fine."
nic "Of course, there will come a day when he'll know all about it. But I wish for it to be in the distant future."
scene ep10_nicole_date18 with dissolve
mc "You've worked in this business for a long time now. Is it still a problem for you and Luke?"
scene ep10_nicole_date17 with dissolve
nic "While it got easier for me to do my job, Luke never came to terms with it."
nic "We can stay civil in front of Marvin, but I know he's watching me with eagle eyes, in case I slip up somehow."
scene ep10_nicole_date18 with dissolve
mc "That's rough."
scene ep10_nicole_date19 with dissolve
nic "He is a great father. Perhaps, too good."
nic "Sometimes, it makes me feel like I'm a bad mother."
scene ep10_nicole_date20 with dissolve
mc "Nicole..."
mc "I didn't realize any of this."
scene ep10_nicole_date21 with dissolve
nic "How could you?"
nic "I'm not unique that way, [name]. Everyone you meet is fighting a battle you don't know anything about."
nic "That's why I always try to be kind."
nic "Do you know what I can't believe?"
scene ep10_nicole_date22 with dissolve
mc "What?"
scene ep10_nicole_date23 with dissolve
nic "That I'm having a wonderful date with a teenager I met at work."
nic "Saying it out loud makes me feel like I have truly slipped..."
nic "But I don't think that's what it is."
scene ep10_nicole_date24 with dissolve
$ renpy.pause()
scene ep10_nicole_date25 with dissolve
nic "*{i}Smack{/i}*"
scene ep10_nicole_date26 with dissolve
nic "I've talked a lot about myself tonight..."
nic "I want to hear something personal about you."
scene ep10_nicole_date27 with dissolve
mc "Well... What is there to tell?"
scene ep10_nicole_date26 with dissolve
nic "What's the best memory you have of something?"
scene ep10_nicole_date27 with dissolve
mc "My best memory?"
scene ep10_nicole_date26 with dissolve
nic "Yeah. If you think about your life fast without analyzing it too much..."
nic "...is there a moment that springs to mind that makes you feel extra good?"
scene ep10_nicole_date28 with dissolve
mc "..."
scene ep10_nicole_date29 with dissolve
mc "Yeah... I don't know why it was the first one that popped into my head just now, but it's about my dad."
scene ep10_nicole_date30 with dissolve
nic "Tell me about it."
scene ep10_nicole_date29 with dissolve
mc "So, Dad is very close to a buddy from his work, Luis."
mc "Dad helped him build a lodge up in White Creek when I was 14."
scene ep10_nicole_date31 with dissolve
mc "There was this jetty we used to sit on at night. Sometimes, we fished; sometimes, we just sat there and took it all in."
mc "The fresh air, the clucking sound of the water as it hit the boat."
mc "At night, when I'm outdoors and the air feels fresh... Like now..."
mc "It takes me back to that moment."
mc "It makes me feel...peaceful."
scene ep10_nicole_date32 with dissolve
nic "That's a wonderful memory."
scene ep10_nicole_date33 with dissolve
$ renpy.pause()
if affinity == "DIK":
    scene ep10_nicole_date34 with dissolve
    $ renpy.pause()
scene ep10_nicole_date35 with dissolve
nic "The rain seems to be getting worse."
scene ep10_nicole_date38 with dissolve
mc "Yeah. Are you freezing?"
scene ep10_nicole_date35 with dissolve
nic "A tad... Do you wanna head inside?"
scene ep10_nicole_date37 with dissolve
mc "I don't want the date to end."
scene ep10_nicole_date36 with dissolve
nic "Who said it has to end?"
nic "Let's be honest, you won't walk home in this weather."
scene ep10_nicole_date39 with dissolve
$ renpy.music.stop(channel="sfx2", fadeout=3)
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx3", loop=True, fadein=3)
nic "And if you're staying the night, why not make the most out of it?"

label ep10_nicole_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    play music "music/ep10/date_night.mp3"
    $ affinity = "CHICK"
    $ ep10_nicole_questions = [False,False,False]
    $ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx3", loop=True, fadein=3)
    $ ep6_envy_lewd = True

hide screen new_phone_screen
scene anim_envy_kiss_ep10 with dissolve
pause

scene ep10_nicole_lewd1 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd2 with dissolve
nic "Mmm... [name]... Are you going straight at it?"
mc "I'm so goddamned horny."
scene ep10_nicole_lewd3 with dissolve
nic "There's no rush, [name]. You're staying the night."
scene ep10_nicole_lewd4 with dissolve
nic "Let's take this slow and I'll show you how good it can be."
scene ep10_nicole_lewd5 with dissolve
$ renpy.pause(0.5)
scene ep10_nicole_lewd6 with dissolve
$ renpy.pause(1.0)
scene ep10_nicole_lewd7 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd8 with dissolve
nic "Come here..."
scene ep10_nicole_lewd9 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd10 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd11 with dissolve
nic "Kiss my body. Slowly."
$ tmpInt = 0
scene ep10_nicole_lewd12 with dissolve
label ep10_nicole_lewd_loop1_label:
menu:
    "Kiss her lips":
        scene ep10_nicole_lewd13 with dissolve
        $ renpy.pause()
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Kiss her neck":
        scene ep10_nicole_lewd14 with dissolve
        $ renpy.pause()
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Kiss her tits":
        scene ep10_nicole_lewd15 with dissolve
        $ renpy.pause()
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Kiss her belly":
        scene ep10_nicole_lewd16 with dissolve
        $ renpy.pause()
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Kiss her thighs":
        scene ep10_nicole_lewd17 with dissolve
        mc "*{i}Smack{/i}*"
        scene ep10_nicole_lewd18 with dissolve
        nic "*{i}Moans{/i}*"
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Kiss her feet":
        scene ep10_nicole_lewd19 with dissolve
        $ renpy.pause()
        $ tmpInt += 1
        jump ep10_nicole_lewd_loop1_label
    "Continue" if tmpInt > 2:
        $ renpy.pause(0.5)
scene ep10_nicole_lewd20 with dissolve
nic "Go on, [name]... Eat me..."

scene anim_envy_lick_ep10 with dissolve
nic "Yes, [name]. Lick me... Gently."
nic "Make me warm and moist... Prepare it for your cock."
pause
scene anim_envy_lick2_ep10 with dissolve
nic "*{i}Moans{/i}* You're so good at that... Swivel your tongue around."
pause

$ tmpBool3 = False
menu:
    "Lick asshole":
        $ tmpBool3 = True
        scene anim_envy_lick4_ep10 with dissolve
        nic "Hngn... I see what you want..."
        pause
        scene anim_envy_lick3_ep10 with dissolve
        nic "Prepare me for it and I'll let you have it tonight."
        pause
        scene ep10_nicole_lewd21 with dissolve
        nic "Mhm..."
    "Stick to vaginal":
        $ renpy.pause(0.5)

scene ep10_nicole_lewd22 with dissolve
nic "Push your cock against my lips, [name]."
scene ep10_nicole_lewd23 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd24 with dissolve
nic "*{i}Suck suck{/i}*"
scene ep10_nicole_lewd25 with dissolve
nic "Mmpfhh..."
mc "Can I go deep?"
nic "Mhm."
scene anim_envy_bj_ep10 with dissolve
mc "Let me know if I'm pushing it in too far..."
nic "*{i}Suck glug{/i}*"
mc "You have no idea how good you are at that."
pause
scene anim_envy_bj2_ep10 with dissolve
pause
scene anim_envy_bj3_ep10 with dissolve
nic "*{i}Suck suck glug glug{/i}*"
pause

scene ep10_nicole_lewd26 with dissolve
nic "*{i}Gasps{/i}* Fuck!"
scene ep10_nicole_lewd27 with dissolve
mc "So much for going \"slow\"."
scene ep10_nicole_lewd28 with dissolve
nic "Then, it's time to go a bit faster."
nic "How do you want me, [name]?"
scene ep10_nicole_lewd27 with dissolve

$ tmpInt = 0
label ep10_nicole_lewd_loop2_label:
menu:
    "Blowjob":
        scene anim_envy_bj_ep10 with dissolve
        mc "I wanna fuck your throat more."
        nic "*{i}Suck glug{/i}*"
        pause
        scene anim_envy_bj2_ep10 with dissolve
        pause
        scene anim_envy_bj3_ep10 with dissolve
        pause
        jump ep10_nicole_lewd_loop2_label
    "Missionary":
        $ tmpInt += 1
        scene anim_envy_miss_ep10 with dissolve
        mc "Damn, that's tight..."
        pause
        scene anim_envy_miss2_ep10 with dissolve
        nic "*{i}Moans{/i}* Fuck me, [name]."
        pause
        jump ep10_nicole_lewd_loop2_label
    "Doggystyle":
        $ tmpInt += 1
        scene anim_envy_doggy_ep10 with dissolve
        nic "*{i}Moans{/i}* Fuck, [name]... I want all of you."
        pause
        scene anim_envy_doggy2_ep10 with dissolve
        mc "Work it... I love watching your sexy ass slap against me like that."
        pause
        jump ep10_nicole_lewd_loop2_label
    "Doggystyle (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_envy_doggy_anal_ep10 with dissolve
        nic "Yes! God! Yes! Ahhh..."
        pause
        scene anim_envy_doggy_anal2_ep10 with dissolve
        mc "I could fuck your ass for days and not get tired of it."
        pause
        scene anim_envy_doggy_anal3_ep10 with dissolve
        nic "Haha, I don't think I've got days to spare... Let's make the most out of it now."
        pause
        scene anim_envy_doggy_anal4_ep10 with dissolve
        mc "Believe me, I am."
        pause
        jump ep10_nicole_lewd_loop2_label
    "From below (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_envy_below_ep10 with dissolve
        nic "*{i}Moans{/i}* Fuck, fuck... Ahhh!!! Yes!"
        pause
        scene anim_envy_below2_ep10 with dissolve
        pause
        jump ep10_nicole_lewd_loop2_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_envy_rev_ep10 with dissolve
        nic "You're so hot to watch while riding you."
        pause
        scene anim_envy_rev2_ep10 with dissolve
        pause
        jump ep10_nicole_lewd_loop2_label
    "Reverse cowgirl (Anal)" if tmpBool3:
        $ tmpInt += 1
        scene anim_envy_rev_anal_ep10 with dissolve
        nic "Ahh... You're so...deep..."
        pause
        scene anim_envy_rev2_anal_ep10 with dissolve
        nic "Fuck my ass, [name]."
        pause
        jump ep10_nicole_lewd_loop2_label
    "Hugging ({color=#ffffff}{size=-[persistent.scale_factor]}{font=fonts/collegiate.ttf}CHICK{/font}{/size} affinity{/color})" if affinity == "CHICK":
        $ tmpInt += 1
        scene anim_envy_hug_ep10 with dissolve
        nic "*{i}Smack{/i}* Mmm... I love how you can be gentle and still fuck me good like this."
        pause
        scene anim_envy_hug2_ep10 with dissolve
        mc "Being close to your warm body is so sexy, Nicole."
        nic "*{i}Moans{/i}* Tell me about it. I love looking into your eyes and feeling you fully penetrate me."
        pause
        jump ep10_nicole_lewd_loop2_label
    "Cum" if tmpInt > 2:
        menu:
            "On tits":
                mc "I'm gonna cum..."
                scene anim_envy_cum_ep10 with dissolve
                nic "Cum all over me, [name]. Spray your cum on my chest."
                pause
                scene anim_envy_cum2_ep10 with hpunch
                mc "Ahh!!!"
                pause
                scene ep10_nicole_lewd31 with dissolve
                $ renpy.pause()
            "Creampie":
                scene anim_envy_miss_ep10 with dissolve
                mc "I'm gonna cum..."
                nic "Cum inside of me, [name]. I want to feel you release all of it and fill me up."
                scene ep10_nicole_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_nicole_lewd29 at vpunch, cum1
                $ renpy.pause(0.5)
                scene ep10_nicole_lewd29 at vpunch, cum1
                mc "Ahh!!!"
                nic "Oh God! Yes!!! Ahhh!"
                scene ep10_nicole_lewd30 with dissolve
                nic "That's what I'm talking about... Wow..."
            "On ass":
                if tmpBool3:
                    scene anim_envy_doggy_anal4_ep10 with dissolve
                else:
                    scene anim_envy_doggy2_ep10 with dissolve
                mc "I'm cumming..."
                nic "Yes! Cum, [name]! Cum!!!"
                scene ep10_nicole_lewd32 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_nicole_lewd32 at vpunch, cum2
                $ renpy.pause(0.5)
                scene ep10_nicole_lewd32 at vpunch, cum2
                mc "Ahh!!!"
                scene ep10_nicole_lewd33 with dissolve
                mc "Your ass is so hot covered in cum."
$ guideSuggestedPage = 131
scene ep10_nicole_lewd34 with dissolve
nic "Come here, sexy."
nic "You're great in bed."
scene ep10_nicole_lewd35 with dissolve
mc "Likewise."
scene ep10_nicole_lewd34 with dissolve
nic "Do you prefer it when we're alone, or do you miss Lily?"
scene ep10_nicole_lewd35 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Lily path)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Alone is better  [m_c1][mod_choices[2]]":
        if not _in_replay:
            $ ep10_nicole_questions[0] = False
            $ dk(-1)
        mc "I'm only thinking about you now."
        scene ep10_nicole_lewd36 with dissolve
        $ renpy.pause()
    "Threesomes are nice [m_c1][mod_choices[3]]":
        if not _in_replay:
            $ dk(1)
            $ ep10_nicole_questions[0] = True
        mc "I mean, threesomes are nice. More is always better."
        scene ep10_nicole_lewd34 with dissolve
        if ep6_envy_lewd:
            nic "Haha, I guess that means you miss Sandy, too."
        else:
            nic "Haha, I can't argue with that logic."

scene ep10_nicole_lewd37 with dissolve
$ renpy.pause()
scene ep10_nicole_lewd38 with dissolve
mc "What are you thinking about?"
scene ep10_nicole_lewd39 with dissolve
nic "I was thinking..."
scene ep10_nicole_lewd37 with dissolve
nic "..."
scene ep10_nicole_lewd39 with dissolve
nic "I was thinking that I don't know what this is."
nic "Having sex with you, dating you..."
scene ep10_nicole_lewd37 with dissolve
nic "..."
scene ep10_nicole_lewd39 with dissolve
nic "What are we doing, really?"
scene ep10_nicole_lewd38 with dissolve
mc "Pretty much what you just said."
scene ep10_nicole_lewd39 with dissolve
nic "I keep thinking about where it will lead."
nic "Normally, when I date someone, I know it after one date. Or, at the very least, I have a good guess."
nic "But with you... I can't predict it."
scene ep10_nicole_lewd37 with dissolve
menu:
    "Who knows? Let's just have fun.":
        if not _in_replay:
            $ ep10_nicole_questions[1] = False
        scene ep10_nicole_lewd38 with dissolve
        mc "Who knows where things will go from here? Let's just have fun together and figure it out as we go."
        scene ep10_nicole_lewd40 with dissolve
        nic "That sounds like one way to do it."
        scene ep10_nicole_lewd38 with dissolve
        mc "Do you have any other suggestions?"
        scene ep10_nicole_lewd40 with dissolve
        nic "Nope. The only thing I feel is that I think I want you around."
    "Do you have to know it?":
        if not _in_replay:
            $ ep10_nicole_questions[1] = True
        scene ep10_nicole_lewd38 with dissolve
        mc "Do you have to know it?"
        scene ep10_nicole_lewd40 with dissolve
        nic "No. I don't have to know it."
        nic "But I think I want you around."
scene ep10_nicole_lewd37 with dissolve
menu:
    "Even if it's just about sex? [m_c1][mod_choices[3]]":
        if not _in_replay:
            $ dk(1)
            $ ep10_nicole_questions[2] = False
        scene ep10_nicole_lewd38 with dissolve
        mc "Even if it's just about sex?"
        scene ep10_nicole_lewd39 with dissolve
        nic "Is it?"
        scene ep10_nicole_lewd38 with dissolve
        mc "Not necessarily. But I don't know what this is either."
        $ renpy.music.stop(channel="sfx3", fadeout=5)
        stop music fadeout 5
        scene ep10_nicole_lewd40 with dissolve
        nic "I guess we'll have to wait and find out."
        scene ep10_nicole_lewd37 with dissolve
        $ renpy.pause()
    "I'm not going anywhere  [m_c1][mod_choices[2]]":
        if not _in_replay:
            $ dk(-1)
            $ ep10_nicole_questions[2] = True
        $ renpy.music.stop(channel="sfx3", fadeout=5)
        stop music fadeout 5
        scene ep10_nicole_lewd38 with dissolve
        mc "I'm not going anywhere."
        scene ep10_nicole_lewd41 with dissolve
        $ renpy.pause()
$ renpy.end_replay()
$ persistent.ep10_lewd_nicole = True
$ calcScenes()
show screen new_phone_screen
$ mphone_stats_add_girl_s3("envy","You had sex with Nicole during your date at her place in episode 10.")
$ new_bio("Envy", "I had an awesome date with Nicole at her place, and we talked in a way we hadn't before.")
$ new_bio("Envy", "Nicole asked me questions related to dating her, and I answered as I saw fit.")

if not persistent.ep10_card15:
    $ persistent.ep10_card15 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep10_card16:
    $ persistent.ep10_card16 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

scene ep10_nicole_lewd42 with Fade(1,1,1)
play music "music/ep8/licensed_music/track65.mp3"
nic "Wake up, [name]."
scene ep10_nicole_lewd43 with dissolve
mc "Hm? Do I have to?"
scene ep10_nicole_lewd42 with dissolve
nic "I mean this in the most non-creepy way possible..."
nic "You have school today."
scene ep10_nicole_lewd43 with dissolve
mc "Haha... Actually, I don't. It's Sunday."
scene ep10_nicole_lewd44 with dissolve
nic "Oh, wow. Haha! I'm sorry - my days kind of blend into each other."
nic "With my schedule, it's hard to separate weekdays and weekends."
scene ep10_nicole_lewd43 with dissolve
mc "Do you have to get to work?"
scene ep10_nicole_lewd42 with dissolve
nic "Tonight, yes. I'll spend the day running some errands."
scene ep10_nicole_lewd43 with dissolve
mc "That sounds...fun."
scene ep10_nicole_lewd42 with dissolve
nic "Not really. I'd rather spend the day in bed with you."
scene ep10_nicole_lewd43 with dissolve
mc "You and me, both."
scene ep10_nicole_lewd45 with dissolve
mc "At least it's not raining anymore."
scene ep10_nicole_lewd46 with dissolve
nic "*{i}Smack{/i}*"
scene ep10_nicole_lewd42 with dissolve
nic "Call me later."
scene ep10_nicole_lewd43 with dissolve
mc "Sure thing."
scene ep10_nicole_lewd47 with dissolve
mc "(Wow... What a night that was. Nicole is incredible.)"
scene ep10_nicole_lewd48 with dissolve
mc "(If only she didn't have a kid...)"
stop music fadeout 3
mc "(It won't stop me from dating her, but I can't lie... I feel weird about it.)"
jump ep10_science_label

label ep10_nora_date_label:
$ guideSuggestedPage = 131
play music "music/ep2/journey_of_hope.mp3"
if branchAlone and ep9_riona_choice == "DIK":
    scene ep10_nora_date1 with wipeleft
else:
    scene ep10_nora_date1
no "And this is the kitchen-slash-living room area."
scene ep10_nora_date2 with dissolve
mc "Very nice! Where's your TV?"
scene ep10_nora_date3 with dissolve
no "It's in another room. I prefer to relax with other activities."
scene ep10_nora_date4 with dissolve
mc "I'm not that much into TV, either. I recently got one but have barely watched it."
scene ep10_nora_date5 with dissolve
no "Now, that is refreshing to hear. We're kindred spirits, then."
scene ep10_nora_date6 with dissolve
mc "It's nice that we have more things in common than we know."
scene ep10_nora_date7 with dissolve
no "Who knows what else we might have in common?"
scene ep10_nora_date6 with dissolve
mc "Yeah. We should explore each other more."
scene ep10_nora_date8 with dissolve
no "Is that flirting?"
scene ep10_nora_date9 with dissolve
mc "Well, exploring each other can be done in different ways."
mc "But I wasn't talking about spelunking."
scene ep10_nora_date10 with dissolve
no "*{i}Snort laugh{/i}*"
no "That one went into my nose. Haha!"
mc "Do you need a tissue?"
scene ep10_nora_date11 with dissolve
no "No, thanks. I'm fine."
scene ep10_nora_date12 with dissolve
mc "This is a great apartment. I can't believe how big it is for being smack dab in the middle of the city."
mc "Do you live here alone?"
scene ep10_nora_date13 with dissolve
no "I do have a roommate."
scene ep10_nora_date6 with dissolve
mc "Oh?"
scene ep10_nora_date7 with dissolve
no "Perhaps you'd like to meet her?"
scene ep10_nora_date6 with dissolve
mc "Sure. Uh... Is she here right now?"
scene ep10_nora_date14 with dissolve
no "Fluffy!"
play sound "sound_effects/season3/cat_meow1.mp3"
scene ep10_nora_date15 with dissolve
no "There she is."
mc "Oh! You have a cat!"
scene ep10_nora_date16 with dissolve
play sound "sound_effects/season3/cat_meow2.mp3"
no "I do. Do you like cats?"
mc "I don't dislike them, but I'm not around them much."
scene ep10_nora_date17 with dissolve
no "Fluffy's my little princess. She always picks me up when I'm feeling low."
scene ep10_nora_date18 with dissolve
mc "I can imagine."
mc "Hi there, Fluffy."
play sound "sound_effects/season3/cat_hiss.mp3"
scene ep10_nora_date19 with dissolve
fl "*{i}Hisses{/i}*"
scene ep10_nora_date20 with dissolve
mc "Oh... Doesn't she like strangers?"
scene ep10_nora_date21 with dissolve
no "She usually does. But I've noticed her having issues with males in the past."
no "Give it time and I'm sure you two will get along."
scene ep10_nora_date22 with dissolve
mc "I've got plenty of time for it."
scene ep10_nora_date23 with dissolve
no "Let's sit down for a while."
play sound "sound_effects/season3/cat_meow1.mp3"
scene ep10_nora_date24 with dissolve
$ renpy.pause()
play sound "sound_effects/season3/cat_hiss.mp3"
scene ep10_nora_date25 with dissolve
fl "*{i}Hisses{/i}*"
scene ep10_nora_date26 with dissolve
mc "(Am I getting cockblocked by a cat now?)"
scene ep10_nora_date27 with dissolve
no "I gotta say it's nice to meet you while not being a sweaty mess."
scene ep10_nora_date28 with dissolve
mc "I like running into you at the gym, but I agree. It's nice to see that you wear normal clothes, too."
mc "You're pretty when you're not sweating."
scene ep10_nora_date27 with dissolve
no "I'm pretty when I'm sweating, too."
scene ep10_nora_date28 with dissolve
mc "Yeah, of course!"
mc "So, what do you do when you're not sweating?"
scene ep10_nora_date29 with dissolve
no "I spend a lot of my free time on my art. I love the creative process and I've been focusing on paintings for the last couple of years."
scene ep10_nora_date30 with dissolve
mc "That's cool! A friend of mine paints. I'm always amazed at how people can do that."
mc "I can draw stick figures, but that's about it."
scene ep10_nora_date31 with dissolve
no "Haha, we all have to start somewhere. And even I start with basic shapes when I draw."
scene ep10_nora_date30 with dissolve
mc "You'll have to show me your paintings."
scene ep10_nora_date31 with dissolve
no "Absolutely."
scene ep10_nora_date30 with dissolve
mc "What about when you're not free? What's your profession?"
scene ep10_nora_date32 with dissolve
no "I'm a scientist. I've got a Ph.D. in biochemistry and I'm currently doing my second year of postdoctoral studies."
scene ep10_nora_date30 with dissolve
mc "Science? No way! I like science too."
scene ep10_nora_date33 with dissolve
no "You do?"
scene ep10_nora_date30 with dissolve
mc "I do. Is it fun being a scientist?"
scene ep10_nora_date32 with dissolve
no "It is stimulating to the mind, yes."
no "You get to focus on a few projects, sometimes for years, before moving on to something new."
no "It allows you to become an expert at something and dig deep into the field."
scene ep10_nora_date30 with dissolve
mc "Sounds cool. What are you working on? Are you allowed to say?"
scene ep10_nora_date32 with dissolve
no "I'm developing and improving methods of chromatography."
scene ep10_nora_date30 with dissolve
mc "That...tells me nothing."
scene ep10_nora_date29 with dissolve
no "I'd love to tell you about it, but if you get me started on this topic, that will be all there is for us tonight."
scene ep10_nora_date30 with dissolve
mc "Haha! It sounds like you're passionate about it."
scene ep10_nora_date31 with dissolve
no "Indeed."
no "What about you, [name]? What are you passionate about?"
scene ep10_nora_date30 with dissolve
mc "I'd say my biggest passion is my music. I play the acoustic guitar."
scene ep10_nora_date34 with dissolve
no "Well, aren't you dreamy?"
scene ep10_nora_date35 with dissolve
mc "I'd play for you if I had brought it with me."
scene ep10_nora_date34 with dissolve
no "I'm sure there will be another chance for it."
scene ep10_nora_date35 with dissolve
mc "Are you that sure?"
scene ep10_nora_date31 with dissolve
no "I feel that we mix well thus far. We have good chemistry, pardon the puns."
no "I feel fairly certain that there will be at least another date. Wouldn't you agree?"
scene ep10_nora_date30 with dissolve
mc "Totally! I want to learn more about you."
mc "But I gotta say... I initially thought this would be weird, considering that we're quite different at a glance..."
mc "...but I'm happy we're alike in some areas."
scene ep10_nora_date36 with dissolve
no "Hm... Let's find out how alike we are."
scene ep10_nora_date37 with dissolve
no "Take these."
mc "What do I do with them?"
scene ep10_nora_date38 with dissolve
no "Let's take turns asking questions we must answer with either yes or no at the same time."
no "This way, we'll find out if we're that alike."
scene ep10_nora_date39 with dissolve
mc "I love games like this. Let's do it."
scene ep10_nora_date40 with dissolve
no "I'll start us off easily."
no "I love listening to music. Yes or no?"
scene ep10_nora_date43 with dissolve
mc "Well, obviously."
scene ep10_nora_date41 with dissolve
no "Me too. Now, you go."
scene ep10_nora_date39 with dissolve
mc "Hm... Cats are better than dogs. Yes or no?"
scene ep10_nora_date42 with dissolve
mc "Not surprising."
scene ep10_nora_date44 with dissolve
no "But yours is. Care to elaborate?"
scene ep10_nora_date45 with dissolve
mc "I've been around more dogs than cats. I think that's why."
mc "Dogs show so much more emotions than cats."
scene ep10_nora_date40 with dissolve
no "If you'd been around cats more, you'd know that's not true."
no "Cats have personalities and their way of showing emotions, but you have to learn their patterns and earn their trust."
scene ep10_nora_date39 with dissolve
mc "I'll take your word for it."
scene ep10_nora_date40 with dissolve
no "Looks are very important in a relationship to me. Yes or no?"
scene ep10_nora_date39 with dissolve
menu:
    "Yes  [m_c1][mod_choices[3]]":
        $ dk(1)
        scene ep10_nora_date43 with dissolve
        mc "Of course!"
        scene ep10_nora_date46 with dissolve
        mc "What? You went with no?"
        scene ep10_nora_date47 with dissolve
        no "They aren't very important. Sure, it's nice to have something pretty to look at, but why bother if there's no substance behind the exterior?"
        scene ep10_nora_date39 with dissolve
        mc "Sure, but if you don't like what you're looking at, there's no way that substance will make up for it romantically."
        scene ep10_nora_date40 with dissolve
        no "Looks will fade with time, [name]."
        scene ep10_nora_date39 with dissolve
        mc "Yeah, I know. But I don't think it would move past a friendship if I wasn't attracted to my date."
        scene ep10_nora_date40 with dissolve
        no "I see. Well, I agree to some extent. But looks aren't {b}very{/b} important to me, and that was the question."
    "No [m_c1][mod_choices[2]]":
        $ dk(-1)
        scene ep10_nora_date45 with dissolve
        mc "I'm gonna say no. They aren't very important, but it doesn't hurt if you got them."
        scene ep10_nora_date47 with dissolve
        no "We seem to agree on this one, too. Are you just answering what you think will please me, or are you being honest?"
        scene ep10_nora_date39 with dissolve
        mc "I'm being honest. Sure, it's nice to date someone as attractive as yourself, but if the talks are boring and you don't connect, looks won't matter in the long run."
        scene ep10_nora_date40 with dissolve
        no "We think the same about this. Color me impressed."
scene ep10_nora_date39 with dissolve
mc "I'll take it up a notch..."
mc "Sex is important in a relationship. Yes or no?"
scene ep10_nora_date48 with dissolve
no "That's a leading question, isn't it?"
scene ep10_nora_date43 with dissolve
mc "Well, my answer is yes. But I'm curious what you think."
scene ep10_nora_date41 with dissolve
no "Of course, it is important."
scene ep10_nora_date39 with dissolve
mc "Haha! Good."
scene ep10_nora_date48 with dissolve
no "That's the biggest smile from you yet."
scene ep10_nora_date49 with dissolve
mc "You too."
scene ep10_nora_date50 with dissolve
$ renpy.pause()
scene ep10_nora_date51 with dissolve
no "..."
scene ep10_nora_date52 with dissolve
no "I want kids in the future. Yes or no?"
scene ep10_nora_date51 with dissolve
mc "That's a big question."
$ guideSuggestedPage = 132
scene ep10_nora_date52 with dissolve
no "You dialed it up, didn't you? Dare to answer it?"
scene ep10_nora_date51 with dissolve
menu:
    "[mod_gr]I think I want kids":
        $ ep10_nora_kids = True
        scene ep10_nora_date43 with dissolve
        mc "I think I want kids in the future."
        mc "I haven't thought about it much since it's not something I see in the near future, but I'm not against it."
        scene ep10_nora_date52 with dissolve
        no "That's good to know."
        scene ep10_nora_date51 with dissolve
        mc "You haven't shown me your sign."
        scene ep10_nora_date53 with dissolve
        no "Yes, I absolutely do."
        scene ep10_nora_date54 with dissolve
        mc "That's a strong yes."
    "No, I don't want kids":
        $ ep10_nora_kids = False
        scene ep10_nora_date45 with dissolve
        mc "I don't think I want kids in the future."
        mc "I haven't thought about it much since it's not something I see in the near future..."
        mc "But my gut feeling is telling me that I don't want kids. I think I want to focus on myself first and see what happens."
        scene ep10_nora_date52 with dissolve
        no "It isn't an emphatic no, I hear."
        scene ep10_nora_date51 with dissolve
        mc "Everyone can change their mind in time, but at the moment, I'm leaning toward no."
        scene ep10_nora_date53 with dissolve
        no "That's unfortunate. We're not alike when it comes to this."
        scene ep10_nora_date54 with dissolve
        mc "Ah... I figured. It was a leading question from you, too, wasn't it?"
scene ep10_nora_date52 with dissolve
no "I've always known I wanted kids."
no "It's a social convention that you don't ask about having kids during a first date, but it's important to me. I figured, why waste my time not asking?"
scene ep10_nora_date51 with dissolve
mc "It's not something you put in your dating profile, I guess."
scene ep10_nora_date55 with dissolve
no "Being honest about private things too early will have you come off too strong."
scene ep10_nora_date56 with dissolve
mc "Scared off guys by doing it, or what?"
no "..."
mc "Sorry... That was a joke."
scene ep10_nora_date55 with dissolve
no "It's ok. I know."
no "It's just that the short answer to that question would be yes."
scene ep10_nora_date56 with dissolve
mc "Ah, damn... Now I feel like a dick."
scene ep10_nora_date55 with dissolve
no "Please, don't. I'm having a good time with you."
no "I brought that one on myself."
if ep10_nora_kids:
    scene ep10_nora_date56 with dissolve
    mc "You won't scare me off with it if that's comforting to hear."
    scene ep10_nora_date57 with dissolve
    no "It certainly is. I'm enjoying your company."
    no "Despite our age difference, we've found a lot of common ground."
    no "We may be at different stages of our lives, but we have a shared outlook on the future."
    no "And you're fun to be around, and the truth is that I could need someone like you around me. You're a pleasant and welcomed distraction."
    scene ep10_nora_date58 with dissolve
    mc "I never knew I could use someone like you, either. I've found this date refreshing."
else:
    scene ep10_nora_date56 with dissolve
    mc "Since we don't see eye to eye on that big question..."
    mc "The question that came to mind immediately was whether you are still interested in dating me or feel like I am wasting your time."
    scene ep10_nora_date55 with dissolve
    no "I appreciate you not beating around the bush with it and neither will I."
    no "I honestly don't feel like I'm wasting my time since I'm enjoying your company."
    no "Despite our age difference, we've found some common ground."
    scene ep10_nora_date57 with dissolve
    no "Yes, we want different things for our future, but at the moment, I could need someone like you around me. You're a pleasant and welcomed distraction."
    no "I don't think it's a waste of time at all. I believe this is a life experience for both of us that will be memorable regardless of its outcome."
    scene ep10_nora_date58 with dissolve
    mc "Great! I agree. Let's see what happens."

scene ep10_nora_date57 with dissolve
no "This conversation got pretty heavy for a first date and an innocent game. How about if I show you some of my art to take the edge off?"
scene ep10_nora_date58 with dissolve
mc "Yes, I want to see it, for sure."
scene ep10_nora_date57 with dissolve
no "Follow me."

scene ep10_nora_date59 with dissolve
mc "Did you make these?"
scene ep10_nora_date60 with dissolve
no "Yes, I did. I have been dabbling with abstract art lately, but before that, I made plenty of portraits and landscape paintings."
scene ep10_nora_date61 with dissolve
mc "You're very gifted."
scene ep10_nora_date62 with dissolve
no "Thank you, [name]. I can assure you it's not a gift. It's countless hours of practice with pencils and brushes."
no "I'm sure you've made a similar journey with your guitar."
scene ep10_nora_date61 with dissolve
mc "Oh, tell me about it. I've worked through the callouses and fat fingers to get to where I am."
mc "I can still improve, but I feel rather confident about my music."
scene ep10_nora_date62 with dissolve
no "Do you write songs of your own?"
scene ep10_nora_date61 with dissolve
mc "I do. Like you, the creation of something is an amazing feeling. I get lost in the music when I play."
scene ep10_nora_date62 with dissolve
no "It's exactly how you describe it. I get lost in my paintings too. An entire afternoon can pass in the blink of an eye in this room."
no "You'll have to try it with me sometime."
scene ep10_nora_date61 with dissolve
mc "If you teach me how to do it, sure."
scene ep10_nora_date62 with dissolve
no "Will you excuse me for a moment? I'll be right back."
scene ep10_nora_date63 with dissolve
mc "(This date is going great!)"
mc "(I can't believe it.)"
scene ep10_nora_date64 with dissolve
mc "(I'm absolutely clicking with this hot and mature chick...)"
mc "(But boy, I'm struggling to keep up with her. It feels like I'm trying too hard to impress her...)"
mc "(I guess I want her to like me that badly.)"
scene ep10_nora_date65 with dissolve
mc "(These paintings are something else. She could sell these. Maybe she is?)"
no "[name]?"
scene ep10_nora_date66 with dissolve
mc "There you are."
scene ep10_nora_date67 with dissolve
no "This night seems to fly by fast."
scene ep10_nora_date68 with dissolve
mc "Yeah, it does."
scene ep10_nora_date69 with dissolve
no "*{i}Smack{/i}*"
scene ep10_nora_date70 with dissolve
no "Sadly, I need to get up early tomorrow."
scene ep10_nora_date71 with dissolve
mc "Oh? That's ok. I understand. If you have to go to bed, I'll get going."
scene ep10_nora_date70 with dissolve
no "Not quite yet. I need to get to bed early, but I was wondering if we could spend the remainder of the evening in my bedroom before that?"
mc "(Blood is fucking rushing to my dick right now...)"
no "I'll take your silence as a yes."
scene ep10_nora_date71 with dissolve
mc "I left my \"yes paper\" on the couch, but yes!"
scene ep10_nora_date70 with dissolve
no "Perfect."
scene ep10_nora_date72 with dissolve
stop music fadeout 3
mc "You weren't lying in your profile... You are straightforward."
no "Sweet of you to remember."

label ep10_nora_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
hide screen new_phone_screen
$ ep10_nora_lewd = True
play music "music/ep6/licensed_music/track34.mp3"
scene ep10_nora_lewd1 with dissolve
no "*{i}Smack{/i}*"
scene ep10_nora_lewd2 with dissolve
$ renpy.pause()
scene ep10_nora_lewd3 with dissolve
$ renpy.pause()
scene ep10_nora_lewd4 with dissolve
$ renpy.pause()
scene ep10_nora_lewd5 with dissolve
mc "I love your ass..."
scene bg anim_nora_slap_ep10 movie with dissolve
pause
scene ep10_nora_lewd6 with dissolve
no "Are you going to remove your clothes or what?"
scene ep10_nora_lewd7 with dissolve
mc "Yes, ma'am."
scene ep10_nora_lewd8 with dissolve
no "Nuh-uh. Don't ma'am, me."
scene ep10_nora_lewd9 with dissolve
mc "What would you like me to call you, then?"
scene ep10_nora_lewd10 with dissolve
no "..."
scene ep10_nora_lewd11 with dissolve
no "Can I be your bad kitty tonight?"
scene ep10_nora_lewd12 with dissolve
mc "My bad kitty, eh?"
scene ep10_nora_lewd13 with dissolve
no "It doesn't sound as old as ma'am."
mc "It does sound young. And you are young, just a bit older than me."
scene ep10_nora_lewd14 with dissolve
no "Smooth talker, you."
scene ep10_nora_lewd15 with dissolve
no "Come to Kitty... Put it in there."
scene anim_nora_boobjob1_ep10 with dissolve
mc "Damn... That's so hot, Nora...Kitty."
no "Mmm... Kitty wants it bad."
mc "I love your soft tits. That bra makes them look amazing."
pause
scene anim_nora_boobjob2_ep10 with dissolve
no "Your enormous cock is perfect between my tits."
no "Let me massage it for you."
mc "Yeah, do it."
pause
scene anim_nora_boobjob3_ep10 with dissolve
no "Yes. Fuck my tits, [name]. Kitty needs it bad..."
mc "I've never done this before."
pause
scene anim_nora_boobjob3b_ep10 with dissolve
no "Most girls can't do this, I'm sure."
mc "Definitely not. Fuck... It feels so good."
pause
scene ep10_nora_lewd16 with dissolve
mc "You're not even undressed and I'm still having the time of my life with you."
scene ep10_nora_lewd17 with dissolve
no "Put your cock between my thighs, [name]."
scene ep10_nora_lewd18 with dissolve
no "Rub against me."
scene anim_nora_rub_ep10 with dissolve
mc "God...everything is so soft... That friction between your thighs and the soft feeling of your panties against my cock can make me explode."
pause
scene anim_nora_rub2_ep10 with dissolve
no "You're not exploding anytime soon, [name]. I want you to get nice and hard for Kitty."
mc "Oh, I will."
pause
scene ep10_nora_lewd19 with dissolve
no "Then it's time for me to taste you."
scene ep10_nora_lewd20 with dissolve
mc "You're spoiling me."
scene anim_nora_bj1_ep10 with dissolve
mc "Such a naughty Kitty. Suck my cock."
no "Mmphff... *{i}Suck suck{/i}*"
pause
scene anim_nora_bj2_ep10 with dissolve
mc "Take my cock, Kitty. I wanna watch you gag on it."
pause
scene ep10_nora_lewd21 with hpunch
no "*{i}Gags{/i}*"
mc "Fuck, yes! Like that!"
scene ep10_nora_lewd22 with dissolve
no "*{i}Coughs{/i}*"
no "Did I do good?"
scene anim_nora_bj3_ep10 with dissolve
mc "Yeah, Kitty's doing great."
pause
scene anim_nora_bj3b_ep10 with dissolve
no "*{i}Lick lick{/i}*"
pause

scene ep10_nora_lewd23 with dissolve
mc "Yeah, show me those big beautiful tits of yours."
scene ep10_nora_lewd24 with dissolve
mc "Mmm... I wanna fuck those tits again."
scene anim_nora_boobjob4_ep10 with dissolve
mc "I could fuck your tits for hours..."
pause
scene anim_nora_boobjob5_ep10 with dissolve
mc "But I gotta say, I'm tempted to check what's hiding behind those sexy panties."
pause
scene ep10_nora_lewd25 with dissolve
no "Let me introduce you, [name]."
scene ep10_nora_lewd26 with dissolve
mc "Oh fuck... I wanna lick it."
scene ep10_nora_lewd27 with dissolve
no "Mmphff..."
scene anim_nora_lick_ep10 with dissolve
mc "*{i}Lick lick{/i}*"
no "*{i}Muffled{/i}* Yes! *{i}Moans{/i}* Lap Kitty... Kitty needs your tongue..."
pause
scene anim_nora_lick2_ep10 with dissolve
no "*{i}Moans{/i}*"
pause

scene ep10_nora_lewd28 with dissolve
no "*{i}Muffled{/i}* I wanna taste it."
menu:
    "Kiss her":
        scene ep10_nora_lewd30 with dissolve
        no "Mmm..."
    "Spit in her mouth":
        scene ep10_nora_lewd29 with dissolve
        mc "*{i}Spits{/i}*"
        scene ep10_nora_lewd30 with dissolve
        no "Mmm..."

scene ep10_nora_lewd31 with dissolve
no "Do you want me, [name]?"
scene ep10_nora_lewd32 with dissolve
mc "With an ass like that, who wouldn't?"
no "Oh? You want my ass?"
no "No. Not tonight."
scene ep10_nora_lewd33 with dissolve
mc "I didn't mean anal when I said I wanted your ass."
scene ep10_nora_lewd34 with dissolve
no "Oh? What would you do to it then?"
mc "Maybe I could get a nice assjob from it?"
scene ep10_nora_lewd35 with dissolve
mc "Squeeze your cheeks together for me."
scene anim_nora_assjob_ep10 with dissolve
mc "Yes! Like that. Damn..."
mc "Just like your tits gave the perfect boobjob, your ass gives a great assjob."
no "Haha! I'm glad."
pause
scene anim_nora_assjob2_ep10 with dissolve
no "[name]... Kitty wants your cock now..."
mc "Do you now?"
no "Mhm... Kitty craves it."
pause

scene ep10_nora_lewd36 with dissolve
$ renpy.pause()
scene ep10_nora_lewd37 with dissolve
mc "As Kitty wishes..."
scene bg anim_nora_insert_ep10 movie with dissolve
no "*{i}Gasps moans{/i}*"
no "*{i}Moans{/i}* Fuck! I thought the cock would never end. It kept going deeper and deeper inside of me."
scene anim_nora_prone1_ep10 with dissolve
mc "Now it's your turn to get it. I'm gonna punish you with my cock."
no "Yes, punish me! I've been so bad!"
mc "Yeah? What have you done that deserves punishment?"
scene anim_nora_prone2_ep10 with dissolve
no "Kitty's been eyeing your cock and ass whenever you looked another way. And she feels no shame for doing it, either."
mc "Haha! Wow! Really?"
mc "Since we're being honest, I've been eyeing your hot body, too."
no "I know. I've seen you checking me out a lot at the gym."
mc "(Fuck. Am I that bad at sneaking peeks?)"
mc "I'm gonna punish you for looking."
no "*{i}Moans{/i}* Yes! Do it!"
pause

$ tmpInt = 0
$ tmpBool3 = False
label ep10_nora_lewd_loop_label:
menu:
    "Prone":
        $ tmpInt += 1
        scene anim_nora_prone1_ep10 with dissolve
        pause
        scene anim_nora_prone2_ep10 with dissolve
        pause
        jump ep10_nora_lewd_loop_label
    "Sideways":
        $ tmpInt += 1
        scene anim_nora_side1_ep10 with dissolve
        pause
        scene anim_nora_side2_ep10 with dissolve
        pause
        jump ep10_nora_lewd_loop_label
    "Standing":
        $ tmpInt += 1
        scene anim_nora_stand1_ep10 with dissolve
        no "Fuck me, [name]... Yes! God!"
        pause
        scene anim_nora_stand2_ep10 with dissolve
        mc "Your pussy feels amazing and tight, Nora."
        pause
        scene anim_nora_stand3_ep10 with dissolve
        pause
        jump ep10_nora_lewd_loop_label
    "Reverse cowgirl":
        $ tmpInt += 1
        scene anim_nora_rev1_ep10 with dissolve
        no "Hngn... Let me give it to you..."
        pause
        jump ep10_nora_lewd_loop_label
    "From behind":
        $ tmpInt += 1
        if not tmpBool3:
            scene ep10_nora_lewd40 with dissolve
            mc "Fluffy... Scram."
            play sound "sound_effects/season3/cat_hiss.mp3"
            scene ep10_nora_lewd41 with dissolve
            fl "*{i}Hisses{/i}*"
            scene ep10_nora_lewd39 with dissolve
            no "Ignore her. She's not here."
            $ tmpBool3 = True
        scene anim_nora_doggy1_ep10 with dissolve
        no "Yes! Harder... Fuck me..."
        pause
        scene anim_nora_doggy2_ep10 with dissolve
        mc "Fuck... This feels too good."
        no "*{i}Moans{/i}* Yes! Harder!"
        pause
        jump ep10_nora_lewd_loop_label
    "Cowgirl":
        $ tmpInt += 1
        scene anim_nora_ride1_ep10 with dissolve
        pause
        scene anim_nora_ride2_ep10 with dissolve
        pause
        jump ep10_nora_lewd_loop_label
    "Cum" if tmpInt > 2 and tmpBool3:
        menu:
            "Doggystyle":
                scene anim_nora_doggy1_ep10 with hpunch
                mc "Ah!!! I'm cumming!"
                no "Yes! Cum inside of me! Cum!!!"
                scene bg anim_nora_cum1_ep10 movie with dissolve
                mc "Nora... Fuck! That was so good."
                pause
            "Cowgirl":
                scene anim_nora_ride1_ep10 with dissolve
                mc "I'm gonna cum!"
                no "Yes! Cum inside of me! Cum!!!"
                pause
                scene anim_nora_cum2_ep10 with vpunch
                mc "Ahhh!!! Fuck!"
                no "Yes! CUM! I can feel it!"
                pause
                scene ep10_nora_lewd38 with dissolve
                mc "Nora... Fuck! That was so good."


scene ep10_nora_lewd42 with dissolve
no "*{i}Breathes heavily{/i}*"
no "God... I haven't been fucked like that in years...if ever."
scene ep10_nora_lewd43 with dissolve
mc "You needed it, huh?"
scene ep10_nora_lewd42 with dissolve
no "Desperately..."
scene ep10_nora_lewd44 with dissolve
no "I hope I'm not rude for asking you to leave after using your cock like this."
scene ep10_nora_lewd45 with dissolve
mc "Not at all. You laid the grounds early. You have an early morning."
scene ep10_nora_lewd44 with dissolve
no "Thanks..."
no "*{i}Phew{/i}* Can I go clean up?"
stop music fadeout 5
scene ep10_nora_lewd45 with dissolve
mc "Be my guest. I need to catch my breath."

$ renpy.end_replay()
$ persistent.ep10_lewd_nora = True
$ calcScenes()
$ mphone_stats_add_girl_s3("nora","You had sex with Nora during your date at her place in episode 10.")
show screen new_phone_screen
if not persistent.ep10_card9:
    $ persistent.ep10_card9 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()
if not persistent.ep10_card10:
    $ persistent.ep10_card10 = True
    $ persistent.rew_2d_unlocked += 1
    $ persistent.chat_new_rewards = True
    $ calcRenders()

$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx3", loop=True)
scene ep10_nora_lewd46 with dissolve
mc "(Wow... My balls are drained...)"
play sound "sound_effects/season3/cat_hiss.mp3"
scene ep10_nora_lewd47 with vpunch
play music "music/ep10/faked_reality.mp3"
mc "Ow!"
scene ep10_nora_lewd48 with dissolve
mc "Hey! You little...fucker."
mc "Stop ruining my night."
play sound "sound_effects/season3/cat_hiss.mp3"
fl "*{i}Hisses{/i}*"
scene ep10_nora_lewd49 with vpunch
mc "Ow!"
scene ep10_nora_lewd50 with dissolve
mc "That's it. Get out of here!"
scene ep10_nora_lewd51 with dissolve
mc "Yeah, and stay there."
scene ep10_nora_lewd52 with dissolve
mc "Oh no..."
scene ep10_nora_lewd53 with dissolve
$ renpy.pause()
scene ep10_nora_lewd56 with dissolve
mc "*{i}Gentle voice{/i}* Um... Fluffy? Come here."
scene ep10_nora_lewd54 with dissolve
mc "Don't touch that glass."
play sound "sound_effects/season3/glass_push.mp3"
scene ep10_nora_lewd55 with dissolve
$ renpy.pause()
scene ep10_nora_lewd57 with dissolve
mc "Don't!"
play sound "sound_effects/season3/glass_push.mp3"
scene bg anim_fluffy_ep10 movie with dissolve
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/season2/mug.mp3", channel="sfx1", loop=False)
$ renpy.sound.play("sound_effects/season2/drink_splash.mp3", channel="sfx2", loop=False)
$ renpy.pause(1.5)
scene ep10_nora_lewd58 with hpunch
play sound "sound_effects/season3/cat_meow1.mp3"
mc "No!!!"
mc "Fuck! Fluffy! What did you just do!?"
scene ep10_nora_lewd59 with dissolve
mc "No, no, no... Dammit!"
no "[name]? *{i}Gasps{/i}*"
stop music fadeout 5
scene ep10_nora_lewd60 with dissolve
no "My paintings! What did you do?"
mc "It wasn't me! It was an accident! It was Fluffy!"
scene ep10_nora_lewd61 with dissolve
no "Fluffy?"
scene ep10_nora_lewd62 with dissolve
$ renpy.pause()
scene ep10_nora_lewd63 with dissolve
mc "I swear, it was! I chased her in here and she pushed my glass from that box."
scene ep10_nora_lewd64 with dissolve
no "..."
no "They are ruined..."
scene ep10_nora_lewd65 with dissolve
mc "Fuck, I'm so sorry."
scene ep10_nora_lewd66 with dissolve
no "Damn it... I loved these paintings."
no "*{i}Sigh{/i}* Please, don't put any more drinks near my paintings in the future."
scene ep10_nora_lewd65 with dissolve
mc "It wasn't me...it... Yeah, that one is my fault, but Fluffy..."
mc "*{i}Sigh{/i}*"
$ renpy.music.stop(channel="sfx3", fadeout=3)
scene ep10_nora_lewd62 with dissolve
mc "(That fucking cat!)"




if branchIsabella:
    jump ep10_bella_solo_label    


    
if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label


jump ep10_science_label

label ep10_rio_solo_label:
$ guideSuggestedPage = 130
scene ep10_rio_solo58a with wipeleft
$ renpy.pause()
play sound "sound_effects/season2/beachball.mp3"
scene ep10_rio_solo58 with vpunch
le "Damn! But that's a new record, right?"
scene ep10_rio_solo59 with dissolve
if persistent.basket_score[0][0] == "Jacob":
    jac "It's not. I've still got all of you beat."
else:
    jac "It's not. [name] still holds it."
    scene ep10_rio_solo60 with dissolve
    mc "Damn straight."
scene ep10_rio_solo61 with dissolve
ri "It won't be long until you're on top. You looked sexy shooting those shots."
scene ep10_rio_solo62 with dissolve
mc "(She's doing it again... But now it's with Leon...)"
scene ep10_rio_solo63 with dissolve
mc "I see what you're doing."
scene ep10_rio_solo64 with dissolve
ri "It's about time."
scene ep10_rio_solo63 with dissolve
mc "Are you trying to make me jealous?"
scene ep10_rio_solo64 with dissolve
ri "Is it working?"
scene ep10_rio_solo63 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Lily path)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Yeah [m_c1][mod_choices[2]]":
        $ dk(-1)
        mc "Yeah."
        scene ep10_rio_solo65 with dissolve
        ri "Haha! Wait! No way?"
    "Nope  [m_c1][mod_choices[3]]":
        $ dk(1)
        mc "Nope."
        scene ep10_rio_solo65 with dissolve
        ri "Wait! Come on. It has to be working a bit."
scene ep10_rio_solo66 with dissolve
mc "This isn't what I meant with what I said at Halloween."
scene ep10_rio_solo65 with dissolve
ri "I thought you wanted me to be hard to get."
scene ep10_rio_solo66 with dissolve
mc "You got this from that?"
scene ep10_rio_solo67 with dissolve
ri "Hey, why not? I'm free today and I'm bored."
scene ep10_rio_solo68 with dissolve
mc "You gave Leon false hope."
scene ep10_rio_solo67 with dissolve
ri "No, I didn't. I boosted his confidence. And after Halloween, he definitely needed it."
scene ep10_rio_solo68 with dissolve

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Riona date)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "Spend time with Rio [m_c2][mod_choices[0]]":
        $ ep10_riona_date = True
        mc "You're free today, huh? What are the rest of you doing?"
    "Don't spend time with Rio [m_c1][mod_choices[3]]":
        $ dk(1)
        $ ep10_riona_date = False
        mc "Stop toying with my brothers' emotions for my benefit."
        stop music fadeout 3
        scene ep10_rio_solo67b with dissolve
        ri "Sheesh. Fine."
        $ new_bio("Riona", "I told her to stop flirting with the DIKs to get my attention.")
        
        if ep10_dating_nora:
            jump ep10_nora_date_label
        
        
            
        if branchIsabella:
            jump ep10_bella_solo_label    
            
        if ep10_date_nicole and not ep10_cancel_date_nicole:
            jump ep10_nicole_date_label

        
        
        if ep10_date_nicole and not ep10_cancel_date_nicole:
            jump ep10_nicole_date_label
        elif ep10_dating_nora:
            jump ep10_nora_date_label
        else:
            jump ep10_science_label

scene ep10_rio_solo67 with dissolve
ri "Stuff. Nothing that sounded fun to me, so I came here instead."
ri "I don't like that I do what they want all the time, but they never do what I want."
scene ep10_rio_solo68 with dissolve
mc "Like what?"
scene ep10_rio_solo69 with dissolve
ri "I go on shopping trips with them and even help them figure out what to wear, but if I ask them to come to the arcade or something, they laugh and say no."
scene ep10_rio_solo68 with dissolve
mc "The arcade? Is that where you want to go?"
scene ep10_rio_solo67 with dissolve
ri "Yeah. The HOTs aren't that much into video games."
scene ep10_rio_solo68 with dissolve
mc "I could play some video games with you if you want."
scene ep10_rio_solo70 with dissolve
ri "You would?"
scene ep10_rio_solo68 with dissolve
mc "Hey, I'm free now too. How about it?"
scene ep10_rio_solo70 with dissolve
ri "Dude, you're gonna love it."
scene ep10_rio_solo71 with dissolve
stop music fadeout 3
if ep8_mansion_won:
    mc "Let me get Rusty's car keys and then you can tell me all about it."
else:
    mc "Tell me all about it."

if ep8_mansion_won:
    scene ep10_rio_solo1b with wipeleft
else:
    scene ep10_rio_solo1 with wipeleft
play sound "sound_effects/season3/arcade.mp3"
mc "Where do you even begin? There are so many different games..."
scene ep10_rio_solo2 with dissolve
ri "Right!? I hope you didn't bring too much money, because I usually leave here broke as hell."
play music "music/ep8/licensed_music/track88.mp3"
if ep8_mansion_won:
    scene ep10_rio_solo3b with dissolve
else:
    scene ep10_rio_solo3 with dissolve
mc "Is it always this loud in here? Machines are ringing everywhere."
if ep8_mansion_won:
    scene ep10_rio_solo4b with dissolve
else:
    scene ep10_rio_solo4 with dissolve
ri "If you think this is bad, you should go to Japan. Their arcades get even worse."

scene ep10_rio_solo5 with dissolve
gam1 "Aw, shoot. Those darn geese. I hate them."
scene ep10_rio_solo6 with dissolve
gam2 "Damn! I was this close to first place."
scene ep10_rio_solo7 with dissolve
gam1 "Wanna give this game a try?"
scene ep10_rio_solo6 with dissolve
gam2 "Does it have cars in it?"
scene ep10_rio_solo7 with dissolve
gam1 "No, but it has dinosaurs."
scene ep10_rio_solo6 with dissolve
gam2 "No cars, no quarter."
scene ep10_rio_solo8 with dissolve
gam2 "Hey! You're in my space!"
scene ep10_rio_solo9 with dissolve
mc "Sorry, I didn't realize I was standing that close."
scene ep10_rio_solo10 with dissolve
gam2 "That's why I put a license plate on the floor, dude."
scene ep10_rio_solo8 with dissolve
gam2 "Think of this area surrounding me as a virtual cockpit, if you will. Step out of my car and let me have my immersion."
scene ep10_rio_solo11 with dissolve
gam1 "Don't mind him. He gets invested in his car games. You two have a good day."
scene ep10_rio_solo12 with dissolve
ri "Let's go. Some of these guys are hardcore gamers. They attract every kind of player here."
scene ep10_rio_solo13 with dissolve
mc "So, what do you want to play?"
scene ep10_rio_solo14 with dissolve
ri "Hm... I wanna play this!"
mc "gUndead? I never heard of it."
scene ep10_rio_solo15 with dissolve
stop music fadeout 3
ri "Put in a quarter and grab a gun. It's time to slay some zombies!"
hide screen new_phone_screen
play music "music/ep10/licensed_music/track146.mp3"
scene ep10_rio_solo16 with dissolve
ri "Aim for the dead guys and avoid shooting the living."
scene ep10_rio_solo17 with dissolve
mc "Ok? How do I tell the difference?"
play sound "sound_effects/season3/zombie1.mp3"
scene bg anim_zombie_run_ep10 movie with dissolve
$ renpy.pause(1.167,hard=True)
scene ep10_rio_solo18 with vpunch
mc "Ahh!!!"
play sound "sound_effects/season3/gunshot.mp3"
"BLAM!"
scene bg anim_zombie_die_ep10 movie
show screen gundead_splat_screen
with vpunch
$ renpy.sound.play("sound_effects/season3/zombie2.mp3", channel="sfx2", loop=False)
play sound "sound_effects/season3/gunshot.mp3"
$ renpy.pause(1.67,hard=True)
hide screen gundead_splat_screen
$ renpy.block_rollback()
scene ep10_rio_solo19 with dissolve
ri "That was a dead one."
scene ep10_rio_solo20 with dissolve
mc "He looked like he was alive to me. Aside from the blood and all..."
$ _skipping = False
scene ep10_rio_solo19 with dissolve
ri "Don't overthink it! Just shoot!"
$ renpy.block_rollback()
$ mouse_visible = False
scene bg anim_civilian_ep10 movie
show screen gundead_screen
show screen gundead_screen_civ
with dissolve
$ renpy.pause(4.5)
hide screen gundead_screen
hide screen gundead_screen_civ
play sound "sound_effects/season3/gunshot.mp3"
scene bg anim_civilian_dead_ep10 movie
show screen gundead_splat2_screen
with vpunch
ri "No! What are you doing? You're killing innocent people."
hide screen gundead_splat2_screen
mc "Is anyone truly innocent? Maybe she did something bad, like shoplifted or forgot someone's birthday?"
ri "Haha! Be more careful!"
hide screen gundead_screen
$ mouse_visible = True
jump ep10_gundead_2_label

label ep10_gundead_civ_alive_label:
hide screen gundead_screen
$ mouse_visible = True
$ renpy.block_rollback()
scene ep10_rio_solo19 with dissolve
ri "Don't shoot! That's a civilian."
scene ep10_rio_solo20 with dissolve
mc "I saw it. *{i}Phew{/i}*"
jump ep10_gundead_2_label

label ep10_gundead_2_label:
scene ep10_rio_solo19 with dissolve
ri "Look alive, [name]! There are so many zombies coming for us!"
$ tmpList = [False,False,False,False,False]
$ renpy.block_rollback()
$ mouse_visible = False
scene bg anim_zombie_idle_ep10 movie
show screen gundead_screen
show screen gundead_screen_zombies
with dissolve
$ renpy.sound.play("sound_effects/season3/zombie3.mp3", channel="sfx2", loop=False)
$ renpy.sound.play("sound_effects/season3/zombie4.mp3", channel="sfx1", loop=False)
$ renpy.pause(3,hard=True)
$ renpy.sound.play("sound_effects/season3/zombie1.mp3", channel="sfx2", loop=False)
$ renpy.pause(2,hard=True)
$ renpy.sound.play("sound_effects/season3/zombie2.mp3", channel="sfx1", loop=False)
$ renpy.pause(1,hard=True)
$ renpy.sound.play("sound_effects/season3/zombie3.mp3", channel="sfx2", loop=False)
$ renpy.pause(2,hard=True)
$ renpy.sound.play("sound_effects/season3/zombie4.mp3", channel="sfx1", loop=False)
$ renpy.pause(2,hard=True)

label ep10_gundead_3_label:
$ mouse_visible = True
hide screen gundead_screen
hide screen gundead_screen_zombies
$ renpy.block_rollback()
if tmpList[0]:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_zombie_1 with vpunch
    $ renpy.pause(0.5)
if tmpList[1]:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_zombie_3 with vpunch
    $ renpy.pause(0.5)
if tmpList[2]:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_zombie_2 with vpunch
    $ renpy.pause(0.5)
if tmpList[3]:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_zombie_5 with vpunch
    $ renpy.pause(0.5)
if tmpList[4]:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_zombie_4 with vpunch
    $ renpy.pause(0.5)

if not False in tmpList:
    scene ep10_rio_solo21 with dissolve
    ri "Wow! You're a natural at this! How did you hit them that fast?"
    mc "I have no idea! I'm panicking, pointing and shooting!"
elif True in tmpList:
    scene ep10_rio_solo21 with dissolve
    ri "That's pretty good for your first time!"
    mc "Sorry, I wish I was better, but they are moving too fast!"
else:
    scene ep10_rio_solo22 with vpunch
    play sound "sound_effects/season3/gunshot.mp3"
    "BLAM BLAM BLAM!"
    play sound "sound_effects/season3/gunshot.mp3"
    ri "I'm on fire! WOHO! Take that, assface!"


$ renpy.sound.play("sound_effects/door_break.mp3", channel="sfx2", loop=False)
$ renpy.sound.play("sound_effects/season3/zombie3.mp3", channel="sfx1", loop=False)
scene bg anim_boss_ep10 movie with vpunch
$ renpy.pause(2.33,hard=True)
scene ep10_rio_solo24 with dissolve
ri "Oh, no! Big boss time! I'm reloading here. [name], do something!"
$ renpy.block_rollback()
$ tmpInt = 0
$ mouse_visible = False
$ renpy.sound.play("sound_effects/season3/zombie3.mp3", channel="sfx1", loop=False)
scene bg anim_boss_idle_ep10 movie
show screen gundead_screen
show screen gundead_screen_boss
with dissolve
$ renpy.pause(3.33, hard=True)
hide screen gundead_screen
hide screen gundead_screen_boss
$ mouse_visible = True
$ renpy.block_rollback()
$ _skipping = True
if tmpInt > 3:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_rio_solo20 with dissolve
    mc "I'm shooting her in the head, but it's doing nothing! Help!!!"
    scene ep10_boss_dead with vpunch
    $ renpy.sound.play("sound_effects/season3/zombie2.mp3", channel="sfx1", loop=False)
    play sound "sound_effects/season3/gunshot.mp3"
    show screen gundead_screen_win
    ri "You did it! Yes!!! We won!"
    scene ep10_rio_solo23
    hide screen gundead_screen_win
    stop music fadeout 3
    with dissolve
    $ ep10_gundead_win = True
    mc "We did?"
    scene ep10_rio_solo26 with dissolve
    ri "Yes! We did!"
    scene ep10_rio_solo25 with dissolve
    ri "Let's play something else."
else:
    play sound "sound_effects/season3/gunshot.mp3"
    scene ep10_rio_solo24 with dissolve
    ri "Your aim is way off, [name]!!!"
    scene ep10_boss_kill with vpunch
    $ renpy.sound.play("sound_effects/season3/zombie3.mp3", channel="sfx1", loop=False)
    show screen gundead_screen_loss
    ri "Aw! We lost!"
    scene ep10_rio_solo23
    hide screen gundead_screen_loss
    stop music fadeout 3
    with dissolve
    $ ep10_gundead_win = False
    mc "Sorry... That was my fault."
    scene ep10_rio_solo25 with dissolve
    ri "It's a hard game, don't worry about it."
    ri "Let's play something else."

show screen new_phone_screen
play music "music/ep8/licensed_music/track88.mp3"

scene ep10_rio_solo27 with dissolve
ri "Oh, look. Those animals are so cute."
scene ep10_rio_solo28 with dissolve
ri "Too bad they're stuck inside of a rigged machine."
scene ep10_rio_solo29 with dissolve
mc "You can win at these things. I've done it before."
scene ep10_rio_solo30 with dissolve
ri "Nah, you'd end up wasting your money on it. Trust me."
scene ep10_rio_solo29 with dissolve
show screen newmoneymsg
hide screen new_phone_screen

if persistent.mod_wt_enabled: 
                    $mod_choices = ["(Riona date)","(+Josy)","(-DIK)","(+DIK)","(-Maya)","(-Josy)","","","","","","" ]
                    #[m_c1][mod_choices[0]]

menu:
    "[m_c1]Give it a try ({color=#36ca2b}$1{/color})" if money >= 1:
        $ mny(-1)
        $ renpy.pause(1)
        hide screen newmoneymsg
        mc "Hold on there, Rio. Let me try it."
        scene ep10_rio_solo30 with dissolve
        ri "Save your money for another game, [name]. We could play something fun instead."
        scene ep10_rio_solo31 with dissolve
        play sound "sound_effects/season2/coins.mp3"
        mc "I wanna get you something to remember the day by."
        $ renpy.block_rollback()
        scene ep10_grab_machine
        call screen claw_machine_screen
        $ renpy.block_rollback()
        $ renpy.music.stop(channel="sfx1")
        if True:
            jump ep10_claw_success_label
        scene bg anim_failed_grab_ep10 movie with dissolve
        play sound "sound_effects/season3/claw_machine_short.mp3"
        mc "Come on! Get it!"
        mc "Crap! That claw is so weak!"
        ri "I told you this would happen. Come on, let's go."
        menu:
            "[m_c1]Give it one more try":
                play sound "sound_effects/season2/coins.mp3"
                mc "No, no. I'm getting used to how it works. It usually takes a couple of tries to get it."
                scene ep10_rio_solo32 with dissolve
                ri "To get what? A gambling addiction?"
                ri "You're not getting an animal, [name]."
                $ claw_offset = [-600,0]
                $ renpy.block_rollback()
                scene ep10_grab_machine
                call screen claw_machine_screen
                $ renpy.block_rollback()
                $ renpy.music.stop(channel="sfx1")
                if True:
                    jump ep10_claw_success_label
                scene bg anim_failed_grab_ep10 movie with dissolve
                play sound "sound_effects/season3/claw_machine_short.mp3"
                mc "Aw! Come on! I was {b}this{/b} close!"
                ri "That's how it gets you. I bet it made you want to try again."
                menu:
                    "[m_c1]Give it one more try":
                        play sound "sound_effects/season2/coins.mp3"
                        mc "You bet your ass it did."
                        scene ep10_rio_solo32 with dissolve
                        ri "Even if you win, it would be cheaper to buy one of those animals from a store."
                        scene ep10_rio_solo33 with dissolve
                        mc "Yeah, yeah. Make fun of me all you want. I'm not leaving here until I get you a nice and fluffy animal!"
                        $ claw_offset = [-600,0]
                        $ renpy.block_rollback()
                        scene ep10_grab_machine
                        call screen claw_machine_screen
                        $ renpy.block_rollback()
                        $ renpy.music.stop(channel="sfx1")

                        label ep10_claw_success_label:
                        $ ep10_rio_animal = True
                        scene bg anim_success_grab_ep10 movie with dissolve
                        play sound "sound_effects/season3/claw_machine_short.mp3"
                        mc "Yes! Look! Rio! Look!"
                        ri "No way!"
                        mc "Haha! I told you I would win!"
                        scene ep10_rio_solo34 with dissolve
                        mc "I fucking told...you..."
                        mc "Well, this is the ugliest thing I've ever seen in my life."
                        scene ep10_rio_solo35 with dissolve
                        ri "Hahaha! What even is that?"
                        scene ep10_rio_solo36 with dissolve
                        mc "I'm sorry, Rio. I tried."
                        scene ep10_rio_solo35 with dissolve
                        ri "Hahaha! I love it!"
                        scene ep10_rio_solo37 with dissolve
                        ri "Thank you, [name]. *{i}Smack{/i}*"
                        scene ep10_rio_solo38 with dissolve
                        ri "I'm going to call it Mini-[name]."
                        scene ep10_rio_solo40 with dissolve
                        mc "If I had a kid, it wouldn't be that ugly."
                        scene ep10_rio_solo39 with dissolve
                        ri "Unless you fucked a goat or something. Hahaha!"
                    "Stop playing":
                        hide screen newmoneymsg
                        mc "No. I'm not letting it get inside my head like that. I'm done."
            "Stop playing":
                hide screen newmoneymsg
                mc "I should have listened the first time. Oh, well. It was worth a shot."
    "Don't bother":
        hide screen newmoneymsg
        mc "Yeah, you're right. Let's spend it on something else instead."

show screen new_phone_screen
if ep10_rio_animal:
    scene ep10_rio_solo41 with wipeleft
else:
    scene ep10_rio_solo41b with wipeleft
play sound "sound_effects/season3/arcade.mp3"
mc "This is a fun place. I can't believe no one wanted to come here with you."
if ep10_rio_animal:
    scene ep10_rio_solo42 with dissolve
else:
    scene ep10_rio_solo42b with dissolve
ri "None of the HOTs, anyway. But it's ok. I've had a blast here with you today."
if ep10_rio_animal:
    scene ep10_rio_solo41 with dissolve
else:
    scene ep10_rio_solo41b with dissolve
mc "Me too. I'm happy we did this."
if ep10_rio_animal:
    scene ep10_rio_solo42 with dissolve
else:
    scene ep10_rio_solo42b with dissolve
ri "And to think all it took was to flirt with some guys to get you to come here."
scene ep10_rio_solo43 with dissolve
mc "You didn't have to do that. Say you want to go on a date next time."
scene ep10_rio_solo44 with dissolve
ri "Go out on a date? Who says that these days?"
scene ep10_rio_solo43 with dissolve
mc "That's what this was."
scene ep10_rio_solo44 with dissolve
if ep10_rio_animal:
    ri "Nah. We hung out, chatted, played some games and had a buncha fun together. And you won me a stuffed animal."
else:
    ri "Nah. We hung out, chatted, played some games and had a buncha fun together."
if ep8_mansion_won:
    scene ep10_rio_solo45b with dissolve
else:
    scene ep10_rio_solo45 with dissolve
ri "Holy crap, this was a date!"
mc "I told you."
scene ep10_rio_solo44 with dissolve
ri "Wait! We didn't eat. Then, it's not a date."
scene ep10_rio_solo43 with dissolve
mc "Come on, you don't have to eat on a date. A date can be a simple walk."
scene ep10_rio_solo46 with dissolve
ri "Nope. Unless you eat, it's not a date."
scene ep10_rio_solo47 with dissolve
mc "Want a gum?"
scene ep10_rio_solo48 with dissolve
ri "Yes. But gum isn't food."
if ep8_mansion_won:
    scene ep10_rio_solo49 with dissolve
else:
    scene ep10_rio_solo49b with dissolve
mc "It is if you swallow it."
if ep8_mansion_won:
    scene ep10_rio_solo50b with dissolve
else:
    scene ep10_rio_solo50 with dissolve
ri "Haha! Ok, I'm not eating this."
ri "Wanna head back?"
if ep8_mansion_won:
    scene ep10_rio_solo49 with dissolve
else:
    scene ep10_rio_solo49b with dissolve
mc "Yeah, I ran out of quarters a while ago. I've been pretending to push the buttons while you played."
if ep8_mansion_won:
    if ep10_rio_animal:
        scene ep10_rio_solo51b with dissolve
    else:
        scene ep10_rio_solo51 with dissolve
else:
    if ep10_rio_animal:
        scene ep10_rio_solo51c with dissolve
    else:
        scene ep10_rio_solo51d with dissolve
ri "Haha, yeah. I saw. I found it kinda cute."
if ep10_rio_animal:
    scene ep10_rio_solo52 with fade
else:
    scene ep10_rio_solo52b with fade
mc "Don't you want me to walk you back home? It's not a problem."
scene ep10_rio_solo53 with dissolve
ri "No, that would make it feel too much like a date."
scene ep10_rio_solo54 with dissolve
mc "Yeah, haha. Sure."
scene ep10_rio_solo53 with dissolve
ri "Guess I'll see you another time."
scene ep10_rio_solo54 with dissolve
mc "Yeah. Just flirt with Rusty to let me know when, ok?"
scene ep10_rio_solo53 with dissolve
ri "Haha! See you, [name]."
if ep10_rio_animal:
    scene ep10_rio_solo55 with dissolve
else:
    scene ep10_rio_solo55b with dissolve
$ renpy.pause()
if notifications:
    play sound mphone_notifications[current_notification_sound][1]
scene ep10_rio_solo56 with dissolve
stop music fadeout 5
"*{i}Text message{/i}*"
$ tmpInt = 0
$ tmpInt2 = 0
$ text_message_screen_list = []
if ep10_rio_animal:
    $ text_message_screen_list.append(["Riona","Mini-[name] says thanks for the date. mphone_emoji_kiss",True])
    $ text_message_screen_list.append(["Riona","chat_rio_pic1b_ep10_thumb",True])
else:
    $ text_message_screen_list.append(["Riona","Thanks for the date. mphone_emoji_kiss",True])
    $ text_message_screen_list.append(["Riona","chat_rio_pic1_ep10_thumb",True])
$ text_message_screen_list.append(["%s" % name,"I had a great time today. Thanks, Rio. mphone_emoji_heart",False])
hide screen new_phone_screen
scene ep10_rio_solo57 with dissolve
show screen text_message_screen
$ renpy.pause()
play sound "sound_effects/interlude/zoey_message.mp3"
$ tmpInt += 1
$ renpy.pause()
$ tmpInt += 1
$ renpy.pause()
hide screen text_message_screen
$ mphone_scene_to_chat("Riona",text_message_screen_list)
$ new_bio("Riona", "We spent the day at the arcade together. It was a fun date, but she didn't realize it was one until I pointed it out to her.")
$ mgallery_add_photo("ep10_rio_date_pic1")
if ep10_rio_animal:
    $ mgallery_add_photo("chat_rio_pic1b_ep10_zoomed")
else:
    $ mgallery_add_photo("chat_rio_pic1_ep10_zoomed")
show screen new_phone_screen


    

if ep10_dating_nora:
    jump ep10_nora_date_label
    
if branchIsabella:
    jump ep10_bella_solo_label    

    
if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label


if ep10_date_nicole and not ep10_cancel_date_nicole:
    jump ep10_nicole_date_label
elif ep10_dating_nora:
    jump ep10_nora_date_label

jump ep10_science_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
